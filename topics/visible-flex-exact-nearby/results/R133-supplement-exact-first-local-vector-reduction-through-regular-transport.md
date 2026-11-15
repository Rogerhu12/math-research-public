# R133 supplement: exact reduction of the first local genuine-source vector through regular transport

2026-11-15, visible-exact / phase_inverse.

**Proved exact identities and a conditional complete scalar-budget recipe.** The first retained local vector can be evaluated without separately bounding the second radial derivative of the first correction. The reduction uses the same leading amplitude, the exact normalized forced transport and the same genuine common potential. It neither changes the trial nor discards an inverse, primitive, mean or interface term. New numerical bounds and any improvement remain to be evaluated in public Actions.

Use [the signed genuine forcing](R133-supplement-signed-first-forcing-and-root-cancellation-for-genuine-common-reference.md), [the ordered complete source identity](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md), and the accepted scalar result of run 43698106023/1. The current complete ordinary-source bounds are those of [the directed-word result](R133-supplement-actual-directed-word-genuine-negative-source-bounds.md).

## 1. One common branch, the original leading matrix and the regular solution

Fix the original intrinsic parameter eta_0, the full original complex delta square, the same input label j and carrier sign epsilon, and the corresponding potential V=V_j(T). Set n=4|j|, |j|>=97. All identities are initially on the same smooth reference branch as G.1--G.14. Put
$$
 E=E_{12},\qquad K=\begin{pmatrix}0&T\\1&0\end{pmatrix},
 \qquad \mathcal J=\operatorname{diag}(-1,1).
 \tag{P.1}
$$
Here K is a matrix; the scalar intrinsic curvature is written K_sc below.

Keep the original leading amplitudes and matrix
$$
 w_0=(a_0,b_0)^t,\qquad
 M=[w_0,Kw_0]=a_0\,1+b_0K,\qquad
 w_1^V=MZ,\quad Z=(A,B)^t .
 \tag{P.2}
$$
The normalized forcing is f=(f_b^V,f_a)^t; write its first component simply as f_b in this paper. Exactly,
$$
 2A_T+2i\epsilon T B_X=f_a,\qquad
 2TB_T+B+2i\epsilon T A_X=f_b .
 \tag{P.3}
$$
This is the original regular first correction, with
$$
 A(0,X)=0,\qquad B(0,X)=f_b(0,X).
 \tag{P.4}
$$
The nonzero second root value is retained. The leading matrix M is unchanged by replacing free columns with genuine columns.

The correct canonical principal operator is
$$
 \mathscr P=\partial_T^2+T\partial_X^2 .
 \tag{P.5}
$$
In particular the sign is the same as the actual carrier and the equation
Y_TT=(n^2T-V)Y.

## 2. Two second-derivative cancellations and a regular integral

Define the analytic quotient
$$
 \mathfrak b(T,X)=\frac{f_b(T,X)-B(T,X)}{T}.
 \tag{P.6}
$$
It is removable at T=0 by (P.4). More usefully, it has an integral containing no division by T:
$$
 \boxed{\quad
 \mathfrak b(T,X)=
 \int_0^1s^{1/2}
       [\,f_{b,T}(sT,X)+i\epsilon A_X(sT,X)\,]\,ds .
 \quad}
 \tag{P.7}
$$
To prove this, apply the regular Euler inverse to the second equation in (P.3):
$$
 B(T,X)=\frac12\int_0^1s^{-1/2}f_b(sT,X)\,ds
       -i\epsilon T\int_0^1s^{1/2}A_X(sT,X)\,ds .
$$
The difference between f_b(T,X) and its first integral is
T times the first integral in (P.7), by the fundamental theorem of calculus and interchanging the two finite integrals.

