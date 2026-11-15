# R185：重叠八包圆的周期核内六矩右逆与十个 ruling 方向

日期：2026-11-15。**完整纸面证明；没有新的 profile 积分、几何计算或算子编译。** 来源为 [R183 导数分包重叠圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R181 周期 gauge 方程](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md) 与 [R184 完整第四联合判据](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)。

本稿固定 R183 已构造的同一几何与 profile 圆。其整个二阶周期算子为零，整个第三算子为非零 $\kappa\mathfrak H$，完整二、三阶 range 已支付。新增结论是：第四周期方程的像，在加上全部六个交叉矩条件后完全不缩小。六矩可以由周期算子的一个明确十六维核空间支付；其中还剩十维保持周期及第三 range 的方向，可用于第四 ruling。

没有声称这十个方向在 ruling 商中独立，也没有证明第四联合方程已有解。

## 1. 完整 packet 与共同导数空间

把 R183 的一个完整基本 packet 记作 $(f_*,g_*)$。它已经包含左侧三矩补偿，实线性无关，且

$$
\mathbf m(f_*,g_*)=0,\qquad
\mathbf m(f_*,f_*)=\mathbf m(g_*,g_*)=(E,\mu_1,\mu_2),
\qquad E>0, \tag{1}
$$

其中

$$
\mathbf m(a,b)=\left(
\int a''b'',\ \int\xi a''b'',\
\int\xi^2a''b''+2\int a'b'\right).
$$

取八个互不交的完整平移包

$$
f_j(\xi)=f_*(\xi-t_j),\qquad
g_j(\xi)=g_*(\xi-t_j),\qquad
t_j=t_*+jL,\quad j=0,\ldots,7,
$$

以及 R183 的非零幅度

$$
a_j=(-1)^j\binom7j^{1/3},\qquad
f=\sum_j a_jf_j,\quad g=\sum_j a_jg_j. \tag{2}
$$

共同缩放到物理区间以后，仍可在缩放后的坐标中使用相同记法。以下只用 $a_j\ne0$、平移中心互异及完整包支撑不交，不使用浮点幅度。

定义

$$
\mathcal K=\operatorname{span}_{\mathbb R}
\{f_0,\ldots,f_7,g_0,\ldots,g_7\}. \tag{3}
$$

每个完整包内的 $(f_j,g_j)$ 实线性无关，不同包支撑不交，故

$$\dim\mathcal K=16. \tag{4}$$

R183 的导数分包性质对整个 $\mathcal K$ 成立：在每个更小的导数包内，任意 $v\in\mathcal K$ 的所有正阶导数都是同一个辅助实 profile 正阶导数的固定倍数。R183(1) 的 hook 原式只有同点三次正阶导数密度和单层右积分。因此相同的逐包证明给

$$
\boxed{\mathfrak H|_{\mathcal K\times\operatorname{Sym}^2\mathcal K}=0.} \tag{5}
$$

这比只在原二维平面上取零更强，但仍仅是这个具体导数分包空间的恒等式。

令

$$L_f(w)=\mathfrak H(w;f,f).$$

由于 $f\in\mathcal K$，

$$\boxed{\mathcal K\subset\ker L_f.} \tag{6}$$

所有 $\mathcal K$ 中的函数本身都是共同双 collar 为零的光滑 profile；这里没有把带非零端值的辅助原函数拿来当合法 gauge。

## 2. 六交叉矩在这个周期核上满射

平移 (1) 得

$$
\mu_j:=\mathbf m(f_j,f_j)=\mathbf m(g_j,g_j)
=\left(E,\ \mu_1+Et_j,\
\mu_2+2\mu_1t_j+Et_j^2\right), \tag{7}
$$

且 $\mathbf m(f_j,g_j)=0$。不同完整包之间所有交叉矩均为零。

对

$$v=\sum_j(c_jf_j+d_jg_j)\in\mathcal K,$$

准确有

$$
\boxed{
\mathbf m(f,v)=\sum_j a_jc_j\mu_j,\qquad
\mathbf m(g,v)=\sum_j a_jd_j\mu_j.} \tag{8}
$$

任取三个不同中心，例如 $t_0,t_1,t_2$，令

$$V=(\mu_0\ \mu_1\ \mu_2).$$

这里矩阵列符号 $\mu_j$ 指 (7) 的三维向量，不与基本 packet 的标量 $\mu_1,\mu_2$ 混用。逐行消元给

$$
\det V
=E^3(t_1-t_0)(t_2-t_0)(t_2-t_1)\ne0. \tag{9}
$$

