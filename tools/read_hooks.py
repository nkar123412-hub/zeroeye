from __future__ import annotations
from pathlib import Path
from typing import Protocol, runtime_checkable
import logging

logger = logging.getLogger("read_hooks")

@runtime_checkable
class ReadToolHook(Protocol):
    """
    Protocol for a read tool hook that allows intercepting or 
    customizing how source code is read from a path.
    """
    def read(self, path: Path) -> str:
        ...

class DefaultFileSystemReader:
    """Standard reader that reads files directly from the disk."""
    def read(self, path: Path) -> str:
        logger.debug(f"Reading file from disk: {path}")
        return path.read_text(encoding="utf-8", errors="replace")

class LoggingReadHook(ReadToolHook):
    """A hook that logs the reading process and can be used for auditing."""
    def __init__(self, base_reader: ReadToolHook):
        self.base_reader = base_reader

    def read(self, path: Path) -> str:
        logger.info(f"Hook intercepting read request for: {path}")
        content = self.base_reader.read(path)
        logger.info(f"Read {len(content)} characters from {path}")
        return content
