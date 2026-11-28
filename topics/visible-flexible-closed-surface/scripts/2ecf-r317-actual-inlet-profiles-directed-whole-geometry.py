#!/usr/bin/env python3
"""Actual R317/R319 frozen Gram and six-jet geometry including all three optional physical inlet profiles."""
import argparse,gzip,hashlib,importlib.util,io,json,math,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

def load(path,name):
    S=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(S);sys.modules[name]=m;S.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ff(x):return F.from_float(float(x))
def fra(a):return [[ff(v) for v in row] for row in np.asarray(a)]

def drop_table(B,kn,raw,c):
    H=kn[-1]
    units=[v/H for v in kn]
    piece=B.extract_bezier(units,[[v] for v in raw])
    total=sum(((r-l)*H*sum(x[0] for x in z)/6 for l,r,z in piece),F(0))
    if total<=0 or min(raw)<0:raise ValueError('Invalid saved axial allocation')
    scale=c/total;acc=F(0);result=[]
    for l,r,z in piece:
        v=[scale*t[0] for t in z]
        coeff=[math.comb(5,j)*sum(((-1)**(j-h)*math.comb(j,h)*v[h] for h in range(j+1)),F(0)) for j in range(6)]
        width=(r-l)*H
        result.append((l*H,r*H,c-acc,coeff));acc+=width*sum(v)/6
    if acc!=c:raise ValueError('Exact height drop failed')
    return result

def fullnative(core,c,t,left,right,scale,tr,m):
    rows=core.horn(c,(t-left)/(right-left),(right-left)*scale)
    out=[]
    for r,d in core.ORD:
        a=rows[r];x=core.I(0);y=core.I(0);z=core.I(0)
        for j in range(m+1):
            si,co=tr(j);ct=(co,-si,-co)[d];st=(si,co,-si)[d];f=j**d
            x+=a[...,j]*f*ct;z+=a[...,2*m+1+j]*f*ct
            if j:y+=a[...,m+j]*f*st
        out.append([x,y,z])
    return out

def relative_gram(core,J,Q,W,rho):
    I=core.I;E=core.sq(J[1]);cross=core.dot(J[1],J[2]);G=core.sq(J[2])
    if np.any(Q.lo<=0) or np.any(W.lo<=0) or np.any(rho.lo<=0):raise ArithmeticError('Failed common positive metric enclosure')
    u=E/Q-1;v=G/(rho.square()*W)-1
    # The normalized off-diagonal appears squared, so Q*W suffices.
    ab=cross.square()/(Q*W*rho.square())
    z=(u-v).square()/4+ab
    rad=I(np.maximum(0,z.lo),z.hi).sqrt()
    return (I((u+v).abs_upper())/2+rad).hi

