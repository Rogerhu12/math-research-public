# R119 supplement: continuous exact-tail selection and the true second-phase response

2026-11-15, visible-exact / tail_connector.

**Status: proved analytic continuity on the stated parameter domain.** This paper identifies one continuous selection furnished by the actual iteration in S. It does not infer differentiability of that selection from a finite-regularity inverse theorem. In particular, the fixed-metric column in R is not renamed as the derivative of a family whose design parameters change.

The physical object, fixed stop, chosen five-box point, good exterior parameter and intrinsic nu are fixed throughout. The first design parameter is selected by L during the iteration. The second design parameter is the value associated with the actual RG seed and is then frozen during that one iteration. It can change when the inner datum changes.

The proofs used below are:

- [M: the two-input zero-width cap and complete inner outputs](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md);
- [RG: the rough-inner-data 94-step seed](R119-supplement-rough-inner-curvature-data-and-true-smoothed-B-seed.md);
- [S: exact far straightening and the complete graph Nash iteration](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md), including S.42--S.46;
- [Jph: the complete joint two-phase selection](R119-supplement-new-outer-joint-two-phase-scalar-normal-form-and-high-feedback.md);
- [Nph: the controlled joint phase estimates](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md);
- [L: the low-norm principal value map](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md);
- [E: the fixed reference graph and angular smoothing](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md);
- [A: the complete graph approximate inverse](R119-supplement-reference-graph-approximate-right-inverse-and-exact-port-defects.md);
- [G: the first-parameter projected source and Schur](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md);
- [Jr: three radial source jets and four state jets](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md);
- [O: the actual two-input exterior and all source units](R133-supplement-actual-two-input-cap-long-tame-forms-and-physical-Poisson.md);
- [Mhol: the complete finite-Sobolev holonomy and height chart](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md);
- [Cjet: the actual broken radial jets and holonomy retraction](R119-supplement-off-shell-controlled-radial-jets-and-exact-holonomy-retraction.md);
- [P: the true first-principal counterterm](R119-supplement-finite-Sobolev-principal-KAM-and-true-first-metric-counterterm.md);
- [I: the complete nearby proxy and its mean-charge identity](R119-supplement-nearby-finite-Sobolev-full-tail-proxy-inverse-and-complete-sources.md);
- [N: the two-level complete network](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md);
- [Qmet: exact metric sources and the full neighbor weights](R119-supplement-exact-nonlinear-ordinary-sources-and-Gamma-reference-height-lifts.md);
- [Gseed: the actual five-jet collar and graph seed](R119-supplement-new-94-B-collar-lift-and-actual-graph-seed.md);
- [Fph: the new exterior first-phase estimates](R119-supplement-new-outer-two-root-strong-scattering-and-complete-first-phase.md).

All angle norms use the physical signed set \(4\mathbb Z\). Ordinary Fourier mean, holonomy mean, flux charge and the one rigid height constant are kept distinct.

## 1. The parameter domain and the deterministic selection

Put \(r_\gamma=10^{-9}\). The real parameter set is
$$
 \mathcal D_\gamma=
 \left\{\gamma\in H^{8193}_{\ne0,\mathrm{ev}}:
   \|\gamma/r_\gamma\|_{A^0}\le1/128,\quad
   \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576}\right\}.
 \tag{C.1}
$$
Its topology is the relative \(H^{8193}\) topology. This is a physical-angle condition. It is not a conclusion about an arbitrary moving low-97 vector or about an arbitrary zero-width datum.

For every \(\gamma\), use exactly RG's incoming fixed point and its 94 ordered updates; denote the resulting label by \(a_{94}(\gamma)\). Set
$$
 \mathfrak q(\gamma)
   =\Gamma_2^*(a_{94}(\gamma))-\bar\Gamma_2.
 \tag{C.2}
$$
The radial reference used in S is the true reference with this second parameter and with its corresponding radial first-parameter compensation. Use the same cutoff sequence, the same unique complete proxy inverses, and the same normalization of the first-principal map at every step of S. There is no discretionary subsequence or choice of a new exterior good point.

