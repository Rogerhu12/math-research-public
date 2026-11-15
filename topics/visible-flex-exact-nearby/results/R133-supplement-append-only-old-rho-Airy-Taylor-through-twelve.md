# Append-only old-radial Airy Taylor coefficients through degree twelve

**Status: proved finite-algebra consumer contract. The new degrees and their scalar budgets have not yet been computed.**

This supplements the [original complete Taylor computation](R133-supplement-actual-complete-old-radial-first-Airy-Taylor-bounds.md) and the [actual intrinsic derivatives through fifteen](R133-supplement-actual-append-only-true-root-intrinsic-jets-through-fifteen.md). It keeps the repaired explicit family, fixed original $\eta_0$, complete complex square $|\Re\delta|,|\Im\delta|\le10^{-8}$, true-root bracket and original physical root piece. Physical seams, the independent mean and final completion criterion are unchanged.

## T.1. Completed inputs are preserved

Original Taylor run 43653825736/1 has native SHA256
18990ac2c1ed8e559d00982b75d663c08ad7e193455de1f8482511c36938b719
and process SHA256
eebbbf37419729069c28ef3cd7c7d34f02154b8c391b0cfa9ca093de8855a356.
Its child returned zero, twenty gates passed, and all seventy-five natural stages have exact receipts. Its cubic rows, background, fold through degree eight, leading series, local and normalized transport coefficients, forcing and correction through degree six, full Fourier norms and original derivative budgets remain accepted.

New intrinsic run 43661471951/1 has native SHA256
ec702cffb8d1dcb25cdb01eaa89127b1f0044ae1cd3cee9e6e293e8165250480
and process SHA256
c7ff69243d3f724f539cd0ee95c2b0ba219caa5ffba47ff9b084387255e78e5b.
Its child returned zero and twelve gates passed. All four ordinary old-radial intrinsic jets $K,\beta,\gamma,s$ are complete through derivative fifteen; the original ten coefficients and 54 comparison records were preserved exactly.

The successor verifies both actual results and every original natural stage. It never invokes an old target, FFT, intrinsic, cubic, ray or auxiliary-domain producer. All seventy-five original compressed files remain byte-identical. Reading lower coefficients for a new higher operation does not authorize rebuilding their old outputs.

## T.2. Exact order accounting

For $\rho=r_*-r$ and an intrinsic scalar $h$,
$$
 [\rho^j]h=\frac{(-1)^j}{j!}h^{(j)}(r_*).
\tag{T.1}
$$
The certified true-root identity $K(0)=0$ gives
$$
 k=-K/\rho,\qquad
 [\rho^j]k=\frac{(-1)^j}{(j+1)!}K^{(j+1)}(r_*).
\tag{T.2}
$$

| Object | Original degrees | New degrees |
|---|---|---|
| Background $u,v,K,\beta,\gamma,s,k,\eta,a,S,d$ | $0,\ldots,8$ | $9,\ldots,14$ |
| Fold $\chi=X-\phi$, $A$ and leading reconstruction | $0,\ldots,8$ | $9,\ldots,14$ |
| Local operator and normalized transport coefficients | $0,\ldots,6$ | $7,\ldots,12$ |
| Forcing, normalized forcing, transport and correction | $0,\ldots,6$ | $7,\ldots,12$ |
| Norm at each original angular width | $0,\ldots,6$ | $7,\ldots,12$ |

The candidate and direction cubics have zero derivatives above order three on this physical piece. The value repairs are constant, and the compact bump vanishes on the whole original germ. Thus the new coefficients of $u$ are exactly zero and those of $v$ equal the new coefficients of $s$. This is an identity of the original piece, not padding missing intrinsic coefficients. All nine original background coefficients are loaded unchanged.

Use the original relations
$$
 \eta=-\gamma\langle v\rangle,\quad a=\eta\sqrt{k},\quad
 S=u^2+Kv^2,\quad d=-\beta JS.
\tag{T.3}
$$
The same positive constant branches are retained.

## T.3. Triangular extension with full Fourier outputs

For complete Laurent polynomials,
$$
 [\rho^n](PQ)=\sum_{j=0}^{n}P_jQ_{n-j}.
\tag{T.4}
$$
Products are non-circular with physical multiplier $4j$; all means and finite support are preserved. With nonzero radial constant,
$$
 (P^{-1})_n=-P_0^{-1}\sum_{j=1}^{n}P_j(P^{-1})_{n-j}.
\tag{T.5}
$$
Already saved inverse coefficients are copied. Previously unsaved helper series can require lower coefficients to compute a new higher coefficient; such helpers are separately identified, saved and reused. They do not replace any original completed leading, forcing, transport or correction coefficient.

