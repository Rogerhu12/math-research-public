#!/usr/bin/env python3
"""Stream original exact tail cells into complete correlated Gram enclosures.

All original raw blobs and exact accumulated dyadic source coefficients are
retained. Fixed angular interval expressions are cached without refitting.
Original D3/reflection identities reduce the certified angular fundamental
domain, with all frequency and reality conditions explicitly checked.
"""
from __future__ import annotations
import argparse,bisect,gzip,hashlib,importlib.util,json,math,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
def load(name,p):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m
base=load('original_first_tail_correlated',HERE/'2ecf-m12-first-tail-correlated/m12-tail-total-gram-local.py')
k,I,Jet=base.k,base.I,base.Jet
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

ORIGINAL_STREAM_SHA='9c5d93d84a61f96a3770130f6b992eed0779c82c5e35a5399598e8565c3ee7e9'
ADAPTIVE_PARENT_SHA='03c3f0ea36b1003a2d6b91e3e5b9cae2d493ca6a8784563ce4a26a82956948cf'

def lower_constant_jet(x):
    return x.c[0] if isinstance(x,Jet) and all(np.all(c.lo==0) and np.all(c.hi==0) for c in x.c[1:]) else x

class CachedTail(base.TailGram):
    def __init__(self,args,source):
        super().__init__(args,source);self.angular_cache=[];self.cache_hits=0;self.cache_misses=0
        # The first-tail route never used this central second trace; normalize
        # its auxiliary parameter explicitly before any future reuse.
        C=self.central;C.epp*=8;cm=base.cmod
        P=cm.convq({0:F(1),3:-C.e0/2,-3:-C.e0/2},cm.planar(C.rows[2]))
        for mode,value in C.gamma_coeff.items():
            cm.add(P,mode+3,C.epp*mode*value/6);cm.add(P,mode-3,-C.epp*mode*value/6)
        C.second_coeff={mode:value for mode,value in P.items() if value}
        for pm,zm in [(self.pm,self.zm),(self.wpm,self.wzm)]:
            if np.any(pm%3!=1) or np.any(zm%3!=0):raise ValueError('Original D3 angular symmetry is not retained')
        # Avoid any binary64 proposal in the strict monotonicity bound.
        n=len(self.Rp)-1
        b=[sum((self.Rp[j]*F(math.comb(i,j),math.comb(n,j)) for j in range(i+1)),I(0)) for i in range(n+1)]
        self.rpmin=min(v.lo for v in b)
        if self.rpmin<=0:raise ArithmeticError('Exact common radial monotonicity failed')

    def angular(self,theta):
        cs=theta.c if isinstance(theta,Jet) else [theta]
        for previous,data in self.angular_cache:
            if len(previous)==len(cs) and all(a.shape==b.shape and np.array_equal(a.lo,b.lo) and np.array_equal(a.hi,b.hi) for a,b in zip(previous,cs)):
                self.cache_hits+=1;return data
        if isinstance(theta,Jet) and all(np.all(c.lo==0) and np.all(c.hi==0) for c in theta.c[1:]):
            raw=self.angular(theta.c[0])
            data={name:tuple(Jet.constant(v,theta.order) for v in value) if isinstance(value,tuple) else Jet.constant(value,theta.order) for name,value in raw.items()}
        else:
            u=self.central.u(theta);ratio=self.central.a/self.central.speed(theta)
            eu=base.expand(u);et=base.expand(theta)
            data={'u':u,'ratio':ratio,'unit':k.sincos(u),
              'source_planar':k.sincos(eu*self.pm),'source_height':k.sincos(eu*self.zm),
              'W_planar':k.sincos(et*self.wpm),'W_height':k.sincos(et*self.wzm)}
        self.angular_cache.append(([I(c.lo.copy(),c.hi.copy()) for c in cs],data));self.cache_misses+=1
        return data

    def vector(self,c,pm,zm,trig,derivative=0,negative=False):
        s,co=trig[0];ss,cc=trig[1];pp=base.take(c,slice(0,len(pm)));zz=base.take(c,slice(len(pm),None))
        if derivative:
            out=[base.reduce_sum(-pp*pm*s),base.reduce_sum(pp*pm*co),base.reduce_sum(-zz*zm*ss)]
        else:out=[base.reduce_sum(pp*co),base.reduce_sum(pp*s),base.reduce_sum(zz*cc)]
        if negative:out[2]=-out[2]
        return out

    def changes(self,z,theta):
        z,theta=lower_constant_jet(z),lower_constant_jet(theta)
        t=(self.T*z-self.S)/self.h;r=self.c-self.h*k.poly(self.R,t)
        kr=-self.T*k.poly(self.Rp,t);q=(r-self.rl)/(self.rr-self.rl);a=self.angular(theta)
        vv=k.poly(self.vp,base.expand(q));vr=k.poly(self.vrp,base.expand(q))
        source_trig=(a['source_planar'],a['source_height']);wtrig=(a['W_planar'],a['W_height'])
        Vr=self.vector(vr,self.pm,self.zm,source_trig,negative=True)
        Vu=self.vector(vv,self.pm,self.zm,source_trig,derivative=1,negative=True)
        wc=base.deboor(z,self.knots,self.wc,5,self.index)
        wd=base.deboor(z,self.knots[1:-1],self.wd,4,self.index-1)
        Wz=self.vector(wd,self.wpm,self.wzm,wtrig);Wt=self.vector(wc,self.wpm,self.wzm,wtrig,derivative=1)
        aa=[v+w/kr for v,w in zip(Vr,Wz)];bb=[v+a['ratio']*w for v,w in zip(Vu,Wt)]
        return r,a['u'],q,aa,bb

    def evaluate(self,z,theta):
        z,theta=lower_constant_jet(z),lower_constant_jet(theta)
        if getattr(self,'global_value_only',False) and (isinstance(z,Jet) or isinstance(theta,Jet)):
            raise ArithmeticError('Global background value interval cannot stand in for derivative jets')
        r,u,q,aa,bb=self.changes(z,theta);sn,cs=self.angular(theta)['unit']
        bq=(r-self.bg_rl)/(self.bg_rr-self.bg_rl);wp=k.poly(self.wpoly,bq)
        br=[cs,sn,-wp];bu=[-r*sn,r*cs,k.const_like(z,0)]
        return [2*base.dot(br,aa)+base.dot(aa,aa),base.dot(br,bb)+base.dot(aa,bu)+base.dot(aa,bb),2*base.dot(bu,bb)+base.dot(bb,bb)]

    def fit_background(self,rl,rr):
        self.bg_rl,self.bg_rr=rl,rr
        profile=self.bg.proposal_profile((rl+rr)/2)
        xp,x0,x1=self.bg.inverse_polynomial(profile,rl,rr)
        residual=self.bg.radial_residual(profile,xp,x0,x1,rl,rr)
        wp,rem=self.bg.slope_polynomial(profile,xp,x0,x1,8);route='original-analytic-order8'
        if len(wp)==1:
            # The original cap glues at t=0,1 to order four: J(t)=O(t^5),
            # and 1-J'(t)=(1-t)^4(1+4t+10t^2+20t^3).
            # Hence the already outward branch-hull jets through order four
            # bound true derivatives even on a crossing box. No claim is
            # made for derivatives five and above across that interface.
            m=self.bgmod;center=float((F(x0)+F(x1))/2)
            rrj=self.bg.source.evaluate(profile.n,profile.j,m.Jet.variable(m.I(x0,x1),4))
            ppj=self.bg.source.evaluate(profile.n,profile.j,m.Jet.variable(m.I(center),4))
            shifted=list(xp);shifted[0]=shifted[0]-m.I(center)
            wp=m.compose_poly(ppj['w'].c[:4],shifted)
            radius=max(abs(F(x0)-F(center)),abs(F(x1)-F(center)))
            rem=float((rrj['w'].c[4].abs()*m.qbounds(radius**4)).hi)
            route='original-globally-C4-cap-Taylor'
        self.wpoly=[I.bounds(base.fq(v.lo),base.fq(v.hi)) for v in wp]
        self.werror=I(base.fq(rem))+I(24)*base.fq(residual)
        return {'background_profile':[profile.n,profile.j],'background_polynomial_degree':len(wp)-1,
          'background_route':route,'background_radial_residual_upper':residual,
          'background_slope_error_upper_exact':str(k.exact(self.werror.hi))}

    def certify(self,row,angular,nr,na):
        self.rl,self.rr=F(row['left_exact']),F(row['right_exact'])
        self.vp=base.vector_power(row['V_controls']);self.vrp=base.vector_power(row['Vr_controls'])
        edges=[I(F(j,3*angular))*k.PI for j in range(angular+1)]
        angles=I(np.array([v.lo for v in edges[:-1]]),np.array([v.hi for v in edges[1:]]))
        pending=[(self.rl,self.rr,0)];accepted=[];attempts=[];target=F(1,500000000)
        while pending:
            rl,rr,depth=pending.pop();fitted_background=None
            low=self.inverse_r(rr);high=self.inverse_r(rl);zl,zh=k.exact(low.lo),k.exact(high.hi)
            cuts=[zl]+sorted(set(x for x in self.knots if zl<x<zh))+[zh];pieces=[];split=False
            for left,right in zip(cuts,cuts[1:]):
                self.index=bisect.bisect_right(self.knots,(left+right)/2)-1
                if self.index<5 or self.index>=len(self.wc):raise ValueError('Unexpected active W knot piece')
                z=I.bounds(left,right)
                # The original |w| <= 16/15 gives a true pointwise interval
                # enclosure even though w varies with r. This route uses
                # only I-valued expressions; never use it for any derivative.
                self.bg_rl,self.bg_rr=rl,rr;self.wpoly=[I.bounds(F(-16,15),F(16,15))]
                self.werror=I(0);self.global_value_only=True
                values=self.evaluate(z,angles)
                E=I(values[0].abs_upper());Fv=I(values[1].abs_upper())/rl;G=I(values[2].abs_upper())/(rl*rl)
                global_bound=k.exact(np.max(k.matrix_norm_bound(E,Fv,G)))
                self.global_value_only=False
                if global_bound<=target:
                    pieces.append({'unit_interval_exact':[str(left),str(right)],'W_knot_span':self.index,
                      'radius_branch_exact':[str(rl),str(rr)],'depth':depth,
                      'route':'global-background-complete-value-interval','metric_upper_exact':str(global_bound),
                      'background':{'global_slope_range_exact':['-16/15','16/15'],'value_intervals_only':True},
                      'background_error_E_upper_exact':'0','background_error_F_upper_exact':'0'})
                    continue
                if fitted_background is None:
                    background=self.fit_background(rl,rr)
                    fitted_background=(background,self.wpoly,self.werror)
                else:
                    background,self.wpoly,self.werror=fitted_background
                r,u,q,aa,bb=self.changes(z,angles)
                er=2*self.werror*I(aa[2].abs_upper());ef=self.werror*I(bb[2].abs_upper())
                background_loss=(er+ef/rl).hi
                if np.max(background_loss)>float(target)/8 and depth<self.args.max_radial_depth:
                    attempts.append({'depth':depth,'radius_exact':[str(rl),str(rr)],'reason':'background-uniform-budget','upper':str(k.exact(np.max(background_loss)))})
                    split=True;break
                values=self.evaluate(z,angles)
                E=I(values[0].abs_upper())+er;Fv=(I(values[1].abs_upper())+ef)/rl;G=I(values[2].abs_upper())/(rl*rl)
                U=k.matrix_norm_bound(E,Fv,G);route='complete-direct-interval';raw=None
                if np.max(U)>float(target):
                    raw=k.tensor_enclose(self.evaluate,z,angles,nr,na)
                    E=I(raw[0]['upper'])+er;Fv=(I(raw[1]['upper'])+ef)/rl;G=I(raw[2]['upper'])/(rl*rl)
                    U=k.matrix_norm_bound(E,Fv,G);route='complete-tensor-Chebyshev'
                bound=k.exact(np.max(U))
                if bound>target and depth<self.args.max_radial_depth:
                    attempts.append({'depth':depth,'radius_exact':[str(rl),str(rr)],'reason':'complete-Gram-work-budget','upper':str(bound)})
                    split=True;break
                piece={'unit_interval_exact':[str(left),str(right)],'W_knot_span':self.index,
                  'radius_branch_exact':[str(rl),str(rr)],'depth':depth,'route':route,
                  'metric_upper_exact':str(bound),'background':background,
                  'background_error_E_upper_exact':str(k.exact(np.max(er.hi))),
                  'background_error_F_upper_exact':str(k.exact(np.max(ef.hi)))}
                if raw is not None:
                    for name in ('upper','polynomial_upper','remainder_upper','radial_remainder_upper','angular_remainder_upper','node_width_max'):
                        piece[name]=[str(k.exact(np.max(v[name]))) for v in raw]
                pieces.append(piece)
            if split:
                middle=(rl+rr)/2;pending.extend([(middle,rr,depth+1),(rl,middle,depth+1)])
            else:accepted.extend(pieces)
        return {'source_span':row['source_span'],'source_radius_exact':[str(self.rl),str(self.rr)],
          'pieces':accepted,'attempt_history':attempts,'metric_upper_exact':str(max(F(v['metric_upper_exact']) for v in accepted)),
          'whole_original_source_cell_and_all_angles_covered':True,
          'original_background_cap_C4_used_only_for_uniform_value_remainder':True}

