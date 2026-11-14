"""Universal rational identities for actual birth-two phase normalization.
No positivity of the general quartic is asserted. Self-contained symbolic algebra.
"""
import sympy as s
M,N,u,e,th,t=s.symbols('M N u eta theta tau')
delta=M*u-N;H=M+N
J=u*(M+1+e)-N+1;K=N+1-u*(M-1-e)
a=N-1-u*e;b=M-1-e
R=N/(M*u)-(N-1)*J*t/(M*u*a)
T=M*u/N-(M-1)*K/(N*b*t)
Du=u*(2*th-1)+((1+u)*(2*th-1)+delta)/e
De=(1-th)*K/u
Dt=th*(1-th)*(u-delta-(1+u)*th)/(e*u)
Dd=th*(1-th)*(1+u)/(e*u)
def deriv(f):return s.diff(f,u)*Du+s.diff(f,e)*De+s.diff(f,th)*Dt
r0=-(1-th)+(th*(delta+2)-1)/(e*u)
r1=-th+((u-delta)-(2*u-delta)*th)/(e*u)
f0=(J*(N+(N-1)*t)-2*u*(H-1))/(e*u)
f1=(K*(M-1+M*t)-2*(H-1)*t)/(e*t)
for f,r,v in ((f0,r0,2*M*u),(f1,r1,2*N)):
 got=v+e*u/(th*(1-th))*(Dd*r+deriv(r))
 assert s.cancel(got-f.subs(t,th/(1-th)))==0
print('UNIVERSAL_HIGHER_CURVATURE_DIFFERENTIATION_PASS',flush=True)
def base(mm,nn,uu,ee,tt):
 aa=nn-1-uu*ee;bb=mm-1-ee;jj=uu*(mm+1+ee)-nn+1;kk=nn+1-uu*bb
 rr=nn/(mm*uu)-(nn-1)*jj*tt/(mm*uu*aa)
 zz=mm*uu/nn-(mm-1)*kk/(nn*bb*tt)
 return aa,bb,jj,kk,rr,zz
minus=(M+1,N-1,u*(N-1)*R/a,u*e*M/(N-1),(N-1)*t/(a*R))
plus=(M-1,N+1,u*b/((M-1)*T),e*N*T/(u*b),b*T*t/(M-1))
pm=base(*minus);pp=base(*plus)
assert s.cancel(pm[5]-R)==0
assert s.cancel(pp[4]-T)==0
assert s.cancel(plus[2]*plus[3]-N*e/(M-1))==0
assert s.cancel(pm[1]-M*a/(N-1))==0
print('UNIVERSAL_BOTH_PHASE_STEPS_PASS',flush=True)
def pair(mm,nn,uu,ee,tt):
 aa,bb,jj,kk,rr,zz=base(mm,nn,uu,ee,tt)
 return ((jj*(nn+(nn-1)*tt)-2*uu*(mm+nn-1))/(ee*uu),
 (kk*(mm-1+mm*tt)-2*(mm+nn-1)*tt)/(ee*tt))
fm=s.cancel(M*u/(N-1)*pair(*minus)[0])
fp=s.cancel(N*T/(u*b)*pair(*plus)[1])
n=N-2;m=M-2
assert s.cancel(R*fm-f0-n*t*(R*f1-f0)/(u*R*(m+1)))==0
assert s.cancel(f1-T*fp-m*u*(f1-T*f0)/(t*(n+1)*T))==0
print('UNIVERSAL_NORMALIZED_TWO_DIRECTION_PEARSON_PASS',flush=True)
a0,c0,d0,p0,r0,s0,xx,yy,w=s.symbols('a c d p r ss x y w')
bm=w*p0/(p0+w);bb=w*r0/(1+w*r0);bp=w*r0*s0/(r0+w*s0)
hm=s.Matrix([[a0+w+bm*xx**2,-bm*xx],[-bm*xx,bm]])
h0=s.diag(1+w*c0,bb)
hp=s.Matrix([[c0+w*d0+bp*yy**2,-bp*yy],[-bp*yy,bp]])
invp=s.Matrix([[1/(c0+w*d0),yy/(c0+w*d0)],[yy/(c0+w*d0),1/bp+yy**2/(c0+w*d0)]])
la=(a0*c0-1)+w*(a0*d0-c0)+w*w*(d0-c0*c0)
ff=p0*(s0-r0*r0)+w*r0*(p0*s0-r0)+w*w*r0*s0*(p0*r0-1)
pol=la*ff-w*p0*r0*(c0+w*d0)*(r0+w*s0)*xx**2-w*r0*r0*s0*(a0+w)*(p0+w)*yy**2-2*w*p0*r0*s0*(1+w*c0)*(1+w*r0)*xx*yy-w*w*p0*r0*r0*s0*xx**2*yy**2
sch=hm-h0*invp*h0
det=sch[0,0]*sch[1,1]-sch[0,1]*sch[1,0]
assert s.cancel(det*(p0+w)*(1+w*r0)**2*(c0+w*d0)*s0/w-pol)==0
print('UNIVERSAL_COMPLETE_SCHUR_QUARTIC_PASS',flush=True)
print('ALL_PASS: universal rational identities',flush=True)
