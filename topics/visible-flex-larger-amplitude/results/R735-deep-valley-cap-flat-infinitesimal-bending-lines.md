# R735 — An actual cap-flat infinitesimal bending line at every higher angular mode of the fixed deep-valley metric

2026-11-28. **Proved.** For every integer $m\ge2$ the precise R690 deep-valley tail, with its actual fixed circular cap, admits a nonzero real radial solution of the linearized isometry equations in mode $m$. All its derivatives vanish at the cap. In either angular parity its cap-vanishing solution space has dimension exactly one. The two angular phases give two independent real bending fields per $m$; different frequencies are independent. These are classical infinitesimal isometries of a one-cap annular piece of the actual axisymmetric reference. They continue to every compact interior segment with $a>0$ and positive vertical meridional speed. This is a positive existence conclusion stronger than failure of R690's former sufficient uniqueness test. It neither integrates the bending to finite amplitude nor imposes the second cap or the prescribed Fejér core.

## 1. Actual fixed scalar and exact reduction to a positive canonical system

Let $u=S-s$, $d_0$ be the original positive binary out width, $a=a_{\rm deep}(S-u)$, and take $0<u<d_0/8$. Set
$$
 v=(d_0/u)^4,\quad B_0=(3/2)d_0,\quad
 \beta=B_0\exp[-\sqrt v-v(1+\sin v)],\quad
 c=\sin\beta,\quad b=a_s=-\cos\beta,\quad b_+=-b=a_u.
 \tag{1}
$$
These are [R690, (3)–(5)](R690-quasimonotone-tail-and-deep-valley-input.md) without cutting off any phase. In particular $a(0)=R>0$ when using $u$ as argument, $c>0$ for $u>0$, and $b_+$ tends to one. Decrease the upper $u$ endpoint if necessary so that $R/2<a<2R$ and $1/2<b_+\le1$. Here $a(0)$ in the backward coordinate is not the physical core value of $a(s)$.

Use [R669, §3](R669-same-g-axisymmetric-tail-linear-uniqueness-and-endpoint-defect.md)'s cylindrical components of a linearized field about $F_*(s,\theta)=a(s)e_r(\theta)+z_*(s)e_z$. For a positive integer $m\ge2$ write the complex angular coefficients as radial $mV$, tangential $iV$, vertical $W$ with $V,W$ real, and multiply by $e^{im\theta}$. Taking real or imaginary parts later gives the two parities. The radial coefficient is exactly $-im$ times the tangential one, so the angular–angular Gram variation vanishes. The other two vanishing Gram equations in the original $s$ coordinate become
$$
 V_s=-(m^2-1)(b/a)V-(mc/a)W,\qquad W_s=-(mb/c)V_s .
 \tag{2}
$$
All divisions here are on the open tail. Equivalently, in $u$ the first equation is $V_u=-(m^2-1)(b_+/a)V+(mc/a)W$, and $W_u=(m b_+/c)V_u$.

Set $y=a^{m^2-1}V$, $z=-a^{-m^2}W$. The minus sign is convenient because $v$ **increases toward the cap**. With $j(v)=|du/dv|=d_0/(4v^{5/4})$, direct differentiation of (2) gives
$$
 y_v=\mathcal A(v)\,z,\qquad z_v=-\mathcal B(v)\,y,\qquad
 \mathcal A=j\,m a^{2m^2-2}c,\quad
 \mathcal B=j\,m(m^2-1)b_+^2 a^{-2m^2}/c .
 \tag{3}
$$
Both coefficients are strictly positive. Their product is $j^2m^2(m^2-1)b_+^2/a^2$. The trace of the system matrix is zero, so every fundamental transfer matrix has determinant one. All comparison constants below may depend on the fixed $m$ and original inputs. We need no uniform-in-$m$ constants to establish each individual mode or the independence of their finite sums.

## 2. Controlled exact transfers on the two half periods

