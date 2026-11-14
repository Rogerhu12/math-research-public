# R176. 真实除幂源格与逐层共同前缀饱和

**状态：已证明。** 日期：2026-11-12。

完整证明：
[真实除幂源格、对数合流矩阵与逐层共同前缀](../notes/2026-11-12-actual-divided-source-lattices-and-prefix-saturation.md)。

固定惰性 $p\ge7$、$r=(p+1)/4$，在 R174 的同一实际平面上令
$E_D=\mathbb Z_p[a,b]_{\le D}$。定义真正保持多项式次数的源格链

$$
L_t=\sum_{s=0}^t p^{-s}b^{rs}E_{D-rs},\qquad
0\le t\le\lfloor D/r\rfloor.
$$

其基为 $p^{-\min(t,\lfloor j/r\rfloor)}a^ib^j$，
$i+j\le D$，指数准确为

$$
\log_p[L_t:E_D]=\sum_{s=1}^t\binom{D-rs+2}{2}.
$$

在 $k<pr$ 的真实共同余式矩阵中，所有 $L_t$ 均整；
因为 $b=V\cdot\mathrm{unit}$，且
$V^r=\pi_0U$、$\pi_0=p\kappa$，故 $b^r/p$ 的余式整。

置

$$
N_t=(t+1)(D+1)-rt(t+1)/2.
$$

若 $N_t\le p$ 且 $r(N_t-1)<k<pr$，则对完整实际前缀
$\operatorname{ord}_vP(\gamma_v)\ge k$ 有

$$
P\in L_t\quad\Longrightarrow\quad P/p\in L_{t+1}.
$$

末层无新的 $b$ 幂块时，该前缀核为零。
证明保留全部分块相消，利用实际纵轴
$F(a,0)=\kappa\eta(a-1)/\eta'(a-1)^r$；
到阶 $<p$ 它准确是 $\kappa a^r\log a$。
逐 $b$ 次数归纳后，共同合流 Vandermonde 的节点为
$0,\ldots,D-j$，各节点重数由允许的除幂层给出，
在所列范围内行列式确为单位。

若能连续执行 $t$ 次，则原真实饱和 jet 获得

$$
\|\varphi_{D,k}\|_p\le p^{\lfloor k/r\rfloor-t}.
$$

该结论严格限定在 $k<pr$、前 $p$ 个纵轴 Taylor 行的范围。
下一共同共振与更高对数 carry 尚未支付，故不能据此宣称
$p\ll\sqrt{k}$ 的累计预算已获控制，也未推出 R159 的严格门。

