# R133 supplement: an exact full-circle subprincipal normalizer and its strong remainder budget

2026-11-15, newton_source.

**Proved analytic result.** The real nonmean first coefficient in Section 5 of [the selected-family root and phase theorem](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md) has an explicit full-circle normalizer. Its inverse is a periodic first-order equation with two retained mean functionals. This removes the need to introduce a further finite cutoff merely to invert this subprincipal normalizer.

The quantitative input is the complete nonmean coefficient in the actual rotation coordinate, measured in $H^3$. No numerical value for this input is inferred from the already certified scalar $\beta_*$ or from a volume-residual bound. The result gives explicit forward, inverse and strong-remainder bounds in terms of this one input and the preceding complete strong remainder. It does not recompute any successful science.

## 1. The exact coefficient, angle and Fourier units

Let the rotation angle have period $\pi/2$, with normalized measure,
$$
 e_j(x)=e^{4ijx},\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 I=\partial_x^{-1}(1-\Pi),\quad \Pi f=\langle f\rangle.
 \tag{CN.1}
$$
The actual principal rotation is $\Omega=\pi\rho_{15}/2$. The already proved principal gap of the selected-family theorem is
$$
 |e^{4ij\Omega}-1|>\frac1{68|j|},\qquad j\ne0.
 \tag{CN.2}
$$
This is the bounded15 target and the physical frequency $4j$. The former bounded7 constant is not used.

Let $c$ be the real complete first coefficient after the true principal angle conjugacy and all already prescribed root, waist and density transformations. Put
$$
 \mu=\langle c\rangle,\qquad v=c-\mu,\qquad
 C=\|v\|_{H^3},\qquad v\in H^3,\quad \langle v\rangle=0.
 \tag{CN.3}
$$
In particular $c$ is not a raw strict-region $\Xi$ at a single radius. It contains the complete first coefficient, including the prescribed root and endpoint contributions, in the same rotation coordinate.

Solve
$$
 w(x-\Omega)-w(x)=v(x),\qquad \langle w\rangle=0.
 \tag{CN.4}
$$
The Fourier formula and (CN.2) give
$$
 w_j=\frac{v_j}{e^{-4ij\Omega}-1},\qquad
 |w_j|\le17(4|j|)|v_j|,\qquad
 p=Iw,\quad |p_j|\le17|v_j|,\quad j\ne0.
 \tag{CN.5}
$$
Both signs are included. Reality of $v$ gives reality of $w,p$. The stated regularity gives $w\in H^2$ and $p\in H^3$; their means are zero.

## 2. Complete weighted Fourier bounds

For $r\ge0$ define
$$
 \|f\|_{\mathcal W_r}
  =\sum_{j\in\mathbb Z}(1+4|j|)^r|f_j|.
 \tag{CN.6}
$$
These are Banach algebra norms, since
$1+|a+b|\le(1+|a|)(1+|b|)$. Also
$$
 \|M_f\|_{H^s\to H^s}\le\|f\|_{\mathcal W_{|s|}}.
 \tag{CN.7}
$$
For negative as well as positive $s$, this follows from
$\Lambda_m/\Lambda_k\le1+4|m-k|$ and its exchanged version, followed by the full convolution inequality. No high-index support is assumed for $f$ or the input.

The following bounds will be used:
$$
\begin{aligned}
 \|v\|_{\mathcal W_0}&\le C/32,&
 \|w\|_{\mathcal W_0}&\le2C,&
 \|w\|_{\mathcal W_{1/3}}&\le4C,\\
 \|w\|_{\mathcal W_{4/3}}&\le51C,&
 \|p\|_{\mathcal W_0}&\le17C/32,&
 \|p\|_{\mathcal W_{4/3}}&\le9C/2.
\end{aligned}
 \tag{CN.8}
