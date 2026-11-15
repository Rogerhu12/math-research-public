# R133 supplement: signed common-potential Taylor series on the whole original root piece

2026-11-15, visible-exact / phase_inverse.

**Proved identities and a complete finite recipe; new signed Taylor norms remain to be executed.** The common radial potential changes exactly one normalized forcing component. Its contribution to the first correction can be solved by one explicit radial integral. The old accepted first-correction coefficients can therefore be reused unchanged as inputs to a new signed addition. They are not relabeled as the new solution.

The proof gives the actual coordinate composition, the required finite orders, a whole-product tail with all Fourier outputs and the independent mean, and the precise remaining source terms. It does not assert a new full strong-return constant or a cutoff inverse.

## 1. Fixed object and an already paid common domain

Use [the signed genuine-reference identity](R133-supplement-signed-first-forcing-and-root-cancellation-for-genuine-common-reference.md), (F.1)--(F.22), and [the common radial potential](R133-supplement-minimal-complete-common-radial-potential-and-derivative-budget.md). The intrinsic parameter is the original fixed $\eta_0$; the true root is independent of the explicit parameter on this window. Write
$$
 \rho=r_*-r,\qquad
 |\Re\delta|,|\Im\delta|\le10^{-8},\qquad
 |\Re z|,|\Im z|\le97^{-2},\qquad z=j^{-2},\quad |j|\ge97.
 \tag{T.1}
$$
All algebra is bilinear over the complex parameter family. Both signs $\epsilon=\operatorname{sgn}j$ and the physical frequency $n=4|j|$ remain. The parameter value $z=0$ is the infinite-frequency radial limit, not the physical even mean.

The actual nonradial fold and its radial counterpart are
$$
 T(\rho,\phi)=-\rho A(\rho,\phi)^{2/3},\qquad
 \overline T(\rho)=-\rho\overline A(\rho)^{2/3},\qquad
 \overline A(\rho)=\frac32\int_0^1s^{1/2}a_\infty(s\rho)\,ds,
 \quad a_\infty=\eta\sqrt{k}.
 \tag{T.2}
$$
The common root normalization is $\overline T_1=T_1=-\kappa_*$, where
$\kappa_*=a_\infty(0)^{2/3}\ne0$. In particular $r$ differentiation is
$-\partial_\rho$ before any coordinate composition.

[The actual complete potential and image result](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md) gives, on the common reference disk $|\rho|\le H=1/6000$, the holomorphic potential $V(z,\overline T(\rho))$, its first two $T$ derivatives, and a uniformly single-valued inverse of $\overline T$ on a disk about zero. The guaranteed old-fold radius exceeds $8.006066537225\,10^{-5}$, on the full old-angle strip $|\Im\phi|\le3/128$. Thus the smaller closed product
$$
 |\rho|\le R_s=\frac3{40000},\qquad
 |\Im\phi|\le\Sigma=\frac1{128}
 \tag{T.3}
$$
maps strictly inside that common image. The extra factor two in the original image gate leaves a strict inclusion; this is not an extrapolation of the radial potential at the same physical $r$.

The complete original physical piece2549 has worst root cover
$$
 h_*=\frac{893368603925465506687}
             {21990232555520000000000000}
       <\frac{41}{10^6}<R_s.
 \tag{T.4}
$$
Its two sides use the same analytic root germ. Mathematical continuation of that germ outside piece2549 is not identified with a different physical cubic. In particular this proof changes none of the actual coefficients or nonzero entry data on pieces2547,2548,2550,2551.

## 2. The finite signed radial potential uses no new intrinsic derivative

Let $v(z,\rho)=V(z,\overline T(\rho))$. The complete original ordinary intrinsic derivatives through order15 and the accepted background/characteristic Taylor coefficients through degree14 are the inputs already used by the preceding potential calculation and the [append-only degree12 construction](R133-supplement-append-only-old-rho-Airy-Taylor-through-twelve.md).

