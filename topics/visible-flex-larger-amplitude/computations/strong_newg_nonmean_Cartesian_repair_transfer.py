#!/usr/bin/env python3
"""Exact continuous Cartesian jet costs of the saved new-g state repair.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only the linear cylindrical nonmean state synthesis is transferred.
Complete mean, background, differential/metric and seam costs stay separate.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

REPAIR_SHA='71c929c36847500dd236e2d1750e4dd82d4ce1e428ad27fcf82053ae42901063'
SYNTH_SHA='d319574d946f2f6c465b76ffeb92117201aa95bc4318e7100377b184a530fa33'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def ex(z):return F(int(z[0]))*F(2)**int(z[1])
def rat(z):return str(z.numerator)+'/'+str(z.denominator)
def pack(z,bits=160):
    if z<0:raise ArithmeticError('Positive Cartesian error upper required')
    if not z:return ['0',0]
    k=z.numerator.bit_length()-z.denominator.bit_length()
    if z<F(2)**k:k-=1
    e=k-bits+1;r=z/F(2)**e;m=(r.numerator+r.denominator-1)//r.denominator
    v=[str(m),e]
    if ex(v)<z:raise ArithmeticError('Inward Cartesian transfer rounding')
    return v


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repair','repair-resource','synthesis-source','out'):p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Use a fresh Cartesian transfer')
    d,u=read(a.repair),read(a.repair_resource);counts={}
    def check(name,ok):
        if not ok:raise ArithmeticError(name)
        counts[name]=counts.get(name,0)+1
    check('actual_repair_complete',d['schema']=='actual-accepted-physical-quintic-C2-comparison-certificate-v1' and d['all_gates'] and all(d['gates'].values()))
    check('formal_repair_exit',u['exitcode']==0 and u['termination_signal'] is None and u['wait4_observed'])
    check('exact_original_synthesis_and_repair_sources',sha(a.synthesis_source)==SYNTH_SHA and d['source_sha256']==REPAIR_SHA)
    identity=d['input_identity'];M=d['modes'];N=3*M+1
    check('complete_base2_saved_state_layout',identity['angular_chart']=='general-support-core-blend-v1' and identity['modes']==M and d['state_count']==N and [r['state_index'] for r in d['state_bounds']]==list(range(N)))
    q=abs(F.from_float(float(identity['gauge_amplitude'])))
    check('actual_positive_gauge',q>0)
    mode=[];weights=[];kinds=[]
    for j in range(N):
        if j==0:m=0;w=(1,1,1);kind='horizontal_R0'
        elif j<=M:m=2*j;w=(1,m,m*m+1);kind='horizontal_R_cos'
        elif j<=2*M:m=2*(j-M);w=(1,m,m*m+1);kind='horizontal_iT_sin'
        else:m=2*(j-2*M);w=(1,m,m*m);kind='vertical_Z_cos'
        mode.append(m);weights.append(w);kinds.append(kind)
        check('complete_original_even_frequency_cover',j==0 or 2<=m<=2*M and m%2==0)
    errors=[[ex(d['state_bounds'][j]['global_correction_C0_C1_C2'][order]) for j in range(N)] for order in range(3)]
    check('all_actual_state_bounds_positive',all(z>=0 for row in errors for z in row))
    requests=[('X',0,0),('Xs',1,0),('Xpsi',0,1),('Xss',2,0),('Xspsi',1,1),('Xpsipsi',0,2)]
    jets=[]
    for name,so,ao in requests:
        terms=[q*weights[j][ao]*errors[so][j] for j in range(N)]
        total=sum(terms,F(0));out=pack(total)
        check('exact_full_state_cartesian_triangle_sum',ex(out)>=total>=0)
        jets.append({'jet':name,'physical_s_order':so,'original_psi_order':ao,
            'Euclidean_norm_uniform_upper':out,'exact_unrounded_sum':rat(total),
            'per_state_positive_contributions_upper':list(map(pack,terms)),
            'whole_physical_s_and_whole_angle':True})
    result={'schema':'actual-newg-C2-state-repair-to-nonmean-Cartesian-six-jets-v1',
        'scope':__doc__,'all_gates':True,'gate_count':sum(counts.values()),'gates':{k:True for k in counts},'gate_multiplicities':counts,
        'source_sha256':sha(__file__),'input_identities':{str(p):sha(p) for p in (a.repair,a.repair_resource,a.synthesis_source)},
        'accepted_input_identity_sha256':d['input_identity_sha256'],'repaired_state_definition_sha256':d['comparison_field_definition_sha256'],
        'exact_normalized_correction_stream_sha256':d['exact_normalized_correction_stream_sha256'],
        'actual_primary_sha256':identity['primary_sha256'],'gauge_exact':rat(q),'modes':M,'complete_states':N,
        'basis_contract':'R0 exp(i psi), R_m cos(m psi) exp(i psi), i T_m sin(m psi) exp(i psi), Z_m cos(m psi); identical to pinned SavedPrefix.synth, interpreted as exact real formulas.',
        'basis_rows':[{'state':j,'kind':kinds[j],'frequency':mode[j],'Euclidean_angle_derivative_weights_0_1_2':list(weights[j])} for j in range(N)],
        'jet_rows':jets,
        'bound_proof':'Each state basis vector has Euclidean derivative norm bounded by its listed weight for every real psi; triangle inequality uses the saved full-s statewise supremum before summation.',
        'radial_and_angular_domains':'The complete accepted physical interval and every real computational psi, hence a complete period. No angular sampling is used.',
        'whole_field_mean_change_paid':False,'background_or_float_evaluation_error_paid':False,
        'PDE_metric_curvature_reach_or_closed_surface_certified':False,
        'original_accepted_candidate_or_target_g_modified':False,
        'new_ODE_Newton_Node_or_geometry_sampling':0,
        'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_gates':True,'gate_count':result['gate_count'],'path':str(a.out),'sha256':sha(a.out),'bytes':a.out.stat().st_size,
        'jet_displays':{r['jet']:float(ex(r['Euclidean_norm_uniform_upper'])) for r in jets},
        'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)


if __name__=='__main__':main()
