# R491 — 原赋值格内的因子整提升与双 jet 仿射偏移消失

日期：2026-11-14。**状态：已证明。** 原单 $Y=\mathscr R$ 来源格在清去固定 $d$ 分母后，是有限个明确 Gauss 赋值半空间的交。每个模 $p$ 因子可同时保持这些赋值整提升，所以一个已经属于原格的分解 $t^rF^mQ$，可在**同一预算内**选到真正因子化的整来源基准。

当 $m\ge3$ 时，这付出 R489 尚保留的仿射基准：它在整个真实“值/法向导数”余核中的类恒零。因此 R489 两最高极的实际兼容式可以准确化为齐次式。这里消掉的是两个分支 jet 的来源偏移，不是原 $J(P^{\rm fact})/p$ 的首次强迫、$\xi$、原 $M$ 两条十三行 carry 或第三精度。

同一论证也适用于 R473 的三源规范化 $\mathcal B_{\le N}$；固定 conductor 返回仍须按显示基和全部新增 carry 支付。本篇不对有稀疏混合指数限制的其他来源自动作同样结论。

## 1. 允许的局部系数与固定角点

取 $\mathcal O=\mathbf Z_p$ 或其有限非分歧扩张，剩余域 $k$；本篇应用保 $p>83$。在必要的非分歧扩张内，固定角多项式
$$
t,\quad t-1,\quad h_7=16t^2+4t+7,\quad d=1+8t
\tag{1}
$$
全部按其模 $p$ 不可约因子作唯一 monic Hensel 分解。各因子彼此素，且判别式、结果式均为单位。

具体地，$\operatorname{disc}(h_7)=-432$，
$h_7(0)=7$、$h_7(1)=27$、
$h_7(-1/8)=27/4$；其他三个线性角点之间的差只含 $2,3$。所以这里只需排除 $2,3,7$，当前 $p>83$ 已全部覆盖。若 $h_7$ 在 $k$ 上不可约，其两根要求相同的系数整除阶，直接使用 monic $h_7$ 因子即可；若分裂，分别使用两个 Hensel 线性因子。系数域不必因此任意扩大。

以下的“提升”是原 $\mathcal O$ 来源格中的局部系数选择。并不声称得到与 $p$ 无关的有理因子或一个新的全局高度界。

## 2. 同时保持全部 Gauss 赋值的因子提升

令 $q_\nu(t)$ 为有限个上述互素 monic 因子，给每个因子指定正整数 $e_\nu$ 及整数 $w_\nu$。对非零多项式 $G(t,Y)=\sum_i g_i(t)Y^i$ 定义
$$
v_\nu(G)=\min_i\{e_\nu\operatorname{ord}_{q_\nu}(g_i)+w_\nu i\}.
\tag{2}
$$
另取无穷远的
$$
v_\infty(G)=\min_i\{-e_\infty\deg_t g_i+w_\infty i\},
\qquad e_\infty>0.
\tag{3}
$$
零系数在取最小时略去。这些都是 $K(t)[Y]$ 上的 Gauss 赋值；它们对非零乘积严格相加。理由是在对应赋值的分次剩余域上，最低初形式的乘积仍为非零多项式。这个理由同时适用于模 $p$ 域，不需要为最高或最低项另加无取消假设。

**引理 1。** 每个非零 $\bar G(t,Y)\in k[t,Y]$ 都有 $\widetilde G\in\mathcal O[t,Y]$，同时满足：

- $\widetilde G\bmod p=\bar G$；
- 每个非零 $Y^i$ 系数的 $t$ 次数与约化相同；
- 在所有固定 $q_\nu$ 上，每个系数的整除阶与约化相同；
- 因而所有 (2)、(3) 的值及 $\deg_Y$ 都准确相同。

