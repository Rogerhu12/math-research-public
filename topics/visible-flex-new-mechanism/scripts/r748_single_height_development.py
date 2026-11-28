"""R748 use one true periodic height, one radial development and both actual cap two-jets."""
from types import SimpleNamespace
import numpy as np
from numpy.polynomial import legendre as leg
from r726_closed_spinor_fourier import public


def add(x,y):
    return tuple(a+b for a,b in zip(x,y))


def neg(x):
    return tuple(-a for a in x)


def mul(x,y):
    a,b,c=x;d,e,f=y
    return a*d,b*d+a*e,c*d+2*b*e+a*f


def inv(x):
    a,b,c=x
    return 1/a,-b/a**2,2*b*b/a**3-c/a**2


def sqrt_jet(x):
    a,b,c=x
    if not np.all(np.isfinite(a)) or np.any(a.real<=0):raise FloatingPointError('Positive radial graph chart required.')
    f=np.sqrt(a)
    return f,b/(2*f),c/(2*f)-b*b/(4*f**3)


def scalar(x):
    return x,np.zeros_like(x),np.zeros_like(x)


def vector(x,y):
    return tuple(np.stack((a,b),axis=-1) for a,b in zip(x,y))


def rotate_vec(x):
    return np.stack((-x[...,1],x[...,0]),axis=-1)


def phase(t):
    a,b,c=t
    v=np.stack((np.cos(a),np.sin(a)),axis=-1);vp=rotate_vec(v)
    return v,vp*b[...,None],vp*c[...,None]-v*b[...,None]**2


def times(z,v):
    return mul(tuple(a[...,None] for a in z),v)


def cmul(z,w):
    return vector(add(mul(tuple(a[...,0] for a in z),tuple(b[...,0] for b in w)),
                      neg(mul(tuple(a[...,1] for a in z),tuple(b[...,1] for b in w)))),
                  add(mul(tuple(a[...,0] for a in z),tuple(b[...,1] for b in w)),
                      mul(tuple(a[...,1] for a in z),tuple(b[...,0] for b in w))))


def conjugate(z):
    # Real two-vector rotation, retaining any complex-step dependence on real design parameters.
    return tuple(np.stack((a[...,0],-a[...,1]),axis=-1) for a in z)


def constant_scale(v,c):
    return tuple(a*c for a in v)


class RadialGrid:
    def __init__(self,edges,order):
        public()
        self.edges=np.ascontiguousarray(edges,dtype=np.float64)
        if len(self.edges)<2 or self.edges[0]<=0 or not np.all(np.isfinite(self.edges)) or np.any(np.diff(self.edges)<=0) or not 2<=order<=32:
            raise ValueError('Strict physical intervals and Gauss order 2..32 required.')
        self.order=order
        x,self.w=leg.leggauss(order);t=np.r_[-1.,x,1.]
        V=leg.legvander(x,order-1)
        primitives=[]
        for j in range(order):
            coeff=np.zeros(order);coeff[j]=1.
            a=leg.legint(coeff)
            primitives.append(leg.legval(t,a)-leg.legval(1.,a))
        self.P=np.linalg.solve(V.T,np.asarray(primitives)).T
        self.P[-1]=0.
        points=[];self.cells=[]
        for lo,hi in zip(self.edges,self.edges[1:]):
            y=(lo+hi)/2+(hi-lo)*x/2
            if min(y)<=lo or max(y)>=hi:raise ArithmeticError('The real material quadrature has unresolved coincident radii.')
            index=len(points);self.cells.append((index,index+order+1,(hi-lo)/2))
            points.extend((lo,*y))
        self.r=np.r_[points,self.edges[-1]]
    def primitive_from_outer(self,values,boundary):
        values=np.asarray(values)
        if values.shape[0]!=len(self.r):raise ValueError('Wrong physical radial field.')
        out=np.empty_like(values,dtype=np.result_type(values,boundary))
        out[-1]=boundary
        for i,j,h in reversed(self.cells):
            out[i:j]=out[j]+h*np.tensordot(self.P[:-1],values[i+1:j],axes=(1,0))
        return out


