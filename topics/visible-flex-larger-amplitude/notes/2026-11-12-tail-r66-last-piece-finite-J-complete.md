# R66 application: complete finite-J bound for the same physical-radius last piece

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

**Proved scope:** the previously defined physical-radius R48 candidate on original cell 0, segment 8 has full-angle physical Darboux defect less than **0.02629675** over its complete radial interval. Its original R64 bound was $0.253539306$. Both refer to the same exact candidate and the same metric; the new calculation retains all finite residual frequencies and uses a finite integer-Horner enclosure of the actual candidate derivatives.

The new complete cell 0 composition has bound less than **0.193211** on **7563 continuous intervals**, with its largest remaining component in original segment 3. This is still a candidate defect bound, not an outer existence, Green/Schur, or curvature certificate.

## 1. Identity of the physical-radius candidate

The input is the complete `2026-11-12-tail-outer-cell0-last-physical-r-r1.json` candidate. Its true left radius is near $0.2996355065640876643$, and its right endpoint is the previously paid actual $R_{\rm out}$ near $0.3000000000000071591$, rather than binary 0.3. Its width is the same positive real integral, enclosed near $0.0003644934359194948$.

Write

$$
u=\frac{r-r_L}{r_R-r_L}.
$$

The old five exact R48 positive moments are integrals against the **same true** $w(r)\,dr$. Their saved interval boxes are read without selecting any midpoint. The normalized endpoint jets are reconstructed from the same shared physical two-jets, true width and endpoint $w,w_r$. The unique bubble coefficients are intersected with the original saved enclosures. Consequently the exact polynomial and height primitive are unchanged even though interval representations may be slightly different.

The original complete background, node and source hashes are checked, including the real R31 background curvature ledger. The same whole-piece $w$ range and its original $w_r$ intersection with that ledger are reused. No new source profile is evaluated, no true integral is redefined, and no source quadrature or radial ODE is performed.

## 2. Complete mean, actual derivatives and all finite frequencies

Sixteen closed physical-$u$ intervals cover $[0,1]$ without gaps. Positive integral monotonicity gives the original before/after primitive boxes on each interval. The [finite integer-Horner lemma](2026-11-12-tail-r66-finite-horner-probe-and-correction.md) encloses the actual normalized slope polynomial and its actual derivative. The source variable for R64 is now exactly $x=r$, so

$$
r_x=1,\qquad \ell=\frac{w_r}{w},\qquad
k_r=\frac{k_u}{r_R-r_L}.
$$

The full R64 scalar mean and its actual derivative are paid on each interval. No ODE right-hand side is substituted for $k_r$ or for a second height derivative.

All cosine coefficients of the exact finite polynomial $J$ through $m=80$ are retained. The physical formula is

$$
\mathscr D=\frac{w^2}{rE^2}J,
$$

with no additional original source-speed factor. The coefficient absolute sum bounds every real angle. The complete mean and its radial derivative are included in $J$.

## 3. Actual completed calculation

Session **6972** completed with tool and wait4 exit code **0**, no termination signal, wall time **3.026000738143921 s**, and peak RSS **30172 KiB**. All six candidate/coverage/complete-mean/full-frequency gates are true.

The complete-angle physical defect satisfies

$$
\sup|\mathscr D|<0.02629675.
$$

The largest recorded interval is $u\in[15/16,1]$. On the same unchanged candidate, the original-style R64 scalar norm bound after finite polynomial enclosure is $<0.08213188$; the complete signed finite spectrum yields the tighter bound above. The complete contribution beyond the saved height cutoff 40 is less than $6.637886\,10^{-14}$. Thus the result does not arise from discarding generated frequencies.

The actual nonmean second height derivative has the recorded $W^1_{1/64}$ bound $<0.314490$. This is a height-jet bound on the candidate; no principal-curvature interpretation is made.

## 4. Exact stored-data composition

The standard-library composition was executed immediately after the numerical audit. Its resource record has exit **0**, no signal, wall time **0.4889683723449707 s**, and peak RSS **13096 KiB**. The tool returned completion directly, without a persistent session identifier. All seven checks passed.

It verifies the identical candidate SHA, all input/source hashes, the exact complete physical-radius interval cover, every finite residual mode, and the strictly positive saved mean/domain margins. It then replaces only segment 8's physical bound in the prior complete cell composition. The other eight component candidates and bounds are unchanged.

The resulting largest bound is in segment 3 and equals the exact dyadic

$$
2425605235243691386290210419391614505518096891472969797169\,2^{-193}
<0.193211.
$$

The cover remains 7563 intervals. The next two largest component bounds are segment 5 below $0.192327$ and segment 1 below $0.111805$. The original complete mean height convention and one additive constant are preserved. No coordinate residuals are mixed with physical quantities, and no geometry is recomputed by this composition.

Primary records are `2026-11-12-tail-outer-cell0-last-physical-r-finite-J-r2.json.gz` and `2026-11-12-tail-outer-cell0-components-3578-horner-r2.json`, with their resource files. The old physical-radius construction and its original primary packet remain unchanged.
