"""PHI: first complete signed nonlocal phase pairing of the frozen NP trial.

Only the new functional and its full errors are evaluated.  Its exact
phase and PDE trial carriers are supplied by the immutable restorers.
"""
from fractions import Fraction as F
from math import factorial

OUTPUT_ORDER = (
    'complete_original_trial_phase_pairing',
    'complete_original_trial_phase_field_L1_upper',
    'complete_selected_trial_phase_field_difference_L1_upper',
    'complete_label_and_selected_background_phase_fee_upper',
    'complete_true_particular_phase_error_upper',
    'complete_true_strict_parameter_phase_enclosure',
)
SIGNED_INDICES = (0,5)


def require(ok,message):
    if not ok:raise ValueError(message)


def multiply_jets(a,b):
    return [sum((a[j]*b[k-j] for j in range(k+1)),a[0]*0) for k in range(4)]


def curvature_power_jets(jets,exponent,read_ball):
    k = [-read_ball(jets['K'+str(j) if j else 'K'])/factorial(j) for j in range(4)]
    require(k[0].lower() > 0 and exponent in (F(1,2),F(-1,2)), 'whole negative curvature denominator')
    base = k[0].sqrt() if exponent > 0 else 1/k[0].sqrt()
    s = base*0+exponent.numerator; s /= exponent.denominator
    r1,r2,r3 = (value/k[0] for value in k[1:])
    return [base,base*s*r1,base*(s*r2+s*(s-1)*r1*r1/2),
            base*(s*r3+s*(s-1)*r1*r2+s*(s-1)*(s-2)*r1**3/6)]


def whole_jet_field(c,core,row,left,right,evaluator):
    a,b = map(F,row['interval']);require(a <= left < right <= b,'one entire original scalar cell')
    values = evaluator(row['intrinsic_midpoint_jets'])[:3]+[evaluator(row['intrinsic_whole_third_jets'])[3]]
    centre,half = (a+b)/2,(b-a)/2;points = [];error = c.arb(0)
    for k,value in enumerate(values):
        x = float(value.mid());require(c.np.isfinite(x),'finite explicit scalar polynomial coefficient')
        delta = value-c.arb(x)
        error += max(abs(delta.lower()),abs(delta.upper()))*c.exact(half)**k
        points.append(c.Box(x))
    cs = c.affine_polynomial(points,(left+right)/2-centre,(right-left)/2)
    return core.BatchRadialFourier.scalar(c,cs,c.arb_box(error.upper()).hi)


def exact_phase_derivative(c,core,polynomial):
    require(len(polynomial) == 13 and all(len(p) == 129 for p in polynomial),
            'the whole original degree12 two-sided extent64 carrier')
    z = c.zeros((core.GRID,13,1))
    for k,p in enumerate(polynomial):
        for j,(re,im) in enumerate(p):
            mode = j-64
            if mode:z[mode % core.GRID,k,0] = c.CBox(c.box(-4*mode*im),c.box(4*mode*re))
    z[0,0,0] = c.CBox(1.)
    return core.BatchRadialFourier.from_fourier(c,z,64,0.,0)


def restrict_phase(c,core,phase,old_left,old_right,left,right):
    require(old_left <= left < right <= old_right,'the true phase polynomial coordinate')
    centre,half = (left+right)/2,(right-left)/2
    cs = c.affine_polynomial(phase.coefficients,(centre-old_left)/(old_right-old_left),half/(old_right-old_left))
    return core.BatchRadialFourier(c,cs,64,phase.norm,0.,0)


def box_to_ball(c,value):
    value = c.finite(value)
    require(value.lo.size == value.hi.size == 1,'one complete scalar result')
    return c.arb(float(value.lo.reshape(-1)[0])).union(c.arb(float(value.hi.reshape(-1)[0])))


