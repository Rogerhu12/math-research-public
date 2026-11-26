# R144 supplement: the complete positive hybrid adapter for the compact centre

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved.** This gives the exact difference between the compact physical
differential and the original WVC hybrid, in the original low193 and
infinite high spaces. Its two cross blocks use only the shell 97--160,
and their complete moving-mean row or column is zero. The whole positive
relative optical-speed change is less than $1.893\,10^{-7}$. On the
positive part of the already completed core window, the raw low-input
fee is less than $0.002130$ and the raw high-to-low fee is less than
$0.003499$. The compact centre has exactly zero direct high ordinary
Newton source and zero direct high affine jumps.

The original WVC reference Green, fixed weights, true root, root97
and outer96 observations are retained. A full positive inverse is not
asserted: the whole positive low receiver and a high principal update
are still necessary. In particular an ordinary high-source bound with
one third of an angular derivative does not absorb an unbounded
first-order coefficient perturbation for free.

## PA1. One physical centre on the entire positive interval

Use the objects of [SM](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md),
[SC](R144-supplement-selected-metric-compact-residual-and-full-operator-fees.md)
and [RTC](R144-supplement-actual-root-Cauchy-and-true-cut-for-compact-centres.md).
Put $I=[a,R]$, where $a$ is the original true positive root and $R=25/8$.
The whole interval lies strictly above $9/50$. Thus the compact metric
bump and the density control both vanish there. For every real
$|\delta|\le10^{-10}$,

$$
 \widetilde Q_\delta|_I=Q_*=(u,tv),\qquad
 t=M/m,\quad m=\langle v\rangle,\quad |M-m|<2\,10^{-7},
 \qquad (K_\delta,\gamma_\delta)|_I=(K,\gamma)|_I.
 \tag{PA.1}
$$

Here $(u,v)$ is the original raw degree32 state and $M$ is the unique
compact terminal mean at $\delta=0$. This is equality of functions;
it does not mean that $Q_*$ is already a nonmean solution. In particular
$Q_*(R)=(u,v)(R)$ exactly, including all angular derivatives.

Let $Q_c=(u_c,v_c)$ be the original repaired degree32 centre,
$m_c=\langle v_c\rangle$, and
$Q_\delta^{\rm sel}=Q_c+\delta Z$, $m_\delta=\langle v_\delta^{\rm sel}\rangle$.
Write $e=Q_*-Q_c$ and $e_m=\langle e_2\rangle$. The actual saved bounds
quoted in SC and RTC give

$$
 \begin{gathered}
 \|e\|_{A^0,\rm pair}<E_0=3.848\,10^{-7},\qquad
 \|e_\phi\|_{A^0,\rm pair}<E_1=1.020\,10^{-6},\\
 |e_m|<2.001\,10^{-7},\qquad
 |M-m_\delta|<E_m=2.021\,10^{-7},\\
 \|Q_c\|_{A^0,\rm pair}<7,\qquad
 \|(Q_c)_\phi\|_{A^0,\rm pair}<6 .
 \end{gathered}
 \tag{PA.2}
$$

For example $2\,10^{-7}\|v/m\|_{A^0}<2\,10^{-7}(1.923)$,
and the complete repair contributes less than $3.861\,10^{-18}$.
The angular estimate is
$2\,10^{-7}(5.438)/1.068+1.970\,10^{-17}<1.020\,10^{-6}$.
The last mean estimate adds the entire $19\,10^{-10}$ selected-direction
fee. All comparisons are at the same moving angle.

Since $|m|>1.068$ and the old mean has the negative sign,

$$
 \left|{M-m_\delta\over m_\delta}\right|
 <{2.021\,10^{-7}\over1.068-3.861\,10^{-18}-19\,10^{-10}}
 <1.893\,10^{-7}.
 \tag{PA.3}
$$

Hence the new speed $-\gamma M$ is positive and differs relatively
from the same selected speed $-\gamma m_\delta$ by this amount.
This proves a full positive sign and relative coefficient bound;
it does not yet transfer a Riccati frame or its source kernels.

## PA2. Exact full difference, including the mean rank

