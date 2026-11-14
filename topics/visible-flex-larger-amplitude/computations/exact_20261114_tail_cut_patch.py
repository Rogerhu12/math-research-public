#!/usr/bin/env python3
"""Evaluate a complete outer cut-jet correction on the existing finite tail.

The vector quintic equals the saved prefix-minus-tail 0/1/2 radial jets at
the cut and has zero 0/1/2 jets at the inner edge of a fixed-width band.
All angular derivatives come from that same finite correction polynomial.
The original metric and every tail stage outside the band are retained.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def cardinal(y,n,d=0):
    N=len(y);f=np.fft.rfft(np.asarray(y,dtype=float),axis=0)/N
    q=np.zeros((n//2+1,3),complex);q[:len(f)]=f
    if n>N:q[N//2]*=.5
    k=np.arange(n//2+1)[:,None]
    return np.fft.irfft(q*(1j*k)**d,n=n,axis=0)*n


def norm(v):return float(np.max(np.sqrt((v*v).sum(axis=1))))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('complete','background','base-metric','cut-comparison','cut-arrays','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--width',type=float,default=.01)
    p.add_argument('--metric-source',type=Path,default=Path(__file__).with_name('exact_20261114_background_preserving_metric.py'))
    a=p.parse_args();start=time.monotonic();source_hash=sha(__file__);metric_source_hash=sha(a.metric_source)
    spec=importlib.util.spec_from_file_location('exact_cut_patch_metric',a.metric_source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    complete,r,osc,v,w=m.load_nodes(a.complete);bg=json.loads(a.background.read_text());base=json.loads(a.base_metric.read_text());cut=json.loads(a.cut_comparison.read_text())
    if sha(a.cut_arrays)!=cut['array_sha256']:raise ValueError('Cut arrays changed')
    if sha(a.complete)not in base['input_sha256'].values()or sha(a.background)not in base['input_sha256'].values():raise ValueError('Base metric belongs to other node/background data')
    base_method=base.get('horizontal_rr',{}).get('method')
    if base_method is None and base['source_sha256']=='5ad4a401001f16ebcbb26bdace3fb9bc489ca83a0e7fd4427a73d3c636f9fa2a':
        base_method='nonuniform-difference'  # The measured pre-option source had this single rule.
    if base_method!='nonuniform-difference':raise ValueError('This patch consumes the measured nonuniform-rr base field')
    rows=complete['rows'];ns=len(rows)-1;N=complete['angular'];angles=base['angular_evaluation']
    cutR=r[0];width=np.longdouble(a.width);left=cutR-width
    if not(0<width<cutR-r[-1]):raise ValueError('Patch band must lie inside the finite tail')
    y=osc.copy();y[:,:,2]+=np.array([q['meanPerturbationInnerAnchor']for q in rows],dtype=np.longdouble)[:,None]
    v[:,:,2]-=np.array([q['geometry']['w']for q in rows],dtype=np.longdouble)[:,None]
    w[:,:,2]-=np.array([q['geometry']['w']*q['geometry']['dlogwdx']/q['geometry']['drdx']for q in rows],dtype=np.longdouble)[:,None]
    r=r[::-1].copy();y=y[::-1].copy();v=v[::-1].copy();w=w[::-1].copy()
    for i in range(1,ns):
        hm=r[i]-r[i-1];hp=r[i+1]-r[i]
        w[i,:,:2]=hp/(hm+hp)*(v[i,:,:2]-v[i-1,:,:2])/hm+hm/(hm+hp)*(v[i+1,:,:2]-v[i,:,:2])/hp
    w[0,:,:2]=(v[1,:,:2]-v[0,:,:2])/(r[1]-r[0]);w[-1,:,:2]=(v[-1,:,:2]-v[-2,:,:2])/(r[-1]-r[-2])
    arrays=np.load(a.cut_arrays);reflection=np.array([1.,1.,cut['cut']['reflection_z']])
    delta=[(arrays['prefix_position']-arrays['tail_position'])*reflection,
           (arrays['prefix_radial_first']-arrays['tail_radial_first'])*reflection,
           (arrays['prefix_radial_second']-arrays['tail_rr_nonuniform'])*reflection]
    zero=np.zeros((N,3),dtype=np.longdouble)
    patch=m.angular_jets(m.hermite(zero,delta[0],zero,delta[1],zero,delta[2],width),angles)
    theta=2*np.pi*np.arange(angles)/angles;er=np.c_[np.cos(theta),np.sin(theta),np.zeros(angles)];et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(angles)]
    maxima=dict(metric=0.,kappa=0.,correction_position=0.,correction_r=0.,correction_theta_over_r=0.)
    witnesses={};stages=[];covered=[]
    for si,stage in enumerate(bg['rows']):
        i=ns-1-si
        if r[i+1]<left:continue
        covered.append(si);h=r[i+1]-r[i]
        coeff=m.angular_jets(m.hermite(y[i],y[i+1],v[i],v[i+1],w[i],w[i+1],h),angles)
        sm=sk=0.
        for pt in stage['points']:
            radius=np.longdouble(pt['r']);u=np.clip((radius-r[i])/h,0,1)
            fr=m.evaluate(coeff[0],u,h,1)+er;fr[:,2]+=pt['w'];ft=m.evaluate(coeff[1],u,h)+radius*et
            frr=m.evaluate(coeff[0],u,h,2);frr[:,2]+=pt['wr'];frt=m.evaluate(coeff[1],u,h,1)+et;ftt=m.evaluate(coeff[2],u,h)-radius*er
            if radius>=left:
                t=np.clip((radius-left)/width,0,1)
                b=m.evaluate(patch[0],t,width);br=m.evaluate(patch[0],t,width,1);bt=m.evaluate(patch[1],t,width)
                fr+=br;ft+=bt;frr+=m.evaluate(patch[0],t,width,2);frt+=m.evaluate(patch[1],t,width,1);ftt+=m.evaluate(patch[2],t,width)
                maxima['correction_position']=max(maxima['correction_position'],norm(b))
                maxima['correction_r']=max(maxima['correction_r'],norm(br))
                maxima['correction_theta_over_r']=max(maxima['correction_theta_over_r'],norm(bt/radius))
            E=(fr*fr).sum(1);F=(fr*ft).sum(1);G=(ft*ft).sum(1);Eg=np.longdouble(pt['E'])
            ga=(E-Eg)/Eg;gb=F/(np.sqrt(Eg)*radius);gc=G/radius**2-1
            error=(abs(ga+gc)+np.sqrt((ga-gc)**2+4*gb*gb))/2;j=int(np.argmax(error));value=float(error[j]);sm=max(sm,value)
            if value>maxima['metric']:maxima['metric']=value;witnesses['metric']=dict(stage=si,x=pt['x'],r=pt['r'],theta=float(theta[j]))
            normal=np.cross(fr,ft);normal/=np.sqrt((normal*normal).sum(1))[:,None]
            ee=(frr*normal).sum(1);ff=(frt*normal).sum(1);gg=(ftt*normal).sum(1);det=E*G-F*F
            tr=(ee*G+gg*E-2*ff*F)/det;prod=(ee*gg-ff*ff)/det;kap=(abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*prod)))/2
            j=int(np.argmax(kap));value=float(kap[j]);sk=max(sk,value)
            if value>maxima['kappa']:maxima['kappa']=value;witnesses['kappa']=dict(stage=si,x=pt['x'],r=pt['r'],theta=float(theta[j]))
        stages.append(dict(stage=si,metric=sm,kappa=sk))
    # Report all six endpoint functions, with angular derivatives computed from
    # the same cardinal correction, rather than copied from independent jets.
    tailKeys=['position','radial_first','radial_second','angular_first','mixed','angular_second']
    endpoint={};endpointCardinal={}
    # Work in the aligned physical frame here. The added global mean constant
    # is zero by the same cut convention used by the comparison producer.
    base0=arrays['tail_position'];base1=arrays['tail_radial_first'];base2=arrays['tail_rr_nonuniform']
    patched0=cardinal(base0,angles)+m.evaluate(patch[0],np.longdouble(1),width)*reflection
    patched1=cardinal(base1,angles)+m.evaluate(patch[0],np.longdouble(1),width,1)*reflection
    patched2=cardinal(base2,angles)+m.evaluate(patch[0],np.longdouble(1),width,2)*reflection
    endpointValues=dict(position=patched0,radial_first=patched1,radial_second=patched2,
        angular_first=cardinal(base0,angles,1)+m.evaluate(patch[1],np.longdouble(1),width)*reflection,
        mixed=cardinal(base1,angles,1)+m.evaluate(patch[1],np.longdouble(1),width,1)*reflection,
        angular_second=cardinal(base0,angles,2)+m.evaluate(patch[2],np.longdouble(1),width)*reflection)
    for key in tailKeys:endpoint[key]=norm(endpointValues[key]-cardinal(arrays['prefix_'+key],angles))
    endpointCardinal['angular_first']=norm(endpointValues['angular_first']-cardinal(arrays['prefix_position'],angles,1))
    endpointCardinal['mixed']=norm(endpointValues['mixed']-cardinal(arrays['prefix_radial_first'],angles,1))
    endpointCardinal['angular_second']=norm(endpointValues['angular_second']-cardinal(arrays['prefix_position'],angles,2))
    inner={str(d):norm(m.evaluate(patch[0],np.longdouble(0),width,d))for d in [0,1,2]}
    unchanged=[q for q in base['variants']['correct_background_quadrature']['stage_rows']if q['stage']not in set(covered)]
    allMax=dict(metric=max(maxima['metric'],max(q['metric']for q in unchanged)),kappa=max(maxima['kappa'],max(q['kappa']for q in unchanged)))
    result=dict(schema='actual-A-fixed-g-outer-vector-quintic-patch-v1',finished=True,
        source_sha256_at_start=source_hash,metric_helper_sha256_at_start=metric_source_hash,
        input_sha256={str(q):sha(q)for q in [a.complete,a.background,a.base_metric,a.cut_comparison,a.cut_arrays]},
        width=float(width),inner_radius=float(left),outer_radius=float(cutR),angular_evaluation=angles,
        covered_stages=len(covered),sampled_radial_points=sum(len(bg['rows'][j]['points'])for j in covered),
        correction_endpoint_data_norms=[norm(q)for q in delta],inner_endpoint_zero_jet_residual=inner,
        outer_endpoint_vs_saved_prefix_jets=endpoint,outer_angular_vs_same_cardinal_target=endpointCardinal,
        patch_band_maxima=maxima,patch_band_witnesses=witnesses,whole_finite_tail_sampled_maxima=allMax,
        patched_stage_rows=stages,seconds=time.monotonic()-start,
        definition='B is the vector quintic with inner zero value/r/rr and outer full prefix-minus-base-tail value/r/rr. Position differences use one common cut mean anchor; derivatives and g do not receive independent fits.',
        limitations=['Finite floating sampling only, not a continuous metric/reach bound.',
            'C2 matching is algebraic for the complete endpoint functions in the stated cardinal construction; differences from the independently evaluated saved prefix jets are reported.',
            'A global vertical translation fixes the cut means; the absolute complete-prefix mean integral is not evaluated here.',
            'This corrects the finite outer seam only. It does not produce the inner cap, full closed surface, all-time family or strict exact-isometry existence.'])
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=str(a.out),whole_tail=allMax,patch_band=maxima,endpoint=endpoint,inner=inner,seconds=result['seconds'])),flush=True)


if __name__=='__main__':main()
