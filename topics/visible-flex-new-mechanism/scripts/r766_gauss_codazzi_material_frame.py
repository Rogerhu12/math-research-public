"""True R764 material Gauss--Codazzi variables and native differentiated SO(3) radial development."""
import numpy as np
from scipy.interpolate import BSpline
from r738_negative_tail_and_macro_source import A0, B0, THETA
from r758_material_jet_and_angles import J
from r764_positive_slope_material import material

REACH_GERM=(.085,.21)


def knots(spans):
    # All earlier knots are retained by every registered refinement.
    return np.r_[[A0]*3,np.unique(np.r_[np.linspace(A0,B0,spans+1),.085,.21]),[B0]*3]

class Space:
    def __init__(self,stage):
        self.K=stage['K'];self.spans=stage['spans'];self.knots=knots(self.spans)
        self.splines=len(self.knots)-4;self.tail=int(stage['log_pairs']);self.radial=self.splines+4*self.tail
        self.size=3+2*self.radial*(2*self.K+1)
    def coefficients(self,x):return np.asarray(x[3:]).reshape(2,self.radial,2*self.K+1)
    def prolong(self,old,x):
        if self.K<old.K or self.tail<old.tail:raise ValueError('The entire prior space is required.')
        previous=old.coefficients(x);out=np.zeros((2,self.radial,2*self.K+1));ns=2*old.K+1
        for i in range(2):
            s=BSpline(old.knots,previous[i,:old.splines],3,axis=0)
            for knot in np.setdiff1d(self.knots,old.knots):s=s.insert_knot(knot)
            if not np.array_equal(s.t,self.knots):raise ValueError('Nested source spline knots differ.')
            out[i,:self.splines,:ns]=s.c
            out[i,self.splines:self.splines+old.tail*4,:ns]=previous[i,old.splines:]
        return np.r_[x[:3],out.ravel()]
    def radial_basis(self,r):
        s=BSpline(self.knots,np.eye(self.splines),3,axis=0)
        val=[s(r)];der=[s(r,nu=1)]
        # At every positive distance there are live logarithmic cells right to each material cap.
        # t^3(1-t)^5 gives a C2 zero extension at both ends; each pair is uniformly bounded by 1.
        for k in range(1,self.tail+1):
            for side,rim in ((1,A0),(-1,B0)):
                z=side*(r-rim)/.01;ok=(z>0)&(z<1);t=np.where(ok,z,1.)
                arg=2*np.pi*k*np.log2(t);scale=32.
                amp=scale*t**3*(1-t)**5
                da=scale*(3*t**2*(1-t)**5-5*t**3*(1-t)**4);dp=2*np.pi*k/(np.log(2.)*t)
                for w,dw in ((np.cos(arg),-np.sin(arg)),(np.sin(arg),np.cos(arg))):
                    val.append(np.where(ok,amp*w,0.)[:,None]);der.append(np.where(ok,side*(da*w+amp*dw*dp)/.01,0.)[:,None])
        return np.concatenate(val,axis=1),np.concatenate(der,axis=1)

def modes(phi,K):
    angle=phi[:,None]*np.arange(1,K+1)[None,:];j=np.arange(1,K+1)[None,:]
    arr=[]
    for k in range(3):
        base=np.ones(len(phi)) if k==0 else np.zeros(len(phi))
        arr.append(np.column_stack((base,np.stack((np.cos(angle+k*np.pi/2)*j**k,np.sin(angle+k*np.pi/2)*j**k),axis=-1).reshape(len(phi),2*K))))
    return arr

def prod(p,q):return (p[0]*q[0],p[1]*q[0]+p[0]*q[1],p[2]*q[0]+2*p[1]*q[1]+p[0]*q[2])
def mul(p,b):return tuple(v*b for v in p)
def plus(p,q):return tuple(x+y for x,y in zip(p,q))
def expo(p):
    e=np.exp(p[0]);return e,e*p[1],e*(p[2]+p[1]**2)

