# 两个原有限头逆芽的次阶放大与同源大窗口兼容

Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro；2026-11-15。

本稿给一个严格更大的实际逆芽圆盘，同时保留原非线性小量 $e^{-d^3/4}$。它改善次阶 $d^2$ 预算，不把主三次系数 12.5 降成较小常数，也不证明尚未支付的原两费比较。

依赖原[十二点五半径及真实列权](../notes/2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)、[真实带权窗口](R271-appendix-true-minimal-projection-weighted-window.md)、[强尾同源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)和[首段损耗与圆盘演算](R271-appendix-first-row-observability-loss-exact-source-contraction-and-disk-calculus.md)。

## 1. 新半径

仍取 $m\ge10$、$d=2^m$、$q=d/2$、$d_0=e^{-20}$，原系数 $\Lambda_i,d_i,b_i$ 不改。定义

$$
\tau_m^\sharp=
\frac{\Lambda_{m-1}+d^3/4+\log16}{q-1},
\qquad
\rho_m^\sharp=e^{-\tau_m^\sharp},
\qquad
r_m^\sharp=\frac{\rho_m^\sharp}{2d_0},
\qquad
\varepsilon_m=e^{-d^3/4}.
\tag{1.1}
$$

有

$$
12d^3\le\tau_m^\sharp
\le\frac{25}{2}d^3-\frac12d^2.
\tag{1.2}
$$

下界由 $\Lambda_{m-1}\ge6d^4$ 和 $q-1<d/2$ 得到。上界只需展开

$$
\begin{aligned}
&(q-1)\left(\frac{25}{2}d^3-\frac12d^2\right)
-\Lambda_{m-1}-\frac14d^3-\log16\\
&=\frac18d^3+\frac12d^2-(75m-125/2)d-\log16>0.
\end{aligned}
$$

最后一步使用 $75m\le d^2/16$；它在 $m=10$ 成立，随后右侧每步乘 4 而左侧线性增加。

准确除法还给

$$
\tau_m^\sharp
=\frac{25}{2}d^3-\frac34d^2-\frac32d
+150m-128+\frac{300m-256+2\log16}{d-2}.
\tag{1.3}
$$

特别 $\rho_m^\sharp$ 至少是旧 $\rho_m=e^{-(25/2)d^3}$ 的 $e^{d^2/2}$ 倍。

## 2. 两个原函数的完整圆盘估计

本节同时适用于

$$
F_{N,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i},
\qquad
F_{Y,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i+z^{2^i}}.
$$

最高位由新半径的定义准确给

$$
\frac{(\rho_m^\sharp)^{q-1}}{d_{m-1}}
=\frac{\varepsilon_m}{16}.
\tag{2.1}
$$

对 $1\le i\le m-2$，令 $q_i=2^i$。由
$\Lambda_i\le(25/16)d^3q_i$ 和 (1.2)，

$$
\Lambda_i-\tau_m^\sharp(q_i-1)
\le \left(12-\frac{167}{16}q_i\right)d^3
\le-\frac{71}{8}d^3.
\tag{2.2}
$$

因此所有 $\left|z^{q_i}/d_i\right|$ 在 $|z|\le\rho_m^\sharp$ 上均小于 $1/2$；最低位也有 $|z|/d_0<1/2$。$Y$ 模型的全部分母在闭圆盘及其一个邻域内非零。

$N$ 模型的最低项准确为 $z/d_0$。$Y$ 模型最低项除以 $z$ 后是 $(d_0+z)^{-1}$，其与 $d_0^{-1}$ 的差至多 $2\rho_m^\sharp/d_0^2$。非线性分母至多损因子 2，故两模型统一有

$$
\begin{aligned}
\left|\frac{F_m(z)}z-d_0^{-1}\right|
&\le
\frac{\varepsilon_m}{8}
+2d\,e^{-71d^3/8}
+2e^{40-12d^3}\\
&\le\varepsilon_m,\qquad |z|\le\rho_m^\sharp.
\end{aligned}
\tag{2.3}
$$

最后两项分别除以 $\varepsilon_m$ 后为
$2d e^{-69d^3/8}$ 和 $2e^{40-47d^3/4}$，在 $d\ge1024$ 时各小于 $1/4$。

对 $|w|\le r_m^\sharp$，在 $|z|=\rho_m^\sharp$ 上，

$$
|F_m(z)-z/d_0-w|
\le\rho_m^\sharp\varepsilon_m+\frac{\rho_m^\sharp}{2d_0}
<\frac{\rho_m^\sharp}{d_0}.
$$

Rouché 定理给圆盘中唯一单零，随 $w$ 解析变化并延拓原零点逆芽。闭圆盘上的严格余量给一个解析邻域。于是同一个真实逆芽 $\psi_m$ 满足

$$
|\psi_m(w)|\le\rho_m^\sharp,\qquad
|\psi_m(w)-d_0w|
\le2d_0^2\varepsilon_m|w|.
\tag{2.4}
$$

## 3. 系数及真实输入列权仍保留

对全部整数 $k,n\ge0$，Cauchy 公式给

