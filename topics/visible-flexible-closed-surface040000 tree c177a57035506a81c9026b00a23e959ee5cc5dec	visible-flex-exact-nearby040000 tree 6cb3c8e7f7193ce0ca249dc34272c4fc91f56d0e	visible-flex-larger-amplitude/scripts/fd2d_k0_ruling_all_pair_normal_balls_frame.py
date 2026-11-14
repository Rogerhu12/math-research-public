#!/usr/bin/env python3
"""Streaming all-angle/all-radial normal-ball certificate of the saved coast.

Every accepted product box is paid by one of:
* actual point separation greater than twice the prescribed normal radius;
* R151's d<=1/5 extension of the R147 short-chord theorem, with both boundaries;
* a convex radial quadratic supporting-plane lower bound in Arb, with the
  independently certified actual normal variation along a ruling subtracted.

Floating arithmetic only chooses a feasible point for a convex supporting
plane and the order of subdivision.  It never decides a certified leaf.
This is the original delta=0 Cartesian coast, not an altered BVP target.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,time,resource
from collections import OrderedDict
from pathlib import Path
import numpy as np
import flint
from flint import arb,ctx
from fd2d_k0_ruling_actual_curvature_taylor import (TaylorActualRuledIntervals,
    jmul,jinv,jder,jdot,jcross,vsub,vmul,taylor_value)
from fd2d_k0_ruling_actual_curvature_certificate import digest,bounds
from fd2d_k0_ruling_angular_certificate import moment
from fd2d_k0_ruling_metric_convolution import load,from_bounds,magnitude_upper


def dot(a,b):return sum((x*y for x,y in zip(a,b)),arb(0))
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def mul(c,a):return [c*x for x in a]
def squared(x):
    lo,hi=x.lower(),x.upper()
    if lo>=0:return (lo*lo).union(hi*hi)
    if hi<=0:return (hi*hi).union(lo*lo)
    q=max(abs(lo),abs(hi));return arb(0).union(q*q)
def norm2(a):return sum((squared(x) for x in a),arb(0))
def norm_upper(a):return norm2(a).upper().sqrt().upper()
def radius_float(a):return math.sqrt(sum((float(x.upper()-x.lower())/2)**2 for x in a))
def tofloat(a):return np.asarray([float(x.mid()) for x in a])
def sqrt_jet(a):
    r=a[0].sqrt();u=1/a[0]
    return [r,r*a[1]*u/2,r*(a[2]*u/2-a[1]*a[1]*u*u/8)]


def invsqrt_jet(a):
    r=1/a[0].sqrt();u=1/a[0]
    return [r,-r*a[1]*u/2,r*(3*a[1]*a[1]*u*u/8-a[2]*u/2)]


class PairGeometry(TaylorActualRuledIntervals):
    def __init__(self,inlet,candidate,moments,means,position_modes,cache_limit):
        super().__init__(inlet,candidate,moments,position_modes)
        mom=load(moments);packet=load(means)
        if packet['exact_moment_report']['sha256']!=digest(moments) or not packet['source_moment_intervals_remain_valid']:
            raise ValueError('Material-coordinate means have a different definition')
        if [r['angular_mode'] for r in packet['rows']]!=list(range(2,1025,2)):
            raise ValueError('The full 512 mean packet is required')
        self.means=[moment(r['material_weighted_mean']) for r in packet['rows']]
        self.a0=moment(mom['enclosures']['a0'])
        p=mom['parameters'];self.seed_r,self.seed_D,self.seed_c,self.seed_k=(arb(p[k]) for k in ('r','D','c','k'))
        self.adjust=[moment(mom['enclosures'][k]) for k in ('u0','u2','u4')]
        self.U_tail=((self.seed_r+self.seed_D)/self.a0*(-arb(513)/10).exp()/(513*(1-(-arb(1)/10).exp()))).upper()
        self.cache=OrderedDict();self.cache_limit=cache_limit;self.calls=0;self.invalid=0

    def h(self,phi):
        c2=(2*phi).cos();c4=(4*phi).cos()
        rho=self.seed_r+self.seed_D*(1-(self.seed_k*(c2-self.seed_c)).tanh())/2+self.adjust[0]+self.adjust[1]*c2+self.adjust[2]*c4
        return rho/self.a0

    def material_center(self,mid):
        ans=mid
        for j,mu in enumerate(self.means,1):ans+=mu/j*(2*j*mid).sin()
        return ans+arb(0,tuple(map(int,self.U_tail.man_exp())))

    def angle(self,index,den):
        key=(index,den)
        if key in self.cache:
            self.cache.move_to_end(key);return self.cache[key]
        self.calls+=1;pi=arb.pi();mid=pi*(2*index+1)/den;half=pi/den
        delta=arb(0,tuple(map(int,half.upper().man_exp())))
        phi=(2*pi*index/den).union(2*pi*(index+1)/den)
        Fc,nc,mc=self.fourier_jets(mid);Fi,ni,mi=self.fourier_jets(phi)
        Fi=[self.refine_field(c,i,delta) for c,i in zip(Fc,Fi)]
        ni=self.refine_field(nc,ni,delta);mi=self.refine_field(mc,mi,delta)
        value=None
        if ni[0]>0:
            kc=jmul(mc,jinv(nc));ki=jmul(mi,jinv(ni))
            Gc=vsub(Fc[3:6],vmul(kc,Fc[6:9]));Gi=vsub(Fi[3:6],vmul(ki,Fi[6:9]))
            # Reference E=e1 cross e2 is deliberately not normalized.
            # Its error from every actual ruling normal is paid by the
            # separately certified packet, including ||E|-1|<=H.
            Ec=jcross(Fc[3:6],Fc[6:9]);Ei=jcross(Fi[3:6],Fi[6:9])
            if ni[0]>0:
                Nc=[x[:3] for x in Ec];Ni=[x[:3] for x in Ei]
                X=[taylor_value(c,i,delta) for c,i in zip(Fc[:3],Fi[:3])]
                G=[taylor_value(c,i,delta) for c,i in zip(Gc,Gi)]
                N=[taylor_value(c,i,delta) for c,i in zip(Nc,Ni)]
                k=taylor_value(kc,ki,delta)
                C=self.L*(2*self.rho0+self.L)
                def Wjets(kj):
                    z=jmul(kj[:3],kj[:3]);z[0]+=1
                    z=[C*x for x in z];z[0]+=self.rho0*self.rho0
                    # Replace the zeroth argument by a positive enclosure.
                    z[0]=self.rho0*self.rho0+C*(1+squared(kj[0]))
                    rj=sqrt_jet(z);rj[0]+=self.rho0
                    return [C*x for x in jinv(rj)]
                Wc,Wi=Wjets(kc),Wjets(ki)
                Ac,Ai=vmul(Wc,Gc),vmul(Wi,Gi)
                W=taylor_value(Wc,Wi,delta)
                A=[taylor_value(c,i,delta) for c,i in zip(Ac,Ai)]
                h=self.h(phi);tc=self.material_center(mid);t=tc+h*delta
                sn,cs=(self.v*t).sin_cos()
                Y=[self.rho0*cs,self.rho0*sn]
                Aflat=[W*(cs+k*sn),W*(sn-k*cs)]
                value=dict(X=X,A=A,N=N,Y=Y,Aflat=Aflat,t=t,k=k,W=W,
                    Xf=tofloat(X),Af=tofloat(A),Nf=tofloat(N),
                    Yf=tofloat(Y),Aflatf=tofloat(Aflat),
                    angular_score=radius_float(X)+radius_float(A)+.136*radius_float(N),
                    finite_n_lower=ni[0].lower(),delta=delta,
                    center_jets=dict(X=[x[:3] for x in Fc[:3]],A=Ac,N=Nc),
                    interval_jets=dict(X=[x[:3] for x in Fi[:3]],A=Ai,N=Ni))
        if value is None:self.invalid+=1
        self.cache[key]=value
        if len(self.cache)>self.cache_limit:self.cache.popitem(last=False)
        return value


def interval_range(index,den):return arb(index)/den,arb(index+1)/den
def endpoint_vector(data,index,den,flat=False,shift=0,v=None):
    base,direction=(data['Y'],data['Aflat']) if flat else (data['X'],data['A'])
    rows=[add(base,mul(x,direction)) for x in interval_range(index,den)]
    if flat and shift:
        sn,cs=(2*arb.pi()*shift*v).sin_cos()
        rows=[[cs*p[0]-sn*p[1],sn*p[0]+cs*p[1]] for p in rows]
    return rows


def feasible_minimizer(p,q,pl,ph,ql,qh,normal,sign,radius=.136):
    """Float guess only. All four edge minimizers and resolved interior."""
    A,B=p['Af'],q['Af'];d=q['Xf']-p['Xf'];shift=d-sign*radius*normal
    aa=float(A@A);bb=-float(A@B);cc=float(B@B)
    c0=-float(A@shift);c1=float(B@shift)
    candidates=[]
    for x in (pl,ph):candidates.append((x,float(np.clip(-(c1+bb*x)/cc,ql,qh))))
    for y in (ql,qh):candidates.append((float(np.clip(-(c0+bb*y)/aa,pl,ph)),y))
    det=aa*cc-bb*bb
    if det>64*np.finfo(float).eps*aa*cc:
        x=(bb*c1-cc*c0)/det;y=(bb*c0-aa*c1)/det
        if pl<=x<=ph and ql<=y<=qh:candidates.append((x,y))
    def val(xy):
        x,y=xy;chord=d+y*B-x*A
        return float(chord@chord-2*sign*radius*(normal@chord))
    best=min(candidates,key=val)
    return best,val(best)


def product_jet(a,b):
    return [a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+a[0]*b[2],
        a[3]*b[0]+a[1]*b[1]+a[0]*b[3],
        a[4]*b[0]+a[1]*b[2]+a[2]*b[1]+a[0]*b[4],
        a[5]*b[0]+a[2]*b[2]+a[0]*b[5]]


def mixed_dot(a,b):
    products=[product_jet(x,y) for x,y in zip(a,b)]
    return [sum((r[k] for r in products),arb(0)) for k in range(6)]


def embed_jets(rows,axis):
    zero=arb(0)
    if axis==0:return [[r[0],r[1],zero,r[2],zero,zero] for r in rows]
    return [[r[0],zero,r[1],zero,zero,r[2]] for r in rows]


def mixed_position(data,x,axis,kind):
    rows=data[kind]
    return embed_jets([[a+x*b for a,b in zip(u,v)] for u,v in zip(rows['X'],rows['A'])],axis)


def mixed_range(center,interval,dp,dq):
    return center[0]+center[1]*dp+center[2]*dq+interval[3]*(dp*dp)+interval[4]*(dp*dq)+interval[5]*(dq*dq)


def mixed_ball_and_gradients(p,q,x,y,normal_owner,sign,rho,kind):
    P=mixed_position(p,x,0,kind);Q=mixed_position(q,y,1,kind)
    D=[[b-a for a,b in zip(u,v)] for u,v in zip(P,Q)]
    N=embed_jets((p if normal_owner==0 else q)[kind]['N'],normal_owner)
    shifted=[[d-sign*rho*n for d,n in zip(dr,nr)] for dr,nr in zip(D,N)]
    dd=mixed_dot(D,D);nd=mixed_dot(N,D)
    value=[d-2*sign*rho*n for d,n in zip(dd,nd)]
    Ap=embed_jets(p[kind]['A'],0);Aq=embed_jets(q[kind]['A'],1)
    gx=[-2*z for z in mixed_dot(Ap,shifted)];gy=[2*z for z in mixed_dot(Aq,shifted)]
    return value,gx,gy


def convex_lower(p,q,pr,qr,normal,normal_float,sign,rho,normal_owner):
    pl,ph=interval_range(*pr);ql,qh=interval_range(*qr)
    (xf,yf),midval=feasible_minimizer(p,q,float(pl),float(ph),float(ql),float(qh),normal_float,sign,float(rho))
    x,y=arb(xf),arb(yf)
    if not (x>=pl and x<=ph and y>=ql and y<=qh):raise ValueError('Nonfeasible supporting point')
    owner=normal_owner
    center=mixed_ball_and_gradients(p,q,x,y,owner,sign,rho,'center_jets')
    interval=mixed_ball_and_gradients(p,q,x,y,owner,sign,rho,'interval_jets')
    value,gx,gy=[mixed_range(c,i,p['delta'],q['delta']) for c,i in zip(center,interval)]
    lower=(value.lower()+min((-gx*(x-pl)).lower(),(gx*(ph-x)).lower())
        +min((-gy*(y-ql)).lower(),(gy*(qh-y)).lower())).lower()
    return lower,midval


def check_box(definition,pkey,qkey,rho,epsN):
    pi,pden,pri,prden=pkey;qi,qden,qri,qrden=qkey
    p,q=definition.angle(pi,pden),definition.angle(qi,qden)
    if p is None or q is None:return dict(kind=None,invalid_p=p is None,invalid_q=q is None)
    pr,qr=(pri,prden),(qri,qrden)
    pe=endpoint_vector(p,*pr);qe=endpoint_vector(q,*qr)
    pbox=[a.union(b) for a,b in zip(*pe)];qbox=[a.union(b) for a,b in zip(*qe)]
    actual_distance2=norm2(sub(qbox,pbox))
    if actual_distance2.lower()>4*rho*rho:
        d=actual_distance2.lower().sqrt()
        return dict(kind='separation',lower=(d*(d-2*rho)).lower())
    # Use the closest inlet-label lift, then prove the whole chosen polar
    # angle is inside (-pi,pi). The small-distance test thereby uses R147's
    # shortest material lift, including the 0/2pi seam.
    center_difference=(2*qi+1)/(2*qden)-(2*pi+1)/(2*pden)
    shift=-1 if center_difference>.5 else (1 if center_difference<-.5 else 0)
    polar=definition.v*(q['t']+2*arb.pi()*shift-p['t'])
    correction=2*(arb(28)/100*7/(arb(39)/10))
    lift_safe=bool(magnitude_upper(polar)+correction<arb.pi())
    py=endpoint_vector(p,*pr,flat=True);qy=endpoint_vector(q,*qr,flat=True,shift=shift,v=definition.v)
    flat_max2=max(norm2(sub(b,a)).upper() for a in py for b in qy)
    if lift_safe and flat_max2<=arb(1)/25:return dict(kind='short_chord',developed_distance2_upper=flat_max2)
    max_chord=max(norm_upper(sub(b,a)) for a in pe for b in qe)
    correction_normal=(2*rho*epsN*max_chord).upper()
    lowers=[];midvals=[]
    for normal_owner,(normal,nf) in enumerate(((p['N'],p['Nf']),(q['N'],q['Nf']))):
        for sign in (-1,1):
            low,mid=convex_lower(p,q,pr,qr,normal,nf,sign,rho,normal_owner)
            lowers.append((low-correction_normal).lower());midvals.append(mid)
    lower=min(lowers)
    if lower>0:return dict(kind='convex_QP',lower=lower)
    angular=[p['angular_score'],q['angular_score']]
    radial=[np.linalg.norm(p['Af'])/prden,np.linalg.norm(q['Af'])/qrden]
    # This is only a work ordering heuristic. It is not part of a proof.
    near=bool(min(midvals)<.004)
    if near and max(radial)>.07 and max(angular)<max(radial)/4:
        which=2+int(radial[1]>radial[0])
    else:which=int(angular[1]>angular[0])
    return dict(kind=None,split=which,lower=lower,mid_min=min(midvals),flat_upper=flat_max2,
        angular_scores=angular,radial_scores=radial,lift_safe=lift_safe)


def split_key(key,angular):
    i,d,r,rd=key
    if angular:return (2*i,2*d,r,rd),(2*i+1,2*d,r,rd)
    return (i,d,2*r,2*rd),(i,d,2*r+1,2*rd)


def main():
    root=Path(__file__).resolve().parent.parent;ap=argparse.ArgumentParser(description=__doc__)
    default=lambda name:root/'notes'/name
    ap.add_argument('--inlet',type=Path,default=default('2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz'))
    ap.add_argument('--candidate',type=Path,default=default('2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json'))
    ap.add_argument('--moments',type=Path,default=default('2026-11-12-fd2d-balanced-moments-taylor-01.json'))
    ap.add_argument('--means',type=Path,default=default('2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz'))
    ap.add_argument('--variation',type=Path,default=default('2026-11-12-fd2d-k0-ruling-frame-reference-bound-01.json'))
    ap.add_argument('--extension',type=Path,default=default('2026-11-12-fd2d-k0-ruling-extension-certificate-02.json.gz'))
    ap.add_argument('--initial-angles',type=int,default=32)
    ap.add_argument('--maximum-angle-denominator',type=int,default=32768)
    ap.add_argument('--maximum-radial-denominator',type=int,default=32)
    ap.add_argument('--cache-limit',type=int,default=4096)
    ap.add_argument('--position-modes',type=int,default=96)
    ap.add_argument('--first-row',type=int,default=0)
    ap.add_argument('--last-row',type=int,default=None)
    ap.add_argument('--resume',type=Path,default=None)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    if args.initial_angles<=0 or args.initial_angles&(args.initial_angles-1):raise ValueError('Use dyadic angular boxes')
    last=args.initial_angles if args.last_row is None else args.last_row
    if not 0<=args.first_row<last<=args.initial_angles:raise ValueError('Invalid initial row range')
    started=time.monotonic();ctx.prec=160
    variation,extension=load(args.variation),load(args.extension)
    for packet in (variation,extension):
        if packet['inlet_sha256']!=digest(args.inlet) or not packet['passed']:raise ValueError('Actual input/certificate mismatch')
    if extension['candidate_sha256']!=digest(args.candidate) or extension['moments_sha256']!=digest(args.moments):raise ValueError('Short-chord extension mismatch')
    if extension['extension']!='3/1000':raise ValueError('The d<=.2 theorem requires the certified .003 auxiliary extension')
    definition=PairGeometry(args.inlet,args.candidate,args.moments,args.means,args.position_modes,args.cache_limit)
    if not (definition.rho0>arb(39)/10 and definition.v>arb(1)/4 and definition.v<arb(3)/10 and definition.L<arb(28)/100):raise ValueError('R147 lift constants not applicable')
    rho=arb(17)/125;epsN=from_bounds(variation['actual_normal_to_frame_cross_global_upper']).upper()
    counts=dict(separation=0,short_chord=0,convex_QP=0);bad=[];calls=0;splits=0;max_stack=0;min_lower=None;max_short=arb(0)
    chain='0'*64;initial_done=0;rows=[];last_progress=time.monotonic()
    binding=dict(source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),moments_sha256=digest(args.moments),means_sha256=digest(args.means),variation_sha256=digest(args.variation),extension_sha256=digest(args.extension),initial_angles=args.initial_angles,first_row=args.first_row,last_row=last,maximum_angle_denominator=args.maximum_angle_denominator,maximum_radial_denominator=args.maximum_radial_denominator,position_modes=args.position_modes)
    next_row=args.first_row;previous_seconds=0.0;previous_angles=0;previous_invalid=0;resume_sha=None
    if args.resume is not None:
        saved=load(args.resume)
        if saved['binding']!=binding:raise ValueError('Checkpoint definition/configuration mismatch')
        next_row=saved['next_row']
        if not args.first_row<=next_row<=last:raise ValueError('Invalid checkpoint row')
        counts=saved['methods'];bad=saved['unresolved'];calls=saved['recursive_box_calls'];splits=saved['split_count'];max_stack=saved['maximum_stack_size'];chain=saved['leaf_hash_chain_sha256'];initial_done=saved['completed_initial_products'];rows=saved['rows']
        min_lower=from_bounds(saved['minimum_strict_far_Phi_lower']).lower() if saved['minimum_strict_far_Phi_lower'] is not None else None
        max_short=from_bounds(saved['maximum_short_developed_distance2_upper']).upper()
        previous_seconds=saved['seconds'];previous_angles=saved['angle_interval_evaluations'];previous_invalid=saved['invalid_coarse_angle_boxes'];resume_sha=digest(args.resume)
    checkpoint_path=args.out.with_name(args.out.name+'.checkpoint.json')
    for i in range(next_row,last):
        rowcounts={k:0 for k in counts};rowcalls=0
        for j in range(i,args.initial_angles):
            stack=[((i,args.initial_angles,0,1),(j,args.initial_angles,0,1))]
            while stack:
                max_stack=max(max_stack,len(stack));p,q=stack.pop();calls+=1;rowcalls+=1
                result=check_box(definition,p,q,rho,epsN);kind=result['kind']
                if kind is not None:
                    counts[kind]+=1;rowcounts[kind]+=1
                    leaf=dict(p=p,q=q,kind=kind)
                    if kind=='short_chord':
                        max_short=max(max_short,result['developed_distance2_upper']);leaf['d2_upper']=bounds(result['developed_distance2_upper'])
                    else:
                        low=result['lower'];min_lower=low if min_lower is None else min(min_lower,low);leaf['Phi_lower']=bounds(low)
                    chain=hashlib.sha256(bytes.fromhex(chain)+json.dumps(leaf,sort_keys=True,separators=(',',':')).encode()).hexdigest()
                    continue
                if result.get('invalid_p') or result.get('invalid_q'):
                    which=0 if result.get('invalid_p') else 1
                else:which=result['split']
                # If a preferred axis is exhausted, try another actual axis.
                possible=[d for d in (which,0,1,2,3) if ((p if d%2==0 else q)[1 if d<2 else 3] < (args.maximum_angle_denominator if d<2 else args.maximum_radial_denominator))]
                if not possible:
                    bad.append(dict(p=p,q=q,reason='No strict leaf bound at declared subdivision limits',lower=bounds(result['lower']) if 'lower' in result else None))
                    continue
                which=possible[0];children=split_key(p if which%2==0 else q,which<2);splits+=1
                if which%2==0:stack.extend((child,q) for child in reversed(children))
                else:stack.extend((p,child) for child in reversed(children))
                if time.monotonic()-last_progress>20:
                    print(json.dumps(dict(row=i,pair=j,calls=calls,leaves=counts,unresolved=len(bad),angle_evaluations=definition.calls,cache=len(definition.cache),stack=len(stack),seconds=time.monotonic()-started)),flush=True);last_progress=time.monotonic()
            initial_done+=1
        rows.append(dict(row=i,calls=rowcalls,leaves=rowcounts))
        checkpoint=dict(schema='fd2d-all-pair-completed-rows-checkpoint-v1',binding=binding,next_row=i+1,methods=counts,unresolved=bad,recursive_box_calls=calls,split_count=splits,maximum_stack_size=max_stack,leaf_hash_chain_sha256=chain,completed_initial_products=initial_done,rows=rows,minimum_strict_far_Phi_lower=bounds(min_lower) if min_lower is not None else None,maximum_short_developed_distance2_upper=bounds(max_short),seconds=previous_seconds+time.monotonic()-started,angle_interval_evaluations=previous_angles+definition.calls,invalid_coarse_angle_boxes=previous_invalid+definition.invalid)
        temporary=checkpoint_path.with_name(checkpoint_path.name+'.tmp');temporary.write_text(json.dumps(checkpoint,indent=2,allow_nan=False)+'\n');temporary.replace(checkpoint_path)
        print(json.dumps(dict(completed_row=i,calls=calls,leaves=counts,unresolved=len(bad),angles=definition.calls,seconds=time.monotonic()-started)),flush=True)
    report=dict(schema='fd2d-actual-coast-all-pair-normal-ball-Arb-v4-frame-reference',actual_execution=True,
        source_sha256=digest(__file__),helper_sources={name:digest(Path(__file__).with_name(name)) for name in ('fd2d_k0_ruling_actual_curvature_taylor.py','fd2d_k0_ruling_actual_curvature_certificate.py','fd2d_k0_ruling_angular_certificate.py','fd2d_k0_ruling_metric_convolution.py')},
        inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),moments_sha256=digest(args.moments),means_sha256=digest(args.means),normal_variation_sha256=digest(args.variation),short_chord_extension_sha256=digest(args.extension),
        precision_bits=160,flint_version=flint.__version__,radius=bounds(rho),normal_variation_upper=bounds(epsN),
        initial_angle_boxes=args.initial_angles,initial_rows=[args.first_row,last],completed_initial_products=initial_done,
        full_initial_triangle_covered=args.first_row==0 and last==args.initial_angles,
        unordered_angle_products_with_both_endpoint_normals_and_both_signs=True,
        radial_cover='tau=w/W(phi) in [0,1] for both points; every split is an exact dyadic partition',
        periodic_boundary='Chosen inlet lift checked to stay inside a polar angle of pi; short-chord cells then invoke the certified material shortest-lift theorem',
        actual_finite_Cartesian_surface_used=True,changed_delta_target=False,
        exact_frame_or_developability_assumed=False,boundary_normal_cone_reach_not_claimed=True,
        methods=counts,recursive_box_calls=calls,split_count=splits,angle_interval_evaluations=previous_angles+definition.calls,invalid_coarse_angle_boxes=previous_invalid+definition.invalid,
        angle_cache_limit=args.cache_limit,maximum_stack_size=max_stack,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        complete_pair_function_Taylor_order=2,
        reference_vector='unnormalized E=e1 cross e2; actual normal error included separately',reference_vector_assumed_unit=False,reference_bound_source_sha256=variation['source_sha256'],
        maximum_angle_denominator=args.maximum_angle_denominator,maximum_radial_denominator=args.maximum_radial_denominator,
        minimum_strict_far_Phi_lower=bounds(min_lower) if min_lower is not None else None,
        maximum_short_developed_distance2_upper=bounds(max_short),leaf_hash_chain_sha256=chain,
        passed=not bad,unresolved=bad,rows=rows,seconds=previous_seconds+time.monotonic()-started,
        short_chord_cutoff='1/5',short_chord_normal_ball_coefficient='1/200',normal_owner_explicit_even_for_identical_angle_cache=True,resumed_checkpoint_sha256=resume_sha,completed_row_checkpoint=str(checkpoint_path),
        displayed_decimals_are_not_outward_rounded=True,strict_values_are_exact_binary_endpoint_fields=True)
    raw=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if args.out.suffix=='.gz':args.out.write_bytes(gzip.compress(raw,mtime=0))
    else:args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),passed=report['passed'],complete=report['full_initial_triangle_covered'],leaves=counts,unresolved=len(bad),seconds=report['seconds'])),flush=True)
    if bad:raise SystemExit(1)


if __name__=='__main__':main()