Put $D=\operatorname{diag}(1,K)$ and
$J=\left(\begin{smallmatrix}0&K\\-1&0\end{smallmatrix}\right)$.
The full physical field and differential are those of SC. The WVC
hybrid is exactly

$$
 A^c=D_QF(Q_c)+\gamma(m_\delta-m_c)J\partial_\phi .
 \tag{PA.4}
$$

This follows directly from the existing
`_complete_centre_packet`, `_local_signed_entry` and
`_centre_mean_row` in
[`fourfold_codazzi_true_collar_signed_packet_math.py`](../scripts/fourfold_codazzi_true_collar_signed_packet_math.py):
the principal uses `actual_eta=-gamma*m_delta`; all lower coefficients,
the independent mean-input rank and the complete output mean row use
the repaired degree32 centre.

Define $T=2Q_c^tDe+e^tDe$. For every full physical direction $h$,
the difference $E=A_*-A^c$, $A_*=D_QF(Q_*)$, is

$$
 \begin{aligned}
 Eh={}&[-\beta\mathcal I T\,I_2+\gamma(M-m_\delta)J]h_\phi\\
 &-\beta\{Th+2e(Q_c^tDh)+2Q_c(e^tDh)+2e(e^tDh)\}\\
 &-2\beta\{e_\phi\mathcal I(Q_c^tDh)
       +(Q_c)_\phi\mathcal I(e^tDh)
       +e_\phi\mathcal I(e^tDh)\}\\
 &+\gamma\langle h_2\rangle J e_\phi .
 \end{aligned}
 \tag{PA.5}
$$

Each primitive means $\mathcal I=\partial_\phi^{-1}P_{\ne0}$.
In particular the three ordered primitive words cannot be replaced
by one product with a zero intermediate mode. The principal mean
difference is $M-m_\delta$, whereas the last line uses $e_\phi$.
Replacing both by the same scalar mean error would lose a real term.

Proof: subtract the displayed full differential in SC at $Q_c+e$
and $Q_c$, then subtract the principal correction in (PA.4).
Expanding the quadratic energy gives $T$; expanding the two factors
of the primitive gives exactly the three displayed words. The mean
rank is linear in $Q_\phi$. This proves (PA.5), including its output
mean, before taking any projection or norm. No radial derivative of
$e$, a weight, or an approximate state is used. $\square$

The accompanying pure adapter
[`fourfold_codazzi_compact_positive_hybrid_adapter.py`](../scripts/fourfold_codazzi_compact_positive_hybrid_adapter.py)
forms these signed entries with the existing complete ordered
assembly. It accepts whole-cell enclosures of the raw and repaired
degree32 coefficients, $M-m$, and $\delta Z_m$. It never computes a
new Green, changes a reference matrix, or calls an old producer.

## PA3. Exact block supports and genuine zero sources

Let $P$ retain odd96, the independent moving even mean, and even96;
let $H=I-P$. Each coefficient in the local and drift terms of (PA.5)
has degree at most64. Each primitive word has two factors of degree32.
Consequently

$$
 HE P=H_{97:160}EP,\qquad
 PE H=PEH_{97:160}.
 \tag{PA.6}
$$

The same statements hold for $A^c$ and $A_*$. They hold for the
complete physical differential, before any density division.
The radial principal difference is diagonal in the nonzero angular
frequency and therefore contributes to neither cross block.
The mean-input rank has output at most32 and also contributes to
neither cross block. Furthermore

$$
 HE\,\iota_m=0,\qquad \pi_m EH=0,
 \quad HA_*\iota_m=0,\qquad \pi_m A_*H=0 .
 \tag{PA.7}
$$

For the first identity, a constant input produces output at most64
in every term. For the second, the complete mean row of a physical
differential is

$$
 \langle (A_Qh)_2\rangle
 =\beta\{(1-\langle u^2+Kv^2\rangle-2K\langle v\rangle^2)
                 \langle h_2\rangle
 -2\langle v\rangle\langle uh_1+Kv_{\ne0}h_2\rangle\}.
 \tag{PA.8}
$$

