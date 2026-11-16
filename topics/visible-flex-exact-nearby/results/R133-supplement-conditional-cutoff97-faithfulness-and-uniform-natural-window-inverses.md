# R133 supplement: conditional cutoff97 faithfulness and uniform natural-window inverses

2026-11-16, tail_connector.

**Conditional analytic result. The R97 strict comparison has not been executed or assumed to pass in this note. No new scientific arithmetic is performed.** A later same-family certificate with a strictly positive uniform margin would remove the parameter kernel, cokernel and FC completion for the original high Ai family. The proof below also gives uniform bounded inverses on its two fixed natural negative windows, with separate smoothing constants. It does not transfer the L2 numerical inverse bound to either negative window.

## RNI1. Fixed objects and exact primary identities

Use the real family $Q_\delta=Q_0+\delta Z$, $|\delta|\le d=10^{-8}$, at fixed intrinsic $\eta_0$, on the original root piece. The moving speed $\eta_\delta=-\gamma m_\delta$ is not that intrinsic parameter. The intrinsic bump is zero on this root piece, as in B.2 and the R97 input qualification.

The circle, normalized measure, reflection realization and both physical frequency signs are exactly those of SE1. Let $\mathcal H^t=\mathcal H_H^t$ be the fixed original high coordinate space $|j|\ge97$, with Bessel weights $(1+16j^2)^{1/2}$. Let $N e_j=4|j|e_j$ on this high space. Neither a frequency inverse nor an old-circle inverse is applied to an independent physical mean.

| Primary | Immutable Git blob | Bytes | SHA256 |
|---|---|---:|---|
| R97, original-cutoff scalar recipe | cc0d98891f52a8c6ec1c718c57d7be143db0134c | 20143 | 543ebc3899931db63bda92c31ce20d8f21013daac906e00eaf761a28ff582f74 |
| RD, exact stable row and full error | 24b3523585bdfe9f1d96b57e3ca2e4f0727fd2d4 | 17725 | 34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f |
| SE, natural stable Fredholm structure | eb7b1bb1ea1fdf713fcf172428f68ed20afafdb2 | 20047 | 2220174707046248cbdf9f9f8c47bc13bc233b0ab65f5ed598ddcbf964e93ad4 |
| FC, finite completion of the same graph | 8b7ff6fe74fa4ce914c8bc0c2192deae85ce0768 | 20794 | 46ccc206c86afef16ee3d3221162f0e5c373ad8420283bc9fbe40e52fe3e24bd |
| B, full-real-parameter root construction | e561b822673bbce15c1391ee851fb93d4143d43e | 15703 | f5f980a1fb085103f548d7bbdf6fe0124dda176276fa1b8bac6783b6b22a150c |
| RBO, ordered powers and complete mean row | 6d6a8f44edaf99ae4613c53addcd3682a86df82e | 18718 | a45e0264875c1a5cded48c6f108004f3c21b6ade73247a7b02231d9b26a30f50 |
| BF, complete finite-factor realization | 921dbfc574e94da86c8d44872a919c201c569060 | 19339 | e8e29c49deb9fabf6be9b9dd9059c26e94afbd1bc274742d7d3fe7527bf4a02e |

The corresponding texts are [R97](R133-supplement-complete-root-cutoff97-scalar-recipe.md), [RD](R133-supplement-exact-leading-root-derivative-and-complete-stable-trace-gate.md), [SE](R133-supplement-natural-stable-port-Fredholm-and-exact-reference-elimination.md), [FC](R133-supplement-finite-Fredholm-completion-of-the-actual-regular-Ai-graph.md), [RBO](R133-supplement-ordered-genuine-root-input-powers-and-complete-mean-row.md), and [BF](R133-supplement-retained-finite-factors-and-complete-bordered-incoming.md). The B identity and common-domain statements used here are its sections 1--3, particularly B.2 and the paragraph giving uniform root coefficient constants.

RD.21--24 give the exact factorization
$$
 S_{{\rm nat},\delta}=\mathcal M_\delta\widehat S_\delta,\qquad
 \widehat S_\delta=D_{g,\delta}+E_\delta,\qquad
 \mathcal M_\delta e_j=(1+\widetilde p_{j,\delta})^{-1/2}e_j,
 \quad 0<\widetilde p_{j,\delta}<66 .
 \tag{RNI.1}
$$
The positive output diagonal stays on the left. In particular, on every fixed $\mathcal H^t$,
$$
 \|\mathcal M_\delta\|\le1,\qquad
 \|\mathcal M_\delta^{-1}\|\le\sqrt{67}.
 \tag{RNI.2}
