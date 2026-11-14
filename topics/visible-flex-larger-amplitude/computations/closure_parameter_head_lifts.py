#!/usr/bin/env python3
"""All46 exact-chart shallow-height lifts for R45/R47, without new flows.

Every source/target normalization is explicit.  Completed q panel caps
are converted to the requested envelope by its exact Xbar ratio, and
the entire continuous strip must remain the same q function.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from flint import arb,ctx
from closure_real_head_source_enclosure import power2,ball_record
from closure_real_head_green_enclosure import load_json,ball,endpoint
from closure_assemble_centred_green import compact_upper


def sha(b):return hashlib.sha256(b).hexdigest()


def unpack(x):return arb(int(x[0]))*power2(int(x[1]))


def same(a,b):
    return endpoint(a['lower'])==endpoint(b['lower']) and endpoint(a['upper'])==endpoint(b['upper'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('low','columns','ordered','density','panel-density','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--parameter-z-log2',type=int,default=-2200)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh parameter-lift output')
    docs={};hashes={}
    for name in ('low','columns','ordered','density','panel_density'):
        path=getattr(args,name);docs[name],raw=load_json(path);hashes[str(path)]=sha(raw)
    low=docs['low'];cols=docs['columns'];order=docs['ordered']
    den=docs['density'];panelden=docs['panel_density']
    cells=list(range(12,225));modes=list(range(2,93,2));N=len(cells)
    if low['cells']!=cells or cols['modes']!=modes or low['modes']!=modes or not low['full_range_covered']:
        raise ValueError('The complete true46 chart and full real head are required')
    for name in ('columns','ordered','density'):
        if hashes[str(getattr(args,name))] not in low['input_hashes'].values():raise ValueError('Lift inputs differ from the paid Green ledger: '+name)
    for data in (den,panelden):
        if not all(data['gates'].values()) or [r['cell'] for r in data['rows']]!=cells:raise ValueError('A complete physical domain is unpaid')
    if hashes[str(args.density)]!=hashes[str(args.panel_density)]:
        origin=den.get('continuous_strip_origin',{})
        if origin.get('path')!=str(args.panel_density) or origin.get('sha256')!=hashes[str(args.panel_density)]:
            raise ValueError('The entire continuous strip must be the exact panel-density strip')
    ratios=[]
    for d,q in zip(den['rows'],panelden['rows']):
        for name in ('B','Q_coefficient','mu_lower','mu_upper','tau_inner','tau_outer'):
            if not same(d[name],q[name]):raise ValueError('Real profile or continuous strip endpoint changed')
        x=ball(d['canonical_total_envelope']);xq=ball(q['canonical_total_envelope'])
        if not x.lower()>0 or not xq.lower()>0:raise ValueError('A chosen envelope is nonpositive')
        ratios.append(x/xq)
    panelrows={};panel_hashes={};seen=[]
    for path,wanted in low['panel_hashes'].items():
        d,raw=load_json(Path(path));digest=sha(raw)
        if digest!=wanted or d['modes']!=modes:raise ValueError('A completed full46 panel cap changed')
        if hashes[str(args.panel_density)] not in d['input_hashes'].values():raise ValueError('The physical panel norm differs')
        n=d['cell'];seen.append(n);panel_hashes[path]=digest
        for row in d['rows']:panelrows[(row['mode'],n)]=row
    if sorted(seen)!=list(range(12,24)):raise ValueError('All12 completed shallow cap packages are required')
    refined={(row['mode'],c['cell']):c for row in order['mode_rows'] for c in row['refined_cells']}
    lifts=[[arb(0) for _ in modes] for _ in cells];far=[arb(0) for _ in modes]
    Sf=ball(low['far_scale_S']);group_hashes={}
    if not Sf.lower()>0 or low['far_strip']!=38 or low['far_physical_node']!=225:raise ValueError('The exact R18 evaluation scale differs')
    for gr in cols['column_groups']:
        group,raw=load_json(Path(gr['path']));digest=sha(raw)
        if digest!=gr['sha256']:raise ValueError('A complete true column group changed')
        group_hashes[gr['path']]=digest
        if [r['cell'] for r in group['cell_rows']]!=cells:raise ValueError('A column group omits cells')
        for j,m in enumerate(group['modes']):
            index=m//2-1;e=group['endpoint_rows'][j]
            lo=endpoint(e['Q_gain']['lower']);hi=endpoint(e['Q_gain']['upper'])
            if not(lo>0 or hi<0):raise ArithmeticError('The true normalized shallow-height chart contains zero')
            gain=lo if lo>0 else -hi
            far[index]=((arb(38*m)).exp()/(Sf.lower()*gain)).upper()
            for k,row in enumerate(group['cell_rows']):
                n=row['cell'];lin=row['linear_rows'][j];d=den['rows'][k]
                q=ball(lin['column_Q_sup']).upper()/gain
                xi=ball(lin['column_Xi_sup']).upper()/gain
                cap=refined.get((m,n))
                if cap:
                    q=min(q.upper(),ball(cap['refined_phi_Q_sup']).upper())
                    xi=min(xi.upper(),ball(cap['refined_phi_Xi_sup']).upper())
                X=ball(d['canonical_total_envelope']).lower();B=ball(d['B']).upper()
                a=ball(d['Q_coefficient']).lower();tau=ball(d['tau_inner']).upper()
                angular=(m*tau).exp().upper()
                phip=((1+m)*B*m*q*angular/(X*a)).upper()
                phik=((1+m)*(m*m*q/(X*a)+xi/X)*angular).upper()
                panel=panelrows.get((m,n))
                if panel:
                    phip=min(phip,(ball(panel['phi_physical_p_sup']).upper()/ratios[k].lower()).upper())
                    phik=min(phik,(ball(panel['phi_physical_kappa_sup']).upper()/ratios[k].lower()).upper())
                lifts[k][index]=(phip+phik).upper()
    packed=[[compact_upper(v) for v in row] for row in lifts]
    packed_far=[compact_upper(v) for v in far]
    lifts=[[unpack(v) for v in row] for row in packed]
    far=[unpack(v) for v in packed_far]
    # Choose positive dyadic physical shallow-height units from the
    # independently evaluated far columns.  No parameter direction is zero.
    Z=power2(args.parameter_z_log2);units=[]
    for value in far:
        bound=(Z/value).lower()
        m,e=bound.man_exp();exponent=int(m).bit_length()-1+int(e)
        unit=power2(exponent)
        if not unit>0 or not value*unit<=Z:raise ArithmeticError('The outward far parameter-unit check failed')
        units.append(unit)
    l=[max((lifts[k][j]*units[j]).upper() for j in range(46)) for k in range(N)]
    efar=max((far[j]*units[j]/Z).upper() for j in range(46))
    result=dict(status='Complete46 true parameter lifts and independent far evaluations, no new radial solve; a positive uniform ball still requires a successful full joint input',
        cells=cells,modes=modes,all46_chart_directions=True,
        A_upper=packed,far_E_upper=packed_far,
        compact_number='Each pair is an exact nonnegative dyadic upper [mantissa,binary_exponent]; all parameter units and l constants are computed from THESE stored upward bounds.',
        parameter_units=[ball_record(v) for v in units],parameter_far_scale=ball_record(Z),
        norm='sum_j |a_j|/u_j, where a_j is the full real cosine shallow Q_(2j) increment',
        parameter_cell_lift=[dict(cell=n,l=ball_record(l[k])) for k,n in enumerate(cells)],
        parameter_far_lift=ball_record(efar),
        physical_conversion='Separate radial sup for B*p/V and kappa_perp/V, then sum; the stored full cosine accounts for both signed Fourier halves.',
        input_hashes=hashes,panel_hashes=panel_hashes,group_hashes=group_hashes,
        source_hashes={name:sha(Path(__file__).with_name(name).read_bytes()) for name in
            (Path(__file__).name,'closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py','closure_assemble_centred_green.py')},
        radial_integrations=0,linear_flow_solves=0,actual_uniform_parameter_ball_paid=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(payload)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    args.out.write_bytes(payload)
    print(json.dumps(dict(event='done',output=str(args.out),sha256=sha(payload),bytes=len(payload),
                         seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
