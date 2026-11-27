# R149 supplement UDR: unit-disk phase residuals for the original Theta rows

2026-11-27, `visible-exact-astra-fb31ed6-20261127 / trial_restore`.

**Proved.** The complete original signed ASR trial can be kept unchanged
while a new, disk-based phase input certifies its action on all96 original
IR rows. The joint formulas below also pay the action of the coefficient
error on the **infinite** IR inverse error. They do not need the very large
completed ASR scalar error as their only admissible bound. No ASR result,
coefficient, midpoint, phase, mean or SHA is replaced.

This is a new joint-row residual target. It does not report a new execution
of ASR's two already completed scalar targets. The actual UDR products and
resulting row bounds have not yet been computed.

## 1. Actual reason for the new input

The full [ASR actual](../notes/original_alpha_carrier_ci/run-45914639857-1/actual-original-alpha-carrier.json)
and [execution](../notes/original_alpha_carrier_ci/run-45914639857-1/execution.json)
are complete and successful, with respectively

| Whole file | Bytes | SHA-256 |
|---|---:|---|
| actual | 14305 | `7ae6a9ad0c5d142250548e5c72d371b39e3685796ee3e38484ca3fbf0eadd68c` |
| execution | 17495 | `e65e2161db85f3970893ffac4270c09c2ae5d38bbcde40e806ce399adca3c1b8` |

The execution ended at `2026-11-27T01:26:55.013225+00:00`, with all2048
modes and both complete scalar targets. Their saved full balls give
$e_{\alpha,\infty}<7.954\,10^{220}$ and
$e_{\alpha,2}<3.469\,10^{220}$. The saved entire tails are much smaller:
the Linfinity tail is below $0.000102493$, and the L2 tail is below
$2.772\,10^{-6}$. These facts do not identify a singular operator.

The finite-input source
`fourfold_codazzi_original_alpha_full_source_math.py:WholeQuadrature`
updates8192 complex **rectangles** by `powers = powers * steps`, for2048
successive modes. A fixed real rotation maps a rectangular error of equal
coordinate radii to a rectangle whose coordinate radii may be multiplied
by $|\cos\theta|+|\sin\theta|>1$. Iterating this enclosure can therefore
amplify an initially tiny width exponentially, although the exact phase
powers have modulus1. The new method proves a circular error invariant
instead of interpreting such a rectangular width as an intrinsic norm.

The original exact signed alpha trial remains the whole95675-byte object
with SHA
`df6ed2ab4f3b12ecb6f3510401995291bcc989fa89f92f3712496845962d2e85`.
The old full raw192 and8192-point grid retain their SHA identities
`c692148e7e84530ed138bdb607ebe9eac645e5af1716e8825a2fbc225d2a406f`
and `f5daf796446064ba9d39894664d121970366357b6d2258b127c3ef6b82a7eab9`.
The already completed IR trial and, once complete, OT finite-row carrier
are likewise immutable inputs. Necessary recovery of their exact finite
bytes does not run their completed residual or norm reducers.

## 2. An exact unit-disk recurrence, with explicit rounding residuals

Use the normalized circle of physical period $\pi/2$, so Fourier mode$n$
has physical frequency$4n$. Let $N=8192$ and $x_m=\pi m/(2N)$. At each
node the whole original grid encloses the real values

\[
 t_m=\widehat t(x_m),\qquad g_m=\widehat G(x_m),\qquad
 \zeta_m=e^{-4ig_m},\qquad |\zeta_m|=1.                 \tag{UDR.1}
\]

Here $\widehat t$ is the complete raw192 trial **including its mean**,
and $\widehat G=K_{48}\circ H_{24}$ is the original finite map. Write
$u_m$ and$s_m$ for exact dyadic centers, with directed certificates

\[
 |t_m-u_m|\le\eta_m,\qquad |\zeta_m-s_m|\le\tau_m.
                                                               \tag{UDR.2}
\]

These are certificates of the saved grid's complete balls, including its
decimal conversion. They do not replace$g_m$ or the true map by a center.

Choose $c_{m,0}=1$. At each step choose any exact dyadic$c_{m,n+1}$ and
certify the complete finite multiplication residual

\[
 \rho_{m,n}\ge|c_{m,n}s_m-c_{m,n+1}|.
\]

In implementation it is the midpoint of the new directed product, and
the whole product-minus-midpoint ball supplies$\rho$. Starting$d_{m,0}=0$,
save an outward upper satisfying

\[
 d_{m,n+1}\ge d_{m,n}+(1+d_{m,n})\tau_m+\rho_{m,n}.
                                                               \tag{UDR.3}
\]

Then, for every node and every$n\le2048$,

\[
 |\zeta_m^n-c_{m,n}|\le d_{m,n}.                         \tag{UDR.4}
\]

Indeed the difference at the next step is exactly

\[
 (\zeta_m^n-c_{m,n})\zeta_m
       +c_{m,n}(\zeta_m-s_m)
       +(c_{m,n}s_m-c_{m,n+1}).
\]

