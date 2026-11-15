# R133 supplement: the exact Maslov sign operator and the common-input outgoing order

2026-11-15, tail_connector.

**Proved analytic statement and source audit.** The two independently leading-normalized branch receivers of WY, CG and WE are retained exactly. With one common incoming normalization, the outgoing branch has an additional sign operator in a specified position. This note proves that position, proves the actual common root normalizer commutes with that sign operator, and gives a complete strong commutator estimate when a later construction chooses to change the position. It performs no new numerical calculation and does not certify a full incoming inverse or a complete return.

## MS1. Circle, domains and the two normalizations

Use the same selected member, true root and waist maps, original terminal-Ai reference, and physical wave labels as PF.20b and WY.39--51. The original root circle has length $\pi/2$, normalized measure and frequencies $4j$. Write
$$
 I=\partial_\phi^{-1}(1-\Pi_0),\qquad
 P_{97}=P_{\{|j|\ge97\}},\qquad
 \Lambda_j=(1+16j^2)^{1/2},
 \qquad
 \|a\|_{H^t}^2=\sum_j\Lambda_j^{2t}|\widehat a_j|^2 .
 \tag{MS.1}
$$
The root Fourier projectors $\Pi_+,\Pi_-,\Pi_0$ mean $j>0,j<0,j=0$. They are not moving waist projectors or selected-angle projectors.

Let $\mathcal A_\sigma$ be the exact branch map after the fixed waist matrix normalizer has been withdrawn and the complete primitive-plus-mean row has been read, as in WY.5, WY.11 and WY.47--49. On the original $P_{97}$ input, define its individually normalized root branch $\mathcal L_\sigma$ by
$$
 \mathcal A_\sigma
   =U_{X_{-\sigma}}\mathcal L_\sigma\Lambda_\sigma,
 \qquad
 \Lambda_\sigma
   =\ell_{\sigma,+}\Pi_+
                  +\ell_{\sigma,-}\Pi_- .
 \tag{MS.2}
$$
Thus $\mathcal L_\sigma=1+M_{C_\sigma}I+\mathcal R_\sigma$ is an exact definition when $\mathcal R_\sigma$ contains every remaining term. A paid sub-budget for $\mathcal R_\sigma$ is not a proof that its complete norm has been paid. The exact primitive projections, physical means, old head, second reference column and other retained contributions keep the scope recorded in WY and WE.

The true selected input chart is
$$
 \mathcal S=U_{\mathcal H^{-1}}U_{X_-}
           =U_{X_-\circ\mathcal H^{-1}},\qquad
 U_{\mathcal H^{-1}}U_{X_+}=U_{R_\Omega}\mathcal S .
 \tag{MS.3}
$$
Here $U_\alpha U_\beta=U_{\beta\circ\alpha}$ is the density pullback convention. Put
$$
 \mathcal B_\sigma
       :=\mathcal S\mathcal L_\sigma T_F^{-1}\mathcal S^{-1}.
 \tag{MS.4}
$$
These are the **individually** $\Lambda_\sigma$-normalized branches. In particular the selected physical outgoing receiver with its own normalization is $U_{R_\Omega}\mathcal B_-$.

All identities about the existing high construction initially hold on
$\operatorname{ran}P_{97}^{\mathcal S}$, where
$$
 P_{97}^{\mathcal S}=\mathcal S P_{97}\mathcal S^{-1}.
 \tag{MS.5}
$$
This projector is not asserted to be an orthogonal selected Fourier projection. An identity on the full space requires the actual low columns and two independent physical mean ports as well. They are not supplied by an arbitrary extension of (MS.2).

## MS2. The actual relative phase is $i\epsilon$

FA.21 uses printed phase $X+\tau\omega$ and the coefficient
$e^{-i\epsilon\tau\pi/4}/(2\sqrt\pi)$. The physical convention of PF.2 and WY.39 is $\tau=-\sigma$. The original terminal-Ai normalization has $a_{0,*}=1$ and the other free coefficient vanishes to the stated root order. Consequently
$$
 \kappa_{\sigma,\epsilon}
       =\frac{e^{i\epsilon\sigma\pi/4}}{2\sqrt\pi}.
 \tag{MS.6}
