#!/usr/bin/env python3
"""Finite-amplitude one-sided isometric disk with a free, reflected shoulder."""
import argparse
import hashlib
import json
import os
import sys
import time
import traceback
from pathlib import Path

import numpy as np
import scipy
from scipy.interpolate import BSpline, BarycentricInterpolator
from scipy.linalg import null_space
from scipy.special import betainc, betaln
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
from scipy.spatial import cKDTree


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def array_digest(value):
    return digest_bytes(np.ascontiguousarray(value, dtype="<f8").tobytes())


def put_json(path, value):
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
    os.replace(temp, path)


def smooth(v):
    return v**3 * (10.0 + v * (-15.0 + 6.0 * v))


def smooth_integral(v):
    return v**4 * (2.5 + v * (-3.0 + v))


class Disk:
    def __init__(self, p):
        self.h, self.b, self.e = p["straight"], p["bend_width"], p["ramp_fraction"]
        self.H = p["height"]
        g = p["angle"]
        cg, sg = np.cos(g),np.sin(g)
        self.frame = np.array([[cg,0.,-sg],[0.,1.,0.],[sg,0.,cg]])
        self.angle = g
        self.quad, self.qw = np.polynomial.legendre.leggauss(p["disk_quadrature"])

    def angles(self, x):
        t = np.clip((x - self.h) / self.b, 0.0, 1.0)
        u = np.minimum(t, 1.0 - t)
        v = np.minimum(u / self.e, 1.0)
        primitive = np.where(u < self.e, self.e * smooth_integral(v), u - .5*self.e)
        total = 1.0 - self.e
        factor = np.pi/(2.0*total)
        beta = factor*np.where(t <= .5, primitive, total - primitive)
        active = (x > self.h) & (x < self.h + self.b)
        b1 = factor*smooth(v)*active/self.b
        b2 = factor*30.0*v**2*(1.0-v)**2*np.where(t < .5, 1., -1.)*active/(self.b**2*self.e)
        b3 = factor*60.0*v*(1.0-v)*(1.0-2.0*v)*active/(self.b**3*self.e**2)
        return beta, b1, b2, b3

    def curve(self, x):
        x = np.asarray(x)
        flat = np.zeros(x.shape + (3,))
        flat[..., 0] = np.minimum(x, self.h)
        high = self.h + self.b
        flat[..., 2] = np.maximum(x - high, 0.0)
        for l0, r0 in ((0., self.e), (self.e, 1.-self.e), (1.-self.e, 1.)):
            left = self.h + self.b*l0
            width = np.clip(x-left, 0., self.b*(r0-l0))
            nodes = left + width[..., None]*(1.0+self.quad)/2.0
            beta = self.angles(nodes)[0]
            flat[..., 0] += width * (np.cos(beta) @ self.qw)/2.0
            flat[..., 2] += width * (np.sin(beta) @ self.qw)/2.0
        beta, b1, b2, b3 = self.angles(x)
        t = np.stack([np.cos(beta), np.zeros_like(beta), np.sin(beta)], axis=-1)
        n = np.stack([-np.sin(beta), np.zeros_like(beta), np.cos(beta)], axis=-1)
        b1, b2, b3 = b1[..., None], b2[..., None], b3[..., None]
        return flat, t, b1*n, b2*n-b1*b1*t, (b3-b1**3)*n-3*b1*b2*t

    def rim(self, theta):
        x, v = np.cos(theta), np.sin(theta)
        a, b, c, d, e = self.curve(x)
        x, v = x[:, None], v[:, None]
        y = np.array([[0., 1., 0.]])
        height = np.array([[0., 0., self.H]])
        pos = (a + v*y + height, -v*b + x*y, v*v*c-x*b-v*y)
        f = x*b
        f1 = b+x*c
        f2 = 2*c+x*d
        vel = (f+v*y, -v*f1+x*y, v*v*f2-x*f1-v*y)
        f = x*x*c
        f1 = 2*x*c+x*x*d
        f2 = 2*c+4*x*d+x*x*e
        acc = (f, -v*f1, v*v*f2-x*f1)
        return pos, vel, acc

    def point(self, x, y):
        point = self.curve(np.asarray(x))[0].copy()
        point[..., 1] = y
        point[..., 2] += self.H
        return point


