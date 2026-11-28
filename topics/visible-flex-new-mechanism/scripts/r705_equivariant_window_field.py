"""Half-turn Cartesian joint source and SO(3) increments with a physically free crown."""
import numpy as np
from scipy.spatial import ConvexHull, distance

from r688_closed_shell_observer import SUPPORT, REFLECT, normal_and_curvature, normal_chords
from r688_joint_window_field import basis, basis_field, extrema, mv, whiten_metric
from r688_two_port_material_atlas import rotation
from r705_paid_coaxial_geometry import EX, Q


class Representation:
    def __init__(self,spans,modes,knots):
        self.knots=np.asarray(knots,float)
        if self.knots[0]!=0 or self.knots[-1]!=1 or min(np.diff(self.knots))<=0:
            raise ValueError('Incorrect physical increment knots')
        self.angular=1+2*modes
        self.columns=[]
        for radial in range(spans+3):
            for angular in range(self.angular):
                frequency=(angular+1)//2
                for component in range(3):
                    if (-1)**frequency==Q[component]:
                        self.columns.append((radial*self.angular+angular,component))
        self.shape=(len(knots),len(self.columns))

    def from_parent(self,parent):
        old=np.asarray(parent['parameters'],dtype='<f8')
        if (old.shape!=(len(self.knots),(max(i for i,j in self.columns)+1),3)
                or not np.array_equal(parent['phases'],self.knots)):
            raise ValueError('Actual old parameter layout/knots differ')
        import hashlib
        if hashlib.sha256(old.tobytes()).hexdigest()!=parent['packed_le_float64_sha256']:
            raise ValueError('Actual paid parameter SHA differs')
        retained=np.stack([old[:,i,j] for i,j in self.columns],axis=1)
        remainder=old.copy()
        for i,j in self.columns:
            remainder[:,i,j]=0
        # R688 used absolute one-exponential fields, R705 uses ordered increments.
        # Coefficient differences are only a guess even when angle parity is retained.
        q=retained.copy()
        q[2:]=np.diff(retained[1:],axis=0)
        return q,float(np.linalg.norm(remainder))

    def cartesian(self,B,row):
        coeff=np.zeros((B.shape[-1],3))
        for value,(i,j) in zip(row,self.columns,strict=True):
            coeff[i,j]=value
        f=basis_field(B,coeff)
        n=f.shape[1]//2
        f[:,n:]=f[:,:n]*Q
        return f

    def fraction(self,index,phase):
        return np.clip((phase-self.knots[index-1])/(self.knots[index]-self.knots[index-1]),0.,1.)


def maximum_distance(points,indices):
    far=-1.
    for j in range(0,len(indices),128):
        row=distance.cdist(points[indices[j:j+128]],points[indices])
        u,v=np.unravel_index(np.argmax(row),row.shape)
        if row[u,v]>far:
            far=float(row[u,v]); pair=(int(indices[j+u]),int(indices[v]))
    return far,pair


