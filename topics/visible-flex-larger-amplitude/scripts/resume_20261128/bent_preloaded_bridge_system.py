"""Analytic fixed-target Gram, immersion and genuine normal-curvature linearizations for R770."""
import numpy as np
from scipy.sparse.linalg import LinearOperator,cg
from scipy.interpolate import CubicSpline

def clock(nodes,times):
    if len(nodes)==1:return np.zeros((len(times),0))
    return CubicSpline(nodes,np.eye(len(nodes)),axis=0,bc_type=("natural",(1,np.zeros(len(nodes)))))(times)[:,1:]

def geometry(f):
    a,b=f[:,1],f[:,2];A=np.linalg.norm(a,axis=1)
    t=a/A[:,None];v=np.einsum("ij,ij->i",t,b);per=b-t*v[:,None]
    B=np.linalg.norm(per,axis=1);n=np.cross(t,per/B[:,None])
    # coordinate columns giving an orthonormal material basis
    C=np.zeros((len(f),2,2));C[:,0,0]=1/A;C[:,1,1]=1/B;C[:,0,1]=-v/(A*B)
    return C,n

def transformed(f,C):
    a=C[:,0,0,None];b=C[:,0,1,None];c=C[:,1,1,None]
    return np.stack((f[:,0],a*f[:,1],b*f[:,1]+c*f[:,2],a*a*f[:,3],
                     a*b*f[:,3]+a*c*f[:,4],b*b*f[:,3]+2*b*c*f[:,4]+c*c*f[:,5]),axis=1)

def fixed(f,B):
    C,n=geometry(f);return transformed(f,C),transformed(B,C),C

def dot(a,b):return np.einsum("ij,ij->i",a,b)

def residual(F,B,w,par,linear=True):
    npts,_,k=B.shape;one=np.ones(npts);a,b=F[:,1],F[:,2];P,Q=B[:,1],B[:,2]
    ncr=np.cross(a,b);area=np.linalg.norm(ncr,axis=1)
    nn=ncr/np.maximum(area,1.e-14)[:,None];ab=dot(a,b)
    aa=dot(a,a);bb=dot(b,b);r=[];jac=[]
    def add(value,j,wgt):
        weight=w*wgt;r.append(value*weight)
        if linear:jac.append(j*weight[:,None,None])
    if linear:
        ja=2*P[:,:,None]*a[:,None,:];jb=2*Q[:,:,None]*b[:,None,:]
        jab=P[:,:,None]*b[:,None,:]+Q[:,:,None]*a[:,None,:]
    else:ja=jb=jab=None
    add(aa-1,ja,1.);add(ab,jab,2**.5);add(bb-1,jb,1.)
    # Relative area barrier. delta |a cross b|=delta a.(b cross n)+delta b.(n cross a).
    dm=np.maximum(par["area_floor"]-area,0)
    jj=None
    if linear:
        jj=-(P[:,:,None]*np.cross(b,nn)[:,None,:]+Q[:,:,None]*np.cross(nn,a)[:,None,:])*(dm>0)[:,None,None]
    add(dm,jj,par["area_weight"])
    worst=np.zeros(npts)
    for co,si in ((1.,0.),(0.,1.),(2**-.5,2**-.5),(2**-.5,-2**-.5)):
        v=co*a+si*b;vv=dot(v,v)
        H=co*co*F[:,3]+2*co*si*F[:,4]+si*si*F[:,5]
        h=dot(nn,H);active=np.maximum(abs(h)-par["curvature_bound"]*vv,0.)
        worst=np.maximum(worst,abs(h)/np.maximum(vv,1.e-15))
        j=None
        if linear:
            hp=(H-h[:,None]*nn)/np.maximum(area[:,None],1.e-14)
            # delta n.H = delta a.(b cross Hperp)/area + delta b.(Hperp cross a)/area.
            ah=np.cross(b,hp);bh=np.cross(hp,a)
            BH=co*co*B[:,3]+2*co*si*B[:,4]+si*si*B[:,5]
            hj=P[:,:,None]*ah[:,None,:]+Q[:,:,None]*bh[:,None,:]+BH[:,:,None]*nn[:,None,:]
            j=np.sign(h)[:,None,None]*hj-2*par["curvature_bound"]*(co*P+si*Q)[:,:,None]*v[:,None,:]
            j*=(active>0)[:,None,None]
        add(active,j,par["curvature_weight"])
    e=.5*(aa+bb)-1;d=np.hypot(.5*(aa-bb),ab);op=np.maximum(abs(e+d),abs(e-d))
    return np.concatenate(r),(np.concatenate(jac,axis=0).reshape(-1,3*k) if linear else None),op,area,worst

