#!/usr/bin/env python3
"""Outward conditional nonlow certificate with actual LF and far fixed.

Source stage writes actual small owned cell batches. Assemble stage pays all
original Green triangles, far forcing,11290 strict image and Jw gates.
This is not yet the independent lower-width same-field comparison.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json,time,resource,gc,sys
from flint import arb,arb_mat,ctx
B=Path('/workspace/scratch/d1aa462cfc02');E=B/'exact-work';TOP=B/'math-research/topics/visible-flex-larger-amplitude'
PINS={
 'LF':(E/'inner-actual-LF-shift060-r1.json.gz','ff1df29ff5f24ffd6ed13dbc80c9f4a96d0e3084bacf03ebce41343d2d0ac811'),
 'LF_resource':(E/'inner-actual-LF-shift060-run1-resource.json','b9e95c4eb67cb109e50fc3b3b63be5b12871dfcff7f50ecacf31dde2e7b8ad83'),
 'source':(E/'inner-actual-LF-shift060-source-r1-summary.json','9f9ba881882e14f633a59fbd1111c7fd0ade9657fee36822f14ad8c495052b38'),
 'source_resource':(E/'inner-actual-LF-shift060-source-run1-resource.json','5a90ea604796167d473b2d2af72432f9f7bbfdb72150986fd859b89c4572da7e'),
 'DQ':(E/'inner-actual-LF-shift060-DQ-r1/certificate.json.gz','f652efba56708c9b0efe0230a52838abe106967266273a48740c2f09ccbdad18'),
 'DQ_resource':(E/'inner-actual-LF-shift060-DQ-run1-resource.json','92d1b56ee090dd3709ba2b427963fac0fd801faf0d0d40dd9bd446585d0565c1'),
 'recon':(E/'inner-actual-LF-shift060-conditional-recon-r1.json.gz','4fd35e00520ebf07713593c5249f7dae26756e71606ea70c19f4a298f5b18772'),
 'recon_resource':(E/'inner-actual-LF-shift060-conditional-recon-run1-resource.json','7f5f80b9714b303f0df7c2b7564ad8b349c17b77e4b3baf58d3a78756500c0af'),
 'density':(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'split':(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz','b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd'),
 'Gamma':(B/'geometry-work/inner-window-gamma-r1/output/certificate.json','3033c330ed219a1e87420818df8dd3d7bca44c246afe4f661d68870a783847b1'),
}
WIN=[[m,m] for m in range(94,185,2)]+[[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ab(v):
 if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
 if 'upper' in v:return ab(v['upper'])
 if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
 return arb(int(v['numerator']))/int(v['denominator'])
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 return F(int(v['numerator']),int(v['denominator']))
def pack(v,bits=160):
 if not v.is_finite():raise ArithmeticError('finite positive outward value')
 t=v.upper()
 if t<0:raise ArithmeticError('nonnegative source')
 if t==0:return ['0',0]
 m,e=t.man_exp();m,e=int(m),int(e);s=max(0,m.bit_length()-bits)
 if s:m,e=(m+(1<<s)-1)>>s,e+s
 if not arb(m)*arb(2)**e>=t:raise ArithmeticError('outward storage')
 return [str(m),e]
def up(v):return ab(pack(v))
def posfloat(x):
 f=F.from_float(x)*F(1048577,1048576)
 if f<=0:raise ArithmeticError('strictly positive proposed radius/weight')
 return up(arb(f.numerator)/f.denominator)
def save(p,d):
 if p.exists():raise FileExistsError('Immutable fresh actual output')
 b=gzip.compress((json.dumps(d,separators=(',',':'))+'\n').encode(),mtime=0)
 if len(b)>=5000000:raise ArithmeticError('split actual packet')
 p.write_bytes(b);return dict(path=str(p),sha256=sha(p),bytes=len(b))
def formal(d):return d['exitcode']==0 and d['termination_signal'] is None and d['peak_rss_kib']<98304 and d['resource_wrapper_sha256']=='bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--stage',choices=['sources','assemble'],required=True);ap.add_argument('--first-cell',type=int);ap.add_argument('--last-cell',type=int);ap.add_argument('--batch-manifest',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 if a.out.exists():raise FileExistsError('fresh actual proof')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();g={};counts={}
 def gate(k,v):
  if not v:raise ArithmeticError(k)
  g[k]=True;counts[k]=counts.get(k,0)+1
 def rss():gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 for k,(p,s) in PINS.items():gate('pin_'+k,sha(p)==s)
 for k in ('LF','source','DQ','recon'):gate('owned_actual_'+k,formal(read(PINS[k+'_resource'][0])))
 lf,src,dq,rec=(read(PINS[k][0]) for k in ('LF','source','DQ','recon'))
 gate('actual_full_low_identity',lf['finite_LF_is_actual_projection_of_same_existing_field'] and lf['no_unknown_infinite_reweight'] and all(x['all_gates'] for x in (lf,src,dq)) and lf['cells']==list(range(12,225)) and lf['modes']==list(range(2,93,2)))
 gate('same_input_source_DQ',dq['input_identities']['modal']['sha256']==PINS['LF'][1] and src['input_hashes'][str(PINS['LF'][0])]==PINS['LF'][1] and dq['windows_out']==WIN and dq['windows_in']==[[2,92]]+WIN+[[8192,None]])
 gate('source_mean_full_inverse',src['gates']['complete_mean_inverse_zero_mode_and_positive_tail'] and src['all213_original_cells'] and ex(lf['angular_weight_translation'])==F(3,5))
 gate('only_proposed_floats_imported',not rec['certified'] and not rec['new_fixedpoint_claimed'] and rec['candidate_found'] and len(rec['candidate_radius'])==len(rec['candidate_distance'])==11290 and rec['input_identities']['LF']['sha256']==PINS['LF'][1])
 rr=list(map(posfloat,rec['candidate_radius']));ww=list(map(posfloat,rec['candidate_distance']));R=[rr[n*53:(n+1)*53] for n in range(213)];W=[ww[n*53:(n+1)*53] for n in range(213)];h,dh=rr[-1],ww[-1];del rec,rr,ww;gc.collect();rss()
 C=[ab(r['finite_LF_common_cap']) for r in lf['rows']];aa=[ab(r['physical_Amax']) for r in lf['rows']];tau=[ab(r['translated_tau_outer_lower']) for r in lf['rows']]
 qref=[[arb(0) for w in WIN] for n in range(213)];tail=[ab(r['source_common_mass']['common_d']['shared_complete_inverse_tail']) for r in src['rows']];qhi=[ab(r['source_common_mass']['common_d']['infinite8192up']) for r in src['rows']]
 parts=[];seen=0;which={m:w for w,(lo,hi) in enumerate(WIN) for m in range(lo,hi+1,2)}
 for part in src['source_parts']:
  p=Path(part['path']);gate('complete_source_part_pin',sha(p)==part['sha256']);parts.append(part)
  with gzip.open(p,'rt') as stream:
   for line in stream:
    r=json.loads(line);n=r['cell']-12;gate('complete_source_cell',n==seen and r['complete_mean_and_inverse_retained'] and r['polynomial_support_max736']);seen+=1
    for pair in r['high_polynomial_pair_rows']:qref[n][which[pair['mode']]]+=ab(pair['common_d'])
 gate('complete_source_all213',seen==213)
 for n,row in enumerate(src['rows']):
  for w in range(53):qref[n][w]=min(up(qref[n][w]+tail[n]),ab(row['source_common_mass']['common_d']['near94to184' if w<46 else 'rest186to8190']))
 del src;gc.collect();rss()
 supports=[]
 for i,(il,ih) in enumerate(WIN):
  for j in range(i,53):
   jl,jh=WIN[j];sm=[w for w,(lo,hi) in enumerate(WIN) if max(il+jl,lo)<=min(ih+jh,hi)];df=[w for w,(lo,hi) in enumerate(WIN) if ((i<j and max(jl-ih,lo)<=min(jh-il,hi)) or (i==j and ih-il>=lo))];supports.append((i,j,sm,df,ih+jh>=8192))
 def quadratics(x,dx,t):
  sq=[arb(0) for _ in WIN];jsq=[arb(0) for _ in WIN];hi=arb(0);jhi=arb(0);decay=[up((-2*lo*t).exp()) for lo,_ in WIN];eh=up((-16384*t).exp())
  for i,j,sm,df,tohi in supports:
   xy=x[i]*x[j];dxy=dx[i]*x[j]+x[i]*dx[j];cs=arb(5)/(8 if i==j else 4);sv=cs*xy;sj=cs*dxy
   for w in sm:sq[w]+=sv;jsq[w]+=sj
   if df:
    dv=arb(5)/4*decay[i]*xy;dj=arb(5)/4*decay[i]*dxy
    for w in df:sq[w]+=dv;jsq[w]+=dj
   if tohi:hi+=sv;jhi+=sj
  for w,(lo,whi) in enumerate(WIN):
   for i,(il,ih) in enumerate(WIN):
    if ih>=8192-whi:
     de=up((-2*max(il,8192-whi)*t).exp());sq[w]+=arb(5)/4*de*x[i]*h;jsq[w]+=arb(5)/4*de*(dx[i]*h+x[i]*dh)
   sq[w]+=arb(5)/4*eh*h*h;jsq[w]+=arb(5)/2*eh*h*dh
  st=sum(x,arb(0));sdt=sum(dx,arb(0));hi+=arb(23)/9*st*h+arb(23)/18*h*h;jhi+=arb(23)/9*(sdt*h+st*dh+h*dh)
  return list(map(up,sq)),list(map(up,jsq)),up(hi),up(jhi)
 if a.stage=='sources':
  gate('declared_source_range',a.first_cell is not None and a.last_cell is not None and 12<=a.first_cell<=a.last_cell<=224)
  rows=[];chunks=[]
  for cell in range(a.first_cell,a.last_cell+1):
   n=cell-12;drec=dq['chunk_records'][n];p=Path(drec['path']);gate('DQ_chunk_pin',drec['cell']==cell and sha(p)==drec['sha256']);drow=read(p);chunks.append(drec)
   gate('DQ_actual_same_LF',drow['reference_common_cap']==lf['rows'][n]['finite_LF_common_cap'] and drow['reference_strong_pair_caps']==lf['rows'][n]['finite_LF_pair_caps'])
   km=arb_mat([[ab(v) for v in row[1:]] for row in drow['kernels_s_upper']]);v=arb_mat([[x,y] for x,y in zip(R[n]+[h],W[n]+[dh])]);prod=km*v
   for x,y in zip(drow['kernels_s_upper'],drow['kernels_ell_upper']):
    for a0,b0 in zip(x,y):gate('actual_s_coefficient_majorizes_ell',ex(a0)>=ex(b0))
   t=up(sum(R[n],arb(0))+h);dt=up(sum(W[n],arb(0))+dh);phys=up(aa[n]*(C[n]+t));gate('whole_ball_complete_mean_inverse_domain',phys<arb(1)/128)
   sq,jsq,isq,jisq=quadratics(R[n],W[n],tau[n]);rem=up(270*aa[n]*(C[n]+t)*(C[n]*t+t*t/2));jrem=up(270*aa[n]*(C[n]*C[n]+3*C[n]*t+arb(3)/2*t*t)*dt)
   lin=[up(prod[w,0]) for w in range(53)];jlin=[up(prod[w,1]) for w in range(53)]
   s=[up(qref[n][w]+lin[w]+sq[w]+rem) for w in range(53)];ds=[up(jlin[w]+jsq[w]+jrem) for w in range(53)]
   il=up(arb(23)/9*C[n]*(R[n][-1]+h));ijl=up(arb(23)/9*C[n]*(W[n][-1]+dh));isrc=up(qhi[n]+il+isq+rem);ijsrc=up(ijl+jisq+jrem)
   for x in s+ds+[isrc,ijsrc]:gate('every_source_entry_finite_nonnegative',x.is_finite() and x>=0)
   rows.append(dict(cell=cell,radius=list(map(pack,R[n])),distance=list(map(pack,W[n])),actual_LF_common=pack(C[n]),total_nonlow_radius=pack(t),whole_ball_physical=pack(phys),source=list(map(pack,s)),derivative_source=list(map(pack,ds)),infinite_source=pack(isrc),infinite_derivative_source=pack(ijsrc),constant_source=list(map(pack,qref[n])),DQ_source=list(map(pack,lin)),Q_source=list(map(pack,sq)),complete_T_source=pack(rem),DQ_direction=list(map(pack,jlin)),Q_direction=list(map(pack,jsq)),complete_T_direction=pack(jrem),infinite_parts=dict(constant=pack(qhi[n]),DQ=pack(il),Q=pack(isq),complete_T=pack(rem))))
   rss()
   if len(rows)%12==0 or cell==a.last_cell:print(json.dumps(dict(event='actual_conditional_source_cell',cell=cell,count=len(rows),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
  out=dict(schema='actual-LF-shift060-conditional-nonlow-source-batch-v1',stage='sources',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=all(g.values()),gates=g,gate_categories=counts,gate_count=sum(counts.values()),rows=rows,first_cell=a.first_cell,last_cell=a.last_cell,infinite_radius=pack(h),infinite_distance=pack(dh),window_partition=WIN,input_identities={k:dict(path=str(p),sha256=s) for k,(p,s) in PINS.items()},complete_source_parts=parts,DQ_chunks=chunks,actual_LF_and_far_fixed=True,new_existence_claimed=False,precision_bits=256,storage_bits=160,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 else:
  gate('source_batch_manifest_given',a.batch_manifest is not None);bm=read(a.batch_manifest);s=arb_mat(213,53);ds=arb_mat(213,53);ins=[];inds=[];physical=[];batch_records=[];expected=12
  for br in bm['batches']:
   pp=Path(br['path']);rp=Path(br['resource_path']);gate('batch_primary_resource_pins',sha(pp)==br['sha256'] and sha(rp)==br['resource_sha256']);bd=read(pp);ru=read(rp);gate('batch_same_math_and_actual0',bd['all_gates'] and all(bd['gates'].values()) and formal(ru) and bd['source_sha256']==sha(__file__) and bd['input_identities']=={k:dict(path=str(p),sha256=z) for k,(p,z) in PINS.items()} and bd['first_cell']==expected and str(pp) in ru['command']);batch_records.append(br)
   for row in bd['rows']:
    n=row['cell']-12;gate('ordered_complete_batch_cell',row['cell']==expected);expected+=1;gate('same_actual_radius_weight',row['radius']==list(map(pack,R[n])) and row['distance']==list(map(pack,W[n])) and bd['infinite_radius']==pack(h) and bd['infinite_distance']==pack(dh))
    for w in range(53):s[n,w]=ab(row['source'][w]);ds[n,w]=ab(row['derivative_source'][w])
    ins.append(ab(row['infinite_source']));inds.append(ab(row['infinite_derivative_source']));physical.append(ab(row['whole_ball_physical']))
   del bd;gc.collect();rss()
  gate('all213_source_rows',expected==225 and len(ins)==len(inds)==213)
  gamma=read(PINS['Gamma'][0]);gate('original_Green_identity',gamma['original_maximum_bitwise_identity'] and gamma['original_complete_far_and_pure_identity'] and gamma['new_ODE_integrations']==0 and gamma['Vprime_scale']==[257,256])
  image=arb_mat(213,53);jimage=arb_mat(213,53);covered=[];gpins=[]
  for ix,gr in enumerate(gamma['files']):
   p=PINS['Gamma'][0].parent/gr['path'];gate('Green_chunk_pin',sha(p)==gr['sha256']);gg=read(p);M=arb_mat(213,213);visited=set()
   for k,n,m,e in gg['entries']:
    gate('causal_Green_vertex',12<=k<=n<=224 and (k,n) not in visited);visited.add((k,n));M[k-12,n-12]=ab([m,e])
   gate('complete_Green_triangle',len(visited)==22791);ixs=[w for w,(lo,hi) in enumerate(WIN) if gr['first_mode']<=lo<=hi<=gr['last_mode']];covered+=ixs;ss=arb_mat([[s[n,w] for w in ixs]+[ds[n,w] for w in ixs] for n in range(213)]);pp=M*ss
   for j,w in enumerate(ixs):
    for n in range(213):image[n,w]=pp[n,j];jimage[n,w]=pp[n,len(ixs)+j]
   gpins.append(dict(path=str(p),sha256=gr['sha256']));del gg,M,ss,pp,visited;gc.collect();rss();print(json.dumps(dict(event='actual_conditional_Green_window',index=ix,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
  gate('all53_Green_windows',sorted(covered)==list(range(53)))
  sys.path.insert(0,str(TOP/'computations'))
  from closure_split_joint_io_v2 import metadata_without_array
  sp=metadata_without_array(PINS['split'][0],'gamma_rows');density=read(PINS['density'][0]);gi=up(arb(257)/256*ab(density['gamma_high']));z=ab(lf['fixed_far_parameter']['new_actual_upper']);zdom=ab(lf['fixed_far_parameter']['evaluation_graph_domain']);Z0=arb(2)**-2200;gate('actual_fixed_far_graph_domain',z<zdom/4 and 2*zdom<arb(2)**-1948 and lf['fixed_far_parameter']['finite46_only'] and lf['fixed_far_parameter']['unknown_graph_output_not_reweighted'])
  far_ratio=up((z/Z0)**2/(arb(257)/256));hm=up(gi*sum(ins,arb(0))+ab(sp['deep_high_boundary'])*far_ratio);hjm=up(gi*sum(inds,arb(0)));gate('complete_infinite_strict_selfmap',hm<h);gate('complete_infinite_strict_Jw_half',hjm<dh/2)
  rows=[];maxim=up(hm/h);maxjm=up(hjm/dh)
  for n,row in enumerate(sp['cells']):
   im=[];jm=[];far=[]
   for w in range(53):
    f=up(ab(row['far_boundary_near' if w<46 else 'far_boundary_rest'])*far_ratio);v=up(image[n,w]+f);jv=up(jimage[n,w]);gate('every_finite_strict_selfmap',v<R[n][w]);gate('every_finite_strict_Jw_half',jv<W[n][w]/2);gate('every_saved_map_finite',v.is_finite() and jv.is_finite());im.append(pack(v));jm.append(pack(jv));far.append(pack(f));maxim=max(maxim,up(v/R[n][w]));maxjm=max(maxjm,up(jv/W[n][w]))
   rows.append(dict(cell=n+12,radius=list(map(pack,R[n])),distance=list(map(pack,W[n])),image=im,Jw=jm,complete_far_source=far,whole_ball_physical=pack(physical[n])))
  out=dict(schema='actual-LF-shift060-conditional-nonlow-existence-v1',stage='assemble',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=all(g.values()),gates=g,gate_categories=counts,gate_count=sum(counts.values()),input_identities={k:dict(path=str(p),sha256=z) for k,(p,z) in PINS.items()},batch_manifest=dict(path=str(a.batch_manifest),sha256=sha(a.batch_manifest)),source_batches=batch_records,Green_chunks=gpins,domain=lf['domain'],angular_weight_translation=lf['angular_weight_translation'],windows=WIN,rows=rows,infinite_radius=pack(h),infinite_distance=pack(dh),complete_infinite_image=pack(hm),complete_infinite_Jw=pack(hjm),maximum_image_ratio=pack(maxim),maximum_distance_ratio=pack(maxjm),uniform_contraction_rate=dict(numerator='1',denominator='2'),maximum_whole_ball_physical=pack(max(physical)),fixed_far_parameter=lf['fixed_far_parameter'],fixed_far_forcing_uses_full_quadratic_bound=True,complete_mean_inverse_Q_T_and_infinite=True,actual_LF_is_low_projection_not_auxiliary=True,unknown_infinite_never_reweighted=True,new_conditional_nonlow_exists=True,lower_width_same_field_identified=False,old_original_radius_not_relabelled=True,no_new_ODE_or_Green_integral=True,precision_bits=256,storage_bits=160,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 packet=save(a.out,out);print(json.dumps(dict(all_gates=True,packet=packet,gate_count=out['gate_count'],elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
