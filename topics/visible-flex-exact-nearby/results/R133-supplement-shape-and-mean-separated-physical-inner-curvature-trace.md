# R133 supplement: shape and mean separation in the actual physical inner-curvature trace

2026-11-15. This is an analytic improvement of the low trace gate in [V](R133-supplement-physical-inner-curvature-data-from-true-moving-core-trace.md). It uses the same repaired centre, actual section $L=9/10$, physical angle, reflection normalization and complete even mean. No numerical enclosure is recomputed.

The new conclusion is
$$
 \|\gamma\|_{A^0_\theta}
 \le
 \frac1{16}\|\partial_\phi(h-j_0\mu)\|_{L^2_\phi}
       +\frac{|\mu|}{576}
 \le\frac1{15}\|h\|_{H^1_\phi},
 \qquad h=v-v_0,\quad \mu=\langle h\rangle_\phi ,
 \tag{J.1}
$$
on the same elementary low neighbourhood $\|h\|_{H^1}\le2^{-10}$.
In particular the sufficient low gate for the current exact-tail domain can be enlarged to
$$
 \boxed{\quad \|v-v_0\|_{H^1_\phi}\le\frac{15\,10^{-9}}{128}.\quad}
 \tag{J.2}
$$
This is a sufficient condition, not a claim that the current core construction has already passed it. The separate $H^{8193}$ trace condition is retained.

## 1. Same actual value map and paid reference bounds

All circle norms use normalized measure and frequencies $4\mathbb Z$. The actual and reference angles and curvatures are exactly those of V:
$$
 m=\langle v\rangle,\quad j=v/m,\quad
 \Theta=\mathrm{id}+I_\phi(j-1),\quad
 C=(1/v)\circ\Theta^{-1},\quad
 \gamma=P_{\ne0,\theta}(C-\widehat C).
 \tag{J.3}
$$
The reference has $m_0<0$, $j_0=v_0/m_0$ and angle $\Theta_0$. Reflection fixes the real lifts; no independent angular constant is chosen.

The original complete reference table, as used in V.6--V.7, implies
$$
 |m_0|>\frac{25}{8},\quad
 \frac{63}{64}<j_0<\frac{65}{64},\quad
 \|(j_0)_\phi\|_\infty<\frac1{16},
$$
$$
 \|\widehat C_\theta\|_\infty<\frac1{32},\qquad
 \|\widehat C_{\theta\theta}\|_\infty<\frac12,\qquad
 \|P_{\ne0}\widehat C\|_{A^0}
 \le\frac14\|\widehat C_\theta\|_{A^0}
 <\frac1{192}.
 \tag{J.4}
$$
For the last inequality use the already paid full bound
$\|\widehat C_\theta\|_{A_{1/64}}<.020269146<1/48$.
Only this known reference is evaluated at different real angles below.
No complex evaluation or derivative bound for an unknown datum is used.

Put $\varepsilon=2^{-10}$ and assume $\|h\|_{H^1}\le\varepsilon$.
The complete-circle embedding gives $|\mu|\le\varepsilon$ and
$\|h\|_\infty<2\varepsilon$. Thus $m<0$, $|m|>3$, and the exact identity
$$
 j-j_0=\frac{h-j_0\mu}{m}
 \tag{J.5}
$$
gives
$$
 \|j-j_0\|_\infty
 <\frac{193}{192}\varepsilon,\qquad
 \frac{31}{32}<j<\frac{33}{32}.
 \tag{J.6}
$$
Both angle maps are therefore genuine increasing real diffeomorphisms.

## 2. Separate the actual mean before estimating the shape change

Define
$$
 a=\frac{m_0}{m}>0,\qquad
 \widetilde v=av,\qquad
 e=h-j_0\mu,\qquad k=\widetilde v-v_0=ae .
 \tag{J.7}
$$
Then $\langle e\rangle=\langle k\rangle=0$ and
$\langle\widetilde v\rangle=m_0$.
The normalized angle of $\widetilde v$ is precisely the actual $\Theta$,
since $\widetilde v/m_0=v/m=j$. In particular this is an exact change
of the mean at fixed normalized angle; it does not alter the physical
input convention.

