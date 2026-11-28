# R149 ASQ. The phase formulation's amplitude output and its single world-height column

**Proved.** For the actual phase-counterterm formulation the low curvature
boundary budget, physical amplitude, and vertical translation can be classified
without a matrix rank experiment. At fixed remaining ports the two scalar
coordinates have an invertible triangular **direct** block in the strict
particular chart. The residual feedback of that chart is part of the resulting
regular operator. This statement does not prove invertibility of that operator.

## 1. Which rows have already been used

In [WOB.30–31](R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md)
the unknowns are a radial function with 193 components, 97 root initial data
(96 odd modes and one even mean), and 96 even nonmean endpoint coordinates.
The two outputs are a radial function with 193 components and 193 endpoint
coordinates. The outer equations resolve the 96 odd Robin coefficients,
the 96 even nonmean endpoint coordinates and the single physical even mean.
In particular the physical-frequency-four Robin row is the first odd
harmonic in this low system. Its arbitrary source enters there. The
positive inverse, when established, solves that equation for every
prescribed root-even vector, high input and inhomogeneity. Appending it
again to the negative propagation would duplicate its source. The mean
propagates through the entire radial solve, including all forcing and
jumps. [PN](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md)
then leaves precisely the 96 root-even inputs, in addition to its high input
and independent exterior and body sources. This is a conditional elimination
until the actual positive gate succeeds.

The [quarter-holonomy row replacement, (144.5)](R144-fourfold-holonomy-transfers-outer-mean-to-waist.md)
is a different implementation of the physical even mean. It requires the
specified cap and winding hypotheses and off-shell source transformation.
It supplies no additional scalar row after the WOB solve. The physical
fourth-mode Robin source and the raw phase average are independent.
They enter the positive right side and the final scalar phase row,
respectively.

