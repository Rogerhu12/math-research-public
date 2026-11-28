#!/usr/bin/env python3
"""Complete original V+W Gram on explicitly selected finite tail cells.

The common radial coordinate makes r and W polynomial. The certified
background slope polynomial has a separate uniform error, which multiplies
only the small correction after the exact background Gram cancellation.
This local consumer never promotes its listed cells to a whole-surface claim.
"""
from __future__ import annotations
import argparse,bisect,gzip,hashlib,importlib.util,io,json,math,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
def load(name,p):
    if name in sys.modules:return sys.modules[name]
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m
k=load('m12_correlated_interval_kernel',HERE/'m12-correlated-gram-interval-kernel.py')
cmod=load('m12_original_central_arclength',HERE/'m12-original-central-arclength-interval.py')
I,Jet,LD=k.I,k.Jet,k.LD
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(x):return F.from_float(float(x))
def expand(x):
    if isinstance(x,Jet):return Jet([expand(a) for a in x.c])
    return I(x.lo[...,None],x.hi[...,None])
def reduce_sum(x):
    return Jet([a.sum(-1) for a in x.c]) if isinstance(x,Jet) else x.sum(-1)
def take(x,sl):return Jet([a[...,sl] for a in x.c]) if isinstance(x,Jet) else x[...,sl]
def arrq(q):
    a=[I(x) for x in q]
    return I(np.array([v.lo for v in a]),np.array([v.hi for v in a]))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),k.const_like(a[0],0))
def bpower(row):
    n=len(row)-1
    return [sum((F(math.comb(n,j)*math.comb(j,i)*(-1)**(j-i))*row[i] for i in range(j+1)),F(0)) for j in range(n+1)]
def vector_power(controls):
    columns=[bpower(list(map(F,row))) for row in controls]
    return [arrq([row[j] for row in columns]) for j in range(len(columns[0]))]
def bernstein_hull(power):
    n=len(power)-1;rows=[sum((power[j]*F(math.comb(i,j),math.comb(n,j)) for j in range(i+1)),I(0)) for i in range(n+1)]
    return I(min(float(v.lo) for v in rows),max(float(v.hi) for v in rows)).widen(F(1,2**48))
def deboor(x,knots,coeff,degree,index):
    xx=expand(x);d=[coeff[index-degree+j] for j in range(degree+1)]
    for r in range(1,degree+1):
        for j in range(degree,r-1,-1):
            left=knots[index-degree+j];right=knots[index+j+1-r]
            if right<=left:raise ArithmeticError('Nonpositive active B-spline denominator')
            alpha=(xx-left)/(right-left);d[j]=(1-alpha)*d[j-1]+alpha*d[j]
    return d[degree]