Differentiate only the exact functions. Substitution of the first transport equation gives
$$
 \begin{split}
 \mathfrak b_T={}&
 \int_0^1s^{3/2}f_{b,TT}(sT,X)\,ds\\
 &+\frac{i\epsilon}{2}\int_0^1s^{3/2}f_{a,X}(sT,X)\,ds
       +T\int_0^1s^{5/2}B_{XX}(sT,X)\,ds .
 \end{split}
 \tag{P.8}
$$
Direct differentiation of (P.3) now yields
$$
 \boxed{\quad
 \mathscr P A=\frac{f_{a,T}-i\epsilon f_{b,X}
                             -i\epsilon B_X}{2},
 \qquad
 \mathscr P B=\frac{\mathfrak b_T-i\epsilon f_{a,X}}2 .
 \quad}
 \tag{P.9}
$$
For example the mixed derivative from A_TT cancels T A_XX after using the X derivative of the second transport equation. These identities are exact through the removable root.

Every segment (sT,X), 0<=s<=1, must stay in the same paid canonical product. A centered T disk and a fixed X strip provide this automatically. This observation does not enlarge the original canonical disk, angular strip, physical piece or parameter square.

## 3. The leading intertwiner, with its exact matrix order

Let
$$
 \begin{split}
 c_T&=\mu^{-1}(D^2T+\eta^2K_{\rm sc}T_{\phi\phi}-T_0DT),\\
 c_X&=\mu^{-1}(D^2X+\eta^2K_{\rm sc}X_{\phi\phi}-T_0DX).
 \end{split}
 \tag{P.10}
$$
Thus the differential part in canonical variables is
mu times (mathscr P+c_T partial_T+c_X partial_X), plus its zero-order terms. No derivative of mu is introduced by this rewriting.

The leading transport is
$$
 \mathscr T(w)=2Kw_T+2i\epsilon T w_X+c_TKw
                         +i\epsilon c_Xw+Ew .
$$
It obeys mathscr T(w_0)=0. Since K_T=E and KE+EK=1,
mathscr T(Kw_0)=w_0. Consequently
$$
 2KM_T+2i\epsilon T M_X+c_TKM+i\epsilon c_XM+EM=ME .
 \tag{P.11}
$$
This is a consequence of the original leading solution, not an additional hypothesis about the new potential.

Set
$$
 \mathsf C=M_T+\frac{c_T}{2}M .
$$
The commutators needed below are
$$
 [M,E]=b_0\mathcal J,\qquad [K,M_T]=[M,E].
$$
Using (P.11), in the stated order,
$$
 2T M_X+c_XM-2i\epsilon\mathsf C K
                  =i\epsilon b_0\mathcal J .
 \tag{P.12}
$$
The sign on the right is positive. Although M commutes with K, its T derivative need not commute with K.

## 4. A complete identity for the first local vector

Keep G.6's exact raw operator
$$
 \mathfrak A(w)=
 (D^2+\eta^2K_{\rm sc}\partial_\phi^2-T_0D+V_0-\mu V)w
                       +i\epsilon\vartheta QKw ,
 \tag{P.13}
$$
and G.4's correction
$$
 \mathfrak C_V(w)=
 \mu E\{2Vw_T+(V_T+c_TV)w\}.
$$
Thus the original first local vector is L_1=mathfrak A(w_1^V)-mathfrak C_V(w_0). Its raw numerator is not divided by mu in the physical source.

The normalized forcing gives
$$
 \mathfrak A(w_0)=-\mu Mf,\qquad
 \mathfrak A(Kw_0)=K\mathfrak A(w_0)
                      +\mu E(2w_{0,T}+c_Tw_0).
 \tag{P.14}
$$
The second equality uses the product rule and K_T=E. The zero-order term
i epsilon vartheta QK commutes with K, so its complete contribution has not been dropped.

Combining (P.3), (P.11)--(P.14) proves
$$
 \boxed{
 \begin{split}
 L_1=\mu\big\{&
 M[\,\mathscr P Z-(A\,1+BK)f\,]\\
 &+\mathsf C\binom{f_a}{\mathfrak b}
       +i\epsilon b_0\mathcal J Z_X\\
 &+E[(B-V)(2w_{0,T}+c_Tw_0)-V_Tw_0]\big\}.
 \end{split}}
 \tag{P.15}
