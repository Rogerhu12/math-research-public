#!/usr/bin/env python3
"""Audit a nested core embedding only; this does not run a new BVP."""
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
from plateau_core import PlateauSupportCore
from bimodal_core import make_core_class as design_core
from nested_projection_core import make_core_class,embed_compact_coefficients
from exact_lift_parameter_jac import parameter_jets


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--modes',type=int,default=12)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    sys.path[:0]=[str(a.source_topic/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    from curve_stable_prefix_bvp import load_checkpoint
    rec=load_checkpoint(a.checkpoint);oldM=rec['config']['modes'];q=rec['core_summary']['q_parameter']
    settings=rec['plateau_settings'];c=np.asarray(rec['core_summary']['corrections'])
    Old=design_core(PlateauSupportCore);New=make_core_class(PlateauSupportCore,oldM)
    old=Old(q,c,4,arc_nodes=1024,**settings);probe=New(q,np.zeros(a.modes-1),4,arc_nodes=1024,**settings)
    d,embedding=embed_compact_coefficients(old.basis,c,probe.basis)
    new=New(q,d,4,arc_nodes=1024,**settings)
    theta=2*np.pi*np.arange(2048)/2048;phi=theta
    j0=old.rho_material_jets(theta);j1=new.rho_material_jets(theta)
    errors={key:float(abs(j1[key]-j0[key]).max())for key in ('F','Ft','Ftt','rho','rho_u','rho_uu')}
    b0=old.basis.support_jets(phi,4,settings['homotopy']);b1=new.basis.support_jets(phi,4,settings['homotopy'])
    control_errors=[float(abs(c@b0[k]-d@b1[k]).max())for k in range(5)]
    jt=2*np.pi*np.arange(128)/128;js=parameter_jets(new,jt)
    direction=np.cos(np.arange(a.modes)+1)*q
    predicted=[np.einsum('j,jpk->pk',direction,x)for x in js];jac=[]
    for step in (1e-5,3e-6,1e-6,3e-7):
        plus=New(q+step*direction[0],d+step*direction[1:],4,arc_nodes=512,**settings).evaluate(jt)
        minus=New(q-step*direction[0],d-step*direction[1:],4,arc_nodes=512,**settings).evaluate(jt)
        jac.append(dict(step=step,
            errors={key:float(abs((plus[key]-minus[key])/(2*step)-v).max())for key,v in zip(('F','Ft','Ftt'),predicted)},
            scales={key:float(abs(v).max())for key,v in zip(('F','Ft','Ftt'),predicted)}))
    result=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
        modes_old=oldM,modes_new=a.modes,frozen_projection_order=oldM,homotopy=settings['homotopy'],
        embedding=embedding,actual_core_errors=errors,support_derivative_errors_0_to_4=control_errors,
        fixed_material_parameter_jac_checks=jac,
        positivity=dict(old_lower=old.rho_lower,new_lower=new.rho_lower,old_grid=old.positivity_grid_per_sector,new_grid=new.positivity_grid_per_sector),
        source_sha256={k:hashlib.sha256(Path(__file__).with_name(k).read_bytes()).hexdigest()for k in ['audit_nested_projection.py','nested_projection_core.py','bimodal_core.py','fixed_bimodal_core.py','complementary_moment_basis.py','moment_interval_bounds.py','exact_lift_parameter_jac.py']})
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
