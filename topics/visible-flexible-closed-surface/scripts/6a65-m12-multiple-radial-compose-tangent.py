#!/usr/bin/env python3
"""Use the true R114 composition/tangent solver with multi-radial Cartesian W.

This is an explicit adapter: the only mathematical replacement is patch_jet,
now b_j(s)=chi(s)Legendre_j(2tau-1). Cached field values are identical stored
512-mode Fourier values at the same input. All underlying source identities
are recorded after the delegated actual run.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


tangent=module("m12_multi_tangent",HERE/"6a65-m12-up-patch-tangent-followup.py")
multiple=module("m12_multi_cartesian",HERE/"6a65-m12-multiple-radial-stress.py")
original=tangent.comp.PartialField


class CachedField(original):
    def value_derivatives(self,s):
        if getattr(self,"last_s",None)==s:
            return self.last_value
        self.last_s=s
        self.last_value=super().value_derivatives(s)
        return self.last_value


def patch(S,U,psi,rg,coeff):
    if coeff.ndim==1:
        if len(coeff)%24:
            raise ValueError("Incomplete radial Cartesian block")
        coeff=coeff.reshape(-1,24)
    return multiple.patch_jets(S,U,psi,rg,coeff)


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--parameters",type=Path,required=True)
    args,_=parser.parse_known_args()
    p=json.loads(args.parameters.read_text())
    if p.get("schema")!="6a65-multi-radial-cartesian-parameters-v1":
        raise ValueError("Expected explicitly identified multi-radial parameters")
    tangent.comp.PartialField=CachedField
    tangent.comp.patch_jet=patch
    tangent.main()
    report=json.loads(args.out.read_text())
    report["adapter_source_sha256"]=tangent.comp.sha(__file__)
    report["multiple_stress_source_sha256"]=tangent.comp.sha(HERE/"6a65-m12-multiple-radial-stress.py")
    report["radial_cartesian_blocks"]=p["radial_blocks"]
    report["mathematical_object"]="(X+W_multi) o (Phi_R114+P,Q), same original g0 supplier; every trial is a shifted-point full-Gram evaluation"
    report["cached_field_scope"]="Same s/input psi only; values/first derivatives unchanged, no approximation"
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:report[k] for k in ("adapter_source_sha256","multiple_stress_source_sha256","radial_cartesian_blocks")},indent=2))


if __name__=="__main__":
    main()

