# R43 supplement: the complete root potential through the physical cut

For the unchanged old R37 fixed-type family, the complete exact negative
canonical potential has now been bounded on a product neighborhood containing
the whole root-to-strict-cut collar. The result is

\[
\boxed{|V|<752814}
                                                               \tag{V.1}
\]

on

\[
 \operatorname{dist}(\xi,[0,1/4000])\le1/100000,
 \qquad |\Im\phi|\le1/40000.                                \tag{V.2}
\]

The radial derivative bound
\(|V_\xi|<7.528136\,10^{10}\) holds for real
\(0\le\xi\le1/4000\), still with \(|\Im\phi|\le1/40000\).
This derivative estimate is not asserted on the radial halo boundary.

Every true physical strict cut is strictly inside this rectangle. Its exact
canonical graph was already certified in the preceding real-cut supplement.
The new bound uses the full seven analytic fields, their true parameter and
infinite errors, and an exact second-order removable quotient. It is not an
extension of the root jets by assumption and does not use the positive-side
finite canonical chart.

A constant-potential reference of 5050 then gives a full-frequency height
Volterra contraction below \(.023683236\) on \(0\le\xi\le1/4000\), with
the mean retained. The higher Sobolev, complete momentum/source and graph
frame estimates are separate consumers. This note does not upgrade a height
\(L^2\) contraction to the full strong returned remainder.

## 1. Recover the complete invariant potential density from the seven fields

Use \(\rho=t(p)-r\), pointing into the negative side. Let

\[
 G=\rho^{5/2}D_{\rm red},\quad
 S=\rho^{-1/2}S_{\rm reg},\quad
 V_\rho=\rho^{-3/2}U_0+\rho^{-1/2}U_1,
\]

\[
 V_\theta=qV_\rho-\sqrt\rho\,kL_\theta,
 \qquad kU_0=1/2.
\]

Here \(V_\rho,V_\theta\) are the R106 vector-density components, not the
canonical scalar potential. The full old operator includes the original
fixed-type zero-order term. R106 (106.2)–(106.3) gives

\[
 \frac{\mathcal F}{\mu}
 =D_{\rm red}+\partial_\theta S
                 -\tfrac12(\partial_\rho V_\rho+\partial_\theta V_\theta).
                                                               \tag{V.3}
\]

Thus the analytic numerator \(A=\rho^{5/2}\mathcal F/\mu\) is exactly

\[
\begin{aligned}
 A={}&G+\tfrac34U_0
 +\rho\left[\tfrac14U_1-\tfrac12U_{0,\rho}
                         -\tfrac12(qU_0)_\theta\right]\\
 &+\rho^2\left[(S_{\rm reg})_\theta-\tfrac12U_{1,\rho}
                         -\tfrac12(qU_1)_\theta\right]
 +\tfrac12\rho^3(kL_\theta)_\theta .                         \tag{V.4}
\end{aligned}
\]

In particular, the angular divergence and both radial vector terms are
retained. Omitting them would not give the same potential.

Set \(Z=G+U_0/8\). The actual leading identity in the seven-field proof gives
\(Z(0,\theta)=0\). With the exact characteristic coefficient

\[
 \mathcal C=-\frac{U_{0,\rho}+qU_{0,\theta}}{U_0}-q_\theta,
\]

(V.4) becomes the more accurately evaluated identity

\[
\begin{aligned}
 H:=kA-\tfrac5{16}
 ={}&kZ+\tfrac\rho4(kU_1+\mathcal C)\\
 &+\rho^2 k\left[(S_{\rm reg})_\theta-\tfrac12U_{1,\rho}
                                 -\tfrac12(qU_1)_\theta\right]
 +\tfrac12\rho^3 k(kL_\theta)_\theta .                      \tag{V.5}
\end{aligned}
\]

The linear finite combination \(Z\) is formed before interval evaluation.
Its complete error is \(\epsilon_G+\epsilon_{U_0}/8\); no assumed correlation
between different error balls is used.

## 2. Actual complete joint-boundary calculation

The new native producer is
`fourfold_negative_root_complete_potential_density.py`. It consumes the exact
same complete parameter-transferred degree-80/Fourier-degree-650 report as the
previous characteristic certificate. Its new closed bidisk is

