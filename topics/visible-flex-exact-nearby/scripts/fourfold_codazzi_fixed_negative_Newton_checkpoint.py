"""Atomic acceptance of a whole residual/trace pair after the actual ASQ27 zero-suffix failure."""
import argparse
import ast
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from types import ModuleType

TOPIC = "topics/visible-flex-exact-nearby"
P = TOPIC + "/scripts/fourfold_codazzi_fixed_negative_Newton"
ORIGINAL = P + "_owner.py"
SCIENCE = P + "_checkpoint.py"
WORKER = P + "_checkpoint_worker.py"
GENERATOR = TOPIC + "/scripts/make_fixed_negative_Newton_checkpoint_manifest.py"
PARENT_MANIFEST = TOPIC + "/notes/2026-11-28-fixed-affine-negative-Newton-trajectory-inputs.json"
MANIFEST = TOPIC + "/notes/2026-11-28-fixed-negative-Newton-checkpoint-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-fixed-negative-Newton-checkpoint-public.yml"
PARENT_RUN = "46149703541"
PARENT_JOB = 140993452971
EVENT = "053173652dcd7b29b9ecd5b696aafcf6d72a01da"
CHECKOUT = "af15246f1df8dfed6c87776ea296884d1584469e"
BASE = TOPIC + "/notes/fixed_negative_Newton_trajectory_ci"
DEST = BASE + "/run-" + PARENT_RUN + "-1"
NEW_BASE = TOPIC + "/notes/fixed_negative_Newton_checkpoint_ci"
ORIGINAL_SHA = "719ca0a9fec163ca382f076ff1e49e02d494a9c4ca5a8e0371de7878b27caf6e"
TRIAL_SHA = "f1f9ead72df153a5aa41020d5febac6200536a6e4f28dc9ea509ab86761c0097"
FILES = {
    "ASQ27_manifest":(PARENT_MANIFEST,"cc7cc7235b49c3d1be27cc49fdf9c6ac2595086a3e45f42bd4b4a486aa0bb7e5"),
    "ASQ27_actual":(DEST+"/fixed-negative-Newton-trajectory.json","2b79666c2a62fbd02bcb41a810494cdccc1c5b75689e107e4a5610d132d2234f"),
    "ASQ27_execution":(DEST+"/execution.json","9dfe7c0fa1ff6a1a4aba1cb0ea1427e7d97775bd4d6de7d7b9c4cb14bdf72230"),
    "ASQ27_consumed":(BASE+"/consumed-v1.json","4b23e304f9308863cc22c3a3770b8fec5819c4f6b6d4ce7a230d9a84d541737b"),
    "ASQ27_science":(ORIGINAL,ORIGINAL_SHA),
    "ASQ27_worker":(P+"_public_worker.py","3f1898d0aeedf12443a66042ad71788eb7eda5dcfee5f72a5cff27780e155bfa"),
    "ASQ27_generator":(TOPIC+"/scripts/make_fixed_negative_Newton_trajectory_manifest.py",
                       "59b9871542be3ba8db1d0fcc60022f7f8087feef086c3bf7b91383d24c0d40a0")}


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def pinned(root, role):
    path, digest = FILES[role]
    raw = (root/path).read_bytes()
    require(sha(raw)==digest,"original whole "+role)
    return raw


def parent(root):
    raw = pinned(root,"ASQ27_actual")
    d = json.loads(raw)
    e,m,c = [json.loads(pinned(root,k)) for k in ("ASQ27_execution","ASQ27_manifest","ASQ27_consumed")]
    idn = d["identity"]
    require(e["run_id"]==idn["run_id"]==c["run_id"]==PARENT_RUN
            and e["run_attempt"]==idn["run_attempt"]==c["run_attempt"]=="1"
            and e["event_commit"]==idn["workflow_event_commit"]==EVENT
            and e["actual_scientific_checkout"]==idn["actual_scientific_checkout"]==CHECKOUT
            and e["manifest_sha256"]==idn["manifest_sha256"]==c["manifest_sha256"]==FILES["ASQ27_manifest"][1]
            and e["problem_id"]==c["problem_id"]==m["problem_id"] and c["output_directory"]==DEST
            and e["scientific_children"]==e["actual_child_returncode"]==1 and e["timed_out"] is False
            and d["complete"] is d["proved"] is e["complete"] is e["original_scientific_complete"] is False
            and e["scientific_files"]==[{"path":FILES["ASQ27_actual"][0],"bytes":len(raw),"sha256":sha(raw)}]
            and d["complete_cells"]==e["actual_complete_new_cells"]==0 and d["complete_suffix"] is None
            and d["failure"] is d["actual_returncode"] is e["original_scientific_failure"] is None
            and d["stage"]=="signed_fixed_affine_backward_trial" and d["new_records"]=={}
            and d["completed_targets"]==e["completed_natural_targets"]==[]
            and e["new_target_order"]==c["target_order"]==m["target_order"]
            and c["automatic_scientific_retry"] is c["old_completed_targets_may_be_recomputed"] is False,
            "one truly failed original job and zero accepted cells or targets")
    return m,d