For $Y=P^p$ on the original branch,
$$
 nP_0Y_n=pnP_nY_0+
 \sum_{j=1}^{n-1}\bigl((p+1)j-n\bigr)P_jY_{n-j}.
\tag{T.6}
$$
Normalized powers have $Y_0=1$. If $Y'=gY$, $Y_0=1$, then
$$
 nY_n=\sum_{j=0}^{n-1}g_jY_{n-1-j}.
\tag{T.7}
$$
Unavailable coefficients are never replaced by zero unless the other factor has a proved exact zero.

The original fold recurrences append degrees nine through fourteen with nonzero divisors $n$ and $2n+3$. Then
$$
 T=-\rho A^{2/3},\quad Q=aA^{-1/3},\quad
 B_\pm=X_\phi^2\pm TT_\phi^2,
$$
$$
 \mu=Q^2B_+,\quad a_0=GB_-,\quad
 b_0=-2i\epsilon GX_\phi T_\phi.
\tag{T.8}
$$
The different signs in $\mu$ and $a_0$ are essential. Degree twelve of the local operator requires second derivatives of leading degree fourteen. The internal drift derivative also requires degree thirteen of $\ell$ and the scalar coefficient $b_{\rm loc}$; those two additional helper coefficients are explicitly computed.

The normalized forcing uses the same complete inverse
$$
 M_0^{-1}=(a_0^2-Tb_0^2)^{-1}
 \begin{pmatrix}a_0&-Tb_0\\-b_0&a_0\end{pmatrix}.
\tag{T.9}
$$
Original ordered Fuchsian recurrences append degrees seven through twelve using $\mathcal A(0)=0$, $\mathcal B(0)=f_b(0)$. Lower coefficients are always the accepted originals. Reconstruction $w_1=M_0(\mathcal A,\mathcal B)^t$ keeps the even mean.

The same triangular support induction gives
$$
 \deg a_{1,p}\le192(p+1),\qquad
 \deg b_{1,p}\le192(p+2).
\tag{T.10}
$$
Every new stage checks its actual full support. The identities $a_{1,-}=-a_{1,+}$ and $b_{1,-}=b_{1,+}$ use the same complex parameter, without conjugation.

## T.4. Complete infinite tails on the unchanged domain

Retain $R=1/6000$, $\Sigma=1/128$ and the exact original physical cover
$$
 h=9\cdot10^{-6}+(r_+-r_-),\qquad x=h/R<1.
\tag{T.11}
$$
The old-product image was already proved to lie inside the larger auxiliary canonical rectangle. Its complete amplitude suprema $M_a,M_b$ and domain certificate are reused.

For $N=12$ define
$$
 U_0=\frac{x^{N+1}}{1-x},\quad
 U_1=\frac{(N+1)x^N}{1-x}+\frac{x^{N+1}}{(1-x)^2},
$$
$$
 U_2=\frac{N(N+1)x^{N-1}}{1-x}
 +\frac{2(N+1)x^N}{(1-x)^2}
 +\frac{2x^{N+1}}{(1-x)^3}.
\tag{T.12}
$$
For radial order $p\le2$, angular order $q\le3$ and $\sigma<\Sigma$, the full strip-supremum tail is bounded by
$$
 M R^{-p}U_p(x)\frac{q!}{(\Sigma-\sigma)^q}.
\tag{T.13}
$$
For the Wiener tail, replace the last factor by the complete geometric Fourier sum
$$
 \sum_{j\in\mathbb Z}(4|j|)^q e^{-4|j|(\Sigma-\sigma)};
\tag{T.14}
$$
the zero mode is included at $q=0$. The finite part is
$$
 \sum_{j=p}^{12}\frac{j!}{(j-p)!}h^{j-p}
 \|\partial_\phi^q w_{1,j}\|_{A_\sigma}.
\tag{T.15}
$$
Only the eighteen missing degree/width norm rows are new; the original widths are $0,1/1024,1/512$. Three new degree-twelve budgets combine the original norm rows, new norm rows, T.13--T.15 and original complete local coefficient majorants. The old three budgets remain unchanged. Sup and Wiener outputs are labelled separately.

No numerical improvement is asserted before an actual successful public child. Large upper bounds are not lower bounds or a proof of failure.

## T.5. Recovery and remaining obligations

Exact sources, runtime, both original natives and the complete stage inventory are pinned. Every new natural stage is saved atomically and resumes only under matching identities. Mathematical success and publication failure remain distinct. All new arithmetic runs only in this public repository's Actions; real pulls and both README diffs follow its rules.

This supplies higher coefficients and local derivative budgets for subsequent consumers, including the exact root-value subtraction. It does not pay uncomputed old-circle or independent-mean source norms, physical seam errors, positive affine ports, complete strong return, full low/high Schur closure, a nonlinear state ball, holonomy or the final family.
