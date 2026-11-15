# R133 supplement: correlated complete local numerator from the accepted old-radial Taylor table

**Status.** This is a proved analytic consumption contract. Its new finite convolution, scalar norm and complete remainder budgets still require their own public Actions execution. No improvement or cutoff is assumed in advance.

The inputs are the same complete first correction at fixed $\eta_0$, the same complex parameter disk $|\delta|\le10^{-8}$, the same original physical root piece, and the already completed [Taylor table through degree twelve](R133-supplement-actual-append-only-old-rho-Airy-Taylor-through-twelve.md). The principal-factor convention is the corrected one from [the exact fold construction](R133-supplement-exact-fold-matrix-cancellation-and-leading-inverse-defect.md). The full old-circle and independent-mean terms remain governed by [the complete first-correction source contract](R133-supplement-exact-old-mean-compression-and-first-correction-nonlocal-budgets.md).

## N.1. Exact differential operator and carrier sign

Use the original old radial coordinate and physical angle,

$$
\rho=r_*-r,\qquad
D=\partial_r-d\partial_\phi=-\partial_\rho-d\partial_\phi.
$$

For a two-amplitude column $w=(a,b)^t$ define the complete local numerator

$$
\mathcal N_\varepsilon w
=
\left[
\partial_\rho^2
+2d\,\partial_\rho\partial_\phi
+c_1\partial_\phi+c_2\partial_\phi^2
+T_0\partial_\rho+V_0
\right]w
+i\varepsilon\,\vartheta Q
\begin{pmatrix}0&T\\1&0\end{pmatrix}w,
\tag{N.1}
$$

where

$$
c_1=d_\rho+d\,d_\phi+T_0d,
\qquad
c_2=d^2+\eta^2K.
\tag{N.2}
$$

Every multiplication in these expressions occurs after the displayed derivative. In particular, no derivative is moved through $d,T_0,Q,T$ or $\vartheta$.

Equation (N.1) follows by expanding $D^2-T_0D$ in the old variables and using the exact fold identity

$$
H^{-1}H_D=-i\varepsilon Q
\begin{pmatrix}0&T\\1&0\end{pmatrix}.
$$

The remaining second angular coefficient is $+\eta^2K$, with its actual signed $K$. Thus (N.1) is the same unnormalized operator used in the accepted complete forcing stages. The principal factor is

$$
\mu=Q^2(X_\phi^2+TT_\phi^2),
\tag{N.3}
$$

and $\mathcal N_\varepsilon w=\mu L_0w$. No division by $\mu$ is made when constructing the local first-row source $JP\,S(\mathcal N_\varepsilon w)$.

This paragraph concerns only the exact local numerator. It does not remove any of the separate old-circle $I/J$ or independent even-mean terms.

## N.2. The finite correlated coefficients

Let

$$
w_1(\rho,\phi)=\sum_{j\ge0}w_j(\phi)\rho^j,
\qquad
w_j=(a_j,b_j)^t.
$$

The actual Taylor extension supplies $w_j$ for $0\le j\le12$, all operator coefficients needed through degree ten, and the complete non-circular Fourier arrays of each coefficient.

For $0\le n\le10$, define the new finite outputs by

$$
N_n=[\rho^n]\,\mathcal N_\varepsilon w_1.
\tag{N.4}
$$

The coefficient $N_n$ requires at most $w_{n+2}$, so no derivative or Taylor coefficient beyond the accepted degree twelve is requested. Multiplication by any coefficient in (N.1) is a complete Taylor convolution at that degree. Angular differentiation multiplies Fourier index $j$ by the physical factor $4ij$.

For the first component, (N.4) is explicitly

$$
\begin{aligned}
(N_n)_a={}&(n+2)(n+1)a_{n+2}\\
&+2\sum_{i+j=n}d_i(j+1)\partial_\phi a_{j+1}\\
&+\sum_{i+j=n}(d_\rho+d\,d_\phi)_i\partial_\phi a_j
+\sum_{i+j=n}(d^2+\eta^2K)_i\partial_\phi^2a_j\\
&+\sum_{i+j=n}(T_0)_i(j+1)a_{j+1}
+\sum_{i+j=n}(T_0d)_i\partial_\phi a_j\\
&+\sum_{i+j=n}(V_0)_i a_j
+i\varepsilon\sum_{i+j=n}(\vartheta Q)_i(Tb)_j.
\end{aligned}
\tag{N.5}
$$

