#!/usr/bin/env sage-python
"""Candidate complete low-weight graph admission and both actual-ideal row returns."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import hashlib
from sage.all import matrix, vector
from original_ys_divisor_ideal_tools import (
    canonical, digest, element_digest, field_description, finite_field_coordinates,
    polynomial_matrix_digest, _hermite_remainder_rows)
from original_w_ideal_transport import _ideal_from_certified_basis
from original_complete_quadratic_returns import complete_product
from original_short_graph_field import PackedField
from original_short_graph_multichain import multichain_hermite
from original_short_graph_popov import (
    PackedRow, admit_compact_pair, change_coefficients, complete_popov, divide_into_rows)


def freeze_matrix(A):
    result=matrix(A.base_ring(),[list(row) for row in A.rows()])
    result.set_immutable()
    return result


class MatrixRowDigest:
    def __init__(self, R, n):
        self.R,self.k,self.n,self.count=R,R.base_ring(),n,0
        self.hasher=hashlib.sha256(canonical(dict(
            encoding="original-affine-polynomial-matrix-v1", field=field_description(self.k),
            rows=n,columns=n)).encode())

    def append(self,row):
        if row.base_ring() is not self.R or len(row)!=self.n or self.count>=self.n:
            raise ArithmeticError("Malformed original polynomial-matrix row stream")
        self.hasher.update(b"\n")
        for polynomial in row:
            self.hasher.update(canonical([
                finite_field_coordinates(c,self.k) for c in polynomial.list()]).encode())
            self.hasher.update(b";")
        self.count+=1

    def finish(self):
        if self.count!=self.n:
            raise ArithmeticError("The full original matrix digest ended before the last row")
        return self.hasher.hexdigest()


def projection_return(Y,X,bound,progress=None,try_prime=True):
    R=Y.base_ring()
    y,x,admission=admit_compact_pair(Y,X,try_prime=try_prime)
    B,C,pop=complete_popov(y,x)
    H,chains=multichain_hermite(B,degree_bound=bound,progress=progress)
    if B.base_ring() is not R:
        B=change_coefficients(B,R)
        C=None if C is None else change_coefficients(C,R)
        H=change_coefficients(H,R)
    # The original-domain reverse inclusion follows the full Popov/triangular
    # coordinates, and does not rely on a descent hash.
    original_rows=[PackedRow(R,PackedField(R.base_ring()),row) for row in B.rows()]
    pivots=[int(B[i,i].degree()) for i in range(int(B.nrows()))]
    for i,start in enumerate(Y.rows()):
        r=divide_into_rows(start,original_rows,pivots)
        if r*B!=start or (C is not None and r*C!=X.row(i)):
            raise ArithmeticError("The entire original-domain projected pair did not round-trip")
    for h in H.rows():
        if divide_into_rows(h,original_rows,pivots)*B!=h:
            raise ArithmeticError("An actual original-domain Hermite row missed the original projection")
    if not _hermite_remainder_rows(Y,H).is_zero() or not _hermite_remainder_rows(B,H).is_zero():
        raise ArithmeticError("Original projected-polynomial-module inclusion failed")
    return H,B,C,dict(admission=admission,popov=pop,multichain=chains,
                      original_hnf_sha256=polynomial_matrix_digest(H))


class PairedSource:
    def __init__(self,H,B,C):
        if H.base_ring() is not B.base_ring() or B.base_ring() is not C.base_ring():
            raise ValueError("An immutable graph must use a single original ring")
        self.H,self.B,self.C=(freeze_matrix(A) for A in (H,B,C))
        self.R=self.B.base_ring()
        self.n=int(H.nrows())
        self.degrees=[int(self.B[j,j].degree()) for j in range(self.n)]
        k=PackedField(self.R.base_ring())
        self.rows=[PackedRow(self.R,k,row) for row in self.B.rows()]
        for row in self.rows:
            row.data.setflags(write=False)

    def decode(self,h):
        r=divide_into_rows(h,self.rows,self.degrees)
        if r*self.B!=h:
            raise ArithmeticError("A canonical source row did not return exactly from compact coordinates")
        return r*self.C


def original_operator_product(h,M):
    return complete_product(matrix(M.base_ring(),[h]),M).row(0)


def require_outer_row(h,x,reference,MN,MD,positive_H,degree_cap):
    if x!=reference:
        raise ArithmeticError("The complete post-ideal polynomial row changed")
    if any(q and q.degree()>degree_cap for q in x):
        raise ArithmeticError("An actual integral image exceeded the complete geometric row bound")
    if original_operator_product(x,MD)!=original_operator_product(h,MN):
        raise ArithmeticError("The original full polynomial numerator and denominator did not return")
    if not _hermite_remainder_rows(matrix(h.base_ring(),[x]),positive_H).is_zero():
        raise ArithmeticError("The complete image row is outside the actual positive Hermite ideal")


def graph_scan(source,H,positive_H,MN,MD,degree_cap,reference=None):
    R,n=source.R,source.n
    stream=MatrixRowDigest(R,n)
    records=[]
    count=0
    for i in range(n):
        h=H.row(i)
        x=source.decode(h)
        if reference is None:
            original=x
        else:
            h_in=reference.H.row(i)
            if h_in!=h:
                raise ArithmeticError("The actual post-construction negative source changed")
            # Decode, in full, the distinct immutable inner representation.
            original=reference.decode(h_in)
        require_outer_row(h,x,original,MN,MD,positive_H,degree_cap)
        count+=sum(len(q.list()) for q in x)
        stream.append(x)
        records.append(dict(index=i,actual_source_sha256=element_digest(h),
                            complete_X_row_sha256=element_digest(x),exact_full_residual_zero=True))
    return dict(complete_hermite_sha256=polynomial_matrix_digest(H),
                complete_X_sha256=stream.finish(),actual_returned_X_cells=count,
                complete_source_rows=records)


def projected_pair_after_proof(engine,numerator,denominator,Y,X,label,admit_complete,
                               projective_pole_degree,max_weight,try_prime=True):
    """Caller supplies either the real RR admission below or a complete fixture reference."""
    R,n=engine.R,int(engine.dimension)
    if Y.base_ring() is not R or X.base_ring() is not R or (
            Y.dimensions()!=(n,n) or X.dimensions()!=(n,n)):
        raise ValueError("Expected all rows of both original square low graph projections")
    N,D=engine.element(numerator),engine.element(denominator)
    if N.is_zero() or D.is_zero():
        raise ValueError("Both original endpoint elements must be nonzero")
    MN,MD=engine.multiplication_matrix(N),engine.multiplication_matrix(D)
    if engine.unit*MN!=N or engine.unit*MD!=D:
        raise ArithmeticError("The complete actual unit did not recover the original maps")
    for i in range(n):
        if original_operator_product(Y.row(i),MN)!=original_operator_product(X.row(i),MD):
            raise ArithmeticError("An input low-weight pair failed the original polynomial equation")
    H,B,C,minus=projection_return(Y,X,projective_pole_degree,engine.progress,try_prime)
    G,unused,unused_side,plus=projection_return(X,None,projective_pole_degree,engine.progress,try_prime)
    if unused_side is not None:
        raise ArithmeticError("The independent positive projection unexpectedly gained an attached block")
    # Both full-rank projection proofs now exist. A proper subgraph obeys the
    # same equations and cannot be admitted merely by its rank.
    completeness=admit_complete(Y,X,H,G)
    source=PairedSource(H,B,C)
    degree_cap=projective_pole_degree+max_weight
    inner=graph_scan(source,H,G,MN,MD,degree_cap)
    certificate=dict(label=label,complete_low_graph=completed_identity(completeness),
                     negative_projection=minus,positive_projection=plus,all_rows=inner,
                     original_G_N_sha256=element_digest(N),original_G_D_sha256=element_digest(D),
                     full_MN_sha256=polynomial_matrix_digest(MN),full_MD_sha256=polynomial_matrix_digest(MD))
    positive=_ideal_from_certified_basis(engine,freeze_matrix(G),certificate,label+": complete zero ideal")
    negative=_ideal_from_certified_basis(engine,freeze_matrix(H),certificate,label+": complete pole ideal")
    if positive.engine is not engine or negative.engine is not engine:
        raise ArithmeticError("The two constructed ideals do not belong to the same original engine")
    for ideal,basis in ((negative,H),(positive,G)):
        if ideal.basis!=basis or not ideal.basis.is_hermite() or not ideal.receipt[
                "both_polynomial_row_module_inclusions_verified"]:
            raise ArithmeticError("The actual constructed original Hermite ideal did not return")
    actual_N,actual_D=engine.element(numerator),engine.element(denominator)
    if actual_N!=N or actual_D!=D:
        raise ArithmeticError("The actual original numerator or denominator changed after construction")
    current_MN=engine.multiplication_matrix(actual_N)
    current_MD=engine.multiplication_matrix(actual_D)
    if current_MN!=MN or current_MD!=MD or engine.unit*current_MN!=N or engine.unit*current_MD!=D:
        raise ArithmeticError("An actual post-ideal original multiplication operator changed")
    # Both views are independent of the matrices supplied to the constructors.
    current=PairedSource(negative.basis,B,C)
    for i in range(n):
        if original_operator_product(current.B.row(i),current_MN)!=original_operator_product(current.C.row(i),current_MD):
            raise ArithmeticError("The actual low graph failed after both original ideals existed")
    outer=graph_scan(current,negative.basis,positive.basis,current_MN,current_MD,degree_cap,
                     reference=source)
    if outer!=inner:
        raise ArithmeticError("The complete inner and post-ideal original matrix streams differ")
    identity=dict(label=label,actual_engine_id=id(engine),infinity_chart=engine.infinity_chart,
                  actual_numerator_input_id=id(numerator),actual_denominator_input_id=id(denominator),
                  actual_positive_id=id(positive),actual_negative_id=id(negative),
                  source_row_count_verified_after_both_ideals=n,
                  positive_hnf_sha256=polynomial_matrix_digest(positive.basis),
                  negative_hnf_sha256=polynomial_matrix_digest(negative.basis),
                  complete_post_ideal_row_stream_sha256=digest(outer["complete_source_rows"]),
                  actual_positive_zero_length=int(positive.length),actual_negative_pole_length=int(negative.length),
                  omitted_fiber_zero_length=int(projective_pole_degree-positive.length),
                  omitted_fiber_pole_length=int(projective_pole_degree-negative.length),
                  complete_X_sha256=outer["complete_X_sha256"])
    return positive,negative,dict(kernel=certificate,post_ideal_outer=identity)


def completed_identity(proof):
    if not isinstance(proof,dict) or proof.get("complete_graph_for_this_full_original_function") is not True:
        raise ArithmeticError("The supplied paired rows lack the entire graph admission")
    return proof


def fixed_endpoint_after_low_graph(engine,six,index,Y,X,original_engines):
    if index not in (0,1) or type(engine.infinity_chart) is not bool:
        raise ValueError("Only the four specified chart/endpoints are covered by the RR admission")
    N0=306
    if (original_engines[engine.infinity_chart] is not engine or
            six["kind"]!="rank2_original_Y_fraction_consumer_context" or int(six["prime"])!=29):
        raise ValueError("A different original chart registry or fraction context was supplied")
    weights=[int(v) for v in engine.chart["original_basis_weights"]]
    if (int(engine.dimension)!=N0 or int(engine.R.base_ring().characteristic())!=29 or
            len(weights)!=N0 or [weights.count(j) for j in range(5)]!=[1,0,65,226,14]):
        raise ValueError("The actual original r29 integral basis is required")
    function=six["A"][index]["y0"]
    model=six["model"]
    if (function.model is not model or model.k is not engine.k or
            (model.S if engine.infinity_chart else model.P) is not engine.R or tuple(weights)!=tuple(model.weights)):
        raise ValueError("The current original chart and the actual endpoint model do not agree")
    numerator,denominator=function.chart_pair(engine.infinity_chart)
    def rr_admission(Y0,X0,H,G):
        rho=[]
        for i in range(N0):
            rho.append(max(int(q.degree())+weights[j]
                           for block in (Y0,X0) for j,q in enumerate(block.row(i)) if q))
        if max(rho)>13 or sum(rho)!=3120 or sum(14-r for r in rho)!=1164:
            raise ArithmeticError("The actual low graph does not exhaust the RR dimension")
        # First projection has rank 306, as independently certified from its
        # real full Popov/Hermite inputs. All 1164 shifts are independent.
        if not H.is_hermite() or not G.is_hermite() or any(
                not H[i,i] or not G[i,i] for i in range(N0)):
            raise ArithmeticError("Actual complete low pair projections are not full rank")
        return dict(complete_graph_for_this_full_original_function=True,
                    route="R883/R925 original 2256/559 degree13 full RR graph",
                    actual_original_function_id=id(function),actual_chart=engine.infinity_chart,
                    actual_original_endpoint=index,original_paired_weights=rho,
                    full_independent_shift_count=1164,complete_RR_dimension=1164)
    p,m,rec=projected_pair_after_proof(engine,numerator,denominator,Y,X,
        "original A%d y0"%index,rr_admission,2256,max(weights))
    current=function.chart_pair(engine.infinity_chart)
    if current[0] is not numerator or current[1] is not denominator:
        raise ArithmeticError("The actual original chart-pair object binding changed")
    return p,m,rec
