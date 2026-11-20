"""Exact bicubic facts used for three distinct physical support points.

All polynomial identities and the pure-cube obstruction resultant are over Z.
The degree-eight discriminant factor is certified squarefree by a nonzero
resultant modulo 103.  No finite-field zero is lifted to characteristic zero.
"""
# Corrected 2026-11-20 by Astra-ISP-b2a9acde-20261120 / root; AI-assisted GPT-6 Astra Pro.
# The pure-cube condition is B^3 - 27*A^2*D, with the corresponding exact resultant.
from pathlib import Path
import json


def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
    return a


def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)


def scale(a,c):return trim([c*x for x in a])


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)


def power(a,n):
    c=[1]
    for _ in range(n):c=mul(c,a)
    return c


def evaluate(a,t):
    c=0
    for x in reversed(a):c=c*t+x
    return c


def bareiss(M):
    A=[list(row) for row in M];last=1;sign=1
    for k in range(len(A)-1):
        row=next((i for i in range(k,len(A)) if A[i][k]),None)
        if row is None:return 0
        if row!=k:A[row],A[k]=A[k],A[row];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,len(A)):
            for j in range(k+1,len(A)):
                numerator=pivot*A[i][j]-A[i][k]*A[k][j]
                assert numerator%last==0
                A[i][j]=numerator//last
            A[i][k]=0
        last=pivot
    return sign*A[-1][-1]


def detmod(M,p=103):
    A=[[x%p for x in row] for row in M];out=1
    for k in range(len(A)):
        row=next((i for i in range(k,len(A)) if A[i][k]),None)
        if row is None:return 0
        if row!=k:A[row],A[k]=A[k],A[row];out=-out
        pivot=A[k][k];out=out*pivot%p;inverse=pow(pivot,-1,p)
        for i in range(k+1,len(A)):
            c=A[i][k]*inverse%p
            for j in range(k,len(A)):A[i][j]=(A[i][j]-c*A[k][j])%p
    return out%p


def sylvester(f,g):
    f=list(reversed(trim(f)));g=list(reversed(trim(g)))
    m=len(f)-1;n=len(g)-1
    return [[0]*i+f+[0]*(n-i-1) for i in range(n)]+[[0]*i+g+[0]*(m-i-1) for i in range(m)]


def verify():
    C=[[0,0,-5,1],[0,22,-3,1],[-5,-3,-3,0],[1,1,0,0]]
    assert bareiss(C)==70
    Kdata=json.loads(Path(__file__).with_name('2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json').read_text())
    K=[[int(x) for x in row] for row in Kdata['K']]
    square={(2,0):1,(1,1):-2,(0,2):1}
    calculated=[[0]*6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            for (a,b),coefficient in square.items():calculated[i+a][j+b]-=C[i][j]*coefficient
    assert calculated==K
    # q(z,t)=A(t) z^3+B(t) z^2+C1(t) z+D(t).
    A=[1,1];B=[-5,-3,-3];C1=[0,22,-3,1];D=[0,0,-5,1]
    discriminant=add(add(mul(power(B,2),power(C1,2)),scale(mul(A,power(C1,3)),-4)),
                     add(add(scale(mul(power(B,3),D),-4),scale(mul(power(A,2),power(D,2)),-27)),
                         scale(mul(mul(A,B),mul(C1,D)),18)))
    E=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
    assert discriminant==[0,0]+E
    derivative=[i*E[i] for i in range(1,len(E))]
    squarefree=detmod(sylvester(E,derivative));assert squarefree==18
    assert evaluate(E,0)==9600 and evaluate(E,-1)==13900
    P=add(power(B,2),scale(mul(A,C1),-3))
    Q=add(power(B,3),scale(mul(power(A,2),D),-27))
    assert P==[25,-36,-18,24,6]
    assert Q==[-125,-225,-225,-54,-135,-108,-27]
    resultant=bareiss(sylvester(P,Q))
    assert resultant==260758295153015625
    assert resultant%103==56
    assert evaluate(A,-1)==0 and evaluate(B,-1)==-5
    # q(z,infinity)=z+1 as a binary cubic: it has one simple and one double root.
    infinity_fiber=[C[i][3] for i in range(4)]
    assert infinity_fiber==[1,1,0,0]
    return dict(all_pass=True,exact_kernel_factorization=True,
                bicubic_coefficient_matrix=C,bicubic_matrix_determinant=70,
                exact_discriminant_factorization='disc_z q(z,t)=t^2 E(t)',
                E_coefficients_ascending=E,E_derivative_resultant_mod103=squarefree,
                E_at_zero=9600,E_at_minus_one=13900,
                pure_cube_test_P_coefficients_ascending=P,
                pure_cube_test_Q_coefficients_ascending=Q,
                pure_cube_test_resultant=resultant,
                infinity_binary_cubic_coefficients_ascending=infinity_fiber,
                scope='The accompanying elementary argument proves that the only singular points of the original (3,3) bicubic are the diagonal points (0,0) and (infinity,infinity), and no physical polar binary cubic is a nonzero pure cube. Together with det C=70 these facts support the complete three-distinct-point critical-support classification.')


if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
