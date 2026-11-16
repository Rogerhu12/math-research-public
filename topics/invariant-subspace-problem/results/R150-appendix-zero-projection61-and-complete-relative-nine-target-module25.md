# R150: zero projection length 61 and generation of the full 25-dimensional relative module by the nine original squares

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Completed conclusions

Keep the original primitive seventeen-equation map and its complete degree-three source dictionary:
$$
A:\mathbb Q[s]^{6188}\longrightarrow V=\mathbb Q[s]^{4367},
\qquad L=\operatorname{im}A.
$$
Use the original binomial coordinates
$$
z_j=\sum_{a=0}^j\binom ja(-s)^{j-a}m_a,\qquad
c=z_0,\quad d=z_1,
$$
and the coordinate summand
$$
W=(z_2,\ldots,z_{10})^2_{\le5}\subset V,\qquad
\operatorname{rank}W=4212.
$$
Define the relative module and the original nine classes by
$$
\mathcal T=W/(L\cap W),\qquad t_j=z_j^2,\qquad 2\le j\le10.
$$

The new, independently executed zero-chart calculation proves that the complete original projection to $V/W$ has positive Smith exponents at $s=0$
$$
\boxed{1,1,1,1,3,4,4,4,5,6,6,7,8,10.}
\tag{1.1}
$$
Its torsion length is 61, its largest positive exponent is 10, and its generic free rank is thirteen. The original full zero length is 66, so
$$
\boxed{\operatorname{length}_{\mathbb Q[s]_{(s)}}\mathcal T_{(s)}=5.}
\tag{1.2}
$$
This is a new zero-chart calculation with the original $K$; no infinity spectrum or reversal symmetry is used.

Combining (1.2) with the completed other local calculations gives
$$
\boxed{\dim_{\mathbb Q}\mathcal T=5+6+6+8=25.}
\tag{1.3}
$$
The original nine classes generate this entire rational relative module:
$$
\boxed{\mathcal T=\sum_{j=2}^{10}\mathbb Q[s]\,[t_j].}
\tag{1.4}
$$
In particular, if
$$
h_*=s^3F_+^2F_-^2E_8,\qquad m_*=\operatorname{mon}(h_*),
$$
then
$$
\boxed{
\chi_{\mathcal T}(s)=s^5\operatorname{mon}(F_+^2F_-^2E_8)
=s^2m_*(s),\qquad
\operatorname{ann}_{\mathbb Q[s]}\mathcal T=(m_*).
}
\tag{1.5}
$$
Here the characteristic polynomial means the characteristic polynomial of multiplication by $s$ on the 25-dimensional $\mathbb Q$-space. Each individual original class has the same minimal annihilator $m_*$, of degree 23.

A useful consequence of (1.4) is the original-source inclusion
$$
\boxed{h_*W\subseteq L.}
\tag{1.6}
$$
It applies to the whole degree-at-most-five normal-square summand, not only its nine diagonal squares. It is an existence statement in the original degree-three source module; no new expanded array of 4212 sources is claimed.

## 2. The projection is the original quotient

Let
$$
C_{\mathbb Q}=V/L,\qquad
C_P=(V/W)/((L+W)/W).
$$
The [original generic-image bridge](R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md) proves
$$
\operatorname{rank}_{\mathbb Q(s)}A=4354,\qquad
\operatorname{rank}_{\mathbb Q(s)}P=142,\qquad
W_{\mathbb Q(s)}\subseteq L_{\mathbb Q(s)}.
$$
Thus $\mathcal T$ is a finite torsion $\mathbb Q[s]$-module, and both $C_{\mathbb Q}$ and $C_P$ have generic free rank thirteen.

The exact original-source sequence is
$$
0\longrightarrow\mathcal T\longrightarrow C_{\mathbb Q}
\longrightarrow C_P\longrightarrow0.
\tag{2.1}
$$
At every monic irreducible $f$, its torsion terms form a short exact sequence. One can see the right-hand surjectivity directly: if a preimage maps to a torsion class, a nonzero polynomial multiple of it lies in $\mathcal T$; another nonzero polynomial kills that element because $\mathcal T$ is torsion. The preimage is therefore torsion itself.

