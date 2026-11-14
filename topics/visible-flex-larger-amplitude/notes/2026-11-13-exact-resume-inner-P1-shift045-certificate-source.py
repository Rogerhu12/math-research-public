#!/usr/bin/env python3
"""Actual complete641 fixedpoint in a new uniformly translated strip space.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only finite reference fields are reweighted. The radius and distance vector
are arbitrary exact positive dyadics proposed by a separate float run; all
source, self-map, derivative, physical and same-object gates below use Arb.
"""
import argparse,gzip,hashlib,json,resource,sys,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,arb_mat,ctx
BASE=Path('/workspace/scratch/d1aa462cfc02');TOP=BASE/'math-research/topics/visible-flex-larger-amplitude'
PINS={
 'low':('2026-11-12-closure-strong-same-tau-four-green-r1.json.gz','841c42ff527f2ca3846abf7ede8e9e03eb296a1f979cf7b01f48069197d312ac'),
 'split':('2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz','b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd'),
 'density':('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'jacobian':('2026-11-12-closure-strong-parameter-jacobian-r1.json.gz','7b9d5f6bafe69879246ee5edffbfdd280bfec0b5207c5ea6f79959fc3b61dfc4')}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ex(v):
 if isinstance(v,F):return v
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 v=ex(v);return arb(v.numerator)/v.denominator
def pack(z,bits=160):
 t=z.upper()
 if not(t.is_finite() and t>=0):raise ArithmeticError('Finite positive complete comparison required')
 if t==0:return ['0',0]
 m,e=map(int,t.man_exp());q=max(0,m.bit_length()-bits)
 if q:m,e=(m+(1<<q)-1)>>q,e+q
 ans=[str(m),e]
 if not ab(ans)>=t:raise ArithmeticError('Exact outward dyadic storage')
 return ans
def up(z):return ab(pack(z))
def arr(v):return [pack(z) for z in v]
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for n in ('modal-input','modal-resource','source-summary','source-resource','candidate','candidate-resource','out-prefix'):p.add_argument('--'+n,type=Path,required=True)
 p.add_argument('--rss-kib',type=int,default=98304);args=p.parse_args();ctx.prec=256;ctx.threads=1;start=time.monotonic()
 out=Path(str(args.out_prefix)+'.json.gz')
 if out.exists():raise FileExistsError('Preserve each complete new-strip attempt')
 sys.path.insert(0,str(TOP/'computations'));from closure_split_joint_io_v2 import read_field,iter_array,metadata_without_array
 ids={};paths={k:TOP/'notes'/v[0] for k,v in PINS.items()}
 for k,path in paths.items():
  if sha(path)!=PINS[k][1]:raise ArithmeticError('Original complete positive kernel pin '+k)
  ids[k]=dict(path=str(path),sha256=sha(path))
 for k in ('modal_input','modal_resource','source_summary','source_resource','candidate','candidate_resource'):
  path=getattr(args,k);ids[k]=dict(path=str(path.resolve()),sha256=sha(path))
 modal,mu,source,su,can,cu=(read(getattr(args,k)) for k in ('modal_input','modal_resource','source_summary','source_resource','candidate','candidate_resource'))
 for usage in (mu,su,cu):
  if not(usage['exitcode']==0 and usage['termination_signal'] is None):raise ArithmeticError('Owned formal input completion required')
 if not(modal['all_gates'] and all(modal['gates'].values()) and source['all_gates'] and all(source['gates'].values()) and source['all213_original_cells']):raise ArithmeticError('Complete true finite reference and source required')
 if not(modal['schema']=='inner-R100-uniformly-shifted-Cs-Lambda-modal-v1' and source['schema']=='visible-flex-R100-shifted-profile-complete-two-material-source-v1' and modal['domain']==source['domain']):raise ArithmeticError('Exactly matching translated source domain')
 if not(ex(modal['angular_weight_translation'])==F(9,20) and modal['cells']==list(range(12,225)) and modal['modes']==list(range(2,93,2)) and not modal['full_error_or_infinite_tail_reweighted']):raise ArithmeticError('Finite-only shift and all original cells/modes')
 shashes={str(Path(k).resolve()):v for k,v in source['input_hashes'].items()}
 if shashes.get(str(args.modal_input.resolve()))!=sha(args.modal_input) or shashes.get(str(paths['density'].resolve()))!=sha(paths['density']):raise ArithmeticError('Source actual modal and density identity')
 chashes={str(Path(k).resolve()):v for k,v in can['input_sha256'].items()}
 if chashes.get(str(args.modal_input.resolve()))!=sha(args.modal_input) or chashes.get(str(args.source_summary.resolve()))!=sha(args.source_summary) or can['certified'] or can['new_fixedpoint_claimed']:raise ArithmeticError('Candidate is only a matching numerical proposal')
 parent=read(Path(modal['input_identities']['parent_modal']['path']))
 if sha(Path(modal['input_identities']['parent_modal']['path']))!=modal['input_identities']['parent_modal']['sha256']:raise ArithmeticError('Original unshifted finite parent pin')
 gates={};counts={}
 def gate(k,b):
  b=bool(b);gates[k]=gates.get(k,True) and b;counts[k]=counts.get(k,0)+1;return b
 S=arb(257)/256;Z0=arb(2)**-2200;Zdom=ab(modal['far_domain']['proposed_new_graph_ball']);ratio=up(Zdom/Z0);delta=ab(modal['angular_weight_translation'])
 r=[ab(F.from_float(z)) for z in can['candidate_radius']];w=[ab(F.from_float(z)) for z in can['candidate_distance_weight']]
 if not(len(r)==len(w)==641 and all(z.is_finite() and z>0 for z in r+w)):raise ArithmeticError('All641 positive exact candidate dyadics')
 density=read(paths['density']);split=metadata_without_array(paths['split'],'gamma_rows');jm=metadata_without_array(paths['jacobian'],'rows')
 W0=list(map(ab,jm['metric_weights']));C=[ab(row['Cs_common_cap']) for row in modal['rows']];L=[ab(row['Lambda_common_cap_on_domain']) for row in modal['rows']];B=[ab(row['Cs_plus_Lambda_common_cap']) for row in modal['rows']]
 aa=[up(S*ab(row['V_over_w_upper'])) for row in density['rows']]
 base=read_field(paths['low'],'base');GL=arb_mat(213,213)
 if len(base)!=213 or any(len(row)!=213 for row in base):raise ArithmeticError('All213x213 low source entries')
 for k,row in enumerate(base):
  for n,z in enumerate(row):GL[k,n]=up(S*ab(z))
 del base
 GF=arb_mat(1,213);gfar=read_field(paths['low'],'far_z_source_upper')['base']
 for n,z in enumerate(gfar):GF[0,n]=up(S*S*ab(z)/Z0)
 GH={g:arb_mat(213,213) for g in ('near','rest')};q={g:[ab(row['source_common_mass']['common_d'][band]) for row in source['rows']] for g,band in [('near','near94to184'),('rest','rest186to8190'),('infinite','infinite8192up')]}
 pure=[arb(0)]*641;farimage=[arb(0)]*641;farjac=[arb(0)]*641
 for k,row in enumerate(iter_array(paths['split'],'gamma_rows')):
  if row['output_cell']!=12+k or len(row['sources'])!=213-k:raise ArithmeticError('Original causal source row order')
  for n,entry in enumerate(row['sources'],k):
   if entry['source_cell']!=12+n:raise ArithmeticError('Original causal source column order')
   for g in GH:GH[g][k,n]=up(S*ab(entry[g+'_gamma']))
  for g,off in [('near',213),('rest',426)]:
   f=ab(split['cells'][k]['far_boundary_'+g])/S
   farimage[off+k]=up(f*ratio*ratio);farjac[off+k]=up(4*f*ratio)
   pure[off+k]=up(sum((GH[g][k,n]*q[g][n] for n in range(k,213)),arb(0)))
 GI=up(S*ab(density['gamma_high']));pure[639]=up(GI*sum(q['infinite'],arb(0)));pure[640]=up(ab(modal['far_common_on_domain'])/Z0)
 f=ab(split['deep_high_boundary'])/S;farimage[639]=up(f*ratio*ratio);farjac[639]=up(4*f*ratio)
 seen=[]
 for row in iter_array(paths['jacobian'],'rows'):
  i=row['index']
  if i<213 or i==640:
   z=next((ab([m,e]) for j,m,e in row['coefficients'] if j==640),None)
   if z is None:raise ArithmeticError('Every original actual far derivative column retained')
   farjac[i]=up(z*W0[i]/W0[640]*ratio/(S if i<213 else 1));seen.append(i)
 gate('all_original_low_far_columns',set(seen)==set(list(range(213))+[640]))
 SL=arb_mat(213,1);DL=arb_mat(213,1);H={g:arb_mat(213,1) for g in ('near','rest','infinite')};DH={g:arb_mat(213,1) for g in H};rows=[]
 dow={k:up((-m*delta).exp()) for k,m in [('low',2),('near',94),('rest',186),('infinite',8192)]}
 maxphysical=arb(0);maxold=arb(0)
 for n in range(213):
  lo,ne,re,hi=r[n],r[213+n],r[426+n],r[639];t=up(lo+ne+re+hi);var=up(L[n]+t)
  dw=up(w[n]+w[213+n]+w[426+n]+w[639])
  ql=up((arb(23)/9)*C[n]*(L[n]+lo+ne));qs=up((arb(23)/18)*var*var)
  tl=up(270*aa[n]*(C[n]+var)*(C[n]*var+var*var/2));SL[n,0]=up(ql+qs+tl)
  DL[n,0]=up((arb(23)/9)*C[n]*(w[n]+w[213+n])+(arb(23)/9)*var*dw+270*aa[n]*(C[n]*C[n]+3*C[n]*var+arb(3)*var*var/2)*dw)
  sq=up((arb(23)/18)*t*t);th=up(270*aa[n]*(B[n]+t)*(B[n]*t+t*t/2))
  dr=up((arb(23)/9)*t*dw+270*aa[n]*(B[n]*B[n]+3*B[n]*t+arb(3)*t*t/2)*dw)
  act={'near':lo+ne+re,'rest':ne+re+hi,'infinite':re+hi}
  dact={'near':w[n]+w[213+n]+w[426+n],'rest':w[213+n]+w[426+n]+w[639],'infinite':w[426+n]+w[639]}
  for g in H:H[g][n,0]=up((arb(23)/9)*B[n]*act[g]+sq+th);DH[g][n,0]=up((arb(23)/9)*B[n]*dact[g]+dr)
  phys=up(aa[n]*max(C[n]+var,B[n]+t));old=up(dow['low']*lo+dow['near']*ne+dow['rest']*re+dow['infinite']*hi+ab(parent['rows'][n]['Lambda_common_cap_on_domain']))
  maxphysical=max(maxphysical,phys);maxold=max(maxold,old)
  gate('whole_new_ball_full_mean_inverse_Hessian_domain',phys<arb(1)/128)
  rows.append(dict(cell=n+12,error_total=pack(t),low_Lambda_plus_error=pack(var),low_quadratic_linear=pack(ql),low_quadratic_new=pack(qs),low_complete_T=pack(tl),low_source=pack(SL[n,0]),low_directional_source=pack(DL[n,0]),
   high_quadratic_new=pack(sq),high_complete_T=pack(th),high_source={g:pack(H[g][n,0]) for g in H},high_directional_source={g:pack(DH[g][n,0]) for g in H},physical_whole_ball=pack(phys),lowered_original_work_radius=pack(old)))
 low=GL*SL;dlow=GL*DL;fars=(GF*SL)[0,0];dfar=(GF*DL)[0,0];high={g:GH[g]*H[g] for g in GH};dhigh={g:GH[g]*DH[g] for g in GH}
 image=list(pure);jw=[up(farjac[i]*w[640]) for i in range(641)]
 for k in range(213):
  image[k]=up(low[k,0]+farjac[k]*r[640]);jw[k]=up(jw[k]+dlow[k,0])
  for g,off in [('near',213),('rest',426)]:image[off+k]=up(image[off+k]+farimage[off+k]+high[g][k,0]);jw[off+k]=up(jw[off+k]+dhigh[g][k,0])
 image[639]=up(image[639]+farimage[639]+GI*sum((H['infinite'][n,0] for n in range(213)),arb(0)))
 jw[639]=up(jw[639]+GI*sum((DH['infinite'][n,0] for n in range(213)),arb(0)))
 image[640]=up(image[640]+fars+farjac[640]*r[640]);jw[640]=up(jw[640]+dfar)
 ir=[];jr=[]
 for i in range(641):
  gate('every_complete_image_strictly_inside',image[i]<r[i]);gate('every_complete_direction_strictly_contracting',jw[i]<w[i])
  gate('every_saved_full_vector_finite_positive',all(z.is_finite() and z>0 for z in (r[i],w[i],image[i],jw[i])))
  ir.append(up(image[i]/r[i]));jr.append(up(jw[i]/w[i]))
 newfar=up(ab(modal['far_domain']['finite46_auxiliary_far_bound_in_new_width'])+Z0*r[640]);oldfar=up(arb(2)**-2224+dow['low']*Z0*r[640])
 gate('new_complete_far_graph_domain',newfar<Zdom and Zdom<=arb(2)**-1948)
 gate('same_original_far_graph_after_restriction',oldfar<Z0)
 # A fresh, explicitly enlarged OLD-width comparison ball identifies the
 # field. It contains both the lowered new ball and the original R100 box.
 # This does not alter the old rho gate, which is reported diagnostically.
 cw=[ab(F.from_float(z)) for z in can['comparison_candidate_distance_weight']]
 if len(cw)!=641 or not all(z.is_finite() and z>0 for z in cw):raise ArithmeticError('Positive old-width comparison proposal')
 drops=[dow['low']]*213+[dow['near']]*213+[dow['rest']]*213+[dow['infinite'],dow['low']]
 cr=[up(max(drops[i]*r[i],1048832*W0[i])) for i in range(641)]
 for i in range(641):
  gate('comparison_contains_lowered_new_ball',cr[i]>=drops[i]*r[i])
  gate('comparison_contains_original_R100_certified_box',cr[i]>=1048832*W0[i])
 cC=[ab(row['Cs_common_cap']) for row in parent['rows']];cL=[ab(row['Lambda_common_cap_on_domain']) for row in parent['rows']];cB=[ab(row['Cs_plus_Lambda_common_cap']) for row in parent['rows']]
 cDL=arb_mat(213,1);cDH={g:arb_mat(213,1) for g in H};comparison_rows=[];comparison_physmax=arb(0)
 for n in range(213):
  t=up(cr[n]+cr[213+n]+cr[426+n]+cr[639]);var=up(cL[n]+t);dw=up(cw[n]+cw[213+n]+cw[426+n]+cw[639])
  cDL[n,0]=up((arb(23)/9)*cC[n]*(cw[n]+cw[213+n])+(arb(23)/9)*var*dw+270*aa[n]*(cC[n]*cC[n]+3*cC[n]*var+arb(3)*var*var/2)*dw)
  rem=up((arb(23)/9)*t*dw+270*aa[n]*(cB[n]*cB[n]+3*cB[n]*t+arb(3)*t*t/2)*dw)
  ca={'near':cw[n]+cw[213+n]+cw[426+n],'rest':cw[213+n]+cw[426+n]+cw[639],'infinite':cw[426+n]+cw[639]}
  for g in cDH:cDH[g][n,0]=up((arb(23)/9)*cB[n]*ca[g]+rem)
  phys=up(aa[n]*max(cC[n]+var,cB[n]+t));comparison_physmax=max(comparison_physmax,phys)
  gate('comparison_full_mean_inverse_Hessian_domain',phys<arb(1)/128)
  comparison_rows.append(dict(cell=n+12,error_total=pack(t),physical_whole_ball=pack(phys),low_directional_source=pack(cDL[n,0]),high_directional_source={g:pack(cDH[g][n,0]) for g in cDH}))
 clow=GL*cDL;cfar=(GF*cDL)[0,0];chigh={g:GH[g]*cDH[g] for g in GH}
 cj=[up(farjac[i]/ratio*cw[640]) for i in range(641)]
 for k in range(213):
  cj[k]=up(cj[k]+clow[k,0])
  for g,off in [('near',213),('rest',426)]:cj[off+k]=up(cj[off+k]+chigh[g][k,0])
 cj[639]=up(cj[639]+GI*sum((cDH['infinite'][n,0] for n in range(213)),arb(0)));cj[640]=up(cj[640]+cfar)
 cjr=[]
 for i in range(641):
  gate('comparison_every_complete_direction_contracting',cj[i]<cw[i]);gate('comparison_every_saved_entry_finite_positive',all(z.is_finite() and z>0 for z in (cr[i],cw[i],cj[i])))
  cjr.append(up(cj[i]/cw[i]))
 comparison_far=up(arb(2)**-2224+Z0*cr[640]);gate('comparison_same_complete_far_graph_domain',comparison_far<Z0)
 gate('owned_96MiB_limit',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=args.rss_kib)
 required={k:v for k,v in gates.items() if not k.startswith('comparison_') and k!='same_original_far_graph_after_restriction'}
 existence=all(required.values());identification=existence and all(gates.values())
 result=dict(schema='new-uniformly-shifted-complete641-fixedpoint-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),precision_bits=256,
  all_gates=all(gates.values()),gates=gates,gate_count=sum(counts.values()),gate_categories=counts,input_identities=ids,domain=modal['domain'],angular_weight_translation=modal['angular_weight_translation'],
  new_complete_fixedpoint_proved=existence,same_original_full_field_identified=identification,old_infinite_caps_reweighted=False,full_source_mean_inverse_far_retained=True,
  rows=rows,candidate_radius=arr(r),candidate_distance_weight=arr(w),complete_image=arr(image),complete_directional_derivative=arr(jw),image_ratios=arr(ir),derivative_ratios=arr(jr),
  pure_reference_image=arr(pure),new_far_absolute_high_image=arr(farimage),far_derivative_column=arr(farjac),
  maxima=dict(image_ratio=pack(max(ir)),image_row=max(range(641),key=lambda i:ex(pack(ir[i]))),derivative_ratio=pack(max(jr)),derivative_row=max(range(641),key=lambda i:ex(pack(jr[i]))),physical_whole_ball=pack(maxphysical),lowered_original_work_radius=pack(maxold),comparison_derivative_ratio=pack(max(cjr)),comparison_physical_domain=pack(comparison_physmax)),
  original_rho_diagnostic=dict(threshold='2^-30',lowered_new_ball_passes=bool(maxold<arb(2)**-30),not_used_to_identify_when_false=True),
  comparison=dict(rows=comparison_rows,radius=arr(cr),distance_weight=arr(cw),directional_derivative=arr(cj),derivative_ratios=arr(cjr),far_argument=pack(comparison_far),
    purpose='A separately paid complete R116/R43 old-width Lipschitz domain containing both known solutions; no self-map claim is needed here.'),
  far=dict(original_scale=pack(Z0),new_graph_domain=pack(Zdom),whole_new_graph_argument=pack(newfar),whole_lowered_original_argument=pack(oldfar),raw_quadratic_constant='2^1967'),
  constants=dict(Q='23/18',DQ='23/9',D2T='270 R',S='257/256',old_work_radius='2^-30',old_uniform_contraction='33159425/33554432'),
  map_definition='R45 exact Cs+Lambda+e map, low/far N(Cs+Lambda+e)-N(Cs), high N(Cs+Lambda+e), independent far increment; new-strip positive kernels unchanged by simultaneous translation',
  derivative_definition='Full exact quadratic supports for centre times unknown; all new quadratic and complete T paid. The complete far D vanishes to second order at zero and is bounded using its true enlarged graph radius.',
  identification='Lower every frequency block by its true support minimum. A fresh old-width convex box contains that whole ball and the original1048832W R100 box. Complete R116/R43 derivative, mean/inverse and far gates on that comparison box prove equality, without pretending it is the original rho work domain.',
  scope='Inner cells12..224 and same R18 full infinite tail only. No new outer continuation, angular width at node10, or closed surface claimed.',
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 raw=(json.dumps(result,separators=(',',':'))+'\n').encode()
 if len(raw)>=4_900_000:raise MemoryError('Compact complete certificate budget')
 out.write_bytes(gzip.compress(raw,mtime=0));print(json.dumps(dict(path=str(out),sha256=sha(out),bytes=out.stat().st_size,all_gates=result['all_gates'],new_fixedpoint=existence,same_field=identification,gate_count=result['gate_count'],max_image=str(max(ir)),max_derivative=str(max(jr)),max_old_work=str(maxold),comparison_derivative=str(max(cjr)),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
 if not result['all_gates']:raise SystemExit(1)
if __name__=='__main__':main()
