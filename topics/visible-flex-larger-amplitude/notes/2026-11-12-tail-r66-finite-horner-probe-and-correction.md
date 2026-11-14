# Finite integer Horner: complete same-leaf correction

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

**Proved scope:** a finite implementation of the same R48 quartic gives a much tighter complete-angle interval residual on the original segment 7 witness. It changes only its enclosure. It does not yet give a new whole-segment maximum or solve the outer radial boundary problem.

The original implementation issue and the continued validity of its finite original-basis bounds are recorded in [the correction](2026-11-12-tail-r66-centered-power-correction.md). Original executable sources, original primary data, and original execution records are preserved.

## 1. Finite enclosure of the exact same polynomial

For the fixed R48 quartic $k(u)=\sum_{i=0}^4 a_i u^i$, put $t=\operatorname{mid}(I)$ and $v=u-t$. Its shifted coefficients are exactly

$$
b_j=\sum_{i=j}^4\binom{i}{j}a_i t^{i-j}.
$$

The v2 helper computes $t^n$ by $n$ repeated interval multiplications, starting from 1. It evaluates the shifted polynomial by the recurrence

$$
z_4=b_4,\qquad z_j=b_j+v z_{j+1}\quad(j=3,2,1,0).
$$

Induction gives $z_0=\sum_{j=0}^4b_jv^j$ for every fixed choice of the exact enclosed coefficients and every $u\in I$. Directed interval multiplication and addition therefore enclose the entire same polynomial, even when $v$ changes sign. The derivative is treated as the degree-three polynomial with coefficients $(a_1,2a_2,3a_3,4a_4)$, then multiplied by the original exact $u_x$. This avoids a general real-power operation on a signed interval.

Both inputs and output of every new intersection must be finite; otherwise the computation stops with an explicit exception. Intersecting this finite enclosure with the old finite five-basis enclosure is legitimate because both contain the same exact polynomial. Repeated uses of the same exact endpoint or bubble constant may widen the result but cannot remove a true value. All true R48 integrals, shared physical two-jets, modes, background, and the height primitive are unchanged.

The finite-mean and full-$J$ machinery is also unchanged. The adapter recovers the original diagnostic source exactly on reversing its recorded substitutions. The original 30 rational basis/derivative identities remain, and the executable additionally checks the finite signed-interval recurrence and rejection of a deliberately nonfinite intersection argument.

## 2. Formal six-case calculation

Original comparison session **24039**: tool and wait4 exit 0, 3.654759407043457 s, peak 31696 KiB. Finite-Horner comparison session **61369**: tool and wait4 exit 0, 6.564970016479492 s, peak 31620 KiB. Both preserve the original complete positive bin primitive enclosure and radius enclosure; neither computes a new source integral or radial ODE.

The original witness is $I=[1/256,1/128]$ in original segment 7, substage 0, bin 0. Its midpoint is $3/512$. Every table entry is a strict outward decimal bound from the recorded exact dyadic endpoint.

| Set | Original five-basis full-angle physical defect | Finite integer-Horner full-angle physical defect |
|---|---:|---:|
| Entire $I$ | $<0.760858$ | $<0.00710530$ |
| Left half | $<0.376707$ | $<0.00318689$ |
| Right half | $<0.338199$ | $<0.00392974$ |
| Left endpoint | $<0.000568380$ | $<0.000568380$ |
| Midpoint | $<0.000711283$ | $<0.000711283$ |
| Right endpoint | $<0.000772304$ | $<0.000772304$ |

The two closed halves cover $I$, so together they prove a complete **whole-witness** bound $<0.00392974$. This conclusion comes from two interval calculations, not interpolation between three point samples. The original quartic derivative coefficient enclosure on the whole witness was approximately $k_{2,x}\in[-0.0191,0.0191]$; the finite recurrence reduces it to an enclosure contained in $[-7.74,7.74]\,10^{-5}$. The actual point derivatives remain exactly the same enclosed quantities.

The whole-witness contribution from modes above the stored height cutoff 40 is below $3.844509\,10^{-17}$. All residual modes through 80 and the complete scalar mean/mean derivative remain in the main total. No tail of the finite residual polynomial is discarded.

There is also a true nonzero point residual: the complete cosine-mode-2 interval yields the rigorous lower bounds $>0.000252988$, $>0.000298601$, and $>0.000303539$ on the angular supremum of the physical defect at the three respective points. For a real even function, its complex Fourier coefficient at mode 2 is half its cosine coefficient, and its absolute value does not exceed the angular supremum; this is the factor used. These lower bounds establish that the candidate is not the exact outer solution. They do not estimate the eventual correction after applying an outer Green/Schur inverse.

## 3. Continuation and preserved limits

The complete segment 7 v2 run is separate and has its own plan, fresh streams and formal resource record. The old whole-segment and complete-cell bounds remain the available continuous bounds until that run and the same-candidate composition finish. Neither targeted improvement changes the candidate, the common metric, the inner exact family, or the outer existence obligations.

Sources are `tail_outer_centered_quartic_fields_v2.py`, `tail_outer_substage_quartic_diagnostic_v2.py`, and `tail_outer_centered_span_refinement_v2.py`. The first is the finite helper; the latter two are narrow reversible adapters. No MJS is changed.
