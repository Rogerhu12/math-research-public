# R133 supplement: two ordinary source kernels and both outputs for the genuine radial reference

2026-11-15.

This is an analytic consequence of the already proved genuine two-column radial reference. It computes the frequency and radial-measure units of its ordinary source map. It does not evaluate a new target, propagator, Fourier array, or scientific certificate.

The conclusion is restricted to a real physical parameter slice, the actual increasing radial coordinate, and the original interval on which the genuine-column theorem applies. It is not an inverse for the complete nonradial core operator or its two-ended boundary problem.

## 1. Exact reference and normalization

Use the definitions in [the common radial reference, C.12--C.18](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md) and [the genuine columns, A.19--A.27](R133-supplement-genuine-common-radial-reference-columns-and-two-source-ports.md). For either sign of j, put
$$
 n=4|j|\ge N=388,\qquad \lambda=n^{2/3},\qquad L=\frac1{2000}.
 \tag{K.1}
$$
On the true radial branch let T increase from -L to 0, with
$$
 \kappa=T_r>0,\qquad
 0<\kappa_-\le\kappa\le\kappa_+,\qquad
 0<G_-\le |G|\le G_+,\qquad
 0<a_-\le |a|\le a_+,\qquad |\mathfrak c|\le c_+ .
 \tag{K.2}
$$
These constants must enclose every retained frequency and the same actual real parameter slice. Here a and the connection coefficient \mathfrak c are the original frequency-dependent coefficients in C.12; \mathfrak c is not a mean source. No numerical values for the constants in K.2 are asserted.

Let
$$
 \Psi_j(T)=
 \begin{pmatrix}\widehat f_j(T)&g_j(T)\\
                 \widehat f_{j,T}(T)&g_{j,T}(T)\end{pmatrix},
 \qquad \det\Psi_j=\frac{n^{2/3}}{\pi}.
 \tag{K.3}
$$
The columns solve Y_TT=(n^2T-V_j)Y with the genuine potential. They are the full two-column basis from A.19, including the actual root shear. They are not an Ai-only boundary condition.

For the reference physical state h_j define
$$
 U_j=\frac{h_{2,j}}{G},\qquad
 P_j=\frac{i\epsilon n a\,h_{1,j}+\mathfrak c h_{2,j}}
                       {\kappa G},\qquad
 \xi_j=n^{-7/6}\Psi_j^{-1}\binom{U_j}{P_j}.
 \tag{K.4}
$$
Thus (U,P)=n^{7/6}\Psi_j\xi_j. This is the density normalization from the actual root parametrix. It is not the height normalization n^{1/6}.

For independent ordinary source rows F_1,F_2 the exact equation C.14 gives
$$
 \frac{d\xi_j}{dr}
 =n^{-7/6}\Psi_j(T(r))^{-1}
 \begin{pmatrix}
 0&G^{-1}\\
 i\epsilon n a/(\kappa G)&\mathfrak c/(\kappa G)
 \end{pmatrix}
 \binom{F_{1,j}}{F_{2,j}} .
 \tag{K.5}
$$
In particular F_2 is not differentiated. The factor dT=\kappa dr has already been used to obtain K.5.

## 2. Two complete row integrals

Write Y_j=(\widehat f_j,g_j) and use Euclidean row norm. The bounds in [V.8 and V.14--V.15](R133-supplement-genuine-negative-reference-column-operators-and-complete-source-ledger.md) apply to the entire two-column row. They do not require an extra factor sqrt(2).

Put h=-T and t=2nh^{3/2}/3. On t<1 they give
$$
 \|Y_j\|\le8,\qquad \|Y_{j,T}\|\le8n^{2/3}.
 \tag{K.6}
$$
On t\ge1 they give
$$
 \|Y_j\|\le9n^{-1/6}h^{-1/4},\qquad
 \|Y_{j,T}\|\le\frac{21}{2}n^{5/6}h^{1/4}.
 \tag{K.7}
$$
The second inequality follows from the complete row bound 9 and
1+1/(6t)\le7/6. Both signs and both genuine columns remain present.

Let h_n=(3/(2n))^{2/3}. Integration of the two regions yields
$$
 \begin{split}
 I_Y(n)&:=\int_{-L}^0\|Y_j(T)\|^2\,dT\\
 &\le64\min(L,h_n)+162n^{-1/3}\sqrt L
 <18n^{-1/3},\\
 I_{Y_T}(n)&:=\int_{-L}^0\|Y_{j,T}(T)\|^2\,dT\\
 &\le64n^{4/3}\min(L,h_n)
          +\frac{147}{2}n^{5/3}L^{3/2}
 <n^{5/3}.
 \end{split}
 \tag{K.8}
