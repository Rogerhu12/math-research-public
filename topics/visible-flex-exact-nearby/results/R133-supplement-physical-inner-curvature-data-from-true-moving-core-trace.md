# R133 supplement: physical inner-curvature data from a true moving core trace

2026-11-15, visible-exact / tail_connector.

**Status: proved finite-Sobolev conversion on the stated trace domain.** This paper gives a direct, finite-Sobolev conversion at the actual section L=9/10. The conversion includes the complete moving even mean and the normalized angular map. It supplies explicit sufficient conditions for the physical input domain used by the continuous exact-tail selection. It does not assert that the existing moving L2 cut certificate has already verified those conditions.

Use the same continuous 440866 repaired M32 centre, physical intrinsic coefficients and normalized reflection sector as in:

- [C: the continuous physical centre and residual conjugation](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md), C.1--C.9;
- [P: the full-frequency moving boundary and Poisson interface](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md), P.1--P.8;
- [M: the two-input zero-width cap and complete inner outputs](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md);
- [L: the finite real-angle interpolation estimate](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md), L.18;
- [S: the exact far chart and body iteration](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md), S.42--S.46;
- [Ct: the continuous exact-tail selection](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md).

All angular frequencies below are the physical signed set 4Z. L2 integrals on either circle are normalized. For an integer q, Hq uses the multiplier Lambda_m=(1+m^2)^(1/2). Fourier means in the two coordinates are written explicitly.

## 1. The exact value map and its two means

At L, let the true moving trace be Q=(u,v), with u odd, v even and m=<v>_phi nonzero. Define
$$
 j=v/m,\qquad
 \Theta(\phi)=\phi+I_\phi(j-1),\qquad
 \Theta_\phi=j>0,\qquad \phi=\Theta^{-1}.
 \tag{V.1}
$$
The inverse is a real circle diffeomorphism. Its lift is fixed by reflection: both Theta and phi are odd. No independent angular constant is reset.

The physical curvature trace is
$$
 B=(u/v)\circ\phi,\qquad C=(1/v)\circ\phi.
 \tag{V.2}
$$
Let Q0=(u0,v0) denote the same repaired centre at L, with corresponding m0,j0,Theta0 and physical trace (hat B,hat C). The cap input in M is exactly
$$
       \gamma=P_{\ne0,\theta}(C-\widehat C).
 \tag{V.3}
$$
It is a change relative to the complete physical centre. It is not P_ne C alone, and a moving finite Fourier cutoff is not a physical cutoff.

Changing variables with dtheta=j dphi gives the exact means
$$
 \langle C\rangle_\theta=1/m,\qquad
 \langle B\rangle_\theta=\langle u\rangle_\phi/m .
 \tag{V.4}
$$
Consequently the actual C-mean change is
$$
 \langle C-\widehat C\rangle_\theta
            =-\frac{\langle v-v0\rangle_\phi}{m\,m0}.
 \tag{V.5}
$$
The moving even mean in this formula is retained. B has zero mean in the present reflection sector because u is odd. In the full ambient class the second formula in (V.4) is an independent mean row; it is not removed by (V.3).

## 2. Paid centre bounds and a real low neighbourhood

The complete C table, valid at every point of the cap and hence at L, gives
$$
 \begin{gathered}
 3.1914104290<|m0|<5.8639401366,\qquad
 \|j0-1\|_{A_{1/32}}<.015211829<1/64,\\
 \|(j0)_\phi\|_{A_{1/32}}<.061779810,\qquad
 \|v0\|_{A_{1/64}}<5.953141388<6,\\
 \|\widehat C_\theta\|_{A_{1/64}}<.020269146 .
 \end{gathered}
 \tag{V.6}
$$
Here A_sigma is the Fourier norm sum exp(sigma|m|)|f_m|. These are the original full signed coefficient bounds, not sampled angles.

In particular,
$$
 |v0|>25/8,\quad
 |(v0)_\phi|<1/2,\quad
 |\widehat C_\theta|<1/32,\quad
 |\widehat C_{\theta\theta}|<1/2 .
 \tag{V.7}
$$
The last inequality uses the already paid positive width:
sup_{x>=0} x exp(-x/64)=64/e<24, and
24*.020269146<1/2. Thus no derivative of an unknown datum is estimated by complex Cauchy.

