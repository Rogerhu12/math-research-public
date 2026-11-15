# R133 supplement: finite Fredholm completion of the actual regular Ai graph

2026-11-15, visible-exact / newton_source.

**New analytic completion theorem; no numerical evaluation.** At one fixed admissible real parameter, the actual stable root map of SE can be completed by a finite-rank operator to an isomorphism in both required natural Sobolev windows. The same finite operator works in every fixed window to which the existing coordinate maps apply. Its construction does not assume incoming injectivity.

The completed family parametrizes the same regular positive given-head graph, with the same homogeneous difference equations and outer condition. The original Ai family can have a redundant finite-dimensional parameter kernel and can miss finitely many stable directions. Neither issue is declared absent. The completion replaces those zero physical directions by the missing genuine positive-Poisson columns. All newly added columns, their full dual rows, every independent mean and the complete remaining matching equations stay in the actual relation.

This removes the circular basis-spanning hypothesis from SE's reference change. It does not prove a numerical rank, a complete incoming inverse, a finite Schur inverse, a uniform parameter-family completion, or a new bulk estimate on rough stable data.

## FC1. Fixed objects and scope

Use the normalized circle of period $\pi/2$, physical frequencies $4j$, original high projection $P_H={\bf1}_{|j|\ge97}$, and the original reflection realization of SE. Both signs are retained in its complexification. Independent physical means are not elements on which an inverse power of frequency acts.

All parameters, radial pieces, selected-coordinate qualifications and original positive boundary conditions are precisely those of the following existing proofs.

| Primary | Immutable Git blob | Bytes | SHA256 |
|---|---|---:|---|
| SE, natural stable Fredholm structure | eb7b1bb1ea1fdf713fcf172428f68ed20afafdb2 | 20047 | 2220174707046248cbdf9f9f8c47bc13bc233b0ab65f5ed598ddcbf964e93ad4 |
| IN, genuine stable trace and seven-port identity | f13509b4d0afc691cfc95d86c0f8e5562f919129 | 33894 | d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75 |
| P, actual corrected high Poisson construction | 11250cbb5f9921fdaa70791b6095c306e16bc5d7 | 35230 | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |
| Full-delta negative-one positive source graph | 6765382c0ea8af731b6593b687cbc84401a4f7ec | 15756 | 0f1383da8611aef931829876b49579f41c7a967435c795ef68a85d2a142cac23 |
| Actual full-delta positive graph | 8b28bcd0929df468f44186236dd0cf2e9c037dad | 10464 | e144ad9f8cd7dbc29904f92524e9da9511f4bb8d403e06620d8ad85f3105742c |
| BF, complete finite factors and augmented incoming system | 921dbfc574e94da86c8d44872a919c201c569060 | 19339 | e8e29c49deb9fabf6be9b9dd9059c26e94afbd1bc274742d7d3fe7527bf4a02e |

Fix one allowed real $\delta$. No basis below is asserted to depend smoothly, analytically or uniformly on $\delta$. A change of kernel dimension is not excluded. The estimates and identifications are at this same fixed physical operator.

Let $\mathcal H^t=\mathcal H_H^t$ be SE's reflected high space and put
$$
 A=S_{\rm nat}=D_c+K.
 \tag{FC.1}
$$
SE.18--20 give, for every fixed real $t$,
$$
 K:\mathcal H^t\longrightarrow\mathcal H^{t+2/3},
 \qquad
 0<c_-\le c_n\le c_+<\infty.
 \tag{FC.2}
$$
The constants may depend on $t$ and on the fixed operator. This theorem does not evaluate them. The real diagonal $D_c$ and its inverse act boundedly on all these spaces. In particular $A$ is Fredholm of index zero in every fixed window.

## FC2. One smooth kernel and one smooth annihilator

Take the adjoint in the original normalized $L^2$ inner product on $\mathcal H^0$. For the duality argument, write $\langle e,x\rangle$ for the pairing conjugate-linear in $e$ and linear in $x$. The same convention extends it to smooth-test/distribution pairs.

The gain statement in (FC.2) at exponent $-t-2/3$ dualizes to
$$
 K^*:\mathcal H^t\longrightarrow\mathcal H^{t+2/3}
                  \quad\text{for every fixed }t.
 \tag{FC.3}
$$
Thus $A^*=D_c+K^*$ has the same regularity gain in its kernel equation. Every distributional kernel vector of either operator bootstraps by $2/3$ repeatedly and is smooth.

