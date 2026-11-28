"""Consume an existing R643 dense column. No solve, root, field construction or FFT."""
import hashlib
import math
import time
import weakref
from fractions import Fraction
from pathlib import Path

import r658_actual_germ_normalization_thresholds_20261128 as old
import r663_actual_dense_denominator_intervals_20261128 as coef

I, mag, rat = coef.I, coef.mag, coef.rat
SCHEMA = 'R663-existing-86da-dense-finite-M25-denominator-v1'


BOUND_MODULES = (
    (old, '4ad46fbd5f25164522ecd195080e330f99ed1de543f26d84030e491d2d464e0c'),
    (coef, '756f517cc86f162348278ce280432d3fff72e3ccc9d59abb012e7a9fc51cd076'),
    (coef.iv, 'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f'),
    (coef.iv.original, '35060aa3e862c4852b30396493be37d1bd688281b4a093bd1e532d964e562631'))
for module, expected_sha in BOUND_MODULES:
    if hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() != expected_sha:
        raise ValueError('different published finite denominator consumer or interval arithmetic')
# Reuse genuine completed proofs only for the identical live source owner and requested precision.
FLAT_PROOFS = weakref.WeakKeyDictionary()
COLUMN_PROOFS = weakref.WeakKeyDictionary()


def dot(v, w):
    return v[0]*w[0]+v[1]*w[1]


def det(v, w):
    return v[0]*w[1]-v[1]*w[0]


def norm2(v):
    d = v[0]**2+v[1]**2
    if d.lo <= 0:
        raise ArithmeticError('positive nominal norm unresolved')
    return d


def act(a, x):
    return a[0]*x[0]+a[1]*x[1], a[2]*x[0]+a[3]*x[1]


def scaled(a, s):
    return tuple(v*s for v in a)


def add(v, w):
    return tuple(a+b for a,b in zip(v,w))


def sub(v, w):
    return tuple(a-b for a,b in zip(v,w))


def width(x, y):
    return mag(x-y)


def compare(v, q, bias):
    # The signed local angle has |atan(det/dot)| <= |det/dot| for positive dot.
    d = dot(v,q)
    if d.lo <= 0:
        raise ArithmeticError('orientation agreement unresolved')
    angle = mag(det(v,q)/d)
    radial = mag((coef.log(norm2(v))-coef.log(norm2(q)))/2+bias)
    return angle,radial


def jump(oldp, newp, b, lam, bias=I(0)):
    db, dl = compare(oldp,newp,bias)
    return (I(b)+db).hi,(I(lam)+dl).hi


def changed_chart(p, q, matrix, b, lam, bias=I(0)):
    if b >= .9:
        raise ArithmeticError('chart change requires a positive directional cone')
    t = I(-b,b)
    # cos(delta) multiplies p + tan(delta) Jp, with cos >= 1-b^2/2.
    cl = (1-I(b)**2/2).lo
    tn = t/I(cl,1)
    v = p[0]-p[1]*tn,p[1]+p[0]*tn
    db,dl = compare(act(matrix,v),q,bias+coef.log(I(cl,1)))
    return db,(I(lam)+dl).hi


def bridge(a, b, angle, radial, generator):
    span = width(a,b)
    mat = generator(coef.hull(a,b))
    # Frobenius norm bounded by the sum of the four absolute entries.
    n = sum((I(mag(x)) for x in mat), I(0))
    cost = n*span
    return (I(angle)+cost).hi,(I(radial)+cost).hi


def polynomial(ob, indices, factors):
    if (type(ob).__name__ != 'Dop853DenseOutput' or ob.F.shape != (7,len(ob.y_old))
            or float(ob.h)==0 or ob.t_old==ob.t):
        raise ValueError('existing native DOP853 dense step with seven coefficient rows required')
    fr = lambda x: Fraction.from_float(float(x))
    ratio = (fr(ob.t)-fr(ob.t_old))/fr(ob.h)
    out = []
    for i,scale in zip(indices,factors):
        p = [Fraction(0)]
        for n,row in enumerate(reversed(ob.F)):
            p[0] += fr(row[i])
            if n%2 == 0:
                p = [Fraction(0)] + p
            else:
                p = [p[0]] + [p[k]-p[k-1] for k in range(1,len(p))] + [-p[-1]]
        p[0] += fr(ob.y_old[i])
        p = [a*ratio**k*scale for k,a in enumerate(p)]
        jets = []
        for _ in range(4):
            jets.append([rat(v) for v in p])
            p = [k*p[k] for k in range(1,len(p))]
        out.append(jets)
    return out


def value(poly, s, derivative=0):
    v = []
    for component in poly:
        a = component[derivative]
        y = a[-1]
        for c in reversed(a[:-1]):
            y = c+s*y
        v.append(y)
    return tuple(v)


