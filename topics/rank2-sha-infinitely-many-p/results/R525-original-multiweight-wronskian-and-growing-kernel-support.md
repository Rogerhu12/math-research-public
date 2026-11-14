# R525 — 原低轴的多权 Wronskian 零估计与临界支持下界

日期：2026-11-14。**状态：已证明。** 本篇接 R526 的同一个原
Theta 对数方程，给一般混权一个保系数帽的必要条件。
不只排除单权和两权：在真正二次临界量级中，任何非零原首核
的非零权数至少为常数乘 $N^{1/3}$；低第三块时至少为
$((17/147)^{1/6}-o(1))p^{1/6}$。

证明使用原有限低轴的 Wronskian，保完整原矩阵的一条必要投影。
它不把形式微分当作已证明的同预算来源操作，也不排除支持更多
权的真实核。主目标仍未完成。

## 1. 同一原低轴与一个全局代数解障碍

保
$$
p=6s-1>83,\qquad \Bbbk\text{ 为原完美剩余域},\qquad
\delta=t\partial_t,\qquad
\theta=\overline{\Theta}_{\rm reg},\quad\theta(0)=1.
$$
R526 支付了原整方程及其 Gaussian 余项；在原第一块，准确为
$$
x=\delta\theta/\theta,\qquad
6(1-t)\delta x-(1+2t)x=\frac23t\pmod{t^s}.
\tag{1}
$$
以下所有低轴评价只使用 (1) 到 $t^s$。不把 $x$ 当作某个
满足全局微分方程的代数函数。

先研究假想的全局方程
$$
6t(1-t)D X=(1+2t)X+\frac23t,\qquad D=\partial_t.
\tag{2}
$$
在 $\Bbbk(t)$ 中令
$$
H=t^s(1-t)^{3s-1}.
$$
由 $6s=1$ 在 $\Bbbk$ 中成立，直接有
$$
\frac{D H}{H}=\frac{1+2t}{6t(1-t)}.
$$
因此 (2) 的任何解都会满足
$$
D(X/H)=f(t),\qquad
f(t)=\frac1{9t^s(1-t)^{3s}}.
\tag{3}
$$
$f(t)dt$ 在 $0$ 的残数是
$$
c=\frac19\binom{4s-2}{s-1}\ne0,
\tag{4}
$$
因为 $0\le s-1\le4s-2<p$，相关阶乘全为单位。

事实上，(2) 在任意有限可分扩张 $L/\Bbbk(t)$ 中都无解。
$D$ 唯一延拓到 $L$；特征 $p$ 中 $D^p$ 是导子，在 $\Bbbk(t)$
上为零，有限可分性遂使其在 $L$ 上也为零。
如果 (3) 成立，则必须 $D^{p-1}f=0$。
但 $f$ 在 $0$ 的极阶只有 $1,\ldots,s<p$。
其 $c/t$ 项经 $p-1$ 次导数给 $-ct^{-p}$；
阶 $2,\ldots,s$ 的各极项的导数系数均含一个 $p$ 因子，
原正规部分不产生负次项。因此
$$
D^{p-1}f=-ct^{-p}+\text{在 }0\text{ 正规的项}\ne0.
\tag{5}
$$
这给矛盾。这里没有只凭有残数就排除野分歧拉回；
(5) 的可分导子论证已经保留了这一问题。

定义清分母的实际多项式导子
$$
\mathcal V
=6t(1-t)\partial_t+
 \left((1+2t)X+\frac23t\right)\partial_X.
\tag{6}
$$
由上述障碍，对任意不可约 $F\in \Bbbk[t,X]$、$\deg_XF>0$，
$$
\boxed{F\nmid\mathcal VF.}
\tag{7}
$$
证明如下。若 $F_X\ne0$，在 $\Bbbk(t)$ 上取其一个根形成有限可分
扩张；$F\mid\mathcal VF$ 与隐函数求导会给 (2)，与 (5) 矛盾。
若 $F_X=0$，整除关系给 $F\mid t(1-t)F_t$。
因 $\deg_XF>0$，$F$ 不整除 $t(1-t)$，故 $F\mid F_t$；
比较 $t$ 次数得 $F_t=0$。
完美性使同时 $F_X=F_t=0$ 的 $F$ 是一个 $p$ 次幂，
与不可约性矛盾。特别，(7) 不需要 $\deg_XF<p$。

