# R638：保留全部原形状方向的真实 P／动能双端图

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。

**已证明：在 R636 的显式物理输入附近，可以先用一个真实末高度控制准确消掉 P，再用唯一正幅值消掉动能端。所得局部图保留原 257 个自由方向，并始终满足两个真实偶端。** 关键不是把旧末高度列删掉：新增的显式五次控制不属于旧二阶 spline 规则的方向空间。本稿先增加这一真实方向，再消去一个真实方程。

这是连续积分的纸面图，不是已执行的数值根，也不支付其余两端、完整 ruling 或主题的宏观条件。实际消费时须验证同一分支的根和非零导数，并保留所有隐式历史链；不能只把 P 的打印值设成零。

## 1. 同一个真实形状与新增高度控制

使用 [R636](R636-explicit-c2-physical-input-with-two-true-even-ends.md) 的

$$
e=\frac14,\quad \ell=\frac34,\quad H=\frac{17}{20},\quad
B_* =\frac{585769}{207900},\quad L_*=4,
$$
$$
\psi(t)=t+4t^3-7t^4+3t^5,\qquad S(t)=10t^3-15t^4+6t^5.
$$

在整个归一化区间定义实际控制

$$
\sigma(x)=
\begin{cases}0,&0\le x\le e,\\ S((x-e)/\ell),&e\le x\le1.
\end{cases}                                                   \tag{1}
$$

它属于 $C^2[0,1]$，在中心附近恒为零，且
$\sigma(1)=1,\sigma'(1)=\sigma''(1)=0$。R636 的背景就是

$$
h_*=H+(B_*-H)\sigma,\qquad
\kappa_*=
\begin{cases}-\psi(x/e),&x\le e,\\-1,&x\ge e.\end{cases}          \tag{2}
$$

保留 $\kappa(0)=0,\kappa_x(0)=-4,\kappa_{xx}(0)=0$，
$h_x(0)=h_x(1)=\kappa_x(1)=0$ 等原 C² germ。$h_{xx}(0)$ 仍是自由形状坐标。

先在任意满足这些 germ 的有限维 C² 方向空间中写

$$
h=h_*+v+b\sigma,\qquad \kappa=\kappa_*+z,\qquad L>0,              \tag{3}
$$

其中 $v(1)=0$；所以 $b$ 确实是末高度 $h(1)-B_*$。
第 5 节给出保留原全部 257 个参数的具体 $v,z,L$ 表示。

定义同一条曲线的真实历史

$$
\eta_\kappa(x)=\int_0^x\frac{\kappa_y}{2h}\,dy,
\quad d_\kappa=h\eta_\kappa-\kappa,
\quad P_0(h,\kappa)=-\int_0^1\kappa d_\kappa.                    \tag{4}
$$

这里没有独立的 stored $\eta$ 或 $d$。$P_0$ 与物理长度无关。

## 2. 明确非零的末高度导数

在背景 (2)，第一段有 $h=H$，第二段有 $\kappa=-1$，故

$$
\eta_{\kappa_*}(x)=\frac{\kappa_*(x)}{2H}\quad(x\le e),
\qquad \eta_{\kappa_*}(x)=-\frac1{2H}\quad(x\ge e).
$$

只改变 (3) 的 $b$ 时，$\kappa_*'$ 与 $\sigma$ 的支持不相交。
因此 $\partial_b\eta_{\kappa_*}=0$，并且

$$
\boxed{
\partial_bP_0(h_*,\kappa_*)
=-\int_e^1(-1)\sigma(x)\left(-\frac1{2H}\right)dx
=-\frac{\ell}{4H}=-\frac{15}{68}.}                              \tag{5}
$$

用的是 $\int_0^1S=1/2$；没有有限采样或特殊函数近似。
背景本身由 R636 准确满足 $P_0=0$。

**局部真实 P 图。** 存在背景参数的一个开邻域，及唯一光滑函数
$b=b(v,z)$，满足 $b(0,0)=0$ 和

$$
P_0(h_*+v+b(v,z)\sigma,\kappa_*+z)=0.                            \tag{6}
$$

证明：在正高度 C² 邻域内，(4) 的积分及除法是光滑的有限参数映射。
(5) 非零，所以有限维隐函数定理直接给出 (6)。缩小邻域后还可保持

$$
\partial_bP_0<-\frac{15}{136}.                                  \tag{7}
$$

