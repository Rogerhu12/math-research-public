# R150: the complete global second coefficient-31 saturation is U7

Author: ChatGPT (AI), literature_audit.  
Date: 2026-11-15 UTC.

## 1. Exact conclusion

Let $p=31$, $D=\mathbf Z_{(31)}$, $R_D=D[s]$, and retain the original
$4367\times6188$ polynomial matrix $A$. Write
$$
L=\operatorname{im}_{R_D}A,\qquad
N=R_D^{4367}\cap\operatorname{im}_{\mathbf Q(s)}A,\qquad C=N/L.
$$
The finite $D$-module $C$ and its embedding modulo $p$ into the complete original
finite-field cokernel are those of the
[finite coefficient-module construction](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md).
For $e\geq1$ define the canonical submodule
$$
I_e(A)=\operatorname{im}\bigl(C[p^e]\longrightarrow C/pC\bigr).
\tag{1.1}
$$
It is viewed inside the original 315-dimensional finite-field torsion module;
the extra one-dimensional quotient defect is not included in $C/pC$.

The actual complete global197 calculation proves
$$
\boxed{I_2(A)=U_7,\quad \dim_{\mathbf F_{31}} I_2(A)=7,\quad
\chi_{I_2}(s)=(s-1)^2(s-2)^5.}
\tag{1.2}
$$
Here $U_7$ is the previously paid seven-dimensional space of genuine divided
original sources. This equality is over the full polynomial parameter ring,
with every original source and every primary component retained.

The [complete first coefficient Bockstein theorem](../notes/2026-11-14-r150-complete-polynomial-bockstein-obstruction-789f.md) already proved the image to be
$$
I_1(A),\qquad \chi_{I_1}(s)=(s-1)(s-2).
\tag{1.3}
$$
Consequently the exact multiplicity of coefficient-prime exponent $2$ is five:
$$
\boxed{\dim(I_2/I_1)=5,\qquad
\chi_{I_2/I_1}(s)=(s-1)(s-2)^4.}
\tag{1.4}
$$
Thus exponent $2$ contributes one direction on the $s=1$ primary and four on
the $s=2$ primary, and none on any other primary. This is an exact global
multiplicity statement, not a lower bound from selected columns.

The previously proved bounds remain
$$
\deg\Delta_{\rm aff}\leq299,\qquad \deg\mu\leq21,\qquad
\deg(\mu h_*)\leq44.
\tag{1.5}
$$
This calculation does not lower them. Further coefficient-prime torsion, if
present, must have exponent at least $3$.

## 2. Why 197 divided columns are a complete input

Put
$$
S_e=\{x\in R_D^{6188}:Ax\in p^eR_D^{4367}\}.
$$
The
[complete original $p^2$ source theorem](../notes/2026-11-14-r150-full-p2-source-envelope-by-197-unscaled-columns-789f.md)
proves, by two finite source eliminations,
$$
S_2=H_{\rm nat}+K_{\rm low}
       +\sum_{j=2}^{198}\widetilde\kappa_jR_D,
\tag{2.1}
$$
where
$$
H_{\rm nat}=p^2R_D^{6188}+p\kappa_1R_D+p\kappa_2R_D
                 +\sum_{i=3}^{9}\kappa_iR_D,
\quad
\widetilde\kappa_j=\widehat K_j-p\widehat q_{1,j}.
$$
The 1632 columns in $K_{\rm low}$ are exact original syzygies. The high
$K_1,\ldots,K_{202}$ together with them are the complete finite-field polynomial
kernel. The four exceptional first-image relations and the source initial
value $\bar\kappa_7=22K_1$ are part of the proof of (2.1), not dimension guesses.

