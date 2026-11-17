#!/usr/bin/env python3
"""Reuse exact axis records and existing lambda budgets for beta=1/4 support."""
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
PARENT='828ad538cae8b9e44076246705533bc44e285854ccbead67d3277f0aba9cbfbe'
INPUT='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lower(x):
 y=float(x);return math.nextafter(y,-math.inf)if F(y)>x else y
def upper(x):
 y=float(x);return math.nextafter(y,math.inf)if F(y)<x else y
def main(a):
 selfsha=sha(__file__);assert sha(a.axis_report)==PARENT
 d=json.loads(a.axis_report.read_bytes());assert d['input_sha256']==INPUT and d['exact_axis_values'];beta=F(1,4);rows=[];deps={}
 paths={h:p for p,h in d['dependencies'].items()}
 for z in d['records']:
  h=z['gram_budget_sha256'];p=Path(paths[h]);assert sha(p)==h;budget=json.loads(p.read_bytes());assert budget['input_sha256']==INPUT and budget['strict_under_stated_IEEE_arithmetic'];deps[str(p)]=h
  eps=F(budget['lambda_minus_one']);eps1=F(budget['lambda_s']);v={k:F(s)for k,s in z['raw_coefficients'].items()};R,Z,Rs,Zs,c,cs=(v[k]for k in ('R','Z','R_s','Z_s','c','c_s'));assert R>0 and v['dT']>0
  D=R*Zs-beta*Z*Rs
  E=(2*eps+eps*eps)*abs(D)+(1+eps)*eps*abs(R*cs-beta*c*Rs)+eps1*abs(R)*((1-beta)*(1+eps)*abs(Z-c)+beta*abs(c))
  lo,hi=D-E,D+E;speed=F(z['G_meridian_speed_upper']);assert speed>0
  row=dict(node=z['node'],s=z['s'],axis=z['axis'],raw_weighted_numerator_exact=str(D),normalization_error_upper_exact=str(E),G_weighted_numerator_interval_exact=[str(lo),str(hi)],G_weighted_numerator_lower=lower(lo),G_weighted_numerator_upper=upper(hi),positive_weighted_support_at_this_point=lo>0)
  if lo>0:row['G_weighted_unit_support_lower_exact']=str(lo/speed);row['G_weighted_unit_support_lower']=lower(lo/speed)
  rows.append(row)
 assert sha(__file__)==selfsha and sha(a.axis_report)==PARENT
 out=dict(scope=__doc__,source_sha256=selfsha,parent_axis_report_sha256=PARENT,input_sha256=INPUT,beta_exact=str(beta),normal_orientation='G_phi cross G_s',new_field_samples=0,new_lambda_evaluations=0,dependencies=deps,records=rows,all_14_axis_points_positive=all(z['positive_weighted_support_at_this_point']for z in rows),minimum_unit_support_lower=min((z.get('G_weighted_unit_support_lower',-math.inf)for z in rows)),whole_field_weighted_support_certified=False,reach_certified=False,closed_surface=False)
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(source_sha256=selfsha,output=str(a.out),output_sha256=sha(a.out),minimum_unit_support_lower=out['minimum_unit_support_lower'],summary=[{k:z[k]for k in ('node','s','axis','G_weighted_numerator_lower','G_weighted_numerator_upper','G_weighted_unit_support_lower')if k in z}for z in rows]),indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--axis-report',type=Path,required=True);p.add_argument('--out',type=Path,required=True);main(p.parse_args())
