"""Run39 physical mesh and material velocity at a continuous regular chart point."""
from types import SimpleNamespace

import numpy as np
from scipy.optimize import brentq

import bent_body_ambient as ambient
import bent_body_atlas as atlas


class Polynomial:
    """Contract the original component/parity dictionary before taking chart derivatives."""
    def __init__(self, degree, physical, scale, coefficients):
        self.degree = degree
        self.physical = physical
        self.scale = np.asarray(scale)
        self.coefficients = coefficients
        self.blocks = []
        at = 0
        for component in range(3):
            powers = [(i,j,k) for i in range(degree+1) for j in range(degree+1-i)
                      for k in range(degree+1-i-j)
                      if j%2 == (component==1 if physical else component!=1)
                      and k%2 == (component==2)]
            n = len(powers)
            self.blocks.append((np.asarray(powers).T, coefficients[at:at+n]))
            at += n
        if at != len(coefficients):
            raise ValueError("Run39 coefficient count differs from its actual polynomial dictionary")

    def values(self, f, chi):
        scaled = f/self.scale
        tabs = [ambient.Cheb(np.array([v]), self.degree) for v in scaled[0]]
        result = np.empty((6 if self.physical else 3, 3))
        axes = np.eye(3, dtype=int)
        for component, (powers, coef) in enumerate(self.blocks):
            def term(orders):
                return np.dot(coef, tabs[0][orders[0]][0,powers[0]] *
                              tabs[1][orders[1]][0,powers[1]] *
                              tabs[2][orders[2]][0,powers[2]])
            val = term((0,0,0))
            grad = np.array([term(a) for a in axes])
            first = scaled[1:3] @ grad
            result[0,component] = chi[0]*val
            result[1:3,component] = chi[1:3]*val + chi[0]*first
            if self.physical:
                hess = np.empty((3,3))
                for i in range(3):
                    for j in range(i,3):
                        hess[i,j] = hess[j,i] = term(axes[i]+axes[j])
                for k,(a,b) in enumerate(((1,1),(1,2),(2,2)),3):
                    second = scaled[k] @ grad + scaled[a] @ hess @ scaled[b]
                    result[k,component] = (chi[k]*val + chi[a]*first[b-1] +
                                           chi[b]*first[a-1] + chi[0]*second)
        return result

    def original_difference(self, f, chi):
        m = SimpleNamespace(f=f[None,:,:], chi=chi[None,:])
        original = ambient.Basis(m, self.degree, self.physical, self.scale)
        return float(np.abs(self.values(f,chi)-original.values(self.coefficients)[0]).max())