def radius_source(base,r):
    material_data=material(base,r);W,Wp=material_data['W'],material_data['Wp']
    m=np.sqrt(1+W*W);mr=W*Wp/m;support=np.zeros_like(r);spr=np.zeros_like(r)
    for center in REACH_GERM:
        z=(r-center)/.0045;t=np.maximum(0.,1-z*z);support+=t**6;spr-=12*z*t**5/.0045
    kap=W/m+.013*support;kr=Wp/m**3+.013*spr
    # h'/k = -(W/(m*kappa))*W'/m² * exp(-u). On the actual deep interval
    # kappa=W/m, including the removable limit W=0 at the exact physical cap.
    quotient=np.ones_like(r);mask=support>0
    quotient[mask]=W[mask]/(m[mask]*kap[mask]);base.count['new_R766_true_radial_material_rows']+=len(r)
    return dict(m=m,mr=mr,kap=kap,kr=kr,quot=-quotient*Wp/m**2,E=material_data['E'],Ep=material_data['Ep'])

class Design:
    def __init__(self,sp,r,phi,base,book):
        import hashlib
        self.r=r;self.phi=phi
        key=hashlib.sha256(np.ascontiguousarray(r,dtype='<f8').tobytes()).hexdigest()
        angular_key=hashlib.sha256(np.ascontiguousarray(phi,dtype='<f8').tobytes()).hexdigest()
        self.b,self.d=book.once(f'gc_basis_{sp.spans}_{sp.tail}_'+key,'read',lambda:sp.radial_basis(r))
        self.angular=book.once(f'gc_modes_{sp.K}_'+angular_key,'read',lambda:modes(phi,sp.K))
        self.mat=book.once('gc_material_'+key,'read',lambda:radius_source(base,r))
    def field(self,sp,x):
        mat=self.mat;co=sp.coefficients(x);g=[];gr=[]
        for c in co:
            v=self.b@c;g.append(tuple(v@a.T for a in self.angular));gr.append(self.d@c@self.angular[0].T)
        u,v=g;ur,vr=gr
        if np.max(abs(u[0].real))>10 or np.max(abs(v[0].real))>12:raise FloatingPointError('Resolved positive-azimuthal-curvature chart left finite trial range.')
        m=mat['m'][:,None];b=m/self.r[:,None];e=expo(u);ei=expo(mul(u,-1))
        k=mul(e,mat['kap'][:,None]);ell=prod(k,v)
        a=plus(mul(prod(ell,v),b),mul(ei,-mat['quot'][:,None]))
        kr=e[0]*(mat['kr'][:,None]+mat['kap'][:,None]*ur);lr=kr*v[0]+k[0]*vr
        return dict(k=k,ell=ell,a=a,omega=(mul(ell,b),mul(a,-1)),
             gc=(kr-a[0]/m-b*ell[1],lr-a[1]+ell[0]/self.r[:,None]),
             literal_Gauss=(b*ell[0]**2-a[0]*k[0])+mat['mr'][:,None]/m**2)

def angular_mat(p,q):
    return (p[0]@q[0],p[1]@q[0]+p[0]@q[1],p[2]@q[0]+2*(p[1]@q[1])+p[0]@q[2])

def exp_pade(omega):
    aa,bb=omega;S=[]
    for x,y in zip(aa,bb):
        m=np.zeros(x.shape+(3,3),dtype=np.result_type(x,y));m[...,0,2]=y;m[...,1,2]=-x;m[...,2,0]=-y;m[...,2,1]=x;S.append(m)
    sq=angular_mat(S,S);D=[y/12-x/2 for x,y in zip(S,sq)];N=[y/12+x/2 for x,y in zip(S,sq)]
    D[0]=D[0]+np.eye(3);N[0]=N[0]+np.eye(3)
    # The [2/2] Padé transfer is a genuine rotation on the real skew algebra.
    # Solve all three phi-jet equations with the same nonsingular D0.
    inv=np.linalg.inv(D[0]);r=inv@N[0];dr=inv@(N[1]-D[1]@r)
    ddr=inv@(N[2]-D[2]@r-2*(D[1]@dr));return r,dr,ddr

