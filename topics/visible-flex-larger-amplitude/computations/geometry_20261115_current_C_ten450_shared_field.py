#!/usr/bin/env python3
"""Current-C ten450 radial Hermite/shared-background finite field.

This source consumes a genuine R400 frozen450 checkpoint and the independent
complete current-C radial replay.  It does not call old stored-tail or old
background constructors.  The exact_field API differentiates the explicitly
defined exact Hermite/Fourier expression.  Separate numerical rendering
methods are rounded approximations, with no transferred error certificate.
Its defining
horizontal second-node data use the disclosed original nonuniform finite
difference rule; they are not certified second derivatives of the old point
readout.  Target C, the exact ten scalar DAG, and geometric B remain different
objects.  No BVP or geometric acceptance is produced.

The old R249 inlet projection and exact difference bounds are reused as pure
algebra, with a new current-ten source identity and no legacy scalar dispatch.
All scientific execution, including FFT/Hermite generation, is Actions-only.
Author: geometry agent (AI), 2026-11-15.
"""
from __future__ import annotations
import argparse
from collections import OrderedDict
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import struct
import subprocess
import sys
import time
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent
REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R409-current-C-ten450-shared-background-complete-field-v1"
PLAN_SCHEMA="R409-current-C-ten450-shared-field-plan-input-v1"
NODE_NAME="geometry_20261115_current_C_ten450_radial_readout.mjs"
NODE_SHA="5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568"
NODE_SCHEMA="current-C-ten450-complete-radial-Cartesian-readout-v1"
SAVED_NAME="geometry_20261115_continuous_ten_frozen450_saved_prefix.py"
SAVED_SHA="1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520"
BACKGROUND_NAME="geometry_20261114_shared_background_normal_form.py"
BACKGROUND_SHA="da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9"
PARITY_NAME="geometry_20261114_inlet_parity_normal_form.py"
PARITY_SHA="ce5f287c1de870b6bf71d1650d6942e23fd2bdd23a25af72ec5b637599a97410"
ACTIVE_NAME="geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA="675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
CAPACITY_NAME="exact_20261114_tail_capacity_loader.mjs"
CAPACITY_SHA="07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395"
GUARD_KEY="closed_geometry_wrapper"
LOADER_NAME="geometry_20261115_current_C_ten450_shared_field.load_shared_bundle"
SOURCE_PINS={SAVED_NAME:SAVED_SHA,BACKGROUND_NAME:BACKGROUND_SHA,PARITY_NAME:PARITY_SHA,
             ACTIVE_NAME:ACTIVE_SHA,NODE_NAME:NODE_SHA,CAPACITY_NAME:CAPACITY_SHA}

def actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
            os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Construct actual current-C finite fields only in the named public repository Actions")

def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def receipt(path,base=None):
    path=Path(path);raw=path.read_bytes()
    return dict(file=str(path.relative_to(base)) if base is not None else path.name,
        bytes=len(raw),sha256=sha(raw))

def read(path,expected=None):
    raw=Path(path).read_bytes()
    if expected is not None and sha(raw)!=expected:
        raise ValueError("Actual input SHA differs: "+str(path))
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)

def within(root,name):
    root=Path(root).resolve()
    if not isinstance(name,str) or Path(name).is_absolute():
        raise ValueError("Relative owned payload path required")
    candidate=root/name
    if not candidate.resolve().is_relative_to(root) or candidate.resolve()==root:
        raise ValueError("Payload escaped its actual root")
    v=candidate
    while v!=root:
        if v.is_symlink():raise ValueError("Payload symlink is not an owned file")
        v=v.parent
    return candidate

def member(root,descriptor):
    p=within(root,descriptor["file"]);r=receipt(p)
    if r["bytes"]!=descriptor["bytes"] or r["sha256"]!=descriptor["sha256"]:
        raise ValueError("Complete current field member differs")
    return p

def write(path,value):
    path=Path(path);raw=canonical(value)
    with path.open("xb") as f:f.write(raw);f.flush();os.fsync(f.fileno())
    return receipt(path)

def exact(value):
    if isinstance(value,Q):return value
    if isinstance(value,str):return Q(value)
    if type(value) is int:return Q(value)
    if not math.isfinite(float(value)):raise ValueError("Finite exact source value required")
    return Q.from_float(float(value))

def word(x):
    return struct.pack("<d",float(x)).hex()

def array_identity(np,a,dtype):
    b=np.asarray(a,dtype=dtype,order="C")
    if not np.all(np.isfinite(b)):raise ValueError("Nonfinite defining array")
    raw=b.tobytes()
    return dict(shape=list(b.shape),dtype=dtype,bytes=len(raw),sha256=sha(raw),
        shape_and_raw_sha256=sha(str(b.shape).encode()+b"\0"+raw))

def load(directory,name,expected,module_name):
    p=Path(directory)/name
    if receipt(p)["sha256"]!=expected:raise ValueError("Source differs: "+name)
    for module in tuple(sys.modules.values()):
        f=getattr(module,"__file__",None)
        if f is not None and Path(f).resolve()==p.resolve():return module
    spec=importlib.util.spec_from_file_location(module_name,p)
    m=importlib.util.module_from_spec(spec);sys.modules[module_name]=m
    try:spec.loader.exec_module(m)
    except BaseException:
        sys.modules.pop(module_name,None);raise
    return m

def runtime(directory):
    actions();directory=Path(directory)
    if str(directory) not in sys.path:sys.path.insert(0,str(directory))
    source={}
    for n,h in SOURCE_PINS.items():
        source[n]=receipt(directory/n)
        if source[n]["sha256"]!=h:raise ValueError("Complete current field source differs: "+n)
    Saved=load(directory,SAVED_NAME,SAVED_SHA,"_current_ten_radial_saved")
    Background=load(directory,BACKGROUND_NAME,BACKGROUND_SHA,"_current_ten_shared_B")
    Parity=load(directory,PARITY_NAME,PARITY_SHA,"_current_ten_parity_algebra")
    import numpy as np
    source[Path(__file__).name]=receipt(__file__)
    return np,Saved,Background,Parity,source

class ResourceStop(RuntimeError):
    pass