For clarity the nonsingular formula being expanded is
$$
 \ell=\frac{\eta_r}{\eta}+\frac{k_r}{2k}
                 -\frac{\overline A_r}{3\overline A},\qquad
 q=D_{\rm rad}+\frac{\eta_r}{\eta}
                       +\frac{\theta_r}{1+\theta},
 \quad \theta=\frac{z\alpha}{\eta},
$$
$$
 c=\frac{k_r}{4k}-\frac{\overline A_r}{6\overline A}
                    -\frac{D_{\rm rad}}2
                    -\frac{\theta_r}{2(1+\theta)},\qquad
 \kappa=a_\infty\overline A^{-1/3},
$$
$$
 v=\kappa^{-2}
   \left[-c_r+\frac{c(\ell+q)}2
                    -16K(2\eta\alpha+z\alpha^2)\right].
 \tag{T.5}
$$
Here $D_{\rm rad}$ and $\alpha$ are the exact radial diagonal quantities of the common-reference theorem, with every intermediate label $1\le l\le96$ and denominator $1-l^2z$ retained. They are not the old transport derivation $D=\partial_r-d\partial_\phi$. Every derivative in (T.5) is at fixed $z$.

To form $v_0,\ldots,v_{12}$ one needs $c$ through degree13. This uses $\eta,k,\overline A,\alpha$ through degree14. The identity $K=-\rho k$ gives
$$
 k_p=-K_{p+1},\qquad
 \overline A_p=\frac3{2p+3}(a_\infty)_p,\qquad0\le p\le14.
 \tag{T.6}
$$
Thus $k_{14}$ uses the already paid $K_{15}$, and no $K_{16}$ is requested. The coefficients of $\eta$ and $\alpha$ use the original degree96 family, its complete two repaired means, and the same intrinsic prefix. Constant piecewise value repairs have zero positive-order derivatives on this one piece; their values and the full direction mean are still in order zero. Their genuine physical derivative jumps are not discarded.

Taylor coefficients are ordinary derivatives divided by factorial. For data saved as ordinary $r$ derivatives, the conversion is exactly $(-1)^p/p!$. Reciprocal and fractional-power series use the declared nonzero constant and the previously paid holomorphic branch. No missing coefficient is padded with zero.

On the original complex $z$ square,
$$
 \Re(1-l^2z)\ge1-\frac{96^2}{97^2}=\frac{193}{9409}>0.
 \tag{T.7}
$$
This real-part bound is also a complete modulus lower bound. It must not be replaced by an interval-modulus routine that spuriously loses this known gap. The other denominators and branches retain the actual common-potential gates.

## 3. The actual old-angle composition

Define the single analytic inverse composition
$$
 \sigma(\rho,\phi)=\overline T^{-1}(T(\rho,\phi)),
 \qquad \sigma_0=0,\quad \sigma_1=1.
 \tag{T.8}
$$
It is well-defined on (T.3) by the genuine common image gate. The notation $\sigma$ here denotes a coordinate, not an angular strip width.

For $2\le m\le12$ its exact finite recurrence is
$$
 \sigma_m=\frac{T_m-
       \displaystyle\sum_{k=2}^{m}\overline T_k
                         [\sigma^k]_m}{\overline T_1}.
 \tag{T.9}
$$
In every term of the sum, the coefficient $[\sigma^k]_m$ only uses previously known $\sigma_1,\ldots,\sigma_{m-1}$. The leading zero and unit coefficient come from the exact shared root normalization; they are not obtained by projecting a nonzero numerical residual to zero.

The potential in the actual old circle is
$$
              {\cal V}(z,\rho,\phi)=v(z,\sigma(\rho,\phi)).
 \tag{T.10}
$$
There is no extra Jacobian in (T.10). It is a scalar composition. The sign $\partial_r=-\partial_\rho$ has already been used in (T.5) and must not be applied a second time because of (T.8).

Let $f=(f_b,f_a)^t=M_0^{-1}F$ be the original signed normalized forcing. Its new complete Taylor coefficients through degree12 are
$$
 (f_b^V)_m=(f_b)_m+[v(z,\sigma)]_m,\qquad
 (f_a^V)_m=(f_a)_m,\qquad0\le m\le12.
 \tag{T.11}
