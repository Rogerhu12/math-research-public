"""A frozen finite prefix metric with a regular exact flat-annulus cut.

This is a physical candidate and a pole-free rotational initial field, not a
nonround solution.  No linear tail direction is imposed.  The old feedback
prefix and its central circumference are retained; a shorter phase-controlled
contraction leaves positive radial room for the exact r=.8 flat cut.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import copy
import importlib.util
import json
import math
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('flat_cut_family',HERE/'fd2d-wider-cut-prefix-screen.py')
wide=importlib.util.module_from_spec(spec);spec.loader.exec_module(wide)
fm=wide.fm


def build(source,*,vmid=.4,contraction_curvature=6.8,early_curvature=3.4,
          ramp=.04,coast=.02,deep_phase=1.45,brake_length=.04,cylinder=.5):
    # This temporary positive-w description is replaced before any Candidate
    # is constructed.  Its old tail direction is deliberately discarded.
    b=wide.provisional_bundle(source,vmid,.8,.1,5.,deep_phase)
    ids={q.get('label'):j for j,q in enumerate(b['segments'])}
    ie=ids['partial_return_acceleration_entry'];ip=ids['partial_return_acceleration_plateau'];ix=ids['partial_return_acceleration_exit']
    original=[copy.deepcopy(b['segments'][j]) for j in (ie,ip,ix)]
    jet=original[0]['jet0'];phi0=math.asin(jet[1]);ps0=jet[2]/math.cos(phi0)
    phi1=-math.asin(vmid);entry_end=phi0+ramp*(ps0-contraction_curvature)/2
    exit_start=phi1+contraction_curvature*ramp/2
    plateau=(entry_end-exit_start)/contraction_curvature
    if plateau<=0:raise ValueError('The phase contraction needs a positive plateau')
    b['segments'][ie]=dict(kind='phase_bridge',p0=phi0,p1=entry_end,L=ramp,
        ps0=ps0,ps1=-contraction_curvature,start_from_previous=True,
        start_second_from_previous=True,label='partial_return_acceleration_entry')
    b['segments'][ip]=dict(kind='phase_bridge',p0=entry_end,p1=exit_start,L=plateau,
        ps0=-contraction_curvature,ps1=-contraction_curvature,start_from_previous=True,
        label='partial_return_acceleration_plateau')
    b['segments'][ix]=dict(kind='phase_bridge',p0=exit_start,p1=phi1,L=ramp,
        ps0=-contraction_curvature,ps1=0.,start_from_previous=True,
        label='partial_return_acceleration_exit')
    early=b['segments'][ids['early_shallow_return']]
    early.update(K=early_curvature,L=abs(early['p1']-phi1)/(.92*early_curvature),length_from_turn_rate=True)
    b['segments'][0]['L']=cylinder
    b['segments'][ids['partial_return_matching_coast']]['L']=coast
    b['segments'][ids['redeepen_after_partial_return']]['p1']=-deep_phase
    deep=b['segments'][ids['final_deep_coast']]
    deep.update(p0=-deep_phase,p1=-deep_phase,radius_after_next=.8)
    ib=ids['cut_second_jet_brake']
    b['segments'][ib]=dict(kind='phase_bridge',p0=-deep_phase,p1=-math.pi/2,
        L=brake_length,ps0=0.,ps1=0.,start_from_previous=True,
        label='flat_cut_quadratic_brake',exact_endpoint_phase='-pi/2')
    for key in ('finite_linear_screen','full_m2_amplification','metric_diagnostics',
                'provisional_tail_target','moderate_deep_design','fixed_tail_design'):
        b.pop(key,None)
    b['cut_reference']=dict(r=.8,w=0.,wr=0.,meaning='Exact flat metric endpoint; do not divide by w or reference n')
    b['cut']=dict(r=.8,a_prime=-1.,a_second=0.,gaussian_curvature=0.,
        cuff_radius=.32,flat_collar_radius=.34,tail_metric='dr^2+r^2 du^2',
        tail_definition='R128 integral-defined exact developable annulus',
        tail_bending_amplitude_interval=[0.,1.2],tail_bending_amplitude_initial=0.,
        plane_height_unknown=True,linear_DN_not_used=True,complete_two_jet_required=True)
    b['inputs']={k:v for k,v in b.get('inputs',{}).items() if not k.startswith('tail_')}
    b['flat_cut_design']=dict(vmid=vmid,contraction_curvature=contraction_curvature,
        early_return_curvature=early_curvature,ramp_length=ramp,coast_length=coast,
        deep_phase=deep_phase,brake_length=brake_length,cylinder_length=cylinder,
        old_contraction_pieces=original,contraction_plateau_length=plateau,
        physical_metric_changed=True,
        terminal_phase='-pi/2 + O((s_cut-s)^2); phase speed tends to zero',
        reference_initialization='Exact rotational embedding for the frozen scalar metric, evaluated by quadrature',
        amplitude='R128 A varies the exact tail embedding without changing the flat tail metric',
        future_design_T='Changing the shallow coast T changes the prefix metric and must be frozen before same-g refinement')
    b['partial_return_design_parameters'].update(vmid=vmid,coast_length=coast,
        epsilon=math.pi/2-deep_phase)
    b['status']=dict(metric_frozen=True,nonlinear_prefix_solved=False,
        nonlinear_tail_matched=False,closed_nonround_surface=False,
        reach_certified=False,strong_target_complete=False)
    return b


class FlatCutCandidate(fm.Candidate):
    """Same scalar reader plus an initialization with no 1/b or 1/n at the cut."""
    def __init__(self,bundle):
        super().__init__(bundle)
        self.height_starts=[];height=0.
        for p in self.segments:
            self.height_starts.append(height);height+=self._height(p,1.)
        self.background_cut_height=height

    def _height(self,p,u):
        if p['kind']=='hermite':
            _,v,_=self._jet(p,u*fm.GX)
            return p['L']*u*float(np.dot(np.sqrt((1-v)*(1+v)),fm.GW))
        return fm.phase_integral(p,u,np.cos)

    def meridian_reference(self,s):
        s=np.atleast_1d(np.asarray(s,float))
        if np.any(s<0) or np.any(s>self.end+1e-12):raise ValueError('Outside prefix')
        ids=np.minimum(np.searchsorted(self.breaks,s,side='right')-1,len(self.segments)-1)
        ids=np.maximum(ids,0)
        values={k:np.empty_like(s) for k in ('a','ap','app','b','phase_speed','z')}
        for j in np.unique(ids):
            mask=ids==j;p=self.segments[j];t=np.clip((s[mask]-p['s0'])/p['L'],0,1)
            a,v,acc=self._jet(p,t)
            if p['kind']=='hermite':
                bb=np.sqrt((1-v)*(1+v));ps=acc/bb
            else:
                phase,ps=fm.phase(p,t);bb=np.cos(phase)
            if j==len(self.segments)-1:
                bb=np.where(t==1,0.,bb);ps=np.where(t==1,0.,ps)
                v=np.where(t==1,-1.,v);acc=np.where(t==1,0.,acc)
            z=self.height_starts[j]+np.array([self._height(p,float(q)) for q in t.ravel()]).reshape(t.shape)
            for name,data in zip(values,(a,v,acc,bb,ps,z)):values[name][mask]=data
        values.update(s=s,piece=ids,l=-values['phase_speed'],m=np.zeros_like(s),
                      n=values['b']/values['a'])
        return values

    def reference(self,s,u):
        s,u=np.broadcast_arrays(np.asarray(s,float),np.asarray(u,float))
        shape=s.shape;q=self.meridian_reference(s.ravel());q={k:v.reshape(shape) for k,v in q.items()}
        cs,sn=np.cos(u),np.sin(u);a,v,acc,b,ps,z=(q[k] for k in ('a','ap','app','b','phase_speed','z'))
        zero=np.zeros_like(a)
        X=np.stack((a*cs,a*sn,z),axis=-1)
        Xs=np.stack((v*cs,v*sn,b),axis=-1)
        Xu=np.stack((-a*sn,a*cs,zero),axis=-1)
        Xss=np.stack((acc*cs,acc*sn,-v*ps),axis=-1)
        Xsu=np.stack((-v*sn,v*cs,zero),axis=-1)
        Xuu=np.stack((-a*cs,-a*sn,zero),axis=-1)
        N=np.stack((-b*cs,-b*sn,v),axis=-1);e2=Xu/a[...,None]
        out=dict(q,X=X,X_s=Xs,X_u=Xu,X_ss=Xss,X_su=Xsu,X_uu=Xuu,e1=Xs,e2=e2,N=N)
        out['raw_gc_values']=np.concatenate((q['l'][...,None],q['m'][...,None],q['n'][...,None],X,Xs,e2,N),axis=-1)
        return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=HERE.parent/'notes/2026-11-12-fd2d-moderate-deep-p148-frozen-01.json')
    p.add_argument('--out-prefix',type=Path,required=True)
    a=p.parse_args();started=time.monotonic();stem=a.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use an unused physical input stem')
    b=build(json.loads(a.source.read_text()))
    b['inputs'].update(flat_cut_generator=Path(__file__).name,flat_cut_generator_sha256=fm.digest(__file__),
        historical_candidate=a.source.name,historical_candidate_sha256=fm.digest(a.source),
        scalar_reader_sha256=fm.digest(HERE/'fd2d_frozen_ellipse_candidate.py'))
    candidate=FlatCutCandidate(b)
    coasts=[dict(label=q.get('label'),length=q['L']) for q in candidate.segments if q['kind'] in ('coast','coast_to')]
    if any(q['length']<=0 for q in coasts):raise ValueError('Positive physical coasts required')
    s=np.unique(np.concatenate([np.linspace(q['s0'],q['s1'],33) for q in candidate.segments]))
    ref=candidate.meridian_reference(s)
    sample=stem.with_name(stem.name+'-meridian.npz');np.savez_compressed(sample,**ref)
    out=stem.with_name(stem.name+'-candidate.json');out.write_text(json.dumps(b,indent=2)+'\n')
    angles=2*np.pi*np.arange(32)/32;cut=candidate.reference(np.full(32,candidate.end),angles)
    expectedX=np.column_stack((.8*np.cos(angles),.8*np.sin(angles),np.full(32,candidate.background_cut_height)))
    expectedXs=np.column_stack((-np.cos(angles),-np.sin(angles),np.zeros(32)))
    expectedXu=np.column_stack((-.8*np.sin(angles),.8*np.cos(angles),np.zeros(32)))
    expectedXsu=np.column_stack((np.sin(angles),-np.cos(angles),np.zeros(32)))
    expectedXuu=np.column_stack((-.8*np.cos(angles),-.8*np.sin(angles),np.zeros(32)))
    expected=dict(X=expectedX,X_s=expectedXs,X_u=expectedXu,X_ss=np.zeros((32,3)),X_su=expectedXsu,X_uu=expectedXuu)
    scalar=candidate.metric_diagnostics()
    report=dict(schema='fd2d-flat-cut-prefix-physical-candidate-v1',source_sha256=fm.digest(__file__),
        candidate_file=out.name,candidate_sha256=fm.digest(out),
        scalar_metric=scalar,background_cut_height=candidate.background_cut_height,
        positive_coasts=coasts,meridian_length=candidate.end,central_a0=candidate.a0,
        sampled_minimum_radius=float(ref['a'].min()),sampled_maximum_radius=float(ref['a'].max()),
        sampled_maximum_meridian_curvature=float(abs(ref['phase_speed']).max()),
        sampled_minimum_outward_support=float((ref['a']*ref['b']-ref['z']*ref['ap']).min()),
        cut_scalar=dict(a=float(ref['a'][-1]),ap=float(ref['ap'][-1]),app=float(ref['app'][-1]),
            b=float(ref['b'][-1]),l=float(ref['l'][-1]),n=float(ref['n'][-1])),
        actual_A0_complete_cut_jet_errors={k:float(abs(cut[k]-v).max()) for k,v in expected.items()},
        meridian_file=sample.name,meridian_sha256=fm.digest(sample),
        raw_gc_layout=['l','m','n','X[3]','e1[3]','e2[3]','N[3]'],
        scope='One explicit new physical metric and its regular rotational initialization. No nonlinear central deformation, nonzero-A seam solution or strong-target certificate.',
        seconds=time.monotonic()-started)
    report_path=stem.with_name(stem.name+'-report.json');report_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__=='__main__':main()