The first term costs$d_{m,n}$ because$|\zeta_m|=1$; also
$|c_{m,n}|\le1+d_{m,n}$. This proves (UDR.3--4) inductively.
No multiplication by$|\cos|+|\sin|$ occurs, and no normalization of a
true phase, omission of a rounding radius or floating stability assumption
is used. A large computed residual remains large; the formula cannot
declare an unstable approximate center accurate.

Choose an exact dyadic$q_n$ and certify

\[
 \sigma_n\ge\left|N^{-1}\sum_m u_m c_{m,n}-q_n\right|.
\]

For the complete discrete integral$Q_n=N^{-1}\sum_m t_m\zeta_m^n$,

\[
 |Q_n-q_n|\le R_n:={1\over N}\sum_m
             (\eta_m+|u_m|d_{m,n})+\sigma_n.              \tag{UDR.5}
\]

This follows by writing
$t_m\zeta_m^n-u_mc_{m,n}=(t_m-u_m)\zeta_m^n+
u_m(\zeta_m^n-c_{m,n})$. Every8192 term is kept. A complex rectangle
with both coordinate radii$R_n$ contains this disk and may be used in
the following directed cohomological formula. Its modest enlargement
does not reintroduce a2048-step rectangular recurrence.

## 3. Residual to the **same** original signed alpha trial

Use the exact original quadratic rotation$\Omega$ and the entire source
phase ball$b=2H(0)+\Omega$. For each$n=1,\ldots,K$, $K=2048$, put

\[
 q=e^{-4in\Omega},\quad t=e^{-4inb},\quad
 d_n^-\le|q-1|,\quad d_n^->0,
 \qquad L_n(v)={qv+t\overline v\over q-1}.                \tag{UDR.6}
\]

This is the original AS/ASR cohomological divisor and original moving
reflection; no phase reset, denominator midpoint or unrelated normalizer
is introduced. Let$\mathcal Q_n$ be the disk enclosure in (UDR.5), and
let$\widehat\alpha_n$ be the exact coefficient of the **old entire**
signed carrier. The complete new directed coefficient residual is

\[
 \Delta_n\ge |L_n(\mathcal Q_n)-\widehat\alpha_n|
       +{2\over d_n^-}(E_n+M_n+A_n).                     \tag{UDR.7}
\]

Here$|L_n(\mathcal Q_n)-\widehat\alpha_n|$ means an upper for the
absolute value of the full ball. The already proved AS.10--12 supply
the full source/model/alias payments, in unchanged units:

\[
 \begin{aligned}
 E_n&=\min_{0\le r\le3}{E_r\over(4n)^r},\\
 M_n&=4nE_HTe^{-4nm\sigma},\\
 A_n&={2T e^{4nG_1\sigma}a\over1-a},\qquad
 a=e^{-4\sigma N},\quad \sigma=1/128.                     
 \end{aligned}                                             \tag{UDR.8}
\]

All$E_r$, $E_H$, $T$, $G_1$, and the positive lower$m$ are the whole
completed ASR global records. The already completed whole tail records
$T_\infty,T_2$ from ASR are reused directly. The source includes all
ordinary transport errors and the complete source192. Thus (UDR.7)
proves$|\alpha_n-\widehat\alpha_n|\le\Delta_n$ for all2048 modes;
the negative coefficients are conjugates, both exact means are zero,
and the full tail beyond$K$ is still present. This certifies a residual
to an existing trial; it does not substitute a new alpha trial or
recompute ASR's original two scalar conclusions.

For the proof only, abbreviate

\[
 D_\infty=2\sum_{n=1}^K\Delta_n+T_\infty,
 \qquad D_2=\left(2\sum_{n=1}^K\Delta_n^2+T_2^2\right)^{1/2}.
                                                               \tag{UDR.9}
\]

The new computational outputs are the **weighted joint products** below.
The implementation accumulates their whole weighted contributions and
does not publish replacement ASR scalar targets. In particular a missing
mode or tail cannot be replaced by a progress counter.

## 4. Paying the coefficient error on the infinite inverse error

Use exactly the real zero-mean Hilbert spaces, physical frequency$4n$,
$G=|\partial_x|^{-1}$, $I=\partial_x^{-1}$ and original same-sign

\[
 T_f=\Pi_+M_f\Pi_++\Pi_-M_f\Pi_-,\qquad
 A=Id-T_\alpha I,
\]

from [DT](R149-supplement-original-same-sign-source-Toeplitz-and-Theta-row-action.md).
Let$Z$ denote the96 true energy-adjoint inverse columns in IR and
$Y=\widehat Z$ their complete original192-mode trial. Put$E=Z-Y$.
The original whole IR residuals and SDI imply

\[
 \|E\|_{\ell^2_{96}\to\dot H^{-1/2}_0}\le\epsilon_H,
 \quad \|E\|_{\ell^2_{96}\to L^2_0}\le
 S:={51\over50}(\epsilon_0+\tfrac{10}{9}\epsilon_H).       \tag{UDR.10}
\]

These bounds include all infinite modes, aliases and true-map errors;
the proof is DB's complete inverse bootstrap with SDI.5--6. No finite
Galerkin residual is being used as a whole-space inverse error.

