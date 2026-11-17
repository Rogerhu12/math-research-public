#!/usr/bin/env python3
"""Volume inertia of a closed oriented triangular OBJ, with optional exact arithmetic.

This integrates the piecewise linear mesh itself. It supplies no bound between
that mesh and any smooth surface. No files are written. See the companion
2026-11-17-parallel-geometry-second-moment.md, equations (20)--(21).
"""

import argparse
from collections import defaultdict
from fractions import Fraction
import json
import math
from pathlib import Path


class Accumulator:
    def __init__(self, exact):
        self.exact = exact
        self.value = Fraction(0) if exact else 0.0
        self.correction = 0.0

    def add(self, x):
        if self.exact:
            self.value += x
            return
        result = self.value + x
        if abs(self.value) >= abs(x):
            self.correction += (self.value - result) + x
        else:
            self.correction += (x - result) + self.value
        self.value = result

    def total(self):
        return self.value if self.exact else self.value + self.correction


def read_obj(path, exact):
    scalar = Fraction if exact else float
    vertices = []
    faces = []
    with Path(path).open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            words = line.split()
            if not words or words[0].startswith("#"):
                continue
            if words[0] == "v":
                if len(words) != 4:
                    raise ValueError(f"Line {line_number}: expected three vertex coordinates")
                vertex = tuple(scalar(word) for word in words[1:])
                if not exact and not all(math.isfinite(x) for x in vertex):
                    raise ValueError(f"Line {line_number}: nonfinite vertex")
                vertices.append(vertex)
            elif words[0] == "f":
                if len(words) != 4:
                    raise ValueError(f"Line {line_number}: only triangular faces are supported")
                face = []
                for word in words[1:]:
                    index = int(word.split("/", 1)[0])
                    index = index - 1 if index > 0 else len(vertices) + index
                    if not 0 <= index < len(vertices):
                        raise ValueError(f"Line {line_number}: unavailable vertex index")
                    face.append(index)
                if len(set(face)) != 3:
                    raise ValueError(f"Line {line_number}: repeated vertex in a triangle")
                faces.append(tuple(face))
    if not vertices or not faces:
        raise ValueError("Mesh has no vertices or no triangular faces")
    return vertices, faces


def closed_edge_check(faces):
    counts = defaultdict(lambda: [0, 0])
    for face in faces:
        for first, second in zip(face, face[1:] + face[:1]):
            key = (min(first, second), max(first, second))
            counts[key][0] += 1
            counts[key][1] += 1 if first < second else -1
    bad = [key for key, (count, balance) in counts.items()
           if count != 2 or balance != 0]
    if bad:
        raise ValueError(f"Mesh is not closed and consistently oriented: {len(bad)} bad edges")
    return len(counts)


def mesh_moments(vertices, faces, exact=False):
    edge_count = closed_edge_check(faces)
    zero = Fraction(0) if exact else 0.0
    bounds_min = [min(vertex[i] for vertex in vertices) for i in range(3)]
    bounds_max = [max(vertex[i] for vertex in vertices) for i in range(3)]
    # A nearby origin reduces floating cancellation. Raw moments are restored below.
    origin = [(bounds_min[i] + bounds_max[i]) / 2 for i in range(3)]
    shifted = [tuple(vertex[i] - origin[i] for i in range(3))
               for vertex in vertices]
    pairs = [(i, j) for i in range(3) for j in range(i, 3)]
    sums = [Accumulator(exact) for _ in range(10)]
    for face in faces:
        a, b, c = (shifted[index] for index in face)
        determinant = (a[0] * (b[1] * c[2] - b[2] * c[1])
                       - a[1] * (b[0] * c[2] - b[2] * c[0])
                       + a[2] * (b[0] * c[1] - b[1] * c[0]))
        volume = determinant / 6
        s = [a[i] + b[i] + c[i] for i in range(3)]
        sums[0].add(volume)
        for i in range(3):
            sums[1 + i].add(volume * s[i] / 4)
        for index, (i, j) in enumerate(pairs):
            sums[4 + index].add(volume * (s[i] * s[j] + a[i] * a[j]
                                         + b[i] * b[j] + c[i] * c[j]) / 20)
    totals = [acc.total() for acc in sums]
    volume, first = totals[0], totals[1:4]
    if volume <= 0:
        raise ValueError("Signed volume is nonpositive; outward orientation is required")
    raw = [[zero for _ in range(3)] for _ in range(3)]
    centered = [[zero for _ in range(3)] for _ in range(3)]
    for index, (i, j) in enumerate(pairs):
        q = totals[4 + index]
        centered[i][j] = centered[j][i] = q - first[i] * first[j] / volume
        restored = q + origin[i] * first[j] + origin[j] * first[i]
        restored += volume * origin[i] * origin[j]
        raw[i][j] = raw[j][i] = restored
    center = [origin[i] + first[i] / volume for i in range(3)]
    norm_squared = sum((entry * entry for row in centered for entry in row), zero)
    return {
        "object": "oriented piecewise linear mesh; no smooth-surface error bound",
        "arithmetic": "exact rational OBJ coordinates" if exact else "binary64 compensated sums; not a validated enclosure",
        "vertices": len(vertices),
        "triangles": len(faces),
        "closed_oriented_edges": edge_count,
        "embeddedness": "not checked by the moment integral",
        "signed_volume": volume,
        "centroid": center,
        "raw_second_moment": raw,
        "centered_second_moment": centered,
        "invariant_frobenius_squared": norm_squared,
        "A2_about_original_z_axis": [raw[0][0] - raw[1][1], 2 * raw[0][1]],
        "bbox_diagonal_squared": sum(((bounds_max[i] - bounds_min[i]) ** 2 for i in range(3)), zero),
    }


def json_scalar(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("obj", type=Path)
    parser.add_argument("--exact", action="store_true",
                        help="Integrate the decimal OBJ coordinates as exact rationals")
    args = parser.parse_args()
    vertices, faces = read_obj(args.obj, args.exact)
    print(json.dumps(mesh_moments(vertices, faces, args.exact),
                     default=json_scalar, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
