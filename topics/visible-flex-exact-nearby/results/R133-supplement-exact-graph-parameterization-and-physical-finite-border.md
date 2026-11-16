# R133 supplement: exact graph parameterization and the physical finite border

2026-11-16, phase_inverse.

**Proved analytic reduction on the WFI graph domain, with the genuine physical finite columns and parameter rows left explicit.** The complete normalized homogeneous waist row can be parameterized by the reference graph inverse on one $L^2$ target space. The reference extension has the exact form $Id+K$, with a complete one-third-derivative high-tail estimate. When actual additional finite input columns are supplied, their difference from the reference columns is retained as a genuine finite factor. The complete high/finite/metric-parameter elimination then has the BF/RNS block form in its correct order.

The reference extension is an analysis device. It does not create physical low inputs, erase the 96 constraints of the original homogeneous high column, or supply a physical finite inverse. No new bound, cutoff or determinant is numerically evaluated, and no old arithmetic is repeated.

## WGB1. The fixed graph and the three distinct projections

Use the same selected parameter, real reflection phases, physical frequencies and complete trace qualification as WFI. Write
$$
 X=X_b^{-1},\qquad Y=Y_a^0,\qquad
 \mathcal D=\{x\in X_b^{-1}:\overline Mx\in Y\},
 \qquad \overline G=\overline M^{-1}:Y\longrightarrow\mathcal D .
 \tag{WGB.1}
$$
Here $\overline M=M_\nu P_{97}+L_{\rm low}Q_{97}$ is the exact WFI reference: $M_\nu=\Pi_a^+(Id+\nu_i I)$ on the high modes, and $L_{\rm low}$ is the explicitly chosen real reference on modes $1,\ldots,96$. No low gap for $M_\nu$ is asserted. In this note $\nu_i$ is the fixed first-coefficient mean, not the varying physical metric parameter.

Keep the actual input projector and graph subspace
$$
 \widetilde P=\widetilde P_{97},\qquad
 \widetilde Q=Id-\widetilde P,\qquad
 \mathcal D_{\rm true}=\widetilde P\mathcal D.
 \tag{WGB.2}
$$
The full normalized physical row is
$$
 \mathcal L=M_\nu+\mathcal E:
          \mathcal D_{\rm true}\longrightarrow Y,\qquad
 \mathcal E:\widetilde X_{-4/3}\to Y
                 \text{ bounded and complete}.
 \tag{WGB.3}
$$
All complete terms in WBP.23 remain in $\mathcal E$, including the genuine density mean rank and the full WPL physical state contribution.

The symbols have different roles:

| Projection | Exact role |
|---|---|
| $P_{97},Q_{97}$ | Ordinary model Fourier high and low parts; $Q_{97}$ has 96 reflected real modes |
| $\widetilde P,\widetilde Q$ | The actual input projection and its transported complement from WBN/WBP |
| $P_J,Q_J$ below | A new ordinary Fourier high/low split of the target $Y$, with $J\ge97$ |

Neither $\widetilde P=P_{97}$ nor $\widetilde P=P_J$ is assumed. A physical mean or an independent radial source is not inserted into one of these scalar circle projections by notation.

As proved in WFI, $\mathcal D$ is complete, $\overline M:\mathcal D\to Y$ is an isomorphism, $L^2\cap X_b^0\subset\mathcal D$, and $\widetilde P,\widetilde Q$ are bounded on this graph. The actual high domain has codimension 96. The full-circle principal inverse of $T_i$ is not used as an inverse of this reflected row.

## WGB2. The known coordinate columns and rows

Let
$$
 \mathcal U=\mathcal A^{-1}\mathcal C D_+,
 \qquad \mathcal C=\mathcal W\mathcal S,
$$
and let $E_{96}:\mathbb R^{96}\to\operatorname{Fix}(R_*)\cap L^2_0$ insert the normalized real root-even modes $1,\ldots,96$. Its complexification has the same dimension over the complex field. Define
$$
 C_Q=\mathcal U E_{96},\qquad
 V_Q=E_{96}^*\mathcal U^{-1}.
 \tag{WGB.4}
