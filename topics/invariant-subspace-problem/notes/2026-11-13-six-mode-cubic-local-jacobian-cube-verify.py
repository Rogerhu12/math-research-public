"""Self-contained exact local certificate for the six-mode cubic Jacobian.
Uses only Fraction and the previously published exact third-moment data.
All matrix formulas are the full R3 formulas, without numerical tolerances.
"""
import json,itertools,time,sys,math
from fractions import Fraction as F
from pathlib import Path

CUTOFF=3
class P:
 def __init__(self,x=0):
  self.d=dict(x) if isinstance(x,dict) else ({(0,0):F(x)} if x else {})
 def __add__(self,b):
  if not isinstance(b,P):b=P(b)
  d=dict(self.d)
  for k,v in b.d.items():
   n=d.get(k,F(0))+v
   if n:d[k]=n
   elif k in d:del d[k]
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.d.items()})
 def __sub__(self,b):return self+-b if isinstance(b,P) else self+(-F(b))
 def __rsub__(self,b):return -self+b
 def __mul__(self,b):
  if not isinstance(b,P):return P({k:v*F(b) for k,v in self.d.items() if v*b})
  d={}
  for (i,j),a in self.d.items():
   for (k,l),c in b.d.items():
    if 2*(i+k)+j+l>CUTOFF:continue
    key=(i+k,j+l);n=d.get(key,F(0))+a*c
    if n:d[key]=n
    elif key in d:del d[key]
  return P(d)
 __rmul__=__mul__
 def __truediv__(self,b):return self*F(1,b)
 def __pow__(self,n):
  p=P(1)
  for _ in range(n):p=p*self
  return p

data=json.loads(Path(__file__).with_name('2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json').read_text())
K=[[int(x) for x in row] for row in data['K']]
Ji=[[F(int(x),int(data['detJ3'])) for x in row] for row in data['adjugateJ3']]
HM=[[[int(i+j==m) for j in range(6)] for i in range(6)] for m in range(11)]
def mv(A,b):return [sum((x*y for x,y in zip(a,b)),P()) for a in A]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),P())
def mm(A,B):return [[dot(a,col) for col in zip(*B)] for a in A]
def tr(A):return sum((A[i][i] for i in range(len(A))),P())
def anti(A):return [sum((A[i][j] for i in range(6) for j in range(6) if i+j==m),P()) for m in range(11)]
def conv(A,B):return [sum((A[i]*B[k-i] for i in range(max(0,k-len(B)+1),min(len(A),k+1))),P()) for k in range(len(A)+len(B)-1)]
QH=[anti(mm(mm(K,A),K)) for A in HM]
def formula(x,grad=True):
 y=x[:6];H=[[x[6+i+j] for j in range(6)] for i in range(6)]
 p=mv(K,y);F0=dot(y,p)/2;Hp=mv(H,p);KHp=mv(K,Hp);KH=mm(K,H);KH2=mm(KH,KH)
 b=dot(p,Hp);c=dot(Hp,KHp);t2=tr(KH2);t3=tr(mm(KH2,KH))
 q=anti(mm(KH,K));d=conv(conv(p,p),p);e=conv(q,p);ell=[a-6*b for a,b in zip(d,e)];ie=mv(Ji,ell)
 G=F0**3-6*F0*b+6*F0*t2+12*c-8*t3;R=G-dot(ell,ie)/2
 if not grad:return R,ell
 third=mv(K,mv(H,KHp))
 gy=[(3*F0*F0-6*b+6*t2)*p[i]-12*F0*KHp[i]+24*third[i] for i in range(6)]
 gh=[-6*F0*dot(p,mv(A,p))+12*F0*tr(mm(KH,mm(K,A)))+24*dot(p,mv(A,KHp))-24*tr(mm(KH2,mm(K,A))) for A in HM]
 ly=[]
 for j in range(6):
  a=conv(conv(p,p),[K[i][j] for i in range(6)]);bq=conv(q,[K[i][j] for i in range(6)])
  ly.append([3*aa-6*bb for aa,bb in zip(a,bq)])
 lh=[[-6*a for a in conv(QH[m],p)] for m in range(11)]
 g=[a-dot(bb,ie) for a,bb in zip(gy+gh,ly+lh)]
 return R,g,ell



def eliminate(A, rhs=None):
    A=[list(row) for row in A]
    if rhs is not None:
        for row,b in zip(A,rhs): row.append(F(b))
    n=len(A); sign=1; det=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None: return F(0),None
        if pivot!=k:
            A[pivot],A[k]=A[k],A[pivot];sign=-sign
        a=A[k][k];det*=a
        for j in range(k,len(A[k])): A[k][j]/=a
        for i in range(n):
            if i==k or not A[i][k]:continue
            c=A[i][k]
            for j in range(k,len(A[i])): A[i][j]-=c*A[k][j]
    return sign*det,([row[-1] for row in A] if rhs is not None else None)


def verify():
    global CUTOFF
    base=[F(1)]*6+[F(0)]*11
    CUTOFF=1
    Hess=[[F(0) for _ in range(17)] for _ in range(17)]
    for j in range(17):
        x=[P(a) for a in base];x[j]=x[j]+P({(0,1):F(1)})
        R,g,_=formula(x)
        assert R.d.get((0,0),0)==0
        for i in range(17):
            assert g[i].d.get((0,0),0)==0
            Hess[i][j]=g[i].d.get((0,1),F(0))
    assert Hess==[list(a) for a in zip(*Hess)]
    solved=[3,4,5,8,9,10,11,12,13,14,15,16]
    M=[[Hess[i][j] for j in solved] for i in solved]
    det,solution=eliminate(M,[-Hess[i][2] for i in solved])
    assert det and det.denominator%103
    det103=(det.numerator%103)*pow(det.denominator%103,-1,103)%103
    assert det103==70
    v=[F(0)]*17;v[2]=F(1)
    for j,a in zip(solved,solution):v[j]=a
    assert all(sum(Hess[i][j]*v[j] for j in range(17))==0 for i in range(17))
    den=1986132064
    expected=[0,0,1986132064,8968264800,29268304608,89336254496,0,0,-361544476,-1159751133,-2415939762,-4110758331,-6074808164,-7612556445,-6553855382,2420577073,28256379896]
    assert [a*den for a in v]==expected
    CUTOFF=3
    x=[P(a)+P({(0,1):b}) for a,b in zip(base,v)]
    R,_=formula(x,grad=False)
    assert all(R.d.get((0,j),0)==0 for j in range(3))
    cubic=R.d.get((0,3),0)
    expected_cubic=F(672625783316756245312265088,239097168542993716033883)
    assert cubic==expected_cubic!=0
    return dict(all_pass=True,base_y=[1]*6,base_H=[0]*11,
                solved_coordinates_zero_based=solved,
                exact_hessian_symmetry=True,exact_hessian_kernel_checks=17,
                morse_block_determinant=str(det),morse_block_det_mod103=det103,
                transverse_direction_denominator=den,
                transverse_direction_numerator=expected,
                transverse_cubic_coefficient=str(cubic),
                scope="Exact local matrix and cubic identities for R3. Together with the rational critical graph and the local algebra lemma, these prove every matched Br cubed belongs to the localized full Jacobian ideal at this point. No global membership or new operator cyclicity is claimed.")

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
