#!/usr/bin/env python3
"""Whole-half fixed-g solve consuming an actual nested radial/angular warm field.

New source derived from the frozen R243 solver. Only the transfer reader
and corresponding report labels change; it explicitly accepts the exact
Boehm inclusion followed by a certified nonzero binary storage error.
The same whole-domain three-row objective, physical J/JT, LSMR diagnostics,
line-search checks, all endpoint jets and independent observers remain.
This consumer still requires simple radial knots; repeated-knot production
is not implied by the separately checked finite transfer kernel.
"""
from __future__ import annotations
import argparse,gc,gzip,hashlib,importlib.util,io,json,resource,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import lsmr

HERE=Path(__file__).resolve().parent;LD=np.longdouble
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def exact_key(x):return str(Q(*LD(x).as_integer_ratio()))
def ld(q):return LD(q.numerator)/LD(q.denominator)


class WholeChart:
    def __init__(self,prefix,background):
        self.prefix=prefix;self.background=background;self.S=prefix.total
        self.c,self.cuff=background.cut,background.cuff;self.h=self.c-self.cuff;self.total=self.S+self.h
        k=2/np.sqrt(LD(5));a=1-k;b=28*self.h/(25*self.c)
        self.co=np.asarray([0,k,-b/2,6*a+3*b/2,-8*a-3*b/2,3*a+b/2],LD)
        self.first=self.co[1:]*np.arange(1,6);self.second=self.first[1:]*np.arange(1,5)
        self.cache={}

    def radius(self,z):
        q=LD(z)*self.total;t=np.clip((q-self.S)/self.h,0,1)
        R=np.polynomial.polynomial.polyval(t,self.co)
        rp=-np.polynomial.polynomial.polyval(t,self.first)
        rpp=-np.polynomial.polynomial.polyval(t,self.second)/self.h
        r=self.c-self.h*R
        if q==self.S:r=self.c
        if q==self.total:r=self.cuff;rp=LD(-1);rpp=LD(0)
        return np.clip(r,self.cuff,self.c),rp,rpp

    def radial_packet(self,z):
        key=exact_key(z)
        if key in self.cache:return self.cache[key]
        if LD(z)*self.total<=self.S:answer=(LD(1),LD(0),None,None)
        else:
            r,rp,rpp=self.radius(z);w,wr,drop,*rest=self.background.point(r);root=np.sqrt(1+w*w)
            H=-rp*root;Hq=-rpp*root-rp*rp*w*wr/root
            if H<=0:raise ArithmeticError('Common radial chart lost positivity')
            answer=(H,Hq,r,(w,wr,drop))
        self.cache[key]=answer;return answer

    def scales(self,z):
        rows=[self.radial_packet(x) for x in z]
        return np.asarray([r[0] for r in rows],float),np.asarray([r[1] for r in rows],float)

    def inverse_radius(self,r):
        target=(self.c-LD(r))/self.h;lo,hi=LD(0),LD(1);x=np.clip(target,0,1)
        for unused in range(50):
            value=np.polynomial.polynomial.polyval(x,self.co)-target
            if abs(value)<LD('2e-20'):break
            if value>0:hi=x
            else:lo=x
            slope=np.polynomial.polynomial.polyval(x,self.first);proposal=x-value/slope
            x=proposal if lo<proposal<hi else (lo+hi)/2
        return (self.S+self.h*x)/self.total


def quadrature(mesh,gauss,chart):
    x,w=np.polynomial.legendre.leggauss(gauss)
    z=((mesh[:-1]+mesh[1:])[:,None]/2+(mesh[1:]-mesh[:-1])[:,None]*x/2).ravel()
    weights=((mesh[1:]-mesh[:-1])[:,None]*w/2*float(chart.total)).ravel()
    H,unused=chart.scales(z)
    return z,weights*H


