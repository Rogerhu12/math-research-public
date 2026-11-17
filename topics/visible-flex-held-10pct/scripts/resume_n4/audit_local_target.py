#!/usr/bin/env python3
import json,hashlib,numpy as np
from pathlib import Path
from plateau_core import PlateauSupportCore
from local_flatten_core import make_core_class
Core=make_core_class(PlateauSupportCore)
a=.147;b=.08;eta=1/(3-4*(np.sqrt(2)-1)*(1-np.cos(4*a)))
settings=dict(halfwidth=a,transition=b,control_transition=.16,bimodal_eta=eta,arc_nodes=4096)
base=Core(.06,np.zeros(7),4,homotopy=0,**settings)
new=Core(.06,np.zeros(7),4,homotopy=1,**settings)
N=65536;phi=2*np.pi*np.arange(N)/N
unit=new.unit_rho(phi);smooth=base.unit_rho(phi)
rhos=new.rho_material_jets(np.linspace(.003,2*np.pi-.003,507));h=1e-6
pp=new.rho_material_jets(np.linspace(.003,2*np.pi-.003,507)+h)
mm=new.rho_material_jets(np.linspace(.003,2*np.pi-.003,507)-h)
out=dict(scope='Numerical geometric diagnostics of the new exact defining core; not a surface or interval geometry certificate',eta=eta,q=.06,halfwidth=a,transition=b,beta=new.local_flatten_beta,mean_unit=float(unit.mean()),max_unit_change=float(abs(unit-smooth).max()),sampled_rho_min=new.rho_min_sample,rho_lower_derivative_envelope=new.rho_lower,core_control_free=True,phi_sample_count=N,
    support_moments_per_q={str(k):float(2*np.mean(unit*np.cos(k*phi))/(1-k*k))for k in (4,8,12,16,20,24)},
    baseline_support_moments_per_q={str(k):float(2*np.mean(smooth*np.cos(k*phi))/(1-k*k))for k in (4,8,12,16,20,24)},
    material_rho_first_difference_error=float(abs((pp['rho']-mm['rho'])/(2*h)-rhos['rho_u']).max()),material_rho_second_difference_error=float(abs((pp['rho_u']-mm['rho_u'])/(2*h)-rhos['rho_uu']).max()),
    protected_arc_radius_error=float(abs(1+.06*new.unit_rho(np.linspace(-a,a,1001))-.1).max()),
    circle_center_x=float(new.normal_geometry(np.array([0.]))['F'][0,0]-.1),
    source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in (Path('local_flatten_core.py'),Path(__file__))})
Path('local-target-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