Define the finite-dimensional spaces
$$
 E=\ker(A:\mathcal H^0\to\mathcal H^0),\qquad
 F=\ker(A^*:\mathcal H^0\to\mathcal H^0),\qquad
 m=\dim E=\dim F.
 \tag{FC.4}
$$
Index zero gives equality of dimensions; it does not give $m=0$. Every element of $E$ and $F$ lies in $\bigcap_t\mathcal H^t$. The kernel in any other fixed window is exactly $E$.

The annihilator of the range in $\mathcal H^t$ consists of the distributional adjoint kernel in $\mathcal H^{-t}$ and hence of the same smooth $F$. Therefore
$$
 \operatorname{ran}(A:\mathcal H^t\to\mathcal H^t)
  =\{y\in\mathcal H^t:\langle f,y\rangle=0
                         \text{ for every }f\in F\}.
 \tag{FC.5}
$$
Both inclusion and equality are important: inclusion is the adjoint identity, while closed range and codimension $m$ supply equality. No change of the Sobolev inner product is used to choose a different cokernel basis.

## FC3. A finite completion independent of the window

Choose $L^2$ orthonormal bases $e_1,\ldots,e_m$ of $E$ and $f_1,\ldots,f_m$ of $F$. Define on distributions
$$
 W x=\sum_{\nu=1}^m f_\nu\langle e_\nu,x\rangle.
 \tag{FC.6}
$$
For $m=0$ use the empty sum $W=0$. If the actual operator is restricted to its real conjugation-invariant reflection space, choose real orthonormal bases there and complexify. Then $W$ preserves that same reality and reflection structure. No independent sign sector or physical mean is silently removed.

The operator $W$ has rank $m$, annihilates $E^\perp$, and maps $E$ isometrically onto $F$. Its adjoint satisfies
$$
 W^*W=\Pi_E,\qquad WW^*=\Pi_F.
 \tag{FC.7}
$$
Here $\Pi_E,\Pi_F$ are these finite $L^2$ projections, not Fourier truncations.

Since the basis vectors are smooth, for any fixed $t,u$,
$$
 \|W:\mathcal H^t\to\mathcal H^u\|
 \le\sum_{\nu=1}^m
             \|f_\nu\|_{\mathcal H^u}
             \|e_\nu\|_{\mathcal H^{-t}}<\infty.
 \tag{FC.8}
$$
This is a genuine smoothing finite factorization. It is not a numerical value and does not identify a finite Fourier support.

At $L^2$, the decomposition of domain and target is
$$
 \mathcal H^0=E\oplus E^\perp,\qquad
 \mathcal H^0=F\oplus F^\perp.
$$
The restriction $A:E^\perp\to F^\perp$ is a bounded isomorphism: its kernel is zero, its range is the closed range of $A$, and (FC.5) identifies that range. In these decompositions $A+W$ consists of the two isomorphisms
$$
 W:E\to F,\qquad A:E^\perp\to F^\perp.
 \tag{FC.9}
$$
Consequently $A^\sharp:=A+W$ is invertible on $L^2$. Equivalently, if $G$ denotes the inverse on $F^\perp$ with range $E^\perp$, extended as zero on $F$, then
$$
 (A^\sharp)^{-1}=G+W^*,\quad
 AG=1-\Pi_F,\quad GA=1-\Pi_E.
 \tag{FC.10}
$$
This formula is an existence statement, not a computed generalized inverse.

For every fixed $t$, $A^\sharp$ is still Fredholm of index zero because $W$ has finite rank. A distributional vector in its kernel obeys
$x=-D_c^{-1}(K+W)x$ and therefore is smooth. Its $L^2$ kernel is zero by (FC.9), so its kernel in $\mathcal H^t$ is zero. Index zero now gives
$$
 \boxed{A^\sharp:\mathcal H^t\longrightarrow\mathcal H^t
         \text{ is a bounded isomorphism for every fixed }t.}
 \tag{FC.11}
$$
These inverses agree on overlapping distributional domains, by uniqueness. One fixed $W$ was used throughout, rather than a new finite correction for each exponent.

The rank $m$ is minimal for an invertible finite correction: any finite $W_1$ with $A+W_1$ injective must be injective on $E$ when restricted there and hence has rank at least $m$. This does not determine the actual value of $m$.

## FC4. Natural weights and the exact common root input