def polynomial(coeff, t, j):
    for _ in range(j):
        coeff = [n*v for n, v in enumerate(coeff)][1:]
    return np.polynomial.polynomial.polyval(t, coeff)


def angular(theta, mode, odd, derivative):
    freq = np.arange(1 if odd else 0, mode+1)
    phase = theta[:, None]*freq + derivative*np.pi/2
    return (np.sin(phase) if odd else np.cos(phase))*freq**derivative


def radial(spans, t, is_z):
    knots = np.r_[np.zeros(5), np.linspace(0.,1.,spans+1), np.ones(5)]
    spl = BSpline(knots, np.eye(len(knots)-6), 5)
    bc = [spl(0., nu=j) for j in (0,1,2)]
    bc.extend(spl(1.,nu=j) for j in ((0,1,2) if is_z else (1,)))
    transform = null_space(np.asarray(bc))
    return tuple(spl(t,nu=j) @ transform for j in (0,1,2))


class Shoulder:
    def __init__(self, disk, length, equator, spans, mode, t, theta):
        self.disk, self.L, self.eq = disk, length, equator
        self.spans, self.mode = spans, mode
        self.t, self.theta = np.asarray(t), np.asarray(theta)
        theta, t = self.theta, self.t
        rim = [[v @ disk.frame for v in row] for row in disk.rim(theta)]
        self.bs = [radial(spans,t,k==2) for k in range(3)]
        self.ph = [[angular(theta,mode,k==1,j) for j in range(3)] for k in range(3)]
        self.dims = [(self.bs[k][0].shape[1],self.ph[k][0].shape[1]) for k in range(3)]
        self.slices = []
        n = 0
        for size in self.dims:
            count = size[0]*size[1]
            self.slices.append(slice(n,n+count))
            n += count
        self.n = n
        # Quintic Hermite basis for left position/velocity/acceleration,
        # right position, and right velocity (-vertical). The right horizontal
        # acceleration and the whole horizontal rim position are free in the spline.
        h = [[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],
             [0,0,0,10,-15,6],[0,0,0,-4,7,-3]]
        self.base = {}
        pairs = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
        for j,k in pairs:
            rest = np.stack([self.eq*np.cos(theta+k*np.pi/2),
                             self.eq*np.sin(theta+k*np.pi/2), np.zeros_like(theta)],axis=-1)
            edge = np.zeros_like(rest)
            if k==0:
                edge[:,2] = -length
            values = [rim[0][k],length*rim[1][k],length**2*rim[2][k],rest,edge]
            self.base[j,k] = sum(polynomial(co,t,j)[:,None,None]*v[None,:,:]
                                 for co,v in zip(h,values))/length**j

    def delta(self,x,j,k):
        out = np.empty((len(self.t),len(self.theta),3))
        for i,sl in enumerate(self.slices):
            out[...,i] = (self.bs[i][j] @ x[sl].reshape(self.dims[i]) @ self.ph[i][k].T)/self.L**j
        return out

    def field(self,x,j,k):
        return self.base[j,k]+self.delta(x,j,k)

    def adjoint(self,val,j,k):
        out = np.empty(self.n)
        for i,sl in enumerate(self.slices):
            out[sl] = (self.bs[i][j].T @ val[...,i] @ self.ph[i][k]).ravel()/self.L**j
        return out


def dot(a,b):
    return np.sum(a*b,axis=-1)


def remove_mean(a):
    return a-np.mean(a,axis=1,keepdims=True)


def measure(b,x):
    f,u,v = [b.field(x,*jk) for jk in ((0,0),(1,0),(0,1))]
    return f,u,v,dot(u,u),dot(u,v),dot(v,v)


class FrozenMetric:
    def __init__(self,b,x,angle_count):
        self.spans = b.spans
        nodes = (1.-np.cos(np.pi*np.arange(11)/10.))/2.
        self.nodes = nodes
        t = ((np.arange(self.spans)[:,None]+nodes)/self.spans).ravel()
        k = Shoulder(b.disk,b.L,b.eq,b.spans,b.mode,t,np.arange(angle_count)*2*np.pi/angle_count)
        g = np.mean(dot(k.field(x,0,1),k.field(x,0,1)),axis=1)
        self.words = g.reshape(self.spans,11)
        weights = np.r_[.5,np.ones(9),.5]*(-1.)**np.arange(11)
        self.poly = [BarycentricInterpolator(nodes,z,wi=weights) for z in self.words]

    def __call__(self,t):
        cell = np.minimum((t*self.spans).astype(int),self.spans-1)
        return np.array([float(self.poly[i](s*self.spans-i)) for s,i in zip(t,cell)])


