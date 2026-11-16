# R133 supplement: exact finite root factor and a reduced graph high test

2026-11-16, visible-exact / root.

**Proved exact finite-factor identity and conditional high-block criterion.**
The complete root finite-head term in WUE factors through the actual finite
root trace. It can therefore remain as an auxiliary finite variable in the
WGB system. The infinite high block then uses the other complete error terms,
without a smallness charge for this finite factor. The root response columns,
their full high/low cross maps and the auxiliary equations are still required.
No numerical high test or finite inverse is asserted.

This is an exact rearrangement of the same physical column and the same WBP
left and right coordinates. No upper bound is subtracted from another.
The missing 96 physical input columns and any unknown radial functions
remain separate obligations.

## WFR1. The actual root term and a finite trace space

Fix the original selected real member, its physical reflection, the genuine
terminal-Ai column and all units of WUE. In particular
$P=Id-\Pi$, the old physical frequencies are $4j$, and the input before the
genuine trial is the original natural reflected space $\mathcal H_{\rm nat}$.
Let
$$
 \mathcal H_* f=h^G_f(r_*),\qquad
 P_F=\mathbf 1_{\{|j|\le96\}}
 \tag{WFR.1}
$$
with $P_F$ acting on both original physical curvature rows. This is the
finite Fourier trace at the true root; it is not a projection on a radial
source function or on a waist coordinate.

Let $\mathscr X_*$ denote PW's original complete root trace space and let
$\mathcal R_*:\mathscr X_*\to\mathcal Y_0$ be its same full root-to-waist
receiver. Its output is the complete old primitive-density pair and both
mean slots. WUE's signed root finite term is exactly
$$
             R_F=-\mathcal R_*P_F\mathcal H_* .
 \tag{WFR.2}
$$
The independent positive correction is still $R_+$; neither its stable
condition nor any separate head, source, outer or mean port is changed.

Use first the full real finite space
$$
 \mathbb F_*=
 P_F\bigl(L^2_{\rm real}(\mathbb T;\mathbb R^2)\bigr),
 \qquad \dim_{\mathbb R}\mathbb F_*=386 .
 \tag{WFR.3}
$$
Here a single real row has its constant and the sine and cosine modes
$1,\ldots,96$. The inner product is the original normalized circle
inner product on the two rows. Let $E_*:\mathbb R^{386}\to\mathbb F_*$
be an isometric Fourier injection. Its range consists of smooth traces,
so it also defines a bounded map into $\mathscr X_*$. Set
$$
                  V_* =E_*^*P_F\mathcal H_* .
 \tag{WFR.4}
$$
Then, as actual operators on finite smooth input sums,
$$
                  R_F=-\mathcal R_*E_*V_* .
 \tag{WFR.5}
$$

There are two exact optional reductions. PC.6 gives
$\Pi h_1^G=\Pi h_2^G=0$, so this particular trace lies in a space of
dimension at most 384. Under the actual N.3/WUE natural physical reflection,
$h_1^G$ is root-odd and $h_2^G$ root-even. Each nonmean row then has
96 real coordinates, so dimension at most 192 suffices. One may use that
isometric restricted injection in (WFR.4)--(WFR.5). No assertion that
the rank is exactly 192, or that it is only 96, is needed. The full
386-coordinate factor is valid even when these reductions are not used.

The vanishing of the two means in this particular trial trace does not
set the independent physical mean ports to zero. The receiver
$\mathcal R_*$ evolves the full coupled system and can produce nonzero
mean outputs from an initially nonmean trace. Both output mean slots
remain inside every column $\mathcal R_*E_*$.

PC.29--31 already prove a complete bound
$$
       P_F\mathcal H_*:
       \mathcal H_{\rm nat}^{-4/3}\longrightarrow\mathbb F_* .
 \tag{WFR.6}
$$
Indeed PC.31 bounds the root as part of the entire positive-collar
supremum, using the actual shifted old-angle contour and the full
exponential-lag $J,L,B$ matrices. Thus $V_*$ is a bounded vector of
actual rows, not a list of norm upper bounds. Its distributional
extension is unique from dense finite natural Fourier sums. Equation
(WFR.5) extends as the same bounded complete root error.

## WFR2. Keep the physical row and the ordered coordinate factors

Write WUE's physical row in its original units:
$$
 \frac{\mathfrak W_\partial}{2\kappa_{\rm waist}}
   =Q_aT_i+E_\partial^{\rm fr},
$$
$$
 E_\partial^{\rm fr}
  =D_{\rm alg}
    +L_\partial(R_++R_F+T_{\rm neg}+E_{\rm end})N_i .
 \tag{WFR.7}
