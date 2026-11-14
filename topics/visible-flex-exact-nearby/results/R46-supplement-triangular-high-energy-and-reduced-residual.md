# R46 supplement: a complete triangular derivative energy and a reduced exact WKB residual

2026-11-13. This result supplies a genuine all-frequency, whole-parameter integer derivative energy construction for the actual R37 operator. The new consumer has actually run through order 10 on the completed strict leaf 0060. Its source norm is the ordinary source norm required by R46; it does not change the R110 weak-source convention or treat a weak divergence load as an ordinary load.

The actual numerical execution covers only the displayed leaf. It does not claim the whole strict interval, either turning connection, the returned strong remainder, or an effective high cutoff. The precise composition law below permits further strict leaves to be joined without inserting a norm-equivalence factor at every interface.

## 1. Exact operator and normalization

Use the unchanged physical angle theta, of period pi/2, and its full frequency lattice 4Z. Let

\[
Pu=\partial_r(a u_r+b u_\theta)
  +\partial_\theta(bu_r+cu_\theta)+d u=f,\qquad
p=a u_r+b u_\theta.
\]

Here all coefficients are those of the fixed R37 type-corrected operator on the current actual family

\[
p_{\rm family}=p_5+\eta,\qquad
p_5=-7789843107295549/4611686018427387904,\qquad
|\eta|\le10^{-9}.
\]

To avoid confusion, the symbol p without the subscript family below is momentum, not the family parameter.

Write

\[
\alpha=a^{-1},\quad v=b/a,\quad
\gamma=(b^2-ac)/a,\quad
\nu=\sqrt{\alpha\gamma}>0,\quad D=\partial_\theta.
\]

The full potential is d=tau+D sigma. Take a positive radial weight lambda, either the actual lambda=-K0 or a fixed positive constant. On the closed strict interval, lambda,alpha,gamma are positive.

For an integer j>=0 set

\[
u_j=D^ju,\quad q_j=D^{j+1}u,\quad p_j=D^jp,\qquad
e_j^2=\int(\lambda|u_j|^2+\gamma|q_j|^2+\alpha|p_j|^2).
\tag{1}
\]

The angular measure is normalized over the complete physical period. The zero mode is retained.

## 2. The diagonal high-order rate contains only first characteristic derivatives

The base constraint-preserving system is

\[
u_r=\alpha p-vq,\qquad
q_r=D(\alpha p-vq),\qquad
p_r=D(\gamma q-vp)-du+f.
\tag{2}
\]

For the j-th derivatives, separate the exact top terms:

\[
\begin{aligned}
(u_j)_r&=\alpha p_j-vq_j+U_j,\\
(q_j)_r&=\alpha Dp_j-vDq_j
 +(j+1)\alpha_\theta p_j-(j+1)v_\theta q_j+Q_j,\\
(p_j)_r&=\gamma Dq_j-vDp_j
 +(j+1)\gamma_\theta q_j-(j+1)v_\theta p_j-du_j+P_j+D^jf.
\end{aligned}
\tag{3}
\]

All lower terms are

\[
\begin{aligned}
U_j&=\sum_{\ell<j}\binom j\ell
 [D^{j-\ell}\alpha\,p_\ell-D^{j-\ell}v\,q_\ell],\\
Q_j&=\sum_{\ell<j}\binom{j+1}\ell
 [D^{j+1-\ell}\alpha\,p_\ell-D^{j+1-\ell}v\,q_\ell],\\
P_j&=\sum_{\ell<j}\binom{j+1}\ell
 [D^{j+1-\ell}\gamma\,q_\ell-D^{j+1-\ell}v\,p_\ell]
 -\sum_{\ell<j}\binom j\ell D^{j-\ell}d\,u_\ell .
\end{aligned}
\tag{4}
\]

These are exact Leibniz identities, including j=0, for which the sums are empty.

