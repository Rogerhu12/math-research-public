# R133 supplement: zero-Volterra preconditioning and the complete positive-head mesh contract

The positive radial-head equation admits an exact left preconditioning whose radial tail bound contains no evaluated exponential. This does not improve the norm of the true initial-value propagator by assertion: it changes the complete equation by an explicitly invertible Volterra factor. The kernel is preserved, the cokernel is transported by the inverse adjoint, and every source, initial, jump, endpoint and exterior column is transformed with the equation.

The accompanying readonly inventory identifies the actual whole-positive source columns and the three already completed per-cell coefficient fields. Their global maxima were not saved by the old producer. Those maxima, the new typed coupling combination and a declared mesh test are new targets. No new target has been evaluated for this note; no old producer or scientific formula has been rerun, and no native binary body has been fetched. In particular no feasible finite matrix or finite inverse is claimed.

## WHV1. Same operator, interval and physical ports

Use WHR.1--12 at the admitted selected member of the actual full real family. Thus
$$
 I_+=[r_*,R],\quad R=25/8,\quad
 \mathscr H=L^2(I_+;E_L),\quad \dim_{\mathbb R}E_L=193,
 \quad \mathscr V=L^2_rP_HH^{-1}_\phi .
 \tag{WHV.1}
$$
The angular fiber is the original fixed normalized raw $L^2$ reflection pair: the first component is odd, the second is even, and its physical mean remains. The measure is ordinary $dr$. The head cutoff is $|j|\le96$, the high cutoff is $|j|\ge97$, and physical frequency is $n=4|j|$.

Keep the exact WHR raw generator, including both ordered primitive convolutions and its complete physical mean rank. Write
$$
 A=A_L,\quad
 K=B_{LH}\mathcal P_a,\quad
 q_y=F_y y+f_L,\quad
 a'=Aa+Ka+q_y .
 \tag{WHV.2}
$$
Here the same completed positive high inverse gives
$v=\mathcal P_a a+\mathcal P_y y+v_f$.
The map $\mathcal P_a$ uses only the ordinary source $B_{HL}a$, with the original stable root, chart, height, mean and jump ports zero. Their independent columns remain in $\mathcal P_y$ or $v_f$. In particular $K$ may be noncausal in radius.

The coordinate $a_*$ is the actual initial low state, subject to all original root equations. The outer chart variable $b$ remains its original $H^{-5/6}$ low nonmean port; it is not renamed as the raw trace $a_R$. The complete chart relation among $b$, $a_R$, high endpoint, independent height and mean is retained. No statement here uses a waist trace isomorphism as a positive raw-bulk theorem.

## WHV2. Exact left factor, with the right side transformed

Set $\ell=R-r_*$ and define the ordinary zero-initial primitive
$$
 (V_0f)(r)=\int_{r_*}^{r}f(t)\,dt,\qquad
 C_*c(r)=c,\qquad
 (J_0\mathbf j)(r)=\sum_{r_*<r_\alpha\le r}j_\alpha .
 \tag{WHV.3}
$$
The last signs are the actual convention $[a]_{r_\alpha}=j_\alpha$; impulses have no radial-length multiplier.

Let $V$, $E_*$ and $J_L$ be the true same-$A$ operators in WHR.14--17. Variation of constants, first on smooth functions and then on their stated $L^2/H^1$ domains, gives
$$
 V=V_0+V_0AV,\qquad
 E_*=C_*+V_0AE_*,\qquad
 J_L=J_0+V_0AJ_L .
 \tag{WHV.4}
$$
Products have their displayed order. Introduce
$$
 B_0=Id-V_0A,\qquad F=Id-VK,\qquad
 H=A+K,\qquad F_0=Id-V_0H .
 \tag{WHV.5}
$$
Then
$$
 B_0V=V_0,\qquad
 \boxed{F_0=B_0F},\qquad
 B_0E_*=C_*,\quad B_0J_L=J_0 .
 \tag{WHV.6}
$$
Indeed $B_0VK=V_0K$, without commuting $A$, $K$ or $V$.

