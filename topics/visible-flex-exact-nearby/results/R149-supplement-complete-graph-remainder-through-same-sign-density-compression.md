# R149 supplement: the complete graph remainder through the same density compression

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**Proved new bounds for the original selected operator.** The actual inverse
lift already has enough complete complex-strip qualification to give
`||C^{-1}:H^{-4/3}_0 -> H^{-4/3}_0|| < 2^14`. No new inverse-lift
calculation is needed for this conservative bound. Collecting the **whole**
original graph remainder before taking norms then replaces the separate
large `W^{-1}` and transported-projection costs by this one inverse.
At the original cutoff `J_dagger=2^4608`, the resulting bounds are

\[
\begin{aligned}
 \|P_JK_0P_J\|&<2^{-437},\\
 \|P_JK_+P_J\|&\le2^{-1462}C_{\rm add},\\
 \|P_JU_{\rm phys}\Theta P_J\|
       &\le2^{-1479}D_{96}+2^{-1470}.
\end{aligned}
\tag{DG.1}
\]

Here `C_add` and `D_96` are exactly the complete common6 WPL receiver
and PN56 port9 from [CG](R149-supplement-positive-feedback-in-the-complete-graph-high-block.md).
Their actual successful certificates are still prerequisites for the last
two assertions as physical coupled operators. No finite inverse, full
incoming inverse or parameter border is inferred from these high bounds.

## DG1. A complete old analytic qualification supplies the third derivative

Use exactly [DC](R149-supplement-same-sign-density-compression-and-finite-Theta-rows.md)
and [DB](R149-supplement-complete-Theta-row-regularity-and-negative-window-density-inverse.md):

\[
 S=U_\psi,
 \quad p=\psi^{-1}=\mathcal H\circ(X_-^{\delta_*})^{-1},
 \quad C=WS=\tfrac12(S-ZSZ),\quad
 G=|D_\phi|^{-1}.
\tag{DG.2}
\]

All are the same true selected maps; the circle has period `pi/2` and
physical frequencies `4j`. The R31 whole one-leg Lipschitz budget
`L_delta<1/16` is an integral of the full **complex** angular derivative
on the original field strip `1/16`. This scope follows directly from the
original source's `complete_one_leg_integrated_first_derivative`, its
complete `Astrip` first-parameter integral on `1/16`, and the full
second-parameter term, all retained in
[the original R31 source](../scripts/fourfold_codazzi_phase_explicit_family_R31.py).
It is not merely a real-axis flow derivative bound.

For the real selected parameter, the scalar speed is real. If
`S_-=(X_-^{delta_*})^{-1}` denotes the full inverse minus leg, complex
Gronwall, first on a stopped substrip and then by continuation, gives

\[
 |\operatorname{Im}S_-(x+iy)|
       \le e^{L_\delta}|y|,
 \qquad |S_-'(z)|\le e^{L_\delta}<16/15.
\tag{DG.3}
\]

The same integral bounds the reverse leg: the time direction changes the
sign but not the integrated absolute derivative. For `|y|<1/256`, the
entire trajectory stays inside `1/240<1/128<1/16`. Thus the continuation
argument does not assume a complex trajectory exists outside its paid
field strip. This is the complete strip qualification already used in
DC.20, now also applied to its variational equation.

The actual [W.5](R133-supplement-actual-physical-Wiener-conjugacy-strip.md)
bound is the **whole** Wiener derivative bound
`||H'||_{A_{1/128}}<33/32`. Therefore, on the whole strip `sigma=1/256`,

