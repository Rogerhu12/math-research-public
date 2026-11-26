#!/usr/bin/env python3
"""Use the explicit nested actual warm solve with a full coupled-M12 right preconditioner.

Only the linear right-coordinate map and its physical-gradient inverse
change. The frozen nested core still supplies the real same-g field, all
three Gram rows, trial acceptance, independent observers and endpoint
checks. This entry does not prepare a grid or change the input field.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,sys
from pathlib import Path

CORE_NAME='6a65-m12-entire-half-nested-warm-refinement.py'
CORE_SHA='39f4b31bcf50123cd9cb6ce69db8415c9ed28e0999c568f579439c01d7a88899'
NORMAL_NAME='6a65-m12-complete-gram-normal-preconditioner.py'
NORMAL_SHA='f19a09b0d4efbb9f6f8122de446f371306d291dfa47cf0dfeb7727fe0e0b18f9'
GENERIC_NAME='6a65-cartesian-complete-radial-normal.py'
GENERIC_SHA='1fdaa80e4a56631c858c1a0f4f31557ec8a72254170b6b1df4ec16cbe6437361'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def argument(args,name):
    indices=[i for i,value in enumerate(args) if value==name]
    if len(indices)!=1 or indices[0]+1==len(args):raise ValueError('Exactly one '+name+' value required')
    return args[indices[0]+1]

def main():
    ap=argparse.ArgumentParser(description=__doc__,add_help=False)
    ap.add_argument('--preconditioner-eta',type=float,default=1e-6)
    ap.add_argument('--normal-assembly-block',type=int,default=8)
    ap.add_argument('--full-normal-source',type=Path)
    args,core_args=ap.parse_known_args()
    if not core_args or core_args[0]!='solve':raise ValueError('This adapter only consumes the complete actual warm solve')
    if not math.isfinite(args.preconditioner_eta) or args.preconditioner_eta<=0 or args.normal_assembly_block<1:
        raise ValueError('Explicit positive finite preconditioner eta/block required')
    scripts=Path(argument(core_args,'--scripts')).resolve();out=Path(argument(core_args,'--out'))
    if out.exists() or Path(str(out)+'.warm-observed.json').exists():raise FileExistsError('Fresh actual output paths required')
    core_path=scripts/CORE_NAME;generic_path=scripts/GENERIC_NAME
    normal_path=args.full_normal_source or scripts/NORMAL_NAME
    for path,expected in [(core_path,CORE_SHA),(normal_path,NORMAL_SHA),(generic_path,GENERIC_SHA)]:
        if sha(path)!=expected:raise ValueError('Pinned actual numerical dependency changed: '+str(path))
    core=load('M12_frozen_nested_warm_core',core_path);normal=load('M12_full_Gram_normal_adapter',normal_path)
    original_load=core.load;original_lsmr=core.lsmr;assemblies=[]
    source_chain={'execution_adapter_sha256':sha(__file__),'frozen_nested_core_sha256':sha(core_path),
                  'complete_M12_normal_source_sha256':sha(normal_path),'R244_generic_helper_sha256':sha(generic_path)}
    print(json.dumps({'actual_source_chain':source_chain,'preconditioner_eta':args.preconditioner_eta,
                      'physical_objective_lambda':0.,'required_LSMR_damp':0.,
                      'same_actual_warm_input_and_complete_trial_observers':True}),flush=True)

    def actual_load(name,path):
        module=original_load(name,path)
        if Path(path).name=='6a65-m12-global-common-cut-position-recovered.py':
            original_factory=module.stream.StreamingLinearized
            def factory(*a,**kw):
                linear=original_factory(*a,**kw)
                wrapped=normal.CompleteGramRightPreconditioned(linear,args.preconditioner_eta,
                    generic_path,args.normal_assembly_block)
                # Existing matvec/rmatvec call these instance methods. Their
                # physical three-row formulae and all cached point data stay.
                linear.unpack=wrapped.unpack
                linear.transpose_precondition=wrapped.blocks.transpose
                linear._actual_M12_full_normal=wrapped
                assemblies.append(wrapped.receipt)
                print(json.dumps({'actual_full_normal_assembly':wrapped.receipt}),flush=True)
                return linear
            module.stream.StreamingLinearized=factory
        return module

    def actual_physical_gradient(op,value):
        if not hasattr(op,'_actual_M12_full_normal'):
            raise ValueError('Full-normal physical-gradient recovery requires its actual preconditioner')
        return op._actual_M12_full_normal.blocks.physical_gradient(value)

    def unregularized_lsmr(*a,**kw):
        if kw.get('damp',0.)!=0.:raise ValueError('The original M12 physical objective has lambda=0')
        kw['damp']=0.
        return original_lsmr(*a,**kw)

    core.load=actual_load
    core.physical_gradient_from_old_coordinates=actual_physical_gradient
    core.lsmr=unregularized_lsmr
    sys.argv=[str(core_path),*core_args]
    core.main()
    result=json.loads(out.read_text())
    if len(assemblies)!=len(result.get('rows',[])):
        raise ValueError('Every actual Newton row must bind one full normal assembly')
    warm_path=Path(str(out)+'.warm-observed.json');warm=json.loads(warm_path.read_text())
    warm['frozen_core_script_sha256']=warm['script_sha256'];warm['script_sha256']=sha(__file__)
    warm['actual_execution_source_chain']=source_chain
    warm['linear_preconditioner_does_not_change_initial_field']=True
    warm_path.write_text(json.dumps(warm,indent=2,allow_nan=False)+'\n')
    result['frozen_core_script_sha256']=result['script_sha256'];result['script_sha256']=sha(__file__)
    result['warm_observed_result_sha256']=sha(warm_path)
    result['actual_execution_source_chain']=source_chain
    result['actual_linear_preconditioner']='complete coupled-planar M12 H + eta original H1, right coordinates only'
    result['preconditioner_eta']=args.preconditioner_eta
    result['physical_objective_lambda']=0.;result['required_LSMR_damp']=0.
    result['actual_full_normal_assemblies']=assemblies
    result['original_full_physical_problem_and_acceptance_unchanged']=True
    result['positive_uniform_lambda_zero_spectrum_bound_claimed']=False
    out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'actual_full_normal_warm_result':str(out),'sha256':sha(out),
                      'field_sha256':result['field_sha256'],'accepted_steps':result['accepted_steps_this_refinement'],
                      'independent_after':result['independent_observer_after'],
                      'actual_execution_source_chain':source_chain},allow_nan=False),flush=True)

if __name__=='__main__':main()
