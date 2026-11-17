"""Small independent finite-difference audit of the replacement core API."""
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from complementary_moment_basis import ComplementaryMomentBasis
from uniform_complement_core import make_core_class


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def refined_evaluation(core,theta):
    phi=core.evaluate(theta)['phi'].copy()
    for _ in range(5):
        g=core.normal_geometry(phi);res=core.arc(phi)-theta
        phi-=res/g['rho']
    return core.normal_geometry(phi),phi


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference-core',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    spec=importlib.util.spec_from_file_location('explicit_reference_core',a.reference_core)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    Core=make_core_class(mod.PlateauSupportCore)
    common=dict(base_mode=4,halfwidth=.145,transition=.08,control_transition=.08,arc_nodes=512)
    coefficients=np.array([1e-5,-2e-6,3e-7,-4e-8,5e-9])
    theta=np.linspace(.013,2*np.pi-.019,71)
    cases=[]
    for lam in (0.,.4,1.):
        core=Core(q=.005,corrections=coefficients,homotopy=lam,**common)
        analytic=core.parameter_derivatives(theta)
        checks=[]
        for index in (0,1,5):
            errors=[]
            for h in (1e-5,5e-6,2.5e-6):
                plus=np.r_[.005,coefficients];minus=plus.copy();plus[index]+=h;minus[index]-=h
                cp=Core(q=plus[0],corrections=plus[1:],homotopy=lam,**common)
                cm=Core(q=minus[0],corrections=minus[1:],homotopy=lam,**common)
                Fp=refined_evaluation(cp,theta)[0]['F'];Fm=refined_evaluation(cm,theta)[0]['F']
                fd=(Fp-Fm)/(2*h);err=float(np.max(np.linalg.norm(fd-analytic[index],axis=1)))
                errors.append(dict(step=h,max_position_parameter_derivative_error=err))
            checks.append(dict(parameter_index=index,errors=errors))
        normal=np.array([-.53,-.31,-.205,-.183,-.16,-.02,.17,.193,.217,.33,.57])
        material=core.arc(normal);jets=core.rho_material_jets(material)
        rho_fd=[]
        for h in (1e-4,5e-5,2.5e-5):
            rho=[]
            for multiple in (-2,-1,0,1,2):rho.append(refined_evaluation(core,material+multiple*h)[0]['rho'])
            first=(rho[0]-8*rho[1]+8*rho[3]-rho[4])/(12*h)
            second=(-rho[0]+16*rho[1]-30*rho[2]+16*rho[3]-rho[4])/(12*h*h)
            rho_fd.append(dict(step=h,rho_u_error=float(np.max(abs(first-jets['rho_u']))),rho_uu_error=float(np.max(abs(second-jets['rho_uu'])))))
        cases.append(dict(homotopy=lam,rho_lower=core.rho_lower,rho_min_sample=core.rho_min_sample,
                          positivity_grid=core.positivity_grid_per_sector,parameter_derivatives=checks,rho_material_jets=rho_fd))
    strong=Core(q=.06,corrections=coefficients*.1,homotopy=1.,**common)
    plain=Core(q=.06,corrections=np.zeros(5),homotopy=1.,**common)
    protected=np.linspace(-.145,.145,65)
    bg=strong.basis.support_jets(protected,4,1.)
    circle=dict(q=.06,protected_max_b_derivatives=[float(abs(v).max()) for v in bg],
                protected_max_primitive=float(abs(strong.basis.primitive(protected,1.)).max()),
                position_change_from_zero_control=float(np.max(np.linalg.norm(strong.normal_geometry(protected)['F']-plain.normal_geometry(protected)['F'],axis=1))),
                material_arc_change=float(np.max(abs(strong.arc(protected)-plain.arc(protected)))),
                rho_change_from_radius=float(np.max(abs(strong.normal_geometry(protected)['rho']-.1))),
                period_arc_error=float(np.max(abs(strong.arc(protected+2*np.pi)-strong.arc(protected)-2*np.pi))),
                rho_lower=strong.rho_lower,rho_min_sample=strong.rho_min_sample)
    basis=strong.basis;points=np.array([-.43,-.215,-.197,-.16,.018,.17,.193,.213,.4,.68]);derivs=basis.support_jets(points,4)
    functional=[]
    for h in (1e-5,5e-6):
        errors=[]
        for k in range(4):
            b=[basis.support_jets(points+m*h,k)[k] for m in (-2,-1,1,2)]
            fd=(b[0]-8*b[1]+8*b[2]-b[3])/(12*h)
            errors.append(float(np.max(abs(fd-derivs[k+1]))/max(1.,np.max(abs(derivs[k+1])))))
        f=[basis.primitive(points+m*h) for m in (-2,-1,1,2)]
        fd=(f[0]-8*f[1]+8*f[2]-f[3])/(12*h)
        functional.append(dict(step=h,b_derivative_relative_errors=errors,primitive_first_error=float(np.max(abs(fd-derivs[0])))))
    high=ComplementaryMomentBasis(modes=6,halfwidth=.145,transition=.08,quadrature_order=96)
    primitive_quadrature=float(np.max(abs(high.primitive(points)-basis.primitive(points))))
    report=dict(scope='Independent finite-difference/API checks for new explicit core controls; no new prefix BVP or closed surface.',
      reference=dict(path=str(a.reference_core),sha256=sha(a.reference_core)),
      source_sha256={n:sha(Path(__file__).with_name(n)) for n in ('audit_uniform_core.py','uniform_complement_core.py','complementary_moment_basis.py','moment_interval_bounds.py')},
      cases=cases,protected_circle=circle,functional_derivatives=functional,
      primitive_64_to_96_difference=primitive_quadrature,elapsed_seconds=time.monotonic()-started,
      limitations='Finite differences and floating evaluations are diagnostic. Rational moment coefficient and derivative enclosures are checked separately; no geometric BVP is solved.')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__=='__main__':main()
