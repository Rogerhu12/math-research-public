# R150 appendix: an exact lower-degree input for the finite-source H(2+1), Hp=0 chart

日期：2026-11-26 UTC。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

## Status and scope

This appendix gives a proved algebraic equivalence and a new exact characteristic-zero certificate input. It does not record an unexecuted computation as successful and does not claim an invariant-subspace theorem.

The predecessor is [the four-variable quadratic reduction](R150-appendix-rank-three-double-plus-single-zero-hp-four-variable-quadratic-reduction.md), committed in `116a91ca3c94f7c9836ee322839910c20948e4c1`. Its seven necessary equations describe the remaining finite-source chart of the original R150 critical system under the rank-H-three, rank-V-two, essential-dimension-six contradiction hypothesis, with H support type 2+1 and Hp=0. All source and scale exclusions used below are exactly those already paid in that reduction. In particular, no assumption that the whole polar matrix N vanishes is made.

The change here replaces the original jet equation, of degree eight in the isolated-source difference, by an equivalent quadratic equation. The mean-norm and highest-value equations are also quadratic in that difference. The same physical localization is retained. The equivalence is equality of localized ideals, not merely agreement at a modular sample.

## 1. Original physical coefficients and field

Use the original curve u(t)=(1,t,...,t^5)^T and kernel

$
k(s,t)=-(t-s)^2q_s(t),
$
$
q_s(t)=s^3-5s^2+(s^3-3s^2+22s)t
 -(3s^2+3s+5)t^2+(s+1)t^3.
$

The double H source is s, its isolated source is w=s+d, and the two reduced V sources have elementary symmetric functions x and z. Put

$
\Delta=x^2-4z,\qquad E=s^2-sx+z,\qquad E'=2s-x,
$
$
q=x^3-5x^2+x^2z-6xz+32z-5z^2,\qquad
b_s=-2s^2(s-2)(s+6),\qquad q_w=q_s(s+d).
$

For each source t define A_t,B_t by the exact monic division

$
k(t,a)\equiv A_t+B_ta\pmod{a^2-xa+z}.
$

Here A_t,B_t are polynomials in t,x,z; a prime on them below means partial differentiation in t while x,z are held fixed. Define

$
S_*(r)=A_sB_r-B_sA_r,\qquad
N_s=A_s^2+xA_sB_s+zB_s^2,
$
$
J_0=A_sB_s'-B_sA_s'.
$

The original physical factor identities give polynomial quotients

$
J_0=EJ,\qquad N_s=E^2Q_n.
$

Taylor expansion at s defines U,V,W,L without divisions:

$
S_*(s+\delta)=J_0\delta+U\delta^2+V\delta^3+W\delta^4+L\delta^5.
$

The quotient polynomials used by the predecessor are

$
C=U+dV+d^2W+d^3L,\qquad B_1=W+dL.
$

Set w=s+d after forming derivatives in the following expression:

$
k(s,w)\,\partial_sN_s-2N_s\,\partial_sk(s,w)
 =E(w-s)\,W_{\rm red}(s,w,x,z).
$

Write R=W_red(s,s+d,x,z). Also write

$
L_2=2A_sA_w+x(A_sB_w+B_sA_w)+2zB_sB_w,\qquad w=s+d.
$

In this formula B_w denotes the remainder coefficient of k(w,a), not the value at w of the quotient S_*/((r-s)^2(r-w)).

The norm coefficient is defined without selecting roots of the V quadratic. Let

$
Z(r)=(r-s)^2(r-s-d)(r^2-xr+z)
     =\sum_{i=0}^5 Z_i r^i
$

and Z_n=Z_vec^T M Z_vec, where the exact integral matrix is

$
M=3200K^{-1}=
\begin{pmatrix}
25&-25&0&100&80&-2800\\
-25&25&0&-100&-80&-400\\
0&0&0&0&640&3200\\
100&-100&0&0&0&0\\
80&-80&640&0&-6912&-34560\\
-2800&-400&3200&0&-34560&-172800
\end{pmatrix}.
$

Because each Z_i is affine in d, Z_n has degree at most two in d.

The normalized Gram parameter lies in

$
K_e=\mathbb Q[e]/(G_9),\qquad
G_9=16e^9-108e^8+36e^7-15e^6+18e^4-1.
$

The already executed predecessor certificate proves G_9 irreducible by the prime-37 Rabin identities. No fresh irreducibility or modular Groebner calculation is required here. Put

$
c=1-2e,\quad R_e=2e^3+1,\quad Q=4e^3-1,\quad
D=2e^3+1-12e^4,\quad H_0=Q+6e.
$