$$
The original fixed phase $D_+$ and all source factors have their WFI order. Then
$$
 \widetilde Q=C_QV_Q,\qquad
 V_QC_Q=Id_{\mathbb R^{96}},\qquad
 \widetilde PC_Q=0,\qquad V_Q\widetilde P=0 .
 \tag{WGB.5}
$$
These are actual coordinate columns and rows of the transported projection. They are not physical Poisson columns.

WIT/WBN's two-window bounds, with interpolation at $-1$, give
$$
 C_Q:\mathbb R^{96}\to X_b^0\subset\mathcal D,\qquad
 V_Q:X_b^{-4/3}\to\mathbb R^{96}.
 \tag{WGB.6}
$$
For clarity, let $K_{\mathcal U,s}$ and $K_{\mathcal U^{-1},s}$ be complete same-map bounds in the stated window. One valid joint bound is
$$
 \|C_Q\|_{\mathbb R^{96}\to L^2}\le K_{\mathcal U,0},\qquad
 \|V_Q\|_{H^{-4/3}\to\ell^2}
      \le K_{\mathcal U^{-1},-4/3}\Lambda_{96}^{4/3}.
 \tag{WGB.7}
$$
There is no extra $\sqrt{96}$: $E_{96}$ is an isometry and the finite negative-to-zero Fourier embedding has the displayed largest weight. The individual rows are interpreted distributionally through the smooth root Fourier functions.

Put
$$
 C_\nu=1+\frac{|\nu_i|}{4}.
$$
The bounded model and the unit low reference give $\|\overline M\|_{L^2\to L^2}\le C_\nu$. Thus
$$
 \|C_Q\|_{\ell^2\to\mathcal D}
       \le(1+C_\nu)K_{\mathcal U,0},\qquad
 \|\overline M C_Q\|_{\ell^2\to Y}
       \le C_\nu K_{\mathcal U,0}.
 \tag{WGB.8}
$$
These are symbolic bounds for known reference objects. The columns $\overline M C_Q$ will appear only as reference columns in an exact subtraction of operators, never as substitutes for unknown physical columns.

The complete coordinate bound
$$
 K_P\ge\|\widetilde P:H^{-4/3}_0\to H^{-4/3}_0\|
 \tag{WGB.9}
$$
is likewise available as an ordered positive product of the already qualified coordinate norms. For example $K_{\mathcal U,-4/3}K_{\mathcal U^{-1},-4/3}$ is valid. This does not assert that $\widetilde P$ is orthogonal.

## WGB3. Exact reference parameterization and a complete high-tail bound

Define an extension only for analysis:
$$
 \mathcal L_{\rm ext}
       =\mathcal L\widetilde P+\overline M\widetilde Q:
                   \mathcal D\longrightarrow Y .
 \tag{WGB.10}
$$
Every occurrence of $\mathcal L$ acts on its true domain. The second term is the declared reference on the complementary 96 coordinates. Outside $\mathcal D_{\rm true}$, this extension is not called a physical trace.

Equations (WGB.2)--(WGB.3) give the exact identity
$$
 \mathcal L_{\rm ext}
       =\overline M+\mathcal F,\qquad
 \mathcal F=
       \big[(M_\nu-\overline M)+\mathcal E\big]\widetilde P .
 \tag{WGB.11}
$$
The right side has a well-defined bounded extension
$$
 \mathcal F:X_b^{-4/3}\longrightarrow Y .
 \tag{WGB.12}
$$
For its second term the projection is applied first, so $\mathcal E$ is evaluated only in $\widetilde X_{-4/3}$. No arbitrary extension of $\mathcal E$ to an unqualified circle input has been supplied.

