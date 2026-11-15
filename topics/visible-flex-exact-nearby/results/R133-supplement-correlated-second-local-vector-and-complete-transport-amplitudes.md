# R133 supplement: correlated second local vector and exact transport amplitudes for the genuine reference

2026-11-15, visible-exact / phase_inverse.

**Proved exact identities; numerical comparisons remain conditional.** This is a continuation of [the regular-transport first local vector](R133-supplement-exact-first-local-vector-reduction-through-regular-transport.md). It keeps the same original leading matrix, the same genuine first correction and the complete two source rows. The identities require no new target, fold, ordinary differential equation solution or change of trial.

Use G.1--G.23 of [the complete ordered source theorem](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md). Every identity is first interpreted on a common smooth reference branch. Physical and reference matching contributions are retained separately.

## 1. Fixed order and notation

For the same input label j, n=4|j| and epsilon=sgn(j), set
$$
 K=\begin{pmatrix}0&T\\1&0\end{pmatrix},\quad E=E_{12},
 \quad J_*=\operatorname{diag}(-1,1),\quad
 M=[w_0,Kw_0]=a_0 I+b_0K,\quad w_1^V=MZ,\quad Z=(A,B)^t.
 \tag{L.1}
$$
The scalar intrinsic curvature is denoted K_sc. Put
$$
 D=\partial_r-d\partial_\phi,\quad x=X_\phi,\quad y=T_\phi,\quad
 DT=Qx,\quad DX=-QTy,\quad \mu=Q^2(x^2+Ty^2).
$$
The normalized forcing is f=(f_b^V,f_a)^t; write f_b=f_b^V. Retain the analytic root quotient and connection from P.6--P.18:
$$
 \mathfrak b=(f_b-B)/T,\qquad v=\binom{f_a}{\mathfrak b},
 \qquad \mathsf C=M_T+\frac{c_T}{2}M,\qquad \Xi=c_X/T.
 \tag{L.2}
$$
These quotients are evaluated by the regular formulas of P.7 and P.18. They are not numerical divisions by a small T.

The normalized first correction obeys exactly
$$
 Z_T=\frac12v-i\epsilon KZ_X .
 \tag{L.3}
$$
The full independent mean has not been projected from Z, v, M or any product below.

## 2. The complete second local vector

Direct differentiation of w_1^V=MZ and (L.3) gives
$$
 \boxed{\quad
 2(w_1^V)_T+c_Tw_1^V
   =2\mathsf C Z+Mv-2i\epsilon MKZ_X .
 \quad}
 \tag{L.4}
$$
In particular the large common radial derivative in M_T and the paired c_TM/2 have already been combined.

G.7 defines the same retained second local vector as
$$
 L_{2,j}=-\mu E\{2V_j(w_1^V)_T+(V_{j,T}+c_TV_j)w_1^V\}
                         +\mathfrak R_j(w_0).
$$
Consequently,
$$
 \boxed{\quad
 L_{2,j}=
 -\mu E\{V_j(2\mathsf C Z+Mv-2i\epsilon MKZ_X)
                            +V_{j,T}MZ\}
              +\mathfrak R_j(w_0).
 \quad}
 \tag{L.5}
$$
All V_j and V_j,T are evaluated at the actual common T. E remains on the left. Its bracket reads only the second component. With C_ab the entries of mathsf C, this component is exactly
$$
 \begin{split}
 &V_j\{2C_{21}A+2C_{22}B+b_0f_a+a_0\mathfrak b
                 -2i\epsilon(a_0 A_X+Tb_0 B_X)\}\\
 &\hspace{4em}+V_{j,T}(b_0A+a_0B).
 \end{split}
 \tag{L.6}
$$
There is no a_1,T or b_1,T left in (L.6). No zero-order, inverse or mean term was removed: the complete original mathfrak R_j(w_0) remains in (L.5).

For example, suppose all indicated upper bounds have been proved on a common product which contains the actual old-circle image. Then the first bracket in (L.5) has the complete scalar upper bound
$$
 \begin{split}
 V_+\{&
 2C_{21}^+A_++2C_{22}^+B_+
 +b_+F_a+M_*\mathfrak b^+
 +2M_*A_X^++2R b_+B_X^+\}\\
 &+V_T^+(b_+A_++M_*B_+).
 \end{split}
 \tag{L.7}
