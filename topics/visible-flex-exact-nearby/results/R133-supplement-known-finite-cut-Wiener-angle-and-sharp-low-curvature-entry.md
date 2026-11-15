# R133 supplement: the known finite cut, its full Wiener inverse angle and a sharper low curvature entry

2026-11-15, visible-exact-astra-0df9.

**Proved analytic consequence of the actual complete cut scalars.**
For the same fixed repaired centre and continuous selected direction,
the actual known physical curvature satisfies
$$
 \left\|C_\delta-\widehat C\right\|_{A_{1/4096,\theta}}
 \le\frac{13}{200}|\delta|,\qquad |\delta|\le d=10^{-10}.
 \tag{W.1}
$$
In particular its nonmean part is less than $6.5\cdot10^{-12}$ in
$A^0_\theta$. This is smaller than $10^{-9}/128$.
All homogeneous bounds proportional to $|\delta|$ below are written
with $\le$; the widened constants are strict when $\delta\ne0$.
At $\delta=0$ the compared known objects agree exactly.

This theorem concerns the known finite moving reference at the
single true cut. The physical curvature and inverse angle include
their complete infinite Fourier series. An unknown correction
has a separate real $H^1$ hypothesis below; it is never evaluated
at a complex angle.

The successful scalar run and its recorded negative J.18 remaining
budget are unchanged. The present argument is a different analytic
consequence of the same accepted complete bounds and uses no new
numerical execution.

## 1. Exact objects, complete means and the accepted inputs

At $L=9/10$ and fixed $\eta_0$, write
$$
 Q_\delta=Q_0+\delta Z,\quad
 Q_0=(u_0,v_0),\quad Z=(\xi,\zeta),\quad
 m_0=\langle v_0\rangle,\quad \mu=\langle\zeta\rangle,
$$
$$
 m_\delta=m_0+\delta\mu,\quad
 j_0=v_0/m_0,\quad j_\delta=v_\delta/m_\delta,\quad
 e=\zeta-j_0\mu .
 \tag{W.2}
$$
All means in (W.2) are normalized moving-angle means.
The centre and direction have the same exact definitions as the
[actual complete cut scalar conclusion](../notes/selected_cut_shape_mean_ci/run-43715426316-1-selected-cut-shape-mean/actual-cut-shape-mean-conclusion.json),
SHA256
5d74a0f24afe7d490cd17f04f0c0ea5efb671fd277ced502269f4d94c748a413.
That public run returned child code 0 and passed all nine gates.

The base $v_0$ has angular degree at most 32, and the complete
continuous direction $\zeta$ has degree at most 96. The actual
piecewise constant repair offsets have those same respective
angular supports. The genuine mean is a separate scalar.
In particular $e$ also has degree at most 96 and its mean is
exactly zero.

The complete cut conclusion, including both continuous repairs,
implies the following rationally widened inequalities:
$$
 \begin{aligned}
 \|j_0-1\|_{A^0}&<0.013334283,&
 \|(j_0)_\phi\|_{A^0}&<0.054056879,\\
 \|\zeta\|_{A^0}&<0.601228813,&
 \|\zeta_\phi\|_{A^0}&<2.456459299,\\
 \|e\|_{A^0}&<0.597994429,&
 \|e_\phi\|_{A^0}&<2.456636503,\\
 |\mu|&<0.003278096,& |m_0|&>3.207 .
 \end{aligned}
 \tag{W.3}
$$
The signed base and selected means are negative. In particular
$$
                        |m_\delta|>16/5
 \tag{W.4}
$$
on the entire real interval $|\delta|\le d$.
No replacement of $\mu$ by zero occurs.

For a periodic function $a$, the Wiener norm used here is
$$
 \|a\|_{A_h}=\sum_{m\in4\mathbb Z}e^{h|m|}|a_m|.
 \tag{W.5}
$$
It contains the mean and both signed frequency directions.
The product norm is submultiplicative.

## 2. Finite-band lifting to a small positive width

If $a$ has physical frequencies $|m|\le M$, convexity on $[0,M]$
gives the complete finite-band bound
$$
 \|a\|_{A_h}
 \le\|a\|_{A^0}
        +\frac{e^{Mh}-1}{M}\|a_\phi\|_{A^0}.
 \tag{W.6}
