"""Ambient polynomial material fields on all actual charts of a closed embedded body."""
import numpy as np
from numpy.polynomial.chebyshev import chebvander
from scipy.sparse.linalg import LinearOperator,lsmr
from bent_body_atlas import dot

def Cheb(x,degree):
    v=chebvander(x,degree);d=np.zeros_like(v);dd=np.zeros_like(v)
    if degree:d[:,1]=1
    for n in range(2,degree+1):
        d[:,n]=2*v[:,n-1]+2*x*d[:,n-1]-d[:,n-2]
        dd[:,n]=4*d[:,n-1]+2*x*dd[:,n-1]-dd[:,n-2]
    return v,d,dd

class Basis:
    """The same frozen reference coordinates are used when physical coefficients vary."""
    def __init__(self,m,degree,physical,scale):
        self.degree=degree;self.physical=physical
        f=m.f/np.asarray(scale);N=len(f);nj=6 if physical else 3
        self.powers=[];self.fields=[];self.names=[];self.slices=[]
        c=m.chi;tabs=[Cheb(f[:,0,i],degree) for i in range(3)]
        start=0
        for comp in range(3):
            powr=[(i,j,k) for i in range(degree+1) for j in range(degree+1-i)
                  for k in range(degree+1-i-j) if (j%2)==((comp==1) if physical else (comp!=1)) and k%2==(comp==2)]
            self.powers.append(powr);B=np.empty((nj,N,len(powr)))
            for n,p in enumerate(powr):
                def value(J):
                    return tabs[0][J[0]][:,p[0]]*tabs[1][J[1]][:,p[1]]*tabs[2][J[2]][:,p[2]]
                g=value((0,0,0))
                dg=np.column_stack([value(tuple(int(j==i) for j in range(3))) for i in range(3)])
                gs=dot(dg,f[:,1]);ga=dot(dg,f[:,2])
                B[0,:,n]=c[:,0]*g
                B[1,:,n]=c[:,1]*g+c[:,0]*gs;B[2,:,n]=c[:,2]*g+c[:,0]*ga
                if physical:
                    hess=np.empty((N,3,3))
                    for i in range(3):
                        for j in range(i,3):
                            H=value(tuple(int(k==i)+int(k==j) for k in range(3)))
                            hess[:,i,j]=H;hess[:,j,i]=H
                    for k,(a,b) in enumerate(((1,1),(1,2),(2,2)),3):
                        second=dot(dg,f[:,k])+np.einsum("ni,nij,nj->n",f[:,a],hess,f[:,b])
                        B[k,:,n]=c[:,k]*g+c[:,a]*(ga if b==2 else gs)+c[:,b]*(ga if a==2 else gs)+c[:,0]*second
            self.fields.append(B);self.names.extend((comp,)+p for p in powr)
            self.slices.append(slice(start,start+len(powr)));start+=len(powr)
        self.n=start
    def values(self,z):
        return np.stack([(b@z[s]).T for b,s in zip(self.fields,self.slices)],axis=-1)
    def adjoint(self,v):
        return np.concatenate([b.reshape(-1,b.shape[-1]).T@np.ascontiguousarray(v[...,i].T).ravel()
                               for i,b in enumerate(self.fields)])
    def transfer(self,prior,z):
        old=dict(zip(prior.names,z))
        return np.array([old.get(k,0.) for k in self.names])

def safe(x,floor):
    return np.where(x.real>floor,x,floor)

