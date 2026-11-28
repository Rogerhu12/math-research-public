"""Integrate each true meridian pair once and use that same contribution at its reflected depth."""
import numpy as np

import r765_paired_material as pair

model=pair.model


def kernel(build,phase,degree,radii,ss,order,physical_breaks):
    """One actual angle block, with the canonical u cuts of both original R760 members."""
    r=np.asarray(radii,float);s=np.asarray(ss,float)
    if r.ndim!=1 or s.ndim!=1 or not len(s) or not len(r):raise ValueError('empty radial reconstruction block')
    ell=model.space.ell_data(r)[0]
    u=np.clip(np.minimum(ell,pair.SUM-ell),*pair.OUTER)
    a,b=pair.OUTER
    four=build.radius_at(np.r_[a,b,pair.SUM-b,pair.SUM-a])
    original_radii=np.asarray(physical_breaks(build,four))
    marks=model.space.ell_data(original_radii)[0]
    all_marks=np.r_[a,b,*pair.ACTIVE,marks,pair.SUM-marks,u]
    cuts=np.unique(all_marks[(all_marks>=a)&(all_marks<=b)])
    points,weights=model.moments.rules(cuts,order)
    distance,kind,_=build.ring.label(s)
    start=np.where(kind==1,2.,4.+build.ring.LU)
    uv=(distance-start)/build.ring.LU
    active=np.flatnonzero(((kind==1)|(kind==3))&(uv>.10)&(uv<.90))
    result=dict(cuts=cuts,points=points,weights=weights,mark=np.searchsorted(cuts,u),radii=r,angles=s,
                active=active,phase=phase,degree=degree,order=order)
    if not len(active):return result
    sr=s[active];pa=build.radius_at(points);pb=build.radius_at(pair.SUM-points)
    first=model.R760Frame(build,phase,pa[:,None],sr[None,:],degree)
    other=model.R760Frame(build,phase,pb[:,None],sr[None,:],degree)
    p,sp=np.broadcast_arrays(points[:,None],sr[None,:])
    basis=pair.new_basis(build,degree,p.ravel(),sp.ravel())
    if max(np.max(abs(model.space.ell_data(pa)[0]-points)),
           np.max(abs(model.space.ell_data(pb)[0]-(pair.SUM-points))))>5.e-14:
        raise ArithmeticError('canonical pair did not recover the actual source arclengths')
    result.update(first=first,other=other,basis=basis)
    return result


def partial(kernel,q,y):
    """Return physical position and normalized angular derivative increments at every original radius."""
    ns=len(kernel['angles']);nr=len(kernel['radii']);cols=kernel['active']
    change=np.zeros((nr,ns,2,3))
    if not len(cols) or not np.any(y):
        return dict(position_and_s=change,compatible_endpoint=np.zeros((ns,2,3)),physical_pair_defect=0.,
                    maximum_position_change=0.,support_count=len(cols))
    f,g=kernel['first'],kernel['other']
    aa=pair.physical_parts(f,q);bb=pair.physical_parts(g,q)
    fj=pair.twist.original_from_local(f,*aa);gj=pair.twist.original_from_local(g,*bb)
    e0,e1=model.space.ell_data(f.r),model.space.ell_data(g.r)
    ax=tuple(v@y for v in kernel['basis'])
    _,zz=pair.paired_jet(fj,gj,e0,e1,np.ones(len(f.r),dtype=bool),ax)
    E,Es=zz['E'],zz['E_s']
    # This independent check uses the second true vector and its angular jet;
    # the integrated second increment always comes from -E on the same rule.
    L2,_,L2s=pair.unit_radial(gj,e1[1],e1[2])
    use=model.weak.fields.apply
    m=use(zz['H_minus_I'],L2)
    ms=use(zz['H_s'],L2)+use(zz['H_minus_I'],L2s)
    observation=max(float(np.max(abs(E+m))),float(np.max(abs(Es+ms))))
    if not np.isfinite(observation) or observation>3.e-9:
        raise ArithmeticError('opposite actual meridian jets do not conserve the angular endpoint')
    data=np.stack((E,Es),axis=1).reshape(len(kernel['points']),len(cols),2,3)
    integrated=(kernel['weights'][:,None,None,None]*data).reshape(len(kernel['cuts'])-1,kernel['order'],len(cols),2,3).sum(axis=1)
    prefix=np.concatenate((np.zeros_like(integrated[:1]),np.cumsum(integrated,axis=0)))
    change[:,cols]=prefix[kernel['mark']]
    # Do not subtract separately integrated interior moment arrays. Both paired
    # windows add the same physical row with opposite signs by construction.
    return dict(position_and_s=change,compatible_endpoint=np.zeros((ns,2,3)),
                signed_complete_first_window=prefix[-1],signed_complete_second_window=-prefix[-1],
                partial_cuts=kernel['cuts'],physical_pair_defect=observation,
                maximum_position_change=float(np.linalg.norm(change[:,:,0],axis=-1).max()),support_count=len(cols))


def correction_jets(primary,partner,q,z,y,aux_basis,pair_basis,first):
    """The three true local radial differential changes; no endpoint or new metric inferred from these."""
    old=pair.twist.original_from_local(primary,*pair.physical_parts(primary,q))
    out,data=pair.physical(primary,partner,q,z,y,aux_basis,pair_basis,first)
    return dict(Pr=out[1]-old[1],Prr=out[4]-old[4],Prs=out[3]-old[3],
                native_curl=out[0]/primary.det[:,None],coframe_s=out[2],coframe_ss=out[5],
                canonical_position_integrand=data['E'],canonical_integrand_s=data['E_s'])


def assembled_physical(old_jets,position_and_s,radial,minus,plus,delta_s):
    """Return all six reconstructed jets. Pss uses the actual centered instrument at its recorded spacing."""
    corrected=[np.array(a,copy=True) for a in old_jets]
    corrected[0]+=position_and_s[:,:,0];corrected[2]+=position_and_s[:,:,1]
    for j,k in ((1,'Pr'),(3,'Prr'),(4,'Prs')):corrected[j]+=radial[k]
    corrected[5]+=(plus[:,:,1]-minus[:,:,1])/(2.*delta_s)
    return tuple(corrected)