Write h=v-v0. Suppose first that
$$
                         \|h\|_{H^1_\phi}\le2^{-10}.
 \tag{V.8}
$$
The complete-circle inequalities
$$
 \|I_\phi f\|_\infty
 \le \frac{\pi}{4\sqrt3}\|P_{\ne0}f\|_2<\tfrac12\|f\|_2,
 \qquad
 \|h\|_\infty<2\|h\|_{H^1}
 \tag{V.9}
$$
include both signs. They give
$$
 |m|\ge3,\qquad |v|\ge3,\qquad |v|\le7,\qquad
 \|j-1\|_\infty<1/8,\qquad 7/8<j<9/8 .
 \tag{V.10}
$$
Indeed, the exact normalized difference is
$$
 \delta j:=j-j0
    =\frac{h-j0\langle h\rangle_\phi}{m},
 \qquad
 \Theta-\Theta0=I_\phi\delta j .
 \tag{V.11}
$$
Using |j0|<33/32 yields
||delta j||2<3||h||2/4 and
||delta j||infinity<2||h||H1. Together with (V.6), these prove (V.10).
The constant part of h is visible in both identities (V.11).

## 3. The actual gamma A0 gate only needs H1 of the moving difference

Pull the physical difference back by the actual angle:
$$
 F(\phi)=\{C-\widehat C\}(\Theta(\phi))
       =\frac1v-\frac1{v0}
            -\{\widehat C(\Theta)-\widehat C(\Theta0)\}.
 \tag{V.12}
$$
This is an exact identity for two real diffeomorphisms. The known function hat C, not an unknown direction, is evaluated at the two real angles.

The first difference has derivative
$$
 \left(\frac1v-\frac1{v0}\right)_\phi
   =-\frac{h_\phi}{v^2}
       +(v0)_\phi\left(\frac1{v0^2}-\frac1{v^2}\right).
$$
Since |v0|<=6 and |v|<=7, (V.7)--(V.10) imply
$$
 \left\|\left(\frac1v-\frac1{v0}\right)_\phi\right\|_2
 \le\frac19\|h_\phi\|_2+\frac1{12}\|h\|_2 .
 \tag{V.13}
$$
The second difference in (V.12) has derivative
$$
 [\widehat C_\theta(\Theta)-\widehat C_\theta(\Theta0)]j
              +\widehat C_\theta(\Theta0)\delta j .
$$
The known second derivative in (V.7), (V.9), and (V.11) therefore give
$$
 \left\|[\widehat C(\Theta)-\widehat C(\Theta0)]_\phi\right\|_2
  \le\left(\frac{27}{128}+\frac3{128}\right)\|h\|_2
  =\frac{15}{64}\|h\|_2 .
 \tag{V.14}
$$
Combining (V.13)--(V.14),
||F_phi||2 <=(61/192)||h||2+(1/9)||h_phi||2
<||h||H1/2.

The real measure is still essential:
$$
 \|\partial_\theta(C-\widehat C)\|_{L^2_\theta}^2
                  =\int |F_\phi|^2j^{-1}\,d\phi
                  \le(8/7)\|F_\phi\|_2^2 .
$$
Using the full signed Fourier estimate in (V.9) once more,
$$
 \boxed{\quad
       \|\gamma\|_{A^0_\theta}
                <\tfrac12\|h\|_{H^1_\phi}.
       \quad}
 \tag{V.15}
$$
The displayed 1/2 is a safe widening. No H2 bound on h was used.
In particular, with r_gamma=10^-9, the explicit sufficient gate
$$
                   \|v-v0\|_{H^1_\phi}\le r_\gamma/128
 \tag{V.16}
$$
places gamma strictly in the required ball
||gamma/r_gamma||A0<=1/128.
It also implies the low geometric neighbourhood (V.8).

## 4. Direct high physical derivatives, with only one high moving norm

This section is a value estimate and does not use an unknown complex inverse angle. From (V.1)--(V.2),
$$
 (\partial_\theta^q C)\circ\Theta
       =m^{-1}\mathcal P_q(j),\qquad
 \mathcal P_q(j)=(j^{-1}\partial_\phi)^q(j^{-1}).
 \tag{V.17}
$$
For q>=1, every monomial in P_q is of the form
$$
 j^{-(q+k+1)}
          \prod_{\alpha=1}^k\partial_\phi^{n_\alpha}j,
 \qquad n_\alpha>=1,\quad
 \sum_{\alpha=1}^k n_\alpha=q,\quad 1<=k<=q .
 \tag{V.18}
