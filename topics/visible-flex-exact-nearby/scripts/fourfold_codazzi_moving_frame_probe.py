#!/usr/bin/env python3
"""Moving-angle candidate geometry through the complete inverse physical angle.

The regular anchor uses the exact rotational circle/frame of the sampled
target at the actual saved right endpoint, integrates the candidate frame back to the waist, translates
its mean height to zero, and then observes a fresh inward sweep. Its angular and
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
from fourfold_codazzi_reciprocal_polynomial_system import ReciprocalPolynomial
from fourfold_codazzi_moving_polynomial_system import COORDINATES
from fourfold_codazzi_compact_metric_frame_probe import angular_derivative
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_codazzi_two_end_probe import save_npz_gz
from fourfold_phase_local_correction_probe import sha


class MovingPhysicalView(ReciprocalPolynomial):
    """Evaluate every stored moving mode at uniform physical theta.

    The inverse lift is theta=phi+alpha I(V)/mean(v). A safeguarded
    Newton iteration measures its actual residual at every requested point;
    it neither truncates physical modes nor regards phi as physical theta.
    This is still a floating evaluation, not a continuous inverse proof.
    """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.inverse_angle_residual_max=0.
        self.inverse_angle_derivative_sample_min=np.inf
        self.inverse_angle_max_iterations=0

    def actual_fields(self,r,y,p):
        r=np.atleast_1d(np.asarray(r,dtype=float));y=np.asarray(y,dtype=float)
        if y.ndim==1:y=y[:,None]
        if y.shape!=(2*self.modes+1,len(r)):
            raise ValueError('complete moving coefficients are required')
        target=self.controlled(r,float(p[0]));s=1/target[5]
        M=self.modes;al=self.alpha;mean=s+al*y[M]
        if np.any(mean>=0):raise ValueError('moving curvature mean is not negative')
        expected=np.broadcast_to(self.theta[:,None],(self.angular_grid,len(r)))
        phi=expected.copy();lower=np.zeros_like(phi);upper=np.full_like(phi,np.pi/2)
        freq=self.frequency[:,None,None];yc=y[M+1:][...,None]
        def evaluate_phi(phi):
            phase=freq*phi[None,:,:]
            sine=np.sin(phase);cosine=np.cos(phase)
            U=np.einsum('mar,mr->ar',sine,y[:M],optimize=True)
            V=y[M]+np.einsum('mar,mr->ar',cosine,y[M+1:],optimize=True)
            IV=np.einsum('mar,mr->ar',sine,y[M+1:]/self.frequency[:,None],optimize=True)
            v=s+al*V;lift=phi+al*IV/mean
            return U,v,lift,v/mean
        for iteration in range(48):
            U,v,lift,derivative=evaluate_phi(phi)
            if np.any(derivative<=0) or not np.all(np.isfinite(lift)):
                raise ValueError('sampled actual inverse angle is not monotone')
            error=lift-expected
            if np.max(abs(error))<=2e-13:break
            lower=np.where(error<0,phi,lower);upper=np.where(error>0,phi,upper)
            proposal=phi-error/derivative
            outside=(proposal<=lower)|(proposal>=upper)|~np.isfinite(proposal)
            proposal=np.where(outside,(lower+upper)/2,proposal)
            phi=np.where(abs(error)<=2e-13,phi,proposal)
        else:raise ValueError('complete physical angle inversion did not converge')
        self.inverse_angle_residual_max=max(self.inverse_angle_residual_max,float(np.max(abs(error))))
        self.inverse_angle_derivative_sample_min=min(self.inverse_angle_derivative_sample_min,float(np.min(derivative)))
        self.inverse_angle_max_iterations=max(self.inverse_angle_max_iterations,iteration+1)
        if np.any(v>=0):raise ValueError('sampled physical second form leaves its negative chart')
        return al*U/v,1/v


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
    if meta['object_sha256']!=sha(args.object) or meta['coordinates']!=COORDINATES:
        raise ValueError('different complete candidate target or chart')
    if args.angles<8*m or args.step<=0 or args.coefficient_batch<1:raise ValueError('invalid complete diagnostic resolution')
    if (args.save_radial+2)*args.angles*9*8>4_800_000:raise ValueError('complete saved geometry exceeds the selected repository budget')
    geometry,definition=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=MovingPhysicalView(geometry,m,args.angles,body,graft)
    system.alpha=alpha=float(meta['amplitude']);nu=float(meta['nu'])
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes']);n=args.angles;theta=system.theta
    right=float(saved['radial_nodes'][-1])
    if saved['radial_nodes'][0]!=0 or not 1.5<=right<=3.125:raise ValueError('the actual body cut must lie in [3/2,25/8]')
    r=np.unique(np.r_[np.linspace(0.,right,int(np.ceil(right/args.step))+1),saved['radial_nodes']])
    a0=system.base([0.])[0,0];cr0=system.controlled([0.],nu)[5][0]
    _,waistC=system.actual_fields([0.],pp(0.)[:,None],[nu])
    waist_fourier=np.fft.fft(waistC[:,0])/n
    waist=np.r_[waist_fourier[0].real,2*waist_fourier[1:n//2].real,waist_fourier[n//2].real]
    mean_gap=float(waist[0]+1/a0)
    fulln=4*n;fulltheta=2*np.pi*np.arange(fulln)/fulln;frequency=4*np.arange(1,n//2+1)
    # The same sampled sine primitive through a full-circle FFT: the highest
    # sine is Nyquist and vanishes at every one of these sample points.  This
    # retains every sampled physical waist mode without a dense n-by-4n array.
    phase_spectrum=np.zeros(fulln//2+1,dtype=complex)
    phase_spectrum[frequency[:-1]]=1j*a0*waist[1:-1]/(2*frequency[:-1])
    phase=fulltheta+np.fft.irfft(phase_spectrum,n=fulln)*fulln
    tangent=1j*np.exp(1j*phase);ft=np.fft.fft(tangent)/fulln;ff=np.fft.fftfreq(fulln,1/fulln)
    primitive=np.zeros(fulln,dtype=complex);nz=ff!=0;primitive[nz]=a0*ft[nz]/(1j*ff[nz])
    initial=np.fft.ifft(primitive)*fulln
    waist_state=np.zeros((n,12));waist_state[:,:2]=np.column_stack([initial[:n].real,initial[:n].imag])
    waist_state[:,5]=1;waist_state[:,6:8]=np.column_stack([tangent[:n].real,tangent[:n].imag])
    waist_state[:,9:11]=np.column_stack([np.cos(phase[:n]),np.sin(phase[:n])])
    aR,gR,betaR,KR,ellR,CrR,*_=system.controlled([right],nu)
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
            B,C=system.actual_fields(stages,pp(stages).T,[nu]);A=(KK+B*B)/C
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
        raw_F=F
        if args.anchor=='regular':
            F=raw_F.copy();F[:,2]-=backward_height_shift
        frame=np.stack([X,Y,N],axis=2);gram=np.einsum('nai,naj->nij',frame,frame)-np.eye(3)
        Ft=angular_derivative(raw_F,theta);Ftt=angular_derivative(raw_F,theta,2)
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
    first=True;observation_direction=-1 if args.anchor=='regular' else 1
    if args.anchor=='regular':state=regular_state.copy()
    for j,h,i0,im,i1,fields in blocks(observation_direction):
        if first:
            observe(len(r)-1 if observation_direction<0 else 0,state,i0,fields);first=False
        state=step(state,h,i0,im,i1,fields);observe(j,state,i1,fields)
        if time.monotonic()-lastprint>20:
            print(dict(pass_name='inward_geometry' if observation_direction<0 else 'outward_geometry',radius=float(r[j]),position_angular_error=summary['position_angular_constraint'],
                full_metric_error=summary['relative_angular_metric_error'],wall_seconds=time.monotonic()-started),flush=True);lastprint=time.monotonic()
    summary['nominal_reflected_sampled_diameter']=2*summary['max_position_norm']
    summary['witness_sample_over_nominal_reflected_sampled_diameter']=summary['phase_witness_sampled_nearest_distance']/summary['nominal_reflected_sampled_diameter']
    if args.anchor=='regular':
        final_waist=state.copy();final_waist[:,2]-=backward_height_shift
        summary['deterministic_repeat_waist_maximum_state_difference']=float(np.max(abs(final_waist-start_state)))
        summary['outer_height_range']=[-backward_height_shift,-backward_height_shift]
    else:summary['outer_height_range']=[float(np.min(state[:,2])),float(np.max(state[:,2]))]
    endB,endC=system.actual_fields([right],pp(right)[:,None],[nu]);endc=endC-CrR
    source=Path(__file__);metadata=dict(kind='floating_complete_moving_candidate_physical_angle_geometry',
        source_sha256=sha(source),object_sha256=sha(args.object),candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        anchor=args.anchor,modes=m,quarter_angles=n,amplitude=alpha,nu=nu,actual_right=right,exact_nu=str(Fraction.from_float(nu)),
        exact_amplitude=str(Fraction.from_float(alpha)),coordinates='physical r and quarter angle; Cartesian frame X,Y,n')
    order=np.argsort(stored_r)
    save_npz_gz(args.geometry,radial_nodes=np.array(stored_r)[order],theta=theta,position=np.array(stored_F)[order],normal=np.array(stored_normal)[order],
        candidate_II=np.array(stored_fields)[order],initial_state=start_state,metadata=np.array(json.dumps(metadata)))
    if args.geometry.stat().st_size>5_000_000:raise ValueError('complete saved geometry file exceeded repository limit')
    report=dict(**metadata,certified=False,complete_floating_reconstruction=True,summary=summary,worst_radii=worst,
        complete_inverse_angle_sampled_residual=system.inverse_angle_residual_max,
        complete_inverse_angle_sampled_derivative_min=system.inverse_angle_derivative_sample_min,
        complete_inverse_angle_max_iterations=system.inverse_angle_max_iterations,
        all_stored_moving_modes_evaluated_before_physical_angle_inversion=True,
        radial_steps=len(r)-1,maximum_step=float(np.max(np.diff(r))),coefficient_batch=args.coefficient_batch,
        RK_method='ordinary explicit RK4 without reorthogonalization or rigorous integration error bounds',
        initial_waist_C_mean_gap=mean_gap,waist_anchor_mean_explicitly_removed=(args.anchor=='waist'),
        regular_anchor_initial_B_difference=float(np.max(abs(endB))),
        regular_anchor_initial_C_difference=float(np.max(abs(endc))),
        rotational_initial_slope_identity_error=float(abs(radial_slope**2+vertical_slope**2-1)),
        observation_direction=observation_direction,angular_derivatives_before_constant_height_translation=True,
        backward_seconds=backward_seconds,backward_mean_height_shift=backward_height_shift,waist_diagnostics=waist_diagnostics,
        geometry_path=str(args.geometry),geometry_sha256=sha(args.geometry),geometry_bytes=args.geometry.stat().st_size,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        dependencies={name:sha(source.with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_reciprocal_polynomial_system.py','fourfold_codazzi_moving_polynomial_system.py','fourfold_codazzi_compact_metric_frame_probe.py',
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_codazzi_rotational_cap_jacobi_probe.py','fourfold_phase_codazzi_two_end_probe.py')},
        limitations=[
            'All geometry is floating, finitely sampled, and belongs to this exact stored nu and amplitude only.',
            'The regular anchor imposes a rotational outer position/frame; its nonzero B/C trace differences are printed, not certified away.',
            'The backward waist is not projected to a plane or to vertical meridians; its actual constraint errors remain in the report.',
            'Candidate II and actual reconstructed II are measured separately, including the small-radius cap where differentiation may amplify roundoff.',
            'The nominal reflection is a diagnostic diameter convention; nonzero waist constraint errors prevent claiming an exact reflected C2 surface.',
            'The sampled nearest distance is an upper bound on the continuous nearest distance, not a certified held lower bound.',
            'Every moving coefficient is evaluated through the inverse lift at physical angles; the inversion and physical angular tails remain floating diagnostics.',
            'If the stored candidate stops at 3/2, the region from that cut to the true closed cap/tail is absent from this diagnostic.',
            'No true nonlinear regular tail, all-mode PDE existence, fixed-grip noncongruence, closed surface, or reach is certified.'],
        wall_seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(summary=summary,waist_diagnostics=waist_diagnostics,wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
