# R133 supplement: complete second local-vector budget from regular transport and the true rank term

2026-11-15, visible-exact / newton_source.

**Status: analytic consumption contract; the new scalar gates have not been executed.** This contract gives one complete replacement bound for the second local vector in the already successful genuine-reference volume-source certificate. It does not recompute an accepted fold, coefficient enclosure, transport solution, genuine-column norm, source row or radial integral. It does not assert a high BVP inverse or a strong-return contraction.

The primary identities are [G: ordered genuine sources](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md), [P: the regular first-vector reduction](R133-supplement-exact-first-local-vector-reduction-through-regular-transport.md), and [L: the correlated second vector and transport amplitudes](R133-supplement-correlated-second-local-vector-and-complete-transport-amplitudes.md). The complete positive-linear comparison is the one actually certified by C, run 43702688640. The complete forcing and amplitudes are those of S, run 43698106023. The current complete source ledger is D, run 43703879926, or a later strictly verified consumption of the same ledger.

## 1. Objects, domains and source units

Use the original physical root piece 2549, fixed physical eta_0, both carrier signs, both genuine reference columns and every input index |j|>=97. Write n=4|j|, N=388, and keep the full complex frequency parameter square |Re z|,|Im z|<=1/9409 with n^{-2}=z/16. All scalar parameter and frequency domains are the original ones. The final old-circle operators use real physical slices.

The matrices and functions are
$$
 K=\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 M=a_0 I+b_0K,\qquad w_0=M e_1,
$$
$$
 Z=\binom{A}{B},\qquad w_1^V=MZ,\qquad
 v_{\rm reg}=\binom{f_a}{\mathfrak b},\qquad
 \mathfrak b=\frac{f_b-B}{T}.
 \tag{L2.1}
$$
The scalar B is a normalized correction amplitude, not the physical curvature B, the old inverse matrix, or a boundary operator. The quotient in (L2.1) is the exact regular integral from P.7--P.8 and is analytic at T=0. No inverse power of a small real T is used.

Let
$$
 \mathsf C=M_T+\tfrac12 c_T M,\qquad
 x=X_\phi,\quad y=T_\phi,\quad
 \mu=Q^2(x^2+Ty^2),\quad B_+=x^2+Ty^2,
$$
$$
 \Delta_V=B_+-n^{-2}Vy^2.
 \tag{L2.2}
$$
Here Q is the actual fold scalar and V is the complete genuine-reference potential. The original scalar K of the PDE is not the matrix K in (L2.1).

The raw local vector has its original numerator unit:
$$
 L_2=-\mu E_{12}
   \{V(2\mathsf C Z+Mv_{\rm reg}-2i\epsilon MKZ_X)+V_TMZ\}
                   +R_j(w_0).
 \tag{L2.3}
$$
It has not been divided by mu. The original final source reconstruction, input-frequency weights, outer J, old-circle norms and physical dr remain outside this identity in their original order.

## 2. The component identity before any norm

Since the second row of MK is (a_0,Tb_0), the entire expression selected by E_12 is
$$
 \begin{split}
 {\cal F}_2={}&V\{2(\mathsf C_{21}A+\mathsf C_{22}B)
           +b_0f_a+a_0\mathfrak b
           -2i\epsilon(a_0A_X+Tb_0B_X)\}\\
       &+V_T(b_0A+a_0B).
 \end{split}
 \tag{L2.4}
$$
There is no derivative of T in the Z_X term. Its operation is matrix multiplication followed by an X derivative at fixed T.

The exact rank calculation in L section 4a gives
$$
 R_j(w_0)
   =-\vartheta QVG\,\frac{B_+}{\Delta_V}
                    \binom{xy}{i\epsilon y^2}.
 \tag{L2.5}
$$
Indeed H_V^{-1}e_1=\Delta_V^{-1}(-i\epsilon x,y)^t and
(i\epsilon y,x)M=GB_+(-i\epsilon y,x). Therefore
$$
 L_2=
 \binom{-\mu{\cal F}_2-\vartheta QVG B_+xy/\Delta_V}
       {-i\epsilon\vartheta QVG B_+y^2/\Delta_V}.
 \tag{L2.6}
$$
Both rows are retained. In particular the second row consists solely of the true rank term and retains its y^2 factor. This is not the result of setting an independent physical even mean source to zero.

## 3. One genuinely new smaller product

The accepted S bounds apply to the normalized forcing on
$$
 |T|\le R_T=1/2000,\quad |\operatorname{Im}X|\le\Sigma_F=1/128
$$
and to the complete amplitudes a_1^V,b_1^V on
$$
 |T|\le R_T,\quad |\operatorname{Im}X|\le\Sigma_A=3/512.
$$
Use the new smaller product
$$
 R=1/4000,\qquad \Sigma=5/1024,\qquad \sigma_p=1/256.
 \tag{L2.7}
