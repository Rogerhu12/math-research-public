"""WMR input only: rematerialize the exact completed RHI endpoint.

The original coefficient construction and floating proposal recurrence
are necessary inputs to a NEW physical-height contraction.  The old
RHI residual certification, strip accumulation, norms and mean targets
are not called.  Whole endpoint/ordered-chain mismatch is failure.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib,json
from pathlib import Path


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()


def coefficient_grid(c,core,fields,grid):
    """Exactly the coefficient-only first part of frozen RHI.source.

    No source-error norm, strip integral or published target is produced.
    The unchanged Fourier interval endpoints determine the exact source
    midpoint used by the original floating proposal.
    """
    z=c.zeros((grid,4,12))
    for j,f in enumerate(fields):
        old=f.Fourier();n=old.real.lo.shape[1]
        z[:core.GRID//2,:n,j:j+1]=old[:core.GRID//2]
        z[-core.GRID//2:,:n,j:j+1]=old[core.GRID//2:]
    values=c.real(c.fft.fft(z,inverse=True)*grid)
    coefficients=c.affine_polynomial(
        [values[:,k,:] for k in range(4)],Fraction(1),Fraction(-2))
    return c.Box(c.np.stack([x.lo for x in coefficients]),
                 c.np.stack([x.hi for x in coefficients]))


def restore(np,c,core,nu,rhi,base,offsets,rows,nodes,original_plan,
            jets,read_ball,actual,private,progress,atomic):
    """Return exact all18 endpoint, original receipt and restoration facts."""
    expected=actual["whole_private_carrier_receipt"]
    require(actual["complete"] is actual["proved"] is True
        and actual["failure"] is None and actual["saved_record_count"]==4,
        "one actually completed entire RHI result is required")
    require(rhi.GRID==2048 and rhi.ORDER==6
        and expected["all18_components_retained"] is True
        and expected["complete_readback"] is True
        and expected["exact_endpoint"]=="0"
        and expected["shape"]==[2048,18] and expected["bytes"]==294912,
        "whole completed18-component carrier, not only its means")
    plan=rhi.full_plan(original_plan)
    plan_sha=sha(canonical(plan))
    require(plan_sha==expected["complete_plan_sha256"],
        "same complete ordered original RHI certificate plan")
    fields=rhi.Fields(c,core,nu)
    state=np.zeros((rhi.GRID,18))
    state[:,:9]=np.eye(3).reshape(1,9)
    edge=Fraction(9,50)
    chain=sha(b"RHI complete ordered relative carrier v1\n")
    for index,item in enumerate(reversed(plan),1):
        left,right=map(Fraction,item["interval"])
        require(right==edge,"same complete reverse interval order")
        source_fields=fields.make(base,offsets,rows[item["row"]],
            item,nodes,jets,read_ball)
        source=coefficient_grid(c,core,source_fields,rhi.GRID)
        unused_coefficients,state=rhi.proposal(np,state,source,right-left)
        payload=np.asarray(state,dtype="<f8").tobytes(order="C")
        receipt={"shape":[2048,18],"bytes":len(payload),"sha256":sha(payload),
                 "encoding":"little-endian IEEE754 binary64 row-major"}
        chain=sha(canonical({"previous":chain,"complete_cells":index,
            "exact_endpoint":str(left),"whole_carrier":receipt}))
        edge=left
        if index%64==0 or index==len(plan):
            progress("restoring_necessary_original_RHI_carrier",
                {"restored_ordered_cells":index,"complete_cells":len(plan),
                 "exact_endpoint":str(edge),"old_scientific_targets":0})
    require(edge==0 and receipt["sha256"]==expected["sha256"]
        and chain==expected["whole_ordered_receipt_chain_sha256"],
        "exact original whole endpoint and ordered chain; no substitute trial")
    require(actual["relative_carrier_prefix"]["complete_cells"]==len(plan)
        and actual["relative_carrier_prefix"]["exact_interval"]==["0","9/50"]
        and actual["relative_carrier_prefix"]["whole_private_endpoint"]==receipt
        and actual["relative_carrier_prefix"]["whole_accepted_endpoint_chain_sha256"]==chain,
        "same genuinely accepted full RHI endpoint prefix")
    target=Path(private)/"same-complete-relative-endpoint.f64"
    atomic(target,payload)
    require(target.read_bytes()==payload,"whole necessary carrier readback")
    restored=np.memmap(target,dtype="<f8",mode="r",shape=(2048,18))
    return restored,{
        "all18_original_components_retained":True,
        "complete_original_endpoint":receipt,
        "complete_plan_sha256":plan_sha,
        "whole_ordered_receipt_chain_sha256":chain,
        "complete_ordered_cells":len(plan),
        "exact_interval":["0","9/50"],
        "coefficient_construction_and_proposal_only":True,
        "old_RHI_residual_steps_evaluated":0,
        "old_RHI_strip_or_mean_targets_evaluated":0,
        "old_NP_targets_evaluated":0,
        "new_carrier_chosen":False,
        "complete_private_readback":True}
