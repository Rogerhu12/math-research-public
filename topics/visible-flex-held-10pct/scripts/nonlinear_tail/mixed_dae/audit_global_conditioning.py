"""Finite mixed Jacobian spectra in the explicit unscaled Euclidean norm.

This is a conditioning diagnostic for the stated grid and variables; it is
neither a norm-independent estimate nor an infinite-mode inverse bound.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from scipy.linalg import svdvals
from mixed_bvp import MixedBVP
from mu_free_fields import MuFreeFields

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--reports', nargs='+', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
rows = []
for path in args.reports:
    report = json.loads(path.read_text())
    for row in report['results']:
        if not row.get('success'):
            continue
        checkpoint = Path(row['checkpoint']['path'])
        if hashlib.sha256(checkpoint.read_bytes()).hexdigest() != row['checkpoint']['sha256']:
            raise ValueError('Checkpoint hash mismatch')
        data = np.load(checkpoint)
        Y, ref, x = data['Y'], data['reference'], data['x']
        f = MuFreeFields(row['modes'], 2, row['angular'], row['full_cosine_sine'], .01)
        profile = lambda x:dict(r=.25+row['radial_span']*x, w=.00358, rx=row['radial_span'], ell=0.)
        bvp = MixedBVP(f, x, profile, ref[0,:f.d], ref[-1,f.d:2*f.d])
        e = bvp.evaluate(Y, True)
        singular = svdvals(e['jacobian'].toarray(), check_finite=True)
        item = dict(amplitude=row['amplitude'], modes=row['modes'],
                    intervals=row['intervals'], full_cosine_sine=row['full_cosine_sine'],
                    dimension=bvp.size, minimum_singular_value=float(singular[-1]),
                    maximum_singular_value=float(singular[0]),
                    condition=float(singular[0]/singular[-1]),
                    report_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    checkpoint_sha256=row['checkpoint']['sha256'])
        rows.append(item)
        print(json.dumps(item), flush=True)
args.out.write_text(json.dumps(dict(scope=__doc__, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), rows=rows), indent=2)+'\n')
