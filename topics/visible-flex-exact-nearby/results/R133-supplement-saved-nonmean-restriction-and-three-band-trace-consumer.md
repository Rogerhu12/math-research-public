# R133 supplement: saved nonmean restrictions for the three-band collar trace

2026-11-15. Contract for one new scalar consumer. It reads original complete
rows and computes new interval restrictions and explicit trace coefficients.
It does not compute an unknown correction, a new Green operator, or another
mean flow.

The analytic trace theorem is
[LT](R133-supplement-finite193-middle-band-and-infinite-collar-trace.md).
The source identity and the corrected high window are exactly
[MC](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md)
and [MA](R133-supplement-actual-raw-mean-fee-and-restored-high-collar-domain.md).

## 1. The exact saved field

The original producer is
[fourfold_codazzi_correlated_head_residual_rows.py](../scripts/fourfold_codazzi_correlated_head_residual_rows.py),
blob 3af195a36ccb30630dbfcab0caef3564738ab169, 13043 bytes,
SHA256 1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07.
Its forty natural parts contain 7721 complete rows, with canonical row
payload SHA256
06fdb69708f63d27587fb91bb0760b50e23fa8d1719ed8b8903d8be6e922abe6.
The original full response has all 193 physical moving amplitudes and its
mean. The full real parameter box in the original rows is unchanged.

The field used here is the original row's
**uncorrected_response_nonmean**. Its four required subfields are
**L2_sup**, **L2_L2_radial**, **H1_sup**, and **H1_L2_radial**.
They were produced by the original complete radial-polynomial/Fourier
norm routine. They include its full finite-support coefficient errors.
The pair norm is the Euclidean $L^2$ pair norm in normalized angular
measure, and the radial integral uses $dr$.

The source identity is visible directly in the frozen producer:
row_budget lines 105--111 form $R=Dq-F_\nu$, retain the exact mean
of $R_2$, and define $R_{\rm non}=(R_1,P_\perp R_2)$; lines 125 and
137 pass exactly that pair to the norm routine. The full physical
trial is loaded without the background amplitude at lines 102--104,
whereas the background alone receives its original amplitude at
lines 97--99. No amplitude is reapplied to these residual fields.

The frozen helper
[fourfold_codazzi_correlated_radial_Fourier.py](../scripts/fourfold_codazzi_correlated_radial_Fourier.py)
has blob fcad3e31360289406466cc58fa105bb9fed19e1f,
SHA256 18de4ef746eed069a9a92ba783d54e2f394887866d60cbb286502b9c55cb17c5.
Its norms function begins at line 198. Lines 216--225 add the complete
finite-support error separately to the uniform Fourier norm and to
the radial integral, the latter with its true $\sqrt{|I_i|}$ factor.
Line 237 combines the two components by the square root of the sum
of squares. This establishes the field semantics used in (NR.1),
independently of row counts.

This is not the later **response_complete_nonmean_residual** field.
That later field includes nonnegative bounds for the exact scalar
mean-completion correction. MC explains why its resulting saved
whole-source budget can still be used as an upper bound, with its
independent raw mean separately restored.

## 2. New restrictions use two complete bounds per original row

For the complete old row $I_i$, let $U_i,V_i$ be its saved uniform
$L^2_\phi$ bound and its saved complete $L^2_{r,\phi}(I_i)$ bound.
For a new requested interval $I$, set
$$
 \lambda_i=|I\cap I_i|,\qquad
 t_i=\min\{\lambda_i U_i^2,V_i^2\}.                    \tag{NR.1}
$$
Each side is independently a bound for the restricted square integral.
The old whole-cell integral is not multiplied by
$\lambda_i/|I_i|$. No old polynomial, target, Fourier transform or
radial integral is recomputed.

The complete signed intrinsic row gives positive $K_i^-\le K\le K_i^+$.
Put
$$
 p_i^2=\max\{\sqrt{K_i^+},1/\sqrt{K_i^-}\}.
