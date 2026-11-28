"""Actual fixed-metric coframe, its first curl, and simultaneous polar/shape steps."""
import numpy as np
from scipy.linalg import cho_factor,cho_solve
from bent_shared_rim_phase import pair_list

def dot(a,b):
    return np.sum(a*b,axis=-1)

class Reference:
    def __init__(self,F):
        fs,fv=F[:,1],F[:,2];self.F=F
        aa=np.sqrt(dot(fs,fs));bb=dot(fs,fv)/aa
        cc=np.sqrt(np.maximum(dot(fv,fv)-bb**2,1.e-28))
        self.a,self.b,self.c=aa,bb,cc
        self.W=np.zeros((len(F),2,2));self.W[:,0,0]=1/aa
        self.W[:,0,1]=-bb/(aa*cc);self.W[:,1,1]=1/cc
        self.dW=[];self.dabc=[]
        for i,j in ((3,4),(4,5)):
            da=dot(fs,F[:,i])/aa
            db=(dot(F[:,i],fv)+dot(fs,F[:,j])-bb*da)/aa
            dc=(dot(fv,F[:,j])-bb*db)/cc
            W=np.zeros_like(self.W);W[:,0,0]=-da/aa**2;W[:,1,1]=-dc/cc**2
            W[:,0,1]=-db/(aa*cc)+bb*(da/aa+dc/cc)/(aa*cc)
            self.dW.append(W);self.dabc.append((da,db,dc))
        jw=F[:,1:3].transpose(0,2,1)@self.W
        self.U0=jw
        dual=jw@self.W.transpose(0,2,1)
        # Each q_ij removes the fixed initial Christoffel tangent solution.
        h=np.zeros((len(F),3,6))
        for k in range(3):
            h[:,k,3+k]=1.
            h[:,k,1:3]=-np.einsum("nc,nci->ni",F[:,3+k],dual)
        r=bb/aa;op=np.zeros((len(F),6,6));op[:,0,0]=1.
        op[:,1,1]=1/aa;op[:,2,1]=-r/cc;op[:,2,2]=1/cc
        op[:,3]=h[:,0]/aa[:,None]**2
        op[:,4]=np.sqrt(2.)*(h[:,1]-r[:,None]*h[:,0])/(aa*cc)[:,None]
        op[:,5]=(h[:,2]-2*r[:,None]*h[:,1]+r[:,None]**2*h[:,0])/cc[:,None]**2
        self.op=op
    def rows(self,F):return self.op@F

def polar(Z):
    u,sv,vt=np.linalg.svd(Z,full_matrices=False);Q=u@vt
    H=(vt.transpose(0,2,1)*sv[:,None,:])@vt
    inv=(vt.transpose(0,2,1)/np.maximum(sv,1.e-13)[:,None,:])@vt
    return Q,sv,H,inv

def projection_report(F,ref):
    A=F[:,1:3].transpose(0,2,1);Q,sv,H,Hi=polar(A@ref.W)
    norm=np.cross(Q[:,:,0],Q[:,:,1])
    def dq(i,j,axis):
        dA=F[:,[i,j]].transpose(0,2,1)@ref.W+A@ref.dW[axis]
        K=Q.transpose(0,2,1)@dA
        skew=(K-K.transpose(0,2,1))/np.maximum(np.trace(H,axis1=1,axis2=2),1.e-14)[:,None,None]
        return (dA-Q@K)@Hi+Q@skew
    Qs=dq(3,4,0);Qv=dq(4,5,1)
    q1,q2=Q[:,:,0],Q[:,:,1]
    a,b,c=ref.a,ref.b,ref.c;_,bs,cs=ref.dabc[0];av=ref.dabc[1][0]
    cur=(bs-av)[:,None]*q1+cs[:,None]*q2+b[:,None]*Qs[:,:,0]+c[:,None]*Qs[:,:,1]-a[:,None]*Qv[:,:,0]
    curl=np.linalg.norm(cur,axis=1)/(a*c)
    reliable=sv[:,-1]>1.e-12
    curl=np.where(reliable,curl,0.)
    U=ref.U0;U3=np.concatenate((U,np.cross(U[:,:,0],U[:,:,1])[:,:,None]),axis=2)
    Q3=np.concatenate((Q,norm[:,:,None]),axis=2);R=Q3@U3.transpose(0,2,1)
    return np.linalg.norm(sv-1,axis=1),curl,R,reliable,sv

def pair_move(F,pairs,r,locked):
    a,b=pairs.T
    n=np.cross(F[a,1],F[a,2]);n/=np.maximum(np.linalg.norm(n,axis=1),1.e-14)[:,None]
    d=F[b,0]-F[a,0];sg=np.where(dot(d,n)>=0.,1.,-1.)
    w=d-sg[:,None]*r*n;l=np.linalg.norm(w,axis=1)
    act=(l<r)&((~locked[a])|(~locked[b]));ii=np.flatnonzero(act)
    move=np.zeros((len(F),3));count=np.zeros(len(F))
    if len(ii):
        aa,bb=a[ii],b[ii];rr=w[ii]/np.maximum(l[ii],1.e-14)[:,None]
        rr=np.where((l[ii]>1.e-14)[:,None],rr,-sg[ii,None]*n[ii])
        correction=(r-l[ii])[:,None]*rr;nu=(~locked[aa]).astype(int)+(~locked[bb]).astype(int)
        for idx,sign in ((aa,-1),(bb,1)):
            use=~locked[idx]
            np.add.at(move,idx[use],sign*correction[use]/nu[use,None])
            np.add.at(count,idx[use],1)
    return move/np.maximum(count,1.)[:,None],int(len(ii))