## 2. 对数变量的完整有限零估计

**引理 1。** 设 $P(t,X)\in \Bbbk[t,X]$ 非零，
$$
\deg_tP\le A,\qquad \deg_XP=B\ge1.
$$
若 $1\le T\le s$ 且 $P(t,x(t))=0\bmod t^T$，则
$$
\boxed{T\le2AB+B.}
\tag{8}
$$

先证不可约且正 $X$ 次数的情形。由 (7)，
$$
R_P(t)=\operatorname{Res}_X(P,\mathcal VP)
$$
是非零多项式。由 (6)，
$$
\deg_t(\mathcal VP)\le A+1,\qquad
\deg_X(\mathcal VP)\le B,
$$
故
$$
\deg_tR_P\le2AB+B.
\tag{9}
$$
原低轴 (1) 给
$$
(\mathcal VP)(t,x(t))
\equiv6(1-t)\delta\{P(t,x(t))\}\pmod{t^s}.
\tag{10}
$$
$\delta$ 保 $t$ 阶，所以 $P$ 与 $\mathcal VP$ 的实际评价都
消失到 $T$。resultant 的多项式 Bézout 身份使 $R_P(t)$
也消失到 $T$；(9) 即给 (8)。

一般情形写
$$
P=c(t)\prod_iP_i^{r_i},\qquad
A_0=\deg c,\quad A_i=\deg_tP_i,\quad B_i=\deg_XP_i>0.
$$
若 $2AB+B\ge s$，结论对 $T\le s$ 已平凡。
否则每个 $2A_iB_i+B_i<s$；对每个因子用上面的截断证明，
其可见实际阶至多 $2A_iB_i+B_i$。
这一步不需要知道 $t^s$ 后的任何系数。
于是
$$
\begin{aligned}
\operatorname{ord}_tP(t,x(t))
&\le A_0+\sum_i r_i(2A_iB_i+B_i)\\
&\le A_0+2B(A-A_0)+B\\
&\le2AB+B.
\end{aligned}
$$
纯 $t$ 因子的阶已由 $A_0$ 完整计入。引理证毕。

(8) 适用于任意 $B\ge1$，包括 $B\ge p$；
非可分因子已经在 (7) 中处理。
它仍只是原低轴长度 $s$ 内的估计，不将 (1) 免费延长。

## 3. 原多权函数的 Wronskian

保 R486、R526 的同一来源
$$
a(t)=t(t-1)(7+4t+16t^2),\qquad
c_m=\lceil m/68\rceil,\qquad
e_m=\lfloor11m/34\rfloor-4c_m.
\tag{11}
$$
取 $k\ge2$ 个不同非空权
$$
0\le m_1<\cdots<m_k\le N<p
$$
及非零 $f_i(t)\in \Bbbk[t]_{\le e_{m_i}}$。
置
$$
A_i=a(t)^{c_{m_i}}f_i,\qquad
j_i=\operatorname{ord}_0f_i,\qquad
v_i=c_{m_i}+j_i,\qquad
B_i=t^{-v_i}A_i .
\tag{12}
$$
这里 $B_i$ 是原多项式，不是另一个来源选择；$B_i(0)\ne0$，
且准确有
$$
\deg B_i=3c_{m_i}+\deg f_i-j_i.
\tag{13}
$$
记
$$
g_i=t^{v_i}B_i\theta^{m_i},\qquad
F_{\rm ord}=\sum_{i=1}^k g_i,\qquad
q=\frac{k(k-1)}2,\quad
A=\sum_i\deg B_i,\quad v=\min_i v_i.
\tag{14}
$$

令 $D_0(t)=6(1-t)$，定义实际多项式递推
$$
P_{0,i}=B_i,
$$
$$
\boxed{
P_{j+1,i}
=\mathcal VP_{j,i}
+\{D_0(v_i+m_iX)+6jt\}P_{j,i}.
}
\tag{15}
$$
由 (1) 及乘积法则，
$$
t^{-v_i}\delta^jg_i
\equiv
\theta^{m_i}D_0^{-j}P_{j,i}(t,x(t))
\pmod{t^s}.
\tag{16}
$$
(16) 的截断长度仍为 $s$：微分中产生的原 ODE 误差总带
原列共有的 $t^{v_i}$，先除这个显示因子后才读取同一 $s$。
$\delta$ 不降低任何误差阶，$D_0(0)=6$ 为单位。
没有用全局精确的 $x$ 方程代替原 (1)。

