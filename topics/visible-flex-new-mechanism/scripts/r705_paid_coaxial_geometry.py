"""Restore the paid R688 interpolants. Build the new coaxial three-dimensional geometry."""
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.integrate._ivp.common import OdeSolution
from scipy.integrate._ivp.rk import Dop853DenseOutput, RkDenseOutput
from scipy.interpolate import BPoly, BSpline, CubicSpline, RectBivariateSpline
from scipy.optimize import brentq
from scipy.sparse import csr_matrix

from r688_actual_r664_window_collars import Centerline, Collar, active_width, band, require_public, smooth
from r688_closed_shell_observer import KnownBody, REFLECT, unit, vec3, normal_and_curvature
from r688_joint_window_field import extrema, whiten_metric
from r688_true_caps_and_reference_sections import D, EPS_CAP, HOLE, ReferenceSections, W
from r709_paid_physical_spline_strip_bound import consume_arrays
from r688_two_port_material_atlas import MaterialAtlas, differentiate, frame, rotation, separated, softmax2, step_vec

Q = np.array([1., -1., -1.])
EX = np.array([1., 0., 0.])
PARENT = dict(run=46148075849, job=140988404437,
              source='5374a6817d9761fbea489d44803e4728ddc22d0b',
              request_sha256='0218265a5a3cd1fb41d1544308679580c7618bfe07f0fbc043d8f43d8951ea63')


def digest(data):
    return hashlib.sha256(data).hexdigest()


class PaidArchive:
    """The new request binds this manifest, its FINAL and every consumed array."""
    def __init__(self, manifest, manifest_sha256, root):
        require_public()
        self.root = Path(root)
        literal = Path(manifest).read_bytes()
        if digest(literal) != manifest_sha256:
            raise ValueError('R705 paid-manifest digest differs')
        self.manifest = json.loads(literal)
        if self.manifest['parent'] != PARENT:
            raise ValueError('R688 source/request/run/job differs')
        self.final = self.read_bytes(self.manifest['final'],Path(manifest).parent)
        self.record = json.loads(self.final)
        self.used = {}

    def read_bytes(self, item, directory=None):
        name = item['name']
        if name != Path(name).name:
            raise ValueError('Invalid archive basename')
        data = ((self.root if directory is None else directory)/name).read_bytes()
        if len(data) != item['bytes'] or digest(data) != item['sha256']:
            raise ValueError('Wrong paid object '+name)
        return data

    def arrays(self, name):
        from io import BytesIO
        item = self.manifest['objects'][name]
        if item['name'] != name:
            raise ValueError('Paid object name mismatch')
        raw = self.read_bytes(item)
        self.used[name] = item['sha256']
        return np.load(BytesIO(raw), allow_pickle=False)


def dense(fields, prefix):
    """Use the original SciPy dense polynomials and the original piece selector."""
    tt = fields[prefix+'_breaks']
    start, end = fields[prefix+'_t_old'], fields[prefix+'_t']
    initial = fields[prefix+'_y_old']
    if prefix+'_F' in fields:
        cls, coeff = Dop853DenseOutput, fields[prefix+'_F']
    else:
        cls, coeff = RkDenseOutput, fields[prefix+'_Q']
    return OdeSolution(tt, [cls(a,b,y,c) for a,b,y,c in zip(start,end,initial,coeff,strict=True)])


def spline(fields, key):
    tck = tuple(fields[key+'_'+str(i)] for i in range(3))
    return RectBivariateSpline._from_tck(tck+(5,5))


def reference(archive):
    ref = ReferenceSections.__new__(ReferenceSections)
    with archive.arrays('true-reference.npz') as z:
        ref.angle = BSpline(z['section_angle_knots'], z['section_angle_c'], int(z['section_angle_degree']))
        ref.starts, ref.cuts = z['starts'], z['cuts']
        ref.arc_lengths = np.diff(ref.cuts)
        for key in ('xf','height','S','sphere_turn','source_turn'):
            setattr(ref,key,float(z[key]))
        ref.tube_length = float(z['tube'])
        ref.tables = [spline(z,'cap_'+str(i)) for i in range(2)]
        ref.cap_normals = [spline(z,'cap_'+str(i)) for i in range(2,5)]
        paths = [dense(z,'path_'+str(i)) for i in range(6)]
    ref.turns = [None,*paths[:3]]
    ref.crown,ref.sphere_arc,ref.source_arc = paths[3:]
    ref.phi,ref.sphere_r = np.pi/3,.11
    ref.theta_b,zb,ref.rb = ref.crown(.001)
    ref.xb = .96-zb
    ref.crown_end_x = ref.xb-ref.sphere_arc(ref.sphere_turn)[0]
    ref.meridian_end = .00025+ref.sphere_turn+ref.tube_length+ref.source_turn
    return ref


