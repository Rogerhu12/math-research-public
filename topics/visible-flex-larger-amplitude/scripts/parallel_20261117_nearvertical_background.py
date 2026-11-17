#!/usr/bin/env python3
"""New finite logw table sampled from a smooth near-vertical meridian.

The declared metric is the emitted Hermite table, not an unstated exact arc.
True-cut chord and return-cap diagnostics use reference mean height only.
No nonlinear field, common-g family, reach, or successful end patch is claimed.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import CubicHermiteSpline
from parallel_20261117_frenet_symbol import Frenet


def sha(raw):return hashlib.sha256(raw).hexdigest()


def segment(theta,length,k0,k1,kind):
    return dict(theta=theta,length=length,k0=k0,k1=k1,kind=kind)


def evaluate(d,s):
    u=np.asarray(s)/d['length']
    theta=d['theta']+d['k0']*s+(d['k1']-d['k0'])*d['length']*(u**3-u**4/2)
    k=d['k0']+(d['k1']-d['k0'])*(3*u*u-2*u**3)
    return theta,k


def displacement(d,s):
    t,wt=leggauss(32);s=np.atleast_1d(s)
    th,_=evaluate(d,s[:,None]*(t[None,:]+1)/2)
    return s/2*(np.cos(th)@wt),s/2*(np.sin(th)@wt)


def main(a):
    raw=a.trace.read_bytes();trace=json.loads(raw);mr=a.material_trace.read_bytes();mt=json.loads(mr)
    if mt['physical_trace_sha256']!=sha(raw):raise ValueError('Material trace has another physical parent')
    th0=np.arctan(trace['w']);thp=np.pi/2-a.peak_angle_gap;thd=np.arctan(a.deep_w)
    k0=trace['w_r']/(1+trace['w']**2)**1.5;kt=a.curvature;tau=a.ramp
    rising=[segment(th0,tau,k0,kt,'ramp')]
    th1=float(evaluate(rising[-1],tau)[0]);duration=(thp-kt*tau/2-th1)/kt
    if duration<=0:raise ValueError('No positive rising arc')
    rising.append(segment(th1,duration,kt,kt,'arc'))
    rising.append(segment(thp-kt*tau/2,tau,kt,0.,'ramp'))
    falling=[segment(thp,tau,0.,-kt,'ramp')]
    th1=thp-kt*tau/2;duration=(th1-thd-kt*tau/2)/kt
    if duration<=0:raise ValueError('No positive descending arc')
    falling.append(segment(th1,duration,-kt,-kt,'arc'))
    falling.append(segment(thd+kt*tau/2,tau,-kt,0.,'ramp'))
    Rarc=Harc=0.
    for d in rising+falling:
        r,h=displacement(d,d['length']);Rarc+=float(r[0]);Harc+=float(h[0])
    patch_height=a.extension*a.deep_w/2
    Hcap=np.sqrt((a.diameter_limit/2-a.cap_rho-a.cap_ramp)**2-a.cuff_radius**2)-a.cap_rho-a.height_slack
    height=Hcap-mt['height_mean']-patch_height
    width=a.cuff_radius-a.extension-trace['r']
    lengths=np.linalg.solve([[np.cos(thp),np.cos(thd)],[np.sin(thp),np.sin(thd)]],[width-Rarc,height-Harc])
    if np.min(lengths)<=0:raise ValueError('Budgets give a nonpositive plateau length')
    segments=rising+[segment(thp,float(lengths[0]),0.,0.,'plateau')]+falling+[segment(thd,float(lengths[1]),0.,0.,'flat')]
    rows=[];r0=trace['r'];h0=0.;s0=0.
    for j,d in enumerate(segments):
        if d['kind']=='arc':
            end=float(evaluate(d,d['length'])[0]);count=max(32,int(np.ceil(abs(np.log(np.tan(end))-np.log(np.tan(d['theta'])))/a.log_step)))
            th=np.arctan(np.exp(np.linspace(np.log(np.tan(d['theta'])),np.log(np.tan(end)),count+1)))
            ss=(th-d['theta'])/d['k0'];ss[[0,-1]]=[0.,d['length']]
        else:ss=np.linspace(0,d['length'],65 if d['kind']=='ramp' else 17)
        rr,hh=displacement(d,ss);theta,k=evaluate(d,ss)
        for i in range(len(ss)):
            if rows and i==0:continue
            w=np.tan(theta[i]);lr=k[i]/(np.sin(theta[i])*np.cos(theta[i])**2)
            rows.append(dict(r=float(r0+rr[i]),logw=float(np.log(w)),dlogwdr=float(lr),
                             cell=0,segment=j,x=float(ss[i]/d['length']),reference_s=float(s0+ss[i])))
        dr,dh=displacement(d,d['length']);r0+=float(dr[0]);h0+=float(dh[0]);s0+=d['length']
    table=dict(schema='parallel-nearvertical-Hermite-background-v1',scope=__doc__,shallow_at='left',rows=rows,
               bridge=dict(r0=trace['r'],r1=trace['r']),boundary=[],source_sha256=sha(Path(__file__).read_bytes()),
               physical_trace_sha256=sha(raw),material_trace_sha256=sha(mr),
               generating_meridian=dict(segments=segments,peak_angle_gap=a.peak_angle_gap,curvature_bound=a.curvature,
                                       ramp=a.ramp,cut_curvature=k0,arc_length=s0,height_span=h0),
               proposed_reference_patch=dict(radius_start=r0,radius_end=a.cuff_radius,w_start=a.deep_w,
                   w_polynomial_in_unit_coordinate=[1,0,0,-10,15,-6],scope='Reference-only patch, with no actual nonaxisymmetric field.'))
    table_raw=(json.dumps(table)+'\n').encode();a.background_out.write_bytes(table_raw)
    r=np.array([d['r'] for d in rows]);u=np.array([d['logw'] for d in rows]);ur=np.array([d['dlogwdr'] for d in rows]);spline=CubicHermiteSpline(r,u,ur)
    diagnostics=[]
    for order in [8,12]:
        t,wt=leggauss(order);xx=(r[:-1,None]+r[1:,None])/2+np.diff(r)[:,None]*t/2;w=np.exp(spline(xx))
        height_table=float(np.sum(np.diff(r)[:,None]/2*wt*w));length_table=float(np.sum(np.diff(r)[:,None]/2*wt*np.sqrt(1+w*w)))
        tt,tw=leggauss(96);v=(tt+1)/2;wp=a.deep_w*(1-10*v**3+15*v**4-6*v**5)
        patch_length=float(a.extension/2*(tw@np.sqrt(1+wp*wp)))
        H=mt['height_mean']+height_table+patch_height
        q=Frenet(trace['M'],a.angles);F,_,_=q.jet(np.array(trace['frenet_state']));rho=np.linalg.norm(F[:,:2],axis=1)
        chord=np.hypot(a.cuff_radius-rho,H-F[:,2]);j=int(np.argmax(chord))
        xx=(r[:-1,None]+np.diff(r)[:,None]*np.linspace(0,1,9));w=np.exp(spline(xx));kap=w*spline(xx,1)/(1+w*w)**1.5
        diagnostics.append(dict(gauss_order=order,reference_height_span=height_table,reference_length=length_table,
                   conditional_cuff_height=H,total_reference_length=length_table+patch_length,
                   maximum_actual_cut_chord=float(chord[j]),chord_slack=float(length_table+patch_length-chord[j]),
                   worst_phi=float(q.angle[j]),cut_radius_at_worst=float(rho[j]),cut_height_at_worst=float(F[j,2]),
                   sampled_max_table_curvature=float(np.max(abs(kap))),
                   conditional_cap_diameter_upper=float(2*(np.hypot(a.cuff_radius,H+a.cap_rho)+a.cap_rho+a.cap_ramp))))
    report=dict(scope=__doc__,nonlinear_success=False,background_sha256=sha(table_raw),source_sha256=table['source_sha256'],
                physical_trace_sha256=sha(raw),material_trace_sha256=sha(mr),parameters=vars(a).copy(),
                rows=len(rows),width=width,plateau_lengths=lengths.tolist(),diagnostics=diagnostics)
    report['parameters']={k:str(v) if isinstance(v,Path) else v for k,v in report['parameters'].items()}
    out_raw=(json.dumps(report)+'\n').encode();a.out.write_bytes(out_raw)
    print(json.dumps(report));print(json.dumps(dict(output_sha256=sha(out_raw))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ['trace','material-trace','background-out','out']:p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--cuff-radius',type=float,default=1.55);p.add_argument('--extension',type=float,default=.07)
    p.add_argument('--cap-rho',type=float,default=.145);p.add_argument('--cap-ramp',type=float,default=.001)
    p.add_argument('--diameter-limit',type=float,default=4.8);p.add_argument('--height-slack',type=float,default=.0001)
    p.add_argument('--curvature',type=float,default=6.5);p.add_argument('--ramp',type=float,default=.0001)
    p.add_argument('--peak-angle-gap',type=float,default=.002);p.add_argument('--deep-w',type=float,default=.0012)
    p.add_argument('--log-step',type=float,default=.01);p.add_argument('--angles',type=int,default=4096)
    main(p.parse_args())