def decimal_endpoint(endpoint, rounding):
    if endpoint.is_zero():
        return Decimal(0)
    mant, exp = map(int,endpoint.man_exp())
    value = Fraction(mant)*(Fraction(2)**exp)
    return Context(prec=82,rounding=rounding).divide(Decimal(value.numerator),Decimal(value.denominator))


def ball(value, direction):
    """An outward decimal pair of the exact two Arb dyadic endpoints, including exact zero."""
    require(direction=="upper" and value.is_finite(),"finite directed residual scalar for publication")
    lo = decimal_endpoint(value.lower(),ROUND_FLOOR)
    hi = decimal_endpoint(value.upper(),ROUND_CEILING)
    scale = min(lo.as_tuple().exponent,hi.as_tuple().exponent)
    def integer(endpoint):
        digits = endpoint.as_tuple()
        coeff = int("".join(map(str,digits.digits)))
        return (-1 if digits.sign else 1)*coeff*10**(digits.exponent-scale)
    left,right = integer(lo),integer(hi)
    require(left<=right,"outward decimal endpoints in order")
    return dict(kind="complete_decimal_ball_v1",mathematical_direction=direction,
                midpoint_integer=str(5*(left+right)),radius_integer=str(5*(right-left)),
                decimal_exponent=str(scale-1))


def repair_trial(trial,radial):
    raw=Path(trial.__file__).read_bytes()
    require(sha(raw)==TRIAL_SHA,"entire original trial operator and flat quadrature")
    tree=ast.parse(raw)
    fn,=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="run"]
    forms=['sums[region][0] += (2*half*(e2+beyond)).upper()',
           'sums[region][1] += (2*half*y2).upper()']
    new=['sums[region][0] += (2*half*finite_integral(e2+beyond, weights0[-1]*M**2, row,k,lo,hi,region,"residual")).upper()',
         'sums[region][1] += (2*half*finite_integral(y2, trial.bound**2, row,k,lo,hi,region,"trial")).upper()']
    for src, dst in zip(forms,new):
        expected=ast.dump(ast.parse(src).body[0])
        node,=[n for n in ast.walk(fn) if isinstance(n,ast.AugAssign) and ast.dump(n)==expected]
        node.value=ast.parse(dst).body[0].value
    diagnostic={"residual":0,"trial":0}
    def finite_integral(flat,cap,row,k,lo,hi,region,kind):
        if flat.is_finite():
            return flat
        # Pointwise on the real cell, squared H^s <= maximum Fourier weight
        # times the squared pair A0 bound. The flat reference mass is one.
        require(cap.is_finite() and cap>=0,"nonfinite analytic bound for "+repr((row,k,lo,hi,region,kind)))
        diagnostic[kind]+=1
        if diagnostic[kind]<=3:
            print("analytic pointwise integral bound",row,k,str(lo),str(hi),region,kind,str(cap),flush=True)
        return cap.upper()
    trial.finite_integral=finite_integral
    exec(compile(ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[])),trial.__file__,"exec"),vars(trial))
    return diagnostic


def replace_once(text,a,b):
    require(text.count(a)==1,"one immutable original source locus: "+a[:75])
    return text.replace(a,b)