def original_cells(args,meta,coverage):
    helper=load('stream_tail_exact_polynomial_source',args.scripts/'6a65-m12-tail-polynomial-continuous-bounds-recovered.py')
    producer=load('stream_tail_original_blob_definition',args.scripts/'6a65-m12-stream-tail-exact-endpoint.py')
    C=meta['format']['coefficientCount'];radial=meta['radialGeometry'];beta=F(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
    S1=[F(0)]*C;S2=[F(0)]*C;first=None;previous=None;r=F(radial['innerAnchor']);count=0
    for block,info in enumerate(meta['files']):
        name=Path(info['path']).name;raw=(args.raw_cache/name).read_bytes()
        key=name.split('-raw')[1].split('.f64')[0].replace('-part','-');blob=producer.BLOBS[key]
        if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=info['sha256'] or hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:
            raise ValueError('Original raw source identity changed '+name)
        data=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
        if not np.all(np.isfinite(data)) or (previous is not None and not np.array_equal(data[0],previous)):
            raise ValueError('Original finite source seam or values changed')
        vals=data[:,2:2+4*C].reshape(len(data),4,C)
        if first is None:first=[base.fq(x) for x in vals[0,0]]
        for i in range(len(data)-1):
            ell=base.fq(data[i+1,-1]);L=beta*ell
            if L<=0:raise ValueError('Original radial increment is not positive')
            wanted=args.span_start<=count<args.span_stop
            row={'source_span':count,'left_exact':str(r),'right_exact':str(r+L),'V_controls':[],'Vr_controls':[]}
            # Beyond the last requested cell, the accumulated coefficient
            # state is never consumed. Still inspect every original blob,
            # seam, positive radial increment and final exact outer anchor.
            for j in range(C) if count<args.span_stop else ():
                f0,f1=base.fq(vals[i,1,j]),base.fq(vals[i+1,1,j]);s0,s1=base.fq(vals[i,2,j]),base.fq(vals[i+1,2,j]);mid=base.fq(vals[i+1,3,j])
                if wanted:
                    value=first[j]+beta*S1[j]/30+beta*beta*S2[j]/60
                    vv,vr,_=helper.span_controls(value,f0,f1,s0,s1,mid,L)
                    row['V_controls'].append(vv);row['Vr_controls'].append(vr)
                S1[j]+=ell*(7*(f0+f1)+16*mid);S2[j]+=ell*ell*(s0-s1)
            r+=L;count+=1
            if wanted:yield row
        previous=data[-1].copy();coverage.append({'file':name,'sha256':info['sha256'],'git_blob':blob,'spans_through':count})
    if r!=F(radial['outerAnchor']):raise ArithmeticError('Exact original spans do not reach outer anchor')
    if count!=18552:raise ArithmeticError('Original finite source span count changed')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','data','grid','field','result','correction-bounds','primitive','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--raw-cache',type=Path);p.add_argument('--source-polynomials',type=Path)
    p.add_argument('--span-start',type=int,default=0);p.add_argument('--span-stop',type=int,default=18552)
    p.add_argument('--angular',type=int,default=32);p.add_argument('--radial-order',type=int,default=6);p.add_argument('--angular-order',type=int,default=8)
    p.add_argument('--max-radial-depth',type=int,default=12)
    a=p.parse_args();start=time.monotonic()
    if not 0<=a.span_start<a.span_stop<=18552:raise ValueError('Invalid original source cell range')
    if a.out.exists():raise FileExistsError('Fresh complete correlated tail output required')
    manifest=a.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    if sha(manifest)!='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104':raise ValueError('Original manifest changed')
    meta=json.loads(manifest.read_text());coverage=[]
    if a.source_polynomials:
        source=json.loads(a.source_polynomials.read_text());iterator=iter(source['selected_spans'])
    else:
        if a.raw_cache is None:raise ValueError('Original local raw blobs required')
        source={'manifest_sha256':sha(manifest),'planar_modes':meta['format']['planarModes'],'height_modes':meta['format']['heightModes'],
          'integrated_value_from_exact_original_cumulative_sums':True,'exact_all_source_nodes_and_normalization_checked':True}
        iterator=original_cells(a,meta,coverage)
    consumer=CachedTail(a,source);rows=[];U=F(0);rowpath=Path(str(a.out)+'.rows.jsonl')
    if rowpath.exists():raise FileExistsError('Fresh exact row stream required')
    with rowpath.open('w') as stream:
        for row in iterator:
            then=time.monotonic();cert=consumer.certify(row,a.angular,a.radial_order,a.angular_order)
            bound=F(cert['metric_upper_exact']);U=max(U,bound)
            stream.write(json.dumps(cert,allow_nan=False)+'\n');stream.flush()
            rows.append({'source_span':row['source_span'],'metric_upper_exact':str(bound),'pieces':len(cert['pieces'])})
            print(json.dumps({'completed':len(rows),'source_span':row['source_span'],'cell_seconds':time.monotonic()-then,'maximum':float(U),'current':float(bound),'angular_cache_misses':consumer.cache_misses,'angular_cache_hits':consumer.cache_hits,'seconds':time.monotonic()-start}),flush=True)
    full=(not a.source_polynomials and a.span_start==0 and a.span_stop==18552 and len(rows)==18552 and len(coverage)==24)
    out={'schema':'2ecf-original-M12-correlated-tail-adaptive-exact-stream-v3','script_sha256':sha(__file__),
      'adaptive_parent_source_sha256':ADAPTIVE_PARENT_SHA,'global_background_interval_used_for_values_only':True,
      'original_stream_source_sha256':ORIGINAL_STREAM_SHA,'exact_zero_Jet_coefficients_lowered_to_constant_intervals':True,'unused_central_second_trace_parameter_normalized':True,'max_radial_depth':a.max_radial_depth,'frozen_first_consumer_sha256':sha(base.__file__),'frozen_interval_sha256':sha(k.__file__),
      'inputs':{name:sha(getattr(a,name)) for name in ('data','grid','field','result','correction_bounds','primitive')},
      'source_polynomials_sha256':sha(a.source_polynomials) if a.source_polynomials else None,'manifest_sha256':sha(manifest),
      'all_original_raw_blobs_verified':coverage,'all_original_finite_tail_spans_covered':full,
      'all_angles_by_original_D3_and_reflection':True,'fundamental_angle_interval':'[0,pi/3]',
      'angular_boxes':a.angular,'radial_order':a.radial_order,'angular_order':a.angular_order,
      'angular_cache_exact_interval_input_comparison':True,'angular_cache_misses':consumer.cache_misses,'angular_cache_hits':consumer.cache_hits,
      'row_stream_sha256':sha(rowpath),'row_stream_path':rowpath.name,'covered_source_spans':[x['source_span'] for x in rows],
      'metric_upper_exact':str(U),'metric_upper_display':float(U),'below_original_solver_tolerance':U<=F(1,500000000),
      'whole_surface_claim':False,'fixed_cuff_gap_and_prefix_not_in_this_receipt':True,'seconds':time.monotonic()-start}
    a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps({'report':str(a.out),'sha256':sha(a.out),'bound':float(U),'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
