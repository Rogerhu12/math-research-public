#!/usr/bin/env python3
"""Restore exact even/even local chronological terms from saved first integrals.

This transforms a previously certified complete g0 accumulator. A missing
scientific leaf retains its full original fee. It never rebuilds field
coefficients from reports, nor subtracts norms of cancelling functions.
"""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, json, os, platform, subprocess, time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb, acb, ctx
from fourfold_forward_density_pipeline_composition_v9 import (
    decode_ball, encode_ball, save, coefficient_norms)
from fourfold_parameter_ordered_defect import add_rows, derivative_product
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record

BASE = Path('data/phase_ring_continuation/step5_complete_flow_ci_43301401638')
INDEX_SHA = '4174c3edde41f5c8ab12b036d4760c20ec987e475158aa2855ea08158ff7cb45'
PREFIX = 'topics/visible-flex-exact-nearby/'
README_PATHS = ['README.md', PREFIX+'README.md']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_bytes())


def upper(record):
    x = arb(record['upper']).upper()
    if not x.is_finite():
        raise ValueError('nonfinite saved upper endpoint')
    return x


def checked_relative(path):
    path = Path(path)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('scientific dependency must remain inside topic')
    return path


def git(args, input_text=None, check=True):
    workspace = os.environ['GITHUB_WORKSPACE']
    credential = '!f() { printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; }; f'
    base = ['git', '-c', 'safe.directory='+workspace, '-c', 'gc.auto=0',
            '-c', 'maintenance.auto=false', '-c', 'credential.helper=',
            '-c', 'credential.helper='+credential]
    p = subprocess.run(base+args, cwd=workspace, input=input_text, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       env=dict(os.environ, GIT_TERMINAL_PROMPT='0'))
    if check and p.returncode:
        print(p.stdout, flush=True)
        raise RuntimeError('native Git command failed: '+args[0])
    return p


def materialize(paths, tracked):
    wanted = sorted({PREFIX+str(checked_relative(p)) for p in paths}
                    & tracked)
    missing = [p for p in wanted if not (Path(os.environ['GITHUB_WORKSPACE'])/p).is_file()]
    if missing:
        git(['sparse-checkout', 'add', '--stdin'],
            ''.join('/'+p+'\n' for p in missing))
    return [p for p in paths if Path(p).is_file()]


def function_ast(path, names):
    tree = ast.parse(Path(path).read_text())
    result = []
    for name in names:
        found = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name]
        if len(found) != 1:
            return None
        node = copy.deepcopy(found[0])
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str):
            node.body.pop(0)
        result.append(ast.dump(node, include_attributes=False))
    return result


def first_norm_lowers(row, width):
    """Lower bounds on the norms of every exact function in these balls."""
    n, d = arb(0), arb(0)
    for k, z in enumerate(row):
        m = max(arb(0), abs(z).lower())
        weight = (1 if k == 0 else 2)*(k*width).exp()
        n = (n+m*weight).lower()
        d = (d+k*m*weight).lower()
    return max(arb(0), n), max(arb(0), d)