The factor $B_0$ is invertible on $\mathscr H$. For example, the iterated Volterra kernels are bounded by the usual simplex factors
$(\ell\|A\|_\infty)^k/k!$, so their series converges without any smallness hypothesis. This is an existence proof, not a new numerical exponential bound and not a norm estimate for $F_0^{-1}$.

Consequently the complete low equation is exactly
$$
 \boxed{\quad
 F_0a=C_*a_*+V_0(F_yy+f_L)+J_0\mathbf j .
 \quad}
 \tag{WHV.7}
$$
Every right-side term changes with the left factor. Replacing only $V$ in $VK$ while retaining $E_*$ or $J_L$ would give a different equation.

Conversely, a solution of (WHV.7) satisfies
$a-J_0\mathbf j\in H^1$ and the original differential equation with its actual initial value and jumps. Thus (WHV.7) has exactly the original solutions. No derivative of an arbitrary ordinary source, of a coefficient seam, or of the noncausal map $K$ was introduced.

## WHV3. Trace-safe endpoint and the cokernel

The endpoint is now the bounded full-$L^2$ row
$$
 \boxed{\quad
 a_R=a_*+
  V_{0,R}\bigl((A+K)a+F_y y+f_L\bigr)+\sum_\alpha j_\alpha,
 \qquad V_{0,R}f=\int_{r_*}^{R}f(t)\,dt .
 \quad}
 \tag{WHV.8}
$$
On solutions this is the actual raw trace. For an auxiliary $L^2$ variable it is the declared bounded row, not a nonexistent trace functional $a\mapsto a(R)$. Every direct term in the original exterior equations must be updated when (WHV.8) replaces the old Green endpoint formula. The original chart $b$ and its complete high, height and mean matching are untouched.

Because $B_0$ is invertible,
$$
 \ker F_0=\ker F,\qquad
 \ker F_0^*=B_0^{-*}\ker F^*,\qquad
 \operatorname{ind}F_0=0 .
 \tag{WHV.9}
$$
The old cokernel basis is not copied unchanged. If $W_0$ spans $\ker F^*$, the compatibility rows for a datum $g_0$ are
$W_0^*B_0^{-1}g_0=0$.
The transported columns need not remain orthonormal.

If $G$ is the original restricted inverse on the compatible range, then
$GB_0^{-1}$ is a compatible solution operator for $F_0$; this is not a new claim about its norm or a newly chosen Moore--Penrose inverse. Likewise a trace-safe completion $U_+\subset H^1$ transports to $B_0U_+\subset H^1$. Its unknown finite dimension is still $m_H$. Neither the stable root $m=0$ result nor this preconditioning proves $m_H=0$.

One may instead formulate the entire system directly from (WHV.7)--(WHV.8), retaining every original observation on its qualified core. This is convenient for the new tail test and avoids numerically evaluating $B_0^{-1}$.

## WHV4. Radial constants without an evaluated exponential

In the fixed Euclidean angular fiber and ordinary radial measure,
$$
 \|V_0\|_{\mathscr H\to\mathscr H}=\frac{2\ell}{\pi},
 \qquad \|\partial_rV_0\|=1,\qquad
 \|V_{0,R}\|_{\mathscr H\to E_L}=\sqrt{\ell}.
 \tag{WHV.10}
$$
For the first bound write $w=V_0f$, reflect $w$ evenly across $R$ onto an interval of length $2\ell$, and apply the Dirichlet Poincare inequality. Both squared norms double. Equality is attained by a scalar multiple of
$\sin(\pi(r-r_*)/(2\ell))$ in one fixed unit fiber direction.
The other two statements follow from differentiation and Cauchy--Schwarz.

If complete bounds $A_\infty\ge\|A\|$ and $C_K\ge\|K\|$ are supplied, then
$$
 T_0=V_0(A+K),\qquad
 \|T_0\|\le \frac{2\ell}{\pi}(A_\infty+C_K),
 \qquad
 \|\partial_rT_0\|\le A_\infty+C_K .
 \tag{WHV.11}
$$
This operator is compact through $H^1(I_+;E_L)$, even though $K$ is noncausal.
These are bounds for the new exact integral formulation. The old true-$V$ constants $C_V,C_D,C_R$ in WHR.16 have not been lowered by assertion or reevaluated.