def definition(args,joint,bg_module):
    notes=args.scripts.parent/'notes';meta_path=notes/joint.ad.base.META_NAME
    bridge_path=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    manifest=notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    calibrations=notes/'2026-11-09-db6f-tail-finite-source-calibrations.json'
    meta=json.loads(meta_path.read_text());bridge=json.loads(bridge_path.read_text())
    with np.load(io.BytesIO(gzip.decompress(args.data.read_bytes())),allow_pickle=False) as raw:mesh=np.asarray(raw['mesh'],LD)
    if sha(args.data)!=joint.ad.base.DATA_SHA:raise ValueError('Wrong original prefix data')
    prefix=joint.ExactMetric(meta,bridge,mesh[-1])
    bg=bg_module.OriginalTailBackground(manifest,calibrations,LD(args.background_tolerance))
    chart=WholeChart(prefix,bg)
    return notes,meta_path,bridge_path,meta,mesh,chart


def prepare(args,joint,bg_module):
    if args.out.exists():raise FileExistsError('Fresh preparation output required')
    began=time.monotonic();notes,meta_path,bridge_path,meta,native,chart=definition(args,joint,bg_module)
    prefix=chart.prefix
    pm=np.unique(np.r_[np.linspace(0,1,args.prefix_elements+1),np.asarray(prefix.breakpoints,float),
                        np.asarray(meta['chart']['knots'],float),.75,float(native[meta['correction_start_index']]/native[-1])])
    knots=list(np.asarray(pm,LD)*chart.S/chart.total)
    knots+=list((chart.S+chart.h*np.linspace(0,1,args.tail_elements+1,dtype=LD))/chart.total)
    for row in chart.background.outer_order:
        if row.n>=args.tail_depth:continue
        for r in (row.r_left,row.r_right):knots.append(chart.inverse_radius(np.clip(r,chart.cuff,chart.c)))
        if row.n<8:
            for x in chart.background.source.raw_critical_nodes(row.n,row.j):
                partial=row.partial(x);r=row.r_left+partial[0]+chart.background.alpha*partial[1]
                knots.append(chart.inverse_radius(np.clip(r,chart.cuff,chart.c)))
    manifest=json.loads((notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json').read_text())
    inner=ld(Q(manifest['radialGeometry']['innerAnchor']));knots.append(chart.inverse_radius(inner))
    mesh=np.unique(np.asarray(knots,float));mesh=mesh[(mesh>=0)&(mesh<=1)]
    mesh[0]=0;mesh[-1]=1;mesh=mesh[np.r_[True,np.diff(mesh)>1e-14]]
    radii={exact_key(chart.c),exact_key(chart.cuff),exact_key(inner)}
    grids=[]
    for gauss in (args.gauss,args.gauss+2):
        z,weights=quadrature(mesh,gauss,chart);grids.append(len(z))
        for point in z:
            if LD(point)*chart.total>chart.S:radii.add(exact_key(chart.radius(point)[0]))
    query_path=Path(str(args.out)+'.queries.json')
    query_path.write_text(json.dumps({'schema':'6a65-original-M12-whole-half-radial-queries-v1',
                                      'radii':sorted(radii,key=Q)},indent=2)+'\n')
    record={'schema':'6a65-original-M12-whole-half-grid-v1','script_sha256':sha(__file__),
            'joint_source_sha256':sha(Path(joint.__file__)),'background_source_sha256':sha(Path(bg_module.__file__)),
            'data_sha256':sha(args.data),'common_meta_sha256':sha(meta_path),'bridge_sha256':sha(bridge_path),
            'unit_mesh':mesh.tolist(),'prefix_elements_requested':args.prefix_elements,'tail_elements_requested':args.tail_elements,
            'tail_source_depth_in_mesh':args.tail_depth,'gauss':args.gauss,'angular':args.angular,'order':args.order,
            'background_tolerance':args.background_tolerance,'query_file_sha256':sha(query_path),
            'physical_prefix_length_numerical':str(chart.S),'material_chart_length_numerical':str(chart.total),
            'true_cuff_exact':exact_key(chart.cuff),'background':chart.background.receipt()}
    args.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'prepared_grid_sha256':sha(args.out),'query_file':str(query_path),'query_file_sha256':sha(query_path),
                      'elements':len(mesh)-1,'radial_nodes':grids,'tail_queries':len(radii),
                      'unknowns':(len(mesh)-2)*(3*args.order+2),'true_cuff_exact':exact_key(chart.cuff),
                      'internal_common_cut_free':True,'seconds':time.monotonic()-began}),flush=True)


