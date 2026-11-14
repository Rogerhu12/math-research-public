#!/usr/bin/env python3
"""All-regular physical endpoint/jump consumer with waist-amplitude output.

Explicitly new Schur complement and outer-dual schema; no execution is implied.
Reads the exact complete ac1 background and the already complete mean arrays.
The preserved body failure is not relabelled; full body residual combination
remains separate. This version computes independent endpoints and jumps.
Original v2 read an already complete body/mean
certificate, and explicit physical response/adjoint PPoly trials. Uses
noncyclic Arb Laurent products and complete exponential/physical-mode
tails, not finite-angle quadrature or a finite moving-to-physical map.
The true nonlinear regular derivative and all exterior means are kept.
A successful report pays these boundary and jump quantities; it does not
supply a complete BVP inverse or prove the actual nu Schur nonzero.
"""
from __future__ import annotations
# Explicit v2 consumes the mathematically identical body-v2 rows, whose
# parser accepts both the actual plain waist JSON and gzip certificates.
# No old native is relabelled and every original operator/mean/jump is kept.
import argparse
from bisect import bisect_left,bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import arb,acb,acb_poly,ctx

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_curvature_angle_energy_prefix import dyadic
from fourfold_codazzi_mean_completed_head_body_residual_v2 import read_trial,read
from fourfold_codazzi_completed_mean_prefix import read_completed_mean_prefix
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

KIND='actual_final_all_regular_independent_physical_boundary_and_exact_jumps_v4'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
BODY_KIND='actual_final_exact_mean_completed_response_adjoint_body_residual_v2'
BODY_SOURCE='e0a2442f8c9f63d4fe4ca733facc601e4db206a14d03a1bba80dd4816e2385b3'
MEAN_SOURCE='6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
WAIST_SHA='8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b'
WAIST_MEAN_SHA='63986d47452a34f0b52a70ebfa40aad7630eba2e0f47ec39274ac6e83f0b5b56'
BUDGET_SHA='697f74a86ecc47f8f6edf4a044f7659516e6eace1516da0774798981ef5a8091'
DUAL_KIND='actual_final_physical_all_Robin_dual_regular_complement_v2'
DUAL_COORDINATES='all physical cosine Robin amplitudes including m=4; full outer mean independent'
RIGHT=Fraction(25,8)
QNUM=Fraction(562949953420957,562949953421312)
ORDERS={'L2':Fraction(0),'H_one_sixth':Fraction(1,6),'H1':Fraction(1)}
LD={'L2':arb('0.000005898255'),'H_one_sixth':arb('0.0000111'),'H1':arb(1)/4000}


_original_record=record
def record(value):
    if not value.is_finite():
        raise ArithmeticError('a genuine physical endpoint bound is nonfinite; no numeric result certified')
    return _original_record(value)

def up(x):return arb(x).upper()
def sym(x):
    x=up(abs(x));return (-x).union(x)
def ar(x):return exact_arb(Fraction(x))
def cb_record(z):return dict(real=record(z.real),imaginary=record(z.imag))
def read_cb(row):return acb(box_from_record(row['real']),box_from_record(row['imaginary']))
def coefficient_abs(z):return up(abs(z))


