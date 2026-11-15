# R334 — 原角域余量的八次多项式与真实 Hermite 缺陷传递

作者：ChatGPT /root（AI协作）；2026-11-15。

**已证明：准确有限维代数及条件包围定理；没有新数值结果。** 本文延续 [R262](R262-Hermite-RMS-domain-gradient-and-projected-descent.md)、[R265](R265-full-angle-linear-inequality-damped-model.md) 的原 Frenet 域条件。[R333](R333-actual141-eight-complete-thirty-five-pairs-and-exterior-domain-failures.md) 已记录所选查询的一阶 slack 非负而真实 trial 仍失域；后两批另有未选 MID489/490。新增37查询只补后者，不能由此消去前者的非线性余项。

下面给出同一域条件的无分母表示，以及在准确仿射查询上完整保留至八次的步长多项式。真实 RMS/中点查询包含重新计算的端点 RHS，一般不是仿射查询；第5—6节明确保留这一缺陷。本文不修改原 BVP 方程、merit、全部域检查、17档回溯或接受门，也没有为155增加先行认证关卡。

## 1. 准确对象与等价的无分母余量

固定原网格、一个原查询位置及一个 physical angle。令 $d,e\in\mathbb R^3$ 为原几何的完整一、二阶角导数，$a,\nu\in\mathbb R$ 为该位置实际声明的 scalar 字段。这里 $\nu$ 是源称作 ap 的字段，不假定独立有限积分实现满足 $\nu=\partial_s a$。

定义

$$
Q=d\cdot d,\qquad v=d\times e,\qquad W=v\cdot v,
\qquad P=a^2W-\nu^2Q^3.
\tag{334.1}
$$

在原正则域内，R262给出

$$
b:=\beta_{\rm Frenet}^2=1-\frac{\nu^2Q^3}{a^2W}.
\tag{334.2}
$$

**命题334-A。** 对任意有限准确实 $a,\nu,d,e$，有点态等价

$$
\boxed{a>0,\ Q>0,\ W>0,\ b>0
\quad\Longleftrightarrow\quad a>0,\ P>0.}
\tag{334.3}
$$

左边的 $b$ 只在非零分母时定义；右边是处处定义的多项式条件。

**证明。** 左边乘正分母 $a^2W$ 得 $P=a^2Wb>0$。反向，$P>0$ 蕴含 $a^2W>\nu^2Q^3\ge0$，所以 $W>0$。若 $Q=0$，则 $d=0$，必有 $W=|d\times e|^2=0$，矛盾。因此 $Q>0$，分母正且 $b=P/(a^2W)>0$。证毕。

因此不必在准确条件中除以接近零的 $W$ 或 $\nu$。特别地 $\nu=0$ 时仍合法，条件是 $a>0,W>0$。单有 $P>0$ 不规定 $a$ 的符号，不能省略 $a>0$。

命题只支付该查询的这一个域条件；原 scalar、core density、所有节点/中点/两组RMS及其它分支条件仍独立保留。普通浮点的原法向量表达式与交叉积表达式也不逐运算同值：原 computations/geometry_20261114_full_angle_domain_direction_probe.py 的 angular_values 已分别保留 beta 与 cross_beta，本文不将后者替换原 trial 的前者。

## 2. 仿射查询的完整八次步长多项式

现在明确假设四个输入沿一个准确实参数 $\alpha$ 仿射变化：

$$
a=a_0+\alpha a_1,\quad \nu=\nu_0+\alpha\nu_1,\quad
d=d_0+\alpha d_1,\quad e=e_0+\alpha e_1.
\tag{334.4}
$$

固定物理角的完整 Fourier 角导数是物理系数的线性映射。因此，准确仿射物理节点与仿射 scalar 参数在相应 scalar 字段也仿射时满足此假设。入口须使用原完整 core 注入，不能把其余节点或全局参数链删除。

令

$$
q_0=|d_0|^2,\quad q_1=2d_0\cdot d_1,\quad q_2=|d_1|^2,
\tag{334.5}
$$

$$
v_0=d_0\times e_0,\quad
v_1=d_0\times e_1+d_1\times e_0,\quad
v_2=d_1\times e_1.
\tag{334.6}
$$

于是

$$
Q(\alpha)=\sum_{i=0}^2q_i\alpha^i,\qquad
W(\alpha)=\sum_{j=0}^4w_j\alpha^j,
\quad w_j=\sum_{\substack{0\le i,k\le2\\i+k=j}}v_i\cdot v_k.
\tag{334.7}
$$

