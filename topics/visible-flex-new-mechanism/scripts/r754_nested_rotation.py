"""Nested R746 rotation field with two physical release regions and one exact local meridian correction."""
import hashlib
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import r746_physical_core_seed as old
import r750_rigid_annulus as release
import r754_broad_seed as broad

weak,space=old.weak,old.space
HERE=Path(__file__).resolve().parent
NEW_FILES=('r750_rigid_annulus.py','r754_broad_seed.py','r754_nested_rotation.py','r754_parent_archive.py',
           'r754_ranged_zip.py','r754_augmented_operator.py','r754_tsqr_reuse.py','r754_nested_disk_solver.py')


def tags(degree):
    return space.tagged_terms(degree)+release.extra_tags(degree)+[('broad_and_local',)]


def padded(q,old_degree,new_degree):
    coeff=dict(zip(tags(old_degree),np.asarray(q).reshape(-1,3),strict=True))
    return np.asarray([coeff.get(k,np.zeros(3)) for k in tags(new_degree)]).ravel()


def split(q,degree):
    q=np.asarray(q)
    n=3*len(space.tagged_terms(degree))
    if q.ndim!=1 or q.size!=3*len(tags(degree)):
        raise ValueError('wrong R754 native control identity')
    return q[:n],q[n:-3],q[-3:]


def set_new_fields(frame,build,phase):
    ell,er,_=space.ell_data(frame.r)
    possible=np.zeros(len(ell),dtype=bool)
    for knots in release.RELEASE_KNOTS:possible|=(ell>knots[0])&(ell<knots[-1])
    candidate=np.flatnonzero(possible)
    cols=len(release.extra_tags(frame.degree))
    if len(candidate):
        empty=np.empty((len(candidate),0))
        temp=SimpleNamespace(r=frame.r[candidate],s=frame.s[candidate],degree=frame.degree,B=empty,Br=empty,Bs=empty)
        release.add_releases(temp,build,ell[candidate],er[candidate])
        keep=np.any((temp.B!=0)|(temp.Br!=0)|(temp.Bs!=0),axis=1)
        frame.plus_nodes=candidate[keep]
        frame.plus,frame.plus_r,frame.plus_s=(b[keep] for b in (temp.B,temp.Br,temp.Bs))
    else:
        frame.plus_nodes=candidate
        frame.plus,frame.plus_r,frame.plus_s=(np.empty((0,cols)) for _ in range(3))
    frame.ncols=3*len(tags(frame.degree));frame.q0=np.zeros(frame.ncols)
    frame.region=np.zeros(len(ell),dtype=bool);frame.region[frame.plus_nodes]=True
    frame.active=np.flatnonzero((ell>old.early.EARLY)&(ell<.060))
    ix=frame.active
    ss=frame.s[ix]
    ring=build.target(phase)
    _,kind,v=ring.label(ss)
    main=(kind==0)|(kind==2)
    vs=np.where(kind==0,ring.length,np.where(kind==2,-ring.length,0.))
    w,wp,_=weak.physical.native_w(v)
    w=np.where(main,w,0.);ws=wp*vs
    av=(abs(v)-.949)/.05
    az=weak.pulse.gate(1-av)*main
    az_s=-weak.pulse.gate(1-av,1)*np.sign(v)*vs/.05
    rho0=weak.B0/(weak.B0+phase*weak.INCREMENT/.0998)
    rho=1-(1-rho0)*az;rho_s=-(1-rho0)*az_s
    el=ell[ix];th,kmer,_=build.profile.s.angle_jet(el-old.early.EARLY)
    st,ct=np.sin(th),np.cos(th)
    cp=np.sqrt(1-(rho*st)**2)
    om=np.arcsin(rho*st)-th
    omr=(rho*ct/cp-1)*kmer*er[ix]
    oms=rho_s*st/cp
    g,gd=release.flat_step((.060-el)/.009)
    gr=-gd*er[ix]/.009
    frame.carrier=g*(1-w)*om
    frame.carrier_r=(1-w)*(gr*om+g*omr)
    frame.carrier_s=g*((1-w)*oms-ws*om)
    e,es=np.zeros((len(ix),3,3)),np.zeros((len(ix),3,3))
    if len(ix):
        _,t,n,k,_=ring.jets(ss)
        e[:,0,0]=1.;e[:,1:,1],e[:,1:,2]=t,n
        es[:,1:,1]=(k*ring.length)[:,None]*n
        es[:,1:,2]=-(k*ring.length)[:,None]*t
    live=(frame.carrier!=0)|(frame.carrier_r!=0)|(frame.carrier_s!=0)
    frame.active=ix[live]
    frame.region[frame.active]=True
    frame.carrier,frame.carrier_r,frame.carrier_s=(a[live] for a in (frame.carrier,frame.carrier_r,frame.carrier_s))
    frame.triad,frame.triad_s=e[live],es[live]
    broad.install(frame,build,phase,ell,er)


