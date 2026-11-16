# R133 supplement: interpolation bounds for the same positive density intertwiner

2026-11-16, phase_inverse.

**Proved analytic refinement for the unchanged WIT operator.** The already certified complete sign difference and the already certified two sign-operator norms give new symbolic bounds for the same density intertwiner and its same inverse. Interpolation is used only between compatible bounds for that one operator. An exact resolvent identity also gives a strong difference bound that is linear in the original strong constant, multiplied by finite sign-window factors.

This note changes no source, target, selected chart, normalizer or finite projection. It does not recompute the DZA sign bound or any successful target, and evaluates no fractional power or new numerical product. Every full-density mean rank and the actual transported finite complement remain.

## WIR1. The same fixed operator and the complete saved inputs

Use WIT's fixed selected real chart and its nonmean carrier
$$
 H^s_0=(Id-\Pi)H^s,\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 Z=i\Pi_+-i\Pi_- .
$$
On this carrier define
$$
 \mathcal J=\mathcal S Z\mathcal S^{-1},\qquad
 D=\mathcal J-Z,\qquad
 R=\frac12ZD,\qquad
 \mathcal W=Id-R=\frac12(Id-Z\mathcal J).
 \tag{WIR.1}
$$
These are exactly WIT's operators. In particular $\mathcal W$ is not replaced by a new approximation to its first symbol.

The energy space and its metric are
$$
 \mathscr H=\dot H^{-1/2}_0,\qquad
 \|f\|_{\mathscr H}^2
       =\sum_{j\ne0}|4j|^{-1}|\widehat f_j|^2,\qquad
 G=IZ=|\partial|^{-1}.
 \tag{WIR.2}
$$
WIT's exact density pairing proves that $\mathcal W$ is self-adjoint in this energy metric, is bounded below by $Id/2$, and has a genuine onto inverse
$$
 \|\mathcal W_{\mathscr H}^{-1}\|_{\mathscr H\to\mathscr H}\le2 .
 \tag{WIR.3}
$$
The notation does not assert ordinary $L^2$ self-adjointness.

Take complete positive upper constants
$$
 \begin{aligned}
 J_0&\ge\|\mathcal J:H^0_0\to H^0_0\|,\\
 J_-&\ge\|\mathcal J:H^{-4/3}_0\to H^{-4/3}_0\|,\\
 C_D&\ge\|D:H^{-4/3}_0\to L^2_0\|.
 \end{aligned}
 \tag{WIR.4}
$$
The existing DZA full-circle bounds are valid such constants after restriction to nonmeans. The input for $C_D$ is its complete sign-difference bound, including the independently paid full-density mean contribution. No outgoing subtotal or isolated $T_oD$ bound is used in its place.

For exact input identification, the DZA science is blob
**67b41ac717207f8696b637c667fb210088fca638**, 26909 bytes, SHA256
**05036749a28c55499e2ed6fe47019cd31f4438652e3e6ab1319e6f9f2f2c4dba**,
at
[the unique complete science](../notes/fourth_angle_global_sign_budgets_ci/run-43773671216-1/actual-scientific-conclusion.json).
Its complete same-operator records are:

| Constant in this note | Exact original path within that science |
|---|---|
| $J_0$ | complete_new_commonout_paid_conclusion.complete_ZS_L2_upper |
| $J_-$ | complete_new_commonout_paid_conclusion.complete_ZS_Hminus4_3_whole_upper |
| $C_D$ | complete_new_strong_sign_conclusion.complete_D_Hminus4_3_to_L2_upper |

The second path is the already selected complete negative-window record, with its original full candidates and scope. It is not reselected from different entries here. A later numerical consumer must read all three entire records and take their outward upper endpoints; the present text does not evaluate them.

Define only the positive symbolic combinations
$$
 d_0=1+J_0,\qquad d_-=1+J_-.
 \tag{WIR.5}
$$
Since $Z$ is an isometry on every nonmean Bessel space, these bound the same $D:L^2_0\to L^2_0$ and $D:H^{-4/3}_0\to H^{-4/3}_0$.

## WIR2. Exact Bessel interpolation and the energy comparison

