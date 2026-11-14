# R133: complete final-centre strict four-state Cauchy and source bounds

2026-11-14, visible-exact / phase_inverse. **The actual final-centre
calculation is complete.** The full ac1 moving candidate has now been
evaluated on all **3,071 closed radial boxes** from \(0\) to

\[
 r_a=\frac{1191939371497}{5000000000000}=0.2383878742994.
\tag{S.1}
\]

All 1,024 closed angular cells, the full original affine interval
\(|\eta|\le10^{-9}\), every intrinsic primitive remainder, every
candidate Fourier coefficient and every actual PPoly interface
are included. The native reports `complete=true`, `failure=null`.
It contains 2,549 complete candidate jump rows and nine freshly
evaluated target boxes beyond .238.

The candidate is exactly
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`,
with the original exact \(\alpha\), \(\nu\), coordinates and all
five shard bytes. The two former amplitude-.75 certificates are
not transferred to this centre.

## 1. Full operator and the four channels

Use the actual moving Jacobi equation (Y.2) in
`R133-supplement-four-state-moving-energy-and-residual-physical-ports.md`.
At every strict radius put

\[
 q=\sqrt{-K},\quad H=\operatorname{diag}(1,q^2),\qquad
 X=(E_0,M,E_1,Y)^T
 =\bigl(\|H^{1/2}h\|_2,|\langle h_2\rangle|,
         \|H^{1/2}h_\phi\|_2,\|h_2\|_2\bigr)^T.
\tag{S.2}
\]

The second component's ordinary norm \(Y\) is retained independently.
It is not replaced by \(E_0/q\). The full scalar mean is the second
channel, and the first component's allowed mean stays in \(E_0\).
For the intended reflection class the first component is odd.

The exact four-state comparison is (Y.6)–(Y.7) of that theorem.
The principal symmetrizer cancellation, the local identity
\((L_0)_{12}=K(L_0)_{21}\), the original primitive, complete mean
feedback, first angular commutator and ordinary second equation
are all retained. The current computation evaluates its actual
coefficients; it does not change the comparison theorem.

In particular, no finite angular Jacobian is used as an inverse.
The full symmetric-hyperbolic energy and characteristic construction
on each strict piece gives the full Fourier solution. Its exact
interfaces are then joined with the explicitly retained affine
sources. Smooth approximation and the uniform estimates extend
the result to the displayed ordinary source spaces.

## 2. Whole true target and exact joins

The cached original target boxes are used only on their proved
domains through .238. The new interval \([.238,r_a]\) is refined
by the actual candidate knots and genuine scalar-germ endpoints.
Each of its nine closed cells is evaluated by the complete
`ReciprocalFullTargetJets` at the exact current \(\nu\) and whole
original \(\eta\) interval. No root-crossing cached \(K\) box is
cropped and relabelled negative. Every actual cell separately
passes \(K<0\), \(\gamma>0\), \(s<0\), \(v<0\) and \(m<0\).

The compact perturbation and all original target seams remain in
the interval. The native keeps the exact target kind, scalar germ
and candidate piece for every row. All finite angular fields are
enclosed over the full closed angular circle by the actual
trigonometric sums and interval remainder, not only at sampled
grid values. Safe global numerical summaries are

\[
 \begin{gathered}
 |v|>0.0901777099,\quad |m|>1.0686761961,\quad
 q>0.0053976399,\\
 \|H^{1/2}Q\|_\infty<1.911031619,\quad
 \|H^{1/2}Q_\phi\|_\infty<3.703838174,\quad
 \|H^{1/2}Q_{\phi\phi}\|_\infty<14.746699851.
 \end{gathered}
\tag{S.3}
\]

These are complete current enclosures; some are deliberately
broad. No lower bound in (S.3) is substituted for an unproved
sharp root-distance asymptotic.

At each genuine PPoly join, both one-sided cubic values are exact
dyadic fractions. The full jump state is

\[
 \left(\sqrt{J_u^2+q^2J_v^2},\ J_m,
        \sqrt{J_{u\phi}^2+q^2J_{v\phi}^2},\ J_v\right)^T,
\tag{S.4}
\]

with a common true upper \(q\) at the interface. The unknown
moving correction has the true affine jump \(-[Q_c]\). The
homogeneous interface is the identity in this same moving unknown.
A physical-angle interface still uses its exact change of variables;
it is not silently substituted for this moving identity.

## 3. Complete forward propagation and ordinary sources

The product of the complete positive matrix exponentials gives
the following upper majorant for every forward subinterval and
every source insertion time:

\[
 P_+\le
 \begin{pmatrix}
 2.342768&1.208990&0&0\\
 .116969&1.096523&0&0\\
 2.895836&5.915025&2.283100&0\\
 .372944&1.061031&.372857&1.195758
 \end{pmatrix}.
\tag{S.5}
\]

The native also saves the sharper signed endpoint product; (S.5)
uses the all-subinterval positive majorant so that a source may
enter at any actual radius. No mean is reset between boxes.

The full ordinary \(H^1_\phi\) input/source injects into the four
channels by

\[
 \begin{pmatrix}w&0\\1&0\\0&w\\1&0\end{pmatrix},
 \qquad w=\max(1,\sup q),
\tag{S.6}
\]

acting on \((\|f\|_2,\|f_\phi\|_2)\). This preserves the
ordinary mean source and avoids dividing by the smallest root
weight. Taking the Frobenius upper bound of the complete
three-output matrix gives

\[
 \|(E_0,E_1,Y)\|_{\ell^2}
 <10.124885\|h(0)\|_{H^1_\phi}
   +10.240174\|f\|_{L^1_rH^1_\phi}
   +\mathcal J_+.
\tag{S.7}
\]

Here the actual full jump output is kept by its native four-state
column; useful component bounds are

\[
 (\mathcal J_{E_0},\mathcal J_{H^1_H},\mathcal J_Y)
 <(7.447674\,10^{-17},\ 4.061357\,10^{-16},\
   7.990237\,10^{-17}).
\tag{S.8}
\]

For arbitrary affine jumps, their own complete four-state norms
are propagated by (S.5); (S.8) is the particular actual centre
correction, not a replacement for general jump inputs.

If the input is instead measured solely in the degenerate
\(H^{s}_\phi\) norm of \(H^{1/2}h\), the mean conversion is paid
at the input radius. The native's complete forward gains are

| Order | Full initial data | Conditional initial mean zero |
|---|---:|---:|
| \(0\) | 3.650161 | 2.342768 |
| \(1/6\) | 4.334964 | 2.599177 |
| \(1/3\) | 5.148242 | 2.883649 |
| \(1\) | 10.241246 | 4.368864 |

The conditional column does not remove later mean production.
It only specifies the initial mean. Interpolation is on the same
complete Fourier scale. For a source measured in that degenerate
norm alone, the native separately records the conservative
\(L^1\) gains \(226.327571,295.530121,385.892237,1121.820067\)
in those four orders. These are not the ordinary-source contract
(S.7); the latter retains the ordinary mean and second component
before estimating, which is why it avoids that large conversion.

## 4. Physical port conversion remains exact and separate

At both endpoints the full actual inverse-angle gap passes. The
native saves both complete directions of the variation map

\[
 k=h-Q_\phi\chi,\qquad
 \chi=v^{-1}I(h_2-zv/m),\qquad z=\langle h_2\rangle,
\tag{S.9}
\]

and the actual physical measure and angular derivative factors.
At \(r_a\), the three physical outputs satisfy the safe matrix
bound

\[
 \begin{pmatrix}E_{0,\theta}\\E_{1,\theta}\\Y_{2,\theta}\end{pmatrix}
 \le
 \begin{pmatrix}
 1.263590&1.817511&0&1.683229\\
 0&22.755082&1.513850&25.880519\\
 0&1.770938&0&2.903686
 \end{pmatrix}
 \begin{pmatrix}E_0\\M\\E_1\\Y\end{pmatrix}.
\tag{S.10}
\]

No \(q(r_a)^{-1}\) occurs in this conversion. Its genuine angular
Jacobian is enclosed by
\(.4363496753<\theta_\phi<1.596659198\). The full reverse port
matrix is also recorded. The initial port has its own different
matrix and is not identified with (S.10).

The separate physical common-root-piece result now begins at
any \(r_0\ge r_c\), including \(r_a\). Thus (S.10) supplies its
normed trace once the **actual residual-sensitive Jacobi bridge**
has been included in the equation. This theorem does not discard
that bridge or claim that a moving Jacobi solution is already a
physical Jacobi solution. The signed physical/body boundary and
mean conditions remain independent global inputs.

## 5. Exact residual-sensitive scalar mean on this interval

For the scalar mean transform use \(n=a^2/m^2\),
\(\mathrm{Var}=\langle u^2\rangle+K\langle(v-m)^2\rangle\) and

\[
 \begin{split}
 R_0={}&\alpha V_0'
   -\beta\alpha V_0\bigl[1-K(m^2+ms+s^2)\bigr]
   +\beta m\,\mathrm{Var},\\
 \widetilde c={}&2\beta\,\mathrm{Var}-3R_0/m.
 \end{split}
\tag{S.11}
\]

The first equality uses the exact rotational equation for \(s\)
before interval evaluation. It retains every finite Fourier square
and the whole parameter/primitive error. In particular a large
canceling reference residual is not estimated before cancellation.

The complete actual negative diagonal integral is below
\(.005582539842\). All multiplicative mean interfaces add less
than \(3.903173\,10^{-19}\) to its logarithm, giving

\[
 \Gamma_{[0,r_a]}<1.005598152.
\tag{S.12}
\]

The complete reference-subtracted \(\nu\) interface fee is below
\(1.024061\,10^{-19}\). The full mean source and nonmean forcing
remain present. (S.12) is a scalar mean-given-nonmean bound on this
strict interval, not the whole-body mean Green or a scalar parameter
inverse. The latter is separately covered by Newton's whole-body
consumer.

## 6. Complete report, history, and permissions

The actual unchanged source is
`scripts/fourfold_codazzi_final_moving_strict_energy_v2.py`,
SHA256 `c6baae3e8448b4ceec95eeed50a38e8761207b1ca622173c1a8bccce3245b526`.
It consumed successful saved prefixes of 64, 576 and 1,600 rows,
then completed all 3,071. The report keeps every prefix identity
and complete dependency SHA; none of the prefix outputs was
mislabelled complete.

The original complete gzip is 8,499,033 bytes, SHA256
`23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a`.
Its lossless durable manifest is
`notes/2026-11-14-R133-final-strict-v2-ac1-complete-binary-parts.json`,
with five small consecutive binary `partNNN.bin.gz` files. The
shared helper directly gzips original byte ranges, without an
encoding or numerical rewrite. An actual scratch restoration
verified the complete original container SHA.

```bash
python3 scripts/fourfold_native_lossless_parts.py restore --manifest notes/2026-11-14-R133-final-strict-v2-ac1-complete-binary-parts.json --out /actual/scratch/final-strict-v2-ac1-complete-native.json.gz
```

For a new full reproduction, run the original producer at the
same actual ac1 candidate with a new output name. Its `--resume`
option takes the previous successful partial file and requires a
different new output file; it refuses failed or complete prefixes.
The restored runtime used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0
and python-flint 0.9.0.

The native also preserves the old unoptimized reverse comparison.
Its large bound, about \(2.55\,10^{26}\) for an ordinary source,
comes from separately enclosing the radial \(K'/K\) energy term
on each box. That valid coarse reverse estimate is not used in
(S.5)–(S.12) and is not advertised as an effective global inverse.
A subsequent grouped curvature-variation consumer can reduce it
without changing or erasing this report.

This conclusion grants full Fourier forward Cauchy and ordinary
source estimates on the stated strict interval, all exact joins,
the two endpoint variation norm conversions, and the stated scalar
mean factor. It does not grant the negative return inverse, finite
head inverse, complete positive/negative feedback, scalar \(\nu\)
condition, nonlinear solution, or nonlinear neighbourhood inverse.
