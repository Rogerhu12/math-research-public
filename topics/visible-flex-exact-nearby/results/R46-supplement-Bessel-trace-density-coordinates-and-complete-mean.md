# R46 supplement: complete density-coordinate norms from Bessel trace energy

The original density-coordinate operator is unchanged:

\[
 \Lambda_n=\max(1,|n|),\qquad
 Q_H=\Lambda^{1/2}C_H\Lambda^{-1/2},\qquad C_Hf=f\circ H.
 \tag{Q.1}
\]

For the actual physical-cut, graph-flow, strict-flow and final-circle
maps, this note gives full bounds for \(Q_H,Q_H^{-1}\) and their adjoints
on every \(H_N^s\), \(-2\le s\le2\), at the already used \(N=2^{20}\).
It retains the whole Fourier space and the exact mean row. No frequency
projection is inserted in the proof.

The complete results are:

| Actual map | New full \(|s|\le2\) bound | Previous bound |
|---|---:|---:|
| Physical cut angle | \(19.515367760\) | \(168038.685\) |
| Graph characteristic angle | \(1.703076133\) | \(1964.030\) |
| Strict characteristic angle, all pairs of times | \(1039.440120334\) | \(3.272643\,10^8\) |
| Actual final root circle | \(326.440786040\) | \(3.859485\,10^8\) |

The final-circle base \(L^2\) bound, for the map, inverse and adjoints,
is \(3.099734290\), independent of \(N\). The resulting factor product
for all the original coordinate factors is at most
\(1.404918048\,10^{17}\), in place of \(1.892714124\,10^{68}\).
The counts are unchanged. This is a new coordinate-operator theorem;
a returned-remainder consumer must still combine it with the actual
phase and Cauchy/scattering errors.

## 1. An exact full-mean half-order extension estimate

Temporarily use the Bessel weight
\(\nu=(1+D^2)^{1/2}\), \(D=-i\partial_x\), on the normalized
\(2\pi\)-circle. The exact trace identity is

\[
 \|\nu^{1/2}g\|_2^2
 =\inf_{U(x,0)=g(x)}
   \int_0^\infty\!\!\int_{\mathbb S^1}
        (|U_x|^2+|U_y|^2+|U|^2)\,dx\,dy.
 \tag{Q.2}
\]

The normalized angular measure is used on both sides. The minimizing
extension is \(U=e^{-y\nu}g\), as is seen mode by mode. The mass term
is essential: it includes the constant mode exactly.

