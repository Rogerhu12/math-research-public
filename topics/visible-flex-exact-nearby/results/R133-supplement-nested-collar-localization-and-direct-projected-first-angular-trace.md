# R133 supplement: nested collar localization and a direct projected first-angular trace

## 1. Object, hypotheses, and the new claim

This is a conditional estimate for the **same real, continuous, two-sided
$H^1$ state** on the positive collar
$I_0=[17/20,19/20]$, with cut $c=9/10$.
It uses [the complete collar energy E](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md),
[the selected-reference split SB](R133-supplement-selected-reference-band-splitting-with-complete-small-source.md),
and [the component and frequency bounds LC](R133-supplement-saved-positive-collar-component-bounds-and-high-frequency-coercivity.md).
Their full means, exact centre repair, canonical degree96 response,
fixed $\eta_0$, selected range $|\delta|\le10^{-10}$, ordinary residual
and genuine interface conditions are retained.

The new step is to iterate the **zero-order localized estimate** on
finitely many nested intervals, and then apply the exact first-angular
equation to the high projection. It gives an ordinary $H^1$ high trace
directly from the displayed source/body columns. No $H^{8193}$ interpolation
constant enters this particular trace inequality. The separate high
regularity requirement for the exact tail construction is unchanged.

All circle measures are normalized on the fourfold physical circle.
The mode label $j$ has physical frequency $4j$. All radial integrals use
the actual measure $dr$.

Write
$$
 P=\operatorname{diag}(K^{-1/4},K^{1/4}),\qquad
 W=PQ,\quad W_\delta=PQ_\delta,\quad z=W-W_\delta,\quad
 F=P(f-f_\delta).
 \tag{NC.1}
$$
Here $Q_\delta=Q_0+\delta Z$ is the same explicit selected reference.
For $J=96$ or $288$, put
$$
 \Pi_J=\mathbf1_{\{|j|\le J\}},\quad H_J=1-\Pi_J,\quad
 z_L=\Pi_Jz,\quad z_H=H_Jz,\quad
 z_S=(\Pi_J-\Pi_{J-64})z,\quad n=4(J+1).
 \tag{NC.2}
$$
In particular $z_L$ contains both independent means.

The principal operator and its high restriction are
$$
 \mathcal L=\partial_r-d\partial_\phi+aJ_0\partial_\phi,\qquad
 \mathcal L_H=\partial_r-H_Jd\partial_\phi+aJ_0\partial_\phi,
 \quad a=-Gm\sqrt K>0,\quad
 J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
 \tag{NC.3}
$$
The sign convention for $J_0$ is the one in E; reversing both displayed
$J_0$ conventions changes none of the estimates. The coefficients are
those of the actual state, not of an independently chosen cap solution.

Assume the complete LC bounds hold on $I_0$, including
$$
 a\ge a_->0,\quad |a_r/a|\le L,\quad |d|\le d_+,\quad
 \tau=\frac{L}{a_-n}<1.
 \tag{NC.4}
$$
For an approximate state, the actual residual mean term in the formula
for $a_r/a$ must be included, exactly as in E.7 and LC.10.
A true solution has $f=0$.

Define
$$
 c_p^\#=\frac1{a_-\sqrt{1-\tau}},\qquad
 c_r^\#=1+d_+c_p^\#.
 \tag{NC.5}
