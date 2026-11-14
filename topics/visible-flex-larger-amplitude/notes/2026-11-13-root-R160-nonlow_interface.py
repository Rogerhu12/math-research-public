#!/usr/bin/env python3
"""Complete nonlow image and Jw with all 1150 low input frequencies retained.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No assumption that the chosen low radii solve their equations is made here.
All decisions use Fraction; floats in output are display only.
Import NonlowInterface, prepare(low_caps), images(prepared,r,h), and
action(prepared,r,h,du,dr,dh). Directions may be any nonnegative fractions.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ex(v):
    if isinstance(v,F):return v
    if isinstance(v,int):return F(v)
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    return F(int(v['numerator']),int(v['denominator']))


def rec(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))


def up(v):
    if v<0:raise ArithmeticError('Positive comparison data required')
    if not v:return F(0)
    unit=F(2)**(v.numerator.bit_length()-v.denominator.bit_length()-96)
    return (v//unit+1)*unit


def inv(q,m,v):
    a,b,c,d=m;x=q-a;y=q-d;det=x*y-b*c
    if min(x,y,det)<=0 or min(b,c)<0:return None
    return ((y*v[0]+b*v[1])/det,(c*v[0]+x*v[1])/det)


class NonlowInterface:
    """Exact conditionally valid half of the full 1200-component map.

    low_caps[j][n//2-1] is the complete P/K strong local-V pair radius
    on the common strip, with each component's radial sup taken first.
    high coordinates: block5 balanced physical; block21 balanced positive
    profile; all other blocks physical localV. They are exactly R126's.
    """
    def __init__(self,joint,near):
        self.joint=read(joint) if isinstance(joint,(str,Path)) else joint
        self.near=read(near) if isinstance(near,(str,Path)) else near
        a,b=self.joint,self.near
        if not(a['all_gates'] and all(a['gates'].values()) and b['all_gates'] and all(b['gates'].values())
               and a['comparison_partition']==b['comparison_partition'] and a['fixed_common_strip']==b['common_strip']
               and a['profile_high_block']==21 and a['physical_high_comparison_blocks']==[5]
               and ex(a['transverse_radius'])==F(1,32) and a['high_cutoff']==34816):
            raise ArithmeticError('Same complete R126 domain, kernel and near-window input required')
        if isinstance(joint,(str,Path)):
            h=[v for k,v in b['input_hashes'].items() if Path(k).name==Path(joint).name]
            if h!=[sha(joint)]:raise ArithmeticError('The frozen actual R126 source identity changed')
        self.KT=270*F(2)**-34;self.K=F(23,9)+self.KT;self.C=F(10)
        self.B=ex(a['physical_high_conversion']);self.D=ex(a['high_direction_divided_by_frame'])
        self.Rstar=ex(a['complete_Hessian_domain_upper']);self.Rprofile=ex(a['profile_physical_upper'])
        if self.K!=ex(a['full_complete_Hessian_upper']) or self.Rstar!=F(2)**-34:
            raise ArithmeticError('Original complete complex Hessian domain required')
        self.N=25;self.modes=list(range(2,93,2));self.partition=a['comparison_partition']
        self.G={p:[[ex(v) for v in r['all_finite_source_materials'][str(p)]] for r in a['rows']] for p in (2,1,0)}
        self.A={p:[[ex(v) for v in r['all_high_source_materials']['physical_source'][str(p)]] for r in a['rows']] for p in (2,1,0)}
        self.Q={p:[[ex(v) for v in r['all_high_source_materials']['already_divided_by_frame'][str(p)]] for r in a['rows']] for p in (2,1,0)}
        self.Gc=[ex(r['profile_source21_kernels']['finite_cross']) for r in a['rows']]
        self.Gs=[ex(r['profile_source21_kernels']['finite_square']) for r in a['rows']]
        self.Ac=[ex(r['profile_source21_kernels']['high_cross']) for r in a['rows']]
        self.As=[ex(r['profile_source21_kernels']['high_square']) for r in a['rows']]
        self.V=[ex(r['V_max']) for r in a['rows']]
        self.headf=[ex(r['true_finite_head_and_centre']) for r in a['rows']]
        self.headh=[ex(r['true_high_head_and_complete_centre']) for r in a['rows']]
        self.L=[[[ex(c['coefficient']) for c in s['pure_DQ_centre_to_middle_by_low_input']]
                 for s in r['source_rows']] for r in b['rows']]
        self.windows=[r['window'] for r in b['actual_near_windows']]
        self.W=[[[ex(v) for v in row] for row in r['source_rows']] for r in b['actual_near_windows']]
        self.windowof={m:w for w,(lo,hi) in enumerate(self.windows) for m in range(lo,hi+1,2)}
        if sorted(self.windowof)!=list(range(94,185,2)) or len(self.windows)!=19:
            raise ArithmeticError('All true near outputs required')
        self.pairs=[(ki,ni,self.windowof[k+n],F(5*k*n+1,4*(1+k)*(1+n)))
                    for ki,k in enumerate(self.modes) for ni,n in enumerate(self.modes) if k+n>=94]
        for a0 in (self.L,):
            if len(a0)!=25 or any(len(row)!=i+1 for i,row in enumerate(a0)):
                raise ArithmeticError('All causal source blocks required')

    def normalize_modes(self,caps):
        if len(caps)!=25 or any(len(r)!=46 for r in caps):raise ValueError('Exactly25x46 physical low mode radii required')
        value=[[ex(v) for v in r] for r in caps]
        if min(min(r) for r in value)<0:raise ValueError('Nonnegative low modes required')
        return value

    def quadratic_masses(self,caps,direction=None):
        """Actual ordered sum-frequency source masses, not one common cap.

        With direction=None this is Q(u), so ordered pairs cost alpha/2.
        Otherwise this is DQ(u)[du], with the full ordered alpha.
        """
        if direction is None:direction=caps;factor=F(1,2)
        else:factor=F(1)
        out=[]
        for j in range(25):
            row=[F(0)]*19
            for k,n,w,alpha in self.pairs:
                row[w]+=factor*alpha*caps[j][k]*direction[j][n]
            out.append(row)
        return out

    def prepare(self,low_caps):
        caps=self.normalize_modes(low_caps);U=[sum(r,F(0)) for r in caps]
        masses=self.quadratic_masses(caps);pf=[];ph=[];pureq=[]
        for i in range(25):
            qr=[];fr=[];hr=[]
            for j in range(i+1):
                qv=sum((v*u for v,u in zip(self.L[i][j],caps[j])),F(0))+sum((self.W[w][i][j]*masses[j][w] for w in range(19)),F(0))
                tm=self.KT*(self.C*U[j]+U[j]*U[j]/2)
                qr.append(qv);fr.append(qv+self.G[2][i][j]*tm);hr.append(self.A[2][i][j]*tm)
            pureq.append(qr);pf.append(fr);ph.append(hr)
        return dict(caps=caps,U=U,quadratic_masses=masses,pure_q= pureq,pure_f=pf,pure_h=ph)

    def coefficients(self,i,j):
        """F/H quadratic forms k[g(Cr+r²/2)+c(C+r)h+s h²/2]."""
        if j==21:return (self.G[2][i][j],self.Gc[i],self.Gs[i],self.A[2][i][j],self.Ac[i],self.As[i])
        if j==5:return (self.G[2][i][j],self.B*self.G[1][i][j],self.B*self.B*self.G[0][i][j],
                        self.A[2][i][j],self.D*self.Q[1][i][j],self.D*self.B*self.Q[0][i][j])
        g=self.G[2][i][j];a=self.A[2][i][j]
        return (g,g,g,a,a,a)

    def feedback(self,i,j,U,r,h):
        g,c,s,a,d,t=self.coefficients(i,j);C=self.C+U
        return (self.K*(g*(C*r+r*r/2)+c*(C+r)*h+s*h*h/2),
                self.K*(a*(C*r+r*r/2)+d*(C+r)*h+t*h*h/2))

    def derivative_nn(self,i,j,U,r,h):
        g,c,s,a,d,t=self.coefficients(i,j);C=self.C+U
        return (self.K*(g*(C+r)+c*h),self.K*(c*(C+r)+s*h),
                self.K*(a*(C+r)+d*h),self.K*(d*(C+r)+t*h))

    def domain(self,p,r,h):
        return [(self.C+p['U'][j]+r[j])*self.V[j]+h[j]*(self.Rprofile if j==21 else self.B if j==5 else self.V[j]) for j in range(25)]

    def images(self,p,r,h):
        if len(r)!=25 or len(h)!=25 or min(r+h)<0:raise ValueError('All nonnegative finite and high radii required')
        f=[];z=[]
        for i in range(25):
            vf=self.headf[i]+sum(p['pure_f'][i],F(0));vh=self.headh[i]+sum(p['pure_h'][i],F(0))
            for j in range(i+1):
                x,y=self.feedback(i,j,p['U'][j],r[j],h[j]);vf+=x;vh+=y
            f.append(vf);z.append(vh)
        return dict(finite=f,high=z,domain=self.domain(p,r,h))

    def action(self,p,r,h,du,dr,dh):
        """Full exact nonlow Jw; arbitrary nonnegative1150+25+25 direction.

        Low-frequency directions are never combined before pure Q's true
        sum-frequency convolution. Complete T and mixed N use their paid
        operator bounds and the required common l1 masses.
        """
        du=self.normalize_modes(du)
        if len(dr)!=25 or len(dh)!=25 or min(dr+dh)<0:raise ValueError('Nonnegative complete nonlow direction required')
        dU=[sum(row,F(0)) for row in du];qm=self.quadratic_masses(p['caps'],du)
        f=[];z=[]
        for i in range(25):
            vf=F(0);vh=F(0)
            for j in range(i+1):
                qd=sum((v*d for v,d in zip(self.L[i][j],du[j])),F(0))+sum((self.W[w][i][j]*qm[j][w] for w in range(19)),F(0))
                td=self.KT*(self.C+p['U'][j])*dU[j]
                g,c,s,a,d,t=self.coefficients(i,j)
                nn=self.derivative_nn(i,j,p['U'][j],r[j],h[j])
                vf+=qd+self.G[2][i][j]*td+self.K*(g*r[j]+c*h[j])*dU[j]+nn[0]*dr[j]+nn[1]*dh[j]
                vh+=self.A[2][i][j]*td+self.K*(a*r[j]+d*h[j])*dU[j]+nn[2]*dr[j]+nn[3]*dh[j]
            f.append(vf);z.append(vh)
        return dict(finite=f,high=z,domain=self.domain(p,r,h))

    def low_columns(self,p,r,h):
        """Compact1150 input columns; high columns are shared within a block."""
        qd=[]
        for j in range(25):
            mass=[[F(0)]*46 for _ in range(19)]
            for k,n,w,alpha in self.pairs:mass[w][n]+=alpha*p['caps'][j][k]
            qd.append(mass)
        rows=[]
        for i in range(25):
            rr=[]
            for j in range(i+1):
                g,c,s,a,d,t=self.coefficients(i,j)
                common_f=self.G[2][i][j]*self.KT*(self.C+p['U'][j])+self.K*(g*r[j]+c*h[j])
                common_h=self.A[2][i][j]*self.KT*(self.C+p['U'][j])+self.K*(a*r[j]+d*h[j])
                rr.append(dict(finite=[self.L[i][j][n]+sum((self.W[w][i][j]*qd[j][w][n] for w in range(19)),F(0))+common_f for n in range(46)],high_shared=common_h))
            rows.append(rr)
        return rows

    def solve(self,p,padding=F(17,16),q=F(1,2),limit=128):
        """Find/verify only the nonlow ball with p's low ball held arbitrary."""
        if not 1<padding<=2 or not 0<q<1:raise ValueError('Fixed exact margins required')
        r=[];h=[];weights=[];rows=[];failure=None
        for i in range(25):
            af=self.headf[i]+sum(p['pure_f'][i],F(0));ah=self.headh[i]+sum(p['pure_h'][i],F(0))
            for j in range(i):
                f,z=self.feedback(i,j,p['U'][j],r[j],h[j]);af+=f;ah+=z
            linear=self.derivative_nn(i,i,p['U'][i],F(0),F(0))
            seed=inv(F(1),linear,(af,ah))
            if seed is None:failure=dict(block=i,reason='affine_inverse_failed');break
            ri,hi=up(padding*seed[0]),up(padding*seed[1]);history=[]
            for it in range(limit):
                ff,fh=self.feedback(i,i,p['U'][i],ri,hi);ff+=af;fh+=ah
                history.append(dict(finite_radius=rec(ri),high_radius=rec(hi),finite_ratio=rec(up(ff/ri)),high_ratio=rec(up(fh/hi))))
                if ff<ri and fh<hi:break
                if ff>=ri:ri=up(padding*ff)
                if fh>=hi:hi=up(padding*fh)
                dom=(self.C+p['U'][i]+ri)*self.V[i]+hi*(self.Rprofile if i==21 else self.B if i==5 else self.V[i])
                if dom>=self.Rstar:break
            r.append(ri);h.append(hi)
            nn=[self.derivative_nn(i,j,p['U'][j],r[j],h[j]) for j in range(i+1)]
            target=(1+sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i)),F(0)),
                    1+sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i)),F(0)))
            w=inv(q,nn[i],target)
            if w is None:failure=dict(block=i,reason='nonlow_positive_metric_failed');break
            wf,wh=map(up,w);weights.append((wf,wh))
            df=sum((nn[j][0]*weights[j][0]+nn[j][1]*weights[j][1] for j in range(i+1)),F(0))/wf
            dh=sum((nn[j][2]*weights[j][0]+nn[j][3]*weights[j][1] for j in range(i+1)),F(0))/wh
            ff,fh=self.feedback(i,i,p['U'][i],ri,hi);ff+=af;fh+=ah
            dom=(self.C+p['U'][i]+ri)*self.V[i]+hi*(self.Rprofile if i==21 else self.B if i==5 else self.V[i])
            gates=dict(finite_strict_selfmap=ff<ri,high_strict_selfmap=fh<hi,whole_complete_physical_ball=dom<self.Rstar,finite_conditional_distance=df<q,high_conditional_distance=dh<q)
            rows.append(dict(target_block=i,low_total=rec(p['U'][i]),finite_radius=rec(ri),high_radius=rec(hi),finite_image=rec(up(ff)),high_image=rec(up(fh)),domain=rec(up(dom)),
                finite_distance_weight=rec(wf),high_distance_weight=rec(wh),finite_distance_exact=rec(df),high_distance_exact=rec(dh),radius_history=history,
                pure_low_quadratic_middle=rec(up(sum(p['pure_q'][i],F(0)))),pure_low_complete_T_middle=rec(up(sum(p['pure_f'][i],F(0))-sum(p['pure_q'][i],F(0)))),pure_low_complete_T_high=rec(up(sum(p['pure_h'][i],F(0)))),
                complete_causal_nonlow_derivative=[[rec(up(v)) for v in block] for block in nn],gates=gates))
            print(json.dumps(dict(event='conditional_nonlow_block',block=i,all_gates=all(gates.values()),finite=float(ri),high=float(hi),low_total=float(p['U'][i]))),flush=True)
            if not all(gates.values()):failure=dict(block=i,reason='actual_conditional_gate_failed',gates=gates);break
        return dict(r=r,h=h,weights=weights,rows=rows,failure=failure,all_gates=failure is None and len(rows)==25)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('joint','joint-resource','joint-certificate','near','near-resource','low-input','out-prefix'):
        ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--low-scale',default='2');ap.add_argument('--zero-low',action='store_true')
    a=ap.parse_args();start=time.monotonic();output=Path(str(a.out_prefix)+'.json.gz');summary=Path(str(a.out_prefix)+'-summary.json')
    if output.exists() or summary.exists():raise FileExistsError('Fresh conditional whole-frequency consumer output required')
    ju,nu,jc=read(a.joint_resource),read(a.near_resource),read(a.joint_certificate)
    if not(ju['exitcode']==nu['exitcode']==0 and ju['termination_signal'] is None and nu['termination_signal'] is None and jc['all_gates']):
        raise ArithmeticError('Both original formal successful commands and independent R126 certificate required')
    model=NonlowInterface(a.joint,a.near);candidate=read(a.low_input);scale=F(a.low_scale)
    if scale<=0:raise ValueError('Positive fixed conditional low scaling required')
    if len(candidate['rows'])!=25 or any(r['target_block']!=j or r['modes']!=model.modes for j,r in enumerate(candidate['rows'])):
        raise ArithmeticError('All actual low input positions and frequencies required')
    caps=[[F(0) if a.zero_low else scale*ex(v) for v in r['separate_mode_caps']] for r in candidate['rows']]
    p=model.prepare(caps);sol=model.solve(p)
    columns=model.low_columns(p,sol['r'],sol['h']) if sol['all_gates'] else []
    for i,row in enumerate(sol['rows']):
        if columns:row['complete_low_input_derivative_columns']=[dict(source_block=j,finite_by_low_input=[rec(up(v)) for v in rr['finite']],high_same_for_each_low_input=rec(up(rr['high_shared']))) for j,rr in enumerate(columns[i])]
    gates=dict(paid_all_original_inputs=True,all1150_low_modes_retained=True,all19_actual_near_windows=True,
        complete_pure_low_T_and_mixed_N_paid=True,conditional_all25_nonlow_budget=sol['all_gates'])
    result=dict(schema='visible-flex-exact-1150-low-input-complete-nonlow-conditional-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=all(gates.values()),gates=gates,failure=sol['failure'],
        comparison_partition=model.partition,low_modes=model.modes,low_scale=rec(scale),low_mode_radii=[[rec(v) for v in row] for row in caps],
        rows=sol['rows'],same_R126_parameter_domain=True,transverse_radius=rec(F(1,32)),complete_mean_and_inverse_retained=True,
        chosen_low_ball_is_only_a_conditional_input=True,low_equation_closed=False,full1200_component_fixed_point_claimed=False,
        pure_low_quadratic_support=[94,184],pure_low_quadratic_infinite_high_exactly_zero=True,
        high_coordinate_spaces=['balanced_positive_profile' if j==21 else 'balanced_physical' if j==5 else 'physical_localV' for j in range(25)],
        complete_T_Hessian=rec(model.KT),complete_N_Hessian=rec(model.K),whole_physical_domain_limit=rec(model.Rstar),
        source_sha256=sha(__file__),input_hashes={str(getattr(a,n)):sha(getattr(a,n)) for n in ('joint','joint_resource','joint_certificate','near','near_resource','low_input')},
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=9) as packed:packed.write((json.dumps(result,separators=(',',':'))+'\n').encode())
    if output.stat().st_size>=5_000_000:raise ArithmeticError('Partition the conditional matrix output')
    short={k:v for k,v in result.items() if k not in ('rows','low_mode_radii')};short['primary']=dict(path=str(output),bytes=output.stat().st_size,sha256=sha(output))
    summary.write_text(json.dumps(short,indent=2)+'\n')
    print(json.dumps(dict(all_gates=result['all_gates'],failure=result['failure'],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'],output_bytes=output.stat().st_size)),flush=True)


if __name__=='__main__':main()