Let $b_i=A\kappa_i/p^{e_i}$, where
$$
(e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4),
\qquad
R_{2,j}=A\widetilde\kappa_j/p^2.
$$
The equivalent exact colon theorem is
$$
B_2=[A,b_1,\ldots,b_7,pb_8,p^2b_9,R_{2,2},\ldots,R_{2,198}],
\qquad
\boxed{\operatorname{im}_{D[s]}B_2=(L:p^2).}
\tag{2.2}
$$
All these vectors lie in $N$, since a nonzero power of $p$ times each belongs to
$L$. Therefore
$$
C[p^2]=(L:p^2)/L.
\tag{2.3}
$$
Reducing (2.2) into the complete original finite-field cokernel kills the $A$
columns, $pb_8$, and $p^2b_9$. Its image is exactly the polynomial span of
$U_7$ and the 197 classes $[R_{2,j}]$.

A different valid first correction $q_{1,j}$ changes the corresponding divided
class by an element of $I_1(A)\subset U_7$. Indeed the difference of the two
corrections is a finite-field kernel, and its image divided by $p$ is precisely
a first Bockstein class. Thus the complete span in (2.2) is unaffected by this
choice. Actual higher carries still require the chosen integer representatives.

## 3. What the actual calculation retained

The new run restored the original graph, original normal forms, the old high
kernel and image source dictionaries, the primitive integer model, the exact
315-state, and the exact $U_7$ selector, with complete byte and payload hashes.
It did not recompute the old normal-form Gaussian elimination.

The seven batches cover exactly $K_2,\ldots,K_{198}$, with active sizes
$31,31,31,31,31,31,11$. The final twenty padding columns are exact zero sources;
their cost and full 820-coordinate remainder gates were checked before they
were discarded. No active original label is lost or duplicated.

For every one of the 197 columns the program:

1. restores the original 6188-source first correction, including the old
   prebasis, forward and backward transformations, and the parameter shifts;
2. forms the actual integer source $\widehat K_j-p\widehat q_{1,j}$ and
   multiplies by all 17 original equations, retaining all 4367 outputs;
3. verifies coefficientwise divisibility by $p^2$ and computes its reduction
   after division from the product modulo $p^3$;
4. replays the paid normal-form transformations, with their complete forward
   and backward byte hashes unchanged, and verifies the full image/remainder
   identity;
5. retains the whole 820-coordinate state, checks all 505 free observations,
   and verifies reconstruction from all 315 torsion coordinates.

Divisibility verified modulo $p^3$ gives actual integer divisibility by $p^2$
for the chosen integer source; it also determines the exact divided column
modulo $p$. No higher-precision product is fabricated by appending zero digits.

The final consumer starts with all 204 original seeds, namely $U_7$ and the
197 divided columns. It closes them under the paid complete parameter action
$J$, checks reconstruction of every seed, checks $JB=BJ_B$, and replays the
whole source-expression DAG. It uses no primary projection and no truncated
parameter jets.

## 4. Exact returned finite-field data

The completed result reports
$$
\operatorname{rank}[U_7,R_{2,2},\ldots,R_{2,198}]=7,\qquad
\dim\langle J^kU_7,J^kR_{2,j}:k\geq0\rangle=7.
$$
The old $U_7$ already has rank seven. Hence both spaces equal that same $U_7$.
The complete returned characteristic coefficients, in ascending order, are
$$
[30,20,7,1,16,30,19,1].
\tag{4.1}
$$
Their factorization is $(s-1)^2(s-2)^5$; multiplication of those factors gives
(4.1). The actual source basis and action have hashes
$$
\begin{aligned}
B:\;&\texttt{4a2effb4d2304242c1fe2594fb6da977aeb4983b7ca9c5f303c0742b79c44b36},\\
J_B:\;&\texttt{c3a2ea91d45ce62d8341741a1a1688993288fd2320c82e89ef4eee31aea50400}.
\end{aligned}
$$
Together with the exact colon theorem, these checks prove (1.2).

For clarity about the interpretation, a summand $D/(p^a)$ in a finite
$D$-module contributes one dimension to $I_e$ if and only if $a\leq e$.
The filtration $I_1\subset I_2\subset\cdots$ is canonical and preserved by $s$,
even though an arbitrary decomposition as a $D$-module need not be preserved
by $s$. Thus $\dim I_2-\dim I_1$ counts exactly the summands of exponent $2$,
and the quotient characteristic determines their primary distribution.
The complete first-image theorem gives (1.3); division of the two
characteristics proves (1.4).