class CenteredLine:
    """In the h_lambda frame, C(v) = (Cold(v)-Cold(-v))/2, exactly odd."""
    fields = Centerline.fields

    def __init__(self, z, phase):
        self.old = Centerline.__new__(Centerline)
        self.phase = float(phase)
        self.old.curve = BPoly(z['physical_centerline_bernstein'], z['physical_centerline_knots'])
        self.old.far = dense(z,'line')(1.)[1:]
        self.curve = self.old.curve
        self.center = np.r_[0.,(self.old.far+[-1.,0.])/2]

    def cartesian(self,v,order=0):
        return (self.old.cartesian(v,order)-(-1)**order*self.old.cartesian(-np.asarray(v),order))/2


def phase_objects(archive, phase, h):
    name='actual-line-collars-'+str(phase)+'.npz'
    with archive.arrays(name) as z:
        if float(z['phase']) != phase:
            raise ValueError('Restored phase mismatch')
        line = CenteredLine(z,phase)
        try:
            line.physical_strip_bounds=consume_arrays(z,phase,archive.used[name])
        except (ValueError,ArithmeticError) as error:
            line.physical_strip_bounds=dict(position_normal_gate=False,reason=str(error),
                C2_curve_seam_and_parent_plate_certificate=False)
        grids = []
        for grid in range(2):
            pair = []
            for j,sign in enumerate((1,-1)):
                coll = Collar.__new__(Collar)
                coll.h,coll.sign,coll.line = h,sign,line
                coll.splines = [spline(z,f'grid{grid}_pulse{j}_field{k}') for k in range(14)]
                pair.append(coll)
            grids.append(pair)
    return line,grids


def actual_strip(pair,t,v,side):
    """Right upper or its prescribed half-turn image on the lower outer band."""
    vv = v if side == 1 else -v
    ix = 0 if np.max(vv)<0 else 1
    if np.min(vv)*np.max(vv)<=0:
        raise ValueError('A collar call must select one connected pulse')
    jets = list(pair[ix].position_jets(t,vv))
    jets[0] = jets[0]+[0.,0.,D]
    if side < 0:
        jets = [j*Q*sign for j,sign in zip(jets,(1,1,-1,1,-1,1),strict=True)]
    return jets


