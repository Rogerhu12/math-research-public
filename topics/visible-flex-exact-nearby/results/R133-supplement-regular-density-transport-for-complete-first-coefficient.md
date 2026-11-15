# R133 supplement: regular density transport for the complete first coefficient

2026-11-15, newton_source.

**Proved analytic identities and complete residual estimates; no new numerical execution is asserted.** This supplements [PF](R133-supplement-pointwise-root-finite-part-and-complete-true-ray-first-coefficient.md), published at commit 6f6bc02d with blob e384f8711a44e1ad16dd05804faf65d62bf016c2 and SHA256 5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026. It turns the complete function finite part into two regular Cauchy targets in the original physical moving angle. The actual rays, scalar finite part and selected-angle KAM certificate are reused.

The same exact repaired family is
$$
 Q_\delta=\overline Q+\delta Z,\qquad \nu_\delta=\nu_0+\delta,\qquad
 \eta_{\rm design}=\eta_0 .
 \tag{CT.1}
$$
Its candidate, repaired centre and full direction have SHA256
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413,
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47 and
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The formulas hold on the previously proved real parameter domain. A minimal consumer may restrict to $|\delta|\le10^{-10}$, which contains the selected parameter. The true radial root is independent of this compact metric parameter. Its accepted enclosure is reused without a new root search.

## 1. Complete branch coefficient in physical coordinates

Use period $\pi/2$, physical frequencies $4j$, normalized angular measure and
$$
 \rho=r_*-r,\quad q=\sqrt{\rho k(\rho)},\quad
 \eta=-\gamma\langle v\rangle>0,\quad
 c_\sigma=d+\sigma\eta q,\quad \sigma\in\{+1,-1\}.
 \tag{CT.2}
$$
Here $b=a_{\rm phys}'/a_{\rm phys}$ and $d=-bI(u^2+Kv^2)$ have exactly the original strict-symbol convention. The full mean of $v$ remains in $\eta$. The symbol $b$ is not the scalar return phase.

Let $H_\sigma$ solve PF.17, put $\Phi_\sigma=H_\sigma^{-1}$ and $J_\sigma=H_\sigma'$, and use
$$
                         U_\psi f=\psi'(f\circ\psi).
 \tag{CT.3}
$$
The complete first root-input coefficient has the individual equation
$$
 \partial_\rho C_\sigma=-J_\sigma(a_\sigma\circ H_\sigma).
 \tag{CT.4}
$$
It contains the full S.12 coefficient, not only its mean or its radial product term. Defining $f_\sigma=U_{\Phi_\sigma}C_\sigma$ gives
$$
 \boxed{\quad
 \partial_\rho f_\sigma+\partial_\phi(c_\sigma f_\sigma)=-a_\sigma .
 \quad} \tag{CT.5}
$$
Indeed $(J_\sigma\circ\Phi_\sigma)\Phi_\sigma'=1$, so the source is exactly $-a_\sigma$.

PF proves the same finite term $F_*(x)=-\ell_*(x)/(2\eta_*)$ in the two root-input branches. Set
$$
 \widetilde C_\sigma=C_\sigma-F_*,
 \qquad \widetilde f_\sigma=f_\sigma-U_{\Phi_\sigma}F_* .
 \tag{CT.6}
$$
The subtracted term is a genuine homogeneous solution of CT.5. The source is unchanged and $\widetilde C_--\widetilde C_+=C_--C_+$. The two physical-angle functions $U_{\Phi_-}F_*$ and $U_{\Phi_+}F_*$ are generally different; they are not cancelled before their actual ordered pullbacks.

## 2. Physical counterterm and regular remainder

Retain the full PF function $g_1^{\rm pt}$ and define
$$
 \chi(\phi)=g_1^{\rm pt}(\phi)+\frac{2g_0}{3}(d_*)_\phi(\phi),\qquad
 S_\sigma(\rho,\phi)=\sigma\left\{
       \frac{g_0}{3\rho^{3/2}}+\frac{\chi(\phi)}{\sqrt\rho}\right\}.
 \tag{CT.7}