class ClosedAtlas:
    """A signed outward transverse arclength on the tube, Cartesian (x,z) on each cap."""
    def __init__(self, parent, design, params):
        self.p, self.d = params, design
        self.g, self.center, self.frame, self.h = atlas.info(design["geometry"],parent,design["gap"])
        self.head = parent.parent
        self.rim = 1.+self.head.END_LENGTH
        self.width = self.head.CAP_NORMAL_CHART_WIDTH
        self.inner = .30*self.width
        self.outer = .65*self.width
        _,self.m0,_,_,self.half,*_ = self.g.profile_constants(32)
        self.period = 2*self.half
        self.kw = ({"jacobi":bool(design["gap"])} if design["geometry"]=="equal"
                   else {"gap_amplitude":design["gap"]})
        self.ref_c = self.center[[0,2]]
        self.dcap = self.head.end_limits(32)[1]
        self.nodes = np.linspace(0.,self.period,513)
        pos = self.ray_curve(self.nodes)
        theta = np.unwrap(np.arctan2(pos[:,1],pos[:,0]))
        self.orientation = np.sign(theta[-1]-theta[0])
        self.radii = np.linalg.norm(pos,axis=1)
        self.angles = self.orientation*(theta-theta[0])
        self.theta0 = theta[0]
        if np.any(np.diff(self.angles)<=0):
            raise ValueError("reference planar offset does not give a regular polar transition")

    def base(self, chart, q):
        u, w = q
        if chart != "tube":
            side = 1 if chart=="cap+" else -1
            f = self.g.cap_cartesian(np.array([u]),np.array([w]),side)[0]
            chi, x0 = atlas.material(self.g,np.array([u]),np.array([w]),chart,
                                      self.p["shape_mask_width"],self.d["field_width"])
        else:
            u = float(u%self.period)
            w = float(w)
            if abs(w)<=1.:
                lab,v,sign = "cylinder",w,1.
            else:
                sign = 1. if w>0 else -1.
                end = "+" if w>0 else "-"
                if abs(w)<=self.rim:
                    lab,v = "end"+end,abs(w)-1.
                else:
                    lab,v = "cap-normal"+end,abs(w)-self.rim
            us,vs = np.array([u]),np.array([v])
            f = self.g.chart_jet(lab,us,vs,markers=False,**self.kw)[0]
            chi, x0 = atlas.material(self.g,us,vs,lab,self.p["shape_mask_width"],self.d["field_width"])
            f[[2,4]] *= sign
            chi[:,[2,4]] *= sign
            x0[:,:,1] *= sign
            x0[:,2,:] *= sign
        f = f@self.frame
        f[0] -= self.center@self.frame
        return f,chi[0],x0[0]

    def ray_curve(self,u):
        pos,tan,normal,k,kp = self.g.profile_coordinates(u,32)
        return pos-(self.dcap+self.inner)*normal-self.ref_c

    def approximate_cap_margin(self,q):
        delta=np.asarray(q)-self.ref_c
        angle=(self.orientation*(np.arctan2(delta[1],delta[0])-self.theta0))%(2*np.pi)
        return float(np.interp(angle,self.angles,self.radii)-np.linalg.norm(delta))

    def ray(self,q):
        diff = np.asarray(q)-self.ref_c
        a = np.arctan2(diff[1],diff[0])
        angle = float((self.orientation*(a-self.theta0))%(2*np.pi))
        i = min(len(self.nodes)-2, max(0,np.searchsorted(self.angles,angle,side="right")-1))
        left,right = self.nodes[i:i+2]
        def signed(u):
            z = self.ray_curve(u)
            return self.orientation*np.arctan2(z[1]*np.cos(a)-z[0]*np.sin(a),
                                               z[0]*np.cos(a)+z[1]*np.sin(a))
        lo,hi = signed(left),signed(right)
        if abs(lo)<2e-14:
            u = left
        elif abs(hi)<2e-14:
            u = right
        else:
            u = brentq(signed,left,right,xtol=1e-14,rtol=2e-14)
        return float(u), float(np.linalg.norm(self.ray_curve(u))-np.linalg.norm(diff))

    def switch(self, chart, q):
        if chart=="tube":
            new_chart = "cap+" if q[1]>0 else "cap-"
            f,_,_ = self.base(chart,q)
            pos = f[0]@self.frame.T+self.center
            new_q = pos[[0,2]]
        else:
            new_chart = "tube"
            u,dist = self.ray(q)
            side = 1 if chart=="cap+" else -1
            new_q = np.array([u,side*(self.rim+self.inner)])
        a = self.base(chart,q)[0]
        b = self.base(new_chart,new_q)[0]
        B,A = b[1:3].T,a[1:3].T
        transition = np.linalg.solve(B.T@B,B.T@A)
        return new_chart,new_q,transition,float(np.linalg.norm(a[0]-b[0])),float(np.linalg.norm(B@transition-A))

    def seed(self, point):
        lab = point["chart"]
        u,v = point["coordinate_1"],point["coordinate_2"]
        side = 1 if lab.endswith("+") else -1
        if lab=="cylinder":
            return "tube",np.array([u,v])
        if lab.startswith("end"):
            return "tube",np.array([u,side*(1.+v)])
        if lab.startswith("cap-center"):
            return "cap"+lab[-1],np.array([u,v])
        if lab.startswith("cap"):
            f = self.g.chart_jet(lab,np.array([u]),np.array([v]),markers=False,**self.kw)[0,0]
            xz = f[[0,2]]
            if v>=1.-1e-14:
                return "tube",np.array([u,side*self.rim])
            # Cap coordinates past the switching ring initially use the
            # regular tube collar. Recover BOTH offset and periodic profile
            # arclength, including the radial and normal directions' skew.
            _,d = self.ray(xz)
            if d<=0:
                from scipy.optimize import root
                u0,_ = self.ray(xz)
                def equation(z):
                    pos,tan,n,k,kp = self.g.profile_coordinates(z[0],32)
                    return pos-(self.dcap+z[1])*n-xz
                sol = root(equation,[u0,self.inner])
                if not sol.success and np.linalg.norm(equation(sol.x))>1e-11:
                    raise ValueError("initial polar-to-collar conversion failed")
                return "tube",np.array([sol.x[0],side*(self.rim+max(0.,sol.x[1]))])
            return "cap"+lab[-1],xz
        raise ValueError("unknown parent check chart "+lab)

    def marker(self, chart, q):
        if chart!="tube" or abs(q[1])>1 or q[0]%self.period>self.half:
            return 0.,np.zeros(2)
        x,y = q[0]%self.period-self.m0-1.,q[1]
        if self.d["geometry"]=="equal":
            marks, heights = self.g.MARKS,[self.g.HEIGHT]*len(self.g.MARKS)
        else:
            marks = self.g.disk.MARKERS
            heights = [1e-4*r*r for _,_,r in marks]
        total,grad = 0.,np.zeros(2)
        for (cx,cy,r),h in zip(marks,heights):
            delta=np.array([x-cx,y-cy])
            t=max(0.,1.-delta@delta/(r*r))
            total+=h*t**3
            grad-=6*h*t*t*delta/(r*r)
        return total,grad


class Field:
    def __init__(self, domain, stage, physical, material):
        self.a=domain
        cfg=stage["configuration"]
        scale=domain.p["scale"]
        self.physical=Polynomial(cfg["shape_degree"],True,scale,physical)
        self.material=Polynomial(cfg["field_degree"],False,scale,material)

    def jets(self, chart, q):
        ref,chi,x0=self.a.base(chart,q)
        f=ref+self.physical.values(ref,chi)
        extra=self.material.values(ref,chi)
        return ref,f,extra,x0

    def velocity(self,chart,q):
        ref,f,extra,x0=self.jets(chart,q)
        T=f[1:3]
        G=T@T.T
        w=np.linalg.solve(G,T@extra[0])
        derivative=np.empty((2,2))
        for j,(a,b) in enumerate(((3,4),(4,5))):
            Tj=f[[a,b]]
            DjG=Tj@T.T+T@Tj.T
            derivative[:,j]=x0[j+1]+np.linalg.solve(G,Tj@extra[0]+T@extra[j+1]-DjG@w)
        return x0[0]+w,derivative
