#!/usr/bin/env python3
"""Complete low46 source and exact-support DQ of the R100 reference Cs+Lambda d.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Keeps all46 actual modes, exact complex reflection halves, both physical
radial materials, the mean root, zero numerator mode and full inverse tail.
The existing full-head correction e remains a separate required input.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,arb_poly,ctx


def read(p):
    raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def ab(v):
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    if 'upper' in v:return ab(v['upper'])
    if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
    return arb(int(v['numerator']))/int(v['denominator'])


def bound(v,bits=160):
    if not v.is_finite():raise ArithmeticError('Every source coefficient must be finite')
    t=v.upper()
    if not t>=0:raise ArithmeticError('A positive coefficient upper is negative')
    if t==0:return ['0',0]
    m,e=t.man_exp();m,e=int(m),int(e);shift=max(0,m.bit_length()-bits)
    if shift:m,e=(m+(1<<shift)-1)>>shift,e+shift
    q=arb(m)*arb(2)**e
    if not q>=t:raise ArithmeticError('Outward source rounding failed')
    return [str(m),e]


def upper(v):return ab(bound(v))


def shiftpoly(poly,n):return arb_poly([arb(0)]*n+poly.coeffs())


WINDOWS_IN=[[2,92],[94,94],[96,96],[98,104],[106,112],[114,128],[130,184],[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190],[8192,None]]


def low_DQ(cap,B,tau):
    # Every possible low output2..92 and input2..184 is enumerated. Inputs
    #186up have exactly zero quadratic interaction with centre modes2..92.
    factors={m:upper((-2*m*tau).exp()) for m in range(2,93,2)}
    matrices={name:[] for name in ('d1','d_lambda')}
    for j in range(2,93,2):
        rows={name:[arb(0)]*15 for name in matrices}
        for n in range(2,185,2):
            vals={name:arb(0) for name in matrices}
            terms=[]
            if 2<=j-n<=92:terms.append((j-n,arb(1)))
            if n+j<=92:terms.append((n+j,factors[n]))
            if 2<=n-j<=92:terms.append((n-j,factors[n-j]))
            for k,factor in terms:
                den=4*(1+k)*(1+n)
                bs=arb(5*k*n)/den
                be=max(arb(1),arb(5*k)/(4*B),arb(5*n)/(4*B),arb(5*k*n+1)/(4*B*B))/((1+k)*(1+n))
                if not bs>=be:raise ArithmeticError('Pointwise common-material dominance failed')
                vals['d1']+=cap[k]*bs*factor;vals['d_lambda']+=cap[k]*be*factor
            col=next(i for i,(lo,hi) in enumerate(WINDOWS_IN) if hi is not None and lo<=n<=hi)
            for name in matrices:rows[name][col]=max(rows[name][col],upper(vals[name]))
        for name in matrices:matrices[name].append([bound(z) for z in rows[name]])
    return matrices


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('modal-input','modal-resource','density','out-prefix'):
        ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--first-cell',type=int,default=12);ap.add_argument('--last-cell',type=int,default=224)
    ap.add_argument('--rss-kib',type=int,default=98304)
    a=ap.parse_args();ctx.prec=256;ctx.threads=1;start=time.monotonic()
    summary=Path(str(a.out_prefix)+'-summary.json')
    if summary.exists():raise FileExistsError('Fresh complete inner source output required')
    inp,usage,density=read(a.modal_input),read(a.modal_resource),read(a.density)
    if not(inp['all_gates'] and all(inp['gates'].values()) and usage['exitcode']==0 and usage['termination_signal'] is None
           and inp['cells']==list(range(12,225)) and inp['modes']==list(range(2,93,2))
           and inp['input_identities']['density']['sha256']==sha(a.density)
           and inp['C_S_is_low46_auxiliary'] and inp['C_S_domain_contained_in_R121_R74']):
        raise ArithmeticError('All original true R100 Cs+Lambda input gates and identities required')
    S=ab(inp['R100_envelope_scale'])
    if ex(inp['R100_envelope_scale'])!=F(257,256) or ex(inp['transverse_radius'])!=F(1,32):raise ArithmeticError('Same actual R100 domain required')
    dr={r['cell']:r for r in density['rows']};items=[];records=[];part_paths=[];part_stream=None;part_raw=None;part_count=0
    cells=list(range(a.first_cell,a.last_cell+1))
    if not 12<=a.first_cell<=a.last_cell<=224:raise ValueError('True original cell range required')
    domain_gates=[];finite_gates=[]
    for row in inp['rows']:
        cell=row['cell']
        if cell not in cells:continue
        if part_stream is None:
            part_count+=1;path=Path(str(a.out_prefix)+f'-cells-part{part_count}.jsonl.gz')
            if path.exists():raise FileExistsError('Keep each actual source-cell output immutable')
            part_raw=path.open('wb');part_stream=gzip.GzipFile(filename='',mode='wb',fileobj=part_raw,mtime=0,compresslevel=9)
        Amax=upper(S*ab(dr[cell]['V_over_w_upper']));C=ab(row['Cs_plus_Lambda_common_cap'])
        Bexact=ex(dr[cell]['B']);Bfloor=Bexact.numerator//Bexact.denominator
        if Bfloor<120:raise ArithmeticError('The original balanced physical frame lower bound changed')
        B=arb(Bfloor)
        domain=Amax*C
        if not domain<arb(1)/64:raise ArithmeticError('The complete mean/inverse physical source ball is unpaid')
        domain_gates.append(True)
        cap={m:ab(v) for m,v in zip(inp['modes'],row['Cs_plus_Lambda_pair_caps'])}
        coeff=[arb(0)]*93;weak=[arb(0)]*93;der=[arb(0)]*93
        for k in range(-46,47):
            if not k:continue
            m=2*abs(k);z=upper(cap[m]/2)
            coeff[k+46]=z;weak[k+46]=upper(z/(1+m));der[k+46]=upper(m*z/(1+m))
        W=arb_poly(weak);D=arb_poly(der)
        lin=W+(arb(5)/(4*B))*D
        lead=Amax*lin+arb_poly([arb(0)]*46+[4*C*C*Amax*Amax])
        bs=(arb(5)/4)*(D*D)
        bl=(1+1/(4*B*B))*(W*W)+(arb(5)/(2*B))*(D*W)+(arb(5)/(4*B*B))*(D*D)
        bl+=8*C*C*Amax*shiftpoly(lin,46)+arb_poly([arb(0)]*92+[16*C**4*Amax*Amax])
        # Each resulting common numerator coefficient dominates both actual
        # material numerators, before any radial supremum or inverse product.
        bc=arb_poly([max(bs[k].upper(),bl[k].upper()) for k in range(185)])
        Ln=upper(sum((lead[k].upper() for k in range(93)),arb(0)))
        if not 0<Ln<arb(1)/2:raise ArithmeticError('Positive complete inverse tail denominator required')
        inv=arb_poly([arb(0)]*276+[arb(1)]);term=arb_poly([1])
        for power in range(1,7):
            term=term*lead;inv+=shiftpoly(term,(6-power)*46)
        mats={};tails={};zero={};allpair={}
        for name,num in (('d1',bs),('d_lambda',bl),('common_d',bc)):
            pn=num*inv;Nn=upper(sum((num[k].upper() for k in range(185)),arb(0)))
            tail=upper(Nn*Ln**7/(1-Ln));tails[name]=tail;zero[name]=bound(pn[368])
            pairs=[]
            for m in range(2,737,2):
                val=upper(pn[368+m//2]+pn[368-m//2]);pairs.append(val)
            allpair[name]=pairs
            near=upper(sum(pairs[46:92],arb(0))+tail)
            rest=upper(sum(pairs[92:],arb(0))+tail)
            mats[name]=dict(low2to92=bound(upper(sum(pairs[:46],arb(0))+tail)),near94to184=bound(near),rest186to8190=bound(rest),infinite8192up=bound(tail),shared_complete_inverse_tail=bound(tail),numerator_total=bound(Nn),full_numerator_zero_retained=True)
            finite_gates.append(all(v.is_finite() and v>=0 for v in pairs+[tail]))
        dqlow=low_DQ(cap,B,ab(row['tau_outer_lower']))
        full=dict(cell=cell,source_normalization='d1_prime=V_prime^2/(r*w); d_lambda_prime=abs(w_r/w)*V_prime^2/w; common_d=d1_prime+d_lambda_prime',
            physical_input='same true low46 Cs+Lambda(d), without full-head correction e',
            physical_pair_halves_exact_from_complex_reflection=True,common_field_cap=bound(C),relative_physical_cap=bound(domain),a_max=bound(Amax),B_floor=Bfloor,
            leading_inverse_total=bound(Ln),inverse_polynomial_degree=6,polynomial_support_max736=True,
            complete_mean_and_inverse_retained=True,full_numerator_zero_coefficients=zero,material_bands=mats,
            low_polynomial_pair_rows=[dict(mode=m,**{n:bound(allpair[n][m//2-1]) for n in allpair}) for m in range(2,93,2)],
            low_DQ_input_windows=WINDOWS_IN,low_DQ_two_material_window_kernels=dqlow,
            low_DQ_contract='Per output low mode and each input block, one shared strong pair mass; difference weight exp(-2 min(k,n) tau_outer), all possible n2..184 explicitly enumerated, n186up gives exact zero quadratic interaction. Full Q(e) and T are separate.')
        part_stream.write((json.dumps(full,separators=(',',':'))+'\n').encode())
        items.append(dict(cell=cell,source_common_mass={n:mats[n] for n in mats},relative_physical_cap=bound(domain),leading_inverse_total=bound(Ln)))
        records.append(cell)
        if len(records)%20==0 or cell==cells[-1]:
            part_stream.close();part_raw.close();part_stream=part_raw=None
            if path.stat().st_size>=5_000_000:raise ArithmeticError('Split the complete source-cell packet')
            part_paths.append(dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path),first_cell=records[-min(len(records)%20 or 20,len(records))],last_cell=cell))
            print(json.dumps(dict(event='actual_complete_inner_source',completed=len(records),cell=cell,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned actual Arb source RSS guard exceeded')
    if records!=cells or not all(domain_gates+finite_gates):raise ArithmeticError('The declared complete original source range is missing')
    out=dict(schema='visible-flex-R100-true-low46-reference-complete-source-and-DQ-v2',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
        gates=dict(same_R100_complex_domain=True,all_declared_cells=records==cells,all_relative_physical_domains=all(domain_gates),every_saved_coefficient_finite=all(finite_gates),
            complete_mean_inverse_zero_mode_and_positive_tail=True,all46_low_source_modes_and_low_DQ_support=True,all46_real_lift_inputs_retained=True,exact_reflection_pair_halves=True,original_R100_envelope_and_both_materials=True),
        cells=cells,all213_original_cells=len(cells)==213,output_modes=list(range(2,93,2)),DQ_input_windows=WINDOWS_IN,rows=items,source_parts=part_paths,
        source_applies_to='The true low reference Cs+Lambda(d) on the declared R100 parameter domain',
        full_head_correction_e_still_separate=True,full_high_head_proved=False,complete_head_family_already_exists_in_R100=True,
        inverse_tail_shared_once_in_any_total_frequency_mass=True,source_formula='N=Pi_perp[Q+ell(2c Lambda+c^2)]/(1+c+Lambda), with the exact same true w and complete mean small root',
        Laurent_model='signed mode caps are paired caps/2; W_m=A_m/(1+abs(m)); D_m=abs(m)*W_m; Lambda/a <= W+5D/(4B); source at d1 and d_lambda retained separately',
        input_hashes={str(getattr(a,n)):sha(getattr(a,n)) for n in ('modal_input','modal_resource','density')},source_sha256=sha(__file__),precision_bits=ctx.prec,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    summary.write_text(json.dumps(out,indent=2)+'\n')
    if summary.stat().st_size>=1_000_000:
        packed=summary.with_suffix('.json.gz');packed.write_bytes(gzip.compress(summary.read_bytes(),mtime=0));summary.unlink()
    print(json.dumps(dict(all_gates=True,cells=len(cells),elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