所以

$$
\mathcal M_6:\mathcal K\longrightarrow\mathbb R^3\oplus\mathbb R^3,
\qquad v\longmapsto(\mathbf m(f,v),\mathbf m(g,v))
$$

满射。一个明确固定右逆如下：给定 $r_f,r_g\in\mathbb R^3$，置

$$
(c_0,c_1,c_2)^T
=\operatorname{diag}(a_0,a_1,a_2)^{-1}V^{-1}r_f,
$$

$$
(d_0,d_1,d_2)^T
=\operatorname{diag}(a_0,a_1,a_2)^{-1}V^{-1}r_g,
$$

其余系数为零，并令

$$
\boxed{
S_6(r_f,r_g)=\sum_{j=0}^2(c_jf_j+d_jg_j).} \tag{10}
$$

于是 $\mathcal M_6S_6=\mathrm{id}$，同时由 (6)，

$$L_fS_6=0. \tag{11}$$

该右逆只使用已经给定的完整 packet 与三个平移中心，不改变几何、圆、目标度量或真实锚。

## 3. 六矩约束不缩小第四周期方程的像

记 $\mathcal X$ 为在固定双 collar 为零的实光滑 profiles，定义

$$
\mathcal X_0=\{w\in\mathcal X:
\mathbf m(f,w)=\mathbf m(g,w)=0\}. \tag{12}
$$

定义固定线性投影

$$
\boxed{
\mathcal Qw=w-S_6(\mathbf m(f,w),\mathbf m(g,w)).} \tag{13}
$$

则

$$
\mathcal Q(\mathcal X)\subset\mathcal X_0,\qquad
\mathcal Q|_{\mathcal X_0}=\mathrm{id},\qquad
L_f\mathcal Q=L_f. \tag{14}
$$

因此得到完整函数像恒等式

$$
\boxed{L_f(\mathcal X_0)=L_f(\mathcal X).} \tag{15}
$$

这不是离散矩阵的近似秩结论。给定任意目标函数 G，若存在共同 collar 的光滑 $w$ 使 $L_f(w)=G$，则 $\mathcal Qw$ 是满足全部六交叉矩的同一个周期方程解。反向包含显然。

在 R184 的非零 hook 几何上，第四周期改变量是 $2\kappa L_f(w_\theta)$。六矩为零足以保证新增第三 forcing 的全部 ruling 为零，而整个二阶算子为零保证其完整周期为零。因此 (13) 能在不改变第四周期函数的条件下，准确支付这项低阶合法性要求。

若原 $w_\theta$ 随 $\theta$ 光滑、$2\pi$ 周期，且 $w_0=w_\pi=0$，固定线性投影 $\mathcal Q$ 保留这些性质。修正并不依赖逐 s 选择，也不需要为每个相位重新解一个退化 Gram 问题。

**联合问题的边界。** $\mathcal Q$ 通常会改变 R184 的线性 ruling 响应 $\mathcal B_\theta(w)$。式 (15) 只证明周期像不缩小，不能据此说完整 period 与 ruling 的联合像也不缩小。因此它不能把 R184 的准确相位定义域无条件替换为六矩强约束。

## 4. 十个明确的周期不变、第三合法方向

由 (4)、(8)，

$$
\boxed{\dim(\mathcal K\cap\mathcal X_0)=16-6=10.} \tag{16}
$$

对 $j=3,\ldots,7$，定义

$$
v_j^f=f_j-S_6(a_j\mu_j,0),\qquad
v_j^g=g_j-S_6(0,a_j\mu_j). \tag{17}
$$

它们都属于 $\mathcal K\cap\mathcal X_0$。在线性组合中限制到第 j 个完整包，右逆项仅在第 0、1、2 包，故余下恰是该包的 $f_j,g_j$ 组合；两者独立迫对应两系数为零。这样十个函数构成 (16) 的一个真基。

取某个已满足六矩的周期解 $w_\theta^{\rm per}$，再置

$$
w_\theta=w_\theta^{\rm per}
+\sum_{\ell=1}^{10}b_\ell(\theta)v_\ell. \tag{18}
$$

任意平滑周期 $b_\ell$ 都保持原周期方程及六矩。要求 $b_\ell(0)=b_\ell(\pi)=0$ 即保留准确种子。

在 R184 的真实商空间 $C^\infty(S_s^1)/\mathcal W$ 中，待付 ruling 准确变成

$$
\left[K^0_\theta+\mathcal B_\theta(w_\theta^{\rm per})\right]
+\sum_{\ell=1}^{10}b_\ell(\theta)
[\mathcal B_\theta(v_\ell)]=0. \tag{19}
$$

