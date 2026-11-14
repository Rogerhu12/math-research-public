#!/usr/bin/env python3
"""Actual q106 complex angular strips and complete periodic-mean error.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Every saved physical quintic and actual background piece is retained. Real
radial boxes are paired with a complete complex psi strip. Bilinear P,W,D
(no complex conjugation) must have strictly positive real W,D and chart rho.
This supplies a single holomorphic square-root branch and pays the exact
uniform periodic trapezoidal alias error. IEEE function/node evaluation,
radial Gauss6 integration and coordinate alignment are separate costs.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from math import comb,factorial
from pathlib import Path
import resource
import sys
import time
import numpy as np
from flint import arb,ctx,fmpq as QQ

HERE=Path(__file__).resolve().parent
REAL_SOURCE=HERE/'strong_newg_continuous_mean_domain.py'
REAL_SHA='66e3c84b0f58fc7b7578615a2a6bf3823e6d7cf7cf2635d93157218f8d6facb1'
DOMAIN_SHA='d9c057155600660827770378e9a55054bfad06003fb74405d5cb2a285cb1040f'
PRIMARY_SHA='83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b)
def dy(z):return F(int(z[0]))*F(2)**int(z[1])
def rat(z):return F(int(z['numerator']),int(z['denominator']))
def binary(z):return F.from_float(float(z))
def aq(z):
    z=F(z);return arb(z.numerator)/z.denominator
def upper(z):
    m,e=arb(z).upper().man_exp();return [str(m),int(e)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('background','state-repair','radial','table','background-source','domain','primary','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--strip-widths',nargs='+',default=['1/32','3/128','1/64'])
    p.add_argument('--angular',type=int,default=1024)
    p.add_argument('--angular-max',type=int,default=4096)
    p.add_argument('--mean-angular',type=int,default=1360)
    p.add_argument('--atom-first',type=int,default=0)
    p.add_argument('--atom-limit',type=int,default=0,help='Explicit partial development only; never a complete certificate')
    a=p.parse_args();started=time.monotonic();ctx.prec=256;ctx.threads=1
    if a.out.exists():raise FileExistsError('Fresh actual complex-strip certificate required')
    widths=list(map(F,a.strip_widths))
    if not widths or not all(0<w<=F(1,16) for w in widths) or widths!=sorted(set(widths),reverse=True):
        raise ValueError('Declare decreasing distinct positive actual strip widths at most 1/16')
    if a.angular<512 or a.angular&(a.angular-1) or a.angular_max<a.angular or a.mean_angular!=1360:
        raise ValueError('The full q106 mean count and explicit complete angular boxes are required')
    if sha(REAL_SOURCE)!=REAL_SHA or sha(a.domain)!=DOMAIN_SHA or sha(a.primary)!=PRIMARY_SHA:
        raise ValueError('Actual real-domain source, positive box cover or accepted field changed')
    # Reuse only the exact pinned construction of actual background intervals
    # and input identities. Return before its old real-domain production loop.
    source=REAL_SOURCE.read_text();anchor=" rows=[];failures=[];intervals=0;atoms=0;cursor=F(0);piece_index=0;inputids={str(getattr(a,k)):sha(getattr(a,k)) for k in PINS}\n"
    if source.count(anchor)!=1:raise ValueError('Frozen real context boundary changed')
    changed=source.replace(anchor,' return locals()\n'+anchor,1)
    if changed.replace(' return locals()\n'+anchor,anchor,1)!=source:raise ValueError('Real context edit reversal failed')
    context_namespace=dict(__file__=str(REAL_SOURCE),__name__='actual_real_domain_context_only')
    exec(compile(changed,'<actual-real-domain-context-only>','exec'),context_namespace)
    argv=sys.argv;sys.argv=[argv[0]]
    for key in ('background','state_repair','radial','table','background_source','out'):
        sys.argv+=['--'+key.replace('_','-'),str(getattr(a,key))]
    try:context=context_namespace['main']()
    finally:sys.argv=argv
    R=type('RealIntervalAPI',(),{k:staticmethod(context_namespace[k]) for k in ('ai','qi','const','add','neg','sub','mul','div','square','absmax','widen','isum','dot','down','up')})
    primary,domain=read(a.primary),read(a.domain)
    manifest=context['manifest'];state=context['state'];background=context['profile'];pieces=context['pieces'];bgbox=context['background_box']
    if (not primary['solver_success'] or primary.get('audit_pending',True) or not domain['all_domain_gates'] or
        domain['primary_sha256']!=PRIMARY_SHA or domain['background_comparison_definition_sha256']!=background['comparison_definition_sha256'] or
        domain['state_comparison_definition_sha256']!=state['comparison_field_definition_sha256']):
        raise ValueError('The same actual repaired field and complete domain are required')
    M=28;n=85;L=binary(primary['meridian_length']);gauge=binary(primary['gauge_amplitude'])
    if primary['modes']!=M or manifest['complete_state_count']!=n or primary.get('chart_transition_start',0)!=0 or primary.get('chart_transition_end',1)!=1:
        raise ValueError('Full actual q106 chart required')
    inputs={str(getattr(a,k)):sha(getattr(a,k)) for k in ('background','state_repair','radial','table','background_source','domain','primary')}
    inputs[str(REAL_SOURCE)]=REAL_SHA
    coefficients=np.empty((6,manifest['original_physical_intervals'],n),dtype=np.float64);covered=0
    for block in primary['pp_coefficient_chunks']:
        path=a.primary.parent/block['file'];lo,hi=block['state_first'],block['state_last_exclusive']
        if lo!=covered or not lo<hi<=n or sha(path)!=block['sha256']:raise ValueError('Full original binary polynomial coverage/SHA')
        with gzip.open(path,'rb') as f:values=np.load(f,allow_pickle=False)
        if values.shape!=(6,manifest['original_physical_intervals'],hi-lo) or values.dtype!=np.float64 or not np.isfinite(values).all():raise ValueError('Complete finite original binary quintics required')
        coefficients[:,:,lo:hi]=values;covered=hi;inputs[str(path)]=sha(path)
    if covered!=n:raise ValueError('An original physical state was omitted')
    repair=[np.array([R.up(float(dy(r['global_correction_C0_C1_C2'][j]))) for r in state['state_bounds']]) for j in (0,1)]
    exact_cache={}
    def states_on(index,left,right):
        if index not in exact_cache:
            exact_cache.clear();exact_cache[index]=[[QQ(*float(coefficients[5-j,index,k]).as_integer_ratio()) for j in range(6)] for k in range(n)]
        origin=binary(primary['mesh'][index]);x=left-origin;h=right-left
        if not origin<=left<right<=binary(primary['mesh'][index+1]):raise ArithmeticError('Actual restricted physical interval changed')
        X=QQ(x.numerator,x.denominator);H=QQ(h.numerator,h.denominator);result=[]
        for order in (0,1):
            degree=5-order
            trans=[[QQ(comb(j,i))*X**(j-i)*H**i for j in range(i,degree+1)] for i in range(degree+1)]
            bounds=[]
            for original in exact_cache[index]:
                power=original if order==0 else [(j+1)*original[j+1] for j in range(5)]
                normalized=[sum((trans[i][j-i]*power[j] for j in range(i,degree+1)),QQ(0)) for i in range(degree+1)]
                bern=[sum((normalized[i]*QQ(comb(k,i),comb(degree,i)) for i in range(k+1)),QQ(0)) for k in range(degree+1)]
                qlo,qhi=min(bern),max(bern)
                bounds.append([R.down(float(F(int(qlo.p),int(qlo.q)))),R.up(float(F(int(qhi.p),int(qhi.q))))])
            result.append(R.widen(np.asarray(bounds).T,repair[order]))
        return result
    def cr(x):return (x,np.zeros_like(x))
    def ca(x,y):return (R.add(x[0],y[0]),R.add(x[1],y[1]))
    def cn(x):return (R.neg(x[0]),R.neg(x[1]))
    def cs(x,y):return ca(x,cn(y))
    def cm(x,y):return (R.sub(R.mul(x[0],y[0]),R.mul(x[1],y[1])),R.add(R.mul(x[0],y[1]),R.mul(x[1],y[0])))
    def scale(x,q):return (R.mul(x[0],q),R.mul(x[1],q))
    def csum(values):
        out=values[0]
        for value in values[1:]:out=ca(out,value)
        return out
    def cabs(x):return R.up(R.absmax(x[0])+R.absmax(x[1]))
    def cvecdot(x,y):return csum([cm(q,r) for q,r in zip(x,y)])
    def ccross(x,y):return [cs(cm(x[1],y[2]),cm(x[2],y[1])),cs(cm(x[2],y[0]),cm(x[0],y[2])),cs(cm(x[0],y[1]),cm(x[1],y[0]))]
    def fdot(coef,angles):return (R.dot(coef,angles[0]),R.dot(coef,angles[1]))
    def chorner(coef,z):
        out=cr(R.qi(coef[-1]))
        for c in reversed(coef[:-1]):out=ca(cm(out,z),cr(R.qi(c)))
        return out
    def csincos(z,A):
        z2=cm(z,z)
        sn=cm(z,chorner([F((-1)**j,factorial(2*j+1)) for j in range(7)],z2))
        co=chorner([F((-1)**j,factorial(2*j)) for j in range(8)],z2)
        # Absolute entire-series tails for complex arguments, not the real
        # Lagrange remainder used by the earlier real-domain constructor.
        rema=aq(A)**15/factorial(15)/(1-aq(A)**2/272)
        remb=aq(A)**16/factorial(16)/(1-aq(A)**2/306)
        ea=R.ai(rema)[1];eb=R.ai(remb)[1]
        return tuple(R.widen(q,ea) for q in sn),tuple(R.widen(q,eb) for q in co)
    qref=[binary(v) for v in primary['chart_reference_coefficients']];freq=primary['chart_reference_frequencies']
    angular_cache={};modes=R.const(2*np.arange(1,M+1,dtype=float));m2=R.const((2*np.arange(1,M+1,dtype=float))**2)
    def angular(width,N):
        key=(str(width),N)
        if key in angular_cache:return angular_cache[key]
        sn=[np.empty((2,M,N)),np.empty((2,M,N))];co=[np.empty((2,M,N)),np.empty((2,M,N))]
        for j in range(N):
            psi=2*arb.pi()*context['helper'].interval(F(j,N),F(j+1,N))
            for k in range(M):
                m=2*k+2;ss=R.ai((m*psi).sin());cc=R.ai((m*psi).cos())
                cp=aq(m*width).cosh();sp=aq(m*width).sinh()
                hypercos=np.array([1.,R.ai(cp)[1]]);hypersin=np.array([-R.ai(sp)[1],R.ai(sp)[1]])
                sn[0][:,k,j]=R.mul(ss,hypercos);sn[1][:,k,j]=R.mul(cc,hypersin)
                co[0][:,k,j]=R.mul(cc,hypercos);co[1][:,k,j]=R.neg(R.mul(ss,hypersin))
        q=np.array([R.qi(q) for q in qref]).T;indices=np.array([m//2-1 for m in freq]);mm=np.array(freq,dtype=float)
        coeff=R.mul(q,R.const(1-mm*mm))
        Q=fdot(R.div(coeff,R.const(mm)),tuple(z[:,indices] for z in sn))
        qp=fdot(coeff,tuple(z[:,indices] for z in co));qpp=cn(fdot(R.mul(coeff,R.const(mm)),tuple(z[:,indices] for z in sn)))
        A=dy(upper(sum((aq(abs((1-m*m)*v)/m)*aq(m*width).exp() for v,m in zip(qref,freq)),arb(0))))
        if not A<1:raise ArithmeticError('Actual complex small chart phase has not been paid')
        angular_cache[key]=(tuple(sn),tuple(co),Q,qp,qpp,A)
        return angular_cache[key]
    def angular_states(Y,sn,co):
        RR=Y[:,1:M+1];TT=Y[:,M+1:2*M+1];ZZ=Y[:,2*M+1:];R0=Y[:,0]
        du=[cn(fdot(R.add(R.mul(modes,RR),TT),sn)),ca(cr(R0[:,None]),fdot(R.add(RR,R.mul(modes,TT)),co)),cn(fdot(R.mul(modes,ZZ),sn))]
        dv=[cn(ca(cr(R0[:,None]),fdot(R.add(R.mul(R.add(m2,R.const(1)),RR),R.mul(R.const(2),R.mul(modes,TT))),co))),
            cn(fdot(R.add(R.mul(R.add(m2,R.const(1)),TT),R.mul(R.const(2),R.mul(modes,RR))),sn)),cn(fdot(R.mul(m2,ZZ),co))]
        return du,dv
    def enclose(row,Y,Ys,width,N):
        left,right=map(F,row['s_interval']);piece=pieces[row['background_piece']]
        radius,t=bgbox(piece,left,right)
        sn,co,Q,qp,qpp,A=angular(width,N)
        x=np.array([R.qi(left/L)[0],R.qi(right/L)[1]])
        def weight(s):
            z=s/L;return 1-z**3*(10-15*z+6*z*z)
        b=np.array([R.qi(weight(right))[0],R.qi(weight(left))[1]]);omb=R.sub(R.const(1),b)
        bp=R.mul(R.qi(-30/L),R.mul(R.square(x),R.square(R.sub(R.const(1),x))))
        bpp=R.mul(R.qi(-60/L**2),R.mul(R.mul(x,R.sub(R.const(1),x)),R.sub(R.const(1),R.mul(R.const(2),x))))
        rho=ca(cr(R.const(1)),scale(qp,b));rhoc=ca(cr(R.const(1)),qp);rp=scale(qpp,b)
        rs=scale(qp,bp);rps=scale(qpp,bp);phase=scale(Q,b);phase_s=scale(Q,bp)
        snp,cop=csincos(phase,A);cop_s=cn(cm(snp,phase_s));snp_s=cm(cop,phase_s)
        zero=cr(np.zeros((2,N)))
        U=[cn(scale(cm(rho,snp),omb)),ca(scale(cm(rho,cop),omb),scale(rhoc,b)),zero]
        Us=[cn(csum([scale(cm(rho,snp),R.neg(bp)),scale(cm(rs,snp),omb),scale(cm(rho,snp_s),omb)])),
            csum([scale(cm(rho,cop),R.neg(bp)),scale(cm(rs,cop),omb),scale(cm(rho,cop_s),omb),scale(rhoc,bp)]),zero]
        rho2=cm(rho,rho)
        ax=ca(cm(rho2,cop),cm(rp,snp));ay=cs(cm(rp,cop),cm(rho2,snp))
        axs=csum([scale(cm(cm(rho,rs),cop),R.const(2)),cm(rho2,cop_s),cm(rps,snp),cm(rp,snp_s)])
        ays=cs(ca(cm(rps,cop),cm(rp,cop_s)),ca(scale(cm(cm(rho,rs),snp),R.const(2)),cm(rho2,snp_s)))
        V=[cn(ca(scale(ax,omb),scale(rhoc,b))),ca(scale(ay,omb),scale(qpp,b)),zero]
        Vs=[cn(csum([scale(ax,R.neg(bp)),scale(axs,omb),scale(rhoc,bp)])),csum([scale(ay,R.neg(bp)),scale(ays,omb),scale(qpp,bp)]),zero]
        du,dv=angular_states(Y,sn,co);dus,dvs=angular_states(Ys,sn,co)
        factor=R.div(R.qi(gauge),radius);ratio=R.div(t,radius)
        U=[ca(base,scale(v,factor)) for base,v in zip(U,du)]
        V=[ca(base,scale(v,factor)) for base,v in zip(V,dv)]
        Us=[ca(base,cs(scale(vs,factor),scale(v,R.mul(factor,ratio)))) for base,vs,v in zip(Us,dus,du)]
        Vs=[ca(base,cs(scale(vs,factor),scale(v,R.mul(factor,ratio)))) for base,vs,v in zip(Vs,dvs,dv)]
        P=cvecdot(U,U);Ps=scale(cvecdot(U,Us),R.const(2));Z=ccross(U,V)
        Zs=[ca(x,y) for x,y in zip(ccross(Us,V),ccross(U,Vs))]
        W=cvecdot(Z,Z);Ws=scale(cvecdot(Z,Zs),R.const(2));P2=cm(P,P);P3=cm(P2,P)
        D=cs(W,scale(P3,R.square(t)))
        ts_cap=dy(piece['row']['continuous_second_absolute_upper'])+dy(piece['row']['quintic_repair_uniform_C0_C1_C2_upper'][2])
        ts=np.array([-R.qi(ts_cap)[1],R.qi(ts_cap)[1]])
        Ds=cs(Ws,ca(scale(P3,R.mul(R.const(2),R.mul(t,ts))),scale(cm(P2,Ps),R.mul(R.const(3),R.square(t)))))
        minW=float(np.min(W[0][0]));minD=float(np.min(D[0][0]));minrho=float(np.min(rho[0][0]))
        positive=min(float(radius[0]),minW,minD,minrho)>0
        record=dict(real_part_W_lower=minW,real_part_D_lower=minD,real_part_chart_rho_lower=minrho,actual_radius_lower=float(radius[0]))
        if not positive:return False,record
        def cap(z):return aq(binary(float(np.max(cabs(z)))))
        T=aq(binary(float(R.absmax(t))));Ts=aq(ts_cap);aa=aq(binary(float(radius[1])))
        cc=cvecdot(U,V);ccs=ca(cvecdot(Us,V),cvecdot(U,Vs))
        Az=cs(cm(P,V[2]),cm(cc,U[2]))
        Azs=cs(ca(cm(Ps,V[2]),cm(P,Vs[2])),ca(cm(ccs,U[2]),cm(cc,Us[2])))
        Pu,Psu,Du,Dsu,Wsu=map(cap,(P,Ps,D,Ds,Ws));Azcap,Azscap,Zcap,Zscap=map(cap,(Az,Azs,Z[2],Zs[2]))
        Wlow,Dlow,rholow=map(aq,map(binary,(minW,minD,minrho)))
        rootup=Du.sqrt();rootlow=Dlow.sqrt()
        numerator=T*Pu*Azcap+rootup*Zcap
        normal=numerator/Wlow
        normal_s=((Ts*Pu+T*Psu)*Azcap+T*Pu*Azscap+Dsu*Zcap/(2*rootlow)+rootup*Zscap)/Wlow+numerator*Wsu/Wlow**2
        nu=cap(scale(Q,bp))/rholow
        nu_s=cap(scale(Q,bpp))/rholow+cap(cm(scale(Q,R.square(bp)),qp))/rholow**2
        uz,usz=cap(U[2]),cap(Us[2])
        full=normal+nu*aa*uz
        full_s=normal_s+nu_s*aa*uz+nu*(T*uz+aa*usz)
        alias_den=(aq(a.mean_angular*width)).exp()-1
        record.update(complex_mean_integrand_Vz_absolute_upper=upper(full),complex_mean_derivative_Vsz_absolute_upper=upper(full_s),
                      complete_periodic_mean_Hs_Hss_alias_upper=[upper(2*full/alias_den),upper(2*full_s/alias_den)])
        return True,record
    records=[];failed=[];cover=F(0);height_error=F(0);maxerrs=[F(0),F(0)];quality={}
    for number,row in enumerate(domain['rows']):
        if number<a.atom_first:continue
        if a.atom_limit and len(records)>=a.atom_limit:break
        left,right=map(F,row['s_interval'])
        if not a.atom_limit and a.atom_first==0 and left!=cover:raise ArithmeticError('Full physical strip cover has a gap')
        Y,Ys=states_on(row['original_interval'],left,right);ok=False;attempts=[]
        for width in widths:
            N=a.angular
            while True:
                ok,data=enclose(row,Y,Ys,width,N)
                attempts.append(dict(strip_width=str(width),angular_boxes=N,positive=ok,**{k:v for k,v in data.items() if k.startswith('real_part_')}))
                if ok or N>=a.angular_max:break
                N*=2
            if ok:break
        item=dict(atom=number,original_interval=row['original_interval'],background_piece=row['background_piece'],s_interval=row['s_interval'],
                  whole_physical_interval_and_complex_angular_strip=True,whole_repair_homotopy=True,positive_complex_domain=ok,
                  actual_original_quintics_restricted_exactly=True,strip_width=str(width),angular_boxes=N,attempts=attempts,**data)
        records.append(item);cover=right
        if ok:
            err=list(map(dy,data['complete_periodic_mean_Hs_Hss_alias_upper']));height_error+=(right-left)*err[0]
            maxerrs=[max(x,y) for x,y in zip(maxerrs,err)];quality[str(width)]=quality.get(str(width),0)+1
        else:failed.append(number)
        if len(records)%64==0:print(json.dumps(dict(event='actual_complex_mean_strip_progress',atoms=len(records),failed=len(failed),width_counts=quality,
                                                  Hs_Hss=[float(z) for z in maxerrs],rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    complete=a.atom_first==0 and not a.atom_limit and len(records)==len(domain['rows']) and cover==L
    passed=complete and not failed
    result=dict(schema='actual-q106-complete-complex-angular-mean-strip-v1',scope=__doc__,author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
                source_sha256=sha(__file__),input_sha256=inputs,primary_sha256=PRIMARY_SHA,
                background_comparison_definition_sha256=domain['background_comparison_definition_sha256'],state_comparison_definition_sha256=domain['state_comparison_definition_sha256'],
                complete_domain_cover=complete,all_complex_domain_gates=passed,complete_atoms=len(records),failed_atoms=failed,
                exact_mean_angular=a.mean_angular,complex_strip_width_counts=quality,rows=records,
                complete_mean_alias_H_Hs_Hss_upper=[upper(aq(z)) for z in [height_error,*maxerrs]] if passed else None,
                full_mean_alias_H_Hs_Hss_display=[float(z) for z in [height_error,*maxerrs]] if passed else None,
                H_alias_scope='Single exact radial primitive of the angular alias only; radial Gauss6 integration error is separate.',
                branch='Bilinear complex P/W/D; Re(W)>0 and Re(D)>0 throughout each complete strip; principal sqrt is holomorphic and agrees with the real positive branch.',
                exact_uniform_periodic_trapezoidal_formula='2 M/(exp(N*delta)-1)',
                original_IEEE_libm_and_node_evaluation_or_coordinate_alignment_paid=False,radial_Gauss6_error_paid=False,
                original_g_PDE_reach_or_closed_surface_certified=False,new_ODE_Node_Newton_or_spatial_sampling_calls=0,
                elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True);payload=(json.dumps(result,separators=(',',':'))+'\n').encode()
    with a.out.open('wb') as f:
        with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as g:g.write(payload)
    print(json.dumps(dict(event='actual_complex_mean_strip_finished',all_complex_domain_gates=passed,atoms=len(records),failed=len(failed),
                         H_Hs_Hss=result['full_mean_alias_H_Hs_Hss_display'],path=str(a.out),sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