class Laurent:
    """A genuine finite Laurent polynomial plus a full complex Wiener tail.

    The error is an A0 norm. It is never differentiated. Composition uses
    the complete exponential Taylor remainder. Fourier multiplication is
    an ordinary acb_poly product with all coefficients retained.
    """
    def __init__(self,coefficients=None,error=arb(0)):
        self.c={int(j):acb(v) for j,v in (coefficients or {}).items() if not acb(v)==0}
        self.error=up(error)
        if self.error<0:raise ValueError('a full angular remainder must be nonnegative')

    @classmethod
    def constant(cls,value):return cls({0:acb(value)})

    def coerce(self,value):return value if isinstance(value,Laurent) else Laurent.constant(value)
    def coefficient(self,j):return self.c.get(int(j),acb(0))
    def finite_A(self,width=Fraction(0)):
        return up(sum((abs(z)*(ar(4*abs(j)*width)).exp()
                       for j,z in self.c.items()),arb(0)))

    def A(self):
        return up(self.finite_A()+self.error)

    def analytic_finite_A(self,width):
        if not self.error==0:raise ValueError('an A0 tail was not assigned an unpaid analytic width')
        return self.finite_A(width)

    def __add__(self,value):
        value=self.coerce(value)
        c=dict(self.c)
        for j,z in value.c.items():c[j]=c.get(j,acb(0))+z
        return Laurent(c,self.error+value.error)
    __radd__=__add__
    def __neg__(self):return Laurent({j:-z for j,z in self.c.items()},self.error)
    def __sub__(self,value):return self+(-self.coerce(value))
    def __rsub__(self,value):return self.coerce(value)+(-self)

    def __mul__(self,value):
        value=self.coerce(value)
        error=up(self.finite_A()*value.error+value.finite_A()*self.error+self.error*value.error)
        if not self.c or not value.c:return Laurent({},error)
        if len(self.c)==1 and 0 in self.c:
            return Laurent({j:self.c[0]*z for j,z in value.c.items()},error)
        if len(value.c)==1 and 0 in value.c:
            return Laurent({j:value.c[0]*z for j,z in self.c.items()},error)
        l1,r1=min(self.c),max(self.c);l2,r2=min(value.c),max(value.c)
        a=acb_poly([self.coefficient(j) for j in range(l1,r1+1)])
        b=acb_poly([value.coefficient(j) for j in range(l2,r2+1)])
        product=a*b
        size=(r1-l1)+(r2-l2)+1
        return Laurent({l1+l2+i:product[i] for i in range(size)},error)
    __rmul__=__mul__

    def __truediv__(self,value):
        if isinstance(value,Laurent):raise TypeError('only an explicit scalar division is permitted')
        z=acb(value)
        if z.contains(0):raise ValueError('scalar Fourier division contains zero')
        return self*(1/z)

    def shift(self,j):return Laurent({k+j:z for k,z in self.c.items()},self.error)
    def conjugate(self):
        return Laurent({-j:z.conjugate() for j,z in self.c.items()},self.error)
    def nonmean(self):
        return Laurent({j:z for j,z in self.c.items() if j},self.error)

    def primitive(self):
        return Laurent({j:z/acb(0,4*j) for j,z in self.c.items() if j},self.error/4)

    def derivative(self):
        if not self.error==0:raise ValueError('no differentiation of an unweighted infinite remainder')
        return Laurent({j:acb(0,4*j)*z for j,z in self.c.items() if j})

    def hilbert(self):
        return Laurent({j:acb(0,1 if j>0 else -1)*z for j,z in self.c.items() if j},
                       self.error)

    def mean_complex(self):
        return self.coefficient(0)+acb(sym(self.error),sym(self.error))
    def mean_real(self):
        z=self.mean_complex()
        if not z.imag.contains(0):raise ValueError('a real complete mean lost reality')
        return z.real

    def L2(self):
        finite=sum((abs(z).upper()**2 for z in self.c.values()),arb(0))
        return up(finite.sqrt()+self.error)
    def H(self,order):
        if not self.error==0 and order:
            raise ValueError('no Sobolev norm assigned to a bare infinite A0 tail')
        finite=sum((abs(z).upper()**2*(ar(order)*arb(1+16*j*j).log()).exp()
                    for j,z in self.c.items()),arb(0))
        return up(finite.sqrt()+self.error)


def finite_pair(x,y):
    total=acb(0)
    for j,z in x.c.items():total+=z*y.coefficient(-j)
    fee=up(x.finite_A()*y.error+y.finite_A()*x.error+x.error*y.error)
    answer=total+acb(sym(fee),sym(fee))
    if not answer.imag.contains(0):raise ValueError('complete real pairing lost its imaginary zero')
    return answer.real


def exp_finite(p,tolerance,max_terms=256):
    if not p.error==0:raise ValueError('exponential input must be the actual finite phase')
    M=p.finite_A()
    term=Laurent.constant(1);answer=term
    scalar=arb(1)
    for n in range(1,max_terms+1):
        term=term*p/n;answer=answer+term
        scalar=scalar*M/n
        first=up(scalar*M/(n+1))
        ratio=up(M/(n+2))
        if ratio<1:
            fee=up(first/(1-ratio))
            if fee<tolerance:
                answer.error=up(answer.error+fee)
                return answer,dict(terms=n,phase_A0=record(M),
                     complete_exponential_A0_tail=record(fee))
    raise ValueError('the full exponential Taylor tail has not closed')


def lift_exact(values,M,scale=arb(1),background=arb(0)):
    cu={};cv={0:acb(background+scale*ar(values[M]))}
    for j in range(1,M+1):
        a=scale*ar(values[j-1])/2;b=scale*ar(values[M+j])/2
        cu[j]=acb(0,-a);cu[-j]=acb(0,a)
        cv[j]=acb(b);cv[-j]=acb(b)
    return Laurent(cu),Laurent(cv)


def exact_at(saved,nodes,r,side='right'):
    if r<nodes[0] or r>nodes[-1]:raise ValueError('actual PPoly trace is outside its domain')
    if side=='right':j=min(bisect_right(nodes,r)-1,len(nodes)-2)
    elif side=='left':j=max(0,bisect_left(nodes,r)-1)
    else:raise ValueError('a genuine one-sided trace must be specified')
    if not nodes[j]<=r<=nodes[j+1]:raise ValueError('wrong actual PPoly germ for endpoint')
    h=r-nodes[j]
    coefficients=saved['piece_coefficients'][:,j,:]
    out=[]
    for k in range(coefficients.shape[1]):
        z=Fraction(0)
        for row in range(4):z=z*h+dyadic(coefficients[row,k])
        out.append(z)
    return out,j


def exact_real_pair(x,Mx,y,My):
    if x[Mx] or y[My]:raise ValueError('this exact jump pairing expects explicit nonmean vectors')
    ans=Fraction(0)
    for j in range(1,min(Mx,My)+1):
        ans+=(x[j-1]*y[j-1]+x[Mx+j]*y[My+j])/2
    return ans


def value_table(values):return list(map(str,values))


