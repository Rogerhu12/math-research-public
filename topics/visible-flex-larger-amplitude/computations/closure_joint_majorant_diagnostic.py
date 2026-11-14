#!/usr/bin/env python3
"""Lightweight FLOAT diagnostic of the failed positive majorant, not a proof.

Stream the large middle rows, retain only logarithms, and compare several
rho choices without another Arb matrix inverse.  Spectral values, inverse
signs and dropped underflows are explicitly numerical diagnostics.  No
joint mathematical gate is paid by this program.
"""
import argparse,gzip,hashlib,json,math,resource,time
from pathlib import Path
import numpy as np


def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for part in iter(lambda:f.read(1024*1024),b''):h.update(part)
    return h.hexdigest()


def read(path):
    with (gzip.open(path,'rt') if path.suffix=='.gz' else path.open()) as f:return json.load(f)


def iter_array(path,key):
    """Stream one generated JSON array by decoding one element at a time."""
    needle='"'+key+'"';decoder=json.JSONDecoder();buf=''
    with (gzip.open(path,'rt') if path.suffix=='.gz' else path.open()) as f:
        while True:
            more=f.read(65536)
            if not more:raise ValueError('Array field not found: '+key)
            buf+=more;at=buf.find(needle)
            if at>=0:
                tail=buf[at+len(needle):].lstrip()
                if tail.startswith(':'):
                    tail=tail[1:].lstrip()
                    if tail.startswith('['):buf=tail[1:];break
            buf=buf[-256:]
        while True:
            buf=buf.lstrip()
            if buf.startswith(','):buf=buf[1:].lstrip()
            if buf.startswith(']'):return
            try:obj,end=decoder.raw_decode(buf)
            except json.JSONDecodeError:
                more=f.read(65536)
                if not more:raise ValueError('Incomplete generated JSON array')
                buf+=more;continue
            yield obj;buf=buf[end:]


def lp(v):
    m,e=int(v[0]),int(v[1])
    return math.log2(m)+e if m>0 else -math.inf


def lr(v):return lp([v['upper']['mantissa'],v['upper']['binary_exponent']])


def la(*values):
    result=-math.inf
    for value in values:result=float(np.logaddexp2(result,value))
    return result


def exponent_text(s):
    if not isinstance(s,str) or not s.startswith('2^'):raise ValueError('Expected an exact dyadic label')
    return int(s[2:])


def logsum_rows(a):
    mx=np.max(a,axis=1)
    return mx+np.log2(np.exp2(a-mx[:,None]).sum(axis=1))


