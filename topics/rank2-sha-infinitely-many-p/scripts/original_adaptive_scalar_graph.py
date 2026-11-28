#!/usr/bin/env sage-python
"""Complete selected original zero/pole graphs from one fraction and exact adaptive constraints."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research Actions.")

from copy import deepcopy
from collections import OrderedDict
import hashlib
from pathlib import Path
from sage.all import matrix, vector, identity_matrix
import original_triangular_artinian_values as values
import original_complete_quadratic_returns as quadratic
from original_ys_divisor_ideal_tools import (polynomial_digest,polynomial_matrix_digest,
                                            element_digest,digest)
from original_adaptive_dixon_solver import OneRightHandSide

IMPLEMENTATION = 'original-adaptive-scalar-graph-laurent-residual-v1'
ENDPOINT_LABELS = frozenset(('original A0 y0','original A1 y0'))
ORIGINAL_ZERO_POLES = values.OriginalTriangularIdealEngine.zero_pole_ideals
ORIGINAL_INTEGRAL_MULTIPLE = values.OriginalTriangularIdealEngine.integral_fraction_multiple
INNER, OUTER = [], []


def _weight(row,weights):
    return max(int(p.degree())+d for p,d in zip(row,weights) if p)


def _row_product(row,M):
    return quadratic.complete_product(matrix(M.base_ring(),[row]),M).row(0)


def _dot_mod(row,column,q):
    R = q.parent()
    return sum((x*y for x,y in zip(row,column) if x and y),R.zero())%q


def _tail_reduce(row,H,start):
    for j in range(start,H.nrows()):
        if row[j]:
            quotient,unused = row[j].quo_rem(H[j,j])
            if quotient:
                row -= quotient*H.row(j)
    return row


def refine(H,column,q):
    """One complete scalar congruence, directly in the old H coordinates."""
    R,n = H.base_ring(),H.nrows()
    c = [_dot_mod(row,column,q) for row in H.rows()]
    out = matrix(R,n,n,0)
    lift,beta = vector(R,n),q
    steps = []
    for i in reversed(range(n)):
        beta_i,u,v = c[i].xgcd(beta)
        scale = R.base_ring().one()/beta_i.leading_coefficient()
        beta_i,u,v = scale*beta_i,scale*u,scale*v
        assert u*c[i]+v*beta==beta_i
        a,rem_a = beta.quo_rem(beta_i)
        b,rem_b = c[i].quo_rem(beta_i)
        assert not rem_a and not rem_b
        candidate = _tail_reduce(a*H.row(i)-b*lift,out,i+1)
        assert candidate[i]==a*H[i,i] and all(not candidate[j] for j in range(i))
        assert not _dot_mod(candidate,column,q)
        out.set_row(i,candidate)
        lift = _tail_reduce(u*H.row(i)+v*lift,out,i)
        assert _dot_mod(lift,column,q)==beta_i%q
        steps.append((i,int(a.degree()),polynomial_digest(beta_i)))
        beta = beta_i
    assert out.is_hermite()
    assert quadratic.complete_remainder_rows(out,H).is_zero()
    return out,dict(suffix_bezout_pivots=steps,complete_original_congruence_rows=n,
        complete_source_hnf_sha256=polynomial_matrix_digest(H),
        returned_hnf_sha256=polynomial_matrix_digest(out))


def _rev(p):
    return p.parent()(list(reversed(p.list())))


class LaurentWindows:
    """True b_j*f windows with individually sufficient lower endpoints."""
    def __init__(self,engine,W,q,weights,cache_coefficients=2000000):
        self.engine,self.R,self.n = engine,engine.R,engine.dimension
        self.W,self.q,self.weights = W,q,weights
        self.U = _weight(W,weights)-int(q.degree())
        self.multiplier_degree_bound = 2*max(weights)
        self.cached = OrderedDict()
        self.cache_limit = int(cache_coefficients)
        self.cache_cells = self.cache_peak = 0
        self.precision = 0
        self.series = [self.R.zero() for unused in range(self.n)]

    def ensure(self,needed):
        if needed<=self.precision:
            return
        R,t=self.R,self.R.gen()
        modulus=t**needed
        qr=_rev(self.q)
        g,inv,unused=qr.xgcd(modulus)
        assert g.degree()==0
        inv=(inv*(R.base_ring().one()/g[0]))%modulus
        assert (qr*inv)%modulus==1
        series=[]
        for p in self.W:
            if not p:
                series.append(R.zero())
                continue
            shift=self.U+int(self.q.degree())-int(p.degree())
            assert shift>=0
            target=(t**shift*_rev(p))%modulus
            component=(target*inv)%modulus
            assert (qr*component)%modulus==target
            series.append(component)
        self.precision,self.series=needed,series

    def row(self,j,depth):
        saved=self.cached.pop(j,None)
        if saved is not None:
            saved_depth,saved_cells,saved_row=saved
            if saved_depth==depth:
                self.cached[j]=saved
                return saved_row
            self.cache_cells-=saved_cells
        R,t=self.R,self.R.gen()
        lower=depth+self.multiplier_degree_bound
        count=max(0,self.U+lower+1)
        self.ensure(count)
        if count:
            truncated=vector(R,[R([p[v] for v in reversed(range(count))]) for p in self.series])
            basis=vector(R,self.n)
            basis[j]=1
            product=self.engine.multiply(basis,truncated)
            drop=t**self.multiplier_degree_bound
            result=vector(R,[entry//drop for entry in product])
        else:
            result=vector(R,self.n)
        for i,p in enumerate(result):
            assert not p or p.degree()<=depth+self.U+self.weights[j]-self.weights[i]
        cells=sum(int(p.degree())+1 for p in result if p)
        if cells<=self.cache_limit:
            while self.cached and self.cache_cells+cells>self.cache_limit:
                unused,evicted=self.cached.popitem(last=False)
                self.cache_cells-=evicted[1]
            self.cached[j]=(depth,cells,result)
            self.cache_cells+=cells
            self.cache_peak=max(self.cache_peak,self.cache_cells)
        return result

    def polynomial_part(self,row,depths):
        R,t=self.R,self.R.gen()
        value=vector(R,self.n)
        for j,h in enumerate(row):
            if not h:
                continue
            depth=depths[j]
            assert h.degree()<=depth
            window=self.row(j,depth)
            shift=t**depth
            if depth:
                value+=vector(R,[(h*p)//shift for p in window])
            else:
                value+=h*window
        return value


class EndpointGraph:
    def __init__(self,engine,N,D,MN,MD,projective_pole_bound=None,limit=32000000):
        self.engine,self.R,self.n=engine,engine.R,int(engine.dimension)
        self.N,self.D,self.MN,self.MD=N,D,MN,MD
        self.limit=int(limit)
        self.weights=tuple(int(d) for d in engine.chart['original_basis_weights'])
        assert len(self.weights)==self.n and min(self.weights)>=0
        self.solver=OneRightHandSide(MD,progress=engine.progress)
        self.transpose_solver=None
        dD,wN=_weight(D,self.weights),_weight(N,self.weights)
        a,b=(self.n-1)*dD+wN,self.n*dD
        if projective_pole_bound is not None:
            a,b=min(a,int(projective_pole_bound)),min(b,int(projective_pole_bound))
        self.W,self.q,self.solve_record=self.solver.reconstruct_row(
            N,a,b,lambda W,q: _row_product(W,MD)==q*N)
        engine.progress('complete original endpoint single RHS returned',
            infinity_chart=engine.infinity_chart, scalar_denominator_degree=int(self.q.degree()),
            actual_normalization_weight=_weight(self.W,self.weights),one_rhs=self.solve_record)
        self.wW=_weight(self.W,self.weights)
        self.d=self.solver.d
        self.modulus=self.R.gen()**self.d if self.d else None
        def low(M):
            return matrix(self.R,[[x%self.modulus for x in row] for row in M.rows()])
        self.low_N,self.low_D=(low(MN),low(MD)) if self.d else (None,None)
        self.refinements=[]
        self.MD_hash,self.MN_hash=polynomial_matrix_digest(MD),polynomial_matrix_digest(MN)

    def _residual(self,h,x):
        if not self.d:
            return _row_product(h,self.MN)-_row_product(x,self.MD)
        def low(v):
            return vector(self.R,[p%self.modulus for p in v])
        return low(_row_product(low(h),self.low_N)-_row_product(low(x),self.low_D))

    def _witness(self,residual):
        S=vector(self.R,residual)
        while all(not (p%self.solver.pi) for p in S):
            S=vector(self.R,[p//self.solver.pi for p in S])
        u=self.solver.solve_residue(S)
        return next(j for j,p in enumerate(u) if p)

    def _full_column(self,j):
        if self.transpose_solver is None:
            self.transpose_solver=self.solver.transposed()
        RHS=self.MN.column(j)
        def verify(column):
            return _row_product(column,self.transpose_solver.M)==self.q*RHS
        cap=max(self.weights)+self.wW-self.weights[j]
        return self.transpose_solver.scaled_polynomial_solution(RHS,self.q,cap,verify)

    def scan(self,H,windows,expected_X=None):
        depths=[int(H[i,i].degree()) for i in range(self.n)]
        rows=[]
        X=matrix(self.R,self.n,self.n,0) if expected_X is None else expected_X
        cell_count=0
        for i,h in enumerate(H.rows()):
            x=windows.polynomial_part(h,depths)
            if expected_X is not None and x!=expected_X.row(i):
                raise ArithmeticError("The actual returned row changed its complete polynomial part")
            residual=self._residual(h,x)
            if not residual.is_zero():
                if expected_X is not None:
                    raise ArithmeticError("A post-ideal full row identity failed")
                return None,(i,self._witness(residual),element_digest(residual)),None
            cell_count+=sum(len(p.list()) for p in x)
            # Only enforce this final-output guard if all source rows eventually pass.
            if expected_X is None and cell_count<=self.limit:
                X.set_row(i,x)
            rows.append(dict(index=i,actual_source_sha256=element_digest(h),
                complete_X_row_sha256=element_digest(x),exact_full_residual_zero=True))
        if cell_count>self.limit:
            raise MemoryError("The actual complete X exceeds the configured final-output coefficient budget")
        return X,None,dict(complete_source_rows=rows,actual_returned_X_cells=cell_count,
            degree_strict_upper_bound_on_entire_residual=self.d,
            complete_hermite_sha256=polynomial_matrix_digest(H),
            complete_X_sha256=polynomial_matrix_digest(X))

    def compute(self):
        H=identity_matrix(self.R,self.n)
        windows=LaurentWindows(self.engine,self.W,self.q,self.weights)
        used=set()
        while True:
            X,rejection,scan=self.scan(H,windows)
            if rejection is None:
                return X,H,dict(implementation=IMPLEMENTATION,
                    complete_denominator_operator_sha256=self.MD_hash,
                    complete_numerator_operator_sha256=self.MN_hash,
                    numerator_sha256=element_digest(self.N),denominator_sha256=element_digest(self.D),
                    q_sha256=polynomial_digest(self.q),W_sha256=element_digest(self.W),
                    one_rhs=self.solve_record,refinements=self.refinements,all_rows=scan,
                    retained_window_cache_peak_coefficients=windows.cache_peak,
                    retained_window_cache_budget_coefficients=windows.cache_limit,
                    full_global_paired_identity_returned=True,
                    all_original_denominator_source_vectors_retained=True,
                    complete_graph_dual_inclusions_verified=True,
                    denominator_hnf_executed=False,full_universal_inverse_materialized=False)
            source_row,j,residual_hash=rejection
            if j in used or len(used)>=self.n:
                raise ArithmeticError("Repeated or impossible true nonintegral coordinate")
            column=self._full_column(j)
            if not _dot_mod(H.row(source_row),column,self.q):
                raise ArithmeticError("Failure witness did not exclude its actual original source")
            H,rec=refine(H,column,self.q)
            rec.update(original_output_column=j,excluded_source_row=source_row,
                       complete_residual_sha256=residual_hash,complete_column_sha256=element_digest(column))
            self.refinements.append(rec)
            used.add(j)
            self.engine.progress('complete scalar graph original coordinate admitted',
                infinity_chart=self.engine.infinity_chart, rejected_actual_row=source_row,
                new_original_column=j, admitted_columns=len(used),
                full_constraint_hnf_sha256=rec['returned_hnf_sha256'])


def zero_pole_ideals(engine,numerator,denominator,label,projective_pole_bound=None,
                     max_returned_coefficients=32000000,register=False):
    N,D=engine.element(numerator),engine.element(denominator)
    if N.is_zero() or D.is_zero():
        raise ValueError("Both selected zero/pole source elements must be nonzero")
    MN,MD=engine.multiplication_matrix(N),engine.multiplication_matrix(D)
    assert _row_product(engine.unit,MN)==N and _row_product(engine.unit,MD)==D
    graph=EndpointGraph(engine,N,D,MN,MD,projective_pole_bound,max_returned_coefficients)
    X,H,record=graph.compute()
    identity=dict(label=label,actual_engine_id=id(engine),infinity_chart=engine.infinity_chart,
        actual_numerator_input_id=id(numerator),actual_denominator_input_id=id(denominator),
        original_source_count=engine.dimension,source_N_sha256=element_digest(N),
        source_D_sha256=element_digest(D),MN_sha256=graph.MN_hash,MD_sha256=graph.MD_hash,
        H_sha256=record['all_rows']['complete_hermite_sha256'],
        X_sha256=record['all_rows']['complete_X_sha256'],graph_receipt_sha256=digest(record))
    if register:
        INNER.append(dict(identity))
    positive=engine.ideal_from_rows(X,label+': complete zero ideal',provenance=record)
    negative=engine.ideal_from_rows(H,label+': complete pole ideal',provenance=record)
    assert positive.engine is negative.engine is engine and negative.basis==H
    for ideal in (positive,negative):
        assert polynomial_matrix_digest(ideal.basis)==ideal.receipt['full_hermite_basis_sha256']
        assert ideal.receipt['both_polynomial_row_module_inclusions_verified']
    assert _row_product(graph.W,MD)==graph.q*N
    assert engine.element(numerator)==N and engine.element(denominator)==D
    assert polynomial_matrix_digest(MN)==graph.MN_hash and polynomial_matrix_digest(MD)==graph.MD_hash
    # Rebuild the original source windows and ALL low residue operators after
    # both actual ideals exist. The retained paired rows themselves are compared.
    if graph.d:
        graph.low_N=matrix(engine.R,[[p%graph.modulus for p in row] for row in MN.rows()])
        graph.low_D=matrix(engine.R,[[p%graph.modulus for p in row] for row in MD.rows()])
    X_outer,rejection,outer=graph.scan(negative.basis,
        LaurentWindows(engine,graph.W,graph.q,graph.weights),expected_X=X)
    assert X_outer is X and rejection is None and outer==record['all_rows']
    outer_record=dict(identity,actual_positive_id=id(positive),actual_negative_id=id(negative),
        positive_hnf_sha256=polynomial_matrix_digest(positive.basis),
        negative_hnf_sha256=polynomial_matrix_digest(negative.basis),
        positive_ideal_receipt_sha256=digest(positive.receipt),negative_ideal_receipt_sha256=digest(negative.receipt),
        source_row_count_verified_after_both_ideals=len(outer['complete_source_rows']),
        complete_post_ideal_row_stream_sha256=digest(outer['complete_source_rows']))
    if register:
        OUTER.append(dict(outer_record))
    return positive,negative,dict(original_function=label,numerator_sha256=element_digest(N),
        denominator_sha256=element_digest(D),zero_ideal=positive.receipt,pole_ideal=negative.receipt,
        kernel=record,post_ideal_outer=outer_record,concrete_implementation=IMPLEMENTATION,
        only_this_affine_chart=True,closed_points_or_shadow_claimed=False)


ORIGINAL_GRAPH=values.complete_paired_fraction_graph
SOURCE_DEPENDENCIES=tuple(dict.fromkeys(('original_adaptive_scalar_graph.py',
    'original_adaptive_dixon_solver.py')+values.SOURCE_DEPENDENCIES+quadratic.SOURCE_DEPENDENCIES))


def _selected(engine,numerator,denominator,label='original function'):
    if label not in ENDPOINT_LABELS:
        return ORIGINAL_ZERO_POLES(engine,numerator,denominator,label)
    assert engine.dimension==306 and type(engine.infinity_chart) is bool
    return zero_pole_ideals(engine,numerator,denominator,label,2256,register=True)


def bind_original_endpoint_graphs():
    assert hashlib.sha256(Path(values.__file__).read_bytes()).hexdigest()=='9327760e26f1666dcd04a22b964b3b15a67b3e7d66e4f66bee84dd350b73db5d'
    cls=values.OriginalTriangularIdealEngine
    assert ORIGINAL_ZERO_POLES.__module__==values.__name__ and ORIGINAL_ZERO_POLES.__name__=='zero_pole_ideals'
    assert ORIGINAL_GRAPH.__module__==values.__name__ and ORIGINAL_GRAPH.__name__=='complete_paired_fraction_graph'
    assert cls.zero_pole_ideals is ORIGINAL_ZERO_POLES
    assert values.complete_paired_fraction_graph is ORIGINAL_GRAPH
    assert cls.integral_fraction_multiple is ORIGINAL_INTEGRAL_MULTIPLE
    assert not INNER and not OUTER
    cls.zero_pole_ideals=_selected
    return dict(implementation=IMPLEMENTATION,selected_labels=sorted(ENDPOINT_LABELS),
        general_graph_untouched=True,old_integral_fraction_multiple_untouched=True,
        actual_mathematical_instances_from_binding=0)


def actual_endpoint_usage(context):
    """Consume the four concrete calls, including their original source object identities."""
    assert context['certificate']['status']=='all_requested_original_acceptance_gates_completed'
    assert values.OriginalTriangularIdealEngine.zero_pole_ideals is _selected
    assert values.complete_paired_fraction_graph is ORIGINAL_GRAPH
    assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_INTEGRAL_MULTIPLE
    geometry,six=context['geometry'],context['six']
    assert geometry['six'] is six and len(INNER)==len(OUTER)==4
    expected_inner,expected_outer=[],[]
    for index in (0,1):
        fn=six['A'][index]['y0']
        entry=geometry['endpoint_poles'][index]['y0']
        assert entry is geometry['complete_principal_divisor_cache'][id(fn)] and entry['function'] is fn
        label='original A%d y0'%index
        for flag in (False,True):
            engine=geometry['engines'][flag]
            assert engine.infinity_chart is flag
            N,D=fn.chart_pair(flag)
            record=entry['records'][str(flag)]
            graph,after=record['kernel'],record['post_ideal_outer']
            assert graph['implementation']==IMPLEMENTATION and record['original_function']==label
            assert element_digest(N)==graph['numerator_sha256']==record['numerator_sha256']
            assert element_digest(D)==graph['denominator_sha256']==record['denominator_sha256']
            ret=graph['all_rows']
            assert [r['index'] for r in ret['complete_source_rows']]==list(range(306))
            assert all(r['exact_full_residual_zero'] for r in ret['complete_source_rows'])
            assert graph['full_global_paired_identity_returned'] and graph['complete_graph_dual_inclusions_verified']
            assert graph['all_original_denominator_source_vectors_retained'] and not graph['denominator_hnf_executed']
            positive,negative=(entry['charts'][flag][s] for s in ('positive','negative'))
            assert positive.engine is negative.engine is engine
            assert record['zero_ideal']==positive.receipt and record['pole_ideal']==negative.receipt
            core=dict(label=label,actual_engine_id=id(engine),infinity_chart=flag,
                actual_numerator_input_id=id(N),actual_denominator_input_id=id(D),original_source_count=306,
                source_N_sha256=element_digest(N),source_D_sha256=element_digest(D),
                MN_sha256=graph['complete_numerator_operator_sha256'],MD_sha256=graph['complete_denominator_operator_sha256'],
                H_sha256=polynomial_matrix_digest(negative.basis),X_sha256=ret['complete_X_sha256'],
                graph_receipt_sha256=digest(graph))
            assert core['H_sha256']==ret['complete_hermite_sha256']
            exp=dict(core,actual_positive_id=id(positive),actual_negative_id=id(negative),
                positive_hnf_sha256=polynomial_matrix_digest(positive.basis),negative_hnf_sha256=core['H_sha256'],
                positive_ideal_receipt_sha256=digest(positive.receipt),negative_ideal_receipt_sha256=digest(negative.receipt),
                source_row_count_verified_after_both_ideals=306,
                complete_post_ideal_row_stream_sha256=digest(ret['complete_source_rows']))
            assert after==exp
            expected_inner.append(core)
            expected_outer.append(exp)
    def by_actual_chart(records):
        return sorted(records,key=lambda r:(r['label'],r['infinity_chart']))
    assert by_actual_chart(INNER)==by_actual_chart(expected_inner)
    assert by_actual_chart(OUTER)==by_actual_chart(expected_outer)
    F=geometry['F_poles']
    assert F['function'] is six['F_y'] and F is geometry['complete_principal_divisor_cache'][id(six['F_y'])]
    frecords=[]
    for flag in (False,True):
        graph=F['records'][str(flag)]['kernel']
        div=graph['full_paired_numerator_division']
        assert div['method']=='same full attached-column Hermite reduction and exact back substitution'
        assert div['reduction'] is not None and div['reduction']['attached_block']
        assert div['every_source_row_returned_against_original_denominator'] and div['no_source_row_dropped_or_rescaled']
        assert not div['fractional_solution_or_denominator_clearing_used']
        frecords.append(dict(infinity_chart=flag,graph_sha256=digest(graph)))
    return dict(implementation=IMPLEMENTATION,actual_four_inner=deepcopy(INNER),
        actual_four_post_ideal_outer=deepcopy(OUTER),original_F_attached_Hermite_route=frecords)