class CoaxialAtlas(MaterialAtlas):
    def __init__(self, ref, source, angular, rings, h, shift):
        if angular%2:
            raise ValueError('An even angular grid is necessary')
        self.ref,self.h,self.source=ref,h,source
        self.L=.22
        self.end=ref.meridian_end+self.L
        material=np.linspace(-1.,1.,16001)
        _,yy,zz=source.fields(material)
        self.inv=CubicSpline(yy,material,extrapolate=False)
        self.vstar=brentq(lambda v:float(source.fields(np.asarray(v))[1]),0.,.001,xtol=5e-16)
        self.Ylo,self.Yhi=yy[0],yy[-1]
        self.Zlo,self.Zhi=zz[0],zz[-1]
        def ysz(v):
            _,y,z=source.fields(np.atleast_1d(v))
            return y,z
        angles=list(2*np.pi*(np.arange(angular)+shift)/angular)
        outer_arc=ref.S+.00025
        corner_v=1-EPS_CAP/2
        corner_angles=[]
        for v in [-corner_v,-.93,-.90,-.89,-.88,-.64,-.63,-.62,-.59,0,
                  .59,.62,.63,.64,.88,.89,.90,.93,corner_v]:
            y,z=ysz(v)
            for side in (-1,1):
                angle=float(np.arctan2(z[0]+side*outer_arc,y[0])%(2*np.pi))
                angles.append(angle)
                if abs(v)==corner_v:
                    corner_angles.append(angle)
                    angles.extend(angle+j for j in (-.00008,-.000035,-.000012,.000012,.000035,.00008))
        self.theta=separated([a%(2*np.pi) for a in angles],1.e-7)
        self.corner_ray_indices=[]
        for center in corner_angles:
            for off in (-.00008,-.000035,-.000012,0.,.000012,.000035,.00008):
                gap=abs((self.theta-center-off+np.pi)%(2*np.pi)-np.pi)
                idx=int(np.argmin(gap))
                if gap[idx]>1.e-7:
                    raise ArithmeticError("R705 actual corner neighbor was lost")
                self.corner_ray_indices.append(idx)
        if len(set(self.corner_ray_indices))!=28:
            raise ArithmeticError("R705 needs seven distinct rays at each of four physical corners")
        t1=.00025
        t2=t1+ref.sphere_turn; t3=t2+ref.tube_length; t4=ref.meridian_end
        sections=[(0,t1,4),(t1,t2,rings),(t2,t3,rings),(t3,t4,2*rings),(t4,self.end,3*rings)]
        coords=[]
        for a,b,k in sections:
            frac=np.arange(1,k)/k
            coords.extend([a,b,*list(a+(b-a)*(frac+shift/k))])
        coords.extend(self.end-i for i in [.00005,.00012,.0002,.00035,.0005,.00075,.0011,.0016,.0024,.0035,.006,.012,.022,.037])
        self.t=separated(coords,1e-7)
        self.T,self.A=np.meshgrid(self.t,self.theta,indexing='ij')
        co,si=np.cos(self.A),np.sin(self.A)
        def coords(r,cc,ss):
            y=r*cc; z=r*ss
            yc=np.clip(y,self.Ylo,self.Yhi)
            v=self.inv(yc)
            for _ in range(4):
                alpha,yy0,zz0=source.fields(v)
                if np.max(abs(yy0-yc))<4e-15:
                    break
                v=np.clip(v-(yy0-yc)/source.cartesian(v,1)[...,0],-1.,1.)
            alpha,yy0,zz0=source.fields(v)
            if np.max(abs(yy0-yc))>3e-14:
                raise ArithmeticError("Original material inverse failed on the true stored source line")
            return v+(y-yc),z-zz0,yy0+(y-yc),zz0
        # The perimeter intersection depends only on angle, once per actual ray.
        cc,ss=co[0],si[0]
        lo=np.full_like(cc,.198); hi=np.full_like(cc,2.)
        for _ in range(52):
            mid=(lo+hi)/2; v,s,y,zbase=coords(mid,cc,ss)
            val=softmax2(abs(v)/(1-EPS_CAP/2),abs(s)/outer_arc,.00002)
            hi=np.where(val>=1,mid,hi); lo=np.where(val<1,mid,lo)
        rr=(lo+hi)/2
        w=np.maximum(0,self.T-ref.meridian_end)
        r=HOLE+w+(rr[None,:]-HOLE-self.L)*smooth(w/self.L)
        self.v,self.s,self.y,self.z0=coords(r,co,si)
        self.outer=self.T>=ref.meridian_end
        self.wing=ref.S-abs(self.s)
        self.side=np.sign(self.s)
        self.gap=1-abs(self.v)
        self.width=active_width(self.v,h)
        self.cap_allow=smooth((self.gap-EPS_CAP)/.07)
        self.wing_allow=smooth((self.wing-self.width)/.07)
        self.bridge=(~self.outer)|(r<=.2005)
        self.free=np.where(self.outer,smooth((r-.2005)/.055)*self.cap_allow*self.wing_allow,0.)
        self.paid=self.bridge|(self.outer&((self.wing<=self.width)|(self.gap<=EPS_CAP)))
        self.outer_weight=np.where(self.outer,smooth((r-.2005)/.12),0.)
        self.tie=smooth((w/self.L-.18)/.54)
        outside=self.paid&~self.bridge
        if (np.any(self.tie[self.bridge]!=0) or np.any(self.tie[outside]!=1)
                or np.any(np.diff(outside.astype(int),axis=0)<0)):
            raise ArithmeticError("Actual crown/primary paid intervals and two-sided integration bands differ")
        self.Dt=differentiate(self.t,1); self.Dtt=differentiate(self.t,2)
        self.Da=differentiate(self.theta,1,True); self.Daa=differentiate(self.theta,2,True)
        self.Dt,self.Dtt,self.Da,self.Daa=map(csr_matrix,(self.Dt,self.Dtt,self.Da,self.Daa))
        # Piecewise linear integral is monotone on this deliberately nonuniform grid.
        self.I=np.zeros((len(self.t),len(self.t)))
        for i,dt in enumerate(np.diff(self.t),1):
            self.I[i]=self.I[i-1]; self.I[i,i-1:i+1]+=dt/2
        widths=(np.roll(self.theta,-1)-self.theta)%(2*np.pi)
        self.angular_weights=(widths+np.roll(widths,1))/2
        self.quad=(self.I[-1,:,None]*self.angular_weights[None,:])/(self.end*2*np.pi)
        self.geometry={}
        base=np.empty(self.T.shape+(3,))
        inner=~self.outer
        x,rad=ref.meridian(self.T[inner])
        base[inner]=np.stack((x,rad*co[inner],rad*si[inner]),axis=-1)
        s,v,y=self.s[self.outer],self.v[self.outer],self.y[self.outer]
        x,z=ref.section(s,v,y)
        base[self.outer]=np.stack((x,y,self.z0[self.outer]+z),axis=-1)
        self.base=base
        n = len(self.theta)//2
        if len(self.theta)!=2*n or np.max(abs(self.theta[n:]-self.theta[:n]-np.pi))>2e-12:
            raise ValueError('Unpaired physical angular grid')
        self.theta[n:] = self.theta[:n]+np.pi
        self.A = np.broadcast_to(self.theta,self.T.shape)
        self.n = n
        for name in ('outer','paid','bridge','tie','free','outer_weight','wing','width','cap_allow','wing_allow'):
            arr = getattr(self,name)
            if np.max(abs(arr[:,n:].astype(float)-arr[:,:n].astype(float)))>2e-8:
                raise ValueError('Unpaired material field '+name)
            arr[:,n:] = arr[:,:n]
        for arr in (self.s,self.v,self.y,self.z0,self.side):
            arr[:,n:] = -arr[:,:n]
        self.base[:,n:] = self.base[:,:n]*Q
        for name in ('Da','Daa'):
            arr = getattr(self,name).toarray()
            arr[n:,:] = np.roll(arr[:n,:],n,axis=1)
            setattr(self,name,csr_matrix(arr))
        self.angular_weights[n:] = self.angular_weights[:n]
        self.angular_weights *= 2*np.pi/self.angular_weights.sum()
        self.quad = self.I[-1,:,None]*self.angular_weights[None,:]/(self.end*2*np.pi)
        self.stencils={}
        for key,matrix in (('t',self.Dt),('tt',self.Dtt),('a',self.Da),('aa',self.Daa)):
            m=matrix.shape[0]
            idx=np.repeat(np.arange(m)[:,None],5,axis=1)
            coeff=np.zeros((m,5))
            for j in range(m):
                start,end=matrix.indptr[j:j+2]
                col=matrix.indices[start:end]
                idx[j,:len(col)]=col
                coeff[j,:len(col)]=matrix.data[start:end]
            if key in ('a','aa'):
                idx[self.n:]=(idx[:self.n]+self.n)%m
                coeff[self.n:]=coeff[:self.n]
            self.stencils[key]=(idx,coeff)

    def difference(self,X,key,axis):
        f=np.moveaxis(X,axis,0)
        idx,coeff=self.stencils[key]
        # Use neighbor differences for each row, so a rigid translation has zero jet
        # even when the geometric corner adds very closely spaced angular labels.
        out=np.einsum('ij,ij...->i...',coeff,f[idx]-f[:,None])
        return np.moveaxis(out,0,axis)

    def dt(self,X,order=1):
        return self.difference(X,'t' if order==1 else 'tt',0)

    def da(self,X,order=1):
        return self.difference(X,'a' if order==1 else 'aa',1)

    def _lifting(self,line,collars,source_collars):
        a,y,z=line.fields(self.v)
        a0,y0,z0=self.source.fields(self.v)
        P=self.base+self.outer_weight[...,None]*vec3(0.,y-y0,z-z0)
        rv=vec3(self.outer_weight*(a-a0),np.zeros_like(a),np.zeros_like(a))
        for side in (-1,1):
            for sign in (-1,1):
                weight=band(sign*self.v,-.907,-.90,-.62,-.613)
                mask=(self.outer&(self.side==side)&(self.wing>=0)&(self.wing<=2.3*self.h)&(weight>0))
                if not np.any(mask):
                    continue
                t,v=self.wing[mask],self.v[mask]
                pc,pt,pv,*_=actual_strip(collars,t,v,side)
                _,ot,ov,*_=actual_strip(source_collars,t,v,side)
                old_line=vec3(W+t,y[mask],z[mask]+side*D)
                wt=weight[mask]*(1-smooth((t/self.h-1)/1.3))
                P[mask]+=wt[:,None]*(pc-old_line)
                rel=frame(pt,pv)@frame(ot,ov).swapaxes(-1,-2)
                old=rotation(rv[mask])
                rv[mask]=step_vec(rotation(wt[:,None]*step_vec(rel@old.swapaxes(-1,-2)))@old)
        # Pair actual second-half values, including every derivative of the material lift.
        P[:,self.n:]=P[:,:self.n]*Q
        rv[:,self.n:]=rv[:,:self.n]*Q
        return P,rotation(rv)


