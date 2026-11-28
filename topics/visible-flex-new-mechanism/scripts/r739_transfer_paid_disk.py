"""R739 read-only correction of paid R732 fields using the same two boundary-position jets."""
import argparse
import json
import os
from pathlib import Path
import platform
import time
import numpy as np
import scipy
from r688_actual_r664_window_collars import require_public, quadrature
from r732_compensated_pulses import gate
from r732_disk_fields import Frame, rotation, apply
from r732_disk_qualification import tail_weight, true_breaks, geometry, point_cloud, diameter, chords
from r732_disk_solver import Pack, plain, digest, array_id, FILES
from r732_physical_disk import EPS, R0

ORIGINAL_RUN='46164917792'
ORIGINAL_ARTIFACT=15271038061
ORIGINAL_COMMIT='706ed9ca3ded0131f1da879bf98a3e20adabfa57'
ORIGINAL_INPUT='30e7f24cabda9e0ebb08e9c1181c4c58a24823ee200e5fa8e0da68752c608045'
ARCHIVE_IDS={
    0.:'e4e603d511d434f51517430e3fd87f23873c474754b119cd7a94521a07fb8a0a',
    .02:'afe8f6af93f37cc5081f8ae124eb75d236a5b264333595c89e4a973e9bf758ca',
    .08:'7d86ca7e1ed0f635a9e7e7982688ac4ad213257e05c6d18b909323f974dddf87',
    .2:'dcc6c066070f3f558d75d2423a5c55d38fa66a32ce3f90949c33dd74a1e8b060',
    .4:'e443385e0e84d18eef5d72400c9dbd5667d2dbab302d12f0e5b48dc75c3e7d25',
    .65:'e8f2d9ebfc73b54b633d998ff20f40f7392ab66fba8588c20fbd1038f39c1325',
    .85:'73af18553006b69c3af6e782458436adffb336e4b7608699c23730b232a9b05a',
    1.:'6f3d8bd324d6599b72c5296e1e4ee19fe966da7143ae4045779d58ab0c875a04'}


def atomic_npz(path,**data):
    temp=path.with_suffix('.partial')
    with temp.open('wb') as f:np.savez_compressed(f,**data)
    os.replace(temp,path)


def json_out(path,d):
    tmp=path.with_suffix('.partial');tmp.write_text(plain(d)+'\n');os.replace(tmp,path)


class Input:
    def __init__(self,root):
        self.root=root;self.meta=json.loads((root/'input-identity.json').read_text())
        self.identifier=digest(plain(self.meta).encode())
        if self.identifier!=ORIGINAL_INPUT:raise ValueError('expected original published R732 input SHA')
        for name,value in (('python',platform.python_version()),('numpy',np.__version__),('scipy',scipy.__version__)):
            if self.meta[name]!=value:raise ValueError('restore original R732 version of '+name)
        here=Path(__file__).resolve().parent
        for f in FILES:
            if digest((here/f).read_bytes())!=self.meta['sha256'][f]:raise ValueError('original model source mismatch: '+f)
        terminal=json.loads((root/'terminal.json').read_text())
        if terminal['run'].split('-')[0]!=ORIGINAL_RUN or terminal['input_identity']!=self.identifier:
            raise ValueError('expected the original naturally finished R732 first allocation')
        self.records=json.loads((root/'continuation.json').read_text())['records']
        if [rec['phase'] for rec in self.records]!=list(ARCHIVE_IDS):
            raise ValueError('incomplete original eight physical records')
        self.build=self.receipt('source_build',[])
        if self.build.seed_identity!=json.loads((root/'source-identity.json').read_text()):
            raise ValueError('different source disk identity')
        self.level=self.meta['settings']['level']

    def receipt(self,kind,key):
        tag=[self.identifier,kind,key]
        path=self.root/'paid'/(kind+'-'+digest(plain(tag).encode())+'.npz')
        with np.load(path,allow_pickle=False) as z:
            header=json.loads(z['meta'].tobytes())
            if header['semantic']!=json.loads(plain(tag)):raise ValueError('original operation identity differs')
            return Pack.decode(header['tree'],z)

    def phase(self,phase):
        if phase not in self.build.rings:self.build.rings[phase]=self.receipt('phase_ring',[phase])
        if phase not in self.build.pulse_cache:
            self.build.pulse_cache[phase]=self.receipt('phase_pulses',[phase])

    def physical(self,record):
        qual=record['physical_qualification']
        path=self.root/'physical'/Path(qual['physical_archive']).name
        original_sha=digest(path.read_bytes())
        if original_sha!=qual['archive_sha256'] or original_sha!=ARCHIVE_IDS[record['phase']]:
            raise ValueError('original physical archive SHA mismatch')
        with np.load(path,allow_pickle=False) as z:data={k:z[k] for k in z.files}
        if array_id(data['q'])!=record['q'] or float(data['phase'])!=record['phase']:
            raise ValueError('physical q or phase not the original accepted two-grid state')
        return data,original_sha


