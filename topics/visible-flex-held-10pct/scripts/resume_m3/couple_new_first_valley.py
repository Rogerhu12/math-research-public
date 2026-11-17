#!/usr/bin/env python3
"""Use the old metric's original restart only to form a new-design initial field.

The old port is supplied literally. During the old restart that old metric is
still installed; it is then restored to the new port before any new equation
is evaluated. Only beta0 differs; the analytic prefix cut is unchanged, and
the numerical cut representations must satisfy the recorded rounding bound.
No same-metric convergence or accepted new field is inferred from this step.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value


def main():
    p=argparse.ArgumentParser(add_help=False,allow_abbrev=False)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--short-bridge',type=Path,required=True)
    p.add_argument('--restart-port',type=Path,required=True)
    a,rest=p.parse_known_args()
    if '--fixed' in rest or '--preserve-restart-mesh' in rest:
        raise ValueError('This is an explicitly new physical design')
    source=a.source_topic.resolve();c=module('m3_new_valley_coupler',source/'scripts/db6f-prefix-coupled.py')
    flat=module('m3_new_valley_flat',source/'scripts/db6f-prefix-flat-profile.py');flat.install(c.adaptive)
    short=module('m3_new_valley_short',a.short_bridge.resolve());original_install=c.adaptive.old.install_source
    def install(root):original_install(root);short.install()
    c.adaptive.old.install_source=install
    old_port=json.loads(a.restart_port.read_text())
    out=Path(rest[rest.index('--out-prefix')+1]);out.parent.mkdir(parents=True,exist_ok=True)
    record=dict(scope=__doc__,command=[sys.executable,*sys.argv],
                old_port_sha256=hashlib.sha256(a.restart_port.read_bytes()).hexdigest(),
                wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    recfile=out.with_name(out.name+'-design-initializer.json')
    def save():recfile.write_text(json.dumps(record,indent=2)+'\n')
    original_build=c.adaptive.build_classes
    def build(chart):
        Flow,BVP=original_build(chart);original_restart=BVP.restart
        def restart(self,path):
            from curve_stable_prefix_bvp import load_checkpoint
            previous=load_checkpoint(path)
            if self.fixed or not previous.get('solver_success') or not previous.get('tail_seam',{}).get('tail_converged'):
                raise ValueError('Design restart requires a genuinely accepted old coupled state')
            if previous['physical_port_sha256']!=record['old_port_sha256']:
                raise ValueError('Old port is not the literal recorded accepted port')
            current=self.port
            old_parameters=old_port['parameters'];new_parameters=current['parameters']
            if {k:v for k,v in old_parameters.items() if k!='valleyControls'}!={k:v for k,v in new_parameters.items() if k!='valleyControls'}:
                raise ValueError('Only first valley beta may differ')
            old_controls=old_parameters['valleyControls'];new_controls=new_parameters['valleyControls']
            if old_controls[1:]!=new_controls[1:]:
                raise ValueError('All later valley controls must be unchanged')
            r=float(new_parameters['rCut']);w=float(new_parameters['wCut']);second=-7*w/r
            exact_cut=dict(radius=r,backgroundSlope=w,backgroundSecond=second,E=1+w*w,Ep=2*w*second)
            if old_port['cut'].get('_prefix_bridge')!=current['cut'].get('_prefix_bridge'):
                raise ValueError('Prefix bridge design changed')
            cut_gap=0.
            for key,value in exact_cut.items():
                bound=64*abs(np.spacing(max(1.,abs(value))))
                if abs(old_port['cut'][key]-value)>bound or abs(current['cut'][key]-value)>bound:
                    raise ValueError('Cut is not within its explicitly recorded analytic rounding bound: '+key)
                cut_gap=max(cut_gap,abs(old_port['cut'][key]-current['cut'][key]))
            self.port=old_port;self._flow_key=None;self._flow=None
            try:
                x,y,par=original_restart(self,path)
            finally:
                self.port=current;self._flow_key=None;self._flow=None
            flow=self.flow(par[0]);s,_=self.chart(x,par[0]);correction=self.initial(par)-y[:,0]
            cutoff=(flow.Tu if flow.direction=='outward' else flow.Td)/2
            y+=correction[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3
            record['initializer']=dict(old_beta0=old_controls[0],new_beta0=new_controls[0],
                                        old_actual_q=previous['actual_primary_amplitude'],new_q=self.q,
                                        correction_linf=float(abs(correction).max()),nodes=len(x),
                                        old_new_cut_roundoff_linf=cut_gap,cut_rounding_bound_ulps=64,
                                        old_restart_guard_retained=True,new_metric_solve_still_required=True)
            save();print(json.dumps(dict(event='different_metric_prefix_initial',**record['initializer'])),flush=True)
            return x,y,par
        BVP.restart=restart
        return Flow,BVP
    c.adaptive.build_classes=build;save()
    sys.argv=[sys.argv[0],'--source-root',str(source/'repro/source-root')]+rest
    started=time.monotonic()
    try:c.main();record['wrapper_returned']=True
    finally:record['seconds']=time.monotonic()-started;save()


if __name__=='__main__':main()
