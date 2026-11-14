# R133 supplement: a whole-positive reference floor and the actual cached coefficient producer

2026-11-14, phase_inverse.

**Proved and actually checked:** 11 new exact rational gates give the
whole-positive intrinsic curvature floor, the fixed interface with the
paid root block, and a complete all-frequency Riccati frame bound 5.

**Implemented but not executed in the unavailable native runtime:**
the new complete moving-field producer and its full high-block consumer.
There is no new successful whole-positive coefficient report or
whole-positive inverse in this result. The consumer grants that inverse
only when the actual complete native coefficients and its stated
Volterra gate have both passed.

The centre is the final complete moving candidate
\[
 \mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413},
\]
with \(M_c=32\), whole original \(|\eta|\le10^{-9}\), and the actual
compact metric parameter
\(\nu=-2572625729470897/72057594037927936\).
Only unchanged intrinsic data outside the support of the metric bump
are reused. No amplitude-\(.75\) nonradial coefficient is imported.

## 1. A fixed cut inside every already paid root block

Set
\[
 r_b=0.2384058742994,\qquad R=25/8,\qquad
 r_*^-=0.2383968742994,\quad r_*^+=0.2383968743003 .
                                                               \tag{C.1}
\]
The actual root lies in \([r_*^-,r_*^+]\), and the paid root block
has length \(h=9/10^6\). The exact identities and inequalities are
\[
 r_b=r_*^-+h,\qquad r_*^+<r_b\le r_*(\eta)+h,\qquad
 r_b-r_*^+>8999/10^9 .                                  \tag{C.2}
\]
The interval from the true root to \(r_b\) stays in the proved
joint complex germ and actual candidate piece 2549.

The existing root inverse may be restricted to
\([r_*(\eta),r_b]\) in the **same full global Riccati reference**.
Its diagonal Green bounds use an upper bound on interval length;
the coefficient, source, head-feedback and trace bounds therefore
remain valid with the old length \(h\). The global reference at the
true root is unchanged. In particular one need not rebuild a
different Robin reference just because the right local cut is
now fixed. There is no domain gap or curved-cut identification
in this interface.

The required actual inputs are:

* [current moving physical complex germ](R133-supplement-current-moving-body-physical-complex-germ.md),
  blob \(\mathtt{bfe73ee59142618bc7e36d5e3fe06929d9fb68cb}\);
* [current root Riccati inverse](R133-supplement-current-moving-positive-root-Riccati-and-full-head.md),
  blob \(\mathtt{3edf335784786da9a4a515b28d364d8ad2914e24}\);
* [the single global positive reference](R133-supplement-global-positive-reference-and-current-collar.md),
  blob \(\mathtt{5e89a2ec36f36f2852d47738bc46373fdacf67d1}\).

## 2. A true curvature floor on the entire remaining positive interval