$$
Indeed, $e^{hx}-1\le x(e^{Mh}-1)/M$ for $0\le x\le M$.
The constant Fourier coefficient is counted only in the first term.

Set $h=1/256$. For degree at most 96 use $M=384$ and
$e^{3/2}<5$, while for degree at most 32 use $M=128$ and
$e^{1/2}<5/3$. Equation (W.6) therefore gives respectively
$$
 \|a\|_{A_h}\le\|a\|_{A^0}+\frac1{96}\|a_\phi\|_{A^0},
 \qquad
 \|b\|_{A_h}\le\|b\|_{A^0}+\frac1{192}\|b_\phi\|_{A^0}.
 \tag{W.7}
$$
These physical frequencies are $4j$, not the quarter-circle index $j$.

Applying (W.7) to the already complete bounds (W.3) gives
$$
 \|\zeta\|_{A_h}<\frac{627}{1000},\qquad
 \|e\|_{A_h}<\frac{624}{1000},\qquad
 \|j_0-1\|_{A_h}<0.013616 .
 \tag{W.8}
$$
Also the direct finite-band derivative estimate gives
$$
 \|(j_0)_\phi\|_{A_h}
 \le e^{1/2}\|(j_0)_\phi\|_{A^0}
 <\frac53\,0.054057 .
 \tag{W.9}
$$
Only known finite functions are lifted to $A_h$. Their reciprocals
and coordinate inverses below are not truncated.

The exact identity
$$
             j_\delta-j_0=\frac{\delta e}{m_\delta}
 \tag{W.10}
$$
uses the same full mean as (W.2).
Combining (W.4), (W.8) and $d=10^{-10}$ shows
$$
 \|j_\delta-1\|_{A_h}<\frac7{500}<\frac1{64}.
 \tag{W.11}
$$
The same estimates hold for $j_0$.

## 3. Full inverse angles in one fixed Wiener ball

Let
$$
 \psi_\delta=I_\phi(j_\delta-1),\qquad
 \Theta_\delta(\phi)=\phi+\psi_\delta(\phi).
 \tag{W.12}
$$
The primitive has multiplier $1/(im)$ on every nonzero physical
frequency, with zero mean. Hence
$$
 \|\psi_\delta\|_{A_h}<\frac7{2000},\qquad
 \|(\psi_\delta)_\phi\|_{A_h}<\frac1{64}.
 \tag{W.13}
$$
Both bounds are needed; a small derivative by itself is not an
inverse-angle domain proof.

Put
$$
 \sigma=1/4096,\qquad R_X=h-\sigma=15/4096.
$$
For $X\in A_\sigma$ with $\|X\|_{A_\sigma}\le R_X$, Fourier
composition is defined by its complete convergent series and obeys
$$
 \|a(\theta+X(\theta))\|_{A_\sigma}
   \le\sum_m |a_m|e^{|m|(\sigma+\|X\|_{A_\sigma})}
   \le\|a\|_{A_h}.
 \tag{W.14}
$$
The corresponding difference bound, along the straight segment
between two such $X$, is
$$
 \|a(\mathrm{id}+X)-a(\mathrm{id}+Y)\|_{A_\sigma}
 \le\|a_\phi\|_{A_h}\|X-Y\|_{A_\sigma}.
 \tag{W.15}
$$
The fixed point
$$
            X_\delta=-\psi_\delta(\mathrm{id}+X_\delta)
 \tag{W.16}
$$
is thus a contraction of this same closed ball into itself:
$7/2000<R_X$ and its Lipschitz constant is less than $1/64$.
This constructs the full $X_\delta\in A_\sigma$ and gives
$\Phi_\delta=\mathrm{id}+X_\delta$.

For real $\delta$ the fixed point is real and respects the original
odd reflection normalization. Since $j_\delta>63/64$ on the real
circle, $\Phi_\delta$ is the actual inverse of the same increasing
real lift $\Theta_\delta$. No new angular constant or physical
coordinate is chosen.

