#!/usr/bin/env python3
"""Exercise both real source wrapper layers up to, but not inside, solve_bvp.

This is an explicit protocol fixture on the full saved raw arrays and audited
tail packet. It includes the production first-request guard omitted from the
earlier fixture. It performs no physical RHS, global Jacobian, BVP or Node.
"""
from __future__ import annotations
import argparse
import ast
import copy
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

from strong_actual_fixed_control_response import raw_flat
from strong_actual_recorded_tail_port import make_port_class
from strong_physical_merit_actual_bvp import argument, prepare_configuration
from strong_physical_merit_and_affine_resume import Runtime
import strong_physical_merit_actual_bvp_v2 as corrected

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path = Path(path)
    contents = path.read_bytes()
    return json.loads(gzip.decompress(contents) if path.suffix == '.gz' else contents)


def function_source(source, name):
    nodes = [node for node in ast.walk(ast.parse(source))
             if isinstance(node,ast.FunctionDef) and node.name == name]
    if len(nodes) != 1:
        raise ValueError('Expected one actual source method: '+name)
    node = nodes[0]
    return textwrap.dedent(''.join(source.splitlines(keepends=True)[node.lineno-1:node.end_lineno]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--failed-r3-adapter', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    args = parser.parse_args()
    output = args.out_prefix.with_suffix('.json')
    if output.exists():
        raise FileExistsError('Use a fresh first-request protocol output')
    begin = time.monotonic()
    hashes = {str(p): sha(p) for p in (args.plan,args.failed_r3_adapter,Path(__file__))}
    arguments = document(args.plan)['run_argv'][2:]
    configuration = prepare_configuration(arguments,
        Path(argument(arguments,'--resume-original-affine-anchor')),
        Path(argument(arguments,'--original-inner-entry-raw')),
        Path(argument(arguments,'--original-inner-entry-tail-config')))
    runtime = Runtime(configuration,args.out_prefix)
    runtime.hashes[str(HERE/'strong_physical_merit_actual_bvp_v2.py')] = sha(HERE/'strong_physical_merit_actual_bvp_v2.py')
    report = dict(scope=__doc__,finished=False,passed=False,source_sha256=hashes,
        physical_RHS_evaluations=0,global_Jacobian_evaluations=0,BVP_solves=0,
        Node_worker_start_attempts=0,nonlinear_solution=False,tests=[])
    original_solve = scipy.integrate.solve_bvp
    port = None
    try:
        raw_path = Path(configuration['resume_raw'])
        raw = document(raw_path)
        arrays = {key: np.asarray(raw_flat(raw_path,raw,key,hashes),float).reshape(raw['arrays'][key]['shape'])
                  for key in ('x','y','p')}
        disk_configuration = dict(temporary_parent=None,backward_error_tolerance=5e-11,heartbeat_seconds=20.)
        source, provenance = corrected.build_source(configuration,disk_configuration)
        previous_source,_ = corrected.BASE_BUILD_SOURCE(configuration,disk_configuration)
        report['production_source_transform'] = provenance

        class NoWorker:
            def __init__(self,*a,**k):
                report['Node_worker_start_attempts'] += 1
                raise RuntimeError('No Node may start during this protocol fixture')
        Port = make_port_class(NoWorker,configuration['affine_anchor_packet'],
            configuration['affine_anchor_ready'],argument(arguments,'--source-topic'),
            release_between_responses=True)
        port = Port(configuration['resume_prior_tail_config'],
            Path(argument(arguments,'--source-topic'))/'repro/source-root',
            args.out_prefix.with_name(args.out_prefix.name+'-tail-fixture'),node_heap=256)
        namespace = dict(np=np,options=SimpleNamespace(coupling='outer',actual_tail_tol=1e-10),out=args.out_prefix)
        method = function_source((HERE/'root_actual_neck_bvp.py').read_text(),'solve_coupled')
        exec(compile(method,'<actual-outer-method-protocol-fixture>','exec'),namespace)
        namespace['solve_coupled'].__qualname__ = 'ProtocolFixture.Actual.solve_coupled'

        class Fixture:
            solve_coupled = namespace['solve_coupled']
            M,q = runtime.M,runtime.q
            def ensure_tail(self):
                if self.tail is not port:raise ValueError('Changed fixture port')
            def tail_height(self,value):
                return -self.q*np.asarray(value[2*self.M+1:],float)
        runtime.install_affine_on_class(Fixture)
        obj = Fixture()
        obj.tail,obj.anchor,obj.outer_history,obj.design_provenance = port,None,[],{}
        tail_warm = copy.deepcopy(document(configuration['affine_anchor_packet'])['response']['checkpoint'])
        wrapper_namespace = dict(np=np,json=json,recorder=SimpleNamespace(obj=None),
            tail_warm=tail_warm,
            tail_warm_info=document(args.failed_r3_adapter)['explicit_same_H_tail_warm_recovery'],
            options=SimpleNamespace(inspect_local_output=None,inspect_warm_output=None),
            merit_runtime=runtime,solve=Fixture.solve_coupled)

        class BeforeBVP(RuntimeError):pass
        def stop_before_bvp(fun,bc,x,y,p,**kw):
            if (obj.anchor[0].tobytes()!=runtime.H0.tobytes() or
                    obj.anchor[1].tobytes()!=runtime.K0.tobytes() or
                    obj.anchor[2].tobytes()!=runtime.J0_full[:runtime.M].tobytes()):
                raise ValueError('Both wrapper layers did not install the exact original affine anchor')
            raise BeforeBVP('Both actual source layers reached solve_bvp with original H0/K0/J0; no solve executed')
        scipy.integrate.solve_bvp = stop_before_bvp
        previous = dict(wrapper_namespace)
        exec(compile(function_source(previous_source,'coupled'),'<prior-upper-first-request-guard>','exec'),previous)
        try:
            previous['coupled'](obj,None,None,arrays['x'],arrays['y'],arrays['p'],tol=1e-7)
        except ValueError as error:
            if 'does not match the first live actual request' not in str(error):raise
            report['tests'].append(dict(name='prior_r3_upper_guard_failure_reproduced',passed=True,error=str(error)))
        else:raise AssertionError('Prior wrapper did not reproduce the recorded guard failure')

        exec(compile(function_source(source,'coupled'),'<corrected-upper-first-request-guard>','exec'),wrapper_namespace)
        coupled = wrapper_namespace['coupled']
        old_H = tail_warm['cutHeight'][:]
        tail_warm['cutHeight'][0] = float(np.nextafter(old_H[0],np.inf))
        try:
            coupled(obj,None,None,arrays['x'],arrays['y'],arrays['p'],tol=1e-7)
        except ValueError as error:
            if 'does not match the first live actual request' not in str(error):raise
            report['tests'].append(dict(name='one_bit_saved_first_H0_mismatch_rejected',passed=True,error=str(error)))
        else:raise AssertionError('Changed complete first-request H was not rejected')
        tail_warm['cutHeight'] = old_H

        changed_p = arrays['p'].copy()
        changed_p[-1] = np.nextafter(changed_p[-1],np.inf)
        try:
            coupled(obj,None,None,arrays['x'],arrays['y'],changed_p,tol=1e-7)
        except ValueError as error:
            if 'complete raw state differs' not in str(error):raise
            report['tests'].append(dict(name='one_bit_pending_raw_parameter_rejected_through_both_layers',passed=True,error=str(error)))
        else:raise AssertionError('Changed full raw state was not rejected through the corrected wrapper')

        try:
            coupled(obj,None,None,arrays['x'],arrays['y'],arrays['p'],tol=1e-7)
        except BeforeBVP as error:
            report['tests'].append(dict(name='corrected_two_layer_original_H0_protocol',passed=True,
                controlled_stop=str(error),original_affine_anchor=runtime.anchor_record,
                upper_wrapper_identity=obj.design_provenance['same_H_tail_warm_recovery']))
        else:raise AssertionError('Fixture unexpectedly produced a BVP result')
        if (report['Node_worker_start_attempts'] or port.provenance['live_new_Node_requests'] or
                runtime.anchor_record['restored_raw_H_equals_H0'] or
                obj.design_provenance['same_H_tail_warm_recovery']['current_raw_H_audited_here']):
            raise ValueError('The original H0 request and pending current H were conflated')
        report['passed'] = True
    except BaseException as error:
        report['error'] = repr(error)
        raise
    finally:
        scipy.integrate.solve_bvp = original_solve
        if port is not None:port.close()
        runtime.finish()
        report.update(finished=True,seconds=time.monotonic()-begin,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            runtime_source_sha256=runtime.hashes,runtime_transforms=runtime.transform_records)
        output.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(event='two_layer_first_request_check_complete',passed=report['passed'],
            file=str(output),tests=len(report['tests']),seconds=report['seconds'],
            peak_rss_kib=report['peak_rss_kib'],Node_worker_start_attempts=report['Node_worker_start_attempts'])),flush=True)


if __name__ == '__main__':main()
