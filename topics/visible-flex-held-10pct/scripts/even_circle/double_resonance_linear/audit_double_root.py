"""Recheck one double root with the untouched original single-mode integrator."""
import argparse,ast,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from physical_linear_design import PhysicalDesign,geometry


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True);p.add_argument('--port',type=Path,required=True)
    p.add_argument('--profile',type=Path,required=True);p.add_argument('--tail-certificate',type=Path,required=True)
    p.add_argument('--tail-constants',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();d=PhysicalDesign(args.source_root,args.port);cfg=json.loads(args.profile.read_text());f=d.profile(cfg)
    original=args.source_root/'topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_outward_bridge_linear.py'
    tree=ast.parse(original.read_text());nodes=[node for node in tree.body if isinstance(node,ast.ClassDef)and node.name=='BackwardLine']
    if len(nodes)!=1:raise RuntimeError('Exactly one original BackwardLine class required')
    namespace=dict(np=np,math=math,solve_ivp=solve_ivp)
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(original),'exec'),namespace)
    BackwardLine=namespace['BackwardLine'];rows=[]
    for index in (0,1):
        mode=d.port['modes'][index];cut=d.port['cut'];m2=mode*mode
        terminal=np.array([-cut['backgroundSlope']*(cut['radius']*d.port['linearSlope'][index]-m2)/(m2-1),1.])
        def rhs(s,y):
            a,v,_=f.profile([s]);a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return np.array([-(m2-1)*v*y[0]-m2*b*y[1],(m2-1)*v*v*y[0]/b+m2*v*y[1]])/a
        line=BackwardLine(rhs,f.breaks,terminal)
        rows.append(dict(mode=mode,normalized_core=line.core.tolist(),logscale=line.logscale,
            unnormalized_core=(line.core*math.exp(line.logscale)).tolist()))
    jacobians=[]
    for factor in (1.,.1):
        J=np.zeros((2,2))
        for k,(name,h0)in enumerate((('delta',1e-7),('vd',1e-6))):
            h=h0*factor;plus=dict(cfg);minus=dict(cfg);plus[name]+=h;minus[name]-=h
            J[:,k]=(d.linear(plus,2,2e-13)['core'][:,1]-d.linear(minus,2,2e-13)['core'][:,1])/(2*h)
        jacobians.append(dict(step_factor=factor,parameter_order=['delta','vd'],matrix=J.tolist(),singular_values=np.linalg.svd(J,compute_uv=False).tolist()))
    constants=json.loads(args.tail_constants.read_text());cert=json.loads(args.tail_certificate.read_text())
    mismatch={k:[v,constants['parameters'].get(k)]for k,v in d.port['parameters'].items()if k!='spacing'and constants['parameters'].get(k)!=v}
    if mismatch:raise RuntimeError('Tail background physics differ: '+str(mismatch))
    if constants['factory_sha256']!=d.port['source']['source_sha256']['closing_weighted_tail.mjs']:raise RuntimeError('Tail factory differs')
    height=cert['exact_background_height']['upper'];geo=geometry(f,halfwidth=.147,cylinder_length=.54,nominal_tail_rise=height)
    delta,vu,vd,eps,eta=[F(str(cfg[k]))for k in ('delta','vu','vd','ramp','ramp_eta')]
    aramp=1+delta*eps/(2*(1-eps));chi_square=delta*eps*(1-eta)/(aramp*(1-eps));a=F(147,1000)
    ku_square=(vu*vu*(1-eps)/(eps*delta*(1-eta)))**2/(1-vu*vu)
    kd_square=(vd*vd*(1-eps)/(eps*delta*(1-eta)))**2/(1-vd*vd)
    cut=d.port['cut'];wr=F(str(cut['backgroundSecond']));w=F(str(cut['backgroundSlope']));r=F(str(cut['radius']))
    exact=dict(scope='Exact rational inequalities at the literal profile and cut scalars; not a certificate for the root location or nonlinear surface.',
        lower_characteristic_loss_over_R_squared=str(chi_square),required_halfwidth_squared=str(a*a),
        characteristic_window_strictly_consumed=chi_square>a*a,
        up_meridian_curvature_upper_squared=str(ku_square),down_meridian_curvature_upper_squared=str(kd_square),
        flat_loop_meridian_curvature_below_8=bool(max(ku_square,kd_square)<64),
        short_bridge_declared_curvature=cfg['prefix_bridge']['curvature'],
        short_bridge_cut_curvature_below_4=bool(wr*wr<16*(1+w*w)**3),
        parallel_curvature_below_4=bool(r>F(1,4)))
    if not all(exact[k]for k in ('characteristic_window_strictly_consumed','flat_loop_meridian_curvature_below_8','short_bridge_cut_curvature_below_4','parallel_curvature_below_4')):raise RuntimeError('A requested rational budget gate failed')
    report=dict(scope=__doc__,profile=cfg,original_class_extraction='AST extraction of the unchanged BackwardLine class; only its original numpy/math/solve_ivp globals are supplied.',
        original_single_mode=rows,jacobians=jacobians,background_geometry=geo,rational_head_and_curvature_gates=exact,
        tail_background=dict(physical_parameter_mismatches=mismatch,spacing_is_not_a_rotational_background_parameter=True,
            height_interval=cert['exact_background_height'],factory_sha256=constants['factory_sha256']),
        provenance={**d.provenance,**{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in
            (Path(__file__),original,args.profile,args.tail_certificate,args.tail_constants)}})
    args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))


if __name__=='__main__':main()
