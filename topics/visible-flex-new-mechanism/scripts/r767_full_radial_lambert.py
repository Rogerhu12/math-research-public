"""R767 independent direct material generators, two all-order flat characteristics and true R764 caps."""
import numpy as np
from r726_closed_spinor_fourier import public
from r758_material_jet_and_angles import J,operation,root,sine,cosine,implicit,vecjet
from r762_high_regular_circle import Two,sqrt_two
from r762_signed_lambert_material_frame import tilt
from r764_positive_slope_lambert import (circle_velocity,curve,tail,radial_rows)
from r767_integrated_material_rows import MODEL,CENTERS,A0,B0,digest,prepare,layout


def atan2jet(x):
    z=x.x.value;v=1/(1+z*z)
    a=operation(x.x,(np.arctan(z),v,-z*v*v,(3*z*z-1)*v**3/3))
    k=1/(1+x.x*x.x)
    return Two(a,k*x.d,k*x.dd-2*x.x*k*k*x.d*x.d)


def flat(radial,velocity):
    """Exact material angle increment on a true flat characteristic, including both independent angle derivatives."""
    delta=Two(radial);u=delta*(2+delta)
    y=u/(1+sqrt_two(1+(1+velocity*velocity)*u))
    return atan2jet(velocity*y/(1+y))


def fields(v):return (v.x,v.d,v.dd)


def subset(v,shape,ix):
    return J.pack({k:np.broadcast_to(a,shape)[ix] for k,a in v.a.items()})


def extended(v):
    return Two(*(J.pack({k:np.asarray(a)[...,None] for k,a in j.a.items()}) for j in fields(v)))


def expand(v,shape,ix):
    terms={}
    for k,a in v.a.items():
        out=np.zeros(shape,dtype=np.asarray(a).dtype);out[ix]=a;terms[k]=out
    return J.pack(terms)


def contraction(v,w):
    return Two(*(J.pack({k:np.sum(a*w,axis=-1) for k,a in j.a.items()}) for j in fields(v)))


def zero():return Two(J(0.),J(0.),J(0.))


def high_native(t,gain,blocks,shape):
    bg,dg=zero(),zero()
    for block in blocks:
        ix=block['i']
        if not len(ix):continue
        shape1=(len(ix),shape[1]);ang=subset(t,shape,ix)
        vel=Two(*circle_velocity(ang,gain));wide=extended(vel)
        c=block['center'];corr=zero()
        for part in block['total']:
            value=flat(J(part['z'][None,None,:]/c),wide)
            corr+=contraction(value,part['w'][None,None,:])
        # D contains the actual explicit radial derivative of the compact profiles.
        dr=J(block['delta'][:,None]/c,dr=1/c)
        D=flat(dr,vel)*Two(J(block['chi'][:,None],block['chi_r'][:,None]))-corr*Two(
                    J(block['comp'][:,None],block['comp_r'][:,None]))
        B=-corr*Two(J(block['bcomp'][:,None]))
        for part in block['partial']:
            jj=part['i'];mini=Two(*(subset(v,shape1,jj) for v in fields(vel)))
            val=flat(J(part['z'][:,None,:]/c),extended(mini))
            tmp=contraction(val,part['w'][:,None,:])
            B+=Two(*(expand(v,shape1,jj) for v in fields(tmp)))
        # The evaluated B holds only the argument's material derivative so far.
        # Its partial radial derivative is exactly (mu'/mu)(D-B) throughout the open support.
        rate=block['rate'][:,None];at_center=block['delta'][:,None]==0.
        br=(D-B)*Two(J(rate))
        br=Two(*(u.at(~at_center,v*(10/11)/c)
                 for u,v in zip(fields(br),fields(vel))))
        B+=br*Two(J(0.,dr=1.))
        bg+=Two(*(expand(v,shape,ix) for v in fields(B)))
        dg+=Two(*(expand(v,shape,ix) for v in fields(D)))
    return bg,dg


def rows_for(r,mu,w,cal,labels,receipt):
    ordinary=[x for x in labels if x[0]<100]
    if any(not 0<=d<=15 for d,j,trig in ordinary):raise ValueError('The retired R764 Hermite modes are not R767 modes.')
    old=iter(radial_rows(r,mu,w,cal,ordinary))
    out=[]
    for d,j,kind in labels:
        if d<100:
            out.append(next(old));continue
        u=receipt['columns'][str(d)];H=u['H'][:,None];Hr=u['Hr'][:,None]
        b=J(u['B'][:,None],u['Br'][:,None])
        # Keep the integrated H itself available; B is its positive material quotient for the stable square root.
        actual=J(H,Hr)
        out.append((b,J(u['D'][:,None],u['Dr'][:,None]),j,kind,
                    u['absolute_B_and_D'],u['absolute_B_and_D'],actual))
    return out


