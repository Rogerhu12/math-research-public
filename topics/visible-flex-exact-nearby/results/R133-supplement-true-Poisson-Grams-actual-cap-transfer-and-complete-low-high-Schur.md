# R133 supplement: true Poisson Grams, actual-cap transfer and a complete low/high Schur criterion

2026-11-15, newton_source.

This is a conditional consumer theorem for the completed scalar conclusions of the ongoing finite193 Green computation. It identifies exactly which numerical inequalities would transfer that inverse to the actual nonlinear cap and then close the infinite low/high system. No numerical gate of the ongoing run is presumed here. The original successful cells, source bounds, adjoint Grams and propagators are read only.

The centre is ac1 with continuous repair
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47.
The inner generator, physical eta0, original nu and delta=0 are fixed. The direction, when used below, is the complete continuous Z with definition
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
We use the original reflection sector, its orthonormal sine/cosine coordinates, and its complete even mean.

The main inputs are:

- [the complete directional finite193 contract](../notes/2026-11-15-R133-complete-directional-matrix-Green-contract.md);
- [the true complete97 Poisson contract](../notes/2026-11-15-R133-complete97-right-Poisson-Gram-contract.md);
- [the full cap/same97 contraction contract](../notes/2026-11-15-R133-complete-same97-cap-posterior-and-Poisson-contract.md);
- [I: the actual-cap inner Poisson comparison](R133-supplement-actual-cap-inner-Poisson-perturbation-and-complete97-interface.md);
- [R: the actual inner-cap/tail-height interface](R133-supplement-actual-inner-cap-complete-tail-height-feedback-and-97-interface.md), including its uniform-height clarification;
- [P: the full-frequency moving cap rows](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md);
- [the same-Z finite response result](R133-supplement-actual-native-point-Hessian-same-Z-Green.md);
- [the complete phase-response functional P.16--P.25](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md);
- [the sharp full-label row L.2 and L.8--L.9](R133-supplement-full-label-L2-energy-and-sharp-phase-row.md).

## 1. Three true outputs, with a separate cut trace

Put L=9/10 and rplus=2383968743003/10^13. Let G0 be the true old finite193 inverse on [0,L], including its true 97 right rows and 96 waist rows. Let R0 be its right Poisson column. Its input is the original 97-dimensional regular-row Euclidean space: 96 odd rows and one independent even-mean row. There is no second rho input weight.

The output spaces are
$$
 Y_B=L^2([0,L];L^2_{\rm pair}),\qquad
 Y_N=L^2([0,rplus];L^2_{\rm pair}),\qquad
 Y_C=L^2_{\rm pair}\text{ at }L .
 \tag{S.1}
$$
The complete actual certificates must give
$$
 R_0^*R_0\preceq H_Y,\qquad
 \|R_0\|_{\mathbb R^{97}\to Y}\le p_Y,\qquad Y=B,N,C .
 \tag{S.2}
$$
Here pY is the recorded directed upper bound for sqrt(||HY||), not a sampled eigenvalue. HY is the true posterior Gram. The proposal and posterior-error Grams separately do not replace it.

Let ALH be the fixed M32 high-to-low body block, and CH0 the old full even-high-trace-to-97 cap column. The same completed computation supplies
$$
 \|G_0A_{LH}\|_{L^2_rL^2_H\to Y}\le a_Y,\qquad
 \|R_0C_{H0}\|_{L^2_{{\rm e},H}\to Y}\le c_Y .
 \tag{S.3}
$$
The aY bounds include the reference and complete model-error channels. The cY bounds retain the full signed contraction with Wcap and all infinite composition tails. A cap trial cutoff is not a cutoff on CH0's input.

The whole and negative-body L2 outputs never supply the cut output. All quantities involving pC, aC or cC require the actual point-trace certificate.

## 2. Complete actual-cap perturbation in the same fixed coordinates

Write E for the restriction of a low cut state to its 97 even coordinates; ||E||<=1. Use exactly the old endpoint maps S0 and HC0 in P, without commuting Fourier projections through them.

I.21--I.28 and R's uniform-height clarification give the actual boundary changes
$$
 \Delta E^0=-S_0(K_{B,*}-K_{B,0})P_\perp H_{C,0},\qquad
 \Delta M^0=-(K_{0,*}-K_{0,0})P_\perp H_{C,0}.
 \tag{S.4}
$$
Let
$$
 s_* \ge \|S_0\|,\qquad c_* \ge \|H_{C,0}\|,\qquad
 \epsilon=\max(s_*,1)c_*/5 .
 \tag{S.5}
