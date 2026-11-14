#!/usr/bin/env python3
"""Small floating diagnostic of one saved causal edge, never a certificate.

Uses four cells 12..15 and the eleven existing rigorous band records.
No ODE, quadrature, Node worker, matrix factorization or source evaluation.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import gzip
import hashlib
import json
import math
from pathlib import Path


def main():
    names = {
        "middle": "notes/2026-11-12-tail-r33-plateau2-middle-causal-box-v2.json.gz",
        "density": "notes/2026-11-12-tail-r33-plateau2-density-window.json.gz",
        "positive": "notes/2026-11-12-closure-positive-highband-38.json.gz",
        "local": "notes/2026-11-12-tail-r33-plateau2-middle-local-homogeneous.json.gz",
        "ready": "notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json",
        "low": "notes/2026-11-12-closure-recovery2-centred-four-green-r1.json.gz",
    }
    docs, hashes = {}, {}
    for key, name in names.items():
        data = Path(name).read_bytes()
        docs[key] = json.loads(gzip.decompress(data) if name.endswith(".gz") else data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    def number(record):
        point = record["upper"]
        try:
            return math.ldexp(float(int(point["mantissa"])), point["binary_exponent"])
        except OverflowError:
            return math.inf
    def multiply(a, b):
        return 0.0 if a == 0 or b == 0 else a*b
    def positive_sum(a, b):
        return a+b
    middle = docs["middle"]
    rows = {r["cell"]: r for r in docs["density"]["rows"]}
    local = {r["cell"]: r for r in docs["local"]["cell_rows"]}
    positive = {r["cell"]: r for r in docs["positive"]["cell_rows"]}
    params = docs["ready"]["rationalDeepModel"]["physicalParameters"]
    rc = float(params["rCuff"])
    R, rho, rt12 = rc*257/256, 2**(11/4), math.sqrt(12)
    output = []
    for bi, band in enumerate(middle["bands"]):
        lo, hi = band["first_mode"], band["last_mode"]
        nu_lo, nu_hi = lo*lo*(lo*lo-1)/12, hi*hi*(hi*hi-1)/12
        cfg = {}
        for n in range(12, 16):
            r, loc = rows[n], local[n]["bands"][bi]
            B, X, a = (number(r[k]) for k in ("B", "canonical_total_envelope", "Q_coefficient"))
            ml, mu, wl = (number(r[k]) for k in ("mu_lower", "mu_upper", "w_lower"))
            qweight, zweight = (1+hi)*(B*hi+hi*hi)/(a*X), (1+hi)*nu_hi/X
            yq = R**3*(B*hi+hi*hi)
            yin = rt12*mu*nu_hi/(rc**4*(ml/R**7))
            I = (R**4/(rt12*ml)*(X*(a*R**3+rt12*mu/(rc**4*wl)))**2
                 *(number(r["TV_log_w_upper"])+number(r["normalized_width_upper"])))
            matrix = (positive[n]["positive_cell_matrices"][bi]
                      if bi < len(docs["positive"]["bands"]) else None)
            A = [[number(v) for v in row] for row in matrix] if matrix is not None else None
            own = [number(loc["canonical_Q_end"]), number(loc["canonical_Xi_over_nu_end"])]
            peak, ownR = number(loc["local_gamma"])/2, number(loc["physical_norm_end"])
            if A is not None:
                other = [multiply(A[i][1], I)/nu_lo for i in range(2)]
                peak = min(peak, qweight*other[0]+zweight*other[1])
                ownR = min(ownR, yq*other[0]+yin/rho*other[1])
                own = [min(own[i], other[i]) for i in range(2)]
            cfg[n] = dict(
                B=B, A=A, own=own, ownR=ownR, peak=peak, yq=yq, yin=yin,
                yout=yin/rho, qweight=qweight, zweight=zweight,
                decay=math.exp(-lo*(number(r["tau_inner"])-number(r["tau_outer"]))),
                hpeak=(1+hi)*number(loc["homogeneous_peak_over_V"]),
                hend=number(loc["homogeneous_physical_end"]),
                qconvert=1/(B*lo*rc**3),
                zconvert=R**4*(rho*mu/rc**7)/(rt12*ml*nu_lo)*max(1, hi/B))
        c = cfg[15]
        state, oldB = (c["own"][0], c["own"][1], c["ownR"]), c["B"]
        for n in range(14, 11, -1):
            c = cfg[n]; Q, Z, Y = state
            inp = [Q, Z/rho]
            Rin = min(c["yq"]*inp[0]+c["yin"]*inp[1], max(1, c["B"]/oldB)*Y)
            localpeak, endR = c["hpeak"]*Rin, c["hend"]*Rin
            end = [c["qconvert"]*endR, c["zconvert"]*endR]
            peak = localpeak
            if c["A"] is not None:
                prop = [multiply(c["A"][i][0], inp[0])+multiply(c["A"][i][1], inp[1])
                        for i in range(2)]
                peak = min(peak, c["qweight"]*prop[0]+c["zweight"]*prop[1])
                end = [min(end[i], multiply(c["decay"], prop[i])) for i in range(2)]
            Yout = min(c["yq"]*end[0]+c["yout"]*end[1], endR)
            state, oldB = (end[0], end[1], Yout), c["B"]
        output.append(dict(index=bi, **band, approximate_gamma_12_15=2*peak))
    original = next(s for s in middle["gamma_rows"][0]["sources"] if s["source_cell"] == 15)
    corr = docs["low"]["gamma_upper"]["corr"][3][0]
    corr = math.ldexp(float(corr[0]), corr[1])
    near = max(row["approximate_gamma_12_15"] for row in output[:5])
    rest = max(row["approximate_gamma_12_15"] for row in output[4:])
    data = dict(
        status="Read-only small floating band diagnostic; not an interval certificate",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        output_cell=12, source_cell=15, bands=output,
        original_gamma=number(original["gamma"]), original_maximizing_band=original["maximizing_band"],
        near_true_modes=[94, 184], rest_true_modes=[186, 8190],
        shared_saved_band=[130, 192],
        near_approximate_gamma=near, rest_approximate_gamma=rest,
        low_corr_15_12=corr,
        old_cycle_9_H_C=9*number(original["gamma"])*corr,
        near_cycle_9_H_C_diagnostic=9*near*corr,
        notes=["Band4's existing upper covers either true subband conservatively.",
               "This changes only the comparison grouping, never the true kernel or source.",
               "Full mean, inverse remainder and quadratic changes retain all frequencies."],
        input_hashes=hashes,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    path = Path("notes/2026-11-12-tail-frequency-split-edge-probe.json")
    if path.exists():
        raise FileExistsError("Keep the existing diagnostic and use a fresh filename")
    path.write_text(json.dumps(data, indent=2)+"\n")
    print(json.dumps(data))


if __name__ == "__main__":
    main()
