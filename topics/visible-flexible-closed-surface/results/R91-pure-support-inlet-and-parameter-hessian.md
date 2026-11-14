# R91：纯支撑入口的精确 G 缺陷与固定弧长参数 Hessian

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明。** 本文给出当前入口构造的精确几何恒等式：纯 $j=1$ 支撑与参考 warp 匹配时，真实截面本身等距且只有一个圆柱模式；其余理想有限 M 缺陷来自未截圆背景，具有阶乘小的明确上界。对实际允许的多个支撑参数，本文计算固定弧长的完整 Hessian 和真实 Taylor 积分余项，说明非线性重参数化的未表示部分从二阶开始。所有理想 Fourier/精确节点公式与 binary 保存图的严格入口检查分别说明；不以纯模特例代替新的 M15 实际参数。

## 1. 真实支撑曲线及共同材料角

取整数 $m\ge2$，$k_j=mj$，以及有限支撑系数 $c=(c_1,\ldots,c_J)$。定义

$$
h_c(\phi)=1+\sum_{j=1}^J c_j\cos(k_j\phi),\qquad
\rho_c=h_c+h_c''=1+\sum_j(1-k_j^2)c_j\cos(k_j\phi),
\tag{1}
$$

并假设 $\rho_c>0$。记 $e_r(\phi)=(\cos\phi,\sin\phi)$、$e_\theta=(-\sin\phi,\cos\phi)$。支撑曲线和其弧长材料角是

$$
\gamma_c(\phi)=h_c e_r+h_c'e_\theta,\qquad
A_c(\phi)=\phi+\sum_j\frac{1-k_j^2}{k_j}c_j\sin(k_j\phi).
\tag{2}
$$

逐项求导给 $\gamma_c'=\rho_c e_\theta$、$A_c'=\rho_c$。因此 $A_c$ 是满足 $A_c(\phi+2\pi)=A_c(\phi)+2\pi$ 的圆周微分同胚，曲线周长为 $2\pi$。令

$$
\Gamma_c(u)=\gamma_c(A_c^{-1}(u)).
$$

则准确地有 $\partial_u\Gamma_c=e_\theta(A_c^{-1}(u))$，故 $|\partial_u\Gamma_c|=1$。这正是当前 `PlanarSupportCore` 的材料参数定义。

固定一个参考 $c^*$，并用 $u=A_{c^*}(\psi)$ 作入口图。任何其他正支撑曲线在这个共同图中的准确角向度量都是

$$
\left|\frac{d}{d\psi}\Gamma_c(A_{c^*}(\psi))\right|^2
=\rho_{c^*}(\psi)^2.
\tag{3}
$$

因此支撑参数的变化不改变入口的物理度量；有限模近似造成的误差需要另算。

## 2. 当前纯单模特例及实际 round-background 分解

当前 $m=3$。令 $q_*$ 是参考幅度，$0<8q_*<1$，$c^*=(q_*,0,\ldots)$，记

$$
w=8q_*,\quad u_*(\psi)=\psi-\frac w3\sin3\psi,
\quad\rho_*(\psi)=1-w\cos3\psi.
\tag{4}
$$

若实际支撑恰好是这个 $c^*$，则 $A_{c^*}(\psi)=u_*(\psi)$，故正常角恰为 $\phi=\psi$，并且

$$
\Gamma_*(u_*(\psi))=
e^{i\psi}(1+q_*\cos3\psi-3i q_*\sin3\psi).
\tag{5}
$$

它的圆柱系数只有 $R_0=1,R_1=q_*,T_1=-3q_*$；其导数为 $i\rho_*e^{i\psi}$，所以相对 (3) 的 G 误差准确为零。这是纯截面本身的结论。

当前 `950f-prefix-warped-bvp.py::WarpedBVP.initial` 的表示另保留未截断圆背景

$$
B_*(\psi)=e^{iu_*(\psi)}.
$$

令 $P_M$ 是理想圆柱 Fourier 投影：对水平复坐标 $X$，
$P_MX=e^{i\psi}\Pi_{|j|\le M}(e^{-i\psi}X)$，其中局部频率为 $3j$。
在本反射对称类上，这与 $R_j\cos3j\psi\,e_r+T_j\sin3j\psi\,e_\theta$ 的投影一致。理想入口是

$$
F_M=B_*+P_M(\Gamma_*-B_*)
=\Gamma_*+(I-P_M)B_*,\qquad M\ge1.
\tag{6}
$$