$$
These are the original complete all-mode constants. The second is not a finite97 compression. Projecting the output onto the original 97 rows gives two restrictions of the same full operator:
$$
 \|\Delta B_L\|_{\ell^2_{97}\to\ell^2_{97}}\le\epsilon,\qquad
 \|\Delta C_H\|_{L^2_{{\rm e},H}\to\ell^2_{97}}\le\epsilon .
 \tag{S.6}
$$
The first restriction includes the even constant input. HC0 can send that input to infinitely many physical nonmean modes. All such modes are included before the true Poisson map and final low projection.

The old reference K0, residual Hessian H0, physical centre and source coordinates remain locked. The actual height may be any value in M's admitted product ball, while the partial gamma direction keeps that height fixed. Uniformity does not replace the old K0 by a newly chosen reference.

For the separately proved fixed-background tail-height proxy, one may replace 1/5 in (S.5) by 1/5+2^(-52000000), provided exactly the R source/charge conventions are retained. This does not supply an unknown negative-high inverse, a nonlinear tail solution, or a reduced metric-charge inverse.

A useful operator bound is
$$
 \|R_0\Delta B_L\|_Y,\ \|R_0\Delta C_H\|_Y
                  \le\epsilon p_Y .
 \tag{S.7}
$$
There is no factor sqrt(97). The larger epsilon*sqrt(tr HY) is also valid by a Hilbert--Schmidt estimate, but is unnecessary for this already proved full operator perturbation.

## 3. An actual finite193 boundary inverse from one scalar cut gate

Keep the inner body equation and waist rows unchanged and replace only the old low cap rows by the actual rows in (S.4). For old-data solution u0, the new solution obeys
$$
 u=u_0-R_0\Delta B_L E u(L).
 \tag{S.8}
$$
Signs of independently supplied right data can be inserted into u0. At the cut the feedback has norm at most
$$
                         \tau=\epsilon p_C .
 \tag{S.9}
$$
If the directed gate tau<1 holds, Neumann inversion of this actual cut operator proves existence and uniqueness for the changed finite boundary problem. Reconstruction by (S.8) gives its full solution. This uses the original true inverse, not an invertibility assumption on the nominal cap matrix.

For any old load family with bounds ||u0||Y<=dY, define
$$
 d_Y^*=d_Y+\frac{\epsilon p_Yd_C}{1-\tau},\qquad
 d_C^*=\frac{d_C}{1-\tau}.
 \tag{S.10}
$$
The first formula specializes to the second at Y=C. The new right Poisson norms satisfy
$$
                              p_Y^*\le\frac{p_Y}{1-\tau}.
 \tag{S.11}
$$

These scalar inequalities do not assert the false matrix inequality
Hnew<=HY/(1-tau)^2. The exact boundary inverse can rotate the 97 input directions. If a full new input Gram is wanted, a legal alternative, for any t>0, is
$$
 R_{\rm new}^*R_{\rm new}\preceq
 (1+t)H_Y+
 (1+t^{-1})
 \left(\frac{\epsilon p_Yp_C}{1-\tau}\right)^2I_{97}.
 \tag{S.12}
$$
The right-hand side is a proved Loewner majorant for the new true Poisson Gram. It follows by applying Young to Rnew=R0+(Rnew-R0). Exact signed conjugation by a separately certified actual boundary inverse is another option. A whole-matrix majorant is not made by entrywise minima.

## 4. The old direction-sensitive columns after the actual-cap change

For a high body input h and an independent high even trace z, the low equation reads
$$
 u=G_0A_{LH}h-R_0(C_{H0}+\Delta C_H)z
                       -R_0\Delta B_LEu(L)+u_{\rm data}.
 \tag{S.13}
$$
Therefore the following directly consumable constants are valid:
$$
 \begin{aligned}
 a_Y^*&=a_Y+\frac{\epsilon p_Ya_C}{1-\tau},\\
 c_Y^*&=c_Y+\epsilon p_Y+
          \frac{\epsilon p_Y(c_C+\epsilon p_C)}{1-\tau},\\
 p_Y^*&=\frac{p_Y}{1-\tau}.
 \end{aligned}
 \tag{S.14}
$$
In particular
aC*=aC/(1-tau) and cC*=(cC+epsilon*pC)/(1-tau).
The old cY remains the signed HY--Wcap contraction. Only the new uniformly bounded perturbation uses (S.7).

