# R133 supplement: a root-anchored characteristic enclosure and exact continuation of the larger auxiliary case

2026-11-14, phase_inverse.

**Proved enclosure refinement and a fixed-prefix continuation contract.**
This uses the completed coefficient stages of public run 43646714623.
It introduces a new bound for the same analytic characteristic speed
on the larger proposed auxiliary fold. It does not change the original
family, root, completed smaller case, or original failed gate.

Numerical success of the larger fold remains conditional on the new
public execution. The original child return $1$ and its failed radial
self-map are retained.

## 1. The same analytic function has a root integral

Use the unchanged notation of
[the anchored-fold theorem](R133-supplement-anchored-auxiliary-fold-and-direct-complex-leading-derivatives.md).
On the auxiliary old product let
$$
 a(\rho,\delta)=\eta(\rho,\delta)\sqrt{k(\rho)},\qquad
 a_*(\delta)=\eta_*(\delta)\sqrt{k_*}.
 \tag{C.1}
$$
The root is real and fixed on the full complex disk $|\delta|\le10^{-8}$.
The two roots and the fractional power are the same branches used
by the complete old scalarization. The mean entering $\eta$ includes
the repaired full 193-component direction.

The completed larger coefficient stage already provides
$$
 \operatorname{Re}k\ge k_->0,\quad |k|\le k_+,\quad
 |\eta|\le\eta_+,\quad |\eta_\rho|\le\eta_1,\quad
 |k_\rho|\le k_1
 \tag{C.2}
$$
on $|\rho|\le R=3/8000$. Consequently its saved number
$$
 A_1=\eta_1\sqrt{k_+}
       +\frac{\eta_+k_1}{2\sqrt{k_-}}
 \tag{C.3}
$$
is a complete bound for $|a_\rho|$. This formula does not depend on
a previously computed rectangle for $a$. It is already an accepted
part of the old coefficient prefix.

For every point and fixed allowed complex parameter, the straight
segment from the true root stays in the same auxiliary product.
The fundamental theorem of holomorphic differentiation therefore gives
$$
 a(\rho,\delta)-a_*(\delta)
   =\rho\int_0^1 a_\rho(t\rho,\delta)\,dt,\qquad
 |a-a_*|\le R A_1 .
 \tag{C.4}
$$
This is an estimate for the actual holomorphic function, not an
independent branch selection or a derivative of an interval enclosure.

If $\mathcal B_{\rm old}$ is the previously saved rectangle for $a$,
and $\mathcal B_*$ the saved root rectangle, a valid tighter rectangle is
$$
 \mathcal B_{\rm new}
 =\mathcal B_{\rm old}\cap
   \bigl(\mathcal B_*+[-RA_1,RA_1]+i[-RA_1,RA_1]\bigr).
 \tag{C.5}
$$
Both component intervals must have a nonempty intersection.
The rectangular enlargement in (C.5) contains the disk in (C.4);
no disk is enlarged into an asserted physical holomorphic domain.

There is also the independent modulus bound
$$
 |a|\le\eta_+\sqrt{k_+}.
 \tag{C.6}
$$
Thus the new stored lower and upper bounds are
$$
 a_-^{\rm new}=\inf\operatorname{Re}\mathcal B_{\rm new},\qquad
 a_+^{\rm new}=\min\left(
       \sup_{z\in\mathcal B_{\rm new}}|z|,
       \eta_+\sqrt{k_+},a_+^{\rm old}\right).
 \tag{C.7}
$$
All operations use directed Arb endpoints. The derivative bounds
$A_1,A_2$ and every other complete coefficient bound stay unchanged.

This refinement avoids depending solely on the rectangle returned by
the square-root evaluation of a wide complex interval. It makes no
claim that the latter original rectangle was invalid.

## 2. Exactly which new stages are needed

The accepted source for run 43646714623 is SHA256
`410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783`,
and its input manifest is
`1f5de8e5f2a877bad414ec50d50b47ca8ac816a05ef1e90303e3dc79edecbdb9`.
Its exact original native is
`a6f6225cd993718f48b9d35533b81134f966f350b1c9ce704e61e38b34855807`.

The successor must verify all those identities and its original
process return $1$. It then copies, without mathematical reevaluation:

- the complete root anchor;
- the entire successful $R=3/40000$ case, including its 13 gates,
  fold, direct leading derivatives, forcing and first correction;
- the accepted complete coefficient stage for $R=3/8000$.

The first new mathematical stage is only (C.5)--(C.7) for the latter
case. The new complete coefficient dictionary is a copy of the old one
with only its speed rectangle, speed real-part lower bound and speed
modulus upper bound refined. The old dictionary and all its hashes
remain available separately.

The remaining new stages evaluate the unchanged anchored-fold,
direct-leading and forcing functions using this refined input.
They are new bounds for the previously unresolved larger case.
The old failed self-map gate is not edited or reclassified.
The same radial self-map threshold, canonical radius, angular widths,
physical inner cover and full complex parameter disk are used.

The scientific implementation imports the exact old scientific source,
whose hash is checked before use. It must not call the old coefficient
constructor or the old root-anchor constructor. Every newly completed
refinement/fold/leading/forcing stage is checkpointed immediately.
A subsequent interruption resumes only an identical new source,
manifest, runtime and original native identity. Failed outcomes remain
in the final actual audit.

## 3. Physical identity and limitations

All auxiliary characteristics belong to the analytic continuation of
the same original scalar and cubic root piece. Any first correction
used as a statement about the physical background is still restricted
to the original scalar/cubic intersection. Its coincidence with the
physical correction follows from the same root initial-value problem
and uniqueness. No new interface condition is inserted.

All original physical seams, the independent even mean, both original
old-angle projections, the complete old $I/J$ inverse remainder, and
the full parameter direction remain part of the problem.
A successful larger inverse gate would provide additional domain
and derivative bounds. It would not by itself prove a small strong
return, a cutoff-97 inverse, or a nonlinear PDE solution.