class Objective:
    pairs = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]

    def __init__(self,b,p,reg,target=None):
        self.b,self.p,self.reg,self.target = b,p,reg,target
        self.last = None
        self.count = 0
        self.Kcap = p["curvature_price"]
        w = b.disk.point(p["witness_x"],0.)
        self.opposite = np.array([-w[0],0.,w[2]]) @ b.disk.frame
        self.dirs = [(np.cos(a),np.sin(a)) for a in np.arange(p["shape_directions"])*np.pi/p["shape_directions"]]
        self.weights = np.sqrt(len(b.t)*len(b.theta))
        self.nrows = 7+len(self.dirs)
        self.shape = (self.nrows,len(b.t),len(b.theta))
        self.costs = []

    def prepare(self,x):
        if self.last is not None and np.array_equal(self.last,x):
            return
        self.last = x.copy()
        fields = [self.b.field(x,*jk) for jk in self.pairs]
        f,u,v,uu,uv,vv = fields
        nt,na = f.shape[:2]
        res = np.zeros(self.shape)
        gs = [np.zeros(self.shape+(3,)) for _ in self.pairs]
        F,U,V,UU,UV,VV = gs
        g11,g12,g22 = dot(u,u),dot(u,v),dot(v,v)
        res[0],U[0] = g11-1.,2*u
        rs = np.sqrt(2.)
        res[1],U[1],V[1] = rs*g12,rs*v,rs*u
        self.center = self.target is None
        res[2] = remove_mean(g22) if self.center else g22-self.target(self.b.t)[:,None]
        V[2] = 2*v
        flip = self.p["geometry_price"]
        def high(i,value,g,vec):
            active = value>0
            res[i] = flip*np.maximum(value,0.)
            g[i] = flip*active[...,None]*vec
        high(3,-f[...,2],F,np.array([0.,0.,-1.]))
        high(4,dot(f,f)-self.p["body_radius"]**2,F,2*f)
        h = f-self.opposite
        high(5,self.p["witness_ball"]**2-dot(h,h),F,-2*h)
        cross = f[...,0]*v[...,1]-f[...,1]*v[...,0]
        sign = (cross < self.p["section_area_floor"])[...,None]
        res[6] = flip*np.maximum(self.p["section_area_floor"]-cross,0.)
        F[6,...,0] = -flip*sign[...,0]*v[...,1]
        F[6,...,1] = flip*sign[...,0]*v[...,0]
        V[6,...,0] = flip*sign[...,0]*f[...,1]
        V[6,...,1] = -flip*sign[...,0]*f[...,0]
        normal0 = np.cross(u,v)
        norm = np.maximum(np.linalg.norm(normal0,axis=-1),1.e-12)
        normal = normal0/norm[...,None]
        price = self.p["bending_weight"]
        for j,(c,s) in enumerate(self.dirs,7):
            tangent = c*u+s*v
            acc = c*c*uu+2*c*s*uv+s*s*vv
            hess = dot(acc,normal)
            g = np.abs(hess)/self.Kcap-dot(tangent,tangent)
            gate = price*(g>0)[...,None]
            res[j] = price*np.maximum(g,0.)
            unit = (np.sign(hess)/self.Kcap)[...,None]
            ngrad = gate*unit*(acc-hess[...,None]*normal)/norm[...,None]
            U[j] = np.cross(v,ngrad)-2*c*gate*tangent
            V[j] = np.cross(ngrad,u)-2*s*gate*tangent
            UU[j] = gate*unit*c*c*normal
            UV[j] = gate*unit*2*c*s*normal
            VV[j] = gate*unit*s*s*normal
        self.gs,self.res = gs,res
        self.count += 1

    def fun(self,x):
        self.prepare(x)
        out = np.r_[self.res.ravel()/self.weights,self.reg*x]
        if self.count % 12 == 1:
            print(json.dumps({"event":"objective","evaluations":self.count,
                              "rms_scaled":float(np.linalg.norm(out)),
                              "gram_max":float(np.max(np.abs(self.res[:3])))}),flush=True)
        return out

    def jac(self,x):
        self.prepare(x)
        ctx = self
        gs = self.gs
        shape = self.shape
        n = self.b.n
        def mv(dx):
            dx = dx.ravel()
            out = np.zeros(shape)
            for g,(j,k) in zip(gs,ctx.pairs):
                out += np.einsum("rsnc,snc->rsn",g,ctx.b.delta(dx,j,k))
            if ctx.center:
                out[2]=remove_mean(out[2])
            return np.r_[out.ravel()/ctx.weights,ctx.reg*dx]
        def rmv(d):
            d = d.ravel()
            vf = d[:np.prod(shape)].reshape(shape).copy()/ctx.weights
            if ctx.center:
                vf[2]=remove_mean(vf[2])
            out = ctx.reg*d[-n:].copy()
            for g,(j,k) in zip(gs,ctx.pairs):
                out += ctx.b.adjoint(np.einsum("rsn,rsnc->snc",vf,g),j,k)
            return out
        return LinearOperator((int(np.prod(shape))+n,n),matvec=mv,rmatvec=rmv,dtype=float)


