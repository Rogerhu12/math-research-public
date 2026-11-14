#!/usr/bin/env python3
"""Independent checks of the ellipse BVP prototype; no completion certificate.
Only notes/independent_ellipse_* files are written.  No continuation is run here.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
import sys,json,hashlib,math
from types import SimpleNamespace
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.interpolate import PPoly

NOTES=Path(__file__).resolve().parent
ROOT=Path('/workspace/scratch/f6f33987b45e/math-research')
sys.path.insert(0,str(NOTES));sys.path.insert(0,str(ROOT/'topics/large-amplitude-twist-flex/scripts'))
from repo_scan_ellipse_bvp import EllipseBVP,audit
from repo_scan_ellipse_core import PlanarEllipseCore
from repo_scan_gentle import scaled_port
from f6curve_outward_bridge_linear import read_port
from curve_stable_prefix_bvp import load_checkpoint
CFG=json.loads((NOTES/'repo_scan_ellipse_gentle_candidate.json').read_text())
PORT=scaled_port(read_port(ROOT/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json'),CFG['cut_radius'],CFG['cut_slope'])


def context(path):
    d=load_checkpoint(path)
    obj=EllipseBVP(CFG,PORT,d['config']['aspect'],d['config']['modes'],d['config']['angular'])
    p=np.asarray(d['parameters']);flow=obj.flow(p[0]);obj.initial(p)
    poly=PPoly.construct_fast(np.asarray(d['pp_coefficients']),np.asarray(d['mesh']),extrapolate=True,axis=1)
    sol=SimpleNamespace(x=np.asarray(d['mesh']),sol=poly,p=p)
    return d,obj,flow,sol


def error(actual,expected):
    norm=float(np.linalg.norm(expected))
    return dict(max_absolute=float(np.max(np.abs(actual-expected))),
                relative_l2=(float(np.linalg.norm(actual-expected)/norm) if norm>1e-25 else None))


def four_difference(fn,x,v,h):
    return (-fn(x+2*h*v)+8*fn(x+h*v)-8*fn(x-h*v)+fn(x-2*h*v))/(12*h)


def jacobians(obj,flow,sol):
    s=(flow.breaks[:-1]+flow.breaks[1:])/2
    t=s/flow.end;y=sol.sol(s);p=sol.p.copy()
    J,P=obj.fun_jac(t,y,p)
    rng=np.random.default_rng(20861109);v=rng.normal(size=y.shape);v/=np.linalg.norm(v)
    pred=np.einsum('ijk,jk->ik',J,v)
    complex_actual=obj.fun(t,y.astype(complex)+1e-25j*v,p).imag/1e-25
    report={'sample_t':t.tolist(),'state_jacobian_complex_step':error(complex_actual,pred),
            'p0_parameter_column':[],'other_interior_parameter_columns_max':float(np.max(np.abs(P[:,1:])))}
    ep=np.zeros_like(p);ep[0]=1.
    for h in [1e-4,3e-5,1e-5,3e-6,1e-6]:
        actual=four_difference(lambda pp:obj.fun(t,y,pp),p,ep,h)
        report['p0_parameter_column'].append({'step':h,**error(actual,P[:,0,:])})
    expected_Lprime=CFG['cycles']*(1/CFG['vu']+1/CFG['vd'])/(1-CFG['ramp'])
    h=1e-5
    numerical=(obj.flow(p[0]+h).end-obj.flow(p[0]-h).end)/(2*h)
    report['length_chain_rule']={'analytic_Lprime':expected_Lprime,'finite_difference_Lprime':numerical}
    obj.flow(p[0]);obj.initial(p)
    ya=sol.sol(0.);yb=sol.sol(flow.end)
    A,B,Q=obj.bc_jac(ya,yb,p)
    v=rng.normal(size=len(yb));v/=np.linalg.norm(v)
    report['right_state_boundary_jacobian']=[{'step':h,**error(four_difference(lambda yy:obj.bc(ya,yy,p),yb,v,h),B@v)} for h in [1e-4,1e-5,1e-6]]
    report['boundary_parameter_columns']=[]
    for j in range(len(p)):
        v=np.zeros_like(p);v[j]=1.
        step=1e-4 if j==0 else 3e-6/(obj.pscale[j-1]*(j+1)**2)
        actual=four_difference(lambda pp:obj.bc(ya,yb,pp),p,v,step)
        report['boundary_parameter_columns'].append({'column':j,'step':step,**error(actual,Q[:,j]),
                                                     'computed_column_norm':float(np.linalg.norm(Q[:,j]))})
    obj.initial(p);obj.flow(p[0])
    return report


def raw_curve(phi,aspect,corrections):
    phi=np.asarray(phi)
    w=np.zeros_like(phi);wp=w.copy();wpp=w.copy()
    for j,c in enumerate(corrections,start=2):
        w+=c*(np.cos(2*j*phi)-(1. if j%2==0 else np.cos(2*phi)))
        wp+=c*(-2*j*np.sin(2*j*phi)+(0. if j%2==0 else 2*np.sin(2*phi)))
        wpp+=c*(-(2*j)**2*np.cos(2*j*phi)+(0. if j%2==0 else 4*np.cos(2*phi)))
    co,si=np.cos(phi),np.sin(phi)
    zero=np.zeros_like(phi)
    F=np.stack([co+w*co,si/aspect+w*si,zero],axis=-1)
    d=np.stack([-si+wp*co-w*si,co/aspect+wp*si+w*co,zero],axis=-1)
    dd=np.stack([-co+wpp*co-2*wp*si-w*co,-si/aspect+wpp*si+2*wp*co-w*si,zero],axis=-1)
    return F,d,dd


def own_basis(M,theta):
    theta=np.asarray(theta);er=np.stack([np.cos(theta),np.sin(theta),np.zeros_like(theta)],axis=-1)
    et=np.stack([-np.sin(theta),np.cos(theta),np.zeros_like(theta)],axis=-1)
    ez=np.zeros_like(er);ez[:,2]=1
    B=np.zeros((3*M+1,len(theta),3));D=np.zeros_like(B);DD=np.zeros_like(B)
    B[0]=er;D[0]=et;DD[0]=-er
    for j in range(M):
        m=2*(j+1);c=np.cos(m*theta)[:,None];s=np.sin(m*theta)[:,None]
        ir,it,iz=1+j,M+1+j,2*M+1+j
        B[ir]=c*er;D[ir]=-m*s*er+c*et;DD[ir]=-(m*m+1)*c*er-2*m*s*et
        B[it]=s*et;D[it]=m*c*et-s*er;DD[it]=-(m*m+1)*s*et-2*m*c*er
        B[iz]=c*ez;D[iz]=-m*s*ez;DD[iz]=-m*m*c*ez
    return B,D,DD


def values(C,B):
    return np.einsum('kn,kpc->npc',C,B)


def core_checks(obj,flow,sol):
    obj.initial(sol.p);core=obj._core
    speed=lambda ph:float(np.linalg.norm(raw_curve(ph,core.aspect,core.corrections)[1]))
    perimeter,quad_error=quad(speed,0,2*np.pi,epsabs=2e-13,epsrel=2e-13,limit=200)
    a0=perimeter/(2*np.pi)
    theta=np.array([.11,.43,1.13,1.91,3.83,5.73])
    phis=[]
    for th in theta:
        f=lambda ph:quad(speed,0,ph,epsabs=2e-13,epsrel=2e-13,limit=200)[0]-a0*th
        phis.append(brentq(f,0,2*np.pi,xtol=5e-15,rtol=1e-14))
    F,d,dd=raw_curve(np.asarray(phis),core.aspect,core.corrections)
    F/=a0;d/=a0;dd/=a0
    sp=np.linalg.norm(d,axis=1);spp=np.sum(d*dd,axis=1)/sp
    Ft=d/sp[:,None];Ftt=dd/sp[:,None]**2-d*spp[:,None]/sp[:,None]**3
    observed=core.evaluate(theta)
    nt=4096;angles=2*np.pi*np.arange(nt)/nt;geom=core.evaluate(angles)
    er=np.stack([np.cos(angles),np.sin(angles),np.zeros(nt)],axis=-1)
    et=np.stack([-np.sin(angles),np.cos(angles),np.zeros(nt)],axis=-1)
    radial=np.sum(geom['F']*er,axis=1);tangent=np.sum(geom['F']*et,axis=1)
    coef=np.zeros(obj.n);coef[0]=radial.mean()
    for j in range(obj.M):
        m=2*(j+1);coef[1+j]=2*np.mean(radial*np.cos(m*angles))
        coef[obj.M+1+j]=2*np.mean(tangent*np.sin(m*angles))
        coef[obj.iz+j]=2*np.mean(geom['F'][:,2]*np.cos(m*angles))
    actual=flow.base(np.array([0.]))[:,0]+obj.q*sol.sol(0.)
    B,D,DD=own_basis(obj.M,angles)
    projected=values(actual[:,None],B)[0];pd=values(actual[:,None],D)[0];pdd=values(actual[:,None],DD)[0]
    gram=np.einsum('kpc,lpc->kl',B,B)/nt
    diag=np.r_[1.,np.full(obj.n-1,.5)]
    raw_vertices=raw_curve(np.array([0.,np.pi/2]),core.aspect,core.corrections)[0]
    return {'corrections':list(core.corrections),'not_an_exact_ellipse_when_corrections_nonzero':bool(np.any(np.asarray(core.corrections)!=0)),
            'reference_raw_a0_quad':a0,'source_raw_a0':core.raw_a0,
            'raw_a0_difference':abs(a0-core.raw_a0),'quadrature_error_estimate':quad_error,
            'arclength_reference_position':error(observed['F'],F),
            'arclength_reference_first_jet':error(observed['Ft'],Ft),
            'arclength_reference_second_jet':error(observed['Ftt'],Ftt),
            'axis_vertex_aspect':float(raw_vertices[0,0]/raw_vertices[1,1]),
            'independent_full_physical_projection_coefficient_error':float(np.max(abs(coef-actual))),
            'basis_gram_error':float(np.max(abs(gram-np.diag(diag)))),
            'dense_inlet_position_error':float(np.max(np.linalg.norm(projected-geom['F'],axis=1))),
            'dense_inlet_theta_jet_error':float(np.max(np.linalg.norm(pd-geom['Ft'],axis=1))),
            'dense_inlet_theta2_jet_error':float(np.max(np.linalg.norm(pdd-geom['Ftt'],axis=1))),
            'dense_inlet_metric_error':float(np.max(abs(np.sum(pd*pd,axis=1)-core.a0**2))),
            'spectral_tail_scope':'Source omitted-l1 values concern its sampled FFT, not a certified continuous analytic tail bound.'}


def seam_checks(obj,sol):
    c=sol.sol.c.astype(np.longdouble);h=np.diff(sol.x).astype(np.longdouble)[:,None]
    v=(((((c[0]*h+c[1])*h+c[2])*h+c[3])*h+c[4])*h+c[5])
    d=((((5*c[0]*h+4*c[1])*h+3*c[2])*h+2*c[3])*h+c[4])
    dd=(((20*c[0]*h+12*c[1])*h+6*c[2])*h+2*c[3])
    jumps=[v[:-1]-c[5,1:],d[:-1]-c[4,1:],dd[:-1]-2*c[3,1:]]
    return {'stored_float_polynomial_physical_coefficient_jump_max':[float(obj.q*np.max(abs(j))) for j in jumps],
            'stored_float_polynomial_physical_angular_l1_jump_max':[float(obj.q*np.max(np.sum(abs(j),axis=1))) for j in jumps],
            'scope':'Shared-jet Hermite construction is C2 in its exact definition; rounded PPoly coefficients exhibit the listed nonzero numerical seam jumps.'}


def mean_and_derivative_checks(obj,flow,sol):
    M=obj.M;nt=256;th=2*np.pi*np.arange(nt)/nt
    B,D,DD=own_basis(M,th)
    def coefficients(s,k=0):return flow.base(np.atleast_1d(s),k)+obj.q*sol.sol(np.atleast_1d(s),k)
    def independent_mu(s):
        s=np.atleast_1d(s);C=coefficients(s)
        d,dd=values(C,D),values(C,DD)
        lam=np.linalg.norm(d,axis=2);T=d/lam[:,:,None]
        nvec=dd-np.sum(dd*T,axis=2)[:,:,None]*T
        nn=np.linalg.norm(nvec,axis=2);N=nvec/nn[:,:,None]
        curvature=nn/lam**2;a,ap,_=flow.profile(s)
        alpha=-ap[:,None]/(a[:,None]*curvature);beta=np.sqrt(1-alpha*alpha)
        V=alpha[:,:,None]*N+beta[:,:,None]*np.cross(T,N)
        return np.mean(V[:,:,2],axis=1)
    def evaluated_jets(s,angles):
        s=np.atleast_1d(s);C,Cp,Cpp=[coefficients(s,k) for k in [0,1,2]]
        fr=flow.frame(s,C,D,DD)
        dv=flow.frame_jvp(fr,values(Cp,D),values(Cp,DD))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap'])
        dv+=ae[:,:,None]*fr['N']+(-fr['alpha']*ae/fr['beta'])[:,:,None]*fr['Bin']
        bb,bd,bdd=own_basis(M,angles)
        first=values(Cp,bb);first[:,:,2]+=fr['V'][:,:,2].mean(axis=1)[:,None]
        second=values(Cpp,bb);second[:,:,2]+=dv[:,:,2].mean(axis=1)[:,None]
        return {'s':first,'ss':second,'t':values(C,bd),'st':values(Cp,bd),'tt':values(C,bdd),
                'mu':fr['V'][:,:,2].mean(axis=1),'mup':dv[:,:,2].mean(axis=1)}
    candidates=[]
    for i in range(10,len(sol.x)-11):
        center=(sol.x[i]+sol.x[i+1])/2;width=sol.x[i+1]-sol.x[i]
        if np.min(abs(flow.breaks-center))>.3*width:candidates.append((center,width))
    chosen=[candidates[i] for i in np.linspace(0,len(candidates)-1,5,dtype=int)]
    angles=np.array([.17,.71,1.37,2.63,4.71]);gx,gw=np.polynomial.legendre.leggauss(12)
    first_weights=[(-2,1),(-1,-8),(1,8),(2,-1)]
    second_weights=[(-2,-1),(-1,16),(0,-30),(1,16),(2,-1)]
    errors=[];mu_errors=[];formal_differences=[]
    for center,width in chosen:
        expected=evaluated_jets([center],angles)
        def position(s,theta):
            s=np.atleast_1d(s);bb,_,_=own_basis(M,np.asarray(theta))
            points=values(coefficients(s),bb)
            nodes=(center+s[:,None])/2+(s[:,None]-center)*gx[None,:]/2
            height=(s-center)/2*(independent_mu(nodes.ravel()).reshape(nodes.shape)@gw)
            points[:,:,2]+=height[:,None]
            return points[0]
        for factor in [.12,.06,.03]:
            hs=width*factor;ht=1e-3
            fs=sum(w*position([center+u*hs],angles) for u,w in first_weights)/(12*hs)
            fss=sum(w*position([center+u*hs],angles) for u,w in second_weights)/(12*hs*hs)
            ft=sum(w*position([center],angles+u*ht) for u,w in first_weights)/(12*ht)
            ftt=sum(w*position([center],angles+u*ht) for u,w in second_weights)/(12*ht*ht)
            fst=sum(w*v*position([center+u*hs],angles+z*ht) for u,w in first_weights for z,v in first_weights)/(144*hs*ht)
            errors.append({'physical_s':center,'radial_step':hs,'angular_step':ht,
                           **{k:error(v,expected[k][0]) for k,v in [('s',fs),('ss',fss),('t',ft),('st',fst),('tt',ftt)]}})
        hs=.06*width
        mup=sum(w*independent_mu([center+u*hs])[0] for u,w in first_weights)/(12*hs)
        mu_errors.append({'s':center,'mean_value_error':abs(independent_mu([center])[0]-expected['mu'][0]),
                          'mean_derivative_difference':abs(mup-expected['mup'][0])})
        Cp=coefficients([center],1)
        formal=flow.base(np.array([center]),1)+obj.q*flow.fun(np.array([center]),sol.sol(np.array([center])),sol.p)
        formal_differences.append(float(np.max(abs(Cp-formal))))
    samples=np.array([s for s,w in chosen]+[flow.end])
    h6=flow.height_integral(sol,samples,nt,6);h12=flow.height_integral(sol,samples,nt,12)
    return {'actual_coordinate_derivative_differences':errors,'independent_mean_height_jets':mu_errors,
            'maximum_actual_vs_formal_projected_Cprime_difference':max(formal_differences),
            'height_quadrature_order6_vs12_max_difference':float(np.max(abs(h6-h12))),
            'mean_rule_nodes_fixed':nt,
            'scope':'Derivative tests use exact-integral interpretation of the fixed-angle mean height; Gauss rules are numerical evaluations, not a replacement mathematical definition.'}


def compare_checkpoints():
    rows=[]
    for ratio in ['1p02','1p05']:
        old=load_checkpoint(NOTES/f'repo_scan_ellipse_gentle_m4_ratio{ratio}.json.gz')
        new=load_checkpoint(NOTES/f'independent_ellipse_gentle_m4_ratio{ratio}.json.gz')
        rows.append({'ratio':ratio,'parameters_exact_match':old['parameters']==new['parameters'],
                     'frozen_profile_exact_match':old['frozen_profile']==new['frozen_profile'],
                     'mesh_exact_match':bool(np.array_equal(old['mesh'],new['mesh'])),
                     'polynomial_coefficients_exact_match':bool(np.array_equal(old['pp_coefficients'],new['pp_coefficients'])),
                     'summary_exact_match':old['summary']==new['summary']})
    return rows


def main():
    report={'scope':'Independent prototype audit; distinct from direct-band solver, no task completion claim.',
            'source_hashes':{name:hashlib.sha256((NOTES/name).read_bytes()).hexdigest()
                for name in ['repo_scan_ellipse_bvp.py','repo_scan_ellipse_core.py','repo_scan_ellipse_line.py']},
            'reproduction_comparison':compare_checkpoints(),'checks':[]}
    for name,kind in [('independent_ellipse_gentle_m4_ratio1p05.json.gz','fresh_independent_solve'),
                      ('repo_scan_ellipse_gentle_m4_ratio1p2.json.gz','existing_checkpoint_read_only_audit')]:
        d,obj,flow,sol=context(NOTES/name)
        row={'checkpoint':name,'role':kind,'aspect':obj.aspect,
             'jacobian_checks':jacobians(obj,flow,sol),
             'core_checks':core_checks(obj,flow,sol),
             'C2_seams':seam_checks(obj,sol),
             'actual_map_derivatives':mean_and_derivative_checks(obj,flow,sol)}
        report['checks'].append(row)
        print(json.dumps({'aspect':obj.aspect,'state_J_error':row['jacobian_checks']['state_jacobian_complex_step'],
                          'best_p0_J_error':min(r['relative_l2'] for r in row['jacobian_checks']['p0_parameter_column']),
                          'core_reference_position':row['core_checks']['arclength_reference_position'],
                          'inlet_position_error':row['core_checks']['dense_inlet_position_error'],
                          'inlet_theta_jet_error':row['core_checks']['dense_inlet_theta_jet_error'],
                          'inlet_theta2_jet_error':row['core_checks']['dense_inlet_theta2_jet_error'],
                          'C2_seams':row['C2_seams'],
                          'max_mean_derivative_error':max(r['mean_derivative_difference'] for r in row['actual_map_derivatives']['independent_mean_height_jets'])}),flush=True)
    (NOTES/'independent_ellipse_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'reproduction_comparison':report['reproduction_comparison'],'output':'notes/independent_ellipse_checks.json'}),flush=True)

if __name__=='__main__':main()
