#!/usr/bin/env python3
"""NEW h=k: full original NV against Loww in the inverse-t monic cubic.
Only f33's original-coordinate definition prefix is reconstructed. No old
mean/Loww resultant, individual NP/NV scalar, or frozen gate is replayed.
The three genuine multiplication columns, adjugate target and both original
source multipliers are returned. All new pure-weight zeros are retained.
180 seconds / 4 GiB, one absolute deadline, profile-only output.
"""
import ast,hashlib,json,resource,signal,time
from pathlib import Path
START=time.perf_counter()
DEADLINE=START+180.0
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180.0)
COUNTS={'monic_division_returns':0,'multiplication_columns':0,
        'adjugate_coordinates':0,'exact_weight_divisions':0,
        'paid_denominator_checks':0,'original_two_source_coefficients':0}
def say(stage,**kw):
    kw.update(stage=stage,seconds=time.perf_counter()-START)
    print(json.dumps(kw,separators=(',',':')),flush=True)
DEP='2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py'
path=Path(__file__).with_name(DEP)
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2'
marker=b'\n# Exact scalar forms'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==4540
assert hashlib.sha256(prefix).hexdigest()=='a56e54b840cc323675394f96484c99658cad9a8420933cd2f344fe2df0d76efc'
tree=ast.parse(prefix.decode('utf-8'),filename=DEP+'#coordinates-only')
def callname(n):
    if isinstance(n,ast.Name):return n.id
    if isinstance(n,ast.Attribute):return callname(n.value)+'.'+n.attr
    return ''
kept=[];omitted=[]
for node in tree.body:
    drop=isinstance(node,ast.Assert)
    if isinstance(node,ast.Assign):
        drop=drop or any(isinstance(x,ast.Name) and x.id=='start' for x in node.targets)
    if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
        drop=drop or callname(node.value.func) in ('signal.alarm','signal.setitimer','resource.setrlimit','say')
    if drop:omitted.append(getattr(node,'lineno',0))
    else:kept.append(node)
tree.body=kept
env={'__file__':str(path),'__name__':'new_hk_inverse_t_NV_Loww_definition'}
exec(compile(ast.fix_missing_locations(tree),str(path)+'#necessary-definitions','exec'),env)
R,U,ctx=[env[k] for k in ('R','U','ctx')]
lam,u,Q,disc,A,B,ell,T,w,hh,S=[env[k] for k in
    ('lam','u','Q','disc','A','B','ell','T','w','hh','S')]
m,bc,P02,Pf,Phi,J,G,Pc,NF,NC,Delta,Tnum=[env[k] for k in
    ('m','bc','P02','Pf','Phi','J','G','Pc','NF','NC','Delta','Tnum')]
zeroP=ctx.constant(0);oneP=ctx.constant(1)
M=4*bc*disc
atoms=[('A',A.n),('B',B.n),('Q',Q.n),('delta',disc.n),
       ('Pf_original_chart',Pf.n),('M_equals_4bc_delta',M.n),
       ('P02_original',P02.n),('lambda_original_mean',lam.n),
       ('lambda_half_original_rank',(2*lam-1).n)]
def dex(a,b):
    q,r=divmod(a,b)
    assert not r and q*b==a
    COUNTS['exact_weight_divisions']+=1
    return q
def strip_paid(p):
    if not p:return p,oneP,[]
    q=p;removed=oneP;history=[]
    for name,atom in atoms:
        layers=0
        while True:
            g=q.gcd(atom)
            if int(g.total_degree())<=0:break
            q=dex(q,g);removed*=g;layers+=1
        if layers:history.append({'label':name,'gcd_layers':layers})
    assert q*removed==p
    return q,removed,history
def paid_den(p):
    assert p
    rem,_,_=strip_paid(p)
    assert int(rem.total_degree())==0
    COUNTS['paid_denominator_checks']+=1
