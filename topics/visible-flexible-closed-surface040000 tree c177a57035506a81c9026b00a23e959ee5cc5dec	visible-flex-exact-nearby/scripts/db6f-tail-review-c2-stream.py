#!/usr/bin/env python3
"""Independent small exact-index check for the C2 storage adapter only."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Bounds:
    def __init__(self, lo, hi):
        self.lo, self.hi = np.array(lo), np.array(hi)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    target = Path(__file__).with_name('db6f-prefix-tail-c2-stream.py')
    tree = ast.parse(target.read_text())
    fn = next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == 'main')
    classes = [x for x in fn.body if isinstance(x, ast.ClassDef) and
               x.name in ['BatchPolynomials', 'OrderView']]
    assert len(classes) == 2
    planar = np.array([-11, -8, -5, -2, 1, 4, 7, 10])
    height = np.array([0, 3, 6, 9, 12])
    P, C = len(planar), len(planar)+len(height)
    namespace = dict(np=np, planar=planar, height=height, P=P, C=C,
                     backend=SimpleNamespace(I=Bounds))
    exec(compile(ast.Module(body=classes, type_ignores=[]), str(target), 'exec'), namespace)

    class FakeGeometry:
        def __init__(self, pm, hm):
            self.reader = SimpleNamespace(planar_modes=np.array(pm), height_modes=np.array(hm))
            self.count = len(pm)+len(hm)

        def span_polys(self, index):
            return [Bounds(np.arange((6-j)*self.count).reshape(6-j, self.count)
                           +10000*index+1000*j,
                           np.arange((6-j)*self.count).reshape(6-j, self.count)
                           +10000*index+1000*j+.5) for j in range(3)]

    cases = [FakeGeometry([-8, -2, 1, 10], [0, 3, 9]),
             FakeGeometry([-11, -5, 1, 4, 7], [0, 6, 12])]
    compared = zeros = 0
    for geom in cases:
        batch = namespace['BatchPolynomials'](geom)
        slots = [int(np.flatnonzero(planar == m)[0]) for m in geom.reader.planar_modes]
        slots += [P+int(np.flatnonzero(height == m)[0]) for m in geom.reader.height_modes]
        for indices in [np.array([1, 0, 1]), np.array([2]), np.array([2])]:
            for order in range(3):
                got = namespace['OrderView'](batch, order)[indices]
                assert got.lo.shape == got.hi.shape == (len(indices), C, 6-order)
                for row, index in enumerate(indices):
                    expected = geom.span_polys(int(index))[order]
                    for slot in range(C):
                        for side in ['lo', 'hi']:
                            actual = getattr(got, side)[row, slot]
                            if slot in slots:
                                want = getattr(expected, side)[:, slots.index(slot)]
                                assert np.array_equal(actual, want)
                                compared += len(actual)
                            else:
                                assert np.array_equal(actual, np.zeros_like(actual))
                                zeros += len(actual)
    result = dict(status='independent-storage-axis-and-zero-extension-check-pass',
                  target_file=str(target), target_sha256=sha(target),
                  script_sha256=sha(__file__), copied_endpoint_values=compared,
                  exact_zero_values=zeros,
                  scope='Synthetic exact-index checks of source-extracted BatchPolynomials and OrderView only; no metric, source ODE, infinite-tail or whole-comparison certificate.')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status', 'copied_endpoint_values', 'exact_zero_values']}))


if __name__ == '__main__':
    main()