class ExternalStop(RuntimeError):
    def __init__(self,number):
        self.signal_number=number
        super().__init__("Actual external signal "+str(number)+"; no geometric failure is inferred")

class Budget:
    def __init__(self,out,seconds,reserve,start=None):
        if not math.isfinite(seconds) or seconds<=0 or type(reserve) is not int or reserve<0:
            raise ValueError("Positive work budget and explicit disk reserve required")
        self.out=Path(out);self.seconds=seconds;self.reserve=reserve
        self.start=time.monotonic() if start is None else start
    def check(self):
        if time.monotonic()-self.start>=self.seconds:raise ResourceStop("Explicit finite-field work deadline reached")
        st=os.statvfs(self.out)
        if st.f_bavail*st.f_frsize<self.reserve:raise ResourceStop("Owned finite-field disk reserve reached")

def normalize_inlet(saved,np,Parity):
    """Same R249 node projection, explicit current-ten metadata, no old loader."""
    old=saved.quintic;x=np.asarray(old.x,dtype=float)
    nodal=[v.copy() for v in old.nodal];iz=2*saved.M+1
    if x[0]!=0 or len(x)<2 or saved.n!=338:
        raise ValueError("Complete original reflection inlet and all338 rows required")
    nodal[0][0,iz:]=0.0;nodal[1][0,:iz]=0.0;nodal[2][0,iz:]=0.0
    differences=np.asarray([a[0]-b[0] for a,b in zip(nodal,old.nodal)])
    new=saved._kernel.PhysicalQuintic(x,*nodal)
    if (not all(np.array_equal(a[1:],b[1:]) for a,b in zip(old.nodal,new.nodal))
            or not np.array_equal(old.coefficients[1:],new.coefficients[1:])):
        raise AssertionError("Only the three original R249 inlet blocks may change")
    h=exact(x[1])-exact(x[0])
    bounds,_=Parity._patch_bounds(saved,differences,h)
    witness=Parity._exact_cell_witness(differences,h)
    record=dict(schema=SCHEMA+"-R249-inlet-projection",source=receipt(__file__),
        original_pure_algebra_source_sha256=PARITY_SHA,
        actual_checkpoint=copy.deepcopy(saved.checkpoint.receipt),
        original_nodes=[array_identity(np,a,"<f8") for a in old.nodal],
        normalized_nodes=[array_identity(np,a,"<f8") for a in new.nodal],
        original_complete_target=copy.deepcopy(saved.checkpoint.target_identity),
        exact_correction_witness=witness,continuous_patch_jet_bounds=bounds,
        first_cell=[float(x[0]),float(x[1])],
        projection={"position":"all z0..z112 at node0",
                    "first_s":"all R0..R112,T1..T112 at node0",
                    "second_s":"all z0..z112 at node0"},
        every_other_node_and_cut_twojet_retained=True,
        same_actual_native_H_and_all112_response_retained=True,
        actual_checkpoint_not_edited=True,new_BVP_acceptance=False,
        exact_real_shared_node_inlet_reflection_C2=True,
        rounded_evaluator_identity_certified=False,target_metric_bound_certified=False)
    saved.original_quintic=old;saved.quintic=new
    saved.sol=SimpleNamespace(x=x,y=new.nodal[0].T,p=saved.sol.p,sol=new)
    saved.inlet_normalization=record;saved.inlet_exact_correction_witness=witness
    saved.definition=copy.deepcopy(saved.definition)
    saved.definition.update(current_C_closed_inlet_normalization=record,
        actual_accepted_parent_is_source_only_after_geometric_projection=True,
        original_prefix_metric_bounds_inherited=False)
    return record

