#!/usr/bin/env python3
"""Refine only unpaid q106 domain boxes using the full original quintics.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Every already positive interval from the pinned complete first pass is
retained verbatim. Failed boxes are bisected in physical s; all 85 state
values are re-enclosed by exact-rational Bernstein conversion of the six
original binary quintic coefficients on that smaller interval. The same
complete background, angle and repair-homotopy enclosures are then applied.
No original field, metric, numerical source or physical ODE is changed.
"""
import ast
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE/'strong_newg_continuous_mean_domain.py'
ORIGINAL_SHA='66e3c84b0f58fc7b7578615a2a6bf3823e6d7cf7cf2635d93157218f8d6facb1'
PRIOR_SHA='e8eb6d474b9f8d4a9d03100b038e3c4d8757341e3941cc12a12d9afaa322ce76'


def unique(source,before,after):
    if source.count(before)!=1:raise ValueError('Frozen domain edit site is not unique: '+before[:100])
    changed=source.replace(before,after,1)
    if changed.count(after)!=1 or changed.replace(after,before,1)!=source:
        raise ValueError('Domain edit is not exactly reversible')
    return changed


def main():
    source=ORIGINAL.read_text()
    if hashlib.sha256(source.encode()).hexdigest()!=ORIGINAL_SHA:
        raise ValueError('Original full-domain producer changed')
    changes=[]
    def edit(before,after):
        nonlocal source
        source=unique(source,before,after);changes.append((before,after))
    edit('from math import factorial\n','from math import factorial, comb\nfrom flint import fmpq as QQ\n')
    edit(" p.add_argument('--radial-limit',type=int,default=0,help='Explicit partial development run only')\n",
         " p.add_argument('--radial-limit',type=int,default=0,help='Explicit partial development run only')\n"
         " p.add_argument('--prior',type=Path,required=True)\n"
         " p.add_argument('--primary',type=Path,required=True)\n"
         " p.add_argument('--max-radial-depth',type=int,default=8)\n")
    edit(" M=manifest['modes'];n=3*M+1;gauge=binary(saved['gauge']);L=binary(saved['meridian_length'])\n",
         " M=manifest['modes'];n=3*M+1;gauge=binary(saved['gauge']);L=binary(saved['meridian_length'])\n"
         " if sha(a.prior)!=REFINE_PRIOR_SHA or sha(a.primary)!=primary:raise ValueError('Original full-domain or primary identity changed')\n"
         " prior=read(a.prior);primary_record=read(a.primary)\n"
         " if (not prior['complete_original_interval_cover'] or prior['source_sha256']!=REFINE_ORIGINAL_SHA or prior['primary_sha256']!=primary or not primary_record['solver_success'] or primary_record.get('audit_pending',True)):raise ValueError('Complete real prior/primary required')\n"
         " prior_rows={(r['original_interval'],*r['s_interval']):r for r in prior['rows']}\n"
         " if len(prior_rows)!=len(prior['rows']):raise ValueError('Duplicate original domain atoms')\n"
         " C=np.empty((6,manifest['original_physical_intervals'],n),dtype=np.float64);covered=0;coefficient_ids={}\n"
         " for chunk in primary_record['pp_coefficient_chunks']:\n"
         "  file=a.primary.parent/chunk['file'];lo=chunk['state_first'];hi=chunk['state_last_exclusive']\n"
         "  if Path(chunk['file']).name!=chunk['file'] or lo!=covered or not lo<hi<=n or sha(file)!=chunk['sha256']:raise ValueError('Original quintic chunk coverage or SHA')\n"
         "  with gzip.open(file,'rb') as stream:values=np.load(stream,allow_pickle=False)\n"
         "  if values.dtype!=np.float64 or values.shape!=(6,manifest['original_physical_intervals'],hi-lo) or not np.isfinite(values).all():raise ValueError('All original binary quintic coefficients required')\n"
         "  C[:,:,lo:hi]=values;covered=hi;coefficient_ids[str(file)]=sha(file)\n"
         " if covered!=n or len(primary_record['mesh'])!=manifest['original_physical_intervals']+1:raise ValueError('Complete original physical states/mesh required')\n"
         " if not 1<=a.max_radial_depth<=12:raise ValueError('Explicit finite radial subdivision depth 1..12 required')\n")
    edit(" repair=np.array([up(float(dy(r['global_correction_C0_C1_C2'][0]))) for r in state['state_bounds']])\n",
         " repair=np.array([up(float(dy(r['global_correction_C0_C1_C2'][0]))) for r in state['state_bounds']])\n"
         " exact_power_cache={}\n"
         " def refined_state_box(index,left,right):\n"
         "  if index not in exact_power_cache:\n"
         "   exact_power_cache.clear();exact_power_cache[index]=[[QQ(*float(C[5-j,index,k]).as_integer_ratio()) for j in range(6)] for k in range(n)]\n"
         "  origin=F.from_float(float(primary_record['mesh'][index]));x=left-origin;h=right-left\n"
         "  if not origin<=left<right<=F.from_float(float(primary_record['mesh'][index+1])):raise ArithmeticError('Subinterval outside original quintic')\n"
         "  X=QQ(x.numerator,x.denominator);H=QQ(h.numerator,h.denominator)\n"
         "  transforms=[[QQ(comb(j,i))*X**(j-i)*H**i for j in range(i,6)] for i in range(6)]\n"
         "  result=[]\n"
         "  for power in exact_power_cache[index]:\n"
         "   normalized=[sum((transforms[i][j-i]*power[j] for j in range(i,6)),QQ(0)) for i in range(6)]\n"
         "   bern=[sum((normalized[i]*QQ(comb(k,i),comb(5,i)) for i in range(k+1)),QQ(0)) for k in range(6)]\n"
         "   lo,hi=min(bern),max(bern);fl=F(int(lo.p),int(lo.q));fh=F(int(hi.p),int(hi.q))\n"
         "   result.append([down(float(fl)),up(float(fh))])\n"
         "  return widen(np.asarray(result).T,repair)\n")
    edit(" rows=[];failures=[];intervals=0;atoms=0;cursor=F(0);piece_index=0;inputids={str(getattr(a,k)):sha(getattr(a,k)) for k in PINS}\n",
         " rows=[];failures=[];intervals=0;atoms=0;cursor=F(0);piece_index=0;inputids={str(getattr(a,k)):sha(getattr(a,k)) for k in PINS}\n"
         " inputids.update({str(a.prior):sha(a.prior),str(a.primary):sha(a.primary),str(REFINE_ORIGINAL_PATH):REFINE_ORIGINAL_SHA,**coefficient_ids})\n"
         " reused_atoms=0;refined_original_atoms=0;refined_leaves=0;seen_prior=set()\n"
         " def refine_atom(index,pindex,left,right,depth):\n"
         "  nonlocal atoms,refined_leaves\n"
         "  yy=refined_state_box(index,left,right);radius,ap=background_box(pieces[pindex],left,right);N=max(1024,a.angular_start)\n"
         "  passed,bounds=domain(yy,radius,ap,left,right,N)\n"
         "  if not passed and depth<a.max_radial_depth:\n"
         "   middle=(left+right)/2;refine_atom(index,pindex,left,middle,depth+1);refine_atom(index,pindex,middle,right,depth+1);return\n"
         "  while not passed and N<a.angular_max:\n"
         "   N*=2;passed,bounds=domain(yy,radius,ap,left,right,N)\n"
         "  item=dict(original_interval=index,background_piece=pindex,s_interval=[str(left),str(right)],angular_intervals=N,radial_subdivision_depth=depth,original_binary_quintic_exact_Bernstein_restricted=True,whole_radial_angular_and_repair_homotopy_enclosed=True,positive_domain=passed,**bounds)\n"
         "  rows.append(item);atoms+=1;refined_leaves+=1\n"
         "  if not passed:failures.append(item)\n")
    before="""    radius,ap=background_box(piece,left,right);N=a.angular_start
    while True:
     passed,bounds=domain(Y,radius,ap,left,right,N)
     if passed or N>=a.angular_max:break
     N*=2
    item=dict(original_interval=intervals,background_piece=piece_index,s_interval=[str(left),str(right)],
     angular_intervals=N,whole_radial_angular_and_repair_homotopy_enclosed=True,positive_domain=passed,**bounds)
    rows.append(item);atoms+=1
    if not passed:failures.append(item)
"""
    after="""    key=(intervals,str(left),str(right));old=prior_rows.get(key)
    if old is None or old['background_piece']!=piece_index:raise ArithmeticError('Original complete atom cover changed')
    seen_prior.add(key)
    if old['positive_domain']:
     rows.append(dict(old,retained_original_positive_box_verbatim=True));atoms+=1;reused_atoms+=1
    else:
     refined_original_atoms+=1;refine_atom(intervals,piece_index,left,right,0)
"""
    edit(before,after)
    edit(" if not a.radial_limit and not complete:raise ArithmeticError('Complete original field was not consumed')\n",
         " if not a.radial_limit and not complete:raise ArithmeticError('Complete original field was not consumed')\n"
         " if complete and seen_prior!=set(prior_rows):raise ArithmeticError('An original prior atom was not consumed')\n"
         " coverage_cursor=F(0)\n"
         " for rr in rows:\n"
         "  lo,hi=map(F,rr['s_interval'])\n"
         "  if lo!=coverage_cursor or not lo<hi:raise ArithmeticError('Refined physical cover has a gap or overlap')\n"
         "  coverage_cursor=hi\n"
         " if complete and coverage_cursor!=L:raise ArithmeticError('Refined cover misses the actual endpoint')\n")
    edit("  continuous_product_atoms=atoms,failed_atoms=len(failures),rows=rows,\n",
         "  continuous_product_atoms=atoms,failed_atoms=len(failures),rows=rows,\n"
         "  adaptive_exact_radial_refinement=dict(retained_positive_prior_atoms=reused_atoms,unpaid_original_atoms_refined=refined_original_atoms,refined_leaves=refined_leaves,max_depth=a.max_radial_depth,original_full_pass_sha256=sha(a.prior),exact_complete_refined_coverage=True),\n")
    ast.parse(source)
    reverse=source
    for before,after in reversed(changes):reverse=unique(reverse,after,before)
    if reverse!=ORIGINAL.read_text():raise ValueError('Refinement changed an unlisted original formula')
    namespace=dict(__file__=str(Path(__file__).resolve()),__name__='actual_continuous_domain_exact_radial_refinement',
        REFINE_ORIGINAL_SHA=ORIGINAL_SHA,REFINE_PRIOR_SHA=PRIOR_SHA,REFINE_ORIGINAL_PATH=ORIGINAL)
    exec(compile(source,'<original-domain-with-exact-local-refinement>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