def angular_grid(n,shift=0.):
    return (np.arange(n)+shift)*2.*np.pi/n


def sampling(disk,design,stage,dense=False):
    n = stage["radial"] if not dense else stage["check_radial"]
    a = stage["angular"] if not dense else stage["check_angular"]
    t = (1.-np.cos(np.pi*np.arange(n)/(n-1)))/2.
    return Shoulder(disk,design["length"],design["equator_radius"],stage["spans"],stage["mode"],
                    t,angular_grid(a,.173 if dense else 0.))


def geometric_seed(b,design):
    t = b.t
    power = design["radial_power"]
    width = b.L*.5*np.exp(betaln(.5,power+1.))
    radius = 1.+width*betainc(.5,power+1.,t*t)
    shift = design["fillet_shift"]*smooth(t)
    xi = radius[:,None]*np.cos(b.theta)
    y = radius[:,None]*np.sin(b.theta)
    pos = b.disk.point(xi,y) @ b.disk.frame
    angle = b.disk.angles(xi)[0]-b.disk.angle
    pos[...,0] += shift[:,None]*np.sin(angle)
    pos[...,2] -= shift[:,None]*np.cos(angle)
    pos[...,2] *= (1.-2.*t**3+t**4)[:,None]
    return pos


def fit_initial(b,design,old=None):
    if old is None and design["seed"]=="hermite":
        return np.zeros(b.n)
    a = angular_grid(max(4*b.mode+12,64))
    t = np.linspace(0.,1.,max(7*b.spans+11,51))
    work = Shoulder(b.disk,b.L,b.eq,b.spans,b.mode,t,a)
    if old is None:
        goal = geometric_seed(work,design)
    else:
        base,x = old
        goal = Shoulder(b.disk,base.L,base.eq,base.spans,base.mode,t,a).field(x,0,0)
    delta = goal-work.base[0,0]
    out = np.zeros(work.n)
    for i,sl in enumerate(work.slices):
        coeff = np.linalg.lstsq(work.bs[i][0],delta[...,i],rcond=None)[0]
        out[sl] = np.linalg.lstsq(work.ph[i][0],coeff.T,rcond=None)[0].T.ravel()
    return out


def field_metrics(b,x,target):
    f,u,v,E,F,G = measure(b,x)
    g = np.mean(G,axis=1)[:,None] if target is None else target(b.t)[:,None]
    if np.min(g)<=0:
        raise FloatingPointError("nonpositive designed angular metric")
    h = .5*(E+G/g)
    delta = np.sqrt((.5*(E-G/g))**2+F**2/g)
    gram = np.maximum(np.abs(h+delta-1.),np.abs(h-delta-1.))
    normal0 = np.cross(u,v)
    area = np.linalg.norm(normal0,axis=-1)
    normal = normal0/np.maximum(area[...,None],1.e-15)
    l,m,n = [dot(normal,b.field(x,*jk)) for jk in ((2,0),(1,1),(0,2))]
    det = np.maximum(area**2,1.e-30)
    half = .5*(G*l-2*F*m+E*n)/det
    disc = np.sqrt(np.maximum(0.,half**2-(l*n-m*m)/det))
    curv = np.maximum(np.abs(half+disc),np.abs(half-disc))
    return {"gram_max":float(np.max(gram)),"gram_rms":float(np.sqrt(np.mean(gram**2))),
            "gram_components":[float(np.max(np.abs(vv))) for vv in (E-1.,F,G-g)],
            "shoulder_K_abs_sample_max":float(np.max(curv)),"min_area":float(np.min(area)),
            "angular_target_min":float(np.min(g)),"height_in_equator_frame_min":float(f[...,2].min()),
            "origin_radius_sample_max":float(np.linalg.norm(f,axis=-1).max()),
            "samples":[len(b.t),len(b.theta)]},f,normal