这也给出实际标量根的可复用定位方式。固定一个充分小的 $b$ 半宽 $r_b$，
若候选形状在整段 $[-r_b,r_b]$ 上满足 (7)，且

$$
|P_0(h_*+v,\kappa_*+z)|<\frac{15}{136}r_b,
$$

则两个端点的真实 $P_0$ 异号，整个区间严格单调，并有且仅有一个根。
这不是准许以 Newton 迭代停止值代替根：执行时仍须实际支付括号、导数和积分误差。

## 3. 全部离根历史导数与隐式链

对任意当前正高度曲线，给一个真实形状方向 $(V,Z)$，记

$$
\dot\eta_\kappa(x)
=\int_0^x\left(\frac{Z_y}{2h}-\frac{\kappa_yV}{2h^2}\right)dy,
\qquad
\dot d_\kappa=V\eta_\kappa+h\dot\eta_\kappa-Z.                    \tag{8}
$$

那么完整导数为

$$
\boxed{DP_0[V,Z]
=-\int_0^1\{Z d_\kappa+\kappa(V\eta_\kappa+h\dot\eta_\kappa-Z)\}.} \tag{9}
$$

对 (6) 的自由方向 $(\dot v,\dot z)$，

$$
\dot b=-\frac{DP_0[\dot v,\dot z]}{DP_0[\sigma,0]},\qquad
\dot h=\dot v+\dot b\sigma,\qquad \dot\kappa=\dot z.             \tag{10}
$$

分子中的 $\dot v$ 不含尚未求出的 $\dot b$，分母在当前根上评价。
(7) 保证该分母远离零。把 (10) 代回 (8) 才得到真正的历史方向；
一般扰动后 $\kappa'$ 不再支持于第一段，不能继续把
$\partial_b\eta_\kappa$ 误置为零。(5) 只是在明确背景点上的简化。

## 4. 与正动能幅值组合，准确消掉两个原偶端

对 (6) 的真实形状，令

$$
K_0=\int_0^1\kappa^2,\qquad U=\int_0^1(h_x/h)^2,\qquad
\alpha=\left(\frac{1+U/L^2}{K_0}\right)^{1/2}>0,                \tag{11}
$$
$$
k=\alpha\kappa,\qquad \eta=\alpha\eta_\kappa,
\qquad d=\alpha d_\kappa.
$$

$K_0,U$ 在背景均正；小邻域中继续为正。由
[R612 的真实末矩身份](R612-exact-physical-length-elimination-and-three-true-end-integrals.md)，

$$
\frac{A_{p_1}(L)}L=\alpha^2P_0=0,
\qquad
\frac{8A_{t_1}(L)+2A_{p_1}(L)}L
=\alpha^2K_0-1-U/L^2=0.                                      \tag{12}
$$

所以 $A_{p_1}(L)=A_{t_1}(L)=0$，都针对同一实际轨道。
在把 $b,\alpha$ 暂作独立变量时，这两个归一化方程在共同根的控制 Jacobian 是

$$
\begin{pmatrix}
\alpha^2P_{0,b}&0\\
-U_b/L^2&2\alpha K_0
\end{pmatrix},\qquad
\det=2\alpha^3K_0P_{0,b}\ne0.                                 \tag{13}
$$

它解释了两次消元为何不会把一个依赖方程重复当作两个控制。

全部导数仍明确保留。对 (10) 的总高度方向，

$$
\dot U=2\int\frac{h_x}{h}
 \left(\frac{\dot h_x}{h}-\frac{h_x\dot h}{h^2}\right),
\qquad \dot K_0=2\int\kappa\dot\kappa,
$$
$$
\boxed{\frac{\dot\alpha}{\alpha}
=\frac{\dot U-2U\dot L/L}{2(L^2+U)}
-\frac{\dot K_0}{2K_0}.}                                      \tag{14}
$$

然后
$\dot k=\dot\alpha\kappa+\alpha\dot\kappa$、
$\dot\eta=\dot\alpha\eta_\kappa+\alpha\dot\eta_\kappa$。
八个 A、六个 rho、全程系数、正势和规范都必须消费这条完整链。
若标量根尚未准确解到零，物理 P 的离根导数仍是
$2\alpha\dot\alpha P_0+\alpha^2\dot P_0$；不能提前删第一项。

