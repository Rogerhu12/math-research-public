#!/usr/bin/env python3
"""One fixed mode-damped residual-jet warm on the existing full Hold mesh.

No parameter scan, nonlinear solve, normalization, or geometry audit.
The same scalar/mesh/R/H/analytic lift is retained. Only finite residual-q
jets after s=1 change; all first 819 node triples remain literal copies.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

PARENT_BUNDLE_SHA='401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a'
PARENT_REPORT_SHA='0c499334cebe74f0c417ccb89b5ee4dcf86cb07dfbab1f0d46c0b805f4a71b80'
INPUT_SHA='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
ORACLE_SHA='a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'
M=160

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def cap_lift(s,S,R,H,width,C):
    if s<=S-width:chi=cp=cpp=0.
    elif s>=S:chi,cp,cpp=1.,0.,0.
    else:
        u=(s-S+width)/width
        chi=u*u*u*(10+u*(-15+6*u));cp=30*u*u*(1-u)*(1-u)/width
        cpp=60*u*(1-u)*(1-2*u)/(width*width)
    b=R+(S-s);out=np.array([chi*b,cp*b-chi,cpp*b-2*cp])[:,None]*C
    out[:,2*M+1]+=H*np.array([chi,cp,cpp]);return out

class Reference:
    def __init__(self,full,H):self.f=full;self.H=H
    def angle_curvature(self,tbox):
        f=self.f;h=f.h;o=f.o;lo,hi=Q(tbox[0],h.S),Q(tbox[1],h.S)
        # All requested nodes are s>=1. Uniform derivative bounds are
        # used only to transport uncertain exact segment endpoints.
        km=Q(5,2);k1=Q(4653,1000)*Q(15,8)/f.f
        endpoint_k=[f.K,h.interval(f.kn),h.interval(f.kn),h.interval(f.kp),h.interval(f.kp),(0,0)]
        for t,alpha,k in zip(f.time,f.alpha,endpoint_k):
            tl,th=Q(t[0],h.S),Q(t[1],h.S)
            if lo<=th and hi>=tl:
                fee=max(abs(lo-th),abs(hi-tl))
                return h.add(alpha,o.box(-km*fee,km*fee)),h.add(k,o.box(-k1*fee,k1*fee))
        j=next((j for j in range(5)if lo>Q(f.time[j][1],h.S)and hi<Q(f.time[j+1][0],h.S)),None)
        if j is None:raise ValueError('Reference node did not belong to a fixed exact segment')
        local=o.subtract(tbox,f.time[j])
        if j not in f.ramps:
            k=f.kn if j==1 else f.kp
            return o.subtract(f.alpha[j],h.scale(local,k)),h.interval(k)
        ramp=f.ramps[j];l,r=Q(local[0],h.S),Q(local[1],h.S);mid=(l+r)/2;fee=(r-l)/2
        u=mid/ramp.width;v=10*u**3-15*u**4+6*u**5
        alpha=h.add(ramp.angle(mid),o.box(-km*fee,km*fee))
        k=h.add(h.add(h.scale(ramp.left,1-v),h.scale(ramp.right,v)),o.box(-k1*fee,k1*fee))
        return alpha,k
    def jets(self,tbox,C,*,terminal=False,R=None):
        f=self.f;h=f.h;o=f.o;abox,zbox=f.at_box(tbox)
        z=o.subtract(h.add(h.interval(Q(self.H)),zbox),f.height_increment)
        if terminal:
            values=[R,-1.,0.,self.H,0.,0.]
        else:
            alpha,k=self.angle_curvature(tbox);sn,cs=h.sine_cosine(alpha)
            values=[f.carrier(abox),f.carrier(sn),f.carrier(h.neg(h.multiply(k,cs))),
                    f.carrier(z),f.carrier(cs),f.carrier(h.multiply(k,sn))]
        out=np.array(values[:3])[:,None]*C
        out[:,2*M+1]+=values[3:]
        return out,values

def main(a):
    clock=time.perf_counter();source_sha=sha(__file__)
    for p,want in [(a.parent_bundle,PARENT_BUNDLE_SHA),(a.parent_report,PARENT_REPORT_SHA),(a.input,INPUT_SHA),(a.scalar_source,ORACLE_SHA)]:
        if sha(p)!=want:raise ValueError('Changed fixed mode-damped warm dependency')
    parent=json.loads(a.parent_report.read_bytes());old=np.load(a.parent_bundle,allow_pickle=False)
    arrays={k:np.array(old[k],copy=True)for k in old.files};mesh=arrays['mesh'];qjets=arrays['qjets'];C=arrays['circle_projection']
    if mesh.shape!=(923,)or qjets.shape!=(923,3,482)or mesh[818]!=1:raise ValueError('Require the actual 923-node M160 warm')
    H,R,width=(float(arrays[k])for k in ('Hcap','radius','width'));S=float(mesh[-1]);T=S-1
    data=json.loads(gzip.decompress(a.input.read_bytes()));full=load('mode_damped_exact_hold',a.scalar_source).FullHold(data,a.integer_source,a.hold_source,panels=128)
    reference=Reference(full,H);a1box,_=full.at_box(full.point_box(Q(1)));a1=full.carrier(a1box)
    base1,values1=reference.jets(full.point_box(Q(1)),C)
    difference=qjets[818]-base1
    frequency=np.r_[np.arange(M+1),np.arange(1,M+1),np.arange(M+1)]*2
    rates=np.maximum(1,frequency)/a1
    dy,du,da=difference;p0=dy;p1=du+rates*dy;p2=da+2*rates*du+rates*rates*dy
    tail_reference=[];cut_formula=None;terminal_formula=None
    for i in range(818,len(mesh)):
        definition=parent['true_scalar_nodes'][i]
        tbox=full.affine_time(Q(definition['S_coefficient']),Q(definition['constant']))
        base,scalars=reference.jets(tbox,C,terminal=i==len(mesh)-1,R=R)
        t=float(mesh[i]-1);u=t/T
        if i==818:zeta,zp,zpp=1.,0.,0.
        elif i==len(mesh)-1:zeta,zp,zpp=0.,0.,0.
        else:
            zeta=1-u*u*u*(10+u*(-15+6*u));zp=-30*u*u*(1-u)*(1-u)/T
            zpp=-60*u*(1-u)*(1-2*u)/(T*T)
        poly=p0+t*p1+.5*t*t*p2;polyp=p1+t*p2;polyd2=p2
        exp=np.exp(-rates*t);e0=exp*poly;e1=exp*(polyp-rates*poly)
        e2=exp*(polyd2-2*rates*polyp+rates*rates*poly)
        delta=np.stack((zeta*e0,zp*e0+zeta*e1,zpp*e0+2*zp*e1+zeta*e2))
        value=base+delta-cap_lift(float(mesh[i]),S,R,H,width,C)
        if i==818:cut_formula=value.copy()
        elif i==len(mesh)-1:terminal_formula=value.copy();qjets[i]=0.
        else:qjets[i]=value
        tail_reference.append(scalars)
    if not np.isfinite(qjets).all()or not np.array_equal(qjets[:819],old['qjets'][:819]):raise ValueError('Prefix changed or nonfinite candidate')
    if np.any(qjets[-1]!=0):raise ValueError('Terminal affine port failed')
    if sha(__file__)!=source_sha:raise ValueError('Producer changed during generation')
    arrays['mode_rates']=rates;arrays['cut_reference_three_jets']=base1;arrays['cut_difference_three_jets']=difference
    arrays['tail_reference_a_ap_app_z_zp_zpp']=np.array(tail_reference)
    bundle=a.out.with_suffix('.npz');np.savez_compressed(bundle,**arrays)
    report=dict(schema='fullclosed-hold-single-mode-damped-warm-v1',source_sha256=source_sha,
        parent_bundle_sha256=PARENT_BUNDLE_SHA,parent_report_sha256=PARENT_REPORT_SHA,
        raw_pulse_sha256=INPUT_SHA,scalar_source_sha256=ORACLE_SHA,bundle_path=str(bundle),bundle_sha256=sha(bundle),
        M=M,J=923,cells=922,stages=1845,free_size=parent['free_size'],S_carrier=S,radius_carrier=R,Hcap=H,
        scalar_and_symbolic_mesh_identity='unchanged parent exact Hold a/S/R and affine-in-S node definitions',
        fixed_rates='max(1,2j)/a(1) for every R-cos/T-sin/Z-cos mode; same rate 1/a(1) for both means',
        a1_box=full.enclosure(a1box),a1_carrier=a1,mode_rate_min=float(rates.min()),mode_rate_max=float(rates.max()),
        reference_baseline='B(s)=a(s)*C_M + [H-zref(S)+zref(s)]ez, with same finite warm circle C_M; full physical lift remains analytic',
        formula='delta=zeta*exp(-lambda*t)*(dY+(dU+lambda*dY)*t+(dA+2lambda*dU+lambda^2*dY)*t^2/2), zeta=1-S5(t/T)',
        all_three_jets_evaluated_analytically=True,prefix_819_triples_bitwise_identical=True,
        cut_formula_roundoff_by_jet=np.max(np.abs(cut_formula-qjets[818]),axis=1).tolist(),
        terminal_formula_roundoff_by_jet=np.max(np.abs(terminal_formula),axis=1).tolist(),
        baseline_cut_scalars=values1,cut_difference_coefficient_l1_by_jet=np.sum(np.abs(difference),axis=1).tolist(),
        terminal_q_three_jets_exact_zero=True,core_and_first3_unchanged=True,
        all_parent_arrays_except_qjets_unchanged=True,one_design_only=True,parameter_scan=False,
        nonlinear_solve=False,geometry_readout_executed=False,metric_accepted=False,embedding_certified=False,reach_certified=False,
        floating_generation_scope='Literal output jets define the new exact C2 quintic field. Analytic damping formula and scalar boxes guide one floating evaluation; no full enclosure of its rounded geometric jets is asserted.',
        seconds=time.perf_counter()-clock)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True);print(json.dumps(dict(report_sha256=sha(a.out))),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('parent-bundle','parent-report','input','scalar-source','integer-source','hold-source','out'):p.add_argument('--'+k,type=Path,required=True)
    main(p.parse_args())
