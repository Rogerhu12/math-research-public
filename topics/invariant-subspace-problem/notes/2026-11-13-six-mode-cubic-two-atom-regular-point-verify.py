"""Exact full-Hessian certificate at a noncolliding two-atom critical point."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import json

path=Path(__file__).with_name('2026-11-13-six-mode-cubic-local-jacobian-cube-verify.py')
spec=importlib.util.spec_from_file_location('cubic_local_exact',path)
algebra=importlib.util.module_from_spec(spec)
spec.loader.exec_module(algebra)


def verify():
    algebra.CUTOFF=1
    base=[Q(3)]+[Q(2)]*5+[Q(5,2)]+[Q(2)]*10
    Hess=[[Q(0) for _ in range(17)] for _ in range(17)]
    for j in range(17):
        x=[algebra.P(a) for a in base]
        x[j]=x[j]+algebra.P({(0,1):Q(1)})
        R,g,_=algebra.formula(x)
        assert R.d.get((0,0),0)==0
        for i in range(17):
            assert g[i].d.get((0,0),0)==0
            Hess[i][j]=g[i].d.get((0,1),Q(0))
    assert Hess==[list(a) for a in zip(*Hess)]
    normal=[i for i in range(17) if i not in [0,1,6,7]]
    M=[[Hess[i][j] for j in normal] for i in normal]
    det,_=algebra.eliminate(M)
    assert det and det.denominator%103
    residue=(det.numerator%103)*pow(det.denominator%103,-1,103)%103
    assert residue==91
    return dict(all_pass=True,atoms=dict(a=1,b=2,s=0,t=1),
                base_y=[3,2,2,2,2,2],base_H=['5/2']+['2']*10,
                full_critical_value_and_gradient_zero=True,
                full_hessian_symmetric=True,
                normal_coordinates_zero_based=normal,
                normal_hessian_determinant=str(det),determinant_mod103=residue,
                scope="Exact finite nondegeneracy certificate; the complete rational critical graph then identifies the localized full gradient ideal with that graph ideal. No global Jacobian or operator-inverse conclusion is asserted.")


if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
