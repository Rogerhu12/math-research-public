"""Exact all-profile coefficient certificate for the Gaussian star transition.

No finite-dimensional or floating-point substitution is made.  The formal
weighted moment functional and the half-line moment recurrence are retained.
The companion Markdown proof defines every matrix and projection below.
"""
import sympy as s
x,y,chi,u,k3,k4,k5,k6,lam=s.symbols('x y chi u k3 k4 k5 k6 lam')
mom={0:s.Integer(1),1:s.Integer(1),2:1+chi,3:1+3*chi+k3,4:1+6*chi+4*k3+k4,5:1+10*chi+10*k3+5*k4+k5,6:1+15*chi+20*k3+15*k4+6*k5+k6}
def simp(p):return s.cancel(p)
def E(p):
 p=s.Poly(s.expand(p),x)
 return simp(sum(c*mom[k[0]] for k,c in p.terms()))
def canon(D,O):return s.expand(D),s.expand(sum(c*f*g.subs(x,y) for c,f,g in O))
def make(D,O):
 D,O=canon(D,O) if isinstance(O,list) else (s.expand(D),s.expand(O))
 pp=s.Poly(O,x,y)
 return D,[(simp(c),x**i,x**j) for (i,j),c in pp.terms() if c!=0]
def add(*aa):return make(sum(a[0] for a in aa),sum((a[1] for a in aa),[]))
def sc(c,a):return make(c*a[0],[(c*b,f,g) for b,f,g in a[1]])
def out(f,g):return (0,[(s.Integer(1),s.expand(f),s.expand(g))])
def dg(f):return s.expand(f),[]
def tr(a):return a[0],[(c,g,f) for c,f,g in a[1]]
def aw(a,p):return simp(a[0]*p+sum(c*f*E(g*p) for c,f,g in a[1]))
def star(a,b):
 da,oa=a;db,ob=b;c0=1/u
 D=c0*da*db/x;O=[(-c0,da,db)]
 for c,h,k in ob:O +=[(c0*c,da*h/x,k),(-c0*c*E(h),da,k)]
 for c,f,g in oa:O +=[(c0*c,f,g*db/x),(-c0*c*E(g),f,db)]
 for c,f,g in oa:
  for e,h,k in ob:O +=[(c0*c*e*(E(g*h/x)-E(g)*E(h)),f,k)]
 return make(D,O)
def hnormal(n):
 if n==0:return s.Integer(1)
 if n==1:return u
 return ((n-1)*hnormal(n-2)-lam*hnormal(n-1))/chi
def mus(n):
 a=hnormal(n)
 ew1=lam*chi*hnormal(2)+k3*hnormal(3)/3
 en1=lam*chi*hnormal(n+2)+k3*hnormal(n+3)/3
 def ew2(j):
  return (-lam**2*(1+chi)*hnormal(j+2)/2-lam*(k3+chi)*hnormal(j+3)-k4*hnormal(j+4)/4
          +lam**2*chi**2*hnormal(j+4)/2+lam*chi*k3*hnormal(j+5)/3+k3**2*hnormal(j+6)/18)
 b=en1-a*ew1
 c=ew2(n)-a*ew2(0)-ew1*b
 return list(map(simp,[a,b,c]))
ms={j:mus(j) for j in range(1,5)}
v=ms[2][0]-u*u
v1=ms[2][1]-2*u*ms[1][1]
v2=ms[2][2]-2*u*ms[1][2]-ms[1][1]**2
v12=ms[3][0]-u*ms[2][0]
v121=ms[3][1]-u*ms[2][1]-ms[1][1]*ms[2][0]
v22=ms[4][0]-ms[2][0]**2
v221=ms[4][1]-2*ms[2][0]*ms[2][1]
v13=hnormal(4)-u*hnormal(3)
v23=hnormal(5)-hnormal(2)*hnormal(3)
c=x-1;zc=x*c
G2=sc(v,out(x,x))
G3=add(dg(u*x),sc(v1-2*lam*v,out(x,x)),sc(-v12,add(out(x,zc),out(zc,x))))
G4=add(dg((ms[1][1]-lam*u)*x-ms[2][0]*x*(2*x-1)),sc(v2-2*lam*v1+lam**2*v+2*lam*v12,out(x,x)),sc(-v121+3*lam*v12,add(out(x,zc),out(zc,x))),sc(v22,out(zc,zc)),sc(v13,add(out(x,x*c*c),out(x*c*c,x))))
G5=add(dg((ms[1][2]-lam*ms[1][1])*x-ms[2][1]*x*(2*x-1)+ms[3][0]*x*(3*x*x-4*x+1)+lam*ms[2][0]*x*(4*x-1)),sc(v221-4*lam*v22,out(zc,zc)),sc(-v23,add(out(zc,x*c*c),out(x*c*c,zc))))
wp=1+(v12/u)*(c-chi)
sig1=E(wp*aw(G3,wp))
def K1(a,b):return add(sc(1/v,out(aw(a,wp),aw(tr(b),wp))),sc(-1,star(star(a,G4),b)))
def K2(a,b):
 av=aw(a,wp);bv=aw(tr(b),wp)
 return add(star(star(star(a,G4),G4),b),sc(-1,star(star(a,G5),b)),sc(-1/v,add(out(aw(star(a,G4),wp),bv),out(av,aw(star(tr(b),G4),wp)))),sc(-sig1/v**2,out(av,bv)))
