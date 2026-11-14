#!/usr/bin/env python3
"""Frozen R137/R139 ruling-label chart and its full scalar second jet.

xi is the fixed seed-normal label of the inlet ruling.  U(s,xi) is the
physical material angle.  The map is frozen from this saved base inlet;
on a changed radial metric it is only a reference chart.  Coast endpoint
radial derivatives are one-sided and generally do not match the old chart.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy import fft
from fd2d_k0_native_gc import SavedNativeCoast,native_from_inlet
from fd2d_k0_ruling_coast import ruling_coordinates


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def pulled_metric(a,U_s,U_xi):
    """Exact coordinate pullback of ds^2+a(s)^2 du^2 for any positive a."""
    a=np.asarray(a)
    return dict(g_ss=1+a*a*U_s*U_s,g_sxi=a*a*U_s*U_xi,g_xixi=a*a*U_xi*U_xi,
        determinant=a*a*U_xi*U_xi)


class FrozenRulingChart:
    def __init__(self,inlet_path):
        self.path=Path(inlet_path);self.base=SavedNativeCoast(self.path)
        self.a,self.v,self.length,self.entry_s=self.base.a,self.base.v,self.base.length,self.base.entry_s
        self.geometry=self.base.geometry

    def inlet_at_label(self,xi):
        xi=np.asarray(xi,np.longdouble);f=self.base.f
        C=np.cos(xi[...,None]*f);S=np.sin(xi[...,None]*f)
        n=C@self.base.n;m=S[...,1:]@self.base.m
        np1=-S@(f*self.base.n);mp1=C[...,1:]@(f[1:]*self.base.m)
        np2=-C@(f*f*self.base.n);mp2=-S[...,1:]@(f[1:]**2*self.base.m)
        reference=self.geometry.material_coordinate(xi);h,hp=reference['u_phi'],reference['u_phi_phi']
        return dict(u=reference['u'],n=n,m=m,n_u=np1/h,m_u=mp1/h,
            n_uu=(np2-hp*np1/h)/(h*h),m_uu=(mp2-hp*mp1/h)/(h*h),
            inlet_chart_derivative=h,inlet_chart_second=hp)

    def jet(self,sigma,xi,*,include_native=False):
        sigma=float(sigma)
        if not 0<=sigma<=self.length:raise ValueError('Outside the frozen reference coast')
        data=self.inlet_at_label(xi);n,m=data['n'],data['m'];nu,mu=data['n_u'],data['m_u']
        k=m/n;ku=mu/n-m*nu/n**2
        kuu=data['m_uu']/n-m*data['n_uu']/n**2-2*mu*nu/n**2+2*m*nu*nu/n**3
        c=ruling_coordinates(self.a,self.v,sigma,k,ku,kuu)
        h,hp=data['inlet_chart_derivative'],data['inlet_chart_second']
        out=dict(U=data['u']+c['material_shift'],U_s=c['U_s'],U_xi=c['U_t']*h,
            U_ss=c['U_ss'],U_sxi=c['U_st']*h,U_xixi=c['U_tt']*h*h+c['U_t']*hp,
            inlet_U=data['u'],inlet_U_xi=h,inlet_U_xixi=hp,D=c['D'],
            physical_s=self.entry_s+sigma,one_sided_at_coast_endpoints=True)
        if include_native:
            native=native_from_inlet(self.a,self.v,sigma,data)
            out['native']=native
            out['native_n_s_computational']=native['n_s']+out['U_s']*native['n_u']
            out['native_m_s_computational']=native['m_s']+out['U_s']*native['m_u']
            out['native_n_xi']=native['n_u']*out['U_xi']
            out['native_m_xi']=native['m_u']*out['U_xi']
            out['native_l_xi']=native['l_u']*out['U_xi']
        return out

    def definition(self):
        return dict(inlet_sha256=digest(self.path),candidate_sha256=self.base.candidate_sha256,
            a_c=self.a,v=self.v,physical_coast=[self.entry_s,self.entry_s+self.length],
            label='xi is fixed inlet seed-normal angle; inlet material t=U_seed(xi)',
            map='U=t-atan(w*k/(rho_c+w))/v',
            map_input_is_frozen=True,map_is_not_updated_with_unknown_BVP_fields=True,
            delta_scope='Reference chart remains valid as a coordinate map for modified positive a_delta; native analytic GC field belongs only to the base delta=0 metric.',
            endpoint_radial_chart_derivatives_may_jump=True,
            metric='ds^2+a_delta(s)^2*(U_s ds+U_xi dxi)^2',
            physical_fields='l,m,n remain components in the original fixed-u orthonormal frame')


def main():
    ap=argparse.ArgumentParser(description=__doc__);root=Path(__file__).resolve().parent.parent
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--fixed-chart-report',type=Path,default=root/'notes/2026-11-12-fd2d-k0-native-gc-01-report.json')
    ap.add_argument('--work',type=int,default=768);ap.add_argument('--radial-nodes',type=int,default=9)
    ap.add_argument('--stem',type=Path,required=True);args=ap.parse_args()
    if list(args.stem.parent.glob(args.stem.name+'*')):raise FileExistsError('Use a new chart output stem')
    start=time.monotonic();chart=FrozenRulingChart(args.inlet)
    xi=np.arange(args.work,dtype=np.longdouble)*(2*np.arccos(np.longdouble(-1))/args.work)
    sigma=np.linspace(0,chart.length,args.radial_nodes);fields=[];rows=[]
    names=('U','U_s','U_xi','U_ss','U_sxi','U_xixi');maps={k:[] for k in names}
    for s in sigma:
        q=chart.jet(float(s),xi,include_native=True);n=q['native']
        fields.append(np.asarray(np.stack((n['l'],n['m'],n['n']),axis=-1),float))
        for name in names:maps[name].append(np.asarray(q[name],float))
        radius=chart.a+chart.v*s;c=chart.v/radius
        Rm=q['native_m_s_computational']-q['U_s']/q['U_xi']*q['native_m_xi']-q['native_l_xi']/(radius*q['U_xi'])+2*c*n['m']
        Rn=q['native_n_s_computational']-q['U_s']/q['U_xi']*q['native_n_xi']-q['native_m_xi']/(radius*q['U_xi'])-c*(n['l']-n['n'])
        rows.append(dict(sigma=float(s),physical_s=chart.entry_s+float(s),D_min=float(np.min(q['D'])),
            U_xi_min=float(np.min(q['U_xi'])),U_s_max=float(np.max(abs(q['U_s']))),
            angle_shift_max=float(np.max(abs(q['U']-q['inlet_U']))),
            transformed_Codazzi_residual=float(max(np.max(abs(Rm)),np.max(abs(Rn))))))
    fields=np.asarray(fields);raw=fft.rfft(fields,axis=1,norm='forward');table=[]
    previous=json.loads(args.fixed_chart_report.read_text())
    if previous['inlet_sha256']!=digest(args.inlet):raise ValueError('Fixed-chart comparison uses another inlet')
    fixed={r['maximum_mode']:r['value_projection_error_max'] for r in previous['finite_projection_diagnostics']}
    for wave in (15,31,63,95,191):
        tmp=raw.copy();tmp[:,wave+1:]=0
        restored=fft.irfft(tmp,n=args.work,axis=1,norm='forward')
        err=np.max(abs(fields-restored),axis=(0,1));value=float(err.max())
        table.append(dict(maximum_integer_wave_in_label=wave,maximum_k_in_cos_2k_label=wave//2,
            component_value_errors=err.tolist(),ruling_label_maximum_error=value,
            previous_fixed_seed_phi_maximum_error=fixed[wave],improvement_factor=fixed[wave]/value))
    j=np.arange(args.work);parity={name:float(np.max(abs(fields-fields[:,idx]*sign))) for name,idx,sign in
        [('pi_period',(j+args.work//2)%args.work,np.array([1,1,1])),
         ('minus_label',(-j)%args.work,np.array([1,-1,1])),
         ('pi_minus_label',(args.work//2-j)%args.work,np.array([1,-1,1]))]}
    arrays=args.stem.with_name(args.stem.name+'-chart.npz')
    np.savez_compressed(arrays,xi=np.asarray(xi,float),sigma=sigma,physical_s=chart.entry_s+sigma,lmn=fields,
        **{k:np.asarray(v) for k,v in maps.items()},inlet_sha256=digest(args.inlet),candidate_sha256=chart.base.candidate_sha256)
    report=dict(schema='fd2d-ruling-label-actual-chart-comparison-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),fixed_chart_report_sha256=digest(args.fixed_chart_report),
        dependencies={name:digest(root/'scripts'/name) for name in ('fd2d_k0_native_gc.py','fd2d_k0_ruling_coast.py','fd2d_balanced_curvature_core.py')},
        definition=chart.definition(),angular_work=args.work,rows=rows,projection_table=table,parity=parity,
        entry_one_sided_U_s_max=rows[0]['U_s_max'],exit_one_sided_U_s_max=rows[-1]['U_s_max'],
        atlas_not_claimed_globally_C1=True,continuous_spectral_tail_bound=False,
        no_new_physical_g_created=True,arrays_file=arrays.name,arrays_sha256=digest(arrays),seconds=time.monotonic()-start)
    path=args.stem.with_name(args.stem.name+'-report.json');path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(path),sha256=digest(path),seconds=report['seconds'],table=table,
        parity=parity,entry_U_s=rows[0]['U_s_max'],exit_U_s=rows[-1]['U_s_max']),allow_nan=False))


if __name__=='__main__':main()