逐次由 (15) 得
$$
\deg_XP_{j,i}\le j,\quad
\deg_tP_{j,i}\le\deg B_i+j,\quad
[X^j]P_{j,i}=D_0^jm_i^jB_i.
\tag{17}
$$
定义
$$
\mathscr W(t,X)=\det(P_{j,i})_{0\le j\le k-1,\ 1\le i\le k}.
$$
其最高 $X$ 系数准确为
$$
\boxed{
[X^q]\mathscr W
=D_0^q\left(\prod_iB_i\right)
       \prod_{i<l}(m_l-m_i)\ne0.
}
\tag{18}
$$
$N<p$ 保全部不同权差非零。包括 $m_1=0$ 的情形，
这里都是同一个 Vandermonde 身份。
所以
$$
\boxed{
\deg_X\mathscr W=q,\qquad
\deg_t\mathscr W\le A+q.
}
\tag{19}
$$
不存在一个凭有限 jet 猜测 Wronskian 非零的步骤。

由 (16)，完整归一 Wronskian 满足
$$
\det(t^{-v_i}\delta^jg_i)_{j,i}
\equiv
\theta^{\sum_i m_i}D_0^{-q}\mathscr W(t,x(t))
\pmod{t^s}.
\tag{20}
$$

**定理 2（保实际系数次数的多权接触界）。**
若 $1\le H\le s$ 且
$F_{\rm ord}=0\bmod t^H$，则
$$
\boxed{
H\le v+q(2A+2q+1).
}
\tag{21}
$$

若 $H\le v$，结论立即成立。否则选 $v_a=v$。
在 (20) 左边，把第 $a$ 列换成
$$
t^{-v}\delta^jF_{\rm ord}
=\sum_i t^{v_i-v}(t^{-v_i}\delta^jg_i).
$$
第 $a$ 列的系数为一；其余系数全在 $\Bbbk[t]$，
所以行列式不变。新列的每个条目均在 $t^{H-v}$ 中，
因为 $\delta$ 保原 $H$ 阶。其他列都正规。
于是 (20) 给
$$
\mathscr W(t,x(t))=0\bmod t^{H-v}.
$$
其中 $H-v\le s$，两个外因子均为单位。
对 (19) 用引理1，即得
$H-v\le2q(A+q)+q$，证明 (21)。

单权时不需要 Wronskian：$\theta$ 和 $B_1$ 都为单位，
所以其实际阶就是 $v_1$。
本篇没有为不同权分别提出一个相同的 Theta 因子。

## 4. 原完整 M 的支持数门

原完整矩阵仍为
$$
M=c_*U_0m_{13}J.
$$
保其全部 $P_{134}$、Gaussian、三块、两条进位和原十三自由行。
若经 R486 的固定 conductor 返回，令
$$
r_c=\operatorname{ord}_0q_{\mathfrak c};
$$
不用 conductor 时令 $r_c=0$。
只在已付原返回/整单位范围及固定坏素数排除下使用
$$
d_0=13+r_c,\qquad H=s-d_0>0.
\tag{22}
$$
R526 的完整必要第一块投影准确是
$$
\boxed{
\bar M P=0
\Longrightarrow
\sum_{m\le N}\theta^ma(t)^{c_m}f_m=0\bmod t^H.
}
\tag{23}
$$
因此可以把 (21) 应用于真正的原核；不能反向从 (23) 构造
完整三块的核。

设该核有 $k$ 个非零约化权。
沿用准确的累计上界
$$
E_N=\max_{m\le N,\ e_m\ge0}e_m,\qquad C_N=\lceil N/68\rceil.
$$
当 $N=68u+r$、$0\le r<68$ 时，
$$
E_N=18u+\max\{0,\lfloor11r/34\rfloor-4\}.
\tag{24}
$$
由 (12)–(13)，
$$
v\le C_N+E_N,\qquad A\le k(3C_N+E_N).
$$

**定理 3（真实累计来源的支持必要条件）。**
若 $N<p$ 且 $P\in\ker\bar M$ 非零，则：

