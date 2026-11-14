#!/usr/bin/env python3
"""Bind a new accepted geometry to complete radial jets and patch/mean work.

This is an actual consumer of every saved physical quintic coefficient and
every original radial interval. Exact rational Bernstein bounds enclose all
state values and first/second physical-s derivatives, then signed dyadic
rounding is checked outward. The original polynomial's two-sided knot jets
are not declared equal. No background, mean, full Cartesian surface, true
PDE, global reach, fixed held region or closed surface is certified here.

The accompanying JSON contract makes those remaining inputs explicit and
binds them to this exact accepted field. A structurally valid contract is
not a proof. No Flow, RHS, Newton, Node worker or source integral is run.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import time

import numpy as np
from flint import fmpq as Q


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def exact_float(value):
    value = float(value)
    if not math.isfinite(value):
        raise ArithmeticError('A finite binary64 coefficient is required')
    return Q(*value.as_integer_ratio())


def fraction(value):
    return str(value.p)+'/'+str(value.q)


def unpack(value):
    m, e = int(value[0]), int(value[1])
    return Q(m*2**e) if e >= 0 else Q(m, 2**(-e))


def signed_dyadic(value, upper, bits=128):
    """Exact floor/ceiling, including negative endpoints and very small ones."""
    if not value:
        return ['0', 0]
    n, d = int(value.p), int(value.q)
    e = abs(n).bit_length()-d.bit_length()-bits+1
    while True:
        nn, dd = (n, d*2**e) if e >= 0 else (n*2**(-e), d)
        m = -((-nn)//dd) if upper else nn//dd
        if abs(m).bit_length() <= bits:
            break
        e += 1
    result = [str(m), e]
    if (upper and unpack(result) < value) or (not upper and unpack(result) > value):
        raise ArithmeticError('A signed interval endpoint was rounded inward')
    return result


def local_file(parent, name):
    if Path(name).name != name:
        raise ValueError('Saved coefficient chunks must have local basenames')
    return parent/name


def load_accepted(primary, raw_path, tail_path, interior_path):
    from strong_actual_fixed_control_response import raw_flat
    from strong_actual_augmented_core import LAYOUT
    saved, raw, tail = map(read, (primary, raw_path, tail_path))
    M = int(saved['modes'])
    n = 3*M+1
    if (not saved.get('solver_success') or saved.get('audit_pending', True)
            or not saved['config'].get('actual_nonlinear_tail')
            or not raw.get('solver_success') or raw.get('physical_surface') is not False
            or saved['raw_collocation_checkpoint']['sha256'] != sha(raw_path)):
        raise ValueError('A completely accepted physical/raw nonlinear-tail field is required')
    identity = raw['identity']
    for old, new in (('gauge','gauge_amplitude'),('profile','frozen_profile'),
            ('reference_coefficients','chart_reference_coefficients'),
            ('reference_frequencies','chart_reference_frequencies'),
            ('physical_tail_parameters','physical_tail_parameters'),
            ('physical_tail_cut','physical_tail_cut')):
        if identity[old] != saved[new]:
            raise ValueError('The accepted material/physical identity differs: '+old)
    if (identity['numerical_reference_knots'] != saved['numerical_meridian_chart']['reference_t']
            or not identity.get('coupling_context',{}).get('actual_nonlinear_tail')):
        raise ValueError('The actual coupled numerical material chart differs')
    if (int(saved['config'].get('base_mode',2)) != 2
            or saved['angular_chart'] != 'general-support-core-blend-v1'
            or saved['core']['frequencies'] != list(range(2,2*M+1,2))):
        raise ValueError('The complete original base2 cylindrical state layout is required')
    hashes = {str(p):sha(p) for p in (primary,raw_path,tail_path)}
    arrays = {}
    for key in ('x','y','p','cubic','rms'):
        a = np.asarray(raw_flat(raw_path,raw,key,hashes),dtype=np.float64).reshape(raw['arrays'][key]['shape'])
        if not np.isfinite(a).all():
            raise ArithmeticError('A complete accepted raw array is nonfinite')
        arrays[key] = a
    t, y, p = (arrays[key] for key in ('x','y','p'))
    if (t.ndim != 1 or t[0] != 0. or t[-1] != 1. or not np.all(np.diff(t)>0)
            or y.shape != (n,len(t)) or arrays['cubic'].shape != (4,len(t)-1,n)
            or p.shape not in ((M,),(M+3,)) or not np.array_equal(p,raw['parameter_state'])):
        raise ValueError('Complete accepted raw dimensions changed')
    if ((len(p)==M and not identity.get('fixed'))
            or (len(p)==M+3 and identity.get('parameter_layout')!=LAYOUT)):
        raise ValueError('The current M or M+3 all-core layout is not the original one')
    H = -float(saved['gauge_amplitude'])*y[2*M+1:,-1]
    response = tail['response']
    if (not response.get('converged') or response['residual']>tail['config']['solveTolerance']
            or tail['source_sha256']!=saved['actual_tail']['source_sha256']
            or np.asarray(tail['request']['height'],dtype=np.float64).tobytes()!=H.tobytes()
            or np.asarray(response['checkpoint']['cutHeight'],dtype=np.float64).tobytes()!=H.tobytes()
            or len(response['heightJetJacobian'])!=(3*M+2)*M):
        raise ValueError('The final full H/J actual-tail identity differs')
    x = np.asarray(saved['mesh'],dtype=np.float64)
    if (x.shape!=t.shape or len(x)!=int(saved['nodes']) or not np.isfinite(x).all()
            or x[0]!=0. or x[-1]!=float(saved['meridian_length']) or not np.all(np.diff(x)>0)):
        raise ValueError('The complete physical quintic mesh differs')
    coefficients = np.empty((6,len(x)-1,n),dtype=np.float64)
    chunks, first = [], 0
    for part in saved['pp_coefficient_chunks']:
        file = local_file(primary.parent,part['file'])
        lo, hi = int(part['state_first']), int(part['state_last_exclusive'])
        if lo!=first or not lo<hi<=n or sha(file)!=part['sha256'] or file.stat().st_size!=part['bytes']:
            raise ValueError('Physical quintic chunk coverage or SHA differs')
        with gzip.open(file,'rb') as stream:
            a = np.load(stream,allow_pickle=False)
        if a.dtype!=np.float64 or a.shape!=(6,len(x)-1,hi-lo) or not np.isfinite(a).all():
            raise ValueError('All six original physical quintic coefficients are required')
        coefficients[:,:,lo:hi] = a
        first = hi
        chunks.append(dict(path=str(file),sha256=part['sha256'],bytes=part['bytes'],state_first=lo,state_last_exclusive=hi))
        hashes[str(file)] = part['sha256']
    if first!=n:
        raise ValueError('A physical Fourier state was omitted')
    interior = None
    if interior_path:
        interior=read(interior_path)
        if (interior.get('input_sha256')!=sha(primary) or interior['modes']!=M
                or interior['config'].get('mean_angular')!=max(512,16*n)):
            raise ValueError('The complete-mean interior witness belongs to another accepted field')
        hashes[str(interior_path)] = sha(interior_path)
    del arrays, y
    return saved, raw, tail, x, t, coefficients, chunks, hashes, H, interior


def jet_boxes(coefficients, length):
    """Exact Bernstein hulls on one complete physical-s polynomial cell."""
    hpower = [Q(1)]
    for j in range(1,6):
        hpower.append(hpower[-1]*length)
    transforms = []
    for order in range(3):
        degree = 5-order
        transforms.append([[hpower[j]*Q(math.factorial(j+order),math.factorial(j))
                            *Q(math.comb(i,j),math.comb(degree,j))
                            for j in range(i+1)] for i in range(degree+1)])
    by_order = [[],[],[]]
    for state in range(coefficients.shape[1]):
        power = [exact_float(coefficients[5-j,state]) for j in range(6)]
        for order in range(3):
            bernstein=[sum((row[j]*power[j+order] for j in range(len(row))),Q(0))
                       for row in transforms[order]]
            lo, hi = min(bernstein), max(bernstein)
            by_order[order].append([signed_dyadic(lo,False),signed_dyadic(hi,True)])
    return by_order


def contract():
    rat = {'type':'string','pattern':r'^-?[0-9]+/[1-9][0-9]*$'}
    interval = {'type':'array','items':rat,'minItems':2,'maxItems':2}
    vec = {'type':'array','items':interval,'minItems':3,'maxItems':3}
    sha_type = {'type':'string','pattern':'^[0-9a-f]{64}$'}
    def obj(required, properties):
        return {'type':'object','required':required,'properties':properties,'additionalProperties':True}
    patch = obj(['id','component','phase_class','s_interval','psi_turn_interval',
                 'input_identity_sha256','state_cells','mean_cells','cartesian_jets',
                 'domain','curvature_upper','position_centre','normal_centre',
                 'position_radius','normal_radius','continuous_enclosure_proof_sha256'],{
        'id':{'type':'string'},'component':{'enum':['prefix','tail','cap','marker']},
        'phase_class':{'enum':['rotating','fixed']},'s_interval':interval,'psi_turn_interval':interval,
        'input_identity_sha256':sha_type,'state_cells':{'type':'array','items':{'type':'integer','minimum':0}},
        'mean_cells':{'type':'array','items':{'type':'string'}},
        'cartesian_jets':obj(['X','Xs','Xtheta','Xss','Xstheta','Xthetatheta'],
            {key:vec for key in ['X','Xs','Xtheta','Xss','Xstheta','Xthetatheta']}),
        'domain':obj(['rho_lower','area_lower','P_lower','W_lower','D_lower'],
            {key:rat for key in ['rho_lower','area_lower','P_lower','W_lower','D_lower']}),
        'curvature_upper':rat,'position_centre':vec,'normal_centre':vec,
        'position_radius':rat,'normal_radius':rat,'continuous_enclosure_proof_sha256':sha_type})
    mean = obj(['id','s_interval','input_identity_sha256','field_definition_sha256',
                'measure','global_anchor_sha256','m','m_s','H','quadrature_error',
                'field_repair_error','whole_angular_cover_sha256','proof_sha256'],{
        'id':{'type':'string'},'s_interval':interval,'input_identity_sha256':sha_type,
        'field_definition_sha256':sha_type,'measure':{'const':'uniform original computational psi'},
        'global_anchor_sha256':sha_type,'m':interval,'m_s':interval,'H':interval,
        'quadrature_error':obj(['angular_alias','radial_Gauss6','floating_evaluation'],
            {key:obj(['A0','A1','A2'],{axis:rat for axis in ['A0','A1','A2']})
             for key in ['angular_alias','radial_Gauss6','floating_evaluation']}),
        'field_repair_error':obj(['A0','A1','A2'],{key:rat for key in ['A0','A1','A2']}),
        'whole_angular_cover_sha256':sha_type,'proof_sha256':sha_type})
    return dict(
        **{'$schema':'https://json-schema.org/draft/2020-12/schema',
           '$id':'urn:math-research:visible-flex-larger:newg-continuous-patch-mean-v1'},
        title='Same accepted new-g continuous Cartesian patches and complete mean contract',
        description='Structural validation is not mathematical certification. Every stated radius, domain, seam, material identity, cover and all-pair margin needs its independently checked producer/proof.',
        type='object',required=['schema','input_identity_sha256','field_definition_sha256',
            'global_frame_anchor','patches','means','coverage','assembly','held_region','reach','metric'],
        properties=dict(schema={'const':'newg-continuous-patch-mean-certificate-v1'},
            input_identity_sha256=sha_type,field_definition_sha256=sha_type,
            global_frame_anchor=obj(['definition','sha256'],{'definition':{'type':'object'},'sha256':sha_type}),
            patches={'type':'array','minItems':1,'items':patch},means={'type':'array','minItems':1,'items':mean},
            coverage=obj(['complete_surface','parameter_cover_proof_sha256','angular_periodic_identification_sha256'],
                {'complete_surface':{'const':True},'parameter_cover_proof_sha256':sha_type,'angular_periodic_identification_sha256':sha_type}),
            assembly=obj(['closed_connected_C2','all_Cartesian_seams_sha256','injectivity_proof_sha256','phase_law_proof_sha256'],
                {'closed_connected_C2':{'const':True},'all_Cartesian_seams_sha256':sha_type,
                 'injectivity_proof_sha256':sha_type,'phase_law_proof_sha256':sha_type}),
            held_region=obj(['patch_ids','nonempty_interior_proof_sha256','pointwise_fixed_for_all_phase_sha256','diameter_lower'],
                {'patch_ids':{'type':'array','items':{'type':'string'},'minItems':1},
                 'nonempty_interior_proof_sha256':sha_type,'pointwise_fixed_for_all_phase_sha256':sha_type,'diameter_lower':rat}),
            reach=obj(['D_upper','tau','curvature_upper','complete_pair_cover_sha256','short_path_bounds_sha256'],
                {'D_upper':rat,'tau':rat,'curvature_upper':rat,'complete_pair_cover_sha256':sha_type,'short_path_bounds_sha256':sha_type}),
            metric=obj(['same_prescribed_g_sha256','continuous_relative_error_upper','same_g_refinement_manifest_sha256'],
                {'same_prescribed_g_sha256':sha_type,'continuous_relative_error_upper':rat,'same_g_refinement_manifest_sha256':sha_type})),
        mathematical_requirements_not_implied_by_JSON_validation=[
            'All interval endpoints ordered; all named strict lower bounds positive; all error radii nonnegative.',
            'Exact radial/angle/phase cover, including both sides of every seam and the actual cap/tail components.',
            'Every X/normal ball covers its continuous patch after all background, state-repair, mean and evaluation costs.',
            'One common global Cartesian frame/height anchor; no independent per-patch recentering.',
            'The complete source has P=|d|^2>0, W=|d cross e|^2>0 and D=W-c^2 P^3>0 in all mean/homotopy boxes.',
            'R11 all-phase formulas apply only after the actual S_phi=R_phi A union B decomposition is proved.',
            'R16 near-diagonal path bounds do not replace independent injectivity/closedness.',
            'tau >=3 D_upper/100, curvature_upper*tau<=1, held diameter_lower>=D_upper/5, and every nonlocal pair covered.',
            'The stated complete-mean map is distinct from finite angular/Gauss samples until their errors are bounded.',
            'Old q096 chart/mean or old g/candidate/H_tail certificates are not relabelled for this new identity.'])


def save(path,value):
    p=Path(path);raw=(json.dumps(value,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if p.suffix=='.gz':raw=gzip.compress(raw,compresslevel=9,mtime=0)
    if len(raw)>=5_000_000 or p.exists():
        raise ValueError('Use a fresh artifact smaller than5MB')
    p.write_bytes(raw)
    return dict(path=str(p),sha256=sha(p),bytes=len(raw))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('input','raw','tail','source-topic','port','out-prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--interior-audit',type=Path)
    ap.add_argument('--angular-panels',type=int,default=96)
    ap.add_argument('--intervals-per-chunk',type=int,default=64)
    a=ap.parse_args();begin=time.monotonic()
    if a.angular_panels<4 or a.angular_panels%4 or not 1<=a.intervals_per_chunk<=64:
        raise ValueError('Use a full fourfold angle cover and bounded radial chunks')
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if list(a.out_prefix.parent.glob(a.out_prefix.name+'-*')):
        raise FileExistsError('Fresh complete packet prefix required')
    data=load_accepted(a.input,a.raw,a.tail,a.interior_audit)
    saved,raw,tail,x,t,coefficients,pp_chunks,hashes,H,interior=data
    M=int(saved['modes']);n=3*M+1
    origin_path=a.source_topic/'source-origin.json';origin=read(origin_path)
    if origin['source_revision']!='869436630c99aa5a68afb55bd8877c826034d117':
        raise ValueError('The exact pinned physical source origin changed')
    if sha(a.port)!=saved['physical_port_sha256']:
        raise ValueError('The actual physical port identity differs')
    for p in (Path(__file__),origin_path,a.port,
              Path(__file__).with_name('strong_actual_fixed_control_response.py'),
              Path(__file__).with_name('strong_actual_augmented_core.py')):
        hashes[str(p)]=sha(p)
    identity=dict(primary_sha256=sha(a.input),raw_sha256=sha(a.raw),tail_sha256=sha(a.tail),
        frozen_profile=saved['frozen_profile'],gauge=saved['gauge_amplitude'],
        meridian_length=saved['meridian_length'],chart_reference_coefficients=saved['chart_reference_coefficients'],
        chart_reference_frequencies=saved['chart_reference_frequencies'],
        angular_chart=saved['angular_chart'],numerical_meridian_chart=saved['numerical_meridian_chart'],
        physical_tail_parameters=saved['physical_tail_parameters'],physical_tail_cut=saved['physical_tail_cut'],
        physical_port_sha256=saved['physical_port_sha256'],tail_source_sha256=tail['source_sha256'],
        complete_physical_pp_chunks=pp_chunks,original_source_revision=origin['source_revision'],
        complete_H_float64le_sha256=hashlib.sha256(H.astype('<f8').tobytes()).hexdigest())
    identity_sha=hashlib.sha256(canonical(identity)).hexdigest()
    contract_record=save(str(a.out_prefix)+'-contract.json',contract())
    rows,records=[],[];checked=0
    for i in range(len(x)-1):
        left,right=exact_float(x[i]),exact_float(x[i+1]);length=right-left
        bounds=jet_boxes(coefficients[:,i,:],length)
        checked+=6*n
        rows.append(dict(original_interval=i,s_interval=[fraction(left),fraction(right)],
            raw_t_interval=[fraction(exact_float(t[i])),fraction(exact_float(t[i+1]))],
            state_jet_intervals=bounds,jet_order=['Y','Y_s','Y_ss'],
            angular_patch_indices=[0,a.angular_panels],
            angular_patch_rule='psi/(2*pi) in [j/N,(j+1)/N], j=0,...,N-1; endpoints identified only by the original periodic chart',
            full_mean_request=dict(id='mean-'+str(i),same_radial_interval=True,whole_angular_period_required=True,
                mean_height_anchor='One global zero-height mean anchor at physical s=0, as in the original height_integral; do not reset by cell.',
                required=['continuous m and m_s','continuous primitive H','strict full P/W/D domain',
                          'angular alias to original1360 rule','radial Gauss6 and floating evaluation errors','C2 state repair effects']),
            state_bounds_are_exact_original_polynomial_only=True,
            continuous_Cartesian_patch_and_mean_certified=False))
        if len(rows)==a.intervals_per_chunk or i==len(x)-2:
            rec=save(str(a.out_prefix)+f'-radial{len(records):03d}.json.gz',dict(
                schema='newg-complete-radial-state-jet-request-v1',input_identity_sha256=identity_sha,
                modes=M,state_count=n,angular_panels=a.angular_panels,
                signed_endpoint_format='[integer_mantissa,binary_exponent]; each interval [lower,upper]',
                coefficient_interpretation='Every original saved binary64 physical quintic coefficient and knot is exact; no PDE derivative substitution.',
                first_interval=rows[0]['original_interval'],last_interval_exclusive=i+1,rows=rows))
            records.append(rec);rows=[]
            print(json.dumps(dict(event='newg_radial_jet_chunk',completed=i+1,total=len(x)-1,
                sha256=rec['sha256'],bytes=rec['bytes'])),flush=True)
    summary=dict(schema='newg-complete-state-jets-patch-mean-preparation-v1',scope=__doc__,
        finished=True,source_sha256=sha(__file__),source_and_input_sha256=hashes,
        input_identity_sha256=identity_sha,input_identity=identity,contract=contract_record,
        original_physical_intervals=len(x)-1,original_raw_nodes=len(t),modes=M,complete_state_count=n,
        all_six_quintic_coefficients_read=True,all_original_intervals_covered=True,
        all_radial_state_jets_exactly_enclosed=True,outward_signed_endpoint_comparisons=checked,
        original_parameter_count=raw['arrays']['p']['shape'][0],raw_array_and_physical_quintic_SHA_complete=True,
        full_H_request_checkpoint_bitwise_equal=True,radial_chunks=records,
        complete_prefix_patch_request_count=(len(x)-1)*a.angular_panels,
        angular_panels=a.angular_panels,whole_angular_period_required=True,
        original_complete_mean_rule=dict(angular=max(512,16*n),Gauss_order=6,anchor_s='0/1',anchor_mean_height='0/1'),
        interior_sample_witness=interior['top']['kappa'] if interior else None,
        interior_witness_is_not_a_continuous_enclosure=True,
        accepted_nonmean_seam_diagnostic=saved['actual_tail']['seam_nonmean'],
        pending_actual_invariants=['new-g exact profile/Gauss64 and material-angle transport',
            'actual C2 state seam repair and complete mean A0/A1/A2',
            'all Cartesian jet/domain/normal patch enclosures','full prefix-tail Cartesian seam in one frame',
            'actual infinite continuation/closing caps and exact fixed-region parameterization',
            'continuous global diameter, injectivity, all nonlocal pairs and fixed-g refinement'],
        background_mean_Cartesian_closed_surface_or_reach_claimed=False,
        old_g_or_q096_chart_certificate_transferred=False,
        new_ODE_Node_Newton_or_geometry_sampling_calls=0,
        elapsed_seconds=time.monotonic()-begin,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out=save(str(a.out_prefix)+'-manifest.json',summary)
    print(json.dumps(dict(event='newg_complete_radial_state_packet_finished',manifest=out,
        exact_intervals=len(x)-1,outward_endpoint_checks=checked,
        continuous_Cartesian_mean_and_reach_certified=False,elapsed_seconds=summary['elapsed_seconds'],
        peak_rss_kib=summary['peak_rss_kib'])),flush=True)


if __name__=='__main__':
    main()
