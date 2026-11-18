#!/usr/bin/env python3
"""One independent same-design run with the missing original RMS-point guard.

Preparation is metadata/source only. The original failed entry is preserved.
The new run uses the one original q060 circle-trace initializer and all original
physical/finite parameters. Only Newton trial-domain coverage and interior
state recording differ; it is not a replay to manufacture a missing old state.
"""
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
PARENT=HERE/'run_q060_circle_trace_coupled.py'
PARENT_SHA='1204d93ce144efec9d61d34de7af189e4c597d3c1bf85090a1f7bcbae7c020f3'
GUARD=HERE/'m3_lobatto_domain_guard.py'


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj


def main():
    parent=module('frozen_q060_circle_coupled_parent',PARENT)
    if parent.sha(PARENT)!=PARENT_SHA:raise ValueError('The first frozen coupled entry changed')
    parser=argparse.ArgumentParser(description=__doc__)
    option=parser.add_mutually_exclusive_group(required=True)
    option.add_argument('--prepare',type=Path);option.add_argument('--run-plan',type=Path)
    args=parser.parse_args()
    guard=module('q060_circle_lobatto_guard',GUARD)
    if args.prepare is not None:
        import scipy
        import scipy.integrate._bvp as bvp
        directory=args.prepare.resolve()
        parent.prepare(directory)
        basefile=directory/'launch-plan.json';base=parent.load(basefile);plan=copy.deepcopy(base)
        plan.pop('identity_sha256')
        domain_path=Path(next(p for p in base['source_sha256'] if p.endswith('/f6curve_domain_newton.py')))
        code=guard.recording_newton_source(domain_path)
        excerpt=directory/'recording-newton-excerpt.py'
        with excerpt.open('x') as stream:stream.write(code)
        plan['runner']=parent.ref(__file__)
        plan['unchanged_parent_plan']=parent.ref(basefile)
        plan['source_sha256'].update({str(Path(__file__).resolve()):parent.sha(__file__),
            str(GUARD):parent.sha(GUARD),str(Path(bvp.__file__).resolve()):parent.sha(bvp.__file__)})
        plan['lobatto_guard']=dict(source=parent.ref(GUARD),scipy_version=scipy.__version__,
            scipy_bvp=parent.ref(bvp.__file__),original_domain_newton=parent.ref(domain_path),
            recording_newton_source=parent.ref(excerpt),
            exact_point_rule='xmid=x[:-1]+0.5*h; s=0.5*h*(3/7)**0.5; x1=xmid+s; x2=xmid-s',
            exact_state_rule='Original create_spline(Y,ff,x,h), using ff from the original col_fun four-tuple',
            guard_rule='Original fun_wrapped at x1 then x2; propagate the same FloatingPointError to original domain backtracking; return the unchanged original four-tuple',
            no_new_RMS_or_merit_acceptance=True,
            observation_rule='Save full raw state before initial Newton evaluation, after its first successful evaluation, after each accepted assignment, before both returns, and the actual last evaluation on escaping exception. Save node ff and original cubic whenever available, plus the actual fixed inner DN anchor.')
        plan['scope']=__doc__
        plan['single_algorithm_change']='Add the two missing original RMS Lobatto-domain evaluations to the original Newton col_fun; preserve every equation and threshold.'
        plan['identity_sha256']=parent.payload_sha(plan)
        path=directory/'lobatto-launch-plan.json';parent.write_json(path,plan)
        command=[sys.executable,str(Path(__file__).resolve()),'--run-plan',str(path)]
        observer=[sys.executable,str(parent.OBSERVER),'--out',str(directory/'resource.json'),
                  '--log',str(directory/'stdout.log'),'--',*command]
        parent.write_json(directory/'lobatto-launch-command.json',dict(plan=parent.ref(path),command=command,observer_command=observer))
        print(json.dumps(dict(plan=parent.ref(path),plan_identity_sha256=plan['identity_sha256'],
            metadata_only=True,source_files=len(plan['source_sha256']),observer_command=observer)),flush=True)
    else:
        class Context(parent.RunContext):
            def install_trace(self):
                super().install_trace()
                self.lobatto_hook=guard.install(self)
        parent.RunContext=Context
        parent.run(args.run_plan)


if __name__=='__main__':main()
