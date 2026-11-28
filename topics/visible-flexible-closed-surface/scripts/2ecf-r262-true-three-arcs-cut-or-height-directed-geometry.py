#!/usr/bin/env python3
"""Directed continuous height, radial support and both curvature forms of the actual all-original-ring R262/true-D3 prefix."""
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

def main():
    ap=argparse.ArgumentParser()
    for arg in ('scripts','work','state','out'):ap.add_argument('--'+arg,type=Path,required=True)
    ap.add_argument('--core',type=Path)
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
        is_cut='heightDropEnd' not in st
        if (not is_cut and 'rawDropVelocity' not in st) or float(st['lam'])!=1:raise ValueError('Require actual full-amplitude cut or LP allocation')
        low=float(st['low'])
        if low not in (.25,.35) or abs(float(st['anchor'])-np.pi/3)>2e-16:raise ValueError('Require a registered aligned R309 inlet')
        arc=core.TrueArc(F(1,4) if low==.25 else F(7,20),a.arc_divisions)
        c=ff(st['fullSleeve']);lift=ff(st['liftEnd']);physicalS=ff(st['S']);X=np.asarray(st['actualPhysicalXYZ'])
        xx=list(map(ff,st['knots']));mk=int(st['modes'])
        origin=c if is_cut else F(0)
        if xx[0]!=origin or xx[-1]!=physicalS or X.shape[1]!=3*mk+2:raise ValueError('Actual physical Cartesian knots differ')
        if np.any(X[:,0]) or any(np.any(X[:,j]) or np.any(X[:,mk+j]) for j in range(3,mk+1,3)):raise ValueError('Forbidden planar D3 channels')
        if any(not np.array_equal(X[:,mk+j],X[:,j]*(1 if j%3==1 else -1)) for j in range(1,mk+1) if j%3):raise ValueError('Cartesian D3/reflection changed')
        if any(np.any(X[:,2*mk+1+j]) for j in range(1,mk+1) if j%3):raise ValueError('Forbidden height channels')
        new=B.extract_bezier([(v-origin)/(physicalS-origin) for v in xx],fra(X))
        gate_width=ff(st['fullGate'])
        if is_cut:
            drop=[];H=F(0)
        else:
            drop=drop_table(B,list(map(ff,st['rawDropKnots'])),list(map(ff,st['rawDropVelocity'])),c)
            H=drop[-1][1]
            if H!=ff(st['heightDropEnd']):raise ValueError('Actual LP endpoint differs')
    new=[(l,r,core.power(z)) for l,r,z in new]
    K=I(F(a.K));sig=I(F(a.support));Z=I(F(a.height))
    elements=[i for i,p in enumerate(ow) if p[0]*D.Klo<D.end and p[1]*D.Khi>D.lamlo*origin]
    selected=a.elements if a.elements is not None else elements[a.start:a.start+a.count]
    if not selected or len(set(selected))!=len(selected) or any(i not in elements for i in selected):raise ValueError('Invalid selected prefix elements')
    anglecache={};seen={};bad=[];closed=[];best={z:float('inf') for z in ['height','support','area2','curvatureFormMin']}
    totalRows=0;accepted=0;unresolved=0
    def angular(depth):
        count=a.angles*(2**depth)
        if depth not in anglecache:
            e=k.PI*I(np.arange(count+1,dtype=k.LD))/(3*count)
            theta=I(e.lo[:-1],e.hi[1:])
            anglecache[depth]=core.angular(C,D.lam,arc,theta)
        return anglecache[depth],count
    def getang(depth,ids):
        full,count=angular(depth)
        t=full['tr'].theta[ids]
        a0={key:full[key][ids] for key in ['u','up','upp']}
        a0['tr']=core.BoxTrig(t)
        for key in ['delta','d0','d2','newArc']:
            a0[key]=[[v[ids] if v.shape else v for v in row] for row in full[key]]
        return a0
    expectedField='5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8'
    def save(final):
        out=dict(schema='R262-true-three-arcs-complete-cut-or-axial-prefix-directed-local-geometry-v2',completed=final,allSelectedPassed=final and unresolved==0,
                 allOriginalPrefixElements=elements,selected=selected,closed=closed,originalFieldSHA256=sha(field),historicalMatch=sha(field)==expectedField,
                 stateSHA256=sha(a.state),originalDataSHA256=sha(data),manifestSHA256=sha(man),sourceSHA256=sha(__file__),kernelSHA256=sha(core.__file__),
                 nativeSourceCells=len(D.mesh)-1,commonRefinedRows=totalRows,acceptedBoxes=accepted,unresolvedBoxes=unresolved,firstUnresolved=bad[:6],
                 acceptedDirectedMinima={z:(float(v) if np.isfinite(v) else None) for z,v in best.items()},
                 limits=dict(curvature=a.K,support=a.support,height=a.height),sleeveExact=str(c),actualCuffExact=str(cuff),
                 geometryFamily=('true-cut-and-sleeve' if is_cut else 'full-original-rings-LP'),metricClock='new radial spline coefficients evaluated at origin+(Sf-origin)(s-origin)/(S-origin), with actual algebraic S; old W evaluated with actual T1',seconds=time.monotonic()-t0,
                 scope='Only the explicitly selected continuous native/W/XYZ/drop/central/angle cover. New time action preserves these three observables. Tail transfer and full diameter/holding are separate.')
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
                for xl,xr,coeff in new:
                    nlo=max(L,D.end*xl+D.lamlo*origin*(1-xl));nhi=min(R,D.end*xr+D.lamhi*origin*(1-xr))
                    if nhi<=nlo:continue
                    for hiH,HL,HR in [(True,F(0),D.lamhi*lift),(False,D.lamlo*lift,D.end)]:
                        tl=max(nlo,HL);tr=min(nhi,HR)
                        if tr<=tl:continue
                        if is_cut:
                            windows=[(-2,D.lamlo*c,D.lamhi*(c+gate_width)),(-1,D.lamlo*(c+gate_width),D.end)]
                        else:
                            windows=[(i,D.lamlo*d[0],D.lamhi*d[1]) for i,d in enumerate(drop)]+[(-1,D.lamlo*H,D.end)]
                        for dp,dl,dr in windows:
                            ll=max(tl,dl);rr=min(tr,dr)
                            if rr<=ll:continue
                            actual.append((ll,rr));totalRows+=1
                            def cover(l,r,depth,ids):
                                nonlocal accepted,unresolved
                                angle=getang(depth,ids);n=I.bounds(l,r);s=n/D.lam;t=(s-origin)/(D.S-origin)
                                J=core.source(D,cell,n,ch,angle,means[cell],active)
                                W=core.spectral(wp,s/D.total,wl,wr-wl,D.total,pm,hm,angle['tr'])
                                V=core.spectral(coeff,t,xl,xr-xl,D.S-origin,(),(),angle['tr'],True)
                                for j in range(6):J[j]=core.add(J[j],W[j])
                                if hiH:core.apply_lift(J,angle['delta'],core.cpolys([1,0,0,-10,15,-6],s,lift))
                                if dp>=0:
                                    pl,pr,offset,p=drop[dp];v=(s-pl)/(pr-pl)
                                    z0=offset-(pr-pl)*k.poly([F(0)]+[v/F(j+1) for j,v in enumerate(p)],v)
                                    z1=-k.poly(p,v);z2=-k.poly([j*v for j,v in enumerate(p) if j],v)/(pr-pl)
                                    for j,zz in zip((0,1,3),(z0,z1,z2)):J[j][2]=J[j][2]+zz
                                if is_cut:J=core.cut_blend(J,angle,s,c,gate_width,dp==-2)
                                for j in range(6):J[j]=core.add(J[j],V[j])
                                ans=core.geometry(J,K)
                                ok=np.zeros(len(ids),dtype=bool) if ans is None else ((ans['height']>Z.hi)&(ans['support']>sig.hi)&(ans['curvatureFormMin']>0))
                                if ans is not None and np.any(ok):
                                    for key in best:best[key]=min(best[key],float(np.nextafter(float(np.min(np.broadcast_to(ans[key],ok.shape)[ok])),-np.inf)))
                                accepted+=int(np.count_nonzero(ok))
                                pending=ids[~ok]
                                if not len(pending):return
                                if depth>=a.depth:
                                    unresolved+=len(pending)
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