$$
Here A_+,B_+ refer to the normalized correction, while M_* bounds a_0 and b_+ bounds b_0. This is a bound for a complete exact sum and not a subtraction of upper bounds.

The ordinary source uses this vector with the original input multiplier n^-1, after the first-local-vector density has been factored. It is not an output Fourier multiplier. Its actual old-circle conversion, radial envelope, outer J and original physical radial integration must still be retained.

## 3. Exact compressed g for both densities

To avoid confusion with the potential V_j and normalized correction B, write
$$
 \mathcal B_j=(H_j^V)^{-1},\qquad
 \mathcal Q_j=QV_j\,\mathcal B_j e_1(i\epsilon y,\ x).
 \tag{L.8}
$$
Thus mathfrak R_j= vartheta mathcal Q_j in G.6. The row on the right acts first. G.5 gives the exact matrix identity
$$
 \mathcal B_j H_{D,j}^V=-i\epsilon QK-n^{-2}\mathcal Q_j .
 \tag{L.9}
$$
Since eta is radial, G.10's g is exactly
$$
 \begin{split}
 g_j(w)&=Dw-\partial_\phi(\mathcal B_jH_{D,j}^Vw)\\
       &=\mathcal G_0(w)+n^{-2}\partial_\phi(\mathcal Q_jw),
 \qquad
 \mathcal G_0(w)=Dw+i\epsilon\partial_\phi(QKw).
 \end{split}
 \tag{L.10}
$$
The phi derivative differentiates the whole ordered product in the last term. The factor n^-2 remains attached to the same input label.

Put U_*=xI+i epsilon yK. The identities DT=Qx and DX=-QTy yield
$$
 \begin{split}
 \mathcal G_0(MZ)
  &=\mathcal G_0(M)Z+\frac Q2 U_*Mv,\\
 \mathcal G_0(Kw_0)
  &=K\mathcal G_0(w_0)+QE\,U_*w_0.
 \end{split}
 \tag{L.11}
$$
The first equality uses (L.3), K^2=TI and the fact that M commutes with K. The coefficient of Z_X is
Q[-i epsilon U_*K-TyI+i epsilon xK]=0.
The second follows from
I-KE=EK and the full derivative of QK. In particular it retains Q_phi and K_phi.

Equivalently, the complete genuine first-correction amplitude is
$$
 \boxed{
 \begin{split}
 g_j(w_1^V)={}&
 (AI+BK)\mathcal G_0(w_0)+BQ E U_*w_0
                  +\frac Q2 U_*Mv\\
 &+n^{-2}\partial_\phi(\mathcal Q_jMZ).
 \end{split}}
 \tag{L.12}
$$
This expression has no independent old-radial derivative of w_1^V.

One may also eliminate M_T and M_X from mathcal G_0(M), using P.17:
$$
 \boxed{
 \begin{split}
 \mathcal G_0(M)={}&
 -\frac Q2U_*(c_TI+i\epsilon\Xi K)M
 +\frac Q2\frac{b_0}{T}U_*KJ_*\\
 &+i\epsilon(Q_\phi K+QyE)M.
 \end{split}}
 \tag{L.13}
$$
The last line is essential. The formula is analytic at the root because b_0/T and Xi have their already specified removable extensions. It retains the same radial mean contribution through c_T and M; it does not assert that mathcal G_0(M) vanishes.

## 4. The full q, h and y amplitudes

Write v_bg for the original background v, so that it is distinct from the vector v in (L.2). Because v_bg is a scalar multiplier, the original amplitudes obey
$$
 \begin{split}
 h_j(w)&=\eta^{-1}(-i\epsilon QK-n^{-2}\mathcal Q_j)w,\\
 y_j(w)&=v_{\rm bg}(-i\epsilon QK-n^{-2}\mathcal Q_j)w.
 \end{split}
 \tag{L.14}
