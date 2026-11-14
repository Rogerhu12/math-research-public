#!/usr/bin/env python3
"""Original physical-quintic readout with the explicit frozen v2 controls."""
import hashlib
import json
from pathlib import Path
import sys

import geometry_20261114_full_dn_readout as original
from geometry_20261114_prefix_controls_profile import reconstruct_profile


def main():
    original.exact_profile_formula = reconstruct_profile
    original.main()
    output = Path(sys.argv[sys.argv.index("--out")+1])
    data = json.loads(output.read_text())
    data["prefix_controls_readout_source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data["prefix_controls_profile_source_sha256"] = hashlib.sha256(Path(__file__).with_name(
        "geometry_20261114_prefix_controls_profile.py").read_bytes()).hexdigest()
    output.write_text(json.dumps(data,indent=2,allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
