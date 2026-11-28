"""Read both actual angle reconstructions, rigid closure, and two-component objective."""
from __future__ import annotations
import math
import numpy as np
from r683_proper_phase_metric_transport_20261128 import shell,shell_ok
from r703_weighted_material_field import dot,weighted_I


def cones(sh,angle):
    _,D,Y,rr,rp,pp=sh
    N=np.cross(D,Y);det=dot(N,N)
    if np.min(det.real)<=1e-12 or not np.all(np.isfinite(det)):raise FloatingPointError('Nonimmersed physical reconstruction.')
    n=N/np.sqrt(det)[...,None];a,b,c=dot(D,D),dot(D,Y),dot(Y,Y)
    L,M,K=dot(n,rr),dot(n,rp),dot(n,pp)
    vals=[]
    for sign in (-.03,.03):
        vals.extend((1+sign*(c*L-2*b*M+a*K)/(2*det),
                     ((a+sign*L)*(c+sign*K)-(b+sign*M)**2)/det))
    vals.extend((n[...,2],n[...,2]*math.cos(angle)+n[...,0]*math.sin(angle)))
    return vals,(a,b,c,det,L,M,K)


def relmetric(tensors,e):
    a,b,c=tensors[:3]
    z,w=a/e**2-1,c-1
    return abs((z+w)/2)+np.sqrt(((z-w)/2)**2+(b/e)**2)


def direction(g,st,n):
    angles=np.linspace(-np.pi,np.pi,n,endpoint=False)
    direction=np.stack((np.cos(angles),np.sin(angles)),axis=1)
    A=abs(np.angle(np.exp(1j*(angles+g.theta))));B=abs(angles);T=.03
    span=g.b-g.a;S=(g.w@st['meridian_e'])[:,None];C=st['C'][0,[0,2]]
    if np.any(S.real<=T*np.max(abs(A-B))):raise FloatingPointError('End tangent cones fail to meet.')
    mm=(A+B-S/T)/2;merge=np.where(mm.real>0,mm,0.)
    U=np.where(mm.real>0,T*(np.sin(A)+np.sin(B)-2*np.sin(merge)),S-T*(A-np.sin(A)+B-np.sin(B)))
    vec=np.array([g.b-g.a*math.cos(g.theta),g.a*math.sin(g.theta)])
    return ((direction@vec)[None,:]+np.array([[-1.],[1.]])*(direction@C)[None,:]-U)/span,S[:,0]


def barrier(z,gap):
    mask=z.real>0;res=np.zeros_like(z);res[mask]=z[mask]*np.exp(-gap/z[mask]);return res


def objective(g,st,level,opt,selection=False):
    w=np.sqrt(g.w[:,None]*st['J']/((g.b-g.a)*len(g.phi)))
    # Fixed outer circle has zero integration weight; interior Gauss points carry the full objective.
    rows=[(w*dot(st['G'],u)).ravel() for u in (st['Ur'],st['Br'])]
    rows.append(opt['closure_weight']*(np.sqrt(g.w/(g.b-g.a))*st['closure'][:,1]))
    masks=[np.ones(row.size,dtype=bool) for row in rows]
    gw=np.sqrt(g.guard_weights[:,None]*st['J']/((g.b-g.a)*len(g.phi)))
    for sh,weights in ((st['F'],gw),(st['Fi'],gw),(st['Fi_left'],gw[g.edge_ids])):
        vv,_=cones(sh,g.theta)
        for i,a in enumerate(vv):
            guard=opt['axis_guard'] if i>=4 else opt['cone_guard']
            rows.append((weights*opt['geometry_weight']*barrier(guard-a,opt['barrier_width'])).ravel())
            masks.append((a.real<guard).ravel())
    z,_=direction(g,st,opt['work_betas'])
    rows.append((opt['length_weight']*barrier(z+level*.0002/(g.b-g.a),.0005)/np.sqrt(z.size)).ravel())
    masks.append((z.real+level*.0002/(g.b-g.a)>0).ravel())
    result=np.concatenate(rows)
    return (result,np.concatenate(masks)) if selection else result


class ActualPose:
    def __init__(self,g,center):self.ang=g.theta;self.b=g.b;self.C=center
    def center(self,x,r):return self.C