$$
PF.20b and WY.6--7 give
$$
 \ell_{\sigma,\epsilon}
   =\frac{\sigma\sqrt2}{i\epsilon}\,
      n_{g,*}\left(\frac{k_*}{\lambda_*}\right)^{1/4}
       E(0)\,\kappa_{\sigma,\epsilon}.
 \tag{MS.7}
$$
The complete mean-residual factor $E(0)$ and all radial normalizations are common in the ratio. They have not been set to one or replaced by a residual-free equation. Hence
$$
 \boxed{\quad
 \frac{\ell_{-,\epsilon}}{\ell_{+,\epsilon}}
     =-e^{-i\epsilon\pi/2}=i\epsilon .
 \quad}
 \tag{MS.8}
$$
This is the outgoing/incoming ratio in (MS.2). Reversing the ratio reverses the sign. No extra sum or $\sqrt2$ is incurred when the two input sectors are assembled into the same operator.

For full-circle algebra choose the explicit extension
$$
 Z=\Pi_0+i\Pi_+-i\Pi_- .
 \tag{MS.9}
$$
Extend each $\Lambda_\sigma$ by its own sign constant on $1\le|j|<97$ and by one at $j=0$. These extensions make $\Lambda_-\Lambda_+^{-1}=Z$ on the full auxiliary circle. Their values below 97 are only an algebraic convention: the actual old finite columns must still be retained. In particular (MS.9) does not replace either of the two physical mean receivers.

On every $H^t$, $Z$ and $Z^{-1}$ have norm one. Also
$Z^2=-1+2\Pi_0$, and the real Fourier conjugacy is preserved.

## MS3. The saved common root normalizer preserves the two signs exactly

The actual operator of TF and TFA is
$$
 T_F=1+A_F,\qquad
 A_F=P_{J_F}M_{F_*}I P_{J_F},\qquad
 J_F=1024,\qquad
 \operatorname{supp}\widehat F_*\subset[-192,192].
 \tag{MS.10}
$$
The full mean of $F_*$ is included. The successful TFA receipt gives the same inverse on $L^2$ and $H^{-4/3}$; it acts as identity below $J_F$ and on the independently adjoined mean coordinates.

For $k\ne0$ its Fourier matrix is
$$
 (A_F)_{jk}
   ={\bf1}_{|j|\ge J_F}{\bf1}_{|k|\ge J_F}
        \frac{\widehat F_*(j-k)}{i\,4k}.
 \tag{MS.11}
$$
If $j,k$ have opposite signs, then $|j-k|\ge2J_F>192$, so this entry is exactly zero. Every row or column below $J_F$ is zero as well. It follows that
$$
 [T_F,\Pi_\pm]=[T_F,\Pi_0]=[T_F,P_{97}]
   =[T_F,\Lambda_\sigma]=[T_F,Z]=0 .
 \tag{MS.12}
$$
Multiplying by the same two-sided inverse proves all these commutators also vanish for $T_F^{-1}$. This is an exact support argument, not an inference from a small norm or from finitely tested modes.

Thus the specific $T_F^{-1}$ of (MS.10) is an exception to the general prohibition against commuting a sign diagonal through a nonconstant multiplier. The broad caution in WY.49 remains necessary for $\mathcal S^{-1}$, arbitrary normalizers and transported rows. The present exception uses both high projections and the complete degree192 support; it does not hold for unrestricted $1+M_{F_*}I$.

## MS4. One incoming right normalization gives a right outgoing sign factor

Use one common input map
$$
 \mathcal N_i=\Lambda_+^{-1}T_F^{-1}\mathcal S^{-1}.
 \tag{MS.13}