def signed_mean_integral(c,core,value,length):
    """Exact angular trapezoid for the entire finite support, exact radial monomials."""
    require(2*value.degree < core.GRID,'every output mode precedes the alias threshold')
    total = c.Box(0.)
    for k,coefficient in enumerate(value.coefficients):
        if k % 2:continue
        mean = coefficient[0] if coefficient.lo.shape[0] == 1 else c.reduce_box(coefficient,axis=0)/core.GRID
        total = total+mean*c.box(length/F(k+1))
    error = c.mul_upper(value.error,c.box(length))
    total = total+c.Box(-error.hi,error.hi)
    return box_to_ball(c,total)


def direct_selected_field_difference(c,whole,wp_upper,read_ball):
    """Complete physical direct-nu field difference, not a PDE-source normalizer."""
    a,g,beta = (read_ball(whole[key]) for key in ('a','gamma','beta'))
    require(a.lower() > 0 and g.lower() > 0,'whole original positive metric denominators')
    abs_beta = max(abs(beta.lower()),abs(beta.upper()))
    T = (abs_beta/(2*a.lower()**2*g.lower()**2)).upper()
    d = c.exact(F(1,10**10));eps = c.exact(F(2,10**9));wp = wp_upper
    qm,qM,V,G,B = (c.exact(F(x)) for x in ('.5338','1.03','4','7','2'))
    ed,eh = d.exp(),(d/2).exp()
    k0 = qM*qM
    dK = k0*(ed-1)+d*ed*T*wp
    dT = T*(ed-1)
    dKn = dK+dT*wp
    Kn = k0+dK+T*ed*wp
    # I:L2->Linfinity <1/2, and the full angular suprema give L2 bounds.
    first = B*((2*V*eps+eps**2)*Kn+V*V*dKn)/2
    dq = dK/(2*qm)
    A0 = G*T/(2*qm)
    delta_A = A0*((eh-1)+eh*dq/qm)
    speed = wp*(A0*eh*eps+V*delta_A)
    return (first+speed).upper()


def state_selected_field_difference(c,old_H0):
    """PH.10--12 in the original NP whole L1L2 units, with both means."""
    eps,dk,qm,qM = (c.exact(F(x)) for x in ('2e-9','1.048e-7','.5338','1.03'))
    dq = dk/(2*qm)
    coefficient = 2*(eps+qM*qM*eps+4*dk)+c.exact(F('4e-10'))*qM+7*dq
    return (coefficient*old_H0).upper()