R636 给背景全程物理盒的严格内部界；C² 依赖、积分连续性和 (10)—(14)
遂给一个同样在原盒内部的开邻域。中心 $\kappa_x=-4$ 保持，实际
$v=k_s(0)=-4\alpha/L\ne0$。背景 $B_2=-H\alpha^2/4<0$，
也在足够小的邻域继续非零。此处没有借旧正 $B_2$ 数值支的资格。

## 5. 保留原 257 个方向的准确有限空间

原 R632/R636 使用 65 个均匀节点。其形状自由度为：
129 个 h 方向、127 个 κ 方向，以及一个绝对 L，共 257 个。
记旧 h 方向空间为 $V_h$，基为 $\phi_1,\ldots,\phi_{129}$。
这些方向的节点二阶导数由节点一阶数据的 C² cubic spline 导出，
仅中心二阶另设自由坐标；定义见
[`r632_true_hermite_kinetic_chart.py`](../scripts/r632_true_hermite_kinetic_chart.py)。

先证明本稿的 $\sigma\notin V_h$，而不是根据五次次数猜测。
若 $\sigma\in V_h$，设 T 是其节点速度数据的那个 C² cubic spline。
在分界 $e=1/4$ 左邻节点区间，$\sigma'=\sigma''=0$ 于两端；
于是 T 的值和一阶导数均为零，唯一 cubic Hermite 多项式就是零。
故 $T''(e-)=0$。

在右邻区间 $[e,e+\Delta]$，$\Delta=1/64$，真正速度是四次式

$$
Q(x)=\sigma'(x)
=\frac{30(x-e)^2}{\ell^3}-\frac{60(x-e)^3}{\ell^4}
 +\frac{30(x-e)^4}{\ell^5}.
$$

假设 $\sigma\in V_h$ 还要求 T 在该区间两端同时匹配 Q 和 Q'。
因此四次差的两个端点都是二重零，且其最高系数确定，故

$$
Q(x)-T(x)=\frac{30}{\ell^5}(x-e)^2(x-e-\Delta)^2.
$$

从而

$$
T''(e+)=\frac{60}{\ell^3}
\left(1-\frac{\Delta^2}{\ell^2}\right)>0,
$$

与 T 的 C² 性矛盾。分界附近节点都不是中心，因此中心二阶自由替换不影响此论证。

现在定义

$$
\widehat\phi_i=\phi_i-\phi_i(1)\sigma.                         \tag{15}
$$

它们全部末值为零，而且仍有 129 个线性独立方向：若某个线性组合为零，
则一个 $V_h$ 元素等于其末值乘 $\sigma$；由 $\sigma\notin V_h$，
该末值和该元素都为零，再由旧基独立性得所有系数为零。

取 $v=\sum q_i\widehat\phi_i$，原 127 个 κ 方向和绝对 L 全部照留。
在尚未解 (6) 时，(3) 有 $129+127+1+1=258$ 个独立参数。
它包含原全部形状变化：旧 $v_{\rm old}=\sum q_i\phi_i$ 对应
$v=\sum q_i\widehat\phi_i$ 与 $b=v_{\rm old}(1)$。

随后用 (6) 唯一解掉 b，得到 **257 个自由参数** 的准确 P 图；
再由 (11) 确定原已消去的幅值 α。这里没有删除旧末高方向，
也没有把显式 $\sigma$ 冒称为旧 spline 方向。
由 $V_h\cap\operatorname{span}\{\sigma\}=0$，该有限参数图在真实形状空间中亦为浸入。

## 6. 实际消费及仍须完成的方程

本图的两个端零是连续定义。实际离散执行若只用固定求积求出 b、α，
所得只能先称该离散图的零；连续积分误差仍须单独控制。
在同曲线 fine 中，必须冻结已经选定的 b、α、L、全部形状系数、八中心 A
及三常规范；不能在 fine 重新解 P 或能量后把新曲线称为同一条。

余下 $A_{r_1}(L),A_{s_0}(L)$、所有原 ruling、历史一致性及原绝对门仍在。
本稿没有将它们替换为任意端口目标，也没有改变原十八块母、全正势或物理盒。
若局部标量图的导数门丢失，应保留实际未完输入并换合法图或输入，
而不是删掉该控制方程、强制 clipping 或把 P 设为 stored 零。

R632 与 R636 已声明的活动范围继续独立消费；本稿给的是之后可实际接入的
新共同端图，不篡改任何已运行来源或接受条件。
