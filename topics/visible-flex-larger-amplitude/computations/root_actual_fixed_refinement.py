#!/usr/bin/env python3
"""Refine one actual finite prefix--nonlinear-tail problem at fixed metric.

--fixed-reference is the immutable baseline checkpoint defining the physical
profile, tail metric, gauge and material-angle chart. --restart may be that
checkpoint or a later refinement of it. All core support coefficients are
unknown boundary data; no meridian design parameter is optimized. The same
actual-tail acceptance and complete-vector D-N map remain in force.

This solves a finite joined problem, not an exact infinite-tail closure.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
import root_radial_batching as radial

HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':')).encode()


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--fixed-reference',type=Path,required=True)
    parser.add_argument('--frozen-port',type=Path)
    options,remaining=parser.parse_known_args()
    with gzip.open(options.fixed_reference,'rt') if options.fixed_reference.suffix=='.gz' else options.fixed_reference.open() as handle:
        reference=json.load(handle)
    if not reference.get('solver_success',False):
        raise ValueError('The fixed reference must be an actually successful checkpoint')
    if not reference['config'].get('actual_nonlinear_tail',False):
        raise ValueError('Use an actually coupled nonlinear-tail checkpoint as the fixed reference')
    if reference.get('angular_chart')!='general-support-core-blend-v1':
        raise ValueError('This adapter requires the recorded general material-angle chart')

    def argument(name):
        if name not in remaining:
            raise ValueError('Required argument '+name)
        return Path(remaining[remaining.index(name)+1])

    out=argument('--out-prefix')
    port_file=argument('--port')
    utility=module('root_actual_fixed_utility',HERE/'geometric-fixed-dual-prefix.py')
    _,port_check=utility.verify_port(reference,port_file,options.frozen_port)
    profile=reference['frozen_profile']
    gauge=float(reference['gauge_amplitude'])
    if '--profile' in remaining:
        if canonical(json.loads(argument('--profile').read_text()))!=canonical(profile):
            raise ValueError('Provided physical profile differs from the frozen reference')
    else:
        profile_file=out.with_name(out.name+'-frozen-profile.json')
        profile_file.parent.mkdir(parents=True,exist_ok=True)
        profile_file.write_text(json.dumps(profile,indent=2)+'\n')
        remaining+=['--profile',str(profile_file)]
    if '--q' in remaining:
        if float(remaining[remaining.index('--q')+1])!=gauge:
            raise ValueError('Gauge amplitude must remain identical to the reference')
    else:
        remaining+=['--q',repr(gauge)]
    if '--newton-backend' not in remaining:
        remaining+=['--newton-backend','refresh']
    if '--restart' not in remaining:
        remaining+=['--restart',str(options.fixed_reference)]
    if '--warm-scale' in remaining:
        raise ValueError('Amplitude-scaled warm deformations are disabled for fixed-metric refinement')
    if '--meridian-chart' in remaining and remaining[remaining.index('--meridian-chart')+1]!='all-knots':
        raise ValueError('This finite-neck refinement uses the positive all-knots numerical coordinate')

    provenance=dict(
        fixed_reference=str(options.fixed_reference),
        fixed_reference_sha256=hashlib.sha256(options.fixed_reference.read_bytes()).hexdigest(),
        physical_profile_sha256=hashlib.sha256(canonical(profile)).hexdigest(),
        physical_tail_parameters_sha256=hashlib.sha256(canonical(reference['physical_tail_parameters'])).hexdigest(),
        physical_cut_sha256=hashlib.sha256(canonical(reference['physical_tail_cut'])).hexdigest(),
        chart_reference_coefficients=reference['chart_reference_coefficients'],
        chart_reference_frequencies=reference['chart_reference_frequencies'],
        gauge_amplitude=gauge,physical_length=reference['meridian_length'],
        port_verification=port_check,
        adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        radial_batching_sha256=hashlib.sha256((HERE/'root_radial_batching.py').read_bytes()).hexdigest(),
        radial_batch_size=48,
        scope='Physical metric and reference chart frozen. Core coefficients are solved fields, not changed design controls. Finite tail only.')

    actual=module('root_actual_fixed_coupling',HERE/'root_actual_neck_bvp.py')
    # Preserve an enclosing bounded/direct-block loader through this extra
    # fixed-metric layer. Ordinary direct invocation still uses this module's
    # unchanged importlib loader.
    actual.module=module
    original_loader=actual.module

    def load_with_fixed_factory(name,path):
        loaded=original_loader(name,path)
        if name!='root_actual_dual':
            return loaded
        source_factory=loaded.make_dual

        def fixed_factory(adaptive,charts,chart,*unused,**kwargs):
            # Keep an immutable factory reference: utility.make_fixed must not
            # recursively call the replacement installed below.
            Base=utility.make_fixed(SimpleNamespace(make_dual=source_factory),
                adaptive,charts,chart,reference['chart_reference_coefficients'],
                reference['chart_reference_frequencies'])

            class Fixed(Base):
                def __init__(self,cfg,port,q,M,angular):
                    # The neck's all-knots initialization constructs a flow
                    # during the parent initializer; set its chart order first.
                    self.ref_frequencies=list(reference['chart_reference_frequencies'])
                    if canonical(cfg)!=canonical(profile) or float(q)!=gauge:
                        raise ValueError('Physical metric or gauge changed before construction')
                    super().__init__(cfg,port,q,M,angular)
                    if canonical(self.port['parameters'])!=canonical(reference['physical_tail_parameters']):
                        raise ValueError('Physical tail parameters changed')
                    if canonical(self.port['cut'])!=canonical(reference['physical_tail_cut']):
                        raise ValueError('Physical tail cut changed')
                    if abs(self.flow().end-reference['meridian_length'])>2e-13:
                        raise ValueError('Physical meridian length changed')
                    self.fixed_metric_provenance=provenance

                def restart_from(self,saved,pullback,nodes,warm_scale):
                    t,y,p,record=self.restart_fixed(saved,pullback,nodes)
                    record['fixed_metric_provenance']=provenance
                    return t,y,p,record

                def fun(self,t,y,p):
                    f=self.flow();s,ds=self.chart(t,0.)
                    return ds[None,:]*radial.value(f,s,y,p)

                def fun_jac(self,t,y,p):
                    f=self.flow();s,ds=self.chart(t,0.)
                    J=radial.state_jacobian(f,s,y,p)
                    J*=ds[None,None,:]
                    return J,np.zeros((self.n,self.M,len(t)))

            return Fixed

        loaded.make_dual=fixed_factory
        return loaded

    actual.module=load_with_fixed_factory
    sys.argv=[sys.argv[0]]+remaining
    actual.main()


if __name__=='__main__':
    main()
