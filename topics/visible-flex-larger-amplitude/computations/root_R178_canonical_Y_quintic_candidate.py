#!/usr/bin/env python3
"""Define a C0 rational quintic Y candidate from the original complete M20 data.

Y=sqrt(r*w^3)*(P,K). The square-root factors used to DEFINE node values
are fixed binary rationals. The candidate physical field divides these
polynomials by the TRUE background factor. All derivative approximations
only define coefficients; their accuracy is never a proof assumption.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import gzip,hashlib,json,math,resource,sys,time
from pathlib import Path
import numpy as np
from flint import arb,ctx

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw)if p.suffix=='.gz'else raw)
def qr(q):return [str(q.numerator),str(q.denominator)]
def hermite(y0,y1,d0,d1,dd0,dd1):return [y0,y0+d0/5,y0+2*d0/5+dd0/20,y1-2*d1/5+dd1/20,y1-d1/5,y1]
def save(p,v):
    if p.exists():raise FileExistsError(p)
    raw=(json.dumps(v,separators=(',',':'))+'\n').encode();p.write_bytes(gzip.compress(raw,mtime=0)if p.suffix=='.gz'else raw)
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--inputs',type=Path,required=True);ap.add_argument('--out-prefix',type=Path,required=True)
    a=ap.parse_args();assert not any(a.out_prefix.parent.glob(a.out_prefix.name+'*'));started=time.monotonic();ctx.prec=256;ctx.threads=1
    ids=load(a.inputs);counts={}
    def gate(k,v):
        counts[k]=counts.get(k,0)+1
        if not v:raise ArithmeticError(k)
    for k in ('jets','jets_resource','jets_source','original_ready','original_source_manifest'):
        gate('input_identity_'+k,sha(ids['files'][k]['path'])==ids['files'][k]['sha256'])
    jets=load(ids['files']['jets']['path']);jr=load(ids['files']['jets_resource']['path'])
    gate('actual_original_complete_jets',jr['exitcode']==0 and jets['all_gates'] and len(jets['pieces'])==216)
    cr=jets['inputs']['files']['R168_primary'];rr=jets['inputs']['files']['R168_resource']
    gate('same_canonical_coordinates',sha(cr['path'])==cr['sha256'] and sha(rr['path'])==rr['sha256'])
    coords=load(cr['path']);gate('actual_canonical_coordinates',coords['all_gates'] and load(rr['path'])['exitcode']==0 and len(coords['rows'])==217)
    original=load(ids['files']['original_source_manifest']['path'])
    for v in original['source_files']:gate('original_background_source',sha(v['path'])==v['sha256'])
    sys.path.insert(0,ids['original_sources_directory'])
    from tail_r33_middle_ordered_physical import SourceValues
    from closure_real_linear_head_enclosure import PositiveKernels
    h=SourceValues(load(ids['files']['original_ready']['path']));ker=PositiveKernels(h,12,92);h.cells={n:ker.source_cell(n)for n in (7,8,9)}
    nodes={};node_records=[]
    for row in coords['rows']:
        radius=float(row['radius']);w=float(row['w']);db=math.sqrt(radius)*w*math.sqrt(w)
        gate('positive_finite_binary_defining_factor',math.isfinite(db) and db>0)
        df=F.from_float(db);values=[df*F.from_float(v)for v in row['relative_P_sine']+row['relative_K_cosine']]
        nodes[row['saved_node']]=(row,df,values)
        node_records.append(dict(saved_node=row['saved_node'],binary_factor=qr(df),exact_Y=[qr(v)for v in values]))
    modes=np.arange(2,41,2,dtype=float);N=1024;theta=2*np.pi*np.arange(N)/N;co=np.cos(np.outer(theta,modes));si=np.sin(np.outer(theta,modes));eps=2.0**-18
    min_denom=1.;max_relative_first_defect=0.;records=[];pieces={}
    def background(bg,x,r):
        q=h.source_point(bg,arb(x));w=float(q['w']);ell=float(q['log_w_x']);ro_x=float(q['ro_x']);E=1+w*w
        rx=abs(w*ell)/(8*E**1.5)+float(h.alpha)*ro_x/E
        return w,rx/(8*r),ell/8,rx/8
    def fieldY(bg,x,r,Y):
        nonlocal min_denom
        w,s,ell,_=background(bg,x,r);E=1+w*w;df=math.sqrt(r)*w*math.sqrt(w);P,K=Y[:20]/df,Y[20:]/df
        q0=float(np.sum((K*K+E*P*P)/4+modes*K*P/2));disc=1-2*q0
        if not disc>0:raise ArithmeticError('finite_definition_mean_branch')
        c=-2*q0/(1+math.sqrt(disc));pv=si@P;tv=co@(modes*P);kv=c+co@K;uv=-si@(modes*K)-pv;den=1+kv+E*tv
        min_denom=min(min_denom,float(den.min()))
        if not den.min()>0:raise ArithmeticError('finite_definition_inverse')
        rhs=(E*s*uv*uv+ell*((kv+tv)**2+w*w*(2*kv*tv+tv*tv-pv*pv)))/den;nm=(2./N)*(co.T@rhs);c0=(ell-s)/2
        return np.r_[c0*Y[:20]-modes*s*Y[20:],-modes*ell*Y[:20]-c0*Y[20:]+df*nm]
    for row in jets['pieces']:
        n,j,k=row['raw_cell'],row['raw_segment'],row['part'];bg=h.cells[n]['segments'][j];allY=[];allDY=[];allDD=[];diagnostics=[]
        for side,node in [(0,row['inner_node']),(1,row['outer_node'])]:
            nr,df,Y=nodes[node];ep=row['endpoint_jets'][side]
            gate('same_original_canonical_node_values',all(F.from_float(v)==F.from_float(w)for v,w in zip(row['P'+str(side)]+row['K'+str(side)],nr['relative_P_sine']+nr['relative_K_cosine'])))
            first=list(map(F.from_float,row['dP'+str(side)]+row['dK'+str(side)]));cf=(F.from_float(ep['s'])+3*F.from_float(ep['l']))/2
            DY=[df*dv+cf*v for dv,v in zip(first,Y)];yf=np.array(list(map(float,Y)));dy=np.array(list(map(float,DY)));x=(k+side)/8.;r=float(nr['radius']);_,_,_,rt=background(bg,x,r)
            f0=fieldY(bg,x,r,yf);defect=float(np.max(np.abs(f0-dy)))/float(df);max_relative_first_defect=max(max_relative_first_defect,defect)
            plus=fieldY(bg,x+eps/8,r+eps*rt,yf+eps*dy);minus=fieldY(bg,x-eps/8,r-eps*rt,yf-eps*dy);dd=(plus-minus)/(2*eps)
            gate('all_finite_candidate_second_jets',bool(np.isfinite(dd).all()));allY.append(Y);allDY.append(DY);allDD.append(list(map(F.from_float,dd.tolist())))
            diagnostics.append(dict(side=side,saved_node=node,finite_field_first_defect_divided_by_binary_factor=defect))
        coeff=[hermite(*v)for v in zip(allY[0],allY[1],allDY[0],allDY[1],allDD[0],allDD[1])];pieces[n,j,k]=coeff
        records.append(dict(cell=n,segment=j,part=k,stage_index=row['stage_index'],exact_YP_Bernstein=[[qr(v)for v in p]for p in coeff[:20]],exact_YK_Bernstein=[[qr(v)for v in p]for p in coeff[20:]],endpoint_definition_diagnostics=diagnostics))
    ordered=list(reversed(jets['pieces']))
    for aa,bb in zip(ordered,ordered[1:]):
        left=pieces[aa['raw_cell'],aa['raw_segment'],aa['part']];right=pieces[bb['raw_cell'],bb['raw_segment'],bb['part']]
        gate('exact_rational_Y_C0_join',all(v[-1]==w[0]for v,w in zip(left,right)))
    gate('complete_original216_piece_domain',len(pieces)==216 and set(pieces)=={(n,j,k)for n in (7,8,9)for j in range(9)for k in range(8)})
    polref=save(Path(str(a.out_prefix)+'-polynomials.json.gz'),dict(schema='R178-rational-quintic-canonical-Y216-v1',rows=records))
    result=dict(schema='R178-explicit-canonical-Y-quintic-candidate-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        input_manifest=dict(path=str(a.inputs),sha256=sha(a.inputs)),canonical_coordinates=cr,original_jets=ids['files']['jets'],polynomial_file=polref,
        all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,canonical_nodes=node_records,
        exact_C0_in_Y=True,physical_candidate_definition='(P,K)=the exact rational Y polynomials divided by the original TRUE sqrt(r*w^3).',
        finite_angular_nodes=N,finite_difference_epsilon=eps,minimum_sampled_denominator_diagnostic=min_denom,max_relative_first_defect_diagnostic=max_relative_first_defect,
        numerical_derivatives_only_define_coefficients=True,derivative_accuracy_not_assumed=True,complete_mean_and_continuous_residual_unpaid=True,
        changed_candidate_not_silently_identified_with_R173=True,R177_P_error_does_not_automatically_apply=True,
        no_new_ODE_or_BVP=True,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    ref=save(Path(str(a.out_prefix)+'-definition.json.gz'),result)
    print(json.dumps(dict(primary=ref,polynomials=polref,gate_count=result['gate_count'],first_defect_diagnostic=max_relative_first_defect,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