class Integrator:
    def __init__(self,c,core,nu,base,offsets,rows,nodes,plan,jets,read_ball):
        self.c,self.core,self.nu = c,core,nu
        self.base,self.offsets,self.rows,self.nodes,self.plan,self.jets = base,offsets,rows,nodes,plan,jets
        self.read_ball = read_ball;self.position = 0;self.cursor = F(0)
        self.signed = c.arb(0);self.forcing = c.arb(0);self.direct_difference = c.arb(0)
        self.cells = 0;self.trial_cache = {};self.max_output_degree = 0

    def consume(self,phase_left,phase_right,phase_polynomial):
        c,core,nu = self.c,self.core,self.nu
        require(phase_left == self.cursor,'one whole chronological new pairing prefix')
        phase = exact_phase_derivative(c,core,phase_polynomial)
        left = phase_left
        while left < phase_right:
            while F(self.plan[self.position]['interval'][1]) <= left:self.position += 1
            item = self.plan[self.position];pl,pr = map(F,item['interval'])
            right = min(pr,phase_right);require(pl <= left < right <= pr,'complete NP/common-phase intersection')
            row = self.rows[item['row']]
            scalar = {name:core.scalar_taylor(c,row['intrinsic_midpoint_jets'],row['intrinsic_whole_third_jets'],
                name,*row['interval'],left,right,self.read_ball) for name in ('beta','K','gamma','s')}
            u,v = nu.base_background(c,core,self.base,self.offsets,item['background_piece'],left,right,scalar['s'])
            ti = item['trial_piece']
            if ti not in self.trial_cache:
                values_l = [c.Box(self.jets[k][ti,:,None]) for k in range(4)]
                values_r = [c.Box(self.jets[k][ti+1,:,None]) for k in range(4)]
                self.trial_cache = {ti:core.hermite_coefficients(c,values_l,values_r,c.exact(self.nodes[ti+1]-self.nodes[ti]))}
            cs = core.restrict_trial_coefficients(c,self.trial_cache[ti],c.exact(self.nodes[ti]),
                c.exact(self.nodes[ti+1]-self.nodes[ti]),left,right)
            h1,h2 = core.reflection_polynomial(c,cs)
            beta,K,gamma = (scalar[name] for name in ('beta','K','gamma'))
            q = whole_jet_field(c,core,row,left,right,
                lambda jets:curvature_power_jets(jets,F(1,2),self.read_ball))
            fd = 2*beta*(u*h1+K*v*h2).primitive()-gamma*q*h2.mean()
            if left >= nu.A:
                w,wp = nu.control_fields(c,core,left,right)
                T = nu.metric_T_taylor(c,core,row,left,right,self.read_ball)
                Tq = whole_jet_field(c,core,row,left,right,lambda jets:multiply_jets(
                    nu.metric_T_jets(jets,self.read_ball),curvature_power_jets(jets,F(-1,2),self.read_ball)))
                fd = fd+beta*(v*v).primitive()*(-w*K+T*wp)+gamma*v.mean()*Tq*wp*F(1,2)
                wp_upper = box_to_ball(c,c.add_upper(wp.norm,wp.error)).upper()
                self.direct_difference += c.exact(right-left)*direct_selected_field_difference(
                    c,row['intrinsic_whole_third_jets'],wp_upper,self.read_ball)
            else:
                require(right <= nu.A,'the original compact seam must not be crossed')
            a = restrict_phase(c,core,phase,phase_left,phase_right,left,right)
            integrand = 2*a*a*fd
            require(fd.degree <= 128 and integrand.degree <= 256,'all complete original functional products')
            self.max_output_degree = max(self.max_output_degree,integrand.degree)
            self.signed += signed_mean_integral(c,core,integrand,right-left)
            self.forcing += c.exact(right-left)*box_to_ball(c,c.add_upper(fd.norm,fd.error)).upper()
            self.cells += 1;left = right
        self.cursor = phase_right

    def prefix(self,record):
        return {'kind':'PHI_complete_new_phase_integral_prefix_v1','exact_interval':['0',str(self.cursor)],
            'complete_new_intersections':self.cells,'maximum_complete_output_degree':self.max_output_degree,
            'signed_trial_integral':record(self.signed,'signed_enclosure'),
            'whole_forcing_L1_upper':record(self.forcing.upper(),'upper'),
            'whole_direct_selected_field_difference_L1_upper':record(self.direct_difference.upper(),'upper'),
            'all_new_cells_and_scalar_remainders_retained':True}


def finish(c,integrator,old_H0,old_error,publish):
    require(integrator.cursor == F(9,50) and integrator.position == len(integrator.plan)-1,
            'the entire exact requested phase integral')
    signed = publish(OUTPUT_ORDER[0],integrator.signed,'signed_enclosure')
    forcing = publish(OUTPUT_ORDER[1],integrator.forcing.upper(),'upper')
    changed = publish(OUTPUT_ORDER[2],(integrator.direct_difference
        +state_selected_field_difference(c,old_H0)).upper(),'upper')
    label = c.exact(F('3.521e-5'));phase_size = c.exact(F(11,10))
    fee = publish(OUTPUT_ORDER[3],(2*(label*forcing+phase_size**2*changed)).upper(),'upper')
    pde = publish(OUTPUT_ORDER[4],(c.exact(F(3,2))*old_error).upper(),'upper')
    total = (fee+pde).upper()
    publish(OUTPUT_ORDER[5],signed+c.arb(0,total),'signed_enclosure')