class TailQueries:
    def __init__(self,report,cache):
        record=json.loads(Path(report).read_text())
        if sha(cache)!=record['endpoint_cache_sha256']:raise ValueError('Tail query cache identity mismatch')
        with np.load(cache,allow_pickle=False) as data:
            self.coefficients=data['coefficients'].copy();self.pm=data['planar_modes'].copy();self.hm=data['height_modes'].copy()
            self.lookup={str(k):i for i,k in enumerate(data['query_fraction'])}
        self.record=record;self.cache_path=Path(cache)

    def coefficient(self,r):
        key=exact_key(r)
        if key not in self.lookup:raise ValueError('No exact cache query at radius '+key)
        return self.coefficients[self.lookup[key]]

    def apply(self,a,u,order):
        P=len(self.pm);m=np.asarray(self.pm,LD);h=np.asarray(self.hm,LD)
        angle=m[:,None]*u[None,:];factor=(1j*m.astype(np.clongdouble))**order
        c=np.sum(a[:P,None]*factor[:,None]*(np.cos(angle)+1j*np.sin(angle)),axis=0)
        angle_z=h[:,None]*u[None,:]
        vertical=np.sum(a[P:,None]*np.real((1j*h.astype(np.clongdouble))[:,None]**order*(np.cos(angle_z)+1j*np.sin(angle_z))),axis=0)
        return np.stack((c.real,c.imag,-vertical),axis=-1)


class WholePosition:
    def __init__(self,src,central,chart,tail,joint):
        self.src,self.central,self.chart,self.tail,self.joint=src,central,chart,tail,joint
        self.prefix_cache={};self.angular_cache={}

    def angular(self,N):
        if N not in self.angular_cache:self.angular_cache[N]=self.joint.bvp.central_chart(self.central,N)
        return self.angular_cache[N]

    def tail_point(self,r,N):
        u,rho,rhop=self.angular(N);u=np.asarray(u,LD);rho=np.asarray(rho,LD);rhop=np.asarray(rhop,LD)
        c=self.tail.coefficient(r);w,wr,drop,*rest=self.chart.background.point(r)
        er=np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1)
        et=np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)),axis=-1)
        X=self.tail.apply(c[0],u,0)+r*er;X[:,2]+=self.src.cut_height+drop
        Xr=self.tail.apply(c[1],u,0)+er;Xr[:,2]-=w
        Xu=self.tail.apply(c[0],u,1)+r*et
        Xrr=self.tail.apply(c[2],u,0);Xrr[:,2]-=wr
        Xru=self.tail.apply(c[1],u,1)+et;Xuu=self.tail.apply(c[0],u,2)-r*er
        E=1+w*w;rs=-1/np.sqrt(E);rss=-w*wr/(E*E)
        p=np.stack((X,rs*Xr,Xu*rho[:,None],rs*rs*Xrr+rss*Xr,
                    rs*Xru*rho[:,None],Xuu*rho[:,None]**2+Xu*rhop[:,None]))
        return np.asarray(p,float),np.asarray(r*rho,float)

    def __call__(self,z,N):
        out=np.empty((len(z),6,N,3));bb=np.empty((len(z),N))
        prefix=np.asarray(z,LD)*self.chart.total<=self.chart.S
        if np.any(prefix):
            x=np.asarray(z,LD)[prefix]*self.chart.total/self.chart.S
            out[prefix],bb[prefix]=self.joint.background(self.src,self.central,x,N,self.prefix_cache)
        for i in np.flatnonzero(~prefix):out[i],bb[i]=self.tail_point(self.chart.radius(z[i])[0],N)
        return out,bb