def b_s_shifted(build,phase,q,degree,radii,ss,order):
    """Only the missing source-corrected derivative integral from the original radial primitive."""
    cuts=true_breaks(build,radii);nodes,weights=quadrature(order)
    # No J, fitted samples, full position, or full six-jet reconstruction here.
    pieces=np.empty((len(cuts)-1,len(ss),3))
    coef=np.asarray(q).reshape(-1,3)
    for i in range(0,len(cuts)-1,4):
        left=cuts[i:i+4];right=cuts[i+1:i+5];n=len(right);left=left[:n]
        half=(right-left)/2;r=(left[:,None]+half[:,None]*(1+nodes)).ravel()
        f=Frame(build,phase,r[:,None],ss[None,:],degree)
        ang=f.B@coef;d_s=f.Bs@coef;M=f.base;S=f.bs
        for axis in range(3):
            V,dV=rotation(ang[:,axis],axis);dotM=M@dV
            S=S@V+d_s[:,axis,None,None]*dotM;M=M@V
        brs=apply(S,f.j0[1])+apply(M,f.j0[4])-f.j0[4]
        values=brs.reshape(n,order,len(ss),3)
        pieces[i:i+n]=half[:,None,None]*np.einsum('k,ikbc->ibc',weights,values)
    integral=np.cumsum(pieces[::-1],axis=0)[-1]
    return build.boundary_jets(phase,ss)[1]-build.boundary_jets(0.,ss)[1]-integral


def missing_second(inp,phase,degree,q,r,ss,order,fd,work,deadline,code):
    if not np.any(q) and phase==0:return np.zeros((len(ss),3)),0,0
    result=np.empty((len(ss),3));paid=0;reused=0
    key=digest(plain([inp.identifier,phase,degree,array_id(q),array_id(r),array_id(ss),order,fd,code]).encode())[:24]
    for i in range(0,len(ss),16):
        path=work/(key+f'-{i:04d}.npz')
        if path.exists():
            with np.load(path,allow_pickle=False) as z:
                if str(z['identity'])!=key or int(z['index'])!=i:raise ValueError('wrong shifted derivative chunk')
                values=z['bss']
            reused+=1
        else:
            if time.monotonic()>=deadline:raise TimeoutError('next missing Bss chunk remains')
            labels=ss[i:i+16]
            side=np.r_[labels-fd,labels+fd]
            b_s=b_s_shifted(inp.build,phase,q,degree,r,side,order)
            low,high=np.split(b_s,2);values=(high-low)/(2*fd)
            atomic_npz(path,identity=key,index=i,bss=values,lower=b_s[:len(labels)],upper=b_s[len(labels):])
            paid+=1
        result[i:i+len(values)]=values
    return result,paid,reused


def weights(build,r):
    x,u,xr,ur,xrr,urr,ell=build.profile.read(r)
    y=(ell-.04)/.43
    # The active range is strictly inside the original straight sleeve. There ell=x-W exactly.
    return gate(y),gate(y,1)*xr/.43,gate(y,2)*(xr/.43)**2+gate(y,1)*xrr/.43


