#!/usr/bin/env python3
"""Actual fixed-E mean, complete connection and position derivative chain.

This is new pure source for a later declared public Actions scope. There is
no incoming q, execution request, optimizer or automatically chosen branch.
Every root uses ONE caller-declared angular functional, independently of
the output/position grid. The frozen target is evaluated only from the
literal reference height. Trial heights never redefine it.

Floating root brackets, derivative signs and angular values below are
observations. They are NOT whole-bracket interval certificates, exact
continuous means or full README certificates. Their unresolved errors are
returned. In particular a sign change of the pointwise C is not a reason to
divide by C; only the actual mean coefficient enters the scalar implicit
chain, and its sign may be either sign on the declared reference branch.
"""
from collections import defaultdict
import os
import numpy as np

COUNTS = defaultdict(int)
JET_KEYS = ('f','fr','frr','ft','ftt','frt')


def public_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('fixed-E science requires a declared public Actions scope')


def _jets(jets):
    result = {key:np.asarray(jets[key],dtype=float) for key in JET_KEYS}
    shape = result['f'].shape
    if len(shape) != 1 or any(value.shape != shape for value in result.values()):
        raise ValueError('all six actual jets on one angular axis required')
    if any(not np.all(np.isfinite(value)) for value in result.values()):
        raise ArithmeticError('nonfinite actual height jet')
    return result


def _root(evaluate, left, right, sign, seed, steps, tolerance, count_name):
    """Safeguarded scalar root in the supplied reference component.

    This deliberately does not search another branch when the supplied
    bracket, positive domain or reference derivative sign fails. Endpoint
    and every attempted-point signs are recorded observations, not an
    assertion about unseen interior points. A later interval branch receipt
    must enclose the entire bracket before claiming continuous uniqueness.
    """
    if not (np.isfinite(left) and np.isfinite(right) and left <= right
            and sign in (-1,1) and steps > 0 and tolerance > 0):
        raise ValueError('explicit finite same-branch root contract required')
    def call(x):
        COUNTS[count_name] += 1
        value, derivative, payload = evaluate(float(x))
        if not (np.isfinite(value) and np.isfinite(derivative) and sign*derivative > 0):
            raise ArithmeticError('declared reference mean-root branch lost its derivative sign')
        return float(value),float(derivative),payload
    fl,dl,pl = call(left)
    if fl == 0:
        return left,pl,{'iterations':0,'residual':fl,'derivative':dl,'bracket':[left,right]}
    fr,dr,pr = call(right)
    if fr == 0:
        return right,pr,{'iterations':0,'residual':fr,'derivative':dr,'bracket':[left,right]}
    if sign*fl > 0 or sign*fr < 0:
        raise ArithmeticError('same-branch endpoints do not bracket the actual mean root')
    x = min(max(float(seed),left),right)
    for iteration in range(steps):
        f,d,payload = call(x)
        if f == 0 or (right-left <= tolerance*(1+abs(x))):
            return x,payload,{'iterations':iteration+1,'residual':f,'derivative':d,
                              'bracket':[left,right]}
        if sign*f < 0:
            left,fl = x,f
        else:
            right,fr = x,f
        candidate = x-f/d
        if not (left < candidate < right):
            candidate = left+(right-left)/2
        if candidate == x:
            # The residual is retained; no root-error certificate is inferred
            # from the finite arithmetic failing to move another float.
            return x,payload,{'iterations':iteration+1,'residual':f,'derivative':d,
                'bracket':[left,right],'floating_step_resolution_reached':True}
        x = candidate
    raise ArithmeticError('same-branch scalar root exhausted its declared iterations')