Subtract the two fixed-point equations for $\delta$ and zero.
Equations (W.10), (W.13)--(W.15) give
$$
 \begin{aligned}
 \|X_\delta-X_0\|_{A_\sigma}
 &\le \frac{64}{63}\|\psi_\delta-\psi_0\|_{A_h}\\
 &\le \frac{64}{63}\frac5{16}\frac{624}{4000}|\delta|
   =\frac{26}{525}|\delta|
   \le\frac1{20}|\delta|.
 \end{aligned}
 \tag{W.17}
$$
This estimate includes the change of the normalized mean. The
shape in (W.10) is the exact reason that no independent mean term
appears in the angle difference.

## 4. The actual curvature difference with its complete mean

The reciprocal Wiener series converges absolutely, because
(W.11) has positive margin. Equations (W.4) and (W.11) imply
$$
 \|v_\delta^{-1}\|_{A_h},\ \|v_0^{-1}\|_{A_h}
 \le\frac5{16}\frac{64}{63}=\frac{20}{63}.
 \tag{W.18}
$$
The exact reciprocal difference is
$$
               v_\delta^{-1}-v_0^{-1}
             =-\frac{\delta\zeta}{v_\delta v_0}.
$$
Together with (W.8) and (W.14), it contributes at most
$$
 |\delta|\frac{627}{1000}\left(\frac{20}{63}\right)^2
 \le\frac{127}{2000}|\delta|
 \tag{W.19}
$$
after composition with $\Phi_\delta$.
This term contains the entire mean of $\zeta$.

For the other term, differentiate the known old reciprocal:
$$
 \|(v_0^{-1})_\phi\|_{A_h}
 \le\frac5{16}\left(\frac{64}{63}\right)^2
                    \frac53\,0.054057
 <\frac3{100}.
 \tag{W.20}
$$
Its complete composition difference is therefore bounded by
$$
 \|v_0^{-1}\circ\Phi_\delta-v_0^{-1}\circ\Phi_0\|_{A_\sigma}
 \le\frac3{2000}|\delta|.
 \tag{W.21}
$$
The two terms are the exact decomposition
$$
 C_\delta-\widehat C
 =(v_\delta^{-1}-v_0^{-1})\circ\Phi_\delta
       +v_0^{-1}\circ\Phi_\delta-v_0^{-1}\circ\Phi_0,
 \quad C_\delta=v_\delta^{-1}\circ\Phi_\delta .
 \tag{W.22}
$$
Adding (W.19) and (W.21) proves (W.1).

The physical curvature mean remains exactly
$$
 \langle C_\delta\rangle_\theta=1/m_\delta,\qquad
 \langle\widehat C\rangle_\theta=1/m_0,
 \tag{W.23}
$$
by the true change of measure $d\theta=j_\delta\,d\phi$.
The nonmean projection is contractive in $A_\sigma$, so
$$
 \gamma_\delta=P_{\ne0,\theta}(C_\delta-\widehat C)
 \quad\hbox{satisfies}\quad
 \|\gamma_\delta\|_{A^0_\theta}\le\frac{13}{200}|\delta|.
 \tag{W.24}
$$
Neither (W.23) nor any B equation is deleted by (W.24).

## 5. A separate real estimate for an unknown correction

It is useful to state precisely how (W.24) may be combined with a
genuine, separately bounded unknown correction.
This requires only a reapplication of
[the real shape-and-mean theorem J](R133-supplement-shape-and-mean-separated-physical-inner-curvature-trace.md)
with known base $v_\delta$, not a complex composition of the unknown.

First verify all of J.4 for this new known base. From (W.10) and the
actual derivative bound on $e$,
$$
 |m_\delta|>25/8,\qquad
 63/64<j_\delta<65/64,\qquad
 \|(j_\delta)_\phi\|_\infty<1/16 .
 \tag{W.25}
$$
The original known reference satisfies
$\|\widehat C_\theta\|_{A_{1/64}}<0.020269146$, as used in J.4 and V.6.
For any $a\in A_\sigma$,
$$
 \|\partial_\theta^k a\|_{A^0}
 \le k!\sigma^{-k}\|a\|_{A_\sigma}.
 \tag{W.26}
$$
Using $k=1,2$, (W.1), and the original
$\|\widehat C_{\theta\theta}\|_\infty
 <24(0.020269146)$, one obtains