$$
Define the actual selected incoming and outgoing maps on this common input by
$$
 \mathcal I_{\rm com}=U_{\mathcal H^{-1}}\mathcal A_+\mathcal N_i,
 \qquad
 \mathcal O_{\rm com}=U_{\mathcal H^{-1}}\mathcal A_-\mathcal N_i .
 \tag{MS.14}
$$
Set
$$
 Z^{\mathcal S}=\mathcal S Z\mathcal S^{-1}.
 \tag{MS.15}
$$
Equations (MS.2)--(MS.4), (MS.8) and (MS.12) prove, in order,
$$
 \begin{split}
 \mathcal I_{\rm com}
   &=\mathcal S\mathcal L_+T_F^{-1}\mathcal S^{-1}
     =\mathcal B_+,\\
 \mathcal O_{\rm com}
   &=U_{R_\Omega}\mathcal S\mathcal L_-Z
                                     T_F^{-1}\mathcal S^{-1}\\
   &=U_{R_\Omega}\mathcal S\mathcal L_-T_F^{-1}
                                      Z\mathcal S^{-1}\\
   &=\boxed{\,U_{R_\Omega}\mathcal B_-Z^{\mathcal S}\,}.
 \end{split}
 \tag{MS.16}
$$
No $Z$ has been passed through $\mathcal L_-$, a scalar coefficient or the true input chart. This is the common-input outgoing order.

The exact factor $Z^{\mathcal S}$ is a full infinite-dimensional operator. It has two infinite eigenspaces and is not part of a finite head merely because it came from two sign labels. It can be retained in the exact position in (MS.16), without a commutator estimate. For $t=0,-4/3$,
$$
 \|Z^{\mathcal S}\|_{H^t\to H^t},
 \ \|(Z^{\mathcal S})^{-1}\|_{H^t\to H^t}
 \le \|\mathcal S\|_{H^t\to H^t}
       \|\mathcal S^{-1}\|_{H^t\to H^t}.
 \tag{MS.17}
$$
The four true coordinate factors on the right have existing WX receipts. Their products, if wanted as printed directed numbers, would be a new scalar combination; none is calculated here. There is no claim that $Z^{\mathcal S}$ is unitary in the selected $L^2$ measure.

The transported input projector commutes with $Z^{\mathcal S}$:
$$
 [P_{97}^{\mathcal S},Z^{\mathcal S}]=0 .
 \tag{MS.18}
$$
This statement does not move $P_{97}^{\mathcal S}$ through a branch or identify it with a selected Fourier cutoff. Nor is $[U_{R_\Omega},Z^{\mathcal S}]=0$ asserted.

The full density identities $\Pi_0\mathcal S=\Pi_0$ and
$\Pi_0\mathcal S^{-1}=\Pi_0$ give
$$
 \Pi_0 Z^{\mathcal S}=\Pi_0,\qquad
 (Z^{\mathcal S})^2
    =-1+2(\mathcal S1)\otimes\Pi_0 .
 \tag{MS.19}
$$
Thus scalar integral preservation is exact. The transported zero-mode subspace is the span of $\mathcal S1$, not an uncharged identification with the selected constant function. The two physical mean ports and any mean-identity realization corrections remain separate.

## MS5. What is required to move the sign factor to the left

The exact alternative to (MS.16) is
$$
 \boxed{\quad
 \mathcal O_{\rm com}
   =U_{R_\Omega}Z^{\mathcal S}\mathcal B_-
     +U_{R_\Omega}[\mathcal B_-,Z^{\mathcal S}].
 \quad}
 \tag{MS.20}
$$
For the individually normalized expansion
$\mathcal B_-=1+M_{c_o}I+\mathcal E_o$, the extra term is
$$
 [\mathcal B_-,Z^{\mathcal S}]
   =[M_{c_o}I,Z^{\mathcal S}]
      +[\mathcal E_o,Z^{\mathcal S}] .
 \tag{MS.21}
$$
Both parts have their actual directed order. Any exact finite pieces of
$\mathcal E_o$ can remain individually recorded, but the whole commutator is not declared finite rank.