def basis_for(joint,mesh,order,chart):
    class Basis(joint.bvp.Basis):
        def __init__(self):
            super().__init__(mesh,order);self.full_nb=self.nb;self.nb-=6
        def matrices(self,z):
            H,Hq=chart.scales(z);T=float(chart.total)
            p0=self.spline(z)[:,3:-3];p1=self.spline(z,nu=1)[:,3:-3];p2=self.spline(z,nu=2)[:,3:-3]
            return [csr_matrix(p0),csr_matrix(p1/(T*H[:,None])),
                    csr_matrix(p2/(T*T*H[:,None]**2)-p1*Hq[:,None]/(T*H[:,None]**3))]
    return Basis()


def actual_warm_field(args,basis):
    """Consume the actual nested transfer, including its nonzero storage error."""
    if args.warm_field is None or args.warm_receipt is None:
        raise ValueError('Actual nested field and its source-bound storage receipt are required')
    receipt=json.loads(args.warm_receipt.read_text())
    transfer_source=args.scripts/'6a65-m12-exact-radial-angular-warm-transfer.py'
    if receipt.get('schema')!='6a65-M12-exact-nested-space-warm-transfer-v1':
        raise ValueError('The explicit radial/angular transfer schema is required')
    if sha(transfer_source)!='cd2eea7beba4f6902067ff0952487bf1e426e13790150690458fe6dcba3ed0ca':
        raise ValueError('Pinned nested-transfer source changed')
    for key,path in [('script_sha256',transfer_source),('new_grid_sha256',args.grid),
                     ('transferred_field_sha256',args.warm_field)]:
        if receipt[key]!=sha(path):raise ValueError('Nested input identity mismatch: '+key)
    for key in ('same_original_g','exact_space_inclusion_before_binary_storage',
                'D3_and_ambient_reflection_retained',
                'complete_central_and_true_cuff_zero_two_jets_retained'):
        if receipt.get(key) is not True:raise ValueError('Nested input property missing: '+key)
    expected={str((r,j)) for r in range(3) for j in range(3-r)}
    for key in ('binary_storage_native_six_jet_error','binary_storage_physical_s_material_u_six_jet_error'):
        if set(receipt[key])!=expected:raise ValueError('Complete continuous storage six-jet budget required')
        for entry in receipt[key].values():
            if not isinstance(entry,dict) or Q(entry['upper_exact'])<0:
                raise ValueError('The actual nonnegative rational storage bound is required')
    for key in ('binary_storage_target_differential_Frobenius_upper',
                'binary_storage_target_scaled_coordinate_Hessian_upper'):
        if Q(receipt[key]['upper_exact'])<0:raise ValueError('Invalid physical storage budget')
    if receipt.get('new_nonlinear_solve_executed') is not False or receipt.get('exact_isometry_proved') is not False:
        raise ValueError('A transfer receipt must not claim a new solved field or exact isometry')
    with np.load(args.warm_field,allow_pickle=False) as raw:
        coeff=raw['coefficients'].copy()
        if not np.array_equal(raw['unit_knots'],basis.knots):
            raise ValueError('Actual transferred radial knots changed')
        if not np.array_equal(raw['planar_modes'],basis.pm) or not np.array_equal(raw['vertical_modes'],basis.zm):
            raise ValueError('Actual transferred complete Fourier modes changed')
    if coeff.dtype!=np.float64 or coeff.shape!=(basis.nb,basis.na) or not np.all(np.isfinite(coeff)):
        raise ValueError('The complete finite actual warm coefficient matrix is required')
    if list(coeff.shape)!=receipt['new_field_shape']:
        raise ValueError('The nested transfer receipt has a different output shape')
    return coeff,receipt


def physical_gradient_from_old_coordinates(op,gradient):
    """If T=L_S^-T, recover g from the actual coordinate gradient T^T g."""
    value=np.asarray(gradient).reshape(op.basis.na,op.basis.nb)
    out=np.zeros((op.basis.nb,op.basis.na))
    for a,k in enumerate(op.basis.modes):
        lower=op.factors[abs(int(k))][0]
        for d in range(op.bandwidth+1):
            out[d:,a]+=lower[d,:op.basis.nb-d]*value[a,:op.basis.nb-d]
    return out


