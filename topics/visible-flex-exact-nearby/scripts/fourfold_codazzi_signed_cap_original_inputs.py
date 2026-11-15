#!/usr/bin/env python3
"""Read exact old cap trials and scalar jets for the new SC functional.

No original target, QR, physical coefficient model, residual or Gram producer
is called.  Candidate offsets are replayed from their original exact definition
and checked against the already published full sequence hash.
"""
from __future__ import annotations

import ast
import gzip
import io
import hashlib
import json
import math
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import arb, arb_mat

from fourfold_codazzi_signed_cap_radial_moments import (
    rat,saved_interval,inflate,trig,centered_fields)

CURRENT = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
OBJECT = "df9844506e25bdd207472fd8f5f7e9fbfaf90514c2e1a3629be2e5594eb25ca0"
PLAN = "93e9b52054d9af86b9f238fb13a4183ec23b90f2e0017676aef4773fa28dce32"
PLAN_SOURCE = "6b3a47a54386171b2c659c776bbfeff52ae0ebe4456ced5b67350f7eabf48a8d"
LEFT,RIGHT = Fraction(9,10),Fraction(25,8)
PILOTS = (0,64,4096,7907)
SCALARS = ("s","K","gamma","beta")
EXPECTED_REQUESTS = ((0,4,0),(16,4,0),(1024,4,0),(1976,4,3))


