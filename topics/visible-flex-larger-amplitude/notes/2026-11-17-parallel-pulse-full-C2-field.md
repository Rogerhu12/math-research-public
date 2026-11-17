# Pulse scalar: actual C² bridge, interior metric defect, and finite extension stop

This is a new explicit map with the fixed A=−5,w=.005 scalar of [the six-case pulse experiment](2026-11-17-parallel-inward-curvature-pulse.md). It is not an accepted full BVP, a closed surface or completed fixed-g refinement.

## Whole new segment, not just the endpoint

M320/N4096 integrates all962 equations from the original accepted .995 parent to1.0 with rtol1e−13, atol1e−16 and max/first step1/64000. Of322 accepted integrator nodes, the declared existing64ulp terminal policy removes only .9999999999999883, retaining the actual1.0 endpoint and its jets. The321 remaining nodes define320 genuine quintic cells.

The [new wrapper](2026-11-17-parallel-pulse-common-jet-field.py) explicitly supplies PulseProfile both to the nodal integrator and the geometry reader; the old unpulsed profile factory is never used to read this map. It applies exactly the R637 Hermite correction on the first32 cells, width .0004999999999988347. The original saved first jet is checked equal to its recomputation, the first0/1/2 jets are shared with the old prefix, and every jet from the join node onward is unchanged. Finite angular Fourier sums and shared exact-real binary nodal data therefore give all six Cartesian C² seam jets. This explicitly modified map is not the raw IVP itself.

All320 cells,8192 angles and4 subdivisions per cell give13,107,200 samples:

| quantity | actual sampled value |
|---|---:|
| max relative Gram operator | **1.3124250390406716e−6** |
| location | s=.998871093749991, phi=.43104860139586515, cell247,u=.75 |
| rr / mixed / angular there | −4.7548836868e−8 /3.3837176792e−8 /−1.3115198481e−6 |
| max absolute principal curvature |6.982223448658665, at s=1.0 |
| minimum Q / W / H |.0376247802247 /7.5131293407e−5 /6.9633904356e−5 |
| minimum actual Gram determinant |.037624781524398285 |
| max sampled position norm |1.756365780756234 |
| minimum sampled old-core witness distance |.9623137591415504 |
| old-cut first / second jump |0 /0 |

Thus endpoint Gram8.173e−7 does **not** establish the whole-segment1e−6 gate: the actual interior exceeds it. The old prefix remains unchanged; its previously sampled4.001e−7 is not a new uniform common-grid read. No continuous angular/radial bound, all-t family, closed tail, diameter, held set or reach follows.

## Same scalar, longer IVP request

The unchanged A=−5,w=.005 scalar and original start were integrated toward1.01 with the same finite settings. It stopped on Q/W/H domain evaluation after598 accepted nodes and7295 RHS calls; last accepted s=1.0039895757594532. This finite failure is not a new parent or proof of mathematical nonextendability; no smaller-step scan is claimed.

## Reproduction and identities

With S=this topic's scripts directory, PYTHONDONTWRITEBYTECODE=1 and BLAS/OMP threads1:

```sh
PYTHONPATH="$S" python "$S/../notes/2026-11-17-parallel-pulse-common-jet-field.py" --reference parallel-continue0995-m112.json.gz --metric parallel-inward0997-m112.json.gz --amplitude -5 --half-width .005 --end 1.0 --output-stem parallel-pulse-a5-fullfield
PYTHONPATH="$S" python "$S/../notes/2026-11-17-parallel-inward-curvature-pulse.py" --reference parallel-continue0995-m112.json.gz --metric parallel-inward0997-m112.json.gz --amplitudes -5 --half-width .005 --end 1.01 --out parallel-inward-negative-pulse-extend101.json
```

SHA256: wrapper `7525fe7713078ec09f1b2096f96c5df2920cb32c3fcfda80a0038a4f866bce4e`; frozen reader `ed0de0d513f28e1d227ba4f49a2ac2b2379107ca200c50f0d43f933e0edfd924`; frozen pulse `148dd6305df67c881ceb180249f4eaf34e3a996a6568c7378be467d41a92d157`. Parent/carrier are exactly those in the pulse note. Raw scratch final local field `94c59bb204c7b3b3c584912a52980f9320b2d4e82febd3b2fb1c1870c9c57a31`; actual C² bridge `381de9825a713e301787ef67f0d694e288bea2e920d6b269b9240e90e9d3851a`; full readout `224b3eab9f4e0921620dc7f6061cc17293d4b4904c3686b7ef41df193bfff0b8`; longer failed-IVP report `7ec1c558560fc1e4edbfb9cc56f2860c2b1368183d9c1ede6df32f29bd699d2d`. The helper's initial progress hash precedes the wrapper's explicit pulse metadata; these final identities are the authoritative ones.
