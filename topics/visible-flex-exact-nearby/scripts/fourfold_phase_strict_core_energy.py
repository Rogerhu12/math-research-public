#!/usr/bin/env python3
"""Continuous strict-negative H^(1/2) Cauchy-energy inputs from true fields.

This consumes a completed nine-field coefficient rectangle, including its
complete physical-r derivative error. All real radial values and all angular
gaps are paid. It is not a global core inverse and cannot cross a turning root.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,acb_mat,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_low_feedback_paid_inputs import norm

FIELDS=('a','b','c','tau','sigma','alpha','v','gamma','kappa')
USED=('alpha','v','gamma','kappa','tau','sigma')
ODD={'b','sigma','v'}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    def bad(value):raise ValueError('nonfinite JSON '+value)
    return json.loads(Path(path).read_text(),parse_constant=bad)
def save(path,doc):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
def upper(record):
    return arb(record['ball']).upper()
def interval(left,right):
    if not left<=right:raise ValueError('reversed interval')
    return exact_arb(Fraction(left)).union(exact_arb(Fraction(right)))
def pad(value,error):
    if not error>=0:raise ValueError('negative error radius')
    return value+arb(0,error)
def range_record(values):
    return dict(lower=ball_record(min(x.lower() for x in values)),
                upper=ball_record(max(x.upper() for x in values)))
def root_positive(x,name):
    if not x>0:raise ValueError(name+' is not strictly positive')
    return x.sqrt()
def finite(value):
    if not value.is_finite():raise ValueError('nonfinite energy constant')
    return value
def phi_integral(beta,length):
    x=2*beta*length
    if x==0:return length
    if not x.contains(0):
        answer=length*x.expm1()/x
    else:
        answer=length*max(arb(0),x.upper()).exp()
    if not answer>0:raise ValueError('invalid positive Duhamel integral')
    return answer.upper()

class CompleteEnergyFields:
    def __init__(self,path):
        self.path=Path(path)
        self.doc=read(path)
        if (not self.doc.get('complete') or self.doc.get('kind')!=
                'complete_uniform_true_core_energy_coefficient_polynomial'):
            raise ValueError('a completed actual energy-field rectangle is required')
        producer=Path(__file__).with_name('fourfold_phase_core_energy_fields.py')
        if sha(producer)!=self.doc['source_sha256']:
            raise ValueError('energy-field producer changed')
        for name,digest in self.doc['dependency_sha256'].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError('field dependency changed: '+name)
        if self.doc['fields']!=list(FIELDS):
            raise ValueError('energy fields or ordering differ')
        if not self.doc['identity'].get('uniform_in_the_entire_real_parameter_interval'):
            raise ValueError('the real parameter family is missing')
        record=self.doc['arrays']
        array_path=Path(record['path'])
        if sha(array_path)!=record['sha256']:
            raise ValueError('complete field arrays changed')
        stream=(io.BytesIO(gzip.decompress(array_path.read_bytes()))
                if array_path.suffix=='.gz' else array_path)
        with np.load(stream,allow_pickle=False) as data:
            raw=np.array(data['rotated_positive_real_dyadic_coefficients'],copy=True)
        if raw.ndim!=3 or raw.shape[0]!=len(FIELDS) or np.any(~np.isfinite(raw)):
            raise ValueError('invalid complete coefficient tensor')
        self.raw={name:raw[FIELDS.index(name)] for name in USED}
        self.left,self.right=map(Fraction,self.doc['exact_real_interval'])
        self.center=(self.left+self.right)/2
        self.h=(self.right-self.left)/2
        if not self.h>0:raise ValueError('empty actual radial interval')
        self.K=raw.shape[2]-1
        self.errors={}
        for name in USED:
            row=self.doc['field_reports'][name]
            self.errors[name]=[
                list(map(upper,row['complete_real_time_polynomial_error_A012'])),
                list(map(upper,row['physical_radial_derivative_errors']['complete_A012']))]
        if np.any(self.raw['kappa'][:,1:]!=0):
            raise ValueError('curvature must retain its exact angular-constant identity')

    def evaluate(self,left,right,nodes):
        if not self.left<=left<right<=self.right:
            raise ValueError('the requested physical interval is outside the field proof')
        if nodes<=2*self.K or nodes%2:
            raise ValueError('exact finite angular evaluation requires even nodes>2K')
        u=interval((left-self.center)/self.h,(right-self.center)/self.h)
        h=exact_arb(self.h)
        gap=arb.pi()/(4*nodes)
        delta=arb(0,gap)
        coefficients={}
        values={}
        finite_moments={}
        for name in USED:
            raw=self.raw[name]
            coeff=[[],[]]
            for k in range(self.K+1):
                value,derivative=arb(0),arb(0)
                for number in raw[:,k][::-1]:
                    derivative=derivative*u+value
                    value=value*u+arb(float(number))
                coeff[0].append(value)
                coeff[1].append(derivative/h)
            coefficients[name]=coeff[0]
            field_nodes={}
            moments={}
            for dr in (0,1):
                M=[arb(0),arb(0),arb(0)]
                for k,c in enumerate(coeff[dr]):
                    size=abs(c).upper()
                    for dt in range(3):
                        weight=(1 if k==0 and dt==0 else 0 if k==0 else 2*(4*k)**dt)
                        M[dt]+=weight*size
                M=[(M[j]+self.errors[name][dr][j]).upper() for j in range(3)]
                moments[dr]=M
                for dt in (0,1):
                    data=[acb(0) for _ in range(nodes)]
                    data[0]=acb(coeff[dr][0]) if dt==0 else acb(0)
                    for k in range(1,self.K+1):
                        p=acb(0,coeff[dr][k]) if name in ODD else acb(coeff[dr][k])
                        n=-p if name in ODD else p
                        data[(-k)%nodes]=p*acb(0,4*k)**dt
                        data[k%nodes]=n*acb(0,-4*k)**dt
                    transformed=acb.dft(data)
                    result=[]
                    for z in transformed:
                        if not z.imag.contains(0):
                            raise ValueError('a real finite angular derivative lost reality')
                        result.append(pad(z.real,self.errors[name][dr][dt]))
                    field_nodes[dr,dt]=result
            # True first-order Taylor in theta plus its complete second derivative.
            value=[field_nodes[0,0][j]+delta*field_nodes[0,1][j]
                   +arb(0,gap*gap*moments[0][2]/2) for j in range(nodes)]
            theta=[field_nodes[0,1][j]+arb(0,gap*moments[0][2])
                   for j in range(nodes)]
            radial=[field_nodes[1,0][j]+delta*field_nodes[1,1][j]
                    +arb(0,gap*gap*moments[1][2]/2) for j in range(nodes)]
            values[name]=dict(value=value,theta=theta,radial=radial)
            finite_moments[name]=moments
        return values,coefficients,finite_moments

    def multiplier_and_commutator(self,name,coeff):
        mh,mth,A,B,DA=arb(0),arb(0),arb(0),arb(0),arb(0)
        for k,value in enumerate(coeff):
            t=arb(4*k)
            z=abs(value).upper()*(1 if k==0 else 2)
            root=(1+t).sqrt()
            mh+=root*z
            mth+=(1+t)*root*z
            if k:
                A+=(root-1)*z
                B+=t*root*z
                DA+=t*(root-1)*z
        E0,E1,E2=self.errors[name][0]
        eh=(E0+(E0*E1).sqrt()).upper()
        eth=((E0+E1)*(E0+2*E1+E2)).sqrt().upper()
        eA=min(E1/2,(E0*E1).sqrt()).upper()
        eB=(E1*(E1+E2)).sqrt().upper()
        eDA=min(E2/2,(E1*E2).sqrt()).upper()
        return dict(Mhalf=(mh+eh).upper(),Mthreehalf=(mth+eth).upper(),
                    Ahalf=(A+eA).upper(),Bhalf=(B+eB).upper(),
                    derivative_Ahalf=(DA+eDA).upper())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field-report',type=Path,required=True)
    ap.add_argument('--left',type=Fraction)
    ap.add_argument('--right',type=Fraction)
    ap.add_argument('--angles',type=int,default=4096)
    ap.add_argument('--lambda-constant',type=Fraction)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    wall,cpu=time.monotonic(),time.process_time()
    doc=dict(kind='actual_strict_negative_half_derivative_energy_inputs',
        complete=False,source_sha256=sha(__file__),bits=args.bits,
        input_field_report=dict(path=str(args.field_report),sha256=sha(args.field_report)),
        actual_global_inverse_certified=False)
    save(args.out,doc)
    try:
        fields=CompleteEnergyFields(args.field_report)
        left=fields.left if args.left is None else args.left
        right=fields.right if args.right is None else args.right
        value,coefficient,moments=fields.evaluate(left,right,args.angles)
        n=args.angles
        lower=lambda name:min(z.lower() for z in value[name]['value'])
        upperv=lambda name:max(z.upper() for z in value[name]['value'])
        amin,amax=lower('alpha'),upperv('alpha')
        gmin,gmax=lower('gamma'),upperv('gamma')
        kmin,kmax=lower('kappa'),upperv('kappa')
        for z,name in ((amin,'alpha'),(gmin,'gamma'),(kmin,'minus target curvature')):
            root_positive(z,name)
        if args.lambda_constant is None:
            lambdas=value['kappa']['value']
            lambda_radial=value['kappa']['radial']
            lmin,lmax=kmin,kmax
            weight=dict(kind='minus_actual_target_curvature',exact_definition='lambda=-K0(r,p)>0')
        else:
            lam=exact_arb(args.lambda_constant)
            root_positive(lam,'constant lambda')
            lambdas=[lam]*n;lambda_radial=[arb(0)]*n
            lmin=lmax=lam
            weight=dict(kind='positive_exact_constant',value=str(args.lambda_constant))
        forward=[];backward=[];potentials=[]
        for j in range(n):
            a=value['alpha']['value'][j];ar=value['alpha']['radial'][j];at=value['alpha']['theta'][j]
            g=value['gamma']['value'][j];gr=value['gamma']['radial'][j];gt=value['gamma']['theta'][j]
            v=value['v']['value'][j];vt=value['v']['theta'][j]
            d=value['tau']['value'][j]+value['sigma']['theta'][j]
            potentials.append(d)
            lam=lambdas[j];lr=lambda_radial[j]
            mat_a=(ar+v*at)/a
            mat_g=(gr+v*gt)/g
            mat_l=lr/lam
            trace=mat_l+mat_a
            difference=mat_l-mat_a+2*vt
            cross=(lam-d)*(a/lam).sqrt()
            discriminant=(abs(difference).upper()**2+4*abs(cross).upper()**2).sqrt()
            qrate=mat_g-vt
            forward.append(max(qrate.upper(),((trace.upper()+discriminant)/2).upper()))
            backward.append(max((-qrate).upper(),((-trace.lower()+discriminant)/2).upper()))
        base_forward=max(forward).upper()
        base_backward=max(backward).upper()
        norm_inputs={name:fields.multiplier_and_commutator(name,coefficient[name])
                     for name in USED}
        aa,vv,gg=norm_inputs['alpha'],norm_inputs['v'],norm_inputs['gamma']
        Ad=(norm_inputs['tau']['Ahalf']+norm_inputs['sigma']['derivative_Ahalf']).upper()
        ru=aa['Ahalf']/amin.sqrt()+vv['Ahalf']/gmin.sqrt()
        rq=aa['Bhalf']/amin.sqrt()+vv['Bhalf']/gmin.sqrt()
        rp=vv['Bhalf']/amin.sqrt()+gg['Bhalf']/gmin.sqrt()+Ad/lmin.sqrt()
        comm=(lmax*ru*ru+gmax*rq*rq+amax*rp*rp).sqrt().upper()
        beta_forward=(base_forward/2+comm).upper()
        beta_backward=(base_backward/2+comm).upper()
        L=exact_arb(right-left)
        wiring=acb_mat([[0,lmax.sqrt()*aa['Mhalf'],0],
            [0,gmax.sqrt()*aa['Mthreehalf'],0],
            [amax.sqrt(),amax.sqrt()*vv['Mthreehalf'],amax.sqrt()]])
        source_gain=norm(wiring)
        gf=(beta_forward*L).exp().upper()
        gb=(beta_backward*L).exp().upper()
        jf=phi_integral(beta_forward,L)
        jb=phi_integral(beta_backward,L)
        constants=dict(base_energy_rate_forward=base_forward,
            base_energy_rate_backward=base_backward,
            half_derivative_commutator_gain=comm,
            energy_sqrt_rate_forward=beta_forward,
            energy_sqrt_rate_backward=beta_backward,
            homogeneous_energy_sqrt_amplification_forward=gf,
            homogeneous_energy_sqrt_amplification_backward=gb,
            source_vector_energy_gain=source_gain,
            forward_Duhamel_L2_kernel_squared=jf,
            backward_Duhamel_L2_kernel_squared=jb,
            forward_L2_source_to_endpoint_energy_sqrt=source_gain*jf.sqrt(),
            backward_L2_source_to_endpoint_energy_sqrt=source_gain*jb.sqrt())
        for z in constants.values():finite(z)
        doc.update(complete=True,identity=fields.doc['identity'],
            exact_physical_interval=[str(left),str(right)],
            exact_scalar_germ=fields.doc['exact_scalar_germ'],
            energy_weight=weight,angular_closed_cells=n,
            full_real_radial_interval_paid=True,full_real_theta_circle_paid=True,
            strict_negative_target_curvature_proved=True,
            coefficient_positive_ranges=dict(alpha=[ball_record(amin),ball_record(amax)],
                gamma=[ball_record(gmin),ball_record(gmax)],
                kappa=[ball_record(kmin),ball_record(kmax)],
                lambda_weight=[ball_record(lmin),ball_record(lmax)]),
            full_potential_range=range_record(potentials),
            actual_multiplier_and_commutator_inputs={
                name:{k:ball_record(z) for k,z in row.items()} for name,row in norm_inputs.items()},
            actual_Ahalf_potential_upper=ball_record(Ad),
            constants={k:ball_record(z.upper()) for k,z in constants.items()},
            exact_PDE_state='(u,q,pbar), q=partial_theta u, pbar=physical p-fr',
            exact_source_convention='P u=f0+Dr fr+Dtheta ftheta; for the saved weak reference f0=-R0,fr=Rr,ftheta=Rtheta and pbar=p_N exactly',
            source_product_space='L2(dr; H^(1/2) f0 direct_sum H^(3/2) fr direct_sum H^(3/2) ftheta), physical Fourier weights max(1,4|k|)^s',
            exact_energy='integral lambda|Lambda_half u|^2+gamma|Lambda_half q|^2+alpha|Lambda_half pbar|^2, with angular measure normalized over one period',
            matching_energy_at_adjacent_spans='The underlying exact lambda,alpha,gamma are continuous and identical at a common real interface. Join certificates with the same energy-weight definition; no per-cell norm-equivalence multiplier is necessary.',
            scope=['Only this strict-negative interval and the same entire real parameter family.',
                   'No turning root or positive collar is included. A failed positivity test is not silently dropped.',
                   'This is a constraint-preserving full PDE energy and source bound, not a replacement for the actual finite Galerkin matrix propagation.',
                   'Global frame/canonical-label conversion, Airy connections, both exterior caps and the infinite feedback inverse remain separate.'])
    except Exception as exc:
        doc.update(failure=repr(exc),traceback=traceback.format_exc())
    doc.update(CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_core_energy_fields.py','fourfold_phase_low_feedback_paid_inputs.py',
            'fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_interval.py')})
    save(args.out,doc)
    print(json.dumps({k:doc.get(k) for k in ('complete','exact_physical_interval',
        'failure','constants','CPU_seconds','wall_seconds')},indent=2,allow_nan=False),flush=True)
    if not doc['complete']:raise SystemExit(1)
if __name__=='__main__':main()