It reads only the degree32 coefficients of $u,v$. A high input has
zero pairing and zero mean. The sign of the odd real coordinate
agrees with the original `ui` encoding; (PA.8) is the physical
function identity underlying the original signed mean row.

SC proves that $R_*=Q_{*,r}-F(Q_*)$ has degree at most96, with zero
even mean, and that each actual value jump of $Q_*$ has degree32
and zero even mean. Thus, on the full positive interval,

$$
 HR_*=0,\qquad H[Q_*]_i=0,\qquad
 \|R_*\|_{L^2_{r,\phi}}<8.965\,10^{-4}.
 \tag{PA.9}
$$

The affine low jumps remain their exact signed values; their sum
is bounded by $3.028\,10^{-12}$ in the common raw pair units.
Equations (PA.7)--(PA.9) do not set a returned high solution, an
independent high boundary port, or either physical-density mean to
zero. In particular a nonzero low correction creates a genuine high
response through $HA_*P$.

## PA4. Actual core fees and the complete whole-positive integrands

Let $b\ge|\beta|$, $g\ge\gamma$ and $k\ge\max(1,|K|)$ be valid
pointwise positive functions. Define

$$
 \begin{gathered}
 C=14E_0+E_0^2,\qquad
 L=3bkC+{bk\over2}\{6E_0+(7+E_0)E_1\},\\
 M_1={bkC\over4}+gkE_m,\qquad M_0=L+gkE_1 .
 \end{gathered}
 \tag{PA.10}
$$

The full physical difference satisfies
$\|Eh\|_2\le M_1\|h_\phi\|_2+M_0\|h\|_2$.
For the two cross blocks, the two $g$ terms vanish exactly, so valid
raw fees are

$$
 \begin{aligned}
 e_{LL}&=M_0+384M_1,\\
 e_{HL}&=L+384bkC/4,\qquad
 e_{LH}=L+640bkC/4.
 \end{aligned}
 \tag{PA.11}
$$

These follow by the same $A^0$ multiplication and $\|\mathcal I\|_{2\to2}=1/4$
estimates as SC. The derivative bound640 in the last line uses the
actual shell (PA.6); it does not truncate a high response.

In the completed D calculation put $e_0^o=19\,10^{-10}$ and
$e_1^o=83\,10^{-10}$. Exact rational comparison gives

$$
 \begin{gathered}
 14E_0+E_0^2<203(14e_0^o+(e_0^o)^2),\\
 6E_0+(7+E_0)E_1<203\{6e_0^o+(7+e_0^o)e_1^o\},\\
 E_m<203e_0^o,\qquad E_1<203e_1^o.
 \end{gathered}
 \tag{PA.12}
$$

Every extra intrinsic metric term in the old positive majorants is
nonnegative. Thus $M_j\le203M_j^o$ on their actual proved domain.
The whole saved endpoints from public run43713242980/1 yield

$$
 \begin{array}{c|rrrr}
 \text{domain}&M_0&M_1&e_{LL},e_{HL}&e_{LH}\\ \hline
 I\cap[0,9/10]&7.663\,10^{-5}&5.347\,10^{-6}
                       &0.002130&0.003499 .
 \end{array}
 \tag{PA.13}
$$

The last bound uses $203(\sup M_0^o+640\sup M_1^o)$; the low
bound uses the sharper saved maximum of $M_0^o+384M_1^o$.
These comparisons and (PA.2)--(PA.3) are implemented in
[`fourfold_codazzi_compact_positive_hybrid_saved_bounds.py`](../scripts/fourfold_codazzi_compact_positive_hybrid_saved_bounds.py).
No native rows, quadratures or scientific targets are reevaluated.
The domain in (PA.13) is not extended to $R$.

For a whole-positive evaluation, (PA.10)--(PA.11) are the complete
new scalar integrands, including the independent principal-mean
term. They can be evaluated on the existing intrinsic coefficient
rows. The signed adapter permits a tighter complete assembly instead.
Neither route calls for recomputing the old defect Green.

## PA5. Original weights, every atom, point sources and true boundaries

