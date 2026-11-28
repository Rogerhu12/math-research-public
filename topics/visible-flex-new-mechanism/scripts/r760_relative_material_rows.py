"""True R750 endpoint rows on R760 material quadrature, retaining eligible original ray data."""
import numpy as np
from scipy.sparse import csr_matrix,hstack,vstack

import r750_relative_boundary as before
import r760_full_annulus_frame as model


def matched_rows(previous_rule,now):
    old=np.asarray(previous_rule['radius']);new=np.asarray(now['radius'])
    if not np.all(np.diff(old)>0) or not np.all(np.diff(new)>0):
        raise ValueError('R760 original and refined material quadratures must be strictly increasing')
    at=np.searchsorted(old,new)
    keep=at<len(old);keep[keep]=old[at[keep]]==new[keep]
    return np.flatnonzero(keep),at[keep]


def redisplay(piece,new_base,pr,bmat,grid,ss):
    order=np.asarray(ss)
    nr,ns=len(grid['radius']),len(order)
    if bmat.shape!=(nr*ns,piece['nterm']) or new_base.shape!=(nr*ns,3,3) or pr.shape!=(nr*ns,3):
        raise ValueError('incomplete transported original material kernel')
    return dict(shape=(nr,ns),ns=ns,ss=order,weights=grid['weights'],goals=piece['goals'],
                physical_source_inner=piece['physical_source_inner'],inner_displacement=piece['inner_displacement'],
                matrix=new_base,pr=pr,nterm=piece['nterm'],data=bmat.data,indices=bmat.indices,indptr=bmat.indptr)


def kernel(build,phase,degree,ss,grid,prior=None):
    """prior=(old material rule, original R750 kernel at exactly these angles and degree)."""
    build.set_phase(phase);ss=np.asarray(ss);nr,ns=len(grid['radius']),len(ss)
    rr=np.asarray(grid['radius']);allrows=np.arange(nr)
    old=None;keep=np.empty(0,dtype=int);loc=keep;nterm=len(model.shoulders.tags(degree))
    if prior is not None:
        pg,old=prior
        if (old['nterm']!=len(model.old.tags(degree)) or not np.array_equal(ss,old['ss']) or pg['order']!=grid['order']
                or pg['anchor']!=grid['anchor'] or not np.array_equal(pg['weights'],old['weights'])):
            raise ValueError('different original R750 material rule, angular labels or native space')
        keep,loc=matched_rows(pg,grid)
    missing=np.setdiff1d(allrows,keep,assume_unique=True)
    ordered=np.r_[keep,missing]
    mats=[];vectors=[];blocks=[]
    if len(keep):
        flat=(loc[:,None]*ns+np.arange(ns)).ravel()
        m=old['matrix'][flat].copy()
        v=old['pr'][flat]
        el=model.space.ell_data(rr[keep])[0]
        changed=(el>model.moments.START)&(el<model.old.FLAT_START)
        flatell=np.repeat(el,ns);ids=np.flatnonzero(np.repeat(changed,ns))
        for j in range(0,len(ids),4096):
            i=ids[j:j+4096]
            m[i]=model.axial_jet(build,phase,flatell[i],ss[i%ns],build.r760_small)[0][0]
        mats.append(m);vectors.append(v)
        rawr=np.repeat(rr[keep],ns);raws=np.tile(ss,len(keep))
        newcols=[]
        for j in range(0,len(rawr),4096):
            newcols.append(model.shoulders.appended(build,degree,rawr[j:j+4096],raws[j:j+4096],False))
        blocks.append(hstack((before.controls(old)[flat],vstack(newcols,format='csr')),format='csr'))
    for lo in range(0,len(missing),64):
        ids=missing[lo:lo+64]
        frame=model.R760Frame(build,phase,rr[ids,None],ss[None,:],degree)
        mats.append(frame.base);vectors.append(frame.j0[1]);blocks.append(csr_matrix(frame.B))
    if old is None:
        pi=build.geometry(np.full_like(ss,grid['anchor']),ss)[0][0]
        outer=build.boundary_jets(phase,ss)[0]-build.boundary_jets(0.,ss)[0]
        origin=np.r_[build.profile.endx,build.ring.origin]
        inner=model.old.core_shift(build,phase)+(pi-origin)@(model.old.turn(phase)-np.eye(3)).T
        old=dict(nterm=nterm,goals=outer-inner,physical_source_inner=pi,inner_displacement=inner)
    restore=(np.argsort(ordered)[:,None]*ns+np.arange(ns)).ravel()
    old={**old,'nterm':nterm}
    out=redisplay(old,np.concatenate(mats)[restore],np.concatenate(vectors)[restore],
                  vstack(blocks,format='csr')[restore],grid,ss)
    out['original_geometry_and_coefficient_rows']=len(keep)*ns
    out['new_material_rows']=len(missing)*ns
    return out