$$
Let $A_H,C_S,C_L$ denote the complete LC.13--14 bounds, and suppose
$$
 t_0=\frac{c_p^\#A_H}{n}<1,\qquad
 b_p=\frac{c_p^\#}{1-t_0},\qquad
 b_r=\frac{c_r^\#}{1-t_0},\qquad k=\frac{b_p}{n}.
 \tag{NC.6}
$$
These hypotheses concern the same actual state and the same parameter
interval. Successful scalar candidate tests do not by themselves
construct a state in that domain.

## 2. The full zero-order local estimate

For a real radial cutoff $\chi$ with $0\le\chi\le1$, zero at both
endpoints of its support, the exact SB high equation and LC energy give
$$
 \begin{split}
 \|(\chi z_H)_\phi\|_2
 &\le b_p\{\|H_JF\|_{2,\operatorname{supp}\chi}
       +C_S\|z_S\|_{2,\operatorname{supp}\chi}
       +C_L\|z_L\|_{2,\operatorname{supp}\chi}
       +\|\chi' z_H\|_2\},\\
 \|\chi z_H\|_2
 &\le k\{\|H_JF\|_{2,\operatorname{supp}\chi}
       +C_S\|z_S\|_{2,\operatorname{supp}\chi}
       +C_L\|z_L\|_{2,\operatorname{supp}\chi}
       +\|\chi' z_H\|_2\}.
 \end{split}
 \tag{NC.7}
$$
The second line follows from the high Poincare inequality at every
radial slice. All primitive, mean, and angular projection operators
commute with a radial scalar cutoff. No division by $\chi$ occurs.
In particular the last term is present even after the high zeroth-order
coefficient has been absorbed.

Let $I_0\supset I_1\supset\cdots\supset I_N$ be concentric intervals,
each obtained by shortening both ends by $h>0$, and assume $I_N$ has
positive length. A piecewise linear cutoff from $I_{i-1}$ to $I_i$
has $|\chi_i'|\le h^{-1}$. Put
$$
 B_i=\|z_H\|_{2,I_i},\qquad
 E=\|H_JF\|_{2,I_0}+C_S\|z_S\|_{2,I_0}
                         +C_L\|z_L\|_{2,I_0},\qquad
 r=\frac{k}{h}.
 \tag{NC.8}
$$
Equation (NC.7) gives, for every $1\le i\le N$,
$$
 B_i\le kE+rB_{i-1}.
 \tag{NC.9}
$$
The source/body terms may all be bounded on the same outer interval:
restriction only decreases their ordinary $L^2$ norms. Induction yields
$$
 \boxed{\quad
 B_N\le \eta_N B_0+\sigma_N E,\qquad
 \eta_N=r^N,\qquad
 \sigma_N=k\sum_{j=0}^{N-1}r^j .
 \quad}
 \tag{NC.10}
$$
The finite positive polynomial is valid for all $r\ge0$, including
$r=1$. A useful decay factor requires a separately verified $r<1$.
There is no infinite series, limiting argument in $N$, or assumption
of increasing angular regularity.

If the actual full raw difference obeys the same LC bound
$\|Q-Q_\delta\|_{C^0(I_0\times S^1)}\le\rho$, then
$$
 B_0\le p_+\rho\sqrt{|I_0|},\qquad
 p_+=\sup_{I_0}\max(K^{1/4},K^{-1/4}).
 \tag{NC.11}
$$
This uses the normalized circle measure and the true radial length.
It does not replace the separate low and shell body inputs in $E$.

## 3. Exact differentiated equation and the second absorption gate

Set $p=z_\phi$. The exact E.16--17 identities, with $W^0=W_\delta$,
are
$$
 \mathcal Lp=A_1p+\mathcal B_{10}z+F_\phi,\qquad
 A_1=d_\phi\operatorname{Id}+\alpha D
          -b(|W|^2\operatorname{Id}+2WW^t),
 \tag{NC.12}
$$
where
$$
 \begin{split}
 \mathcal B_{10}z={}&
 -b\{W_{\delta,\phi}((W+W_\delta)\cdot z)
       +2z(W\cdot W_{\delta,\phi})
       +2W_\delta(W_{\delta,\phi}\cdot z)\}\\
 &-bW_{\delta,\phi\phi}I_\phi((W+W_\delta)\cdot z)
       -bW_{\delta,\phi}P_{\perp,\phi}((W+W_\delta)\cdot z)\\
 &+g\langle z_2\rangle J_0W_{\delta,\phi\phi}.
 \end{split}
 \tag{NC.13}
$$
Here $b=\beta\sqrt K$, $\alpha=\beta+K_r/(4K)$ and $g=GK^{1/4}$.
The exact derivative of the primitive is the full nonmean projection;
its finite-rank correction is not discarded.

Suppose
$$
 |W|,\ |W_\delta|\le M,\quad
 |W_{\delta,\phi}|\le M_{\delta,1},\quad
 |W_{\delta,\phi\phi}|\le M_{\delta,2},\quad
 |d_\phi|\le D_1.
$$
Then
$$
 A_1^+=D_1+\alpha_++3b_+M^2,\qquad
 B_{10}^H=8b_+MM_{\delta,1}
                       +\frac{b_+M}{2}M_{\delta,2}
 \tag{NC.14}
$$
bound $\|A_1\|_\infty$ and
$\|H_J\mathcal B_{10}\|_{L^2\to L^2}$, respectively.
Indeed $\|I_\phi\|_{L^2\to L^2}\le1/4$ and
$\|P_{\perp,\phi}\|_{L^2\to L^2}=1$.
The last term of (NC.13) has output degree at most96, so its final
$H_J$ projection is exactly zero for both stated values of $J$.
All other occurrences of the low mean in (NC.13) remain in $z$.
Before that projection the complete E bound includes $g_+M_{\delta,2}$.

For the LC component bounds one may take
$$
 M=M_\delta+\eta,\qquad
 M_{\delta,2}\le128M_1+384E_1.
 \tag{NC.15}
$$
The repaired degree32 base gives the factor $4\cdot32=128$ on its
already bounded first angular derivative; the selected degree96
direction gives $4\cdot96=384$ on $E_1$. Neither factor is a frequency
cutoff of the unknown state.

Here $D_1$ must bound the **actual** drift derivative. One safe choice
is $2b_+M^2$. A sharper bound from the same saved LC fields is available.
Let $U_A,V_A$ be the original raw full $A^0$ component bounds,
$R_A=U_A+V_A$, $k_K=\max(1,K_+)$, and
$e_k=3.861\cdot10^{-18}+19d_\nu$, where $d_\nu$ is the selected
parameter half-width. If $D_{\mathrm{raw},1}$ is the saved
$\|d_{\mathrm{raw},\phi}\|_{A^0}$ bound, an admissible choice is
$$
 D_1=D_{\mathrm{raw},1}
   +|\beta|_+k_K(2R_Ae_k+e_k^2)
   +2|\beta|_+k_K\rho\{2(R_A+e_k)+\rho\}.
 \tag{NC.16}
$$
The known repair and canonical difference use the norm-one nonmean
projection in $A^0$; the unknown $C^0$ difference uses its norm-two
bound. This formula does not substitute a reference derivative for
the actual derivative. It uses no derivative of the unknown state.

Define the separate gate
$$
 t_1=\frac{c_p^\#A_1^+}{n}<1,\qquad
 b_{p,1}=\frac{c_p^\#}{1-t_1},\qquad
 b_{r,1}=\frac{c_r^\#}{1-t_1}.
 \tag{NC.17}
$$
The success of $t_0$ alone does not assert (NC.17).

Projecting (NC.12), with $p_L=\Pi_Jp$ and $p_H=H_Jp$, gives exactly
$$
 \mathcal L_Hp_H
 =H_JA_1p_H+H_JA_1p_L+H_J\mathcal B_{10}z
                      +H_J(d\,\partial_\phi p_L)+H_JF_\phi .
 \tag{NC.18}
$$
In particular the low principal column has the plus sign on the right.
Its two complete low-input bounds are
$$
 \|p_L\|_2\le4J\|z_L\|_2,\qquad
 \|\partial_\phi p_L\|_2\le(4J)^2\|z_L\|_2.
 \tag{NC.19}
$$
The zero angular derivatives of the means in (NC.19) do not remove
the undifferentiated means from $\mathcal B_{10}z$.

## 4. Cutoffs, weak states, and the direct high trace

Inside $I_N$, take radial cutoffs $\chi_0,\chi_1$ with values in $[0,1]$,
each zero at the two endpoints of its support, such that $\chi_0=1$
on the support of $\chi_1$ and $\chi_1(c)=1$.
Let $|\chi_0'|\le\kappa_0$ and $|\chi_1'|\le\kappa_1$.
Set
$$
 \begin{aligned}
 Z_L&=\|z_L\|_{2,I_N},&Z_S&=\|z_S\|_{2,I_N},&
 Z_H&=\|z_H\|_{2,I_N},\\
 Z&=\|z\|_{2,I_N},&
 F_0&=\|H_JF\|_{2,I_N},&
 F_1&=\|H_JF_\phi\|_{2,I_N},\\
 E_0&=F_0+C_SZ_S+C_LZ_L+\kappa_0Z_H .
 \end{aligned}
 \tag{NC.20}
$$
First (NC.7) gives
$\|p_H\|_{2,\operatorname{supp}\chi_1}\le b_pE_0$.
Applying (NC.17) to $v=\chi_1p_H$ in (NC.18) then gives
$$
 \begin{aligned}
 G_1={}&F_1+B_{10}^HZ+
         \{4JA_1^++(4J)^2d_+\}Z_L+\kappa_1 b_pE_0,\\
 \|v_\phi\|_2&\le b_{p,1}G_1,\qquad
 \|v_r\|_2\le b_{r,1}G_1,\qquad
 \|v\|_2\le n^{-1}b_{p,1}G_1 .
 \end{aligned}
 \tag{NC.21}
$$
The source $F_\phi$ in this assertion is an actual hypothesis.
For an arbitrary approximate residual, ordinary $L^2$ control of $F$
does not imply this source derivative bound.

The use of (NC.21) does not assume the unknown already has an $H^2$
bound. Initially $z\in H^1$ gives $p_H\in L^2$. The differentiated
identity (NC.18) holds in distributions, and its right side belongs
to $L^2$ under the stated source hypothesis. To justify the energy
estimate, convolve $\chi_1p_H$ in the angular variable with a periodic
approximate identity. The high projection and radial derivative
commute with this convolution. The only principal commutator is
$H_J[d,S_\varepsilon]\partial_\phi(\chi_1p_H)$.
Its $L^2$ norm is uniformly bounded by a fixed kernel constant times
$\|d_\phi\|_\infty\|\chi_1p_H\|_2$, and tends to zero: this follows
by integration by parts in the kernel, verification first on smooth
inputs, and density in $L^2$.
The bounded multiplication commutator with $A_1$ also tends to zero.
For each fixed $\varepsilon$ the convolved equation supplies the radial
$L^2$ derivative, so the compact-support LC energy applies.
Absorb $A_1$ using $t_1<1$ before passing to the limit.
Weak lower semicontinuity gives (NC.21) with the displayed constants.
No auxiliary commutator bound is added to the final sharp estimate.
This argument only uses bounded actual $d_\phi$, radial Lipschitz $a$,
and the stated genuine continuous-state interface condition.

For a Hilbert-valued $v$ zero at both radial ends, the two
fundamental-theorem-of-calculus identities give
$$
 \|v(c)\|^2
 \le\int\|v(r)\|\|v_r(r)\|\,dr
 \le\|v\|_2\|v_r\|_2 .
 \tag{NC.22}
$$
There is no factor two after using both ends. On the high subspace,
$$
 \|z_H(c)\|_{H^1_\phi}
 \le\sqrt{1+n^{-2}}\,\|p_H(c)\|_{L^2_\phi}.
$$
Consequently
$$
 \boxed{\quad
 \|H_J(Q-Q_\delta)(c)\|_{H^1_\phi}
 \le \mathcal T_J G_1,\qquad
 \mathcal T_J=p_c\sqrt{1+n^{-2}}
                 \sqrt{\frac{b_{p,1}b_{r,1}}{n}},
 \quad
 p_c=\max(K(c)^{1/4},K(c)^{-1/4}).
 \quad}
 \tag{NC.23}
$$
The radial physical conversion occurs once, at the final output.
The norm is the Euclidean pair Sobolev norm in the actual moving
circle. A subsequent conversion to a sum of component norms, or to
another physical angle, must use its own stated factor.

## 5. One fixed collar geometry and all five output columns

For a completely explicit reusable geometry, choose any positive
integer $N$ and set
$$
 h=\frac1{40N},\qquad
 I_i=[c-(1/20-ih),c+(1/20-ih)] .
 \tag{NC.24}
$$
Then $I_N=[c-1/40,c+1/40]$.
Let $\chi_0$ be one on $[c-1/80,c+1/80]$, vanish at the two ends of
$I_N$, and be linear in between. Let $\chi_1$ be the triangular cutoff
on $[c-1/80,c+1/80]$ with value one at $c$.
Both derivative bounds are exactly available with
$\kappa_0=\kappa_1=80$. These cutoffs are independent of the unknown
state and can be approximated within the same bounds.

For this paragraph only, use outer-window inputs
$$
 F_0^o=\|H_JF\|_{2,I_0},\quad F_1^o=\|H_JF_\phi\|_{2,I_0},\quad
 Z_S^o=\|z_S\|_{2,I_0},\quad Z_L^o=\|z_L\|_{2,I_0},\quad B_0=\|z_H\|_{2,I_0}.
$$
Put
$$
 \begin{aligned}
 r_N&=40Nk,\qquad
 \eta_N=r_N^N,\qquad
 \sigma_N=k\sum_{j=0}^{N-1}r_N^j,\\
 \Gamma_H&=B_{10}^H+6400b_p,\\
 \Gamma_L&=B_{10}^H+4JA_1^++(4J)^2d_+,\\
 \Theta_N&=80b_p+\Gamma_H\sigma_N .
 \end{aligned}
 \tag{NC.25}
$$
Use $Z\le Z_L+Z_H$, (NC.10), and restriction of each low/source norm.
Equations (NC.21)--(NC.23) give the full five-column inequality
$$
 \boxed{\quad
 \begin{split}
 \|H_J(Q-Q_\delta)(c)\|_{H^1_\phi}
 \le \mathcal T_J\{&
 F_1^o+\Theta_N F_0^o+\Theta_N C_S Z_S^o\\
 &+(\Gamma_L+\Theta_N C_L) Z_L^o
                    +\Gamma_H\eta_N B_0\}.
 \end{split}
 \quad}
 \tag{NC.26}
$$
All columns are nonnegative upper bounds for one complete operator
estimate. Selecting a value of $N$ selects this entire row.
A consumer must not choose entrywise minima from different rows
without separately justifying a common bound.

One can substitute (NC.11) into the last column after the same actual
$C^0$ domain is proved. This does not supply $Z_L^o,Z_S^o$.
In particular, a cap boundary bound is not an interior low body bound.

For a true solution, the selected explicit residual has angular degree
at most288. Thus
$$
 F_1^o\le1152F_0^o\quad(J=96),\qquad
 F_0^o=F_1^o=0\quad(J=288).
 \tag{NC.27}
$$
The frequency $1152=4\cdot288$ is the complete physical bandwidth of
that residual. The already proved NR/WC bound for the same full
$F_{96}$ can be read without reintegrating its source rows.
Its raw mean correction remains in the underlying full residual and
vanishes here only under the actual high projection.
For an approximate state, both $H_JPf$ and $H_JP f_\phi$ remain.

## 6. What is and is not closed

Equations (NC.10), (NC.23), and (NC.26) are proved conditional statements.
They do not assert numerical values for $t_1$, $\mathcal T_J$, any
optimized $N$, or the unknown body/cut inputs. Such new scalar bounds
must be evaluated in the public repository's own Actions from the
already successful complete LC inputs or conclusion, preserving
their exact identities and full parameter domain.

The consumer needs only the saved component bounds and new scalar
assembly. It must not rerun the original Fourier trial, intrinsic
jets, repair, source integrals, or successful LC mathematics.
Finite evaluations of the complete row (NC.26) can report every
candidate and its gate; a failed sufficient gate is not a singularity
claim.

This direct high $H^1$ route does not require the narrow MA high-domain
hypothesis for that trace estimate. It also does not prove that
separate high-domain hypothesis, the low trace, actual core existence,
whole-core matching, the true parameter Schur complement, or the
README's final fixed-metric family.
