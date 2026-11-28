"""Independent R740 weak-baseline closed source, true pulse collars and moving frame."""
import hashlib
import importlib.util
from pathlib import Path

import numpy as np

from r688_actual_r664_window_collars import require_public
from r733_inserted_meridian import ANGLE, BUFFER, LEG, LENGTH, START_X
from r733_physical_disk import R733Profile, R733Build, S_START, FILLET_START, TOTAL, material_breaks
from r740_material_rotation_space import GLOBAL_BREAKS, FILLET_BREAKS, install


HERE = Path(__file__).resolve().parent
BASELINE = .0052
INCREMENT = 1.0148
B0 = BASELINE/(.102*.998)
PINS = {
    "r732_disk_solver.py": "ed1dd8910eaf8dba190308d7717a4ec9053302f62e1181d10b446f9b24257472",
    "r732_disk_qualification.py": "08feb20d441a5695b6d07e531d71ad3569afe7f874637ef8926a23041855a033",
    "r732_disk_fields.py": "c403b3d979273760fe5ccfd68ba5f7c929f56a28d9113df4770e5a346a109d71",
    "r732_physical_disk.py": "752165ed2eac07e18c9993ede8218a15de16a8820d42210f1cf801d346d10369",
    "r732_closed_ring.py": "58c04599e8d24b0aee8204426491fb0d0132922900b2014fdcbab0f4b1a578e0",
    "r732_compensated_pulses.py": "8df0b12620daf51978873d29319da4b05028088803de570c0995ad98448c7f11",
}


def bound_module(label,name):
    data=(HERE/name).read_bytes()
    if hashlib.sha256(data).hexdigest()!=PINS[name]:
        raise ValueError("different pinned numerical entry " + name)
    spec=importlib.util.spec_from_file_location(label,HERE/name)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Rebind every native differentiating, source, and compensated ODE reference.
# These are private module namespaces. No object from a strong-source run is loaded.
pulse=bound_module("_r740_pulse","r732_compensated_pulses.py")
pulse.B0=B0
pulse.PHASE_HEIGHT=INCREMENT
ring=bound_module("_r740_ring","r732_closed_ring.py")
ring.PARTS=((.205,.102,BASELINE),(.846,.102,-BASELINE),
            (.206,.100,INCREMENT),(.847,.100,-INCREMENT))
physical=bound_module("_r740_disk","r732_physical_disk.py")
physical.B0,physical.Pulse,physical.Ring,physical.angles=B0,pulse.Pulse,ring.Ring,ring.angles
fields=bound_module("_r740_field","r732_disk_fields.py")
fields.B0,fields.angles,fields.line_k=B0,ring.angles,ring.line_k
fields.physical_psi,fields.time_from_x,fields.native_w=physical.physical_psi,physical.time_from_x,physical.native_w


class R740Frame(fields.Frame):
    def __init__(self,build,phase,r,s,degree):
        super().__init__(build,phase,r,s,degree)
        install(self,build)
        if phase==0:
            return
        _,_,xr,ur,_,_,ell=build.profile.read(self.r)
        mask=ell>S_START
        if not np.any(mask):
            return
        ss=self.s[mask]; rr=self.r[mask]; el=ell[mask]
        target=build.target(phase)
        _,kind,v=target.label(ss)
        prim=(kind==0)|(kind==2)
        dv=np.where(kind==0,target.length,np.where(kind==2,-target.length,0.))
        aa=(abs(v)-.949)/.05
        az=pulse.gate(1-aa)*prim
        az_s=-pulse.gate(1-aa,1)*np.sign(v)*dv/.05
        ratio=B0/(B0+phase*INCREMENT/(.100*.998))
        loss=(1-ratio)*az
        rho=1-loss
        rho_s=-(1-ratio)*az_s
        theta=np.full_like(rr,np.pi/2)
        theta_r=np.zeros_like(rr)
        on_s=el<=FILLET_START
        if np.any(on_s):
            local=np.clip(el[on_s]-S_START,0.,LENGTH)
            th,curve,_=build.profile.s.angle_jet(local)
            theta[on_s]=th
            theta_r[on_s]=-curve*np.hypot(xr[mask][on_s],ur[mask][on_s])
        arc=(~on_s)&(rr>=physical.R0)
        if np.any(arc):
            yy=np.clip((el[arc]-FILLET_START)/physical.L,0.,1.)
            theta[arc]=(np.pi/2)*physical.sym_step(yy)
            curve=(np.pi/2)*(physical.mollifier_cdf((yy-.001)/.0005)
                             -physical.mollifier_cdf((yy-.999)/.0005))/(.998*physical.L)
            theta_r[arc]=-curve*np.hypot(xr[mask][arc],ur[mask][arc])
        st,ct=np.sin(theta),np.where(theta==np.pi/2,0.,np.cos(theta))
        d2=loss*(2-loss)
        cc=np.sqrt(ct*ct+d2*st*st)
        den=cc+rho*ct
        sine=np.divide(st*d2,den,out=np.zeros_like(st),where=den>0)
        relative=-np.arctan2(sine,ct*cc+rho*st*st)
        rel_r=-theta_r*np.divide(d2,cc*den,out=np.zeros_like(st),where=(cc*den)>0)
        rel_s=np.divide(rho_s*st,cc,out=np.zeros_like(st),where=cc>0)
        g=np.ones_like(rr);gr=np.zeros_like(rr);gs=np.zeros_like(rr)
        core=rr<physical.R0
        if np.any(core):
            # Fade to the free Cartesian centre in true planar source distance,
            # never in its very slow outer polar coordinate.
            p,pr,ps,*_=self.j0
            yz=p[mask][core,1:]-build.ring.origin
            length=np.linalg.norm(yz,axis=-1)
            radial=np.divide(yz,length[:,None],out=np.zeros_like(yz),where=length[:,None]>0)
            z=(length-.006)/.05
            g[core]=pulse.gate(z)
            gd=pulse.gate(z,1)/.05
            gr[core]=gd*np.sum(radial*pr[mask][core,1:],axis=-1)
            gs[core]=gd*np.sum(radial*ps[mask][core,1:],axis=-1)
        delta,ds=target.angular_data(ss)
        X,Xp=fields.rotation(g*delta,0)
        Xr=(gr*delta)[:,None,None]*Xp
        Xs=(gs*delta+g*ds)[:,None,None]*Xp
        angle=g*relative
        ar=gr*relative+g*rel_r
        ass=gs*relative+g*rel_s
        _,T,N,k,_=target.jets(ss)
        E=np.zeros((len(ss),3,3));E[:,0,0]=1
        E[:,1:,1],E[:,1:,2]=T,N
        Es=np.zeros_like(E)
        Es[:,1:,1]=(k*target.length)[:,None]*N
        Es[:,1:,2]=-(k*target.length)[:,None]*T
        V,dV=fields.rotation(angle,1)
        Et=np.swapaxes(E,-1,-2)
        K=E@V@Et; Kt=E@dV@Et
        Ks=Es@V@Et+E@V@np.swapaxes(Es,-1,-2)+ass[:,None,None]*Kt
        self.base[mask]=X;self.br[mask]=Xr;self.bs[mask]=Xs
        keep=(az!=0)&((g!=0)|(gr!=0)|(gs!=0))
        idx=np.flatnonzero(mask)[keep]
        self.br[idx]=(ar[:,None,None]*Kt)[keep]@X[keep]+K[keep]@Xr[keep]
        self.bs[idx]=Ks[keep]@X[keep]+K[keep]@Xs[keep]
        self.base[idx]=K[keep]@X[keep]


