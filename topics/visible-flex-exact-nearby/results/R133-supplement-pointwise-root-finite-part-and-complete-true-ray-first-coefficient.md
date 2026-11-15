# R133 supplement: the pointwise root finite part and the complete first coefficient through the true rays

2026-11-15, newton_source, independently reviewed by root and phase_inverse. **Proved.** No new numerical computation is used or reported.

This note strengthens the scalar root statement in the selected-family theorem only after reconstructing the two complete branch coefficients at every fixed strict cut. In the original strict-density convention, the finite root constant is zero as a function of the true root label. The function multiplying the second singular power differs from the scalar counterterm: it includes the derivative of the actual root flow. The result gives an exact convergent expression for the complete first coefficient before the true principal conjugacy.

No numerical norm of that function, no numerical strong remainder, no cutoff-97 inverse, and no full core inverse follows from this note. The original two independent means, finite complement, sources, jumps, incoming inverse, and physical readouts remain in their existing contracts.

## 1. Fixed object and primary inputs

Fix one real member of the continuously repaired explicit family
$Q_\delta=\overline Q+\delta Z$, $\nu_\delta=\nu_0+\delta$, at intrinsic $\eta_0$, in the original interval $|\delta|\le10^{-8}$. In particular this includes the member paired with the actual strip-$1/128$ principal conjugacy. The root does not move under the compact intrinsic perturbation. Write
$$
 \rho=r_*-r,\qquad q=\sqrt{-K}=\sqrt{\rho k(\rho)},\qquad
 \eta=-\gamma\langle v\rangle>0,\qquad b=\beta_{\rm metric},
 \qquad I=\partial_\phi^{-1}(1-\Pi).
 \tag{PF.1}
$$
All circles have normalized measure and period $\pi/2$; physical frequencies are $4j$. Means in the original equations are never replaced by a root-label mean without its actual Jacobian.

The following original results are used with their complete scopes.

| Primary text | Immutable Git blob | SHA256 |
|---|---|---|
| Moving root parametrix, P.1–P.37 | 11250cbb5f9921fdaa70791b6095c306e16bc5d7 | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |
| Selected-family root finite coefficient, B.1–B.13 | e561b822673bbce15c1391ee851fb93d4143d43e | f5f980a1fb085103f548d7bbdf6fe0124dda176276fa1b8bac6783b6b22a150c |
| Complete moving first symbol, S.1–S.19 | a223a263c3dea6e87e9e51364ee541946eed4c77 | 2010d9a15ff5604dcdfd7d1db8f782a5f247806b4b007565073b02c8d4008fac |
| First-symbol mean through true rays | 5a758bd310a5d6c35e029ef51f1f9fd7b2d2de36 | 964537f77f037212afd697cc7cd0ac71d4bd9c21a6e6165d092128f58e62ac3e |
| Original primitive on actual Airy amplitudes | ddc62b4539d640a950c2005505e08695f80910e7 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| Ordered scalar root operator | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |

The first two texts already prove the genuine all-parameter correction, the arbitrary finite amplitude construction, and the existence of the resulting high relation after a sufficiently large finite cutoff. They also already prove the scalar finite part. Those conclusions are inherited here, not recomputed or claimed for the first time.

The new pointwise assertion below uses the original free-Airy recursion P.8, with every ordered scalar factor, old primitive, genuine $J$, and mean remainder retained. Its first amplitude is not relabelled as the later genuine-reference amplitude $w_1^V$. In fact the new root-limit identity does not require a new numerical evaluation of either amplitude.

## 2. The two actual phases and the fixed-cut extraction

Use the original fold and put $t=-T>0$. Choose the branch label by
$$
 \Phi_\sigma=X-\sigma\frac23t^{3/2},\qquad
 D_0\Phi_\sigma=\sigma\eta q\,\Phi_{\sigma,\phi},
 \qquad \sigma\in\{+1,-1\}.
 \tag{PF.2}
$$
Here $D_0=\partial_r-d\partial_\phi$ when applied to an actual coefficient. The fold identities $D_0T=QX_\phi$, $D_0X=-QT T_\phi$ and $Q\sqrt t=\eta q$ prove PF.2. This fixes the correspondence between the Airy signs and the two physical wave rows.

