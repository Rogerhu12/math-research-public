# R133 supplement: sharp graph high-block tests and complete-source regularity thresholds

2026-11-16, visible-exact / phase_inverse.

**Proved analytic sharpening and conditional source-to-graph interface.** On the already declared reflected waist graph, the artificial low comparison map makes no contribution to the actual high/high block. Its complete finite output remains in the low equations. The high test therefore needs the complete physical error bound, with the actual transported source projection, and no norm charge for that low comparison in the high block.

The same argument works at every fixed $1<\sigma\le4/3$. This identifies the minimum complete source regularity needed for the graph Fredholm argument. It does not identify a relative Airy remainder with a received physical error, evaluate a new scalar, supply the missing physical columns, or solve a finite matrix. The published WFI/WGB statements and their conservative bounds remain unchanged.

## WGT1. The fixed physical row and its graph

Keep exactly the selected parameter, real reflected spaces, physical frequency $4j$, and complete coordinate maps of WFI/WGB. Put
$$
 P=Id-\Pi,\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad n_j=4|j|,
 \qquad b=a+\Omega .
 \tag{WGT.1}
$$
The mean-zero reflected source and target are
$$
 X_b^s=\operatorname{Fix}(-ZR_b)\cap H_0^s,\qquad
 Y_a^s=\operatorname{Fix}R_a\cap H_0^s .
 \tag{WGT.2}
$$
The target projection onto its even reflection line is $Q_a=P\Pi_a^+$. It is different from a Fourier low projection.

Write
$$
 M_\nu=Q_a(Id+\nu_i I),\qquad
 \overline M=M_\nu P_{97}+L_{\mathrm{low}}Q_{97},\qquad
 Q_{97}=P-P_{97}.
 \tag{WGT.3}
$$
Here $L_{\mathrm{low}}$ is only the WFI real low comparison isomorphism. It is not a physical Poisson column. The model mean is the actual $\nu_i$ fixed by WCS/WPL, not the physical metric increment.

The closed model graph and its inverse are
$$
 \mathcal D=\{x\in X_b^{-1}:\overline Mx\in Y_a^0\},
 \qquad \overline G=\overline M^{-1}:Y_a^0\longrightarrow\mathcal D .
 \tag{WGT.4}
$$
Its norm retains both $\|x\|_{H^{-1}}$ and $\|\overline Mx\|_2$. WFI proves $L^2\cap X_b\subset\mathcal D$ using the actual $L^2$ forward bound for $\overline M$.

Let $C=\mathcal W S$, and let $A_{\rm src}$ be WBP's source normalizer. The genuine source projection is
$$
 \widetilde P=A_{\rm src}^{-1}C P_{97}C^{-1}A_{\rm src},
 \qquad \mathcal D_{\rm true}=\widetilde P\mathcal D .
 \tag{WGT.5}
$$
All products have their original order. In particular $\widetilde P$ need not commute with $\overline G$ or an ordinary Fourier cutoff. WFI proves that its complementary rank is $96$ on the real reflected line, that it is bounded on the graph, and that $\mathcal D_{\rm true}$ is closed of codimension $96$. The ambient signed complex complement has rank $192$; it is not a second copy of the reflected physical coordinates.

The complete homogeneous physical primitive row in these coordinates has the form
$$
 L=M_\nu+E
 \quad\hbox{on the actual source space.}
 \tag{WGT.6}
$$
This is the WPL row after the full WBP left and right changes. The physical factor $2\kappa_{\rm waist}$, independent means, amplitude equation, metric column and other ports retain their declared places. A bound for the raw WAD row is not automatically a bound for $E$ in (WGT.6).

## WGT2. A complete weaker smoothing window

Fix
$$
                         1<\sigma\le4/3 .
 \tag{WGT.7}
$$
The new hypothesis needed in this window is a bound for the same complete error,
$$
 E:\widetilde P X_b^{-\sigma}\longrightarrow Y_a^0,
 \qquad \|E\|\le C_{E,\sigma}.
 \tag{WGT.8}
$$
No extension of $E$ to an unrelated full circle is required. The formula $E\widetilde P$ uses its actual domain.

The already admitted same-operator bounds for $\widetilde P$ on $L^2$ and $H^{-4/3}$ give its $H^{-\sigma}$ bound by Hilbert interpolation. For example, with complete bounds $K_{P,0},K_{P,-}$,
$$
 \|\widetilde P\|_{H^{-\sigma}\to H^{-\sigma}}
 \le K_{P,\sigma}
 :=K_{P,0}^{\,1-3\sigma/4}K_{P,-}^{\,3\sigma/4}.
 \tag{WGT.9}
