#!/usr/bin/env python3
"""Prepared v2 complete signed low46 source of the fixed R88 centre.

v1 was prepared but never executed. v2 distinguishes the10793 saved source
rows from the10933 underlying Green profile subpanels; it changes only
coverage/schema checks, not the complete physical source formula.

Reuse every original R88 real field enclosure. Keep its original modes6..40,
its true linear modes2/4, the complete scalar mean, numerator zero mode, and
four full Neumann terms before extracting any of the46 nonmean coefficients.
An explicit norm tail bounds every omitted inverse term. This is a new source
evaluation, not the full46 exterior fixed point or its cut consistency.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gc
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, arb_poly, ctx
import closure_outer_two_cell_adjoint as compact_helper
from closure_outer_two_cell_adjoint import compact_endpoint

OLD_SOURCE_SHA = '306b2bc0c49635d731f3bbe91653310f2b2ecba19bcb7437f8ef932f37a5d75b'
HELPER_SHA = '184667ec3f78b9d99d2a5fe28465c243ecee0e6ba4d4685199e72bd9bef0899a'
MODES = list(range(2, 93, 2))
INPUT_MODES = list(range(2, 41, 2))

def digest(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()

def point(x):
    if isinstance(x, dict):
        return arb((int(x['mantissa']), int(x['binary_exponent'])))
    return arb((int(x[0]), int(x[1])))

def ball(x):
    if isinstance(x, dict):
        return point(x['lower']).union(point(x['upper']))
    return point(x[0]).union(point(x[1]))

def compact(x):
    if not x.is_finite():
        raise ArithmeticError('Nonfinite complete source interval')
    return [compact_endpoint(x.lower(), -1, 96),
            compact_endpoint(x.upper(), 1, 96)]

def upper(x):
    if not x.is_finite() or x.lower() < 0:
        raise ArithmeticError('A finite nonnegative proof bound is required')
    return compact_endpoint(x.upper(), 1, 96)

def overlap(a, b):
    lo, hi = max(a.lower(), b.lower()), min(a.upper(), b.upper())
    if lo > hi:
        raise ArithmeticError('Original selected complete source no longer intersects')
    return lo.union(hi)

def shift(p, n):
    return arb_poly([arb(0)]*n + p.coeffs())

def with_constant(p, centre, c):
    a = p.coeffs()
    a += [arb(0)]*max(0, centre+1-len(a))
    a[centre] += c
    return arb_poly(a)

def coefficient(p, k):
    a = p.coeffs()
    return a[k] if 0 <= k < len(a) else arb(0)

def full_source(row, weights):
    original = row['original_candidate_PK']
    selected = row['true_linear_selected_PK']
    if [int(v['mode']) for v in original] != INPUT_MODES:
        raise ValueError('All original20 nonmean modes are required')
    if [int(v['mode']) for v in selected] != [2, 4]:
        raise ValueError('Only the two original selected centre modes are replaced')
    values = {int(v['mode']): (ball(v['P']), ball(v['K'])) for v in original}
    values.update({int(v['mode']): (ball(v['P']), ball(v['K'])) for v in selected})
    r, rx, w, ell = [ball(row[k]) for k in ('radius','radius_x','w','log_w_x')]
    if not r > 0 or not rx > 0 or not w > 0 or not w <= arb(1)/2:
        raise ArithmeticError('Same true positive physical source domain required')
    E, z, s = 1+w*w, w*w, rx/r
    strong_R = point(row['strong_R']['upper'])
    mean_cap = point(row['complete_mean_abs']['upper'])
    leading = point(row['complete_leading_norm']['upper'])
    full_norm = point(row['complete_nonlinear_source_W1']['upper'])
    if not 0 <= strong_R < arb(1)/64 or not 0 <= mean_cap or not 0 <= leading < 1:
        raise ArithmeticError('Complete mean and Wiener inverse domain unpaid')
    c = (-mean_cap).union(mean_cap)

    # Exponents j correspond to physical frequency2j. Pp and Up are odd real
    # Laurent polynomials, so the actual sine fields are Pp/(2i), Up/(2i).
    # Kp and Tp are even; actual cosine fields are Kp/2 and Tp/2.
    pa, ka, ta, ua = ([arb(0) for _ in range(41)] for _ in range(4))
    for m in INPUT_MODES:
        p, k = values[m]
        j, t, u = m//2, m*p, -m*k-p
        pa[20+j], pa[20-j] = p, -p
        ua[20+j], ua[20-j] = u, -u
        ka[20+j] = ka[20-j] = k
        ta[20+j] = ta[20-j] = t
    Pp, Kp, Tp, Up = map(arb_poly, (pa, ka, ta, ua))
    Cp = Kp+Tp
    quarter = arb(1)/4
    Q = (-(Up*Up)*(E*s) +
         (Cp*Cp+(Kp*Tp*2+Tp*Tp+Pp*Pp)*z)*ell)*quarter
    # B_c=ell[2c(K+E T)+c^2]. Its constant term MUST remain until division.
    B = with_constant((Kp+Tp*E)*(c*ell), 20, ell*c*c)
    numerator = Q+shift(B, 20)
    leading_poly = with_constant((Kp+Tp*E)*(arb(1)/2), 20, c)
    series, term, offset = numerator, numerator, 40
    for _ in range(3):
        term = -(term*leading_poly)
        series = shift(series, 20)+term
        offset += 20
    # Exact identity: N=A sum_{j=0}^3(-L)^j + L^4 N.
    # The old stored bound is for the FULL UNPROJECTED quotient, hence valid.
    remainder_W1 = (leading**4*full_norm).upper()
    saved = {int(v['mode']): v for v in row['selected_cosine_sources']}
    result = []
    for m in MODES:
        quadratic = 2*coefficient(Q, 40+m//2)
        finite = 2*coefficient(series, offset+m//2)
        error = (remainder_W1/weights[m].lower()).upper()
        enclosure = finite+(-error).union(error)
        if m in saved:
            overlap(quadratic, ball(saved[m]['quadratic_cosine']))
            enclosure = overlap(enclosure, ball(saved[m]['complete_source_cosine']))
        result.append({'mode':m, 'quadratic_cosine':compact(quadratic),
                       'four_term_neumann_cosine':compact(finite),
                       'complete_source_cosine':compact(enclosure),
                       'complete_inverse_tail_cosine_upper':upper(error)})
    return result, remainder_W1, leading, mean_cap

class Writer:
    def __init__(self, prefix, cell, segment, limit):
        self.prefix,self.cell,self.segment,self.limit=prefix,cell,segment,limit
        self.number,self.count=0,0
        self.handle=None
        self.files=[]
    def add(self, row):
        if self.handle is None:
            self.path=Path(str(self.prefix)+f'-cell{self.cell:03d}-segment{self.segment}-part{self.number:03d}.jsonl.gz')
            self.partial=Path(str(self.path)+'.partial')
            if self.path.exists() or self.partial.exists():
                raise FileExistsError('Immutable fresh output prefix required')
            self.handle=gzip.open(self.partial,'wt',compresslevel=9)
            self.handle.write(json.dumps({'kind':'header','cell':self.cell,
                'segment':self.segment,'part':self.number,'modes':MODES,
                'centre':'exact original R88 fixed Z0, not actual full46 solution',
                'complete_mean_numerator_zero_mode_retained':True,
                'neumann_terms':4},separators=(',',':'))+'\n')
            self.count=0
        self.handle.write(json.dumps(row,separators=(',',':'))+'\n')
        self.count+=1
        if self.count>=self.limit:
            self.close()
    def close(self):
        if self.handle is None:
            return
        self.handle.write(json.dumps({'kind':'trailer','complete':True,
                                     'subpanels':self.count})+'\n')
        self.handle.close()
        self.handle=None
        if self.partial.stat().st_size>=5_000_000:
            raise ArithmeticError('Complete gzip file exceeds repository limit')
        self.partial.rename(self.path)
        self.files.append({'path':str(self.path),'bytes':self.path.stat().st_size,
                           'sha256':digest(self.path),'subpanels':self.count})
        self.number+=1

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fields-summary',type=Path,required=True)
    ap.add_argument('--fields-summary-sha256',required=True)
    ap.add_argument('--input-root',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--rss-kib',type=int,default=98304)
    ap.add_argument('--chunk-rows',type=int,default=64)
    a=ap.parse_args()
    if not 1<=a.chunk_rows<=64:
        raise ValueError('Keep independently bounded complete chunks')
    output=Path(str(a.out_prefix)+'-summary.json')
    if output.exists() or Path(str(a.out_prefix)+'-failure.json').exists():
        raise FileExistsError('Do not overwrite an observed prior run')
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if digest(a.fields_summary)!=a.fields_summary_sha256:
        raise ValueError('Whole original R88 summary hash mismatch')
    if digest(Path(compact_helper.__file__))!=HELPER_SHA:
        raise ValueError('Frozen directed dyadic helper changed')
    ctx.prec,ctx.threads=256,1
    d=json.loads(a.fields_summary.read_text())
    if (not d['all_gates'] or not all(d['gates'].values()) or
        d['source_sha256']!=OLD_SOURCE_SHA or
        d['original_panels']!=10793 or d['actual_subpanels']!=10933 or
        d['tau']!='1/64'):
        raise ValueError('Require the complete actually executed original R88 centre')
    if [(int(g['cell']),int(g['segment'])) for g in d['groups']] != [(n,j) for n in (11,10) for j in range(9)]:
        raise ValueError('Keep all18 true groups in their exact source order')
    weights={m:(1+m)*(arb(m)/64).exp() for m in MODES}
    inputs={str(a.fields_summary):a.fields_summary_sha256}
    groups=[]
    original=set()
    count=0
    max_tail,max_lead,max_mean=arb(0),arb(0),arb(0)
    began=time.monotonic()
    active=None
    try:
        for g in d['groups']:
            n,j=int(g['cell']),int(g['segment'])
            active={'cell':n,'segment':j,'completed_subpanels':0}
            writer=Writer(a.out_prefix,n,j,a.chunk_rows)
            previous=Fraction(0)
            for chunk in g['chunks']:
                p=Path(chunk['path'])
                if not p.is_absolute():
                    p=a.input_root/p
                if digest(p)!=chunk['sha256']:
                    raise ValueError('A complete R88 original field chunk changed')
                inputs[str(p)]=chunk['sha256']
                with gzip.open(p,'rt') as f:
                    block=json.load(f)
                if int(block['cell'])!=n or int(block['segment'])!=j:
                    raise ValueError('Source group identity mismatch')
                for row in block['panels']:
                    left,right=Fraction(row['x_left']),Fraction(row['x_right'])
                    if left!=previous or not left<right or right>1:
                        raise ValueError('No gap/overlap may be removed from source coverage')
                    previous=right
                    sources,tail,lead,mean=full_source(row,weights)
                    writer.add({'kind':'complete_fixed_centre_source',
                        'cell':n,'segment':j,'panel':int(row['panel']),
                        'x_left':row['x_left'],'x_right':row['x_right'],
                        'source_envelope':row['source_envelope'],
                        'sources':sources,'complete_inverse_tail_W1':upper(tail)})
                    max_tail,max_lead,max_mean=max(max_tail,tail),max(max_lead,lead),max(max_mean,mean)
                    original.add((n,j,int(row['panel'])))
                    count+=1
                    active['completed_subpanels']+=1
                    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
                        raise MemoryError('Owned small-Arb RSS guard')
                del block
                gc.collect()
            writer.close()
            if previous!=1 or active['completed_subpanels']!=int(g['panels']):
                raise ValueError('The full original physical segment was not consumed')
            groups.append({'cell':n,'segment':j,
                           'source_panels':active['completed_subpanels'],
                           'underlying_profile_subpanels':int(g['subpanels']),
                           'chunks':writer.files})
            print(json.dumps({'event':'complete_low46_centre_source_group',
                              'cell':n,'segment':j,'subpanels':active['completed_subpanels']}),flush=True)
        gates={'all_original_chunk_hashes':True,'all18_complete_groups':len(groups)==18,
            'all10793_original_leaves':len(original)==10793,
            'all10793_original_field_source_rows':count==10793,
            'all10933_underlying_original_profile_subpanels':sum(int(g['subpanels']) for g in d['groups'])==10933,
            'all20_original_input_modes_and_both_actual_linear_modes_retained':True,
            'all46_nonmean_outputs_retained':True,
            'full_scalar_mean_and_numerator_zero_mode_kept_until_inverse':True,
            'signed_finite_quadratic_and_four_complete_neumann_terms':True,
            'entire_omitted_inverse_tail_paid_by_unprojected_norm':True,
            'old_selected2and4_intersect_same_true_source':True,
            'same_actual_background_and_whole_source_coverage':True}
        result={'schema':'visible-flex-larger-fixed-R88-centre-low46-signed-source-v2',
            'author':'/root (GPT-6 Astra Pro, AI-assisted)','status':'Actual complete fixed-centre source enclosures',
            'all_gates':all(gates.values()),'gates':gates,'groups':groups,
            'original_panels':len(original),'processed_source_panels':count,
            'underlying_original_profile_subpanels':int(d['actual_subpanels']),'modes':MODES,
            'tau':'1/64','neumann_terms':4,'source_sha256':digest(Path(__file__)),
            'original_field_source_sha256':OLD_SOURCE_SHA,'helper_sha256':HELPER_SHA,
            'input_hashes':inputs,'maximum_complete_inverse_tail_W1':upper(max_tail),
            'maximum_complete_leading_norm':upper(max_lead),
            'maximum_complete_mean_absolute_bound':upper(max_mean),
            'new_ODE_or_source_integral':False,'actual_Arb_source_evaluation':True,
            'actual_full46_fixed_point_or_cut_or_closed_surface_claimed':False,
            'elapsed_seconds':time.monotonic()-began,
            'peak_RSS_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
        output.write_text(json.dumps(result,indent=2)+'\n')
        if not result['all_gates']:
            raise ArithmeticError('Complete coverage gate failed')
        print(json.dumps({'event':'complete_low46_source_done','output':str(output),
            'sha256':digest(output),'all_gates':True,'subpanels':count}),flush=True)
    except BaseException as error:
        fail=Path(str(a.out_prefix)+'-failure.json')
        fail.write_text(json.dumps({'status':'Incomplete source evaluation, no nonexistence conclusion',
            'error_type':type(error).__name__,'error':str(error),'active':active,
            'completed_groups':groups,'source_sha256':digest(Path(__file__)),
            'input_hashes':inputs,'elapsed_seconds':time.monotonic()-began},indent=2)+'\n')
        raise

if __name__=='__main__':
    main()