$$
Because $P=\operatorname{diag}(K^{-1/4},K^{1/4})$ is radial,
$$
 \|P R_{\rm raw,nonmean}\|_{L^2(I)}^2
                \le \sum_i p_i^2t_i.                 \tag{NR.2}
$$
The same construction with the saved inhomogeneous $H^1$ fields gives
a complete angular-derivative bound. Independently the full output
support is at most degree 160, whose maximum physical frequency is
640. Therefore
$$
 N_I=\left(\sum_i p_i^2t_i\right)^{1/2},\qquad
 N_{I,\phi}\le\min\{640N_I,N_{I,H^1}\}.                \tag{NR.3}
$$
All these quantities concern the original nonmean residual. The
independent raw mean is copied only from the already successful MC
receipt; it is not recomputed in this consumer.

The new domains are exactly $[17/20,19/20]$ and
$$
 I_*=[589819/655360,589829/655360]
       =[9/10-2^{-17},9/10+2^{-17}].                  \tag{NR.4}
$$
They use respectively 140 and two intersecting original closed rows.
The full forty-part identity and complete radial coverage are checked
before either restriction. The larger window is a distinct new bound;
it is not substituted into a formula requiring the narrow window's
source normalization.

## 3. Complete repair and continuity fees

Let $R_{\rm rep}$ be the original complete global upper bound in
**complete_repair_source_sup.complete_repair**. It includes both the
centre operator change and the parameter-source change in the original
complete pair units.

As proved in MC.5--MC.8, the original operator fee uses an enlarged
$H_0$ and nonnegative coefficients. It therefore bounds
$\Delta A\,q_{\rm raw}$ as well as the originally considered
mean-completed input. This majorant argument does not require a
new term $\Delta A\,e_{\rm mean}$ on top of the same fee.

Let $R_{\rm cont}$ be the unchanged retained-case
**response_offset_sup**, the complete
$E_Z(384C_1+C_0)$ fee for the canonical piecewise constant continuity
repair. Its ordinary radial derivative is zero on each piece and
its exact jumps cancel those of the original response. These true
interfaces are the same ones used by MC.

Using the retained complete $p_I=\sup_I\|P\|$ upper bound, set
$$
 R_I=p_I\sqrt{|I_*|}(R_{\rm rep}+R_{\rm cont}),\qquad
 S_{\rm loc}=N_{I_*}+R_I,\quad
 S_{\rm loc,\phi}=N_{I_*,\phi}+640R_I .                \tag{NR.5}
$$
For these fees the actual support remains at most 160: the original
and repaired centres both have degree 32, while $q_{\rm raw}$ and
$e_{\rm cont}$ have degree 96. Every linearized cubic operator term
therefore has degree at most $96+2\cdot32=160$; primitives preserve
support and rank mean outputs have smaller degree. The intrinsic
parameter-source difference has degree at most 96 and is identically
zero on this collar outside its compact bump. The full sup fee remains
a valid upper bound there. Thus the physical factor $640$ in (NR.5)
is justified for both repair and continuity terms. No $\alpha$ is
applied to the raw physical response.

The old retained **S0** is used with its MC meaning, a complete
upper bound for $Pb_0$, where $b_0=s_0+r_0e_2$. It is used here only
as a complete upper bound for $H_{96}Pb_0$. This same projected source
has maximum physical frequency 640, which is the reason for
$S_{96,\phi}\le640S_{96}$ below. Hence both arguments of
each following minimum are complete bounds for the same projected
source:
$$
 S_{96}=\min\{S_{\rm loc},S_{0,\rm old}\},\qquad
 S_{96,\phi}=\min\{S_{\rm loc,\phi},640S_{96}\}.
                                                               \tag{NR.6}
$$
There is no subtraction of two interval upper bounds.

## 4. Known source in the middle band and above 288

Keep the exact identity
$$
 f_\delta=f_0-\delta b_0+\delta r_0e_2
              -\delta^2T_2-\delta^3T_3 .