Let $\widetilde C=(1/\widetilde v)\circ\Theta^{-1}$ and
$\widetilde\gamma=P_{\ne0}(\widetilde C-\widehat C)$. Then
$$
 C=a\widetilde C,\qquad
 \gamma=a\widetilde\gamma+(a-1)P_{\ne0}\widehat C,
 \qquad a-1=-\frac{\mu}{m}.
 \tag{J.8}
$$
The complete mean change itself remains $1/m-1/m_0$; it has not been
removed from the independent physical mean equation.

Also,
$$
 a<1+\frac{\varepsilon}{3}<\frac{1025}{1024},
 \qquad a^2<\frac{257}{256}.
 \tag{J.9}
$$
The derivative used in (J.1) is a scalar derivative in the original
moving angle:
$\partial_\phi e=h_\phi-(j_0)_\phi\mu$.

## 3. A mean-zero shape estimate with the actual measure

Pull the exact shape difference back by the actual angle:
$$
 F=(\widetilde C-\widehat C)\circ\Theta
   =\frac1{\widetilde v}-\frac1{v_0}
      -\{\widehat C(\Theta)-\widehat C(\Theta_0)\}.
 \tag{J.10}
$$
Because the two moving means now agree, the exact angle difference is
$$
 \Theta-\Theta_0=\frac{I_\phi k}{m_0},\qquad
 j-j_0=\frac{k}{m_0}.
 \tag{J.11}
$$
For the reciprocal part,
$$
 \left(\frac1{\widetilde v}-\frac1{v_0}\right)_\phi
 =-\frac{k_\phi}{\widetilde v^2}
    +(v_0)_\phi\left(\frac1{v_0^2}-\frac1{\widetilde v^2}\right).
$$
Here $|\widetilde v|=|m_0|j>3$, by (J.4) and (J.6).
Since $|(v_0)_\phi|\le|m_0|/16$ and
$j,j_0\in(31/32,33/32)$, the second coefficient satisfies
$$
 \frac{|(v_0)_\phi|\,|v_0+\widetilde v|}
 {|v_0|^2|\widetilde v|^2}
 \le\frac{33}{256}\left(\frac{32}{31}\right)^4
                         \left(\frac8{25}\right)^2
 =\frac{8650752}{577200625}<\frac1{64}.
 \tag{J.12}
$$
Consequently
$$
 \left\|\left(\frac1{\widetilde v}-\frac1{v_0}\right)_\phi\right\|_2
 \le\frac19\|k_\phi\|_2+\frac1{64}\|k\|_2 .
 \tag{J.13}
$$

The other derivative in (J.10) equals
$$
 [\widehat C_\theta(\Theta)-\widehat C_\theta(\Theta_0)]j
              +\widehat C_\theta(\Theta_0)(j-j_0).
$$
Use the real mean value theorem, (J.4), and the exact
$\|I_\phi\|_{L^2_{\ne0}\to L^2_{\ne0}}=1/4$ in (J.11).
This gives
$$
 \left\|[\widehat C(\Theta)-\widehat C(\Theta_0)]_\phi\right\|_2
 \le\left(\frac{33}{32}\frac12\frac2{25}
                    +\frac1{32}\frac8{25}\right)\|k\|_2
 =\frac{41}{800}\|k\|_2 .
 \tag{J.14}
$$
No supremum of the primitive is used at this step.
Since $k$ has mean zero, $\|k\|_2\le\|k_\phi\|_2/4$.
It follows that
$$
 \|F_\phi\|_2
 \le\left(\frac19+\frac{107}{6400}\right)\|k_\phi\|_2
 =\frac{7363}{57600}\|k_\phi\|_2
 \le\frac{41}{320}\|k_\phi\|_2 .
 \tag{J.15}
$$

The physical measure conversion is still explicit:
$$
 \|\partial_\theta(\widetilde C-\widehat C)\|_{L^2_\theta}
 \le\sqrt{\frac{32}{31}}\|F_\phi\|_{L^2_\phi}.
