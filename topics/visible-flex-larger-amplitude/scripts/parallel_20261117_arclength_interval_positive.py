#!/usr/bin/env python3
"""Directed enclosures for a fixed finite arclength coordinate on C2 cells.

Only IEEE binary64 +,-,*,/,sqrt with one nextafter outward are used for
array interval arithmetic. A custom radix-two interval transform replaces
FFT error assumptions. Twiddles use integer interval Taylor series and a
Machin arctangent enclosure of pi. Exact-real binary nodal jets define the
quintic map. This certifies q_N and rho positivity, not a metric/reach bound.
"""
import argparse,gzip,hashlib,json,math,time
from fractions import Fraction
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def down(x):return np.nextafter(x,-np.inf)
def up(x):return np.nextafter(x,np.inf)
def exact(x):
    y=np.asarray(x,dtype=float);return y,y
def add(a,b):return down(a[0]+b[0]),up(a[1]+b[1])
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=np.array([a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]])
    return down(v.min(axis=0)),up(v.max(axis=0))
def div(a,b):
    if np.any((b[0]<=0)&(b[1]>=0)):raise ValueError('Interval division by zero')
    return mul(a,(down(1/b[1]),up(1/b[0])))
def scale(a,v):return mul(a,exact(v))
def absolute_upper(a):return np.maximum(abs(a[0]),abs(a[1]))
def square(a):
    lo=np.where((a[0]<=0)&(a[1]>=0),0.,np.minimum(abs(a[0]),abs(a[1])))
    hi=absolute_upper(a);return np.maximum(0.,down(lo*lo)),up(hi*hi)
def sqrt(a):
    if np.any(a[1]<0):raise ValueError('Negative square root interval')
    return np.maximum(0.,down(np.sqrt(np.maximum(0.,a[0])))),up(np.sqrt(np.maximum(0.,a[1])))
def sum_upper(x,axis=-1):
    # Sequential upper sums avoid an unspecified reduction-error model.
    z=np.moveaxis(np.asarray(x),axis,-1);out=np.zeros(z.shape[:-1])
    for j in range(z.shape[-1]):out=up(out+z[...,j])
    return out
def stack(values):return np.array([v[0]for v in values]),np.array([v[1]for v in values])
def at(a,key):return a[0][key],a[1][key]
def horner(co,u):
    ans=at(co,-1)
    for j in range(len(co[0])-2,-1,-1):ans=add(scale(ans,u),at(co,j))
    return ans

def atan_inverse(n,terms=80):
    val=sum((Fraction((-1)**j,(2*j+1)*n**(2*j+1))for j in range(terms)),Fraction())
    nxt=Fraction((-1)**terms,(2*terms+1)*n**(2*terms+1))
    return min(val,val+nxt),max(val,val+nxt)

