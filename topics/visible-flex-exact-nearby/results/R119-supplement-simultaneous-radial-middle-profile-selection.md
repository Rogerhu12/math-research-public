# R119 supplement: one phase-preserving radial profile for every actual middle frequency

2026-11-14, visible-exact / root. **Proved; 30 exact rational gates passed.**

For each actual controlled negative window there is now one common real
compact shape that preserves both prescribed radial phases and gives a
quantitative nonzero normalized Wronskian for every fourfold frequency
in its genuine moving-middle range. The entire shape has \(C^4\) norm
less than \(2^{-65}\). The construction uses successive unused supports,
finite parameter boxes, and an explicit budget preserving earlier gaps.

The conclusion concerns the fixed-port radial Wronskians. It does not
invert the full network of positive-DN cross contacts or the nonradial
middle matrix. No numerical list of the selected shape parameters is
reported by the accompanying exact-budget calculation.

## 1. Actual domain and statement

Use the exact controlled family and actual two-phase compensation of
[the Hessian theorem](R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md),
blob \(\mathtt{dd0d1378fce997297795ce14312fe91b181af4b1}\).
Use the disjoint intervals and true current-profile controls of
[the unused-support theorem](R119-supplement-unused-short-interval-radial-control-and-width.md),
blob \(\mathtt{27e75c019c0e4441c3237a36bb3c9f485fd2cdbf}\).

Fix \(j\ge8193\), one actual radial window, and its real slide parameter.
Let
\[
 \delta=(2/25)2^{-j},\quad J=j+5,\quad
 h=8\delta^{1/256},\quad
 K=2^{6000}J^8\delta^{-16},\quad B=\Delta/a.
\]
The genuine middle range is
\[
 {\cal M}_j=\{M\in4\mathbb N:
      2^{-40}\delta^{-1/8}\le M\le T_j\},\qquad
 T_j=2^{65536}J^{204}\delta^{-320}.                      \tag{C.1}
\]
The [controlled-family joint/high theorem](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md),
blob \(\mathtt{fc3aab62e99a51cc06bd26a7233663a2b8e4dd73}\),
has now re-established this same actual high threshold on the new
family. It has not closed the middle matrix.

For each \(M\), fix real unit left and right wave lines \(l_M,r_M\).
In the intended local radial Schur application they are the unchanged
positive-DN diagonal Robin lines. Their off-diagonal contacts remain
external network inputs. Let
\[
 {\cal W}_M(\Xi)=[r_M,{\cal C}_M(\Xi)l_M]                \tag{C.2}
\]
be the true normalized Wronskian, with the exact two-bump compensation
included in \({\cal C}_M\).

There exists a real finite sum \(\Xi_j\) of the actual compact directions
such that
\[
 \boxed{\qquad
 \|\Xi_j\|_{\sum_{q=0}^4\|\partial_x^q\cdot\|_\infty}<2^{-65},
 \qquad
 |{\cal W}_M(\Xi_j)|>e^{-2^{-800}Mh}
           \quad\hbox{for every }M\in{\cal M}_j .
 \qquad}                                                  \tag{C.3}
\]
Both prescribed radial phases are exactly unchanged. Negative Fourier
modes are the real-conjugate copy of this same scalar radial equation.

The construction can be made in every actual internal window, with the
same uniform \(C^4\) bound. The resulting sequence belongs to the already
paid \(\ell^\infty(C^4)\) parameter ball. This does not assign uniform
fifth or higher shape derivatives or introduce a new source norm.

## 2. Dyadic bands and uniform real derivative bounds

Put
\[
 k_0=\left\lfloor\frac{j+3}{8}\right\rfloor-40,\qquad
 U_n=2^{k_0+n+1}.
\]
Because \(j+3<-\log_2\delta<j+4\),
\(k_0=\lfloor\log_2(2^{-40}\delta^{-1/8})\rfloor\) exactly.
Band \(n\) consists of the actual modes with
\[
                   U_n/2\le M<U_n
\]
after intersection with (C.1). Include the final endpoint in the next
band if it is itself a dyadic boundary. Thus \(U_n\le2T_j\),
and every mode in the band satisfies \(U_n\le2M\).
There are fewer than \(2^{10}J\) bands.