class CoaxialBody(KnownBody):
    def cloud(self,line,collars,h):
        pts=[]; normals=[]; tags=[]
        def add(x,n,tag=0,mirror=False,half=False):
            x=x.reshape(-1,3); n=n.reshape(-1,3)
            for zz,nn in ([(x,n),(x*Q,n*Q)] if half else [(x,n)]):
                pts.append(zz+line.center); normals.append(nn); tags.append(np.full(len(zz),tag))
                if mirror:
                    pts.append(zz*REFLECT+line.center); normals.append(nn*REFLECT)
                    tags.append(np.full(len(zz),-tag))
        near=np.r_[0.,line.cartesian(-1.)]
        orient=np.array([1.,-1.,1.])
        add(self.cap*orient+near,self.cap_n*orient,half=True)
        add(self.primary_shoulder*orient+near,self.primary_shoulder_n*orient,mirror=True,half=True)
        add(self.crown,self.crown_n,tag=1,mirror=True)
        v,u=np.meshgrid(self.v,self.u,indexing='ij')
        al,y,z=line.fields(v)
        add(vec3(u,y,z+D),vec3(0.,-np.sin(al),np.cos(al)),half=True)
        for sign in (1,-1):
            vv=sign*np.linspace(-.90,-.62,len(self.v))
            f,v=np.meshgrid(np.linspace(0.,1.,5),vv,indexing='ij')
            X,a,b,*_=actual_strip(collars,f*active_width(v,h),v,1)
            add(X,unit(np.cross(a,b)),mirror=True,half=True)
        return np.concatenate(pts),np.concatenate(normals),np.concatenate(tags)


def strip_readout(pair,source,h):
    rows=[]
    for sign in (1,-1):
        vv=sign*np.linspace(-.90,-.62,301)
        f,v=np.meshgrid(np.linspace(0,1,13),vv,indexing='ij')
        t=f*active_width(v,h)
        for side in (1,-1):
            X,a,b,aa,ab,bb=actual_strip(pair,t,v,side)
            N,k,sine,g=normal_and_curvature(a,b,aa,ab,bb)
            g0=normal_and_curvature(*actual_strip(source,t,v,side)[1:])[3]
            line=pair[0].line
            ang,y,z=line.fields(v)
            plate=vec3(W,y,z+side*D)
            target=vec3(0.,-np.sin(ang),np.cos(ang))
            rows.append(dict(sign=sign,side=side,position_jet_max_abs_k=float(k.max()),
                min_param_sine_squared=float(sine.min()),max_relative_reference_gram=float(extrema(whiten_metric(g,g0)).max()),
                distance_to_plate_max=float(np.linalg.norm(X-plate,axis=-1).max()),
                near_plate_unoriented_normal_max=float(np.minimum(np.linalg.norm(N-target,axis=-1),np.linalg.norm(N+target,axis=-1)).max())))
    return rows
