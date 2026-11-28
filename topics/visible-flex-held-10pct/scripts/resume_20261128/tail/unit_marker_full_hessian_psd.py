#!/usr/bin/env python3
"""Exact all-angle Hessian bound for the complete rational threefold marker.

For phi(z)=(1-|z|^2)^3 Re[z^3/(1-z^3/2)] on the unit disk, prove
K I + D^2 phi and K I - D^2 phi positive definite by their exact principal
minors. The two variables are r in [0,1] and c=cos(3 theta) in [-1,1].
Four integer tensor-Bernstein certificates cover this entire rectangle.
There is no Fourier truncation, sampled positivity test, new numerical
surface or change to any previously frozen marker/metric.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb, lcm
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]


def clean(p):
    return {key:Q(value) for key,value in p.items() if value}


def add(*items):
    out = {}
    for p in items:
        for key,value in p.items():
            out[key] = out.get(key,Q(0))+value
    return clean(out)


def scale(p,a):
    return clean({key:Q(a)*value for key,value in p.items()})


def multiply(p,q):
    out = {}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            key = i+k,j+l
            out[key] = out.get(key,Q(0))+a*b
    return clean(out)


def power(p,n):
    out = {(0,0):Q(1)}
    for _ in range(n):
        out = multiply(out,p)
    return out


def derivative(p,axis):
    out = {}
    for key,value in p.items():
        if key[axis]:
            target = list(key)
            target[axis] -= 1
            out[tuple(target)] = value*key[axis]
    return clean(out)


def divide_r_squared(p):
    if any(i<2 for i,j in p):
        raise ArithmeticError('An apparent polar singularity did not cancel exactly')
    return {(i-2,j):value for (i,j),value in p.items()}


def at_radius(p,r):
    out = {}
    for (i,j),value in p.items():
        out[j] = out.get(j,Q(0))+value*Q(r)**i
    return {j:value for j,value in out.items() if value}


def serial_poly(p):
    return [[i,j,str(value)] for (i,j),value in sorted(p.items())]


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                     allow_nan=False).encode()).hexdigest()


def hessian_numerators():
    one, r, c = {(0,0):Q(1)}, {(1,0):Q(1)}, {(0,1):Q(1)}
    r3 = power(r,3)
    D = add(scale(one,4),scale(multiply(r3,c),-4),power(r,6))
    P = scale(multiply(multiply(r3,power(add(one,scale(power(r,2),-1)),3)),
                       add(scale(c,2),scale(r3,-1))),2)
    Dr,Dc = derivative(D,0),derivative(D,1)
    U = add(multiply(derivative(P,0),D),scale(multiply(P,Dr),-1))
    V = add(multiply(derivative(P,1),D),scale(multiply(P,Dc),-1))
    # phi_r=U/D^2, phi_c=V/D^2. All operations are exact rational
    # polynomial operations; no symbolic simplifier or derivative sampler.
    A = add(multiply(derivative(U,0),D),scale(multiply(U,Dr),-2))
    W = add(multiply(derivative(V,1),D),scale(multiply(V,Dc),-2))
    Y = add(multiply(derivative(V,0),D),scale(multiply(V,Dr),-2))
    C = divide_r_squared(add(multiply(multiply(r,U),D),
        scale(multiply(add(one,scale(power(c,2),-1)),W),9),
        scale(multiply(multiply(c,V),D),-9)))
    T = scale(divide_r_squared(add(multiply(r,Y),scale(multiply(V,D),-1))),-3)
    if any(at_radius(p,0) for p in (A,C,T)):
        raise ArithmeticError('The Cartesian Hessian at the origin is not the exact zero jet')
    if any(at_radius(p,1) for p in (P,U,V,A,C,T)):
        raise ArithmeticError('The full disk boundary does not have exact zero two-jets')
    return D,P,A,C,T


def principal_minor_polynomials(K):
    D,P,A,C,T = hessian_numerators()
    one, c = {(0,0):Q(1)}, {(0,1):Q(1)}
    D3 = power(D,3)
    KD3 = scale(D3,K)
    square_offdiag = multiply(add(one,scale(power(c,2),-1)),power(T,2))
    polynomials = {}
    for sign,label in ((1,'plus'),(-1,'minus')):
        a = add(KD3,scale(A,sign))
        b = add(KD3,scale(C,sign))
        polynomials['radial_minor_'+label] = a
        polynomials['determinant_'+label] = add(multiply(a,b),scale(square_offdiag,-1))
    definition = dict(marker='(1-|z|^2)^3 Re(z^3/(1-z^3/2))',
        polar_function='2 r^3 (1-r^2)^3 (2 c-r^3)/(4-4 r^3 c+r^6)',
        polar_variables='r=|z|, c=cos(3 theta)',
        positive_D='4-4 r^3 c+r^6 >= (2-r^3)^2 >= 1',
        orthonormal_polar_Hessian='D^(-3) [[A,sin(3 theta) T],[sin(3 theta) T,C]]',
        original_Hessian_entries=dict(A='phi_rr',C='phi_r/r+phi_thetatheta/r^2',
                                      offdiag='phi_rtheta/r-phi_theta/r^2'),
        numerator_polynomial_sha256={key:digest(serial_poly(value)) for key,value in
            (('D',D),('P',P),('A',A),('C',C),('T',T))},
        numerator_degrees={key:[max(i for i,j in value),max(j for i,j in value)]
                           for key,value in (('A',A),('C',C),('T',T))},
        exact_polar_removable_singularities_checked=True,
        exact_origin_Hessian_zero=True, exact_boundary_zero_two_jet=True,
        source_function_is_smooth_rational_in_x_y_inside_disk=True)
    return polynomials,definition


def bernstein_on_initial_rectangle(p):
    """Return integer numerators / common positive denominator.

    First substitute c=2u-1, then convert the entire bidegree polynomial to
    tensor Bernstein form on (r,u) in [0,1]^2. No coefficient is rounded.
    """
    transformed = {}
    for (i,j),a in p.items():
        for k in range(j+1):
            key = i,k
            transformed[key] = transformed.get(key,Q(0))+a*comb(j,k)*2**k*(-1)**(j-k)
    transformed = clean(transformed)
    n = max(i for i,j in transformed)
    m = max(j for i,j in transformed)
    coefficient_denominator = lcm(*(a.denominator for a in transformed.values()))
    rn = [comb(n,k) for k in range(n+1)]
    cm = [comb(m,k) for k in range(m+1)]
    Lr,Lc = lcm(*rn),lcm(*cm)
    denominator = coefficient_denominator*Lr*Lc
    values = [[0]*(m+1) for _ in range(n+1)]
    for (k,l),a in transformed.items():
        integer = a.numerator*(coefficient_denominator//a.denominator)
        for i in range(k,n+1):
            v = integer*comb(i,k)*(Lr//rn[k])
            for j in range(l,m+1):
                values[i][j] += v*comb(j,l)*(Lc//cm[l])
    if denominator<=0:
        raise ArithmeticError('Invalid exact Bernstein scale')
    return values,denominator


def split_rows(values,denominator):
    """Exact midpoint de Casteljau, with one integer scale for each child."""
    n,m = len(values)-1,len(values[0])-1
    left,right = [[0]*(m+1) for _ in range(n+1)],[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for k in range(i+1):
            weight = comb(i,k) << (n-i)
            for j in range(m+1):
                left[i][j] += weight*values[k][j]
        for k in range(i,n+1):
            weight = comb(n-i,k-i) << i
            for j in range(m+1):
                right[i][j] += weight*values[k][j]
    return (left,denominator << n),(right,denominator << n)


def split(box,axis):
    values,denominator = box
    if axis == 0:
        return split_rows(values,denominator)
    transpose = list(map(list,zip(*values)))
    children = split_rows(transpose,denominator)
    return tuple((list(map(list,zip(*matrix))),d) for matrix,d in children)


def check_complete_tree(paths):
    """Independently collapse the exact full binary leaf partition to root."""
    stack = []
    for path in paths:
        if stack and path<=stack[-1]:
            raise ArithmeticError('The exact binary partition is duplicated or unordered')
        stack.append(path)
        while len(stack)>=2 and stack[-2].endswith('0') and stack[-1]==stack[-2][:-1]+'1':
            parent = stack[-2][:-1]
            stack[-2:] = [parent]
    if stack != ['']:
        raise ArithmeticError('The positive rectangles do not cover the entire domain once')


def prove(K,max_depth,outdir):
    started = time.monotonic()
    polynomials,definition = principal_minor_polynomials(K)
    initial = {name:bernstein_on_initial_rectangle(p) for name,p in polynomials.items()}
    paths,leaves = [],[]
    minima = {name:None for name in polynomials}
    counters = dict(attempted_boxes=0,positive_boxes=0,subdivisions=0,maximum_depth=0)
    total_area = Q(0)
    output = outdir/'positive-rectangles.jsonl'
    with output.open('w') as stream:
        def visit(boxes,rlo,rhi,clo,chi,path):
            nonlocal total_area
            counters['attempted_boxes'] += 1
            minimum = {name:min(map(min,matrix)) for name,(matrix,den) in boxes.items()}
            if min(minimum.values())>0:
                counters['positive_boxes'] += 1
                counters['maximum_depth'] = max(counters['maximum_depth'],len(path))
                paths.append(path)
                total_area += (rhi-rlo)*(chi-clo)
                entry = dict(path=path,r_exact=list(map(str,(rlo,rhi))),
                    cos3theta_exact=list(map(str,(clo,chi))),depth=len(path),proofs={})
                for name,(matrix,den) in boxes.items():
                    lower = Q(minimum[name],den)
                    minima[name] = lower if minima[name] is None else min(minima[name],lower)
                    entry['proofs'][name] = dict(minimum_coefficient_exact=str(lower),
                        complete_integer_coefficient_matrix_sha256=digest(dict(values=matrix,denominator=den)))
                stream.write(json.dumps(entry,sort_keys=True,separators=(',',':'))+'\n')
                stream.flush()
                leaves.append(dict(path=path,exact_area=(rhi-rlo)*(chi-clo)))
                return
            if len(path)>=max_depth:
                raise ArithmeticError('A full-box positivity proof did not finish; no Hessian bound is claimed')
            counters['subdivisions'] += 1
            # The prescribed alternating split makes every dyadic rectangle
            # independently reconstructible from its binary path.
            axis = len(path)%2
            children = {name:split(value,axis) for name,value in boxes.items()}
            left = {name:pair[0] for name,pair in children.items()}
            right = {name:pair[1] for name,pair in children.items()}
            if axis==0:
                mid = (rlo+rhi)/2
                visit(left,rlo,mid,clo,chi,path+'0')
                visit(right,mid,rhi,clo,chi,path+'1')
            else:
                mid = (clo+chi)/2
                visit(left,rlo,rhi,clo,mid,path+'0')
                visit(right,rlo,rhi,mid,chi,path+'1')
        visit(initial,Q(0),Q(1),Q(-1),Q(1),'')
    check_complete_tree(paths)
    if total_area != 2 or counters['subdivisions'] != len(paths)-1:
        raise ArithmeticError('The exact full angular/radius coverage check failed')
    proofs = [dict(polynomial=name,
        bidegree=[len(initial[name][0])-1,len(initial[name][0][0])-1],
        original_power_polynomial_sha256=digest(serial_poly(p)),
        minimum_Bernstein_coefficient_exact=str(minima[name]),
        all_coefficients_strictly_positive=True) for name,p in polynomials.items()]
    return dict(status='complete_unit_marker_Cartesian_Hessian_operator_bound_certified',
        unit_Hessian_operator_upper_exact=str(K),full_two_variable_domain={'radius':['0','1'],'cos3theta':['-1','1']},
        all_angles_and_all_harmonics_included=True,finite_sampling_used_as_a_proof=False,
        exact_integer_Bernstein_arithmetic=True,complete_exact_single_cover=True,
        independently_collapsed_full_binary_partition=True,exact_rectangle_area_sum=str(total_area),
        matrix_test='Both K I + D^2 phi and K I - D^2 phi: positive first principal minor and positive determinant.',
        Hessian_itself_claimed_positive_semidefinite=False,
        definition=definition,polynomial_proofs=proofs,**counters,
        full_leaf_record={'path':str(output.resolve()),'sha256':hashlib.sha256(output.read_bytes()).hexdigest()},
        physical_scaling='||D^2 [epsilon phi((x+iy)/radius)]||op <= K epsilon/radius^2',
        any_existing_surface_or_frozen_metric_changed=False,
        new_physical_marker_parameters_selected=False,old_low_lambda_geometry_recomputed=False,
        seconds=time.monotonic()-started)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bound',type=Q,default=Q(23,10))
    parser.add_argument('--max-depth',type=int,default=20)
    parser.add_argument('--outdir',type=Path,required=True)
    args = parser.parse_args()
    if args.bound<=0 or not 0<=args.max_depth<=30:
        raise ValueError('Use a positive exact bound and a finite declared proof depth')
    out = args.outdir.resolve()
    if out==REPO or REPO in out.parents:
        raise ValueError('Keep all regenerable proof leaves outside Git')
    out.mkdir(parents=True,exist_ok=False)
    source = dict(path=str(Path(__file__).resolve()),sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    try:
        result = prove(args.bound,args.max_depth,out)
    except BaseException as exc:
        (out/'summary.json').write_text(json.dumps(dict(status='not_certified',source=source,
            requested_bound_exact=str(args.bound),error=dict(type=type(exc).__name__,text=str(exc)),
            no_Hessian_or_surface_bound_claimed=True),indent=2)+'\n')
        raise
    result.update(source=source,requested_bound_exact=str(args.bound),max_depth=args.max_depth)
    (out/'summary.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:result[key] for key in ('status','unit_Hessian_operator_upper_exact',
        'positive_boxes','attempted_boxes','maximum_depth','seconds')}),flush=True)


if __name__ == '__main__':
    main()