$$
All coefficients in (T.11) are summed as full Laurent polynomials before any modulus or norm. The original polynomial values are unchanged inputs. The new radial coefficients depend on the input label through $z$ and may not be assigned to the output Fourier label after a convolution.

## 4. An exact integral for the change of first correction

Here $A,B$ denote the normalized correction amplitudes, distinct from the fold coefficient $A$ in (T.2). In the original normalized canonical transport convention,
$$
 2A_T-2i\epsilon T B_X=f_a,\qquad
 2T B_T+B-2i\epsilon T A_X=f_b.
 \tag{T.12}
$$
The complete analytic root normalization is $A(0,X)=0$, $B(0,X)=f_b(0,X)$.

Because the extra forcing in (T.11) depends only on the actual canonical $T$, define
$$
 {\cal B}_j(T)=\frac12\int_0^1s^{-1/2}V_j(sT)\,ds .
 \tag{T.13}
$$
The path is in the same star-shaped image disk. Its integrable endpoint is ordinary scalar integration, not a new choice of root branch. Differentiating $s^{1/2}V_j(sT)$ gives
$$
 2T{\cal B}_j'(T)+{\cal B}_j(T)=V_j(T),\qquad
 {\cal B}_j(0)=V_j(0).
 \tag{T.14}
$$
Hence the exact correction to (T.12) is
$$
               \Delta A=0,\qquad \Delta B={\cal B}_j(T).
 \tag{T.15}
$$
Its $X$ derivative is zero at fixed canonical $T$; its old-angle derivative after (T.10) generally is not zero.

For the original leading matrix and amplitudes,
$$
 M_0=\begin{pmatrix}a_0&Tb_0\\b_0&a_0\end{pmatrix},
 \qquad w_1=M_0(A,B)^t ,
$$
the actual new first correction is therefore
$$
 \boxed{\quad
 w_1^V=w_1+
       \binom{Tb_0}{a_0}{\cal B}_j(T),\qquad
 a_1^V=a_1+Tb_0{\cal B}_j(T),\quad
 b_1^V=b_1+a_0{\cal B}_j(T).
 \quad}
 \tag{T.16}
$$
This is an exact signed addition to the old solution with its original root integration constant. It constructs a new solution of the new forcing equation. It does not rerun the old transport or rename its old solution. The old even physical source equation is independent of the scalar amplitude $B$ and has not been set to zero.

For each $p$ for which the complete potential derivative is bounded on this disk,
$$
 \sup|{\cal B}_j^{(p)}|
       \le\frac{\sup|V_j^{(p)}|}{2p+1}.
 \tag{T.17}
$$
In particular the already paid $p=0,1,2$ potential bounds apply. There is no free bound for an unpaid higher derivative. A derivative in old coordinates must use the actual chain rule for $T(\rho,\phi)$.

## 5. A scalar recurrence instead of a repeated transport solve

Set $b(z,\rho)={\cal B}_j(\overline T(\rho))$. Then
$$
       2\overline T\,b_\rho+\overline T_\rho b
                                      =\overline T_\rho v.
 \tag{T.18}
$$
Writing $\overline T=\sum_{k\ge1}t_k\rho^k$, one obtains
$$
 b_0=v_0,\qquad
 b_m=\frac{t_1v_m+
   \displaystyle\sum_{k=2}^{m+1}t_k
      \{k\,v_{m+1-k}-(2m+2-k)b_{m+1-k}\}}
                    {(2m+1)t_1},\quad1\le m\le12.
 \tag{T.19}
$$
Only earlier $b$ coefficients occur on the right. Degree12 uses at most $t_{13}$, already covered by the old degree14 leading prefix. In fact the last summand cancels identically because $b_0=v_0$; a consumer may use this exact identity instead of subtracting two copies of the same interval. The denominator is the nonzero shared root coefficient, not a small value of $\overline T$ away from the root.

Now form
$$
 {\cal B}_j(T(\rho,\phi))=b(z,\sigma(\rho,\phi))
 \tag{T.20}