$$
To check the cross derivatives, write
Z_T=(f_a,mathfrak b)^t/2-i epsilon KZ_X.
Then
$$
 (2M_T+c_TM)Z_T+(2T M_X+c_XM)Z_X
 =\mathsf C(f_a,\mathfrak b)^t+i\epsilon b_0\mathcal J Z_X
$$
by (P.12). The zero-order product is
-mu M(A1+BK)f, while (P.14) and -mathfrak C_V(w_0) give the last line of (P.15).

The last E is on the left. Its sole nonzero component is
$$
 [(B-V)(2b_{0,T}+c_Tb_0)-V_Tb_0]e_1 .
 \tag{P.16}
$$
In particular it uses b_0 and b_0,T, with their exact second-order leading root zero. It does not require an unrelated bound for the first component a_0,T in this term.

Formula (P.15) replaces neither w_1^V nor the complete source operator. It combines terms of that same L_1 before taking a modulus. Its ingredients contain only the first T derivative of the leading matrix, first and second T derivatives of the known forcing, and angular derivatives of the normalized first correction. It contains no separately estimated w_1,TT or old w_1,rr.

## 5. Optional exact cancellation in the leading connection

A still more correlated expression for mathsf C follows from (P.11):
$$
 \boxed{\quad
 \mathsf C=-i\epsilon K M_X
       -\frac{i\epsilon}{2}\Xi K M
       +\frac12\frac{b_0}{T}K\mathcal J,\qquad
 \Xi=\frac{c_X}{T}.
 \quad}
 \tag{P.17}
$$
Both quotients in (P.17) are analytic root quotients, not numerical divisions by small T. Indeed b_0=T^2 times an analytic function.

There is also an exact no-small-denominator formula for Xi. Write
x=X_phi, y=T_phi and C=d_phi, with the same branch
Q=a_infinity A_fold^(-1/3). Then
$$
 Q_\phi=-\frac{Q}{2}\frac yT,\qquad
 \frac yT=\frac23\frac{(A_{\rm fold})_\phi}{A_{\rm fold}} .
$$
Using DX=-QTy, DT=Qx, and [D,partial_phi]=C partial_phi in (P.10), one obtains
$$
 \boxed{\quad
 \Xi=-\mu^{-1}\left[
       (DQ+QC-T_0Q)y+\frac{Q^2x}{2}\frac yT
                      \right].
 \quad}
 \tag{P.18}
$$
Here the quotient y/T is evaluated by the second displayed formula, or by its analytic root factor. The original anchor A_fold(0,phi)=a_infinity(0) is independent of phi, so (A_fold)_phi=O(rho). The original nonzero T/rho gap gives y/T=O(T) and y=O(T^2); (P.18) therefore gives Xi=O(T). Equivalently the first leading-transport row, a_0(0,X)=1 and b_0=T^2 b_2 give c_X=O(T^2). Thus mathsf C vanishes at the root. All full old-angle means remain in Q, T_0 and the leading amplitude.

This option cancels the large common radial leading connection before taking a norm. It must not be simulated by subtracting an upper bound for M_T from an upper bound for c_TM/2. Either the exact formula (P.17) or a complete direct bound for their sum is required.

## 6. Concrete complete supremum bounds on an unchanged product

The successful scalar run supplies the normalized forcing on
$$
 |T|\le R_T=1/2000,\qquad |\operatorname{Im}X|\le\Sigma_F=1/128,
$$
and the actual amplitudes a_1^V,b_1^V on
$$
 |T|\le R_T,\qquad |\operatorname{Im}X|\le\Sigma_A=3/512 .
 \tag{P.19}