$$
The original degree-32 centre makes $f_0$ degree at most 96.
The selected reference has full degree at most 96 and its complete
residual has degree at most 288. The original normalized $T_2,T_3$
bounds for the same $I_*$ are copied, not recomputed.

For $d=10^{-10}$ the new known source terms are
$$
\begin{aligned}
 F_{96}^{\rm known}
 &\le dS_{96}+d^2T_{2,I_*}+d^3T_{3,I_*},\\
 F_{96,\phi}^{\rm known}
 &\le dS_{96,\phi}+896d^2T_{2,I_*}+1152d^3T_{3,I_*},\\
 F_{288}^{\rm known}&=F_{288,\phi}^{\rm known}=0 .
\end{aligned}                                                   \tag{NR.7}
$$
The last equalities concern only the complete known reference residual.
An approximate unknown state's true high residual remains an independent
source. The raw mean is required in the complete equation and MA
authorization even though these high projections annihilate it.

## 5. Explicit trace coefficients, without invented unknown bounds

For each of the five MA-authorized cases, the scalar consumer reads
the original retained $M_0,M_1,M_2,\eta,\alpha_+,b_+,g_+,d_+,L,a_-$
and computes exactly LT.4, LT.13--LT.16 and LT.20. This is new
scalar arithmetic on complete already proved bounds, not a new
coefficient-grid calculation.

It records positive coefficients for
$$
 E_{96}\le F_{96}+c_L^{\rm body}Z_L+c_H^{\rm body}Z_H,
 \qquad
 E_{288}\le F_{288}+d_L^{\rm body}Z_L+d_H^{\rm body}Z_H,
                                                               \tag{NR.8}
$$
using the complete linear expressions in LT.7 and LT.16.
The stronger three-band expression LT.15 is also retained.
Here every $Z$ denotes the **$P$-scaled ordinary body norm**, not an
operator gain or a pointwise radius.

The finite cut multiplier $\Lambda_{96}$, the middle multiplier
$\sqrt{\Lambda_{288}}\,p_c\sqrt{\kappa_{96}c_pc_r}$,
and the far half-trace multiplier
$p_c\sqrt{\kappa_{288}c_pc_r}$ are given separately.
The old complete $p_I$ may safely upper-bound $p_c$.
The far interpolation exponent is $16384/16385$, with complete
prefactor $2^{24}$ and the same-state MA high bound $2^{377903}$.

The fixed additive middle-source budget is printed, as is its
signed difference from the sufficient radius $63d/320$.
That difference is not an actual-state gate: none of the missing
unknown body or cut values has been inserted as zero.
No numerical pass for the full low curvature entry is asserted.

## 6. Actual data required after this consumer

A later evaluation of LT.20 must supply the same selected-reference
raw finite193 cut norm, the actual low/high body norms on **both**
halves of $I_*$, and all actual residual information. The old Green's
whole inner output is only $[0,9/10]$ and cannot supply the right half.
The same continuous state must underlie both halves; matching and true
jump terms are not removed by a norm comparison.

The five high-window authorizations are copied from the complete
successful mean-correction execution
43717700427/1, SHA256
c5424be21b98cf5e195ea7246ccba46cf746d1f16d9c118042fda1fad433e408.
Their hypotheses remain one true two-sided solution in the specified
raw $C^0$ ball. They are not transferred to a general approximate state
with uncharged high residual.

## 7. Scientific and execution limits

The new run may restore the original forty exact natural parts into
temporary Actions storage. It must validate their canonical row
identity and the successful original D and collar receipts.
The successful MC mean restriction, its five corrected verdicts,
the old 91 cases, all source polynomials, Fourier arrays, target jets,
mean flows and Green data are immutable.

Only the two new nonmean restrictions, their complete scalar source
fees and the five coefficient tables are evaluated. A complete small
conclusion and its source/run/input hashes may be retained. A
per-row audit stays temporary and is represented by its hash.
All full means, exact radial intersections and complete old errors
remain in the scientific account.