Use the exact phase points $v_n=2\pi n+\pi/2$ and $w_n=v_n+\pi$. At $v_n$, $c$ is near its deep minimum; at $w_n$ it is near a peak. Write $I_n^+=[v_n,w_n]$ and $I_n^-=[w_n,v_{n+1}]$. On either half $j=O(n^{-5/4})$. Let $F(v)=\sqrt v+v(1+\sin v)$, so $c$ is between $(B_0/2)e^{-F}$ and $B_0e^{-F}$ for all large $n$. On $I_n^-$ the function $F$ is nondecreasing. On $I_n^+$, for $x\le y$, the decreasing sine gives
$$
 F(y)-F(x)\le\sqrt y-\sqrt x+2(y-x)\le1+2\pi
$$
for sufficiently large $n$. Boundedness of $a,1/a,b_+$ and the comparisons in (1) therefore give the **oppositely ordered** estimates
$$
 \begin{array}{ll}
 \mathcal B(y)\mathcal A(x)\le C n^{-5/2} &(x\le y,\ x,y\in I_n^+),\\
 \mathcal A(y)\mathcal B(x)\le C n^{-5/2} &(x\le y,\ x,y\in I_n^-).
 \end{array}
 \tag{4}
$$
The other order can be extremely large and is retained below.

For an interval $I$ write $A_I=\int_I\mathcal A$ and $B_I=\int_I\mathcal B$. Both are strictly positive for nonzero length. For the increasing-$c$ half, let $M$ transfer $(y,z)$ from its beginning to its end. Integrating (3) twice gives
$$
 z(r)=z_0-y_0 B_{[v_n,r]}
 -\int_{v_n}^r\mathcal B(y)\int_{v_n}^y\mathcal A(x)z(x)\,dx\,dy .
$$
By (4) the double integral, viewed as an operator on bounded $z$, has norm at most $\epsilon_n=C\pi^2 n^{-5/2}$. For input $(0,1)$ this shows $z=1+O(\epsilon_n)$ uniformly and $M_{12}=A_I(1+O(\epsilon_n))$. For input $(1,0)$ the error in $z$ at its endpoint relative to $-B_I$ is $O(\epsilon_n)B_I$ by the same norm bound and the inequality $B_{[v_n,r]}\le B_I$. Thus
$$
 M_{22}=1+O(\epsilon_n),\quad
 M_{12}=A_I(1+O(\epsilon_n)),\quad
 M_{21}=-B_I(1+O(\epsilon_n)).
 \tag{5}
$$
These relative estimates use the true positive integrals, even if extremely small or large. They hold identically with $I$ replaced by any first portion of that half. On the decreasing-$c$ half integrate twice for $y$, using the second line of (4). Starting with $(1,0)$ gives $y=1+O(\epsilon_n)$ and endpoint $M_{21}=-B_I(1+O(\epsilon_n))$. Starting with $(0,1)$ gives $M_{12}=A_I(1+O(\epsilon_n))$. Thus (5) holds with $M_{11}=1+O(\epsilon_n)$ replacing the claim about $M_{22}$, again for every first portion.

For $p,q\ge0$ abbreviate the matrices
$$
 T(p)=\begin{pmatrix}1&p\\0&1\end{pmatrix},\qquad
 L(-q)=\begin{pmatrix}1&0\\-q&1\end{pmatrix}.
$$
The determinant identity now yields the **exact** factorizations
$$
 M_n^+=T(p_n^+)\operatorname{diag}(1/d_n,d_n)L(-q_n^+),\qquad
 M_n^-=L(-q_n^-)\operatorname{diag}(e_n,1/e_n)T(p_n^-).
 \tag{6}
$$
Here $d_n=(M_n^+)_{22}$ and $e_n=(M_n^-)_{11}$ are $1+O(\epsilon_n)>0$. In each half $p$ is $M_{12}$ divided by the specified diagonal and $q$ is $-M_{21}$ divided by it. Hence $p=(1+O(\epsilon_n))A_I>0$, $q=(1+O(\epsilon_n))B_I>0$ for large $n$. The omitted diagonal entry follows exactly from the determinant, without a perturbative assumption on $A_I B_I$. The same factorization on every initial portion (allowing $p=q=0$ for length zero) will control what happens between phase endpoints.

## 3. Phase concentration and the stable scalar recurrence

For all sufficiently large $n$, on a window of one-sided length $w_n^{-1/2}$ against $w_n$ in either adjacent half, $v(1+\sin v)$ is bounded by an absolute constant: $1+\sin(w_n+\delta)=1-\cos\delta\le\delta^2/2$. Consequently each relevant peak half has
$$
 A_I\ \ge c_1 n^{-7/4}\exp(-C_1\sqrt n).
