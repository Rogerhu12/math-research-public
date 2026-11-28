"""True finite harmonic position feedback on one fixed normalized packet metric."""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


def harmonics(count, angles, offset=0.0, fundamental=2):
    u = 2 * np.pi * (np.arange(angles) + offset) / angles
    freq = fundamental * np.arange(count)
    return freq, np.cos(freq[:, None] * u), np.sin(freq[:, None] * u)


def gram(R, w, mode, deriv, angle_count=40, offset=0.0, need_modes=False, second=None, wr=None, fundamental=2):
    if len(R)>1536:
        top=None; all_rows=[]; maxima=np.zeros(3)
        for i in range(0,len(R),1536):
            h=slice(i,min(i+1536,len(R)))
            out=gram(R[h],w[h],mode[h],deriv[h],angle_count,offset,need_modes,
                     None if second is None else second[h],None if wr is None else wr[h],fundamental)
            obs,extra=out if need_modes else (out,None)
            maxima=np.maximum(maxima,obs['components'])
            if top is None or obs['metric']>top['metric']:
                top={**obs,'at':[obs['at'][0]+i,obs['at'][1]]}
            if extra is not None:
                all_rows.append(extra)
        top['components']=maxima.tolist()
        if need_modes:
            return top,tuple(np.concatenate(x,axis=0) for x in zip(*all_rows))
        return top
    freq, cos, sin = harmonics(mode.shape[2], angle_count, offset, fundamental)
    a, b, c = np.moveaxis(mode, 1, 0)
    ar, br, cr = np.moveaxis(deriv, 1, 0)
    er, et, ez = ar @ cos, br @ sin, cr @ cos
    ur = (-freq * a - b) @ sin
    ut = (a + freq * b) @ cos
    uz = (-freq * c) @ sin
    e = 2 * (er + w[:, None] * ez) + er**2 + et**2 + ez**2
    f = ur + R[:, None]*et + w[:, None]*uz + er*ur + et*ut + ez*uz
    g = 2 * R[:, None]*ut + ur**2 + ut**2 + uz**2
    E, F, G = e / (1 + w[:, None]**2), f / (R*np.hypot(1,w))[:,None], g/R[:,None]**2
    op = abs((E+G)/2) + np.hypot((E-G)/2, F)
    i, j = np.unravel_index(np.argmax(op), op.shape)
    stats = dict(metric=float(op[i,j]), at=[int(i),int(j)], components=[float(np.max(abs(x))) for x in (E,F,G)])
    if not need_modes:
        return stats
    gur = (-freq * ar-br) @ sin
    gut = (ar+freq*br) @ cos
    guz = (-freq*cr) @ sin
    gr = 2*ut+2*R[:,None]*gut+2*(ur*gur+ut*gut+uz*guz)
    factor = np.full(len(freq), 2.0/angle_count)
    factor[0] /= 2
    rows=[(e,cos),(f,sin),(g,cos),(gr,cos)]
    if second is not None:
        aa,bb,cc=np.moveaxis(second,1,0)
        ar2,at2,az2=aa@cos,bb@sin,cc@cos
        u2r=(-freq*aa-bb)@sin
        u2t=(aa+freq*bb)@cos
        u2z=(-freq*cc)@sin
        ep=2*(ar2+wr[:,None]*ez+w[:,None]*az2+er*ar2+et*at2+ez*az2)
        fp=(gur+et+R[:,None]*at2+wr[:,None]*uz+w[:,None]*guz
            +ar2*ur+at2*ut+az2*uz+er*gur+et*gut+ez*guz)
        gpp=4*gut+2*R[:,None]*u2t+2*(gur**2+gut**2+guz**2+ur*u2r+ut*u2t+uz*u2z)
        rows.extend(((ep,cos),(fp,sin),(gpp,cos)))
    return stats, tuple((x @ y.T)*factor for x,y in rows)


def physical_scales(node, eps):
    n, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, d, qout, ro = node
    # Each band's physical unit is attached to its outer endpoint.
    w = .00014 * 1.5**(-3*n) / ro**7
    A = eps**2 * ro**7 * qout**2 / d**2
    return np.array([A, A/(w*d)])


