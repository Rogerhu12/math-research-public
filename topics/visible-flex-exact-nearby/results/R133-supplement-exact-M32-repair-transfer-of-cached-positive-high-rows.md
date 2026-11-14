# R133 supplement: exact M32 repair transfer of the cached whole-positive high rows

2026-11-14, visible-exact / tail_connector.

**Status: proved transfer contract; the new repair consumer has not yet run.**
This note specifies how to reuse all 4,650 complete coefficient rows of the
actual ac1 centre for an exact repair that retains its 32 moving Fourier
modes. It does not grant new numerical inverse constants before the new
scalar sweeps and endpoint gates pass. A 96-mode parameter direction is a
separate small-tail problem and is not inserted into the 32-mode denominators.

## 1. Object, identities and the required repair input

The old complete coefficient native is recovered losslessly from

- `notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json`;
- original native SHA256
  `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`;
- original producer SHA256
  `1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c`;
- original consumer
  `scripts/fourfold_codazzi_current_positive_high_Volterra.py`, SHA256
  `808319ccaaab63ade3d0137b7c8dc74d7e11e136735dfb214badaac482d9aa28`;
- original centre SHA256
  `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.

Their whole requested interval is
$$
 [r_b,R]=[0.2384058742994,25/8].
 \tag{A.1}
$$
Every old closed row, its intrinsic enclosure, its original one-sided
interface, and the complete source/dependency identities are retained.
The same intrinsic $K,\beta,\gamma$ may be reused only for the same
metric object and parameter: the compact $\nu$ perturbation vanishes
on (A.1). This is not permission to reuse them for a changed intrinsic
metric.

Write the exact repaired moving background as
$$
 \widetilde Q=(\widetilde u,\widetilde v)=Q+(e_u,e_v),
 \qquad \widetilde m=\langle\widetilde v\rangle .
$$
On a common refinement of every old closed row and every repair-error row,
supply complete upper bounds
$$
 E_u=\|e_u\|_{A^0},\quad E_v=\|e_v\|_{A^0},\quad
 E_{u1}=\|(e_u)_\phi\|_{A^0},\quad
 E_{v1}=\|(e_v)_\phi\|_{A^0},\quad
 E_m=|\langle e_v\rangle|,\quad
 E_{v\ne0}=\|P_{\ne0}e_v\|_{A^0}.
 \tag{A.2}
$$
The input must prove all six on the whole closed row, and bind the exact
repair definition and its native SHA. Separate signed mean enclosures
can be used instead of the symmetric $E_m$ interval. It must also
prove that the repaired background has moving band at most 32.
Neither an $L^2$ error nor a finite trial's band proves that assertion
for a different unknown background.

The new parameter domain is the intersection of the old certificate's
domain with the actually proved repair domain. In particular a repair
proved only at $\eta_0$ grants only $\eta_0$; it does not inherit the
old whole-$\eta$ statement.

## 2. Exact inflation of every coefficient needed by the high consumer

Use each old row's actual fields $U,V,U_1,V_1,V_{\ne0}$, mean interval
$m$, intrinsic $K,\beta,\gamma$, and its saved reaction/drift bounds.
All quantities in the following upper formulas are nonnegative outward
bounds; $K_+$ is the true row upper endpoint.

Set
$$
\begin{split}
 \Delta U_2&=2UE_u+E_u^2,&
 \Delta V_2&=2VE_v+E_v^2,\\
 \Delta UV&=UE_v+VE_u+E_uE_v,&
 \Delta S&=\Delta U_2+K_+\Delta V_2 .
\end{split}
 \tag{A.3}
$$
Complete Wiener convolution and the exact local reaction matrix give
$$
\begin{split}
 \delta a&=|\beta|(3\Delta U_2+K_+\Delta V_2),\\
 \delta e&=|\beta|(\Delta U_2+3K_+\Delta V_2),\\
 \delta b&=2|\beta|\Delta UV,\\
 \delta d_1&=|\beta|\Delta S,\qquad \delta d_0=\delta d_1/4 .
\end{split}
 \tag{A.4}
$$
Indeed the moving reaction is
$\left(\begin{smallmatrix}
-\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
-2\beta uv&\beta(1-u^2-3Kv^2)
\end{smallmatrix}\right)$.
Its grounded off-diagonal form has the same scalar $b$ in the
upper-right $Kb$ and lower-left entry. Thus (A.4) may be added
separately to both the saved Wiener and supremum bounds of $a,e,b$.
The estimate for $d=-\beta I(u^2+Kv^2)$ uses the true mean-zero
primitive $I$, with norm $1/4$. It never bounds an unknown
$d\partial_\phi h$ by an $L^2$ multiplier.

The complete replacement field rows are
$$
 \widetilde U=U+E_u,\quad \widetilde V=V+E_v,\quad
 \widetilde U_1=U_1+E_{u1},\quad
 \widetilde V_1=V_1+E_{v1},\quad
 \widetilde V_{\ne0}=V_{\ne0}+E_{v\ne0}.
 \tag{A.5}
$$
For the nonlocal and mean columns use the same exact formulas with
these new bounds:
$$
\begin{split}
 \widetilde N_{\rm raw}
 &=\frac{|\beta|}{2}(\widetilde U_1+\widetilde V_1)
                         (\widetilde U+K_+\widetilde V),\\
 \widetilde M_{\rm raw}
 &=|\gamma|(\widetilde U_1+K_+\widetilde V_1),\\
 \widetilde{\mathrm{meanFB}}
 &=2|\beta|(|m|+E_m)
                      (\widetilde U+K_+\widetilde V_{\ne0}).
\end{split}
 \tag{A.6}
$$
The signed own-mean rate is not replaced by an unsigned positive rate.
If its saved interval is $r_m=\beta(1-S_0-2Km^2)$, enclose the new
rate in
$$
 r_m+[-\epsilon_m,\epsilon_m],\qquad
 \epsilon_m=|\beta|\{\Delta S+
             2K_+(2|m|E_m+E_m^2)\}.
 \tag{A.7}
$$
The full $S_0$ interval is enlarged by $[-\Delta S,\Delta S]$.
These rows remain available to the finite head; a high inverse does
not delete them.

## 3. The principal mean changes the reference

The actual new speed is
$$
 \widetilde a=-\gamma\widetilde m .
$$
A sufficient complete row lower bound is
$$
 \widetilde a_-=a_- -|\gamma|E_m>0 ,
 \tag{A.8}
$$
with the analogous upper bound $a_++|\gamma|E_m$.
Using the signed product interval can be sharper. The physical inverse
angle gap must also be checked:
$$
 \widetilde g_{\rm phys}\ge
             g_{\rm phys,old}-E_m-E_{v\ne0}>0 .
 \tag{A.9}
$$
A strictly positive speed alone does not imply (A.9).

For the continuous frequency range $M\ge4$, which contains every actual
nonzero physical mode $M=4|j|$, define a **new single full-interval reference**
on $[r_*,R]$:
$$
\begin{split}
 \widetilde g_M'&=M\widetilde a(K-\widetilde g_M^2),
      &\widetilde g_M(r_*)&=M^{-1/3},\\
 \widetilde p_M'&=M\widetilde a(\widetilde p_M^2-K),
      &\widetilde p_M(R)&=\widetilde p_*,
      &\widetilde p_*&=q_*/(-\widetilde m_R).
\end{split}
 \tag{A.10}
$$
Here $q_*=(1+w_R^2)^{-1/2}$ belongs to the same intrinsic outer
object. The genuine endpoint datum must be proved to satisfy
$$
                    1/8<\widetilde p_*<1/5 .
 \tag{A.11}
$$
It is permissible to prove that the repair preserves the endpoint
exactly; then the old datum is genuinely unchanged. Otherwise (A.11)
is recomputed from the new mean, not inferred from an interior
$L^2$ error.

The full reference is not initialized by $g(r_b)=0$.
Zero is only the conservative lower comparison at that interior cut.
Its true initial value remains $M^{-1/3}$ at $r_*$, and its
backward endpoint is the actual $\widetilde p_*$ at $R$.
This distinction prevents a mismatch with both the root and the
regular cap.

The positive variational proof in
`R133-supplement-global-positive-reference-and-current-collar.md`
applies to this frequency-independent positive speed:
$$
 0<\widetilde p_M,\widetilde g_M<2,\qquad
 |M\partial_M\log\widetilde p_M|,
 |M\partial_M\log\widetilde g_M|\le1 .
 \tag{A.12}
$$
Consequently the same neighboring-frequency constants remain valid
for the exact new frame. No small norm of old-frame minus new-frame
is asserted or required.

## 4. Only scalar lower comparisons and scalar Volterra sweeps are new

Let $N=97$, $M_0=388$. Reuse the exact function
`lower_flow` from the old consumer with the new $\widetilde a_-$.
On a row of length $\ell$, reset its incoming lower value to
$b_0=\min(b,\sqrt{K_-})$ and use
$$
 y(\ell)=\sqrt{K_-}\,
 \frac{b_0+\sqrt{K_-}\tanh(M_0\widetilde a_-\sqrt{K_-}\ell)}
      {\sqrt{K_-}+b_0\tanh(M_0\widetilde a_-\sqrt{K_-}\ell)} .
 \tag{A.13}
$$
The backward $p$ lower sweep starts at $1/8$; the forward $g$
lower sweep at $r_b$ starts at zero. Since the actual intrinsic
floor remains $K>1/2000$, the independently proved invariant
lower bound $p>1/45$ is retained. Take
$$
 \widetilde w_i=p_{-,i}+g_{-,i},\qquad
 \widetilde k_i=M_0\widetilde a_{-,i}\widetilde w_i/2,\qquad
 \widetilde q_i=K_{+,i}/\widetilde w_i.
 \tag{A.14}
$$
Every value bounds all $M\ge388$ on the entire closed row.
The reset in (A.13) is essential: it ensures
$K_--y^2\ge0$ before lowering the speed or frequency.

With the inflated six reaction bounds, put
$$
\begin{split}
 \widetilde B_\infty
  &=\widetilde a_\infty+\widetilde e_\infty+
                      (\widetilde q_i+4)\widetilde b_\infty,\\
 \widetilde B_A
  &=\widetilde a_A+\widetilde e_A+
                      (\widetilde q_i+4)\widetilde b_A,\\
 \widetilde F_N
  &=\widetilde U_1\widetilde U+
       K_+\widetilde V_1\widetilde V+
       \widetilde q_i\widetilde U_1\widetilde V+
       4\widetilde V_1\widetilde U .
\end{split}
 \tag{A.15}
$$
The complete new high remainder is bounded by
$$
 \widetilde E_i^{(s)}
  =(c_s+\tfrac12)\widetilde d_{\phi,A}
   +2\widetilde B_\infty
   +\frac{8d_s\,32}{97}\widetilde B_A
   +\frac{n_s|\beta|}{65}\widetilde F_N ,
 \tag{A.16}
$$
where $(c_s,d_s,n_s)=(6,3,4)$ for $s=0$ and
$(18,9,8)$ for $s=1$. The actual new drift, including its
unbounded derivative, stays in the exact shared skew transport.
The finite band, both signs, both coefficient convolutions, and
the true intermediate primitive denominator are exactly the old
proved hypotheses, now verified for the repaired M32 field.

Apply the old `affine_decay` and `directed_sweep` formulas to
$(\widetilde E,\widetilde k)$. For each order retain the maxima
on every closed row, rather than only at its endpoints globally:
$$
 \widetilde\tau_s=
  \max_i\sqrt{(\sup_{I_i}A_s)^2+(\sup_{I_i}A_u)^2}.
 \tag{A.17}
$$
The two branch spaces are orthogonal. Thus the new feedback is
$$
 \widetilde\chi_0=\widetilde\tau_0+\widetilde\epsilon_R,\qquad
 \widetilde\chi_1=\widetilde\tau_1 .
 \tag{A.18}
$$
The full right high port remains independent for $s=1$.
Only an actually passed $\widetilde\chi_s<1$ grants a new high inverse.
The old .303291679 and .788277736 numbers are not copied as new results.

## 5. Ordinary sources, the full head, and all true interface sources

Use the new complete source/reconstruction row
$$
 \widetilde C_i=
 \min\{5,\ 2M_0^{-1/6}\max(2,\widetilde w_i^{-1/2})\}.
 \tag{A.19}
$$
The same all-frequency proof validates either term, so their minimum
is a valid bound. The two ordinary-source sweeps use forcing
$\widetilde C_i^2$ and damping $2\widetilde k_i$.
If their complete sum is bounded by $\widetilde B_f^2$, then
$$
 \|Z_H\|_{\sup H^s}\le
 \frac{\widetilde B_f\|f_H\|_{L^2_rH^{s+1/3}}
                     +G_s}{1-\widetilde\chi_s}.
 \tag{A.20}
$$
Raw $L^2$ reconstruction and both endpoint traces are recomputed
from the same $\widetilde C_i$, the same row lengths, and the
factor $(1+388^{-2})^{s/2}$. No source radial derivative is introduced.

For the retained 193-state head, including its independent even mean,
the exact sufficient coupling rows remain
$$
\begin{split}
 \widetilde L_{\rm raw}
   &=\widetilde a_A+\widetilde e_A+(1+K_+)\widetilde b_A,\\
 \widetilde A_{HL}
   &=384\widetilde d_A+\widetilde L_{\rm raw}
                                      +\widetilde N_{\rm raw},\\
 \widetilde A_{LH}
   &=\widetilde A_{HL}+\widetilde d_{\phi,A}.
\end{split}
 \tag{A.21}
$$
The whole M32 head-to-high source has index at most $96+64=160$;
its actual $H^{s+1/3}$ source weight is
$(1+640^2)^{(s+1/3)/2}$.
The finite head's own generator additionally retains
$384\widetilde a_+\max(1,K_+)$ and
$\widetilde M_{\rm raw}$. These are inputs for the global Schur
problem, not an assertion that it is invertible.

At any interface the new reference is continuous, since (A.10)
has an absolutely continuous solution. For a genuine affine jump
$j_i=h^+-h^-$, the exact transformed jump is
$$
 j_{Z,i}=M^{1/6}\widetilde T_M(r_i)^{-1}
                   \operatorname{diag}(-i\operatorname{sgn}k,1)j_i .
 \tag{A.22}
$$
The source term $G_s$ includes
$\sum_i\widetilde C_i\|j_i\|_{H^{s+1/3}}$, with the proper
backward sign before taking its norm. It also includes the actual
head, mean, $f_B,r_B,r_C$, and independent port columns.

The old centre's jump and a new trial's jump are different objects.
If the repair theorem proves continuity, its own centre jump is
exactly zero. If a piecewise trial is used to solve a new linear
response, its saved jump remains an affine source. Otherwise an
error-jump enclosure gives
$$
 \|[\widetilde Q]\|_{A^q}
 \le\|[Q]\|_{A^q}+\|[e]\|_{A^q},\qquad q=0,1,2.
 \tag{A.23}
$$
For the mean retain the signed new jump, or its explicitly justified
absolute bound. A homogeneous identity interface never removes
these affine data.

## 6. Root and exterior contracts must be transferred separately

The actual old global-root budget is
`notes/2026-11-14-R133-global-reference-current-collar-rational.json`,
with its source
`scripts/fourfold_codazzi_global_reference_current_collar.mjs`.
Its 25 gates refer to the same ac1 centre and state explicitly

- full domain $[r_*(\eta),25/8]$;
- genuine $g_M(r_*)=M^{-1/3}$;
- genuine $p_M(R)=q_*/(-m_R)$;
- $h=9/1000000$, $N=97$, $M_0=388$;
- global $p,g<2$, root $p(r_*)<66M^{-1/3}$;
- old root $E=18262183/1261$, old $hE=164359647/1261000000$;
- old complete 193-head loop $1921439637/250000000000$.

The old root and outer text inputs are bound there to Git blobs
`3edf335784786da9a4a515b28d364d8ad2914e24` and
`7784d7158974d4632ca634369e55dc095e134902`, respectively.
They are not new repair numerical certificates.

The repair root consumer must verify its new speed bounds, optical
$K_s=K_r/\widetilde a$, reaction/drift/nonlocal rows, source frame,
all head crossing rows and full head loop. If it proves the old
displayed envelopes remain true, the old inequalities can be
reused exactly. Otherwise it evaluates their displayed formulas
with the newly enlarged bounds. The new whole-body reference
needs no extra old-to-new frame comparison, because its definition
already uses (A.10).

At the outer endpoint the complete regular-graph theorem is
`R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md`.
Its .0000222 reflection is a proved consequence of specific actual
physical background, moving-coefficient, mean and change-of-angle
bounds, not a universal constant for every M32 field.
A new outer consumer must either prove endpoint data unchanged,
or place the repaired physical background and complete angle
map inside that theorem's stated balls and re-evaluate its
(S.10)--(S.18), (S.20)--(S.38) formulas.
In particular an interior moving $L^2$ repair bound does not
by itself bound the infinite physical Fourier tail.
All mean and independent boundary source rows are retained.
For $s=1$, this transfer still supplies no unpaid nonlinear
physical $H^{7/6}$ exterior graph.

## 7. Minimal implementation and provenance

A new consumer should load and SHA-check the restored old native,
the independent repair-error native, and any new root/outer natives.
It should:

1. Intersect their exact parameter domains and take their exact
   common radial refinement; check both adjacent endpoint identities.
2. Copy each old intrinsic enclosure and all original fields unchanged
   into an `original_row` record. Attach the repair error and construct
   a separate `inflated_row` by (A.3)--(A.9).
3. Reject a missing M32-band proof, a nonpositive new speed/angle gap,
   an unproved outer $p_*$, or a gap in any complete cover.
4. Reuse `lower_flow`, `affine_decay`, `directed_sweep` for the
   new scalar rows and exact new frame. Retain a digest of every
   derived row and the complete closed-row maxima.
5. Record the independently supplied root and exterior permissions.
   Grant only the body high inverse until both have been transferred.
6. Recompute every source, head coupling, mean and affine jump row.
   Bind their identities separately from the coefficient identity.
7. Preserve a failed attempt with its actual exit code and gate;
   never overwrite an old successful native or label the old centre
   SHA as the repaired centre.

No new coefficient-grid evaluation or intrinsic 4,650-row production
is required by this contract. Only the actually proved repair-error
cover and the new scalar sweeps are new work. The result is a complete
all-frequency high inverse when its stated numerical gates pass;
the full negative return, finite head, scalar $\nu$ row and nonlinear
equation remain separate obligations.