- 若 $k=1$，必须 $H\le C_N+E_N$。
- 若 $k\ge2$，令 $q=k(k-1)/2$，必须
$$
\boxed{
H\le C_N+E_N+
q\{2k(3C_N+E_N)+2q+1\}.
}
\tag{25}
$$

此处 $k$ 是同一规范化直接和中的非零约化权数，
不是某个冗余单项式呈示的非零系数数。
一个 primitive 的模 $p^2$ 或模 $p^3$ 右核提升，
其非零约化也须满足完全相同的条件。
不把另一份未经证明饱和的来源呈示的 primitive 性移到这里。

在 (15)–(21) 中做微分只用于必要的零估计。
没有断言 $\delta^jP$ 属于原同预算来源，
没有使用未证明的 $P(\operatorname{im}J)$ 稳定性，
也没有将连接的系数增长免费放入算术预算。

## 5. 二次临界中的明确发散下界

考虑任何已经存在的真实临界候选序列，令 $N\to\infty$，
$$
\ell/s\to\tau,\qquad 0\le\tau\le1,
$$
且原来源维数与原目标处于 R526 的临界量级：
$$
\dim\mathcal B_{\le N}=\frac9{68}N^2+O(N),\qquad
s\sim\frac{9N^2}{68(2+\tau)}.
\tag{26}
$$
固定 conductor 的 $r_c$ 不随 $N,p$ 变化。
此时 $N<p$ 最终自动成立，且
$$
C_N+E_N=\frac{19}{68}N+O(1),\qquad
3C_N+E_N=\frac{21}{68}N+O(1).
\tag{27}
$$

由 (25) 必有
$$
\boxed{
\liminf\frac{k}{N^{1/3}}
\ge\left(\frac3{7(2+\tau)}\right)^{1/3}.
}
\tag{28}
$$
严格读法是对每个固定 $\varepsilon>0$，
最终 $k$ 大于右边常数减 $\varepsilon$ 再乘 $N^{1/3}$。

证明只需反设 $k\le(c-\varepsilon)N^{1/3}$，
其中 $c^3=3/[7(2+\tau)]$。将 (27) 代入 (25)，
其右边至多
$$
\frac{21}{68}k^3N+o(N^2),
$$
因为 $q=(k^2-k)/2$，其余项为
$O(k^4+k^3+N+k^2N)$，在该反设下都是 $o(N^2)$。
左边由 (22)、(26) 为
$9N^2/[68(2+\tau)]+o(N^2)$，常数严格矛盾。

使用 $p=6s-1$，也可写成
$$
\boxed{
k\ge
\left\{\left(\frac{34}{147(2+\tau)}\right)^{1/6}-o(1)\right\}p^{1/6}.
}
\tag{29}
$$
特别低第三块 $\ell/s\to0$ 时，
$$
\boxed{
k\ge\left\{(17/147)^{1/6}-o(1)\right\}p^{1/6}.
}
\tag{30}
$$
这排除了任意固定数目的权支撑临界核的可能，
并给真实增长阶；它不是只说“至少三条”。

## 6. 剩余范围与依赖

允许的原权数仍可为 $O(N)$，而 (28) 只迫 $N^{1/3}$ 量级。
所以本篇没有排除完整原核，也未给原首次/第二障碍或某条
中央导数赋非零。三层真实连接、同一首次修正、
Gaussian/两次 carry、第三精度仍须按原 $M$ 联立。

本篇也没有从 (26) 的维数近似制造候选；
(28)–(30) 只约束实际存在并满足该临界关系的候选序列。
若使用 conductor，完整固定权 $10980$、原点阶、系数范数
和所有返回门都保持。

- [R526：原 Theta 对数方程、两权估计及实际第一块投影](R526-original-theta-logarithmic-zero-bound-and-two-weight-kernel-exclusion.md)。
- [R486：同一规范化来源、全部68余类与真实原M](R486-graded-integral-connection-and-actual-homogeneous-third-kernels.md)。
- [R479：原M全部进位及同一修正](R479-original-carry-graph-and-two-normal-jets.md)。
- [R481：原第三精度与真实第二障碍](R481-full-third-precision-normal-form-and-common-correction.md)。

这里的残数、导子、resultant 和 Wronskian 均为全参数证明；
没有新增素数扫描，也没有引入未证明的高度或消失阶假设。