def read_outer_dual(path,meta):
    row=read(path)
    if (row.get('kind')!=DUAL_KIND or row.get('coordinates')!=DUAL_COORDINATES
        or row.get('background_candidate_sha256')!=CANDIDATE
        or Fraction(row['background_exact_alpha'])!=Fraction(meta['exact_float_amplitude'])
        or Fraction(row['background_exact_nu'])!=Fraction(meta['exact_float_nu'])
        or row.get('physical_frequency_factor')!=4
        or row.get('no_physical_Robin_mode_omitted') is not True
        or row.get('original_fourth_retained_multiplier_is_free') is not True
        or row.get('output_functional')!='physical waist C4 amplitude'
        or Fraction(row.get('exact_amp_multiplier','0'))!=-1
        or 'omitted_physical_mode' in row):
        raise ValueError('the outer dual must include every regular physical row and have waist output')
    values=[Fraction(x) for x in row['cosine_amplitude_multipliers']]
    if not values or row.get('modes')!=len(values):
        raise ValueError('all declared physical dual modes are required')
    # Real cosine-amplitude multipliers pair with 2 lambda_j cos(4j theta).
    # The scalar output is at the waist, hence there is no right 2 cos(4theta).
    # This weight is precisely minus the complete nonmean right multiplier.
    w=[-2*x for x in values]
    return row,w


def norm_weight(w):
    return up(sum((ar(x)**2/2 for x in w),arb(0)).sqrt())


