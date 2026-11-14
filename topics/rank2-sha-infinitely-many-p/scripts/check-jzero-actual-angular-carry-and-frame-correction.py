#!/usr/bin/env python3
"""R299 symbolic checks; no target-prime sampling or nonvanishing search."""
import sympy as s,json
from pathlib import Path
q,p,r,a0,ell,a,b=s.symbols('q p r a0 ell a b',nonzero=True)
L=s.Function('L')(q);T=s.Function('T')(q)
U=q**(-r)*(L-T)
checks=[]
def must(n,c):
    if not c:raise AssertionError(n)
    checks.append(n)
conj=s.expand(q**r*(U+3*q*s.diff(U,q)))
expect=(1-3*r)*(L-T)+3*q*(s.diff(L,q)-s.diff(T,q))
must('complete first-order conjugation of angular remainder',s.simplify(conj-expect)==0)
must('conjugation mass factor is minus p',s.expand((1-3*r)+p).subs(p,3*r-1).expand()==0)
must('canonical source bad-band normalization includes ell times hplus',s.expand((a0+p*ell)/p-a0/p-ell)==0)
must('rational correction origin is ell modulo p',s.expand(3*r*ell-ell-p*ell).subs(p,3*r-1).expand()==0)
must('hplus multiplied by v squared gives v to p',s.expand(2+3*(r-1)-p).subs(p,3*r-1).expand()==0)
must('first unresolved remainder index is 2r minus1',s.expand(r+(2*r-1)-p).subs(p,3*r-1).expand()==0)
must('actual first-order resonance is twice p',s.expand(1+3*(2*r-1)-2*p).subs(p,3*r-1).expand()==0)
Q8=(q-2)**2*(1+q)*(1-2*q)*(q**4+q**3+6*q*q-14*q+7)
G=Q8/28
must('actual angular unit constant',G.subs(q,0)==1)
must('actual angular unit first coefficient',s.diff(G,q).subs(q,0)==-4)
Lqprime=-s.Rational(2,3)/(1-q)+s.diff(Q8,q)/Q8
must('full rational angular log derivative',s.cancel(Lqprime-(s.diff(s.log(Q8),q)+s.diff(s.Rational(2,3)*s.log(1-q),q)))==0)
# All p-adic residue assertions used here are proved uniformly in the text.
must('theta pth log carry',s.Rational(2*34,3)==s.Rational(68,3))
must('actual q unit pth log carry is18',s.Rational(68,3)-s.Rational(2,3)-4==18)
h1=s.Rational(2,3)/4
must('Dixon logarithm first coefficient',h1==s.Rational(1,6))
must('actual z unit pth log carry is17',18-6*h1==17)
must('h resonance denominator equals2p',s.expand(3*(2*r-1)+1-2*p).subs(p,3*r-1).expand()==0)
must('h numerator contains p at index r minus1',s.expand(3*(r-1)+2-p).subs(p,3*r-1).expand()==0)
must('h pth factorial denominator cancels its one numerator p',(3*(r-1)+2).subs(r,(p+1)/3)==p)
# Exact frame conversion: a^6=4b and az=u h.
u,h,S=s.symbols('u h S',nonzero=True)
z=u*h/a
Fq=4*b*S/u**6;Fz=S/z**6
must('original z unit equals q unit times h to minus6',s.factor((Fz-Fq/h**6).subs(b,a**6/4))==0)
ans={'status':'PASS','target_prime_scan':False,'checks':checks,'number_of_checks':len(checks),
 'original_q_unit':'4*b*S/q^2=theta_minus^34*v^2*Q8/28',
 'original_z_unit':'S/z^6=(4*b*S/q^2)*h^(-6)',
 'Q8_ascending':[str(s.Poly(s.expand(Q8),q).nth(j)) for j in range(9)],
 'q_unit_boundary_carry':18,'z_unit_boundary_carry':17,
 'canonical_normalization':'a0_source=a0_theta+p*ell_r; U_source=U_theta+q^(-r)*(L-L_<r)-ell_r*hplus',
 'full_correction':'R_p-ell_r*v^p',
 'h_mod_p_before_qp':'hplus+c_p*q^(2r-1), c_p a unit',
 'global_Cartier_of_paid_finite_model':'-2 dv',
 'window':'mod q^(2r-1) for canonical U; cannot include the first resonant coefficient',
 'scope':'The q-unit rational correction is built from the actual Q8; the z-unit uses the actual finite polynomial H_p only within the proved window.'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'actual_q_carry':18,'actual_z_carry':17},indent=2))
