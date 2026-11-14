#!/usr/bin/env python3
"""Complete finite mesh pipeline, with all approximate closing steps labeled.

This preserves the saved quintic prefix, material angle and mean primitive,
reads the integrated-Fr finite tail, and uses the original explicit endpoint
Hermite collar on the unchanged rotational background. A small full Cartesian
cut correction is part of this FINITE map definition and is audited separately.
The infinite nonaxisymmetric tail, exact common-g limit, continuous embedding,
and reach are not certified by this script or by a watertight triangle mesh.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);return json.loads(gzip.decompress(p.read_bytes())if p.suffix=='.gz'else p.read_text())
def write(p,data):Path(p).write_text(json.dumps(data,indent=2)+'\n')
def distinct(values,lo,hi,tol=1e-11):
    out=[float(lo)]
    for v in sorted(float(x)for x in values if lo<x<hi):
        if v-out[-1]>tol and hi-v>tol:out.append(v)
    out.append(float(hi));return np.asarray(out)


def load(args):
    pb=module('geometric_assembly_pullback',HERE/'geometric-checkpoint-core-pullback.py')
    saved,loader=pb.load_saved(args.checkpoint,args.source_topic,args.port,angular=args.height_angular)
    tailmod=module('geometric_assembly_integrated',args.source_topic/'scripts/db6f_tail_integrated.py')
    tail=tailmod.IntegratedTail(args.tail_manifest)
    if not saved.rec['solver_success']or not saved.rec.get('actual_tail'):raise ValueError('A solved actual-tail prefix is required')
    if saved.sol.sol.c.shape[0]!=6:raise ValueError('Saved prefix must already be the reviewed quintic C2 representation')
    if saved.mode!=2 or tail.meta['settings']['spacing']!=2:raise ValueError('This assembly is for the current m2 family')
    if args.angular%8 or args.angular<64:raise ValueError('Material sampling must be divisible by 8 and at least 64')
    if tail.meta['parameters']['orientation']!=1:raise ValueError('Positive-r source orientation required')
    if loader.source_revision(args.source_topic)!='869436630c99aa5a68afb55bd8877c826034d117':raise ValueError('Wrong source revision')
    return saved,tail


def plan(args):
    saved,tail=load(args);end=saved.flow.end;cuff=tail.meta['parameters']['rCuff'];inner=float(tail.r[0]);cut=float(tail.r[-1])
    if not 0<args.cut_correction_width<end:raise ValueError('Cut correction width must be positive and below prefix length')
    if not all(np.isfinite(args.marker_kappas))or not 0<args.marker_kappas[0]or not np.all(np.diff(args.marker_kappas)>0):raise ValueError('Four finite, positive, strictly increasing marker curvatures are required')
    s=distinct(np.r_[np.linspace(0,end,args.prefix_intervals+1),saved.flow.breaks,end-args.cut_correction_width],0,end)
    rawends=np.cumsum([int(f['rows'])-1 for f in tail.meta['files']]);r=distinct(np.r_[np.linspace(inner,cut,args.tail_intervals+1),tail.r[rawends]],inner,cut)
    collar=np.linspace(cuff,inner,args.collar_intervals+1)
    ell=cuff/8;center=cuff/2
    cap=distinct(np.r_[np.linspace(0,cuff,args.cap_intervals+1),ell/2,ell,center-ell,center-ell/2,center,center+ell/2,center+ell],0,cuff)
    upper=[dict(kind='prefix',coordinate=float(x))for x in s];upper[-1]['cut']=True
    upper += [dict(kind='tail',coordinate=float(x))for x in r[-2::-1]]
    upper += [dict(kind='collar',coordinate=float(x))for x in collar[-2::-1]];upper[-1]['cuff']=True
    upper += [dict(kind='cap',coordinate=float(x))for x in cap[-2:0:-1]]
    rings=2*len(upper)-1;vertices=rings*args.angular+2;faces=2*rings*args.angular;bytes_upper=25*vertices+13*faces+4096
    if bytes_upper>=5_000_000:raise ValueError('Mesh plan exceeds the user per-file limit; lower sampling counts')
    rp=Path(str(args.out_prefix)+'-radii.json');radii=sorted(set(map(float,np.r_[r,collar,cut,cuff])))
    write(rp,dict(radii=radii,finite_tail_manifest_sha256=sha(args.tail_manifest)))
    result=dict(status='finite-approximate-closed-mesh-plan',scope=__doc__,source_revision='869436630c99aa5a68afb55bd8877c826034d117',
        checkpoint=dict(file=str(args.checkpoint.resolve()),sha256=sha(args.checkpoint)),tail_manifest=dict(file=str(args.tail_manifest.resolve()),sha256=sha(args.tail_manifest)),
        port=dict(file=str(args.port.resolve()),sha256=sha(args.port)),source_topic=str(args.source_topic.resolve()),script_sha256=sha(__file__),
        upper_rings=upper,angular=args.angular,prefix_end=end,tail_inner=inner,cuff=cuff,cut=cut,cut_correction_width=args.cut_correction_width,
        radius_file=str(rp.resolve()),radius_file_sha256=sha(rp),vertices=vertices,faces=faces,rings=rings,uncompressed_bytes_upper=bytes_upper,
        times=[0.,.5,1.],phase_angles=[0.,math.pi/4,math.pi/2],phase_interval=[0.,math.pi/2],phase_rule='alpha=pi*t/2, t in [0,1]; F_alpha(s,theta)=R_alpha F_0(s,theta-alpha); prefix theta is inverted with SavedPrefix.inverse, never shifted in the numerical eta chart.',
        prefix_representation='Retain existing saved quintic coefficient PPoly (6 coefficients per span); height is its velocity mean primitive. No new prefix interpolation is substituted.',
        fixed_cap=dict(kind='two planar disks with four fixed C3 compactly supported radial bumps',bump_radius=ell,upper_center_radius=center,kappas=args.marker_kappas,
          formula='z=(kappa*ell^2/8)*(1-rho^2/ell^2)^4_+ relative to its plane; outward signs differ on upper/lower cap.',
          marker_theorem='R8 is conditional on all active curvature strictly below the chosen minimum marker curvature and isolated distinct peaks; no curvature or reach certificate is inferred here.'),
        piece_labels={'0':'A: moving prefix, finite tail and nonzero perturbation collar','1':'C: fixed rotational flat caps outside marker supports, including cuff','2':'P: fixed marker graph patches'},
        exact_infinite_tail=False,exact_common_metric_limit=False,continuous_embedding_certificate=False,reach_certificate=False)
    path=Path(str(args.out_prefix)+'-plan.json');write(path,result)
    print(json.dumps(dict(plan=str(path),radii=str(rp),vertices=vertices,faces=faces,bytes_upper=bytes_upper)),flush=True)


def material_jets(saved,s,theta,height):
    s=np.asarray(s);target=np.broadcast_to(theta,(len(s),len(theta)));eta,res,it=saved.inverse(s,target)
    old=saved.jets(s,eta,height);a=saved.angle(s,eta);rho=a['rho'];ep=1/rho;es=-a['theta_s']/rho
    epp=-a['rhop']/rho**3;esp=-(a['rho_s']+a['rhop']*es)/rho**2
    ess=-(a['theta_ss']+2*a['rho_s']*es+a['rhop']*es*es)/rho
    out=dict(pos=old['pos'],p1=old['p1']*ep[:,:,None],p2=old['p2']*ep[:,:,None]**2+old['p1']*epp[:,:,None],
        s1=old['s1']+old['p1']*es[:,:,None],
        s2=old['s2']+2*old['sp']*es[:,:,None]+old['p2']*es[:,:,None]**2+old['p1']*ess[:,:,None],
        sp=(old['sp']+old['p2']*es[:,:,None])*ep[:,:,None]+old['p1']*esp[:,:,None])
    return out,res,it


def synth(tail,c,theta,derivative=0):
    c=np.asarray(c);theta=np.asarray(theta);mp=tail.planar_modes;mh=tail.height_modes
    planar=np.einsum('...k,nk->...n',c[...,:tail.P],(1j*mp)**derivative*np.exp(1j*theta[:,None]*mp))
    if derivative==0:basis=np.cos(theta[:,None]*mh)
    elif derivative==1:basis=-mh*np.sin(theta[:,None]*mh)
    elif derivative==2:basis=-mh*mh*np.cos(theta[:,None]*mh)
    else:raise ValueError('Angular derivative must be 0,1,2')
    z=np.einsum('...k,nk->...n',c[...,tail.P:],basis)
    return np.asarray(np.stack([planar.real,planar.imag,z],axis=-1),float)


def endpoint_safe_coefficients(tail,r):
    # Absolute radius subtraction can put a rounded endpoint a few ulps
    # outside t=0/1 on an extremely thin span. Use its defining coordinate.
    if r==tail.r[0]or float(r)==float(tail.r[0]):return tail.span_coefficients(0,0.)
    if r==tail.r[-1]or float(r)==float(tail.r[-1]):return tail.span_coefficients(len(tail.L)-1,1.)
    return tail.coefficients(r)


def hermite(t,L,derivative=0):
    coeff=np.array([[0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]],float)*np.array([1,L,L*L])[:,None]
    for _ in range(derivative):coeff=coeff[:,1:]*np.arange(1,coeff.shape[1])[None,:]/L
    return np.stack([np.polynomial.polynomial.polyval(t,c)for c in coeff],axis=-1)


class Assembly:
    def __init__(self,saved,tail,plan,heights,height_angular):
        self.saved,self.tail,self.plan=saved,tail,plan;self.height_angular=height_angular
        self.height={float(r['r']):r for r in heights['rows']};self.cuff=plan['cuff'];self.inner=plan['tail_inner'];self.cut=plan['cut'];self.L=plan['prefix_end'];self.W=plan['cut_correction_width']
        self.theta_audit=2*np.pi*np.arange(256)/256
        endheight=saved.height_jets(np.array([self.L]),angular=height_angular)
        old,res,_=material_jets(saved,np.array([self.L]),self.theta_audit,endheight)
        self.prefix_cut_mean=float(np.mean(old['pos'][0,:,2]));v=endpoint_safe_coefficients(tail,tail.r[-1])[0];self.offset=self.prefix_cut_mean+float(v[tail.P])
        self.cap_height=self.offset+self.height[self.cuff]['heightFromRToCut'];self.inner_coeff=endpoint_safe_coefficients(tail,tail.r[0])
        new=self.tail_jets(np.array([self.cut]),self.theta_audit)
        cut=saved.rec['physical_tail_cut'];E=float(cut['E']);Ep=float(cut['Ep']);sigma=float(saved.flow.bridge.sigma)
        rs=sigma/np.sqrt(E);rss=-Ep/(2*E*E)
        target=dict(pos=new['pos'],s1=rs*new['s1'],s2=rs*rs*new['s2']+rss*new['s1'],p1=new['p1'],p2=new['p2'],sp=rs*new['sp'])
        self.cut_errors={k:float(np.max(np.linalg.norm(target[k]-old[k],axis=-1)))for k in old}
        delta=np.stack([target[k][0]-old[k][0]for k in ('pos','s1','s2')]);freq=np.fft.fftfreq(256,1/256).astype(int)
        keep=abs(freq)<=max(abs(tail.planar_modes).max(),tail.height_modes.max(),2*saved.M+1)
        self.correction_frequencies=freq[keep];self.correction_coeff=np.fft.fft(delta,axis=1)[:,keep]/256
        reco=self.correction_angles(self.theta_audit,0)
        self.correction_projection_error=float(np.max(abs(reco-delta)))
        self.chart_cut_inverse_residual=res
        self.cut_radial_jets=dict(rs=float(rs),rss=float(rss),sigma=sigma,E=E,Ep=Ep)

    def correction_angles(self,theta,order):
        k=self.correction_frequencies;basis=np.exp(1j*np.asarray(theta)[:,None]*k)*(1j*k)**order
        return np.einsum('jkc,nk->jnc',self.correction_coeff,basis).real

    def prefix_jets(self,s,theta,height=None):
        s=np.asarray(s);height=self.saved.height_jets(s,self.height_angular)if height is None else height
        j,res,it=material_jets(self.saved,s,theta,height);t=np.clip((s-(self.L-self.W))/self.W,0,1)
        bases=[hermite(t,self.W,d)for d in range(3)];angles=[self.correction_angles(theta,d)for d in range(3)]
        for key,i,k in [('pos',0,0),('s1',1,0),('s2',2,0),('p1',0,1),('sp',1,1),('p2',0,2)]:
            j[key]+=np.einsum('sj,jnc->snc',bases[i],angles[k])
        return j,res,it

    def perturbation(self,r,theta):
        r=np.asarray(r);C=[]
        for value in r:
            if value>=self.inner:
                query=np.longdouble(value)
                if value==self.cut:query=self.tail.r[-1]
                if value==self.inner:query=self.tail.r[0]
                C.append(endpoint_safe_coefficients(self.tail,query))
            else:
                t=(value-self.cuff)/(self.inner-self.cuff);L=self.inner-self.cuff
                C.append(tuple(hermite(t,L,d)@np.stack(self.inner_coeff)for d in range(3)))
        coeff=np.asarray(C)
        return dict(pos=synth(self.tail,coeff[:,0],theta),s1=synth(self.tail,coeff[:,1],theta),s2=synth(self.tail,coeff[:,2],theta),
            p1=synth(self.tail,coeff[:,0],theta,1),p2=synth(self.tail,coeff[:,0],theta,2),sp=synth(self.tail,coeff[:,1],theta,1))

    def tail_jets(self,r,theta):
        r=np.asarray(r);j=self.perturbation(r,theta);co=np.cos(theta)[None,:];si=np.sin(theta)[None,:]
        h=np.array([self.height[float(x)]['heightFromRToCut']for x in r]);w=np.array([self.height[float(x)]['w']for x in r]);wr=np.array([self.height[float(x)]['wr']for x in r])
        for val in j.values():val[:,:,2]*=-1
        j['pos']+=np.stack(np.broadcast_arrays(r[:,None]*co,r[:,None]*si,(self.offset+h)[:,None]),axis=-1)
        j['s1']+=np.stack(np.broadcast_arrays(co,si,-w[:,None]),axis=-1)
        j['s2'][:,:,2]-=wr[:,None]
        j['p1']+=np.stack(np.broadcast_arrays(-r[:,None]*si,r[:,None]*co,np.zeros((len(r),len(theta)))),axis=-1)
        j['p2']+=np.stack(np.broadcast_arrays(-r[:,None]*co,-r[:,None]*si,np.zeros((len(r),len(theta)))),axis=-1)
        j['sp']+=np.stack(np.broadcast_arrays(-si,co,np.zeros((len(r),len(theta)))),axis=-1)
        return j

    def cap(self,r,theta,upper=True):
        r=np.asarray(r);xy=np.stack(np.broadcast_arrays(r[:,None]*np.cos(theta),r[:,None]*np.sin(theta)),axis=-1)
        z=np.full(xy.shape[:-1],self.cap_height);labels=np.ones(z.shape,np.uint8);ell=self.plan['fixed_cap']['bump_radius'];c=self.plan['fixed_cap']['upper_center_radius']
        centers=[(c*np.cos(2*np.pi*j/3),c*np.sin(2*np.pi*j/3))for j in range(3)]if upper else [(0.,0.)]
        kappas=self.plan['fixed_cap']['kappas'][:3]if upper else self.plan['fixed_cap']['kappas'][3:]
        for center,kappa in zip(centers,kappas):
            t=np.sum((xy-np.array(center))**2,axis=-1)/ell**2;inside=t<1;z+=kappa*ell**2/8*np.maximum(0,1-t)**4;labels[inside]=2
        if not upper:z=-z
        return np.dstack([xy,z]),labels

    def cap_normals(self,X,upper=True):
        xy=X[...,:2];gradient=np.zeros_like(xy);ell=self.plan['fixed_cap']['bump_radius'];c=self.plan['fixed_cap']['upper_center_radius']
        centers=[(c*np.cos(2*np.pi*j/3),c*np.sin(2*np.pi*j/3))for j in range(3)]if upper else [(0.,0.)]
        kappas=self.plan['fixed_cap']['kappas'][:3]if upper else self.plan['fixed_cap']['kappas'][3:]
        for center,kappa in zip(centers,kappas):
            delta=xy-np.array(center);t=np.sum(delta*delta,axis=-1)/ell**2
            gradient-=kappa*delta*np.maximum(0,1-t)[...,None]**3
        normal=np.concatenate([-gradient,np.full(xy.shape[:-1]+(1,),1. if upper else -1.)],axis=-1)
        return normal/np.linalg.norm(normal,axis=-1)[...,None]


def metric_curvature(j,E0,G0,inward=False):
    A,B,C,D,E=[j[k]for k in ('s1','p1','s2','sp','p2')];g0=np.sum(A*A,axis=-1);g1=np.sum(A*B,axis=-1);g2=np.sum(B*B,axis=-1);det=g0*g2-g1*g1
    n=np.cross(A,B);n/=np.linalg.norm(n,axis=-1)[:,:,None]
    h0=np.sum(n*C,axis=-1);h1=np.sum(n*D,axis=-1);h2=np.sum(n*E,axis=-1);tr=(h0*g2-2*h1*g1+h2*g0)/det;prod=(h0*h2-h1*h1)/det
    root=np.sqrt(np.maximum(0,tr*tr-4*prod));kap=np.maximum(abs((tr+root)/2),abs((tr-root)/2))
    metric=np.maximum.reduce((abs(g0/E0[:,None]-1),abs(g1)/np.sqrt(E0[:,None]*G0[:,None]),abs(g2/G0[:,None]-1)))
    X=j['pos'];R2=np.sum(X[:,:,:2]**2,axis=-1);bp=(X[:,:,0]*B[:,:,1]-X[:,:,1]*B[:,:,0])/R2
    bu=(X[:,:,0]*A[:,:,1]-X[:,:,1]*A[:,:,0])/R2;J=(bp*A[:,:,2]-bu*B[:,:,2])*(-1 if inward else 1)
    return dict(metric=float(metric.max()),curvature=float(kap.max()),area_ratio_min=float(np.sqrt(det/(E0[:,None]*G0[:,None])).min()),
        cylinder_R_min=float(np.sqrt(R2).min()),cylinder_beta_theta_min=float(bp.min()),cylinder_J_upward_min=float(J.min()),fixed_beta_height_derivative_upward_min=float((J/bp).min()))


def topology(faces,vertices):
    edges=np.sort(np.concatenate([faces[:,[0,1]],faces[:,[1,2]],faces[:,[2,0]]]),axis=1);_,counts=np.unique(edges,axis=0,return_counts=True)
    cross=np.cross(vertices[faces[:,1]]-vertices[faces[:,0]],vertices[faces[:,2]]-vertices[faces[:,0]])
    volume=np.sum(np.einsum('ij,ij->i',vertices[faces[:,0]],cross))/6
    return dict(vertices=len(vertices),edges=len(counts),faces=len(faces),euler=len(vertices)-len(counts)+len(faces),all_edges_have_two_faces=bool(np.all(counts==2)),zero_area_faces=int(np.sum(np.linalg.norm(cross,axis=1)==0)),signed_volume=float(volume))


def ply(path,X,faces,labels):
    header=('ply\nformat binary_little_endian 1.0\ncomment finite approximate assembly; no exact-infinite-tail or reach certificate\n'
      f'element vertex {len(X)}\nproperty double x\nproperty double y\nproperty double z\nproperty uchar piece\n'
      f'element face {len(faces)}\nproperty list uchar int vertex_indices\nend_header\n').encode()
    v=np.empty(len(X),dtype=[('x','<f8'),('y','<f8'),('z','<f8'),('piece','u1')])
    for i,key in enumerate(('x','y','z')):v[key]=X[:,i]
    v['piece']=labels;f=np.empty(len(faces),dtype=[('count','u1'),('indices','<i4',(3,))]);f['count']=3;f['indices']=faces
    raw=header+v.tobytes()+f.tobytes()
    if len(raw)>=5_000_000:raise ValueError('PLY exceeds user file limit')
    zipped=gzip.compress(raw,compresslevel=9,mtime=0);Path(path).write_bytes(zipped)
    old=Path(path).with_suffix('')
    if old.exists():
        if hashlib.sha256(old.read_bytes()).digest()!=hashlib.sha256(raw).digest():raise ValueError('An older uncompressed mesh differs; refusing to remove it')
        old.unlink()
    return dict(file=str(Path(path).resolve()),bytes=len(zipped),uncompressed_bytes=len(raw),sha256=sha(path),uncompressed_sha256=hashlib.sha256(raw).hexdigest())


def render(args):
    started=time.time();saved,tail=load(args);p=read(args.plan);heights=read(args.heights)
    for key,path in [('checkpoint',args.checkpoint),('tail_manifest',args.tail_manifest),('port',args.port)]:
        if p[key]['sha256']!=sha(path):raise ValueError('Plan binding changed: '+key)
    if heights['inputs']['manifest']['sha256']!=sha(args.tail_manifest)or heights['inputs']['radii']['sha256']!=p['radius_file_sha256']:raise ValueError('Background binding changed')
    A=Assembly(saved,tail,p,heights,args.height_angular);theta=2*np.pi*np.arange(p['angular'])/p['angular'];upper=np.empty((len(p['upper_rings']),len(theta),3));lower=upper.copy();upper_normal=upper.copy();lower_normal=upper.copy();labels=np.zeros(upper.shape[:-1],np.uint8);lower_labels=labels.copy();audits={};inverse=0
    for kind in ('prefix','tail','collar','cap'):
        indices=[i for i,row in enumerate(p['upper_rings'])if row['kind']==kind];values=np.array([p['upper_rings'][i]['coordinate']for i in indices])
        if kind=='prefix':
            h=saved.height_jets(values,args.height_angular);j,res,it=A.prefix_jets(values,theta,h);inverse=max(inverse,res);upper[indices]=j['pos'];r=saved.flow.profile(values)[0]
            audits[kind]=metric_curvature(j,np.ones(len(values)),r*r)
            upper_normal[indices]=np.cross(j['p1'],j['s1'])
        elif kind in ('tail','collar'):
            j=A.tail_jets(values,theta);upper[indices]=j['pos'];w=np.array([A.height[float(r)]['w']for r in values]);audits[kind]=metric_curvature(j,1+w*w,values*values,inward=True)
            upper_normal[indices]=np.cross(j['s1'],j['p1'])
        else:
            upper[indices],labels[indices]=A.cap(values,theta,True);lower[indices],lower_labels[indices]=A.cap(values,theta,False)
            upper_normal[indices]=A.cap_normals(upper[indices],True);lower_normal[indices]=A.cap_normals(lower[indices],False)
        if kind!='cap':
            upper_normal[indices]/=np.linalg.norm(upper_normal[indices],axis=2)[:,:,None]
            lower[indices]=upper[indices];lower[indices,:,2]*=-1;lower_normal[indices]=upper_normal[indices];lower_normal[indices,:,2]*=-1
    for i,row in enumerate(p['upper_rings']):
        if row.get('cuff'):
            labels[i]=1;lower_labels[i]=1;upper_normal[i]=[0.,0.,1.];lower_normal[i]=[0.,0.,-1.]
    # Existing inlet symmetry is audited; a shared core ring avoids duplicate topology.
    inlet=np.array([0.]);ih=saved.height_jets(inlet,args.height_angular);ij,_,_=A.prefix_jets(inlet,theta,ih)
    mirror=dict(z_at_core=float(abs(ij['pos'][0,:,2]).max()),horizontal_s_at_core=float(np.linalg.norm(ij['s1'][0,:,:2],axis=1).max()),z_ss_at_core=float(abs(ij['s2'][0,:,2]).max()))
    baseline=np.concatenate([lower[:0:-1],upper]);normal_rings=np.concatenate([lower_normal[:0:-1],upper_normal]);piece=np.concatenate([lower_labels[:0:-1],labels]);R=len(baseline);N=len(theta)
    bottom=A.cap(np.array([0.]),np.array([0.]),False)[0][0,0];top=A.cap(np.array([0.]),np.array([0.]),True)[0][0,0]
    bottom_label=int(A.cap(np.array([0.]),np.array([0.]),False)[1][0,0]);top_label=int(A.cap(np.array([0.]),np.array([0.]),True)[1][0,0])
    faces=[]
    for i in range(R-1):
        for j in range(N):
            a=i*N+j;b=i*N+(j+1)%N;c=(i+1)*N+j;d=(i+1)*N+(j+1)%N;faces.extend(((a,b,c),(b,d,c)))
    for j in range(N):faces.extend(((R*N,(j+1)%N,j),(R*N+1,(R-1)*N+j,(R-1)*N+(j+1)%N)))
    faces=np.asarray(faces,dtype=np.int32);all_labels=np.r_[piece.ravel(),bottom_label,top_label].astype(np.uint8);files=[];clouds=[];fixed=piece>0
    for index,alpha in enumerate(p['phase_angles']):
        shift=int(round(alpha*N/(2*np.pi)));cur=np.roll(baseline,shift,axis=1).copy();co=np.cos(alpha);si=np.sin(alpha);x=cur[:,:,0].copy();y=cur[:,:,1].copy();cur[:,:,0]=co*x-si*y;cur[:,:,1]=si*x+co*y
        # Fixed cap points and the common cuff are copied bit-for-bit.
        cur[fixed]=baseline[fixed];X=np.vstack([cur.reshape(-1,3),bottom,top]);clouds.append(X)
        path=Path(str(args.out_prefix)+f'-phase{index}.ply.gz');files.append({**ply(path,X,faces,all_labels),'alpha':alpha})
    topological=topology(faces,clouds[0]);cloud=clouds[0];tree=cKDTree(cloud);phase=[]
    ball=2*float(np.linalg.norm(cloud,axis=1).max());i=int(np.argmax(np.linalg.norm(cloud,axis=1)));j=int(np.argmax(np.linalg.norm(cloud-cloud[i],axis=1)));k=int(np.argmax(np.linalg.norm(cloud-cloud[j],axis=1)));diameter_lower=float(np.linalg.norm(cloud[j]-cloud[k]))
    for alpha,X in zip(p['phase_angles'][1:],clouds[1:]):
        d=tree.query(X,workers=1)[0];back=cKDTree(X).query(cloud,workers=1)[0];H=float(max(d.max(),back.max()));phase.append(dict(alpha=alpha,vertex_cloud_hausdorff=H,ratio_using_vertex_ball_diameter_upper=H/ball,fixed_vertices_bitwise_equal=bool(np.array_equal(X[all_labels>0],cloud[all_labels>0]))))
    # A modest spatial subset in the direct R11 interface. Analytic phase
    # elimination is exact; selecting this finite spatial subset is not.
    normals=np.vstack([normal_rings.reshape(-1,3),[0.,0.,-1.],[0.,0.,1.]])
    rings=np.unique(np.r_[np.arange(0,R,2),np.flatnonzero(np.any(piece>0,axis=1))]);angles=np.arange(0,N,2)
    selected=np.r_[(rings[:,None]*N+angles).ravel(),R*N,R*N+1];moving=selected[all_labels[selected]==0];fixed_indices=selected[all_labels[selected]>0]
    normals_path=Path(str(args.out_prefix)+'-normal-samples.npz')
    np.savez_compressed(normals_path,moving_xyz=cloud[moving],moving_normal=normals[moving],fixed_xyz=cloud[fixed_indices],fixed_normal=normals[fixed_indices],
        moving_source_indices=moving,fixed_source_indices=fixed_indices,fixed_piece_labels=all_labels[fixed_indices],tau=np.array(.03*ball),diameter_vertex_ball_upper=np.array(ball))
    if normals_path.stat().st_size>1_000_000:raise ValueError('Normal sample packet exceeds 1 MB; reduce the spatial subset')
    phase_reach=module('geometric_assembly_phase_reach',HERE/'root_phase_reach.py')
    cross=phase_reach.screen(cloud[moving],normals[moving],cloud[fixed_indices],normals[fixed_indices],.03*ball,batch=64)
    cross.update(input=str(normals_path.resolve()),input_sha256=sha(normals_path),helper_sha256=sha(HERE/'root_phase_reach.py'),sample_phase_interval='all real phases (stronger than the mesh alpha interval)',
        tau_basis='0.03 times the vertex-cloud ball-diameter upper, not a continuous diameter certificate',fixed_piece_counts={str(i):int(np.sum(all_labels[fixed_indices]==i))for i in (1,2)})
    if cross['worst']:
        row=cross['worst'];ii=moving[row['moving_index']];jj=fixed_indices[row['fixed_index']]
        row.update(moving_point=cloud[ii].tolist(),moving_normal=normals[ii].tolist(),fixed_point=cloud[jj].tolist(),fixed_normal=normals[jj].tolist(),fixed_piece=int(all_labels[jj]),source_vertex_indices=[int(ii),int(jj)])
    cross_path=Path(str(args.out_prefix)+'-all-phase-cross-pairs.json');write(cross_path,cross)
    # Finite prefix PPoly endpoint residuals are measured, not misidentified as cubic.
    pp=saved.sol.sol;steps=np.diff(pp.x);jets=[]
    for order in range(3):
        coeff=pp.c.copy()
        for _ in range(order):coeff=coeff[:-1]*np.arange(coeff.shape[0]-1,0,-1)[:,None,None]
        left=np.zeros_like(coeff[0,:-1])
        for c in coeff[:,:-1]:left=left*steps[:-1,None]+c
        right=coeff[-1,1:];jets.append(float(np.max(abs(left-right))))
    cutheight=saved.height_jets(np.array([A.L]),args.height_angular);cj,_,_=A.prefix_jets(np.array([A.L]),A.theta_audit,cutheight);tj=A.tail_jets(np.array([A.cut]),A.theta_audit);rs=A.cut_radial_jets['rs'];rss=A.cut_radial_jets['rss']
    targets=dict(pos=tj['pos'],s1=rs*tj['s1'],s2=rs*rs*tj['s2']+rss*tj['s1'],p1=tj['p1'],p2=tj['p2'],sp=rs*tj['sp'])
    after={key:float(np.max(np.linalg.norm(cj[key]-targets[key],axis=-1)))for key in targets}
    # Exact-jet collar endpoint identities of the explicit polynomial definition.
    collar0=A.perturbation(np.array([A.cuff]),A.theta_audit);collar_bounds={key:float(np.max(np.linalg.norm(value,axis=-1)))for key,value in collar0.items()}
    n=p['fixed_cap'];ell=n['bump_radius'];cr=n['upper_center_radius'];centers=[]
    for v,kappa in enumerate(n['kappas']):
        if v<3:xy=[cr*np.cos(2*np.pi*v/3),cr*np.sin(2*np.pi*v/3)];z=A.cap_height+kappa*ell**2/8
        else:xy=[0.,0.];z=-A.cap_height-kappa*ell**2/8
        centers.append(xy+[z])
    affine=float(np.linalg.det(np.array(centers)[1:]-np.array(centers)[0]))
    report=dict(status='complete-finite-approximate-closed-family-mesh',scope=__doc__,finished=True,
        inputs=dict(plan=dict(file=str(args.plan.resolve()),sha256=sha(args.plan)),heights=dict(file=str(args.heights.resolve()),sha256=sha(args.heights))),
        script_sha256=sha(__file__),source_revision=p['source_revision'],files=files,topology=topological,piece_labels=p['piece_labels'],
        prefix_ppoly_degree=pp.c.shape[0]-1,prefix_ppoly_join_residuals_orders_012=jets,
        mean_height_gauge=dict(prefix_cut_mean=A.prefix_cut_mean,tail_cut_mean=float(endpoint_safe_coefficients(tail,tail.r[-1])[0][tail.P]),upper_constant_offset=A.offset,upper_cap_height=A.cap_height,reflected_entire_tail_height=True),
        material_inverse_max_residual=inverse,cut_material_inverse_residual=A.chart_cut_inverse_residual,mirror_inlet_samples=mirror,
        cut_before_correction=A.cut_errors,cut_after_correction=after,cut_radial_jets=A.cut_radial_jets,
        cut_correction=dict(width=A.W,definition='Full Cartesian endpoint quintic in physical s, zero 2-jet at L-W and prescribed difference 2-jet at L; included in this finite approximation only.',frequencies=A.correction_frequencies.tolist(),coefficients_real=A.correction_coeff.real.tolist(),coefficients_imag=A.correction_coeff.imag.tolist(),angular_projection_error=A.correction_projection_error),
        collar=dict(interval=[A.cuff,A.inner],definition='Original endpoint Hermite collar: V=Vr=Vrr=0 at cuff, matching full integrated-tail 2-jet at inner port, on the unchanged infinite rotational background.',cuff_jet_norms=collar_bounds,
          inner_endpoint_coefficient_l1=[float(np.sum(abs(c)))for c in A.inner_coeff],metric_defect_is_not_zero=True),
        fixed_markers=dict(centers=centers,kappas=n['kappas'],affine_determinant=affine,conditional_R8_remaining='A continuous upper bound on all other curvature strictly below min kappa and the remaining R8 hypotheses; mesh samples alone do not establish them.'),
        fixed_hold=dict(definition='The union of the two entire fixed caps; disconnected H is expressly allowed in the source README.',selected_pole_distance=float(np.linalg.norm(top-bottom)),ratio_using_vertex_ball_diameter_upper=float(np.linalg.norm(top-bottom))/ball),
        sampled_piece_jets=audits,integrated_tail_export_diagnostics=tail.meta['totals'],phase_vertex_cloud_samples=phase,
        normal_samples=dict(file=str(normals_path.resolve()),sha256=sha(normals_path),bytes=normals_path.stat().st_size,moving_count=len(moving),fixed_count=len(fixed_indices)),
        all_phase_cross_pair_samples=dict(file=str(cross_path.resolve()),sha256=sha(cross_path),pair_count=cross['pair_count'],negative_sample_pairs=cross['negative_sample_pairs'],worst=cross['worst']),
        vertex_cloud_diameter_lower=diameter_lower,vertex_cloud_ball_diameter_upper=ball,
        exact_infinite_nonlinear_tail=False,exact_common_g_isometry=False,continuous_embedding_certificate=False,all_phase_reach_certificate=False,
        unpaid=['Finite prefix source/discretization error and stored polynomial arithmetic','Finite tail spectral/RK/far boundary error','Actual derivative reconstruction and stage correction error','Nonzero common-cut and Hermite collar metric defect','Same fixed-g convergence to a C2 infinite nonaxisymmetric tail','Continuous cross-piece embedding and all spatial normal-chord pairs','Amplitude and diameter/reach bounds for a closed all-time family'],seconds=time.time()-started)
    path=Path(str(args.out_prefix)+'-assembly.json');write(path,report)
    print(json.dumps(dict(report=str(path),files=[f['file']for f in files],topology=topological,cut_before=A.cut_errors,cut_after=after,metric_curvature_samples=audits,cap_height=A.cap_height,phase=phase,seconds=report['seconds'])),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['plan','render'])
    for key in ('source-topic','checkpoint','port','tail-manifest','out-prefix'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--plan',type=Path);p.add_argument('--heights',type=Path);p.add_argument('--angular',type=int,default=96);p.add_argument('--height-angular',type=int,default=256)
    p.add_argument('--marker-kappas',type=float,nargs=4,default=[8.2,8.25,8.3,8.35],metavar=('K1','K2','K3','K4'),help='Candidate-specific fixed marker curvatures; requires a separate continuous active-curvature bound and reach audit')
    for key,value in [('prefix-intervals',112),('tail-intervals',112),('collar-intervals',8),('cap-intervals',16)]:p.add_argument('--'+key,type=int,default=value)
    p.add_argument('--cut-correction-width',type=float,default=.1);a=p.parse_args();a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if a.action=='plan':plan(a)
    else:
        if not a.plan or not a.heights:p.error('render requires --plan and --heights')
        render(a)


if __name__=='__main__':main()