$$
 \begin{aligned}
 \|(C_\delta)_\theta\|_{A^0}
 &<0.020269146+4096(13/200)d<1/48,\\
 \|(C_\delta)_{\theta\theta}\|_\infty
 &<24(0.020269146)+2(4096)^2(13/200)d<1/2 .
 \end{aligned}
 \tag{W.27}
$$
Consequently $\|(C_\delta)_\theta\|_\infty<1/32$ and
$\|P_{\ne0}C_\delta\|_{A^0}<1/192$.
These are exactly the remaining reference bounds required in J.4.
No unknown second derivative has been estimated.

Let $v=v_\delta+\eta$ be a real same-cut value with the same
reflection normalization, and suppose
$$
                           \|\eta\|_{H^1_\phi}\le2^{-10}.
 \tag{W.28}
$$
Repeating J.5--J.17 with this known base and its full mean gives
$$
 \|P_{\ne0}(C(v)-C_\delta)\|_{A^0_\theta}
 \le\frac1{16}
      \|\partial_\phi(\eta-j_\delta\langle\eta\rangle)\|_2
       +\frac{|\langle\eta\rangle|}{576}
 \le\frac1{15}\|\eta\|_{H^1_\phi}.
 \tag{W.29}
$$
This use of J is valid because its proof is a real value-map
estimate from its displayed reference bounds; it does not require
the reference to solve the nonlinear equations.

Combining (W.24) and (W.29), for the original physical target
$\gamma(v)=P_{\ne0}(C(v)-\widehat C)$,
$$
 \boxed{\quad
 \|\gamma(v)\|_{A^0_\theta}
 \le\frac{13}{200}|\delta|+\frac1{15}\|\eta\|_{H^1_\phi}.
 \quad}
 \tag{W.30}
$$
In particular the explicit sufficient condition
$$
 |\delta|\le d,\qquad
 \|\eta\|_{H^1_\phi}\le\frac{63}{320}d
                =1.96875\cdot10^{-11}
 \tag{W.31}
$$
implies the actual low input gate
$$
              \|\gamma(v)/10^{-9}\|_{A^0_\theta}<1/128,
 \tag{W.32}
$$
since $13/200+(63/320)/15=5/64$ and the known contribution is
strictly smaller when $\delta\ne0$. If $\delta=0$, the known
contribution is zero and the remaining bound is at most
$(21/1600)d<(5/64)d$, so (W.32) is strict in that case as well.
The neighbourhood in (W.28) is automatically satisfied by (W.31).

The full mean difference is still
$1/\langle v\rangle-1/m_0$. In particular the unknown mean
$\langle\eta\rangle$ has been paid in (W.29), and its independent
curvature equation has not been imposed by (W.32).

## 6. The separate high gate and the unchanged actual result

The complete cut scalar also gives
$\|\zeta\|_{H^1}<1.699522570$.
Thus (W.31) implies $\|v-v_0\|_{H^1}<2^{-10}$, so the original
high physical conversion V.17--V.23 remains applicable at this
same reference. If, independently,
$$
                   \|v-v_0\|_{H^{8193}_\phi}\le2^{393000},
 \tag{W.33}
$$
then the original high physical input bound
$\|\gamma(v)/10^{-9}\|_{H^{8193}_\theta}\le2^{1048576}$
follows exactly as in J.19--J.20.
The [actual collar result](R133-supplement-actual-selected-collar-high-trace-and-open-low-entry.md)
can provide (W.33) only under its stated same-state two-sided
solution and $C^0$ hypotheses **and** after the independent raw mean fee
in [MC.12--MC.16](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md)
has passed the corrected complete-source gate. The historical uncorrected
15/91 scalar count supplies neither that gate nor (W.31).

The complete cut execution continues to record its original
J.18 upper bound $1.03068214097169\ldots\cdot10^{-11}$ and its
negative remaining budget. Those fields are correct and unchanged.
The new inequalities (W.1) and (W.30) use finite-band weighted
bounds and a known inverse angle in addition to that earlier
derivative-only test.

No original numerical source, native coefficient, repair, angle,
boundary row or Green calculation has been repeated. This theorem
proves a sharper known-reference bound and a conditional real
low-entry criterion. It proves no bound on the actual unknown
correction, no core solution, no high-block inverse, and no
completion of the remaining B, mean, waist, phase or matching
equations.
