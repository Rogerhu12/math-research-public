"""Exact fourth-order strengthening at the published positive Gaussian point.

The twelve eliminated ORIGINAL gradients are solved through order four.
All three graph-parameter derivatives are computed as the exact linear
combinations of the eleven original H-gradients.  Their fourth-order terms
are retained; one fills the final degree-four transverse quotient.
"""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import json

path=Path(__file__).with_name('2026-11-13-six-mode-cubic-gaussian-plane-local-verify.py')
spec=importlib.util.spec_from_file_location('gaussian_local_exact',path)
gaussian=importlib.util.module_from_spec(spec)
spec.loader.exec_module(gaussian)
alg=gaussian.alg


def quartic(values):
    c0,c4,plus,minus,c12=values
    c2=(plus+minus)/2-c0-c4
    mix=(plus-minus)/2
    c3=(c12-c0-16*c4-4*c2-2*mix)/6
    return [c0,mix-c3,c2,c3,c4]


def verify():
    head=[1,0,0]
    hh=gaussian.tail(head)
    base=[Q(0)]*6+hh
    parameter_vectors=[gaussian.tail([int(i==j) for i in range(3)]) for j in range(3)]
    alg.CUTOFF=1
    Hess=[[Q(0)]*17 for _ in range(17)]
    for j in range(17):
        x=[alg.P(z) for z in base]
        x[j]=x[j]+alg.P({(0,1):Q(1)})
        _,g,_=alg.formula(x)
        assert all(not z.d.get((0,0),0) for z in g)
        for i in range(17):
            Hess[i][j]=g[i].d.get((0,1),Q(0))
    solved=[0,1,2,3,9,10,11,12,13,14,15,16]
    M=[[Hess[i][j] for j in solved] for i in solved]
    determinant,_=alg.eliminate(M)
    assert gaussian.mod(determinant)==81
    directions=[(1,0),(0,1),(1,1),(1,-1),(1,2)]
    values=[]
    parameter_values=[[],[],[]]
    for u,v in directions:
        alg.CUTOFF=4
        x=[alg.P(z) for z in base]
        x[4]=alg.P({(0,1):Q(u)})
        x[5]=alg.P({(0,1):Q(v)})
        for order in [1,2,3,4]:
            _,g,_=alg.formula(x)
            d,correction=alg.eliminate(M,[-g[i].d.get((0,order),Q(0)) for i in solved])
            assert d==determinant
            for i,c in zip(solved,correction):
                x[i]=x[i]+alg.P({(0,order):c})
        R,g,_=alg.formula(x)
        # These are all twelve original eliminated gradients, to every order 0..4.
        assert all(not g[i].d.get((0,order),0) for i in solved for order in range(5))
        assert all(not g[i].d.get((0,order),0) for i in range(17) for order in range(3))
        assert all(not g[i].d.get((0,3),0) for i in [6,7,8])
        assert all(not g[i].d.get((0,4),0) for i in [4,5])
        assert all(not R.d.get((0,order),0) for order in range(4))
        values.append(R.d.get((0,4),Q(0)))
        for j,h in enumerate(parameter_vectors):
            original=sum((h[n]*g[6+n] for n in range(11)),alg.P(0))
            assert all(not original.d.get((0,order),0) for order in range(4))
            # Since the other eight H-gradients have actually been eliminated,
            # this is also the remaining original H_j gradient on this jet.
            assert original.d.get((0,4),Q(0))==g[6+j].d.get((0,4),Q(0))
            parameter_values[j].append(original.d.get((0,4),Q(0)))
    F4=quartic(values)
    E=[quartic(row) for row in parameter_values]
    assert E[0]==F4
    f=F4
    Fu=[4*f[0],3*f[1],2*f[2],f[3]]
    Fv=[f[1],2*f[2],3*f[3],4*f[4]]
    four=[Fu+[Q(0)],[Q(0)]+Fu,Fv+[Q(0)],[Q(0)]+Fv]
    matrix=four+[E[1]]
    matrix_mod=[[gaussian.mod(z) for z in row] for row in matrix]
    expected=[[45,23,65,49,0],[0,45,23,65,49],
              [42,65,44,31,0],[0,42,65,44,31],[20,93,43,14,91]]
    assert matrix_mod==expected
    assert gaussian.solve_mod(matrix_mod)[0]==1
    _,left=alg.eliminate([row[:4] for row in four],[-row[4] for row in four])
    left.append(Q(1))
    assert [gaussian.mod(z) for z in left]==[89,11,22,71,1]
    socle=[sum(z*w for z,w in zip(row,left)) for row in E]
    assert [gaussian.mod(z) for z in socle]==[0,96,44]
    return dict(all_pass=True,base_y=[0]*6,base_H=list(map(str,hh)),
                eliminated_variables_zero_based=solved,
                morse_block_determinant=str(determinant),morse_block_det_mod103=81,
                directions=directions,
                twelve_original_gradients_vanish_through_degree4=True,
                three_parameter_gradients_vanish_through_degree3=True,
                transverse_quartic_coefficients=list(map(str,F4)),
                parameter_quartic_coefficients=[list(map(str,row)) for row in E],
                transverse_quartic_mod103=[gaussian.mod(z) for z in F4],
                parameter_quartics_mod103=[[gaussian.mod(z) for z in row] for row in E],
                five_by_five_quartic_matrix_mod103=matrix_mod,
                five_by_five_determinant_mod103=1,
                degree_four_left_functional_mod103=[89,11,22,71,1],
                parameter_socles_mod103=[0,96,44],
                scope="Exact fourth-order local certificate using all seventeen original gradients. Together with the published local-algebra reduction it proves Br^4 membership for every r at p_plus, and the original three directions have minimal local exponent exactly four. No global membership or cyclicity is claimed.")


if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