On the actual common analytic root germ,
$$
 \begin{gathered}
 t=\rho\tau(\rho,\phi),\quad
 \tau(0,\phi)=\lambda_*=(\eta_*^2k_*)^{1/3}>0,\\
 T_\phi=O(\rho^2),\quad X(0,\phi)=\phi,\quad
 X_\phi(0,\phi)=1,\\
 a_0(0,X)=1,\quad b_0=O(T^2),\quad
 a_1(0,X)=0,\quad b_1\text{ analytic at }T=0.
 \end{gathered}
 \tag{PF.3}
$$
A star means evaluation at $\rho=0$. The symbols $a_0,b_0,a_1,b_1$ in PF.3 are exactly the amplitudes in P.8, after their actual evaluation at $(T(r,\phi),X(r,\phi))$.

Fix $\rho>0$ first. Write $k_{\rm ang}=\epsilon n$, $n=4|j|$, $\epsilon=\operatorname{sgn}j$, and use $(ik_{\rm ang})^{-1}$ as the first-order expansion unit. The height contribution of branch $\sigma$ has the form
$$
 f_\sigma=n^{-1/6}e^{ik_{\rm ang}\Phi_\sigma}
       \left(A_\sigma+(ik_{\rm ang})^{-1}B_\sigma
                       +O(n^{-2})\right).
 \tag{PF.4}
$$
The common nonzero Airy constant is denoted by $\kappa_{\sigma,\epsilon}$. Set
$$
 \alpha_\sigma=a_0+i\epsilon\sigma\sqrt t\,b_0,\qquad
 A_\sigma=\kappa_{\sigma,\epsilon}\,t^{-1/4}\alpha_\sigma.
 \tag{PF.5}
$$
For sufficiently small fixed $\rho$, $\alpha_\sigma$ and $\Phi_{\sigma,\phi}$ are nonzero. All logarithmic derivatives below mean the corresponding quotient of derivatives; no global choice of logarithm is needed.

The complete relative first height coefficient is
$$
 \frac{B_\sigma}{A_\sigma}
 =-\frac{5\sigma}{48t^{3/2}}
   +\frac{i\epsilon b_0}{4t\alpha_\sigma}
   +i\epsilon
       \frac{a_1+i\epsilon\sigma\sqrt t\,b_1}{\alpha_\sigma}.
 \tag{PF.6}
$$
For clarity, the universal coefficients in this formula can be checked directly. The phase of a free Airy branch has derivative $\sigma\sqrt t$ with respect to $T$, and its leading amplitude is $t^{-1/4}$. Substitution in $Y_{TT}=n^2TY$ gives the relative first coefficient $-5\sigma/(48t^{3/2})$. Since the second Airy profile is $n^{-1}\partial_TY$, its corresponding coefficient is $7\sigma/(48t^{3/2})$. Their difference gives the second term of PF.6. The original expansion is $v_0+n^{-1}v_1$, so the conversion to $(ik_{\rm ang})^{-1}$ gives exactly the last factor $i\epsilon$.

PF.6 contains the full original first amplitude. It is not obtained by retaining only the leading scalar potential.

## 3. Reconstruction of both rows and the old primitive

In the notation of the ordered scalarization,
$$
 A_{\rm op}=\eta\partial_\phi+\ell+\mathcal O^{-1},\qquad
 B_{\rm op}=b_{\rm loc}+\mathcal O^{-1},
 \quad
 \ell=-2buv,\quad b_{\rm loc}=b(1-u^2-3Kv^2).
 \tag{PF.7}
$$
The exact construction is $h_1=J(D_0-B_{\rm op})f$, $h_2=f$, with the original projections and mean equations retained.

Define $D_\sigma=\partial_r-(d+\sigma\eta q)\partial_\phi$. Expanding the exact equation $A_{\rm op}h_1=(D_0-B_{\rm op})f$ in PF.4 gives
$$
 h_{1,0}=\sigma qA_\sigma,\qquad
 h_{1,1}=\sigma qB_\sigma+
 \frac{D_\sigma A_\sigma-b_{\rm loc}A_\sigma
                         -\sigma q\ell A_\sigma}
      {\eta\Phi_{\sigma,\phi}}.
 \tag{PF.8}