Consequently, for the monic full and projected determinantal divisors,
$$
\operatorname{length}_{\mathbb Q[s]_{(f)}}\mathcal T_{(f)}
=v_f(\Delta_A)-v_f(\Delta_P).
\tag{2.2}
$$
This is the [original projection-divisor exact sequence](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md), not a comparison of unrelated matrices.

At zero the true projected sources can be compressed to 224 rows: 170 pure-tangent source rows and 54 actual one-normal rows. The 155 target coordinates consist of 20 pure and 135 one-normal monomials. The present computation verifies this compression in the zero chart as follows.

The original source and output counts, ordered by normal degree, are
$$
(170,918,2295,2805),\qquad
(20,135,450,990,1485,1287).
$$
All seventeen pure-plane equations are reconstructed as whole polynomials. Their common parameter factor has order two at zero. The selected original equation is zero-based equation 8; after separating that common factor, its denominator polynomial has nonzero constant 2400. Thus its ratios with the other pure-plane equations are regular in $\mathbb Q[[s]]$.

For each of the 54 one-normal multiplier slots, the other sixteen original equation rows are the corresponding regular multiples of the retained actual row. The script verifies all 918 projected rows and the whole-polynomial ratio identities. It eliminates 864 redundant rows by these regular source operations. The common $s^2$ factor remains in each retained source; it is never divided away.

All remaining 5100 source rows have identically zero projection, by the complete original normal-degree support. The script checks their coefficients as well. Thus the 224-row matrix represents exactly the original projected image over $\mathbb Q[[s]]$, with all 6188 sources retained or accounted for by exact identities.

The source and target binomial transformations are degree-preserving polynomial units. The fixed nonzero rational scales between the physical and primitive seventeen equations are the scales of the pinned original zero proof. These operations preserve the original module and the degree-three multiplier bound.

## 3. Actual complete zero Smith calculation

The calculation uses exact rational Taylor coefficients through degree eleven. Its constant projection rank is 128, leaving 27 constant heads. Each subsequent stage selects a true constant unit block, checks its series solve, retains the complete residual matrix, and divides by $s$ only after the complete residual constant term is zero.

The actual positive exits are:

| Order | Newly exiting directions | Cumulative positive directions |
|---:|---:|---:|
| 1 | 4 | 4 |
| 2 | 0 | 4 |
| 3 | 1 | 5 |
| 4 | 3 | 8 |
| 5 | 1 | 9 |
| 6 | 2 | 11 |
| 7 | 1 | 12 |
| 8 | 1 | 13 |
| 9 | 0 | 13 |
| 10 | 1 | 14 |

Their weighted sum is
$$
4+3+12+5+12+7+8+10=61.
$$
The fourteen exits bring the total rank to $128+14=142$, the independently proved generic rank of this same original projection. No positive direction remains. This is the completeness criterion; the value 61 is not inferred from a finite collection of lower bounds alone.

The transformations also retain the original 155-coordinate cochains. The script checks every original source coefficient below each positive exponent and verifies each nonzero leading block. It separately verifies the thirteen remaining finite jets through order eleven. The actual gates are:

| Original verification | Actual result |
|---|---:|
| Zero product coordinates on the original 6188 sources | 1342796, all zero |
| Leading product coordinates of all positive groups | 86632, all verified |
| Constant and free leading heads together | rank 27 |
| Original one-normal projected rows | all 918 verified |
| Original higher-normal projected source rows | all 5100 exactly zero |
| Positive directions that actually exited | all 14 |
| Original remaining finite jets | 13, verified through order 11 |

The remaining finite jets are not asserted to be a specified infinite formal-kernel basis. Completeness of the positive spectrum follows instead from the fourteen actual exits and the independent generic rank.