Equivalently one may keep the complete infinite leading factor and conjugate the whole branch:
$$
 \mathcal O_{\rm com}
   =(U_{R_\Omega}Z^{\mathcal S})
       \bigl((Z^{\mathcal S})^{-1}\mathcal B_-Z^{\mathcal S}\bigr).
 \tag{MS.22}
$$
This has no omitted term. It does not identify the conjugated coefficient with the old $c_o$ or permit the unchanged old scalar gap calculation to stand for the entire return.

If the actual incoming inverse is later established on its full required space, its common-input return is
$$
 \mathcal O_{\rm com}\mathcal I_{\rm com}^{-1}
    =U_{R_\Omega}\mathcal B_-Z^{\mathcal S}\mathcal B_+^{-1}.
 \tag{MS.23}
$$
Existence of that inverse is a hypothesis here. Neither
$Z^{\mathcal S}$ nor $\mathcal B_+^{-1}$ has been commuted. The old finite Schur and physical mean completion obligations persist.

In particular the notation $\zeta U_{R_\Omega}(1+M_{c_o}I+\mathcal E_o)$ in IC.20, and its sector uses in P/PF, must retain its fixed-sector or declared leading-separation meaning. It is not, without the missing commutator or an explicit new conjugation, the global common-input formula (MS.16). The normalized $c_i,c_o$ of IC.23/WY.50--51 remain the same functions. The successful CG, PG and WE branch budgets are unchanged. A scalar Cayley/Maslov gap certificate keeps its original scalar scope and is not thereby a certificate for (MS.23).

## MS6. A complete strong estimate for the root sign commutator

There is a direct way to pay a genuine sign commutator when its position must change. Define
$$
 W_{1/3}(c)=\sum_{\ell\in\mathbb Z}
                  (1+|4\ell|)^{1/3}|\widehat c_\ell| .
 \tag{MS.24}
$$
For every $c$ with finite $W_{1/3}$,
$$
 \boxed{\quad
 \|[M_cI,Z]\|_{H^{-4/3}\to L^2}
    \le \frac{17}{8}\,
           W_{1/3}(c-\langle c\rangle).
 \quad}
 \tag{MS.25}
$$
The commutator also annihilates a constant input, since $I1=0$; its possible nonzero scalar mean output is included.

Indeed, writing $z_0=1$ and $z_j=i\,\operatorname{sgn}j$ otherwise, the exact Fourier entry for $k\ne0$ is
$$
 ([M_cI,Z])_{jk}
   =\frac{z_k-z_j}{i\,4k}\widehat c_{j-k}.
 \tag{MS.26}
$$
A nonzero entry has $j=0$ or opposite nonzero signs, so
$|j-k|\ge|k|$ and $|z_k-z_j|\le2$. The $k=0$ column is zero. Also
$$
 \frac{\Lambda_k^{4/3}}{4|k|}
   =(4|k|)^{1/3}
           \left(1+\frac1{16k^2}\right)^{2/3}
   \le \left(\frac{17}{16}\right)^{2/3}
                  (4|j-k|)^{1/3}.
 \tag{MS.27}
$$
Apply the $\ell^1$--$\ell^2$ convolution inequality to the weighted input
$\Lambda_k^{-4/3}\widehat a_k$. Since
$2(17/16)^{2/3}<17/8$, (MS.25) follows. The coefficient at $\ell=0$ commutes identically and is the only coefficient excluded from its right side. This exclusion is an exact commutator identity, not deletion of a physical mean. In particular the entire $j=0,k\ne0$ output row was kept in (MS.26).

For the complete density-conjugated first primitive,
$$
 \mathcal D_c=\mathcal S M_cI\mathcal S^{-1}
      =M_{\mathcal S c}I+\mathcal F_c,\qquad
 \mathcal F_c
   =(\mathcal S c)\otimes p_\psi
      -((\mathcal S c)p_\psi)\otimes1 ,
 \tag{MS.28}
