# R133 supplement BT: concrete transported-head factors and the retained-operator audit

2026-11-15. Analytic identities and source audit only; no new scientific numerical execution.

This supplement applies [BF](R133-supplement-retained-finite-factors-and-complete-bordered-incoming.md) to the actual cutoffs and coordinate order in [WY](R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md), [MS](R133-supplement-exact-Maslov-sign-operator-and-common-input-outgoing-order.md) and [ZD](R133-supplement-strong-sign-density-conjugation-and-global-Cayley-return.md). It supplies two exact improvements for the genuine old finite input: its transported dual rows do not need the root-normalizer inverse factor, and its right Maslov factor acts through a finite unitary diagonal matrix. It also separates a finite Fourier head on one circle from a finite angular head varying over a radial interval.

The exact primary versions read for this audit include BF blob 921dbfc574e94da86c8d44872a919c201c569060 (19339 bytes, SHA256 e8e29c49deb9fabf6be9b9dd9059c26e94afbd1bc274742d7d3fe7527bf4a02e), SE blob eb7b1bb1ea1fdf713fcf172428f68ed20afafdb2 (20047 bytes, SHA256 2220174707046248cbdf9f9f8c47bc13bc233b0ab65f5ed598ddcbf964e93ad4), and the complete SF source identity 0f93e925d354133675b84ffeaa959a0b58d339a0 (35289 bytes, SHA256 add091118ef1af71bc8c4be275742d4124a076d6cf2ebaf00d35c66f8348f2b4).

The complete numerical WE/SJ/CG paid map is retained as one strong term. No previously paid norm is subtracted from an upper bound. No actual low-input column, physical matching mean or independent second-reference input is assigned zero.

## 1. Fixed circles, actual cutoffs and independent means

Use the normalized circle with basis $e_j=e^{4ij\phi}$ and
$$
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 P_N=1_{\{|j|\ge N\}},\quad Q_N=1-P_N,\qquad
 I=\partial_\phi^{-1}(1-\Pi).
 \tag{BT.1}
$$
The exact common input and root normalizer are
$$
 \mathcal S=U_{\mathcal H^{-1}}U_{X_-},\qquad
 T_F=1+P_{1024}M_{F_*}IP_{1024},\qquad
 R=T_F^{-1}\mathcal S^{-1}.
 \tag{BT.2}
$$
The complete $F_*$ has degree at most 192. The same $T_F^{-1}$ exists on $L^2$ and $H^{-4/3}$ by the already completed TF result. The same selected $\mathcal S^{\pm1}$ acts on both windows by WX. Both true-density maps preserve the scalar integral.

The actual original high input is $P_{97}$ on this root input circle. It is distinct from the moving cutoff $J_s=268435456$ and from any final principal-coordinate cutoff $J$. The auxiliary scalar mode $j=0$ is distinct from the two independent physical mean coordinates in the raw/primitive-plus-mean matching problem.

Let
$$
 E:\mathbb C^{193}\longrightarrow\operatorname{ran}Q_{97},
 \qquad E E^*=Q_{97},\quad E^*E=1,
 \tag{BT.3}
$$
be the normalized full complex Fourier embedding for $-96\le j\le96$. If the actual original domain omits its auxiliary zero mode, the actual embedding has 192 nonzero slots instead. Neither convention removes either physical mean.

The exact old columns used below must be those of the chosen actual Poisson/matching realization. A normalization formula proved only for $|j|\ge97$ does not define an extension to the old low modes. In particular the high-only formula for $\Lambda_\sigma^{-1}$ is not evaluated on them by convention.

## 2. The root-normalizer factor cancels on the actual old head

Set $A_F=P_{1024}M_{F_*}IP_{1024}$. Since $Q_{97}P_{1024}=0$,
$$
 Q_{97}A_F=A_FQ_{97}=0,\qquad
 Q_{97}T_F=T_FQ_{97}=Q_{97}.
 \tag{BT.4}
$$
Multiplying these equalities by the same two-sided inverse gives
$$
 \boxed{
 Q_{97}T_F^{-1}=T_F^{-1}Q_{97}=Q_{97}.
 }
 \tag{BT.5}