$$
These are direct integral majorants, including the case h_n>L. For the first, use min(L,h_n)\le sqrt(Lh_n), (3/2)^{1/3}<2 and sqrt(L)<1/40. The resulting coefficient is less than (128+162)/40<18. For the second use min(L,h_n)\le L and N^{1/3}>7. Its coefficient is bounded by
$$
 \frac{64}{14000}+\frac{147}{160000}<1 .
 \tag{K.9}
$$
Extending either nonnegative high-region integral down to zero only enlarges the bound. It does not assert that the high asymptotic formula holds in the central region.

## 3. The two ordinary source kernels

The exact inverse in K.3 is
$$
 \Psi_j^{-1}
 =\pi n^{-2/3}
 \begin{pmatrix}
 g_{j,T}&-g_j\\
 -\widehat f_{j,T}&\widehat f_j
 \end{pmatrix}.
 \tag{K.10}
$$
Combining K.5, K.8 and dr=dT/\kappa gives three constants
$$
 A_1=\frac{\pi\sqrt{18}\,a_+}{\kappa_-^{3/2}G_-},\qquad
 A_{20}=\frac{\pi}{\sqrt{\kappa_-}G_-},\qquad
 A_{21}=\frac{\pi\sqrt{18}\,c_+}{\kappa_-^{3/2}G_-}.
 \tag{K.11}
$$
For any subinterval with endpoints r_0,r in the same branch, variation of constants and Cauchy--Schwarz give
$$
 \|\xi_j(r)-\xi_j(r_0)\|
 \le A_1 n^{-1}\|F_{1,j}\|_{L^2_r}
       +(A_{20}n^{-1}+A_{21}n^{-2})
                                      \|F_{2,j}\|_{L^2_r}.
 \tag{K.12}
$$
The source norms on the right may be taken over the full branch. This also bounds the supremum over r. The signs of backward integration are retained in the exact integral and disappear only when its norm is bounded.

For clarity, the common factor before the source columns is n^{-11/6}. The first physical row contributes n, and the height row integral contributes n^{-1/6}; their product is n^{-1}. The second physical row has a derivative-row term n^{5/6} and a connection term n^{-1/6}; these give n^{-1} and n^{-2}. The three powers of \kappa in A_1 and A_21 consist of the physical source factor \kappa^{-1} and the square-root measure factor \kappa^{-1/2}. There is only the latter factor in A_20.

Put \Lambda_j=sqrt(1+16j^2) and
$$
 \|\xi\|_{\mathfrak M_s}^2
   =\sum_{|j|\ge97}\Lambda_j^{2s}
                       \sup_r\|\xi_j(r)\|^2 .
 \tag{K.13}
$$
For a zero initial coefficient and any real s, K.12 gives
$$
 \|\xi\|_{\mathfrak M_{s+1}}
 \le\frac{17}{16}\left[
 A_1\|F_1\|_{L^2_rH^s}
 +(A_{20}+A_{21}/388)\|F_2\|_{L^2_rH^s}\right].
 \tag{K.14}
$$
Here \Lambda_j/n<17/16. Parseval and nonnegative Fubini justify the sum of the squared radial source norms. The two source rows are combined by the displayed triangle inequality; no false orthogonality between them is used.

## 4. The complete negative reference body output

From C.13 and K.4,
$$
 h_{2,j}=G n^{7/6}Y_j\xi_j,\qquad
 h_{1,j}=\frac{G}{i\epsilon a}\,n^{1/6}
                  (\kappa Y_{j,T}-\mathfrak c Y_j)\xi_j .
 \tag{K.15}
$$
K.8 therefore proves a physical pair block-sum bound
$$
 \|h_j\|_{L^2_r(\ell^2_{\rm pair})}
       \le L_B n\sup_r\|\xi_j(r)\|,
$$
$$
 L_B=\frac{G_+}{\sqrt{\kappa_-}}
 \left[\sqrt{18}+\frac{\kappa_+}{a_-}
                  +\frac{\sqrt{18}\,c_+}{388a_-}\right].
 \tag{K.16}