class R740Build(physical.Build):
    frame_type=R740Frame
    radius_at=R733Build.radius_at

    def __init__(self,baseline=BASELINE,modes=8192,steps=12,order=48):
        require_public()
        if baseline!=BASELINE or modes<128 or steps<6 or not 32<=order<=96:
            raise ValueError("fixed weak R740 source and compensated physical settings required")
        self.baseline,self.modes,self.steps,self.order=baseline,modes,steps,order
        self.rings={0.:ring.Ring(0.,order)}
        self.pulse_cache={}
        self.ring=self.rings[0.]
        self.profile=R733Profile(physical.Profile(order),order)
        self.integration_ell_breaks=np.unique(np.r_[material_breaks(None),GLOBAL_BREAKS,FILLET_BREAKS,
                  .04+.43*np.array([.002,.004,.5,.996,.998]),.52+.04*np.array([.002,.004,.5,.996,.998]),
                  TOTAL-.035*np.array([.002,.004,.5,.996,.998]),physical.H+.035*np.array([.002,.004,.5,.996,.998])])
        self.identity=dict(source="R740 weak baseline whole closed S-meridian disk",baseline=baseline,
                increment=INCREMENT,basal_curvature=B0,modes=modes,steps=steps,order=order,
                W=physical.W,a=physical.A,round_length=physical.L,core_R=physical.R0,
                core_rad=physical.EPS,core_collar=physical.DU,pulse_h=physical.H,
                section_length=self.ring.length,reverse_start_x=START_X,reverse_leg=LEG,
                reverse_angle=ANGLE,straight_buffer=BUFFER,reverse_length=LENGTH,
                meridian_to_core=TOTAL,fillet_start_ell=FILLET_START,
                true_fillet_x_translation=self.profile.s.fillet_translation,
                transfer_window_ell=[.04,.47])

    def nodes(self,level,purpose):
        r,s=super().nodes(level,purpose)
        sh={"train":.5,"validation":.319,"qualification":.173}[purpose]
        extra=self.integration_ell_breaks
        r=np.r_[r,self.radius_at(material_breaks(sh)),self.radius_at(extra),
                self.radius_at(GLOBAL_BREAKS[:-1]+sh*np.diff(GLOBAL_BREAKS)),
                self.radius_at(FILLET_BREAKS[:-1]+sh*np.diff(FILLET_BREAKS)),
                physical.R0+.13*np.array([.002,.5,.998]),.24+.38*np.array([.002,.5,.998])]
        vs=[.949+.05*np.array([.002,.004,sh,.996,.998])]
        for c,width in ((.205,.102),(.206,.100),(.846,.102),(.847,.100)):
            cut=np.array([.0005,.001,.0015,.9985,.999,.9995])
            vs.append(c+width*np.r_[cut,cut[0]+sh*.001,cut[3]+sh*.001])
        v=np.unique(np.concatenate(vs));v=np.r_[v,-v]
        s=np.r_[s,(v+1)/self.ring.length,(3+self.ring.LU-v)/self.ring.length]
        # The old failing coordinates are material label probes only. This
        # source, its q, its residuals and every derivative are evaluated anew.
        probes={"train":(.6875,.8512161090317758),
                "validation":(.6748773585614992,.8511210367268025),
                "qualification":(.6748773585614992,.8511210367268025)}
        pr,ps=probes[purpose]
        return np.unique(np.r_[r,pr]),np.unique(np.mod(np.r_[s,ps],1.))

    @property
    def seed_identity(self):
        paths=tuple(PINS)+("r688_actual_r664_window_collars.py","r688_true_caps_and_reference_sections.py",
              "r733_inserted_meridian.py","r733_physical_disk.py","r740_weak_material_disk.py",
              "r740_material_rotation_space.py","r740_disk_solver.py")
        return {**self.identity,"physics_sha256":{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in paths}}
