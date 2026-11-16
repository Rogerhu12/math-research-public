# R133 supplement: asymmetric Schur and Parseval bounds for the unchanged positive cutoff

2026-11-16. New analytic bound; no new scalar evaluation.

[WPC](R133-supplement-complete-positive-cutoff-in-its-actual-output-window.md) and its actual [PCRA](R133-supplement-actual-positive-cutoff-and-reflected-coefficient-bounds.md) success already preserve uniform zero- and second-derivative bounds for each complete positive-cutoff symbol. A fixed input column also satisfies Parseval. Using Parseval only in that column sum gives a different complete Schur bound. The other sum uses the full pointwise bounds and allows arbitrary dependence on the input label.

The same genuine trial, terminal condition, root shear, cutoff, positive boundary problem, both physical rows, means, entire input and all output modes are retained. This note does not change any previously completed scalar or evaluate it again.

## WSP1. The exact weighted matrix

Keep WPC's normalized angular measure, physical period pi/2, n=4|j|, |j|>=97, and
$$
 \Lambda_j=(1+16j^2)^{1/2}.
$$
After the actual real scalar change xi=X(phi), the same WPC.6 and WPC.10 matrix is
$$
 M_{mj}=\Lambda_m^{-2/3}\widehat b_j(m-j)\Lambda_j^{2/3}.
 \tag{WSP.1}
$$
Here b_j already contains the factor Lambda_j^(2/3)n and both original genuine reference components. It is a scalar function of xi for each fixed admitted input j. Its dependence on j is unrestricted.

Suppose uniformly in j, the real family and the original radial transition,
$$
 \|b_j\|_\infty\le D_0,\qquad
 \|\partial_\xi^2b_j\|_\infty\le D_2.
 \tag{WSP.2}
$$
These are exactly WPC's already-weighted symbol bounds, after its true inverse angle. They are not unweighted amplitude moduli. The same physical n^(7/6) input normalization and the WPC profile shift +5/2 remain.

For l=m-j, the original Bessel ratio obeys
$$
 \Lambda_j^{2/3}/\Lambda_m^{2/3}
 \le w_l:=(1+4|l|)^{2/3}.
 \tag{WSP.3}
$$
Every output m, including zero and the full finite output, is kept. An absent input j may simply be bounded by zero when extending a sum over all integer l.

## WSP2. Complete row sum

Fix an integer L>=1. Normalized Fourier coefficients satisfy, for each individual j,
$$
 |\widehat b_j(l)|\le D_0,\qquad
 |\widehat b_j(l)|\le\frac{D_2}{16l^2}\quad(l\ne0).
 \tag{WSP.4}
$$
For a fixed output m, the symbol b_(m-l) varies with l. Use only (WSP.4) in this sum. Splitting at |l|=L and using 1+4l<=5l for l>=1 gives
$$
 \sum_{|j|\ge97}|M_{mj}|
 \le D_0\!\left(1+2\,5^{2/3}\sum_{l=1}^L l^{2/3}\right)
       +\frac{5^{2/3}D_2}{8}
                      \sum_{l=L+1}^{\infty}l^{-4/3}.
$$
Monotonicity gives the complete upper estimates
$$
 \sum_{l=1}^L l^{2/3}
 \le\frac35\big((L+1)^{5/3}-1\big),\qquad
 \sum_{l=L+1}^{\infty}l^{-4/3}\le3L^{-1/3}.
$$
Consequently the full row bound is
$$
 R_L(D_0,D_2)=a_LD_0+b_LD_2,
\quad
 a_L=1+\frac65\,5^{2/3}\big((L+1)^{5/3}-1\big),
\quad
 b_L=\frac38\,5^{2/3}L^{-1/3}.
 \tag{WSP.5}
$$
No common symbol, orthogonality or input-label derivative is assumed in this row argument.

## WSP3. Complete column sum

Now fix one input j. Parseval on the normalized circle yields
$$
 \sum_{l\in\mathbb Z}|\widehat b_j(l)|^2
       =\|b_j\|_2^2\le D_0^2,
