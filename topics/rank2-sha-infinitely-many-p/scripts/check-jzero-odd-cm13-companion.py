#!/usr/bin/env python3
"""R307: exact original CM13 on the six-dimensional odd companion space.

Rebuilds the true degree-13 fibers, including the full sigma and y gauges.
The seven fixed fibers are an exact finite-dimensional determination, not a
search over target primes. All arithmetic is in Q(sqrt(-3)).
"""
import sympy as s, json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
x=s.symbols('x');d=s.sqrt(-3);w=(-1+d)/2
K=s.QQ.algebraic_field(d)
P=lambda q:s.Poly(q,x,domain=K)
g=4+w;gb=4+s.conjugate(w)
q=P(g*(x**6+(2+6*d)*x**3+(40+24*d)/13))
qb=P(gb*(x**6+(2-6*d)*x**3+(40-24*d)/13))
B=P(x**3+1)
num=P(13*x)*q**2-4*B*(q.diff().diff()*q-q.diff()**2)-P(6*x*x)*q.diff()*q
den=(q**2).mul_ground(g*g)
numb=P(13*x)*qb**2-4*B*(qb.diff().diff()*qb-qb.diff()**2)-P(6*x*x)*qb.diff()*qb
denb=(qb**2).mul_ground(gb*gb)
c=s.polys.polytools.gcd(num,den);num=num.exquo(c);den=den.exquo(c)
c=s.polys.polytools.gcd(numb,denb);numb=numb.exquo(c);denb=denb.exquo(c)
checks=[]
def check(name, condition):
    assert condition, name
    checks.append(name)
check('true CM13 x-map degrees', (num.degree(),den.degree())==(13,12))
def pw(a,n,f):
    out=P(1)
    while n:
        if n&1: out=(out*a).rem(f)
        a=(a*a).rem(f);n>>=1
    return out
dn=num.diff()*den-num*den.diff()
dnb=numb.diff()*denb-numb*denb.diff()
fibers=[]
for a in range(2,9):
 f=(num-den.mul_ground(a)).monic()
 check(f'degree13 separable fiber x={a}', f.degree()==13 and s.polys.polytools.gcd(f,f.diff()).degree()==0)
 ratio=(qb*s.invert(q,f)).rem(f)
 xb=(numb*s.invert(denb,f)).rem(f)
 yratio=(dnb*pw(den,2,f)*s.invert((pw(denb,2,f)*dn).rem(f),f)).rem(f).mul_ground(s.simplify(g/gb))
 check(f'complete y-ratio on fiber x={a}', (yratio**2-(P(1)+pw(xb,3,f)).mul_ground(s.Rational(1,a**3+1))).rem(f).is_zero)
 step=pw(xb,3,f)
 val=(pw(ratio,34,f)*yratio).rem(f)
 row=[]
 for j in range(6):
  row.append((val*f.diff()).rem(f).nth(12))
  val=(val*step).rem(f)
 fibers.append(row)
 print('fiber',a,'done',flush=True)
E=s.Matrix([[s.Integer(a)**(3*j) for j in range(6)] for a in range(2,8)])
M=(E.inv()*s.Matrix(fibers[:6])).applyfunc(s.expand)
check('held-out complete fiber x=8 all six columns', all(s.simplify(sum(s.Integer(8)**(3*k)*M[k,j] for k in range(6))-fibers[6][j])==0 for j in range(6)))
DM=DomainMatrix.from_Matrix(M).convert_to(K)
char=DM.charpoly()
char_expr=sum(K.to_sympy(c)*s.Symbol('t')**(6-j) for j,c in enumerate(char))
output={'status':'PASS','basis':'sigma^34*y*x^(3j), j=0..5, b=1','CM13_matrix':[[str(M[i,j]) for j in range(6)] for i in range(6)],'characteristic_polynomial':str(s.factor(char_expr,extension=d)),'full_y_ratio':'(gamma/gammabar)*(xbarprime/xgammaprime)','fit_fibers':list(range(2,8)),'held_fiber':8}
for label,index in [('T_pm',0),('origin_derivative',5)]:
 row=s.zeros(1,6);row[0,index]=1;rows=[]
 for j in range(6):
  rows.append(row);row=(row*M).applyfunc(s.expand)
 O=DomainMatrix.from_Matrix(s.Matrix.vstack(*rows)).convert_to(K)
 _,piv=O.rref();null=O.nullspace().to_Matrix().applyfunc(s.simplify)
 check(label+' full observation rank',len(piv)==6)
 output[label+'_observability_rank']=len(piv)
 output[label+'_observation_determinant']=str(s.factor(K.to_sympy(O.det()),extension=d))
 output[label+'_kernel']=[[str(null[i,j]) for j in range(null.cols)]for i in range(null.rows)]
check('characteristic polynomial t6-gamma3*t3+gamma6',s.expand(char_expr-(s.Symbol('t')**6-g**3*s.Symbol('t')**3+g**6))==0)
check('primitive eighteenth-root polynomial after scaling',s.expand(char_expr.subs(s.Symbol('t'),g*s.Symbol('u'))/g**6-(s.Symbol('u')**6-s.Symbol('u')**3+1)).simplify()==0)
for k in (1,3,5):
    check(f'no original source eigenvalue k={k}',s.simplify(char_expr.subs(s.Symbol('t'),-g*w**(k-1))-3*g**6)==0)
# Full meromorphic connection and its exact five-dimensional holomorphic domain.
X,b=s.symbols('X b',nonzero=True)
coeff=s.symbols('r0:6')
R=sum(coeff[j]*X**j for j in range(6))
Podd=R.subs(X,x**3)
# C=sigma^34*y*Podd, F=sigma^34*x^17.  The zeta terms cancel.
actual=s.cancel(3*x*x*Podd+2*(x**3+b)*s.diff(Podd,x)-34*(x**3+b)*Podd/x)
expected=(6*X*(X+b)*s.diff(R,X)-(31*X+34*b)*R).subs(X,x**3)/x
check('full odd theta connection identity',s.cancel(actual-expected)==0)
R5=sum(coeff[j+1]*X**j for j in range(5))
full=(6*X*(X+b)*s.diff(X*R5,X)-(31*X+34*b)*X*R5)
L=6*X*(X+b)*s.diff(R5,X)-(25*X+28*b)*R5
check('natural j>=1 domain maps by original L',s.expand(full-X*L)==0)
check('only j=0 contributes real Tpm pole',s.expand((6*X*(X+b)*s.diff(R,X)-(31*X+34*b)*R).subs(X,0)+34*b*coeff[0])==0)
output.update({'origin_derivative_row':'-coefficient of X^5',
 'Tpm_value_row':'sigma(Tpm)^34*y(Tpm)*coefficient of X^0',
 'connection_full':'sigma^34/x * (6X(X+b)Pprime-(31X+34b)P)',
 'holomorphic_connection_domain':'P divisible by X; C=sigma^34*y*x^3*R(X), deg R<=4',
 'connection_holomorphic':'sigma^34*x^2 * (6X(X+b)Rprime-(25X+28b)R)',
 'characteristic_polynomial_compact':'t^6-gamma^3*t^3+gamma^6',
 'spectrum':'gamma times all primitive eighteenth roots of unity',
 'checks':checks,'check_count':len(checks)})
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(checks),'charpoly':output['characteristic_polynomial_compact'],'Tpm_rank':output['T_pm_observability_rank'],'origin_rank':output['origin_derivative_observability_rank']},indent=2),flush=True)
