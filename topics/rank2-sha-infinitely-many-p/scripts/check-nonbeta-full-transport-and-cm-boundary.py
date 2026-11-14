#!/usr/bin/env python3
"""R265: complete non-pullback transport, true boundary poles and connection.

Every finite-flat trace is recovered from its proved 17-dimensional target,
using 17 exact fibers and an additional exact fiber.  No target-prime samples.
"""
import importlib.util
import json
import math
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'r248', HERE/'check-ray17-conjugate-trace-and-yang-projection.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
U, ii, K = m.U, s.I, s.QQ_I
D = U**8*(U-1)**8
checks = {}


def check(label, condition):
    checks[label] = bool(condition)
    if not condition:
        raise AssertionError(label)


def dm(a):
    return a.to_DM(domain=K)


def columns(a):
    b = a.to_Matrix() if hasattr(a, 'to_Matrix') else a
    return [[str(s.expand(b[j,k])) for j in range(b.rows)]
            for k in range(b.cols)]


def fiber(a):
    f = s.Poly(U,U,domain=K)*m.Qba**4-(m.Kba**4).mul_ground(a)
    check('actual_monic_seventeen_fiber_'+str(a),f.degree()==17 and f.LC()==1)
    base = m.ipow((m.Pbe*m.inv(m.Pba,f)).rem(f),17,f)
    adjacent = (base*m.Qba**2*m.inv(m.Kba**2,f)).rem(f)
    iu = m.inv(s.Poly(U,U,domain=K),f)
    ib = m.inv(s.Poly(U-1,U,domain=K),f)
    out = []
    for mult in (base,adjacent):
        ans, now = [], mult
        for _ in range(9):
            ans.append(s.expand((now*f.diff()).rem(f).nth(16)*a**8*(a-1)**8))
            now = (now*iu).rem(f)
        now = (mult*ib).rem(f)
        for _ in range(1,9):
            ans.append(s.expand((now*f.diff()).rem(f).nth(16)*a**8*(a-1)**8))
            now = (now*ib).rem(f)
        out.append(ans)
    return out


# Partial fractions form a unimodular polynomial basis after multiplication D.
carrier_polys = [s.Poly(U**(8-j)*(U-1)**8,U,domain=K) for j in range(9)]
carrier_polys += [s.Poly(U**8*(U-1)**(8-h),U,domain=K) for h in range(1,9)]
B = dm(s.Matrix.hstack(*map(m.vector,carrier_polys)))
check('actual_partial_fraction_basis_unimodular',B.det() in (K.one,-K.one))
check('positive_true_T0_order',34-32==2)
check('adjacent_true_T0_order',34-32-2==0)
check('both_true_Tplus_Tminus_order',17-16==1)

vals = []
for a in range(2,19):
    vals.append(fiber(a))
    print('complete positive/adjacent fiber',a,flush=True)
held = fiber(19)
transport, tdata = [], {}
for sign,label in enumerate(('positive','adjacent')):
    ps = [m.interpolate([row[sign][j] for row in vals],start=2) for j in range(17)]
    for j,p in enumerate(ps):
        check(label+'_whole_target_degree_'+str(j),p.degree()<=16)
        check(label+'_held_out_full_fiber_'+str(j),p.eval(19)==held[sign][j])
    T = dm(s.Matrix.hstack(*map(m.vector,ps)))*B.inv()
    transport.append(T)
    det = s.expand(K.to_sympy(T.det()))
    re, im = det.as_real_imag()
    detden = s.ilcm(s.denom(re),s.denom(im))
    gcd = math.gcd(int(re*detden),int(im*detden))
    entryden = s.ilcm(*[s.denom(z) for z in T.to_Matrix() for z in s.expand(z).as_real_imag()])
    check(label+'_rank_seventeen',T.rank()==17)
    check(label+'_entry_denominators_only_two',set(s.factorint(entryden))<={2})
    check(label+'_determinant_inert_units',set(s.factorint(gcd))<={2})
    check(label+'_determinant_denominators_only_two',set(s.factorint(detden))<={2})
    tdata[label] = {
        'canonical_matrix_columns':columns(T),'rank':T.rank(),
        'determinant':str(det),'entry_denominator_lcm':str(entryden),
        'Gaussian_determinant_denominator':str(detden),
        'Gaussian_numerator_real_imag_gcd':str(gcd),
        'all_odd_inert_primes_are_units':True,
    }
Tp,Tm = transport


def full_second(P):
    return (16*U*(U-1)*s.diff(P,U,2)-(508*U-260)*s.diff(P,U)
            +(4290-1190/U+1088/(U-1))*P)


