#!/usr/bin/env python3
"""Independent relative-lattice audit of the original target extension.
Author: ChatGPT (AI), root. Date: 2026-11-16.
Uses exact integer lattice bases and their relative Smith matrices; does not
reuse the producer's modular Smith or its successive-image length routine.
All mathematical arrays remain in the supplied temporary computation.
"""
import argparse, hashlib, json, time
from fractions import Fraction
from pathlib import Path
from flint import fmpz_mat, fmpq_mat

P=31
MOD=P**6
PIN=(16797,'46cb736d61e85daf6af0a4476ffa857c98b06f84d8c6e149b6180ce054d14a5c')
BINDING='4d3f5dbf2bd02328ba5e7cea47641cd2c21cdc6467950eaee97c2b22d4864222'
def require(c,m):
 if not c: raise ValueError(m)
def identity(p):
 b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def canonical(d):return (json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode()
def mul(a,b):
 return [[sum(x*y for x,y in zip(row,col))%MOD for col in zip(*b)] for row in a]
def poly_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def polynomial(c,x):
 n=len(x);v=[[0]*n for _ in range(n)]
 for z in reversed(c):
  v=mul(v,x)
  for i in range(n):v[i][i]=(v[i][i]+z)%MOD
 return v
def join(*a):return [sum((x[i] for x in a),[]) for i in range(len(a[0]))]
def basis(a,e):
 n=len(e);r=[list(c) for c in zip(*a)]
 r += [[P**e[j] if i==j else 0 for i in range(n)] for j in range(n)]
 h=fmpz_mat(r).hnf()
 b=[[int(h[i,j]) for j in range(n)] for i in range(h.nrows()) if any(h[i,j] for j in range(n))]
 require(len(b)==n,'full ambient integer lattice');return fmpz_mat(b)
def integral_matrix(a):
 out=[]
 for i in range(a.nrows()):
  row=[]
  for j in range(a.ncols()):
   z=Fraction(str(a[i,j]));require(z.denominator==1,'exact sublattice inclusion');row.append(z.numerator)
  out.append(row)
 return fmpz_mat(out)
def p_exponents(a):
 s=a.snf();out=[]
 for i in range(s.nrows()):
  z=abs(int(s[i,i]));require(z>0,'finite relative quotient');e=0
  while z%P==0:z//=P;e+=1
  require(z==1,'relative lattice quotient has only the true coefficient prime')
  if e:out.append(e)
 return sorted(out)
def quotient(outer,inner):
 c=integral_matrix(fmpq_mat(inner)*outer.inv())
 require(c*outer==inner,'all relative inclusion products')
 return p_exponents(c)
def row_coordinates(v,b):return fmpq_mat([v])*b.inv()
def denominator_lcm(v):
 import math
 q=1
 for i in range(v.nrows()):
  for j in range(v.ncols()):q=math.lcm(q,Fraction(str(v[i,j])).denominator)
 return q
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--data',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();start=time.monotonic()
 pin=identity(a.data);require((pin['bytes'],pin['sha256'])==PIN,'complete original presentation pin')
 d=json.loads(a.data.read_bytes());require(d['binding']==BINDING,'complete original binding')
 A=d['coordinateRows'];e=d['ambientExponents'];X=d['xActionOnOriginal26Generators'];n=len(X)
 require(len(A)==14 and len(A[0])==26 and n==26,'entire original coordinate frame')
 # Evaluate the original polynomial directly at s=2+x. No Hensel factor or
 # producer extension coordinate is used to construct this image.
 h=poly_mul([0,0,0,1],poly_mul(poly_mul([-8,32,-25,5],[-8,32,-25,5]),poly_mul(poly_mul([864,864,135,5],[864,864,135,5]),[9600,-25472,-3392,15936,-2888,-936,153,50,5])))
 require(len(h)==24 and h[-1]==3125,'original hstar parameters')
 SX=[row[:] for row in X]
 for i in range(n):SX[i][i]=(SX[i][i]+2)%MOD
 H=mul(A,polynomial(h,SX));B=join(d['originalNineHstarCoordinates'],d['originalNineXHstarCoordinates'])
 b=[row[0] for row in d['originalNineHstarCoordinates']]
 LS=basis(A,e);LH=basis(H,e);LB=basis(B,e);LHB=basis(join(H,[[z] for z in b]),e)
 require(LB==LHB,'entire original B equals hstar S plus the original b2')
 s_h=quotient(LS,LH);s_b=quotient(LS,LB)
 require(s_h==[1]*5+[2]*3 and s_b==[1]*4+[2]*3,'complete relative quotient Smith types')
 require(denominator_lcm(row_coordinates(b,LH))==P,'original extension class has exact order p')
 LP=basis(join([[P*z%MOD for z in row] for row in A],H),e)
 require(denominator_lcm(row_coordinates(b,LP))==P,'extension class is nonzero modulo p of the quotient')
 # This is the actual R b2: both b2 and x b2 are kept.
 RB=basis([[row[0],d['originalNineXHstarCoordinates'][i][0]] for i,row in enumerate(d['originalNineHstarCoordinates'])],e)
 s_rb=quotient(LS,RB);require(s_rb==[2]*7+[4,4,5],'complete original single-target quotient')
 result={'format':'r150-root-independent-extension-relative-lattice-audit-v1','status':'completed','source':identity(Path(__file__)),'completeData':pin,'parentBinding':BINDING,'method':'exact-relative-integer-lattice-inclusion-and-Smith','allRelativeInclusionProductsVerified':True,'originalPolynomialEvaluatedWithoutHenselFactor':True,'originalBIncludesBothNineColumnFamilies':True,'S2ModuloHstarS2Exponents':s_h,'S2ModuloBExponents':s_b,'S2ModuloOriginalRb2Exponents':s_rb,'originalBRecoveredFromHstarSAndB2':True,'extensionClassExactOrder':P,'extensionClassPrimitiveInQuotient':True,'originalLargeSolveRepeated':False,'mathematicalArraysTemporaryOnly':True,'elapsedSeconds':time.monotonic()-start}
 a.out.write_bytes(canonical(result));print(canonical(result).decode(),end='')
if __name__=='__main__':main()