式 (6) 保留了当前原函数的“未截 round 背景加有限扰动”约定；不能因为 (5) 本身是有限多项式就断言 (6) 也精确相同。

## 3. 纯特例的精确 G 公式与阶乘尾界

置 $z=e^{3i\psi}$、$b=w/6$，则

$$
B_*=e^{i\psi}E(z),\qquad
E(z)=\exp[-b(z-z^{-1})]=\sum_{j\in\mathbb Z} e_jz^j.
\tag{7}
$$

记 $T_M(z)=\sum_{|j|>M}e_jz^j$ 和
$S_M(z)=(1+3z\partial_z)T_M(z)$。由 (6)，误差导数是
$[(I-P_M)B_*]'=i e^{i\psi}S_M$，故有限入口的**精确**归一化 G 缺陷为

$$
\boxed{
\mathcal G_M(\psi)=
\frac{2\operatorname{Re}S_M(e^{3i\psi})}{\rho_*(\psi)}
+\frac{|S_M(e^{3i\psi})|^2}{\rho_*(\psi)^2}.}
\tag{8}
$$

这给出整个角域的函数，而不是只给两个轴点。

从 $E=\exp(-bz)\exp(bz^{-1})$ 相乘，$j\ge0$ 时

$$
e_j=(-1)^j\sum_{l\ge0}\frac{(-1)^l b^{j+2l}}{(j+l)!l!},
\qquad e_{-j}=(-1)^j e_j.
$$

所以

$$
|e_j|=|e_{-j}|\le e^{b^2}\frac{b^j}{j!}
\le\frac{b^j}{j!(1-b^2)}.
\tag{9}
$$

第二个不等式由 $0<b^2<1$ 和 $e^x\le(1-x)^{-1}$ 得出，后者逐项比较幂级数即可。
因 $|1+3j|+|1-3j|=6j$（$j\ge1$），

$$
\begin{aligned}
\|S_M\|_\infty
&\le\frac6{1-b^2}\sum_{j=M+1}^\infty\frac{j b^j}{j!}\\
&\le \mathcal T_M:={6b^{M+1}\over
(1-b^2)M!\,[1-b/(M+1)]}.
\end{aligned}
\tag{10}
$$

最后一步把 $j b^j/j!=b\,b^{j-1}/(j-1)!$，并用相邻项比至多 $b/(M+1)$。于是

$$
\boxed{\quad
\|\mathcal G_M\|_\infty\le
\frac{2\mathcal T_M}{1-w}
+\frac{\mathcal T_M^2}{(1-w)^2}.
\quad}
\tag{11}
$$

这不是把误差作为物理渐近参数压小：M 是对同一精确截面、同一物理入口度量的数值频率。并且本条只解释入口，不付全曲面的加密门。

## 4. 精确 N 点投影与当前幅度的严格数量级

理想 N 点三角求和需要再计入 alias。令 $n=N/\gcd(N,3)$，且 $n>2M$。在局部变量 $z=e^{3i\psi}$ 中，这些点等价于 n 个均匀单位根（可能重复），因此保留系数是

$$
e_j^{[N]}=\sum_{l\in\mathbb Z}e_{j+ln},\qquad |j|\le M.
\tag{12}
$$

这是有限几何级数的正交和，直接证明了式 (12)。纯支撑多项式 (5) 本身无 alias。背景 alias 的导数总量至多

$$
\mathcal A_{M,N}\le
(1+3M)\sum_{|k|\ge n-M}|e_k|.
\tag{13}
$$

每个被折入的高下标属于唯一保留余数类，所以这里没有漏掉重复因子。若 $b<1/7$，则由 (9) 丢掉阶乘并取几何尾可得

$$
\mathcal A_{M,N}\le
\frac{343}{144}(1+3M)\,7^{-(n-M)}.
\tag{14}
$$

故 (11) 中把 $\mathcal T_M$ 换成 $\mathcal T_M+\mathcal A_{M,N}$，就同时覆盖精确 N 点入口。

当前参考输入严格按 binary64 的 `0.1` 解释：

$$
q_*={3602879701896397\over36028797018963968},\qquad
w={3602879701896397\over4503599627370496},\quad b=w/6.
\tag{15}
$$

它满足 $b<1/7$、$1-w>19/100$。当前 initial 使用 $N=\max(2048,128M)$，不应和内部 RHS 的 N512/N1024 混为一个节点数。对本表，(14) 全部严格小于 $10^{-100}$。以这个保守 alias 上界代入 (11)，得到严格安全的十进上界：

