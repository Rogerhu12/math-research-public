#!/usr/bin/env python3
"""R797: complete r=2,q0=0,b=b0=3 original source gate.
Imports the published R788 exact arithmetic routines, not its five-profile
or geometry conclusions. All mathematical execution is for public Actions.
No generated data files are written.
"""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys

sys.dont_write_bytecode = True
sys.set_int_max_str_digits(200000)
_base_path = Path(__file__).with_name("check-r788-original-b3-contact-all-primes.py")
_spec = importlib.util.spec_from_file_location("r788_exact_arithmetic", _base_path)
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)

ceildiv = base.ceildiv
primes_to = base.primes_to
mul = base.mul
power = base.power
pad = base.pad
partitions = base.partitions
cumul = base.cumul


def digest(value):
    if not isinstance(value, str):
        value = json.dumps(value, separators=(",", ":"), sort_keys=True)
    return hashlib.sha256(value.encode()).hexdigest()


def original_profiles():
    """A=(t-1)^i d^j h7^k, deg A <= 6-3z.
    These are necessary envelopes, not freely added old-source columns.
    z is the exact degree of H in F(t,0)=lambda*d^c*H.
    """
    out = {}
    counts = {}
    for z in range(3):
        cap = 6-3*z
        count = 0
        for i in range(cap+1):
            for j in range(cap-i+1):
                for kh in range((cap-i-j)//2+1):
                    a = i+j+2*kh
                    mh = min(3, (4*kh+1)//3)
                    m1 = min(3, i)
                    dd = (2*j+1)//3
                    di = (13-2*a)//3
                    assert di >= 2*z and dd >= 0
                    key = (z,mh,m1,dd,di)
                    mask = [i,j,kh]
                    if key not in out:
                        out[key] = {
                            "z":z,"mh_max":mh,"m1_max":m1,
                            "delta_d_max":dd,"delta_inf_max":di,
                            "masks":[mask]}
                    else:
                        out[key]["masks"].append(mask)
                    count += 1
        counts[z] = count
    assert counts == {0:50,1:13,2:1}
    return list(out.values()), counts


def geometry_classes(profiles):
    """All nineteen-angle necessary classes, including H(0)=0.
    The two h7 chains coincide over F_p (p == 5 mod 6).
    Extra primitivity or exact-attainment tests are never assumed.
    """
    out = {}
    for prof in profiles:
        z = prof["z"]
        for mh in range(prof["mh_max"]+1):
            for m1 in range(prof["m1_max"]+1):
                for dd in range(prof["delta_d_max"]+1):
                    for di in range(2*z,prof["delta_inf_max"]+1):
                        for c in range((3+dd)//2+1):
                            vd = 2*c-dd
                            if not 0 <= vd <= 3:
                                continue
                            for v in range(z,(3+di)//2+1):
                                vi = 2*v-di
                                if not 0 <= vi <= 3:
                                    continue
                                u = c+v
                                for mhv in partitions(3-mh,4):
                                    for m1v in partitions(3-m1,3):
                                        for mdv in partitions(vd,2):
                                            if mdv[0] > c:
                                                continue
                                            for miv in partitions(vi,2):
                                                if miv[0] > v-z:
                                                    continue
                                                vh,v1,vdt,vin = map(
                                                    cumul,(mhv,m1v,mdv,miv))
                                                # The whole f0=d^c*H, deg H=z,
                                                # is allowed at every chosen center.
                                                if any(j*c < a for j,a in enumerate(vdt,1)):
                                                    continue
                                                if any(j*(u-c-z) < a for j,a in enumerate(vin,1)):
                                                    continue
                                                kappa = (36+6*u
                                                  -2*sum(a*a for a in mhv)
                                                  -sum(a*a for a in m1v+mdv+miv))
                                                chi = 9+2*mh+m1+dd+di
                                                if kappa < chi-2 or (kappa-chi)%2:
                                                    continue
                                                specs = []
                                                for n in range(1,4):
                                                    bh=max([0]+[
                                                        ceildiv(a-3+n,j)
                                                        for j,a in enumerate(vh,1)])
                                                    ct=max([0]+[
                                                        ceildiv(a-3+n,j)
                                                        for j,a in enumerate(v1,1)])
                                                    zd=max([0]+[
                                                        ceildiv(a-n,j)
                                                        for j,a in enumerate(vdt,1)])
                                                    K=min([u+4*n]+[
                                                        (j*u+(4*j+1)*n-a)//j
                                                        for j,a in enumerate(vin,1)])
                                                    E=K-2*bh-ct-zd
                                                    specs.append((n,bh,ct,zd,E))
                                                key=(z,c,u,mhv,m1v,mdv,miv)
                                                out[key]={
                                                    "z":z,"c":c,"u":u,
                                                    "mu_h":mhv,"mu_1":m1v,
                                                    "mu_d":mdv,"mu_inf":miv,
                                                    "kappa":kappa,"chi":chi,
                                                    "specs":specs}
    classes=list(out.values())
    assert classes
    # Follows also directly from the displayed multiplicity bounds:
    # 2 sum(mu_h^2)+sum(mu_1^2)<=27 and each remaining contribution >=0.
    assert all(c["kappa"] >= 9+6*c["z"] for c in classes)
    return classes


def affine_report(rows,rhs,p,labels,values0,z):
    n=len(labels)
    A=[[v % p for v in row]+[b % p] for row,b in zip(rows,rhs)]
    r=0
    piv=[]
    for c in range(n):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[v*inv % p for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                a=A[i][c]
                A[i]=[(x-a*y) % p for x,y in zip(A[i],A[r])]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    consistent=all(any(row[:n]) or row[n] == 0 for row in A)
    report={"rank":r,"augmented_rank":r+int(not consistent),
            "consistent":consistent}
    if not consistent:
        return report
    x=[0]*n
    for i,c in enumerate(piv):
        x[c]=A[i][n]
    free=[c for c in range(n) if c not in piv]

    def possible(v,offset=0):
        if (offset+sum(a*b for a,b in zip(v,x))) % p:
            return True
        return any((v[f]-sum(v[c]*A[i][f]
                   for i,c in enumerate(piv))) % p for f in free)

    f3=[(values0[j] % p if lab==(3,0) else 0)
        for j,lab in enumerate(labels)]
    fy=[(lab[0]*values0[j] % p if lab[0]>0 and lab[1]==0 else 0)
        for j,lab in enumerate(labels)]
    td=-pow(8,-1,p) % p
    hd=[(pow(td,lab[1],p) if lab[0]==0 else 0) for lab in labels]
    flags=[possible(f3),possible(fy),possible(hd,pow(td,z,p))]
    # There are only three forbidden affine hyperplanes and p>101:
    # if each is proper their union cannot cover the solution space.
    report.update({
        "affine_dimension":len(free),
        "b0_three_possible":flags[0],
        "smooth_possible":flags[1],
        "H_coprime_d_possible":flags[2],
        "linear_open_nonempty":all(flags),
        "rref_sha256":digest(A)})
    return report


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--max-order",type=int,default=64)
    ap.add_argument("--remaining-examples",type=int,default=20)
    args=ap.parse_args()
    M=args.max_order
    if not 48 <= M <= 96:
        raise ValueError("Only the fixed b=3 certificate is authorized")
    if not 0 <= args.remaining_examples <= 40:
        raise ValueError("Bounded small remaining-class report only")
    cap=M+1
    trial_bound=12*M+11
    small=primes_to(trial_bound)
    theta=base.theta_powers(M)

    @lru_cache(None)
    def d_power(exp):
        if exp >= 0:
            return tuple(pad(power([1,8],exp,cap),cap))
        vals=[Q(1)]
        for k in range(1,cap):
            vals.append(vals[-1]*Q(8*(exp-k+1),k))
        assert all(v.denominator==1 for v in vals)
        return tuple(vals)

    @lru_cache(None)
    def source_series(n,bh,ct,dp):
        v=mul(power([7,4,16],bh,cap),power([-1,1],ct,cap),cap)
        v=mul(v,list(d_power(dp)),cap)
        if n:
            v=mul(v,theta[n],cap)
        return tuple(pad(v,cap))

    def shifted(v,j):
        return pad(([Q(0)]*j+list(v))[:cap],cap)

    def nonconstant_matrix(specs,normalized):
        cols=[]
        labels=[]
        v0=[]
        for n,bh,ct,z,E in specs:
            if E < 0:
                continue
            dp=n-z if normalized else n+z
            v=source_series(n,bh,ct,dp)
            for j in range(E+1):
                cols.append(shifted(v,j))
                labels.append((n,j))
                v0.append(int(v[0]) if j==0 else 0)
        rows=[[col[i] for col in cols] for i in range(cap)]
        return rows,labels,v0

    profiles,mask_counts=original_profiles()
    profile_reports=[]
    max_bad=101
    max_used_row=0
    uniform=True
    for number,prof in enumerate(profiles):
        z=prof["z"]
        specs=[]
        for n in range(1,4):
            bh=max(0,ceildiv(n-prof["mh_max"],4))
            ct=max(0,ceildiv(n-prof["m1_max"],3))
            zd=(n+prof["delta_d_max"])//2
            K=(9*n+prof["delta_inf_max"])//2
            E=K+zd-2*bh-ct
            specs.append((n,bh,ct,zd,E))
        rows,labels,v0=nonconstant_matrix(specs,True)
        N=len(labels)
        if N+z >= M:
            raise ValueError("Increase the bounded prefix for this full profile")
        ints,denbits=base.row_integral(rows,small)
        g=0
        minors=[]
        remaining=0
        factors=[]
        # The constant columns 1,t,...,t^z have an identity block in rows 0..z.
        # Each displayed determinant is therefore a full augmented minor.
        for first in range(z+1,M-N+2):
            inds=list(range(first,first+N))
            det=base.det_bareiss([ints[i] for i in inds])
            if det == 0:
                continue
            g=math.gcd(g,abs(det))
            remaining,factors=base.strip_small(g,small)
            minors.append({
                "constant_rows":[0,z],"nonconstant_rows":[first,first+N-1],
                "det_sha256":digest(str(det)),
                "det_bits":abs(det).bit_length()})
            print("R797 profile=%d z=%d first=%d remaining_bits=%d" %
                  (number,z,first,remaining.bit_length()),
                  file=sys.stderr,flush=True)
            if remaining==1:
                break
        paid=(g!=0 and remaining==1)
        uniform=uniform and paid
        used=max((x["nonconstant_rows"][1] for x in minors),default=0)
        max_used_row=max(max_used_row,used)
        if factors:
            max_bad=max(max_bad,max(p for p,e in factors))
        profile_reports.append({
            **prof,"specs":specs,
            "nonconstant_columns":N,
            "full_columns":N+z+1,
            "minor_count":len(minors),"max_row":used,
            "minor_ranges":[x["nonconstant_rows"] for x in minors],
            "minor_stream_sha256":digest(minors),
            "first_two_minors":minors[:2],
            "gcd_bits":g.bit_length(),"gcd_sha256":digest(str(g)),
            "gcd_factorization":factors,
            "remaining_large_part_bits":remaining.bit_length(),
            "remaining_large_part_sha256":digest(str(remaining)),
            "uniform_gate_paid":paid,"row_denominator_max_bits":denbits})
    # Every denominator in a used row n is supported at primes <=6n-1.
    # p>12*max_used_row+11 also gives h=(p-11)/12>max_used_row.
    cutoff=(max(101,max_bad,12*max_used_row+11) if uniform else trial_bound)
    assert cutoff <= trial_bound
    classes=geometry_classes(profiles)
    cache={}
    finite=[]
    remaining_classes=[]
    eligible_counts={}
    for p in primes_to(cutoff):
        if p<=101 or p%12!=11:
            continue
        h=(p-11)//12
        eligible=[c for c in classes if c["kappa"]+14<=h]
        checked=0
        consistent=0
        possible=0
        for c in eligible:
            z=c["z"]
            key=(p,z,c["c"],tuple(c["specs"]))
            if key not in cache:
                rows,labels,v0=nonconstant_matrix(c["specs"],False)
                # Lower coefficients of monic H are true unknowns.
                # The leading H_z=1 contributes the exact right hand side.
                constants=[shifted(d_power(c["c"]),j) for j in range(z)]
                all_rows=[row+[col[i] for col in constants]
                          for i,row in enumerate(rows)]
                all_labels=labels+[(0,j) for j in range(z)]
                all_v0=v0+[int(d_power(c["c"])[0]) if j==0 else 0
                            for j in range(z)]
                rr=base.field_rows(all_rows[:h],p)
                target=shifted(d_power(c["c"]),z)[:h]
                rhs=[(-v.numerator*pow(v.denominator,-1,p)) % p
                     for v in target]
                cache[key]=affine_report(
                    rr,rhs,p,all_labels,all_v0,z)
            report=cache[key]
            checked += 1
            if report["consistent"]:
                consistent += 1
                if report["linear_open_nonempty"]:
                    possible += 1
                    remaining_classes.append({"prime":p,"h":h,**c,**report})
        finite.append({
            "prime":p,"h":h,
            "eligible_geometry_classes":checked,
            "consistent_geometry_classes":consistent,
            "necessary_open_classes":possible})
        eligible_counts[p]=checked
        print("R797 p=%d h=%d eligible=%d consistent=%d remaining=%d" %
              (p,h,checked,consistent,possible),file=sys.stderr,flush=True)

    all_excluded=uniform and not remaining_classes
    result={
        "format":"R797 original r2 q0=0 b3 all-prime source gate",
        "max_order":M,
        "base_producer_sha256":hashlib.sha256(_base_path.read_bytes()).hexdigest(),
        "raw_mask_counts_by_z":mask_counts,
        "deduplicated_profile_count":len(profiles),
        "profiles":profile_reports,
        "uniform_gate_paid":uniform,
        "large_prime_cutoff":cutoff,
        "largest_common_bad_prime":max_bad,
        "largest_used_row":max_used_row,
        "geometry_class_total":len(classes),
        "minimum_geometric_kappa":min(c["kappa"] for c in classes),
        "distinct_finite_matrices":len(cache),
        "finite_prime_count":len(finite),
        "finite_checked_geometry_classes":sum(x["eligible_geometry_classes"] for x in finite),
        "finite_consistent_geometry_classes":sum(x["consistent_geometry_classes"] for x in finite),
        "finite_prime_reports_sha256":digest(finite),
        "finite_prime_ranges":[[x["prime"],x["h"],x["eligible_geometry_classes"],
                                x["consistent_geometry_classes"],x["necessary_open_classes"]]
                               for x in finite],
        "remaining_class_count":len(remaining_classes),
        "remaining_classes_sha256":digest(remaining_classes),
        "remaining_examples":remaining_classes[:args.remaining_examples],
        "all_strong_b3_excluded":all_excluded,
        "scope":"F_p, p=12h+11>101; r2 ell1 k0; q0=0 hence q=Y*qtilde,mq1; b=b0=3; actual original hats and h>=kappa+14. H(0) may be zero. No higher-b, p^3 or central claim.",
        "outputs_persisted":False}
    result["all_geometry_inputs_sha256"]=digest(classes)
    result["all_finite_matrix_results_sha256"]=digest(
        [{"key":key,"result":val} for key,val in sorted(cache.items())])
    # Reporting-only compaction after every exact calculation has finished.
    # The full dictionaries remain reproducible and their joint hash is retained.
    result["full_profile_reports_sha256"]=digest(profile_reports)
    result["profile_bounds_order"]=["mh_max","m1_max","delta_d_max","delta_inf_max"]
    result["profiles"]=[{
        "z":r["z"],"masks":r["masks"],
        "bounds":[r[k] for k in result["profile_bounds_order"]],
        "columns":r["nonconstant_columns"],
        "full_columns":r["full_columns"],
        "minor_ranges":r["minor_ranges"],
        "minor_stream_sha256":r["minor_stream_sha256"],
        "first_two_det_sha256":[d["det_sha256"] for d in r["first_two_minors"]],
        "gcd_factorization":r["gcd_factorization"],
        "gcd_bits":r["gcd_bits"],"gcd_sha256":r["gcd_sha256"],
        "unfactored_bits":r["remaining_large_part_bits"],
        "unfactored_sha256":r["remaining_large_part_sha256"],
        "max_row":r["max_row"],"uniform_gate_paid":r["uniform_gate_paid"]
    } for r in profile_reports]
    encoded=json.dumps(result,separators=(",",":"))
    while len(encoded.encode()) > 59000 and result["remaining_examples"]:
        result["remaining_examples"].pop()
        encoded=json.dumps(result,separators=(",",":"))
    if len(encoded.encode()) > 59000:
        raise ValueError("Output exceeds the 59000-byte public-log budget")
    print(encoded)


if __name__=="__main__":
    main()
