"""Read and edit the mouse sensitivity stored in profile.bin.

Mouse sensitivity is entry id=121: an Int32 (4-byte big-endian) inside the
LZO-compressed entry stream. Editing decompresses, patches that value, recompresses,
and re-hashes so only the value changes and the file stays valid. This is far more
reliable than patching a byte inside the compression stream.
"""

import hashlib
import struct
from pathlib import Path

import lzokay

from util import try_input

SENSITIVITY_ID = 121


def _decompress(body: bytes) -> bytearray:
    """body = [4-byte BE uncompressed size][LZO1X]; return the entry stream."""
    (uncompressed_size,) = struct.unpack(">I", body[:4])
    return bytearray(lzokay.decompress(body[4:], uncompressed_size))


def _compress(stream: bytearray) -> bytes:
    """Entry stream -> [4-byte BE uncompressed size][LZO1X]."""
    return struct.pack(">I", len(stream)) + lzokay.compress(bytes(stream))


def _find_value_span(stream: bytearray, target_id: int) -> tuple[int, int]:
    """Locate an entry's value bytes within the entry stream. Returns (offset, length)."""
    (entry_count,) = struct.unpack(">I", stream[:4])
    pos = 4
    for _ in range(entry_count):
        indicator = stream[pos]
        pos += 1
        if indicator == 0:  # broken entry: fixed 6 bytes, no fields
            pos += 6
            continue
        (entry_id,) = struct.unpack(">i", stream[pos:pos + 4])
        pos += 4
        data_type = stream[pos]
        pos += 1
        if data_type == 1 or data_type == 5:  # Int32 / Float
            value_length = 4
        elif data_type == 4 or data_type == 6:  # String / Binary: 4-byte length prefix
            (value_length,) = struct.unpack(">I", stream[pos:pos + 4])
            pos += 4
        elif data_type == 8:  # Int8
            value_length = 1
        else:
            raise ValueError(f"Unknown profile entry data type {data_type}")
        value_offset = pos
        pos += value_length
        if entry_id == target_id:
            return value_offset, value_length
        pos += 1  # separation byte
    raise KeyError(f"profile entry id {target_id} not found")


def _load_body(profile_path: str | Path) -> bytes:
    return Path(profile_path).read_bytes()[20:]


def read_sens(profile_path: str | Path) -> int:
    stream = _decompress(_load_body(profile_path))
    offset, _ = _find_value_span(stream, SENSITIVITY_ID)
    return struct.unpack(">I", stream[offset:offset + 4])[0]


def _patch_and_save(profile_path: str | Path, value: int) -> None:
    body = _load_body(profile_path)
    stream = _decompress(body)
    offset, _ = _find_value_span(stream, SENSITIVITY_ID)
    stream[offset:offset + 4] = struct.pack(">I", value)
    body = _compress(stream)
    Path(profile_path).write_bytes(hashlib.sha1(body).digest() + body)


def write_sens(profile_path: str | Path) -> int:
    value = try_input(int, prompt="\nEnter your new desired sensitivity (1-255): ")
    _patch_and_save(profile_path, value)
    print(
        "\nDone! Restart the game, check the mouse settings, and enjoy your newly configured sensitivity."
    )
    print(
        "\nWARNING: Next time you launch the game, select your LOCAL save, not the cloud "
        "save. If prompted, overwrite the cloud save with your local save."
    )
    return value


def all_profiles(profile_path: str | Path) -> list[Path]:
    """Every profile.bin under the SaveData root, most-recent first, then the rest."""
    primary = Path(profile_path)
    root = primary.parent.parent
    found = [p for p in root.rglob("profile.bin") if p.is_file()]
    return [primary] + [p for p in found if p != primary]


def _try_read_sens(profile_path: str | Path) -> int | None:
    try:
        return read_sens(profile_path)
    except Exception:
        return None


def find_active_profile(profile_path: str | Path) -> Path:
    """Find the profile the game actually writes by watching which one's
    sensitivity changes (the fallback differential)."""
    profiles = all_profiles(profile_path)
    while True:
        before = {p: _try_read_sens(p) for p in profiles}
        input(
            "\nTo find your active profile: in your game, change mouse sensitivity to a "
            "new value and exit to the main menu.\nPress enter once you are done. "
        )
        changed = [p for p in profiles if before[p] != _try_read_sens(p)]
        if len(changed) == 1:
            print(f"\nActive profile: {changed[0]}")
            return changed[0]
        print(f"\nDetected {len(changed)} changed profiles (expected exactly 1). Try again.")
