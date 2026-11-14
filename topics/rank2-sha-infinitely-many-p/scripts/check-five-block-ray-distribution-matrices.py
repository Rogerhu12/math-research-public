#!/usr/bin/env python3
"""R255: exact five-block raw-distribution and balanced-CM5 matrices."""
import json
from pathlib import Path
import sympy as s

def main():
    here=Path(__file__).resolve().parent
    d=json.loads((here/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
    assert d['status']=='PASS'
    ii=s.I;pi=2+ii;pib=2-ii
    A=s.Matrix([[s.sympify(x) for x in r['primitive_coefficients_H_S2312_S39304']]
                for r in d['projection_rows']])
    C=s.Matrix([[s.sympify(x) for x in r['CM_coefficients_beta_barbeta']]
                for r in d['projection_rows']])
    delta=(A.adjugate()*C[:,0]).applyfunc(s.expand)
    ai=A.inv()
    mup=s.diag(-ii,1,ii);mub=s.diag(1,-1,1)
    Dp=(ai*mup*A).applyfunc(s.simplify)
    Db=(ai*mub*A).applyfunc(s.simplify)
    zero=s.zeros(3);Id=s.eye(3)
    assert (Dp**4-Id).applyfunc(s.simplify)==zero
    assert (Db+Dp**2).applyfunc(s.simplify)==zero
    assert (Db**2-Id).applyfunc(s.simplify)==zero
    assert (A*Dp-mup*A).applyfunc(s.simplify)==zero
    Lam=s.diag(ii,-1,-ii)
    comparison=(pi**2*Dp-pi*Lam).applyfunc(s.simplify)
    cm=(pi**2*Dp*delta-pi*delta).applyfunc(s.simplify)
    det=s.simplify(comparison.det());assert det!=0
    def enc(M):return [[str(M[j,k]) for k in range(M.cols)] for j in range(M.rows)]
    out={'status':'PASS','raw_mu_pi':['-I','1','I'],
         'raw_mu_barpi':['1','-1','1'],
         'D_pi':enc(Dp),'D_barpi':enc(Db),
         'D_pi_fourth_power_identity':True,'D_barpi_equals_minus_D_pi_squared':True,
         'CM_vector_delta':list(map(str,delta)),
         'raw_CM_vector_pi':list(map(str,(Dp*delta).applyfunc(s.simplify))),
         'raw_CM_vector_barpi':list(map(str,(Db*delta).applyfunc(s.simplify))),
         'balanced_primitive_Lambda':['I','-1','-I'],
         'raw_minus_balanced_primitive_matrix':enc(comparison),
         'raw_minus_balanced_CM_vector':list(map(str,cm)),
         'raw_minus_balanced_primitive_determinant':str(det),
         'full_raw_distribution':'R_alpha^Q=alpha^2*U_alpha^u*D_alpha*J_Q(Z)',
         'full_B_observer':'R_alpha^B=U_alpha^u*Y_B',
         'B_mass':'-4*I',
         'balanced_B_comparison':'K_B=(-1-r_p(u))*Y_B+2*(-U_beta^u+(1-4*I)*U_barbeta^u)',
         'difference_first_derivative':'-4*I*ell5',
         'difference_second_derivative':'2*ell5*Y_B_prime-4*I*(p-1)*log_p(5)*ell5',
         'divided_full_row':'(R_pi^B-R_barpi^B)/(u*ell5*D5(u))=Y_B',
         'division_scalar_not_asserted_algebraic':True}
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