$$
The full signed Fourier sum, including both nonzero directions, gives
$$
 \|P_{\ne0}q\|_{A^0}
 \le\frac{\pi}{4\sqrt3}\|q_\theta\|_2 .
$$
Using $\pi/(4\sqrt3)<15/32$ and
$\sqrt{32/31}<33/32$, their product is less than
$495/1024<31/64$. Therefore
$$
 \|\widetilde\gamma\|_{A^0}
 \le\frac{31}{64}\frac{41}{320}\|k_\phi\|_2.
 \tag{J.16}
$$

## 4. Complete low bound, including the independent mean

In (J.8), use $k=ae$, (J.9), (J.16) and (J.4). The shape coefficient is
$$
 a^2\frac{31}{64}\frac{41}{320}
 <\frac{257\cdot1271}{256\cdot20480}
 =\frac{326647}{5242880}<\frac1{16}.
$$
The mean coefficient is at most $1/(3\cdot192)=1/576$.
This proves the first inequality of (J.1) with every mean retained.

For the second inequality, use
$$
 \|e_\phi\|_2
 \le\|h_\phi\|_2+\frac{|\mu|}{16}.
$$
The first bound in (J.1) is consequently at most
$$
 \frac1{16}\|h_\phi\|_2+\frac{13}{2304}|\mu|.
 \tag{J.17}
$$
Cauchy--Schwarz and
$\|h_\phi\|_2^2+|\mu|^2\le\|h\|_{H^1}^2$ give
$$
 \frac{\sqrt{20905}}{2304}\|h\|_{H^1}
 \le\frac1{15}\|h\|_{H^1},
$$
because $225\cdot20905=4703625<5308416=2304^2$.
This establishes (J.1) and the larger sufficient gate (J.2).

For a comparison with the selected known family
$Q_\delta=Q_0+\delta Z$, write
$h=\xi_v+\delta Z_v(L)$, where $\xi=Q-Q_\delta$ is the actual
unknown correction. The more informative first bound remains
$$
 \begin{split}
 \|\gamma\|_{A^0}
 \le{}&\frac1{16}\bigl[
 \|\partial_\phi(\xi_v-j_0\langle\xi_v\rangle)\|_2
 +|\delta|\,\|\partial_\phi(Z_v-j_0\langle Z_v\rangle)\|_2\bigr]\\
 &+\frac1{576}\bigl[
 |\langle\xi_v\rangle|+|\delta|\,|\langle Z_v\rangle|\bigr].
 \end{split}
 \tag{J.18}
$$
All quantities in (J.18) are at the same actual cut $L$.
The known direction may be evaluated from its own exact accepted
coefficient data; no global-body norm is silently identified with
a cut norm. Equation (J.18) is an analytic formula, not a new
evaluation of those particular cut quantities.

## 5. Entry to the actual tail and to the collar estimate

The high physical conversion V.17--V.23 applies on the same low
neighbourhood proved above. Thus the pair of sufficient hypotheses
$$
 \|v-v_0\|_{H^1_\phi}\le15\,10^{-9}/128,\qquad
 \|v-v_0\|_{H^{8193}_\phi}\le2^{393000}
 \tag{J.19}
$$
implies the same full physical input gates
$$
 \|\gamma/10^{-9}\|_{A^0_\theta}\le1/128,\qquad
 \|\gamma/10^{-9}\|_{H^{8193}_\theta}\le2^{1048576}.
 \tag{J.20}
$$
The continuous value-map argument and full curvature matching in V
are unchanged: the nonmean C data are selected by $\gamma$, while
the complete B function and the independent C mean remain equations.

For a two-sided same-state positive collar, the explicit E.21--E.22
bound of [the residual-sensitive energy lemma](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md)
can now be compared with $15\,10^{-9}/128$ when its reference is
$Q_0$. When the reference is $Q_\delta$, first include its known
cut contribution through (J.18) or the full triangle inequality.
Every ordinary residual, coefficient gap, mean and true seam
condition in that energy lemma remains necessary.

Neither (J.19) nor its actual core estimates are claimed here.
The new proved result is the sharper complete low conversion,
its shape/mean formula and its precise use with the same existing
high tail domain.
