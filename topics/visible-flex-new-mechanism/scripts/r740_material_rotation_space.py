"""C2 native disk rotation coordinates and true sparse all-column R740 derivatives."""
import numpy as np
from scipy.sparse import csr_matrix

from r688_actual_r664_window_collars import mollifier_cdf, quadrature
from r732_compensated_pulses import H, gate
from r732_disk_fields import rotation, apply
from r732_physical_disk import R0, DU


TOTAL = .776
GLOBAL_BREAKS = np.array([0.,.07,.47,.52,.548,.584,.602,.662,.721,TOTAL])
FILLET_BREAKS = np.array([.52,.602,.663,.719,TOTAL])
# All degree levels use these same splines. Increasing the level adds tagged
# columns, preserving the smaller field exactly by injection.
NP_GLOBAL = len(GLOBAL_BREAKS)+2
NP_LOCAL = len(FILLET_BREAKS)+2


def tagged_terms(degree):
    if degree not in (3,5):
        raise ValueError("the two actual R740 levels are 3 and 5")
    core = [("core",i,j) for i in range(degree+1) for j in range(degree+1-i)]
    modes = [0,1,-1] if degree==3 else [0,1,-1,2,-2,3,-3]
    ring = [("ring",i,m) for i in range(NP_GLOBAL) for m in modes]
    radial = (1,3,5) if degree==3 else tuple(range(NP_LOCAL))
    brushes = ("wide",) if degree==3 else ("wide","nested")
    edge = [("pulse",i,side,sgn,c,brush) for i in radial
            for side in (0,2) for sgn in (-1,1) for c in (.206,.847) for brush in brushes]
    return core+ring+edge


def padded(q,old,new):
    before = tagged_terms(old)
    after = tagged_terms(new)
    vals = dict(zip(before,np.asarray(q).reshape(-1,3),strict=True))
    return np.asarray([vals.get(tag,np.zeros(3)) for tag in after]).reshape(-1)


def ell_data(r):
    r = np.asarray(r)
    t = np.clip((r-R0)/(1-R0),0.,1.)
    c = DU*(1-R0)/R0
    h = TOTAL-c
    return ((1-t)*(c+h*(1+t+t*t)), -(c+3*h*t*t)/(1-R0), -6*h*t/(1-R0)**2)


def tail_weight(r):
    ell,er,err = ell_data(r)
    v = (ell-.04)/.43
    return gate(v),gate(v,1)*er/.43,gate(v,2)*(er/.43)**2+gate(v,1)*err/.43


def cubic(x, breaks):
    """All clamped physical cubic B splines and their true material derivative."""
    knots = np.r_[np.repeat(breaks[0],3),breaks,np.repeat(breaks[-1],3)]
    a = np.asarray(x)
    inside = (a>=breaks[0])&(a<=breaks[-1])
    # The right-limit convention in the final clamped span is its real left limit.
    z = np.minimum(a,np.nextafter(breaks[-1],breaks[0]))
    table = ((z[:,None]>=knots[:-1])&(z[:,None]<knots[1:])).astype(float)
    derivative = None
    for order in (1,2,3):
        n = len(knots)-1-order
        left = knots[order:order+n]-knots[:n]
        right = knots[order+1:order+1+n]-knots[1:1+n]
        la = np.divide(table[:,:n],left,out=np.zeros((len(a),n)),where=left!=0)
        ra = np.divide(table[:,1:1+n],right,out=np.zeros((len(a),n)),where=right!=0)
        table = (z[:,None]-knots[:n])*la+(knots[order+1:order+1+n]-z[:,None])*ra
        derivative = order*(la-ra)
    table[~inside,:]=0.;derivative[~inside,:]=0.
    return table,derivative


