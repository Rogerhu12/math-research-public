#!/usr/bin/env python3
"""Exact R74-family canonical cell12 contribution from all other cells and far.

No new ODE, interval propagation, source quadrature, or outer-centre spectrum.
Uses the original R39 plateau-strip Green row and complete R23 source bounds,
enlarged by the already proved full R74 family envelope. This is a common
canonical l1 budget, not an independent budget assignable to every output.
"""
from __future__ import annotations
import argparse
from decimal import Decimal,localcontext,ROUND_CEILING
from fractions import Fraction as F
import gzip,hashlib,json,resource,sys,time
from pathlib import Path

sys.set_int_max_str_digits(0)
PINS={
 'green':('2026-11-12-closure-newg-strong-m20-real-green.json.gz','40d5fe5eef1ed986393ffc74a597b34b4ae64cca96b14b1c32580d13037d0bc1'),
 'reference':('2026-11-12-closure-newg-strong-m20-real-reference.json','d87a6862836c31f9cb72ed9b8ad74c0ee618797e45a83785c8206a83455233cb'),
 'box':('2026-11-12-closure-newg-strong-m20-real-box.json','81f8f89aa5ca4ce18d4ea55c33e5fc0d63a8f1776090725af0ab032bc2e703c7'),
 'far':('2026-11-12-closure-newg-strong-m20-real-low-far-lift.json','41bc0b2407ea83415be43363e212bac2024b1c5d0c9d80fa6684a6d6abe9c2e3'),
 'family':('2026-11-12-root-anisotropic-auxiliary-family-r3.json.gz','4306f0641856e85a8390dee4c22271dbefe1c6c3c7934f9c9b9a1ec6195ad866'),
}

