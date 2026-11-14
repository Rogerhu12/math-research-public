#!/usr/bin/env python3
"""Exact algebra certificates for the high-frequency/Klein existence proof.

Only rational polynomial identities, Fourier averages, and finite group algebra
are evaluated.  No geometry is sampled, no optimizer or research ODE is run,
and this certificate does not supply an embedded curve or a reach estimate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


VARIABLES = ('a', 'v', 't', 'z', 'w', 'D', 'J')
DIM = len(VARIABLES)
ZERO_EXPONENT = (0,)*DIM


class Poly:
    def __init__(self, terms=None):
        self.terms = {k:F(v) for k,v in (terms or {}).items() if v}

    @staticmethod
    def scalar(value):
        return Poly({ZERO_EXPONENT:F(value)})

    @staticmethod
    def variable(index):
        key = [0]*DIM
        key[index] = 1
        return Poly({tuple(key):F(1)})

    @staticmethod
    def convert(value):
        return value if isinstance(value, Poly) else Poly.scalar(value)

    def __add__(self, other):
        answer = dict(self.terms)
        for key,value in self.convert(other).terms.items():
            answer[key] = answer.get(key,F(0))+value
        return Poly(answer)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key:-value for key,value in self.terms.items()})

    def __sub__(self, other):
        return self+-self.convert(other)

    def __rsub__(self, other):
        return self.convert(other)+-self

    def __mul__(self, other):
        answer = {}
        for a,x in self.terms.items():
            for b,y in self.convert(other).terms.items():
                key = tuple(i+j for i,j in zip(a,b))
                answer[key] = answer.get(key,F(0))+x*y
        return Poly(answer)

    __rmul__ = __mul__

    def __truediv__(self, value):
        return self*F(1,value)

    def __pow__(self, power):
        result = self.scalar(1)
        for _ in range(power):
            result = result*self
        return result


def determinant(matrix):
    a,b,c = matrix
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def multiply_laurent(p, q):
    answer = {}
    for i,a in p.items():
        for j,b in q.items():
            answer[i+j] = answer.get(i+j,F(0))+a*b
    return {key:value for key,value in answer.items() if value}


def exact_certificate():
    a,v,t,z,w,D,J = [Poly.variable(j) for j in range(DIM)]
    m1 = a
    m2 = a*a+v
    m3 = a**3+3*a*v+t
    m4 = a**4+6*a*a*v+4*a*t+z
    m5 = a**5+10*a**3*v+10*a*a*t+5*a*z+w
    E = a*D+J
    matrix = [
        [-m3/8-m1/2, -m2/16-F(1,4), m5/32+3*m3/16+m1/4-E/8],
        [m2/2, m1/4, -m4/8-m2/4+D/4],
        [-m1/2, Poly.scalar(F(-1,4)), m1/4+m3/8]]
    det = determinant(matrix)
    numerator = (-2*D*t+4*J*v+3*a*t*t-3*a*z*v+3*a*v**3
                 +t*z+t*v*v-v*w)
    assert not (det-numerator/256).terms
    assert not sum(matrix[j][j] for j in range(3)).terms
    Bmatrix = [
        [-m5/128-3*m3/64-m1/16+E/32,
         m4/32+m2/16-D/16, -m3/32-m1/16],
        [-m2/32-F(1,8), m1/8, Poly.scalar(F(-1,8))],
        [m3/32+m1/8, -m2/8, m1/8]]
    assert not (det+32*determinant(Bmatrix)).terms

    # f=cos(theta)+(1/2)cos(2theta).  D_z f=(1/i)d_theta f.
    f = {-2:F(1,4),-1:F(1,2),1:F(1,2),2:F(1,4)}
    f2 = multiply_laurent(f,f)
    f3 = multiply_laurent(f2,f)
    df_without_i = {j:j*c for j,c in f.items()}
    df2 = {j:-c for j,c in multiply_laurent(df_without_i,df_without_i).items()}
    fdf2 = multiply_laurent(f,df2)
    averages = dict(f2=f2.get(0,F(0)),f3=f3.get(0,F(0)),
                    df2=df2.get(0,F(0)),f_df2=fdf2.get(0,F(0)))
    assert averages == dict(f2=F(5,8),f3=F(3,8),df2=F(1),f_df2=F(3,8))
    determinant_leading_over_D_epsilon3 = (
        -2*averages['f3']+4*averages['f_df2']*averages['f2']/averages['df2'])/256
    assert determinant_leading_over_D_epsilon3 == F(3,4096)

    aa,ee,dd = F(20),F(1,3),F(20740,27)
    yy = ee+aa/2
    K = (aa*ee-1)*(ee+aa)
    Kp = 2*aa*ee+aa*aa-1
    C = (K*(ee*ee+1)-dd*ee/2)/8
    Cp = (Kp*(ee*ee+1)+2*ee*K-dd/2)/8
    W = (K*ee-dd/4)/4
    ratio = W/Cp
    assert C == 0 and Cp == F(679,36) and W == F(-1037,27)
    assert ratio == F(-4148,2037) and F(-9,4) < ratio < F(-5,4)
    A0,Ap,App = -aa*(ee*ee+1)/2, -aa*ee, -aa
    B0 = Kp*(ee*ee+1)/8
    Bp = (2*aa*(ee*ee+1)+2*ee*Kp)/8
    Bpp = aa*ee+Kp/4
    Wp = (Kp*ee+K)/4
    jet1 = -A0/(2*B0)
    jet2 = (Ap+(A0+2*Bp)*jet1)/(2*W)
    jetK = App+(2*Ap+2*Bpp)*jet1+(A0+2*Bp-2*Wp)*jet2
    assert jet2 == 0 and jetK == 0  # The limit itself must not be miscertified.

    identity = (1,1,1)
    g1,g2,g3 = (1,-1,-1),(-1,1,-1),(-1,-1,1)
    group = [identity,g1,g2,g3]
    assert tuple(sum(g[j] for g in group) for j in range(3)) == (0,0,0)
    word = [g1,g2,g1,g2,g2,g1,g2,g1]
    current = identity
    edges = []
    for generator in word:
        edges.append((current,generator))
        current = tuple(x*y for x,y in zip(current,generator))
    assert current == identity
    assert len(set(edges)) == 8
    assert set(edges) == {(g,h) for g in group for h in [g1,g2]}
    S0 = [[F(0),F(0),F(-1)],[F(0),F(-1),F(0)],[F(-1),F(0),F(0)]]
    assert determinant(S0) == 1
    assert [S0[j][0] for j in range(3)] == [0,0,-1]

    return dict(
        certificate='constant-h-moments-and-Klein-closure-exact-v1',
        arithmetic='Python Fraction sparse multivariate polynomials and Laurent polynomials',
        central_moment_variables=list(VARIABLES),
        matrix_trace_exact_zero=True,
        determinant_central_moment_formula_exact=True,
        determinant_formula_nonzero_monomials=len(det.terms),
        det_M_equals_minus_32_det_B_exact=True,
        trigonometric_averages={key:str(val) for key,val in averages.items()},
        det_leading_over_D_epsilon_cubed=str(determinant_leading_over_D_epsilon3),
        limit=dict(a=str(aa),e=str(ee),D=str(dd),xi=str(yy),C=str(C),
                   C_prime=str(Cp),W=str(W),ratio=str(ratio),
                   ratio_strictly_inside_R26_interval=True,
                   limit_itself_has_zero_Kjet=True,
                   limit_first_jet=str(jet1),limit_second_jet=str(jet2)),
        klein_group_sum_exact_zero=True,klein_euler_word_all_8_edges_exact=True,
        half_turn_sends_first_axis_to_negative_third_exact=True,
        geometry_evaluated=False,optimizer_called=False,research_ODE_run=False,
        finite_n_selected=False,finite_N_selected=False,
        smooth_connection_existence_is_proved_in_note_not_by_this_certificate=True,
        embedding_proved=False,reach_lower_certified=False,task_complete=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    result=exact_certificate()
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output=json.dumps(result,indent=2,allow_nan=False)+'\n'
    if args.out is not None:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(output)
    print(output,end='')


if __name__=='__main__':
    main()