def targets(F,ref,cfg,locked):
    y=ref.rows(F);Q,sv,H,Hi=polar(y[:,1:3].transpose(0,2,1))
    n=np.cross(Q[:,:,0],Q[:,:,1]);k=np.empty((len(y),2,2))
    k[:,0,0]=dot(n,y[:,3]);k[:,0,1]=k[:,1,0]=dot(n,y[:,4])/np.sqrt(2)
    k[:,1,1]=dot(n,y[:,5]);kv,V=np.linalg.eigh(k)
    clip=np.clip(kv,-cfg["curvature_cap"],cfg["curvature_cap"])
    k=(V*clip[:,None,:])@V.transpose(0,2,1)
    delta=np.empty_like(y);delta[:,1:3]=Q.transpose(0,2,1)-y[:,1:3]
    delta[:,3]=k[:,0,0,None]*n-y[:,3]
    delta[:,4]=np.sqrt(2.)*k[:,0,1,None]*n-y[:,4];delta[:,5]=k[:,1,1,None]*n-y[:,5]
    pp,pr=pair_list(F,None,cfg["pair_count"])
    delta[:,0],hits=pair_move(F,pp,cfg["tube_radius"],locked)
    dist=np.linalg.norm(sv-1.,axis=1)
    atoms=np.sum(delta**2,axis=2)
    out={"polar_peak":float(dist.max()),"minimum_stretch":float(sv[:,-1].min()),
         "fixed_covariant_bending_peak":float(abs(kv).max()),"maximum_scanned_inverse":pr["max_inverse"],
         "sample_ball_halfspaces_active":hits}
    return delta,dist,atoms,out

class System:
    def __init__(self,M,ref,cfg,focus):
        self.M=M;self.ref=ref;m=M.mesh
        w=m.weight**2;self.locked=m.lab=="cylinder"
        for key,u,v,sl in m.cases:
            if key.startswith("end"):w[sl]*=1+cfg["rim_weight"]*(v>=.96*m.delay.END_LENGTH)
            elif key in ("cap+","cap-"):w[sl]*=1+cfg["rim_weight"]*(v>=.96)
        if focus is not None:
            # Symmetric common spatial weights permit exactly one spatial
            # least-squares operator for the true plus/minus physical components.
            by={key:sl for key,u,v,sl in m.cases}
            for name in ("end","cap","cap-cartesian"):
                a=by[name+"+"];b=by[name+"-"];v=np.maximum(focus[a],focus[b])
                p=max(.015,float(np.quantile(v,.85)))
                w[a]*=1+np.minimum(v/p,8.)**2;w[b]*=1+np.minimum(v/p,8.)**2
        self.ow=w/w.sum();self.rw=np.array([cfg["pair_position_weight"],1.,1.,
                 cfg["covariant_weight"],cfg["covariant_weight"],cfg["covariant_weight"]])
        self.blocks=list(M.blocks());H=np.zeros((M.width,M.width))
        for name,sl,ids,B,D in self.blocks:
            if name.endswith("-"):continue
            h=np.zeros((len(ids),len(ids)))
            for a,b,bb in self.chunks(sl,B,D):
                ww=self.ow[a:b,None]*self.rw[None,:]
                mat=(bb*np.sqrt(ww)[:,:,None]).reshape(-1,len(ids))
                h+=mat.T@mat
            H[np.ix_(ids,ids)]+=h
        self.diag=np.sqrt(np.maximum(np.diag(H),1.e-15))
        H=H/self.diag[:,None]/self.diag[None,:]
        H.flat[::1+M.width]+=cfg["shape_damping"]
        self.H=cho_factor((H+H.T)*.5,lower=True,check_finite=False)
    def chunks(self,sl,B,D):
        for i in range(0,B.shape[1],224):
            j=min(B.shape[1],i+224);a,b=sl.start+i,sl.start+j
            raw=np.concatenate((B[:,i:j,:],D[:,i:j,:]),axis=2).transpose(1,0,2)
            yield a,b,self.ref.op[a:b]@raw
    def rhs(self,residual):
        weighted=(self.ow[:,None]*self.rw[None,:])[:,:,None]*residual
        force=self.ref.op.transpose(0,2,1)@weighted
        return self.M.adj(force).reshape(2,self.M.width,3)
    def change(self,A,h):
        # Product time-space normal equations with one coefficient vector at
        # each strictly positive phase node. Time zero is identically anchored.
        wt=np.ones(len(A));wt[-1]=.5;T=A.T@(wt[:,None]*A)
        raw=np.einsum("kn,n,nabc->kabc",A.T,wt,h)
        y=np.linalg.solve(T,raw.reshape(len(T),-1)).reshape(raw.shape)
        out=np.zeros_like(y)
        for side in range(2):
            r=y[:,side].transpose(1,0,2).reshape(len(self.diag),-1)/self.diag[:,None]
            x=cho_solve(self.H,r,check_finite=False)/self.diag[:,None]
            out[:,side]=x.reshape(len(self.diag),len(T),3).transpose(1,0,2)
        return out.reshape(len(T),-1)
    def score(self,atoms):return float(np.sum(self.ow[:,None]*self.rw[None,:]*atoms))
