#!/usr/bin/env python3
"""Actual compact-metric body and natural graft through third target jets.

Every call stays on a true scalar germ and a compact-control polynomial
piece. The original body primitive retains all its Fourier tails. On the
actual natural graft a complete Wiener Taylor majorant pays the entire
primitive correction through its required fifth radial jet. No existing
provider is modified and no candidate or target polynomial is extrapolated.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,acb_series,ctx
from fourfold_codazzi_reciprocal_compact_target_jets import (
    ReciprocalCompactTargetJets,real,add,scale,power,exponential,bump_series)
from fourfold_codazzi_cubic_target_jets import series_sqrt
from fourfold_codazzi_high_target_jets import series_mul,series_inv,series_dr
from fourfold_phase_beta_bulk_box import CBox,Box,cdot,reduce_box,arb_box
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_natural_exterior_graft import (
    NaturalGraft,real_coefficient,absolute_jet,sinh,cosh_minus_one,modulus)
from fourfold_phase_metric_defect import record,save,sha
from fourfold_codazzi_rotational_cap_jacobi import box_from_record


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def assemble(aa,L,H,energy,left,right,rad,nu,primitive_bound,fees):
    """Taylor arithmetic for the exact cancelled target, not sampled jets."""
    ia2=power(series_inv(aa),2)
    L2,H2=power(L,2),power(H,2)
    Ebar=add(add(L2,series_mul(power(aa,2),H2)),energy)
    Lp,Hp,ep=series_dr(L),series_dr(H),series_dr(energy)
    N=add(series_mul(H2,add(L2,scale(Lp,-1))),series_mul(series_mul(L,H),Hp))
    N=add(N,scale(series_mul(add(series_mul(L,ep),scale(series_mul(Lp,energy),-2)),ia2),arb(1)/2))
    oldK=series_mul(N,power(series_inv(Ebar),2))
    hh=bump_series(left,right,rad);n=exact_arb(nu)
    expnu=exponential(scale(hh,n));expm1=[(n*hh[0]).expm1()]+expnu[1:]
    G=series_mul(Ebar,expnu)
    R=add(add(H2,series_mul(energy,ia2)),series_mul(series_mul(Ebar,ia2),expm1))
    if not (aa[0]>0 and Ebar[0]>0 and G[0]>0 and R[0]>0):
        raise ValueError('the complete actual rotational target chart is unresolved')
    K=series_mul(add(oldK,scale(series_mul(series_mul(series_mul(L,series_dr(hh)),ia2),
        series_inv(Ebar)),n/2)),series_inv(expnu))
    gamma=series_sqrt(G);s=scale(series_sqrt(series_mul(G,series_inv(R))),-1)
    result=dict(a=aa[0],Ebar=Ebar[0],controlled_Ebar=G[0],controlled_scaled_gap=R[0],
        Cref=1/s[0],nu=n,compact_bump=hh[0],complete_primitive_tail_A0=primitive_bound)
    for name,values in (('gamma',gamma),('beta',L),('K',K),('s',s)):
        if len(values)<4:raise ValueError('an actual third jet is missing')
        for j in range(4):result[name+(str(j) if j else '')]=math.factorial(j)*values[j]
    for j,fee in enumerate(fees):result['complete_scaled_energy_error_'+str(j)]=fee
    if not all(x.is_finite() for x in result.values()):raise ValueError('a full actual target jet is nonfinite')
    return result


class ExtendedBodyTargetJets(ReciprocalCompactTargetJets):
    def coefficients(self,left,right,nu):
        left,right,nu=Fraction(left),Fraction(right),Fraction(nu)
        if not 0<=left<=right<=3:raise ValueError('the actual finite body is [0,3]')
        # Preserve the already published prefix arithmetic exactly.
        if right<=Fraction(3,2):return super().coefficients(left,right,nu)
        j=bisect_right(self.cuts,left)-1
        if left==3:j-=1
        gl,gr=self.cuts[j:j+2]
        if not gl<=left<=right<=gr:raise ValueError('the new body box crosses an actual scalar germ')
        self.set_cell(gl,gr);rad=real_interval(left,right)
        primitive,_=self.unit_finite_data(acb(rad));_,_,radius,height=self.last_scalar
        aa=[real(radius[j],'a'+str(j))/math.factorial(j) for j in range(6)]
        zz=[real(height[j],'z'+str(j))/math.factorial(j) for j in range(6)]
        if not aa[0]>0:raise ValueError('actual body radius is not strictly positive')
        ia=series_inv(aa);L=series_mul(series_dr(aa),ia)
        H=series_mul(series_dr(zz),power(ia,2));Ld=[math.factorial(j)*z for j,z in enumerate(L)]
        Lbox=[CBox(arb_box(z)) for z in Ld]
        tail=self.unit_tail_errors(acb(rad),arb(0))[0]
        eps=[(math.factorial(j)*tail/self.tail_radius**j).upper() for j in range(6)]
        uu=[];eu=[];Mu=[]
        for order in range(5):
            value=primitive[order+1];fee=eps[order+1]
            for j in range(order+1):
                value+=math.comb(order,j)*Lbox[j]*primitive[order-j]
                fee+=math.comb(order,j)*abs(Ld[j])*eps[order-j]
            uu.append(value);eu.append(fee.upper())
            Mu.append(arb(float(np.max(reduce_box(Box(value.magnitude_upper())).hi))).upper())
        reverse=(-np.arange(self.nodes))%self.nodes;energy=[];fees=[]
        for order in range(5):
            finite=CBox(0.);fee=arb(0)
            for j in range(order+1):
                c=math.comb(order,j);k=order-j
                finite+=2*c*Lbox[j]*uu[k][0,0]+c*cdot(uu[j],uu[k][reverse]).sum()
                fee+=2*c*abs(Ld[j])*eu[k]+3*c*(Mu[j]*eu[k]+Mu[k]*eu[j]+eu[j]*eu[k])
            energy.append((real(finite,'actual_scaled_energy_'+str(order))+arb(0,fee.upper()))/math.factorial(order))
            fees.append(fee.upper())
        return assemble(aa,L,H,energy,left,right,rad,nu,tail,fees),(gl,gr)


class ReciprocalFullTargetJets:
    """Same coefficients(left,right,nu)->(values,germ) interface on [0,25/8].

    A point r=3 defaults to the left body germ. For the right one-sided
    third jet at that interface call graft_coefficients(3,3,nu) explicitly.
    No cell crossing r=3, an original body germ, or a bump join is accepted.
    """
    def __init__(self,object_path,half_width=Fraction(0),nodes=512):
        self.object_path=Path(object_path);self.half_width=Fraction(half_width);self.nodes=nodes
        self.body=ExtendedBodyTargetJets(object_path,self.half_width,nodes);self._graft=None
        self.cuts=sorted(set(self.body.cuts)|{Fraction(1,20),Fraction(9,50),Fraction(3),Fraction(25,8)})
        self.last_part=None

    @property
    def graft(self):
        if self._graft is None:self._graft=NaturalGraft(self.object_path,self.half_width,Fraction(1,8))
        return self._graft

    def coefficients(self,left,right,nu):
        left,right,nu=Fraction(left),Fraction(right),Fraction(nu)
        if not 0<=left<=right<=Fraction(25,8):raise ValueError('outside the actual body and natural graft')
        if right<=3:
            self.last_part='body';return self.body.coefficients(left,right,nu)
        if left<3:raise ValueError('a target cell crosses the actual body/graft join')
        return self.graft_coefficients(left,right,nu)

    def graft_coefficients(self,left,right,nu):
        left,right,nu=Fraction(left),Fraction(right),Fraction(nu)
        if not 3<=left<=right<=Fraction(25,8):raise ValueError('outside the actual natural graft')
        old=ctx.cap;ctx.cap=max(old,6)
        try:
            jets=self.graft.jets(left-3,right-3)
            aa=[real_coefficient(jets['radius'],j) for j in range(6)]
            L=[(j+1)*real_coefficient(jets['log_radius'],j+1) for j in range(5)]
            H=[real_coefficient(jets['slope_ratio'],j) for j in range(5)]
            # All Taylor coefficients of these series are nonnegative majorants.
            B=acb_series([acb(sum((modulus(v[j]) for v in jets['beta']),arb(0))) for j in range(6)])
            G=acb_series([acb(sum((modulus(v[j]) for v in jets['gamma']),arb(0))) for j in range(6)])
            cb,cg=cosh_minus_one(B),cosh_minus_one(G)
            dx=(1+cg)*sinh(B);dy=cb+cg+cb*cg;dz=sinh(G);dh=dx+dy
            La=acb_series([acb(abs(v).upper()) for v in L])
            horizontal=La*dh+dh.derivative();vertical=(La*dz+dz.derivative())/4
            mean_energy=2*La*(La*dy+dy.derivative())+horizontal**2+vertical**2
            maj=[modulus(mean_energy[j]) for j in range(5)]
            energy=[arb(0,z) for z in maj]
            fees=[(math.factorial(j)*z).upper() for j,z in enumerate(maj)]
            # This is a bound for the whole unexpanded primitive correction,
            # not a zero omitted-Fourier-tail claim on the graft.
            primitive=(modulus(dh[0])+modulus(dz[0])/4).upper()
            result=assemble(aa,L,H,energy,left,right,real_interval(left,right),nu,primitive,fees)
            self.last_part='natural_graft_full_Wiener_jet'
            return result,(Fraction(3),Fraction(25,8))
        finally:ctx.cap=old


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--reference',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--nu',type=Fraction,default=Fraction(-80394554034525,2251799813685248))
    ap.add_argument('--locations',type=Fraction,nargs='+',default=[Fraction(3,2),Fraction(2),Fraction(14,5),Fraction(3),Fraction(301,100),Fraction(49,16),Fraction(25,8)])
    ap.add_argument('--width',type=Fraction,default=Fraction(1,100000))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual full-provider attempt')
    ref=read(args.reference)
    if not ref['complete'] or ref['object_sha256']!=sha(args.object):raise ValueError('the complete actual reference differs')
    if args.half_width>Fraction(ref['parameter_half_width']):raise ValueError('reference comparison has a smaller parameter interval')
    t=ReciprocalFullTargetJets(args.object,args.half_width,512)
    doc=dict(kind='actual_full_body_and_natural_graft_third_target_jets_selected_boxes',complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.object,args.reference)},
        object_sha256=sha(args.object),
        actual_nu=str(args.nu),parameter_half_width=str(args.half_width),whole_requested_parameter_interval=True,
        complete_infinite_primitive_retained=True,only_listed_actual_closed_boxes_claimed=True,
        supported_domain=['0','25/8'],all_original_germs_and_compact_joins_respected=True,
        graft_primitive_error_is_a_full_Wiener_majorant_not_zero=True,
        coefficient_derivative_orders=[0,1,2,3],coefficient_names=['gamma','beta','K','s'],
        third_derivatives_at_interfaces_are_one_sided_no_global_C3_claim=True,rows=[],failure=None,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_reciprocal_compact_target_jets.py','fourfold_codazzi_cubic_target_jets.py',
            'fourfold_codazzi_high_target_jets.py','fourfold_phase_metric_defect.py',
            'fourfold_phase_natural_exterior_graft.py','fourfold_phase_exterior_entry_jet.py',
            'fourfold_phase_cap_scaled_body.py')})
    try:
        for point in args.locations:
            if not Fraction(3,2)<=point<=Fraction(25,8):raise ValueError('this check covers the new outer domain')
            candidates=[r for r in ref['rows'] if Fraction(r['interval'][0])<=point<=Fraction(r['interval'][1])]
            if not candidates:raise ValueError('no true original reference box at the requested location')
            original=next((r for r in candidates if Fraction(r['interval'][0])==point and point!=3),candidates[0])
            lo,hi=map(Fraction,original['interval'])
            if point==3:left=max(lo,point-args.width);right=point
            elif point==Fraction(25,8):left=max(lo,point-args.width);right=point
            else:left=max(lo,point-args.width/2);right=min(hi,point+args.width/2)
            value,germ=t.coefficients(left,right,args.nu)
            overlap={k:bool(value[k].overlaps(box_from_record(original['coefficients'][k]))) for k in ('a','beta','gamma','K','Cref')}
            if not all(overlap.values()):raise ValueError('new actual jets fail the original lower-coefficient identity')
            row=dict(requested_location=str(point),interval=list(map(str,(left,right))),actual_scalar_germ=list(map(str,germ)),
                actual_part=t.last_part,original_reference_interval=original['interval'],original_lower_order_overlap=overlap,
                coefficients={k:record(v) for k,v in value.items()})
            doc['rows'].append(row);save(args.out,doc)
            print(dict(point=str(point),part=t.last_part,K=value['K'].str(12),K3=value['K3'].str(12)),flush=True)
        # A separate genuine right-side point jet is paid at the C4 join.
        values,germ=t.graft_coefficients(Fraction(3),Fraction(3),args.nu)
        doc['right_side_r3_graft_jet']=dict(actual_scalar_germ=list(map(str,germ)),coefficients={k:record(v) for k,v in values.items()})
        doc.update(complete=True,all_requested_actual_boxes_completed=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