## WHV5. Actual old fields and their input/output types

The whole-positive negative-one summary of run 43627228225 has the exact input order
$$
(s,F_c,F_b,B,J_c,J_s,J_u).
$$
Its already saved complete raw-state row is
`response_rows.entire_positive_raw_L2r_Hminus1`.
Only entries 1 and 2 are used in the self-feedback estimate:
$$
\begin{split}
 C_c&:\ L^2(I_c;H^{-2/3}_\phi)\longrightarrow\mathscr V,\\
 C_b&:\ L^2(I_b;H^{-2/3}_\phi)\longrightarrow\mathscr V,
\end{split}
 \tag{WHV.12}
$$
where $I_c=[r_*,c]$, $I_b=[c,R]$ and
$c=1192029371497/5000000000000$.
They are complete whole-interval state columns, not body-only endpoint fees. Their original ball strings are:

- $C_c$: `[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]`;
- $C_b$: `[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]`.

The ordinary source norm is precisely $L^2_rH^{-2/3}_\phi$ and the raw output is $L^2_rH^{-1}_\phi$. The independent even mean is separate in that high output and remains in the low equation. No new factor from the Riccati frame, primitive reconstruction or root coordinate change is applied to (WHV.12).

The successful collar process, using its complete real-family degree96 background, already saves these exact rational strings:
$$
 A_{c,\rm raw}=23/2,\qquad
 L_{c,\rm raw}=58/5,\qquad
 G_c=62286/125 .
 \tag{WHV.13}
$$
Their paths are respectively
`exact_rational_contract.low_to_high_L2`,
`high_to_low_L2`, and `low_generator_upper`.
The last includes the principal low derivative, full local matrix, complete primitive and physical mean rank. It is the same $A_L$ of WHR.9 on the collar.

The original full-delta body source saves, in every one of its 4,650 closed rows and in each completed order,
$$
\begin{split}
 A_{HL,i}&=384d_i+L_{{\rm raw},i}+N_{{\rm raw},i},\\
 A_{LH,i}&=A_{HL,i}+d_{\phi,i},\\
 G_i&=384\,\eta_{+,i}\max(1,K_{+,i})
       +A_{HL,i}+M_{{\rm raw},i}.
\end{split}
 \tag{WHV.14}
$$
Here all terms are the full inflated real-family upper fields; $N_{\rm raw}$ is the ordered primitive fee and $M_{\rm raw}$ the complete mean-rank fee.
For order zero, the exact saved fields are:

| Field in `orders[0].complete_rows[i].bounds` | Proved type |
|---|---|
| `low_to_high_source` | $B_{HL}:E_L\to H^{1/3}_\phi$ |
| `high_to_low_raw` | $B_{LH}:L^2_\phi$ on its true shell $\to E_L$ |
| `head_generator` | $A_L:E_L\to E_L$ |

This table is (WHV.15). The first is formed with the complete output shell factor
$\langle1152\rangle^{1/3}$; the second is an upper bound for $A_{LH,i}$ and therefore also for $A_{HL,i}$. This uses the positive defining formula (WHV.14), not subtraction of independently rounded upper bounds.

The body producer does not save the maxima of these three fields. They are absent from both its 21,555-byte summary and its 8,744-byte outcome. Define the genuinely new named targets
$$
 H_b=\max_i H_i^{\rm saved},\qquad
 L_b=\max_i L_i^{\rm saved},\qquad
 G_b=\max_i G_i^{\rm saved}.
 \tag{WHV.16}
$$
Each maximum must inspect all 4,650 original complete row records and retain the selected original record, index and exact interval. The old coefficients, inflation, lower flows, 4,650 kernels, 3,594 interfaces and all source sweeps are only read; none is run again.

## WHV6. Complete coupling combination with the actual negative source window

Put $\Lambda_0=(1+388^2)^{1/2}$. Since the output of $B_{HL}$ lies in $|n|\ge388$,
$$
 A_c=\Lambda_0^{-2/3}A_{c,\rm raw},\qquad
 A_b=\min\{\Lambda_0^{-1}H_b,\ \Lambda_0^{-2/3}L_b\}
 \tag{WHV.17}
