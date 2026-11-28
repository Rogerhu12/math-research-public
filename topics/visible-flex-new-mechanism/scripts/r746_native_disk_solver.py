"""Run the frozen R743 columns and physical checks with the R746 planar seed."""
import builtins
import hashlib
import importlib.util
import os
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace


HERE = Path(__file__).resolve().parent
PINS = {
    'r743_early_material_disk.py': '9513d8fb67459f4338bf494be0d88a07b848ed6da98cd9975fbac523b5d9ca0c',
    'r743_native_disk_solver.py': 'a83c42cdbeded98836e539fdb98664475b2798e4919511a39f9d78328e766f18',
    'r742_native_tsqr.py': 'd9565b37ad9e3b8d70df7adf0aa1b82015fd66edadcd6386923c1a1197f2b729',
}


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY','').lower() != 'rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID','').isdigit()):
        raise SystemExit('R746 requires the public research Actions runner')
    for name,sha in PINS.items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest() != sha:
            raise ValueError('changed R743 source, continuation, or TSQR: '+name)
    import r743_early_material_disk as early
    import r746_physical_core_seed as seed

    # Only the private solver module sees this facade; source frames retain
    # their normal references to the real source and geometrical operators.
    model = ModuleType('_r746_solver_material')
    vars(model).update({k:v for k,v in vars(early).items() if not k.startswith('__')})
    model.R743Build,model.R743Frame = seed.R746Build,seed.R746Frame
    model.weak = SimpleNamespace(**vars(early.weak))
    checks = {}
    context = {}

    def bound(label,name):
        module = early.weak.bound_module(label,name)
        if name == 'r732_disk_qualification.py':
            original = module.center_jets
            module.center_jets = lambda *args: seed.centre_jets(original,*args)
            qualify = module.qualify
            def physical(build,phase,q,degree,**kwargs):
                if (phase,degree) not in checks:
                    # A wall-clock tail after a restored job may qualify its last
                    # paired field before setting up that phase in this process.
                    paid,level = context['paid'],context['level']
                    keys = {'train':[phase,'train',level], 'validation':[phase,'validation',level+1]}
                    if any(not paid.filename('r746_zero_core_seed',k).is_file() for k in keys.values()):
                        raise ValueError('missing original paired R746 zero-seed receipt')
                    checks[phase,degree] = {p:paid.get('r746_zero_core_seed',k,None) for p,k in keys.items()}
                report = qualify(build,phase,q,degree,**kwargs)
                report['r746_zero_seed_before_fit'] = checks[phase,degree]
                return report
            module.qualify = physical
        elif name == 'r732_disk_solver.py':
            module.FILES = (*module.FILES,'r746_physical_core_seed.py','r746_native_disk_solver.py')
            base = module.Continuation
            class Audited(base):
                def __init__(self,paid,level,iterations):
                    context.update(paid=paid,level=level)
                    super().__init__(paid,level,iterations)

                def setup(self,phase,degree):
                    frames = super().setup(phase,degree)
                    if (phase,degree) in checks:
                        return frames
                    result = {}
                    for purpose,level in (('train',self.level),('validation',self.level+1)):
                        frame = frames[purpose]
                        key = [phase,purpose,level]
                        def measure():
                            value = seed.check_zero_seed(frame,self.build,phase)
                            value['original_radial_rows'] = module.array_id(frame.r)
                            value['original_material_angles'] = module.array_id(frame.s)
                            return value
                        result[purpose] = self.p.get('r746_zero_core_seed',key,measure)
                    checks[phase,degree] = result
                    emit('R746_ZERO_CORE',module.plain({'phase':phase,'degree':degree,'checks':result}),flush=True)
                    return frames
            module.Continuation = Audited
        return module

    model.weak.bound_module = bound
    def emit(marker,*args,**kwargs):
        tag = {'R743_PHASE':'R746_PHASE','R743_DISK_FINAL':'R746_DISK_FINAL'}.get(marker,marker)
        builtins.print(tag,*args,**kwargs)

    path = HERE/'r743_native_disk_solver.py'
    spec = importlib.util.spec_from_file_location('_r746_paid_runner',path)
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    runner.builtins = SimpleNamespace(print=emit)
    if not any(x=='--state' or x.startswith('--state=') for x in sys.argv[1:]):
        sys.argv.extend(('--state','r746-paid-state'))
    sys.modules['r743_early_material_disk'] = model
    try:
        runner.main()
    finally:
        sys.modules['r743_early_material_disk'] = early


if __name__=='__main__':
    main()
