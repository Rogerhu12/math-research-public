#!/usr/bin/env sage-python
"""Small software fixtures only. No original geometry or shadow is implied."""
import os
if (os.environ.get('GITHUB_ACTIONS')!='true' or
        os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
    raise SystemExit('Use only the public research Actions.')
from sage.all import GF,PolynomialRing,matrix,vector,identity_matrix
import original_adaptive_scalar_graph as adaptive
from original_adaptive_dixon_solver import OneRightHandSide
from original_ys_divisor_ideal_tools import canonical,digest


class TwoChartEngine(adaptive.values.OriginalTriangularIdealEngine):
    """k[t,b]/(b^2-t), with reciprocal basis c=s*b satisfying c^2=s."""
    def __init__(self,k,infinity):
        self.k,self.dimension,self.infinity_chart=k,2,infinity
        self.R=PolynomialRing(k,'s_test' if infinity else 't_test')
        self.unit=vector(self.R,[1,0])
        self.identity=identity_matrix(self.R,2)
        self.kernel_method='minimal'
        self.progress=lambda *a,**kw: None
        self.chart={'original_basis_weights':(0,1)}

    def multiplication_matrix(self,v):
        p,b=self.element(v)
        return matrix(self.R,[[p,b],[self.R.gen()*b,p]])

    def multiply(self,u,v):
        return self.element(u)*self.multiplication_matrix(v)


def compare(engine,N,D,name):
    MN,MD=engine.multiplication_matrix(N),engine.multiplication_matrix(D)
    Xref,Yref,old=adaptive.ORIGINAL_GRAPH(MN,MD,progress=engine.progress,label='exact reference '+name)
    pos,neg,receipt=adaptive.zero_pole_ideals(engine,N,D,name)
    graph=receipt['kernel']
    assert neg.basis==Yref and pos.basis==Xref.hermite_form(include_zero_rows=False)
    assert graph['all_rows']['complete_X_sha256']==adaptive.polynomial_matrix_digest(Xref)
    assert Xref*MD==Yref*MN
    assert graph['all_rows']['complete_hermite_sha256']==adaptive.polynomial_matrix_digest(Yref)
    assert len(graph['all_rows']['complete_source_rows'])==2
    assert receipt['post_ideal_outer']['X_sha256']==graph['all_rows']['complete_X_sha256']
    return graph


def main():
    counts=[]
    k=GF(29**2,'z_test')
    for infinity in (False,True):
        E=TwoChartEngine(k,infinity)
        t=E.R.gen()
        b,e=vector(E.R,[0,1]),E.unit
        shared=t*e+b
        cases=[(E.multiply(shared,k.gen()*e+b),E.multiply(shared,b),'non-scalar common factor'),
               (e,t**2*e,'both nilpotent branches of the full scalar congruence'),
               ((t**3+1)*b,e,'integral map constant denominator'),
               (e,(t+1+k.gen())*e+b,'nontrivial original quadratic coefficients')]
        for N,D,name in cases:
            g=compare(E,N,D,name)
            counts.append(len(g['refinements']))
            if name.startswith('both nilpotent'):
                assert len(g['refinements'])==2
        N,D=cases[0][:2]
        MN,MD=E.multiplication_matrix(N),E.multiplication_matrix(D)
        session=adaptive.EndpointGraph(E,N,D,MN,MD)
        # Corrupt the ACTUAL returned matrix only after its positive HNF and
        # both real ideal objects exist. The low t^d residue stays unchanged.
        original_ideal_from_rows=E.ideal_from_rows
        pending=[]
        def mutate_after_both(rows,label,provenance=None):
            answer=original_ideal_from_rows(rows,label,provenance=provenance)
            if label.endswith(': complete zero ideal'):
                pending.append(rows)
            elif label.endswith(': complete pole ideal'):
                assert len(pending)==1
                pending[0][0,0]+=t**session.d
            return answer
        before=(len(adaptive.INNER),len(adaptive.OUTER))
        E.ideal_from_rows=mutate_after_both
        try:
            adaptive.zero_pole_ideals(E,N,D,'deliberate post-ideal t^d corruption',register=True)
        except ArithmeticError as exc:
            assert 'changed its complete polynomial part' in str(exc)
        else:
            raise AssertionError('The full post-ideal polynomial-part check admitted a changed t^d multiple')
        finally:
            del E.ideal_from_rows
        assert (len(adaptive.INNER),len(adaptive.OUTER))==(before[0]+1,before[1])
        before=(len(adaptive.INNER),len(adaptive.OUTER))
        try:
            adaptive.zero_pole_ideals(E,N,D,'deliberate true output budget rejection',
                                      max_returned_coefficients=1,register=True)
        except MemoryError as exc:
            assert 'actual complete X' in str(exc)
        else:
            raise AssertionError('The complete output guard did not reject')
        assert (len(adaptive.INNER),len(adaptive.OUTER))==before
    # No linear base point is good here. Exercise a genuine degree-two
    # residue place and the transpose over original indices at that same place.
    fp=GF(29)
    R=PolynomialRing(fp,'x_test')
    x=R.gen()
    M=matrix(R,[[x**29-x,1],[0,x*x+x+1]])
    solver=OneRightHandSide(M)
    assert solver.e==2
    target=vector(R,[1,x+3])
    W,q,rec=solver.reconstruct_row(target,40,40,lambda w,q:w*M==q*target)
    assert W*M==q*target
    trans=solver.transposed()
    w,q,rec=trans.reconstruct_row(target,40,40,lambda w,q:w*M.transpose()==q*target)
    assert w*M.transpose()==q*target
    payload=dict(kind='small_adaptive_graph_software_only',comparisons=len(counts),
        refinements_by_case=counts,actual_post_ideal_polynomial_part_tamper_rejections=2,
        actual_final_X_budget_rejections_before_any_new_audit=2,
        nonlinear_good_place_and_true_transpose=True,original_geometry_claimed=False)
    print('RANK2_ADAPTIVE_SCALAR_GRAPH_SOFTWARE_RESULT '+canonical(payload),flush=True)
    print('RANK2_ADAPTIVE_SCALAR_GRAPH_SOFTWARE_SHA256 '+digest(payload),flush=True)

if __name__=='__main__':
    main()