记 $A_i,N_i$ 分别为 $(a_0+\alpha a_1)^2$ 与 $(\nu_0+\alpha\nu_1)^2$ 的三项系数，超出索引范围的系数为零。则

$$
\boxed{P(\alpha)=\sum_{r=0}^8c_r\alpha^r,\qquad
c_r=\sum_{i+j=r}A_iw_j-
\sum_{i+j+k+\ell=r}N_iq_jq_kq_\ell.}
\tag{334.8}
$$

**证明。** 叉积双线性给出式(334.6)的三个系数；平方内积产生式(334.7)的完整有序卷积，交叉项出现两次。$a^2W$ 次数至多6，$\nu^2Q^3$ 次数至多8；乘法卷积恰给出式(334.8)。没有丢弃二次以上项，也没有只取最坏角的一条导数。证毕。

当这些输入是明确提升的有限二进制字面实数时，全部系数为有理数，可由整数/有理运算准确生成。若输入是严格区间，使用包含全部联合选择的外向区间算术仍给有效包围，但不把盒中各端点的任意组合都称为同一实际模型。

该式沿所声明的仿射查询准确，不自动描述原中点或RMS trial。也不能把在每个角独立记录的字面三角表视为已经定义了连续角上的准确三角函数。

## 3. 与原完整一阶域行的关系

在基点正则域内 $P=a^2Wb$，故

$$
P'(0)=a_0^2W_0\,b'(0)+(a^2W)'(0)b_0,
\tag{334.9}
$$

$$
b'(0)=\frac{P'(0)-b_0(a^2W)'(0)}{a_0^2W_0}.
\tag{334.10}
$$

这里 $b'(0)$ 正是对这条完整查询方向应用R262局部导数所得的值；若查询是实际Hermite查询的一阶展开，还须包含其全部端点RHS链和直接scalar链。式(334.10)由乘积求导直接得到，亦与R262的无 $\nu$ 除法公式相符。

因此，原 $b_0+\alpha b'(0)$ 的非负性只是一阶信息。既不能把 $P$ 的线性项与它混同，也不能由全部线性slack合法推出式(334.8)在同一步长为正。本文保留R333的两种独立事实：所选查询上的真实非线性失败，与所选集合之外的真实失败。

## 4. 完整闭步长区间的有限包围

设 $P$ 是式(334.8)的准确多项式，次数不足8时补零。对任一闭区间 $[u,u+h]$，$h>0$，写

$$
P(u+ht)=\sum_{k=0}^8d_kt^k,
\qquad d_k=h^k\sum_{r=k}^8c_r\binom rk u^{r-k}.
\tag{334.11}
$$

其八次Bernstein系数为

$$
B_j=\sum_{k=0}^j d_k\frac{\binom jk}{\binom8k},
\qquad 0\le j\le8,
\tag{334.12}
$$

满足准确恒等式

$$
P(u+ht)=\sum_{j=0}^8B_j\binom8j t^j(1-t)^{8-j}.
\tag{334.13}
$$

**证明。** 式(334.11)是二项展开。对每个 $k$，由二项式定理有
$t^k=\sum_{j=k}^8\binom jk/\binom8k\,\binom8j t^j(1-t)^{8-j}$；代入幂基表达即得(334.12)—(334.13)。权重非负且和为1，所以

$$
\min_jB_j\le P(\alpha)\le\max_jB_j
\quad(u\le\alpha\le u+h).
\tag{334.14}
$$

若该闭区间上 $a>0$ 且全部 $B_j>0$，由命题334-A得到整个闭步长区间的该查询域条件。对仿射 $a$，检查两个准确端点的最小值即可。若 $\max_jB_j\le0$，该整个闭区间不满足原严格域；有界包围跨零则只是未决。

对任意有限个已声明查询/角行，基点各自满足 $a_0>0,P(0)>0$ 时，存在共同 $A>0$，使各行在 $[0,A]$ 上由上述Bernstein正系数判据证明合法。**证明：** 在区间 $[0,A]$，式(334.12)各系数为 $P(0)+\sum_{k\ge1}c_kA^k\binom jk/\binom8k$，故当 $A\downarrow0$ 时全部趋于该行正的 $P(0)$；$a$ 两端亦趋于 $a_0>0$。有限行取最小邻域即得。以任意固定正有理 $A_0$ 反复减半，在准确无资源限制的运算中最终可取得这种共同区间。

