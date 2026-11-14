#!/usr/bin/env python3
"""Auxiliary two-sided continuation of the SAME ruled Cartesian formula.

Certifies metric, actual curvature, and coordinate positivity on
sigma in [-1/1000,L+1/1000].  This is a mathematical extension used to
prove short geodesic existence; the original physical surface is unchanged.
"""
from __future__ import annotations
import argparse,gzip,json,time
from pathlib import Path
import flint
from flint import arb,ctx
from fd2d_k0_ruling_actual_curvature_taylor import TaylorActualRuledIntervals,jder,taylor_value
from fd2d_k0_ruling_actual_curvature_certificate import quadratic_range,digest,bounds
from fd2d_k0_ruling_angular_certificate import moment
from fd2d_k0_ruling_metric_convolution import from_bounds,magnitude_upper


class ExtendedActualCoast(TaylorActualRuledIntervals):
    def __init__(self,inlet,candidate,moments,position_modes,metric_packet,extension):
        super().__init__(inlet,candidate,moments,position_modes)
        mom=json.loads(Path(moments).read_text());self.a0=moment(mom['enclosures']['a0'])
        p=mom['parameters'];self.r,self.delta,self.c,self.kseed=(arb(p[k]) for k in ('r','D','c','k'))
        self.adjust=[moment(mom['enclosures'][k]) for k in ('u0','u2','u4')]
        saved=json.loads(Path(metric_packet).read_text())
        if saved['inlet_sha256']!=digest(inlet) or saved['moments_sha256']!=digest(moments) or not saved['passed']:
            raise ValueError('Metric residual packet is not for this actual inlet')
        keys=('frame_Gram_operator_error_upper','C_vector_upper','B_vector_upper','tangent_C_vector_upper','tangent_B_vector_upper')
        self.H,self.C,self.B,self.TC,self.TB=[from_bounds(saved[key]).upper() for key in keys]
        self.extension=arb(extension)

    def angle_box(self,left,right,den):
        pi=arb.pi();phi=(2*pi*left/den).union(2*pi*right/den)
        mid=pi*(left+right)/den;half=pi*(right-left)/den
        delta=arb(0,tuple(map(int,half.upper().man_exp())))
        Fc,nc,mc=self.fourier_jets(mid);Fi,ni,mi=self.fourier_jets(phi)
        Fi=[self.refine_field(c,i,delta) for c,i in zip(Fc,Fi)]
        ni=self.refine_field(nc,ni,delta);mi=self.refine_field(mc,mi,delta)
        if not ni[0]>0:return None
        center=self.coefficient_jets(Fc,nc,mc);interval=self.coefficient_jets(Fi,ni,mi)
        k=taylor_value(center['k'],interval['k'],delta)
        kp=taylor_value(jder(center['k']),jder(interval['k']),delta)
        c2=(2*phi).cos();c4=(4*phi).cos()
        rho=self.r+self.delta*(1-(self.kseed*(c2-self.c)).tanh())/2+self.adjust[0]+self.adjust[1]*c2+self.adjust[2]*c4
        h=rho/self.a0
        if not h>0:return None
        def endpoint(sigma):
            q2=self.rho0*self.rho0+(1+k*k)*sigma*(2*self.rho0+sigma)
            if not q2>0:return None
            return sigma*(2*self.rho0+sigma)/(self.rho0+q2.sqrt())
        wm=endpoint(-self.extension);wp=endpoint(self.L+self.extension)
        if wm is None or wp is None:return None
        slope=self.v*(1+k*k)-kp/h
        Dm=self.a+wm*slope;Dp=self.a+wp*slope
        if not (Dm>0 and Dp>0):return None
        Dlo=min(Dm.lower(),Dp.lower());hlo=h.lower();nlo=ni[0].lower()
        beta=((1+magnitude_upper(k)*magnitude_upper(k)).sqrt()/(hlo*Dlo)).upper()
        wabs=max(magnitude_upper(wm),magnitude_upper(wp))
        q=(self.TC+wabs/nlo*self.TB).upper();d=(self.C+wabs/nlo*self.B).upper()
        metric=(self.H+2*beta*q+beta*beta*d*d).upper()
        return dict(n=ni[0],h=h,wminus=wm,wplus=wp,Dminus=Dm,Dplus=Dp,
            covector_beta_upper=beta,metric_upper=metric,
            area_coeff=[taylor_value(c,i,delta) for c,i in zip(center['area'],interval['area'])],
            numerator_coeff=[taylor_value(c,i,delta) for c,i in zip(center['num'],interval['num'])],
            fnum=taylor_value(center['fn'],interval['fn'],delta))

    @staticmethod
    def radial_box(data,left,right,den):
        width=data['wplus']-data['wminus']
        wlo=(data['wminus']+arb(left)/den*width).lower()
        whi=(data['wminus']+arb(right)/den*width).upper()
        area=quadratic_range(data['area_coeff'],wlo,whi)
        if not area>0:return None
        num=quadratic_range(data['numerator_coeff'],wlo,whi)
        P=magnitude_upper(num);f=magnitude_upper(data['fnum']);lo,hi=area.lower(),area.upper()
        upper=((P+(P*P+4*f*f*hi).sqrt())/(2*lo*lo.sqrt())).upper()
        return dict(actual_area_squared=area,actual_curvature_upper=upper)


