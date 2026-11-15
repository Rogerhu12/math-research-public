# R133 supplement: complete free Airy first-omitted strict-cut columns

2026-11-15, newton_source.

**Analytic contract.** This gives a finite, explicit strong-norm bound for the free first-order Airy trial at the exact cut (P.22), including the complete original nonlocal inverse, original primitive, both physical rows, the two oscillatory branches and all mean terms. The leading and first coefficients are those of (P.23a)--(P.24). The bound is a new scalar target; no numerical value of it is asserted here. The already successful free-amplitude, fold, TN and TC calculations are read as inputs and are not repeated.

The genuine-minus-free contribution, including the terminal-Ai root matrix and positive correction, is separately retained by AD, RR, ST and AW. The present statement supplies the free first-omitted cut contribution. Its propagation to the waist, the true leading receiver there, complete incoming and outgoing remainders, incoming inversion and finite Schur rows remain distinct interfaces.

## 1. Exact reference, cut and input normalization

Use the same continuous repaired selected family at intrinsic $\eta_0$, with real $|\delta|\le10^{-8}$. The full complex parameter disk is used only for the already certified coefficient bounds. The original P construction at $\delta=0$ extends to this same family by the full-family B/PF construction; it is not re-proved here. Fix
$$
 r_c={76285779072683\over320000000000000},\qquad
 \rho=r_*(\delta)-r_c,\qquad 0<\rho<4\,10^{-6}.
 \tag{FA.1}
$$
The certified root interval is
$[1191984371497/5000000000000,\,
2383968743003/10000000000000]$.
All evaluations use its actual selected root, not its midpoint.

Write $n=4|j|$, $\epsilon=\operatorname{sgn}j$, and $z=n^{-1}$.
For an optional input cutoff $J_c\ge97$, put $N=4J_c$.
The finite labels $97\le|j|<J_c$ remain explicit. A strict-normalizer cutoff $J_s$ used below is a separate parameter and projector.

