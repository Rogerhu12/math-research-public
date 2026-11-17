#!/usr/bin/env python3
"""A compact curvature pulse changes the scalar design after the true cut.

Each amplitude defines a different fixed scalar, not a refinement of the
old one. The cut a/a'/a'' agree with the original; the plateau compensates
the pulse's exact total turn so the ideal reference endpoint stays planar.
Finite IVP failures are not accepted prefixes or mathematical obstructions.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np

BASE=Path(__file__).with_name('2026-11-17-parallel-geometry-short-ivp-refine.py')
spec=importlib.util.spec_from_file_location('frozen_high_mode_probe',BASE)
probe=importlib.util.module_from_spec(spec);spec.loader.exec_module(probe)
from parallel_20261117_inward_profile import InwardProfile,primitive,smoothstep


class PulseProfile(InwardProfile):
    def __init__(self,geometry,origin,cut,curvature,ramp_in,ramp_out,quadrature,
                 amplitude,half_width):
        self.pulse_amplitude=float(amplitude);self.pulse_half_width=float(half_width)
        if not 0<2*self.pulse_half_width<=ramp_in:
            raise ValueError('The compact pulse must fit in the first curvature ramp')
        super().__init__(geometry,origin,cut,curvature,ramp_in,ramp_out,quadrature)
        self.alpha1=self.alpha0-self.ramp_in*(self.kappa0+self.curvature)/2-self.pulse_amplitude*self.pulse_half_width
        self.plateau=(self.alpha1+np.pi/2-self.curvature*self.ramp_out/2)/self.curvature
        if self.plateau<=0:raise ValueError('The pulse leaves no constant-curvature interval')
        self.alpha2=self.alpha1-self.curvature*self.plateau
        self.end=self.cut+self.ramp_in+self.plateau+self.ramp_out
        self.shift1=self.transition_integral(self.ramp_in,False)
        self.shift2=self.shift1+np.array([
            (np.cos(self.alpha2)-np.cos(self.alpha1))/self.curvature,
            (np.sin(self.alpha1)-np.sin(self.alpha2))/self.curvature])
        self.shift3=self.shift2+self.transition_integral(self.ramp_out,True)
        self.radius=self.ac+self.shift3[0]
        if self.radius<=0:raise ValueError('The new reference crosses the axis')

    def pulse_integral(self,t):
        w=self.pulse_half_width;z=np.asarray(t)
        u=np.clip(z/w,0.,1.);v=np.clip(z/w-1.,0.,1.)
        return self.pulse_amplitude*w*(primitive(u)+v-primitive(v))

    def pulse_curvature(self,t):
        u=np.clip(np.asarray(t)/self.pulse_half_width,0.,1.)
        v=np.clip(np.asarray(t)/self.pulse_half_width-1.,0.,1.)
        return self.pulse_amplitude*(smoothstep(u)-smoothstep(v))

    def transition_angle(self,t,final):
        angle=super().transition_angle(t,final)
        return angle if final else angle-self.pulse_integral(t)

    def transition_integral(self,t,final):
        if final:return super().transition_integral(t,final)
        breaks=sorted(set([0.,float(t),min(float(t),self.pulse_half_width),
                           min(float(t),2*self.pulse_half_width)]))
        shift=np.zeros(2)
        for a,b in zip(breaks[:-1],breaks[1:]):
            at=self.transition_angle(a+(b-a)*(self.nodes+1)/2,False)
            shift+=(b-a)/2*np.array([self.weights@np.sin(at),self.weights@np.cos(at)])
        return shift

    def meridian(self,s):
        result=super().meridian(s);t=float(s)-self.cut
        if 0<t<self.ramp_in:
            kappa=result['curvature']+float(self.pulse_curvature(t))
            result.update(curvature=kappa,app=-kappa*result['height_s'],height_ss=kappa*result['ap'])
        return result

    def spec(self):
        result=super().spec()
        result['compact_curvature_pulse']=dict(amplitude=self.pulse_amplitude,
            half_width=self.pulse_half_width,total_turn=self.pulse_amplitude*self.pulse_half_width,
            formula='A*(S(t/w)-S(t/w-1)), with S clamped to [0,1]',
            exact_definition='Curvature and exact split position integrals; Gauss32 is only evaluation')
        return result


def main(args):
    reference=json.loads(gzip.decompress(args.reference.read_bytes()))
    metric=json.loads(gzip.decompress(args.metric.read_bytes()))
    if not reference.get('success'):raise ValueError('Accepted original cut required')
    h=probe.h;old=h.Frenet(reference['M'],reference['N'])
    q=h.Frenet(args.modes,args.angles);reader=h.Frenet(args.modes,args.read_angles)
    y=probe.base.lift_states(np.asarray(reference['states'][-1]),old.M,q.M)
    core=np.pad(np.asarray(reference['core']['coefficients']),(0,q.M-old.M))
    start=float(reference['mesh'][-1]);settings=metric['inward_scalar_profile']
    original=h.profile_from(metric)
    report=dict(scope=__doc__,source_sha256=h.sha(__file__),base_sha256=h.sha(BASE),
        reference_sha256=h.sha(args.reference),metric_carrier_sha256=h.sha(args.metric),
        M=q.M,N=q.N,read_angles=reader.N,start=start,end=args.end,max_step=args.max_step,
        rtol=args.rtol,atol=args.atol,half_width=args.half_width,cases=[])
    for amplitude in args.amplitudes:
        profile=PulseProfile(reference['fixed_scalar_profile']['geometry'],reference['analytic_extension_origin'],
            settings['cut'],settings['curvature'],settings['ramp_in'],settings['ramp_out'],settings['quadrature'],
            amplitude,args.half_width)
        case,last=probe.integrate(q,profile,start,args.end,y,args.rtol,args.atol,args.max_step)
        case.update(amplitude=amplitude,scalar=profile.spec(),
            initial_scalar_jet_difference=(np.asarray(profile(start))-np.asarray(original(start))).tolist(),
            reference_length=profile.end-profile.cut,last_valid_coefficients=last.tolist())
        if case['ivp_reached_end']:
            a,ap,_=profile(args.end);v=q.rhs(last,ap/a);local=q.local(last,ap/a)
            case.update(endpoint_RHS_gram=probe.base.gram(reader,last,v,a,core),
                endpoint_sample_H_min=float(local['H'].min()),new_BVP_parent=False,
                actual_C2_join_completed=False)
        report['cases'].append(case)
        args.out.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({k:v for k,v in case.items() if k!='last_valid_coefficients'}),flush=True)
    print(json.dumps(dict(output_sha256=h.sha(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference',type=Path,required=True);p.add_argument('--metric',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--amplitudes',nargs='+',type=float,default=[-.5,.5,1.])
    p.add_argument('--half-width',type=float,default=.001);p.add_argument('--modes',type=int,default=320)
    p.add_argument('--angles',type=int,default=4096);p.add_argument('--read-angles',type=int,default=8192)
    p.add_argument('--end',type=float,default=1.0);p.add_argument('--max-step',type=float,default=.000015625)
    p.add_argument('--rtol',type=float,default=1e-13);p.add_argument('--atol',type=float,default=1e-16)
    main(p.parse_args())