def prepare(args):
    if sha(args.candidate)!=CANDIDATE:raise ValueError('restore the complete exact final ac1 candidate')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    nodes=list(map(dyadic,saved['radial_nodes']));M=int(meta['modes'])
    if (M!=32 or nodes[0]!=0 or nodes[-1]!=RIGHT
        or saved['piece_coefficients'].shape!=(4,len(nodes)-1,65)
        or meta['exact_cap_cut']!='25/8'
        or meta['physical_frequency_factor']!=4):
        raise ValueError('complete final moving coordinates or PPoly shape changed')
    if any(Fraction(x)!=QNUM for x in meta['exact_float_q_values']):
        raise ValueError('the physical proposal q used by the published complete fee changed')
    body=read_completed_mean_prefix(args.body);mean=read(args.mean);waist=read(args.waist);budget=read(args.budget)
    waist_mean=read(args.waist_mean)
    if (body.get('candidate_sha256')!=CANDIDATE or body.get('candidate_metadata')!=meta
        or not body.get('completed_mean_prefix_provenance')):
        raise ValueError('the actual full completed mean arrays are required')
    for path in (args.candidate,args.mean,args.response,args.adjoint,args.waist_mean):
        if sha(path) not in body['inputs'].values():
            raise ValueError('body certificate and boundary input bytes differ: '+str(path))
    if (mean.get('source_sha256')!=MEAN_SOURCE or not mean.get('complete')
        or mean.get('candidate_sha256')!=CANDIDATE or mean.get('candidate_metadata')!=meta
        or mean.get('exact_interval')!=['0','25/8']):
        raise ValueError('complete actual target/mean identity is required')
    if sha(args.waist)!=WAIST_SHA or not waist['complete'] or waist['candidate_sha256']!=CANDIDATE:
        raise ValueError('the published whole-eta actual waist radius/vector identity changed')
    if (sha(args.waist_mean)!=WAIST_MEAN_SHA or not waist_mean['complete']
        or waist_mean['candidate_sha256']!=CANDIDATE):
        raise ValueError('the complete actual waist mean derivative certificate changed')
    if (sha(args.budget)!=BUDGET_SHA or not budget['complete']
        or budget['candidate_sha256']!=CANDIDATE or budget['gate_count']!=10
        or any(not row['passed'] for row in budget['gates'])):
        raise ValueError('the actual full physical transpose fee is required')
    response=read_trial(args.response,'response',meta)
    adjoint=read_trial(args.adjoint,'adjoint_nonmean',meta)
    if body['response_metadata']!=response['meta'] or body['adjoint_metadata']!=adjoint['meta']:
        raise ValueError('the body and true physical endpoint trial roles differ')
    outer,w=read_outer_dual(args.outer_dual,meta)
    amp=Fraction(body['exact_amp_multiplier'])
    if amp!=-1:
        raise ValueError('the waist output adjoint must have exact initial mean -a0')
    for trial in (response,adjoint):
        tm=trial['meta']
        if (tm.get('Schur_complement')!='full_regular_waist_amplitude_output'
            or tm.get('scalar_output')!='physical waist C4 amplitude'
            or tm.get('original_fourth_Robin_row_retained') is not True
            or tm.get('regular_complement_source_sha256')!=sha(
                Path(__file__).with_name('fourfold_codazzi_final_regular_head_model.py'))):
            raise ValueError('a b4-output trial cannot be relabelled as an all-regular trial')
    if not (args.moments>=max(response['m'],len(w),32) and Fraction(0)<args.strip<=Fraction(1,8)
            and args.tail_bits>=80):
        raise ValueError('all physical output modes and a paid analytic tail are required')
    ports=read(args.ports)
    if (ports.get('kind')!='actual_R25over8_regular_vector_and_complete_nonlinear_long_ports'
        or not ports.get('complete') or ports.get('physical_cut')!='25/8'
        or not ports.get('whole_affine_parameter_interval') or not ports.get('complete_primitive_tail')
        or not ports.get('all_Fourier_modes_and_mean_retained')
        or ports.get('object_sha256')!=meta['object_sha256']
        or ports.get('source_sha256')!=sha(Path(__file__).with_name('fourfold_codazzi_actual_regular_endpoint_ports.py'))):
        raise ValueError('the actual point R target, true regular line and all-mode long identity are required')
    for path,expected in ports['inputs'].items():
        if sha(path)!=expected:raise ValueError('actual R dependency changed: '+path)
    endpoints=body['endpoint_mean_traces']
    e0,p0=exact_at(saved,nodes,Fraction(0));eR,pR=exact_at(saved,nodes,RIGHT,'left')
    if list(map(str,e0[M:]))!=waist['exact_full_V_coefficients']:
        raise ValueError('the exact complete waist vector differs from its published certificate')
    alpha=ar(meta['exact_float_amplitude'])
    a0lo,a0hi=map(ar,waist['exact_target_waist_radius_enclosure'])
    s0=-(a0lo.union(a0hi))
    Cr=box_from_record(ports['bounds']['actual_C_reference'])
    if not Cr<0:raise ValueError('the true outer reference has lost its negative sign')
    Q0=lift_exact(e0,M,alpha,s0);QR=lift_exact(eR,M,alpha,1/Cr)
    if not Q0[1].coefficient(0).real<0 or not QR[1].coefficient(0).real<0:
        raise ValueError('the actual complete moving mean must be negative')
    c=dict(saved=saved,meta=meta,nodes=nodes,M=M,alpha=alpha,body=body,mean=mean,ports=ports,Cr=Cr,
           response=response,adjoint=adjoint,outer=outer,w=w,weight_norm=norm_weight(w),
           amp=ar(amp),amp_fraction=amp,
           bm=arb(waist_mean['derivative_interval_outward_decimal'][0]).union(
              arb(waist_mean['derivative_interval_outward_decimal'][1])),tolerance=arb(2)**(-args.tail_bits),
           strip=args.strip,moments=args.moments,Q0=Q0,QR=QR,
           exact_center_0=e0,exact_center_R=eR,
           z0=box_from_record(endpoints['response_0']),
           zR=box_from_record(endpoints['response_R']),
           mu0=box_from_record(endpoints['adjoint_0']),
           muR=box_from_record(endpoints['adjoint_R']))
    for name,t in (('response',response),('adjoint',adjoint)):
        q0,_=exact_at(t['saved'],t['nodes'],Fraction(0))
        qr,_=exact_at(t['saved'],t['nodes'],RIGHT,'left')
        c[name+'_values_0']=q0;c[name+'_values_R']=qr
        c[name+'_0']=lift_exact(q0,t['m'])
        c[name+'_R']=lift_exact(qr,t['m'])
    c['h0']=(c['response_0'][0],c['response_0'][1]+c['z0'])
    c['hR']=(c['response_R'][0],c['response_R'][1]+c['zR'])
    c['m0']=Q0[1].coefficient(0).real;c['mR']=QR[1].coefficient(0).real
    c['psi0']=Q0[1].nonmean().primitive()/c['m0']
    c['psiR']=QR[1].nonmean().primitive()/c['mR']
    c['dthetaR']=(c['response_R'][1].primitive()-c['zR']*c['psiR'])/c['mR']
    # Recheck the published analytic input inequalities on the exact final
    # endpoint over the same complete target interval, with no resampling.
    if not (abs(c['mR']).lower()>ar('29/5') and abs(c['mR']).upper()<7
        and c['psiR'].analytic_finite_A(Fraction(1,8))<arb('1.480385e-11')
        and QR[0].analytic_finite_A(Fraction(1,8))<arb('1.643190e-9')):
        raise ValueError('published actual complete outer analytic inputs are not reproduced')
    c['epsilon']=ar('11437/1250000000000000000000')+arb(2)**(-512)
    deps=('fourfold_codazzi_candidate_shards.py','fourfold_codazzi_curvature_angle_energy_prefix.py',
          'fourfold_codazzi_mean_completed_head_body_residual_v2.py','fourfold_codazzi_completed_mean_prefix.py','fourfold_codazzi_rotational_cap_jacobi.py',
          'fourfold_codazzi_actual_regular_endpoint_ports.py','fourfold_phase_beta_bulk_interval.py',
          'fourfold_phase_metric_defect.py','fourfold_codazzi_final_regular_head_model.py')
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,stage='endpoint_rows',
        inputs={str(p):sha(p) for p in (args.candidate,args.body,args.mean,args.response,args.adjoint,
                                      args.outer_dual,args.waist,args.waist_mean,args.budget,args.ports)},
        dependencies={name:sha(Path(__file__).with_name(name)) for name in deps},
        candidate_sha256=CANDIDATE,candidate_metadata=meta,
        response_metadata=response['meta'],adjoint_metadata=adjoint['meta'],outer_dual_metadata=outer,
        exact_amp_multiplier=str(amp),original_output='physical waist C4 amplitude',
        Schur_complement='fixed_nu_all_regular_rows_waist_amplitude_output',
        parameter_source_convention='D h = (+ partial_nu F) delta_nu + f',
        all_physical_regular_rows_including_m4_retained=True,
        physical_frequency_factor=4,exact_interval=['0','25/8'],whole_original_eta=True,
        original_target_primitive_tail_preserved=True,
        fixed_far_background='original allowed analytic f_B class; direction delta_f_B=0 for this nu response',
        physical_moments=args.moments,analytic_strip=str(args.strip),full_tail_bits=args.tail_bits,
        exact_center_endpoint_coefficients={'waist':value_table(e0),'R':value_table(eR)},
        endpoint_mean_traces=body['endpoint_mean_traces'],completed_mean_prefix_provenance=body['completed_mean_prefix_provenance'],physical_weight_cosine_amplitudes=value_table(w),
        complete_physical_weight_L2=record(c['weight_norm']),
        endpoint_rows={},moment_rows=[],exact_response_jump_pairings=[],exact_adjoint_jump_pairings=[],
        resume_history=[],complete_BVP_inverse_proved=False,actual_nu_Schur_nonzero_proved=False)
    return c,doc


