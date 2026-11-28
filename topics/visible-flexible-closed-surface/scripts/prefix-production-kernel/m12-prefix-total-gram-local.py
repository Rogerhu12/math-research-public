#!/usr/bin/env python3
"""Actual original-source X+C+W correlated Gram on specified prefix cells.

This local consumer preserves the original exact metric and the saved field.
It currently requires every requested native source cell to lie strictly inside
one W span, one analytic target ramp piece, one original chart piece, and the
central correction support. The local scope is explicit; no whole-surface or
completion claim is made from a partial cover.
"""
from __future__ import annotations
import argparse,bisect,gzip,hashlib,importlib.util,io,json,math,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

def load(name,path):
    if name in sys.modules:return sys.modules[name]
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
centralmod=load('m12_original_central_interval',Path(__file__).with_name('m12-original-central-arclength-interval.py'))
kern=centralmod.kern;I,Jet,LD=kern.I,kern.Jet,kern.LD;Trig=centralmod.Trig
def fq(x):return F.from_float(float(x))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def arrq(a):
    shape=np.asarray(a,dtype=object).shape;rows=[I(v) for v in np.asarray(a,dtype=object).reshape(-1)]
    return I(np.array([x.lo for x in rows]).reshape(shape),np.array([x.hi for x in rows]).reshape(shape))
def last_axis(x):
    def one(c):return c.reshape(*c.shape,1)
    return Jet([one(c) for c in x.c]) if isinstance(x,Jet) else one(x)
def at(x,k):return x[...,k]
def dot(a,b):return sum((v*w for v,w in zip(a,b)),kern.const_like(a[0],0))
def plus(*a):return [sum((x[j] for x in a),kern.const_like(a[0][j],0)) for j in range(3)]
def times(a,b):return [v*b for v in a]
def minus(a,b):return plus(a,times(b,-1))
def cart(v,trig):
    s,c=trig(1);return [v[0]*c-v[1]*s,v[0]*s+v[1]*c,v[2]]
def horner_rows(c,x):
    x=last_axis(x);v=kern.const_like(x,c[-1])
    for j in range(len(c.lo)-2,-1,-1):v=v*x+c[j]
    return v

class NativePiece:
    def __init__(self,cell,raw,old):
        self.cell=cell;self.left=fq(raw['mesh'][cell]);self.right=fq(raw['mesh'][cell+1]);self.width,columns=old.span_power(raw,cell)
        self.c=arrq(list(zip(*columns)));self.d=arrq([[F(j)*col[j]/self.width for col in columns] for j in range(1,6)])
        self.M=(len(columns)-2)//3
    def first(self,n,psi,e,ep,lam,trig=None):
        trig=trig or Trig(psi);c=horner_rows(self.c,(n-self.left)/self.width);d=horner_rows(self.d,(n-self.left)/self.width)
        M=self.M;zero=kern.const_like(psi,0)
        R=at(c,0);T=zero;Rn=at(d,0);Tn=zero;Zn=at(d,-1);Rp=zero;Tp=zero;Zp=zero
        for j in range(1,M+1):
            k=3*j;s,co=trig(k)
            R=R+at(c,j)*co;T=T+at(c,M+j)*s
            Rn=Rn+at(d,j)*co;Tn=Tn+at(d,M+j)*s;Zn=Zn+at(d,2*M+j)*co
            Rp=Rp-k*at(c,j)*s;Tp=Tp+k*at(c,M+j)*co;Zp=Zp-k*at(c,2*M+j)*s
        xp=[Rp-T,Tp+R,Zp];xn=[Rn,Tn,Zn];s3,c3=trig(3);rho=1-e*c3
        xs=times(plus(xn,times(xp,ep*s3/(3*rho))),lam);xu=times(xp,1/rho)
        return cart(xs,trig),cart(xu,trig)