Let H0 be the normalized real symmetric energy matrix of R110 (110.6), derived using the actual constraint q=D u. The same constraint q_j=D u_j holds at every level. Repeating the integration by parts gives

\[
H_j=H_0+
2j\begin{pmatrix}
0&0&0\\
0&-v_\theta&\nu_\theta\\
0&\nu_\theta&-v_\theta
\end{pmatrix}.
\tag{5}
\]

Indeed the extra q,p cross term before normalization is
j(gamma alpha_theta+alpha gamma_theta); division by sqrt(alpha gamma)=nu gives 2j nu_theta. This uses the exact product identity alpha gamma=nu^2. It does not bound the two derivatives separately before cancellation.

Consequently, if g_+ and g_- are the complete base energy rates of R110, define

\[
\chi_+=\sup_{\theta,r,\eta}\max(0,-v_\theta+|\nu_\theta|),\qquad
\chi_-=\sup_{\theta,r,\eta}\max(0,v_\theta+|\nu_\theta|).
\tag{6}
\]

The normalized top rate is bounded forward by g_++2j chi_+ and backward by g_-+2j chi_-. Higher angular coefficient derivatives do not appear on this diagonal.

The two characteristic speeds are v+-nu. Thus (6) is precisely a bound on their signed first angular derivatives. No approximation to a radial background is made.

## 3. Every lower derivative remains in a triangular source matrix

Let alpha_+/-, gamma_+/-, lambda_+/- be positive full real bounds on the same closed interval. Suppose

\[
A_n(z)\ge\sup_r\sum_{k\in\mathbb Z}|4k|^n|\widehat z_k(r)|
\]

for n>0, and use weight one at k=0 when n=0. Then A_n(z) bounds the full L-infinity norm of D^n z.

For 0<=ell<j put n=j-ell, c0=binom(j,ell), c1=binom(j+1,ell). A complete bound on the map from the ell-th weighted energy state to the forcing in (3) is the Frobenius norm of the following explicit nonnegative matrix:

\[
B_{j\ell}=
\begin{pmatrix}
0&
c_0 A_n(v)\sqrt{\lambda_+/\gamma_-}&
c_0 A_n(\alpha)\sqrt{\lambda_+/\alpha_-}\\
0&
c_1 A_{n+1}(v)\sqrt{\gamma_+/\gamma_-}&
c_1 A_{n+1}(\alpha)\sqrt{\gamma_+/\alpha_-}\\
c_0 A_n(d)\sqrt{\alpha_+/\lambda_-}&
c_1 A_{n+1}(\gamma)\sqrt{\alpha_+/\gamma_-}&
c_1 A_{n+1}(v)\sqrt{\alpha_+/\alpha_-}
\end{pmatrix}.
\tag{7}
\]

All entries follow directly from (4), multiplying each output row by the square root of its energy weight and each input column by the reciprocal square root. Taking its Frobenius norm only enlarges the true Euclidean operator norm.

Define two lower triangular matrices C_+ and C_- by

\[
(C_\pm)_{jj}=\max(0,g_\pm/2+j\chi_\pm),\qquad
(C_\pm)_{j\ell}=\|B_{j\ell}\|_{\rm F}\quad(\ell<j),
\tag{8}
\]

and zero above the diagonal. The energy derivative and Cauchy--Schwarz imply, in the upper Dini derivative sense,

\[
\frac{d}{dr}e_j
 \le (C_+)_{jj}e_j+\sum_{\ell<j}(C_+)_{j\ell}e_\ell
      +\sqrt{\alpha_+}\|D^jf\|_2 .
\tag{9}
\]

At e_j=0 the same statement follows by first replacing e_j by sqrt(e_j^2+epsilon^2) and then taking epsilon to zero. Reversing the radial direction gives (9) with C_-. The matrices are Metzler and entrywise nonnegative, so variation of constants gives a comparison for the entire vector of energies:

\[
e(r_1)\le e^{L C_+}e(r_0)
 +\int_{r_0}^{r_1}e^{(r_1-r)C_+}\sqrt{\alpha_+}
   (\|f\|_2,\|Df\|_2,\ldots,\|D^kf\|_2)^t\,dr.
\tag{10}
\]

The backward statement uses e^{L C_-}. The inequalities are componentwise. The same complete interval matrices bound every subinterval, since all entries are nonnegative.

This is a full PDE estimate, not an estimate of a finite Galerkin system. Friedrichs approximation preserves the uniform estimate; weak compactness constructs the actual solution, the backward estimate gives uniqueness and onto propagation, and the constraint is preserved because the first equation differentiated is the second equation.

## 4. Conversion to the exact R46 Cauchy scale

For this physical angular normalization let

\[
\|(u,p)\|_{\mathcal P_s}^2
=\|u\|_{H^{s+1/2}}^2+\|p\|_{H^{s-1/2}}^2,
\quad
\|v\|_{H^t}^2=\sum_{k\in\mathbb Z}(1+16k^2)^t|\widehat v_k|^2.
\]

Put h_-=min(lambda_-,gamma_-,alpha_-) and
h_+=max(lambda_+,gamma_+,alpha_+). The exact binomial identity gives

\[
h_-\|(u,p)\|_{\mathcal P_{k+1/2}}^2
\le\sum_{j=0}^k\binom kj e_j^2
\le h_+\|(u,p)\|_{\mathcal P_{k+1/2}}^2.
\tag{11}
\]

The identity uses both u and q=D u:

\[
\sum_{j=0}^k\binom kj
 (\|D^ju\|_2^2+\|D^{j+1}u\|_2^2+\|D^jp\|_2^2)
=\|u\|_{H^{k+1}}^2+\|p\|_{H^k}^2.
\]

Let W_k=diag(sqrt(binomial(k,j))) for j=0,...,k and let the subscript <=k mean the corresponding principal matrix. A sufficient full Cauchy bound is

\[
E^\pm_{k+1/2}
=\sqrt{h_+/h_-}\,
 \|W_k(e^{LC_\pm})_{\le k}W_k^{-1}\|_2.
\tag{12}
\]

The ordinary L1(dr;H^k) source gain is bounded by the same matrix norm times sqrt(alpha_+/h_-). This follows from (10), (11), and the exact H^k binomial norm of the source. It contains the mean and both height/momentum components.

The actual Green flux preserved by P is unchanged. Its duality pairs P_s with P_{-s}. Applying the positive-order bound to the backward propagator therefore pays the negative-order bound. Hilbert interpolation between adjacent half-integer spaces then pays every real finite window. In particular P_10 is paid by the geometric mean of the P_9.5 and P_10.5 bounds, and this is the intermediate s+2 space required in R46 when s=8.

If another calculation uses a normalized 2pi angular variable x=4theta with weights (1+k^2), the norm conversion must be made explicitly. The present report declares physical weights (1+16k^2); it does not silently identify them with another root or final-circle label.

## 5. Joining radial cells without repeated norm conversion

At an actual common radius, lambda,alpha,gamma and the solution agree. Therefore each e_j in (1) agrees exactly on both sides. For consecutive cells the correct comparison is

\[
e(r_N)\le
 e^{L_{N-1}C_{N-1}}\cdots e^{L_0C_0}e(r_0)
 +\text{the corresponding propagated ordinary-source integrals}.
\tag{13}
\]

Only the initial and final forms of (11) are needed. Multiplying sqrt(h_+/h_-) separately at every leaf is neither necessary nor the convention of the new source.

Piecewise scalar germs are allowed provided the actual principal coefficients and conormal traces match. The estimates use only the displayed one-sided radial derivatives and integrate them. No additional source jump is inserted at a smooth common knot.

## 6. Complete high derivative moments from the actual coefficient rectangle

The numerical consumer is

    scripts/fourfold_strict_high_energy_triangular.py

