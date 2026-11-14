#!/usr/bin/env python3
"""Actual same P1+.4 field: 46 near singletons plus seven rest windows.

Finite posterior only. Full low46, Q(error), complete T/mean/inverse,
full infinite input/output and genuine far graph budgets all remain.
The original eleven Green matrices are restricted to smaller windows.
New source kernels are stored as rigorously upward binary64 pairs to
avoid millions of resident Arb objects; arithmetic itself remains256bit.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from array import array
from fractions import Fraction as F
import gc,gzip,hashlib,importlib.util,json,resource,time
from pathlib import Path
from flint import arb,arb_mat,ctx

WINDOWS=[[m,m] for m in range(94,185,2)]+[[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
PARENT_WINDOWS=[[94,94],[96,96],[98,104],[106,112],[114,128],[130,184],[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
REGIONS=[list(range(46)),list(range(46,53))]
PMAP=[next(i for i,(l,h) in enumerate(PARENT_WINDOWS) if l<=lo<=hi<=h) for lo,hi in WINDOWS]
CHILDREN=[[w for w,p in enumerate(PMAP) if p==g] for g in range(13)]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p)
 with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)
def dyadkey(v):
 m,e=int(v[0]),int(v[1]);b=m.bit_length()
 return (e+b,m<<(256-b)) if m else (-10**15,0)
def bin64(v):
 m,e=int(v[0]),int(v[1])
 if m<0:raise ArithmeticError('negative comparison coefficient')
 if not m:return 0,0
 shift=max(0,m.bit_length()-63);u=(m+(1<<shift)-1)>>shift
 if not 0<u<2**64 or (u<<shift)<m:raise ArithmeticError('exact outward binary64 save')
 return u,e+shift
def bkey(m,e):
 b=m.bit_length();return (e+b,m<<(64-b)) if m else (-10**15,0)
def save(p,d):
 if p.exists():raise FileExistsError(p)
 b=gzip.compress((json.dumps(d,separators=(',',':'))+'\n').encode(),mtime=0)
 if len(b)>=5000000:raise ArithmeticError('strict output size')
 p.write_bytes(b);return dict(path=str(p),sha256=sha(p),bytes=len(b))

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input-json',type=Path,required=True);ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--steps',type=int,default=32);a=ap.parse_args()
 if not 1<=a.steps<=128:raise ValueError('finite declared substitutions')
 out=Path(str(a.out_prefix)+'.json.gz')
 if out.exists():raise FileExistsError('fresh posterior output')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();cfg=read(a.input_json);ids=cfg['inputs'];paths={k:Path(v['path']) for k,v in ids.items()};gates={};counts={}
 def gate(k,b,n=1):
  if not b:raise ArithmeticError(k)
  gates[k]=True;counts[k]=counts.get(k,0)+n
 def rss():gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 for k,p in paths.items():gate('pin_'+k,sha(p)==ids[k]['sha256'])
 spec=importlib.util.spec_from_file_location('fine53_saved_utility',paths['utility']);util=importlib.util.module_from_spec(spec);spec.loader.exec_module(util)
 ab,ex,pack,up,support=util.ab,util.ex,util.pack,util.up,util.support
 for k in paths:
  if k.endswith('_resource'):gate('owned0_'+k,util.completed(read(paths[k])))
 parent,modal,source,density,dq=(read(paths[k]) for k in ('parent','modal','source','density','dq'))
 for k,d in zip(('parent','modal','source','density','dq'),(parent,modal,source,density,dq)):gate('all_original_'+k,all(d['gates'].values()) and d.get('all_gates',True))
 domain=parent['domain'];gate('same_complex_P1_and_shift',domain==modal['domain']==source['domain']==dq['domain'] and domain['name']=='R156_actual_full_cut_posterior' and ex(parent['angular_weight_translation'])==ex(modal['angular_weight_translation'])==ex(dq['angular_weight_translation'])==F(2,5))
 gate('same_proved_shift040_parent',parent['schema']=='same-P1-complete-shift040-window13-finite-posterior-v1' and parent['complete_mean_inverse_far'] and parent['old_infinite_reweighted'] is False and parent['input_identities']['modal']['sha256']==ids['modal']['sha256'] and parent['input_identities']['source']['sha256']==ids['source']['sha256'])
 gate('same_complete_source_density',source['all213_original_cells'] and [v for k,v in source['input_hashes'].items() if Path(k).name==paths['density'].name]==[ids['density']['sha256']] and [v for k,v in source['input_hashes'].items() if Path(k).name==paths['modal'].name]==[ids['modal']['sha256']] and modal['input_identities']['density']['sha256']==ids['density']['sha256'])
 gate('true53_fine_partition',dq['schema']=='inner-P1-shift040-fine53-DQ-two-material-chunks-v1' and dq['windows_out']==WINDOWS and dq['windows_in']==[[2,92]]+WINDOWS+[[8192,None]] and dq['input_identities']['modal']['sha256']==ids['modal']['sha256'] and parent['windows']==PARENT_WINDOWS and sum((list(range(lo,hi+1,2)) for lo,hi in WINDOWS),[])==list(range(94,8191,2)))
 aa=[up(arb(257)/256*ab(r['V_over_w_upper'])) for r in density['rows']]
 C=[ab(r['Cs_plus_Lambda_common_cap']) for r in modal['rows']]
 low=[ab(r['fixed_low_cap']) for r in parent['rows']];low_modes=[[ab(z) for z in r['low_mode_caps']] for r in parent['rows']]
 caps=[[ab(r['window_caps'][PMAP[w]]) for w in range(53)] for r in parent['rows']]
 parent_caps=[[ab(z) for z in r['window_caps']] for r in parent['rows']]
 region_caps=[[ab(z) for z in r['near_rest_common_caps']] for r in parent['rows']]
 gate('whole213_original_rows',len(caps)==len(C)==len(aa)==213 and [r['cell'] for r in parent['rows']]==list(range(12,225)) and all(len(x)==46 for x in low_modes))
 infinite=ab(parent['complete_infinite_cap']);far=ab(parent['fixed_far_cap'])
 far_source=[[ab(z) for z in row] for row in parent['complete_far_source_by_cell']];infinite_far=ab(parent['complete_infinite_far_source'])
 GI=up(arb(257)/256*ab(density['gamma_high']))
 eps=ab(parent['point_physical_epsilon_prime']);old_head=list(map(ab,parent['translated_head_window_masses']));old_band=list(map(ab,parent['translated_head_band_masses']));old_original=list(map(ab,parent['actual_R100_head_band_masses']))
 known34816=ab(parent['complete_tail34816_at040']);head_strip=parent['head_strip'];head_strip_original=parent['head_strip_original'];units=parent['same_original617_units']
 initial_rows=[dict(cell=n+12,parent_window_caps=list(map(pack,parent_caps[n])),near_rest_common_caps=list(map(pack,region_caps[n])),fixed_low_cap=pack(low[n])) for n in range(213)]
 del parent,density;gc.collect();rss()
 # Compact source kernels: one common s coefficient majorizes ell
 # coefficientwise before the sum. Merely comparing two norms would not suffice.
 K=213*53*55;L=213*46*46
 km=array('Q',[0])*K;ke=array('q',[0])*K;lm=array('Q',[0])*L;le=array('q',[0])*L
 near_order=array('B');rest_order=array('B');low_order=array('B')
 chunk_pins=[]
 for n,rec in enumerate(dq['chunk_records']):
  path=Path(rec['path']);gate('actual_DQ_chunk_pin',rec['cell']==n+12 and sha(path)==rec['sha256']);r=read(path);chunk_pins.append(rec)
  gate('same_DQ_centre_and_cell',r['cell']==n+12 and dyadkey(r['reference_common_cap'])==dyadkey(pack(C[n])) and r['B_floor']>=120)
  # For k,n>=2:5*k*n/4>=max(1,5*n/(4*B)), so the same s
  # Fourier majorant dominates each ell Fourier coefficient pointwise.
  for w in range(53):
   row=r['kernels_s_upper'][w];other=r['kernels_ell_upper'][w]
   gate('every55_DQ_shape',len(row)==len(other)==55)
   base=(n*53+w)*55
   for j,(v,z) in enumerate(zip(row,other)):
    gate('source_material_coefficient_domination',dyadkey(v)>=dyadkey(z));m,e=bin64(v);km[base+j]=m;ke[base+j]=e
   near_order.extend(sorted(range(46),key=lambda j:bkey(km[base+1+j],ke[base+1+j]),reverse=True))
   rest_order.extend(sorted(range(7),key=lambda j:bkey(km[base+47+j],ke[base+47+j]),reverse=True))
   x=r['low_singleton_kernels_s_upper'][w];y=r['low_singleton_kernels_ell_upper'][w]
   gate('every46_low_shape',len(x)==len(y)==46)
   if w>=46:gate('no_low_quadratic_support_above184',all(int(v[0])==int(z[0])==0 for v,z in zip(x,y)),46)
   else:
    base0=(n*46+w)*46
    for j,(v,z) in enumerate(zip(x,y)):
     gate('low_material_coefficient_domination',dyadkey(v)>=dyadkey(z));m,e=bin64(v);lm[base0+j]=m;le[base0+j]=e
    low_order.extend(sorted(range(46),key=lambda j:bkey(lm[base0+j],le[base0+j]),reverse=True))
  if n%48==0:print(json.dumps(dict(event='packed_fine53_DQ',cell=n+12,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
  rss()
 gate('all213_full_source_kernels',len(chunk_pins)==213)
 del r,dq,modal;gc.collect();rss()
 poly=[[arb(0)]*53 for n in range(213)];tails=[];bandref=[]
 for n,r in enumerate(source['rows']):
  gate('actual_complete_reference_cell',r['cell']==n+12);q=r['source_common_mass']['common_d'];tails.append(ab(q['shared_complete_inverse_tail']));bandref.append([ab(q[k]) for k in ('near94to184','rest186to8190')])
 source_parts=[];seen=0;winof={m:w for w,(lo,hi) in enumerate(WINDOWS) for m in range(lo,hi+1,2)}
 for rec in source['source_parts']:
  path=paths['source'].parent/Path(rec['path']).name;gate('full_source_part_pin',sha(path)==rec['sha256']);source_parts.append(dict(path=str(path),sha256=rec['sha256']))
  with gzip.open(path,'rt') as stream:
   for line in stream:
    r=json.loads(line);n=r['cell']-12;gate('full_reference_poly_and_inverse',n==seen and r['complete_mean_and_inverse_retained'] and r['polynomial_support_max736'] and [q['mode'] for q in r['high_polynomial_pair_rows']]==list(range(94,737,2)));seen+=1
    for q in r['high_polynomial_pair_rows']:poly[n][winof[q['mode']]]+=ab(q['common_d'])
    poly[n]=list(map(up,poly[n]))
 gate('complete213_reference_source',seen==213)
 qref=[[min(up(poly[n][w]+tails[n]),bandref[n][int(w>=46)]) for w in range(53)] for n in range(213)]
 infinite_ref=[ab(r['source_common_mass']['common_d']['infinite8192up']) for r in source['rows']]
 del source,poly,tails,bandref,r;gc.collect();rss()
 gamma=read(paths['gamma']);gate('same_eleven_Green_matrices',gamma['schema']=='original-inner-eleven-window-Gamma-replay-v1' and gamma['original_maximum_bitwise_identity'] and gamma['original_complete_far_and_pure_identity'] and gamma['Vprime_scale']==[257,256] and gamma['new_ODE_integrations']==0)
 gamma_arrays=[];gamma_groups=[];gamma_pins=[]
 for ix,rec in enumerate(gamma['files']):
  path=paths['gamma'].parent/rec['path'];gate('gamma_pin',rec['index']==ix and sha(path)==rec['sha256']);gamma_pins.append(dict(path=str(path),sha256=rec['sha256']))
  mm=array('Q',[0])*22791;ee=array('q',[0])*22791;visited=bytearray(22791)
  data=read(path)
  for k,n,m,e in data['entries']:
   k-=12;n-=12;gate('causal_full_Green_vertex',0<=k<=n<213);index=k*213-k*(k+1)//2+n;gate('unique_Green_vertex',not visited[index]);visited[index]=1;m,e=bin64([m,e]);mm[index]=m;ee[index]=e
  gate('complete_causal_Green_triangle',sum(visited)==22791);gamma_arrays.append((mm,ee));gamma_groups.append([w for w,(lo,hi) in enumerate(WINDOWS) if rec['first_mode']<=lo<=hi<=rec['last_mode']])
  del data;gc.collect();rss()
 gate('every_fine_window_has_one_Green',sorted(sum(gamma_groups,[]))==list(range(53)))
 del gamma;gc.collect();rss()
 def groupcaps(n):return [min(parent_caps[n][g],up(sum((caps[n][w] for w in CHILDREN[g]),arb(0)))) for g in range(13)]
 def common(n,gc0=None):
  gc0=groupcaps(n) if gc0 is None else gc0
  return [min(region_caps[n][0],up(sum(gc0[:6],arb(0)))),min(region_caps[n][1],up(sum(gc0[6:],arb(0))))]
 def nested(weights,n,region,gc0,cm,permutation):
  ix=REGIONS[region];rem=cm[region];remaining=gc0[:];ans=arb(0)
  for p in permutation:
   if rem==0:break
   if weights[p]==0:continue
   w=ix[p];g=PMAP[w];take=min(rem,caps[n][w],remaining[g]);ans+=weights[p]*take
   rem=up(max(arb(0),(rem-take).upper()));remaining[g]=up(max(arb(0),(remaining[g]-take).upper()))
  return min(up(ans),up(max(weights)*cm[region]),up(sum((weights[p]*caps[n][w] for p,w in enumerate(ix)),arb(0))))
 def source_row(n):
  gc0=groupcaps(n);cm=common(n,gc0);t=up(low[n]+cm[0]+cm[1]+infinite);cc=C[n]
  gate('complete_physical_mean_inverse_domain',aa[n]*(cc+t)<arb(1)/128)
  sq=up(arb(23)/18*t*t);rem=up(270*aa[n]*(cc+t)*(cc*t+t*t/2));dqs=[]
  for w in range(53):
   base=(n*53+w)*55;weights=[arb(km[base+j])*arb(2)**ke[base+j] for j in range(55)]
   if w<46:
    base0=(n*46+w)*46;lw=[arb(lm[base0+j])*arb(2)**le[base0+j] for j in range(46)]
    lc=min(up(weights[0]*low[n]),support(lw,low_modes[n],low[n],low_order[base0:base0+46]))
   else:lc=arb(0)
   bo=(n*53+w)*46;bro=(n*53+w)*7
   dqs.append(up(lc+weights[54]*infinite+nested(weights[1:47],n,0,gc0,cm,near_order[bo:bo+46])+nested(weights[47:54],n,1,gc0,cm,rest_order[bro:bro+7])))
  def sqproject(lower):
   # Equality stays in the high group; no support at l/2 is discarded.
   GL=min(low[n],up(sum((z for m,z in zip(range(2,93,2),low_modes[n]) if 2*m>=lower),arb(0))))
   G=GL
   for region in range(2):
    portion=arb(0)
    for g in (range(6) if region==0 else range(6,13)):
     portion+=min(gc0[g],up(sum((caps[n][w] for w in CHILDREN[g] if 2*WINDOWS[w][1]>=lower),arb(0))))
    G+=min(cm[region],up(portion))
   G=min(t,up(G+infinite));return min(sq,up(arb(23)/9*t*G))
  return gc0,cm,t,sq,rem,dqs,[sqproject(lo) for lo,hi in WINDOWS],sqproject(8192)
 checkpoints=[];infinite_steps=[]
 def checkpoint(step):
  cm=common(0);head=[min(up(cm[g]*eps),old_band[g]) for g in range(2)]+[min(up(infinite*eps),old_band[2])]
  cp=dict(step=step,cell12_windows=list(map(pack,caps[0])),cell13_windows=list(map(pack,caps[1])),cell12_common=list(map(pack,cm)),complete_infinite_cap=pack(infinite),wholecell_head=list(map(pack,head)));checkpoints.append(cp)
  print(json.dumps(dict(event='actual_fine53_posterior',step=step,head=[str(x) for x in head],point94=str(up(caps[0][0]*eps)),point184=str(up(caps[0][45]*eps)),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
 checkpoint(0)
 for step in range(1,a.steps+1):
  src=arb_mat(213,53);isrc=[]
  for n in range(213):
   gc0,cm,t,sq,rem,dq,squares,isq=source_row(n)
   for w in range(53):src[n,w]=up(qref[n][w]+dq[w]+squares[w]+rem)
   di=up(arb(23)/9*C[n]*(caps[n][-1]+infinite));isrc.append(up(infinite_ref[n]+di+isq+rem))
  images=arb_mat(213,53)
  for (mm,ee),ws in zip(gamma_arrays,gamma_groups):
   green=arb_mat(213,213);index=0
   for k in range(213):
    for n in range(k,213):green[k,n]=arb(mm[index])*arb(2)**ee[index];index+=1
   selected=arb_mat([[src[n,w] for w in ws] for n in range(213)]);product=green*selected
   for j,w in enumerate(ws):
    for n in range(213):images[n,w]=product[n,j]
   del green,selected,product
  nxt=[]
  for n in range(213):
   row=[]
   for w in range(53):
    v=min(caps[n][w],up(images[n,w]+far_source[n][int(w>=46)]));gate('every_actual_window_monotone',v.is_finite() and 0<v<=caps[n][w]);row.append(v)
   nxt.append(row)
  iv=up(GI*sum(isrc,arb(0))+infinite_far);newi=min(infinite,iv);gate('complete_infinite_monotone',newi.is_finite() and 0<newi<=infinite)
  infinite_steps.append(dict(step=step,before=pack(infinite),full_image=pack(iv),after=pack(newi)));caps=nxt;infinite=newi
  if step&(step-1)==0 or step==a.steps:checkpoint(step)
  del src,images;gc.collect();rss()
 headwin=[];headrows=[]
 for w,window in enumerate(WINDOWS):
  whole=up(caps[0][w]*eps);coarse=old_head[PMAP[w]];chosen=min(whole,coarse,old_band[int(w>=46)])
  headwin.append(chosen);headrows.append(dict(window=window,parent_window=PARENT_WINDOWS[PMAP[w]],wholecell=pack(whole),previous_point_parent=pack(coarse),actual_translated_head=pack(chosen)))
 cm=common(0);head=[]
 for region in range(2):head.append(min(up(cm[region]*eps),up(sum((headwin[w] for w in REGIONS[region]),arb(0))),old_band[region]))
 head.append(min(up(infinite*eps),old_band[2]));original=[min(up(head[g]*(-arb(2)*m/5).exp()),old_original[g]) for g,m in enumerate((94,186,8192))]
 rows=[]
 for n in range(213):
  gc0,cm,t,sq,rem,dq,squares,isq=source_row(n)
  rows.append(dict(cell=n+12,window_caps=list(map(pack,caps[n])),retained_parent13_mass_caps=list(map(pack,gc0)),near_rest_common_caps=list(map(pack,cm)),fixed_low_cap=pack(low[n]),low_mode_caps=list(map(pack,low_modes[n])),complete_infinite_cap=pack(infinite),total_error=pack(t),full_quadratic_source=pack(sq),full_quadratic_window_sources=list(map(pack,squares)),full_quadratic_infinite_source=pack(isq),full_mean_inverse_difference_source=pack(rem),DQ_common_source=list(map(pack,dq))))
 result=dict(schema='same-P1-complete-shift040-fine53-finite-posterior-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=all(gates.values()),gates=gates,gate_categories=counts,gate_count=sum(counts.values()),source_sha256=sha(__file__),input_config_sha256=sha(a.input_json),input_identities=ids,domain=domain,angular_weight_translation=dict(numerator='2',denominator='5'),windows=WINDOWS,parent_windows=PARENT_WINDOWS,parent_window_of_fine=PMAP,steps=a.steps,rows=rows,initial_parent_constraints=initial_rows,checkpoints=checkpoints,infinite_steps=infinite_steps,complete_infinite_cap=pack(infinite),fixed_far_cap=pack(far),complete_far_source_by_cell=[[pack(z) for z in r] for r in far_source],complete_infinite_far_source=pack(infinite_far),source_parts=source_parts,DQ_chunks=chunk_pins,Green_chunks=gamma_pins,head_strip=head_strip,head_strip_original=head_strip_original,head_bands=[[94,184],[186,8190],[8192,None]],translated_head_band_masses=list(map(pack,head)),translated_head_window_masses=list(map(pack,headwin)),actual_R100_head_band_masses=list(map(pack,original)),head_window_readout=headrows,point_physical_epsilon_prime=pack(eps),same_original617_units=units,complete_tail34816_at040=pack(min(known34816,up(infinite*eps))),parent_full_infinite_mass_at040=pack(head[2]),complete_mean_inverse_far=True,only_same_existing_complex_P1_field=True,all_parent13_and_near_rest_mass_constraints_retained=True,low_quadratic_tail_uses_all46_separate_modes=True,old_infinite_reweighted=False,new_fixedpoint_claimed=False,no_new_ODE_or_integral=True,coefficient_storage='All160bit upper coefficients were exactly rounded upward to at most64bit mantissas; full arithmetic remains256bit. The same pointwise s-majorant dominates ell before the Green common-material map.',source_tail_accounting='Full positive inverse/Q/T budgets remain in every individual output bound. Shared parent13 and near/rest masses are retained; no repeated shared tail is treated as free.',precision_bits=256,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 rec=save(out,result);rss();print(json.dumps(dict(all_gates=True,primary=rec,gate_count=result['gate_count'],head=[str(z) for z in head],point184=str(headwin[45]),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
