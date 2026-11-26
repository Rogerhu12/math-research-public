#!/usr/bin/env python3
"""Numerical evaluator of the fixed original M12 analytic tail background.

The definition is the existing FrozenSource: the same 160 exact binary cell
constants, analytic lengths/cap/weights, and the exact integral-normalized
alpha. This module evaluates that definition numerically; adaptive Gauss
differences are diagnostics, never rigorous remainder certificates. It is
not a new background made from rounded alpha or a fitted w polynomial.

Queries return w and its actual analytic radial derivative wd/(A+alpha B),
and the rotational height drop from the cut. At the actual cuff, w=wr=0 is
the original C2 limit. The infinite old-radius tail below protected cell
160 is not replaced in the mathematical definition. Its tiny contribution
is separately identified when reporting numerical finite-cell totals.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np

LD=np.longdouble


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def gauss(n):
    """Long-double Newton Legendre nodes, avoiding binary64 quadrature tables."""
    pi=np.arccos(LD(-1));x=np.cos(pi*(np.arange(n,dtype=LD)+LD('.75'))/(n+LD('.5')))
    for unused in range(20):
        p=np.ones(n,LD);q=np.zeros(n,LD)
        for k in range(1,n+1):p,q=((2*k-1)*x*p-(k-1)*q)/k,p
        dp=n*(x*p-q)/(x*x-1);step=p/dp;x-=step
        if np.max(abs(step))<LD('2e-20'):break
    # Re-evaluate at the final nodes; normalize only quadrature roundoff.
    p=np.ones(n,LD);q=np.zeros(n,LD)
    for k in range(1,n+1):p,q=((2*k-1)*x*p-(k-1)*q)/k,p
    dp=n*(x*p-q)/(x*x-1);w=2/((1-x*x)*dp*dp)
    return x,w


GX={n:gauss(n) for n in (16,32)}


class FrozenNumericalSource:
    def __init__(self,parameters,frozen):
        self.p=parameters;self.frozen=frozen
        for key,value in frozen['calibrationParameters'].items():
            if parameters.get(key)!=value:raise ValueError('Frozen calibration parameter changed: '+key)
        p=parameters
        if len(frozen['constants'])!=160 or p['protectCell']!=160 or p['orientation']!=1:
            raise ValueError('Requires the original 160-cell positively oriented background')
        if p['etaPower']!=1.5 or p['capMode']!='cut-preserving' or p.get('flatOuterThroughCell',-1)>=0 or p.get('rejoinR20At') is not None:
            raise ValueError('Different tail definition')
        self.delta0=LD(p['delta0']);self.eta0=self.delta0*LD(p['etaRatioAtN0'])
        self.root12=np.sqrt(LD(12));self.q=1/(2*np.sqrt(LD(2)));self.log2=np.log(LD(2))
        self.total=6*self.delta0+6*self.eta0/(1-self.q)
        self.cuff=LD(p['rCuff']);self.cut=LD(p['rCut'])
        self.oldcut=self.cuff*np.exp(self.total/self.root12)
        self.logdelta=np.log(self.delta0);self.logwcut=np.log(LD(p['wCut']))
        self.a=LD(p['a']);self.cells={}

    def cell(self,n):
        if n in self.cells:return self.cells[n]
        p=self.p;d=self.delta0/LD(2)**n;eta=self.eta0*self.q**n
        after=3*d+6*eta*self.q/(1-self.q);ld=self.logdelta-n*self.log2
        cal=self.frozen['constants'][n]['value']
        if float.fromhex(self.frozen['constants'][n]['hex'])!=cal:raise ValueError('Calibration binary identity mismatch')
        R=p['prefixRByCell'][n] if n<=p['prefixEnd'] else p['R']
        beta=LD(p['valleyControls'][n]) if n<len(p['valleyControls']) else LD(0)
        levels=[ld,np.log(LD(R)),2*ld-np.log(LD(cal))+beta,LD(0),ld+self.a*self.log2]
        desc=[(0,0,eta),(0,1,eta),(1,1,d),(1,2,eta),(2,2,d),(2,3,eta),(3,3,d),(3,4,eta),(4,4,eta)]
        pulse=p.get('pulseCaps',[]);valley=p.get('valleyCaps',[])
        pulse=pulse[n] if n<len(pulse) else [p['slopeCap']]*2
        valley=valley[n] if n<len(valley) else p['slopeCap']
        caps=np.asarray([p['slopeCap'],pulse[0],valley,pulse[1],p['slopeCap']],LD)
        weights=p.get('warpWeightLevels',[]);weights=np.asarray(weights[n] if n<len(weights) else [1]*5,LD)
        offset=LD(0);segments=[]
        for left,right,length in desc:
            segments.append((levels[left],levels[right],length,offset));offset+=length
        result=(after,segments,np.log(caps),np.log(weights),caps,weights)
        self.cells[n]=result;return result

    def evaluate(self,n,j,x):
        x=np.asarray(x,LD);after,segments,lcaps,lweights,caps,weights=self.cell(n)
        lo,hi,length,offset=segments[j]
        S=x**3*(10+x*(-15+6*x));Sd=30*x*x*(1-x)*(1-x)
        shape=lo+(hi-lo)*S;shape_d=(hi-lo)*Sd
        distance=after+offset+x*length
        raw=self.logwcut-self.a*self.log2-(self.a-1)*n*self.log2-self.logdelta+(self.total-distance)*7/self.root12+shape
        raw_d=-7*length/self.root12+shape_d
        if j%2==0:
            caplog=lcaps[j//2];caplog_d=LD(0);weight=weights[j//2];fixedcap=caps[j//2]
        else:
            k=(j-1)//2;caplog=lcaps[k]+S*(lcaps[k+1]-lcaps[k]);caplog_d=Sd*(lcaps[k+1]-lcaps[k])
            weight=np.exp(lweights[k]+S*(lweights[k+1]-lweights[k]))
            fixedcap=caps[k] if caps[k]==caps[k+1] else None
        L=LD(self.p['capTransition']);t=(raw-caplog+L)/(2*L);tc=np.clip(t,0,1);u=1-tc
        def J(z):return z**5*(7+z*(-14+z*(10-LD('2.5')*z)))
        def P(z):return z**4*(35+z*(-84+z*(70-20*z)))
        middle_shape=np.where(tc<=LD('.5'),tc-J(tc),LD('.5')-J(u))
        d=np.where(tc<=LD('.5'),1-P(tc),P(u))
        logw=np.where(t<=0,raw,np.where(t>=1,caplog,caplog-L+2*L*middle_shape))
        logwd=np.where(t<=0,raw_d,np.where(t>=1,caplog_d,d*raw_d+(1-d)*caplog_d))
        if n==0 and j==7:
            logwd=Sd*(raw-logw)+S*raw_d+(1-S)*logwd
            logw=S*raw+(1-S)*logw
        elif n==0 and j==8:logw,logwd=raw,raw_d
        w=np.exp(logw);wd=w*logwd
        if fixedcap is not None and not (n==0 and j in (7,8)):
            w=np.where(t>=1,fixedcap,w);wd=np.where(t>=1,LD(0),wd)
        E=1+w*w;rx=self.cuff*np.exp(distance/self.root12)*length/self.root12
        chi=1-S if n==0 and j==8 else S if n==159 and j==0 else LD(1)
        j0=1+S*(self.cut/self.oldcut-1) if n==0 and j==8 else LD(1)
        A=rx*j0*(1-chi)+chi*abs(wd)/(LD(self.p['curvatureBound'])*E*np.sqrt(E))
        B=chi*rx/E*weight
        return A,B,w,wd

    def raw_critical_nodes(self,n,j):
        """Consume the already audited inner-warp stable critical formula.

        For the constant inner caps these include every uncapped turning
        point; tiny endpoint lobes must not be left to blind Gauss probes.
        Extra splitting of a fully capped interval changes no integral.
        """
        unused,segments,*rest=self.cell(n);lo,hi,length,offset=segments[j]
        jump=hi-lo;lam=7*length/self.root12
        if jump<=0 or jump*LD(15)/8<=lam:return []
        h=np.sqrt(lam/(30*jump));root=2*h/(1+np.sqrt(1-4*h))
        return [root,1-root]


class ProfilePrimitive:
    def __init__(self,source,n,j,tolerance=LD('2e-18')):
        self.source,self.n,self.j,self.tolerance=source,n,j,LD(tolerance)
        self.leaves=[];self.evaluations=0;self.error=np.zeros(6,LD);self.max_depth=0
        nodes=np.unique(np.r_[np.arange(9,dtype=LD)/8,source.raw_critical_nodes(n,j)])
        for left,right in zip(nodes[:-1],nodes[1:]):self.integrate(left,right,save=True)
        self.leaves.sort(key=lambda row:row[0])
        self.left=np.asarray([x[0] for x in self.leaves],LD);self.right=np.asarray([x[1] for x in self.leaves],LD)
        values=np.asarray([x[2] for x in self.leaves],LD)
        self.prefix=np.vstack((np.zeros((1,6),LD),np.cumsum(values,axis=0,dtype=LD)))
        self.total=self.prefix[-1].copy()

    def integrand(self,x):
        A,B,w,unused=self.source.evaluate(self.n,self.j,x);root=np.sqrt(1+w*w)
        return np.stack((A,B,root*A,root*B,w*A,w*B),axis=-1)

    def quadrature(self,left,right,n):
        x,w=GX[n];half=(right-left)/2;mid=(left+right)/2
        self.evaluations+=n
        return half*np.sum(self.integrand(mid+half*x)*w[:,None],axis=0,dtype=LD)

    def integrate(self,left,right,depth=0,save=False):
        if left==right:return np.zeros(6,LD)
        low=self.quadrature(left,right,16);high=self.quadrature(left,right,32)
        error=abs(high-low);budget=self.tolerance*(abs(high)+LD('.01')*(right-left))
        # The comparison is a numerical refinement rule, not an enclosure.
        if np.all(error<=budget) or depth>=22:
            if save:
                self.leaves.append((left,right,high));self.error+=error;self.max_depth=max(self.max_depth,depth)
            return high
        mid=(left+right)/2
        return self.integrate(left,mid,depth+1,save)+self.integrate(mid,right,depth+1,save)

    def partial(self,x):
        if x<=0:return np.zeros(6,LD)
        if x>=1:return self.total.copy()
        index=min(len(self.right)-1,int(np.searchsorted(self.right,x,side='right')))
        return self.prefix[index]+self.integrate(self.left[index],LD(x))


class OriginalTailBackground:
    def __init__(self,manifest,calibrations,tolerance=LD('2e-18')):
        self.manifest_path=Path(manifest);self.calibration_path=Path(calibrations)
        if sha(self.manifest_path)!='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104':
            raise ValueError('This consumer is tied to the original M12 manifest')
        data=json.loads(self.manifest_path.read_text());self.parameters=data['parameters']
        frozen=json.loads(self.calibration_path.read_text())
        self.source=FrozenNumericalSource(self.parameters,frozen);self.profiles=[]
        self.cut,self.cuff=self.source.cut,self.source.cuff;self.tolerance=LD(tolerance)
        totals=np.zeros(6,LD)
        for n in range(160):
            for j in range(9):
                row=ProfilePrimitive(self.source,n,j,self.tolerance)
                self.profiles.append(row);totals+=row.total
        remaining_log=6*self.source.delta0/LD(2)**160+6*self.source.eta0*self.source.q**160/(1-self.source.q)
        self.deep_radius_excess=self.cuff*np.expm1(remaining_log/self.source.root12)
        self.alpha=(self.cut-self.cuff-self.deep_radius_excess-totals[0])/totals[1]
        if self.alpha<=0:raise ArithmeticError('Nonpositive original normalization')
        alpha_path=self.manifest_path.parent/'2026-11-09-db6f-tail-tight-alpha.json'
        alpha_record=json.loads(alpha_path.read_text())
        if sha(self.calibration_path)!=alpha_record['inputs']['calibrations']['sha256']:
            raise ValueError('Existing alpha proof uses different calibrations')
        self.alpha_proof_sha256=sha(alpha_path)
        low,high=map(LD,alpha_record['exactRadialAlpha'])
        if not low<=self.alpha<=high:
            raise ArithmeticError('Numerical alpha misses the previously proved exact source box')
        self.totals=totals;right=self.cut;drop=LD(0)
        self.outer_order=[]
        for n in range(160):
            for j in range(8,-1,-1):
                row=self.profiles[9*n+j];row.r_right=right;row.height_at_right=drop
                row.r_left=right-row.total[0]-self.alpha*row.total[1]
                row.radius_nodes=row.r_left+row.prefix[:,0]+self.alpha*row.prefix[:,1]
                row.source_nodes=np.r_[row.left,LD(1)]
                right=row.r_left;drop+=row.total[4]+self.alpha*row.total[5]
                self.outer_order.append(row)
        self.height_finite=drop;self.inner_anchor_residual=right-self.cuff-self.deep_radius_excess
        self.left_radii=np.asarray([row.r_left for row in self.outer_order],LD)
        self.query_cache={}

    def point(self,radius):
        r=LD(radius);key=str(r)
        if key in self.query_cache:return self.query_cache[key]
        if r<self.cuff or r>self.cut:raise ValueError('Outside the original tail')
        if r==self.cut:
            w=LD(self.parameters['wCut']);answer=(w,-7*w/self.cut,LD(0),LD(0),0,8,LD(1))
        elif r==self.cuff:
            # Exact endpoint jets. The displayed height is the finite part;
            # the original infinitesimal n>=160 height remains in the definition.
            answer=(LD(0),LD(0),self.height_finite,LD(0),160,-1,LD(0))
        else:
            index=min(len(self.outer_order)-1,int(np.searchsorted(-self.left_radii,-r,side='left')))
            row=self.outer_order[index]
            if r<row.r_left-LD('1e-17') or r>row.r_right+LD('1e-17'):
                raise ArithmeticError('Numerical source-profile localization failed')
            leaf=min(len(row.radius_nodes)-2,max(0,int(np.searchsorted(row.radius_nodes,r,side='right')-1)))
            low,high=row.source_nodes[leaf],row.source_nodes[leaf+1]
            rl,rh=row.radius_nodes[leaf],row.radius_nodes[leaf+1]
            x=(low+high)/2 if rh<=rl else low+(high-low)*np.clip((r-rl)/(rh-rl),0,1)
            residual=LD('inf');values=None
            for unused in range(40):
                values=row.partial(x);rr=row.r_left+values[0]+self.alpha*values[1]
                residual=rr-r
                A,B,w,wd=self.source.evaluate(row.n,row.j,x);rx=A+self.alpha*B
                if abs(residual)<LD('2e-19'):break
                if residual>0:high=x
                else:low=x
                proposal=x-residual/rx
                x=proposal if low<proposal<high else (low+high)/2
            if abs(residual)>LD('2e-16'):raise ArithmeticError('Numerical radial inverse did not settle')
            height=row.height_at_right+(row.total[4]-values[4])+self.alpha*(row.total[5]-values[5])
            answer=(LD(w),LD(wd/rx),LD(height),LD(residual),row.n,row.j,LD(x))
        self.query_cache[key]=answer;return answer

    def receipt(self):
        return {'manifest_sha256':sha(self.manifest_path),'calibration_sha256':sha(self.calibration_path),
                'alpha_proof_sha256':self.alpha_proof_sha256,
                'alpha_numerical':str(self.alpha),'inner_anchor_residual_numerical':str(self.inner_anchor_residual),
                'finite_height_numerical':str(self.height_finite),'deep_radius_excess_numerical':str(self.deep_radius_excess),
                'profiles':len(self.profiles),'quadrature_leaves':sum(len(r.leaves) for r in self.profiles),
                'quadrature_evaluations':sum(r.evaluations for r in self.profiles),
                'maximum_refinement_depth':max(r.max_depth for r in self.profiles),
                'estimated_quadrature_error_only':[str(x) for x in sum((r.error for r in self.profiles),np.zeros(6,LD))],
                'original_exact_background_definition_retained':True,'numerical_evaluator_not_interval_certificate':True,
                'infinite_protected_height_not_numerically_included':True}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--calibrations',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--tolerance',default='2e-18')
    ap.add_argument('--radii',type=float,nargs='*',default=[.6,.59,.5,.3,.2,.16,.153,.151,.1501])
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh background report required')
    start=time.monotonic();model=OriginalTailBackground(args.manifest,args.calibrations,LD(args.tolerance))
    rows=[]
    for r in args.radii:
        value=model.point(r);rows.append({'r':r,'w':str(value[0]),'wr':str(value[1]),'height_drop':str(value[2]),
                                         'inverse_residual':str(value[3]),'cell':value[4],'segment':value[5],'x':str(value[6])})
    report={'schema':'6a65-original-M12-background-numerical-consumer-v1','script_sha256':sha(__file__),
            **model.receipt(),'rows':rows,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))


if __name__=='__main__':main()
