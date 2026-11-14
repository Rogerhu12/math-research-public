"""Circle-background Fourier transfer scan for C2 radius return cycles.

Author: solver_audit, GPT-6 Astra Pro, AI-assisted, 2026-11-08.
Linear diagnostic only. Stable Floquet directions are not nonlinear solutions.
The chosen ramp joins a constant-radius core with a'=a''=0.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp,quad


def ramp(q,epsilon):
    q=np.asarray(q);w=np.ones_like(q,dtype=float);integ=q-epsilon/2
    left=q<epsilon;right=q>1-epsilon
    x=q[left];w[left]=np.sin(np.pi*x/(2*epsilon))**2
    integ[left]=x/2-epsilon*np.sin(np.pi*x/epsilon)/(2*np.pi)
    x=1-q[right];w[right]=np.sin(np.pi*x/(2*epsilon))**2
    integ[right]=1-epsilon-(x/2-epsilon*np.sin(np.pi*x/epsilon)/(2*np.pi))
    return w,integ


def constant_segment(mode,v,ratio):
    if v==0:raise ValueError('Use cylinder transfer for v=0')
    b=math.sqrt(1-v*v);m2=mode*mode
    P=np.array([[-(m2-1),-m2*b/v],[(m2-1)*v/b,m2]])
    return np.eye(2)+(ratio-1)*P


def upward(mode,delta,V,eps,dense=False):
    duration=delta/(V*(1-eps));m2=mode*mode
    def fun(q,y):
        w,I=ramp(np.array([q]),eps);a=1+delta*I[0]/(1-eps);v=V*w[0];b=math.sqrt(1-v*v)
        M=np.array([[-(m2-1)*v,-m2*b],[(m2-1)*v*v/b,m2*v]])/a
        return (duration*M@y.reshape(2,2)).ravel()
    sol=solve_ivp(fun,[0,1],np.eye(2).ravel(),method='DOP853',rtol=2e-12,atol=2e-14,dense_output=dense,max_step=.05)
    U=sol.y[:,-1].reshape(2,2)
    height=duration*((1-2*eps)*math.sqrt(1-V*V)+2*eps*quad(lambda q:math.sqrt(1-V*V*math.sin(np.pi*q/2)**4),0,1,epsabs=2e-13)[0])
    kmer=V*math.pi/(eps*duration*math.sqrt(2*(1+math.sqrt(1-V*V))))
    return dict(U=U,duration=duration,height=height,kmer=kmer,det_error=float(np.linalg.det(U)-(1+delta)),solution=sol)


def cycle_record(mode,delta,Vu,Vd,eps,up,down):
    # Reverse the downward expansion path using the exact reversal symmetry.
    R=1+delta;D=np.diag([1.,-1.]);U=up['U'];V=down['U']
    inverse=np.array([[V[1,1],-V[0,1]],[-V[1,0],V[0,0]]])/R
    T=D@inverse@D@U;trace=float(np.trace(T));disc=trace*trace-4
    W=delta;L=up['duration']+down['duration'];H=up['height']+down['height']
    norm=lambda y:math.sqrt((1+1/mode**2)*y[0]**2+y[1]**2)
    rec=dict(mode=mode,delta=delta,V_up=Vu,V_down=Vd,ramp_fraction=eps,a_min=1.,a_max=1+delta,
             W_radial_excursion=W,L_cycle=L,H_circle_cycle=H,L_over_W=L/W,
             circle_kappa_bound=max(1.,up['kmer'],down['kmer']),
             circle_kappa_bound_times_W=max(1.,up['kmer'],down['kmer'])*W,
             circle_annulus_box_diameter_over_W=math.hypot(2*(1+delta),H)/W,
             matrix=T.tolist(),trace=trace,det_error=float(np.linalg.det(T)-1),
             plane_full_spatial_ratio=norm(T@np.array([1.,0.]))/norm(np.array([1.,0.])))
    if disc<=0:
        rec.update(kind='elliptic_or_parabolic',stable_multiplier=None,stable_slope_g_over_f=None)
        return rec
    unstable=(trace+math.copysign(math.sqrt(disc),trace))/2;stable=1/unstable
    eigvals,eigvecs=np.linalg.eig(T);i=int(np.argmin(abs(eigvals)));vec=eigvecs[:,i].real
    if abs(vec[0])<1e-14:rho=None
    else:rho=float(vec[1]/vec[0])
    rec.update(kind='hyperbolic',stable_multiplier=stable,stable_slope_g_over_f=rho,
               stable_eigen_residual=float(np.linalg.norm(T@vec-stable*vec)))
    if rho is not None and rho<0:
        h=-1/(mode*mode*rho);rec['central_halfwidth_over_a0']=h;rec['budgets']={}
        for target in [.05,.2]:
            g0=target*W/2;f0=g0/rho;initial=norm(np.array([f0,g0]))/math.sqrt(2)/W
            loops=max(1,int(math.ceil(math.log(1e-6/initial)/math.log(abs(stable))))) if initial>1e-6 else 1
            height=2*h+2*loops*H
            rec['budgets'][str(target)]=dict(central_height_amplitude=g0,linear_port_f=f0,
                    linear_port_circle_fit_over_W=initial,linear_core_regularity_margin=1-(mode*mode-1)*abs(f0),
                    loops_to_circle_fit_1e_6=loops,linear_endpoint_circle_fit_over_W=initial*abs(stable)**loops,
                    symmetric_core_and_tails_L=2*h+2*loops*L,
                    circle_symmetric_band_box_over_W=math.hypot(2*(1+delta),height)/W,
                    rough_two_cap_box_over_W=math.hypot(2*(1+delta),height+2)/W)
    return rec


def exact_control_check(mode=2):
    v=.2;R=4/3;duration=(R-1)/v;m2=mode*mode;b=math.sqrt(1-v*v)
    def rhs(s,y):
        a=1+v*s
        return [-(m2-1)*v*y[0]/a-m2*b*y[1]/a,(m2-1)*v*v*y[0]/(a*b)+m2*v*y[1]/a]
    sol=solve_ivp(rhs,[0,duration],[1.,0.],method='DOP853',rtol=2e-13,atol=2e-15)
    expected=np.array([m2-(m2-1)*R,(v/b)*(m2-1)*(R-1)])
    direct=constant_segment(mode,v,R)@np.array([1.,0.])
    return dict(mode=mode,v=v,ratio=R,integrated=sol.y[:,-1].tolist(),closed_form=expected.tolist(),
                max_difference=float(np.max(abs(sol.y[:,-1]-expected))),matrix_difference=float(np.max(abs(direct-expected))))


def selected_path(rec,target=.2,points=129):
    mode=rec['mode'];delta=rec['delta'];eps=rec['ramp_fraction'];Vu=rec['V_up'];Vd=rec['V_down'];rho=rec['stable_slope_g_over_f']
    up=upward(mode,delta,Vu,eps,True);down=upward(mode,delta,Vd,eps,True);D=np.diag([1.,-1.])
    y0=np.array([target*delta/(2*rho),target*delta/2]);middle=up['U']@y0
    q=np.linspace(0,1,points);states=[];svalues=[];radii=[];vel=[]
    for t in q:
        mat=up['solution'].sol(t).reshape(2,2);w,I=ramp(np.array([t]),eps)
        states.append(mat@y0);svalues.append(up['duration']*t);radii.append(1+delta*I[0]/(1-eps));vel.append(Vu*w[0])
    # Reverse the down expansion's fundamental map from q=1 to q=1-t.
    Uend=down['U'];inv=np.array([[Uend[1,1],-Uend[0,1]],[-Uend[1,0],Uend[0,0]]])/(1+delta)
    for t in q[1:]:
        part=down['solution'].sol(1-t).reshape(2,2);w,I=ramp(np.array([t]),eps)
        mat=D@part@inv@D
        states.append(mat@middle);svalues.append(up['duration']+down['duration']*t);radii.append(1+delta*(1-I[0]/(1-eps)));vel.append(-Vd*w[0])
    states=np.array(states);radii=np.array(radii);vel=np.array(vel);m2=mode*mode
    norm=np.sqrt((1+1/m2)*states[:,0]**2+states[:,1]**2)
    linear_margin=1-(m2-1)*abs(states[:,0])/radii-abs(vel)
    theta=2*np.pi*(np.arange(256)+.173)/256
    er=np.column_stack((np.cos(theta),np.sin(theta),np.zeros(len(theta))))
    et=np.column_stack((-np.sin(theta),np.cos(theta),np.zeros(len(theta))))
    ez=np.tile([0.,0.,1.],(len(theta),1));c=np.cos(mode*theta);sn=np.sin(mode*theta)
    # This is a screening geometry made from the first-order position formula,
    # not a nonlinear flow solution. Its curvature is nevertheless evaluated exactly
    # for that parameterized trigonometric curve before sampling the minimum.
    exact_margins=[];dimensionless_kappa=[]
    for (f,g),a,v in zip(states,radii,vel):
        d=a*et-(mode-1/mode)*f*sn[:,None]*er-mode*g*sn[:,None]*ez
        dd=-a*er-(m2-1)*f*c[:,None]*er-(mode-1/mode)*f*sn[:,None]*et-m2*g*c[:,None]*ez
        speed=np.linalg.norm(d,axis=1);cross=np.linalg.norm(np.cross(d,dd),axis=1);kap=cross/speed**3
        ae=float(np.mean(speed));ak=float(ae*np.min(kap))
        dimensionless_kappa.append(ak);exact_margins.append(ak-abs(v))
    return dict(target_PV_over_W=target,scope='First-order stable-mode transport and algebraic-curve curvature screen, not a nonlinear construction.',
                initial_vector=y0.tolist(),final_vector=states[-1].tolist(),
                max_full_spatial_norm_gain=float(np.max(norm)/norm[0]),
                max_abs_f_over_a=float(np.max(abs(states[:,0])/radii)),max_abs_g_over_a=float(np.max(abs(states[:,1])/radii)),
                minimum_first_order_root_margin=float(np.min(linear_margin)),
                minimum_reconstructed_curve_root_margin=float(np.min(exact_margins)),
                minimum_reconstructed_akappa=float(np.min(dimensionless_kappa)),
                worst_s=float(svalues[int(np.argmin(exact_margins))]))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--summary',required=True);args=ap.parse_args()
    deltas=[.25,.35,.45,.6,.8,1.,1.25,1.5,2.,2.5,3.]
    velocities=[.3,.5,.7,.85,.93,.97,.99,.995]
    ramps=[.05,.1,.2];records=[];start=time.perf_counter()
    for delta in deltas:
        for eps in ramps:
            cache={v:upward(2,delta,v,eps) for v in velocities}
            for vu in velocities:
                for vd in velocities:records.append(cycle_record(2,delta,vu,vd,eps,cache[vu],cache[vd]))
    candidates=[r for r in records if r.get('central_halfwidth_over_a0') is not None and r['circle_kappa_bound_times_W']<100]
    eligible=[r for r in candidates if r['budgets']['0.2']['rough_two_cap_box_over_W']<10 and r['budgets']['0.2']['linear_core_regularity_margin']>.1]
    best=sorted(eligible,key=lambda r:abs(r['stable_multiplier']))[:12]
    by_slope=sorted(eligible,key=lambda r:r['central_halfwidth_over_a0'])[:8]
    ids=set();selected=[]
    for r in best+by_slope:
        key=(r['delta'],r['V_up'],r['V_down'],r['ramp_fraction'])
        if key in ids:continue
        ids.add(key);rr=dict(r);rr['path_screen_20pct']=selected_path(r,.2);rr['path_screen_5pct']=selected_path(r,.05);selected.append(rr)
    summary=dict(scope='Finite linear m=2 control scan only; no nonlinear or collar completion claim.',count=len(records),eligible_20pct_circle_budget=len(eligible),
                 constant_slope_control=exact_control_check(),best_plane_initial=sorted(records,key=lambda r:r['plane_full_spatial_ratio'])[:5],
                 selected_stable=selected,seconds=time.perf_counter()-start)
    with gzip.open(args.out,'wt') as f:json.dump(dict(summary=summary,records=records),f,indent=2,allow_nan=False)
    Path(args.summary).write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    brief=[]
    for r in selected:
        brief.append({k:r[k] for k in ['delta','V_up','V_down','ramp_fraction','stable_multiplier','stable_slope_g_over_f','central_halfwidth_over_a0','L_cycle','H_circle_cycle','circle_kappa_bound_times_W']}|dict(budget20=r['budgets']['0.2']['rough_two_cap_box_over_W'],margin20=r['path_screen_20pct']['minimum_reconstructed_curve_root_margin'],margin5=r['path_screen_5pct']['minimum_reconstructed_curve_root_margin']))
    print(json.dumps(dict(count=len(records),eligible=len(eligible),seconds=summary['seconds'],selected=brief,control=summary['constant_slope_control']),indent=2))

if __name__=='__main__':main()
