#!/usr/bin/env python3
"""Strict scaling jets from the fixed 4096 construction nodes only.

Reuses the exact scalar/field preparation of the frozen representative engine.
The finite mean b=mean_j |F_phi(s,2*pi*j/4096)| defines lambda=a/b.
Every radial point is covered by directed Bernstein bounds. No continuous
angular claim, Fourier interpolation of a nonlinear residual, or curvature
claim is made by this kernel.
"""
import argparse,hashlib
from pathlib import Path

ENGINE_SHA='d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882'
REFERENCE_SHA='83ee1ba24ee0c68be8b92369cd10ee8d6932d7e480efee11caff4ddf2a550cf0'

NODE_TAIL=r'''
 # Only fixed construction nodes occur below.  Their rho mean equals one
 # exactly because rho has Fourier degree 2*M=640 < N=4096.
 T=jet(co);G=pdot(T,T);AA=pmul(A,A)
 DG=padd(G,I.mul(AA,rho_sq),-1)
 RG=padd(pmul(A,pder(G)),I.scale(pmul(Ap,G),2),-1)
 SG=padd(pmul(A,pder(RG)),I.scale(pmul(Ap,RG),3),-1)
 d=I.div(DG,rho);r=I.div(RG,rho);ss=I.div(SG,rho)
 Dn=pbound(I.div(DG,rho_sq));Rn=pbound(r);Sn=pbound(ss)
 mD=pbound(pmean(d));mR=pbound(pmean(r));mS=pbound(pmean(ss))
 U=udiv(Dn,lpower(Amin,2))
 if not 0<=U<1:raise ValueError('Fixed-node square-root expansion invalid')
 oneU=lowdiff(1.,U);sqrtUlo=float(I.sqrt(I.exact(oneU))[0])
 eta=udiv(U,lmul(sqrtUlo,ladd(1.,sqrtUlo)))
 eq=udiv(umul(umul(Amax,rho_max),upower(U,2)),lmul(8.,lmul(oneU,sqrtUlo)))
 bA=uadd(udiv(mD,lmul(2.,Amin)),eq);bmin=lowdiff(Amin,bA)
 if bmin<=0:raise ValueError('Finite mean speed lost positivity')
 ld=udiv(uadd(ea,bA),bmin);lambda_max=uadd(1.,ld)
 C0=udiv(Rn,lmul(2.,lpower(Amin,2)));ec=umul(C0,eta)
 meanC=uadd(udiv(mR,lmul(2.,lpower(Amin,2))),ec)
 gamma=udiv(meanC,bmin)
 ratioerr=udiv(uadd(umul(eap,Amax),umul(Apmax,ea)),lmul(lowdiff(Amin,ea),Amin))
 ls=uadd(0.,umul(lambda_max,uadd(ratioerr,gamma)))
 h_s=udiv(meanC,Amin)
 hss_mean=udiv(mS,lmul(2.,lpower(Amin,4)))
 hss_rem=umul(udiv(Sn,lmul(2.,lpower(Amin,4))),eta)
 hss_R2=udiv(upower(Rn,2),lmul(4.,lmul(lpower(Amin,6),lmul(rho_min,lmul(oneU,sqrtUlo)))))
 h_ss=uadd(hss_mean,hss_rem,hss_R2)
 Lambda_max=uadd(1.,udiv(bA,bmin))
 Lambda_s=umul(upower(Lambda_max,2),h_s)
 Lambda_ss=uadd(umul(umul(2.,upower(Lambda_max,3)),upower(h_s,2)),umul(upower(Lambda_max,2),h_ss))
 ea2Q=Q(a4bound)*(hq/2)**2/2
 ea2=0. if ea2Q==0 else float(I.up(float(ea2Q)))
 if Q.from_float(ea2)<ea2Q:raise ValueError('Second Taylor remainder not outward')
 Appmax=pbound(pder(Ap));beta_max=uadd(1.,udiv(ea,Amin))
 beta_s=uadd(udiv(eap,Amin),udiv(umul(ea,Apmax),lpower(Amin,2)))
 beta_ss=uadd(udiv(ea2,Amin),udiv(umul(ea,Appmax),lpower(Amin,2)),udiv(umul(2.,umul(eap,Apmax)),lpower(Amin,2)),udiv(umul(2.,umul(ea,upower(Apmax,2))),lpower(Amin,3)))
 ls_product=uadd(umul(beta_s,Lambda_max),umul(beta_max,Lambda_s))
 ls=min(ls,ls_product)
 lss=uadd(umul(beta_max,Lambda_ss),umul(2.,umul(beta_s,Lambda_s)),umul(beta_ss,Lambda_max))
 values=[ld,ls,lss,rho_min,rho_max,Amin,Amax,U,Dn,Rn,Sn,mD,mR,mS,bmin]
 if not all(math.isfinite(v)and v>=0 for v in values):raise ValueError('Nonfinite/negative certificate bound')
 report=dict(scope=__doc__,source_sha256=source_sha,engine_sha256=ENGINE_SHA,generated_kernel_sha256=GENERATED_SHA,input_sha256=expected,dependencies={str(p):s for p,s in dependency_hashes.items()},interval_source_sha256=sha(a.interval_source),scalar_oracle_sha256=sha(a.scalar_oracle),cell=i,part=a.part,left_exact=str(left),right_exact=str(right),original_left=float(x[i]),original_right=float(x[i+1]),exact_pulse_midpoint=str(boundary),construction_angles=N,evaluated_angles=Qn,scalar_panels=a.scalar_panels,scalar_kind=scalar_kind,scalar_quintic_knot=scalar_knot,A_degree=len(A[0])-1,D_radial_degree=len(DG[0])-1,R_radial_degree=len(RG[0])-1,S_radial_degree=len(SG[0])-1,field_tangent_bandwidth=2*M,rho_lower_at_nodes=rho_min,rho_upper_at_nodes=rho_max,Amin=Amin,Amax=Amax,U_at_nodes=U,D_over_rho2_node_bound=Dn,R_over_rho_node_bound=Rn,S_over_rho_node_bound=Sn,mean_D_over_rho_bound=mD,mean_R_over_rho_bound=mR,mean_S_over_rho_bound=mS,sqrt_remainder_at_nodes=eq,mean_speed_difference=bA,mean_speed_lower=bmin,mean_C_bound=meanC,h_s_bound=h_s,h_ss_bound=h_ss,h_ss_linear_mean_term=hss_mean,h_ss_sqrt_remainder=hss_rem,h_ss_quadratic_R_term=hss_R2,Lambda_max=Lambda_max,Lambda_s_bound=Lambda_s,Lambda_ss_bound=Lambda_ss,a_Taylor_error=ea,ap_Taylor_error=eap,a_second_Taylor_error=ea2,A_second_derivative_bound=Appmax,beta_max=beta_max,beta_s_bound=beta_s,beta_ss_bound=beta_ss,lambda_minus_one_bound=ld,lambda_s_bound=ls,lambda_ss_bound=lss,all_radius_covered=True,strict_under_stated_IEEE_arithmetic=True,continuous_angle_cover_required_for_finite_mean=False,curvature_certified=False,seconds=time.perf_counter()-start)
 if a.reference is not None:
  rawref=a.reference.read_bytes();ref=json.loads(rawref)
  if ref['source_sha256']!=REFERENCE_SHA or ref['engine_sha256']!=ENGINE_SHA or ref['input_sha256']!=expected or ref['cell']!=i or ref['part']!=a.part or ref['left_exact']!=str(left)or ref['right_exact']!=str(right)or ref['construction_angles']!=4096:
   raise ValueError('Reference certificate has a different object or range')
  keys=['lambda_minus_one_bound','lambda_s_bound','lambda_ss_bound','mean_S_over_rho_bound','h_ss_bound']
  report['comparison']=dict(reference_sha256=hashlib.sha256(rawref).hexdigest(),reference_source_sha256=REFERENCE_SHA,reference_bounds={k:ref[k]for k in keys},node_bounds={k:report[k]for k in keys},reference_seconds=ref['seconds'],all_three_scaling_bounds_no_larger=all(report[k]<=ref[k]for k in keys[:3]))
 if sha(__file__)!=source_sha or sha(a.engine)!=ENGINE_SHA or sha(a.input)!=expected or any(sha(p)!=s for p,s in dependency_hashes.items()):raise ValueError('Input/source changed during certificate')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('report_sha256',sha(a.out))
'''

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main(a):
 if sha(a.engine)!=ENGINE_SHA:raise ValueError('Frozen representative engine changed')
 text=a.engine.read_text()
 cut=' F,T=jet(co);V,_=jet(pder(co));G=pdot(T,T);Mix=pdot(V,T);E=pdot(V,V)'
 if text.count(cut)!=1:raise ValueError('Expected unique preparation endpoint')
 text=text[:text.index(cut)]+NODE_TAIL
 def replace(old,new):
  nonlocal text
  if text.count(old)!=1:raise ValueError('Expected unique frozen source anchor: '+old[:60])
  text=text.replace(old,new)
 replace('Qn<=N or Qn&(Qn-1)','Qn!=N or Qn&(Qn-1)')
 first=text.index('"""');last=text.index('"""',first+3)+3
 text=text[:first]+repr(__doc__)+text[last:]
 tangent_start=text.index('  F=[tr.cosine_sine(')
 tangent_end=text.index('\n',tangent_start)+1
 text=text[:tangent_start]+text[tangent_end:]
 replace('  return F,t','  return t')
 start=text.index(' rho1=float(I.sum_upper(')
 end=text.index(' # Exact old quintic, or cubic Taylor',start)
 finite_density=" rho_min=float(rho[0].min());rho_max=float(rho[1].max())\n if rho_min<=0:raise ValueError('Construction-node density not positive')\n rho_sq=I.square(rho)\n"
 text=text[:start]+finite_density+text[end:]
 generated_sha=hashlib.sha256(text.encode()).hexdigest()
 namespace=dict(__name__='finite_mean_lambda2_kernel',__file__=__file__,ENGINE_SHA=ENGINE_SHA,REFERENCE_SHA=REFERENCE_SHA,GENERATED_SHA=generated_sha)
 exec(compile(text,str(a.engine)+'::finite-construction-node-scaling-jets','exec'),namespace)
 a.angles=4096;a.scalar_panels=4096
 namespace['main'](a)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('input','engine','interval-source','scalar-oracle','out'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--reference',type=Path)
 p.add_argument('--cell',type=int,required=True);p.add_argument('--part',choices=['all','before','after'],default='all')
 main(p.parse_args())