The second component is obtained by replacing each displayed $a$ by $b$ and the final $(Tb)_j$ by $a_j$.

All signed summands in each complete Fourier coefficient are added **before** taking any absolute value or norm. This is the only new correlation claimed: it concerns the actual local residual of the same first correction. No cancellation is inferred merely from a small floating-point centre.

The already saved complete helpers $\vartheta Q$ and $T_0d$ are read directly. The original background drift prefix, local operator prefix, leading $T$ prefix and first-correction prefixes are also read directly. The only new finite outputs are the numerator coefficients and newly needed supporting derivatives or products. Original accepted stages are not regenerated.

## N.3. Complete mean and the other carrier sign

The Fourier coefficient at $j=0$ is retained in every product and every $N_n$. The constant coefficient of an Airy amplitude is not the independent old-circle mean of the reconstructed oscillatory function. It must not be removed in anticipation of the later projection $P$.

The accepted exact symmetry at the same complex parameter is

$$
a_{1,-}=-a_{1,+},
\qquad
b_{1,-}=b_{1,+}.
$$

All scalar coefficients in (N.1) are independent of $\varepsilon$. The cross term changes its explicit sign. Consequently,

$$
(\mathcal N_-w_{1,-})_a=-(\mathcal N_+w_{1,+})_a,
\qquad
(\mathcal N_-w_{1,-})_b=(\mathcal N_+w_{1,+})_b.
\tag{N.6}
$$

Both original Airy carrier branches therefore have the same absolute numerator bounds. This is an algebraic symmetry, not complex conjugation or a restriction to real $\delta$.

## N.4. The existing complete complex product domain

Write

$$
R=\frac1{6000},
\qquad
\Sigma=\frac1{128},
\qquad
h=\frac{90000009}{10^{13}}.
\tag{N.7}
$$

The old-product certificate proves holomorphy and complete bounds for the same $w_1$ on $|\rho|\le R$, $|\operatorname{Im}\phi|\le\Sigma$, uniformly on the original complex $\delta$ disk. Let its accepted amplitude bounds be $M_a,M_b$.

The required coefficient bounds are restrictions of the already accepted complete auxiliary coefficient and fold bounds to this product domain. In the actual auxiliary case, the coefficient rectangle and fold domain are larger than (N.7); the old-product image gates and common physical-piece identity must still be checked. The consumer may not replace these complex bounds by the smaller real-circle table.

The physical conclusion is only on the original inner interval with $|\rho|\le h$. The same one-piece analytic extension is used for Cauchy estimates. No continuation of the physical background across any original seam is asserted.

## N.5. Six complete multiplier bounds

Let $D_0,D_1,D_{\rho,0},\eta_+,K_+,T_+,V_+,\vartheta_+,Q_+,T_{\max}$ be accepted nonnegative upper bounds on the corresponding complete holomorphic coefficients on (N.7). Here $T_+$ denotes the bound for the scalar coefficient $T_0$, while $T_{\max}$ bounds the fold coordinate $T$.

The following are valid whole-product bounds for the grouped multipliers:

$$
\begin{aligned}
C_{11}&=2D_0,\\
C_{01}&=D_{\rho,0}+D_0D_1+T_+D_0,\\
C_{02}&=D_0^2+\eta_+^2K_+,\\
C_{10}&=T_+,\\
C_{00}&=V_+,\\
C_{ab}&=\vartheta_+Q_+T_{\max},
\qquad
C_{ba}=\vartheta_+Q_+.
\end{aligned}
\tag{N.8}
$$

The first two subscripts indicate the radial and angular derivative orders on the same amplitude. The two final constants multiply the other amplitude without a derivative.

These bounds pay all radial coefficient variations. A coefficient such as $c_1$ may be bounded by (N.8), while its finite coefficients in (N.5) are still evaluated with their full signs. Bounding a complete multiplier does not erase the correlation in its retained finite prefix.

## N.6. Radial coefficient-tail lemma

Suppose $c,w$ are holomorphic on the product domain and

$$
\|c\|\le C,\qquad \|w\|\le M.
$$

Cauchy in $\rho$ gives $\|c_i\|\le CR^{-i}$ and $\|w_j\|\le MR^{-j}$ on the same angular strip. For a nonnegative radial derivative order $p$,

