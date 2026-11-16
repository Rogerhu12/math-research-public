#!/usr/bin/env python3
"""Exact small integer-lattice audit of the original target extension class.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
Uses the already completed original root-two coordinate/action presentation.
No original equation solve or integer source reconstruction is repeated.
"""
import argparse,hashlib,json,time
from pathlib import Path
from math import comb
from flint import fmpz_mat
P=31; MOD=P**6
DATA_PIN=(16797,'46cb736d61e85daf6af0a4476ffa857c98b06f84d8c6e149b6180ce054d14a5c')
REC_PIN=(10067,'18085ddfc8be6d691c87588ed6ee03a5470f1996588cea0fc0d08f4ca97ce0bf')
BINDING='4d3f5dbf2bd02328ba5e7cea47641cd2c21cdc6467950eaee97c2b22d4864222'
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def identity(p):
 b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(c,m):
 if not c:raise ValueError(m)
def checked(p,pin):
 b=p.read_bytes();check((len(b),hashlib.sha256(b).hexdigest())==pin,'exact input '+str(p));return json.loads(b)
def multiply(a,b):
 check(len(a[0])==len(b),'matrix dimensions')
 return [[sum(x*y for x,y in zip(row,col))%MOD for col in zip(*b)] for row in a]
def join(*a):return [sum((z[i] for z in a),[]) for i in range(len(a[0]))]
def scale(a,c):return [[c*z%MOD for z in row] for row in a]
def reduce(a,e):return [[z%P**e[i] for z in row] for i,row in enumerate(a)]
def product(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def polynomial(p,x):
 n=len(x);a=[[0]*n for _ in range(n)]
 for c in reversed(p):
  a=multiply(a,x)
  for i in range(n):a[i][i]=(a[i][i]+c)%MOD
 return a
def vp_pure(n):
 check(n>0,'positive lattice index');v=0
 while n%P==0:n//=P;v+=1
 check(n==1,'lattice index is a pure p power');return v
def length(a,e):
 n=len(e);rows=[list(c) for c in zip(*a)]+[[P**z if i==j else 0 for i in range(n)] for j,z in enumerate(e)]
 H=fmpz_mat(rows).hnf();basis=[[int(H[i,j]) for j in range(n)] for i in range(H.nrows()) if any(H[i,j] for j in range(n))]
 check(len(basis)==n,'full integer HNF lattice rank')
 return sum(e)-vp_pure(abs(int(fmpz_mat(basis).det())))
def types(lengths):
 check(lengths[-1]==0,'complete finite p bound');b=[lengths[k]-lengths[k+1] for k in range(len(lengths)-1)]
 check(all(z>=0 for z in b) and all(b[k]>=b[k+1] for k in range(len(b)-1)),'valid full p filtration')
 es=[k+1 for k in range(len(b)) for _ in range(b[k]-(b[k+1] if k+1<len(b) else 0))]
 check(sum(es)==lengths[0],'all cyclic lengths recovered')
 return {'exponents':es,'length':lengths[0],'successivePImageLengths':lengths}
def group(a,e):return types([length(scale(a,P**k),e) for k in range(7)])
def quotient(a,h,e):
 L=length(h,e);return types([length(join(scale(a,P**k),h),e)-L for k in range(7)])
def matrix_record(a):return {'rows':len(a),'columns':len(a[0]),'sha256':hashlib.sha256(canonical(a)).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--completion-dir',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();start=time.monotonic()
 rp=a.completion_dir/'original-joint-m-root-two-p12-readonly-completion-receipt.json';dp=a.completion_dir/'root-two-complete-presentation-and-action.json'
 r=checked(rp,REC_PIN);d=checked(dp,DATA_PIN)
 check(r['status']=='completed' and r['binding']==d['binding']==BINDING,'exact complete original parent')
 A=d['coordinateRows'];e=d['ambientExponents'];X=d['xActionOnOriginal26Generators'];u=d['xOfPrimitiveFreeGeneratorTorsionColumn'];beta=d['betaModuloP6'];K=d['completeDRelationMatrix']
 check(len(A)==14 and all(len(z)==26 for z in A) and len(X)==26 and all(len(z)==26 for z in X),'entire original torsion and action frame')
 check(all(z==0 for row in reduce(multiply(A,K),e) for z in row),'complete actual D relations')
 AX=multiply(A,X)
 check(all(z==0 for row in reduce(multiply(AX,K),e) for z in row),'true action preserves every complete relation')
 hp=product([0,0,0,1],product(product([-8,32,-25,5],[-8,32,-25,5]),product(product([864,864,135,5],[864,864,135,5]),[9600,-25472,-3392,15936,-2888,-936,153,50,5])))
 check(len(hp)==24 and hp[-1]==3125,'same original hstar')
 ht=[sum(hp[d]*comb(d,k)*2**(d-k) for d in range(k,len(hp)))%MOD for k in range(len(hp))]
 check(sum(z*pow(beta,k,MOD) for k,z in enumerate(ht))%MOD==0,'actual Hensel root to full torsion precision')
 q=[0]*23
 for k in range(22,-1,-1):q[k]=(ht[k+1]+(beta*q[k+1] if k<22 else 0))%MOD
 check((ht[0]+beta*q[0])%MOD==0 and q[0]%P!=0,'true simple Hensel factor and unit cofactor')
 hx=polynomial(ht,X);qx=polynomial(q,X)
 DX=[[((z-beta) if i==j else z)%MOD for j,z in enumerate(row)] for i,row in enumerate(X)]
 check(multiply(DX,qx)==hx,'complete polynomial factor identity on all original generators')
 H=multiply(A,hx);Delta=multiply(A,DX);Q=multiply(A,qx)
 check(length(Q,e)==length(A,e),'cofactor is an automorphism of the complete finite torsion')
 check(length(H,e)==length(Delta,e)==length(join(H,Delta),e),'hstar S equals the actual (x-beta) S')
 b=multiply(A,multiply(qx,u));paid_b=[[row[0]] for row in d['originalNineHstarCoordinates']]
 check(reduce(b,e)==reduce(paid_b,e),'original b2 equals q(x)u in every true ambient coordinate')
 B=join(d['originalNineHstarCoordinates'],d['originalNineXHstarCoordinates'])
 Bext=join(H,b);check(length(B,e)==length(Bext,e)==length(join(B,Bext),e),'entire original B equals hstar S plus D b2')
 quotient_type=quotient(A,H,e);class_type=quotient(b,H,e);u_type=quotient(multiply(A,u),Delta,e)
 check(class_type==u_type,'both normalizations of the same extension class have equal full p type')
 check(len(class_type['exponents'])<=1,'one genuine extension class')
 nak=length(A,e)-length(join(scale(A,P),AX),e)
 nak_u=length(A,e)-length(join(scale(A,P),AX,multiply(A,u)),e)
 check(nak_u==nak-1,'primitive extension class removes exactly one Nakayama generator')
 result={'format':'r150-original-joint-m-extension-class-small-audit-v1','status':'completed','source':identity(Path(__file__)),'inputs':{'completeReceipt':identity(rp),'completeData':identity(dp)},'parentBinding':BINDING,'method':'exact-integer-HNF-lattice-index','S2':group(A,e),'hstarS2':group(H,e),'S2ModuloHstarS2':quotient_type,'originalT2ExtensionClass':class_type,'equivalentXBetaClass':u_type,'S2ModuloOriginalSingleB2':quotient(A,join(b,multiply(AX,multiply(qx,u))),e),'allOriginalBRecoveredFromHstarSAndB2':True,'sameHstarAndSimpleHenselFactorVerified':True,'allCompleteRelationsAndActionVerified':True,'extensionIsNonzero':class_type['length']>0,'extensionIsPrimitiveModuloPX':nak_u==nak-1,'rootTwoSMinimumPolynomialGenerators':nak,'rootTwoMMinimumPolynomialGenerators':1+nak_u,'hstarActionIdentity':matrix_record(hx),'extensionCoordinateIdentity':matrix_record(reduce(b,e)),'originalLargeSolveRepeated':False,'largeArraysTemporaryOnly':True,'elapsedSeconds':time.monotonic()-start}
 a.out.write_bytes(canonical(result));print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