def independent_prefix(blocks):
    """Pure associative scan in the true order of right-trivialized radial rotations."""
    n=len(blocks[0]);span=1;out=blocks
    while span<n:
        tail=angular_mat([q[:-span] for q in out],[q[span:] for q in out]);out=tuple(np.concatenate((q[:span],t)) for q,t in zip(out,tail));span*=2
    return out

def vec_to_jet(q,qr):
    out=[]
    for j in range(3):
        out.append(J.pack({(0,i):q[i][...,j]/(2 if i==2 else 1) for i in range(3)}|
                          {(1,i):qr[i][...,j]/(2 if i==2 else 1) for i in range(3)}))
    return tuple(out)

def stepnodes(r):
    # Physical integration proceeds from the outer true cap to the inner true cap.
    right=r[:0:-1];h=r[-2::-1]-right;cen=right+h/2
    return (cen-h/(2*np.sqrt(3)),cen+h/(2*np.sqrt(3))),h

class Frame:
    def __init__(self,sp,grid,phi,base,book,refine=1):
        self.grid,self.phi=grid,phi
        r=grid.r
        if refine==2:r=np.sort(np.r_[r,(r[1:]+r[:-1])/2]);self.indices=np.arange(0,len(r),2)
        else:self.indices=np.arange(len(r))
        self.r=r;self.original=Design(sp,r,phi,base,book)
        self.nodes,self.h=stepnodes(r)
        self.gauss=[Design(sp,rr,phi,base,book) for rr in self.nodes]
    def read(self,sp,x):
        va=self.original.field(sp,x);v1,v2=[g.field(sp,x)['omega'] for g in self.gauss]
        aa=(3+2*np.sqrt(3))/12;bb=.5-aa;h=self.h[:,None]
        def step(a,b):return exp_pade([mul(plus(mul(v,a),mul(w,b)),h) for v,w in zip(v1,v2)])
        s,t=step(aa,bb),step(bb,aa);out=independent_prefix(angular_mat(s,t));phi=self.phi
        s,c=np.sin(phi),np.cos(phi);outer=[np.zeros((len(phi),3,3)) for _ in range(3)]
        for i,(x0,y0) in enumerate(((c,s),(-s,c),(-c,-s))):
            outer[i][:,0,0]=x0;outer[i][:,1,0]=y0;outer[i][:,0,1]=-y0;outer[i][:,1,1]=x0
        outer[0][:,2,2]=1.;rot=angular_mat(outer,out)
        rot=tuple(np.concatenate((v[::-1],q[None]),axis=0) for v,q in zip(rot,outer))
        P,T,n=[tuple(v[...,j] for v in rot) for j in range(3)]
        def times(q,val):return prod(q,tuple(x[...,None] for x in val))
        av=va['a'];bl=va['omega'][0];pr=times(n,av);tr=times(n,bl)
        nr=mul(plus(times(P,av),times(T,bl)),-1)
        return dict(rotation=rot,rotation_slopes=tuple(np.stack((pr[k],tr[k],nr[k]),axis=-1) for k in range(3)),n=vec_to_jet(n,nr),P=vec_to_jet(P,pr),T=vec_to_jet(T,tr),shape=P[0].shape[:-1],
            gc=va['gc'],literal_Gauss=va['literal_Gauss'],k=va['k'][0],ell=va['ell'][0],a=av[0],
            actual_Xphi_errors=(P[1]-T[0]/self.original.mat['m'][:,None,None]-va['ell'][0][...,None]*n[0],
                       T[1]+P[0]/self.original.mat['m'][:,None,None]-va['k'][0][...,None]*n[0]))