$$
This uses the actual double compression and nested cutoffs. It is not division of one upper bound by another.

Consequently the precise old-low expression retained in WY.38 has the sharper factorization
$$
 \boxed{
 A_{\rm old}Q_{97}T_F^{-1}\mathcal S^{-1}
       =L_{\rm old}V_{\rm old},\qquad
 L_{\rm old}=A_{\rm old}E,\quad V_{\rm old}=E^*\mathcal S^{-1}.
 }
 \tag{BT.6}
$$
Here $A_{\rm old}$ already includes every actual left normalization that belongs to those old columns. All root, waist, radial, angular and physical-mean units of these columns remain part of their definition. No claimed bound for an arbitrary source-to-solution inverse manufactures the actual signed columns $A_{\rm old}e_j$.

Let $K_{\mathcal S^{-1},-}$ be the complete accepted $H^{-4/3}$ norm of the same selected inverse density. Then
$$
 \begin{split}
 \|(V_{\rm old})_j\|_{(H^{-4/3})^*}
       &\le K_{\mathcal S^{-1},-}\Lambda_j^{4/3},\\
 \|V_{\rm old}:H^{-4/3}\to\ell^2_{193}\|
       &\le K_{\mathcal S^{-1},-}\Lambda_{96}^{4/3}.
 \end{split}
 \tag{BT.7}
$$
The joint estimate uses the orthogonal finite Fourier projection and has no additional $\sqrt{193}$. Unlike the general BF.7 estimate, BT.7 contains no $K_{F,-}$.

For $j=0$ there is the exact improvement
$$
                     (V_{\rm old})_0=\Pi\mathcal S^{-1}=\Pi .
 \tag{BT.8}
$$
This only concerns the auxiliary scalar mean row. An actual physical mean matching row is not changed into $\Pi$ by this formula.

If the actual old column operator has norm $L_{\rm old}^+$, a complete permitted bound is $L_{\rm old}^+K_{\mathcal S^{-1},-}\Lambda_{96}^{4/3}$. This text does not claim that the actual $L_{\rm old}^+$ or the signed finite matrix has already been supplied. The correct row estimate and the missing column obligation are separate.

## 3. The transported head is an idempotent and respects the actual sign

The correct finite complement in the selected common input is
$$
 \widetilde Q=R^{-1}Q_{97}R
     =\mathcal S Q_{97}\mathcal S^{-1}
     =(\mathcal S E)(E^*\mathcal S^{-1}),
 \qquad \widetilde P=1-\widetilde Q.
 \tag{BT.9}
$$
Thus $\widetilde Q^2=\widetilde Q$, its rank is 193 under BT.3, and $R\widetilde P=P_{97}R$. It need not be orthogonal. Its range is the genuine span of the transported functions $\mathcal S e_j$, rather than the first 193 Fourier functions of the new principal angle.

An estimate proved only on $\operatorname{ran}\widetilde P$ does not authorize setting the complementary actual map to zero. For any already defined complete operator $B$,
$$
 B\widetilde Q=(B\mathcal S E)(E^*\mathcal S^{-1}).
 \tag{BT.10}
$$
The columns $B\mathcal S e_j$ are again actual columns. BT.10 is not an identification with $A_{\rm old}e_j$ unless the actual definition of $B$ gives that identification.

Use the complete root sign of MS,
$$
 \mathcal Z=\Pi+i\Pi_+-i\Pi_-,
 \qquad \mathcal Z^{\mathcal S}=\mathcal S\mathcal Z\mathcal S^{-1},
 \qquad Z_{97}=E^*\mathcal Z E .
 \tag{BT.11}
$$
The finite $Z_{97}$ is unitary, with diagonal entries $-i,1,i$ on the negative, zero and positive labels. Since $[Q_{97},\mathcal Z]=0$,
$$
 [\widetilde Q,\mathcal Z^{\mathcal S}]=0,\qquad
 V_{\rm old}\mathcal Z^{\mathcal S}=Z_{97}V_{\rm old}.
 \tag{BT.12}
