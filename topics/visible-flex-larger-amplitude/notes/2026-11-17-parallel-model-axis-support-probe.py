#!/usr/bin/env python3
"""Exact-rational axis support at specified stored nodes; no whole-field scan."""
import argparse,gzip,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
INPUT='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
FINAL='df41433b71147ac11d3f0193be31323d7e23a879cb2b05231d3a3e166b0d88fb'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lower(x):
 y=float(x);return math.nextafter(y,-math.inf)if F(y)>x else y
def upper(x):
 y=float(x);return math.nextafter(y,math.inf)if F(y)<x else y
def sqrt_up(x):
 assert x>=0
 k=math.isqrt((x.numerator<<160)//x.denominator)
 if k*k*x.denominator < x.numerator*(1<<160):k+=1
 return F(k,1<<80)
def exact(z):return F(float(z))
def main(a):
 selfsha=sha(__file__);assert sha(a.input)==INPUT and sha(a.gram_result)==FINAL
 d=json.loads(gzip.decompress(a.input.read_bytes()));r=json.loads(a.gram_result.read_bytes());M=d['M'];assert M==320 and r['complete_scope_certified'];x=[exact(z)for z in d['mesh']]
 targets=[F(v)for v in a.targets];indices=sorted({min(range(len(x)),key=lambda i:abs(x[i]-v))for v in targets});rows=[];deps={}
 for i in indices:
  owner=None;budget=None
  for ent in r['entries']:
   if ent['cell'] not in (max(0,i-1),min(i,len(x)-2)):continue
   p=Path(ent['report_path']);q=json.loads(p.read_bytes())
   if F(q['left_exact'])<=x[i]<=F(q['right_exact']):
    assert sha(p)==ent['report_sha256'];assert q['input_sha256']==INPUT and q['strict_under_stated_IEEE_arithmetic'];owner=ent;budget=q;deps[str(p)]=ent['report_sha256'];break
  assert budget is not None
  ep=exact(budget['lambda_minus_one']);ep1=exact(budget['lambda_s']);assert 0<=ep<1 and ep1>=0
  Y=[exact(v)for v in d['states'][i]];U=[exact(v)for v in d['rhs'][i]];assert len(Y)==len(U)==3*M+2
  c,cs=Y[2*M+1],U[2*M+1]
  for parity in (0,1):
   signs=[F(1 if parity==0 or j%2==0 else -1)for j in range(M+1)]
   R=sum(Y[j]*signs[j]for j in range(M+1));Rs=sum(U[j]*signs[j]for j in range(M+1))
   Z=c+sum(Y[2*M+1+j]*signs[j]for j in range(1,M+1));Zs=cs+sum(U[2*M+1+j]*signs[j]for j in range(1,M+1))
   dT=R+sum(2*j*Y[M+j]*signs[j]for j in range(1,M+1));assert R>0 and dT>0
   D=R*Zs-Z*Rs;E=(2*ep+ep*ep)*abs(D)+(1+ep)*ep*abs(R*cs-c*Rs)+ep1*abs(c*R)
   lo,hi=D-E,D+E;vr=(1+ep)*abs(Rs)+ep1*abs(R);vz=abs(Zs)+ep*abs(Zs-cs)+ep1*abs(Z-c);un=sqrt_up(vr*vr+vz*vz)
   q=dict(node=i,s=float(x[i]),s_exact=str(x[i]),axis='phi=0'if parity==0 else'phi=pi/2',raw_coefficients={k:str(v)for k,v in dict(R=R,Z=Z,R_s=Rs,Z_s=Zs,c=c,c_s=cs,dT=dT).items()},raw_support_numerator_exact=str(D),normalization_error_upper_exact=str(E),G_support_numerator_lower_exact=str(lo),G_support_numerator_upper_exact=str(hi),G_support_numerator_lower=lower(lo),G_support_numerator_upper=upper(hi),G_meridian_speed_upper=upper(un),positive_support_at_this_point=lo>0,negative_support_at_this_point=hi<0,gram_budget_sha256=owner['report_sha256'])
   if lo>0:q['G_unit_support_lower']=lower(lo/un)
   rows.append(q)
 assert sha(a.input)==INPUT and sha(a.gram_result)==FINAL and sha(__file__)==selfsha
 out=dict(scope=__doc__,source_sha256=selfsha,input_sha256=INPUT,gram_result_sha256=FINAL,targets=a.targets,selected_nodes=indices,construction_angles=4096,center=[0,0,0],normal_orientation='G_phi cross G_s',exact_axis_values=True,dependencies=deps,records=rows,all_selected_points_positive=all(z['positive_support_at_this_point']for z in rows),some_selected_point_negative=any(z['negative_support_at_this_point']for z in rows),whole_field_support_certified=False,reach_certified=False,closed_surface=False)
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(output=str(a.out),output_sha256=sha(a.out),source_sha256=selfsha,summary=[{k:z[k]for k in ('node','s','axis','G_support_numerator_lower','G_support_numerator_upper','positive_support_at_this_point','negative_support_at_this_point','G_unit_support_lower')if k in z}for z in rows]),indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--gram-result',type=Path,required=True);p.add_argument('--targets',nargs='+',default=['0','.5','.8','.95','.99','.995','1']);p.add_argument('--out',type=Path,required=True);main(p.parse_args())
