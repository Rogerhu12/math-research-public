# R133 supplement: exact root derivative of the first Airy amplitude

**Status.** Analytic identity for the same actual repaired family and the same original first Airy transport. No new numerical enclosure, source computation, phase flow, or inverse test is performed. This supplement fills the $Da_1$ identity left independent in RD.10; it does not prove the complete stable-trace gate of RD.26.

## RDA1. Frozen definitions and same domain

Use the actual repaired real family $|\delta|\le10^{-8}$, its original intrinsic parameter, and its analytic root piece, exactly as in RD.1. All derivatives have the original outward physical orientation. Set
$$
 D=\partial_r-d\partial_\phi,\qquad
 K(r_*)=0,\qquad k_1=K_r(r_*)>0,\qquad
 \eta_*=-\gamma_*m_*>0,\qquad \lambda_*^3=\eta_*^2k_1.
 \tag{RDA.1}
$$
The functions $\eta,\beta,K$ are radial. Here $\beta$ is the coefficient denoted $b$ in L and O. The state variables $u,v$ include their original full means. In particular, no nonlinear PDE identity for the repaired reference is assumed.

The original circle has period $\pi/2$, normalized angular measure, and physical Fourier frequencies $4j$. Write $P=1-\Pi$, $I=\partial_\phi^{-1}P$, $P_H=1_{\{|j|\ge97\}}$, $P_\epsilon=1_{\{\operatorname{sgn}j=\epsilon,\ |j|\ge97\}}$, and $N e_j=4|j|e_j$ on $P_H$. The independent physical mean coordinates receive no inverse power of $N$.

The following original complete texts fix the coefficient and transport conventions.

| Text | Original equations used | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| [RD](R133-supplement-exact-leading-root-derivative-and-complete-stable-trace-gate.md) | RD.1--10, RD.14--20 | 24b3523585bdfe9f1d96b57e3ca2e4f0727fd2d4 | 17725 | 34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f |
| [L](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md) | L.1--6 and L.22 | 2451ca1c639f04dd69de5c01ff25e59c65a6abb3 | 15780 | a798e93d73aa64115cb43313985054e0d682a41fd1393f4efea4704301699e3a |
| [I](R133-supplement-original-primitive-on-actual-Airy-amplitudes-and-exact-mean.md) | I.18--19 | ddc62b4539d640a950c2005505e08695f80910e7 | 14772 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| [P](R133-supplement-actual-moving-root-parametrix-and-scalar-finite-part.md) | P.7--8, original root conditions | 11250cbb5f9921fdaa70791b6095c306e16bc5d7 | 35230 | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |
| [O](R133-supplement-ordered-scalar-root-operator-and-one-gain-radial-remainder.md) | O.2 and the ordered degree-zero operator | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |

Below $b_{0,\epsilon}^{\rm Airy}$ is the second leading Airy amplitude. It is distinct from the local coefficient $b_{\rm op}$ of the operator $B_{\rm op}$. The letter $\ell=-2\beta uv$ denotes the coefficient of the original first-order operator; it is not an interval length.

## RDA2. The second canonical derivative of the leading second amplitude

At the same root use the original canonical coordinates $(T,X)$ and write $\tau=r-r_*$. RD.6 gives
$$
 T=\lambda_*\tau+t_2(\phi)\tau^2+O(\tau^3),
 \qquad
 (t_2)_\phi=\frac{2\lambda_*}{5}d_{\phi\phi,*},
 \qquad
 X_\phi(r_*,\phi)=1,\quad DX(r_*,\phi)=0.
 \tag{RDA.2}
$$
The leading scalar $G$ and both amplitudes are the exact functions of L.22:
$$
 a_0=G(X_\phi^2-TT_\phi^2),\qquad
 b_{0,\epsilon}^{\rm Airy}=-2i\epsilon G X_\phi T_\phi,
 \qquad G(r_*,\phi)=1.
 \tag{RDA.3}
$$
The last equality follows also from the original $a_0(0,X)=1$ and $X_\phi=1$. Because $\lambda_*$ is radial,
$$
 T_\phi=(t_2)_\phi\tau^2+O(\tau^3).
 \tag{RDA.4}
$$
The analytic inverse coordinate map has $\tau=T/\lambda_*+O(T^2)$ and $\phi=X+O(T)$. Thus the coefficient of $T^2$ at fixed $X$ is determined exactly:
$$
 b_{0,\epsilon}^{\rm Airy}(T,X)
   =-\frac{2i\epsilon}{\lambda_*^2}(t_2)_\phi(X)T^2+O(T^3).
 \tag{RDA.5}
$$
Consequently
$$
 \boxed{\left.\partial_T^2 b_{0,\epsilon}^{\rm Airy}\right|_{T=0}
       =-\frac{4i\epsilon}{\lambda_*^2}(t_2)_\phi
       =-\frac{8i\epsilon}{5\lambda_*}d_{\phi\phi,*}.}
 \tag{RDA.6}
