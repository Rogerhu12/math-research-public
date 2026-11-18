#!/usr/bin/env python3
"""Record source preparation only; never import/evaluate the new oracle."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def ref(path):
    return dict(path=str(path.resolve()),sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Do not overwrite a frozen interface record')
    source = HERE/'circle_trace_core_intervals.py'
    tree = ast.parse(source.read_text(),filename=str(source))
    classes = [node.name for node in tree.body if isinstance(node,ast.ClassDef)]
    if classes != ['ExactCircleTraceM3Core']:
        raise ValueError('The explicit interface class changed')
    helpers = [HERE/name for name in (
        'generic_raw_core_intervals.py','fast_integral_core_intervals.py',
        'integral_core_intervals.py','certify_protected_arc_curvature_dual.py')]
    m3 = HERE.parent/'resume_m3'
    definitions = [m3/name for name in (
        'circle_trace_controls.py','circle_trace_replacement_basis.py',
        'circle_trace_replacement_core.py','raw_second_order_core.py')]
    definitions += sorted((m3/'round_raw_lib').glob('*.py'))
    result = dict(
        scope='R41 to R44 integral-oracle source preparation; AST syntax and file identities only.',
        command=[sys.executable,*sys.argv],recorder=ref(Path(__file__)),
        prepared_source=ref(source),
        inherited_oracle_sources=[ref(path) for path in helpers],
        current_circle_trace_definition_sources=[ref(path) for path in definitions],
        source_identity_scope='Current explicit implementation identities for this prepared interface; no retroactive numerical execution source claim.',
        accepted_kind='exact_m3_circle_trace_replacement_integral',
        accepted_path='circle-trace-replace-last-two-v1',
        mathematical_inputs='n3, eta0, even/C3, mathematical centre pi/3, lambda=1, M>=4, complete c2..c(M-2),t,u; decimal-roundtrip widths and exact binary64 physical coefficients.',
        changes='Recompute true low two moments for SA/SB, convert to T/U, combine the complete controls before absolute bounds; add cutoff-local frequency-one seed to control jets and primitive.',
        inherited_formulas='Actual-width primary/Green constants; normal curve and material inverse/jet formulas; fixed physical atlas identity.',
        exact_protected_circle='R=1+8q+t, c=q*C-(u-t), O=-c*er(pi/3), u(pi/3)=pi/3; identities only.',
        coefficient_scope='True-versus-binary64 projection coefficient enclosure only, not a bound on all source jets or libm/quadrature/inverse evaluation.',
        AST_syntax_parsed=True,oracle_module_imported=False,
        numerical_core_constructed=False,oracle_constructed=False,
        angular_panels_evaluated=False,material_inverse_evaluated=False,
        metric_evaluated=False,BVP_solver_invoked=False,actual_tail_solver_invoked=False,
        any_candidate_certified=False,
        limits='No candidate or CP is asserted to pass. Positive all-angle rho must be established before inherited inverse/derivative transfer. R38/R40/R41 numeric constants, full graph/closure/reach and held ratio do not transfer automatically.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('x') as stream:
        json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(output=str(args.out.resolve()),sha256=ref(args.out)['sha256'],
                         metadata_only=True,oracle_imported=False)))


if __name__ == '__main__':
    main()
