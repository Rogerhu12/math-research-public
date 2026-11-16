# R133 supplement: frozen cross-block value enclosures for the positive radial head

This gives a second complete tail certificate for the same positive problem as WPT. It freezes a finite cross block on each radial cell and pays its entire signed value difference. No radial derivative of the actual cross block is required. In particular, this candidate does not require new whole-positive bounds for beta_r or K_r.

The WHV result remains unchanged: run 43838214094/1 completed its scientific targets, but its sufficient mesh gate was false at N=4096. Its diagnostic required N=145475, above the declared cap. That failure proves neither singularity nor the feasibility of a much larger finite solve. This note evaluates no new number, chooses no new computational mesh, and grants no finite inverse.

## WPTV1. Same positive realization and all physical inputs

Use the actual interval I_+=[r_*,25/8], ordinary dr and the real reflected head fibre E_L of dimension 193: 96 odd components and 97 even components including the physical mean. Let

$$
 \mathscr H=L^2(I_+;E_L),\qquad
 K=B_{LH}G_H B_{HL},\qquad F_0=I-V_0(A_L+K).
 \tag{WPTV.1}
$$

Here G_H is the already admitted positive given-head realization, with its actual boundary and transmission conditions. Its complete source and output spaces are

$$
 G_H:L^2_rH^{-2/3}_{\phi,H}\longrightarrow L^2_rH^{-1}_{\phi,H}.
 \tag{WPTV.2}
$$

It is not a new Green operator with convenient artificial endpoint conditions. The independent radial head, physical means, radial initial values, original outer chart, nu column, affine sources and jumps, Theta constraints and all earlier finite factors remain as in WHR, WHV and WPT.

The old source split is fixed:

$$
 I_c=[r_*,c],\quad I_b=[c,25/8],\quad
 c=1192029371497/5000000000000 .
 \tag{WPTV.3}
$$

The original complete raw-state columns C_c,C_b bound G_H on these two disjoint ordinary-source subspaces. Equivalently, for the distribution adjoint,

$$
 \|\mathbf1_{I_j}G_H^*v\|_{L^2H^{2/3}}\le C_j\|v\|_{L^2H^1},
 \quad j=c,b .
 \tag{WPTV.4}
$$

These are the full original source columns, not endpoint-only fees. Their original records are read from the successful WHV document; neither source propagation is repeated.

Partition I_+ into cells I_i of length h_i, with every genuine value or transmission jump, each change of the chosen S_i, and c at a cell endpoint. An old interface at which the actual coefficients and homogeneous state really agree may lie inside a cell, but each closed coefficient enclosure must still be evaluated on its own valid original piece. Retain every one-sided coefficient value and every affine jump. A subdivision introduced only for interval estimates is not a new state impulse.

Choose the same mean-preserving, cellwise constant S_i and selfadjoint transformed principal Dtilde_i as WPT. In a body cell one may use

$$
 S_i(h_1,h_2)=(h_1,q_i h_2),\quad q_i>0,\qquad
 D_i=\eta_i
 \begin{pmatrix}0&-q_i^2\partial_\phi\\\partial_\phi&0\end{pmatrix}.
 \tag{WPTV.5}
$$

The entire even component, including its mean, is scaled. On the root collar the safe choice is S_0=I,D_0=0. No positive curvature gap is extended through the true root.

Let Pi_i be ordinary cell averaging and Q_i=I-Pi_i, and put Q=direct_sum Q_i. The whole difference e_i>=||S_i(A_L-D_i)S_i^{-1}|| retains every term of WPT.12. All norms and their conversion factors refer to this fixed raw fibre.

## WPTV2. Freeze a cross block, without replacing the true operator

For each cell choose an explicit constant finite map

$$
 B_i^0:E_L\longrightarrow H_{\phi,H},\qquad
 B_i^0=P_{\{97\le |j|\le J_i\}}B_i^0,\quad J_i\le288 .
 \tag{WPTV.6}
$$

Its entries can be exact rationals in the same normalized real reflected bases. It is only a reference map. A rational midpoint of a verified enclosure is not asserted to be the actual coefficient at a point. Its full 193 input columns, including the even constant, must be retained.

Define, on I_i,

$$
 C_i=S_i^{-*}B_i^{0*},\qquad
 E_i(r)=S_i^{-*}(B_{HL}(r)^*-B_i^{0*}) .
 \tag{WPTV.7}
$$

Take complete bounds

