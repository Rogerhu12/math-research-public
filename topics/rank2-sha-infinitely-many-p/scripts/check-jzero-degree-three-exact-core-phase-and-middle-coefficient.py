#!/usr/bin/env python3
"""R345: actual symmetric theta lifts, all six CM residues, and the C core.

No prime scan.  The one p=13 fiber is the same original fiber as R336/R343.
"""
import json
from fractions import Fraction
from pathlib import Path
import sympy as S

checks=[]


def check(name, value):
    assert bool(value), name
    checks.append(name)


beta,a,delta=S.symbols('beta a delta',nonzero=True)
c=-delta*beta
om=(delta-1)/2
Q=S.Matrix([[-S.Rational(1,2),0,3*beta/2],
            [0,1,0],[-1/(2*beta),0,-S.Rational(1,2)]])
R=S.Matrix([[S.Rational(1,2),-a/2,c/2],
            [-1/a,0,c/a],[-1/(2*c),-a/(2*c),-S.Rational(1,2)]])
J=S.diag(-1,-1,1)


def red(f):
    nn,dd=S.fraction(S.cancel(f))
    nn=S.rem(nn,delta**2+3,delta)
    dd=S.rem(dd,delta**2+3,delta)
    return S.cancel(nn/dd)


def zero(M):
    return all(red(v)==0 for v in M)


check('actual Q lift has exact order three',zero(Q**3-S.eye(3)))
check('actual R lift has exact order three',zero(R**3-S.eye(3)))
check('actual Q lift is symmetric, not merely projective',zero(J*Q*J-Q**2))
check('actual R lift is symmetric, not merely projective',zero(J*R*J-R**2))
check('the actual commutator is omega, with the paid sign',zero(Q*R-om*R*Q))
B=S.Matrix([0,1,0])
vp=S.Matrix([-delta*beta,0,1])
vm=S.Matrix([delta*beta,0,1])
check('B is the unique U_Q eigenline one',zero(Q*B-B))
check('C-delta beta A is the omega line',zero(Q*vp-om*vp))
check('C+delta beta A is the omega-squared line',zero(Q*vm-om**2*vm))
check('the actual R translation sends B to the positive commutator line',
      zero(R*B-(-a/(2*c))*vp))

residues=[]
for aa in [1,-1]:
    for cc in [0,1,2]:
        exponent=(cc*aa) % 3
        shear=(2*exponent) % 3
        eta=aa*om**exponent
        M=S.diag(eta,aa,eta)
        W=om**shear*(Q**shear)*R
        check(f'CM residue ({aa},{cc}): Q covariance is exact',zero(M*Q-Q*M))
        check(f'CM residue ({aa},{cc}): R covariance has the correct direction',
              zero(M*R-W*M))
        check(f'CM residue ({aa},{cc}): eta is a sixth root',red(eta**6-1)==0)
        # omega=1-delta in O_K/(3), delta^2=0.  Thus eta has pair
        # (aa,-aa*exponent), and multiplication gives the full primary value.
        epair=(aa % 3,(-aa*exponent) % 3)
        primary=((aa*epair[0]) % 3,(aa*epair[1]+cc*epair[0]) % 3)
        check(f'CM residue ({aa},{cc}): pi eta is exactly one modulo three',
              primary==(1,0))
        residues.append({'pi_mod3':[aa % 3,cc],
                         'shear':shear,'eta_sign':aa,'eta_omega_exponent':exponent})

check('the six unit-root residues are distinct',
      len({(r['eta_sign'] % 3,(-r['eta_sign']*r['eta_omega_exponent']) % 3)
           for r in residues})==6)

# The reference curve is y^2=x^3+1/4; its displayed eight nonzero 3-torsion
# points lie in Q(delta).  No arithmetic-rank assertion is used.
check('reference Q coordinates are on the curve',S.Rational(1,2)**2==S.Rational(1,4))
check('reference nonkernel 3-torsion coordinates are on the curve',
      red((delta/2)**2-((-1)**3+S.Rational(1,4)))==0)
check('the reference 3-division roots are all in the CM field',
      red((-om)**3+1)==0 and red((-om**2)**3+1)==0)

data=json.loads(Path(__file__).with_name(
    'check-jzero-ordinary-as-verschiebung-and-two-negative-rows.json').read_text())
fiber=data['single_actual_fiber']
p,b0,H=fiber['p'],fiber['b'],fiber['H']
bb=b0 % p
eta_res=pow(4*bb,(p-1)//6,p)
C12=Fraction(57*b0*b0,15400)
Cres=C12.numerator*pow(C12.denominator,-1,p) % p
check('the actual original p13 C coefficient has the complete phase',
      (H-Cres) % p==eta_res)
X=S.symbols('X')
P=S.Poly(S.sympify(fiber['kernel_polynomial_in_X'],locals={'X':X}),X,modulus=p)
T=S.Poly(S.sympify(fiber['T_P'],locals={'X':X}),X,modulus=p)
Mpoly=P*T+S.Poly(3*X,X,modulus=p)*(P*T.diff()-2*P.diff()*T)
s0=(p-1)//6
middle=int(Mpoly.nth(2*s0)) % p
P0=int(P.nth(0)) % p
eps3=pow(bb,(p-1)//2,p)
check('the same actual kernel gives the correct middle Cartier coefficient',
      middle==eta_res)
check('the middle coefficient equals the complete three-torsion phase',
      middle==eps3*pow(H*P0,-1,p) % p)

# The cubic sigma coefficient is computed in the ORIGINAL u=x^-1/2
# coordinate.  Its p13 diagonal index is two, not an extra prime search.
a1=Fraction(-2*b0,5)
a2=Fraction(16*b0*b0,55)
log1=3*a1/6
log2=3*a2/12
Acubic2=log2+log1*log1/2
check('actual u-coordinate sigma-cubic diagonal is the same unit',
      Acubic2.numerator*pow(Acubic2.denominator,-1,p) % p==eta_res)

out={
    'status':'PASS','check_count':len(checks),'checks':checks,
    'Q_lift':[[str(v) for v in Q.row(i)] for i in range(3)],
    'R_lift':[[str(v) for v in R.row(i)] for i in range(3)],
    'all_CM_residue_classes':residues,
    'exact_core':{
        'A=sigma^3':'eta_p',
        'B=x sigma^3':'epsilon^3',
        'C=y sigma^3':'eta_p',
        'eta_p':'the unique unit in mu_6 with pi*eta_p=1 mod 3',
        'reference':'eta_p=psi_(1/4)(mathfrak p)/psi_b(mathfrak p)',
        'residue':'eta_p=(4b)^((p-1)/6) mod mathfrak p',
    },
    'actual_p13':{'eta':eta_res,'C_coefficient':Cres,'middle':middle,
                  'lambda_residue':eta_res*pow(H,-1,p)%p,
                  'C_unit_mass_residue':-(1-eta_res*pow(H,-1,p))%p},
    'scope':'Full original low-source core and all ordinary unit masses. No claim that the target S central derivative is nonzero.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'{len(checks)} exact checks: PASS')