def relative_seed(build,phase,ss,order):
    """Independent curl-free-axis integral and honest two transverse residual components.

    Positive integral points from the original outer to the rigid inner anchor.
    Original numerical h^4Q correction is read directly before taking its integral.
    """
    build.set_phase(phase);ss=np.asarray(ss);n=len(ss)
    per=build.ring.length;h=model.weak.physical.H
    lo,hi=0.,2*h
    d,wt=model.moments.rules(np.r_[lo,h,h+h*np.array([.002,.004,.5,.996,.998]),hi],order)
    d=np.broadcast_to(d[:,None],(len(wt),n));s=np.broadcast_to(ss,d.shape)
    dd=d.ravel();ang=s.ravel()
    j=model.weak.fields.collar_jets(build,phase,dd,ang,True)
    j0=model.weak.fields.collar_jets(build,0.,dd,ang,False)
    m=model.weak.fields.frames(j)[0]@model.weak.fields.trans(model.weak.fields.frames(j0)[0])
    db=model.weak.fields.apply(m,j0[1])-j0[1]
    jh=np.einsum('r,rsj->sj',wt,db.reshape(len(wt),n,3))
    # From 2h to START the orientation is Rx(delta), and b(START)=0.
    delta,_=build.target(phase).angular_data(ss)
    rx=model.weak.fields.rotation(delta,0)[0]
    gamma,t0,n0,k,_=build.ring.jets(ss)
    _,kind,v=build.ring.label(ss);orient=np.where(kind==0,1.,np.where(kind==2,-1.,0.))
    amp=model.weak.physical.native_w(v)[0]*np.where(abs(v)<.6,1.,-1.)*np.sign(v)*orient/model.weak.B0
    b2=amp*model.weak.physical.physical_psi(np.full(n,hi),build.order)[0]
    nn=np.column_stack((np.zeros(n),n0))
    jh+=b2[:,None]*(model.weak.fields.apply(rx,nn)-nn)
    anchor=float(build.radius_at(np.array([model.old.CLOSE_ELL]))[0])
    ui=float(build.profile.read(np.array([anchor]))[1][0])
    end=model.old.CLOSE_ELL-model.moments.START
    breaks=model.moments.cuts(build,build.r760_profile)
    breaks=np.unique(np.r_[0.,breaks[(breaks>0.)&(breaks<end)],.065-model.moments.START,end])
    z,w=model.moments.rules(breaks,order);ell=z+model.moments.START
    state=build.r760_states[phase][bool(build.r760_small)]
    th,_,o,_=model.moments.mixture(build,z,build.r760_profile,state)
    closed=build.r760_three_periods and phase<=.08
    l0,l1=(model.weak.FILLET_START,model.old.FLAT_START) if closed else (.065,model.weak.FILLET_START)
    g,_=model.old.flat_step((ell-l0)/(l1-l0))
    psi=(1-g[:,None])*delta+g[:,None]*(.5074*phase)
    th=np.broadcast_to(th[:,None],psi.shape).copy()
    if closed:
        coeff,_=model.triple.lookup(build,phase,ss);c,b,a=coeff.T
        th[:]=o[:,None]
        here=ell<=model.weak.FILLET_START
        ovals=o[here,None];gg=ovals/.16
        th[here]=ovals*c+gg*gg*b;psi[here]+=gg*a
    n1,n2=n0[:,0],n0[:,1];cp,sp=np.cos(psi),np.sin(psi)
    depth=w[:,None]*np.sin(th)
    integ=np.column_stack((np.sum(depth*(cp*n1-sp*n2),axis=0),np.sum(depth*(sp*n1+cp*n2),axis=0)))
    dx=w@(2*np.sin(.5*(th+o[:,None]))*np.sin(.5*(o[:,None]-th)))
    correction=np.column_stack((dx,ui*n0-integ))
    pi=build.geometry(np.full(n,anchor),ss)[0][0]
    outer=build.boundary_jets(phase,ss)[0]-build.boundary_jets(0.,ss)[0]
    origin=np.r_[build.profile.endx,build.ring.origin]
    inside=model.old.core_shift(build,phase)+(pi-origin)@(model.old.turn(phase)-np.eye(3)).T
    res=outer+jh+correction-inside
    limit=float(np.max(abs(res))) if closed else float(np.max(abs(res[:,0]-jh[:,0])))
    if not np.isfinite(res).all() or limit>4.e-10:
        raise ArithmeticError('true endpoint, original source angle or full axial moment disagree')
    return dict(order=order,phase=phase,labels=ss,outer_displacement=outer,inner_displacement=inside,
                true_collar_and_straight_period=jh,free_meridian_period=correction,
                outward_to_inward_residual=res,relative_peak_by_axis=np.max(abs(res),axis=0),
                source_inner_u=ui,source_perimeter=per,small_branch=bool(build.r760_small),all_three_matched=closed)