$$
The two operators denoted by $\mathcal O^{-1}$ in PF.7 enter one order later in this reconstruction. Their contributions to $a_1,b_1$ and to the full remainder are still present.

The own-wave projection $(h_2+\sigma h_1/q)/2$ therefore has relative first coefficient
$$
 \frac{B_\sigma}{A_\sigma}
  +\frac{\sigma(D_\sigma\log A_\sigma-b_{\rm loc})}
           {2\eta q\Phi_{\sigma,\phi}}
  -\frac{\ell}{2\eta\Phi_{\sigma,\phi}}.
 \tag{PF.9}
$$
The physical wave matrix adds only a radial factor to this own-wave amplitude. The old primitive acts on the actual phase, as in P.31, and contributes
$$
 -\frac{1}{\Phi_{\sigma,\phi}}
           \partial_\phi\log\left(\frac{A_\sigma}
                                      {\Phi_{\sigma,\phi}}\right).
 \tag{PF.10}
$$
Thus the complete own-phase relative first coefficient in the primitive density row is
$$
 \begin{split}
 d_\sigma^{(1)}
 ={}&\frac{B_\sigma}{A_\sigma}
  +\frac{\sigma(D_\sigma\log A_\sigma-b_{\rm loc})}
           {2\eta q\Phi_{\sigma,\phi}}
  -\frac{\ell}{2\eta\Phi_{\sigma,\phi}}\\
 &-\frac{1}{\Phi_{\sigma,\phi}}
           \partial_\phi\log\left(\frac{A_\sigma}
                                      {\Phi_{\sigma,\phi}}\right).
 \end{split}
 \tag{PF.11}
$$

There is no additional own-phase first contribution from the strict off-diagonal frame. The leading part of the other wave row carries the other phase. The term obtained by applying $-SI$ to it cancels the complete wrong-phase first coefficient by the exact P.23a identity. The next strict normalizer has order minus two. Consequently neither changes PF.11. This uses the two-row reconstruction, not the zero mean of the isolated finite symmetric summand in P.33.

Old-mean corrections and finite head maps are retained as exact smooth finite-rank operators. In a fixed-cut high-column expansion their coefficients decay beyond any prescribed inverse power by the old nonstationary primitive construction. They are not deleted from the original equations or from the final port problem.

## 4. The pointwise finite term

Every assertion in this section is an expansion of PF.11 after the first coefficient has already been extracted at a fixed positive $\rho$.

First, PF.3 and PF.6 give
$$
 \frac{B_\sigma}{A_\sigma}
 =-\frac{5\sigma}{48t^{3/2}}+O(\sqrt\rho).
 \tag{PF.12}
$$
The term involving $b_0/t$ is $O(\rho)$, while the full first-amplitude ratio is $O(\sqrt\rho)$. If a different common analytic root normalization of $a_1$ were used, it would give the same finite term on both branches.

Next,
$$
 D_\sigma\log A_\sigma
 =\frac1{4\rho}
   +\frac{\tau_\rho+(d+\sigma\eta q)\tau_\phi}{4\tau}
   +D_\sigma\log\alpha_\sigma.
 \tag{PF.13}
$$
The branch-dependent part of $\alpha_\sigma-a_0$ is $O(\rho^{5/2})$, so its radial derivative is $O(\rho^{3/2})$. Also $\tau_\phi=O(\rho)$ and $(a_0)_\phi=O(\rho)$. Thus the terms carrying an explicit $\sigma\eta q$ in the regular part of PF.13 produce $O(\rho)$ after the prefactor in PF.11. They create no finite branch-dependent term.

Finally,
$$
 \Phi_{\sigma,\phi}=X_\phi+O(\rho^{5/2}),\qquad
 X_\phi=1+O(\rho).
 \tag{PF.14}
$$
Its branch-dependent correction times the most singular term $\rho^{-3/2}$ is $O(\rho)$. The old-primitive term PF.10 tends to zero by PF.3. The only finite term remaining in PF.11 is therefore the common function $-\ell_*/(2\eta_*)$.