$$
Here is a complete Cauchy--Schwarz verification. Write $n=4|j|$ and sum over both signs. For $a>1$,
$$
 \sum_{j\ne0}(4|j|)^{-a}
 \le2\,4^{-a}\left(1+\frac1{a-1}\right).
 \tag{CN.9}
$$
The $v$ bound follows because
$$
 \sum_{j\ne0}\Lambda_j^{-6}
 \le\frac{12}{5\cdot4^6}<\frac1{32^2}.
$$
For $w$ in $\mathcal W_0$, (CN.5) gives the coefficient factor17 and
$\sum_{j\ne0}n^{-4}\le1/96$, so $17/\sqrt{96}<2$.
For the intermediate weighted sum,
$$
 \left(\sum_{j\ne0}n^{-10/3}\right)^{1/2}<\frac3{17}.
 \tag{CN.10}
$$
Indeed $4^{10/3}>96$, so the square is below $5/168<9/289$. Since
$(1+n)^{1/3}\le(5/4)^{1/3}n^{1/3}<(4/3)n^{1/3}$ and
$(1+n)^{4/3}<(3/2)n^{4/3}$ for $n\ge4$, (CN.10) proves the bounds for $w$ in $\mathcal W_{1/3}$ and for $p$ in $\mathcal W_{4/3}$.
Finally
$$
 \left(\sum_{j\ne0}n^{-4/3}\right)^{1/2}
 \le2^{1/6}<2
$$
gives $\|w\|_{\mathcal W_{4/3}}\le17(3/2)\cdot2C=51C$.
The $\mathcal W_0$ bound for $p$ follows directly from that for $v$.
Every series here includes the full infinite complement and both signs.

The true primitive, including its zero mean convention, satisfies
$$
 \|I\|_{H^s\to H^s}=\frac14,\quad
 \|I\|_{H^{-4/3}\to H^{-1/3}}=\frac{\sqrt{17}}4,\quad
 \|I\|_{H^{-1/3}\to L^2}=\frac{17^{1/6}}4.
 \tag{CN.11}
$$
Thus
$$
 a_I:=\frac{17^{2/3}}{16}<\frac12
 \tag{CN.12}
$$
is both the product of the last two norms and
$\|I^2\|_{H^{-4/3}\to L^2}$. The coefficient of the constant mode is zero in these formulas; it is not an omitted input coordinate.

## 3. Exact inverse on the whole circle, including the mean

Define
$$
 \mathcal T=\operatorname{Id}+M_w I,\qquad
 a=e^p,\qquad p=Iw.
 \tag{CN.13}
$$
For this real coefficient $a$ is strictly positive and periodic. Given any $f\in H^s$, $-4/3\le s\le0$, form
$$
\begin{aligned}
 h_0&=\frac{\langle af\rangle}{\langle a\rangle},&
 u&=I\{a(f-h_0)\},\\
 \kappa&=-\frac{\langle a^{-1}u\rangle}{\langle a^{-1}\rangle},&
 z&=a^{-1}(u+\kappa),&
 h&=f-wz .
\end{aligned}
 \tag{CN.14}
$$
All means are distribution pairings when $s<0$. The coefficient regularity and (CN.7)--(CN.8) make these pairings and products bounded in the stated spaces.

By the first quotient in (CN.14), $a(f-h_0)$ has exact mean zero. Therefore
$$
 (az)'=a(f-h_0),\qquad z'+wz=f-h_0,\qquad\langle z\rangle=0.
 \tag{CN.15}
$$
The second quotient is exactly the condition $\langle z\rangle=0$. It is independent of the first weighted mean and cannot be dropped. Since
$h=f-wz=z'+h_0$, one obtains
$$
 \langle h\rangle=h_0,\qquad Ih=z,\qquad
                         \mathcal T h=f.
 \tag{CN.16}
$$
Although the construction initially bounds $z$ in $H^s$, equation (CN.15) also gives its distribution derivative in $H^s$, hence $z\in H^{s+1}$. It justifies (CN.16) at the lowest stated index without imposing an extra derivative on $f$.

