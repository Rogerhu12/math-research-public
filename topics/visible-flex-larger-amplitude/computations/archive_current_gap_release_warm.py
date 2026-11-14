#!/usr/bin/env python3
"""Freeze the actual gap-preserving current-A warm, retaining its exact controls.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Cheap derived geometry arrays remain in scratch with complete original chunk
hashes and regeneration commands. No new solution or continuous bound is asserted.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import struct


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def bits(values):
    return b''.join(struct.pack('<d', x) for x in values)


def rat(x):
    return dict(numerator=str(x.numerator), denominator=str(x.denominator))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic', type=Path, required=True)
    ap.add_argument('--tag', required=True)
    a = ap.parse_args()
    base = Path('m32-q126-r1')
    prefix = 'gap-release-tail2-size099-exact-warm-r2'
    plan_path = base/(prefix+'-plan.json')
    plan = read(plan_path)
    row = plan['candidates'][0]
    report, owned = read(row['report']), read(row['resource'])
    inlet_path = base/'gap-release-tail2-size099-inlet-data-r2-report.json'
    inlet = read(inlet_path)
    background_path = base/'gap-release-tail2-size099-background-diagnostic-r1.json'
    background = read(background_path)
    from root_geometry_execute_plan import inspect_complete
    complete = inspect_complete(row)
    geometry = report['geometry_fields']
    core = geometry['actual_core']
    assert (owned['wait4_observed'] and complete['complete_finite_field']
            and owned['command'] == row['command'][row['command'].index('--')+1:]
            and geometry['shape'] == [3767, 768, 3]
            and geometry['mean_quadrature']['angular'] == 1552
            and len(core) == 32 and len(report['complete_warm_H']) == 32
            and bits(core) == bits(inlet['actual_full_core'])
            and bits(report['complete_warm_H']) == bits(inlet['genuine_warm_H'])
            and bits(report['actual_target']) == bits(row['expected_core'])
            and report['warm_profile'] == inlet['warm_profile']
            and background['input_sha256'][str(plan_path)] == sha(plan_path)
            and background['input_sha256'][row['report']] == sha(row['report']))
    gap = 2*sum(map(F.from_float, core[::2]))
    rho = F(1)+sum((1-(2*j+2)**2)*F.from_float(c)*(-1)**(j+1)
                   for j, c in enumerate(core))
    r7 = F.from_float(report['warm_profile']['start_acceleration'])*gap*rho
    size = geometry['twice_radius_max_sample']
    kappa = geometry['kappa_abs_max_sample']
    summary = dict(schema='current-gap-preserving-complete-warm-design-summary-v1',
        source_sha256=sha(__file__), actual_target3=report['actual_target'],
        complete_physical_steps=row['complete_physical_steps'],
        actual_complete_core=core, core32_little_endian_float64_sha256=hashlib.sha256(bits(core)).hexdigest(),
        actual_complete_H=report['complete_warm_H'],
        H32_little_endian_float64_sha256=hashlib.sha256(bits(report['complete_warm_H'])).hexdigest(),
        full_inlet_and_geometry_core_and_H_all_bits_equal=True,
        complete_axis_gap=rat(gap), gap_display=float(gap),
        short_axis_core_radius=rat(rho), R7=rat(r7), R7_display=float(r7),
        raw_cubic_kappa=kappa, prefix_S=size, kappa_S=kappa*size,
        full_gap_over_prefix_S=float(gap)/size,
        original_inlet_metrics=inlet['original_inlet_metrics'],
        finite_Frenet_margin=geometry['minimum_frenet_margin_sample'],
        finite_tangent_area=geometry['minimum_tangent_area_sample'],
        complete_mean_angular=1552, original_shape=geometry['shape'],
        background_combined_S=background['maximum_prefix_and_background_size_diagnostic'],
        background_combined_kappa_S=background['prefix_curvature_times_combined_size_diagnostic'],
        actual_full_field_record=complete, field_execution_command=row['command'],
        exact_chart_order=geometry['actual_exact_chart_order_bridge'],
        actual_inlet_and_finite_warm_only=True, new_nonlinear_solution=False,
        changed_H_nonlinear_tail_not_evaluated=True,
        continuous_metric_curvature_reach_or_closed_D_certified=False)
    files = []
    def save(src, dest):
        data = Path(src).read_bytes()
        if dest.exists():
            if dest.read_bytes() != data:
                raise FileExistsError(dest)
        else:
            dest.write_bytes(data)
        files.append(dict(path=str(dest.relative_to(a.topic)), sha256=sha(dest),
                          bytes=len(data), original_path=str(Path(src).resolve())))
    save(__file__, a.topic/'computations'/Path(__file__).name)
    named = [('plan.json',plan_path), ('screen.json',Path(row['report'])),
        ('resource.json',Path(row['resource'])), ('field-manifest.json',Path(row['field'])),
        ('execution-ledger.json',base/(prefix+'-ledger.json')),
        ('exact-chart-order.json',Path(geometry['actual_exact_chart_order_bridge']['path'])),
        ('warm-adapter.json',base/(prefix+'-actual-three-control-adapter.json')),
        ('provider-source.json',base/(prefix+'-initial-laws-geometry-source.json')),
        ('background.json',background_path),
        ('background-resource.json',base/'gap-release-tail2-size099-background-owned-r1-resource.json')]
    for suffix, source in named:
        save(source, a.topic/'notes'/(a.tag+'-'+suffix))
    out = a.topic/'notes'/(a.tag+'-summary.json')
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(summary, indent=2)+'\n')
    files.append(dict(path=str(out.relative_to(a.topic)), sha256=sha(out), bytes=out.stat().st_size))
    note = '''# Actual current-A gap-preserving warm

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

The complete current-M32 warm has been evaluated using all 2590 raw nodes and the unchanged 3767-by-768 common grid, with the original 1552-point angular mean and Gauss6 height rule. Its owned execution and every derived chunk are verified by the original complete-field reader. The accompanying inlet and geometry outputs have exactly identical binary core coefficients and all 32 H coordinates.

The actual finite prefix curvature is 8.279007052446111, S=2 max norm is 3.938532664305123, and their product is 32.607139704071486. The original accepted-A finite product was about 33.19818874. The complete core gap, computed as twice the sum of all coefficients at frequencies 2 modulo 4, is .2506381130462593; gap/S is .06363743414337775. No coefficient is omitted. The exact binary gap, short-axis radius and R7 value are stored in the summary; R7 is .23644261112015857.

The original actual inlet metric Fourier l1 diagnostic is 1.1667291698732543e-7. The positive finite Frenet margin is .005132740095946997 and tangent area minimum is .22020639890046026. These sampled values do not certify continuous inequalities. The same frozen-tail background 1440-profile size diagnostic gives S=3.9430259488970205 and product 32.644339638896454, while retaining the changed-H nonlinear tail, complete cap and continuous errors as unpaid.

The original floating common-grid rejection is retained in the separate inlet/chart archive. The explicitly identified exact-order entry proves strict order of all stored binary-polynomial sample coordinates while retaining the original strict raw-node gate. It changes no candidate coefficient, point or geometric formula. Both displayed-equal common points are retained, and no adjacent common-grid rounded difference is used as a derivative denominator.

The full field remains an unsolved tangent warm state. No new PDE solution, RMS acceptance, new-H tail solve, all-time embedding, reach, Hausdorff amplitude or complete closed diameter is asserted. The exact original target3 and six physical neutral steps are retained for the original production BVP; rounded chat values must not replace them.

The 18 regenerable compressed geometry chunks (about 26.4 MB) remain in scratch under the original field manifest. The archive retains every path, exact byte count, SHA, complete coverage and original owned command. Reproduction uses the same frozen sources and accepted/raw/response inputs in the plan, runs the saved command with fresh output paths, and checks the regenerated numerical array contents and complete coverage. Output-path-dependent manifests need not have identical text bytes after renaming; original array data hashes are the reproduction targets.
'''
    path = a.topic/'notes'/(a.tag+'-note.md')
    if path.exists():
        raise FileExistsError(path)
    path.write_text(note)
    files.append(dict(path=str(path.relative_to(a.topic)),sha256=sha(path),bytes=path.stat().st_size))
    manifest = dict(schema='current-A-complete-gap-preserving-warm-compact-archive-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',files=files,
        total_bytes=sum(f['bytes'] for f in files),all_completed_owned_outcomes_verified=True,
        derived_chunks_archived=False,derived_chunk_count=len(complete['chunks']),
        derived_chunk_bytes=sum(c['bytes'] for c in complete['chunks']),
        exact_original_BVP_controls_preserved=True,new_nonlinear_solution=False)
    path=a.topic/'notes'/(a.tag+'-manifest.json')
    if path.exists():raise FileExistsError(path)
    path.write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(manifest=str(path),sha256=sha(path),files=len(files),
        archived_bytes=manifest['total_bytes'],actual_kappa_S=kappa*size)),flush=True)


if __name__ == '__main__':
    main()