def label(i,N=213):return {'cell':i+12} if i<N else {'block':'far_z'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('low','high','density','out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--rho-log2',default='-30,-60,-90,-120,linear')
    args=p.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh diagnostic prefix')
    hashes={str(getattr(args,n)):digest(getattr(args,n)) for n in ('low','high','density')}
    low=read(args.low);N=213;dim=N+1
    if low['cells']!=list(range(12,225)) or low['modes']!=list(range(2,93,2)):raise ValueError('Need the complete exact low data')
    G={name:np.array([[lp(v) for v in row] for row in low['gamma_upper'][name]],dtype=float)
       for name in ('main','corr','base','remainder')}
    F={name:np.array([lp(v) for v in low['far_z_source_upper'][name]],dtype=float) for name in G}
    blog=np.array([lr(r['B_low']) for r in low['rows']],dtype=float)
    eblog=lr(low['E_B_low']);cdlog=exponent_text(low['raw_D_constant'])
    low_witnesses=[r.get('families',{}) for r in low['rows']]
    if hashes[str(args.density)] not in low['input_hashes'].values():raise ValueError('Low physical domain changed')
    del low
    high=read(args.high);zlog=high['z_log2'];middle=Path(high['gamma_source'])
    if hashes[str(args.density)] not in high['input_hashes'].values():raise ValueError('High physical domain changed')
    mh=digest(middle);hashes[str(middle)]=mh
    if mh not in high['input_hashes'].values():raise ValueError('Middle causal source changed')
    pure=np.array([lr(r['pure_low_residual']) for r in high['rows']],dtype=float)
    far=np.array([lr(r['far_boundary']) for r in high['rows']],dtype=float)
    deep=lr(high['deep_high_boundary']);pureinf=lr(high['pure_low_infinite_residual'])
    H=np.full((N,N),-np.inf,dtype=float);count=0;row_count=0
    for row in iter_array(middle,'gamma_rows'):
        k=row['output_cell']-12
        if k!=row_count:raise ValueError('The actual high row order differs')
        for src in row['sources']:
            n=src['source_cell']-12
            if not 0<=k<=n<N:raise ValueError('The high causal source order differs')
            H[k,n]=lr(src['gamma']);count+=1
        row_count+=1
    if count!=N*(N+1)//2 or row_count!=N:raise ValueError('The high triangle is incomplete')
    density=read(args.density)
    A=np.array([lr(r['V_over_w_upper']) for r in density['rows']],dtype=float)
    gamma=lr(density['gamma_high']);del density
    beta=blog+2+cdlog+2*zlog;betaz=eblog+2+cdlog+zlog
    b=np.full(dim,-np.inf);b[:N]=np.logaddexp2(np.logaddexp2(pure,far),la(pureinf,deep))
    scenarios=[]
    for choice in args.rho_log2.split(','):
        rho=0.0 if choice=='linear' else math.exp2(int(choice))
        rlog=-math.inf if rho==0 else math.log2(rho)
        plus=math.log2(1+rho)
        Lparts=dict(main=G['main'],corr=G['corr']+math.log2(3),
                    rho_base=G['base']+math.log2(3)+rlog,
                    remainder=G['remainder']+math.log2(216)+2*plus)
        L=np.logaddexp2(np.logaddexp2(Lparts['main'],Lparts['corr']),
                        np.logaddexp2(Lparts['rho_base'],Lparts['remainder']))
        slopes=np.logaddexp2(math.log2(3)+plus,math.log2(216)+A+2*plus)
        HC=H+slopes[None,:];IC=gamma+slopes
        fl=np.logaddexp2(np.logaddexp2(F['main'],F['corr']+math.log2(3)),
                         np.logaddexp2(F['base']+math.log2(3)+rlog,F['remainder']+math.log2(216)+2*plus))-zlog
        R=np.full((dim,dim),-np.inf)
        R[:N,:N]=np.logaddexp2(np.logaddexp2(L,HC),IC[None,:])
        R[:N,N]=np.logaddexp2(np.logaddexp2(beta,far+2),deep+2)
        R[N,:N]=fl;R[N,N]=betaz
        x=np.zeros(dim);history=[]
        for it in range(64):
            y=logsum_rows(R+x[None,:]);ratios=y-x
            if it in (0,1,3,7,15,31,63):history.append(dict(iteration=it+1,
                collatz_log2_lower_float=float(np.min(ratios)),collatz_log2_upper_float=float(np.max(ratios))))
            x=y-float(np.max(y))
        scale=np.floor(x);exponents=R+scale[None,:]-scale[:,None]
        underflows=np.isneginf(exponents)|(exponents < -1074)
        if np.max(exponents)>1000:
            scenarios.append(dict(rho=choice,status='Numerical scaling overflow; no certificate',history=history));continue
        matrix=np.exp2(np.maximum(exponents,-1074));matrix[underflows]=0
        rhs_log=b-scale;rhs_shift=float(np.max(rhs_log))
        rhs=np.exp2(np.maximum(rhs_log-rhs_shift,-1074));rhs[~np.isfinite(rhs_log)]=0
        system=np.eye(dim)-matrix
        eig=np.linalg.eigvals(matrix);spectral=float(np.max(np.abs(eig)))
        solution=np.linalg.solve(system,rhs)
        residual=float(np.max(np.abs(system@solution-rhs)))
        negative=[i for i in range(dim) if solution[i]<0]
        cycles=[]
        for i in range(dim):
            for j in range(i+1,dim):cycles.append((float(R[i,j]+R[j,i]),i,j))
        cycles=sorted(cycles,reverse=True)[:10]
        def components(k,n):
            if k<N and n<N:
                parts={name:float(v[k,n]) for name,v in Lparts.items()}
                parts.update(middle=float(HC[k,n]),infinite=float(IC[n]))
                witnesses={}
                for name in ('main','corr','base','remainder'):
                    row=low_witnesses[k].get(name,{})
                    if k==n:witnesses[name]=row.get('diagonal_mode')
                    elif row.get('largest_source_cell')==n+12:witnesses[name]=row.get('largest_source_mode')
                return dict(log2_positive_summands=parts,known_low_modal_witnesses=witnesses)
            if k<N:return dict(log2_positive_summands=dict(low_far=float(beta[k]),middle_far=float(far[k]+2),infinite_far=float(deep+2)))
            return dict(log2_positive_summands=dict(far_row=float(fl[n]) if n<N else betaz))
        scenarios.append(dict(rho=choice,status='Float diagnostic only; no interval inverse or joint gate is asserted',
            spectral_radius_float=spectral,spectral_log2_float=math.log2(spectral),
            collatz_history=history,max_diagonal=float(np.max(np.diag(matrix))),
            scaled_row_sum_max=float(np.max(matrix.sum(axis=1))),
            system_condition_2_float=float(np.linalg.cond(system)),
            inverse_proposal_float_residual_inf=residual,
            negative_coordinate_count=len(negative),negative_coordinates=[dict(index=i,**label(i),scaled_value=float(solution[i])) for i in negative],
            proposal_coordinates=[dict(index=i,**label(i),scaled_value=float(solution[i]),scale_log2=float(scale[i])) for i in range(dim)],
            lost_scaled_underflow_entries=int(np.count_nonzero(underflows & np.isfinite(exponents))),
            largest_two_cycles=[dict(log2_product_float=v,first=dict(index=i,**label(i)),second=dict(index=j,**label(j)),
                forward=components(i,j),reverse=components(j,i)) for v,i,j in cycles]))
        print(json.dumps(dict(event='scenario',rho=choice,spectral_radius_float=spectral,
            negative_coordinates=len(negative),condition_float=scenarios[-1]['system_condition_2_float'],
            seconds=time.monotonic()-started,RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    result=dict(status='Numerical diagnostics of the positive majorant, not a spectral or existence certificate',
        scopes=['The exact g, all46 low coordinates, full middle triangle, infinity source and R18 far normalization are unchanged.',
                'rho is a proposal-domain derivative bound. The linear scenario drops only the 3*rho*base and positive higher-rho corrections.',
                'No actual Arb negative coordinate is manufactured; these signs are float proposals for a later exact check.',
                'A failed majorant says nothing by itself about nonexistence of the true field.'],
        scenarios=scenarios,input_hashes=hashes,source_sha256=digest(Path(__file__)),numpy_version=np.__version__,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        mathematical_gates_paid=False)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=True)+'\n')
    print(json.dumps(dict(event='done',output=str(args.out),seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