def boundary_solve(R, w, nodes, eps, m, e, f, g, gr, ep, fp, gpp, higher):
    """Integrate the area-compatible mode and solve all packet boundaries together."""
    L = -g/(2*R)
    Lr = -gr/(2*R)-L/R
    source = Lr-L/R+m*f/R
    forcing = np.column_stack((source,(-e/2-source)/w))
    wr=nodes[:,5]
    Lrr=-gpp/(2*R)-2*Lr/R
    sp=Lrr-Lr/R+L/R**2+m*(fp/R-f/R**2)
    sprime=np.column_stack((sp,(-ep/2-sp-wr*forcing[:,1])/w))
    dr = np.diff(R)
    rm = (R[:-1]+R[1:])/2
    wm = np.sqrt(w[:-1]*w[1:])
    H = np.empty((len(dr),2,2))
    H[:,0,0], H[:,0,1] = -(m*m-1)/rm, -m*m*wm/rm
    H[:,1,0], H[:,1,1] = -H[:,0,0]/wm, (m*m)/rm
    ds = dr/(1-dr/(2*rm))
    T = np.eye(2)[None,:,:]+ds[:,None,None]*H
    sm = (forcing[:-1]+forcing[1:])/2
    B = dr[:,None]*sm + (dr*ds/2)[:,None]*np.einsum('ijk,ik->ij',H,sm)
    Hend=np.empty((len(R),2,2))
    Hend[:,0,0],Hend[:,0,1]=-(m*m-1)/R,-m*m*w/R
    Hend[:,1,0],Hend[:,1,1]=-Hend[:,0,0]/w,m*m/R
    if higher:
        # Lobatto IIIA elimination at the actual middle physical radius.
        hh=dr[:,None,None]
        wm=(w[:-1]+w[1:])/2+dr*(wr[:-1]-wr[1:])/8
        if np.min(wm)<=0:
            raise ValueError("radial mesh underresolves the positive slope")
        H[:,0,1],H[:,1,0]=-m*m*wm/rm,(m*m-1)/(wm*rm)
        a,b=Hend[:-1],Hend[1:]
        lm=np.eye(2)-hh*(b+2*H-(hh/2)*(H@b))/6
        rm0=np.eye(2)+hh*(a+2*H+(hh/2)*(H@a))/6
        sm=(forcing[:-1]+forcing[1:])/2+dr[:,None]*(sprime[:-1]-sprime[1:])/8
        qq=forcing[:-1]+forcing[1:]+4*sm+(dr/2)[:,None]*np.einsum('ijk,ik->ij',H,forcing[:-1]-forcing[1:])
        T=np.linalg.solve(lm,rm0)
        B=np.linalg.solve(lm,(dr[:,None]*qq/6)[:,:,None])[:,:,0]
    # Multiple shooting at every native phase-part boundary, with common shared nodes.
    changes = np.where((np.diff(nodes[:,0])!=0)|(np.diff(nodes[:,1])!=0))[0]
    ix = np.unique(np.r_[0,changes,len(R)-1])
    blocks, targets, scaling = [], [], [physical_scales(nodes[k],eps) for k in ix]
    for j,(a,b) in enumerate(zip(ix,ix[1:])):
        mat = np.diag(scaling[j])
        rhs = np.zeros(2)
        for k in range(a,b):
            rhs = T[k] @ rhs + B[k]
            mat = T[k] @ mat
        blocks.append(mat/scaling[j+1][:,None])
        targets.append(rhs/scaling[j+1])
    n = len(blocks)
    C = sparse.lil_matrix((2*n+2,2*(n+1)))
    y = np.zeros(C.shape[0])
    for i,(mat,rhs) in enumerate(zip(blocks,targets)):
        scale = np.sqrt(1+np.sum(mat**2,axis=1))
        C[2*i:2*i+2,2*i:2*i+2] = -mat/scale[:,None]
        C[2*i:2*i+2,2*i+2:2*i+4] = np.diag(1/scale)
        y[2*i:2*i+2] = rhs/scale
    # The growing homogeneous input is pinned at opposite ends.  In particular
    # the external vertical second harmonic stays exactly at its nonzero seed.
    C[-2,0] = 1.0
    C[-1,-1] = 1.0
    C=C.tocsr()
    interior=spsolve(C.tocsc(),y)
    if not np.all(np.isfinite(interior)):
        raise ValueError("singular mode constraint")
    residual=float(np.max(abs(C@interior-y)))
    X=np.empty((len(R),2))
    error=0.0
    for j,(a,b) in enumerate(zip(ix,ix[1:])):
        v=interior[2*j:2*j+2]*scaling[j]
        X[a]=v
        for k in range(a,b):
            v=T[k]@v+B[k]
            X[k+1]=v
        shared=interior[2*j+2:2*j+4]*scaling[j+1]
        error=max(error,float(np.max(abs(shared-v))))
        X[b]=shared
    aa,cc=X.T
    bb=(L-aa)/m
    dar=source-(m*m-1)*aa/R-m*m*w*cc/R
    dcr=(-e/2-dar)/w
    dbr=(Lr-dar)/m
    d2ar=sp+(m*m-1)*aa/R**2-(m*m-1)*dar/R-m*m*(wr/R-w/R**2)*cc-m*m*w*dcr/R
    d2cr=(-ep/2-d2ar-wr*dcr)/w
    d2br=(Lrr-d2ar)/m
    return (np.column_stack((aa,bb,cc)),np.column_stack((dar,dbr,dcr)),
            np.column_stack((d2ar,d2br,d2cr)),(residual,error))