$$
Also $A_I\le C_2$ throughout. On a one-sided window of length $v_n^{-1/2}$ beside a valley $v_n$, $1+\sin(v_n+\delta)=1+\cos\delta\ge 2-\delta^2/2$. It follows that $B_I\ge\exp(c_2 n)$ for all sufficiently large $n$ with some $c_2>0$; on each whole half $B_I\le\exp(C_3 n)$ by (1). The bounds apply on the appropriate side of each of the two alternating extrema, with index shifts by one harmless. These window estimates require the actual sine phase in (1); a monotone or bounded-contrast tail does not give this concentration.

Define $X_n=L(-q_n^+)(y(v_n),z(v_n))^T$. Its first component is still $y_n=y(v_n)$; denote the second by $z_n^*$. Combining (6) in order and grouping the elementary factors gives exactly
$$
 X_{n+1}
 =L(-Q_{n+1})\operatorname{diag}(\alpha_n,1/\alpha_n)T(P_n)X_n,\qquad
 Q_{n+1}=q_{n+1}^++q_n^-,\quad
 \alpha_n=e_n/d_n,\quad P_n=d_n^2(p_n^++p_n^-).
 \tag{7}
$$
In particular $1/2<\alpha_n<2$, $P_n>0$, $|\log P_n|=o(n)$, and $Q_{n+1}\ge e^{c n}$ for some $c>0$ at all sufficiently large $n$. All individual $q_n^\pm$ are $\le e^{Cn}$. Equation (7) first gives $y_{n+1}=\alpha_n(y_n+P_n z_n^*)$ and then $z_{n+1}^*=z_n^*/\alpha_n-Q_{n+1}y_{n+1}$. Eliminating the second component gives
$$
 y_{n+2}=-D_{n+1}y_{n+1}-E_{n+1}y_n,
$$
$$
 D_{n+1}=\alpha_{n+1}
 \left(P_{n+1}Q_{n+1}-1-\frac{P_{n+1}}{\alpha_n^2P_n}\right),\qquad
 E_{n+1}=\frac{\alpha_{n+1}P_{n+1}}{\alpha_n P_n}>0.
 \tag{8}
$$
The growing term has logarithm at least $cn-o(n)$, while the subtracted ratio has logarithm $o(n)$. Therefore for a possibly smaller $\sigma>0$ and all large indices $D_n\ge e^{\sigma n}$, $|\log E_n|=o(n)$. We never require the endpoint transfer matrix to be uniformly close in norm to a single shear.

Put $x_n=(-1)^n y_n$. For the recurrence $x_{n+1}=D_n x_n-E_n x_{n-1}$ construct positive stable ratios by the **backward** equation
$$
 \mu_n=\frac{E_n}{D_n-\mu_{n+1}} .
 \tag{9}
$$
For all $n\ge n_0$, (9) maps $[0,1]$ to $(0,e^{-\sigma n/2}]$ and has Lipschitz constant at most $E_n/(D_n-1)^2<1/2$. Starting with $\mu_{N+1}=0$, iterate backward. For each fixed $n$ the effect of any bounded terminal ratio at $N+1$ is at most $\prod_{j=n}^{N}E_j/(D_j-1)^2$, tending to zero. The limits solve (9), and are positive since $\mu_n\ge E_n/D_n>0$. Set $x_{n_0-1}=1$ and $x_n=\mu_n x_{n-1}$. Then (8) holds and
$$
 |y_n|\le C\exp(-c_3 n^2)
 \tag{10}
$$
for some $c_3>0$. These are genuine nonzero values, with alternating signs. Set $z_n^*=(y_{n+1}/\alpha_n-y_n)/P_n$ and $z(v_n)=z_n^*+q_n^+ y_n$. Equations (7),(8) check both first-order component relations, hence the physical ODE solution from the state at $v_{n_0}$ has exactly these states at every subsequent $v_n$. The state is nonzero at its starting phase. Since $1/P_n=e^{o(n)}$ and $q_n^+\le e^{Cn}$, both physical components at the phase points still satisfy $O(e^{-c_4 n^2})$ for some $c_4>0$.