If $\mathcal T h=0$, the same integrating factor first gives $h_0=0$, and then $z$ is a constant multiple of $a^{-1}$. Its zero ordinary mean forces that constant to vanish. This proves uniqueness. Consequently (CN.14) is a two-sided inverse on each stated full Sobolev space, without a finite cutoff or a smallness assumption on $C$.

The output mean is the genuine weighted functional
$\langle af\rangle/\langle a\rangle$. It is not silently replaced by $\langle f\rangle$. In particular
$\mathcal T1=\mathcal T^{-1}1=1$, while general nonmean inputs may contribute to the output mean. Independent physical mean and charge rows must be transformed with these exact functionals.

## 4. Explicit forward and inverse norm bounds

Since $\langle p\rangle=0$ and $p$ is real, Jensen's inequality gives
$$
                       \langle a\rangle,\langle a^{-1}\rangle\ge1.
 \tag{CN.17}
$$
The Banach algebra estimate and (CN.8) imply
$$
 \|a^{\pm1}\|_{\mathcal W_{4/3}}\le M:=e^{9C/2}.
 \tag{CN.18}
$$
For $-4/3\le s\le0$, the four successive operations in (CN.14) give
$$
 |h_0|\le M\|f\|_{H^s},\qquad
 \|u\|_{H^s}\le\frac14M(1+M)\|f\|_{H^s},
 \qquad
 \|z\|_{H^s}\le\frac14M^2(1+M)^2\|f\|_{H^s}
              \le M^4\|f\|_{H^s}.
 \tag{CN.19}
$$
Thus valid full-circle bounds are
$$
 \boxed{\displaystyle
 \|\mathcal T\|_{H^s\to H^s}\le1+13C,\qquad
 \|\mathcal T^{-1}\|_{H^s\to H^s}\le1+51C e^{18C},
 \quad -4/3\le s\le0.}
 \tag{CN.20}
$$
The forward estimate uses $\|M_w I\|\le51C/4\le13C$.

For the output $L^2$ norm there is a useful smaller inverse bound. Use only
$$
 \|a^{\pm1}\|_\infty\le M_0=e^{17C/32},\qquad
 \|w\|_\infty\le2C
$$
in the same four operations. Then
$$
 \boxed{\displaystyle
 \|\mathcal T^{-1}\|_{L^2\to L^2}
 \le K_0(C):=1+2C e^{17C/8}.}
 \tag{CN.21}
$$
All these bounds take the correct value1 when $C=0$.

The stronger qualitative conclusion is the exact inverse (CN.14). The displayed bounds are quantitative upper estimates; they do not assert that the actual nonmean coefficient has a small $H^3$ norm.

## 5. Exact conjugation and every order-two term

Let $U=U_{R_\Omega}$ be the rotation density operator; because it is a rotation, it is the same unitary translation on every $H^s$. Write the corresponding component of the complete return as
$$
 \mathcal N=\zeta\,U(\operatorname{Id}+M_c I)+\mathcal R,
 \qquad \zeta^4=1,\qquad
 \mathcal R:H^{-4/3}\longrightarrow L^2 .
 \tag{CN.22}
$$
Any independently retained finite-head, mean or source port is carried separately with the exact coordinate change. If such ports have instead been included in $\mathcal R$, their full norms are part of its norm; none is assigned zero here.

Set $w_-(x)=w(x-\Omega)$ and
$\mathcal T_-=\operatorname{Id}+M_{w_-}I=U^{-1}\mathcal T U$.
Equation (CN.4) is the exact multiplication identity $c+w-w_-=\mu$. Since $I$ commutes with rotation,
$$
\begin{aligned}
 (\operatorname{Id}+M_cI)\mathcal T
   &=\mathcal T_-(\operatorname{Id}+\mu I)+\mathcal Q,\\
 \mathcal Q&=M_c I M_w I-\mu M_{w_-}I^2.
\end{aligned}
 \tag{CN.23}