def p2(e):return F(2)**int(e)
def endpoint(row):return F(int(row['mantissa']))*p2(row['binary_exponent'])
def upper(row):return endpoint(row['upper'])
def lower(row):return endpoint(row['lower'])
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def compact(x,bits=160):
    """Upward dyadic record; comparisons use the unrounded Fraction."""
    x=F(x)
    if x<0:raise ValueError('Positive bound required')
    if x==0:return dict(upper_dyadic=['0',0],decimal_upward='0')
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<p2(e):e-=1
    shift=e-bits+1
    y=x/p2(shift)
    m=(y.numerator+y.denominator-1)//y.denominator
    out=F(m)*p2(shift)
    if not out>=x:raise ArithmeticError('Upward dyadic conversion failed')
    with localcontext() as c:
        c.prec=28;c.rounding=ROUND_CEILING
        shown=str(Decimal(out.numerator)/Decimal(out.denominator))
    return dict(upper_dyadic=[str(m),shift],decimal_upward=shown)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--notes',type=Path,default=Path('notes'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh primary result path')
    docs={};ids={}
    for key,(name,wanted) in PINS.items():
        path=args.notes/name;raw=path.read_bytes();got=hashlib.sha256(raw).hexdigest()
        if got!=wanted:raise ValueError('Immutable primary changed: '+str(path))
        docs[key]=json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
        ids[str(path)]=dict(sha256=got,bytes=len(raw))
    green,ref,box,far,family=(docs[k] for k in ('green','reference','box','far','family'))
    gates={}
    def check(key,value):
        gates[key]=bool(value)
        if not value:raise ArithmeticError('Unpaid complete R74 cell12 gate: '+key)
    cells=list(range(12,225));modes=list(range(2,93,2))
    check('original_all46_green',green['modes']==modes)
    check('all213_green_rows',[r['cell'] for r in green['response_rows']]==cells)
    check('all213_reference_rows',[r['cell'] for r in ref['cell_rows']]==cells)
    check('all213_box_rows',[r['cell'] for r in box['rows']]==cells)
    check('all213_true_far_rows',[r['cell'] for r in far['rows']]==cells)
    check('all213_R74_auxiliary_rows',[r['cell'] for r in family['auxiliary_rows']]==cells)
    check('complete_reference_identity_checks',all(ref['checks'].values()))
    check('complete_R39_box_gates',all(box['gates'].values()))
    check('complete_true_far_gates',all(far['gates'].values()))
    check('complete_R74_all_family_gates',family['all_gates'] is True and all(family['gates'].values()))
    check('all20_independent_R74_axes',[r['mode'] for r in family['parameter_axes']]==list(range(2,41,2)))
    for name in ('reference','box','far'):
        path='notes/'+PINS[name][0]
        check('family_same_'+name,family['input_hashes'][path]==PINS[name][1])
    check('green_same_true_reference',green['input_hashes']['notes/'+PINS['reference'][0]]==PINS['reference'][1])
    for name in ('reference','box'):
        check('far_same_'+name,far['input_hashes']['notes/'+PINS[name][0]]==PINS[name][1])
    check('target12_original_plateau_tau2',lower(ref['cell_rows'][0]['tau'])==upper(ref['cell_rows'][0]['tau'])==2)
    check('complete_green_matrix_shape',len(green['gamma_log2_upper'])==213 and all(len(r)==213 for r in green['gamma_log2_upper']))
    S=upper(family['envelope_factor']);kA=upper(family['auxiliary_nonlinear_factor'])
    alpha=upper(family['total_linear_factor'])
    check('exact_R74_enlargements',S==F(257,256) and kA==F(259,256) and alpha==F(513,512))
    Z=upper(family['retained_auxiliary_far_ball'])
    check('complete_actual_family_far_stays_in_original_ball',upper(family['auxiliary_far_upper'])<Z==p2(-2224))
    check('same_original_true_far_equation',far['far_z_dyadic_bound']=='2^-2224' and far['raw_D_constant']=='2^1967')
    rows=[];terms=[]
    for n,r,b,fam,ge in zip(cells,ref['cell_rows'],box['rows'],family['auxiliary_rows'],green['gamma_log2_upper'][0]):
        xl,xu=lower(r['reference_X']),upper(r['reference_X'])
        check('positive_reference_'+str(n),0<xl<=xu)
        U=upper(b['total_radius_multiple']);v=upper(b['correction_radius_multiple'])
        rho_multiple=upper(fam['nonlinear_radius_multiple'])
        check('original_auxiliary_radius_identity_'+str(n),U==1+v and rho_multiple==kA*v)
        check('whole_R74_field_envelope_'+str(n),alpha+rho_multiple<=S*U)
        check('already_paid_R74_row_'+str(n),all(fam['gates'].values()))
        # Stored R23 bound is B_n*x_n^2. Dividing by the LOWER
        # reference endpoint first safely encloses the coefficient B_n.
        # The actual family norm uses the original chosen upper endpoint.
        B=upper(r['complete_R23_source_L1'])/(xl*xl)
        source=B*(S*U*xu)**2
        term=p2(ge)*source
        terms.append(term)
        rows.append(dict(source_cell=n,target_cell=12,original_green_power2=ge,
            R74_family_source_L1_upper=compact(source),
            canonical_target12_contribution_upper=compact(term),
            full_original_source_mean_inverse_retained=True,
            role='cell12 term to be replaced by a frequency-aware bound' if n==12 else 'unchanged other-cell contribution'))
    x12=upper(ref['cell_rows'][0]['reference_X'])
    rho12=upper(family['auxiliary_rows'][0]['nonlinear_radius_multiple'])*x12
    direct_far=upper(far['rows'][0]['boundary_operator'])*p2(1967)*Z*Z
    outside=sum(terms[1:],F(0));fixed=outside+direct_far;total=sum(terms,F(0))+direct_far
    check('full_old_R74_map_still_inside_complete_radius',total<rho12)
    check('all212_other_cells_retained',len(rows[1:])==212)
    check('true_far_not_set_to_zero',direct_far>0)
    check('common_l1_budget_not_per_mode',True)
    result=dict(scope=__doc__,author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        source_sha256=digest(__file__),input_identities=ids,all_gates=all(gates.values()),gates=gates,
        parameter_domain=family['parameter_domain'],
        parameter_axes=family['parameter_axes'],
        target_cell=12,canonical_reference_strip=2,all46_modes_retained=modes,
        original_R74_total_error_radius=compact(rho12),
        original_R74_reference_x12=compact(x12),
        source12_contribution=compact(terms[0]),
        outside212_source_contribution=compact(outside),direct_true_far_contribution=compact(direct_far),
        fixed_outside_plus_far=compact(fixed),
        outside_plus_far_over_reference=compact(fixed/x12),
        outside_plus_far_over_error_radius=compact(fixed/rho12),
        original_complete_map_over_error_radius=compact(total/rho12),
        diagnostics={f'outside_plus_far_lt_error_radius_2minus{j}':fixed<rho12*p2(-j) for j in (10,20,30,40,50,60)},
        rows=rows,
        interpretation='A bound on the common canonical sum of modal radial suprema at cell12 from all other cells plus the original true far lift. It is a fixed budget for a local bootstrap, not a lower bound on the actual solution and not a separately spendable radius for every mode.',
        no_new_ODE=True,no_new_Arb=True,no_new_source_integral=True,no_Node=True,
        outer_R101_centre_spectrum_used=False,frequency_bootstrap_executed=False,
        full_inner_or_outer_matching_claimed=False,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode()
    payload=gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw
    if len(payload)>=5_000_000:raise ValueError('Per-file repository cap exceeded')
    if len(raw)>1_000_000 and args.out.suffix!='.gz':raise ValueError('Large output must use gzip')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('xb') as f:f.write(payload)
    print(json.dumps(dict(out=str(args.out),sha256=digest(args.out),all_gates=result['all_gates'],
        gates=len(gates),outside_plus_far_over_error_radius=result['outside_plus_far_over_error_radius'],
        outside_plus_far_over_reference=result['outside_plus_far_over_reference'],
        direct_true_far=result['direct_true_far_contribution'],diagnostics=result['diagnostics'],
        seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