$$
A separately proved complete bound may instead be used. This is a symbolic formula, not a new evaluation of those bounds.

Any old $H^{-4/3}\to L^2$ error term can be restricted contractively to $H^{-\sigma}$. Thus only a genuinely new trial/source difference needs its new window. Its addition to the other complete terms must be justified by an exact same-column identity. A new trial's source norm is not, on its own, the complete $C_{E,\sigma}$.

The map
$$
 \mathcal D_{\rm true}\longrightarrow H^{-1}
       \lhook\joinrel\longrightarrow H^{-\sigma}
 \tag{WGT.10}
$$
has a bounded first arrow and a compact second arrow. Limits remain in the closed range of $\widetilde P$ in $H^{-\sigma}$. Hence (WGT.8) is compact from $\mathcal D_{\rm true}$ to $Y_a^0$. The WFI graph proof and index $-96$ therefore remain valid in this weaker smoothing window.

The strict inequality $\sigma>1$ is essential to this argument. At $\sigma=1$ it supplies neither compactness nor a decaying high-block estimate. Failure to prove this particular criterion is not a proof of noninvertibility.

## WGT3. Exact removal of the low comparison from the high block

For $J\ge97$ let $P_J$ be the ordinary high projection in the target $Y_a^0$, and put $Q_J=Id_{Y_a^0}-P_J$. WCS's high model inverse preserves each paired absolute frequency. Consequently
$$
 \|\overline G P_J:L^2\to H^{-\sigma}\|
 \le 2K_{\rm CYA}\Lambda_J^{-(\sigma-1)} .
 \tag{WGT.11}
$$
The order is the original one-loss inverse $L^2\to H^{-1}$, followed by the high embedding $H^{-1}\to H^{-\sigma}$. Only after those operations does $\widetilde P$ act.

Use the WGB reference extension
$$
 L_{\rm ext}=L\widetilde P+\overline M(Id-\widetilde P),\qquad
 L_{\rm ext}\overline G=Id+K ,
$$
$$
 K=K_E+K_{\rm ref},\qquad
 K_E=E\widetilde P\overline G,\qquad
 K_{\rm ref}=(M_\nu-\overline M)\widetilde P\overline G .
 \tag{WGT.12}
$$
This is an analysis extension, not a declaration of physical columns outside the true source.

Both $M_\nu$ and $L_{\rm low}$ preserve the paired absolute frequency. Therefore
$$
 M_\nu-\overline M=(M_\nu-L_{\rm low})Q_{97},
 \qquad
 \operatorname{ran}(M_\nu-\overline M)\subset Q_{97}Y_a^0 .
 \tag{WGT.13}
$$
It follows exactly that
$$
 P_JK_{\rm ref}=0,\qquad
 H_J:=Id_{P_J}+P_JKP_J
       =Id_{P_J}+P_JE\widetilde P\overline G P_J .
 \tag{WGT.14}
$$
No source projection has been commuted through a model inverse.

A sufficient high test is now
$$
 \boxed{\quad
 \chi_{J,\sigma}:=
 2K_{\rm CYA}\,C_{E,\sigma}\,K_{P,\sigma}
          \Lambda_J^{-(\sigma-1)}<1,\qquad
 \|H_J^{-1}\|_{2\to2}\le(1-\chi_{J,\sigma})^{-1}.
 \quad}
 \tag{WGT.15}
$$
For $\sigma=4/3$ this is the factor $\Lambda_J^{-1/3}$. For a smaller smoothing window its own exponent must be used.

The conservative WGB low comparison norm
$(2+|\nu_i|/4)\Lambda_{96}^{\sigma}$ is still valid where that finite map is estimated. It is absent from (WGT.15) because of the exact left projection (WGT.14), not because one numerical upper was subtracted from another. The full $Q_JKQ_J$ and $Q_JKP_J$ still contain it.

## WGT4. The finite comparison remains explicit

Let $E_X,E_Y$ be the isometric injections of the $96$ WFI real low basis vectors into $X_b$ and $Y_a$. For $1\le m\le96$, with $k=4m$, these vectors are
$$
 u_m=\sqrt2\cos(k\phi-kb/2-\pi/4),\qquad
 v_m=\sqrt2\cos(k\phi-ka/2).
 \tag{WGT.16}
$$
They obey
$$
 M_\nu u_m=r_m v_m,\qquad
 r_m=\cos\theta_m-\frac{\nu_i}{k}\sin\theta_m,\qquad
 \theta_m=k\Omega/2+\pi/4 .
 \tag{WGT.17}
