#!/usr/bin/env python3
"""One actual M160 closed-port warm field, not a solved isometry.

The saved M320 pulse prefix is truncated explicitly, then a long physical
Hermite bridge is projected onto the finite residual-q space. The compact
material-circle lift remains analytic and untruncated. Exact Hold scalar
and symbolic node locations are accompanied by rigorous scalar boxes;
the ordinary-double operator uses their declared floating carriers.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

INPUT_SHA='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
ORACLE_SHA='a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'
M=160
PROJECTION_N=8192

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
def upper_float(q):
    out=float(q)
    if Q(out)<q:out=np.nextafter(out,np.inf)
    if not np.isfinite(out):raise ValueError('Nonfinite bound carrier')
    return float(out)
def carrier_error(f,box,scale):
    return max(abs(Q(f)-Q(box[0],scale)),abs(Q(f)-Q(box[1],scale)))
def hermite(t,width,left,right):
    c0=left[0];c1=width*left[1];c2=.5*width*width*left[2]
    e0=right[0]-c0-c1-c2;e1=width*right[1]-c1-2*c2;e2=width*width*right[2]-2*c2
    c3=10*e0-4*e1+.5*e2;c4=-15*e0+7*e1-e2;c5=6*e0-3*e1+.5*e2
    value=c0+t*(c1+t*(c2+t*(c3+t*(c4+t*c5))))
    first=(c1+t*(2*c2+t*(3*c3+t*(4*c4+t*5*c5))))/width
    second=(2*c2+t*(6*c3+t*(12*c4+t*20*c5)))/(width*width)
    return np.stack((value,first,second))
def compact_lift(s,S,R,H,width,C):
    if s<=S-width:chi=cp=cpp=0.
    elif s>=S:chi,cp,cpp=1.,0.,0.
    else:
        u=(s-S+width)/width
        chi=u*u*u*(10+u*(-15+6*u));cp=30*u*u*(1-u)*(1-u)/width
        cpp=60*u*(1-u)*(1-2*u)/(width*width)
    b=R+(S-s)
    out=np.array([chi*b,cp*b-chi,cpp*b-2*cp])[:,None]*C[None,:]
    out[:,2*M+1]+=H*np.array([chi,cp,cpp])
    return out

def main(a):
    start=time.perf_counter();source_sha=sha(__file__)
    if sha(a.input)!=INPUT_SHA or sha(a.scalar_source)!=ORACLE_SHA:
        raise ValueError('This warm definition has fixed real-parent and exact-oracle identities')
    data=json.loads(gzip.decompress(a.input.read_bytes()))
    full=load('fullclosed_exact_hold',a.scalar_source).FullHold(
        data,a.integer_source,a.hold_source,panels=128)
    oldM=int(data['M']);oldmesh=np.array(data['mesh']);n=3*M+2
    old=np.stack([np.array(data[k])for k in ('states','rhs','d2')],axis=1)
    if oldM!=320 or oldmesh.shape!=(819,) or oldmesh[0]!=0 or oldmesh[-1]!=1:
        raise ValueError('Unexpected actual pulse parent')
    keep=np.r_[np.arange(M+1),np.arange(oldM+1,oldM+M+1),np.arange(2*oldM+1,2*oldM+M+2)]
    prefix=old[:,:,keep].copy();omit=np.setdiff1d(np.arange(3*oldM+2),keep)
    omitted=np.sum(np.abs(old[:,:,omit]),axis=2)
    core=prefix[0,0,1:M+1].copy();freq=2.*np.arange(1,M+1);qfreq=1-freq*freq

    # This finite circle is a warm-generator projection, not the physical
    # lift. Its exact binary coefficients are saved in the bundle.
    phi=2*np.pi*np.arange(PROJECTION_N)/PROJECTION_N
    delta=np.sin(phi[:,None]*freq)@((qfreq/freq)*core)
    co,si=np.cos(delta),np.sin(delta)
    fc=np.fft.rfft(co)/PROJECTION_N;fs=np.fft.rfft(si)/PROJECTION_N
    C=np.zeros(n);C[0]=fc[0].real;C[1:M+1]=2*fc[(2*np.arange(1,M+1))].real
    C[M+1:2*M+1]=-2*fs[(2*np.arange(1,M+1))].imag
    reconstructed=np.c_[np.cos(phi[:,None]*np.r_[0,freq])@C[:M+1],
                          np.sin(phi[:,None]*freq)@C[M+1:2*M+1]]
    projection_grid_error=float(np.max(np.linalg.norm(reconstructed-np.c_[co,si],axis=1)))

    S,R=full.carrier(full.S),full.carrier(full.R)
    w_exact=Q(.05);width=float(w_exact)
    _,z1=full.at_box(full.point_box(Q(1)))
    dz=full.o.subtract(full.height_increment,z1)
    reference_lift=full.carrier(dz)
    H=float(prefix[-1,0,2*M+1]+reference_lift)

    # Each node is exactly a*S+b. Original binary nodes have a=0, and
    # are retained literally in the numerical carrier mesh as well.
    node_defs=[(Q(0),Q(float(s)))for s in oldmesh]
    fixed_rise_start=full.cut+full.f+full.hold
    fixed_rise_end=fixed_rise_start+full.rise
    segments=[((Q(0),Q(1)),(Q(0),fixed_rise_start),4),
              ((Q(0),fixed_rise_start),(Q(0),fixed_rise_end),8),
              ((Q(0),fixed_rise_end),(Q(1),-w_exact),64),
              ((Q(1),-w_exact),(Q(1),-full.out),12),
              ((Q(1),-full.out),(Q(1),Q(0)),16)]
    for l,r,count in segments:
        if node_defs[-1]!=l:raise ValueError('Symbolic mesh does not concatenate')
        for j in range(1,count+1):
            t=Q(j,count);node_defs.append(((1-t)*l[0]+t*r[0],(1-t)*l[1]+t*r[1]))
    time_boxes=[full.affine_time(c,b)for c,b in node_defs]
    mesh=np.array([full.carrier(b)for b in time_boxes]);mesh[:len(oldmesh)]=oldmesh;mesh[-1]=S
    if len(mesh)!=923 or not np.all(np.diff(mesh)>0):raise ValueError('Unexpected fixed 922-cell mesh')

    # Long bridge in floating carriers, used only to choose literal q
    # nodal coefficients. The exact candidate is the shared-quintic q
    # on the symbolic mesh plus the full analytic lift, not this bridge.
    terminal=np.zeros((3,n));terminal[0]=R*C;terminal[0,2*M+1]+=H;terminal[1]=-C
    qjets=np.zeros((len(mesh),3,n));qjets[:len(prefix)]=prefix
    bridge_width=S-1
    for i in range(len(prefix),len(mesh)):
        bridge=hermite((mesh[i]-1)/bridge_width,bridge_width,prefix[-1],terminal)
        qjets[i]=bridge-compact_lift(mesh[i],S,R,H,width,C)
    terminal_roundoff=qjets[-1].copy();qjets[-1]=0.

    # Explicit affine projection is part of the new warm identity.
    # The raw parent differs in one tiny T relation; U0 and A0_Z are
    # already exact. This is not silently attributed to the parent.
    before=qjets[0].copy();qjets[0,0]=0.;qjets[0,0,0]=1.;qjets[0,0,1:M+1]=core
    qjets[0,0,M+1:2*M+1]=-freq*core
    qjets[0,1]=0.;qjets[0,1,2*M+1]=1.;qjets[0,2,2*M+1:]=0.
    core_delta=qjets[0]-before

    stage_defs=[]
    for i,d in enumerate(node_defs):
        stage_defs.append(d)
        if i+1<len(node_defs):
            e=node_defs[i+1];stage_defs.append(((d[0]+e[0])/2,(d[1]+e[1])/2))
    stage_times=np.empty(2*len(mesh)-1);stage_times[::2]=mesh
    stage_times[1::2]=mesh[:-1]+np.diff(mesh)/2
    a_values=[];a_boxes=[];a_errors=[];time_errors=[]
    for j,(c,b)in enumerate(stage_defs):
        tbox=full.affine_time(c,b);abox,_=full.at_box(tbox)
        value=full.carrier(abox)
        if j==0:value=1.
        if j==len(stage_defs)-1:value=R
        a_values.append(value);a_boxes.append(full.enclosure(abox))
        a_errors.append(carrier_error(value,abox,full.h.S))
        time_errors.append(carrier_error(float(stage_times[j]),tbox,full.h.S))
    a_values=np.array(a_values)
    if not np.all(a_values>0)or a_values[0]!=1. or a_values[-1]!=R:raise ValueError('Bad scalar carriers')
    if not np.isfinite(qjets).all()or not np.isfinite(H):raise ValueError('Nonfinite warm')
    if sha(__file__)!=source_sha:raise ValueError('Producer changed during generation')

    bundle=a.out.with_suffix('.npz')
    np.savez_compressed(bundle,mesh=mesh,qjets=qjets,a_stages=a_values,
        radius=np.array(R),Hcap=np.array(H),width=np.array(width),
        fixed_core_first3=core[:3],circle_projection=C,
        a_stage_absolute_error=np.array([upper_float(v)for v in a_errors]),
        stage_time_absolute_error=np.array([upper_float(v)for v in time_errors]))
    report=dict(schema='fullclosed-hold-real-pulse-warm-v1',source_sha256=source_sha,
        input_path=str(a.input),input_sha256=INPUT_SHA,bundle_path=str(bundle),bundle_sha256=sha(bundle),
        scalar_source_path=str(a.scalar_source),scalar=full.metadata(),
        M=M,n=n,projection_N=PROJECTION_N,suggested_operator_N=2048,
        J=len(mesh),cells=len(mesh)-1,stages=len(stage_defs),free_size=3*len(mesh)*n-2413,
        radius_carrier=R,S_carrier=S,Hcap=H,width_exact=str(w_exact),width_carrier=width,
        Hcap_definition='binary pulse end Z-mean plus the binary midpoint of exact Hold reference height from s=1 to S; a free design height, not a solved physical quantity',
        reference_lift_box=full.enclosure(dz),reference_lift_carrier=reference_lift,
        true_scalar_nodes=[dict(S_coefficient=str(c),constant=str(b))for c,b in node_defs],
        true_a_stage_boxes=a_boxes,
        maximum_a_carrier_error_exact=str(max(a_errors)),maximum_a_carrier_error_upper=upper_float(max(a_errors)),
        maximum_stage_time_carrier_error_exact=str(max(time_errors)),maximum_stage_time_carrier_error_upper=upper_float(max(time_errors)),
        prefix_projection=dict(parent_M=oldM,retained_M=M,preserved_original_binary_nodes=len(oldmesh),
            nodal_omitted_coefficient_l1_max_by_jet=np.max(omitted,axis=0).tolist(),
            scope='ordinary coefficient diagnostics at saved nodes; not inherited continuous Gram or curvature bounds',
            core_affine_change_by_jet=np.max(np.abs(core_delta),axis=1).tolist(),
            core_affine_changed_entries=np.argwhere(core_delta!=0).tolist(),
            all_other_retained_prefix_coefficients_preserved=bool(np.array_equal(qjets[1:len(prefix)],prefix[1:])),
            actual_parent_fixed_first3=core[:3].tolist()),
        circle_projection=dict(method='N8192 DFT of cos(Theta-phi),sin(Theta-phi), retain ordinary even frequencies 0..320; literal coefficients saved',
            sampled_projection_error=projection_grid_error,analytic_physical_lift_truncated=False),
        terminal_affine_projection_by_jet=np.max(np.abs(terminal_roundoff),axis=1).tolist(),
        field_definition='Exact binary q node jets on exact affine-in-S mesh; unique shared quintic per cell; add analytic untruncated compact material-circle lift',
        numerical_operator_scope='Ordinary double carrier mesh/a/R approximate the exact target; scalar/time carrier errors enclosed, no full field rounding certificate',
        same_prefix_metric_after_cut=False,
        metric_note='The retained raw pulse prefix after .995 is only a warm for the new Hold scalar, even before M160 truncation',
        exact_core_affine=True,terminal_q_three_jets_exact_zero=True,
        terminal_physical_port='R*e_r(Theta)+H*e_z, radial derivative -e_r(Theta), radial second derivative 0',
        nonlinear_solve=False,metric_accepted=False,embedding_certified=False,reach_certified=False,
        seconds=time.perf_counter()-start)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k]for k in ('schema','source_sha256','bundle_path','bundle_sha256','J','cells','stages','free_size','S_carrier','radius_carrier','Hcap','maximum_a_carrier_error_upper','maximum_stage_time_carrier_error_upper','seconds')},indent=2),flush=True)
    print(json.dumps(dict(report_path=str(a.out),report_sha256=sha(a.out))),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('input','scalar-source','integer-source','hold-source','out'):p.add_argument('--'+k,type=Path,required=True)
    main(p.parse_args())