The [complete original full zero spectrum](R150-appendix-zero-complete-positive-smith-spectrum-length66-and-sharp-cubic-target-factor.md) is
$$
1^4,3,4^3,5,6,7,8,10,11,
$$
of length 66. Applying (2.2) to the new projection length 61 proves (1.2).

At this point the number five is only the length of the relative zero module. Subtracting the two full spectra term by term would not determine the invariant factors of the kernel in (2.1).

## 4. All finite support of the rational relative module

The other local terms in (2.2) are already complete original-source conclusions:

| Finite factor | Full local length | Projected local length | Relative local length | Contribution to $\dim_{\mathbb Q}\mathcal T$ |
|---|---:|---:|---:|---:|
| $s$ | 66 | 61 | 5 | 5 |
| $s-2$ | 12 | 12 | 0 | 0 |
| $s+6$ | 12 | 12 | 0 | 0 |
| $F_+$, degree 3 | 8 | 6 | 2 | 6 |
| $F_-$, degree 3 | 8 | 6 | 2 | 6 |
| $E_8$, degree 8 | 5 | 4 | 1 | 8 |
| Outside these factors | equal full and projected valuations | equal | 0 | 0 |

The zero row is the new calculation. The $s-2$ and $s+6$ rows follow from the [complete two-point theorem](R150-appendix-two-complete-third-connection-smith12-and-all-original-square-local-membership.md) and the [complete minus-six theorem](R150-appendix-minus-six-local-smith-length12-and-original-nine-target-membership.md); both prove the stronger local inclusion of the whole $W$.

The [exact critical square-target theorem](R150-appendix-critical-original-square-targets-exact-local-exponents.md) proves the three critical rows. It first uses only the genuine complete-projection lower bounds 6, 6 and 4. Actual original dual target pairings then force relative lengths 2, 2 and 1; only afterwards does it conclude the complete projected spectra $(3,3),(3,3),(2,2)$. Thus no unproved identification of a low slice with the whole projection is used here.

Finally, the [completed affine divisor theorem](R150-appendix-exact-affine-divisor298-unmultiplied-nine-sources-and-rank-one-bell16.md) proves
$$
\Delta_A=\operatorname{mon}(K_{178})\Omega,\qquad
K_{178}=s^{66}(s-2)^{12}(s+6)^{12}F_+^8F_-^8E_8^5,
$$
where the exact original projected outside divisor is $\Omega$, of degree 120 and coprime to
$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8.
$$
The full and projected valuations therefore agree at every factor outside $\Sigma_0$, so $\mathcal T$ has no other finite support.

Multiplying the residue-field degrees by the local lengths gives (1.3). It also gives the characteristic polynomial in (1.5) and the complete projected determinantal divisor
$$
\boxed{
\Delta_P=
\operatorname{mon}\!\left(
s^{61}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4
\right)\Omega,\qquad \deg\Delta_P=273.
}
\tag{4.1}
$$
Indeed $298-273=25$. This is the full original projected divisor, not the determinant of a chosen square submatrix.

## 5. The integral carrier used for the nine-target lower bound

A field rank alone cannot prove (1.4). The required integral bridge is the already completed [coefficient-127 and exact-source theorem](R150-appendix-unique-coefficient127-torsion-and-integral-nine-square-sources.md). We spell out its role.

Put
$$
D=\mathbb Z_{(127)},\qquad p=127,\qquad k=\mathbb F_{127}.
$$
Use the same original primitive integer matrix over $D[s]$, and set
$$
V_D=D[s]^{4367},\quad
L_D=\operatorname{im}_{D[s]}A,\quad
N_D=V_D\cap\operatorname{im}_{\mathbb Q(s)}A,\quad
C_D=N_D/L_D.
$$
The intersection is in the original rational generic output space. It is $p$-saturated: $N_D\cap pV_D=pN_D$. A unit-leading original maximal minor annihilates $C_D$, so $C_D$ is a finite $D$-module.