def solve(args,joint,bg_module):
    if any(path.exists() for path in (args.out,Path(str(args.out)+'.field.npz'),Path(str(args.out)+'.warm-observed.json'))):
        raise FileExistsError('Fresh warm whole-half outputs required')
    began=time.monotonic();record=json.loads(args.grid.read_text())
    args.background_tolerance=record['background_tolerance']
    notes,meta_path,bridge_path,meta,native,chart=definition(args,joint,bg_module)
    for key,path in [('data_sha256',args.data),('common_meta_sha256',meta_path),('bridge_sha256',bridge_path),
                     ('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg_module.__file__))]:
        if record[key]!=sha(path):raise ValueError('Grid source changed: '+key)
    tail=TailQueries(args.query_report,args.query_cache)
    if tail.record['query_file_sha256']!=record['query_file_sha256']:raise ValueError('Query grid identity changed')
    src=joint.CommonCutSource(args.data,meta_path,bridge_path,args.query_report,args.query_cache)
    unused,central_c=joint.ad.exact_section(args.data,Q(0));central=joint.ad.NativeCurve(central_c,512,32)
    position=WholePosition(src,central,chart,tail,joint);mesh=np.asarray(record['unit_mesh'])
    order,N,gauss=record['order'],record['angular'],record['gauss']
    if N<=2*(3*order+1):raise ValueError('Aliased angular correction basis')
    if 'unit_knots' in record:raise ValueError('This nested production entry currently supports only simple radial knots')
    basis=basis_for(joint,mesh,order,chart);z,weights=quadrature(mesh,gauss,chart)
    coeff,warm_receipt=actual_warm_field(args,basis);warm_initial_coeff=coeff.copy();stream=joint.stream
    initial=stream.observe(basis,z,weights,position,coeff,N,args.block)
    print(json.dumps({'initial_entire_half':initial,'unknowns':coeff.size,'radial_nodes':len(z),
                      'common_cut_fixed':False,'true_cuff':str(chart.cuff)}),flush=True)
    rows=[];adjoint_error=None
    for step in range(args.newton):
        op=stream.StreamingLinearized(basis,z,weights,position,coeff,N,args.block)
        if step==0:
            rng=np.random.default_rng(8128);x=rng.normal(size=op.shape[1]);y=rng.normal(size=op.shape[0])
            a=np.dot(op.matvec(x),y);b=np.dot(x,op.rmatvec(y));adjoint_error=abs(a-b)/max(1,abs(a),abs(b))
            if adjoint_error>1e-10:raise ArithmeticError('Whole-half J/JT mismatch')
            del x,y;gc.collect()
        scale=1e9;rhs=-op.residual.ravel()*scale;del op.residual
        solution=lsmr(op.operator,rhs,atol=1e-10,btol=1e-10,conlim=1e12,maxiter=args.iterations)
        if not np.all(np.isfinite(solution[0])):raise ArithmeticError('Nonfinite actual LSMR direction')
        change=op.unpack(solution[0])/scale;before=op.statistics
        linearized_scaled=op.matvec(solution[0])-rhs
        coordinate_normal=op.rmatvec(linearized_scaled)/scale
        coordinate_initial_gradient=op.rmatvec(-rhs)/scale
        physical_normal=physical_gradient_from_old_coordinates(op,coordinate_normal)
        physical_initial_gradient=physical_gradient_from_old_coordinates(op,coordinate_initial_gradient)
        physical_gradient_norm=float(np.linalg.norm(physical_initial_gradient))
        physical_normal_norm=float(np.linalg.norm(physical_normal))
        jv=(linearized_scaled+rhs)/scale
        slope=float(np.dot(-rhs/scale,jv))
        normal_report={'lsmr_operator_norm_estimate':float(solution[5]),
            'lsmr_coordinate_normal_norm_estimate':float(solution[4])/scale,
            'actual_coordinate_normal_norm':float(np.linalg.norm(coordinate_normal)),
            'actual_initial_coordinate_gradient_norm':float(np.linalg.norm(coordinate_initial_gradient)),
            'actual_physical_normal_norm':physical_normal_norm,
            'actual_initial_physical_gradient_norm':physical_gradient_norm,
            'actual_relative_physical_normal_norm':physical_normal_norm/max(np.finfo(float).tiny,physical_gradient_norm),
            'actual_physical_normal_maximum':float(np.max(np.abs(physical_normal))),
            'actual_linearized_residual_norm':float(np.linalg.norm(linearized_scaled))/scale,
            'actual_unregularized_direction_slope':slope,
            'predicted_unregularized_energy_decrease':float(-2*slope-np.dot(jv,jv)),
            'physical_coefficient_step_norm':float(np.linalg.norm(change)),
            'lsmr_coordinate_step_norm':float(solution[7])/scale,
            'lsmr_convergence_code_reached':int(solution[1]) in (1,2,4,5),
            'linear_target_regularization':0.,
            'all_Gram_rows_and_cross_channel_couplings_retained':True}
        del op,rhs,linearized_scaled,coordinate_normal,coordinate_initial_gradient
        del physical_normal,physical_initial_gradient,jv
        gc.collect()
        attempts=[];accepted=None
        for alpha in (1.,.5,.25,.125,.0625):
            stat=stream.observe(basis,z,weights,position,coeff+alpha*change,N,args.block);attempts.append({'alpha':alpha,**stat})
            if stat['weighted_energy']<before['weighted_energy'] and stat['metric_peak']<=1.05*before['metric_peak']:
                accepted=alpha;coeff+=alpha*change;break
        row={'step':step,'lsmr_stop':int(solution[1]),'lsmr_iterations':int(solution[2]),'lsmr_residual':float(solution[3])/scale,
             'condition_estimate':float(solution[6]),'accepted_alpha':accepted,'attempts':attempts,
             'actual_linear_solver_diagnostics':normal_report}
        rows.append(row);print(json.dumps(row),flush=True)
        if accepted is None:break
    oz,ow=quadrature(mesh,gauss+2,chart)
    old_observation=stream.observe(basis,oz,ow,position,np.zeros_like(coeff),2*N,args.block)
    warm_observation=stream.observe(basis,oz,ow,position,warm_initial_coeff,2*N,args.block)
    new_observation=stream.observe(basis,oz,ow,position,coeff,2*N,args.block)
    endpoint_changes=[float(np.max(abs(B@coeff))) for B in basis.matrices([0.,1.])]
    # Evaluate the actual original common-cut seam directly from both maps.
    pp,bp=joint.background(src,central,[LD(1)],2*N,position.prefix_cache)
    pt,bt=position.tail_point(chart.c,2*N)
    seam=[float(np.max(np.linalg.norm(pp[0,j]-pt[j],axis=-1))) for j in range(6)]
    initial_result=Path(str(args.out)+'.warm-observed.json')
    warm_record={'schema':'6a65-M12-nested-warm-field-independent-observation-v1',
        'script_sha256':sha(__file__),'R243_parent_core_sha256':'e58d4f3c036a1ec4b78a3c7022ac6e6677e9b7bac4c3be8eea43ed8665a2ae81','grid_sha256':sha(args.grid),
        'field_sha256':sha(args.warm_field),'query_report_sha256':sha(args.query_report),
        'query_cache_sha256':sha(args.query_cache),'nested_transfer_receipt_sha256':sha(args.warm_receipt),
        'independent_observer_before':old_observation,'independent_observer_after':warm_observation,
        'original_exact_metric_unchanged':True,'all_internal_interfaces_free':True,
        'true_flat_cuff_included':True,'full_half_including_finite_tail_and_deep_collar':True,
        'new_nonlinear_field_solved_in_this_record':False,
        'exact_space_inclusion_before_binary_storage':True,
        'actual_saved_warm_field_and_finer_observation_only':True,
        'binary_storage_error_receipted_and_not_called_zero':True,'exact_isometry_proved':False}
    initial_result.write_text(json.dumps(warm_record,indent=2,allow_nan=False)+'\n')
    field=Path(str(args.out)+'.field.npz')
    np.savez_compressed(field,coefficients=coeff,unit_knots=basis.knots,planar_modes=basis.pm,vertical_modes=basis.zm)
    out={'schema':'6a65-original-M12-entire-half-fixed-g-Cartesian-BVP-v1','script_sha256':sha(__file__),
         'R243_parent_core_sha256':'e58d4f3c036a1ec4b78a3c7022ac6e6677e9b7bac4c3be8eea43ed8665a2ae81',
         'grid_sha256':sha(args.grid),'query_report_sha256':sha(args.query_report),'query_cache_sha256':sha(args.query_cache),
         'joint_source_sha256':sha(Path(joint.__file__)),'stream_operator_sha256':sha(Path(stream.__file__)),
         'background_source_sha256':sha(Path(bg_module.__file__)),'field_sha256':sha(field),
         'source':src.source_identity,'background':chart.background.receipt(),'order':order,'angular':N,'gauss':gauss,
         'elements':len(mesh)-1,'unknowns':int(coeff.size),'analytic_adjoint_relative_error':float(adjoint_error),
         'initial_training_entire_half':initial,'rows':rows,'independent_observer_before':old_observation,
         'independent_observer_initial_warm_field':warm_observation,
         'warm_field_sha256':sha(args.warm_field),'warm_transfer_receipt_sha256':sha(args.warm_receipt),
         'nested_initial_transfer':warm_receipt,'actual_warm_field_used_without_reset':True,
         'warm_observed_result_sha256':sha(initial_result),
         'accepted_steps_this_refinement':sum(row['accepted_alpha'] is not None for row in rows),
         'independent_observer_after':new_observation,'independent_peak_material_q':float(oz[new_observation['peak_radial_index']]*chart.total),
         'central_and_true_cuff_correction_jets_max':endpoint_changes,'original_common_cut_actual_six_jet_differences':seam,
         'original_exact_metric_unchanged':True,'all_internal_interfaces_free':True,'true_flat_cuff_included':True,
         'full_half_including_finite_tail_and_deep_collar':True,'continuous_metric_certificate':False,
         'exact_isometry_proved':False,'whole_family_reach_certified':False,
         'resident_high_water_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('stage',choices=['prepare','solve'])
    ap.add_argument('--scripts',type=Path,default=HERE);ap.add_argument('--data',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--prefix-elements',type=int,default=80)
    ap.add_argument('--tail-elements',type=int,default=64);ap.add_argument('--tail-depth',type=int,default=12)
    ap.add_argument('--gauss',type=int,default=6);ap.add_argument('--angular',type=int,default=384);ap.add_argument('--order',type=int,default=32)
    ap.add_argument('--background-tolerance',default='2e-18');ap.add_argument('--grid',type=Path)
    ap.add_argument('--query-report',type=Path);ap.add_argument('--query-cache',type=Path)
    ap.add_argument('--warm-field',type=Path);ap.add_argument('--warm-receipt',type=Path)
    ap.add_argument('--iterations',type=int,default=800);ap.add_argument('--newton',type=int,default=1)
    ap.add_argument('--block',type=int,default=24);args=ap.parse_args()
    joint=load('entire_half_prefix',args.scripts/'6a65-m12-global-common-cut-position-recovered.py')
    bg_path=HERE/'6a65-m12-original-tail-background.py'
    if not bg_path.exists():bg_path=args.scripts/bg_path.name
    bg_module=load('entire_half_background',bg_path)
    if args.stage=='prepare':prepare(args,joint,bg_module)
    else:
        if not all((args.grid,args.query_report,args.query_cache)):raise ValueError('Solve requires grid and exact query cache')
        solve(args,joint,bg_module)


if __name__=='__main__':main()