$$
Coefficients can have either sign. Let S_q be the sum of their absolute values after a full expansion. Differentiating one such monomial and multiplying by j^-1 costs at most
(q+k+1)+k<=3q+1. Hence
$$
          S_q\le\prod_{a=0}^{q-1}(3a+1)\le3^q q! .
 \tag{V.19}
$$
This count includes the derivatives of every inverse power of j.

Apply L.18 once to each positive derivative of z=j-1, with r=q. The sum of the derivative orders is exactly q. Holder thus has exponent sum 1/2, while the sum of high interpolation powers is exactly 1. Since ||z||infinity<=1/8,
$$
 \left\|\prod_{\alpha=1}^k
             \partial_\phi^{n_\alpha}j\right\|_2
 \le2^{32q}(q+1)^{2q}
       \|z\|_\infty^{k-1}
          (\|\partial_\phi^qz\|_2+\|z\|_\infty)
 \le2^{32q+1}(q+1)^{2q}\|z\|_{H^q}.
 \tag{V.20}
$$
The last step uses the mean-zero circle embedding. This is one high norm, not a product of k high norms. The low bound on z is a hypothesis already proved in (V.10); positivity of j alone would not justify this step.

The denominator in (V.18) is at most 2^(2q+1), and the real change of measure costs less than 2 in norm. For the nonmean part, the exact physical minimum frequency is 4, so
||P_ne C||Hq <=(17/16)^(q/2)||partial_theta^q C||2.
For 1<=q<=8193,
$$
 q!\le((q+1)/2)^q\le2^{13q},\qquad
 (q+1)^{2q}\le2^{28q}.
$$
Combining these bounds with (V.19)--(V.20), and using
||z||Hq=|m|^-1||P_ne v||Hq, gives
$$
 \boxed{\quad
 \|P_{\ne0,\theta}C\|_{H^q_\theta}
       \le2^{78q+16}\|P_{\ne0,\phi}v\|_{H^q_\phi},
       \qquad 1\le q\le8193 .
 \quad}
 \tag{V.21}
$$
The constants were widened only after the complete monomial and signed-mode sums. In particular 78*8193+16=639070<655360, so 2^655360 is a uniform bound in (V.21).

The same estimate applies to the centre. Its joint A_(1/32) bound gives
||P_ne v0||A_(1/32)<6*.015211829<1/10.
By x^q<=q! exp(x),
$$
                    \|P_{\ne0}v0\|_{H^{8193}}
                                        <2^{163840}.
 \tag{V.22}
$$
For example 2^(q+1)32^q q! bounds the Bessel multiplier against the exponential weight, and 19*8193+1<163840.

It follows that
$$
 \|\gamma\|_{H^{8193}_\theta}
 \le2^{655360}
       \{\|v-v0\|_{H^{8193}_\phi}
                              +2\|P_{\ne0}v0\|_{H^{8193}_\phi}\}.
 \tag{V.23}
$$
There is no subtraction of two unrelated upper bounds here: the estimate is the triangle inequality for the exact value difference (V.3).

## 5. A complete sufficient core trace gate for the current tail domain

Suppose the actual moving trace satisfies
$$
 \boxed{\quad
 \|v-v0\|_{H^1_\phi}\le10^{-9}/128,\qquad
 \|v-v0\|_{H^{8193}_\phi}\le2^{393000}.
 \quad}
 \tag{V.24}
$$
Then (V.15) and (V.23) imply, with full physical nonmean even data,
$$
 \|\gamma/r_\gamma\|_{A^0_\theta}\le1/128,\qquad
 \|\gamma/r_\gamma\|_{H^{8193}_\theta}\le2^{1048576}.
 \tag{V.25}
$$
Indeed r_gamma^-1<2^30 and
655360+393001+30=1048391<1048576.
The centre term in (V.23) is strictly smaller than the one extra bit allowed by 393001.

The low gate in (V.24) is a genuine H1 trace gate. Neither the old moving L2 cut bound nor the final-geometry C0 ball alone implies it. The high condition is likewise a genuine bound at the same section. It cannot be inferred by declaring the moving low-97 input to have finite physical Fourier support.

