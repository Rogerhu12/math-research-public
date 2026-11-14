#!/usr/bin/env python3
"""R377: exact q-Frobenius Smith factors, with finite-ring AH verification.

Standard library only.  Recomputes p-adic candidate coordinates from formal
series, then verifies all 23 actual products in O_F43/(pi^90).
"""
import argparse, json, time, hashlib
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('notes_dir',type=Path)
parser.add_argument('--certificate',type=Path,required=True)
parser.add_argument('--write',action='store_true')
parser.add_argument('--progress',action='store_true')
args=parser.parse_args()
NOTES=args.notes_dir
def report(*values,**keywords):
    if args.progress:print(*values,**keywords)
p = 43
M = p**4
MOD = p**2
N = 130
LABELS = list(range(1,43))+[44,45]
st = time.monotonic()

class RS:
    def __init__(self):
        self.zero = [0]*N
        self.one = [1]+[0]*(N-1)
    def add(self,a,b): return [(x+y)%M for x,y in zip(a,b)]
    def sub(self,a,b): return [(x-y)%M for x,y in zip(a,b)]
    def scale(self,a,c): return [x*c%M for x in a]
    def shift(self,a,n): return [0]*n+a[:N-n]
    def mul(self,a,b):
        c=[0]*N
        ia=[(i,x) for i,x in enumerate(a) if x]
        ib=[(j,y) for j,y in enumerate(b) if y]
        for i,x in ia:
            for j,y in ib:
                if i+j>=N: break
                c[i+j]+=x*y
        return [x%M for x in c]
    def inv(self,a):
        c=[0]*N;c[0]=pow(a[0],-1,M)
        for n in range(1,N):
            c[n]=-c[0]*sum(a[j]*c[n-j] for j in range(1,n+1))%M
        return c
    def power(self,a,k):
        out=self.one
        while k:
            if k&1: out=self.mul(out,a)
            k//=2
            if k: a=self.mul(a,a)
        return out
    def evaluate(self,coeff,a):
        out=self.zero[:]
        for c in reversed(coeff):
            out=self.mul(out,a);out[0]=(out[0]+c)%M
        return out
    def plog(self,a):
        derivative=[k*a[k]%M for k in range(1,N)]+[0]
        logder=self.mul(derivative,self.inv(a));out=[0]*N
        for k in range(1,N):
            out[k]=(p*pow(k,-1,M) if k%p else pow(k//p,-1,M))*logder[k-1]%M
        return out

data=json.loads((NOTES/'r171_principal_norm_selflocal_certificate.json').read_text())
extra=json.loads((NOTES/'r185_p_local_kummer_certificate.json').read_text())
units=json.loads((NOTES/'r243_h_unit_norm_kernel_certificate.json').read_text())
P=list(reversed(data['P']));C=-P[0]//p
R=RS()
coeff=[(P[i]//p)*pow(C,-1,M)%M for i in range(44)]
def equation(u):
    powers=[R.one]
    for j in range(44): powers.append(R.mul(powers[-1],u))
    f=R.sub(powers[44],R.one);d=R.scale(powers[43],44)
    for j in range(1,44):
        if coeff[j]:
            f=R.add(f,R.scale(R.shift(powers[j],j),coeff[j]))
            d=R.add(d,R.scale(R.shift(powers[j-1],j),j*coeff[j]))
    return f,d
u=R.one
for _ in range(8):
    f,d=equation(u);u=R.sub(u,R.mul(f,R.inv(d)))
assert equation(u)[0]==R.zero
y=R.shift(u,1)
z=R.evaluate([int(a)*pow(2*int(b),-1,M)%M for a,b in extra['h_coefficients_ascending']],y)
report('canonical_parameter',round(time.monotonic()-st,2),flush=True)

def coordinates(g):
    assert g[0]%p
    ell=R.plog(g)
    assert all(ell[j]%p==0 for j in range(1,43))
    A1=(ell[1]//p+C*ell[45]+C*C*p*ell[89])%(p**3)
    pA43=(ell[43]+C*p*ell[87])%(p**3)
    assert (A1-pA43)%p==0
    out={1:pA43%MOD,45:((A1-pA43)//p)*pow(C,-1,MOD)%MOD}
    AA={j:(ell[j]//p+C*ell[j+44]+(C*C*p*ell[j+88] if j+88<N else 0))%MOD
        for j in range(2,43)}
    out.update(AA)
    out[42]=(AA[42]-C*out[2])%MOD
    out[41]=(AA[41]-C*C*p*out[3])%MOD
    w=(pow(g[0],42,p**3)-1)%(p**3)
    logc=(w-w*w*pow(2,-1,p**3))*pow(42,-1,p**3)%(p**3)
    A0=(logc+C*ell[44]+C*C*p*ell[88])%(p**3)
    assert A0%p==0
    out[44]=(A0//p)*pow(C,-1,MOD)%MOD
    return {'constant_mod_p4':g[0], 'p_log_coefficients_mod_p4':ell,
            'A0_mod_p3':A0,'A1_mod_p3':A1,'pA43_mod_p3':pA43,
            'AH_coordinates_mod_p2':[out[j] for j in LABELS]}

eps=[]
for row in units['ordinary_units']:
    el=row['element'];den=int(el['common_denominator']);assert den%p
    g=R.evaluate([int(a)*pow(den,-1,M)%M for a in el['numerators_ascending']],z)
    rec=coordinates(g);rec['index']=row['index'];eps.append(rec)
    assert rec['A0_mod_p3']==0,('global_norm_trace',row['index'])
    report('unit',row['index'],round(time.monotonic()-st,2),flush=True)
alpha=coordinates(R.add(R.one,R.scale(y,int(data['b']))))
q=int(data['q'])
w=(pow(-q,42,p**3)-1)%(p**3)
lognorm=(w-w*w*pow(2,-1,p**3))*pow(42,-1,p**3)%(p**3)
assert 44*alpha['A0_mod_p3']%(p**3)==lognorm

def gmul(a,b,mod=MOD):
    return ((a[0]*b[0]-a[1]*b[1])%mod,(a[0]*b[1]+a[1]*b[0])%mod)
omega=(352,197)
wp=[(1,0)]
for _ in range(44): wp.append(gmul(wp[-1],omega))
assert wp[44]==(1,0) and wp[22]==(MOD-1,0) and wp[11]==(0,1)

E=[]
for j in range(22): E.append([[a,0] for a in eps[j]['AH_coordinates_mod_p2']])
for j in range(22):
    if j!=8:
        E.append([gmul((a,0),wp[-r%44]) for r,a in zip(LABELS,eps[j]['AH_coordinates_mod_p2'])])
Frob=[]
for j in range(44):
    Frob.append([gmul((-a%MOD,0),wp[-r*j%44]) for r,a in zip(LABELS,alpha['AH_coordinates_mod_p2'])])
def matrix(cols):
    return [[col[k][c] for col in cols] for k in range(44) for c in (0,1)]

A=matrix(E+Frob)
original_A=[row[:] for row in A]
pivot_ops=[]
def eliminate_column(A,r,c,mod):
    k=next((k for k in range(r,len(A)) if A[k][c]%p),None)
    if k is None: return False
    A[r],A[k]=A[k],A[r]
    pivot=A[r][c];inv=pow(pivot,-1,mod)
    A[r]=[x*inv%mod for x in A[r]]
    for j in range(len(A)):
        if j!=r:
            t=A[j][c];A[j]=[(x-t*y)%mod for x,y in zip(A[j],A[r])]
    pivot_ops.append([r,c,k,pivot])
    return True
for j in range(43): assert eliminate_column(A,j,j,MOD)
Q=[row[43:] for row in A[43:]]
q_reduced=[row[:] for row in Q];pivot_ops=[];piv=[];r=0
for c in range(44):
    if eliminate_column(q_reduced,r,c,MOD): piv.append(c);r+=1
assert r==41
free=[c for c in range(44) if c not in piv]
rem=[[q_reduced[j][c] for c in free] for j in range(41,45)]
assert all(x%p==0 for row in rem for x in row)
div=[[x//p for x in row] for row in rem]
rankmat=[row[:] for row in div];r2=0;p2piv=[];pivot_ops=[]
for c in range(3):
    if eliminate_column(rankmat,r2,c,p): p2piv.append(c);r2+=1
report('q_rank_mod43',r,'remaining_p_divided_matrix',div,'rank',r2,flush=True)
out={'schema':'R377-q-frobenius-smith-factors-v1','p':p,'C':C,
     'series_modulus':M,'series_precision':N,'local_coordinate_modulus':MOD,
     'labels':LABELS,'canonical_u_mod_p4':u,'units':eps,'alpha':alpha,
     'omega_mod_p2':omega,'full_matrix_88_by_87':original_A,
     'q_quotient_matrix_45_by_44':Q,'q_reduced_matrix':q_reduced,
     'q_pivots_mod_p':piv,'remaining_columns':free,
     'remaining_matrix_div_p_mod_p':div,'remaining_rank':r2,
     'actual_norm_preimage_computed':False,'actual_L_computed':False}

# Independent multiplication check in the actual finite local ring.
P=43
RINGMOD=P**3
DEPTH=90
LABELS=list(range(1,43))+[44,45]

class Ring90:
    def __init__(self,C):
        self.C=C
        self.cp=C*P%RINGMOD
        self.zero=[(0,0)]*44
        self.one=[(1,0)]+[(0,0)]*43
        self.x=[(0,0),(1,0)]+[(0,0)]*42
    def normalize(self,a):
        return [(x%(RINGMOD if j<2 else P*P),y%(RINGMOD if j<2 else P*P))
                for j,(x,y) in enumerate(a)]
    def add(self,a,b):return self.normalize([(x+z,y+w) for (x,y),(z,w) in zip(a,b)])
    def sub(self,a,b):return self.normalize([(x-z,y-w) for (x,y),(z,w) in zip(a,b)])
    def scale(self,a,c):
        if isinstance(c,int):c=(c,0)
        u,v=c
        return self.normalize([(x*u-y*v,x*v+y*u) for x,y in a])
    def mul(self,a,b):
        out=[[0,0] for _ in range(87)]
        ia=[(j,x,y) for j,(x,y) in enumerate(a) if x or y]
        ib=[(j,x,y) for j,(x,y) in enumerate(b) if x or y]
        for j,x,y in ia:
            for k,u,v in ib:
                out[j+k][0]+=x*u-y*v
                out[j+k][1]+=x*v+y*u
        for j in range(43):
            out[j][0]+=self.cp*out[j+44][0]
            out[j][1]+=self.cp*out[j+44][1]
        return self.normalize(out[:44])
    def power(self,a,n):
        assert n>=0
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            n//=2
            if n:a=self.mul(a,a)
        return out
    def scalar(self,c):
        if isinstance(c,int):c=(c,0)
        return self.normalize([c]+self.zero[1:])
    def gaussian_inverse(self,c):
        x,y=c;t=pow(x*x+y*y,-1,RINGMOD)
        return (x*t%RINGMOD,-y*t%RINGMOD)
    def inv(self,a):
        v=self.scalar(self.gaussian_inverse(a[0]))
        for _ in range(7):v=self.mul(v,self.sub(self.scalar(2),self.mul(a,v)))
        assert self.mul(a,v)==self.one
        return v
    def evaluate(self,coeff,x):
        out=self.zero
        for c in reversed(coeff):out=self.add(self.mul(out,x),self.scalar(c))
        return out
    def pi_power(self,n,c=1):
        if n>=DEPTH:return self.zero
        if isinstance(c,int):c=(c,0)
        v=pow(self.cp,n//44,RINGMOD)
        out=self.zero[:];out[n%44]=(v*c[0],v*c[1])
        return self.normalize(out)
    def canonical_y(self,data):
        f=list(reversed(data['P']))
        assert len(f)==45 and f[-1]==1
        assert all(a%P==0 for a in f[:-1]) and f[0]%(P*P)
        assert -f[0]//P==self.C
        c=[(f[j]//P)*pow(self.C,-1,RINGMOD)%RINGMOD for j in range(44)]
        def equation(u):
            powers=[self.one]
            for _ in range(44):powers.append(self.mul(powers[-1],u))
            F=self.sub(powers[44],self.one);D=self.scale(powers[43],44)
            for j in range(1,44):
                if c[j]:
                    F=self.add(F,self.scale(self.mul(self.pi_power(j),powers[j]),c[j]))
                    D=self.add(D,self.scale(self.mul(self.pi_power(j),powers[j-1]),j*c[j]))
            return F,D
        u=self.one
        for _ in range(7):
            f,d=equation(u);u=self.sub(u,self.mul(f,self.inv(d)))
        assert equation(u)[0]==self.zero
        y=self.mul(self.x,u)
        assert self.evaluate(list(reversed(data['P'])),y)==self.zero
        return u,y

def check(notes,probe,progress=False):
    data=json.loads((notes/'r171_principal_norm_selflocal_certificate.json').read_text())
    extra=json.loads((notes/'r185_p_local_kummer_certificate.json').read_text())
    units=json.loads((notes/'r243_h_unit_norm_kernel_certificate.json').read_text())
    C=-data['P'][-1]//P
    R=Ring90(C);u,y=R.canonical_y(data)
    z=R.evaluate([int(a)*pow(2*int(b),-1,RINGMOD)%RINGMOD for a,b in extra['h_coefficients_ascending']],y)
    G=[]
    for row in units['ordinary_units']:
        el=row['element'];den=int(el['common_denominator'])
        G.append(R.evaluate([int(a)*pow(den,-1,RINGMOD)%RINGMOD for a in el['numerators_ascending']],z))
    G.append(R.add(R.one,R.scale(y,int(data['b']))))
    # Exact Artin--Hasse power series coefficients through degree89.
    e=[Fraction(1)]
    for n in range(1,DEPTH):
        e.append((e[n-1]+(e[n-P] if n>=P else 0))/n)
        assert e[n].denominator%P
    bases=[]
    for r in LABELS:
        v=R.one
        for n in range(1,(DEPTH-1)//r+1):
            c=e[n].numerator*pow(e[n].denominator,-1,RINGMOD)%RINGMOD
            v=R.add(v,R.pi_power(r*n,c))
        bases.append(v)
    gp=R.power(R.add(R.one,R.x),P*P)
    ip=R.power(R.add(R.one,R.scale(R.x,(0,1))),P*P)
    assert gp==R.add(R.add(R.one,R.pi_power(87,pow(C,-1,RINGMOD))),R.scale(R.x,P*P))
    assert ip==R.add(R.add(R.one,R.pi_power(87,(0,-pow(C,-1,RINGMOD)))),R.scale(R.x,(0,P*P)))
    rows=[]
    records=probe['units']+[probe['alpha']]
    for j,(g,rec) in enumerate(zip(G,records)):
        # H elements have rational residue.  Teichmuller lift is c^(p²) mod p³.
        assert g[0][1]==0
        c=g[0][0]%P;teich=pow(c,P*P,RINGMOD)
        actual=R.scale(g,pow(teich,-1,RINGMOD))
        product=R.one
        for b,a in zip(bases,rec['AH_coordinates_mod_p2']):
            product=R.mul(product,R.power(b,a))
        quotient=R.mul(actual,R.inv(product))
        assert quotient[43][0]%P==0 and quotient[43][1]%P==0
        a=quotient[43][0]//P%P
        b=-quotient[43][1]//P%P
        reduced=R.mul(quotient,R.inv(R.mul(R.power(gp,a),R.power(ip,b))))
        assert reduced==R.one,('finite_p2_power',j,quotient,reduced)
        rows.append({'index':j if j<22 else 'alpha','power_correction_mod43':[a,b],
                     'finite_ratio_mod_pi90':quotient})
        if progress:print('PASS exact finite AH product',j,flush=True)
    return {'pi_precision':DEPTH,'canonical_u_mod_pi90':u,
            'canonical_y_mod_pi90':y,'ordinary_z_mod_pi90':z,
            'p2_power_of_1_plus_pi':gp,'p2_power_of_1_plus_i_pi':ip,
            'all23_finite_AH_product_checks':rows}


assert r2==2
assert div==[[23,7,27],[0,0,0],[0,0,0],[1,5,4]]
assert (div[0][0]*div[3][1]-div[0][1]*div[3][0])%p==22
quadratic=[1 if j%2==0 else MOD-1 for j in range(44)]
quadratic_image=[sum(x*y for x,y in zip(row,quadratic))%MOD for row in Q]
assert quadratic_image==[0]*45
weights16=[[wp[(16*j)%44][c] for j in range(44)] for c in (0,1)]
images16=[[sum(x*y for x,y in zip(row,w))%MOD for w in weights16] for row in Q]
assert all(a%p==0 for row in images16 for a in row)
div16=[[a//p for a in row] for row in images16]
tmp=[row[:] for row in div16];rr=0;pivot_ops=[]
for c in range(2):
    if eliminate_column(tmp,rr,c,p):rr+=1
assert rr==2
out['quadratic_alternating_image_mod_p2']=quadratic_image
out['Teichmuller_lifts_of_two_16_character_relations']=weights16
out['two_16_character_images_div_p_mod_p']=div16
out['remaining_rank2_minor_rows']=[0,3]
out['remaining_rank2_minor_columns']=[0,1]
out['remaining_rank2_minor_determinant_mod43']=22
out['finite_ring_verification']=check(NOTES,out,args.progress)
out['input_sha256']={name:hashlib.sha256((NOTES/name).read_bytes()).hexdigest()
  for name in ['r171_principal_norm_selflocal_certificate.json',
               'r185_p_local_kummer_certificate.json',
               'r243_h_unit_norm_kernel_certificate.json']}
out['q_Frobenius_integral_rank']=43
out['q_Frobenius_nonzero_Smith_valuations']=[0]*41+[1,1]
out['q_split_tower_abelianization_free_rank']=2
out['q_split_tower_abelianization_torsion_invariant_factors']=[43,43]
out['torsion_Delta_character_exponents']=[16,28]
out['free_Delta_character_exponents']=[0,22]
out['q_split_tower_minimal_relation_number_bounds']=[2,3]
out['exact_rank_upper_bound_uses_proved_quadratic_relation']=True
out['used_GRH']=False
out['nonabelian_q_Frobenius_computed']=False
out=json.loads(json.dumps(out))
if args.write:
    args.certificate.write_text(json.dumps(out,indent=2)+'\n')
else:
    assert out==json.loads(args.certificate.read_text())
print('PASS R377: all23 finite AH checks; Smith valuations 0^41,1,1; exact abelianization Z43^2+(Z/43)^2.',flush=True)
print('PASS actual Norm/L remain uncomputed.',flush=True)