**证明。** 对每个非零系数 $\bar g_i$，令
$$
\bar D_i=\prod_\nu\bar q_\nu^{\,\operatorname{ord}_{\bar q_\nu}(\bar g_i)},
\qquad \bar g_i=\bar D_i\bar u_i.
$$
在原域中，这个乘积按不可约因子取；不同 Hensel 因子仍互素。将 $\bar u_i$ 按相同次数任意逐系数整提升，并乘以
$D_i=\prod_\nu q_\nu^{\operatorname{ord}_{\bar q_\nu}(\bar g_i)}$。
这里有限角条件与无穷远帽确实相容：
$\deg\bar D_i=\sum_\nu\deg(\bar q_\nu)\operatorname{ord}_{\bar q_\nu}(\bar g_i)
\le\deg\bar g_i$，
因为这些互素因子的乘积已经整除给定的 $\bar g_i$。
所以余因子的准确次数 $\deg\bar g_i-\deg\bar D_i$ 非负；
Hensel 因子 monic 且不变次数，所选余因子首系数为单位，
乘积次数遂仍恰为 $\deg\bar g_i$。没有分别选择角条件和无穷远帽后另假设它们相容。
其首系数为单位，且约化余因子不被任何 $\bar q_\nu$ 整除，所以次数及全部整除阶都准确保持。零系数提升为零。逐个 $Y$ 系数组合即可。$\square$

由此得到一个非线性的来源结论。设一个有限自由多项式格准确给定为
$$
\mathcal V=\{P\in\mathcal O[t,Y]:
\deg_Y P\le D,\quad v_\nu(P)\ge c_\nu,\quad
v_\infty(P)\ge c_\infty\}.
\tag{4}
$$
若 $\bar P\in\overline{\mathcal V}$ 有分解
$$
\bar P=\bar G_1\cdots\bar G_a,
\tag{5}
$$
则分别用引理 1 提升每个因子。所得乘积
$P^{\rm fact}=\widetilde G_1\cdots\widetilde G_a$
有与 $\bar P$ 相同的各 Gauss 值及 $Y$ 次数，故
$$
\boxed{P^{\rm fact}\in\mathcal V,\qquad
P^{\rm fact}\bmod p=\bar P.}
\tag{6}
$$
对于指定重复因子，在 (5) 中只选一个提升后取其同一幂。固定因子 $t^r$ 保持为原 $t^r$。
这不是把不同模 $p$ 因子随意独立提升后忽略来源：引理保持的全部赋值正是保证乘积仍在 (4) 中的条件。

## 3. 原单 Y 格的准确赋值半空间

保 R472/R489 的
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
f_n=\lfloor9n/2\rfloor+4.
$$
将固定分母全部保留，记
$$
\mathcal V_D=d^{C_D}\mathcal W_D\subset\mathcal O[t,Y].
\tag{7}
$$
对 $P=\sum_{n=0}^D P_n(t)Y^n$，定义以下具体赋值。$a$ 在第一行遍历 $t=0$ 与 $h_7$ 的两个根；若后两点不分裂，使用同一个不可约 $h_7$ 的阶。
$$
\begin{array}{c|c|c}
\text{角点}&v(P)&\text{准确下界}\\ \hline
a=0,\ h_7(a)=0&
\min_n(4\operatorname{ord}_a P_n-n)&-2\\
1&\min_n(3\operatorname{ord}_1 P_n-n)&-1\\
-1/8&\min_n(2\operatorname{ord}_{-1/8}P_n+n)&2C_D\\
\infty&\min_n(-2\deg P_n+9n)&-2C_D-8 .
\end{array}
\tag{8}
$$

**定理 2。** $\mathcal V_D$ 准确等于 $\deg_Y P\le D$ 及 (8) 所定义的格，且这个识别在模 $p$ 后仍准确成立。

**证明。** 对每个 $n$，(8) 的有限点条件逐项等价于
$$
\begin{aligned}
\operatorname{ord}_{0,h_7}P_n
&\ge\left\lceil\frac{n-2}{4}\right\rceil=A_n,\\
\operatorname{ord}_{1}P_n
&\ge\left\lceil\frac{n-1}{3}\right\rceil=B_n,\\
\operatorname{ord}_{-1/8}P_n
&\ge\left\lceil\frac{2C_D-n}{2}\right\rceil=C_D-C_n.
\end{aligned}
\tag{9}
$$
这些右端对 $0\le n\le D$ 均非负。因固定因子两两互素，等价于
$(th_7)^{A_n}(t-1)^{B_n}d^{C_D-C_n}\mid P_n$。
无穷远条件恰为
$$
\deg P_n\le\left\lfloor\frac{9n+2C_D+8}{2}\right\rfloor
=f_n+C_D.
$$
除去前述固定因子的准确次数后，剩余次数就是原 $e_{n+1}$。这给 (7) 的两个方向，也同时证明显示来源基的约化没有额外饱和缺口。$\square$

