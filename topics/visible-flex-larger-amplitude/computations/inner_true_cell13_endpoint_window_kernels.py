#!/usr/bin/env python3
"""Complete true cell13 endpoint kernels from its original saved panels.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No ODE, new radial quadrature, source field evaluation or new fixed point.
Both absolute physical and divided-by-true-w endpoint units are explicit.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_split_joint_io_v2 import iter_array, metadata_without_array


PINS = {
    'panels13': ('2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell013.json.gz',
                 '7397ebc436ae5c4cd396ae2e6d5d27c4f2b45e17fae5e75f94eb0acb9e95dc22'),
    'qdensity': ('2026-11-12-tail-r33-plateau2-density-window.json.gz',
                 '0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9'),
    'density': ('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz',
                'e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
    'positive': ('2026-11-12-closure-positive-highband-38.json.gz',
                 'cf293799252e8beb9ef15ff27dba1ebbe698186cee3258b6f9df34ab8dff5600'),
    'ready': ('2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json',
              '563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6'),
}
SOURCE_PINS = {
    'closure_split_joint_io_v2.py': '6cbcb8cf69a39d8df5d10be35a29b941b47fd66456364eb90fab7bbb22b386f0',
    'closure_split_joint_io.py': 'cd03e2fc375e19c8b4d291b601e423a37c584a3e4402957c9f377e82b8cce390',
    'closure_real_head_source_enclosure.py': '97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47',
    'tail_high_two_material_kernel.py': 'eeeed8974da5732759a05004168042d2e84ffc38543e0be175537592295247e1',
}
WINDOWS = [(94,94),(96,96),(98,104),(106,112),(114,128),(130,184),
           (186,192),(194,256),(258,512),(514,1024),(1026,2048),
           (2050,4096),(4098,8190)]
MATERIALS = ('d1', 'd_lambda')


def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:
        return json.load(f)


def exact(v, side='upper'):
    if isinstance(v,list): return F(int(v[0]))*F(2)**int(v[1])
    if isinstance(v,dict):
        if side in v: return exact(v[side],side)
        if 'mantissa' in v: return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
        return F(int(v['numerator']),int(v['denominator']))
    if isinstance(v,float): return F.from_float(v)
    return F(v)


def aq(v):
    f=v if isinstance(v,F) else exact(v)
    return arb(f.numerator)/f.denominator


def ab(v,side='upper'): return aq(exact(v,side))
def ball(v): return ab(v,'lower').union(ab(v,'upper'))


def pack(z,bits=160):
    if not z.is_finite(): raise ArithmeticError('Nonfinite endpoint coefficient')
    t=z.upper()
    if not t>=0: raise ArithmeticError('Negative positive endpoint coefficient')
    if t==0:return ['0',0]
    m,e=t.man_exp();m,e=int(m),int(e);s=max(0,m.bit_length()-bits)
    if s:m,e=(m+(1<<s)-1)>>s,e+s
    out=[str(m),e]
    if not ab(out)>=t:raise ArithmeticError('Endpoint rounding went inward')
    return out


def up(z):return ab(pack(z))


def lower_pack(z):
    t=z.lower()
    if not(t.is_finite() and t>0):raise ArithmeticError('Strict positive endpoint denominator required')
    m,e=t.man_exp()
    return [str(int(m)),int(e)]


class Gates:
    def __init__(self): self.count=0;self.by_name={}
    def check(self,name,condition):
        self.count+=1
        if not condition:raise ArithmeticError(name)
        self.by_name[name]=self.by_name.get(name,0)+1


def closed_port_w(ready,node):
    """The exact original port formula, without constructing RealHead.

    physical node k is the inner port of cell k-1. The old unwarped
    radius ro is used in w=mu/ro^7; actual physical r remains a separate
    interval read from the original saved panel endpoint.
    """
    c=ready['rationalDeepModel']['exactSourceConstants']
    p=ready['rationalDeepModel']['physicalParameters']
    d0,c0=aq(F(c['delta0'])),aq(F(c['etaRatioAtN0']))
    rc,eps=aq(p['rCuff']),aq(p['epsilonScale'])
    n=node-1;delta=d0*arb(2)**(-n);q32=arb(2)**(arb(-3)/2)
    after=3*delta+6*c0*d0*q32**(n+1)/(1-q32)
    ro=rc*(after/arb(12).sqrt()).exp()
    mu=eps*((arb(11)/4)*delta.log()).exp()
    return {'physical_node':node,'normalization_cell':n,'w':mu/ro**7,
            'mu':mu,'old_radius':ro}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--rss-kib',type=int,default=98304)
    args=parser.parse_args();ctx.prec=256;ctx.threads=1
    started=time.monotonic();gates=Gates();check=gates.check
    out=Path(str(args.out_prefix)+'.json')
    if out.exists():raise FileExistsError('Use a fresh immutable endpoint output')
    paths={k:args.inputs/v[0] for k,v in PINS.items()};identities={}
    for k,p in paths.items():
        check('original_input_sha256',sha(p)==PINS[k][1])
        identities[k]={'path':str(p),'sha256':PINS[k][1],'bytes':p.stat().st_size}
    src=Path(__file__).parent
    source_identities={}
    for name,wanted in SOURCE_PINS.items():
        check('frozen_source_sha256',sha(src/name)==wanted)
        source_identities[name]=wanted
    density,qdensity,ready=(read(paths[k]) for k in ('density','qdensity','ready'))
    check('all_original_density_gates',all(density['gates'].values()) and all(qdensity['gates'].values()))
    rows={r['cell']:r for r in density['rows']};qr={r['cell']:r for r in qdensity['rows']}
    meta=metadata_without_array(paths['panels13'],'panels')
    posmeta=metadata_without_array(paths['positive'],'cell_rows')
    matrices=next(r for r in iter_array(paths['positive'],'cell_rows') if r['cell']==13)['positive_cell_matrices']
    check('same_ready_in_positive_geometry',PINS['ready'][1] in posmeta['input_hashes'].values())
    check('same_ready_in_panel_geometry',PINS['ready'][1] in meta['input_hashes'].values())
    check('same_qdensity_in_panel_geometry',PINS['qdensity'][1] in meta['input_hashes'].values())
    check('original_q_strip_in_strong_density',PINS['qdensity'][1] in density['input_hashes'].values())
    n=13;r=rows[n];rnext=rows[n+1];qrow=qr[n]
    check('actual_cell13',meta['cell']==n)
    for key in ('B','tau_inner','tau_outer'):
        check('same_original_full_strip_and_frame',
              exact(meta[key],'lower')==exact(qrow[key],'lower')==exact(r[key],'lower')
              and exact(meta[key])==exact(qrow[key])==exact(r[key]))
    check('nonincreasing_outward_interface_strip',exact(r['tau_inner'])<=exact(rnext['tau_outer'],'lower'))
    for rr in (r,rnext,qrow):
        check('fixed_positive_reference_envelope',
              exact(rr['canonical_total_envelope'],'lower')==exact(rr['canonical_total_envelope'])>0)
    ratio=exact(r['canonical_total_envelope'])/exact(qrow['canonical_total_envelope'])
    S=arb(257)/256;scale=S*aq(ratio)
    B=ball(r['B']);kappa=ball(meta['k'])
    check('strict_original_damping_and_frame',B.lower()>=120 and kappa.lower()>0)
    p=ready['rationalDeepModel']['physicalParameters']
    check('original_port_powers',exact(p['a'])==F(11,4) and exact(p['etaPower'])==F(3,2))
    rc=aq(p['rCuff']);R=rc*257/256;sq12=arb(12).sqrt()
    pin,pout=closed_port_w(ready,14),closed_port_w(ready,13)
    for pp in (pin,pout):
        check('finite_strict_port_w',pp['w'].is_finite() and pp['w'].lower()>0)
    check('cell13_mu_identity',pin['mu'].lower()>=ab(r['mu_lower'],'lower') and pin['mu'].upper()<=ab(r['mu_upper']))
    jump=up(max(arb(1),ab(r['B'])/ab(rnext['B'],'lower')))
    states=[]
    for lo,hi in WINDOWS:
        check('even_complete_window',94<=lo<=hi<=8190 and lo%2==0 and hi%2==0)
        states.append({'lo':lo,'hi':hi,'q':up(max(arb(0),(1-arb(lo)/B).upper())),
                       'G':arb(1),'H':{mat:arb(0) for mat in MATERIALS}})
    first=last=None;last_segment=0;last_x=F(0);count=0;segment_counts=[0]*9
    for panel in iter_array(paths['panels13'],'panels'):
        seg=int(panel['segment']);left,right=(F(*panel[key]) for key in ('x_left','x_right'))
        if seg==last_segment:check('complete_ordered_panel_coverage',left==last_x)
        else:
            check('complete_ordered_panel_coverage',seg==last_segment+1 and last_x==1 and left==0)
            last_segment=seg
        check('strict_panel_interval',0<=left<right<=1 and 0<=seg<=8)
        last_x=right;segment_counts[seg]+=1;count+=1
        if first is None:first=panel
        last=panel
        V,a,w=(ball(panel[key]) for key in ('V','V_over_w','w'))
        mat=ball(panel['material_cV_over_w']);rad=ball(panel['radial_log_increment'])
        variation=ball(panel['log_w_variation']);down=ab(panel['log_w_down_variation'])
        radius=ball(panel['radius'])
        check('complete_positive_material_panel',all(z.is_finite() for z in (V,a,w,mat,rad,variation,down,radius))
              and V.lower()>0 and a.lower()>0 and w.lower()>0 and w.upper()<=arb(1)/2
              and mat.lower()>0 and rad.lower()>0 and variation.lower()>=0 and down>=0)
        check('original_physical_radius_domain',radius.lower()>=rc and radius.upper()<=R)
        Jlo=(mat.lower()/kappa.upper()).lower();Jhi=(mat.upper()/kappa.lower()).upper()
        raw={'d1':up(V.upper()*a.upper()*rad.upper()),
             'd_lambda':up(V.upper()*a.upper()*variation.upper())}
        for st in states:
            lo=st['lo'];growth=up((st['q']*down).exp());prop=up((st['q']*down-lo*Jlo).exp())
            common=up(kappa.upper()*V.upper()*(-(-lo*Jhi).expm1())/lo)
            for matname in MATERIALS:
                st['H'][matname]=up(prop*st['H'][matname]+growth*min(raw[matname],common))
            st['G']=up(prop*st['G'])
        if count%256==0:
            rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            check('owned_RSS_guard',rss<=args.rss_kib)
            print(json.dumps({'event':'complete_cell13_endpoint_panel','panels':count,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':rss}),flush=True)
    check('entire_actual_cell13_1975_panels',count==1975 and last_segment==8 and last_x==1 and all(segment_counts))
    for port,panel in ((pin,first),(pout,last)):
        check('closed_true_w_inside_original_endpoint_panel',
              port['w'].lower()>=ab(panel['w'],'lower') and port['w'].upper()<=ab(panel['w']))
    check('first_and_last_strip_anchors',
          ball(first['tau_left']).contains(ab(r['tau_inner'])) and ball(last['tau_right']).contains(ab(r['tau_outer'])))
    rin,rout=ball(first['radius_left']),ball(last['radius_right'])
    check('actual_endpoint_radius_bounds',rin.lower()>=rc and rout.upper()<=R and rin.upper()<rout.lower())
    win_lo,win_hi=pin['w'].lower(),pin['w'].upper();wout_lo=pout['w'].lower()
    # Cell14's envelope is evaluated at the SAME actual physical boundary.
    Vin=up(S*ab(rnext['canonical_total_envelope'])*
           (ab(rnext['Q_coefficient'])*rin.upper()**3+
            sq12*ab(rnext['mu_upper'])/(rin.lower()**4*win_lo)))
    check('positive_nextcell_boundary_Vprime',Vin>0)
    outrows=[]
    for st in states:
        lo,hi=st['lo'],st['hi'];physical=up(2*jump*st['G']);canonical=None
        covers=[j for j,b in enumerate(posmeta['bands']) if b['first_mode']<=lo and hi<=b['last_mode']]
        chosen=physical;detail=None
        if covers:
            j=covers[0];A=[[ab(x) for x in row] for row in matrices[j]]
            check('actual_positive_canonical_matrix',all(z.is_finite() and z>=0 for row in A for z in row) and A[0][0]>=1 and A[1][1]>=1)
            nulo=arb(lo*lo*(lo*lo-1))/12;nuhi=arb(hi*hi*(hi*hi-1))/12
            cin=[1/(B.lower()*lo*rin.lower()**3),
                 rin.upper()**4*win_hi/(sq12*ab(r['mu_lower'],'lower')*nulo)*max(arb(1),arb(hi)/B.lower())]
            cout=[(B.upper()*hi+hi*hi)*rout.upper()**3,
                  sq12*ab(r['mu_upper'])*nuhi/(rout.lower()**4*wout_lo)]
            drop=(ab(r['tau_inner'],'lower')-ab(r['tau_outer'])).lower()
            check('complete_original_strip_drop',drop>0)
            decay=up((-lo*drop).exp())
            propagated=[up(A[i][0]*cin[0]+A[i][1]*cin[1]) for i in range(2)]
            canonical=up(2*jump*aq(F(1+hi,1+lo))*decay*sum((cout[i]*propagated[i] for i in range(2)),arb(0)))
            chosen=min(physical,canonical)
            detail={'original_matrix_window':[posmeta['bands'][j]['first_mode'],posmeta['bands'][j]['last_mode']],
                    'input_conversion':list(map(pack,cin)),'output_conversion':list(map(pack,cout)),
                    'full_cell_angular_decay':pack(decay),'physical_to_same_cell_canonical_no_crosscell_rho':True}
        kernels={mat:up(2*(1+hi)*scale**2*st['H'][mat]) for mat in MATERIALS}
        row={'cell':13,'input_cell':14,'window':[lo,hi],
             'homogeneous_scalar_factor':pack(st['G']),
             'homogeneous_absolute_strong':{'physical_upper':pack(physical),
                 'canonical_upper':pack(canonical) if canonical is not None else None,
                 'chosen_upper':pack(chosen)},
             'homogeneous_to_relative_strong_upper':pack(chosen/wout_lo),
             'nextcell_Vprime_mass_to_absolute_strong_upper':pack(chosen*Vin),
             'nextcell_Vprime_mass_to_relative_strong_upper':pack(chosen*Vin/wout_lo),
             'source_two_material_to_absolute_strong_upper':{mat:pack(kernels[mat]) for mat in MATERIALS},
             'source_two_material_to_relative_strong_upper':{mat:pack(kernels[mat]/wout_lo) for mat in MATERIALS},
             'source_common_to_absolute_strong_upper':pack(sum(kernels.values(),arb(0))),
             'source_common_to_relative_strong_upper':pack(sum(kernels.values(),arb(0))/wout_lo),
             'canonical_details':detail}
        outrows.append(row)
        check('every_finite_endpoint_and_source_column',all(z.is_finite() and z>=0 for z in [physical,chosen,*kernels.values()]))
    check('13_frequency_windows_cover_94_to_8190',len(outrows)==13 and all(WINDOWS[i][1]+2==WINDOWS[i+1][0] for i in range(12)))
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;check('owned_RSS_guard',rss<=args.rss_kib)
    output={
        'schema':'same-original-inner-cell13-true-endpoint-two-material-window-kernels-v1',
        'author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        'all_gates':True,'gate_count':gates.count,'gates':{k:True for k in gates.by_name},'gate_multiplicities':gates.by_name,
        'input_identities':identities,'source_sha256':sha(__file__),'frozen_reference_source_sha256':source_identities,
        'cell':13,'input_cell':14,'panels':count,'segment_panel_counts':segment_counts,'windows':[list(w) for w in WINDOWS],
        'domain':'The same original inner real geometry, continuous q strip, and strong Vs envelope; no new metric or H family is substituted.',
        'source_units':{'d1':'Vprime^2/(r*w)','d_lambda':'abs(w_r/w)*Vprime^2/w',
                        'source_input':'weak radial-supremum-first pair Fourier mass per material, normalized by that material and the original tau(r)'},
        'output_units':{'absolute_strong':'sum_m (1+|m|) exp(tau13_outer |m|) (|B13 p_m|+|kappa_perp_m|) at the actual node13 endpoint',
                        'relative_strong':'the same absolute strong endpoint mass divided by the true w at node13',
                        'homogeneous_input':'absolute strong physical mass in B14 at node14 and tau14_outer',
                        'nextcell_input':'cell14 strong mass normalized by its original Vprime=(257/256)Vs; all deeper sources/far dependence stay in this input'},
        'common_window_mass_rule':'Use a maximum of the appropriate window columns against a single shared mass, or a positive support function against window caps intersected with that shared mass; never sum independent full copies.',
        'frame_jump_upper':pack(jump),'normalization_S':['257',-8],
        'exact_strong_to_q_Xbar_ratio':[str(ratio.numerator),str(ratio.denominator)],
        'source_scale_squared_upper':pack(scale**2),
        'tau_output':r['tau_outer'],'tau_cell13_inner':r['tau_inner'],'tau_input':rnext['tau_outer'],
        'true_w_in_lower':lower_pack(pin['w']),'true_w_in_upper':pack(pin['w']),
        'true_w_out_lower':lower_pack(pout['w']),'true_w_out_upper':pack(pout['w']),
        'input_physical_radius':{'lower':lower_pack(rin),'upper':pack(rin)},
        'output_physical_radius':{'lower':lower_pack(rout),'upper':pack(rout)},
        'cell14_boundary_Vprime_upper':pack(Vin),
        'port_w_formula':'node k is inner port of cell k-1; w=mu_(k-1)/ro_k^7 with the exact original closed ro and mu formulas; physical r is the saved original panel endpoint',
        'factor_two_retained':True,'all_actual_cell13_source_terms_must_be_paid':True,
        'infinite_band_changed':False,'new_fixedpoint_or_truecut_consistency_claimed':False,
        'new_ODE_or_radial_quadrature_or_Node_calls':0,
        'rows':outrows,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':rss}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'all_gates':True,'gate_count':gates.count,'path':str(out),'sha256':sha(out),'bytes':out.stat().st_size,
                      'elapsed_seconds':output['elapsed_seconds'],'peak_rss_kib':rss,
                      'first_two_display':[{'window':r['window'],'initial_abs':str(ab(r['nextcell_Vprime_mass_to_absolute_strong_upper'])),
                         'source_abs':[str(ab(r['source_two_material_to_absolute_strong_upper'][m])) for m in MATERIALS]} for r in outrows[:2]]}),flush=True)


if __name__=='__main__':main()