The value map v -> gamma is continuous from this subset of H8193_phi to H8193_theta. One direct proof is as follows. All the finite differential polynomials (V.18) depend continuously in L2_phi on v in H8193, with inverse factors bounded away from zero by (V.10). The real maps Theta and their inverses converge in C1. To compare the resulting L2 functions in one physical coordinate, approximate one fixed L2 function by a smooth function and use the common Jacobian bounds for the remainder. This proves strong L2 convergence of each physical derivative in (V.17), and hence H8193 convergence. This argument neither invokes a same-order inverse theorem for a rough composition operator nor asserts parameter differentiability of the exact tail.

## 6. The actual remaining inner equations

For gamma in (V.25), let
f=mathcal T_far(gamma)
be the deterministic continuous exact-tail output in Ct and S. It is the original normalized nonmean physical height at B. Let
$$
 (B_{\rm cap},C_{\rm cap})
             =\mathcal C(\gamma,f)\big|_{r=L}
 \tag{V.26}
$$
be the actual cap value map M, including its true nonlinear outer graph, its independent C mean and its actual height span. This notation never substitutes the original linear centre for the new cap value.

By definition of the gamma input,
P_ne C_cap=P_ne hat C+gamma.
Consequently the full curvature match at L is exactly the following two remaining equations:
$$
 B_{\rm core}(\theta)=B_{\rm cap}(\theta),\qquad
             1/m_{\rm core}=\langle C_{\rm cap}\rangle_\theta .
 \tag{V.27}
$$
The B equation includes every allowed frequency. In the actual reflection sector its mean is identically zero on both sides. The even C mean in the second equation is an actual scalar equation and is not fixed by gamma.

Equivalently, in the same moving variable,
$$
 u_{\rm core}(\phi)
       =v_{\rm core}(\phi)\,
                B_{\rm cap}(\Theta_{\rm core}(\phi)),\qquad
             1/m_{\rm core}=\langle C_{\rm cap}\rangle_\theta .
 \tag{V.28}
$$
Together with (V.3), these are equivalent to complete physical B,C matching. Once the full C values agree, (V.4) gives the same m, and both inverse-angle derivatives equal m C. Reflection fixes their integration constant. Thus the moving charts also agree; there is no unnoticed reparametrization of the inner boundary.

The scalar height and one initial frame/position are then read and matched by the already proved single-frame construction. They are not replaced by the curvature means in (V.27), and they are not two independently prescribed world anchors. The precise one-initial-value scope is that of T section 9. No body residual or far-boundary residual is removed by these observations.

## 7. A precise conditional closing statement

The following implication states what would suffice from the core, with no differentiability assertion for the tail selection.

Let B_f be the closed ball
$$
 \{f\in H^3_{\ne0,\mathrm{ev}}:
                  \|f\|_{H^3}\le2^{-54864000}\}.
 \tag{V.29}
$$
This is inside the cap's dot-A2 input ball, since
||f||dot-A2 <=2||f||H3<2^-60.
Suppose a continuous core-plus-cap solution graph is actually proved on B_f, with the following properties:

1. It solves the true core equations and all the original regular waist, parameter and full inner equations for that fixed f.
2. Its L trace is continuous in H8193 and satisfies (V.24) uniformly.
3. Its intrinsic data agree with the fixed cap data of M, and the tail design changes remain on their original supports, away from the fixed core/cap coefficients and B scale.

Then define
$$
       \mathcal K(f)
           =\mathcal T_{\rm far}\bigl(\gamma(Q_{\rm core}(f)|_L)\bigr).
 \tag{V.30}
$$
The hypotheses, (V.25), and Ct make this a continuous map on B_f.
Ct's uniform H1859 bound is less than 2^-54865000. Thus its image lies strictly inside B_f and is relatively compact in H3. The usual compact fixed-point theorem on a closed convex Banach ball gives f=mathcal K(f).

At that fixed point the independently constructed true core/cap and true tail have the same actual far height and the complete curvature match (V.27). All intrinsic design parameters are selected once for that member and then frozen. The subsequent geometric family uses the already proved material/ambient circle action, not an intrinsic-nu variation.

This is a conditional theorem: the core graph, its H1 endpoint gate, its actual H8193 endpoint bound, and its remaining full B/Cmean equations are the hypotheses. The new conclusion of this paper is the complete, quantitative conversion (V.24)->(V.25), the continuous physical value readout and the exact reduction (V.27). H1859 compactness of the far output alone proves none of those core hypotheses.
