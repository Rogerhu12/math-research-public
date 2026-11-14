#!/usr/bin/env python3
"""Extract the actual all213 R74 canonical modal-bootstrap inputs.

Each original cell retains its own reference strip tau_n. The actual
plateau Green maximum is a valid bound for each retained mode separately;
it is not summed over modes. Actual low columns provide the linear modal
caps, all original20 parameter axes remain, and the positive true-far mass
is shared once per target. This only prepares data for finite substitution
in the already proved auxiliary family; it makes no new fixed-point claim.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import fmpq as Q

PINS={
 'reference':('2026-11-12-closure-newg-strong-m20-real-reference.json','d87a6862836c31f9cb72ed9b8ad74c0ee618797e45a83785c8206a83455233cb'),
 'box':('2026-11-12-closure-newg-strong-m20-real-box.json','81f8f89aa5ca4ce18d4ea55c33e5fc0d63a8f1776090725af0ab032bc2e703c7'),
 'family':('2026-11-12-root-anisotropic-auxiliary-family-r3.json.gz','4306f0641856e85a8390dee4c22271dbefe1c6c3c7934f9c9b9a1ec6195ad866'),
 'columns':('2026-11-12-closure-real-linear-q003-low46-recovered.json.gz','cabdb3fca1d9176b1f2c46a2f7b2ff5b82ff1af426c4c942c7863c3c15c65f91'),
 'ordered':('2026-11-12-closure-ordered-green-low46-v2.json.gz','482a56deff89bb0e330690713fb33afc3d6f478dc02e58c8f765d2a12fc25ce0'),
 'green':('2026-11-12-closure-newg-strong-m20-real-green.json.gz','40d5fe5eef1ed986393ffc74a597b34b4ae64cca96b14b1c32580d13037d0bc1'),
 'far':('2026-11-12-closure-newg-strong-m20-real-low-far-lift.json','41bc0b2407ea83415be43363e212bac2024b1c5d0c9d80fa6684a6d6abe9c2e3'),
 'cell12':('2026-11-13-inner-aux-cell12-spectral-bootstrap-r1.json.gz','490bbdaa71cbd14b4dab9fbf6ac820d72b895b7fc5664b8a3a2ff454bb63a1c6'),
}
BITS=160
def p2(e):return Q(1<<e) if e>=0 else Q(1,1<<(-e))
def ep(d):return Q(int(d['mantissa']))*p2(int(d['binary_exponent']))
def lo(d):return ep(d['lower'])
def hi(d):return ep(d['upper'])
def exact(d):
    a,b=lo(d),hi(d)
    if a!=b:raise ArithmeticError('An exact saved constant is required')
    return a
def decode(d):return Q(int(d[0]))*p2(int(d[1]))
def compact(d):return decode(d['upper_dyadic'])
def pack(x):
    if x<0:raise ArithmeticError('Positive upper bounds only')
    if not x:return ['0',0]
    e=int(x.p).bit_length()-int(x.q).bit_length()
    if x<p2(e):e-=1
    shift=e-BITS+1;y=x/p2(shift);m=(int(y.p)+int(y.q)-1)//int(y.q)
    if Q(m)*p2(shift)<x:raise ArithmeticError('Outward endpoint conversion failed')
    return [str(m),shift]
def up(x):return decode(pack(x))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--notes',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    if a.out.suffix!='.gz':raise ValueError('Compress the complete scientific input')
    identities={};gates={}
    def check(name,yes):
        if not yes:raise ArithmeticError(name)
        gates[name]=True
    def load(p,wanted):
        raw=p.read_bytes();got=hashlib.sha256(raw).hexdigest()
        check('input_'+p.name,got==wanted);identities[str(p)]=dict(sha256=got,bytes=len(raw))
        return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
    docs={key:load(a.notes/name,wanted) for key,(name,wanted) in PINS.items()}
    ref,box,fam,col,ordered,green,far,boot=[docs[k] for k in PINS]
    cells=list(range(12,225));modes=list(range(2,93,2))
    check('all46_modes',ref['modes']==col['modes']==ordered['modes']==green['modes']==modes)
    check('all213_reference_box_family_far_green',all([r['cell'] for r in rows]==cells for rows in
          (ref['cell_rows'],box['rows'],fam['auxiliary_rows'],far['rows'],green['response_rows'])))
    check('complete_original_gates',all(ref['checks'].values()) and all(box['gates'].values()) and
          fam['all_gates'] and all(fam['gates'].values()) and all(far['gates'].values()) and
          boot['all_gates'] and all(boot['gates'].values()))
    check('actual_cellwise_reference_strip',green['strip_formula']==ref['strip_formula']==
          'tau_n = max(2, 1 + (n-12)*log(2)/4); each whole cell uses its stated constant strip')
    check('all45369_original_gamma',len(green['gamma_log2_upper'])==213 and
          all(len(r)==213 and all(isinstance(v,int) for v in r) for r in green['gamma_log2_upper']))
    for key in ('reference','columns','ordered'):
        name,wanted=PINS[key];check('green_same_'+key,green['input_hashes']['notes/'+name]==wanted)
    for key in ('reference','box','columns','far'):
        name,wanted=PINS[key];check('family_same_'+key,fam['input_hashes']['notes/'+name]==wanted)
    for key in ('reference','box'):
        name,wanted=PINS[key];check('far_same_'+key,far['input_hashes']['notes/'+name]==wanted)
    S,alpha,kA=[exact(fam[k]) for k in ('envelope_factor','total_linear_factor','auxiliary_nonlinear_factor')]
    check('same_R74_scale_constants',(S,alpha,kA)==(Q(257,256),Q(513,512),Q(259,256)))
    axes={r['mode']:r for r in fam['parameter_axes']}
    check('all20_original_independent_axes',list(axes)==modes[:20])
    check('same_true_far_ball_and_map',exact(fam['retained_auxiliary_far_ball'])==p2(-2224) and
          hi(fam['auxiliary_far_upper'])<p2(-2224) and far['far_z_dyadic_bound']=='2^-2224' and far['raw_D_constant']=='2^1967')
    Z=p2(-2224);farD=p2(1967)*Z*Z
    exphi,explo=Q(87,32),Q(8,3)
    sqrt2hi=Q(14142135623730951,10**16)
    check('same_elementary_exponential_enclosures',Q(1631,600)<exphi and sum((Q(1,k) for k in (1,1,2,6)),Q(0))==explo)
    check('actual_half_power_enclosure',sqrt2hi>0 and sqrt2hi**2>2)
    xx=[];BB=[];originalrho=[];totals=[];farhat=[];rows=[]
    for i,n in enumerate(cells):
        r,b,f=ref['cell_rows'][i],box['rows'][i],fam['auxiliary_rows'][i]
        x=hi(r['reference_X']);xl=lo(r['reference_X']);U=exact(b['total_radius_multiple']);v=exact(b['correction_radius_multiple'])
        rho=exact(f['nonlinear_radius_multiple'])
        check('original_same_cell_domain_'+str(n),0<xl<=x and U==1+v and rho==kA*v and
              alpha+rho<=S*U and S*U*hi(r['relative_to_R23_radius'])<1 and all(f['gates'].values()))
        B=up(hi(r['complete_R23_source_L1'])/(xl*xl));bx=up(B*x)
        fhat=up(hi(far['rows'][i]['boundary_operator'])*farD/x)
        check('positive_original_far_'+str(n),fhat>0)
        e=[rho]*46;initialrho=rho
        if i==0:
            bxref=compact(boot['reference_x12'])
            check('same_cell12_bootstrap_reference',bxref>=x and boot['target_cell']==12 and
                  boot['canonical_reference_strip']==2 and boot['all46_modes_retained']==modes)
            bridge=bxref/x
            initialrho=min(rho,up(compact(boot['final_common_error_over_reference'])*bridge))
            e=[min(initialrho,up(compact(row['auxiliary_error_pair_mass_over_reference'])*bridge)) for row in boot['final_modal_rows']]
            check('same_R121_all46_rows',[r['mode'] for r in boot['final_modal_rows']]==modes)
        correlations=[]
        for m in modes:
            value=explo**(-4*m) if n<18 else explo**(-2*m)*p2(-m*(n-12)//2)
            correlations.append(pack(value))
        xx.append(x);BB.append(B);originalrho.append(rho);totals.append(S*U);farhat.append(fhat)
        rows.append(dict(cell=n,tau_interval=r['tau'],reference_x_upper=pack(x),B_upper=pack(B),
            B_times_reference_upper=pack(bx),source_Rmax_per_unit_common=pack(bx/32),
            linear_pair_caps_over_reference=None,linear_common_cap_over_reference=None,
            initial_correction_pair_caps_over_reference=list(map(pack,e)),
            initial_correction_common_cap_over_reference=pack(initialrho),
            original_correction_common_cap_over_reference=pack(rho),
            far_correction_common_over_reference=pack(fhat),
            difference_correlation_upper_by_positive_minimum_mode=correlations,
            original_total_field_common_cap_over_reference=pack(S*U),
            original_R23_domain_ratio_upper=pack(S*U*hi(r['relative_to_R23_radius']))))
    refined={(r['mode'],z['cell']):z for r in ordered['mode_rows'] for z in r['refined_cells']}
    byref={r['mode']:r for r in ref['endpoint_rows']};groups={r['path']:r for r in fam['original_column_groups']}
    linear=[[Q(0)]*46 for _ in cells];mode_ledger=[];seen=[]
    for binding in col['column_groups']:
        spelling=binding['path'];wanted=binding['sha256'];g=load(a.notes/Path(spelling).name,wanted)
        check('same_true_group_'+Path(spelling).name,groups[spelling]['sha256']==wanted and groups[spelling]['all213_cells']
              and ref['input_hashes'][spelling]==green['input_hashes'][spelling]==ordered['input_hashes'][spelling]==wanted
              and g['modes']==binding['modes']==groups[spelling]['modes']
              and [r['cell'] for r in g['cell_rows']]==cells)
        for epindex,eprec in enumerate(g['endpoint_rows']):
            m=eprec['mode'];seen.append(m);j=m//2-1
            gainlo,gainhi=lo(eprec['Q_gain']),hi(eprec['Q_gain'])
            check('true_nonzero_height_gain_'+str(m),gainlo>0 or gainhi<0)
            check('reference_height_gain_'+str(m),gainlo==lo(byref[m]['Q_gain']) and gainhi==hi(byref[m]['Q_gain']))
            gain=gainlo if gainlo>0 else -gainhi
            if m in axes:
                ax=axes[m];centre,half=exact(ax['exact_centre']),exact(ax['half_axis'])
                check('same_full_R74_axis_'+str(m),centre==exact(byref[m]['reference_Q']) and
                      exact(ax['lower'])==centre-half and exact(ax['upper'])==centre+half and half==abs(centre)*exact(ax['relative_radius']))
                amplitude=abs(centre)+half
            else:
                amplitude=Q(0);check('all26_zero_reference_heights_'+str(m),exact(byref[m]['reference_Q'])==0)
            for i,n in enumerate(cells):
                lr=g['cell_rows'][i]['linear_rows'][epindex]
                check('mode_cell_order_'+str(n)+'_'+str(m),lr['mode']==m)
                phiQ,phiXi=hi(lr['column_Q_sup'])/gain,hi(lr['column_Xi_sup'])/gain
                rr=refined.get((m,n))
                if rr is not None:phiQ=min(phiQ,hi(rr['refined_phi_Q_sup']));phiXi=min(phiXi,hi(rr['refined_phi_Xi_sup']))
                if n<18:angle=exphi**(2*m)
                else:
                    div,rem=divmod(m*(n-12),4)
                    check('half_dyadic_angle_'+str(n)+'_'+str(m),rem in (0,2))
                    angle=exphi**m*p2(div)*(sqrt2hi if rem else 1)
                linear[i][j]=min(alpha,up(amplitude*angle*((1+m)**3*phiQ+(1+m)*phiXi)/xx[i]))
            mode_ledger.append(dict(mode=m,shallow_height_modulus=pack(amplitude),normalized_true_gain_lower=pack(gain),
                original_group=spelling,original_group_sha256=wanted))
        del g
        print(json.dumps(dict(event='actual_all213_linear_modes',modes=binding['modes'],elapsed_seconds=time.monotonic()-started)),flush=True)
    check('all46_exact_true_columns',seen==modes)
    for i,row in enumerate(rows):
        row['linear_pair_caps_over_reference']=list(map(pack,linear[i]))
        row['linear_common_cap_over_reference']=pack(min(alpha,sum(linear[i],Q(0))))
    A=[]
    for k,nk in enumerate(cells):
        vals=[up(p2(gam)*BB[n]*xx[n]*xx[n]/xx[k]) for n,gam in enumerate(green['gamma_log2_upper'][k])]
        check('positive_all_original_targetsources_'+str(nk),all(v>0 for v in vals))
        oldmap=sum((v*totals[n]**2 for n,v in enumerate(vals)),Q(0))+farhat[k]
        check('unchanged_complete_R74_source_still_inside_'+str(nk),oldmap<originalrho[k])
        A.append(list(map(pack,vals)))
    result=dict(schema='inner-r74-all213-canonical-modal-bootstrap-input-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13',source_sha256=sha(__file__),
        input_identities=identities,gates=gates,all_gates=all(gates.values()),cells=cells,modes=modes,
        rows=rows,A_upper=A,gamma_log2_upper=green['gamma_log2_upper'],linear_mode_ledger=mode_ledger,
        parameter_domain=fam['parameter_domain'],all20_parameter_axes=fam['parameter_axes'],
        strip_formula=green['strip_formula'],
        normalization='Each positive mode is its full cosine/sine pair canonical strong mass e^(m tau_n)[(1+m)^3|Q_m|+(1+m)|Xi_m|], divided by that cell original chosen x_n upper. Source is L1_r W_tau_n of the canonical scalar Xi-source.',
        matrix_formula='A_kn >= 2^gamma_kn B_n x_n^2/x_k; original gamma already includes target (1+m)^3/(1+m) component weights and exp(m(tau_k-tau_n)); no repeated angular-width, Green, Wronskian or frame charge.',
        constants=dict(S=pack(S),alpha=pack(alpha),auxiliary_nonlinear_factor=pack(kA),
            canonical_quadratic='23/288',canonical_full_mean_inverse_remainder='13/16',
            material_integral_factor='1/16',pointwise_physical_factor='1/32',
            e_upper='87/32',e_lower='8/3',dyadic_significant_bits=BITS),
        far_semantics='One positive common low46 far budget per target; it is a valid individual cap but may be summed only once in a common-mass row.',
        auxiliary_domain_only=True,full_inner_head_claimed=False,new_existence_claimed=False,
        old_g_unchanged=True,no_new_ODE_Green_or_source_integral=True,no_Node=True,
        current_strong_q098_q106_g_not_identified_with_this_old_auxiliary=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();payload=gzip.compress(raw,mtime=0)
    if len(payload)>=5_000_000:raise ArithmeticError('Split complete input before exceeding repository per-file cap')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(payload)
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),bytes=len(payload),gates=len(gates),all_gates=True,
        elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