The two compatible input-window bounds for $D$ give, at input index $-1/2$,
$$
 \|D:H^{-1/2}_0\to L^2_0\|
     \le d_0^{5/8}C_D^{3/8}.
 \tag{WIR.6}
$$
The interpolation parameter is $(1/2)/(4/3)=3/8$. No output regularity of a different operator is inserted.

For the fixed input $H^{-4/3}_0$, interpolate the two output-window bounds in (WIR.4)--(WIR.5). At output index $-1/2$ this gives
$$
 \|D:H^{-4/3}_0\to H^{-1/2}_0\|
     \le d_-^{3/8}C_D^{5/8}.
 \tag{WIR.7}
$$
These are the exact constant-one interpolation inequalities for the Bessel Hilbert scale. For example, on finite Fourier sums the first follows from the analytic operator family $D\Lambda^{(4/3)z}$ and the two boundary estimates. For the second use
$\Lambda^{-4/3+(4/3)z}D\Lambda^{4/3}$ with the input represented in $L^2$.
The complex imaginary powers are unitary. Extension by the compatible distributional operator gives (WIR.6)--(WIR.7).

The physical lowest nonzero frequency is four, not 97 or the moving normalizer cutoff. Direct comparison of the weights gives
$$
 \|f\|_{H^{-1/2}}
        \le\|f\|_{\mathscr H}
        \le r_4\|f\|_{H^{-1/2}},\qquad
 r_4=\left(\frac{17}{16}\right)^{1/4},
 \tag{WIR.8}
$$
and
$$
 \|f\|_{\mathscr H}\le\frac12\|f\|_2,\qquad
 \|f\|_{H^{-4/3}}\le\|f\|_{\mathscr H}.
 \tag{WIR.9}
$$
In (WIR.8) the largest ratio is
$\sup_{j\ne0}(\Lambda_j/|4j|)^{1/2}=r_4$.
All these comparisons are on nonmeans.

Put
$$
 L=d_0^{5/8}C_D^{3/8},\qquad
 N=r_4d_-^{3/8}C_D^{5/8}.
 \tag{WIR.10}
$$
Then the two typed gains are
$$
 \|D:\mathscr H\to L^2_0\|\le L,\qquad
 \|D:H^{-4/3}_0\to\mathscr H\|\le N.
 \tag{WIR.11}
$$
The factors $r_4$ and $1/2$ have different origins and are not interchanged. No high-frequency assumption on the true transported input is used.

## WIR3. Two bounds for the same inverse

For $f\in L^2_0$, first solve in the energy space:
$$
 u=\mathcal W_{\mathscr H}^{-1}f.
$$
Equations (WIR.3) and (WIR.9) give
$\|u\|_{\mathscr H}\le\|f\|_2$.
The equation $u=f+Ru$ and (WIR.11) now show $u\in L^2_0$ and
$$
 \boxed{\quad
 \|\mathcal W^{-1}:L^2_0\to L^2_0\|
       \le 1+\frac L2=:K_{0,\rm int}.
 \quad}
 \tag{WIR.12}
$$
This is a regularity bootstrap from the already existing energy inverse. It is not an $L^2$ coercivity assertion.

For $f\in H^{-4/3}_0$, do not place $f$ in $\mathscr H$. Instead construct
$$
 u=f+\mathcal W_{\mathscr H}^{-1}Rf .
 \tag{WIR.13}
$$
The second term is well defined because $Rf\in\mathscr H$ by (WIR.11). It lies in $H^{-4/3}_0$ by (WIR.9), and the compatible operator equation gives $\mathcal Wu=f$.

If $\mathcal Wu=0$ in this negative window, then $u=Ru\in L^2_0$ by the original strong bound in (WIR.4), hence $u\in\mathscr H$. Energy uniqueness forces $u=0$. Thus (WIR.13) gives the same two-sided inverse, agreeing with (WIR.12) and WIT on the common domain. Its bound is
$$
 \boxed{\quad
 \|\mathcal W^{-1}:H^{-4/3}_0\to H^{-4/3}_0\|
       \le 1+N=:K_{-,\rm int}.
 \quad}
 \tag{WIR.14}
