# R119 supplement: quantitative radial control on every reserved unused interval

2026-11-14, visible-exact / root. **Proved; 54 exact rational gates passed.**

A later frequency band can now use its own untouched part of the actual
descending ramp. The complete quantitative kernel separation and compact
\(C^4\) control are proved on each such interval, even after earlier
controls have changed the profile elsewhere. Their additional cost is
quadratic in a logarithmic interval parameter. On the actual finite
middle window, the full cost still fits the original angular width.

This supplies directions at true radial resonances. Common finite
parameters, preservation of earlier gaps, and the coupled nonradial
middle inverse remain subsequent tasks.

## 1. Actual family and the reserved intervals

Use the controlled family and its original quantities from
[the complete controlled chart](R119-supplement-controlled-profile-full-label-and-raw-ports.md),
blob \(\mathtt{f11edbccd752bf034aa40e71888859d667a04b42}\), and
[the actual phase compensation](R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md),
blob \(\mathtt{dd0d1378fce997297795ce14312fe91b181af4b1}\).
In particular
\[
 \delta=(2/25)2^{-j},\quad j\ge8193,\quad
 a=\delta^{3/2}/(8\sqrt6),\quad
 j/2<\Delta<3(j+4),\quad B=\Delta/a .
\]
Write \(M=|m|\ge4\), \(\lambda=M^2\),
\[
 K_j=2^{6000}(j+5)^8\delta^{-16},\quad
 \chi=1+M\sqrt{a(1+\Delta)},\quad T=1+\Delta+\chi .
                                                               \tag{S.1}
\]
The true wave propagator and its inverse on every real internal
subinterval have norm below \(K_j\), for the complete new family.

In \(J=[7/16,15/32]\), set \(x_0=113/256\) and reserve
\[
 I_n=\left[
 x_0+\frac1{256}\frac n{n+1},
 x_0+\frac1{256}\frac{n+1}{n+2}\right],\qquad n=0,1,\ldots .
                                                               \tag{S.2}
\]
Their interiors are disjoint. All lie strictly inside \(J\),
and their total length is \(1/256\).
Let \(c_n\) be the midpoint and
\[
 \ell_n=\frac1{512(n+1)(n+2)},\qquad
 L_n=12+\left\lceil\log_2((n+1)(n+2))\right\rceil .
                                                               \tag{S.3}
\]
Then \(L_n\ge13\), \(\ell_n\le1/1024\), and
\[
 2(2+\ell_n)/\ell_n\le2^{L_n},\qquad
 2(1024+\ell_n)/\ell_n<2^{L_n+9}.                    \tag{S.4}
\]

At the current parameter point, assume all previous compact controls
are supported outside \(I_n\). Their total \(C^4\) norm lies in the
already proved ball \(2^{-64}\). The original two compensating bumps
are outside all of \(J\). Consequently the coefficient on \(I_n\) is
still **exactly**
\[
                  Q(x)=7+30B x^2(1-x)^2,\qquad dt=a\,dx .
                                                               \tag{S.5}
\]
The true solution on this interval has the actual real Cauchy values
of the already controlled global profile. No initial datum from the
unperturbed profile is reused.

## 2. Propagation from a short interval inside a fixed complex disk

Let \(I=[c-\ell,c+\ell]\subset J\), \(L\ge13\), and suppose
\(2(2+\ell)/\ell\le2^L\).
If an entire function \(F\) satisfies
\[
 \|F\|_{|z-c|\le1024}\le A,\qquad \|F\|_I\le b\le A,
\]
then
\[
                    \|F\|_{|z-c|\le2}
                          \le3 A^{1-1/L}b^{1/L}.       \tag{S.6}
\]
The case \(b=0\) is the identity theorem.
For \(b>0\), use \(N+1\) Chebyshev nodes on \(I\).
The sum of the Lagrange basis norms is at most \(2^{LN}\).
The exact contour remainder is at most \(2Aq^{N+1}\), with
\[
 q=\frac{2+\ell}{1024-\ell}
 \le\frac{129}{65535}<2^{-8}.
\]
Choose \(N=\lfloor\log_2(A/b)/(L+8)\rfloor\).
The interpolation and remainder are bounded respectively by one
and two times
\(A^{1-\vartheta}b^\vartheta\), where
\(\vartheta=8/(L+8)\ge1/L\). Since \(b/A\le1\), this proves (S.6).

