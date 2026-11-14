# Actual circle probe: increase field resolution, not only angle quadrature

Public Actions run `43587375529`, job `132424691588`, returned artifact
`14110971053` (`visible-mainline-circleprobe-43587375529-1`).  The report
`material-circle-domain-probe.json.gz` has SHA-256
`da10825ea0062b856b69bc09f1e44c6fc0860d4c680fb1a8f4a4a88352f7219f`.
The complete five-case probe took `2.44821922700001` seconds.

It retained the complete original 96-mode core and the same zero-control
scalar function.  It tested 16 selected actual bad/representative
turn, coast and bridge intervals, with both original RMS fractions and
the midpoint in each: **48 queries per case**, not a complete new mesh
preflight or a continuous domain bound.  Replaying the saved original RHS
gave maximum difference exactly `0.0`; its saved Hermite curve had 25 bad
queries and minimum beta squared `-0.14619094124759857` on this selection.

| Field M | Angle N | Bad / 48 original-RHS Hermite queries | Minimum beta squared | Maximum endpoint nonmean height RHS | Maximum unit-circle curvature error |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 96 | 1024 | 25 | -0.146190944924 | 1.10770567130e-2 | 2.33129221090e-3 |
| 96 | 2048 | 26 | -0.211658175307 | 1.10770811576e-2 | 2.33129218729e-3 |
| 112 | 2048 | 0 | 5.08594680423e-3 | 1.06863335181e-7 | 2.64286835572e-6 |
| 128 | 2048 | 0 | 4.91991266345e-3 | 3.82904335756e-7 | 2.15049472230e-6 |
| 160 | 4096 | 0 | 4.98154031063e-3 | 1.56837922317e-7 | 4.39718568335e-7 |

At fixed `M=96`, changing the projection quadrature from 1024 to 2048
changed its circle coefficients by at most `4.1700341892003014e-17`.
Its relative angular metric error stayed about `3.5460392e-6`, and its
curvature error about `2.3312922e-3`.  The finer angular grid exposes
additional/worse bad points; it does not cure the finite-field error.
This is consistent with the exact coast Hermite identity in
[R247](../results/R247-affine-coast-hermite-midpoint-blindness.md).

The complete analytic-circle Hermite reference had minimum beta squared
`0.005153113626780614`.  It is a separate untruncated reference, not a
replacement for the original finite RHS in the table.

The report also keeps **all sampled even height-velocity frequencies**,
including those above each field cutoff.  Passing the selected domain
queries does not make that omitted velocity vanish: at the late bridge,
for example, `M=112/N=2048` still has a sampled velocity mode above M of
about `2.89e-6`, with maximum second-angular weighted amplitude about
`0.2265`.  Higher M does not give monotone improvements in every retained
RHS coefficient.  Neither a full metric estimate nor a complete angular
tail certificate follows from this short probe.

## Selected next actual coupled problem

Use the smallest tested passing field resolution, `M=T=112`, with
`N=2048`, as a new original-equation full-DN attempt.  Retain the original
accepted M96/N1024 prefix's identity and scalar function.  Its complete
states, full mean height, RHS and core coefficients are embedded as a
**warm initial guess**, with all added coefficients initially zero in the
prefix.  The extension's finite material-circle projection is recomputed
at M112; it is not asserted to be a solved extension.

The new full problem retains all 112 physical Fourier modes and all 112
material DN rows.  Three low core coefficients remain fixed, modes
4–112 are free, and the same three actual prefix scalar controls remain.
There are `3*112+2=338` physical rows, 112 constant core rows and three
constant control rows: 453 unknown states, with 341 left and 112 right
boundary rows.  Rank remains an actual calculation.

The new scalar schema must store `base_prefix_M=96`, `field_modes=112`,
`tail_modes=112`, all three control supports/polynomials and source
hashes separately.  Reconstructing it as `T=112` minus a design `M=96`
would incorrectly manufacture 19 controls, so that interpretation is
forbidden.  The full original mesh and all actual RMS queries must pass
the new preflight before QR is attempted.

A new T112/N2048 zero-height response, complete Jacobian and audit must
be computed from the original public native solver.  The completed T96
response cannot serve as that anchor.  Original domain, full-J, boundary,
Newton, line-search, RMS and final true-tail audit gates remain intact.
This note records a selected new computation, not its acceptance.
