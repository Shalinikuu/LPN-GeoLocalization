"""File and configuration hashing utilities."""

from pathlib import Path
import hashlib
import json


def sha256_file(file_path, chunk_size=1024 * 1024):
    file_path = Path(file_path)
    digest = hashlib.sha256()

    with file_path.open("rb") as file:
        while True:
            chunk = file.read(chunk_size)

            if not chunk:
                break

            digest.update(chunk)

    return digest.hexdigest()


def sha256_json(data):
    serialized = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    return hashlib.sha256(
        serialized
    ).hexdigest()