$$
No lower bound or nonzero claim for these low $r_m$ is used. The reference map sends $u_m$ to $v_m$.

Define the exact finite factors
$$
 U_0=E_Y\,\operatorname{diag}(r_m-1),\qquad
 V_0=E_X^*\widetilde P\overline G .
$$
Then
$$
                    K_{\rm ref}=U_0V_0,\qquad P_JU_0=0 .
 \tag{WGT.18}
$$
The rows of $V_0$ are the displayed transported rows. They are not ordinary low input coefficients. The symbols $U_0,V_0$ in this section are finite factors, not background or Airy amplitudes.

For the problem with no additional physical columns, WGB gives
$$
 (Id+K_E+U_0V_0)u=f,\qquad \Theta u=0,\qquad
 \Theta=V_Q\overline G .
 \tag{WGT.19}
$$
The $96$ equations $\Theta u=0$ express the actual high source restriction. They have not been supplied by the reference columns.

Write $P=P_J,Q=Q_J$ only in the rest of this section, and set
$$
 D=PK_EQ,\qquad
 C=QK_EP+U_0V_0P,\qquad
 A_{00}=Id_Q+QK_EQ+U_0V_0Q .
 \tag{WGT.20}
$$
Once (WGT.15) passes, the exact remaining equations are
$$
 (A_{00}-CH_J^{-1}D)q=Qf-CH_J^{-1}Pf,
$$
$$
 (\Theta Q-\Theta PH_J^{-1}D)q
                  =-\Theta PH_J^{-1}Pf .
 \tag{WGT.21}
$$
The second right side is negative. Every finite comparison contribution is visible in $A_{00}$ and $C$.

If genuine physical columns $H_{\rm phys}$ are supplied, their difference from the reference columns is still
$$
 (H_{\rm phys}-\overline M C_Q)V_Q\overline G .
 \tag{WGT.22}
$$
It is retained as WGB's complete finite factor, with its real high/finite cross maps. No smallness of this factor's high/high action is needed when its auxiliary variable is kept. The high inverse in (WGT.15) remains the inverse before that finite factor is eliminated.

The full WGB/RNS $(q,z,\varkappa)$ matrix, its right side, the true metric column and all mean/amplitude rows remain in their original order. In particular $\varkappa$ is the physical metric increment, not $\nu_i$. The sharpened high test does not prove the finite matrix invertible, create $H_{\rm phys}$, or remove the original $96$ low output constraints.

## WGT5. What a uniform two-row trial must actually supply

Let $\mathscr U_j=(h_{1,j},f_j+z_j)$ be a proposed trial for the same complete reference column, parameter, physical signs and positive/root normalization. Its full volume residual and true seam jumps are
$$
 g_j=(\partial_r-G_h)\mathscr U_j,\qquad
 j_{\lambda,j}=[\mathscr U_j]_{r_\lambda}.
 \tag{WGT.23}
$$
The original input normalization, including $n_j^{7/6}$ when that is the declared column, belongs to these expressions before a decay exponent is assigned.

The N.6/N.7 reconstruction with the same complete $J$ can make the second ordinary residual exactly zero. If this has been proved for the proposed trial, then on each actual smooth piece
$$
 g_j=(g_{1,j},0),\qquad
 g_{1,j}=(D_0-E)J[(D_0-B)f_j-z_jb_2]-KCf_j-z_jb_1 .
 \tag{WGT.24}
$$
Its parity is odd in the original physical angle. The solved state mean $z_j$ remains in this expression and in the state. Zero second residual is not zero second state.

On a strict interval with the actual $q>0$, the complete primitive-density source is exactly
$$
 \mathfrak D_r(g_{1,j},0)
 =\frac{n_g}{\sqrt{2q}}\big(Ig_{1,j},Ig_{1,j};0,0\big).
 \tag{WGT.25}
$$
The two last entries vanish by the proved odd source parity. The actual evolution still couples to the stored means. The same formula applies to a jump $(j_{1,j},0)$ only after continuity of the trial's second row has been proved. General true jumps retain both rows and all mean entries.

The factor in (WGT.25) is not used at the turning point by division by $q=0$. The root collar, its positive correction, and the same-reference initial error need their original qualified maps or a new complete estimate. A zero trace difference is a permissible conclusion only from exact equality of both physical root state rows in the same genuine normalization. Equality to a free trial does not identify the nonzero genuine root shear.

A complete bound for the received error must include all of the following, in the same input and output units:

- The full initial/root/positive difference and its true propagation to the observation row.
- The full volume residual integrated in ordinary physical $dr$, with the actual receiver and every Jacobian if another radial variable is used.
- Every true state jump as an impulse, with no radial-length factor.
- The complete endpoint trial-to-first-symbol difference, including the full old primitive, the mean/density ranks and both sides of the actual normalizers.
- The full left normalization to (WGT.6) and the full right input coordinate. A coordinate change changes the leading row and its error together.

A relative profile estimate, a scalar height-only estimate, or a source before its true $J/I$, physical frame, input power and receiver has been paid is not the decay exponent used below. A critical transition width alone supplies no additional power: WTS retains the entire derivative-of-cutoff term.

For a fixed compatible physical observation, the exact signed adjoint identity on a strict interval $[0,c]$ is
$$
 \langle\lambda(0),e(0)\rangle
 =\langle\lambda(c),e(c)\rangle
  +\int_0^c\langle\lambda(r),g_{\mathscr U}(r)\rangle\,dr
  +\sum_{0<r_\lambda<c}\langle\lambda(r_\lambda),j_{\lambda,\mathscr U}\rangle ,
 \tag{WGT.26}
$$
where $e$ is exact state minus trial and $\lambda'=-G_h^*\lambda$. True one-sided matching is retained when required. If the residual and jump have the qualified first-row form, only their first components pair in (WGT.26); $\lambda_2$ is still part of the full adjoint evolution. This supplies a route to genuine finite entries or complete bounds. It is not an evaluation of them.

## WGT6. Complete column and block criteria

Use a fixed coordinate isomorphism $\mathcal U$ from the original reflected high Fourier space to the actual source of (WGT.8), with its already qualified $H^{-\sigma}$ inverse bound. For instance WFI uses the entire $A_{\rm src}^{-1}CD_+$, restricted to the original reflected high space. No transported projection is replaced by an ordinary one.

Suppose the whole received error, after all items in WGT5, has complete column bounds
$$
 \|E\mathcal U e_j\|_{Y_a^0}\le C\,n_j^{-p},
                  \qquad j\ge97 .
 \tag{WGT.27}
$$
Here $e_j$ is an orthonormal basis of the single reflected line for each positive absolute frequency. A calculation using two separate signed input sets must retain its complete corresponding direct-sum fee.

The full weighted Hilbert--Schmidt sum is
$$
 \|E\mathcal U:H^{-\sigma}\to Y_a^0\|^2
 \le C^2\sum_{j\ge97}\Lambda_j^{2\sigma}(4j)^{-2p}.
 \tag{WGT.28}
$$
It converges when
$$
                              p>\sigma+\tfrac12 .
 \tag{WGT.29}
$$
Multiplication by $\|\mathcal U^{-1}\|_{H^{-\sigma}}$ then gives the bound on the true source. No output orthogonality was assumed.

Alternatively let $B_k$ be the original orthogonal input blocks
$2^k97\le j<2^{k+1}97$, and suppose a genuine full block-operator estimate has been proved:
$$
 \|E\mathcal U B_k:L^2\to Y_a^0\|
             \le C(4\cdot97\cdot2^k)^{-p}.
 \tag{WGT.30}
$$
Put $\gamma_4=\sqrt{17}/4$. On that block
$\Lambda_j\le2\gamma_4(4\cdot97\cdot2^k)$.
Triangle inequality followed by Cauchy--Schwarz gives
$$
 \|E\mathcal U:H^{-\sigma}\to Y_a^0\|
 \le C(2\gamma_4)^\sigma
 \left\{\sum_{k\ge0}
       (4\cdot97\cdot2^k)^{2(\sigma-p)}\right\}^{1/2}.
 \tag{WGT.31}
$$
Thus this complete block criterion needs $p>\sigma$. A per-column estimate cannot be substituted for (WGT.30). At equality this proof supplies no convergent bound; an additional operator argument would be needed.

For the original $\sigma=4/3$ goal, (WGT.29) requires $p>11/6$ and the block criterion requires $p>4/3$. If only the graph Fredholm conclusion is needed, there exists a qualified $1<\sigma\le4/3$ whenever the complete column exponent satisfies $p>3/2$, or the complete block exponent satisfies $p>1$. One chooses $\sigma$ strictly below the relevant upper endpoint and uses its own high decay in (WGT.15). These are sufficient criteria, not converse obstructions.

## WGT7. Which finite quantities still need actual computation

This is a directed inventory for the named WGB/WPL/WBP construction.