def read(g,st,nbeta):
    geo=[];metrics=[];interior=[];peaks=[]
    allrows=np.arange(len(g.r))
    for sh,rows in ((st['F'],allrows),(st['Fi'],allrows),(st['Fi_left'],g.edge_ids)):
        vv,ten=cones(sh,g.theta);a,b,c,det,L,M,K=ten
        mean=(c*L-2*b*M+a*K)/(2*det);gauss=(L*K-M*M)/det
        curv=abs(mean)+np.sqrt(np.maximum(0.,mean**2-gauss));eta=relmetric(ten,st['e0'][rows,None])
        aspect=relmetric(ten,st['e'][rows]);metrics.append(float(eta.max()));interior.append(float(aspect.max()))
        im=np.unravel_index(eta.argmax(),eta.shape);ik=np.unravel_index(curv.argmax(),curv.shape)
        peaks.append(dict(rotational_metric_at=[float(g.r[rows[im[0]]]),float(st['angle'][rows[im[0]],im[1]])],curvature_at=[float(g.r[rows[ik[0]]]),float(st['angle'][rows[ik[0]],ik[1]])],
                          maximum_curvature=float(curv.max())))
        C=st['C'][rows];rd=g.r[rows];U=(sh[0]-C[:,None,:])/rd[:,None,None]
        geo.append(shell(ActualPose(g,C),None,dict(r=rd,q=np.zeros_like(rd)),dict(U=U),
                    dict(actual_center=C[0,[0,2]],min_outer_normal=float(vv[4].min()),
                         min_inner_normal=float(vv[5].min()),max_abs_curvature=float(curv.max()))))
    d,S=direction(g,st,nbeta);T=st['j']['T'].x;psi=g.phi;r=g.r[:,None];bound={}
    for i,angle,label in ((0,g.theta,'inner'),(-1,0.,'outer')):
        co,si=np.cos(psi),np.sin(psi);ca,sa=np.cos(angle),np.sin(angle)
        R=np.stack((ca*co,si,-sa*co),axis=-1);Et=np.stack((-ca*si,co,sa*si),axis=-1)
        known=[st['C'][i]+g.r[i]*R,R,Et,np.zeros_like(R),Et/g.r[i],-R/g.r[i]]
        bound[label]={name:[float(np.max(np.linalg.norm(k[i]-wanted,axis=-1))) for k,wanted in zip(sh,known)]
                      for name,sh in (('continuous_formula',st['F']),('angular_and_center_interpolant',st['Fi']),('other_one_sided_center',st['Fi_left']))}
    viol=[]
    for a in geo:
        viol.extend(max(0.,-v) for k,v in a.items() if k.startswith('sampled_') and ('margin' in k or k.endswith('_min') or k.endswith('dominance')))
        viol.extend([max(0.,a['sampled_whole_D_upper_estimate']-1),max(0.,-a['peg_outer_tube_cylinder_margin'])])
    G=st['G'];jj=st['J']
    return dict(sampled_whole_shell_pass=all(shell_ok(a) for a in geo),sampled_shell_violation=float(sum(viol)),
                paired_geometry=geo,physical_peaks=peaks,sampled_rotational_eta=max(metrics),sampled_design_eta=max(interior),
                paired_rotational_metric=metrics,paired_design_metric=interior,actual_rim_six_jets=bound,
                sample_min_tangent_speed=float(st['j']['v'].x.min()),sample_min_material_angle_jacobian=float(jj.min()),
                sample_min_virtual_e=float(st['e'].min()),sample_max_virtual_e=float(st['e'].max()),
                physical_angle_warp=float(np.max(abs(st['material_change']))),sampled_rms_curl=float(np.sqrt(np.max((dot(G,G)*jj).mean(axis=1)))),
                sampled_max_curl=float(np.max(np.linalg.norm(G,axis=-1))),discarded_exact_tangent_component=float(np.max(abs(dot(G,T)))),
                true_ring_closure=float(np.max(np.linalg.norm(st['closure'],axis=-1))),true_target_meridian_lengths_0_pi=S.tolist(),
                true_angular_length_margin=float(-d.max()*(g.b-g.a)),actual_center=st['C'][0].tolist(),
                finite_mass_raw_value_and_scaled_radial_residuals=st['sampled_raw_mass_errors'],scaled_mass_derivative_min=st['mass_margin'],scaled_mass_residual=st['mass_error'])


def transport_cost(g,old,soft):
    anc=g.anchor;T=anc['T'];r=g.r[:,None,None]
    unit=np.ones((len(g.r),len(g.phi)))
    I,mean=weighted_I(T[0,0],unit);Ir,mt=weighted_I(T[1,0],unit);Irr,_=weighted_I(T[2,0],unit)
    H=T[0,0]-mean
    original=[anc['original_center'][:,None,:]+r*I,anc['original_center_slope'][:,None,:]+I+r*Ir,
              H,anc['original_center_acc'][:,None,:]+2*Ir+r*Irr,(H+r*(T[1,0]-mt))/r,T[0,1]/r]
    def six(a,b):return [float(np.max(np.linalg.norm(x-y,axis=-1))) for x,y in zip(a,b)]
    projected=old['virtual']-anc['original_D'];j=old['j'];identity=(dot(anc['original_G'],j['T'].x)/j['v'].x)[...,None]*j['U'].x
    choice=soft['virtual']-old['virtual']
    return dict(**anc['errors'],source_grid_original_six_to_true_projected=six(original,old['F']),
                source_grid_projected_to_softened_six=six(old['F'],soft['F']),
                two_projected_inner_centers=[old['C'][0].tolist(),soft['C'][0].tolist()],
                nearest_radial_column_change=float(np.max(np.linalg.norm(projected,axis=-1))),
                old_numerical_to_analytic_projection_formula_disagreement=float(np.max(np.linalg.norm(projected-identity,axis=-1))),
                true_p_to_smoothed_p_radial_column_change=float(np.max(np.linalg.norm(choice,axis=-1))),
                old_to_projected_virtual_squared_length=float(np.max(abs(old['e']**2-anc['original_e']**2))),
                projected_to_smoothed_virtual_squared_length=float(np.max(abs(soft['e']**2-old['e']**2))))
