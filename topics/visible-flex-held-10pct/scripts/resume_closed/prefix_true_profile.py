#!/usr/bin/env python3
"""True-integral fixed prefix metric on the unchanged shared material domain.

Only physical inputs are frozen.  All derived lengths, including the bridge
plateau, use real arithmetic and real integrals.  The resulting true arclength
domain is pulled back to the original finite domain [0,L_binary].  An
affine map plus a fixed rounding-sized cut Hermite jet identifies this
metric with the exact finite-map atlas; all refinements share that map.
"""
from fractions import Fraction as Q
import math
import mpmath as mp
from certify_background_sharp import Jet,iv,lower,upper,interval,q,absmax


def sincos(a):
    """Interval Taylor sine/cosine, coefficients are derivatives/factorial."""
    sn=[iv.sin(a.c[0])];cs=[iv.cos(a.c[0])]
    for j in range(1,a.n+1):
        sn.append(sum((k*a.c[k]*cs[j-k]for k in range(1,j+1)),iv.mpf(0))/j)
        cs.append(-sum((k*a.c[k]*sn[j-k]for k in range(1,j+1)),iv.mpf(0))/j)
    return Jet(sn),Jet(cs)


def power(a,n):
    out=a.coerce(1)
    for _ in range(n):out=out*a
    return out


def evaluate(coefficients,x):
    out=iv.mpf(0)
    for c in coefficients[::-1]:out=out*x+c
    return out


def float_bound(v):
    return math.nextafter(float(lower(v)),-math.inf),math.nextafter(float(upper(v)),math.inf)