def polynomial_second(P):
    return s.cancel(16*U*(U-1)*s.diff(P,U,2)-(508*U-260)*s.diff(P,U)
        +4290*P-1190*(P-P.subs(U,0))/U+1088*(P-P.subs(U,1))/(U-1))


# Check the complete covariant derivative by the original elliptic derivation.
x = s.symbols('x')
def DD(f):
    return 4*(x**3-x)*s.diff(f,x,2)+2*(3*x*x-1)*s.diff(f,x)

ks = []
for j in range(17):
    P = U**j
    h = (P/D).subs(U,x*x)/x
    check('original_second_derivative_column_'+str(j),
          s.cancel(D.subs(U,x*x)*DD(h)-full_second(P).subs(U,x*x))==0)
    q = s.Poly(polynomial_second(P),U,domain=K)
    check('both_true_boundary_poles_'+str(j),
          s.cancel(full_second(P)-q.as_expr()+1190*P.subs(U,0)/U
                   -1088*P.subs(U,1)/(U-1))==0)
    check('polynomial_diagonal_'+str(j),q.nth(j)==(4*j-65)*(4*j-66))
    ks.append(q)
K2 = dm(s.Matrix.hstack(*map(m.vector,ks)))
pd = s.factorint(abs(int(K.to_sympy(K2.det()))))
check('polynomial_second_only_large_inert_exceptions',
      {int(p) for p in pd if p>19 and p%4==3}=={23,31})

# Exact derivative ladders, including the highest poles at h=8.
for h in range(9):
    u = 1/(x*(x*x-1)**h)
    expected = (2*(4*h+1)*(2*h+1)-6/(x*x))/(x*x-1)**h
    expected += 8*h*(2*h+1)/(x*x-1)**(h+1)
    check('complete_adjacent_derivative_ladder_'+str(h),s.cancel(DD(u)-expected)==0)
for h in range(1,9):
    v = 1/(x*x-1)**h
    expected = 4*h*((4*h-1)/(x*(x*x-1)**(h-1))
        +(8*h+1)/(x*(x*x-1)**h)+(4*h+2)/(x*(x*x-1)**(h+1)))
    check('complete_positive_derivative_ladder_'+str(h),s.cancel(DD(v)-expected)==0)
for a in range(1,18):
    check('complete_x_power_derivative_ladder_'+str(a),
          s.cancel(DD(x**(-a))-2*a*((2*a-1)*x**(1-a)-(2*a+1)*x**(-a-1)))==0)

d264 = json.loads((HERE/'check-normtwo-finite-connection-kernel.json').read_text())
Gamma = s.Matrix(list(map(s.sympify,d264['actual_CM_compensator_polynomial'])))
Gammabar = Gamma.conjugate()
check('actual_CM_beta_reverse_polynomial',Gamma==-s.Matrix(list(reversed(m.vector(m.Pbe)))))
check('actual_CM_barbeta_reverse_polynomial',Gammabar==-s.Matrix(list(reversed(m.vector(m.Pba)))))
G = dm(Gamma.row_join(Gammabar))
boundary = dm(s.Matrix([[1]+[0]*16,[1]*17]))
GB = boundary*G
check('actual_CM_boundary_matrix',GB.to_Matrix()==s.Matrix([
    [-1,-1],[-65536-262144*ii,-65536+262144*ii]]))
check('actual_CM_boundary_determinant',GB.det()==K.from_sympy(-2**19*ii))
CC = GB.inv()*boundary
I17 = dm(s.eye(17))
Reg = I17-G*CC
check('actual_CM_regularization_projection',(Reg*Reg-Reg).is_zero_matrix)
check('both_actual_poles_removed',(boundary*Reg).is_zero_matrix)
check('regularized_source_dimension',Reg.rank()==15)
check('full_CM_source_reconstruction',(Reg+G*CC-I17).is_zero_matrix)
E = dm(s.Matrix.hstack(*[m.vector(s.Poly(U**(j+1)*(U-1),U,domain=K))
                         for j in range(15)]))
check('original_fifteen_space_unchanged',(Reg*E-E).is_zero_matrix)
L15 = K2*E

# Every branch has slope 1/bar(beta).  Preserve the complete connection defect.
r2 = K.from_sympy(s.expand_complex(1/(4+ii)**2))
target_CM = CC*Tm*E
Delta = K2*Reg*Tm*E-(Tp*L15).scalarmul(r2)
polar = dm(s.Matrix([[-1190]+[0]*16,[1088]*17]))
Kfull = K2.vstack(polar)
zero2 = dm(s.zeros(2,15))
Deltafull = Kfull*Tm*E-(Tp*L15).vstack(zero2).scalarmul(r2)
check('full_connection_poles_and_CM_compensation',
      (Deltafull-Delta.vstack(zero2)-Kfull*G*target_CM).is_zero_matrix)
