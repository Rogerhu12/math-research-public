"""Consume actual R745 receipts and prove (or retain the unresolved enclosure of) its two physical valley roots."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import struct
import time
import zipfile
from fractions import Fraction as F
from flint import arb, ctx
from r689_continuous_native_field_balls_20261128 import Jet, pack_ball, unball, public_only
from r759_projective_valley_taylor import a, cover, union, knots, slope, transfer, send_cone, align, MID, CUT, H

FP='1b40bcf507d16497579ef47032968914ce787f6113899a185e60c050b42167cf'
OLD_FINAL='e9ec284cc041db1649576ad6ef8e0fe97247ac2717bc8b1a857658b54bb5b21b'
OLD_BLOCK='d07dc6fc1972061c4cabe75a2da679b7b26d6f86d8bf65f8d39e02a2352292b9'
OLD_PORT='cc1826cc43e71c7575ba6a042dcfd06d0df7f1b40e2e17f7696d96f79e9bda20'

class Pause(Exception):pass
class Resolution(Exception):pass

def digest(raw):return hashlib.sha256(raw).hexdigest()
def bytes_of(v):return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def state_pack(v):return [v[0],*[pack_ball(q) for q in v[1:]]]
def state_unpack(v):return [v[0],*[unball(q) for q in v[1:]]]
def unit_name(*parts):return '|'.join(str(q) for q in parts)

class Book:
    def __init__(self,spec,seconds,reserve):
        self.start=time.monotonic();self.seconds=seconds;self.reserve=reserve
        self.path=Path(os.environ['RUNNER_TEMP'])/'r759-paid';self.path.mkdir(exist_ok=True)
        self.fid=digest(bytes_of(spec));self.cache={};self.new=0;self.pending=None;self.chain=0;self.seen={}
        jf=self.path/'units.jsonl'
        if jf.exists():
            with jf.open() as stream:
                for line in stream:
                    r=json.loads(line)
                    if r['identity']!=self.fid or r['key'] in self.cache:raise ValueError('Wrong or duplicated R759 operator receipt.')
                    self.cache[r['key']]=r['value'];self.chain+=r['time']
        self.out=jf.open('a',buffering=1)
    def once(self,key,f):
        if key in self.cache:return self.cache[key]
        if time.monotonic()-self.start+self.reserve>=self.seconds:self.pending=key;raise Pause()
        st=time.monotonic();prior=self.chain;v=f();dt=max(0.,time.monotonic()-st-(self.chain-prior))
        self.out.write(bytes_of(dict(identity=self.fid,key=key,time=dt,value=v)).decode()+'\n');self.cache[key]=v
        self.new+=1;self.chain+=dt;return v

def inputs(root):
    final=(root/'r745-final.json').read_bytes(); donor=(root/'r745-depth6.json').read_bytes(); ports=(root/'r738-complete.npz').read_bytes()
    if [len(final),digest(final),len(donor),digest(donor),len(ports),digest(ports)]!=[30183,OLD_FINAL,93744,OLD_BLOCK,13093,OLD_PORT]:raise ValueError('Wrong original byte objects.')
    original=json.loads(final);bundle=json.loads(donor)
    if original['kind']!='terminal' or original['fingerprint']!=FP or original['actual']['true_two_valley_box'] is not None:raise ValueError('Not the naturally completed R745 object.')
    if bundle['origin']['fingerprint']!=FP or [b['label'] for b in bundle['original_blocks']]!=['96ac3baadc9e45efb1be513b','b1ffad9ab01196c8b33e7c8c']:raise ValueError('Unexpected ordered original depth-6 side blocks.')
    with zipfile.ZipFile(io.BytesIO(ports)) as z:raw=z.read('meta.npy')
    if raw[:8]!=b'\x93NUMPY\x01\x00':raise ValueError('Wrong original scalar metadata.')
    offset=10+struct.unpack('<H',raw[8:10])[0];p=json.loads(raw[offset:])
    return original,bundle,p['actual_new_ports']

def initial(source,ports,s,j,origin):
    ks=knots(s); summit=MID[0 if s==-1 else 2];ia=ks.index(summit)
    Jet.order=0
    if origin=='actual_cut':
        r=CUT[s]; w=slope(Jet.cast(r),r,a(0))[0].c[0];lo,hi=ports[str((s,j))]['f_0_1_2'][1]
        z=a(r)*cover(F(lo),F(hi))-j*j
        return 0,[0,w,z,a(0)],'original_four_physical_tail_ports'
    # First two completed pieces end exactly at the foot of the genuine first ramp.
    end=ia if origin=='first_summit' else 2
    cap=source['original_blocks'][int(s==1)]; rec=cap['piece_endpoints'][end-1]
    if rec['piece']!=end-1 or rec['key']!=f"enc_{cap['label']}_p{end-1}_z63":raise ValueError('Different genuine piece endpoint.')
    datum=rec['cached_value']['data']['states'][str(j)]
    c=[unball(t) for t in datum['c']];Q=[unball(t) for t in datum['Q']];h=[unball(t) for t in datum['h']]
    r=ks[end]; w=slope(Jet.cast(r),r,a(0))[0].c[0] if end!=ia else a(H)/(1-a(H)**2).sqrt()
    corners=[(c[0]+Q[0]*x+Q[1]*y,(c[1]+Q[2]*x+Q[3]*y)/w) for x in (h[0].lower(),h[0].upper()) for y in (h[1].lower(),h[1].upper())]
    choice=[]
    for axis in (0,1):
        den=union([row[axis] for row in corners])
        if not den.contains(0):choice.append((abs(den).lower(),axis))
    if not choice:raise Resolution('Empty projective chart on original parallelogram.')
    axis=max(choice,key=lambda q:q[0])[1]
    return end,[axis,w,union([row[1-axis]/row[axis] for row in corners]),a(0)],rec['key']

def side(book,source,ports,s,j,vr,origin,opt):
    def original_cone():
        try:
            begin,state,key=initial(source,ports,s,j,origin)
            return dict(begin=begin,state=state_pack(state),original_unit=key)
        except Resolution as exc:return dict(unresolved=str(exc))
    entry=book.once(unit_name('original_projective_cone',s,j,origin),original_cone)
    if 'unresolved' in entry:raise Resolution(entry['unresolved'])
    begin,st,old=entry['begin'],state_unpack(entry['state']),entry['original_unit']
    ks=knots(s);v=cover(*vr)
    tag=','.join(map(str,vr));prefix=unit_name(origin,s,j,tag)
    def walk(l,r,vstate,depth):
        fixed=s*(l-MID[0 if s==-1 else 2])>=0 and s*(r-MID[0 if s==-1 else 2])>=0
        # Physical coefficient and its zero parameter derivative here are independent of the full trial box.
        operator=unit_name('Taylor',s,j,l,r,'fixed' if fixed else tag)
        def matrix():
            z=transfer(l,r,j,a(0) if fixed else v,opt['order'],opt['absolute_local_remainder'])
            if z is None:return None
            sc,M,N,e,det=z
            return [pack_ball(sc),[pack_ball(x) for x in M],[pack_ball(x) for x in N],pack_ball(e),pack_ball(det)]
        d=book.once(operator,matrix)
        # Nonlinear cone evaluation can require shorter pieces even when operator tolerance passed.
        state_id=unit_name('cone',s,j,l,r,origin,'fixed' if fixed else tag,digest(bytes_of(state_pack(vstate)))[:24])
        if d is not None:
            def prop():
                try:
                    z=(unball(d[0]),tuple(unball(x) for x in d[1]),tuple(unball(x) for x in d[2]),unball(d[3]),unball(d[4]))
                    return state_pack(send_cone(vstate,z))
                except ArithmeticError:return None
            val=book.once(state_id,prop)
            if val is not None:return state_unpack(val)
        if depth>=opt['maximum_subdivisions']:raise Resolution('Finite Taylor/projective subdivision limit for '+operator)
        mid=(l+r)/2;vstate=walk(l,mid,vstate,depth+1);return walk(mid,r,vstate,depth+1)
    for l,r in zip(ks[begin:],ks[begin+1:]):
        name=unit_name('whole-piece',prefix,l,r);oldstate=st
        st=state_unpack(book.once(name,lambda:state_pack(walk(l,r,oldstate,0))))
    return st,old

def read_rows(book,source,ports,vals,origin,opt,axes=None):
    scales=a(H)/(1-a(H)**2).sqrt();out=[];ds=[];used=[];picked=[]
    for j in (2,3):
        l,ql=side(book,source,ports,-1,j,vals[0],origin,opt);r,qr=side(book,source,ports,1,j,vals[1],origin,opt)
        options=(axes[j-2],) if axes is not None else (l[0],1-l[0]);one=None
        for axis in options:
            try:
                u,du=align(l,axis,scales);v,dv=align(r,axis,scales);one=(u-v,[du,-dv]);break
            except ArithmeticError:pass
        if one is None:raise Resolution('No common chart for both genuine physical rays.')
        out.append(one[0]);ds.append(one[1]);used.append([ql,qr]);picked.append(axis)
    return out,ds,picked,used

def check(book,source,ports,center,radius,origin,opt):
    zero=[(v,v) for v in center];box=[(v-radius,v+radius) for v in center]
    v0,j0,axes,old=read_rows(book,source,ports,zero,origin,opt)
    jmid=[[x.mid() for x in row] for row in j0];p,q=jmid[0];r,s=jmid[1];det=p*s-r*q
    if det.contains(0):raise Resolution('Mid-J is not invertible.')
    # This rational preconditioner is a single fixed point matrix (each division mid is dyadic).
    B=[[(s/det).mid(),(-q/det).mid()],[(-r/det).mid(),(p/det).mid()]]
    if (B[0][0]*B[1][1]-B[0][1]*B[1][0]).contains(0):raise Resolution('Chosen preconditioner is singular.')
    center_cost=[sum((t*x for t,x in zip(row,v0)),a(0)) for row in B]
    if any(not abs(t).upper()<a(radius) for t in center_cost):
        return dict(strict_interior=False,source=origin,radius=str(radius),original_ray_units=old,common_projective_axes=axes,
            reason="Computed center-enclosure budget already exceeds this trial radius.",center_preconditioned_residual=[pack_ball(x) for x in center_cost])
    _,j,_,_=read_rows(book,source,ports,box,origin,opt,axes)
    Y=[];contraction=[]
    for i in range(2):
        g=sum((t*x for t,x in zip(B[i],v0)),a(0)); row=[int(i==k)-sum((B[i][m]*j[m][k] for m in range(2)),a(0)) for k in range(2)]
        Y.append(-g+sum((t*cover(-radius,radius) for t in row),a(0)));contraction.append(sum((abs(t) for t in row),a(0)).upper())
    success=all(abs(y).upper()<a(radius) for y in Y)
    return dict(strict_interior=success,unique_for_each_fixed_true_cut_pair=success and all(k<1 for k in contraction),
                physical_valley_box=[[str(x),str(y)] for x,y in box],actual_center=[str(v) for v in center],source=origin,
                original_ray_units=old,common_projective_axes=axes,cartesian_slopes_at_center=[pack_ball(t) for t in v0],
                full_derivative_wrt_physical_valleys=[[pack_ball(x) for x in row] for row in j],
                fixed_preconditioner=[[pack_ball(x) for x in row] for row in B],relative_inclusion=[pack_ball(x) for x in Y],
                infinity_contraction_bounds=[pack_ball(x) for x in contraction])

def main():
    public_only();cli=argparse.ArgumentParser();cli.add_argument('--config',required=True);cli.add_argument('--max-seconds',required=True,type=float);args=cli.parse_args()
    opt=json.loads(Path(args.config).read_bytes());read_at=time.monotonic();source=Path(os.environ['RUNNER_TEMP'])/'r759-sources'
    old,blocks,ports=inputs(source);read_seconds=time.monotonic()-read_at
    req=json.loads(Path(os.environ['R759_REQUEST']).read_bytes());ctx.prec=opt['precision_bits'];Jet.scalar=arb;Jet.order=0
    spec=dict(schema='R759-projective-valleys-v1',source_hashes={k:v for k,v in req['source_sha256'].items() if k.endswith('.py')},
              geometry=opt,old_fingerprint=FP,blocks=OLD_BLOCK,cut=OLD_PORT,terminal=OLD_FINAL)
    book=Book(spec,args.max_seconds,opt['reserve_seconds']);allq=[];kind='terminal';result=None
    center=[F.from_float(x) for x in old['actual']['best_actual']['valley']]
    try:
        for trial in opt['origin_and_radii']:
            origin,rs=trial
            for n in rs:
                def run():
                    try:return check(book,blocks,ports,center,F(n),origin,opt)
                    except Resolution as ex:return dict(strict_interior=False,reason=str(ex),source=origin,radius=n)
                item=book.once(unit_name('krawczyk',origin,n),run);allq.append(item)
                if item['strict_interior']:result=item;break
            if result is not None:break
    except Pause:kind='paid_partial'
    finally:
        book.out.close();summary=dict(kind=kind,original_run=46174255201,original_job=141069279288,
          original_source=old['source_history'],old_counts=old['counts'],old_elapsed=old['current_elapsed'],old_ledger_seconds=old['cumulative_seconds'],
          inherited_first_summit_receipts=blocks['origin'],fingerprint=book.fid,original_bytes_read_seconds=read_seconds,
          newly_completed_units=book.new,retained_units=len(book.cache),retained_exclusive_unit_seconds=book.chain,
          current_allocation_wall_seconds=time.monotonic()-book.start,pending=book.pending,completed_trials=allq,
          certified_projective_double_kernel=result,continuous_beta=None,finite_angle_solution=None,README_completion_claim=False)
        raw=bytes_of(summary);(book.path/'final.json').write_bytes(raw);print('R759_FINAL '+raw.decode(),flush=True)

if __name__=='__main__':main()
