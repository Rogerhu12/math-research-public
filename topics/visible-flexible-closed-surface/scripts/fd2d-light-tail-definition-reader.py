"""Minimal checked binary reader for the strict streaming tail verifier.

The original numerical IntegratedTail additionally constructs approximate
long-double node values and retains all diagnostic source-position rows.
The exact streaming verifier uses neither. This reader retains the exact
same binary derivative arrays, first value and radial increments, checking
each complete raw shard and shared boundary before releasing that shard.
It is intentionally NOT a general replacement for the numerical reader.
"""
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np


class CheckedTailDefinition:
    def __init__(self, manifest):
        self.manifest_path = Path(manifest)
        self.meta = json.loads(self.manifest_path.read_text())
        if self.meta['status'] not in ('finite-C2-integrated-explicit-tail-with-sampled-audit',
                                       'finite-C2-increment-integrated-explicit-tail-with-sampled-audit'):
            raise ValueError('Wrong actual integrated-tail format')
        if not self.meta.get('finished'):
            raise ValueError('Incomplete actual tail definition')
        fmt = self.meta['format']
        self.planar_modes = np.array(fmt['planarModes'], dtype=int)
        self.height_modes = np.array(fmt['heightModes'], dtype=int)
        self.P, self.C = len(self.planar_modes), fmt['coefficientCount']
        if self.C != self.P+len(self.height_modes):
            raise ValueError('Inconsistent tail coefficient count')
        files = self.meta['files']
        if not files:
            raise ValueError('No actual raw tail shards')
        count = sum(info['rows'] for info in files)-len(files)+1
        if count < 2:
            raise ValueError('The tail has no span')
        # Only the radial column is needed through reader.nodes by the exact
        # streaming verifier; every raw column is still checked below.
        self.nodes = np.empty((count, 1), dtype=np.float64)
        self.first = np.empty((count, self.C), dtype=np.float64)
        self.second = np.empty_like(self.first)
        self.midpoint = np.empty((count-1, self.C), dtype=np.float64)
        self.source_values = np.empty((1, self.C), dtype=np.float64)
        has_increments = 'radialGeometry' in self.meta
        increments = np.empty(count, dtype=np.float64) if has_increments else None
        previous, cursor = None, 0
        expected_columns = 2+4*self.C+int(has_increments)
        self.checked_raw_shards = []
        for info in files:
            path = Path(info['path'])
            if not path.exists():
                path = self.manifest_path.parent/path.name
            encoded = path.read_bytes()
            digest = hashlib.sha256(encoded).hexdigest()
            if digest != info['sha256'] or info['columns'] != expected_columns:
                raise ValueError('Changed raw tail shard or column layout: '+str(path))
            raw = gzip.decompress(encoded)
            values = np.frombuffer(raw, dtype='<f8').reshape(info['rows'], info['columns'])
            if not np.isfinite(values).all():
                raise ValueError('Nonfinite raw tail definition')
            start = 0
            if previous is not None:
                if not np.array_equal(values[0], previous):
                    raise ValueError('Actual raw tail interface rows differ')
                start = 1
            block = values[start:]
            stop = cursor+len(block)
            jets = block[:, 2:2+4*self.C].reshape(len(block), 4, self.C)
            self.nodes[cursor:stop, 0] = block[:, 0]
            self.first[cursor:stop] = jets[:, 1]
            self.second[cursor:stop] = jets[:, 2]
            if cursor == 0:
                self.source_values[0] = jets[0, 0]
                self.midpoint[:stop-1] = jets[1:, 3]
            else:
                self.midpoint[cursor-1:stop-1] = jets[:, 3]
            if has_increments:
                increments[cursor:stop] = block[:, -1]
            previous = values[-1].copy()
            cursor = stop
            self.checked_raw_shards.append(dict(file=str(path.resolve()), sha256=digest,
                                                rows=info['rows'], columns=info['columns']))
            del block, jets, values, raw, encoded
        if cursor != count:
            raise ValueError('Actual tail row count changed')
        if has_increments:
            radial = self.meta['radialGeometry']
            self.unscaled_lengths = increments[1:].copy()
            self.radial_scale = Fraction(int(radial['normalization']['numerator']),
                                        int(radial['normalization']['denominator']))
            if self.radial_scale <= 0 or np.any(self.unscaled_lengths <= 0):
                raise ValueError('Nonpositive exact defining radial increments')
        else:
            self.unscaled_lengths = None
            self.radial_scale = Fraction(1)
            if np.any(np.diff(self.nodes[:, 0]) <= 0):
                raise ValueError('Nonpositive physical radial spans')