$$
All maps have their WUE order. In particular $N_i$ is the same true
common-input inverse, not an ordinary high Fourier projection.
Define the exact operator
$$
 E_\partial^\circ
    =D_{\rm alg}
       +L_\partial(R_++T_{\rm neg}+E_{\rm end})N_i .
 \tag{WFR.8}
$$
Equations (WFR.5), (WFR.7) and (WFR.8) give
$$
 E_\partial^{\rm fr}
       =E_\partial^\circ-L_\partial\mathcal R_*E_*V_*N_i .
 \tag{WFR.9}
$$
This definition keeps all of $D_{\rm alg}$, including its genuine
density mean rank and full finite and two-primitive terms. The
positive correction, complete negative volume and true jumps,
and complete WES endpoint are still present in (WFR.8).

Now use precisely WBP's two distinct normalizers
$\mathcal A$ on the source and $\mathcal B$ on the target, and its
full density intertwiner $\mathcal W$. On the actual source,
$$
 \widetilde{\mathcal B}_{\rm ss}
 =\mathcal B^{-1}
   \frac{\mathfrak W_\partial}{2\kappa_{\rm waist}}
             \mathcal W^{-1}\mathcal A
 =M_\nu+E^\circ+U_*V_{\rm src},
 \tag{WFR.10}
$$
where
$$
 \begin{split}
 E^\circ=\mathcal B^{-1}\bigl[
     Q_a\mathcal R_{\rm ss}
    +Q_aT_i(\mathcal W^{-1}-Id)\mathcal A
    +E_\partial^\circ\mathcal W^{-1}\mathcal A\bigr],\\
 U_*=-\mathcal B^{-1}L_\partial\mathcal R_*E_*,
 \qquad
 V_{\rm src}=V_*N_i\mathcal W^{-1}\mathcal A .
 \end{split}
 \tag{WFR.11}
$$
The codomain of $U_*$ is the true reflected nonmean primitive target
$Y_a^0$: WUE.28 applies the full pair reflection projection before the
mean-preserving density change, even for the unreduced 386-column injection.
The finite rows act only on the true source
$\widetilde X_{-4/3}$; their extension in the graph formula below
uses the actual transported projection. No factor is commuted
through $N_i$, $\mathcal W^{-1}$ or $\mathcal A$.

The qualified WUE, PC and WBP maps imply
$$
 U_*:\mathbb R^{d_*}\to Y_a^0,\qquad
 V_{\rm src}:\widetilde X_{-4/3}\to\mathbb R^{d_*}
 \quad\hbox{bounded},
 \qquad d_*\in\{386,384,192\}
 \tag{WFR.12}
$$
when the corresponding exact trace convention above is used.
The columns $U_*$ are true root impulses propagated through
$\mathcal R_*$ and the actual left observation. They are not
the unknown 96 physical positive Poisson columns, nor a low
comparison isomorphism.

## WFR3. A complete positive budget for the infinite remainder

Use the original $H^{-4/3}$ window. Let the complete WUE constants
bound their displayed operators, and write
$$
 K_\partial\ge\|L_\partial\|_{\mathcal Y_0\to Y_a^0},
 \qquad K_{N,-}\ge\|N_i\|_{X_{-4/3}^{\rm fr}\to
                                  \mathcal H_{\rm nat}^{-4/3}} .
$$
For example the original qualified $K_{H^{-1},0}/\sqrt2$
and the saved full NIF $A_-$ are allowed; their order and units
are unchanged. A direct positive bound for (WFR.8) is
$$
 C_\partial^\circ
  :=C_{\rm alg}
     +K_\partial K_{N,-}
          (C_+^w+C_{{\rm neg},4/3}+C_{\rm end}) .
 \tag{WFR.13}
$$
The full received $C_+^w$ is read as a whole; another root receiver
factor is not added to it. WUB supplies the complete negative
$H^{-4/3}$ operator, and WES supplies the complete same-old-target
endpoint comparison. Their new quantitative budgets still need
to be evaluated before (WFR.13) becomes a numerical input.

For either of WBP's two whole choices
$r\in\{\mathrm{unc},\mathrm{col}\}$, its exact (WBP.23) gives
$$
 C^\circ_r
 :=K_{B,0}\left[
       C_r
       +K_{i,0}^{\rm fwd}C_{W-Id}K_{A,-}
       +C_\partial^\circ K_WK_{A,-}
                    \right]
       \ \ge\|E^\circ\|_{H^{-4/3}\to Y_a^0}.
 \tag{WFR.14}