def feedback(nodes,eps,depth,order,seen=None,higher=True,fundamental=2):
    R,w=nodes[:,3],nodes[:,4]
    if not np.all(np.diff(R)>0):
        raise ValueError('native radii must increase strictly')
    K=order//fundamental+1
    mode=np.zeros((len(R),3,K))
    deriv=np.zeros_like(mode)
    mode[:,0,0],deriv[:,0,0],deriv[:,2,0]=nodes[:,12],nodes[:,13],nodes[:,15]
    dR=np.diff(R)
    mode[:,2,0]=np.r_[0,np.cumsum(dR*(deriv[:-1,2,0]+deriv[1:,2,0])/2)]
    mode[:,0,1],deriv[:,0,1]=nodes[:,9],nodes[:,10]
    mode[:,1,1],deriv[:,1,1]=-nodes[:,9]/fundamental,-nodes[:,10]/fundamental
    mode[:,2,1],deriv[:,2,1]=nodes[:,6],nodes[:,7]
    second=np.zeros_like(mode)
    second[:,0,0],second[:,2,0]=nodes[:,14],nodes[:,16]
    second[:,0,1],second[:,1,1],second[:,2,1]=nodes[:,11],-nodes[:,11]/fundamental,nodes[:,8]
    base_mode,base_deriv,base_second=mode.copy(),deriv.copy(),second.copy()
    if seen is not None:
        mode,deriv=seen
    start=gram(R,w,mode,deriv,2*order+12,.317,fundamental=fundamental)
    cut=R[np.flatnonzero(nodes[:,0] <= nodes[0,0]-2)[0]]
    u=np.clip((R-R[0])/(cut-R[0]),0,1)
    chi=u**3*(10+u*(-15+6*u))
    chip=30*(u*(1-u))**2/(cut-R[0])
    chipp=60*u*(1-u)*(1-2*u)/(cut-R[0])**2
    hist=[]
    for it in range(depth):
        _,(E,F,G,Gr,Ep,Fp,Gpp)=gram(R,w,mode,deriv,4*order+8,0,True,second,nodes[:,5],fundamental)
        change=np.zeros_like(mode); dchange=np.zeros_like(mode); d2change=np.zeros_like(mode)
        change[:,0,0]=-G[:,0]/(2*R)
        dchange[:,0,0]=-Gr[:,0]/(2*R)-change[:,0,0]/R
        dchange[:,2,0]=(-E[:,0]/2-dchange[:,0,0])/w
        d2change[:,0,0]=-Gpp[:,0]/(2*R)-2*dchange[:,0,0]/R
        d2change[:,2,0]=(-Ep[:,0]/2-d2change[:,0,0]-nodes[:,5]*dchange[:,2,0])/w
        increment=dR*(dchange[1:,2,0]+dchange[:-1,2,0])/2
        if higher:
            increment+=dR**2*(d2change[:-1,2,0]-d2change[1:,2,0])/12
        change[:,2,0]=np.r_[0,np.cumsum(increment)]
        worst_constraint,edge_error=0.0,0.0
        for j in range(1,K):
            c,d,dd,err=boundary_solve(R,w,nodes,eps,fundamental*j,E[:,j],F[:,j],G[:,j],Gr[:,j],Ep[:,j],Fp[:,j],Gpp[:,j],higher)
            change[:,:,j],dchange[:,:,j],d2change[:,:,j]=c,d,dd
            worst_constraint=max(worst_constraint,err[0]);edge_error=max(edge_error,err[1])
        d2change=d2change*chi[:,None,None]+2*dchange*chip[:,None,None]+change*chipp[:,None,None]
        dchange=dchange*chi[:,None,None]+change*chip[:,None,None]
        change*=chi[:,None,None]
        old=gram(R,w,mode,deriv,2*order+12,.317,fundamental=fundamental)['metric']
        choices=[]
        for step in (1,.75,.5,.25,.125,.0625,.03125):
            new=gram(R,w,mode+step*change,deriv+step*dchange,2*order+12,.317,fundamental=fundamental)
            choices.append((new['metric'],step,new))
        value,step,obs=min(choices,key=lambda x:x[0])
        if value>=old:
            hist.append(dict(stopped=True,old=old,best=value))
            break
        mode+=step*change;deriv+=step*dchange;second+=step*d2change
        hist.append(dict(step=step,**obs,constraint=worst_constraint,edge_error=edge_error))
    # The remaining correction is defined between nodes by Hermite interpolation.
    return dict(start=start,hist=hist,outer_fixed=float(mode[-1,2,1]),inner_mode=float(mode[0,2,1])),mode-base_mode,deriv-base_deriv,second-base_second