class CurrentRadialReadout:
    def __init__(self,directory,result_sha,checkpoint,np):
        self.directory=Path(directory);self.np=np
        self.result=read(self.directory/"result.json",result_sha)
        r=self.result
        if (r.get("schema")!=NODE_SCHEMA or r.get("completed") is not True
                or r.get("source",{}).get("sha256")!=NODE_SHA
                or r.get("run_id")!=checkpoint.manifest["run_id"]
                or r.get("source_commit")!=checkpoint.manifest["source_commit"]
                or r.get("checkpoint")!=checkpoint.receipt
                or r.get("current_target_identity")!=checkpoint.target_identity):
            raise ValueError("The complete current-C replay belongs to another actual450 field")
        self.complete_path=member(self.directory,r["complete"])
        self.complete=read(self.complete_path);c=self.complete
        if (c.get("schema")!=NODE_SCHEMA+"-complete" or c.get("finished") is not True
                or c.get("originalStages")!=576 or c.get("angular")!=2048
                or c.get("run_id")!=checkpoint.manifest["run_id"]
                or c.get("source_commit")!=checkpoint.manifest["source_commit"]
                or c.get("original_checkpoint")!=checkpoint.receipt
                or c.get("final_native")!=checkpoint.manifest["members"]["final_native"]
                or c.get("original_native_binding")!=checkpoint.manifest["original_native_binding"]
                or c.get("current_target_identity")!=checkpoint.target_identity):
            raise ValueError("Complete original stage/mean/native/target identity differs")
        self.N=2048;self.steps=int(c["steps"])
        if (self.steps!=checkpoint.native_configuration["steps"] or
                len(c["rows"])!=576*self.steps+1 or c["completedNodes"]!=len(c["rows"])):
            raise ValueError("Keep every actual RK-step endpoint and every shooting stage")
        original=c["rows"]
        if [row["node"] for row in original]!=list(range(len(original))):
            raise ValueError("Complete radial nodes are missing or reordered")
        self.rows=list(reversed(copy.deepcopy(original)))
        self.r=np.asarray([row["geometry"]["r"] for row in self.rows],dtype=float)
        if not np.all(np.diff(self.r)>0):
            raise ValueError("The actual full radial node words are not strictly increasing")
        if exact(self.r[-1])!=checkpoint.owner.data["cut"]:
            raise ValueError("The actual radial cut differs from this same target")
        self.raw_cache=OrderedDict()
    def raw(self,index):
        if index in self.raw_cache:
            self.raw_cache.move_to_end(index);return self.raw_cache[index]
        row=self.rows[index];p=within(self.directory,row["file"]);blob=p.read_bytes()
        if len(blob)!=row["bytes"] or sha(blob)!=row["sha256"]:raise ValueError("Original radial packet differs")
        raw=gzip.decompress(blob)
        if len(raw)!=row["raw_bytes"] or sha(raw)!=row["rawSha256"] or row["shape"]!=[self.N,12]:
            raise ValueError("Complete radial angular packet identity differs")
        values=self.np.frombuffer(raw,dtype="<f8").reshape(self.N,12).copy()
        if not self.np.all(self.np.isfinite(values)):raise ValueError("A radial packet is nonfinite")
        self.raw_cache[index]=values
        while len(self.raw_cache)>3:self.raw_cache.popitem(last=False)
        return values
    def defining_node_coefficients(self,index):
        """New binary64 node definition; derivative consistency belongs to Hermite."""
        np=self.np;z=self.raw(index);row=self.rows[index];g=row["geometry"]
        y=z[:,:3].copy();v=z[:,3:6].copy();a=np.empty_like(y)
        y[:,2]+=float(row["meanPerturbationInnerAnchor"])
        v[:,2]-=float(g["w"]);a[:,2]=z[:,9]-float(g["wr"])
        if index==0:
            a[:,:2]=(self.raw(1)[:,3:5]-z[:,3:5])/(self.r[1]-self.r[0])
        elif index==len(self.r)-1:
            a[:,:2]=(z[:,3:5]-self.raw(index-1)[:,3:5])/(self.r[index]-self.r[index-1])
        else:
            hm=self.r[index]-self.r[index-1];hp=self.r[index+1]-self.r[index]
            a[:,:2]=(hp/(hm+hp)*(z[:,3:5]-self.raw(index-1)[:,3:5])/hm+
                       hm/(hm+hp)*(self.raw(index+1)[:,3:5]-z[:,3:5])/hp)
        result=[]
        for values in (y,v,a):
            coefficients=np.fft.rfft(values,axis=0)/self.N
            coefficients[1:-1]*=2
            result.append(coefficients)
        result=np.asarray(result,dtype="<c16")
        if result.shape!=(3,self.N//2+1,3) or not np.all(np.isfinite(result)):
            raise ValueError("Keep the complete DC/Nyquist/all coordinate/node012 coefficients")
        return result

class CurrentRadialTail:
    """Original full Fourier API, sourced solely from the new current-C nodes."""
    def __init__(self,directory,definition,np,Background):
        self.directory=Path(directory);self.definition=definition;self.np=np;self.Bg=Background
        self.N=definition["angular"];self.rows=copy.deepcopy(definition["rows"])
        self.r=np.asarray([row["geometry"]["r"] for row in self.rows],dtype=float)
        self.coefficient_records=definition["coefficient_records"]
        if self.N!=2048 or len(self.rows)!=len(self.coefficient_records) or not np.all(np.diff(self.r)>0):
            raise ValueError("Complete current radial coefficient layout differs")
        self.cache=OrderedDict();self.cell_cache=OrderedDict()
    def node_coefficients(self,index):
        if index in self.cache:self.cache.move_to_end(index);return self.cache[index]
        d=self.coefficient_records[index];p=member(self.directory,d);raw=p.read_bytes()
        if d["shape"]!=[3,self.N//2+1,3] or d["dtype"]!="<c16" or d["order"]!="C":
            raise ValueError("Complete radial Fourier node descriptor differs")
        a=self.np.frombuffer(raw,dtype="<c16").reshape(d["shape"]).copy()
        if not self.np.all(self.np.isfinite(a)):raise ValueError("Nonfinite complete radial coefficient")
        self.cache[index]=a
        while len(self.cache)>4:self.cache.popitem(last=False)
        return a
    def exact_span(self,index):
        if index in self.cell_cache:self.cell_cache.move_to_end(index);return self.cell_cache[index]
        if index<0:raise ValueError("Collar coefficients are defined by the closed assembler")
        left,right=self.node_coefficients(index),self.node_coefficients(index+1)
        h=exact(self.r[index+1])-exact(self.r[index])
        value=tuple(tuple(tuple(self.Bg.hermite(
            tuple(exact(left[d,k,j].real if part==0 else left[d,k,j].imag) for d in range(3)),
            tuple(exact(right[d,k,j].real if part==0 else right[d,k,j].imag) for d in range(3)),h)
            for part in range(2)) for j in range(3)) for k in range(self.N//2+1))
        self.cell_cache[index]=value
        while len(self.cell_cache)>2:self.cell_cache.popitem(last=False)
        return value
    def coefficients(self,radius):
        from bisect import bisect_right
        r=exact(radius)
        if not exact(self.r[0])<=r<=exact(self.r[-1]):raise ValueError("Radial query outside represented field")
        index=min(len(self.r)-2,bisect_right([exact(v) for v in self.r],r)-1)
        h=exact(self.r[index+1])-exact(self.r[index]);t=(r-exact(self.r[index]))/h
        span=self.exact_span(index);result=self.np.empty((3,self.N//2+1,3),dtype="<c16")
        for d in range(3):
            for k in range(self.N//2+1):
                for j in range(3):
                    q=[self.Bg.evaluate(self.Bg.differentiated(span[k][j][part],h,d),t) for part in range(2)]
                    result[d,k,j]=complex(float(q[0]),float(q[1]))
        return result

def synth(np,coefficients,theta,order=0):
    c=np.asarray(coefficients);theta=np.asarray(theta,dtype=float)
    k=np.arange(c.shape[-2],dtype=float)
    phase=np.exp(1j*k[:,None]*theta[None,:])*(1j*k[:,None])**order
    return np.real(np.einsum("...kj,kn->...nj",c,phase))

class CurrentSharedAssembly:
    """Independent complete field with one common material map and own B."""
    def __init__(self,saved,tail,plan,B,geometry,np,Background,registration=None):
        self.saved,self.tail,self.plan=saved,tail,plan
        self.shared_background,self.shared_background_geometry=B,copy.deepcopy(geometry)
        self.np,self.Bg=np,Background
        self.cuff=float(plan["cuff"]);self.inner=float(tail.r[0]);self.cut=float(tail.r[-1])
        self.L=float(saved.quintic.x[-1]);self.W=float(plan["cut_correction_width"]);self.sigma=-1.
        self.reflection=np.array([1.,1.,-1.])
        self.ap,self.app=map(float,plan["declared_cut_radial_chart_jets"][1:])
        self.a=self.cut;self.cap_height=float(B.nodal[0][0]);self.offset=float(B.nodal[-1][0])
        if not 0<self.cuff<self.inner<self.cut-self.W<self.cut or not self.ap<0:
            raise ValueError("The complete original collar/cut-chart layout is unpaid")
        self.inner_coeff=tail.node_coefficients(0)
        self.outer_coeff=tail.node_coefficients(len(tail.r)-1)
        self._collar=None;self.delta_cache={};self._scalar_cache={}
        if registration is None:
            theta=2*np.pi*np.arange(tail.N)/tail.N
            original,_,_=saved.nine_jets([self.L],theta,normalized=False)
            native=self.native_cut_nine(theta)
            saved.set_native_registration(original[(0,0)][0,:,:2],native[(0,0)][:,:2])
        else:
            if saved.registration is not None:raise ValueError("Do not stack registrations")
            saved.registration=copy.deepcopy(registration)
            saved.rotation_to_native=np.asarray(registration["prefix_to_native_row_rotation"],dtype=float)
            saved.translation_from_native=np.asarray(registration["prefix_translation_to_subtract"],dtype=float)
        self.registration=copy.deepcopy(saved.registration)
    def scalar_jets(self,radii):
        rows=[]
        for value in radii:
            q=exact(value)
            if q not in self._scalar_cache:
                self._scalar_cache[q]=tuple(float(self.shared_background.evaluate_exact(q,d)) for d in range(3))
            rows.append(self._scalar_cache[q])
        return self.np.asarray(rows,dtype=float)
    def native_cut_nine(self,theta):
        np=self.np;theta=np.asarray(theta,dtype=float);scalar=self.scalar_jets([self.cut])[0]
        circle=(np.column_stack([np.cos(theta),np.sin(theta)]),
            np.column_stack([-np.sin(theta),np.cos(theta)]),
            np.column_stack([-np.cos(theta),-np.sin(theta)]))
        result={}
        for d in range(3):
            for j in range(3):
                v=synth(np,self.outer_coeff[d],theta,j)*self.reflection
                v[:,:2]+=(self.cut,1.,0.)[d]*circle[j]
                if j==0:v[:,2]+=scalar[d]
                result[d,j]=v
        return result
    def cut_difference(self,theta):
        np=self.np;theta=np.asarray(theta,dtype=float);key=theta.tobytes()
        if key in self.delta_cache:return self.delta_cache[key]
        full,_,_=self.saved.nine_jets([self.L],theta);native=self.native_cut_nine(theta)
        out={}
        for j in range(3):
            target=(full[0,j][0],full[1,j][0]/self.ap,
                full[2,j][0]/self.ap**2-self.app*full[1,j][0]/self.ap**3)
            for d in range(3):out[d,j]=target[d]-native[d,j]
        self.delta_cache[key]=out
        if len(self.delta_cache)>4:self.delta_cache.pop(next(iter(self.delta_cache)))
        return out
    def collar_coefficients(self,radius):
        np=self.np;h=exact(self.inner)-exact(self.cuff);t=(exact(radius)-exact(self.cuff))/h
        result=np.empty_like(self.inner_coeff)
        for d in range(3):
            for k in range(self.tail.N//2+1):
                for j in range(3):
                    values=[]
                    for part in range(2):
                        right=tuple(exact(self.inner_coeff[a,k,j].real if part==0 else self.inner_coeff[a,k,j].imag) for a in range(3))
                        coeff=self.Bg.hermite((Q(0),Q(0),Q(0)),right,h)
                        values.append(self.Bg.evaluate(self.Bg.differentiated(coeff,h,d),t))
                    result[d,k,j]=complex(float(values[0]),float(values[1]))
        return result
    def weights(self,radius,derivative):
        r=exact(radius);start=exact(self.cut)-exact(self.W);W=exact(self.W)
        if r<start:return (0.,0.,0.)
        t=(r-start)/W
        rows=((0,0,0,10,-15,6),(0,0,0,-4*W,7*W,-3*W),
              (0,0,0,W*W/2,-W*W,W*W/2))
        return tuple(float(self.Bg.evaluate(self.Bg.differentiated(c,W,derivative),t)) for c in rows)
    def perturbation(self,radii,theta):
        np=self.np;radii=np.asarray(radii,dtype=float);theta=np.asarray(theta,dtype=float)
        coeff=np.asarray([self.tail.coefficients(r) if r>=self.inner else self.collar_coefficients(r) for r in radii])
        indices=dict(pos=(0,0),s1=(1,0),s2=(2,0),p1=(0,1),p2=(0,2),sp=(1,1))
        out={name:synth(np,coeff[:,d],theta,j) for name,(d,j) in indices.items()}
        if np.any(radii>=self.cut-self.W):
            delta=self.cut_difference(theta)
            for name,(d,j) in indices.items():
                weights=np.asarray([self.weights(r,d) for r in radii])
                values=np.stack([delta[k,j]*self.reflection for k in range(3)])
                out[name]+=np.einsum("rk,knc->rnc",weights,values)
        return out
    def tail_jets(self,radii,theta):
        np=self.np;r=np.asarray(radii,dtype=float);theta=np.asarray(theta,dtype=float)
        scalar=self.scalar_jets(r);out=self.perturbation(r,theta)
        for v in out.values():v[:,:,2]*=-1
        co,si=np.cos(theta)[None,:],np.sin(theta)[None,:];zero=np.zeros((len(r),len(theta)))
        out["pos"]+=np.stack(np.broadcast_arrays(r[:,None]*co,r[:,None]*si,scalar[:,0,None]),axis=-1)
        out["s1"]+=np.stack(np.broadcast_arrays(co,si,scalar[:,1,None]),axis=-1)
        out["s2"][:,:,2]+=scalar[:,2,None]
        out["p1"]+=np.stack(np.broadcast_arrays(-r[:,None]*si,r[:,None]*co,zero),axis=-1)
        out["p2"]+=np.stack(np.broadcast_arrays(-r[:,None]*co,-r[:,None]*si,zero),axis=-1)
        out["sp"]+=np.stack(np.broadcast_arrays(-si,co,zero),axis=-1)
        return out
    def prefix_jets(self,s,theta,height=None):
        return self.saved.material_jets(s,theta,height)
    def marker_rows(self,upper):
        return [r for r in self.plan["fixed_cap"]["markers"] if r["upper"] is upper]
    def cap(self,r,theta,upper=True):
        np=self.np;xy=np.stack(np.broadcast_arrays(np.asarray(r)[:,None]*np.cos(theta),
            np.asarray(r)[:,None]*np.sin(theta)),axis=-1)
        z=np.full(xy.shape[:-1],self.cap_height);labels=np.ones(z.shape,dtype=np.uint8)
        for row in self.marker_rows(upper):
            u=np.sum((xy-row["center"])**2,axis=-1)/row["radius"]**2
            z+=row["height"]*np.maximum(0,1-u)**4;labels[u<1]=2
        if not upper:z*=-1
        return np.dstack([xy,z]),labels
    def cap_normals(self,xyz,upper=True):
        np=self.np;gradient=np.zeros_like(xyz[...,:2])
        for row in self.marker_rows(upper):
            d=xyz[...,:2]-row["center"];u=np.sum(d*d,axis=-1)/row["radius"]**2
            gradient-=8*row["height"]/row["radius"]**2*d*np.maximum(0,1-u)[...,None]**3
        n=np.concatenate([-gradient,np.full(gradient.shape[:-1]+(1,),1. if upper else -1.)],axis=-1)
        return n/np.linalg.norm(n,axis=-1)[...,None]
    def phase_jets(self,kind,coordinate,theta,alpha,height=None):
        np=self.np
        if kind=="prefix":jets,residual,_=self.prefix_jets(coordinate,np.asarray(theta)-alpha,height)
        elif kind in ("tail","collar"):jets,residual=self.tail_jets(coordinate,np.asarray(theta)-alpha),0.
        else:raise ValueError("Fixed caps do not receive the active rotation")
        co,si=np.cos(alpha),np.sin(alpha);R=np.array([[co,-si,0.],[si,co,0.],[0.,0.,1.]])
        return {k:v@R.T for k,v in jets.items()},residual

def checked_plan(path,expected,saved,tail):
    p=read(path,expected)
    if p.get("schema")!=PLAN_SCHEMA or p.get("checkpoint_sha256")!=saved.checkpoint.receipt["sha256"]:
        raise ValueError("A new explicit plan for this true450 field is required")
    for key in ("cuff","cut_correction_width","cap_height"):
        if type(p.get(key)) not in (int,float) or not math.isfinite(p[key]):
            raise ValueError("Supply explicit finite binary64 construction parameters")
    cuff,width=exact(p["cuff"]),exact(p["cut_correction_width"])
    inner,cut=exact(tail.r[0]),exact(tail.r[-1])
    if not 0<cuff<inner<cut-width<cut:raise ValueError("Complete positive radial construction layout is unpaid")
    markers=p["fixed_cap"]["markers"]
    if not isinstance(markers,list):raise ValueError("Retain the entire explicit cap marker list")
    for row in markers:
        raw_center=row.get("center")
        if (not isinstance(raw_center,list) or len(raw_center)!=2 or
                any(type(v) not in (int,float) or not math.isfinite(v)
                    for v in raw_center+[row.get("radius"),row.get("height")])):
            raise ValueError("Use explicit finite binary64 cap parameters, not implicit string projections")
        center=list(map(exact,raw_center));radius=exact(row["radius"]);height=exact(row["height"])
        if len(center)!=2 or type(row["upper"]) is not bool or radius<=0:
            raise ValueError("Each actual cap bump must have its full side, center, positive radius and height")
        if not sum(x*x for x in center)<(cuff-radius)**2 or radius>=cuff:
            raise ValueError("Every fixed marker support must be strictly inside its cuff disk")
    return p

def prepare(args):
    """Standalone/API scientific entry; preserve external-stop partial state."""
    actions();handlers={}
    def interrupted(number,frame):
        raise ExternalStop(number)
    try:
        for sig in (signal.SIGTERM,signal.SIGINT):
            handlers[sig]=signal.signal(sig,interrupted)
        return _prepare(args)
    finally:
        for sig,handler in handlers.items():signal.signal(sig,handler)

def _prepare(args):
    actions();start=time.monotonic();out=Path(args.out).resolve()
    temp=Path(os.environ["RUNNER_TEMP"]).resolve()
    if out.exists() or not out.is_relative_to(temp) or out==temp:raise ValueError("Fresh owned temporary output required")
    out.mkdir(parents=True);(out/"coefficients").mkdir()
    budget=Budget(out,args.budget_seconds,args.free_bytes_reserve,start)
    np,Saved,Background,Parity,sources=runtime(args.computations)
    saved=Saved.ContinuousTenSavedPrefix(args.checkpoint_directory,args.checkpoint_sha256,args.computations)
    replay=CurrentRadialReadout(args.radial_directory,args.radial_result_sha256,saved.checkpoint,np)
    plan=checked_plan(args.plan,args.plan_sha256,saved,replay)
    normalization=normalize_inlet(saved,np,Parity)
    records=[];row_ledger=out/"node-coefficient-identities.jsonl";current=0
    try:
        for current in range(len(replay.rows)):
            budget.check();a=replay.defining_node_coefficients(current);raw=a.tobytes(order="C")
            p=out/"coefficients"/("node-"+str(current).zfill(6)+".c128le")
            with p.open("xb") as f:f.write(raw);f.flush();os.fsync(f.fileno())
            d=receipt(p,out);d.update(index=current,shape=list(a.shape),dtype="<c16",order="C",completed=True)
            records.append(d)
            with row_ledger.open("ab") as f:f.write(canonical(d));f.flush();os.fsync(f.fileno())
        radial=dict(schema=SCHEMA+"-radial-definition",angular=2048,rows=replay.rows,
            coefficient_records=records,current_target_identity=copy.deepcopy(saved.checkpoint.target_identity),
            original_radial_result=receipt(Path(args.radial_directory)/"result.json"),
            original_complete_readout=receipt(replay.complete_path),
            coefficient_definition="Complete binary64 FFT of disclosed new node012 values; exact real Hermite thereafter",
            mean_and_Nyquist_modes_retained=True,all_576_stages_and_all_original_RK_step_endpoints=True,
            horizontal_second_node_source="Original nonuniform derivative-of-sampled-first-jet rule, newly evaluated in binary64",
            horizontal_second_node_values_are_not_certified_exact_derivatives_of_old_point_readout=True,
            actual_radial_ODE_trajectory_to_exact_Hermite_error_certified=False)
        tail=CurrentRadialTail(out,radial,np,Background)
        M=saved.M;core=list(map(exact,saved.core))
        state=list(map(exact,saved.quintic.nodal[0][-1,2*M+1:]))
        mean=state[0]+sum((Q(1-4*m*m,2)*core[m-1]*state[m] for m in range(1,M+1)),Q(0))
        tail_mean=exact(tail.node_coefficients(len(tail.r)-1)[0,0,2].real)
        sigma=Q(-1);offset=mean-sigma*tail_mean
        bgcut=exact(replay.rows[-1]["backgroundRKInnerAnchor"])
        radii=[exact(plan["cuff"])]+list(map(exact,tail.r))
        nodal=[(exact(plan["cap_height"]),Q(0),Q(0))]
        for row in replay.rows:
            g=row["geometry"];bg=exact(row["backgroundRKInnerAnchor"])
            nodal.append((offset-sigma*(bgcut-bg),sigma*exact(g["w"]),sigma*exact(g["wr"])))
        budget.check();B=Background.SharedBackground(radii,nodal);encoded=B.encode();budget.check()
        a,ap,app=map(float,saved.profile(saved.flow.end))
        if exact(a)!=saved.checkpoint.owner.data["cut"]:
            # This reports a construction-coordinate discrepancy; it never
            # accepts the BVP or replaces its exact target cut by this value.
            radius_gap=dict(profile_radius=a,actual_tail_cut=float(tail.r[-1]),word_equal=word(a)==word(tail.r[-1]))
        else:radius_gap=dict(profile_radius=a,actual_tail_cut=float(tail.r[-1]),word_equal=True)
        newplan=copy.deepcopy(plan)
        newplan.update(schema=SCHEMA+"-plan",finished=True,tail_inner=float(tail.r[0]),cut=float(tail.r[-1]),
            prefix_end=saved.flow.end,background_radii=[float(v) for v in radii],
            declared_cut_radial_chart_jets=[float(tail.r[-1]),ap,app],
            declared_chart_is_not_proof_of_numeric_scalar_derivative_identity=True,
            phase_rule="For all real alpha, moving F_alpha(s,theta)=R_alpha F_0(s,theta-alpha); fixed caps are unchanged. alpha=pi*t/2 on t in [0,1].")
        target=dict(schema=SCHEMA+"-target-contract",complete_current_ten_target=copy.deepcopy(saved.checkpoint.target_identity),
            prefix_target="(L_true/L_numeric)^2 ds_numeric^2 + a_true(L_true*s_numeric/L_numeric;p10)^2 dtheta^2",
            tail_target="Original same model-C E(r) dr^2+r^2 dtheta^2, with complete validated radial coverage required",
            cap_target="Induced metric of each fixed cap, hence relative metric error zero on the cap itself",
            geometric_Bprime_is_not_the_target_slope=True,
            geometric_B_does_not_select_a_common_accurate_C_root=True,
            actual_continuous_target_atlas_and_full_radial_coverage_unpaid=True)
        target_path=out/"target-contract.json";write(target_path,target)
        geometry=dict(schema=SCHEMA,producer_source=receipt(__file__),
            original_complete_prefix_definition_sha256=sha(canonical(saved.definition)),
            exact_background_payload_sha256=Background.canonical_sha(encoded),
            original_target_metric_background_sha256=receipt(target_path)["sha256"],
            target_contract=receipt(target_path),
            actual_450_checkpoint=copy.deepcopy(saved.checkpoint.receipt),
            current_target_identity=copy.deepcopy(saved.checkpoint.target_identity),
            full_radial_replay=receipt(Path(args.radial_directory)/"result.json"),
            full_radial_node_identity_ledger=receipt(row_ledger),
            target_metric_not_replaced_by_Bprime=True,
            exact_field_definition_independent_of_rounded_renderer=True,
            new_actual_nonlinear_acceptance=False,geometric_acceptance=False)
        A=CurrentSharedAssembly(saved,tail,newplan,B,geometry,np,Background)
        geometry["recorded_single_global_planar_registration"]=copy.deepcopy(saved.registration)
        newplan["shared_background_geometry"]=copy.deepcopy(geometry)
        guard=dict(schema=SCHEMA,required_geometry_loader=LOADER_NAME,
            producer_source_sha256=receipt(__file__)["sha256"],
            exact_background_payload_sha256=geometry["exact_background_payload_sha256"],
            actual_450_checkpoint_sha256=saved.checkpoint.receipt["sha256"],
            legacy_tail_or_B_reconstruction_authorized=False,identity_annotation_only=True)
        definition=copy.deepcopy(saved.definition);definition[GUARD_KEY]=guard
        newplan["large_core_prefix"]=definition
        assembly=dict(schema=SCHEMA+"-assembly",finished=True,
            shared_background_geometry=copy.deepcopy(geometry),large_core_prefix=definition,
            mean_gauge=dict(whole_lower_sheet_reflected=True,
                original_z0_and_both_native_mean_channels_retained=True,
                exact_prefix_cut_material_mean=str(mean),exact_tail_zero_mode=str(tail_mean),
                exact_upper_background_cut_offset=str(offset)),
            core_and_hold_gauge=dict(native_cap_rotation_axis_xy=[0.,0.],
                same_original_R248_phase_family=True,held_distance_not_certified=True),
            single_global_planar_registration=copy.deepcopy(saved.registration),
            inlet_normalization=normalization,
            exact_closed_seam_construction=dict(inlet_R249_projection=True,
                complete_outer_correction_reformed_against_own_B=True,
                collar_zero_twojet_and_full_inner_node=True,
                fixed_cap_flat_cuff_twojet=True,
                same_material_Phi_and_complete_core112=True,
                regularity_injectivity_target_atlas_metric_reach_held_unpaid=True),
            cut_coordinate_word_diagnostic=radius_gap,
            all_native_angular_modes_including_zero_and_Nyquist=True,
            continuous_envelopes_inherited=False,actual_BVP_reaccepted=False,
            display_mesh_generated=False,all_phase_pair_coverage_generated=False,
            geometric_acceptance=False,task_completed=False)
        background=dict(schema=SCHEMA+"-background",finished=True,
            exact_background=encoded,exact_background_payload_sha256=geometry["exact_background_payload_sha256"],
            exact_background_definition="Unique exact shared-node Hermite B from full current RK-background means and current w/wr words, plus explicit flat cap datum",
            exact_RK_background_words_not_an_exact_continuous_C_primitive=True,
            native_small_mean_is_separate_in_full_Fourier_U=True,
            source_RK_background_mean_at_cut=str(bgcut),
            explicit_new_cap_datum=str(exact(plan["cap_height"])),
            old_frozen_background_or_old_ready_primitive_used=False,
            all_current_radial_nodes_retained=True,
            target_contract=copy.deepcopy(target),shared_background_geometry=copy.deepcopy(geometry))
        payloads={}
        for key,name,data in (("radial","radial-definition.json",radial),("plan","plan.json",newplan),
            ("assembly","assembly.json",assembly),("background","shared-background.json",background)):
            p=out/name;write(p,data);payloads[key]=receipt(p,out)
        payloads["target"]=receipt(target_path,out)
        result=dict(schema=SCHEMA,completed=True,source=receipt(__file__),sources=sources,
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            checkpoint=copy.deepcopy(saved.checkpoint.receipt),checkpoint_directory=str(Path(args.checkpoint_directory).resolve()),
            radial_replay=receipt(Path(args.radial_directory)/"result.json"),
            plan_input=receipt(args.plan),payloads=payloads,
            current_target_identity=copy.deepcopy(saved.checkpoint.target_identity),
            complete_prefix_definition_sha256=sha(canonical(saved.definition)),
            normal_form_prefix_definition_sha256=sha(canonical(definition)),
            node_count=len(tail.r),angular=tail.N,coefficient_count=len(records),
            background_nodes=len(B.radii),all_shape_mean_Nyquist_and_full_twojets_retained=True,
            real_shared_node_Hermite_geometry_defined=True,
            finite_native_replay_not_certified_exact_continuous_C_trajectory=True,
            target_metric_error_or_curvature_or_reach_or_embedding_or_held_certified=False,
            display_mesh_or_complete_pair_enumeration_generated=False,
            original_BVP_acceptance_replaced=False,
            resource_partial=False,error=None,pending=[],elapsed_seconds=time.monotonic()-start)
        write(out/"result.json",result)
        print(json.dumps(dict(event="current-C-ten450-shared-field-defined",result=receipt(out/"result.json"),
            nodes=len(tail.r),angular=tail.N,background_nodes=len(B.radii),
            exact_finite_field_defined=True,full_geometry_accepted=False)),flush=True)
        return result
    except BaseException as exc:
        result=dict(schema=SCHEMA,completed=False,source=receipt(__file__),sources=sources,
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            checkpoint=copy.deepcopy(saved.checkpoint.receipt),coefficient_records_completed=len(records),
            node_identity_ledger=receipt(row_ledger) if row_ledger.exists() else None,
            pending=dict(current_node=current,total_nodes=len(replay.rows),
                uncommitted_coefficient_suffix=[len(records),len(replay.rows)],
                shared_background_full_closed_expression_and_all_envelopes_unpaid=True),
            resource_partial=isinstance(exc,ResourceStop),
            external_interruption=isinstance(exc,ExternalStop),
            error=dict(type=type(exc).__name__,message=str(exc)),elapsed_seconds=time.monotonic()-start)
        write(out/"result.json",result)
        print(json.dumps(dict(event="current-C-ten450-shared-field-partial",result=receipt(out/"result.json"),
            resource_partial=result["resource_partial"],error=result["error"])),flush=True)
        return result

def load_shared_bundle(args):
    """Seven-member exact-expression API; no fabricated mesh/sample evidence."""
    actions();np,Saved,Background,Parity,sources=runtime(args.computations)
    root=Path(args.directory);result=read(root/"result.json",args.result_sha256)
    if (result.get("schema")!=SCHEMA or result.get("completed") is not True
            or result.get("source",{}).get("sha256")!=receipt(__file__)["sha256"]
            or result.get("sources")!=sources):
        raise ValueError("Use a complete independently typed current-ten shared field")
    checkpoint_directory=getattr(args,"checkpoint_directory",None) or result["checkpoint_directory"]
    saved=Saved.ContinuousTenSavedPrefix(checkpoint_directory,result["checkpoint"]["sha256"],args.computations)
    normalize_inlet(saved,np,Parity)
    if (saved.checkpoint.receipt!=result["checkpoint"] or
            saved.checkpoint.target_identity!=result["current_target_identity"] or
            sha(canonical(saved.definition))!=result["complete_prefix_definition_sha256"]):
        raise ValueError("The complete current-ten prefix/normal form differs")
    paths={key:member(root,d) for key,d in result["payloads"].items()}
    plan,assembly,background,radial,target=(read(paths[k]) for k in ("plan","assembly","background","radial","target"))
    if (plan.get("schema")!=SCHEMA+"-plan" or plan.get("finished") is not True
            or assembly.get("schema")!=SCHEMA+"-assembly" or assembly.get("finished") is not True
            or background.get("schema")!=SCHEMA+"-background" or background.get("finished") is not True
            or radial.get("schema")!=SCHEMA+"-radial-definition"
            or target.get("schema")!=SCHEMA+"-target-contract"
            or radial.get("current_target_identity")!=saved.checkpoint.target_identity
            or radial.get("original_radial_result")!=result["radial_replay"]
            or len(radial.get("rows",[]))!=result["node_count"]
            or len(radial.get("coefficient_records",[]))!=result["coefficient_count"]):
        raise ValueError("Keep every independently typed component and the complete radial node layout")
    geometry=plan["shared_background_geometry"]
    if (geometry.get("actual_450_checkpoint")!=saved.checkpoint.receipt
            or geometry.get("current_target_identity")!=saved.checkpoint.target_identity
            or geometry.get("full_radial_replay")!=result["radial_replay"]
            or background.get("target_contract")!=target
            or assembly["shared_background_geometry"]!=geometry or background["shared_background_geometry"]!=geometry
            or target["complete_current_ten_target"]!=saved.checkpoint.target_identity
            or receipt(paths["target"])!=geometry["target_contract"]
            or geometry["producer_source"]["sha256"]!=receipt(__file__)["sha256"]):
        raise ValueError("Keep the same target and background on every actual field")
    encoded=background["exact_background"]
    if Background.canonical_sha(encoded)!=geometry["exact_background_payload_sha256"]:
        raise ValueError("The full exact shared-background payload differs")
    B=Background.SharedBackground(
        [Background.qread(r["radius"]) for r in encoded["nodes"]],
        [[Background.qread(v) for v in r["jets"]] for r in encoded["nodes"]])
    if B.encode()!=encoded:raise ValueError("The same exact nodal background coefficients differ")
    tail=CurrentRadialTail(root,radial,np,Background)
    A=CurrentSharedAssembly(saved,tail,plan,B,geometry,np,Background,
        registration=assembly["single_global_planar_registration"])
    expected=copy.deepcopy(saved.definition);expected[GUARD_KEY]=copy.deepcopy(plan["large_core_prefix"][GUARD_KEY])
    if (plan["large_core_prefix"]!=expected or assembly["large_core_prefix"]!=expected
            or expected[GUARD_KEY].get("required_geometry_loader")!=LOADER_NAME
            or sha(canonical(expected))!=result["normal_form_prefix_definition_sha256"]):
        raise ValueError("The explicit new loader guard or same-field prefix differs")
    bindings=dict(schema=SCHEMA+"-binding",source=receipt(__file__),sources=sources,
        complete_current_target_identity=copy.deepcopy(saved.checkpoint.target_identity),
        actual_450_checkpoint=saved.checkpoint.receipt,
        complete_prefix_definition=expected,shared_background_geometry=geometry,
        closed_expression_files={k:receipt(v) for k,v in paths.items()},
        no_legacy_scalar_tail_or_background_loader_called=True,
        actual_display_mesh_and_normals_not_supplied=True,
        complete_pair_or_curvature_or_metric_or_held_bounds_not_inherited=True,
        same_new_loader_required_for_every_exact_geometry_consumer=True,
        geometric_acceptance_created=False)
    return paths,plan,assembly,target,saved,A,bindings

def exact_field(args):
    """Pure675 six-jet interpreter, now bound to the new complete seven-tuple."""
    bundle=load_shared_bundle(args)
    np,Saved,Background,Parity,sources=runtime(args.computations)
    Active=load(args.computations,ACTIVE_NAME,ACTIVE_SHA,"_current_ten_full_exact_jet")
    from flint import arb,ctx,fmpq
    Active.np,Active.arb,Active.ctx,Active.fmpq=np,arb,ctx,fmpq
    # No old initialise_runtime / stored-tail / geometric loader is invoked.
    field=Active.ExactFiniteField(bundle,Background)
    return bundle,field,Active,Background

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action",choices=("prepare","describe"))
    parser.add_argument("--computations",type=Path,default=HERE)
    parser.add_argument("--checkpoint-directory",type=Path)
    parser.add_argument("--checkpoint-sha256")
    parser.add_argument("--radial-directory",type=Path)
    parser.add_argument("--radial-result-sha256")
    parser.add_argument("--plan",type=Path)
    parser.add_argument("--plan-sha256")
    parser.add_argument("--budget-seconds",type=float)
    parser.add_argument("--free-bytes-reserve",type=int)
    parser.add_argument("--out",type=Path)
    parser.add_argument("--directory",type=Path)
    parser.add_argument("--result-sha256")
    args=parser.parse_args(argv);actions()
    if args.action=="prepare":
        for name in ("checkpoint_directory","checkpoint_sha256","radial_directory","radial_result_sha256",
                     "plan","plan_sha256","budget_seconds","free_bytes_reserve","out"):
            if getattr(args,name) is None:parser.error("Explicit --"+name.replace("_","-")+" required")
        try:
            return 0 if prepare(args)["completed"] else 2
        except BaseException as exc:
            # Binding/setup failures are a wholly unpaid construction; retain
            # them instead of leaving an absent result looking like zero work.
            if args.out.exists() and not (args.out/"result.json").exists():
                failure=dict(schema=SCHEMA,completed=False,source=receipt(__file__),
                    run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
                    phase="binding-or-setup",error=dict(type=type(exc).__name__,message=str(exc)),
                    checkpoint_sha256=args.checkpoint_sha256,radial_result_sha256=args.radial_result_sha256,
                    plan_sha256=args.plan_sha256,resource_partial=isinstance(exc,ResourceStop),
                    external_interruption=isinstance(exc,ExternalStop),
                    pending=dict(entire_new_radial_Hermite_background_and_closed_expression=True))
                write(args.out/"result.json",failure)
                print(json.dumps(dict(event="current-C-field-setup-failure",result=receipt(args.out/"result.json"),
                    error=failure["error"])),flush=True)
            raise
    if args.directory is None or args.result_sha256 is None:parser.error("--directory and --result-sha256 required")
    bundle=load_shared_bundle(args)
    binding_raw=canonical(bundle[-1])
    print(json.dumps(dict(schema=SCHEMA+"-description",
        complete_binding_identity=dict(canonical_bytes=len(binding_raw),canonical_sha256=sha(binding_raw)),
        actual_checkpoint=bundle[-1]["actual_450_checkpoint"],
        source=receipt(__file__),source_count=len(bundle[-1]["sources"]),
        radial_nodes=len(bundle[-2].tail.r),angular=bundle[-2].tail.N,
        exact_finite_geometry_defined=True,actual_complete_surface_accepted=False,
        complete_binding_available_only_through_same_field_API=True)),flush=True)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