def frozen_reference_metric(r, W, W_r, reference_jets, *, inner_chart,
                            root_steps, root_tolerance, target_sha256):
    """Evaluate the SAME reference-root E and E_r, never a trial's metric.

    e-1 is stored directly. On the true inner chart, (e-1)/W^2 is the
    numerical unknown and the turning equation is rationalized before any
    division by W^2. This avoids forming E-1 or subtracting two unit-sized
    turning values. In the core E is kept split as W^2+e throughout u.
    """
    public_only()
    j = _jets(reference_jets)
    r,W,W_r = float(r),float(W),float(W_r)
    if not (r > 0 and W > 0 and np.isfinite(W_r)):
        raise ArithmeticError('positive finite frozen W and positive radius required')
    q,t,fr = j['ft'],j['ftt'],j['fr']
    b2 = r*r-q*q
    if np.any(b2 <= 0):
        raise ArithmeticError('frozen reference angular graph left its positive domain')
    b = np.sqrt(b2)
    p = -W+fr
    if inner_chart:
        w2 = W*W
        if w2 == 0:
            raise ArithmeticError('inner chart requires higher precision; W^2 underflowed')
        v = fr/W
        nbar = (q/W)**2/(b*(r+b))+r*r*(v-1)*(t/W)/b**3
        shiftbar = -2*v+v*v+(v-1)**2*q*q/b2
        nminus = w2*nbar
        B = 2*nbar+w2*nbar*nbar+shiftbar
        def evaluate(z):
            u2 = 1+w2*(z-shiftbar)
            N = 1+nminus
            if np.any(u2 <= 0) or np.any(N <= 0):
                raise ArithmeticError('same frozen inner root bracket lost positivity')
            u = np.sqrt(u2)
            value = np.mean((B-z)/(u*(N+u)))
            derivative = -.5*np.mean(N/u**3)
            return value,derivative,{'u':u,'N':N}
        z,payload,receipt = _root(evaluate,float(np.min(B)),float(np.max(B)),
            -1,float(np.mean(B)),root_steps,root_tolerance,'frozen_reference_root_evaluations')
        eta,eta_inner = w2*z,z
    else:
        nminus = q*q/(b*(r+b))+r*r*p*t/b**3
        shift = -2*W*fr+fr*fr+p*p*q*q/b2
        B = 2*nminus+nminus*nminus+shift
        def evaluate(eta):
            u2 = 1+eta-shift
            N = 1+nminus
            if np.any(u2 <= 0) or np.any(N <= 0):
                raise ArithmeticError('same frozen reference root bracket lost positivity')
            u = np.sqrt(u2)
            return np.mean((B-eta)/(u*(N+u))),-.5*np.mean(N/u**3),{'u':u,'N':N}
        eta,payload,receipt = _root(evaluate,float(np.min(B)),float(np.max(B)),
            -1,float(np.mean(B)),root_steps,root_tolerance,'frozen_reference_root_evaluations')
        eta_inner = None
    e,E = 1+eta,W*W+1+eta
    u,N = payload['u'],payload['N']
    across = j['frt']-q/r
    C = E*t+r*p
    M = r+p*t-q*q/r
    K = (e+W*fr)*t+r*fr-W*q*q/r
    omega = r*r/(u**3*b**3)
    At = C*j['frr']-E*across*across-W_r*K
    e_r = 2*np.mean(omega*At)/np.mean(N/u**3)
    c0 = np.mean(omega*C)
    if not (np.isfinite(e_r) and np.isfinite(c0) and c0 != 0):
        raise ArithmeticError('frozen reference mean branch is unresolved')
    COUNTS['frozen_reference_radial_points'] += 1
    COUNTS['frozen_reference_angular_points'] += len(q)
    return {'target_sha256':target_sha256,'r':r,'W':W,'W_r':W_r,
        'eta':float(eta),'eta_inner':None if eta_inner is None else float(eta_inner),
        'e':float(e),'e_r':float(e_r),'E':float(E),
        'E_r':float(2*W*W_r+e_r),'inner_chart':bool(inner_chart),
        'reference_mean_derivative':float(c0),'reference_branch_sign':1 if c0 > 0 else -1,
        'root_receipt':receipt,'angular_functional_points':len(q),
        'root_angular_radial_DtN_ODE_and_roundoff_errors_enclosed':False,
        'continuous_target_definition_not_replaced_by_node_table':True}


