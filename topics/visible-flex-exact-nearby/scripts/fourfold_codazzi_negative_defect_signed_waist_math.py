"""Two real negative-body solutions for Newton and q_nu-Z, with full joint residual."""
from fractions import Fraction
from pathlib import Path
import hashlib


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def truncate(c, tc, field, count):
    """Keep powers 0..count; charge the entire omitted Fourier--radial Wiener norm."""
    if len(field.coefficients) <= count+1:
        return field
    tail=c.wiener(field.Fourier()[:,count+1:,:])
    return tc.BatchRadialFourier(c,field.coefficients[:count+1],field.degree,field.norm,
                                c.add_upper(field.error,tail),field.degree)


def combine(c, tc, first, second):
    fields=(first,second)
    z=c.zeros((tc.GRID,max(len(x.coefficients) for x in fields),2))
    for j,p in enumerate(fields):
        z[:,:len(p.coefficients),j:j+1]=p.Fourier()
    error=c.Box(c.np.array([float(c.np.max(p.error.hi)) for p in fields]))
    return tc.BatchRadialFourier.from_fourier(c,z,max(x.degree for x in fields),error,
                                              max(x.error_degree for x in fields))


def equations(c,tc,positive,np_math,helper,base,direction,offsets,row,piece,lo,hi,read):
    """Selected compact coefficient as a signed radial polynomial, before any range is taken."""
    def scalar(value):
        return tc.BatchRadialFourier.scalar(c,[value])
    fields={name:tc.scalar_taylor(c,row["intrinsic_midpoint_jets"],row["intrinsic_whole_third_jets"],
                 name,*row["interval"],lo,hi,read) for name in ("K","gamma","s","beta")}
    delta=c.exact(-helper.DELTA).union(c.exact(helper.DELTA))
    delta_field=scalar(c.arb_box(delta))
    K0,g0,s,beta=(fields[k] for k in ("K","gamma","s","beta"))
    W,dW,L,dK,Knu,J12,J21=(scalar(0) for _ in range(7))
    K,gamma=K0,g0
    if helper.CONTROL[0]<=lo and hi<=helper.CONTROL[1]:
        W,dW=np_math.control_fields(c,tc,lo,hi)
        # W is in [0,1] on its full actual support. A constant exponential
        # enclosure multiplies a signed radial polynomial; it costs O(delta).
        e=delta*c.arb(0).union(c.arb(1))
        expneg=scalar(c.arb_box((-e).exp()))
        exphalf=scalar(c.arb_box((e/2).exp()))
        expmhalf=scalar(c.arb_box((-e/2).exp()))
        W,dW=(truncate(c,tc,f,5) for f in (W,dW))
        T=np_math.metric_T_taylor(c,tc,row,lo,hi,read)
        L=truncate(c,tc,T*dW,5)
        dK=K0*scalar(c.arb_box((-e).expm1()))+delta_field*expneg*L
        K,gamma=K0+dK,g0*exphalf
        affine=K0+delta_field*L
        Knu=truncate(c,tc,expneg*(L-W*affine),6)
        J12=truncate(c,tc,g0*expmhalf*(L-W*affine*.5),6)
        J21=truncate(c,tc,-gamma*W*.5,6)
    else:
        require(hi<=helper.CONTROL[0] or lo>=helper.CONTROL[1],"all compact seams split")
    (u0,w0),(ur0,wr0)=positive.cubic_pair(c,tc,helper,base,offsets["base"],piece,lo,hi,"base")
    (a,b),(ar,br)=positive.cubic_pair(c,tc,helper,direction,offsets["direction"],piece,lo,hi,"direction")
    u,w=u0+delta_field*a,w0+delta_field*b
    v=s+w
    op=tc.prepare_operator((u,v),{"K":K,"gamma":gamma,"beta":beta})
    op={key:truncate(c,tc,value,6) for key,value in op.items()}
    up,vp=u.derivative(),v.derivative()
    v2=v*v
    S=u*u+K*v2
    drift=op["d"]
    newton=(drift*up+op["speed12"]*vp-beta*u*(1+S)-ur0-delta_field*ar,
            drift*vp+op["speed21"]*up+beta*(w-u*u*v-K*w*(v2+v*s+s*s)-dK*s*s*s)-wr0-delta_field*br)
    az=tc.apply_operator(op,(a,b))
    iv=v2.primitive()
    fnu=(-beta*Knu*(iv*up+v2*u)+v.mean()*J12*vp,
         -beta*Knu*(iv*vp+v2*v)+v.mean()*J21*up)
    nu=(az[0]+fnu[0]-ar,az[1]+fnu[1]-br)
    return op,tuple(combine(c,tc,truncate(c,tc,x,7),truncate(c,tc,y,7)) for x,y in zip(newton,nu))