$$
Indeed the correction in (WIR.13) has norm at most $2(N/2)\|f\|_{H^{-4/3}}$.

The forward operator has separate complete bounds directly from its exact definition:
$$
 \boxed{\quad
 \|\mathcal W\|_0\le\frac{1+J_0}{2},\qquad
 \|\mathcal W\|_{-4/3}\le\frac{1+J_-}{2}.
 \quad}
 \tag{WIR.15}
$$
These forward bounds are not assigned to the inverse. They can be much different from (WIR.12)--(WIR.14), and each must be used on its actual side of an ordered product.

## WIR4. A complete strong difference with a single power of the strong input

The rough-input construction (WIR.13) already gives
$$
 (\mathcal W^{-1}-Id)f
       =\mathcal W_{\mathscr H}^{-1}Rf .
$$
Set $v=\mathcal W_{\mathscr H}^{-1}Rf$. Its equation is $v-Rv=Rf$, so, with every indicated window retained,
$$
 \boxed{\quad
 \mathcal W^{-1}-Id
       =R+R\mathcal W_{\mathscr H}^{-1}R:
                     H^{-4/3}_0\longrightarrow L^2_0 .
 \quad}
 \tag{WIR.16}
$$
The first $R$ in the sum uses the original strong bound $C_D/2$.
In the three-factor term the right $R$ maps $H^{-4/3}$ to $\mathscr H$ with bound $N/2$, the middle inverse has energy norm at most two, and the left $R$ maps $\mathscr H$ to $L^2$ with bound $L/2$. This proves
$$
 \|\mathcal W^{-1}-Id\|_{H^{-4/3}\to L^2}
       \le\frac{C_D+LN}{2}.
 \tag{WIR.17}
$$
There is no illegal embedding of the original rough $f$ into the energy space and no interpolation of two different inverses.

The same expression can be collected as a positive scalar identity:
$$
 \boxed{\quad
 C_{\rm res}
    =\frac{C_D}{2}
        \left[1+r_4d_0^{5/8}d_-^{3/8}\right]
    =\frac{C_D+LN}{2}.
 \quad}
 \tag{WIR.18}
$$
This uses the exact exponents $3/8+5/8=1$ before taking any numerical upper. It does not subtract upper bounds. It is a bound for the entire strong difference of the same inverse.

Another complete candidate follows from
$\mathcal W^{-1}-Id=\mathcal W^{-1}R$ with its true output-side inverse:
$$
 C_{\rm prod}=\frac12 K_{0,\rm int}C_D .
 \tag{WIR.19}
$$
The original WIT candidate $K_WC_D/2$, $K_W=1+C_D/2$, remains valid as well. These are all whole bounds for one and the same strong map. A later consumer may compare complete saved outward candidates for this target. It must not replace $K_{0,\rm int}$ by the forward bound in (WIR.15).

If the exact $C_D$ chosen as a norm upper is zero, the same statements have their limiting elementary interpretation: $D=0$, $\mathcal W=Id$, and the strong difference vanishes. No reciprocal of $C_D$ occurs in any formula.

## WIR5. What changes in later ordered estimates, and what stays present

WIT's reflections and true projections are unchanged:
$$
 \mathcal W\mathcal J=Z\mathcal W,\qquad
 [\mathcal W,R_b]=0,\qquad
 \widehat P_{97}
       =\mathcal W\mathcal S P_{97}
                    \mathcal S^{-1}\mathcal W^{-1}.
 \tag{WIR.20}
$$
The further source normalization still uses
$\widetilde P_{97}=\mathcal A^{-1}\widehat P_{97}\mathcal A$.
No ordinary Fourier cutoff is substituted for these actual projections. Their full nonmean rank-192 and reflected rank-96 complements are retained.

For example, WBP's physical normalized remainder has the exact structure
$$
 \mathcal B^{-1}\left[
 Q_a\mathcal R_{\rm ss}
 +Q_aT_i(\mathcal W^{-1}-Id)\mathcal A
 +E_\partial^{\rm fr}\mathcal W^{-1}\mathcal A
 \right].
 \tag{WIR.21}
