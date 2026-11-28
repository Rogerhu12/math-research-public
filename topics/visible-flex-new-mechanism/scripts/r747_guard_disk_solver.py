"""Launch the frozen R742 material/solver with the R747 analytic guard seed."""
import builtins
import hashlib
import importlib.util
import os
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace


HERE=Path(__file__).resolve().parent
PINS={
    "r742_changed_sleeves.py":"023a4c7d6d39661b024074c1269c928dda26b313569468b2a9a87bc3b1653b75",
    "r742_native_disk_solver.py":"95b65a8b9491ec866072bd2d994d7f41c581d0aa43ceca4d6b1f8bac5a6c560c",
    "r742_native_tsqr.py":"d9565b37ad9e3b8d70df7adf0aa1b82015fd66edadcd6386923c1a1197f2b729",
}


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public"
            or not os.environ.get("GITHUB_RUN_ID","").isdigit()):
        raise SystemExit("R747 requires the public research Actions runner")
    for name,digest in PINS.items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=digest:
            raise ValueError("changed R742 input or paid operator: "+name)
    import r742_changed_sleeves as source
    import r747_physical_guard_seed as seed

    # The frozen runner imports this facade only inside main; its private source
    # objects keep referring to the original R742 module namespace.
    model=ModuleType("_r747_solver_model")
    model.R742Frame=seed.R747Frame
    model.R742Build=seed.R747Build
    model.collar_jets=source.collar_jets
    model.weak=SimpleNamespace(**vars(source.weak))

    def bound(label,name):
        module=source.weak.bound_module(label,name)
        if name!="r732_disk_solver.py":
            return module
        module.FILES=(*module.FILES,*seed.PHYSICAL_FILES)
        base=module.Continuation

        class Audited(base):
            def setup(self,phase,degree):
                frames=super().setup(phase,degree)
                key=[phase]
                first=not self.p.filename("r747_analytic_guard_seed",key).exists()
                result=self.p.get("r747_analytic_guard_seed",key,
                                  lambda:seed.homogeneous_probe(self.build,phase))
                if first:
                    emit("R747_ZERO_GUARD",module.plain(module.summarize(result)),flush=True)
                return frames
        module.Continuation=Audited
        return module

    model.weak.bound_module=bound
    def emit(marker,*args,**kwargs):
        tag={"R742_PHASE":"R747_PHASE","R742_DISK_FINAL":"R747_DISK_FINAL",
             "R742_GUARD_FEET":"R747_GUARD_FEET"}.get(marker,marker)
        builtins.print(tag,*args,**kwargs)

    spec=importlib.util.spec_from_file_location("_r747_paid_runner",HERE/"r742_native_disk_solver.py")
    runner=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    runner.builtins=SimpleNamespace(print=emit)
    if not any(a=="--state" or a.startswith("--state=") for a in sys.argv[1:]):
        sys.argv.extend(("--state","r747-paid-state"))
    sys.modules["r742_changed_sleeves"]=model
    try:
        runner.main()
    finally:
        sys.modules["r742_changed_sleeves"]=source


if __name__=="__main__":
    main()
