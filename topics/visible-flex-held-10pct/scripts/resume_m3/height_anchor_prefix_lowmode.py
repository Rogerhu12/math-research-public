#!/usr/bin/env python3
"""Recover a prefix with one scaled historical height and seven original DNs.

The low-mode height target is a declared initializer condition. When q differs
from the historical .06 value it is scaled by q/.06, not called a measured
true-tail response. All other terminal equations remain the original linear
DN. The full flow, domain guards and sampled metric gates remain unchanged.
Every original nonlinear DN condition is still unpaid by this initializer.
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
    parser.add_argument('--amplitude',type=float,required=True)
    parser.add_argument('--height-count',type=int,default=1)
    args,remaining=parser.parse_known_args()
    if '--tail-config' in remaining:
        raise ValueError('Height initialization cannot claim a nonlinear DN solve')
    record=json.loads(args.height_record.read_text())
    if not record['solver_success']:
        raise ValueError('Historical height source did not accept its prefix')
    heights=np.asarray(record['tail_records'][-1]['request']['height'],float)
    if heights.shape!=(8,) or not np.isfinite(heights).all():
        raise ValueError('The recorded complete m3 H8 is required')
    if not 1<=args.height_count<=8 or not args.amplitude>0:
        raise ValueError('Declare a positive amplitude and 1..8 height conditions')
    historical_q=float(record['q_actual'])
    ratio=args.amplitude/historical_q
    heights=heights[:args.height_count]*ratio**np.arange(1,args.height_count+1)
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
                        if self.M!=8:
                            raise ValueError('This path retains the declared M8 model')
                        instances.append(self)
                        original_terminals.append(Base.terminal)
                    def terminal(self,y,par):
                        residual=super().terminal(y,par)
                        count=len(heights)
                        residual[:count]=(self.bridge.sigma*self.q*y[self.iz:self.iz+count]-heights)/self.bcweights[:count]
                        return residual
                    def bc_jac(self,ya,yb,par):
                        A,B,P=super().bc_jac(ya,yb,par)
                        for j in range(len(heights)):
                            B[self.n+j]=0.
                            B[self.n+j,self.iz+j]=self.bridge.sigma*self.q/self.bcweights[j]
                            P[self.n+j]=0.
                        return A,B,P
                return Flow,HeightBVP
            result.adaptive.build_classes=build
        return result

    driver.module=module
    original_command=list(sys.argv)
    sys.argv=[str(path),*remaining,'--amplitude',str(args.amplitude),'--outdir',str(args.outdir)]
    driver.main()
    output=args.outdir/'run.json'
    report=json.loads(output.read_text())
    report.update(boundary_kind='scaled_low_height_and_original_high_linear_DN_initializer',
                  prescribed_physical_height=heights.tolist(),
                  height_count=len(heights),historical_q=historical_q,
                  initializer_height_amplitude=args.amplitude,
                  height_scaling_kind='(q/historical_q)**mode_index; initializer condition only',
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
        audit['initializer_boundary_max']=audit.pop('physical_bc_max')
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