def intersect(x,y):
    return I(max(x.lo,y.lo),min(x.hi,y.hi))


class Column:
    def __init__(self, owner, j, forced, deadline, max_cells, rate):
        self.owner,self.j,self.mu,self.forced = owner,j,j*j,forced
        self.deadline,self.max_cells,self.rate = deadline,max_cells,rate
        self.examined=self.accepted=self.steps=0
        self.last = None
        self.guard=coef.check_profile(owner.par)
        self.cfrac=Fraction(self.mu,12500)
        self.c=rat(self.cfrac)
        self.prev=None
        self.b=self.lam=0.
        self.chart='flat'
        self.prevlog=I(0)

    def generator(self,x):
        if self.chart=='flat':
            return coef.flat(x,self.mu,self.c)
        if self.chart=='body':
            return coef.body(x,self.mu,self.guard)
        return coef.core(x,self.mu,self.guard)

    def tube(self, poly, t, h, l, r):
        if self.examined>=self.max_cells or time.monotonic()>=self.deadline:
            raise TimeoutError('budget ended at the last proved prefix')
        self.examined+=1
        s=I(l,r)
        dt=I(r)-l
        u=t+h*s
        M=scaled(self.generator(u),h)
        p=value(poly,s)
        res=sub(act(M,p),value(poly,s,1))
        if self.chart=='flat':
            # Taylor enclosure of Bp - p' about the exact dyadic midpoint.
            # It keeps the cancellation between the dense polynomial and the exact ODE.
            mid=(l+r)/2
            at=I(mid)
            dc=s-at
            center,dcenter,_=coef.flat_derivatives(t+h*at,self.mu,self.c)
            _,dall,ddall=coef.flat_derivatives(u,self.mu,self.c)
            pc=value(poly,at)
            mc,md=scaled(center,h),scaled(dcenter,h**2)
            r0=sub(act(mc,pc),value(poly,at,1))
            r1=sub(add(act(md,pc),act(mc,value(poly,at,1))),value(poly,at,2))
            r2=sub(add(add(act(scaled(ddall,h**3),p),
                           act(scaled(dall,2*h**2),value(poly,s,1))),
                       act(M,value(poly,s,2))),value(poly,s,3))
            res=tuple(intersect(a,b+dc*c+dc**2*d/2) for a,b,c,d in zip(res,r0,r1,r2))
        n=norm2(p)
        et,er=mag(det(p,res)/n),mag(dot(p,res)/n)
        D=(I(mag(M[0]-M[3]))+mag(M[1]+M[2])).hi
        # Only split on validated residual size; never accept a sample-based underestimate.
        if max(et,er) > (I(mag(h))*self.rate).lo:
            raise ArithmeticError('residual density requires subdivision')
        g=dot(p,act(M,p))/n
        trans=(M[0]+M[3]-2*g).hi
        candidate=min(.9,max(.00001,self.b*1.25+.00001))
        for _ in range(7):
            L=min(D,(I(trans)+2*I(D)*candidate).hi)
            E=coef.exp(I(L)*dt)
            source=I(et)*dt*coef.exp(I(max(0.,L))*dt)
            end=(E*self.b+source).hi
            # Constant majorant solution is monotone, so its maximum is at an endpoint.
            # For L<0 the source replacement et*h only bounds its endpoint.
            # The upper function exp(L*x)b+et*x is convex when L<0.
            whole=max(self.b,end)
            if whole<=candidate:
                self.lam=(I(self.lam)+dt*(I(er)+I(D)*whole)).hi
                self.b=end
                self.accepted+=1
                self.last={'chart':self.chart,'coordinate_interval':[u.lo,u.hi],
                           'angle_radius':self.b,'log_norm_radius':self.lam}
                return
            candidate=min(.9,max(candidate*1.5,whole*1.01))
        raise ArithmeticError('finite angular tube not self-consistent')

    def step(self, ob, poly):
        t,h=I(float(ob.t_old)),I(float(ob.t))-float(ob.t_old)
        stack=[(0.,1.,0)]
        while stack:
            l,r,depth=stack.pop()
            try:
                self.tube(poly,t,h,l,r)
            except ArithmeticError:
                if depth>=23:
                    raise
                m=(l+r)/2
                stack.extend([(m,r,depth+1),(l,m,depth+1)])
        self.steps+=1
        self.prev=value(poly,I(1))
        self.coord=I(float(ob.t))

    def chart_steps(self, dense, indices, factors, logscale, first):
        if (not hasattr(dense,'interpolants') or not dense.interpolants
                or len(dense.ts)!=len(dense.interpolants)+1):
            raise LookupError('missing native dense polynomial coefficients')
        for n,ob in enumerate(dense.interpolants):
            if (float(ob.t_old)!=float(dense.ts[n]) or float(ob.t)!=float(dense.ts[n+1])
                    or ((ob.t>ob.t_old) != (self.chart=='body'))):
                raise ValueError('disconnected or reversed native source step')
            poly=polynomial(ob,indices,factors)
            q=value(poly,I(0))
            if first is not None:
                self.b,self.lam=first(I(float(ob.t_old)),q)
                first=None
            else:
                if self.coord.lo!=float(ob.t_old) or self.coord.hi!=float(ob.t_old):
                    raise ValueError('source step endpoint gap on the same chart')
                self.b,self.lam=jump(self.prev,q,self.b,self.lam,self.prevlog-logscale)
            self.prevlog=logscale
            self.step(ob,poly)

    def run(self):
        obj=self.owner
        if not (getattr(obj.flat,'segments',None) and getattr(obj.forward,'sol',None) is not None
                and getattr(obj.raw_core,'sol',None) is not None):
            raise LookupError('original flat, forward and raw-core dense arrays required')
        def initial(t,q):
            if t.lo!=float(obj.flat.alpha):
                raise ValueError('source peak start differs')
            a,delta=coef.seed_alpha(t.lo,self.mu)
            z=coef.finite_initial_z(a,self.mu)
            size=I(120)*delta
            b,lam=compare((I(1),z*self.c),q,I(0))
            return (I(b)+size).hi,(I(lam)+size).hi
        key=(self.j,self.rate,float(obj.flat.alpha).hex(),float(obj.flat.display_log).hex())
        proof=FLAT_PROOFS.get(obj.flat,{}).get(key)
        if proof is None:
            extra=self.flat_chain(obj,initial)
            FLAT_PROOFS.setdefault(obj.flat,{})[key]=(self.prev,self.coord,self.prevlog,self.b,self.lam,extra)
            self.flat_reused=False
        else:
            self.prev,self.coord,self.prevlog,self.b,self.lam,extra=proof
            self.flat_reused=True
        return self.after_flat(obj,extra)

    def flat_chain(self,obj,initial):
        first=initial
        extra=0
        for low,high,dense,L in obj.flat.segments:
            if (float(dense.ts[0]),float(dense.ts[-1]))==(float(low),float(high)):
                if (self.j not in (18,20,22) or first is not initial or float(low)!=float(obj.flat.alpha)):
                    raise ValueError('unexpected extension outside the normalization path')
                extra+=1
                continue
            if (float(dense.ts[0]),float(dense.ts[-1]))!=(float(high),float(low)):
                raise ValueError('different flat normalization path')
            if first is initial and L!=0:
                raise ValueError('first peak requires unit amplitude')
            self.chart_steps(dense,(0,1),(1,self.cfrac),I(float(L)),first)
            first=None
        if first is not None or width(self.coord,I(2.5))>1e-12:
            raise ValueError('original numerical flat mouth is missing')
        # The analytic flat chart can be transported across the roundoff-size distance to 5/2.
        self.b,self.lam=bridge(self.coord,I(2.5),self.b,self.lam,self.generator)
        return extra

    def after_flat(self,obj,extra):
        self.chart='body'
        idx=(0,2 if self.forced else 1)
        def enter_body(t,q):
            u=I(2.5)
            r,e,_,_=coef.flat_parts(u,self.mu)
            w=coef.AMP*coef.exp(-u*(2-coef.sin(u)))
            k=w*r*u**2*e/((self.mu-1)*coef.ELL*self.c)
            gain=self.prevlog-I(float(obj.flat.display_log))+self.mu*coef.log(r)
            # First compare with q at the exact mouth using the same constant nominal q.
            b,lam=changed_chart(self.prev,q,(I(0),k,-w,k),self.b,self.lam,gain)
            if width(t,coef.R0)>1e-12:
                raise ValueError('wrong connector mouth')
            return bridge(coef.R0,t,b,lam,self.generator)
        self.chart_steps(obj.forward.sol,idx,(1,1),I(0),enter_body)
        def enter_core(x,q):
            rx=coef.core_r(x)
            if width(self.coord,rx)>1e-12:
                raise ValueError('wrong body-to-core switch')
            b,lam=bridge(self.coord,rx,self.b,self.lam,lambda r: coef.body(r,self.mu,self.guard))
            w=coef.body_slope(rx,self.guard)[0]
            return changed_chart(self.prev,q,(I(1),I(0),1/w,-1/w),b,lam)
        self.chart='core'
        self.chart_steps(obj.raw_core.sol,idx,(1,1),I(0),enter_core)
        if self.coord.lo!=0 or self.coord.hi!=0:
            raise ValueError('dense core does not reach the rim')
        k=1 if self.forced else 0
        observed=float(obj.raw_core_C[0] if self.forced else obj.Acore)
        # |e^{delta ell}R(delta theta)p-p| <= |p|[(e^lam-1)+e^lam*b].
        E=coef.exp(I(self.lam))
        n=coef.iv.sqrt_i(norm2(self.prev))
        sigma=(n*((E-1)+E*self.b)+mag(self.prev[k]-observed)).hi
        threshold=Fraction.from_float(abs(observed))/2
        return {'status':'completed_finite_denominator_bound','angle_radius':self.b,
                'log_norm_radius':self.lam,'finite_denominator_signed_observation':observed,
                'proved_absolute_error_upper':sigma,'threshold_met':Fraction.from_float(sigma)<=threshold,
                'unused_inward_extensions':extra,'same_live_flat_proof_reused':self.flat_reused}


