# Full physical multiple shooting on the true low193 problem

Let the 1424 original true-root cell endpoints be indexed by $0,\ldots,n$. In physical raw coordinates the exact differential equation gives $x_{i+1}=T_i x_i+f_i$, with $T_i$ ranging over its original directed joint operator ball for the varying equation. Write $a x_0=\pi_{97:193}x_0$ in zero-based half-open row notation. At the other end $b x_n=(\pi_{0:96}x_n+(13/80)\pi_{97:193}x_n,\pi_{96}x_n)$. The last scalar is the independent outer mean. The complementary root mean remains among the freely observed 97. The output atoms are the free 97 at the root and $\Theta\pi_{97:193}$ at the outer end with the original 96 multipliers. A change to balanced local integration coordinates is already undone in the original whole-cell transfer and moment data.

This supplement gives a separate sufficient inverse test and physical source estimates. Its first target consists of ordered defect bounds on every original equation, its second is a strict global contraction, and its third measures all four original sources. The previous GG and GDC graph numerics retain their own outcomes.

## MSS.1. A square operator with two physical boundaries

Choose finite matrices of dyadic neighbourhood centres $U_i:\mathbb R^{97}\to\mathbb R^{193}$ and $V_i:\mathbb R^{96}\to\mathbb R^{193}$. Set $x_i=U_ic_i+V_id_i$. A numerical QR of the midpoint forward on $U_0=(I_{97},0)^t$ and of the independently provided midpoint inverse on $V_n=(-13 I_{96}/80,0,I_{96})^t$ proposes columns only. All actually stored entries are exact binary64 dyadics. In particular the terminal coefficient selected by floating $13/80$ has its actual error paid at the physical boundary. No invertibility or orthogonality of either QR basis is used in the proof.

For each interval define
$$
 L_i=[T_iU_i,-V_{i+1}],\qquad H_i=[U_{i+1},-T_iV_i],\quad
 y_i=(c_i,d_{i+1}),\quad v_i=(c_{i+1},d_i).
$$
The equation is $L_i y_i=H_i v_i-f_i$. Select a dyadic preconditioner $P_i$ from the proposed inverse of the centre of $L_i$. Choose dyadic $R_i,S_i$ from the two diagonal blocks of the midpoint $P_iH_i$, keeping their signs. Then
$$
 y_i-\operatorname{diag}(R_i,S_i)v_i
 =(I-P_iL_i)y_i+
     (P_iH_i-\operatorname{diag}(R_i,S_i))v_i-P_i f_i .
\tag{MSS.1}
$$
At the root choose a dyadic $P_a$ approximating $(a V_0)^{-1}$, at the outer end a dyadic $P_b$ approximating $(b U_n)^{-1}$. Apply them to the two physical boundary equations. The root remainder is
$-P_a a U_0 c_0+(I-P_a a V_0)d_0$; the outer remainder is $(I-P_b b U_n)c_n-P_b b V_n d_n$. There are precisely 96 and 97 boundary rows.

Every one of the eight local defect blocks is computed on signed matrices before taking a norm. For $T_i=T_i^0+\Delta_i$ with $\|\Delta_i\|_2\le t_i$, only the two blocks actually containing $T_i$ pay $t_i\|\pi_k P_i\|_2\|U_i\|_2$ or $t_i\|\pi_kP_i\|_2\|V_i\|_2$, respectively. Thus there is no per-entry $t_i$ charged to an entire 193 by 193 array. A directed upper for $\|M\|_2$ uses the original GDC signed Gram complement. For any actually stored finite real $E$, $\lambda_{\max}(M^tM)\le\lambda_{\max}(M^tM+E^tE)$. An outward Gershgorin bound on the right, rescaling for large or small products, suffices. The original Schur row/column estimate and the zero matrix case give alternative rigorous uppers.

## MSS.2. The global inverse and its evidence