## 5. Consequences for the rational divisor

The independently paid
[quotient defect calculation](R150-appendix-original-quotient-defect-one-and-affine-degree299.md)
gives
$$
\chi_{C/pC}=\Delta_{31}/(s-2),\qquad \dim(C/pC)=314.
\tag{5.1}
$$
The exact
[$s=2$ coefficient spectrum through five](R150-appendix-root2-coefficient31-spectrum-through-five-and-affine-degree300.md)
has multiplicities $(1,4,2,4,2)$. Its last three levels contribute eight
directions beyond $I_2$, all on the $s=2$ primary. Consequently
$$
\boxed{\overline{\Delta_{\rm aff}}\ \bigm|\ 
 \frac{\Delta_{31}}{\chi_{I_2}(s)(s-2)^9}
 =
 \frac{\Delta_{31}}{(s-1)^2(s-2)^{14}}.}
\tag{5.2}
$$
The exponent nine in the first expression comprises the one-dimensional
quotient defect and the eight already proved higher coefficient directions.
The degree of the right side is $315-7-9=299$.

The exact rational outside factor
[$\Omega=f_{60}^2$, of degree 120](R150-appendix-exact-original-external-divisor120-multiplier21-and-source-cost8411.md)
and the original degree-158 factor $K_{158}$ give the already proved
$\deg\mu\leq299-158-120=21$. This uses their rational divisibility and the
complete target-module argument. It does not assume that the reduction of
$\Omega$ equals the factor called $Q_{60}^2$ in $\Delta_{31}$.

The separate actual coefficient audit has now checked that identification;
the precise comparison is recorded below. The original rational source bound
remains 8411 and the uniform $D$-source bound for already existing solutions
remains 8535. No new characteristic-zero membership of the nine original
$h_0t_j$ follows from the equality $I_2=U_7$ alone.

### 5.1. Actual Omega reduction and the exact residual support envelope

The independent
[small original-divisor audit](../notes/r150-source-kernel-session-789f/43756208221-paid-outside-divisor-reduction31-audit-60.json)
completed in 0.002218695000919979 seconds, with all 121 rational coefficient
denominators proved to be 31-units, and the exact rational and finite-field
square identities checked. Its raw receipt has 3463 bytes and SHA256
`b536af2e8586add34298599b04bbe89f042a994d7b780af1cffc1ffb62abe627`.
The published outer receipt is 11089 bytes, SHA256
`b5ee9b9d2a7a2fe68106cc5f66a88dc964e988e4286dc896b18ed70a2b30b37b`.
Binding:
`13528e66e253f0e321ba4c790d20a7b42c6c48f439e9acba178aec86748fa1ae`.

That run did not load the 315-state; its
`crossReceiptQ60ComparisonPerformed` field is correctly false. The subsequent
cross-receipt comparison uses its full 121 coefficients and the complete
factor coefficients in the global197 receipt. Multiplying the five outside
factors of degrees $2,6,7,16,29$, each twice, gives exactly those 121
coefficients. Thus
$$
\boxed{\bar\Omega=Q_{60}^2.}
\tag{5.3}
$$
The common canonical coefficient SHA256 is
`fcde24eb5801fcf9d172f77a10ed2bcf162a50e742fe97a49b92e7cb85e628be`.
This is a coefficient-by-coefficient comparison of the two actual small
receipts, not an inference from their equal degrees.