因此，对任意真正的约化分解
$$
d^{C_D}\bar P=t^rF^mQ,\qquad
\bar P\in\overline{\mathcal W}_D,
\tag{10}
$$
可选择 $\widetilde F,\widetilde Q$，保持每个因子的全部有限角阶、斜次数和 $Y$ 次数，使
$$
\boxed{P^{\rm fact}
=d^{-C_D}t^r\widetilde F^{\,m}\widetilde Q
\in\mathcal W_D.}
\tag{11}
$$
原 $D$、每条 $q_n$、每个 $e_{n+1}$ 都未增加，$d^{-C_D}$ 仍完整保留。这里无须 $F$ 的导数为单位；后文接正规分支时才用该条件。

## 4. 双 jet 余核中的仿射偏移恒零

现在取 R489 的 $F(0,1)=0$、$F_Y(0,1)\ne0$，且 (10) 中 $m\ge3$。令 $Y=\psi(t)$ 为其同一正规分支，并记任意两长度的原映射
$$
\mathcal T_{V,N}(R)=
\bigl(R(t,\psi)\bmod t^V,\;(\mathcal ER)(t,\psi)\bmod t^N\bigr),
\qquad\mathcal E=Y\partial_Y.
\tag{12}
$$
$d(0)=1$，所以本节所有分母在这条分支局部均为单位。

取任意实际 $P^{\rm base}\in\mathcal W_D$ 提升 $\bar P$，以及任意保持约化的因子提升 $F_0,Q_0$，定义 R459 的仿射基修正
$$
R^{\rm base}=
\frac{P^{\rm base}-d^{-C_D}t^rF_0^mQ_0}{p}.
\tag{13}
$$
这个局部整表达未必自己属于 $\mathcal W_D$；不能在证明前设为零。

**定理 3。** 约化后的双 jet 满足
$$
\boxed{\mathcal T_{V,N}(\bar R^{\rm base})
\in\operatorname{im}\mathcal T_{V,N}
\bigl(\overline{\mathcal W}_D\bigr).}
\tag{14}
$$
事实上可按 (11) 选择 $P^{\rm base}=P^{\rm fact}$ 和同一因子提升，使 $R^{\rm base}=0$。式 (14) 保任意其他原提升选择。

**证明。** 取 (11) 的真正因子化基准。两实际基准相减除 $p$ 给
$$
W=\frac{P^{\rm base}-P^{\rm fact}}p\in\mathcal W_D,
$$
因为原来源显示基为有限自由且约化核恰为 $p\mathcal W_D$。
另外
$$
\frac{d^{-C_D}t^r
(\widetilde F^{\,m}\widetilde Q-F_0^mQ_0)}p
\bmod p
\in F^{m-1}k[t,Y,d^{-1}].
\tag{15}
$$
这是对两因子提升作一次准确展开；无需除以 $m$。当 $m\ge3$，右侧包含在 $F^2$ 理想中，故其值与 $\mathcal E$ 导数在 $F=0$ 上都零。由 (13) 得
$\mathcal T_{V,N}(\bar R^{\rm base})=\mathcal T_{V,N}(\bar W)$，即 (14)。$\square$

所以 R489 式 (29) 的右端对**每个原真左行**都准确为零，而不是另一个待定标量。只要该文两长度及 $K\ge-1$ 等真实范围成立，单位 $-2$ 和单位 $5$ 的联合兼容条件化为
$$
\boxed{
a_{-N'}-\frac25u_0(-1)^h b_{-V'}=0
\quad\text{对全部 }\Phi\in\mathscr D^{\rm actual}_{V,N}.}
\tag{16}
$$
这里仍保 R489 (18) 的全局正则、(24) 的其余原列测试，以及真实接触首项 $u_0$。
定理 3 证明了为何这次可以取齐次像；它没有证明 (16) 必成立或必不成立。

这一结论也说明：改变合法因子提升及实际来源基准不改变联合障碍类。不是先挑一个便利的 $\xi$ 再丢掉其他提升。

## 5. 三源规范化也有同预算的因子提升