$$
 \begin{split}
 E_{B,i}&\ge\|E_i\|_{H^{2/3}_{\phi,H}\to E_L}
       =\|(B_{HL}-B_i^0)S_i^{-1}\|_{E_L\to H^{-2/3}_{\phi,H}},\\
 C_{A,i}&\ge\|C_iA_{HH}^*\|_{H^{2/3}_{\phi,H}\to E_L},\\
 C_{B,i}&\ge\|C_iB_{LH}^*S_i^*\|_{E_L\to E_L},\\
 C_{LH,1}&\ge\|B_{LH}^*S^*\|_{\mathscr H\to L^2_rH^1_{\phi,H}}.
 \end{split}
 \tag{WPTV.8}
$$

All cell bounds are essential suprema on their complete cell. In particular, E_B is obtained from a true signed difference with B_i^0; subtracting two positive operator-norm upper bounds cannot produce it. C_A contains the whole actual high generator, including drift, reaction and ordered primitive terms. Freezing its principal part alone would not prove (WPTV.8).

The angular products are finite. With the original full coefficient shift 192, B_LH reads only 97..288 and

$$
 A_{HH}B_i^0=P_{\{97\le |j|\le J_i+192\}}A_{HH}B_i^0 .
 \tag{WPTV.9}
$$

Thus J_i<=288 gives the safe 97..480 output shell. For a reference constructed only from the large degree32 centre, one can have J_i<=160; the actual family still has its full degree96 difference. This support reduction is not a band assigned to an unknown high state.

The Riesz weights are explicit: E_B uses Lambda^(-2/3)(B_HL-B0)S^-1, C_A uses Lambda^(-2/3)A_HH B0 S^-1, and C_B uses S B_LH B0 S^-1, in the true bases, where Lambda_j=(1+16j^2)^(1/2). The primitive retains both ordered convolutions and annihilates only its actual intermediate zero mode. The physical head mean is not that intermediate mode.

## WPTV3. Exact weak identity and the new input-tail estimate

For psi in the transformed head space put

$$
 w=G_H^*B_{LH}^*S^*\psi,\qquad
 \widetilde K=S K S^{-1}.
 \tag{WPTV.10}
$$

The same weak interior identity used in WPT gives

$$
 -w'=A_{HH}^*w+B_{LH}^*S^*\psi,\qquad
 \widetilde K^*\psi=C_iw+E_iw\quad\hbox{on }I_i .
 \tag{WPTV.11}
$$

Although w need not have a whole angular derivative in the source norm, the finite quantity C_iw has the required ordinary radial weak derivative: its right side is bounded by the two complete composites in (WPTV.8). C_i is radial constant inside the cell. Hence Poincare applies to C_iw:

$$
 \|Q_i C_iw\|\le\frac{h_i}{\pi}
       \{C_{A,i}\|w\|_{I_i,H^{2/3}}
                         +C_{B,i}\|\psi\|_{I_i,E_L}\}.
 \tag{WPTV.12}
$$

The other term uses only the contraction norm of Q_i:

$$
                  \|Q_i E_iw\|\le E_{B,i}\|w\|_{I_i,H^{2/3}} .
 \tag{WPTV.13}
$$

No derivative of E_i, B_HL, a saved upper bound or an ordinary input occurs.

As a simple complete bound, let C_A,C_B,E_B be the respective cell maxima and C_G=(C_c^2+C_b^2)^(1/2). Combining (WPTV.12)--(WPTV.13), the L2 direct sum and (WPTV.2) gives

$$
 \|\widetilde KQ\|=\|Q\widetilde K^*\|
 \le\frac{h_{\max}}{\pi}(C_A C_G C_{LH,1}+C_B)
                                +E_B C_G C_{LH,1}.
 \tag{WPTV.14}
$$

There is a useful complete refinement that retains the small original collar column. Define

$$
 d_i=\frac{h_i}{\pi}C_{A,i}+E_{B,i},\qquad
 b_i=\frac{h_i}{\pi}C_{B,i},\qquad
 d_j=\max_{I_i\subset I_j}d_i\ (j=c,b),\quad b_*=\max_i b_i .
 \tag{WPTV.15}
$$

Then

$$
 \boxed{\quad
 \|\widetilde KQ\|\le B_K:=
 C_{LH,1}\sqrt{(C_c d_c)^2+(C_b d_b)^2}+b_* .
 \quad}
 \tag{WPTV.16}
$$

