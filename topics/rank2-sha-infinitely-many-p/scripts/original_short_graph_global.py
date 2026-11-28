#!/usr/bin/env sage-python
"""One full short fibre recovers both bounded projective integral graphs."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import numpy as np
from sage.all import matrix,vector
from original_adaptive_dixon_solver import OneRightHandSide,_join
from original_ys_divisor_ideal_tools import element_digest,polynomial_digest,polynomial_matrix_digest
from original_short_graph_field import PackedField
from original_short_graph_kernel import independent_leading_rows,left_kernel,prime_rows,prime_rref
from original_short_graph_outer import original_operator_product


def chart_operators(engine,N,D):
    numerator,denominator=engine.element(N),engine.element(D)
    if numerator.is_zero() or denominator.is_zero():
        raise ValueError("The original nonzero endpoint numerator and denominator are required")
    MN,MD=engine.multiplication_matrix(numerator),engine.multiplication_matrix(denominator)
    if engine.unit*MN!=numerator or engine.unit*MD!=denominator:
        raise ArithmeticError("The actual unit failed to recover the original numerator or denominator")
    return numerator,denominator,MN,MD


def ring_residue(row,q):
    return vector(q.parent(),[value%q for value in row])


def solve_short_fibre(engine,N,MN,MD,required_degree):
    R=engine.R
    solver=OneRightHandSide(MD,progress=engine.progress)
    m=(required_degree+solver.e-1)//solver.e
    q=solver.pi**m
    if not m or q.degree()<required_degree:
        raise ArithmeticError("The actual full good-place power is too short")
    stream=solver.digits(N)
    raw=[next(stream) for _ in range(m)]
    w=vector(R,[_join([solver._unflatten_coordinate(values,i) for values in raw],solver.pi)
                for i in range(solver.n)])
    if any(pol and pol.degree()>=q.degree() for pol in w):
        raise ArithmeticError("The actual short-fibre representative is not reduced")
    if not ring_residue(original_operator_product(w,MD)-N,q).is_zero():
        raise ArithmeticError("The complete original single RHS failed after short precision")
    MW=engine.multiplication_matrix(w)
    if engine.unit*MW!=w:
        raise ArithmeticError("The original multiplication table changed the full short-fibre element")
    residue=[]
    for i,row in enumerate(MW.rows()):
        z=ring_residue(row,q)
        if not ring_residue(original_operator_product(z,MD)-MN.row(i),q).is_zero():
            raise ArithmeticError("An original short-fibre multiplication column equation failed")
        residue.append(z)
    multiplication=matrix(R,residue)
    record=dict(original_good_irreducible_sha256=polynomial_digest(solver.pi),
                original_good_place_degree=solver.e,actual_prime_PLU_width=solver.width,
                actual_nonunit_centers_skipped=list(solver.rejected),
                requested_full_fibre_degree=required_degree,actual_pi_digits=m,
                complete_fibre_modulus_degree=int(q.degree()),
                actual_fibre_modulus_sha256=polynomial_digest(q),
                complete_short_representative_sha256=element_digest(w),
                whole_short_multiplication_matrix_sha256=polynomial_matrix_digest(multiplication),
                all_original_operator_rows_returned=solver.n)
    return multiplication,solver.pi,q,record


def _domain_positions(weights,window):
    return [(i,a) for i,d in enumerate(weights) for a in range(max(0,window-d+1))]


def multiplication_windows(field,multiplication,q,weights,window):
    n,L=len(weights),int(q.degree())
    if L<=window:
        raise ValueError("A unique bounded output requires a modulus longer than the maximum polynomial degree")
    domain=_domain_positions(weights,window)
    low=[i*L+a for i,a in domain]
    high=[i*L+a for i,d in enumerate(weights) for a in range(max(0,window-d+1),L)]
    if len(low)+len(high)!=n*L or len(set(low+high))!=n*L:
        raise ArithmeticError("The low and high windows do not exhaust every original coordinate")
    full=np.empty((field.f,len(domain),n*L),dtype=np.uint8)
    modulus=[field.coords(q[a]) for a in range(L)]
    if q.leading_coefficient()!=1:
        raise ArithmeticError("The complete original fibre modulus must be monic")
    row_at=0
    for i,row in enumerate(multiplication.rows()):
        if window<weights[i]:
            continue
        current=np.zeros((field.f,n,L),dtype=np.uint8)
        for j,pol in enumerate(row):
            if pol and pol.degree()>=L:
                raise ArithmeticError("An unreduced original multiplier reached the fibre windows")
            for a,c in enumerate(pol.list()):
                current[:,j,a]=field.coords(c)
        for h in range(window-weights[i]+1):
            if domain[row_at]!=(i,h):
                raise ArithmeticError("The true source monomial order changed")
            full[:,row_at,:]=current.reshape(field.f,n*L)
            row_at+=1
            if h==window-weights[i]:
                break
            # t times the current element modulo the WHOLE monic q, including carries.
            following=np.zeros_like(current)
            following[:,:,1:]=current[:,:,:-1]
            top=current[:,:,-1]
            for a,c in enumerate(modulus):
                if any(c):
                    following[:,:,a]=(following[:,:,a].astype(np.int64)-
                                      field.scalar_times(c,top))%field.p
            current=following
    if row_at!=len(domain):
        raise ArithmeticError("The short-fibre matrix did not include every bounded source")
    return np.take(full,low,axis=2),np.take(full,high,axis=2),domain


def unpack_low_pair(field,R,packed,domain,n):
    polys=[[] for _ in range(2*n)]
    for half in range(2):
        for position,(j,a) in enumerate(domain):
            if len(polys[half*n+j])!=a:
                raise ArithmeticError("The bounded polynomial powers are not consecutive")
            polys[half*n+j].append(field.decode(packed[:,half*len(domain)+position]))
    return vector(R,[R(c) for c in polys[:n]]),vector(R,[R(c) for c in polys[n:]])


def weighted_row(row,weights):
    return max((int(pol.degree())+d for pol,d in zip(row,weights) if pol),default=-1)


def reciprocal_row(row,weight,weights,ring):
    out=[]
    for j,pol in enumerate(row):
        cap=weight-weights[j]
        if not pol:
            out.append(ring.zero())
            continue
        if cap<pol.degree():
            raise ArithmeticError("A true chart-pair row exceeded its original weight")
        coeff=[ring.base_ring().zero()]*(cap+1)
        for a,c in enumerate(pol.list()):
            coeff[cap-a]=c
        out.append(ring(coeff))
    return vector(ring,out)


def actual_residue_rank(Y,pi,field):
    R=Y.base_ring()
    n,e=int(Y.nrows()),int(pi.degree())
    data=np.zeros((field.f,n*e,n*e),dtype=np.uint8)
    for i,row in enumerate(Y.rows()):
        for j,pol in enumerate(row):
            v=pol%pi
            for h in range(e):
                for a,c in enumerate(v.list()):
                    data[:,i*e+h,j*e+a]=field.coords(c)
                if h+1<e:
                    v=(v*R.gen())%pi
    whole,piv=prime_rref(field.p,prime_rows(field,data))
    if piv!=tuple(range(field.f*n*e)):
        raise ArithmeticError("The actual pole projection is singular at a proved unit-denominator fibre")
    return dict(actual_good_place_projection_prime_rank=len(piv),original_module_rank=n,
                residue_degree=e,constant_field_degree=field.f)


def two_chart_low_graph(finite,infinite,finite_pair,infinite_pair,common_weight,
                        projective_degree,genus,window):
    """The genus/pole data must come from the caller's actual model or an exact toy fixture."""
    if finite.infinity_chart is not False or infinite.infinity_chart is not True:
        raise ValueError("Both labelled original affine and reciprocal chart engines are required")
    n=int(finite.dimension)
    weights=tuple(int(d) for d in finite.chart["original_basis_weights"])
    if (not n or n!=int(infinite.dimension) or len(weights)!=n or min(weights)<0
            or tuple(infinite.chart["original_basis_weights"])!=weights or
            finite.R.base_ring() is not infinite.R.base_ring()):
        raise ValueError("The reciprocal chart changed original weights, rank, or coefficient field")
    if genus!=1+sum(weights)-n or window<max(weights) or n*(window-1)-projective_degree<=2*genus-2:
        raise ValueError("The claimed saturated RR window is not justified by the actual parameters")
    field=PackedField(finite.R.base_ring())
    N,D,MN,MD=chart_operators(finite,*finite_pair)
    Ni,Di,MNi,MDi=chart_operators(infinite,*infinite_pair)
    if (reciprocal_row(N,common_weight,weights,infinite.R)!=Ni or
            reciprocal_row(D,common_weight,weights,infinite.R)!=Di):
        raise ArithmeticError("The two inputs are not the genuinely same weighted numerator and denominator")
    required_degree=(n*window+projective_degree)//n+1
    multiplication,pi,q,sol=solve_short_fibre(finite,N,MN,MD,required_degree)
    if n*int(q.degree())<=n*window+projective_degree:
        raise ArithmeticError("The complete thick fibre is not longer than the divisor of a nonzero residual")
    low,high,domain=multiplication_windows(field,multiplication,q,weights,window)
    K,ker=left_kernel(field,high)
    del high
    target=n*window-projective_degree+1-genus
    if K.shape[1]!=target or len(domain)!=n*(window+1)-sum(weights):
        raise ArithmeticError("The whole original bounded graph differs from its actual RR dimension")
    if ker["original_rank"]!=len(domain)-target:
        raise ArithmeticError("The original true high-coefficient rank does not match rank-nullity")
    whole=np.empty((field.f,target,2*len(domain)),dtype=np.uint8)
    whole[:,:,:len(domain)]=K
    for lo_idx in range(0,target,32):
        hi_idx=min(target,lo_idx+32)
        whole[:,lo_idx:hi_idx,len(domain):]=field.product(K[:,lo_idx:hi_idx,:],low)
    del K,low
    info=[(j+half*n,a,a+weights[j]) for half in range(2) for j,a in domain]
    selections,leading=independent_leading_rows(field,whole,info,n,window)
    del whole
    Y,X,Yi,Xi=[],[],[],[]
    rho=[]
    for actual_weight,coord,packed in selections:
        h,x=unpack_low_pair(field,finite.R,packed,domain,n)
        if max(weighted_row(h,weights),weighted_row(x,weights))!=actual_weight:
            raise ArithmeticError("The graded monomial and the returned actual polynomial weights differ")
        if original_operator_product(h,MN)!=original_operator_product(x,MD):
            raise ArithmeticError("An actual bounded finite pair failed the original unreduced polynomial equation")
        hi=reciprocal_row(h,actual_weight,weights,infinite.R)
        xi=reciprocal_row(x,actual_weight,weights,infinite.R)
        if (reciprocal_row(hi,actual_weight,weights,finite.R)!=h or
                reciprocal_row(xi,actual_weight,weights,finite.R)!=x):
            raise ArithmeticError("The full weighted reciprocal graph row failed to return")
        if original_operator_product(hi,MNi)!=original_operator_product(xi,MDi):
            raise ArithmeticError("A reciprocal pair failed the complete original polynomial equation")
        Y.append(h)
        X.append(x)
        Yi.append(hi)
        Xi.append(xi)
        rho.append(actual_weight)
    if len(rho)!=n or sum(rho)!=sum(weights)+projective_degree or sum(window-d+1 for d in rho)!=target:
        raise ArithmeticError("The exact low-pair weights do not exhaust the entire RR graph")
    Y,X=matrix(finite.R,Y),matrix(finite.R,X)
    Yi,Xi=matrix(infinite.R,Yi),matrix(infinite.R,Xi)
    rank_cert=actual_residue_rank(Y,pi,field)
    # This is the actual entire paired rank at s=0, even if separate Y_i drops rank there.
    constants=np.empty((field.f,n,2*n),dtype=np.uint8)
    for i in range(n):
        for half,block in enumerate((Yi,Xi)):
            for j in range(n):
                constants[:,i,half*n+j]=field.coords(block[i,j][0])
    cmat,cpiv=prime_rref(field.p,prime_rows(field,constants))
    if len(cpiv)!=field.f*n:
        raise ArithmeticError("The actual complete reciprocal graph is not saturated at s=0")
    infinity_weights=[max(weighted_row(Yi.row(i),weights),weighted_row(Xi.row(i),weights))
                      for i in range(n)]
    if infinity_weights!=rho:
        raise ArithmeticError("The actual reciprocal row weights changed the complete original RR window")
    records=dict(original_constant_degree=field.f,original_rank=n,actual_weights=list(weights),
                 original_finite_N=element_digest(N),original_finite_D=element_digest(D),
                 original_infinity_N=element_digest(Ni),original_infinity_D=element_digest(Di),
                 original_operator_sha256=[polynomial_matrix_digest(A) for A in (MN,MD,MNi,MDi)],
                 actual_common_input_weight=int(common_weight),proved_projective_pole_degree=projective_degree,
                 actual_full_thick_fibre=sol,actual_high_kernel=ker,actual_column_echelon=leading,
                 actual_RR_window=window,actual_full_RR_dimension=target,
                 actual_low_graph_row_weight_sum=sum(rho),actual_finite_source_rank=rank_cert,
                 reciprocal_whole_constant_prime_rank=len(cpiv),source_projection_rank_by_reversal=n,
                 original_finite_Y=polynomial_matrix_digest(Y),original_finite_X=polynomial_matrix_digest(X),
                 original_reciprocal_Y=polynomial_matrix_digest(Yi),original_reciprocal_X=polynomial_matrix_digest(Xi),
                 all_ordinal_original_polynomial_pairs_rechecked_in_both_charts=True)
    return {False:(Y,X),True:(Yi,Xi)},records


