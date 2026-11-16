# R133 supplement: exact leading second root jet and the first Airy b value

2026-11-16, visible-exact / root.

**Proved analytic identities, with no new numerical evaluation.** On the same analytic root piece as [RD](R133-supplement-exact-leading-root-derivative-and-complete-stable-trace-gate.md), the cubic coefficient of the genuine fold gives the leading amplitude's second radial derivative and then the first free Airy b amplitude at the root. The two frequency signs share that b amplitude. These are new inputs to RD's complete stable-trace gate; no numerical pass is asserted.

All derivatives use the original outward coordinate r. The repaired family, intrinsic parameter, full physical means, positive potential and exact primitive/inverse remainders retain their original definitions. No nonlinear PDE equation is assumed for the repaired reference.

## RBJ1. Original identities and the root convention

Use L.4–6 and L.22–23 of [the explicit first-forcing theorem](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md), I.19–21 for actual analytic transport, G.2 for the genuine fold, O.19 for the full radial mean coefficient, and RD.1–16 for root normalization.

| Primary | Complete Git blob | Bytes | SHA256 |
|---|---|---:|---|
| L, explicit first forcing | 2451ca1c639f04dd69de5c01ff25e59c65a6abb3 | 15780 | a798e93d73aa64115cb43313985054e0d682a41fd1393f4efea4704301699e3a |
| I, original primitive and actual amplitudes | ddc62b4539d640a950c2005505e08695f80910e7 | 14772 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| G, genuine fold and amplitudes | 8fa0d675d454a19451f946ed8f8a8eead7145089 | 22688 | c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e |
| O, ordered complete scalar operator | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |
| RD, complete stable root trace gate | 24b3523585bdfe9f1d96b57e3ca2e4f0727fd2d4 | 17725 | 34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f |

On the same real root circle set
$$
 \tau=r-r_*,\quad D=\partial_r-d\partial_\phi,\quad
 k_j=\partial_r^jK(r_*),\quad
 \lambda^3=\eta_*^2k_1,\quad \eta_*>0,\quad k_1>0,\quad\lambda>0 .
 \tag{RBJ.1}
$$
The coefficients eta and K are independent of the angle. Use beta for the intrinsic coefficient called b in L, distinct from the Airy amplitudes. Every unmarked coefficient in a root formula below is evaluated at the same root. Define
$$
 e_1=\frac{\eta_r}{\eta_*},\quad e_2=\frac{\eta_{rr}}{\eta_*},
 \qquad c_2=\frac{k_2}{2k_1},\quad c_3=\frac{k_3}{6k_1},
 \qquad p=d_\phi .
 \tag{RBJ.2}
$$
Here e2 is an ordinary second derivative ratio, not the second derivative of log eta. The displayed factorials belong to the ordinary Taylor coefficients of K. No derivative of a saved value enclosure is taken.

## RBJ2. The exact cubic fold coefficient

The actual identities are
$$
 DT=QX_\phi,\quad DX=-QT T_\phi,\quad \eta^2K=Q^2T,
 \quad T(r_*,\phi)=0,\quad X(r_*,\phi)=\phi .
 \tag{RBJ.3}
$$
Write the genuine analytic expansions
$$
 T=\lambda\tau+\lambda t\,\tau^2+\lambda s\,\tau^3+O(\tau^4),
 \qquad Q=\lambda(1+q_1\tau+q_2\tau^2)+O(\tau^3).
 \tag{RBJ.4}
$$
Since lambda is angle independent, $T_\phi=O(\tau^2)$ and $DX=O(\tau^3)$. Therefore $X_r=dX_\phi+O(\tau^3)$ gives
$$
 X_\phi=1+p\tau+x_2\tau^2+O(\tau^3),\qquad
 x_2=\frac{d_{r\phi}+p^2+d\,d_{\phi\phi}}2 .
 \tag{RBJ.5}
$$
This is the ordinary r expansion; its second coefficient is not Dp/2.

Expansion of the third identity in (RBJ.3), on its actual positive root branch, gives
$$
 \begin{split}
 q_1&=e_1+(c_2-t)/2,\\
 q_2&=(e_2+c_3-s)/2+e_1(c_2-t)/2
          +3t^2/8-c_2t/4-c_2^2/8 .
 \end{split}
 \tag{RBJ.6}
$$
In particular the second coefficient of eta squared divided by eta-star squared is $e_1^2+e_2$; the $e_1^2$ cancels in its square root. This is an exact coefficient identity, never a subtraction of independent upper bounds.

Matching the first identity of (RBJ.3) gives
$$
 2t=q_1+p,\qquad 3s-dt_\phi=q_2+q_1p+x_2.
 \tag{RBJ.7}
