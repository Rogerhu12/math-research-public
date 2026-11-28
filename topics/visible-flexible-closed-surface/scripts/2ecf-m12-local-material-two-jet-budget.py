#!/usr/bin/env python3
"""Exact local two-jet bounds for a saved M12 Cartesian spline correction.

The material angular second derivative is evaluated as the single Fourier
numerator a^2(P W_tt - P_t W_t/2)/P^2, P=|gamma_t|^2. All source identities,
central correction, true cuff, and radial chart factors are retained.
This is a sufficient continuous geometry transfer, not an exact isometry.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, io, json, math, time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

BITS=96
S=1<<BITS

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def floor(q):q=Q(q);return q.numerator*S//q.denominator
def ceil(q):q=Q(q);return -((-q.numerator*S)//q.denominator)
def up(q):return Q(ceil(q),S)
def packet(q,side='upper'):return {side+'_exact':str(q),'display':float(q)}

def central_laurent(data):
    with np.load(io.BytesIO(gzip.decompress(Path(data).read_bytes())),allow_pickle=False) as f:
        row=[fq(x) for x in f['jets'][0,0]]
    M=(len(row)-2)//3
    if any(row[2*M+1:]):raise ValueError('Original central curve must be planar')
    c={1:row[0]}
    for j in range(1,M+1):
        c[1+3*j]=(row[j]+row[M+j])/2;c[1-3*j]=(row[j]-row[M+j])/2
    P={}
    for m,a in c.items():
        for n,b in c.items():P[m-n]=P.get(m-n,Q(0))+m*n*a*b
    return {k:v for k,v in P.items() if v}

def elevated_derivatives(c,width):
    """All 0,1,2 derivatives represented by the same degree-five weights."""
    out=[c]
    for d in (1,2):
        row=c
        degree=5
        for unused in range(d):
            row=[[degree*(b-a)/width for a,b in zip(x,y)] for x,y in zip(row[:-1],row[1:])]
            degree-=1
        while degree<5:
            n=degree+1
            row=[row[0]]+[[Q(i,n)*a+Q(n-i,n)*b for a,b in zip(row[i-1],row[i])]
                          for i in range(1,n)]+[row[-1]]
            degree+=1
        out.append(row)
    return out

def round_vector(row,pm,zm):
    p={int(m):v for m,v in zip(pm,row[:len(pm)])}
    z={}
    for m,v in zip(zm,row[len(pm):]):
        m=int(m)
        if m:z[m]=v/2;z[-m]=v/2
        else:z[0]=v
    values=[];err=[Q(0)]*3;exact=[Q(0)]*3
    for part in (p,z):
        integer={m:floor(v) for m,v in part.items() if v}
        for m,v in part.items():
            e=abs(v-Q(integer.get(m,0),S))
            for j in range(3):err[j]+=abs(m)**j*e;exact[j]+=abs(m)**j*abs(v)
        values.append(integer)
    return values,err,exact

def cosine_norm(values):
    """Squared Euclidean norm of complex xy plus real z Laurent series."""
    out={}
    for part in values:
        terms=sorted((m,v) for m,v in part.items() if v)
        out[0]=out.get(0,0)+sum(v*v for m,v in terms)
        for i,(m,a) in enumerate(terms):
            for n,b in terms[i+1:]:
                if (n-m)%3:raise ValueError('D3 symmetry not retained')
                k=(n-m)//3;out[k]=out.get(k,0)+2*a*b
    return {k:v for k,v in out.items() if v}

def angular_derivative(values,j):
    # The common i^j phase has unit norm and is omitted for both components.
    return [{m:m**j*v for m,v in part.items() if m or j==0} for part in values]

class Bounds:
    def __init__(self,old,cert,metric,P,cells,degree):
        self.old,self.cert,self.metric=old,cert,metric
        self.angular=old.AngularBoxes(cert,cells,degree)
        self.pi={m:floor(v) for m,v in P.items()}
        self.perr=[sum((abs(m)**j*abs(v-Q(self.pi[m],S)) for m,v in P.items()),Q(0)) for j in range(2)]
        self.pl1=[Q(sum(abs(m)**j*abs(v) for m,v in self.pi.items()),S) for j in range(2)]
        cosine={0:P.get(0,Q(0))}
        for m,v in P.items():
            if m>0:
                if m%3 or P.get(-m)!=v:raise ValueError('Central speed symmetry changed')
                cosine[m//3]=2*v
        rounded={k:floor(v) for k,v in cosine.items()}
        error=ceil(sum((abs(v-Q(rounded[k],S)) for k,v in cosine.items()),Q(0)))
        minimum=floor(metric.Jmin**2)
        self.Plo=[Q(max(minimum,a-error),S) for a,b in self.angular.enclose(rounded,S)]
        if min(self.Plo)<=0:raise ArithmeticError('Unresolved positive central speed')

    def numerator(self,values,error,exact):
        result=[]
        for part in values:
            out={}
            for k,p in self.pi.items():
                for m,w in part.items():
                    n=k+m;out[n]=out.get(n,0)+p*w*(-2*m*m+k*m)
            result.append({m:v for m,v in out.items() if v})
        # Numerator integer denominator is 2*S^2. Exact P and W rounding
        # errors are propagated before taking any spatial or angular supremum.
        e=(self.perr[0]*exact[2]+self.pl1[0]*error[2]
           +(self.perr[1]*exact[1]+self.pl1[1]*error[1])/2)
        return result,e

    def norms(self,values,denominator,error):
        boxes=self.angular.enclose(cosine_norm(values),denominator**2)
        return [self.cert.I.raw(max(0,b),max(0,b)).sqrt().upper()+error for a,b in boxes]

    def scales(self,lo,hi):
        metric=self.metric
        radial,fmin,pc=metric.scales(lo,hi)
        Hmin=radial/metric.Tlo;Hq=Q(0)
        if hi*metric.Thi>metric.Slo:
            a=max(Q(0),(lo*metric.h-(1-lo)*metric.Shi)/metric.h)
            b=min(Q(1),(hi*metric.h-(1-hi)*metric.Slo)/metric.h)
            first=self.old.interval_polynomial(metric.first,a,b,self.cert.I)
            second=self.old.interval_polynomial([i*metric.first[i] for i in range(1,5)],a,b,self.cert.I)
            rp=max(abs(first.lower()),abs(first.upper()))
            rpp=max(abs(second.lower()),abs(second.upper()))
            # R223/R226: |w|<=16/15, |w_r|<24, sqrt(1+w^2)<3/2.
            Hq=min(Q(60),Q(3,2)*rpp/metric.h+rp*rp*Q(16,15)*24)
        return radial,fmin,pc,Hq/(metric.Tlo*Hmin**3)

    def piece(self,c,lo,hi,pm,zm,cc,quick_p,quick_c):
        d0,d1,d2=elevated_derivatives(c,hi-lo)
        radial,fmin,pc,Bss=self.scales(lo,hi);A=self.metric.ahi
        active=bool(pc);c_eta=cc[0,0] if active else Q(0)
        c_second=cc[2,0]+2*cc[1,1]+cc[0,2] if active else Q(0)
        maxeta=maxfirst=maxsecond=Q(0);fine=0;worst=None
        for i,rows in enumerate(zip(d0,d1,d2)):
            v0,e0,l0=round_vector(rows[0],pm,zm)
            v1,e1,l1=round_vector(rows[1],pm,zm)
            v2,e2,l2=round_vector(rows[2],pm,zm)
            nv,ne=self.numerator(v0,e0,l0)
            nl1=Q(sum(abs(x) for part in nv for x in part.values()),2*S*S)+ne
            J=self.metric.Jmin
            crude_p=l1[0]/radial+A*l0[1]/(fmin*J)
            crude_c=l2[0]/radial**2+Bss*l1[0]+2*A*l1[1]/(radial*fmin*J)+A*A*nl1/(fmin*fmin*J**4)
            eta,p,c2=l0[0],crude_p,crude_c
            if crude_p+pc>quick_p or crude_c+c_second>quick_c:
                N0=self.norms(v0,S,e0[0]);N1=self.norms(v1,S,e1[0]);N2=self.norms(v2,S,e2[0])
                Nt=self.norms(angular_derivative(v0,1),S,e0[1])
                N1t=self.norms(angular_derivative(v1,1),S,e1[1]);NN=self.norms(nv,2*S*S,ne)
                pp=[];second=[]
                for u,z,zz,t,zt,n,p0 in zip(N0,N1,N2,Nt,N1t,NN,self.Plo):
                    js=self.cert.I(p0).sqrt().lower()
                    pp.append(self.cert.I((z/radial)**2+A*A*t*t/(fmin*fmin*p0)).sqrt().upper())
                    second.append(zz/radial**2+Bss*z+2*A*zt/(radial*fmin*js)+A*A*n/(fmin*fmin*p0*p0))
                eta=min(eta,max(N0));p=min(p,max(pp));c2=min(c2,max(second));fine+=1
            maxeta=max(maxeta,eta);maxfirst=max(maxfirst,p)
            if c2>maxsecond:maxsecond=c2;worst=i
        return (up(maxeta+c_eta),up(maxfirst+pc),up(maxsecond+c_second)),{
            'unit_interval':[str(lo),str(hi)],'target_radial_denominator_lower':str(radial),
            'target_radius_lower':str(fmin),'Hq_over_T_H_cubed_upper':str(Bss),
            'central_correction_active':active,'angular_refined_rows':fine,'worst_second_jet_control':worst}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','data','field','grid','result','correction-bounds','source-bounds','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--angular-cells',type=int,default=128);ap.add_argument('--taylor-degree',type=int,default=8)
    ap.add_argument('--max-radial-depth',type=int,default=1)
    ap.add_argument('--quick-first',default='0.0000004');ap.add_argument('--quick-second',default='0.01')
    args=ap.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh output required')
    if not 0<=args.max_radial_depth<=6:raise ValueError('Unsupported radial depth')
    old=load('m12_R236',args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py')
    cert=load('m12_R220',args.scripts/'6a65-m12-r137-continuous-domain.py')
    if cert.BITS!=BITS:raise ValueError('Wrong interval precision')
    notes=args.scripts.parent/'notes'
    meta_path=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    bridge_path=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    manifest_path=notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    for path,expected in [(args.data,old.DATA_SHA),(meta_path,old.META_SHA),(bridge_path,old.BRIDGE_SHA),(manifest_path,old.MANIFEST_SHA)]:
        if sha(path)!=expected:raise ValueError('Changed original source: '+str(path))
    grid,result,change,source=[json.loads(x.read_text()) for x in [args.grid,args.result,args.correction_bounds,args.source_bounds]]
    field_sha,grid_sha=sha(args.field),sha(args.grid)
    if change['script_sha256']!=old.R226_SHA or change['reference_only']:raise ValueError('Actual R226 field receipt required')
    for record in (change,result):
        if record['field_sha256']!=field_sha or record['grid_sha256']!=grid_sha:raise ValueError('Different actual fields')
    if not all(change['exact_zero_endpoint_jets']) or not change['continuous_all_knots_and_all_angles']:raise ValueError('Complete C2 traces required')
    if not result['original_exact_metric_unchanged'] or not result['true_flat_cuff_included']:raise ValueError('Wrong original complete domain')
    for key,expected in [('data_sha256',old.DATA_SHA),('common_meta_sha256',old.META_SHA),('bridge_sha256',old.BRIDGE_SHA),('tail_manifest_sha256',old.MANIFEST_SHA)]:
        if source[key]!=expected:raise ValueError('Changed continuous source '+key)
    if not source['continuous_all_spans_and_all_angles'] or not source['exact_common_cut_change_included']:raise ValueError('Incomplete source')
    if source['tail_cache_sha256']!=result['query_cache_sha256'] or source['tail_report_sha256']!=result['query_report_sha256']:raise ValueError('Different true tail')
    metric=old.LocalMetric(json.loads(meta_path.read_text()),json.loads(bridge_path.read_text()),json.loads(manifest_path.read_text()),change,cert)
    bounder=Bounds(old,cert,metric,central_laurent(args.data),args.angular_cells,args.taylor_degree)
    with np.load(args.field,allow_pickle=False) as f:
        coeff=f['coefficients'];knots=f['unit_knots'];pm=f['planar_modes'];zm=f['vertical_modes']
        if not np.all(np.isfinite(coeff)) or not np.all(np.isfinite(knots)):raise ValueError('Nonfinite field')
        if not np.array_equal(pm,np.arange(-grid['order'],grid['order']+1)*3+1) or not np.array_equal(zm,np.arange(grid['order']+1)*3):raise ValueError('Different D3 basis')
        coeff=[[fq(v) for v in row] for row in coeff];knots=list(map(fq,knots))
    if any(knots.count(u)>3 for u in set(knots) if 0<u<1):raise ValueError('The actual spline must be globally C2')
    label={(0,0):'W',(1,0):'Ws',(0,1):'Wu',(2,0):'Wss',(1,1):'Wsu',(0,2):'Wuu'}
    cc={k:Q(change['deterministic_central_reference_change_jets'][v]['upper_exact']) for k,v in label.items()}
    pieces=old.extract_bezier(knots,coeff);stack=[(i,a,b,c,0) for i,(a,b,c) in enumerate(pieces)]
    accepted=[];digest=hashlib.sha256();qp,qc=Q(args.quick_first),Q(args.quick_second)
    while stack:
        i,a,b,c,depth=stack.pop();values,row=bounder.piece(c,a,b,pm,zm,cc,qp,qc)
        if (values[1]>qp or values[2]>qc) and depth<args.max_radial_depth:
            left,right=old.split_bezier(c);mid=(a+b)/2
            stack.extend([(i,mid,b,right,depth+1),(i,a,mid,left,depth+1)]);continue
        row.update(element=i,depth=depth,displacement=str(values[0]),differential=str(values[1]),scaled_second=str(values[2]))
        digest.update((json.dumps(row,sort_keys=True)+'\n').encode());accepted.append((values,row))
        if len(accepted)%100==0:print(json.dumps({'continuous_subpieces_completed':len(accepted),'pending':len(stack),'seconds':time.monotonic()-began}),flush=True)
    eta,p,cw=[max(v[j] for v,row in accepted) for j in range(3)]
    d=Q(257212,10**13);K0=Q(4763997235009095,562949953421312);R=Q(2131902881202937,1125899906842624)
    cx=Q(source['entire_half_original_C_X']['upper_exact']);eps=d+2*(1+d)*p+p*p;nu=(3*p+p*p)/(1-d)
    diameter=2*(R+eta);support=Q(737,1000)-Q(19,10)*nu-eta;loss=2400*eta*(1+9*eta)**2
    geometry=False;quant={'displacement':packet(eta),'target_differential':packet(p),'change_scaled_second_jets':packet(cw),
        'metric_triangle':packet(eps),'normal_change':packet(nu),'support':packet(support,'lower'),'diameter':packet(diameter)}
    if eps<1:
        K=(K0*(1+d)+nu*cx+cw)/(1-eps);reach=1/(K*diameter);held=(Q(19989114,10**8)-2*eta)/diameter
        geometry=(eta<1/K0 and R+eta<2 and loss<Q(44016,10**5) and support>1/K and K<2000)
        quant.update(principal_curvature=packet(K),reach_over_diameter=packet(reach,'lower'),held_over_diameter=packet(held,'lower'),
                     fixed_cap_diameter_ratio=packet(Q(35426,10**4)/diameter,'lower'),activity_third_moment_loss=packet(loss))
    out={'schema':'2ecf-M12-local-material-two-jet-continuous-budget-v1','script_sha256':sha(__file__),
        'field_sha256':field_sha,'grid_sha256':grid_sha,'solver_result_sha256':sha(args.result),
        'correction_receipt_sha256':sha(args.correction_bounds),'source_receipt_sha256':sha(args.source_bounds),
        'R236_helper_sha256':sha(old.__file__),'interval_helper_sha256':sha(cert.__file__),
        'same_original_metric':True,'same_actual_field':True,'all_original_spans_and_all_angles':True,
        'central_correction_included':True,'material_angular_numerator_cancellation_used':True,
        'source_cross_Gram_cancellation_used':False,'source_normal_projection_cancellation_used':False,
        'radial_pieces':len(pieces),'accepted_subpieces':len(accepted),'row_stream_sha256':digest.hexdigest(),
        'angular_cells':args.angular_cells,'taylor_degree':args.taylor_degree,'integer_bits':BITS,
        'rational_quantities':quant,'geometry_transfer_conditions':geometry,'metric_below_1e_6':eps<Q(1,10**6),
        'reach_over_D_above_003':bool(geometry and reach>Q(3,100)),
        'held_over_D_above_005':bool(geometry and held>Q(5,100)),
        'top_second_jet_subpieces':[r for v,r in sorted(accepted,key=lambda a:a[0][2],reverse=True)[:8]],
        'exact_isometry_proved':False,'README_completion_claim':False,'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(out,indent=2,allow_nan=False))

if __name__=='__main__':main()