If $C_E$ is a complete bound for $\mathcal E$, then one safe whole positive bound is
$$
 C_{\rm low}=(2+|\nu_i|/4)\Lambda_{96}^{4/3},\qquad
 C_F=(C_{\rm low}+C_E)K_P,\qquad
 \|\mathcal F\|_{H^{-4/3}\to L^2}\le C_F .
 \tag{WGB.13}
$$
Indeed $M_\nu-\overline M=(M_\nu-L_{\rm low})Q_{97}$. The separate $L^2$ norms of the model and low reference are bounded by $C_\nu$ and one; the ordinary low negative-input embedding supplies $\Lambda_{96}^{4/3}$. No low trigonometric multiplier is evaluated and no difference of upper bounds is taken.

Now use the exact graph variable
$$
 u=\overline Mx,\qquad x=\overline Gu .
$$
Then
$$
 \boxed{\quad
 \mathcal L_{\rm ext}\overline G=Id_Y+K,\qquad
 K=\mathcal F\overline G
   =(\mathcal L-\overline M)\widetilde P\,\overline G .
 \quad}
 \tag{WGB.14}
$$
The last expression is evaluated only after $\widetilde P$ has placed the input in the true graph. The operator $K:Y\to Y$ is compact by WFI's graph compactness, or directly from (WGB.12) and the compact embedding $H^{-1}\hookrightarrow H^{-4/3}$.

For an ordinary target cutoff $J\ge97$, $\overline G P_J$ uses only the certified high multiplier. It preserves the original paired $\pm j$ frequency blocks. WCS first gives its $L^2\to H^{-1}$ bound $2K_{\rm CY}$, and only then the high embedding gives
$$
 \|\overline G P_J:Y\to X_b^{-4/3}\|
       \le(2K_{\rm CY})\Lambda_J^{-1/3}.
 \tag{WGB.15}
$$
The transported projection is already contained on the right side of $\mathcal F$. It is not commuted through $\overline G$ or the cutoff.

Consequently
$$
 \|KP_J:Y\to Y\|
      \le\chi_J,\qquad
 \chi_J=(2K_{\rm CY})C_F\Lambda_J^{-1/3}.
 \tag{WGB.16}
$$
This is the correct tail power after the one-derivative-loss model inverse. BF's earlier $\Lambda_J^{-4/3}$ principal-inverse gate is not the gate of this realization.

If a complete $C_F$ and an actual $J$ have established $\chi_J<1$, then
$$
 H_J=Id_{P_JY}+P_JKP_J
 \quad\hbox{has inverse}\quad
 \|H_J^{-1}\|_{Y\to Y}\le(1-\chi_J)^{-1}.
 \tag{WGB.17}
$$
All finite quantities in (WGB.13) imply abstractly that some finite sufficiently large $J$ satisfies the inequality. This is not an evaluated cutoff, a feasible finite matrix, or a numerical gate verdict. The scalar combination in (WGB.16) is a new target if a later consumer is authorized.

## WGB4. The original high column retains its 96 constraints

Set
$$
 \Theta=V_Q\overline G:Y\longrightarrow\mathbb R^{96}.
 \tag{WGB.18}
$$
It is bounded, and the graph change gives
$$
 x\in\mathcal D_{\rm true}
       \quad\Longleftrightarrow\quad \Theta u=0.
$$
Thus the exact original homogeneous high equation is
$$
 \boxed{\quad
 (Id+K)u=f,\qquad \Theta u=0 .
 \quad}
 \tag{WGB.19}
$$
The reference extension alone, with its constraints omitted, is a different problem. A prescribed physical right side and all independent data used to form it remain inside $f$ in the already chosen normalized target units.

For example the same known norms give
$$
 \|\Theta\|
   \le K_{\mathcal U^{-1},-4/3}
        \Lambda_{96}^{4/3}\max\{1,2K_{\rm CY}\},
$$
$$
 \|\Theta P_J\|
   \le K_{\mathcal U^{-1},-4/3}
        \Lambda_{96}^{4/3}(2K_{\rm CY})\Lambda_J^{-1/3}.
 \tag{WGB.20}