The outer disk has remained fixed. The loss is in the exponent \(1/L\),
and has no dependence on a growing complex radius or on the separation
of quartic roots.

## 3. Full kernel separation on the current untouched interval

At a true resonance take the left unit wave solution and its kernel
\[
 {\cal K}=\mu(h_t^2-2\lambda hh_t+\lambda h^2),\qquad
 \mu_t/\mu=-1-Q .
\]
The input [quantitative kernel proof](R119-supplement-quantitative-transparent-resonance-kernel.md),
blob \(\mathtt{8b5e908a0da26a3a6038de2808cbe41c9849f439}\),
gives the exact local phase kernels \(P/Q^{9/2}\), \(\deg P\le19\).
It also gives the quartic root separation, complete 20-jet Hermite
bound, and the symmetric-square energy identity. Those formulas hold
on \(I\) because (S.5) is the actual coefficient there.

The unique entire continuation of the local quartic solution from
its true value at \(c\) has
\[
 \|{\cal K}\|_{|z-c|\le1024}
 \le {\cal M}:=2^{10}\lambda a^{-2}K_j^2e^{2^{60}T}.
                                                               \tag{S.7}
\]
Every estimate used for this bound is uniform for \(c\in J\):
\(|Q|<2^{46}B\), the balanced generator bound \(2^{47}T\),
the initial wave bounds \(K_j^{-1}\le|Y(c)|\le K_j\), and the
straight-segment length 1024. The continuation is only a local
analytic device; the global profile outside \(I\) need not be quartic.

Here are the changed interpolation constants in full.
For a comparison polynomial \(P\) put
\(\epsilon=\|{\cal K}-P/Q^{9/2}\|_I\).
The case \(\epsilon\ge{\cal M}\) already satisfies all subsequent
lower bounds. Otherwise put \(E=\epsilon/{\cal M}<1\) and
\[
                       p_L=20L+200,\qquad
 {\cal M}_P=2^{p_L}B^5{\cal M}.
\]
On \(I\), \(\|P\|<2^{16}B^5{\cal M}\).
Degree-19 interpolation and (S.4) bound its full large-disk norm
by \({\cal M}_P\).

Use the entire function
\[
                            F=Q^9{\cal K}^2-P^2 .
\]
Its large-disk and small-interval bounds are
\[
 \|F\|_{1024}\le2{\cal M}_P^2,\qquad
 \|F\|_I<2^{31}B^9{\cal M}^2E .
\]
Applying (S.6), and using
\(30-2p_L=-40L-370\), yields
\[
             \|F\|_2<2^{\,2p_L-37}B^{10}{\cal M}^2E^{1/L}.
                                                               \tag{S.8}
\]
At each of the four simple roots of \(Q\), the first nine coefficients
of \(Q^9{\cal K}^2\) vanish. Radius-one Cauchy estimates therefore
bound the first nine coefficients of \(P^2\) by (S.8).
Divide by \({\cal M}_P^2\); the resulting number is at most
\(2^{-37}E^{1/L}<1\).
The complete square-root jet recursion with constants \(1,2,3,5,7\)
then gives the first five coefficients of \(P\) at every root below
\[
                       2^{p_L+3}B^5{\cal M}E^{1/(32L)} .
\]
All four roots are within distance one of any \(c\in J\).
The original Hermite estimate \(2^{80}B^{10}\) thus gives
\[
 \|{\cal K}\|_I
 <2^{p_L+84}B^{15}{\cal M}E^{1/(32L)} .                \tag{S.9}
\]
The comparison includes the whole degree-19 polynomial space,
not just two phase directions.