$$
This differs from the proposed R=1/3000 product used by the first-vector consumer. Its complete scalar bounds are new quantities. Accepted numerical outputs, if available at these exact domains, are instead read unchanged.

Let the original full physical radial cover be
$$
 h_*=\frac{893368603925465506687}
             {21990232555520000000000000}.
$$
Retain the old fold product R_G=3/8000, Sigma_G=3/128, old coefficient width 1/32, and the already paid RF disk R_F=3/20000. The prospective consumer must explicitly verify
$$
 h_* A_+^{2/3}<R,\qquad
 \sigma_p+(h_*/R_G)M_\chi<\Sigma.
 \tag{L2.8}
$$
It also verifies the original inverse-image bounds, including
$$
 \frac{R}{\lambda-E_r}<R_F,\qquad
 \Sigma+B_{\rm inv}<\Sigma_G,\qquad
 \Sigma+B_{\rm inv}<1/32,\qquad \lambda=9/2,
 \tag{L2.9}
$$
with the saved positive lower bound for lambda-E_r. The relevant potential image must contain the whole R_T disk. All original mu and A gaps are kept. The whole sT segment, 0<=s<=1, lies in the same smaller product. A failed image or denominator gate produces no new source bound.

The whole physical piece, including the uncertainty band of the true root, is unchanged. A restriction of a coefficient domain does not create a new physical seam, omit a side of that band, or license the use of an unrestricted growing positive column.

## 4. Complete bounds for the leading connection and rank factor

Write t=R/[R_G(lambda-E_r)], evaluated with the saved directed lower gap. From the original complete fold data one may use
$$
 \delta_x=t j_*,\qquad x_+=1+\delta_x,\qquad
 y_{\rm quot}^+=\frac{2t(A_\phi)_+}{3A_-},\qquad
 y_+=\min\{t^2 B_T,\ R y_{\rm quot}^+\}.
 \tag{L2.10}
$$
The notation y_{\rm quot}^+ in this display means a bound for the analytic quotient y/T; it is not the T derivative of y. These are whole-domain bounds, not samples.

The old complete leading bounds are denoted by M_*=sup|a_0|, B_2=sup|b_0/T^2|, G_+=sup|G| and B_i for the original inverse leading branch. Put
$$
 d_T=R_T-R,\quad d_A=\Sigma_A-\Sigma,\quad
 b_+=B_2R^2,\quad b_X^+=B_2R^2/d_A .
$$
A complete a_X bound is M_*/d_A. When the original exact normalization a_0(0,X)=1 and M_*>=1 are both retained, the independent Caratheodory bound
$$
 a_X^+\le
 \min\left\{\frac{M_*}{d_A},
       \frac{2(M_*-1)R}{d_Td_A}\right\}
 \tag{L2.11}
$$
is also available. This is not a subtraction of unrelated upper bounds.

P.17--P.18 give the exact regular connection, with Xi=c_X/T:
$$
 \mathsf C=-i\epsilon KM_X-\frac{i\epsilon}{2}\Xi KM
                 +\frac12\frac{b_0}{T}K\operatorname{diag}(-1,1).
$$
Only its second row is needed here:
$$
 c_{21}^+=a_X^++\tfrac12\Xi_+M_*+\tfrac12B_2R,
 \qquad
 c_{22}^+=Rb_X^++\tfrac12\Xi_+R b_+ .
 \tag{L2.12}
$$
Xi_+ is obtained on this whole product from the exact P.18 formula, including DQ, Q d_phi, T_0Q and the regular y/T term. The full radial, angular and mean coefficients are retained.

For completeness, if Q_phi^+=Q_+y_{\rm quot}^+/2,
Q_r^+=Q_+/(R_G-R/(lambda-E_r)), and
$$
 H_Q=Q_r^++d_+Q_\phi^++Q_+(d_\phi)_++(T_0)_+Q_+,
$$
then valid sufficient bounds are
$$
 \Xi_+=\frac{H_Qy_++Q_+^2x_+y_{\rm quot}^+/2}{\mu_-},
 \qquad
 \mu_+=Q_+^2(x_+^2+Ry_+^2).
 \tag{L2.13}
$$
The scalar inverse and drift derivative must be read from the same original coefficient product.

The frequency square implies |n^{-2}|=|z|/16<=sqrt(2)/388^2<2/388^2. Therefore the following new directed gate suffices for the full rank denominator:
$$
 d_\Delta=(1-\delta_x)^2-
             (R+2V_+/388^2)y_+^2>0,\qquad \delta_x<1.
 \tag{L2.14}
$$
In particular, it is not a real-frequency lower bound improperly reused on a complex square. Set
$$
 r_+=\vartheta_+Q_+V_+G_+
                 \frac{x_+^2+Ry_+^2}{d_\Delta}.
 \tag{L2.15}