$$
These domains follow from its actual inverse-image and path gates. The raw forcing F and normalized forcing f are different; this section uses its saved normalized f_b,f_a bounds.

Choose a smaller product |T|<=R<R_T, |Im X|<=Sigma<Sigma_A. A prospective consumer may use R=1/3000 and Sigma=5/1024, but must check the complete image of the unchanged physical root piece at the chosen old angular strip. For example, with h_* the original full physical cover and sigma_p=1/256, it must verify
$$
 h_* A_+^{2/3}<R,\qquad
 \sigma_p+(h_*/R_G)M_\chi<\Sigma .
 \tag{P.20}
$$
The original first-order zero of X-phi justifies the second factor. The old inverse-image gate for the larger product and every mu, leading-matrix and fold gap are retained. A failed new scalar image gate asserts no new bound.

Write d_T=R_T-R, d_F=Sigma_F-Sigma, d_A=Sigma_A-Sigma. Let F_b,F_a be the complete normalized forcing suprema on (P.19)'s larger forcing domain, and let A_*,B_* bound the normalized functions A,B on the larger amplitude domain. The latter may be obtained by applying the accepted full leading inverse matrix to the accepted a_1^V,b_1^V suprema, in their original order. This is a new scalar norm combination, not a new solution of the old forced transport.

For example the original inverse-leading-branch bound B_i, whole |a_0| bound M_*, and complete |b_0/T^2| bound B_2 give
$$
 \begin{pmatrix}A_*\\B_*\end{pmatrix}
 \preceq B_i^2
 \begin{pmatrix}M_*&R_T^3B_2\\R_T^2B_2&M_*\end{pmatrix}
 \begin{pmatrix}\sup|a_1^V|\\\sup|b_1^V|\end{pmatrix}.
 \tag{P.21}
$$
All quantities here are complete domain bounds, including full means.

Cauchy and the exact integral masses give the following finite recipe:
$$
 \begin{gathered}
 A_X^+=A_*/d_A,\qquad B_X^+=B_*/d_A,\qquad
 B_{XX}^+=2B_*/d_A^2,\\
 \mathfrak b^+=\frac23(F_b/d_T+A_X^+),\\
 P_A^+=\frac12(F_a/d_T+F_b/d_F+B_X^+),\\
 P_B^+=\frac{2F_b}{5d_T^2}
                  +\frac{3F_a}{5d_F}+\frac{R}{7}B_{XX}^+ .
 \end{gathered}
 \tag{P.22}
$$
For P_B, the three masses in (P.8) are 2/5, 2/5 and 2/7. Together with (P.9) these give exactly the factors in (P.22).

Let bold M, bold C be entrywise nonnegative bounds for M, mathsf C on the smaller product, and let b_+,b_T^+,c_T^+,V_+,V_T^+,mu_+ be complete bounds there. A sufficient complete raw-vector bound is
$$
 \begin{split}
 \binom{L_{1,a}^+}{L_{1,b}^+}
 =\mu_+\bigg\{&
 \boldsymbol M\left[
 \binom{P_A^+}{P_B^+}
 +\binom{A_*F_b+RB_*F_a}{A_*F_a+B_*F_b}\right]\\
 &+\boldsymbol C\binom{F_a}{\mathfrak b^+}
 +b_+\binom{A_X^+}{B_X^+}\\
 &+\binom{(B_*+V_+)(2b_T^++c_T^+b_+)+V_T^+b_+}{0}
 \bigg\}.
 \end{split}
 \tag{P.23}
$$
No term in this expression is a difference of upper bounds. The optional connection formula uses
$$
 \boldsymbol C\preceq
 |K|\boldsymbol M_X+\tfrac12\Xi_+|K|\boldsymbol M
                      +\tfrac12(B_2R)|K|,
 \qquad |K|=\begin{pmatrix}0&R\\1&0\end{pmatrix}.
 \tag{P.24}