$$
If its complete physical input $C_\partial$ has been admitted, a corresponding new whole positive candidate can use
$$
 K_{B,0}\left[
    C_{\rm alg}
    +K_{i,0}^{\rm fwd}C_{\rm res}K_{A,-}
    +C_\partial K_{-,\rm int}K_{A,-}
 \right].
 \tag{WIR.22}
$$
Here $C_{\rm alg}$ denotes one declared complete bound for the algebraic projected remainder in WBP, such as its collected or uncollected whole candidate. Equation (WIR.22) does not mix separate entries of those two recipes.

Only constants in the estimate have changed. The actual left and right coordinates in (WIR.21) are exactly the same operators as in WBP. Thus complete candidates for that same coordinate realization can be compared after all retained terms are included. This differs from comparing WBN and WBP remainders with their different left normalizers.

In a projection or coordinate bound involving $\mathcal W$ itself, use its forward window from (WIR.15); when $\mathcal W^{-1}$ occurs, use its inverse window from (WIR.12) or (WIR.14). For example the order
$\mathcal A^{-1}\mathcal W\mathcal S P_{97}
 \mathcal S^{-1}\mathcal W^{-1}\mathcal A$
keeps one forward and one inverse factor. No common numerical label makes these factors interchangeable.

The auxiliary mean extension remains explicitly
$$
 \widehat{\mathcal W}=\Pi+\mathcal WP,\qquad
 \widehat{\mathcal W}^{-1}
       =\Pi+\mathcal W^{-1}P .
 \tag{WIR.23}
$$
Its forward bound is $\max\{1,(1+J_s)/2\}$ in the corresponding window; its inverse bounds above already include one. This extension is not the uncompressed formula $(Id-Z_{\rm full}\mathcal J_{\rm full})/2$.

The exact full sign identity still has its mean column:
$$
 \widehat{\mathcal W}\mathcal J_{\rm full}
       \widehat{\mathcal W}^{-1}
    =Z_{\rm full}
       +(\mathcal W\Delta_{\rm full}1)\otimes\Pi .
 \tag{WIR.24}
$$
Neither this column nor the physical relation
$K_H=R_a-2h_H\Pi$ is removed by the refined nonmean bounds. The genuine density rank $(h_H-1)\otimes\rho_i$ in the physical primitive row remains a complete term. The stored physical means, actual mean/amplitude equations, metric-parameter column, independent source ports and graph-domain conditions retain their original meanings.

## WIR6. Boundary of a later numerical readout

A later authorized calculation would read the three entire records in WIR1, their common selected scope and complete provenance. It could then evaluate the new positive powers and products for (WIR.10), the two inverse bounds, the two forward bounds and the complete strong candidates. None of those expressions requires an old sign computation, a KAM map, an old ray or a new exponential.

For each window, compare only complete candidates for that same map and window. For the strong difference compare only entire candidates for $\mathcal W^{-1}-Id$. A refinement of a norm is not a new operator identity and does not remove the declared physical input qualifications of (WIR.21). All selections must preserve their complete input domain and the original same-operator inverse.

No new number, actual comparison, cutoff, contraction, physical incoming inverse or finite matching inverse is asserted in this note.

| Primary and exact role | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WIT: energy positivity, same inverse and full mean extension | 68737e28209551cab5b45aa251869892bc51b380 | 21308 | 13c5972c82dd1af1ded73ccdfdd6b8ba69da3c3a84bb278aea602d3dd90ba437 |
| DZA: complete same sign operator in both windows and its full strong difference | 67b41ac717207f8696b637c667fb210088fca638 | 26909 | 05036749a28c55499e2ed6fe47019cd31f4438652e3e6ab1319e6f9f2f2c4dba |
| WBP: unchanged source/target normalizers and complete physical remainder | 54f859b305861a1c4be4be7826c059e1e4ffc3e8 | 18114 | 19f0182fb19cb3842948ee427993f7478af0557f2ec790c7c2f8ce5849015a7e |
| WPL: actual physical primitive row, density mean and restricted strong error | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |

Only immutable text and saved record paths have been read. No numerical function or successful producer is executed by this proof.