这不保证原17档回溯已经达到该尺度，也不证明真实merit下降、连续角覆盖、其它原域条件或本次数值轨迹成功。实际实现若有工作上限，必须保留全部未决区间/行，不能由预算结束宣称反证。用于建议步长时只改变优化策略，原 trial 仍按原表达式求值与接受。

## 5. 真正Hermite查询的非线性缺陷

沿原完整准确坐标直线，令

$$
Y_i(\alpha)=Y_i+\alpha\dot Y_i,\quad
p(\alpha)=p+\alpha\dot p,\quad
f_i(\alpha)=f(s_i,Y_i(\alpha),p(\alpha)).
$$

假设这些实际原RHS在所讨论区间内有定义，且所用基点导数存在。固定原Hermite权重的实际查询是

$$
Y_t(\alpha)=h_{00}Y_i(\alpha)+h_{01}Y_{i+1}(\alpha)
+h h_{10}f_i(\alpha)+h h_{11}f_{i+1}(\alpha).
\tag{334.15}
$$

记 $\dot f_i=J_i\dot Y_i+P_i\dot p$，以及

$$
E_i(\alpha)=f_i(\alpha)-f_i(0)-\alpha\dot f_i,
\qquad \bar Y_t(\alpha)=Y_t(0)+\alpha\dot Y_t(0).
$$

则准确地

$$
\boxed{Y_t(\alpha)-\bar Y_t(\alpha)
=h\,[h_{10}E_i(\alpha)+h_{11}E_{i+1}(\alpha)].}
\tag{334.16}
$$

**证明。** 将两个端点的 $f_i(0)+\alpha\dot f_i+E_i$ 代入式(334.15)。常值和一阶项正是R262完整链给出的 $Y_t(0),\dot Y_t(0)$；余项即式(334.16)。核心自由度若通过入口注入或显式RHS列进入，必须一并放入同一 $\dot f_i$，不能以局部无显式core代替全部耦合。

在原中点 $t=1/2$，该式化为

$$
Y_{1/2}(\alpha)-\bar Y_{1/2}(\alpha)
=\frac h8[E_i(\alpha)-E_{i+1}(\alpha)].
\tag{334.17}
$$

一般两组RMS则保其真实 $h_{10},h_{11}$，不能套中点权重。只用完整一阶Hermite展开相当于忽略这些 $E_i$；若冻结基点RHS或只插值节点方向，还会漏掉本应保留的一阶RHS链。两种处理都不能冒真实查询。

若已独立证明沿完整线段 $f_i$ 为二次连续可微且 $\|f_i''(\alpha)\|\le M_i$，则对 $\alpha\ge0$，Taylor积分余项给

$$
\|E_i(\alpha)\|\le\tfrac12\alpha^2 M_i,
\quad
\|Y_t-\bar Y_t\|\le
\tfrac12h\alpha^2(|h_{10}|M_i+|h_{11}|M_{i+1}).
\tag{334.18}
$$

这里的 $f_i''$ 是完整方向 $(\dot Y_i,\dot p)$ 上的二阶变分。RHS的实分支存在、整段合法性及 $M_i$ 都是实质前提；没有这些包围，式(334.18)不是本题已有数值界，不能循环假定待证的域合法性来支付前提。

## 6. 从仿射八次式传递到有缺陷的真实查询

下面不要求误差为二阶；任何已证明的实际包围均可使用。在一个闭步长区间上，设准确仿射参考为 $\bar a,\bar\nu,\bar d,\bar e$，并有统一界

$$
|a-\bar a|\le\epsilon_a,\quad |\nu-\bar\nu|\le\epsilon_\nu,
\quad\|d-\bar d\|\le\epsilon_d,\quad\|e-\bar e\|\le\epsilon_e,
\tag{334.19}
$$

以及非负上界 $A\ge|\bar a|,N\ge|\bar\nu|,D\ge\|\bar d\|,
E\ge\|\bar e\|,V\ge\|\bar d\times\bar e\|$。这些均须覆盖整个当前区间。定义