class WindowField:
    def __init__(self,atlas,phases,bodies,spans,modes,rep):
        self.atlas,self.phases,self.bodies,self.rep=atlas,phases,bodies,rep
        self.B=basis(atlas,spans,modes)
        self.base={p:atlas.geometry[p][0] for p in phases}
        self.D={p:(atlas.dt(self.base[p]),atlas.da(self.base[p])) for p in phases}
        self.width=np.sqrt(atlas.quad)
        self.shape=rep.shape
        self.curv_body=max([9.53,1/.12,bodies['shoulder_k'],*bodies['collar_k']])
        self.known_domain_min=min([bodies['shoulder_sine'],
              *[r['min_param_sine_squared'] for a in bodies['actual_by_phase'].values() for r in a['strips']]])

    def state(self,q,full=True,active=None):
        A=self.atlas
        q=np.asarray(q).reshape(self.shape)
        F=[self.rep.cartesian(self.B,row) for row in q]
        X=self.base[0.]+F[0]
        a,b=A.dt(X),A.da(X)
        S=normal_and_curvature(a,b,A.dt(X,2),A.da(a),A.da(X,2))[3]
        poses=[]; reports=[]; rr=[]; clouds=[]
        weights=A.angular_weights
        source_length=A.I[-1]@np.linalg.norm(a,axis=-1)
        for i,p in enumerate(self.phases):
            Y=self.base[p]
            yt,ya=self.D[p]
            if i:
                R=A.geometry[p][1]
                for j in range(1,len(F)):
                    f=self.rep.fraction(j,p)
                    if f>0:
                        R=R@rotation(f*F[j])
                ft,fa=mv(R,a),mv(R,b)
            else:
                ft,fa=a,b
            raw_t,raw_a=ft-yt,fa-ya
            raw_ports=[raw_t[A.paid],raw_a[A.paid]]
            # Full beta, including both paid bands. Subtracting and exactly integrating
            # the known lift is a variance-reducing quadrature, not a band deletion.
            curl=A.dt(raw_a)-A.da(raw_t)
            raw_mismatch=A.integrate(raw_t)[-1]
            naive_mismatch=A.integrate(ft)[-1]-(Y[-1]-Y[0])
            half_w=weights[:A.n]
            sigma=-float(half_w@raw_mismatch[:A.n,0]/half_w.sum()) if i else 0.
            mismatch=raw_mismatch+sigma*EX
            period=np.einsum('a,taj->tj',weights,fa)
            dperiod=np.einsum('a,taj->tj',weights,raw_a)
            # Every actual outer/crown open band is a prescribed physical position.
            # Its finite differential minus R dX is independently charged above/below.
            rt=np.where(A.paid[...,None],0.,raw_t)
            increments=(rt[1:]+rt[:-1])*(np.diff(A.t)[:,None,None]/2)
            back=np.zeros_like(rt)
            back[:-1]=np.cumsum(increments[::-1],axis=0)[::-1]
            U=A.integrate(rt)
            w=1-A.tie
            P0=Y+w[...,None]*U-A.tie[...,None]*back
            P=P0+w[...,None]*(sigma*EX)
            if not i:
                P0=P=X
            pa,pb=A.dt(P),A.da(P)
            paa,pab,pbb=A.dt(P,2),A.da(pa),A.da(P,2)
            N,k,sine,G=normal_and_curvature(pa,pb,paa,pab,pbb)
            metric=whiten_metric(G,S)
            prescribed=Y+w[...,None]*sigma*EX
            diff=P-prescribed
            jets=[diff,A.dt(diff),A.da(diff),A.dt(diff,2),A.da(A.dt(diff)),A.da(diff,2)]
            port_delta=(Y[-1]-Y[0])-sigma*EX
            excess=np.linalg.norm(port_delta,axis=-1)-np.sqrt(1+1e-6)*source_length
            if i:
                measure=self.width[...,None]
                rr.extend((curl*measure,metric*measure,
                           np.maximum(0,excess)*np.sqrt(weights/(2*np.pi))))
                for val in raw_ports:
                    rr.append(val*.12/np.sqrt(A.paid.sum()))
                for val in jets:
                    rr.append(val[A.paid]*.06/np.sqrt(A.paid.sum()))
                rr.append(np.array([max(0.,abs(sigma)-.05)]))
            poses.append((P,N,k,sine))
            # All six jets of the actual P, in its moving frame, so a rigid
            # translation is absent before differencing and restored for the hull.
            tw=[np.linalg.norm(z[:,A.n:]-z[:,:A.n]*Q,axis=-1) for z in (P,pa,pb,paa,pab,pbb)]
            tw_inner=A.bridge[:,:A.n]
            tw_outer=(A.paid&~A.bridge)[:,:A.n]
            twist=dict(order=['position','radial','angle','radial2','mixed','angle2'],
                       full=[float(z.max()) for z in tw],
                       inner_paid_band=[float(z[tw_inner].max()) for z in tw],
                       outer_paid_band=[float(z[tw_outer].max()) for z in tw],
                       inner_circle=[float(z[0].max()) for z in tw],
                       outer_circle=[float(z[-1].max()) for z in tw])
            reports.append(dict(phase=p,actual_sigma=sigma,excess_sigma=max(0.,abs(sigma)-.05),
                max_cartesian_curl=np.max(abs(curl),axis=(0,1)).tolist(),
                max_raw_two_port_components=np.max(abs(raw_mismatch),axis=0).tolist(),
                max_corrected_two_port_components=np.max(abs(mismatch),axis=0).tolist(),
                corrected_half_mean_axial=float(half_w@mismatch[:A.n,0]/half_w.sum()),
                direct_minus_control_variate_port_quadrature=float(np.max(np.linalg.norm(naive_mismatch-raw_mismatch,axis=-1))),
                enforced_band_integral_correction=float(np.max(np.linalg.norm(U[-1]-raw_mismatch,axis=-1))),
                raw_period_components=np.max(abs(period),axis=0).tolist(),
                corrected_period_components=np.max(abs(dperiod),axis=0).tolist(),
                largest_sampled_chord_minus_source_path=float(excess.max()),
                max_relative_gram=float(extrema(metric).max()),
                min_window_cross=float(np.min(np.linalg.norm(np.cross(pa,pb),axis=-1))),
                actual_half_turn_six_jet_defects=twist,
                six_paid_position_jet_defects=[float(np.linalg.norm(z[A.paid],axis=-1).max()) for z in jets],
                raw_paid_beta_defects=[float(np.linalg.norm(z,axis=-1).max()) for z in raw_ports],
                radial_angular_actual_beta_defects=[float(np.linalg.norm(z,axis=-1).max()) for z in (pa-ft,pb-fa)],
                P0_lifting_max_distance=float(np.linalg.norm(P0-Y,axis=-1).max())))
            base,normals,tags=self.bodies[p]
            known=base+tags[:,None]*(sigma*EX)
            flat=P.reshape(-1,3)+self.bodies['centers'][p]; nn=N.reshape(-1,3)
            clouds.append((np.vstack((known,flat,flat*REFLECT)),np.vstack((normals,nn,nn*REFLECT))))
        physical,report,active=self.shell(poses,clouds,reports,full,active)
        rr.append(np.asarray(physical))
        residual=np.concatenate([z.ravel() for z in rr])
        if not np.all(np.isfinite(residual)) or not np.isfinite(np.linalg.norm(residual)):
            raise ArithmeticError('Nonfinite reconstructed Cartesian or physical residual')
        return residual,report,active

    def shell(self,poses,clouds,reports,full,active):
        if full:
            hulls=[ConvexHull(x).vertices for x,n in clouds]
            e=np.vstack([clouds[i][0][ids] for i,ids in enumerate(hulls)])
            addresses=[(i,int(j)) for i,ids in enumerate(hulls) for j in ids]
            diameter,(u,v)=maximum_distance(e,ConvexHull(e).vertices)
            ends=[addresses[u],addresses[v]]
            active=[]
            # A distinct undeformed material position suffices to prove distinct tags.
            # Equal source positions alone do not certify identification or injectivity.
            refpts=self.base[0.].reshape(-1,3)+self.bodies['centers'][0.]
            label=np.vstack((self.bodies[0.][0],refpts,refpts*REFLECT))
            for i,((x,n),(P,N,k,sine)) in enumerate(zip(clouds,poses,strict=True)):
                chord=normal_chords(x,n,.03*diameter,clouds[0][0],label)
                j=int(np.argmax(x@SUPPORT))
                dia,_=maximum_distance(x,hulls[i])
                reports[i].update(chord,support=float(x[j]@SUPPORT),diameter=dia,
                    max_abs_window_principal=float(k.max()),min_window_sine_squared=float(sine.min()),
                    max_abs_principal_including_known=max(float(k.max()),self.curv_body),
                    min_right_x=float(P[...,0].min()),physical_points=len(x))
                active.append(dict(union_diameter=ends,support=j,peak=int(k.argmax()),
                    chord=chord['attaining_pair'],intrinsic=chord['projected_chord_pair']))
        if active is None:
            raise ValueError('Missing physical witnesses for this grid')
        (ai,aj),(bi,bj)=active[0]['union_diameter']
        dia=float(np.linalg.norm(clouds[ai][0][aj]-clouds[bi][0][bj]))
        sup=[float(x[w['support']]@SUPPORT) for (x,n),w in zip(clouds,active,strict=True)]
        delta=sup[-1]-sup[0]; tau=.03*dia
        physical=[max(0.,.30*dia-delta),max(0.,.20*dia-.80),max(0.,tau*self.curv_body-1),
                  max(0.,1e-8-self.known_domain_min)]
        for (P,N,k,sine),(x,n),w,row in zip(poses,clouds,active,reports,strict=True):
            physical.extend((np.maximum(0.,tau*k-1)*self.width).ravel())
            physical.extend((np.maximum(0.,1e-6-sine)*self.width).ravel())
            physical.extend((np.maximum(0.,.001-P[...,0])*self.width).ravel())
            physical.append(max(0.,tau*k.ravel()[w['peak']]-1))
            val=0.
            if w['chord'] is not None:
                i,j=w['chord']; chord=x[i]-x[j]; dd=chord@chord
                if dd>1e-24:
                    val=max(0.,2*tau*max(abs(chord@n[i]),abs(chord@n[j]))/dd-1)
            physical.append(val)
            val=0.
            if w['intrinsic'] is not None:
                i,j=w['intrinsic']; dd=np.linalg.norm(x[i]-x[j])
                d0=np.linalg.norm(clouds[0][0][i]-clouds[0][0][j])
                val=max(0.,(np.sqrt(1-1e-6)*d0*(1-dd/(2*tau))-dd)/tau)
            physical.append(val)
            ext=self.bodies['actual_by_phase'][row['phase']]
            vals=[ext['actual_sheet_relative_gram'],*[z['max_relative_reference_gram'] for z in ext['strips']]]
            physical.extend(max(0.,z-1e-6) for z in vals)
            row['actual_external_metric_maxima']=vals
        return physical,dict(phases=reports,all_phase_union_sample_diameter=dia,endpoint_support_difference=delta,
            support_difference_over_diameter=delta/dia,fixed_open_grip_diameter_lower=.80,
            continuous_domain_and_phase_qualification=False,source_design_unfrozen=True,
            raw_distinct_material_coincidences_and_seams_unqualified=True),active
