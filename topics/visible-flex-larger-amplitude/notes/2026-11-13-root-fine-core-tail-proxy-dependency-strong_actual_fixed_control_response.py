#!/usr/bin/env python3
"""Differentiate an accepted actual-tail problem in physical design controls.

At the unchanged accepted raw state, the fixed-metric full Jacobian has all
core coefficients as boundary unknowns.  Delta/LB/vp, and optional other
prefix-only controls, enter as external forcing columns.  A 3x3 exchange
then prescribes actual c2/c4/c6 while solving for those three controls.

The recorded complete nonlinear-tail height Jacobian is used only at its
exact recorded boundary H.  There is no Node worker, new tail solve, BVP
continuation, or new accepted surface.  The original actual/fixed loader and
boundary Jacobian are reused, with a local affine tail tangent for this
derivative calculation only.  --metadata-only does not import NumPy or load
any Flow; it checks the linked input data and complete H byte identity.
"""
from __future__ import annotations
import argparse
import array
import ast
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys

HERE=Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def raw_flat(path,record,name,hashes):
    item=record['arrays'][name];result=[]
    if item['dtype']!='float64':
        raise ValueError('Expected raw float64 state')
    for chunk in item['chunks']:
        if chunk['first']!=len(result) or Path(chunk['file']).name!=chunk['file']:
            raise ValueError('Unexpected raw chunk layout')
        file=Path(path).parent/chunk['file']
        if digest(file)!=chunk['sha256']:
            raise ValueError('Raw state chunk SHA mismatch')
        hashes[str(file)]=chunk['sha256']
        data=gzip.decompress(file.read_bytes())
        if data[:6]!=b'\x93NUMPY':raise ValueError('Expected NPY array')
        version=tuple(data[6:8])
        if version==(1,0):start=10;size=struct.unpack('<H',data[8:10])[0]
        elif version in ((2,0),(3,0)):start=12;size=struct.unpack('<I',data[8:12])[0]
        else:raise ValueError('Unsupported NPY version')
        header=ast.literal_eval(data[start:start+size].decode('utf-8'))
        if header['descr'] not in ('<f8','>f8','=f8') or header['shape']!=(chunk['count'],):
            raise ValueError('Unexpected raw chunk dtype or shape')
        payload=data[start+size:]
        if len(payload)!=8*chunk['count']:raise ValueError('Incorrect raw array length')
        values=array.array('d')
        if values.itemsize!=8:raise ValueError('Expected binary64 platform')
        values.frombytes(payload)
        if ((header['descr'][0]=='<' and sys.byteorder!='little')
                or (header['descr'][0]=='>' and sys.byteorder!='big')):values.byteswap()
        result.extend(values)
    if len(result)!=math.prod(item['shape']) or not all(math.isfinite(x) for x in result):
        raise ValueError('Incomplete or nonfinite raw array')
    return result


