#!/usr/bin/env python3
"""Inspect the actual fine warm chart only, retaining its original rejection.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This reuses the original exact-binary chart diagnostic and genuine fine warm
constructor. It returns before geometry/mean evaluation and never changes a
production orientation gate. The returned diagnostic explicitly has no full
geometry result and is not an accepted field.
"""
import hashlib
import inspect
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PINS = {
    'root_actual_warm_chart_orientation_probe.py':
        'cd9aedc0edc0b3d13dcc4bd4724c386b0f5ddb847fa0317f9e4b16c559e88868',
    'root_actual_coarse_increment_geometry_complete_mean.py':
        'c986073622d4ebabb2be7d1eea46fe8ac4966a404b56bbc6a6af3b48371092bc',
    'root_actual_geometry_field_complete_mean.py':
        '614a671b86dc1bacccf52d62311c51a7473c83072f9ce39e81ae3e421541dd86',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    for name, wanted in PINS.items():
        if sha(HERE/name) != wanted:
            raise ValueError('Original fine chart diagnostic source changed: '+name)
    import root_actual_warm_chart_orientation_probe as original_probe
    import root_actual_geometry_field_complete_mean as geometry
    import root_actual_coarse_increment_geometry_complete_mean as fine

    def actual_probe(obj, x, t, flow, parameters, output):
        response = original_probe.probe(obj, x, t, flow, parameters, output)
        result = json.loads(output.read_text())
        result['actual_fine_warm_chart_adapter'] = dict(
            source_sha256=sha(__file__), original_sources=PINS,
            original_exact_binary_chart_probe_unchanged=True,
            genuine_current_fine_warm_constructor_used=True,
            finite_geometry_gate_bypassed_to_accept_a_field=False,
            numerical_geometry_or_mean_evaluations=0)
        output.write_text(json.dumps(result, indent=2)+'\n')
        response['original_chart_gate_diagnostic']['sha256'] = sha(output)
        return response

    old_geometry = geometry.main
    original = inspect.getsource(old_geometry)
    before = "        physical_nodes, unused_ds = obj.chart(x, 0.)\n        physical_grid, unused_ds = obj.chart(t, 0.)\n        if not np.all(np.diff(physical_nodes) > 0) or not np.all(np.diff(physical_grid) > 0):\n            raise ValueError('The physical chart lost orientation')\n"
    after = "        completed = True\n        return actual_fine_chart_probe(obj,x,t,flow,p,output)\n"+before
    if original.count(before) != 1:
        raise ValueError('The original full geometry gate moved')
    changed = original.replace(before, after, 1)
    if changed.replace(after, before, 1) != original:
        raise ValueError('Undeclared original geometry source change')
    namespace = dict(old_geometry.__globals__, actual_fine_chart_probe=actual_probe)
    exec(compile(changed, '<fine-chart-only-before-original-geometry-gate>', 'exec'), namespace)

    fine_original = inspect.getsource(fine.main)
    start = fine_original.index("        if report.get('explicit_coarse_increment_warm')!=record or report['geometry_fields']")
    end = fine_original.index('    finally:coarse._ACTIVE,entry.main,sys.argv=', start)
    old = fine_original[start:end]
    new = """        if report.get('explicit_coarse_increment_warm')!=record:
            raise ValueError('The chart diagnostic did not consume the actual fine warm')
        diagnostic=report.get('original_chart_gate_diagnostic',{})
        if (report.get('finite_domain_passed') is not False or 'geometry_fields' in report
            or not diagnostic or sha(diagnostic['path'])!=diagnostic['sha256']):
            raise ValueError('Require an explicit chart-only diagnostic, never a geometry field')
        print(json.dumps(dict(event='actual_fine_chart_only_finished',path=diagnostic['path'],
            sha256=diagnostic['sha256'],original_gate_passed=diagnostic['original_gate_passed'],
            original_production_orientation_gate_unchanged=True,new_solution=False)),flush=True)
"""
    fine_changed = fine_original[:start]+new+fine_original[end:]
    if fine_changed.replace(new, old, 1) != fine_original:
        raise ValueError('Undeclared fine constructor source change')
    ns = dict(fine.main.__globals__)
    exec(compile(fine_changed, '<actual-fine-warm-with-chart-only-result>', 'exec'), ns)
    geometry.main = namespace['main']
    try:
        ns['main']()
    finally:
        geometry.main = old_geometry


if __name__ == '__main__':
    main()
