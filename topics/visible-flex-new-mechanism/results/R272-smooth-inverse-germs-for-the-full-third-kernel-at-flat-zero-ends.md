# R272：全第三核在指数全平零端的光滑逆解

日期：2026-11-15。**完整纸面证明；没有新研究计算、人工检查、profile 求积或旧算子重编。** 本稿证明一个此前未付的端点结论：对明确的指数全平零端，完整十八维第三核的 K 输出只要已经满足真实平台与总通量条件，R225 的平端逆解 germ 就自动光滑。内部退化点和同一校正的 ruling 仍须另外处理。

来源：[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md)、[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R264](R264-potential-tail-moments-and-complete-platform-flux-equivalence.md)。与 [R236](R236-quadratic-endpoint-principal-part-criterion.md) 的临界二次层一致；以下直接证明完整光滑余项的积分结论，不只比较有限渐近项。

## 1. 精确端点类与要解的原方程

令 e 为一个真实活动区间的端点，取向内坐标 $t>0$，使
$x=e+\sigma t$、$\sigma\in\{1,-1\}$。假设

$$
f(e)=0,\qquad p(x)=f'(x)
=t^m a(t)e^{-c/t},\qquad c>0,\quad m\in\mathbb Z,
\tag{1}
$$

其中 $a\in C^\infty([0,t_0])$ 且 $a(0)\ne0$。缩小 $t_0$ 后 a 处处非零。允许 m 为负：指数仍使 p 及全部导数全平为零。这涵盖原标准指数 bump 的导数所带有限幂前因子，不把它误作必须有界的 a。

设

$$
G=\sum_{\alpha=1}^{M}K_f^{\tau_\alpha}(w_\alpha),
\qquad \tau_\alpha\in Z,\quad w_\alpha\in C^\infty(I),
\tag{2}
$$

且全部 K 使用原共同右锚。每个 $w_\alpha$ 可以含真实左尾。研究 R225 的原 period 方程 $\mathcal L_fv=G$，用

$$
u=v',\quad A_H=6pp''-2(p')^2,\quad
\mathcal F(x)=\int_{a_j}^x pG''
\tag{3}
$$

记相应活动区间的真实通量。正则子区间上的原变参数式为

$$
u=p\left(C+\int \frac{\mathcal F}{A_Hp^2}\,dx\right).
\tag{4}
$$

**本稿的端点前提**是 $G''(e)=0$ 与 $\mathcal F(e)=0$。前者由相邻真实平台的 $G''=0$ 支付；左活动端的后者来自定义，右活动端的后者正是原总通量门。不能在右端重新减掉一个未支付的通量常数。

结论是 (4) 在 e 有真实 $C^\infty$ 延拓，而且其端值由 G 决定。本文不从 $f$ 全平或有限个形式通量为零直接推此结论；下面证明必要的完整增长界和精确积分性质。

## 2. 两个精确指数积分引理

记 $p(t)=t^m a(t)e^{-c/t}$。

### 2.1. 衰减端积分

若 $k$ 为正整数、$r\in\mathbb Z$、$B\in C^\infty([0,t_0])$，则

$$
\boxed{
\int_0^t p(s)^k s^rB(s)\,ds
=p(t)^k t^{r+2}H(t),\qquad H\in C^\infty([0,t_0]),
\quad H(0)=\frac{B(0)}{kc}.}
\tag{5}
$$

**证明。** 作精确变量替换 $z=1/s-1/t$，即
$s=t/(1+tz)$。除去右边的 $p(t)^kt^{r+2}$ 后，积分准确为

$$
H(t)=\int_0^\infty e^{-kc z}
(1+tz)^{-(km+r+2)}
\left[\frac{a(t/(1+tz))}{a(t)}\right]^k
B\!\left(\frac t{1+tz}\right)\,dz.
\tag{6}
$$

a 及其有限阶导数有界，分母远离零。对每个固定微分阶，(6) 中被积函数及其 t 导数均由 $e^{-kc z}$ 乘一个固定 z 多项式控制，适用于 $0\le t\le t_0$。故可逐阶在积分号内求导，得到所有右端导数连续延拓至零。代 $t=0$ 给 (5) 的端值。由标准单侧光滑延拓可在零的另一侧接成 $C^\infty$ germ。这里得到的是精确光滑余项，不仅是一条形式渐近级数。

### 2.2. 逆指数原函数

若 $B\in C^\infty([0,t_0])$，则

$$
\boxed{
p(t)\int_{t_0}^{t}p(s)^{-1}s^{-2}B(s)\,ds
\ \text{在 }t=0\text{ 光滑},\qquad
\lim_{t\downarrow0}=-\frac{B(0)}c.}
\tag{7}
$$

任何改变积分参考点所增加的常数乘 p 都全平光滑。

**证明。** 对反向积分作精确替换 $z=1/t-1/s$，得

