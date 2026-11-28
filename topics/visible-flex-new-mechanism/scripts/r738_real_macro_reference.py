"""The finite-angle R738 base immersion, in the exact material chart, with independent quadratures."""
import hashlib
import numpy as np
from r738_negative_tail_and_macro_source import A0,B0,THETA,HALFWIDTH,FIRST,RATIO,WEIGHT,stepp,bump,bounds_t

SEPARATORS=np.array([A0,.085,.09,.145,.15,.205,.21,B0])


class Base:
    def __init__(self,order,book,count):
        self.book,self.count,self.order=book,count,order
        self.X,self.W=np.polynomial.legendre.leggauss(order)
        self.near_terms={}
        s=book.once(f'r738_angular_calibration_{order}',lambda:self.angular_calibration())
        self.M=s['M'];self.right=s['right']
    def gauss(self,lo,hi,fn):
        l=np.asarray(lo);h=np.asarray(hi)
        pts=(l[...,None]+h[...,None])/2+(h-l)[...,None]*self.X/2
        return np.sum(fn(pts)*self.W,axis=-1)*(h-l)/2
    def angular_calibration(self):
        v=self.gauss(SEPARATORS[:-1],SEPARATORS[1:],lambda r:bump(r)[0]/r)
        val=np.r_[np.cumsum(v[::-1])[::-1],0.]
        self.count['true_base_angular_quadrature_nodes']+=len(v)*self.order
        return dict(M=float(THETA/val[0]),right=val)
    def omega(self,r):
        r=np.asarray(r);i=np.clip(np.searchsorted(SEPARATORS,r,side='right')-1,0,len(SEPARATORS)-2)
        local=self.gauss(r,SEPARATORS[i+1],lambda z:bump(z)[0]/z)
        w=self.M*(local+self.right[i+1])
        return np.where(r<=.085,THETA,np.where(r>=.21,0.,w))
    def center_one(self,r):
        x=z=0.
        for a,b in zip(SEPARATORS,SEPARATORS[1:]):
            lo=max(r,a)
            if lo>=b:continue
            s=(lo+b)/2+(b-lo)*self.X/2
            w=self.omega(s);q=bump(s)[0]
            x-=self.M*1.01*(b-lo)/2*np.dot(self.W,q*np.sin(w))
            z-=self.M*1.01*(b-lo)/2*np.dot(self.W,q*np.cos(w))
            self.count['true_base_center_quadrature_nodes']+=self.order
        return np.array([x,0.,z])
    def slope_segment(self,t,L):
        from r738_negative_tail_and_macro_source import H_and_derivative
        h,_=H_and_derivative(t,L);x=t*L
        return WEIGHT*np.exp((5-2*h)*np.log(x)+h*np.log(256.))
    def partial_cell(self,n,t):
        L=np.ldexp(1/512,-n);cut=bounds_t(L);s=0.
        for a,b in zip(cut,cut[1:]):
            up=min(t,b)
            if up>a:s+=L*self.gauss(a,up,lambda v:self.slope_segment(v,L))
        return s
    def slope_height(self,sign,x):
        # Below L_26 the exact missing primitive is bounded by 2 L_26^4.
        N=26;Ltiny=np.ldexp(1/512,-N)
        if x<=Ltiny:return 0.
        edge=np.ldexp(1/512,-FIRST[sign]);xx=min(x,edge)
        value=0.
        for n in range(N-1,FIRST[sign]-1,-1):
            L=np.ldexp(1/512,-n)
            if xx<=L/2:break
            if xx<L:
                value+=self.partial_cell(n,xx/L);break
            if n not in self.near_terms:
                self.near_terms[n]=self.partial_cell(n,1.)
            value+=self.near_terms[n]
        if x>edge:value+=.1*(x**5-edge**5)
        return -sign*RATIO[sign]*value
    def rows(self,r):
        r=np.asarray(r);k,kd=bump(r);p=-self.M*k;pd=-self.M*kd
        w=self.omega(r);wp=p/r;wpp=pd/r-p/r**2
        ez=np.column_stack((np.sin(w),np.zeros_like(w),np.cos(w)))
        dez=np.column_stack((np.cos(w),np.zeros_like(w),-np.sin(w)))*wp[:,None]
        c=np.stack([self.center_one(v) for v in r])
        cr=-1.01*p[:,None]*ez
        crr=-1.01*(pd[:,None]*ez+p[:,None]*dez)
        from r738_negative_tail_and_macro_source import w_actual
        eh=np.zeros((len(r),3))
        for i,v in enumerate(r):
            sign=-1 if v<(A0+B0)/2 else 1
            rim=A0 if sign==-1 else B0
            xi=abs(v-rim)
            if xi>=.01:continue
            rho=RATIO[sign];x=xi/rho
            h=self.slope_height(sign,x);ww,dw=w_actual(sign,x)
            S,D,E=stepp((xi-.008)/.002)
            cc=1-S;cp=sign*D/.002;cpp=-E/.002**2
            eh[i]=[cc*h,cc*ww+cp*h,cc*dw/rho+2*cp*ww+cpp*h]
            c[i]+=eh[i,0]*ez[i];cr[i]+=eh[i,1]*ez[i];crr[i]+=eh[i,2]*ez[i]
        t=np.tan(w/2);t0=-t;t1=-(1+t*t)*wp/2;t2=-(1+t*t)*(wpp+t*wp*wp)/2
        self.count['native_physical_base_radii']+=len(r)
        return dict(r=r,zb=np.stack((t0,t1,t2),axis=-1),center=np.stack((c,cr,crr),axis=1),
                    omega=w,reference_E=1+(2.01*p)**2+eh[:,1]**2,
                    full_true_tail_primitive_absolute_error=2*np.ldexp(1/512,-26)**4,
                    ordinary_quadrature_has_continuous_certificate=False)
    def paid(self,r):
        r=np.ascontiguousarray(r,dtype=np.float64)
        key=hashlib.sha256(r.tobytes()).hexdigest()
        return self.book.once(f'base_{self.order}_{key}',lambda:self.rows(r))