def digest(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda:stream.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def canonical(doc):
    return hashlib.sha256((json.dumps(doc,sort_keys=True,separators=(",",":"))+"\n").encode()).hexdigest()


def read(path):
    path=Path(path)
    raw=path.read_bytes()
    if path.name.endswith(".gz"):
        raw=gzip.decompress(raw)
    return json.loads(raw)


def raw_array_sha(value):
    return hashlib.sha256(np.asarray(value,dtype="<f8").tobytes(order="C")).hexdigest()


def relative(value):
    path=Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("an original input path escapes its exact bundle")
    return path


def complete(d):
    return (d.get("complete") is True and d.get("failure") is None
            and bool(d.get("gates")) and all(g.get("passed") is True for g in d["gates"]))


def original_plan(path):
    if digest(path)!=PLAN:
        raise ValueError("the original complete7908 plan bytes changed")
    p=read(path)
    if (not complete(p) or p.get("phase")!="plan"
            or p.get("source_sha256")!=PLAN_SOURCE
            or p.get("object_identity_sha256")!=OBJECT
            or p.get("completed_bundles")!=32 or len(p.get("bundles",[]))!=32
            or len(p.get("complete_quarter_origin_records",[]))!=7908):
        raise ValueError("the same exact32 bundle plan and complete origin table are required")
    cursor=LEFT
    for i,r in enumerate(p["complete_quarter_origin_records"]):
        l,h=map(Fraction,r["interval"])
        if r["index"]!=i or tuple(r["request"])!=(i//4,4,i%4) or l!=cursor or not l<h:
            raise ValueError("the original full7908 physical cover has a gap")
        cursor=h
    if cursor!=RIGHT:
        raise ValueError("the old scalar partition does not end at the true cap endpoint")
    return p


def pilot_rows(paths,plan):
    """Only the three original non-reused ranges, no old64 pilot substitution."""
    rows={}
    for item in paths:
        path=Path(item["path"])
        if digest(path)!=item["sha256"]:
            raise ValueError("one original successful range native changed")
        d=read(path)
        if not complete(d):
            raise ValueError("an original complete scalar range is not successful")
        for row in d.get("rows",[]):
            request=tuple(row.get("request",()))
            if request not in EXPECTED_REQUESTS:
                continue
            i=request[0]*4+request[2]
            origin=plan["complete_quarter_origin_records"][i]
            if (i in rows or canonical(row)!=origin["original_row_sha256"]
                    or row["interval"]!=origin["interval"]
                    or not row.get("intrinsic_midpoint_jets")):
                raise ValueError("one pilot lost its complete exact original midpoint or identity")
            rows[i]=row
    if sorted(rows)!=list(PILOTS):
        raise ValueError("all four original omitted pilot scalar rows are required")
    return rows


def original_slice(folder,group,plan,pilots):
    folder=Path(folder)
    desc=plan["bundles"][group]
    if desc["group"]!=group:
        raise ValueError("the original exact slice group changed")
    ip=folder/"bundle-index.json"
    if digest(ip)!=desc["bundle_index"]["sha256"]:
        raise ValueError("the original exact slice index changed")
    d=read(ip)
    if (d.get("group")!=group or d.get("range")!=desc["range"]
            or d.get("object_identity_sha256")!=OBJECT
            or not d.get("all_node_values_and_derivatives_are_literal_original_binary64_slices")):
        raise ValueError("this is not the same exact physical Hermite trial")
    for item in d["exact_source_files"]:
        path=folder/relative(item["file"])
        if path.stat().st_size!=item["bytes"] or digest(path)!=item["sha256"]:
            raise ValueError("an exact original slice member changed")
    old=read(folder/"exact-original-quarters.json.gz")
    start,end=desc["range"]
    indices=[i for i in range(start,end) if i not in PILOTS]
    if old["indices"]!=indices or d["indices"]!=indices or len(old["rows"])!=len(indices):
        raise ValueError("one complete original non-pilot quarter is missing or duplicated")
    if [canonical(r) for r in old["rows"]]!=d["original_quarter_row_sha256"]:
        raise ValueError("an original complete scalar row changed")
    table=dict(zip(indices,old["rows"]))
    table.update({i:r for i,r in pilots.items() if start<=i<end})
    if sorted(table)!=list(range(start,end)):
        raise ValueError("the new signed functional must include every original quarter")
    for i,row in table.items():
        original=plan["complete_quarter_origin_records"][i]
        if (canonical(row)!=original["original_row_sha256"]
                or row["request"]!=original["request"] or row["interval"]!=original["interval"]):
            raise ValueError("one complete original quarter has another exact origin")
    arrays={}
    with np.load(folder/"exact-original-Hermite-slice.npz",allow_pickle=False) as z:
        for name,receipt in d["exact_selected_array_receipts"].items():
            value=np.asarray(z[name],dtype="<f8")
            if list(value.shape)!=receipt["shape"] or raw_array_sha(value)!=receipt["raw_binary64_sha256"]:
                raise ValueError("an exact original physical trial array changed")
            arrays[name]=value
    if set(arrays)!={"nodes","state","derivative_left","derivative_right"}:
        raise ValueError("all four original arrays are required")
    nodes=list(map(Fraction.from_float,map(float,arrays["nodes"])))
    n=len(nodes)
    if (arrays["state"].shape!=(n,257,97)
            or arrays["derivative_left"].shape!=(n-1,257,97)
            or arrays["derivative_right"].shape!=(n-1,257,97)
            or not all(a<b for a,b in zip(nodes,nodes[1:]))):
        raise ValueError("the full original257 state97 input dimensions changed")
    l,h=map(Fraction,d["interval"])
    if not ((nodes[0]<=l or d["original_global_first_node"]==0 and LEFT<=l<nodes[0])
            and h<=nodes[-1]):
        raise ValueError("the true full scalar slice is not covered by its same Hermite trial")
    return d,table,nodes,arrays



def original_definitions():
    """Compile only the unchanged pure old readers, never their producer main.

    Exact source SHA binds each AST definition.  This avoids importing the old
    target/coefficient/Gram dependency graph merely to replay literal data.
    """
    specifications = (
        ("fourfold_codazzi_candidate_shards.py",
         "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
         ("digest","load_candidate")),
        ("fourfold_codazzi_final_continuous_value_repair.py",
         "51a3f7968991ed85211b74c23befae7021bb192796daf0ae2d12ec5a1d45329b",
         ("fraction","iter_repair")))
    output=[]
    for filename,expected,names in specifications:
        path=Path(__file__).with_name(filename)
        if digest(path)!=expected:
            raise ValueError("one immutable exact-data definition source changed")
        parsed=ast.parse(path.read_text(),filename=str(path))
        chosen=[n for n in parsed.body if isinstance(n,ast.FunctionDef) and n.name in names]
        if [n.name for n in chosen]!=list(names):
            raise ValueError("the complete original pure definitions are missing")
        namespace=dict(np=np,io=io,gzip=gzip,json=json,Path=Path,
                       sha256=hashlib.sha256,Fraction=Fraction)
        module=ast.Module(body=chosen,type_ignores=[])
        exec(compile(module,str(path),"exec"),namespace)
        output.append(namespace[names[-1]])
    return tuple(output)


class ExactCandidate:
    def __init__(self,index,repair,wanted_pieces=None):
        index,repair=Path(index),Path(repair)
        if digest(index)!=CURRENT:
            raise ValueError("the exact original ac1 candidate changed")
        if index.suffix!=".json":
            raise ValueError("only the original complete sharded JSON candidate is admitted")
        load_candidate,iter_repair=original_definitions()
        self.saved=load_candidate(index)
        meta=json.loads(str(self.saved["metadata"]))
        self.alpha=Fraction(meta["exact_float_amplitude"])
        self.knots=list(map(Fraction.from_float,map(float,self.saved["radial_nodes"])))
        if int(meta["modes"])!=32 or self.saved["piece_coefficients"].shape!=(4,6144,65):
            raise ValueError("all original finite65 candidate slots are required")
        old=read(repair)
        if (not old.get("complete") or old.get("derived_definition_sha256")!=CENTRE
                or canonical(old["definition"])!=CENTRE):
            raise ValueError("the exact published continuous centre definition changed")
        h=hashlib.sha256()
        self.offsets={}
        wanted=None if wanted_pieces is None else set(wanted_pieces)
        count=0
        for piece,offset,_ in iter_repair(self.saved,self.alpha):
            h.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,offset))),
                       sort_keys=True,separators=(",",":"))+"\n").encode())
            if wanted is None or piece in wanted:
                self.offsets[piece]=list(map(Fraction,offset))
            count+=1
        if count!=6144 or h.hexdigest()!=old["definition"]["offset_sequence_sha256"]:
            raise ValueError("the original complete exact repair offset sequence changed")
        self.repair_sequence_sha256=h.hexdigest()

    def piece(self,left,right):
        left,right=Fraction(left),Fraction(right)
        p=bisect_right(self.knots,left)-1
        if not (0<=p<6144 and self.knots[p]<=left<right<=self.knots[p+1]):
            raise ValueError("SC18a: the complete old scalar row crosses a candidate piece")
        if p not in self.offsets:
            raise ValueError("the exact original offset for this whole piece was not restored")
        return p

    def polynomial_jets(self,piece,x):
        delta=x-rat(self.knots[piece])
        cube=self.saved["piece_coefficients"][:,piece]
        jets=[]
        alpha=rat(self.alpha)
        for k in range(4):
            row=[]
            for slot in range(65):
                value=arb(0)
                for j in range(4-k):
                    power=3-j
                    value += rat(float(cube[j,slot]))*(math.factorial(power)//math.factorial(power-k)) \
                        *delta**(power-k)
                value*=alpha
                if k==0:
                    value+=rat(self.offsets[piece][slot])
                row.append(value)
            jets.append(row)
        u=[trig(row[:32],[]) for row in jets]
        eta=[trig([],row[32:]) for row in jets]
        return u,eta

    def row_fields(self,row):
        left,right=map(Fraction,row["interval"])
        germ=tuple(map(Fraction,row["actual_scalar_germ"]))
        if not germ[0]<=left<right<=germ[1]:
            raise ValueError("an old complete scalar row escaped its original germ")
        piece=self.piece(left,right)
        center=(left+right)/2
        whole_x=rat(left).union(rat(right))
        mid_u,mid_eta=self.polynomial_jets(piece,rat(center))
        all_u,all_eta=self.polynomial_jets(piece,whole_x)
        mid={};whole={}
        for name in SCALARS:
            mid[name]=[saved_interval(row["intrinsic_midpoint_jets"][name+(str(k) if k else "")])
                       for k in range(4)]
            whole[name]=[saved_interval(row["all_original_target_coefficients"][name+(str(k) if k else "")])
                         for k in range(4)]
        return dict(piece=piece,left=left,right=right,center=center,
                    scalar_mid=mid,scalar_whole=whole,
                    mid=centered_fields(mid_u,mid_eta,mid["s"],mid["K"]),
                    whole=centered_fields(all_u,all_eta,whole["s"],whole["K"]))


def exact_matrix(values):
    return arb_mat([[rat(float(x)) for x in row] for row in values])


def hermite_at_center(nodes,arrays,left,right,center):
    """Same exact original cubic, including the first true9/10 short extension."""
    left,right,center=map(Fraction,(left,right,center))
    piece=bisect_right(nodes,left)-1
    if piece<0 and LEFT<=left<nodes[0]:
        piece=0
    if not (0<=piece<len(nodes)-1
            and (nodes[piece]<=left or piece==0 and LEFT<=left<nodes[0])
            and left<right<=nodes[piece+1]):
        raise ValueError("the requested interval crosses an actual Hermite join")
    a,b=nodes[piece:piece+2]
    h=rat(b-a);x=rat((center-a)/(b-a))
    Y0,Y1=map(exact_matrix,(arrays["state"][piece],arrays["state"][piece+1]))
    D0,D1=map(exact_matrix,(arrays["derivative_left"][piece],arrays["derivative_right"][piece]))
    V1=D0*h
    V2=(Y1-Y0)*3-(D0*2+D1)*h
    V3=(Y0-Y1)*2+(D0+D1)*h
    coefficients=[Y0+V1*x+V2*x*x+V3*x*x*x,
                  (V1+V2*(2*x)+V3*(3*x*x))*(1/h),
                  (V2+V3*(3*x))*(1/(h*h)),
                  V3*(1/(h*h*h))]
    return coefficients,piece