Keep SE.21--23 without commuting any factor:
$$
 S_{\rm tr}^{Y}
   =N_{\rm out}^{-1}A N_{\rm in}^{7/6},
 \qquad
 C_s=S_{\rm tr}^{Y}N_i:
    \mathcal X_s\longrightarrow
    \mathcal Y_s=\mathcal H^{s-1/6}.
 \tag{FC.12}
$$
Here $N_i:\mathcal X_s\to\mathcal H^s$ is the actual bounded incoming-coordinate isomorphism. In the declared common-input realization it is
$\Lambda_+^{-1}T_F^{-1}\mathcal S^{-1}$ in precisely that order. $\Lambda_+$ is the original nonzero root scalar diagonal, not a Bessel frequency weight. The low complement and independent means are separate ports.

Define the same finite map on the common core by
$$
 F_C=N_{\rm out}^{-1}W N_{\rm in}^{7/6}N_i,\qquad
 C^\sharp=C+F_C
       =N_{\rm out}^{-1}A^\sharp N_{\rm in}^{7/6}N_i.
 \tag{FC.13}
$$
The two required windows are
$$
 \begin{array}{c|c|c}
 s&\text{window for }A^\sharp&\mathcal Y_s\\ \hline
 0&-7/6&\mathcal H^{-1/6}\\
 -4/3&-5/2&\mathcal H^{-3/2}.
 \end{array}
 \tag{FC.14}
$$
Thus (FC.11) yields, without an incoming hypothesis,
$$
 \boxed{
 (C_s^\sharp)^{-1}
 =N_i^{-1}N_{\rm in}^{-7/6}
     (A^\sharp)^{-1}N_{\rm out}:
        \mathcal Y_s\longrightarrow\mathcal X_s.}
 \tag{FC.15}
$$
The same conclusion holds for any other fixed $s$ for which the actual $N_i$ and its inverse have the stated bounded coordinate realizations. No unproved coordinate norm in another window is supplied by this sentence.

The finite factors in (FC.13) are explicitly
$$
 y_\nu=N_{\rm out}^{-1}f_\nu,\qquad
 \ell_\nu(x)=
   \langle e_\nu,N_{\rm in}^{7/6}N_i x\rangle
   =\langle N_{\rm in}^{7/6}e_\nu,N_i x\rangle,\qquad
 F_C=\sum_{\nu=1}^m y_\nu\ell_\nu.
 \tag{FC.16}
$$
The equality moves the selfadjoint frequency power within its pairing; it does not move it through $N_i$. All $y_\nu$ are smooth high stable data, and the complete rows obey
$$
 \|\ell_\nu\|_{\mathcal X_s^*}
 \le \|N_i:\mathcal X_s\to\mathcal H^s\|
       \|N_{\rm in}^{7/6}e_\nu\|_{\mathcal H^{-s}}.
 \tag{FC.17}
$$
For $s=-4/3$ this is the required positive $4/3$ dual regularity in the actual common input coordinates. Right composition has not made $\ell_\nu$ a finite Fourier row. If a full BF space uses an additional actual projection or extension to select $\mathcal X_s$, its complete dual factor must also be included.

## FC5. The original parameter kernel is a zero physical direction

Let $\mathcal P_{\rm hom}$ be the **linear stable-input column** of the original positive given-head graph, with its supplied head and every other independent positive input zero. It is the homogeneous difference operator for that graph. It does not include a nonzero affine base solution.

Write
$$
 \Psi_i=\Psi_A N_i .
$$
IN.28 and SE.24 give on the smooth core
$$
 \Psi_i=\mathcal P_{\rm hom}C.
 \tag{FC.18}
$$
The corrected family uses the same true regular outer condition. Its PC correction has zero stable root input, so the stable trace in (FC.18) is the actual trace, not a formal leading diagonal.

If $C_sx=0$, SE's bootstrap implies that
$N_{\rm in}^{7/6}N_ix$ lies in the smooth $E$. Equation (FC.18) and the uniqueness of the original given-head high graph then give
$$
 \Psi_i x=0.
 \tag{FC.19}
$$
Conversely a zero physical column has zero actual stable trace and therefore $Cx=0$. Accordingly the parameter kernel and the zero-physical-column kernel coincide on this core and on any compatible trace extension where the stable trace is defined.

This is not a proof that $x=0$. Physical uniqueness does not by itself prove faithful Ai coordinates. It also does not identify an incomplete incoming high-row compression with the complete physical trace.

The word “graph” here has exactly the original meaning: the positive high equation is solved with its specified supplied head and regular outer condition. The original low equations, both physical means, waist matching and any other coupled equations are still imposed through their original rows. No graph theorem is promoted to a full coupled Codazzi inverse.