def main():
    root=Path(__file__).resolve().parent.parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--metric-packet',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-metric-convolution-01.json')
    ap.add_argument('--extension',default='1/1000')
    ap.add_argument('--initial-angle-boxes',type=int,default=256)
    ap.add_argument('--radial-boxes',type=int,default=16)
    ap.add_argument('--maximum-depth',type=int,default=5)
    ap.add_argument('--position-modes',type=int,default=96)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=160
    definition=ExtendedActualCoast(args.inlet,args.candidate,args.moments,args.position_modes,args.metric_packet,args.extension)
    assert definition.rho0>arb(39)/10 and definition.v>arb(1)/4 and definition.v<arb(3)/10
    records=[];bad=[];calls=0
    def visit(l,r,den,depth):
        nonlocal calls
        calls+=1;data=definition.angle_box(l,r,den);ok=data is not None;rows=[]
        if ok:
            ok=bool(data['metric_upper']<arb(1)/1000000)
        if ok:
            for j in range(args.radial_boxes):
                row=definition.radial_box(data,j,j+1,args.radial_boxes)
                if row is None or not row['actual_curvature_upper']<arb(73)/10:ok=False;break
                rows.append(row)
        if ok:
            area=rows[0]['actual_area_squared'];curv=rows[0]['actual_curvature_upper']
            for row in rows[1:]:
                area=area.union(row['actual_area_squared']);curv=curv.union(row['actual_curvature_upper'])
            keys=('n','h','wminus','wplus','Dminus','Dplus','covector_beta_upper','metric_upper')
            records.append(dict(angle_left_over_2pi=[l,den],angle_right_over_2pi=[r,den],depth=depth,
                radial_uniform_cells=args.radial_boxes,all_radial_cells_verified=True,
                **{key:bounds(data[key]) for key in keys},actual_area_squared=bounds(area),actual_curvature_upper=bounds(curv)))
        elif depth<args.maximum_depth:
            visit(2*l,l+r,2*den,depth+1);visit(l+r,2*r,2*den,depth+1)
        else:bad.append(dict(left_over_2pi=[l,den],right_over_2pi=[r,den],depth=depth))
    for j in range(args.initial_angle_boxes):
        visit(j,j+1,args.initial_angle_boxes,0)
        if (j+1)%32==0:print(json.dumps(dict(progress=j+1,accepted=len(records),unresolved=len(bad),seconds=time.monotonic()-started)),flush=True)
    report=dict(schema='fd2d-same-ruled-surface-auxiliary-extension-certificate-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),moments_sha256=digest(args.moments),metric_residual_packet_sha256=digest(args.metric_packet),
        helper_sources={name:digest(Path(__file__).with_name(name)) for name in ('fd2d_k0_ruling_actual_curvature_taylor.py','fd2d_k0_ruling_actual_curvature_certificate.py','fd2d_k0_ruling_angular_certificate.py','fd2d_k0_ruling_metric_convolution.py')},
        flint_version=flint.__version__,precision_bits=160,extension=args.extension,
        original_physical_surface_changed=False,auxiliary_formula='Same X+w(e1-(m/n)e2), extended only for the short-geodesic argument',
        original_sigma_range=[bounds(arb(0)),bounds(definition.L)],extended_sigma_range=[bounds(-definition.extension),bounds(definition.L+definition.extension)],
        radius_rhoc=bounds(definition.rho0),v=bounds(definition.v),
        strict_claims=['actual immersion','coordinate D>0 and n>0','actual common flat metric relative operator error < 1e-6','actual principal curvature absolute < 73/10','rho_c > 39/10','1/4 < v < 3/10'],
        curvature_or_metric_exact_compatibility_assumed=False,full_reach_certificate=False,
        passed=not bad,accepted_angle_boxes=len(records),accepted_radial_boxes=len(records)*args.radial_boxes,
        interval_angle_evaluations=calls,unresolved=bad,boxes=records,seconds=time.monotonic()-started,
        strict_bounds_are_binary_fields=True,displays_not_outward_rounded=True)
    raw=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if args.out.suffix=='.gz':args.out.write_bytes(gzip.compress(raw,mtime=0))
    else:
        if len(raw)>1000000:raise ValueError('Use .json.gz for data over 1 MB')
        args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),bytes=args.out.stat().st_size,passed=report['passed'],angles=len(records),unresolved=len(bad),seconds=report['seconds'])),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
