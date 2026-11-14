"""Numerical implementation checks for R129, using the actual R128 two-jets.

This checks formula/sign/coordinate interfaces.  It is not a continuous residual
certificate and does not solve or assert a nonround prefix or a closed surface.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from fd2d_flat_developable_tail import FlatDevelopableTail
import fd2d_gc_three_field_residual as gc


HERE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path)
    data = path.read_bytes()
    return dict(path=str(path.relative_to(HERE.parent)), bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest())


def maximum(value):
    return float(np.max(np.abs(value)))


def flat_shape_jets(tail, r, u):
    """Analytic local derivatives of the independent flat l,m,n fields."""
    r, u = np.broadcast_arrays(np.asarray(r), np.asarray(u))
    p, q = np.sin(u), np.cos(u)
    y = r*p
    curve = tail.curve(y)
    k, ky = curve['kappa'], curve['kappa_y']
    t = (np.abs(y)-tail.flat_radius)/tail.width
    z = np.clip(t, 0., 1.)
    third = 2520*z*z*(1-z)**2*(3-14*z+14*z*z)
    kyy = np.where((t > 0.) & (t < 1.), tail.amplitude*third/tail.width**3, 0.)
    return dict(
        l=k*p*p, m=-k*p*q, n=k*q*q,
        l_u=r*ky*q*p*p+2*k*p*q,
        m_u=-r*ky*p*q*q-k*(q*q-p*p),
        n_u=r*ky*q**3-2*k*p*q,
        m_s=ky*p*p*q, n_s=-ky*p*q*q,
        l_uu=r*r*kyy*p*p*q*q+r*ky*(-p**3+4*p*q*q)+2*k*(q*q-p*p),
        m_uu=-r*r*kyy*p*q**3+r*ky*(3*p*p*q-2*q**3)+4*k*p*q,
        n_uu=r*r*kyy*q**4-5*r*ky*p*q*q-2*k*(q*q-p*p),
        m_su=r*kyy*p*p*q*q+ky*(2*p*q*q-p**3),
        n_su=-r*kyy*p*q**3-ky*(q**3-2*p*p*q))


def eval_cos(coef, angle):
    return np.sum(np.asarray(coef)[:, None]*np.cos(2*np.arange(len(coef))[:, None]*angle), axis=0)


def eval_sin(coef, angle):
    return np.sum(np.asarray(coef)[:, None]*np.sin(2*np.arange(1,len(coef)+1)[:, None]*angle), axis=0)


def run():
    tail = FlatDevelopableTail(amplitude=1., quadrature_order=96)
    radii = np.array([.32,.34,.4,.58,.8])[:, None]
    angles = (2*np.pi*np.arange(1024)/1024)[None, :]
    local = flat_shape_jets(tail, radii, angles)
    residual = gc.physical_residuals(a=radii,a_s=-1.,a_ss=0.,
        **{k:local[k] for k in ('l','m','n','l_u','m_u','m_s','n_s')})
    actual = tail.evaluate(radii, angles)
    frame = np.stack((actual['e1'],actual['e2'],actual['N']),axis=-1)
    jets = gc.compatible_cartesian_twojet(frame=frame,a=radii,a_s=-1.,
        **{k:local[k] for k in ('l','m','n')})
    jet_errors = {k:maximum(v-actual[k]) for k,v in jets.items()}
    rotation_checks = {}
    for phase in (0., .37, 1.2):
        out = tail.evaluate(radii, angles,phase=phase)
        ff=np.stack((out['e1'],out['e2'],out['N']),axis=-1)
        jj=gc.compatible_cartesian_twojet(frame=ff,a=radii,a_s=-1.,
            **{k:out[k] for k in ('l','m','n')})
        rotation_checks[str(phase)] = max(maximum(jj[k]-out[k]) for k in jj)

    # Nontrivial moving computation angle, with the physical metric unchanged.
    x=np.array([0., .05, .15, .25])[:,None]
    xi=(2*np.pi*np.arange(512)/512)[None,:]
    S=x+.1*x*x; J=1+.2*x
    U=xi+.07*x*(1-x)*np.sin(2*xi)
    Ux=.07*(1-2*x)*np.sin(2*xi)
    om=1+.14*x*(1-x)*np.cos(2*xi)
    omxi=-.28*x*(1-x)*np.sin(2*xi)
    Uxxi=.14*(1-2*x)*np.cos(2*xi)
    r=.8-S
    z=flat_shape_jets(tail,r,U)
    native=dict(a=r,a_s=-1.,a_ss=0.,J=J,U_x=Ux,U_xi=om,
        **{k:z[k] for k in ('l','m','n')},
        l_xi=z['l_u']*om,m_xi=z['m_u']*om,n_xi=z['n_u']*om,
        m_x=J*z['m_s']+Ux*z['m_u'],n_x=J*z['n_s']+Ux*z['n_u'])
    moving=gc.native_residuals(**native)
    angular=dict(a=r,a_s=-1.,J=J,U_x=Ux,U_xi=om,U_x_xi=Uxxi,U_xixi=omxi,
        **{k:z[k] for k in ('l','m','n')},
        l_xi=native['l_xi'],m_xi=native['m_xi'],n_xi=native['n_xi'],
        l_xixi=z['l_uu']*om**2+z['l_u']*omxi,
        m_xixi=z['m_uu']*om**2+z['m_u']*omxi,
        n_xixi=z['n_uu']*om**2+z['n_u']*omxi,
        m_x_xi=J*z['m_su']*om+Uxxi*z['m_u']+Ux*z['m_uu']*om,
        n_x_xi=J*z['n_su']*om+Uxxi*z['n_u']+Ux*z['n_uu']*om)
    angular_out=gc.native_angular_residuals(**angular)

    # This algebraic JVP includes genuine changes of metric and chart inputs.
    rng=np.random.default_rng(129)
    direction={k:.1*rng.standard_normal(np.shape(v)) for k,v in native.items()}
    jvp=gc.native_jvp(**native,**{'d'+k:v for k,v in direction.items()})
    steps=[]
    for h in (.02,.01,.005,.0025):
        plus=gc.native_residuals(**{k:v+h*direction[k] for k,v in native.items()})
        minus=gc.native_residuals(**{k:v-h*direction[k] for k,v in native.items()})
        errors={k:maximum((plus[k]-minus[k])/(2*h)-jvp[k])
                for k in ('G','Rm','Rn','connection_vector')}
        steps.append(dict(step=h,errors=errors))

    order=7
    ll=rng.standard_normal(order+1);nn=rng.standard_normal(order+1)
    mm=rng.standard_normal(order);KK=.21
    dl=rng.standard_normal(order+1);dn=rng.standard_normal(order+1)
    dm=rng.standard_normal(order);dK=.13
    uu=2*np.pi*np.arange(4096)/4096
    full=gc.gauss_fourier(ll,mm,nn,KK)
    direct=eval_cos(ll,uu)*eval_cos(nn,uu)-eval_sin(mm,uu)**2-KK
    dfull=gc.gauss_fourier_jvp(ll,mm,nn,dl,dm,dn,dK)
    ddirect=(eval_cos(dl,uu)*eval_cos(nn,uu)+eval_cos(ll,uu)*eval_cos(dn,uu)
             -2*eval_sin(mm,uu)*eval_sin(dm,uu)-dK)
    epsilon=.125
    high=gc.gauss_fourier([1.,epsilon],[0.],[1.,-epsilon],1-epsilon**2/2)
    projected_rank=gc.gauss_fourier([.5],[],[.5],0.)

    result=dict(
        schema='fd2d-three-field-interface-check-v1',
        scope='Floating formula and genuine two-jet interface check. No continuous certificate or solved nonround prefix.',
        sources=[identity(__file__),identity(HERE/'fd2d_gc_three_field_residual.py'),
                 identity(HERE/'fd2d_flat_developable_tail.py')],
        flat=dict(amplitude=1.,radii=radii[:,0].tolist(),angles=1024,
            zero_n_samples=int(np.count_nonzero(local['n']==0.)),
            zero_entire_shape_samples=int(np.count_nonzero((local['l']==0.)&(local['m']==0.)&(local['n']==0.))),
            residual_max={k:maximum(residual[k]) for k in ('G','Rm','Rn','connection_operator_norm')},
            actual_twojet_errors=jet_errors,rotated_actual_twojet_max=rotation_checks),
        moving_chart=dict(x=x[:,0].tolist(),angles=512,
            S='x + 0.1*x^2',U='xi + 0.07*x*(1-x)*sin(2*xi)',
            minimum_J=float(J.min()),minimum_U_xi=float(om.min()),
            residual_max={k:maximum(moving[k]) for k in ('G','Rm','Rn','connection_operator_norm')},
            angular_residual_max={k:maximum(angular_out[k]) for k in ('G_u','Rm_u','Rn_u','connection_u_operator_norm')}),
        native_jvp=dict(seed=129,direction_scale=.1,finite_difference=steps),
        fourier=dict(input_order=order,output_order=len(full)-1,
            full_product_error=maximum(eval_cos(full,uu)-direct),
            full_product_jvp_error=maximum(eval_cos(dfull,uu)-ddirect),
            exact_dyadic_high_mode_witness=dict(epsilon=epsilon,cosine_coefficients=high.tolist(),
                low_projected_coefficients=high[:2].tolist(),nonzero_omitted_mode=high[2]),
            rank_one_projection_counterexample=dict(projected_l=.5,projected_m=0.,projected_n=.5,
                projected_G=projected_rank.tolist())))
    result['implementation_checks_passed']=bool(
        max(result['flat']['residual_max'].values())<1e-10 and max(jet_errors.values())<1e-12
        and max(rotation_checks.values())<1e-12
        and max(result['moving_chart']['residual_max'].values())<1e-10
        and max(result['moving_chart']['angular_residual_max'].values())<1e-9
        and max(steps[-1]['errors'].values())<max(steps[0]['errors'].values())/50
        and result['fourier']['full_product_error']<1e-11
        and result['fourier']['full_product_jvp_error']<1e-11
        and np.array_equal(high[:2],[0.,0.]) and high[2]==-epsilon**2/2
        and projected_rank[0]==.25)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();result=run();result['seconds']=time.monotonic()-started
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,allow_nan=False))
    return 0 if result['implementation_checks_passed'] else 1


if __name__=='__main__':raise SystemExit(main())