def edge_shapes(build,ss):
    unique, inverse = np.unique(ss,return_inverse=True)
    _,kind,v = build.ring.label(unique)
    dv = np.where(kind==0,build.ring.length,np.where(kind==2,-build.ring.length,0.))
    q,w = quadrature(build.order)
    norm = np.exp(-1/(1-q*q))@w
    def density(c,width):
        t = (abs(v)-c)/width
        a,b = (t-.001)/.0005,(t-.999)/.0005
        def bump(z):
            f = np.zeros_like(z)
            k = abs(z)<1
            f[k] = np.exp(-1/(1-z[k]**2))/norm
            return f
        val = mollifier_cdf(a)-mollifier_cdf(b)
        ds = (bump(a)-bump(b))*np.sign(v)*dv/(.0005*width)
        return val,ds
    result = {}
    for c in (.206,.847):
        wide,wd = density(c-.001,.102)
        inner,ide = density(c,.100)
        for side in (0,2):
            for sign in (-1,1):
                mask = (kind==side)&(np.sign(v)==sign)
                result[(side,sign,c,"wide")] = ((wide*mask)[inverse],(wd*mask)[inverse])
                result[(side,sign,c,"nested")] = (((inner-wide)*mask)[inverse],((ide-wd)*mask)[inverse])
    return result


def install(frame, build):
    degree = frame.degree
    tags = tagged_terms(degree)
    r,s = frame.r,frame.s
    # Radial splines vanish together with both jets at the disk centre and
    # at the prescribed Cauchy band. Cartesian polynomials supply the centre.
    ell,er,_ = ell_data(r)
    keep = 1-gate((r-.24)/.38)
    kr = -gate((r-.24)/.38,1)/.38
    core = frame.B.copy()
    core_r = frame.Br.copy()
    core_s = frame.Bs.copy()
    global_b,global_e = cubic(ell,GLOBAL_BREAKS)
    local_b,local_e = cubic(ell,FILLET_BREAKS)
    # Taper the local clamped end basis on BOTH native extent boundaries.
    # This prevents the endpoint basis jumping when extended by zero.
    la = (ell-FILLET_BREAKS[0])/.04
    lb = (TOTAL-ell)/.035
    local_gate = gate(la)*gate(lb)
    local_gate_e = (gate(la,1)*gate(lb)/.04-gate(la)*gate(lb,1)/.035)
    local_e = local_gate[:,None]*local_e+local_gate_e[:,None]*local_b
    local_b *= local_gate[:,None]
    a,b = (ell-H)/.035,(r-R0)/.13
    envelope = gate(a)*gate(b)
    envelope_r = gate(a,1)*er/.035*gate(b)+gate(a)*gate(b,1)/.13
    modes = {0:(np.ones_like(s),np.zeros_like(s))}
    for m in (1,2,3):
        angle = 2*np.pi*m*s
        factor = 2*np.pi*m
        modes[m] = np.cos(angle),-factor*np.sin(angle)
        modes[-m] = np.sin(angle),factor*np.cos(angle)
    edge = edge_shapes(build,s)
    shape = (len(r),len(tags))
    B,Br,Bs = (np.empty(shape) for _ in range(3))
    for j,t in enumerate(tags):
        if t[0]=="core":
            B[:,j]=keep*core[:,j]
            Br[:,j]=kr*core[:,j]+keep*core_r[:,j]
            Bs[:,j]=keep*core_s[:,j]
            continue
        if t[0]=="ring":
            radial = global_b[:,t[1]]
            radial_r = global_e[:,t[1]]*er
            angular,angular_s = modes[t[2]]
        else:
            radial = local_b[:,t[1]]
            radial_r = local_e[:,t[1]]*er
            angular,angular_s = edge[t[2:]]
        radial_r = envelope_r*radial+envelope*radial_r
        radial = envelope*radial
        B[:,j]=radial*angular
        Br[:,j]=radial_r*angular
        Bs[:,j]=radial*angular_s
    frame.B,frame.Br,frame.Bs = B,Br,Bs
    frame.ncols=3*len(tags)
    frame.q0=np.zeros(frame.ncols)


def angular_curl(frame,a,ar,az):
    M,R,S = frame.base,frame.br,frame.bs
    for axis in range(3):
        U,D = rotation(a[:,axis],axis)
        d = M@D
        R=R@U+ar[:,axis,None,None]*d
        S=S@U+az[:,axis,None,None]*d
        M=M@U
    _,xr,xs,*_ = frame.j0
    return (apply(R,xs)-apply(S,xr))/frame.det[:,None]