$$
It follows that
$$
 \boxed{t=\frac{2e_1+c_2+2p}{5},\qquad t_\phi=\frac25d_{\phi\phi},}
 \tag{RBJ.8}
$$
and
$$
 \boxed{\displaystyle
 s=\frac27\left[
 dt_\phi+\frac{e_2+c_3}{2}+\frac{e_1(c_2-t)}2
 +\frac{3t^2}{8}-\frac{c_2t}{4}-\frac{c_2^2}{8}
 +q_1p+x_2\right].}
 \tag{RBJ.9}
$$
Only the displayed genuine drift jets, eta through order two and K through order three are used. The coordinate is the original fold, not a separately chosen Airy model.

## RBJ3. The leading second derivative, including the complete mean

Put
$$
 S=u^2+Kv^2,\qquad M(r)=\beta(r)\langle S(r,\cdot)\rangle .
 \tag{RBJ.10}
$$
The original L.22 amplitudes are
$$
 a_0=G(X_\phi^2-TT_\phi^2),\qquad
 b_{0,\epsilon}=-2i\epsilon GX_\phi T_\phi .
 \tag{RBJ.11}
$$
Since $T=-\rho A^{2/3}$ and $k=-K/\rho$, the same G satisfies locally
$$
 \log G=\mathrm{constant}+\frac14\log(T/K)
                      -2\int_{r_*}^r M(q)\,dq .
 \tag{RBJ.12}
$$
The quotient T/K has its analytic nonzero extension at the root and the original branch. Its root value lambda/k1 is independent of phi; the constant fixes G at the root to one.

The term $TT_\phi^2=O(\tau^5)$ contributes to neither of the first two root jets. The exact commutator $[D,\partial_\phi]=d_\phi\partial_\phi$ gives
$$
 D\log X_\phi=p+O(\tau^3),\qquad
 D^2\log X_\phi\big|_*=Dp=d_{r\phi}-d\,d_{\phi\phi}.
 \tag{RBJ.13}
$$
Expansion of the actual quotient logarithm, applying both copies of D, gives
$$
 \begin{split}
 D\log(T/K)\big|_*&=t-c_2,\\
 D^2\log(T/K)\big|_*&=
          2s-t^2-2c_3+c_2^2-2dt_\phi .
 \end{split}
 \tag{RBJ.14}
$$
The final drift term has factor two; differentiating only the first radial coefficient would omit one contribution.

Define the actual leading first derivative
$$
 A_0:=Da_0\big|_*=(t-c_2)/4+2p-2M_* .
 \tag{RBJ.15}
$$
This is exactly RD.9. The next derivative is
$$
 \boxed{\displaystyle
 C_0:=D^2a_0\big|_*=
 A_0^2+\frac{2s-t^2-2c_3+c_2^2-2dt_\phi}{4}
                   +2Dp-2M_r .}
 \tag{RBJ.16}
$$
The mean derivative retains all original terms:
$$
 M_r=\beta_r\langle u^2\rangle+
          \beta\{2\langle u u_r\rangle+k_1\langle v^2\rangle\}.
 \tag{RBJ.17}
$$
The term with $k_1\langle v^2\rangle$ survives even though K itself vanishes at the root. These are actual reference derivatives on its analytic root piece; no background PDE is used to replace ur or the mean.

## RBJ4. Exact sign structure of the free first forcing

With $x=X_\phi$, $y=T_\phi$, define
$$
 {\cal K}=\begin{pmatrix}0&T\\1&0\end{pmatrix},\quad
 H=i\epsilon x\,\mathrm{Id}+y{\cal K},\quad
 H_D=i\epsilon DX\,\mathrm{Id}+DT\,{\cal K}.
 \tag{RBJ.18}
$$
The principal identities and $ {\cal K}^2=T\,\mathrm{Id}$ give
$$
 H(-i\epsilon Q{\cal K})
      =Qx{\cal K}-i\epsilon QTy\,\mathrm{Id}=H_D.
$$
Thus, on the whole common fold neighborhood,
$$
                  \boxed{H^{-1}H_D=-i\epsilon Q{\cal K}.}
 \tag{RBJ.19}
$$
The original ordered term in L.5 is consequently $+i\epsilon\vartheta Q{\cal K}w$. It remains the complete degree-zero contribution of the one-gain radial operator.

For real coefficients, a0 is real and independent of epsilon, while b0 is i-epsilon times a real function. The real scalar differential part of L.5 and (RBJ.19) therefore give
$$
                 F_{b,\epsilon}=F_b,\qquad
                 F_{a,\epsilon}=i\epsilon F_a^{\rm real}.
 \tag{RBJ.20}
$$
These are the original free sources L.6. They precede the potential-dependent change to genuine amplitudes.

