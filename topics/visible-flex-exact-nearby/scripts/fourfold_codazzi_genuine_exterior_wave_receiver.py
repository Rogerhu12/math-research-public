"""Both true Airy rows, the common input multiplier, and whole-circle negative-order reception."""
from fractions import Fraction as Q
from flint import arb,acb,acb_series,arb_series
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_genuine_outer_seam_operator import der
from fourfold_codazzi_genuine_exterior_wave_fields import BINS,exterior_pair

N=388


def signed(a):
    return acb_series([acb(a[j]) for j in range(3)],prec=3)


def weights(x,t,s,pp,pm,w):
    x,t,s,pp,pm=map(signed,(x,t,s,pp,pm))
    gap=pp*pm;y=-t/s;T=-s*s;ii=acb(0,1)
    v=[signed(w[0])*ii,signed(w[1])]
    def inv(v):return [(-ii*x*v[0]+T*y*v[1])/gap,(y*v[0]-ii*x*v[1])/gap]
    v1=inv(v);v2=inv(v1);bd=inv(list(map(der,v1)))
    first=[der(a)+b for a,b in zip(v2,bd)];zero=list(map(der,bd))
    return [[abs(z[0]).upper() for z in pair] for pair in (v,v2,first,zero)]


def compact(rows):
    """All original normalized jets on closed centered full-circle bins."""
    out=[]
    for k in range(BINS):
        fine=[rows[(4*k+i)%128] for i in range(-2,3)]
        v=list(fine[0])
        for f in fine[1:]:v=[a.union(b) for a,b in zip(v,f)]
        out.append(v)
    return out


def receive(geos,raw,ratios,scale,jj,mid,radius,mixed):
    physical=compact(ratios);groups=[[[arb(0),arb(0)] for _ in range(4)] for _ in range(2)]
    smin=smax=pmin=None;array=[]
    for i,geo in enumerate(geos):
        x,t,_,pp,pm=geo
        rp=arb_series(physical[i],prec=len(physical[i]))
        rev=physical[(-i)%BINS];rm=arb_series([(-1)**(j+1)*v for j,v in enumerate(rev)],prec=len(rev))
        f,g,s=exterior_pair(geo,raw,i,(rp,rm))
        umin=s[0].lower();umax=s[0].upper();p=min(pp[0].lower(),pm[0].lower())
        smin=umin if smin is None else min(smin,umin)
        smax=umax if smax is None else max(smax,umax)
        pmin=p if pmin is None else min(pmin,p)
        for k,pair in enumerate(([v+mid*z for v,z in zip(f,g)],g)):
            ww=weights(x,t,s,pp,pm,pair)
            for j,r in enumerate(ww):groups[k][j]=[max(v,z) for v,z in zip(groups[k][j],r)]
        array.extend(z[j] for pair in (f,g) for z in pair for j in range(3))
    theta=(arb(N).root(3)**(-2)+smax*smax).sqrt()
    mod=min(exact(Q(18,25)),(arb(2)/(1+arb(N).root(3)**2*smin*smin)).root(4))
    phi=2/pmin.sqrt()*exact(Q(6,5))*(1+exact(Q(5,8))*(smax*smax/(smin*smin)).log())*mod
    fees=[];numeric=[]
    for group in groups:
        zero,two,one,rest=[p[0]+theta*p[1] for p in group]
        second=two+exact(Q(4,17))*one+exact(Q(1,17))*rest
        # In the mixed slice use the actual root J<2. In the exterior
        # strict slice the previously typed two-stage angular inverse is jj.
        if mixed:
            budget=2*arb(N).root(6)**(-1)*zero.root(6)*(second.root(6))**5
        else:budget=jj*second/arb(N).sqrt()
        fees.append((phi*budget*(1+exact(Q(1,N*N)))*scale).upper())
        numeric.extend([zero,two,one,rest])
    value=(fees[0]+radius*fees[1]).upper()
    check(value>=0 and value.is_finite(),'complete physical two-column common-multiplier receiver')
    factor=2039 if mixed else 192
    # A single signed physical label has no composition-operator or
    # level-set loss: its exact oscillatory scalar has modulus one, and
    # the genuine two-column right matrix is constant in the angle.
    whole=(value*factor*exact(Q(719,1000))).upper()
    single=(whole*(exact(Q(6,5))*mod)/phi).upper()
    return whole,single,array,[*numeric,phi,jj,scale,*fees]


def source_plan(plan,root):
    rl,rh=root;start=rl-Q(1,5000);cut=rh-Q(1,200)
    result=[]
    for n,(i,l,r) in enumerate(plan):
        stop=min(r,start)
        if stop<=l:continue
        bounds=[stop]
        if l<cut<stop:bounds.append(cut)
        bounds.append(l)
        for b,a in zip(bounds,bounds[1:]):
            result.append((n,i,a,b,a>=cut))
    check(result[0][3]==start and result[-1][2]==0 and all(l[2]==r[3] for l,r in zip(result,result[1:])),
          'entire support-exterior radial domain without duplicated physical mass')
    return result