def stats(F):
    a,b=F[:,1],F[:,2];normal=np.cross(a,b);ar=np.linalg.norm(normal,axis=1)
    n=normal/np.maximum(ar[:,None],1.e-15)
    aa,bb,ab=dot(a,a),dot(b,b),dot(a,b);E=.5*(aa+bb)-1;D=np.hypot(.5*(aa-bb),ab)
    op=np.maximum(abs(E+D),abs(E-D));coef=ar**2
    h,j,k=dot(n,F[:,3]),dot(n,F[:,4]),dot(n,F[:,5])
    mean=(bb*h+aa*k-2*ab*j)/(2*np.maximum(coef,1.e-30));gauss=(h*k-j*j)/np.maximum(coef,1.e-30)
    rr=np.sqrt(np.maximum(0.,mean*mean-gauss))
    pk=np.maximum(abs(mean-rr),abs(mean+rr))
    return op,pk,ar

def shape_step(tables,base,W,Z,par):
    # One frozen side per call. All positive time knots enter the common Gauss-Newton system.
    K=len(Z[0].ravel());nt=len(Z);H=[];g=[];value=0.;ill=0.
    for ib,(phase,rows) in enumerate(base):
        c=np.tensordot(W[ib],Z,axes=1);HH=np.zeros((K,K));gg=np.zeros(K)
        for (B,w),F0 in zip(tables,rows):
            F=F0+B@c
            for start in range(0,len(F),par["jac_chunk"]):
                sl=slice(start,start+par["jac_chunk"])
                r,J,op,ar,pk=residual(F[sl],B[sl],w[sl],par)
                HH+=J.T@J;gg+=J.T@r
                value+=r@r;ill=max(ill,float(op.max()))
        H.append(HH);g.append(gg)
    H=np.array(H);g=np.array(g);G=W.T@g
    diag=np.einsum("tp,ti->pi",W*W,np.diagonal(H,axis1=1,axis2=2))
    reg=par["damping"]*np.maximum(np.mean(diag),1.e-7)
    def mul(x):
        z=W@x.reshape(nt,K)
        return (W.T@np.einsum("tij,tj->ti",H,z)+reg*x.reshape(nt,K)).ravel()
    A=LinearOperator((nt*K,nt*K),matvec=mul)
    M=LinearOperator(A.shape,matvec=lambda x:x/(diag.ravel()+reg))
    its=[0]
    def count(_):its[0]+=1
    step,info=cg(A,-G.ravel(),M=M,rtol=par["cg_tol"],atol=0.,maxiter=par["cg_max"],callback=count)
    out=step.reshape(Z.shape)
    # Bound actual Euclidean displacement of every training point at every phase.
    move=0.;slope=0.
    for i,(_,rows) in enumerate(base):
        dx=np.tensordot(W[i],out,axes=1)
        for B,w in tables:
            d=B@dx
            move=max(move,float(np.linalg.norm(d[:,0],axis=-1).max()))
            slope=max(slope,float(np.linalg.norm(d[:,1:3],axis=-1).max()))
    fac=min(1.,par["step_displacement"]/max(move,1.e-15),par["step_tangent"]/max(slope,1.e-15))
    return fac*out,dict(current_objective=float(value),raw_max_gram=ill,cg_status=int(info),
           cg_iterations=its[0],raw_update_norm=float(np.linalg.norm(out)),raw_physical_move=move,
           raw_orthonormal_tangent_move=slope,trust_factor=fac)

def objective(tables,base,W,Z,par):
    val=0.;peak=0.
    for i,(_,rows) in enumerate(base):
        c=np.tensordot(W[i],Z,axes=1)
        for (B,w),f0 in zip(tables,rows):
            r,_,op,_,_=residual(f0+B@c,B,w,par,False)
            val+=r@r;peak=max(peak,float(op.max()))
    return float(val),peak
