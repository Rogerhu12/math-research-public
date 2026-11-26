# R150 appendix: two linear isolated-source equations on the unchanged physical chart

Date: 2026-11-26 UTC. Author: Astra-ISP-347c-20261126 / prior_results_map; AI-assisted GPT-6 Astra Pro.

## Status

This is an exact further change of generators for the finite-source H(2+1), Hp=0 chart. It is not a new modular experiment and does not assert that an unexecuted characteristic-zero certificate has succeeded. It depends on the [exact lower-degree seven-equation equivalence](R150-appendix-rank-three-double-plus-single-zero-hp-lowered-original-ideal-equivalence.md) and retains precisely its physical localization Pi.

The result is that the source cubic and jet quadratic can both be replaced by equations linear in d=w-s. Keeping the norm quadratic pays every division by A. No new open subset is selected.

## 1. Notation

Use the preceding lower-degree reduction's polynomials

$
J,\quad \widetilde C,\quad \widetilde H,\quad
\widetilde N,\quad \widetilde G,\quad K,\quad \widetilde V
$

in R=Ke[s,x,z,d,Pi^{-1}]. All definitions of the original kernel, E=s^2-sx+z, E'=2s-x, A=partial_s J, the Taylor coefficients V,W,L, Q_n, q, Delta and b_s are unchanged.

In particular,

$
\widetilde C=EA+2dV+2d^2W+2d^3L,
$
$
\widetilde H=h_0+h_1d+h_2d^2,
$

where

$
\gamma=12e(e^2+1),\qquad h_0=\gamma EA,
$
$
h_1=4H_0V+3cE'A,\qquad h_2=2H_0W+3cA.
$

Here c=1-2e, H_0=4e^3-1+6e, R_e=2e^3+1, and the normalized Gram field is Ke=Q[e]/G_9 with the previously proved irreducible polynomial G_9 of degree nine.

The retained norm equation

$
\widetilde N=c^2A^2Z_n-
102400e(1-e)qQ_nE^2d^2=0
$

makes A a unit in either quotient used below. The constant gamma is also a unit: it is a nonzero polynomial of degree three in e. E and d are original physical units. Consequently h_0 is a forced unit.

## 2. Linear replacement of the source cubic

Put

$
D_v=4R_eV-3cE'A.
$

The exact scalar identity 2gamma-4H_0=4R_e gives D_v=2gamma V-h_1. Define the polynomial linear in d

$
C_{\rm lin}=
 (2\gamma^2EA L-h_2D_v)d
 +2\gamma^2EA W-\gamma EA h_2-h_1D_v.
$

The universal polynomial identity is

$
\boxed{
\gamma^2EA\,\widetilde C
 -(h_0+D_vd)\widetilde H
 =d^2C_{\rm lin}.
}\tag{1}
$

To verify it, expand both sides by powers of d. The constant terms cancel because h_0=gamma EA. The coefficient of d cancels because D_v=2gamma V-h_1. The remaining coefficients of d^2 and d^3 are exactly the displayed constant and linear coefficients of C_lin. No field relation or geometric equation is used in this identity.

Modulo the retained norm and physical localization, E,A,d,gamma are units. Hence adjoining Htilde=0 makes Ctilde=0 equivalent to C_lin=0.

## 3. Linear replacement of the jet quadratic

Put

$
B=AE'-2V,\qquad C_s=3E'A-4V,\qquad
J_e=8e^3+6e+1.
$

Then the existing jet quadratic is

$
\widetilde G=3e^2c^2Q_n(Bd-EA)^2
 +2R_e\Delta q b_s A^2d^2.
$

Its constant coefficient is

$
g_0=3e^2c^2Q_nE^2A^2.
$

Define

$
L_d=
12e^2(e^2+1)c^2Q_nB^2
+8R_e(e^2+1)\Delta q b_sA^2
-e c^2Q_nEA h_2
$

and the polynomial linear in d

$
G_{\rm lin}=L_dd-e c^2Q_nEAJ_e C_s.
$

The second universal identity is

$
\boxed{
h_0\widetilde G-g_0\widetilde H
 =3eEA\,d\,G_{\rm lin}.
}\tag{2}
$

For the coefficient of d, the elementary cancellation is

$
24e(e^2+1)B+h_1=J_e(3E'A-4V).
$

The constant coefficient of the left side is zero. Its coefficient of d^2 is 3eEA times the displayed L_d. This proves (2) as an identity before imposing G_9.

Because h_0, 3eEA and d are units modulo the retained norm and original physical factors, Htilde=0 makes Gtilde=0 equivalent to G_lin=0.

Neither L_d nor C_s is divided out. In particular, their simultaneous-zero fiber remains in the equations. Writing G_lin as a linear relation is not permission to solve for d unless the corresponding coefficient is separately known to be nonzero.

## 4. Exact equality of localized ideals

The two identities show

$
(J,\widetilde C,\widetilde H,\widetilde N,
 \widetilde G,K,\widetilde V)
=
(J,C_{\rm lin},\widetilde H,\widetilde N,
 G_{\rm lin},K,\widetilde V)
$

inside R. For the forward inclusion use the physical unit d in (1) and the forced units e,E,A,d in (2). For the reverse inclusion first use the retained norm to make A a unit, then (1) recovers Ctilde and (2) recovers Gtilde.

Thus, together with the predecessor's six universal identities, the two-linear input is exactly the original seven-equation physical chart. It preserves every previously unpaid source fiber and introduces no additional saturation factor.

The same principle can be viewed by setting y=1/d: the reversed H equation is h_0y^2+h_1y+h_2, whose leading coefficient is a forced unit. Identities (1) and (2) are explicit small remainders of the reversed source and jet equations. The displayed formulas avoid expanding a general high-degree pseudo-division.

## 5. Exact certificate execution interface

The [frozen source](../notes/2026-11-26-h21-two-linear-original-true-Ke-certificate-347c.py), blob `70cde76699e9a440c638c5908f6dc907724fac1d`, was launched by commit `bc05818d4e52ccdbe16b1df5ba632d3b3e3a7c0a` through the repository's public Actions workflow. Its execution is separate from the polynomial proof above.

It reconstructs the original physical polynomials, performs the six predecessor identities, and then checks (1) and (2) as literal zero multivariate integer polynomials. It also checks deg_d C_lin <=1 and deg_d G_lin <=1. It retains the norm generator and exactly the same nPi-1 generator.

Its characteristic-zero field check, lift smoke check, complete stdout-line verification, actual multiplication matrix(I)*certificate=[1], 900-second Singular bound, 4-GiB address bound, and failure semantics are those of the lower-degree source. No modular Groebner gate is rerun. The frozen old modular hashes are checked solely for input provenance.

The source has not been declared successful by this appendix. Any actual future execution must supply its own source SHA, input SHA and execution receipt; a timeout remains unresolved. A verified unit identity would close only the explicitly stated R150 finite-source branch.