$$
where $\mathcal S=U_\psi$ and $p_\psi$ is the full mean-zero displacement, IC.16 gives
$$
 [\mathcal D_c,Z^{\mathcal S}]
       =\mathcal S[M_cI,Z]\mathcal S^{-1}.
 \tag{MS.29}
$$
Consequently
$$
 \|[\mathcal D_c,Z^{\mathcal S}]\|_{H^{-4/3}\to L^2}
 \le\frac{17}{8}
       \|\mathcal S\|_{L^2\to L^2}
       \|\mathcal S^{-1}\|_{H^{-4/3}\to H^{-4/3}}
       W_{1/3}(c-\langle c\rangle).
 \tag{MS.30}
$$
The two ranks in $\mathcal F_c$ are essential in this exact conjugation. If one estimates $[M_{\mathcal S c}I,Z^{\mathcal S}]$ by itself, one must additionally retain or bound $[\mathcal F_c,Z^{\mathcal S}]$.

There is an equally direct estimate before the common root normalizer. If the complete root remainder in (MS.2) has a verified bound
$\|\mathcal R_\sigma\|_{H^{-4/3}\to L^2}\le E_\sigma^{\rm root}$, then (MS.12) proves
$$
 [\mathcal B_\sigma,Z^{\mathcal S}]
   =\mathcal S[M_{C_\sigma}I+\mathcal R_\sigma,Z]\,
                         T_F^{-1}\mathcal S^{-1},
 \tag{MS.31}
$$
and hence
$$
 \begin{split}
 \|[\mathcal B_\sigma,Z^{\mathcal S}]\|_{H^{-4/3}\to L^2}
 \le {}&
 \|\mathcal S\|_{0}\,K_{F,-4/3}
           \|\mathcal S^{-1}\|_{-4/3}\\
 &{}\times
 \left\{\frac{17}{8}W_{1/3}
                  (C_\sigma-\langle C_\sigma\rangle)
                       +2E_\sigma^{\rm root}\right\}.
 \end{split}
 \tag{MS.32}
$$
The factor two comes from two genuine compositions with the unitary root $Z$, one on each side of the remainder. There is no second $T_F^{-1}$ and no extra sign count. The complete root $C_\sigma$, rather than an upper bound obtained by subtracting the two normalized branches, is the coefficient in this formula.

CG already stores a whole-function $W_{1/3}$ bound for the complete cut-plus-propagated $C_\sigma$. That full bound may conservatively replace the nonmean norm in (MS.32). The bound $E_\sigma^{\rm root}$ must still concern the complete same root remainder. A selected paid subtotal cannot be substituted without its exact coordinate and remainder identity. Keeping the exact factor in (MS.16) avoids this optional reordering altogether.

For direct consumption of the already selected, normalized paid submap, define
$$
 z_t^\#=\|\mathcal S\|_{H^t\to H^t}
                   \|\mathcal S^{-1}\|_{H^t\to H^t},
 \qquad t=0,-4/3 .
 \tag{MS.33}