def cloud(b,x,radial,angles,p):
    disk = b.disk
    rs = np.linspace(0.,1.,radial)
    a = angular_grid(angles)
    xx,yy = (rs[1:,None]*v for v in (np.cos(a),np.sin(a)))
    xx=np.r_[0.,xx.ravel()]; yy=np.r_[0.,yy.ravel()]
    pos = disk.point(xx,yy) @ disk.frame
    beta = disk.angles(xx)[0]
    normal = np.stack([-np.sin(beta),np.zeros_like(beta),np.cos(beta)],axis=-1) @ disk.frame
    t = np.linspace(0.,1.,radial)[1:]
    k = Shoulder(disk,b.L,b.eq,b.spans,b.mode,t,a)
    patch = k.field(x,0,0)
    n = np.cross(k.field(x,1,0),k.field(x,0,1))
    n /= np.maximum(np.linalg.norm(n,axis=-1,keepdims=True),1.e-15)
    # Outward orientation is coherent at the disk rim by the exact jets.
    top = np.vstack([pos,patch.reshape(-1,3)])
    ntop = np.vstack([normal,n.reshape(-1,3)])
    low = top[:-angles].copy()
    nlow = ntop[:-angles].copy()
    low[:,2] *= -1.; nlow[:,2] *= -1.
    shape = np.vstack([top,low]) @ disk.frame.T
    normals = np.vstack([ntop,nlow]) @ disk.frame.T
    # Add the same fine samples inside each exact fixed circular marker.
    # Top disk samples entering a support are raised below, after phase rotation.
    extra = []
    for cx,cy,br,height in p["markers"]:
        brs = np.linspace(0.,br,5)[1:]
        ang = angular_grid(16)
        xm = (cx+brs[:,None]*np.cos(ang)).ravel()
        ym = (cy+brs[:,None]*np.sin(ang)).ravel()
        xm=np.r_[cx,xm]; ym=np.r_[cy,ym]
        extra.append(np.stack([xm,ym,np.full_like(xm,disk.H)],axis=-1))
    return shape,normals,len(pos),np.vstack(extra)