More precisely, for every fixed finite angular Sobolev index $s$, there is a smooth real function $A_{-1/2}(\phi)$ such that
$$
 d_\sigma^{(1)}(\rho,\phi)
 =\frac{\sigma g_0}{3\rho^{3/2}}
  +\frac{\sigma A_{-1/2}(\phi)}{\sqrt\rho}
  -\frac{\ell_*(\phi)}{2\eta_*}
  +O_{H^s}(\sqrt\rho),\qquad
 g_0=\frac1{16\eta_*\sqrt{k_*}}.
 \tag{PF.15}
$$
The leading coefficient follows without an unspecified scalar convention:
$-5/48$ from PF.12 plus $1/8$ from PF.13 is $1/48$, and
$\lambda_*^{3/2}=\eta_*\sqrt{k_*}$.

The $H^s$ remainder in PF.15 follows from the common analytic germ and finite Laurent expansions in $\sqrt\rho$. This is not an estimate uniform in the high-frequency limit. That limit was taken at the fixed cut in PF.4.

## 5. The actual root-label maps and the function counterterm

Let
$$
 H_\sigma(\rho,\cdot)=\Phi_\sigma(\rho,\cdot)^{-1},\qquad
 J_\sigma=\partial_xH_\sigma .
 \tag{PF.16}
$$
The variable $x$ is the true root label. These are the actual maps, not a radial replacement. Their equations and initial values are
$$
 \partial_\rho H_\sigma
   =d(\rho,H_\sigma)+\sigma\eta(\rho)\sqrt{\rho k(\rho)},
 \qquad H_\sigma(0,x)=x.
 \tag{PF.17}
$$
In particular,
$$
 \begin{split}
 H_\sigma(\rho,x)
   &=x+\rho d_*(x)
       +\sigma\frac23\eta_*\sqrt{k_*}\rho^{3/2}
       +O_{H^s}(\rho^2),\\
 J_\sigma(\rho,x)&=1+\rho(d_*)_\phi(x)+O_{H^s}(\rho^2),\\
 H_+-H_-&=O_{H^s}(\rho^{3/2}),\qquad
 J_+-J_-=O_{H^s}(\rho^{5/2}).
 \end{split}
 \tag{PF.18}
$$
The leading branch difference in $H_\sigma$ is angularly constant. Differentiating the two equations in PF.17 proves the last, stronger Jacobian bound.

In the P.24 convention the first coefficient on the root input circle is
$C_\sigma=d_\sigma^{(1)}\circ H_\sigma$. Put
$$
 \mathcal B(\rho,x)=C_-(\rho,x)-C_+(\rho,x).
 \tag{PF.19}
$$
The leading singular coefficient in PF.15 is radial. Substitution of PF.18 into its subleading function changes that term only by $O_{H^s}(\sqrt\rho)$. The common finite term also has the same root-label limit. Thus PF.15 already proves that the finite part of PF.19 is zero as a function, with its second singular coefficient still to be identified.

That coefficient is fixed by the full strict equations. Set
$$
 \begin{gathered}
 r_\sigma=u+\sigma qv,\qquad
 B_\sigma^{\rm w}=-\frac{q_r}{2q}-b(1+r_\sigma^2),\\
 a_\sigma=-d_{\phi\phi}
             -b(r_\sigma)_\phi r_{-\sigma}
             +\frac{\sigma B_+^{\rm w}B_-^{\rm w}}{2\eta q},\\
 \mathcal F(\rho,x)
   =J_+(\rho,x)a_+(\rho,H_+(\rho,x))
       -J_-(\rho,x)a_-(\rho,H_-(\rho,x)).
 \end{gathered}
 \tag{PF.20}
$$
These are the complete S.12 coefficients. To specify the radial gauge and its root normalization, use exactly Q.6/Q.10 of [the complete quadratic-density theorem](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md):
$$
 \mathfrak n=\frac{a_{\rm phys}^2}{\langle v\rangle^2},\qquad
 w_\sigma=\mathfrak n\,\frac{h_1+\sigma qh_2}{\sqrt{2q}}.
 \tag{PF.20a}