The conclusions are continuity of the resulting nonmean height in the common graph specified below, continuity of its complete mean and height readouts, and compactness of the actual normalized far-height output in \(H^2\). No core solution graph or global self-map is assumed in these conclusions.

## 2. A genuine auxiliary gamma ball for the seed

The zero-width cap in M.3 exists on the whole product
\(\|\gamma\|_{A^0}<r_\gamma\), \(\|f_B\|_{\dot A^2_0}<2^{-60}\).
Every occurrence of gamma in RG.3--RG.26 is through this map, its uniform value bound \(r_f=10^{-8}\), and the half-ball derivative in the \(f_B\) input. Therefore the same proof is valid on the auxiliary complex-even gamma ball
\(\|\gamma/r_\gamma\|_{A^0}<1/64\).
Both signed coefficients and all mean outputs remain present.

The incoming width is \(7L/16\) only when \(f_B=0\). The mixed construction instead has B-end width \(s_\beta\), cap-end width zero, and slope \(s_\beta/L<1/32\). Thus this enlargement in gamma makes no new complex-angle evaluation of an unknown datum.

The incoming contraction, the 94 bounded label operations, and the already constructed holomorphic joint phase map prove Banach holomorphy in gamma. With
\(R_a=2^{-55000000}\), their original uniform bounds give
$$
 \|a_{94}(\gamma)\|_{\ell^1_{66624}}<R_a/4,\qquad
 \|D_\gamma a_{94}\|_{A^0\to\ell^1_{66624}}
          <2^8R_a/r_\gamma
 \quad(\|\gamma/r_\gamma\|_{A^0}\le1/128).
 \tag{C.3}
$$
For the derivative, a complex direction circle of radius \(r_\gamma/256\) stays inside the auxiliary ball; its direct Cauchy bound is already smaller than the displayed one.

The label has no zero Fourier input. Hence the actual minimum physical frequency is 4, and
$$
 \|a\|_{224}\le e^{-4(66624-224)}\|a\|_{66624}
                         <2^{-332000}\|a\|_{66624}.
 \tag{C.4}
$$
This bound is applied to labels and their genuine parameter derivatives, not to arbitrary physical height traces.

## 3. The second parameter in its actual layer weight

For an internal negative component \(i=(j,k)\ne o\), put
$$
 C_j^{\rm P}=C_j+\mathbf1_{j\ge130}C_{j-1},\qquad
 W_i=(j+5)^3\delta_j^{-5}C_j^{\rm P},\qquad W_o=1,
$$
$$
 \|\mathfrak q\|_{\mathcal P_2}
                     =\sup_{i\in\mathcal I_+}|\mathfrak q_i|/W_i .
 \tag{C.5}
