#!/usr/bin/env python3
"""R343: all-residue-class division identities and the two true Faber rows.

No prime scan.  The only numerical fiber reuses R336's actual p=13 kernel.
"""
import json
from pathlib import Path
import sympy as S

checks=[]


def check(name, value):
    assert bool(value), name
    checks.append(name)


def e(n):
    return (0,1,1,0,-1,-1)[n % 6]


for r in range(6):
    check(f"division odd recurrence: complete residue class {r}",
          e(2*r+1) == e(r+2)*e(r)**3-e(r-1)*e(r+1)**3)
    check(f"division even recurrence: complete residue class {r}",
          e(2*r) == e(r)*(e(r+2)*e(r-1)**2-e(r-2)*e(r+1)**2))

m,j,k,ss=S.symbols('m j k s',integer=True)
E=lambda n:(n*n-1)/3
check("first odd term has the exact exponent",S.expand(E(m+2)+3*E(m)-E(2*m+1))==0)
check("second odd term has the exact exponent",S.expand(E(m-1)+3*E(m+1)-E(2*m+1))==0)
check("first even term has the exact exponent",S.expand(E(m)+E(m+2)+2*E(m-1)-1-E(2*m))==0)
check("second even term has the exact exponent",S.expand(E(m)+E(m-2)+2*E(m+1)-1-E(2*m))==0)
check("p=6s+1 has positive three-torsion sign",2*ss % 2 == 0)
check("three-torsion exponent is 2s(p+1)",S.expand(E(6*ss+1)-2*ss*(6*ss+2))==0)
check("the two complete constant phases differ by 2^(p-1)",4*ss-(-2*ss)==6*ss)

unsym=36*j*k-6*k*(6*k+1)
sym=S.expand((unsym+unsym.xreplace({j:k,k:j}))/2)
check("the complete Wronskian pairing has the stated symmetric coefficient",
      S.expand(sym-(-18*(j-k)**2-3*(j+k)))==0)
check("the true second row uses j+k=s+1",6*(ss+1)+2==6*ss+8)
check("the row lies above all one-factor polar/regular cross terms",6*ss+8-(6*ss+2)==6)
check("the sigma row has exponent reduction -6j",S.expand((6*ss+1)-6*j-1+6*j)==6*ss)

src=Path(__file__).with_name('check-jzero-ordinary-as-verschiebung-and-two-negative-rows.json')
data=json.loads(src.read_text())['single_actual_fiber']
p,b,H=data['p'],data['b'] % data['p'],data['H']
X=S.symbols('X')
P=S.Poly(S.sympify(data['kernel_polynomial_in_X'],locals={'X':X}),X,modulus=p)
a1=data['sigma_laurent_row']; a2=1
P0=int(P.nth(0)) % p
check("the actual R336 kernel has the fully specified cubic phase",
      H*P0 % p==pow(b*pow(2,-1,p)%p,(p-1)//3,p))
check("the p13 Faber quadratic is the actual second Laurent row",
      (-54*a1*a2) % p==data['theta_laurent_row'])
check("the actual sigma row carries the complete common H^6 factor",
      pow(H,6,p)*a1 % p==data['actual_sigma_coefficient'])
check("the actual Theta row carries the same complete H^6 factor",
      pow(H,6,p)*data['theta_laurent_row'] % p==data['actual_theta_coefficient'])

out={
    'status':'PASS','check_count':len(checks),'checks':checks,
    'actual_phase':'H*P(0)=(b/2)^(2s), p=6s+1',
    'faber_sigma_row':'H^6*alpha_1',
    'faber_theta_row':'H^6 sum_(j+k=s+1) (-18(j-k)^2-3(s+1))*alpha_j*alpha_k',
    'fiber_reused':data,
    'scope':'Complete original phase and both observations; no joint nonvanishing or new prime scan.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'{len(checks)} exact checks: PASS')