| M | initial 的 N | 全角相对 G 误差上界 |
|---|---:|---:|
| 14 | 2048 | $5.291\cdot10^{-23}$ |
| 15 | 2048 | $4.700\cdot10^{-25}$ |
| 22 | 2816 | $4.086\cdot10^{-40}$ |

完整 Fraction 计算实际 **8153a2 自然 exit0**，脚本为
[78718-geometry-pure-support-inlet-tail.py](../scripts/78718-geometry-pure-support-inlet-tail.py)，报告为
[2026-11-10-78718-geometry-pure-support-inlet-tail.json](../notes/2026-11-10-78718-geometry-pure-support-inlet-tail.json)。证明是 (9)–(15) 的有理不等式，脚本把同一有限算术直接求值；没有读候选数组、运行 BVP 或调用尾。

**范围。** 表中精确 N 点求和没有包含原 binary `sin/cos`、弧长求逆和浮点投影的舍入；R90 已明确这类误差与 FFT 的关系。表也没有声称当前实际 M15 支撑参数正好为 (15) 的纯单模。故不能把它搬到新 CP 或实际 `prefix-base`；那些仍使用 R84 的实际系数公式或其 Cartesian 首 jet 版本。它证明的是：纯单模/参考 warp 本身的有限模几何尾不可能解释当前约 $10^{-9}$ 的入口量级。

## 5. 固定弧长的完整参数 Hessian

对参数方向 $d=(d_j)$，定义

$$
f_d(\phi)=\sum_j d_j\cos(k_j\phi),\qquad
g_d(\phi)=-\sum_j\frac{d_j}{k_j}\sin(k_j\phi),
$$
$$
S_d(\phi)=D A_c[d]=
\sum_j\frac{1-k_j^2}{k_j}d_j\sin(k_j\phi).
\tag{16}
$$

在固定材料角 u 下，$A_c(\phi)=u$ 给
$D\phi[d]=-S_d/\rho_c$。在固定正常角求导 (2) 并加入移动角项，得到

$$
\boxed{D\Gamma_c[d](u)=f_d(\phi)e_r(\phi)+g_d(\phi)e_\theta(\phi).}
\tag{17}
$$

其中切向项是 $f_d'-S_d=g_d$。再注意

$$
\partial_\phi(f_d e_r+g_d e_\theta)
=(f_d'-g_d)e_r+(f_d+g_d')e_\theta
=S_d e_r.
$$

式 (17) 没有别的直接参数依赖，因此对另一方向 e 再求导即得

$$
\boxed{
D^2\Gamma_c[d,e](u)
=-\frac{S_d(\phi)S_e(\phi)}{\rho_c(\phi)}e_r(\phi),
\qquad \phi=A_c^{-1}(u).}
\tag{18}
$$

公式对 d、e 对称，且是在真正固定弧长 u 下求导；没有把正常角固定的导数误当成它。它与当前 `PlanarSupportCore.parameter_derivatives` 的一阶公式一致。

## 6. 真正的 Taylor 积分余项及二阶入口尾

取一般参考 $c^*$，令 $c=c^*+d$，并假设线段 $c_t=c^*+td$ 全部具有正 $\rho_{c_t}$。例如两端均有相同正下界 $r_*$ 时，因 $\rho_{c_t}(\phi)$ 对 t 为仿射函数，这一假设自动成立。固定入口图 $u=A_{c^*}(\psi)$，记 $\phi_t=A_{c_t}^{-1}(u)$。

由完整二阶 Taylor 积分式和 (18)，准确地有

$$
\Gamma_c(A_{c^*}(\psi))=
\gamma_{c^*}(\psi)+f_d(\psi)e_r(\psi)+g_d(\psi)e_\theta(\psi)
+\mathcal R_d(\psi),
\tag{19}
$$

$$
\boxed{
\mathcal R_d(\psi)=
-\int_0^1(1-t)\frac{S_d(\phi_t)^2}{\rho_{c_t}(\phi_t)}
e_r(\phi_t)\,dt.}
\tag{20}
$$

这不是只得到形式二阶 jet：式 (20) 是有限参数变化的准确余项。若参考和 d 的所有支撑频率都不超过 M，则 (19) 的前三项全部在圆柱 M 空间内，未表示的支撑曲线部分恰为 $(I-P_M)\mathcal R_d$。

给出可直接核的 $C^1$ 余项界。假设所有 $t,\phi$ 上有
$\rho_{c_t}\ge r_*>0$、$|\partial_\phi\rho_{c_t}|\le B_*$，并置
$R_*\ge\|\rho_{c^*}\|_\infty$ 以及