Write the monic finite-field cubics and sextic as
$$
P_+=[17,25,26,1],\qquad P_-=[24,24,27,1],\qquad
E_6=[30,15,0,2,18,13,1],
$$
where arrays list ascending coefficients. Normalizing the original $E_8$
by its leading coefficient and reducing gives exactly
$(s-1)(s-2)E_6$. The full 316 coefficients verify
$$
\Delta_{31}
=\chi_{I_2}(s)(s-2)^9\bar K_{158}\bar\Omega B_{21},
\qquad
B_{21}=(s-1)(s-2)^2P_+^2P_-^2E_6.
\tag{5.4}
$$
The ascending coefficients of $B_{21}$ are
$$
[7,25,15,20,20,15,22,9,26,15,29,26,28,8,4,21,15,11,29,5,21,1],
$$
with canonical SHA256
`cb7a22121ed1a40632946f4e54539aa3b8aa4d0d04ca53826d95a48acc53ea92`.
The [root's independent cross-receipt audit](../notes/2026-11-15-r150-omega-i2-root-cross-audit-789f.json) and an independent direct polynomial multiplication
verified (5.3), the nine normalized $E_8$ coefficients, and all 316
coefficients of (5.4).

The monic remaining target multiplier $\mu$ divides
$\Delta_{\rm aff}/(K_{158}\Omega)$ by the paid relative-target-module theorem.
All these monic factors are 31-integral. Reducing and cancelling in
$\mathbf F_{31}[s]$, using (5.2) and (5.4), proves
$$
\boxed{\bar\mu\mid B_{21}.}
\tag{5.5}
$$
This identifies a precise residual support envelope. It does not assert that
any factor of $B_{21}$ is actually needed, nor that $\mu=1$. A factor supported
away from the critical set over $\mathbf Q$ can reduce into critical
finite-field primaries; this possibility is retained.

## 6. A complete next global colon interface

The result now gives a precise global third-level interface. This section is
an exact source theorem and an execution plan, not a report that the new
divided columns have been calculated.

Write $V_7=[b_1,\ldots,b_7]$ with its fixed original integer representatives.
For each $j$ choose the actual constant coordinates $c_j\in\mathbf F_{31}^7$
such that $[R_{2,j}]=U_7c_j$. Select full polynomial sources $q_j$ satisfying
$$
\bar A q_j=\bar R_{2,j}-\bar V_7c_j.
$$
Choose integer polynomial lifts of these data and put
$$
d_j=\frac{R_{2,j}-V_7\widehat c_j-A\widehat q_j}{p}.
\tag{6.1}
$$
Every numerator is a genuinely divisible original polynomial vector.

Let $J_7$ be the complete actual action on the same ordered $U_7$ basis.
The kernel of the map
$\mathbf F_{31}[s]^7\to U_7$ is exactly
$(sI_7-J_7)\mathbf F_{31}[s]^7$. Therefore choose full original sources $q'_i$
for the seven columns of $V_7(sI_7-\widehat J_7)$ modulo $p$ and define
$$
e_i=\frac{\bigl(V_7(sI_7-\widehat J_7)\bigr)_i-A\widehat q'_i}{p}.
\tag{6.2}
$$
If the stored $U_7$ basis is changed, its actual source matrix and action must
both be transported; no quotient basis is substituted without that transport.

These vectors give the complete exact identity
$$
\boxed{(L:p^3)=
 (L:p^2)+\sum_{j=2}^{198}d_jD[s]
       +\sum_{i=1}^{7}e_iD[s]+b_8D[s]+pb_9D[s].}
\tag{6.3}
$$
To prove it, apply the one-step kernel lifting construction to $B_2$ in (2.2).
Subtracting the chosen $A$ and $V_7$ combinations makes each of the 197 columns
zero modulo $p$. The last two columns $pb_8,p^2b_9$ are also zero modulo $p$.
The remaining block $[\bar A,\bar V_7]$ has a full kernel generated by the
original kernel of $\bar A$ and the seven graph relations (6.2): project any
relation to the original cokernel, express its last seven coordinates through
$sI_7-J_7$, subtract these graph relations, and use the complete original
$\bar A$-kernel.

Dividing the images of these lifted kernel generators by $p$ yields exactly
(6.1), (6.2), $b_8$, $pb_9$, and first divided original $A$-kernel images.
The latter already lie in $(L:p)\subset(L:p^2)$. The $p$ times source generators
give $(L:p^2)$ itself. This proves both inclusions in (6.3) by a finite
calculation; no completion or Nakayama argument for $D[s]$ is used.

All columns in (6.3) have true $p^3$ original sources. For example,
$$
p^3d_j
 =A\left(\widetilde\kappa_j
       -\sum_{i=1}^7p^{\,2-e_i}\kappa_i\widehat c_{ij}
       -p^2\widehat q_j\right).
\tag{6.4}
$$
The analogous formula for $e_i$ uses
$\sum p^{2-e_i}\kappa_i(sI_7-\widehat J_7)_{i\ell}-p^2\widehat q'_\ell$.
Also $p^3b_8=A\kappa_8$ and $p^3(pb_9)=A\kappa_9$.

For the next reduced image $I_3$, the column $pb_9$ is zero in $C/pC$.
The complete remaining candidates are the old $U_7$, the 197 columns (6.1),
the seven action-relation columns (6.2), and $b_8$, followed by closure under
the full original $J$. Merely correcting each $R_{2,j}$ to its $U_7$ class,
while omitting the seven polynomial relations, would not be a complete
global colon computation.

The existing calculation determines $R_{2,j}$ only modulo $p$. Computing
(6.1) modulo $p$ requires their actual next digit, hence original products
modulo $p^4$, together with the fixed original sources of $V_7$ and full
$A$-preimages of the remainders. These data must be reconstructed and checked;
they are not obtained by appending a zero digit to the present arrays.

## 7. Reproduction and exact actual identities

Actual research run:
[43772109844](https://github.com/Rogerhu12/math-research-public/actions/runs/43772109844).
The first 600-second call made a checked partial checkpoint. The continuation
used exactly the same source, semantic binding, and output directory and
completed all remaining stages, without redoing the completed original rows.

Final step: `complete-global197-original-i2-resume600`.  
Execution source: `596f6d7a5ddcf0a02ccc24e966e17c787a9b4df8`.  
Continuation mathematical time: 293.5614321799999 seconds.  
Binding:
`3cdbc4361da3d71a35655eda11ea5862641de0398f085de159343ca54036bbe1`.

The [published final receipt](../notes/r150-source-kernel-session-789f/43772109844-complete-global197-original-i2-resume600.json)
is 77304 bytes, SHA256
`4590ad661b71bc0480dfaa43755bdab778fe53be3d473caa91367e9e829ca4aa`.
Its complete temporary receipt is 46870 bytes, SHA256
`5d9fc76f51013680792c47e61d55516137c86a2cd784d3241ebdfe11f9a8f24f`.

The exact source list is in the
[frozen source manifest](../notes/2026-11-15-r150-global197-i2-source-manifest-789f.json);
the reconstruction and interpretation contract is in the
[original-input interface](../notes/2026-11-15-r150-global197-i2-complete-original-interface-789f.md).
Runner SHA256:
`fc1bfafdf11119390f19adef3f6230d76cf8d93d7bdaa95d439589a3f4ec77df`.
Closure SHA256:
`9071f4a3b48fdf277a6cc6e7c65f5dc0b5aea213dd6cf0b4affffc1eccb1a471`.

The temporary complete source-expression system is 14868 compressed bytes,
SHA256
`5d3160c9a455b613b0303980d05bb4942f391a65ec57fca33364cc45388ac13c`,
with payload SHA256
`a26534a0ab410f02ea64d809423afe8a242d4a557f9f2de87c2e3351bd39b1f7`.
It records all 204 seeds and their whole-source DAG. The original 315-state
and $U_7$ selector hashes are, respectively,
`06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf`
and
`2d90d72ac72cc63e5531b80a6e788ef82c6bf794481b53546b27b0afcb7134ee`.

Only source code, parameters, the small receipts, and hashes are permanent.
The reproducible original arrays and intermediate source systems remain
temporary. The bound 177 concerns the 197 initial source constructions; it is
not asserted as a common bound for every later parameter multiple in a
polynomial closure.