$$
and the two signed additions in (T.16) through degree12. The old accepted coefficients of $a_1,b_1,a_0,b_0,T$ are read from their exact original stages. There is no new evaluation of an old target, FFT, intrinsic jet, fold, repaired cubic, normalized forcing or first-correction coefficient.

The resulting finite Fourier ranges are computed from complete convolutions. No output projection back to degree96, no finite-input square truncation, and no deletion of the zero Fourier coefficient is permitted. The unchanged $(f_a)_m$ is reused, not recomputed. If a separately paid complete root norm is compared with the new degree-zero norm, both must refer to the same whole operator and the same parameter/angle domain; a norm cannot be substituted for a signed Fourier coefficient.

## 6. Complete tails and the distinction between strip supremum and a joint Wiener norm

The old normalized forcing and first amplitudes have paid whole-product bounds on
$|\rho|\le R_0=1/6000$, $|\Im\phi|\le\Sigma=1/128$.
The accepted stage complete-original-reference-holomorphic-majorants preserves these exact domains. Its field names are:
$$
 {\tt f0}=f_a,\quad {\tt f1}=f_b,\quad
 {\tt F0}=F_b,\quad {\tt F1}=F_a,\quad
 {\tt Z0}=A,\quad {\tt Z1}=B.
 \tag{T.21}
$$
The names must not be inferred from their numerical order. The other relevant fields are $ {\tt w1a},{\tt w1b},{\tt a0},{\tt b0},{\tt T}$, each with its own stored radius and strip. The common-potential bound is used only after the image gate (T.3).

For example valid whole-product sup bounds on (T.3) are
$$
 M_{f_b^V}=M_{f_b}+M_V,\qquad M_{f_a^V}=M_{f_a},
$$
$$
 M_{a_1^V}=M_{a_1}+M_T M_{b_0}M_V,\qquad
 M_{b_1^V}=M_{b_1}+M_{a_0}M_V .
 \tag{T.22}
$$
Each displayed $M$ is a complete supremum on a product containing (T.3). These bounds do not claim that the actual new correction is large or small. Sharper correlated bounds may replace them only with a proof for the same whole function. Since $T$ has a simple zero and $b_0$ a double zero on the old full germ, their complete disk bounds can alternatively be restricted by their true zero orders; an arbitrary upper bound cannot be scaled that way.

Let $g=\sum_{m\ge0}g_m(\phi)\rho^m$ be any one of these complete new functions and let $M_g$ be its paid supremum on $|\rho|\le R$, $|\Im\phi|\le\Sigma$, with $R\ge R_s$. For $0<h<R$ and $0\le\omega<\Sigma$, put
$$
 {\mathsf S}_q(\Delta)=
    \sum_{l\in\mathbb Z}(4|l|)^q e^{-4|l|\Delta},
 \quad \Delta=\Sigma-\omega>0,
 \tag{T.23}
$$
where the $l=0$ term is one for $q=0$ and zero for $q>0$.
For $p\le12$ define
$$
 {\mathsf T}_{13,p}(t)=
       \sum_{m\ge13}\frac{m!}{(m-p)!}\,t^{m-p}
       =\frac{d^p}{dt^p}\frac{t^{13}}{1-t}.
$$
Then the full remainder after degree12 obeys the joint estimate
$$
 \sum_{l\in\mathbb Z}e^{4|l|\omega}(4|l|)^q
    \sup_{\substack{|\rho|\le h\\\delta,z\ {\rm in}\ (T.1)}}
       \left|\partial_\rho^p
        \left(g-\sum_{m=0}^{12}g_m\rho^m\right)_l\right|
 \le M_g R^{-p}{\mathsf T}_{13,p}(h/R)
                             {\mathsf S}_q(\Sigma-\omega).
 \tag{T.24}
$$
This follows by applying the radial and angular Cauchy integrals to each complete Fourier coefficient before the two sums. It proves a sum of uniform coefficient bounds. A bound for the supremum of an angular Wiener norm is not silently exchanged with that joint sum.