\[
 |p'(z)|<(33/32)(16/15)=11/10,
 \qquad
 |p'''(x)|\le 2!\,(11/10)\sigma^{-2}
               =\frac{720896}{5}=:b_3.
\tag{DG.4}
\]

The second statement is Cauchy's formula applied to the analytic
**periodic derivative** `p'`, using smaller disks and taking their limit
if the strip is open. A real-axis upper bound for `p'` alone would not
justify it. The real-axis qualifications DC.21--22 supply

\[
 m=465/512<p',\qquad |p''|<6=:b_2.
\tag{DG.5}
\]

Use the complete, unconditional inverse bootstrap DB.18 with these
inputs. Write its opposite-sign constant as

\[
 B_{\rm off}=\frac1{16}
       \left(\frac{b_3}{m^3}+\frac{3b_2^2}{m^4}\right).
\]

The exact rational comparison `B_off<3*2^12` reduces to

\[
 131052\,2^{20}=137417981952
       <140259751875=3\,465^4.
\tag{DG.6}
\]

In DB notation,
`S_{1/3}^3=m^{-7/2}(m+3/2)<4<(8/5)^3`:
use `9/10<m<1` and `(10/9)^4<8/5`. Also
`4^{-5/6}<1/3` and `(17/16)^{2/3}<21/20`, each by cubing or
raising to the sixth power and comparing integers. Hence

\[
\begin{aligned}
 K_{C,-4/3}
 &\le(17/16)^{2/3}S_{1/3}
       [1+4^{-5/6}(9B_{\rm off}/4)]\\
 &<\frac{21}{20}\frac85
            \left[1+\frac13\frac94(3\,2^{12})\right]
   =\frac{387114}{25}<2^{14}.
\end{aligned}
\tag{DG.7}
\]

This is an analytic consequence of complete old bounds and DB's new
operator theorem, not a rerun of an old scientific target. The sharper
new compound-lift `b_3=h_3+6 E_p sigma^{-3}` may later improve it.
It is unnecessary for the bound proved here. The one-factor Bessel
conversion in DB.18 is included exactly once.

## DG2. Collect the original complete remainder before taking its norm

Keep all WDH/CG maps, the original target normalizer `B`, source map `A`,
natural/model source projection `P=P_97`, transported source projector
`P_tilde`, and ordinary target projection `P_J`. Precisely,

\[
 \widetilde P=A^{-1}CP C^{-1}A,
 \quad \overline M=M_\nu P+L_{\rm low}Q_{97},
 \quad\overline G=\overline M^{-1}.
\tag{DG.8}
\]

No one of these three projections is exchanged with another. Direct
adjacent inverse cancellation gives the three exact ordered identities

\[
\begin{aligned}
 A\widetilde P&=CP C^{-1}A,\\
 W^{-1}A\widetilde P&=SP C^{-1}A,\\
 (W^{-1}-Id)A\widetilde P&=(S-C)P C^{-1}A.
\end{aligned}
\tag{DG.9}
\]

The qualified range of the second identity is the original `X_fr`;
this follows from the original transported-projector identity. It does
not follow merely from the letters `SP` or an ordinary high cutoff.

Use WDH.14 in full and replace its final physical error by the exact
same-column sum `E_partial + Delta_partial` from CG.3. Then

\[
\boxed{\quad
 E_{\rm coupled}\widetilde P\overline G
 = B^{-1}\left[
       Q_aR_{\rm ss}A^{-1}C
       +Q_aT_i(S-C)
       +(E_\partial^{\rm fr}+\Delta_\partial)S
       \right]P C^{-1}A\overline G .
 \quad}
\tag{DG.10}
\]

The last bracket entry is used only after the displayed right factors
place its input in `X_fr`. It does not extend the physical error to an
unqualified full-circle domain. In particular, DG.10 is an identity of
the whole ordered product, not a claim that each bracket term has an
independently specified arbitrary-source realization.

The original strong difference
`S-C=(Id-W)S=(Z Delta_full/2)S` on nonmean input gives

\[
 \|S-C:H^{-4/3}_0\to L^2_0\|
 \le (C_\Delta/2)\|S\|_{-4/3}.
\tag{DG.11}
\]

Here `C_Delta` is the **whole** DZA norm, including its independent
input-mean rank and both sign blocks, exactly as WIT/WDH read it.
No component is subtracted from that upper bound. The physical density
mean rank `(h_H-1) tensor rho_i`, both stored physical means, full root
head, source/interface/endpoint terms and all original `N_i` conversion
inside `E_partial` remain. The auxiliary nonmean restriction is not a
deletion of an independent physical equation.

For any Fourier Hilbert window `s`, orthogonality of the two signs gives

\[
 \|C:H^s_0\to H^s_0\|
 =\|\Pi_+S\Pi_++\Pi_-S\Pi_-\|
 \le\|S:H^s_0\to H^s_0\|.
\tag{DG.12}
\]

There is no extra `sqrt(2)` or sum of block bounds. This is only a
forward compression bound; the inverse uses the genuine DB theorem.

## DG3. Complete high bounds in the unchanged negative window

The complete old dyadic envelopes are those of WDH.11--17 and CG.13:

\[
 \begin{gathered}
 \|B^{-1}\|_0<2^8,\quad
 \|A^{\pm1}\|_{-4/3}<2^{14},\quad
 \|S\|_{-4/3}<2^{29},\quad \|T_i\|_0<2^5,\\
 \|Q_aR_{\rm ss}\|_{-4/3\to0}<2^{18},\quad
 C_\Delta<2^{120},\quad C_\partial<2^{1024},\\
 \|\overline G P_J:L^2\to H^{-4/3}\|
       \le 2^9\Lambda_J^{-1/3},\qquad J\ge97.
 \end{gathered}
\tag{DG.13}
\]

The sole high gain is taken immediately after the original model inverse,
before any variable coordinate. No gain is invented after `C^{-1}`.
The three bracket terms in DG.10 are bounded, on their stated whole
product, by `2^61`, `2^153`, and `2^29(C_partial+C_add)`.
Consequently the same reference-extension high block obeys

\[
\boxed{\quad
 \|P_JK_{\rm coupled}P_J\|
 \le K_{C,-4/3}
       [2^{92}+2^{184}+2^{60}(C_\partial+C_{\rm add})]
                        \Lambda_J^{-1/3}.
 \quad}
\tag{DG.14}
\]

The exact reference term `K_ref` remains in `K_coupled`. Its output is
contained in `Q_97 Y_a^0`, hence `P_J K_ref=0` in this high compression.
All its transported input rows and low/cross equations remain. We have
not subtracted a bound for it from the whole error.

Set `C_add=0` for the original homogeneous operator only. Since
`2^92+2^184+2^1084<2^1085`, DG.7 gives

\[
 \|P_JK_0P_J\|<2^{1099}\Lambda_J^{-1/3},\qquad
 \|P_JK_+P_J\|\le2^{74}C_{\rm add}\Lambda_J^{-1/3}.
\tag{DG.15}
\]

Thus DG.1's first two estimates follow at the original fixed cutoff.
The homogeneous high inverse already also exists at `J=2^3300`, where
the deviation is strictly below `1/2`. This optional smaller cutoff still
has ordinary low dimension `2^3300-1`; it does not turn the problem into
a solved96-dimensional finite system. The coupled formulas below keep
the original cutoff, so no downstream finite basis is silently changed.

## DG4. The same physical96 columns and complete Theta high row

The unchanged WGB coordinates become, by the same exact identity,

\[
 C_Q=A^{-1}CD_+E_{96},\qquad
 V_Q=E_{96}^*D_+^{-1}C^{-1}A,\qquad
 \Theta=V_Q\overline G.
\tag{DG.16}
\]

`D_+` is the original unitary phase multiplier, and `E_96` is the
original normalized real reflected isometry. The complete WX forward
`L^2` ball read in CG.21 gives `||S||_0<2^3`; with
`||A^{-1}||_0<2^9` and `||Mbar||_0<2^5`, DG.12 gives

\[
 \|C_Q\|<2^{12},\quad
 \|\overline M C_Q\|<2^{17},\quad
 \|U_{\rm phys}\|\le 2^8D_{96}+2^{17}.
\tag{DG.17}
\]

The last bound uses the **sum** for the genuine difference
`U_phys=B^{-1}H_96^partial-Mbar C_Q`. Reference columns are not
renamed physical columns, and the latter receive no right source factor.

For the complete row `Theta`, use DG.16 in its actual order. At the
original position of the Fourier extraction,
`||E_96^*:H^{-4/3}->ell2||=Lambda_96^{4/3}<2^12`. Therefore

\[
 \|\Theta P_J\|
  \le 2^{12+14+9}K_{C,-4/3}\Lambda_J^{-1/3}
  <2^{49}\Lambda_J^{-1/3}.
\tag{DG.18}
\]

This pays the original one-derivative-loss model inverse and the genuine
negative-window coordinate inverse. A new `V_Q:L^2->ell2` bound is
not used in its place. No transported row is treated as ordinary low
output. Combining DG.17--18 gives DG.1's third bound.

The complete physical96 augmented primitive square therefore has

\[
 \|P_J(K_{\rm coupled}+U_{\rm phys}\Theta)P_J\|
 <2^{-437}+2^{-1462}C_{\rm add}
             +2^{-1479}D_{96}+2^{-1470}.
\tag{DG.19}
\]

A sufficient complete whole-ball test is

\[
 C_{\rm add}\le2^{1459},\qquad D_{96}\le2^{1476}.
\tag{DG.20}
\]

Only after the actual common6 and PN56 records pass their original
qualification and these tests does DG.19 prove the coupled augmented
high inverse has norm less than2. Without physical augmentation, keeping
the original auxiliary `z=Theta u` instead needs only the reference high
test, for which `C_add<=2^1460` suffices. These are explicit future tests,
not assertions that the current incomplete prerequisites have succeeded.

## DG5. Retained equations and actual-consumer boundary

All WGB/CG low, cross, source, full mean, height, actual metric-parameter
and phase equations remain, with the same signs and normalizers. In the
augmented primitive formulation the ordinary low complement still has
dimension `J_dagger-1`. In the homogeneous realization the complete
constraint `Theta u=0` still remains. Projection of any independent
finite physical border is `P_J directsum 0`, never a projection deleting
that border. This result remains a graph-preconditioned primitive target
bound with gain `Lambda_J^{-1/3}`; it is not the different principal
RNS `Lambda_J^{-4/3}` realization or a new choice of target normalizer.

The [pure scalar adapter](../scripts/fourfold_codazzi_compressed_graph_high_math.py)
reuses CG's complete receiver admission and emits only the four **new**
whole envelope records. It additionally requires the owner to admit the
same complete DC/DB/W/R31 analytic qualification. All old input balls are
consumed from their original whole objects; this note does not duplicate
their large JSON carriers. Each new dependent expression must use the
complete saved-and-read-back previous record. There is no manifest or
scientific execution before actual common6 and PN56 exist. No old
sign norm, flow, KAM, compound, pairing, radial integral, inverse or scalar
target is recomputed by this analytic result.
