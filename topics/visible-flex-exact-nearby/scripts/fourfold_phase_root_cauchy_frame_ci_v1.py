#!/usr/bin/env python3
"""Actual physical and grounded Cauchy frames with full primitive fees."""
from __future__ import annotations
import argparse,time
from collections import deque
from fractions import Fraction
from pathlib import Path
from flint import acb,arb,ctx
from fourfold_native_series_fft import NativeSeriesFFT
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_phase_root_finite_grid_v2 import GridRootModel
from fourfold_phase_root_potential_complex_strip import ComplexRootModel,sin_cos
from fourfold_phase_canonical_root_jets import along_shear,derivative,dot,cross,jet_function,trim


class FrameFormula:
    def frame(self,angle,complex_domain):
        old,ctx.cap=ctx.cap,max(8,self.m+3,self.n+3)
        try:
            B,G=self.complex_phases(angle) if complex_domain else self.phases(angle)
            sb,cb=sin_cos(trim(B,self.m,self.n));sg,cg=sin_cos(trim(G,self.m,self.n))
            T=[-sb*cg,cb*cg,sg]
            F=self.complex_position(angle,T) if complex_domain else self.position(angle,T)
            m,n=self.m-1,self.n;keep=lambda v:trim(v,m,n)
            bt,gt=keep(derivative(B,'angle')),keep(derivative(G,'angle'))
            br=-trim(derivative(B,'radial'),m,n)/self.scale
            gr=-trim(derivative(G,'radial'),m,n)/self.scale
            sb,cb,sg,cg=map(keep,(sb,cb,sg,cg));T=list(map(keep,T))
            X=[-derivative(v,'radial')/self.scale for v in F];F=list(map(keep,F))
            hv=-sb*X[0]+cb*X[1];vv=-cb*X[0]-sb*X[1]
            Q=cg*X[2]-sg*hv;W=Q*Q+vv*vv
            D=(1+bt)*cg*Q-gt*vv;M=br*cg*Q-gr*vv
            H=dot(cross(T,X),F);R2=dot(F,F)
            kappa=self.lift(self.kappa,m=m,n=n)
            factors={'Fz':F[2],'W':W,'D':D,'H':H,'kappa':kappa,'R2':R2}
            z0=lambda v:v.coefficient(0,0)
            for name,value in factors.items():
                if not z0(value).real>0:raise ValueError('unresolved actual complex root branch: '+name)
            q=M*jet_function(D,'inverse')
            lk,lz,lw,lh,ld,lr=[jet_function(v,'log') for v in (kappa,F[2],W,H,D,R2)]
            logU=lk+4*lz+2*lw-4*lh;logV=lk+2*lw-2*ld
            DU=z0(along_shear(logU,q,self.scale));DV=z0(along_shear(logV,q,self.scale))
            qt=z0(derivative(q,'angle'));mu=(DU-DV/5+2*qt/5)/4
            t0=z0(jet_function(-logU/4,'exp'))
            Yprime=z0(jet_function(-logV/2,'exp'))
            Yjet=jet_function(lz-lr/2,'exp');Y=z0(Yjet)
            alpha=z0(jet_function((logU-logV)/2,'exp'))
            piY=-alpha*z0(along_shear(Yjet,q,self.scale))/(Y*Y)
            h=Y*t0;c=Yprime/h;s=t0*piY+c*mu;cg0=Yprime/t0
            values={'h':h,'c':c,'s':s,'inverse_h':1/h,'inverse_c':1/c,
                't0':t0,'inverse_t0':1/t0,'grounded_c':cg0,'grounded_s':cg0*mu,
                'inverse_grounded_c':1/cg0,'physical_height_Y':Y,'physical_Piola_Y':piY,
                'root_momentum_shear':mu,'Y_prime':Yprime,
                'source_root_factor':h/Yprime,'grounded_flux_root_factor':t0/Yprime}
            if any(not abs(v).is_finite() for v in values.values()):
                raise ValueError('nonfinite actual root frame')
            if complex_domain:
                return dict(moduli={name:ball_record(abs(v).upper()) for name,v in values.items()},
                    positive_factor_real_lower={name:ball_record(z0(v).real.lower()) for name,v in factors.items()})
            if any(not v.imag.contains(0) for v in values.values()):raise ValueError('real frame lost its real axis')
            return {name:ball_record(v.real) for name,v in values.items()}
        finally:ctx.cap=old


