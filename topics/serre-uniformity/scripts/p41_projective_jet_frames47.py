#!/usr/bin/env python3
"""Batched integral projective jets in a unit frame, including fc-zero points.

indices_0based always indexes the original input W0 rows.  A chart uses one
frame v and one coordinate c, normalized by Wv=1 and Wc=W0c+z.  Nonprojective
zero raw rows must be replaced by the R208 coarse elliptic rows by the caller.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

Q=47**4


def matrix_digest(A):
    import numpy as np
    h=hashlib.sha256()
    for x in A:h.update(np.asarray(x,dtype='<i8').tobytes())
    return h.hexdigest()


def install_exact_float_mm(r):
    """Each nonnegative real dot has exact integer sum below 2^53."""
    import numpy as np
    if getattr(r.mm,'exact_nonnegative_float64',False):return r.mm
    original=r.mm
    def mm(A,B,q=Q):
        k=A[0].shape[1]
        assert k==B[0].shape[0] and k<=820 and 1<=q<=Q
        assert all(np.all((x>=0)&(x<q)) for x in A+B)
        if k*(q-1)**2>=2**53:return original(A,B,q)
        ar,ai=(np.asarray(x,dtype=np.float64) for x in A)
        br,bi=(np.asarray(x,dtype=np.float64) for x in B)
        # Convert and reduce separately: never add two float dot products.
        ac=(ar@br).astype(np.int64)%q
        bd=(ai@bi).astype(np.int64)%q
        ad=(ar@bi).astype(np.int64)%q
        bc=(ai@br).astype(np.int64)%q
        return (ac-bd)%q,(ad+bc)%q
    mm.exact_nonnegative_float64=True
    mm.original_integer_mm=original
    r.mm=mm
    # Maximal nonnegative inputs exercise the actual largest bound used here.
    for q in (47**3,Q):
        x=np.arange(3*325,dtype=np.int64).reshape(3,325)
        y=np.arange(325*4,dtype=np.int64).reshape(325,4)
        A=((q-1-x)%q,(q-2-3*x)%q);B=((q-1-y)%q,(q-3-7*y)%q)
        assert r.equal(mm(A,B,q),original(A,B,q))
    return mm


class ProjectiveJetFrames:
    def __init__(self,a,exact_blas=True):
        self.a,self.r,self.np=a,a.r,a.np
        r,np=self.r,self.np
        if exact_blas:install_exact_float_mm(r)
        self.Hsource=r.mm(a.M['V3'],a.H)
        if exact_blas:
            assert r.equal(self.Hsource,r.mm.original_integer_mm(a.M['V3'],a.H))
            assert r.equal(r.mm(a.M['W'],a.fc),a.f)
        eye=r.eye(73)
        plus=r.add(eye,a.M['A1'])
        minus=r.sub(eye,a.M['A1'])
        imin=(-minus[1]%Q,minus[0].copy())
        self.candidates=r.hcat(plus,imin)
        assert r.equal(r.mm(a.M['A1'],r.conjugate(self.candidates)),self.candidates)
        self.frames={matrix_digest(a.fc):{'frame':a.fc,'H':a.H,
                     'source820_verified':True,'kind':'fc'}}

    def frame_derivation(self,v):
        a,r=self.a,self.r
        key=matrix_digest(v)
        if key in self.frames:return self.frames[key]
        fv=r.mm(a.M['W'],v);Hv=r.mm(self.Hsource,v)
        numerator=r.sub(r.mul(fv,self.Hsource),r.mul(a.M['W'],Hv))
        values=r.mul(numerator,r.inverse_values(a.f))
        H=r.rows(values,a.M['P3'])
        assert r.equal(r.mm(a.M['V3'],H),values)
        assert r.equal(r.mul(a.f,values),numerator)
        assert r.iszero(r.mm(H,v))
        item={'frame':v,'H':H,'source820_verified':True,'kind':'unit_replacement',
              'source_identity_sha256':matrix_digest(values)}
        self.frames[key]=item
        return item

    @staticmethod
    def projective_indices(W0):
        import numpy as np
        return np.flatnonzero(np.any(((W0[0]%47)**2+(W0[1]%47)**2)%47!=0,axis=1)).tolist()

    def _groups(self,W0,indices):
        """Frame/coordinate choices only; no high-order jets allocated here."""
        a,r,np=self.a,self.r,self.np
        remaining=set(indices)
        assert remaining.issubset(self.projective_indices(W0)), 'Use R208 coarse points for raw elliptic zero rows'
        first=True
        while remaining:
            I=sorted(remaining)
            if first:
                v=a.fc;units=r.units(r.mm(r.rows(W0,I),v))[:,0]
                first=False
                if not np.any(units):continue
            else:
                values=r.mm(r.rows(W0,I),self.candidates)
                unit=r.units(values);column=int(np.argmax(np.sum(unit,axis=0)))
                assert np.any(unit[:,column]), 'No unit section in the rational spanning family'
                v=r.cols(self.candidates,[column]);units=unit[:,column]
            J=[i for i,ok in zip(I,units) if ok]
            item=self.frame_derivation(v)
            raw=r.rows(W0,J);frame0=r.mm(raw,v)
            normalized=r.mul(raw,r.inverse_values(frame0))
            V2,V3=a.evaluate(normalized)
            H0=r.mm(V3,item['H'])
            coordvalues=r.mm(H0,self.candidates)
            possible=r.units(coordvalues)
            left=set(range(len(J)));first_coordinate=True
            while left:
                K=sorted(left)
                if first_coordinate:
                    column=0;first_coordinate=False
                    hit=[k for k in K if possible[k,column]]
                    if not hit:continue
                else:
                    column=int(np.argmax(np.sum(possible[K],axis=0)))
                    hit=[k for k in K if possible[k,column]]
                    assert hit, 'The global derivation has no unit projective tangent at a requested point'
                c=r.cols(self.candidates,[column])
                yield {'indices_0based':[J[k] for k in hit],
                       'frame':v,'coordinate':c,'H_matrix':item['H'],
                       'frame_kind':item['kind'],'frame_source820_verified':True,
                       'coordinate_candidate':column}
                left.difference_update(hit)
            remaining.difference_update(J)

    def local_jets(self,W0,frame=None,coordinate=None,H_matrix=None,order=27):
        """W0 is already the selected batch; order is the highest degree."""
        a,r,np=self.a,self.r,self.np
        assert 0<=order<47, 'Orders >=47 need additional precision or integral coefficient recovery'
        v=frame if frame is not None else a.fc
        c=coordinate if coordinate is not None else a.rational_coordinate(0)
        H=H_matrix if H_matrix is not None else self.frame_derivation(v)['H']
        nrow=W0[0].shape[0]
        f0=r.mm(W0,v);assert np.all(r.units(f0))
        W=[r.mul(W0,r.inverse_values(f0))]
        V2=[];V3=[];F=[];Hvals=[];Hc=[];inverse_Hc=[]
        Wa=[];Wb=[];Z3=[];V2b=[]
        for n in range(order+1):
            # Only coefficient n is generated; lower section jets are retained.
            F.append(r.mm(W[n],a.fc))
            Wa.append(r.cols(W[n],a.a2));Wb.append(r.cols(W[n],a.b2))
            raw2=r.zeros(nrow,199)
            for k in range(n+1):raw2=r.add(raw2,r.mul(Wa[k],Wb[n-k]))
            V2.append(r.mm(raw2,a.C2));V2b.append(r.cols(V2[n],a.b3))
            Z3.append(r.sub(r.cols(W[n],a.a3),r.mul(F[n],a.lam)))
            raw3=r.zeros(nrow,126);first=r.zeros(nrow,199)
            for k in range(n+1):
                raw3=r.add(raw3,r.mul(V2b[k],Z3[n-k]))
                first=r.add(first,r.mul(F[k],V2[n-k]))
            extra=r.mm(raw3,a.E3)
            V3.append(r.hcat(r.sub(r.mul(first,a.ifP2),r.mm(extra,a.C)),extra))
            Hvals.append(r.mm(V3[n],H));Hc.append(r.mm(Hvals[n],c))
            if n==0:
                assert np.all(r.units(Hc[0]))
                inverse_Hc.append(r.inverse_values(Hc[0]))
            else:
                value=r.zeros(nrow,1)
                for k in range(1,n+1):value=r.add(value,r.mul(Hc[k],inverse_Hc[n-k]))
                inverse_Hc.append(r.neg(r.mul(value,inverse_Hc[0])))
            if n<order:
                value=r.zeros(nrow,73)
                for k in range(n+1):value=r.add(value,r.mul(Hvals[k],inverse_Hc[n-k]))
                value=a.scale(value,pow(n+1,-1,Q))
                assert r.iszero(r.mm(value,v))
                assert r.equal(r.mm(value,c),r.column([[int(n==0),0]]*nrow))
                W.append(value)
        assert len(W)==len(V2)==len(V3)==order+1
        assert r.equal(r.mm(W[0],v),r.column([[1,0]]*nrow))
        return {'W':W,'V2':V2,'V3':V3,'H':Hvals,'Hc':Hc,'inverse_Hc':inverse_Hc,
                'frame':v,'coordinate':c,'H_matrix':H,'frame_value_at_input':f0,
                'coordinate_base_value':r.mm(W[0],c),'order':order}

    def iter_charts(self,W0,indices=None,order=27,max_points=64,label=''):
        """Yield at most max_points rows; indices refer to original W0 rows."""
        r=self.r
        indices=list(range(W0[0].shape[0])) if indices is None else list(indices)
        assert len(set(indices))==len(indices) and max_points>=1
        covered=set()
        for group in self._groups(W0,indices):
            members=group['indices_0based']
            for start in range(0,len(members),max_points):
                I=members[start:start+max_points]
                assert not covered.intersection(I)
                batch=self.local_jets(r.rows(W0,I),group['frame'],group['coordinate'],
                                      group['H_matrix'],order)
                batch.update({k:v for k,v in group.items() if k not in batch})
                batch['indices_0based']=I;batch['label']=label
                covered.update(I)
                yield batch
        assert covered==set(indices)

    def build_charts(self,*args,**kwargs):
        """Convenience for small input only; use iter_charts for whole fibres."""
        return list(self.iter_charts(*args,**kwargs))

    def physical_to_chart(self,raw_jets,chart,order=4,already_selected=False):
        """Return z(t) coefficients 0..order.  No division by physical t."""
        from p41_elliptic_coarse_atlas47 import Series
        a,r=self.a,self.r
        assert len(raw_jets)>=order+1
        I=chart['indices_0based']
        W=raw_jets[:order+1] if already_selected else [r.rows(w,I) for w in raw_jets[:order+1]]
        vv=[r.mm(w,chart['frame']) for w in W]
        cc=[r.mm(w,chart['coordinate']) for w in W]
        s=Series(a,order+1)
        normalized=s.mul(cc,s.inverse(vv))
        normalized[0]=r.sub(normalized[0],chart['coordinate_base_value'])
        assert r.iszero(normalized[0])
        assert self.np.all(r.units(normalized[1]))
        return normalized

    def coarse_to_chart(self,coarse_record,chart):
        raw=[self.r.from_json(w) for w in coarse_record['coarse_values']]
        assert len(raw)>=4
        return self.physical_to_chart(raw,chart,order=3)


def ordinary_physical_jets(at,j,order=4,coarse_path=None):
    """R216 order means highest degree: order=4 really returns five terms."""
    from p41_scalar_primitive_atlas47 import ScalarPrimitiveAtlas
    coarse_path=coarse_path or at.a.folder/'data/p41_elliptic_coarse_atlas47_verified.json.gz'
    obj=ScalarPrimitiveAtlas(at,coarse_path)
    jets,indices,patches,beta=obj.ordinary_jets(j,order=order)
    assert len(jets)==order+1
    assert all(w[0].shape==(820,73) for w in jets)
    return {'W':jets,'ordinary_indices_0based':indices,'clearing_patches':patches,
            'parameter':'A-A_reference' if j==0 else 'B-B_reference','order':order}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--order',type=int,default=27)
    ap.add_argument('--max-points',type=int,default=64)
    ap.add_argument('--reference',type=int,default=9)
    ap.add_argument('--first-batch-only',action='store_true')
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    from p41_elliptic_coarse_atlas47 import setup
    at=setup(args.script_dir.resolve());a,r=at.a,at.r
    helper=ProjectiveJetFrames(a);W0=at.refs[args.reference]['W']
    physical=ordinary_physical_jets(at,args.reference,order=4)
    records=[];start=time.monotonic()
    for chart in helper.iter_charts(W0,physical['ordinary_indices_0based'],args.order,args.max_points,str(args.reference)):
        z=helper.physical_to_chart(physical['W'],chart,4)
        # Compose the chart jets independently back to the physical section values.
        from p41_elliptic_coarse_atlas47 import Series
        I=chart['indices_0based'];raw=[r.rows(w,I) for w in physical['W']]
        vv=[r.mm(w,chart['frame']) for w in raw]
        normalized=Series(a,5).mul(raw,Series(a,5).inverse(vv))
        composed=Series(a,5).compose(chart['W'][:5],z,5)
        assert all(r.equal(x,y) for x,y in zip(normalized,composed))
        if chart['frame_kind']=='fc':
            # The original independent implementation is used only to degree4.
            V2,V3=a.evaluate(chart['W'][0])
            assert r.equal(V2,chart['V2'][0]) and r.equal(V3,chart['V3'][0])
        rec={'indices_0based':I,'order':args.order,'frame_kind':chart['frame_kind'],
             'frame_sha256':matrix_digest(chart['frame']),'coordinate_sha256':matrix_digest(chart['coordinate']),
             'W_sha256':[matrix_digest(w) for w in chart['W']],
             'V2_sha256':[matrix_digest(w) for w in chart['V2']],
             'V3_sha256':[matrix_digest(w) for w in chart['V3']],
             'physical_to_chart_coefficients_0to4':[r.to_json(w) for w in z],
             'physical_composition_all73_through_degree4':True,'source820_frame_identity':True}
        records.append(rec)
        out={'reference':args.reference,'order':args.order,'records':records,
             'complete':sum(len(x['indices_0based']) for x in records)==len(physical['ordinary_indices_0based']),
             'physical_jet_length':len(physical['W']),
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'input_sha256':a.inputs}
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_bytes(gzip.compress(json.dumps(out,sort_keys=True,separators=(',',':')).encode(),mtime=0))
        print('chart',args.reference,len(records),'rows',len(I),'frame',chart['frame_kind'],'seconds',round(time.monotonic()-start,3),flush=True)
        if args.first_batch_only:break


if __name__=='__main__':main()