$$
Multiplication by the physical density
$\Phi_\sigma'=1-\rho(d_*)_\phi+O(\rho^2)$ changes the root-label $\rho^{-1/2}$ coefficient by $-g_0(d_*)_\phi/3$. Thus
$$
 \chi=\widehat g_1-\frac{g_0}{3}(d_*)_\phi,\qquad
 u_\sigma:=\widetilde f_\sigma-S_\sigma
                            =O_{H^s}(\sqrt\rho).
 \tag{CT.8}
$$
The limit of $u_\sigma$ at the root is zero as a function, using PF's pointwise theorem. Its exact equation is
$$
 \partial_\rho u_\sigma+\partial_\phi(c_\sigma u_\sigma)=R_\sigma,
 \qquad R_\sigma=-a_\sigma-\partial_\rho S_\sigma
                              -\partial_\phi(c_\sigma S_\sigma).
 \tag{CT.9}
$$
The following formula evaluates the complete integrable source before taking any norm.

## 3. Eight regular source terms

Put
$$
 \begin{split}
 a_{\rm e}&=-d_{\phi\phi}-b(u_\phi u-\rho k v_\phi v),\\
 a_{\rm r}&=\frac{k_\rho}{4k}-b(1+u^2+\rho kv^2),\\
 A&=(16\eta\sqrt{k})^{-1},&
 B&=\frac{a_{\rm r}}{2\eta\sqrt{k}},\\
 C&=\frac{a_{\rm r}^2}{\eta\sqrt{k}},&
 D&=\frac{4b^2\sqrt{k}\,u^2v^2}{\eta}
                           +2b\sqrt{k}(u v_\phi-vu_\phi).
 \end{split}
 \tag{CT.10}
$$
Only $A$ is radial. The other three are complete angular functions. S.12--S.16 give
$$
 a_\sigma=a_{\rm e}+\frac{\sigma}{2}\Xi,\qquad
 \Xi=\rho^{-5/2}A+\rho^{-3/2}B+\rho^{-1/2}C-\rho^{1/2}D,
 \quad A(0)=g_0,\quad A_\rho(0)+B(0)=g_1^{\rm pt}.
 \tag{CT.11}
$$
On the original common root germ use the analytic divided differences
$$
 \begin{split}
 A_2&=\int_0^1(1-t)A_{\rho\rho}(t\rho)\,dt
                 =\frac{A(\rho)-A(0)-\rho A_\rho(0)}{\rho^2},\\
 B_1&=\int_0^1B_\rho(t\rho,\phi)\,dt
                 =\frac{B(\rho,\phi)-B(0,\phi)}{\rho},\\
 d_1&=\int_0^1d_{\phi\rho}(t\rho,\phi)\,dt
                 =\frac{d_\phi(\rho,\phi)-(d_*)_\phi(\phi)}{\rho}.
 \end{split}
 \tag{CT.12}
$$
The integral definitions include $\rho=0$ and authorize signed Taylor polynomials with complete integral remainders. They do not authorize subtraction of interval upper bounds. Away from zero the algebraic quotients remain exact; they require no analytic extension across a radial join.

Set $s=\sqrt\rho$ and $U_\sigma(s,\phi)=u_\sigma(s^2,\phi)$. The new regular target is
$$
 \boxed{\quad
 \partial_s U_\sigma+
 2s\,\partial_\phi\!\left[
   \big(d(s^2,\phi)+\sigma\eta(s^2)s\sqrt{k(s^2)}\big)U_\sigma
                  \right]=G_\sigma(s,\phi),\qquad U_\sigma(0)=0 .
 \quad} \tag{CT.13}
$$
Its complete right side is
$$
 \boxed{\begin{split}
 G_\sigma={}&-\sigma A_2-\sigma B_1
       -\frac{2\sigma g_0}{3}d_1-\sigma C+\sigma s^2D\\
 &-2\sigma\partial_\phi(d\chi)
       -2s\,a_{\rm e}-2s\,\eta\sqrt{k}\,\chi_\phi .
 \end{split}} \tag{CT.14}
$$
All fields on the right are evaluated at $\rho=s^2$. In particular the last term is the radial optical speed acting on the nonconstant counterterm, and the $d_1$ term retains the actual density correction.