class GridFrame(FrameFormula,GridRootModel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # Exact jet truncation; original complete Cauchy errors stay on each coefficient.
        self.m,self.n=3,3

    def at_index(self,index):
        self.current_index=index;self.current_angle=arb.pi()*index/(2*self.grid)
        return dict(index=index,exact_quarter_fraction=str(Fraction(index,self.grid)),
            **self.frame(self.current_angle,False))


class ComplexFrame(FrameFormula,ComplexRootModel):
    def __init__(self,object_path,half_width,root_certificate,strip,*,nodes,refine_steps):
        super().__init__(object_path,half_width,root_certificate,strip,nodes=nodes)
        self.initial_root=self.root;self.root_refinement=[];self.target.fourier=NativeSeriesFFT()
        if refine_steps:
            old,ctx.cap=ctx.cap,max(8,self.m+3)
            try:
                self.root,self.root_refinement=self.target.refine_certified_root(
                    self.root,self.scale,self.budget,steps=refine_steps)
                self.coefficient,self.radius,self.E,self.C,self.K=self.target.target(self.root,self.scale,self.budget)
                self.beta,self.gamma,_,_=self.target.scalars(acb(self.root),-self.scale)
                from flint import acb_series
                self.kappa=acb_series([-self.K[j+1]/self.scale for j in range(4)],prec=4)
            finally:ctx.cap=old
        self.m,self.n=3,3


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=['grid','strip'],default='grid')
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--root-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json'))
    p.add_argument('--complex-root',type=Path,default=Path('notes/2026-11-12-actual-root-complex-potential-variation.json.gz'))
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,1000000000))
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--grid',type=int,default=4096)
    p.add_argument('--first',type=int,default=0);p.add_argument('--last',type=int)
    p.add_argument('--strip',type=Fraction,default=Fraction(1,256))
    p.add_argument('--angle-cells',type=int,default=128);p.add_argument('--vertical-cells',type=int,default=1)
    p.add_argument('--max-depth',type=int,default=10);p.add_argument('--refine-steps',type=int,default=3)
    p.add_argument('--bits',type=int,default=256);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec,ctx.cap=a.bits,10;wall,cpu=time.monotonic(),time.process_time()
    if a.mode=='grid':model=GridFrame(a.object,a.half_width,a.root_certificate,nodes=a.nodes,grid=a.grid,refine_steps=a.refine_steps)
    else:model=ComplexFrame(a.object,a.half_width,a.root_certificate,a.strip,nodes=a.nodes,refine_steps=a.refine_steps)
    identity=provenance(model.target,a.object)
    report=dict(kind='actual_root_Cauchy_frame_'+a.mode,complete=False,proved=False,
        source_sha256=sha(__file__),identity=identity,bits=a.bits,primitive_nodes=a.nodes,
        root_certificate_path=str(a.root_certificate),root_certificate_sha256=sha(a.root_certificate),
        complex_root_path=str(a.complex_root),complex_root_sha256=sha(a.complex_root),
        initial_certified_root=ball_record(model.initial_root),refined_family_root=ball_record(model.root),
        interval_Newton_trace=model.root_refinement,common_scalar_spans=model.spans,
        retained_radial_jet_precision=model.m,retained_angular_jet_precision=model.n,
        exact_parameter_half_width=str(a.half_width),primitive_full_uniform_error=ball_record(model.budget['field_errors'][0]),
        exact_Cauchy_matrix='(w,pi_w)=[[h,0],[s,-c]](U,U_xi); determinant=-Yprime',
        physical_Piola_term_retained=True,root_mean_retained=True,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in
            ('fourfold_native_series_fft.py','fourfold_phase_beta_interval.py',
             'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_parameter_germ.py',
             'fourfold_phase_root_fourier_fit.py','fourfold_phase_root_finite_grid_v2.py',
             'fourfold_phase_root_potential_complex_strip.py','fourfold_phase_canonical_root_jets.py',
             'fourfold_time_angle_jets.py')})
    def checkpoint():
        report.update(wall_seconds=time.monotonic()-wall,cpu_seconds=time.process_time()-cpu);save(a.out,report)
    if a.mode=='grid':
        last=a.grid//2+1 if a.last is None else a.last
        if not 0<=a.first<last<=a.grid:raise ValueError('invalid exact grid range')
        report.update(grid=a.grid,requested_indices=list(range(a.first,last)),rows=[]);checkpoint()
        for j in range(a.first,last):
            report['rows'].append(model.at_index(j))
            if len(report['rows'])%32==0:
                checkpoint();print(dict(completed=len(report['rows']),requested=last-a.first,wall=report['wall_seconds']),flush=True)
        report['complete']=True
    else:
        if a.angle_cells%2 or a.vertical_cells<1:raise ValueError('invalid strip partition')
        report.update(exact_physical_strip=str(a.strip),angle_cells=a.angle_cells,vertical_cells=a.vertical_cells,
            complex_primitive_full_error=ball_record(model.complex_errors[0]),cells=[],failed=[],attempts=0)
        queue=deque((Fraction(j,a.angle_cells),Fraction(j+1,a.angle_cells),a.strip*k/a.vertical_cells,
                     a.strip*(k+1)/a.vertical_cells,0) for k in range(a.vertical_cells) for j in range(a.angle_cells//2))
        while queue:
            l,r,b,t,depth=queue.popleft();report['attempts']+=1
            theta=acb((exact_arb((l+r)/4)+arb(0,exact_arb((r-l)/4)))*arb.pi(),
                exact_arb((b+t)/2)+arb(0,exact_arb((t-b)/2)))
            try:
                values=model.frame(theta,True)
                report['cells'].append(dict(exact_quarter_interval=[str(l),str(r)],
                    exact_imaginary_interval=[str(b),str(t)],depth=depth,**values))
            except (ValueError,ZeroDivisionError) as exc:
                if depth>=a.max_depth:
                    report['failed'].append(dict(interval=[str(l),str(r),str(b),str(t)],reason=str(exc)))
                    report['pending']=[[str(l),str(r),str(b),str(t),d] for l,r,b,t,d in queue];checkpoint();raise
                mid=(l+r)/2;queue.appendleft((mid,r,b,t,depth+1));queue.appendleft((l,mid,b,t,depth+1))
            if report['attempts']%16==0:
                report['pending']=[[str(l),str(r),str(b),str(t),d] for l,r,b,t,d in queue]
                checkpoint();print(dict(accepted=len(report['cells']),pending=len(queue),wall=report['wall_seconds']),flush=True)
        for k in range(a.vertical_cells):
            pair=[str(a.strip*k/a.vertical_cells),str(a.strip*(k+1)/a.vertical_cells)];cursor=Fraction(0)
            rows=sorted((r for r in report['cells'] if r['exact_imaginary_interval']==pair),key=lambda r:Fraction(r['exact_quarter_interval'][0]))
            for row in rows:
                l,r=map(Fraction,row['exact_quarter_interval'])
                if l!=cursor:raise ValueError('complex frame cover has a gap or overlap')
                cursor=r
            if cursor!=Fraction(1,2):raise ValueError('half-quarter strip incomplete')
        report.update(complete=True,proved=True,pending=[],
            full_strip_symmetry='exact even fields and Schwarz conjugation fill remaining strip',
            uniform_moduli={name:ball_record(max(stored(c['moduli'][name]).upper() for c in report['cells'])) for name in report['cells'][0]['moduli']})
    checkpoint();print(dict(complete=report['complete'],proved=report['proved'],mode=a.mode,
        wall=report['wall_seconds'],sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