$$
A_0=\sum_j\left|{1-k_j^2\over k_j}d_j\right|,
\qquad A_1=\sum_j|(1-k_j^2)d_j|.
$$

则

$$
\|\mathcal R_d\|_\infty\le\frac{A_0^2}{2r_*},
\tag{21}
$$

$$
\boxed{
\|\partial_\psi\mathcal R_d\|_\infty
\le\frac{R_*}{2r_*^2}
\left[2A_0A_1+A_0^2\left(1+\frac{B_*}{r_*}\right)\right].}
\tag{22}
$$

证明：(21) 直接由 (20) 积分。由材料角恒等式，
$\partial_\psi\phi_t=\rho_{c^*}(\psi)/\rho_{c_t}(\phi_t)$。
对 $S_d^2\rho_{c_t}^{-1}e_r$ 求 $\phi$ 导数，其范数至多
$2A_0A_1/r_*+A_0^2B_*/r_*^2+A_0^2/r_*$。
再乘 $R_*/r_*$、积分 $\int_0^1(1-t)dt=1/2$，即 (22)。

圆柱复 Fourier 投影与物理 $\psi$ 导数可交换：它只保留物理频率 $1+3j$ 的指定集合，而求导乘以 $i(1+3j)$。每个 Fourier 系数的绝对值不大于函数上确界，故

$$
\|\partial_\psi(I-P_M)\mathcal R_d\|_\infty
\le(2M+2)\|\partial_\psi\mathcal R_d\|_\infty.
\tag{23}
$$

这里在求导后的奇偶类上使用相同频率集合的复投影；未把导数后的向量强制投回原来的偶径向/奇切向类。式 (21)–(23) 在固定 M 和正曲率半径邻域内给出真正的二阶小量。

另一方面，(18) 也解释了为什么实际尾可以比纯 round 尾慢。在纯参考下，Hessian 含因子 $1/(1-w\cos3\psi)$。令

$$
r=\frac{w}{1+\sqrt{1-w^2}}\in(0,1),
$$

几何级数直接给

$$
\frac1{1-w\cos\theta}
=\frac1{\sqrt{1-w^2}}
\left(1+2\sum_{j\ge1}r^j\cos j\theta\right).
\tag{24}
$$

因 $w=2r/(1+r^2)$，将右边通分即可验证。在理想十进 $w=4/5$ 时 r 恰为 $1/2$；实际 binary w 的 r 只是非常接近 $1/2$，不冒称精确相等。除非分子消去这些极点，Hessian 的高模尾具有这种几何尺度，而不是第3节的阶乘尺度。本文不从二阶首项推断任何实际新 CP 的全余项大小；完整余项已由 (20) 指定。

## 7. 实际入口的准确分解与后续坐标用途

对一般参考 $c^*$，设 $B_*(\psi)=e^{iA_{c^*}(\psi)}$。若仍采用当前的“未截 round 背景加有限扰动”表示，则 (19) 准确推出

$$
F_M-\Gamma_c=(I-P_M)B_*-(I-P_M)\mathcal R_d.
\tag{25}
$$

因此可诚实陈述的是：**已知背景尾，加上二阶参数余项**。不能仅把参考 warp 换成某个多谐波支撑 $c^*$ 就删去第一项；一般高谐波 $B_*$ 的尾未必像纯单模表中那样小。

若另把入口表示的背景直接锚到有限曲线 $\gamma_{c^*}(\psi)$，则第一项不存在，入口近似与准确曲线的导数差至多 (23)。由 (3)，如该差上界为 $\varepsilon$，相对 G 误差至多

$$
\frac{2\varepsilon}{\min\rho_{c^*}}
+\frac{\varepsilon^2}{(\min\rho_{c^*})^2}.
\tag{26}
$$

这给一个可用于后续固定参考重求的二阶坐标/表示工具。扩展到内部时仍须明确同一个物理材料角、背景和全部链式导数；本稿没有改动活动 M15 或已定后续 W22 源，也没有把坐标改变当作物理参数优化。

当前实际 callback 使用 $q=q_{seed}\exp p_0$ 及其余 $p_j$ 的非零支撑修正，不能事先设 $c_{j\ge2}=0$。原 M15 UNSOLVED warm 的 R84 全角上界约 $1.30244\cdot10^{-9}$，正是针对其实际保存系数的结论；本表纯特例没有替换它。最终新的真实 M15 `prefix-base` 到来时，仍应从该图自己的 Cartesian 首 jet 做严格全角检查，再推进它自己的全域、接缝和闭图几何。