\qquad
 \sum_{l\in\mathbb Z}(4l)^4|\widehat b_j(l)|^2
       =\|\partial_\xi^2 b_j\|_2^2\le D_2^2.
 \tag{WSP.6}
$$
This use is valid because j is fixed. It is not a Parseval assertion for the varying-symbol row of WSP2.

Cauchy--Schwarz separately on the complete head and tail gives
$$
 \begin{split}
 \sum_m|M_{mj}|
 &\le D_0\left(\sum_{|l|\le L}w_l^2\right)^{1/2}\\
 &\quad+D_2
       \left(\sum_{|l|>L}\frac{w_l^2}{(4l)^4}\right)^{1/2}.
 \end{split}
$$
Keep the zero term in the head. The finite and infinite sums satisfy
$$
 \sum_{|l|\le L}w_l^2
 \le1+\frac67\,5^{4/3}\big((L+1)^{7/3}-1\big),
$$
$$
 \sum_{|l|>L}\frac{w_l^2}{(4l)^4}
 \le \frac{5^{4/3}}{128}\sum_{l=L+1}^\infty l^{-8/3}
 \le\frac{3\,5^{4/3}}{640}L^{-5/3}.
$$
Thus the complete column bound is
$$
 C_L(D_0,D_2)=c_LD_0+d_LD_2,
$$
$$
 c_L=\left[1+\frac67\,5^{4/3}
               \big((L+1)^{7/3}-1\big)\right]^{1/2},
\qquad
 d_L=\frac{5^{2/3}}{16}\sqrt{\frac65}\,L^{-5/6}.
 \tag{WSP.7}
$$
Both carrier signs are already input labels in WSP.1. Parseval is applied to the scalar sum of the two genuine reference components after their complete component-sum bounds, so no component or reflected-pair normalization is omitted.

## WSP4. The new complete three functionals

The Schur test, first on finite sequences and then by completion, gives
$$
 \|M\|_{\ell^2\to\ell^2}
 \le\sqrt{R_L(D_0,D_2)C_L(D_0,D_2)}.
 \tag{WSP.8}
$$
This uses two different complete sums; it does not claim output-block orthogonality.

Choose once and for all
$$
                         L=128 .
 \tag{WSP.9}
$$
This is an integer splitting parameter for the proof, not a physical input or output cutoff. All frequencies remain.

For q=w, h^amp, g^amp, read directly from the actual PCRA science
$$
 D_{0,q}=\text{complete weighted phase derivative upper}[0],\qquad
 D_{2,q}=\text{complete inverse-angle second derivative upper}.
$$
Read the same saved scalar-pullback bound C_(X,2/3). Define the new whole functional
$$
 F_q^{\rm SP}
 =C_{X,2/3}
       \sqrt{R_{128}(D_{0,q},D_{2,q})
                    C_{128}(D_{0,q},D_{2,q})}.
 \tag{WSP.10}
$$
Then the exact same reasoning after WPC.14 gives
$$
 \|P{\sf T}(q):H^{-4/3}\to H^{-2/3}\|
       \le F_q^{\rm SP}.
 \tag{WSP.11}
$$
The proof also bounds the unprojected output, so no mean was used to reduce either Schur sum. The scalar pullback is applied after the matrix bound and is not replaced by a full-density coordinate map.

No profile, amplitude derivative, geometry derivative, moment, inverse-angle derivative or matrix-word product is reevaluated. Their completed values and scopes are the inputs to a new Schur/Parseval combination.

## WSP5. The whole original physical pair and positive correction

Read the three already-completed ordered-word bounds from PCRA,
$$
 J^\#=\text{complete ordered J word upper},\quad
 (JL)^\#=\text{complete ordered JL word upper},\quad
 (JB)^\#=\text{complete ordered JB word upper}.
$$
Their one window conversion is already included. They are not recomputed from the old z-products.