$$
The actual PC correction has zero stable root input, so these are the stable traces of the corrected high family, not merely its formal leading columns.

## RNI2. The single conditional numerical premise

Assume that a later complete R97 receipt, with the exact input and output qualification of that contract, supplies common constants
$$
 \|E_\delta\|_{\mathcal H^0\to\mathcal H^0}\le e,\qquad
 0<g_-\le g_{j,\delta}\le g_+<\infty,\qquad
 \mu:=g_--e>0
 \tag{RNI.3}
$$
for every stated real $\delta$ and every original $|j|\ge97$. The lower and upper endpoints used for the comparison must be the actually retained outward records. A pointwise-parameter pass, a larger cutoff, or a truncated error does not supply (RNI.3).

The same R97 inputs permit the symbolic upper choice
$$
 g_+=A_*+\lambda_+D_*/\eta_-.
 \tag{RNI.4}
$$
This note does not evaluate it or any other new scalar. Formula (RNI.4) just bounds the exact genuine diagonal $A_n-(\lambda/\eta)D_n$ by its two complete amplitude bounds.

The Neumann argument around $D_{g,\delta}$ gives
$$
 \|\widehat S_\delta^{-1}\|_{\mathcal H^0\to\mathcal H^0}
       \le\mu^{-1},\qquad
 \|S_{{\rm nat},\delta}^{-1}\|_{\mathcal H^0\to\mathcal H^0}
       \le\sqrt{67}\,\mu^{-1}.
 \tag{RNI.5}
$$
These are exactly the L2 inverse conclusions in RD6, now with an explicitly uniform premise. The complete positive mean-rank term and $IR_0$ cost $r_0/4$ remain inside $e$; no high-input primitive replacement is made.

## RNI3. A finite smoothing formula for a uniform negative-window inverse

Here is the elementary Banach-scale fact used below. Suppose $A_\delta$ is one compatible family on a Sobolev scale and, for each of finitely many exponents needed,
$$
 \|A_\delta:H^q\longrightarrow H^{q+\alpha}\|\le a_q,
 \qquad \alpha>0,
 \tag{RNI.6}
$$
uniformly in $\delta$. Assume $B_{0,\delta}=(1+A_\delta)^{-1}$ exists on $H^0$ and $\|B_{0,\delta}\|\le b_0$ uniformly.

Fix $t<0$ and an integer $m$ with $t+m\alpha\ge0$. Define
$$
 B_{t,\delta}
 =\sum_{k=0}^{m-1}(-A_\delta)^k
       +(-1)^m B_{0,\delta}A_\delta^m:
             H^t\longrightarrow H^t .
 \tag{RNI.7}
$$
The last composition is well typed: $A_\delta^m$ first maps into
$H^{t+m\alpha}\subset H^0$, then $B_{0,\delta}$ acts on $H^0$, which embeds in $H^t$. Its order is not reversed.

The finite geometric sum gives
$$
 (1+A_\delta)\sum_{k=0}^{m-1}(-A_\delta)^k
     =1+(-1)^{m-1}A_\delta^m .
$$
The last term in (RNI.7) cancels this remainder, because
$(1+A_\delta)B_{0,\delta}A_\delta^m=A_\delta^m$.
The right-inverse identity follows either by
$A_\delta^m(1+A_\delta)=(1+A_\delta)A_\delta^m$
on the compatible spaces, or by the following uniqueness argument:
a distributional kernel vector satisfies $x=-A_\delta x$, improves by
$\alpha$ repeatedly, reaches $H^0$, and is zero there. Thus (RNI.7) is the two-sided inverse and agrees with $B_{0,\delta}$ on the overlap.

With empty products equal to one, a complete uniform bound is
$$
 \|B_{t,\delta}\|
 \le \mathfrak B_t:=
  \sum_{k=0}^{m-1}\prod_{r=0}^{k-1}a_{t+r\alpha}
       +b_0\prod_{r=0}^{m-1}a_{t+r\alpha}.
 \tag{RNI.8}
$$
The embeddings in this formula have norm at most one for the stated Bessel scale. No smallness of the smoothing constants $a_q$ is required. They must be finite and uniform on the same parameter domain.

This is a finite algebraic formula, not a numerical Neumann iteration in a negative norm. It introduces no new Fourier cutoff.

## RNI4. Why the root smoothing constants can be uniform

