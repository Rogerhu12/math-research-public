#!/usr/bin/env python3
"""Check the explicit merit and H0 restart on real saved data, without a BVP.

The original complete raw arrays and audited tail packet are read and verified.
The original outer method is compiled as a protocol fixture and interrupted
at the first solve_bvp entry. No physical RHS, Jacobian, Newton solve, geometry,
new tail worker or accepted surface is computed by this check.
"""
from __future__ import annotations
import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path
import resource
import textwrap
import time
from types import SimpleNamespace

import numpy as np
import scipy.integrate

import strong_actual_newton_checkpoints as checkpoints
import strong_actual_recorded_tail_port as recorded
import strong_neck_bvp as adapter
from strong_actual_fixed_control_response import raw_flat
from strong_physical_merit_actual_bvp import argument, prepare_configuration
from strong_physical_merit_and_affine_resume import Runtime

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path = Path(path)
    contents = path.read_bytes()
    return json.loads(gzip.decompress(contents) if path.suffix == '.gz' else contents)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--previous-accepted', type=Path, required=True)
    parser.add_argument('--alpha', type=float, required=True)
    parser.add_argument('--original-merit', type=float, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    options = parser.parse_args()
    output = options.out_prefix.with_suffix('.json')
    if output.exists() or not 0 < options.alpha <= 1:
        raise ValueError('Use a fresh output prefix and the observed accepted alpha')
    begin = time.monotonic()
    inputs = {str(options.plan): sha(options.plan),
              str(options.previous_accepted): sha(options.previous_accepted),
              str(Path(__file__)): sha(__file__)}
    plan = document(options.plan)
    arguments = plan['run_argv'][2:]
    configuration = prepare_configuration(arguments,
        Path(argument(arguments, '--resume-original-affine-anchor')),
        Path(argument(arguments, '--original-inner-entry-raw')),
        Path(argument(arguments, '--original-inner-entry-tail-config')))
    runtime = Runtime(configuration, options.out_prefix)
    report = dict(scope=__doc__, finished=False, passed=False, source_sha256=inputs,
        physical_RHS_evaluations=0, global_Jacobian_evaluations=0,
        BVP_solves=0, Node_worker_start_attempts=0, nonlinear_solution=False,
        tests=[])
    old_solve_bvp = scipy.integrate.solve_bvp
    port = None
    try:
        current_path = Path(configuration['resume_raw'])
        current = document(current_path)
        previous = document(options.previous_accepted)
        arrays = {name: np.asarray(raw_flat(current_path, current, name, inputs), float)
                  .reshape(current['arrays'][name]['shape']) for name in ('x','y','p')}
        before = {name: np.asarray(raw_flat(options.previous_accepted, previous, name, inputs), float)
                  .reshape(previous['arrays'][name]['shape']) for name in ('x','y','p')}
        if not np.array_equal(arrays['x'], before['x']):
            raise ValueError('The real accepted pair has different full meshes')
        n, nodes = arrays['y'].shape
        direction = np.r_[((arrays['y']-before['y'])/options.alpha).ravel(order='F'),
                          (arrays['p']-before['p'])/options.alpha]
        raw_cost = float(direction@direction)
        weighted = runtime.cost(direction, n, nodes)
        direct = float(direction[:n*nodes]@direction[:n*nodes])
        direct += float(np.sum(np.square(direction[n*nodes:]*runtime.weights)))
        if abs(raw_cost/options.original_merit-1) > 2e-10 or abs(weighted-direct) > 2e-15:
            raise ValueError('The complete observed direction or fixed weighted merit differs')
        report['tests'].append(dict(name='complete_observed_Newton_direction_merit',passed=True,
            original_merit=options.original_merit, reproduced_raw_merit=raw_cost,
            raw_relative_difference=abs(raw_cost/options.original_merit-1),
            fixed_physical_merit=weighted, independent_weighted_expression=direct,
            fixed_parameter_weights=runtime.weights.tolist(), complete_field_entries=n*nodes))
        del direction, before

        adapter.LINEAR_SOLVER = 'block-qr'
        adapter.NEWTON_FACTOR = 1.
        adapter.TRACE_NEWTON = True
        adapter.COLLECT_FLOW_GARBAGE = True
        loaded = adapter.module('strong_merit_protocol_original_newton', HERE/'root_domain_newton.py')
        runtime.install_newton(loaded, HERE/'root_domain_newton.py', adapter)
        checkpoints.install_observer(loaded, HERE/'root_domain_newton.py', adapter,
            SimpleNamespace(save=lambda *a, **k: (_ for _ in ()).throw(
                RuntimeError('This protocol check must not execute Newton'))))
        transformed = (HERE/'root_domain_newton.py').read_text()
        for change in adapter.TRANSFORMS['root_domain_newton.py']['replacements']:
            if transformed.count(change['old']) != change['count']:
                raise ValueError('Actual owned Newton transform no longer reproduces')
            transformed = transformed.replace(change['old'],change['new'])
        if (transformed.count('_strong_fixed_physical_merit(') != 2 or
                'threshold = h*(bvp_tol/30.)' not in transformed or
                'np.all(abs(br) < bc_tol)' not in transformed or
                loaded._strong_fixed_physical_merit.__self__ is not runtime or
                '_strong_actual_checkpoint' not in loaded.solve_newton.__code__.co_names):
            raise ValueError('Fixed merit, original stopping gate or observation chain differs')
        report['tests'].append(dict(name='actual_owned_Newton_loader_and_checkpoint_compile',
            passed=True, merit_replacements=2, original_stopping_gate_preserved=True,
            original_factor_residual_and_domain_rejection_preserved=True,
            checkpoint_observer_compiled=True, executed_Newton=False,
            transformed_sha256=hashlib.sha256(transformed.encode()).hexdigest()))

        class ForbiddenLiveClient:
            def __init__(self, *a, **k):
                report['Node_worker_start_attempts'] += 1
                raise RuntimeError('No worker may start in this explicit protocol fixture')

        Port = recorded.make_port_class(ForbiddenLiveClient,
            configuration['affine_anchor_packet'], configuration['affine_anchor_ready'],
            argument(arguments, '--source-topic'), release_between_responses=True)
        port = Port(configuration['resume_prior_tail_config'],
            Path(argument(arguments, '--source-topic'))/'repro/source-root',
            options.out_prefix.with_name(options.out_prefix.name+'-tail-fixture'), node_heap=256)
        source = (HERE/'root_actual_neck_bvp.py').read_text()
        node = [node for node in ast.walk(ast.parse(source))
                if isinstance(node,ast.FunctionDef) and node.name == 'solve_coupled'][0]
        method = textwrap.dedent(''.join(source.splitlines(keepends=True)[node.lineno-1:node.end_lineno]))
        namespace = dict(np=np, options=SimpleNamespace(coupling='outer',actual_tail_tol=1e-10),
                         out=options.out_prefix)
        exec(compile(method, '<original-actual-outer-protocol-fixture>', 'exec'), namespace)
        namespace['solve_coupled'].__qualname__ = 'ProtocolFixture.Actual.solve_coupled'

        class Fixture:
            solve_coupled = namespace['solve_coupled']
            M, q = runtime.M, runtime.q
            def ensure_tail(self):
                if self.tail is not port:
                    raise ValueError('Fixture port unexpectedly changed')
            def tail_height(self, value):
                return -self.q*np.asarray(value[2*self.M+1:],float)

        fixture = Fixture()
        fixture.tail, fixture.outer_history, fixture.anchor = port, [], None
        changed_p = arrays['p'].copy()
        changed_p[-1] = np.nextafter(changed_p[-1], np.inf)
        try:
            runtime.restore_anchor(fixture, arrays['x'], arrays['y'], changed_p)
        except ValueError as error:
            if 'complete raw state differs' not in str(error):
                raise
            report['tests'].append(dict(name='one_bit_complete_parameter_mutation_rejected',
                passed=True, error=str(error)))
        else:
            raise AssertionError('A changed raw parameter was not rejected')
        fixture.tail_height = lambda value: +runtime.q*np.asarray(value[2*runtime.M+1:],float)
        try:
            runtime.restore_anchor(fixture, arrays['x'], arrays['y'], arrays['p'])
        except ValueError as error:
            if 'not the complete actual height at the original inner entry' not in str(error):
                raise
            report['tests'].append(dict(name='wrong_original_H0_phase_rejected',passed=True,error=str(error)))
        else:
            raise AssertionError('A changed original phase was not rejected')
        del fixture.tail_height
        runtime.install_affine_on_class(Fixture)

        class BeforeBVP(RuntimeError):
            pass

        def stop_before_bvp(fun, bc, x, y, p, **kw):
            if (fixture.anchor[0].tobytes() != runtime.H0.tobytes() or
                    fixture.anchor[1].tobytes() != runtime.K0.tobytes() or
                    fixture.anchor[2].tobytes() != runtime.J0_full[:runtime.M].tobytes()):
                raise ValueError('The original outer method did not install exact H0/K0/J0')
            raise BeforeBVP('Stopped at the first solve_bvp entry; no BVP was executed')

        scipy.integrate.solve_bvp = stop_before_bvp
        try:
            fixture.solve_coupled(None, None, arrays['x'], arrays['y'], arrays['p'],tol=1e-7)
        except BeforeBVP as error:
            report['tests'].append(dict(name='original_actual_outer_method_H0_restart_before_BVP',
                passed=True, controlled_stop=str(error), record=runtime.anchor_record,
                exact_source_ready_guard_passed=port.provenance['complete_packet_ready_binding'],
                complete_original_tail_sources_checked=port.provenance['all_recorded_tail_source_hashes_checked'],
                live_new_Node_requests=port.provenance['live_new_Node_requests']))
        else:
            raise AssertionError('The protocol fixture unexpectedly returned a BVP result')
        if (report['Node_worker_start_attempts'] or port.provenance['live_new_Node_requests'] or
                runtime.anchor_record['restored_raw_H_equals_H0'] or
                runtime.stats['original_affine_anchor_restorations'] != 1):
            raise ValueError('The saved H0 and pending changed H were conflated')
        report['passed'] = True
    except BaseException as error:
        report['error'] = repr(error)
        raise
    finally:
        scipy.integrate.solve_bvp = old_solve_bvp
        if port is not None:
            port.close()
        runtime.finish()
        report.update(finished=True, seconds=time.monotonic()-begin,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            runtime_source_sha256=runtime.hashes,
            runtime_transforms=runtime.transform_records)
        output.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(event='fixed_merit_affine_protocol_check_complete',
            passed=report['passed'],file=str(output),tests=len(report['tests']),
            Node_worker_start_attempts=report['Node_worker_start_attempts'],
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])),flush=True)


if __name__ == '__main__':
    main()