$$
are complete bounds for $B_{HL}$ from its respective raw head $L^2$ domain to the required $H^{-2/3}$ source space.
The first body candidate uses
$\|f\|_{H^{-2/3}}\le\Lambda_0^{-1}\|f\|_{H^{1/3}}$.
The second uses the raw bound in (WHV.14).
The two complete candidates are both retained before choosing their whole minimum.
The low-input frequency is not substituted for the high-output frequency in either argument.

The two radial restrictions of $a$ have orthogonal ordinary-$dr$ norms. Thus the triangle inequality for the two complete graph outputs, followed by scalar Cauchy--Schwarz on the input split, gives
$$
 \|\mathcal P_a\|
 \le C_P:=
   \sqrt{(C_cA_c)^2+(C_bA_b)^2}.
 \tag{WHV.18}
$$
No orthogonality of those two output states is asserted. The old sum bound remains valid but is unnecessary.

The true high-to-low input shell is $97\le|j|\le288$. Its Bessel conversion is the original saved factor 1153, so
$$
 L_*=\max\{58/5,L_b\},\qquad
 \boxed{\ C_K=1153L_*C_P,\qquad
         A_\infty=\max\{62286/125,G_b\}.\ }
 \tag{WHV.19}
$$
This factor is used only after the exact shell restriction in $B_{LH}$.
There is no assumption that the unknown high state is band-limited.
The physical mean and all primitive factors remain in their original operator positions.

## WHV7. New mesh gate and exact finite rows

Use the same ordinary cell-average projection $\Pi_N=E_NE_N^*$ as WHR.27.
It has output dimension $193N$, not a finite restriction of the input.
For maximum cell length $h_{\max}$,
$$
 \|(Id-\Pi_N)T_0\|
 \le\varepsilon_{0,N}:=
       \frac{h_{\max}}{\pi}(A_\infty+C_K).
 \tag{WHV.20}
$$
This follows from $\partial_rT_0=A+K$ and the cellwise vector Poincare inequality. It requires no coefficient radial derivative and no derivative of an ordinary source. Genuine prescribed jumps stay in the complete right side of (WHV.7).

If, and only if, a retained outward comparison proves $\varepsilon_{0,N}<1$, define
$$
 R_{0,N}=Id-(Id-\Pi_N)T_0,\quad
 W_N=E_N^*T_0,\quad
 F_0=R_{0,N}-E_NW_N,\quad
 \|R_{0,N}^{-1}\|\le(1-\varepsilon_{0,N})^{-1}.
 \tag{WHV.21}
$$
For a cell $I_i=[l_i,r_i]$ of length $\ell_i$, the full dual row is explicitly
$$
 (W_Na)_{i,k}
 =\int_{r_*}^{R}w_i(t)
    \langle e_k,\,A(t)a(t)+B_{LH}(t)(\mathcal P_a a)(t)\rangle\,dt,
 \tag{WHV.22}
$$
where
$$
 w_i(t)=
 \begin{cases}
 \sqrt{\ell_i},&t<l_i,\\
 (r_i-t)/\sqrt{\ell_i},&l_i\le t\le r_i,\\
 0,&t>r_i .
 \end{cases}
 \tag{WHV.23}
$$
Fubini proves (WHV.22). Its argument is the full $L^2$ head function, including the entire noncausal high response. The row is not replaced by a finite vector of sampled head inputs.

For the complete system, write (WHV.7) as
$F_0a=\mathscr B_0y+f_0$, and write all remaining actual rows, with the trace-safe endpoint (WHV.8), as
$\mathscr C_0a+\mathscr D_0y=g_0$.
Then with $z_N=W_Na$ the exact remaining system is
$$
 \begin{pmatrix}
 \mathscr D_0+\mathscr C_0R_{0,N}^{-1}\mathscr B_0&
                 \mathscr C_0R_{0,N}^{-1}E_N\\
 -W_NR_{0,N}^{-1}\mathscr B_0&
                 Id-W_NR_{0,N}^{-1}E_N
 \end{pmatrix}
 \binom{y}{z_N}
 =
 \binom{g_0-\mathscr C_0R_{0,N}^{-1}f_0}
       {W_NR_{0,N}^{-1}f_0}.
 \tag{WHV.24}
