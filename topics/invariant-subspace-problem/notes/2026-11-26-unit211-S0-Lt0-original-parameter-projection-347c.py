#!/usr/bin/env python3
"""R150 S0, original P1 t coefficient zero: exact parameter projection.
Only algebraic identities and necessary parameter factors are reported.
No factor, zero leading coefficient, or new parameter curve is discarded.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
started=time.perf_counter()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(300)
ctx=fmpq_mpoly_ctx.get(('lam','z','theta'),'lex')
la,z,th=ctx.gens();zero=ctx.constant(0)
s=2*la-3;A=2*la*la-2*la+1;C=-4*la*la+5*la-2;R=3-4*la
D=s*C-A*z;Delta=s*s-4*z;B=2*C*z-D*s
U=D+th*B;V=U-z*z;Q=1-th*th*Delta
# u=U/z^2, l=D/z^2, T=C/z, w=W/z.
W=(la-1)*z-C;E=D+C*z
# G=z^4*Lt/(bc). No division by its theta leading coefficient.
G=z*z*(z*z-D)*Q-2*V*(V-z*z)
Traw=z*z*(2*U-D*Q)-2*U*U
Tn=-4*V-z*z*Q
assert Traw-z*z*Tn==G
Praw=(2*z*z-3*U)*(2*U-D*Q)*z*z-Q*U*z**4+2*U**3
assert Praw-2*D*Q*V*z*z==-U*G
assert z*z*(D-z*z)*Q+2*U*(z*z-U)==-G-4*V*V
# Cross=b*p*(k-1)+c*q*(h-1)=Y/(2z^2).
Y=2*(D*s-C*z)+th*(B*s-D*Delta)
# On G=0 this is z^7 times Q/v times the compatibility of
# the original P1 line with the original N(V) line. v=u-1 is already paid.
K=z**3*(R-z)*(-Tn*Tn+2*D*E*Q*Q-2*la*D*Q*Tn)+8*D*E*Q*V*V-2*V*Tn*W*Y
def degree(p,j):return max((int(m[j]) for m in p.to_dict()),default=-1)
def profile(p):return {'degrees':[degree(p,j) for j in range(3)],'terms':len(p.to_dict())}
def co(p,j):
 return ctx.from_dict({(int(m[0]),int(m[1]),0):v for m,v in p.to_dict().items() if int(m[2])==j})
def serialized(p):
 t=str(p)
 return {'profile':profile(p),'polynomial':t if len(t)<=8000 else None,'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
def factor_report(p):
 content,ff=p.factor()
 return {'content':str(content),'factors':[{'exponent':int(e),**serialized(f)} for f,e in ff]}
rem=K;steps=0;lc=co(G,2)
while degree(rem,2)>=2:
 n=degree(rem,2);rr=co(rem,n)
 rem=lc*rem-rr*th**(n-2)*G;steps+=1
r0=co(rem,0);r1=co(rem,1);common=r0.gcd(r1)
sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say({'stage':'exact_original_parameter_identities_and_pseudoremainder','sourceSha256':sha,'LtPolynomial':profile(G),'compatibilityPolynomial':profile(K),'pseudoSteps':steps,'linearRemainder':[profile(r0),profile(r1)],'commonRemainderFactorization':factor_report(common),'linearCoefficientsAfterCommon':[serialized(r0/common),serialized(r1/common)],'claimExcluded':False})
res=G.resultant(K,'theta')
assert degree(res,2)<=0
say({'schema':'r150-unit211-S0-Lt0-parameter-projection-v1','status':'exact_original_necessary_parameter_factors_generated','sourceSha256':sha,'originalResultantFactorization':factor_report(res),'unpaidBranchesRetained':True,'claimExcluded':False,'claimS0LayerEmpty':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
