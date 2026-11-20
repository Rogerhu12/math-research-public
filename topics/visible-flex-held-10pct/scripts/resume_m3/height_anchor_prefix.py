#!/usr/bin/env python3
"""Recover a prefix initial field from all eight recorded true cut heights.

Only the terminal boundary is changed: H = sigma*q*y_z is prescribed.
The original Frenet equation, domain guard, collocation tolerances and full
physical metric audit remain in use. This is an initializer, not acceptance
of the original linear or nonlinear DN, and not a closed flexible surface.
"""
import argparse
import gzip
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def main():
    parser=argparse.ArgumentParser(description=__doc__,add_help=False)
    parser.add_argument('--height-record',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args,remaining=parser.parse_known_args()
    if '--tail-config' in remaining:
        raise ValueError('Height initialization cannot claim a nonlinear DN solve')
    record=json.loads(args.height_record.read_text())
    if not record['solver_success']:
        raise ValueError('Historical height source did not accept its prefix')
    heights=np.asarray(record['tail_records'][-1]['request']['height'],float)
    if heights.shape!=(8,) or not np.isfinite(heights).all():
        raise ValueError('The recorded complete m3 H8 is required')
    path=Path(__file__).with_name('portable_prefix_continue.py')
    spec=importlib.util.spec_from_file_location('m3_height_driver',path)
    driver=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=driver
    spec.loader.exec_module(driver)
    driver.__doc__=__doc__
    original_module=driver.module
    instances=[]
    original_terminals=[]

    def module(name,path):
        result=original_module(name,path)
        if name=='portable_m3_coupler':
            original_build=result.adaptive.build_classes
            def build(chart):
                Flow,Base=original_build(chart)
                class HeightBVP(Base):
                    def __init__(self,*a,**kw):
                        super().__init__(*a,**kw)
                        if self.M!=len(heights):
                            raise ValueError('Use all eight original physical heights')
                        instances.append(self)
                        original_terminals.append(Base.terminal)
                    def terminal(self,y,par):
                        return (self.bridge.sigma*self.q*y[self.iz:]-heights)/self.bcweights
                    def bc_jac(self,ya,yb,par):
                        A,B,P=super().bc_jac(ya,yb,par)
                        B[self.n:]=0.
                        P[self.n:]=0.
                        B[self.n:,self.iz:]=np.diag(self.bridge.sigma*self.q/self.bcweights)
                        return A,B,P
                return Flow,HeightBVP
            result.adaptive.build_classes=build
        return result

    driver.module=module
    original_command=list(sys.argv)
    sys.argv=[str(path),*remaining,'--outdir',str(args.outdir)]
    driver.main()
    output=args.outdir/'run.json'
    report=json.loads(output.read_text())
    report.update(boundary_kind='historical_true_H_initialization_only',
                  prescribed_physical_height=heights.tolist(),
                  height_record=str(args.height_record.resolve()),
                  height_record_sha256=driver.sha(args.height_record),
                  height_wrapper_sha256=driver.sha(__file__),
                  height_wrapper_command=original_command,
                  original_linear_DN_accepted=False,
                  original_nonlinear_DN_accepted=False)
    if instances and report.get('raw_return'):
        model=instances[-1]
        raw=np.load(args.outdir/report['raw_return']['file'])
        par=raw['p'];model.initial(par)
        try:
            residual=original_terminals[-1](model,raw['y'][:,-1],par)
            report['original_linear_DN_physical_residual']=(residual*model.bcweights).tolist()
        except FloatingPointError as exc:
            report['original_linear_DN_diagnostic_error']=str(exc)
    if 'prefix_audit' in report:
        audit=report['prefix_audit']
        audit['scope']=__doc__
        audit['prescribed_height_defect']=audit.pop('physical_bc_max')
    checkpoint=args.outdir/'checkpoint.json.gz'
    if checkpoint.exists():
        with gzip.open(checkpoint,'rt') as stream:
            saved=json.load(stream)
        saved.update(scope=__doc__,boundary_kind=report['boundary_kind'],
                     original_nonlinear_DN_accepted=False)
        with gzip.open(checkpoint,'wt') as stream:
            json.dump(saved,stream)
        report['checkpoint_sha256']=driver.sha(checkpoint)
    driver.dump(output,report)
    metric=report.get('prefix_audit',{}).get('metric_l1')
    accepted=bool(report.get('solver_success') and not report.get('error')
                  and metric is not None and metric<=1e-6)
    print(json.dumps(dict(event='height_initializer_terminal',
          initializer_accepted=accepted,solver_success=report.get('solver_success'),
          metric_l1=metric,raw=report.get('raw_return',{}).get('file'),
          original_nonlinear_DN_accepted=False)),flush=True)
    return 0 if accepted else 2


if __name__=='__main__':
    sys.exit(main())