$$
These are derivatives of the actual analytic coefficient, at fixed canonical $X$. They are not derivatives of a saved error bound. In particular $b_0=Db_0=0$ at the root, while its displayed second canonical derivative is retained.

## RDA3. The complete original first forcing at the root

The actual degree-zero operator in L.5 is
$$
 {\cal L}_0w
 =\mu_{\rm can}^{-1}
 \left[(D^2+\eta^2K\partial_\phi^2-T_0D)w
          +V_0w-\vartheta H^{-1}H_Dw\right],
 \qquad (F_b,F_a)=-{\cal L}_0(a_0,b_0^{\rm Airy}).
 \tag{RDA.7}
$$
Here $\mu_{\rm can}$ denotes the normalization factor called $\mu$ in L.5; it is not the mean of a return-map coefficient. At the root,
$$
 \mu_{\rm can,*}=\lambda_*^2,\qquad
 H_*=i\epsilon\,{\rm Id},\qquad
 (H_D)_*=\lambda_*\begin{pmatrix}0&0\\1&0\end{pmatrix},
 \qquad
 (H^{-1}H_D)_*=-i\epsilon\lambda_*
                       \begin{pmatrix}0&0\\1&0\end{pmatrix}.
 \tag{RDA.8}
$$
The order in $H^{-1}H_D$ is the original one. Acting on $(a_0,b_0)_*=(1,0)$, the second component of (RDA.7) therefore gives
$$
 F_{a,\epsilon,*}
  =-\left.\partial_T^2b_{0,\epsilon}^{\rm Airy}\right|_*
       -\frac{i\epsilon}{\lambda_*}\vartheta_* .
 \tag{RDA.9}
$$
For example, $D^2b_0=\lambda_*^2(b_0)_{TT}$ at the root since all first derivatives of $b_0=O(T^2)$ vanish there. The terms $T_0Db_0$, $V_0b_0$, and $K\partial_\phi^2b_0$ vanish as values. None of their radial derivatives is being discarded.

The second transport row of I.19 is
$$
 {\cal T}_{\epsilon,1}(a,b)
    =2a_T+2i\epsilon T b_X+l_{\rm can}a
                                   +i\epsilon T^2m_{\rm can}b.
 \tag{RDA.10}
$$
Its original first-order root condition is $a_{1,\epsilon}(0,X)=0$. Hence
$2(a_{1,\epsilon})_T(0,X)=F_{a,\epsilon,*}$. Since $DT=\lambda_*$ and $DX=0$,
$$
 \boxed{Da_{1,\epsilon,*}
    =i\epsilon\left(\frac45d_{\phi\phi,*}
                                   -\frac12\vartheta_*\right).}
 \tag{RDA.11}
$$

The coefficient $\vartheta$ in (RDA.7)--(RDA.11) is the complete one from L.4. It includes the degree-zero contribution of the original one-gain radial term. Replacing it by a truncated local forcing would change the identity.

## RDA4. Reduction to one radial derivative and two angular derivatives

The original coefficients are
$$
 \ell=-2\beta uv,\qquad e=-\beta(1+3u^2+Kv^2),\qquad
 r_Q=D\ell+\eta e_\phi-2\beta\eta u_\phi u
                                  -\ell(\eta_r/\eta+d_\phi),
 \qquad
 \vartheta=r_Q/\eta-2\beta Kvv_\phi .
 \tag{RDA.12}
$$
At $K=0$, radiality of $\eta$ and $\beta$ gives
$$
 \vartheta_*
   =D(\ell/\eta)_*-(\ell/\eta)_*d_{\phi,*}
                                  -8\beta_*u_*u_{\phi,*}.
 \tag{RDA.13}
$$
The original complete drift retains the mean:
$$
 d_{\phi,*}=-\beta_*(u_*^2-\langle u_*^2\rangle),
 \qquad d_{\phi\phi,*}=-2\beta_*u_*u_{\phi,*}.
 \tag{RDA.14}
$$
Combining these equalities proves the exact low-derivative form
$$
 \boxed{\vartheta_*
     =D(\ell/\eta)_*-(\ell/\eta)_*d_{\phi,*}
                                      +4d_{\phi\phi,*},}
 \tag{RDA.15}
$$
$$
 \boxed{Da_{1,\epsilon,*}=-i\epsilon\,{\cal R}_*,\qquad
 {\cal R}_*=\frac65d_{\phi\phi,*}
          +\frac12D(\ell/\eta)_*
          -\frac12(\ell/\eta)_*d_{\phi,*}.}
 \tag{RDA.16}
