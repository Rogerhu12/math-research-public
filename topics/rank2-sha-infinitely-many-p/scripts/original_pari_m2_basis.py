#!/usr/bin/env sage-python
"""R892: one persistent exact PARI M2(867) basis for the original map producers.

No coefficient file is created.  Every expansion is computed by mfcoefs on the
same mfinit object; larger requests must reproduce every previous coefficient.
The resulting forms expose only the q_expansion interface used by the original
producers and their same-process consumers.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

import hashlib
from pathlib import Path
from sage.all import QQ, PowerSeriesRing, pari


class _PariWeightTwoForm:
    def __init__(self, owner, index):
        self.owner = owner
        self.index = index

    def q_expansion(self, precision):
        precision = int(precision)
        self.owner.ensure_precision(precision)
        ring = PowerSeriesRing(QQ, "q", default_prec=precision)
        return ring(self.owner.columns[self.index][:precision]).add_bigoh(precision)


class PariOriginalM2Basis:
    def __init__(self, progress):
        self.progress = progress
        self.seed = 20261116
        self.precision = 0
        self.columns = None
        progress("initialize exact PARI full rational M2(867) basis")
        # The seed is set immediately before mfinit, independently of any earlier
        # finite-ideal calculations.  Pinning the image also pins PARI.
        pari.allocatemem(268435456, 4294967296)
        pari.setrand(self.seed)
        self.mf = pari.mfinit([867, 2, 1], 4)
        parameters = list(pari.mfparams(self.mf))
        assert [int(t) for t in parameters[:4]] == [867, 2, 1, 4]
        assert int(pari.mfspace(self.mf)) == 4
        assert int(pari.mfdim(self.mf)) == 120
        self.basis = list(pari.mfbasis(self.mf))
        assert len(self.basis) == 120
        self.forms = [_PariWeightTwoForm(self, j) for j in range(120)]
        self.provenance = {
            "engine": "PARI full mfinit([867,2,1],4), one fixed mfbasis",
            "pari_version": str(pari.version()),
            "seed_immediately_before_mfinit": self.seed,
            "space": [867, 2, 1, 4],
            "dimension": 120,
            "coefficient_field": "QQ",
            "coefficient_method": "mfcoefs on the same space; whole-matrix columns",
            "dependency_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        }
        progress("exact PARI full rational basis initialized",
                 basis_provenance=self.provenance)

    def ensure_precision(self, precision):
        precision = int(precision)
        assert precision >= 1
        if precision <= self.precision:
            return
        self.progress("extend persistent PARI basis", precision=precision,
                      previous_precision=self.precision)
        coefficients = pari.mfcoefs(self.mf, precision-1)
        assert tuple(int(t) for t in coefficients.matsize()) == (precision, 120)
        # QQ conversion is exact and deliberately rejects a nonrational value.
        columns = [[QQ(coefficients[i, j]) for i in range(precision)]
                   for j in range(120)]
        if self.columns is not None:
            assert all(columns[j][:self.precision] == self.columns[j]
                       for j in range(120))
        self.columns = columns
        self.precision = precision
        self.progress("persistent PARI basis expansion ready", precision=precision)