The completed integral theorem proves
$$
T_p:=C_D[p^\infty]\simeq k[s]/(s+64),
\qquad pT_p=0.
\tag{5.1}
$$
The exact zero quotient defect $J_{127}=0$ identifies $C_D/pC_D$ with the complete original field torsion module. These facts concern the finite carrier $C_D$, not the full cokernel with its thirteen free parameter directions.

It also proves genuine original polynomial source identities over $D[s]$:
$$
h_*t_j\in L_D,\qquad j=2,\ldots,10.
\tag{5.2}
$$
The original integer polynomial has degree 23 and leading coefficient 3125, a unit in $D$. Its actual value satisfies
$$
h_*(63)\equiv44\pmod{127},\qquad
m_*(63)\equiv55\pmod{127}.
\tag{5.3}
$$
Thus multiplication by $h_*$ is invertible on $T_p$. The original 24 coefficients, integer Horner evaluation and factored evaluation behind (5.3) are verified in the [exact evaluation audit](../notes/2026-11-16-r150-original-hstar-at63-exact-integer-cross-audit-789f.json).

Now let
$$
M_D=\sum_{j=2}^{10}D[s]\,[t_j]\subset C_D.
$$
Equation (5.2) kills $M_D$ by the monic polynomial $m_*$, so it is a finite $D$-module. Any coefficient-prime torsion in $M_D$ would belong to $T_p$, but $h_*$ both kills that intersection and acts invertibly on it. Therefore
$$
M_D\cap T_p=0.
$$
A finite torsion-free module over the DVR $D$ is free. Consequently $M_D$ is a finite free $D$-module.

## 6. The actual 25-dimensional field image closes the rational span

The [complete original nine-target calculation at 127](R150-appendix-original127-nine-target-module-twentyfive-and-minimal-hstar.md) computes the image of these same nine classes in $C_D/pC_D$, with the original target labels and complete free-tail constraints. Its joint parameter-stable span has dimension 25. Its verification includes
$$
7245\text{ original finite-window products},\quad
7475\text{ action-intertwining products},\quad
2691\text{ seed-span coordinates}.
$$
In particular, there is a surjection
$$
M_D/pM_D\longrightarrow \overline M,
\qquad \dim_k\overline M=25.
$$
Since $M_D$ is free,
$$
\operatorname{rank}_D M_D=\dim_k M_D/pM_D\ge25.
\tag{6.1}
$$

After extending coefficients to $\mathbb Q$, the original classes lie in $\mathcal T$, because every $t_j$ lies in $W$. The rationalized finite carrier embeds as the torsion part of the original rational cokernel, so this gives the genuine injection
$$
M_D\otimes_D\mathbb Q\hookrightarrow\mathcal T.
$$
By (1.3),
$$
\operatorname{rank}_D M_D
=\dim_{\mathbb Q}(M_D\otimes_D\mathbb Q)\le25.
\tag{6.2}
$$
Equations (6.1) and (6.2) give equality throughout:
$$
\operatorname{rank}_D M_D=25,\qquad
M_D\otimes_D\mathbb Q=\mathcal T.
$$
This proves (1.4). It also shows that the map $M_D/pM_D\to\overline M$ is an isomorphism. The dimension statement is thus transported through a proved torsion-free original integral module; it is not a direct promotion of a finite-field zero or rank.

The same integral theorem proves, separately for every $j$,
$$
D[s]\,[t_j]\simeq D[s]/(m_*).
$$
Thus each rational cyclic submodule has dimension 23 and annihilator exactly $m_*$. Their joint module, now equal to $\mathcal T$, is killed by $m_*$ and contains each one of them. Its annihilator is therefore also exactly $m_*$, proving the second assertion of (1.5).

At zero this implies that the five-dimensional relative primary has largest exponent three. It does not distinguish the possible partitions $(3,2)$ and $(3,1,1)$. Neither the new projected spectrum nor the preceding field image calculation is used to assign one of those partitions without another argument.

## 7. Consequences for original high-normal targets and the remaining boundary

