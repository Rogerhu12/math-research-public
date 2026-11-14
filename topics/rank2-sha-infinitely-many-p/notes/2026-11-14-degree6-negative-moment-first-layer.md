# 固定六度负矩的普通第一层、完整递推与有限证据

日期：2026-11-14。状态：下述模 $p$ 恒等式及递推已证明；表内结果仅为有限数值证据。本笔记不占新的主结果编号，也不预断固定负矩非零。

## 1. 原测度与准确第一层

取 R533 的原整来源
$$
f_4=x_\wp\sigma^6,\qquad f_1=-x_\wp y_\wp\sigma^6,
$$
以及同一普通周期 $\Omega_p$。其整性由
$f_4=Q_1\sigma^3$、$f_1=Q_1B_3$ 的原卷积给出。
本节只需 $p>7$、$p\equiv1\pmod6$、$p\nmid17$，
不需要 R529 的更细 whole-core 射线。

定义原单位域负矩
$$I_4=\int_{\mathbb Z_p^\times}z^{-2}\,d\nu_{f_4},\qquad
I_1=\int_{\mathbb Z_p^\times}z^{-5}\,d\nu_{f_1}.$$
由单位群 Fermat 同余和测度整性，
$$
\boxed{
\begin{aligned}
I_4&\equiv\Omega_p^{p-3}(p-3)![z^{p-3}]f_4(z)\pmod p,\\
I_1&\equiv\Omega_p^{p-6}(p-6)![z^{p-6}]f_1(z)\pmod p.
\end{aligned}}
\tag{1}
$$
证明中的两步是：先把单位域负幂换为 $p-3,p-6$ 次正幂，
再把单位域补为全域。补上的 $p\mathbb Z_p$ 积分由于正幂大于零
属于 $p\mathcal O$；这一步不需要预设核心为某个 scalar。
最后用原矩归一 $\int z^j\,d\nu_F=\Omega_p^jF^{(j)}(0)$。
这里两个阶乘都不含 $p$，周期也是单位。

置 $p=6s+1$、$r=s-1$，以下级数不依赖 $p$：
$$
u=bz^6,\quad b=17,\qquad
A(u)=z^2x_\wp(z)=1+\sum_{n\ge1}a_nu^n,
$$
$$
B(u)=A(u)-3uA'(u),\qquad
S(u)=\left(\frac{\sigma(z)}z\right)^6.
\tag{2}
$$
于是 $-y_\wp=z^{-3}B$ 且
$$
f_4=z^4 A(u)S(u),\qquad f_1=zA(u)B(u)S(u).
$$
写
$$c_{4,p}=[u^r]AS,\qquad c_{1,p}=[u^r]ABS\quad\text{于 }\mathbb F_p,$$
(1) 准确成为
$$
\boxed{\begin{aligned}
I_4&\equiv \Omega_p^{p-3}(p-3)!\,17^r c_{4,p}\pmod p,\\
I_1&\equiv \Omega_p^{p-6}(p-6)!\,17^r c_{1,p}\pmod p.
\end{aligned}}
\tag{3}
$$
因此 $I_4$ 是单位当且仅当 $c_{4,p}\ne0$，
$I_1$ 是单位当且仅当 $c_{1,p}\ne0$。
系数为零只表示负矩被 $p$ 整除，**不表示它作为 $p$ 进数为零**。

## 2. 无 $p$ 分母的完整计算

原微分方程 $x_\wp''=6x_\wp^2$ 及曲线
$y_\wp^2=x_\wp^3+b$ 给
$$
a_0=1,\qquad a_1=-\frac17,\qquad
\boxed{a_n=\frac{\sum_{j=1}^{n-1}a_ja_{n-j}}
{(6n+1)(n-1)}}\quad(n\ge2).
\tag{4}
$$
的确，$z^{6n-4}$ 系数左边减去右边两端项的因子为
$(6n-2)(6n-3)-12=6(6n+1)(n-1)$。
$n=1$ 的自由系数由原曲线常数 $b$ 确定为 $-1/7$。

令 $E=\log S=\sum e_nu^n$、$S=\sum s_nu^n$。
由 $(\log\sigma)''=-x_\wp$，
$$
\boxed{e_n=-\frac{a_n}{n(6n-1)},\qquad
s_0=1,\qquad s_n=\frac1n\sum_{j=1}^n j e_j s_{n-j}.}
\tag{5}
$$
且
$$
B(u)=1+\sum_{n\ge1}(1-3n)a_nu^n.
\tag{6}
$$
(4)–(6) 再作两次有限卷积，完整决定 (3) 的两个系数，
不截掉任何低尾或用浮点拟合。

在所需范围 $1\le n\le s-1$，全部分母中的 $n,n-1,6n-1,6n+1$
都小于 $p$ 且不被 $p$ 整除。$7$ 也为单位。首个
$6n+1=p$ 的共振在 $n=s$，位于本次所需范围之外。
所以整个算法可直接在 $\mathbb F_p$ 中运行，无须任选提升或除以 $p$。

这只说明第一层准确可计算；没有证明两个指定对角不能同时为零。

## 3. 已执行的有限范围

随附脚本已在当前 JavaScript 环境执行其同一计算核心。
范围为 $13\le p<2000$、$p\equiv1\pmod6$ 的全部 $147$ 个素数。
结果为：

- $c_{4,p}$ 在这 $147$ 个素数上均非零。
- $c_{1,p}=0$ 恰出现于 $p=61$；那里 $c_{4,61}=47$。
- 此范围内没有两个第一层同时为零。

例如：
| $p$ | $r$ | $c_{4,p}$ | $c_{1,p}$ |
|---:|---:|---:|---:|
| 13 | 1 | 1 | 5 |
| 19 | 2 | 4 | 17 |
| 31 | 4 | 18 | 18 |
| 61 | 9 | 47 | 0 |
| 199 | 32 | 74 | 137 |
| 967 | 160 | 308 | 347 |
| 1543 | 256 | 836 | 386 |

范围中的后三个只是满足 $p\equiv7\pmod{64}$ 的子集；
**未声称它们满足当前全部 CM ray 条件**。
本次有限计算覆盖更宽的普通素数集合，不是本题无穷射线的证书。

## 4. 尚未支付的步骤

R533 的双单位域等价保持原负矩，所以可以使用 (3) 的第一层证书。
但还须证明指定对角无穷次非零，或从完整有限 Schwartz/Hecke 数据
取得实际局部比较。单重 $\mu_6$ 型、whole 核、没有见到小素数零，
都不能替代该步骤；即使固定负矩已非零，还须把相应双单位域合法
接回原 $S/T$ 的完整中央及补域。

来源：
- [R533：完整两变量核及固定负矩接口](../results/R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)。
- [R316：原 sigma/Theta 整性及周期规范](../results/R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [生成脚本](../scripts/probe-original-degree6-negative-moment-first-layer.mjs)。
- [全部147个精确有限域结果](../scripts/probe-original-degree6-negative-moment-first-layer.json)。