$$
After the original primitive and the positive $n^{7/6}$ input normalization, its leading branch amplitude is
$$
 \frac{\sigma\sqrt2}{i\epsilon}\,
    \mathfrak n\,\frac{\sqrt q\,A_\sigma}{\Phi_{\sigma,\phi}}
 \longrightarrow
 \frac{\sigma\sqrt2}{i\epsilon}\,
   \mathfrak n_*\kappa_{\sigma,\epsilon}
                \left(\frac{k_*}{\lambda_*}\right)^{1/4}.
 \tag{PF.20b}
$$
This is a nonzero angular constant by PF.3; no additional unknown root function remains. The ratio of the two displayed constants is the already fixed Maslov factor and is retained. The actual leading density equation is
$\partial_r y=(c_\sigma\partial_\phi+d_\phi-2R_0/\langle v\rangle)y$.
Its unique solution with that constant root normalization is the displayed constant times
$E(r)U_{\Phi_\sigma}$, where
$E(r)=\exp\{\int_{r_*}^r-2R_0/\langle v\rangle\,ds\}$ is common and radial, with $E(r_*)=1$. Its endpoint factors and source conversion stay in the port ledger; the common factor cancels in the homogeneous branch relation.

Conjugating the first-order generator by this exact density pullback gives $J_\sigma(a_\sigma\circ H_\sigma)I$. Since $\partial_r=-\partial_\rho$, the ordered first-coefficient equation is
$$
 \partial_\rho\mathcal B=\mathcal F.
 \tag{PF.21}
$$

The pointwise expansion of S.16 gives
$$
 \begin{gathered}
 g_1^{\rm pt}(x)
  =g_0\left[
        -\frac{\eta_\rho}{\eta}
        +\frac32\frac{k_\rho}{k}
        -8b(1+u^2)
       \right]_{\rho=0,\ \phi=x},\\
 \widehat g_1(x)=g_1^{\rm pt}(x)+g_0(d_*)_\phi(x),\\
 \mathcal F(\rho,x)
  =g_0\rho^{-5/2}
       +\widehat g_1(x)\rho^{-3/2}
       +O_{H^s}(\rho^{-1/2}).
 \end{gathered}
 \tag{PF.22}
$$
The extra term $g_0(d_*)_\phi$ is necessary: it is the product of the leading radial singularity with the common $\rho(d_*)_\phi$ term of the two actual Jacobians. Composing $g_1^{\rm pt}$ with the root maps first changes only the integrable $\rho^{-1/2}$ term. The regular common part of $a_+$ and $a_-$ gives no nonintegrable contribution.

Comparing PF.21 with PF.15 and PF.19 identifies $A_{-1/2}=\widehat g_1$. Therefore the new pointwise conclusion is
$$
 \boxed{\displaystyle
 \mathcal B(\rho,\cdot)
  +\frac{2g_0}{3\rho^{3/2}}
  +\frac{2\widehat g_1}{\sqrt\rho}
       \longrightarrow 0\quad\hbox{in every fixed }H^s
       \quad(\rho\downarrow0).}
 \tag{PF.23}
$$
The integration constant function is removed by PF.11–PF.19, not by its scalar mean. Taking the mean only afterwards recovers the old scalar result because
$$
 \langle\widehat g_1\rangle
  =\langle g_1^{\rm pt}\rangle=g_1.
 \tag{PF.24}
$$

## 6. A convergent expression for the complete coefficient

PF.21–PF.23 give the exact function identity
$$
 \boxed{\displaystyle
 \mathcal B(\rho,x)
 =-\frac{2g_0}{3\rho^{3/2}}
    -\frac{2\widehat g_1(x)}{\sqrt\rho}
  +\int_0^\rho
       \left\{\mathcal F(t,x)-g_0t^{-5/2}
                          -\widehat g_1(x)t^{-3/2}\right\}\,dt .}
 \tag{PF.25}
$$
This is an ordinary convergent integral after the explicit subtractions. With $t=s^2$, its integrand including $dt=2s\,ds$ extends continuously to $s=0$ in every fixed angular Sobolev norm. Signed Taylor-integral remainders may be used before taking a norm; subtraction of nearby upper bounds is not authorized.

