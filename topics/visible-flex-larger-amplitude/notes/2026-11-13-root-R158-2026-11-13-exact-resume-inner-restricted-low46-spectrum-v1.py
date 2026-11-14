#!/usr/bin/env python3
"""Same-field restricted low46 error spectra with complete Q/T/far source.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No new existence is asserted: every step intersects an existing solution's
caps with its complete source image. Cs and Lambda are kept distinct.
"""
import argparse,gc,gzip,hashlib,json,resource,sys,time
from pathlib import Path
from flint import arb,arb_poly,ctx,fmpq as Q

MODES=list(range(2,93,2))
WINDOWS=[[94,94],[96,96],[98,104],[106,112],[114,128],[130,184],
         [186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    with (gzip.open(path,'rt') if path.suffix=='.gz' else path.open()) as f:return json.load(f)


def ab(v):
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    if 'upper' in v:return ab(v['upper'])
    if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
    return arb(int(v['numerator']))/int(v['denominator'])


def exact(v):
    if isinstance(v,list):return Q(int(v[0]))*Q(2)**int(v[1])
    if 'upper' in v:return exact(v['upper'])
    if 'mantissa' in v:return Q(int(v['mantissa']))*Q(2)**int(v['binary_exponent'])
    return Q(int(v['numerator']),int(v['denominator']))


def pack(z,bits=160):
    if not z.is_finite():raise ArithmeticError('Nonfinite complete modal budget')
    z=z.upper()
    if not z>=0:raise ArithmeticError('Positive modal budget became negative')
    if z==0:return ['0',0]
    m,e=z.man_exp();m,e=int(m),int(e);shift=max(0,m.bit_length()-bits)
    if shift:m,e=(m+(1<<shift)-1)>>shift,e+shift
    out=[str(m),e]
    if not ab(out)>=z:raise ArithmeticError('Modal outward serialization')
    return out


def up(z):return ab(pack(z))


def order(weights):return sorted(range(len(weights)),key=lambda i:exact(pack(weights[i])),reverse=True)


def support(weights,caps,mass,indices):
    total=arb(0);remaining=mass
    for i in indices:
        take=min(remaining,caps[i]);total+=weights[i]*take
        remaining=up(max(arb(0),(remaining-take).upper()))
        if remaining==0:break
    return min(up(total),up(max(weights)*mass),up(sum((c*w for c,w in zip(caps,weights)),arb(0))))


def successful(r):return r.get('exitcode',r.get('exit_code'))==0 and r.get('termination_signal') is None


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('topic','modal-input','modal-resource','field641','field641-resource','window-field','window-resource','mode-kernels','kernel-resource','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--steps',type=int,default=32);p.add_argument('--rss-kib',type=int,default=98304)
    p.add_argument('--previous-low-field',type=Path);p.add_argument('--previous-low-resource',type=Path)
    a=p.parse_args();ctx.prec=256;ctx.threads=1;t0=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Preserve every actual low46 finite substitution')
    if not 1<=a.steps<=256:raise ValueError('A finite positive step count is required')
    counts={};ids={}
    def check(name,value):
        if not value:raise ArithmeticError('Low46 spectral gate: '+name)
        counts[name]=counts.get(name,0)+1
    for key in ('modal_input','modal_resource','field641','field641_resource','window_field','window_resource','mode_kernels','kernel_resource'):
        path=getattr(a,key);ids[key]=dict(path=str(path),sha256=sha(path))
    for key in ('modal_resource','field641_resource','window_resource','kernel_resource'):check('formal_input_success',successful(read(getattr(a,key))))
    modal=read(a.modal_input);domain=modal['domain'];f641=read(a.field641);window=read(a.window_field);kg=read(a.mode_kernels)
    for obj in (modal,f641,window,kg):check('complete_actual_input',obj['all_gates'] and all(obj['gates'].values()))
    check('exact_restricted_domain',modal['schema']=='inner-R100-Cs-Lambda-restricted-profile-modal-input-v1' and modal['domain']==f641['domain']==window['domain'])
    check('same_reference_in_window',window['input_identities']['modal_input']['sha256']==sha(a.modal_input))
    check('same_actual641_field',window['input_identities']['field']['sha256']==sha(a.field641))
    check('complete_kernel_contract',kg['schema']=='same-R100-inner-low46-factored-field-kernels-v1' and kg['modes']==MODES and kg['cells']==list(range(12,225)))
    check('complete_source_material_S_scale',exact(kg['S'])==Q(257,256) and kg['nonlinear_constants_or_complete_source_not_preinserted'])
    check('all_factor_vertices_within_original_common',kg['factor_vertices_exceeding_old_common_before_min']==0)
    check('original_full_mode_quadratic_support',window['windows']==WINDOWS and modal['modes']==MODES)
    sys.path.insert(0,str(a.topic/'computations'))
    from closure_split_joint_io_v2 import iter_array
    density_path=a.topic/'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz'
    jacobian_path=a.topic/'notes/2026-11-12-closure-strong-parameter-jacobian-r1.json.gz'
    check('same_original_density_pin',sha(density_path)=='e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700')
    check('same_original_complete_Jbar_pin',sha(jacobian_path)=='7b9d5f6bafe69879246ee5edffbfdd280bfec0b5207c5ea6f79959fc3b61dfc4')
    ids['density']=dict(path=str(density_path),sha256=sha(density_path));ids['jacobian']=dict(path=str(jacobian_path),sha256=sha(jacobian_path))
    density=read(density_path);S=arb(257)/256;Theta=arb(16705)/16384
    aa=[up(S*ab(r['V_over_w_upper'])) for r in density['rows']]
    mode_kernel_parts=kg['mode_kernel_parts'];del kg['common_field_matrix'];del kg;gc.collect()
    factors=[];part_pins=[]
    for entry in mode_kernel_parts:
        path=Path(entry['path']);check('exact_mode_kernel_part_pin',sha(path)==entry['sha256']);part_pins.append(entry)
        for row in iter_array(path,'rows'):
            check('all46_original_factor_mode_order',row['mode']==MODES[len(factors)])
            fields={name:list(map(ab,row[name])) for name in ('phi_target','psi_target','mu_ratio','phi_source','psi_source','ordered_diagonal')}
            check('complete213_mode_factor_rows',all(len(v)==213 and all(x.is_finite() and x>0 for x in v) for v in fields.values()))
            factors.append(fields)
    check('complete46_mode_kernel_coverage',len(factors)==46)
    old_common=[ab(r['fixed_low_cap']) for r in window['rows']]
    caps=[[z for _ in MODES] for z in old_common]
    near_caps=[list(map(ab,r['window_caps'][:6])) for r in window['rows']]
    high_common=[list(map(ab,r['near_rest_common_caps'])) for r in window['rows']]
    infinite=ab(window['complete_infinite_cap']);far=ab(window['fixed_far_cap'])
    check('positive_complete_infinite_and_far',infinite>0 and far>0)
    W=list(map(ab,f641['same_original_metric_weights']));far_readout=[arb(0)]*213
    for row in iter_array(jacobian_path,'rows'):
        k=row['index']
        if k>=213:continue
        for j,m,e in row['coefficients']:
            if j==640:far_readout[k]=up(W[k]*Theta*ab([m,e])*far/W[640])
    if a.previous_low_field:
        check('previous_low_resource_required',a.previous_low_resource is not None and successful(read(a.previous_low_resource)))
        previous=read(a.previous_low_field)
        check('same_previous_low_domain',previous['all_gates'] and previous['domain']==modal['domain'] and previous['input_identities']['modal_input']['sha256']==sha(a.modal_input))
        ids['previous_low_field']=dict(path=str(a.previous_low_field),sha256=sha(a.previous_low_field));ids['previous_low_resource']=dict(path=str(a.previous_low_resource),sha256=sha(a.previous_low_resource))
        for n,row in enumerate(previous['rows']):
            check('previous_low_all46_cells',row['cell']==n+12 and len(row['low_mode_caps'])==46)
            caps[n]=[min(caps[n][j],ab(z)) for j,z in enumerate(row['low_mode_caps'])]
            old_common[n]=min(old_common[n],ab(row['low_common_cap']))
        del previous
    cs=[];lamb=[];cscommon=[];lamcommon=[];cp=[];rcp=[];rho=[];high_coeff=[];high_order=[]
    for n,row in enumerate(modal['rows']):
        check('all213_actual_modal_rows',row['cell']==n+12)
        c=list(map(ab,row['Cs_complete_pair_caps']));la=list(map(ab,row['Lambda_pair_caps_on_domain']))
        cs.append(c);lamb.append(la);cscommon.append(ab(row['Cs_common_cap']));lamcommon.append(ab(row['Lambda_common_cap_on_domain']))
        tau=ab(row['tau_outer_lower']);rr=[up((-2*m*tau).exp()) for m in MODES];rho.append(rr)
        derived=[up(m*c[j]/(1+m)) for j,m in enumerate(MODES)]
        cp.append(arb_poly([arb(0)]+derived));rcp.append(arb_poly(list(reversed([arb(0)]+[up(z*r) for z,r in zip(derived,rr)]))))
        h=[];ho=[]
        for m in MODES:
            coeff=[]
            for lower,upper in WINDOWS[:6]:
                values=[]
                for source_mode in range(lower,upper+1,2):
                    k=source_mode-m
                    if 2<=k<=92:
                        values.append(up(c[k//2-1]*arb(5*k*source_mode)/(4*(1+k)*(1+source_mode))*rr[k//2-1]))
                coeff.append(max(values) if values else arb(0))
            h.append(coeff);ho.append(order(coeff))
        high_coeff.append(h);high_order.append(ho)
    del modal,density,window,f641,W;gc.collect()
    def low_common(n):return min(old_common[n],up(sum(caps[n],arb(0))))
    def sources(save=False):
        all_sources=[];records=[]
        for n in range(213):
            lo=low_common(n);t=up(lo+high_common[n][0]+high_common[n][1]+infinite);v=up(lamcommon[n]+t);C=cscommon[n]
            check('complete_physical_Hessian_domain',v<arb(2)**-30 and aa[n]*(C+v)<arb(1)/128)
            qtail=up(arb(23)*v*v/18);ttail=up(270*aa[n]*(C+v)*(C*v+v*v/2))
            vv=[up(lamb[n][j]+caps[n][j]) for j in range(46)]
            derived=[up(m*vv[j]/(1+m)) for j,m in enumerate(MODES)]
            vp=arb_poly([arb(0)]+derived)
            rvp=arb_poly(list(reversed([arb(0)]+[up(z*r) for z,r in zip(derived,rho[n])])))
            sums=cp[n]*vp;diff1=rcp[n]*vp;diff2=cp[n]*rvp
            common_dq=up((arb(23)/9)*C*up(lamcommon[n]+lo))
            dqlow=[];dqhigh=[];src=[]
            for j in range(1,47):
                linear=min(up(arb(5)/4*(sums[j]+diff1[46+j]+diff2[46+j])),common_dq)
                high=support(high_coeff[n][j-1],near_caps[n],high_common[n][0],high_order[n][j-1])
                value=up(linear+high+qtail+ttail)
                check('every_complete_source_finite_positive',value.is_finite() and value>0)
                dqlow.append(linear);dqhigh.append(high);src.append(value)
            all_sources.append(src)
            if save:records.append(dict(cell=n+12,DQ_Cs_Lambda_plus_low=list(map(pack,dqlow)),DQ_Cs_near_difference=list(map(pack,dqhigh)),
                complete_Q_Lambda_plus_all_e=pack(qtail),complete_mean_inverse_T_difference=pack(ttail),
                total_low_sources=list(map(pack,src)),low_common_cap=pack(lo),lambda_plus_all_error_common=pack(v)))
        return all_sources,records
    checkpoints=[]
    def snapshot(step):
        checkpoints.append(dict(step=step,cell12_modes=list(map(pack,caps[0])),cell13_modes=list(map(pack,caps[1])),cell12_low_common=pack(low_common(0))))
        print(json.dumps(dict(event='same_existing_restricted_low46_finite_step',step=step,cell12_mode92=str(caps[0][-1]),cell13_mode92=str(caps[1][-1]),cell12_low_common=str(low_common(0)),elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    snapshot(0)
    for step in range(1,a.steps+1):
        src,_=sources();nxt=[[z for z in row] for row in caps]
        for j,f in enumerate(factors):
            prefix=[arb(0)]*213;suffix=[arb(0)]*213;acc=arb(0)
            for n in range(213):
                prefix[n]=up(acc);acc+=f['mu_ratio'][n]*f['psi_source'][n]*src[n][j]
            acc=arb(0)
            for n in range(212,-1,-1):
                suffix[n]=up(acc);acc+=f['mu_ratio'][n]*f['phi_source'][n]*src[n][j]
            for k in range(213):
                image=up(f['phi_target'][k]*prefix[k]+f['psi_target'][k]*suffix[k]+f['ordered_diagonal'][k]*src[k][j]+far_readout[k])
                nxt[k][j]=min(caps[k][j],image)
                check('every_mode_monotone_finite_step',nxt[k][j].is_finite() and 0<nxt[k][j]<=caps[k][j])
        caps=nxt
        if step&(step-1)==0 or step==a.steps:snapshot(step)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned low46 spectral RSS guard')
    _,final_sources=sources(save=True)
    result=dict(schema='same-R100-restricted-low46-spectral-error-finite-bootstrap-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,
      input_identities=ids,mode_kernel_parts=part_pins,source_sha256=sha(__file__),domain=domain,steps=a.steps,modes=MODES,cells=list(range(12,225)),
      rows=[dict(cell=n+12,low_mode_caps=list(map(pack,caps[n])),low_common_cap=pack(low_common(n)),original_valid_common_cap=pack(old_common[n]),complete_original_far_readout=pack(far_readout[n])) for n in range(213)],
      final_complete_source_rows=final_sources,checkpoints=checkpoints,fixed_far_cap=pack(far),fixed_complete_infinite_cap=pack(infinite),
      source_identity='e_low=G_low[N(Cs+Lambda+e)-N(Cs)]+original complete far difference. DQ(Cs)(Lambda+e) uses all low modes and near difference support; full Q(Lambda+e) and full mean/inverse T are never projected by finite support.',
      convolution_identity='c_k=Cs_(2k)*2k/(1+2k),v_n=(Lambda+e)_(2n)*2n/(1+2n),rho_k=exp(-4k*tau_outer); DQ_low_(2j)<=5/4*((c*v)_j+sum_k c_k*rho_k*v_(k+j)+sum_n c_(n+j)*v_n*rho_n).',
      source_material='Vprime^2/(r*w)+abs(w_r/w)*Vprime^2/w',field_norm='original continuous-strip strong full Fourier pair (B p,kappa)/Vprime',
      complete_mean_inverse_far_and_infinite_retained=True,no_new_ODE_or_source_integral=True,new_fixedpoint_or_full_parameter_cut_claimed=False,
      elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    if out.stat().st_size>5_000_000:raise ArithmeticError('Split actual low-mode spectrum artifact')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned low46 final RSS guard')
    print(json.dumps(dict(path=str(out),sha256=sha(out),bytes=out.stat().st_size,all_gates=True,gate_count=result['gate_count'],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
