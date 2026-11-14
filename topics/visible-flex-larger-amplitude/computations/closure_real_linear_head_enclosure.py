#!/usr/bin/env python3
"""Validated finite-mode REAL linear head columns and whole-cell source budgets.

This consumes R26's real source, integrates positive scalar kernels with Arb,
and encloses every linear matrix flow by Peano--Baker alternating-path bounds.
It is a reference trajectory / forcing certificate, not a nonlinear Green
inverse or a complete infinite-frequency matching result.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import acb, arb, ctx
from closure_real_head_source_enclosure import RealHead, exact_q, power2, zero_to, ball_record, dyadic_endpoint
from closure_projective_interval_column import ProjectiveColumn


def eye():
    return [[arb(1),arb(0)],[arb(0),arb(1)]]


def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(2)),arb(0)) for j in range(2)] for i in range(2)]


def mv(a,b):
    return [sum((a[i][k]*b[k] for k in range(2)),arb(0)) for i in range(2)]


def upper_abs(x):
    return abs(x).upper()


def maximum(a,b):
    return a.union(b).upper()


def interval(lo,hi):
    return lo.union(hi)


def matrix_record(m):
    return [[ball_record(x) for x in row] for row in m]


def positive_scale_bounds(bounds,factor):
    if not factor>0:raise ArithmeticError('A positive coordinate scale is required')
    lo,hi=bounds;fl,fu=factor.lower(),factor.upper()
    if lo>=0:return (lo*fl).lower(),(hi*fu).upper()
    if hi<=0:return (lo*fu).lower(),(hi*fl).upper()
    return (lo*fu).lower(),(hi*fu).upper()


def range_record(bounds):
    lo,hi=bounds
    return dict(lower=dyadic_endpoint(lo),upper=dyadic_endpoint(hi),
        display='['+str(lo)+', '+str(hi)+']',
        representation='separate outward dyadic endpoints; do not infer a zero solely from conversion to a wide symmetric ball')


def ideal_slope(mode,rho):
    if mode==2:
        return arb(0)
    nu=arb(mode*mode*(mode*mode-1))/12
    d=1/rho
    t00=1-65*nu
    t10=65*d*nu*(nu-1)
    t11=d*(1-arb(65)*nu/64)
    tr=t00+t11
    lam=(tr-(tr*tr-4*d).sqrt())/2
    return t10/(lam-t11)


def peano_matrix(A,B):
    """T for q'=a xi, xi'=-b q, a,b>=0, with integral balls A,B.

    An ordered term with k factors a and l factors b is bounded by
    A^k B^l/(k! l!). All terms after the exact first off-diagonal integral
    are enclosed with their alternating signs and positive majorants.
    """
    au,bu=A.upper(),B.upper()
    p=au*bu
    if not 0<=p<1:
        raise ArithmeticError('Subdivide until integral A*B<1')
    even=p*p/(4*(1-p))
    odd=p*p/(12*(1-p))
    diagonal=interval(1-p-even,1+even)
    positive=interval(A.lower()-au*(p/2+odd),A.upper()+au*odd)
    negative=interval(-B.upper()-bu*odd,-B.lower()+bu*(p/2+odd))
    matrix=[[diagonal,positive],[negative,diagonal]]
    # A nonnegative upper matrix for every subinterval, its inverse, and
    # the absolute values of the full flow. Its diagonal is >=1.
    major=[[1+even,au*(1+odd)],[bu*(1+odd),1+even]]
    return matrix,major,p


class PositiveKernels:
    def __init__(self,head,far,max_mode):
        self.head=head
        self.far=far
        self.max_mode=max_mode
        self.source_cache={}
        self.radius_cache={}
        self.integral_count=0
        self.kernel_cache={}

    def source_cell(self,n):
        if n in self.head.cells:
            return self.head.cells[n]
        if n in self.source_cache:
            return self.source_cache[n]
        h=self.head
        delta=h.d0*power2(-n)
        c=h.c0*(-arb(n)*h.log2/2).exp()
        mu=h.eps_phys*(h.a*delta.log()).exp()
        q32=(-arb(3)*h.log2/2).exp()
        after=3*delta+6*h.c0*h.d0*q32**(n+1)/(1-q32)
        inner_log_r=h.rc.log()+after/h.sqrt12
        row=h.data[n] if n<160 else dict(R=64,alpha=65/64)
        alpha=exact_q(row['alpha']) if n<160 else arb(65)/64
        logs=[arb(0),exact_q(row['R']).log()-delta.log(),
              delta.log()-alpha.log(),-delta.log(),h.a*h.log2]
        pieces=[(0,0,c),(0,1,c),(1,1,arb(1)),(1,2,c),(2,2,arb(1)),
                (2,3,c),(3,3,arb(1)),(3,4,c),(4,4,c)]
        offset=arb(0);segments=[]
        for j,(lo,hi,ratio) in enumerate(pieces):
            length=delta*ratio
            s=dict(n=n,j=j,length=length,log_mu=mu.log(),
                log_r0=inner_log_r+offset/h.sqrt12,
                log_p0=logs[lo],log_jump=logs[hi]-logs[lo],
                transition=lo!=hi,delta=delta)
            s['critical_points']=h.critical_points(s)
            segments.append(s);offset+=length
        result=dict(n=n,delta=delta,mu=mu,segments=segments)
        self.source_cache[n]=result
        return result

    def radius_point(self,n,j,x):
        key=(n,j,x)
        if key in self.radius_cache:return self.radius_cache[key]
        h=self.head;s=self.source_cell(n)['segments'][j]
        if n<159:
            r=h.physical_point(n,j,x)['r']
        elif n==159:
            delta=h.d0*power2(-n)
            W=power2(21)*(arb(7)*delta.log()/4).exp()
            tail=h.rc*(326*delta+11*W/(1-(-arb(7)*h.log2/4).exp()))
            r=h.rc+zero_to(tail)
        else:
            r=h.source_point(s,exact_q(x))['ro']
        self.radius_cache[key]=r
        return r

    def scalar_integral(self,s,left,right,kind):
        h=self.head;lo=exact_q(left);hi=exact_q(right)
        length=s['length'];span=hi-lo
        # Normalized free kernels: sqrt(12)*mu*int(ro_x/w) and
        # sqrt(12)/mu*int(ro_x*w); mu cancels before evaluation.
        c_r,sign=(8,-1) if kind=='a' else (-6,1)
        if not s['transition']:
            log_r=s['log_r0']+length*lo/h.sqrt12
            z=c_r*length*span/h.sqrt12
            return h.sqrt12/c_r*(c_r*log_r+sign*s['log_p0']).exp()*z.expm1()
        smooth_lo=h.smooth(lo)
        log_r_lo=s['log_r0']+length*lo/h.sqrt12
        log_p_lo=s['log_p0']+s['log_jump']*smooth_lo
        scale=length*(c_r*log_r_lo+sign*log_p_lo).exp()
        def f(x,analytic):
            # The integrand equals 1 at the left endpoint. A tiny physical
            # cell length is outside the integral, so the absolute tolerance
            # cannot erase a positive deep-cell kernel.
            exponent=c_r*length*(x-lo)/h.sqrt12+sign*s['log_jump']*(h.smooth(x)-smooth_lo)
            return exponent.exp()
        val=acb.integral(f,acb(lo),acb(hi),rel_tol=power2(-110),abs_tol=power2(-200),
                         deg_limit=64,eval_limit=20000,depth_limit=30)
        self.integral_count+=1
        if not val.is_finite() or not val.imag.contains(0) or not val.real>0:
            raise ArithmeticError('A positive scalar kernel was not enclosed')
        return scale*val.real

    def variation(self,s,left,right,kind):
        h=self.head;lo=exact_q(left);hi=exact_q(right)
        points=[lo]
        for t in s['critical_points']:
            if lo<t<hi:points.append(t)
            elif not (t<lo or t>hi):
                raise ArithmeticError('A dyadic panel endpoint overlaps a critical root interval')
        points.append(hi)
        values=[]
        for x in points:
            g=h.source_point(s,x);w=g['w'];root=(1+w*w).sqrt()
            values.append(g['log_w']-(1+root).log()+1/root if kind=='a'
                          else w*w/(root*(1+root)))
        return sum((abs(b-a) for a,b in zip(values,values[1:])),arb(0))

    def kernels(self,n,j,left,right):
        key=(n,j,left,right)
        if key in self.kernel_cache:return self.kernel_cache[key]
        h=self.head;c=self.source_cell(n);s=c['segments'][j]
        r=self.radius_point(n,j,left).union(self.radius_point(n,j,right))
        af=self.scalar_integral(s,left,right,'a')
        bf=self.scalar_integral(s,left,right,'b')
        if n>=160:
            ca,cb=arb(0),arb(0)
            free_factor=arb(1)
        else:
            ca=h.sqrt12*c['mu']/8*self.variation(s,left,right,'a')
            cb=h.sqrt12/(8*c['mu'])*self.variation(s,left,right,'b')
            W=power2(21)*(arb(7)*c['delta'].log()/4).exp()
            invE=interval(1/(1+W*W),arb(1))
            if n==159 and j==0:
                # Exact protected collar chi in [0,1]. Its free coefficient
                # lies between 1/E and alpha; curvature is between 0 and full.
                free_factor=interval(1/(1+W*W),h.alpha)
                ca=zero_to(ca.upper());cb=zero_to(cb.upper())
            else:
                free_factor=h.alpha*invE
        result=dict(r=r,coreA=free_factor*af+ca,coreB=free_factor*bf+cb)
        self.kernel_cache[key]=result
        return result

    def mode_integrals(self,kernel,mode):
        h=self.head;u=mode*mode-4;nu=arb(mode*mode*(mode*mode-1))/12
        r=kernel['r']
        A=(h.rc/r)**(2*u)*r**(-8)*kernel['coreA']
        B=nu*(r/h.rc)**(2*u)*r**6*kernel['coreB']
        return A,B

    def panels(self,n,j,threshold):
        stack=[(Q(0),Q(1),0)]
        while stack:
            left,right,level=stack.pop()
            kernel=self.kernels(n,j,left,right)
            A,B=self.mode_integrals(kernel,self.max_mode)
            if A.upper()*B.upper()>threshold:
                if level>=30:raise ArithmeticError('Panel subdivision limit')
                mid=(left+right)/2
                stack.append((mid,right,level+1));stack.append((left,mid,level+1))
                continue
            yield left,right,kernel

    def release_cell(self,n):
        self.kernel_cache.clear();self.radius_cache.clear()
        if n in self.source_cache:del self.source_cache[n]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ready',required=True,type=Path)
    p.add_argument('--source-ledger',required=True,type=Path)
    p.add_argument('--response',required=True,type=Path)
    p.add_argument('--out-prefix',required=True,type=Path)
    p.add_argument('--modes',type=int,default=1)
    p.add_argument('--reference-modes',type=int)
    p.add_argument('--start',type=int,default=12)
    p.add_argument('--far',type=int,default=225)
    p.add_argument('--product-bits',type=int,default=20)
    p.add_argument('--tau',type=int,default=1)
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision
    started=time.monotonic()
    ready_raw=args.ready.read_bytes();ready=json.loads(ready_raw)
    ledger_raw=args.source_ledger.read_bytes();ledger=json.loads(ledger_raw)
    response_raw=args.response.read_bytes()
    response=json.loads(gzip.decompress(response_raw) if args.response.suffix=='.gz' else response_raw)
    actual=response['response']['endpointCanonicalTrace']
    if actual['physicalNode']!=args.start:raise ValueError('Actual height is at a different physical node')
    if not 1<=args.modes<=46:raise ValueError('R18 has 46 independent low linear columns')
    reference_modes=min(args.modes,len(actual['Q'])) if args.reference_modes is None else args.reference_modes
    if not 1<=reference_modes<=min(args.modes,len(actual['Q'])):
        raise ValueError('The reference must retain a positive number of supplied actual heights')
    if not all(ledger['checks'].values()) or hashlib.sha256(ready_raw).hexdigest() not in ledger['input_hashes'].values():
        raise ValueError('The exact source ledger does not certify this ready input')
    head=RealHead(ready,start=args.start,far=159,exact_through=23)
    modes=[2*(j+1) for j in range(args.modes)]
    kernels=PositiveKernels(head,args.far,max(modes))
    first=kernels.source_cell(args.far-1)['segments'][0]
    r_far=head.source_point(first,arb(0))['ro']
    vectors=[]
    for m in modes:
        u=m*m-4;nu=arb(m*m*(m*m-1))/12
        s=ideal_slope(m,head.rho)
        # R18 (9.4): exact LINEAR far graph, one independent modal column.
        s=s+interval(-nu*power2(-60),nu*power2(-60))
        scale=(r_far/head.rc)**u
        vectors.append(ProjectiveColumn([1/scale,scale*s]))
    records=[];total_panels=0;maximum_product=arb(0)
    for n in range(args.far-1,args.start-1,-1):
        if n<args.far-1:
            for v in vectors:v.multiply_component(1,1/head.rho)
        c=kernels.source_cell(n)
        cell_mats=[eye() for _ in modes]
        major_forward=[eye() for _ in modes]
        major_backward=[eye() for _ in modes]
        qmax=[arb(0) for _ in modes];ximax=[arb(0) for _ in modes]
        panel_count=0
        for j in range(9):
            for left,right,kernel in kernels.panels(n,j,power2(-args.product_bits)):
                panel_count+=1
                for k,m in enumerate(modes):
                    A,B=kernels.mode_integrals(kernel,m)
                    T,major,product=peano_matrix(A,B)
                    maximum_product=maximum(maximum_product,product)
                    u=m*m-4
                    abs0=vectors[k].absolute_uppers()
                    partial=mv(major,abs0)
                    qphys=upper_abs((kernel['r']/head.rc)**u)*partial[0]
                    xiphys=upper_abs((head.rc/kernel['r'])**u)*partial[1]
                    qmax[k]=maximum(qmax[k],qphys)
                    ximax[k]=maximum(ximax[k],xiphys)
                    try:
                        vectors[k].advance(T)
                    except ArithmeticError as error:
                        failure=dict(status='The projective interval enclosure failed; no true singularity is inferred',
                            cell=n,segment=j,left=str(left),right=str(right),mode=m,
                            input_pivot=vectors[k].pivot,input_ratio=ball_record(vectors[k].ratio),
                            panel_matrix=matrix_record(T),error=str(error),
                            elapsed_seconds=time.monotonic()-started,
                            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                            entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                            projective_column_sha256=hashlib.sha256(Path(__file__).with_name('closure_projective_interval_column.py').read_bytes()).hexdigest())
                        Path(str(args.out_prefix)+'-failure.json').write_text(json.dumps(failure,indent=2)+'\n')
                        raise
                    cell_mats[k]=mm(T,cell_mats[k])
                    major_forward[k]=mm(major,major_forward[k])
                    major_backward[k]=mm(major_backward[k],major)
        total_panels+=panel_count
        r_out=kernels.radius_point(n,8,Q(1));r_in=kernels.radius_point(n,0,Q(0))
        rows=[]
        for k,m in enumerate(modes):
            u=m*m-4;scale=(r_out/head.rc)**u
            q_bounds=positive_scale_bounds(vectors[k].component_bounds(0),scale)
            xi_bounds=positive_scale_bounds(vectors[k].component_bounds(1),1/scale)
            q=q_bounds[0].union(q_bounds[1]);xi=xi_bounds[0].union(xi_bounds[1])
            # Sum norm for arbitrary linear sources on any two points of this
            # cell. These intentionally coarse Cauchy bounds are NOT a head DN.
            radius_all=r_in.union(r_out)
            Dmax=[upper_abs((radius_all/head.rc)**u),upper_abs((head.rc/radius_all)**u)]
            Dinvmax=[Dmax[1],Dmax[0]]
            all_bounds=[]
            for P in (major_forward[k],major_backward[k]):
                Pphys=[[P[i][j]*Dmax[i]*Dinvmax[j] for j in range(2)] for i in range(2)]
                ratio=arb((1+m)**2)
                weighted=max(upper_abs(Pphys[0][0]+Pphys[1][0]/ratio),
                             upper_abs(ratio*Pphys[0][1]+Pphys[1][1]))
                all_bounds.append(weighted)
            rows.append(dict(mode=m,Q_out=q,Xi_cell_out=xi,
                Q_out_bounds=q_bounds,Xi_out_bounds=xi_bounds,
                Q_sup=qmax[k],Xi_sup=ximax[k],gauge_matrix=cell_mats[k],
                gauge_backward_majorant=major_backward[k],
                weighted_Cauchy_bound=maximum(*all_bounds)))
        records.append(dict(cell=n,panels=panel_count,delta=c['delta'],mu=c['mu'],
                            r_inner=r_in,r_outer=r_out,rows=rows))
        if n%16==0 or n==args.start:
            print(json.dumps(dict(event='cell',cell=n,panels=total_panels,
                seconds=time.monotonic()-started,RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        kernels.release_cell(n)
    final=records[-1]['rows']
    raw_endpoint_rows=[]
    for k,m in enumerate(modes):
        qlo,qhi=final[k]['Q_out_bounds'];unit=vectors[k].unit()
        raw_endpoint_rows.append(dict(mode=m,Q_gain=range_record((qlo,qhi)),
            Xi_gain=range_record(final[k]['Xi_out_bounds']),
            Q_direction_interval=ball_record(unit[0]),Xi_direction_interval=ball_record(unit[1]),
            pivot=vectors[k].pivot,common_scale_sign=vectors[k].sign,
            common_scale_log2_ratio=ball_record((vectors[k].absolute_upper/vectors[k].absolute_lower).log()/head.log2),
            height_chart_paid=bool(qlo>0 or qhi<0)))
    # Preserve the costly real cell flows before testing any shallow chart.
    # A failed height chart must not discard independently completed columns.
    groups=[]
    for first_mode in range(0,len(modes),8):
        stop=min(first_mode+8,len(modes));group_cells=[]
        for record in reversed(records):
            group_cells.append(dict(cell=record['cell'],mu=ball_record(record['mu']),
                r_inner=ball_record(record['r_inner']),r_outer=ball_record(record['r_outer']),
                linear_rows=[dict(mode=row['mode'],column_Q_sup=ball_record(row['Q_sup']),
                    column_Xi_sup=ball_record(row['Xi_sup']),
                    weighted_Cauchy_bound=ball_record(row['weighted_Cauchy_bound']),
                    gauge_matrix=matrix_record(row['gauge_matrix']),
                    gauge_backward_majorant=matrix_record(row['gauge_backward_majorant']))
                    for k,row in enumerate(record['rows']) if first_mode<=k<stop]))
        group_path=Path(str(args.out_prefix)+f'-columns-{first_mode+1:02d}-{stop:02d}.json.gz')
        group_data=dict(modes=modes[first_mode:stop],endpoint_rows=raw_endpoint_rows[first_mode:stop],cell_rows=group_cells)
        group_raw=gzip.compress((json.dumps(group_data,separators=(',',':'))+'\n').encode(),mtime=0)
        if len(group_raw)>=5_000_000:raise ArithmeticError('A column group exceeds the repository cap')
        group_path.write_bytes(group_raw)
        groups.append(dict(path=str(group_path),sha256=hashlib.sha256(group_raw).hexdigest(),bytes=len(group_raw),modes=group_data['modes']))
        del group_cells,group_data,group_raw
    raw_manifest=dict(status='Validated real linear cell enclosures saved before shallow chart acceptance',
        modes=modes,reference_modes=reference_modes,endpoint_rows=raw_endpoint_rows,column_groups=groups,
        start_physical_node=args.start,far_physical_node=args.far,tau=args.tau,
        input_hashes={str(args.ready):hashlib.sha256(ready_raw).hexdigest(),
            str(args.source_ledger):hashlib.sha256(ledger_raw).hexdigest(),
            str(args.response):hashlib.sha256(response_raw).hexdigest()},
        entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        projective_column_sha256=hashlib.sha256(Path(__file__).with_name('closure_projective_interval_column.py').read_bytes()).hexdigest(),
        source_enclosure_sha256=hashlib.sha256(Path(__file__).with_name('closure_real_head_source_enclosure.py').read_bytes()).hexdigest())
    Path(str(args.out_prefix)+'-raw-manifest.json').write_text(json.dumps(raw_manifest,indent=2)+'\n')
    amps=[];endpoint_rows=[]
    for k,m in enumerate(modes):
        qlo,qhi=final[k]['Q_out_bounds']
        if not (qlo>0 or qhi<0):
            failure=dict(status='The interval enclosure did not prove a nonzero low-height chart; not a zero of the true chart',
                failed_mode=m,panels=total_panels,
                endpoint_columns=raw_endpoint_rows,column_groups=groups,
                elapsed_seconds=time.monotonic()-started,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
            Path(str(args.out_prefix)+'-failure.json').write_text(json.dumps(failure,indent=2)+'\n')
            raise ArithmeticError('The cut height chart enclosure contains zero at mode '+str(m))
        target=exact_q(actual['Q'][k]) if k<reference_modes else arb(0)
        gain_sign=1 if qlo>0 else -1
        gl,gu=(qlo,qhi) if gain_sign>0 else (-qhi,-qlo)
        alo=(abs(target).lower()/gu).lower();ahi=(abs(target).upper()/gl).upper()
        amplitude_sign=(1 if target>=0 else -1)*gain_sign
        amplitude_bounds=(alo,ahi) if amplitude_sign>0 else (-ahi,-alo)
        amps.append(ahi)
        unit=vectors[k].unit();scale=(records[-1]['r_outer']/head.rc)**(m*m-4)
        slope=unit[1]/unit[0]/(head.rho*scale*scale)
        defect=exact_q(actual['canonicalXi'][k])-target*slope if k<reference_modes else None
        endpoint_rows.append(dict(mode=m,log2_absolute_Q_gain=ball_record(gl.log().union(gu.log())/head.log2),
            Q_gain=range_record((qlo,qhi)),raw_worker_slope=ball_record(slope),reference_Q=ball_record(target),
            reference_height_origin='saved actual binary height' if k<reference_modes else 'chosen zero in the LINEAR reference only; not a corrected nonlinear boundary assertion',
            required_far_Q=range_record(amplitude_bounds),
            actual_canonical_minus_reference=ball_record(defect) if defect is not None else None))
    output_rows=[];max_ratio=arb(0);sum_forcing=arb(0);sum_mean=arb(0)
    for record in reversed(records):
        n=record['cell'];delta=record['delta']
        X=sum(((arb(args.tau*m)).exp()*((1+m)**3*row['Q_sup']+(1+m)*row['Xi_sup'])*amps[k]
               for k,(m,row) in enumerate(zip(modes,record['rows']))),arb(0))
        radius=power2(-23)*head.eps/head.rc**3*(arb(19)*delta.log()/4).exp()
        B=power2(12)*head.rc**3/head.eps*(-arb(19)*delta.log()/4).exp()
        H=power2(8)*head.rc**7/head.eps*(-arb(23)*delta.log()/4).exp()
        if not X<radius:raise ArithmeticError('The reference whole-cell R23 radius was not paid at cell '+str(n))
        ratio=X/radius;max_ratio=maximum(max_ratio,ratio)
        forcing=B*X*X;mean=H*X*X
        sum_forcing+=forcing;sum_mean+=mean
        output_rows.append(dict(cell=n,panels=record['panels'],
            whole_cell_reference_X=ball_record(X),log2_X=ball_record(X.log()/head.log2),
            relative_to_R23_radius=ball_record(ratio),
            complete_source_L1_bound=ball_record(forcing),mean_height_increment_bound=ball_record(mean),
            ))
    result=dict(status='Validated exact-LINEAR finite-Fourier reference and complete nonlinear SOURCE budget; no nonlinear correction is asserted',
        modes=modes,reference_modes=reference_modes,tau=args.tau,start_physical_node=args.start,far_physical_node=args.far,
        far_linear_graph_band='R18 (9.4), |s-s_ideal|<=nu*2^-60 separately for each linear modal column',
        endpoint_rows=endpoint_rows,cell_rows=output_rows,
        all_reference_R23_balls_paid=True,maximum_reference_radius_ratio=ball_record(max_ratio),
        complete_source_L1_sum=ball_record(sum_forcing),mean_height_increment_sum=ball_record(sum_mean),
        product_threshold_bits=args.product_bits,maximum_accepted_AB=ball_record(maximum_product),
        panel_count=total_panels,scalar_integrals=kernels.integral_count,
        source_integrals=head.integral_count,elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        input_hashes={str(args.ready):hashlib.sha256(ready_raw).hexdigest(),
            str(args.source_ledger):hashlib.sha256(ledger_raw).hexdigest(),
            str(args.response):hashlib.sha256(response_raw).hexdigest()},
        entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        projective_column_sha256=hashlib.sha256(Path(__file__).with_name('closure_projective_interval_column.py').read_bytes()).hexdigest(),
        column_representation='Common amplitude times an interval projective direction; each panel chooses a nonzero normalized pivot and retains all interval uncertainty.',
        source_enclosure_sha256=hashlib.sha256(Path(__file__).with_name('closure_real_head_source_enclosure.py').read_bytes()).hexdigest(),
        bound_semantics='Balls for X, Q_sup, Xi_sup, source, mean and Cauchy-bound fields enclose the calculated positive majorant, not the unknown norm itself. Their upper endpoints are the certified upper bounds. Endpoint/gain/source-coordinate balls enclose the actual indicated values.',
        limits=['All stated low linear columns are actually enclosed. Only reference_modes saved heights are retained in the reference; other reference heights are chosen zero, not asserted zero in the corrected nonlinear tail.',
                'Higher frequencies of the true nonlinear correction and of R18 nonlinear far trace are not set to zero.',
                'A full-frequency boundary-value Green operator is still required; the listed within-cell Cauchy bounds do not replace it.',
                'Current saved node height fixes a reference, not a rigorous enclosure of the finite nonlinear solution path.',
                'The original floating source/ODE state errors at the shallow side remain separate from this real reference.'])
    result['column_groups']=groups
    result['peak_RSS_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result['elapsed_seconds']=time.monotonic()-started
    out=Path(str(args.out_prefix)+'.json.gz')
    raw=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(raw)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    out.write_bytes(raw)
    summary={k:v for k,v in result.items() if k not in ('cell_rows','input_hashes')}
    summary.update(first_cell=output_rows[0],output=str(out),output_bytes=len(raw),output_sha256=hashlib.sha256(raw).hexdigest())
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(output=str(out),panels=total_panels,modes=modes,
        first_X_log2=output_rows[0]['log2_X']['display'],
        max_radius_ratio=str(max_ratio),source_L1_sum=str(sum_forcing),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
