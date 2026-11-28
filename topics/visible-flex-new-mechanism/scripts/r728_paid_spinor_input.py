"""Immutable receipt and shape conversion. No old nonlinear phase or Jacobian is run."""
import hashlib
import json
import os
from pathlib import Path
from types import SimpleNamespace
import argparse
import io
import struct
import time
from urllib import request,error,parse
from zipfile import ZipFile



def checked_receipt(opt):
    # The bound administrative workflow stage authenticates and unpacks the historical receipt.
    # The sponsor wrapper clears all GitHub credentials before scientific execution.
    final=(Path(os.environ['RUNNER_TEMP'])/'r728-r703-natural-final.json').read_bytes()
    if len(final)!=39163:raise ValueError('Unexpected natural final length.')
    from r726_closed_spinor_fourier import r703_paid
    prior=r703_paid(final,46151140087,140997832329,'1b2ba533d51b4f4b416d30dcee1aaa516b2c64be','success')
    packed=struct.pack('<157d',*prior['all_parameters'])
    if hashlib.sha256(packed).hexdigest()!='9547c2fb5f33f75f13f9725f1bfa8acdc1a3cd77078679f9438d3e5a8b7ab8f8':
        raise ValueError('The paid R703 parameter identity differs.')
    return prior


def delta_six(new,old,r,angles,ids):
    import numpy as np
    out=[]
    for n,o in zip(new,old):
        w=np.linalg.norm((n-o)[ids],axis=-1)
        i,j=np.unravel_index(w.argmax(),w.shape)
        out.append(dict(maximum=float(w[i,j]),at=[float(r[ids][i]),float(angles[j])]))
    return out


def transfer(opt,layout,prior,count,elapsed):
    import numpy as np
    from r726_closed_spinor_fourier import ClosedSpinor
    from r726_paid_half_projection import paid_primitive,source_centroid,material_six
    from r703_weighted_material_field import Space,Field
    from r703_transported_lattice_anchor import CalibratedGrid
    from r728_paid_spinor_hermite import project,hermite_fits
    from r728_full_spinor_geometry import state,read_curve
    from r703_real_material_mass_continuation_20261128 import emit
    raw=Path(opt['frame']).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=opt['frame_sha256']:raise ValueError('Wrong immutable R687 frame.')
    original=json.loads(raw)
    if original['run']!=46146623642 or len(original['all_parameters'])!=1604:
        raise ValueError('R687 field is incomplete.')
    before=dict(count)
    g=CalibratedGrid(original,9,289,12,count)
    x703=np.array(prior['all_parameters'])
    A,sh,j703,cold,cleft,old=paid_primitive(Field(Space(12,5),g),x703)
    Eold=old['e0'].copy()**2
    count['new_needed_paid_source_native_reconstructions']+=1
    r=g.r;edge=g.edge_ids
    source_id=dict(angle_count=289,radial_order=9,outer_spans=12,radial_count=len(r),
                   parameter_count=157,prior_seconds=prior['elapsed_seconds'],prior_counts=prior['counts'],
                   original_R687_run=original['run'],preexisting_R687_counts=original['counts'])
    # The prior numerical frame and its large intermediate arrays are no longer needed.
    del old,g.anchor
    ctarget,length=source_centroid(A,cold,r)
    za,zb,pr=project(A,layout.K,opt['projection_half_cells'],count)
    fit=np.arange(len(r))%3!=1
    coeff,herm=hermite_fits(layout.space,r,g.guard_weights,fit,za,zb,ctarget,count)
    x=layout.pack(coeff)
    core=ClosedSpinor(layout.K,opt['reference_angles'])
    st,c,_=state(layout,core,x,r)
    uold=(A.x,A.d,A.dd);pold=(sh.x,sh.d,sh.dd)
    source_reads=[]
    for M in opt['source_material_reads']:
        phi=2*np.pi*np.arange(M)/M
        oldsix,oread=material_six(r,uold,pold,cold,phi)
        newsix,nread=material_six(r,st['auxiliary_position_jets'],st['auxiliary_shift_jets'],c,phi)
        both=np.broadcast_to(phi,(len(r),M))
        held=np.flatnonzero(~fit);selected=np.flatnonzero(fit)
        # Changing the source center's one-sided r jet changes only the true radial and double-radial columns.
        left=[y[edge].copy() for y in oldsix]
        left[1]+=(cleft[1]-cold[1][edge])[:,None,:]
        left[3]+=(cleft[2]-cold[2][edge])[:,None,:]
        eg=SimpleNamespace(r=r[edge],theta=g.theta,b=g.b);ec=tuple(z[edge] for z in cold)
        row=dict(material_angles=M,old_native_inverse=oread,new_native_inverse=nread,
                 fitted_six_actual=delta_six(newsix,oldsix,r,phi,selected),
                 held_out_six_actual=delta_six(newsix,oldsix,r,phi,held),
                 other_source_center_trace=delta_six([z[edge] for z in newsix],left,r[edge],phi,np.arange(len(edge))),
                 old_actual_on_prior_E=read_curve(g,oldsix,cold,Eold,both),
                 new_actual_on_prior_E=read_curve(g,newsix,c,Eold,both),
                 new_actual_on_own_E=read_curve(g,newsix,c,st['E'],both),
                 old_other_center_trace_on_prior_E=read_curve(eg,left,ec,Eold[edge],both[edge]))
        count['source_and_new_native_material_inversions']+=2*len(r)*M
        source_reads.append(row)
    target_diff=[float(np.linalg.norm(n-o,axis=-1).max()) for n,o in zip(c,ctarget)]
    emit('paid_source_represented_in_new_chart',source=source_id,counts_before=before,counts=dict(count),
         projected=pr,full_Hermite=herm,center_three_fit_errors=target_diff,
         normalized_old_curve_length_range=[float(length.x.min()),float(length.x.max())],
         actual_new_space=[layout.spans,layout.K],coefficients=x.tolist(),two_cross_reads=source_reads,seconds=elapsed())
    return x