The two epsilon*pY contributions in cY* have different origins: the direct change of the high cap column, and the low boundary feedback driven by the resulting cut response. They are not independent copies of the high input. Formula (S.14) follows from a triangle inequality on that same input.

If one of these bounds is too large, this is a limitation of the available enclosure. It does not prove that the true operator is large. A tighter result then requires a newly proved directional perturbation covariance or a sharper actual cap comparison. The old HY cannot simply be relabelled as the new true Gram.

## 5. A quantitative complete low/high Schur condition

Use solution spaces with a genuine trace norm, and set
$$
 l=\binom{\|u_L\|_{Y_B}}{\|u_L(L)\|_2},\qquad
 h=\binom{\|u_H\|_{L^2([0,L];L^2_{\rm pair})}}
              {\|u_H(L)\|_2}.
 \tag{S.15}
$$
The low vector retains all 193 states, and the high trace is an independent coordinate. In particular no high L2 body bound substitutes for its point trace.

From (S.14) the low feedback is bounded by
$$
 l\le d+A h,\qquad
 A=\begin{pmatrix}a_B^*&c_B^*\\a_C^*&c_C^*\end{pmatrix}.
 \tag{S.16}
$$
A bound for the full high pair trace also bounds its even part needed in (S.13).

Suppose, independently, that the actual high/high problem has a true two-ended inverse GH in these solution and source spaces. It must include its complete high cap rows, physical root conditions, seams and all permitted source/mean ports. Suppose its responses to the low body and low cut inputs give a nonnegative matrix B and data vector e such that
$$
                              h\le e+B l .
 \tag{S.17}
$$
The entries of B must pay the full low-to-high body block and full cap low-to-high column, in their true source units. A finite97 forward cap matrix can pay its proved low-input column, including its complete output tail. It cannot pay the arbitrary-high-input cap block.

With K=AB a sufficient and directly testable Schur gate is
$$
 K_{11}<1,\qquad K_{22}<1,\qquad
 (1-K_{11})(1-K_{22})>K_{12}K_{21}.
 \tag{S.18}
$$
For a nonnegative two-by-two matrix these conditions imply spectral radius less than one. In a positive weighted product norm the actual feedback is then a contraction. The complete solution bounds are
$$
 l\le(I-AB)^{-1}(d+A e),\qquad h\le e+B l .
 \tag{S.19}
$$
Existence and uniqueness follow from the actual block operators, not from a merely formal inequality on unspecified solutions.

All higher body input labels above160 vanish in ALH only for this fixed M32 body block. They do not vanish in the cap. The actual cap HH and HL blocks are all-frequency operators. The high/high inverse in (S.17) includes them, or else must contain their explicitly paid separate feedback variables.

A positive graph with a prescribed complete head is not GH. If that graph is used to construct GH, its head on the entire cap and its true high cut trace must first be supplied through the full physical Poisson interface. The current genuine-column amplitude and volume-source bounds are also not GH. At the time of this theorem, no numerical matrix B satisfying (S.17) is being asserted.

The negative-window readout, once (S.19) is paid, is
$$
 \|u_L\|_{Y_N}\le d_N+a_N^*h_1+c_N^*h_2 .
 \tag{S.20}
$$
A high negative-window readout is another true GH output, with its own data and two low-input gains. It cannot be inferred by renaming a primitive or weak Cauchy output.

## 6. Using the original complete Z residual without changing its identity

The accepted same-Z finite result has
$$
 e_{0,B}<.007490301792401,\quad
 e_{0,N}<.003509417445587,\quad
 e_{0,C}\le .060889190964764 .
 \tag{S.21}
$$
The last follows from its actual C0-in-r estimate, not its L2 estimate. These are bounds for the old complete finite solution minus the same continuous Z. The first is the whole-inner interval [0,9/10] bound. The second is the separately certified ordinary pair L2 bound on [0,rplus], including the entire true-root bracket. These windows remain distinct: the .007490301792401 whole-window bound has not been replaced by the negative-window bound.

The reason the negative window is relevant to the nu phase row is the original full response-functional theorem. Its P.17--P.21 integrate the response contribution only from 0 to the true r_*. Its P.24 proves r_*<=rplus. Thus restriction from YN to [0,r_*] pays that particular scalar functional, while the complete regular response itself must still solve the full spatial problem with all original boundary and mean rows.

