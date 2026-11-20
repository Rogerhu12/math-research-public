#!/usr/bin/env python3
"""Read a new candidate once using an existing same-g Gauss carrier bundle.

Reuses the complete observation operator and streaming reader.  It performs
no scalar regeneration, optimization, old dense probe, or continuous audit.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from read_gauss_closed_gram import load, sha, read_candidate, event


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--carrier', type=Path, required=True)
    p.add_argument('--bundle', type=Path, action='append', required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--module', type=Path)
    p.add_argument('--batch-source', type=Path)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Keep the earlier actual readout and choose a fresh output')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    root = a.repo.resolve()/'topics/visible-flex-larger-amplitude'
    source = (a.module or Path(__file__).resolve().with_name('gauss_observed_closed_gram.py')).resolve()
    batch = (a.batch_source or root/'scripts/resume_20261120_batched_closed_gram.py').resolve()
    dense = root/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    module = load('reused_carrier_gauss_operator', source)
    with np.load(a.carrier, allow_pickle=False) as data:
        carrier = {key: np.array(data[key]) for key in data.files}
    plan = module.ObservationPlan.from_arrays(carrier)
    report = dict(schema='existing-same-scalar-Gauss-candidate-readout-20261120-v1',
        source_sha256=sha(__file__), reader_sha256=sha(Path(__file__).resolve().with_name('read_gauss_closed_gram.py')),
        module_sha256=sha(source), batch_sha256=sha(batch), dense_sha256=sha(dense),
        observation_carrier=str(a.carrier.resolve()), observation_carrier_sha256=sha(a.carrier),
        full_angles=a.angles, stage_block=a.stage_block, candidates=[],
        new_scalar_queries=0, nonlinear_solves=0, old_dense_probes_repeated=False,
        retained_old_rows_read=True)
    for path in a.bundle:
        path = path.resolve()
        with np.load(path, allow_pickle=False) as data:
            for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
                if not np.array_equal(data[key], carrier[key]):
                    raise ValueError('The new candidate changed the declared same-g carrier: '+key)
            M = (data['qjets'].shape[-1]-2)//3
            op = module.create(dense, data['mesh'], data['a_stages'], float(data['radius']),
                data['fixed_core_first3'], batch_source=batch, observation_plan=plan,
                a_observations=carrier['a_observations'], M=M, N=a.angles,
                width=float(data['width']), quarter=True, stage_block=a.stage_block)
            x, affine = op.pack(data['qjets'], float(data['Hcap']), require_affine=True)
        result = dict(bundle=str(path), bundle_sha256=sha(path), M=M,
            observation=op.observation_metadata(), affine=affine, readout=read_candidate(op, x))
        report['candidates'].append(result)
        a.out.write_text(json.dumps(report, indent=2)+'\n')
        event(event='existing_carrier_candidate_read', bundle=str(path), bundle_sha256=result['bundle_sha256'],
            old_gram=result['readout']['old_rows']['max_relative_gram'],
            new_gram=result['readout']['new_gauss_rows']['max_relative_gram'],
            old_curvature=result['readout']['old_rows']['maximum_absolute_principal_curvature'],
            new_curvature=result['readout']['new_gauss_rows']['maximum_absolute_principal_curvature'])
    event(event='existing_carrier_read_complete', report=str(a.out.resolve()), report_sha256=sha(a.out))


if __name__ == '__main__':
    main()