$$
The block sum dominates the pair Euclidean norm. This estimate remains valid for an inhomogeneous coefficient function \xi_j(r); it does not require constant coefficients.

Consequently
$$
 \|h\|_{L^2_rH^s_{\rm pair}}\le L_B\|\xi\|_{\mathfrak M_{s+1}} .
 \tag{K.17}
$$
Combining K.14 and K.17 gives a same-order ordinary-source estimate for this reference Cauchy problem on the negative branch. It does not impose or solve the true right boundary condition.

## 5. A separate point trace at a fixed strict negative cut

Fix T_c=-h_c<0 in this same interval. A body L2 estimate is not used as a trace estimate.

At the central frequencies t_c<1, n^{1/6}<(3/2)^{1/6}h_c^{-1/4} and 8(3/2)^{1/6}<9. Together with K.7 this proves for every retained n
$$
 \|Y_j(T_c)\|\le9n^{-1/6}h_c^{-1/4},\qquad
 \|Y_{j,T}(T_c)\|
 \le8n^{2/3}+\frac{21}{2}n^{5/6}h_c^{1/4}.
 \tag{K.18}
$$
The second bound is a sum of valid alternatives. It remains valid whether the frequency is central or oscillatory. Substitution in K.15 gives
$$
 \|h_j(r_c)\|_{\ell^2_{\rm pair}}\le L_C n\|\xi_j(r_c)\|,
$$
$$
 L_C=G_+\left[
 9h_c^{-1/4}
 +\frac{\kappa_+}{a_-}
       \left(8\,388^{-1/6}+\frac{21}{2}h_c^{1/4}\right)
 +\frac{9c_+}{388a_-}h_c^{-1/4}
 \right].
 \tag{K.19}
$$
Thus
$$
 \|h(r_c)\|_{H^s_{\rm pair}}\le L_C\|\xi\|_{\mathfrak M_{s+1}}.
 \tag{K.20}
$$
This cut is a fixed strict negative radius. It is not the turning point, the positive joining cut, or the actual finite193 cut at 9/10.

## 6. Root and seam data retain different units

At T=0 the exact root identity is still A.26:
$$
 \binom{U}{n^{-2/3}P}
 =
 \begin{pmatrix}
 0&1\\
 i\epsilon a/\kappa&n^{-2/3}\mathfrak c/\kappa
 \end{pmatrix}
 \binom{n^{1/3}h_1}{h_2}.
 \tag{K.21}
$$
In particular a unit density coefficient has root mixed size of order n^{7/6}, not n. The integrated estimate K.16 does not remove this point-trace factor. When the already proved positive graph or negative root Cauchy theorem is used with its mixed root input, that exact factor and its full frame constants remain.

An original physical seam with raw jump J_j has coefficient jump
$$
 [\xi_j]=n^{-7/6}\Psi_j^{-1}\mathcal T_j J_j
 \tag{K.22}
$$
only when the same continuous reference coordinates are used on both sides. If the actual reference or gauge changes, use the full one-sided coordinate event in addition to the raw jump. The genuine mean j=0 is always the independent original scalar equation; K.4 and K.22 are not defined there. No mean, finite complement, boundary row or affine source is discarded.

## 7. Exact limit of this result

K.5--K.20 are proved for the genuine radial reference, on real r with real increasing T. They cannot be applied to a complex parameter curve T(r) by replacing its measure with dT=\kappa dr and integrating over a real interval.

For the complete physical operator, C.18 contains
$$
 \mathcal T_j(\Delta\mathcal G)_{jm}\mathcal T_m^{-1}.
 \tag{K.23}
$$
Its principal nonradial drift is still first order. The input and output frequency matrices do not commute through this coupling. The present proof supplies neither a smallness estimate for K.23 nor an ordinary-source norm for pullback to a tilted nonradial (T,X) coordinate surface.

The full strong return also needs its actual incoming coordinate inverse, nonmean normalizers, all original physical seams, the genuine positive two-ended selection, the same-background scalar phase, and its finite complement. These requirements are not replaced by a small reference Wronskian or by the given-head positive graph. In particular this result grants no complete high BVP inverse, no finite193-to-infinite Schur closure and no final nu response.

The proved contribution is the explicit one-derivative gain in the two ordinary reference source kernels, together with the separate one-derivative losses for the negative body and strict-cut outputs. It fixes their frequency and measure units without recomputing any accepted scientific input.