$$
|[w^k]\psi_m(w)^n|
\le(2d_0)^k(\rho_m^\sharp)^{n-k}.
\tag{3.1}
$$

$k<n$ 时系数为零，$n=0$ 时只留常项。对 $1\le n<d$、$k>n$，原小量证明原样给

$$
|[w^k]\psi_m(w)^n|
\le4n d_0^{n+1}\varepsilon_m
(r_m^\sharp)^{n-k}.
\tag{3.2}
$$

真实物理输入列权仍为 $W_n=\prod_{i\in\operatorname{bits}(n)}d_i$。对每个 $i<m$，

$$
\Lambda_i\le\tau_m^\sharp 2^i.
$$

最高位由 (1.1) 直接得到，其余位由 (2.2) 的更强界得到。因此

$$
\log\!\left(W_n^{-1}(\rho_m^\sharp)^{n-k}\right)
=\tau_m^\sharp k+
\sum_{i\in\operatorname{bits}(n)}
(\Lambda_i-\tau_m^\sharp2^i)
\le\tau_m^\sharp k.
\tag{3.3}
$$

所以完整真实链基逆仍可取 $\|K_m^{-1}\|\le d e^{\tau_m^\sharp(d-1)}$。这依然有 $d^4$ 主指数，不能改称只付 $\rho^{-1}$ 的来源 Schur 比较。

## 4. 扩头真源上的完整 $h-1$ 阶演算

令 $C=A_m+D_<$ 为真实扩头，$C^h=0$，$h=d+R$；远尾范数记为 $\delta$。已付首段损耗说明，实际源算子 $C_s$ 在同源两个度量

$$
S_b=L+B,\qquad S_f=L+G^{-1}
$$

中均为 $\delta$ 收缩，并有真实有限模型的圆盘演算。

定义解析函数

$$
H_m(w)=\frac{\psi_m(w)}{d_0w},\qquad H_m(0)=1.
$$

由 (2.4) 及 $H_m-1$ 在零点消失，Schwarz 引理给

$$
|H_m(w)-1|
\le4d_0^2\varepsilon_m\,\frac{|w|}{\rho_m^\sharp},
\qquad |w|\le r_m^\sharp.
$$

当 $\delta\le r_m^\sharp$ 时，真正作用于扩头源的算子必须用全部 $h-1$ 阶：

$$
H_m(C_s)=\sum_{j=0}^{h-1}[w^j]H_m(w)\,C_s^j.
$$

在两种实际度量中都有

$$
\boxed{
\|H_m(C_s)-I\|_{S_b},\
\|H_m(C_s)-I\|_{S_f}
\le4d_0^2\varepsilon_m\,\delta/\rho_m^\sharp.
}
\tag{4.1}
$$

这里没有用旧 $d-1$ 截断代替扩头展开，也没有认同 $\psi_m(C_s)$ 与旧 $B_m$。

## 5. 原同窗与新预算量级

原同一 $w$、真实 $u_Q$、母提升和带权投影定理均未改动。实际头函数、逆芽及仅依赖 $m$ 的原 gauge 多项式没有更换；新强头使用同一 $\psi_m$ 按新的实际高度 $h$ 取到 $h-1$ 阶，不能沿用旧强头高度的截断。旧证明在较小圆盘上的所有界继续成立，因此无需重做原物理窗口。

具体取

$$
R=\left\lceil 4/\rho_m^\sharp\right\rceil,
\qquad h=d+R,
\qquad
Q_*=\left\lfloor
\exp\!\left(\frac{1601}{64}d^3\right)
\right\rfloor.
$$

则原远尾满足 $\delta\le1/(m+R)\le\rho_m^\sharp/4$，所以 (4.1) 可用。并且

$$
h\le6/\rho_m^\sharp,
\qquad
\frac{Q_*}{h}
\ge\frac{1}{12}
\exp\!\left(\frac{1601}{64}d^3-\tau_m^\sharp\right).
\tag{5.1}
$$

由 $h+R\le11/\rho_m^\sharp$ 及 (1.2)，在全部 $m\ge10$ 时有 $h+R<Q_*/4$。因此 $n+h+R<Q_*$ 的真实来源区间仍有同量级长度，没有把并头的额外 $R$ 支撑删去。并且 $2h+R\le2(h+R)<Q_*/2$，所以[强 gauge 原未来链](R271-appendix-strong-gauge-true-left-feedback-driven-return-and-ordinary-endpoint.md)所需的更强条件 $n+2h+R<Q_*$ 也保留同量级区间。

由 (1.2)，(5.1) 至少给

$$
\frac{Q_*}{h}
\ge\frac{1}{12}
\exp\!\left(\frac{801}{64}d^3+\frac12d^2\right).
\tag{5.2}
$$

准确增益可用 (1.3)。这只是把尚需证明的同源比较常数 $\kappa$ 的可容纳量级提高一个次阶因子；$\mu^2\le\kappa\Xi^2$ 本身仍未得到证明。原两费、全部 nuisance 与高返回要求保持不变。