def channels(frame,q):
    coef = np.asarray(q).reshape(-1,3)
    args = [frame.B@coef,frame.Br@coef,frame.Bs@coef]
    out = np.empty((3,3,len(frame.r),3))
    for slot in range(3):
        for axis in range(3):
            z = [a.astype(complex) if i==slot else a for i,a in enumerate(args)]
            z[slot][:,axis] += 1.e-24j
            out[slot,axis] = angular_curl(frame,*z).imag/1.e-24
    if not np.isfinite(out).all():
        raise ArithmeticError("nonfinite actual polar-to-Cartesian curl channel")
    return out


def sparse_jac(frame,q,ch):
    from scipy.sparse import vstack
    blocks = []
    B,Br,Bs = frame.B,frame.Br,frame.Bs
    nb = B.shape[1]
    for i in range(0,len(B),96):
        h = slice(i,i+96)
        rows = len(B[h])
        data = np.empty((rows,3,nb,3))
        for axis in range(3):
            data[:,:,:,axis] = sum(ch[k,axis,h,:,None]*v[h,None,:]
                                    for k,v in enumerate((B,Br,Bs)))
        blocks.append(csr_matrix(data.reshape(3*rows,3*nb)))
    mat = vstack(blocks,format="csr")
    ids = np.unique(np.r_[0,1,2,np.linspace(0,3*nb-1,12,dtype=int),3*nb-1])
    defects = []
    for j in ids:
        z = np.asarray(q,dtype=complex).copy()
        z[j]+=1.e-24j
        direct = frame.curl(z).imag.ravel()/1.e-24
        use = mat.getcol(j).toarray().ravel()
        defects.append(float(np.max(abs(direct-use))/max(1.,np.max(abs(direct)))))
    if max(defects)>2.e-10:
        raise ArithmeticError("native all-column Jacobian disagrees with independent original complex-step")
    return dict(data=mat.data,indices=mat.indices,indptr=mat.indptr,shape=mat.shape,
                sampled_columns=ids,scaled_check_defects=defects)


def normal_factor(raw,residual,identity):
    mat = csr_matrix((raw["data"],raw["indices"],raw["indptr"]),shape=raw["shape"])
    nrow = residual.size//3
    scale = np.sqrt(np.asarray(mat.power(2).sum(axis=0)).ravel()/nrow)
    active = scale>0
    bounded = np.maximum(scale,max(1.e-300,float(np.max(scale))*1.e-8))
    inv = 1./bounded
    scaled = mat.multiply(inv).tocsr()
    gram = (scaled.T@scaled).toarray()/nrow
    g = np.asarray(scaled.T@residual.ravel()).ravel()/nrow
    lam,V = np.linalg.eigh((gram+gram.T)/2)
    lam=lam[::-1];V=V[:,::-1]
    cutoff = 64*np.finfo(float).eps*len(lam)*max(1.,float(lam[0]))
    if np.min(lam)<-cutoff:
        raise ArithmeticError("invalid scaled Gram spectrum")
    sv=np.sqrt(np.where(lam>cutoff,lam,0.))
    projected=np.divide(V.T@g,sv,out=np.zeros_like(sv),where=sv>0)
    raw_gram=bounded[:,None]*gram*bounded[None,:]
    raw_lam=np.linalg.eigvalsh((raw_gram+raw_gram.T)/2)
    raw_floor=64*np.finfo(float).eps*len(raw_lam)*max(1.,float(raw_lam[-1]))
    label=dict(format="csr",shape=list(raw["shape"]),nnz=len(raw["data"]),
               arrays={k:identity(raw[k]) for k in ("data","indices","indptr")},
               spectrum_convention="column-scaled J/sqrt(number of vector samples)",
               gram_eigenvalue_resolution=cutoff,nonzero_columns=int(np.sum(active)),
               raw_singular_largest=float(np.sqrt(max(0.,raw_lam[-1]))),
               raw_rank_above_gram_resolution=int(np.sum(raw_lam>raw_floor)),
               raw_gram_eigenvalue_resolution=raw_floor,column_scale_floor=float(np.min(bounded)),
               column_scales=identity(scale),independent_columns=raw["sampled_columns"].tolist(),
               max_independent_scaled_defect=max(raw["scaled_check_defects"]))
    return dict(s=sv,Vt=V.T*inv[None,:],projected=projected,raw=label,
                column_scale=scale,gram=gram,gradient=g,raw_gram_eigenvalues=raw_lam)