$$
\begin{aligned}
\epsilon_Q&=2D\epsilon_d+\epsilon_d^2,\\
\epsilon_v&=D\epsilon_e+E\epsilon_d+\epsilon_d\epsilon_e,\\
\epsilon_W&=2V\epsilon_v+\epsilon_v^2,\\
\epsilon_{a^2}&=2A\epsilon_a+\epsilon_a^2,\qquad
\epsilon_{\nu^2}=2N\epsilon_\nu+\epsilon_\nu^2,\\
\epsilon_{Q^3}&=3D^4\epsilon_Q+3D^2\epsilon_Q^2+\epsilon_Q^3,\\
\epsilon_P&=\epsilon_{a^2}V^2+(A^2+\epsilon_{a^2})\epsilon_W
+\epsilon_{\nu^2}D^6+(N^2+\epsilon_{\nu^2})\epsilon_{Q^3}.
\end{aligned}
\tag{334.20}
$$

**命题334-B。** 整个区间上都有 $|P-\bar P|\le\epsilon_P$。若进一步有严格下界

$$
\inf\bar a>\epsilon_a,\qquad
\inf\bar P>\epsilon_P,
\tag{334.21}
$$

则真实查询在整个区间满足式(334.3)。其中 $\inf\bar P$ 可用第4节的完整多项式下界支付。

**证明。** 平方范数差给 $|Q-\bar Q|\le\epsilon_Q$。叉积展开
$d\times e-\bar d\times\bar e=\bar d\times(e-\bar e)+(d-\bar d)\times\bar e+(d-\bar d)\times(e-\bar e)$，由叉积范数界得 $\epsilon_v$，再次用平方范数差得 $\epsilon_W$。标量平方差分别给 $\epsilon_{a^2},\epsilon_{\nu^2}$。因为 $0\le\bar Q\le D^2$，展开 $(\bar Q+(Q-\bar Q))^3-\bar Q^3$ 后取绝对值给 $\epsilon_{Q^3}$。

最后将两个乘积分别拆成

$$
a^2W-\bar a^2\bar W=(a^2-\bar a^2)\bar W+a^2(W-\bar W),
$$

$$
\nu^2Q^3-\bar\nu^2\bar Q^3=(\nu^2-\bar\nu^2)\bar Q^3+
\nu^2(Q^3-\bar Q^3).
$$

用 $\bar W\le V^2,\bar Q^3\le D^6,a^2\le A^2+\epsilon_{a^2},
\nu^2\le N^2+\epsilon_{\nu^2}$，即得式(334.20)最后一行。式(334.21)保证 $a>0,P>0$，由命题334-A完成。证毕。

在第5节的固定角处，若 $D_1,D_2$ 是完整角导数线性映射，则可取
$\epsilon_d=\|D_1\|\epsilon_Y,\epsilon_e=\|D_2\|\epsilon_Y$。若同一 scalar 字段在这些参数上确实仿射，$\epsilon_a=\epsilon_\nu=0$；否则仍保原误差项。所有算子范数及RHS缺陷均须实际支付，不能以一阶FD或某个 trial 的小误差冒整段上界。

## 7. 与当前37查询及实际计算的边界

155仍可直接按已声明的完整37行组和原实际非线性检查运行；本结果不是它的前置门。以后若用此式建议步长或诊断线性/非线性差异，须保持下列身份：

- 明确哪个点是准确仿射节点、哪个是重算RHS后的真实中点/RMS查询；后者保式(334.16)的完整缺陷。
- 保全部物理角、所有选定query及完整原方向/core/参数支持，不把最坏角的一条多项式当全角结论。
- 原N2048表只给所声明离散角行；连续角须另按实际准确Fourier或完整复合表达支付整个角区间，不能从DFT采样或有限最小值直接推出。
- 字面实数提升、准确原实表达、实际浮点法向量程序三者分别绑定；严谨传递至浮点执行时还需其实际舍入包围，原 beta 与 cross_beta 的字差继续保留。
- 保存全部多项式/区间结果及未付范围的实际来源；仅源、参数、run/SHA和紧凑结论入库，可重算原输出在Actions临时读后清。旧141 raw已清，不能据其SHA补出缺失的八次系数或RHS二阶界。

本文没有计算任何当前37行的 $c_r$、Bernstein下界或 $\epsilon_P$；没有支付新查询域、merit下降、QP最优、非零场、同g闭合、reach或完成标准。所增加的是一个准确保留非线性项的有限代数工具及其真实Hermite误差责任，下一实际判断仍由原公开Actions中的完整问题给出。

环境说明：初稿的终端写入在共享环境失联时未确认完成；此正式文本由已写出的完整证明重建，源身份以本次发布字节为准，未假称原临时文件已保存。