It first verifies the complete R110 base energy source and dependency hashes, the complete nine-field rectangle source, its dependency hashes and its saved coefficient tensor. The parameter identity must be the entire real family, and the base report must have paid both the closed radial interval and the whole real angle circle.

The underlying saved dyadic polynomial is a complete rectangular Taylor/Fourier approximation. It includes a separate error radius for every retained coefficient. For each physical angular order through 11 the consumer retains:

1. the full finite polynomial on the closed real time interval;
2. all recorded selected-coefficient errors, including the producer's DFT, alias and choice errors;
3. every unretained angular frequency;
4. every unretained radial Taylor coefficient at retained angular frequencies.

No A0/A1/A2 error is extrapolated to a higher derivative. The actual saved coefficient error tensor and the original complete analytic bidisk are reread.

For a true normalized angular strip S and q=exp(-S), the infinite derivative tail is evaluated by the exact positive rational identity

\[
\sum_{k=K+1}^\infty k^n q^k
=q^{K+1}\sum_{\ell=0}^n\binom n\ell(K+1)^{n-\ell}
 \sum_{j=0}^{\ell}
 \left\{\begin{matrix}\ell\\j\end{matrix}\right\}
 \frac{j!q^j}{(1-q)^{j+1}}.
\tag{14}
\]

The braces are Stirling numbers of the second kind. The recurrence
S(ell,j)=S(ell-1,j-1)+j S(ell-1,j) proves (14) by repeatedly applying q d/dq to 1/(1-q). The physical derivative weight 4^n and the two signs of every nonzero Fourier frequency are included.

A useful refinement is made before multiplying by high derivative weights. At every retained frequency, the true coefficient has both the saved polynomial/error enclosure and the original analytic Cauchy bound M exp(-S|k|). The consumer intersects these two absolute bounds:

\[
|\widehat f_k(r)|
\le\min\left(
 |\widehat p_k(r)|+E_k+
 M e^{-S|k|}\frac{R^{-m}}{1-R^{-1}},
 \ M e^{-S|k|}
\right).
\tag{15}
\]

This prevents a common nodal interval error from being interpreted as a real flat high-frequency spectrum. Both bounds concern the same entire true coefficient and the same parameter family. The comparison does not discard a true mode.

Finally d=tau+D sigma is used with all orders, so A_n(d)<=A_n(tau)+A_{n+1}(sigma). The derivative nu_theta in (6) is evaluated on every actual closed angle cell by

\[
\nu_\theta
=\frac{\gamma\alpha_\theta+\alpha\gamma_\theta}
       {2\sqrt{\alpha\gamma}}.
\]

The existing complete true derivative errors and the complete interpolation gaps are included in those cell values.

## 7. Actual native execution through the required intermediate order

The executed input is

    data/native_core_20261113_ac0d/energy9_leaf0060_continuous.json

whose underlying nine-field rectangle is

    data/native_core_20261113_ac0d/energy9_leaf0060.json

The exact physical interval is

\[
I_{60}=
[6112257798907291/72057594037927936,\
 6124895493223875/72057594037927936].
\]

The whole real parameter interval is still p5+-10^-9. This is strictly negative curvature; no turning root or positive collar is crossed.

The saved final report is

    notes/2026-11-13-R46-actual-leaf0060-integer-energy10-v2.json

with SHA256

    b5ddf7396fadbd7b8e8d29bbcaff0d242116837e5ccd72d8d6f80adc9e45443a

The actual full top rates satisfy

\[
\chi_+<29.070591,\qquad \chi_-<41.522810,
\]

and the R110 base energy rates are less than 14.051964 forward and 23.605836 backward. Thus no derivative of order >=2 is placed on the exponential diagonal.

Conservative complete Cauchy bounds after endpoint norm conversion and interpolation are:

| Physical P_s space | Bound, both directions and every subinterval of I60 |
| --- | ---: |
| s=1 | 10.102 |
| s=2 | 233.527 |
| s=3 | 29950 |
| s=4 | 5828377 |
| s=5 | 2.0390e9 |
| s=6 | 1.3947e12 |
| s=7 | 1.4482e15 |
| s=8 | 1.7456e18 |
| s=9 | 2.2191e21 |
| s=10 | 2.9021e24 |

These are genuine finite high-order bounds, and the large constants are displayed rather than treated as an effective final inverse. The report retains the full 11-by-11 comparison generators and exponentials, all high-order derivative budgets, all half-integer ordinary-source gains and the exact family/interval identity.

The preliminary report without the per-frequency Cauchy intersection is superseded and is not an input to this conclusion.

Reproduction in the topic directory:

~~~sh
python3 scripts/fourfold_strict_high_energy_triangular.py \
  --energy-report data/native_core_20261113_ac0d/energy9_leaf0060_continuous.json \
  --order 10 --angles 4096 --bits 256 \
  --out notes/2026-11-13-R46-actual-leaf0060-integer-energy10-v2.json
~~~

The source refuses an existing output path. The actual final native run took about 2.056 seconds.

## 8. A reduced exact expression for the actual R46 WKB residual

There is a second cancellation useful when paying the ordinary residual in R46. It is an algebraic identity for the same actual operator, without a smallness hypothesis.

Let

\[
\mu=\sqrt{b^2-ac},\quad m=\mu^{-1/2},\quad
L=\log\mu,\quad q=b/a,\quad\nu=\mu/a,
\]

\[
v_\sigma=q-\sigma\nu,\quad
D_\sigma=\partial_r+v_\sigma\partial_\theta,\quad
B_r=a_r+b_\theta-aL_r-bL_\theta.
\]

Let the actual label S_sigma satisfy D_sigma S_sigma=0. Define

\[
\mathcal F=m^{-1}P m,\qquad
g_\sigma=D_\sigma h_\sigma=
 \frac{\mathcal F}{2\mu S_{\sigma,\theta}}.
\]

Then the exact full residual is

\[
\boxed{
 P(mh_\sigma)
 =m\left[
 \mathcal Fh_\sigma+
 aD_\sigma g_\sigma+
 2\sigma\mu\,\partial_\theta g_\sigma+
 B_r g_\sigma
 \right].
}
\tag{16}
\]

In particular this expression does not require a separate bound on h_theta_theta.

To prove it, expand m^-1P(mw). Its principal part is a w_rr+2b w_rtheta+c w_thetatheta, its radial first-order coefficient is B_r, and its zero-order coefficient is F. Rewriting the principal part in D_sigma gives

\[
aD_\sigma^2+2\sigma\mu D_\sigma\partial_\theta
 -a(D_\sigma v_\sigma)\partial_\theta.
\]

The exact WKB amplitude identity for m implies that the remaining coefficient of w_theta is 2 sigma mu v_sigma,theta after the B_r D_sigma part is removed. This can also be checked directly from mu=a nu:

\[
b_r+c_\theta-bL_r-cL_\theta
-v_\sigma B_r-aD_\sigma v_\sigma
=2\sigma\mu\,v_{\sigma,\theta}.
\]

Since partial_theta D_sigma=D_sigma partial_theta+v_sigma,theta partial_theta, the complete differential part is

\[
aD_\sigma^2+2\sigma\mu\,\partial_\theta D_\sigma+B_rD_\sigma.
\]

Substitution of w=h_sigma proves (16). Every coefficient is the original full coefficient, including d. Its multiplication by the actual m and the R46 initial momentum defect are still required. Formula (16) does not identify the reduced R106 density D with F/mu, and it does not remove the two root finite parts.

The remaining work for the full R46 numerical conclusion is the whole strict radial cover, actual F and its first derivatives in (16), actual h and S composition bounds, the complete frame and all cross-cone/mean outputs. The present exact cancellation and actual high-order energy consumer are inputs to that work.