At any fixed root-collar width $h$ one can evaluate the identical expression at the waist as
$$
 \begin{split}
 \mathcal C_{\rm root}
 ={}&-\frac{2g_0}{3h^{3/2}}
       -\frac{2\widehat g_1}{\sqrt h}\\
 &+\int_0^h
       \{\mathcal F-g_0t^{-5/2}-\widehat g_1t^{-3/2}\}\,dt
   +\int_h^{r_*}\mathcal F(t,\cdot)\,dt .
 \end{split}
 \tag{PF.26}
$$
The root-based flows in this formula extend to the actual waist. At polynomial seams the continuously repaired state and the strict first frame have the same values, as in the selected-family theorem. Their higher derivative jumps and all source jumps remain in the complete remainder; they do not create an omitted order-minus-one jump in PF.26.

Here the directed-word lifts have exactly the original fixed waist convention:
$S_\pm(0,\cdot)=\mathrm{id}$ and
$\partial_rS_\pm+(-d\pm\eta q)\partial_\phi S_\pm=0$.
The symbols $S_\pm$ and $X_\pm=S_\pm^{-1}$ in the next display mean their values at the same actual root $r_*$, not maps based at a different cut. Uniqueness of the characteristic equation gives
$\Phi_\sigma(r)=X_{-\sigma}(r_*)\circ S_{-\sigma}(r)$, and hence
$$
 H_+(r_*)=S_-(r_*),\qquad
 H_-(r_*)=S_+(r_*),\qquad
 P=S_-\circ X_+ .
 \tag{PF.27}
$$
The two branch maps have leading factors $U_{X_-}$ and $U_{X_+}$ at the waist. Factoring the actual directed relation in the original density convention therefore gives
$$
 \mathcal R
   =\zeta U_P(1+M_{c_0}I)+R_{4/3},\qquad
 \boxed{\ c_0=X_-'\,(\mathcal C_{\rm root}\circ X_-)\ }.
 \tag{PF.28}
$$
Indeed $U_{X_+}U_{X_-}^{-1}=U_P$, and the first symbol of
$U_{X_-}M_{\mathcal C_{\rm root}}I U_{X_-}^{-1}$ is
$M_{X_-'(\mathcal C_{\rm root}\circ X_-)}I$. Its exact mean and commutator remainders are retained in $R_{4/3}$ and the finite rows. The Maslov factor $\zeta$ and the original directed order are unchanged.

This is the full strict-density first coefficient. A separately chosen half-density or physical-state realization must still apply its actual conjugation and endpoint readouts; no such transformation is silently absorbed into PF.28.

The mean identities are exact:
$$
 \langle\mathcal F(\rho)\rangle=\langle a_+-a_-\rangle
       =\langle\Xi(\rho)\rangle,\qquad
 \langle c_0\rangle
       =\langle\mathcal C_{\rm root}\rangle
       =\mathfrak X(\delta).
 \tag{PF.29}
$$
Thus $\beta(\delta)=-\langle c_0\rangle/4$ agrees with the published scalar identity.

## 7. What the new formula supplies, and what it does not

PF.26–PF.28 replace an unspecified nonmean endpoint function by a complete, ordered, convergent expression in the actual coefficients and the two actual root-based rays. They include both drift terms, both branch multipliers, the nonlocal first symbol, the root Jacobian counterterm, and all Fourier modes.

A subsequent numerical consumer would have to bound this full function, together with the true density postcomposition. It cannot replace $\mathcal F$ by its angular mean, use the scalar finite-part native as a nonmean bound, or use a local piece of $\Xi$ as the whole return coefficient. Existing old fields and ray certificates may be consumed on their proved common domains; accepted targets are not to be recomputed.

For the exact principal angle $\mathcal H$, the input of the new full-circle normalizer is
$$
 \bigl\|c_0-\mu\mathcal H'\bigr\|_{H^3_\phi},
 \qquad \mu=\langle c_0\rangle,
 \tag{PF.30}
$$
followed by the separately proved actual-angle density transfer. PF.30 has not been numerically evaluated here.

All source and mean columns, the finite bordered block, the incoming branch inverse, the strong remainder, and physical port changes still require their stated quantitative bounds. The pointwise root calculation changes none of those scopes and does not promote the current ordinary weak source ledger into a strong return inverse.