$$
The second inequality requires $J\ge97$. Neither says that a transported row vanishes on an ordinary high input.

Write $P_J=P$, $Q_J=Q$, and $u=p+q$ in this subsection. Under (WGB.17),
$$
 p=H_J^{-1}(Pf-PKQq).
 \tag{WGB.21}
$$
The complete remaining system is
$$
 \begin{aligned}
 (Id_Q+QKQ-QKPH_J^{-1}PKQ)q
       &=Qf-QKPH_J^{-1}Pf,\\
 (\Theta Q-\Theta PH_J^{-1}PKQ)q
       &=-\Theta PH_J^{-1}Pf .
 \end{aligned}
 \tag{WGB.22}
$$
The negative sign in the last right side follows from the zero constraint. That row is not the positive right side of the BF auxiliary equation $z=Vu$.

Here $q$ has $J-1$ reflected real Fourier coordinates. The second line contributes 96 actual additional equations. This is the finite form of WFI's index $-96$ ledger; it is not a square matrix whose determinant has been shown nonzero.

The alternative ordinary high-target realization still retains
$Q_{97}\mathcal Lx=Q_{97}f$ as 96 output equations. These output equations and the input constraint $\Theta u=0$ arise from different decompositions. They are not swapped or cancelled against each other without an explicit change of the complete system.

## WGB5. Substitution of genuine physical columns

Suppose, now as an additional physical input, that 96 actual finite columns in the same complete normalized target have been specified:
$$
 H_{\rm phys}:\mathbb R^{96}\longrightarrow Y.
 \tag{WGB.23}
$$
Every column must be the genuine physical column with its root, mean, waist, head and other prescribed-port convention. This is not furnished by $C_Q$ or by $L_{\rm low}$. If the actual full system has a different number or type of independent inputs, its own index ledger and equations must be used instead.

The physical augmented primitive equation is
$$
 \mathcal Lx+H_{\rm phys}c=f,\qquad
       x\in\mathcal D_{\rm true},\quad c\in\mathbb R^{96}.
 \tag{WGB.24}
$$
The coordinate isomorphism
$$
 (x,c)\longmapsto \widehat x=x+C_Qc\in\mathcal D,\qquad
 x=\widetilde P\widehat x,\quad c=V_Q\widehat x
 \tag{WGB.25}
$$
has the declared graph norm and actual ordered rows. It encodes the physical finite coefficients once; introducing them again later would double the finite input.

In the full graph coordinate, the exact operator is
$$
 \begin{aligned}
 \mathcal L_{\rm phys}^{\sharp}
    &=\mathcal L\widetilde P+H_{\rm phys}V_Q\\
    &=\mathcal L_{\rm ext}
          +(H_{\rm phys}-\overline M C_Q)V_Q .
 \end{aligned}
 \tag{WGB.26}
$$
Therefore, on the single target variable $u=\overline M\widehat x$,
$$
 \boxed{\quad
 \mathcal L_{\rm phys}^{\sharp}\overline G
      =Id+K+UV,\qquad
 U=H_{\rm phys}-\overline M C_Q,\qquad
 V=\Theta .
 \quad}
 \tag{WGB.27}
$$
This is subtraction of exact operators before any norm is taken. A later complete column bound may use the sum of norms of $H_{\rm phys}$ and $\overline M C_Q$; it may not subtract their upper bounds.

In (WGB.27), $z=Vu$ exposes the already encoded physical coordinate $c$. It is an auxiliary variable for the elimination, not a second independent copy of the 96 physical inputs. No smallness assumption is placed on $PUVP$, even when a column has high Fourier output.

If only (WGB.3) is known and the columns (WGB.23) have not been supplied, (WGB.27) is not an admitted physical square. The actual problem is still (WGB.19). Setting $H_{\rm phys}=\overline M C_Q$ just to remove $U$ would replace unknown physical columns by the reference and is not authorized.