Let $P=1-\Pi$ and $I=\partial_\phi^{-1}P$ on the old normalized circle of period $\pi/2$. For a two-amplitude vector $a$ define
$$
 {\cal U}(a)=e^{i\epsilon nX}
 \{a_1\operatorname{Ai}(n^{2/3}T)
       +a_2n^{-1/3}\operatorname{Ai}'(n^{2/3}T)\}.
 \tag{FA.2}
$$
An amplitude matrix means rowwise application of this formula. The prime on $\operatorname{Ai}$ is the derivative in its scalar argument.

Set $W=w_0+z w_1$, where $w_1$ is the original free first amplitude. It is not the genuine-potential amplitude $w_1^V=w_1+\mathcal B K_Tw_0$. This identity is fixed by the original Taylor producer: its order-zero forcing uses the complete ordered scalar coefficient and the $\vartheta$ contribution from $R_{-1}D_0$; its free transport equation, common root condition $a_1(0,X)=0$, and the unique analytic transport (I.21) are precisely (P.8) for $k=0$. In particular the $\vartheta$ term is not silently dropped when identifying the saved amplitude.

The exact physical trial is
$$
 h_2=P{\cal U}(W),\qquad
 h_1=J(D_0-B)P{\cal U}(W),\qquad
 D_0=\partial_r-Pd\partial_\phi P.
 \tag{FA.3}
$$
Here, with radial coefficients $b,K,\eta$,
$$
 \begin{split}
 A&=\eta\partial_\phi+P\ell P-2bPv_\phi IuP,\qquad J=A^{-1},\\
 \ell&=-2buv,\qquad b_{\rm loc}=b(1-u^2-3Kv^2),\\
 B&=P b_{\rm loc}P-2bK Pv_\phi IvP,\qquad
 D=\partial_r-d\partial_\phi .
 \end{split}
 \tag{FA.4}
$$
All products retain their order. The even mean equation outside $J$ is independent. Complex columns are considered before their exact reflection restriction, so both physical signs and every intermediate mean are present.

## 2. Complete real Airy remainder, including small $n(-T)^{3/2}$

The external primary sources are the official DLMF equations
[9.7.2](https://dlmf.nist.gov/9.7.E2),
[9.7.9](https://dlmf.nist.gov/9.7.E9),
[9.7.10](https://dlmf.nist.gov/9.7.E10), and the third paragraph of
[9.7(iii), Error Bounds for Real Variables](https://dlmf.nist.gov/9.7.iii).
The last source supplies the bound for each real oscillatory series when the first omitted term and its successor have opposite signs. This is the real-variable error theorem, not merely the asymptotic expansion sign.

Put $t=-T>0$, $\omega=2t^{3/2}/3$, and $\chi=n\omega-\pi/4$.
The coefficients are
$$
 u_0=v_0=1,\qquad
 u_k={(6k-5)(6k-3)(6k-1)\over(2k-1)216k}u_{k-1},
 \qquad v_k={6k+1\over1-6k}u_k .
 \tag{FA.5}
$$
In particular $u_1=5/72$, $v_1=-7/72$, and $u_k>0$, $v_k<0$ for $k\ge1$.

Retain one term in each even and odd series. In the Ai even series the omitted pair has signs $-u_2,+u_4$; in its odd series they are $-u_3,+u_5$. In the derivative even and odd series the corresponding pairs are $-v_2,+v_4$ and $-v_3,+v_5$. Thus the required alternation holds in all four cases. For every positive $t$ and $n$, the real theorem gives
$$
 \begin{split}
 n^{1/6}\operatorname{Ai}(-n^{2/3}t)
 &=\pi^{-1/2}t^{-1/4}
       \left(\cos\chi+{u_1\over n\omega}\sin\chi+r_a\right),\\
 n^{-1/6}\operatorname{Ai}'(-n^{2/3}t)
 &=\pi^{-1/2}t^{1/4}
       \left(\sin\chi-{v_1\over n\omega}\cos\chi+r_b\right),\\
 |r_a|&\le {u_2\over n^2\omega^2}
                 +{u_3\over n^3\omega^3},\\
 |r_b|&\le {|v_2|\over n^2\omega^2}
                 +{|v_3|\over n^3\omega^3}.
 \end{split}
 \tag{FA.6}
$$
This includes $n=388$ at (FA.1). It does not require $n\omega\ge1$.
The resulting constants may be large near the root. No derivative is ever taken of either error term in (FA.6).

Suppose complete same-cut bounds $0<t_-\le t\le t_+$ are supplied and set $\omega_-=2t_-^{3/2}/3$. Define
$$
 \begin{split}
 P_a&={t_-^{-1/4}\over\sqrt\pi}
 \left(1+{u_1\over N\omega_-}
          +{u_2\over N^2\omega_-^2}
          +{u_3\over N^3\omega_-^3}\right),\\
 P_b&={t_+^{1/4}\over\sqrt\pi}
 \left(1+{|v_1|\over N\omega_-}
          +{|v_2|\over N^2\omega_-^2}
          +{|v_3|\over N^3\omega_-^3}\right),\qquad
 P_*=\max(P_a,P_b),\\
 P_1&={1\over\sqrt\pi\,\omega_-}
               \max(u_1t_-^{-1/4},|v_1|t_+^{1/4}),\\
 P_2&={1\over\sqrt\pi}
 \max\left\{
 t_-^{-1/4}\left({u_2\over\omega_-^2}
                   +{u_3\over N\omega_-^3}\right),
 t_+^{1/4}\left({|v_2|\over\omega_-^2}
                   +{|v_3|\over N\omega_-^3}\right)\right\}.
 \end{split}
 \tag{FA.7}
$$
Here $P_*$ bounds both complete scaled profiles, $P_1$ bounds their first inverse-frequency coefficient, and $P_2 n^{-2}$ bounds their complete first-omitted scaled remainder. Matrix and vector norms below are entry-sum norms; they dominate the Euclidean output norm and make (FA.7) directly applicable to all entries.

## 3. Finite coefficient calculus and the old mean

For an amplitude polynomial $F(z)=\sum_kz^kF_k$ use
$$
 [F]_{N,\sigma}=\sum_kN^{-k}\|F_k\|_{\sigma},
 \tag{FA.8}
$$
with the complete entry-sum supremum on the genuine old physical strip.
Without a strip subscript the same bound, or its restriction to the real circle, is used. Products are bounded before summing the positive coefficient budget. No upper bound is subtracted from another upper bound.

The saved free-amplitude radius stage at $h=9\,10^{-6}$ contains all $p=0,1,2$ and $q=0,1,2,3$ budgets on physical widths zero and $1/512$. Its complete $p=0,1$ holomorphic suprema suffice for the new formulas here. Higher angular derivatives of the finite expressions below are new Cauchy products on nested strips from $1/512$ to $1/1024$; the saved Taylor coefficients or saved norms are not recomputed. At most six successive explicit angular differentiations occur in these expressions, so allocating sixteen equal positive strip losses is sufficient. Every initial coefficient, its required radial derivative and $H_\epsilon^{-1}$ must have its same original full-strip input certificate.

The exact amplitude matrices and primitive recursion are
$$
 \begin{split}
 H_\epsilon&=i\epsilon X_\phi{\rm Id}+T_\phi K_T,&
 M_\epsilon&=i\epsilon DX\,{\rm Id}+DT\,K_T,&
 K_T&=\begin{pmatrix}0&T\\1&0\end{pmatrix},\\
 {\cal I}_0a&=H_\epsilon^{-1}a,&
 {\cal I}_{l+1}a&=-H_\epsilon^{-1}\partial_\phi{\cal I}_la,&
 {\cal I}^{[3]}a&=z{\cal I}_0a+z^2{\cal I}_1a+z^3{\cal I}_2a .
 \end{split}
 \tag{FA.9}
$$
Thus
$$
 \partial_\phi{\cal U}(a)={\cal U}(z^{-1}H_\epsilon a+a_\phi),
 \quad D{\cal U}(a)={\cal U}(z^{-1}M_\epsilon a+Da),
 \quad
 I{\cal U}(a)=P{\cal U}({\cal I}^{[3]}a)
                -z^3I{\cal U}(\partial_\phi{\cal I}_2a).
 \tag{FA.10}
$$
This last identity holds for an amplitude with nonzero old mean.

The original contour proof (I.13) also retains that mean:
$$
 |\Pi{\cal U}(a)|
 \le20M_F(1+n^{2/3}T_c)e^{-cn}\|a\|_{1/1024}.
 \tag{FA.11}
$$
Here $T_c$ is the original complete contour image and
$M_F=\max(|\operatorname{Ai}(0)|,|\operatorname{Ai}'(0)|)<1$.
The original physical contour width $3/1024$ had
$c_\Pi>0.002921264998045$.
Restriction to width $1/1024$ loses $1/512$ from this exponent and still permits $c=1/2048$. Its original $T_c$ and displacement bounds remain valid by restriction. This assertion uses the original full-family fold and primitive identities; a numerical consumer must lock those identities and the amplitude-strip qualification.

For any $\alpha\ge0$ set
$$
 E_\alpha=20M_F\left(
      \sup_{x\ge N}x^\alpha e^{-cx}
       +T_c\sup_{x\ge N}x^{\alpha+2/3}e^{-cx}\right).
 \tag{FA.12}
$$
Each supremum is evaluated at $N$ or at the stationary point $p/c$ for its exponent $p$. Then
$|\Pi{\cal U}(F(z))|\le n^{-\alpha}E_\alpha[F]_{N,1/1024}$.
All signs and the complete old mean are included; there is no finite Fourier-tail surrogate.

## 4. Complete $J$ reconstruction through a sufficient finite order

Put $\mathcal A_0=\eta\partial_\phi+\ell$ on amplitudes. Define the following four finite vectors for each physical sign:
$$
 \begin{split}
 g_0={}&(\eta H_\epsilon)^{-1}M_\epsilon w_0,\\
 g_1={}&(\eta H_\epsilon)^{-1}
 \{M_\epsilon w_1+(D-b_{\rm loc})w_0-\mathcal A_0g_0\},\\
 g_2={}&(\eta H_\epsilon)^{-1}
 \{(D-b_{\rm loc})w_1+2bK v_\phi\mathcal I_0(vw_0)
                 -\mathcal A_0g_1+2b v_\phi\mathcal I_0(ug_0)\},\\
 g_3={}&(\eta H_\epsilon)^{-1}
 \{2bK v_\phi[\mathcal I_0(vw_1)+\mathcal I_1(vw_0)]
                 -\mathcal A_0g_2
          +2b v_\phi[\mathcal I_0(ug_1)+\mathcal I_1(ug_0)]\},\\
 G(z)={}&g_0+zg_1+z^2g_2+z^3g_3 .
 \end{split}
 \tag{FA.13}
$$
No inverse of an infinite formal series is used. The only new inverses here are the actual point matrix and the radial nonzero $\eta$.

Form the complete amplitude polynomial
$$
 \begin{split}
 \mathcal R(z)={}&z^{-1}\eta H_\epsilon G+\mathcal A_0G
                     -2b v_\phi\mathcal I^{[3]}(uG)\\
 &-z^{-1}M_\epsilon W-(D-b_{\rm loc})W
                     -2bK v_\phi\mathcal I^{[3]}(vW).
 \end{split}
 \tag{FA.14}
$$
The coefficients of degrees $-1,0,1,2$ vanish by (FA.13). The remainder has only degrees $3,\ldots,6$. Define
$R_3=[z^{-3}\mathcal R]_N$, using complete strip bounds for all of its coefficients.

Write $m_F=\Pi\mathcal U(F)$, including when $F$ is a polynomial in $z$.
Substitution into the exact operators gives
$$
 \begin{split}
 \mathcal E&=AP\mathcal U(G)-(D_0-B)P\mathcal U(W)
                =P\mathcal U(\mathcal R)+\mathcal M+\mathcal T,\\
 \mathcal M={}&-P\ell\,m_G
       +2bPv_\phi\,m_{\mathcal I^{[3]}(uG)}
       +2b\,m_G Pv_\phi Iu\\
 &-P b_{\rm loc}\,m_W
       +2bK Pv_\phi\,m_{\mathcal I^{[3]}(vW)}
       +2bK\,m_W Pv_\phi Iv,\\
 \mathcal T={}&2bz^3Pv_\phi I\mathcal U(\partial_\phi\mathcal I_2(uG))
       +2bKz^3Pv_\phi I\mathcal U(\partial_\phi\mathcal I_2(vW)).
 \end{split}
 \tag{FA.15}
$$
In particular the radial derivative of $m_W$ disappears only under the explicit final $P$ in $D_0P\mathcal U(W)=PD\mathcal U(W)$. It is not dropped from an unprojected equation. The signs of all six mean terms in (FA.15) follow from the actual $A$ and $B$, not a local replacement.

Let $u_*,v_*,v_{1,*},\ell_*,b_{{\rm loc},*}$ be complete real-circle suprema, and define
$$
 \begin{split}
 M_{\rm old}={}&
 \left(\ell_*+{|b|v_{1,*}u_*\over2}\right)[G]_N
 +\left(b_{{\rm loc},*}+{|bK|v_{1,*}v_*\over2}\right)[W]_N\\
 &+2|b|v_{1,*}
    \left([\mathcal I^{[3]}(uG)]_N
                 +|K|[\mathcal I^{[3]}(vW)]_N\right),\\
 C_J^{\rm res}={}&P_*
 \left\{R_3+{|b|v_{1,*}\over2}
 \left([\partial_\phi\mathcal I_2(uG)]_N
          +|K|[\partial_\phi\mathcal I_2(vW)]_N\right)\right\}
           +E_{19/6}M_{\rm old}.
 \end{split}
 \tag{FA.16}
$$
The strip norm is understood for every term used with $E_{19/6}$.
The factors $1/2$ are $2\|I\|=2/4$; no independent mean is deleted.

For all $n\ge N$, (FA.6), (FA.11) and the exact primitive norm imply
$$
 \|\mathcal E\|_2\le C_J^{\rm res}n^{-19/6},\qquad
 \|h_1-P\mathcal U(G)\|_2
              \le J_* C_J^{\rm res}n^{-19/6}.
 \tag{FA.17}
$$
The second inequality is the exact residual identity
$h_1=P\mathcal U(G)-J\mathcal E$.
$J_*$ is a complete same-domain $L^2$ inverse bound, such as the original (I.15), not an inverse Fourier truncation. No derivative of its error is used.

## 5. Physical wave matrix and the outer old primitive

Let $\mathcal R_c$ be the exact radial gauge and characteristic wave matrix in the chosen P/S convention at $r_c$, with complete norm $R_*$. For the ungauged AW density convention this is the stated radial $n_gT(q)$; if the common radial reaction gauge has been removed, its endpoint factor is included in $\mathcal R_c$. It is independent of $\phi$, and its normalization must agree with the subsequent strict frame. A change between those conventions is a real scalar multiplication, never an omitted factor.

Define
$$
 V(z)=\mathcal R_c
       \begin{pmatrix}G_1(z)&G_2(z)\\W_1(z)&W_2(z)\end{pmatrix},
 \qquad
 \mathcal B(z)=\sum_{\ell=0}^2z^\ell\mathcal I_\ell V(z)
                   =\sum_{k=0}^5z^k\mathcal B_k .
 \tag{FA.18}
$$
The recursion acts on each row amplitude, before multiplication by the Airy profiles. The complete normalized old density column is
$$
 F_{n,\epsilon}=n^{7/6}I\,\mathcal R_c
                  \begin{pmatrix}h_1\\h_2\end{pmatrix}.
 \tag{FA.19}
$$
Its input normalization is $n^{7/6}$, as in P24 and AW, not $n^{1/6}$.

A second use of (FA.10) gives
$$
 \begin{split}
 \|F_{n,\epsilon}-n^{1/6}\mathcal U(\mathcal B(z))\|_2
                  &\le C_{\rm rec}n^{-2},\\
 C_{\rm rec}
 &= {R_*J_*C_J^{\rm res}\over4}
      +{P_*\over4}[\partial_\phi\mathcal I_2V]_N
      +E_{13/6}[\mathcal B]_N .
 \end{split}
 \tag{FA.20}
$$
The three terms respectively pay the full $J$ residual, the full outer primitive remainder, and its old mean. The exact trial rows in (FA.3) have zero physical mean; this does not set the independent physical means of the corrected solution or the supplied data to zero. The mean terms of the finite approximation and all external mean rows remain.

## 6. Two true phases and their complete first-omitted coefficient

Put $\Phi_\sigma=X+\sigma\omega$, $\sigma=\pm1$. For each row of the amplitude matrix define the following column vectors:
$$
 \begin{split}
 A_{\sigma,0}
  &={e^{-i\epsilon\sigma\pi/4}\over2\sqrt\pi}
       \{t^{-1/4}\mathcal B_{0,a}
               -i\epsilon\sigma t^{1/4}\mathcal B_{0,b}\},\\
 A_{\sigma,1}
  &={e^{-i\epsilon\sigma\pi/4}\over2\sqrt\pi}
       \{t^{-1/4}\mathcal B_{1,a}
               -i\epsilon\sigma t^{1/4}\mathcal B_{1,b}
        -{i\epsilon\sigma u_1\over\omega}
                           t^{-1/4}\mathcal B_{0,a}
        -{v_1\over\omega}t^{1/4}\mathcal B_{0,b}\}.
 \end{split}
 \tag{FA.21}
$$
The suffixes $a,b$ select the first and second Airy columns of the matrix. Define the full leading-plus-first operator on the input Fourier basis by
$$
 \mathcal Le_j=\sum_{\sigma=\pm1}
       e^{i\epsilon n\Phi_\sigma}
                 (A_{\sigma,0}+n^{-1}A_{\sigma,1}).
 \tag{FA.22}
$$
The physical wave label satisfying
$\partial_r\Phi_\sigma=c_\sigma\partial_\phi\Phi_\sigma$
may exchange the displayed plus and minus signs, exactly as in P23a.

All remaining terms are bounded without differentiating the Airy remainder:
$$
 \begin{split}
 C_{\rm Airy}={}&
 P_*\sum_{k=2}^5N^{-(k-2)}\|\mathcal B_k\|_\infty
       +P_1\|\mathcal B_1\|_\infty\\
 &+P_2(\|\mathcal B_0\|_\infty
                         +N^{-1}\|\mathcal B_1\|_\infty),\\
 C_{\rm pre}&=C_{\rm rec}+C_{\rm Airy},\qquad
 \|(F-\mathcal L)e_j\|_2\le C_{\rm pre}(4|j|)^{-2}.
 \end{split}
 \tag{FA.23}
$$
The first term uses the complete profiles for every coefficient of degree at least two. The second pays the first Airy correction multiplying $\mathcal B_1$. The last pays both complete profile remainders multiplying $\mathcal B_0+z\mathcal B_1$. Thus there is no double deletion or coefficientwise minimum between different objects.

With $\Lambda_j=\sqrt{1+16j^2}$ define
$$
 \mathcal H(J_c)={2\over4^{2/3}}
             (J_c^{-4/3}+3J_c^{-1/3})^{1/2}.
 \tag{FA.24}
$$
The original P25 Hilbert--Schmidt argument, including both physical signs and every output Fourier mode, yields
$$
 \|F-\mathcal L\|_{H^{-4/3}(\{|j|\ge J_c\})\to L^2}
                  \le\mathcal H(J_c)C_{\rm pre}.
 \tag{FA.25}
$$
The output has not been projected onto a diagonal Fourier multiplier. No growing scalar ODE is used as a substitute for this strong operator bound.

## 7. Exact first-frame error with the original mean

For a real circle lift $\Phi$ let $\kappa=\Phi_\phi>0$ and $e=e^{i\epsilon n\Phi}$. This exponential is genuinely periodic because $n=4|j|$. For a known smooth vector $a$ put $b_a=a/\kappa$. Differentiation followed by the original $I$ gives
$$
 I(ea)={z\over i\epsilon}
          \{e b_a-\Pi(e b_a)-I(e\,\partial_\phi b_a)\}.
 \tag{FA.26}
$$
A real integration by parts also gives
$|\Pi(e b_a)|\le z\|\partial_\phi(b_a/\kappa)\|_2$.
Applying (FA.26) once more to its final primitive, and using $\|I\|=1/4$, proves
$$
 \begin{split}
 E_0(a,\kappa)&=
 \|\partial_\phi(b_a/\kappa)\|_2
       +2\|(\partial_\phi b_a)/\kappa\|_2
       +{1\over4}
         \|\partial_\phi((\partial_\phi b_a)/\kappa)\|_2,\\
 E_1(a,\kappa)&=
       2\|a/\kappa\|_2
          +{1\over4}\|\partial_\phi(a/\kappa)\|_2,\\
 \left\|I(ea)-{z\over i\epsilon}e\,a/\kappa\right\|_2
       &\le z^2E_0(a,\kappa),\qquad
 \|zI(ea)\|_2\le z^2E_1(a,\kappa).
 \end{split}
 \tag{FA.27}
$$
The factor two is a safe triangle bound retaining the whole projected mean. These are derivatives of known phase amplitudes, not derivatives of the Airy errors in (FA.6).

Use the actual off-diagonal first normalizer $S$ from P27/S9 and the same physical density convention as $\mathcal R_c$. Let $S_*$ bound its complete real multiplication norm. Define
$$
 \begin{split}
 C_{\rm frame}&=S_*\max_{\epsilon=\pm1}
       \sum_{\sigma=\pm1}
        \{E_0(A_{\sigma,0},\kappa_\sigma)
                         +E_1(A_{\sigma,1},\kappa_\sigma)\},
       \qquad \kappa_\sigma=\partial_\phi\Phi_\sigma,\\
 B_{\rm free}^{[1]}e_j
   &=\sum_{\sigma=\pm1}e^{i\epsilon n\Phi_\sigma}
       \left\{A_{\sigma,0}
          +z\left(A_{\sigma,1}
                 -{S A_{\sigma,0}\over i\epsilon\kappa_\sigma}\right)\right\}.
 \end{split}
 \tag{FA.28}
$$
Then
$\|((1-SI)\mathcal L-B_{\rm free}^{[1]})e_j\|_2
\le C_{\rm frame}n^{-2}$.
The order-minus-one other-row coefficient cancels exactly by P23a: the first amplitudes in (FA.13) solve that same complete free transport, and the first old primitive is exactly the one used in (FA.26). Consequently the remaining first coefficient is the own-branch coefficient of P24, including its endpoint terms. This assertion does not remove any of the remainder in (FA.27).

## 8. Exact TN remainder and complete leading receiver

On the moving output circle, with its separate cutoff $J_s$, write
$$
 A_s=P_{J_s}SI P_{J_s},\qquad
 B_s=P_{J_s}S_2I^2P_{J_s},\qquad
 \mathcal N=(1+B_s)^{-1}(1+A_s)^{-1}.
 \tag{FA.29}
$$
The same inverse acts on its two certified windows. The input finite complement is retained, and independent physical means have the stated identity block. TN gives the exact decomposition
$$
 \mathcal N=1-SI+F_S+R_N,\qquad
 F_S=SI-P_{J_s}SI P_{J_s}.
 \tag{FA.30}
$$
Its complete actual bounds are denoted $K_0$ on $L^2$,
$R_{N,*}$ from $H^{-4/3}$ to $L^2$, and $F_{S,*}$ on the same strong window. The finite term includes the full input and output support through $J_s+191$ and its auxiliary mean terms; it is not set to zero. The actual TN numerical cutoff need not equal $J_c$.

Equations (FA.25), (FA.28) and (FA.30) give the exact split
$$
 \mathcal NF-B_{\rm free}^{[1]}
 =\mathcal N(F-\mathcal L)
       +[(1-SI)\mathcal L-B_{\rm free}^{[1]}]
       +(F_S+R_N)\mathcal L.
 \tag{FA.31}
$$
Thus, if $L_-$ is a complete norm of $\mathcal L$ on $H^{-4/3}$,
$$
 C_{\rm free,cut}
   =K_0\mathcal H(J_c)C_{\rm pre}
        +\mathcal H(J_c)C_{\rm frame}
        +(F_{S,*}+R_{N,*})L_-
 \tag{FA.32}
$$
is a complete strong bound for this normalized free cut remainder. Alternatively $F_S\mathcal L$ may be retained as its exact finite-rank map and its displayed norm fee removed from (FA.32); the map itself and its true transported finite span are then mandatory data.

Here is an explicit complete leading receiver for (FA.32). For a scalar or vector coefficient put
$W_{4/3}(a)=\sum_{k\in\mathbb Z}(1+|4k|)^{4/3}|\widehat a_k|$,
using entry-sum norms for vectors.
Let $B_{\Phi_\sigma,-}$ be the TC bound for the true density
$U_{\Phi_\sigma}f=\kappa_\sigma(f\circ\Phi_\sigma)$
on $H^{-4/3}$ at this same cut. Then
$$
 L_-=\sum_{\epsilon=\pm1}\sum_{\sigma=\pm1}
 B_{\Phi_\sigma,-}
 \left\{W_{4/3}(A_{\sigma,0}/\kappa_\sigma)
      +N^{-1}W_{4/3}(A_{\sigma,1}/\kappa_\sigma)\right\}
 \tag{FA.33}
$$
is sufficient. Indeed $M_aC_\Phi=M_{a/\kappa}U_\Phi$.
The positive and negative input projectors have norm one, and the inverse-frequency factor is an input multiplier of norm at most $1/N$. On these nonmean inputs the TC density block and its adjoined-mean version agree; all output means subsequently generated by multiplication are still included. A generic full-circle bound requiring only known derivatives is
$$
 W_{4/3}(a)\le3\|a\|_{H^2},\qquad
 \|a\|_{H^2}^2=\|a\|_2^2+2\|a_\phi\|_2^2+\|a_{\phi\phi}\|_2^2 .
 \tag{FA.34}
$$
For its proof, the zero mode is charged separately; the two-sign Cauchy--Schwarz sum has square root at most $9/8$, and
$(1+n)^{4/3}\le(27/20)n^{4/3}$ for $n\ge4$.
Hence $1+243/160<3$ bounds the complete sum. The squared identity in (FA.34) is for a scalar coefficient. For a vector or matrix coefficient, the right-hand $H^2$ quantity means the sum of the scalar component $H^2$ norms, matching the entry-sum definition of $W_{4/3}$. Componentwise application followed by summation gives the stated vector bound.

The later strict-propagation input is the corrected first-order map
$B_{\rm free}^{[1]}$, rather than $\mathcal L$. Its negative-window norm is saved separately. TN also saves a complete $S_{\phi,*}$ and the exact angular bandwidth $192$. The real Bernstein inequality gives $\|S_{\phi\phi}\|_\infty\le768S_{\phi,*}$ entrywise. Because $S$ is off diagonal, the scalar weighted multiplication bound applies to each of its two independent entries without an extra matrix factor. Thus a sufficient complete multiplication norm is
$$
 M_{S,-}=3\sqrt{S_*^2+2S_{\phi,*}^2+(768S_{\phi,*})^2},\qquad
 \widetilde L_-=
 L_-+{M_{S,-}\over N}
   \sum_{\epsilon,\sigma}B_{\Phi_\sigma,-}
             W_{4/3}(A_{\sigma,0}/\kappa_\sigma^2).
 \tag{FA.34a}
$$
This uses (FA.34) and keeps the complete zero mode of $S$. It proves
$\|B_{\rm free}^{[1]}\|_{H^{-4/3}\to H^{-4/3}}\le\widetilde L_-$.
The additional scalar products use the same already constructed amplitude and phase derivatives. They do not repeat an old normalizer target. A subsequent conversion from inverse-normalized error back to the raw cut must also multiply by the true forward $L^2$ norm of the same ordered normalizer. A radial $n_g^{-1}$ for a different raw convention must use its own positive same-cut lower bound.

The constants in (FA.33) belong to the actual P22 maps. They are not reused as waist-map constants. Conjugating the final error by any subsequent leading multiplier or density map costs that map's actual source and target window norms. Neither boundedness nor invertibility of a finite compression follows from (FA.32).

## 9. New scalar target and saved-input discipline

A numerical consumer of this contract must check and save, before any terminal size guard:

1. The exact family, root interval, piece and cut; the full physical-strip identities for the free amplitudes and fold coefficients; complete positive lower bounds for $t$, $\eta$, the point determinant and each real $\kappa_\sigma$.
2. The finite Cauchy products (FA.8)--(FA.16), including every polynomial coefficient and all six mean budgets, with outward upper bounds and without subtracting unrelated upper bounds.
3. The three separate reconstruction fees (FA.20), real Airy constants (FA.7), and first-frame fees (FA.27)--(FA.28).
4. The actual same-cut TN/TC conclusions and their full scalar source identity; the complete leading receiver (FA.33), both sign inputs, external means and any retained finite map.
5. The separate cutoffs $J_c,J_s$, whether $F_S\mathcal L$ is norm-paid or explicitly retained, and the exact strong source and output types.

Only these new finite scalar products and their complete norm budgets are authorized by this contract. The original free Taylor coefficients, their complete old radius bounds, old profile integrals, full inverse, successful normalizers and coordinate enclosures are read rather than recomputed. All binary original evidence is restored only in the public runner. New temporary arrays or coefficient polynomials are not repository outputs.

The final statement is
$$
 \|\mathcal NF-B_{\rm free}^{[1]}\|_{H^{-4/3}\to L^2}
       \le C_{\rm free,cut},
 \tag{FA.35}
$$
with the optional explicitly retained finite map as specified above. This statement is conditional on those numerical input bounds when a numerical constant is requested. It does not claim that this constant has been evaluated, that a cutoff-97 incoming inverse passes, or that a complete return remainder has been assembled.

## 10. Primary identity table

All repository paths below are relative to topics/visible-flex-exact-nearby. Exact bytes are identifiers, not permission to execute old producers.

| Primary | Path | Git blob | Bytes | SHA-256 |
|---|---|---|---:|---|
| P | results/R133-supplement-actual-moving-root-parametrix-and-scalar-finite-part.md | 11250cbb5f9921fdaa70791b6095c306e16bc5d7 | 35230 | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |
| I | results/R133-supplement-original-primitive-on-actual-Airy-amplitudes-and-exact-mean.md | ddc62b4539d640a950c2005505e08695f80910e7 | 14772 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| O | results/R133-supplement-ordered-scalar-root-operator-and-one-gain-radial-remainder.md | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |
| Original free Taylor source | scripts/fourfold_codazzi_old_rho_first_Airy_Taylor_extension.py | 354308bc385a77e17fa6d438e4fc669029c120fb | 53507 | 42048094f7c5e0ba3b83f10e9e6fcbc5cd4c5b3d67057f69241409a5a4be87a1 |
| Original whole free-radius source | scripts/fourfold_codazzi_whole_physical_root_piece_first_Airy_sources.py | 327ecef0f265b88be9789212b4044afde9a28f22 | 51126 | 66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81 |

The original successful radius-stage evidence is in run 43669106351/1, under notes/whole_physical_root_piece_first_Airy_sources_ci/run-43669106351-1/consumers/stages/complete-radius-budget-9-1000000.json.gz; it has 20924 bytes and SHA-256 8b31b1c0030f892ec763d32ecf7b4968d468c5f93b30bbfe7408d6bf0b4892d5. The wrapper's separate old formatter failure is not a mathematical failure of that stage.

TN, TC, AW and the selected-family B/PF statements are consumed in their published exact versions. A future manifest must pin the specific successful scalar receipts it actually reads; this analytic statement does not guess their later file hashes.