def record_files(paths):
    rows = []
    for p in paths:
        p = Path(p)
        size = p.stat().st_size
        if size > 5_000_000 or (size > 1_000_000 and p.suffix != '.gz'):
            raise ValueError('proof artifact exceeds repository file limits: '+str(p))
        rows.append(dict(path=str(p), sha256=sha(p), bytes=size))
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index', type=Path, default=BASE/'g0/index.json.gz')
    p.add_argument('--out', type=Path, default=Path('data/phase_ring_continuation/step5_local_J0_symmetric_ci'))
    p.add_argument('--summary', type=Path, default=Path('notes/2026-11-12-ci-local-J0-symmetric-summary.json'))
    p.add_argument('--materialize', action='store_true')
    p.add_argument('--bits', type=int, default=256)
    args = p.parse_args()
    ctx.prec = args.bits
    started = time.monotonic()
    index = read(args.index)
    if sha(args.index) != INDEX_SHA:
        raise ValueError('complete original g0 index changed')
    if (not index.get('complete') or not index.get('whole_forward_leg')
        or index.get('completed_segments') != 550
        or not index.get('all_listed_time_and_finite_reference_seams_exact')):
        raise ValueError('complete original exact chronological cover required')
    if Fraction(index['inner_strip']) != Fraction(3, 1024):
        raise ValueError('unexpected original local-J strip')
    width = exact_arb(Fraction(index['inner_strip']))
    tracked = set()
    if args.materialize:
        tracked = set(git(['ls-tree', '-r', '--name-only', 'HEAD', '--', PREFIX]).stdout.splitlines())
        materialize([r['path'] for r in index['leaves']]+[index['accumulator_path']], tracked)
    accumulator_path = checked_relative(index['accumulator_path'])
    if sha(accumulator_path) != index['accumulator_sha256']:
        raise ValueError('original complete accumulator changed')
    accumulator = read(accumulator_path)
    if (accumulator['identity']['leaves'] != index['leaves']
        or accumulator['identity']['descriptor_sha256'] != index['descriptor_sha256']
        or not accumulator.get('every_cross_frequency_retained')):
        raise ValueError('original accumulator sequence or identity changed')
    original_first = [decode_ball(z) for z in accumulator['first']]
    original_second = [decode_ball(z) for z in accumulator['second_cross']]
    original_total = upper(index['summary']['omitted_local_J'])
    names = ['coefficient_norms', 'first_integral_and_local_second_bound']
    template_path = Path(__file__).with_name('fourfold_forward_density_pipeline_composition_v9.py')
    template_ast = function_ast(template_path, names)
    allowed = {}
    for f in Path(__file__).parent.glob('fourfold_forward_density_pipeline*.py'):
        if function_ast(f, names) == template_ast:
            allowed[sha(f)] = str(f)
    leaf_reports = {}
    first_paths = []
    skipped = []
    for r in index['leaves']:
        path = checked_relative(r['path'])
        if not path.is_file():
            skipped.append(dict(path=str(path), reason='original scientific leaf not materialized; full fee retained'))
            continue
        if sha(path) != r['sha256']:
            raise ValueError('original density leaf changed: '+str(path))
        report = read(path)
        ref = report['identity']['reference']
        if (not report.get('complete') or not report.get('complete_continuous_true_density_proved')
            or ref['retarget_descriptor_sha256'] != index['descriptor_sha256']
            or ref['leg'] != 'forward' or int(ref['segment']) != int(r['segment'])
            or list(map(Fraction, ref['normalized_subspan'])) != list(map(Fraction, r['normalized_subspan']))
            or Fraction(report['inner_strip']) != Fraction(index['inner_strip'])):
            raise ValueError('saved same-reference complete density identity differs')
        if report['source_sha256'] not in allowed:
            skipped.append(dict(path=str(path), reason='source local-J formula not AST-identical; full fee retained',
                                source_sha256=report['source_sha256']))
            continue
        leaf_reports[str(path)] = (r, report)
        first_paths.append(report['first_integral_file']['path'])
    if args.materialize:
        materialize(first_paths, tracked)
    correction = [acb(0)]
    removed = arb(0)
    processed_old = arb(0)
    rows = []
    for path, (r, report) in leaf_reports.items():
        link = report['first_integral_file']
        first_path = checked_relative(link['path'])
        if not first_path.is_file():
            skipped.append(dict(path=path, reason='original first integral absent; full fee retained'))
            continue
        if sha(first_path) != link['sha256'] or first_path.stat().st_size != link['bytes']:
            raise ValueError('saved first-integral bytes changed')
        first_doc = read(first_path)
        if (first_doc['kind'] != 'complete_enclosed_first_integral_of_exact_finite_density'
            or first_doc['identity'] != report['identity']
            or first_doc['density_coefficient_sha256'] != report['density_coefficient_sha256']):
            raise ValueError('first integral belongs to another finite density')
        G = [decode_ball(z) for z in first_doc['coefficients']]
        if not G or not G[0].imag.contains(0) or any(not z.is_finite() for z in G):
            raise ValueError('finite real Fourier first integral required')
        G[0] = acb(G[0].real)
        n0, n1 = first_norm_lowers(G, width)
        removable = max(arb(0), (n0*n1/2).lower())
        old = upper(report['R72_inputs']['omitted_local_second_integral_bound_on_inner_strip'])
        if not 0 <= removable <= old:
            raise ValueError('subtracted explicit budget component exceeds old fee')
        remainder = (old-removable).upper()
        J = [z/2 for z in derivative_product(G, G)]
        if not J[0].contains(0):
            raise ValueError('half derivative of G squared has nonzero mean')
        J[0] = acb(0)  # exact mean of a derivative, not an estimated cancellation
        correction = add_rows(correction, J)
        removed = (removed+removable).lower()
        processed_old = (processed_old+old).upper()
        rows.append(dict(path=path, sha256=r['sha256'], segment=int(r['segment']),
            normalized_subspan=r['normalized_subspan'], first_integral=link,
            source_path=allowed[report['source_sha256']], source_sha256=report['source_sha256'],
            density_coefficient_sha256=report['density_coefficient_sha256'],
            first_norm_lower=ball_record(n0), first_derivative_norm_lower=ball_record(n1),
            old_local_fee=ball_record(old), removed_budget_lower=ball_record(removable),
            remaining_bracket_fee=ball_record(remainder), correction_positive_count=len(J)))
        if len(rows) % 50 == 0:
            print('SYMMETRIC_LOCAL_J_PROGRESS', len(rows), 'removed_lower', str(removed), flush=True)
    if not rows or not 0 < removed <= original_total:
        raise ValueError('no positive verified improvement or inconsistent global fee')
    new_total = (original_total-removed).upper()
    improved_second = add_rows(original_second, correction)
    improved_W = add_rows(original_first, improved_second)
    args.out.mkdir(parents=True, exist_ok=True)
    coefficient_path = args.out/'coefficients.json.gz'
    save(coefficient_path, dict(kind='complete_local_J0_symmetric_correction',
         original_index_path=str(args.index), original_index_sha256=sha(args.index),
         descriptor_sha256=index['descriptor_sha256'], strip=index['inner_strip'],
         exact_identity='sum over processed leaves of one half G_x G',
         every_product_frequency_retained=True, exact_zero_mode=0,
         correction=[encode_ball(z) for z in correction],
         improved_first=[encode_ball(z) for z in original_first],
         improved_second=[encode_ball(z) for z in improved_second],
         improved_W=[encode_ball(z) for z in improved_W]))
    A, E, gap = [upper(index['summary'][k]) for k in ('A','E','R')]
    if not A <= gap/2:
        raise ValueError('original complete R72 displacement gate fails')
    new_coordinate_error = (E*(1+A/gap)+A**3/(2*(gap-A)**2)+new_total).upper()
    ranked = sorted(rows, key=lambda r: r['remaining_bracket_fee']['mid_float'], reverse=True)
    report = dict(kind='proved_saved_first_integral_symmetric_local_J0_refinement',
        proved=True, complete_global_budget_transformation=True,
        full_original_geometry_revalidated=False,
        original_verified_index=dict(path=str(args.index), sha256=sha(args.index)),
        original_accumulator=dict(path=str(accumulator_path), sha256=sha(accumulator_path)),
        descriptor_sha256=index['descriptor_sha256'], source_path='scripts/'+Path(__file__).name,
        source_sha256=sha(__file__), label_strip=index['label_strip'], inner_strip=index['inner_strip'],
        original_leaf_count=len(index['leaves']), refined_leaf_count=len(rows), unchanged_leaf_count=len(skipped),
        full_old_fee=ball_record(original_total), removed_explicit_budget_lower=ball_record(removed),
        full_remaining_local_fee=ball_record(new_total), old_fees_on_processed_leaves=ball_record(processed_old),
        correction_A_inner=ball_record(coefficient_norms([correction],width)[0][0]),
        improved_complete_W_A_inner=ball_record(coefficient_norms([improved_W],width)[0][0]),
        true_R72_coordinate_error=ball_record(new_coordinate_error),
        all_infinite_source_errors_and_chronological_tail_unchanged=True,
        coefficients=dict(path=str(coefficient_path),sha256=sha(coefficient_path),bytes=coefficient_path.stat().st_size),
        audited_budget_functions=names, audited_source_paths=allowed,
        proof='J=.5 G_x G + sum_even_e,odd_o 2/((e+o+2)(e+1))*(g_o,x*g_e-g_e,x*g_o). Old fee is an upper bound on .5 U(G)U(G_x)+positive bracket norm sum. Lower norms of saved complete G give a lower bound on that explicit positive budget component. Removing only that lower bound retains an upper bound for every omitted bracket. Unprocessed leaves keep all their old fees.',
        refined_leaves=rows, unchanged_leaves=skipped,
        parameter_orders_1_and_2_not_modified=True, R31_acceptance_not_asserted=True,
        runtime=dict(python=platform.python_version(),flint=flint.__version__,bits=ctx.prec),
        run_id=os.environ.get('GITHUB_RUN_ID'),workflow_commit=os.environ.get('GITHUB_SHA'),
        wall_seconds=time.monotonic()-started)
    report_path=args.out/'report.json.gz'
    save(report_path,report)
    summary={k:v for k,v in report.items() if k not in ('refined_leaves','unchanged_leaves','audited_source_paths')}
    summary['full_report']=dict(path=str(report_path),sha256=sha(report_path),bytes=report_path.stat().st_size)
    summary['largest_remaining_fees']=[{k:r[k] for k in ('path','segment','old_local_fee','removed_budget_lower','remaining_bracket_fee')} for r in ranked[:12]]
    summary['unchanged_leaf_reasons']={}
    for row in skipped:
        reason=row['reason']
        summary['unchanged_leaf_reasons'][reason]=summary['unchanged_leaf_reasons'].get(reason,0)+1
    save(args.summary,summary)
    manifest_path=args.out/'manifest.json'
    save(manifest_path,dict(complete=True,files=record_files([coefficient_path,report_path,args.summary]),
        source_sha256=sha(__file__),run_id=os.environ.get('GITHUB_RUN_ID'),
        workflow_commit=os.environ.get('GITHUB_SHA')))
    print(json.dumps(dict(refined_leaf_count=len(rows),unchanged_leaf_count=len(skipped),
        full_remaining_local_fee=ball_record(new_total),true_R72_coordinate_error=ball_record(new_coordinate_error),
        summary_path=str(args.summary),summary_sha256=sha(args.summary)),indent=2),flush=True)


if __name__ == '__main__':
    main()
