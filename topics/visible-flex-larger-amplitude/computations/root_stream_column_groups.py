#!/usr/bin/env python3
"""Stream complete, hash-bound JSON column groups one physical cell at a time.

Only storage is changed. Every number is decoded by the same standard JSON
decoder; no mathematical field is transformed or discarded inside a cell.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import gzip
import json


class Reader:
    def __init__(self, stream):
        self.stream = stream
        self.buffer = ""
        self.position = 0
        self.eof = False
        self.decoder = json.JSONDecoder()

    def more(self):
        self.buffer = self.buffer[self.position:]
        self.position = 0
        chunk = self.stream.read(65536)
        self.buffer += chunk
        self.eof = not bool(chunk)

    def peek(self):
        while True:
            while self.position < len(self.buffer) and self.buffer[self.position].isspace():
                self.position += 1
            if self.position < len(self.buffer):
                return self.buffer[self.position]
            if self.eof:
                return ""
            self.more()

    def expect(self, token):
        if self.peek() != token:
            raise ValueError("Unexpected JSON structure while streaming columns")
        self.position += 1

    def value(self):
        if not self.peek():
            raise ValueError("Unexpected end of the saved column group")
        while True:
            try:
                result, end = self.decoder.raw_decode(self.buffer, self.position)
                self.position = end
                return result
            except json.JSONDecodeError:
                if self.eof:
                    raise
                self.more()


def iter_group_cells(path, expected_modes):
    with (gzip.open(path, "rt") if str(path).endswith(".gz") else open(path)) as stream:
        reader = Reader(stream)
        reader.expect("{")
        saw_modes = saw_rows = False
        row_count = 0
        while reader.peek() != "}":
            key = reader.value()
            if not isinstance(key, str):
                raise ValueError("A top-level JSON key was not a string")
            reader.expect(":")
            if key == "cell_rows":
                if saw_rows:
                    raise ValueError("Duplicate physical cell array")
                saw_rows = True
                reader.expect("[")
                while reader.peek() != "]":
                    row = reader.value()
                    if not isinstance(row, dict) or row.get("cell") != 12+row_count:
                        raise ValueError("A physical cell was omitted or reordered")
                    row_count += 1
                    yield row
                    if reader.peek() == ",":
                        reader.expect(",")
                    elif reader.peek() != "]":
                        raise ValueError("Malformed physical cell separator")
                reader.expect("]")
            else:
                value = reader.value()
                if key == "modes":
                    if saw_modes or value != expected_modes:
                        raise ValueError("The saved column-group modes differ")
                    saw_modes = True
            if reader.peek() == ",":
                reader.expect(",")
            elif reader.peek() != "}":
                raise ValueError("Malformed column-group separator")
        reader.expect("}")
        if reader.peek() or not saw_modes or not saw_rows or row_count != 213:
            raise ValueError("The entire original column group was not consumed")