To verify every cancellation,
$$
 \partial_\rho S_\sigma
       =-\frac{\sigma g_0}{2\rho^{5/2}}
                          -\frac{\sigma\chi}{2\rho^{3/2}},\qquad
 \partial_\phi(c_\sigma S_\sigma)
       =\frac{\sigma g_0d_\phi}{3\rho^{3/2}}
        +\frac{\sigma\partial_\phi(d\chi)}{\sqrt\rho}
        +\eta\sqrt{k}\,\chi_\phi .
 \tag{CT.15}
$$
Substitute CT.11 and
$A=g_0+\rho A_\rho(0)+\rho^2A_2$,
$B=B(0)+\rho B_1$,
$d_\phi=(d_*)_\phi+\rho d_1$.
The $\rho^{-5/2}$ terms cancel. CT.7 cancels the remaining nonintegrable $\rho^{-3/2}$ coefficient. Multiplication by $2s$ gives CT.14 with all eight signs.

The source is analytic in $s$ on the common root germ and piecewise regular afterwards. Its root values are
$A_2(0)=A_{\rho\rho}(0)/2$, $B_1(0)=B_\rho(0)$ and
$d_1(0)=d_{\phi\rho}(0)$. Evaluating a singular quotient at a zero-containing numerical ball is not an alternative validation.

## 4. Complete Fourier support, means and interfaces

Both physical state components of CT.1 have degree at most 96, including their means. Hence $d,\chi$ have degree at most 192, and CT.14 has degree at most 384. These support assertions concern known coefficient functions; the solution $U_\sigma$ has no imposed Fourier cutoff.

For a newly constructed reference $\widehat U_\sigma$ of degree $N$, the complete residual is
$$
 {\cal E}_\sigma=
 \partial_s\widehat U_\sigma+
          2s\partial_\phi(c_\sigma\widehat U_\sigma)-G_\sigma .
 \tag{CT.16}
$$
Its full angular support is at most $\max(N+192,384)$. Both signs, all these labels and label zero must be included. A projected finite evolution may choose the reference; every mode discarded by it remains in CT.16.

The exact mean equation is
$$
                \partial_s\langle U_\sigma\rangle
                                   =\langle G_\sigma\rangle .
 \tag{CT.17}
$$
There is no mean flux from a periodic divergence. The accepted $\mu=\mathfrak X(\delta_*)$ is read from its original scalar certificate; no old scalar target or quadrature is called to compute it again. Every mean carried by the new density target is retained in its complete residual.

The repaired state and strict first frame are continuous at the original joins, as proved in PF.26 and S.9--S.12. Any value jump of a piecewise reference is charged as an actual validation impulse. Background radial derivative jumps remain in the complete higher-order remainder; they do not create a missing order-minus-one source here.

A consumer may use $s$ on the root collar and original $r$ on the remaining closed pieces. The identity $G_\sigma\,ds=R_\sigma\,d\rho$ preserves the ordinary source measure. The exact old root enclosure and complete root-to-cut interval must be used, not a decimal root or a shorter unproved collar.

## 5. Terminal recovery without computing new rays

At $\rho=r_*$ recover
$$
 \widetilde f_\sigma=
 S_\sigma(r_*,\cdot)+U_\sigma(\sqrt{r_*},\cdot).
 \tag{CT.18}
$$
PF gives $\Phi_+=X_-$, $\Phi_-=X_+$ and $P=S_-\circ X_+$. Since $U_aU_b=U_{b\circ a}$,
$$
 \boxed{\quad c_0=U_{P^{-1}}\widetilde f_--\widetilde f_+ .\quad}
 \tag{CT.19}
$$
In fact $U_{P^{-1}}=U_{X_-}U_{X_+}^{-1}$, so this is exactly
$U_{X_-}(\widetilde C_--\widetilde C_+)$. The common $F_*$ cancels after this ordered operation, not before.

At the selected parameter let the already proved physical angle satisfy
$\mathcal H\circ P=R_{\Omega_{15}}\circ\mathcal H$. Then
$$
 \boxed{\quad
 c=U_{\mathcal H^{-1}}c_0
  =U_{R_{\Omega_{15}}^{-1}}U_{\mathcal H^{-1}}\widetilde f_-
                         -U_{\mathcal H^{-1}}\widetilde f_+ .
 \quad} \tag{CT.20}
