#!/usr/bin/env python3
"""Independent standard-library check of the R79 small-CM twist certificate."""

import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from verify_p41_twist_certificate import determinant_mod, krylov_rows


def main(path):
    data = json.loads(path.read_text())
    assert (data["level"], data["weight"], data["star"], data["fricke"]) == (1681, 2, -1, 1)
    assert data["new"] and data["dimension"] == 54 and data["modulus"] == 1009
    assert data["trace_T2"] == -8
    source = path.with_name(data["hecke_reference"])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == data["hecke_reference_sha256"]
    h = json.loads(source.read_text())["hecke_matrix_mod"]
    assert len(h) == 54 and all(len(row) == 54 for row in h)
    for i, discriminant in enumerate((4, 8)):
        row = data[f"twist{discriminant}_exact"]
        assert len(row) == 54 and all(isinstance(v, int) for v in row)
        value = determinant_mod(krylov_rows(row, h, 1009), 1009)
        assert value == data["krylov_determinants_mod"][i] == (414, 520)[i]
        print(f"D=-{discriminant}: exact rank 54, determinant mod 1009 = {value}")
    print("Verified both translation Heegner divisors on every eigenline.")


if __name__ == "__main__":
    default = Path(__file__).with_name("data") / "p41_small_cm_certificate.json"
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
