"""Check E/P boundary differentiation, including both scalar mean rows.

Small linear response with exactly representable binary data; no DN or BVP.
The forward view is differentiated independently of its supplied Jacobian.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

T = Path(__file__).resolve().parent.parent
source = T/'scripts/78718-prefix-projected-tail.py'
spec = importlib.util.spec_from_file_location('projected_tail_check', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
rows = []
for M, W in ((3,5), (15,22), (22,22)):
    matrix = (np.arange((3*W+2)*W).reshape(3*W+2,W) % 13-6).astype(float)
    h = np.arange(M, dtype=float)/16
    class FullLinearPort:
        M = W
        linearD = np.arange(W, dtype=float)
        def solve(self, x, jacobian=True, audit=False):
            assert np.asarray(x).shape == (W,) and np.all(x[M:] == 0)
            z = matrix@x
            return {'jets': {'slope': z[:W].tolist(), 'second': z[W:2*W].tolist(),
                    'meanSlope': float(z[2*W]), 'meanSecond': float(z[2*W+1]),
                    'height': z[2*W+2:].tolist(), 'E': 4.},
                    'heightJetJacobian': matrix.ravel().tolist() if jacobian else None}
    view = module.ProjectedTailPort(FullLinearPort(), M)
    def vector(response):
        j = response['jets']
        return np.r_[j['slope'], j['second'], j['meanSlope'], j['meanSecond'], j['height']]
    base = view.solve(h)
    derivative = np.asarray(base['heightJetJacobian']).reshape(3*M+2, M)
    eps = 2.**-20
    fd = np.column_stack([(vector(view.solve(h+np.eye(M)[j]*eps, jacobian=False))
                           -vector(base))/eps for j in range(M)])
    assert np.array_equal(fd, derivative)
    assert base['jets']['E'] == 4. and view.linearD.shape == (M,)
    assert np.any(derivative[2*M:2*M+2])
    rows.append({'prefix_modes':M, 'tail_modes':W,
                 'forward_derivative_exact_difference':float(np.max(np.abs(fd-derivative))),
                 'both_mean_rows_preserved':True, 'all_high_target_modes_zero':True})
result = {'scope':__doc__, 'source':str(source),
          'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'cases':rows, 'solver_calls':0, 'tail_calls':0}
with args.out.open('x') as stream:
    json.dump(result,stream,indent=2)
    stream.write('\n')
print(json.dumps({'cases':len(rows),'all_exact':True,'solver_calls':0,'tail_calls':0,
                  'report':str(args.out),'sha256':hashlib.sha256(args.out.read_bytes()).hexdigest()}))
