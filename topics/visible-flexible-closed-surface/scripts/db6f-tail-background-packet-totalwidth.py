#!/usr/bin/env python3
"""Certified w(r), w_r(r) polynomial packets for an exact finite-tail grid.

An approximate cubic inverse is only a proposal. Its true radial residual
is enclosed by the validated source primitive, then multiplied by the
reviewed global bound |w_r|<24. A direct forward-bracketed inverse box
encloses w_r on outer profiles. Inner profiles may use the independent
global cap and curvature bounds. No floating inverse is trusted as exact.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import time
import numpy as np

from db6f_tail_interval_elementary import I, qbounds
from db6f_tail_interval_source import FrozenSource, Jet
from db6f_tail_interval_source_stable import FrozenSource as StableSource
from db6f_tail_background_primitive import ProfilePrimitive, from_pair, poly_value
from db6f_tail_integrated import IntegratedTail


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def add_poly(a,b):
    size=max(len(a),len(b))
    return [(a[k] if k<len(a) else I(0))+(b[k] if k<len(b) else I(0)) for k in range(size)]


def mul_poly(a,b):
    out=[I(0) for _ in range(len(a)+len(b)-1)]
    for j,v in enumerate(a):
        for k,w in enumerate(b):out[j+k]=out[j+k]+v*w
    return out


def compose_poly(a,b):
    out=[I(0)]
    for v in a[::-1]:
        out=mul_poly(out,b);out[0]=out[0]+v
    # Remove only the structurally added leading zero, not small values.
    return out[:1+(len(a)-1)*(len(b)-1)]


def bernstein_range(a):
    degree=len(a)-1
    low,high=math.inf,-math.inf
    for k in range(degree+1):
        value=I(0)
        for j in range(k+1):
            value=value+a[j]*qbounds(Q(math.comb(k,j),math.comb(degree,j)))
        low=min(low,float(value.lo));high=max(high,float(value.hi))
    return I(low,high)


def truncate_polynomial(poly,remainder,degree):
    """On 0<=tau<=1, discarded coefficient l1 bounds the omitted tail."""
    extra=I(0)
    for coefficient in poly[degree+1:]:extra=extra+coefficient.abs()
    return poly[:degree+1],float((I(remainder)+extra).hi)


def write_npz(stem,arrays):
    buffer=io.BytesIO();np.savez_compressed(buffer,**arrays);payload=buffer.getvalue()
    if len(payload)>1000000:
        payload=gzip.compress(payload,mtime=0);path=Path(str(stem)+'.npz.gz')
    else:path=Path(str(stem)+'.npz')
    if len(payload)>=5000000:raise ValueError('compressed packet exceeds per-file limit')
    path.write_bytes(payload)
    return path


def exact_nodes(t):
    if t.unscaled_lengths is None:
        return [Q(float(x)) for x in t.r_display]
    radial=t.meta['radialGeometry']
    out=[Q(radial['innerAnchor'])]
    for ell in t.unscaled_lengths:
        if not ell>0:raise ValueError('nonpositive exact radial increment')
        out.append(out[-1]+t.radial_scale*Q(float(ell)))
    if out[-1]!=Q(radial['outerAnchor']):
        raise ValueError('sum of exact scaled increments does not reach the outer anchor')
    return out


class Background:
    def __init__(self, primitive, calibrations):
        self.data=read(primitive)
        if not self.data.get('finished'):raise ValueError('partial radial primitive')
        if sha(calibrations)!=self.data['inputs']['calibrations']['sha256']:
            raise ValueError('primitive calibration table hash mismatch')
        for name in ['db6f_tail_background_primitive.py','db6f_tail_interval_source.py',
                     'db6f_tail_interval_elementary.py','db6f-audit-continuous-hermite.py']:
            if sha(Path(__file__).with_name(name))!=self.data['sources'][name]:
                raise ValueError('primitive implementation changed: '+name)
        self.p=self.data['parameters']
        self.alpha=I(*self.data['alpha'])
        if self.data.get('sourceModelModule')=='db6f_tail_interval_source_stable.py':
            if sha(Path(__file__).with_name('db6f_tail_interval_source_stable.py'))!=self.data['sources']['db6f_tail_interval_source_stable.py']:
                raise ValueError('stable source implementation changed')
            self.source=StableSource(self.p,read(calibrations))
        else:
            self.source=FrozenSource(self.p,read(calibrations))
        self.profiles=[ProfilePrimitive(x) for x in self.data['profiles']]
        self.profiles.sort(key=lambda x:sum(x.anchors['left']))
        self.lowest=min(x.anchors['left'][0] for x in self.profiles)
        self.covered={(x.n,x.j) for x in self.profiles}
        expected={(n,j) for n in range(self.data['settings']['depth']) for j in range(9)}
        self.complete_source=self.covered==expected
        thresholds=[x.anchors['left'][0] for x in self.profiles if x.n==0 and x.j==0]
        thresholds += [x.anchors['right'][0] for x in self.profiles if x.n==1 and x.j==8]
        self.inner_threshold=max(thresholds) if thresholds else None

    def candidates(self,rl,rr):
        return [x for x in self.profiles if Q(x.anchors['left'][0])<=rr and Q(x.anchors['right'][1])>=rl]

    def proposal_profile(self,mid):
        choices=self.candidates(mid,mid)
        if choices:return min(choices,key=lambda x:abs(sum(x.anchors['left'])+sum(x.anchors['right'])-4*float(mid)))
        return min(self.profiles,key=lambda x:min(abs(float(mid)-sum(x.anchors[k])/2) for k in ['left','right']))

    def inverse_polynomial(self,profile,rl,rr):
        x0=profile.approximate_inverse(float(rl));x1=profile.approximate_inverse(float(rr))
        if x1<x0:raise ArithmeticError('approximate inverse endpoints reversed')
        value=self.source.evaluate(profile.n,profile.j,Jet.variable(I(np.array([x0,x1])),0))
        rx=value['A'].c[0]+value['B'].c[0]*self.alpha
        rxmid=(rx.lo+rx.hi)/2
        width=float(rr-rl)
        if np.all(rxmid>0) and np.all(np.isfinite(rxmid)):
            c1=min(x1,max(x0,x0+width/(3*rxmid[0])))
            c2=min(x1,max(x0,x1-width/(3*rxmid[1])))
        else:c1,c2=x0,x1
        if c1>c2:
            c1=x0+(x1-x0)/3;c2=x0+2*(x1-x0)/3
        controls=list(map(Q,[x0,c1,c2,x1]))
        a,b,c,d=controls
        if not Q(0)<=a<=b<=c<=d<=Q(1):
            raise ArithmeticError('inverse Bezier controls leave the ordered source interval')
        exact=[a,3*(b-a),3*(c-2*b+a),d-3*c+3*b-a]
        return [qbounds(z) for z in exact],x0,x1

    def radial_residual(self,profile,xpoly,x0,x1,rl,rr):
        first=profile.leaf_index(x0);last=profile.leaf_index(x1)
        # Monotonicity is an independent, always valid fallback. It avoids
        # composing thousands of tiny leaves near one |w_x| branch point.
        left=profile.point(x0);right=profile.point(x1)
        monotone=max(abs(Q(float(left.lo))-rr),abs(Q(float(right.hi))-rl))
        monotone_bound=float(qbounds(monotone).hi)
        if last-first>64:return monotone_bound
        bound=0.
        for leaf in profile.leaves[first:last+1]:
            shifted=list(xpoly);shifted[0]=shifted[0]-I(leaf['center'])
            cc=[from_pair(v) for v in leaf['polynomial']]
            polynomial=compose_poly(cc,shifted)
            polynomial[0]=(polynomial[0]+from_pair(leaf['radiusAtLeft'])
                           -from_pair(leaf['polynomialAtLeft'])-qbounds(rl))
            if len(polynomial)<2:polynomial.append(I(0))
            polynomial[1]=polynomial[1]-qbounds(rr-rl)
            residual=bernstein_range(polynomial).abs()+I(leaf['primitiveRemainder'])
            bound=max(bound,float(residual.hi))
        return min(bound,monotone_bound)

    def slope_polynomial(self,profile,xpoly,x0,x1,order):
        center=float((Q(x0)+Q(x1))/2)
        rr=self.source.evaluate(profile.n,profile.j,Jet.variable(I(x0,x1),order))
        pp=self.source.evaluate(profile.n,profile.j,Jet.variable(I(center),order))
        if not bool(rr['validB']) or not bool(pp['validB']):
            # A range is a valid degree-zero polynomial enclosure.
            return [rr['w'].c[0]],0.
        shifted=list(xpoly);shifted[0]=shifted[0]-I(center)
        poly=compose_poly(pp['w'].c[:order],shifted)
        radius=max(abs(Q(x0)-Q(center)),abs(Q(x1)-Q(center)))
        remainder=rr['w'].c[order].abs()*qbounds(radius**order)
        return poly,float(remainder.hi)

    def derivative_range(self,rl,rr):
        if self.inner_threshold is not None and rr<=Q(self.inner_threshold):
            return I(-6.01,6.01)
        if not self.complete_source and not any(rl>=Q(x.anchors['left'][1]) and rr<=Q(x.anchors['right'][0]) for x in self.profiles):
            return I(-24,24)
        candidates=self.candidates(rl,rr)
        if not candidates:
            return I(-24,24)
        lo,hi=math.inf,-math.inf
        for profile in candidates:
            xr=profile.inverse_cover(rl,rr)
            value=self.source.evaluate(profile.n,profile.j,Jet.variable(xr,0))
            rx=value['A'].c[0]+value['B'].c[0]*self.alpha
            if float(rx.lo)<=0:
                piece=I(-24,24)
            else:
                raw=value['wd'].c[0]/rx
                piece=I(max(-24.,float(raw.lo)),min(24.,float(raw.hi)))
            lo=min(lo,float(piece.lo));hi=max(hi,float(piece.hi))
        # At a truncated table boundary a missing inner profile is harmless
        # only under the independently proved inner cap/curvature estimate.
        if rl<Q(self.lowest):lo=min(lo,-24.);hi=max(hi,24.)
        return I(lo,hi)

    def derivative_polynomial(self,profile,xpoly,x0,x1,rl,rr,radial_error,order):
        """Taylor q=dw/dr only on one certified analytic source branch.

        Let x_true be the exact inverse and x_app the cubic proposal. On
        their source-coordinate convex hull, r_x >= m > 0 implies
        |x_true-x_app| <= radial_error/m. The local bound on |q_x| then
        transports the source Taylor polynomial to the true physical r.
        Across source/cap/absolute-value interfaces, use the proven range.
        """
        fallback=lambda:([self.derivative_range(rl,rr)],0.)
        if self.inner_threshold is not None and rr<=Q(self.inner_threshold):
            return [I(-6.01,6.01)],0.
        if rl<Q(profile.anchors['left'][1]) or rr>Q(profile.anchors['right'][0]):
            return fallback()
        if profile.n>=1:return [I(-6.01,6.01)],0.
        inverse=profile.inverse_cover(rl,rr)
        xl=min(x0,float(inverse.lo));xh=max(x1,float(inverse.hi))
        cover=self.source.evaluate(profile.n,profile.j,Jet.variable(I(xl,xh),1))
        if not bool(cover['validA']) or not bool(cover['validB']):return fallback()
        cover_rx=cover['A']+cover['B']*self.alpha
        lower=float(cover_rx.c[0].lo)
        if lower<=0:return fallback()
        cover_q=cover['wd']/cover_rx
        derivative=cover_q.c[1].abs()
        center=float((Q(x0)+Q(x1))/2)
        rr_source=self.source.evaluate(profile.n,profile.j,Jet.variable(I(x0,x1),order))
        point=self.source.evaluate(profile.n,profile.j,Jet.variable(I(center),order))
        if not bool(rr_source['validA']) or not bool(rr_source['validB']) or not bool(point['validA']) or not bool(point['validB']):
            return fallback()
        range_rx=rr_source['A']+rr_source['B']*self.alpha
        point_rx=point['A']+point['B']*self.alpha
        if float(range_rx.c[0].lo)<=0 or float(point_rx.c[0].lo)<=0:return fallback()
        range_q=rr_source['wd']/range_rx;point_q=point['wd']/point_rx
        shifted=list(xpoly);shifted[0]=shifted[0]-I(center)
        poly=compose_poly(point_q.c[:order],shifted)
        radius=max(abs(Q(x0)-Q(center)),abs(Q(x1)-Q(center)))
        taylor=range_q.c[order].abs()*qbounds(radius**order)
        phase=derivative*I(radial_error)/I(lower)
        return poly,float((taylor+phase).hi)


def polynomial_uncertainty(poly, remainder):
    """Conservative bound using full coefficient widths, not half widths.

    This only chooses an audit subdivision. Every retained interval and
    remainder is unchanged and must still be consumed by the verifier.
    """
    total = I(remainder)
    for value in poly:
        total = total + (I(value.hi) - I(value.lo))
    return float(total.hi)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--primitive',type=Path,required=True)
    ap.add_argument('--calibrations',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--order',type=int,default=8)
    ap.add_argument('--output-degree',type=int,default=8)
    ap.add_argument('--radial-residual',type=float,default=1e-8)
    ap.add_argument('--w-width',type=float,default=2e-7)
    ap.add_argument('--wr-width',type=float,default=.08)
    ap.add_argument('--max-depth',type=int,default=22)
    ap.add_argument('--span-start',type=int,default=0)
    ap.add_argument('--span-stop',type=int)
    ap.add_argument('--rows-per-shard',type=int,default=5000)
    args=ap.parse_args()
    if args.order<2 or args.order%2 or not 0<=args.max_depth<=48 or args.rows_per_shard<=0 or args.output_degree<0:
        raise ValueError('invalid packet settings')
    t=IntegratedTail(args.manifest);nodes=exact_nodes(t)
    bg=Background(args.primitive,args.calibrations)
    gkeys=['rCut','rCuff','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation',
           'prefixR','prefixEnd','prefixReturnStart','protectCell','slopeCap','capTransition','capMode',
           'valleyControls','pulseCaps','valleyCaps','warpWeightLevels','prefixRByCell']
    if any(t.meta['parameters'].get(k)!=bg.p.get(k) for k in gkeys):
        raise ValueError('packet target background differs from the manifest')
    expected={(n,j) for n in range(bg.data['settings']['depth']) for j in range(9)}
    complete_source=bg.covered==expected
    stop=len(nodes)-1 if args.span_stop is None else args.span_stop
    if not 0<=args.span_start<stop<=len(nodes)-1:raise ValueError('invalid span selection')
    full_selection=args.span_start==0 and stop==len(nodes)-1
    if full_selection and not complete_source:raise ValueError('a full packet requires complete outer source cells')
    if nodes[0]<=Q(bg.p['rCuff']) or nodes[-1]>Q(bg.p['rCut']):
        raise ValueError('finite radii lie outside the exact background domain')
    if full_selection and (bg.inner_threshold is None or nodes[0]>Q(bg.inner_threshold)):
        raise ValueError('collar cap bound lacks a certified inner-domain threshold')
    degree=args.output_degree
    report={'status':'validated-background-packet-pending-independent-review','scope':__doc__,
            'finite_tail_manifest_sha256':sha(args.manifest),'finite_tail_manifest':str(args.manifest),
            'primitive_file':str(args.primitive),'primitive_sha256':sha(args.primitive),
            'background_definition_hashes':bg.data['inputs'],
            'source_hashes':{name:sha(Path(__file__).with_name(name)) for name in [Path(__file__).name,'db6f_tail_background_primitive.py','db6f_tail_interval_source.py','db6f_tail_interval_source_stable.py','db6f_tail_interval_elementary.py','db6f_tail_integrated.py']},
            'settings':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'basis':'power coefficients in tau=(u-u_left)/(u_right-u_left), all saved binaries exact enclosure endpoints',
            'coefficient_degree':degree,'span_count':len(nodes)-1,'span_selection':[args.span_start,stop],
            'files':[],'finished':False,'rows':0,'unmet_tolerance_rows':0,
            'maximum_radial_residual':0.,'maximum_w_remainder':0.,'maximum_outer_wr_uncertainty':0.,
            'maximum_wr_remainder':0.,'maximum_w_total_uncertainty':0.,
            'w_working_tolerance_criterion':'remainder plus outward sum of full coefficient widths; coarse dispatch rows are exempt and require the actual metric verifier',
            'exact_radial_anchor_invariant':True,'background_curvature_bound':6,
            'global_background_wr_absolute_bound':24,
            'notes':['No source inverse is assumed exact.','The independent backend must include w_remainder and wr_remainder.',
                     'Coarse inner w/wr boxes use separately reviewed cap/curvature proofs; they are not tight inverse results.']}
    buffer=[];started=time.time()

    def save_rows():
        if not buffer:return
        rows=len(buffer);part=len(report['files'])
        arrays={}
        for name in ['span_index','u_left','u_right','w_remainder','wr_remainder','source_cell','source_segment','radial_residual']:
            arrays[name]=np.array([x[name] for x in buffer],dtype=np.int64 if name in ['span_index','source_cell','source_segment'] else np.float64)
        for name in ['w_lo','w_hi','wr_lo','wr_hi']:
            arrays[name]=np.stack([x[name] for x in buffer])
        path=write_npz(str(args.out_prefix)+f'-part{part:03d}',arrays)
        report['files'].append({'data_file':str(path),'sha256':sha(path),'rows':rows,'bytes':path.stat().st_size})
        buffer.clear()
        Path(str(args.out_prefix)+'.json').write_text(json.dumps(report,indent=2)+'\n')

    def record(index,ul,ur,poly,rem,wrpoly,wrrem,profile,residual,unmet=False):
        wlo=np.zeros(degree+1);whi=np.zeros(degree+1)
        for k,v in enumerate(poly):wlo[k]=float(v.lo);whi[k]=float(v.hi)
        wrlo=np.zeros(degree+1);wrhi=np.zeros(degree+1)
        for k,v in enumerate(wrpoly):wrlo[k]=float(v.lo);wrhi[k]=float(v.hi)
        if not all(np.all(np.isfinite(a)) for a in [wlo,whi,wrlo,wrhi]) or not np.all(wlo<=whi) or not np.all(wrlo<=wrhi):
            raise ArithmeticError('nonfinite or reversed background packet')
        buffer.append({'span_index':index,'u_left':ul,'u_right':ur,'w_lo':wlo,'w_hi':whi,
                       'w_remainder':rem,'wr_lo':wrlo,'wr_hi':wrhi,'wr_remainder':wrrem,
                       'source_cell':profile.n if profile else -1,'source_segment':profile.j if profile else -1,
                       'radial_residual':residual})
        report['rows']+=1;report['unmet_tolerance_rows']+=int(unmet)
        report['maximum_radial_residual']=max(report['maximum_radial_residual'],residual)
        report['maximum_w_remainder']=max(report['maximum_w_remainder'],rem)
        report['maximum_w_total_uncertainty']=max(report['maximum_w_total_uncertainty'],polynomial_uncertainty(poly,rem))
        report['maximum_wr_remainder']=max(report['maximum_wr_remainder'],wrrem)
        if profile is not None and profile.n==0:
            report['maximum_outer_wr_uncertainty']=max(report['maximum_outer_wr_uncertainty'],float(np.sum(wrhi-wrlo))+2*wrrem)
        if len(buffer)>=args.rows_per_shard:save_rows()

    if full_selection:
        record(-1,0.,1.,[I(0,float(qbounds(Q(1,49)).hi))],0.,[I(-6.01,6.01)],0.,None,0.)
    for index in range(args.span_start,stop):
        r0,L=nodes[index],nodes[index+1]-nodes[index]
        if complete_source and nodes[index+1]<=Q(bg.lowest):
            record(index,0.,1.,[I(0,float(qbounds(Q(1,49)).hi))],0.,[I(-6.01,6.01)],0.,None,0.)
            continue
        pending=[(0.,1.,0)]
        while pending:
            ul,ur,level=pending.pop()
            rl,rr=r0+L*Q(ul),r0+L*Q(ur)
            # A physical span can cross the uncertain inner edge of the
            # primitive table. Its lower children belong to the already
            # proved coarse inner domain and must be treated there; merely
            # clamping their inverse to x=0 would never reduce the residual.
            if complete_source and rr<=Q(bg.lowest):
                record(index,ul,ur,[I(0,float(qbounds(Q(1,49)).hi))],0.,[I(-6.01,6.01)],0.,None,0.)
                continue
            profile=bg.proposal_profile((rl+rr)/2)
            xpoly,x0,x1=bg.inverse_polynomial(profile,rl,rr)
            residual=bg.radial_residual(profile,xpoly,x0,x1,rl,rr)
            poly,taylor_error=bg.slope_polynomial(profile,xpoly,x0,x1,args.order)
            remainder=float((I(taylor_error)+I(residual)*24).hi)
            wrpoly,wrrem=bg.derivative_polynomial(profile,xpoly,x0,x1,rl,rr,residual,args.order)
            poly,remainder=truncate_polynomial(poly,remainder,degree)
            wrpoly,wrrem=truncate_polynomial(wrpoly,wrrem,degree)
            # Include interval coefficient widths at every degree. This is a
            # working subdivision criterion, never an error certificate.
            w_uncertainty=polynomial_uncertainty(poly,remainder)
            wr_width=sum(float(v.hi-v.lo) for v in wrpoly)+2*wrrem if profile.n==0 else 0.
            okay=(residual<=args.radial_residual and w_uncertainty<=args.w_width and wr_width<=args.wr_width)
            if okay or level>=args.max_depth:
                record(index,ul,ur,poly,remainder,wrpoly,wrrem,profile,residual,not okay)
            else:
                mid=(ul+ur)/2
                pending.extend([(mid,ur,level+1),(ul,mid,level+1)])
        if index%16==0:
            print(json.dumps({'span':index,'rows':report['rows'],'seconds':time.time()-started}),flush=True)
    save_rows()
    # The independent consumer currently accepts one NPZ. Merge only when
    # the compressed result obeys the explicit per-file limit; otherwise
    # retain the already bounded shards and require a shard-aware consumer.
    def load_shard(path):
        raw=Path(path).read_bytes()
        if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
        return np.load(io.BytesIO(raw),allow_pickle=False)
    loaded=[load_shard(item['data_file']) for item in report['files']]
    arrays={key:np.concatenate([item[key] for item in loaded],axis=0) for key in loaded[0].files}
    try:
        path=write_npz(str(args.out_prefix),arrays)
        report['data_file']=path.name;report['data_sha256']=sha(path)
    except ValueError:
        report['requires_shard_consumer']=True
    for item in loaded:item.close()
    report['finished']=True;report['seconds']=time.time()-started
    Path(str(args.out_prefix)+'.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['finished','rows','seconds','unmet_tolerance_rows','maximum_radial_residual','maximum_w_remainder','maximum_w_total_uncertainty','maximum_wr_remainder','maximum_outer_wr_uncertainty']}))


if __name__=='__main__':main()