Indeed, the cell inequalities give ||Q_i Ktilde*psi||<=d_i||w||_i+b_i||psi||_i. Apply Minkowski to the L2 direct sum, then (WPTV.4) to its two original source regions. This does not assume output orthogonality between the two forward Green columns.

For the root-cell choice B_0^0=0,S_0=I, C_A,0=C_B,0=0. E_B,0 can be read directly as the already saved WHV A_c, of type E_L to H^(-2/3). No q^(-1), beta_r or K_r is needed on that cell.

## WPTV4. Complete tail gate and retained finite equations

The exact transformed tail block is still

$$
 R_Q=R_D-QSV_0(A_L-D)S^{-1}Q-QSV_0KS^{-1}Q .
 \tag{WPTV.17}
$$

Here R_D is WPT's true block principal operator, with ||R_D^{-1}||<=1. In the final term the past-cell integral is constant on the receiving cell and is killed by Q_i. The remaining outer operator is

$$
             T_i=Q_i V_{0,i},\qquad \|T_i\|\le h_i/\pi .
 \tag{WPTV.18}
$$

There is **no right Q_i** in (WPTV.18). The intermediate feedback may have a radial mean; replacing T_i by Q_iV0,iQ_i would omit its ramp. The latter periodic primitive can be used only after retaining WPT's separate zeta equation and full ramp columns.

Set delta_A=max_i h_i e_i/pi. The complete candidate (WPTV.16) gives the new sufficient gate

$$
 \delta_{\mathrm{value}}
      :=\delta_A+\frac{h_{\max}}{\pi}B_K<1 .
 \tag{WPTV.19}
$$

The simpler candidate (WPTV.14) instead gives

$$
 \delta_{\mathrm{simple}}
 =\delta_A+\frac{h_{\max}^2}{\pi^2}(C_A C_G C_{LH,1}+C_B)
                         +\frac{h_{\max}}{\pi}E_B C_G C_{LH,1}.
 \tag{WPTV.20}
$$

Only after one complete candidate passes a saved outward strict comparison may its same-operator resolvent bound (1-delta)^(-1) be recorded. Different meshes, S, D or B0 choices are kept as separate whole candidates; their matrix entries are never spliced. The existing WPT derivative candidate also remains separate and unchanged.

A successful tail gate would only make the true WPT.31 four-block Schur reduction available. All four blocks, both right sides, original initial values, physical means, actual outer-coordinate matching, 96 prescribed root-even coordinates, nu, Theta, WFR/WCF factors, cokernel conditions and independent function inputs must still be carried through. The signed finite pairings and a verified inverse of that genuine square are separate targets. No dimension increase is silently authorized by a false bound.

## WPTV5. A smaller complete value-data closure

The baseline does not need to restore the original degree96 response shards. The full-delta positive native already preserves, in every original closed row:

- the complete original intrinsic enclosure;
- the large degree32 repaired-centre bounds;
- the complete delta drift and local differences;
- the full pair A0 and first angular-derivative differences;
- the independent true mean difference.

These are exactly the fields listed in the companion input inventory. Reading them preserves the complete real-family scope. It does not declare the full response to solve the PDE.

The signed large-centre values are obtained from the unchanged exact binary64 cubic data and the original 65 rational repair-offset suprema:

$$
 u_0=\alpha U_{\rm cubic}+e_u,\qquad
 v_0=C_{\rm ref}^{-1}+\alpha V_{\rm cubic}+e_v .
 \tag{WPTV.21}
$$

The alpha, PPoly descending-power order, physical frequency factor4, every original piece and every Fourier component are fixed by the complete old index. The already computed offset suprema enclose the exact offset for every original piece. Their old 6143-interface construction is not repeated. The new signed coefficient enclosures serve the new B0/difference/composite targets; they do not rerun the old A0-row, Riccati or Green targets.

For clarity, the small delta term can be bounded as an entire operator difference. Let U,V,U1,V1 be the already saved repaired-centre A0 bounds, e0,e1 the saved complete pair differences, k an upper bound for |K| and b for |beta|. Let dd,ddphi,da,de,db be the saved complete delta coefficient fees. Put

$$
 \begin{split}
 D_\Delta&=d_a+d_e+(1+k)d_b,\\
 N_\Delta&=\frac b2\{e_1[U+e_0+k(V+e_0)]
                         +(U_1+V_1)(1+k)e_0\}.
 \end{split}
 \tag{WPTV.22}
$$

