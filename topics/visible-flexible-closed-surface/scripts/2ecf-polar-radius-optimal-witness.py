#!/usr/bin/env python3
"""Sharp pointwise optimum when only the target angular radius may vary."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def analyze(path):
    record = json.loads(path.read_text())
    statistics = record.get("statistics", record.get("evaluation"))
    witness = statistics["worstMetric"]
    e, f, g = [witness[key] for key in ("e","f","g")]
    E = 1+e
    normalized_G = 1+g
    if E <= 0 or normalized_G <= 0 or E*normalized_G <= f*f:
        raise ValueError("A positive definite induced metric is required")
    optimum = (math.sqrt(e*e+(1-e)*f*f/normalized_G) if E < 2 else e)
    radius_ratio = math.sqrt(normalized_G/(2-E)) if E < 2 else None
    return dict(input=path.name,inputSHA256=hashlib.sha256(path.read_bytes()).hexdigest(),
                s=witness["s"],u=witness["u"],e=e,f=f,g=g,
                observed=witness["relative"],bestErrorAtThisPointOverAllRadii=optimum,
                bestRadiusRatioToOriginal=radius_ratio,
                radiusAloneAbsoluteRoomAtMost=witness["relative"]-optimum,
                finiteSample=True,positionFieldFixed=True)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("inputs",nargs="+",type=Path)
    args=parser.parse_args()
    rows=[analyze(path) for path in args.inputs]
    with args.output.open("x") as out:
        json.dump(dict(schema="sharp-pointwise-target-radius-floor-v1",rows=rows),out,indent=2)
        out.write("\n")
    for row in rows:
        print(row["input"],row["observed"],row["bestErrorAtThisPointOverAllRadii"])
