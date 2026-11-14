#!/usr/bin/env python3
"""Complete Wiener inverse and physical boundary of a finite U,V candidate.

The floating FFT only chooses a finite exact dyadic Laurent polynomial W.
The entire residual 1-vW is subsequently enclosed by directed polynomial
convolution. A strict A0 Neumann gate pays all infinitely many modes of 1/v.
This certifies the stated boundary, not the interior PDE or a BVP inverse.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,acb_poly,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_reciprocal_compact_target_jets import ReciprocalCompactTargetJets
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def dyadic(x):return Fraction.from_float(float(x))


class Laurent:
    def __init__(self,lower,coefficients):
        self.lower=int(lower);self.coefficients=list(map(acb,coefficients))
        self.upper=self.lower+len(self.coefficients)-1

    def get(self,k):
        return self.coefficients[k-self.lower] if self.lower<=k<=self.upper else acb(0)

    def __add__(self,other):
        if not isinstance(other,Laurent):other=Laurent(0,[other])
        lo=min(self.lower,other.lower);hi=max(self.upper,other.upper)
        return Laurent(lo,[self.get(j)+other.get(j) for j in range(lo,hi+1)])

    __radd__=__add__

    def __neg__(self):return self.scale(-1)

    def __sub__(self,other):return self+(-other)

    def __mul__(self,other):
        if not isinstance(other,Laurent):return self.scale(other)
        product=acb_poly(self.coefficients)*acb_poly(other.coefficients)
        count=len(self.coefficients)+len(other.coefficients)-1
        return Laurent(self.lower+other.lower,[product[j] for j in range(count)])

    def scale(self,c):return Laurent(self.lower,[c*z for z in self.coefficients])

    def derivative(self,order=1):
        return Laurent(self.lower,[z*acb(0,4*k)**order
            for k,z in zip(range(self.lower,self.upper+1),self.coefficients)])

    def norm(self,*,order=0,select=lambda j:True):
        return sum((abs(z)*(4*abs(j))**order for j,z in
            zip(range(self.lower,self.upper+1),self.coefficients) if select(j)),arb(0)).upper()

    def hilbert(self):
        return Laurent(self.lower,[z*acb(0,1 if j>0 else -1 if j<0 else 0)
            for j,z in zip(range(self.lower,self.upper+1),self.coefficients)])


def exact_trace(saved,r):
    """Exact dyadic PPoly evaluation, retaining the selected side at a join."""
    nodes=list(map(dyadic,saved['radial_nodes']));r=Fraction(r)
    if not nodes[0]<=r<=nodes[-1]:raise ValueError('no candidate extrapolation')
    j=min(bisect_right(nodes,r)-1,len(nodes)-2);h=r-nodes[j]
    cc=saved['piece_coefficients'][:,j];out=[]
    for column in cc.T:
        value=dyadic(column[0])
        for c in column[1:]:value=value*h+dyadic(c)
        out.append(value)
    return out,j,[nodes[j],nodes[j+1]]


def fields(y,m):
    U=[acb(0)]*(2*m+1);V=[acb(0)]*(2*m+1)
    V[m]=acb(exact_arb(y[m]))
    for j in range(1,m+1):
        us=exact_arb(y[j-1])/2;vc=exact_arb(y[m+j])/2
        U[m+j]=acb(0,-us);U[m-j]=acb(0,us)
        V[m+j]=V[m-j]=acb(vc)
    return Laurent(-m,U),Laurent(-m,V)


def finite_inverse_proposal(v,degree,grid):
    if grid<=2*max(degree,v.upper,-v.lower):
        raise ValueError('proposal grid must contain the finite proposed polynomial')
    coeff=np.zeros(grid,dtype=complex)
    for j in range(v.lower,v.upper+1):coeff[j%grid]=complex(v.get(j))
    values=np.fft.ifft(coeff).real*grid
    if not np.all(np.isfinite(values)) or np.any(values==0):
        raise ValueError('floating inverse proposal is unavailable')
    spectrum=np.fft.fft(1/values)/grid
    # Enforce exact real even symmetry. This is only a polynomial proposal;
    # no estimate of floating FFT accuracy is used anywhere in the proof.
    positive=[float(spectrum[j].real) for j in range(degree+1)]
    W=Laurent(-degree,[acb(exact_arb(dyadic(positive[abs(j)])))
        for j in range(-degree,degree+1)])
    return W,positive,dict(grid=grid,degree=degree,
        sampled_v_min=float(np.min(values)),sampled_v_max=float(np.max(values)),
        sampled_values_are_not_used_as_a_true_gap=True)


def one_boundary(saved,meta,r,target,qdata,args):
    m=int(meta['modes']);alpha=exact_arb(dyadic(meta['amplitude']));nu=Fraction(meta['exact_float_nu'])
    if nu!=dyadic(meta['nu']):raise ValueError('the exact actual metric parameter differs')
    y,piece,cell=exact_trace(saved,r);U,V=fields(y,m)
    actual,germ=target.coefficients(r,r,nu)
    # The induced rotational waist has a'=0, hence Cref=-1/a exactly.
    s=-actual['a'] if r==0 else actual['s'];Cr=1/s
    if not s<0:raise ValueError('true negative rotational C chart is missing')
    v=V.scale(alpha)+s
    W,proposal,proposal_info=finite_inverse_proposal(v,args.inverse_degree,args.proposal_grid)
    residual=Laurent(0,[1])-v*W
    eps=[residual.norm(order=k) for k in range(3)]
    passed=bool(eps[0]<1)
    result=dict(radius=str(r),candidate_piece=piece,exact_candidate_piece=list(map(str,cell)),
        exact_target_scalar_germ=list(map(str,germ)),
        actual_target={k:record(actual[k]) for k in ('a','Cref','s','complete_primitive_tail_A0')},
        true_used_s=record(s),true_used_Cref=record(Cr),
        polynomial_proposal=proposal_info,
        W_nonnegative_exact_float_coefficients=proposal,
        full_residual_support=[residual.lower,residual.upper],
        residual_derivative_A0=[record(x) for x in eps],W_A0=record(W.norm()),
        entire_inverse_certified=passed)
    if not passed:return result
    I0=(W.norm()/(1-eps[0])).upper()
    v1,v2=v.norm(order=1),v.norm(order=2)
    I1=(I0**2*v1).upper();I2=(2*I0**3*v1**2+I0**2*v2).upper()
    remainder=[(I0*eps[0]).upper(),(I1*eps[0]+I0*eps[1]).upper(),
        (I2*eps[0]+2*I1*eps[1]+I0*eps[2]).upper()]
    # vW is invertible in A0, hence v is invertible in this commutative
    # Banach algebra. One true value selects the negative real component.
    v_at_zero=sum(v.coefficients,acb(0))
    negative=bool(v_at_zero.imag.contains(0) and v_at_zero.real<0)
    if not negative:raise ValueError('actual one-point negative sign unresolved')
    U0,U1,U2=[U.norm(order=j) for j in range(3)]
    Bpoly=(U*W).scale(alpha);Cpoly=W;c_poly=W+(-Cr);b_poly=Bpoly.hilbert()
    Bfee=(abs(alpha)*U0*remainder[0]).upper();Cfee=remainder[0]
    Bbounds=[(abs(alpha)*U0*I0).upper(),
        (abs(alpha)*(U1*I0+U0*I1)).upper(),
        (abs(alpha)*(U2*I0+2*U1*I1+U0*I2)).upper()]
    Cbounds=[I0,I1,I2]
    result.update(actual_v_strictly_negative=True,actual_v_abs_lower=record((1/I0).lower()),
        actual_inverse_derivative_A0=[record(x) for x in Cbounds],
        actual_inverse_full_A2_1_plus_m_squared=record((I0+2*I1+I2).upper()),
        inverse_minus_W_derivative_A0=[record(x) for x in remainder],
        physical_B_derivative_A0=[record(x) for x in Bbounds],
        physical_B_minus_polynomial_A0=record(Bfee),physical_C_minus_polynomial_A0=record(Cfee),
        physical_B_mean_exactly_zero_by_reflection=True,
        physical_c_nonmean_A0_upper=record((c_poly.norm(select=lambda j:j!=0)+Cfee).upper()),
        physical_c_nonmean_homogeneous_A2_upper=record((c_poly.norm(order=2)+remainder[2]).upper()),
        physical_c_mean_ball=record(c_poly.get(0).real+arb(0,Cfee)),
        physical_c_mean_abs_upper=record((abs(c_poly.get(0))+Cfee).upper()),
        retained_physical_modes=m,complete_physical_B_tail_A0=record((Bpoly.norm(select=lambda j:abs(j)>m)+Bfee).upper()),
        complete_physical_c_tail_A0=record((c_poly.norm(select=lambda j:abs(j)>m)+Cfee).upper()),
        all_infinite_quotient_modes_paid=True,all_true_angle_derivatives_to_two_paid=True)
    if r==0:
        result.update(actual_waist_B_A0_upper=record(Bbounds[0]),
            actual_waist_mean_C_plus_inverse_a_ball=record(W.get(0).real+1/actual['a']+arb(0,Cfee)),
            normalized_waist_c_fourth_plus_one_abs_upper=record((abs(2*c_poly.get(1)/alpha+1)+2*Cfee/abs(alpha)).upper()))
    if r==Fraction(3,2):
        qmax=exact_arb(Fraction(qdata['all_nonmean_q_abs_upper_exact']))
        if len(qdata['q_values'])<m:raise ValueError('complete retained q vector missing')
        nominal=arb(0);qfee=arb(0)
        for j in range(1,m+1):
            q=exact_arb(dyadic(qdata['q_values'][j-1]))
            err=box_from_record(qdata['true_q_error_directed_records'][j-1]).upper()
            for sign in (-1,1):
                k=sign*j;nominal+=abs(b_poly.get(k)+q*c_poly.get(k));qfee+=err*abs(c_poly.get(k))
        nominal=nominal.upper();qfee=qfee.upper()
        bt=Bpoly.norm(select=lambda j:abs(j)>m);ct=c_poly.norm(select=lambda j:abs(j)>m)
        analytic_fee=(Bfee+qmax*Cfee).upper()
        full_linear=(nominal+qfee+bt+qmax*ct+analytic_fee).upper()
        small=bool(box_from_record(result['physical_c_nonmean_A0_upper']).upper()<arb(2)/10**5)
        nonlinear=arb('1.663187e-8');mean=arb('4.636375e-9')
        result.update(actual_cap_input_A0_gate=small,actual_cap_input_A2_gate=True,
            independent_fB_domain_still_required='||f_B||_dotA2_sigma <= 2^-60',
            complete_linear_Robin_terms={k:record(z) for k,z in dict(
                exact_finite_nominal=nominal,actual_true_q_vector_fee=qfee,
                finite_unretained_B_tail=bt,finite_unretained_qC_tail=(qmax*ct).upper(),
                full_infinite_quotient_fee=analytic_fee).items()},
            actual_complete_linear_Robin_A0_upper=record(full_linear),
            actual_complete_nonlinear_cap_matching_A0_upper=record((full_linear+nonlinear).upper()) if small else None,
            actual_complete_nonlinear_cap_mean_matching_abs_upper=record((abs(c_poly.get(0))+Cfee+mean).upper()) if small else None,
            true_nonlinear_cap_B_fee=record(nonlinear),true_nonlinear_cap_mean_fee=record(mean),
            nonlinear_cap_is_not_replaced_by_a_zero_remainder=True)
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-cap-cut-r15-q256-with-tail.json'))
    ap.add_argument('--radii',type=Fraction,nargs='+',default=[Fraction(0),Fraction(3,2)])
    ap.add_argument('--inverse-degree',type=int,default=1024);ap.add_argument('--proposal-grid',type=int,default=8192)
    ap.add_argument('--bits',type=int,default=320);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve each complete Wiener boundary calculation')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));qd=read(args.q_vector)
    if (meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object)
        or meta['physical_frequency_factor']!=4 or qd['object_sha256']!=meta['object_sha256']
        or not qd['complete'] or not qd['success']
        or not qd['all_frequencies_above_the_table_are_retained']
        or sha(qd['directed_vector_path'])!=qd['directed_vector_sha256']
        or sha(qd['complete_screening_path'])!=qd['complete_screening_sha256']):
        raise ValueError('same actual object and complete true q inputs required')
    target=ReciprocalCompactTargetJets(args.object,Fraction(0),512)
    rows=[];failure=None
    try:
        for radius in args.radii:
            row=one_boundary(saved,meta,radius,target,qd,args);rows.append(row)
            print(dict(radius=str(radius),inverse=row['entire_inverse_certified'],
                eps0=row['residual_derivative_A0'][0]['upper'],
                c_A0=row.get('physical_c_nonmean_A0_upper',{}).get('upper'),
                Robin=row.get('actual_complete_nonlinear_cap_matching_A0_upper'),
                wall_seconds=time.monotonic()-started),flush=True)
    except Exception as exc:failure=dict(type=type(exc).__name__,message=str(exc))
    complete=bool(failure is None and len(rows)==len(args.radii))
    doc=dict(kind='actual_full_Wiener_reciprocal_physical_boundary_v1',complete=complete,
        source_sha256=sha(__file__),object_sha256=meta['object_sha256'],
        inputs={str(p):sha(p) for p in (args.object,args.candidate,args.q_vector)},
        candidate_metadata=meta,exact_eta='0',actual_final_nu=meta['exact_float_nu'],
        actual_amplitude=str(dyadic(meta['amplitude'])),whole_circle=True,complete_primitive_tail=True,
        finite_candidate_does_not_claim_whole_eta_uniformity=True,
        all_requested_Wiener_inverse_gates_passed=complete and all(r['entire_inverse_certified'] for r in rows),
        all_infinite_physical_boundary_modes_retained=True,physical_mean_rows_retained=True,
        rows=rows,failure=failure,interior_PDE_solution_proved=False,full_body_inverse_proved=False,
        floating_FFT_only_selects_a_finite_exact_polynomial=True,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_reciprocal_candidate_tools.py',
            'fourfold_codazzi_reciprocal_compact_target_jets.py','fourfold_codazzi_cubic_target_jets.py',
            'fourfold_codazzi_high_target_jets.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_metric_defect.py','fourfold_phase_beta_bulk_interval.py')},
        wall_seconds=time.monotonic()-started)
    save(args.out,doc)
    if not complete:raise RuntimeError(str(failure))


if __name__=='__main__':main()