$$
Therefore the exact full operator identity is
$$
 \boxed{\displaystyle
 \mathcal T^{-1}\mathcal N\mathcal T
 =\zeta\,U(\operatorname{Id}+\mu I)
       +\zeta\,U\mathcal T_-^{-1}\mathcal Q
       +\mathcal T^{-1}\mathcal R\mathcal T .}
 \tag{CN.24}
$$
It is not a formal truncation in powers of $I$.

For comparison with the old primitive ledger, the exact commutator is
$$
 I M_w=M_w I-I M_{\partial_x w}I+(Iw)\Pi-\Pi M_w I.
 \tag{CN.25}
$$
Consequently (CN.23) also retains the finite-rank term
$-M_c\Pi M_w I^2$. The term $(Iw)\Pi I$ is zero only by the exact identity $\Pi I=0$. No general output mean or independent physical mean is projected away. Bounds below use the ordered expression (CN.23), so they automatically include these mean terms.

Using (CN.8), (CN.11) and (CN.12) in the two possible intermediate Sobolev spaces gives
$$
\begin{aligned}
 \|\mathcal Q\|_{H^{-4/3}\to L^2}
 &\le a_I\big[
       (|\mu|+C/32)\,4C+|\mu|\,2C\big]\\
 &\le 3|\mu|C+\frac{C^2}{16}.
\end{aligned}
 \tag{CN.26}
$$
The first term applies $I:H^{-4/3}\to H^{-1/3}$, then the complete $w$ multiplier in that intermediate space, then $I:H^{-1/3}\to L^2$, and finally the $c$ multiplier. The second term uses the complete $I^2$ norm. This explicitly pays the negative Sobolev multiplication loss.

If $R_0\ge\|\mathcal R\|_{H^{-4/3}\to L^2}$, the whole new strong remainder after the linear first coefficient has upper bound
$$
 \boxed{\displaystyle
 R_{\rm lin}\le
 K_0(C)\left[(1+13C)R_0+3|\mu|C+\frac{C^2}{16}\right].}
 \tag{CN.27}
$$
The factor $1+13C$ is the input $H^{-4/3}$ norm of $\mathcal T$; the factor $K_0(C)$ is its output $L^2$ inverse norm. These factors are not interchanged.

For a full coupled system, every source is sent to $\mathcal T^{-1}f$, every independently retained input column is sent to $\mathcal T^{-1}B$, and every retained output row becomes $L\mathcal T$. Their mean functionals are exactly those in (CN.14)--(CN.16). The transformation alone solves none of the original finite equations. Its full-circle inverse introduces no additional finite frequency window.

## 6. Pay the scalar exponential replacement

For real $\mu$, $e^{t\mu I}$ is unitary on every Fourier Hilbert space, including its constant coordinate. Taylor's integral formula yields
$$
 (\operatorname{Id}+\mu I)-e^{\mu I}
 =-\mu^2 I^2\int_0^1(1-t)e^{t\mu I}\,dt.
 \tag{CN.28}
$$
Hence
$$
 \|(\operatorname{Id}+\mu I)-e^{\mu I}\|_{H^{-4/3}\to L^2}
 \le\frac{\mu^2}{2}a_I\le\frac{\mu^2}{4}.
 \tag{CN.29}
$$
The last inequality is strict when $\mu\ne0$; at $\mu=0$ both sides are zero.
The scalar symbol is now exactly
$$
 \zeta\,Ue^{\mu I}e_j
   =\zeta\,\exp\{i(2\pi j\rho_{15}+\beta/j)\}e_j,
 \qquad \beta=-\mu/4,\qquad j\ne0.
 \tag{CN.30}
$$
The constant coordinate is unchanged by the exponential, since $I1=0$.

Denote the complete transformed operator remainder after (CN.30) by $\mathcal R_{\rm exp}$. A conservative strong norm bound is
$$
 \boxed{\displaystyle
 R_{\rm exp}\le
 K_0(C)\left[(1+13C)R_0+3|\mu|C+\frac{C^2}{16}\right]
       +\frac{\mu^2}{4}.}
 \tag{CN.31}
