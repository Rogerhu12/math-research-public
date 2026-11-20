#!/usr/bin/env python3
"""Strict Darboux integral of the fixed finite mean before the short bridge.

The object uses exact shared-two-jet Y/e polynomials, the exact rational
multistage prefix profile at frozen delta with explicit endpoint normalization,
the complete R53 core reference
lift, and the fixed positive 1168-node mean. The new core is enclosed by a
proved two-jet tube about its actual finite support predecessor. Core height
is zero. No node samples or ODE projection replace the radial interval range.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
import argparse,bisect,hashlib,importlib.util,json,math,sys,time
import numpy as np
import mpmath as mp
def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp)
    sys.modules[name]=m;sp.loader.exec_module(m);return m
def fq(x):return Q.from_float(float(x))
def qval(poly,t):
    y=Q(0)
    for x in poly[::-1]:y=y*t+x
    return y
def qder(poly):return [(i+1)*poly[i+1]for i in range(len(poly)-1)]
def right_correction(poly,h,target):
    old=[qval(poly,h),qval(qder(poly),h),qval(qder(qder(poly)),h)]
    d0,d1,d2=[b-a for a,b in zip(old,target)]
    return [Q(0),Q(0),Q(0),(10*d0-4*h*d1+h*h*d2/2)/h**3,
            (-15*d0+7*h*d1-h*h*d2)/h**4,(6*d0-3*h*d1+h*h*d2/2)/h**5]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--source-run',type=Path,required=True);p.add_argument('--physical',type=Path,required=True)
p.add_argument('--support-dir',type=Path,required=True)
p.add_argument('--mean-kernel',type=Path,required=True);p.add_argument('--interval-kernel',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
p.add_argument('--mean-nodes',type=int,default=1168)
p.add_argument('--width',type=float,default=.18)
p.add_argument('--max-cells',type=int,default=20000)
args=p.parse_args()
started=time.monotonic()
base=module('_prefix_z0_mean_range_kernel',args.mean_kernel)
K=module('_prefix_z0_interval_kernel',args.interval_kernel);base.K=K
I=base.I
ad=module('_prefix_z0_actual_model',args.support_dir/'actual_m3_metric_model.py')
ld=module('_prefix_z0_physical_map',args.support_dir/'audit_full_relative_metric.py')
o=ad.load_model({'source_run':str(args.source_run.resolve())});z=ld.load_physical(args.physical)
o.initial(z.p);f=o.flow(z.p[0]);core=f.exact_lift_core
record=json.loads(args.source_run.read_text())
assert args.mean_nodes==int(record['prefix_audit']['samples_psi'])==1168
assert o.M==24 and f.base_mode==3
assert core.curvature_blend==1 and 0<fq(core.homotopy)<Q(1,499)
assert Q(199,1000)<fq(core.k)<Q(201,1000)
assert fq(core.halfwidth)==Q(1,2) and fq(core.halfwidth)+fq(core.transition)/2<Q(601,1000)
coeff=[fq(x)for x in core.original.coefficients];freq=[int(x)for x in core.original.frequencies]
rho_l=Q(1)-sum(abs((1-m*m)*a)for a,m in zip(coeff,freq));rho_h=2-rho_l
assert rho_l>Q(5,11) and 1/rho_h>Q(201,1000)
# pi>157/50 implies halfperiod>157/150; beta is then positive and <3.
Astar=Q(601,1000)*(Q(11,5)-Q(199,1000))
denom=Q(157,150)-Q(601,1000)
assert Astar/denom<3 and Astar/Q(499)<Q(1,400)
assert Q(11,5)*Q(1,400)+Q(3,499)<Q(3,250)
print(json.dumps({'stage':'model','seconds':time.monotonic()-started,'rho_lower_exact':str(rho_l),'prefix_end':float(f.prefix_end)}),flush=True)
N=args.mean_nodes;M=o.M;n=o.n
entry=fq(f.prefix_end);full_end=fq(f.end);qq=I(o.q)
xx=[fq(v)for v in z.x]
def irat(x):return I.rational(Q(x))
def iarr(values):
    low=[];high=[]
    for x in values:
        v=irat(x);low.append(float(v.x[0]));high.append(float(v.x[1]))
    return I(np.asarray(low),np.asarray(high))
def ipoly(coef,x):
    out=I(0)
    for c in coef[::-1]:out=out*x+c
    return out
def ider(coef):return [(i+1)*coef[i+1]for i in range(len(coef)-1)]
def isin(x):return base.sincos_i(x)
def norm(v):return sum((u.sq()for u in v),I(0)).sqrt()
def dot(v,w):return sum((a*b for a,b in zip(v,w)),I(0))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
# Exact shared Y Hermite definition; only pieces touching the prefix are needed.
pc={}
for i in range(len(xx)-1):
    if xx[i]>=entry:break
    h=xx[i+1]-xx[i];rows=[]
    for j in range(n):
        pp=[fq(z.sol.c[5-k,i,j])for k in range(6)]
        if i+1<len(xx)-1:
            target=[fq(z.sol.c[5,i+1,j]),fq(z.sol.c[4,i+1,j]),2*fq(z.sol.c[3,i+1,j])]
        else:target=[qval(pp,h),qval(qder(pp),h),qval(qder(qder(pp)),h)]
        cc=right_correction(pp,h,target);rows.append([a+b for a,b in zip(pp,cc)])
    pc[i]=[iarr([row[k]for row in rows])for k in range(6)]
# Same shared angular spline, before its unchanged late cutoff (outside prefix).
spx=[fq(v)*full_end for v in f.spline.x];ec={}
assert entry<Q(3,4)*full_end
for i in range(len(spx)-1):
    if spx[i]>=entry:break
    pp=[fq(f.spline.c[3-k,i])/full_end**k for k in range(4)]+[Q(0),Q(0)]
    h=spx[i+1]-spx[i]
    target=[fq(f.spline.c[3,i+1]),fq(f.spline.c[2,i+1])/full_end,2*fq(f.spline.c[1,i+1])/full_end**2]if i+1<len(spx)-1 else[qval(pp,h),qval(qder(pp),h),qval(qder(qder(pp)),h)]
    cc=right_correction(pp,h,target)
    ec[i]=[irat((a+b)*fq(f.warp_e))for a,b in zip(pp,cc)]
print(json.dumps({'stage':'shared-polynomials','seconds':time.monotonic()-started,'Y_pieces':len(pc)}),flush=True)
# Exact intended rational velocity law.  The amplitude delta is unchanged;
# duration is explicitly normalized to the literal physical prefix endpoint.
# This declares a C2 representation and pays its profile transfer below.
spec=f.cfg['multistage_flat'];eta=Q(spec['eta']);ratio=fq(f.delta)/Q(spec['reference_delta'])
reference=[];t=Q(0);area=Q(0)
for name in('up','down'):
    for row in spec[name]:
        v0,v1,L=map(Q,row)
        reference.append((t,L,v0,v1,area))
        area+=L*(v0+v1)/2;t+=L
assert area==0
duration_ratio=entry/t;velocity_ratio=ratio/duration_ratio
true_profile_end=entry
segments=[];profile_grid=[Q(0),entry]
for start,L,v0,v1,area in reference:
    segments.append((duration_ratio*start,duration_ratio*L,v0,v1,area,L))
    profile_grid.extend([duration_ratio*start,duration_ratio*(start+L)])
    if v0!=v1:profile_grid.extend([duration_ratio*(start+eta*L),duration_ratio*(start+(1-eta)*L)])
assert reference[0][2]==reference[-1][3]==0
assert Q(49,1000)<fq(f._multistage_eta)<Q(51,1000)
# Exact comparison with the source-constant hand-jet interpretation.  All
# source segment constants, eta, rounded dv, and ratio are frozen as binary
# rationals, but the formulas below are evaluated in real arithmetic.  This
# does not claim a bound for every later IEEE/libm evaluation of that code.
source_ratio=fq(f._multistage_ratio);source_eta=fq(f._multistage_eta)
eta_gap=abs(source_eta-eta);profile_gaps=[Q(0),Q(0),Q(0)]
speed_max=velocity_ratio*max(abs(x)for row in reference for x in row[2:4])
accel_max=max(velocity_ratio*abs(v1-v0)/(duration_ratio*L*(1-eta))for _,L,v0,v1,_ in reference)
jerk_max=max(velocity_ratio*abs(v1-v0)*Q(3,2)/(eta*(1-eta)*(duration_ratio*L)**2)for _,L,v0,v1,_ in reference)
source_rows=f._multistage_segments;profile_transfer_rows=[]
assert len(source_rows)==len(reference)
for index,(ref,source)in enumerate(zip(reference,source_rows)):
    start,L,v0,v1,area=ref;ss,ls,vs0,vs1,ars=map(fq,source)
    dvs=fq(float(source[3]-source[2]));dv=v1-v0
    du=entry*abs(1/(source_ratio*ls)-1/(duration_ratio*L))+abs(ss/ls-start/L)
    source_next=source_ratio*fq(source_rows[index+1][0])if index+1<len(source_rows)else entry
    edge=max(abs(source_ratio*ss-duration_ratio*start),abs(source_next-duration_ratio*(start+L)))
    # For eta in [.049,.051], |F_u|<=2, |P_u|<=1, and both
    # eta derivatives have absolute value <4.  d=F_u satisfies
    # |d_u|<33, |d_eta|<24 and 0<=d<2.  The literal .15 in P is
    # separately enclosed; no hidden replacement by 3/20 is needed.
    Pgap=du+4*eta_gap+abs(fq(.15)-Q(3,20))*source_eta**2/(1-source_eta)
    ag=abs(source_ratio-ratio)*(abs(ars)+ls*(abs(vs0)+abs(dvs)))
    ag+=ratio*(abs(ars-area)+abs(ls-L)*(abs(vs0)+abs(dvs))
               +L*(abs(vs0-v0)+abs(dvs-dv)+abs(v0)*du+abs(dv)*Pgap))
    vg=abs(1-velocity_ratio)*(abs(vs0)+abs(dvs))
    vg+=velocity_ratio*(abs(vs0-v0)+abs(dvs-dv)+abs(dv)*(2*du+4*eta_gap))
    new_accel_coef=velocity_ratio*dv/(duration_ratio*L)
    gg=2*abs(dvs/(source_ratio*ls)-new_accel_coef)+abs(new_accel_coef)*(33*du+24*eta_gap)
    gaps=[ag+speed_max*edge,vg+accel_max*edge,gg+jerk_max*edge]
    profile_gaps=[max(a,b)for a,b in zip(profile_gaps,gaps)]
    profile_transfer_rows.append({'segment':index,'normalized_u_gap_exact':str(du),'edge_gap_exact':str(edge),'jet_gaps_exact':list(map(str,gaps))})
assert max(profile_gaps)<Q(1,10**10)
starts=[row[0]for row in segments]
def profile(s,left,right):
    mid=(left+right)/2
    if mid>=true_profile_end:return I(1),I(0)
    k=min(len(segments)-1,bisect.bisect_right(starts,mid)-1)
    start,physical_L,v0,v1,old_area,L=segments[k]
    u=(s-irat(start))/irat(physical_L);dv=v1-v0
    if dv==0:
        return 1+irat(ratio)*(irat(old_area)+irat(L*v0)*u),irat(velocity_ratio*v0)
    u_mid=(mid-start)/physical_L
    et=irat(eta)
    if u_mid<eta:
        x=u/et;F=et/(1-et)*(x**3-x**4/2);P=et.sq()/(1-et)*(x**4/4-x**5/10)
    elif u_mid>1-eta:
        zz=1-u;x=zz/et
        F=1-et/(1-et)*(x**3-x**4/2)
        P=I(.5)-zz+et.sq()/(1-et)*(x**4/4-x**5/10)
    else:
        F=(u-et/2)/(1-et);P=(u.sq()/2-et*u/2+irat(Q(3,20))*et.sq())/(1-et)
    aa=1+irat(ratio)*(irat(old_area)+irat(L)*(irat(v0)*u+irat(dv)*P))
    ap=irat(velocity_ratio)*(irat(v0)+irat(dv)*F)
    return aa,ap
# Literal angular nodes, true elementary functions at these fixed nodes.
psi=2*np.pi*np.arange(N)/N;mp.mp.dps=90;mp.iv.dps=65;iv=mp.iv
def mplow(v):return mp.make_mpf(v._mpi_[0])
def mphigh(v):return mp.make_mpf(v._mpi_[1])
def mpq(v):v=Q(v);return iv.mpf(v.numerator)/v.denominator
def toIarray(v):
    return I(np.array([float(K.dn(float(mplow(x))))for x in v]),np.array([float(K.up(float(mphigh(x))))for x in v]))
co=[];sn=[]
for m in [3]+freq:
    co.append(toIarray([iv.cos(iv.mpf(float(p))*m)for p in psi]))
    sn.append(toIarray([iv.sin(iv.mpf(float(p))*m)for p in psi]))
co3,sn3=co[0],sn[0]
co=I(np.stack([a.x[0]for a in co[1:]]),np.stack([a.x[1]for a in co[1:]]))
sn=I(np.stack([a.x[0]for a in sn[1:]]),np.stack([a.x[1]for a in sn[1:]]))
fr=I(np.asarray(freq)[:,None])
# The old support material-angle inverse is validated by strict endpoint signs.
ac=[mpq(c)for c in coeff]
theta=[iv.mpf(float(p))-mpq(fq(f.warp_e))*iv.sin(3*iv.mpf(float(p)))/3 for p in psi]
seed=core.original.evaluate(np.array([float((mplow(t)+mphigh(t))/2)for t in theta]))['phi']
def arc(p):
    return p+sum((c*(1-m*m)/m*iv.sin(m*p)for c,m in zip(ac,freq)),iv.mpf(0))
oldFtR=[];oldFtT=[];oldFttR=[];oldFttT=[];bracket_width=0.
for j,(target,estimate)in enumerate(zip(theta,seed)):
    eps=1e-12
    for attempt in range(12):
        left=float(estimate-eps);right=float(estimate+eps)
        if mphigh(arc(iv.mpf(left)))<mplow(target) and mplow(arc(iv.mpf(right)))>mphigh(target):break
        eps*=4
    else:raise ArithmeticError('Old support inverse bracket failed')
    ph=iv.mpf([left,right]);rh=1+sum((c*(1-m*m)*iv.cos(m*ph)for c,m in zip(ac,freq)),iv.mpf(0))
    assert mplow(rh)>0
    angle=ph-iv.mpf(float(psi[j]));si,cs=iv.sin(angle),iv.cos(angle)
    oldFtR.append(-si);oldFtT.append(cs);oldFttR.append(-cs/rh);oldFttT.append(-si/rh)
    bracket_width=max(bracket_width,right-left)
# The R53 curvature/phase tube is rigorous and planar.
pad1=irat(Q(1,400));pad2=irat(Q(3,250))
padding1=I(-float(pad1.x[1]),float(pad1.x[1]));padding2=I(-float(pad2.x[1]),float(pad2.x[1]))
ftR,ftT=toIarray(oldFtR)+padding1,toIarray(oldFtT)+padding1
fttR,fttT=toIarray(oldFttR)+padding2,toIarray(oldFttT)+padding2
initial=I(np.asarray(f.exact_lift_initial,float))*qq
def angle_jets(y):
    rr=y.item(slice(1,M+1)).expand();tt=y.item(slice(M+1,2*M+1)).expand();zz=y.item(slice(2*M+1,None)).expand()
    R=y.item(0)+(rr*co).sum();Rp=-(rr*(fr*sn)).sum();Rpp=-(rr*(fr.sq()*co)).sum()
    T=(tt*sn).sum();Tp=(tt*(fr*co)).sum();Tpp=-(tt*(fr.sq()*sn)).sum()
    Zp=-(zz*(fr*sn)).sum();Zpp=-(zz*(fr.sq()*co)).sum()
    return [Rp-T,Tp+R,Zp],[Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp]
ini1,ini2=angle_jets(initial)
rho0=1-I(f.warp_e)*co3;rp0=3*I(f.warp_e)*sn3
sd0,cd0=isin(I(f.warp_e)*sn3/3)
H1=[rho0*ftR-rho0*sd0-ini1[0],rho0*ftT-rho0*cd0-ini1[1],-ini1[2]]
H2=[rho0.sq()*fttR+rp0*ftR-(rp0*sd0-rho0.sq()*cd0)-ini2[0],
    rho0.sq()*fttT+rp0*ftT-(rp0*cd0+rho0.sq()*sd0)-ini2[1],-ini2[2]]
print(json.dumps({'stage':'core-tube','seconds':time.monotonic()-started,'inverse_brackets':N,'bracket_width':bracket_width}),flush=True)
lift_lo=fq(.5)*entry;lift_hi=fq(.9)*entry
def lift(s,left,right):
    if right<=lift_lo:return I(1)
    if left>=lift_hi:return I(0)
    u=(s-irat(lift_lo))/irat(lift_hi-lift_lo)
    chi=1-u**3*(10-15*u+6*u.sq())
    return I(np.maximum(0,chi.x[0]),np.minimum(1,chi.x[1]))
def evaluate(left,right):
    s=I(irat(left).x[0],irat(right).x[1]);mid=(left+right)/2
    i=min(len(xx)-2,bisect.bisect_right(xx,mid)-1)
    y=ipoly(pc[i],s-irat(xx[i]))*qq
    j=min(len(spx)-2,bisect.bisect_right(spx,mid)-1)
    e=ipoly(ec[j],s-irat(spx[j]));ep=ipoly(ider(ec[j]),s-irat(spx[j]))
    aa,ap=profile(s,left,right);chi=lift(s,left,right)
    a1,a2=angle_jets(y)
    d1=[a1[k]+aa*chi*H1[k]for k in range(3)]
    d2=[a2[k]+aa*chi*H2[k]for k in range(3)]
    rho=1-e*co3;rp=3*e*sn3
    sd,cd=isin(e*sn3/3)
    R1,T1=d1[0]*cd-d1[1]*sd,d1[0]*sd+d1[1]*cd
    R2,T2=d2[0]*cd-d2[1]*sd,d2[0]*sd+d2[1]*cd
    U=[R1/(aa*rho),1+T1/(aa*rho),d1[2]/(aa*rho)]
    V=[-1+R2/(aa*rho.sq())-R1*rp/(aa*rho**3),
       T2/(aa*rho.sq())-T1*rp/(aa*rho**3),
       d2[2]/(aa*rho.sq())-d1[2]*rp/(aa*rho**3)]
    un=norm(U);ka=norm(cross(U,V))/(un**3);Tu=[x/un for x in U]
    vproj=dot(Tu,V);nv=[x-vproj*t for x,t in zip(V,Tu)];nn=norm(nv);Nu=[x/nn for x in nv];Bi=cross(Tu,Nu)
    alpha=-ap/ka;root=1-alpha.sq()
    if np.any(root.x[0]<=0):raise ValueError('Interval Frenet root not positive')
    beta=root.sqrt();normal=alpha*Nu[2]+beta*Bi[2]
    normal=I(np.maximum(-1,normal.x[0]),np.minimum(1,normal.x[1]))
    convection=-ep*sn3/(3*rho)*d1[2]
    mean=(normal+convection).sum()/N
    return mean,float(np.min(root.x[0]))
grid=sorted(set([Q(0),entry]+[v for v in xx if 0<v<entry]+[v for v in spx if 0<v<entry]+
                [v for v in profile_grid if 0<v<entry]+[lift_lo,lift_hi]+([true_profile_end]if true_profile_end<entry else[])))
stack=[(l,r,0)for l,r in zip(grid[:-1],grid[1:])][::-1]
attempts=accepted=split=0;root_min=math.inf;mean_lo=math.inf;mean_hi=-math.inf;integral=I(0);failed=None;max_depth=0
while stack:
    left,right,depth=stack.pop();attempts+=1
    try:
        mean,root=evaluate(left,right)
        lo,hi=float(mean.x[0]),float(mean.x[1]);valid=hi-lo<=args.width
        reason='mean range too wide'
    except(ValueError,ArithmeticError,FloatingPointError)as ex:
        valid=False;lo,hi=-math.inf,math.inf;reason=str(ex)
    if not valid:
        if attempts>=args.max_cells or depth>=24:
            failed={'left':str(left),'right':str(right),'depth':depth,'reason':reason,'mean_range':[lo,hi]};break
        mid=(left+right)/2;stack.extend([(mid,right,depth+1),(left,mid,depth+1)]);split+=1;continue
    accepted+=1;integral=integral+mean*irat(right-left)
    root_min=min(root_min,root);mean_lo=min(mean_lo,lo);mean_hi=max(mean_hi,hi);max_depth=max(max_depth,depth)
    if accepted%200==0:print(json.dumps({'stage':'radial','accepted':accepted,'attempts':attempts,'pending':len(stack),'height_partial':[float(integral.x[0]),float(integral.x[1])],'seconds':time.monotonic()-started}),flush=True)
complete=failed is None
height=[float(integral.x[0]),float(integral.x[1])]
passed=complete and height[0]>.35 and height[1]<.51
report={'status':'prefix_mean_height_certified'if passed else'prefix_mean_height_unresolved','complete':complete,'height_window_passed':passed,'height_core_anchor':0,'height_interval':height,
 'mean_nodes':N,'field_definition':'Exact shared-right-two-jet Hermite Y/e; full R53 reference lift; true rational multistage profile with amplitude delta fixed and duration normalized to the exact binary prefix endpoint; fixed literal angular nodes with positive equal weights.',
 'source_run_sha256':sha(args.source_run),'physical_sha256':sha(args.physical),'source_sha256':sha(__file__),'mean_kernel_sha256':sha(args.mean_kernel),'interval_kernel_sha256':sha(args.interval_kernel),
 'frozen_delta_exact':str(fq(f.delta)),'profile_amplitude_ratio_exact':str(ratio),'profile_duration_ratio_exact':str(duration_ratio),'profile_velocity_ratio_exact':str(velocity_ratio),'profile_velocity_ratio_minus_one_exact':str(velocity_ratio-1),'true_profile_end_exact':str(true_profile_end),'integration_end_exact':str(entry),
 'endpoint_profile_jet_exact':[1,0,0],
 'source_constant_real_profile_jet_gap_upper':[float(irat(v).x[1])for v in profile_gaps],
 'source_constant_real_profile_jet_gap_exact':list(map(str,profile_gaps)),
 'source_constant_profile_transfer_rows':profile_transfer_rows,
 'source_floating_evaluation_roundoff_certified':False,
 'core_old_rho_lower_exact':str(rho_l),'core_old_rho_upper_exact':str(rho_h),'core_tube_first':'1/400','core_tube_second':'3/250','validated_old_inverse_brackets':N,'maximum_inverse_bracket_width':bracket_width,
 'accepted_cells':accepted,'attempted_cells':attempts,'split_cells':split,'maximum_depth':max_depth,'finite_mean_value_range':[mean_lo,mean_hi],'frenet_root_lower':root_min,'failed_cell':failed,
 'radial_integration':'Outward Darboux sums over all polynomial/profile/lift breaks; no radial trapezoid or Gaussian assumption.',
 'full_surface_or_tail_certified':False,'floating_source_oracle_identified_with_new_C2_map':False,'seconds':time.monotonic()-started}
args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report),flush=True)
if not passed:raise SystemExit(1)