This is the two-factor difference of the actual ordered primitive
-2 beta (u_phi,v_phi)^t I(u,Kv). The factor1/2 is 2 times the true L2 primitive norm1/4; it is not an L-infinity primitive bound. Both components, the mean and every mixed product are retained. The whole raw coupling differences satisfy

$$
 \|\Delta B_{HL}\|_{E_L\to L^2}
       \le384d_d+D_\Delta+N_\Delta,\qquad
 \|\Delta B_{LH}\|_{L^2\to E_L}
       \le384d_d+d_{d\phi}+D_\Delta+N_\Delta .
 \tag{WPTV.23}
$$

For the second drift estimate, transpose the full drift and use the low output derivative; the derivative of the multiplier is precisely the retained ddphi. The Sobolev conversion for the high output uses the existing WHV Lambda388^(-2/3) record. It is not replaced by a low-input frequency.

The radial scalar principal commutes with Q_L. Its low-to-high and high-to-low blocks are zero. The physical gamma rank has low output and vanishes on high input. Those facts remove them only from B_HL, B_LH and the high-high rank term. The actual high generator in C_A still has its full eta principal; the true eta difference is bounded by gamma times the saved mean difference. A_L and e_i retain both their principal difference and the entire gamma mean rank.

Thus a coefficient-level or block-level signed enclosure can combine the large-centre reference with (WPTV.22)--(WPTV.23). It must also pay the complete repaired-centre-to-B0 difference, including the original repair-offset enclosure; the delta difference alone is not E_B. For C_A it must also include the actual eta variation and every action of A_HH on the complete range of B0. For C_B it keeps the full ordered product with B_LH. This statement does not authorize subtracting a saved positive fee from any other fee.

One safe complete choice for C_LH,1 is the new product

$$
             C_{LH,1}^{\rm basic}:=1153\,L_*\,\max_i\|S_i\|,
 \tag{WPTV.24}
$$

which majorizes the norm in (WPTV.8). Here L_* and 1153 are already saved in WHV. The shell identity precedes this conversion. A new direct finite contraction for the same complete operator can replace that whole candidate. Neither route repeats the L_* maximum.

No new beta_r, K_r, gamma_r, eta_r, metric second jet or natural-graft primitive is required by this value-only certificate. Those remain possible inputs to WPT's independent derivative route. In particular, old negative-only scalar jets or a root-only enclosure are not extended over the positive body.

## WPTV6. Exact readonly restoration and type checks

The companion inventory fixes 17 existing small UTF-8 inputs and 19 historical binary parts. This is an input inventory, not a frozen executable manifest or an already executed admission.

The binary closure consists of:

1. The same 13 WHV lossless parts. Concatenating their decoded byte chunks yields the exact original 25,507,783-byte gzip, SHA256 1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c.
2. The five original ac1 PPoly shards, all available at commit 46f127c7153f5393dcd2a00f42d4c1d3662c294d. Their complete index is 6750 bytes, SHA256 ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413.
3. The original centre-repair gzip at commit 12b06502f2e4d522ca5dc16d6064267859b3a0a1, blob f5dc1d8e7f40cc6a97ca80de26455b12000c163a, 14,226 bytes, SHA256 6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc.

Only authorized own Actions may fetch and decode those binary objects, in a temporary data directory. No binary body was fetched in preparing this note. The original producers and the old shard module are readonly source evidence; the new consumer must use its own data-only reader, not import a module that imports an old producer.

Admission preserves the complete old native: all11 gates, both4650-row orders, the whole inflated4650-row cover and3594 original interfaces, full summary projection, all input identities and the genuine 4608 progress literal. The manifest's older zero/null row metadata is not reinterpreted. WHV's three named maxima are now completed old records and are not selected again.

For the candidate, every part's exact bytes/SHA/Git blob, original shape [4,6144,65], strict node order, shared endpoint bits, 6145 nodes and all metadata are checked before decoding its exact binary64 values as dyadic rationals. No finite solve is run and the original finite-success/noncertificate flags remain unchanged.

The repair reader preserves its complete six gates, centre definition, 65 exact rational suprema, special offsets, full mean and scope. It does not rebuild the offset sequence. Intrinsic beta/K/gamma/Cref records enter signed constructions as full intervals. Positive norm records are read at their upper endpoints; positive denominator roles use their lower endpoints. In particular, a negative Cref interval is not replaced by an unsigned upper value.