def peak(values,r,s):
    idx=np.unravel_index(np.argmax(values),values.shape)
    return dict(value=float(values[idx]),r=float(r[idx[0]]),s=float(s[idx[1]]))


def convert(inp,record,out,deadline,code):
    z,oldsha=inp.physical(record)
    r=z['r'];ss=z['s'];phase=float(z['phase']);degree=int(z['degree']);q=z['q']
    inp.phase(phase)
    name=f'phase-{phase:.12g}-{oldsha[:12]}';receipt=out/(name+'.json')
    if receipt.exists():
        info=json.loads(receipt.read_text())
        if info['original_archive_sha256']!=oldsha or info['code_sha256']!=code:raise ValueError('wrong R739 receipt')
        if digest((out/info['new_physical_file']).read_bytes())!=info['new_archive_sha256']:raise ValueError('missing R739 geometry')
        return info
    order=max(6,4+2*inp.level);fd=2.4e-7/(inp.build.ring.length*inp.level)
    work=out/'missing-angular';work.mkdir(exist_ok=True)
    bss,new,old=missing_second(inp,phase,degree,q,r,ss,order,fd,work,deadline,code)
    # Independently refine just the missing scalar-material derivative of the vector drift on 1/4 of the angles.
    check,new2,old2=missing_second(inp,phase,degree,q,r,ss[::4],order+4,fd/2,work,deadline,code)
    w_old=tail_weight(r);w_new=weights(inp.build,r);d,dr,drr=[a-b for a,b in zip(w_old,w_new)]
    B=z['centre_drift'];Bs=z['boundary_derivative_drift']
    def inc(f,v):return f[:,None,None]*v[None,:,:]
    delta=(inc(d,B),inc(dr,B),inc(d,Bs),inc(drr,B),inc(dr,Bs),inc(d,bss))
    j=tuple(a+b for a,b in zip(z['physical_jets'],delta,strict=True))
    j0=z['source_jets']
    try:
        n,g0,me,k=geometry(j,j0)
    except (ArithmeticError,np.linalg.LinAlgError) as exc:
        newfile=name+'.npz'
        area=np.linalg.norm(np.cross(j[1],j[2]),axis=-1)
        atomic_npz(out/newfile,r=r,s=ss,degree=degree,q=q,phase=phase,Bss=bss,Bss_ref=check,
                   physical_jets=np.asarray(j),physical_center_jets=z['physical_center_jets'],
                   source_g=z['source_g'],source_center_g=z['source_center_g'],tangent_area=area,
                   centre_drift=B,boundary_derivative_drift=Bs,original_archive_sha256=oldsha)
        idx=np.unravel_index(np.argmin(area),area.shape)
        info=dict(phase=phase,degree=degree,q=array_id(q),original_archive_sha256=oldsha,code_sha256=code,
                  new_physical_file=newfile,new_archive_sha256=digest((out/newfile).read_bytes()),
                  numerical_geometry_failure=repr(exc),minimum_tangent_area=float(area[idx]),
                  minimum_area_label=[float(r[idx[0]]),float(ss[idx[1]])],
                  unchanged_original_sampled_curl=record['physical_qualification']['disk_cartesian_curl_max'],
                  new_missing_blocks=new+new2,reused_missing_blocks=old+old2,new_jacobian_columns=0,
                  continuous_reach_and_common_metric_qualified=False)
        json_out(receipt,info)
        return info
    if not np.array_equal(g0,z['source_g']):raise ValueError('transferred source Gram does not match the archived rows')
    # The correction is identically zero around the marked true centre.
    cj=z['physical_center_jets']
    point=np.r_[inp.build.profile.endx,inp.build.ring.origin][None]
    centre_src=(point,np.array([[0.,EPS/R0,0.]]),np.array([[0.,0.,EPS/R0]]),
                np.zeros_like(point),np.zeros_like(point),np.zeros_like(point))
    cn,cg,ce,ck=geometry(cj,centre_src)
    if not np.array_equal(cg,z['source_center_g']):raise ValueError('source Cartesian centre Gram changed')
    one=dict(P=j[0],N=n,centre=cj[0],centre_n=cn)
    group,norm=point_cloud(inp.build,phase,one,ss)
    source=dict(P=j0[0],N=n,centre=point,centre_n=cn)
    sourcepts,_=point_cloud(inp.build,0.,source,ss)
    old_bound=record['physical_qualification']
    # Geometry-only second-scale difference from the one new missing quantity. Its effect is exactly delta(w)*delta(Bss).
    late=np.linalg.norm(bss[::4]-check,axis=-1)
    closed=chords(group,norm,1/10.4)
    newfile=name+'.npz'
    atomic_npz(out/newfile,r=r,s=ss,degree=degree,q=q,phase=phase,Bss=bss,Bss_ref=check,
               physical_jets=np.asarray(j),physical_center_jets=cj,source_g=z['source_g'],source_center_g=cg,
               centre_metric=ce,centre_curvature=ck,
               metric=me,principal_curvatures=k,centre_drift=B,boundary_derivative_drift=Bs,
               original_q_sha256=array_id(q)['sha256'],original_archive_sha256=oldsha)
    curv=np.max(abs(k),axis=-1)
    info=dict(phase=phase,degree=degree,q=array_id(q),original_archive_sha256=oldsha,code_sha256=code,
              new_physical_file=newfile,new_archive_sha256=digest((out/newfile).read_bytes()),
              unchanged_original_sampled_curl=old_bound['disk_cartesian_curl_max'],
              original_metric_max=old_bound['disk_metric_max'],
              original_metric_nominal_grid_peak=peak(z['metric'],r,ss),converted_metric_nominal_grid_peak=peak(me,r,ss),
              unchanged_centre_metric=float(np.max(ce)),unchanged_centre_curvature=float(np.max(abs(ck))),
              original_curvature_max=old_bound['disk_curvature_max'],
              original_curvature_nominal_grid_peak=peak(np.max(abs(z['principal_curvatures']),axis=-1),r,ss),
              converted_curvature_nominal_grid_peak=peak(curv,r,ss),
              max_missing_Bss_refinement_difference=float(np.max(late)),
              max_transferred_Pss_difference_from_missing_term=float(np.max(abs(d))*np.max(late)),
              new_missing_blocks=new+new2,reused_missing_blocks=old+old2,new_jacobian_columns=0,
              new_original_optimizations=0,new_all_sampled_normal_pairs=closed,
              prescribed_open_band_jet_errors=old_bound['prescribed_open_band_jet_errors'],
              given_far_seat_z=old_bound['given_far_seat_z'],
              new_source_and_phase_union_diameter_sample=float(diameter(np.r_[group,sourcepts])),
              new_x_range=[float(group[:,0].min()),float(group[:,0].max())],
              continuous_reach_and_common_metric_qualified=False)
    json_out(receipt,info);return info


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',required=True);parser.add_argument('--out',default='r739-transfer')
    parser.add_argument('--seconds',type=float,default=1200.)
    args=parser.parse_args();require_public()
    root=Path(args.source);out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    if out.resolve()==root.resolve() or root.resolve() in out.resolve().parents:raise ValueError('new output must be outside the original archive')
    inp=Input(root);code=digest(Path(__file__).read_bytes());started=time.monotonic();rows=[]
    status='complete_eight_original_fields'
    try:
        for record in inp.records:
            rows.append(convert(inp,record,out,started+args.seconds,code))
    except TimeoutError as exc:status=str(exc)
    result=dict(status=status,source_run=ORIGINAL_RUN,artifact=ORIGINAL_ARTIFACT,commit=ORIGINAL_COMMIT,
                original_input=inp.identifier,code_sha256=code,elapsed=time.monotonic()-started,
                finished=len(rows),phases=rows)
    json_out(out/'summary.json',result)
    print('R739_TRANSFER',plain({**result,'phases':[dict(phase=x['phase'],metric=x.get('converted_metric_nominal_grid_peak'),
                                                   geometry_failure=x.get('numerical_geometry_failure'),
                                                   curl=x['unchanged_original_sampled_curl']) for x in rows]}),flush=True)


if __name__=='__main__':main()

