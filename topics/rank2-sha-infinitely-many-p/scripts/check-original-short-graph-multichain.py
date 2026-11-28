#!/usr/bin/env sage-python
"""Small public-Action software fixtures for the candidate multi-chain/outer functions."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import runpy
from pathlib import Path
import numpy as np
from sage.all import GF, PolynomialRing, identity_matrix, matrix, vector
from original_ys_divisor_ideal_tools import canonical,digest,polynomial_matrix_digest
from original_short_graph_multichain import StandardQuotient, multichain_hermite
from original_short_graph_field import PackedField
from original_short_graph_popov import complete_popov
import original_short_graph_outer as gates


def manual_case(k):
    R=PolynomialRing(k,"u_short_fixture")
    t,c=R.gen(),k.gen() if k.degree()>1 else k(4)
    B=matrix(R,[[t**2,0,0],[0,t**3,0],[c,0,1]])
    U=matrix(R,[[1,t+1,0],[0,1,t],[0,0,1]])
    C=matrix(R,[[t,1,c],[1,t+2,0],[0,c,1]])
    source,attached=U*B,U*C
    P,paired,receipt=complete_popov(source,attached)
    if P!=B or paired!=C:
        raise ArithmeticError("The entire wrapped Popov transformation changed a paired block")
    q=StandardQuotient(P)
    if not np.array_equal(q.units[:,2,:],q.field.scalar_times(q.field.coords(-c),q.units[:,0,:])):
        raise ArithmeticError("The nonzero tail on a zero-degree pivot was lost")
    H,record=multichain_hermite(P,degree_bound=5,block_size=2)
    if H!=source.hermite_form(include_zero_rows=False) or record["hermite_pivot_degrees"]!=[0,3,2]:
        raise ArithmeticError("The three true short/coupled quotient chains did not return")
    unit,empty=multichain_hermite(identity_matrix(R,3),degree_bound=0,block_size=2)
    if unit!=identity_matrix(R,3) or empty["first_dependencies"]!=3:
        raise ArithmeticError("The zero-length original complete quotient was not retained")
    return dict(field_degree=int(k.degree()),actual_chain_lengths=record["hermite_pivot_degrees"],
                actual_zero_pivot_nonzero_tail=True,actual_complete_column_popov_return=True)


def nonzero_linear_term():
    fp=GF(29)
    base=PolynomialRing(fp,"z_nonbinomial_modulus")
    z=base.gen()
    modulus=z**2-z-fp.one()/fp(4)
    # Discriminant 2 is nonsquare since 29 is 5 mod 8.
    if not modulus.is_irreducible():
        raise ArithmeticError("The explicit original non-binomial modulus is not irreducible")
    k=GF(29**2,"z_nonbinomial",modulus=modulus)
    f=PackedField(k)
    a=k.gen()
    if not f.a or f.b!=1 or a*a!=k(fp.one()/fp(4))+a:
        raise ArithmeticError("The intended original nonzero quadratic linear term was not used")
    left=matrix(k,[[a,0],[a+1,a+2]])
    right=matrix(k,[[a+3,1],[a,a+4]])
    def packed(M):
        return np.asarray([[f.coords(M[i,j]) for j in range(M.ncols())]
                           for i in range(M.nrows())],dtype=np.int64).transpose(2,0,1)
    def actual(data):
        return matrix(k,[[f.decode(data[:,i,j]) for j in range(data.shape[2])]
                         for i in range(data.shape[1])])
    if actual(f.product(packed(left),packed(right)))!=left*right:
        raise ArithmeticError("The nonzero-linear-term packed product changed the original field")
    if actual(f.inverse_lower(packed(left)))!=left.inverse():
        raise ArithmeticError("The nonzero-linear-term packed triangular inverse failed")
    if f.decode(f.inverse_scalar(f.coords(a)))!=1/a:
        raise ArithmeticError("The nonzero-linear-term scalar inverse failed")
    case=manual_case(k)
    case.update(actual_modulus_discriminant=2,actual_structure_constants=[f.a,f.b],
                actual_ground_field_products_and_inverses_returned=True)
    return case


def main():
    # Reuse the exact previously software-PASSed small two-chart model and old full graph.
    reference=runpy.run_path(str(Path(__file__).with_name("check-original-adaptive-scalar-graph.py")))
    OldEngine=reference["TwoChartEngine"]
    original=reference["adaptive"].ORIGINAL_GRAPH
    k=GF(29**2,"z_short_fixture")
    manual=[manual_case(GF(29)),manual_case(k),nonzero_linear_term()]
    comparison_count=0
    admitted,declined=0,0
    rejected_outer=0
    rejected_subgraph=0
    for infinity in (False,True):
        E=OldEngine(k,infinity)
        R,t=E.R,E.R.gen()
        one=E.unit
        b=vector(R,[0,1])
        common=t*one+b
        cases=[(E.multiply(common,k.gen()*one+b),E.multiply(common,b)),
               (one,t**2*one),((t**3+1)*b,one),(one,(t+1+k.gen())*one+b)]
        for number,(N,D) in enumerate(cases):
            Xref,Yref,old=original(E.multiplication_matrix(N),E.multiplication_matrix(D),
                                   progress=E.progress,label="complete old small reference")
            positive_ref=Xref.hermite_form(include_zero_rows=False)
            def exact_reference(Y,X,H,G):
                if H!=Yref or G!=positive_ref:
                    raise ArithmeticError("The independently admitted original graph was a proper subgraph")
                return dict(complete_graph_for_this_full_original_function=True,
                            route="entire old small polynomial graph verified in this same case")
            # Feed real noncanonical generators; negative H is not the input basis.
            U=matrix(R,[[1,t+1],[0,1]])
            if number==0:
                U=matrix(R,[[1,k.gen()*t+1],[0,1]])
            args=(E,N,D,U*Yref,U*Xref,"small complete low graph",exact_reference,32,1)
            pos,neg,rec=gates.projected_pair_after_proof(*args)
            if pos.basis!=positive_ref or neg.basis!=Yref:
                raise ArithmeticError("The candidate changed a true small canonical ideal")
            inner=rec["kernel"]["all_rows"]
            if inner["complete_X_sha256"]!=polynomial_matrix_digest(Xref) or len(inner["complete_source_rows"])!=2:
                raise ArithmeticError("The candidate row-stream digest differs from the true old full X")
            if rec["post_ideal_outer"]["complete_X_sha256"]!=polynomial_matrix_digest(Xref):
                raise ArithmeticError("The actual post-ideal small full matrix stream did not return")
            comparison_count+=1
            if rec["kernel"]["negative_projection"]["admission"]["applied"]:
                admitted+=1
            else:
                declined+=1
            if number!=0:
                continue
            before=gates._ideal_from_certified_basis
            before_row=gates.require_outer_row
            created=[]
            def count_ideals(engine,basis,proof,label):
                result=before(engine,basis,proof,label)
                created.append(result)
                return result
            def corrupt_actual_row(h,x,inner_row,MN,MD,Hplus,cap):
                if len(created)==2:
                    x=vector(R,list(x))
                    x[0]+=t**7
                return before_row(h,x,inner_row,MN,MD,Hplus,cap)
            gates._ideal_from_certified_basis=count_ideals
            gates.require_outer_row=corrupt_actual_row
            try:
                gates.projected_pair_after_proof(*args)
            except ArithmeticError as err:
                if "complete post-ideal polynomial row changed" not in str(err) or len(created)!=2:
                    raise
                rejected_outer+=1
            else:
                raise AssertionError("A complete post-ideal high-degree corruption was accepted")
            finally:
                gates._ideal_from_certified_basis=before
                gates.require_outer_row=before_row
            # Equal fractional-field rank and zero equations survive this error.
            bad=matrix(R,[[t,0],[0,1]])*U
            try:
                gates.projected_pair_after_proof(E,N,D,bad*Yref,bad*Xref,"proper graph",
                                                 exact_reference,32,1)
            except ArithmeticError as err:
                if "proper subgraph" not in str(err):
                    raise
                rejected_subgraph+=1
            else:
                raise AssertionError("A full-rank proper integral graph was accepted")
    if not admitted or not declined or (comparison_count,rejected_outer,rejected_subgraph)!=(8,2,2):
        raise AssertionError("Not all intended original small software paths were exercised")
    result=dict(kind="original_short_graph_multichain_software_only",manual=manual,
                full_chart_comparisons=comparison_count,actual_prime_admissions=admitted,
                actual_quadratic_original_pairs=declined,actual_post_ideal_tamper_rejections=rejected_outer,
                actual_proper_subgraph_rejections=rejected_subgraph,production_geometry_claimed=False)
    print("RANK2_SHORT_GRAPH_MULTICHAIN_SOFTWARE_RESULT "+canonical(result),flush=True)
    print("RANK2_SHORT_GRAPH_MULTICHAIN_SOFTWARE_SHA256 "+digest(result),flush=True)


if __name__=="__main__":
    main()