$$
This is a bound for the newly displayed exact remainder
$E^\circ$, not the old whole remainder with a numerical upper
subtracted. It preserves the full sign commutator, both ordered
primitive factors, the density mean rank and all coordinate
changes. Only entire bounds for this same $E^\circ$ may be
compared.

The root finite term has no charge in (WFR.13)--(WFR.14) because
it is retained as the exact factor $U_*V_{\rm src}$ in
(WFR.10). Its columns and rows remain numerical obligations
of the later finite system. None of the old successful scalar
records is changed or recomputed.

## WFR4. Exact graph equation and the reduced high test

Keep WGT's graph, inverse and actual source projection:
$$
 \mathcal D=\{x\in X_b^{-1}:\overline Mx\in Y_a^0\},\qquad
 \overline G=\overline M^{-1},\qquad
 \mathcal D_{\rm true}=\widetilde P\mathcal D .
 \tag{WFR.15}
$$
Here $\overline M=M_\nu P_{97}+L_{\rm low}Q_{97}$ uses the same
reference low isomorphism. It does not supply physical low columns.
The exact reference extension of (WFR.10) is
$$
 \begin{split}
 \widetilde{\mathcal B}_{\rm ss}\widetilde P
        +\overline M(Id-\widetilde P)
 \end{split}
$$
and, after the same right graph inverse,
$$
             Id+K^\circ+U_*V,\qquad
 V=V_{\rm src}\widetilde P\overline G,
$$
$$
 K^\circ=E^\circ\widetilde P\overline G+K_{\rm ref},
 \qquad
 K_{\rm ref}=(M_\nu-\overline M)\widetilde P\overline G .
 \tag{WFR.16}
$$
All rows in $V$ are bounded on $Y_a^0$: the graph inverse maps
$L^2$ to $H^{-1}$, followed by its bounded embedding into
$H^{-4/3}$ and the actual bounded transported projection.
The auxiliary root coordinate is the value of this exact row.

For an ordinary target cutoff $J\ge97$, set $P_J$ high and
$Q_J=Id-P_J$. WGT's exact low-output identity still gives
$P_JK_{\rm ref}=0$. Consequently
$$
 H_J^\circ=Id_{P_J}+P_JK^\circ P_J
      =Id_{P_J}
        +P_J E^\circ\widetilde P\overline G P_J .
 \tag{WFR.17}
$$
A complete sufficient test is
$$
 \boxed{\quad
 \chi^\circ_{J,r}
   :=2K_{\rm CYA}C^\circ_rK_{P,-}\Lambda_J^{-1/3}<1,
 \qquad
 \|(H_J^\circ)^{-1}\|_{2\to2}
                  \le(1-\chi^\circ_{J,r})^{-1}.
 \quad}
 \tag{WFR.18}
$$
This is the inverse of the infinite block before the finite
factor is eliminated. It is not the inverse of
$H_J^\circ+P_JU_*VP_J$. No smallness of that latter finite
high/high factor is required in the auxiliary formulation.

In particular one has not proved $P_JU_*=0$.
The root response can have arbitrarily high Fourier output,
and every such column remains in the high equation. Likewise,
$V$ is not an ordinary low-frequency input projection.
Compactness and the index of the WFI high domain are unchanged
by this finite-rank rearrangement.

## WFR5. The missing physical columns remain missing

When only the homogeneous high physical column has been
provided, WGB imposes the same 96 exact equations
$$
                  \Theta u=0,\qquad
                  \Theta=V_Q\overline G .
 \tag{WFR.19}
$$
The actual reference-coordinate system is now
$$
 (Id+K^\circ)u+U_*z=f,\qquad z=Vu,\qquad\Theta u=0 .
 \tag{WFR.20}
$$
Here $z$ is an auxiliary value determined by $u$; it is not a
new freely prescribed root port or a replacement for the 96
missing physical inputs. Eliminating $z$ recovers exactly
the same physical high-column system.

For clarity suppose the strict test (WFR.18) has passed, and
write $P=P_J$, $Q=Q_J$, $H=H_J^\circ$. Direct substitution of
$$
 p=H^{-1}(Pf-PK^\circ Qq-PU_*z)
 \tag{WFR.21}
$$
leaves the three full rows
$$
 \begin{split}
 &(Id_Q+QK^\circ Q-QK^\circ PH^{-1}PK^\circ Q)q\\
 &\hspace{10mm}
   +(QU_*-QK^\circ PH^{-1}PU_*)z
       =Qf-QK^\circ PH^{-1}Pf,\\
 &(-VQ+VPH^{-1}PK^\circ Q)q
       +(Id+VPH^{-1}PU_*)z=VPH^{-1}Pf,\\
 &(\Theta Q-\Theta PH^{-1}PK^\circ Q)q
       -\Theta PH^{-1}PU_*z=-\Theta PH^{-1}Pf .
 \end{split}
 \tag{WFR.22}