$$
A norm can therefore use the existing $\mathcal H$ certificate and the isometric real rotation without constructing new rays or a new conjugacy. Every density map preserves the integral, and $\langle c\rangle=\langle c_0\rangle=\mu$. The AC input remains $c_0-\mu\mathcal H'$, not $c_0-\mu$.

## 6. Complete residual propagation with the accepted Wiener budgets

Write $\|f\|_{A_a}=\sum_j|f_j|e^{4|j|a}$ and read the accepted uniform real-family numbers
$$
 {\cal B}\ge\int_0^{r_*}\|d(r)\|_{A_{1/16}}\,dr,\qquad
 {\cal L}\ge\int_0^{r_*}\|d_\phi(r)\|_{A_{1/16}}\,dr .
 \tag{CT.21}
$$
The exact old fields are `complete_real_parameter_one_leg_drift` and
`complete_real_parameter_one_leg_Lipschitz` of the accepted R31 native, SHA256
d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61.
The producer `scripts/fourfold_codazzi_phase_explicit_family_R31.py` has 14666 bytes and SHA256
df58ef8806461a03870e413e6a8d564947c3cd20a6074127a14a8d4bae5d0163.
See the original [uniform input theorem](R133-supplement-complete-explicit-family-circle-KAM-inputs-and-gates.md) and [actual R31 result](R133-supplement-actual-explicit-family-circle-conjugacy.md).

The accepted true flow-margin gate in that producer is
$$
 \frac1{16}-\frac1{32}-U_{\rm inv}-2{\cal B}>0,\qquad U_{\rm inv}\ge0 .
 \tag{CT.22}
$$
It directly implies $\mathcal B<1/64$, with no new numerical estimate.

For real $a$ the original Wiener composition lemma gives
$$
 \|f(\phi+a+v(\phi))\|_{A_\alpha}
                    \le\|f\|_{A_{\alpha+\|v\|_{A_\alpha}}}.
 \tag{CT.23}
$$
Every allowed partial true path has periodic displacement at most $\mathcal B$ and density Jacobian at most $e^{\cal L}$, by the already proved complete-flow theorem. Thus, whenever $a+{\cal B}<1/16$, the full Duhamel error satisfies
$$
 \begin{split}
 \|U_\sigma(\sqrt{r_*})-\widehat U_\sigma(\sqrt{r_*})\|_{A_a}
 \le e^{\cal L}\bigg\{&
 \|\widehat U_\sigma(0)\|_{A_{a+{\cal B}}}
 +\int_0^{\sqrt{r_*}}\|{\cal E}_\sigma(s)\|_{A_{a+{\cal B}}}\,ds\\
 &+\sum_\alpha\|[\widehat U_\sigma]_\alpha\|_{A_{a+{\cal B}}}\bigg\}.
 \end{split}
 \tag{CT.24}
$$
Each source is complete, with the same actual radial measure and any true initial/reference error. This is a density Duhamel estimate, not a bound on the finite projected evolution alone.

For CT.19 the minus error crosses the additional two-leg map $P^{-1}$. It is sufficient to choose
$$
 a_0=\frac1{128},\qquad a_{\rm load}=\frac7{128},\qquad
 a_0+3{\cal B}<a_{\rm load}<\frac1{16}.
 \tag{CT.25}
$$
The minus and plus errors in $c_0$ are bounded respectively by $e^{3{\cal L}}$ and $e^{\cal L}$ times their CT.24 brackets, both bounded on $A_{a_{\rm load}}$. The terminal references and the explicit counterterms must separately be evaluated on the corresponding enlarged widths. All source compositions stay within the same original field domain.

Only real parameters are asserted here. Their radial optical speed is a real translation and costs no width. A complex parameter path would add its imaginary optical displacement to every relevant domain budget.

The smallest new complete validation may take $\widehat U_\sigma=0$, giving a full source-integral bound for CT.14. A sharper one constructs a new signed symbol reference and bounds CT.16. Both concern this new coefficient target; neither calls an accepted old ray solver.

A complete analytic error bound $E_a$ gives, in the exact physical Sobolev convention,
$$
 \|e\|_{H^3}^2=\sum_j(1+16j^2)^3|e_j|^2,\qquad
 \|e\|_{H^3}\le
 \left(1+\frac3a+\frac6{a^2}+\frac6{a^3}\right)E_a.
 \tag{CT.26}