def calc(f,extra,x0,sign,p,reference=None):
    pt,u,v,uu,uv,vv=np.moveaxis(f,1,0)
    A,As,At=np.moveaxis(extra,1,0)
    vel,vs,vt=np.moveaxis(x0,1,0)
    E,F,G=dot(u,u),dot(u,v),dot(v,v)
    C=np.cross(u,v)*sign[:,None];area=np.sqrt(safe(dot(C,C),1e-28));n=C/area[:,None]
    def prod(c,v):return c[:,None]*v
    ys=prod(vel[:,0],uu)+prod(vel[:,1],uv)+prod(vs[:,0],u)+prod(vs[:,1],v)
    yt=prod(vel[:,0],uv)+prod(vel[:,1],vv)+prod(vt[:,0],u)+prod(vt[:,1],v)
    l,mm,h=[dot(n,vv1) for vv1 in (uu,uv,vv)]
    coef=2*dot(A,n)
    K=(2*dot(u,ys+As)+coef*l,dot(u,yt+At)+dot(v,ys+As)+coef*mm,2*dot(v,yt+At)+coef*h)
    II=(l,mm,h)
    def whiten(t,g):
        e,f,h=g;g2=safe(h,1e-14);q=f/g2;m=safe(e-f*q,1e-14)
        a,b,c=t
        return np.column_stack([(a-2*q*b+q*q*c)/m,np.sqrt(2)*(b-q*c)/np.sqrt(m*g2),c/g2])
    W=whiten(K,(E,F,G));B=whiten(II,(E,F,G))
    half=(B[:,0]+B[:,2])/2
    rad=np.sqrt((.5*(B[:,0]-B[:,2]))**2+.5*B[:,1]**2+1.e-20)
    bend=np.sqrt(half**2+1.e-20)+rad
    sup=dot(pt,n)
    result={"K":W,"bend":bend,"support":sup,"metric":(E,F,G),"area":area}
    if reference is not None:
        result["relative"]=whiten((E-reference[0],F-reference[1],G-reference[2]),reference)
    return result

def opnorm(v):
    return abs((v[:,0]+v[:,2])/2)+np.sqrt(((v[:,0]-v[:,2])/2)**2+.5*v[:,1]**2)

def extrem(m,v,high=True):
    i=int(np.argmax(v) if high else np.argmin(v))
    return {"value":float(v[i]),**m.point(i)}

def fixed_vector(m,f,basis,p,iters):
    # Compile the local 3x9 relative strain operator of the material
    # displacement from its values and first derivatives in this chart.
    z0=np.zeros((len(f),3,3));raw=calc(f,z0,m.X0,m.sign,p)["K"]
    # Global mask and its derivatives are already included in the dictionary.
    coeff=np.empty((len(f),3,3,3))
    for j in range(3):
        for i in range(3):
            zz=z0.copy();zz[:,j,i]=1.
            coeff[:,:,j,i]=calc(f,zz,m.X0,m.sign,p)["K"]-raw
    weight=m.weight;reg=p["vector_regularizer"]
    # Dense linear problem in the physical dictionary. Columns are assembled
    # in their true chart frames, then weighted identically across resolutions.
    cols=[]
    for i,B in enumerate(basis.fields):
        cols.append(np.einsum("nrj,jnk->nrk",coeff[:,:,:,i],B,optimize=True))
    J=np.concatenate(cols,axis=-1)
    J=(J*weight[:,None,None]).reshape(-1,basis.n)
    y=-(raw*weight[:,None]).ravel()
    baseJ=J;basey=y;extra_weight=np.ones(len(f));history=[];point=np.zeros(basis.n)
    for power in p["material_reweightings"]:
        rw=np.repeat(extra_weight,3)
        J=baseJ*rw[:,None];y=basey*rw
        scale=np.maximum(np.sqrt(np.sum(J**2,axis=0)+reg*reg),1e-12)
        Js=J/scale
        def mv(a):a=a.ravel();return np.r_[Js@a,reg*a/scale]
        def rm(v):v=v.ravel();return Js.T@v[:len(y)]+reg*v[len(y):]/scale
        op=LinearOperator((len(y)+basis.n,basis.n),matvec=mv,rmatvec=rm,dtype=float)
        sol=lsmr(op,np.r_[y,np.zeros(basis.n)],x0=point*scale,maxiter=iters,atol=2e-10,btol=2e-10)
        point=sol[0]/scale
        rr=opnorm(((baseJ@point-basey).reshape(-1,3))/weight[:,None])
        history.append({"iterations":int(sol[2]),"code":int(sol[1]),"residual":float(sol[3]),
                    "normal_residual":float(sol[4]),"condition_estimate":float(sol[6]),"max_current_op":float(rr.max())})
        denom=max(float(np.quantile(rr,.90)),.0001)
        extra_weight=np.sqrt(1.+np.minimum((rr/denom)**power,16.))
    return point,{"passes":history}