$$
At the actual selected explicit background the already certified interval for $\beta_*$ implies $|\mu|<74$. Thus a further valid displayed bound is obtained by replacing $3|\mu|$ by222 and $\mu^2/4$ by1369. This does not assign a numerical value to $C$ or $R_0$.

On a high input tail $|j|\ge J$, the last term of (CN.31) may instead be bounded by the sharper exact scalar multiplier
$$
 \frac{\mu^2}{2}\,
 \frac{(1+16J^2)^{2/3}}{16J^2}.
 \tag{CN.32}
$$
It is a bound for this complete scalar difference, not an entrywise minimum of different operator certificates.

## 7. The resulting concrete high criterion and the surviving finite system

For the actual selected coefficient, the completed four-root arithmetic gives
$$
 |\exp\{i(2\pi j\rho_{15}+\beta_*/j)\}-\omega|
       >\frac1{512|j|},\qquad |j|\ge97,\quad \omega^4=1.
 \tag{CN.33}
$$
For any chosen fourth-root boundary sign, the corresponding diagonal divisor $D$ has
$|D_j|^{-1}\le128\Lambda_j$. Consequently the previously stated strong-remainder elimination applies with the now explicit normalizer fee:
$$
 \boxed{\displaystyle
 128R_{\rm exp}\Lambda_J^{-1/3}<1.}
 \tag{CN.34}
$$
On a common tail satisfying this inequality, the correctly ordered factorization is
$$
 D+P_J\mathcal R_{\rm exp}P_J
  =(\operatorname{Id}+P_J\mathcal R_{\rm exp}P_JD^{-1})D.
 \tag{CN.35}
$$
The inverse has the indicated one-derivative loss and norm at most
$128/(1-128R_{\rm exp}\Lambda_J^{-1/3})$.
Its natural domain is $\{h\in H^{-1}:Dh\in L^2\}$.
The full finite complement, its mean, all cross maps and the separate physical-to-return source maps remain. A phase-tail criterion is not identified with the full physical high block.

Formula (CN.34) is a concrete quantitative criterion in the complete coefficient norm $C$ and the preceding complete remainder norm $R_0$. It is not an actual pass at97. Neither the current31-term volume ledger nor the scalar interval for $\beta_*$ supplies these two missing operator inputs.

There is also a direct scalar stability margin, when the principal target remains exactly fixed. If a separately proved real coefficient $\widetilde\beta$ satisfies
$$
                  |\widetilde\beta-\beta_*|\le1/1024,
 \tag{CN.36}
$$
then the elementary Lipschitz bound for the scalar exponential and (CN.33) give the four-root gap
$1/(1024|j|)$, with divisor factor256 in place of128.
A change in the principal rotation is not covered by this statement: its phase error grows like $|j|$. The current theorem does not prove (CN.36) for an unknown nonlinear background or extend the finite-part cancellation to an unverified background class.

## 8. Evidence scope

The exact principal gap, reality convention, scalar identification and existing qualitative strong class are inherited from the selected-family theorem, Git blob e561b822673bbce15c1391ee851fb93d4143d43e, especially Sections 5--7. The primitive and density conventions are those of the [directed return word](R133-supplement-directed-return-word-and-root-first-coefficient-contract.md), blob150fce1515b1ce018c4d3066589a8911ece3325f, and the [complete moving first symbol](R133-supplement-complete-moving-first-symbol-and-root-subtractions.md), bloba223a263c3dea6e87e9e51364ee541946eed4c77.

The new content is the full-circle inverse (CN.14), the complete two-window bounds, and the exact strong-remainder fees (CN.26)--(CN.32). No prior numerical result is recomputed or relabelled, and the earlier full-real-delta root finite-part theorem remains the source of that already completed identification.