Assign the unused interval \(I_n\) from S.2 to band \(n\).
Its parameter \(L_n\le J\), and the full short-support theorem gives
a compensated directional derivative at each true resonance exceeding
\(e^{-2^{-803}Mh}\).
Set
\[
 \epsilon=2^{-803},\qquad
 D_n=e^{-\epsilon U_nh},\qquad
 A_n=2K^2(U_n+B).                                      \tag{C.4}
\]
The lower bound \(D_n\) is therefore valid for every mode in this band
whenever its current resonance is controlled on \(I_n\).

On the entire real phase-annihilator ball \(2^{-64}\), the actual
one- and two-variation Duhamel bounds give, for all those modes,
\[
 \|D{\cal C}_M\|\le A_n,\qquad
 \|D^2{\cal C}_M\|\le A_n^2,\qquad
 \|D{\cal W}_M\|\le A_n,\qquad
 \|D^2{\cal W}_M\|\le A_n^2 .                           \tag{C.5}
\]
Indeed \(M+B/M\le U_n+B\), and
\[
 2^{22}K^3(U_n+B)^2\le4K^4(U_n+B)^2=A_n^2
\]
since \(K>2^{6000}>2^{20}\).
The lines and endpoint wave changes are fixed. No missing derivative
of a variable global right line is omitted in (C.5).

## 3. Near-resonant modes have a direction for the actual fixed line

At the start of band \(n\), all previous shape supports are outside
\(I_n\). The coefficient on \(I_n\) is consequently still the actual
quartic. Set
\[
                              q_n=D_n/(16A_n^2).       \tag{C.6}
\]
Call a mode active if \(|{\cal W}_M|\le q_n\).

Write \(v={\cal C}_Ml_M\). The true inverse propagator bound gives
\(|v|\ge K^{-1}\). Choose the sign of
\(\widetilde r=v/|v|\) so that it is the closer unit line to \(r_M\).
Then
\[
                |r_M-\widetilde r|
                    \le2\,|{\cal W}_M|/|v|
                    \le2K|{\cal W}_M|.                 \tag{C.7}
\]
The projection is nondegenerate because
\(q_n<1/(2K)\).

With this auxiliary right line, the current left solution is exactly
resonant. The kernel and compact-control proof used only that left
unit solution, the true two-direction propagator bound, and the
right resonant amplitude \(0<|\alpha|\le K\). It therefore applies to
this auxiliary line as well. This gives a real direction
\(\psi_M\) supported strictly inside \(I_n\), with sum \(C^4\) norm
at most one and both phase derivatives zero, for which the auxiliary
Wronskian derivative has magnitude at least \(D_n\).

The auxiliary line is held fixed while taking this derivative.
It is an estimate for the direction, not a replacement boundary
condition for the actual problem. By (C.5)–(C.7), the difference from
the original fixed-line derivative is at most
\[
        2Kq_nA_n\le D_n/8 .
\]
Orient the direction so that the actual derivative is positive.
Then at the current profile
\[
                          D{\cal W}_M[\psi_M]\ge7D_n/8 .
                                                               \tag{C.8}
\]
The exact zero first derivative of the two compensating bumps at
this current point follows from the unused-support identity H.17.
It has not been extrapolated from the original unperturbed profile.

## 4. One finite parameter box treats the entire band

Let \(d\) be the number of active modes; \(d\le U_n\).
For \(d>0\) use their directions simultaneously:
\[
        \Xi=\Xi_{\rm old}+\sum_{a=1}^d t_a\psi_a,\qquad
                         |t_a|\le\rho_n/d .            \tag{C.9}
\]
Require
\[
                              \rho_n\le D_n/(64A_n^3).
                                                               \tag{C.10}
\]
The total shape change has sum \(C^4\) norm at most \(\rho_n\).
The complete compensated Hessian (C.5) changes each derivative
in (C.8) by at most
\[
                      A_n^2\rho_n\le D_n/(64A_n)\le D_n/64 .
\]
Thus throughout the whole box each active mode has its own coordinate
derivative at least \(D_n/2\). Cross-coordinate effects are included
in this Hessian bound.