$$
Here b_+<=B_2R^2 and
b_T^+<=B_2[2R+R^2/d_T].
For M_X, |(b_0)_X|<=B_2R^2/d_A.
The diagonal |(a_0)_X| may be bounded by M_*/d_A. Since a_0(0,X)=1 for each fixed complex parameter and X, Caratheodory also gives the complete alternative
2(M_*-1)R/(d_Td_A), when M_*>=1. Its use retains the exact root normalization and the whole larger domain; it is not subtraction of unrelated upper bounds.

The c_T, Xi and mu bounds must use the same full product. Formula (P.18), the exact root factor for y/T, and the original accepted whole coefficient/fold bounds provide a concrete finite route. New smaller-domain scalar combinations are allowed. Identical accepted output fields, if present, are read; accepted fold coefficients, target data, forcing solves and prior norm tables are not regenerated.

## 7. Complete all-output conversion and reuse of the actual radial integral

Once (P.20)--(P.24) are actually proved on the old product, its real old-angle derivatives satisfy
$$
 \sup|\partial_\phi^q L_{1,i}|
       \le q!\,L_{1,i}^+/\sigma_p^q,\qquad q=0,1,2 .
 \tag{P.25}
$$
Only the amplitude is continued in the complex old angle. This does not use an unproved complex genuine-column operator norm.

These six real angular budgets can be inserted into the already accepted 18 positive-linear comparison coefficients for the identical fold, genuine-column profiles, label partition and negative physical cover. Their output C_new is the coefficient of the same common column envelope. At each real negative-side circle away from the root,
$$
 \|\mathsf S^V(L_1):H^{-4/3}_{|j|\ge97}\longrightarrow H^{-5/3}\|
       \le |\rho|^{-1/4} C_{\rm new}.
 \tag{P.26}
$$
Both signs, both genuine columns and the output mean are included. C_new alone is not asserted to be a radius-independent pointwise operator norm. The original fixed column operator and profiles are not reevaluated.

The old successful complete L_1 norm was itself a positive algorithmic budget. Its strict positive lower endpoint can therefore be used exactly as in D.6--D.9 of the two-window reuse theorem: if C_new is the new complete coefficient, beta_old is that lower endpoint, and q=min(1,C_new/beta_old), then the accepted local_raw_1 radial L2 bound may be multiplied by q. The original outer J, exact physical dr and uncertain-root charge remain. More explicitly, each of the same six original row intersections retains its complete c_J,1(row) and the squared common envelope |rho|^(-1/2) dr; the original one-sided uncertain-root bound is unchanged. The new ratio only multiplies the shared complete coefficient of this identical measure and never reapplies or cancels the radial envelope. This compares the same entire local vector and never subtracts the old w_1,rr contribution from an upper bound.

The current two other local vectors, all directed-word and old-mean source terms, the independent physical even-mean terms and their complete actual radial integrals are read unchanged. A new pair bound is formed only from complete valid component bounds, retaining an old complete bound whenever it is better.

## 8. Scope and publication

The same original physical piece, fixed intrinsic parameter, complex parameter squares, root normalization, both genuine reference columns and all input labels are required. The proof keeps V_j(T) on the actual common T chart. It neither replaces that potential by a same-r value nor moves an input n power through a convolution.

Reference and physical seams remain governed by G.22--G.23 and their actual two-sided traces. Identities (P.7)--(P.25) are not a proof that any matching jump vanishes. The independent even mean and positive affine graph retain their own source and port equations.

A new public consumer must pin the accepted scalar, column, leading, positive-linear and source conclusions, report every actual image/gap gate and its final complete local and two-row source bounds, and distinguish new scalar arithmetic from old data reads. Only the small final conclusions, source/parameter identities, run, hashes and actual status are persisted. Intermediate matrices and row diagnostics stay temporary.

This theorem does not by itself supply a numerical improvement, a physical-to-wave trace, a complete negative BVP inverse, the positive growing-column graph, low/high feedback or a cutoff-97 strong-return contraction.