\[
 R=279/10^6=.000279,\qquad S=11/5000=.0022,
\]

inside the existing \((.00028,.0025)\) analytic field domain.
The 128 radial phase cells and 2048 angular cells include every finite
coefficient, both signs of every retained angular frequency, all finite
closed-cell motions and all true errors. Derivative errors are paid from the
remaining radial or angular Cauchy margin of the actual field certificate.
The complex value of \(\rho\) itself is enclosed over each entire radial
phase cell before it is used in (V.5).

The complete calculation proves

| Field or denominator | Complete bidisk bound |
|---|---:|
| \(\mathcal C\) | \(<101.595550376\) |
| \(q\) | \(<.823406660795\) |
| \(k\) | \(<21.765654458\) |
| \(U_0\) | \(<.149378378289\) |
| \(H\) | \(<.015876725889\) |
| \(\Re U_0\) | Positive, stored with directed endpoints |

The positive-real-part check on \(U_0\) is made before forming its quotient.
Schwarz reflection supplies the second angular boundary. Successive maximum
principles give the entire bidisk for the denominators and holomorphic
quotients. The producer took about 160.76 seconds.

Take the same characteristic start strip \(S_1=3/2000\). The exact nested
signed/common paths have movement bounded by

\[
 2M_qR+\tfrac23M_kR^{3/2}<.000527082725,
 \quad S-S_1-\text{movement}>.000172917275.
\]

Therefore both exact signed characteristic densities
\(F_\sigma=kT_{\sigma,\theta}\) and the full deflated coordinate
\(\Delta\) exist on the \((R,S_1)\) bidisk. Their exact equations give

\[
 F_\sigma=\exp I_\sigma,\quad |I_\sigma|\le M_CR,
 \quad |\Delta-1|\le e:=e^{M_CR}-1<.028750705256.             \tag{V.6}
\]

The individual signed quantities live naturally on the \(s\)-disk,
\(s^2=\rho\). Their product and \(\Delta\) are even and holomorphic in
\(\rho\). Neither product denominator vanishes.

## 3. Exact density and height invariance give a second-order quotient

Let \(\Psi=(\xi,\phi)\) be the actual negative canonical chart, so
\(\xi=\rho\Delta^{2/3}\) and

\[
 J_\Psi=\sqrt{\rho/\xi}\,F_+F_-/k.
\]

R46 (7.2) proves that the coordinate change sends
\(\mathcal F/\mu\) to \((\mathcal F/\mu)/J_\Psi\). A real positive height
conjugation multiplies both \(\mathcal F\) and \(\mu\) by the same square,
so their ratio is unchanged. In the final canonical height,
\(\mu_c=\sqrt\xi\) and \(\mathcal F_c=V+5/(16\xi^2)\). Hence

\[
 V\circ\Psi
 =\frac{N(\rho,\theta)}{\rho^2\Delta^{4/3}},\qquad
 \boxed{N=(H+5/16)\frac{\Delta^2}{F_+F_-}-5/16.}             \tag{V.7}
\]

This derivation retains both the density Jacobian and the final height. There
is no additional unaccounted height factor in (V.7).

The previously completed true local canonical chart has a holomorphic
potential at \(\rho=0\). Its exact identity (V.7) therefore implies
\(N(0,\theta)=N_\rho(0,\theta)=0\), for every real parameter and every angle
of the common strip. All terms in (V.7) are holomorphic on the larger bidisk,
so the same analytic function continues there. Consequently \(N/\rho^2\)
is a removable holomorphic quotient on that entire bidisk. The root
cancellation is exact, not an interval subtraction of two large root values.

From (V.6),

\[
 \left|\frac{\Delta^2}{F_+F_-}\right|\le e^{4M_CR},
 \quad
 \left|\frac{\Delta^2}{F_+F_-}-1\right|
       \le2(e^{2M_CR}-1)e^{2M_CR}.
\]

The second inequality bounds separately
\(\Delta^2-1\) and \(F_+F_--1\), then uses the complete inverse product.
Thus

\[
 M_N=M_He^{4M_CR}
       +\tfrac58(e^{2M_CR}-1)e^{2M_CR}<.056364213478.
\]