## 4. The solution really extends flat to the cap

Every initial half transfer has norm $\le e^{Cn}$, uniformly in its interior endpoint. Indeed its relevant diagonal stays between $1/2$ and $2$, the two factors in (6) have sizes bounded by the full half integrals as just proved, and the missing diagonal is controlled by their product. Use at most two half transfers to reach any $v\in[v_n,v_{n+1}]$. This proves
$$
 |y(v)|+|z(v)|\le C e^{-c_5 n^2}\quad (v_n\le v\le v_{n+1})
 \tag{11}
$$
for some $c_5>0$. Applying a crude exponential-in-$\sup\mathcal B$ integral estimate here would not suffice; the ordered half-period calculation is needed.

For each fixed derivative order $j$, the physical-$u$ coefficients $m a^{2m^2-2}c$ and $m(m^2-1)b_+^2 a^{-2m^2}/c$ and their first $j$ derivatives are bounded by $e^{C_j n}$ on that cell. To verify this, $u=d_0v^{-1/4}$ turns each $u$ derivative into $-4v^{5/4}/d_0$ times a $v$ derivative. Derivatives of $F(v)$ have polynomial growth; $e^{F(v)}\le e^{Cn}$ and $e^{-F(v)}\le1$. Also $c=\beta(\sin\beta/\beta)$ with the second factor analytic, bounded and bounded away from zero near $\beta=0$. The same estimates hold for its inverse after extracting the explicit factor $1/\beta$. Since $a_u=b_+=\cos\beta$, $a$ is bounded away from zero and its needed derivatives obey the same bounds. Finite products and powers preserve bounds of the displayed form with adjusted constants. By (3) in the physical variable and repeated differentiation, every finite derivative of the state on the punctured tail is a matrix with norm $\le e^{C'_j n}$ times the state there. Equations (10),(11) dominate all such factors. The inverse powers of $u$ grow only polynomially in $n$, so $V=a^{1-m^2}y$, $W=-a^{m^2}z$ and all their derivatives tend to zero faster than every power of $u$. Extending the functions by zero at the cap gives $C^\infty$ flat functions (successive derivatives extend continuously by zero and the fundamental theorem of calculus identifies the derivatives of the extensions).

Taking the real part or the imaginary part of the mode in §1 gives classical real fields with exactly zero linearized Gram on the whole open tail and all jets zero at the rim. They may therefore be adjoined to the zero field on the fixed physical p4 cap, including its marker, with at least $C^2$ regularity. They are not rigid motions: a rigid infinitesimal motion vanishing on an open planar cap is zero everywhere, while the radial state is nonzero. For the same fixed $m$, two cap-vanishing radial states would have constant determinant as functions of $v$, by (3). Their limits at the cap are zero, so that determinant vanishes and ODE uniqueness makes the states proportional. Thus precisely one nonzero radial line is available for each parity, without assuming numerical transfer matrices have found it.

On any compact inward interval with $a>0$ and $c>0$, the regular system (2) extends this line uniquely. The entire old prefix has $|a'|<1$ by FullHold, the Hold extension uses R669's positive vertical branch, and R690 keeps $c>0$ at every interior point of its modified tail. The regularity is read piecewise across the original scalar knots. Those facts give no second boundary equality: the continued bending of the **axisymmetric** reference does not automatically meet an independently prescribed noncircular core, the reflected matching conditions, or the other fixed cap. At $m=0$ the cap-fixed radial solution is trivial by R669; at $m=1$ the $\mathcal B$ equation in (3) makes $z$ constant, so a cap-vanishing solution has $z=y=0$. These statements distinguish the higher-mode bending from ambient infinitesimal translations and rotations.

This proof used the same fixed metric and original infinitely oscillating material tail, not a sequence of varying metrics or a cutoff replacing the deep oscillations. A truncated continued fraction in (9) is a way to approximate the selected line once its half-transfer data are accurately evaluated; the proof gives the truncation-product bound and supplies no unexecuted numerical values. The nonlinear isometric immersion, physically large displacement, two-ended closure and whole-surface reach remain separate. No scientific code or numerical integration was executed for this result.