def geometry_from_split(target, jets, x, chart):
    """Actual p0=-W+s with stable lambda/shift/zeta coordinates."""
    j = _jets(jets)
    r,W,E = target['r'],target['W'],target['E']
    q,t,fr = j['ft'],j['ftt'],j['fr']
    b2 = r*r-q*q
    if np.any(b2 <= 0):
        raise ArithmeticError('trial angular graph lost positivity')
    b = np.sqrt(b2)
    if chart == 'lambda':
        if not target['inner_chart'] or target['eta_inner'] is None:
            raise ValueError('lambda requires the same rationalized frozen inner target')
        w2 = W*W
        v = float(x)+fr/W
        s,d,p = W*float(x),W*v,W*(v-1)
        nbar = (q/W)**2/(b*(r+b))+r*r*(v-1)*(t/W)/b**3
        ubar = target['eta_inner']+2*v-v*v-(v-1)**2*q*q/b2
        nminus,u2 = w2*nbar,1+w2*ubar
        numerator = 2*nbar+w2*nbar*nbar-ubar
        coordinate_scale,residual_scale = W,w2
    elif chart in ('shift','zeta'):
        coordinate_scale = 1. if chart == 'shift' else 1./W
        s = coordinate_scale*float(x)
        d = s+fr
        p = -W+d
        if chart == 'zeta':
            v = float(x)+W*fr
            u_delta = target['eta']+2*v-(v/W)**2-p*p*q*q/b2
        else:
            u_delta = target['eta']+2*W*d-d*d-p*p*q*q/b2
        nminus = q*q/(b*(r+b))+r*r*p*t/b**3
        u2 = 1+u_delta
        numerator = 2*nminus+nminus*nminus-u_delta
        residual_scale = 1.
    else:
        raise ValueError('declared mean chart must be lambda, shift or zeta')
    N = 1+nminus
    if np.any(u2 <= 0) or np.any(N <= 0):
        raise ArithmeticError('trial left the same positive turning component')
    u = np.sqrt(u2)
    C = E*t+r*p
    omega = r*r/(u**3*b**3)
    c0 = np.mean(omega*C)
    if chart == 'lambda':
        derivative = np.mean(omega*(E*(t/W)+r*(v-1)))
    elif chart == 'zeta':
        derivative = c0/W
    else:
        derivative = c0
    value = np.mean(numerator/(u*(N+u)))
    return {'target':target,'jets':j,'x':float(x),'chart':chart,
        's':float(s),'d':d,'p0':-W+s,'p':p,'q':q,'t':t,
        'b':b,'u':u,'N':N,'E':E,'C':C,'omega':omega,
        'B':j['frt']-q/r,'M':r+p*t-q*q/r,
        'mean_derivative':float(c0),'root_value':float(value),
        'root_coordinate_derivative':float(derivative),
        'coordinate_scale':coordinate_scale,'root_residual_scale':residual_scale}


def _connection(state, s_r):
    t = state['target']; j = state['jets']
    r,W,Wr,e,er,E = [t[k] for k in ('r','W','W_r','e','e_r','E')]
    K = (e+W*state['d'])*state['t']+r*state['d']-W*state['q']**2/r
    Q = E*state['B']**2+Wr*K+er*state['M']/2-state['C']*j['frr']
    if s_r is None:
        c0 = state['mean_derivative']
        if c0 == 0 or not np.isfinite(c0):
            raise ArithmeticError('actual mean coefficient vanished')
        s_r = np.mean(state['omega']*Q)/c0
    D = (state['C']*(s_r+j['frr'])-E*state['B']**2-Wr*K-er*state['M']/2)
    result = dict(state)
    result.update(K=K,Q=Q,s_r=float(s_r),p0_r=-Wr+float(s_r),D=D,R=state['omega']*D)
    if not np.all(np.isfinite(result['R'])):
        raise ArithmeticError('nonfinite actual fixed-E connection')
    return result