The exact symmetric-square energy estimate at this same \(c\) gives
\[
 \max(|{\cal K}(c)|,|{\cal K}_x(c)|,|{\cal K}_{xx}(c)|)
      \ge2^{-21}aB^{-4}\lambda^{-2}K_j^{-2}.
\]
Apply (S.6) to \({\cal K}\) and then the radius-one Cauchy estimates.
A valid complete lower bound for its size on \(I\) is
\[
 \|{\cal K}\|_I\ge
 2^{-24L}a^LB^{-4L}\lambda^{-2L}K_j^{-2L}
                                      {\cal M}^{1-L}.  \tag{S.10}
\]
Inserting (S.10) into (S.9) gives, before rounding,
a binary cost \(1728L^2+9088L-10\), a \(B\) cost
\(128L^2+480L\), and the other powers displayed below.
For \(L\ge13\), the conservative result is
\[
 \boxed{\quad
 \operatorname{dist}_{L^\infty(I)}
       ({\cal K},\{P/Q^{9/2}:\deg P\le19\})
 \ge\epsilon_L
 :=2^{-4096L^2}a^{96L^2}B^{-192L^2}
       \lambda^{-96L^2}K_j^{-128L^2}e^{-2^{65}L^2T}.
 \quad}                                                   \tag{S.11}
\]
For example \(9088<(4096-1728)13\) and \(480<(192-128)13\)
pay the two linear-in-\(L\) terms. No numerical root trial or
sampled kernel enters this bound.

## 4. A true compact C4 direction on the short interval

Set \(G=Q^{9/2}{\cal K}\) using the local continuation from Section 3
and the positive branch. Only its restriction to \(I\) is claimed to
be the actual controlled solution. The branch and Cauchy estimates
are uniform for every \(I\subset J\), so
\[
 \|G^{(21)}\|_I\le{\cal M}_{21}=2^{152}B^5{\cal M},\qquad
 \max_{0\le q\le4}\|(Q^{9/2})^{(q)}\|_J<2^{37}B^5 .
\]
Taylor degree 19 on \(I\), together with (S.11), gives a point
where \(|G^{(20)}|\ge\epsilon_L\).
Put \(r=\epsilon_L/(16{\cal M}_{21})\).

This really fits inside the new interval.
Equation (S.4) implies \(\ell>2^{2-L}\), whereas
\(r\le2^{-4096L^2-156}<\ell/8\).
Move the witness point at most \(2r\) inward. On a support of
radius \(r\), the sign of \(G^{(20)}\) is constant and its magnitude
exceeds \(\epsilon_L/2\).

With \(s\) that sign, define
\[
 f(x)=r^{24}\left(1-\left((x-x_1)/r\right)^2\right)_+^{30},
 \qquad
 \psi(x)=\frac{s\,Q^{9/2}f^{(20)}(x)}{2^{220}B^5}.
                                                               \tag{S.12}
\]
Exactly as in
[the full compact-control calculation](R119-supplement-quantitative-phase-preserving-compact-control.md),
blob \(\mathtt{5662bf40391a53a2212311406cf7ad63064908fc}\),
this is compactly supported strictly inside \(I\), is \(C^9\),
and has \(\sum_{q=0}^4\|\partial_x^q\psi\|_\infty\le1\).
Twenty integrations by parts annihilate every \(P/Q^{9/2}\)
of degree at most 19. Thus both actual first phase integrals vanish,
with their original \(dt=a\,dx\) measure.

The full pairing is
\[
 \left|\int{\cal K}\psi\,dx\right|
 \ge2^{-4136}B^{-130}\epsilon_L^{26}{\cal M}^{-25}.
\]
At the current compensated profile, previous compact supports are
disjoint from \(I\). Equation H.17 of the actual phase-compensation
theorem therefore gives \(D\gamma[\psi]=0\) **at this current point**.
The original two bumps make no first-order contribution.

For fixed actual unit left and right Robin lines, the true resonance
normalization is still
\[
 \alpha\Delta_m'(0)=\int{\cal K}\psi\,dt,\qquad
                        0<|\alpha|\le K_j .
\]
Multiplying by \(a/K_j\) and substituting (S.7), (S.11) gives
\[
 \boxed{\quad
 |\Delta_m'(0)|\ge
 D_{L,j,M}:=
 \left[
 2^{-2^{17}}a^{2560}B^{-5120}\lambda^{-2560}K_j^{-3456}
                             e^{-2^{70}T}
 \right]^{L^2}.
 \quad}                                                   \tag{S.13}
\]
The unrounded binary cost is \(26\cdot4096L^2+4386\);
the \(a,B,\lambda,K_j\) powers are respectively
\(2496L^2+51,\ 4992L^2+130,\ 2496L^2+25,\ 3328L^2+51\).
All are bounded by the displayed conservative powers.
Both the material measure and the right resonant amplitude are paid.