## WGB6. Complete finite factors, physical means and the metric column

The same algebra permits additional genuine finite factors once their actual operators and spaces have been specified. For example append their columns to $U$ and their rows, after the right graph inverse, to $V$. A bounded graph row $\ell_{\mathcal D}:\mathcal D\to\mathbb R$ becomes the bounded $L^2$ target row $\ell_{\mathcal D}\overline G$. An old row already bounded on $H^{-4/3}$ qualifies this way through the explicit embedding; an unqualified physical row does not acquire boundedness from its name.

When the actual matching problem includes a finite physical space $\mathbb F$, first specify its input coordinates, output equations and their inherited norms. If a complete square realization is actually available, use the analytical reference $\overline M\oplus Id_{\mathbb F}$ on $\mathcal D\oplus\mathbb F$. Every difference between its identity finite block and the true physical equations, along with all finite/high cross maps, remains in the exact finite factor. The identity block is a reference coordinate, not a new physical equation.

The final high projection is then
$$
 P=P_J\oplus0_{\mathbb F},\qquad Q=Id-P.
 \tag{WGB.28}
$$
All separately declared finite physical means and matching coordinates are in $Q$. The scalar Fourier carrier in $Y_a^0$ has zero auxiliary mean; it is not identified with these physical means. The actual reflected relation between the two stored characteristic mean slots is retained in the choice of $\mathbb F$ and its equations, rather than counted twice.

If an unknown radial mean function, low radial head, independent second reference or other infinite port has not been prescribed or eliminated by a proved complete bounded equation, it remains in the operator system. Merely having finitely many port types does not make $Q$ finite. The reduction below is called finite only after that qualification.

At this stage assume an exact, complete same-coordinate equation
$$
 (Id+K)u+Uz+g\,\varkappa=f,\qquad
 z=Vu,\qquad
 \ell u+\omega\,\varkappa=f_\nu .
 \tag{WGB.29}
$$
Here $u$ belongs to the admitted $L^2$ target-reference space, augmented by $\mathbb F$ when appropriate. All displayed finite rows and columns are bounded there. The compact part $K$ contains the whole declared infinite remainder; the high bound in (WGB.17) must include every such term.

The symbol $\varkappa=\delta\nu_{\rm phys}$ is the actual metric-parameter variation. It is neither the fixed coefficient mean $\nu_i$, nor the normalization factor $\kappa_{\rm waist}$ in the physical primitive row. The column $g$ and the selected scalar row $\ell,\omega$ must be those of the complete regular residual and scalar equation in this same coordinate convention. Under PD's original sign convention the untransformed regular column is $-N_\nu$, and that sign remains in its true transformed column.

The coordinate maps may be frozen as fixed linear maps at the selected parameter. If a parameter-dependent chart is used instead, its derivative contributes the RNS triangular parameter column; no derivative of the true chart or action on a nonzero base residual is discarded. A root coefficient, response approximation or phase coefficient alone is not the complete $g$.

This section uses BF/RNS's exact elimination algebra. It does not transplant their principal $T_i^{-1}$, their old $\Lambda_J^{-4/3}$ gate, or their two-window inverse constants. The present square is obtained by the right graph inverse and is proved here on the $L^2$ target realization. A further window requires its own complete compatible graph and error bounds.

## WGB7. The full $(q,z,\varkappa)$ matrix in the correct order

Let $H=Id_P+PKP$ be the actual high block of (WGB.29), and assume its complete high test has been established. Put $p=Pu$, $q=Qu$. The high equation gives
$$
 p=H^{-1}\big(Pf-PKQq-PUz-Pg\,\varkappa\big).
 \tag{WGB.30}
$$
There is no extra left multiplication by a principal inverse; $f$ is already the full right side in the target coordinates of (WGB.29).