def solve_mean(target, jets, *, chart, bracket, seed, root_steps, root_tolerance):
    public_only()
    def evaluate(x):
        state = geometry_from_split(target,jets,x,chart)
        return state['root_value'],state['root_coordinate_derivative'],state
    x,state,receipt = _root(evaluate,float(bracket[0]),float(bracket[1]),
        target['reference_branch_sign'],seed,root_steps,root_tolerance,
        'trial_mean_root_evaluations')
    result = _connection(state,None)
    result['root_receipt'] = receipt
    result['same_target_sha256'] = target['target_sha256']
    result['mean_connection_residual_observation'] = float(np.mean(result['R']))
    result['continuous_mean_branch_or_errors_certified'] = False
    COUNTS['trial_mean_radial_points'] += 1
    COUNTS['trial_mean_angular_points'] += len(state['p'])
    return result


def state_on_output_grid(mean_state, output_jets):
    """Use the already solved SAME p0/p0_r; output N never changes the mean."""
    public_only()
    state = geometry_from_split(mean_state['target'],output_jets,
                                mean_state['x'],mean_state['chart'])
    result = _connection(state,mean_state['s_r'])
    result['mean_functional_points'] = len(mean_state['p'])
    result['output_mean_a_minus_one_observation'] = float(np.mean(result['N']/result['u'])-1)
    result['output_mean_R_alias_observation'] = float(np.mean(result['R']))
    COUNTS['output_radial_angular_points'] += len(state['p'])
    return result


def _free_geometry_direction(state,H,ds):
    t = state['target']; r = t['r']
    p,q,a,b,u = [state[k][:,None] for k in ('p','q','t','b','u')]
    dp = H['fr']+ds[None,:]
    db = -q*H['ft']/b
    du = -r*r*p*dp/(u*b*b)-r*r*p*p*q*H['ft']/(u*b**4)
    dN = (r*q*H['ft']/b**3+r*r*(a*dp+p*H['ftt'])/b**3
          +3*r*r*p*a*q*H['ft']/b**5)
    return dp,db,du,dN


def _direction_connection(state,H,ds,dsr=None):
    t = state['target']; r,W,Wr,e,er,E = [t[k] for k in ('r','W','W_r','e','e_r','E')]
    dp,db,du,dN = _free_geometry_direction(state,H,ds)
    p,q,a,b,u,N = [state[k][:,None] for k in ('p','q','t','b','u','N')]
    C,B,M,omega,Q,D = [state[k][:,None] for k in ('C','B','M','omega','Q','D')]
    dC = E*H['ftt']+r*dp
    dB = H['frt']-H['ft']/r
    dM = a*dp+p*H['ftt']-2*q*H['ft']/r
    dK = W*dp*a+(e+W*state['d'])[:,None]*H['ftt']+r*dp-2*W*q*H['ft']/r
    dw = -3*omega*(du/u+db/b)
    dQ = (2*E*B*dB+Wr*dK+er*dM/2-dC*state['jets']['frr'][:,None]-C*H['frr'])
    if dsr is None:
        dc0 = np.mean(dw*C+omega*dC,axis=0)
        dsr = (np.mean(dw*Q+omega*dQ,axis=0)-state['s_r']*dc0)/state['mean_derivative']
    dD = (dC*(state['s_r']+state['jets']['frr'])[:,None]
          +C*(dsr[None,:]+H['frr'])-2*E*B*dB-Wr*dK-er*dM/2)
    return {'s':ds,'s_r':dsr,'p':dp,'b':db,'u':du,'N':dN,
        'a':dN/u-N*du/u**2,'R':dw*D+omega*dD,'D':dD,
        'E':np.zeros_like(ds),'E_r':np.zeros_like(ds)}


def mean_direction(mean_state, direction_jets):
    """Complete R618 implicit mean AND mean-radial parameter derivative."""
    public_only()
    H = {key:np.asarray(direction_jets[key],dtype=float) for key in JET_KEYS}
    shape = H['f'].shape
    if len(shape) != 2 or shape[0] != len(mean_state['p']) or any(x.shape != shape for x in H.values()):
        raise ValueError('complete six-jet directions on the SAME mean grid required')
    _,_,du,dN = _free_geometry_direction(mean_state,H,np.zeros(shape[1]))
    u,N = mean_state['u'][:,None],mean_state['N'][:,None]
    ds = -np.mean(dN/u-N*du/u**2,axis=0)/mean_state['mean_derivative']
    result = _direction_connection(mean_state,H,ds,None)
    result['turning_linearized_residual_observation'] = np.mean(result['a'],axis=0)
    result['connection_linearized_residual_observation'] = np.mean(result['R'],axis=0)
    COUNTS['mean_analytic_columns_at_radii'] += shape[1]
    COUNTS['mean_analytic_direction_angular_points'] += int(np.prod(shape))
    return result


