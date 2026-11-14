#!/usr/bin/env python3
"""Streaming two-anchor geometry diagnostics for a complete compact-metric BVP.

The regular anchor uses the exact rotational circle/frame of the sampled
target at r=25/8, integrates the candidate frame back to the waist, translates
its mean height to zero, and then replays it forward.  Its small angular and
waist constraints are measured, never imposed afterwards.  The waist anchor
retains the earlier explicit one-turn mean correction.  Neither anchor solves
the actual regular-tail matching condition or proves a continuous PDE bound.
"""
from __future__ import annotations
import argparse,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from flint import ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_compact_metric_branch_probe import CompactNormalized
from fourfold_codazzi_compact_metric_frame_probe import angular_derivative
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_codazzi_two_end_probe import save_npz_gz
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--anchor',choices=('waist','regular'),default='regular')
    ap.add_argument('--angles',type=int,default=512)
    ap.add_argument('--step',type=float,default=.0005)
    ap.add_argument('--coefficient-batch',type=int,default=64)
    ap.add_argument('--save-radial',type=int,default=96)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--geometry',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists() or args.geometry.exists():raise FileExistsError('preserve earlier complete or failed diagnostics')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if meta['object_sha256']!=sha(args.object) or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c':
        raise ValueError('different complete candidate target or chart')
    if args.angles<4*m or args.step<=0 or args.coefficient_batch<1:raise ValueError('invalid complete diagnostic resolution')
    if (args.save_radial+2)*args.angles*9*8>4_800_000:raise ValueError('complete saved geometry exceeds the selected repository budget')
    geometry,definition=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=CompactNormalized(geometry,m,args.angles,body,graft)
    system.alpha=alpha=float(meta['amplitude']);nu=float(meta['nu'])
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes']);n=args.angles;theta=system.theta
    if saved['radial_nodes'][0]!=0 or saved['radial_nodes'][-1]!=3.125:raise ValueError('the full actual body and graft are required')
    r=np.unique(np.r_[np.linspace(0.,3.125,int(np.ceil(3.125/args.step))+1),saved['radial_nodes']])
    a0=system.base([0.])[0,0];cr0=system.controlled([0.],nu)[5][0]
    waist=alpha*pp(0.)[m:].copy();waist[0]+=cr0
    mean_gap=float(waist[0]+1/a0)
    fulln=4*n;fulltheta=2*np.pi*np.arange(fulln)/fulln;frequency=system.frequency
    phase=fulltheta-a0*np.sum(waist[1:,None]*np.sin(frequency[:,None]*fulltheta)/frequency[:,None],axis=0)
    tangent=1j*np.exp(1j*phase);ft=np.fft.fft(tangent)/fulln;ff=np.fft.fftfreq(fulln,1/fulln)
    primitive=np.zeros(fulln,dtype=complex);nz=ff!=0;primitive[nz]=a0*ft[nz]/(1j*ff[nz])
    initial=np.fft.ifft(primitive)*fulln
    waist_state=np.zeros((n,12));waist_state[:,:2]=np.column_stack([initial[:n].real,initial[:n].imag])
    waist_state[:,5]=1;waist_state[:,6:8]=np.column_stack([tangent[:n].real,tangent[:n].imag])
    waist_state[:,9:11]=np.column_stack([np.cos(phase[:n]),np.sin(phase[:n])])
    aR,gR,betaR,KR,ellR,CrR,*_=system.controlled([3.125],nu)
    aR,gR,betaR,CrR=map(lambda v:float(v[0]),(aR,gR,betaR,CrR))
    radial_slope=betaR/gR;vertical_slope=-aR*CrR
    regular_state=np.zeros((n,12));co,si=np.cos(theta),np.sin(theta)
    regular_state[:,:3]=np.column_stack([aR*co,aR*si,np.zeros(n)])
    regular_state[:,3:6]=np.column_stack([radial_slope*co,radial_slope*si,np.full(n,vertical_slope)])
    regular_state[:,6:9]=np.column_stack([-si,co,np.zeros(n)])
    regular_state[:,9:12]=np.column_stack([vertical_slope*co,vertical_slope*si,np.full(n,-radial_slope)])
    # Only one short radial batch of angular fields is ever materialized.
    def blocks(direction):
        indices=np.arange(len(r)-1) if direction>0 else np.arange(len(r)-2,-1,-1)
        for start in range(0,len(indices),args.coefficient_batch):
            ii=indices[start:start+args.coefficient_batch]
            stages=np.unique(np.r_[r[ii],(r[ii]+r[ii+1])/2,r[ii+1]])
            coeff=system.controlled(stages,nu);aa,gg,bb,KK,ll,Cr,*_=coeff
            Bn,cn=system.normalized_fields(pp(stages).T)
            B=alpha*Bn;C=Cr+alpha*cn;A=(KK+B*B)/C
            if np.any(C>=0) or not np.all(np.isfinite(A)):raise ValueError('sampled candidate second form leaves its chart')
            fields=(aa,gg,bb,A,B,C)
            for j in ii:
                i0=int(np.searchsorted(stages,r[j]));im=int(np.searchsorted(stages,(r[j]+r[j+1])/2));i1=int(np.searchsorted(stages,r[j+1]))
                if direction>0:yield j+1,r[j+1]-r[j],i0,im,i1,fields
                else:yield j,r[j]-r[j+1],i1,im,i0,fields
    def rhs(S,index,fields):
        aa,gg,bb,A,B,C=fields;sg=aa[index]*gg[index]
        X,Y,N=S[:,3:6],S[:,6:9],S[:,9:12];ar=A[:,index,None];br=B[:,index,None]
        out=np.empty_like(S);out[:,:3]=sg*X;out[:,3:6]=sg*ar*N;out[:,6:9]=sg*br*N
        out[:,9:12]=-sg*(ar*X+br*Y);return out
    def step(S,h,i0,im,i1,fields):
        k1=rhs(S,i0,fields);k2=rhs(S+h*k1/2,im,fields);k3=rhs(S+h*k2/2,im,fields);k4=rhs(S+h*k3,i1,fields)
        return S+h*(k1+2*k2+2*k3+k4)/6
    backward_seconds=0.;backward_height_shift=0.;lastprint=time.monotonic()
    if args.anchor=='regular':
        state=regular_state.copy();backward_started=time.monotonic()
        for j,h,i0,im,i1,fields in blocks(-1):
            state=step(state,h,i0,im,i1,fields)
            if time.monotonic()-lastprint>20:
                print(dict(pass_name='regular_to_waist',radius=float(r[j]),wall_seconds=time.monotonic()-started),flush=True);lastprint=time.monotonic()
        backward_height_shift=float(np.mean(state[:,2]));state[:,2]-=backward_height_shift
        backward_seconds=time.monotonic()-backward_started
    else:state=waist_state.copy()
    start_state=state.copy()
    waist_diagnostics=dict(position_height_range=[float(state[:,2].min()),float(state[:,2].max())],
        meridian_frame_distance_to_vertical=float(np.max(np.linalg.norm(state[:,3:6]-np.array([0.,0.,1.]),axis=1))),
        angular_frame_vertical_max=float(np.max(abs(state[:,8]))),
        normal_vertical_max=float(np.max(abs(state[:,11]))),
        maximum_position_distance_to_corrected_planar_waist=float(np.max(np.linalg.norm(state[:,:3]-waist_state[:,:3],axis=1))))
    angle=np.pi/4;witness=state[0,:3].copy();witness[:2]=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])@witness[:2]
    targets=[]
    for j in range(4):
        phi=-j*np.pi/2;c,s=np.cos(phi),np.sin(phi)
        targets.append([c*witness[0]-s*witness[1],s*witness[0]+c*witness[1],witness[2]])
    targets=np.array(targets)
    sample_indices=set(np.unique(np.linspace(0,len(r)-1,args.save_radial,dtype=int)).tolist());sample_indices.update((0,len(r)-1))
    stored_r=[];stored_F=[];stored_normal=[];stored_fields=[]
    summary=dict(frame_orthonormality=0.,frame_angular_constraint=0.,position_angular_constraint=0.,
        relative_angular_metric_error=0.,normalized_cross_metric_error=0.,
        reconstructed_immersion_cross_norm_min=np.inf,candidate_principal_curvature_abs_max=0.,
        actual_principal_curvature_abs_max=0.,actual_principal_curvature_abs_max_r_le_one=0.,
        actual_support_min=np.inf,candidate_normal_support_min=np.inf,max_position_norm=0.,
        phase_witness_sampled_nearest_distance=np.inf,minimum_z_r_ge_quarter=np.inf)
    worst={}
    def observe(j,S,index,fields):
        aa,gg,bb,A,B,C=fields;F,X,Y,N=S[:,:3],S[:,3:6],S[:,6:9],S[:,9:12]
        a=aa[index];gamma=gg[index];beta=bb[index];sg=a*gamma
        frame=np.stack([X,Y,N],axis=2);gram=np.einsum('nai,naj->nij',frame,frame)-np.eye(3)
        Ft=angular_derivative(F,theta);Ftt=angular_derivative(F,theta,2)
        Xt=angular_derivative(X,theta);Yt=angular_derivative(Y,theta);Nt=angular_derivative(N,theta)
        expectedX=(beta/gamma)*Y+a*B[:,index,None]*N
        expectedY=-(beta/gamma)*X+a*C[:,index,None]*N
        expectedN=-a*(B[:,index,None]*X+C[:,index,None]*Y)
        cross=np.cross(Ft,X);crossnorm=np.linalg.norm(cross,axis=1)
        if np.any(crossnorm==0):raise ValueError('sampled reconstructed position loses immersion')
        actualnormal=cross/crossnorm[:,None]
        centre=(A[:,index]+C[:,index])/2;rad=np.sqrt(((A[:,index]-C[:,index])/2)**2+B[:,index]**2)
        candidate_curvature=np.maximum(abs(centre+rad),abs(centre-rad))
        g11=sg*sg*np.sum(X*X,axis=1);g12=sg*np.sum(X*Ft,axis=1);g22=np.sum(Ft*Ft,axis=1)
        ortho=g22-g12*g12/g11
        if np.any(ortho<=0):raise ValueError('sampled actual metric denominator failed')
        h11=sg*sg*A[:,index]*np.sum(actualnormal*N,axis=1)
        h12=sg*np.sum(actualnormal*Xt,axis=1);h22=np.sum(actualnormal*Ftt,axis=1)
        ax=h11/g11;bx=(h12-g12*h11/g11)/np.sqrt(g11*ortho)
        cx=(h22-2*g12*h12/g11+(g12/g11)**2*h11)/ortho
        cent=(ax+cx)/2;rrr=np.sqrt(((ax-cx)/2)**2+bx*bx)
        actual_curvature=float(np.max(np.maximum(abs(cent+rrr),abs(cent-rrr))))
        values=dict(frame_orthonormality=float(np.max(abs(gram))),
            frame_angular_constraint=max(float(np.max(np.linalg.norm(z,axis=1))) for z in (Xt-expectedX,Yt-expectedY,Nt-expectedN)),
            position_angular_constraint=float(np.max(np.linalg.norm(Ft-a*Y,axis=1))),
            relative_angular_metric_error=float(np.max(abs(g22/(a*a)-1))),
            normalized_cross_metric_error=float(np.max(abs(g12/(sg*a)))),
            candidate_principal_curvature_abs_max=float(np.max(candidate_curvature)),
            actual_principal_curvature_abs_max=actual_curvature,
            max_position_norm=float(np.max(np.linalg.norm(F,axis=1))))
        if r[j]<=1:values['actual_principal_curvature_abs_max_r_le_one']=actual_curvature
        for name,value in values.items():
            if value>summary[name]:summary[name]=value;worst[name]=float(r[j])
        summary['reconstructed_immersion_cross_norm_min']=min(summary['reconstructed_immersion_cross_norm_min'],float(np.min(crossnorm)))
        summary['actual_support_min']=min(summary['actual_support_min'],float(np.min(np.sum(F*actualnormal,axis=1))))
        summary['candidate_normal_support_min']=min(summary['candidate_normal_support_min'],float(np.min(np.sum(F*N,axis=1))))
        distances=np.linalg.norm(F[:,None,:]-targets[None,:,:],axis=2);value=float(np.min(distances))
        if value<summary['phase_witness_sampled_nearest_distance']:
            summary['phase_witness_sampled_nearest_distance']=value;worst['witness_nearest_radius']=float(r[j]);worst['witness_nearest_angle']=float(theta[np.unravel_index(np.argmin(distances),distances.shape)[0]])
        if r[j]>=.25:summary['minimum_z_r_ge_quarter']=min(summary['minimum_z_r_ge_quarter'],float(np.min(F[:,2])))
        if j in sample_indices:
            stored_r.append(r[j]);stored_F.append(F.copy());stored_normal.append(actualnormal.copy())
            stored_fields.append(np.stack([A[:,index],B[:,index],C[:,index]],axis=1))
    first=True
    for j,h,i0,im,i1,fields in blocks(1):
        if first:observe(0,state,i0,fields);first=False
        state=step(state,h,i0,im,i1,fields);observe(j,state,i1,fields)
        if time.monotonic()-lastprint>20:
            print(dict(pass_name='waist_to_regular',radius=float(r[j]),position_angular_error=summary['position_angular_constraint'],
                full_metric_error=summary['relative_angular_metric_error'],wall_seconds=time.monotonic()-started),flush=True);lastprint=time.monotonic()
    summary['nominal_reflected_sampled_diameter']=2*summary['max_position_norm']
    summary['witness_sample_over_nominal_reflected_sampled_diameter']=summary['phase_witness_sampled_nearest_distance']/summary['nominal_reflected_sampled_diameter']
    regular_shifted=regular_state.copy();regular_shifted[:,2]-=backward_height_shift
    if args.anchor=='regular':summary['regular_anchor_roundtrip_maximum_state_error']=float(np.max(abs(state-regular_shifted)))
    summary['last_height_range']=[float(np.min(state[:,2])),float(np.max(state[:,2]))]
    endB,endc=system.normalized_fields(pp(3.125)[:,None])
    source=Path(__file__);metadata=dict(kind='floating_streaming_two_anchor_compact_metric_geometry_v2',
        source_sha256=sha(source),object_sha256=sha(args.object),candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        anchor=args.anchor,modes=m,quarter_angles=n,amplitude=alpha,nu=nu,exact_nu=str(Fraction.from_float(nu)),
        exact_amplitude=str(Fraction.from_float(alpha)),coordinates='physical r and quarter angle; Cartesian frame X,Y,n')
    save_npz_gz(args.geometry,radial_nodes=np.array(stored_r),theta=theta,position=np.array(stored_F),normal=np.array(stored_normal),
        candidate_II=np.array(stored_fields),initial_state=start_state,metadata=np.array(json.dumps(metadata)))
    if args.geometry.stat().st_size>5_000_000:raise ValueError('complete saved geometry file exceeded repository limit')
    report=dict(**metadata,certified=False,complete_floating_reconstruction=True,summary=summary,worst_radii=worst,
        radial_steps=len(r)-1,maximum_step=float(np.max(np.diff(r))),coefficient_batch=args.coefficient_batch,
        RK_method='ordinary explicit RK4 without reorthogonalization or rigorous integration error bounds',
        initial_waist_C_mean_gap=mean_gap,waist_anchor_mean_explicitly_removed=(args.anchor=='waist'),
        regular_anchor_initial_B_difference=float(alpha*np.max(abs(endB))),
        regular_anchor_initial_C_difference=float(alpha*np.max(abs(endc))),
        rotational_initial_slope_identity_error=float(abs(radial_slope**2+vertical_slope**2-1)),
        backward_seconds=backward_seconds,backward_mean_height_shift=backward_height_shift,waist_diagnostics=waist_diagnostics,
        geometry_path=str(args.geometry),geometry_sha256=sha(args.geometry),geometry_bytes=args.geometry.stat().st_size,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        dependencies={name:sha(source.with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_compact_metric_branch_probe.py','fourfold_codazzi_compact_metric_frame_probe.py',
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_codazzi_rotational_cap_jacobi_probe.py','fourfold_phase_codazzi_two_end_probe.py')},
        limitations=[
            'All geometry is floating, finitely sampled, and belongs to this exact stored nu and amplitude only.',
            'The regular anchor imposes a rotational outer position/frame; its nonzero B/C trace differences are printed, not certified away.',
            'The backward waist is not projected to a plane or to vertical meridians; its actual constraint errors remain in the report.',
            'Candidate II and actual reconstructed II are measured separately, including the small-radius cap where differentiation may amplify roundoff.',
            'The nominal reflection is a diagnostic diameter convention; nonzero waist constraint errors prevent claiming an exact reflected C2 surface.',
            'The sampled nearest distance is an upper bound on the continuous nearest distance, not a certified held lower bound.',
            'No true nonlinear regular tail, all-mode PDE existence, fixed-grip noncongruence, closed surface, or reach is certified.'],
        wall_seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(summary=summary,waist_diagnostics=waist_diagnostics,wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
