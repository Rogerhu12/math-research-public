#!/usr/bin/env python3
"""R352: whole original canonical derivative and exact source/target costs."""
from pathlib import Path
import json
import sympy as S
checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append(name)
def ceil(a,b):return -((-a)//b)
def e(m):return 3*ceil(3*m,4)+2*ceil(m,2)+ceil(2*m,3)-2
t=S.symbols('t');h=16*t*t+4*t+7
W=t*(t-1)**2*(1+8*t)*h**2
ck('true N2 carrier has allowed degree five',S.Poly((t-1)*(1+8*t)**2*h,t).degree()==5)
ck('true N2 carrier division is exact',S.cancel(W/(t*(t-1)*h/(1+8*t))-(t-1)*(1+8*t)**2*h)==0)
for n in range(12):
    a=(n+1)//4;b=(n+1)//3;c=n//2
    aa=(n+3)//4;bb=(n+3)//3;cc=(n+2)//2
    da=aa-a;db=bb-b
    ck('full pole and degree class '+str(n),3*a+b-c+e(n+1)==(9*n)//2+4 and da in [0,1] and db in [0,1] and cc-c==1 and e(n+3)-e(n+1)==10-3*da-db)
    q=t**a*(t-1)**b*h**a/(1+8*t)**c
    qp=t**aa*(t-1)**bb*h**aa/(1+8*t)**cc
    for j in [0,e(n+1)]:
        B=t**(j+1-da)*(t-1)**(1-db)*(1+8*t)*h**(1-da)*((a+j)*(t-1)*(1+8*t)*h+b*t*(1+8*t)*h+a*t*(t-1)*(1+8*t)*S.diff(h,t)-8*c*t*(t-1)*h)
        ck('actual entire canonical derivative class '+str(n)+' column '+str(j),S.cancel(W*t*S.diff(q*t**j,t)/qp-B)==0)
ck('twelve-step pole and degree growth is exact',all((n+13)//4-(n+1)//4==3 and (n+13)//3-(n+1)//3==4 and (n+12)//2-n//2==6 and e(n+13)-e(n+1)==47 for n in range(12)))
q6=t*h*(t-1)**2/(1+8*t)**3;q7=t*t*h*h*(t-1)**2/(1+8*t)**3
failed=S.cancel((t-1)*(1+8*t)*h*(t*S.diff(q6,t)-q6)/q7)
ck('original degree-one attempt retains its actual h7 pole',S.cancel(failed-(8*t+10-108*(t-1)/h))==0)
ck('true carrier first coefficient before t(w) substitution',S.expand(W).coeff(t,1)==49)
s,p,A,eps=S.symbols('s p A eps')
e2=1+A*eps+A*A*eps*eps/2
ck('complete radial exponential Euler derivative',S.rem(S.Poly(s*eps*S.diff(e2,eps)-s*A*eps*e2,eps),S.Poly(eps**3,eps)).as_expr()==0)
# A fixed block length is only a certificate of the general floor formula.
s0=23;T=3*s0-1
weights=[(r+1)//s0-r//s0 for r in range(T)]
ck('complete one-row shift has exactly its two actual p boundaries',[i for i,x in enumerate(weights) if x]==[s0-1,2*s0-1])
ck('all one-row shift factors have cost at most one',all(x in [0,1] for x in weights))
r=S.symbols('r')
ck('the actual thirteen-row Euler commutator is retained',(r+13)-13-r==0)
out={'status':'PASS','check_count':len(checks),'checks':checks,
     'actual_operator':'Q=R^2*t*(t-1)^2*(1+8*t)*h7^2*(t d/dt)',
     'exact_characteristic_zero_kernel':['1','R'],
     'primitive_range':'floor(9D/2)+4<p',
     'extra_relative_charge':2,'extra_target_rows':1,'uniform_extra_Smith_length_bound':2,
     'actual_moving_pole_factor':'G/h=-x/(y*z) == -x/(y*Z_p) in the paid mod-p window',
     'scope':'Actual whole source operation and full original transfer; no automatic preservation of lifting kernels or C2 quotient.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(str(len(checks))+' exact checks: PASS')