def full_coefficient(p,j):
    return p.coefficient(j)+acb(sym(p.error),sym(p.error))


def pair_norm(pair):
    return up(sum((p.L2()**2 for p in pair),arb(0)).sqrt())


def waist_row(c):
    e,exp_info=exp_finite(c['psi0']*acb(0,4),c['tolerance'])
    e=e.shift(1);sine=(e-e.conjugate())/acb(0,2)
    gradient=8*sine.primitive()/(c['m0']**2)
    # Full amplitude is independent of the first variation component.
    amplitude=finite_pair(gradient,c['response_0'][1])+c['bm']*c['z0']
    dual=c['adjoint_0'][1]-c['amp']*gradient
    q=c['response_values_0'];p=c['adjoint_values_0']
    Mh=c['response']['m'];Mp=c['adjoint']['m']
    dirichlet_pair=sum((p[j-1]*q[j-1]/2 for j in range(1,min(Mh,Mp)+1)),Fraction(0))
    return dict(actual_radius='0',physical_amplitude_derivative=record(amplitude),
        waist_Dirichlet_primal_L2=record(c['response_0'][0].L2()),
        exact_signed_waist_Dirichlet_pairing=str(dirichlet_pair),
        complete_waist_nonmean_dual_L2=record(dual.nonmean().L2()),
        complete_waist_amplitude_nonmean_gradient_L2=record(gradient.L2()),
        complete_amplitude_gradient_A0_tail=record(gradient.error),
        exact_physical_amplitude_mean_column=record(c['bm']),
        complete_waist_dual_mean_exactly_zero=True,
        complete_waist_odd_Dirichlet_dual_exactly_zero=True,
        actual_nonmean_physical_projection=True,
        exponential=exp_info,whole_real_angular_circle=True,
        finite_polynomial_support=max((abs(j) for j in gradient.c),default=0),
        unknown_all_physical_modes_paid=True)


def outer_dual_row(c):
    u,v=c['QR'];m=c['mR']
    B=Laurent();t=Laurent();infos=[]
    for j,w in enumerate(c['w'],1):
        if not w:continue
        k=4*j
        e,info=exp_finite(c['psiR']*acb(0,k),c['tolerance'])
        e=e.shift(j)
        sine=(e-e.conjugate())/acb(0,2);cosine=(e+e.conjugate())/2
        ww=ar(w);B=B+ww*sine
        t=t+ww*k*(u*cosine-ar(QNUM)*sine)
        infos.append(dict(physical_mode=k,**info))
    gradient=(B/m,-t.primitive()/(m*m))
    difference=(gradient[0]-c['adjoint_R'][0],
                gradient[1]-c['adjoint_R'][1])
    model=pair_norm(tuple(p.nonmean() for p in difference))
    fee=up(arb('0.000000177')*c['weight_norm']+
           arb('0.000001106')*abs(c['muR']))
    mean_multiplier=up(50*abs(c['muR'])+arb('0.0000000028')*c['weight_norm'])
    return dict(actual_radius='25/8',model_complete_nonmean_dual_L2=record(model),
        complete_true_regular_and_nonlinear_DN_fee=record(fee),
        true_complete_nonmean_dual_L2=record(up(model+fee)),
        true_physical_mean_adjoint_multiplier_abs_upper=record(mean_multiplier),
        physical_mean_adjoint_definition='(mean_column_of_combined_true_Robin_weight-mu_R)/omega_R',
        original_physical_mean_dual_exactly_zero=True,
        inverse_omega_upper='50',unknown_full_DN_transpose_not_truncated=True,
        exact_physical_weight_L2=record(c['weight_norm']),
        all_regular_outer_rows_output_is_at_waist=True,
        finite_physical_modes_in_weight=len(c['w']),
        finite_composition_support=max((abs(j) for p in gradient for j in p.c),default=0),
        complete_gradient_A0_tails=[record(p.error) for p in gradient],
        whole_real_angular_circle=True,exponentials=infos)