# Ratios of exact current moments; their density corrections are retained.
inv1=[1/u,-ms[1][1]/u**2,ms[1][1]**2/u**3-ms[1][2]/u**2]
ratio21=[simp(sum(ms[2][j]*inv1[k-j] for j in range(k+1))-ms[1][k]) for k in range(3)]
t20=simp(ms[3][0]/u-ms[2][0])
t21=simp(ms[3][1]/u-ms[3][0]*ms[1][1]/u**2-ms[2][1])
t30=simp(ms[4][0]/u-ms[3][0])
R1=-ratio21[0]*x*c
R2=-ratio21[1]*x*c+lam*ratio21[0]*x*(2*x-1)+t20*x*c*c
R3=-ratio21[2]*x*c+lam*ratio21[1]*x*(2*x-1)-lam**2*ratio21[0]*x*x+t21*x*c*c-lam*t20*x*c*(3*x-1)-t30*x*c**3
S1=R1/x;S2=(R2+lam*R1)/x;S3=(R3+lam*R2+lam**2*R1)/x
alpha_m1=lam+chi*u
ew1=lam*chi*hnormal(2)+k3*hnormal(3)/3
ew2=(-lam**2*(1+chi)*hnormal(2)/2-lam*(k3+chi)*hnormal(3)-k4*hnormal(4)/4+lam**2*chi**2*hnormal(4)/2+lam*chi*k3*hnormal(5)/3+k3**2*hnormal(6)/18)
alpha0=-alpha_m1*ew1
alpha1=alpha_m1*(ew1**2-ew2)
hm1=1/u-alpha_m1
h0=-ms[1][1]/u**2-1-alpha0
h1=ms[1][1]**2/u**3-ms[1][2]/u**2-alpha1
rh2=simp(R1/hm1)
rh3=simp(R2/hm1-h0*R1/hm1**2)
rh4=simp(R3/hm1-h0*R2/hm1**2+(h0*h0/hm1**3-h1/hm1**2)*R1)
m1=u*x;m2=(ms[1][1]-lam*u)*x-ms[2][0]*x*c;m3=(ms[1][2]-lam*ms[1][1])*x-ms[2][1]*x*c+lam*ms[2][0]*x*(2*x-1)+ms[3][0]*x*c*c
a1=-lam*x-x*m1;a2=-x*m2+lam*x*m1
b1=u;b2=m2/x+lam*u;b3=m3/x+lam*m2/x+lam**2*u
A2=add(dg(x),out(x,rh2))
A3=add(dg(a1),out(a1,rh2),out(x,rh3))
A4=add(dg(a2),out(a2,rh2),out(a1,rh3),out(x,rh4))
B2=sc(-1,out(S1,b1))
B3=add(dg(b1),sc(-1,add(out(S1,b2),out(S2,b1))))
B4=add(dg(b2),sc(-1,add(out(S1,b3),out(S2,b2),out(S3,b1))))
ar0=simp(alpha_m1/hm1)
ar1=simp(alpha0/hm1-alpha_m1*h0/hm1**2)
J1=add(out(1,m1),out(1,S1),star(A2,B2))
J2=add(out(1,m2),sc(-1,out(m1,m1)),sc(-1,G2),dg(-1),sc(ar0,out(m1,m1)),out(1,S2),sc(-1,out(m1,S1)),star(A2,B3),star(A3,B2),K1(A2,B2))
D1,O1=canon(*J1)
j0=(2*chi*u*u+lam*u-1)/(chi*u)
assert simp(D1)==0 and simp(O1-j0*y)==0
print('J1 = j0 * 1 x*',flush=True)
D2,O2=canon(*J2)
j2=(u*u-v)/(chi*v)-2*u*u
P2=s.Poly(O2,x,y)
assert simp(D2)==0
assert simp(P2.coeff_monomial(x*y)-j2)==0
assert all(simp(co)==0 for (i,j),co in P2.terms() if i!=0 and (i,j)!=(1,1))
print('J2 = 1 r* + j2 * x x*',flush=True)
J3=add(out(1,m3),sc(-1,add(out(m1,m2),out(m2,m1))),sc(-1,G3),sc(ar0,add(out(m1,m2),out(m2,m1))),sc(ar1,out(m1,m1)),out(1,S3),sc(-1,add(out(m1,S2),out(m2,S1),out(rh2,m1))),star(A2,B4),star(A3,B3),star(A4,B2),K1(A2,B3),K1(A3,B2),K2(A2,B2))
D3,O3=canon(*J3)
# Deep output annihilates 1,z; contrast input annihilates z.
P=s.Poly(O3,x,y)
deep=sum(simp(co)*x**i*y**j for (i,j),co in P.terms() if i>=2 and j!=1)
assert simp(D3+j0*x)==0
assert simp(deep)==0
print('J3 diagonal = -j0 * x',flush=True)
print('J3 projected outer = 0',flush=True)
print('All complete-source coefficient identities hold exactly.',flush=True)