On the actual joint root germ,
\(K'>59.74380437\). Thus
\[
 K(r_b)>
 59.74380437\,(r_b-r_*^+)
 =\frac{537694185560576067}{10^{21}}
 >\frac1{2000}.                                         \tag{C.3}
\]
This estimate uses the whole root enclosure, not a numerical
root midpoint.

The full compact metric type theorem, blob
\(\mathtt{15de90fc2e61c0d15df47a1a636675c8f0397122}\),
proves \(K'>46.2850369150182\) on the complete closed cover of
\([.238,.239]\), across its true scalar seams.
Consequently \(K\) stays above (C.3) up to .239.
The complete 1,334-box actual rotational cap certificate,
blob \(\mathtt{1f0c66859862fbe6280fdce466f98dd10cc4a17f}\),
then gives
\[
                   .02679531<K<3.45006391
             \quad\hbox{on }[.239,25/8].
\]
The same type theorem gives the small positive upper endpoint
at .239. Hence the complete true interval satisfies
\[
             \boxed{\quad 1/2000<K(r)<4
                         \quad(r_b\le r\le25/8).\quad} \tag{C.4}
\]
The compact \(\nu\) bump is exactly zero throughout this interval.
Only the same intrinsic target is used in (C.4); no nonlinear
candidate sign or derivative has been deduced from these intrinsic
numbers.

## 3. The global reference has a uniform denominator and frame

Use the same reference as the local root and actual exterior:
\[
\begin{split}
 (g_M)_r&=M a(r)(K-g_M^2),
       &g_M(r_*)&=M^{-1/3},\\
 (p_M)_r&=M a(r)(p_M^2-K),
       &p_M(R)&=p_*\in(1/8,1/5),
\end{split}                                                        \tag{C.5}
\]
where \(a(r)>0\) is frequency independent. For the eventual actual
body it must be \(a=-\gamma\langle v\rangle\). Until that whole-body
sign is certified, (C.5) is a reference for an arbitrary positive
bounded extension of the already paid root speed.

Backward scalar comparison from \(R\), with (C.4), gives
\[
       p_M(r)\ge\sqrt{1/2000}>1/45
             \qquad (r_b\le r\le R).                    \tag{C.6}
\]
Indeed the backward vector field is \(Ma(K-p^2)\), nonnegative
at the barrier \(p=\sqrt{1/2000}\), and \(p_*>1/8\) is above
that barrier. The global upper bounds are still \(p_M,g_M<2\).
Therefore
\[
           1/45<W_M:=p_M+g_M<4 .                        \tag{C.7}
\]
These are all-frequency bounds; they are not finite-mode
Riccati samples.

Set
\[
 T_M=W_M^{-1/2}
       \begin{pmatrix}p_M&-g_M\\1&1\end{pmatrix},
 \qquad Z_k=M^{1/6}T_M^{-1}S_\sigma z_k,\quad
 S_\sigma=\operatorname{diag}(-i\sigma,1).
\]
The comparison of \(T_M\) with
\(D_M=\operatorname{diag}(W_M^{-1/2},W_M^{1/2})\) has both
norms \(<2\). For \(M\ge388\), (C.7) then gives
\[
 \|M^{1/6}T_M^{-1}S_\sigma f\|_{\ell^2}
                   <5\|f\|_{H^{1/3}_\phi},\qquad
 \|z\|_2<5\|Z\|_2 .                                    \tag{C.8}
\]
The complete exact numerical check is
\[
                       64\cdot45^3<5^6\cdot388 .
\]
For one additional angular derivative, homogeneous canonical
weights are converted back to Bessel \(H^1\) by a factor at most
\(\sqrt{1+388^{-2}}\); a sufficient raw reconstruction constant
is \(50001/10000\).

Equations (C.6)–(C.8) are useful even before native fields return:
the remaining positive interval has no hidden root-distance
factor in its source or reconstruction frame. They do not bound
the actual nonradial coefficient remainder or certify
\(a=-\gamma m>0\) on that interval.

## 4. Complete actual coefficient production

The new source is
[scripts/fourfold_codazzi_current_positive_complete_coefficients.py](../scripts/fourfold_codazzi_current_positive_complete_coefficients.py).

Its required input is the complete candidate index supplied with
the --candidate option; no new large candidate copy is created.
By default it requires the exact ac1d SHA above. The current
reconstruction chain already identifies all five candidate shards.
Their individual SHA values, polynomial shapes, adjacent exact
dyadic nodes and finite coefficients are checked by the existing
complete shard loader.

The producer reads the actual moving-coordinate string from the
existing finite-system source and requires the same metadata.
It then uses the exact definitions
\[
 u=\alpha U_{\sin}(\phi),\quad
 v=s+\alpha V_{\cos}(\phi),\quad s=1/C_{\rm ref},\quad
 m=s+\alpha V_0.                                       \tag{C.9}
\]
It does not call these coefficients physical-\(\theta\) Fourier
coefficients.

The only reused numerical table is the complete intrinsic
cap v2 cache
\[
\begin{gathered}
\texttt{notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz},\\
\mathtt{3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22}.
\end{gathered}
\]
That table already contains all 1,334 closed boxes and all original
primitive-tail and whole-\(\eta\) fees. The new producer checks
its actual object, affine centre, interval, successful v2 status,
source identities and complete adjacent cover. It verifies
primitive positivity before taking any new quotient.

Before .239 it calls the unchanged intrinsic body provider on
each actual common scalar germ. It does not use an outer cap box
or the current narrow root germ outside its proved domain.
The independently proved interval (C.4) can be intersected with
a native \(K\) enclosure. The original native \(K\) ball is saved
alongside the intersection; a disjoint intersection is rejected.
This is an intersection of two true enclosures of the same
quantity, not replacement of an unresolved sign by a desired
sign.

The actual radial partition is the union of:

* all complete candidate PPoly knots;
* all reused intrinsic cap box endpoints;
* all true scalar-germ endpoints before .239;
* the two actual interval endpoints.

On every closed row the complete cubic is evaluated with exact
dyadic coefficients by Arb Horner arithmetic. Both sides of every
PPoly join are retained. The full \(u,v\) Fourier arrays have
indices \(-M_c,\ldots,M_c\). Products are computed by complete
finite convolution; there is no FFT grid, aliasing assumption,
or projection of a quadratic intermediate to \(M_c\).

In particular the producer calculates
\[
\begin{gathered}
 S=u^2+Kv^2,\quad d=-\beta I S,\quad
 \|d\|_{A^0},\ \|d_\phi\|_{A^0},\\
 L_0=\begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix},
\end{gathered}
\]
with every coefficient through \(2M_c\). It records the complete
field and derivative Wiener sums, local multiplication envelopes,
the full primitive term, the exact mean-rank column, the signed
mean's own rate and nonmean feedback. The actual speed
\[
                         -\gamma m>0                  \tag{C.10}
\]
must pass separately on every closed row. The stronger real
physical inverse-angle gap
\(-m-\|v-m\|_{A^0}>0\) has its own recorded flag; it is never
inferred merely from (C.10).

The code defaults to at most 64 new accepted rows per run and
atomically saves every eight rows. The --resume option only
continues an unchanged, unfinished, nonfailed checkpoint. It
verifies that the saved prefix and the entire pending partition
still cover the original requested interval without a gap.
A mathematical failure is preserved; --resume cannot overwrite
it. A process interruption can lose only the unsaved short batch,
not a saved expensive prefix.

The report's complete flag refers to the complete coefficient
cover. Its actual_high_inverse_certified and
whole_BVP_inverse_certified fields remain false. A successful
coefficient cover alone is not an inverse certificate.

## 5. Every true join and all source columns

At a candidate join \(r_i\), the intrinsic \(s(r)\) is the same
continuous true scalar function on both sides. Hence the complete
centre jump is exactly
\[
 [u,v]_{r_i}
    =\alpha\bigl([U]_{r_i},[V]_{r_i}\bigr),             \tag{C.11}
\]
computed as exact fractions from the two dyadic cubics.
The native records complete \(A^0,A^1,A^2\) jump bounds and the
exact even-mean jump. These are not set to zero because the
original approximate BVP intended continuity.

In the same moving unknown the homogeneous linear interface is
the identity. For correction of the piecewise centre, the true
affine interface source is \(-[Q_c]\). A physical-angle variable
would instead require the already identified full variation
bridge; it is not substituted here.

The reference \(p_M,g_M\) is absolutely continuous for the
piecewise bounded speed in (C.10). Therefore \(T_M\) is continuous
across the actual coefficient jumps. The raw affine jump gives
the single exact source \(M^{1/6}T_M^{-1}S_\sigma[z]\);
there is no free removal of that source or an artificial frame
jump.

Mean input and output stay in the head. The true exterior mean
row's high-to-low finite-rank path remains an external Schur
column, even though the current centre's interior coefficients
have a finite angular band. The compact metric parameter column
vanishes on this positive interval because the metric bump does;
its negative-body, waist, physical boundary and scalar Schur
equations are not deleted.

## 6. All-frequency lower Riccati comparison from closed rows

The second new source is
[scripts/fourfold_codazzi_current_positive_high_Volterra.py](../scripts/fourfold_codazzi_current_positive_high_Volterra.py).

It requires the first producer's complete true interval.
For a selected \(N\ge97\) with \(N>2M_c\), put \(M_0=4N\).
On a row of length \(\ell\), let \(K_-\) and \(a_-\) be the
actual lower endpoints. Suppose the initial lower comparison
value is \(b\ge0\). Reset
\[
                  b_0=\min(b,\sqrt{K_-}).
\]
For every \(M\ge M_0\), the true forward \(g_M\), and the true
backward \(p_M\), dominate the explicit comparison
\[
 y(t)=\sqrt{K_-}\,
 \frac{b_0+\sqrt{K_-}\tanh(M_0a_-\sqrt{K_-}\,t)}
      {\sqrt{K_-}+b_0\tanh(M_0a_-\sqrt{K_-}\,t)}.         \tag{C.12}
\]
The reason for the reset is essential: \(0\le y\le\sqrt{K_-}\),
so \(K_--y^2\ge0\), and replacing \(Ma\) by its lower bound
preserves the required vector-field inequality. One cannot do
that replacement without this sign check.

The backward sweep starts from \(p_*\ge1/8\). The forward
sweep may start from 0 at \(r_b\), since the actual global
\(g_M(r_b)\) is strictly positive. The proof (C.6) separately
improves every row's lower \(p\) to \(1/45\).
Each comparison is nondecreasing within the row, so its initial
value is a valid complete row lower bound. The code explicitly
intersects the computed endpoint with this analytic monotonicity
bound to avoid rejecting a constant comparison due solely to
outward rounding.

These two sweeps give a complete row lower bound \(w_i\) for
\(W_M(r)\), uniformly in every \(M\ge M_0\). Set
\[
                    k_i=\tfrac12M_0 a_{-,i}w_i>0 .     \tag{C.13}
\]
The actual diagonal stable evolution contracts forward by
\(\exp(-\int k)\), and the unstable evolution contracts backward
by the same bound. The exact scalar skew transport remains in
both evolutions.

## 7. The actual coefficient remainder and the complete Volterra gate

Let the row field Wiener bounds be \(U,V,U_1,V_1\), and let
\(K_+\) be its actual upper bound. Write \(A_\infty,E_\infty,
B_\infty\) for valid supremum envelopes of the local coefficients
\(a,e,b\) in
\[
                    \begin{pmatrix}a&Kb\\c&e\end{pmatrix},
                         \qquad |c|=|b|,
\]
and \(A_A,E_A,B_A\) for their complete Wiener envelopes.
Put
\[
\begin{split}
 q_i&=K_+/w_i,\\
 {\cal B}_{\infty,i}&=A_\infty+E_\infty+(q_i+4)B_\infty,\\
 {\cal B}_{A,i}&=A_A+E_A+(q_i+4)B_A,\\
 {\cal F}_i&=U_1U+K_+V_1V+q_iU_1V+4V_1U .
\end{split}                                                        \tag{C.14}
\]
These retain the exact grounded upper-right factor \(K\).
In particular a general scalar matrix norm is not multiplied by
a root singularity.

The complete centre has band \(2M_c\). For all high input and
output indices the relative frequency ratio is below 2,
and opposite signs cannot directly meet. The exact same
frequency and difference estimates of the root theorem give
\[
 E_i^{(s)}=
 (c_s+\tfrac12)\|d_\phi\|_{A^0}
       +2{\cal B}_{\infty,i}
       +\frac{8d_sM_c}{N}{\cal B}_{A,i}
       +\frac{n_s|\beta|}{N-M_c}{\cal F}_i,              \tag{C.15}
\]
with
\[
            (c_0,d_0,n_0)=(6,3,4),\qquad
            (c_1,d_1,n_1)=(18,9,8).
\]
For the primitive term its actual intermediate index is at least
\(N-M_c\); the full two coefficient convolutions and their
\(K/W,W\) factors give exactly the four terms of \({\cal F}_i\).
No angular projection is inserted inside that primitive.

Equation (C.15) concerns the finite **background** centre, but
the evolving high input remains the whole infinite Hilbert
space. It is not extended to an unknown corrected background
by assuming that the correction has the same band. A
whole-positive nonlinear neighbourhood requires its own
additional coefficient budget.

Let \(a_s(r)\), respectively \(a_u(r)\), solve the positive
scalar comparison equations
\[
 (a_s)'=E^{(s)}-k a_s,\quad a_s(r_b)=0,\qquad
 -(a_u)'=E^{(s)}-k a_u,\quad a_u(R)=0.                    \tag{C.16}
\]
Within one closed row the complete maximum is the maximum of
the two endpoint values, because the constant-coefficient
solution is monotone toward \(E_i^{(s)}/k_i\).
Define the actual computable bound
\[
                  \tau_s=\sup_r
                          \sqrt{a_s(r)^2+a_u(r)^2}.     \tag{C.17}
\]
Using the separate closed-row maxima gives a valid outward
upper bound for this supremum, including all interior points.

The stable and unstable components lie in orthogonal branch
spaces. Variation of constants therefore gives a complete
operator norm at most \(\tau_s\) on the sup-radial Hilbert
state space, with its genuine one-sided traces at joins.

For \(s=0\), the already paid full nonlinear exterior derivative
in this same reference has high reflection norm
\(\epsilon_R<2.22\,10^{-5}\).
Its head, mean and affine source columns remain independent
inputs. The actual high equation with that high exterior row
is invertible if
\[
                          \tau_0+2.22\,10^{-5}<1.       \tag{C.18}
\]
This is a bounded complete Volterra-plus-boundary operator,
so (C.18) grants its full inverse by Neumann series. The
exterior input is the exact complete graph in
[R133 final regular Hs and Riccati outer graph](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md),
blob \(\mathtt{7784d7158974d4632ca634369e55dc095e134902}\).

For \(s=1\), the consumer keeps the entire right high port
independent. It checks \(\tau_1<1\), but does not apply the
exterior nonlinear derivative to physical \(H^{7/6}\) data:
that stronger exterior window has not been granted by the
existing \(0\le s\le1\) nonlinear graph theorem.

The new source **has not executed either (C.17) or (C.18) on
a completed current coefficient table**. Its report records
success only if the requested actual gate passes. A failed
attempt saves the real failure and does not report an inverse.


### 7.1 A computable fallback cutoff from the same actual table

The consumer also gives a fully specified conservative cutoff,
rather than ending with an unspecified sufficiently large \(N\).
Let \(N_b=\max(97,2M_c+1)\). In (C.14) replace \(q_i\) by
\(45K_{+,i}\), and use \(N_b\) in (C.15). Call the maximum of
these complete row bounds \(\overline E_s\), and let
\(a_{\min}\) be the actual minimum speed from the complete
native cover. Both are strictly controlled finite numbers
once that cover has actually passed.

Choose \(N_*\) by starting from \(N_b\) and doubling until the
directed strict inequality
\[
                         N_* a_{\min}>135\overline E_s             \tag{C.21}
\]
passes. This algorithm terminates since \(a_{\min}>0\).
For every \(M\ge4N_*\), the complete diagonal damping is at
least \(k_*=2N_*a_{\min}/45\). The full coefficient remainder
is at most \(\overline E_s\): the two finite-band denominators
only improve for \(N\ge N_b\), and the universal \(K/W\) bound
was already used. Therefore
\[
 \tau_s\le\frac{\sqrt2\,\overline E_s}{k_*}
       <\frac{135\overline E_s}{4N_*a_{\min}}<\frac14 .   \tag{C.22}
\]
For the base state the paid exterior reflection still leaves
a complete resolvent below \(3/2\). With an independent
higher-order right port the same bound is valid for \(s=1\).

Since the source frame is at most 5, the complete source
column has
\[
 \|Z\|_{L^\infty_r}
 \le\frac{15}{2\sqrt{k_*}}\|f_H\|_{L^2_rH^{s+1/3}}
       +\frac32\left(\|g_H\|+
               \sum_i C_i\|[z_H]_{r_i}\|_{H^{s+1/3}}\right).
                                                               \tag{C.23}
\]
The native records the actual integer \(N_*\), its retained
head dimension \(2N_*-1\), and the directed check (C.21).
It does not claim that this conservative head is practical or
invert it. If the requested sharper \(N=97\) attempt fails,
that failure remains the report's selected-cutoff status,
while the separate conservative certificate explicitly states
its different certified cutoff.

No value of \(N_*\) for the current whole body is reported in
this document: the actual field table has not yet been run.

## 8. Full ordinary sources, jumps and retained head columns

On each row the source frame can be bounded by
\[
 C_i=\min\!\left(5,\,
       2M_0^{-1/6}\max(2,w_i^{-1/2})\right).             \tag{C.19}
\]
This maps the true ordinary \(H^{s+1/3}_\phi\) source to the
homogeneous canonical \(H^s\) state. The complete Bessel raw
reconstruction has the extra factor
\((1+M_0^{-2})^{s/2}\).

Solve the two comparisons
\[
       y_s'=C_i^2-2k_i y_s,\qquad
       -y_u'=C_i^2-2k_i y_u
\]
from zero at the corresponding endpoints, and let
\[
                         B_f=\sup_r\sqrt{y_s(r)+y_u(r)}.
\]
Cauchy--Schwarz in the actual radial variable gives the full
ordinary-source contract. If \(\chi=\tau_0+\epsilon_R<1\)
(or \(\chi=\tau_1<1\) with independent higher-order ports),
\[
 \|Z\|_{L^\infty_r\ell^2}
 \le\frac1{1-\chi}
       \left(B_f\|f_H\|_{L^2_rH^{s+1/3}_\phi}
                     +\|g_H\|+
             \sum_i C_i\|[z_H]_{r_i}\|_{H^{s+1/3}_\phi}\right).
                                                               \tag{C.20}
\]
The signed backward impulse is retained in the unstable
variation-of-constants column; its norm is bounded in the sum.
Raw \(L^2_rH^s\) follows by integrating the square of (C.19)'s
reconstruction factor. Both raw endpoints follow by the two
endpoint factors. No source radial derivative is requested.

The producer saves the actual centre jumps in \(A^1,A^2\).
They majorize \(H^{1/3}\) and \(H^{4/3}\) respectively,
so the consumer also computes the complete actual centre-jump
column. The low and mean parts of those jumps are recorded
separately and are not discarded.

The complete head/high couplings are recorded on every row.
For example, with \(\|L_0\|,\|{\cal N}\|\) the complete raw
bounds from the producer,
\[
\begin{split}
 \|{\cal A}_{HL}\|_{2\to2}
    &\le4(N-1)\|d\|_\infty+\|L_0\|+\|{\cal N}\|,\\
 \|{\cal A}_{LH}\|_{2\to2}
    &\le4(N-1)\|d\|_\infty+\|d_\phi\|_\infty
                                      +\|L_0\|+\|{\cal N}\|.
\end{split}
\]
The first output has full support through \(N-1+2M_c\),
so its actual \(H^{s+1/3}\) factor is paid explicitly.
The mean-rank part is zero on high input and has no high
output at this centre, but it is included in the entire head
generator. No finite radial or scalar parameter inverse
is inferred from these coupling bounds.

Thus even a passing (C.18) leaves the complete finite head,
its ordinary source and all exterior mean/high paths in the
global Schur problem. The nonlinear outer graph, physical
moments and negative return are not replaced by diagonal
sampled Robin rows.

## 9. Reproduction and current execution status

The exact reference-floor arithmetic is in
[scripts/fourfold_codazzi_whole_positive_reference_floor.mjs](../scripts/fourfold_codazzi_whole_positive_reference_floor.mjs).
Its complete function was actually executed in V8; all 11 gates
passed. The new report is
[notes/2026-11-14-R133-whole-positive-reference-floor-rational.json](../notes/2026-11-14-R133-whole-positive-reference-floor-rational.json).

The Python producer and consumer were written after the native
execution environment became unavailable. They have been
checked against the actual existing source interfaces and
their mathematics is specified above, but they have **not**
been run or Python-compiled in this environment. No pretend
native output is supplied for them.

The finite centre must be restored using its existing complete
ac1d reconstruction manifest. Supply that actual index path;
the command intentionally has no permanent candidate pathname.
From this topic directory, a bounded first batch is:

~~~bash
python scripts/fourfold_codazzi_current_positive_complete_coefficients.py \
  --candidate /actual/restored/ac1d-candidate.json \
  --max-rows 64 \
  --out /actual/scratch/current-positive-coefficients.json.gz
~~~

Continue the same unchanged prefix by adding --resume.
The output remains incomplete until the entire interval reaches
\(25/8\). A new native runner must provide the repository's
already used NumPy/SciPy and python-flint dependencies; the
producer itself uses complete Arb intervals and exact dyadic
candidate arithmetic.

After the producer truly completes, run a separate actual high
attempt without overwriting any earlier attempt:

~~~bash
python scripts/fourfold_codazzi_current_positive_high_Volterra.py \
  --coefficients /actual/scratch/current-positive-coefficients.json.gz \
  --cutoff 97 --order 0 \
  --out /actual/scratch/current-positive-high-N97.json.gz
~~~

The report records the complete input SHA, actual requested
interval, all-frequency cutoff, the two Riccati comparison
sweeps, a digest of every derived row, the worst complete row,
the actual full feedback and complete source/trace columns.
It records the requested high inverse only if (C.18) really passes;
the separately labelled conservative cutoff additionally requires
its executed strict check (C.21). The consumer refuses to apply
this centre's exterior graph to a different candidate SHA.
The large reproducible coefficient table remains a working
cache; these sources, exact inputs and the meaningful final
consumer output are the durable mathematical deliverables.