$$
The third amplitude has the exact compression
$$
 \boxed{\quad
 q_j(w)=v_{\rm bg}g_j(w)
           +i\epsilon(v_{\rm bg})_\phi QKw
           +n^{-2}(v_{\rm bg})_\phi\mathcal Q_jw .
 \quad}
 \tag{L.15}
$$
Indeed q=v_bg Dw-partial_phi(v_bg mathcal B H_D^Vw), so q=v_bg g-(v_bg)_phi mathcal B H_D^Vw. Substitution of (L.9) gives (L.15).

No derivative of the physical Fourier primitive I or inverse J was interchanged in this derivation. The full old-angle means of g,h,y,q remain in G.19 and G.20. In particular the transported mean is still Pi U^V(g), and the five independent physical even-mean terms remain distinct from an amplitude mean.

## 4a. The exact rank row before taking an amplitude norm

Write $B_+=x^2+Ty^2$ and $\Delta_{V,j}=B_+-n^{-2}V_jy^2$.
On the same paid old-circle inverse domain,
$$
 H_j^V=
 \begin{pmatrix}i\epsilon x&y(T-n^{-2}V_j)\\y&i\epsilon x\end{pmatrix},
 \qquad
 \mathcal B_je_1=\Delta_{V,j}^{-1}\binom{-i\epsilon x}{y}.
 \tag{L.16}
$$
The determinant is $-\Delta_{V,j}$. The original exact leading formulas
$a_0=G(x^2-Ty^2)$ and $b_0=-2i\epsilon Gxy$ give
$$
 (i\epsilon y,x)M=G B_+(-i\epsilon y,x).
 \tag{L.17}
$$
Consequently the entire retained rank is
$$
 \boxed{\quad
 \mathfrak R_j(MZ)=
 \frac{\vartheta QV_jG B_+}{\Delta_{V,j}}
       \binom{-i\epsilon x}{y}(-i\epsilon y A+xB).
 \quad}
 \tag{L.18}
$$
In particular
$\mathfrak R_j(w_0)=
 (\vartheta QV_jG B_+/\Delta_{V,j})(-xy,-i\epsilon y^2)^t$.
This keeps the original second-order root zero of $y=T_\phi$ in the first
component. A later norm may use this exact product without first bounding
the whole leading vector. The complete input-label dependence, output mean
and all angular derivatives of the factors remain. No new determinant gap
or enlarged domain is asserted by (L.16)--(L.18).

## 5. Domains, complete comparisons, and limits of this result

The regular integrals used for mathfrak b require their entire sT segments to lie in the paid canonical product. The leading matrix and normalized correction in (L.4)--(L.7) are evaluated on that same product.

The factor mathcal B_j in (L.8)--(L.15) additionally requires its actual old-circle inverse domain and gap. A canonical subproduct used for (L.4) is not automatically contained in that inverse domain. A complete norm implementation may instead restrict all factors to a common old-radial/old-angle product whose two inclusions have actually been checked, and then take full old-angle derivatives there. Both input signs, both genuine columns, all labels |j|>=97 and the output mean are retained.

On the negative real side, the accepted positive-linear column comparisons retain their common |rho|^-1/4 envelope. Squared-source integration retains the same actual |rho|^-1/2 dr weight and the actual one-sided uncertain-root charge. A smaller complete source coefficient may replace an old one only through a proved same-budget comparison; no old upper bound is subtracted to isolate an allegedly smaller term.

The two inverse/source windows of G.17--G.20 remain different. A complete operator word or one-gain bound from one window is not silently transferred to the other. If a new g or q bound is inserted, every associated nonlocal word, old mean and independent physical mean must use a complete valid norm in its own declared window. All other original source terms remain.

At genuine physical or reference seams, G.22--G.23 apply with actual one-sided traces, including possible distributional primitive contributions. These identities neither reset the first-correction constants nor assert that a matching jump is zero.

This paper proves no numerical improvement by itself. It does not complete the full negative BVP inverse, positive two-ended graph, ordinary-source-to-wave trace, low/high feedback, or cutoff-97 strong-return contraction. Any new numerical comparison is a separate public Actions computation; earlier successful scientific outputs remain read only.