Let $D$ be the left side of (MSS.1) together with $c_n,d_0$; $D$ is triangular in each temporal direction, with identity pivots. The right sides apart from the inputs define $B$. Norm the complete space by
$$
 \|(c,d)\|_w=\max_{0\le j\le n}\max\big(\|c_j\|_2/w^c_j,\|d_j\|_2/w^d_j\big).
$$
All 2850 proposed weights are positive exact finite dyadics, stored and read back before validation. Bound $B_i(c,d)$ by the sum of its four actual block upper norms times $w^c_i,w^d_{i+1},w^c_{i+1},w^d_i$, separately on each of the two ranges. Use the two-term boundary rows above. For the reverse sweep on any interval $i\le k<j$, its homogeneous propagator is the whole signed product $R_i\cdots R_{j-1}$. The forward sweep uses $S_{j-1}\cdots S_i$. An aligned binary tree computes these signed products in directed matrix arithmetic before evaluating their norms. It needs at most logarithmically many live product matrices. At a merge the reverse inhomogeneous bound is $h_{\rm left}+\|R_{\rm left}\| h_{\rm right}$; forward interchanges left and right. The unique aligned dyadic decomposition of every prefix and suffix gives all 2850 observation bounds. This construction never interprets an interval Taylor flow as a frozen matrix exponential.

Divide each resulting bound by the weight at its observation coordinate. Let $\theta$ be their directed upper maximum. A strictly positive $g\le1-\theta$ proves $D^{-1}(D-B)=I-D^{-1}B$ invertible with inverse norm at most $1/g$. The matrix $D-B$, up to a permutation of whole equation rows, is exactly the product of the block diagonal $P_i,P_a,P_b$, the original square physical boundary/evolution operator, and the block diagonal $[U_i,V_i]$. Each factor is square on its respective full space, of common total dimension $193(1425)$. Invertibility of the product implies invertibility of all factors. This proves the original finite low193 two-boundary problem for every actual permitted transfer, without assuming a local inverse for any chart. The exact variation-of-constants solution on each true arc then proves the original continuous inhomogeneous low problem. Floating proposals and a nonpositive observed gap carry no transversality conclusion.

The first natural receipt is written with all eight bounds on each of 1424 cells, the four boundary bounds and all aligned signed product bounds, before weight selection or testing the second target. The full scalar-row private object, ordered per-row hash, native definition and weight definition have separate whole hashes. The third target starts only after the genuine second one is persisted.

## MSS.3. Four source roles in their physical input and output norms

For role $j$, take $G_i(s)=\Phi(s,r_i)^{-1}B_j(s)$ on the whole true physical arc, and $O_i(t)=S(t)\Phi(t,r_i)$. The original local moments are $J_{i,j}=\int G_iG_i^*ds$ and $X_i=\int O_i^*O_i dt$ in ordinary $dr$. The jump $f_i=T_i\int G_i(s)h_i(s) ds$. For each projected range $k$, let $C_{ik}=\pi_kP_iT_i$ and form the full signed covariance $C_{ik}J_{i,j}C_{ik}^*$. Its outward trace bounds local squared Hilbert–Schmidt input cost. Its outward induced norm bounds squared operator cost. Positive semidefiniteness pertains to the true covariance. All arithmetic uses the entire original centre and its joint uncertainty.

Distinct radial cells are orthogonal input summands. In either norm the squared cost of a horizontal concatenation is at most the sum of the squared interval costs, with equality for the Hilbert–Schmidt squares of the true operators. Hence the dyadic merge for source squares uses $h_{\rm left}+\|R_{\rm left}\|^2 h_{\rm right}$ and its forward analogue. Take square roots at each node and divide by the corresponding weight. The maximum, then divided by $g$, bounds each true coefficient operator relative to its weight. For the Hilbert–Schmidt statement, apply the same Neumann proof to coefficient maps with local Hilbert–Schmidt norm; multiplication on the output by a fixed finite block has the same angular induced norm as in MSS.2. This avoids interpreting a Banach-valued sup over nodes as a Hilbert–Schmidt output space.

