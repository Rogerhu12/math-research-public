#!/usr/bin/env python3
"""R260: actual positive norm-two source, weighted traces and terminal CM17 image.

All operations are exact. The original CM5 matrix is from R248. The true
conductor-17 rank-one functional, including its line-bundle normalization,
is the independently constructed R259 certificate.
"""
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'r248', HERE/'check-ray17-conjugate-trace-and-yang-projection.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
U, ii, K = m.U, s.I, s.QQ_I
x, v, t = s.symbols('x v t')
checks = {}


def check(label, condition):
    checks[label] = bool(condition)
    if not condition:
        raise AssertionError(label)


def eq(a,b):
    return s.cancel(a-b)==0


R = (1+x**-2)**17
R2 = 4*(x**3-x)*s.diff(R,x,2)+2*(3*x*x-1)*s.diff(R,x)
q2 = 68*(3*x**4+62*x*x-69)/(x*(x*x+1)**2)
check('original_second_derivative',eq(R2/R,q2))
cp = 544*x*(9*x*x+25)/(x*x+1)**2
check('original_pole_compensation',eq(q2+4692/x,cp))
hp = 68*(3*x**4+62*x*x-69)/(x*x+1)**2
check('positive_source_is_x_times_uncompensated',eq(x*q2,hp))
check('positive_and_compensated_weighted_sources',eq(x*cp-4692,hp))

source_poly = s.Poly(68*(1-t)**17*(1+t)**15*(3+62*t-69*t*t),t)
check('actual_degree136_polynomial_bound',source_poly.degree()==34)
check('actual_positive_source_mass',source_poly.nth(0)==204)
check('actual_positive_source_identity',
      eq(source_poly.as_expr().subs(t,x**-2),(1-x**-4)**17*hp))

va = -ii*(x-1/x)/2
Va = va*va
sigma = lambda f: f.subs(x,-1/x)
trace = lambda f: s.cancel(f+sigma(f))
check('CM2_coordinate_equation',eq(x*x-2*ii*va*x-1,0))
check('positive_true_rational_trace',eq(trace(hp),-4488-4352/(Va-1)))
check('compensated_true_rational_trace',eq(trace(cp),4352*ii*va/(Va-1)))
check('weighted_compensated_trace',eq(trace(x*cp),4896-4352/(Va-1)))
check('quadratic_trace_pair_determinant',
      s.det(s.Matrix([[2,2*ii*v],[2*ii*v,2-4*v*v]]))==4*(1-v*v))
aa,bb = 6800*ii*v/(v*v-1),-4624/(v*v-1)
check('full_compensated_two_fiber_coordinates',eq(cp,(aa+bb*x).subs(v,va)))
norm_cp = 73984*(225*v*v-289)/(v*v-1)**2
check('full_compensated_fiber_norm',eq(cp*sigma(cp),norm_cp.subs(v,va)))

# Exact cancellation of the nonconstant logarithm, with Phi_sigma=-Phi-2C.
Phi,CC = s.symbols('Phi C')
tr0 = cp*Phi+sigma(cp)*(-Phi-2*CC)
tr1 = x*cp*Phi+sigma(x*cp)*(-Phi-2*CC)
check('actual_two_trace_primitive_elimination',
      eq(17*tr1-9*ii*va*tr0,-544*CC*(225*Va-289)/(Va-1)))

