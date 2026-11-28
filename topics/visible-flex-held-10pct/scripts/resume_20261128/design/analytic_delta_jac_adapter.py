"""Replace only the original additive-delta Jacobian difference column.

The original function's complete state and support-control calculations are
retained literally.  The separately checked moving-chart derivative replaces
its centered RHS difference.  Residuals, boundaries and acceptance tests are
not changed.  This is a numerical Jacobian change, not bit identity or proof.
"""
import hashlib
import inspect
from pathlib import Path
import sys
import textwrap
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"analytic"))
from material_delta_column import OriginalDeltaColumn


def install(cls):
    original = cls.fun_jac
    before = textwrap.dedent(inspect.getsource(original))
    marker = ("step=2e-6*max(.1,self.cfg['delta']+p[0]);plus=p.copy();"
              "minus=p.copy();plus[0]+=step;minus[0]-=step;"
              "PJ[:,0,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step);"
              "self.initial(p)")
    if before.count(marker) != 1:
        raise ValueError("The original additive-delta difference statement changed")
    closure = inspect.getclosurevars(original)
    if set(closure.nonlocals) != {"window"}:
        raise ValueError("The original complete Jacobian closure changed")
    after = before.replace(marker,
        "PJ[:,0,:]=_held10_complete_delta(self,p,window).rhs(t,y)")
    namespace = dict(original.__globals__)
    namespace.update(closure.nonlocals)
    namespace["_held10_complete_delta"] = OriginalDeltaColumn
    exec(compile(after, str(Path(__file__).resolve())+"::complete_delta_column",
                 "exec"), namespace)
    replacement = namespace[original.__name__]
    stats = dict(calls=0, seconds=0., original_function_sha256=
        hashlib.sha256(before.encode()).hexdigest(), executed_function_sha256=
        hashlib.sha256(after.encode()).hexdigest(),
        replaced_column="additive_delta_only",
        all_state_and_support_columns_retained=True,
        original_residuals_boundaries_and_gates_changed=False,
        numerical_parameter_derivative_changed=True,
        analytical_column_source_sha256=hashlib.sha256(
            (HERE.parent/"analytic/material_delta_column.py").read_bytes()).hexdigest())

    def complete_delta_jac(self, t, y, p):
        begin = time.monotonic()
        result = replacement(self, t, y, p)
        stats["calls"] += 1
        stats["seconds"] += time.monotonic()-begin
        return result

    cls.fun_jac = complete_delta_jac
    return stats
