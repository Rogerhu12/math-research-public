#!/usr/bin/env python3
"""Check append-only mathematical input while a controller replays its index.

A shorter, unchanged observed prefix is not new evidence and is never used to
publish a certificate.  A follower may wait for it to catch up.  Any changed
overlapping entry, or a shortened index claiming completion, is rejected.
"""


def observed_prefix_ready(observed, processed, *, complete=False):
    overlap = min(len(observed), len(processed))
    if observed[:overlap] != processed[:overlap]:
        raise ValueError("a previously accumulated source prefix changed")
    if len(observed) < len(processed):
        if complete:
            raise ValueError("a complete source index removed accumulated leaves")
        return False
    return True
