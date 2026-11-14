#!/usr/bin/env python3
"""Complete weighted weak-residual Gram majorants for the even core reference.

The field input must be an actually completed true coefficient rectangle on
the same whole parameter family. Finite products keep every Fourier mode.
Exact continuous references keep both Cauchy channels and all radial joins.
Scalar and divergence loads are distinct; a negative boundary norm is never
promoted to a positive-order norm by changing a label.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import gzip
import io
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,acb_mat,acb_poly,ctx
from fourfold_phase_core_even_reference import ExactEvenCoreReference
from fourfold_phase_core_flow_collect import read,sha,norm,write
from fourfold_phase_core_cell_flow import exact_matrix,ball_record
from fourfold_phase_low_feedback_paid_inputs import adjoint,hermitian_enclosure,midpoint
from fourfold_phase_cap_energy_collect import hermitian_norm_bound

SPACES=(('H0',Fraction(0)),('Hhalf',Fraction(1,2)),
        ('H1',Fraction(1)),('Hthreehalf',Fraction(3,2)))
COMPONENTS=('radial_all','radial_high','angular_high','scalar_all','scalar_high')
FIELDS=('a','b','c','tau','sigma')
ODD={'b','sigma'}  # angular theta parity
RADIAL_ODD={'b'}   # sigma=omega*ell is even in r

def afraction(x):
    x=Fraction(x);return arb(x.numerator)/x.denominator
def matrix_state_polynomials(rows,first,count,columns):
    return [[acb_poly([row[first+k,j] for row in rows]) for j in range(columns)]
            for k in range(count)]
def add_gram(destination,values,weight):
    row=acb_mat([values]);value=weight*(adjoint(row)*row)
    return destination+value
def gram_norm(G):
    answer,_=hermitian_norm_bound(hermitian_enclosure(G))
    if not answer.is_finite():raise ValueError('nonfinite positive Gram norm')
    return answer.upper()
def reference_moduli(rows,n,columns,space):
    exponent=afraction(space)
    result={'w':arb(0),'wr':arb(0),'dw':arb(0)}
    states=rows['physical_state_coefficients'];derivative=rows['physical_radial_derivative_coefficients']
    N=(n-1)//2
    for source,key,angular in ((states,'w',False),(derivative,'wr',False),(states,'dw',True)):
        total=arb(0)
        for item in source:
            matrix=acb_mat(n,columns)
            for k in range(n):
                mode=k-N
                weight=arb(max(1,4*abs(mode)))**exponent
                if angular:weight*=acb(0,4*mode)
                for j in range(columns):matrix[k,j]=weight*item[k,j]
            total+=norm(matrix)
        result[key]=total.upper()
    return result
def dominating_gram(rows,halfwidth):
    """Weighted Cauchy--Schwarz in the finite time powers, before integration."""
    factors=[];summation=arb(0)
    for i,G in enumerate(rows):
        size=gram_norm(G)
        if size==0:continue
        factor=(arb(2)*size/(2*i+1)).sqrt().upper()
        if not factor>0:raise ValueError('invalid positive temporal Gram weight')
        factors.append((i,G,factor));summation+=factor
    if not factors:return acb_mat(rows[0].nrows(),rows[0].ncols()),arb(0)
    result=acb_mat(rows[0].nrows(),rows[0].ncols())
    for i,G,factor in factors:result+=(arb(2)/(2*i+1)/factor)*G
    result=halfwidth*summation*result
    return hermitian_enclosure(result),gram_norm(result).sqrt().upper()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cover-root',type=Path,required=True)
    ap.add_argument('--field-report',type=Path,required=True)
    ap.add_argument('--leaf-index',type=int,required=True)
    ap.add_argument('--side',type=int,choices=(-1,1),default=1)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    wall,cpu=time.monotonic(),time.process_time()
    doc=dict(kind='complete_actual_even_core_weak_residual_weighted_Gram_majorants',
        complete=False,source_sha256=sha(__file__),bits=args.bits,
        field_report=dict(path=str(args.field_report),sha256=sha(args.field_report)))
    write(args.out,doc)
    try:
        field=read(args.field_report)
        producer_by_kind={
            'complete_uniform_true_core_coefficient_polynomial':'fourfold_phase_core_field_polynomial.py',
            'complete_uniform_true_core_coefficient_and_wiring_polynomial':'fourfold_phase_core_source_wiring_polynomial.py'}
        if not field.get('complete') or field.get('kind') not in producer_by_kind:
            raise ValueError('true coefficient rectangle is not complete')
        producer=producer_by_kind[field['kind']]
        if sha(Path(__file__).with_name(producer))!=field['source_sha256']:
            raise ValueError('field producer source changed')
        for name,digest in field['dependency_sha256'].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError('field producer dependency changed: '+name)
        record=field['arrays']
        if sha(record['path'])!=record['sha256']:raise ValueError('field arrays changed')
        array_path=Path(record['path'])
        stream=io.BytesIO(gzip.decompress(array_path.read_bytes())) if array_path.suffix=='.gz' else array_path
        with np.load(stream,allow_pickle=False) as saved:
            raw=np.array(saved['rotated_positive_real_dyadic_coefficients'],copy=True)
        if np.any(~np.isfinite(raw)):raise ValueError('field polynomial is nonfinite')
        ref=ExactEvenCoreReference(args.cover_root)
        for key,value in ref.identity.items():
            if field['identity'].get(key)!=value:raise ValueError('different true core family: '+key)
        if not 0<=args.leaf_index<len(ref.leaves):raise ValueError('reference leaf absent')
        leaf=ref.leaves[args.leaf_index]
        if leaf['exact_interval']!=field['exact_real_interval']:
            raise ValueError('field and reference use different physical intervals')
        expected=list(FIELDS)+(['alpha','v'] if field['kind']==
            'complete_uniform_true_core_coefficient_and_wiring_polynomial' else [])
        if field['fields']!=expected or raw.shape[0]!=len(expected):
            raise ValueError('field order or complete tensor shape changed')
        raw=raw[:len(FIELDS)]
        state=ref.coefficients(args.leaf_index,args.side)
        n,d,N=ref.n,ref.dimension,ref.N
        states=state['physical_state_coefficients'];radial=state['physical_radial_derivative_coefficients']
        w=matrix_state_polynomials(states,0,n,d)
        wr=matrix_state_polynomials(radial,0,n,d)
        p=matrix_state_polynomials(states,n,n,d)
        pr=matrix_state_polynomials(radial,n,n,d)
        dw=[[acb(0,4*(k-N))*poly for poly in row] for k,row in enumerate(w)]
        m,K=raw.shape[1],raw.shape[2]-1
        if raw.shape[0]!=len(FIELDS):raise ValueError('field tensor shape differs')
        scalar={}
        for field_index,name in enumerate(FIELDS):
            modes={}
            for k in range(-K,K+1):
                rotation=(acb(0,1 if k>0 else -1) if name in ODD else acb(1))
                parity=args.side if name in RADIAL_ODD else 1
                values=[parity*rotation*arb(float(raw[field_index,i,abs(k)])) for i in range(m)]
                if name in ODD and k==0:values=[acb(0)]*m
                modes[k]=acb_poly(values)
            scalar[name]=modes
        degree=m+len(states)-2
        zero=acb_poly()
        grams={name:{label:[acb_mat(d,d) for _ in range(degree+1)]
                     for label,_ in SPACES} for name in COMPONENTS}
        frequencies=list(range(-K-N,K+N+1))
        for frequency in frequencies:
            rr=[];rt=[];r0=[]
            for column in range(d):
                fr,ft,f0=acb_poly(),acb_poly(),acb_poly()
                for index,mode in enumerate(range(-N,N+1)):
                    lag=frequency-mode
                    if abs(lag)>K:continue
                    a,b,c,tau,sigma=[scalar[name][lag] for name in FIELDS]
                    fr+=a*wr[index][column]+b*dw[index][column]
                    ft+=b*wr[index][column]+c*dw[index][column]+sigma*w[index][column]
                    f0+=sigma*dw[index][column]-tau*w[index][column]
                if abs(frequency)<=N:
                    index=frequency+N
                    fr-=p[index][column]
                    f0-=pr[index][column]+acb(0,4*frequency)*ft
                rr.append(fr);rt.append(ft);r0.append(f0)
            high=abs(frequency)>N
            component_rows={'radial_all':rr,'scalar_all':r0}
            if high:component_rows.update(radial_high=rr,angular_high=rt,scalar_high=r0)
            for name,polynomials in component_rows.items():
                for i in range(degree+1):
                    values=[poly[i] for poly in polynomials]
                    for label,power in SPACES:
                        weight=arb(max(1,4*abs(frequency)))**afraction(2*power)
                        grams[name][label][i]=add_gram(grams[name][label][i],values,weight)
            if frequency%64==0:
                doc.update(stage='finite weak source Gram accumulation',last_completed_finite_frequency=frequency,
                    final_finite_frequency=frequencies[-1],CPU_seconds=time.process_time()-cpu,
                    wall_seconds=time.monotonic()-wall)
                write(args.out,doc)
                print(json.dumps(dict(stage='all finite Fourier weak loads',frequency=frequency,
                    last_frequency=frequencies[-1])),flush=True)
        centers=np.empty((len(COMPONENTS),len(SPACES),d,d),complex)
        records={};h=state['positive_halfwidth']
        for label,power in SPACES:
            sizes=reference_moduli(state,n,d,power)
            errors={name:arb(field['field_reports'][name]['complete_real_time_multiplier_errors'][label]['ball']).upper()
                    for name in FIELDS}
            er=errors['a']*sizes['wr']+errors['b']*sizes['dw']
            et=errors['b']*sizes['wr']+errors['c']*sizes['dw']+errors['sigma']*sizes['w']
            e0=errors['sigma']*sizes['dw']+errors['tau']*sizes['w']
            # P_N and P_H contract every stated diagonal H^s norm.
            # D P_N has norm at most 4N, whereas high scalar has no D term.
            fees={'radial_all':er,'radial_high':er,'angular_high':et,
                  'scalar_all':e0+4*N*et,'scalar_high':e0}
            records[label]=dict(reference_whole_real_time_moduli={k:ball_record(v) for k,v in sizes.items()},
                components={})
            for component in COMPONENTS:
                G,finite_norm=dominating_gram(grams[component][label],h)
                chosen=midpoint(G)
                chosen=(chosen+chosen.conjugate().T)/2
                selection=norm(G-exact_matrix(chosen))
                E=((2*h).sqrt()*fees[component]).upper()
                true_radius=(selection+2*finite_norm*E+E*E).upper()
                finite_center_norm=gram_norm(exact_matrix(chosen))
                true_norm=(finite_center_norm+true_radius).sqrt().upper()
                centers[COMPONENTS.index(component),[x[0] for x in SPACES].index(label)]=chosen
                records[label]['components'][component]=dict(
                    finite_PSD_Gram_majorant_norm=ball_record(finite_norm*finite_norm),
                    finite_PSD_Gram_selection_error=ball_record(selection),
                    complete_actual_residual_L2r_Hs_difference=ball_record(E),
                    complete_true_PSD_Gram_diagonal_radius=ball_record(true_radius),
                    true_residual_operator_norm_upper=ball_record(true_norm))
        endpoint_flux=ref.endpoint_even_flux()
        endpoint_center=midpoint(endpoint_flux)
        endpoint_fee=norm(endpoint_flux-exact_matrix(endpoint_center))
        arrays=args.out.with_suffix('.npz');arrays.parent.mkdir(parents=True,exist_ok=True)
        np.savez_compressed(arrays,finite_PSD_Gram_majorant_centers=centers,
            raw_reference_even_endpoint_flux_center=endpoint_center)
        doc.update(complete=True,identity=ref.identity,leaf_index=args.leaf_index,
            exact_physical_interval=state['exact_physical_interval'],side=args.side,
            physical_modes=N,physical_input_columns=d,spatial_norm_weights='w_0=1, w_k=(4|k|)^s for k!=0',
            exact_weak_form='integral Rr*v_r+Rtheta*v_theta+R0*v, relative to the finite endpoint raw p ports',
            exact_sources=dict(Rr='a*w_r+b*w_theta-p_N',
                Rtheta='P_H(b*w_r+c*w_theta+sigma*w)',
                R0='sigma*w_theta-tau*w-p_N,r-D P_N(b*w_r+c*w_theta+sigma*w)'),
            complete_Fourier_output_range_of_finite_polynomial=[-K-N,K+N],
            exact_reference_definition='Compress each complete generator and transfer by the exact cosine isometry; Z is the resulting finite time polynomial, R=Z Z(-1)^-1+(u+1)(Tcos-Z(1)Z(-1)^-1)/2. The waist map is (A^-1,0)/sqrt(2), positive state is diag(Qcos,Qcos) R Pprefix times that map, and the negative state reflects w evenly and p oddly. No 18-input Dirichlet inverse is used.',
            exact_reference_C0_all_radial_joins=True,
            raw_reference_even_endpoint_flux_selection_error=ball_record(endpoint_fee),
            reference_endpoint_flux_scope='The saved five-by-five raw reference flux is 8 C A^-1 before Hermitian projection or selected-core rounding. It is not silently identified with the actual uniform DN or the selected Hermitian low-block center; any assembly must include their explicit difference.',

            paired_physical_cosine_height_inputs=True,
            angular_mean_retained=True,
            regular_port_scope='The paired regular coordinate is a separate sixth block coordinate; it has zero direct core reference column and remains in the complete cap response.',
            available_physical_wiring_norms={name:field['field_reports'][name].get('complete_true_real_time_multiplier_norms') for name in ('alpha','v') if name in field['field_reports']},
            reference_endpoint_selection_correction_norm=ball_record(state['endpoint_selection_correction_norm']),
            records=records,component_order=list(COMPONENTS),space_order=[x[0] for x in SPACES],
            arrays=dict(path=str(arrays),sha256=sha(arrays),bytes=arrays.stat().st_size),
            Gram_contract='For every endpoint height vector v, its actual residual squared norm in each stated L2(dr;Hs(theta)) is at most v*(saved Gram center + recorded nonnegative radius I)v. This is a PSD majorant, not an assertion that the displayed center is the actual residual Gram.',
            scope=['All finite Fourier products and all complete true coefficient errors are paid on this one real leaf and the same eta family.',
                   'Radial and angular divergence loads, scalar loads, low defects and high outputs remain distinct. Their dual weights are not supplied by this report.',
                   'Neither a full high inverse nor a Schur complement bound follows without the corresponding true weak-solver contract.'])
    except Exception as exc:
        doc.update(failure=repr(exc),traceback=traceback.format_exc())
    doc.update(CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_core_even_reference.py','fourfold_phase_core_even_collect.py',
            'fourfold_phase_core_field_polynomial.py','fourfold_phase_core_source_wiring_polynomial.py',
            'fourfold_phase_core_flow_collect.py','fourfold_phase_low_feedback_paid_inputs.py')})
    write(args.out,doc)
    print(json.dumps({key:doc.get(key) for key in ('complete','exact_physical_interval','failure','CPU_seconds','wall_seconds')},
        indent=2,allow_nan=False),flush=True)
    if not doc['complete']:raise SystemExit(1)
if __name__=='__main__':main()