On the outer \(\rho\)-circle, the quotient has modulus at most \(M_N/R^2\).
The maximum principle extends this to every \(\rho\), including zero.
Since \(|\Delta|\ge1-e\),

\[
 \boxed{|V\circ\Psi|\le
  \frac{M_N}{R^2(1-e)^{4/3}}<752813.541687.}                \tag{V.8}
\]

This is a complete potential bound on the full complex physical bidisk. It
remains to prove an actual product domain in the canonical variables before
using it for their Fourier norms.

## 4. A complete fixed-canonical-angle domain through the entire collar

Restrict physical complex angles to \(|\Im\theta|\le S_1/2\).
Cauchy on the full \(S_1\) strip gives
\(|\Delta_\theta|\le2e/S_1\). The exact coordinate identities give

\[
 \begin{split}
 |\phi_\theta|&\ge 2U_{0,-}(1-e)=:P_\theta,\\
 |J_\Psi|&\ge2U_{0,-}e^{-7M_CR/3}=:J_-,\\
 |\xi_\theta|&\le
 X_\theta:=\tfrac23R(1-e)^{-1/3}(2e/S_1),\\
 |\phi_\rho|&\le
 P_\rho:=2M_qM_{U_0}e^{M_CR}+\sqrt R\,e .
 \end{split}                                                  \tag{V.9}
\]

The inverse differential has the complete bounds

\[
 \begin{split}
 |\rho_\phi|&\le X_\theta/J_-,\qquad
 |\theta_\phi|\le[1+(X_\theta/J_-)P_\rho]/P_\theta,\\
 |\rho_\xi|&\le e^{4M_CR/3},\qquad
 |\theta_\xi|\le P_\rho/J_- .
 \end{split}                                                  \tag{V.10}
\]

For the third bound use the exact simplification
\(\rho_\xi=\Delta^{1/3}(F_+^{-1}+F_-^{-1})/2\); this avoids a
poor independent numerator/denominator estimate.

The directed consumer gives, respectively,

\[
 |\rho_\phi|<.146492885,\quad |\theta_\phi|<20.336569168,
 \quad |\rho_\xi|<1.038516804,\quad |\theta_\xi|<5.158920726.
                                                               \tag{V.11}
\]

For real \(0\le\xi\le L=1/4000\), the complete real inverse starts at
\(\rho\le Le^{2M_CR/3}<.000254769112\). Lift a complex canonical angle
segment of length at most \(\sigma=1/40000\), followed by a complex radial
segment of length at most \(\varepsilon=1/100000\). The total physical
movements from (V.11) are bounded by

\[
 |\Delta\rho|<.000014047491,\qquad
 |\Delta\theta|<.000560003437.
\]

The remaining strict margins are

\[
 R-\rho_{\max}-|\Delta\rho|>1.018339826\,10^{-5},
 \qquad S_1/2-|\Delta\theta|>.000189996563.                  \tag{V.12}
\]

Analytic continuation by the inverse differential therefore never reaches a
singularity or the boundary of its paid physical domain. The identities
\(D\Psi\,D\Psi^{-1}=I\) show that these lifts are local inverse maps.
They agree on overlapping neighborhoods by continuation from the unique real
inverse. The inverse differential is integrable, as the inverse of the
Jacobian of the same holomorphic map, so the local neighborhoods patch to the
product domain (V.2), with its correct periodic lift. This proves a full
fixed-\(\xi\) canonical angle strip, rather than using a moving physical
angle domain as though it were fixed.

The earlier actual physical graph satisfies
\(\chi_p(\phi)<.000248188363<L\), so it is contained in this domain.
Equation (V.8) now holds on the full canonical product, proving (V.1).
At each real radial center \(\xi\in[0,L]\), its radius-\(10^{-5}\)
complex radial disk lies in the paid halo. Cauchy therefore gives
\(|V_\xi|\le752813.541687/10^{-5}\) on that real radial segment and
the same full complex angle strip. It does not give this derivative bound
at the boundary of the radial halo.

## 5. Exact shifted-Airy height propagation and the mean

Write \(W=V-5050\). On (V.2),

\[
 |W|<757863.541687=:M_W.
\]

This is the entire actual residual, including its mean, nonmean part and all
radial dependence. The reference equation at frequency
\(\lambda=q_c|n|\), \(n\ne0\), is