Keep WPC.21's full physical reconstruction. Its new positive candidate is
$$
 \begin{aligned}
 C_{1,\rm SP}
   &=(1+(JL)^\#)F_h^{\rm SP}
        +J^\#F_g^{\rm SP}+(JB)^\#F_w^{\rm SP},\\
 C_{2,\rm SP}&=F_w^{\rm SP},\\
 C_{{\rm cut},\rm SP}
   &=K_\chi\sqrt{C_{1,\rm SP}^2+C_{2,\rm SP}^2},\\
 C_{+,\rm SP}^w
   &=K_{\rm pos}(C_{\rm vol}+C_{{\rm cut},\rm SP}+C_{\rm FH}).
 \end{aligned}
 \tag{WSP.12}
$$
Here K_chi is the complete saved physical cutoff radial factor. The original ordinary-volume source, finite-head source and complete receiver K_pos are read verbatim from PCRA's copied PC records. The Euclidean physical pair, both signs, complete seven-port receiver and its original factor 9 stay exactly as in WPC. The actual physical mean conventions are unchanged.

A new scientific consumer retains every new row head/tail and column head/tail contribution, their complete sums, all three full functionals, all terms of C_1, both rows, the complete cutoff and the received positive candidate. It compares only the final serialized complete C_(+,SP)^w record with PCRA's already-selected complete positive record. Every candidate is retained; a tie keeps the old complete candidate. Componentwise subtraction or a comparison of different operators is not used.

The root finite received term remains distinct. The successful WCE coefficient result is frozen and unchanged. All negative sources, true jumps, four endpoint terms, independent mean/amplitude/radial-head inputs and the actual physical finite border retain their separate obligations. This proof supplies no passing high inverse or surface.

## WSP6. Exact read-only scientific inputs

The prior complete science is
notes/positive_cutoff_and_reflected_coefficient_refinement_ci/run-43812987299-1/actual-scientific-conclusion.json,
Git blob 3d6fbe7cb3c345f5fd4631428e4189823d05684a,
55533 bytes, SHA256 e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d.
Its complete 38-field/22-gate success, original parameter identities, seven graphs, exact original records and all five original scope collections are required. The WCE selected-member restriction is not extended, and the WPC original real family remains.

Exact field paths inside that science are:

| Input | Complete field path |
|---|---|
| Scalar pullback | complete_wpc_geometry_and_moment_conclusion.geometry.scalar_pullback_Hminus2_3_upper |
| Physical cutoff radial factor | complete_wpc_geometry_and_moment_conclusion.geometry.physical_cutoff_radial_factor_upper |
| For q=w,h,g: D0 | complete_wpc_cauchy_and_schur_conclusion.complete_three_amplitude_functionals.q.complete_weighted_phase_derivative_upper[0] |
| For q=w,h,g: D2 | complete_wpc_cauchy_and_schur_conclusion.complete_three_amplitude_functionals.q.complete_inverse_angle_second_derivative_upper |
| J, JL, JB words | complete_wpc_positive_correction_conclusion.complete_ordered_J_word_upper, .complete_ordered_JL_word_upper, .complete_ordered_JB_word_upper |
| Whole volume, finite-head source, receiver | copied_original_scalar_records.WPC.Cvol, .CFH, .Kpos |
| Prior selected complete positive bound | complete_wpc_positive_correction_conclusion.whole_received_positive_choice.complete_selected_upper |

Only these new positive formulas may be evaluated by a new public child after the complete analytic contract and exact input closure are frozen. There is no new numerical claim in this note.

| Complete analytic primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WPC actual-window recipe | 92f5e51af2af959794b527c89d03f103d9e69422 | 16086 | 2bc45c4c67261986bf2e94bb889d20757be8c713c31542c6a08e1da4353f8468 |
| PCRA actual complete targets | 8e0ed75a0fc4f80272d90e20711983c91cff86f2 | 12537 | f2b1e603654a3823bfc0e20664f191d06db739afa1dfdbe9b77426227b55f8ea |
