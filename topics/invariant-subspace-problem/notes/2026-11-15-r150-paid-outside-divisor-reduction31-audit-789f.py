#!/usr/bin/env python3
"""2026-11-15. Author: ChatGPT (AI), literature_audit.
Read-only audit of the paid exact outside divisor and its coefficient reduction.
No original core, determinant, profile, or 56-row certificate is recomputed.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, math, os, resource, signal, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
from flint import fmpq_poly, fmpz_poly, nmod_poly, nmod_mat

P = 31
UPPER_BYTES = 12999
UPPER_SHA = "b6c26ab0cfae6a08dbdb02ebac570ef2fffaec953a0de4d9aef422b74815c3ab"
PAYLOAD_SHA = "e1722fa0f09424affa18c29e4275858619cf4c789a891937fc6c6d4355a867c1"
UPPER_BINDING = "5fc42d162e51b638ce06bbd67c2afd5755539a95a3bf5a650c4155df0ed6c8ef"
UPPER_COEFF_SHA = "150089b4e115b8d975d4e4eb13492779a692a6af258094f852af22b7f34e652d"
OMEGA_SHA = "64c4bb8be9715e4f8bb252a98ca1e5a78d02ccee594946fefba56af058ba44df"
FACTOR_SHA = "c2e27cf7e732257b695a6fa655f24b2305fd817a779baa3965a2eccc5f663dc2"
OMEGA_BINDING = "3456b533e6fba9d39af5638473f5b5afe04cbe342c8bddea7e88e752dd170c2a"
OMEGA_RAW = (4927, "93bcf19e898fb2c0f64bd5f891e656377cb72b900652c3d43c1bf3bb0c4bf152")
OMEGA_OUTER = (9088, "02f152b31cb6a07cf28fb8c310098c3b658aa9f40483a99ee7b4f8f8bd391f1f")
STATE_SHA = "06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
READER_SHA = "8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"

class BudgetStop(Exception):
    pass

def need(value, why):
    if not value:
        raise ValueError(why)

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def atomic(path, value):
    data = canonical(value)
    temporary = Path(str(path) + ".tmp")
    temporary.write_bytes(data)
    os.replace(temporary, path)

def encq(poly):
    return {"n": [str(x) for x in poly.numer().coeffs()], "d": str(poly.denom())}

def coeff(poly):
    return [int(poly[i]) for i in range(int(poly.degree()) + 1)]

def red(poly):
    values = []
    numer, common = poly.numer(), int(poly.denom())
    need(common > 0, "Positive canonical common denominator")
    for i in range(int(poly.degree()) + 1):
        n = int(numer[i])
        content = math.gcd(abs(n), common)
        n, d = n // content, common // content
        need(d > 0 and d % P, "Every actual rational coefficient has a 31-unit denominator")
        values.append((n % P) * pow(d % P, -1, P) % P)
    return nmod_poly(values, P)

def fact(poly):
    unit, parts = poly.factor()
    rebuilt = nmod_poly([int(unit)], P)
    records = []
    for f, e in parts:
        need(f.leading_coefficient() == 1, "Monic field irreducible factor")
        rebuilt *= f ** int(e)
        records.append({"coefficientsAscending": coeff(f), "exponent": int(e), "degree": int(f.degree())})
    need(rebuilt == poly, "Complete field factorization multiplied back")
    records.sort(key=lambda x: (x["degree"], x["coefficientsAscending"]))
    return {"unit": int(unit), "factors": records}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upper", type=Path, required=True)
    ap.add_argument("--omega-receipt", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--state", type=Path)
    ap.add_argument("--state-reader", type=Path)
    ap.add_argument("--seconds", type=float, default=60)
    ap.add_argument("--memory-mib", type=int, default=512)
    a = ap.parse_args()
    need(0 < a.seconds <= 60 and 256 <= a.memory_mib <= 1024, "Explicit small audit budget")
    need(bool(a.state) == bool(a.state_reader), "Optional whole state and pinned reader must be supplied together")
    a.out.mkdir(parents=True, exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS, (a.memory_mib * 1048576,) * 2)
    start = time.monotonic()
    receipt = {"format": "r150-paid-outside-divisor-reduction31-audit-v1", "status": "running",
               "parameters": {"author": "ChatGPT (AI), literature_audit", "prime": P}}
    par = receipt["parameters"]
    def stop(signum, frame):
        raise BudgetStop("Small audit time budget")
    signal.signal(signal.SIGALRM, stop)
    signal.signal(signal.SIGTERM, stop)
    signal.setitimer(signal.ITIMER_REAL, a.seconds)
    code = 1
    try:
        uraw = a.upper.read_bytes()
        need((len(uraw), digest(uraw)) == (UPPER_BYTES, UPPER_SHA), "Entire paid upper gzip bytes and SHA")
        payload = gzip.decompress(uraw)
        need(digest(payload) == PAYLOAD_SHA, "Entire paid upper decompressed SHA")
        u = json.loads(payload)
        need(u["format"] == "r150-three-original-minor-determinant-upper-v1"
             and u["binding"] == UPPER_BINDING and u["completedMinorNumbers"] == [0, 1, 2],
             "Same three original minors and actual upper binding")
        ns = u["primitivePositiveGcd"]
        need(len(ns) == 121 and digest(canonical(ns)) == UPPER_COEFF_SHA, "All121 original primitive coefficients")
        zz = [int(x) for x in ns]
        need(zz[-1] > 0 and math.gcd(*zz) == 1, "Primitive positive original integer polynomial")
        omega = fmpq_poly(fmpz_poly(zz)) / zz[-1]
        need(int(omega.degree()) == 120 and omega.leading_coefficient() == 1
             and digest(canonical(encq(omega))) == OMEGA_SHA, "Exact same monic original Omega")
        ob = a.omega_receipt.read_bytes()
        rid = (len(ob), digest(ob))
        need(rid in (OMEGA_RAW, OMEGA_OUTER), "Exact completed original56 receipt identity")
        paid = json.loads(ob)
        if rid == OMEGA_OUTER:
            need(paid["exitCode"] == 0 and paid["runId"] == "43756208221"
                 and paid["stepId"] == "original56-single-kernel-bockstein-300"
                 and paid["fullTemporaryReceiptSHA256"] == OMEGA_RAW[1], "Completed original execution")
            paid = paid["result"]
        pp = paid["parameters"]
        need(paid["status"] == "completed" and paid["binding"] == OMEGA_BINDING
             and all(pp[k] is True for k in ("completeOriginalOutsideGcdComputed", "exactGcdEqualsUpper",
                 "all21PaidPivotsReproduced", "all56OriginalAxDivisionsVerified",
                 "all56OriginalCorrectionProductsVerified", "allOriginal56RowsCertified")),
             "Paid equality is for the complete original56 matrix")
        need(pp["exactOutsideGcdStatistics"]["coefficientSHA256"] == OMEGA_SHA
             and pp["inputs"]["upperStored"]["sha256"] == UPPER_SHA
             and pp["inputs"]["upperStored"]["payloadSHA256"] == PAYLOAD_SHA
             and pp["identity"]["factorSHA256"] == FACTOR_SHA,
             "Actual Omega/upper/factor identity chain")
        f = omega.gcd(omega.derivative())
        f /= f.leading_coefficient()
        need(int(f.degree()) == 60 and f * f == omega
             and int(f.gcd(f.derivative()).degree()) == 0
             and digest(canonical(encq(f))) == FACTOR_SHA, "Exact paid square of a squarefree monic degree60 factor")
        rb, fb = red(omega), red(f)
        need(int(rb.degree()) == 120 and int(fb.degree()) == 60
             and rb.leading_coefficient() == 1 and fb.leading_coefficient() == 1
             and fb * fb == rb, "All121 coefficients reduce with degree, monicity and square identity")
        par.update(
            upperIdentity={"bytes": UPPER_BYTES, "sha256": UPPER_SHA, "payloadSHA256": PAYLOAD_SHA,
                           "binding": UPPER_BINDING},
            paidOmegaReceipt={"bytes": rid[0], "sha256": rid[1], "binding": OMEGA_BINDING},
            rationalOmegaCoefficientSHA256=OMEGA_SHA, rationalSquareRootCoefficientSHA256=FACTOR_SHA,
            all121OmegaCoefficientDenominatorsAre31Units=True,
            all61SquareRootCoefficientDenominatorsAre31Units=True,
            rationalSquareIdentityVerified=True, fieldSquareIdentityVerified=True,
            fieldOmega={"coefficientsAscending": coeff(rb), "coefficientSHA256": digest(canonical(coeff(rb))),
                        "degree": 120, **fact(rb)},
            fieldSquareRoot={"coefficientsAscending": coeff(fb), "coefficientSHA256": digest(canonical(coeff(fb))),
                             "degree": 60, "repeatedFactorDegree": int(fb.gcd(fb.derivative()).degree()), **fact(fb)},
            fieldOmegaAtRoots={str(x): int(rb(x)) for x in (0, 1, 2, -6)},
            coreOrDeterminantsRecomputed=False, largeProfileDecoded=False,
            crossReceiptQ60ComparisonPerformed=False)
        if a.state:
            need(digest(a.state_reader.read_bytes()) == READER_SHA, "Paid complete315 reader source")
            sr = a.state.read_bytes()
            if sr[:2] == b"\x1f\x8b":
                sr = gzip.decompress(sr)
            need(digest(sr) == STATE_SHA, "Entire original torsion state")
            sp = a.out / "paid-state.bin"
            sp.write_bytes(sr)
            spec = importlib.util.spec_from_file_location("paid_r150_torsion", a.state_reader)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            st = module.load_state(sp)
            need(st["torsionDimension"] == 315 and st["observabilityRank"] == 505, "Entire315 original state")
            full = nmod_mat(st["matrices"]["action"], P).charpoly()
            x = nmod_poly([0, 1], P)
            hp = nmod_poly([17, 25, 26, 1], P)
            hm = nmod_poly([24, 24, 27, 1], P)
            he = nmod_poly([30, 15, 0, 2, 18, 13, 1], P)
            known = x**66 * (x-2)**32 * (x+6)**12 * (x-1)**7 * hp**8 * hm**8 * he**5
            exterior, remainder = divmod(full, known)
            need(not remainder and int(full.degree()) == 315 and int(exterior.degree()) == 120,
                 "Paid original full315 characteristic and complete known primary factors")
            par.update(crossReceiptQ60ComparisonPerformed=True, stateSHA256=STATE_SHA,
                       readerSHA256=READER_SHA, equalsPaidFieldQ60Squared=(rb == exterior),
                       paidFieldQ60Squared={"coefficientsAscending": coeff(exterior),
                                            "coefficientSHA256": digest(canonical(coeff(exterior)))})
        semantic = {"format": receipt["format"], "sourceSHA256": digest(Path(__file__).read_bytes()),
                    "upperSHA256": UPPER_SHA, "upperPayloadSHA256": PAYLOAD_SHA,
                    "omegaReceiptSHA256": rid[1], "omegaBinding": OMEGA_BINDING,
                    "stateSHA256": STATE_SHA if a.state else None}
        receipt["binding"] = digest(canonical(semantic))
        par["identity"] = semantic
        receipt["status"] = "completed"
        code = 0
    except BudgetStop as exc:
        receipt.update(status="budget-checkpoint", errorType=type(exc).__name__, error=str(exc))
        code = 75
    except Exception as exc:
        receipt.update(status="failed", errorType=type(exc).__name__, error=str(exc))
        code = 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        receipt["elapsedSeconds"] = time.monotonic() - start
        need(len(canonical(receipt)) < 30000, "Small exact coefficient audit receipt")
        atomic(a.out / "outside-divisor-reduction31-audit-receipt.json", receipt)
    print(json.dumps({"status": receipt["status"], "elapsedSeconds": receipt["elapsedSeconds"],
                      "fieldDegree": par.get("fieldOmega", {}).get("degree")}), flush=True)
    return code

if __name__ == "__main__":
    raise SystemExit(main())
