# R133 complete scalar model: actual attempts and scope

2026-11-14, phase_inverse.

The successful high-order producer is
`scripts/fourfold_codazzi_phase_complete_Arb_high_scalar_jets.py` with
`scripts/fourfold_codazzi_phase_Arb_high_Taylor_cache.py`.
The complete first-germ native is the distinct corrected output
`2026-11-14-R133-complete-Arb-high-scalar-Taylor-first-germ-native.json.gz`.
Its internal configuration binds both source SHA256 values, the exact
target, fixed nu/eta, requested degree seven, precision, and every
adaptive setting. Only that output is used for the proved numerical
first-germ result.

1. The first scratch Laurent prototype attempted division of an
   `arb_poly` by an integer. python-flint does not implement that
   operation. It was changed to multiplication by the Arb reciprocal;
   the failed source identity and traceback remain in scratch attempt01.
2. Complete point evaluations using one-sided formal exponentials
   succeeded at r=.1 and overlapped every common scalar jet of the
   original complete provider. The more precise arbitrary-order source
   subsequently caches the exact degree20 input polynomials before
   evaluating radial boxes.
3. A requested interval [1/10,100001/1000000] was rejected because it
   crosses an actual dyadic scalar knot. That rejection is preserved;
   it is not a numerical target failure. The independent genuine
   near-root interval [23839/100000,2383901/10000000] passed and
   overlapped every common lower-order original-provider jet.
4. The valid complete degree-three model on the first true germ needed
   64 cells and 140.63 seconds at the requested global scalar budget
   2^-42. This was computationally too expensive for the whole flow
   cover, so the derivative order was raised without changing the
   underlying target or reducing the error requirement.
5. The first degree-seven cache prototype formed sqrt(-K) with an
   explicit series precision8 while the *global* Arb series cap was6.
   python-flint truncates arithmetic to the global cap, so q6 and q7
   were missing. Every output in scratch
   `phase-scalar-cache-20261114/high7-pilot01` is invalidated by its
   `INVALID.json`; none is used or assigned a proof. The saved faulty
   source is `phase-next-20261114/scalar-high7-attempt01-invalid-source.py`.
   The corrected source raises the cap and checks `q.prec>=order+1`.
6. A fresh corrected run in `high7-pilot02` completed the whole first
   germ with two cells, six passed gates, integrated complete scalar
   error <9.117418e-17, germ-loop wall time24.19seconds, and complete
   invocation time26.49seconds including initialization. Its whole-cell
   rejected attempt remains in the successful native, followed by the
   two accepted exact halves.

The prototype source files and intermediates are not alternative
certificates. The current proof includes the entire exponential and
primitive-tail argument and the exact Taylor remainder. The first
germ is complete; the remaining168 genuine target/control germs,
full characteristic evolution, conjugacy residual, phase arithmetic,
and complete body inverse are not claimed by this note.