def phases(b,x,p):
    shape,normals,ndisk,extra = cloud(b,x,p["cloud_radial"],p["cloud_angular"],p)
    ys,ns = [],[]
    for phase in p["phases"]:
        c,s=np.cos(phase),np.sin(phase)
        rot=np.array([[c,s,0.],[-s,c,0.],[0.,0.,1.]])
        pts=np.vstack([shape@rot,extra.copy()])
        nor=np.vstack([normals@rot,np.tile([0.,0.,1.],(len(extra),1))])
        idx=np.r_[np.arange(ndisk),np.arange(len(shape),len(pts))]
        for cx,cy,br,height in p["markers"]:
            dx,dy=pts[idx,0]-cx,pts[idx,1]-cy
            z=1.-(dx*dx+dy*dy)/(br*br)
            use=z>0
            ids=idx[use]; z=z[use]
            pts[ids,2]+=height*z**4
            nor[ids]=np.stack([8*height*dx[use]*z**3/br**2,
                               8*height*dy[use]*z**3/br**2,np.ones_like(z)],axis=-1)
            nor[ids]/=np.linalg.norm(nor[ids],axis=-1,keepdims=True)
        ys.append(pts);ns.append(nor)
    tree0=cKDTree(ys[0])
    wit=b.disk.point(p["witness_x"],0.)
    out=[]
    for i,(pts,nor) in enumerate(zip(ys,ns)):
        far2=0.; ratio=0.
        for a in range(0,len(pts),96):
            sl=slice(a,a+96)
            chord=pts[None,:,:]-pts[sl,None,:]
            dist2=dot(chord,chord)
            far2=max(far2,float(dist2.max()))
            proj=np.abs(np.einsum("bij,bj->bi",chord,nor[sl]))
            den=np.where(dist2>1.e-20,dist2,np.inf)
            ratio=max(ratio,float(np.max(2*proj/den)))
        tree=cKDTree(pts)
        out.append({"phase":p["phases"][i],"sample_diameter":float(np.sqrt(far2)),
                    "sample_Hausdorff_from_phase0":float(max(tree.query(ys[0])[0].max(),
                                                             tree0.query(pts)[0].max())),
                    "witness_to_sample_cloud":float(tree.query(wit)[0]),
                    "sample_two_sided_chord_inverse_reach_max":ratio,"cloud_points":len(pts)})
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--params",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    param_path=Path(args.params); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    src=Path(__file__).read_bytes(); pars=param_path.read_bytes()
    p=json.loads(pars)
    summary={"schema":"bent-disk-shoulder/v1","source_sha256":digest_bytes(src),
             "params_sha256":digest_bytes(pars),"python":sys.version.split()[0],
             "numpy":np.__version__,"scipy":scipy.__version__,"stages":[],
             "scope":"Exact material disk and C2 seam constraints. Finite approximate shoulder. All reported numeric geometry is sampled; no rigorous reach, embedding, exact root or strong closed-family assertion."}
    begin=time.monotonic()
    def save():
        summary["elapsed_seconds"]=time.monotonic()-begin
        put_json(out/"summary.json",summary)
    save()
    def run(design,stage,old=None,target=None):
        pb=dict(p["disk"])
        pb.update({k:design[k] for k in ("height","angle")})
        disk=Disk(pb)
        b=sampling(disk,design,stage)
        x0=fit_initial(b,design,old)
        obj=Objective(b,p,stage["regularizer"],target)
        tstart=time.monotonic()
        # Check the complete objective derivative in a reproducible dense direction.
        # Positive-part corners have a one-sided derivative; report the check rather
        # than treating an active-constraint switch as a physical failure.
        dv=np.cos(.917*np.arange(b.n)+.121);dv/=np.linalg.norm(dv)
        v0=obj.fun(x0)
        jac=obj.jac(x0)
        jv=jac.matvec(dv)
        probe=np.sin(.137*np.arange(len(v0))+.518);probe/=np.linalg.norm(probe)
        jt=jac.rmatvec(probe)
        adjoint_error=abs(float(jv@probe-dv@jt))
        step=p["jacobian_probe"]
        fd=(obj.fun(x0+step*dv)-obj.fun(x0-step*dv))/(2*step)
        fd_error=float(np.linalg.norm(fd-jv)/max(np.linalg.norm(jv),1.e-15))
        interim = {"cost":float("inf"),"iteration":0,"stamp":0.}
        def actual_fun(z):
            fv=obj.fun(z)
            interim["iteration"]+=1
            value=float(.5*(fv@fv))
            if value<interim["cost"]:
                interim["cost"]=value
                now=time.monotonic()
                if now-interim["stamp"]>15. or interim["iteration"]==1:
                    interim["stamp"]=now
                    with open(out/"current-field.tmp","wb") as handle:
                        np.savez(handle,coefficients=z)
                    os.replace(out/"current-field.tmp",out/"current-field.npz")
                    summary["in_progress"]={"stage":len(summary["stages"]),"design":design["id"],
                         "configuration":stage["id"],"actual_objective_call":interim["iteration"],
                         "observed_best_cost":value,"x_sha256":array_digest(z),"shape":list(z.shape)}
                    save()
            return fv
        scale=np.empty(b.n)
        for i,sl in enumerate(b.slices):
            modes=np.arange(1 if i==1 else 0,b.mode+1)
            b0=np.mean(b.bs[i][0]**2,axis=0)[:,None]
            b1=np.mean((b.bs[i][1]/b.L)**2,axis=0)[:,None]
            b2=np.mean((b.bs[i][2]/b.L**2)**2,axis=0)[:,None]
            stiffness=(p["bending_weight"]/p["curvature_price"])**2
            scale[sl]=1./np.sqrt(np.maximum(1.e-6,b1+b0*modes**2+
                            stiffness*(b2+2*b1*modes**2+b0*modes**4))).ravel()
        result=least_squares(actual_fun,x0,jac=obj.jac,method="trf",tr_solver="lsmr",x_scale=scale,
                             tr_options={"maxiter":stage["lsmr_iterations"],"atol":1.e-7,"btol":1.e-7},
                             ftol=1.e-10,xtol=1.e-10,gtol=1.e-10,max_nfev=stage["max_evaluations"])
        x=np.asarray(result.x,dtype=np.float64)
        verify=sampling(disk,design,stage,True)
        metrics,f,_=field_metrics(verify,x,target)
        metrics_train,_,_=field_metrics(b,x,target)
        point=disk.point(p["witness_x"],0.)
        opposite=np.array([-point[0],0.,point[2]]) @ disk.frame
        dshoulder=float(np.linalg.norm(f-opposite,axis=-1).min())
        score=(metrics["gram_max"]+max(0.,metrics["shoulder_K_abs_sample_max"]/p["curvature_price"]-1.)*.3+
               max(0.,p["witness_ball"]-dshoulder)*3.+max(0.,metrics["origin_radius_sample_max"]-p["body_radius"])*3.+
               max(0.,-metrics["height_in_equator_frame_min"])*2.)
        record={"stage":len(summary["stages"]),"design":design,"configuration":stage,
                "fixed_angular_target":target is not None,
                "fixed_angular_target_sha256":array_digest(target.words) if target is not None else None,
                "source_x_sha256":array_digest(old[1]) if old else None,"start_x_sha256":array_digest(x0),
                "x_sha256":array_digest(x),"x_shape":[b.n],"component_shapes":[list(a) for a in b.dims],
                "nfev":int(result.nfev),"njev":int(result.njev or 0),"termination":int(result.status),
                "solver_message":str(result.message),"cost":float(result.cost),"optimality":float(result.optimality),
                "jacobian_adjoint_abs":adjoint_error,"jacobian_fd_relative":fd_error,
                "train":metrics_train,"independent_grid":metrics,"ranking_score":float(score),
                "curve_witness":point.tolist(),"witness_to_comparison_shoulder_samples":dshoulder,
                "witness_separation_from_lower_halfspace_if_upper_nonnegative":float(opposite[2]),
                "stage_seconds":time.monotonic()-tstart}
        index=record["stage"]
        np.savez(out/("stage-%02d.npz"%index),coefficients=x,
                 target_nodes=np.empty((0,11)) if target is None else target.words)
        summary.pop("in_progress",None)
        summary["stages"].append(record)
        save()
        print(json.dumps({"event":"completed_stage","stage":index,"design":design["id"],
                          "nfev":record["nfev"],"x_sha256":record["x_sha256"],
                          "gram":metrics["gram_max"],"curvature":metrics["shoulder_K_abs_sample_max"],
                          "rank":score}),flush=True)
        return b,x,record

    try:
        pool=[]
        for design in p["designs"]:
            b,x,rec=run(design,p["coarse"])
            pool.append((rec["ranking_score"],design,b,x,rec))
        _,design,base,x,rec=min(pool,key=lambda z:z[0])
        summary["selected_design"]=design["id"]
        summary["selected_coarse_stage"]=rec["stage"]
        base,x,rec=run(design,p["medium"],(base,x))
        base,x,rec=run(design,p["fine"],(base,x))
        frozen=FrozenMetric(base,x,p["freeze_angular"])
        summary["frozen_material_target"]={"sha256":array_digest(frozen.words),
                    "shape":list(frozen.words.shape),"source_stage":rec["stage"],
                    "source_x_sha256":array_digest(x),"angular_count":p["freeze_angular"],
                    "description":"Per-span degree-ten Chebyshev-Lobatto interpolation of shared angular mean Gram. Fixed through both subsequent resolutions; no phase interpolation."}
        # Signed physical arclength s=L t and the disk radius remain identical.
        save()
        full=[(base,x,rec)]
        for stage in p["fixed_refinements"]:
            base,x,rec=run(design,stage,(base,x),frozen)
            full.append((base,x,rec))
        for base,x,rec in full:
            rec["sampled_closed_phases"]=phases(base,x,p)
            save()
        summary["last_stage"]=rec["stage"]
        summary["last_x_sha256"]=array_digest(x)
        summary["status"]="completed_finite_design_and_two_fixed_target_resolutions"
        save()
    except Exception as exc:
        summary["status"]="runtime_failure"
        summary["exception_type"]=type(exc).__name__
        summary["exception"]=str(exc)[:1200]
        save()
        traceback.print_exc()
        return 1
    return 0


if __name__=="__main__":
    raise SystemExit(main())
