"""Joint source-design and proper rotation field, both boundary circles, and physical witnesses."""
import numpy as np
from scipy.interpolate import BSpline
from scipy.spatial import ConvexHull, distance

from r688_closed_shell_observer import SUPPORT, normal_and_curvature, normal_chords
from r688_two_port_material_atlas import rotation


def mv(A,x):
    return np.einsum('...ij,...j->...i',A,x)


def basis(atlas,spans,modes):
    knots=np.r_[np.zeros(3),np.linspace(0,1,spans+1),np.ones(3)]
    u=np.clip((atlas.t-atlas.ref.meridian_end)/atlas.L,0.,1.)
    rr=BSpline.design_matrix(u,knots,3).toarray()
    a=atlas.theta
    aa=np.column_stack([np.ones_like(a),*[f(k*a) for k in range(1,modes+1) for f in (np.cos,np.sin)]])
    return (atlas.free[...,None,None]*rr[:,None,:,None]*aa[None,:,None,:]).reshape(*atlas.T.shape,-1)


def whiten_metric(G,S):
    # Gram coefficients in the Cholesky orthonormalized source chart.
    g,f,h=np.moveaxis(S,-1,0)
    a,b,c=np.moveaxis(G-S,-1,0)
    g=np.maximum(g,1e-24); schur=np.maximum(h-f*f/g,1e-24); q=f/g
    d=a/g; e=(b-q*a)/np.sqrt(g*schur); k=(c-2*q*b+q*q*a)/schur
    return np.stack((d,e,k),axis=-1)


def basis_field(B,coeff):
    return (B.reshape(-1,B.shape[-1])@coeff).reshape(*B.shape[:2],3)


def extrema(metric):
    a,b,d=np.moveaxis(metric,-1,0)
    return np.abs((a+d)/2)+np.hypot((a-d)/2,b)