def deep_sector(side,depth,labels,par,center):
    from r764_deep_regular_lambert_solid import divided_sector
    from r764_positive_slope_material import RATIO
    edge=(A0,B0)[side==1];width=RATIO[side]*np.ldexp(1/512.,-depth)+1e-16
    small=[];values=[par[0]]
    for label,a in zip(labels,par[1:]):
        d,j,kind=label
        if d<100:
            small.append(label);values.append(a);continue
        knots=layout(d,1e-5)['cuts']
        closest=min(abs(r-edge) for r in (knots[0],knots[-1]))
        if closest<=width:
            return dict(available=False,side=side,reason='A registered direct radial support crosses the omitted deeper region.')
    return divided_sector(side,depth,small,np.asarray(values),center,ordinary_high_correction_absent_in_deep=True)


def canonical(grid,phi,w,wp,E,Ep,theta,labels,par,calibration):
    public()
    if calibration.get('material_definition')!='R764-positive-cutoff':
        raise ValueError('R767 uses the original fixed R764 positive metric.')
    receipt=calibration['r767_receipt'];ident=receipt['identity'];M=calibration['M']
    phase=theta/np.arcsin(.27)
    if (ident['model']!=MODEL or ident['theta_fraction']!=float(phase).hex() or
        ident['M']!=float(M).hex() or not 0<=phase<=1 or not 10.87<M<10.89):
        raise ValueError('Wrong R767 receipt, material scale or angle.')
    for key,v in zip(('r','w','wp','E','Ep','I'),(grid.r,w,wp,E,Ep,calibration['material_I'])):
        if ident['grid_and_material'][key]!=digest(v):raise ValueError('Stale R767 physical material receipt: '+key)
    coeff=np.asarray(par)
    if len(coeff)!=1+len(labels) or not 0<coeff[0].real<=.01:
        raise ValueError('One positive circle scale and every registered radial/angular column are required.')
    if any(not isinstance(j,(int,np.integer)) or j<0 or trig not in ('sin','cos')
           or (j==0 and trig!='cos') for _,j,trig in labels):raise ValueError('Invalid full angular frequency.')
    r=np.asarray(grid.r)[:,None]
    w=J(np.asarray(w)[:,None],np.asarray(wp)[:,None])
    m=J(np.sqrt(E)[:,None],(np.asarray(Ep)/(2*np.sqrt(E)))[:,None])
    if np.any(w.value.real>0):raise ValueError('Incorrect physical normal orientation.')
    mu=w*w/(m*(1+m));ps=np.sqrt(2)*w/root(m*(1+m))
    e,q,deep,deep_ratio,gain,unit=tail(r,mu,ps,coeff[0],phase)
    angle,g,peak=tilt(r,mu,M,theta);rows=rows_for(r,mu,w,calibration,labels,receipt)
    h=float.fromhex(ident['window'])*phase**2
    if float.fromhex(ident['window'])!=calibration.get('high_zero_window',1.e-5):
        raise ValueError('Incorrect R767 material germ width.')
    ratio=h/CENTERS[0]
    amp=96*ratio;grad=340*ratio;shift=96*ratio;width0=32*ratio
    grouped={}
    for a,row in zip(coeff[1:],rows):
        bv,dv,j,kind,bb,dd=row[:6];hv=row[6] if len(row)==7 else mu*bv
        amp+=abs(a.real)*j*bb;grad+=abs(a.real)*j*j*bb
        shift+=abs(a.real)*j*dd;width0+=abs(a.real)*dd
        old_b,old_d,old_h=grouped.get((j,kind),(J(0.),J(0.),J(0.)))
        grouped[j,kind]=old_b+a*bv,old_d+a*dv,old_h+a*hv
    if amp>=1 or peak>=.395:raise FloatingPointError('Unseparated true material area.')
    pmax=np.sqrt(2*.395*(1+amp))+abs(gain.real);radius=pmax+1.83*abs(gain.real)
    if radius>=np.sqrt(2):raise FloatingPointError('Lambert chart left its positive hemisphere.')
    angular=pmax+np.sqrt(2*.395)*grad/(2*np.sqrt(1-amp))+2.45*abs(gain.real)
    ny_rate=(1+radius**2/(4*np.sqrt(1-radius**2/4)))*angular
    gr=15*abs(theta)/(8*peak)*2/(3*np.sqrt(3));v=abs(coeff[0].real*phase)
    qc=10*v*(1.64*np.sqrt(1+amp)+.82*grad/(2*np.sqrt(1-amp))+4.65*v)
    lower=1-shift-qc-gr*ny_rate
    if lower<=0:raise FloatingPointError('Full material angle derivative has no positive lower bound.')
    shape=(len(r),len(phi));phij=J(np.asarray(phi)[None,:],dp=1.)
    calls=0
    def raw(t):
        nonlocal calls
        calls+=1
        bs,ds=high_native(t,gain,receipt['seed']['blocks'],shape)
        H=mu*bs.x;D=ds.x;Dt=ds.d;fac=1+bs.d;ft=bs.dd
        for (j,kind),(bv,dv,hv) in grouped.items():
            if kind=='sin':z,zt=sine(j*t),j*cosine(j*t)
            else:z,zt=cosine(j*t),-j*sine(j*t)
            H+=hv*z;D+=dv*z;Dt+=dv*zt;fac+=bv*zt;ft-=bv*j*j*z
        scale=root(fac+deep_ratio.at(deep,0.)**2)
        A=ps*scale;At=ps*ft/(2*scale)
        if phase:
            regular=root((ps*ps*fac+e*e).at(~deep,1.))
            A=A.at(deep,-regular);At=At.at(deep,-mu*ft/regular)
        sn,cs=sine(t),cosine(t);v,vp,vs,prim=curve(t)
        x=(A-e*vp)*cs-e*v*sn;y=(A-e*vp)*sn+e*v*cs
        xt=(At-e*vs)*cs-A*sn;yt=(At-e*vs)*sn+A*cs
        lam=root(1-(x*x+y*y)/4);ny=lam*y
        nyt=lam*yt-y*(x*xt+y*yt)/(4*lam)
        delta=D+q*(-A*v+e*prim)+g*ny
        dt=Dt+q*(-At*v-A*vp+e*(1+v*vs))+g*nyt
        extra=(-A*e*v+e*e*prim)/2
        return delta,dt,(x,y,lam,ny,H,extra,D,Dt,fac,ft)
    def real(t):
        f,d,_=raw(J(t))
        return np.broadcast_to(f.value.real,shape),np.broadcast_to(1+d.value.real,shape)
    def both(t):
        f,d,_=raw(t);return f,d
    t,err=implicit(phij,(shape,real,both),1+width0+2*np.pi*(qc+gr*ny_rate))
    _,_,(x,y,lam,ny,H,extra,D,Dt,fac,ft)=raw(t)
    nx,nz=lam*x,1-(x*x+y*y)/2;pole=(nx,ny,1+nz)
    ex=tuple(i-nx*v/(1+nz) for i,v in zip((1,0,0),pole))
    ey=tuple(i-ny*v/(1+nz) for i,v in zip((0,1,0),pole))
    delta=(1-mu)*phij+mu*t+H+extra
    c,s=cosine(delta),sine(delta);cg,sg=cosine(angle),sine(angle)
    def rotate(v):
        x,y,z=v
        return cg*x+sg*z,y,-sg*x+cg*z
    n=rotate((nx,ny,nz))
    P=rotate(tuple(c*x+s*y for x,y in zip(ex,ey)))
    T=rotate(tuple(-s*x+c*y for x,y in zip(ex,ey)))
    vec=lambda value,i,j:vecjet(value,i,j,shape)
    dot=lambda x,y:np.sum(x*y,axis=-1)
    n0,nr,nt=vec(n,0,0),vec(n,1,0),vec(n,0,1);p0,t0=vec(P,0,0),vec(T,0,0)
    cc=r*dot(t0,nr)-m.value*dot(p0,nt)
    cp=r*(dot(vec(T,0,1),nr)+dot(t0,vec(n,1,1)))-m.value*(dot(vec(P,0,1),nt)+dot(p0,vec(n,0,2)))
    angular_atoms=sum(len(b['i'])*sum(len(z['w']) for z in b['total'])+
                      sum(z['w'].size for z in b['partial']) for b in receipt['seed']['blocks'])
    cost=dict(actual_raw_angle_evaluations=calls,complete_material_angle_rows=calls*shape[0]*shape[1],
              actual_characteristic_angle_quadrature_samples=calls*shape[1]*angular_atoms,
              new_material_slope_evaluations_inside_canonical=0)
    sink=calibration.get('r767_runtime_counts')
    if sink is not None:
        for k,v in cost.items():sink[k]=sink.get(k,0)+v
    drfixed=D.jet(1,0)-Dt.value*t.jet(1,0)
    hr=mu.jet(1,0)*D.value
    hrr=receipt['mass_second']['mu_rr'][:,None]*D.value+mu.jet(1,0)*drfixed
    return dict(n=n,P=P,T=T,speed=m,shape=shape,scalar=cc,scalar_phi=cp,actual_generator_work=cost,
        canonical_positive_bounds=[lower,1-amp,1-radius**2/2],
        whole_rotated_nz_lower=np.cos(theta)*(1-radius**2/2)-np.sin(theta)*radius,
        actual_scale=float(np.real(gain)),signed_lambert_scale=unit,
        high_circle_regular_scale=float(np.real(gain)),high_circle_window=h,source_peak_mu=peak,
        implicit_jet_residuals=[err],material_angles_phi=phij.value[0],true_integrated_unit_key=receipt['key'],
        actual_H=H,actual_D=D,actual_H_t=mu*(fac-1),actual_H_tt=mu*ft,actual_D_t=Dt,actual_raw_t=t,
        actual_H_r_fixed_raw_angle=hr,actual_H_rr_fixed_raw_angle=hrr,actual_D_r_fixed_raw_angle=drfixed,
        actual_D_tt_fixed_radius=Dt.jet(0,1)/t.jet(0,1),
        literal_Jacobian_difference=dot(n0,np.cross(nr,nt))-mu.jet(1,0),
        literal_connection_phi_difference=dot(t0,vec(P,0,1))-(1-mu.value),
        literal_connection_r_difference=dot(t0,vec(P,1,0)),
        literal_common_E_difference=1+w.value**2-np.asarray(E)[:,None],periodic_real_map_definition=True)