$$
In particular,
$$
 (L_{\rm old}V_{\rm old})\mathcal Z^{\mathcal S}
       =(L_{\rm old}Z_{97})V_{\rm old}.
 \tag{BT.13}
$$
The norm of the actual finite column operator is unchanged by this finite unitary right factor. This old-head contribution therefore does not require multiplication by the global negative-window norm of $\mathcal Z^{\mathcal S}$. No other, unrelated finite functional is granted the identity in BT.12.

The same statement holds for any actual original Fourier embedding $E_L$:
$$
 V_L=E_L^*T_F^{-1}\mathcal S^{-1}
 \quad\Longrightarrow\quad
 V_L\mathcal Z^{\mathcal S}=Z_LV_L,\qquad
 Z_L=E_L^*\mathcal ZE_L,
 \tag{BT.14}
$$
because the actual $T_F^{-1}$ commutes with the original root sign. The cancellation of $T_F^{-1}$ itself in BT.6 additionally uses $Q_{97}\le Q_{1024}$ and is not asserted for larger $L$.

## 4. Actual finite endpoint maps, with their real factors

The finite root-normalizer difference
$$
 F_F=M_{F_*}I-P_{1024}M_{F_*}IP_{1024}
 \tag{BT.15}
$$
has both input and output support in $|j|\le1215$. Indeed in
$Q_{1024}M_{F_*}I+P_{1024}M_{F_*}IQ_{1024}$ at least one index has absolute value at most 1023, while the two labels differ by at most 192.

For the normalized Fourier embedding $E_F$ of this whole finite span, set
$$
 M_F=E_F^*F_FE_F .
 \tag{BT.16}
$$
At a single fixed endpoint, with its genuine bounded left map $A$,
$$
 AF_FT_F^{-1}\mathcal S^{-1}
       =(AE_FM_F)(E_F^*T_F^{-1}\mathcal S^{-1}).
 \tag{BT.17}
$$
This is a concrete finite factorization. It does not assert finite Fourier input support after the last coordinate change. If this exact term is already included in the complete TF/CG norm-paid remainder, the default treatment is to leave it there. It cannot be removed by subtracting its upper bound from a larger upper bound.

The same fixed-endpoint rule applies to the actual moving $F_T=T-T_{J_s}$ of SF.19–20. Its two-sided support is through $J_s+575$ on the **moving** circle. The embedding and actual matrix must use that circle, both components and every scalar mean row. A finite composition on the left and right preserves rank, although it changes its columns and dual rows.

