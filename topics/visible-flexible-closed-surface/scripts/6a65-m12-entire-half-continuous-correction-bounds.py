#!/usr/bin/env python3
"""Continuous exact-rational bounds for a saved M12 Cartesian correction.

The saved binary64 coefficients and knots define one exact quintic field.
Differentiated B-spline control polygons and their nonnegative partition
of unity bound every point, including all cell interiors. Fourier bounds
are coefficient absolute sums. The original true-cuff chart and original
central material angle are then differentiated analytically.

The solver's reference includes a deterministic central two-jet correction.
That correction is bounded separately against the actual R21 common-cut
map; it is never silently omitted. These are continuous displacement/jet
bounds, not by themselves a new complete metric or reach certificate.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,io,json,math,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

DATA_SHA='359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0'
META_SHA='253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'
BRIDGE_SHA='1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa'
MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(v):return Q.from_float(float(v))
def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def add(target,key,value):target[key]=target.get(key,Q(0))+value
def convolution(a,b):
    out={}
    for k,x in a.items():
        for j,y in b.items():add(out,k+j,x*y)
    return {k:v for k,v in out.items() if v}
def planar(c):
    M=(len(c)-2)//3;out={1:c[0]}
    for j in range(1,M+1):out[1+3*j]=(c[j]+c[M+j])/2;out[1-3*j]=(c[j]-c[M+j])/2
    return {k:v for k,v in out.items() if v}
def l1(a,order=0):return sum((abs(k)**order*abs(v) for k,v in a.items()),Q(0))
def outer(q):
    """A rational upward endpoint; never a rounded binary64 certificate."""
    if q<0:raise ValueError('Upper endpoints are for nonnegative bounds')
    scale=10**24;n=(q.numerator*scale+q.denominator-1)//q.denominator
    return Q(n,scale)
def serialize(values):
    return {key:{'upper_exact':str(outer(value)),'display':float(outer(value))} for key,value in values.items()}


def derivative_controls(knots,controls,degree):
    result=[]
    for i in range(len(controls)-1):
        den=knots[i+degree+1]-knots[i+1]
        if den<=0:raise ValueError('Degenerate derivative-control support')
        result.append([degree*(b-a)/den for a,b in zip(controls[i],controls[i+1])])
    return knots[1:-1],result,degree-1


def control_bounds(knots,coefficients,modes):
    n=len(knots)-6;na=len(modes)
    if len(coefficients)!=n-6 or any(len(row)!=na for row in coefficients):raise ValueError('Wrong full zero-trace basis shape')
    zeros=[Q(0)]*na;control=[zeros.copy() for i in range(3)]+coefficients+[zeros.copy() for i in range(3)]
    tables=[];current_knots=knots;degree=5
    endpoints=[]
    for d in range(3):
        row_bounds={j:[sum((abs(c)*abs(k)**j for c,k in zip(row,modes)),Q(0)) for row in control] for j in range(3-d)}
        tables.append({j:max(rows,default=Q(0)) for j,rows in row_bounds.items()})
        endpoints.append(all(v==0 for v in control[0]+control[-1]))
        if d<2:current_knots,control,degree=derivative_controls(current_knots,control,degree)
    if not all(endpoints):raise ArithmeticError('Central/cuff correction is not exactly zero to order two')
    return {(d,j):v for d,row in enumerate(tables) for j,v in row.items()},endpoints


def central_arclength_residual(metric,e,Jmin,rhomin,cert,panels=2048):
    """Rigorous total and partial primitives of H=|gamma'|-rho.

    The small exact Fourier defect D=|gamma'|^2-rho^2 is subtracted before
    interval evaluation. Derivative bounds follow by differentiating
    2*rho*H+H^2=D; every Simpson remainder is explicit.
    """
    I=cert.I;pi=cert.pi_interval();width=2*pi/panels
    D=[l1(metric,k) for k in range(5)];H=[D[0]/(Jmin+rhomin)]
    for n in range(1,5):
        numerator=D[n]+2*sum((math.comb(n,k)*(3**k*abs(e))*H[n-k] for k in range(1,n+1)),Q(0))
        numerator+=sum((math.comb(n,k)*H[k]*H[n-k] for k in range(1,n)),Q(0))
        H.append(numerator/(2*Jmin))
    if any(metric.get(-k,Q(0))!=v for k,v in metric.items()):raise ArithmeticError('Central speed defect is not real-even')
    trig=[]
    for j in range(2*panels):
        numerator=j if j<=panels else j-2*panels
        trig.append(cert.sincos(pi*Q(numerator,panels)))
    modes=[(k,I(2*v)) for k,v in metric.items() if k>0 and v];d0=I(metric.get(0,Q(0)));ee=I(e)
    values=[];node_hash=hashlib.sha256()
    for j in range(2*panels):
        rho=1-ee*trig[(3*j)%(2*panels)][1]
        defect=d0
        for k,c in modes:defect+=c*trig[(k*j)%(2*panels)][1]
        speed=(rho.square()+defect).sqrt();value=defect/(speed+rho)
        values.append(value);node_hash.update((str(j)+':'+str(value.lo)+':'+str(value.hi)+'\n').encode())
    values.append(values[0]);sums=[I(0)]
    for j in range(panels):sums.append(sums[-1]+width*(values[2*j]+4*values[2*j+1]+values[2*j+2])/6)
    local_error=cert.upper_i(width**5*I(H[4])/2880)
    full_error=local_error*panels
    integral=sums[-1]+I.raw(-full_error.hi,full_error.hi)
    arc=1+integral/(2*pi)
    if arc.lo<=0:raise ArithmeticError('Residual arclength proof missed positivity')
    arc_dev=max(abs(arc.lower()-1),abs(arc.upper()-1));lift=Q(0)
    for j,total in enumerate(sums):
        theta=2*pi*Q(j,panels);sn=trig[(6*j)%(2*panels)][0]
        old_angle=theta-ee*sn/3;err=local_error*j
        primitive=total+I.raw(-err.hi,err.hi)
        difference=(primitive-(arc-1)*old_angle)/arc
        lift=max(lift,Q(difference.absupper(),cert.SCALE))
    # Nearest panel endpoint is at angular distance <=width/2.
    lift_derivative=(H[0]+arc_dev*(1+abs(e)))/arc.lower()
    lift+=width.upper()*lift_derivative/2
    return arc.lower(),arc.upper(),lift/rhomin,{
        'panels':panels,'integer_bits':cert.BITS,'interval_source_sha256':sha(cert.__file__),
        'exact_H_derivative_upper':serialize({str(j):v for j,v in enumerate(H)}),
        'mean_arc_radius_lower_exact':str(arc.lower()),'mean_arc_radius_upper_exact':str(arc.upper()),
        'whole_primitive_simpson_remainder_upper':str(outer(full_error.upper())),
        'degree_one_angle_lift_difference_upper':str(outer(lift)),
        'old_inverse_angle_shift_upper':str(outer(lift/rhomin)),
        'all_point_interval_rows_sha256':node_hash.hexdigest(),
        'continuous_between_nodes_by_derivative_bound':True}


def exact_central_constants(data,meta,bridge,screen,scripts):
    with np.load(io.BytesIO(gzip.decompress(Path(data).read_bytes())),allow_pickle=False) as raw:
        mesh=raw['mesh'];jets=raw['jets'][:,0,:]
    rows=[[fq(x) for x in row] for row in jets];c=rows[0];M=(len(c)-2)//3
    if any(c[2*M+1:]) or rows[1][:-1]!=[Q(0)]*(len(c)-1) or rows[1][-1]!=1:
        raise ValueError('Unexpected central curve or native first trace')
    if any(rows[2][2*M+1:]):raise ValueError('Unexpected vertical central second trace')
    gamma=planar(c);G=[l1(gamma,j) for j in range(4)]
    Jmin=abs(gamma.get(1,Q(0)))-sum((abs(k*v) for k,v in gamma.items() if k!=1),Q(0))
    if Jmin<=0:raise ArithmeticError('Central speed lower bound is unresolved')
    knots,polys=screen.exact_clamped_spline(meta['chart']);end=fq(mesh[-1]);warp=8*fq(meta['warp_reference_q'])
    e=warp*polys[0][0];ep=warp*polys[0][1]/end;epp=2*warp*polys[0][2]/(end*end)
    if ep!=0:raise ValueError('Central radial chart derivative is not zero')
    rho={0:Q(1),3:-e/2,-3:-e/2};rhomin=1-abs(e);rho1=3*abs(e);rho2=9*abs(e)
    if rhomin<=0:raise ArithmeticError('Original central material chart is not positive')
    metric={}
    for k,x in gamma.items():
        for j,y in gamma.items():add(metric,k-j,k*j*x*y)
    for k,v in convolution(rho,rho).items():add(metric,k,-v)
    defect0,defect1=l1(metric),l1(metric,1)
    # R21 controls the exact original central metric as a restriction of its
    # whole map. Thus 1-d <= a, |gamma'|/rho <= 1+d and |a-1| <= d.
    d=Q(257212,10**13)
    cert=load('continuous_m12_central_interval_arithmetic',scripts/'6a65-m12-r137-continuous-domain.py')
    alo,ahi,phase,arc_proof=central_arclength_residual(metric,e,Jmin,rhomin,cert)
    if not 1-d<=alo<=ahi<=1+d:raise ArithmeticError('Refined central arc leaves the R21 metric envelope')
    U1=ahi/Jmin;U2=ahi*ahi*G[2]/Jmin**3
    cfg=meta['frozen_profile'];delta,vu,vd,eps=[fq(cfg[k]) for k in ('delta','vu','vd','ramp')]
    Tu=delta/(vu*(1-eps));Td=delta/(vd*(1-eps));h=Tu*eps
    Slo=Tu+Td+Q(bridge['exact_L']['lo']);Shi=Tu+Td+Q(bridge['exact_L']['hi'])
    lamlo,lamhi=end/Shi,end/Slo
    # Exact source second trace numerator rho X_ss+(e''/3) sin(3psi) gamma'.
    P=convolution(rho,planar(rows[2]))
    for k,v in gamma.items():add(P,k+3,epp*k*v/6);add(P,k-3,-epp*k*v/6)
    P0,P1,P2=[l1(P,j) for j in range(3)]
    second=[lamhi**2*P0/rhomin,
            lamhi**2*(P1/rhomin**2+P0*rho1/rhomin**3),
            lamhi**2*(P2/rhomin**3+3*P1*rho1/rhomin**4+P0*rho2/rhomin**4+3*P0*rho1*rho1/rhomin**5)]
    Amax=G[2]/Jmin**2;Aprime=2*G[3]/Jmin**2+7*G[2]**2/Jmin**3
    vp=(defect1/rhomin**2+2*defect0*rho1/rhomin**3)/(2*(1-d))
    arc_dev=max(abs(alo-1),abs(ahi-1));speed_dev=defect0/(rhomin*(Jmin+rhomin))
    zero=[G[0]*arc_dev/alo+G[1]*phase,
          G[2]/Jmin*phase+speed_dev,
          ahi*Aprime*phase+(arc_dev+defect0/rhomin**2)*Amax+vp/rhomin]
    first=[max(abs(1-lamlo),abs(1-lamhi)),Q(0),Q(0)]
    # Quintic Hermite controls, including physical s derivative factors.
    radial=[[Q(1),2*h/5,h*h/20],[5/h,Q(2),h/4],[20/(h*h),12/h,Q(2)]]
    D=[zero,first,second]
    central={(ds,du):sum((radial[ds][a]*D[a][du] for a in range(3)),Q(0)) for ds in range(3) for du in range(3-ds)}
    return {'Jmin':Jmin,'Jmax':G[1],'D2max':G[2],'D3max':G[3],'original_rho_min':rhomin,
            'U1':U1,'U2':U2,'arc_lower':alo,'arc_upper':ahi,'central_metric_defect_l1':defect0,
            'central_metric_defect_derivative_l1':defect1,'angle_shift':phase,'central_ramp_length':h,
            'prefix_length_lower':Slo,'prefix_length_upper':Shi,'lambda_lower':lamlo,'lambda_upper':lamhi,
            'central_correction':central,'central_trace_value_bounds':zero,'central_trace_first_bounds':first,
            'central_trace_second_bounds':second,'central_second_numerator_l1':[P0,P1,P2],
            'central_arc_and_partial_primitive_proof':arc_proof}


def central_original_second_jets(data,meta,central,screen,scripts):
    """The actual old Cartesian map, on the complete central correction support.

    The old common-cut correction is supported much later, so the original
    exact raw Hermite cells suffice here. This reuses R216's exact-cell
    converter, while the chart range uses its cubic Bernstein controls.
    """
    budget=load('continuous_m12_R216_cell_bounds',scripts/'6a65-m12-up-patch-exact-geometry-budget.py')
    with np.load(io.BytesIO(gzip.decompress(Path(data).read_bytes())),allow_pickle=False) as f:
        raw={k:f[k].copy() for k in ('mesh','jets','mean_increments')}
    M=(raw['jets'].shape[-1]-2)//3;mesh=list(map(fq,raw['mesh']));end=mesh[-1]
    right=central['lambda_upper']*central['central_ramp_length']
    if right>=mesh[meta['correction_start_index']]:raise ValueError('Central support reaches the common-cut correction')
    bpsi=bss=bsp=bpp=Q(0);cells=0
    for cell in range(len(mesh)-1):
        if mesh[cell]>=right:break
        h,power=budget.span_power(raw,cell)
        b0,b1,b2=[budget.coefficient_bounds(h,power,d) for d in range(3)]
        bpsi=max(bpsi,budget.angle_l1(b0,M,1));bss=max(bss,sum(b2,Q(0)))
        bsp=max(bsp,budget.angle_l1(b1,M,1));bpp=max(bpp,budget.angle_l1(b0,M,2));cells+=1
    knots,polys=screen.exact_clamped_spline(meta['chart']);warp=8*fq(meta['warp_reference_q'])
    bounds=[Q(0)]*3;pieces=0
    for j,cs in enumerate(polys):
        if knots[j]>=right/end:break
        width=knots[j+1]-knots[j]
        for d in range(3):
            degree=3-d
            power=[warp*Q(math.factorial(k+d),math.factorial(k))*cs[k+d]*width**k/end**d for k in range(degree+1)]
            bernstein=[sum((power[k]*Q(math.comb(i,k),math.comb(degree,k)) for k in range(i+1)),Q(0)) for i in range(degree+1)]
            bounds[d]=max(bounds[d],max(map(abs,bernstein)))
        pieces+=1
    e0,e1,e2=bounds;rho=1-e0
    if rho<=0:raise ArithmeticError('Central original chart bound unresolved')
    A=e1/(3*rho);Css=(e2/3+2*e1*A+3*e0*A*A)/rho
    Csu=(e1+3*e0*A)/(rho*rho);Cuu=3*e0/(rho**3)
    Hss=bss+2*A*bsp+A*A*bpp+Css*bpsi
    Hsu=(bsp+A*bpp)/rho+Csu*bpsi;Huu=bpp/(rho*rho)+Cuu*bpsi
    lam=central['lambda_upper']
    # The central correction is contained in the first up ramp, where f>=1.
    CX=lam*lam*Hss+2*lam*Hsu+Huu
    return CX,{'raw_source_cells':cells,'chart_pieces':pieces,'chart_e_upper':e0,'chart_ep_upper':e1,'chart_epp_upper':e2,
               'native_Xpsi':bpsi,'native_Xss':bss,'native_Xspsi':bsp,'native_Xpsipsi':bpp,
               'central_actual_source_scaled_coordinate_second_jet_upper':CX}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field',type=Path);ap.add_argument('--grid',type=Path)
    ap.add_argument('--reference-only',action='store_true',help='Certify only the fixed deterministic central-normalized reference')
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--scripts',type=Path,default=Path(__file__).parent);ap.add_argument('--result',type=Path)
    args=ap.parse_args();start=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh continuous-bounds output required')
    notes=args.scripts.parent/'notes'
    meta_path=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    bridge_path=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    manifest_path=notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    for p,expected in ((args.data,DATA_SHA),(meta_path,META_SHA),(bridge_path,BRIDGE_SHA),(manifest_path,MANIFEST_SHA)):
        if sha(p)!=expected:raise ValueError('Changed original input: '+str(p))
    meta=json.loads(meta_path.read_text());bridge=json.loads(bridge_path.read_text());manifest=json.loads(manifest_path.read_text())
    if args.reference_only:
        if args.field or args.grid or args.result:raise ValueError('Reference-only mode takes no saved solver field')
        original_shape=[0,0];raw={(d,j):Q(0) for d in range(3) for j in range(3-d)};zero_traces=[True]*3
    else:
        if not args.field or not args.grid:raise ValueError('Saved-field bounds require --field and --grid')
        grid=json.loads(args.grid.read_text())
        if grid['data_sha256']!=DATA_SHA or grid['common_meta_sha256']!=META_SHA:raise ValueError('Wrong whole-half grid identity')
        if args.result:
            result=json.loads(args.result.read_text())
            if result['field_sha256']!=sha(args.field) or result['grid_sha256']!=sha(args.grid):raise ValueError('Saved field/result identity mismatch')
        with np.load(args.field,allow_pickle=False) as f:
            coeff=f['coefficients'];knots=f['unit_knots'];pm=f['planar_modes'];zm=f['vertical_modes']
            if not np.all(np.isfinite(coeff)) or not np.all(np.isfinite(knots)):raise ValueError('Nonfinite saved field')
            if not np.array_equal(pm,np.arange(-grid['order'],grid['order']+1)*3+1) or not np.array_equal(zm,np.arange(grid['order']+1)*3):raise ValueError('Different angular basis')
            original_shape=list(coeff.shape);coeff=[[fq(x) for x in row] for row in coeff];knots=list(map(fq,knots));modes=[int(x) for x in np.r_[pm,zm]]
        if knots[:6]!=[Q(0)]*6 or knots[-6:]!=[Q(1)]*6 or any(b<a for a,b in zip(knots[:-1],knots[1:])):raise ValueError('Invalid clamped unit knot vector')
        raw,zero_traces=control_bounds(knots,coeff,modes)
    screen=load('continuous_m12_original_chart',args.scripts/'6a65-m12-weak-stress-recovered-v2.py')
    central=exact_central_constants(args.data,meta,bridge,screen,args.scripts)
    CXcentral,source_central=central_original_second_jets(args.data,meta,central,screen,args.scripts)
    cuff=fq(manifest['parameters']['rCuff']);cut=fq(manifest['parameters']['rCut']);h=cut-cuff
    total=central['prefix_length_lower']+h;Hmin=Q(171,250);Hq=Q(60)
    # R223: .684 < -r_q < 1.422. Its derivative Bernstein controls give
    # |R''|<3. The old whole background gives w<=16/15, |w_r|<24.
    # With h>.44 and sqrt(1+w*w)<1.5, this proves |H_q|<60.
    if h<=Q(11,25) or Q(3,1)/h*Q(3,2)+Q(711,500)**2*24>=Hq:raise ArithmeticError('Common-chart analytic constants fail')
    U1,U2=central['U1'],central['U2']
    basis={(0,0):raw[0,0],(1,0):raw[1,0]/(total*Hmin),(0,1):U1*raw[0,1],
           (2,0):raw[2,0]/(total*total*Hmin*Hmin)+Hq*raw[1,0]/(total*Hmin**3),
           (1,1):U1*raw[1,1]/(total*Hmin),(0,2):U1*U1*raw[0,2]+U2*raw[0,1]}
    combined={k:basis[k]+central['central_correction'][k] for k in basis}
    names={(0,0):'W',(1,0):'Ws',(0,1):'Wu',(2,0):'Wss',(1,1):'Wsu',(0,2):'Wuu'}
    def label(table):return {names[k]:v for k,v in table.items()}
    # f>=cuff globally; the deterministic correction is supported where f>=1.
    differential=basis[1,0]+basis[0,1]/cuff+central['central_correction'][1,0]+central['central_correction'][0,1]
    hessian=basis[2,0]+2*basis[1,1]/cuff+basis[0,2]/(cuff*cuff)+central['central_correction'][2,0]+2*central['central_correction'][1,1]+central['central_correction'][0,2]
    # This geometry statement concerns the fixed, normalized reference
    # BEFORE the saved solver field is added. Its changed support lies
    # entirely in the first up ramp; the old limiting-curvature tail is
    # unchanged. The loose derivative bounds are still sufficient here.
    cc=central['central_correction'];eta=cc[0,0];p=cc[1,0]+cc[0,1]
    cw=cc[2,0]+2*cc[1,1]+cc[0,2];d=Q(257212,10**13)
    metric=d+2*(1+d)*p+p*p;normal=(3*p+p*p)/(1-d)
    kp=(Q(5547266,10**6)*(1+d)+normal*CXcentral+cw)/(1-metric)
    K=Q(4763997235009095,562949953421312);R=Q(2131902881202937,1125899906842624)
    support=Q(737,1000)-Q(19,10)*normal-eta;diameter=2*(R+eta)
    reach_ratio=1/(K*diameter);held_ratio=(Q(19989114,10**8)-2*eta)/diameter
    moment_change=2400*eta*(1+9*eta)**2
    reference_checks={'homotopy_immersion':metric<1,'metric_below_1e_6':metric<Q(1,10**6),'normal_bound_hypothesis':2*(1+d)<Q(9,4),
                      'new_first_ramp_curvature_below_unchanged_tail':kp<K,
                      'support_above_inverse_curvature':support>1/K,
                      'reach_ratio_above_0_0312':reach_ratio>Q(312,10**4),
                      'held_ratio_above_0_05278':held_ratio>Q(5278,10**5),
                      'fixed_cap_diameter_above_0_93_D':Q(35426,10**4)/diameter>Q(93,100),
                      'homotopy_tube_within_old_reach':eta<1/K,
                      'positive_activity_third_moment':Q(44016,10**5)>moment_change}
    reference_geometry={'scope':'Only the deterministic exact central-normalized reference; excludes the saved solver correction.',
                        'checks':reference_checks,'all_checks_pass':all(reference_checks.values()),
                        'central_metric_triangle_upper':str(outer(metric)),
                        'central_normal_change_upper':str(outer(normal)),
                        'new_first_ramp_curvature_upper':str(outer(kp)),
                        'support_lower_exact':str(support),'diameter_upper_exact':str(diameter),
                        'reach_ratio_lower_exact':str(reach_ratio),'held_ratio_lower_exact':str(held_ratio),
                        'activity_third_moment_change_upper':str(outer(moment_change)),
                        'new_metric_threshold_not_proved_by_this_triangle_bound':metric>=Q(1,10**6)}
    out={'schema':'6a65-M12-entire-half-continuous-correction-bounds-v1','script_sha256':sha(__file__),
         'field_sha256':sha(args.field) if args.field else None,'grid_sha256':sha(args.grid) if args.grid else None,'data_sha256':DATA_SHA,
         'reference_only':args.reference_only,
         'common_meta_sha256':META_SHA,'bridge_sha256':BRIDGE_SHA,'tail_manifest_sha256':MANIFEST_SHA,
         'field_shape':original_shape,'exact_zero_endpoint_jets':zero_traces,
         'continuous_all_knots_and_all_angles':True,'arithmetic':'Exact Fraction controls; displayed strict upper rational endpoints rounded upward to denominator 10^24.',
         'raw_unit_chart_bounds':serialize({str(k):v for k,v in raw.items()}),
         'solver_correction_physical_uniform_material_jets':serialize(label(basis)),
         'deterministic_central_reference_change_jets':serialize(label(central['central_correction'])),
         'combined_change_from_original_R21_map_jets':serialize(label(combined)),
         'target_orthonormal_differential_l1_upper':str(outer(differential)),
         'target_scaled_coordinate_second_jet_l1_upper':str(outer(hessian)),
         'central_source_constants':serialize({k:central[k] for k in ('Jmax','D2max','D3max','U1','U2','central_metric_defect_l1','central_metric_defect_derivative_l1','angle_shift')}),
         'central_speed_lower_exact':str(central['Jmin']),'central_original_chart_rho_lower_exact':str(central['original_rho_min']),
         'central_second_numerator_l1':serialize({str(i):v for i,v in enumerate(central['central_second_numerator_l1'])}),
         'central_arc_and_partial_primitive_proof':central['central_arc_and_partial_primitive_proof'],
         'original_central_source_second_jet_bound':serialize(source_central),
         'deterministic_normalized_reference_geometry':reference_geometry,
         'inherited_hypotheses':'R21 exact original common-cut map and metric bound; R223 common chart; db6f-audit-entire-background-curvature and its review for w<=16/15 and |wr|<24. Original exact arclength/bridge definitions, not numerical quadrature values, define the comparison.',
         'relative_to_original_exact_common_cut_baseline':True,'central_reference_change_included':True,
         'whole_metric_certificate':False,'whole_reach_certificate':False,
         'remaining_geometry_input':'A bound on the original scaled coordinate second jets, or its complete pullback connection, is still required to convert these continuous W jets to a new curvature bound.',
         'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))

if __name__=='__main__':main()