An inactive mode initially has \(|{\cal W}_M|>q_n\).
Its complete variation is at most
\(A_n\rho_n\le q_n/4\), so it stays above \(3q_n/4\).

Define
\[
                              g_n=D_n\rho_n/(16U_n^2).
                                                               \tag{C.11}
\]
For an active mode, fix all other coordinates. Strict monotonicity in
its own coordinate shows that the portion where
\(|{\cal W}_M|\le g_n\) has length at most \(4g_n/D_n\).
The full coordinate interval has length \(2\rho_n/d\), so its
conditional bad fraction is at most \(2dg_n/(D_n\rho_n)\).
Fubini and the union bound over all \(d\) active modes give
\[
                  \hbox{bad fraction}
                    \le\frac{2d^2g_n}{D_n\rho_n}\le\frac18 .
                                                               \tag{C.12}
\]
The inactive modes already stay above \(g_n\):
indeed \(g_n\le q_n/64<3q_n/4\).
There is therefore a parameter point at which **every** actual
mode of this band has \(|{\cal W}_M|>g_n\).

The complement of the finitely many closed bad sets has positive
volume and contains an interior point of the box. It is open, so
rational coefficient vectors are available. Together with the
explicit compact directions and rigorous ODE evaluation, a fixed
dense enumeration gives a finite terminating selection procedure.
The present result proves its existence and bounds; it does not
claim that these large finite lists were numerically evaluated.

If \(d=0\), choose the zero increment. All modes already have the
required margin, and the same conservative \(g_n\) is recorded.

## 5. Later controls preserve all earlier gaps

Start with \(\Xi_{-1}=0\) and choose the deterministic radii
\[
 \rho_0=\min(2^{-66},D_0/(64A_0^3)),
\]
\[
 \rho_n=\min\left(D_n/(64A_n^3),
                  \frac{g_{n-1}}{16A_{n-1}}\right)
                    \quad(n\ge1),                     \tag{C.13}
\]
where \(g_n\) is (C.11). These radii depend on the explicit
bounds, not on a favorable sampled Wronskian.

Since \(D_n\le1\), \(A_n\ge1\), and \(U_n\ge1\),
\[
 \rho_{n+1}\le\frac{\rho_n}{256A_nU_n^2}
                         \le\rho_n/256 .
\]
Consequently
\[
 \sum_n\rho_n<2\rho_0\le2^{-65}<2^{-64}.               \tag{C.14}
\]
Every intermediate shape and its full parameter box stay inside
the actual compensation and Hessian domain.

For any earlier band \(b\),
\[
 \sum_{n>b}\rho_n
 <2\rho_{b+1}\le g_b/(8A_b).
\]
The derivative bound \(A_b\) for its modes remains valid at every
later controlled profile, because (C.5) is uniform on the whole
ball. Their total subsequent change is below \(g_b/8\).
Their final gap is therefore greater than \(7g_b/8\), in particular
greater than \(g_b/2\).

Every new band uses a still untouched \(I_n\). The loss of the
quartic formula inside previously used intervals is irrelevant:
no later kernel proof is applied there. The final finite sum is
\(C^9\) for each window, while only the uniform \(C^4\) norm in
(C.14) is used across all layers.

## 6. Full cost of radii, dimension and preservation

Write
\[
 d_n=-\log D_n=\epsilon U_nh,\quad
 a_n=\log A_n,\quad u_n=\log U_n,\quad r_n=-\log\rho_n .
\]
The exact recurrence (C.13) is
\[
 r_0=\max(66\log2,\ d_0+6\log2+3a_0),
\]
\[
 r_n=\max(d_n+6\log2+3a_n,\ 
    d_{n-1}+r_{n-1}+8\log2+a_{n-1}+2u_{n-1}).          \tag{C.15}
\]
The second expression includes both factors 16 and the complete
number-of-modes fee \(U_{n-1}^2\).

Since \(U_n\) doubles and \(A_n\) increases, induction gives
\[
 r_n\le66\log2+
       \sum_{b=0}^n(d_b+8\log2+3a_b+2u_b)
 <2d_n+66+(n+1)(8+3a_n+2u_n).                         \tag{C.16}
\]
No recurrence is replaced by an unspecified positive constant.

