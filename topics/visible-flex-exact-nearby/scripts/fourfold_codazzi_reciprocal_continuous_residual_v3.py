#!/usr/bin/env python3
"""Directed full reciprocal residual, v3 scalar and field A0 error budgets.

Every stored cubic and every Fourier mode is retained. Original target
primitive tails and compact-metric third-derivative remainders are paid on
each actual closed radial cell. All angular products have exact support
at most 3M and are resolved by a directed FFT with N>6M. The output is a
residual certificate, not an inverse or a nonlinear existence certificate.
"""
from __future__ import annotations
import argparse,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_reciprocal_compact_target_jets import ReciprocalCompactTargetJets
from fourfold_phase_beta_bulk_box import Box,CBox,zeros,DirectedFFT,arb_box,reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def add(a,b):
    zero=a[0]*0
    return [(a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero)
            for i in range(max(len(a),len(b)))]


def scale(a,c):return [x*c for x in a]


def mul(a,b):
    zero=a[0]*b[0]*0
    return [sum((a[j]*b[k-j] for j in range(max(0,k-len(b)+1),min(len(a)-1,k)+1)),zero)
            for k in range(len(a)+len(b)-1)]


def evaluate(poly,x):
    value=poly[-1]
    for c in poly[-2::-1]:value=value*x+c
    return value


def polynomial_at_affine(descending,offset,half):
    x=[arb_box(exact_arb(offset)),arb_box(exact_arb(half))]
    value=[Box.coerce(descending[0])]
    for coefficient in descending[1:]:value=add(mul(value,x),[Box.coerce(coefficient)])
    return value


def lift_state(values,m,N):
    """Exact sine/cosine normalization, including the V mean."""
    out=zeros((N,2));b=values[:m];c=values[m:]
    out[1:m+1,0]=CBox(0.,-b/2);out[-m:,0]=CBox(0.,b[::-1]/2)
    out[0,1]=CBox(c[0]);out[1:m+1,1]=CBox(c[1:]/2);out[-m:,1]=CBox(c[1:][::-1]/2)
    return out


def wiener_upper(coefficient):
    return arb(float(np.max(reduce_box(Box(coefficient.magnitude_upper())).hi))).upper()


class BudgetPolynomial:
    """Finite dyadic polynomial plus a full uniform radial/Fourier A0 error."""
    def __init__(self,coefficients,norm,error):
        self.coefficients=coefficients;self.norm=arb(norm).upper();self.error=arb(error).upper()
    @staticmethod
    def coerce(value):
        if isinstance(value,BudgetPolynomial):return value
        value=float(value)
        return BudgetPolynomial([Box(value)],abs(arb(value)),arb(0))
    def __add__(self,other):
        other=self.coerce(other)
        return BudgetPolynomial(add(self.coefficients,other.coefficients),self.norm+other.norm,self.error+other.error)
    __radd__=__add__
    def __neg__(self):return BudgetPolynomial(scale(self.coefficients,-1),self.norm,self.error)
    def __sub__(self,other):return self+-self.coerce(other)
    def __rsub__(self,other):return self.coerce(other)+-self
    def __mul__(self,other):
        other=self.coerce(other)
        error=self.norm*other.error+other.norm*self.error+self.error*other.error
        return BudgetPolynomial(mul(self.coefficients,other.coefficients),self.norm*other.norm,error)
    __rmul__=__mul__


def sum_box(value):
    return arb(float(reduce_box(Box(value.abs_upper())).hi)).upper()


def centre_real(value):
    midpoint=np.minimum(np.maximum(value.lo/2+value.hi/2,value.lo),value.hi)
    if not np.all(np.isfinite(midpoint)):raise ValueError('nonfinite selected dyadic reference')
    return Box(midpoint),value-Box(midpoint)