def fixed_original_low_graph(six,index,engines):
    if index not in (0,1) or six["kind"]!="rank2_original_Y_fraction_consumer_context" or int(six["prime"])!=29:
        raise ValueError("Only the two actual direct r29 y0 labels from the original six maps are covered")
    function=six["A"][index]["y0"]
    model=six["model"]
    if function.model is not model or model.k is not engines[False].k or model.k is not engines[True].k:
        raise ValueError("The selected physical fraction changed its original model or field")
    if engines[False].R is not model.P or engines[True].R is not model.S:
        raise ValueError("A different original chart polynomial ring was supplied")
    weights=tuple(model.weights)
    if (len(weights)!=306 or [weights.count(j) for j in range(5)]!=[1,0,65,226,14]
            or tuple(engines[False].chart["original_basis_weights"])!=weights):
        raise ValueError("The actual full original r29 integral basis is required")
    finite_pair=function.chart_pair(False)
    infinity_pair=function.chart_pair(True)
    blocks,record=two_chart_low_graph(engines[False],engines[True],finite_pair,infinity_pair,
                                      int(function.pole_weight_bound),2256,559,13)
    for flag,original in ((False,finite_pair),(True,infinity_pair)):
        current=function.chart_pair(flag)
        if current[0] is not original[0] or current[1] is not original[1]:
            raise ArithmeticError("The actual bound original endpoint chart object changed")
    record.update(actual_original_endpoint=index,actual_original_function_id=id(function),
                  actual_finite_engine_id=id(engines[False]),actual_infinity_engine_id=id(engines[True]))
    return blocks,record
