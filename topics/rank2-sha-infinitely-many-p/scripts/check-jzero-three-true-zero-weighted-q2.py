#!/usr/bin/env python3
"""R322: fixed exact identities for the actual weighted three-source lattice.

No target-prime scan; all-prime saturation is proved in the accompanying text.
"""
import json
from pathlib import Path
import sympy as s

t, R, ep, pp, ap = s.symbols('t R ep p a_p')
checks = []


def check(name, expression):
    assert s.cancel(expression) == 0, name
    checks.append(name)


def factored_integer(n):
    return {str(k): int(v) for k, v in s.factorint(int(n)).items()}


h7 = 16*t**2 + 4*t + 7
g2 = 8*t**2 + 20*t - 1
a = t*(t-1)*h7
f4 = 512*t**4-2048*t**3+1344*t**2-536*t-1
f6 = 4096*t**6-33792*t**5+204288*t**4-47936*t**3+11040*t**2+84*t+1
f3d = 64*t**3-48*t**2+228*t-1
f4d = 1792*t**4-3136*t**3+2112*t**2-40*t+1
tau2 = 64*t*(1-t)**3/(1+8*t)**3
tau3 = -27*t/(1-4*t)**3
R2 = (1+8*t)**10*((1+8*t)**3+512*t*(1-t)**3)
R3 = (1-4*t)**14*((1-4*t)**3-216*t)/(1+8*t)**3
betanum = 27*t*(t-1)*(4*t-1)**2*h7*f3d*f4d
gammanum = -64*t*(t-1)**3*h7*g2**2*f4*f6
beta, gamma = betanum/(1+8*t), gammanum/(1+8*t)**2
check('actual norm-three angular source', R3*a.subs(t,tau3)-beta)
check('actual doubling angular source', R2*a.subs(t,tau2)-gamma)

nf = 27*(4*t-1)**2*f3d*f4d
df = t**2*(t-1)**2*(1+8*t)*h7**2
nh = -64*g2**2*f4*f6
dh = t**3*(t-1)*(1+8*t)**2*h7**3
check('actual degree-nine angular ratio', beta/a**3-nf/df)
check('actual degree-fourteen angular ratio', gamma/a**4-nh/dh)
resf = s.resultant(nf, df, t)
resh = s.resultant(nh, dh, t)
check('degree-nine resultant', resf-2**90*3**118)
check('degree-fourteen resultant', resh-2**288*3**189*7)
Q = t*(t-1)*(1+8*t)*h7
disc = s.discriminant(Q,t)
check('finite pole support discriminant', disc+2**12*3**19*7**2)
assert (s.degree(nf,t),s.degree(df,t)) == (9,9)
assert (s.degree(nh,t),s.degree(dh,t)) == (14,12)
checks.append('exact map degrees nine and fourteen')
assert s.gcd(9,14) == 1
checks.append('coprime degrees imply full parameter field')
for name, num, den, pole in [('f',nf,df,0),('h',nh,dh,2)]:
    assert s.degree(s.gcd(num,den),t) == 0
    assert s.degree(num,t)-s.degree(den,t) == pole
    checks.append(name+' exact finite gcd and infinity order')

for name, expr, coefficient in [('A',a,-7),('B',beta,189),('C',gamma,-448)]:
    check(name+' true angular linear term', s.diff(expr,t).subs(t,0)-coefficient)
    check(name+' zero mass', expr.subs(t,0))
assert (s.degree(a,t),s.degree(betanum,t),s.degree(gammanum,t)) == (4,13,20)
checks.append('three exact numerator degrees')

def e2(v):
    return 1+v+v*v/2


for m in (1,3,4,9):
    check('charge exponent %s' % m,
          s.Poly(s.expand(e2(ap*ep)**m-e2(m*ap*ep)),ep).rem(s.Poly(ep**3,ep)).as_expr())

v = s.symbols('v')
z00,z01,z02,z10,z11,z20 = s.symbols('z00 z01 z02 z10 z11 z20')
raw = z00+z01*v+z02*v*v + ap*ep*(z10+z11*v)+ap**2*ep**2*z20/2
carried = s.expand(raw.subs(v,pp*ep))
check('first integer block', carried.coeff(ep,0)-z00)
check('second integer block retains first carry', carried.coeff(ep,1)-(ap*z10+pp*z01))
check('third integer block retains both carries',
      carried.coeff(ep,2)-(ap**2*z20/2+pp*ap*z11+pp**2*z02))
jet = s.Matrix([[1,1,1],[ap,3*ap,4*ap],[ap**2/2,9*ap**2/2,8*ap**2]])
check('actual three-source unit radial minor', jet.det()-3*ap**3)

# The four residue cases prove the denominator budget; these small fixed
# instances also check the enumeration used to construct finite matrices.
budgets = []
for D in range(13):
    mons = [(i,j,k) for k in range(D//4+1)
            for j in range((D-4*k)//3+1)
            for i in range(D-4*k-3*j+1)]
    bound = 2*(D//4)+(1 if D%4 == 3 else 0)
    assert max(j+2*k for i,j,k in mons) == bound
    assert all(4*(i+3*j+4*k)+2*k+bound <= 5*D for i,j,k in mons)
    budgets.append({'D':D,'denominator_exponent':bound,'number_of_raw_columns':len(mons)})
checks.append('four-case common denominator and polynomial degree budgets')

answer = {
    'status':'PASS', 'number_of_exact_checks':len(checks), 'checks':checks,
    'source_weights':[1,3,4],
    'polynomials':{name:str(s.expand(pol)) for name,pol in
                   [('a',a),('h7',h7),('g2',g2),('f4',f4),('f6',f6),
                    ('f3delta',f3d),('f4delta',f4d),
                    ('beta_numerator',betanum),('gamma_numerator',gammanum)]},
    'ratios':{'f_numerator':str(s.expand(nf)),'f_denominator':str(s.expand(df)),
              'h_numerator':str(s.expand(nh)),'h_denominator':str(s.expand(dh))},
    'resultant_f_factors':factored_integer(resf),
    'resultant_h_factors':factored_integer(resh),
    'pole_support_discriminant_factors':factored_integer(disc),
    'pole_orders_f':[2,0,2,1,2,2],
    'pole_orders_h':[3,2,1,2,3,3],
    'radial_minor':'3*a_p**3', 'small_fixed_budget_checks':budgets,
    'scope':'Fixed exact identities only. All-prime saturation and all-degree kernel formulas are proved in R322.'
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
print('PASS: %s exact checks; %s' % (len(checks),out.name))
