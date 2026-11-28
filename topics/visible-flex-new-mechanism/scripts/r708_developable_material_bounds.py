"""Whole rectangle inequalities for the actual six-control developed strip, and central seam output."""
import math
import numpy as np
from r708_developable_shoulder_rod import (ALPHA, CENTERS, CUTS, E2, LENGTH, T0, UNIT, WIDTH,
                                          angle, phase_center, source_k, speed)


def controls_on_strip(rod,q,bins):
    # All values bound the full subcell, including both signs of the original z.
    # Branch decisions in the public search are floating evaluations of these inequalities.
    edges=np.linspace(-1.,1.,bins+1)
    left,right=edges[:-1],edges[1:]
    near=np.where(left*right<=0.,0.,np.minimum(abs(left),abs(right)))
    far=np.maximum(abs(left),abs(right))
    u=1/(1-near**2)
    v=np.full_like(u,np.inf)
    inside=far<1.
    v[inside]=1/(1-far[inside]**2)
    t=np.minimum(v,np.maximum(u,2.))
    shape=np.exp(-u)
    deriv=2*far*t*t*np.exp(-t)
    k_peak=max(source_k(.10),source_k(.90))
    jlow=1.; pmax=0.; kmin=min(source_k(.10),source_k(.90))
    witness={"minimum_material_jacobian":1., "maximum_abs_curvature":0.}
    for idx,center in enumerate(CENTERS):
        yl,yr=center+WIDTH*left,center+WIDTH*right
        # b decreases and k0 increases throughout the R704 active arc.
        kl,kr=source_k(yl),source_k(yr)
        hi=shape/rod.norm[idx]
        dt=WIDTH*LENGTH*speed(yr)
        dB=deriv/(dt*rod.norm[idx])
        A,D=q[idx],q[idx+3]
        lower=kl+min(0.,A)*hi
        upper=kr+max(0.,A)*hi
        kmin=min(kmin,float(min(lower)))
        if kmin<=0.:
            return dict(pass_strip=False,reason='positive_bending_not_enclosed',k_lower=kmin,bins=bins)
        p=abs(D)*hi/lower
        # |k0_t|=3 k0 sin²α |sinθ cosθ| θ_l / b³, and |sinθ cosθ|≤1/2.
        dk0=1.5*kr*np.sin(ALPHA)**2*(8/.998)/speed(yr)**3
        dp=abs(D)*(kr*dB+hi*dk0)/lower**2
        jl=1-.21*dp
        jlow=min(jlow,float(min(jl)));pmax=max(pmax,float(max(p)))
        for y in center+WIDTH*(left+right)/2:
            k,j,p0,pt=rod.data(y,q)
            zj=1-.21*abs(pt)
            if zj<witness['minimum_material_jacobian']:
                witness.update(minimum_material_jacobian=float(zj),y_material_jacobian=float(y))
            if zj>0:
                cur=abs(k)*(1+p0*p0)/zj
                if cur>witness['maximum_abs_curvature']:
                    witness.update(maximum_abs_curvature=float(cur),y_curvature=float(y))
        if min(jl)<=0:
            return dict(pass_strip=False,reason='fibre_jacobian_not_enclosed',minimum_jacobian_lower=jlow,
                        k_lower=kmin,witness=witness,bins=bins)
        k_peak=max(k_peak,float(max(upper*(1+p*p)/jl)))
    # In (e,T,n), distance from the middle frame ≤ half-arc integral of |k0| plus all control masses.
    # theta in the whole control rectangle is affine. Its projected tangent angle is atan(c0 tan theta).
    beta=lambda y: math.atan(math.cos(ALPHA)*math.tan(angle(y)))
    theta=max(beta(.5)-beta(.10),beta(.90)-beta(.5))
    # For the native numeric normalization: int exp[-1/(1-x²)] dt ≤ .02 L exp(-1).
    theta+=float(np.sum((abs(q[:3])+abs(q[3:]))*(2*WIDTH*LENGTH*math.exp(-1)/rod.norm)))
    reach=math.cos(theta)**2/k_peak if theta<np.pi/2 else 0.
    good=jlow>1.e-8 and k_peak<10.4 and reach>.096
    return dict(pass_strip=bool(good),reason='strip_gates_pass' if good else 'curvature_or_normal_ball_bound',
                k_lower=kmin,minimum_jacobian_lower=jlow,curvature_upper=k_peak,maximum_abs_p=pmax,
                all_pairs_strip_normal_ball_lower=reach,frame_angle_from_middle_upper=theta,witness=witness,bins=bins)


def certificate(rod,q):
    ans=controls_on_strip(rod,q,32)
    if not ans['pass_strip']:
        ans=controls_on_strip(rod,q,128)
    if not ans['pass_strip']:
        ans=controls_on_strip(rod,q,512)
    return ans


def physical_output(rod,phase,q,cur,source_center,sigma=0.):
    h,alpha=phase_center(phase,True,rod.count)
    hcheck,alpha2=phase_center(phase,False,rod.count)
    seam=[];rigid=[];edge_errors=[]
    # Dense reconstruction for any other original l,v uses the stored controls and same ODE.
    # Raw position and five derivatives are in original arclength l and original longitudinal label v.
    for v in (-.203,.203):
        for y in (.10,.195,.20,.205,.50,.795,.80,.805,.90):
            jets,pair=rod.seam(cur,q,y,v)
            jets[0]+=h
            seam.append(dict(v=v,source_first_S_arc_fraction=y,ruling_foot_fraction=pair[0],
                             actual_material_jacobian=pair[1],physical_jets=jets.tolist()))
        for arc,fractions in ((0,(0.,1.)),(1,(0.,.10,.90,1.)),(2,(0.,.5,1.)),
                              (3,(0.,.5,1.)),(4,(0.,.5,1.))):
            for y in fractions:
                jets=rod.rigid_seam(phase,sigma,arc,y,v)
                if arc==1 and y in (.10,.90):
                    controlled,_=rod.seam(cur,q,y,v)
                    edge_errors.append(dict(v=v,y=y,jet_disagreements=np.linalg.norm(jets-controlled,axis=1).tolist()))
                jets[0]+=h
                rigid.append(dict(v=v,upper_section=arc,fraction=y,physical_jets=jets.tolist()))
    def placed(frame):
        out=frame.copy()
        out[0]+=h
        return out.tolist()
    return dict(h0=source_center.tolist(),h_lambda=h.tolist(),centroid_independent_difference=float(np.linalg.norm(h-hcheck)),
                rotation_phase_from_original_pulses=alpha-ALPHA,analytic_phase=phase,
                centerline_angle_checks=[float(abs(alpha-ALPHA-phase)),float(abs(alpha-alpha2))],
                upper_actual_near_position_e_T_n=placed(cur['near']),upper_target_far_position_e_T_n=placed(cur['target']),
                upper_measured_far_position_e_T_n=placed(cur['end']),source_l_v_jets=seam,
                jet_order=['X','X_l','X_v','X_ll','X_lv','X_vv'],
                rigid_seam_by_original_section=rigid,controlled_to_rigid_actual_six_jet_differences=edge_errors,
                maximum_join_jet_error=max(max(x['jet_disagreements']) for x in edge_errors),
                lower_material_is_v_reversed=True,left_material_is_x_reflected=True)