class R754Frame(old.R746Frame):
    def __init__(self,build,phase,r,s,degree):
        super().__init__(build,phase,r,s,degree)
        set_new_fields(self,build,phase)

    @classmethod
    def extend(cls,previous,build,phase):
        if type(previous) is not old.R746Frame:
            raise TypeError('expected the paid R746 native frame')
        result=cls.__new__(cls);vars(result).update(vars(previous))
        set_new_fields(result,build,phase)
        return result

    def baseline(self,coeff):
        if not np.any(coeff):return self.base,self.br,self.bs
        dtype=np.result_type(coeff,self.base)
        base,br,bs=(a.astype(dtype,copy=True) for a in (self.base,self.br,self.bs))
        if coeff[1]!=0 and len(self.active):
            ix=self.active;e,es=self.triad,self.triad_s
            et,est=weak.fields.trans(e),weak.fields.trans(es)
            v=np.broadcast_to(np.eye(3,dtype=dtype),(len(ix),3,3)).copy()
            vr=np.zeros_like(v);vs=vr.copy()
            for j in (1,):
                m,ma=weak.fields.rotation(self.carrier*coeff[j],j);dm=v@ma
                vr=vr@m+(self.carrier_r*coeff[j])[:,None,None]*dm
                vs=vs@m+(self.carrier_s*coeff[j])[:,None,None]*dm;v=v@m
            dv=v-np.eye(3)
            l=np.eye(3)+e@dv@et;lr=e@vr@et;ls=es@dv@et+e@vs@et+e@dv@est
            base[ix],br[ix],bs[ix]=l@self.base[ix],lr@self.base[ix]+l@self.br[ix],ls@self.base[ix]+l@self.bs[ix]
        ix=self.wide_nodes
        for amount,wide in ((coeff[0],self.wide_new),(coeff[2],self.wide_ax)):
            if amount!=0 and len(ix):
                d,dr,ds=broad.correction(self.wide_old,wide,amount)
                sb=base[ix];base[ix],br[ix],bs[ix]=d@sb,dr@sb+d@br[ix],ds@sb+d@bs[ix]
        return base,br,bs

    def carrier_rows(self,carrier):
        if any(c!=0 and c!=1 for c in (carrier[0],carrier[2])):
            return np.union1d(self.active,self.wide_nodes)
        return self.active

    def support(self,carrier):
        if carrier[0]==0 and carrier[2]==0:return self.region
        out=self.region.copy();out[self.wide_nodes]=True;return out

    def changed_mask(self,extra,carrier):
        out=np.zeros(len(self.r),dtype=bool)
        if np.any(extra):
            q=extra.reshape(-1,3)
            local=np.zeros(len(self.plus_nodes),dtype=bool)
            for b in (self.plus,self.plus_r,self.plus_s):local|=np.any((b@q)!=0,axis=1)
            out[self.plus_nodes]=local
        if carrier[1]!=0:out[self.active]=True
        if carrier[0]!=0 or carrier[2]!=0:out[self.wide_nodes]=True
        return out

    def arguments(self,q):
        primary,additional,carrier=split(q,self.degree)
        a=[b@primary.reshape(-1,3) for b in (self.B,self.Br,self.Bs)]
        if np.any(additional):
            for val,b in zip(a,(self.plus,self.plus_r,self.plus_s),strict=True):
                val[self.plus_nodes]+=b@additional.reshape(-1,3)
        return a,self.baseline(carrier)

    def read(self,q,output=False):
        p,extra,carrier=split(q,self.degree)
        if not np.any(extra) and not np.any(carrier):
            return super().read(p,output)
        (a,ar,az),(m,mr,ms)=self.arguments(q)
        for j in range(3):
            v,va=weak.fields.rotation(a[:,j],j);d=m@va
            mr=mr@v+ar[:,j,None,None]*d;ms=ms@v+az[:,j,None,None]*d;m=m@v
        _,xr,xs,xrr,xrs,xss=self.j0
        apply=weak.fields.apply
        curl=apply(mr,xs)-apply(ms,xr)
        if not output:
            return (curl/self.det[:,None]).reshape(self.shape+(3,))
        result=(curl,apply(m,xr),apply(m,xs),apply(ms,xr)+apply(m,xrs),
                apply(mr,xr)+apply(m,xrr),apply(ms,xs)+apply(m,xss))
        return tuple(v.reshape(self.shape+(3,)) for v in result)

    def subset(self,selected):
        selected=np.flatnonzero(selected) if np.asarray(selected).dtype==bool else np.asarray(selected,dtype=int)
        out=type(self).__new__(type(self));vars(out).update(vars(self))
        vars(out).pop('new_probe',None)
        listed=('r','s','base','br','bs','B','Br','Bs','det','region','phi','phip')
        for name in listed:
            val=getattr(self,name);setattr(out,name,val[selected])
        out.j0=tuple(z[selected] for z in self.j0);out.shape=(len(selected),)
        for index_name,arrays in (('active',('carrier','carrier_r','carrier_s','triad','triad_s')),
                                  ('plus_nodes',('plus','plus_r','plus_s'))):
            source=getattr(self,index_name)
            idx=np.searchsorted(source,selected)
            hit=np.zeros(len(selected),dtype=bool);valid=idx<len(source)
            hit[valid]=source[idx[valid]]==selected[valid]
            setattr(out,index_name,np.flatnonzero(hit))
            for name in arrays:setattr(out,name,getattr(self,name)[idx[hit]])
        idx=np.searchsorted(self.wide_nodes,selected);good=idx<len(self.wide_nodes)
        hit=np.zeros(len(selected),dtype=bool);hit[good]=self.wide_nodes[idx[good]]==selected[good]
        out.wide_nodes=np.flatnonzero(hit);out.wide_old=self.wide_old[:,idx[hit]];out.wide_new=self.wide_new[:,idx[hit]];out.wide_ax=self.wide_ax[:,idx[hit]]
        return out