\[
 y''+(\lambda^2\xi+5050)y=0.
\]

With \(a=\lambda^{2/3}\), the exact Airy argument is
\(z=-a\xi-5050/a^2\). It lies on the negative real axis throughout the
negative collar. The complete Green kernel with initial data
\(G(s,s)=0,G_\xi(s,s)=1\) is

\[
 G(\xi,s)=\frac\pi a\left[
 \operatorname{Ai}(z(\xi))\operatorname{Bi}(z(s))
 -\operatorname{Bi}(z(\xi))\operatorname{Ai}(z(s))\right].   \tag{V.13}
\]

For the mean it is
\(\sin(\sqrt{5050}(\xi-s))/\sqrt{5050}\). No inverse nonzero frequency is
applied to that mode.

For every frequency and \(\xi\ge s\),

\[
 |G(\xi,s)|\le\xi-s.                                      \tag{V.14}
\]

Here is a direct proof. For a real solution of \(y''+Q(\xi)y=0\), where
\(Q=5050+\lambda^2\xi>0\) is nondecreasing, the Sonin energy
\(y^2+(y')^2/Q\) is nonincreasing. Before the first maximum of the solution
with data \((0,1)\), positivity and concavity give \(0\le y\le\xi-s\).
If that maximum occurs, the nonincreasing Sonin energy bounds every later
absolute value by that first maximum, which is already below \(\xi-s\).
This proves (V.14), including the constant mean equation. The cosine-type
solution with initial data \((1,0)\) has modulus at most one by the same
energy. Antisymmetry gives the absolute Green bound in the reverse direction.

Since the complete Green operator is Fourier diagonal, (V.14) is its full
\(L^2\) operator bound. Multiplication by the true \(W\) has norm at most
\(M_W\). Thus on \(C([0,L];L^2)\),

\[
 \left\|u\mapsto\int_0^\xi G(\xi,s)W(s)u(s)\,ds\right\|
 \le\frac12 L^2M_W
 <.023683235678<1/40.                                      \tag{V.15}
\]

Picard iteration gives the unique full mild height solution and its ordinary
height-source resolvent. This uses every angular mode and every parameter;
it is not a diagonal approximation to multiplication by \(W\). In
particular, for ordinary \(f\in L^1_\xi L^2\) and initial height and momentum
in \(L^2\),

\[
 \sup_\xi\|u(\xi)\|_2
 \le\frac{\|u(0)\|_2+L\|u_\xi(0)\|_2
                    +L\|f\|_{L^1L^2}}{1-\tfrac12L^2M_W}.
\]

The height estimate alone does not give the natural full Airy Cauchy norm.
Its higher Sobolev commutators, both full momentum rows, exact root-frame
change and ordinary-source conversion must be retained in the next consumer.
In particular the original R43 first phase \(B\) and the full returned
\(b,\beta\) have not been redefined by choosing this reference.

## 6. Executed files and precise remaining scope

The complete density producer/report pair is

- `scripts/fourfold_negative_root_complete_potential_density.py`;
- `notes/2026-11-13-negative-root-complete-potential-density.json`.

The report SHA256 is

    0325b869504dff6cf1d29937b05ac67ddb5130183080db292e41e8f1a45f3923

The complete canonical-domain consumer/report pair is

- `scripts/fourfold_negative_root_full_canonical_domain.py`;
- `notes/2026-11-13-negative-root-full-canonical-domain.json`.

Its report SHA256 is

    e511da0be8da1f489769ed65a948438b6aab6bd059b442b7195a303ec4b42d8e

Reproduction from the topic directory, with fresh output paths:

~~~bash
python3 scripts/fourfold_negative_root_complete_potential_density.py \
  --out notes/2026-11-13-negative-root-complete-potential-density.json
python3 scripts/fourfold_negative_root_full_canonical_domain.py \
  --out notes/2026-11-13-negative-root-full-canonical-domain.json
~~~

All saved reports contain their input and dependency hashes, exact domains,
complete error budgets and strict gates. No large new intermediate data are
needed. The full canonical potential domain and height contraction now reach
past the actual strict physical cut. Full Sobolev/frame/source propagation to
that nonconstant graph, positive Ai/contact and the final returned inverse
remain separate tasks; none follows from (V.15) without its additional proof.