Suppose \(0<m\le H'\le M\) and let \(J=\max(M,m^{-1})\).
The extension \(U(H(x),y)\) has energy at most \(J\) times the energy
of \(U\). Indeed change of angular variables gives coefficients \(H'\)
for the horizontal derivative and \(1/H'\) for the vertical derivative
and mass. It follows that

\[
 \|\widetilde Q_H\|_{2\to2}\le\sqrt J,\qquad
 \widetilde Q_H=\nu^{1/2}C_H\nu^{-1/2}.
 \tag{Q.3}
\]

The same argument applies to \(H^{-1}\). No estimate of a complex
extension, contour error, or Fourier cutoff is used.

For a coefficient \(a(x)\), apply the same argument to
\(a(x)U(H(x),y)\). Minkowski in the three-component energy norm gives

\[
 \|aC_Hg\|_{H^{1/2}_{\nu}}
 \le \|a\|_\infty\sqrt J\,\|g\|_{H^{1/2}_{\nu}}
       +\frac{\|a'\|_\infty}{\sqrt{2m}}\,
                                    \|g\|_{H^{-1/2}_{\nu}}.
 \tag{Q.4}
\]

For the second term,
\(\int_0^\infty\|e^{-y\nu}g\|_2^2dy
=\frac12\|g\|_{H^{-1/2}_{\nu}}^2\).
This proves the stated coefficient and keeps the lower-order term in
its actual weaker norm.

## 2. A finite triangle for all positive integer windows

Write

\[
 e_j=N^{-j}\|\partial_x^jf\|_2,\qquad
 \|f\|_{H_N^k}^2=\sum_{j=0}^k\binom kj e_j^2 .
 \tag{Q.5}
\]

Let \(h_j\) be complete real upper bounds for \(|H^{(j)}|\).
For the Faà di Bruno coefficients, let \(B_{j\ell}\) and
\(E_{j\ell}\) bound their modulus and first angular derivative.
They are computed as nonnegative polynomials:

\[
 B_{00}=1,\qquad
 B_{j\ell}=\sum_{v=1}^{j-\ell+1}
   \binom{j-1}{v-1}h_v B_{j-v,\ell-1},
\]
\[
 E_{j\ell}=\sum_{v=1}^{j-\ell+1}
   \binom{j-1}{v-1}
       (h_{v+1}B_{j-v,\ell-1}+h_vE_{j-v,\ell-1}).
 \tag{Q.6}
\]

The zero entries have their usual meaning. The angular derivatives here
are not radial derivatives.

Apply (Q.4) to each term of
\(\partial_x^jC_H\nu^{-1/2}f\). For \(\ell\ge1\),

\[
 \|\partial_x^\ell\nu^{-1}f\|_2
 \le\|\partial_x^{\ell-1}f\|_2.
 \tag{Q.7}
\]

This is the exact Fourier inequality
\(|n|^\ell/\sqrt{1+n^2}\le|n|^{\ell-1}\); it includes zero.
The coefficient-derivative fee therefore moves down one derivative
level, rather than multiplying a top-order norm.

If \(\bar h_1\) bounds \((H^{-1})'\), a complete triangle for
\(\widetilde Q_H\) is

\[
 T_{j\ell}=N^{-(j-\ell)}
 \left[\sqrt J\,B_{j\ell}
       +\mathbf1_{\ell<j}\sqrt{\bar h_1/2}\,E_{j,\ell+1}\right].
 \tag{Q.8}
\]

With \(W_k=\operatorname{diag}_{j\le k}\sqrt{\binom kj}\),
the full positive bound is \(\|W_kT^{[k]}W_k^{-1}\|_2\).
This controls the ordinary full Fourier norm directly. There is no
\(\sqrt N\) change between unrelated weights. In particular
\(T_{00}=\sqrt J\), while higher coefficient derivatives occur with
their displayed powers of \(N^{-1}\). The real principal powers of
\(H'\) on the diagonal are retained and do not disappear as \(N\)
increases.

For \(k\le2\), only the complete first three real jets of \(H\) and
\(H^{-1}\) are required. The executable uses a directed Schur/Frobenius
upper bound for these finite comparison matrices, not an approximation
of the infinite operator.

## 3. Convert exactly to the original \(\max(1,|n|)\) weight

The weight in (Q.1) is not the Bessel weight of (Q.2). Set

\[
 S=(\Lambda/\nu)^{1/2}.
\]

Its diagonal norm is at most one and its inverse norm is at most
\(2^{1/4}\), on every \(H_N^s\). The exact identity

\[
 Q_H=S\widetilde Q_HS^{-1}
 \tag{Q.9}
\]

therefore costs \(2^{1/4}\) once in each positive-window bound,
including the base. In particular

\[
 \|Q_H\|_{2\to2},\ \|Q_H^{-1}\|_{2\to2}
 \le 2^{1/4}\sqrt J.
 \tag{Q.10}
\]

This factor is included in every final native positive constant.
The displayed native derivative matrices are the Bessel triangles
before this explicitly recorded diagonal conversion.

An initial unconsumed Bessel-only report is marked incomplete and
unproved for the original operator. Only the corrected report ending
in -v2.json is authorized by this note.

## 4. Opposite windows and the complete mean row

Ordinary one-dimensional change of variables gives the exact identity

\[
 C_H^*DC_H=D,\qquad
 Q_H^*J_0Q_H=J_0,\qquad J_0=D/\Lambda .
 \tag{Q.11}
\]

Here \(J_0\) is zero on the mean and is exactly \(\operatorname{sgn}D\)
on all nonzero modes. The mean cannot be inverted through this identity.

Since \(Q_H1=1\), its full block matrix is

\[
 Q_H=\begin{pmatrix}1&b\\0&A\end{pmatrix},
 \qquad A^*J_*A=J_* .
 \tag{Q.12}
\]

The full \(Q_H^{-1}=Q_{H^{-1}}\) exists, so \(A\) is onto and has
the corresponding inverse block. Since \(J_*^{-1}=J_*\) is an
isometry on every \(H_N^k\),

\[
 \|A^*:H_N^k\to H_N^k\|
 \le \|Q_{H^{-1}}:H_N^k\to H_N^k\|.
 \tag{Q.13}
\]

The missing mean-to-nonmean adjoint column is explicit. For
\(G=H^{-1}\),

\[
 b^*=\Lambda^{-1/2}(G'-1).
 \tag{Q.14}
\]

The exact mean of \(G'\) is one. If
\(m_G\le G'\le M_G\), then

\[
 \|G'-1\|_2^2\le(M_G-1)(1-m_G),
 \tag{Q.15}
\]

by integrating \((G'-m_G)(M_G-G')\ge0\).
With the complete jets \(\bar h_j\) of \(G\), this proves

\[
 \|b^*\|_{H_N^k}\le B_k,\qquad
 B_k^2=(\bar h_1-1)(1-h_1^{-1})
           +\sum_{j=1}^k\binom kj N^{-2j}\bar h_{j+1}^{\,2}.
 \tag{Q.16}
\]

The harmless inequality \(\Lambda^{-1/2}\le1\) was used here; every
mode in the mean column remains. Combining (Q.12)–(Q.16) gives

\[
 \|Q_H^*:H_N^k\to H_N^k\|
 \le C_{H^{-1},k}^{+}+B_k.
 \tag{Q.17}
\]

The diagonal block norm also includes one; the paid positive bound is
at least one. Interchanging \(H,G\) treats the inverse adjoint.
At \(k=0\) the sharper bound (Q.10) already applies to adjoints.
Duality supplies the negative integer windows, and interpolation
supplies every real \(s\in[-2,2]\).

Thus both the positive and opposite windows are actual full-space
bounds. The kernel of \(J_0\) has not been ignored, and no mean column
is declared small or zero.

## 5. Consumption of the existing complete actual jets

The physical-cut and graph maps use their already certified common
complex strips solely to give real Cauchy jets through order three.
Both directions use the saved derivative bound on the map and inverse.
No strip is widened.

For the strict maps the actual full R106 Fourier control certificate
supplies the better real jets, uniformly in all pairs of strict times
and both directions:

\[
 h_1=\bar h_1<14.983653,\quad
 h_2=\bar h_2<123831.015772,\quad
 h_3=\bar h_3<3163445102.801.
\]

These statements include all 550 reference segments, all 4400 control
rows, every exact seam, every real angle, and the whole actual parameter
box. They are used only for the real Sobolev theorem above; they do not
replace any complex contour bound.

For the actual final circle, the prior complete forward and inverse
real jet lists are reused as stored. The inverse list is its own
previously paid inverse-jet recursion, not the forward list relabeled.
All identities are checked against the same graph and normal-form
inputs.

The original word counts remain four physical-cut factors, four graph
factors, two strict factors, four unitary Airy translations, and two
actual final-circle factors. Their new full \(|s|\le2\) product is

\[
 P_Q<1.404918048\,10^{17}.
 \tag{Q.18}
\]

Every phase factor, mean correction, opposite-cone error, and old
complex contour strip remains a separate obligation. In particular
the real theorem (Q.18) does not improve any of the saved cross-cone
analytic errors without another argument.

The actual final base reconstruction factor from the two triangular
operations and final coordinate inverse can now be bounded by

\[
 2\|Q_C^{-1}\|_{2\to2}<6.199468579.
 \tag{Q.19}
\]

It acts on the same complete physical amplitudes and regular direct
sum as before. It does not impose a zero physical head, and it does
not itself provide a full inverse.

## 6. Executed consumer

The complete source is
scripts/fourfold_actual_density_Q_Bessel_budget.py;
the final directed native is
notes/2026-11-13-actual-density-Q-Bessel-budget-v2.json.
The final run took about .61 seconds and recomputed no geometric cells.
It stores every positive derivative triangle, both inverse-jet lists,
both mean-adjoint rows, every signed integer-window constant, the
conversion factor in (Q.9), and the unchanged word counts.

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_density_Q_Bessel_budget.py \
  --out /tmp/actual-density-Q-Bessel-budget-v2.json
~~~

The result is ready to be used in the same actual full return. The
current note does not recompute that return, claim a manageable finite
head, or conclude the nearby-surface theorem.