Define
$$
 \begin{aligned}
 S_{11}&=Id_Q+QKQ-QKPH^{-1}PKQ,\\
 S_{12}&=QU-QKPH^{-1}PU,\\
 S_{21}&=-VQ+VPH^{-1}PKQ,\\
 S_{22}&=Id_r+VPH^{-1}PU .
 \end{aligned}
 \tag{WGB.31}
$$
The complete remaining system is
$$
 \boxed{
 \begin{pmatrix}
 S_{11}&S_{12}&Qg-QKPH^{-1}Pg\\
 S_{21}&S_{22}&VPH^{-1}Pg\\
 \ell Q-\ell PH^{-1}PKQ&-\ell PH^{-1}PU&
                      \omega-\ell PH^{-1}Pg
 \end{pmatrix}
 \begin{pmatrix}q\\z\\\varkappa\end{pmatrix}
 =
 \begin{pmatrix}
 Qf-QKPH^{-1}Pf\\
 VPH^{-1}Pf\\
 f_\nu-\ell PH^{-1}Pf
 \end{pmatrix}.
 }
 \tag{WGB.32}
$$
All orders and signs are those of direct substitution into (WGB.29). In particular the second parameter entry and second right side are positive because that auxiliary row is $z-Vu=0$. This is different from the zero physical constraint in (WGB.22).

No factor of $V$, a true circle map, the sign operator or the actual transported input projection is commuted through $H^{-1}$. The full finite high/high factor remains in $z$. The entire metric high feedback remains in the last row.

Eliminating $z$ from (WGB.29) first gives
$$
 (Id+K+UV)u+g\,\varkappa=f,\qquad
 \ell u+\omega\,\varkappa=f_\nu.
 \tag{WGB.33}
$$
Eliminating the qualified high block instead gives (WGB.32). Both eliminations are invertible block operations. Therefore, once the actual square and its high inverse have been supplied, the complete bordered operator (WGB.33) is invertible if and only if the actual matrix in (WGB.32) is invertible. Redundant finite-factor coordinates do not invalidate the equivalence.

Every head coordinate has its inherited real phase and norm. On the pure primitive target, $Q_JY$ has $J-1$ reflected real coordinates. Additional finite physical coordinates and the auxiliary $z$ retain their declared weights. Complexification is a notation change, not a second physical copy. No inverse of this finite matrix is computed or asserted here.

If the regular square $\mathscr B=Id+K+UV$ has separately been proved invertible, the remaining scalar is the exact RNS Schur quantity
$$
 \sigma_\nu=\omega-\ell\mathscr B^{-1}g .
 \tag{WGB.34}
$$
Neither the positive root stable gap nor the scalar mean of $c_i$ proves this quantity nonzero. If the regular finite matrix has corank one, the RNS two nonzero kernel/cokernel pairings are the corresponding alternative criterion; actual corank and pairings are still separate obligations.

## WGB8. What the existing exact maps already supply

The following is a directed audit of the named mathematical records, not a claim about every file in the repository.

| Existing object | Qualification in this graph reduction | Remaining obligation |
|---|---|---|
| WCS high model and real basis | $\overline G:Y\to\mathcal D$ after the explicit low reference; old certified high gap is read in its original scope | The low reference is not a physical column |
| WIT/WBN source maps and same two-window inverses | Actual $C_Q,V_Q,\widetilde P$ with the ordered bounds (WGB.7)--(WGB.9); $H^{-1}$ interpolation and graph inclusion are proved in WFI | Numerical finite entries and actual physical low columns are not produced |
| WPL/WBP complete physical strong difference | Its whole map stays in $\mathcal F$ and $K$ once, including every original mean rank and paid finite source contribution | A quantitative $C_F$ and an evaluated final $J$ are new readouts; no smallness is presumed |
| Explicit IC primitive and density ranks already included in that difference | Their actual column/dual regularity supplies strong terms already in the complete map | They are not added again to $UV$ or removed by subtracting norm uppers |
| Original fixed normalizer endpoint finite maps | They retain their complete ordered endpoint factors; if already in the whole error, they stay there | A different split requires its exact operator identity and complete remaining bound |
| Faithful original high root coordinates from RNI/RNE/NIF | They allow the admitted common-right coordinate change of the same homogeneous regular graph | FC's absent repair does not supply the 96 actual physical low columns or a waist inverse |
| BF/BT original low-head dual maps | Their stated negative-window dual estimates qualify those exact transported rows when composed in the full actual order | The corresponding actual Poisson/readout columns remain required |
| WPM/RNS physical means and scalar equations | Their exact independence, reflection relations and coupled equation types remain available | Each row/column still needs its bounded realization in the proposed completed square and its actual values |
| A prescribed independent PW or radial source | Its admitted effect is part of the complete right side, with all true coordinate factors | An unknown infinite source cannot be relabelled as finitely many columns |
| Actual metric column and selected scalar | RNS supplies the exact block order and coordinate-chain rule | The complete column, row, high feedback and nonzero Schur or finite determinant remain to be established |