def exact_candidate_series(cube,knot,left,right,m,N,fft):
    mid,half=(left+right)/2,(right-left)/2;offset=mid-knot
    coefficients=polynomial_at_affine(cube,offset,half)
    derivative=polynomial_at_affine([Box(cube[0])*3,Box(cube[1])*2,Box(cube[2])],offset,half)
    full_original=[lift_state(v,m,N) for v in coefficients]
    norms=[arb(0) for _ in range(6)];fees=[arb(0) for _ in range(6)]
    centred=[];centred_derivative=[]
    weights=[Box(4*np.arange(1,m+1)),Box(4*np.arange(m+1))]
    for original in coefficients:
        centre,error=centre_real(original);centred.append(lift_state(centre,m,N))
        for component,part in enumerate((slice(0,m),slice(m,2*m+1))):
            norms[component]+=sum_box(centre[part]);fees[component]+=sum_box(error[part])
            norms[component+2]+=sum_box(centre[part]*weights[component])
            fees[component+2]+=sum_box(error[part]*weights[component])
    for original in derivative:
        centre,error=centre_real(original);centred_derivative.append(lift_state(centre,m,N))
        for component,part in enumerate((slice(0,m),slice(m,2*m+1))):
            norms[component+4]+=sum_box(centre[part]);fees[component+4]+=sum_box(error[part])
    modes=np.asarray([k if k<N//2 else k-N for k in range(N)])
    angular=CBox(0.,Box(4*modes[:,None]));block=zeros((N,22))
    for j,c in enumerate(centred):
        block[:,4*j:4*j+2]=c;block[:,4*j+2:4*j+4]=c*angular
    for j,c in enumerate(centred_derivative):block[:,16+2*j:18+2*j]=c
    samples=fft.fft(block,inverse=True)*N
    if not np.all((samples.imag.lo<=0)&(samples.imag.hi>=0)):
        raise ValueError('the complete real dyadic candidate reference lost reality')
    fields=[]
    for k in range(4):fields.append(BudgetPolynomial([samples.real[:,4*j+k] for j in range(4)],norms[k],fees[k]))
    for k in range(2):fields.append(BudgetPolynomial([samples.real[:,16+2*j+k] for j in range(3)],norms[k+4],fees[k+4]))
    return fields,full_original,half


def scalar_budget(values):
    coefficients=[];norm=arb(0);error=arb(0)
    for value in values:
        centre,delta=centre_real(value);coefficients.append(centre)
        norm+=arb(float(centre.abs_upper())).upper()
        error+=arb(float(delta.abs_upper())).upper()
    return BudgetPolynomial(coefficients,norm,error)


def target_model(midpoint,whole,name,half):
    h=exact_arb(half)
    # Taylor's theorem gives a possibly r-dependent third coefficient in
    # this full interval. It is not replaced by its midpoint or by zero.
    coefficients=[midpoint[name],h*midpoint[name+'1'],h*h*midpoint[name+'2']/2,
                  h**3*whole[name+'3']/6]
    return [arb_box(v) for v in coefficients]


def residual_polynomials(fields,model,alpha):
    U,V,Ut,Vt,Ur,Vr=fields
    g,b,K,s=[scalar_budget(model[name]) for name in ('gamma','beta','K','s')]
    al=float(alpha);v=s+al*V;U2=U*U;v2=v*v
    fU=g*(al*U*Ut+K*v*Vt)-b*U*(1+al*al*U2+K*v2)
    T=3*s*s*V+3*al*s*V*V+al*al*V*V*V
    fV=g*(al*U*Vt-v*Ut)+b*(V-K*T-al*v*U2)
    return Ur-fU,Vr-fV,v


def full_residual_norm(polynomials,N,degree,fft):
    length=max(len(p.coefficients) for p in polynomials);block=zeros((N,2*length))
    for component,poly in enumerate(polynomials):
        for j,value in enumerate(poly.coefficients):block[:,2*j+component]=CBox(value)
    coefficients=fft.fft(block)/N
    modes=np.asarray([k if k<N//2 else k-N for k in range(N)]);outside=abs(modes)>degree
    if not (np.all((coefficients.real.lo[outside]<=0)&(coefficients.real.hi[outside]>=0))
        and np.all((coefficients.imag.lo[outside]<=0)&(coefficients.imag.hi[outside]>=0))):
        raise ValueError('a mathematically absent finite Fourier mode lost its zero enclosure')
    coefficients[outside]=0
    per_order=[[],[]];total=[arb(0),arb(0)]
    for component in range(2):
        for j in range(length):
            value=wiener_upper(coefficients[:,2*j+component]);per_order[component].append(value)
            total[component]+=value
        total[component]+=polynomials[component].error
    return [x.upper() for x in total],per_order,length-1


def whole_chart_bounds(full,model,alpha,N,fft):
    """All angular cells, with local first jet and complete second-jet tail."""
    modes=np.asarray([k if k<N//2 else k-N for k in range(N)]);freq=4*modes
    block=zeros((N,16));m2=[[],[]]
    for j,c in enumerate(full):
        block[:,4*j:4*j+2]=c
        block[:,4*j+2:4*j+4]=c*CBox(0.,Box(freq[:,None]))
        for component in range(2):m2[component].append(wiener_upper(c[:,component]*CBox(Box(freq*freq))))
    samples=fft.fft(block,inverse=True)*N
    if not np.all((samples.imag.lo<=0)&(samples.imag.hi>=0)):
        raise ValueError('real closed-angle chart lost reality')
    angle_half=arb.pi()/(4*N);hh=arb_box(angle_half)
    polynomials=[[],[]]
    for component in range(2):
        for j in range(4):
            derivative=samples.real[:,4*j+2+component]
            fee=(hh*Box(derivative.abs_upper())+arb_box(angle_half**2*m2[component][j]/2)).hi
            polynomials[component].append(samples.real[:,4*j+component]+Box(-fee,fee))
    U=evaluate(polynomials[0],Box(-1.,1.))
    v=evaluate(add(model['s'],scale(polynomials[1],arb_box(exact_arb(alpha)))),Box(-1.,1.))
    vlo=arb(float(np.min(v.lo))).lower();vhi=arb(float(np.max(v.hi))).upper()
    if not vhi<0:raise ValueError('complete reciprocal chart v<0 not proved on this cell')
    gap=(-vhi).lower();Uabs=arb(float(np.max(U.abs_upper()))).upper()
    return dict(v_lower=vlo,v_upper=vhi,absolute_v_gap=gap,normalized_U_abs=Uabs,
        physical_C_abs_upper=(1/gap).upper(),physical_B_abs_upper=(abs(exact_arb(alpha))*Uabs/gap).upper())


def all_cells(knots,target,right):
    cuts=set(knots)
    cuts.update(x for x in target.cuts if 0<=x<=right)
    cuts.update((Fraction(0),right,Fraction(1,20),Fraction(9,50)))
    return sorted(x for x in cuts if 0<=x<=right)


def interface_jump(cube_left,cube_right,step,m,N):
    # Every coefficient and the knot displacement is exact dyadic input;
    # directed Horner retains the true floating-spline endpoint jump.
    h=arb_box(exact_arb(step));left=Box(cube_left[0])
    for c in cube_left[1:]:left=left*h+Box(c)
    jump=Box(cube_right[-1])-left
    full=lift_state(jump,m,N)
    return [wiener_upper(full[:,component]) for component in range(2)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--right',type=Fraction,default=Fraction(3,2))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(0))
    ap.add_argument('--nodes',type=int,default=512);ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--bits',type=int,default=192);ap.add_argument('--first',type=int,default=0)
    ap.add_argument('--count',type=int);ap.add_argument('--subdivide',type=int,default=1)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve the original directed result')
    ctx.prec=args.bits;ctx.cap=6
    data=load_candidate(args.candidate);meta=json.loads(str(data['metadata']));m=int(meta['modes']);N=args.angles
    if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object):
        raise ValueError('the exact complete reciprocal candidate is required')
    if N<=6*m or N&(N-1) or args.subdivide<1 or args.first<0:
        raise ValueError('unaliased complete angular support and valid partition are required')
    if not 0<args.right<=Fraction(3,2) or args.half_width<0:raise ValueError('invalid exact target domain')
    alpha=Fraction.from_float(float(meta['amplitude']));nu=Fraction(meta['exact_float_nu'])
    knots=[Fraction.from_float(float(x)) for x in data['radial_nodes']]
    if knots[0]!=0 or knots[-1]<args.right:raise ValueError('no extrapolation of the complete candidate')
    target=ReciprocalCompactTargetJets(args.object,args.half_width,args.nodes);fft=DirectedFFT()
    cuts=all_cells(knots,target,args.right);cells=[]
    for lo,hi in zip(cuts,cuts[1:]):
        cells.extend((lo+(hi-lo)*j/args.subdivide,lo+(hi-lo)*(j+1)/args.subdivide) for j in range(args.subdivide))
    end=len(cells) if args.count is None else min(len(cells),args.first+args.count)
    if not args.first<end:raise ValueError('empty selected complete cell range')
    rows=[];failure=None;maxima=[arb(0),arb(0)];min_gap=None
    for index in range(args.first,end):
        left,right=cells[index];mid=(left+right)/2;piece=bisect_right(knots,left)-1
        if not knots[piece]<=left<right<=knots[piece+1]:raise ValueError('candidate piece coverage failed')
        try:
            whole,germ=target.coefficients(left,right,nu);centre,_=target.coefficients(mid,mid,nu)
            fields,full,half=exact_candidate_series(data['piece_coefficients'][:,piece],knots[piece],left,right,m,N,fft)
            models={name:target_model(centre,whole,name,half) for name in ('gamma','beta','K','s')}
            RU,RV,v=residual_polynomials(fields,models,alpha)
            bounds,per_order,radial_degree=full_residual_norm((RU,RV),N,3*m,fft)
            chart=whole_chart_bounds(full,models,alpha,N,fft)
            row=dict(index=index,interval=list(map(str,(left,right))),candidate_piece=piece,
                actual_scalar_germ=list(map(str,germ)),exact_angular_support_index=3*m,
                maximum_radial_interval_polynomial_degree=radial_degree,
                complete_residual_A0={name:record(value) for name,value in zip(('U','V'),bounds)},
                complete_radial_order_finite_reference_residual_A0={name:[record(v) for v in values] for name,values in zip(('U','V'),per_order)},
                complete_uniform_radial_Fourier_A0_remainder={name:record(poly.error) for name,poly in zip(('U','V'),(RU,RV))},
                whole_chart={name:record(value) for name,value in chart.items()},
                actual_complete_target_coefficients={name:record(value) for name,value in whole.items()})
            rows.append(row);maxima=[max(a,b).upper() for a,b in zip(maxima,bounds)]
            min_gap=chart['absolute_v_gap'] if min_gap is None else min(min_gap,chart['absolute_v_gap']).lower()
        except Exception as error:
            failure=dict(index=index,interval=list(map(str,(left,right))),candidate_piece=piece,
                error_type=type(error).__name__,message=str(error));break
        if (index-args.first+1)%10==0 or index==end-1:
            print(dict(complete_rows=len(rows),requested_rows=end-args.first,last_index=index,
                residual_A0=[v.str(12) for v in maxima],wall_seconds=time.monotonic()-started),flush=True)
    jumps=[];jump_sum=[arb(0),arb(0)]
    selected_left,selected_right=cells[args.first][0],cells[end-1][1]
    if failure is None:
        for j in range(1,len(knots)-1):
            if not selected_left<knots[j]<=selected_right:continue
            values=interface_jump(data['piece_coefficients'][:,j-1],data['piece_coefficients'][:,j],knots[j]-knots[j-1],m,N)
            jumps.append(dict(knot_index=j,radius=str(knots[j]),complete_A0=[record(v) for v in values]))
            jump_sum=[a+b for a,b in zip(jump_sum,values)]
    report=dict(kind='complete_reciprocal_polynomial_continuous_residual_closed_radial_cells_with_A0_budgets',
        complete=failure is None and len(rows)==end-args.first,failure=failure,
        source_sha256=sha(__file__),candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        object_sha256=sha(args.object),exact_nu=str(nu),exact_amplitude=str(alpha),
        exact_original_target_parameter_half_width=str(args.half_width),new_compact_metric=True,
        complete_original_primitive_tail=True,whole_real_angular_circle=True,
        selected_interval=list(map(str,(selected_left,selected_right))),total_partition_cells=len(cells),
        first=args.first,end_exclusive=end,whole_requested_body=args.first==0 and end==len(cells),
        modes=m,angles=N,primitive_nodes=args.nodes,bits=args.bits,rows=rows,
        maximum_complete_residual_A0=[record(v) for v in maxima],
        minimum_v_gap=None if min_gap is None else record(min_gap),
        complete_interface_jumps=jumps,total_complete_interface_jump_A0=[record(v) for v in jump_sum],
        inverse_proved=False,nonlinear_PDE_existence_proved=False,final_geometric_criteria_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_reciprocal_compact_target_jets.py','fourfold_codazzi_cubic_target_jets.py',
            'fourfold_codazzi_high_target_jets.py','fourfold_phase_metric_defect.py',
            'fourfold_phase_cap_scaled_body.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_codazzi_candidate_shards.py')},
        wall_seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],failure=failure,rows=len(rows),out=str(args.out),wall_seconds=report['wall_seconds']),flush=True)
    if failure is not None:raise SystemExit(2)


if __name__=='__main__':main()