## FC6. A faithful parametrization of the same given-head graph

Define
$$
 \widetilde\Psi_i
   =\Psi_i+\mathcal P_{\rm hom}F_C
   =\mathcal P_{\rm hom}C^\sharp.
 \tag{FC.20}
$$
For a fixed collection $p$ of the original remaining inputs, let $u_p$ denote the original corresponding particular solution. It contains the given head, exterior, jump, ordinary-source or mean contributions in their actual types. Then
$$
 u_p+\widetilde\Psi_i x
      =u_p+\mathcal P_{\rm hom}C^\sharp x .
 \tag{FC.21}
$$
As $x$ ranges over the compatible smooth common-input core, $C^\sharp x$ ranges over all smooth stable data. This follows from (FC.15) and the smoothing/bootstrap uniqueness used in FC3. Hence (FC.21) parametrizes **exactly the same entire smooth regular given-head graph**
$$
 \{u_p+\mathcal P_{\rm hom}y:\ y\text{ is smooth stable data}\}.
 \tag{FC.22}
$$
It is one-to-one in $x$, because the actual stable trace of $\mathcal P_{\rm hom}y$ is $y$.

In contrast, the original $\Psi_i$ parametrizes the stable subspace $\operatorname{ran}C$ and has its possible kernel. The decomposition (FC.5)--(FC.9) shows that the completion supplies the missing $m$ stable directions. The old and new parametrizations need not have the same range before this completion.

Every added column is the actual solution
$$
 p_\nu=\mathcal P_{\rm hom}y_\nu
 \tag{FC.23}
$$
with zero supplied head and zero other independent inputs. It satisfies the same homogeneous high equation, actual interface matching and regular outer condition. It introduces no growing boundary datum and no new physical forcing. Its original low-equation residual and independent mean or matching readouts must be kept. On the negative side it is continued by the same original physical Cauchy extension and prescribed root coordinates as the other high Poisson columns.

The phrase “smooth” for $y_\nu$ concerns angular root data. It does not assert extra radial smoothness across the existing piece interfaces, a new global bulk norm, or a numerical bound for $p_\nu$. The column has the regularity furnished by the original Poisson and continuation maps at this smooth input.

Thus the physical boundary conditions and all independent rest ports remain unchanged. Imposing their complete original equations after substitution (FC.21) yields exactly the same admissible physical solution set. The new finite columns change coefficients in those equations, not the equations that define the problem.

## FC7. The actual finite columns and dual rows remain in BF

Let $\mathcal I_P,\mathcal O_P$ denote the complete physical incoming/outgoing maps on stable data and the independent remaining ports. They include every retained physical mean, finite row, sign ordering, supplied head function and source type of the chosen actual realization.

For each smooth stable column $y_\nu$, retain the actual outputs
$$
 i_\nu=\mathcal I_P(y_\nu,0),\qquad
 o_\nu=\mathcal O_P(y_\nu,0).
 \tag{FC.24}
$$
These are obtained from (FC.23) and its complete original receivers. They are not replaced by principal-symbol values. On the smooth core the changed maps satisfy
$$
 \begin{split}
 \widetilde{\mathcal I}_A-\mathcal I_A
        &=\sum_{\nu=1}^m i_\nu\,(\ell_\nu\pi_{\mathcal X}),\\
 \widetilde{\mathcal O}_A-\mathcal O_A
        &=\sum_{\nu=1}^m o_\nu\,(\ell_\nu\pi_{\mathcal X}),
 \end{split}
 \tag{FC.25}
$$
where $\pi_{\mathcal X}(x,p)=x$ is the actual direct-sum coordinate selection. The rest-port columns are unchanged.

When the declared output norm is the complete $L^2$ trace plus its specified physical finite coordinates, BF's genuine strong fee is
$$
 \left\|\sum_\nu i_\nu\ell_\nu:
               \mathcal X_{-4/3}\to\mathcal U_0\right\|
 \le\sum_\nu\|i_\nu\|_{\mathcal U_0}
                 \|\ell_\nu\|_{\mathcal X_{-4/3}^*},
 \tag{FC.26}
$$
and the identical formula applies to $o_\nu$. Membership of the actual columns in the chosen output spaces must be supplied by their original maps; their complete norms or exact retained matrix entries must still be paid. Smooth root data alone is not a numerical column certificate.

