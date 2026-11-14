# Exact polynomial certificate for the q=3, delta=0 two-dimensional primitive block.
# Requires Python 3 and python-flint. All coefficient arithmetic is integer arithmetic.
# Run this file directly. No numerical sampling or unbounded parameter extrapolation is used.
from math import comb

from flint import fmpz_mpoly_ctx
ctx=fmpz_mpoly_ctx.get(('x','y','z'),ordering='lex')
x,y,z=ctx.gens()
P=lambda v:ctx.from_dict({(0,0,0):int(v)})
xx,yy,zz=x,y,z
one=P(1);zero=P(0)
def rising(v,k):
 out=one
 for i in range(k):out*=v+P(i)
 return out
bs=[];ms=[];es=[];ts=[]
for i in range(4):
 weights=[P(comb(3,k))*zz**k*rising(xx+one,i+k)*rising(yy+one,6-i-k) for k in range(4)]
 b=sum(weights,zero);m=sum((P(k)*v for k,v in enumerate(weights)),zero);e=sum((P(k*k)*v for k,v in enumerate(weights)),zero)
 bs.append(b);ms.append(m);es.append(e);ts.append(b*e-m*m)
p,q,r,t=bs;A,B,C,D=ts;m0,m1,m2,m3=ms
X=m0*q*r-2*m1*p*r+m2*p*q
Y=-m1*r*t+2*m2*q*t-m3*q*r
V0=q*t-r*r;V1=p*t-q*r;V2=p*r-q*q
def report(label,N):
 terms=list(N.terms());positive=sum(c>0 for _,c in terms);negative=[(m,str(c)) for m,c in terms if c<0]
 print(label,'terms',len(terms),'positive',positive,'negative',len(negative),'degree',N.total_degree(),flush=True)
 assert not negative,(label,negative[:5])
 expected={'P1':(24201,86),'P2':(42086,104),'P3':(24201,86),'P1 x shifted by minus one':(17145,86),'P2 x shifted by minus one':(29718,104),'P3 x shifted by minus one':(17591,86)}
 assert (len(terms),N.total_degree())==expected[label],(label,len(terms),N.total_degree())

print('Building P1 numerator',flush=True)
N1=(q*q*r*t*A*C-p*r*r*t*B*B)*V1+(p*q*q*r*A*D-p*p*q*t*B*C)*V0-q*t*C*X*X-p*r*A*Y*Y-2*p*t*B*X*Y
report('P1',N1)
print('Building P2 numerator',flush=True)
N2=A*(C*p*q*q*r**3*t*t-C*q**4*r*r*t*t+D*p*q**3*r**3*t-D*q**4*r**4-Y*Y*q*q*r*r)+B*B*(-p*p*r**4*t*t+p*q*q*r**3*t*t)+B*(-C*p*p*q*q*r*r*t*t+C*p*q**3*r**3*t+D*p*p*q**3*r*r*t-D*p*p*q*q*r**4-2*X*Y*p*r*r*t-Y*Y*p*p*r*r)+C*C*(-p*p*q**4*t*t+p*p*q**3*r*r*t)+C*(-X*X*q*q*t*t-2*X*Y*p*q*q*t)-D*X*X*q*q*r*r-X*X*Y*Y
report('P2',N2)
print('Building P3 numerator',flush=True)
N3=(q*r*r*t*A*D-p*r*t*t*B*C)*V2+(p*q*r*r*B*D-p*q*q*t*C*C)*V1-q*t*D*X*X-p*r*B*Y*Y-2*p*t*C*X*Y
report('P3',N3)
for label,N in [('P1',N1),('P2',N2),('P3',N3)]:
 translated=N.compose(x-1,y,z)
 report(label+' x shifted by minus one',translated)
 terms=list(translated.terms());order=min(m[0] for m,c in terms)
 edge=[(m,c) for m,c in terms if m[0]==order]
 assert order==({'P1':8,'P2':10,'P3':8}[label])
 assert len(edge)==({'P1':759,'P2':1106,'P3':715}[label])
 assert all(c>0 for m,c in edge) and any(m[1]==0 and c>0 for m,c in edge)
 print(label,'x+1 vanishing order',order,'positive edge terms',len(edge),'y0 anchor',[(m,str(c)) for m,c in edge if m[1]==0][:2],flush=True)

print('PASS: three positive quartic coefficients, all interior parameters and the exact lower edge',flush=True)