d248 = json.loads((HERE/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
M = s.Matrix.hstack(*[m.vector(m.pp(list(map(s.sympify,col))))
                     for col in d248['CM5_matrix_columns']])
N = M.applyfunc(lambda z:s.expand(z/(2+ii))).to_DM(domain=K)
ID = s.eye(17).to_DM(domain=K)
powers = [ID]
for _ in range(16):
    powers.append(powers[-1]*N)
check('original_CM5_order_16',powers[16]==ID)
P4 = sum((powers[j] for j in (0,4,8,12)),ID*0).scalarmul(K(1)/4)
E = []
for k in range(4):
    a = sum((powers[j].scalarmul(K.from_sympy(ii**(-k*j)))
             for j in range(4)),ID*0)*P4
    E.append(a.scalarmul(K(1)/4))
refs = {k:s.Matrix(list(map(s.sympify,d248['normalized_primitive_polynomials'][str(k)])))
        for k in (1,2,3)}
D = s.Poly(U**8*(U-1)**8,U,domain=K)
DG = s.Poly(U**8*(U-1)**7,U,domain=K)
P = -4488*D-4352*DG


def decompose(poly,label):
    vv = m.vector(poly).to_DM(domain=K)
    blocks = [(a*vv).to_Matrix() for a in E]
    z = blocks[0]
    cb = s.expand((z[15]-(-32-40*ii)*z[16])/(80*ii))
    ca = s.expand(z[16]-cb)
    check(label+'_complete_CM_block',all(s.expand(v)==0 for v in
          z-cb*m.vector(m.Pbe)-ca*m.vector(m.Pba)))
    cs = []
    for k in (1,2,3):
        ix = 15 if k==1 else 16
        c = s.expand(blocks[k][ix]/refs[k][ix])
        check(label+'_primitive_block_'+str(k),
              all(s.expand(v)==0 for v in blocks[k]-c*refs[k]))
        cs.append(c)
    extra = (vv-P4*vv).to_Matrix()
    check(label+'_actual_remainder_nonzero',any(v!=0 for v in extra))
    return [cb,ca]+cs,extra


five,extra = decompose(P,'positive_source')
f_five,_ = decompose(D,'F')
b_five,_ = decompose(DG,'F_over_U_minus_one')
expected = [-s.Rational(77412135,262144)-s.Rational(34636021,524288)*ii,
            -s.Rational(77412135,262144)+s.Rational(34636021,524288)*ii,
            s.Rational(1340259855,524288),-s.Rational(559068341,2097152),
            -s.Rational(560669027,2097152)]
check('five_original_exact_coefficients',five==expected)
Bscalar = s.expand(-640*ii*five[3])
check('basic_actual_B_scalar',Bscalar==s.Rational(2795341705,16384)*ii)
check('original_covariant_horizontal_reference',-4488-(-4352)/2==-2312)

# Pay the final genuine beta pullback and conjugate trace, not only the
# basic degree-68 projection above.
d259 = json.loads((HERE/'check-normtwo-compensation-and-conductor17-trace.json').read_text())
rankone = d259['conductor17_sparse_rankone_operators']['positive']
lf = list(map(s.sympify,rankone['linear_functional_on_ascending_U_powers']))
check('true_terminal_CM_beta_frame',rankone['image_polynomial']==m.coefficients(m.Pbe))


def terminal_scalar(poly):
    return s.expand(sum(lf[j]*poly.nth(j) for j in range(17)))


cM = terminal_scalar(P)
cX = terminal_scalar(4896*D-4352*DG)
cLog = terminal_scalar(-122400*D+34816*DG)
check('complete_CM17_positive_scalar',
      cM==-s.Rational(584661059,131072)+s.Rational(2075649,262144)*ii)
check('complete_CM17_compensated_weighted_scalar',
      cX==s.Rational(319380173,65536)-s.Rational(59007,4096)*ii)
outv = m.vector(m.Pbe).to_DM(domain=K)
check('terminal_CM5_character_one',N*outv==outv)
check('terminal_actual_lambda2_zero',(E[2]*outv).is_zero_matrix)
P8 = sum((powers[j].scalarmul(K((-1)**(j//4))) for j in (0,4,8,12)),ID*0).scalarmul(K(1)/4)
check('terminal_actual_octic_zero',(P8*outv).is_zero_matrix)
check('terminal_source_nonzero',cM!=0 and cX!=0 and cLog!=0)

out = {
 'theorem':'R260','status':'PASS','coefficient_order':'ascending powers',
 'canonical_CM2_deck_lift':'-T_T0^136, so Tr_alpha(H*h)=F*Tr(h)',
 'positive_degree136_source_in_s':list(map(str,source_poly.all_coeffs()[::-1])),
 'positive_rational_ratio_to_H':str(hp),
 'compensated_rational_ratio_to_H':str(cp),
 'positive_CM2_trace_polynomial_in_U':m.coefficients(P),
 'five_original_coefficients_CMbeta_CMbarbeta_H_R2_R3':list(map(str,five)),
 'twelve_dimensional_remainder':list(map(str,extra)),
 'F_five_original_coefficients':list(map(str,f_five)),
 'F_over_U_minus_one_five_original_coefficients':list(map(str,b_five)),
 'basic_B_scalar_without_kappa4':str(Bscalar),
 'full_conductor17_positive_scalar':str(cM),
 'full_conductor17_compensated_weighted_scalar':str(cX),
 'full_conductor17_primitive_elimination_scalar':str(cLog),
 'terminal_lambda2_image':'0','terminal_octic_image':'0',
 'covariant_decomposition':'544 nabla_F^2(F log r) - 2312 F',
 'checks':checks,
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'output':str(target)},ensure_ascii=False))