def midpoint_angular(field, tau):
    a=field.coefficients[-1]
    value=(a.lo+a.hi)/2
    for coefficient in reversed(field.coefficients[:-1]):
        value=tau*value+(coefficient.lo+coefficient.hi)/2
    return value


def proposal_rhs(c, tc, operator, sources, tau):
    """Unverified choices for Hermite endpoints; no subsequent bound trusts the RK step."""
    np=c.np
    op={key:midpoint_angular(value,tau) for key,value in operator.items()}
    forcing=tuple(midpoint_angular(v,tau) for v in sources)
    grid,head=tc.GRID,tc.HEAD
    q=np.sqrt(.5)
    modes=np.fft.fftfreq(grid)*grid
    derivative=(4j*modes)[:,None]
    inverse=np.zeros((grid,1),dtype=np.complex128)
    inverse[1:,0]=1/derivative[1:,0]
    inverse[grid//2,0]=0.
    def raw(state):
        p=np.zeros((grid,2),dtype=np.complex128)
        s=np.zeros_like(p)
        p[1:head+1]=-1j*q*state[:head]
        s[1:head+1]=q*state[head+1:]
        p[-head:]=np.conjugate(p[head:0:-1])
        s[-head:]=np.conjugate(s[head:0:-1])
        s[0]=state[head]
        h1,h2=(np.fft.ifft(z,axis=0).real*grid for z in (p,s))
        h1p,h2p=(np.fft.ifft(derivative*z,axis=0).real*grid for z in (p,s))
        inside=np.fft.ifft(inverse*np.fft.fft(op["inner1"]*h1+op["inner2"]*h2,axis=0),axis=0).real
        f=forcing[0]+op["d"]*h1p+op["speed12"]*h2p+op["l11"]*h1+op["l12"]*h2+op["nonlocal1"]*inside+op["mean1"]*state[head]
        g=forcing[1]+op["d"]*h2p+op["speed21"]*h1p+op["l21"]*h1+op["l22"]*h2+op["nonlocal2"]*inside+op["mean2"]*state[head]
        f,g=(np.fft.fft(z,axis=0)/grid for z in (f,g))
        return np.vstack((-np.sqrt(2)*f[1:head+1].imag,g[:1].real,np.sqrt(2)*g[1:head+1].real))
    return raw


def trial(c,tc,op,forces,lo,hi,right,zero_on_root_bracket):
    h=float(lo-hi)
    np=c.np
    if zero_on_root_bracket:
        require(np.all(right==0),"both trial traces vanish on the whole root bracket")
        left=right.copy()
        slope_l=slope_r=np.zeros_like(right)
    else:
        left_rhs,mid_rhs,right_rhs=(proposal_rhs(c,tc,op,forces,t) for t in (-1.,0.,1.))
        slope_r=right_rhs(right)
        k2=mid_rhs(right+h*slope_r/2)
        k3=mid_rhs(right+h*k2/2)
        k4=left_rhs(right+h*k3)
        left=right+(h/6)*(slope_r+2*k2+2*k3+k4)
        slope_l=left_rhs(left)
    require(np.all(np.isfinite(left)) and np.all(np.isfinite(slope_l)) and np.all(np.isfinite(slope_r)),
            "both full finite proposal columns")
    # These full binary64 endpoints are exact dyadics. The cubic has the exact
    # same joint endpoint as its neighbour, irrespective of derivative rounding.
    y0,y1=c.Box(left),c.Box(right)
    a0,a1=c.box(hi-lo)*c.Box(slope_l),c.box(hi-lo)*c.Box(slope_r)
    cs=[y0,a0,3*(y1-y0)-2*a0-a1,-2*(y1-y0)+a0+a1]
    cs=c.affine_polynomial(cs,Fraction(1,2),Fraction(1,2))
    fields=tc.reflection_polynomial(c,cs)
    return left,slope_l,slope_r,fields


def angular_gram_weights(c, root):
    if not root:
        return c.Box(1.)
    weights=[c.arb_box((c.exact(1+16*int(k)**2).log()/3).exp()) for k in c.modes]
    return c.Box(c.np.array([float(w.lo) for w in weights]),c.np.array([float(w.hi) for w in weights]))


def residual_gram(c,tc,pair,length,root,weight):
    """Full signed 2x2 Gram including every Legendre and both Fourier signs."""
    gram=[[c.Box(0.) for _ in range(2)] for _ in range(2)]
    for p in pair:
        z=c.legendre_coefficients(p.Fourier())
        local=[[c.Box(0.) for _ in range(2)] for _ in range(2)]
        for j in range(2):
            for k in range(j,2):
                for order in range(z.real.lo.shape[1]):
                    a,b=z[:,order,j],z[:,order,k]
                    real=(a.real*b.real+a.imag*b.imag) if j!=k else (
                        tc._square(c,a.real)+
                        tc._square(c,a.imag))
                    local[j][k]=local[j][k]+c.reduce_box(weight*real,axis=0)*c.box(length/(2*order+1))
                local[k][j]=local[j][k]
        # The uniform Fourier-Wiener tail can have either sign and any mode
        # through p.error_degree. The H^(1/3) norm costs a single max weight.
        ew=(c.exact(1+16*p.error_degree**2).log()/6).exp() if root else c.arb(1)
        ed=[c.sqrt_upper(c.box(length))*c.arb_box(ew)*c.Box(float(c.np.broadcast_to(p.error.hi,(2,))[j])) for j in range(2)]
        norms=[c.sqrt_upper(c.upper(local[j][j])) for j in range(2)]
        for j in range(2):
            for k in range(j,2):
                fee=c.upper(norms[j]*ed[k]+norms[k]*ed[j]+ed[j]*ed[k])
                total=local[j][k]+c.Box(-float(fee.hi),float(fee.hi))
                gram[j][k]=gram[j][k]+total
                gram[k][j]=gram[j][k]
    return gram


def run(c,tc,positive,np_math,helper,base,direction,offsets,rows,plan,read,private,checkpoint):
    """First public directed residuals on all negative cells; row identity is exact."""
    np=c.np
    chosen=[item for item in plan if item[2]<helper.ROOT[1]]
    require(chosen[0][2]==0 and chosen[-1][3]==helper.ROOT[1]
            and all(a[3]==b[2] for a,b in zip(chosen,chosen[1:])),"one complete negative enclosing window")
    right=np.zeros((tc.DIMENSION,2),dtype="<f8")
    grams={key:[[c.Box(0.) for _ in range(2)] for _ in range(2)] for key in ("strict","root")}
    directory=Path(private)
    directory.mkdir(parents=True,exist_ok=False)
    weights={root:angular_gram_weights(c,root) for root in (False,True)}
    all_sha=hashlib.sha256()
    chain=hashlib.sha256(b"ASQ23 full signed cubic ordered block chain v1").digest()
    with (directory/"two-signed-cubic-traces.f64").open("xb") as stream:
        for count,(j,k,lo,hi) in enumerate(reversed(chosen),1):
            require(hi<=helper.NEGATIVE_CUT or lo>=helper.NEGATIVE_CUT,"split original strict/mixed interface")
            operator,sources=equations(c,tc,positive,np_math,helper,base,direction,offsets,rows[j],k,lo,hi,read)
            left,sl,sr,h=trial(c,tc,operator,sources,lo,hi,right,lo>=helper.ROOT[0])
            derivatives=tuple(p.radial_derivative(c.exact(2/(hi-lo))) for p in h)
            ah=tc.apply_operator(operator,h)
            residual=tuple(f+a-d for f,a,d in zip(sources,ah,derivatives))
            root=lo>=helper.NEGATIVE_CUT
            local=residual_gram(c,tc,residual,hi-lo,root,weights[root])
            target=grams["root" if root else "strict"]
            for y in range(2):
                for x in range(2):
                    target[y][x]=target[y][x]+local[y][x]
            block=np.ascontiguousarray(np.stack((right,sr,left,sl)),dtype="<f8").tobytes()
            stream.write(block)
            all_sha.update(block)
            chain=hashlib.sha256(chain+hashlib.sha256(block).digest()).digest()
            right=left
            stream.flush()
            checkpoint(count,len(chosen),lo,right,grams,all_sha.hexdigest(),chain.hex())
    path=directory/"two-signed-cubic-traces.f64"
    verify=hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):
            verify.update(block)
    require(verify.hexdigest()==all_sha.hexdigest()
            and path.stat().st_size==len(chosen)*4*tc.DIMENSION*2*8,
            "the whole two-column degree-three signed trial and every complete physical interface")
    return right,grams,{"bytes":path.stat().st_size,"sha256":verify.hexdigest(),"complete_cells":len(chosen),
                        "ordered_hash_chain":chain.hex(),"shape":[len(chosen),4,tc.DIMENSION,2],"dtype":"<f8","order":"descending radial cells"}