[P.16 and §7](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md)
explicitly select the physical waist amplitude as an output. Thus the
dyadic amplitude of the reference fixes its center and scaling. There is
no prescribed-amplitude residual in this realization. If an amplitude
coordinate is wanted, adjoining the equation
$\dot\alpha+D\mathcal A(v(0))[\dot v(0)]=s_\alpha$
is an identity extension with coefficient one for the new coordinate.
It allows arbitrary $s_\alpha$ and uniquely recovers the output. The
fixed-amplitude chart [A.17–24](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
uses a different bordering. Its $b_4$ pivot cannot be appended to this
phase realization. The final displacement and reach still require their
own geometric bounds.

## 2. The actual two scalar columns

Use the phase variable $a$ with zero average and retain its full nonmean
equation. Use the physical vertical translation $t$ of the *whole*
cap, frame anchor and core position, in one common orientation.
The [two-input cap, §8](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)
has the precise mean height $v_0(s)=\lambda+\int_0^s aw\kappa$.
Thus the differential in $\lambda$ is one at every endpoint. Differences
of two heights kill this direction. Nonmean heights, metric, curvature,
ray return and its conjugacy equation also kill it. This separates an
absolute waist mean-height equation from the actual span. The frame
angle is unchanged. Any separately prescribed absolute world position
must transform as the same translation and cannot be used to fix $t$
a second time. The normalized far nonmean field $f_B$ has no constant
component; it cannot supply this column.

Write the state as $u=z+Z_\nu k+Tt$, where $k=\delta\nu$,
$Z_\nu$ is the original strict particular, $T$ is the single vertical
translation, and $z$ is represented at zero translation. Given an actual
state its translation coordinate is the cap's integration constant, so
this splitting and its inverse are unique on that placement chart.
Let $Pz$ and $Hz$ be the complete phase average and absolute mean
height on the remaining state. Include the chart term
$\langle(E'/J)a\rangle$ in $P$ and all independently varying anchor,
frame and geometric impulse terms in $H$. Let $D$ denote all other
rows and $r$ the whole strict parameter residual on them. If other
absolute position rows are present write their translation entries as
the vector $d=DT$. Then the actual equations read
$$
 Dz+rk+dt=f,\qquad
 Pz+c_P k=\sigma,\qquad Hz+c_H k+t=\eta .
$$
The two displayed coefficients are the *same* strict particular
evaluated by [PP](R147-supplement-actual-phase-pivot-with-full-regular-defect-retained.md)
and [HP](R147-supplement-actual-height-pivot-and-complete-phase-mean-transfer.md).
The translation entries are exactly $(0,1)$ by HP.12 and vertical
translation invariance of the metric ray return. Therefore
$$
 k=(\sigma-Pz)/c_P,\qquad
 t=\eta-Hz-c_H(\sigma-Pz)/c_P .
$$
Substitution into the remaining rows yields the exact operator and source
$$
 [D-dH-(r-dc_H)P/c_P]z
 =f-d\eta-(r-dc_H)\sigma/c_P .
$$
These identities preserve every component of the source. The scalar
determinant is $c_P$, already separated from zero in PP. They consume
the single $k$ and the single $t$ once each. With a preassigned world
placement, $t$ is prescribed data instead; these two scalar equations
then leave the HP.5 compatibility row. A relative height-span equation
also remains if independently imposed. Its translation column vanishes.

## 3. How to attach the 100 by 97 observations

The negative graph alone has domain of codimension 96. [WGB.24–27](R133-supplement-exact-graph-parameterization-and-physical-finite-border.md)
makes $\widehat x=x+C_Q c$, $u=\overline M\widehat x$ an exact isomorphism
on adjoining the above physical root data. In this coordinate
$c=\Theta u$ and $U=H_{\rm phys}-\overline M C_Q$. For a target cut
$J$, retain $q$ of dimension $J-1$, the 96 auxiliary coordinates $c$
with their 96 defining equations, the nonmean raw conjugacy function
$a$, and the two scalar coordinates $k,t$. At fixed external ports the
paired equations are the $J-1$ low waist components, 96 coordinate
identities, the complete nonmean phase function and the two scalar rows.
This gives $J+97$ finite coordinates and $J+97$ finite rows **in addition
to** the nonmean phase block. Before applying the two-row reduction,
the high substitution on every one of these equations uses
$$
 p=H_J^{-1}(Pf-PKQq-PUc-Pgk),
$$
and includes the corresponding high sources from all additional ports
when present. It retains the four genuine infinite-dimensional actions
on $PKQ,PU,Pg,Pf$. Raw phase division, normalizer derivatives and direct
metric contributions act before elimination. Counting finite coordinates
does not provide these operators or a bounded inverse for the nonmean
phase equation. The target cut is the original large graph cut, not 96.

[CFC §5](R149-supplement-complete-normalized-TC-columns-and-finite-physical-interface.md)
supplies signed restrictions and errors for these contractions. Its two
stored means on reflected curvature directions satisfy
$m_\pm=\pm n_g\sqrt{q_0/2}\langle h_2\rangle$ at a fixed base,
since its actual waves are $n_g(h_1\pm q_0 h_2)/\sqrt{2q_0}$ and
$h_1$ is odd. This relation concerns the two readings of those columns.
It does not identify the two coordinates of a general receiver source,
nor include a derivative of the normalization on a varying base. Both
coordinates remain in evaluation of the full waist row. Neither is an
additional equation for the 96 root coefficients. The other scalar CFC
readings contribute to $P,H,c_P,c_H$ with the direct and all remaining
terms above. No determinant of the rectangular table occurs.

The [executable block actions](../scripts/fourfold_codazzi_actualsquare_phase_height.py) expose high recovery and the two scalar substitutions separately. If the high response has already been absorbed into the particular, the reader must enclose its resulting full phase coefficient; PP alone pays the strict column before that absorption. One can instead perform the two exact scalar substitutions first and retain the general high feedback.

The construction identifies the square core/phase/absolute-placement
block at fixed remaining ports. The cap graph accepts a nonmean far
height function and returns a genuine height span. If the exterior is
also unknown, its equation or full graph fixing $f_B$ must be attached,
with actual units $s_B f_B$, the returned $s_R f_*$, all independent
mean/position conditions and their own source spaces. WOB treats that
entire function as a source. Its inverse does not solve the exterior
matching problem. A square realization for that enlarged problem requires
the exterior graph; this result supplies its core-side equations.