def verify_grid(train, independent, delta, derivative, second=None, angle_count=71,fundamental=2):
    radius=train[:,3]
    r=independent[:,3]
    if r.min()<radius.min() or r.max()>radius.max():
        raise ValueError('independent domain extends outside the feedback field')
    if second is None:
        second=np.gradient(derivative,radius,axis=0,edge_order=2)
    second[0]=0.0  # The correction joins the original true infinite mean field inside.
    i=np.clip(np.searchsorted(radius,r,side='right')-1,0,len(radius)-2)
    h=(radius[i+1]-radius[i])[:,None,None]
    x=(r-radius[i])[:,None,None]/h
    a0,a1,a2=delta[i],h*derivative[i],h*h*second[i]/2
    d0=delta[i+1]-a0-a1-a2
    d1=h*derivative[i+1]-a1-2*a2
    d2=h*h*second[i+1]-2*a2
    a3,a4,a5=10*d0-4*d1+d2/2,-15*d0+7*d1-d2,6*d0-3*d1+d2/2
    c=((((a5*x+a4)*x+a3)*x+a2)*x+a1)*x+a0
    d=((((5*a5*x+4*a4)*x+3*a3)*x+2*a2)*x+a1)/h
    c[:,0,0]+=independent[:,12]
    d[:,0,0]+=independent[:,13]
    d[:,2,0]+=independent[:,15]
    # A radial axis height constant never enters the first fundamental form.
    c[:,0,1]+=independent[:,9];d[:,0,1]+=independent[:,10]
    c[:,1,1]-=independent[:,9]/fundamental;d[:,1,1]-=independent[:,10]/fundamental
    c[:,2,1]+=independent[:,6];d[:,2,1]+=independent[:,7]
    return gram(r,independent[:,4],c,d,angle_count,.417,fundamental=fundamental)


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('data');ap.add_argument('out');ap.add_argument('--steps',type=int,default=8);ap.add_argument('--order',type=int,default=8)
    ap.add_argument('--verify');ap.add_argument('--verify-only',action='store_true')
    ap.add_argument('--midpoint',action='store_true')
    a=ap.parse_args()
    d=json.loads(Path(a.data).read_text());nodes=np.asarray(d['rows'])
    if a.verify_only:
        old=np.load(a.out)
        z,v=old['delta'],old['derivative']
        dd=old['second'] if 'second' in old else None
        result={}
    else:
        result,z,v,dd=feedback(nodes,d['normalizedEpsilon'],a.steps,a.order,higher=not a.midpoint,fundamental=d.get('fundamental',2))
        np.savez_compressed(a.out,delta=z,derivative=v,second=dd)
    if a.verify:
        ind=np.asarray(json.loads(Path(a.verify).read_text())['rows'])
        result['independent']=verify_grid(nodes,ind,z,v,dd,fundamental=d.get('fundamental',2))
    print(json.dumps(result,indent=2))