Write $\Gamma$ for the resulting weighted gain, using the two types independently. The homogeneous within-cell output has squared ordinary body norm bounded by
$$
 \Gamma^2\sum_i\bigl(
  \|U_i^*X_iU_i\|_2^{1/2} w_i^c+
  \|V_i^*X_iV_i\|_2^{1/2} w_i^d\bigr)^2 .
$$
The remaining true Duhamel kernel on that cell is $1_{s<t}O_i(t)G_i(s)$. Its complete positive Hilbert–Schmidt square is at most $h_i=\operatorname{tr}(X_iJ_{i,j})$, by integrating the full positive square over the entire cell rectangle. These diagonal-cell maps have mutually orthogonal domains and ranges. Their direct-sum Hilbert–Schmidt norm is bounded by $(\sum_i h_i)^{1/2}$, their operator norm by $(\max_i h_i)^{1/2}$. Add to the corresponding homogeneous norm by the triangle inequality. The root97 and exact $\Theta$-outer96 have the analogous two-block observation bounds. Take the Euclidean sum of the two independent output atoms and then body/atoms. Report the genuine Hilbert–Schmidt squares and the smaller admissible operator norm separately. The third source is the original square second-kind correction, preserving all 193 independent atom-input identities. For corrected body/atom gains $b,a$, its ordinary identity-plus-body upper is $(\sqrt{(2+b)^2+a^2}+\sqrt{b^2+a^2})/2$. The four source dimensions remain 193/193/193/128. Arbitrary $L^2$ source data suffice.

## MSS.4. Signed physical forcing and actual two-endpoint data

Given directed true physical signed jumps $f_i$, prescribed root and outer boundary data $A,B$, and any finite dyadic nodal trial $\bar c_i,\bar d_i$, form $\bar x_i=U_i\bar c_i+V_i\bar d_i$.
Use sign-preserving multiplication to form $\pi_kP_i(\bar x_{i+1}-T_i\bar x_i-f_i)$, $P_a(A-a\bar x_0)$, and $P_b(B-b\bar x_n)$. Bound the two triangular free sweeps by the ordinary, unsquared dyadic recurrence of MSS.2 because the same given signed columns occur in every cell and at both ends. If their weighted output upper is $d$, then at node $i$ the true physical correction lies in the joint induced ball about $\bar x_i$ of radius
$$
   (\|U_i\|_2 w_i^c+\|V_i\|_2 w_i^d)d/g.
$$
All nominal formation errors must be added in taking its finite dyadic centre. The implementation produces actual 193-row solution enclosures for all 1425 nodes, bound to a single authenticated model. Its deterministic floating sweep takes the correctly signed $-P_i f_i$ and both physical endpoint right sides. The subsequent directed residual is the proof for any trial it selects. The signed receiver can be applied to actual Newton and parameter families with matching whole source definitions and boundary bindings. A four-map norm bound on arbitrary $L^2$ does not supply those source values, and the preconditioner result alone does not assert a full physical nonlinear branch.

## Entry and reuse of actual science

The manifest maker admits the fixed GDC manifest and its terminal scientific/execution pair. A run still in progress enables no entry. A successfully proved low BVP also enables no second low-inverse entry. The admissible failed graph branch retains any genuine first new cell witness. The MSS computation consumes physical packets only. It recovers the three original TF81 carriers, then the 89 original GG packets with both their full native index and arrival-chain identity. It recovers any additional previously closed GDC packets, checking the entire sorted physical packet index, total bytes and each individual whole object on readback. Only after all needed original bytes match does it schedule previously missing cells. The GDC graph matrices and their denominators are not mathematical inputs to the two-sided MSS square operator. Its own new U/V/P/R/S matrices remain private alongside all native packets, complete local/weight evidence, signed solution arrays and source Gramians. No new mathematical target is claimed until its actual directed run pays it.