Substitution $a_{1,\epsilon}=i\epsilon a_1^{\rm real}$ and $b_{1,\epsilon}=b_1^{\rm real}$ reduces the two equations I.19 to the same real forced system for both signs. The common trace $a_1(0,X)=0$ and analytic uniqueness in I.20–21 imply
$$
       b_{1,+}=b_{1,-}=:b_1,\qquad
       a_{1,+}=-a_{1,-}=i\,a_1^{\rm real}.
 \tag{RBJ.21}
$$
The first equality holds in a common neighborhood, so it also holds for the actual D derivative. The two oscillatory branches remain distinct.

## RBJ5. The exact b1 value and the derivative still required

The original root coefficients are
$$
 \begin{split}
 T_{0,*}&=e_1-4\beta\langle u^2\rangle+5p,\\
 t_{Q,*}&=e_1+p-\beta(1+3u^2),\\
 V_{0,*}&=t_{Q,*}\beta(1-u^2)-\beta_r(1-u^2)
                             +2\beta u\,Du+3\beta k_1v^2 .
 \end{split}
 \tag{RBJ.22}
$$
The last identity evaluates L.4 after differentiating the complete original coefficient $b_{\rm op}=\beta(1-u^2-3Kv^2)$. Its last positive term is not removed by setting K to zero too early.

The first component of $i\epsilon\vartheta Q{\cal K}(a_0,b_0)^t$ is $i\epsilon\vartheta QT b_0=O(\tau^3)$. It vanishes at the root in this component. The angular second-order coefficient also has its exact factor K, while the original normalization gives $\mu_*=\lambda^2$. L.5–6 and the first transport equation at T=0 now give
$$
 \boxed{\displaystyle
 b_1(r_*,\phi)=F_b(r_*,\phi)
       =-\frac{C_0-T_{0,*}A_0+V_{0,*}}{\lambda^2}.}
 \tag{RBJ.23}
$$
This component-specific value does not delete the second forcing component, the nearby one-gain term, or any exact remainder of the full operator.

Differentiating the actual forced transport equation gives
$$
        3(b_1)_T(0,X)+l_*b_1(0,X)=(F_b)_T(0,X),
$$
because the common zero trace gives $(a_1)_X(0,X)=0$. Since DX vanishes at the root and $\lambda l_*=2t-T_{0,*}$,
$$
 \boxed{\displaystyle
 Db_1\big|_*=
       \{DF_b\big|_*-(2t-T_{0,*})b_1\big|_*\}/3 .}
 \tag{RBJ.24}
$$
Here Fb is the actual neighborhood forcing L.5–6. The root-only simplification (RBJ.23) cannot itself be differentiated in r to manufacture DFb. A bound obtained through the differentiated forcing still requires the genuine third leading derivative and every differentiated coefficient; no such new numerical bound is asserted.

For the actual potential correction retained in RD.15,
$$
 2T{\cal B}_n'+{\cal B}_n=V_n,
$$
differentiation of this valid neighborhood identity gives
$$
 {\cal B}_n(0)=V_n(0),\qquad {\cal B}_n'(0)=V_n'(0)/3.
 \tag{RBJ.25}
$$
Thus the same ordered genuine-amplitude formulas are
$$
 b_1^V\big|_*=b_1+V_n(0),\qquad
 Db_1^V\big|_*=Db_1+\lambda V_n'(0)/3+V_n(0)A_0 .
 \tag{RBJ.26}
$$
The true n-dependent potential is kept; it is not replaced by its radial model.

## RBJ6. Complete operator use and the unpaid gates

For RD's high input projection $P_H=P_++P_-$, (RBJ.21) implies
$$
 {\mathsf B}=M_{b_1}P_H,\qquad
 {\mathsf B}_r=M_{Db_1}P_H,\qquad
 {\mathsf A}_r=M_{D a_1^{\rm real}}\,i(P_+-P_-).
 \tag{RBJ.27}
$$
The displayed projection and sign factors have ordinary L2 norm one on their high input. A complete pointwise root supremum of each multiplier therefore gives its whole ordinary L2 operator bound, without an additional factor two or square-root two. This does not authorize sampled maxima or a free negative Sobolev bound.

All multiplier output frequencies, external projections, RD's positive mean-rank term, original J and its primitive, low intermediate outputs, genuine potential, independent physical means and retained finite rows remain. The full primitive and inverse residuals keep their original fees.

A new numerical consumer may evaluate (RBJ.9), (RBJ.16), (RBJ.23) and the complete forcing-derivative identity using original immutable coefficient jets and uniform angular bounds. It must run in this public repository's Actions. Neither the completed whole-domain first forcing nor an old root/inverse calculation may be rerun.

This supplement supplies no new numerical multiplier bound, stable coercivity pass, physical incoming inverse, finite Schur inverse, nonlinear core solution or final global surface.