An already paid finite contribution may remain inside the complete strong part: the high test is then simply more conservative. Moving it into $UV$ is a different exact split and needs a complete bound for what remains. The old total upper is never reduced by subtracting another upper.

The raw WAD first-row output, the selected WPL normalized primitive row, and an original curvature/mean readout have different source and target units. A number for one of them is transported to this square only through the complete declared left and right maps; its leading term must be transported as well. No already successful record is renamed as another operator bound.

The only new unconditional conclusions are the exact reference parameterization (WGB.14), the symbolic complete high-tail bound (WGB.16), the 96-constraint equation (WGB.19)--(WGB.22), and the exact substitution identity (WGB.26)--(WGB.27) when genuine physical columns are supplied. Equations (WGB.29)--(WGB.34) are a conditional finite-border criterion for an actually realized complete square. They prove no full incoming inverse, no finite determinant, no nonlinear solution and no closure of an independent infinite rest block.

## WGB9. Immutable sources

| Primary and precise use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WFI: graph domain, actual finite projection and index ledger | aec7503e379c3abcbb66b33ed0a7e68be39703fa | 23476 | 7abf7f41df8fc48872c82b420836947a0728698d5142ac939c4d2d5ff99c4309 |
| WCS: real model blocks and the admitted high inverse | 4215c33aaec529176b1f8021904fd5f1e173e2fa | 12818 | 4998ef8208e3dc9e5474fe456bed53ebf4e7d987f7684d888f6705c9f1f55d0a |
| WIT: same two-window input inverse and actual reflected projection | 68737e28209551cab5b45aa251869892bc51b380 | 21308 | 13c5972c82dd1af1ded73ccdfdd6b8ba69da3c3a84bb278aea602d3dd90ba437 |
| WBN: source normalizer, true finite complement and ordered retained rows | 9507d853e18de92840abda11cb895a5989df1fc8 | 26506 | f6783549a2b29c5eebd4b31b6b604a89ba31345595cd3f03b86f6080927bde95 |
| WBP: polynomial target inverse and full same-row error | 54f859b305861a1c4be4be7826c059e1e4ffc3e8 | 18114 | 19f0182fb19cb3842948ee427993f7478af0557f2ec790c7c2f8ce5849015a7e |
| WPL: complete physical waist row and its precise strong extension | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |
| BF: genuine finite factors and exact high/finite elimination | 921dbfc574e94da86c8d44872a919c201c569060 | 19339 | e8e29c49deb9fabf6be9b9dd9059c26e94afbd1bc274742d7d3fe7527bf4a02e |
| RNS: complete metric border, full means and frozen-coordinate qualification | db0cce2048897eaecd8bf6e734f40e3b6e78c080 | 24616 | 74c6df5d816d9b80bfdb4c2e646237ad65f18e047788e5bec10739d1d3f64d9b |

All source access for this note is to small immutable text. The displayed norm combinations are symbolic and no numerical test is performed. No saved old scalar, producer, native object or successful graph is recomputed.