class Transform:
    def __init__(self,Q):
        self.Q=Q;self.rev={};F=10**80;self.F=F
        a,b=atan_inverse(5);c,d=atan_inverse(239)
        pi=(16*a-4*d,16*b-4*c);self.pi_upper=up(float(pi[1]))
        assert Fraction.from_float(float(self.pi_upper))>=pi[1]
        def fl(v):return v.numerator//v.denominator
        p=(fl(pi[0]*F),-fl(-pi[1]*F));self.pi_integer=p
        assert 7*p[1]<22*F
        def imul(x,y):
            z=[xx*yy for xx in x for yy in y];return min(z)//F,-((-max(z))//F)
        def idiv(x,n):return x[0]//n,-((-x[1])//n)
        def iadd(x,y):return x[0]+y[0],x[1]+y[1]
        def ineg(x):return -x[1],-x[0]
        # Taylor truncation after term 40 is less than 10^-75 on |x|<pi.
        assert Fraction(22,7)**82/Fraction(math.factorial(82))<Fraction(1,10**75)
        assert Fraction(22,7)**83/Fraction(math.factorial(83))<Fraction(1,10**75)
        radius=10**5;cos=[];sin=[]
        for j in range(Q//2):
            x=(2*j*p[0]//Q,-((-2*j*p[1])//Q));xx=imul(x,x)
            tc=(F,F);ts=x;vc=tc;vs=ts
            for k in range(1,41):
                tc=ineg(idiv(imul(tc,xx),(2*k-1)*(2*k)))
                ts=ineg(idiv(imul(ts,xx),(2*k)*(2*k+1)))
                vc=iadd(vc,tc);vs=iadd(vs,ts)
            def binary(z):
                left=Fraction(z[0]-radius,F);right=Fraction(z[1]+radius,F)
                lo=down(float(left));hi=up(float(right))
                assert Fraction.from_float(float(lo))<=left and Fraction.from_float(float(hi))>=right
                return lo,hi
            cos.append(binary(vc));sin.append(binary(vs))
        self.cos=np.array(cos).T;self.sin=np.array(sin).T

    def fft(self,real,imag,sign=1):
        n=real[0].shape[-1]
        if n not in self.rev:
            bits=n.bit_length()-1
            if 2**bits!=n or self.Q%n:raise ValueError('Power-of-two transform divisor required')
            self.rev[n]=np.array([int(format(j,f'0{bits}b')[::-1],2)for j in range(n)])
        order=self.rev[n];shape=real[0].shape
        rr=(real[0][...,order].copy(),real[1][...,order].copy())
        ii=(imag[0][...,order].copy(),imag[1][...,order].copy())
        m=2
        while m<=n:
            half=m//2;wr=(self.cos[0,np.arange(half)*(self.Q//m)],self.cos[1,np.arange(half)*(self.Q//m)])
            wi=(self.sin[0,np.arange(half)*(self.Q//m)],self.sin[1,np.arange(half)*(self.Q//m)])
            if sign<0:wi=neg(wi)
            r=[z.reshape(-1,n//m,m)for z in rr];im=[z.reshape(-1,n//m,m)for z in ii]
            ar=(r[0][...,:half],r[1][...,:half]);ai=(im[0][...,:half],im[1][...,:half])
            br=(r[0][...,half:],r[1][...,half:]);bi=(im[0][...,half:],im[1][...,half:])
            tr=sub(mul(br,wr),mul(bi,wi));ti=add(mul(br,wi),mul(bi,wr))
            rp,rm=add(ar,tr),sub(ar,tr);ip,imn=add(ai,ti),sub(ai,ti)
            for k in range(2):
                r[k][...,:half]=rp[k];r[k][...,half:]=rm[k]
                im[k][...,:half]=ip[k];im[k][...,half:]=imn[k]
            rr=tuple(z.reshape(shape)for z in r);ii=tuple(z.reshape(shape)for z in im);m*=2
        return rr,ii

    def cosine_sine(self,coef,n,kind):
        # coef is [constant, cos/sin(2phi),...,cos/sin(2M phi)].
        shape=coef[0].shape[:-1]+(n,);rl=np.zeros(shape);rh=np.zeros(shape);il=np.zeros(shape);ih=np.zeros(shape)
        M=coef[0].shape[-1]-1;idx=2*np.arange(1,M+1)
        if 2*M>=n//2:raise ValueError('Field frequency reaches Nyquist')
        half=scale(at(coef,(...,slice(1,None))),.5)
        if kind=='cos':
            rl[...,0]=coef[0][...,0];rh[...,0]=coef[1][...,0]
            rl[...,idx]=rl[...,-idx]=half[0];rh[...,idx]=rh[...,-idx]=half[1]
        else:
            # sin coefficient a has positive-frequency coefficient -i*a/2.
            il[...,idx]=-half[1];ih[...,idx]=-half[0]
            il[...,-idx]=half[0];ih[...,-idx]=half[1]
        return self.fft((rl,rh),(il,ih))[0]

    def speed(self,Y,M,N):
        nu=2*np.arange(1,M+1);R=at(Y,(...,slice(1,M+1)));T=at(Y,(...,slice(M+1,2*M+1)));Z=at(Y,(...,slice(2*M+2,None)))
        def prepend(c,zero):return np.concatenate([zero[0][...,None],c[0]],axis=-1),np.concatenate([zero[1][...,None],c[1]],axis=-1)
        zero=exact(np.zeros(Y[0].shape[:-1]))
        dr=self.cosine_sine(prepend(neg(add(scale(R,nu),T)),zero),N,'sin')
        dt=self.cosine_sine(prepend(add(R,scale(T,nu)),at(Y,(...,0))),N,'cos')
        dz=self.cosine_sine(prepend(neg(scale(Z,nu)),zero),N,'sin')
        return sqrt(add(add(square(dr),square(dt)),square(dz)))

    def angular_lower(self,speed,N):
        zero=exact(np.zeros_like(speed[0]));hat,_=self.fft(speed,zero,sign=-1);hat=scale(hat,1/N)
        # Exact speed is even, so the exact real Fourier coefficients are real.
        Q=self.Q;shape=speed[0].shape[:-1]+(Q,);lo=np.zeros(shape);hi=np.zeros(shape)
        lo[...,0]=hat[0][...,0];hi[...,0]=hat[1][...,0]
        k=np.arange(1,N//2)
        lo[...,k]=lo[...,-k]=hat[0][...,k];hi[...,k]=hi[...,-k]=hat[1][...,k]
        ny=scale(at(hat,(...,N//2)),.5)
        lo[...,N//2]=lo[...,-N//2]=ny[0];hi[...,N//2]=hi[...,-N//2]=ny[1]
        values,_=self.fft((lo,hi),exact(np.zeros(shape)))
        deriv=up(2*sum_upper(up(k*absolute_upper(at(hat,(...,k))))))
        deriv=up(deriv+up((N//2)*absolute_upper(at(hat,(...,N//2)))))
        loss=up(up(self.pi_upper/Q)*deriv)
        return down(values[0].min(axis=-1)-loss),float(np.max(up(values[1]-values[0])))

def cell_coeff(y0,y1,v0,v1,a0,a1,h):
    c0=exact(y0);c1=mul(h,exact(v0));c2=scale(mul(mul(h,h),exact(a0)),.5)
    A=sub(sub(sub(exact(y1),c0),c1),c2);B=sub(sub(mul(h,exact(v1)),c1),scale(c2,2));C=sub(mul(mul(h,h),exact(a1)),scale(c2,2))
    return stack([c0,c1,c2,add(sub(scale(A,10),scale(B,4)),scale(C,.5)),sub(add(scale(A,-15),scale(B,7)),C),add(sub(scale(A,6),scale(B,3)),scale(C,.5))])

def derivative_bound(co,h,M):
    dp=div(scale(at(co,slice(1,None)),np.arange(1,6)[:,None]),h);nu=2*np.arange(1,M+1);B=0.
    for j in range(5):
        b=exact(np.zeros(co[0].shape[-1]))
        for k in range(j+1):b=add(b,div(scale(at(dp,k),math.comb(j,k)),exact(math.comb(4,k))))
        R=at(b,slice(1,M+1));T=at(b,slice(M+1,2*M+1));Z=at(b,slice(2*M+2,None))
        bounds=np.array([sum_upper(absolute_upper(add(scale(R,nu),T))),up(absolute_upper(at(b,0))+sum_upper(absolute_upper(add(R,scale(T,nu))))),sum_upper(absolute_upper(scale(Z,nu)))])
        B=max(B,float(sqrt(exact(sum_upper(up(bounds*bounds))))[1]))
    return B

def main(a):
    begin=time.perf_counter();source_sha=sha(__file__);data=json.loads(gzip.decompress(a.input.read_bytes()))
    M=data['M'];N=a.construction_angles;Q=a.angles;n=a.radial_subdivisions
    if N&(N-1)or Q&(Q-1)or Q<=N or n<1 or n&(n-1):raise ValueError('Need power-two Q>N and dyadic subdivisions')
    if not isinstance(M,int)or M<1 or a.batch_cells<1:raise ValueError('Positive integer field order and batch size required')
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
    x=np.asarray(data['mesh']);Y=np.asarray(data['states']);D=np.asarray(data['rhs'])
    if x.ndim!=1 or len(x)<2 or not np.all(np.isfinite(x))or not np.all(np.diff(x)>0):raise ValueError('Finite, strictly increasing mesh required')
    expected=(len(x),3*M+2)
    if Y.shape!=expected or D.shape!=expected or not np.all(np.isfinite(Y))or not np.all(np.isfinite(D)):raise ValueError('Finite complete value and first-jet tables required')
    if 'd2'in data:DD=np.asarray(data['d2'])
    else:
        import parallel_20261117_frenet_symbol as frenet
        import parallel_20261117_inward_profile as scalar
        if not data.get('success')or 'compact_curvature_pulse'in data['inward_scalar_profile']:raise ValueError('Explicit d2 required for this new scalar')
        if sha(scalar.__file__)!=data['inward_profile_sha256']or sha(frenet.__file__)!='7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831':raise ValueError('Frozen jet dependency changed')
        v=data['inward_scalar_profile'];profile=scalar.InwardProfile(data['fixed_scalar_profile']['geometry'],data['analytic_extension_origin'],v['cut'],v['curvature'],v['ramp_in'],v['ramp_out'],v['quadrature']);q=frenet.Frenet(M,data['N']);DD=[]
        for s,y,dy in zip(x,Y,D):
            r,ap,app=profile(s);k=ap/r;DD.append(q.jvp(y,k,dy,dk=app/r-k*k))
        DD=np.array(DD)
    if DD.shape!=expected or not np.all(np.isfinite(DD)):raise ValueError('Finite complete second-jet table required')
    jet_sha=hashlib.sha256(b''.join(np.ascontiguousarray(z,dtype='<f8').tobytes()for z in [x,Y,D,DD])).hexdigest()
    tr=Transform(Q);worst=dict(value=float('inf'));maxB=0.;maxwidth=0.;batch=[];info=[]
    def finish():
        nonlocal worst,maxwidth
        states=(np.array([z[0]for z in batch]),np.array([z[1]for z in batch]));speeds=tr.speed(states,M,N)
        lower,width=tr.angular_lower(speeds,N);maxwidth=max(maxwidth,width)
        for i,h,B,offset in info:
            ell=float(lower[offset:offset+n+1].min());loss=mul(sqrt(exact(N)),div(mul(exact(B),exact(h)),exact(2*n)))[1];bound=float(down(ell-loss))
            if bound<worst['value']:worst=dict(value=bound,cell=i,left=float(x[i]),right=float(x[i+1]),angle_lower=ell,radial_loss=float(loss),B=B)
        batch.clear();info.clear()
    for i in range(len(x)-1):
        h=sub(exact(x[i+1]),exact(x[i]));co=cell_coeff(Y[i],Y[i+1],D[i],D[i+1],DD[i],DD[i+1],h);B=derivative_bound(co,h,M);maxB=max(maxB,B)
        info.append((i,float(h[1]),B,len(batch)))
        for j in range(n+1):batch.append(horner(co,j/n))
        if len(info)>=a.batch_cells:finish()
    if batch:finish()
    core=np.asarray(data.get('original_core_coefficients',Y[0,1:M+1]))
    if core.shape!=(M,)or not np.all(np.isfinite(core)):raise ValueError('Finite full core density required')
    nu=2*np.arange(1,M+1);amp=scale(exact(core),1-nu*nu)
    rc=(np.r_[1.,amp[0]][None,:],np.r_[1.,amp[1]][None,:]);values=tr.cosine_sine(rc,Q,'cos')
    rho_loss=up(up(tr.pi_upper/Q)*sum_upper(up(nu*absolute_upper(amp))));rho_lower=float(down(values[0].min()-rho_loss))
    if sha(__file__)!=source_sha:raise ValueError('Source changed during this certificate run')
    if not np.isfinite(worst['value'])or not np.isfinite(rho_lower):raise ValueError('Nonfinite certificate bound')
    result=dict(scope=__doc__,input_sha256=sha(a.input),source_sha256=source_sha,nodal_jets_little_endian_float64_sha256=jet_sha,
        construction_angles=N,audit_angles=Q,radial_subdivisions=n,cells=len(x)-1,minimum_qN_bound=worst,rho_all_angle_lower=rho_lower,
        max_F_sphi_bound=maxB,max_qN_grid_interval_width=maxwidth,strict_under_stated_IEEE_arithmetic=True,positive=bool(worst['value']>0 and rho_lower>0),
        pi_fixed_scale=tr.F,pi_integer_lower=tr.pi_integer[0],pi_integer_upper=tr.pi_integer[1],seconds=time.perf_counter()-begin)
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True);print('report_sha256',sha(a.out),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('input','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--construction-angles',type=int,default=2048);p.add_argument('--angles',type=int,default=4096)
    p.add_argument('--radial-subdivisions',type=int,default=4);p.add_argument('--batch-cells',type=int,default=8)
    main(p.parse_args())