def owner(root):
    path=root/ORIGINAL
    raw=pinned(root,"ASQ27_science")
    src=raw.decode()
    src=replace_once(src,'    flint.ctx.prec=320','    flint.ctx.prec=320\n    diagnostic=repair_trial(trial,radial)')
    src=replace_once(src,'            state["complete_cells"]=count\n            state["complete_suffix"]=dict(',
                     '            suffix=dict(')
    src=replace_once(src,'quadratic_integrals={key:[fm.record(v,"upper") for v in vals] for key,vals in sums.items()})\n            save()',
                     '''quadratic_integrals={key:[ball(v,"upper") for v in vals] for key,vals in sums.items()})
            candidate=dict(state,seconds=time.monotonic()-began,complete_cells=count,complete_suffix=suffix,
                           analytic_integral_fallbacks=dict(diagnostic))
            validate(candidate,m)
            previous=signal.pthread_sigmask(signal.SIG_BLOCK,{signal.SIGTERM})
            try:
                payload=encode(candidate)
                require(len(payload)<=PARAMETERS["maximum_actual_bytes"],"complete atomic checkpoint fits")
                core.atomic(out,payload)
                state.update(candidate)
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK,previous)''')
    src=replace_once(src,'        complete_cells=0,complete_suffix=None,','        analytic_integral_fallbacks=dict(diagnostic),complete_cells=0,complete_suffix=None,')
    src=replace_once(src,'    except BaseException as ex:\n        state.update','    except BaseException as ex:\n        traceback.print_exc()\n        state.update')
    src=replace_once(src,'fm.record(target.angular_tail_max,"upper")','ball(target.angular_tail_max,"upper")')
    src=replace_once(src,'upper=lambda v:fm.record(v.upper(),"upper")','upper=lambda v:ball(v.upper(),"upper")')
    mod=ModuleType("_ASQ27R_whole_trial_owner")
    mod.__file__=__file__
    mod.__dict__.update(repair_trial=repair_trial,ball=ball)
    exec(compile(src,str(path)+"#whole-atomic-checkpoint","exec"),vars(mod))
    mod.KIND="R149_fixed_negative_Newton_trajectory_after_zero_checkpoint_v1"
    mod.MANIFEST_KIND="R149_fixed_negative_Newton_atomic_checkpoint_inputs_v1"
    mod.FIELDS=(*mod.FIELDS,"analytic_integral_fallbacks")
    original_admit,original_validate=mod.admit,mod.validate
    def admit(root,raw,digest,rows_index):
        base,failed=parent(Path(root))
        m,roles,admitted=original_admit(root,raw,digest,rows_index)
        require(m["predecessor"]=={"run":PARENT_RUN,"attempt":"1","job":PARENT_JOB,"event":EVENT,
            "accepted_cells":0,"accepted_targets":0}
            and m["operation"]["output_base"]==NEW_BASE
            and m["operation"]["consumed_marker"]==NEW_BASE+"/consumed-v1.json"
            and m["operation"]==dict(base["operation"],output_base=NEW_BASE,consumed_marker=NEW_BASE+"/consumed-v1.json")
            and all(roles[k]["path"]==p and roles[k]["sha256"]==s for k,(p,s) in FILES.items()),
            "complete genuine zero-suffix parent and a distinct first reservation")
        for spec in base["files"]:
            role=spec["role"]
            actual=roles["ASQ27_"+role] if role in ("worker","science","generator") else roles[role]
            require(all(actual[k]==spec[k] for k in spec if k!="role"),"every original mathematical and operational file")
        require(failed["original_input_identity"]==admitted[-1] and base["target_order"]==m["target_order"],
                "same whole 184/32 source, two geometry arrays and both uncomputed targets")
        return m,roles,admitted
    def validate(d,m):
        original_validate(d,m)
        require(set(d["analytic_integral_fallbacks"])=={"residual","trial"} and
                all(type(v) is int and 0<=v<=d["complete_cells"] for v in d["analytic_integral_fallbacks"].values()),
                "complete accepted fallback counts")
    mod.admit,mod.validate=admit,validate
    return mod


# The public worker imports this small definition before starting the scientific child.
_repo=Path(__file__).resolve().parents[3]
_original=owner(_repo)
PARAMETERS,RUNTIME,KIND,MANIFEST_KIND,FIELDS,TARGETS=(
    getattr(_original,k) for k in ("PARAMETERS","RUNTIME","KIND","MANIFEST_KIND","FIELDS","TARGETS"))
admit,validate=_original.admit,_original.validate

if __name__=="__main__":
    arg=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest","manifest-sha","rows-index","checkout","private","out"):
        arg.add_argument("--"+k,required=True)
    arg.add_argument("--preflight-only",action="store_true")
    sys.exit(_original.execute(arg.parse_args()))
