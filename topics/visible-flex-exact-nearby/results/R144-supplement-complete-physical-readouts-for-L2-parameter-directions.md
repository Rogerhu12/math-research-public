# R144 HLP: complete physical parameter readouts for genuine L2 directions

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved.** At a fixed original physical graph coordinate $w$ and
fixed global height input, the true partial parameter-height and
full vector readouts have the bounds
$$
 \|D_\gamma z(\gamma,w)[\eta]\|_{\mathcal Z^2}
           <2^{-56000000}\|\eta/r_\gamma\|_{L^2},\qquad
 \|D_\gamma{\cal V}(\gamma,w)[\eta]\|_{\mathcal V^2}
           <2^{-55000000}\|\eta/r_\gamma\|_{L^2}.
 \tag{HLP.1}
$$
They are the same complete readouts of GHW/GHV. They retain all
one-sided physical two-jets, original means, complete metric
response, finite connector, flat-end outputs and the same single
frame/height conventions. On a general graph they are formal
one-sided readouts, not automatically compatible global $C^2$ jets.

Both operators are jointly continuous in the displayed
$L^2$-direction operator norms when gamma varies in its relative
$A^0$ topology and the common graph background varies in $E_{21}^+$,
within the original value domain. No nonlinear $L^2$ value domain
and no new radial trace are introduced.

This is a transfer from actual Hilbert-direction columns proved
in HL, not an inference from the old $A^0$ norm of those columns.
All constants are the already proved physical constants of
GHR/GHC/GHW/GHV; there is no new numerical combination or rerun.

## 1. Same domain, exact columns and completed Hilbert inputs

Use:

- [HL: complete L2 parameter forcing and actual seed response](R144-supplement-complete-L2-parameter-forcing-and-actual-second-seed-response.md), especially HL.26, HL.34, HL.36 and HL.41;
- [GHR](R144-supplement-actual-seed-metric-reference-height-and-complete-endpoint-column.md);
- [GHC](R144-supplement-complete-actual-parameter-height-at-fixed-physical-coordinate.md);
- [GHW](R144-supplement-complete-physical-height-derivative-in-the-original-low-graph.md);
- [GHV](R144-supplement-actual-horizontal-coframe-and-low-graph-vector-two-jets.md).

The domain is unchanged:
$$
 \|\gamma/r_\gamma\|_{A^0}\le1/128,\qquad
 \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576},\qquad
 \|w\|_{E_{1856}^+}\le2^{-49000000}.
 \tag{HLP.2}
$$
The physical material coordinates, original scales, common
reference, fixed stop, actual B section and its height unit
are fixed. Directions retain the original even nonmean
$4\mathbb Z$ sector.

Put $e=\eta/r_\gamma$. HL proves, by actual kernel and seed
differentiation rather than a small-value inference,
$$
 \begin{split}
 \|D_\gamma{\cal U}_\gamma(w)[\eta]\|_{E_s^+}
   &\le2^{131072}\epsilon_L(1+W_{s+1})\|e\|_2,
                                      \quad20\le s\le2898,\\
 \|D_\gamma\mathfrak q(\gamma)[\eta]\|_{\mathcal P_2}
   &<2^{-110000000}\|e\|_2 .
 \end{split}
 \tag{HLP.3}
$$
The first is the actual endpoint lift, including every mixed
far-height term. The second is the actual 94-step seed's
second parameter, including the full joint phase response.
The complete radial first compensation and first-principal
inverse are the ones consumed by GHR/GF.

The low case of the first estimate is exactly
$2^{131073}\epsilon_L\|e\|_2$, the numerical input used in
GHC with its previous direction norm. The second estimate
is exactly GHR's original weighted parameter budget.
Consequently neither physical reconstruction requires a
new weaker constant.

## 2. Actual endpoint height, mean derivative and reference height

The complete identity at fixed $w$ and fixed global height is
$$
 D_\gamma z[\eta]
       =v_\eta+H_{\partial,\eta}+H_{\rm met,\eta},
       \qquad v_\eta=D_\gamma{\cal U}_\gamma(w)[\eta].
 \tag{HLP.4}
$$
Here $H_{\partial,\eta}$ is the true fixed-metric mean response
to the actual endpoint lift. Its derivative is the one in
GHC, including the actual background state derivative and
all three terms of the radial derivative of the small-root
mean map. The support is GHC's original positive collar.
The cap--long unscreened mean-height span remains a separate
matching output.

The last term is the complete metric reference-height with
the exact formula
$$
 (H_{\rm met,\eta})_t
   =aW\{\psi_\eta(1+\kappa)+\dot\kappa_\eta\},\qquad
 H_{\rm met,\eta}(t_f)=0 .
 \tag{HLP.5}
$$
The reference $1$, the full $\mathcal P_2$ response, the
actual first-principal inverse, two endpoint heights and
original conormal units remain. In particular this height
need not vanish at zero nonmean state.

For the endpoint term, the proof of GHC.7--GHC.15 is a
bounded linear reconstruction from its actual $E_{20}^+$
direction. It does not require that this direction was
generated from an $A^0$ parameter. Apply it to the first
line of (HLP.3). Its actual radial state jets, complete
mean response, and fixed Cartesian conversion give the
same endpoint fee as GHC.17.