$$
Both directions are obtained by substituting
$a=R_{0,N}^{-1}(\mathscr B_0y+f_0+E_Nz_N)$.
All cross blocks remain. The bottom right finite block and the whole system are not asserted invertible. Any independently unknown functional part of $y$ remains infinite-dimensional.

Cellwise constant auxiliary columns need not have a raw $H^1$ trace.
The bounded endpoint formula is therefore retained before the auxiliary constraint is imposed. After the full equivalent system holds, the reconstructed $a$ has exactly the original regularity and genuine prescribed jumps.

## WHV8. Minimal readonly admission and the new scalar targets

The nine core text inputs, their complete bytes and hashes, thirteen historical part tuples and typed field paths are recorded in
`notes/2026-11-16-R133-zero-Volterra-positive-head-readonly-input-inventory.json`.
The inventory is a static input contract, not an actual numerical result.

The original successful body native is 25,507,783 bytes with SHA256
`1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c`.
Its thirteen original lossless pieces were published at
`12b06502f2e4d522ca5dc16d6064267859b3a0a1`.
Their current small manifest is 6,002 bytes, blob
`aabe1eb46cb52e41c8191960a2a998b437ca47e7`,
SHA256 `7b1967565a0ff0a4d9855734a3f0a0621c8049160099e066d8f34ecb35cdd3a3`.

An authorized public Actions consumer may temporarily restore precisely those immutable parts. It must verify each Git blob/size, compressed SHA, decompressed chunk SHA/offset, then the concatenated original gzip's exact size and SHA before decoding its complete JSON. The author has read only the small manifest and directory/history metadata, not any binary body. Historical inputs remain temporary and are not restored into the current publication tree.

The old generic container manifest has `complete_native_rows: 0` and `candidate_sha256: null`. Those original metadata values are preserved; they are not changed to 4650 or treated as permission to skip the actual native rows. The correct complete counts and identity are taken from the native's actual fields, bound to its successful source and process.

The admission must check the original complete body gates, both orders, all 4,650 exact contiguous intervals and all 3,594 original interfaces; every published summary field except its publication-only native hash must agree with the corresponding complete native value, removing only the two per-order row arrays for that comparison. The original progress counter `actual_new_scalar_rows: 4608` is retained; the complete cover is the separate `complete_original_rows: 4650` together with both full row arrays. The negative-one process/summary bind the exact same native, real family, genuine reference and complete seven-input/eight-output graph. The collar process/source bind the same repaired centre, direction, intrinsic metric, actual root piece and complete 19-gate success. Old producers are read or parsed as text only.

Only the following are new scientific work:

1. The three complete maxima (WHV.16), with exact original winner records and full-cover evidence.
2. The two complete body negative-window candidates, the complete orthogonal-input combination and the full bounds (WHV.17)--(WHV.19).
3. The ordinary zero-Volterra constants and a declared radial mesh:
$$
 \ell_+=25/8-r_-,\quad
 r_-={1191984371497\over5000000000000},\quad
 C_{V_0}=2\ell_+/\pi,\ C_{D_0}=1,\ C_{R_0}=\sqrt{\ell_+},
 \quad
 \varepsilon_{0,N}^{+}
   ={\ell_+\over N\pi}(A_\infty+C_K).
 \tag{WHV.25}
$$
The same root enclosure is an exact literal guarded by the original successful collar source, with upper endpoint
$2383968743003/10000000000000$.
It is not a new root solve. A uniform $N$-cell partition of the true interval has cell length at most $\ell_+/N$.
The final new target is the comparison made from the finally saved outward $\varepsilon_{0,N}^{+}$, and only after a passed comparison the associated remainder-resolvent upper bound.

All original nonnegative upper-bound records are read by upper endpoint. Denominators such as $\pi$ use positive lower endpoints. New negative powers are applied to the positive exact $\Lambda_0$ with directed enclosure. Maximum and minimum selection use the outward endpoints of complete candidates, retain deterministic tie-breaking, and copy the selected original literals without rewriting them.