class NativeBatch(NativePiece):
    """Exact polynomial rows for a batch of original source cells."""
    def __init__(self,cells,raw,old):
        pieces=[NativePiece(i,raw,old) for i in cells]
        self.cells=cells;self.lefts=arrq([p.left for p in pieces]);self.widths=arrq([p.width for p in pieces]);self.M=pieces[0].M
        self.cc=I(np.stack([p.c.lo for p in pieces],axis=1),np.stack([p.c.hi for p in pieces],axis=1))
        self.dd=I(np.stack([p.d.lo for p in pieces],axis=1),np.stack([p.d.hi for p in pieces],axis=1))
    def first(self,n,psi,e,ep,lam,trig=None):
        shape=kern.base(n).shape;extra=(1,)*(len(shape)-1);B=len(self.cells)
        self.left=self.lefts.reshape(B,*extra);self.width=self.widths.reshape(B,*extra)
        self.c=self.cc.reshape(6,B,*extra,self.cc.shape[-1]);self.d=self.dd.reshape(5,B,*extra,self.dd.shape[-1])
        return super().first(n,psi,e,ep,lam,trig)

class SavedW:
    def __init__(self,piece,pm,zm,total):
        self.left,self.right,ctrl=piece;self.total=total;self.pm=list(map(int,pm));self.zm=list(map(int,zm));self.P=len(pm)
        power=[[math.comb(5,j)*sum(((-1)**(j-k)*math.comb(j,k)*ctrl[k][m] for k in range(j+1)),F(0)) for m in range(len(ctrl[0]))] for j in range(6)]
        self.c=arrq(power);self.d=arrq([[j*v for v in power[j]] for j in range(1,6)])
    def first(self,q,theta,trig=None):
        trig=trig or Trig(theta);tau=(q/self.total-self.left)/(self.right-self.left)
        c=horner_rows(self.c,tau);d=horner_rows(self.d,tau)/((self.right-self.left)*self.total)
        zero=kern.const_like(theta,0);ws=[zero,zero,zero];wt=[zero,zero,zero]
        for j,k in enumerate(self.pm):
            s,co=trig(k);v=at(c,j);dv=at(d,j)
            ws[0]=ws[0]+dv*co;ws[1]=ws[1]+dv*s
            wt[0]=wt[0]-k*v*s;wt[1]=wt[1]+k*v*co
        for j,k in enumerate(self.zm):
            s,co=trig(k);v=at(c,self.P+j);dv=at(d,self.P+j)
            ws[2]=ws[2]+dv*co;wt[2]=wt[2]-k*v*s
        return ws,wt