$$
\left\|[\rho^n](c\,\partial_\rho^p w)\right\|
\le
CMR^{-n-p}\,
p!\binom{n+p+1}{p+1}.
\tag{N.9}
$$

Indeed, its coefficient is the sum over $i+j=n$ of
$c_i (j+p)!w_{j+p}/j!$, and

$$
\sum_{j=0}^{n}\frac{(j+p)!}{j!}
=
p!\binom{n+p+1}{p+1}.
$$

No unpaid coefficient is evaluated in (N.9); it bounds the entire missing tail from the whole-product certificate.

For the bare $\partial_\rho^2w$, the sharper coefficient factor is $(n+2)(n+1)$, since the multiplying coefficient is the exact constant one.

## N.7. Positive closed forms for the complete radial tails

Let $t=h/R<1$, $m=11$ and $d=1-t$. Define

$$
\begin{aligned}
U(t)&=
\frac{(m+1)(m+2)t^m}{d}
+\frac{2(m+2)t^{m+1}}{d^2}
+\frac{2t^{m+2}}{d^3},\\
V_0(t)&=
\frac{(m+1)t^m}{d}
+\frac{t^{m+1}}{d^2},\\
V_1(t)&=\frac12U(t).
\end{aligned}
\tag{N.10}
$$

These are exactly

$$
\begin{aligned}
U(t)&=\sum_{n\ge11}(n+2)(n+1)t^n,\\
V_0(t)&=\sum_{n\ge11}(n+1)t^n,\\
V_1(t)&=\sum_{n\ge11}\frac{(n+1)(n+2)}2t^n.
\end{aligned}
$$

Every term in (N.10) is nonnegative. A directed interval evaluation can therefore bound them without subtracting a nearly equal finite prefix from a full geometric series.

The appropriate radial factors in the numerator tail are $R^{-2}U$ for the bare second radial derivative, $R^{-1}V_1$ for a multiplier times one radial derivative, and $V_0$ for a multiplier times no radial derivative.

## N.8. Complete angular strip-sup constants

Fix an output strip $0\le\sigma<\Sigma$ and set $\Delta=\Sigma-\sigma>0$. For an output angular derivative order $k$, the bare second radial derivative has angular factor

$$
B_k(\Delta)=\frac{k!}{\Delta^k}.
\tag{N.11}
$$

For a multiplier times $\partial_\phi^q w$, a valid factor is

$$
G_{q,k}(\Delta)=
\begin{cases}
k!\,\Delta^{-k},&q=0,\\[2mm]
\dfrac{(q+k+1)!}{q+1}\,\Delta^{-q-k},&q\ge1.
\end{cases}
\tag{N.12}
$$

For $q=0$, apply Cauchy directly to the product of the two bounded coefficient functions. For $q\ge1$, Leibniz and separate Cauchy estimates give

$$
\sum_{\ell=0}^{k}
\binom{k}{\ell}\ell!(q+k-\ell)!
=
\frac{(q+k+1)!}{q+1}.
$$

This pays the derivative of the multiplier as well as the derivative of $w$; it never commutes $\partial_\phi$ through a varying coefficient for free.

## N.9. A complete strip-sup remainder for each numerator component

With $U,V_0,V_1$ from (N.10), define

$$
\begin{aligned}
\mathcal E_k={}&
R^{-2}U\,B_k
+C_{11}R^{-1}V_1G_{1,k}
+C_{01}V_0G_{1,k}
+C_{02}V_0G_{2,k}\\
&+C_{10}R^{-1}V_1G_{0,k}
+C_{00}V_0G_{0,k}.
\end{aligned}
\tag{N.13}
$$

Then the complete degree-ten numerator tails obey

$$
\begin{aligned}
\left\|\partial_\phi^k
\left((\mathcal N_\varepsilon w_1)_a-
\sum_{n=0}^{10}(N_n)_a\rho^n\right)\right\|_\sigma
&\le M_a\mathcal E_k+M_bC_{ab}V_0G_{0,k},\\
\left\|\partial_\phi^k
\left((\mathcal N_\varepsilon w_1)_b-
\sum_{n=0}^{10}(N_n)_b\rho^n\right)\right\|_\sigma
&\le M_b\mathcal E_k+M_aC_{ba}V_0G_{0,k}.
\end{aligned}
\tag{N.14}
$$

