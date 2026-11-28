"""The genuine three per-ray displacement equations and all angular parameter derivatives."""
import numpy as np
from scipy.optimize import least_squares

import r750_rigid_annulus as old
import r760_meridian_moments as moments

weak=old.weak


def rot(m,v):return weak.fields.apply(m,v)


def before_s(build,phase,ss,order):
    h=weak.physical.H
    r,w=moments.rules(np.r_[0.,h,h+h*np.array([.002,.004,.5,.996,.998]),2*h],order)
    n=len(ss);d=np.repeat(r,n);s=np.tile(ss,len(r))
    j=weak.fields.collar_jets(build,phase,d,s,True)
    o=weak.fields.collar_jets(build,0.,d,s,False)
    a,_,az=weak.fields.frames(j);b,_,bz=weak.fields.frames(o)
    bt=weak.fields.trans(b);q=a@bt;qz=az@bt+a@weak.fields.trans(bz)
    val=rot(q,o[1])-o[1]
    der=rot(qz,o[1])+rot(q,o[4])-o[4]
    jh,jhs=(np.einsum('r,rsj->sj',w,arr.reshape(len(w),n,3)) for arr in (val,der))
    delta,ds=build.target(phase).angular_data(ss);ds=ds/build.ring.length
    x,xa=weak.fields.rotation(delta,0)
    _,t,n0,k,_=build.ring.jets(ss)
    _,kind,v=build.ring.label(ss);orient=np.where(kind==0,1.,np.where(kind==2,-1.,0.))
    weight,wp,_=weak.physical.native_w(v)
    inv=np.where(abs(v)<.6,1.,-1.)*np.sign(v)*orient/weak.B0
    p=weak.physical.physical_psi(np.full(len(ss),2*h),build.order)[0]
    b2=weight*inv*p;b2s=wp*orient*inv*p
    nv=np.column_stack((np.zeros(len(ss)),n0));nd=np.column_stack((np.zeros(len(ss)),-k[:,None]*t))
    diff=rot(x,nv)-nv
    jh+=b2[:,None]*diff
    jhs+=b2s[:,None]*diff+b2[:,None]*(ds[:,None]*rot(xa,nv)+rot(x,nd)-nd)
    return jh,jhs


def targets(build,phase,ss,order):
    n=len(ss);p=build.ring.length
    gamma,t,n0,k,_=build.ring.jets(ss);target,tt,nn,kt,_=build.target(phase).jets(ss)
    delta,ds=build.target(phase).angular_data(ss);ds=ds/p
    jh,jhs=before_s(build,phase,ss,order)
    anchor=build.radius_at(np.array([old.CLOSE_ELL]));ui=build.profile.read(anchor)[1][0]
    q=old.turn(phase)[1:,1:]
    bi=gamma-ui*n0-build.ring.origin
    inner=old.core_shift(build,phase)+np.column_stack((np.zeros(n),bi@(q-np.eye(2)).T))
    outer=np.column_stack((np.zeros(n),target-gamma))
    dh=np.column_stack((np.zeros(n),((1+k*ui)[:,None]*t)@(q-np.eye(2)).T-(tt-t)))-jhs
    val=inner-outer-jh
    cap=weak.FILLET_START;end=old.CLOSE_ELL;tip=.5074*phase
    width=old.FLAT_START-cap
    cuts=np.unique(np.r_[cap,cap+weak.physical.L*moments.KNOTS,end])
    ell,w=moments.rules(cuts[(cuts>=cap)&(cuts<=end)],order)
    theta,_=moments.original(build,ell-moments.START)
    e,_=old.flat_step((ell-cap)/width)
    psi=(1-e[:,None])*delta+e[:,None]*tip;ps=(1-e[:,None])*ds
    co,si=np.cos(psi),np.sin(psi)
    nx=co*n0[:,0]-si*n0[:,1];ny=si*n0[:,0]+co*n0[:,1]
    tx=co*t[:,0]-si*t[:,1];ty=si*t[:,0]+co*t[:,1]
    weight=w*np.sin(theta)
    cap_delta=-np.column_stack((weight@(nx-n0[:,0]),weight@(ny-n0[:,1])))
    cap_s=np.column_stack((weight@((k+ps)*tx-k*t[:,0]),weight@((k+ps)*ty-k*t[:,1])))
    val[:,1:]-=cap_delta;dh[:,1:]-=cap_s
    yz=val[:,1:];z=dh[:,1:]
    dot=lambda x,y:np.sum(x*y,axis=1)
    goal=np.column_stack((-val[:,0],-dot(yz,nn),dot(yz,tt)))
    gs=np.column_stack((-dh[:,0],-dot(z,nn)+kt*dot(yz,tt),dot(z,tt)+kt*dot(yz,nn)))
    return goal,gs,jh