class TruePrefix:
    def __init__(self,cfg,cut,material_length,series_degree=96,cut_width=.04):
        assert cfg['direction']=='outward' and cfg['cycles']==1
        assert cfg['ramp_law']=='flat' and cfg['prefix_bridge']['kind']=='turn_plateau_v1'
        self.cfg=cfg;self.cut=cut;self.material_length=material_length
        self.delta=q(cfg['delta']);self.vu=q(cfg['vu']);self.vd=q(cfg['vd'])
        self.eps=q(cfg['ramp']);self.eta=q(cfg['ramp_eta'])
        self.Tu=self.delta/(self.vu*(1-self.eps))
        self.Td=self.delta/(self.vd*(1-self.eps))
        self.prefix=self.Tu+self.Td
        self.rcut=q(cut['radius']);self.w=q(cut['backgroundSlope'])
        self.wr=-7*self.w/self.rcut
        self.curvature=q(cfg['prefix_bridge']['curvature'])
        self.fraction=q(cfg['prefix_bridge']['peak_fraction'])
        self.pt=iv.atan2(1,self.w)
        self.ps=self.wr/(1+self.w*self.w)**iv.mpf('1.5')
        self.peak=self.pt+self.fraction*(iv.pi/2-self.pt)
        self.drop=self.peak-self.pt
        self.L1=iv.mpf('1.5')*self.peak/self.curvature
        self.L3=2*self.drop/(-self.ps)
        assert upper(self.peak)<lower(iv.pi/2) and lower(self.drop)>0
        assert upper(iv.exp(iv.mpf('3.5')*self.peak))<512
        assert upper(iv.exp(2*self.drop))<512
        self.degree=series_degree
        self.integral_polynomials=[]
        for terms in ([self.peak/2,iv.mpf('1.5')*self.peak,iv.mpf(0),-2*self.peak],
                      [self.peak-self.drop/4,-self.drop,-self.drop]):
            c=terms+[iv.mpf(0)]*(series_degree+1-len(terms))
            sn,_=sincos(Jet(c))
            self.integral_polynomials.append([iv.mpf(0)]+[v/(k+1)for k,v in enumerate(sn.c)])
        # Cauchy on |z-u_center|=1: |sin(phi(z))|<512.  The center
        # is 1/2 and .501 also permits the tiny analytic extensions used
        # when an exact physical break differs from a binary knot.
        self.series_error=512*iv.mpf('.501')**(series_degree+1)/(1-iv.mpf('.501'))
        self.J1=self.integral(iv.mpf(1),0);self.J3=self.integral(iv.mpf(1),1)
        self.L2=(1-self.rcut-self.L1*self.J1-self.L3*self.J3)/iv.sin(self.peak)
        assert lower(self.L2)>0
        self.length=self.prefix+self.L1+self.L2+self.L3
        self.lam=self.length/q(material_length)
        assert lower(self.lam)>iv.mpf('.999999999') and upper(self.lam)<iv.mpf('1.000000001')
        w=float(cut['backgroundSlope']);r=float(cut['radius'])
        self.atlas_first=-1/math.sqrt(1+w*w)
        self.atlas_second=-w*(-7*w/r)/(1+w*w)**2
        exact_first=-1/iv.sqrt(1+self.w*self.w)
        exact_second=-self.w*self.wr/(1+self.w*self.w)**2
        seam_first=q(self.atlas_first)/exact_first
        seam_second=(q(self.atlas_second)-exact_second*seam_first*seam_first)/exact_first
        self.coordinate_d1=seam_first-self.lam
        self.coordinate_d2=seam_second
        width=q(cut_width);self.cut_width=cut_width
        D1=iv.mpf(absmax(self.coordinate_d1));D2=iv.mpf(absmax(self.coordinate_d2))
        self.coordinate_value_error=iv.mpf(2)/5*width*D1+iv.mpf(1)/20*width*width*D2
        self.coordinate_first_error=2*D1+width*D2/4
        e=upper(self.coordinate_first_error)
        self.coordinate_scale=self.lam+interval(-e,e)
        assert lower(self.coordinate_scale)>0
        self.branches=[]
        eps,eta=self.eps,self.eta
        unit=[iv.mpf(0),eps*eta,eps*(1-eta),eps,1-eps,1-eps*(1-eta),1-eps*eta,iv.mpf(1)]
        for half,(start,T) in enumerate([(iv.mpf(0),self.Tu),(self.Tu,self.Td)]):
            for k in range(7):
                self.branches.append(dict(kind='flat',half=half,piece=k,
                    left=(start+T*unit[k])/self.lam,right=(start+T*unit[k+1])/self.lam))
        b=self.prefix
        for k,(lo,hi) in enumerate([(b,b+self.L1),(b+self.L1,b+self.L1+self.L2),
                                   (b+self.L1+self.L2,self.length)]):
            self.branches.append(dict(kind='bridge',piece=k,left=lo/self.lam,right=hi/self.lam))

    def integral(self,u,which):
        assert lower(u)>=mp.mpf('-.001') and upper(u)<=mp.mpf('1.001')
        p=self.integral_polynomials[which]
        value=evaluate(p,u-iv.mpf('.5'))-evaluate(p,-iv.mpf('.5'))
        err=upper(self.series_error*iv.mpf(max(abs(lower(u)),abs(upper(u)))))
        return value+interval(-err,err)

    def choose(self,s):
        s=mp.mpf(float(s))
        for b in self.branches:
            if s <= (lower(b['right'])+upper(b['right']))/2:
                return b
        return self.branches[-1]

    def primitive_turn(self,t,branch):
        eta=self.eta
        if branch==0:
            x=t/eta
            return (power(x,4)/4-power(x,5)/10)*(eta*eta/(1-eta))
        if branch==1:
            return (t*t/2-t*eta/2+iv.mpf('0.15')*eta*eta)/(1-eta)
        x=(1-t)/eta
        return t-iv.mpf('.5')+(power(x,4)/4-power(x,5)/10)*(eta*eta/(1-eta))

    def radius_jet(self,s,order,branch,value=True):
        x=Jet.variable(s,order)*self.lam
        if branch['kind']=='flat':
            half,k=branch['half'],branch['piece']
            start=0 if half==0 else self.Tu
            T=self.Tu if half==0 else self.Td
            u=(x-start)/T
            if k<3:I=self.primitive_turn(u/self.eps,k)*self.eps
            elif k==3:I=u-self.eps/2
            else:I=-self.primitive_turn((1-u)/self.eps,6-k)*self.eps+(1-self.eps)
            if half==0:return 1+I*self.delta/(1-self.eps)
            return -I*self.delta/(1-self.eps)+(1+self.delta)
        k=branch['piece'];v=x-self.prefix
        if k==0:
            u=v/self.L1
            phi=(3*u*u-2*u*u*u)*self.peak
            r0=1-self.L1*self.integral(u.c[0],0) if value else iv.mpf(0)
        elif k==1:
            return -(v-self.L1)*iv.sin(self.peak)+(1-self.L1*self.J1)
        else:
            u=(v-self.L1-self.L2)/self.L3
            phi=-u*u*self.drop+self.peak
            r0=self.rcut+self.L3*(self.J3-self.integral(u.c[0],1)) if value else iv.mpf(0)
        if not order:return Jet([r0])
        sn,_=sincos(phi)
        return Jet([r0]+[-self.lam*sn.c[k-1]/k for k in range(1,order+1)])

    def auxiliary_error(self,left,right,source_jets):
        """Uniform difference between exact input Hermite radius and true a.

        The selected physical branch is analytically extended across an
        adjacent rounding-sized break if necessary.  Its extension cost is
        paid separately using the actual and extended first derivative.
        """
        lo,hi=q(left),q(right);h=hi-lo
        branch=self.choose((left+right)/2)
        a=self.radius_jet(lo,2,branch);b=self.radius_jet(hi,2,branch)
        errors=[]
        for j in range(3):
            errors.append(max(absmax(q(source_jets[j,0])-a.c[j]*math.factorial(j)),
                              absmax(q(source_jets[j,1])-b.c[j]*math.factorial(j))))
        span=interval(lower(lo),upper(hi))
        whole=self.radius_jet(span,6,branch,value=False)
        # The exact quintic Hermite remainder is f^(6)/6! times
        # (s-left)^3(s-right)^3; its maximum magnitude is h^6/64.
        H=iv.mpf(upper(h))
        remainder=iv.mpf(absmax(whole.c[6]))*H**6/64
        jet_cost=2*iv.mpf(errors[0])+2*H*iv.mpf(errors[1])+H*H*iv.mpf(errors[2])
        excursion=max(mp.mpf(0),upper(branch['left']-lo),upper(hi-branch['right']))
        # |a_s|<=lambda for the true profile; the selected extension
        # derivative is enclosed directly on this entire interval.
        extension_slope=iv.mpf(absmax(whole.c[1]))+iv.mpf(upper(self.lam))
        extension=iv.mpf(excursion)*extension_slope
        # |a_sigma|<=1 transfers the fixed cut coordinate correction.
        total=jet_cost+remainder+extension+self.coordinate_value_error
        return dict(upper=math.nextafter(float(upper(total)),math.inf),
            node_jet_errors=[float(x)for x in errors],sixth_remainder=float(upper(remainder)),
            extension_cost=float(upper(extension)),branch=branch['kind'],piece=branch['piece'])

    def report(self):
        return dict(definition='Exact physical input parameters; real flat-profile algebra and true bridge integrals; sigma=(L_true/L_binary)*s plus the fixed zero-value right cut Hermite first/second jet.',
            true_Tu=float_bound(self.Tu),true_Td=float_bound(self.Td),
            true_L1=float_bound(self.L1),true_L2=float_bound(self.L2),true_L3=float_bound(self.L3),
            true_length=float_bound(self.length),material_length=self.material_length,
            arclength_scale=float_bound(self.lam),scale_minus_one=float_bound(self.lam-1),
            cut_atlas_jets=[self.atlas_first,self.atlas_second],cut_coordinate_width=self.cut_width,
            cut_coordinate_delta_first=float_bound(self.coordinate_d1),cut_coordinate_delta_second=float_bound(self.coordinate_d2),
            cut_coordinate_value_error=float_bound(self.coordinate_value_error),
            cut_coordinate_first_error=float_bound(self.coordinate_first_error),
            true_coordinate_derivative_range=float_bound(self.coordinate_scale),
            bridge_integral_error=float_bound(self.series_error),series_degree=self.degree,
            cauchy_radius=1,cauchy_function_bound=512,normalized_argument_max_abs=.501,
            physical_inputs=self.cfg,cut=self.cut)
