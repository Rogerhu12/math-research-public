#!/usr/bin/env python3
"""Stable true-target first jets on the original positive body cap.

The exact radius powers are cancelled before differentiation. The complete
primitive, its radial derivatives and every infinite remainder are retained.
This is a scalar coefficient provider on actual common germs, not a PDE solver.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
from fourfold_codazzi_rotational_cap_jacobi import RotationalPositiveCap,real,box_from_record
from fourfold_phase_cap_scaled_body import poly_derivative,poly_multiply,poly_subtract,poly_eval,magnitude
from fourfold_phase_beta_bulk_box import Box,CBox,arb_box,cdot,reduce_box
from fourfold_phase_beta_bulk_interval import real_interval
from fourfold_phase_metric_defect import record,save,sha


class PositiveCapStableJets(RotationalPositiveCap):
    def body_jets(self,left,right):
        left,right=Fraction(left),Fraction(right)
        if not Fraction(239,1000)<=left<=right<3:raise ValueError('stable differentiated provider is restricted to the actual positive body')
        j=bisect_right(self.cuts,left)-1;gl,gr=self.cuts[j:j+2]
        if not gl<=left<=right<=gr:raise ValueError('stable derivatives cross an actual common scalar germ')
        t=self.body;t.set_cell(gl,gr);radial=acb(real_interval(left,right))
        primitive,radius=t.unit_finite_data(radial);errors=t.unit_tail_errors(radial)
        L,Lp,H,Hp,ia=t.scalar_ratios(radial,radius)
        if getattr(self,'second_ratio_germ',None)!=(gl,gr):
            a=t.scalar_poly[:,-2];ar=poly_derivative(a)
            NL=t.ratio_polynomials['Lprime_numerator'];NH=t.ratio_polynomials['Cprime_numerator']
            self.second_ratio_numerators=(
                poly_subtract(poly_multiply(a,poly_derivative(NL)),2*poly_multiply(ar,NL)),
                poly_subtract(poly_multiply(a,poly_derivative(NH)),3*poly_multiply(ar,NH)))
            self.second_ratio_germ=(gl,gr)
        offset=CBox.from_acb(radial-acb(t.anchor))
        Lpp=poly_eval(self.second_ratio_numerators[0],offset)*ia*ia*ia
        Hpp=poly_eval(self.second_ratio_numerators[1],offset)*ia*ia*ia*ia
        rev=(-np.arange(t.nodes))%t.nodes
        u=L*primitive[0]+primitive[1]
        u1=Lp*primitive[0]+L*primitive[1]+primitive[2]
        u2=Lpp*primitive[0]+2*Lp*primitive[1]+L*primitive[2]+primitive[3]
        e0=2*L*u[0,0]+cdot(u,u[rev]).sum()
        e1=2*Lp*u[0,0]+2*L*u1[0,0]+2*cdot(u,u1[rev]).sum()
        e2=(2*Lpp*u[0,0]+4*Lp*u1[0,0]+2*L*u2[0,0]
            +2*cdot(u1,u1[rev]).sum()+2*cdot(u,u2[rev]).sum())
        eps=[arb_box(math.factorial(q)*errors[0]/t.tail_radius**q) for q in range(4)]
        La,Lpa,Lppa=map(magnitude,(L,Lp,Lpp))
        eu=La*eps[0]+eps[1]
        eu1=Lpa*eps[0]+La*eps[1]+eps[2]
        eu2=Lppa*eps[0]+2*Lpa*eps[1]+La*eps[2]+eps[3]
        Mu,Mu1,Mu2=(Box(np.max(reduce_box(Box(v.magnitude_upper())).hi)) for v in (u,u1,u2))
        fee0=2*La*eu+3*(2*Mu*eu+eu*eu)
        fee1=2*Lpa*eu+2*La*eu1+6*(Mu*eu1+Mu1*eu+eu*eu1)
        fee2=(2*Lppa*eu+4*Lpa*eu1+2*La*eu2
            +6*(2*Mu1*eu1+eu1*eu1)+6*(Mu*eu2+Mu2*eu+eu*eu2))
        e0,e1,e2=e0.pad(fee0,True),e1.pad(fee1,True),e2.pad(fee2,True)
        a=radius[0];Ebar=L*L+a*a*H*H+e0
        Ebar1=2*L*Lp+2*a*a*L*H*H+2*a*a*H*Hp+e1
        R=H*H+e0*ia*ia;R1=2*H*Hp+(e1-2*L*e0)*ia*ia
        numerator=H*H*(L*L-Lp)+L*H*Hp+(L*e1-2*Lp*e0)*ia*ia/2
        numerator1=(2*H*Hp*(L*L-Lp)+H*H*(2*L*Lp-Lpp)
            +Lp*H*Hp+L*(Hp*Hp+H*Hpp)
            +(L*e2-(Lp+2*L*L)*e1+(4*L*Lp-2*Lpp)*e0)*ia*ia/2)
        v={name:real(value,name) for name,value in dict(a=a,beta=L,beta1=Lp,beta2=Lpp,
            height_ratio=H,height_ratio1=Hp,height_ratio2=Hpp,Ebar=Ebar,Ebar1=Ebar1,R=R,R1=R1,
            curvature_numerator=numerator,curvature_numerator1=numerator1).items()}
        if not all(v[k]>0 for k in ('a','Ebar','R','curvature_numerator')):
            raise ValueError('stable true positive coefficient chart unresolved')
        E,E1,Rv,Rv1,N,N1=(v[k] for k in ('Ebar','Ebar1','R','R1','curvature_numerator','curvature_numerator1'))
        v['gamma']=E.sqrt();v['gamma1']=E1/(2*v['gamma'])
        v['K']=N/(E*E);v['K1']=(N1-2*N*E1/E)/(E*E)
        v['Cref']=-(Rv/E).sqrt()
        v['lambda_ref']=N/(E*Rv)
        v['lambda_ref1']=N1/(E*Rv)-v['lambda_ref']*(E1/E+Rv1/Rv)
        # The exact rotational Codazzi identity avoids needless cancellation
        # between the two logarithmic derivatives of Cref.
        v['Cref1']=v['beta']*(v['lambda_ref']-1)*v['Cref']
        v.update({f'primitive_error_{q}':arb(float(f.hi)).upper() for q,f in enumerate((fee0,fee1,fee2))})
        v['complete_primitive_tail_A0']=errors[0]
        if not all(x.is_finite() for x in v.values()):raise ValueError('a stable scalar jet is nonfinite')
        return v,(gl,gr)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--locations',type=Fraction,nargs='+',default=[Fraction(1),Fraction(13,10),Fraction(3,2)])
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;ctx.cap=6;start=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve actual stable-jet diagnostics')
    native=json.loads(gzip.decompress(args.native.read_bytes()))
    if not native['cap_linear_reference_certified'] or native['object_sha256']!=sha(args.object):raise ValueError('different actual positive cap')
    target=PositiveCapStableJets(args.object,Fraction(native['parameter_half_width']),512);rows=[]
    for point in args.locations:
        index=next(j for j,row in enumerate(native['rows']) if Fraction(row['interval'][0])<=point<Fraction(row['interval'][1]))
        old=native['rows'][index];left,right=map(Fraction,old['interval']);values,germ=target.body_jets(left,right)
        if list(map(str,germ))!=old['actual_scalar_germ']:raise ValueError('actual common germ changed')
        overlap={k:bool(values[k].overlaps(box_from_record(old['coefficients'][k]))) for k in ('a','beta','gamma','K','Cref','lambda_ref')}
        if not all(overlap.values()):raise ValueError('stable coefficient recomputation does not overlap the complete original native')
        rows.append(dict(native_index=index,interval=old['interval'],actual_scalar_germ=old['actual_scalar_germ'],
            actual_coefficients_overlap=overlap,coefficients={k:record(v) for k,v in values.items()}))
        print(dict(interval=old['interval'],ell1=values['lambda_ref1'].str(14),K1=values['K1'].str(14)),flush=True)
    report=dict(kind='actual_positive_cap_stable_first_jet_selected_closed_boxes',complete=True,
        source_sha256=sha(__file__),object_sha256=sha(args.object),native_input_sha256=sha(args.native),
        parameter_half_width=native['parameter_half_width'],exact_center_parameter=native['exact_center_parameter'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        requested_locations=list(map(str,args.locations)),only_explicit_closed_boxes_claimed=True,rows=rows,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_cap_scaled_body.py','fourfold_phase_metric_defect.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_bulk_interval.py')},
        wall_seconds=time.monotonic()-start,nonlinear_PDE_validated=False)
    save(args.out,report)


if __name__=='__main__':main()