For any real zero-mean$h\in L^2$,

\[
 \|\Pi_+Gh\|_\infty
 \le\left(\sum_{n\ge1}{1\over(4n)^2}\right)^{1/2}
               \|\Pi_+h\|_2
 ={\pi\over8\sqrt3}\|h\|_2.                            \tag{UDR.11}
\]

Here the positive and negative Fourier energies of a real$h$ are equal.
If$f$ is real, the two sign blocks of$T_fGh$ are conjugate and
orthogonal. Consequently

\[
 \|T_fGh\|_2\le{\pi\over4\sqrt6}\|f\|_2\|h\|_2
             <{1\over3}\|f\|_2\|h\|_2.                  \tag{UDR.12}
\]

For example$\pi<22/7$ proves the last strict rational comparison.
For the joint real96-column operator apply this to each unit input
vector; no additional$\sqrt{96}$ arises. Also the ordinary$L^\infty$
multiplier estimate and$\|G:H\to L^2\|\le1/2$ give

\[
 \|T_{\alpha-\widehat\alpha}GE\|
 \le P_E:=\min\{D_\infty\epsilon_H/2,\ D_2 S/3\}.       \tag{UDR.13}
\]

Let$J_G\ge\|GY\|_{HS}$ and
$B_G\ge\sum_{l=1}^{192}(\sum_j|Y_{lj}|^2/(4l)^2)^{1/2}$
be the complete already computed OT finite-carrier norms, retaining
every signed coefficient. TP's complete joint product proof gives

\[
 \|T_{\alpha-\widehat\alpha}GY\|
 \le P_Y:=\min\{D_\infty J_G,\ \sqrt2 D_2B_G\}.          \tag{UDR.14}
\]

All four whole candidates in (UDR.13--14) must be saved/read before
either minimum is used. This retains the full coefficient error on
the **unseen inverse tail**$E$ as well as on the finite trial$Y$.

## 5. Complete original VQ and Theta row bounds without a giant alpha fee

Let$A_Y\ge\|\widehat\alpha\|_\infty$ be the entire saved OT
finite Wiener norm. The original row column is$A^*GZ$, and its unchanged
trial is$\widehat A^*GY$, where$\widehat A=Id-T_{\widehat\alpha}I$.
Exactly,

\[
 A^*GZ-\widehat A^*GY
 =GE+I T_{\widehat\alpha}GE
       +I T_{\alpha-\widehat\alpha}GE
       +I T_{\alpha-\widehat\alpha}GY .                    \tag{UDR.15}
\]

This uses$A^*=Id+IT_\alpha$, in the original order; the coefficient
is not commuted through$I$ or a sign projection. Since$\|I\|_2\le1/4$,
the entire joint full-L2 row error is bounded by

\[
 \boxed{E_{VQ}\le{\epsilon_H\over2}
       +{1\over4}\left({A_Y\epsilon_H\over2}+P_E+P_Y\right).}
                                                               \tag{UDR.16}
\]

Applying the physical derivative to (UDR.15) gives a unitary sign
multiple of$E$ plus the three full multiplication terms. On the
mean-zero circle,$\|u\|_{H^1}\le(\sqrt{17}/4)\|\partial_xu\|_2$.
Therefore the whole one-loss bound is

\[
 \boxed{E_{H^1}\le{21\over20}
          \left(S+{A_Y\epsilon_H\over2}+P_E+P_Y\right).}   \tag{UDR.17}
\]

No derivative of$\alpha$ is silently requested. For the original
qualified model$\overline G:Y_a^0\to H^{-1}$ with bound$K_G$ and
the complete saved OT model/rounding error$E_M$,

\[
 \|\Theta-\widehat\Theta\|\le K_G E_{H^1}+E_M.           \tag{UDR.18}
\]

The original full candidate may use$K_G=512$ in its already qualified
CYA scope. For the low96 input restriction, TQL's exact isometry of
$\overline GE_{96}$ instead yields

\[
 \|\Theta E_{96}-\widehat\Theta E_{96}\|
       \le E_{VQ}+E_{M,96}.                               \tag{UDR.19}
\]

Here$E_{M,96}$ must cover every entry of the whole96-by96 finite block,
including its true phase; it is not a subset of a gate or a midpoint
replacement. The existing complete global/low candidates may both be
retained before a whole-bound comparison. UDR does not itself assert
that any finite inverse gate has passed.

The original source/target reflections$b=a+\Omega$, nonunitary angular
maps already paid in IR/ASR, mean-zero coefficient condition, complete
CYA high model scope and **two independent physical mean slots** all
remain. This result does not convert SC raw96 pairings into full physical
columns, or imply the positive58/224 inverse, physical signed square,
phase/parameter border, nonlinear family or topic completion.

The accompanying [pure formulas](../scripts/fourfold_codazzi_unit_disk_Theta_residuals.py)
implement precisely (UDR.2--18). A public actual owner must restore and
verify every old carrier SHA, consume the whole completed ASR/IR/OT
records, save all2048 new natural residual records, and publish the four
complete products and the full joint row conclusions. It must not call
the old ASR scalar, old IR residual or old OT norm targets.