$$
The second row comes from $z-Vu=0$; the third from
$\Theta u=0$. Their right sides therefore have opposite
signs. All high response and cross maps are retained.
No new finite matrix entry has been evaluated.

If the true 96 physical columns $H_{\rm phys}$ are later
supplied, WGB instead includes their actual difference factor
$$
 (H_{\rm phys}-\overline M C_Q)V_Q\overline G .
 \tag{WFR.23}
$$
Append those columns to $U_*$ and those rows to $V$, retaining
their declared physical coordinate meaning. Do not also add
another independent copy of the same finite input. Equations
(WGB.29)--(WGB.32) then apply with $K=K^\circ$ and the combined
finite factor. In particular their full $(q,z,\varkappa)$
matrix, right side, physical metric column and scalar Schur
row are unchanged except for these explicit new finite
columns and rows. Redundant root-factor coordinates are
allowed by the exact block elimination.

Independent physical means, amplitude constraints, positive
head equations, exterior conditions, the actual metric
variation and all corresponding high feedback remain.
An unknown function in $L^2_r(\mathbb C^{193})$ is still
infinite-dimensional. This proof isolates a trace at one
fixed root; it makes no finite-dimensional claim for a
radially varying source or head.

## WFR6. Exact conclusions and remaining quantitative work

The proved statements are:

1. The full root finite term of WUE has the exact factorization
   (WFR.5), with a safe 386-dimensional real trace space and the
   specified exact optional reductions.
2. The same WBP physical row has the exact split (WFR.10)--(WFR.11).
   Its infinite remainder has the direct complete positive
   budgets (WFR.13)--(WFR.14).
3. The high inverse may use (WFR.18) while the entire finite
   root factor stays in the auxiliary equations. Its high
   output and all cross terms remain in (WFR.21)--(WFR.22).
4. The original missing physical columns, all independent ports
   and the actual finite/metric inverse requirements are unchanged.

The practical mathematical gain is that the complete old
root finite-head norm need not enter the sufficient
high-block contraction bound. It has been moved into a
finite-factor realization of the same exact equation.
The old positive correction and the complete negative,
endpoint, algebraic and coordinate errors still require
usable whole bounds. This result supplies no passing cutoff,
finite determinant, nonzero metric pairing, nonlinear
solution, parameter-family theorem or final geometric conclusion.

The actual finite rows can be obtained from the true
$P_F\mathcal H_*N_i\mathcal W^{-1}\mathcal A$ coefficients
or from the corresponding complete adjoint pairings.
The actual columns require the full root receiver with the
stated left coordinate. A saved norm upper alone supplies
neither set of matrix entries. These are future new targets;
the old scalar programs are not rerun.

## WFR7. Immutable primary sources

| Source and use | Git blob | Bytes | SHA-256 |
|---|---|---:|---|
| WUE: exact same-leading physical row and root sign | 9b5b13f0178c9a292ae8ba11264051c1fe438c14 | 32557 | e191f96acc39ab802adb93ace2d1e57691b017629ed762ddd39624d3bcb61ce1 |
| PC: complete two-row genuine trace and finite-root contour bound | 35f3ddaec691c2d7c636ec43da3f52605ed6b329 | 37079 | 5368abae4c66f73800c16d5f2b906ddaa0f1d62d07e9bd9a3ca539061bdf5d68 |
| N: physical parity and independent mean equations | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| WBP: the actual two-sided normalizers and full error order | 54f859b305861a1c4be4be7826c059e1e4ffc3e8 | 18114 | 19f0182fb19cb3842948ee427993f7478af0557f2ec790c7c2f8ce5849015a7e |
| WGT: transported projection and exact graph high block | 2827aec2afb53d395218c7d6dbf488083eb66df4 | 20433 | 231ff8b11d405591cdd23c56831a33796a61976cb813165787b6212dd2511d08 |
| WGB: exact finite factor, constraints and metric border | 30cd8f7858888c35f942094611614c9f74b3e2af | 25135 | e7d23c583205fcb538fd21260e2e9c5b4859ed73ab6129a453b8c5d1fb05bf7c |

Only finite-dimensional linear algebra identities and previously
proved bounded operator maps are used here. No old or new
numerical arithmetic, source integration, ray solve, propagator,
root inverse or scientific execution was performed.
