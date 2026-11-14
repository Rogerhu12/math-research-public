#!/usr/bin/env python3
"""Complete Fourier/radial polynomial of the five true core coefficients.

The parameter family and scalar germ are taken from one already paid core
leaf. The new whole radial disk times angular strip is proved explicitly.
A full rectangular time/Fourier complement is paid in A0,A1,A2. This source
does not call a small finite polynomial tail an infinite-field error.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import gzip
import shutil
import json
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_core_parameter_taylor import ParameterCoreTarget,core_provenance
from fourfold_phase_core_low_coefficients import extend_half
from fourfold_phase_core_cell_flow import ball_record
from fourfold_phase_cut_interface_fourier import geometric_tail

NAMES=('a','b','c','tau','sigma')
ODD={'b','sigma'}
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    def bad(value):raise ValueError('nonfinite input '+value)
    return json.loads(Path(path).read_text(),parse_constant=bad)
def save(path,doc):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
def shifted_errors(E):
    E0,E1,E2=E
    return {'H0':E0,'Hhalf':(E0+(E0*E1).sqrt()).upper(),
        'H1':(E0+E1).upper(),
        'Hthreehalf':((E0+E1)*(E0+2*E1+E2)).sqrt().upper(),
        'H2':(E0+2*E1+E2).upper()}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--leaf-report',type=Path,required=True)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--keep',type=int,default=768)
    ap.add_argument('--time-nodes',type=int,default=64)
    ap.add_argument('--time-terms',type=int,default=40)
    ap.add_argument('--outer-radius',type=Fraction,default=Fraction(3))
    ap.add_argument('--sample-radius',type=Fraction,default=Fraction(5,4))
    ap.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,16))
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec,ctx.cap=args.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    doc=dict(kind='complete_uniform_true_core_coefficient_polynomial',
        complete=False,source_sha256=sha(__file__),bits=args.bits,
        leaf_report=dict(path=str(args.leaf_report),sha256=sha(args.leaf_report)))
    def checkpoint():
        doc.update(CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall)
        save(args.out,doc)
    checkpoint()
    try:
        leaf=read(args.leaf_report)
        if not leaf.get('complete') or 'cover_identity' not in leaf:
            raise ValueError('the input is not a complete same-family core leaf')
        identity=leaf['cover_identity']
        if not identity.get('uniform_in_the_entire_real_parameter_interval'):
            raise ValueError('the true field polynomial requires the explicit whole family')
        for name,digest in identity['dependency_sha256'].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError('paid leaf dependency changed: '+name)
        if sha(identity['object_path'])!=identity['object_sha256']:
            raise ValueError('central exact object changed')
        R,rho,S=map(exact_arb,(args.outer_radius,args.sample_radius,args.normalized_strip))
        Nt,m,L,K=args.time_nodes,args.time_terms,args.angles,args.keep
        if not 1<rho<R or Nt%2 or not 0<m<Nt or not 0<K<L//2 or not S>0:
            raise ValueError('invalid complete rectangle parameters')
        target=ParameterCoreTarget(Path(identity['object_path']),
            Fraction(identity['exact_parameter_half_width']),identity['primitive_nodes'],L,
            arb('.003'),arb('.0025'),arb('.32'),native_order=identity['native_order'],
            native_radius=Fraction(identity['native_radius']))
        a,b=map(Fraction,identity['exact_common_span']);target.set_cell(a,b)
        left,right=map(Fraction,identity['exact_real_interval'])
        c,h=exact_arb((left+right)/2),exact_arb((right-left)/2)
        current=core_provenance(target,Path(identity['object_path']))
        for key in ('object_sha256','origin_inputs_sha256','direction_sha256',
                    'exact_parameter_interval','exact_parameter_half_width'):
            if current[key]!=identity[key]:raise ValueError('current family identity differs')
        radial=acb(c+arb(0,h*R),arb(0,h*R))
        coefficient,K0,_,errors,_=target.complete_fast_data(radial)
        M=target.coefficient_moduli_bidisk(radial,coefficient,K0,errors,S)
        doc.update(stage='whole_true_radial_angular_domain_complete',identity=identity,
            exact_real_interval=list(map(str,(left,right))),
            exact_scalar_germ=list(map(str,(a,b))),outer_time_radius=str(args.outer_radius),
            sample_time_radius=str(args.sample_radius),normalized_angular_strip=str(args.normalized_strip),
            physical_angle='theta; normalized periodic x=4theta',
            time_nodes=Nt,time_terms=m,angles=L,positive_fourier_keep=K,
            whole_true_coefficient_moduli={key:ball_record(value) for key,value in M.items()},
            actual_bidisk_geometry=target.last_geometric_domain,
            actual_bidisk_curvature=target.last_curvature_domain,
            actual_primitive_remainders=target.last_native_remainders)
        checkpoint()
        samples=np.empty((Nt,len(NAMES),K+1),object)
        for j in range(Nt//2+1):
            u=acb(rho) if j==0 else acb(-rho) if j==Nt//2 else rho*acb(0,2*arb.pi()*j/Nt).exp()
            radial=acb(c)+h*u
            coefficient,K0,_,errors,real=target.complete_fast_data(radial)
            values=target.coefficient_values(radial,coefficient,K0,errors)
            for field,name in enumerate(NAMES):
                parity=-1 if name in ODD else 1
                transformed=target.fast_fourier.fft(extend_half(values[name],parity))/L
                for k in range(K+1):
                    value=transformed[k].to_acb()
                    if name in ODD:value*=acb(0,-1)
                    if name in ODD and k==0:
                        if not value.contains(0):raise ValueError('odd Fourier zero lost exact zero')
                        value=acb(0)
                    if j in (0,Nt//2):
                        if not value.imag.contains(0):raise ValueError('real rotated Fourier coefficient lost reality')
                        value=acb(value.real)
                    samples[j,field,k]=value
                    if 0<j<Nt//2:samples[Nt-j,field,k]=value.conjugate()
            doc.update(stage='actual_true_time_circle',completed_independent_nodes=j+1,
                required_independent_nodes=Nt//2+1)
            checkpoint()
        chosen=np.empty((len(NAMES),m,K+1),float)
        radii=np.empty_like(chosen);records={}
        ratio=(rho/R)**Nt
        for field,name in enumerate(NAMES):
            selected=[arb(0),arb(0),arb(0)]
            for k in range(K+1):
                transformed=acb.dft(list(samples[:,field,k]))
                angular_alias=((-(L-k)*S).exp()+(-(L+k)*S).exp())/(1-(-L*S).exp())
                complete_alias_factor=angular_alias+((-k*S).exp()+angular_alias)*ratio/(1-ratio)
                for i in range(m):
                    value=transformed[i]/(Nt*rho**i)
                    number=float(value.real.mid())
                    alias=M[name]*R**(-i)*complete_alias_factor
                    fee=(abs(value-acb(number))+alias).upper()
                    if name in ODD and k==0:
                        number=0.;fee=arb(0)
                    upper=float(np.nextafter(float(fee),np.inf)) if fee else 0.
                    if not np.isfinite(number) or not np.isfinite(upper):
                        raise ValueError('nonfinite chosen core polynomial coefficient')
                    chosen[field,i,k]=number;radii[field,i,k]=upper
                    for order in range(3):
                        weight=(1 if k==0 and order==0 else 0 if k==0 else 2*(4*k)**order)
                        selected[order]+=weight*arb(upper)
            outside_angle=[geometric_tail(K,S,order,M[name]) for order in range(3)]
            outside_time=[]
            for order in range(3):
                angular=(arb(1) if order==0 else arb(0))
                for k in range(1,K+1):angular+=2*(4*k)**order*(-k*S).exp()
                outside_time.append((M[name]*R**(-m)/(1-1/R)*angular).upper())
            full=[(selected[j]+outside_angle[j]+outside_time[j]).upper() for j in range(3)]
            records[name]=dict(rotated_positive_coefficients_are_real=True,
                odd_angular_field=name in ODD,
                chosen_coefficient_error_A012=list(map(ball_record,selected)),
                full_angular_complement_A012=list(map(ball_record,outside_angle)),
                retained_angular_unretained_time_complement_A012=list(map(ball_record,outside_time)),
                complete_real_time_polynomial_error_A012=list(map(ball_record,full)),
                complete_real_time_multiplier_errors={k:ball_record(v) for k,v in shifted_errors(full).items()})
        del samples
        arrays=args.out.with_suffix('.npz')
        np.savez_compressed(arrays,rotated_positive_real_dyadic_coefficients=chosen,
            positive_coefficient_error_radii=radii)
        if arrays.stat().st_size>1_000_000:
            compressed=Path(str(arrays)+'.gz')
            with arrays.open('rb') as src, gzip.GzipFile(filename=str(compressed),mode='wb',mtime=0) as dst:
                shutil.copyfileobj(src,dst)
            arrays.unlink();arrays=compressed
        if arrays.stat().st_size>5_000_000:
            raise ValueError('the complete coefficient package exceeds the repository per-file limit')
        doc.update(complete=True,stage='complete_actual_true_coefficient_rectangle',
            fields=list(NAMES),field_reports=records,
            arrays=dict(path=str(arrays),sha256=sha(arrays),bytes=arrays.stat().st_size),
            exact_finite_definition='For even fields g_i,k=c_i,k and g_i,-k=c_i,k. For odd b,sigma, g_i,k=i*c_i,k, g_i,-k=-i*c_i,k and c_i,0=0. Sum u^i exp(4ik theta) over the saved complete finite rectangle.',
            scope='Actual five coefficients for the whole specified real leaf and the whole eta family. All spatial multiplier errors are complete infinite Fourier errors; no weak residual or Schur conclusion is yet claimed.')
    except Exception as exc:
        doc.update(failure=repr(exc),traceback=traceback.format_exc())
    doc['dependency_sha256']={name:sha(Path(__file__).with_name(name)) for name in (
        'fourfold_phase_core_parameter_taylor.py','fourfold_phase_core_waist_taylor.py',
        'fourfold_phase_core_radial_taylor.py','fourfold_phase_cut_interface_fourier.py',
        'fourfold_phase_beta_parameter_germ.py','fourfold_native_series_fft.py')}
    checkpoint()
    print(json.dumps({key:doc.get(key) for key in ('complete','stage','failure','CPU_seconds','wall_seconds')},
        indent=2,allow_nan=False),flush=True)
    if not doc['complete']:raise SystemExit(1)
if __name__=='__main__':main()