The finite factorization is unconditional at the root trace level. Its use in a bounded complete incoming realization requires precisely these actual output-column qualifications, as does BF for every finite factor. A complete physical head function can occur in an output column; the map is still finite rank because only $m$ scalar coordinates feed those fixed columns. The independently variable radial head port remains infinite dimensional.

The change is smoothing in root coordinates. In a waist realization satisfying (FC.26), its full effect belongs to the retained finite strong map, so no published order-zero or first coefficient is replaced. This does not permit deleting the actual finite difference or its mean rows. The number $m$, the bases, their dual norms and the complete physical columns have not been evaluated.

## FC8. Exact common right factor for every remaining port

Let $\mathcal R_s$ be the original rest space. It can be infinite dimensional and retains all original norms. Define
$$
 \mathbb D_\sharp
   =\operatorname{diag}(C_s^\sharp,1_{\mathcal R_s}):
       \mathcal X_s\oplus\mathcal R_s
        \longrightarrow\mathcal Y_s\oplus\mathcal R_s.
 \tag{FC.27}
$$
Its inverse is known to exist from FC4, independently of any incoming injectivity. On the common smooth core, the complete physical maps obey exactly
$$
 \widetilde{\mathcal I}_A=\mathcal I_P\mathbb D_\sharp,
 \qquad
 \widetilde{\mathcal O}_A=\mathcal O_P\mathbb D_\sharp.
 \tag{FC.28}
$$
The actual outgoing global sign and all density, primitive and finite-row factors stay on their existing sides. There is no commute through $\mathbb D_\sharp$.

If the original complete trace maps were only defined on smooth stable data, suppose the left sides of (FC.28) have the required bounded extensions, with the finite columns of FC7 retained. Then
$$
 \mathcal I_P=\widetilde{\mathcal I}_A\mathbb D_\sharp^{-1},
 \qquad
 \mathcal O_P=\widetilde{\mathcal O}_A\mathbb D_\sharp^{-1}
 \tag{FC.29}
$$
define their unique bounded trace extensions from that dense graph. They agree with the original physical maps wherever those were already defined. This is a trace extension, not a new solution theorem for rough bulk data.

In any declared square realization for which these complete maps are bounded, $\mathcal I_P$ is invertible if and only if $\widetilde{\mathcal I}_A$ is invertible. If either condition has actually been proved, then
$$
 \mathcal I_P^{-1}
     =\mathbb D_\sharp\widetilde{\mathcal I}_A^{-1},
 \qquad
 \boxed{\mathcal O_P\mathcal I_P^{-1}
   =\widetilde{\mathcal O}_A
                    \widetilde{\mathcal I}_A^{-1}.}
 \tag{FC.30}
$$
The common coordinate factor cancels exactly on the right. The equality needs no numerical bound for $(C_s^\sharp)^{-1}$. A numerical incoming-inverse estimate would still require the appropriate norm of $\mathbb D_\sharp$ and of the complete inverse in (FC.30).

The expression $\mathcal O_A\mathcal I_A^{-1}$ for the uncompleted family has not been asserted to exist. If that original complete incoming map is independently invertible, FC5 forces $m=0$, so $W=F_C=0$ and (FC.30) reduces to SE.28. Without that hypothesis the completed formula is the valid one.

## FC9. What the completion resolves

The proof of (FC.11), (FC.15) and smooth graph coverage uses only the already proved Fredholm structure and the original given-head Poisson identity. It does not use incoming injectivity to establish faithful coordinates. This is the precise removal of SE9's circular basis-spanning prerequisite.

A second reference basis used solely for the same regular given-head graph is no longer an obligatory additional infinite error: the completed stable coordinates cover that graph. A genuinely independent second input, nonregular solution, exterior datum or other original port remains in $\mathcal R_s$. The theorem does not classify such a port as finite.

For an actual finite Schur or augmented BF computation, all of the following remain necessary:

1. Identify the actual complete square relation and its physical mean, low and independent source rows.
2. Determine a usable completion, or establish $m=0$ by a separate actual stable-kernel argument.
3. Supply the complete new finite columns and dual rows of FC7, either with their correct strong bounds or as exact retained factors.
4. Retain every other infinite error and global sign term in its true ordered location, and pay the complete strong bounds required by the chosen high inverse.
5. Verify the remaining finite matrix and complete incoming conditions; (FC.30) is then available without an additional second-basis estimate.

No original successful Airy, root, positive-graph, propagation, signed-density, KAM or finite computation is repeated. No new public numerical job is requested by this proof.