The existing own prepared archive is an optional restoration source for the same files, not another computation: run43583838026/1, artifact14109363064, exact 166,702,374-byte archive SHA256 34d95f5d263b210134da3ae5bb243df4369cd83fbdd196c068c9727b194cd710. Its complete prepared manifest and current expiry must be rechecked before use. The direct history closure above avoids depending on that expiry.

## WPTV7. The concrete next computation and its limits

The next job can be limited to complete signed value/composite enclosures and the sufficient gate. Its mesh, maximum number of cells, rational reference recipe, whole output shapes and resource cap must be declared before scientific evaluation. This note does not preallocate a large matrix.

The new mathematical graph has these stages:

1. Admit all original data and preserve the old scopes and failed WHV gate.
2. Construct each declared reference and its complete e_i,E_B,i,C_A,i,C_B,i bounds, with every original piece and one-sided value represented. Keep complete candidates and deterministic whole maxima/witnesses.
3. Read old C_c,C_b,L_*,1153,A_c and pi; form the new complete tail candidate (WPTV.15)--(WPTV.19), using the same declared references throughout.
4. Record the strict comparison. Only if it is true form a same-operator resolvent bound. On a false comparison, save the complete result and stop the proposed inverse path.
5. If separately authorized and feasible, compute all true signed finite Schur blocks and test a complete inverse residual. No artificial 96 reference columns replace the physical columns.

Every completed new scientific target is saved in full before its downstream use. Old values are read, not differentiated. No old positive row sweep, high Green construction, trial solve, original repair, root success, completed WHV maximum or previous failed sufficient comparison is reevaluated.

The value-only and derivative certificates are two complete proofs for the same tail. A valid choice compares complete final candidates after all their own prerequisites have been met. It does not turn a finite-output factor into a finite-input operator, identify the true outer chart with a raw endpoint, delete a cokernel, or resolve the independent negative radial head.

## WPTV8. Immutable evidence

Paths below are relative to topics/visible-flex-exact-nearby/. The input inventory supplies all19 exact binary restoration tuples and all17 small-input identities. The new equations above were checked as text; no scientific function was executed.

| Evidence | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| New readonly input inventory, notes/2026-11-16-R133-frozen-cross-block-readonly-input-inventory.json | 18ec6014b06315aaf24cf9068e6fa31e05e6025a | 38086 | f7dd2ed019b30c076aa70ad1536601813095ef59bb504049d976eb0cd93b1547 |
| WPT, cellwise principal/dual-tail contract | b37c59bc05a2131b27014f37c1a6555d6f7e2c58 | 22954 | 22fb6fac312540818390bea1bb3a3ed2c750f515ad91bbbb1b0790fcdfe1fd6e |
| WHV actual, notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json | ebe7ae42c2482ce9b20e7af1d41e02f89b920010 | 12011 | ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72 |
| Existing WHV input inventory | 18428ac8d144863cf831a10eb8af17e51d3c2ddc | 23789 | 80f9f606f14f8cea41f3a4f18a5d6b9c7d59274ea8016199b1cc086cf58b59ce |
| Complete original coefficient source, scripts/fourfold_codazzi_current_positive_complete_coefficients.py | 45ce0d7171ad35aa3175ea03fdac22f5158fa855 | 21756 | 1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c |
| Centre-repair definition, scripts/fourfold_codazzi_final_continuous_value_repair.py | 67d7de2adf36c916123f7c9cf7a5db09af3c7b58 | 9076 | 51a3f7968991ed85211b74c23befae7021bb192796daf0ae2d12ec5a1d45329b |
| Original repair inflation, scripts/fourfold_codazzi_repaired_positive_high_Volterra.py | 538ca4f6c9f25f669daf2ce1a175fd0bfbacb40a | 21932 | 8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d |
| Full family values/difference source, scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py | f4dd9ad8b324e39fed478183b88095c949d5c09a | 19660 | 0df3ae7181d5ac8808928e9b0ed4bcf225fa3f80ae5df944b2a96a5e4d3ae117 |
| Original lossless cubic format, scripts/fourfold_codazzi_candidate_shards.py | 81a21dba0077137601382781b6b3298bdd7d5ade | 4187 | 5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e |
| Complete ac1 index, data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json | 2257c4327fcafcad3ed50f0362fb089e9cfd56d2 | 6750 | ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413 |

The original full source and mean domains enter through the same negative-one graph and WHV qualifications already pinned in WPT. No new background PDE identity is assumed.