$$
If the exact decomposition of one normalized branch is
$\mathcal B_-=1+M_{c_o}I+\mathcal E_o^{\rm paid}
+\mathcal E_o^{\rm retained}$, with the WE bound
$\|\mathcal E_o^{\rm paid}\|_{H^{-4/3}\to L^2}\le C_{\rm paid}$,
then the actual common-input paid contribution and its optional reordering obey
$$
 \begin{split}
 \|U_{R_\Omega}\mathcal E_o^{\rm paid}Z^{\mathcal S}\|
               _{H^{-4/3}\to L^2}
       &\le C_{\rm paid}z_{-4/3}^\#,\\
 \|[\mathcal E_o^{\rm paid},Z^{\mathcal S}]\|
               _{H^{-4/3}\to L^2}
       &\le C_{\rm paid}(z_{-4/3}^\#+z_0^\#).
 \end{split}
 \tag{MS.34}
$$
The rotation is an isometry and is charged once. These are new scalar product formulas using saved coordinate factors, not new evaluated balls. They avoid requiring a reconstruction of the root paid remainder from a selected norm upper. A sharper audit of a particular exact root chain may replace a whole bound, but the unchanged normalized WE number alone does not justify deleting the right $Z^{\mathcal S}$. Every retained term stays in its actual position and receives no norm from (MS.34).

## MS7. Existing inputs and the remaining distinction

No scientific source or successful receipt is modified by this note. The following small primary texts and completed receipts supply its exact identities.

| Primary | Exact role |
|---|---|
| P, P.8, P.23a and P.31--34 | Physical wave relabeling, original input primitive, oriented scalar Airy ratio and original cross reconstruction. |
| PF.20a--b and PF.27--28 | Complete primitive-plus-mean density, leading $\sigma/(i\epsilon)$ factor and original true maps. |
| FA.21, FA.28; WY.39--51 | Printed phase sign, physical $\tau=-\sigma$, same real first coefficient for both input signs, original leading diagonal position. |
| IC.4, IC.9, IC.16, IC.18--25 | The common right input operator, both density rank terms, selected chart, independently normalized coefficients. |
| TF.3, TF.12 and TFA | Complete degree192 root coefficient and actual $J_F=1024$, with the same two-window inverse. |
| WX actual, selected common input conclusion | Same selected $\mathcal S^{\pm1}$ on $L^2$ and $H^{-4/3}$, with original independent mean block. |
| CG and WE/WEA | Completed coefficient-only and paid normalized-branch budgets. Their retained obligations remain. |

The immutable text identities are:

- P: blob `11250cbb5f9921fdaa70791b6095c306e16bc5d7`, 35230 bytes, SHA256 `f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7`.
- PF: blob `e384f8711a44e1ad16dd05804faf65d62bf016c2`, 20413 bytes, SHA256 `5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026`.
- FA: blob `acfb0cfd9a2598c00a6b29c2db05041d0340cba9`, 27814 bytes, SHA256 `24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af`.
- IC: blob `bd4ed3ab5d72a10021df281542d080ef2f67fb0e`, 17274 bytes, SHA256 `4164e4a7a10db651654cf63b7ecf7772fc1ba2cb966da4f9347711156301ddee`.
- WY: blob `847a7dd335158482811561c2ed5e1aa7175e8797`, 30764 bytes, SHA256 `ebf8713508a11ef96decc5691056ea6eaa15d967d08b3a8af4b20c4284f6d1b3`.
- TF: blob `1052d454e98c613177919b7b19e472da1364a828`, 14951 bytes, SHA256 `652a9a2c2a9e0ccce1b07adae8848837ba579bec63d6ba5da21989a24b1bf5a3`.
- CG: blob `e1af6de6c25643fd1e7669824ca4db2c52155eaa`, 21714 bytes, SHA256 `a66ad4c41c831a1d5efd343874c11945edd4cc2b04a39752ddd99d8b16aa72ff`.

The completed TFA science is
[run43766881076](../notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json), blob
`3766aea85aba59230be3813b4b7634d318316e49`, 18206 bytes,
SHA256 `a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720`.
Its `complete_new_root_normalizer_conclusion.actual_J_F` is 1024 and
`same_inverse_on_both_windows` is true. The WX execution is
[run43763424840](../notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json), blob
`5121a599896025d90e2861450756a256aaba659d`, 43753 bytes,
SHA256 `e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12`.

The exact factor $Z^{\mathcal S}$ is now identified and bounded conditionally by already saved same-window coordinate norms. It is not a missing finite column. The optional strong reordering has the complete formulas (MS.20)--(MS.32). Neither choice pays an unverified actual finite Schur block, an independent physical mean/height port, the second reference/growing input, a complete incoming inverse, or the complete return $R_0$. In particular a successful scalar gap test retains its own argument and domain; it cannot silently replace the infinite factor or the ordered product in (MS.23).