def fourier_height(phi,cos_coeff,sin_coeff):
    """Each coefficient array [derivative 0/1/2,r,k=0..K] at one fixed real material lattice."""
    public()
    C=np.asarray(cos_coeff);S=np.asarray(sin_coeff);phi=np.asarray(phi)
    if C.shape!=S.shape or C.ndim!=3 or C.shape[0]!=3 or np.any(S[:,:,0]!=0):raise ValueError('Complete degree zero and Fourier coefficients required.')
    freq=np.arange(C.shape[2]);phase=freq[:,None]*phi[None,:]
    out={}
    for k in range(4):
        c=(freq[:,None]**k)*np.cos(phase+k*np.pi/2)
        s=(freq[:,None]**k)*np.sin(phase+k*np.pi/2)
        for d in range(3):
            if d==0 or k<=2:out[d,k]=C[d]@c+S[d]@s
    return out


def smooth_join(r,left,right):
    if left<=r[0] or right>=r[-1] or not left<right:raise ValueError('The C2 joining band must be strictly inside the body.')
    v=np.clip((r-left)/(right-left),0.,1.);s=v**3*(10+v*(-15+6*v))
    return ((1-s)[:,None,None],(-30*v*v*(1-v)**2/(right-left))[:,None,None],
            (-60*v*(1-v)*(1-2*v)/(right-left)**2)[:,None,None])