def validate_inputs(checkpoint,raw_path,tail_path,hashes):
    saved,raw,tail=(document(p) for p in (checkpoint,raw_path,tail_path))
    for path in (checkpoint,raw_path,tail_path):hashes[str(path)]=digest(path)
    if (not saved.get('solver_success') or saved.get('audit_pending',True)
            or not saved['config'].get('actual_nonlinear_tail')
            or not saved['config'].get('fixed_metric') or not raw.get('solver_success')):
        raise ValueError('A completed actual fixed-metric solution is required')
    if saved['raw_collocation_checkpoint']['sha256']!=hashes[str(raw_path)]:
        raise ValueError('The physical checkpoint names another raw state')
    ident=raw['identity'];context=ident.get('coupling_context')
    if not ident['fixed'] or not context or not context.get('actual_nonlinear_tail'):
        raise ValueError('The accepted raw layout is not fixed/actual')
    for raw_key,final_key in (('gauge','gauge_amplitude'),('profile','frozen_profile'),
            ('physical_tail_parameters','physical_tail_parameters'),('physical_tail_cut','physical_tail_cut'),
            ('reference_coefficients','chart_reference_coefficients'),('reference_frequencies','chart_reference_frequencies')):
        if ident[raw_key]!=saved[final_key]:raise ValueError('Fixed data mismatch: '+raw_key)
    if ident['numerical_reference_knots']!=saved['numerical_meridian_chart']['reference_t']:
        raise ValueError('The accepted numerical reference differs')
    if (saved['frozen_profile'].get('ramp_law')!='hermite_boost_neck'
            or saved['physical_tail_cut'].get('_prefix_bridge',{}).get('kind')!='finite_neck_terminal_v1'):
        raise ValueError('This interface presently supports the recorded neck with sigma=-1')
    modes=int(saved['modes']);n=3*modes+1;m=raw['arrays']['x']['shape'][0]
    if raw['arrays']['y']['shape']!=[n,m] or raw['arrays']['p']['shape']!=[modes]:
        raise ValueError('Fixed-core raw dimensions differ')
    vectors={name:raw_flat(raw_path,raw,name,hashes) for name in ('x','y','p')}
    if vectors['p']!=raw['parameter_state']:raise ValueError('Raw parameter copies differ')
    height=[-saved['gauge_amplitude']*vectors['y'][(2*modes+1+j)*m+m-1] for j in range(modes)]
    request,response=tail['request'],tail['response']
    height_same=(len(request['height'])==modes and
        all(struct.pack('<d',a)==struct.pack('<d',b) for a,b in zip(height,request['height'])))
    if not height_same:
        difference=max((abs(a-b) for a,b in zip(height,request['height'])),default=math.inf)
        raise ValueError('Actual tail tangent is not at the exact complete raw H; max difference='+repr(difference))
    if not request.get('jacobian') or not response.get('converged'):
        raise ValueError('A converged complete tail Jacobian is required')
    if len(response['heightJetJacobian'])!=(3*modes+2)*modes:
        raise ValueError('Tail height-jet Jacobian dimension changed')
    if response['residual']>tail['config']['solveTolerance']:
        raise ValueError('Tail response did not meet its original tolerance')
    if tail.get('source_sha256')!=saved['actual_tail']['source_sha256']:
        raise ValueError('The complete accepted tail source fingerprint differs')
    for key,value in saved['physical_tail_parameters'].items():
        if tail['config'].get(key)!=value:
            raise ValueError('Tail physical parameter mismatch: '+key)
    for key in ('modes','spacing','depth','steps','shootingParts','linearFar','linearSteps',
                'quadrature','solveTolerance','projectionFloor','auditSteps','cuspAwareFlow','actualCuspGrid'):
        if tail['config'].get(key)!=saved['actual_tail']['config'].get(key):
            raise ValueError('Tail finite problem differs: '+key)
    report=dict(scope='Input identity check only, with no Flow, RHS, Jacobian assembly, Node or BVP.',
        full_height_bitwise_equal=True,modes=modes,angular=ident['angular'],nodes=m,
        actual_primary_amplitude=saved['actual_primary_amplitude'],gauge=saved['gauge_amplitude'],
        raw_fixed_parameter_layout=ident['parameter_layout'],raw_tolerance=ident['tol'],
        tail_jacobian_method=response.get('heightJetJacobianMethod'),
        tail_residual=response['residual'],source_sha256=hashes.copy())
    return saved,raw,tail,vectors,report


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--response-checkpoint',type=Path,required=True)
    parser.add_argument('--response-raw',type=Path,required=True)
    parser.add_argument('--response-tail',type=Path,required=True)
    parser.add_argument('--response-out-prefix',type=Path,required=True)
    parser.add_argument('--response-fields',default='delta,boost_length,boost_speed,vu,descending_turn_curvature')
    parser.add_argument('--radial-batch-size',type=int,default=16)
    parser.add_argument('--collocation-batch-size',type=int,default=12)
    parser.add_argument('--metadata-only',action='store_true')
    opts,remaining=parser.parse_known_args()
    prefix=opts.response_out_prefix;output=prefix.with_suffix('.json')
    if output.exists():raise ValueError('Use a fresh response output prefix')
    hashes={str(Path(__file__)):digest(__file__)}
    saved,raw_record,tail,plain,input_report=validate_inputs(
        opts.response_checkpoint,opts.response_raw,opts.response_tail,hashes)
    if opts.metadata_only:
        input_report.update(metadata_only=True,actual_full_jacobian_run=False,inspection_only=True)
        output.write_text(json.dumps(input_report,indent=2)+'\n')
        print(json.dumps(input_report),flush=True);return
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
    import gc
    import io
    import resource
    import time
    from types import SimpleNamespace
    import numpy as np
    import root_actual_bounded_neck as bounded
    import root_block_collocation as blocks
    import root_radial_batching as radial
    import root_raw_collocation as raw
    fields=tuple(filter(None,opts.response_fields.split(',')))
    primary=('delta','boost_length','boost_speed')
    allowed=set(primary+('vu','vd','start_acceleration','descending_turn_curvature',
        'descending_sync_curvature','coast_outward','loop_ratio'))
    if len(set(fields))!=len(fields) or not set(primary)<=set(fields) or not set(fields)<=allowed:
        raise ValueError('Use distinct prefix-only fields including delta/LB/vp')
    if not 1<=opts.radial_batch_size<=48 or not 1<=opts.collocation_batch_size<=24:
        raise ValueError('Only the already checked smaller batches are allowed')
    functions=(radial.value,radial.state_jacobian,blocks.prepare_sys)
    defaults=tuple(f.__defaults__ for f in functions)
    if defaults!=((48,),(48,),(24,)):raise ValueError('Original batching defaults changed')
    radial.value.__defaults__=radial.state_jacobian.__defaults__=(opts.radial_batch_size,)
    blocks.prepare_sys.__defaults__=(opts.collocation_batch_size,)
    for name in ('root_actual_bounded_neck.py','root_actual_neck_bvp.py','root_actual_fixed_refinement.py',
            'root_dual_core_bvp.py','geometric-fixed-dual-prefix.py','root_block_collocation.py',
            'root_radial_batching.py','strong_block_qr.py','root_raw_collocation.py'):
        hashes[str(HERE/name)]=digest(HERE/name)
    ident=raw_record['identity'];context=ident['coupling_context']

    def fixed_argument(name,value):
        value=str(value)
        if name in remaining:
            if remaining[remaining.index(name)+1]!=value:
                raise ValueError('Response restoration argument differs: '+name)
        else:remaining.extend([name,value])

    for name,value in (('--fixed-reference',opts.response_checkpoint),('--restart',opts.response_checkpoint),
            ('--raw-collocation-restart',opts.response_raw),('--q',repr(ident['gauge'])),
            ('--modes',ident['modes']),('--angular',ident['angular']),('--tol',repr(ident['tol'])),
            ('--client',context['client']),('--coupling',context['coupling']),
            ('--actual-tail-tol',repr(context['actual_tail_tolerance'])),
            ('--meridian-chart','all-knots'),('--second-control','boost_length'),
            ('--nodes',0),('--out-prefix',str(prefix)+'-loader')):
        fixed_argument(name,value)
    if '--tail-config' not in remaining:
        raise ValueError('Supply the original actual run tail-config file for raw identity')
    tail_config=Path(remaining[remaining.index('--tail-config')+1])
    if digest(tail_config)!=context['tail_config_sha256']:
        raise ValueError('The original actual tail-config bytes differ')
    hashes[str(tail_config)]=digest(tail_config)
    counters=dict(inspections=0,tail_start_attempts=0)
    original_loader=bounded.adapter.module

    def guard(self):
        counters['tail_start_attempts']+=1
        raise RuntimeError('A tail worker is forbidden in this stored-tangent inspection')

    def save_array(name,value):
        stream=io.BytesIO();np.save(stream,np.asarray(value),allow_pickle=False)
        payload=gzip.compress(stream.getvalue(),mtime=0);path=Path(str(prefix)+'-'+name+'.npy.gz')
        if path.exists() or len(payload)>=5_000_000:raise ValueError('Existing or oversized tangent array')
        path.write_bytes(payload)
        return dict(file=str(path),sha256=hashlib.sha256(payload).hexdigest(),bytes=len(payload),shape=list(np.shape(value)))

    def inspect(self,fun,bc,x,y,p,**kwargs):
        start=time.monotonic();counters['inspections']+=1
        if not self.fixed or self.tail is not None:
            raise ValueError('Expected the actual fixed loader before a tail worker')
        solution,unused=raw.read(opts.response_raw,self,SimpleNamespace(tol=kwargs['tol']))
        for name,value in (('x',x),('y',y),('p',p)):
            if not np.array_equal(value,getattr(solution,name)):
                raise ValueError('The complete accepted raw state changed: '+name)
        height=np.asarray(tail['request']['height']);response=tail['response']
        slope=np.asarray(response['jets']['slope']);JH=np.asarray(response['heightJetJacobian']).reshape(3*self.M+2,self.M)[:self.M].copy()
        if not np.array_equal(self.tail_height(y[:,-1]),height):
            raise ValueError('Live bridge convention differs from the complete stored H')
        self.tail_boundary=lambda value:(slope+JH@(self.tail_height(value)-height),JH)
        self.select(p);self.initial(p);baseline_flow=self.flow(p[0]);baseline_cfg=dict(self.cfg)
        baseline_core=np.asarray(self._core.coefficients).copy()
        if not np.array_equal(baseline_core,saved['core']['coefficients']):
            raise ValueError('The complete actual core differs')
        n,m,k=len(y),len(x),len(p);h=np.diff(x)
        def bounded_jac(*args):
            try:return kwargs['fun_jac'](*args)
            finally:gc.collect()
        col,jac=blocks.prepare_sys(n,m,k,fun,bc,bounded_jac,kwargs['bc_jac'],x,h)
        cr,ym,ff,fm=col(y,p);br=bc(y[:,0],y[:,-1],p)
        physical_bc=float(np.max(abs(br[n:]*self.bcweights)))
        if physical_bc>context['actual_tail_tolerance']:
            raise ValueError('Accepted full-H true boundary residual does not reproduce')
        begin=time.monotonic();matrix=jac(y,p,ym,ff,fm,br);jac_seconds=time.monotonic()-begin
        begin=time.monotonic();factor=blocks.DirectBlockQRFactor(matrix,n,m,k);factor_seconds=time.monotonic()-begin
        del ym,ff,fm;gc.collect()
        print(json.dumps(dict(event='actual_fixed_control_factor',nodes=m,modes=self.M,
            jacobian_seconds=jac_seconds,factor_seconds=factor_seconds,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        parameter_units=np.r_[baseline_core[0],self.pscale]
        physical_units=np.r_[np.full(n*m,self.q),parameter_units]
        directions={};half_directions={};forcings_by_field={};rows=[];arrays=[]

        def backward_error(direction,forcing):
            ay=abs(direction[:n*m]).reshape(m,n);ap=abs(direction[n*m:]);scale=0.
            for lo in range(0,m-1,16):
                hi=min(lo+16,m-1)
                bound=(np.einsum('mij,mj->mi',abs(matrix.a[lo:hi]),ay[lo:hi])
                    +np.einsum('mij,mj->mi',abs(matrix.b[lo:hi]),ay[lo+1:hi+1])
                    +np.einsum('mik,k->mi',abs(matrix.c[lo:hi]),ap)
                    +abs(forcing[lo*n:hi*n]).reshape(hi-lo,n))
                scale=max(scale,float(bound.max()))
            scale=max(scale,float(np.max(abs(matrix.boundary_a)@ay[0]
                +abs(matrix.boundary_b)@ay[-1]+abs(matrix.boundary_p)@ap
                +abs(forcing[n*(m-1):]))),np.finfo(float).tiny)
            return float(np.max(abs(matrix.matvec(direction)+forcing))/scale)

        def residual_vector():
            residual,unused_mid,unused_f,unused_fm=col(y,p)
            return np.r_[residual.ravel(order='F'),bc(y[:,0],y[:,-1],p)]

        def reset(field=None,value=None):
            self.cfg=dict(baseline_cfg)
            if field is not None:self.cfg[field]=float(value)
            self._flow=None;self._flow_key=None;self._core_key=None;self._initial=None
            self.select(p)

        for field in fields:
            original=float(baseline_cfg[field]);width=2e-6*max(.1,abs(original));forcings=[]
            try:
                for step in (width,width/2):
                    reset(field,original+step);plus=residual_vector();reset();gc.collect()
                    reset(field,original-step);minus=residual_vector();reset();gc.collect()
                    forcings.append((plus-minus)/(2*step))
            finally:
                self.cfg=dict(baseline_cfg);self._flow=baseline_flow;self._flow_key='frozen'
                self._core_key=None;self._initial=None;self.select(p);self.initial(p);gc.collect()
            direction=-factor.solve(forcings[0]);half=-factor.solve(forcings[1])
            scaled=physical_units*direction;scaled_half=physical_units*half
            relative=float(np.max(abs(scaled-scaled_half))/max(np.max(abs(scaled)),np.finfo(float).tiny))
            residual_error=float(np.max(abs(matrix.matvec(direction)+forcings[0])))
            forcing_norm=max(float(np.max(abs(forcings[0]))),np.finfo(float).tiny)
            if relative>2e-4:raise ValueError('Physical-control half-step derivative did not stabilize: '+field)
            directions[field]=direction;half_directions[field]=half;forcings_by_field[field]=forcings[0]
            item=dict(field=field,width=width,half_width=width/2,
                half_step_response_relative_difference=relative,
                equation_error_over_forcing_norm=residual_error/forcing_norm,
                equation_relative_backward_error=backward_error(direction,forcings[0]),
                physical_core_derivative=(parameter_units*direction[n*m:]).tolist(),
                field_correction_derivative_max=float(np.max(abs(direction[:n*m]))*self.q))
            rows.append(item);arrays.append(save_array('external-'+field,direction))
            print(json.dumps(dict(event='actual_fixed_external_response',**item)),flush=True)
        Z=np.column_stack([directions[name] for name in primary])
        Zhalf=np.column_stack([half_directions[name] for name in primary])
        Fcontrols=np.column_stack([forcings_by_field[name] for name in primary])
        low=parameter_units[:3,None]*Z[n*m:n*m+3]
        low_half=parameter_units[:3,None]*Zhalf[n*m:n*m+3]
        singular=np.linalg.svd(low,compute_uv=False)
        if not singular[-1]>0:raise ValueError('Low-core/control exchange matrix is singular numerically')
        inverse=np.linalg.solve(low,np.eye(3))
        inverse_half=np.linalg.solve(low_half,np.eye(3))
        exchanged=[];exchange_directions={}
        for j,name in enumerate(('actual_q1','actual_q4','actual_c6')):
            direction=Z@inverse[:,j];exchange_directions[name]=direction
            alternate=Zhalf@inverse_half[:,j]
            core=parameter_units*direction[n*m:]
            target=np.eye(3)[:,j]
            half_difference=float(np.max(abs(physical_units*(direction-alternate)))/
                max(np.max(abs(physical_units*direction)),np.finfo(float).tiny))
            exchanged.append(dict(direction=name,physical_profile_derivative={a:float(b) for a,b in zip(primary,inverse[:,j])},
                core_derivative=core.tolist(),low_core_target_error=float(np.max(abs(core[:3]-target))),
                half_step_exchange_response_relative_difference=half_difference,
                equation_relative_backward_error=backward_error(direction,Fcontrols@inverse[:,j])))
            arrays.append(save_array('prescribed-'+name,direction))
        neutral=[]
        for field in fields:
            if field in primary:continue
            source=directions[field];du=-np.linalg.solve(low,parameter_units[:3]*source[n*m:n*m+3])
            combined=source+Z@du;core=parameter_units*combined[n*m:]
            alternate_source=half_directions[field]
            alternate_du=-np.linalg.solve(low_half,parameter_units[:3]*alternate_source[n*m:n*m+3])
            alternate=alternate_source+Zhalf@alternate_du
            neutral.append(dict(external_field=field,physical_profile_derivative={field:1.,**{a:float(b) for a,b in zip(primary,du)}},
                low_core_derivative_max=float(np.max(abs(core[:3]))),core_derivative=core.tolist(),
                half_step_combination_relative_difference=float(np.max(abs(physical_units*(combined-alternate)))/
                    max(np.max(abs(physical_units*combined)),np.finfo(float).tiny)),
                equation_relative_backward_error=backward_error(combined,forcings_by_field[field]+Fcontrols@du)))
            arrays.append(save_array('core-held-'+field,combined))
        result=dict(scope=__doc__,schema='fixed-actual-to-three-control-response-v1',finished=True,
            inspection_only=True,new_solution=False,tail_worker_started=False,
            input_identity=input_report,source_sha256=hashes,fields=list(fields),
            baseline=dict(profile=baseline_cfg,core=baseline_core.tolist(),gauge=self.q,
                numerical_reference_knots=self._neck_knots.tolist(),reference_coefficients=self.ref_coeff.tolist(),
                actual_physical_bc_max=physical_bc,accepted_rms_max=float(np.max(solution.rms_residuals)),
                raw_state_bitwise_equal=True),
            modes=self.M,angular=self.nt,nodes=m,external_responses=rows,
            physical_core_parameter_scales=parameter_units.tolist(),
            low_three_core_by_physical_control=low.tolist(),control_order=list(primary),
            half_step_low_three_core_by_physical_control=low_half.tolist(),
            low_exchange_condition=dict(singular_values=singular.tolist(),condition_2=float(singular[0]/singular[-1]),
                observed_half_step_matrix_perturbation_norm=float(np.linalg.norm(inverse@(low_half-low),ord=2)),
                scope='Only the physical 3x3 low-core/control response, not the condition of the global BVP Jacobian.'),
            prescribed_low_core_responses=exchanged,additional_core_held_directions=neutral,
            tangent_arrays=arrays,radial_batch_size=opts.radial_batch_size,collocation_batch_size=opts.collocation_batch_size,
            jacobian_seconds=jac_seconds,factor_seconds=factor_seconds,seconds=time.monotonic()-start,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,counters=counters.copy(),
            field_parameter_layout='Saved fixed-core layout. Tail entries of every tangent array are all-core parameter derivatives, not delta/LB/vp design offsets.',
            limitations=['The stored finite D-N derivative is used only at its exact complete H; it is not a new nonlinear tail solve.',
                'These are local derivatives; a finite step needs a new actual nonlinear coupled BVP and geometry audit.',
                'The old triple warm launcher cannot consume this all-core parameter layout without explicit conversion.'])
        output.write_text(json.dumps(result,indent=2)+'\n')
        raise RuntimeError('Actual fixed control response complete; no new BVP or worker requested')

    def loader(name,path):
        loaded=original_loader(name,path)
        if Path(path).name=='root_dual_core_bvp.py':
            original_main=loaded.main
            def entry():
                factory=loaded.make_dual
                def instrument(*args,**kwargs):
                    cls=factory(*args,**kwargs);cls.ensure_tail=guard;cls.solve_coupled=inspect;return cls
                loaded.make_dual=instrument
                return original_main()
            loaded.main=entry
        return loaded

    bounded.adapter.module=loader;sys.argv=[sys.argv[0]]+remaining
    try:
        bounded.main()
        if not output.exists() or not document(output).get('finished'):
            raise RuntimeError('The actual control response did not finish')
        if counters!={'inspections':1,'tail_start_attempts':0}:
            raise RuntimeError('The actual no-worker inspection path was not preserved')
    finally:
        bounded.adapter.module=original_loader
        for function,default in zip(functions,defaults):function.__defaults__=default


if __name__=='__main__':
    main()
