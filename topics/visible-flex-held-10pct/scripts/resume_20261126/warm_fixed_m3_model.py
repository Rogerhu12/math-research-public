#!/usr/bin/env python3
"""Read-only reconstruction of a warm supported-phase, frozen-metric BVP.

The origin is an actual accepted R53 run. Its complete support vector is
frozen once. Lambda can vary for design continuation with the same metric;
only runs at one fixed lambda can be used for refinement of one problem.
The p0 coordinate is log(q_aux/gauge_q), with d_j=phase_scale*p_j for all j.
q_aux is not a support amplitude and never multiplies the field Y.
"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
SCRIPTS=HERE.parent
KIND="warm-supported-material-phase-fixed-metric"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def option(record,name):
    return record['command'][record['command'].index(name)+1]


def original_source_signature(record):
    result={}
    for path,expected in record.get('source_hashes',{}).items():
        if sha(path)!=expected:
            raise ValueError('Original numerical source changed: '+path)
        name=Path(path).name
        if name in result and result[name]!=expected:
            raise ValueError('Ambiguous original source basename: '+name)
        result[name]=expected
    for flag in ('--core-module','--core-config'):
        if flag in record['command']:
            path=option(record,flag)
            actual=sha(path)
            expected=record.get('inputs',{}).get(str(Path(path).resolve()))
            if expected is not None and actual!=expected:
                raise ValueError('Original core input changed: '+path)
            result[flag]=actual
    return result


def embed(value,old_m,new_m):
    value=np.asarray(value)
    if new_m<old_m or value.shape[0]!=3*old_m+1:
        raise ValueError('Invalid Fourier mode transfer')
    out=np.zeros((3*new_m+1,)+value.shape[1:],dtype=value.dtype)
    out[0]=value[0]
    for i,j in ((1,1),(old_m+1,new_m+1),(2*old_m+1,2*new_m+1)):
        out[j:j+old_m]=value[i:i+old_m]
    return out


def lift_weight(flow,s):
    radius=flow.profile(s)[0]
    z=np.clip((s-.5*flow.prefix_end)/(.4*flow.prefix_end),0.,1.)
    return radius*(1-z**3*(10-15*z+6*z*z))


def bootstrap(origin_path):
    origin_path=Path(origin_path).resolve()
    origin=load(origin_path)
    signature=original_source_signature(origin)
    adapter=module('_warm_original_geometry',SCRIPTS/'resume_m3/actual_m3_metric_model.py')
    design=adapter.load_model(dict(source_run=str(origin_path)))
    raw=origin_path.parent/origin['raw_return']['file']
    if sha(raw)!=origin['raw_return']['sha256']:
        raise ValueError('Original accepted raw field changed')
    with np.load(raw,allow_pickle=False) as data:
        p=data['p'].copy()
    design.initial(p)
    if not hasattr(design._core,'original') or not hasattr(design._core.original,'normal_geometry'):
        raise ValueError('The warm anchor must be a positive-lambda R53 support core')
    return design,origin,signature,p


def build_model(design,origin,record,*,anchor_baseline=None):
    definition=record['warm_definition']
    if (definition['anchor_core_settings']!=origin['core_settings'] or
            not np.array_equal(definition['anchor_support_coefficients'],
                               design._core.original.coefficients)):
        raise ValueError('The complete anchor support or its source settings changed')
    if record['frozen_profile']!=origin['frozen_profile']:
        raise ValueError('The actual original metric is not the frozen branch metric')
    if record['mean_nodes']!=1168 or record['bc_normalization']!=.02:
        raise ValueError('The declared mean1168/BC normalization changed')
    if (definition['anchor_run_sha256']!=record['origin_design_sha256'] or
            Path(definition['anchor_run']).resolve()!=Path(record['origin_design_run']).resolve()):
        raise ValueError('The saved anchor identity changed')
    if definition['gauge_q']!=record['gauge_q']:
        raise ValueError('Auxiliary coordinate carrier and fixed gauge differ')
    if origin['gauge_q']!=record['gauge_q'] or origin['angular_chart']!=record['angular_chart']:
        raise ValueError('Changing the gauge or material chart is not this branch')
    provider=module('_warm_supported_provider',HERE/'warm_supported_core_factory.py')
    if record.get('warm_provider_sha256')!=sha(HERE/'warm_supported_core_factory.py'):
        raise ValueError('The warm core provider changed')
    ref=type(design._core.original)
    factory=provider.make_factory(definition,reference_class=ref,
                                  anchor_baseline=anchor_baseline)
    __import__('fixed_metric_mode3_core').PlanarSupportCore=factory
    __import__('fixed_metric_mode3_bvp').PlanarSupportCore=factory
    # The old initial() captures its factory in a closure. Construct new
    # classes after installation; the live old model remains unchanged.
    coupler=sys.modules['_metric_coupler']
    Flow,Base=coupler.adaptive.build_classes(record['angular_chart'])
    sys.path.insert(0,str(SCRIPTS/'resume_m3/round_raw_lib'))
    from exact_core_lift import install_core_lift
    import analytic_adaptive_core_jac as analytic
    Base=install_core_lift(Flow,Base)
    analytic.parameter_jets=lambda core,theta:core.jet_parameter_derivatives(theta)
    analytic.install(Base)
    port_path=Path(record['linear_port_path'])
    port=load(port_path)
    if sha(port_path)!=record['linear_port_sha256']:
        raise ValueError('The numerical port bytes changed')
    port['cut']['_prefix_bridge']=record['frozen_profile']['prefix_bridge']
    port['_sha256']=sha(port_path)
    if (port['parameters']!=record['physical_tail_parameters'] or
            port['cut']!=record['physical_tail_cut']):
        raise ValueError('The physical tail metric changed')
    obj=Base(copy.deepcopy(record['frozen_profile']),port,float(record['gauge_q']),
             int(record['modes']),int(record['angular']),True,float(record['warp_reference']))
    obj.bcweights=np.full(obj.M,float(record['bc_normalization']))
    obj.relative_metric_loader_record=dict(
        model_kind=KIND,fixed_metric=True,fixed_core=False,
        parameter_zero_meaning='log(q_aux/gauge_q)',
        mean_nodes=record['mean_nodes'],bvp_or_tail_solver_invoked=False,
        complete_surface=False)
    return obj


def load_model(config):
    path=Path(config['source_run']).resolve()
    record=load(path)
    if record.get('model_kind')!=KIND or not record.get('fixed_metric'):
        raise ValueError('Expected a declared warm supported-phase fixed-metric run')
    if record.get('parameter_zero_meaning')!='log(q_aux/gauge_q)':
        raise ValueError('Ambiguous auxiliary parameter semantics')
    if record.get('terminal_kind')!='original_linear_dn':
        raise ValueError('This loader has no actual nonlinear DN attached')
    origin=Path(record['origin_design_run'])
    if sha(origin)!=record['origin_design_sha256']:
        raise ValueError('The accepted original run changed')
    design,original,signature,_=bootstrap(origin)
    if signature!=record['frozen_source_signature']:
        raise ValueError('The numerical original source changed')
    return build_model(design,original,record)