def consume(existing_tail,response,paid_receipt,which,deadline,max_cells=600000,rate=0.0002):
    """Consume exactly one actual homogeneous column; deadline uses time.monotonic()."""
    requirements=old.live_thresholds(existing_tail,response,paid_receipt)
    if ((which!='forced_j4_C' and (type(which) is not int or which not in old.germ.MODES))
            or type(max_cells) is not int or max_cells<=0 or not 0<rate<=.01):
        raise ValueError('choose one actual mode A or forced_j4_C and a positive cell budget')
    if which=='forced_j4_C':
        j,forced,obj=4,True,existing_tail.model.old.old.forced
        row=requirements['additional_forced_boundary_observation']
        expected=row['actual_forced_j4_homogeneous_core_C_hex']
    else:
        j,forced=which,False
        obj=next(m for m in existing_tail.model.old.modes if int(m.mode)==j)
        row=requirements['same_actual_mode_precision_requirements'][str(j)]
        if float(obj.flat.display_log).hex()!=row['chosen_common_binary64_display_hex']:
            raise ValueError('different paid display gauge')
        expected=row['observed_abs_core_A_hex']
    col=Column(obj,j,forced,deadline,max_cells,rate)
    key=(which,expected,rate,float(obj.par.gain_height).hex(),float(obj.flat.display_log).hex())
    prior=COLUMN_PROOFS.get(obj,{}).get(key)
    try:
        result=col.run() if prior is None else dict(prior)
    except (TimeoutError,ArithmeticError,LookupError) as exc:
        result={'status':'unresolved_finite_denominator','reason':str(exc),'threshold_met':False,
                'last_complete_proved_prefix':col.last}
    if result.get('status')=='completed_finite_denominator_bound':
        observed=result['finite_denominator_signed_observation']
        if (observed if forced else abs(observed)).hex()!=expected:
            raise ValueError('different paid finite denominator')
        COLUMN_PROOFS.setdefault(obj,{})[key]=dict(result)
    comp=requirements['original_component']
    return {**result,'schema':SCHEMA,'column':which,'complete_native_steps':col.steps,
            'complete_column_proof_reused':prior is not None,
            'examined_continuous_cells':col.examined,'accepted_continuous_cells':col.accepted,
            'same_target_sha256':comp['same_target_sha256'],
            'actual_response_sha256':comp['actual_response_sha256'],
            'same_paid_tail_receipt_sha256':comp['consumed_R643_tail_receipt_sha256'],
            'same_source_contract_sha256':comp['source_contract_sha256'],
            'source_requirement':row,'seven_source_rows_retained':comp['seven_original_source_rows'],
            'other_source_errors_certified':False,'replayed_ODE_or_roots':0}


def archived_0d9a(literal_contract, paid_receipt):
    """Identify the actual published observation, with no path that recreates its missing arrays."""
    req=old.paid_0d9a_thresholds(literal_contract,paid_receipt)
    return {'schema':SCHEMA,'status':'DOP853_polynomials_absent_from_published_0d9a_FINAL',
            'actual_response_sha256':req['original_component']['actual_response_sha256'],
            'original_source_contract_sha256':req['original_component']['source_contract_sha256'],
            'original_log_FINAL_literal_bytes':661848,
            'original_log_FINAL_literal_sha256':'ccae718f0b0dea2f7ee8f81978bd2bab0a7c9df0e1831f0e4107b6436af78943',
            'extracted_FINAL_file_with_one_trailing_LF_bytes':661849,
            'extracted_FINAL_file_with_one_trailing_LF_sha256':'ff009a7930a544b5a48b575b3aa91e97aa4bf9af70ee478467f0f24b5d9b2d83',
            'completed_numerical_denominator_certificates':0,'replayed_ODE_or_roots':0,
            'seven_source_rows_retained':req['seven_source_rows_preserved']}