def moment_row(c,j):
    k=4*j;m=c['mR'];z=c['zR'];u,v=c['QR']
    E,info=exp_finite(c['psiR']*acb(0,-k),c['tolerance'])
    C=full_coefficient(E-1,j)/m
    B=full_coefficient(E*u,j)/m
    if not C.imag.contains(0) or not B.real.contains(0):
        raise ValueError('the actual full background moments lost reflection')
    C=acb(C.real,0);B=acb(0,B.imag)
    dC=-z*C/m+acb(0,-k)*full_coefficient(E*c['dthetaR'],j)/m
    dB=-z*B/m+full_coefficient(E*(c['hR'][0]-acb(0,k)*u*c['dthetaR']),j)/m
    if not dC.imag.contains(0) or not dB.real.contains(0):
        raise ValueError('the full physical response moment lost actual reflection symmetry')
    # True even/odd symmetry, not truncation, gives these exact zeros.
    dC=acb(dC.real,0);dB=acb(0,dB.imag)
    robin=acb(0,1)*dB+ar(QNUM)*dC
    if not robin.imag.contains(0):raise ValueError('the actual model Robin row must be real even')
    return dict(positive_physical_index=j,physical_mode=k,
        actual_background_physical_C=cb_record(C),actual_background_physical_B=cb_record(B),
        full_physical_delta_C=cb_record(dC),full_physical_delta_B=cb_record(dB),
        full_proposal_Robin=cb_record(acb(robin.real,0)),
        physical_regular_row_retained_in_primal_norm=True,
        complete_exponential=info,
        finite_moving_data_used_without_physical_Fourier_truncation=True)


def analytic_physical_tails(c):
    m_inv=up(1/abs(c['mR']).lower());z=up(abs(c['zR']))
    P=c['psiR'].analytic_finite_A(c['strip'])
    U=c['QR'][0].analytic_finite_A(c['strip'])
    H=c['hR'][0].analytic_finite_A(c['strip'])
    T=c['dthetaR'].analytic_finite_A(c['strip'])
    decay=ar(c['strip'])-P
    if not decay>0:raise ValueError('the true complete physical analytic strip collapsed')
    x=(-4*decay).exp();n=c['moments']+1
    if not x<1:raise ValueError('the entire physical Fourier tail does not decay')
    t=x**n
    G0=t/(1-x)
    G1=t*(n/(1-x)+x/(1-x)**2)
    G2=t*(n*n/(1-x)+2*n*x/(1-x)**2+x*(1+x)/(1-x)**3)
    C1=up(z*m_inv*m_inv*P+m_inv*T)
    B0=up(z*m_inv*m_inv*U+m_inv*H)
    B1=up(m_inv*U*T)
    R0=B0;R1=up(B1+ar(QNUM)*C1)
    ctail=up(8*C1*G1)
    rtail=up(2*(R0*G0+4*R1*G1))
    ctail1=up(8*C1*(G1+4*G2))
    rtail1=up(2*(R0*G0+4*(R0+R1)*G1+16*R1*G2))
    return dict(physical_positive_indices_above=c['moments'],
       true_sigma=record(ar(c['strip'])),phase_A_sigma=record(P),
       complete_dtheta_A_sigma=record(T),complete_h1_A_sigma=record(H),
       positive_physical_decay_width=record(decay),
       complete_background_C_A0_tail=record(up(8*m_inv*P*G1)),
       complete_background_B_A0_tail=record(up(2*m_inv*U*G0)),
       geometric_zeroth=record(up(G0)),geometric_first=record(up(G1)),geometric_second=record(up(G2)),
       full_both_signs_C_A0=record(ctail),full_both_signs_Robin_A0=record(rtail),
       full_both_signs_C_H1_majorant_A1=record(ctail1),
       full_both_signs_Robin_H1_majorant_A1=record(rtail1),
       all_nonretained_modes_paid=True)


def exact_response_jump_row(c,i):
    tr=c['response'];du=c['adjoint'];r=tr['nodes'][i]
    left,jl=exact_at(tr['saved'],tr['nodes'],r,'left')
    right,jr=exact_at(tr['saved'],tr['nodes'],r,'right')
    jump=[a-b for a,b in zip(right,left)]
    dual,jd=exact_at(du['saved'],du['nodes'],r,'right')
    pair=exact_real_pair(dual,du['m'],jump,tr['m'])
    return dict(trial_join=i,radius=str(r),response_left_piece=jl,response_right_piece=jr,
        actual_adjoint_right_piece=jd,signed_complete_pairing=str(pair),
        convention='mean_phi(lambda_nonmean(r+), response(r+)-response(r-)); exact rationals',
        full_reconstructed_mean_jump='0',all_finite_trial_modes_preserved=True)


def exact_adjoint_jump_row(c,i):
    tr=c['adjoint'];re=c['response'];r=tr['nodes'][i]
    left,jl=exact_at(tr['saved'],tr['nodes'],r,'left')
    right,jr=exact_at(tr['saved'],tr['nodes'],r,'right')
    jump=[a-b for a,b in zip(right,left)]
    response,jh=exact_at(re['saved'],re['nodes'],r,'left')
    pair=exact_real_pair(jump,tr['m'],response,re['m'])
    return dict(trial_join=i,radius=str(r),adjoint_left_piece=jl,adjoint_right_piece=jr,
        actual_response_left_piece=jh,signed_complete_pairing=str(pair),
        convention='mean_phi(adjoint(r+)-adjoint(r-), response_nonmean(r-)); exact rationals',
        full_reconstructed_mean_jump='0',all_finite_trial_modes_preserved=True)