Using \(J_0=j+5\), the actual tail bounds give the simpler consequence
\[
 D_{L,j,M}\ge
 \left[
 2^{-2^{25}}\delta^{66816}J_0^{-32768}M^{-5120}
 \exp\{-2^{72}J_0-2^{69}M\delta^{3/4}\sqrt{J_0}\}
 \right]^{L^2}.                                         \tag{S.14}
\]
The exact fixed binary cost before rounding is \(20915712<2^{25}\).

## 5. Every actual middle frequency can be assigned a reserved interval

Use the actual lower and upper middle bounds
\[
 M_{\min}=2^{-40}\delta^{-1/8},\qquad
 T_j=2^{65536}J_0^{204}\delta^{-320}.                    \tag{S.15}
\]
The second is the existing complete high-network threshold;
the controlled-family re-instantiation must retain its own actual
high-block gates. This section concerns the radial directions
through that threshold and does not infer a new high inverse.

Split \([M_{\min},T_j]\) by dyadic frequency bands, starting with
the possibly truncated band at \(M_{\min}\), and assign \(I_n\)
to the \(n\)-th band. The number of bands is less than
\[
 \lceil\log_2T_j\rceil+1
 <65538+(204+320)J_0<2^{10}J_0 ,
\]
using \(j+3<-\log_2\delta<j+4<J_0\).
For every interval so assigned,
\[
 L_n<35+2\log_2J_0<35+j/256<J_0 .                      \tag{S.16}
\]
The bound \(J_0<2^{j/512}\), with its whole-layer induction, was
proved in
[the first full middle-width payment](R119-supplement-middle-angular-width-pays-complete-radial-transversality.md).
Thus all interval parameters in the actual finite middle window
satisfy the needed uniform \(L_n\le J_0\), despite the large
number of frequencies in any band.

## 6. The complete short-support fee still fits the original width

Every cost coefficient inside the brackets in (S.14) is smaller
than the corresponding coefficient of the old \(D_{j,M}\) in W.1
of the middle-width proof.
Before its final uniform rounding, that proof gave
\[
 \frac{-\log D_{j,M}}{M}
 <2^{116}J_0\delta^{1/8}
                 +2^{71}\delta^{3/4}\sqrt{J_0}.
\]
Multiply by \(L_n^2\le J_0^2\), divide by
\(\delta^{1/256}\), and retain the full layer dependence:
\[
 \frac{-\log D_{L_n,j,M}}{M\delta^{1/256}}
 <2^{116-59j/512}+2^{71-759j/1024}.
\]
At \(j=8193\), both terms are strictly below \(2^{-801}\);
their exponents decrease thereafter. The exact checks are
\[
 59\cdot8193>(116+801)512,\qquad
 759\cdot8193>(71+801)1024.
\]
Therefore
\[
 \boxed{\quad
  |\Delta_m'(0)|>e^{-2^{-800}M\delta^{1/256}}
                 =e^{-2^{-803}Mh_j},
 \qquad h_j=8\delta^{1/256}.
 \quad}                                                   \tag{S.17}
\]
All interval-localization, layer-only, frequency-polynomial,
and balanced complex-growth costs have been included.
The original \(\zeta_j,h_j\) and low-frequency radial source
weights are unchanged.

## 7. Scope and actual computation

For each as-yet-unused interval and each current true radial resonance,
(S.12) supplies a real admissible direction and (S.17) pays its full
cost on the assigned actual middle band. The current solution may
already include any permitted earlier controls outside that interval.
This is the property needed to proceed through frequency bands
without incorrectly continuing the quartic formula through a
previously changed support.

No simultaneous parameter point has yet been selected here.
Finite parameter boxes require the actual Hessian, control of
near-resonant rather than exactly resonant points, and an explicit
budget protecting earlier gaps. The true coupled nonradial system,
all ordinary/weak source columns, both physical traces, mean and
height, and positive-DN cross terms remain separate obligations.

The complete function in
[scripts/fourfold_unused_interval_radial_control.mjs](../scripts/fourfold_unused_interval_radial_control.mjs)
was executed in V8 using normalized exact BigInt rational arithmetic.
All 54 gates passed. The full report is
[notes/2026-11-14-R119-unused-interval-radial-control-rational.json](../notes/2026-11-14-R119-unused-interval-radial-control-rational.json).
It records the four input proof identities, the exact interval
construction, kernel and true compensated Wronskian bounds, and
the actual middle domain. The analytic arguments above establish
the unbounded layer and frequency claims; the report contains no
pretended numerical solve.