Keep exactly the WVC $S_i=\operatorname{diag}(I_{96},q_i,q_iI_{96})$,
the model $\bar A_i=H_i/h_i$, both original boundary operators and
$\mathcal O$ from [G.1--G.7](R141-low193-directed-green-and-complete-observation-certification.md).
In particular $q_i$ is not changed to $\sqrt K$, to a new mean,
or to a new Riccati variable. Put $s_i=\max(1,q_i)$ and
$s_i^-=\max(1,q_i^{-1})$. The correct source roles are

$$
 \begin{array}{c|c|c}
 \text{new object}&\text{raw source into the old low Green}&
                  \text{pointwise conservative fee}\\ \hline
 \text{low perturbation}&PEP S_i^{-1}&e_{LL}s_i^-\\
 \text{high return perturbation}&PEH_{97:160}&e_{LH}\\
 \text{new low-to-high source}&HA_*P S_i^{-1}&
 (\|HA^cP\|+e_{HL})s_i^- .
 \end{array}
 \tag{PA.14}
$$

An ordinary $H^{1/3}$ high source in the last line pays
$\Lambda_{160}=(1+16\cdot160^2)^{1/6}$ on its actual finite output.
A rough $H^{-1}$ high input in the second line pays
$\sqrt{1+16\cdot160^2}$ on its actual finite input. There is no288
shell fee in these new cross blocks. A comparison with the old
selected *actual* operator must separately retain its old192-band
family difference, which does have the288 shell.

The left output weight is supplied by $\mathcal O\bar G$ or
$\mathcal OG_L^c$, never by adding an extra $S$ to the raw source.
If one instead estimates $SE_{LL}S^{-1}$ directly, its coefficient
fee is $s_i e_{LL}s_i^-$; this is a different typed quantity.

For any completed model source bound $(g_B,g_a,g_R)$, the new low
perturbation has the same three output slots. If PS/NS supplies
the true hybrid inverse, let

$$
 \ell_B=\|SG_L^cPEP S^{-1}\|,\quad
 \ell_a=\|R_a\operatorname{ev}_aG_L^cPEP S^{-1}\|,\quad
 \ell_R=\|\Theta R_b\operatorname{ev}_RG_L^cPEP S^{-1}\|.
 \tag{PA.15}
$$

The sufficient low gate is $\ell_B<1$. Only the body norm is
tested against one. For a source with true hybrid bounds
$(b_W,a_W,r_W)$ the compact low inverse then has bounds

$$
 {b_W\over1-\ell_B},\qquad
 a_W+{\ell_a b_W\over1-\ell_B},\qquad
 r_W+{\ell_R b_W\over1-\ell_B}.
 \tag{PA.16}
$$

This is the same signed resolvent identity as G.29, with a new
declared source. Alternatively use the original model directly:
its total defect source is $(A_L^c-\bar A)S^{-1}+PEPS^{-1}$.
The valid body test is $\varepsilon+g_{E,B}<1$ (or a smaller
signed joint bound), not $\varepsilon<1$ alone. Root97 and outer96
fees add in their own slots. The old model and every already
completed old source moment remain unchanged.

At an actual impulse location $s$, retain
$G(r,s)S(s)^{-1}$ and the full endpoint observations of this kernel.
If $p_s$ bounds the old body point-source column and $p_a(s),p_R(s)$
its two atom outputs, (PA.16) applies with $b_W=p_s$ and the
corresponding two $p$'s. There is no artificial square root of a
radial length. The analogous resolvent identity at a receiver point
uses the old genuine point receiver, not a body $L^2$ trace.
Independent atom inputs still have their original identity block.
The physical raw unknown is continuous across coefficient jumps;
the transformed unknown keeps the exact transmission
$x^+=S_+S_-^{-1}x^-$ and all declared affine jump sources.

The root96 boundary conditions, root odd96 plus mean outputs,
and outer even96 observations have not been changed by this
coefficient comparison. The true physical outer97 rows still use
the complete nonlinear angle/DN/mean chart. At the new centre their
argument is exactly the raw endpoint by (PA.1), differing from the
repaired zero-parameter endpoint by only the complete repair.
This identifies the small input to that chart's derivative, but a
bound for the chart derivative or its difference must still be
consumed. A small endpoint input is not itself a physical-boundary
operator estimate. Both physical-density means and the independent
height source remain distinct from the moving mean in (PA.15).