For the metric term, GHR's scalar inequality is stated in
the true $\mathcal P_2$ norm. Apply it to the second line
of (HLP.3); no identification of a Hilbert gamma direction
with a radial parameter is made. It is the actual
derivative map that sends one to the other.

The same installed factors used in GHW section 7 are still
$$
 s_B\max(1,a_B^{-2})<1,\qquad
 \rho\varepsilon_s\max(1,\rho^{-2})<2^{440}.
$$
Thus the entire prior GHW.22 combination applies unchanged,
with $\|e\|_2$ in place of its previous direction norm.
This proves the first inequality in (HLP.1).

This transfer preserves the true derivative equations.
It is not obtained by replacing $\|\eta\|_{A^0}$ by
$\|\eta\|_2$ in an old inequality: (HLP.3) was independently
proved in exactly the norms required by the downstream
operators.

## 3. Full Cartesian metric and single-frame vector reconstruction

Let $W(a)$ denote the actual radial metric slope. GHV's
exact identity, including the true radial derivative
of its mean coefficient, is
$$
 (H_{\rm met,\eta})_a=\dot W_\eta(1+\mathcal L),\qquad
 |\mathcal L|,\ |\mathcal L_t|<1/4 .
$$
It proves the actual physical metric-direction estimate
$$
 \Xi(\dot W_\eta)
  :=\|\dot W_\eta\|_\infty+\|(\dot W_\eta)_a\|_\infty
                       +\|\dot W_\eta/a\|_\infty
  <4\|H_{\rm met,\eta}\|_{\mathcal Z^2}.
 \tag{HLP.6}
$$
The physical Hessian entry $H_a/a$ is explicitly included.
All scalar coefficients depend on the actual background,
not on the norm originally used to generate the direction.

The Cartesian horizontal metric is the same
$$
                 G=I+W^2e_r e_r^{\mathsf T}-Dz\,Dz^{\mathsf T}.
$$
GHV proves the entire physical readout estimate
$$
 \|\dot{\cal V}\|_{\mathcal V^2}
       \le2^{64}\{\Xi(\dot W)+\|\dot z\|_{\mathcal Z^2}\}.
 \tag{HLP.7}
$$
Its proof retains the true symmetric coframe, full connection,
radial rotation mean, fixed physical paths and the original
flat-disk outputs. It uses only the actual physical first
metric jet and second height jet, not a third height derivative.

The metric fee supplied by (HLP.3), GHR and (HLP.6) is exactly
the one in GHV.12 with $\|e\|_2$. The first part of (HLP.1)
supplies its other input. The already completed GHV.25
combination therefore proves the second part of (HLP.1),
without a new arithmetic gate.

The output remains GHV's formal complete readout off shell.
It becomes an actual global $C^2$ jet only on the original
compatible exact solutions or on limits of their matched
differences. Nothing in this transfer supplies missing
one-sided matching to a generic Hilbert parameter response.

## 4. Genuine joint operator continuity

HL.36 and the original endpoint lift give
$$
 (\gamma,w)\longmapsto v_\bullet
       \quad\hbox{continuous in }\mathcal L(L^2,E_{20}^+)
$$
for gamma in relative $A^0$ and $w$ in $E_{21}^+$.
GHC's fixed-collar mean reconstruction is a continuous
operator of this graph direction and its actual first
radial jet. Thus the first two terms of (HLP.4) have the
claimed joint $L^2\to\mathcal Z^2$ continuity.

HL.26 gives the genuine continuous
$L^2\to\mathcal P_2$ seed operator. The weighted principal
map and GHR's physical mean-height operator have their
proved continuity in that parameter norm and the actual
$E_{20}^+$ background. Their finite-prefix continuity and
uniform physical profile tails are exactly the original
ones. Their composition proves the same continuity for
the final term of (HLP.4).

Formula (HLP.6) uses continuous actual mean coefficients
and their true radial derivatives. GHV's square-root,
connection and bounded material integration then give
the joint $L^2\to\mathcal V^2$ continuity. All physical
scales and every original one-sided representative
remain fixed throughout this argument.

Therefore
$$
 \begin{split}
 D_\gamma z&\in
    C(\mathcal D_\gamma^{A^0}\times E_{21}^+;
                    \mathcal L(L^2,\mathcal Z^2)),\\
 D_\gamma{\cal V}&\in
    C(\mathcal D_\gamma^{A^0}\times E_{21}^+;
                    \mathcal L(L^2,\mathcal V^2)),
 \end{split}
 \tag{HLP.8}
$$
where both statements are restricted to the original
admitted value pairs. The notation does not assert
a nonlinear map on an open $L^2$ value set.

## 5. Complete columns and limits of the conclusion

These are partial gamma derivatives at fixed physical
$w$. They are not yet the total selected derivatives:
those also contain the true $D_w$ operator applied to
the separately constructed selected response. The
fixed-gamma graph operators keep their original
$E_{20}^+$ directions and original continuity topology.
No raw radial $L^2$ direction is granted an endpoint
trace by this result.

The global height input, genuine spatial frame and
position ports retain precisely their GHC/GHV columns.
A moving physical test, angle map, endpoint or density
has its additional differentiated-readout term.
The northern height convention retains its original
fixed sign. The compact support of metric bumps does
not make their integrated height or frame outputs zero
outside those supports.

All inequalities in this transfer consume prior
completed constants verbatim. No saved comparison was
repeated, and no scientific computation was run.
