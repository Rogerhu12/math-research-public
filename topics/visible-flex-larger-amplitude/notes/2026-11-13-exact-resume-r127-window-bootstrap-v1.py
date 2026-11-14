#!/usr/bin/env python3
"""Actual finite substitution in the proved R127 field, retaining185 windows.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The complete fixed point already exists. Each individual window cap follows
from its actual equation on the original all-frequency ball; global shared
mass bounds remain simultaneous and must not be replaced by their repeated
per-window copies. No ODE or frequency window is recomputed.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(p):
    raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def rec(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))


def up(v):
    if v<0:raise ArithmeticError('Nonnegative exact kernel required')
    if not v:return F(0)
    unit=F(2)**(v.numerator.bit_length()-v.denominator.bit_length()-96)
    return (v//unit+1)*unit


@lru_cache(maxsize=8192)
def decay(z):
    if z<0:raise ArithmeticError('No negative width difference is free')
    if not z:return F(1)
    d=min(F(1),up(1/(1+z/65536)))
    for _ in range(16):d=min(F(1),up(d*d))
    return d


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('joint','joint-resource','conditional','r126','near','spectral','source','common','balanced','r117-manifest','r120-manifest','out-prefix'):
        ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--window-prefix',type=Path,action='append',required=True)
    a=ap.parse_args();start=time.monotonic();output=Path(str(a.out_prefix)+'.json.gz');summary=Path(str(a.out_prefix)+'-summary.json')
    if output.exists() or summary.exists():raise FileExistsError('Keep the proved field and every new window output immutable')
    joint,usage,conditional,old,near,spectral,source,common,balanced=[read(getattr(a,n)) for n in ('joint','joint_resource','conditional','r126','near','spectral','source','common','balanced')]
    case=next(r for r in common['cases'] if r['high_threshold']==34816)
    identities={Path(r['path']).name:r['sha256'] for n in ('r117_manifest','r120_manifest') for r in read(getattr(a,n))['files']}
    caps=[[ex(v) for v in row] for row in joint['low_mode_radii']];U=[sum(row,F(0)) for row in caps]
    r=[ex(v) for v in joint['finite_radii']];h=[ex(v) for v in joint['high_radii']]
    modes=list(range(2,93,2));parts=old['comparison_partition'];V=[ex(row['V_max']) for row in old['rows']]
    K=F(23,9)+270*F(2)**-34;KT=270*F(2)**-34;B=F(18555);R=ex(old['profile_physical_upper']);S=ex(old['profile_to_V_upper'])
    gates=dict(actual_full1200_fixed_point=joint['all_gates'] and all(joint['gates'].values()) and joint['full_outer_mixed_boundary_fixed_point_claimed'],
        actual_joint_formal_exit_zero=usage['exitcode']==0 and usage['termination_signal'] is None,
        exact_conditional_identity=joint['inputs']['conditional_nonlow']['sha256']==sha(a.conditional),
        exact_original_R126_identity=joint['inputs']['joint']['sha256']==sha(a.r126),
        all1150_actual_low_mode_radii=caps==[[ex(v) for v in row] for row in conditional['low_mode_radii']],
        all50_actual_nonlow_radii=r==[ex(row['finite_radius']) for row in conditional['rows']] and h==[ex(row['high_radius']) for row in conditional['rows']],
        same_genuine_common_strip=case==old['fixed_common_strip']==near['common_strip'] and common['all_identity_gates'],
        full_same_centre_source=source['all_gates'] and all(source['gates'].values()) and spectral['all_gates'] and source['constant_strip']=='18/125',
        exact_low_source_identity=any(Path(k).name==a.spectral.name and v==sha(a.spectral) for k,v in source['input_hashes'].items()),
        all25_complete_original_blocks=len(parts)==25 and sum(p['panels'] for p in parts)==10793,
        unchanged_complete_Hessian=K==ex(old['full_complete_Hessian_upper']),
        all25_full_mean_and_inverse_domains=all((10+U[j]+r[j])*V[j]+h[j]*(R if j==21 else B if j==5 else V[j])<F(2)**-34 for j in range(25)))
    if not all(gates.values()):raise ArithmeticError(str(gates))
    sigma=[ex(v) for v in near['source_block_sigma_max']];tau=F(18,125)
    ac={row['mode']:ex(row['upper']) for row in spectral['field_caps']}
    centre=[{n:up(ac[n]*decay(n*(tau-sigma[j]))) for n in modes} for j in range(25)]
    psource={row['mode']:up(ex(row['polynomial_pair_mass'])) for row in source['polynomial_pair_rows']}
    tail=up(ex(source['shared_complete_inverse_tail']))
    headm=[ex(v) for v in old['actual_R100_head_band_masses']]
    delta=ex(balanced['exact_head_to_output_strip_gap_lower']);Bcut=ex(balanced['balanced_B_lower'])
    extras=[ex(row['extra_start']) for row in case['blocks']];ends=[ex(row['extra_end']) for row in case['blocks']]
    allwindows=[];hashes={};kernel_files=[];display=[]
    for pi,prefix in enumerate(a.window_prefix):
        primary=Path(str(prefix)+'-windows.jsonl.gz');meta_path=Path(str(prefix)+'.json');resource_path=Path(str(prefix)+'-resource.json')
        meta,ru=read(meta_path),read(resource_path)
        if not(meta['all_enclosure_gates'] and meta['primary']['sha256']==sha(primary)==identities[primary.name]
               and meta['comparison_partition']==parts and meta['precision']>=256 and ru['exitcode']==0 and ru['termination_signal'] is None
               and meta['source_powers']==[2,1,0] and meta['original_leaf_count_per_window']==10793):
            raise ArithmeticError('A complete original185 window input changed')
        hashes.update({str(p):sha(p) for p in (primary,meta_path,resource_path)})
        kout=Path(str(a.out_prefix)+f'-kernels-part{pi+1}.jsonl.gz')
        if kout.exists():raise FileExistsError('Fresh exact kernel stream required')
        seen=[]
        with kout.open('wb') as raw:
            with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=9) as packed:
                with gzip.open(primary,'rt') as stream:
                    for line in stream:
                        win=json.loads(line);lo,hi=win['window'];seen.append([lo,hi]);oldstrip=hi<=5758
                        bi=0 if hi<=184 else 1 if hi<=8190 else 2
                        if not(win['all10793_original_leaves'] and win['all18_original_source_segments_retained'] and win['all3_source_materials']
                               and win['both_initial_columns_retained'] and win['comparison_source_origins']==25 and win['entry_count']==win['exit_count']==1
                               and win['frame_jump_count']==1804 and len(win['rows'])==25):raise ArithmeticError('A whole-leaf frequency interface was omitted')
                        poly=[up(sum((psource[m]*decay(m*(tau-sigma[j])) for m in range(lo,min(hi,736)+1,2)),F(0))) for j in range(25)]
                        ct=[up(poly[j]+tail*decay(lo*(tau-sigma[j]))) for j in range(25)]
                        lowq=[]
                        for j in range(25):
                            value=F(0)
                            if lo<=184:
                                for ni,n in enumerate(modes):
                                    for ki,k in enumerate(modes):
                                        if lo<=k+n<=hi:
                                            alpha=F(5*k*n+1,4*(1+k)*(1+n))
                                            value+=alpha*(centre[j][k]*caps[j][ni]+caps[j][ki]*caps[j][ni]/2)
                            lowq.append(up(value))
                        lowt=[up(KT*(10*u+u*u/2)) for u in U]
                        rows=[];outrows=[]
                        for i,row in enumerate(win['rows']):
                            if row['comparison_block']!=i or ex(row['V_max'])!=V[i] or len(row['source_rows'])!=i+1:raise ValueError('Same actual25 target blocks required')
                            cols=row['initial_localV_separate_component_sups']
                            hg=up(max(sum(map(ex,cols[0]),F(0))/Bcut,sum(map(ex,cols[1]),F(0)))*decay(lo*(delta+(extras[i] if oldstrip else F(0)))))
                            gh={p:[] for p in (2,1,0)}
                            cf=qf=tf=nf=F(0)
                            for j,srow in enumerate(row['source_rows']):
                                if srow['source_comparison_block']!=j or [d['V_power'] for d in srow['density_rows']]!=[2,1,0]:raise ValueError('All true source materials required')
                                factor=decay(lo*max(F(0),extras[i]-ends[j])) if oldstrip and j<i else F(1)
                                for density in srow['density_rows']:
                                    p=density['V_power'];gh[p].append(up(max(ex(density['localV_strong_output_row']),ex(density['P_sup'])+ex(density['K_sup']))*factor))
                                g=gh[2][j]
                                if j==21:
                                    gc=min(S*g,R*gh[1][j]);gs=min(S*S*g,S*R*gh[1][j],R*R*gh[0][j])
                                elif j==5:gc=B*gh[1][j];gs=B*B*gh[0][j]
                                else:gc=gs=g
                                C=10+U[j]
                                cf+=g*ct[j];qf+=g*lowq[j];tf+=g*lowt[j]
                                nf+=K*(g*(C*r[j]+r[j]*r[j]/2)+gc*(C+r[j])*h[j]+gs*h[j]*h[j]/2)
                            head=hg*headm[bi];image=head+cf+qf+tf+nf;cap=min(r[i],up(image))
                            outrows.append(dict(target_block=i,actual_window_mass_upper=rec(cap),untrimmed_equation_upper=rec(up(image)),
                                true_head_upper=rec(up(head)),complete_fixed_centre_upper=rec(up(cf)),pure_low_Q_upper=rec(up(qf)),pure_low_complete_T_upper=rec(up(tf)),complete_nonlow_feedback_upper=rec(up(nf)),global_all_middle_radius=rec(r[i])))
                            rows.append(dict(target_block=i,head_gain=rec(hg),three_materials={str(p):[rec(v) for v in gh[p]] for p in (2,1,0)}))
                        allwindows.append(dict(window=[lo,hi],head_band=bi,whole_window_mass_not_per_mode_sum=True,rows=outrows))
                        packed.write((json.dumps(dict(window=[lo,hi],common_strip_already_paid=True,head_band=bi,rows=rows),separators=(',',':'))+'\n').encode())
                        display.append(dict(window=[lo,hi],block23=float(ex(outrows[23]['actual_window_mass_upper'])),head23=float(ex(outrows[23]['true_head_upper']))))
                if seen!=meta['windows']:raise ArithmeticError('The actual complete window inventory differs from its manifest')
        if kout.stat().st_size>=5_000_000:raise ArithmeticError('Split exact derived kernels before archiving')
        kernel_files.append(dict(path=str(kout),bytes=kout.stat().st_size,sha256=sha(kout),windows=seen))
        print(json.dumps(dict(event='complete_actual_window_part',part=pi+1,windows=len(seen),seconds=time.monotonic()-start)),flush=True)
    allwindows.sort(key=lambda w:w['window']);coverage=[m for w in allwindows for m in range(w['window'][0],w['window'][1]+1,2)]
    gates['all185_actual_windows_and17361_positive_modes']=len(allwindows)==185 and coverage==list(range(94,34816,2))
    if not all(gates.values()):raise ArithmeticError(str(gates))
    result=dict(schema='visible-flex-R127-actual185-window-field-bootstrap-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates=gates,
        same_existing_full_outer_fixed_point=True,parameter_cut_closed=False,closed_surface_claimed=False,actual_finite_substitutions=1,
        comparison_partition=parts,common_strip=case,source_block_sigma_max=[rec(v) for v in sigma],windows=allwindows,
        retained_global_middle_mass_radii=[rec(v) for v in r],retained_global_high_mass_radii=[rec(v) for v in h],
        repeated_window_tail_bounds_are_not_a_new_shared_mass=True,all_complete_mean_inverse_and_source_materials_retained=True,
        actual_head_unchanged='Same complete R1001/32 three-band values; individual true head spectrum not yet sharpened',
        derived_kernel_parts=kernel_files,input_hashes={**hashes,**{str(getattr(a,n)):sha(getattr(a,n)) for n in ('joint','joint_resource','conditional','r126','near','spectral','source','common','balanced','r117_manifest','r120_manifest')}},
        source_sha256=sha(__file__),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=9) as packed:packed.write((json.dumps(result,separators=(',',':'))+'\n').encode())
    if output.stat().st_size>=5_000_000:raise ArithmeticError('Partition the185 actual window bounds')
    short={k:v for k,v in result.items() if k not in ('windows','retained_global_middle_mass_radii','retained_global_high_mass_radii')}
    short['primary']=dict(path=str(output),bytes=output.stat().st_size,sha256=sha(output));short['block23_largest10']=sorted(display,key=lambda v:v['block23'],reverse=True)[:10]
    summary.write_text(json.dumps(short,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,windows=185,largest=short['block23_largest10'],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