Its complete right source is below 1.379019669555e-7, its known full high cut output below 2.920495224265e-7, and its waist source below 1.121483070336e-15. The report retains the true mean, full 14 cap fees, the error on Zeven-w0 and the old complete error-operator norm. None of these particular-input bounds is an unknown-input operator norm.

Let ze be a proved ordinary norm of the actual Zeven(L), not the unrepaired trial. For the new actual cap, with all other reference data fixed, the old low residual response has bounds
$$
                         d_Y^0=e_{0,Y}+\epsilon p_Yz_e .
 \tag{S.22}
$$
Extra parameter, height, mean or boundary-source differences add their actual columns to dY0. Applying (S.10) gives the low data vector d and dN for the error qnu-Z.

The known high error source must be supplied to GH separately. It includes the complete known high body source AHL Z, every true high cap output, physical seam, mean and parameter/height port. For the fixed M32 body, the already proved known high source of Z has support97 through160; this fact does not truncate the unknown high solution. Its actual high cap source receives the additional bound epsilon*ze, with any new independent high data added separately.

If eL,N and eH,N are finally proved for the low and high parts of qnu-Z on the same fixed old angular circle, orthogonal Fourier projection gives the genuine all-mode gate
$$
                       e_{L,N}^2+e_{H,N}^2<\frac1{40000}.
 \tag{S.23}
$$
The complete even mean belongs to the low part. This is an ordinary pair L2 gate on [0,rplus]. It implies ||qnu-Z|| on [0,r_*] is less than 1/200; it asserts no 1/200 bound on [0,9/10]. In the same-background phase convention, P.16 defines the actual scalar Schur as tnu+L_Omega qnu. P.22 and the sharp row L.9 give
$$
 |L_\Omega(q_\nu-Z)|
 <1.274436\,\|G'\|_\infty\,
        \|q_\nu-Z\|_{L^2([0,r_*];L^2_{\rm pair})}
 \le1.274436\,\|G'\|_\infty\,\|q_\nu-Z\|_{Y_N}.
 \tag{S.23a}
$$
Here G is the phase coordinate in that sharp-row theorem, not the spatial Green inverse. Its proved bound ||G'||infty<1.015523233862 and L.2 imply that a complete same-background error at most1/200 leaves the physical phase row above .0071115274966255 and the normalized row above1/50. The exact meaning and source convention of qnu are those of P.16 and L section4, including the original mean and physical fourth-mode boundary rows. A changed angular measure, background, root window or metric requires its own transfer before this implication is used.

The old .003509417445587 bound alone does not imply (S.23): the changed low boundary response, full unknown-high feedback and all high residual sources still enter (S.19)--(S.22).

## 7. The actual gamma value domain is a separate, typed test

The nonlinear cap is admitted only when
$$
 \gamma=P_\perp\big(\Psi(Q_{\rm left})(L)-\widehat W(L)\big)_C
       \quad\hbox{satisfies}\quad \|\gamma\|_{A^0}\le10^{-9},
 \qquad \|f_B\|_{\dot A^2}\le2^{-60}.
 \tag{S.24}
$$
All additional low/high hypotheses of M and O retain their own types and quantifiers. A global moving C0 error below1e-4 is not this gamma test.

Equation (S.24) is only zero-width cap admission. The presently proved tail seed and Nash construction also require their stated positive-strip analytic hypothesis on the fixed gamma datum. In particular their original normalized A_sigma bound cannot be replaced by the A0 bound in (S.24), nor by a finite H8176 bound. The zero-width mixed-species cap theorem does not by itself construct a rough-gamma tail seed. Until a separate finite-regularity seed/transfer theorem has been proved, both the zero-width cap gate and that original analytic tail-input gate are retained.

There is a useful explicit finite-input bound. Write the fixed physical angle map as Phi0(theta)=theta+psi0(theta), put P0=||psi0||A0, and let C0,C1 bound the complete physical centre C and its theta derivative in A0. For u in the 97 orthonormal moving even coordinates,
$$
 \|P_\perp H_{C,0}u\|_{A^0}
 \le c_{\gamma,L}\|u\|_2,\qquad
 c_{\gamma,L}=\sqrt{193}\,e^{384P_0}
                    (C_0^2+C_1C_0/4).
 \tag{S.25}
$$
Indeed ||u||A0<=sqrt(193)||u||2, the physical input has maximal angular frequency384 before composition, and fixed-r Wiener composition costs exp(384P0). The primitive in HC0 costs1/4. The mean normalization is the original reflection normalization, not a discarded physical mean.

