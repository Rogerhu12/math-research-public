#!/usr/bin/env python3
"""Signed low46 zero-entry response to the complete R174 candidate defect.

Original 3940 homogeneous leaves are consumed; no ODE is rerun. Both P and
K forcing components are paid. This is not a nonlinear error tube.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx,fmpq

B=Path('/workspace/scratch/d1aa462cfc02');EW=B/'exact-work'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def ar(q):return arb(fmpq(q.numerator,q.denominator))
def ep(v):
    return arb((int(v[0]),int(v[1]))) if isinstance(v,list) else arb((int(v['mantissa']),int(v['binary_exponent'])))
def ball(v):return ep(v['lower']).union(ep(v['upper']))
def point(v):
    m,e=v.man_exp();return [str(m),int(e)]
def rec(v):return dict(lower=point(v.lower()),upper=point(v.upper()))
def up(v):return v.upper()
def error(v,r):return v+(-up(r)).union(up(r))
def mv(M,v):return [sum((M[i][j]*v[j] for j in range(2)),arb(0)) for i in range(2)]
def save(p,v):
    if p.exists():raise FileExistsError(p)
    raw=(json.dumps(v,separators=(',',':'))+'\n').encode();p.write_bytes(gzip.compress(raw,mtime=0) if p.suffix=='.gz' else raw)
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--residual',type=Path,required=True);ap.add_argument('--resource',type=Path,required=True);ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--rss-kib',type=int,default=196608)
    a=ap.parse_args();assert not any(a.out_prefix.parent.glob(a.out_prefix.name+'*'));started=time.monotonic();ctx.prec=256;ctx.threads=1;counts={}
    def gate(k,v):
        counts[k]=counts.get(k,0)+1
        if not v:raise ArithmeticError(k)
    residual=load(a.residual);owned=load(a.resource)
    gate('actual_complete_R174',owned['exitcode']==0 and residual['all_gates'] and residual['full_original_domain_covered_once'] and residual['original_background_leaves']==3940 and residual['refined_leaves']==3976)
    plan=load(residual['batch_plan']['path']);gate('original_residual_plan',sha(residual['batch_plan']['path'])==residual['batch_plan']['sha256'])
    inputs=load(plan['input_manifest']);gate('same_residual_inputs',sha(plan['input_manifest'])==residual['input_manifest_sha256'])
    mean=load(inputs['files']['R173']['path']);gate('same_exact_quintic_candidate',sha(inputs['files']['R173']['path'])==residual['R173_sha256'] and mean['candidate_degree']==5)
    domain=mean['rows'];mi=load(inputs['files']['R173_inputs']['path'])
    helper=EW/'2026-11-13-exact-resume-outer8to7-signed-low46-v1.py'
    gate('original_signed_helper',sha(helper)=='d34c1e1a7c5933921d5aceeab159eab558b7198af8ee68eca86d4aca407bc0ab')
    spec=importlib.util.spec_from_file_location('original_low46_signed',helper);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    source_manifest=load(mi['files']['original_source_manifest']['path'])
    for rr in source_manifest['source_files']:gate('original_background_source',sha(rr['path'])==rr['sha256'])
    h=old.SourceValues(load(mi['files']['original_ready']['path']));ker=old.PositiveKernels(h,12,92);h.cells={n:ker.source_cell(n) for n in (9,8,7)}
    modes=list(range(2,93,2));sigma=arb(1)/64;weights=[(1+m)*(m*sigma).exp() for m in modes]
    def rows(chunks):
        for rr in chunks:
            gate('complete_saved_chunk_identity',sha(rr['path'])==rr['sha256'])
            for row in load(rr['path'])['rows']:yield row
    it=iter(rows(residual['profile_chunks']));peek=next(it,None);used=total=0;Y=[[arb(0),arb(0)] for _ in modes];Ytail=[[arb(0),arb(0)] for _ in modes]
    cells=[];checkpoints=[]
    for n in (9,8,7):
        pr=mi['files']['profile_'+str(n)];profile=load(pr['path']);pres=load(mi['files']['profile_resource_'+str(n)]['path'])
        gate('same_original_complete_homogeneous_profile',sha(pr['path'])==pr['sha256'] and profile['all_gates'] and pres['exitcode']==0 and profile['config']['coordinates']=='Y=sqrt(r*w^3)*(P_sine,K_cosine)')
        caps=[[arb(0),arb(0)] for _ in modes];tailcaps=[[arb(0),arb(0)] for _ in modes];last={j:F(0) for j in range(9)};ncount=0
        for row in rows(profile['profile_chunks']):
            j=row['segment'];lo,hi=F(row['left']),F(row['right']);ident=(n,j,row['left'],row['right']);gate('original_leaf_coverage',lo==last[j] and hi>lo);last[j]=hi;ncount+=1;total+=1
            joined=None;common=arb(0);pieces=0;subleft=lo
            while peek is not None:
                dm=domain[peek['global_leaf_index']]
                if (dm['cell'],dm['segment'],*dm['source_original_leaf'])!=ident:break
                gate('matching_exact_refined_residual',peek['cell']==n and peek['segment']==j and F(peek['left'])==subleft and F(peek['right'])<=hi)
                subleft=F(peek['right']);pieces+=1;used+=1
                data=peek['finite_inverse_residuals'];gate('all46_finite_residual_components',[x['mode'] for x in data]==modes)
                current=[[ball(x['exact_finite_P_residual']),ball(x['finite_inverse_K_residual'])] for x in data]
                joined=current if joined is None else [[joined[k][i].union(current[k][i]) for i in range(2)] for k in range(46)]
                common=max(common,ep(peek['common_complete_low_remainder_W1']));peek=next(it,None)
            gate('all_original_leaf_residual_pieces',pieces>=1 and subleft==hi and joined is not None and common>0)
            dx=ar(hi-lo);rr=ball(row['whole_radius']);ww=ball(row['whole_w']);rx=ball(row['radius_x']);ell=ball(row['log_w_x'])
            bg=h.source_point(h.cells[n]['segments'][j],ar(lo).union(ar(hi)));positive=(h.alpha*bg['ro_x']/(1+ww*ww)).lower()
            lower=max(rx.lower(),positive);upper=rx.upper();gate('same_true_positive_radius_derivative',rr>0 and ww>0 and lower>0 and upper>=lower)
            rx=lower.union(upper);s=rx/rr;ss=dx*s;ee=dx*ell;dd=(ee-ss)/2;den=(rr*ww**3).sqrt()
            balance=ball(row['balance']);q=ball(row['integral_norm']);gate('original_partial_neumann_domain',balance>0 and 0<=q<1)
            remainder=up(q*q/(1-q));rem=[[remainder,up(remainder/balance)],[up(remainder*balance),remainder]]
            d=up(abs(dd));one=1-d;gate('suffix_diagonal_domain',one>0)
            wr=h.source_point(h.cells[n]['segments'][j],ar(hi))['w'];denend=(ball(row['radius_right'])*wr**3).sqrt();endpoint=[]
            for k,m in enumerate(modes):
                aa,bb=up(m*abs(ss)),up(m*abs(ee));det=one*one-aa*bb;gate('complete_two_component_suffix_resolvent',det>0)
                e_diag=up((d*one+aa*bb)/det);E=[[e_diag,up(aa/det)],[up(bb/det),e_diag]]
                force=[-den*v for v in joined[k]];mass=[up(dx*abs(v)) for v in force]
                remainder_vec=[up(v) for v in mv(E,mass)]
                J=[error(dx*force[i],remainder_vec[i]) for i in range(2)]
                Jpart=[error(arb(0).union(dx)*force[i],remainder_vec[i]) for i in range(2)]
                # Each mode receives a conservative consequence of the same
                # shared W1 tail. Summing these mode bounds overpays (up to
                #46 copies); it is never reported as a conserved shared mass.
                tailforce=up(abs(den)*common/weights[k]);tailmass=up(dx*tailforce)
                Jtail=[up(E[0][1]*tailmass),up((1+E[1][1])*tailmass)]
                M=[[dd,-m*ss],[-m*ee,-dd]]
                partial=[[error(arb(0).union(M[i][l])+(1 if i==l else 0),rem[i][l]) for l in range(2)] for i in range(2)]
                whole0=mv(partial,Y[k]);whole=[(whole0[i]+Jpart[i])/den for i in range(2)]
                partabs=[[up(abs(v)) for v in row0] for row0 in partial]
                whole_tail=[up((v+Jtail[i])/den.lower()) for i,v in enumerate(mv(partabs,Ytail[k]))]
                T=[[ball(v) for v in rr0] for rr0 in row['local_signed_flow'][k]['matrix']]
                Y[k]=[v+J[i] for i,v in enumerate(mv(T,Y[k]))]
                Tabs=[[up(abs(v)) for v in rr0] for rr0 in T]
                Ytail[k]=[up(v+Jtail[i]) for i,v in enumerate(mv(Tabs,Ytail[k]))]
                gate('all_finite_whole_and_endpoint_entries',all(v.is_finite() for v in whole+whole_tail+Y[k]+Ytail[k]))
                for i in range(2):
                    caps[k][i]=max(caps[k][i],up(abs(whole[i])+whole_tail[i]));tailcaps[k][i]=max(tailcaps[k][i],whole_tail[i])
                endpoint.append(dict(mode=m,finite_tracezero_Y=[rec(v) for v in Y[k]],positive_inverse_tail_Y=[point(v) for v in Ytail[k]],physical_PK=[rec(error(Y[k][i]/denend,up(Ytail[k][i]/denend.lower()))) for i in range(2)]))
            if hi==1:
                checkpoints.append(save(Path(str(a.out_prefix)+f'-cell{n}-segment{j}.json.gz'),dict(cell=n,segment=j,endpoint_modes=endpoint,zero_entry=True,finite46_only=True,complete_shared_inverse_tail_conservatively_overpaid=True)))
            if total%200==0:print(json.dumps(dict(event='actual_low46_defect_Duhamel',original_leaves=total,refined_leaves=used,cell=n,elapsed_seconds=time.monotonic()-started)),flush=True)
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Declared192MiB resource cap')
        gate('all_original_nine_segments',all(x==1 for x in last.values()) and ncount==profile['counts']['taylor']+profile['counts']['root_brackets'])
        mass=up(sum((weights[k]*sum(caps[k],arb(0)) for k in range(46)),arb(0)))
        tailmass=up(sum((weights[k]*sum(tailcaps[k],arb(0)) for k in range(46)),arb(0)))
        cells.append(dict(cell=n,original_leaves=ncount,whole_cell_radial_first_strong=point(mass),positive_inverse_tail_contribution_overpaid=point(tailmass),mode_caps=[dict(mode=m,P=point(caps[k][0]),K=point(caps[k][1])) for k,m in enumerate(modes)],endpoint_modes=endpoint))
        print(json.dumps(dict(event='complete_low46_defect_cell',cell=n,strong_display=float(mass),tail_display=str(tailmass))),flush=True)
    gate('all_original_and_refined_leaves',total==3940 and used==3976 and peek is None)
    result=dict(schema='R175-original-low46-complete-quintic-defect-response-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        input_residual=dict(path=str(a.residual),sha256=sha(a.residual)),input_resource=dict(path=str(a.resource),sha256=sha(a.resource)),
        all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,cells=cells,checkpoints=checkpoints,
        original_leaves=total,refined_leaves=used,coordinates='Y=sqrt(r*w^3)*(P_sine,K_cosine)',source='-sqrt(r*w^3)*(RP,RK)',
        complete_mean_and_positive_inverse_tail=True,shared_inverse_tail_conservatively_overpaid_not_free_per_mode=True,
        zero_entry_at_node10=True,finite46_particular_response_only=True,initial_error_and_nonlinear_feedback_and_high_response_unpaid=True,no_new_ODE=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    ref=save(Path(str(a.out_prefix)+'-certificate.json.gz'),result);print(json.dumps(dict(primary=ref,gate_count=result['gate_count'],cells=[dict(cell=c['cell'],strong=float(ep(c['whole_cell_radial_first_strong'])))for c in cells],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