The manifest must declare the tested integer $N$ and a finite resource cap before execution. A conservative required-mesh diagnostic may be saved separately, but a huge integer is not called a practical construction. The output must give the exact dimension $193N$, the actual saved gate, and whether it is within that declared cap. A false gate is a complete scientific outcome. This scalar consumer does not allocate a dense finite matrix, solve a finite pairing, or infer the signs of matrix entries from norm bounds.

Every completed new maximum or graph is saved before proceeding, with a recoverable partial prefix. An unfinished wrapper cannot authorize redoing already saved new targets. The completed collar, positive body, negative-one graph, Riccati reference, original whole source columns and exterior solution remain frozen.

## WHV9. Exact progress and remaining obligations

The completed analytic statement is the equivalence (WHV.6)--(WHV.8), its kernel/cokernel rule (WHV.9), and the exponential-free radial test and full finite factor (WHV.20)--(WHV.24). These hold without evaluating a new scalar or assuming a finite inverse.

The old source columns are already small complete graph coefficients in their proper units. The three body maxima have not yet been inspected as numerical values outside their immutable native. Accordingly this note does not claim that (WHV.20) passes at an affordable mesh.

After a passed mesh gate, signed pairings for (WHV.22) and every column and cross row in (WHV.24) remain a separate actual target. The unknown $m_H$, the genuine 96 physical columns and their required normalization, all 96 $\Theta$ constraints, WFR root factors, WCF finite primitive/rank factors, both stored density means and the independent physical mean equation, the complete metric-$\nu$ column and every external function remain. The negative-side radial head is outside this positive-interval proof.

The old numerical inputs are uniform on the stated real family. This can make the same norm test uniform on that common fixed intrinsic positive interval. It does not prove operator-norm continuity of the feedback, constancy of $m_H$, a uniform finite determinant or a full physical inverse. None of these follows merely from a stable map's strong continuity.

## WHV10. Complete small primary identities

All paths are relative to `topics/visible-flex-exact-nearby/`. The inventory gives the full paths for the nine current core inputs. The following references fix the operator and norm qualifications.

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WHR, exact positive radial-head reduction and trace-safe factors | 0cb48560534119452e71ec1bc6e23df7af245943 | 28267 | 289935c35a77f706ce4f9c151ae40c85b67e14743899eaed293747e5704dbad4 |
| Complete moving-root scalarization, N.3--9 | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| Full-delta negative-one positive source and regular-port contract | 6765382c0ea8af731b6593b687cbc84401a4f7ec | 15756 | 0f1383da8611aef931829876b49579f41c7a967435c795ef68a85d2a142cac23 |
| Actual negative-one positive graph | 8b28bcd0929df468f44186236dd0cf2e9c037dad | 10464 | e144ad9f8cd7dbc29904f92524e9da9511f4bb8d403e06620d8ad85f3105742c |
| Full real-family collar actual | bc92fb193bd8243ae148e07158f7652baabe0f53 | 5049 | 5be836ea9a5f83490f5853e8d06fdc02d67e8631ec8a5e2cdf2f5944156837cc |
| Complete M32/M96 body transfer and coupling source norms | 097f1bdd3e99c7d03a931582e9e99cf83160e142 | 8111 | 4e37dc2bc049ec2c9cc3942a7c1986aae7c3ce3ab733049cab905f3fde840405 |
| Exact M32 transfer, complete ordered couplings | 03642d2b5a277a56cf46c0ee94351ceb0431d6f3 | 16348 | a6c604bc4bb11522f5cc7538dc8f9ed857dfc61474e80a3c350b9310295f6dba |
| Actual full-real-delta outer and positive body | 2be2a1c031d556ea3d1782d6c71788f299a2f70f | 8299 | 23379fe44df4ab46ebd0b49f4749907f95701781d78a9f26b1a77d1ffbe9f810 |

The three original scientific sources are pinned as readonly UTF-8 evidence in the inventory. No old source is imported by this contract, and no native binary body has been fetched or evaluated here.
