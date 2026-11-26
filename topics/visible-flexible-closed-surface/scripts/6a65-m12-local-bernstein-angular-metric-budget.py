#!/usr/bin/env python3
"""Continuous, localized metric budget for one saved original-M12 field.

This independent successor to R226 reads the actual saved coefficients.
It extracts exact Bernstein pieces, retains Fourier cancellation in squared
vector norms, and uses the exact central speed instead of a global inverse
angle factor. It still proves a sufficient metric transfer bound; it does
not assert an exact isometry or infer a result for an unavailable old field.
"""
from __future__ import annotations
import argparse,bisect,gzip,hashlib,importlib.util,io,json,math,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

BITS=96; SCALE=1<<BITS
DATA_SHA='359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0'
META_SHA='253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'
BRIDGE_SHA='1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa'
MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
R226_SHA='81003432a6823b3c86859be226c9a099012ed7fa21e46165ac12091d86727e80'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def ceildiv(a,b):return -((-a)//b)
def ceilfp(q):q=Q(q);return ceildiv(q.numerator*SCALE,q.denominator)
def floorfp(q):q=Q(q);return q.numerator*SCALE//q.denominator
def up(q):return Q(ceilfp(q),SCALE)
def load(name,p):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def summary(q):return {'upper_exact':str(up(q)),'display':float(up(q))}


def insert_knot(knots,controls,p,u):
    """One exact Boehm insertion, with the original spline unchanged."""
    k=bisect.bisect_right(knots,u)-1;s=knots.count(u);n=len(controls)-1
    if not 0<=s<p:raise ValueError('Invalid interior knot multiplicity')
    out=[None]*(n+2)
    for i in range(k-p+1):out[i]=controls[i]
    for i in range(k-s,n+1):out[i+1]=controls[i]
    for i in range(k-p+1,k-s+1):
        den=knots[i+p]-knots[i]
        if den<=0:raise ArithmeticError('Degenerate active knot support')
        a=(u-knots[i])/den
        out[i]=[a*v+(1-a)*w for v,w in zip(controls[i],controls[i-1])]
    if any(row is None for row in out):raise ArithmeticError('Incomplete exact insertion')
    return knots[:k+1]+[u]+knots[k+1:],out


def extract_bezier(knots,coeff,p=5):
    na=len(coeff[0]);zero=[Q(0)]*na
    controls=[zero.copy() for _ in range(3)]+coeff+[zero.copy() for _ in range(3)]
    if len(controls)!=len(knots)-p-1:raise ValueError('Wrong full zero-trace coefficient count')
    mesh=sorted(set(knots))
    if mesh[0]!=0 or mesh[-1]!=1 or knots[:6]!=[Q(0)]*6 or knots[-6:]!=[Q(1)]*6:
        raise ValueError('Expected the full clamped original-M12 domain')
    for u in mesh[1:-1]:
        for _ in range(p-knots.count(u)):knots,controls=insert_knot(knots,controls,p,u)
    if len(controls)!=p*(len(mesh)-1)+1:raise ArithmeticError('Wrong Bernstein extraction count')
    return [(a,b,controls[p*i:p*i+p+1]) for i,(a,b) in enumerate(zip(mesh[:-1],mesh[1:]))]


def split_bezier(c):
    rows=[c];left=[c[0]];right=[c[-1]]
    while len(rows[-1])>1:
        row=[[(a+b)/2 for a,b in zip(x,y)] for x,y in zip(rows[-1][:-1],rows[-1][1:])]
        rows.append(row);left.append(row[0]);right.append(row[-1])
    return left,right[::-1]


def elevated_derivative(c,width):
    d=[[5*(b-a)/width for a,b in zip(x,y)] for x,y in zip(c[:-1],c[1:])]
    out=[d[0]]
    for i in range(1,5):out.append([Q(i,5)*a+Q(5-i,5)*b for a,b in zip(d[i-1],d[i])])
    return out+[d[-1]]


def rounded_coefficients(row):
    out=[];errors=[]
    for v in row:
        n=floorfp(v);out.append(n);errors.append(abs(v-Q(n,SCALE)))
    return out,errors


def norm_cosine_integers(row,pm,zm,angular_order):
    """Exact cosine coefficients of the rounded vector's squared norm.

    Result frequencies are in x=3*theta. Its common denominator is
    (2*SCALE)^2. Complex planar and real cosine height modes are both kept.
    """
    P=len(pm);terms=[[(int(m),2*int(c)*int(m)**angular_order) for c,m in zip(row[:P],pm)]]
    height=[]
    for c,m in zip(row[P:],zm):
        m=int(m);c=int(c)
        if m==0:height.append((0,2*c if angular_order==0 else 0))
        else:height.extend(((m,c*m**angular_order),(-m,c*(-m)**angular_order)))
    terms.append(height);out={}
    for values in terms:
        values=sorted((m,c) for m,c in values if c)
        out[0]=out.get(0,0)+sum(c*c for _,c in values)
        for i,(m,a) in enumerate(values):
            for n,b in values[i+1:]:
                if (n-m)%3:raise ValueError('Lost the actual D3 Fourier symmetry')
                k=(n-m)//3;out[k]=out.get(k,0)+2*a*b
    return {k:v for k,v in out.items() if v}


class AngularBoxes:
    """Integer Taylor enclosures of an exact cosine polynomial on [0,pi]."""
    def __init__(self,cert,cells=128,degree=8,max_mode=None):
        if cells<8 or degree<2:raise ValueError('Insufficient angular enclosure parameters')
        self.cells,self.degree=cells,degree;self.cert=cert;self.pi=cert.pi_interval();self.max_mode=max_mode
        delta=self.pi.upper()/Q(2*cells)
        self.weights=[ceilfp(delta**j/Q(math.factorial(j))) for j in range(degree+1)]
        self.trig=[]
        for j in range(4*cells):
            r=j if j<=2*cells else j-4*cells
            sn,cs=cert.sincos(self.pi*Q(r,2*cells));self.trig.append((sn.lo,sn.hi,cs.lo,cs.hi))
        self.cache={}

    def kernels(self,modes):
        key=tuple(modes)
        if key in self.cache:return self.cache[key]
        rows=[]
        for cell in range(self.cells):
            derivatives=[]
            for d in range(self.degree):
                terms=[]
                for m in modes:
                    snlo,snhi,cslo,cshi=self.trig[(m*(2*cell+1))%(4*self.cells)]
                    if d%4==0:lo,hi=cslo,cshi
                    elif d%4==1:lo,hi=-snhi,-snlo
                    elif d%4==2:lo,hi=-cshi,-cslo
                    else:lo,hi=snlo,snhi
                    k=m**d;terms.append((lo*k,hi*k))
                derivatives.append(terms)
            rows.append(derivatives)
        self.cache[key]=rows;return rows

    def enclose(self,cosine,denominator):
        if self.max_mode is not None:
            if max(cosine,default=0)>self.max_mode:raise ValueError('Angular polynomial exceeds the frozen enclosure basis')
            modes=list(range(self.max_mode+1))
        else:modes=sorted(cosine)
        coeff=[cosine.get(m,0) for m in modes];kernels=self.kernels(modes)
        remainder=sum(abs(c)*m**self.degree for c,m in zip(coeff,modes))*self.weights[self.degree]
        result=[]
        for derivatives in kernels:
            variation=remainder;base_lo=base_hi=0
            for d,terms in enumerate(derivatives):
                lo=sum(c*(a if c>=0 else b) for c,(a,b) in zip(coeff,terms))
                hi=sum(c*(b if c>=0 else a) for c,(a,b) in zip(coeff,terms))
                if d==0:base_lo,base_hi=lo,hi
                else:variation+=ceildiv(max(abs(lo),abs(hi))*self.weights[d],SCALE)
            # Convert to outward fixed-point endpoints, still exact integers.
            result.append(((base_lo-variation)//denominator,ceildiv(base_hi+variation,denominator)))
        return result


def central_speed_polynomial(data):
    with np.load(io.BytesIO(gzip.decompress(Path(data).read_bytes())),allow_pickle=False) as f:c=[fq(x) for x in f['jets'][0,0]]
    M=(len(c)-2)//3;planar={1:c[0]}
    if any(c[2*M+1:]):raise ValueError('Original central curve is not planar')
    for j in range(1,M+1):
        planar[1+3*j]=(c[j]+c[M+j])/2;planar[1-3*j]=(c[j]-c[M+j])/2
    out={}
    for m,a in planar.items():
        for n,b in planar.items():out[m-n]=out.get(m-n,Q(0))+m*n*a*b
    cosine={0:out.get(0,Q(0))}
    for m,v in out.items():
        if m>0:
            if m%3 or out.get(-m)!=v:raise ValueError('Wrong actual central speed symmetry')
            cosine[m//3]=2*v
    rounded={m:floorfp(v) for m,v in cosine.items() if v}
    error=sum((abs(v-Q(rounded.get(m,0),SCALE)) for m,v in cosine.items()),Q(0))
    return rounded,ceilfp(error)


def interval_polynomial(coeff,a,b,I):
    """Exact interval Bernstein restriction on [a,b]."""
    n=len(coeff)-1;h=b-a
    power=[sum((coeff[j]*Q(math.comb(j,k))*a**(j-k)*h**k for j in range(k,n+1)),I(0)) for k in range(n+1)]
    bern=[sum((power[k]*Q(math.comb(i,k),math.comb(n,k)) for k in range(i+1)),I(0)) for i in range(n+1)]
    return I.raw(min(x.lo for x in bern),max(x.hi for x in bern))


class LocalMetric:
    def __init__(self,meta,bridge,manifest,bounds,cert):
        self.I=cert.I;cfg=meta['frozen_profile']
        delta,vu,vd,eps=[fq(cfg[k]) for k in ('delta','vu','vd','ramp')]
        self.sp=delta/((1-eps)*vu)+delta/((1-eps)*vd)
        self.Slo,self.Shi=self.sp+Q(bridge['exact_L']['lo']),self.sp+Q(bridge['exact_L']['hi'])
        self.c,self.cuff=fq(manifest['parameters']['rCut']),fq(manifest['parameters']['rCuff'])
        self.h=self.c-self.cuff;self.Tlo,self.Thi=self.Slo+self.h,self.Shi+self.h
        k=2/self.I(5).sqrt();a=1-k;b=Q(28)*self.h/(25*self.c)
        self.co=[self.I(0),k,self.I(-b/2),6*a+3*b/2,-8*a-3*b/2,3*a+b/2]
        self.first=[i*self.co[i] for i in range(1,6)]
        arc=bounds['central_arc_and_partial_primitive_proof']
        self.ahi=Q(arc['mean_arc_radius_upper_exact']);self.Jmin=Q(bounds['central_speed_lower_exact'])
        self.central_end=delta/(vu*(1-eps))*eps
        cc=bounds['deterministic_central_reference_change_jets']
        self.pc=Q(cc['Ws']['upper_exact'])+Q(cc['Wu']['upper_exact'])

    def scales(self,lo,hi):
        I=self.I;fmin=self.c;Hmin=Q(1)
        if hi*self.Thi<=self.sp:fmin=Q(1)
        else:fmin=max(self.c,1-max(Q(0),hi*self.Thi-self.sp))
        if hi*self.Thi>self.Slo:
            a=max(Q(0),(lo*self.h-(1-lo)*self.Shi)/self.h)
            b=min(Q(1),(hi*self.h-(1-hi)*self.Slo)/self.h)
            if a>b:raise ArithmeticError('Invalid common-chart parameter enclosure')
            rp=interval_polynomial(self.first,a,b,I)
            if rp.lo<=0:raise ArithmeticError('The local exact radial chart bound lost positivity')
            Hmin=min(Hmin,rp.lower())
            # R is increasing; evaluating its right end suffices for r_min.
            R=interval_polynomial(self.co,b,b,I)
            fmin=min(fmin,self.c-self.h*R.upper())
        if fmin<self.cuff:
            # The exact common chart maps into [cuff,cut]; outward endpoint
            # arithmetic is allowed to undershoot the proved endpoint only.
            fmin=self.cuff
        if Hmin<=0 or fmin<=0:raise ArithmeticError('Positive target scales unresolved')
        return self.Tlo*Hmin,fmin,self.pc if lo*self.Tlo<self.central_end else Q(0)


def one_piece_bound(c,lo,hi,pm,zm,metric,angular,denom,quick,cert):
    ds=elevated_derivative(c,hi-lo);scale,fmin,pc=metric.scales(lo,hi)
    rz=1/scale;rt=metric.ahi/(fmin*metric.Jmin);local=Q(0);fine=0;row_worst=None
    for j,(zrow,row) in enumerate(zip(ds,c)):
        az=sum(map(abs,zrow),Q(0));at=sum((abs(v)*abs(int(m)) for v,m in zip(row,list(pm)+list(zm))),Q(0))
        crude=rz*az+rt*at
        if crude+pc<=quick:bound=crude
        else:
            znum,zerr=rounded_coefficients(zrow);tnum,terr=rounded_coefficients(row)
            A=angular.enclose(norm_cosine_integers(znum,pm,zm,0),4*SCALE*SCALE)
            B=angular.enclose(norm_cosine_integers(tnum,pm,zm,1),4*SCALE*SCALE)
            alpha=ceilfp(rz*rz);beta=ceilfp(metric.ahi**2/(fmin*fmin));sq=0
            for ia,ib,Jlo in zip(A,B,denom):
                if Jlo<=0:raise ArithmeticError('Central angular speed lower bound unresolved')
                v=ceildiv(alpha*max(0,ia[1]),SCALE)+ceildiv(beta*max(0,ib[1]),Jlo)
                sq=max(sq,v)
            p=cert.I.raw(sq,sq).sqrt().upper()
            ez=sum(zerr,Q(0));et=sum((e*abs(int(m)) for e,m in zip(terr,list(pm)+list(zm))),Q(0))
            bound=p+rz*ez+rt*et;fine+=1
            bound=min(crude,bound)
        if bound>local:local=bound;row_worst=j
    return local+pc,{'unit_interval':[str(lo),str(hi)],'solver_differential_upper':str(up(local)),
                     'central_correction_differential_upper':str(up(pc)),'target_radial_denominator_lower':str(scale),
                     'target_radius_lower':str(fmin),'worst_bernstein_row':row_worst,'angular_refined_rows':fine}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('field','grid','correction-bounds','data','out'):ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--result',type=Path);ap.add_argument('--scripts',type=Path,default=Path(__file__).parent)
    ap.add_argument('--angular-cells',type=int,default=128);ap.add_argument('--taylor-degree',type=int,default=8)
    ap.add_argument('--max-radial-depth',type=int,default=2);ap.add_argument('--quick-differential',default='0.0000004')
    args=ap.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh localized budget output required')
    if not 0<=args.max_radial_depth<=8:raise ValueError('Unsupported radial refinement depth')
    notes=args.scripts.parent/'notes';meta_path=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    bridge_path=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    manifest_path=notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    for p,expected in ((args.data,DATA_SHA),(meta_path,META_SHA),(bridge_path,BRIDGE_SHA),(manifest_path,MANIFEST_SHA)):
        if sha(p)!=expected:raise ValueError('Changed exact original input: '+str(p))
    grid=json.loads(args.grid.read_text());bounds=json.loads(args.correction_bounds.read_text())
    if bounds['script_sha256']!=R226_SHA or bounds['reference_only']:raise ValueError('An actual-field R226 receipt is required')
    if bounds['field_sha256']!=sha(args.field) or bounds['grid_sha256']!=sha(args.grid):raise ValueError('Actual field/continuous receipt identity mismatch')
    if not bounds['continuous_all_knots_and_all_angles'] or not all(bounds['exact_zero_endpoint_jets']):raise ValueError('Invalid previous continuous field receipt')
    if args.result:
        r=json.loads(args.result.read_text())
        if r['field_sha256']!=sha(args.field) or r['grid_sha256']!=sha(args.grid):raise ValueError('Actual solver result identity mismatch')
    meta=json.loads(meta_path.read_text());bridge=json.loads(bridge_path.read_text());manifest=json.loads(manifest_path.read_text())
    cert=load('localized_m12_interval',args.scripts/'6a65-m12-r137-continuous-domain.py')
    if cert.BITS!=BITS:raise ValueError('Different fixed-point interval scale')
    with np.load(args.field,allow_pickle=False) as f:
        coeff=f['coefficients'];knots=f['unit_knots'];pm=f['planar_modes'];zm=f['vertical_modes']
        if not np.all(np.isfinite(coeff)) or not np.all(np.isfinite(knots)):raise ValueError('Nonfinite saved field')
        if not np.array_equal(pm,np.arange(-grid['order'],grid['order']+1)*3+1) or not np.array_equal(zm,np.arange(grid['order']+1)*3):raise ValueError('Wrong actual angular basis')
        shape=list(coeff.shape);coeff=[[fq(v) for v in row] for row in coeff];knots=list(map(fq,knots))
    angular=AngularBoxes(cert,args.angular_cells,args.taylor_degree,max_mode=max(48,2*grid['order']))
    speed,error=central_speed_polynomial(args.data)
    speedboxes=angular.enclose(speed,SCALE)
    metric=LocalMetric(meta,bridge,manifest,bounds,cert)
    globallower=floorfp(metric.Jmin**2)
    denominator=[max(globallower,lo-error) for lo,hi in speedboxes]
    if min(denominator)<=0:raise ArithmeticError('Actual central angular denominator not positive')
    pieces=extract_bezier(knots,coeff);quick=Q(args.quick_differential)
    if quick<=0:raise ValueError('Positive quick enclosure threshold required')
    queue=[(i,a,b,c,0) for i,(a,b,c) in enumerate(pieces)];accepted=[];rows_hash=hashlib.sha256();subdivisions=0;fine_rows=0
    while queue:
        i,a,b,c,depth=queue.pop()
        p,receipt=one_piece_bound(c,a,b,pm,zm,metric,angular,denominator,quick,cert)
        fine_rows+=receipt['angular_refined_rows']
        if p>quick and depth<args.max_radial_depth:
            left,right=split_bezier(c);mid=(a+b)/2
            queue.extend(((i,mid,b,right,depth+1),(i,a,mid,left,depth+1)));subdivisions+=1;continue
        receipt.update({'original_basis_element':i,'radial_subdivision_depth':depth,'total_differential_upper':str(up(p))})
        rows_hash.update((json.dumps(receipt,sort_keys=True,separators=(',',':'))+'\n').encode());accepted.append((p,receipt))
    worst=max(accepted,key=lambda x:x[0]);p=worst[0];d=Q(257212,10**13)
    residual=d+2*(1+d)*p+p*p
    result={'schema':'6a65-M12-local-Bernstein-angular-continuous-metric-budget-v1',
            'script_sha256':sha(__file__),'interval_helper_sha256':sha(cert.__file__),
            'field_sha256':sha(args.field),'grid_sha256':sha(args.grid),'correction_bounds_sha256':sha(args.correction_bounds),
            'solver_result_sha256':sha(args.result) if args.result else None,'data_sha256':DATA_SHA,
            'common_meta_sha256':META_SHA,'bridge_sha256':BRIDGE_SHA,'tail_manifest_sha256':MANIFEST_SHA,
            'field_shape':shape,'same_actual_field_no_refit':True,'same_original_exact_metric':True,
            'continuous_all_basis_pieces_and_all_angles':True,'exact_Boehm_insertion':True,
            'angular_norms_squared_before_enclosure':True,'central_normalization_correction_included':True,
            'source_cross_Gram_cancellation_used':False,
            'proof_method':'Exact Bernstein extraction and Jensen; exact autocorrelations of rounded dyadic vector coefficients; explicit rounding errors; integer Taylor boxes and strict local target scales.',
            'basis_elements':len(pieces),'accepted_subpieces':len(accepted),'radial_subdivisions':subdivisions,
            'angular_refined_rows':fine_rows,'angular_cells_in_one_reflected_D3_sector':args.angular_cells,
            'angular_taylor_degree':args.taylor_degree,'integer_bits':BITS,'row_stream_sha256':rows_hash.hexdigest(),
            'target_orthonormal_differential_Frobenius_upper':summary(p),
            'metric_triangle_upper':summary(residual),'continuous_metric_below_1e_6':residual<Q(1,10**6),
            'worst_subpiece':worst[1],'top_subpieces':[r for _,r in sorted(accepted,key=lambda x:x[0],reverse=True)[:12]],
            'whole_reach_certificate':False,'exact_isometry_proved':False,
            'raw_retention':'Input field remains temporary; this report contains only scalar identities and bounds.',
            'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result,indent=2,allow_nan=False))

if __name__=='__main__':main()