$$
The two complete rank row bounds are r_+ x_+ y_+ and r_+ y_+^2. Using (L2.14) is a new scalar comparison; it does not recompute the previously accepted inverse-matrix enclosure.

## 5. The normalized correction and the complete two-row bound

Let a_1^+,b_1^+,F_a,F_b be the accepted complete S bounds, in their original units. On the larger amplitude product define
$$
 A_* =B_i^2(M_*a_1^++R_T^3B_2b_1^+),\qquad
 B_* =B_i^2(R_T^2B_2a_1^++M_*b_1^+).
 \tag{L2.16}
$$
These are obtained by the exact inverse of M. Both mean amplitudes are present. Put
$$
 A_X^+=A_*/d_A,\qquad B_X^+=B_*/d_A,\qquad
 \mathfrak b^+=\frac23(F_b/d_T+A_X^+).
 \tag{L2.17}
$$
The last formula is the exact regular-integral mass 2/3. It does not evaluate (f_b-B)/T near the root.

Equations (L2.4)--(L2.6) give the following complete raw suprema:
$$
 \begin{split}
 \ell_a={}&\mu_+\Big[
 V_+\{2(c_{21}^+A_*+c_{22}^+B_*)
       +b_+F_a+M_*\mathfrak b^+
       +2(M_*A_X^++Rb_+B_X^+)\}\\
 &\hspace{34mm}+(V_T)_+(b_+A_*+M_*B_*)\Big]
                         +r_+x_+y_+,\\
 \ell_b={}&r_+y_+^2.
 \end{split}
 \tag{L2.18}
$$
Each is nonnegative. No component is inferred by subtracting an independently bounded first component from a total bound. No derivative of a carrier or reference column is included in ell_a or ell_b.

## 6. Reuse of the actual all-output comparison

The true physical piece maps the whole old angular strip sigma_p into (L2.7), by the mandatory image gates. Cauchy therefore supplies the six old-angle amplitude bounds
$$
 b_{\rm new}=(\ell_a,\ell_a/\sigma_p,2\ell_a/\sigma_p^2,
             \ell_b,\ell_b/\sigma_p,2\ell_b/\sigma_p^2).
 \tag{L2.19}
$$
These are the same amplitude triples used by the already accepted genuine-column operator. The common |rho|^{-1/4} profile and the actual both-column normalization are unchanged. Neither profile is computed again.

For each of C's three complete branches, read its six certified nonnegative coefficients k_{bi}. They already bound the positive linear norm algorithm on every nonnegative six-jet input. A new complete all-output operator bound is
$$
                 K_2^{\rm new}=\sum_{b=1}^3\sum_{i=1}^6
                                       k_{bi}(b_{\rm new})_i.
 \tag{L2.20}
$$
This is an independent bound for the full second raw vector. It is not a recomputation of C's eighteen calibration coefficients.

Let B_2^{old}>0 be the exact positive upper-bound number used by C for its second raw local operator, and let beta_2 be a directed positive lower endpoint for that number. Define
$$
             q_2=\min\{1,K_2^{new}/\beta_2\}.
 \tag{L2.21}
$$
The denominator is not a lower bound for the true source or its operator norm. The original second source-term budget is a positive multiple of that algorithmic bound number on every original row. Consequently its already integrated L2 norm may be multiplied by q_2. This uses the full original row cover, the same outer J window, the original independent means and the actual dr. There is no new radial integration.

In C's displayed raw-local expansion the additional input weights are exactly 1,1/n,1/n^2 for L_1,L_2,L_3. They are already paid in the old integrated terms and must not be applied again when (L2.21) multiplies the saved local_raw_2 term.

## 7. Complete-ledger and execution conditions

The consumer must verify exact source, manifest, runtime and outcome identities for the original S, C and D receipts; the full original fold stage; the potential bound; and all original input paths. If a later first-vector improvement is used, its original complete source ledger and every unchanged term must match D exactly before replacing local_raw_2.

Only that one complete term is changed. The other twenty first-row terms and all ten independent-mean terms remain byte-identical. The new local sum, complete first-row bound and full two-row bound are compared only as complete bounds with the corresponding old bounds. The complete old mean and all source/jump/positive-boundary obligations remain.

The original root cover, physical sources and two J windows have not been enlarged. The old finite scalar potential, forced transport and genuine-column operators are not regenerated. All new products and arrays stay temporary in the one public Actions runner; the repository receives only scripts, input identities, run and output hashes, actual gates and a small conclusion. A mathematical failure is reported with its actual gate and does not alter an old successful certificate.

Even a successful improvement remains a known trial-volume source certificate. It supplies neither the unknown positive growing coefficient, a full physical high inverse, the physical seam charges, a cutoff-97 strong-return contraction nor the final parameter response.