$$
p(t)\int_t^{t_0}p(s)^{-1}s^{-2}B(s)\,ds
=\int_0^{1/t-1/t_0} e^{-cz}(1-tz)^m
\frac{a(t)}{a(t/(1-tz))}
B\!\left(\frac t{1-tz}\right)\,dz.
\tag{8}
$$

取一个关于 $tz$ 的固定光滑截断，在 $tz\le1/2$ 等于1、$tz\ge3/4$ 等于0。对充分小 t，截断区位于 (8) 的实际积分域内。其内 $s\le4t$、$1-tz\ge1/4$，全部 t 导数由 $e^{-cz}$ 乘多项式控制，故截断积分在零光滑，端值 $B(0)/c$。

剩余部分满足 $z\ge1/(2t)$；即使 m 为负，因实际 $s\le t_0$，所有系数、积分端点及其固定阶导数至多增长一个 t 的负幂。它们乘 $e^{-c/(2t)}$ 后全平。故完整 (8) 与截断积分只差一个光滑全平函数。取负号得到 (7)。证毕。

两引理允许任意光滑 B，并未要求 B 解析、只有有限 Laurent 项或满足额外的端点消失条件。

## 3. 全 Z 的局部系数具有统一 jet 总权上界

写完整源为

$$
D^3K_f^\tau(w)=\mathscr A_f^\tau w,\qquad
\mathscr A=aD^4+2a'D^3+dD^2+(d'-a''')D+c_0.
\tag{9}
$$

用 $c_0$ 区别于 (1) 的正指数常数 c。对二次 jet 单项式
$f^{(i)}f^{(j)}$ 定义总权 $i+j$，显式 x 多项式不计入 jet 权。

**引理。** 对全部 $\tau\in Z$，

$$
\boxed{
\operatorname{wt}(a)\le4,\qquad
\operatorname{wt}(d)\le6,\qquad
\operatorname{wt}(c_0)\le7.}
\tag{10}
$$

这里指已付原局部多项式中每一项的上界，不是固定 f 的非零阶数或 rank。

对 R261 的八条系数，(10) 可以直接从人读全表读取：a 的最高型为 $f'f'''$ 或 $(f'')^2$，d 的最高型为 $f'f^{(5)},f''f^{(4)},(f''')^2$，$c_0$ 的最高型为 $f''f^{(5)}$ 或 $f'''f^{(4)}$；其他项权更低。

对 H、J 两根，R258 的完整式直接给 (10)。需要说明整个 $\delta$ 链也保持它，而非默认最高 jet 不增长。记 $\mathscr A=\sum_{k=0}^4u_kD^k$，则由正确的
$-Z^*\mathscr A-\mathscr AZ-D_f\mathscr A[Zf]$，其中
$Z=x^2D-2x$，逐项乘法法则给

$$
\boxed{
u_k^{\rm new}
=x^2Du_k+(6-2k)xu_k
+(k+1)(2-k)u_{k+1}-D_fu_k[Zf],
\quad u_5=0.}
\tag{11}
$$

关键是完整 seed 项。因为

$$
D^j(Zf)
=x^2f^{(j+1)}+2(j-1)xf^{(j)}
+j(j-3)f^{(j-1)},
\tag{12}
$$

$j=0$ 时最后零系数项省去，(11) 中 $x^2Du_k$ 所产生的增加一阶 jet 项与 $D_fu_k[Zf]$ 准确相消。余项只保原权或降低权，显式 x 的导数也不增 jet 权。

对 $k=4$，无邻系数项，所以 a 的上界保持4。对 $k=2$，$(k+1)(2-k)=0$，d 的上界保持6。对 $k=0$，只多 $2u_1=2(d'-a''')$，其上界为7。故 $c_0$ 的上界保持7，归纳支付整个 H/J 链。线性组合给全 Z。此为一般系数递推的纸面界，没有重新展开或重算任何已付链。

## 4. 零端使完整源进入临界衰减类

由 $f(e)=0$、$f'=p$ 及引理 (5) 的 $k=1,r=0$，

$$
f(e+\sigma t)=\sigma\int_0^t p(s)\,ds
=p(t)t^2A_0(t),\qquad A_0\in C^\infty,\quad A_0(0)=\sigma/c.
\tag{13}
$$

由 (1) 逐次微分，对任意固定 $i\ge1$ 有

$$
f^{(i)}(e+\sigma t)
=p(t)t^{2-2i}A_i(t),\qquad A_i\in C^\infty.
\tag{14}
$$

所以一个总权不超过 W 的二次 jet 多项式属于
$p^2t^{4-2W}C^\infty$；权更低的项只多非负整数幂 t。显式 x 系数在真实有限端点光滑。

将 (10) 代入 (9)，得到

$$
a\in p^2t^{-4}C^\infty,\quad
a'\in p^2t^{-6}C^\infty,\quad
d\in p^2t^{-8}C^\infty,
$$

$$
d'-a''',\ c_0\in p^2t^{-10}C^\infty.
\tag{15}
$$