def output_direction(output_state, direction_jets, actual_mean_direction):
    public_only()
    H = {key:np.asarray(direction_jets[key],dtype=float) for key in JET_KEYS}
    result = _direction_connection(output_state,H,
        actual_mean_direction['s'],actual_mean_direction['s_r'])
    COUNTS['output_analytic_direction_angular_points'] += int(H['f'].size)
    return result


def position_state(state,theta,primitive):
    public_only()
    b,u,N,p,q = [state[k] for k in ('b','u','N','p','q')]
    E,r = state['E'],state['target']['r']
    pi = lambda x: primitive@x
    a = N/u
    psi = theta+np.pi/2+pi(a-1)
    T = np.stack([np.cos(psi),np.sin(psi)],axis=1)
    JT = np.stack([-T[:,1],T[:,0]],axis=1)
    pir = pi(state['R'])
    Wstar = pi(b[:,None]*pir[:,None]*JT)
    v = -p*q/b
    pred = v[:,None]*T-u[:,None]*JT
    Yr = pred+Wstar
    Y,Yt = pi(b[:,None]*T),b[:,None]*T
    br = (r-q*state['jets']['frt'])/b
    ut = (-r*r*p*state['jets']['frt']/(u*b*b)
          -r*r*p*p*q*state['t']/(u*b**4))
    psir = (v*a-ut)/b+pir
    Yrt = br[:,None]*T+(b*psir)[:,None]*JT
    bt = -q*state['t']/b
    Ytt = bt[:,None]*T+(b*a)[:,None]*JT
    de = (2*np.sum(Wstar*pred,axis=1)+np.sum(Wstar*Wstar,axis=1))/E
    fc = b*np.sum(Wstar*T,axis=1)/(r*np.sqrt(E))
    eta = (abs(de)+np.sqrt(de*de+4*fc*fc))/2
    alternating = (-1.)**np.arange(len(theta))
    return {'primitive':primitive,'T':T,'JT':JT,'pir':pir,'Wstar':Wstar,
        'S':Wstar/np.sqrt(E),'Y':Y,'Yr':Yr,'Yt':Yt,'Yrt':Yrt,'Ytt':Ytt,
        'eta':eta,'outward_ratio':-np.sum(Yr*JT,axis=1)/u,
        'angular_closure_observation':np.mean(Yt,axis=0),
        'output_mean_a_minus_one_observation':float(np.mean(a)-1),
        'output_mean_R_alias_observation':float(np.mean(state['R'])),
        'output_Nyquist_a_minus_one_observation':float(np.mean((a-1)*alternating)),
        'output_Nyquist_R_observation':float(np.mean(state['R']*alternating)),
        'S_to_eta_and_derivative_jets_are_conditional_identity_observations':True,
        'same_root_mean_and_both_primitive_alias_errors_already_paid':False,
        'actual_metric_qualification_requires_direct_position_and_angular_error_readout':True,
        'same_mean_and_fixed_E_used':True,'continuous_position_error_certified':False}


def position_direction(state,position,direction):
    """Both primitives and the off-solution phase/weight terms, dE=0."""
    public_only()
    pi = lambda x: position['primitive']@x
    dpsi,dpir = pi(direction['a']),pi(direction['R'])
    b,pir = state['b'][:,None],position['pir'][:,None]
    common = direction['b']*pir+b*dpir
    phase = b*pir*dpsi
    answer = np.stack([pi(common*position['JT'][:,k,None]
                -phase*position['T'][:,k,None])/np.sqrt(state['E'])
                for k in range(2)],axis=1)
    if not np.all(np.isfinite(answer)):
        raise ArithmeticError('nonfinite complete fixed-E actual-position derivative')
    COUNTS['complete_position_direction_angular_points'] += int(answer.size)
    return answer