Every class of $W$ is, by (1.4), a polynomial combination of the nine original square classes. Since all nine are killed by $h_*$, (1.6) follows. Explicitly, for each original $w\in W$ there are original degree-at-most-three source coefficients with
$$
h_*w=A x_w,\qquad x_w\in\mathbb Q[s]^{6188}.
$$
This keeps the same original seventeen equations and the same truncated multiplier family. The statement does not construct those coefficients or bound their heights.

For each individual target, its 23-dimensional cyclic submodule has codimension two in the 25-dimensional relative module. The quotient by that individual cyclic submodule has characteristic polynomial $s^2$, because all critical relative primaries are already cyclically generated by each target. This does not determine the invariant-factor partition of that quotient.

The [rational bound 8391 and normalized rank-one Bell sixteenth-power identity](R150-appendix-exact-affine-divisor298-unmultiplied-nine-sources-and-rank-one-bell16.md) remain valid for the already stated targets. The uniform bound 8515 there has the quantifier of reducing already existing $31$-integral sources or congruence solutions. This appendix does not assign either number to newly expanded sources for every element of $W$, nor transfer $127$-integrality to $31$-integrality.

The new result closes the entire rational relative module in this normalized rank-one family. It does not remove the mean-rank-one restriction from the original Bell or Jacobian statement. The unrestricted non-rank-one critical branches and the remaining coefficient-31 exponent problem retain their separate definitions and proof obligations.

## 8. Reproducible execution identities

The zero computation was executed in the completed independent run
[43795759185](https://github.com/Rogerhu12/math-research-public/actions/runs/43795759185),
job 133064092311, step $\texttt{zero-small-original-projection-smith}$, against execution source
$\texttt{7f300e57c9165ae28d01d03846a4bc7000a81ee7}$.
The mathematical elapsed time was 80.048120387 seconds; the runner wall time was 80.165932465 seconds. The process exited zero.

The full mathematical output was read from the completed job log. Under the current storage rule, the repository keeps only the [execution identity manifest](../notes/r150-zero-projection-execution-789f/43795759185-zero-small-original-projection-smith.json), not a newly committed computational-output JSON or the temporary matrix arrays.

| Identity | Exact value |
|---|---|
| Original temporary raw receipt | 22533 bytes |
| Raw SHA256 | 347c76c0e0566d69f719b83442392ef749df2626071db7eb2e2f0260d79e8675 |
| Semantic binding | 494fc0263aae77866972907a814ed043a3b468e6a21d22caf6066c85aa367647 |
| Temporary manifest SHA256 | bb5033f51d422fa0d61dc2648ff40b0f8322c25e0af722021fb8ae6890ee4d88 |
| Original 6188-source dictionary SHA256 | 8000661ac9a1840a3abb88b413680eb740175338b7c6d1693316fefc6d1013ba |
| Original 4367-output dictionary SHA256 | eab90fae08c44a124b16e768742d0c54ccfaea3e6a69aea614715ef91ed1e79a |
| Original verification logical binding | 774fb1de2d905b6f818bb3069bf8a06b77e1d630984f8230c9a747895bbfc018 |

The executable [zero projection consumer](../notes/2026-11-16-r150-zero-small-original-projection-smith-789f.py) has SHA256
$\texttt{81eb7dd4ed337b2e84f4fd618139c98b72f01b7a9523fa4612db9f2a9b45df87}$.
Its [input manifest](../notes/2026-11-16-r150-zero-small-original-projection-smith-inputs-789f.json) and [interface](../notes/2026-11-16-r150-zero-small-original-projection-smith-interface-789f.md) fix the zero parameter, all original dictionaries, exact arithmetic, fourteen-exit completion gate and all-source verification.

It imports the previous infinity consumer only for its generic exact-series Smith routines. The actual coefficient generator is called with the zero chart and the unreversed original $K$. The receipt explicitly records that no infinity-projection value was used, that the zero length was not prefilled, and that the joint rational conclusion was not claimed by that calculation alone. Sections 4–6 provide the separate argument needed for that conclusion.
