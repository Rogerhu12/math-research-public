#!/usr/bin/env python3
"""Apply the R33 density proof to the independently certified plateau2 box.

The continuous strip ceiling remains the original rising tau_n-1/8.
Only the certified reference strip is read from the supplied reference.
The original density proof, numerical gates and all source formulas remain.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import hashlib
from pathlib import Path
import types

HERE = Path(__file__).resolve().parent


def main():
    path = HERE/"tail_r33_physical_density_budget.py"
    source = path.read_text()
    original_hash = hashlib.sha256(source.encode()).hexdigest()
    changes = [
        ('    params = ready["rationalDeepModel"]["physicalParameters"]',
         '    if reference["strip_formula"] != "tau_n = max(2, 1 + (n-12)*log(2)/4); each whole cell uses its stated constant strip":\n'
         '        raise ValueError("The reference is not the certified plateau2 space")\n'
         '    params = ready["rationalDeepModel"]["physicalParameters"]'),
        ('        rows.append(dict(cell=n, canonical_total_envelope=X, B=B, Q_coefficient=a,',
         '        rows.append(dict(cell=n, certified_reference_tau=max(arb(2),1+(n-12)*ln2/4), canonical_total_envelope=X, B=B, Q_coefficient=a,'),
        ('            reference_tau=1+i*ln2/4, minimum_strip_buffer=sigma,',
         '            reference_tau=r["certified_reference_tau"], minimum_strip_buffer=sigma,'),
        ('        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in',
         '        adapter_sha256=_plateau_adapter_hash, base_density_sha256=_base_density_hash,\n'
         '        reference_policy="The true plateau2 low box; the continuous analysis strip uses the original rising ceilings.",\n'
         '        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in')]
    for before, after in changes:
        if source.count(before) != 1:
            raise ValueError("The original density proof anchor changed")
        source = source.replace(before,after)
    module = types.ModuleType("tail_plateau2_density")
    module.__file__ = str(path)
    module.__dict__.update(_plateau_adapter_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                           _base_density_hash=original_hash)
    exec(compile(source,str(path),"exec"),module.__dict__)
    module.main()


if __name__ == "__main__":
    main()