$$
The six-neighbor quantity \(C_j^\#\) will be used when these component weights are collected on an actual cell. It is not substituted for the two-neighbor quantity in the definition without accounting for that collection.

Nph.9 and Nph.11 retain the individual, rather than merely summed, bounds. The radial normalized derivative
\(|\partial_{\gamma_1}\beta_i|/\sqrt{\mathcal B_i}<4\)
is the same local bump integral used in Nph section 2 and in the exterior first-phase proof Fph.36--Fph.37. Combining it with the two displayed individual bounds gives, on the original label ball \(A_*=2^{-262148}\),
$$
 |E_i(a,\mathfrak q)|\le2^{148}W_i\mathcal X\quad(i\ne o),
 \qquad |E_o(a,\mathfrak q)|\le2^{2048}\mathcal X,
 \quad \mathcal X=16\|a\|_{224}.
 \tag{C.6}
$$
Here \(\sqrt{\mathcal B_i}>1\); all real and complex subdomains are the original ones in Jph.7--Jph.14.

The exact scalar inverses have \(\varphi_i(0)=0\) and
\(|\varphi_i'|<2^{10}\). At the actual full fixed point, Jph.13 consequently yields
$$
                  \|\mathfrak q^*(a)\|_{\mathcal P_2}
                              \le2^{4096}\|a\|_{224}.
 \tag{C.7}
$$
This estimate includes the exterior component and every cross-parameter response. It is not obtained by treating those responses as diagonal.

Coordinate holomorphy and the uniform weighted estimate imply holomorphy into \(\mathcal P_2\): take Cauchy coefficients in every coordinate, use (C.7) before taking the supremum, and sum the uniform remainder in the weighted norm. Jph.18 gives \(\mathfrak q^*(0)=D_a\mathfrak q^*(0)=0\) in this same space. To avoid an optimal polarization constant, use two independent direction circles of radius \(A_*/4\), centered at a point of norm at most \(A_*/8\). The uniform bound \(2^{4096}A_*\) gives
\(\|D^2\mathfrak q^*\|\le16\,2^{4096}/A_*\).
Integrating from 0, and widening the constant, gives
$$
 \|D_a\mathfrak q^*(a)\|_{\ell^1_{224}\to\mathcal P_2}
                         \le2^{266256}\|a\|_{224}.
 \tag{C.8}
$$
All actual seed labels lie strictly inside the stated \(A_*/8\) ball.

Combining (C.3)--(C.4) and (C.8), including both factors of the small seed label, proves
$$
 \|\mathfrak q(\gamma)\|_{\mathcal P_2}<2^{-110000000},
 \qquad
 \|D_\gamma\mathfrak q(\gamma)\|_{A^0\to\mathcal P_2}
                              <2^{-110000000}/r_\gamma .
 \tag{C.9}
$$
For example the derivative exponent before this widening is
\(266256-55332002-55331992=-110397738\).
This is a statement about the seed's second design parameter. It is not a derivative assertion about the eventual Nash limit.

## 4. Comparing the true reference graph spaces

Write \(w_0^{\mathfrak q}\) for the radial reference with second parameter
\(\bar\Gamma_2+\mathfrak q\) and the exact radial first compensation
\(\chi_i(\mathfrak q_i)\), with \(|\chi_i'|<2\).
For two such references define
$$
 \psi_{\rm ref}
 =\log\frac{w_0^{\mathfrak q'}}{w_0^{\mathfrak q}}
 =\sum_i\psi_{1,i}\{\chi_i(\mathfrak q'_i)-\chi_i(\mathfrak q_i)\}
                 +\sum_i\psi_{2,i}(\mathfrak q'_i-\mathfrak q_i).
 \tag{C.10}
$$
These are the actual compact metric bumps. They do not alter the root germs, the fixed stop, the B section or the B scale \(s_B=a_Bw_B\).

Let \(p_0,k_0,U_0,V_0\) and \(\mathcal L_0^{\mathfrak q}\) be E.2--E.4, all evaluated on one fixed physical nonmean height \(u\). The new four states are exactly \(e^{-\psi_{\rm ref}}\) times the old ones,
\(Q_0'=Q_0-(\psi_{\rm ref})_t\), and \(c_0'=c_0e^{2\psi_{\rm ref}}\).
Thus the reference source identity is
$$
 \mathcal L_0^{\mathfrak q'}u
 =e^{\psi_{\rm ref}}\mathcal L_0^{\mathfrak q}u
   +c_0e^{\psi_{\rm ref}}(\psi_{\rm ref})_t(k_0+U_0).
 \tag{C.11}
$$
On the added finite connector the bumps vanish, so its ordinary reference source is unchanged. No internal \(c_0\) is inserted into that finite source unit.

Here is the layer bound needed for (C.11). Set
\(\tau=\|\mathfrak q'-\mathfrak q\|_{\mathcal P_2}\).
Let \(g_j\) be the sum of the absolute values of the actual first- and second-bump coefficients whose supports meet \(I_j\). In particular \(g_j\ge\sup_{I_j}|\psi_{\rm ref}|\). Collecting the original supports as in Qmet.24c/G.19, and allowing the adjacent \(\delta,J\) ratios, gives
$$
 g_j\le2^{32}J_j^3\delta_j^{-5}C_j^\#\tau .
$$
$$
 \max_{a\le4}\ell_j^a|\partial_t^a\psi_{\rm ref}|\le2^{64}g_j,
 \qquad
 \max_{a\le3}\ell_j^a|\partial_t^{a+1}\psi_{\rm ref}|
                                    \le2^{64}\delta_j^{-3/2}g_j .
 \tag{C.12}
$$
For clarity, Qmet.22 uses \(64z^3(1-z)^3\), with \(z_x=8\) or \(32\), and \(x_t=\sqrt{12}/\eta_j<2^5\delta_j^{-3/2}\). Through order 4 the sum of absolute derivative coefficients is at most \(50688<2^{16}\). Thus each ordinary derivative is bounded by \(2^{16}(2^{10}\delta_j^{-3/2})^a\) times its original coefficient, and \(\ell_j=2^{-64}J_j^{-2}\delta_j^4\) proves both estimates in (C.12). These are broken jets; no unproved global fourth derivative or deletion of a third-jet jump is involved. The exterior \(o\) is still the separate shallow component in cell129.

Use the exact G.20 inequality
\(c_0(C_j^\#)^2/(\zeta_j\delta_j^{16})
 \le2^{1168}h_j^{-10}(\zeta_j/\mu_j)\delta_j^{-22}\).
The additional source in (C.11) is therefore controlled by
$$
 J_j^3h_j^{-10}\frac{\zeta_j}{\mu_j}\delta_j^{-57/2}.
 \tag{C.13}
$$
The original [controlled-profile formulas C.2 and C.24](R119-supplement-controlled-profile-full-label-and-raw-ports.md), equivalently Mhol.1 and [U.2](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md), give the following three ranges. In particular \(h_j=9/100\) through 4096 and \(h_j=8\delta_j^{1/256}\) thereafter, so the latter contributes exactly \(2^{-30}\delta_j^{-10/256}\). The profile in (C.13) is
\[
 J^3h^{-10}\delta^{-99/4},\qquad
 2^{-30}J^3\delta_{4096}^{-3/2}\delta^{-93/4-10/256},\qquad
 2^{-30}J^3\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
                                     \delta^{98-10/256}.
\]
For the first range \(\log_2\delta^{-1}<4100\), \(J^3<2^{39}\) and
\(h^{-10}<2^{40}\), giving fewer than 102000 bits. For the second,
\(\log_2\delta^{-1}<8196\), \(J^3<2^{42}\), giving fewer than 198000 bits.
The third agrees with the second at its profile junction and then decreases:
its positive exponent exceeds 97 and dominates the step ratio of \(J^3\).
The whole supremum is, conservatively, less than \(2^{262144}\).
The shallow \(o\) term uses G's actual finite-cell calculation; its added
\(J^3\delta^{-5}\) factor is below 1024 bits there and fits the same bound.

Three ordinary source derivatives are distributed by the original scaled Leibniz rule. The needed scalar coefficient bounds are exactly Cjet.4--Cjet.7/E.18, with at most the first four broken bump derivatives. Including the finite sums, the \(2^{32+64+1168}\) in (C.12)--(C.13), the reference-state multipliers and the finite-cell exception, all costs are below
$$
                         K_{\rm ref}=2^{1048576}.
$$
For instance the radial scalar products can be widened to 131200 bits;
\(131200+32+64+1168+262144<524288\), leaving a further full margin inside the displayed constant. Angular order causes no additional factor because every reference multiplier is radial.

Consequently, for \(20\le s\le8192\),
$$
 \left|\|u\|_{E_s(\mathfrak q')}-\|u\|_{E_s(\mathfrak q)}\right|
       \le K_{\rm ref}\tau\|u\|_{E_s(\mathfrak q)} .
 \tag{C.14}
$$
The same conclusion holds for \(E_s^+\), since its added B-height trace and \(s_B\) are unchanged. The norms are mutually equivalent by a factor less than 2 for all seed references in (C.9). They identify the same physical nonmean height, the same original trace constraints, and the same broken source domain.

For the rest of the proof choose \(\mathfrak q=0\) as a common norm reference. This choice does not replace any coefficient in the actual PDE or in its inverse.

## 5. The seed and the low principal construction are continuous in these coordinates

RG's labels are holomorphic in the auxiliary zero-width gamma ball. The original local tail chart and its true joint design parameters are holomorphic in that label. The B-collar lift uses only the same five one-sided jets, complete long endpoint functions and fixed Hermite functions. Hence it is continuous in the original label norm. The uniform Gseed.26 state bound, on its strictly larger label ball, gives continuity into the weighted state norm by Banach Cauchy. This step uses the full label norm; pointwise convergence on each layer alone would not imply continuity of the weighted state supremum.

To read this statement in the graph rather than just pointwise, retain Gseed.26--Gseed.28 and the complete reference identity (C.11). On each fixed cell the derivative formulas are continuous. The bounds entering its narrow source norm contain the same two state factors as E.19, or the profile (C.13) for a reference change. Their deep tails tend to zero uniformly. Finite-cell continuity followed by this uniform tail bound gives convergence in the full weighted supremum. There is no interchange of a Fourier sum and a layer supremum.

It follows that the seed, and its exact straightened coordinate
$$
 w_0(\gamma)=u_{\rm seed}(\gamma)
              -L_\partial q_\gamma(f_B(u_{\rm seed}(\gamma))),
 \tag{C.15}
$$
are continuous in the common \(E_{1856}^+\) norm. Their high
\(E_{8192}^+\) bounds are locally uniform and in fact uniformly controlled by S.31/S.44 on (C.1).

We also need the joint low continuity of the first-principal construction when \(\mathfrak q\) changes. P.3--P.4 use the actual radial curves and L.10 uses the actual real ODE; their coefficients vary continuously under (C.10)--(C.12). The low \(H^{16}\) return estimates L.12 and the counterterm construction L.9 are uniform on these radial boxes. The same contraction L.14 therefore gives continuous first parameters, and its differential on \(\mathcal D_{20}\) directions varies continuously on every fixed finite group of cells. This uses the genuine \(C^1\) statement L.15, not an alleged value map on a \(\mathcal D_8\) open ball.

For the parameter sequence itself, L.12/L.14 give a tail majorant proportional to \(E_i^\ell/\kappa_i\). The original \(\kappa_i^{-1}<2^{28}J_i\delta_i^{-1}\) and the actual deep \(C_i^{\rm P}\) profile make this majorant tend to zero. Thus finite-component continuity and the uniform tail also imply continuity in the full weighted parameter norm. The analogous derivative statement on fixed finite groups follows from the same real ODE and L.9. For source estimates over all cells, use the pointwise L.16--L.17 weights before taking the supremum. After the physical metric source is formed, G.20--G.21 or (C.13) gives a uniform deep tail tending to zero. This extends the required continuity to the complete source norm even when a bare parameter norm alone would not contain that layer decay.

## 6. A complete linear proxy on one fixed space

Let \(\xi=(\gamma,\mathfrak q,w)\) denote a real background at one finite step, let
\(u=\mathcal U_\gamma(w)\), and let
\(\mathcal T_\xi=D\mathcal U_\gamma(w)\).
The latter is S's exact nilpotent change of tangent coordinates. Its inverse is the exact
\(I-L_\partial Dq_\gamma(f_B)F_B\).

For a direction \(v\) with the fixed linear B condition \(B_0v=0\), first take the physical nonmean direction \(\mathcal T_\xi v\). Reconstruct its fixed-metric mean by the full linearized Mhol holonomy equation, using one fixed height gauge. Call this full height
\(H_\xi(v)\). The separate metric lift is still the actual \(H_p\) of A.19--A.23. In particular \(H_\xi(v)\) is not obtained by declaring its ordinary mean to be zero.

Define the projected complete proxy
$$
 \mathscr P_\xi v
 =P_\perp\left\{
      c_{\rm ph}\mathcal J_u H_\xi(v)
             -\mathcal B_{p,u}(\mathcal T_\xi v)\right\}.
 \tag{C.16}
$$
Use the finite ordinary source unit on the finite connector, as in A.6. Its complete mean identity is I.32/Mhol: (Cjet.25 is the same exact charge identity) the reconstructed tangent has zero body charge, and the full expression before \(P_\perp\) is the corresponding \(\Pi_{A_u}\) lift. No independent charged datum is set to zero by a projection. Here those data are fixed to the same compatible body channel as in S.

A.6, G.26 and S.19--S.24 show that \(\mathscr P_\xi\) has the unique complete proxy inverse \(\widehat{\mathcal R}_\xi\) used in S. Equivalently,
$$
 \mathscr P_\xi v
       =D\mathcal F_\gamma(w)[v]
                     +P_\perp\mathcal E_u[H_\xi(v)],
 \qquad
 \mathscr P_\xi\widehat{\mathcal R}_\xi g=g .
 \tag{C.17}
$$
The residual-sensitive \(\mathcal E\) term is not discarded at finite steps. The inverse has uniqueness in the original weak/strong solution class, not just for finite Fourier vectors. This follows from the complete N inverse and the already paid first-parameter Schur.

Writing this operator in fixed nonmean coordinates is essential. Subtracting two full heights with different holonomy linearizations and silently dropping their mean difference would not give the following comparison.

## 7. Continuity of this inverse when applied to the actual high-regularity iterates

Suppose \(\xi_n\to\xi\) in gamma \(H^{8193}\), in \(\mathcal P_2\), and in the common \(E_{1856}^+\) background norm. Assume the finite-step high background norms are bounded. Then
$$
 \|\mathscr P_{\xi_n}-\mathscr P_\xi:
           E_{1856,0}^+\longrightarrow Z_{1794}^{[3]}\|
                                      \longrightarrow0 .
 \tag{C.18}
$$
Here is the derivative and unit accounting for this statement.

The internal rational coefficients and the complete mean projection require at most 1794+8 angular orders, by Cjet.9a, Jr and A.18. The graph-linear part is compared by (C.11), with its original \(\zeta\delta^{16}\) unit. The first-parameter differential is treated by L.15 on \(\mathcal D_{20}\) directions and its pointwise physical weights; the uniform deep-source tail is exactly the one described in section 5. The \(\mathcal E\) coefficients use \(N,N_\theta\) and three radial source jets; A.17 uses at most 1795 source orders and background 1802, all below 1856.

At B, the nilpotent factors and the true row use the actual \(D_fq_\gamma(f)\). M's mixed kernels and O's finite tame maps give continuity of these operators and of their first differentials on the low zero-width balls. One may use outer index 1808 throughout this comparison: its state requirement 1840 and physical-height requirement 1842 fit strictly below the actual state/trace input. These are well below M's 8160 and O's 8144 windows. No unknown gamma is composed at a complex angle. The fixed affine value \(q_\gamma(0)\) and the nonradial linear part vary continuously by these same maps; neither is removed.

The source/mean multipliers have positive low denominators. Their uniform low series bounds permit termwise continuity with a summable majorant. At infinitely many radial cells, first restrict to a finite prefix, use the preceding continuous coefficient formulas, then send the prefix to infinity using E.19, G.21 and (C.13). All seam values and the ordinary one-sided jets use the original interfaces. These arguments give the operator norm in (C.18), not a claim that a high inverse is continuous without loss.

For \(g_n\to g\) in \(Z_{1794}^{[3]}\), put
\(h_n=\widehat{\mathcal R}_{\xi_n}g_n\), \(h=\widehat{\mathcal R}_{\xi}g\).
If these particular outputs have uniformly bounded \(E_{6396}^+\) norms, their exact difference equation is
$$
 \mathscr P_\xi(h_n-h)
   =g_n-g+(\mathscr P_\xi-\mathscr P_{\xi_n})h_n .
 \tag{C.19}
$$
Both directions satisfy the same \(B_0=0\) condition. The full holonomy means in this formula are reconstructed as in (C.16). Applying the actual low estimate S.24, then (C.18), gives
\(\|h_n-h\|_{E_{20}^+}\to0\).
The reference comparison only adds its factor less than 2.

E.9, including the same added terminal trace, now gives
$$
 \|h_n-h\|_{E_{1856}^+}
 \le
 \|h_n-h\|_{E_{20}^+}^{\,1-\vartheta}
 \|h_n-h\|_{E_{6396}^+}^{\,\vartheta}\longrightarrow0,
 \qquad
 \vartheta=\frac{1856-20}{6396-20}.
 \tag{C.20}
$$
The extra high norm is an already proved bound on these actual corrections. It is not an extra hypothesis on an arbitrary rough source, nor an inversion theorem between two equal-regularity Banach spaces.

## 8. Every finite Nash step is continuous

Use the deterministic iteration S.34 with its one common sequence
\(T_n=2^{1500000(5/4)^n}\). The initial step is continuous by section 5.

Inductively suppose \(w_n\) is continuous in \(E_{1856}^+\). For this fixed \(n\), the Fourier projection \(S_{T_n}\) is bounded into every higher graph norm used in the finite step. Thus its background has the required continuity and locally uniform high bounds. The actual map \(\mathcal U_\gamma\), the complete residual, and the source \(S_{T_n}\mathcal F_\gamma(w_n)\) are continuous in the low source norm needed in (C.19). Their finite high bounds are the very bounds S.35--S.37, uniform on (C.1).

The output correction is continuous by (C.19)--(C.20). Therefore \(w_{n+1}\) is continuous as well. This proves all finite steps without differentiating any high inverse.

For clarity, the constants are not chosen afresh with gamma: S.44 gives the same \(K_\partial=2^{6291456}\), the same bound \(\overline B_\gamma<2^{2097152}\), and hence one upper \(C_+\) and one \(T_0\) for the entire domain. Their large numerical sizes do not affect the finite-step continuity argument.

## 9. The actual selected limit is continuous

The S.37 tail estimate is uniform in gamma:
$$
 \sup_{\gamma\in\mathcal D_\gamma}
 \|w_\infty(\gamma)-w_N(\gamma)\|_{E_{1856}^+}
 \le4C_+\sum_{n\ge N}T_n^{-1266}\longrightarrow0 .
 \tag{C.21}
$$
The harmless factor 4 includes conversion to the common reference. It follows from finite-step continuity and uniform convergence that
$$
 \gamma\longmapsto w_\infty(\gamma),\qquad
 \gamma\longmapsto u_\infty(\gamma)=
                   \mathcal U_\gamma(w_\infty(\gamma))
 \quad\text{are continuous into common }E_{1856}^+ .
 \tag{C.22}
$$
This conclusion does not use uniqueness of every possible nonlinear body solution. It concerns the uniquely specified seed, principal choices and successive proxy solves in this actual iteration.

For every gamma, S.38 and S.46 still give the exact body equation and the exact nonlinear far condition. The first design parameter and the full holonomy small root depend continuously on (C.22) and (C.9). The true mean-height integral is continuous as well: on a finite prefix this is the ordinary integral of continuous quantities, while S.40--S.41/Mhol.28--Mhol.30 provide one uniform summable deep bound. The one height constant is selected at the same B section as before. No additional end frame or world anchor is introduced.

The actual cap/long outputs are then continuous by M with their original units. This includes both curvature means, coordinate phase, the long height span, and the inner B/C-mean readouts. This conclusion does not screen any of those outputs.

## 10. A small and compact true far-height value map

Let
$$
                         \mathcal T_{\rm far}(\gamma)
                                  =f_B(u_\infty(\gamma)).
$$
The rough seed has the actual wide B trace
\(\|f_B(u_{\rm seed})\|_{H^{8195}}<2^{-54866000}\), by S.31/RG.28.
Moreover \(f_B(\mathcal U_\gamma w)=f_B(w)\) exactly. Hence S.37, with the actual \(2^{440}\) trace weight, gives
$$
 \|\mathcal T_{\rm far}(\gamma)-f_B(u_{\rm seed}(\gamma))\|_{H^{1859}}
 \le2^{-440}\,2C_+T_0^{-1266}<2^{-1700000440}.
$$
In particular
$$
 \sup_{\gamma\in\mathcal D_\gamma}
         \|\mathcal T_{\rm far}(\gamma)\|_{H^{1859}}
                                    <2^{-54865000}.
 \tag{C.23}
$$
Together with (C.22), this proves continuity into \(H^{1859}\) and relative compactness of its image in \(H^2\). The compactness is the ordinary Fourier tail estimate on one fixed circle, not a compactness assertion for the full uniform-layer state space.

Thus an eventual core coupling may consume a continuous, compact, uniformly small actual far-height map. This alone is not a Schauder self-map on the physical gamma domain. A true core solution map, preservation of the gamma \(H^{8193}\) gate, the real inner B/C-mean matching and the requisite bounded/closed set would still have to be supplied. They are not consequences of (C.23).

## 11. The real parameter equations and the fixed-metric column

The selected objects satisfy precisely
$$
 \begin{gathered}
 \mathfrak q=\mathfrak q^*(a_{94}(\gamma)),\qquad
 \Gamma_1=\mathcal G_1(u_\infty,\mathfrak q),\\
 \mathfrak F_{\mathfrak q}(u_\infty)=0,\qquad
 k_B(u_\infty)=P_\perp\mathcal K
             \bigl(f_B(u_\infty),\Phi_\gamma(f_B(u_\infty))\bigr),
 \end{gathered}
 \tag{C.24}
$$
with the full mean slope from the same holonomy root and with the one B-section mean-height normalization. The exact scalar-phase equation defining \(\mathfrak q^*\) belongs to the seed \(a_{94}\). This construction does not assert that a second scalar phase is re-solved after every nonlinear Nash update.

There is an exact finite-difference identity for the far row. Join two input pairs \((\gamma,f_B)\) by their straight segment in the actual zero-width domain and integrate the full two-input derivative of \(\mathcal K(f,\Phi_\gamma(f))\). Its derivative contains both
\(D_f\mathcal K+D_g\mathcal K D_f\Phi\) and
\(D_g\mathcal K D_\gamma\Phi\), in that order. All mean outputs are differentiated as their complete small-root/height functions. The body comparison also contains the true metric change (C.10); it is not a fixed-metric difference equation.

If differentiability of this selected limit is subsequently established in a specified source/output scale, its second-parameter derivative is already the actual quantity (C.9), and
$$
 \dot\Gamma_1
       =D_u\mathcal G_1\,\dot u
                    +D_{\mathfrak q}\mathcal G_1\,\dot{\mathfrak q}.
 \tag{C.25}
$$
The corresponding physical metric variation is
\(\dot\psi=\sum\psi_1\dot\Gamma_1+\sum\psi_2\dot{\mathfrak q}\);
its full mean/height lift is \(H_p\), not zero.

For any such independent metric direction the exact G.16--G.17 source, with its correct normalization, is
$$
 -\Pi_A\delta_pN
 =\Pi_A\{c_{\rm ph}e_{\psi,\rm rem}
       +c_{\rm ph}(F_K-2Q)\ell-\psi N\},
 \qquad
 \ell=\psi\kappa+\delta\kappa_p .
 \tag{C.26}
$$
Its true height satisfies
\((H_p)_t=aw\{\psi(1+\kappa)+\delta\kappa_p\}\).
At an exact body solution \(N=0\), the last term in (C.26) vanishes, but the other metric terms and the height integral generally do not. The first-parameter feedback is the one already included by G/N. The extra second-parameter direction in (C.25) is an additional actual column, even though its seed weight is extremely small.

By contrast, [R's actual inner-cap/tail feedback](R133-supplement-actual-inner-cap-complete-tail-height-feedback-and-97-interface.md) holds metric fixed. Its outward long source is
\(b_\gamma=-\mu_Ls_BD_g\mathcal K D_\gamma\Phi\,\dot\gamma\);
the short-side data are
\(\beta_\gamma=-P_{\mu_T}(r_\mu b_\gamma)\) and
\(c_{B,\gamma}=+\langle r_\mu b_\gamma\rangle/\langle\mu_T\rangle\).
The \(s_B\) cancellation and its tiny \(H^0\to H^2\) value belong to that same fixed-metric compatible proxy. They cannot be identified with the whole response of (C.24) by deleting (C.25)--(C.26), nor by differentiating the additive seed closeness estimate S.39.

The present result supplies a continuous exact selection and its actual small far-height values. It does not claim a \(C^1\) Banach inverse, an \(H^0\)-Lipschitz selected family, or the still missing core matching. For a single fully matched surface the intrinsic choices are made once and frozen; the separate fixed-metric geometric phase construction then has its previously proved meaning.
