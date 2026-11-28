# Complete physical normal on the admissible suffix of radius parameters

**Numerical evidence.**

An actual 18,480-row, 125-column fixture restricted the eight stored log-radius coefficients to five free ones (first three locked), leaving all 120 Cartesian coefficients active. The assembled principal normal matched explicit JᵀJ + λS to 3.19865e-16 relative, Cartesian/radius cross block to 2.86952e-16, and the independently evaluated normal solve residual was 8.64742e-16.

For injection P selecting every Cartesian column and suffix radius columns, the restricted derivative is JP, its transpose is PᵀJᵀ, and the increment penalty is PᵀSP. Compress the unscaled lower band to the ordered free indices before the final diagonal scaling and band Cholesky. For free pair (i,j), the old band entry is indexed by (keep[i]−keep[j],keep[j]). Outside the old bandwidth the entry is zero. This retains Cartesian cross terms and restricted radial H². Repeated SPD factorization of the larger normal is an implementation cost.

The fixture has 33 radii and 16+24 physical angles, nonzero free alpha, and 332 nonzero area-radius packet entries in the original full derivative. Radius-block relative error 1.74066e-16, step relative to direct dense solve 2.87915e-15. The XYZ-only, radius-only and joint actual derivative and FD direction checks are saved in the output.

In production the planned 51 locked and 36 free radius coefficients leave 12,825 free columns. This small fixture validates the principal-normal algebra. It contributes zero nonlinear accepts or geometric certificates.

## Reproduction

Set S to the topic scripts directory and W to the separate run directory. Use the G10 complete-source and four-baseline recipe and preceding steps for the prepared sources and states. For the small operator check use the preceding extended prepared source from the local log-radius audit. Place the cited scripts in W. All commands below have an actual natural exit 0.

```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 -u $W/2ecf-polar-restricted-radius-local-check.py --scripts $S --prepared $W/polar-c2-extended-prepared.json --output $W/polar-restricted-radius-local.json
```

## SHA-256

- `2ecf-polar-restricted-radius-operator.py`  `f58b11a6de42c9d17c8d50a092c88e7c98488d425aacd7964435a139fae2cc22`.
- `2ecf-polar-restricted-radius-local-check.py`  `033ff26e5787e6edbfda548dfb25f2e5ff034b505439e7eb205c23f11ef154d9`.
- `polar-restricted-radius-local.json`  `e3786a0012cc67b22d1cb43153d816d7d9bb7da6cc4e57613067eaaa9d400f14`.
