#!/usr/bin/env python3
"""Strict lambda/lambda'/lambda'' bounds on one unchanged pulse cell or part.

Uses the frozen complete Gram engine once. A Python return observer retains
its already computed interval polynomials; it does not alter any arithmetic,
field, parameter, source, or existing report. The S residual is then formed
and enclosed by the same directed finite-polynomial cover.
"""
import argparse,contextlib,hashlib,importlib.util,io,json,math,sys,time
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace
import numpy as np

ENGINE_SHA='d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main(a):
 begin=time.perf_counter();source_sha=sha(__file__)
 if sha(a.engine)!=ENGINE_SHA:raise ValueError('Frozen Gram engine changed')
 engine=load(a.engine,'fixed_lambda2_gram_engine');state={}
 def observe(frame,event,arg):
  if event=='return'and frame.f_code is engine.main.__code__:state.update(frame.f_locals)
 base_path=a.out.with_name(a.out.stem+'-gram-base.json')
 config=SimpleNamespace(input=a.input,interval_source=a.interval_source,scalar_oracle=a.scalar_oracle,out=base_path,cell=a.cell,part=a.part,angles=16384,scalar_panels=4096)
 previous=sys.getprofile()
 try:
  sys.setprofile(observe)
  with contextlib.redirect_stdout(io.StringIO()):engine.main(config)
 finally:sys.setprofile(previous)
 base=json.loads(base_path.read_bytes())
 I=state['I'];A=state['A'];Ap=state['Ap'];R=state['RG'];rho=state['rho'];N=state['N'];Qn=state['Qn'];M=state['M']
 padd=state['padd'];pmul=state['pmul'];pder=state['pder'];pmean=state['pmean'];pbound=state['pbound'];cover=state['cover']
 add=state['uadd'];mul=state['umul'];div=state['udiv'];lp=state['lpower'];up=state['upower'];lm=state['lmul'];ldiff=state['lowdiff'];la=state['ladd']
 # S=A R_s-3A'R=A^2 G_ss-4AA'G_s+(6A'^2-2AA'')G.
 # Thus its radial degree is 18 for exact old quintics (14 for Taylor A).
 S=padd(pmul(A,pder(R)),I.scale(pmul(Ap,R),3),-1)
 samples=I.div(I.at(S,(slice(None),slice(None,None,Qn//N))),I.at(rho,slice(None,None,Qn//N)))
 meanS=pbound(pmean(samples));normS=cover(S,'S_over_rho','even',4*M,1)
 Amin=state['Amin'];bmin=state['bmin'];rho_min=state['rho_min'];U=state['U'];rootlo=state['sqrtUlo'];oneU=state['oneU']
 factor=div(U,lm(rootlo,la(1.,rootlo)))
 h_s=div(state['meanC'],Amin)
 linear=div(meanS,lm(2.,lp(Amin,4)))
 nonlinear_S=mul(div(normS,lm(2.,lp(Amin,4))),factor)
 nonlinear_R=div(up(state['Rn'],2),lm(4.,lm(lp(Amin,6),lm(rho_min,lm(oneU,rootlo)))))
 h_ss=add(linear,nonlinear_S,nonlinear_R)
 Lambda_max=add(1.,div(state['bA'],bmin))
 Lambda_s=mul(up(Lambda_max,2),h_s)
 Lambda_ss=add(mul(mul(2.,up(Lambda_max,3)),up(h_s,2)),mul(up(Lambda_max,2),h_ss))
 # lambda=(a/A)*Lambda. Pay the complete second derivative of a/A.
 ea=state['ea'];eap=state['eap'];hq=state['hq'];a4=state['a4bound']
 ea2Q=Q(a4)*(hq/2)**2/2
 ea2=0. if ea2Q==0 else float(I.up(float(ea2Q)))
 if Q.from_float(ea2)<ea2Q:raise ValueError('Second Taylor remainder not outward')
 Appmax=pbound(pder(Ap));Apmax=state['Apmax']
 beta_max=add(1.,div(ea,Amin))
 beta_s=add(div(eap,Amin),div(mul(ea,Apmax),lp(Amin,2)))
 beta_ss=add(div(ea2,Amin),div(mul(ea,Appmax),lp(Amin,2)),div(mul(2.,mul(eap,Apmax)),lp(Amin,2)),div(mul(2.,mul(ea,up(Apmax,2))),lp(Amin,3)))
 lambda_ss=add(mul(beta_max,Lambda_ss),mul(2.,mul(beta_s,Lambda_s)),mul(beta_ss,Lambda_max))
 if not all(math.isfinite(v)for v in (meanS,normS,h_s,h_ss,lambda_ss)):raise ValueError('Nonfinite second-derivative budget')
 report=dict(scope=__doc__,source_sha256=source_sha,engine_sha256=ENGINE_SHA,base_gram_report_sha256=sha(base_path),input_sha256=base['input_sha256'],interval_source_sha256=sha(a.interval_source),scalar_oracle_sha256=sha(a.scalar_oracle),cell=a.cell,part=a.part,left_exact=base['left_exact'],right_exact=base['right_exact'],construction_angles=4096,audit_angles=16384,scalar_panels=4096,scalar_kind=base['scalar_kind'],A_degree=base['scalar_polynomial_degree'],S_radial_degree=len(S[0])-1,S_angular_bandwidth=4*M,S_cover=state['cover_stats']['S_over_rho'],mean_S_over_rho_bound=meanS,S_over_rho_bound=normS,h_s_bound=h_s,h_ss_bound=h_ss,h_ss_linear_mean_term=linear,h_ss_sqrt_remainder=nonlinear_S,h_ss_quadratic_R_term=nonlinear_R,Lambda_max=Lambda_max,Lambda_s_bound=Lambda_s,Lambda_ss_bound=Lambda_ss,a_second_Taylor_error=ea2,A_second_derivative_bound=Appmax,beta_max=beta_max,beta_s_bound=beta_s,beta_ss_bound=beta_ss,lambda_minus_one_bound=state['ld'],lambda_s_bound=state['ls'],lambda_ss_bound=lambda_ss,all_radius_covered=True,strict_under_stated_IEEE_arithmetic=True,only_F_s_s_phi_required=True,curvature_certified=False,seconds=time.perf_counter()-begin)
 if sha(__file__)!=source_sha or sha(a.engine)!=ENGINE_SHA:raise ValueError('Source changed during companion calculation')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('report_sha256',sha(a.out))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('input','engine','interval-source','scalar-oracle','out'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--cell',type=int,required=True);p.add_argument('--part',choices=['all','before','after'],default='all')
 main(p.parse_args())
