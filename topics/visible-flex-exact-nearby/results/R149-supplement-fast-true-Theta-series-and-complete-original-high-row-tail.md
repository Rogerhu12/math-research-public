# R149 ASQ17. The genuine full $\Theta$ row and its high-input tail

Use [DC.9](R149-supplement-same-sign-density-compression-and-finite-Theta-rows.md) in its original order,
$$
 \Theta=E_{96}^*D_+^{-1}C^{-1}A\bar G,\qquad A=Id-\mathcal T_\alpha I .
$$
Here $D_+$ is the fixed sign phase and $E_{96}$ injects the actual normalized natural reflected low basis. In particular the low projection immediately before this readout is the genuine $Q_{97}$. The following applies to all 96 rows jointly and includes the original frequency-$4n$ primitive.

## A summable, uniform inverse for the complete row

[ASQ12.2](R149-supplement-all-positive-i-safe-modes-in-the-physical-waist-square.md) gives $\|D\|<.08$, $\|S^{-1}\|<1.013$ in both $L^2_0$ and $\dot H^{-1}_0$ for the actual $D=S-C$. Thus $K=S^{-1}D$ has both norms less than $.082$ and
$$
 C^{-1}_{[k]}=\sum_{j=0}^{k-1}K^j S^{-1},\qquad
 \|C^{-1}-C^{-1}_{[k]}\|_{\dot H^{-1}\to\dot H^{-1}}
      <1.11(.082)^k,\quad k\ge1 .                           \tag{ASQ17.1}
$$
The same estimate holds for $L^2$ and, by ordinary duality, on $\dot H^1$ for the corresponding adjoint. The exact same-sign inverse is unique in these windows. The formula can use the true signed opposite-sign density and its inverse, or their exact matrix actions on a specified test. It requires no approximate selected inverse or contraction of the unsigned diagonal density.

The true [ASQ16 all-frequency fee](R149-supplement-actual-all-frequency-primitive-and-single-physical-gate.md) together with $1/(4n)\le1/4$ on the 96 low reference isometries gives $\|I\bar G\|\le1.28$ on the whole reflected target. As $\|\mathcal T_\alpha\|_0<1.43$ and $\|I\|\le1/4$,
$$
  \|A\bar G\|_{2\to\dot H^{-1}}
           \le(1+1.43/4)1.28 .
$$
The full selector $E_{96}^*D_+^{-1}$ from $\dot H^{-1}$ has norm at most $384$, the **largest physical frequency** in that finite subspace, with no factor $\sqrt{96}$. Hence
$$
 \|\Theta-E_{96}^*D_+^{-1}C^{-1}_{[k]}A\bar G\|
 \le 744(.082)^k .
                                                               \tag{ASQ17.2}
$$
For $k=12$ this is below $10^{-10}$, including every ordinary frequency. For $k=16$ it is below $4\cdot10^{-15}$. These are truncation costs when the indicated operators use the actual lift and actual multipliers. A numerical implementation that also approximates the primitive, coefficients or phase must add the full action residuals. In particular the order of all 12 terms and actual-sign density factors is part of the row.

## A small true tail for all 96 rows

Let $a=9/640$, as in [ASQ13](R149-supplement-opposite-density-inverse-on-original-high-frequency-inputs.md). There
$$
 C^{-1}=C'-D'(C')^{-1}D',\qquad
       \|D'\|_0<.088,\quad\|(C')^{-1}\|_0<1.12 .
$$
In ordinary $L^2$ units a right input supported on $n\ge N$ gives
$$
 \|Q_{97}C^{-1}P_{\ge N}\|_{0\to0}
  \le45\,\Gamma_N,\qquad
 \Gamma_N=(\sum_{n\ge N}e^{-2an})^{1/2}<6.1e^{-aN}.      \tag{ASQ17.3}
$$
Indeed the exact same-sign low output in $C'$ costs $44\Gamma_N$ and the opposite-sign input to $D'$ costs $6.4\Gamma_N$. Their sum is less than $45\Gamma_N$ by ASQ13. The analogous bound on a diagonal input $\bar G P_{\mathcal J}$ is $45\,(\sum_{n\in\mathcal J}(4ng_n)^2e^{-2an})^{1/2}$.

Suppose $\mathcal J\subset[N,\infty)$, $N\ge4097$ odd, and $g_n\le g$ there. Split $\mathcal T_\alpha I\bar G P_{\mathcal J}$ at $k=(N+1)/2$. Below $k$ a difference at least $k$ is forced in the $\alpha$ coefficient, so the whole low output costs $g A_k$ with $A_k=\|P_{\ge k}\alpha\|_{A^0}$. Above $k$ use (ASQ17.3) after the full multiplication of cost $1.43g$. This proves the genuine total row bound
$$
 \|\Theta P_{\mathcal J}\|
 <45(4g)(\sum_{n\ge N}n^2e^{-2an})^{1/2}
       +1.11g A_k+45(1.43g)\Gamma_k .                     \tag{ASQ17.4}
$$
The middle term uses the actual $L^2$ norm of $C^{-1}$ and the contractive final selector. The analysis never commutes the middle left density inverse with an ordinary cutoff.

In the window $4097\le n\le 2^{20}$ use the actual $g=.573$ from [ASQ14](R149-supplement-original-WMA-head-on-the-true-signed-waist-inverse.md); for $n\ge2^{20}+1$ use $g=1.28$ from ASQ16. The WMA full derivative tail gives $A_k\le.023/\sqrt{8(k-1)}$: it is below $.000180$ for $k=2049$ and below $.0000113$ for $k=524289$. In the first window $\Gamma_{2049}<3\cdot10^{-12}$ and $(\sum_{n\ge4097}n^2e^{-2an})^{1/2}<10^{-18}$. For the latter one may sum the geometric tail explicitly as $e^{-2aN}[N^2/(1-z)+2Nz/(1-z)^2+z(1+z)/(1-z)^3]$, $z=e^{-2a}$. Both exponential bounds only decrease in the second window. Thus
$$
 \|\Theta P_{[4097,2^{20}]}\|<.000115,\qquad
 \|\Theta P_{[2^{20}+1,\infty)}\|<.0000162,\qquad
 \|\Theta P_{\ge4097}\|<.000117 .                          \tag{ASQ17.5}
$$
The last inequality is Cauchy–Schwarz on the two orthogonal input windows.

For true CFC or source data $z$, a computed approximation to all 96 coordinates of $\Theta P_{[1,4096]}z$ incurs at most $.000117\|P_{\ge4097}z\|$ for its omitted band. If $z$ is the recovered high response $H_c r$, the tail fee uses $P_{\ge4097}H_cr$ and the complete lower component of that same signed response. It cannot be applied to $P_{\ge4097}r$ before taking the inverse. The original finite $\Theta E_{96}$ inverse, the 96 physical independent columns, both means and the phase/height rows remain distinct.
