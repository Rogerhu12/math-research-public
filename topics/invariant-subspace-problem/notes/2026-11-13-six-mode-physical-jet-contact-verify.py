"""Exact contact orders of the original three physical polar jets.

These integer calculations supplement the symbolic identity
q(s,s)=-s^2(s+6)(s-2); all zero statements below are exact over Z.
"""
from pathlib import Path
import json
import math


def verify():
    data=json.loads(Path(__file__).with_name('2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json').read_text())
    K=[[int(x) for x in row] for row in data['K']]
    C=[[0,0,-5,1],[0,22,-3,1],[-5,-3,-3,0],[1,1,0,0]]
    diagonal=[sum(C[i][j] for i in range(4) for j in range(4) if i+j==n) for n in range(7)]
    assert diagonal==[0,0,12,-4,-1,0,0]
    expected={0:([4,3,2],[5,-32,108]),2:([3,2,1],[16,-16,-32]),-6:([3,2,1],[-144,144,288])}
    records=[]
    for s,(orders,leading) in expected.items():
        polars=[]
        for d in range(3):
            jet=[math.factorial(i)//math.factorial(i-d)*s**(i-d) if i>=d else 0 for i in range(6)]
            coefficients=[sum(K[i][j]*jet[j] for j in range(6)) for i in range(6)]
            shifted=[sum(coefficients[i]*math.comb(i,n)*s**(i-n) for i in range(n,6)) for n in range(6)]
            order=next(i for i,x in enumerate(shifted) if x)
            assert order==orders[d] and shifted[order]==leading[d]
            polars.append(shifted)
        records.append(dict(point=s,orders=orders,leading_coefficients=leading,exact_local_polar_coefficients=polars))
    polars=[]
    for d in range(3):
        jet=[0]*6;jet[5-d]=math.factorial(d)
        coefficients=[sum(K[i][j]*jet[j] for j in range(6)) for i in range(6)][::-1]
        polars.append(coefficients)
    assert polars==[[0,0,0,0,-1,-1],[0,0,0,5,5,5],[0,0,-16,-8,-64,0]]
    records.append(dict(point='infinity',orders=[4,3,2],leading_coefficients=[-1,5,-16],exact_local_polar_coefficients=polars))
    return dict(all_pass=True,exact_q_diagonal_coefficients=diagonal,
                generic_finite_point_orders=[2,1,0],
                generic_leading_coefficients=['-q(s,s)','2q(s,s)','-2q(s,s)'],
                exceptional_points=records,
                scope='Exact original-kernel contact data. The accompanying valuation argument excludes all nonreduced length-three common jet supports with a nonsecant mean; no numerical or finite-field zero test is used.')


if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