$$
Equivalently, using only the actual state and its drift derivatives,
$$
 \begin{split}
 {\cal R}_*={}&\frac65d_{\phi\phi,*}
  -\left(\frac{\beta_r}{\eta_*}
              -\frac{\beta_*\eta_r}{\eta_*^2}\right)u_*v_*\\
 &-\frac{\beta_*}{\eta_*}
       \big((Du)_*v_*+u_*(Dv)_*\big)
  +\frac{\beta_*}{\eta_*}u_*v_*d_{\phi,*}.
 \end{split}
 \tag{RDA.17}
$$
In particular $\mathcal R_*$ is real for every real member of the same repaired family. It is independent of $\epsilon$ and of the input frequency. The canonical quantities $l_{{\rm can},X}$ and $m_{\rm can}$ are no longer needed for this exact root value.

For the genuine amplitudes used in RD.14--15,
$a_1^V=a_1+{\cal B}_nT b_0$. Because $b_0=O(T^2)$, the correction has zero first root derivative. Thus
$$
                         Da_{1,\epsilon,*}^V=Da_{1,\epsilon,*}.
 \tag{RDA.18}
$$
This does not remove $\mathcal B_n$, $\mathcal B'_n$, $V_n$, or the true nonzero $\beta_n$ from the other root products in RD.

## RDA5. A complete prospective scalar bound and the signed operator

All quantities in the following paragraph are prospective bounds for the exact same root functions. Suppose
$$
 \begin{gathered}
 |u_*|\le U,\quad |v_*|\le V,\quad |(Du)_*|\le U_D,\quad |(Dv)_*|\le V_D,\\
 |\beta_*|\le B,\quad |\beta_r(r_*)|\le B_r,\quad
 \eta_*\ge\eta_->0,\quad |\eta_r(r_*)|\le E_r,\quad
 \|d_{\phi,*}\|_\infty\le d_1,\quad
 \|d_{\phi\phi,*}\|_\infty\le d_2 .
 \end{gathered}
 \tag{RDA.19}
$$
These must cover the declared actual real parameter interval and full angular circle, including the mean of $v$. Then valid complete upper bounds are
$$
 L_0=\frac{2BUV}{\eta_-},\qquad
 L_1=\frac{2B_rUV+2B(U_DV+UV_D)}{\eta_-}
                       +\frac{2BUVE_r}{\eta_-^2},
 \qquad
 R_a=\frac65d_2+\frac12(L_1+L_0d_1).
 \tag{RDA.20}
$$
Here $L_0\ge\|\ell/\eta\|_\infty$, $L_1\ge\|D(\ell/\eta)\|_\infty$, and $R_a\ge\|{\cal R}_*\|_\infty$. If only outward derivatives are supplied, one may first use
$U_D\le U_r+\|d_*\|_\infty U_\phi$ and
$V_D\le V_r+\|d_*\|_\infty V_\phi$ with complete bounds on those same functions. No unproved PDE substitution is involved.

Let $Z=P_+-P_-$ on the original high input. The complete signed multiplier of RD.16 has the exact factorization
$$
 \mathsf A_r
   =\sum_{\epsilon=\pm1}M_{Da_{1,\epsilon,*}}P_\epsilon
   =-iM_{{\cal R}_*}Z,\qquad
              \|\mathsf A_r\|_{L^2\to L^2}\le R_a .
 \tag{RDA.21}
$$
There is no additional factor from summing the two signed inputs: $Z$ is an isometry on $P_HL^2$. Output projection $P$ remains where it appears in RD.19; multiplication by $\mathcal R_*$ is not asserted to preserve the mean.

With the original input diagonal $D_A$ of RD.11 and any complete $A_{\max}\ge\sup_n|A_n|$, the second term of RD.19 consequently satisfies
$$
       \|P\mathsf A_rD_AN^{-1}\|_{L^2\to L^2}
                    \le\frac{R_a A_{\max}}{388}.
 \tag{RDA.22}
$$
The diagonal is still on the right. This estimate neither commutes a diagonal through a multiplier nor assigns an inverse power to a physical mean coordinate.

## RDA6. Exact scope of this addition

Equations (RDA.6), (RDA.11), and (RDA.16)--(RDA.18) are identities of the original leading and first amplitudes with their original root gauge. They use the full first forcing, both signed input sectors, the original analytic canonical map, and the exact mean-containing drift.

Equations (RDA.19)--(RDA.22) are a minimal scalar-consumer contract, not an actual new numerical receipt. They may replace a generic bound for the same $\mathsf A_r$ contribution after all stated complete inputs are independently paid. The other terms of RD.19 remain: $a_*$, $\mathsf B$, $\mathsf B_r$, the potential diagonals, the explicit positive projected-mean rank, and the full inverse $J$. The physical stable row keeps the root normalization of RD.21 without an additional $n^{1/6}$ factor.

All supplied-head, ordinary-source, jump, low, physical-mean, and independent reference ports remain independent. No complete incoming inverse, actual finite-border inverse, stable-trace injectivity, or nonlinear solution follows from this root identity alone.