class PrefixPiece:
    def __init__(self,native,W,central,lam,total,chartpoly,chart_left,end,target_poly,h,central_active=True,angle_cache=None):
        self.native,self.W,self.central=native,W,central;self.lam,self.total,self.end=lam,total,end
        self.chartpoly=chartpoly;self.chart_left=chart_left;self.target_poly=target_poly;self.h=h
        self.central_active=central_active
        self.angle_cache={} if angle_cache is None else angle_cache
        self.ep=[j*v/end for j,v in enumerate(chartpoly) if j]
        self.H=[[F(1),0,0,-10,15,-6],[0,h,0,-6*h,8*h,-3*h],
                [0,0,h*h/2,-3*h*h/2,3*h*h/2,-h*h/2]]
        self.Hq=[[j*F(v)/h for j,v in enumerate(p) if j] for p in self.H]
    def target(self,q):return self.target_poly(q) if callable(self.target_poly) else kern.poly(self.target_poly,q)
    def angular(self,theta):
        coeff=theta.c if isinstance(theta,Jet) else [theta]
        key=(isinstance(theta,Jet),tuple((x.lo.shape,x.lo.tobytes(),x.hi.shape,x.hi.tobytes()) for x in coeff))
        if key not in self.angle_cache:
            C=self.central;trig=Trig(theta);self.angle_cache[key]={'trig':trig,'u':C.u(theta,trig),'speed':C.speed(theta,trig)}
        entry=self.angle_cache[key]
        if self.central_active and 'd0' not in entry:
            C=self.central;trig=entry['trig'];u=entry['u'];speed=entry['speed']
            psi0=kern.implicit_angle(C.e0,u);p0trig=Trig(psi0);s0,c0=p0trig(3);rho=1-C.e0*c0;rp=3*C.e0*s0
            gamma=C.gamma(theta,0,trig);gamma1=C.gamma(theta,1,trig);oldgamma=C.gamma(psi0,0,p0trig);oldgamma1=C.gamma(psi0,1,p0trig)
            P=C.second(psi0,0,p0trig);P1=C.second(psi0,1,p0trig)
            entry['d0']=minus(times(gamma,1/C.a),oldgamma)
            entry['d0u']=minus(times(gamma1,1/speed),times(oldgamma1,1/rho))
            entry['d2']=times(P,-self.lam*self.lam/rho)
            entry['d2u']=times(minus(times(P1,rho),times(P,rp)),-self.lam*self.lam/(rho**3))
        return entry
    def __call__(self,n,theta):
        # In each univariate derivative pass the other coordinate is an
        # interval-valued parameter. Dropping its exactly zero higher jets
        # is algebraically exact and avoids multiplying by zero jet rows.
        n=kern.drop_constant_jet(n);theta=kern.drop_constant_jet(theta)
        C=self.central;angular=self.angular(theta);trig=angular['trig'];q=n/self.lam;e=kern.poly(self.chartpoly,n/self.end-self.chart_left);ep=kern.poly(self.ep,n/self.end-self.chart_left)
        u=angular['u'];psi=kern.implicit_angle(e,u);ptrig=Trig(psi)
        xs,xu=self.native.first(n,psi,e,ep,self.lam,ptrig)
        speed=angular['speed'];ws,wt=self.W.first(q,theta,trig)
        wu=times(wt,C.a/speed)
        if not self.central_active:
            ys=plus(xs,ws);yu=plus(xu,wu);f=self.target(q)
            return [dot(ys,ys)-1,dot(ys,yu)/f,dot(yu,yu)/(f*f)-1]
        d0=angular['d0'];d0u=angular['d0u']
        zero=kern.const_like(theta,0);d1=[zero,zero,1-self.lam]
        d2=angular['d2'];d2u=angular['d2u']
        h=[kern.poly(p,q/self.h) for p in self.H];hq=[kern.poly(p,q/self.h) for p in self.Hq]
        cs=plus(times(d0,hq[0]),times(d1,hq[1]),times(d2,hq[2]))
        cu=plus(times(d0u,h[0]),times(d2u,h[2]))
        ys=plus(xs,cs,ws);yu=plus(xu,cu,wu);f=self.target(q)
        return [dot(ys,ys)-1,dot(ys,yu)/f,dot(yu,yu)/(f*f)-1]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('scripts','data','field','grid','result','correction-bounds','out'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--element',type=int,default=16);ap.add_argument('--source-cells',type=int,nargs='+');ap.add_argument('--complete-element',action='store_true');ap.add_argument('--angular',type=int,default=128)
    ap.add_argument('--nr',type=int,default=12);ap.add_argument('--na',type=int,default=12);ap.add_argument('--radial-subdivisions',type=int,default=1)
    ap.add_argument('--batch',type=int,default=8)
    a=ap.parse_args();began=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh local total Gram report required')
    scripts=a.scripts;notes=scripts.parent/'notes'
    old=load('prefix_total_old_source',scripts/'6a65-m12-up-patch-exact-geometry-budget.py');B=load('prefix_total_old_Bernstein',scripts/'6a65-m12-local-bernstein-angular-metric-budget.py');supplier=load('prefix_total_old_chart',scripts/'78718-prefix-metric-supplier-storage-v1.py')
    metap=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json';bridgep=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    if sha(a.data)!=B.DATA_SHA or sha(metap)!=B.META_SHA or sha(bridgep)!=B.BRIDGE_SHA:raise ValueError('Original source definition differs')
    meta=json.loads(metap.read_text());bridge=json.loads(bridgep.read_text());grid=json.loads(a.grid.read_text());result=json.loads(a.result.read_text());cor=json.loads(a.correction_bounds.read_text())
    for r in (result,cor):
        if r['field_sha256']!=sha(a.field) or r['grid_sha256']!=sha(a.grid):raise ValueError('Saved field identity differs')
    if not result['original_exact_metric_unchanged'] or not cor['continuous_all_knots_and_all_angles']:raise ValueError('Original source/spline facts missing')
    with np.load(io.BytesIO(gzip.decompress(a.data.read_bytes())),allow_pickle=False) as f:raw={k:f[k].copy() for k in ('mesh','jets','mean_increments')}
    end=fq(raw['mesh'][-1]);cfg=meta['frozen_profile'];delta,vu,vd,eps,eta=[fq(cfg[k]) for k in ('delta','vu','vd','ramp','ramp_eta')]
    Tu=delta/(vu*(1-eps));Td=delta/(vd*(1-eps));Slo=Tu+Td+F(bridge['exact_L']['lo']);Shi=Tu+Td+F(bridge['exact_L']['hi'])
    S=I.bounds(Slo,Shi);lam=end/S;total=S+(fq(.6)-fq(.15));h=Tu*eps
    cut,chart=supplier.exact_clamped_spline(meta['chart']);warp=8*fq(meta['warp_reference_q'])
    rows=[[fq(x) for x in row] for row in raw['jets'][:,0,:]];arc=cor['central_arc_and_partial_primitive_proof']
    C=centralmod.Central(rows,warp*chart[0][0],2*warp*chart[0][2]/end**2,(F(arc['mean_arc_radius_lower_exact']),F(arc['mean_arc_radius_upper_exact'])))
    with np.load(a.field,allow_pickle=False) as f:
        knots=list(map(fq,f['unit_knots']));coef=[[fq(x) for x in row] for row in f['coefficients']];pm=f['planar_modes'];zm=f['vertical_modes']
    pieces=B.extract_bezier(knots,coef);piece=pieces[a.element];W=SavedW(piece,pm,zm,total)
    us=[F(0),eps*eta,eps*(1-eta),eps,1-eps,1-eps+eps*eta,1-eps*eta,F(1)]
    profile=[(Tu*u0,Tu*u1,(F(0),Tu,F(0),k)) for k,(u0,u1) in enumerate(zip(us,us[1:]))]
    target=supplier.Target.__new__(supplier.Target);target.eps=eps;target.eta=eta;target.sign=1;target.delta=delta
    edges=[kern.PI*F(j,3*a.angular) for j in range(a.angular+1)]
    angles=I(np.array([[x.lo for x in edges[:-1]]]),np.array([[x.hi for x in edges[1:]]]));records=[]
    print(json.dumps({'initialized_seconds':time.monotonic()-began,'central_audit':C.audit}),flush=True)
    Klo=end*(Shi+fq(.6)-fq(.15))/Shi;Khi=end*(Slo+fq(.6)-fq(.15))/Slo
    wl=piece[0]*Klo;wr=piece[1]*Khi;mesh=list(map(fq,raw['mesh']));lamlo=end/Shi;lamhi=end/Slo
    if a.complete_element==bool(a.source_cells):raise ValueError('Choose complete element or explicit source cells')
    cells=[i for i in range(len(mesh)-1) if mesh[i+1]>wl and mesh[i]<wr] if a.complete_element else a.source_cells
    groups={};segments=[]
    for cell in cells:
        nl=max(mesh[cell],wl);nr=min(mesh[cell+1],wr)
        if nr<=nl:continue
        if nr>=min(mesh[meta['correction_start_index']],3*end/4):raise ValueError('Prototype excludes common-cut/cutoff supports')
        for j in range(len(chart)):
            jl=max(nl,end*cut[j]);jr=min(nr,end*cut[j+1])
            if jr<=jl:continue
            for pk,(ql,qr,info) in enumerate(profile):
                pl=max(jl,lamlo*ql);pr=min(jr,lamhi*qr)
                if pr<=pl:continue
                for active,cl,cr in ((True,F(0),lamhi*h),(False,lamlo*h,end)):
                    ll=max(pl,cl);rr=min(pr,cr)
                    if rr<=ll:continue
                    for sub in range(a.radial_subdivisions):
                        l=ll+(rr-ll)*F(sub,a.radial_subdivisions);r=ll+(rr-ll)*F(sub+1,a.radial_subdivisions)
                        row={'cell':cell,'left':l,'right':r,'chart':j,'target':pk,'central_active':active,'subdivision':sub}
                        groups.setdefault((j,pk,active),[]).append(row);segments.append((l,r))
    ordered=sorted(segments);covered=wl if a.complete_element else (ordered[0][0] if ordered else wl)
    for l,r in ordered:
        if a.complete_element and l>covered:raise ValueError('Analytic common refinement leaves a radial gap')
        covered=max(covered,r)
    if a.complete_element and covered<wr:raise ValueError('Analytic common refinement does not cover the complete element envelope')
    for (j,pk,active),group in groups.items():
        tp=target.a_prefix_poly(F(0),F(1),profile[pk][2])
        for off in range(0,len(group),a.batch):
            chunk=group[off:off+a.batch];native=NativeBatch([r['cell'] for r in chunk],raw,old)
            consumer=PrefixPiece(native,W,C,lam,total,[warp*v for v in chart[j]],cut[j],end,tp,h,active)
            left=arrq([r['left'] for r in chunk]);right=arrq([r['right'] for r in chunk]);radial=I(left.lo[:,None],right.hi[:,None])
            b=time.monotonic();enclosures=kern.tensor_enclose(consumer,radial,angles,a.nr,a.na)
            norm=kern.matrix_norm_bound(*[row['upper'] for row in enclosures])
            for ix,part in enumerate(chunk):
                worst=int(np.argmax(norm[ix]));detail=[]
                for row in enclosures:
                    detail.append({k:{'maximum_exact':str(kern.exact(np.max(v[ix]))),'at_worst_metric_box_exact':str(kern.exact(v[ix,worst]))} for k,v in row.items()})
                rec={'source_cell':part['cell'],'native_interval':[str(part['left']),str(part['right'])],
                    'source_chart_piece':j,'target_analytic_piece':pk,'central_C_active':active,'radial_subdivision':part['subdivision'],
                    'domain_is_actual_source_chart_target_C_W_intersection':True,'polynomial_extensions_enclosed_on_complete_outer_box':True,
                    'relative_metric_upper_exact':str(kern.exact(np.max(norm[ix]))),'relative_metric_upper':float(np.max(norm[ix])),
                    'worst_angular_box':worst,'angular_boxes':a.angular,'component_details':detail}
                records.append(rec)
            print(json.dumps({'last_source_cell':chunk[-1]['cell'],'pieces_done':len(records),'batch_max':float(np.max(norm)),
                              'batch_seconds':time.monotonic()-b,'seconds':time.monotonic()-began}),flush=True)
    out={'schema':'2ecf-original-M12-actual-local-prefix-correlated-total-Gram-v1','script_sha256':sha(__file__),
        'interval_kernel_sha256':sha(kern.__file__),'central_interval_sha256':sha(centralmod.__file__),
        'data_sha256':sha(a.data),'field_sha256':sha(a.field),'grid_sha256':sha(a.grid),'result_sha256':sha(a.result),'correction_bounds_sha256':sha(a.correction_bounds),
        'meta_sha256':sha(metap),'bridge_sha256':sha(bridgep),'actual_W_element':a.element,'source_cells':cells,
        'same_original_exact_g':True,'actual_original_X_plus_C_plus_saved_W':True,'old_uniform_metric_defect_not_added':True,
        'tensor_interpolation_nodes_per_box':[a.nr,a.na],'complete_interval_jet_remainders_paid':True,
        'all_angles_by_original_D3_and_reflection_symmetry':True,'all_points_of_listed_native_intervals':True,
        'complete_selected_W_element':a.complete_element,'outer_native_W_envelope':[str(wl),str(wr)],
        'analytic_common_refinement_complete_on_actual_intersections':a.complete_element,
        'whole_prefix_claim':False,'whole_surface_claim':False,'README_completion_claim':False,
        'central_true_arclength_proof':C.audit,'rows':records,'maximum_relative_metric_upper':max(r['relative_metric_upper'] for r in records),
        'seconds':time.monotonic()-began}
    a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps({'report':str(a.out),'maximum':out['maximum_relative_metric_upper'],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