$$
Indeed $(1+n^2)^{3/2}\le(1+n)^3$ for $n=4|j|$, and
$n^ke^{-an}\le k!/a^k$. The estimate includes the full signed sum and the mean.

## 7. Minimal old-input and new-output contract

| Accepted input | Complete content needed | New use |
|---|---|---|
| Repaired candidate and full direction | All physical Fourier coefficients, radial polynomial pieces, exact continuity offsets and means | Form the known $u_\delta,v_\delta,d_\delta$ and required derivatives |
| Original scalar cover and compact metric cache | Common closed cells, full intrinsic jets and the actual parameter formula | Form $\eta,k,b$ on the complete negative interval |
| Original joint root germ | Fixed true-root enclosure, common radius, positive $k,\eta$ gaps and saved intrinsic jets | Validate CT.12 without root refinement or singular division |
| Existing R31 native | Uniform real $\mathcal B,\mathcal L$ and accepted true domain margin | CT.24--CT.25 |
| Exact-angle certificate | $\mathcal H$, or its finite approximation with the proved full error and domains | CT.20 or AC, including the density Jacobian |
| Existing scalar first-phase conclusion | Complete $\mu$ and its selected-parameter scope | Mean identity and the final nonmean normalizer input |

The old centre finite-part source
`scripts/fourfold_codazzi_current_first_symbol_finite_part.py`,
blob 7557adbbeb8f843597b46ed81c5047733e8acf21,
retains scalar moments in `angular_moments` and bounds $\langle\Xi\rangle$ in its old quadrature. Those scalar outputs cannot supply the angular functions in CT.10 or CT.14.

The original same-family transfer source
`scripts/fourfold_codazzi_first_symbol_parameter_transfer.py`,
blob 4393d55b6ee8152e6d1551d6343e62749969bf79,
pins the same scalar cover, compact metric, complete direction and root germ. Existing values may be restored inside the public runner. The new consumer does not call their generators, root refinement, scalar quadrature, ray integration, KAM iteration or earlier accepted genuine-source producer.

At the root CT.12 needs $A_{\rho\rho}$, $B_\rho$ and $d_{\phi\rho}$ on the complete common germ. They are explicit algebraic combinations of saved intrinsic jets and exact candidate/direction polynomials. Every extra derivative used for a new Taylor reference must be checked against the stored germ order and radius; a saved scalar moment does not provide a missing nonmean derivative.

For a complete known finite field of degree $J$, widening a saved $A_s$ bound to $A_t$ costs $e^{4J(t-s)}$. This is a declared consumption of that same finite known field. It does not make the unknown solution Fourier finite. The complete residual controls the solution tail.

The only new arithmetic is the complete regular source, any new signed symbol reference, its entire residual and the terminal coefficient/error bounds. Old accepted numerical conclusions are restored by exact identities, not rerun. Temporary polynomials and row arrays stay outside Git and are not published as native data or artifacts.

A public small conclusion must report the exact family, positive root and mean gaps, common angular/radial domains, all initial/source/interface errors, both complete branches and all means, the true terminal density convention, and whether a full nonmean $H^3$ bound has actually been obtained. It must separate that new bound from the next strong-return gate.

## 8. Separate quantitative strong-return requirements

This theorem supplies a complete concrete function target for $c_0$. It does not supply the norm of $R_{4/3}$ in PF.28.

That next norm still needs the same actual incoming branch inverse, the complete two-gain strict remainders and their source/mean/interface maps, and the genuine root/positive trial's ordinary source, cutoff jumps and finite-head inputs. The accepted positive seven-port graph and its composed waist map can consume those inputs; they do not assign zero to an unmeasured column or invert the coupled unknown high boundary problem.

The accepted negative root-piece genuine-source bound followed by negative Cauchy and strict propagation is one typed volume contribution. It is not the whole strong return, and it does not bound missing positive trial or incoming columns. A large upper bound leaves a sufficient gate unproved; it is not an impossibility argument.

No actual value of $\|c-\mu\|_{H^3}$, no strong remainder constant, no full high inverse and no global nonlinear solution is asserted here. These require separate complete public conclusions in the declared order.