def summarize(c,doc):
    if len(doc['moment_rows'])!=c['moments'] or set(doc['endpoint_rows'])!={'waist','outer_dual'}:
        raise ValueError('all full physical boundary rows are required')
    for name in ('response','adjoint'):
        if len(doc['exact_'+name+'_jump_pairings'])!=len(c[name]['nodes'])-2:
            raise ValueError('every actual radial trial interface is required')
    tails=analytic_physical_tails(c)
    background_Z=box_from_record(tails['complete_background_C_A0_tail'])
    background_B=box_from_record(tails['complete_background_B_A0_tail'])
    for row in doc['moment_rows']:
        background_Z+=2*abs(read_cb(row['actual_background_physical_C']))
        background_B+=2*abs(read_cb(row['actual_background_physical_B']))
    background_Z=up(background_Z);background_B=up(background_B)
    if not background_Z<arb('1e-12'):
        raise ValueError('actual all-mode background Z did not enter the true nonlinear derivative ball')
    summary={};Cnorms={}
    for name,order in ORDERS.items():
        C2=arb(0);R2=arb(0)
        for row in doc['moment_rows']:
            k=row['physical_mode']
            weight=(ar(order)*arb(1+k*k).log()).exp()
            C=read_cb(row['full_physical_delta_C']);R=read_cb(row['full_proposal_Robin'])
            C2+=2*weight*abs(C)**2
            R2+=2*weight*abs(R)**2
        tailkey='A0' if not order else 'H1_majorant_A1'
        ctail=box_from_record(tails['full_both_signs_C_'+tailkey])
        rtail=box_from_record(tails['full_both_signs_Robin_'+tailkey])
        moment_C=up(C2.sqrt()+ctail)
        complete_H2=c['hR'][1].H(order)
        Z=up(min(moment_C,up(arb('0.03')*complete_H2)))
        model=up(R2.sqrt()+rtail)
        fee=up((LD[name]+c['epsilon'])*Z)
        summary[name]=dict(full_physical_delta_Z_upper=record(Z),
            complete_delta_Z_moment_upper=record(moment_C),
            complete_delta_Z_independent_trace_upper=record(up(arb('0.03')*complete_H2)),
            complete_all_regular_Robin_model_upper=record(model),
            full_true_regular_and_nonlinear_DN_fee=record(fee),
            true_complete_all_regular_Robin_upper=record(up(model+fee)))
        Cnorms[name]=Z
    outer=arb(0)
    for j,w in enumerate(c['w'],1):
        outer+=ar(w)*read_cb(doc['moment_rows'][j-1]['full_proposal_Robin']).real
    waist=doc['endpoint_rows']['waist']
    waist_pair=Fraction(waist['exact_signed_waist_Dirichlet_pairing'])
    amplitude=box_from_record(waist['physical_amplitude_derivative'])
    # Full body pairing is deliberately not supplied by the mean prefix.
    body_pair=None
    jump=sum((Fraction(row['signed_complete_pairing']) for row in doc['exact_response_jump_pairings']),Fraction(0))
    dualjump=sum((Fraction(row['signed_complete_pairing']) for row in doc['exact_adjoint_jump_pairings']),Fraction(0))
    # S0 = ell[q] - Y(Areg q - Fnu); outer = -lambda_R,nonmean BR q.
    # The true outer mean response row is exactly satisfied after scalar completion.
    corrected=amplitude+outer-ar(waist_pair)-ar(jump)
    yR=c['response_R'][1].L2()
    corrected_fee=up(arb('0.000000177')*c['weight_norm']*yR)
    actual=corrected+sym(corrected_fee)
    original_b4=2*read_cb(doc['moment_rows'][0]['full_proposal_Robin']).real
    b4fee=up(arb(2).sqrt()*(LD['L2']+c['epsilon'])*Cnorms['L2'])
    doc.update(complete=True,stage='complete_independent_boundary_and_jump_quantities',
        complete_physical_endpoint_tail=tails,
        actual_background_complete_physical_Z_A0=record(background_Z),
        actual_background_complete_physical_B_A0=record(background_B),
        actual_background_C_mean_delta=record(1/c['mR']-c['Cr']),
        complete_actual_Z_in_true_DN_derivative_ball=True,
        true_physical_all_regular_primal_boundary_norms=summary,
        true_physical_mean_primal_residual_exactly_zero=True,
        true_physical_B_mean_preserved_by_reflection=True,
        all_regular_outer_modes_including_original_m4_paid=True,
        physical_waist_output_not_replaced_by_outer_b4=True,
        actual_background_fB_preserved_and_direction_zero_only=True,
        retained_proposal_b4_residual=record(original_b4),
        true_retained_b4_residual_enclosure=record(original_b4+sym(b4fee)),
        true_retained_b4_complete_DN_fee=record(b4fee),
        signed_terms=dict(negative_full_regular_outer_model_pairing=record(outer),
            exact_waist_Dirichlet_pairing=str(waist_pair),
            true_waist_amplitude_derivative=record(amplitude),
            full_body_dual_response_residual_integral=None,
            exact_response_jump_right_trace_pairing=str(jump),
            exact_adjoint_jump_response_left_trace_pairing=str(dualjump)),
        endpoint_and_jump_scalar_only=dict(model=record(corrected),complete_true_outer_model_fee=record(corrected_fee),
            true_endpoint_and_jump_scalar_enclosure=record(actual),
            missing_term='subtract the complete signed body dual-response residual integral',
            not_the_corrected_S0_or_true_Schur=True),
        full_primal_body_residual=None,full_dual_body_residual=None,
        complete_response_jump_norms=None,complete_adjoint_jump_norms=None,
        full_body_combination_pending=True,
        complete_all_endpoints_and_trial_interfaces=True,
        whole_body_inverse_not_replaced_by_boundary_smallness=True,
        complete_BVP_inverse_proved=False,actual_nu_Schur_nonzero_proved=False)


