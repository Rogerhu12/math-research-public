#!/usr/bin/env python3
"""One immutable R684 finite-mean metric and its complete fixed-target J/J*.

A frozen target is a continuous-s formula of the named canonical R671
field, not an interpolated vector of old sampled means. Every target read
keeps its original finite angles, orbit weights and rho_star. Current mesh,
M, N and free field coefficients may change; current rho enters only the
current Gram. The fixed-target derivative contains no mean projection.

The numerical reader below materializes the fixed formula on an actual
nested observation plan. It records floating local-coordinate carriers;
continuous outward certificates must use the same exact symbolic formula.
No scientific work runs on import. Scientific readers require public Actions.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np

SCHEMA='R684-frozen-rotational-mean-metric-v1'
INPUT_ROLES=('bundle','node_report','scalar_input','observation_carrier','reference_carrier')
SOURCE_ROLES=('evaluator','factory','operator','observed','batch','scalar','integer','hold')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode('utf-8')).hexdigest()


def identity_payload(manifest):
    """Paths, bytes, provenance, certificates and the ID itself are excluded."""
    return dict(schema=manifest['schema'],averaging=manifest['averaging'],
        full_angles=manifest['full_angles'],
        canonical_model_identity_sha256=manifest['canonical_model_identity_sha256'],
        inputs={role:record['sha256'] for role,record in manifest['inputs'].items()},
        sources={role:record['sha256'] for role,record in manifest['sources'].items()},
        domain=manifest['domain'],cap_recipe=manifest['cap_recipe'],
        mean_definition=manifest['mean_definition'])


def target_identity(manifest):
    if canonical_sha(manifest['canonical_model'])!=manifest['canonical_model_identity_sha256']:
        raise ValueError('The frozen canonical model does not match its stated identity')
    return canonical_sha(identity_payload(manifest))


def mean_definition(averaging):
    if averaging not in ('physical','material'):
        raise ValueError('Need an explicit finite mean convention')
    return dict(angle_formula='phi_j=2*pi*j/N_star, j=0,...,N_star-1',
        diagonal_components=['|F_star,s|^2','|F_star,phi|^2/rho_star^2'],
        off_diagonal='zero by exact full-circle reflection parity',
        average_formula=('sum_j component_j/N_star' if averaging=='physical'
            else 'sum_j rho_star,j*component_j/sum_j rho_star,j'),
        radial_rule='Frozen canonical shared quintic on exact symbolic nodes plus its analytic R671 f/h/k, evaluated at every s; no interpolated mean array')


def cap_recipe():
    return dict(schema='R661-fixed-p4-graphs-v1',a='3/20',
        radii=['1/25','9/200','1/20','11/200'],height='1/1000',
        upper_centers_xy=[['3/20','0'],['0','3/20'],['-3/20','0']],
        lower_centers_xy=[['0','0']],
        graph='h*(1-|x-c_xy|^2/b^2)_+^4 along each cap outward normal',
        metric_rule='own induced graph metric; height translation independent')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Frozen metric scientific work requires Rogerhu12/math-research-public Actions')


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def file_record(path,repo=None):
    path=Path(path).resolve()
    result=dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)
    if repo is not None:
        repo=Path(repo).resolve()
        def bind(root,relative):
            commit=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
            committed=subprocess.check_output(['git','-C',str(root),'show',commit+':'+str(relative)],
                stderr=subprocess.DEVNULL)
            if hashlib.sha256(committed).hexdigest()!=result['sha256']:
                raise ValueError('The executed frozen source differs from its recorded commit')
            result['repo_relative_path']=str(relative)
            result['source_commit']=commit
        origin_root=None
        try:
            origin_root=Path(subprocess.check_output(
                ['git','-C',str(path.parent),'rev-parse','--show-toplevel'],
                text=True,stderr=subprocess.DEVNULL).strip()).resolve()
            bind(origin_root,path.relative_to(origin_root))
        except (subprocess.CalledProcessError,ValueError):
            # Frozen followup sources may have been copied without a .git.
            # A known repository suffix is accepted only after byte binding.
            parts=path.parts
            possible=[]
            if 'topics' in parts:
                possible.append(Path(*parts[parts.index('topics'):]))
            try:possible.append(path.relative_to(repo))
            except ValueError:pass
            for relative in possible:
                candidate=repo/relative
                if candidate.is_file() and sha(candidate)==result['sha256']:
                    bind(repo,relative)
                    break
            if 'repo_relative_path' not in result:
                raise ValueError('Cannot bind this frozen source to a repository-relative same-byte file: '+str(path))
    return result


def read_manifest(path):
    manifest=json.loads(Path(path).read_text())
    if manifest.get('schema')!=SCHEMA or manifest.get('frozen') is not True:
        raise ValueError('Need one explicitly frozen R684 target manifest')
    if set(manifest['inputs'])!=set(INPUT_ROLES) or set(manifest['sources'])!=set(SOURCE_ROLES):
        raise ValueError('All frozen field and target-source roles must be explicit')
    N=manifest['full_angles']
    if isinstance(N,bool) or not isinstance(N,int) or N<4 or N%4:
        raise ValueError('The frozen finite full-angle grid must have positive quarter orbits')
    if manifest['mean_definition']!=mean_definition(manifest['averaging']):
        raise ValueError('The frozen finite-mean definition changed')
    if manifest['cap_recipe']!=cap_recipe():
        raise ValueError('This target uses the explicit R661 p4 marker cap metric')
    if target_identity(manifest)!=manifest['target_identity_sha256']:
        raise ValueError('The full frozen target identity changed')
    return manifest


def resolve_record(record,repo=None,override=None):
    if override is not None:path=Path(override).resolve()
    elif repo is not None and 'repo_relative_path' in record:
        path=Path(repo).resolve()/record['repo_relative_path']
    else:path=Path(record['path']).resolve()
    if sha(path)!=record['sha256']:
        raise ValueError('Frozen input/source bytes changed: '+str(path))
    return path


def resolve_report_source(path,expected_sha,repo):
    """Recover an old detached-worktree source only by exact public bytes."""
    original=Path(path).resolve()
    candidates=[original]
    if 'topics' in original.parts:
        candidates.append(Path(repo).resolve()/Path(*original.parts[original.parts.index('topics'):]))
    for candidate in candidates:
        if candidate.is_file() and sha(candidate)==expected_sha:
            return candidate
    raise ValueError('The exact reported source is absent; restore its pinned repository commit: '+str(original))


class FrozenMeanMetricTarget:
    """Actual frozen field + continuous radial formula; no current-field means."""
    def __init__(self,manifest_path,*,repo,input_overrides=None,source_overrides=None,stage_block=64):
        require_actions()
        self.manifest_path=Path(manifest_path).resolve()
        self.manifest=read_manifest(self.manifest_path)
        self.manifest_sha256=sha(self.manifest_path)
        self.identity=self.manifest['target_identity_sha256']
        self.averaging=self.manifest['averaging']
        self.full_angles=self.manifest['full_angles']
        input_overrides={} if input_overrides is None else input_overrides
        source_overrides={} if source_overrides is None else source_overrides
        self.inputs={key:resolve_record(value,override=input_overrides.get(key))
            for key,value in self.manifest['inputs'].items()}
        self.sources={key:resolve_record(value,repo=repo,override=source_overrides.get(key))
            for key,value in self.manifest['sources'].items()}
        if self.sources['evaluator']!=Path(__file__).resolve() and sha(__file__)!=self.manifest['sources']['evaluator']['sha256']:
            raise ValueError('The frozen evaluator implementation changed')
        self.factory=load('frozen_metric_reference_factory',self.sources['factory'])
        model=self.manifest['canonical_model']
        self.context=self.factory.TailLiftContext.from_files(bundle=self.inputs['bundle'],
            carrier=self.inputs['observation_carrier'],node_report=self.inputs['node_report'],
            scalar_input=self.inputs['scalar_input'],scalar_source=self.sources['scalar'],
            integer_source=self.sources['integer'],hold_source=self.sources['hold'],
            observed_source=self.sources['observed'],eta_start_node=model['eta_start_node'],
            lambda_value=model['lambda_value'])
        self.problem,_=self.context.create_pair(self.sources['operator'],self.sources['batch'],
            N=self.full_angles,stage_block=stage_block,quarter=True)
        self.x,_=self.problem.pack(self.context.data['qjets'],float(self.context.data['Hcap']),require_affine=True)
        self.x,_=self.context.transfer_seed(self.problem,self.x,
            source_lambda=model['lambda_value'],mode='keep-q')
        if self.context.definition()!=model:
            raise ValueError('Rebuilt frozen target is not its literal canonical model')
        self._compatible(self.problem)
        self.x.setflags(write=False)
        self.prepared=self.problem.prepare(self.x)
        if not np.isfinite(self.prepared.rho).all() or np.any(self.prepared.rho<=0):
            raise ValueError('The frozen finite target angles need positive material density')
        m=self.problem.multiplicity
        self.weights=(m/m.sum() if self.averaging=='physical'
            else m*self.prepared.rho/np.sum(m*self.prepared.rho))
        self.weights.setflags(write=False)
        self._known_profiles={(int(cell),float(u).hex()):self.problem.lift_scalar9[j]
            for j,(cell,u) in enumerate(zip(self.problem.observation_cells,self.problem.observation_u))}
        self.last_materialization=None

    def _compatible(self,current):
        context=current.reference_tail_context
        wanted=self.manifest['canonical_model']
        model=context.definition()
        for key in ('source_sha256','lambda_value','eta_start_symbolic','eta_end_symbolic',
                'scalar_input_sha256','source_sha256s','operator_source_sha256s'):
            if model[key]!=wanted[key]:
                raise ValueError('Current field changes the fixed scalar/profile source or physical eta: '+key)
        if (float(current.S).hex()!=self.manifest['domain']['S_carrier_hex']
                or float(current.R).hex()!=self.manifest['domain']['R_carrier_hex']
                or float(current.width).hex()!=self.manifest['domain']['width_hex']
                or [float(v).hex() for v in context.data['fixed_core_first3']]
                    !=self.manifest['domain']['fixed_core_first3_hex']):
            raise ValueError('Current field changes fixed S/R/width/core datum')
        return context

    @staticmethod
    def _affine_parameter(point,left,right):
        diff=(right[0]-left[0],right[1]-left[1])
        index=0 if diff[0]!=0 else 1
        if diff[index]==0:
            raise ValueError('Frozen exact symbolic cell has coincident endpoints')
        t=(point[index]-left[index])/diff[index]
        if any(point[k]-left[k]!=t*diff[k] for k in (0,1)) or not 0<=t<=1:
            raise ValueError('This numerical reader requires an exact nested refinement of the frozen mesh')
        return t

    def locations_for_operator(self,current):
        """Map the new exact affine plan into frozen cells before rounding u."""
        context=self._compatible(current)
        frozen=self.context
        intervals=[]
        for j,(left,right) in enumerate(zip(context.nodes[:-1],context.nodes[1:])):
            middle=float(current.mesh[j]+(current.mesh[j+1]-current.mesh[j])/2)
            cell=min(len(frozen.nodes)-2,max(0,int(np.searchsorted(frozen.mesh,middle,side='right')-1)))
            a,b=frozen.nodes[cell:cell+2]
            lo=self._affine_parameter(left,a,b)
            hi=self._affine_parameter(right,a,b)
            if not lo<hi:
                raise ValueError('Refined exact radial orientation changed')
            intervals.append((cell,lo,hi))
        cells=np.empty(current.P,dtype=np.int64)
        local=np.empty(current.P,dtype=float)
        maximum_error=Fraction(0)
        rounded=0
        for j,(newcell,u) in enumerate(zip(current.observation_cells,current.observation_u)):
            cell,lo,hi=intervals[int(newcell)]
            exact=lo+(hi-lo)*Fraction(float(u))
            value=float(exact)
            difference=abs(Fraction(value)-exact)
            maximum_error=max(maximum_error,difference)
            rounded+=bool(difference)
            cells[j],local[j]=cell,value
        info=dict(current_rows=int(current.P),frozen_full_angles=self.full_angles,
            exact_nested_symbolic_cell_mapping=True,
            rounded_local_coordinate_count=rounded,
            maximum_local_u_rounding_error_exact=str(maximum_error),
            numerical_materialization_outward=False,
            target_formula_redefined_from_current_field=False,
            old_mean_arrays_interpolated=False)
        return cells,local,info

    def evaluate_locations(self,cells,local,*,stage_block=64):
        """Numerical evaluation of the SAME full frozen formula at requested s."""
        require_actions()
        cells=np.asarray(cells,dtype=np.int64)
        local=np.asarray(local,dtype=float)
        if cells.shape!=local.shape or cells.ndim!=1:
            raise ValueError('Need matching frozen-cell and local-coordinate vectors')
        if (np.any(cells<0) or np.any(cells>=self.problem.J-1)
                or not np.isfinite(local).all() or np.any(local<0) or np.any(local>1)):
            raise ValueError('A requested target point leaves the frozen radial domain')
        q,p=self.problem,self.prepared
        E=np.empty(len(cells));C=np.empty(len(cells))
        for start in range(0,len(cells),int(stage_block)):
            stop=min(len(cells),start+int(stage_block))
            y=np.empty((stop-start,q.n));v=np.empty_like(y)
            lift=np.empty((stop-start,9))
            for k,(cell,u) in enumerate(zip(cells[start:stop],local[start:stop])):
                h=q.mesh[cell+1]-q.mesh[cell]
                weights=self.context.observed.hermite_weights(h,float(u))
                values=weights@p.jets[cell:cell+2].reshape(6,q.n)
                y[k],v[k]=values[:2]
                known=self._known_profiles.get((int(cell),float(u).hex()))
                lift[k]=q.lift_at(int(cell),float(u)) if known is None else known
            V,T=q._linear_fields(y,v)
            V+=lift[:,4,None,None]*p.er[None]
            V[:,:,2]+=lift[:,1,None]*p.height+lift[:,7,None]
            T+=lift[:,3,None,None]*p.rho[None,:,None]*p.et[None]
            E[start:stop]=np.einsum('sac,sac->sa',V,V)@self.weights
            C[start:stop]=(np.einsum('sac,sac->sa',T,T)/p.rho[None,:]**2)@self.weights
        if (not np.isfinite(E).all() or not np.isfinite(C).all()
                or np.any(E<=0) or np.any(C<=0)):
            raise ValueError('Frozen target positivity failed at a materialized radial row')
        return E,C

    def evaluate_for_operator(self,current,*,stage_block=64):
        cells,local,info=self.locations_for_operator(current)
        E,C=self.evaluate_locations(cells,local,stage_block=stage_block)
        info.update(target_identity_sha256=self.identity,
            target_manifest_sha256=self.manifest_sha256,
            E_min=float(E.min()),E_max=float(E.max()),C_min=float(C.min()),C_max=float(C.max()),
            frozen_rho_retained=True,current_angle_grid_does_not_change_target=True)
        self.last_materialization=info
        return E,C,info


class FixedMetricTransform:
    def __init__(self,raw,radial,angular):
        self.raw=np.asarray(raw)
        self.radial,self.angular=np.asarray(radial),np.asarray(angular)
        if (self.raw.ndim!=3 or self.raw.shape[-1]!=3
                or self.radial.shape!=self.raw.shape[:1] or self.angular.shape!=self.radial.shape):
            raise ValueError('Need all current Gram rows and one fixed positive diagonal per radial row')
        self.scale=np.stack((1/self.radial,1/np.sqrt(self.radial*self.angular),1/self.angular),axis=-1)
        self.result=self.raw*self.scale[:,None,:]
        self.result[...,0]+=1/self.radial[:,None]-1
        self.result[...,2]+=1/self.angular[:,None]-1

    def apply(self,direction):
        return np.asarray(direction)*self.scale[:,None,:]

    def transpose(self,cotangent):
        return self.apply(cotangent)


class FrozenMetricOperator:
    """Fixed target scaling only: every original residual mean is constrained."""
    def __init__(self,original_operator,target,*,stage_block=64):
        require_actions()
        self.original_operator,self.target=original_operator,target
        self.averaging=target.averaging
        E,C,metadata=target.evaluate_for_operator(original_operator,stage_block=stage_block)
        self.fixed_radial=E
        self.fixed_angular=C/original_operator.a**2
        if np.any(self.fixed_radial<=0) or np.any(self.fixed_angular<=0):
            raise ValueError('The same frozen target must remain positive on the current plan')
        self.fixed_scale=np.stack((1/self.fixed_radial,
            1/np.sqrt(self.fixed_radial*self.fixed_angular),1/self.fixed_angular),axis=-1)
        self.target_materialization=metadata
        for value in (self.fixed_radial,self.fixed_angular,self.fixed_scale):value.setflags(write=False)
        self._base_x=self._base_state=None

    def __getattr__(self,name):
        return getattr(self.original_operator,name)

    def _state(self,x):
        x=np.asarray(x)
        if (self._base_x is not None and x.shape==self._base_x.shape
                and x.dtype==self._base_x.dtype and np.array_equal(x,self._base_x)):
            return self._base_state
        return FixedMetricTransform(self.original_operator.raw_residual(x),self.fixed_radial,self.fixed_angular)

    def set_base(self,x):
        record=self.original_operator.set_base(x)
        self._base_x=np.array(x,copy=True)
        self._base_x.setflags(write=False)
        self._base_state=FixedMetricTransform(self.original_operator.raw_residual(x),self.fixed_radial,self.fixed_angular)
        return dict(record,fixed_target_identity=self.target.identity,moving_mean_projection=False,
            fixed_final_metric=True,all_original_mean_constraints_retained=True)

    def clear_base(self):
        self.original_operator.clear_base()
        self._base_x=self._base_state=None

    def raw_residual(self,x):
        return self._state(x).result.copy()

    def residual(self,x):
        return self.raw_residual(x)*self.sqrt_multiplicity[None,:,None]

    def jvp(self,x,direction):
        return self.original_operator.jvp(x,direction)*self.fixed_scale[:,None,:]

    def vjp(self,x,weights):
        weights=np.asarray(weights).reshape(self.P,self.N,3)
        return self.original_operator.vjp(x,weights*self.fixed_scale[:,None,:])

    def observation_metadata(self):
        return dict(self.original_operator.observation_metadata(),
            fixed_target_identity=self.target.identity,frozen_full_angles=self.target.full_angles,
            current_full_angles=self.full_N,fixed_final_metric=True,
            moving_mean_projection=False,target_materialization=self.target_materialization,
            all_original_mean_constraints_retained=True)


def freeze_report(*,repo,report_path,bundle_path,out,averaging=None,full_angles=None):
    require_actions()
    repo=Path(repo).resolve();report_path=Path(report_path).resolve()
    bundle_path=Path(bundle_path).resolve();out=Path(out).resolve()
    if out.exists():raise FileExistsError('Never overwrite a frozen target manifest')
    report=json.loads(report_path.read_text())
    if report.get('complete') is not True or report.get('final_bundle_sha256')!=sha(bundle_path):
        raise ValueError('Freeze only the actual completed report final bundle')
    design=report.get('mean_metric_design') or {}
    averaging=averaging or design.get('averaging')
    full_angles=int(full_angles or design.get('finite_angles') or report['N'])
    if averaging not in ('physical','material') or full_angles<4 or full_angles%4:
        raise ValueError('State the exact finite average and a positive full quarter grid')
    if design and (averaging!=design['averaging'] or full_angles!=design['finite_angles']):
        raise ValueError('Freeze the actual designed finite target without silently changing its average')
    context=report.get('exact_tail_context_final') or report['exact_tail_context']
    model=context['definition']
    if canonical_sha(model)!=context['model_identity_sha256']:
        raise ValueError('The actual parent canonical model identity is inconsistent')
    paths=report['source_paths']
    sources=dict(evaluator=Path(__file__).resolve(),factory=paths['exact_tail'],operator=paths['operator'],
        observed=paths['implementation'],batch=paths['base_batch'],scalar=paths['tail_scalar'],
        integer=paths['tail_integer'],hold=paths['tail_hold'])
    inputs=dict(bundle=bundle_path,node_report=report['exact_tail_node_report'],
        scalar_input=report['exact_tail_scalar_input'],observation_carrier=report['observation_carrier'],
        reference_carrier=report['exact_tail_profile_carrier'])
    expected_inputs=dict(bundle=report['final_bundle_sha256'],node_report=report['exact_tail_node_report_sha256'],
        scalar_input=report['exact_tail_scalar_input_sha256'],observation_carrier=report['observation_carrier_sha256'],
        reference_carrier=report['exact_tail_profile_carrier_sha256'])
    records={role:file_record(path) for role,path in inputs.items()}
    for role,value in records.items():
        if value['sha256']!=expected_inputs[role]:raise ValueError('An actual frozen input changed: '+role)
    source_role_map=dict(factory='exact_tail',operator='operator',observed='implementation',batch='base_batch',
        scalar='tail_scalar',integer='tail_integer',hold='tail_hold')
    source_records={'evaluator':file_record(sources['evaluator'],repo)}
    for role,report_role in source_role_map.items():
        expected=report['source_sha256_by_role'][report_role]
        actual=resolve_report_source(sources[role],expected,repo)
        source_records[role]=file_record(actual,repo)
        source_records[role]['executed_parent_source_path']=str(sources[role])
    with np.load(bundle_path,allow_pickle=False) as data:
        domain=dict(S_carrier_hex=float(data['mesh'][-1]).hex(),R_carrier_hex=float(data['radius']).hex(),
            width_hex=float(data['width']).hex(),
            fixed_core_first3_hex=[float(v).hex() for v in data['fixed_core_first3']],
            eta_left_affine=model['eta_start_symbolic'],eta_right_affine=model['eta_end_symbolic'],
            scalar_rule='original FullHold S/R from the bound scalar_input, scalar, integer and hold sources')
        actual_model=json.loads(str(data['reference_tail_model_json'].item()))
    if actual_model!=model:raise ValueError('The literal frozen bundle canonical model changed')
    current=report.get('final_statistics') or report.get('current') or report['initial']
    manifest=dict(schema=SCHEMA,averaging=averaging,full_angles=full_angles,inputs=records,
        sources=source_records,canonical_model=model,
        canonical_model_identity_sha256=context['model_identity_sha256'],domain=domain,
        mean_definition=mean_definition(averaging),cap_recipe=cap_recipe(),frozen=True,
        target_defined_on_every_radial_point=True,old_sampled_mean_interpolation=False,
        continuous_positivity_certified=False,complete_problem_certified=False,
        provenance=dict(freeze_source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
            github_run_id=os.environ.get('GITHUB_RUN_ID'),workflow_trigger_commit=os.environ.get('GITHUB_SHA'),
            candidate_report=file_record(report_path),candidate_source_commit=report.get('source_commit'),
            candidate_driver_sha256=report['source_sha256'],
            candidate_sampled_design_metric_error=current.get('max_relative_gram'),
            candidate_metric_error_is_continuous_certificate=False),
        scope='One fixed continuous radial metric formula plus the fixed own-induced R661 cap metric. Rebuild its named frozen field exactly; never recompute target means from a refinement candidate or change N_star.')
    manifest['target_identity_sha256']=target_identity(manifest)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(manifest,indent=2,allow_nan=False)+'\n')
    return manifest


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    parser.add_argument('--bundle',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--averaging',choices=('physical','material'))
    parser.add_argument('--full-angles',type=int)
    args=parser.parse_args()
    value=freeze_report(repo=args.repo,report_path=args.report,bundle_path=args.bundle,out=args.out,
        averaging=args.averaging,full_angles=args.full_angles)
    print(json.dumps(dict(manifest=str(args.out.resolve()),manifest_sha256=sha(args.out),
        target_identity_sha256=value['target_identity_sha256'],averaging=value['averaging'],
        full_angles=value['full_angles'],frozen=value['frozen'],
        continuous_positivity_certified=False,complete_problem_certified=False)),flush=True)


if __name__=='__main__':main()