每个 $w_\alpha$ 及所需有限导数在端点光滑，故对整个 (2)，

$$
\boxed{G'''=p^2t^{-10}S(t),\qquad S\in C^\infty.}
\tag{16}
$$

有限方向之间的相消自然保留。这里不要求逐方向的平台或通量分别为零。

由于实际 $G''(e)=0$，从 e 向内积分 (16)，用 (5) 的 $k=2,r=-10$ 得

$$
\boxed{G''=p^2t^{-8}R(t),\qquad R\in C^\infty.}
\tag{17}
$$

没有把一个未付的常数偷偷消去：原平台二导为零正是本步骤所需的积分常数条件。

## 5. 完整通量与原逆解 germ

同样，由真实 $\mathcal F(e)=0$，

$$
\mathcal F(e+\sigma t)
=\sigma\int_0^t p(s)G''(e+\sigma s)\,ds.
$$

对 (17) 使用 (5) 的 $k=3,r=-8$，得到

$$
\mathcal F=\sigma p^3t^{-6}R_1(t),\qquad
R_1\in C^\infty,\quad R_1(0)=\frac{R(0)}{3c}.
\tag{18}
$$

另一方面，(1) 给

$$
\boxed{
A_H=p^2t^{-4}\overline A(t),\qquad
\overline A\in C^\infty,\quad \overline A(0)=4c^2>0.}
\tag{19}
$$

因此足够靠近这个端点没有新的 $A_H$ 零点。原 Green 商准确属于

$$
\frac{\mathcal F}{A_Hp^2}
=\sigma p^{-1}t^{-2}\frac{R_1}{\overline A}.
\tag{20}
$$

在 (4) 中 $dx=\sigma\,dt$，两次方向符号相消。利用引理 (7) 即得

$$
\boxed{u=v'\text{ 在 e 有 }C^\infty\text{ 延拓}.}
\tag{21}
$$

还得到不依赖自由常数 C 的端值

$$
\boxed{
u(e)=-\frac{R(0)}{12c^4},
\qquad
R(0)=\lim_{t\downarrow0}\frac{t^8G''(e+\sigma t)}{p(e+\sigma t)^2}.}
\tag{22}
$$

常数乘 p 在端点全平，所以不能改变 (22)。端值通常可以非零；R225 的平台连接允许这种真实光滑 jet，不应额外要求 u 在每个活动端全平。

左右端完全同理：只在右端必须先支付总通量，使 $\mathcal F(e)=0$。本文没有通过另选右端 primitive 回避这一门。

## 6. 对有限零端活动圆的完整 period 推论

设同一固定 f 的每个活动区间端点都为零端，且分别具有 (1) 的明确 germ；内部属于 R225 的解析、有限阶退化类。对 (2) 的实际 G：

1. 用 R264 对整个控制组合支付所有平台与总通量，保原右 collar 的 $G=G'=0$；
2. 在每个内部 p 或 $A_H$ 零点支付 R225 全部 Laurent 条件。

则本稿 (21) 自动给全部两端光滑 germ。R225 的原平台拼接和 $\int u=0$ 校正遂给真实全 I 解 $\mathcal L_fv=G$，并保两个 collar 的 v 零值。

因此，在这个明确零端类及这些 K 目标上，平端 germ 不再是独立待算观测；完整 period 尚余平台/总通量和内部 Laurent 的实际联合支付。它们的条数没有被当成独立 rank，本文也没有求出这些实际响应的联合像。

在整 profile 逐包比例圆上，若已由完整原式证明 $\zeta=K_f^\tau(g)=0$，R255 的两 mixed 只余
$2K_f^\tau(\Phi_E(f^2-g^2))$ 与
$-4K_f^\tau(\Phi_E(fg))$，其输入都光滑，故可直接用本推论。采用 $2\cos\theta\sin\theta$ 规范时 E 列仍除二。若 $\zeta$ 未证为零，额外 $\Phi_E(\cdot,\zeta)$ 历史不能被本稿吞掉。

## 7. 明确保留的范围

$f(e)=0$ 是实质条件。若端点常值 $F\ne0$，单项 $ff^{(5)}$ 等可只含一份 p；(13) 不成立，(16) 的二次衰减界便不能直接使用。旧非零 step 常端仍保原独立分析。

本文也不声称任意 C∞ 全平 germ 都有 (1)，不把更快或振荡型全平端自动纳入。真实 $w$ 必须光滑；原有限输入确有的多项式左尾不影响这一点，但奇异试输入不属于本定理。

全 $\mathcal R_{p0}$ 仍不等于 $B(E,Z)$，完整 canonical 成本的额外部分未获同一自动结论。真实带符号控制、全部内部条件、同一 v 的第四 ruling、同固定 g 的有限连续族及 README 的几何完成门均仍未支付。这里完成的是上述完整 K 类的准确零端光滑性，不是主课题完成。
