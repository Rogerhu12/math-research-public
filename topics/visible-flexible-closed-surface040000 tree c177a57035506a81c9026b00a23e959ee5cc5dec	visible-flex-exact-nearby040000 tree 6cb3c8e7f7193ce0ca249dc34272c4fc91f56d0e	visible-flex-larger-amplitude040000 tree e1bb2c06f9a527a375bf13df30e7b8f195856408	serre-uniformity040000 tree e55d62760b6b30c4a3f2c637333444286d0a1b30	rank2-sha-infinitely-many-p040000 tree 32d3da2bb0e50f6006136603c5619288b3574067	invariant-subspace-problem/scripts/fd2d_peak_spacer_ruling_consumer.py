#!/usr/bin/env python3
"""R137 consumer of the saved new34 coast inlet, with explicit passive replay.

The original trajectory saved n,m and their first radial derivatives at all
accepted nodes, but only the FINAL position/frame state.  This script never
pretends that final state is the earlier inlet.  It defines a shared cubic
Hermite n,m field from the saved data, passively integrates only X/e1/e2/N
from the exact central seed, freezes the resulting inlet Fourier field,
and propagates the entire K=0 coast by explicit straight rulings.

This is a new finite representation with independently measured inlet and
surface defects, not a recovered byte-identical intermediate DOP853 state.
It neither solves the n,m PDE nor changes the physical scalar metric.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,gzip,hashlib,io,json,time
from pathlib import Path
import numpy as np
from scipy import fft
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicHermiteSpline
from fd2d_balanced_curvature_core import FixedBalancedGeometry,BalancedCurvatureCore
from fd2d_flat_cut_prefix_candidate import FlatCutCandidate
from fd2d_k0_ruling_coast import propagate,inlet_defects,at_material

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def identity(p):return dict(file=Path(p).name,sha256=digest(p),bytes=Path(p).stat().st_size)


class SpectralInlet:
    """Frozen finite position/frame Fourier field plus the actual saved n,m."""
    def __init__(self,frame_fourier,n_coeff,m_coeff,frequencies,geometry):
        self.raw=np.asarray(frame_fourier,dtype=np.complex128)
        self.n=np.asarray(n_coeff,dtype=np.longdouble);self.m=np.asarray(m_coeff,dtype=np.longdouble)
        self.f=np.asarray(frequencies,dtype=np.longdouble);self.geometry=geometry
        self.wave=np.arange(self.raw.shape[0],dtype=np.longdouble)
        weight=np.full(len(self.wave),2,dtype=np.longdouble);weight[[0,-1]]=1
        self.cos=weight[:,None]*np.asarray(self.raw.real,dtype=np.longdouble)
        self.sin=-weight[:,None]*np.asarray(self.raw.imag,dtype=np.longdouble)
        self.sin[[0,-1]]=0
        self.maximum_material_inverse_input_error=0.

    def at_phi(self,phi):
        phi=np.asarray(phi,dtype=np.longdouble)
        C=np.cos(phi[...,None]*self.wave);S=np.sin(phi[...,None]*self.wave)
        values=C@self.cos+S@self.sin
        first=-S@(self.wave[:,None]*self.cos)+C@(self.wave[:,None]*self.sin)
        second=-C@(self.wave[:,None]**2*self.cos)-S@(self.wave[:,None]**2*self.sin)
        Cn=np.cos(phi[...,None]*self.f);Sn=np.sin(phi[...,None]*self.f)
        n=Cn@self.n;m=Sn[...,1:]@self.m
        np1=-Sn@(self.f*self.n);mp1=Cn[...,1:]@(self.f[1:]*self.m)
        np2=-Cn@(self.f*self.f*self.n);mp2=-Sn[...,1:]@(self.f[1:]**2*self.m)
        chart=self.geometry.material_coordinate(phi);h=chart['u_phi'];hp=chart['u_phi_phi']
        out=dict(u=chart['u'],phi=phi,n=n,m=m,n_u=np1/h,m_u=mp1/h,
            n_uu=(np2-hp*np1/h)/(h*h),m_uu=(mp2-hp*mp1/h)/(h*h))
        for j,name in enumerate(('X','e1','e2','N')):
            value=values[...,3*j:3*j+3];d1=first[...,3*j:3*j+3];d2=second[...,3*j:3*j+3]
            out[name]=value;out[name+'_u']=d1/h[...,None]
            out[name+'_uu']=(d2-(hp/h)[...,None]*d1)/(h*h)[...,None]
        return out

    def at_material(self,u):
        phi=self.geometry.normal_angle(np.asarray(u,dtype=np.longdouble))
        out=self.at_phi(phi)
        self.maximum_material_inverse_input_error=max(self.maximum_material_inverse_input_error,
            float(np.max(abs(out['u']-u))))
        # The callback is evaluated at the requested material argument; the
        # independent numerical inverse discrepancy is explicitly reported.
        out['u']=np.asarray(u,dtype=np.longdouble)
        return out


def summarize_defects(defects):
    return {key:float(np.max(abs(value))) if key=='frame_gram' else
        float(np.max(np.linalg.norm(value,axis=-1))) for key,value in defects.items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,default=ROOT/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    ap.add_argument('--trajectory',type=Path,default=ROOT/'notes/2026-11-12-fd2d-peak-spacer34-cyl032-actual-ivp01-trajectory.npz.gz')
    ap.add_argument('--stem',type=Path,required=True)
    ap.add_argument('--work',type=int,default=768)
    ap.add_argument('--radial-samples',type=int,default=65)
    ap.add_argument('--replay-step',type=float,default=.0005)
    args=ap.parse_args()
    if list(args.stem.parent.glob(args.stem.name+'*')):raise FileExistsError('Use a new consumer output stem')
    args.stem.parent.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    raw=gzip.decompress(args.trajectory.read_bytes()) if args.trajectory.suffix=='.gz' else args.trajectory.read_bytes()
    history=np.load(io.BytesIO(raw),allow_pickle=False)
    if str(history['candidate_sha256'].item())!=digest(args.candidate):raise ValueError('Physical candidate identity mismatch')
    candidate=FlatCutCandidate(json.loads(args.candidate.read_text()))
    piece=next(p for p in candidate.segments if p.get('label')=='outward_peak_spacer')
    a,v,L=piece['a_start'],np.sin(piece['p0']),piece['L'];entry=piece['s0']
    end_index=int(np.argmin(abs(history['s']-entry)))
    if abs(history['s'][end_index]-entry)>2e-14:raise ValueError('No saved shared coast inlet')
    cylinder=candidate.segments[0]['L'];start_index=int(np.argmin(abs(history['s']-cylinder)))
    if abs(history['s'][start_index]-cylinder)>2e-14:raise ValueError('No saved central-cylinder endpoint')
    knots=history['s'][start_index:end_index+1]
    geometry=FixedBalancedGeometry();core=BalancedCurvatureCore((),base_kind='balanced_seed',geometry=geometry)
    phi=np.arange(args.work,dtype=np.longdouble)*(2*np.arccos(np.longdouble(-1))/args.work)
    f=history['frequencies'];C=np.cos(f[:,None]*phi);S=np.sin(f[1:,None]*phi)
    saved=lambda key:np.asarray(history[key][start_index:end_index+1],dtype=np.longdouble)
    values=np.stack((saved('n_phi_cos')@C,saved('m_phi_sin')@S),axis=-1)
    first=np.stack((saved('n_s_phi_cos')@C,saved('m_s_phi_sin')@S),axis=-1)
    field=CubicHermiteSpline(knots,np.asarray(values,float),np.asarray(first,float),axis=0)
    seed=core.evaluate_normal_angle(phi)
    state=np.concatenate([np.asarray(seed[key],float) for key in ('X','e1','e2','N')],axis=1)
    state[:,2]+=cylinder
    calls=0
    def rhs(s,y):
        nonlocal calls
        calls+=1;Y=y.reshape(args.work,4,3);nm=field(s);n,m=nm[:,0],nm[:,1]
        if np.min(n)<=0:raise FloatingPointError('Saved Hermite field lost its positive-n chart')
        aa,ap,app=(float(x[0]) for x in candidate.profile([s]));l=(m*m-app/aa)/n
        X,e1,e2,N=(Y[:,j] for j in range(4))
        return np.stack((e1,l[:,None]*N,m[:,None]*N,-l[:,None]*e1-m[:,None]*e2),axis=1).ravel()
    replay=solve_ivp(rhs,(float(knots[0]),float(knots[-1])),state.ravel(),method='DOP853',
        rtol=2e-12,atol=2e-14,max_step=args.replay_step,t_eval=[float(knots[-1])])
    if not replay.success:raise RuntimeError(replay.message)
    final=np.asarray(replay.y[:,-1].reshape(args.work,12),np.longdouble)
    frozen_frame=np.asarray(fft.rfft(final,axis=0,norm='forward'),np.complex128)
    inlet=SpectralInlet(frozen_frame,history['n_phi_cos'][end_index],history['m_phi_sin'][end_index],f,geometry)
    data=inlet.at_phi(phi);defects=summarize_defects(inlet_defects(a,v,data))
    inlet_path=args.stem.with_name(args.stem.name+'-inlet.npz')
    np.savez_compressed(inlet_path,frame_fourier=frozen_frame,n_phi_cos=history['n_phi_cos'][end_index],
        m_phi_sin=history['m_phi_sin'][end_index],frequencies=f,a=a,v=v,entry_s=entry,coast_length=L,
        candidate_sha256=digest(args.candidate),source_trajectory_sha256=digest(args.trajectory),
        representation='New frozen Fourier inlet after passive X/frame replay from saved Hermite n,m; not original intermediate state')
    rows=[];sample_positions=[];sample_material=[];ids=np.arange(0,args.work,max(1,args.work//128))
    held=np.array([0.,float(geometry.A),0.])
    for sigma in np.linspace(0,L,args.radial_samples):
        out=propagate(a,v,float(sigma),data);X,N=out['X'],out['N']
        rows.append(dict(sigma=float(sigma),physical_s=entry+float(sigma),D_min=float(np.min(out['D'])),
            material_jacobian_min=float(np.min(out['U_t'])),metric_max=float(np.max(out['metric'])),
            curvature_max=float(np.max(out['actual_curvature'])),ideal_rank_one_curvature_max=float(np.max(abs(out['ideal_nonzero_curvature']))),
            actual_Gauss_abs_max=float(np.max(abs(out['actual_K']))),
            maximum_radius=float(np.max(np.linalg.norm(X,axis=-1))),maximum_abs_y=float(np.max(abs(X[:,1]))),
            minimum_z=float(np.min(X[:,2])),maximum_z=float(np.max(X[:,2])),
            held_distance_min=float(np.min(np.linalg.norm(X-held,axis=-1))),
            outward_support_min=float(np.min(-np.sum(X*N,axis=-1))),
            map_identity_error=float(np.max(abs(out['material_derivative_identity_error'])))))
        sample_positions.append(np.asarray(X[ids],float));sample_material.append(np.asarray(out['material_u'][ids],float))
    # A real full-circle inverse gives a directly consumable fixed-normal-chart endpoint.
    target=np.asarray(geometry.material_coordinate(phi)['u'],float)
    endpoint=at_material(a,v,L,target,inlet.at_material,tolerance=2e-13)
    endpoint_path=args.stem.with_name(args.stem.name+'-endpoint.npz')
    np.savez_compressed(endpoint_path,**{k:np.asarray(endpoint[k],float) for k in
        ('X','X_s','X_u','X_ss','X_su','X_uu','e1','e2','N','l','m','n','material_u','D','metric','actual_curvature')},
        phi=np.asarray(phi,float),physical_s=entry+L,candidate_sha256=digest(args.candidate),inlet_sha256=digest(inlet_path))
    overview=args.stem.with_name(args.stem.name+'-overview.npz')
    np.savez_compressed(overview,sigma=np.linspace(0,L,args.radial_samples),material_u=np.asarray(sample_material),X=np.asarray(sample_positions))
    report=dict(schema='fd2d-peak-spacer-passive-inlet-and-ruling-consumer-v1',actual_execution=True,
        source=identity(__file__),candidate=identity(args.candidate),trajectory=identity(args.trajectory),
        dependencies=[identity(HERE/q) for q in ('fd2d_k0_ruling_coast.py','fd2d_flat_cut_prefix_candidate.py',
            'fd2d_frozen_ellipse_candidate.py','fd2d_balanced_curvature_core.py','fd2d_metric_curvature_core.py')],
        exact_seed_moments=identity(geometry.moments_path),exact_seed_means=identity(geometry.means_path),
        entry_saved_index=end_index,entry_saved_s=float(history['s'][end_index]),entry_shared_physical_s=entry,
        a=a,v=float(v),coast_length=L,angular_work=args.work,
        passive_reconstruction=dict(saved_knot_count=len(knots),s_interval=[float(knots[0]),float(knots[-1])],
            field='Shared C1 cubic Hermite interpolation of actually saved n,m and first radial RHS coefficients',
            integrated_variables='X,e1,e2,N only; n,m never solved',integrator='DOP853',
            rtol=2e-12,atol=2e-14,max_step=args.replay_step,rhs_calls=calls,solver_success=bool(replay.success),
            message=str(replay.message),intermediate_original_state_recovered=False),
        inlet_defects=defects,inlet_file=identity(inlet_path),endpoint_file=identity(endpoint_path),overview_file=identity(overview),
        rows=rows,summary=dict(D_min=min(r['D_min'] for r in rows),metric_max=max(r['metric_max'] for r in rows),
            curvature_max=max(r['curvature_max'] for r in rows),held_distance_min=min(r['held_distance_min'] for r in rows),
            outward_support_min=min(r['outward_support_min'] for r in rows),maximum_abs_y=max(r['maximum_abs_y'] for r in rows),
            maximum_radius=max(r['maximum_radius'] for r in rows)),
        endpoint_fixed_material_inverse_residual=float(np.max(abs(endpoint['material_u']-target))),
        endpoint_material_provider_input_inverse_error=inlet.maximum_material_inverse_input_error,
        endpoint_fixed_material_metric_max=float(np.max(endpoint['metric'])),
        endpoint_fixed_material_curvature_max=float(np.max(endpoint['actual_curvature'])),
        continuous_geometry_certificate=False,nonlinear_BVP_solved=False,
        scope='Actual finite ruled surface on the complete K=0 coast, with explicit passive replay and input defects. The exact R137 theorem is conditional on exact inlet compatibility; no defects are erased.',
        seconds=time.monotonic()-started)
    path=args.stem.with_name(args.stem.name+'-report.json');path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(path),sha256=digest(path),seconds=report['seconds'],summary=report['summary'],
        inlet_defects=defects,inverse_residual=report['endpoint_fixed_material_inverse_residual'],
        endpoint_metric=report['endpoint_fixed_material_metric_max'],endpoint_curvature=report['endpoint_fixed_material_curvature_max']),allow_nan=False))


if __name__=='__main__':main()