def surface(grid,phi,jet,E,Ep,theta,cx,cz,joining_band):
    public()
    r=grid.r[:,None];phi=np.asarray(phi);E=np.asarray(E)[:,None];Ep=np.asarray(Ep)[:,None]
    if E.shape!=r.shape or Ep.shape!=r.shape or np.any(E.real<=0):raise ValueError('The same prescribed E and its derivative are required.')
    if any(np.shape(jet[d,k])!=(len(r),len(phi)) for d in range(3) for k in range(4 if d==0 else 3)):
        raise ValueError('All needed real material angular derivatives of the same height are required.')
    ur=tuple(jet[1,k] for k in range(3));upp=tuple(jet[2,k] for k in range(3));up=tuple(jet[0,k+1] for k in range(3))
    er=scalar(E);gamma=scalar(Ep/(2*E));sr=scalar(r);se=scalar(np.sqrt(E))
    A2=add(er,neg(mul(ur,ur)));A=sqrt_jet(A2)
    ss=add(scalar(np.ones_like(E)),neg(add(mul(mul(ur,ur),inv(er)),mul(mul(up,up),inv(mul(sr,sr))))))
    normal=sqrt_jet(ss);hrr=add(upp,neg(mul(gamma,ur)))
    B=neg(mul(mul(mul(se,up),hrr),inv(mul(mul(A2,sr),normal))))
    b=tuple(grid.primitive_from_outer(v,t) for v,t in zip(B,(phi,np.ones_like(phi),np.zeros_like(phi))))
    P=phase(b);V=times(A,P)
    zero=np.zeros_like(phi);one=np.ones_like(phi);p=phase((phi,one,zero))
    U=tuple(grid.primitive_from_outer(v,r[-1,0]*q) for v,q in zip(V,p))
    ar=(Ep-2*ur[0]*upp[0])/(2*A[0])
    Urr=ar[...,None]*P[0]+(A[0]*B[0])[...,None]*rotate_vec(P[0])
    C=-ur[0]*up[0]/A[0];dd=r*np.sqrt(E)*normal[0]/A[0]
    ssr=-2*ur[0]*upp[0]/E+ur[0]**2*Ep/E**2-2*up[0]*ur[1]/r**2+2*up[0]**2/r**3
    dd_r=dd*(1/r+gamma[0]+ssr/(2*ss[0])-ar/A[0])
    G=(dd_r+C*B[0])/A[0];W=b[1]-G
    tangent_hat=C[...,None]*P[0]+dd[...,None]*rotate_vec(P[0])
    H=U[1]-tangent_hat
    determinant=hrr[0]*(up[1]+r*ur[0]/E)-(ur[1]-up[0]/r)**2-Ep/(2*r*E**2)*(r*r*E-r*r*ur[0]**2-E*up[0]**2)
    curvature_integrand=-determinant/(r*np.sqrt(E)*normal[0]**3)
    Wint=grid.primitive_from_outer(curvature_integrand,W[-1])
    Hint=grid.primitive_from_outer((A[0]*Wint)[...,None]*rotate_vec(P[0]),H[-1])
    er0=vector((np.cos(theta)*np.cos(phi),-np.cos(theta)*np.sin(phi),-np.cos(theta)*np.cos(phi)),
               (np.sin(phi),np.cos(phi),-np.sin(phi)))
    ua=list(constant_scale(er0,r[0,0]))
    ua[0]=ua[0]+np.array([cx,0.]);ua=tuple(ua)
    mag=sqrt_jet(add(mul(tuple(v[...,0] for v in er0),tuple(v[...,0] for v in er0)),
                     mul(tuple(v[...,1] for v in er0),tuple(v[...,1] for v in er0))))
    ra=cmul(times(inv(mag),er0),conjugate(tuple(v[0] for v in P)))
    inner=add(ua,cmul(ra,tuple(v-v[:1] for v in U)))
    inner_r=cmul(ra,V)
    inner_rr=ra[0][...,0,None]*Urr+ra[0][...,1,None]*rotate_vec(Urr)
    ch,cp,cpp=smooth_join(grid.r,*joining_band)
    dh=add(inner,neg(U));dh_r=add(inner_r,neg(V));dh_rr=inner_rr-Urr
    joined=add(U,tuple(ch*d for d in dh))
    joined_r=add(V,tuple(ch*d+cp*q for d,q in zip(dh_r,dh)))
    joined_rr=Urr+ch*dh_rr+2*cp*dh_r[0]+cpp*dh[0]
    def three(p,z):return np.concatenate((p,z[...,None]),axis=-1)
    def six(u,v,rr):
        return (three(u[0],jet[0,0]),three(v[0],ur[0]),three(u[1],up[0])/r[...,None],
               three(rr,upp[0]),three(v[1],ur[1])/r[...,None],three(u[2],up[1])/r[...,None]**2)
    actual=six(joined,joined_r,joined_rr);outer=six(U,V,Urr);inner_six=six(inner,inner_r,inner_rr)
    boundary=[]
    for ix,ang,center in ((0,theta,[cx,0.,cz]),(-1,0.,[0.,0.,0.])):
        cp0,sp0=np.cos(phi),np.sin(phi)
        e=np.stack((np.cos(ang)*cp0,sp0,-np.sin(ang)*cp0),axis=1)
        t=np.stack((-np.cos(ang)*sp0,cp0,np.sin(ang)*sp0),axis=1)
        known=(np.asarray(center)+r[ix,0]*e,e,t,np.zeros_like(e),t/r[ix,0],-e/r[ix,0])
        boundary.append([float(np.max(np.linalg.norm((z[ix]-k).real,axis=-1))) for z,k in zip(actual,known)])
    dot=lambda a,b:np.sum(a*b,axis=-1)
    metrics=tuple((dot(z[1],z[1])/E-1,dot(z[1],z[2])/np.sqrt(E),dot(z[2],z[2])-1) for z in (outer,inner_six,actual))
    return dict(actual_physical_six=actual,outer_physical_six=outer,inner_physical_six=inner_six,
                relative_Gram_three=metrics,inner_outer_rim_errors=boundary,scalar_D=determinant,
                A=A[0],normal_height=normal[0],rotation_integrand=B[0],coframe_W=W,integrated_W=Wint,
                mixed_displacement=H,integrated_H=Hint,coframe_rotation_mismatch=ra[0]-np.array([1.,0.]),
                inner_minus_outer_position=dh[0],inner_minus_outer_radial=dh_r[0],inner_minus_outer_angular=dh[1],
                all_angle_development_rotation_jets=b,all_angle_development_position_jets=U,
                domain_positive_on_actual_nodes=True,continuous_enclosure=False)