class R754Build(old.R746Build):
    frame_type=R754Frame
    @classmethod
    def extend(cls,previous):
        if type(previous) is not old.R746Build:
            raise TypeError('expected the paid R746 source and geometry cache')
        out=cls.__new__(cls);vars(out).update(vars(previous));out.identity=dict(previous.identity)
        out.identity.update(release='R754 nested early-S correction and true collar controls',parent='R746',
             new_rotation_tags='old native prefix, compact release Euler coefficients, two global alternatives and one compact left meridian angle')
        out.integration_ell_breaks=np.unique(np.r_[previous.integration_ell_breaks,*release.RELEASE_KNOTS,
           weak.physical.H+2e-8,old.early.FORCED_END+.00008,release.RELEASE_KNOTS[0][-1]-.008,
           release.RELEASE_KNOTS[1][-1]-.008,.051,.060,.065,weak.FILLET_START,
           *(.065+(.765-.065)*np.array([0.,.002,.004,.5,.996,.998,1.]))])
        return out

    @property
    def seed_identity(self):
        out=super().seed_identity
        for name in NEW_FILES:
            out['physics_sha256'][name]=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        return out


def probes(build,phase,degree,purpose):
    # Separate new paired or tensor labels. Preserve every old train/validation
    # row and its exact ordering, including the original angular origin.
    f={'train':.5,'validation':.317,'qualification':.183}[purpose]
    ell=np.r_[2.5e-8,.00005,.00007*f,old.early.FORCED_END+np.array([.00004,.000071,.00008*f]),.051,.057]
    ell=np.unique(np.r_[ell,.065+(.765-.065)*np.array([.002,.004,.5,.996,.998,f]),
                      .065+(weak.FILLET_START-.065)*np.array([.125,.5,.875,f]),weak.FILLET_START,.765])
    v=np.r_[.2061,.206+.00005+.0001*f,.84625,.84618+.00015*f,.3061,.8471]
    v=np.r_[v,-v];ring=build.ring
    ss=np.r_[(1+v)/ring.length,(3+ring.LU-v)/ring.length]
    return R754Frame(build,phase,build.radius_at(ell)[:,None],ss[None,:],degree)


def exact_local_check(build,phase):
    ell=np.array([.00005,.05014]);v=np.array([.2061,.84625]);ss=(1+v)/build.ring.length
    r=build.radius_at(ell);f=R754Frame(build,phase,r,ss,3)
    q=f.q0.copy();a=f.curl(q);q[-2]=-1.;b=f.curl(q)
    er=space.ell_data(r)[1]
    scale=f.det/(er*build.ring.length)
    before=a*scale[:,None];after=b*scale[:,None]
    gamma,t,n,k,_=build.target(phase).jets(ss)
    theta=build.profile.s.angle_jet((ell-old.early.EARLY).clip(0.))[0]
    rho=weak.B0/(weak.B0+phase*weak.INCREMENT/.0998)
    want=np.r_[0.,(1-rho)*k[1]*np.sin(theta[1])*t[1]]
    defect=float(np.linalg.norm(before[1]-want))
    if not np.array_equal(f.plus_nodes,np.arange(2)):
        raise ArithmeticError('a true R752 probe lacks native release support')
    positive=np.max(abs(f.plus),axis=1)
    if (not np.isfinite(np.r_[before.ravel(),after.ravel(),positive]).all() or np.min(positive)<=0
            or defect>1.e-10 or np.linalg.norm(after[1])>1.e-10):
        raise ArithmeticError('R754 actual new support or original/compensated R752 coframes disagreed')
    return dict(phase=phase,ell=ell,v=v,s=ss,old_dimensional_curl=before,
                compensated_dimensional_curl=after,original_analytic=want,
                dimensional_discrepancy=defect,new_euler_support_max=positive,
                left_control=q[-3:],all_independent_rows_remain_in_fit=True)
