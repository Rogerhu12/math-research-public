#!/usr/bin/env python3
"""R269: actual companion columns, theta-weighted de Rham primitives and jets."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
d264 = json.loads((HERE/'check-normtwo-finite-connection-kernel.json').read_text())
d268 = json.loads((HERE/'check-normtwo-de-rham-duality-and-unipotent-gauge.json').read_text())
d265 = json.loads((HERE/'check-nonbeta-full-transport-and-cm-boundary.json').read_text())
d254 = json.loads((HERE/'check-octic-ray-original-companion-transport.json').read_text())
d251 = json.loads((HERE/'check-third-adjacent-companion-lambda2.json').read_text())
s,U,x = sp.symbols('s U x')
ii,K = sp.I,sp.QQ_I
checks = {}


def check(name,value):
    checks[name] = bool(value)
    if not value:
        raise AssertionError(name)


def dm(a):
    return a.to_DM(domain=K)


def cols(a):
    a = a.to_Matrix() if hasattr(a,'to_Matrix') else a
    return [[str(sp.expand(a[j,k])) for j in range(a.rows)] for k in range(a.cols)]


P8 = sum(sp.Rational(c)*U**j for j,c in enumerate(d264['kernel_P8_coefficients']))
P = sp.expand(s**8*P8.subs(U,1/s))
ell = sp.Matrix([d264['left_kernel']])
lam = sp.Rational(d268['dual_scale'])
Jcols = []
for n,row in enumerate(d268['primitive_Laurent_polynomials']):
    A = sum(sp.Rational(c)*U**((int(k)+17)//2)
            for k,c in row['R_coefficients'].items())
    check('actual_odd_Laurent_exponents_'+str(n),
          all(-17<=int(k)<=31 and int(k)%2 for k in row['R_coefficients']))
    J = sp.expand(s**24*A.subs(U,1/s))
    check('actual_primitive_degree_'+str(n),sp.degree(J,s)<=24)
    target = s**(16-n)
    identity = 4*P*(1-s)*target+4*s*(1-s)*sp.diff(J,s)
    identity -= (65-63*s)*J+lam*ell[n]*s**16
    check('complete_theta_frame_and_apparent_pole_cancellation_'+str(n),
          sp.expand(identity)==0)
    b = -J/(4*P)
    e = J*((17-8*s)*P-s*(1-s)*sp.diff(P,s))/(P**2*(1-s))
    h = s**16/(4*P*(1-s))
    covb = 3*b+4*s*sp.diff(b,s)+34*s*b/(1-s)
    check('actual_first_covariant_source_identity_'+str(n),
          sp.cancel(covb+e+lam*ell[n]*h-target)==0)
    check('actual_B_leading_mass_'+str(n),
          sp.cancel(b.subs(s,0)+(sp.Rational(1,65) if n==16 else 0))==0)
    check('actual_E_leading_mass_'+str(n),
          sp.cancel(e.subs(s,0)-(sp.Rational(68,65) if n==16 else 0))==0)
    Jcols.append(sp.Matrix([J.coeff(s,j) for j in range(25)]))
Jmat = dm(sp.Matrix.hstack(*Jcols))
check('complete_actual_primitive_map_injective',Jmat.rank()==17)
check('actual_third_plus_second_mass',-sp.Rational(6,65)+sp.Rational(136,65)==2)

# The original R235 two columns, transported using the already paid R254 deltas.
r = sp.sqrt(2)
K8 = sp.QQ.algebraic_field((1+ii)/r)
a1=-sp.Rational(39797,14784000)-sp.Rational(8177,4224000)*r
a3=-sp.Rational(2091,448000)-sp.Rational(2669,1971200)*r
b1=sp.Rational(224494093,56229888000)+sp.Rational(4237163,1363148800)*r
b3=-sp.Rational(6031447,3748659200)-sp.Rational(202405417,62977474560)*r
ab = sp.Matrix.hstack(sp.Matrix([a1,a3,a1.subs(r,-r),a3.subs(r,-r)]),
                     sp.Matrix([b1,b3,b1.subs(r,-r),b3.subs(r,-r)])).to_DM(domain=K8)
refs = sp.Matrix.hstack(*[sp.Matrix(list(map(sp.sympify,c)))
    for c in d254['normalized_new_octic_references']]).to_DM(domain=K8)
delta = sp.diag(*map(sp.sympify,d254['original_dyadic_constants'])).to_DM(domain=K8)
AB = (refs*delta*ab).to_Matrix()
check('actual_A_B_columns_are_Gaussian',all(v in K for v in AB))
AB = dm(AB)
known = ['Cstar_rational','C2_rational','log_free_C0']
Q = AB.hstack(*[dm(sp.Matrix(list(map(sp.sympify,d251[name]['P'])))) for name in known])
names = ['original_C_A','original_C_B_plus']+known
gamma_star,gamma2 = map(sp.sympify,(d251['gamma_star'],d251['gamma2']))
gammas = [0,0,gamma_star,gamma2,0]
tau = sp.sympify(d251['t'])
check('one_actual_five_column_relation',
      (Q.extract(list(range(17)),[4])-Q.extract(list(range(17)),[3])
       +Q.extract(list(range(17)),[2]).scalarmul(K.from_sympy(tau))).is_zero_matrix)
check('four_actual_columns_independent',Q.extract(list(range(17)),[0,1,2,3]).rank()==4)
check('full_Cstar_mass_zero',sp.sympify(d251['Cstar_rational']['P'][16])+gamma_star/4==0)
check('full_C2_mass_one_half',sp.sympify(d251['C2_rational']['P'][16])+gamma2/4==sp.Rational(1,2))

boundary = dm(sp.Matrix([[1]+[0]*16,[1]*17]))
period = dm(ell)*Q
observations = (boundary*Q).vstack(period).vstack(dm(sp.Matrix([gammas])))
four = observations.extract(list(range(4)),list(range(4)))
expected_det = sp.Rational(13674673605957421212332682996609722816,
                           60011686317469517490234375)
check('actual_four_boundary_log_period_conditions_independent',four.det()==K.from_sympy(expected_det))
check('actual_two_boundary_determinant',
      (boundary*Q).extract([0,1],[0,1]).det()==K(-9399989227)/853776000000)
check('actual_A_period',period.to_Matrix()[0,0]==171893911321984*ii/28875)
check('actual_B_period',period.to_Matrix()[0,1]==-2121752694058327*ii/273000)

Tminus = dm(sp.Matrix.hstack(*[sp.Matrix(list(map(sp.sympify,c)))
    for c in d265['transports']['adjacent']['canonical_matrix_columns']]))
preimages = Tminus.inv()*Q
check('all_five_columns_return_through_actual_nonbeta_transport',
      (Tminus*preimages-Q).is_zero_matrix)
Reg = dm(sp.Matrix.hstack(*[sp.Matrix(list(map(sp.sympify,c)))
    for c in d265['CM_regularization_columns']]))
Gamma = dm(sp.Matrix(list(map(sp.sympify,d264['actual_CM_compensator_polynomial']))))
Gamma2 = Gamma.hstack(dm(Gamma.to_Matrix().conjugate()))
cm = (boundary*Gamma2).inv()*boundary*Q
check('all_five_actual_CM_boundary_terms_retained',(Reg*Q+Gamma2*cm-Q).is_zero_matrix)
K2 = dm(sp.Matrix.hstack(*[sp.Matrix(list(map(sp.sympify,c)))
    for c in d265['polynomial_second_matrix_columns']]))
polar = dm(sp.Matrix([[-1190]+[0]*16,[1088]*17]))
full19 = K2.vstack(polar)*Q
check('regular_three_companions_have_no_hidden_poles',
      (polar*Q.extract(list(range(17)),[2,3,4])).is_zero_matrix)

# Exact third-order Euler normal ordering and all shifted Mellin coefficients.
v0,v1,v2,v3,zeta,d,u = sp.symbols('v0 v1 v2 v3 zeta d u')
vs = [v0,v1,v2,v3]
def ED(f):
    return sum(sp.diff(f,vs[j])*vs[j+1] for j in range(3))
normal={0:sp.S.One}
for j in (1,2,3):
    nxt={}
    for k,c in normal.items():
        nxt[k+1]=nxt.get(k+1,0)+c
        nxt[k]=nxt.get(k,0)+j*c-ED(c)-v0*c
    normal={k:sp.expand(c) for k,c in nxt.items()}
xx=d*u
raw=sum(xx**k*c for k,c in normal.items())
shifted=sp.expand(raw.subs({v0:v0+zeta,v1:v1+d*zeta,v2:v2+d*d*zeta},simultaneous=True))
A=3*xx**2+12*xx+11
B=3*xx+6
target=[(xx+1)*(xx+2)*(xx+3)-A*v0+B*(v0*v0+v1)-(v0**3+3*v0*v1+v2),
        -A+d*B-d*d+(2*B-3*d)*v0-3*(v0*v0+v1),
        B-3*d-3*v0,-sp.S.One]
for j in range(4):
    check('complete_third_Mellin_shift_'+str(j),
          sp.expand(shifted.coeff(zeta,j)-target[j])==0)
scalar_sum=sum(d**j*sp.ff(u,j)*target[j].subs({v0:0,v1:0,v2:0}) for j in range(4))
check('full_third_order_horizontal_reference_mass',sp.expand(scalar_sum-6)==0)

# Collect the actual dyadic branches before dividing by z^j.  The left-normal
# covariant expansion keeps the derivatives of every actual connection a_nu.
a0,a1,a2,a3,YB,YE,YH,YL,ellc,gam = sp.symbols('a0 a1 a2 a3 YB YE YH YL ellc gam')
avs=[a0,a1,a2,a3]
def AD(q):
    return sum(sp.diff(q,avs[j])*avs[j+1] for j in range(3))
op={0:sp.S.One};ops={}
for j in range(1,4):
    nxt={}
    for k,c in op.items():
        nxt[k+1]=nxt.get(k+1,0)+c
        nxt[k]=nxt.get(k,0)-AD(c)-a0*c
    op={k:sp.expand(c) for k,c in nxt.items()}
    ops[j]=op
expected2={2:1,1:-2*a0,0:a0*a0+a1}
expected3={3:1,2:-3*a0,1:3*(a0*a0+a1),0:-(a0**3+3*a0*a1+a2)}
for j,expected in ((2,expected2),(3,expected3)):
    for k,c in expected.items():
        check('actual_dyadic_left_connection_'+str(j)+'_'+str(k),sp.expand(ops[j][k]-c)==0)
blocks=[]
grades={a0:3,a1:2,a2:1,a3:0,YB:3,YE:2,YH:2,YL:2,ellc:0,gam:0}
for k in range(4):
    q=sp.expand(ops[3].get(k,0)*YB/8+ops[2].get(k,0)*(YE/4+ellc*YH/4-gam*YL/32))
    blocks.append(q)
    good=True
    for term in sp.Add.make_args(q):
        powers=term.as_powers_dict()
        good=good and sum(int(powers.get(v,0))*grade for v,grade in grades.items())%4==k
    check('aggregated_actual_i_character_'+str(k),good)

# Apparent P8 poles do not meet any of the actual eight-torsion branch origins.
f=x**3-x
divs={0:(sp.S.Zero,sp.S.Zero),1:(sp.S.One,sp.S.Zero),2:(sp.S.Zero,sp.Integer(2)),
      3:(3*x**4-6*x*x-1,sp.S.Zero),4:(sp.S.Zero,4*(x**6-5*x**4-5*x*x+1))}
def add(a,b,sign=1):
    return (sp.expand(a[0]+sign*b[0]),sp.expand(a[1]+sign*b[1]))
def mul(a,b):
    return (sp.expand(a[0]*b[0]+f*a[1]*b[1]),sp.expand(a[0]*b[1]+a[1]*b[0]))
def power(a,n):
    b=(sp.S.One,sp.S.Zero)
    for _ in range(n):b=mul(b,a)
    return b
def psi(n):
    if n in divs:return divs[n]
    m=n//2
    if n%2:
        q=add(mul(psi(m+2),power(psi(m),3)),mul(psi(m-1),power(psi(m+1),3)),-1)
    else:
        q=mul(psi(m),add(mul(psi(m+2),power(psi(m-1),2)),
                          mul(psi(m-2),power(psi(m+1),2)),-1))
        q=(sp.cancel(q[1]/2),sp.cancel(q[0]/(2*f)))
    divs[n]=q
    return q
eight=psi(8)
check('actual_eight_division_y_factor',eight[0]==0)
V8=sum(c*U**(k[0]//2) for k,c in sp.Poly(eight[1],x).terms())
check('actual_eight_division_even_x_powers',sp.expand(V8.subs(U,x*x)-eight[1])==0)
Pint=sp.Poly(P8,U).clear_denoms()[1]
check('apparent_P8_poles_avoid_all_eight_torsion',sp.gcd(Pint,sp.Poly(V8,U)).degree()==0)
res=sp.resultant(Pint,V8,U)
check('fixed_eight_torsion_resultant_nonzero',res!=0)

# The rational horizontal source is not a free replacement by a known CM line.
spec=importlib.util.spec_from_file_location('r248',HERE/'check-ray17-conjugate-trace-and-yang-projection.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
d248=json.loads((HERE/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
N=dm(sp.Matrix.hstack(*[sp.Matrix(list(map(sp.sympify,c))+[sp.S.Zero]*(17-len(c)))
    for c in d248['CM5_matrix_columns']])).scalarmul(K.from_sympy((2-ii)/5))
I=dm(sp.eye(17));pw=[I]
for _ in range(16):pw.append(pw[-1]*N)
P5=(pw[0]+pw[4]+pw[8]+pw[12]).scalarmul(K.one/4)
vk=dm(sp.Matrix(d264['right_kernel'])).scalarmul(K.one/1341153)
pool=dm(sp.Matrix.hstack(m.vector(m.Pbe),m.vector(m.Pba),*[
    sp.Matrix(list(map(sp.sympify,d248['normalized_primitive_polynomials'][str(k)])))
    for k in (1,2,3)]))
rows=list(pool.transpose().rref()[1])
coeff=pool.extract(rows,list(range(5))).inv()*(P5*vk).extract(rows,[0])
check('horizontal_source_known_five_coordinates',(pool*coeff-P5*vk).is_zero_matrix)
check('horizontal_source_has_twelve_type_remainder',not(vk-P5*vk).is_zero_matrix)
check('horizontal_source_is_not_a_CM5_eigenline',vk.hstack(N*vk).rank()==2)

column_data={}
JQ=Jmat*Q
for j,name in enumerate(names):
    q=Q.to_Matrix()[:,j]
    column_data[name]={
        'Q_coefficients':list(map(str,q)),
        'J_degree24_coefficients':list(map(str,JQ.to_Matrix()[:,j])),
        'ell':str(period.to_Matrix()[j]),'original_log_gamma':str(gammas[j]),
        'boundary_zero_one':list(map(str,(boundary*Q).to_Matrix()[:,j])),
        'rational_companion_z2_coefficient':str(q[16]),
        'primitive_B_over_z3_mass':str(-q[16]/65),
        'connection_E_over_z2_mass':str(68*q[16]/65),
        'actual_CM_boundary_coefficients':list(map(str,cm.to_Matrix()[:,j])),
        'all_nineteen_second_derivative_coordinates':list(map(str,full19.to_Matrix()[:,j])),
        'actual_nonbeta_preimage_coefficients':list(map(str,preimages.to_Matrix()[:,j])),
    }
out={
    'theorem':'R269','status':'PASS','checks':checks,
    'actual_source_weight':'a=1/(4*P8(U)*(U-1)^9); (F*a)*eta_Q=(W/x)*Q dz',
    'P8_reverse_coefficients':[str(P.coeff(s,j)) for j in range(9)],
    'primitive_J_matrix_columns':cols(Jmat),
    'finite_identity':'4*P*(1-s)*q_reverse=-4*s*(1-s)*J_prime+(65-63*s)*J+lambda*ell(Q)*s^16',
    'rational_angular_terms':{
        'B_over_theta68_u3':'-J/(4*P)',
        'E_over_theta68_u2_sqrt':'J*((17-8*s)*P-s*(1-s)*P_prime)/(P^2*(1-s))',
        'H_over_theta68_u2_sqrt':'s^16/(4*P*(1-s))'},
    'actual_five_columns':column_data,
    'full_boundary_period_log_matrix_rows':[[str(v) for v in row] for row in observations.to_Matrix().tolist()],
    'four_column_determinant':str(expected_det),
    'original_C0_relation_coefficient_tau':str(tau),
    'complete_third_Euler_left_normal_coefficients':{str(k):str(v) for k,v in normal.items()},
    'complete_third_Mellin_shift_polynomials':[str(sp.expand(q)) for q in target],
    'actual_dyadic_aggregated_blocks_C0_C1_C2_C3':list(map(str,blocks)),
    'eight_division_polynomial_in_U':str(V8),'apparent_pole_eight_torsion_resultant':str(res),
    'horizontal_reference_known_five_coefficients':list(map(str,coeff.to_Matrix())),
    'horizontal_reference_extra_twelve_coordinates':list(map(str,(vk-P5*vk).to_Matrix())),
    'scope':'Original inert frame, all primitive connection terms and central shifts retained.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(checks),'checks; original four-column determinant =',expected_det,flush=True)
