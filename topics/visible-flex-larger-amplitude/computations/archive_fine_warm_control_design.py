#!/usr/bin/env python3
"""Archive an actual complete fine warm design and its original input evidence.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No geometry field is recomputed. Regenerable complete array chunks stay in
scratch with their full hashes. Exact finite-support R7 algebra is labelled
as a local core diagnostic, not a new solution or full-surface amplitude.
"""
from fractions import Fraction as F
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def exact(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
        decimal_display=float(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix', type=Path, required=True)
    parser.add_argument('--prepared-prefix', type=Path)
    parser.add_argument('--original-failed-prefix', type=Path)
    parser.add_argument('--top', type=Path, required=True)
    parser.add_argument('--tag', required=True)
    args = parser.parse_args()
    prefix, prepared = args.prefix, args.prepared_prefix or args.prefix
    screen_path = Path(str(prefix)+'-screen.json')
    resource_path = Path(str(prefix)+'-resource.json')
    screen, owned = read(screen_path), read(resource_path)
    field = screen['geometry_fields']
    if (owned['exitcode'] != 0 or not owned['wait4_observed'] or
            owned['termination_signal'] is not None or not screen['finished'] or
            not screen['finite_domain_passed'] or screen['nonlinear_solution'] or
            screen['true_new_H_tail_evaluated'] or screen['worker_start_attempts'] or
            field['shape'] != [3764,768,3] or len(screen['actual_core']) != 32 or
            field['mean_quadrature']['angular'] != 1552 or not field['storage']['complete']):
        raise ValueError('Require the actual complete q122-fine warm design, not a partial or accepted solve')
    original_prepare = read(Path(str(prepared)+'-prepared-core.json'))
    if (original_prepare['original_verified_coarse_warm'] != screen['explicit_coarse_increment_warm'] or
            max(abs(a-b) for a,b in zip(original_prepare['actual_complete_core'],screen['actual_core'])) > 2e-14):
        raise ValueError('The complete actual warm did not use its declared prepared core and controls')
    # R7(1) finite support algebra at a0=1; every input Float64 is exact here.
    coefficients = list(map(F.from_float,screen['actual_core']))
    gap = 2*sum(coefficients[::2])
    rho = 1-sum((4*j*j-1)*c*((-1)**j) for j,c in enumerate(coefficients,1))
    k0 = F.from_float(screen['warm_profile']['start_acceleration'])
    budget = dict(schema='actual-unsolved-fine-warm-core-and-geometry-budget-v1',
        source_sha256=sha(__file__), primary_sha256=sha(screen_path),
        exact_binary_inputs=True, retained_even_core_modes=32, a0=1,
        full_core_axial_support_gap=exact(gap), short_axis_curvature_radius=exact(rho),
        initial_acceleration=exact(k0), R7_local_witness_product=exact(k0*gap*rho),
        R7_local_product_below_one=(k0*gap*rho<1),
        kappa_sample=field['kappa_abs_max_sample'], fixed_origin_size_sample=field['twice_radius_max_sample'],
        kappa_times_fixed_origin_size_sample=field['kappa_abs_max_sample']*field['twice_radius_max_sample'],
        raw_cubic_unsolved_field_only=True, continuous_or_closed_surface_D_or_amplitude_claimed=False,
        retained_derived_chunks=field['storage']['chunks'], derived_chunks_copied_to_repository=False)
    budget_path = Path(str(prefix)+'-saved-budget.json')
    if budget_path.exists():
        raise FileExistsError('Fresh exact finite-support budget required')
    budget_path.write_text(json.dumps(budget,indent=2)+'\n')
    files=[]
    def copy(src, suffix, computation=False):
        src=Path(src);data=src.read_bytes()
        dest=args.top/'computations'/src.name if computation else args.top/'notes'/(args.tag+suffix)
        if len(data)>=1_000_000:
            raise ValueError('Only compact metadata, not derived arrays, belongs in this archive')
        if dest.exists() and dest.read_bytes()!=data:
            raise ValueError('Never alter a frozen destination: '+str(dest))
        if not dest.exists():dest.write_bytes(data)
        files.append(dict(path=str(dest.relative_to(args.top)),sha256=sha(dest),bytes=len(data),original_path=str(src)))
    copy(__file__,'',True)
    for tail, suffix in [('-prepared-core.json','-prepared-core.json'),
            ('-prepare-resource.json','-prepare-resource.json'),('-inlet.json','-inlet.json'),
            ('-inlet-resource.json','-inlet-resource.json')]:
        copy(str(prepared)+tail,suffix)
    for tail, suffix in [('-screen.json','-screen.json'),('-resource.json','-resource.json'),
            ('-field.json','-field.json'),('-coarse-fine-geometry-prepared.json','-geometry-prepared.json'),
            ('-geometry-launch.json','-geometry-launch.json'),('-saved-budget.json','-saved-budget.json')]:
        copy(str(prefix)+tail,suffix)
    exact_order=Path(str(prefix)+'-field-exact-chart-order.json')
    if exact_order.exists():copy(exact_order,'-exact-chart-order.json')
    if args.original_failed_prefix:
        for tail,suffix in [('-screen.json','-original-failed-screen.json'),
                ('-resource.json','-original-failed-resource.json'),
                ('-coarse-fine-geometry-prepared.json','-original-failed-preparation.json')]:
            copy(str(args.original_failed_prefix)+tail,suffix)
    inlet=read(Path(str(prepared)+'-inlet.json'))
    note=args.top/'notes'/(args.tag+'-proof.md')
    if note.exists():raise FileExistsError(note)
    value=budget['kappa_times_fixed_origin_size_sample']
    note.write_text('\n'.join([
        '# Actual fine32 complete-mean warm design', '',
        'Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.', '',
        '**Numerical unsolved design evidence.** The actual accepted q122 M32 field',
        '`4c0e13b2…` supplies all 97 state channels, 2,587 raw nodes and all 32 core',
        'modes. The frozen M28 eight-control response is an explicitly old design',
        'increment. All four added fine modes retain their actual baseline values.',
        'The original warm constructor performs its original inlet correction and',
        'low-target parameter enforcement; the separately saved preparation and full',
        'warm record agree. This is no fine Jacobian or accepted new BVP.', '',
        '## Complete actual evaluation', '',
        'All 3,764 common radial points and all 768 angles are evaluated. The',
        'periodic mean uses the complete original M32 count 1,552, and the height',
        'uses the original Gauss6 rule over every actual raw interval. No raw node,',
        'mode, known witness or physical-domain gate is dropped. All eighteen',
        'complete three-component geometry chunks are retained in scratch.', '',
        f"The actual sampled curvature maximum is {field['kappa_abs_max_sample']:.17g};",
        f"the fixed-origin size S=2 max|X| is {field['twice_radius_max_sample']:.17g}.",
        f"Their product is {value:.17g}, {'below' if value<100/3 else 'above'} 100/3.",
        'This is a sampled raw-cubic prefix budget. S is not relabelled as the',
        'complete closed-surface diameter, and exceeding this design budget is not',
        'a proof of impossibility of an accepted solution or another construction.', '',
        f"The minimum sampled tangent area is {field['minimum_tangent_area_sample']:.17g}",
        f"and the minimum sampled Frenet margin is {field['minimum_frenet_margin_sample']:.17g}.",
        'All original finite-domain gates passed. The complete new H is saved, but',
        'no true new-H tail, original Newton/RMS solve or acceptance audit was run.', '',
        'The attached original inlet diagnostic uses the complete prepared core.',
        'Its M32 grid-doubling check and M40/M64 projections are projections only;',
        'the larger representations are not new solved surfaces.', '',
        '## Exact finite-core diagnostic', '',
        'For a0=1 and every saved c_(2j) interpreted as its exact binary rational,',
        '`d=2 sum_(j odd)c_(2j)` and',
        '`rho_short=1-sum_j(4j^2-1)(-1)^j c_(2j)`.',
        f"The complete 32-mode d is {float(gap):.17g}, rho_short is {float(rho):.17g},",
        f"and the exact R7 local product k0*d*rho_short displays as {float(k0*gap*rho):.17g}.",
        'The saved numerator/denominator fields, not the decimal displays, define',
        'this algebraic result. R7 concerns the specified local core witness only;',
        'it establishes no global non-occlusion, set Hausdorff amplitude, reach or held set.', '',
        '## Original failures, reproduction and storage', '',
        ('A separate original float chart-order rejection is included. The existing',
         'exact binary chart-order adapter keeps every actual point and parameter;',
         'its exact sample-order proof is included, while all original raw strict',
         'orientation, mean, physical and geometric formulas remain intact.')[0]
            if args.original_failed_prefix else 'The original float chart orientation gate passed without an exact-order substitution.',
        *(['The existing exact binary chart-order adapter keeps every actual point and parameter.',
           'Its exact sample-order proof is included; every original raw strict orientation,',
           'mean, physical and geometric formula remains intact.'] if args.original_failed_prefix else []), '',
        f"Owned execution: exit 0, {owned['wall_seconds']:.9f} seconds, {owned['peak_rss_kib']} KiB peak.",
        'The owned resource contains the exact executed argv. Sources and complete',
        'input identities remain in the full warm preparation. The small field',
        'manifest and saved budget contain every chunk SHA, byte size and coverage.',
        'The cheap regenerable arrays remain in scratch under repository rule 11.',
        'No missing numerical remainder or continuous floating error is treated as zero.', '',
    ]))
    files.append(dict(path=str(note.relative_to(args.top)),sha256=sha(note),bytes=note.stat().st_size))
    manifest=args.top/'notes'/(args.tag+'-manifest.json')
    if manifest.exists():raise FileExistsError(manifest)
    manifest.write_text(json.dumps(dict(schema='actual-fine-complete-warm-control-design-archive-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',classification='numerical unsolved design; exact finite-core local diagnostic',
        files=files,total_bytes=sum(x['bytes'] for x in files),geometry_chunk_count=len(field['storage']['chunks']),
        geometry_chunk_bytes_scratch_only=sum(x['bytes'] for x in field['storage']['chunks']),
        actual_warm_sha256=sha(screen_path),actual_owned_exitcode=0,
        kappa_times_size_sample=value,new_BVP_Node_Newton_or_tail_calls=0,
        original_failed_attempt_retained=bool(args.original_failed_prefix)),indent=2)+'\n')
    print(json.dumps(dict(manifest=str(manifest),sha256=sha(manifest),files=len(files),
        bytes=sum(x['bytes'] for x in files),kappa_size=value,R7=float(k0*gap*rho))),flush=True)


if __name__=='__main__':
    main()