The factors $M_a,M_b$ are the complete bounds of the original first correction, including its constant modes and its analytic tail. They are not bounds of the retained Taylor polynomial alone.

The finite part is bounded from the complete signed Fourier outputs $N_n$:

$$
\sum_{n=0}^{10}
h^n\|\partial_\phi^k(N_n)_a\|_{\mathcal A_\sigma},
\qquad
\sum_{n=0}^{10}
h^n\|\partial_\phi^k(N_n)_b\|_{\mathcal A_\sigma}.
\tag{N.15}
$$

Adding (N.14) to (N.15) gives a complete strip-sup bound. No tail coefficient or Fourier output is silently set to zero.

## N.10. Separately labelled Wiener remainder

For $z=e^{-4\Delta}$, define the complete two-sided Fourier sums

$$
S_q(\Delta)=
\sum_{j\in\mathbb Z}(4|j|)^q e^{-4|j|\Delta},
$$

with the $j=0$ term equal to one for $q=0$ and zero otherwise. The needed closed forms are

$$
\begin{aligned}
S_0&=\frac{1+z}{1-z},&
S_1&=\frac{8z}{(1-z)^2},&
S_2&=\frac{32z(1+z)}{(1-z)^3},\\
S_3&=\frac{128z(1+4z+z^2)}{(1-z)^4},&
S_4&=\frac{512z(1+11z+11z^2+z^3)}{(1-z)^5}.
\end{aligned}
\tag{N.16}
$$

For the bare second radial derivative, replace $B_k$ by $S_k(\Delta)$. For $q=0$, replace $G_{0,k}$ by $S_k(\Delta)$, since the product is bounded on the whole original strip.

For $q\ge1$, either of the following complete factors is valid:

$$
\begin{aligned}
W_{q,k}^{(1)}
&=\sum_{\ell=0}^{k}\binom{k}{\ell}
S_\ell(\Delta)S_{q+k-\ell}(\Delta),\\
W_{q,k}^{(2)}
&=q!\left(\frac2\Delta\right)^q S_k(\Delta/2).
\end{aligned}
\tag{N.17}
$$

The first follows from the full convolution and
$|j+\ell|^k\le\sum_{s=0}^k\binom ks |j|^s|\ell|^{k-s}$.
The second pays the $q$ derivatives of $w$ on the intermediate strip
$\Sigma-\Delta/2$, then converts the bounded product to the final complete Fourier norm with the remaining half width. Their minimum is another valid complete estimate of the same quantity.

Use these factors in (N.13)–(N.14), and add the same finite sums (N.15), to obtain independently labelled analytic Wiener bounds. They are not replaced by the smaller strip-sup estimates.

Orders $0\le k\le2$ and the operator derivatives $q\le2$ require only $S_0,\ldots,S_4$. They do not require new high radial target derivatives.

## N.11. Faithful numerical consumption

A conforming public consumer must:

- pin the actual complete Taylor12 native, its zero-return process, the accepted auxiliary fold native and its process, the unchanged complete Laurent algebra, and every natural finite file that it reads;
- verify the fixed $\eta_0$, exact complex $\delta$ disk, root interval, original physical piece and old-product domains;
- read original stage payloads without rebuilding them, and keep their original source, manifest, algebra and runtime identities distinct from the new source identity;
- form all complete $N_0,\ldots,N_{10}$ before taking their norms, retaining the constant coefficient and full supports;
- evaluate the entire positive tails (N.10), the complete angular factors, and both finite-plus-tail norm families with directed rounding;
- checkpoint each new natural coefficient, norm and budget stage, and reuse an accepted new stage only with the exact same new source, manifest, runtime and original inputs.

It may also retain the original triangle bounds as an independent comparison or take a minimum between two complete estimates of the same numerator. It must not report improvement before an actual gate has established the relevant quantities.

## N.12. Scope for the next source consumer

The output of this contract is a complete bound for $\mathcal N_\varepsilon w_1=\mu L_0w_1$ and its first two physical angular derivatives on the original inner cover, at declared positive strips or the real circle.

A subsequent complete local-source consumer can insert those actual amplitudes into the real or analytic all-output Airy estimates, then apply the original $JP$ and the actual radial weights. The independent even-mean equation and every nonlocal word stay separate. The full first-corrected physical seam sources, positive weighted port, unknown high feedback and final return inverse are not paid by this contract.