SE2 proves the complete weighted Fourier estimate for input-dependent coefficients on a common positive angular strip. B section 3 supplies common root coefficient domains over the full stated real interval. Passing to one fixed smaller strip gives uniform constants for every fixed derivative order and every fixed finite collection of Sobolev exponents.

The old-circle inverse also admits uniform fixed-window bounds from its already uniform L2 derivative input, without presuming a negative-window number. Keep its original parity spaces and write
$$
 \mathscr A_\delta=\eta_\delta\partial_\phi+L_\delta,\quad
 P_\delta=\eta_\delta^{-1}I,\quad
 \mathscr A_\delta P_\delta=1+R_\delta,\quad
 R_\delta=L_\delta P_\delta .
 \tag{RNI.9}
$$
Here $P_\delta$ maps even mean-zero data into the odd domain.
$R_\delta$ gains one derivative uniformly on every fixed exponent needed, because $\eta_-$ is positive and the complete coefficients of $L_\delta$ have the common smooth bounds. On L2,
$$
 (1+R_\delta)^{-1}
      =\eta_\delta\partial_\phi J_\delta,\qquad
 \|(1+R_\delta)^{-1}\|\le \eta_+J_1 .
 \tag{RNI.10}
$$
This is the original left angular derivative of the genuine $J$. The root producer's ordinary-L2 qualification, independently recorded in RI/R97, is needed here. A Wiener norm or a right derivative estimate is not substituted for it.

Apply (RNI.7)--(RNI.8) with gain one to obtain uniform inverses of $1+R_\delta$ in the finitely many negative windows used by the root reconstruction. Then
$$
 J_\delta=P_\delta(1+R_\delta)^{-1}
 \tag{RNI.11}
$$
has the corresponding uniform one-derivative bounds. No independent mean is included in its domain.

SE4--7 and RD.24 now give, for each required fixed $q$,
$$
 \|E_\delta:\mathcal H^q\longrightarrow
                 \mathcal H^{q+2/3}\|\le e_q<\infty
 \tag{RNI.12}
$$
uniformly over the same real family. All constants in this statement include complete coefficient, inverse and primitive products. Equivalently one can start from SE's $S_{\rm nat}=D_c+K$ gain and remove the bounded output diagonal. Changing its free leading diagonal to RD's exact genuine $D_g$ subtracts only a diagonal of order $-4/3$, because the full nonzero shear satisfies the original uniform $|\beta_n|\le C_\beta n^{-4/3}$. Thus the gain $2/3$ persists.

No new value of $e_q$ is claimed. Their finiteness and uniformity follow from the common-domain analytic estimates and the finite formula above; an explicit numerical negative-window inverse would still require actual bounds for these constants.

Set
$$
 A_\delta=D_{g,\delta}^{-1}E_\delta,\qquad
 b_0=g_+/\mu,\qquad a_q=e_q/g_- .
 \tag{RNI.13}
$$
Then $\widehat S_\delta=D_{g,\delta}(1+A_\delta)$ and
$B_{0,\delta}=\widehat S_\delta^{-1}D_{g,\delta}$.
Apply (RNI.7) with $\alpha=2/3$. In the two natural windows,
$$
 \begin{array}{c|c|c}
 t&m&t+2m/3\\ \hline
 -7/6&2&1/6\\
 -5/2&4&1/6
 \end{array}
 \tag{RNI.14}
$$
and the precise inverse order is
$$
 \widehat S_\delta^{-1}=B_{t,\delta}D_{g,\delta}^{-1},
 \qquad
 S_{{\rm nat},\delta}^{-1}
       =B_{t,\delta}D_{g,\delta}^{-1}\mathcal M_\delta^{-1}.
 \tag{RNI.15}
$$
Consequently
$$
 \|\widehat S_\delta^{-1}\|_{\mathcal H^t\to\mathcal H^t}
       \le\mathfrak B_t/g_-,
 \qquad
 \|S_{{\rm nat},\delta}^{-1}\|_{\mathcal H^t\to\mathcal H^t}
       \le\sqrt{67}\,\mathfrak B_t/g_-.
 \tag{RNI.16}
$$
These are separate symbolic bounds, using the complete sequence of gain constants in (RNI.8). They do not identify either negative-window norm with $\mu^{-1}$ or $\sqrt{67}\mu^{-1}$.

## RNI5. The exact common-input inverse and its domain qualification

