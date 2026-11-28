"""Real radial two-jet transfer of the single paid R703 native curve."""
import numpy as np
from scipy.linalg import qr, svdvals, solve_triangular
from r703_weighted_material_field import Rad, rdot
from r726_paid_half_projection import angular_at


def components(f, i):
    return f.transform(lambda t: t[..., i])


def conj(f):
    return f.transform(np.conj)


def norm_complex(f, axis=None):
    v = f*conj(f)
    if axis is not None:
        v = v.transform(lambda t: t.sum(axis=axis, keepdims=True))
    return v.transform(np.real).power(.5)


def project(A, K, n, counts):
    psi = np.linspace(0., np.pi, n+1)
    wt = np.ones(len(psi))/n
    wt[[0,-1]] *= .5
    raw = A.transform(lambda t: angular_at(t, psi, 1))
    mirror = A.transform(lambda t: angular_at(t, -psi, 1)*np.array([1.,-1.,1.]))
    v = (raw-mirror)*.5
    diff = raw-v
    reflect = [float(np.linalg.norm(t, axis=-1).max()) for t in (diff.x,diff.d,diff.dd)]
    endpoint = []
    for z in (v.x,v.d,v.dd):
        endpoint.append(float(abs(z[:, [0,-1]][:,:,[0,2]]).max()))
        for end in (0,-1):
            z[:,end,0] = 0.
            z[:,end,2] = 0.
    if np.any(v.x[:,0,1]<=0) or np.any(v.x[:,-1,1]>=0):
        raise FloatingPointError('The actual paid ring failed its pole orientation.')
    vsq = rdot(v,v)
    if np.any(vsq.x<=0): raise FloatingPointError('A transported velocity vanished.')
    speed = vsq.power(.5)
    L = (speed*wt).transform(lambda z: z.sum(axis=1,keepdims=True))
    length_factor = (speed/L).power(.5)
    normal = v/speed.col()
    nr = len(A.x)
    z = np.zeros(nr,complex)
    f,h = Rad(np.ones(nr,complex),z.copy(),z.copy()),Rad(z.copy(),z.copy(),z.copy())
    def bank():
        zz = [np.empty((nr,len(psi)),complex) for _ in range(3)]
        return Rad(*zz)
    a,b = bank(),bank()
    def put(target, j, value):
        for out,arg in zip((target.x,target.d,target.dd),(value.x,value.d,value.dd)):
            out[:,j] = arg
    put(a,0,f); put(b,0,h)
    overlap = 1.
    for j in range(1,len(psi)):
        nv = normal.transform(lambda t:t[:,j])
        nx,ny,nz = (components(nv,i) for i in range(3))
        off = nx+nz*1j
        ca = ((1+ny)*f+off*h)*.5
        cb = (conj(off)*f+(1-ny)*h)*.5
        ov = (ca*conj(ca)+cb*conj(cb)).transform(np.real)
        if np.any(ov.x<.3**2):raise FloatingPointError('The paid spinor mesh needs angular refinement.')
        scale=ov.power(.5)
        overlap=min(overlap,float(scale.x.min()))
        f,h=ca/scale,cb/scale
        put(a,j,f);put(b,j,h)
    trig=(np.arange(K+1)[:,None]+.5)*psi
    a=(a*length_factor).transform(lambda t:2*(t*wt)@np.cos(trig).T)
    b=(b*length_factor).transform(lambda t:2*(t*wt)@np.sin(trig).T)
    na,nb=norm_complex(a,1),norm_complex(b,1)
    if min(na.x.min(),nb.x.min(),abs(a.x[:,0]).min())<.2:
        raise FloatingPointError('Truncation normalization or the common phase pole is unresolved.')
    a,b=a/na,b/nb
    first=a.transform(lambda t:t[:,0:1]);phase=conj(first)/norm_complex(first)
    a,b=a*phase,b*phase
    def inverse(t,sign):
        flat=t.transform(lambda y:np.stack((y.real,y.imag),axis=-1).reshape(nr,-1))
        denominator=1+flat.transform(lambda y:y[:,0:1])*sign
        if denominator.x.min()<=.05:raise FloatingPointError('A stereographic source pole is too near.')
        return flat.transform(lambda y:y[:,1:])/denominator,float(denominator.x.min())
    za,ma=inverse(a,1);zb,mb=inverse(b,-1)
    aa=a.transform(lambda t:t@np.cos(trig));bb=b.transform(lambda t:t@np.sin(trig))
    cross=2*aa*conj(bb);yy=(aa*conj(aa)-bb*conj(bb)).transform(np.real)
    actual=Rad(*(np.stack((c.real,y,c.imag),axis=-1) for c,y in
                  zip((cross.x,cross.d,cross.dd),(yy.x,yy.d,yy.dd))))
    error=actual-v/L.col()
    counts['discrete_projector_radial_twojet_steps']+=n*nr
    counts['half_frequency_integrated_radial_twojet_coefficients']+=2*nr*(K+1)
    return za,zb,dict(minimum_actual_speed=float(speed.x.min()),minimum_projector_overlap=overlap,
            symmetry_jet_adjustment=reflect,pole_jet_adjustment=endpoint,
            true_normalization_before_projection=[float(L.x.min()),float(L.x.max())],
            unit_coefficient_factors=[[float(na.x.min()),float(na.x.max())],[float(nb.x.min()),float(nb.x.max())]],
            stereographic_denominators=[ma,mb],
            actual_velocity_projection_three_jets=[float(np.linalg.norm(t,axis=-1).max()) for t in
                                                    (error.x,error.d,error.dd)])


def hermite_fits(space,r,weights,chosen,za,zb,center,counts):
    h=(space.b-space.a)/space.spans
    w0=np.sqrt(weights[chosen])[:,None]
    stiffness=(1.,.35*h,.10*h*h)
    def system(values,center_block,subtract_seed):
        mats=[];targets=[]
        for j,(measured,scale) in enumerate(zip(values,stiffness)):
            m=space.basis(r,j)[int(center_block)]
            target=measured[chosen].copy()
            if subtract_seed:target[:,0]-=space.seed(r,j)[chosen]
            mats.append(scale*w0*m[chosen]);targets.append(scale*w0*target)
        A=np.vstack(mats);target=np.vstack(targets)
        Q,R=qr(A,mode='economic',check_finite=False)
        s=svdvals(R)
        if s[-1]<=np.finfo(float).eps*s[0]*len(R):raise ArithmeticError('Complete Hermite fitting matrix lost rank.')
        counts['complete_Hermite_QR_SVD']+=1
        coeff=solve_triangular(R,Q.T@target)
        return coeff,s.tolist()
    fa,sa=system((za.x,za.d,za.dd),False,False)
    fb,sb=system((zb.x,zb.d,zb.dd),False,True)
    fc,sc=system(tuple(t[:,[0,2]] for t in center),True,False)
    return (fa,fb,fc),dict(complete_singular_values=[sa,sb,sc],
           omitted_center_y_jets=[float(abs(t[:,1]).max()) for t in center],
           fit_count=int(chosen.sum()),heldout_count=int((~chosen).sum()),derivative_scales=list(stiffness))
