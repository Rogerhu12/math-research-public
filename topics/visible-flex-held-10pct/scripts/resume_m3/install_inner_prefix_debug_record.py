#!/usr/bin/env python3
"""Retain a clearly unaccepted inner prefix before its actual-tail query.

The original equations, arrays, residuals and acceptance flow are unchanged.
The saved cubic representation uses the original solver chart coordinate;
it is diagnostic data, not a physical C2 prefix or accepted checkpoint.
Apply only to an owned source copy. Canonical sources remain read-only.
"""
import argparse
import hashlib
import json
from pathlib import Path


HELPER = '''def record_inner_prefix_debug(o,sol,a,outer,candidate):
    """Read-only serialization; never an accepted prefix checkpoint."""
    import gzip
    file=a.out_prefix.with_name(a.out_prefix.name+f'-inner-{outer:04d}-debug.json.gz')
    if file.exists():raise FileExistsError('Inner diagnostic prefix already used')
    paths=dict(profile=a.profile,chart=a.chart,linear_port=a.linear_port,
               tail_config=a.tail_config,restart=a.restart)
    inputs={k:dict(path=str(v.resolve()),sha256=hashlib.sha256(v.read_bytes()).hexdigest()) for k,v in paths.items()}
    profile=json.loads(a.profile.read_text());chart=json.loads(a.chart.read_text())
    port=json.loads(a.linear_port.read_text());tail_config=json.loads(a.tail_config.read_text())
    round_file=a.out_prefix.with_name(a.out_prefix.name+'-round-record.json')
    round_record=json.loads(round_file.read_text()) if round_file.exists() else None
    frozen=profile if a.fixed else {**profile,'delta':profile['delta']+float(sol.p[0])}
    data=dict(scope='Unaccepted inner affine-DN prefix before the actual nonlinear tail response. Raw p/sol only; no full metric or C2-map acceptance.',
        solver_success=False,projected_solver_success=bool(sol.success),actual_tail_accepted=False,
        stage='before_actual_tail_query',outer=outer,inputs=inputs,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        core_round_record=round_record,chart=chart,input_profile=profile,
        candidate_frozen_profile=frozen,physical_tail_parameters=port['parameters'],
        physical_tail_cut=port['cut'],tail_config=tail_config,
        gauge_amplitude=float(o.q),modes=o.M,angular=o.nt,fixed_metric=bool(a.fixed),
        central_correction_scales=o.pscale.tolist(),parameters=sol.p.tolist(),
        candidate_cut_height=candidate.tolist(),
        max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
        raw_inner_solution=dict(coordinate='The original solve_bvp independent coordinate; convert with the source chart before physical use.',
            mesh=sol.x.tolist(),values=sol.y.tolist(),
            cubic_breaks=sol.sol.x.tolist(),cubic_coefficients=sol.sol.c.tolist(),
            cubic_axis=sol.sol.axis))
    payload=gzip.compress((json.dumps(data,separators=(',',':'))+'\\n').encode(),mtime=0)
    with file.open('xb') as stream:stream.write(payload)
    print(json.dumps(dict(event='inner_prefix_debug_saved',outer=outer,path=str(file),
        sha256=hashlib.sha256(payload).hexdigest(),actual_tail_accepted=False)),flush=True)


'''


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--manifest', type=Path, required=True)
    a = p.parse_args()
    file = a.source_topic / 'scripts/db6f-prefix-coupled.py'
    before = file.read_text()
    marker = 'def solve_with_actual_tail(o,tail,x,y,par,a):\n'
    old = "        candidate=o.bridge.sigma*o.q*sol.y[o.iz:,-1]\n        actual=tail.solve(candidate,jacobian=True,audit=False)"
    new = "        candidate=o.bridge.sigma*o.q*sol.y[o.iz:,-1]\n        record_inner_prefix_debug(o,sol,a,outer,candidate)\n        actual=tail.solve(candidate,jacobian=True,audit=False)"
    if before.count(marker) != 1 or before.count(old) != 1 or 'def record_inner_prefix_debug' in before:
        raise ValueError('Expected the unmodified original inner/actual-tail boundary')
    after = before.replace(marker, HELPER + marker).replace(old, new)
    if after.replace(HELPER, '').replace(new, old) != before:
        raise AssertionError('Only the isolated diagnostic insertion is allowed')
    compile(after, str(file), 'exec')
    file.write_text(after)
    result = dict(scope=__doc__,file=str(file.resolve()),
                  before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                  after_sha256=hashlib.sha256(after.encode()).hexdigest(),
                  installer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  record_scope='Explicit solver_success=false and actual_tail_accepted=false; raw p/sol is not a production prefix checkpoint.')
    a.manifest.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