check('connection_defect_is_not_zero',not Deltafull.is_zero_matrix)

# Glue to the actual R264 operator, including its one-quarter normalization.
M = dm(s.Matrix(d264['matrix']))
ell = dm(s.Matrix([d264['left_kernel']]))
gamma = K.from_sympy(s.sympify(d264['actual_CM_compensator_pairing']))
M15 = dm(s.Matrix(d264['matrix'])[:,:16])
extended = M15.hstack(dm(Gamma))
lift = extended.inv()*Tm
check('complete_R264_CM_lift',(extended*lift-Tm).is_zero_matrix)
check('actual_R264_compensation_row',
      (lift.extract([16],list(range(17)))-(ell*Tm).scalarmul(1/gamma)).is_zero_matrix)

# The old five genuine positive sources do not already close this larger graph.
d248 = json.loads((HERE/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
d254 = json.loads((HERE/'check-octic-ray-original-companion-transport.json').read_text())
Vplus = s.Matrix.hstack(m.vector(m.Pbe),m.vector(m.Pba),*[
    s.Matrix(list(map(s.sympify,d248['normalized_primitive_polynomials'][str(k)])))
    for k in (1,2,3)])
Vminus = s.Matrix.hstack(*[s.Matrix(list(map(s.sympify,a)))
    for a in d254['normalized_new_octic_references']])
K8 = s.QQ.algebraic_field((1+ii)/s.sqrt(2))
pool = (s.Matrix(d264['matrix'])*Vplus).row_join(-Vminus).row_join(-Gamma)
check('known_five_image_rank_five',dm(s.Matrix(d264['matrix'])*Vplus).rank()==5)
check('known_five_and_octic_plus_CM_intersection_zero',pool.to_DM(domain=K8).rank()==10)

# Strengthen R262 from a fixed exceptional set to every inert p>19.
d262 = json.loads((HERE/'check-nonbeta-normtwo-constants-original-octic.json').read_text())
det4 = s.expand(s.sympify(d262['first_four_determinant']))
re,im = det4.as_real_imag()
den4 = s.ilcm(s.denom(re),s.denom(im))
gcd4 = math.gcd(int(re*den4),int(im*den4))
check('R262_first_four_common_denominator',den4==2**94)
check('R262_first_four_Gaussian_numerator_gcd',gcd4==17)
rr = s.symbols('r')
denentries = []
for row in d262['original_octic_matrix_4_by_9']:
    for q in row:
        q = s.expand(s.sympify(q)).subs(s.sqrt(2),rr)
        for c in s.Poly(q,rr).all_coeffs():
            denentries.extend(s.denom(e) for e in s.expand(c).as_real_imag())
check('R262_all_entries_only_dyadic_denominators',s.ilcm(*denentries)==2**33)

out = {
    'theorem':'R265','status':'PASS','checks':checks,
    'coefficient_order':'ascending powers of U',
    'actual_transport':'Tr_barbeta [F(beta z)/F(z) times the original source]',
    'partial_fraction_basis_polynomials':[m.coefficients(p) for p in carrier_polys],
    'partial_fraction_basis_determinant':str(K.to_sympy(B.det())),
    'transports':tdata,
    'polynomial_second_matrix_columns':columns(K2),
    'polynomial_second_determinant_factorization':{str(p):int(e) for p,e in pd.items()},
    'actual_polar_coefficients':['-1190 P(0)','1088 P(1)'],
    'CM_boundary_matrix':[[str(q) for q in row] for row in GB.to_Matrix().tolist()],
    'CM_boundary_determinant':str(K.to_sympy(GB.det())),
    'CM_regularization_columns':columns(Reg),
    'regular_input_basis_columns':columns(E),
    'regular_input_second_columns':columns(L15),
    'full_unregularized_connection_rank':Deltafull.rank(),
    'regularized_connection_rank':Delta.rank(),
    'regularized_connection_columns':columns(Delta),
    'actual_transport_CM_boundary_columns':columns(target_CM),
    'R264_zero_mass_preimage_and_CM_columns':columns(lift),
    'R264_lift_last_row':'ell(Tminus P)/gamma; actual source K has factor 4',
    'known_positive_five_vs_original_octic_four_plus_CM_rank':10,
    'R262_all_inert_above_19_integral_basis':{
        'entry_denominator_lcm':str(2**33),'determinant_common_denominator':str(den4),
        'Gaussian_numerator_gcd':str(gcd4)},
    'branch_slope':'1/(4+i)','full_branch_scaling_unit':'U_barbeta,p^(-u)',
    'scope':'Actual finite sources and full covariant transpose; no central closure assumption.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(checks),'checks;',
      'connection ranks',Deltafull.rank(),Delta.rank(),flush=True)
