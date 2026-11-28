"""Complete fixed-material coefficient jets of the original lambda-zero core.

For h=1+sum c_j cos(m_j phi), u=phi+sum(1-m_j^2)c_j sin(m_j phi)/m_j.
At fixed u, dphi_j=-(1-m_j^2)sin(m_j phi)/(m_j rho).  Thus
d Gamma_u=-er*dphi and d Gamma_uu=-et*dphi/rho+er*d rho/rho^2,
where d rho=(1-m_j^2)cos(m_j phi)+rho_phi*dphi.  The position
derivative is the original PlanarSupportCore.parameter_derivatives method.

The existing adaptive parameter-Jacobian installer supplies the complete
angular chart, reference lift, projection, state Jacobian and convection.
Its original additive-delta centered difference is retained. No residual,
control scale, domain, BVP equation or acceptance gate is changed here.
"""
import hashlib
import inspect
from pathlib import Path
import numpy as np


def parameter_jets(core,theta):
    if type(core).__name__ != 'PlanarSupportCore':
        raise ValueError('This entry is only for the original lambda-zero PlanarSupportCore')
    theta = np.asarray(theta,dtype=float)
    if theta.ndim != 1:
        raise ValueError('Use the original one-dimensional fixed-material angular grid')
    g = core.evaluate(theta)
    phi = g['phi']
    geometry = core.normal_geometry(phi)
    rho,er,et = (geometry[key] for key in ('rho','er','et'))
    m = np.asarray(core.frequencies,dtype=float)[:,None]
    coefficients = np.asarray(core.coefficients,dtype=float)
    angle = m*phi[None,:]
    sine,cosine = np.sin(angle),np.cos(angle)
    sigma = (1-m*m)*sine/m
    dphi = -sigma/rho[None,:]
    rho_phi = sine.T@(core.frequencies*(core.frequencies**2-1)*coefficients)
    drho = (1-m*m)*cosine+rho_phi[None,:]*dphi
    d0 = core.parameter_derivatives(theta)
    d1 = -dphi[:,:,None]*er[None,:,:]
    d2 = (-dphi[:,:,None]*et[None,:,:]/rho[None,:,None]
          +drho[:,:,None]*er[None,:,:]/rho[None,:,None]**2)
    if (d0.shape != (len(coefficients),len(theta),3)
            or not all(np.all(np.isfinite(value)) for value in (d0,d1,d2))):
        raise FloatingPointError('A complete original-core coefficient jet is nonfinite')
    return d0,d1,d2


def install(BVP,analytic_module,*,window=(.5,.9),original_installer=None):
    """Install on one fresh class; the caller owns global restoration/lifetime."""
    installer = analytic_module.install if original_installer is None else original_installer
    old = BVP.fun_jac
    analytic_module.parameter_jets = parameter_jets
    installer(BVP,window)
    files = (Path(__file__),Path(inspect.getsourcefile(installer)).resolve())
    return dict(kind='original_lambda_zero_support_complete_analytic_parameter_columns',
        source_hashes={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        old_fun_jac_sha256=hashlib.sha256(inspect.getsource(old).encode()).hexdigest(),
        new_fun_jac_sha256=hashlib.sha256(inspect.getsource(BVP.fun_jac).encode()).hexdigest(),
        complete_support_columns_retained=True,original_delta_difference_retained=True,
        all_state_rows_and_columns_retained=True,original_residuals_and_gates_changed=False,
        numerical_parameter_derivative_changed=True)
