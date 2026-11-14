#!/usr/bin/env python3
"""Floating frame/position reconstruction of a complete normalized candidate.

The exact R126 skew frame equations are integrated by ordinary RK4.  The
input waist mean mismatch is printed and explicitly removed only from the
initial planar curve, not from the candidate Codazzi fields.  Angular
constraint/metric errors are measured.  Candidate II is not silently used
as the actual II when these constraints are nonzero.  No reach or closed
surface theorem is issued by this numerical diagnostic.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from flint import ctx
from fourfold_codazzi_compact_metric_branch_probe import CompactNormalized
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_codazzi_two_end_probe import load_candidate,save_npz_gz
from fourfold_phase_local_correction_probe import sha


def angular_derivative(values,theta,order=1):
    """Differentiate a fourfold-covariant Cartesian vector on one quarter."""
    n=len(theta);z=(values[:,0]+1j*values[:,1])*np.exp(-1j*theta)
    frequency=4*np.fft.fftfreq(n,1/n)
    dz=np.fft.ifft((1j*(frequency+1))**order*np.fft.fft(z))*np.exp(1j*theta)
    zz=np.fft.ifft((1j*frequency)**order*np.fft.fft(values[:,2])).real
    return np.column_stack([dz.real,dz.imag,zz])


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--angles',type=int,default=128)
    ap.add_argument('--step',type=float,default=.0005);ap.add_argument('--save-radial',type=int,default=512)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--geometry',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists() or args.geometry.exists():raise FileExistsError('refusing to overwrite a geometry diagnostic')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if meta['object_sha256']!=sha(args.object) or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c':
        raise ValueError('different candidate object or chart')
    if args.angles<4*m or args.step<=0:raise ValueError('inadequate diagnostic resolution')
    if args.save_radial*args.angles*9*8>4_800_000:
        raise ValueError('reduce saved radial samples so the complete gzip geometry remains below the repository file limit')
    geometry,definition=load_exact_object(args.object,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=CompactNormalized(geometry,m,args.angles,body,graft);system.alpha=alpha=float(meta['amplitude']);nu=float(meta['nu'])
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes']);n=args.angles;theta=system.theta
    a0=system.base([0.])[0,0];cr0=system.controlled([0.],nu)[5][0]
    waist=alpha*pp(0.)[m:].copy();waist[0]+=cr0;mean_gap=float(waist[0]+1/a0)
    # Construct an exactly fourfold, one-turn planar initial curve from the
    # nonmean coefficients. Its mean is -1/a0 by definition; report the change.
    fulln=4*n;fulltheta=2*np.pi*np.arange(fulln)/fulln;freq=system.frequency
    phase=fulltheta-a0*np.sum(waist[1:,None]*np.sin(freq[:,None]*fulltheta)/freq[:,None],axis=0)
    tangent=1j*np.exp(1j*phase);ft=np.fft.fft(tangent)/fulln;ff=np.fft.fftfreq(fulln,1/fulln)
    fh=np.zeros(fulln,dtype=complex);nz=ff!=0;fh[nz]=a0*ft[nz]/(1j*ff[nz]);initial=np.fft.ifft(fh)*fulln
    state=np.zeros((n,12));state[:,:2]=np.column_stack([initial[:n].real,initial[:n].imag]);state[:,5]=1
    state[:,6:8]=np.column_stack([tangent[:n].real,tangent[:n].imag])
    state[:,9:11]=np.column_stack([np.cos(phase[:n]),np.sin(phase[:n])])
    witness=np.array([initial[0].real,initial[0].imag,0.]);angle=np.pi/4
    witness=np.array([np.cos(angle)*witness[0]-np.sin(angle)*witness[1],
        np.sin(angle)*witness[0]+np.cos(angle)*witness[1],0.])
    targets=[]
    for j in range(4):
        phi=-j*np.pi/2;c,s=np.cos(phi),np.sin(phi)
        targets.append(np.array([c*witness[0]-s*witness[1],s*witness[0]+c*witness[1],0.]))
    targets=np.array(targets)
    r=np.unique(np.r_[np.linspace(0.,3.125,int(np.ceil(3.125/args.step))+1),saved['radial_nodes']])
    stages=np.sort(np.r_[r,(r[:-1]+r[1:])/2]);left_index=np.searchsorted(stages,r[:-1]);right_index=np.searchsorted(stages,r[1:]);mid_index=np.searchsorted(stages,(r[:-1]+r[1:])/2)
    coeff=system.controlled(stages,nu);aa,gg,bb,KK,ll,Cr,*_=coeff;sg=aa*gg
    states=pp(stages).T;B0,c0=system.normalized_fields(states);B=alpha*B0;C=Cr+alpha*c0;A=(KK+B*B)/C
    if not np.all(np.isfinite(A)) or np.any(C>=0):raise ValueError('invalid sampled candidate second form')
    sample_indices=set(np.unique(np.linspace(0,len(r)-1,args.save_radial,dtype=int)).tolist());sample_indices.add(0);sample_indices.add(len(r)-1)
    stored_r=[];stored_F=[];stored_normal=[];stored_fields=[]
    summary=dict(frame_orthonormality=0.,frame_angular_constraint=0.,position_angular_constraint=0.,
        relative_angular_metric_error=0.,normalized_cross_metric_error=0.,
        reconstructed_immersion_cross_norm_min=np.inf,candidate_principal_curvature_abs_max=0.,
        actual_principal_curvature_abs_max_r_le_one=0.,actual_support_min=np.inf,
        candidate_normal_support_min=np.inf,max_position_norm=0.,
        phase_witness_sampled_nearest_distance=np.inf,minimum_z_r_ge_quarter=np.inf)
    worst={};lastprint=time.monotonic()
    def rhs(S,index):
        X,Y,N=S[:,3:6],S[:,6:9],S[:,9:12];ar=A[:,index,None];br=B[:,index,None];out=np.empty_like(S)
        out[:,:3]=sg[index]*X;out[:,3:6]=sg[index]*ar*N;out[:,6:9]=sg[index]*br*N
        out[:,9:12]=-sg[index]*(ar*X+br*Y);return out
    def observe(j,S,index):
        F,X,Y,N=S[:,:3],S[:,3:6],S[:,6:9],S[:,9:12];a=aa[index];gamma=gg[index];beta=bb[index]
        Frame=np.stack([X,Y,N],axis=2);gram=np.einsum('nai,naj->nij',Frame,Frame)-np.eye(3)
        Ft=angular_derivative(F,theta);Xt=angular_derivative(X,theta);Yt=angular_derivative(Y,theta);Nt=angular_derivative(N,theta)
        expectedX=(beta/gamma)*Y+a*B[:,index,None]*N
        expectedY=-(beta/gamma)*X+a*C[:,index,None]*N
        expectedN=-a*(B[:,index,None]*X+C[:,index,None]*Y)
        cross=np.cross(Ft,X);crossnorm=np.linalg.norm(cross,axis=1)
        if np.any(crossnorm==0):raise ValueError('reconstructed sampled surface loses immersion')
        actualnormal=cross/crossnorm[:,None]
        center=(A[:,index]+C[:,index])/2;rad=np.sqrt(((A[:,index]-C[:,index])/2)**2+B[:,index]**2)
        curv=np.maximum(abs(center+rad),abs(center-rad))
        values=dict(frame_orthonormality=float(np.max(abs(gram))),
            frame_angular_constraint=max(float(np.max(np.linalg.norm(z,axis=1))) for z in (Xt-expectedX,Yt-expectedY,Nt-expectedN)),
            position_angular_constraint=float(np.max(np.linalg.norm(Ft-a*Y,axis=1))),
            relative_angular_metric_error=float(np.max(abs(np.sum(Ft*Ft,axis=1)/(a*a)-1))),
            normalized_cross_metric_error=float(np.max(abs(np.sum(X*Ft,axis=1)/a))),
            candidate_principal_curvature_abs_max=float(np.max(curv)),max_position_norm=float(np.max(np.linalg.norm(F,axis=1))))
        for name,value in values.items():
            if value>summary[name]:summary[name]=value;worst[name]=float(r[j])
        summary['reconstructed_immersion_cross_norm_min']=min(summary['reconstructed_immersion_cross_norm_min'],float(np.min(crossnorm)))
        summary['actual_support_min']=min(summary['actual_support_min'],float(np.min(np.sum(F*actualnormal,axis=1))))
        summary['candidate_normal_support_min']=min(summary['candidate_normal_support_min'],float(np.min(np.sum(F*N,axis=1))))
        distances=np.linalg.norm(F[:,None,:]-targets[None,:,:],axis=2)
        value=float(np.min(distances))
        if value<summary['phase_witness_sampled_nearest_distance']:
            summary['phase_witness_sampled_nearest_distance']=value;worst['witness_nearest_radius']=float(r[j]);worst['witness_nearest_angle']=float(theta[np.unravel_index(np.argmin(distances),distances.shape)[0]])
        if r[j]>=.25:summary['minimum_z_r_ge_quarter']=min(summary['minimum_z_r_ge_quarter'],float(np.min(F[:,2])))
        # Actual shape operator of the reconstructed surface, restricted away
        # from tiny-radius cancellation. The sg' X term is exactly tangential.
        if r[j]<=1:
            Ftt=angular_derivative(F,theta,2);g11=sg[index]**2*np.sum(X*X,axis=1)
            g12=sg[index]*np.sum(X*Ft,axis=1);g22=np.sum(Ft*Ft,axis=1);ortho=g22-g12*g12/g11
            h11=sg[index]**2*A[:,index]*np.sum(actualnormal*N,axis=1)
            h12=sg[index]*np.sum(actualnormal*Xt,axis=1);h22=np.sum(actualnormal*Ftt,axis=1)
            aactual=h11/g11;bactual=(h12-g12*h11/g11)/np.sqrt(g11*ortho)
            cactual=(h22-2*g12*h12/g11+(g12/g11)**2*h11)/ortho
            cc=(aactual+cactual)/2;rrr=np.sqrt(((aactual-cactual)/2)**2+bactual*bactual)
            val=float(np.max(np.maximum(abs(cc+rrr),abs(cc-rrr))))
            if val>summary['actual_principal_curvature_abs_max_r_le_one']:
                summary['actual_principal_curvature_abs_max_r_le_one']=val;worst['actual_curvature_radius']=float(r[j])
        if j in sample_indices:
            stored_r.append(r[j]);stored_F.append(F.copy());stored_normal.append(actualnormal.copy());stored_fields.append(np.stack([A[:,index],B[:,index],C[:,index]],axis=1))
    observe(0,state,left_index[0])
    for j in range(len(r)-1):
        h=r[j+1]-r[j];i0,im,i1=left_index[j],mid_index[j],right_index[j]
        k1=rhs(state,i0);k2=rhs(state+h*k1/2,im);k3=rhs(state+h*k2/2,im);k4=rhs(state+h*k3,i1)
        state=state+h*(k1+2*k2+2*k3+k4)/6
        observe(j+1,state,i1)
        if time.monotonic()-lastprint>20:
            print(dict(radius=float(r[j+1]),steps=j+1,frame_error=summary['frame_orthonormality'],
                angular_error=summary['position_angular_constraint'],witness_sample=summary['phase_witness_sampled_nearest_distance']),flush=True)
            lastprint=time.monotonic()
    summary['diameter_from_sampled_central_symmetry']=2*summary['max_position_norm']
    summary['witness_sample_over_sampled_diameter']=summary['phase_witness_sampled_nearest_distance']/summary['diameter_from_sampled_central_symmetry']
    summary['last_height_range']=[float(np.min(state[:,2])),float(np.max(state[:,2]))]
    metadata=dict(kind='floating_R126_frame_geometry_of_compact_metric_candidate',source_sha256=sha(__file__),
        object_sha256=sha(args.object),candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        modes=m,quarter_angles=n,amplitude=alpha,nu=nu,initial_waist_mean_removed=mean_gap,
        coordinates='r>=0, physical quarter theta; fourfold rotations and equatorial reflection reconstruct the sampled body')
    save_npz_gz(args.geometry,radial_nodes=np.array(stored_r),theta=theta,position=np.array(stored_F),normal=np.array(stored_normal),
        candidate_II=np.array(stored_fields),metadata=np.array(json.dumps(metadata)))
    report=dict(**metadata,certified=False,complete_floating_reconstruction=True,summary=summary,worst_radii=worst,
        radial_steps=len(r)-1,maximum_step=float(np.max(np.diff(r))),RK_method='ordinary explicit RK4, no reorthogonalization or interval error bound',
        actual_target_stage_count=len(stages),saved_radial_count=len(stored_r),waist_mean_original=float(waist[0]),
        exact_closed_waist_mean_used=float(-1/a0),waist_curve_altered_by_mean_only=True,
        geometry_path=str(args.geometry),geometry_sha256=sha(args.geometry),geometry_bytes=args.geometry.stat().st_size,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_compact_metric_branch_probe.py','fourfold_phase_codazzi_two_end_probe.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py')},
        limitations=['Floating finite primitive/Fourier and RK reconstruction only; no continuous parameter, angular or radial certificate.',
            'The input waist mean correction is explicit. Candidate B,C fields were not modified to hide its initial constraint error.',
            'Candidate II and actual reconstructed II are distinguished. Actual curvature is sampled only on r<=1 to avoid tiny-radius coordinate cancellation.',
            'A nearest distance over a finite grid is not a lower bound on the continuous point-to-surface distance.',
            'The true regular tail and a closed surface are not reconstructed by this body-only probe; no reach is claimed.',
            'A phase-rotated auxiliary image is congruent; noncongruence would still require the separate fixed grip repair.'],
        wall_seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(summary=summary,geometry_bytes=report['geometry_bytes'],wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
