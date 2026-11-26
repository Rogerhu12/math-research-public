#!/usr/bin/env python3
"""Repair only the unnecessary height query in the identified finite input.

The completed material field was not persisted as a large array. Its
necessary new evaluation is charged again and its old cost remains in the
ledger. This wrapper does not replay old seed comparisons or core solves,
change the field definition, delete fine points, or alter acceptance gates.
"""
import hashlib
import json
from pathlib import Path

import numpy as np

BINDINGS = {
    "r582_finite_resonant_continuation_20261126.py":
        "f7e4c570cc11f6810973d5357a5543ec9754416ab3a55302876cc70486246d7c",
    "r582_paid_resonant_field_20261126.py":
        "1b046b20541fcee05d5c8722dfdd5a509e7018348aab7182bec77c0813a8b395",
    "r582_continuous_mean_profile_20261126.py":
        "35060aa3e862c4852b30396493be37d1bd688281b4a093bd1e532d964e562631",
}
for filename, expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError("identified finite repair source binding differs: "+filename)
import r582_finite_resonant_continuation_20261126 as driver
from r582_paid_resonant_field_20261126 import (
    ResonantField, REFERENCE_CONTROL, REFERENCE_CORE_RADIUS,
)
from r582_continuous_mean_profile_20261126 import (
    ContinuousMean, CORE_END, LENGTH, FREE_WIDTH, BACKGROUND_END,
    CIRCLE_RADIUS, RC, compact_bump,
)

SCHEMA = "r582-finite-resonant-radius-only-implementation-repair-v2"
PAID_MATERIAL_MESH = "0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991"
ORIGINAL_INPUT_SHA256 = "387d58a18278b1b46cbbe6e834d24d42c8eeb84bf9d3e95e3030d629dac51852"
old_load_input = driver.load_input


def load_input(raw, digest):
    source, paid, nodes = old_load_input(raw,digest)
    origin = source["implementation_repair_origin"]
    if (origin["run_id"] != 45824332845 or origin["job_id"] != 139924470256
            or origin["source_commit"] != "d1e1da311acc61e11143fb2888f7613a4eaeb53a"
            or origin["FINAL_JSON_sha256"] != "7376b0a882baa61d651dab169fbc65448ee0914389794d61adb63c6c6a91157c"
            or origin["paid_material_mesh_binary64_sha256"] != PAID_MATERIAL_MESH):
        raise ValueError("radius-only repair requires its actual completed setup failure")
    original = json.loads(json.dumps(source))
    original.pop("implementation_repair_origin")
    original["prior_cost_ledger"].pop("identified_finite_field_setup_failure")
    encoded = json.dumps(original,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    if hashlib.sha256(encoded).hexdigest() != ORIGINAL_INPUT_SHA256:
        raise ValueError("repair altered the original paid mouth, reference, grid or scope input")
    return source,paid,nodes


class RadiusOnlyField(ResonantField):
    def reference_radius_jets(self, positions):
        """Same arithmetic as ContinuousMean radius; no H or z is requested."""
        self.check()
        s=np.asarray(positions,dtype=float)
        self.counts["radius_only_reference_queries"]+=len(s)
        chi,comp,first,second=ContinuousMean.step_jets(s,CORE_END,LENGTH)
        beta=4*chi*comp
        beta1=4*first*(comp-chi)
        beta2=4*second*(comp-chi)-8*first*first
        x=np.clip((s-CORE_END)/FREE_WIDTH,0,1)
        p,p1,p2=(self.mean.spline_a(x,k)/FREE_WIDTH**k for k in range(3))
        alpha=beta*p
        alpha1=beta1*p+beta*p1
        alpha2=beta2*p+2*beta1*p1+beta*p2
        bg,bgc,bg1,bg2=ContinuousMean.step_jets(s,CORE_END,BACKGROUND_END)
        r0=RC+LENGTH-s
        ab=bgc*CIRCLE_RADIUS+bg*r0
        ab1=bg1*(r0-CIRCLE_RADIUS)-bg
        ab2=bg2*(r0-CIRCLE_RADIUS)-2*bg1
        ea=np.exp(alpha)
        a=ea*ab
        a1=ea*(ab1+ab*alpha1)
        a2=ea*(ab2+2*ab1*alpha1+ab*(alpha2+alpha1*alpha1))
        psi,psi1,psi2=compact_bump(s).T
        mu=REFERENCE_CONTROL[0]
        e=np.exp(mu*psi)
        return (e*a,e*(a1+a*mu*psi1),
            e*(a2+2*a1*mu*psi1+a*(mu*psi2+mu*mu*psi1*psi1)))

    def angular_radial_jets(self, positions, bg_comp, bg_first, bg_second):
        s=np.asarray(positions,dtype=float)
        jets=self.evaluate(s)
        a,a1,a2=self.reference_radius_jets(s)
        def quotient(start,factor):
            v,v1,v2=jets[:,start:start+3].T
            return factor*np.stack((v/a,v1/a-v*a1/a**2,
                v2/a-2*v1*a1/a**2-v*a2/a**2+2*v*a1*a1/a**3),axis=1)
        uj,vj=quotient(0,1.5),quotient(3,-2.)
        core_derivative=3/(4*REFERENCE_CORE_RADIUS)
        uj[:,0]-=np.asarray(bg_comp).ravel()*core_derivative
        uj[:,1]+=np.asarray(bg_first).ravel()*core_derivative
        uj[:,2]+=np.asarray(bg_second).ravel()*core_derivative
        return uj,vj

    def receipt(self):
        value=super().receipt()
        value["radius_only_repair"]={
            "schema":SCHEMA,"unneeded_height_integrals_removed_only_from_seed_quotient":True,
            "same_reference_radius_formula_and_order_of_operations":True,
            "same_q_mu_nu_p_and_all_fine_observation_positions":True,
            "prior_completed_material_mesh_binary64_sha256":PAID_MATERIAL_MESH,
            "new_material_mesh_matches_prior_completed_mesh":self.material_mesh_sha256==PAID_MATERIAL_MESH,
            "necessary_material_reevaluation_is_charged_as_new_work":True,
            "old_70_62187625499996_scientific_seconds_remain_in_source_ledger":True,
            "no_new_independent_preflight_or_old_comparison_run":True}
        return value


def main():
    driver.load_input=load_input
    driver.ResonantField=RadiusOnlyField
    driver.SCHEMA=SCHEMA
    driver.main()


if __name__=="__main__":
    main()