def main():
    ap=argparse.ArgumentParser()
    for arg in ('scripts','work','state','out'):ap.add_argument('--'+arg,type=Path,required=True)
    ap.add_argument('--core',type=Path)
    ap.add_argument('--moments',type=Path)
    ap.add_argument('--physical-source',type=Path)
    ap.add_argument('--metric-ceiling',type=F)
    ap.add_argument('--require-shape',action='store_true')
    ap.add_argument('--full-prefix',action='store_true')
    ap.add_argument('--elements',type=int,nargs='+')
    ap.add_argument('--start',type=int,default=0);ap.add_argument('--count',type=int,default=1)
    ap.add_argument('--angles',type=int,default=96);ap.add_argument('--depth',type=int,default=2)
    ap.add_argument('--K',default='200/23');ap.add_argument('--support',default='23/200');ap.add_argument('--height',default='87/250')
    ap.add_argument('--arc-divisions',type=int,default=8192)
    a=ap.parse_args();t0=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh directed output required')
    S=a.scripts;fielddir=a.work/'h2-c2-m48-g12-04r1';data=a.work/'m12-prefix-data.npz.gz'
    native=load(S/'prefix-production-kernel/m12-prefix-total-gram-full.py','strict_original_R262')
    core=load(a.core or S/'2ecf-r262-true-three-arcs-cut-directed-position-kernel.py','new_full_R262_six_jets');core.setup(native)
    base,k,I=native.base,native.kern,native.I
    O=native.load('R262_trueD3_original_cells',S/'6a65-m12-up-patch-exact-geometry-budget.py')
    B=native.load('R262_trueD3_Bezier',S/'6a65-m12-local-bernstein-angular-metric-budget.py')
    supplier=native.load('R262_original_chart',S/'78718-prefix-metric-supplier-storage-v1.py')
    notes=S.parent/'notes';mp=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    bp=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    meta=json.loads(mp.read_text());bridge=json.loads(bp.read_text())
    if sha(data)!=B.DATA_SHA or sha(mp)!=B.META_SHA or sha(bp)!=B.BRIDGE_SHA:raise ValueError('Original source SHA differs')
    man=S.parent/meta['tail_manifest'];manifest=json.loads(man.read_text())
    if sha(man)!=meta['tail_manifest_sha256']:raise ValueError('Manifest does not bind original source')
    cut,cuff=[ff(manifest['parameters'][z]) for z in ('rCut','rCuff')]
    field=fielddir/'result.json.field.npz';result=json.loads((fielddir/'result.json').read_text())
    query=fielddir/'exact-tail-queries.json';qcache=Path(str(query)+'.npz')
    if sha(field)!=result['field_sha256']:raise ValueError('Actual parent-field result differs')
    with np.load(io.BytesIO(gzip.decompress(data.read_bytes())),allow_pickle=False) as z:
        raw={key:z[key].copy() for key in ('mesh','jets','mean_increments')}
    D=native.source.FullSource(raw,meta,bridge,supplier,O,query,qcache,result)
    # The original helper was initially built on a cutoff rounded to .15.
    D.total=D.S+(cut-cuff)
    D.Klo=D.end*(D.Shi+cut-cuff)/D.Shi;D.Khi=D.end*(D.Slo+cut-cuff)/D.Slo
    rows=fra(raw['jets'][:,0,:])
    C=base.centralmod.Central(rows,D.warp*D.chart[0][0],2*D.warp*D.chart[0][2]/D.end**2)
    means=[F(0)]
    for x in raw['mean_increments']:means.append(means[-1]+ff(x))
    with np.load(field,allow_pickle=False) as z:
        pm=list(map(int,z['planar_modes']));hm=list(map(int,z['vertical_modes']))
        ow=B.extract_bezier(list(map(ff,z['unit_knots'])),fra(z['coefficients']))
    with np.load(a.state,allow_pickle=False) as st:
        if str(st['fieldSHA'])!=sha(field):raise ValueError('New state has another old field')
        expected_source='94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6'
        expected_cut='4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8'
        expected_angles='a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e'
        if [str(st[x]) for x in ('sourceSHA','cutSHA','comparisonSHA')]!=[expected_source,expected_cut,expected_angles]:
            raise ValueError('Different registered normal-angle curve, source or cut')
        if 'heightDropEnd' in st or float(st['lam'])!=1 or float(st['low'])!=.63:
            raise ValueError('Require full adjacent-port cut')
        is_cut=True;profile='physicalInletProfiles' in st;anchor=ff(st['anchor'])
        numericC=ff(st['fullSleeve']);c=F(str(float(st['fullSleeve'])))
        if c not in map(F,('.350','.545','.660','.780')):raise ValueError('Unknown R317/R319 sleeve')
        phys=load(a.physical_source or S/'2ecf-r262-adjacent-low-ports-support-physical-cut.py','R317_source_physical')
        if sha(phys.__file__)!=expected_source:raise ValueError('Unbound physical source')
        moments=load(a.moments or S/'2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py','R317_moments')
        arc=moments.Arc(core,phys,anchor)
        lift=F(str(float(st['liftEnd'])));physicalS=ff(st['S']);gate_width=F(str(float(st['fullGate'])))
        mk=int(st['modes']);xx=list(map(ff,st['knots']));origin=c
        if profile:
            if str(st['inletProfileSourceSHA'])!='4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa':
                raise ValueError('Unknown three-column physical source')
            X=np.asarray(st['inletNativeXYZ']);ex=np.asarray(st['physicalInletProfiles'])
            if ex.shape!=(len(X),3) or 'actualPhysicalXYZ' in st:raise ValueError('Ambiguous field layout')
        else:X=np.asarray(st['actualPhysicalXYZ']);ex=np.zeros((len(X),3))
        keys={'fieldSHA','sourceSHA','comparisonSHA','cutSHA','S','T','fullGate','fullSleeve','liftEnd','lam','low','anchor',
              'metricQ','metricW','metricKnots','knots','modes','spans','reduced','actualPhysicalXYZ','inletNativeXYZ',
              'physicalInletProfiles','inletProfileSourceSHA'}
        if set(st.files)-keys:raise ValueError('Unbound additional state arrays: '+str(set(st.files)-keys))
        if xx[0]!=numericC or xx[-1]!=physicalS or X.shape!=(len(xx)-12,3*mk+2):raise ValueError('Cartesian knots differ')
        d3=not np.any(X[:,0]) and all(not np.any(X[:,j]) and not np.any(X[:,mk+j]) for j in range(3,mk+1,3))
        d3=d3 and all(np.array_equal(X[:,mk+j],X[:,j]*(1 if j%3==1 else -1)) for j in range(1,mk+1) if j%3)
        d3=d3 and all(not np.any(X[:,2*mk+1+j]) for j in range(1,mk+1) if j%3)
        d3=d3 and all(j%3==1 for j in pm) and all(j%3==0 for j in hm)
        normalized=lambda z:[(v-numericC)/(physicalS-numericC) for v in z]
        position=B.extract_bezier(normalized(xx),fra(np.column_stack((X,ex))))
        metkn=list(map(ff,st['metricKnots'])) if 'metricKnots' in st else xx
        if metkn[0]!=numericC or metkn[-1]!=physicalS:raise ValueError('Frozen metric chart differs')
        qv,wv=st['metricQ'],st['metricW']
        if min(1+min(map(ff,qv)),1+min(map(ff,wv)))<=0:raise ValueError('Frozen metric not positive')
        metric=B.extract_bezier(normalized(metkn),fra(np.column_stack((qv,wv))))
    position=[(l,r,core.power([v[:-3] for v in z]),core.power([v[-3:] for v in z])) for l,r,z in position]
    metric=[(l,r,core.power(z)) for l,r,z in metric]
    new=[]
    for xl,xr,vb,eb in position:
        for ml,mr,mb in metric:
            el,er=max(xl,ml),min(xr,mr)
            if el<er:new.append((el,er,(xl,xr,vb,eb),(ml,mr,mb)))
    mouthParts=[]
    if profile:
        ncl,ncr=D.lamlo*c,D.lamhi*c
        for oldpiece in ow:
            if oldpiece[1]*D.Khi<ncl or oldpiece[0]*D.Klo>ncr:continue
            owc=core.power(oldpiece[2]);groups,_=native.intersections(D,oldpiece)
            for (ch_i,target_i,active,common),group in groups.items():
                for row in group:
                    if row['right']>=ncl and row['left']<=ncr:
                        mouthParts.append((row['cell'],D.chart_pieces[ch_i],active,oldpiece[0],oldpiece[1],owc))
        if not mouthParts:raise ArithmeticError('Missing true q=c')
    K=I(F(a.K));sig=I(F(a.support));Z=I(F(a.height))
    elements=[i for i,p in enumerate(ow) if p[0]*D.Klo<D.end and p[1]*D.Khi>D.lamlo*origin]
    selected=elements if a.full_prefix else (a.elements if a.elements is not None else elements[a.start:a.start+a.count])
    if not selected or len(set(selected))!=len(selected) or any(i not in elements for i in selected):raise ValueError('Invalid selected prefix elements')
    anglecache={};seen={};bad=[];closed=[];best={z:float('inf') for z in ['height','support','area2','curvatureFormMin']}
    totalRows=0;accepted=0;unresolved=0;metric_upper=F(0);metric_exceeded=0;geom_unresolved=0
    shape_upper=[F(0),F(0)];shape_unresolved=0
    angleMultiplier=3 if d3 else 1
    metric_limit=I(a.metric_ceiling) if a.metric_ceiling is not None else None
    def angular(depth):
        count=a.angles*(2**depth)
        if depth not in anglecache:
            e=2*k.PI*I(np.arange(count+1,dtype=k.LD))/(angleMultiplier*count)
            theta=I(e.lo[:-1],e.hi[1:])
            angles=core.angular(C,D.lam,arc,theta)
            angles['nk']=arc.last['nk'];angles['hz']=arc.last['hz']
            if profile:
                drows=[]
                for cell,ch,active,wl,wr,owc in mouthParts:
                    J=core.source(D,cell,D.lam*c,ch,angles,means[cell],active)
                    W=core.spectral(owc,I(c)/D.total,wl,wr-wl,D.total,pm,hm,angles['tr'])
                    vals=[]
                    for h,j in enumerate((0,2,5)):
                        factor=1-(c/lift)**3*(10-15*c/lift+6*(c/lift)**2)
                        vec=core.add(J[j],W[j],core.mul(angles['delta'][h],factor))
                        vec=core.sub(vec,angles['newArc'][h])
                        if h==0:vec[2]=vec[2]-c
                        vals.append(vec)
                    drows.append(vals)
                angles['gateResidual']=[[I(np.minimum.reduce(np.broadcast_arrays(*[q[h][j].lo for q in drows])),
                                           np.maximum.reduce(np.broadcast_arrays(*[q[h][j].hi for q in drows])))
                                         for j in range(3)] for h in range(3)]
            anglecache[depth]=angles
        return anglecache[depth],count
    def getang(depth,ids):
        full,count=angular(depth)
        t=full['tr'].theta[ids]
        a0={key:full[key][ids] for key in ['u','up','upp']}
        a0['tr']=core.BoxTrig(t)
        for key in ['delta','d0','d2','newArc','nk','hz']+(['gateResidual'] if profile else []):
            a0[key]=[[v[ids] if v.shape else v for v in row] for row in full[key]]
        return a0
    expectedField='5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8'
    def save(final):
        out=dict(schema='R317-R319-actual-native-and-three-angular-profiles-closed-box-Gram-and-geometry-v1',completed=final,allSelectedPassed=final and unresolved==0,
                 wholeOriginalCutPrefixCovered=(final and set(selected)==set(elements)),physicalProfilesPresent=profile,fullNativeAnglePeriod=('2pi/3' if d3 else '2pi'),analyticMomentAudit=arc.audit(),
                 leafUpperRelativeGramExact=str(metric_upper),leafUpperRelativeGram=float(metric_upper),metricCeiling=(str(a.metric_ceiling) if metric_limit is not None else None),
                 unresolvedMetricBoxes=metric_exceeded,unresolvedGeometryBoxes=geom_unresolved,
                 leafUpperOriginAndArmMixedSquares=[str(z) for z in shape_upper],shapeRequired=bool(a.require_shape),unresolvedShapeBoxes=shape_unresolved,allOriginalPrefixElements=elements,selected=selected,closed=closed,originalFieldSHA256=sha(field),historicalMatch=sha(field)==expectedField,
                 stateSHA256=sha(a.state),originalDataSHA256=sha(data),manifestSHA256=sha(man),sourceSHA256=sha(__file__),kernelSHA256=sha(core.__file__),
                 nativeSourceCells=len(D.mesh)-1,commonRefinedRows=totalRows,acceptedBoxes=accepted,unresolvedBoxes=unresolved,firstUnresolved=bad[:6],
                 acceptedDirectedMinima={z:(float(v) if np.isfinite(v) else None) for z,v in best.items()},
                 limits=dict(curvature=a.K,support=a.support,height=a.height),sleeveExact=str(c),storedSleeveExact=str(numericC),actualCuffExact=str(cuff),
                 geometryFamily='true-R317-circle-input-and-R317-or-R319-registered-cut',metricClock='new radial spline coefficients evaluated at origin+(Sf-origin)(s-origin)/(S-origin), with actual algebraic S; old W evaluated with actual T1',seconds=time.monotonic()-t0,
                 scope='Only the explicitly selected outer prefix cover. Each box consumes all six jets, original tail interface, optional Cauchy profiles and a common frozen metric. The central belt and post-prefix full tail are separate.')
        path=a.out if final else a.out.with_suffix('.progress.json')
        tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');tmp.replace(path)
    for element in selected:
        wl,wr,ctrl=ow[element];wp=core.power(ctrl);groups,_=native.intersections(D,ow[element])
        startFailed=unresolved
        for (ch_i,target_i,active,common),group in groups.items():
            ch=D.chart_pieces[ch_i]
            for row in group:
                cell=row['cell'];L,R=max(row['left'],D.lamlo*origin),row['right']
                if R<=L:continue
                actual=[]
                for el,er,(xl,xr,coeff,ep),(ml,mr,mc) in new:
                    nlo=max(L,D.end*el+D.lamlo*origin*(1-el));nhi=min(R,D.end*er+D.lamhi*origin*(1-er))
                    if nhi<=nlo:continue
                    for hiH,HL,HR in [(True,F(0),D.lamhi*lift),(False,D.lamlo*lift,D.end)]:
                        tl=max(nlo,HL);tr=min(nhi,HR)
                        if tr<=tl:continue
                        windows=[(-2,D.lamlo*c,D.lamhi*(c+gate_width)),(-1,D.lamlo*(c+gate_width),D.end)]
                        for dp,dl,dr in windows:
                            ll=max(tl,dl);rr=min(tr,dr)
                            if rr<=ll:continue
                            actual.append((ll,rr));totalRows+=1
                            def cover(l,r,depth,ids):
                                nonlocal accepted,unresolved,metric_upper,metric_exceeded,geom_unresolved,shape_unresolved
                                angle=getang(depth,ids);n=I.bounds(l,r);s=n/D.lam;t=(s-origin)/(D.S-origin)
                                J=core.source(D,cell,n,ch,angle,means[cell],active)
                                W=core.spectral(wp,s/D.total,wl,wr-wl,D.total,pm,hm,angle['tr'])
                                if d3:V=core.spectral(coeff,t,xl,xr-xl,D.S-origin,(),(),angle['tr'],True)
                                else:V=fullnative(core,coeff,t,xl,xr,D.S-origin,angle['tr'],mk)
                                for j in range(6):J[j]=core.add(J[j],W[j])
                                if hiH:core.apply_lift(J,angle['delta'],core.cpolys([1,0,0,-10,15,-6],s,lift))
                                J=core.cut_blend(J,angle,s,c,gate_width,dp==-2)
                                for j in range(6):J[j]=core.add(J[j],V[j])
                                if profile:
                                    ev=core.horn(ep,(t-xl)/(xr-xl),(xr-xl)*(D.S-origin))
                                    for ix,name in enumerate(('nk','gateResidual','hz')):
                                        core.apply_lift(J,angle[name],[row[...,ix] for row in ev])
                                mv=base.horner_rows(mc,(t-ml)/(mr-ml));Q=1+mv[...,0];U=1+mv[...,1]
                                f=D.target_pieces[target_i]['evaluator'](s)
                                gg=core.cpolys([0,0,0,10,-15,6],s-c,gate_width)[0] if dp==-2 else I(1)
                                rho=(1+core.clamp(gg,0,1)*(f-1))*angle['up']
                                gram=relative_gram(core,J,Q,U,rho)
                                ans=core.geometry(J,K)
                                geom_ok=np.zeros(len(ids),dtype=bool) if ans is None else ((ans['height']>Z.hi)&(ans['support']>sig.hi)&(ans['curvatureFormMin']>0))
                                gm_ok=np.ones(len(ids),dtype=bool) if metric_limit is None else gram<=metric_limit.lo
                                p=J[0];rr2=p[0].square()+p[1].square()
                                rr=I(np.maximum(0,rr2.lo),rr2.hi).sqrt()
                                sh1=(rr2+p[2].square()).hi
                                sh2=((F('2.194')+rr).square()+(F('.233')+I(p[2].abs_upper())).square()).hi
                                sh_ok=(sh1<=I(F('1.915')**2).lo)&(sh2<=I(F('3.830')**2).lo)
                                ok=geom_ok&gm_ok&(sh_ok if a.require_shape else True)
                                keep=np.ones(len(ids),dtype=bool) if depth>=a.depth else ok
                                if np.any(keep):
                                    for pos,z in enumerate((sh1,sh2)):
                                        shape_upper[pos]=max(shape_upper[pos],k.exact(k.up(z[keep].max())))
                                if ans is not None and np.any(ok):
                                    for key in best:best[key]=min(best[key],float(np.nextafter(float(np.min(np.broadcast_to(ans[key],ok.shape)[ok])),-np.inf)))
                                if np.any(ok):metric_upper=max(metric_upper,k.exact(k.up(gram[ok].max())))
                                accepted+=int(np.count_nonzero(ok))
                                pending=ids[~ok]
                                if not len(pending):return
                                if depth>=a.depth:
                                    if a.require_shape:shape_unresolved+=int(np.count_nonzero(~sh_ok))
                                    unresolved+=len(pending);geom_unresolved+=int(np.count_nonzero(~geom_ok));metric_exceeded+=int(np.count_nonzero(~gm_ok))
                                    metric_upper=max(metric_upper,k.exact(k.up(gram[~ok].max())))
                                    if len(bad)<6:bad.append(dict(element=element,cell=cell,native=[str(l),str(r)],depth=depth,firstAngleIndex=int(pending[0])))
                                    return
                                children=(2*pending[:,None]+np.array([[0,1]])).ravel();mid=(l+r)/2
                                cover(l,mid,depth+1,children);cover(mid,r,depth+1,children)
                            cover(ll,rr,0,np.arange(a.angles))
                covered=L
                for l,r in sorted(actual):
                    if l>covered:raise ArithmeticError('Gap in actual physical source partition')
                    covered=max(covered,r)
                if covered<R:raise ArithmeticError('Uncovered end of source cell')
        closed.append(dict(element=element,unresolved=unresolved-startFailed))
        print('DIRECTED',element,accepted,unresolved,best,flush=True);save(False)
    save(True)
if __name__=='__main__':main()