| Quantity | Already available exact qualification | What a new computation must genuinely supply |
|---|---|---|
| $K_{\rm CYA}$ and the paired model | Original certified high gap and the fixed real phases | Read the same saved constant; do not repeat the old scalar gap |
| $\widetilde P,C_Q,V_Q,\Theta$ | Same two-window coordinate maps and graph qualification | Actual finite rows or complete bounds for their displayed compositions when a matrix is evaluated |
| The low reference factor $U_0V_0$ | Exact (WGT.16)--(WGT.18), with no low inverse | Its finite coefficients if numerically used; these are reference coefficients, not physical Poisson columns |
| $C_{E,\sigma}$ | The full exact same-column error decomposition | A complete new source/endpoint/receiver bound, or a previously saved bound of this exact operator and window |
| $H_J^{-1}$ | Conditional Neumann inverse after (WGT.15) | An actual directed strict test; finite high feedback still uses this same inverse |
| $QK_EQ$, $QK_EP H_J^{-1}PK_EQ$ and the $\Theta$ rows | Exact ordered finite formulas (WGT.20)--(WGT.21) | Genuine matrix entries or complete enclosures, including the high feedback |
| $H_{\rm phys}$ | No identification with $L_{\rm low}$ is made | The actual additional physical input columns, their bounded output realization and their true pairings |
| Metric, amplitude, mean and exterior rows/columns | WGB/RNS/WPM retain their exact types and signs | Their complete entries and high feedback; the metric column is not just a root or phase derivative |

Equation (WGT.26), with the true left observation and right input maps, can compute the needed forward/adjoint pairings without pretending that a norm upper is a matrix entry. A finite Neumann expansion for a high feedback may be enclosed only with its complete remainder from the actual strict high test.

The $96$ missing physical columns are not supplied by constructing a better high trial. If those columns are absent, (WGT.21) remains the correct system with $96$ extra constraints. If they are present, the full square and its finite determinant are still separate obligations. An unknown radial head in $L^2_r(\mathbb C^{193})$ or an independent radial mean function remains infinite-dimensional until its real equation has been eliminated.

A new complete upper for the same final physical error may be compared with an old whole upper after their exact source, target and coordinate identities have been proved. Different trials or different left normalizers are not directly compared by taking a numerical minimum of their separate residual bounds. No upper is subtracted from another.

## WGT8. Immutable sources and scope

| Source and use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WFI: true graph, real low basis and index | aec7503e379c3abcbb66b33ed0a7e68be39703fa | 23476 | 7abf7f41df8fc48872c82b420836947a0728698d5142ac939c4d2d5ff99c4309 |
| WGB: graph parameterization and complete finite border | 30cd8f7858888c35f942094611614c9f74b3e2af | 25135 | e7d23c583205fcb538fd21260e2e9c5b4859ed73ab6129a453b8c5d1fb05bf7c |
| WCS: actual constant-model inverse and graph loss | 4215c33aaec529176b1f8021904fd5f1e173e2fa | 12818 | 4998ef8208e3dc9e5474fe456bed53ebf4e7d987f7684d888f6705c9f1f55d0a |
| WPL: complete physical primitive row | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |
| WBP: actual two-sided source and target maps | 54f859b305861a1c4be4be7826c059e1e4ffc3e8 | 18114 | 19f0182fb19cb3842948ee427993f7478af0557f2ec790c7c2f8ce5849015a7e |
| N.3--9: exact two-row residual and independent physical mean | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| WTS: complete trial replacement and frequency-order criteria | 08ec2cc5289729dcbfb3de3ebc5799ba8f7dce95 | 27396 | bb7dff28f8f8f0064029a63622b2a8ef949894733fa06384c8c3b4b084dbb94d |
| WAD: complete physical adjoint and first-row source units | 1dfa6d56a249157b27d23d6249fb451cb9fdb6d0 | 28366 | 0a92e2e5e5c1f0e1e93bc509ad5883d20630ad9909be3b33eaff7546f641702a |
| RNS: genuine metric border and independent rest | db0cce2048897eaecd8bf6e734f40e3b6e78c080 | 24616 | 74c6df5d816d9b80bfdb4c2e646237ad65f18e047788e5bec10739d1d3f64d9b |

This proof uses small immutable text and symbolic operator identities only. No old or new scientific value, profile, ray, source, inverse or matrix is evaluated. The selected reflected homogeneous primitive graph is the scope; no full incoming inverse, actual finite determinant, nonlinear branch, unqualified parameter family, or disappearance of an independent physical port is asserted.
