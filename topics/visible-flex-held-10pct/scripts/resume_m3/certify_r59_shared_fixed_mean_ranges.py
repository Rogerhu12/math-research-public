#!/usr/bin/env python3
"""Continuous mean ranges for an explicit shared-two-jet C2 bridge family.

The original physical file is untouched. The interval family contains both its
piecewise polynomial oracle and the exact shared-Hermite coefficient/chart
object. A separately certified 1e-8 background two-jet envelope includes the
true-primitive or explicit shared-jet repaired bridge. This is a NEW declared
C2 interpretation, not silent identification of the rounded source oracle.
"""
import hashlib,importlib.util,json,sys
from pathlib import Path
from fractions import Fraction as Q
import numpy as np

HERE=Path(__file__).resolve().parent
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m
base=module("_r59_shared_mean_base",HERE/"certify_r59_fixed_mean_ranges.py")
shared=module("_r59_shared_mean_transfer",HERE/"certify_r59_shared_jet_transfer.py")
LAST=None
Original=base.MeanVerifier
class SharedMeanVerifier(Original):
    def __init__(self,o,z,N):
        super().__init__(o,z,N)
        global LAST
        rec=json.loads(Path(o.relative_metric_loader_record["source_run"]).read_text())
        if N!=int(rec["prefix_audit"]["samples_psi"]):
            raise ValueError("Must use the actual original run's declared audit mean rule")
        if self.f.cfg["prefix_bridge"]!={"kind":"turn_plateau_v1","curvature":4,"peak_fraction":.2}:
            raise ValueError("The separate background error certificate is for the curvature-4 bridge")
        expected=[
            Q(5404319552844595,18014398509481984),
            Q(2882303761517127,36028797018963968),
            Q(-4203359652212477,2251799813685248)]
        actual=[Q.from_float(float(self.f.port_data["cut"][key])) for key in
                ("radius","backgroundSlope","backgroundSecond")]
        if actual!=expected or self.f.bridge.astart!=1.:
            raise ValueError("Actual cut differs from the separately certified reference")
        self.transfer=shared.SharedBridgeData(o,z)
        self.background_padding=1e-8
        self.pad_a=self.symmetric(Q(1,10**8))
        self.pad_y=[]
        for row in self.transfer.y_error[:2]:
            values=[float(base.I.rational(v).x[1]) for v in row]
            arr=np.asarray(values)
            self.pad_y.append(base.I(-arr,arr)*base.I(o.q))
        self.pad_e=[self.symmetric(v) for v in self.transfer.e_error]
        LAST=self
    @staticmethod
    def symmetric(v):
        up=float(base.I.rational(v).x[1]);return base.I(-up,up)
    def coefficients(self,s,left,right):
        value=super().coefficients(s,left,right)
        return base.D(value.v+self.pad_y[0],value.d+self.pad_y[1])
    def chart(self,s,left,right):
        e,ep=super().chart(s,left,right)
        return (base.D(e.v+self.pad_e[0],e.d+self.pad_e[1]),
                base.D(ep.v+self.pad_e[1],ep.d+self.pad_e[2]))
    def profile(self,s,left,right):
        a,ap,reference=super().profile(s,left,right)
        return (base.D(a.v+self.pad_a,a.d+self.pad_a),
                base.D(ap.v+self.pad_a,ap.d+self.pad_a),reference)

base.MeanVerifier=SharedMeanVerifier
base.__file__=str(Path(__file__).resolve())
out=Path(sys.argv[sys.argv.index("--out")+1])
try:
    base.main()
finally:
    if out.exists() and LAST is not None:
        j=json.loads(out.read_text())
        j["explicit_shared_C2_interval_family"]=True
        j["original_physical_modified"]=False
        j["base_mean_source_sha256"]=hashlib.sha256((HERE/"certify_r59_fixed_mean_ranges.py").read_bytes()).hexdigest()
        j["shared_transfer_source_sha256"]=hashlib.sha256((HERE/"certify_r59_shared_jet_transfer.py").read_bytes()).hexdigest()
        j["background_error_contract"]="Separate same-cut bridge primitive/repair certificate must give all physical a/ap value/derivative errors <=1e-8; this is an explicit input, not an empirical assumption."
        j["shared_coefficient_0_1_error_maxima"]=[str(max(row)) for row in LAST.transfer.y_error[:2]]
        j["shared_e_0_1_2_error_maxima"]=[str(v) for v in LAST.transfer.e_error]
        j["scope"].append("The padded family includes exact shared-Hermite Y/e and a consistently repaired C2 bridge background, under the explicit 1e-8 background contract. It is not silently the original piecewise oracle.")
        out.write_text(json.dumps(j,indent=2)+"\n")

