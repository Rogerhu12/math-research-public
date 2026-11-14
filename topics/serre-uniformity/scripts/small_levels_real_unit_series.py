#!/usr/bin/env python3
"""Exact real-branch modular-unit series for the R109 interval certificates.

Orbit equations, Bernoulli terms and trigonometric coefficients use Arb.
NumPy values and derivatives only rank which coordinate to try first; no
floating-point comparison is an exclusion certificate. See R109 and the
real-cusp-series note for the complete phase and coefficient derivations.
"""
import json,sys,time,math
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,arb_poly,fmpq,ctx
BASE=Path(__file__).resolve().parent
class UnitCurve:
 def __init__(self,p,c,terms=None,bits=256):
  ctx.prec=bits;self.p=p;self.c=c;self.J=terms or 12*p;self.d=(p-1)//2
  cert=json.loads((BASE/'data/small_levels_archimedean_reduction.json').read_text());lev=next(x for x in cert['levels'] if x['p']==p);old=lev['cusps'][c-1]
  self.g,self.xi=g,xi=lev['g'],lev['xi'];self.kappa=arb(fmpq(lev['kappa_upper_numerator'],2**64))
  logs=[None]+[(2*arb.sin_pi_fmpq(fmpq(a,p))).log() for a in range(1,p)]
  E=arb_mat([[2*logs[pow(g,k,p)]]+[logs[(j*pow(g,k,p))%p]-logs[pow(g,k,p)] for j in range(2,self.d+1)] for k in range(self.d)])
  self.A=A=E.inv();self.delta=[z[0] for z in (A*arb_mat([[arb(fmpq(*v))] for v in old['v']])).tolist()];self.theta=[z[0] for z in (A*arb_mat([[2*sum(n*logs[y] for y,n in row)] for row in old['gamma']])).tolist()]
  invc=pow(c,-1,p);a,b=next((a,b) for a in range(p) for b in range(p) if (a*a-xi*b*b)%p==invc)
  self.matrix=[c*a%p,xi*b%p,c*b%p,a];index={v:k for k in range(self.d) for v in [pow(g,k,p),-pow(g,k,p)%p]}
  self.points=[[[ ] for x in range(p)] for k in range(self.d)]
  for x in range(p):
   for y in range(p):
    if x==y==0:continue
    k=index[(xi*invc*x*x-c*y*y)%p];self.points[k][x].append(y)
  for k,row in enumerate(self.points):
   assert all(len(ys)<=4 and sorted(ys)==sorted(-y%p for y in ys) for ys in row)
   moment=sum(len(ys)*(6*x*x-6*p*x+p*p) for x,ys in enumerate(row))
   assert fmpq(-2*moment,12*p*p)==fmpq(*old['v'][k])
   assert [[y,1] for y in row[0]]==old['gamma'][k]
  cos=[arb.cos_pi_fmpq(fmpq(2*z,p)) for z in range(p)]
  cy=[[[sum((cos[y*r%p] for y in ys),arb(0)) for r in range(p)] for ys in row] for row in self.points]
  S=[[arb(0) for n in range(self.J)] for k in range(self.d)]
  for divisor in range(1,self.J+1):
   for n in range(divisor,self.J+1,divisor):
    r=n//divisor%p;x=divisor%p
    for k in range(self.d):S[k][n-1]+=divisor*cy[k][x][r]
  C=A*arb_mat(S)
  self.coeff=[[arb(0)]+[-4*C[k,n-1]/n for n in range(1,self.J+1)] for k in range(self.d)]
  self.fcoeff=np.array([[float(x.mid()) for x in row] for row in self.coeff]);self.fd=np.array([float(x.mid()) for x in self.delta]);self.ft=np.array([float(x.mid()) for x in self.theta]);self.nn=np.arange(self.J+1)
  self.phase_table=[arb.cos_pi_fmpq(fmpq(z,p)) for z in range(2*p)]
  self.h=None
 def phase(self,h):
  if self.h==h:return
  self.h=h
  self.phases=[self.phase_table[h*n%(2*self.p)] for n in range(self.J+1)]
  self.polys=[arb_poly([c*z for c,z in zip(row,self.phases)]) for row in self.coeff]
  self.fpolys=self.fcoeff*np.array([float(z.mid()) for z in self.phases])
  self.fderivs=self.fpolys*(-self.nn/self.p)
 def value(self,s):
  powers=np.exp(-s/self.p*self.nn)
  return self.fd*s+self.ft+self.fpolys@powers
 def derivative(self,s):
  return self.fd+self.fderivs@np.exp(-s/self.p*self.nn)
 def tail(self,s):
  t=(-arb(s)/self.p).exp();u=self.J+1
  return 8*self.kappa*t**u*((u+1)-u*t)/(1-t)**2
 def avalue(self,s,j):
  s=arb(s);t=(-s/self.p).exp()
  return self.delta[j]*s+self.theta[j]+self.polys[j](t)+arb(0,self.tail(s).upper())