def moment_rule(build,order):
    cuts=np.r_[*(a+h*moments.KNOTS for a,h in ((0.,old.early.LEG),(old.early.LEG,2*old.early.LEG),
                                                (3*old.early.LEG,old.early.LEG)))]
    z,w=moments.rules(cuts,order);theta=moments.original(build,z)[0]
    g=theta/.16
    return theta,g,g*g,w


def values(p,rule):
    c,b,a=p;theta,g,f,w=rule
    st,ct=np.sin(c*theta),np.cos(c*theta)
    sb,cb=np.sin(b*f),np.cos(b*f);sa,ca=np.sin(a*g),np.cos(a*g)
    D=w@(2*np.sin(.5*(c+1)*theta)*np.sin(.5*(c-1)*theta)+ct*2*np.sin(.5*b*f)**2)
    ans=np.array([D,w@(ct*sb*ca),w@(st*cb*sa)])
    jac=np.array([[w@(theta*st*cb),w@(ct*sb*f),0.],
                  [-w@(theta*st*sb*ca),w@(ct*cb*f*ca),-w@(ct*sb*sa*g)],
                  [w@(theta*ct*cb*sa),-w@(st*sb*f*sa),w@(st*cb*ca*g)]])
    return ans,jac


def solve_labels(build,phase,ss,order):
    goal,goal_s,jh=targets(build,phase,ss,order)
    if phase<=.008:lo=np.array([.8,-.061,-.4]);hi=np.array([5.2,.061,.4])
    elif phase<=.02:lo=np.array([3.6,-.21,-.23]);hi=np.array([6.6,.21,.23])
    else:lo=np.array([4.3,-.50,-.38]);hi=np.array([8.8,.50,.38])
    rule=moment_rule(build,order);roots=[];ds=[];defect=[];jac=[]
    for y,ys in zip(goal,goal_s,strict=True):
        fun=lambda x:values(x,rule)[0]-y
        separate=lambda x:values(x,rule)[1]
        c0=1+build.r760_states[phase][True]['parameter']
        state=least_squares(fun,np.clip([c0,0.,0.],lo+1.e-8,hi-1.e-8),jac=separate,
                            bounds=(lo,hi),xtol=1.e-14,ftol=1.e-14,gtol=1.e-14,max_nfev=60)
        actual,J=values(state.x,rule)
        # A few ordinary Newton steps remove scaled-gradient termination error.
        v=state.x.copy()
        for _ in range(3):
            if np.max(abs(actual-y))<1.e-13:break
            v-=np.linalg.solve(J,actual-y)
            actual,J=values(v,rule)
        if (not np.all(v>lo) or not np.all(v<hi) or np.max(abs(actual-y))>2.e-12
                or not np.isfinite(np.r_[v,J.ravel(),ys]).all()):
            raise ArithmeticError('R760 true three-moment material label failed its certified parameter box')
        roots.append(v);ds.append(np.linalg.solve(J,ys));defect.append(actual-y);jac.append(J)
    return dict(labels=ss,goal=goal,goal_sigma=goal_s,parameters=np.array(roots),parameter_sigma=np.array(ds),
                jacobian=np.array(jac),actual_defect=np.array(defect),native_outer_collar=jh,order=order)


def lookup(build,phase,labels):
    ss,reverse=np.unique(labels,return_inverse=True)
    if not 0<=phase<=.08:raise ValueError('R760 three exact periods have only this phase certificate')
    if not phase:
        return np.tile([1.,0.,0.],(len(labels),1)),np.zeros((len(labels),3))
    by_angle=build.r760_label_states.setdefault(phase,{})
    missing=np.array([s for s in ss if float(s) not in by_angle])
    for offset in range(0,len(missing),32):
        m=missing[offset:offset+32]
        fine=solve_labels(build,phase,m,48);independent=solve_labels(build,phase,m,32)
        err=np.max(np.abs(fine['parameters']-independent['parameters']),axis=1)
        derr=np.max(np.abs(fine['parameter_sigma']-independent['parameter_sigma']),axis=1)
        if max(err)>2.e-8 or max(derr)>2.e-6:
            raise ArithmeticError('independent true radial/collar quadratures disagree on the R760 inverse')
        for j,s in enumerate(m):
            by_angle[float(s)]={k:v[j] for k,v in fine.items() if isinstance(v,np.ndarray)}
            by_angle[float(s)].update(independent_parameter_error=err[j],independent_sigma_error=derr[j])
    ans=[by_angle[float(s)] for s in ss]
    return tuple(np.array([rec[k] for rec in ans])[reverse] for k in ('parameters','parameter_sigma'))
