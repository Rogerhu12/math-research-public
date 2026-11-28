#!/usr/bin/env sage-python
"""Exercise the actual short thick fibre, whole kernel, and reciprocal-normalization proof."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import runpy
from pathlib import Path
from sage.all import GF,PolynomialRing,vector
from original_ys_divisor_ideal_tools import canonical,digest,polynomial_matrix_digest
import original_short_graph_global as low
import original_short_graph_outer as outer


def order_at_zero(poly):
    for a,c in enumerate(poly.list()):
        if c:
            return a
    raise ArithmeticError("A nonzero complete ideal determinant was required")


def run_case(engine0,engine1,N,D,common_weight,degree,window,old):
    weights=(0,1)
    Ni=low.reciprocal_row(N,common_weight,weights,engine1.R)
    Di=low.reciprocal_row(D,common_weight,weights,engine1.R)
    args=(engine0,engine1,(N,D),(Ni,Di),common_weight,degree,0,window)
    blocks,rec=low.two_chart_low_graph(*args)
    target=2*window-degree+1
    if (rec["actual_full_RR_dimension"]!=target or
            rec["actual_low_graph_row_weight_sum"]!=1+degree or
            rec["actual_finite_source_rank"]["original_module_rank"]!=2 or
            rec["reciprocal_whole_constant_prime_rank"]!=2*int(engine0.k.degree())):
        raise ArithmeticError("The complete low graph failed the independent projective-line dimensions")
    charts={}
    for flag,E,src in ((False,engine0,(N,D)),(True,engine1,(Ni,Di))):
        Y,X=blocks[flag]
        nore,dore=src
        Xold,Yold,orec=old(E.multiplication_matrix(nore),E.multiplication_matrix(dore),
                            progress=E.progress,label="all original small graph coordinates")
        positive=Xold.hermite_form(include_zero_rows=False)
        def reference(a,b,H,G):
            if H!=Yold or G!=positive:
                raise ArithmeticError("The candidate missed the true original toy ideal basis")
            return dict(complete_graph_for_this_full_original_function=True,
                        route="same small old full graph on this chart and degree")
        pos,neg,checked=outer.projected_pair_after_proof(
            E,nore,dore,Y,X,"short global software graph",reference,degree,1)
        if checked["post_ideal_outer"]["complete_X_sha256"]!=polynomial_matrix_digest(Xold):
            raise ArithmeticError("The compact joint graph changed a whole old post-ideal image row")
        charts[flag]=(pos,neg)
    for sign in (0,1):
        finite,reciprocal=charts[False][sign],charts[True][sign]
        if (finite.length+order_at_zero(reciprocal.determinant)!=degree or
                reciprocal.length+order_at_zero(finite.determinant)!=degree):
            raise ArithmeticError("The two complementary whole-fibre lengths were misidentified")
    return args,rec


def main():
    old_data=runpy.run_path(str(Path(__file__).with_name("check-original-adaptive-scalar-graph.py")))
    old,Engine=old_data["adaptive"].ORIGINAL_GRAPH,old_data["TwoChartEngine"]
    receipts=[]
    shortened=0
    wrong_chart=0
    nonlinear_thick=0
    fp=GF(29)
    rr=PolynomialRing(fp,"grr_nonbinomial_modulus")
    modulus=rr.gen()**2-rr.gen()-fp.one()/fp(4)
    if not modulus.is_irreducible():
        raise ArithmeticError("The explicit quadratic-window fixture lost its nonzero linear coefficient")
    quadratic=GF(29**2,"z_grr_fixture",modulus=modulus)
    if quadratic.gen()**2!=quadratic(fp.one()/fp(4))+quadratic.gen():
        raise ArithmeticError("The short-fibre kernel has the wrong prescribed quadratic basis")
    for k in (fp,quadratic):
        E0,E1=Engine(k,False),Engine(k,True)
        t=E0.R.gen()
        e,b=E0.unit,vector(E0.R,[0,1])
        # Here b^2=t and the true projective curve is P^1_b. In the first
        # case c!=+/-1, so the non-scalar common multiplier cancels exactly.
        c=k(4) if k.degree()==1 else k.gen()
        shared=t*e+b
        cases=[(E0.multiply(shared,c*e+b),E0.multiply(shared,(t-1)*e),2,2,2),
               (e,t**2*e,2,4,3),(b,e,1,1,2)]
        if int(k.degree())==1:
            # This *actual raw denominator* is nonunit at all 29 linear places.
            # Its shared scalar leaves f=b, while its first usable good centre
            # must be quadratic and the complete short modulus must be its square.
            full_linear=t**29-t
            cases.append((full_linear*b,full_linear*e,30,1,2))
        for idx,(N,D,M,degree,window) in enumerate(cases):
            args,rec=run_case(E0,E1,N,D,M,degree,window,old)
            receipts.append(dict(actual_constant_degree=int(k.degree()),true_projective_pole_degree=degree,
                actual_original_RR_dimension=rec["actual_full_RR_dimension"],
                actual_short_fibre_degree=rec["actual_full_thick_fibre"]["complete_fibre_modulus_degree"],
                actual_original_paired_weights=rec["actual_column_echelon"]["actual_original_row_weights"]))
            if idx==3:
                sol=rec["actual_full_thick_fibre"]
                if (sol["original_good_place_degree"]!=2 or sol["actual_pi_digits"]!=2 or
                        sol["complete_fibre_modulus_degree"]!=4 or len(sol["actual_nonunit_centers_skipped"])<29):
                    raise ArithmeticError("The genuinely quadratic thick place did not pass its original route")
                nonlinear_thick+=1
            if idx!=1:
                continue
            before=low.solve_short_fibre
            def omit_last_digit(*values):
                M,pi,q,r=before(*values)
                if q.degree()<=pi.degree():
                    raise AssertionError("The toy requires a genuinely thick place")
                return M,pi,q//pi,r
            low.solve_short_fibre=omit_last_digit
            try:
                low.two_chart_low_graph(*args)
            except ArithmeticError as err:
                if "not longer than the divisor" not in str(err):
                    raise
                shortened+=1
            else:
                raise AssertionError("The strict full-fibre degree bound was not enforced")
            finally:
                low.solve_short_fibre=before
            ninf,dinf=args[3]
            try:
                low.two_chart_low_graph(*args[:3],(ninf+E1.unit,dinf),*args[4:])
            except ArithmeticError as err:
                if "genuinely same weighted numerator" not in str(err):
                    raise
                wrong_chart+=1
            else:
                raise AssertionError("An unrelated reciprocal polynomial pair was admitted")
    if len(receipts)!=7 or (shortened,wrong_chart,nonlinear_thick)!=(2,2,1):
        raise AssertionError("A planned genuine short graph check did not execute")
    result=dict(kind="whole_short_thick_fibre_and_reversal_software_only",
                actual_low_graphs=receipts,complete_chart_comparisons=2*len(receipts),
                truncated_thick_place_rejections=shortened,wrong_original_chart_rejections=wrong_chart,
                actual_genuinely_quadratic_squared_fibre_comparisons=nonlinear_thick,
                actual_both_complementary_projective_degrees_verified=True,
                explicit_quadratic_relation="alpha^2=alpha+1/4 over F29",
                original_rank306_geometry_executed=False)
    print("RANK2_SHORT_GLOBAL_GRAPH_SOFTWARE_RESULT "+canonical(result),flush=True)
    print("RANK2_SHORT_GLOBAL_GRAPH_SOFTWARE_SHA256 "+digest(result),flush=True)


if __name__=="__main__":
    main()