For the needed radial orders,
$$
 {\mathsf T}_{13,0}=\frac{t^{13}}{1-t},\qquad
 {\mathsf T}_{13,1}
  =t^{12}\left(\frac{13}{1-t}+\frac{t}{(1-t)^2}\right),
$$
$$
 {\mathsf T}_{13,2}
  =t^{11}\left(\frac{156}{1-t}
        +\frac{26t}{(1-t)^2}+\frac{2t^2}{(1-t)^3}\right).
 \tag{T.25}
$$
All Fourier tails and both signs of the output label are in (T.23). The mean is retained in $q=0$. There must be a strict positive angular loss, even if a radial Taylor tail is very small.

The sharper split-tail option is also valid: use the old tail with its original $R_0,\Sigma$ and the new added term with $R_s,\Sigma$, while adding their finite degree12 coefficients with signs first. For the unchanged $f_a$ use only its old tail. For $a_1^V,b_1^V$ use the complete old amplitude tail plus the tail of the corresponding product in (T.16). This can avoid shrinking an already paid old domain. It never subtracts two unrelated upper bounds.

## 7. What the new amplitudes do and do not cancel

For $w=w_0+n^{-1}w_1^V$, the genuine-column scalar identity gives the exact retained local expression
$$
 \frac{\mu}{n}\{(\mathcal L_0-V_j)w_1^V-\mathcal C_j(w_0)\}
 +\frac1{n^2}\{-\mu\mathcal C_j(w_1^V)+\mathcal R_j(w_0)\}
 +\frac1{n^3}\mathcal R_j(w_1^V).
 \tag{T.26}
$$
The definitions and matrix order of $\mathcal C_j,\mathcal R_j$ are exactly (F.4),(F.7). In particular $\mathcal C_j(w_0)=O(T)$ and $\mathcal R_j(w_0)=O(T^2)$ are genuine analytic zeros, but their complete numerical derivative norms still need to be paid.

Formula (T.26) retains the unnormalized numerator $\mu(\mathcal L_0-V_j)w_1^V$ in the physical source. It does not replace it by the normalized quantity without the factor $\mu$. All input powers $n^{-k}$ stay with the input label; they are not commuted across the complete output $J$.

The exact old-circle remainder is $\mathcal N^V(w)$ of (F.8)--(F.10), with its actual $B_j=(H_j^V)^{-1}$, every $P,I,J$ and all ordinary means. The physical even-mean equation remains a separate row. A derivative of $\mathcal B_j$ does not remove these terms.

Inside the one common smooth germ, (T.16) creates no new internal splice. At the true endpoints of the physical root piece, however, both ordinary Cauchy traces of the chosen genuine columns and their gauges must be matched to the next actual reference piece. A possible jump of the reconstructed amplitude or of $B_jw$ contributes its actual old-circle distributional/primitive source. Neither $Y,Y_T$ matching alone nor a formal Taylor order proves that source zero. The existing nonzero physical seam data are not overwritten.

## 8. Public consumer and scope

A minimal new consumer can read the exact accepted stage bytes, assemble (T.5)--(T.11) and (T.19)--(T.20), add the full Laurent polynomials in (T.16), and evaluate their complete joint norms and (T.24). It must retain separate counts for reused original coefficients and genuinely new algebra. The degree-zero signed cancellation may be checked against the proved root identity without recomputing an old accepted norm as if it were a new target.

The original stage identities, source, manifest, runtime, physical root bracket, fixed $\eta_0$, both repaired means, full degree96 explicit family, and all declared complex boxes must be checked before a new sum. Only the declared supporting auxiliary germ is used; no original neighbouring physical piece is replaced by it.

Any new numerical result requires its actual public Actions run, exact source/arguments/run identity and small final conclusion. All full Taylor arrays and intermediate certificates remain temporary under the current repository rule15. No new artifact, Release data, or reproducible numerical arrays are published.

This recipe supplies a new full forcing and a genuinely new first correction on the whole original root piece. It does not supply the full positive two-end choice, a complex reference-column norm beyond its proved domain, the old-circle remainder norm, complete low/high feedback, a final strong-return constant, or a PDE branch. Those remain separately checkable source and inverse gates.