def pp(p):
    data=json.dumps([[list(m),str(c)] for m,c in sorted(p.to_dict().items())],separators=(',',':')).encode()
    return {'zero':not bool(p),'degrees_lambda_u_Q':list(p.degrees()),
            'total_degree':int(p.total_degree()),'terms':len(p.to_dict()),
            'canonical_bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def rp(r):
    r=R(r)
    return {'numerator':pp(r.n),'denominator':pp(r.d)}
def up(p):
    p=U(p)
    return {'degree':len(p.c)-1,'coefficients':[rp(c) for c in p.c]}
def coef(p,j):return p.c[j] if j<len(p.c) else R()
def to_t(p):
    return U([c*Q**j for j,c in enumerate(p.c)])
t=U([0,1])
f=to_t(env['f']);nv=to_t(env['nv'])
vn=to_t(env['vn']);Wstar=to_t(env['Wstar'])
V=vn/Q;W1=Wstar/2
x=((u-ell*Q)*V-m*W1)/M
y=(ell*W1-u*V)/M
# Complete NV, including NC and the S*xi term, at this very same t.
assert nv==NF*f+bc*S*env['xi']*Q*t+NC
n=U(Tnum)-bc*Q*Delta*t
assert n==Pf*nv
assert Pf*f+bc*Phi*Q*t+Pc==U()
assert Q*V==J*f-G+bc*Q*t
Kw=2*(t*t+(5*u-4*x-2)*t+2*(x*x-disc*y*y)
      +4*x+4*disc*y-4*u*x+2*u*u-6*u+Q)
Loww=2*P02*(2*lam-1)*w-bc*t*(Kw+4*(f-u)*(t-2))
assert len(Loww.c)<=4
c0=2*P02*(2*lam-1)*w
assert coef(Loww,0)==c0
assert c0==-2*P02*lam*lam*(2*lam-1)**2/B
assert c0
inverse_t=-U(Loww.c[1:])/c0
assert t*inverse_t-U(1)==-Loww/c0
paid_den(c0.n);paid_den(c0.d)
# All input coefficient poles are old physical/chart weight units.
for poly in (f,nv,n,x,y,Loww):
    for c in poly.c:paid_den(c.d)
say('new_complete_NV_and_Loww_same_t_input',
    dependency_prefix_bytes=len(prefix),
    skipped_old_top_level_statements=omitted,
    NV_provenance={
      'source_blob':'bb534b16c2858c7cec98c5358ca105758e736e67',
      'source_sha256':'00d513d603f862ef6b484176fe4d9da3b766e0047d46a87ec8f575622aa8ca14',
      'complete_original_identity':'Q*N4((1,w,h,h))=2*NV'},
    Loww_provenance={
      'source_blob':'dc888d6c09612271a1767c164c0632511f265d00',
      'completed_identity':'Loww=NS-PS+EW2',
      'frozen_targets_not_replayed':['Res_t(E1,Loww)','Res_t(EBo,Loww)']},
    original_NV_degree=len(nv.c)-1,Loww_degree=len(Loww.c)-1,
    complete_NV_affine_identity_returned=True,
    constant_Loww_is_old_paid_unit=True,
    inverse_t_original_identity_returned='t*v-1=-Loww/c0',
    no_Delta_Tnum_or_Loww_top_inverse=True)
# This polynomial variable now denotes zeta=1/t, not an independent point.
zeta=U([0,1])
qz=U([coef(Loww,3-j)/c0 for j in range(4)])
assert len(qz.c)==4 and qz.c[3]==R(1)
assert U([coef(qz,3-j)*c0 for j in range(4)])==Loww
a=-bc*Q*Delta;b=Tnum
az=U([a,b])
assert U([coef(n,1),coef(n,0)])==az
for c in qz.c:paid_den(c.d)
def qreduce(p):
    p=U(p);q=U();r=U(p)
    while r and len(r.c)>=4:
        j=len(r.c)-4
        term=U([R()]*j+[r.c[-1]])
        q=q+term
        r=r-term*qz
    assert p==q*qz+r and len(r.c)<=3
    COUNTS['monic_division_returns']+=1
    return r,q
cols=[];column_q=[]
for j in range(3):
    prod=az*(zeta**j)
    rem,quo=qreduce(prod)
    cols.append([coef(rem,i) for i in range(3)])
    column_q.append(quo)
    COUNTS['multiplication_columns']+=1
Mat=[[cols[j][i] for j in range(3)] for i in range(3)]
# The first adjugate column is a genuine 2x2 cofactor in each coordinate.
adj0=[
    Mat[1][1]*Mat[2][2]-Mat[1][2]*Mat[2][1],
    Mat[1][2]*Mat[2][0]-Mat[1][0]*Mat[2][2],
    Mat[1][0]*Mat[2][1]-Mat[1][1]*Mat[2][0]]
Norm=sum((Mat[0][j]*adj0[j] for j in range(3)),R())
for i in range(3):
    assert sum((Mat[i][j]*adj0[j] for j in range(3)),R())==(Norm if i==0 else R())
    COUNTS['adjugate_coordinates']+=1
v=U(adj0)
Qlift=sum((adj0[j]*column_q[j] for j in range(3)),U())
assert az*v-U(Norm)==Qlift*qz
# The universal linear norm identity keeps b=0 and a=0 entire.
assert Qlift==U(b**3)
assert Norm==a**3-a*a*b*coef(qz,2)+a*b*b*coef(qz,1)-b**3*coef(qz,0)
for c in adj0+[Norm]:paid_den(c.d)
say('new_inverse_t_monic_cubic_full_NV_norm_return',
    monic_cubic_degree=3,true_multiplication_columns=3,
    adjugate_full_coordinates_returned=3,
    full_polynomial_lift_returned=True,
    norm_profile=rp(Norm),
    temporary_head_inverse_used=False,
    every_norm_zero_weight_retained=True)
# Undo zeta=1/t without any new weight inverse.
Omega=U([coef(v,2-j) for j in range(3)])*Pf
Theta=-b**3/c0
target=U([R(),R(),R(),Norm])
first_return=Omega*nv+Theta*Loww
assert first_return==target
COUNTS['original_two_source_coefficients']+=max(len(target.c),len(first_return.c))
# Clear only old-paid poles of the actual two source multipliers and target.
# The common factor also divides the polynomial target, so no unproved
# divisibility through rational original coefficients is assumed.
den=oneP
for c in Omega.c+[Theta,Norm]:
    paid_den(c.d)
    den=dex(den*c.d,den.gcd(c.d))
tags_nv=[dex(den*c.n,c.d) for c in Omega.c]
tag_low=dex(den*Theta.n,Theta.d)
scalar=dex(den*Norm.n,Norm.d)
common=zeroP
for p0 in tags_nv+[tag_low,scalar]:
    if p0:common=p0 if not common else common.gcd(p0)
if common:
    tags_nv=[dex(p0,common) for p0 in tags_nv]
    tag_low=dex(tag_low,common)
    scalar=dex(scalar,common)
else:
    assert not scalar
    common=oneP
Omega2=U([R(p0) for p0 in tags_nv]);Theta2=R(tag_low)
returned=Omega2*nv+Theta2*Loww
assert returned==U([R(),R(),R(),R(scalar)])
COUNTS['original_two_source_coefficients']+=max(4,len(returned.c))
say('new_two_original_sources_common_multiplier_cancelled',
    exact_identity='Omega_NV(t)*NV(t)+Omega_L*Loww(t)=Scalar*t^3',
    same_original_t=True,scalar_profile=pp(scalar),
    common_multiplier_profile=pp(common),
    target_divisibility_also_returned=True,
    all_original_coefficients_returned=True,
    common_zero_fibers_retained=True,
    t_inverse_already_returned_in_same_two_source_ideal=True)
remaining,removed,history=strip_paid(scalar)
assert scalar==removed*remaining
assert returned==U([R(),R(),R(),R(removed*remaining)])
say('new_NV_Loww_pure_weight_necessary_support',
    support_profile=pp(remaining),removed_paid_support=history,
    returned_identity='Omega_NV*NV+Omega_L*Loww=U_paid*Support*t^3',
    norm_zero_or_support_zero_retained=True,
    Delta_zero_Tnum_zero_and_all_new_heads_retained=True,
    factored_pure_weight_source_defined_by_three_term_geometric_identity=True,
    expanded_inverse_t_cube_source_not_computed=True,
    new_finiteness_claim=False,new_emptiness_claim=False,
    counts=COUNTS,source_finished=True,
    source_max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
