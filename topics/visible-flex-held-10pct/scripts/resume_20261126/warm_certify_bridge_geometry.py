#!/usr/bin/env python3
"""Continuous metric and geometry of one new warm field's complete true bridge.

The shared-right-two-jet map, true literal-phase radius, literal mean1168 and
true mean-height primitive are the same definitions used by the new Zc driver.
The old Fourier--Taylor Gram proof and all-angle curvature formulas are reused;
old field numbers and GL64-to-true-map identifications are not reused.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from bisect import bisect_right
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np
import mpmath as mp

REVIEWED={
    'resume_m3/certify_prefix_metric_interval_taylor.py':
        '6b36ccd6bab54fa35c6fe62a433f417faf7a51b80c35b798b17567eb22714986',
    'resume_m3/certify_bridge_metric_fourier_taylor.py':
        'fe99f0afc6ed90dac1b9b3616c857421fa621901958dfbafdbb26191c5766bb2',
    'resume_m3/certify_r59_fixed_mean_ranges.py':
        'ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5',
    'resume_m3/certify_r59_shared_jet_transfer.py':
        '85aff94a38f57e184e8bd5ca99b87898f0fec41043b0eedc9325623c4fba2c00',
    'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py':
        '6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7',
    'resume_20261126/seam_m3_prefix_pieces.py':
        'dd353c3306ea35dd068e25951917fd8d204635b9e4cc07a41f7957834cbee01d',
    'resume_20261126/seam_certify_true_cut_height.py':
        '998509f9463e0d377dc6dcde42ae71c62dcc0c02e77d6e1ec24bb634050a5b7c',
    'resume_20261126/seam_bridge_endpoint_primitive.py':
        'ac9c07f3022f3b271a873acad100dc779f421d44fe1397ccd75612597ac8b7a1',
    'resume_20261126/seam_bridge_cut_trace.py':
        'c77e8e5bb37d4469f6dd7f7a21ec7301721c2eaf979109e249630cd54880b32b',
}
PSI_SHA='f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf'
HERMITE=[
    [Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)],
    [Q(0),Q(1),Q(0),Q(-6),Q(8),Q(-3)],
    [Q(0),Q(0),Q(1,2),Q(-3,2),Q(3,2),Q(-1,2)],
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def fq(value):
    value=float(value)
    if not math.isfinite(value):
        raise ValueError('A finite literal scalar is required')
    return Q.from_float(value)


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec)
    sys.modules[name]=result
    spec.loader.exec_module(result)
    return result


def ref(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def checked(reference):
    path=Path(reference['path']).resolve()
    if sha(path)!=reference['sha256']:
        raise ValueError('A bound input changed: '+str(path))
    return path


def write(path,data):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
    tmp.replace(path)


def scalar(value):
    lo,hi=map(float,value.x)
    if not math.isfinite(lo) or not math.isfinite(hi) or lo>hi:
        raise ArithmeticError('Invalid scalar interval')
    return dict(lower=lo,upper=hi,lower_exact=str(fq(lo)),upper_exact=str(fq(hi)))


def setup(repo):
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    for relative,digest in REVIEWED.items():
        if sha(scripts/relative)!=digest:
            raise ValueError('A reviewed dependency changed: '+relative)
    sys.path.insert(0,str(scripts/'resume_m3'))
    sys.path.insert(0,str(scripts/'resume_20261126'))
    helper=module('_warm_bridge_height_definition',
                  scripts/'resume_20261126/seam_certify_true_cut_height.py')
    b=helper.jets
    b.m.K=module('_warm_bridge_outward_kernel',
                 scripts/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py')
    # The original finite-mean algebra is differentiated twice. This does not
    # change its value definition or its literal angular nodes.
    b.m.D=b.D2
    b.m.sincos_d=b.trig
    if helper.prefix_mean.b is not b or helper.prefix_mean.I is not b.I:
        raise ValueError('The exact bridge and prefix kernels must share one interval type')
    return scripts,helper


class TrueBridgeJets:
    """The same MeanMap bridge, with its actual first two radial derivatives."""
    def __init__(self,base,helper):
        self.base,self.b,self.m=base,helper.jets,helper.jets.m
        self.M,self.N,self.q=base.M,base.N,base.q
        self.frequencies=np.asarray(base.f.even,int)
        self.co,self.sn,self.co3,self.sn3=base.co,base.sn,base.co3,base.sn3
        self.entry,self.end=base.entry,base.end
        self.grid=[x for x in base.grid if self.entry<=x<=self.end]
        self.cache={}

    def field(self,s,left,right,order=0):
        z=self.base
        i=min(len(z.xx)-2,bisect_right(z.xx,(left+right)/2)-1)
        if not z.xx[i]<=left<=right<=z.xx[i+1]:
            raise ValueError('A shared physical quintic join was crossed')
        c=z.pc[i]
        for _ in range(order):
            c=self.m.pder(c)
        x=s-self.b.I.rational(z.xx[i])
        return self.b.D2(self.m.poly(c,x)*self.q,
            self.m.poly(self.m.pder(c),x)*self.q,
            self.m.poly(self.m.pder(self.m.pder(c)),x)*self.q)

    coefficients=field

    def chart(self,s,left,right):
        z=self.base
        i=min(len(z.spx)-2,bisect_right(z.spx,(left+right)/2)-1)
        if not z.spx[i]<=left<=right<=z.spx[i+1]:
            raise ValueError('A shared angular polynomial join was crossed')
        if left<z.cutoff<right:
            raise ValueError('The late angular cutoff join was crossed')
        c=z.ec[i,(left+right)/2>z.cutoff][0]
        c1=self.m.pder(c);c2=self.m.pder(c1);c3=self.m.pder(c2)
        x=s-self.b.I.rational(z.spx[i])
        return (self.b.D2(self.m.poly(c,x),self.m.poly(c1,x),self.m.poly(c2,x)),
                self.b.D2(self.m.poly(c1,x),self.m.poly(c2,x),self.m.poly(c3,x)))

    def profile(self,s,left,right):
        z=self.base
        if not z.entry<=left<=right<=z.end:
            raise ValueError('A bridge-only query left its exact physical interval')
        # This value enclosure is exactly the one used in the Zc definition.
        radius,_=z.bridge(left,right)
        x=self.b.D2(s-self.b.I.rational(z.entry),1)
        first,last=left-z.entry,right-z.entry
        P=self.b.D2(self.b.I.rational(z.peak))
        if last<=z.L1:
            u=x/self.b.I.rational(z.L1)
            phase=P*(3*u*u-2*u*u*u)
        elif first>=z.L1 and last<=z.L1+z.L2:
            phase=P
        elif first>=z.L1+z.L2:
            u=(x-self.b.I.rational(z.L1+z.L2))/self.b.I.rational(z.L3)
            phase=P-u*u*self.b.I.rational(z.eps)
        else:
            raise ValueError('A true bridge phase join was crossed')
        sine,cosine=self.b.trig(phase)
        ap=-sine
        # radius is the unique TRUE primitive. Its derivatives are these
        # analytic identities, never derivatives assigned to a GL64 function.
        a=self.b.D2(radius,ap.v,ap.d)
        return a,ap,cosine

    def evaluate(self,left,right):
        key=(left,right)
        if key not in self.cache:
            value=self.m.MeanVerifier.evaluate(self,left,right)
            if not all(getattr(value[1],name).finite() for name in ('v','d','d2')):
                raise ArithmeticError('Nonfinite true-mean derivative enclosure')
            if len(self.cache)>=4:
                self.cache.clear()
            self.cache[key]=value
        return self.cache[key]


class BridgePieces:
    """The minimal unchanged PrefixMetric interface, with identically zero lift."""
    def __init__(self,jets):
        self.jets=jets

    def field(self,*args):
        return self.jets.field(*args)

    def chart(self,*args):
        return self.jets.chart(*args)

    def profile(self,*args):
        return self.jets.profile(*args)[:2]

    def lift(self,*args):
        return self.jets.b.D2(0),self.jets.b.D2(0)


class HeightPrimitive:
    """Exact rational cumulative Darboux enclosures of this same complete map."""
    def __init__(self,path,run_path,physical_path,core_path,core_arrays,run,obj,helper):
        record=read(path)
        if (record.get('complete') is not True or
                record.get('status')!='actual_true_cut_height_enclosed' or
                record.get('model_kind')!=run['model_kind'] or
                record.get('modes')!=obj.M or record.get('mean_nodes')!=1168 or
                record.get('literal_psi_sha256')!=PSI_SHA or
                record.get('true_height_anchor_exact')!='0' or
                Q(record['prefix_end_exact'])!=obj.entry or
                Q(record['cut_s_exact'])!=obj.end or
                record.get('original_frozen_source_signature')!=run['frozen_source_signature']):
            raise ValueError('Require this complete field\'s true mean-height certificate')
        for key,wanted in (('source_run',run_path),('physical',physical_path),
                           ('core_mean_certificate',core_path),('core_mean_intervals',core_arrays)):
            if checked(record[key])!=Path(wanted).resolve():
                raise ValueError('The true-height input identity differs in '+key)
        if checked(record['source'])!=Path(helper.__file__).resolve():
            raise ValueError('The true-height defining source differs')
        for source,digest in record['helper_sources'].items():
            if sha(source)!=digest:
                raise ValueError('A true-height helper changed: '+source)
        expected={key:str(getattr(obj,key)) for key in ('peak','eps','L1','L2','L3')}
        if record['literal_bridge_phase_exact']!=expected:
            raise ValueError('The true-height bridge phase differs')
        leaves=checked(record['actual_leaf_record'])
        self.rows=[];self.starts=[];total=[Q(0),Q(0)]
        sums={'prefix':[Q(0),Q(0)],'bridge':[Q(0),Q(0)]}
        last=Q(0)
        with gzip.open(leaves,'rt') as stream:
            for line in stream:
                row=json.loads(line)
                left,right=Q(row['left_exact']),Q(row['right_exact'])
                low,high=Q(row['mean_lower_exact']),Q(row['mean_upper_exact'])
                if left!=last or not left<right<=obj.end or low>high:
                    raise ValueError('The true-height leaves do not form an ordered exact partition')
                i=bisect_right(obj.grid,left)-1
                if i<0 or right>obj.grid[i+1]:
                    raise ValueError('A true-height leaf crosses a defining radial join')
                part='prefix' if right<=obj.entry else 'bridge'
                if row['part']!=part or (part=='bridge' and left<obj.entry):
                    raise ValueError('A true-height leaf crosses the prefix/bridge join')
                root=float(row['frenet_root_lower'])
                if not math.isfinite(root) or root<=0:
                    raise ValueError('A true-height leaf has no positive Frenet root')
                self.starts.append(left)
                self.rows.append((left,right,low,high,total[0],total[1]))
                width=right-left
                for j,value in enumerate((low,high)):
                    total[j]+=width*value
                    sums[part][j]+=width*value
                last=right
        if last!=obj.end or len(self.rows)!=record['accepted_cells']:
            raise ValueError('The complete true-height partition is incomplete')
        for key,values in (('prefix_integral',sums['prefix']),
                           ('bridge_integral',sums['bridge']),('Z_cut_interval',total)):
            if [Q(record[key]['lower_exact']),Q(record[key]['upper_exact'])]!=values:
                raise ValueError('The exact true-height leaf sum differs in '+key)
        self.record=record
        self.leaves=leaves
        self.grid=self.starts+[obj.end]

    def enclose(self,left,right,I):
        i=min(len(self.rows)-1,bisect_right(self.starts,(left+right)/2)-1)
        a,b,low,high,zlow,zhigh=self.rows[i]
        if not a<=left<=right<=b:
            raise ValueError('A cumulative mean-primitive leaf was crossed')
        products=[t*m for t in (left-a,right-a) for m in (low,high)]
        lo=zlow+min(products);hi=zhigh+max(products)
        return I(I.rational(lo).x[0],I.rational(hi).x[1])


class TailMatchedTarget:
    """One exact target definition; interval d_j enclose fixed, unique numbers."""
    def __init__(self,base,helper,scripts,trace_path,run_path,physical_path,run):
        self.I=helper.jets.I
        self.base=base
        self.length=Q(1,1000)
        cut_module=module('_warm_bridge_cut_definition',
                         scripts/'resume_20261126/seam_bridge_cut_trace.py')
        trace=read(trace_path)
        if (trace.get('status')!='accepted_prefix_true_cut_R_trace_enclosed' or
                trace.get('source_sha256')!=sha(cut_module.__file__) or
                trace.get('ShortBridge_sha256')!=helper.SHORT_SHA or
                trace.get('source_run_sha256')!=sha(run_path) or
                trace.get('physical_sha256')!=sha(physical_path) or
                trace.get('modes')!=base.M or trace.get('mean_nodes')!=1168 or
                trace.get('psi_sha256')!=PSI_SHA or
                Q(trace['s_entry_exact'])!=base.entry or Q(trace['s_cut_exact'])!=base.end):
            raise ValueError('Require this actual field\'s true common-R cut trace')
        for key,relative in (
                ('primitive_helper_sha256','resume_20261126/seam_bridge_endpoint_primitive.py'),
                ('mean_kernel_sha256','resume_m3/certify_r59_fixed_mean_ranges.py'),
                ('interval_kernel_sha256','finite_closure/m3_m8_closed_map/interval_geometry_kernel.py')):
            if trace[key]!=sha(scripts/relative):
                raise ValueError('The cut-trace defining source differs in '+key)
        reference=scripts.parent/'notes/2026-11-20-m3-m24-warm050-execution.json'
        if trace['background_record_sha256']!=sha(reference):
            raise ValueError('The declared true-tail physical background changed')
        declared=list(run.get('inputs',{}).values())+[run.get('linear_port_sha256')]
        if trace['source_port_sha256'] not in declared:
            raise ValueError('The cut trace is not bound to the actual frozen port')
        Rc,w=map(fq,(.3,.08));wR=-7*w/Rc
        if any(Q(trace[key])!=wanted for key,wanted in (
                ('R_cut_exact',Rc),('target_w_exact',w),('target_wR_exact',wR))):
            raise ValueError('The R58 true cut-background identities differ')
        if fq(run['physical_tail_cut']['radius'])!=Rc:
            raise ValueError('The physical cut radius differs from the unified target')
        exact,phase=cut_module.true_radius(base.bridge_phase,base.f.bridge,base.end-base.entry)
        if trace['literal_phase_parameters']!=phase or not self.length<base.L3:
            raise ValueError('The full literal bridge phase differs or patch leaves its last piece')
        actual=[self.I(self.I.rational(lo).x[0],self.I.rational(hi).x[1])
                for lo,hi in exact]
        E=1+w*w
        wanted=[self.I.rational(Rc),-1/self.I.rational(E).sqrt(),
                self.I.rational(-w*wR/E**2)]
        self.d=[x-y for x,y in zip(wanted,actual)]
        self.start=base.end-self.length
        # The correction definition is exact and has the prescribed two-jets.
        for j,poly in enumerate(HERMITE):
            c=poly
            for k in range(3):
                if (base.bridge_phase.value(c,Q(0))!=(1 if j==k else 0) or
                        base.bridge_phase.value(c,Q(1))!=0):
                    raise ArithmeticError('Target Hermite endpoint identities failed')
                c=base.bridge_phase.derivative(c)
        self.definition=dict(
            material_metric='ds^2 + a_hat(s)^2 dtheta^2',
            bridge_radius='Unique true primitive of minus sine of the frozen literal phase; a(entry)=1',
            true_tail_cut_R_exact=str(Rc),true_tail_cut_w_exact=str(w),
            true_tail_cut_wR_exact=str(wR),patch_length_exact=str(self.length),
            literal_bridge_phase_exact=phase,prefix_end_exact=str(base.entry),
            cut_s_exact=str(base.end),frozen_profile=run['frozen_profile'],
            correction='sum_j (-L)^j h_j((s_end-s)/L) d_j on the final L; zero elsewhere',
            endpoint_d_j_definition='true-tail arclength radius two-jet minus unique true bridge radius two-jet',
            coefficient_midpoints_chosen=False,independent_of_field_and_M=True,
            true_tail_arclength_two_jet_exact=True)
        self.definition_sha256=helper.canonical_sha(self.definition)
        self.endpoint_d_intervals=[scalar(x) for x in self.d]
        self.trace=trace

    def correction(self,left,right,order=0):
        I=self.I
        if right<=self.start:
            return I(0)
        if left<self.start or not left<=right<=self.base.end:
            raise ValueError('A target-radius patch join was crossed')
        u=I(I.rational((self.base.end-right)/self.length).x[0],
            I.rational((self.base.end-left)/self.length).x[1])
        value=I(0)
        for j,poly in enumerate(HERMITE):
            c=poly
            for _ in range(order):
                c=self.base.bridge_phase.derivative(c)
            # The same unique fixed d_j is used across the whole correction;
            # independently enclosing it does not choose another target.
            term=I(0)
            for a in c[::-1]:
                term=term*u+I.rational(a)
            value+=I.rational((-self.length)**j*(-1/self.length)**order)*term*self.d[j]
        return value

    def transfer(self,left,right,amin,metric):
        I=self.I
        gap=self.correction(left,right).absolute_upper()
        lower=I(amin)-I(gap)
        if float(lower.x[0])<=0:
            raise ValueError('The unified target radius is not bounded positive')
        eta=I(gap)/lower
        bound=(1+eta).sq()*metric+2*eta+eta.sq()
        return float(bound.x[1]),dict(
            target_radius_correction_upper=gap,
            target_radius_lower=float(lower.x[0]),
            target_metric_change_upper=float((2*eta+eta.sq()).x[1]))


def angular_boxes(v,frequencies,count):
    lo=2*np.pi*np.arange(count)/count
    mp.iv.dps=75
    endpoint=float(v.m.K.up(float((2*mp.iv.pi).b)))
    hi=np.r_[lo[1:],endpoint]
    if lo[0]!=0 or np.any(hi<=lo) or lo[-1]>=float((2*mp.iv.pi).a):
        raise ValueError('The closed angular boxes must cover true [0,2*pi]')
    table=v.AngleTable(lo,hi,frequencies)
    # The complete core/reference lift is identically zero on the bridge.
    table.H=[[v.I(np.zeros(count)) for _ in range(3)] for _ in range(4)]
    return table


def geometry(v,metric,table,mean,height,left,right,metric_star):
    wd=metric.data(left,right,'radial')
    _,wm,_=mean.evaluate(left,right)
    angular=[v.constant(x.v) for x in wd]
    _,au,av,velocity,rho=metric.metric(table,angular,v.constant(wm.v),'angular',True)
    metric.last_context=(wd,wm,au,av,velocity,rho)
    curvature=metric.curvature(metric_star)
    if not math.isfinite(curvature) or curvature<0:
        raise ArithmeticError('Nonfinite curvature enclosure')
    er,_,_,_,_=metric.frame(table,wd,'radial')
    G=table.basis(wd[0],'radial',0)[0]
    z=height.enclose(left,right,v.I)
    F=[wd[2].v*er[k].v+G[k].v+(z if k==2 else v.I(0)) for k in range(3)]
    U,V=[x.v for x in au],[x.v for x in av]
    cross=[U[1]*V[2]-U[2]*V[1],U[2]*V[0]-U[0]*V[2],U[0]*V[1]-U[1]*V[0]]
    length=sum((x.sq() for x in cross),v.I(0)).sqrt()
    if np.any(length.x[0]<=0):
        raise ValueError('The outward normal denominator is not separated from zero')
    normal=[-x/length for x in cross]
    radius=sum((x.sq() for x in F),v.I(0)).sqrt()
    support=sum((x*n for x,n in zip(F,normal)),v.I(0))
    if not all(x.finite() for x in (radius,support,length)):
        raise ArithmeticError('Nonfinite complete-angle geometry enclosure')
    return dict(curvature_upper=curvature,radius_upper=float(np.max(radius.x[1])),
        support_lower=float(np.min(support.x[0])),
        normal_cross_lower=float(np.min(length.x[0])),height=scalar(z))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','source-run','physical','core-mean-certificate','core-mean-intervals',
                 'true-height-certificate','cut-trace-certificate','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--angular',type=int,default=2048)
    parser.add_argument('--exp-order',type=int,default=12)
    parser.add_argument('--metric-target',type=float,default=9.7e-7)
    parser.add_argument('--max-attempts',type=int,default=100000)
    parser.add_argument('--max-depth',type=int,default=28)
    parser.add_argument('--allow-intermediate-lambda',action='store_true')
    args=parser.parse_args()
    repo=args.repo.resolve();out=args.outdir.resolve()
    if out==repo or repo in out.parents:
        raise ValueError('Full certificate leaves must remain outside the repository')
    if (not math.isfinite(args.metric_target) or not 0<args.metric_target<=1e-6 or
            not 8<=args.exp_order<=32 or args.angular<32 or
            args.max_attempts<1 or not 1<=args.max_depth<=28):
        raise ValueError('Invalid continuous-certificate controls or changed metric gate')
    out.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    report=dict(status='validating_actual_inputs',complete=False,stages=[],progress={},
        result={},error=None,source=ref(__file__),source_run=ref(args.source_run),
        physical=ref(args.physical),BVP_invoked=False,DN_invoked=False,
        old_numeric_bounds_reused=False,complete_surface=False,
        fixed_metric_C2_convergence_paid=False,Cartesian_tail_attachment_paid=False,
        source_float_map_identified_with_explicit_C2_map=False)
    def save():
        report['seconds']=time.monotonic()-begin
        write(out/'summary.json',report)
    def event(name,**values):
        report['progress']=dict(event=name,**values)
        save()
        print(json.dumps(report['progress'],allow_nan=False),flush=True)
    save()
    try:
        scripts,helper=setup(repo)
        b,v=helper.jets,helper.prefix_mean
        run,model,loader_path,source_gate=helper.source_model(
            args.source_run.resolve(),args.allow_intermediate_lambda)
        if helper.SHORT_SHA not in run.get('frozen_source_signature',{}).values():
            raise ValueError('The actual field does not bind the reviewed original ShortBridge source')
        if sha(args.physical)!=run['physical_sha256']:
            raise ValueError('The actual accepted complete field changed')
        core,psi,lift=helper.core_intervals(args.core_mean_certificate,args.core_mean_intervals,
            args.source_run.resolve(),args.physical.resolve(),run)
        loader=module('_warm_bridge_actual_physical',
                      scripts/'resume_m3/audit_full_relative_metric.py')
        physical=loader.load_physical(args.physical)
        M=run['modes']
        if (physical.x.dtype!=np.float64 or physical.sol.c.dtype!=np.float64 or
                physical.p.dtype!=np.float64 or
                physical.sol.c.shape!=(6,len(physical.x)-1,3*M+1) or
                physical.p.shape!=(M,) or
                not all(np.all(np.isfinite(x)) for x in (physical.x,physical.sol.c,physical.p)) or
                not np.all(np.diff(physical.x)>0)):
            raise ValueError('Require the whole actual original physical quintic')
        base=helper.MeanMap(model,physical,psi,lift)
        mean=TrueBridgeJets(base,helper)
        height=HeightPrimitive(args.true_height_certificate,args.source_run,args.physical,
            args.core_mean_certificate,args.core_mean_intervals,run,base,helper)
        target=TailMatchedTarget(base,helper,scripts,args.cut_trace_certificate,
            args.source_run,args.physical,run)
        angular=max(args.angular,16*(3*M+1))
        table=angular_boxes(v,base.f.even,angular)
        pieces=BridgePieces(mean)
        geom=v.PrefixMetric(pieces,None,None,table,0.)
        gram=b.GramVerifier(mean,args.exp_order)
        grid=sorted(set(mean.grid+[target.start]+
                        [x for x in height.grid if base.entry<=x<=base.end]))
        if grid[0]!=base.entry or grid[-1]!=base.end or any(l>=r for l,r in zip(grid,grid[1:])):
            raise ValueError('The complete bridge partition is invalid')
        grid_path=out/'bridge-radial-grid.json'
        write(grid_path,[str(x) for x in grid])
        report.update(status='certifying_complete_actual_bridge',
            model_kind=run['model_kind'],homotopy=run['warm_definition']['homotopy'],
            modes=M,physical_field_dimension=3*M+1,gauge_exact=str(fq(run['gauge_q'])),
            mean_nodes=1168,literal_psi_sha256=PSI_SHA,angular_closed_boxes=angular,
            source_acceptance=source_gate,source_model_loader=ref(loader_path),
            core_mean_certificate=ref(args.core_mean_certificate),
            core_mean_intervals=ref(args.core_mean_intervals),
            true_height_certificate=ref(args.true_height_certificate),
            true_height_leaves=ref(height.leaves),
            cut_trace_certificate=ref(args.cut_trace_certificate),
            reviewed_sources={relative:ref(scripts/relative) for relative in REVIEWED},
            common_map_definition=height.record['explicit_map_definition'],
            original_frozen_source_signature=run['frozen_source_signature'],
            warm_definition=run['warm_definition'],
            exact_prefix_endpoint_algebra=base.endpoint_algebra,
            target_metric_definition=target.definition,
            target_metric_definition_sha256=target.definition_sha256,
            target_endpoint_d_intervals=target.endpoint_d_intervals,
            radial_partition=ref(grid_path),exp_order=args.exp_order,
            metric_target=args.metric_target,
            geometry_targets_exact=dict(curvature='123/10',radius='67/50',support='87/1000'),
            normal_orientation='-(F_s|theta cross F_theta/a_star)/length',
            metric_directly_of_explicit_true_C2_map=True,
            GL64_radius_with_assigned_derivatives_used=False,
            all_angles_covered_without_sampling_assumption=True,
            height_from_same_true_radial_primitive=True)
        event('actual_bridge_inputs_bound',modes=M,radial_pieces=len(grid)-1,angular_boxes=angular)
        todo=[(l,r,0) for l,r in zip(grid[:-1],grid[1:])][::-1]
        attempts=accepted=splits=domain=0
        covered=Q(0)
        maxima=dict(metric_star=0.,metric_target=0.,curvature_upper=0.,radius_upper=0.,
                    target_radius_correction_upper=0.,target_metric_change_upper=0.)
        minima=dict(support_lower=None,normal_cross_lower=None,root_lower=None,
                    target_radius_lower=None)
        failed=None
        leaves=out/'continuous-bridge-leaves.jsonl.gz'
        last_event=time.monotonic()
        with gzip.open(leaves,'wt') as stream:
            while todo:
                if attempts>=args.max_attempts:
                    left,right,depth=todo[-1]
                    failed=dict(left_exact=str(left),right_exact=str(right),depth=depth,
                        reason='Absolute radial-box attempt budget reached')
                    break
                left,right,depth=todo.pop()
                attempts+=1
                row=None
                try:
                    star,meta,_=gram.enclose(left,right)
                    adjusted,transfer=target.transfer(left,right,meta['amin'],star)
                    if not all(math.isfinite(x) for x in (star,adjusted)) or not 0<=star<1:
                        raise ArithmeticError('No positive actual first-fundamental-form bound')
                    geometric=geometry(v,geom,table,mean,height,left,right,star)
                    row=dict(metric_star=star,metric_target=adjusted,
                        root_lower=meta['root_min'],**transfer,**geometric)
                    passed=(adjusted<=args.metric_target and
                        fq(geometric['curvature_upper'])<Q(123,10) and
                        fq(geometric['radius_upper'])<Q(67,50) and
                        fq(geometric['support_lower'])>Q(87,1000))
                    reason='One or more unchanged continuous metric/geometry targets remain unresolved'
                except (ValueError,ArithmeticError,FloatingPointError) as exc:
                    passed=False;reason=str(exc);domain+=1
                if passed:
                    covered+=right-left
                    accepted+=1
                    for key in maxima:
                        maxima[key]=max(maxima[key],row[key])
                    for key in minima:
                        minima[key]=row[key] if minima[key] is None else min(minima[key],row[key])
                    stream.write(json.dumps(dict(left_exact=str(left),right_exact=str(right),
                        depth=depth,**row),separators=(',',':'),allow_nan=False)+'\n')
                elif depth>=args.max_depth or attempts>=args.max_attempts:
                    failed=dict(left_exact=str(left),right_exact=str(right),depth=depth,
                                reason=reason,last_enclosure=row)
                    break
                else:
                    mid=(left+right)/2
                    todo.extend(((mid,right,depth+1),(left,mid,depth+1)))
                    splits+=1
                if time.monotonic()-last_event>=20:
                    event('continuous_bridge_progress',attempts=attempts,accepted=accepted,
                          splits=splits,pending=len(todo),maxima=maxima,minima=minima)
                    last_event=time.monotonic()
        complete=(failed is None and not todo and covered==base.end-base.entry)
        report.update(status=('complete_actual_bridge_metric_geometry_certified' if complete else
                              'actual_bridge_metric_geometry_unresolved'),
            complete=complete,actual_leaf_record=ref(leaves),failed_cell=failed,
            result=dict(accepted_cells=accepted,attempted_cells=attempts,split_cells=splits,
                interval_domain_bisections=domain,remaining_cells=len(todo),
                covered_length_exact=str(covered),required_length_exact=str(base.end-base.entry),
                maxima=maxima,minima=minima,
                complete_true_bridge_metric_and_geometry=complete,
                target_metric_matches_declared_true_tail_two_jet=complete,
                original_inlet_repair_or_prefix_support_paid=False,
                full_tail_geometry_or_global_reach_paid=False))
        save()
        print(json.dumps(dict(status=report['status'],complete=complete,
              result=report['result'],failed_cell=failed),allow_nan=False),flush=True)
        return 0 if complete else 1
    except Exception as exc:
        report.update(status='error',complete=False,error=repr(exc),traceback=traceback.format_exc())
        save()
        print(json.dumps(dict(status='error',error=repr(exc))),flush=True)
        return 1


if __name__=='__main__':
    raise SystemExit(main())