def material_velocity(f,ext,x0):
    """True chart components for F_* X = F_*X0 + orthogonal_projection(A)."""
    u,v=f[:,1],f[:,2];e,ff,g=dot(u,u),dot(u,v),dot(v,v)
    bu,bv=dot(u,ext[:,0]),dot(v,ext[:,0]);det=e*g-ff*ff
    if np.any(det<=0.):raise ValueError("irregular physical chart in material flow")
    return x0[:,0]+np.column_stack([(g*bu-ff*bv)/det,(e*bv-ff*bu)/det])

def physical_res(f,m,ext,p,reference,base,stage):
    c=calc(f,ext,m.X0,m.sign,p,reference); e0,f0,g0=base
    E,F,G=c["metric"];target=c.get("relative")
    row=[p["lie_weight"]*np.arcsinh(c["K"]/p["strain_softness"])*p["strain_softness"]]
    def plus(q):return np.where(q.real>0.,q,0.)
    def col(q):return q[:,None]
    if target is not None:row.append(stage["metric_weight"]*target)
    # With the actual current metric in both the Lie and curvature rows,
    # a shrinking first form cannot mask relative strain.
    q=f0/safe(g0,1e-14);eb=safe(e0-f0*q,1e-14)
    a=(E-2*q*F+q*q*G)/eb;b=(F-q*G)/np.sqrt(eb*g0);d=G/g0
    half=(a+d)/2;rad=np.sqrt(((a-d)/2)**2+b*b+1e-22)
    row.append(col(p["bilipschitz_weight"]*plus(p["metric_floor"]-half+rad)))
    row.append(col(p["bilipschitz_weight"]*plus(half+rad-p["metric_ceiling"])))
    row.append(col(p["bend_weight"]*plus(c["bend"]/p["bend_cap"]-1.)))
    row.append(col(p["support_weight"]*plus(p["support_goal"]-c["support"])))
    dif=f[:,0]-m.f[:,0]
    ds=np.sqrt(dot(dif,dif)+1e-20)
    row.append(col(p["displace_weight"]*plus(ds-p["displace_cap"])))
    return np.concatenate(row,axis=1)

class Shape:
    def __init__(self,m,basis,ext,p,stage,target):
        self.m=m;self.b=basis;self.ext=ext;self.p=p;self.st=stage;self.target=target
        self.base=calc(m.f,ext,m.X0,m.sign,p)["metric"];self.last=None
    def prepare(self,z):
        if self.last is not None and np.array_equal(self.last,z):return
        self.last=z.copy();self.f=self.m.f+self.b.values(z)
        self.r=physical_res(self.f,self.m,self.ext,self.p,self.target,self.base,self.st)
    def fun(self,z):
        self.prepare(z)
        return np.r_[(self.r*self.m.weight[:,None]).ravel(),self.st["regularizer"]*z]
    def jac(self,z):
        self.prepare(z);m=self.m;reg=self.st["regularizer"]
        # Each row uses only the point's six independent physical jets.
        # Complex-step differentiates all current Gram normalizers, projected
        # ambient vectors and curvatures; active inequalities use the real mask.
        g=np.empty((len(m.f),self.r.shape[1],6,3))
        h=1.e-27
        fc=self.f.astype(complex)
        for j in range(6):
            for i in range(3):
                fc[:,j,i]+=1j*h
                g[:,:,j,i]=physical_res(fc,m,self.ext,self.p,self.target,self.base,self.st).imag/h
                fc[:,j,i]-=1j*h
        # The current small dense Jacobian is faster than evaluating a
        # Cartesian polynomial field in every inner LSMR iteration.
        mat=np.concatenate([np.einsum("nrj,jnk->nrk",g[:,:,:,i],B,optimize=True)
                            for i,B in enumerate(self.b.fields)],axis=-1)
        mat=(mat*m.weight[:,None,None]).reshape(-1,self.b.n)
        def mv(v):v=v.ravel();return np.r_[mat@v,reg*v]
        def rm(v):v=v.ravel();return mat.T@v[:-self.b.n]+reg*v[-self.b.n:]
        return LinearOperator((mat.shape[0]+self.b.n,self.b.n),matvec=mv,rmatvec=rm,dtype=float)
