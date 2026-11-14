#!/usr/bin/env python3
"""The actual positive-body form after exact cancellation of radius powers.

This is the same exact affine, symmetric, infinite-primitive graph as BodyForm.
The primitive of T-T_circle is evaluated before multiplication by a; all its
infinite tails remain present.  D=a^2 D2, M=a^2 M2, W=a^2 W2 and H=a H1 are
cancelled algebraically in the grounded form.  The target curvature is likewise
formed from L=a'/a and C=Z'/a^2 without subtracting large radius-scaled terms.

The entry point compares independently assembled true native enclosures and
can certify a requested closed body span.  No finite point comparison is a
claim about a whole cap.  Scalar and raw-spline caches retain one common span.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_bulk_box import (
    CBox, Box, cstack, zeros, cdot, trig_jets, jet_product, complex_sincos,
    arb_box, reduce_box, stack)
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_interval import primitive_fourier_budget, ball_record
from fourfold_phase_cap_energy_interval import (
    BodyForm, FiniteTrial, gauss_rule, certify_interval, sha)
from fourfold_phase_uniform_tail import up


def poly_eval(coefficients, value):
    result = CBox(0.)
    for coefficient in coefficients[::-1]:
        result = result*value+coefficient
    return result


def poly_derivative(coefficients):
    return cstack([j*coefficients[j] for j in range(1,len(coefficients.real.lo))])


def poly_multiply(left, right):
    nl,nr = len(left.real.lo),len(right.real.lo)
    answer = zeros((nl+nr-1,))
    for i in range(nl):
        for j in range(nr):
            answer[i+j] = answer[i+j]+left[i]*right[j]
    return answer


def poly_subtract(left, right):
    answer = zeros((max(len(left.real.lo),len(right.real.lo)),))
    for i in range(len(left.real.lo)):
        answer[i] = answer[i]+left[i]
    for i in range(len(right.real.lo)):
        answer[i] = answer[i]-right[i]
    return answer


def magnitude(value):
    return Box(float(np.max(value.magnitude_upper())))


class ScaledBodyForm(BodyForm):
    def set_cell(self,left,right):
        cell=Fraction(left),Fraction(right)
        if self.cell != cell:
            # These caches contain exact polynomial germs, not mathematical
            # state.  Retaining only the current common cell bounds memory.
            self.fast_cell_cache.clear()
            self.span_cache.clear()
        previous=self.cell
        super().set_cell(*cell)
        if previous == cell and hasattr(self,'ratio_polynomials'):
            return
        a,z=self.scalar_poly[:,-2],self.scalar_poly[:,-1]
        ar,zr=poly_derivative(a),poly_derivative(z)
        arr,zrr=poly_derivative(ar),poly_derivative(zr)
        aa=poly_multiply(a,a)
        # The chosen real dyadics only reorganize an exact identity.  They
        # neither replace the radius nor alter its derivatives.
        l0=float((ar[0]/a[0]).to_acb().real.mid())
        c0=float((zr[0]/(a[0]*a[0])).to_acb().real.mid())
        self.ratio_polynomials=dict(
            L0=l0,C0=c0,
            L_remainder=poly_subtract(ar,l0*a),
            C_remainder=poly_subtract(zr,c0*aa),
            Lprime_numerator=poly_subtract(poly_multiply(a,arr),poly_multiply(ar,ar)),
            Cprime_numerator=poly_subtract(poly_multiply(a,zrr),2*poly_multiply(ar,zr)))

    def unit_finite_data(self,radial):
        delta=CBox.from_acb(radial-acb(self.anchor))
        jet=zeros((4,2*self.modes+2))
        for n in range(20,-1,-1):
            jet=jet*delta+cstack([self.scalar_poly[n],jet[0],2*jet[1],3*jet[2]])
        beta,gamma=jet[:,:self.modes],jet[:,self.modes:2*self.modes]
        radius,height=jet[:,-2],jet[:,-1]
        self.last_scalar=beta,gamma,radius,height
        b=(beta.reshape(4,self.modes,1)*self.fast_sines.reshape(1,self.modes,self.nodes)).sum(1)
        g=(gamma.reshape(4,self.modes,1)*self.fast_sines.reshape(1,self.modes,self.nodes)).sum(1)
        sb,_=trig_jets(b);sg,_=trig_jets(g)
        shb,_=trig_jets(b/2);shg,_=trig_jets(g/2)
        cmb,cmg=-2*jet_product(shb,shb),-2*jet_product(shg,shg)
        one=zeros((4,self.nodes));one[0]=1
        tangent_difference=cstack([
            -jet_product(one+cmg,sb),cmg+cmb+jet_product(cmg,cmb),sg],-1)
        coefficient=self.fast_fourier.fft(tangent_difference,1)/self.nodes
        primitive=zeros((4,self.nodes,3))
        n=np.asarray(self.frequency)
        ii=CBox(0.,Box(n.reshape(1,-1)))
        denominator=Box((1-n*n).reshape(1,-1))
        primitive[:,:,0]=(ii*coefficient[:,:,0]+coefficient[:,:,1])/denominator
        primitive[:,:,1]=(-coefficient[:,:,0]+ii*coefficient[:,:,1])/denominator
        nz=np.flatnonzero(n)
        primitive[:,nz,2]=coefficient[:,nz,2]/CBox(0.,Box(n[nz].reshape(1,-1)))
        primitive[:,self.nodes//2,:]=0
        primitive[:,0,1],primitive[:,0,2]=0,0
        pos=np.arange(1,self.nodes//2)
        for j,parity in enumerate((1,-1,1)):
            value=(primitive[:,pos,j]+parity*primitive[:,-pos,j])/2
            primitive[:,pos,j],primitive[:,-pos,j]=value,parity*value
        self.unit_primitive=primitive
        return primitive,radius

    def unit_tail_errors(self,radial,inner_sigma=arb(0)):
        rho=arb_box(abs(radial-acb(self.anchor)).upper()+self.tail_radius).hi
        bounds=np.zeros(2*self.modes+2)
        for n in range(20,-1,-1):
            bounds=up(up(bounds*rho)+self.scalar_abs[n])
        phase=sum(((arb(float(bounds[j]))+arb(float(bounds[self.modes+j])))
                   *(self.tail_sigma*(j+1)).cosh()
                   for j in range(self.modes)),arb(0)).upper()
        key=inner_sigma.str(35)
        if key not in self.tail_factor_cache:
            self.tail_factor_cache[key]=primitive_fourier_budget(
                self.nodes,self.tail_sigma,inner_sigma,self.tail_radius,
                arb(1),arb(0),arb(1))[0]
        # Unit tangent difference; there is deliberately no factor |a|.
        factor=phase*phase.exp()
        return [(x*factor).upper() for x in self.tail_factor_cache[key]]

    def scalar_ratios(self,radial,radius):
        delta=CBox.from_acb(radial-acb(self.anchor))
        p=self.ratio_polynomials
        ia=1/radius[0]
        L=p['L0']+poly_eval(p['L_remainder'],delta)*ia
        C=p['C0']+poly_eval(p['C_remainder'],delta)*ia*ia
        Lp=poly_eval(p['Lprime_numerator'],delta)*ia*ia
        Cp=poly_eval(p['Cprime_numerator'],delta)*ia*ia*ia
        return L,Lp,C,Cp,ia

    def normalized_data(self,radial):
        primitive,radius=self.unit_finite_data(radial)
        errors=self.unit_tail_errors(radial)
        L,Lp,C,Cp,ia=self.scalar_ratios(radial,radius)
        reverse=(-np.arange(self.nodes))%self.nodes
        u=L*primitive[0]+primitive[1]
        ur=Lp*primitive[0]+L*primitive[1]+primitive[2]
        ebar=2*L*u[0,0]+cdot(u,u[reverse]).sum()
        ebar_r=2*Lp*u[0,0]+2*L*ur[0,0]+2*cdot(u,ur[reverse]).sum()
        eps=[arb_box(math.factorial(j)*errors[0]/self.tail_radius**j) for j in range(3)]
        Labs,Lpabs=magnitude(L),magnitude(Lp)
        eu=Labs*eps[0]+eps[1]
        eur=Lpabs*eps[0]+Labs*eps[1]+eps[2]
        Mu=Box(np.max(reduce_box(Box(u.magnitude_upper())).hi))
        Mur=Box(np.max(reduce_box(Box(ur.magnitude_upper())).hi))
        fee0=2*Labs*eu+3*(2*Mu*eu+eu*eu)
        fee1=2*Lpabs*eu+2*Labs*eur+6*(Mu*eur+Mur*eu+eu*eur)
        real=radial.imag==0
        ebar,ebar_r=ebar.pad(fee0,real),ebar_r.pad(fee1,real)
        a=radius[0]
        Ebar=L*L+a*a*C*C+ebar
        # The mean vertical derivative of the unit primitive is zero.
        # E=a^2 Ebar and the exact target K formula then gives this identity.
        K=(C*C*(L*L-Lp)+L*C*Cp+(L*ebar_r-2*Lp*ebar)*ia*ia/2)/(Ebar*Ebar)
        if real:
            K=CBox(K.real)
        self.last_scaled_diagnostics=dict(
            Ebar=Ebar.to_acb(),L=L.to_acb(),Lprime=Lp.to_acb(),
            C=C.to_acb(),Cprime=Cp.to_acb(),
            normalized_E_errors=[float(fee0.hi),float(fee1.hi)])
        return primitive,K,errors,real,(L,Lp,C,Cp,ia)

    def unit_fields(self,radial,coefficient,errors,real,sigma=None):
        if sigma is not None:
            if not real:
                raise ValueError('complex angular cover requires real radial input')
            errors=self.unit_tail_errors(radial,sigma+arb.pi()/self.angles)
            modes=np.abs(np.asarray(self.frequency)//4)
            re=stack([arb_box(k*arb.pi()/self.angles+(k*sigma).cosh()-1)
                      for k in modes]).reshape(-1,1)
            im=stack([arb_box((k*sigma).sinh()) for k in modes]).reshape(-1,1)
        fields=[]
        for j in range(2):
            values=coefficient[j]
            fee=arb_box(math.factorial(j)*errors[0]/self.tail_radius**j)
            data=zeros((self.angles,3))
            data[(np.asarray(self.frequency)//4)%self.angles]=values
            samples=(self.fast_fourier.fft(data,inverse=True)*self.angles)[:self.sample_count]
            if sigma is None:
                fields.append(samples.pad(fee,real))
            else:
                absolute=Box(values.magnitude_upper())
                rf=(fee+reduce_box(absolute*re)).hi
                imf=(fee+reduce_box(absolute*im)).hi
                fields.append(CBox(samples.real+Box(-rf,rf),Box(-imf,imf)))
        if sigma is not None:
            key=sigma.str(35)
            if key not in self.angle_shift_cache:
                gap,width=arb_box(arb.pi()/self.angles).hi,arb_box(sigma).hi
                shift=CBox(Box(-gap,gap),Box(-width,width))
                ss,cc=self.angle_sines,self.angle_cosines
                s,c=complex_sincos(CBox(np.arange(1,self.modes+1))*shift)
                s,c=s.reshape(-1,1),c.reshape(-1,1)
                self.angle_shift_cache[key]=ss*c+cc*s,cc*c-ss*s
        return fields

    def form_parts(self,radial,sigma=None):
        primitive,K,errors,real,ratios=self.normalized_data(radial)
        P,Pr=self.unit_fields(radial,primitive,errors,real,sigma)
        beta,gamma,radius,height=self.last_scalar
        L,_,C,_,ia=ratios
        a=radius[0]
        X0=L*(1+P[:,0])+Pr[:,0]
        X1=L*P[:,1]+Pr[:,1]
        Xz=C+(L*P[:,2]+Pr[:,2])*ia
        ss,cc=(self.angle_sines,self.angle_cosines) if sigma is None else self.angle_shift_cache[sigma.str(35)]
        frequency=CBox((4*np.arange(1,self.modes+1)).reshape(-1,1))
        phase=lambda v,j:(v[j].reshape(-1,1)*ss).sum()
        angular=lambda v:(v[0].reshape(-1,1)*frequency*cc).sum()
        b,g,br,gr,bt,gt=phase(beta,0),phase(gamma,0),phase(beta,1),phase(gamma,1),angular(beta),angular(gamma)
        sb,cb=complex_sincos(b);sg,cg=complex_sincos(g)
        h1=-sb*X0+cb*X1
        v1=-cb*X0-sb*X1
        Q2=cg*Xz-sg*ia*h1
        D2=(1+bt)*cg*Q2-gt*ia*v1
        M2=br*cg*Q2-gr*ia*v1
        W2=v1*v1+a*a*Q2*Q2
        Fh1=-sb*(1+P[:,0])+cb*P[:,1]
        Fv1=-cb*(1+P[:,0])-sb*P[:,1]
        Fz=height[0]+a*P[:,2]
        Fq=cg*Fz-a*sg*Fh1
        H1=Fq*v1-a*a*Fv1*Q2
        return dict(D=D2,M=M2,W=W2,H=H1,Z=Fz,K=K,
                    primitive_errors=errors,real=real,
                    scaling='D=a^2 D2; M=a^2 M2; W=a^2 W2; H=a H1')


def common_cells(target):
    cuts={Fraction(0),Fraction(3)}
    for key,values in target.frozen.items():
        if key.endswith('_knots'):
            for x in values:
                q=Fraction(float(x));cuts.update((q,-q))
    return sorted(cuts)


def overlap(a,b):
    return bool(np.all((a.real.lo<=b.real.hi)&(b.real.lo<=a.real.hi)
                       &(a.imag.lo<=b.imag.hi)&(b.imag.lo<=a.imag.hi)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    parser.add_argument('--angles',type=int,default=1024)
    parser.add_argument('--primitive-nodes',type=int,default=512)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--energy-element',type=int)
    parser.add_argument('--energy-span',type=int,default=0)
    parser.add_argument('--gauss-order',type=int,default=10)
    parser.add_argument('--max-depth',type=int,default=8)
    parser.add_argument('--radial-factor',type=Fraction,default=Fraction(4))
    parser.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,32))
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();ctx.prec,ctx.cap=args.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    trial=FiniteTrial(args.trial)
    parameters=(trial.object_path,args.primitive_nodes,args.angles,arb('.003'),arb('.0025'),arb('.32'))
    target=ScaledBodyForm(*parameters)
    cuts=common_cells(target)
    report=dict(kind='same_actual_graph_radius_cancelled_positive_body',complete=False,
        source_sha256=sha(__file__),object_sha256=trial.report['object_sha256'],
        exact_delta_fraction=trial.report['exact_delta_fraction'],
        trial_report_path=str(args.trial),trial_report_sha256=sha(args.trial),
        primitive_nodes=args.primitive_nodes,angular_nodes=args.angles,bits=args.bits,
        full_positive_cap_complete=False,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_energy_interval.py','fourfold_phase_positive_family_outer.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_affine.py')})
    def save():
        report['CPU_seconds']=time.process_time()-cpu
        report['wall_seconds']=time.monotonic()-wall
        args.out.parent.mkdir(parents=True,exist_ok=True)
        tmp=args.out.with_suffix(args.out.suffix+'.tmp')
        tmp.write_text(json.dumps(report,indent=2)+'\n');tmp.replace(args.out)
    if args.energy_element is None:
        old=BodyForm(*parameters)
        rows=[];report['comparisons']=rows
        for r in (Fraction(1,4),Fraction(1),Fraction(3)):
            k=bisect_right(cuts,r)-1
            if r==3:k-=1
            cell=cuts[k:k+2]
            for obj in (target,old):obj.set_cell(*cell)
            radial=acb(exact_arb(r))
            newp=target.form_parts(radial);oldp=old.form_parts(radial)
            newv=target.form_values(radial);oldv=old.form_values(radial)
            row=dict(radial=str(r),true_common_span=list(map(str,cell)),
                true_target_K_overlap=overlap(newp['K'],oldp['K']),
                true_form_and_inverse_overlaps=[overlap(x,y) for x,y in zip(newv,oldv)],
                K_new=ball_record(newp['K'].to_acb().real),
                K_previous=ball_record(oldp['K'].to_acb().real),
                new_max_component_radii=[float(np.max((z.real.hi-z.real.lo)/2)) for z in newv],
                previous_max_component_radii=[float(np.max((z.real.hi-z.real.lo)/2)) for z in oldv])
            row['passed']=row['true_target_K_overlap'] and all(row['true_form_and_inverse_overlaps'])
            rows.append(row);save();print(json.dumps(row),flush=True)
        report['complete']=all(row['passed'] for row in rows)
        report['scope']='Independent true point enclosures only; all infinite primitive tails included. No whole cap integral claim.'
    else:
        element=args.energy_element
        left,right=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
        if not Fraction(1,4)<=left<right<=3:
            raise ValueError('this entry covers body elements only, not the natural graft')
        pieces=sorted({left,right}|{q for q in cuts if left<q<right})
        a,b=pieces[args.energy_span:args.energy_span+2]
        k=bisect_right(cuts,(a+b)/2)-1
        target.set_cell(cuts[k],cuts[k+1])
        nodes,weights=gauss_rule(args.gauss_order)
        rows,failures,subdivisions=[],[],[]
        report.update(dict(requested_exact_radial_interval=[str(a),str(b)],
            selected_true_common_span=list(map(str,target.cell)),
            gauss_order=args.gauss_order,gauss_nodes=list(map(ball_record,nodes)),
            gauss_weights=list(map(ball_record,weights)),intervals=rows,
            rejected_parent_boxes=subdivisions,unresolved_intervals=failures))
        pending=[(a,b,0)]
        while pending:
            left,right,depth=pending.pop()
            try:
                row=certify_interval(target,trial,element,left,right,nodes,weights,
                    exact_arb(args.radial_factor),exact_arb(args.normalized_strip))
                row['subdivision_depth']=depth;rows.append(row)
                print(json.dumps(dict(accepted=row['exact_radial_interval'],depth=depth,
                    primal_error=row['primal_energy']['full_operator_error']['ball'],
                    dual_error=row['dual_energy']['full_operator_error']['ball'])),flush=True)
            except (ValueError,ZeroDivisionError) as exc:
                item=dict(exact_radial_interval=[str(left),str(right)],depth=depth,reason=str(exc))
                if depth==args.max_depth:failures.append(item)
                else:
                    subdivisions.append(item);mid=(left+right)/2
                    pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
            report['pending']=[[str(l),str(r),d] for l,r,d in pending];save()
        rows.sort(key=lambda row:Fraction(row['exact_radial_interval'][0]))
        cursor=a
        for row in rows:
            l,r=map(Fraction,row['exact_radial_interval'])
            if l!=cursor:break
            cursor=r
        report['complete']=not failures and cursor==b
        report['scope']='Only the explicitly covered body span: true infinite primitives, directed node/weight errors, full Gaussian analytic tail, and complete angular aliases. The whole cap is not yet certified.'
    save()
    print(json.dumps(dict(complete=report['complete'],CPU_seconds=report['CPU_seconds'],wall_seconds=report['wall_seconds'])),flush=True)
    if not report['complete']:raise SystemExit('requested actual positive-body check incomplete')


if __name__=='__main__':
    main()
