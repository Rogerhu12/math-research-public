#!/usr/bin/env python3
"""R150 original U-value atlas: exact small identities and original nine equations.
This deliberately keeps f,t graph substitution out of a seven-variable
rational gcd expansion. It proves the moment atlas and linear charts,
and generates all nine equations in the original Gram coordinates.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(120)
A1,r,s,t,b,c,q,lam,h,k,w,f,rho=sp.symbols('A1 r s t b c q lam h k w f rho')
a=1-b-c
def eqzero(p):assert sp.expand(p)==0
one=[1,0,1,1]
rows=[[0,0,1,q],[0,A1,r,s],[1,r,0,t],[q,s,t,0]]
def add(v,z):return [x+y for x,y in zip(v,z)]
def scale(z,v):return [z*x for x in v]
def mul(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(mul(row,v)) for row in rows]
d=DK(one);F2=tau(d)
def P2(v):
 z=add(v,scale(-tau(v),one))
 return tau(mul(mul(z,z),z))
def N4(v):
 return 2*tau(mul(d,mul(v,v)))-F2*tau(mul(v,v))-4*tau(v)*tau(mul(d,v))+2*F2*tau(v)**2+tau(mul(v,DK(v)))
def Pjet2(v,z):
 v0=add(v,scale(-tau(v),one));z0=add(z,scale(-tau(z),one))
 return 3*tau(mul(mul(v0,v0),z0))
def Njet4(v,z):return N4(add(v,z))-N4(v)-N4(z)
ev=[tau(mul(rows[0],rows[0])),2*tau(mul(rows[0],rows[1])),tau(mul(rows[2],rows[2])),tau(mul(rows[3],rows[3]))]
E=add(add(ev,scale(-2,DK(d))),add(scale(-2,mul(d,d)),scale(2*F2,d)))
u=b+c*q;V2=b+c*q*q;V3=b+c*q**3
P02=V3-3*u*V2+2*u**3
x=r+a+c*t;y=s+a*q+b*t
eqzero(P2(rows[0])-P02)
eqzero(F2-(A1+2*b*x+2*c*y-2*b*c*t))
eqzero(E[0]-(V2-2*(b*x+c*q*y)-2*u*u+2*F2*u))
eqzero(N4(rows[0])-(2*(b*x+c*q*q*y)-F2*V2-4*u*(b*x+c*q*y)+2*F2*u*u+2*b*c*q*t))
# Complete moment charts: the generic formulas never divide by Al or Bl.
Al=2*lam**2-2*lam+1;Bl=4*lam**3-6*lam**2+3*lam-1
eqzero(Bl-(2*lam-1)*Al+lam)
assert sp.Poly(Al,lam).gcd(sp.Poly(Bl,lam)).degree()==0
hx=h-1;ky=k-1
bn=Bl-ky*Al;cn=hx*Al-Bl
eqzero(bn+cn-Al*(hx-ky))
eqzero(hx*bn+ky*cn-Bl*(hx-ky))
eqzero(lam*(2*lam-1)**2-Al-Bl)
eqzero((lam-1)*Bl-Al**2-lam**2*(1-2*lam))
# Thus every value collision has v-1=Bl/Al, total weight Al^3/Bl^2,
# and w=lambda^2(1-2lambda)/Bl, with Al*Bl != 0.
def CC(z):return 1+z+z*z-2*lam*(1+z)
eqzero(CC(h).subs(lam,sp.Rational(3,4))-(h-1)*(h+sp.Rational(1,2)))
eqzero((Bl+sp.Rational(3,2)*Al).subs(lam,sp.Rational(3,4))-sp.Rational(1,2))
VV=[1,w,h,k]
raw=(3-4*lam)*A1+2*b*CC(h)*r+2*c*CC(k)*s
raw+=2*b*c*(h*h+h*k+k*k-2*lam*(h+k))*t
raw+=2*b*(a*CC(h)+w*(2+h-2*lam))
raw+=2*c*q*(a*CC(k)+w*(2+k-2*lam))
wmean=lam-a-b*h-c*k
M2=tau(mul(VV,VV))-2*lam*lam
eqzero((N4(VV)+F2*M2-raw).subs(w,wmean))
say({'stage':'raw_original_moment_and_N_identities_verified','claimExcluded':False})
# Global E0/N0 graph, checked by original scalar row identities above.
D=2*b*c*q*(q-1)
W12=V2-2*u*u+4*f*u
W2=u*V2-2*u**3+f*(V2+2*u*u)-b*c*q*t+lam*P02
XD=c*q*(q*W12-2*W2)
YD=b*(2*W2-W12)
AD=2*f*D-2*b*XD-2*c*YD+2*b*c*t*D
eqzero(2*(b*XD+c*q*YD)-D*W12)
eqzero(b*XD+c*q*q*YD-D*W2)
eqzero(W2-f*V2-u*W12+2*f*u*u+b*c*q*t-lam*P02)
Anum=2*(q*(1-b-c)-u*(q+1-2*u))*f+(2*u-q-1)*(V2-2*u*u)+2*lam*P02
eqzero(q*AD-D*Anum)
eqzero(sp.diff(AD,t))
# Raw N(V) is linear in Gram coordinates. On the graph, A_t=F_t=0,
# r_t=c/(q-1), s_t=-b*q/(q-1), so the entire t divisor is paid here.
L=q*(h-1)-(k-1);S=h+k+1-2*lam
TT=h*h+h*k+k*k-2*lam*(h+k)
eqzero(CC(h)-q*CC(k)+(q-1)*TT-L*S)
# The S=0 identity keeps its f coefficient and constant separately.
Sraw=(h-1)*(k-1)*A1-(h+k+h*k)*F2-2*w*(b*(k-1)+c*q*(h-1))
eqzero((raw-Sraw).subs(k,2*lam-1-h))
# Original polar identities prove the complete L=0,w split.
eps=[0,1,0,0];k0=rows[0]
eqzero(N4(one))
eqzero(N4(eps)-(2*F2-4*u))
eqzero(Njet4(one,eps)-(2*u-2*F2))
eqzero(Njet4(one,k0)-(V2-2*u*u-E[0]))
eqzero(Njet4(k0,eps)-2*E[0])
VL=add(add(one,scale(rho,k0)),scale(w,eps))
Lidentity=2*F2*w*(w-1)+u*(2*w-4*w*w)+rho*(V2-2*u*u)+rho*(2*w-1)*E[0]+rho*rho*N4(k0)
eqzero(N4(VL)-Lidentity)
eqzero(P2(add(one,scale(rho,k0)))-rho**3*P02)
eqzero((sp.Rational(3,2)*(2*(lam-2)**2-Al)+3*(lam-2)+1)-(sp.Rational(11,2)-6*lam))
eqzero(4*lam*(6*lam-sp.Rational(11,2))+4*lam-3-3*(8*lam*lam-6*lam-1))
eqzero(16*((lam-2)*Bl-Al**2)-3*(7-10*lam)-(-12*lam+5)*(8*lam*lam-6*lam-1))
say({'stage':'global_E0_N0_graph_L_S_divisors_and_L0_polar_identities_verified','claimExcluded':False})
# The complete nine necessary equations are retained as original
# polynomials; no sufficient-condition or physical-realization claim.
Ps=[P02,Pjet2(rows[0],rows[1]),P2(rows[2]),P2(rows[3])]
Ns=[N4(rows[0]),Njet4(rows[0],rows[1]),N4(rows[2]),N4(rows[3])]
conditions=E[1:]+[Ps[1]-3*w*P02,Ps[2]-h**3*P02,Ps[3]-k**3*P02,Ns[1]-4*lam*w*P02,Ns[2]-2*lam*h*h*P02,Ns[3]-2*lam*k*k*P02]
labels=['E1','EB','EC','2(P1-3wP0)','2(PB-h3P0)','2(PC-k3P0)','4(N1-2lambda*wP0)','4(NB-lambda*h2P0)','4(NC-lambda*k2P0)']
gens=(A1,r,s,t,b,c,q,lam,h,k,w)
profiles=[];dig=hashlib.sha256()
for label,ex in zip(labels,conditions):
 pp=sp.Poly(sp.expand(ex),*gens,domain=sp.QQ)
 dig.update((label+'\n'+str(pp.terms())+'\n').encode())
 profiles.append({'name':label,'totalDegree':int(pp.total_degree()),'terms':len(pp.terms())})
signal.alarm(0)
say({'schema':'r150-original-U-atlas-small-identities-v1','status':'all_original_identity_and_complete_value_atlas_checks_pass','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'originalNineEquationInputSha256':dig.hexdigest(),'originalNineConditions':profiles,'newDivisors':['L=q(h-1)-(k-1)','S=h+k+1-2lambda'],'fiveCoordinateExpansionGenerated':False,'claimPhysicalSufficiency':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