R473 的实际规范化为
$$
\mathcal B_{\le N}=\bigoplus_{m=0}^N
\Theta^m a(t)^{c_m}\mathcal O[t]_{\le e_m},
\quad
a=t(t-1)h_7,\quad c_m=\lceil m/68\rceil,
$$
$$
e_m=\lfloor11m/34\rfloor-4c_m.
\tag{17}
$$
对 $P=\sum P_m(t)\Theta^m$，它准确等价于 $\deg_\Theta P\le N$ 以及
$$
\boxed{
\min_m(68\operatorname{ord}_{a_i}P_m-m)\ge0
\quad(a_i\text{ 遍历 }a\text{ 的四根}),\qquad
\min_m(11m-34\deg P_m)\ge0.}
\tag{18}
$$
前者恰给 $a^{c_m}\mid P_m$，后者恰给
$\deg P_m\le\lfloor11m/34\rfloor$。同一引理因此给：
$$
\boxed{\bar P\in\overline{\mathcal B}_{\le N},\
\bar P=t^rF^mQ
\ \Longrightarrow\
t^r\widetilde F^{\,m}\widetilde Q
\in\mathcal B_{\le N}}
\tag{19}
$$
可在原权帽内保持所给分解。这包括混合 $\Theta$ 权，不要求整式齐次。

若在 R473 的显示来源 $\mathfrak c\mathcal B_{\le N}$ 上工作，先对显示的 $\mathcal B$ 因子应用 (19)，再乘**同一个固定** conductor $\mathfrak c$。此时来源成本、$\mathfrak c$ 的真实物理零阶、Gaussian charge 和 R485/R486 的全部 carry 原样保留。
本篇不改变 $\mathfrak c$ 的系数，也不宣称对一个主要来自 $\bar{\mathfrak c}$ 的模 $p$ 新因子，能够免费使固定 $\mathfrak c$ 本身作同样分解。只有显示 $\mathcal B$ 部分的分解由 (19) 支付。

## 6. 非平凡固定证书

因子提升须保持角点条件；逐系数取最小非负代表并不足以做到这一点。一个不涉及原 theta 高接触的固定证书如下：
$$
p=101,\quad D=12,\quad
F=1-Y(1-t)^8,\quad
P=\frac{(th_7)^3(t-1)^3}{d^4}Y^9F^3.
\tag{20}
$$
对 charge $n=9+i$，$0\le i\le3$，其原 $q_n$ 余下系数为常数倍
$$
(th_7)^{3-A_n}(t-1)^{3+8i-B_n}d^{C_n-4}.
$$
所有指数非负，次数依次为 $3,12,16,25$，各自不超过原次数帽。因此 $P\in\mathcal W_{12}$；清分母用的仍是 $d^{C_{12}}=d^6$。

但若将 $-(1-t)^8$ 的系数分别替为模 $101$ 的最小非负整数，其在 $t=1$ 的值为 $505$，不为零。这样未保角赋值的乘积提升，在 charge $11,12$ 只有三个 $t-1$ 因子，少于原要求的四个，故不在 $\mathcal W_{12}$。引理 1 则保原八重角零，完整恢复 (20) 的同预算提升。

证书脚本 [check-r491-factor-lift-source.py](../scripts/check-r491-factor-lift-source.py)
核准确来源条件和这一次失败/修复，未把 (20) 当作原首核或中央零，也不扫描目标素数。

## 7. 未被消去的原障碍

选择 (11) 的因子化基准后，实际 $J(P^{\rm fact})/p$ 仍由同一 regularized 轴给出，R459 的 $\xi$ 和两条真实 carry 仍在；它们产生的单位 $5$、$-2$ 正是 (16) 的输入。
定理 3 没有证明 $P^{\rm fact}$ 已在 $K_2(J)$，更没有把整个 $J$ 的首次提升化为两条分支条件。

恢复原矩阵时仍保
$$
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H.
$$
$P_{134}/U_0$、十三自由行、两条十三行边界和 R481 的同一修正到第三精度的公式均未改变。
若原 $M$ 的 $B_0,B_1$ 非零，仍需将其同一来源输出代回 R479，不能从 (16) 的相对 $J$ 齐次式中将其删掉。

三条原完整中央失败不参与因子整提升定理，亦不因此传播为任意因子的中央零。下一实质条件准确缩为：在实际高 $b$ 候选和通过全部原列测试的真左行上，控制 (16) 的两个最高极系数。全局跨 $p$ 非零和 R418 的严格预算尚未获得。

