"""R757. Consume the completed R755 material ledger and check curvature-strengthened pose inequalities."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import time

from r726_closed_spinor_fourier import public
from r734_true_dyadic_tail import I,D,ZERO,ONE
from r755_harmonic_area_bounds import CAP_SIN,ab,ch,dot,matrix,positive,quadratic,selector,sh,sqroot,square

CUTS=('.075','.085','.09','.145','.15','.205','.21','.22')
SPLITS=(16,24,160,24,160,24,16)
SOURCE='4a271c0f8df58456a66a71a59e003c5d887c07d54b8bb53290e7269625f3ff7e'
CAL='bf12e73ac01668167581f3a4037d115a226984555ca1c80dc146ee7239f14b73'
TILT=CAP_SIN
CT=sqroot(1-square(TILT))
M=100*ONE/3


def hi(t):return I(t.hi)
def low(t):return I(t.lo)
def norm(v):return sqroot(sum((square(x) for x in v),ZERO))
def vmax(*v):return I(max(x.lo for x in v),max(x.hi for x in v))
def positive_root(x):return sqroot(positive(x))


def pack(z):
    if isinstance(z,I):return {'#interval':z.bounds()}
    if isinstance(z,(tuple,list)):return [pack(q) for q in z]
    if isinstance(z,dict):return {k:pack(q) for k,q in z.items()}
    return z


def unpack(z):
    if isinstance(z,list):return [unpack(q) for q in z]
    if isinstance(z,dict):
        if set(z)=={'#interval'}:return I(*z['#interval'])
        return {k:unpack(q) for k,q in z.items()}
    return z


class Paid:
    def __init__(self,path,identity):
        self.root=path;self.root.mkdir(parents=True,exist_ok=True)
        self.identity=hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest()
        self.new=0;self.old=0;self.new_seconds=0.
        manifest=self.root/'identity'
        if manifest.exists() and manifest.read_text()!=self.identity:
            raise ValueError('R757 saved state belongs to another exact operator or source')
        manifest.write_text(self.identity)
    def once(self,key,fn):
        path=self.root/(hashlib.sha256(json.dumps(key,sort_keys=True).encode()).hexdigest()+'.json')
        if path.exists():
            item=json.loads(path.read_bytes())
            if item['identity']!=self.identity or item['key']!=key:
                raise ValueError('R757 immutable paid unit key mismatch')
            self.old+=1
            return unpack(item['value']),False
        t=time.monotonic();v=fn();duration=time.monotonic()-t
        data=dict(identity=self.identity,key=key,seconds=duration,value=pack(v))
        tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(data,separators=(',',':'),allow_nan=False))
        os.replace(tmp,path);self.new+=1;self.new_seconds+=duration
        return v,True


def read_artifact(path,digest):
    if not re.fullmatch('[0-9a-f]{64}',digest):
        raise ValueError('a frozen completed object SHA256 is required')
    b=path.read_bytes()
    if hashlib.sha256(b).hexdigest()!=digest:
        raise ValueError('different completed original R755 bytes')
    return b


def recover(final,journal):
    receipt=json.loads(final)
    if (receipt.get('kind')!='terminal' or receipt.get('source_sha256')!=SOURCE or
        receipt.get('original_calibration_sha256')!=CAL or receipt.get('remaining_old_J_or_RHS_repeated')!=0):
        raise ValueError('complete original R755 terminal and R738 identity required')
    units={}
    for line in journal.splitlines():
        row=json.loads(line);key=row['key']
        if row['fingerprint']!=receipt['fingerprint'] or key in units:
            raise ValueError('foreign or duplicate original R755 unit')
        units[key]=row['value']
    if (len(units)!=receipt['retained_units'] or 'actual_64_positive_weights' not in units or
        {k for k in units if k.startswith('material_')}!={f'material_{i}' for i in range(sum(SPLITS))}):
        raise ValueError('incomplete original R755 material cover')
    cap=receipt.get('actual_cap_identity')
    if (not cap or units['actual_64_positive_weights'].get('actual_cap_identity')!=cap or
        cap.get('all_tested_proper_rotations_sine_hull')!=TILT.bounds()):
        raise ValueError('different frozen R755 proper-rotation interval or missing physical rim identity')
    edges=[]
    for lo,up,n in zip(CUTS,CUTS[1:],SPLITS):
        a,b=I(lo),I(up)
        edges.extend(a+(b-a)*k/n for k in range(n))
    edges.append(I(CUTS[-1]))
    masses=[[I(*v) for v in units[f'material_{i}']] for i in range(len(edges)-1)]
    A,L,S=[sum((row[k] for row in masses),ZERO) for k in range(3)]
    for observed,field in zip((A,L,S),('A_over_pi','L','S')):
        if observed.bounds()!=receipt[field]:
            raise ValueError('retained material sums do not equal the original terminal')
    # Separate prefix/suffix sums avoid interval dependency on the full material total.
    N=len(masses)
    x=[ZERO]*(N+1);s=[ZERO]*(N+1);y=[ZERO]*(N+1);t=[ZERO]*(N+1)
    for i in range(N):
        x[i+1]=x[i]+masses[i][1];s[i+1]=s[i]+masses[i][2]
    for i in reversed(range(N)):
        y[i]=y[i+1]+masses[i][1];t[i]=t[i+1]+masses[i][2]
    cells=[]
    for i,((area,dx,ds),lo,up) in enumerate(zip(masses,edges,edges[1:])):
        r=I(lo.lo,up.hi);left=I(x[i].lo,x[i+1].hi);right=I(y[i+1].lo,y[i].hi)
        den=r*sh(L)
        cells.append(dict(area=area,si=I(s[i].lo,s[i+1].hi),so=I(t[i+1].lo,t[i].hi),
              hs_i=-I('.075')*ch(right)/den,hs_o=I('.22')*ch(left)/den,
              hp_i=I('.075')*sh(right)/den,hp_o=I('.22')*sh(left)/den,
              zero=ONE/(L*r)))
    return receipt,A,L,cells


def eigen_extremes(Q):
    # Identically zero xy,yz terms follow from C_y=0 and the original labelled rim frames.
    if any(Q[i][j].lo!=0 or Q[i][j].hi!=0 for i,j in ((0,1),(1,0),(1,2),(2,1))):
        raise ValueError('R757 uses the original xz-pose plane')
    x,y,z=Q[0][0],Q[1][1],Q[2][2]
    split=sqroot(square(x-z)+4*square(Q[0][2]))
    return I(min(y.lo,((x+z-split)/2).lo)),I(max(y.hi,((x+z+split)/2).hi))


def prepare(A,L,cells,C,eta,curvature):
    mu=1+eta;sm=sqroot(mu);speed=curvature*sm
    _,base,B,di,do=matrix(A,L,C)
    gap=[[base[i][j]+(eta*A if i==j else ZERO)+(1-ONE/mu)*B[i]*B[j]/A
          for j in range(3)] for i in range(3)]
    mean=[v/A for v in B]
    ni=[TILT,ZERO,CT];no=[ZERO,ZERO,ONE]
    deltaN=[norm([p-q for p,q in zip(e,mean)]) for e in (ni,no)]
    fixed=[]
    for c in cells:
        # Store the complete latitude covariance of both actual harmonic gradient coordinates.
        def covariance(reference):
            mat=[[ZERO]*3 for _ in range(3)]
            for i in range(3):
                for j in range(i,3):
                    a=C[i]*C[j]*square(c['zero'])
                    for ki,ko in (('hs_i','hs_o'),('hp_i','hp_o')):
                        left=[c[ki]*d+c[ko]*o-t for d,o,t in zip(di[i],do[i],reference[i])]
                        right=[c[ki]*d+c[ko]*o-t for d,o,t in zip(di[j],do[j],reference[j])]
                        a+=dot(left,right)/2
                    mat[i][j]=mat[j][i]=a
            return mat
        h=covariance([[ZERO,ZERO] for i in range(3)])
        hmax=sqroot(eigen_extremes(h)[1])
        difference=[sqroot(eigen_extremes(covariance(t))[1]) for t in (di,do)]
        fixed.append((c['area'],(speed*c['si'],speed*c['so']),h,hmax,difference))
    return dict(sigma=sm,mu=mu,eta=eta,gap=gap,mean=mean,ni=ni,no=no,
                dn=deltaN,cells=fixed,gap_min=eigen_extremes(gap)[0])


def bounds_for_direction(p,v):
    nv=norm(v);mv=dot(v,p['mean'])
    ve=[dot(v,n) for n in (p['ni'],p['no'])]
    d=[ab(q-mv) for q in ve]
    va=[ab(q) for q in ve]
    lower=ZERO;upper=ZERO
    for area,rot,H,_,_ in p['cells']:
        inc=[z*nv for z in rot]
        n=vmax(*[positive(dd-(p['eta']*nv+i)) for dd,i in zip(d,inc)])
        z=vmax(*[positive(q-i) for q,i in zip(va,inc)])
        tangent=positive_root(square(nv)-square(z))
        rh=positive_root(quadratic(H,v))
        y=positive(rh-p['sigma']*tangent)
        cost=area*(square(n)/p['mu']+square(y))
        lower+=low(cost);upper+=hi(cost)
    gap=quadratic(p['gap'],v)
    # Independent uniform eigenvalue bound prevents a wide direction box losing a true coercive gap.
    lower_gap=max(gap.lo,(p['gap_min']*square(nv)).lo)
    return I((I(lower_gap)-upper).lo,(hi(gap)-lower).hi)


def uniform_slack(p):
    budget=ZERO
    for area,rot,H,energy,difference in p['cells']:
        nu=vmax(*[positive(u-p['eta']-w) for u,w in zip(p['dn'],rot)])
        end=[]
        for w,delta in zip(rot,difference):
            z=positive(ONE-w)
            candidate=positive(energy-p['sigma']*positive_root(ONE-square(z)))
            # For each end, its tangential allowance is at least |P_e v|.
            end.append(I(min(candidate.hi,delta.hi)))
        y=vmax(*end)
        budget+=hi(area*(square(nu)/p['mu']+square(y)))
    return low(p['gap_min']-budget)


def face_vector(face,x,y):
    out=[None]*3
    out[face]=ONE;out[(face+1)%3]=x;out[(face+2)%3]=y
    return out


def cover(p,limit,mode,paid):
    uniform,_=paid.once([mode,'uniform'],lambda:uniform_slack(p))
    def test(v):
        return paid.once([mode,'direction',[s.bounds() for s in v]],lambda:bounds_for_direction(p,v))
    if uniform.lo>=0:
        return dict(all_directions_passed=True,excluded=False,uniform_slack_lower=str(uniform.lo),processed_boxes=0)
    vectors,_=paid.once([mode,'suggested'],lambda:[selector(p['gap'],False)]+[face_vector(i,ZERO,ZERO) for i in range(3)])
    for v in vectors:
        slack,_=test(v)
        if slack.hi<0:
            return dict(all_directions_passed=False,excluded=True,actual_direction=[z.bounds() for z in v],
                        slack=slack.bounds(),processed_boxes=0)
    # |v_j| is largest for one of the faces; homogeneity allows v_j=1, including the other sign.
    stack=[(j,-ONE,ONE,-ONE,ONE) for j in range(3)]
    done=new_boxes=0
    while stack and new_boxes<limit:
        j,a,b,c,d=stack.pop()
        vr=face_vector(j,I(a.lo,b.hi),I(c.lo,d.hi))
        slack,created=test(vr);done+=1;new_boxes+=int(created)
        if slack.lo>=0:continue
        x=(a+b)/2;y=(c+d)/2
        v=face_vector(j,x,y)
        point,_=test(v)
        if point.hi<0:
            return dict(all_directions_passed=False,excluded=True,actual_direction=[z.bounds() for z in v],
                        slack=point.bounds(),processed_boxes=done)
        if (b-a).hi>=(d-c).hi:
            stack.extend(((j,a,x,c,d),(j,x,b,c,d)))
        else:
            stack.extend(((j,a,b,c,y),(j,a,b,y,d)))
    return dict(all_directions_passed=not stack,excluded=False,processed_boxes=done,
                uniform_slack_lower=str(uniform.lo),outstanding_boxes=len(stack),
                outward_unresolved_faces=[[j,a.bounds(),b.bounds(),c.bounds(),d.bounds()] for j,a,b,c,d in stack])


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--final',type=Path,required=True);ap.add_argument('--final-sha256',required=True)
    ap.add_argument('--journal',type=Path,required=True);ap.add_argument('--journal-sha256',required=True)
    ap.add_argument('--state',type=Path,required=True)
    ap.add_argument('--eta',default='0');ap.add_argument('--curvature',default='100/3')
    ap.add_argument('--face-boxes',type=int,default=12);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();public();beg=time.monotonic()
    if args.face_boxes<0:raise ValueError('nonnegative full-box allocation required')
    eta=I(args.eta)
    if eta.lo<0 or eta.hi>=1:raise ValueError('this result uses 0<=eta<1')
    curvature=M if args.curvature=='100/3' else I(args.curvature)
    if curvature.lo<=0:raise ValueError('an actual curvature upper bound is required')
    source_dir=Path(__file__).resolve().parent
    hashes={name:hashlib.sha256((source_dir/name).read_bytes()).hexdigest() for name in
        ('r757_near_metric_pose_budget.py','r755_harmonic_area_bounds.py','r734_true_dyadic_tail.py','r726_closed_spinor_fourier.py')}
    paid=Paid(args.state,dict(final=args.final_sha256,journal=args.journal_sha256,eta=eta.bounds(),curvature=curvature.bounds(),sources=hashes))
    raw=read_artifact(args.final,args.final_sha256);lines=read_artifact(args.journal,args.journal_sha256)
    (receipt,A,L,cells),_=paid.once(['old_complete_material_prefixes'],lambda:recover(raw,lines))
    C=tuple(I(*v) for v in receipt['raw_center'])
    poses={'all_centers_easiest':(ZERO,ZERO,ZERO),'actual_terminal':C,
           'rectangle_positive':(I('.0115'),ZERO,I('.0426')),'rectangle_opposite':(I('.0115'),ZERO,I('-.0426'))}
    report={};read_seconds=time.monotonic()-beg
    for name,center in poses.items():
        t=time.monotonic()
        data,_=paid.once([name,'prepared_physical_bounds'],lambda:prepare(A,L,cells,center,eta,curvature))
        z=cover(data,args.face_boxes,name,paid)
        z['new_material_inequality_seconds']=time.monotonic()-t
        z['center']=[s.bounds() for s in center]
        report[name]=z
    final=dict(kind='terminal',original_fingerprint=receipt['fingerprint'],R755_final_sha256=args.final_sha256,
        R755_journal_sha256=args.journal_sha256,original_R738_cumulative_science=receipt['original_R738_cumulative_science'],
        original_R755_cumulative_unit_seconds=receipt['cumulative_unit_seconds'],old_material_integrals_repeated=0,
        old_J_or_ODE_repeated=0,actual_paid_radial_cells=len(cells),eta=eta.bounds(),curvature=curvature.bounds(),
        actual_cap_identity=receipt['actual_cap_identity'],source_read_and_prefix_seconds=read_seconds,poses=report,new_paid_units=paid.new,reused_paid_units=paid.old,
        new_inequality_unit_seconds=paid.new_seconds,paid_operator_identity=paid.identity,
        all_centers_excluded=report['all_centers_easiest']['excluded'],
        entire_rectangle_passes_this_necessary_gate=all(report[k]['all_directions_passed'] for k in ('rectangle_positive','rectangle_opposite')),
        source_body_or_flex_certified=False,total_seconds=time.monotonic()-beg)
    args.output.write_text(json.dumps(final,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    print('R757_FINAL',json.dumps(final,sort_keys=True,separators=(',',':')),flush=True)


if __name__=='__main__':main()