def stage(opt):
    io_started=time.monotonic()
    token=os.environ.get('GITHUB_TOKEN')
    if not token:raise RuntimeError('The public job needs its read-only Actions receipt token.')
    root='https://api.github.com/repos/Rogerhu12/math-research-public'
    headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','User-Agent':'visible-flex-R728'}
    def metadata(url):
        with request.urlopen(request.Request(url,headers=headers),timeout=60) as q:
            return json.load(q)
    cert=opt['receipt'];rid=cert['run'];aid=cert['artifact']
    receipt_run=metadata(root+'/actions/runs/'+str(rid))
    art=metadata(root+'/actions/artifacts/'+str(aid))
    job=metadata(root+'/actions/jobs/'+str(cert['job']))
    if (job['id']!=cert['job'] or job['run_id']!=rid or job['status']!='completed' or job['conclusion']!='success'
        or art['name']!=cert['name'] or art['size_in_bytes']!=cert['size_bytes']):raise ValueError('Receipt job or actual artifact identity differs.')
    if (receipt_run['status']!='completed' or receipt_run['conclusion']!='success' or
        receipt_run['head_sha']!=cert['source'] or art['expired'] or art['id']!=aid or
        art['workflow_run']['id']!=rid or art['digest']!='sha256:'+cert['zip_sha256']):
        raise RuntimeError('The authenticated completed receipt differs from its binding.')
    class NoRedirect(request.HTTPRedirectHandler):
        def redirect_request(self,*unused):return None
    api_url=root+'/actions/artifacts/'+str(aid)+'/zip'
    try:
        with request.build_opener(NoRedirect).open(request.Request(api_url,headers=headers),timeout=60) as response:
            raw=response.read()
    except error.HTTPError as exc:
        if exc.code not in (301,302,303,307,308):raise
        location=exc.headers['Location']
        if parse.urlparse(location).scheme!='https':raise RuntimeError('Unexpected non-HTTPS artifact handoff.')
        # The signed object download must not carry the GitHub credential.
        with request.urlopen(location,timeout=120) as response:raw=response.read()
    if len(raw)!=cert['size_bytes'] or hashlib.sha256(raw).hexdigest()!=cert['zip_sha256']:raise ValueError('Receipt ZIP SHA differs.')
    with ZipFile(io.BytesIO(raw)) as archive:
        members=archive.namelist()
        if members.count(cert['member'])!=1:raise ValueError('Actual receipt member list lacks a unique R703 FINAL.')
        final=archive.read(cert['member'])
    if len(final)!=39163 or hashlib.sha256(final).hexdigest()!='bd5a52dcc40e31e898d3e02b99e4e5c0d449bfd697ac95faa8a168082c6012b2':
        raise ValueError('The source final member is not the paid 39163-byte literal.')
    output=Path(os.environ['RUNNER_TEMP'])/'r728-r703-natural-final.json'
    output.write_bytes(final)
    print(json.dumps(dict(kind='verified_historical_receipt',receipt_run=rid,artifact_id=aid,
              zip_sha256=cert['zip_sha256'],actual_member_list=members,member=cert['member'],literal_bytes=len(final),
              literal_sha256=hashlib.sha256(final).hexdigest(),administrative_io_seconds=time.monotonic()-io_started,
              new_scientific_evaluations=0),sort_keys=True),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--request',required=True)
    args=ap.parse_args();req=json.loads(Path(args.request).read_bytes())
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public':
        raise SystemExit('Bound public Actions context required.')
    cfg=req['common_parameters']['geometry']
    for p in (str(Path(__file__).resolve().relative_to(Path.cwd())),cfg):
        if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=req['source_sha256'][p]:
            raise ValueError('Administrative receipt source or configuration binding differs.')
    stage(json.loads(Path(cfg).read_bytes()))