On any selected coordinate realization already qualified by SE8, retain
$$
 N_i=\Lambda_+^{-1}T_F^{-1}\mathcal S^{-1}:
       \mathcal X_s\longrightarrow\mathcal H^s,
 \qquad
 C_s=N_{\rm out}^{-1}S_{\rm nat}N_{\rm in}^{7/6}N_i .
 \tag{RNI.17}
$$
Here $\Lambda_+$ is the original nonzero leading scalar diagonal.
The high space $\mathcal X_s$ is the actual transported high space;
the low complement and physical means are separate. No factor is moved
through $\mathcal S$, a sign operator or a projection.

Under (RNI.3), the same exact inverse is
$$
 C_s^{-1}
 =N_i^{-1}N_{\rm in}^{-7/6}
       S_{\rm nat}^{-1}N_{\rm out}:
       \mathcal H^{s-1/6}\longrightarrow\mathcal X_s .
 \tag{RNI.18}
$$
The natural exponent is $t=s-7/6$. Thus $s=0,-4/3$ use precisely (RNI.14). The inverses agree on their common distributional core.

The full-real-parameter root conclusion does not supply an unproved
full-real-parameter selected-angle family. At a single certified selected
state, (RNI.18) uses its actual two-window $N_i$ and inverse. A uniform
statement for $C_{s,\delta}^{-1}$ on fixed identified spaces additionally
requires uniform two-window bounds for the actual $N_{i,\delta}$,
$N_{i,\delta}^{-1}$ and the identifications of $\mathcal X_{s,\delta}$.
Those assumptions are not inferred from one selected KAM or coordinate certificate.

## RNI6. What the full original97 gate would remove

FC2 identifies the smooth, window-independent spaces
$E_{\rm ker}=\ker S_{\rm nat}$ and
$F_{\rm cok}=\ker S_{\rm nat}^*$, with equal dimension $m$.
Under (RNI.3), (RNI.5) gives both
$$
 E_{\rm ker}=F_{\rm cok}=\{0\},\qquad m=0 .
 \tag{RNI.19}
$$
This is the kernel and cokernel of the complete original high stable operator, not a later finite compression. FC's empty-sum convention therefore gives exactly
$$
 W=0,\qquad F_C=0,\qquad C^\sharp=C,\qquad
 \widetilde\Psi_i=\Psi_i .
 \tag{RNI.20}
$$
No kernel/cokernel bases, completion dual norms, or additional Poisson columns from FC.16 and FC.23--26 are then required.

By FC5--6, the original corrected Ai coordinates themselves faithfully cover the same entire smooth regular given-head graph. The former use of complete incoming injectivity to deduce stable-coordinate faithfulness in SE9 is unnecessary after this independent root gate. No complete incoming conclusion is used to prove (RNI.19).

| Obligation | Consequence under the full uniform premise (RNI.3) |
|---|---|
| Original high stable parameter kernel and cokernel | Both vanish at the original cutoff 97 in the fixed natural windows. |
| FC completion $W,F_C$ and its new finite columns/dual rows | Exactly zero; no completion basis needs to be chosen. |
| A second reference used solely as another basis for the same regular given-head graph | It may be replaced by the faithful original Ai coordinate map. This is exact graph coverage, not a finite-rank approximation. |
| A genuinely independent second input, nonregular datum, exterior datum or ordinary source | Retained in its original port space. |
| Both physical mean equations and the original low Fourier complement | Retained; they are not elements of $\mathcal H_H^t$. |
| The whole radial head $L^2_r(\mathbb C^{193})$ and its high/low coupling | Retained as an infinite-dimensional source port. |
| Other actual finite columns, transported head rows and finite/high cross maps in BF/BT | Retained with their own complete factors or bounds. They are unrelated to FC's now-zero completion. |
| Global sign ordering, opposite-sign terms and complete strong errors | Retained in their actual ordered locations. |
| Complete incoming inverse and the remaining finite Schur system | Still require their own full square realization and actual proof. |

For the complete incoming/outgoing maps with all rest ports, one now has
$$
 \mathbb I_A=\mathbb I_P\mathbb D_C,\qquad
 \mathbb O_A=\mathbb O_P\mathbb D_C,\qquad
 \mathbb D_C=\operatorname{diag}(C_s,1_{\rm rest}).
 \tag{RNI.21}
$$
The common factor is invertible by (RNI.18), without an incoming hypothesis.
The complete incoming maps are therefore equivalent as to invertibility
on a declared bounded square realization. Only once that complete
invertibility is proved may one write
$$
 \mathbb O_P\mathbb I_P^{-1}
       =\mathbb O_A\mathbb I_A^{-1}.
 \tag{RNI.22}