class TailGram:
    def __init__(self,args,source):
        self.args=args;self.source=source;notes=args.scripts.parent/'notes'
        meta=json.loads((notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json').read_text())
        bridge=json.loads((notes/'2026-11-09-db6f-root-exact-bridge-m12.json').read_text())
        manifest=json.loads((notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json').read_text())
        if sha(notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json')!=source['manifest_sha256']:
            raise ValueError('Original source manifest differs')
        if not source['integrated_value_from_exact_original_cumulative_sums'] or not source['exact_all_source_nodes_and_normalization_checked']:
            raise ValueError('Complete original exact source reconstruction required')
        cfg=meta['frozen_profile'];delta,vu,vd,eps=[fq(cfg[n]) for n in ('delta','vu','vd','ramp')]
        sp=delta/((1-eps)*vu)+delta/((1-eps)*vd)
        self.S=I.bounds(sp+F(bridge['exact_L']['lo']),sp+F(bridge['exact_L']['hi']))
        self.c=fq(manifest['parameters']['rCut']);self.h=self.c-fq(manifest['parameters']['rCuff']);self.T=self.S+self.h
        kk=2/I(5).sqrt();aa=1-kk;bb=F(28)*self.h/(25*self.c)
        self.R=[I(0),kk,I(-bb/2),6*aa+3*bb/2,-8*aa-3*bb/2,3*aa+bb/2]
        self.Rp=[i*self.R[i] for i in range(1,6)];self.rpmin=bernstein_hull(self.Rp).lo
        if self.rpmin<=0:raise ArithmeticError('Common chart monotonicity not certified')
        with np.load(io.BytesIO(gzip.decompress(args.data.read_bytes())),allow_pickle=False) as raw:
            rows=[[fq(v) for v in row] for row in raw['jets'][:,0,:]];end=fq(raw['mesh'][-1])
        supplier=load('tail_original_clamped_chart',args.scripts/'78718-prefix-metric-supplier-storage-v1.py')
        cuts,chart=supplier.exact_clamped_spline(meta['chart']);warp=fq(meta['warp_reference_q'])
        e0=8*warp*chart[0][0];epp=2*warp*chart[0][2]/end**2
        cor=json.loads(args.correction_bounds.read_text());arc=cor['central_arc_and_partial_primitive_proof']
        self.central=cmod.Central(rows,e0,epp,[F(arc['mean_arc_radius_lower_exact']),F(arc['mean_arc_radius_upper_exact'])])
        grid=json.loads(args.grid.read_text());result=json.loads(args.result.read_text())
        for key,path in [('field_sha256',args.field),('grid_sha256',args.grid),('data_sha256',args.data)]:
            if key in result and result[key]!=sha(path):raise ValueError('Saved actual field binding differs '+key)
        if cor['field_sha256']!=sha(args.field):raise ValueError('Correction receipt belongs to another field')
        with np.load(args.field,allow_pickle=False) as saved:
            if not np.array_equal(saved['unit_knots'],np.asarray(grid['unit_knots'])):raise ValueError('Actual knot multiset differs')
            self.knots=list(map(fq,saved['unit_knots']));self.wpm=saved['planar_modes'].astype(int);self.wzm=saved['vertical_modes'].astype(int)
            coefficients=saved['coefficients'].copy()
        n=len(self.knots)-6
        if len(coefficients)!=n-6:raise ValueError('Declared endpoint two-jet constraints differ')
        zero=I(np.zeros(coefficients.shape[1],dtype=LD))
        self.wc=[zero]*3+[I(row.astype(LD)) for row in coefficients]+[zero]*3
        self.wd=[]
        for j in range(n-1):
            den=self.knots[j+6]-self.knots[j+1]
            self.wd.append((self.wc[j+1]-self.wc[j])*F(5,1)/den if den else zero)
        self.pm=np.asarray(source['planar_modes']);self.zm=np.asarray(source['height_modes'])
        sys.path.insert(0,str(args.scripts))
        self.bgmod=load('tail_original_background_polynomial',args.scripts/'db6f-tail-background-packet-totalwidth.py')
        self.bg=self.bgmod.Background(args.primitive,notes/'2026-11-09-db6f-tail-finite-source-calibrations.json')

    def inverse_r(self,r):
        target=I((self.c-r)/self.h);l,h=LD(0),LD(1)
        for _ in range(90):
            m=(l+h)/2;res=k.poly(self.R,I(m))-target
            if res.hi<0:l=m
            elif res.lo>0:h=m
            else:
                rad=(res/I(self.rpmin)).abs_upper()
                l=max(l,k.down(m-rad));h=min(h,k.up(m+rad));break
        return (self.S+self.h*I(l,h))/self.T

    def prepare(self,row):
        self.rl,self.rr=F(row['left_exact']),F(row['right_exact'])
        self.vp=vector_power(row['V_controls']);self.vrp=vector_power(row['Vr_controls'])
        lo=self.inverse_r(self.rr);hi=self.inverse_r(self.rl);self.zbox=I(lo.lo,hi.hi)
        profile=self.bg.proposal_profile((self.rl+self.rr)/2)
        xp,x0,x1=self.bg.inverse_polynomial(profile,self.rl,self.rr)
        residual=self.bg.radial_residual(profile,xp,x0,x1,self.rl,self.rr)
        wp,rem=self.bg.slope_polynomial(profile,xp,x0,x1,8)
        self.wpoly=[I.bounds(fq(v.lo),fq(v.hi)) for v in wp]
        self.werror=I(fq(rem))+I(24)*fq(residual)
        # Uniform approximation error remains separate; never differentiate it.
        return {'source_span':row['source_span'],'source_radius_exact':[str(self.rl),str(self.rr)],
          'unit_cover_exact':[str(k.exact(self.zbox.lo)),str(k.exact(self.zbox.hi))],
          'background_profile':[profile.n,profile.j],'background_polynomial_degree':len(wp)-1,
          'background_radial_residual_upper':residual,'background_slope_error_upper_exact':str(k.exact(self.werror.hi))}

    def trig_vector(self,c,pm,zm,theta,derivative=0,negative_height=False):
        x=expand(theta);s,co=k.sincos(x*pm);ss,cc=k.sincos(x*zm)
        pp=take(c,slice(0,len(pm)));zz=take(c,slice(len(pm),None))
        if derivative:
            out=[reduce_sum(-pp*pm*s),reduce_sum(pp*pm*co),reduce_sum(-zz*zm*ss)]
        else:out=[reduce_sum(pp*co),reduce_sum(pp*s),reduce_sum(zz*cc)]
        if negative_height:out[2]=-out[2]
        return out

    def changes(self,z,theta):
        t=(self.T*z-self.S)/self.h;r=self.c-self.h*k.poly(self.R,t)
        kr=-self.T*k.poly(self.Rp,t);q=(r-self.rl)/(self.rr-self.rl)
        u=self.central.u(theta);ratio=self.central.a/self.central.speed(theta)
        vv=k.poly(self.vp,expand(q));vr=k.poly(self.vrp,expand(q))
        Vr=self.trig_vector(vr,self.pm,self.zm,u,negative_height=True)
        Vu=self.trig_vector(vv,self.pm,self.zm,u,derivative=1,negative_height=True)
        wc=deboor(z,self.knots,self.wc,5,self.index)
        wd=deboor(z,self.knots[1:-1],self.wd,4,self.index-1)
        Wz=self.trig_vector(wd,self.wpm,self.wzm,theta)
        Wt=self.trig_vector(wc,self.wpm,self.wzm,theta,derivative=1)
        aa=[v+w/kr for v,w in zip(Vr,Wz)];bb=[v+ratio*w for v,w in zip(Vu,Wt)]
        return r,u,q,aa,bb

    def evaluate(self,z,theta):
        r,u,q,aa,bb=self.changes(z,theta);sn,cs=k.sincos(u);wp=k.poly(self.wpoly,q)
        br=[cs,sn,-wp];bu=[-r*sn,r*cs,k.const_like(z,0)]
        return [2*dot(br,aa)+dot(aa,aa),dot(br,bb)+dot(aa,bu)+dot(aa,bb),2*dot(bu,bb)+dot(bb,bb)]

    def certify(self,row,angular,nr,na):
        meta=self.prepare(row);zl,zh=k.exact(self.zbox.lo),k.exact(self.zbox.hi)
        cuts=[zl]+sorted(set(x for x in self.knots if zl<x<zh))+[zh];pieces=[]
        edges=[I(F(2*j,angular))*k.PI for j in range(angular+1)]
        angles=I(np.array([v.lo for v in edges[:-1]]),np.array([v.hi for v in edges[1:]]))
        for left,right in zip(cuts,cuts[1:]):
            self.index=bisect.bisect_right(self.knots,(left+right)/2)-1
            if self.index<5 or self.index>=len(self.wc):raise ValueError('Unexpected active W knot piece')
            z=I.bounds(left,right);raw=k.tensor_enclose(self.evaluate,z,angles,nr,na)
            r,u,q,aa,bb=self.changes(z,angles)
            er=2*self.werror*I(aa[2].abs_upper());ef=self.werror*I(bb[2].abs_upper())
            E=I(raw[0]['upper'])+er;Fv=(I(raw[1]['upper'])+ef)/self.rl;G=I(raw[2]['upper'])/(self.rl*self.rl)
            # True 1+w^2>=1; denominator relaxation is explicitly paid.
            U=k.matrix_norm_bound(E,Fv,G)
            pieces.append({'unit_interval_exact':[str(left),str(right)],'W_knot_span':self.index,
              'metric_upper_exact':str(k.exact(np.max(U))),
              'gram_numerator_upper_exact':[str(k.exact(np.max(v['upper']))) for v in raw],
              'interpolation_remainder_upper_exact':[str(k.exact(np.max(v['remainder_upper']))) for v in raw],
              'node_width_upper_exact':[str(k.exact(np.max(v['node_width_max']))) for v in raw],
              'background_error_E_upper_exact':str(k.exact(np.max(er.hi))),
              'background_error_F_upper_exact':str(k.exact(np.max(ef.hi)))})
        meta['pieces']=pieces;meta['metric_upper_exact']=str(max(F(v['metric_upper_exact']) for v in pieces))
        return meta

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','data','grid','field','result','correction-bounds','source-polynomials','primitive','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--angular',type=int,default=128);p.add_argument('--radial-order',type=int,default=6);p.add_argument('--angular-order',type=int,default=10)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh local complete Gram receipt required')
    source=json.loads(a.source_polynomials.read_text());consumer=TailGram(a,source);rows=[]
    for row in source['selected_spans']:
        rows.append(consumer.certify(row,a.angular,a.radial_order,a.angular_order))
        print(json.dumps({'completed_source_cells':len(rows),'span':row['source_span'],'metric_upper':float(F(rows[-1]['metric_upper_exact'])),'seconds':time.monotonic()-start}),flush=True)
    U=max(F(v['metric_upper_exact']) for v in rows)
    report={'schema':'2ecf-original-M12-full-correlated-tail-local-Gram-v1','script_sha256':sha(__file__),
      'interval_kernel_sha256':sha(HERE/'m12-correlated-gram-interval-kernel.py'),
      'central_arclength_source_sha256':sha(HERE/'m12-original-central-arclength-interval.py'),
      'inputs':{key:sha(getattr(a,key)) for key in ('data','grid','field','result','correction_bounds','source_polynomials','primitive')},
      'same_original_Q_free_source_and_g':True,'all_source_V_and_actual_W_cross_terms_retained':True,
      'true_central_material_angle_used':True,'whole_surface_claim':False,'listed_source_cells_and_all_angles_covered':True,
      'background_uniform_error_not_differentiated':True,'central_arclength':consumer.central.audit,
      'angular_boxes':a.angular,'radial_order':a.radial_order,'angular_order':a.angular_order,
      'rows':rows,'metric_upper_exact':str(U),'metric_upper_display':float(U),'below_original_solver_tolerance':U<=F(1,500000000),
      'seconds':time.monotonic()-start}
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps({'report':str(a.out),'sha256':sha(a.out),'metric_upper':float(U),'seconds':report['seconds']}),flush=True)
if __name__=='__main__':main()
