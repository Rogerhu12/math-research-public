"""Material-angle pullback for a design initial guess, never a solved map.

The old and new angular charts differ when q changes. Pull back the complete
old perturbation, including its exact-core reference lift, before projecting.
An optional secant combines two previously accepted normalized perturbations.
All equations, root guards, Jacobians and solver tolerances are untouched.
"""
import hashlib
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly, CubicSpline


def values_at(coefficients, psi, mode, M):
    c = coefficients.T
    phase = psi[:, :, None] * (mode * np.arange(1, M + 1))[None, None, :]
    co, si = np.cos(phase), np.sin(phase)
    R = c[:, 0, None] + np.einsum('npk,nk->np', co, c[:, 1:M+1])
    T = np.einsum('npk,nk->np', si, c[:, M+1:2*M+1])
    Z = np.einsum('npk,nk->np', co, c[:, 2*M+1:])
    return np.stack((R*np.cos(psi)-T*np.sin(psi),
                     R*np.sin(psi)+T*np.cos(psi), Z), axis=-1)


def restart(obj, BVP, records, settings, chart):
    from fixed_metric_mode3_bvp import merge_profile_mesh
    if obj.fixed or any(r['config']['fixed_metric'] for r in records):
        raise ValueError('This explicit initial-guess helper currently supports design records only')
    if len(records) not in (1, 2):
        raise ValueError('One warm record or two secant records required')
    current_settings = dict(settings)
    old = []
    for rec in records:
        if rec['config']['base_mode'] != 4 or not rec['config']['exact_core_lift']:
            raise ValueError('Expected actual n4 exact-core-lift record')
        if not rec['solver_success']:
            raise ValueError('A predictor may only use previously accepted records')
        for k, v in obj.cfg.items():
            if k != 'delta' and rec['profile'].get(k) != v:
                raise ValueError('Profile family changed at '+k)
        if rec['physical_port']['parameters'] != obj.port['parameters']:
            raise ValueError('Physical tail parameters changed')
        settings.clear(); settings.update(rec['plateau_settings'])
        q = float(rec['gauge_amplitude']); M = int(rec['config']['modes'])
        previous = BVP(rec['profile'], rec['physical_port'], q, M,
                       rec['config']['angular'], False, q)
        previous.pscale = np.asarray(rec['central_correction_scales'])
        previous.bcweights = np.full(M, .01)
        p = np.asarray(rec['parameters']); initial = previous.initial(p).copy()
        f = previous.flow(p[0])
        mesh = np.asarray(rec['mesh'])
        pp = PPoly.construct_fast(np.asarray(rec['pp_coefficients']), mesh,
                                 extrapolate=True, axis=1)
        Nlift = max(4096, 128*M)
        f.geo(np.array([0.]), Nlift)
        lift = f.exact_lift_cache[Nlift][0]
        spline = CubicSpline(np.linspace(0., 2*np.pi, Nlift+1),
                             np.concatenate((lift, lift[:1])), bc_type='periodic')
        old.append(dict(rec=rec, obj=previous, f=f, p=p, pp=pp, q=q, M=M,
                        initial=initial, lift=spline, mesh=mesh))
    settings.clear(); settings.update(current_settings)
    latest = old[-1]; ratio = obj.q/latest['q']
    par = np.zeros(obj.M)
    latest_delta = latest['rec']['profile']['delta'] + latest['p'][0]
    if len(old) == 1:
        par[0] = (latest_delta-latest['rec']['profile']['delta'])*ratio**2 + latest['rec']['profile']['delta']-obj.cfg['delta']
        for j in range(1, min(obj.M, latest['M'])):
            par[j] = latest['p'][j]*latest['obj'].pscale[j-1]*ratio**(j+1)/obj.pscale[j-1]
        weights = [1.]
    else:
        before = old[0]
        if not before['q'] < latest['q'] or before['rec']['plateau_settings'] != latest['rec']['plateau_settings']:
            raise ValueError('Secant requires ordered q on the same core homotopy family')
        factor = (obj.q-latest['q'])/(latest['q']-before['q'])
        factor2 = (obj.q**2-latest['q']**2)/(latest['q']**2-before['q']**2)
        before_delta = before['rec']['profile']['delta'] + before['p'][0]
        par[0] = latest_delta + factor2*(latest_delta-before_delta)-obj.cfg['delta']
        for j in range(1, min(obj.M, latest['M'])):
            last = latest['p'][j]*latest['obj'].pscale[j-1]/latest['q']
            first = before['p'][j]*before['obj'].pscale[j-1]/before['q'] if j<before['M'] else 0.
            par[j] = obj.q*((1+factor)*last-factor*first)/obj.pscale[j-1]
        weights = [-factor, 1+factor]
    obj.initial(par); f = obj.flow(par[0])
    t = latest['obj'].inverse_chart(latest['mesh'], latest['p'][0])
    angular_breaks = obj.inverse_chart(np.r_[chart['knots'], .75]*f.end, par[0])
    t = merge_profile_mesh(t, np.unique(np.r_[obj.chart_breaks, angular_breaks]))
    s = obj.chart(t, par[0])[0]
    N = max(2048, 64*max([obj.M]+[v['M'] for v in old]))
    B = f.basis(N)[0]
    y = np.empty((obj.n, len(t))); pullback_residual = 0.
    for first in range(0, len(t), 24):
        sl = slice(first, first+24)
        g = f.geo(s[sl], N); theta = g['theta']
        target = np.zeros((len(s[sl]), N, 3))
        for weight, v in zip(weights, old):
            sold = v['obj'].chart(t[sl], v['p'][0])[0]
            e = v['f'].geo(sold, 1)['e'][:, None]
            psi = theta.copy()
            for _ in range(40):
                update = (psi-e*np.sin(4*psi)/4-theta)/(1-e*np.cos(4*psi))
                psi -= update
                if float(np.max(abs(update))) < 2e-14: break
            residual = float(np.max(abs(psi-e*np.sin(4*psi)/4-theta)))
            pullback_residual = max(pullback_residual, residual)
            if residual > 1e-12: raise FloatingPointError('Material pullback failed')
            V = v['q']*values_at(v['pp'](sold), psi, 4, v['M'])
            u = np.clip((sold-.5*v['f'].prefix_end)/(.4*v['f'].prefix_end),0.,1.)
            h = v['f'].profile(sold)[0]*(1-u**3*(10-15*u+6*u*u))
            # This spline is only a predictor. The solver evaluates its own
            # exact reference core and all its derivatives after initialization.
            V += h[:,None,None]*v['lift'](np.mod(psi,2*np.pi))
            target += weight*V/v['q']
        base = np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
        base *= f.profile(s[sl])[0][:,None,None]
        target -= (g['pos']-base)/obj.q
        y[:,sl] = f.project(target,B)
    before_bc = float(np.max(abs(obj.bc(y[:,0],y[:,-1],par))))
    correction = obj.initial(par)-y[:,0]
    cutoff = (f.Tu if f.direction=='outward' else f.Td)/2
    y += correction[:,None]*np.maximum(0.,1-s/cutoff)[None,:]**3
    result = dict(method='physical-material-angle-pullback-of-full-reference-plus-field',
                  scope='Initial guess only; no equation, root guard or acceptance change.',
                  q_inputs=[v['q'] for v in old], q_target=obj.q,
                  secant_weights=weights, radial_nodes=len(t), angular_projection=N,
                  pullback_residual=pullback_residual,
                  predicted_physical_delta=obj.cfg['delta']+par[0],
                  maximum_inlet_coefficient_correction=float(np.max(abs(correction))),
                  scaled_bc_before_inlet_repair=before_bc,
                  scaled_bc_after_inlet_repair=float(np.max(abs(obj.bc(y[:,0],y[:,-1],par)))),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  old_reference_lift_evaluation='Periodic cubic interpolation of 4096 or more exact reference samples, solely for the warm guess.')
    if len(old)==1 and obj.q==latest['q'] and obj.M==latest['M'] and current_settings==latest['rec']['plateau_settings']:
        reference=latest['pp'](latest['obj'].chart(t,latest['p'][0])[0])
        result['same_chart_identity_max_coefficient_difference']=float(np.max(abs(y-reference)))
    return t,y,par,result