class JointField:
    def __init__(self,atlas,phases,bodies,spans,modes):
        self.atlas,self.phases,self.bodies=atlas,phases,bodies
        self.B=basis(atlas,spans,modes)
        self.shape=(len(phases),self.B.shape[-1],3)
        self.width=np.sqrt(atlas.quad)
        self.base={f:atlas.geometry[f][0] for f in phases}
        self.D={f:(atlas.dt(self.base[f]),atlas.da(self.base[f])) for f in phases}
        self.curv_body=max([9.53,1/.12,bodies['shoulder_k'],*bodies['collar_k']])
        self.known_domain_min=bodies['shoulder_sine']
        for row in bodies['actual_by_phase'].values():
            self.known_domain_min=min(self.known_domain_min,*[z['min_param_sine_squared'] for z in row['strips']])

    def state(self,q,full,active=None):
        A=self.atlas
        q=np.asarray(q).reshape(self.shape)
        X=self.base[0.]+basis_field(self.B,q[0])
        a,b=A.dt(X),A.da(X)
        _,_,_,S=normal_and_curvature(a,b,A.dt(X,2),A.da(a),A.da(X,2))
        rr=[]; poses=[]; metrics=[]
        for i,phase in enumerate(self.phases):
            Y=self.base[phase]; da0,ds0=self.D[phase]
            if i==0:
                ft,fs=a,b
            else:
                R=A.geometry[phase][1]@rotation(basis_field(self.B,q[i]))
                ft,fs=mv(R,a),mv(R,b)
            dt,ds=ft-da0,fs-ds0
            raw_port=[dt[A.paid],ds[A.paid]]
            # True differential of the known C2 lifting on each paid open band.
            # Retain its uncorrected finite-stencil mismatch as two independent rows.
            dt=np.where(A.paid[...,None],0.,dt); ds=np.where(A.paid[...,None],0.,ds)
            # Integrate from the given crown. Subtraction of a known lifting
            # retains its exact discrete derivatives and removes a large quadrature bias.
            c=A.dt(ds)-A.da(dt)
            integ=A.integrate(dt)
            mismatch=integ[-1]
            back=np.zeros_like(dt)
            increments=(dt[1:]+dt[:-1])*(np.diff(A.t)[:,None,None]/2)
            back[:-1]=np.cumsum(increments[::-1],axis=0)[::-1]
            P=Y+(1-A.tie[...,None])*integ-A.tie[...,None]*back
            if i==0:
                # Source position is the design variable itself; its exact differential
                # has identity rotation for every possible source coefficient.
                P=X; c=np.zeros_like(c); mismatch=np.zeros_like(mismatch)
            period=np.einsum('a,taj->tj',A.angular_weights,fs)
            # For the exact periodic lifting the cycle is zero. Integrate its
            # difference and separately print raw beta quadrature, including roundoff.
            diffperiod=np.einsum('a,taj->tj',A.angular_weights,ds)
            if i==0:
                diffperiod=np.zeros_like(diffperiod)
            pa,pb=A.dt(P),A.da(P)
            N,k,sine,G=normal_and_curvature(pa,pb,A.dt(P,2),A.da(pa),A.da(P,2))
            metric=whiten_metric(G,S)
            nn=A.paid
            jdiff=[P-Y,pa-da0,pb-ds0,A.dt(P-Y,2),A.da(A.dt(P-Y)),A.da(P-Y,2)]
            jet=[float(np.max(np.linalg.norm(x[nn],axis=-1))) for x in jdiff]
            measure=self.width[...,None]
            if i:
                rr.extend((c*measure,mismatch*np.sqrt(A.angular_weights[:,None]/(2*np.pi)),
                           diffperiod*np.sqrt(A.I[-1,:,None]/A.end),metric*measure,
                           raw_port[0]*.12/np.sqrt(nn.sum()),raw_port[1]*.12/np.sqrt(nn.sum())))
                for x in jdiff:
                    rr.append(x[nn]*.06/np.sqrt(nn.sum()))
            # The real crown/primary endpoint chord at every angular label
            # cannot exceed the common source radial material path length.
            length=A.I[-1]@np.linalg.norm(a,axis=-1)
            chord=np.linalg.norm(Y[-1]-Y[0],axis=-1)
            excess=chord-np.sqrt(1+1e-6)*length
            if i:
                rr.append(np.maximum(0,excess)*np.sqrt(A.angular_weights/(2*np.pi)))
            poses.append((P,N,k,sine))
            metrics.append(dict(phase=phase,max_vector_curl=float(np.max(np.linalg.norm(c,axis=-1))),
                 max_two_port_error=float(np.max(np.linalg.norm(mismatch,axis=-1))),
                 max_raw_period=float(np.max(np.linalg.norm(period,axis=-1))),
                 max_lifting_corrected_period=float(np.max(np.linalg.norm(diffperiod,axis=-1))),
                 min_window_cross=float(np.min(np.linalg.norm(np.cross(pa,pb),axis=-1))),
                 max_relative_gram=float(extrema(metric).max()),six_paid_position_jet_defects=jet,
                 uncorrected_paid_differential_maxima=[float(np.max(np.linalg.norm(x,axis=-1))) for x in raw_port],
                 largest_sampled_chord_minus_source_path=float(np.max(excess))))
        clouds=[]
        for i,(P,N,k,sine) in enumerate(poses):
            bp,bn=self.bodies[self.phases[i]]
            mirror=np.array([-1.,1.,1.])
            clouds.append((np.vstack((bp,P.reshape(-1,3),P.reshape(-1,3)*mirror)),
                           np.vstack((bn,N.reshape(-1,3),N.reshape(-1,3)*mirror))))
        bp=self.bodies[0.][0]
        label=np.vstack((bp,self.base[0.].reshape(-1,3),self.base[0.].reshape(-1,3)*np.array([-1.,1.,1.])))
        if full:
            active=[]
            hulls=[ConvexHull(pts).vertices for pts,_ in clouds]
            all_extreme=np.vstack([clouds[i][0][idx] for i,idx in enumerate(hulls)])
            addresses=[(i,int(j)) for i,ii in enumerate(hulls) for j in ii]
            unionidx=ConvexHull(all_extreme).vertices
            ep=all_extreme[unionidx]
            far=(-1.,0,0)
            for j in range(0,len(ep),128):
                dd=distance.cdist(ep[j:j+128],ep)
                u,v=np.unravel_index(np.argmax(dd),dd.shape)
                if dd[u,v]>far[0]:
                    far=(float(dd[u,v]),int(unionidx[j+u]),int(unionidx[v]))
            diam=far[0]
            witness=[addresses[far[1]],addresses[far[2]]]
            for i,(pts,normals) in enumerate(clouds):
                result=normal_chords(pts,normals,.03*diam,clouds[0][0],label)
                P,N,k,sine=poses[i]
                sup=pts@SUPPORT
                obs=dict(support=float(np.max(sup)),support_material_index=int(np.argmax(sup)),
                    max_abs_window_principal=float(k.max()),
                    max_abs_principal_including_known=max(self.curv_body,float(k.max())),
                    min_window_sine_squared=float(sine.min()),min_right_x=float(P[...,0].min()),
                    highest_z=float(pts[:,2].max()),physical_points=len(pts),**result)
                idx=hulls[i]
                far=(-1.,0,0)
                for j in range(0,len(idx),128):
                    ds=distance.cdist(pts[idx[j:j+128]],pts[idx])
                    u,v=np.unravel_index(np.argmax(ds),ds.shape)
                    if ds[u,v]>far[0]:
                        far=(ds[u,v],int(idx[j+u]),int(idx[v]))
                obs['diameter']=float(far[0])
                active.append(dict(union_diameter=witness,support=obs['support_material_index'],
                     chord=result['attaining_pair'],intrinsic=result['projected_chord_pair'],peak=int(np.argmax(poses[i][2]))))
                metrics[i].update(obs)
        else:
            if active is None:
                raise ValueError("Physical witness list must be paid on this exact collocation")
        (ai,aj),(bi,bj)=active[0]['union_diameter']
        diam=float(np.linalg.norm(clouds[ai][0][aj]-clouds[bi][0][bj]))
        supports=[float(pts[w['support']]@SUPPORT) for (pts,_),w in zip(clouds,active)]
        delta=supports[-1]-supports[0]
        physical=[max(0.,.30*diam-delta),max(0.,.20*diam-.80),
                  max(0.,.03*diam*self.curv_body-1),max(0.,1e-8-self.known_domain_min)]
        for (P,N,k,sine),(pts,normals),w in zip(poses,clouds,active):
            physical.extend((np.maximum(0.,.03*diam*k-1)*self.width).ravel())
            physical.extend((np.maximum(0.,1e-6-sine)*self.width).ravel())
            physical.extend((np.maximum(0.,.001-P[...,0])*self.width).ravel())
            physical.append(max(0.,.03*diam*k.ravel()[w['peak']]-1))
            val=0.
            if w['chord'] is not None:
                i,j=w['chord']; d=pts[i]-pts[j]; dd=d@d
                if dd>1e-24:
                    val=max(0.,2*.03*diam*max(abs(d@normals[i]),abs(d@normals[j]))/dd-1)
            physical.append(val)
            val=0.
            if w['intrinsic'] is not None:
                i,j=w['intrinsic']; dd=np.linalg.norm(pts[i]-pts[j])
                d0=np.linalg.norm(clouds[0][0][i]-clouds[0][0][j]); tau=.03*diam
                val=max(0.,(np.sqrt(1-1e-6)*d0*(1-dd/(2*tau))-dd)/tau)
            physical.append(val)
        for phase in self.phases:
            actual=self.bodies['actual_by_phase'][phase]
            rows=[actual['actual_sheet_relative_gram'],*[row['max_relative_reference_gram'] for row in actual['strips']]]
            metrics[self.phases.index(phase)]['actual_external_metric_maxima']=rows
            physical.extend(max(0.,a-1e-6) for a in rows)
        rr.append(np.asarray(physical))
        residual=np.concatenate([x.ravel() for x in rr])
        report=dict(phases=metrics,all_phase_union_sample_diameter=diam,endpoint_support_difference=delta,
                    support_difference_over_diameter=delta/diam,fixed_open_grip_diameter_lower=.80,
                    source_design_and_all_phases_unfrozen=True,
                    coincidence_material_and_continuum_error_unqualified=True)
        return residual,report,active