def validate_resume(c,doc,old):
    for key in ('kind','source_sha256','inputs','dependencies','candidate_sha256','candidate_metadata',
                'response_metadata','adjoint_metadata','outer_dual_metadata','exact_amp_multiplier',
                'physical_moments','analytic_strip','full_tail_bits','physical_weight_cosine_amplitudes'):
        if old[key]!=doc[key]:raise ValueError('actual complete boundary resume identity changed: '+key)
    if old.get('complete') or old.get('failure') is not None:
        raise ValueError('only an explicit successful row prefix may resume')
    if any(k not in ('waist','outer_dual') for k in old['endpoint_rows']):
        raise ValueError('unknown saved endpoint stage')
    for j,row in enumerate(old['moment_rows'],1):
        if row['positive_physical_index']!=j or row['physical_mode']!=4*j or j>c['moments']:
            raise ValueError('saved whole physical moments are not the original complete prefix')
    if old['moment_rows'] and set(old['endpoint_rows'])!={'waist','outer_dual'}:
        raise ValueError('physical moments cannot precede both complete endpoint rows')
    for name in ('response','adjoint'):
        key='exact_'+name+'_jump_pairings'
        for i,row in enumerate(old[key],1):
            if i>=len(c[name]['nodes'])-1 or row['trial_join']!=i or row['radius']!=str(c[name]['nodes'][i]):
                raise ValueError('an actual saved exact jump changed')
        if old[key] and len(old['moment_rows'])!=c['moments']:
            raise ValueError('the saved stage order lost complete physical moments')
    for key in ('endpoint_rows','moment_rows','exact_response_jump_pairings',
                'exact_adjoint_jump_pairings','stage'):
        doc[key]=old[key]


def advance_one(c,doc):
    if 'waist' not in doc['endpoint_rows']:
        doc['stage']='whole_waist_endpoint'
        doc['endpoint_rows']['waist']=waist_row(c);return True
    if 'outer_dual' not in doc['endpoint_rows']:
        doc['stage']='complete_true_outer_adjoint'
        doc['endpoint_rows']['outer_dual']=outer_dual_row(c);return True
    if len(doc['moment_rows'])<c['moments']:
        doc['stage']='complete_physical_response_moments'
        doc['moment_rows'].append(moment_row(c,len(doc['moment_rows'])+1));return True
    for name,fn in (('response',exact_response_jump_row),('adjoint',exact_adjoint_jump_row)):
        key='exact_'+name+'_jump_pairings'
        if len(doc[key])<len(c[name]['nodes'])-2:
            doc['stage']=name+'_exact_interface_pairings'
            doc[key].append(fn(c,len(doc[key])+1));return True
    summarize(c,doc);return False


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','body','mean','response','adjoint','outer-dual'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--waist',type=Path,default=Path('notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json'))
    ap.add_argument('--waist-mean',type=Path,default=Path('notes/2026-11-14-R133-final-waist-mean-adjoint-column-rational.json'))
    ap.add_argument('--budget',type=Path,default=Path('notes/2026-11-14-R133-complete-physical-boundary-transpose-rational.json'))
    ap.add_argument('--ports',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-long-ports-native.json.gz'))
    ap.add_argument('--moments',type=int,default=256)
    ap.add_argument('--strip',type=Fraction,default=Fraction(1,8))
    ap.add_argument('--tail-bits',type=int,default=180)
    ap.add_argument('--resume',type=Path);ap.add_argument('--max-new-rows',type=int,default=64)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;ctx.cap=6;start=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve all previous complete, partial and failed results')
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None)
    try:
        c,doc=prepare(args)
        if args.resume:
            old=read(args.resume);validate_resume(c,doc,old)
            doc['resume_history']=old['resume_history']+[dict(path=str(args.resume),sha256=sha(args.resume),
                original_complete=False,missing_exit_not_inferred=True)]
        if args.max_new_rows<1:raise ValueError('positive explicit new row budget required')
        n=0;checkpoint=time.monotonic()
        while n<args.max_new_rows:
            if not advance_one(c,doc):break
            n+=1
            if time.monotonic()-checkpoint>15:
                doc['wall_seconds']=time.monotonic()-start;save(args.out,doc)
                print(dict(stage=doc['stage'],new_rows=n,physical_rows=len(doc['moment_rows'])),flush=True)
                checkpoint=time.monotonic()
        doc['explicit_complete_stage_row_prefix_only']=not doc['complete']
    except Exception as exc:
        doc['complete']=False;doc['failure']=dict(type=type(exc).__name__,message=str(exc))
        raise
    finally:
        doc['wall_seconds']=time.monotonic()-start;save(args.out,doc)
    print(dict(complete=doc['complete'],stage=doc.get('stage'),out=str(args.out)),flush=True)


if __name__=='__main__':
    main()