$$
This is the original common right-factor cancellation. It does not
move a factor through a physical mean row, a density map or the
Maslov operator. If only smooth physical traces were previously
defined, the bounded trace-extension qualification in FC8/SE10 remains;
no new rough bulk Poisson theorem follows.

## RNI7. Parameter continuity: normalized root, true frame and selected charts

The normalized root family can be considered on the fixed
$\mathcal H^t$ spaces. Its actual finite root coefficients depend
continuously on real $\delta$ in every fixed angular smooth norm:
the underlying repaired state is $Q_0+\delta Z$, and every root
denominator has the common strictly positive gap already required
in R97. The same is true of the exact rational input diagonals,
uniformly for $z\in[0,97^{-2}]$.

For each fixed physical input frequency, the genuine normalized Ai
column depends continuously on the parameter through its original
linear reference ODE and its nonvanishing normalization. The common
bound $|\beta_n|\le C_\beta n^{-4/3}$ then makes the diagonal sequence
$\delta\mapsto(\beta_{n,\delta})_n$ continuous in the uniform norm:
first make the common high-frequency tail small, then use
continuity of the finitely many remaining frequencies. This proves
the needed operator-norm continuity of the exact $D_{g,\delta}$.

The old-circle inverse is continuous on each fixed qualified
window by its genuine resolvent identity
$$
 J_\delta-J_{\delta'}
  =J_\delta(\mathscr A_{\delta'}-\mathscr A_\delta)J_{\delta'} .
 \tag{RNI.23}
$$
Here $\mathscr A_{\delta'}-\mathscr A_\delta$ is measured from
$H^{q+1}$ to $H^q$, and the two $J$ factors use the uniform
one-gain bounds above. The complete ordered RBO/RD expressions then
give continuity of $\widehat S_\delta$ in
$\mathcal B(\mathcal H^t)$: the multipliers, exact input diagonals,
primitive and inverse factors all have their original bounded types.
With the uniform inverse bound (RNI.16),
$$
 \widehat S_\delta^{-1}-\widehat S_{\delta'}^{-1}
   =\widehat S_\delta^{-1}
       (\widehat S_{\delta'}-\widehat S_\delta)
          \widehat S_{\delta'}^{-1}
 \tag{RNI.24}
$$
gives operator-norm continuity of the normalized inverse on each fixed
window.

For the true global Riccati factor $\mathcal M_\delta$, distinguish
two statements. Continuous dependence for each fixed-frequency
Riccati problem, with its actual continuously varying coefficients
and endpoint datum, together with (RNI.2), gives **strong** continuity
of $\mathcal M_\delta$ and $\mathcal M_\delta^{-1}$ by dominated
convergence of the Fourier series. Combined with (RNI.15), this
gives strong continuity of the true natural inverse on each fixed
window. If a reference is supplied only by its diagonal bound,
the fixed-frequency continuous-dependence premise must also be kept.

An operator-norm assertion for the true natural inverse additionally
needs, for example,
$$
 \sup_{|j|\ge97}
 \left|
 (1+\widetilde p_{j,\delta})^{1/2}
 -(1+\widetilde p_{j,\delta'})^{1/2}
 \right|\longrightarrow0
       \quad(\delta'\longrightarrow\delta).
 \tag{RNI.25}
$$
The inequality $0<\widetilde p<66$ alone does not prove (RNI.25).
This note does not add that unverified full-frequency uniform
continuity statement. No such continuity premise is needed for
the uniform boundedness (RNI.16).

Finally, parameter continuity of $C_{s,\delta}^{-1}$ on a fixed
selected chart additionally requires the corresponding continuity
of the actual chart identifications and $N_{i,\delta}^{\pm1}$ in
the declared windows. It is not a consequence of a single selected
coordinate receipt.

## RNI8. Present status

All conclusions that remove a kernel, cokernel or completion in this
note are conditional on the later actual uniform strict certificate
(RNI.3). The current recipe or a failed sufficient comparison is not
that certificate. A failed comparison would not prove a kernel.

The new proof supplies a finite exact route to uniform natural
negative-window bounds and separates the parameter-continuity
requirements. It requests no repeat of any old root, reference,
Poisson, signed-density, propagation, coordinate, finite or scientific
calculation. Complete incoming, the actual remaining finite rows,
the coupled low/head/mean problem and the nonlinear solution remain
independent obligations.