## PA6. All four blocks and the actual remaining smallness test

The existing true $G_H^{\rm sel}$ is for the full selected differential,
including its original high boundary graph, not the hybrid high
block. Accordingly the high-high body difference is

$$
 E_{HH}^{\rm sel}=H(A_*-D_QF(Q_\delta^{\rm sel}))H
                 =HEH-H(D_QF(Q_\delta^{\rm sel})-A^c)H.
 \tag{PA.17}
$$

The second summand is the already defined complete old family
difference. In the first summand, the principal and drift terms
of (PA.5) are still first order on an arbitrary infinite high state.
Although (PA.3) is small, an ordinary-source map
$L^2H^{1/3}\to L^2L^2$ alone does not bound the composition with
either of these terms. The required new item is a full bounded
high perturbation operator in the original state/source graph
spaces (or a direct energy/Riccati certificate with the changed
principal), with its actual outer high boundary difference included.
It is not a finite shell computation.

For clarity, after such a certificate, use the original hybrid low
inverse and the original selected high inverse as the two reference
resolvents. Let $x=Sh_L$ and let $y$ be the original complete high
state, with its legitimate root and outer readouts. The exact body
equations, together with high boundary corrections, have the form

$$
 \binom{x}{y}=\binom{x_0}{y_0}+
 \begin{pmatrix}\mathcal L&\mathcal C\\
                 \mathcal B&\mathcal H\end{pmatrix}
 \binom{x}{y}.
 \tag{PA.18}
$$

Here $\mathcal L=SG_L^cPEPS^{-1}$,
$\mathcal C=SG_L^cPA_*H$ with the same ordinary/rough units as its
declared input, and $\mathcal B$ contains $G_H^{\rm sel}HA_*PS^{-1}$
and the actual low-to-high boundary columns. The operator
$\mathcal H$ contains (PA.17) and the true high-to-high boundary
change. No one of these four blocks has been omitted.
If their actual same-space bounds are respectively
$\ell,c,b,h$, the complete sufficient body gate is

$$
 \ell<1,\qquad h<1,\qquad cb<(1-\ell)(1-h).
 \tag{PA.19}
$$

Under this gate, positive inversion of the $2\times2$ matrix
majorant gives the explicit complete body bound

$$
 \binom{\|x\|}{\|y\|}
 \le {1\over(1-\ell)(1-h)-cb}
 \begin{pmatrix}1-h&c\\b&1-\ell\end{pmatrix}
 \binom{\|x_0\|}{\|y_0\|}.
 \tag{PA.20}
$$

Convergence follows, for example, by a positive diagonal weighting
which makes the nonnegative matrix strictly contractive; (PA.19)
is exactly its two-dimensional spectral-radius condition. Every
root97, outer96, point and physical-mean output is then its original
source output plus its two actual receiver bounds times the two
body responses. Those observations do not enter (PA.19) as artificial
extra contraction requirements.

Finally impose the complete physical right97 plus outer96 finite
system of H.17--H.18 in
[the original GH contract](R141-supplement-actual-GH-source-window-and-return-contract.md),
using the actual new Poisson columns and the complete new outer
chart. The shapes $97^2$, $97\times96$, $96\times97$, $96^2$,
the true root96 data and root97 outputs are unchanged. Norm bounds
such as (PA.20) do not supply its signed matrix or a determinant.

Thus (PA.5), (PA.10)--(PA.17) specify exactly what can be reused and
what new inputs must be received, while (PA.3), (PA.6)--(PA.9) and
(PA.13) are already paid facts. At present no full PS defect bound,
whole positive compact low perturbation receiver or bounded high
principal update has been supplied; no whole-positive gate is
reported as passed. The negative RTC receiver, the nonlinear tame
bounds, the physical Schur rows and the final fixed-metric closed
family remain separate obligations.