The actual middle range gives the following complete bounds:
\[
 n+1<2^{10}J,\quad \log K<25J,\quad
 \log B<4J,\quad u_n<2^{10}J,\quad a_n<2^{11}J .
                                                               \tag{C.17}
\]
For clarity, \(B<96J\delta^{-3/2}\).
Also \(U_n\le2T_j\), so
\(\log_2U_n<65537+524J<1024J\).
Finally
\(\log A_n<2+50J+\max(\log U_n,\log B)<2048J\).
All these inequalities hold at the first layer and improve or remain
strict for larger \(j\).

Inserting (C.17) into (C.16) gives
\[
 r_n<2d_n+2^{24}J^2 .
\]
From (C.11), including the final factor two reserved for future
changes, it follows that
\[
                         -\log(g_n/2)
                         <3d_n+2^{26}J^2 .             \tag{C.18}
\]
The cost of all previous bands, the \(d\)-dimensional box, and
preservation of their gaps has now been explicitly paid.

For a mode in band \(n\), \(U_n\le2M\).
The first term in (C.18) is at most \(6\epsilon Mh\).
The actual moving-middle lower bound pays the remaining layer term:
\[
 \frac{2^{26}J^2}{Mh}
 \le2^{63}J^2\delta^{31/256}
 <2^{63-15j/128}<2^{-803}.                             \tag{C.19}
\]
Here \(J<2^{j/512}\) is the already proved whole-layer bound,
and the final strict check at \(j=8193\) is
\[
                         15\cdot8193>(63+803)\cdot128 .
\]
It continues to improve with \(j\).
Thus
\[
 -\log(g_n/2)<7\cdot2^{-803}Mh<2^{-800}Mh,
\]
which proves the complete simultaneous gap (C.3).
The original \(h_j,\zeta_j\), low-frequency radial source weights,
and finite/head conventions have not been changed.

## 7. Exact phases, all windows, and retained source obligations

Each direction in (C.9) belongs to the same closed two-phase
linear annihilator. The single compensation map
\(\gamma(\Xi)\) from the actual two-bump theorem is used at every
stage; separate approximate phase corrections are not accumulated.
It preserves both full phases exactly at the final shape.

The uniform norm (C.14) permits the construction in every internal
window simultaneously. The resulting \(\Omega\) lies inside the
same actual parameter domain used by the controlled joint-phase
and high-network theorem. Its incoming map and full remaining
equation are those of that new object.

The mean resistance and height generally change. Their complete
sources remain, along with both weak components, ordinary source,
total endpoint traces, bare-flux trace requirements, and positive-DN
off-diagonal contacts. A scalar local Wronskian gap does not solve
these source or coupling equations.

In particular this result does **not** claim:

* an inverse for the full coupled radial network merely from its
  separate fixed-port diagonal Wronskians;
* a same-weight inverse for the nonradial middle matrix;
* smallness of a radial gap inverse times an absolute nonlinear
  remainder;
* analytic dependence of this discrete good-parameter selection on
  labels or on an independently selected global right line;
* vanishing of the actual incoming remainder or completion of the
  final closed surface.

Those are the remaining matching and operator questions. The genuine
advance here is one common, phase-preserving, uniformly small radial
profile with all the displayed middle-frequency margins, including a
finite-step and future-preservation proof.

## 8. Actual exact-budget execution

The complete function in
[scripts/fourfold_simultaneous_radial_middle_selection.mjs](../scripts/fourfold_simultaneous_radial_middle_selection.mjs)
ran in V8 with normalized exact BigInt rationals.
All 30 gates passed. The execution report is
[notes/2026-11-14-R119-simultaneous-radial-middle-selection-rational.json](../notes/2026-11-14-R119-simultaneous-radial-middle-selection-rational.json).

The report checks the true Hessian conversion, auxiliary-line fees,
full parameter-box and bad-volume factors, radius recurrence,
retention of earlier gaps, all polynomial logarithmic costs and
the final original-width payment. It records source SHA-256 and
input proof identities. It expressly distinguishes the proved
finite-selection construction from a numerical array of selected
parameters, which has not been computed here.