The full-density versus mean-identity realization has the explicit scalar factor
$$
 U_\psi-\widehat U_\psi=(\psi'-1)\Pi,\qquad
 U_\psi^{-1}-\widehat U_\psi^{-1}
       =((\psi^{-1})'-1)\Pi .
 \tag{BT.18}
$$
With actual left/right maps $A,B$, the corresponding column and row are $A(\psi'-1)$ and $\Pi B$, or their inverse counterparts, with the sign dictated by the actual realization. If full density is used consistently on both sides, an extra rank is not artificially introduced. If the rank is already part of CG, its fee is not repeated.

The two primitive conjugation ranks in IC are genuine rank-one factors of the form $b\otimes p_\psi-(bp_\psi)\otimes1$. Their complete fees are already inside the accepted CG and WE paid map. Their membership in a finite-rank class does not make their known numerical contributions unpaid again.

## 5. A finite map at each radius need not give a finite integrated operator

The complete SF defect is propagated through the actual radial evolution. Schematically one of its terms has the form
$$
 \mathcal K=\int_{0}^{r_c}
    \mathcal U(0,r)\,\mathcal F_J(r)\,\mathcal V(r)\,dr .
 \tag{BT.19}
$$
SF.20 and SF.35–38 bound the fixed-$r$ finite map $\mathcal F_J(r)$, including its differentiated dual rows. The true left propagation and the right transported trial can make both finite spans depend on $r$.

Consequently the fixed-$r$ Fourier support statement does not, by itself, prove that BT.19 has finite rank. A common fixed finite factor, or a separate exact telescoping identity with all source and jump terms, is required for that conclusion.

For an explicit general example, on a Hilbert space with orthonormal $e_j$, $j\ge1$, put
$$
 v(t)=\sum_{j\ge1}2^{-j}e^{2\pi ijt}e_j,\qquad
 K(t)=v(t)\otimes v(t)^*,\quad 0\le t\le1 .
 \tag{BT.20}
$$
Each $K(t)$ has rank one, the family is smooth, but
$$
                 \int_0^1K(t)\,dt=\operatorname{diag}(4^{-j})_{j\ge1}
 \tag{BT.21}
$$
has infinite rank. Thus even a uniform finite-rank bound at each radius is insufficient.

The successful SJ source integral and all its interface terms are already part of the complete SF contribution to WE. They remain in the norm-paid strong map. This classification does not alter any successful scalar result or weaken its source estimate. In contrast, a finite number of genuine endpoint factors of the form BT.17 retain finite rank under their fixed compositions.

## 6. Physical means and radial low head have different types

Let the chosen actual square matching space be
$$
                \mathbb X^s=H^s(\mathbb T;\mathbb C^d)\oplus\mathbb C^m .
 \tag{BT.22}
$$
The value of $m$ and its actual physical equations must be specified by the matching problem. This notation does not invent an identity block for coupled physical means.

Let $E_m$ embed the actual finite matching coordinates, $P_m=E_mE_m^*$ and $P_c=1-P_m$. For an already defined complete linear map $D$,
$$
 D-P_cDP_c
   =E_m(E_m^*D)+(P_cDE_m)E_m^* .
 \tag{BT.23}
$$
This keeps both the physical mean input columns and the physical mean output rows, without double counting the mean/mean block. To use it as a bounded strong finite factorization, the actual columns $P_cDe_\alpha$ must lie in the output $L^2$ space and the rows $e_\alpha^*D$ must have the required $H^{4/3}$ dual regularity. A finite codomain alone gives neither a missing row value nor its dual bound.

A radial low head has a different domain. Even with only 193 angular slots at each radius, the source space
$$
              L^2((0,r_c);\mathbb C^{193})
 \tag{BT.24}
$$
is infinite dimensional. Its physical given-head Poisson receiver is not BT.6. Zero waist low trace does not imply zero radial low head.

The given-head terminal-Ai column in P/AW is defined with its prescribed head. Independent PW low-head or ordinary-source inputs remain separate ports. If one later eliminates a radial low head through the complete finite-angular Green equation, that elimination produces an actual feedback operator on the remaining function spaces. Its complete bound or exact invariant subspace must be established; an old scalar Green norm does not itself identify the signed feedback or make it finite rank.

The seven PW port **types** are likewise not seven scalar dimensions. Any prescribed external data remain actual right-hand-side inputs. Unknown functional ports cannot be deleted from a square matching problem by calling them a border.

## 7. Complete classification of the six original WE entries

| Original entry | What is now concretely known | What still requires actual input |
|---|---|---|
| Physical mean matching rows | BT.23 gives exact finite factors for a chosen bounded realization; the two physical means stay distinct from $\Pi$. State mean-source errors already paid in WE remain paid. | The actual coupled mean columns/rows and their dual/column data. |
| Full-density/mean-identity difference | BT.18 supplies the true rank-one columns and rows whenever that realization difference is present. IC primitive ranks already belong to CG. | Which realization is actually used, and any term not already included in the accepted paid map. |
| Original low input transported by the common right factor | BT.6–8 give the exact row without $K_{F,-}$. BT.12–13 put its commonout sign into a finite unitary matrix. | The actual old input columns and their original normalization; they are not supplied by a high-only asymptotic theorem. |
| Root head and two-reference blocks | Original circle head is finite; radial head BT.24 is not. The growing component generated by the covered terminal-Ai input remains inside its already complete AW/RR/ST comparison. | A separate independent reference input remains infinite unless its actual domain is finitely projected or the same-graph elimination theorem applies. |
| Opposite sign and Maslov realization | The exact commonout factor is $U_RB_-\mathcal Z^{\mathcal S}$. ZD/DZ pay the specific infinite strong difference $\mathcal Z^{\mathcal S}-\mathcal Z$. | Other actual infinite sign blocks, and the second global Cayley sign commutator, are not made finite by this payment. |
| Final principal high/finite, finite/high and mean rows | These arise from actual finite principal-coordinate projections and admit BT.25 below. | Their complete entries and the finite inverse; they are not read from the old root head or set to zero by a cutoff name. |

[SE](R133-supplement-natural-stable-port-Fredholm-and-exact-reference-elimination.md) permits exact cancellation of a common second-reference factor only on the same actual positive graph, with the specified two-window factor and its genuine isomorphism hypotheses. It does not remove an independent second input. In particular the complete incoming injectivity hypothesis used to establish that isomorphism cannot be replaced by high-block invertibility alone.

## 8. Final cross blocks and the actual complete operator identity

For a chosen final principal-angle finite orthogonal projection $Q=E_JE_J^*$, including every independent physical mean, let $P=1-Q$. Once the complete actual $B$ is defined and bounded in the required spaces,
$$
 \boxed{
 B-PBP=E_J(E_J^*B)+(PB E_J)E_J^* .
 }
 \tag{BT.25}
$$
This identity retains high/finite, finite/high and finite/finite entries exactly once. It does not require the transported old head $\widetilde Q$ to commute with the final $P$; in general it does not.

BT.25 is an exact factorization, not a numerical certificate for those rows or columns. The true normalized inner product, both physical means and every actual right coordinate factor must remain in the entries. A final scalar projection cannot replace the physical matching problem by a different square system.

For one completely specified square incoming realization, the accounting takes the form
$$
 \boxed{
 B=T+E_{\rm paid}+E_{\infty,\rm unpriced}
                +\sum_{\alpha=1}^{N_{\rm factors}}L_\alpha V_\alpha .
 }
 \tag{BT.26}
$$
Each finite factor in the sum is supported by an actual finite projection or finite matching coordinate, as in BT.6, BT.17, BT.18 or BT.23. The original paid submap is kept intact. Every remaining infinite term must either have its own complete strong bound or remain part of an explicitly retained infinite principal relation.

The BF form $B=T+E+LV$ follows only when the actual factors and complete strong remainder have all been identified:
$$
 E=E_{\rm paid}+E_{\infty,\rm unpriced},\qquad
 L=(L_1,\ldots,L_N),\qquad V=(V_1,\ldots,V_N)^{\mathsf T}.
 \tag{BT.27}
$$
A missing infinite norm cannot be replaced by zero in this formula. The finite factorization itself does not prove that $B$ is invertible.

For the outgoing branch, first keep the exact order $U_RB_-\mathcal Z^{\mathcal S}$. BT.13 can be used on genuine transported Fourier-head factors. For the remaining terms, use the full ZD order and its actual bounds. Neither a finite low factor nor a scalar principal inverse permits commuting $\Lambda_\sigma$, $\mathcal S$ or an actual incoming inverse across an unrelated operator.

## 9. Minimal next inputs

A concrete complete incoming/Schur construction now needs the following, rather than another calculation of a successful upper bound:

1. The actual square realization: which complete incoming row, scalar and physical mean inputs, given-head convention, height/outer conditions and independent functional ports are being solved for.
2. The actual normalized old low-input columns $A_{\rm old}e_j$, with their physical mean outputs. The complete row map is already BT.6–8, and the commonout sign is the finite $Z_{97}$.
3. The coupled physical mean columns and dual rows in BT.23, with any exact full-density versus mean-identity difference fixed.
4. For any infinite remainder not already inside WE/SJ/CG/DZ, a same-object strong bound or an exact principal-factor treatment. A radial integral of varying finite maps does not qualify automatically as a finite factor.
5. The actual final principal-coordinate matrix and its full cross rows after all transported finite terms are included. The existing BF augmented equation then applies without discarding $V P$.

The accepted numerical fields already available for the row bounds are the WX selected $\mathcal S^{\pm1}$ windows and the existing TF inverse identity. No old ray, Fourier grid, Green sweep, residual producer or successful scalar consumer is called by this audit. None of the five missing data categories is declared paid merely because it has a symbolic finite-factor representation.