这是同一几何上的真实全函数线性方程。十个 profile 方向独立，并不推出它们的十个 ruling 像独立；其像也可能有非零核。式 (19) 只是一个明确有限充分搜索空间，不穷尽所有周期核方向。

## 5. 十方向的 ruling 数据只需三个相位系数

采用 R183 已付 range 的 $Z_d,Z_c$，并记

$$
Z_\theta=s^2Z_d-csZ_c,\qquad c=\cos\theta,\ s=\sin\theta.
$$

对任一 $v\in\mathcal K\cap\mathcal X_0$，$Z_B(f,v)$、$Z_B(g,v)$ 都是合法的周期、双 collar 二阶恢复：其完整 ruling 由六矩为零支付，周期由整个二阶算子为零支付。

所有以下内积都沿同一真实 physical ruling 积分，保留真实 s 历史：

$$
A_v=\int(Z_d)_u\cdot(Y_v)_u\,du,\qquad
C_v=\int(Z_c)_u\cdot(Y_v)_u\,du,
$$

$$
F_v=\int(Y_f)_u\cdot Z_B(f,v)_u\,du,\qquad
G_v=\int(Y_g)_u\cdot Z_B(g,v)_u\,du,
$$

$$
E_v=\int(Y_f)_u\cdot Z_B(g,v)_u\,du
+\int(Y_g)_u\cdot Z_B(f,v)_u\,du.
$$

直接展开 R184 的原式，无须重新编译整个第四 forcing，得到

$$
\mathcal B_\theta(v)
=2s^2A_v-2csC_v
-4(c^2F_v+s^2G_v+csE_v). \tag{20}
$$

也就是

$$
\boxed{
\mathcal B_\theta(v)
=B_{0,v}+B_{c,v}\cos2\theta+B_{s,v}\sin2\theta,} \tag{21}
$$

$$
B_{0,v}=A_v-2F_v-2G_v,\quad
B_{c,v}=-A_v-2F_v+2G_v,\quad
B_{s,v}=-C_v-2E_v. \tag{22}
$$

所以这十方向只需三十个真实 s 函数及既有三维 $\mathcal W$。R56 的分离变量原式可生成它们；这里只确定接口与准确公式，尚未计算任何真实函数秩或评估一条几何。

尤其不能在不同几何段重新选择右锚或 s 初值，也不能因为某个 complete packet 局部化就删掉 $Z_B(f,v)$ 的跨包历史。

## 6. 仅周期问题还可准确限制为四个相位系数

原 canonical 第四周期 $V^0_\theta$ 仅含 $0,\pm2,\pm4$ 相位，且在 $0,\pi$ 为零。因此可唯一写成

$$
V^0_\theta
=G_1(1-\cos2\theta)+G_2\sin2\theta
+G_3(1-\cos4\theta)+G_4\sin4\theta. \tag{23}
$$

由于 $L_f$ 不依赖相位，周期方程对全相位可解，当且仅当四个真实函数 $G_i$ 都属于 $L_f(\mathcal X)$；有限个相位值即可反解这四个系数，所以这里不依赖函数像的闭性。

若每个方程 $2\kappa L_f(u_i)=-G_i$ 有解，将它们都经 (13) 投影，再取

$$
w_\theta^{\rm per}
=(1-\cos2\theta)\mathcal Qu_1+\sin2\theta\,\mathcal Qu_2
+(1-\cos4\theta)\mathcal Qu_3+\sin4\theta\,\mathcal Qu_4, \tag{24}
$$

就得到平滑周期、种子为零、六矩为零的周期解。

这只是**周期部分**的有限相位结论。联合 ruling 方程可能需要加入周期核中更多相位依赖；本稿没有把 (24) 的四系数形式提升为完整第四解的无损相位限制。

## 7. 仍需解决的具体项

R181 对 $L_f$ 的退化 ODE、每包通量及内部退化点条件依然存在；六矩右逆不会使一个本来不在 $L_f$ 像内的周期目标变为可解。对于当前 R183 几何与 profile，尚未给出实际 $G_i$，也没有评价这些不变量。

若周期已通过，(19)–(22) 给一个比重新构造 universal 响应列小得多的真实 ruling 接口。它可能给充分修正，也可能暴露该十维子空间的不足；两种判断都需要同一冻结几何与 profile 上的全函数证据。

本稿没有构造第四完整形式解，更没有支付更高阶、收敛、有限参数等距、嵌入或 reach。

