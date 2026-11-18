"""A fixed external lambda multiplies the complete integral reference lift.

At zero return the unchanged unlifted Base and never patch Flow.geo. At one
use the existing full lift and analytic parameter installer. At intermediate
lambda derive those same functions with only the full geometric lift and its
control variation multiplied by lambda. The inlet projection/Jacobian is not
scaled. Intermediate inlet metric metadata must not claim exact matching.
"""
import hashlib
from pathlib import Path
import types

LIBRARY=Path(__file__).with_name('round_raw_lib')
LIFT=LIBRARY/'exact_core_lift.py'
JAC=LIBRARY/'analytic_adaptive_core_jac.py'


def derived_sources():
    lift=LIFT.read_text();jac=JAC.read_text()
    replacements=[
        ('g[name]=g[name]+factor[:,None,None]*Hj[None,:,:]',
         'g[name]=g[name]+LIFT_STRENGTH*factor[:,None,None]*Hj[None,:,:]'),
        ("self._inlet_metrics=dict(position=0.,first=0.,second=0.,metric_l1=0.,scope='The analytical reference lift retains the exact core and its two angular jets; quadrature/inversion roundoff is audited separately.',unlifted_projection=self.unlifted_projection)",
         "self._inlet_metrics=dict(partial_lift_strength=LIFT_STRENGTH,scope='The finite inlet is (1-lambda) times its original finite projection plus lambda times the defining core. No zero metric or exact-core inlet is claimed at intermediate lambda.',unlifted_projection=self.unlifted_projection)")]
    for old,new in replacements:
        if lift.count(old)!=1:raise RuntimeError('Original lift anchor changed: '+old[:80])
        lift=lift.replace(old,new)
    old='h=a*chi;hp=v*chi+a*chip'
    new='h=LIFT_STRENGTH*(a*chi);hp=LIFT_STRENGTH*(v*chi+a*chip)'
    if jac.count(old)!=1:raise RuntimeError('Original analytic lift-variation anchor changed')
    jac=jac.replace(old,new)
    return dict(lift=lift,parameter_jacobian=jac)


def install_synchronous_lift(Flow,Base,homotopy,window=(.5,.9)):
    lam=float(homotopy)
    if not 0<=lam<=1:raise ValueError('Fixed lift strength must lie in [0,1]')
    if lam==0.:
        return Base
    if lam==1.:
        from exact_core_lift import install_core_lift
        from analytic_adaptive_core_jac import install as install_parameter_jac
        Lift=install_core_lift(Flow,Base,window=window)
        install_parameter_jac(Lift,window=window)
        return Lift
    texts=derived_sources();modules={}
    for name,source in texts.items():
        mod=types.ModuleType('m3_synchronous_'+name+'_'+lam.hex())
        mod.__file__=str(Path(__file__).resolve())+'::'+name
        mod.__dict__['LIFT_STRENGTH']=lam
        exec(compile(source,mod.__file__,'exec'),mod.__dict__)
        modules[name]=mod
    Lift=modules['lift'].install_core_lift(Flow,Base,window=window)
    modules['parameter_jacobian'].install(Lift,window=window)
    return Lift


def source_provenance():
    texts=derived_sources()
    return dict(scope=__doc__,original_lift_sha256=hashlib.sha256(LIFT.read_bytes()).hexdigest(),
        original_parameter_jac_sha256=hashlib.sha256(JAC.read_bytes()).hexdigest(),
        derived_source_sha256={name:hashlib.sha256(source.encode()).hexdigest() for name,source in texts.items()},
        fixed_window=[.5,.9],control_variation='Multiply h and hp by lambda; inlet _initial_jac unscaled; fixed=False p0 remains the original centered difference.',
        midpoint_inlet='(1-lambda)*(background+finite_projected_core)+lambda*Gamma_lambda',
        mean_height='No explicit vertical mean is supplied by the planar lift. The mean of the actual changed Frenet velocity must be integrated by the original height_integral, with its original domain gates.')
