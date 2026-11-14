#!/usr/bin/env python3
"""Actual full complementary mismatch and its physical angular derivative.

The body kernel evaluates B_theta by exact first-order angular algebra.
It reuses one complete primitive evaluation; P_theta and P_rtheta follow
from the infinite tangent identity, not differentiation of a truncated FFT.
A completed requested body interval is not a completed full cap.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_bulk_box import CBox,Box,cstack,zeros,complex_sincos
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_parameter_comparison import ParameterDiskBody
from fourfold_phase_cap_scaled_body import ScaledBodyForm,common_cells
from fourfold_phase_cap_energy_interval import (
    FiniteTrial,gauss_rule,sha,conjugate,hermitian_midpoint)
from fourfold_phase_core_low_coefficients import extend_half
from fourfold_phase_cap_wiener_cover import write_json
from fourfold_phase_actual_positive_cap import complex_separation


class ThetaJet:
    """True value and physical theta derivative in any real/complex ball ring."""
    def __init__(self,value,derivative=None):
        self.value=value
        self.derivative=value*0 if derivative is None else derivative
    @staticmethod
    def as_jet(x):
        return x if isinstance(x,ThetaJet) else ThetaJet(x,0)
    def __add__(self,x):
        x=self.as_jet(x)
        return ThetaJet(self.value+x.value,self.derivative+x.derivative)
    __radd__=__add__
    def __neg__(self):
        return ThetaJet(-self.value,-self.derivative)
    def __sub__(self,x):
        return self+-self.as_jet(x)
    def __rsub__(self,x):
        return self.as_jet(x)+-self
    def __mul__(self,x):
        x=self.as_jet(x)
        return ThetaJet(self.value*x.value,
            self.derivative*x.value+self.value*x.derivative)
    __rmul__=__mul__
    def reciprocal(self):
        value=1/self.value
        return ThetaJet(value,-self.derivative*value*value)
    def __truediv__(self,x):
        return self*self.as_jet(x).reciprocal()
    def __rtruediv__(self,x):
        return self.as_jet(x)*self.reciprocal()
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError('integer powers only')
        if n<0:return self.reciprocal()**(-n)
        answer=self.as_jet(1)
        for _ in range(n):answer=answer*self
        return answer
    def sincos(self):
        if isinstance(self.value,CBox):
            s,c=complex_sincos(self.value)
        else:
            s,c=self.value.sin(),self.value.cos()
        return ThetaJet(s,c*self.derivative),ThetaJet(c,-s*self.derivative)


def form_from_unit_angular_jets(P,Pr,L,C,inverse_radius,radius,height,K,
                                b,g,br,gr,bt,gt):
    """Exact radius-cancelled grounded form, with true infinite P,T identities.

    P is P(T)-e_r in the rotating cylindrical basis, and Pr its radial
    derivative. b,g,br,gr,bt,gt are ThetaJets; L,C,a,Z,K are radial scalars.
    """
    sb,cb=b.sincos();sg,cg=g.sincos()
    sb0,cb0,sg0,cg0=[x.value for x in (sb,cb,sg,cg)]
    br0,gr0=br.value,gr.value
    tangent=[-cg0*sb0,cg0*cb0,sg0]
    tangent_r=[-cg0*cb0*br0+sg0*sb0*gr0,
               -cg0*sb0*br0-sg0*cb0*gr0,cg0*gr0]
    # D_theta e_r=e_theta, D_theta e_theta=-e_r.  No angular
    # derivative of a finite primitive is substituted for these identities.
    Ptheta=[tangent[0]+P[1],tangent[1]-1-P[0],tangent[2]]
    Prtheta=[tangent_r[0]+Pr[1],tangent_r[1]-Pr[0],tangent_r[2]]
    P=[ThetaJet(x,y) for x,y in zip(P,Ptheta)]
    Pr=[ThetaJet(x,y) for x,y in zip(Pr,Prtheta)]
    L,C,ia,a,Z,K=map(ThetaJet,(L,C,inverse_radius,radius,height,K))
    X0=L*(1+P[0])+Pr[0]
    X1=L*P[1]+Pr[1]
    Xz=C+(L*P[2]+Pr[2])*ia
    h1=-sb*X0+cb*X1
    v1=-cb*X0-sb*X1
    Q2=cg*Xz-sg*ia*h1
    D2=(1+bt)*cg*Q2-gt*ia*v1
    M2=br*cg*Q2-gr*ia*v1
    W2=v1*v1+a*a*Q2*Q2
    Fh1=-sb*(1+P[0])+cb*P[1]
    Fv1=-cb*(1+P[0])-sb*P[1]
    Fz=Z+a*P[2]
    Fq=cg*Fz-a*sg*Fh1
    H1=Fq*v1-a*a*Fv1*Q2
    A=Fz*Fz*D2/(H1*H1)
    drift=-M2/D2
    kappa=Fz*Fz*W2*W2*K/(D2*H1*H1)
    inverse_A=1/A
    inverse_kappa=1/kappa
    values=[A,A*drift,A*drift*drift+kappa,
            inverse_A+drift*drift*inverse_kappa,
            -drift*inverse_kappa,inverse_kappa]
    return values,(A,kappa,drift),dict(D2=D2.value,H1=H1.value,
        Fz=Fz.value,K=K.value,W2=W2.value)


class AngularFamilyBody(ParameterDiskBody):
    # R111's initializer and complete scalar-germ combination are retained.
    # Its special continuous-real-angle-only unit_fields is replaced by the
    # already paid nodal/strip primitive evaluator, since parameters here
    # are real throughout.
    unit_fields=ScaledBodyForm.unit_fields
    def __init__(self,object_path,half_width,nodes,angles):
        eta=Fraction(half_width)
        if eta<0:raise ValueError('negative real parameter half width')
        super().__init__(object_path,eta if eta else Fraction(1,10**9),False,nodes,angles)
        self.offset=acb(arb(0,exact_arb(eta))) if eta else acb(0)
        self.real_parameter=True
        self.parameter_half_width=eta
        self.parameter_interval=(self.parameter_center-eta,self.parameter_center+eta)
        self.parameter_ball=exact_arb(self.parameter_interval[0]).union(
            exact_arb(self.parameter_interval[1]))
        self.fast_cell_cache.clear();self.span_cache.clear()
        self.cell=None

    def form_angular_jets(self,radial,sigma=None):
        primitive,K,errors,real,ratios=self.normalized_data(radial)
        P,Pr=self.unit_fields(radial,primitive,errors,real,sigma)
        beta,gamma,radius,height=self.last_scalar
        L,_,C,_,ia=ratios
        ss,cc=(self.angle_sines,self.angle_cosines) if sigma is None else self.angle_shift_cache[sigma.str(35)]
        frequency=CBox((4*np.arange(1,self.modes+1)).reshape(-1,1))
        phase=lambda v,j:(v[j].reshape(-1,1)*ss).sum()
        angular=lambda v,j:(v[j].reshape(-1,1)*frequency*cc).sum()
        second=lambda v:-(v[0].reshape(-1,1)*frequency*frequency*ss).sum()
        b=ThetaJet(phase(beta,0),angular(beta,0))
        g=ThetaJet(phase(gamma,0),angular(gamma,0))
        br=ThetaJet(phase(beta,1),angular(beta,1))
        gr=ThetaJet(phase(gamma,1),angular(gamma,1))
        bt=ThetaJet(angular(beta,0),second(beta))
        gt=ThetaJet(angular(gamma,0),second(gamma))
        values,normal,domain=form_from_unit_angular_jets(
            [P[:,j] for j in range(3)],[Pr[:,j] for j in range(3)],
            L,C,ia,radius[0],height[0],K,b,g,br,gr,bt,gt)
        for name in ('D2','H1','Fz','K','W2'):
            complex_separation(domain[name],name+' in true angular derivative')
        for jet in values+list(normal):
            if (not np.all(np.isfinite(jet.value.magnitude_upper()))
                    or not np.all(np.isfinite(jet.derivative.magnitude_upper()))):
                raise ValueError('nonfinite true cap form angular jet')
        if real and (sigma is None or sigma==0):
            A,kappa,_=normal
            if not np.all(A.value.real.lo>0) or not np.all(kappa.value.real.lo>0):
                raise ValueError('real cap form has unresolved positive coefficients')
        return values,normal,domain


def scalar_upper(value):
    return arb(float(np.max(value.magnitude_upper()))).upper()


def trial_column_bounds(trial,coefficients,sigma=None):
    """Complete finite angular coefficient l1 then Euclidean input columns."""
    weights=1.
    if sigma is not None:
        weights=CBox.from_acb(acb(1))
        factors=[CBox.from_acb(acb((exact_arb(Fraction(abs(int(n)),4))*sigma).exp()))
                 for n in trial.frequency]
        weights=cstack(factors).reshape(trial.n,1)
    base=list(map(trial.coefficient_l1_columns,[x*weights for x in coefficients]))
    derivative=list(map(trial.coefficient_l1_columns,
        [x*CBox(0.,Box(trial.frequency[:,None]))*weights for x in coefficients]))
    return base,derivative


def mismatch_moduli(jets,base,derivative):
    B=[scalar_upper(x.value) for x in jets[:3]]
    D=[scalar_upper(x.derivative) for x in jets[:3]]
    I=[scalar_upper(x.value) for x in jets[3:]]
    R,T,P,Q=base;Rt,Tt,Pt,Qt=derivative
    z=[B[0]*R+B[1]*T+P,B[1]*R+B[2]*T+Q]
    dz=[D[0]*R+D[1]*T+B[0]*Rt+B[1]*Tt+Pt,
        D[1]*R+D[2]*T+B[1]*Rt+B[2]*Tt+Qt]
    energy=lambda v:(I[0]*v[0]**2+2*I[1]*v[0]*v[1]+I[2]*v[1]**2).upper()
    return energy(z),energy(dz)


def analytic_radial_mismatch_moduli(target,trial,element,center,radius):
    radial=acb(center+arb(0,radius),arb(0,radius))
    jets,_,_=target.form_angular_jets(radial)
    base,derivative=trial_column_bounds(trial,trial.coefficients(element,radial))
    # This bounds the analytic extension of the FINITE angular trapezoid.
    # Coefficient-conjugated trial polynomials have the same bound on the
    # conjugation-symmetric radial disk; no conjugated complex radius is used.
    return mismatch_moduli(jets,base,derivative)


def angular_mismatch_aliases(target,trial,element,left,right,sigma):
    if not sigma>0:raise ValueError('positive normalized angular strip required')
    radial=acb(real_interval(left,right))
    jets,_,_=target.form_angular_jets(radial,sigma)
    base,derivative=trial_column_bounds(trial,trial.coefficients(element,radial),sigma)
    M=mismatch_moduli(jets,base,derivative)
    factor=2*(-target.angles*sigma).exp()/(1-(-target.angles*sigma).exp())
    return [(factor*x).upper() for x in M],M


def native_samples(target,trial,coefficients):
    output=[]
    for coefficient in coefficients:
        data=zeros((target.angles,trial.d))
        data[(np.asarray(trial.frequency)//4)%target.angles]=coefficient
        output.append(target.fast_fourier.fft(data,inverse=True)*target.angles)
    return output


def paired_gram(z0,z1,inverse):
    I0,I1,I2=[x.reshape(len(x.real.lo),1) for x in inverse]
    left=I0*z0+I1*z1;right=I1*z0+I2*z1
    n,d=z0.real.lo.shape
    result=(conjugate(z0).reshape(n,d,1)*left.reshape(n,1,d)
            +conjugate(z1).reshape(n,d,1)*right.reshape(n,1,d)).sum(0)
    return result/n


def sampled_mismatch_grams(target,trial,element,radial):
    if not radial.imag==0:raise ValueError('quadrature nodes must be real')
    jets,_,_=target.form_angular_jets(radial)
    B=[extend_half(x.value,-1 if j in (1,4) else 1)
       for j,x in enumerate(jets)]
    Bt=[extend_half(jets[j].derivative,1 if j==1 else -1) for j in range(3)]
    coefficient=trial.coefficients(element,radial)
    R,T,P,Q=native_samples(target,trial,coefficient)
    Rt,Tt,Pt,Qt=native_samples(target,trial,
        [x*CBox(0.,Box(trial.frequency[:,None])) for x in coefficient])
    b0,b1,b2=[x.reshape(target.angles,1) for x in B[:3]]
    d0,d1,d2=[x.reshape(target.angles,1) for x in Bt]
    z0=b0*R+b1*T-P;z1=b1*R+b2*T-Q
    dz0=d0*R+d1*T+b0*Rt+b1*Tt-Pt
    dz1=d1*R+d2*T+b1*Rt+b2*Tt-Qt
    return paired_gram(z0,z1,B[3:]),paired_gram(dz0,dz1,B[3:])


def full_continuous_form_gate(target,left,right):
    jets,(A,K,v),_=target.form_angular_jets(acb(real_interval(left,right)),arb(0))
    # The sigma=0 path includes the entire real angular mesh gaps.
    a=A.value.real;k=K.value.real
    if not np.all(a.lo>0) or not np.all(k.lo>0):
        raise ValueError('the whole real cap interval is not proved elliptic')
    da=A.derivative/A.value
    dk=K.derivative/K.value
    off2=(A.value/K.value)*v.derivative*v.derivative
    bounds=[]
    for j in range(len(a.lo)):
        qa=da[j].to_acb().real;qk=dk[j].to_acb().real
        off=abs(off2[j].to_acb()).upper()
        # In coordinates sqrt(A)(ur+v utheta),sqrt(K) utheta,
        # B^-1/2 Btheta B^-1/2 is orthogonally similar to
        # [[Atheta/A,sqrt(A/K)vtheta],[same,Ktheta/K]].
        bound=(abs(qa+qk).upper()+
               (abs(qa-qk).upper()**2+4*off).sqrt())/2
        bounds.append(bound.upper())
    B=jets[:3]
    matrix_bound=max((scalar_upper(B[0].value)+scalar_upper(B[1].value)).upper(),
                     (scalar_upper(B[1].value)+scalar_upper(B[2].value)).upper())
    return dict(full_actual_angular_commutator=ball_record(max(bounds).upper()),
        full_real_form_operator_upper=ball_record(matrix_bound),
        diagonalized_positive_A_lower=ball_record(arb(float(np.min(a.lo)))),
        diagonalized_positive_K_lower=ball_record(arb(float(np.min(k.lo)))),
        radial_interval=[str(left),str(right)],
        angular_cells=target.angles,
        definition='C_B=ess sup ||B^(-1/2)(partial_theta B)B^(-1/2)||; complete real radial interval, all angular gaps, whole real parameter interval')


def paid_body_interval(target,trial,element,left,right,sigma,error_density,
                       rules,minimum_radius,max_order):
    h=exact_arb((right-left)/2);center=exact_arb((left+right)/2)
    length=2*h;goal=length*error_density
    aliases,angular_moduli=angular_mismatch_aliases(target,trial,element,left,right,sigma)
    alias=[length*x for x in aliases]
    if not max(alias)<goal/3:
        raise ValueError('complete mismatch angular alias exceeds its allocated error')
    selected=None;attempts=[]
    for factor in (4,2):
        radius=max(factor*h,minimum_radius)
        try:
            moduli=analytic_radial_mismatch_moduli(target,trial,element,center,radius)
        except (ValueError,ZeroDivisionError) as exc:
            attempts.append(dict(radial_factor=factor,passed=False,reason=str(exc)))
            continue
        q=h/radius
        if not q<1:raise ValueError('radial analytic disk does not contain the interval')
        for order in range(2,max_order+1):
            gauss=[(4*h*M*q**(2*order)/(1-q)).upper() for M in moduli]
            if max(gauss)<goal/3:
                selected=order,radius,moduli,gauss;break
        attempts.append(dict(radial_factor=factor,passed=selected is not None))
        if selected:break
    if selected is None:raise ValueError('no complete radial mismatch tail meets the requested error')
    order,radius,moduli,gauss=selected
    if order not in rules:rules[order]=gauss_rule(order)
    nodes,weights=rules[order]
    matrices=[zeros((trial.d,trial.d)),zeros((trial.d,trial.d))]
    for node,weight in zip(nodes,weights):
        values=sampled_mismatch_grams(target,trial,element,acb(center+h*node))
        for j in range(2):
            matrices[j]+=values[j]*CBox.from_acb(acb(h*weight))
    gate=full_continuous_form_gate(target,left,right)
    results={}
    for j,name in enumerate(('mismatch','angular_derivative_mismatch')):
        middle,arithmetic=hermitian_midpoint(matrices[j])
        results[name]=dict(
            matrix_middle=[[[float(z.real),float(z.imag)] for z in row] for row in middle],
            full_operator_error=ball_record((arithmetic+gauss[j]+alias[j]).upper()),
            directed_native_node_weight_and_selection_error=ball_record(arithmetic),
            complete_radial_Gauss_tail=ball_record(gauss[j]),
            complete_angular_alias=ball_record(alias[j]),
            actual_radial_analytic_matrix_modulus=ball_record(moduli[j]),
            actual_angular_strip_matrix_modulus=ball_record(angular_moduli[j]))
    return dict(exact_radial_interval=[str(left),str(right)],finite_element=element,
        actual_common_span=list(map(str,target.cell)),gauss_order=order,
        true_radial_analytic_radius=ball_record(radius),
        normalized_angular_strip=ball_record(sigma),attempts=attempts,
        full_continuous_coefficient_gate=gate,**results)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trial',type=Path,default=Path(
        'notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--element',type=int,required=True)
    ap.add_argument('--first-common-span',type=int,default=0)
    ap.add_argument('--last-common-span',type=int)
    ap.add_argument('--primitive-nodes',type=int,default=512)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,32))
    ap.add_argument('--minimum-analytic-radius',type=Fraction,default=Fraction(1,4096))
    ap.add_argument('--max-gauss-order',type=int,default=32)
    ap.add_argument('--max-depth',type=int,default=10)
    ap.add_argument('--error-per-length',type=Fraction,default=Fraction(1,10000))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec,ctx.cap=args.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    report=dict(kind='actual_complete_body_complementary_mismatch_angular_Gram',
        complete=False,full_cap_complete=False,source_sha256=sha(__file__),
        whole_cap_strong_flux_certified=False)
    rows=[];failed=[];rejected=[];rules={}
    def save():
        report.update(intervals=rows,unresolved_intervals=failed,rejected_parent_boxes=rejected,
            CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall)
        write_json(args.out,report)
    save()
    try:
        if args.half_width<0 or args.angles<args.primitive_nodes or args.angles&(args.angles-1):
            raise ValueError('invalid actual real parameter or angular grid')
        trial=FiniteTrial(args.trial)
        if not 0<=args.element<trial.cells:raise ValueError('unknown exact trial element')
        first,last=map(lambda x:Fraction(float(x)),trial.mesh[args.element:args.element+2])
        if not Fraction(1,4)<=first<last<=3:
            raise ValueError('this body kernel does not substitute for the natural graft/tail')
        target=AngularFamilyBody(trial.object_path,args.half_width,args.primitive_nodes,args.angles)
        common=common_cells(target)
        cuts=sorted({first,last}|{x for x in common if first<x<last})
        end=len(cuts)-1 if args.last_common_span is None else args.last_common_span
        if not 0<=args.first_common_span<end<=len(cuts)-1:
            raise ValueError('invalid exact common-span slice')
        report.update(object_path=str(trial.object_path),object_sha256=sha(trial.object_path),
            exact_center_parameter=trial.report['exact_delta_fraction'],
            exact_parameter_interval=list(map(str,target.parameter_interval)),
            exact_parameter_half_width=str(args.half_width),
            trial_report=dict(path=str(args.trial),sha256=sha(args.trial)),
            exact_trial_arrays=trial.report['arrays'],input_columns=trial.d,
            regular_mean_input_retained=True,element=args.element,
            requested_exact_radial_interval=[str(cuts[args.first_common_span]),str(cuts[end])],
            requested_common_span_indices=[args.first_common_span,end],
            finite_element_interval=[str(first),str(last)],bits=args.bits,
            primitive_nodes=args.primitive_nodes,angular_nodes=args.angles,
            kernel_contract='The body Gram is for z=B grad V-j and Dtheta z, weighted by the same actual B^-1. It is not the norm of a weak PDE residual or of Dtheta(B^-1/2 z).',
            source_derivative='Dtheta z=B grad(Dtheta V)+(Dtheta B)grad V-Dtheta j; physical angular frequencies 4k.',
            origin_inputs_sha256=target.parameter_definition['origin_inputs']['sha256'],
            direction_sha256=target.parameter_definition['direction']['sha256'])
        save()
        for left,right in zip(cuts[args.first_common_span:end],cuts[args.first_common_span+1:end+1]):
            pos=bisect_right(common,(left+right)/2)-1
            target.set_cell(common[pos],common[pos+1])
            pending=[(left,right,0)]
            while pending:
                l,r,depth=pending.pop()
                try:
                    row=paid_body_interval(target,trial,args.element,l,r,
                        exact_arb(args.normalized_strip),exact_arb(args.error_per_length),
                        rules,exact_arb(args.minimum_analytic_radius),args.max_gauss_order)
                    row['subdivision_depth']=depth;rows.append(row)
                except (ValueError,ZeroDivisionError) as exc:
                    item=dict(exact_radial_interval=[str(l),str(r)],depth=depth,reason=str(exc))
                    if depth==args.max_depth:failed.append(item)
                    else:
                        rejected.append(item);mid=(l+r)/2
                        pending.extend([(mid,r,depth+1),(l,mid,depth+1)])
                save()
            print(json.dumps(dict(element=args.element,common_span=[str(left),str(right)],
                accepted=len(rows),unresolved=len(failed)),allow_nan=False),flush=True)
            if failed:break
        rows.sort(key=lambda row:Fraction(row['exact_radial_interval'][0]))
        cursor=cuts[args.first_common_span]
        for row in rows:
            l,r=map(Fraction,row['exact_radial_interval'])
            if l!=cursor:raise ValueError('the actual mismatch cover has a gap or overlap')
            cursor=r
        report['complete']=not failed and cursor==cuts[end]
        if rows:
            report['whole_requested_angular_commutator_upper']=ball_record(max(
                arb(row['full_continuous_coefficient_gate']['full_actual_angular_commutator']['ball']).upper()
                for row in rows))
            report['integrated_operator_errors']={key:ball_record(sum((
                arb(row[key]['full_operator_error']['ball']).upper() for row in rows),arb(0)).upper())
                for key in ('mismatch','angular_derivative_mismatch')}
        report['certified_Gauss_rules']={str(n):dict(nodes=list(map(ball_record,x)),
            weights=list(map(ball_record,w))) for n,(x,w) in rules.items()}
        report['scope']=[
            'Only the explicit complete body interval, same exact finite trials, and declared whole real eta family.',
            'All primitive tails, angular aliases, radial analytic Gaussian remainder and ball arithmetic are paid.',
            'The graft, true Robin/infinite tail, regular output error, and same-family full-domain lift remain required.',
            'No complete cap R1 or numerical strong-flux bound follows from a partial body report.']
    except Exception as exc:
        report.update(failure=repr(exc),traceback=traceback.format_exc())
    report['dependency_sha256']={name:sha(Path(__file__).with_name(name)) for name in (
        'fourfold_phase_cap_parameter_comparison.py','fourfold_phase_cap_scaled_body.py',
        'fourfold_phase_cap_energy_interval.py','fourfold_phase_beta_parameter_germ.py',
        'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_affine.py',
        'fourfold_phase_actual_positive_cap.py')}
    save()
    print(json.dumps({key:report.get(key) for key in ('complete','failure',
        'whole_requested_angular_commutator_upper','integrated_operator_errors',
        'CPU_seconds','wall_seconds')},indent=2,allow_nan=False),flush=True)
    if not report['complete']:raise SystemExit(1)


if __name__=='__main__':
    main()