For a true nonlinear change h at the inner trace the exact test can be bounded as
$$
 \|\gamma\|_{A^0}\le
 c_{\gamma,L}\|h_{L,{\rm even}}(L)\|_2+
 \|P_\perp H_{C,0}h_{H,{\rm even}}(L)\|_{A^0}
 +\|P_\perp(\Psi(Q_0+h)-\Psi(Q_0)-D\Psi_0h)_C\|_{A^0}.
 \tag{S.26}
$$
This formula presumes Psi(Q0)=What at the same trace; an independent base mismatch is otherwise added. The high Wiener term and nonlinear chart remainder are separate obligations. Neither follows from the high L2 trace in (S.15). A certified stronger Sobolev trace may pay these zero-width terms with its actual multiplier/composition constants; it still does not imply a positive-strip analytic gamma norm. Any later smoothing or finite-regularity seed argument must specify its actual separated endpoints, true Poisson map, background regularity and full mean/phase normalization, rather than evaluate an unknown rough input at a complex angle.

Thus even a successful linear Schur test does not by itself put an unknown nonlinear boundary value in the gamma ball. The affine B/Cmean mismatch in I.25 is also retained; a height constant cannot cancel that curvature mean.

## 8. The parameter and charge Schur is still complete

Suppose the full spatial inverse in (S.19) has actually been proved. The following is a general bordered-problem template. Include only parameters, compatibility charges and equations that actually occur in the chosen geometric construction; it creates no extra geometric constraints. In the presently constructed freely placed single half-surface, its world height and frame are geometric outputs. They are not two independently prescribed world-anchor rows. Any later imposed matching or anchoring equation needs its own true column and compatibility statement.

Write the actual remaining finite-dimensional bordered problem, with all its independent parameters and charges retained, as
$$
 \mathcal D u-Ft=f,\qquad \Lambda u+D_{\rm par}t=b .
 \tag{S.27}
$$
Then the true parameter matrix is
$$
                 S_{\rm par}=D_{\rm par}+\Lambda\mathcal D^{-1}F .
 \tag{S.28}
$$
For approximate complete columns Zpar, put SZ=Dpar+Lambda Zpar. The residual columns are evaluated in the same full body, boundary, mean, trace and charge spaces used above. If their true corrections satisfy a verified operator bound
$$
 \|\Lambda(\mathcal D^{-1}F-Z_{\rm par})\|\le e_S
                  <\sigma_{\min}(S_Z),
 \tag{S.29}
$$
the full finite parameter Schur is invertible. A one-scalar nu version is valid only after the other retained parameter/charge block has been independently eliminated. Its familiar test is
|alpha+ell Z|>||ell(qnu-Z)|| in the explicitly stated scalar convention. For the phase row discussed in (S.23a), ell is the original L_Omega, whose response part is supported on [0,r_*]; other actual charge rows are evaluated in their own proved source and trace spaces.

One physical height constant lambda is not a replacement for the even-mean equation. Cap nu-bump support being empty does not delete induced gamma, far-height, metric-installation or independent mean columns. Neither the finite193 result nor the actual cap existence theorem silently resolves these bordered obligations.

## 9. Minimal actual consumer and present status

After successful completion of the current Green run, a minimal scalar consumer can read exactly three small maps from its actual conclusion summary:

| Quantity | Exact summary field |
| --- | --- |
| aY | complete_true_finite193_body_high_to_low_bounds |
| pY | complete_true_right_Poisson_operator_upper |
| cY | complete_same_input_directional_contractions[window].complete_operator_upper |

The three window keys are whole_inner_body, fixed_complete_negative_phase_window, and true_cut_trace. The consumer must check the real child, all complete mathematical gates, original source/manifest/runtime identities, completed coverage, fixed centre, exact boundary units, and the full output hash. A live prefix is not such an input.

Together with the independently proved complete constants s*,c*, these scalar maps suffice for (S.9)--(S.14). The previously computed cY already incorporates the signed matrix contractions; no old Gram needs to be reconstructed or recalculated. Only if a new direction-sensitive perturbation is sought would a new, fully proved covariance be needed.

The GH/B gate, high residual data, zero-width gamma value domain, any still-required analytic tail-input domain, and actual parameter matrix are separate inputs. A consumer lacking them reports the corresponding conditions as unproved. It does not insert zeros, replace them by a one-sided graph, or regard a successful finite scalar update as the infinite PDE inverse.

All new scalar evaluation, if requested, belongs to a public Actions consumer. This theorem performs no new numerical calculation and changes no active scientific source.