The nonzero polynomials e, 1-e, c and R_e have degree less than nine and therefore are units in K_e. Every argument below is valid in each complex embedding of K_e.

Work in precisely the predecessor's physical localization

$
\mathcal R=K_e[s,x,z,d,\Pi^{-1}],\qquad
\Pi=s(s-2)(s+6)d\,\Delta qE Q_nq_w.
$

It makes b_s, d, Delta, q, E, Q_n and q_w units. These factors express the previously paid source distinctness and nonzero physical pairings. No factor A or T defined below is added to Pi.

## 2. The predecessor's seven equations

In the notation above the old generators are J, C, H, N, G, K and V_d, with

$
H=(H_0EW+3cU)d^2
 +(2H_0EV+3cE'U)d
 +12e(e^2+1)EU,
$
$
N=c^2U^2Z_n-25600e(1-e)qQ_nE^4d^2,
$
$
G=3e^2R^2+2R_e\Delta q b_sQ_nd^2q_w^2,
$
$
K=2e^2Q L_2+D\Delta qd^2q_w,
$
$
V_d=RU+cQ_nd^2q_wB_1E+cQ_ndq_wUE'.
$

Thus I_old=(J,C,H,N,G,K,V_d) in R. An ordinary polynomial certificate uses the additional inverse variable n and generator nPi-1.

All constants here are the original ones: in particular, the norm coefficient 25600, the jet coefficient 2R_e, and the full V contribution to K and V_d are retained.

## 3. The lower-degree seven equations

Define two new polynomials, without taking any quotient,

$
A=\partial_sJ,\qquad T=A(dE'-E)-2dV.
$

Set

$
\widetilde C=EA+2dV+2d^2W+2d^3L,
$
$
\widetilde H=(2H_0W+3cA)d^2
 +(4H_0V+3cE'A)d
 +12e(e^2+1)EA,
$
$
\widetilde N=c^2A^2Z_n
 -102400e(1-e)qQ_nE^2d^2,
$
$
\widetilde V=RA+cQ_nq_wT,
$
$
\widetilde G=3e^2c^2Q_nT^2
 +2R_e\Delta q b_sA^2d^2.
$

The new ideal is

$
I_{\rm new}=(J,\widetilde C,\widetilde H,
\widetilde N,\widetilde G,K,\widetilde V)\subset\mathcal R.
$

The polynomials A, E, E', U,V,W,L,Q_n,q,Delta,b_s are independent of d, and T is affine in d. Consequently Htilde, Ntilde and Gtilde each have degree at most two in d. Ctilde has degree at most three, while Vtilde has degree at most four. This is a change of generators and does not replace any original equation by a modular approximation.

### Theorem

$
I_{\rm old}=I_{\rm new}\qquad\text{in }\mathcal R.
$

Both quotient rings force A and T to be units. Their nonvanishing is a conclusion of the original equations; it is not an additional open-set restriction.

## 4. Six universal identities

These identities hold already over Q[e,s,x,z,d], before G_9 is imposed.

First,

$
\boxed{2U=E'J+EA.}\tag{1}
$

Indeed, differentiating J_0=A_sB_s'-B_sA_s' gives
A_sB_s''-B_sA_s''=2U; the two first-derivative cross terms cancel. On the other hand differentiating J_0=EJ gives E'J+E partial_sJ.

It follows directly that

$
\boxed{2C-\widetilde C=E'J.}\tag{2}
$

Put

$
H_U=3cd^2+3cE'd+12e(e^2+1)E.
$

Then substitution in H and N gives

$
\boxed{2H-E\widetilde H=E'JH_U,}\tag{3}
$
$
\boxed{4N-E^2\widetilde N
 =c^2E'J(2U+EA)Z_n.}\tag{4}
$

The derivative equation has the exact identity

$
\boxed{
2V_d-E\widetilde V
 =EcQ_nq_w\widetilde C
  +E'J(R+cQ_ndq_wE').
}\tag{5}
$

For clarity, its remaining bracket after applying (1) is

$
2d^2B_1E+d(E'J+EA)E'-ET
 =d(E')^2J+E\widetilde C.
$

Thus no coefficient is discarded under an unproved relation.

Finally, the jet equation satisfies the difference-of-squares identity

$
\boxed{
A^2G-Q_nq_w^2\widetilde G
 =3e^2(AR-cQ_nq_wT)\widetilde V.
}\tag{6}
$

The second terms in G and Gtilde cancel exactly after multiplication. The first terms factor as
3e^2[(AR)^2-(cQ_nq_wT)^2]. This proves (6) without any division by A, T, R, or a source parameter.

The accompanying source constructs all original polynomials from k and K, and checks each of (1)--(6) as a zero integer multivariate polynomial using FLINT. These checks are universal identities and are independent of any subsequent Singular outcome.

## 5. Forward direction, reverse direction, and all divisions

Modulo I_old, identities (2)--(5) imply Ctilde=Htilde=Ntilde=Vtilde=0, in that order. The only divisions in these implications are by the unit E and rational constants. Since G=0, identity (6) then implies Gtilde=0 after dividing by the already physical unit Q_n q_w^2. J and K are unchanged. Therefore I_new is contained in I_old.

Conversely, work modulo I_new. The norm equation says

$
c^2A^2Z_n
 =102400e(1-e)qQ_nE^2d^2.
$

The right-hand side is a unit in the localized quotient ring. Hence A^2Z_n is a unit, and therefore both A and Z_n are units. This assertion holds in a possibly nonreduced commutative quotient ring; it uses only that a product is a unit.

Equations (2)--(5) now recover C=H=N=V_d=0. Identity (6) gives A^2G=0, and the forced unit A gives G=0. Again J and K are unchanged. Thus I_old is contained in I_new, proving equality.

The same norm argument for I_old uses N=0 and (1): N first makes U a unit, then 2U=EA modulo J makes A a unit. There is no special missing A=0 fiber.

Finally, in either equal quotient ring, Gtilde=0 gives

$
3e^2c^2Q_nT^2
 =-2R_e\Delta q b_sA^2d^2.
$

Its right-hand side is a unit, so T is a unit. Vtilde then makes R a unit as well. Thus T=0 and R=0 are excluded by the equations themselves; neither has been silently removed from the input. No new factor is inserted in Pi, and no source-at-infinity or coincident-source case is claimed here: those cases were independently paid in the predecessor branch decomposition.

## 6. Self-contained genuine number-field certificate input

The [independent source](../notes/2026-11-26-h21-lowered-original-true-Ke-certificate-347c.py), already committed at `d673a8dc75646f1fd240bce9ade3e28dfefc8804`, has blob

`8a1fea8b6edc2fffa8c066fe015e05a01af2622f`.

Its input is the eight polynomial generators

$
J,\widetilde C,\widetilde H,\widetilde N,\widetilde G,K,
\widetilde V,n\Pi-1
$

over the actual degree-nine field K_e. It first reconstructs the old eight generators and checks their exact specialization hashes against the already executed frozen modular input. This is an input-identity check only; it does not rerun a modular Groebner basis and supplies no characteristic-zero emptiness assertion.

It then checks the six universal identities above, constructs the new eight generators, and gives their degrees, term counts and hashes. Singular is invoked with the algebraic coefficient field and minpoly=G_9/16 as the first command after ring creation. A separate field check must print the complete line

`ISP_KE_FIELD_RELATION_VERIFIED`

only after verifying G_9(e)=0 in that actual coefficient field. A small lift-and-remultiplication smoke check must independently pass.

The requested certificate is a transformation matrix C_cert with

$
\operatorname{matrix}(I_{\rm input})\,C_{\rm cert}=[1]
$

in the same characteristic-zero polynomial ring. The program explicitly multiplies the returned matrix by the original eight new generators. Success requires the complete stdout line

`ISP_KE_ORIGINAL_UNIT_IDENTITY_VERIFIED`

and the two other complete field/smoke success lines, together with process return code zero. Matching a line echoed as part of an error message cannot meet this predicate. Returned certificate entries have their exact degree and monomial counts reported.

The source bounds this actual characteristic-zero attempt at 900 seconds and 4 GiB address space. A timeout or an unverified product exits unsuccessfully and must be recorded as unresolved. A later actual execution receipt, rather than this source or the already known modular unit ideal, determines whether the unit certificate has been obtained.

This appendix proves the lower-degree equivalence regardless of that computational outcome. If the new characteristic-zero input is proved a unit ideal, the equality of localized ideals above transfers that exclusion to the original seven-equation physical chart, and the predecessor's reconstruction transfers it to the stated R150 branch only.


The first, higher-degree characteristic-zero attempt is recorded separately in [the bounded execution receipt](../notes/2026-11-26-first-true-Ke-and-original-weight-bounded-execution-347c.json): run `45808873477`, job `139871189003`, timed out after 900 seconds with no original unit certificate. This does not affect the proved identities above and is not used as an exclusion result. The present lower-degree source is a changed exact input, not a repeated modular probe.
