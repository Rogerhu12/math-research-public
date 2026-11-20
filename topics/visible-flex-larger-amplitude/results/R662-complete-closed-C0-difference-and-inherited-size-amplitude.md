# R662：完整闭合场的连续 C0 差，以及直径和整像幅度的传递

2026-11-20，Astra-larger-resume-24b2ab87-20261120；推导及新源由 recover_evidence 完成。

**状态：完整证明及一次全部 922 胞的向外计算均已完成。** 对同一 S/R、同一准确节点和同一解析闭合配方的两个完整场，可以直接对系数差作 Bernstein 包围。既不需要角网格，也不需要重新扫描旧场的直径或整像见证距离。

本条以 [R658](R658-complete-body-diameter-and-fixed-grip.md)、[R659](R659-complete-image-held-amplitude-for-the-same-closed-candidate.md) 已证的 6077 场为基场，以真实 0241 场为新场，得到

$$d_H(S^{0241}_0,S^{6077}_0)\le\varepsilon\le0.028621856.\tag{1}$$

这里的集合包括所有 922 径向胞、全角、镜像半面和两个平帽。由此严格传得

$$D_{0241}\le4.164062712,\qquad
\delta_{{\rm hold},0241}\ge0.914520539,\qquad
{\delta_{{\rm hold},0241}\over D_{0241}}>0.21962>0.2.\tag{2}$$

本条只使用完整像与位置。结论不以尚未支付的闭嵌入为前提，也不把 C0 稳定性当作曲率、reach、等距误差或两个场之间的等距关系。

## 1. 准确的两个场，以及共同径向定义

两个输入如下；名称只是方便复算，数学对象由完整字节和下述准确解释确定。

| 场 | 完整 bundle | SHA256 |
|---|---|---|
| 已有全域证书的基场 | curvature-qp-arbitrary-def1-six-step.npz | 607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941 |
| 本次新场 | curvature-qp-physical-h2-next-six.npz | 0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023 |

两者均有 J=923 个径向节点、M=160 个偶角模。原 mesh、a_stages、radius、width 和 fixed_core_first3 相同；并非把两个不同标量模型强行配对。准确节点由同一原报告给出

$$s_i=\alpha_i S+\beta_i,\qquad 0\le i\le922,$$

其中所有 $\alpha_i,\beta_i$ 是有理数，$s_0=0,s_{922}=S$。同一真实 S/R 所用有理盒为

$$S\in\left[
{296412483966226858607817\over125000000000000000000000},
{2371299871729836522645511\over1000000000000000000000000}
\right],\tag{3}$$

$$R\in\left[
{564734175386577761774707\over1000000000000000000000000},
{282367087693515366508543\over500000000000000000000000}
\right].\tag{4}$$

准确 lift 宽度取原 binary64 值所代表的有理数

$$w={3602879701896397\over72057594037927936}.$$

本条对盒内的共同 S/R 一致成立；不会让两个场分别选盒内不同 S/R 以获得较小差。每胞准确宽度直接用

$$h_i=(\alpha_{i+1}-\alpha_i)S+(\beta_{i+1}-\beta_i),$$

而非把已舍入的两个节点当作准确实数后相减。

所有自由 q 两jet 系数和 H 都取对应 binary64 数的准确实值。两端的原仿射约束重新解释为准确实线性约束：特别是核心 $\nu_j=2j$、$c_j=R_j(0)$ 对应

$$T_j(0)=-\nu_jc_j.\tag{5}$$

因此核心派生 T 的准确差是 $-\nu_j\Delta c_j$。源码直接按此式重建，未将两个分别舍入后的已存 T 槽相减。固定核心前三模、其他固定零槽、核心单位 R 常项及单位 Z 导数、末端完整零两jet都沿原接口保留；全部自由模均被纳入。

## 2. 全部解析 lift 的精确差分公式

在相同 $\phi$ 的径向/切向正交架中写有限角部分

$$q_R=R_0+\sum_{j=1}^M R_j\cos(\nu_j\phi),\quad
q_T=\sum_{j=1}^M T_j\sin(\nu_j\phi),\quad
q_Z=Z_0+\sum_{j=1}^M Z_j\cos(\nu_j\phi).\tag{6}$$

每个径向系数是原胞上的准确 quintic Hermite 多项式。按 [R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)，两个上半场分别为

$$F_a=q_a+f e_r(\delta_a)+\chi H_a e_z,\qquad a=0,1,\tag{7}$$

其中

$$\delta_a(\phi)=\sum_{j=1}^M{1-\nu_j^2\over\nu_j}c_{a,j}\sin(\nu_j\phi),
\quad e_r(v)=(\cos v,\sin v,0),\tag{8}$$

$$\chi(s)=0\ (s\le S-w),\qquad
\chi(s)=10t^3-15t^4+6t^5\ (t=(s-S+w)/w\in[0,1]),$$

$$f(s)=\chi(s)(R+S-s).\tag{9}$$

共同 S/R/w 使 f 和 $\chi$ 完全相同。即使核心变化导致材料角图 $\Theta_a=\phi+\delta_a$ 变化，$\phi$ 仍参数化完整几何圆周；下面只构造两个像集合之间的配对，不要求它是同一材料坐标配对。

因为单位圆参数曲线的导数范数恒为1，微积分基本定理给出对所有实数 u,v 的准确不等式

$$|e_r(u)-e_r(v)|\le|u-v|.\tag{10}$$

令

$$L_\delta=\sum_{j=1}^M\left|{1-\nu_j^2\over\nu_j}\Delta c_j\right|.$$

由 $|\sin|\le1$ 及(10)，完整非多项式 lift 满足

$$|f(e_r(\delta_1)-e_r(\delta_0))|\le |f|L_\delta.\tag{11}$$

这一步保留全部核心角相位及其完整 sine/cosine。没有把 $e_r(\delta)$ 截成有限 Fourier 级数，也没有忽略高次交叉项；(10)直接覆盖它们。

## 3. 在共同 Bernstein 控制点上先合并高度

记 $\Delta=({\rm 新})-({\rm 基})$。在每个原胞，先由准确差两jet构造 $\Delta q$，不先分别形成两个大区间再相减。对端点差 $y_0,u_0,a_0,y_1,u_1,a_1$ 和准确宽度 h，quintic 的六个控制点为

$$\begin{aligned}
b_0&=y_0,&b_1&=y_0+hu_0/5,&b_2&=y_0+2hu_0/5+h^2a_0/20,\\
b_3&=y_1-2hu_1/5+h^2a_1/20,&b_4&=y_1-hu_1/5,&b_5&=y_1.
\end{aligned}\tag{12}$$

所有式子逐步向外。若胞跨 $S-w$，按该准确断点用 de Casteljau 分开；相同方法把 $\chi$ 和 f 限制到相同 piece。然后升到共同 degree6，使用(12)的线性性和 Bernstein 升阶恒等式，得到准确多项式

$$P=\Delta q+\chi\Delta H e_z=\sum_{\ell=0}^6 B^6_\ell(u)P_\ell(\phi).\tag{13}$$

具体地，先在每个控制点把 $\Delta Z_{0,\ell}+\chi_\ell\Delta H$ 合成一个区间，再取绝对值。这样保留原 q 高度与闭合 lift 高度之间的真实抵消。

设控制点 $\ell$ 的三个有限角分量系数分别为 $r_{\ell j},t_{\ell j},z_{\ell j}$，其中 z 的常项已经完成上述合并。定义

$$A_{\ell R}=\sum_{j=0}^M|r_{\ell j}|,\quad
A_{\ell T}=\sum_{j=1}^M|t_{\ell j}|,\quad
A_{\ell Z}=\sum_{j=0}^M|z_{\ell j}|,\tag{14}$$

$$\Gamma=\max_{0\le\ell\le6}
\sqrt{A_{\ell R}^2+A_{\ell T}^2+A_{\ell Z}^2}.$$

逐项 $|\sin|,|\cos|\le1$ 先给每个 $|P_\ell(\phi)|\le\Gamma$。随后由 $B^6_\ell(u)\ge0$ 且 $\sum_\ell B^6_\ell(u)=1$，三角不等式给出

$$|P(u,\phi)|\le\sum_\ell B^6_\ell(u)|P_\ell(\phi)|\le\Gamma.\tag{15}$$

这是全径向、全角的界，没有任何未付的采样间余项。不同角分量在固定 $\phi$ 的物理架正交，故(14)用普通 Euclidean 范数正确；不需要引用目标度量 a。

同 piece 内 f 的 degree6 控制点给 $f_*\ge\sup|f|$。结合(7)、(11)、(15)，得到每 piece 的完整位置差

$$\sup_{s,\phi}|F_1-F_0|\le\Gamma+f_*L_\delta.\tag{16}$$

下半场由相同水平镜像得到，镜像是等距变换，因此不产生额外因子。

## 4. 两个平帽，以及从点配对到完整 Hausdorff 界

两个场的帽半径 R 相同。对上下帽分别以相同 Cartesian 圆盘点 $(x,y)$ 配对，位置仅相差 $\pm\Delta H$，故帽上的差界正好为 $|\Delta H|$。

带面采用相同 $s,\phi$ 配对，帽采用相同 $(x,y)$ 配对。两种配对在接缝上可以不同：Hausdorff 距离只要求每个像点在另一完整像中有一个近邻，并不要求配对形成全局连续映射。完整带面和完整闭圆盘均在两向配对中被覆盖，因而

$$d_H(S_1,S_0)\le
\max\left\{|\Delta H|,\max_{{\rm 全部胞及piece}}(\Gamma+f_*L_\delta)\right\}
=:\varepsilon.\tag{17}$$

该证明对紧像成立，包括可能自交的紧像；因此没有把未证嵌入偷偷用作(17)的前提。

## 5. 直径、真实见证及核心角图的传递

设基场已有 $D_0\le\overline D_0$，且 $d_H(S_1,S_0)\le\varepsilon$。任取新场两点，各自选基场中距其至多 $\varepsilon$ 的点，用三角不等式即得

$$D_1\le\overline D_0+2\varepsilon.\tag{18}$$

按 [R248](R248-finite-C2-phase-family-and-global-reductions.md)，相位 $\pi/2$ 的真实活动像点可取

$$p_a=R_{\pi/2}F_a(0,0)
=\left(0,1+\sum_{j=1}^M c_{a,j},0\right).\tag{19}$$

所以两个见证的准确距离为

$$\eta=|p_1-p_0|=\left|\sum_j\Delta c_j\right|.\tag{20}$$

此处应先求准确和再取绝对值，不能与 phase 所需的绝对值之和混淆。若基场已证 $\operatorname{dist}(p_0,S_0)\ge L_0$，对任意 $x_1\in S_1$ 选近邻 $x_0\in S_0$，得到

$$|p_1-x_1|\ge |p_0-x_0|-|p_1-p_0|-|x_1-x_0|
\ge L_0-\eta-\varepsilon.$$

于是

$$\delta_{{\rm hold},1}\ge\operatorname{dist}(p_1,S_1)
\ge L_0-\eta-\varepsilon,\qquad
{\delta_{{\rm hold},1}\over D_1}
\ge{L_0-\eta-\varepsilon\over\overline D_0+2\varepsilon},\tag{21}$$

当分子为正时右式是有效的比例下界。

为确认新核心仍有原角图，另用

$$\rho_a=1+\sum_j(1-\nu_j^2)c_{a,j}\cos(\nu_j\phi),\qquad
L_\rho=\sum_j|(1-\nu_j^2)\Delta c_j|,$$

得到 $\inf\rho_1\ge\inf\rho_0-L_\rho$。这不是有限网格上的 rho 检查；它直接覆盖全角。R658 的基场连续下界为 $\rho_0\ge0.1657734$。

式(17)–(21)可以反复用于后继，但必须使用有合法全域证书的基场常数。本文脚本run所调用传递方法的默认D/L/rho常数专门属于 SHA6077 基场，调用这条CLI前必须核base为上述6077；不能把任意bundle换为base后沿用这些证书常数。通用的 Difference.cell 方法仍可计算任意同 S/R 节点场的差；它本身不生成旧场的证书。

## 6. 一次新计算的完整返回

本次完整执行自然结束，覆盖 cell=0,...,921 共922个原胞，耗时 **1.536922203 秒**。它未创建角网格，未采样径向点，径向细分数为0；本节点表恰已包含 lift 断点，因此无需额外拆出跨断点胞。实现仍保留准确拆 piece 的一般分支。

输出中的关键向外界如下。

| 项 | 向外返回 |
|---|---:|
| 完整核心 phase 差 $L_\delta$ 上界 | 0.00005991594384564333 |
| 核心 rho 差 $L_\rho$ 上界 | 0.0010871347347972571 |
| 帽位置差上界 | 0.02858794886657634 |
| 带面全部胞的位置差上界 | 0.02862185524069972 |
| 完整像 Hausdorff 差上界 | 0.02862185524069972 |
| 见证位移 $\eta$ 上界 | 0.0000006045805365741819 |

准确高度差与准确见证位移分别为

$$\Delta H=-{8046792241425\over281474976710656},\qquad
\eta={5987475625582552630237\over9903520314283042199192993792}.\tag{22}$$

最坏为末胞921。其多项式及高度合并部分上界为0.028587948866584785，phase lift 项上界为0.00003390637411493089；二者向外相加得到表中完整上界。无 lift 的全部胞中，最坏为胞893，上界0.026450088646291815。由此也能看出这里的全局界主要由真实帽高度变化决定，而不是角分辨率不足。

用 Fraction 准确比较，以上二进制上界分别小于

$$\varepsilon_*={28621856\over10^9}=0.028621856,
\qquad\eta_*={605\over10^9}=0.000000605.$$

将 R658/R659 已证的准确有理数 $\overline D_0=4.106819$、$L_0=0.943143$ 代入(18)、(21)，得到

$$\overline D_1=4.106819+2\varepsilon_*
={520507839\over125000000}=4.164062712,$$

$$L_1=0.943143-\varepsilon_*-\eta_*
={914520539\over10^9}=0.914520539.\tag{23}$$

准确有理比较给 $L_1/\overline D_1>0.21962$。不先按短小数取整而直接传播完整向外输出，源码还给出

$$D_1\le4.164062710481401,\quad
\operatorname{dist}(p_1,S_1)\ge0.9145205401787635,\quad
\delta_{{\rm hold},1}/D_1\ge0.21962218241257872.$$

这些较长数字均为同一0241输入，不是不同候选的组件拼接。上述(23)的较短有理数足以完成本条比例结论。

此外 $L_\rho\le0.001087135$，故全角

$$\rho_1\ge0.1657734-0.001087135=0.164686265>0.\tag{24}$$

原半径 $9/20$ 的固定帽盘仍在共同半径 R 内，握持直径为 $9/10$，因此 $\operatorname{diam}H_{\rm grip}/D_1>0.21613$。

## 7. 固定小帽标记的条件预算

若按 R650 附录C及 R658/R659 的共同帽度量配方，在0241的帽内装固定 C² 图，保持边界附近完整零两jet，且竖直改变量绝对值至多 $h=1/1000$，则完整直径至多再增加 $2h$：

$$D_{1,{\rm marked}}\le4.166062712.\tag{25}$$

活动像不变，$p_{1,z}=0$。新场准确 $H_1$ 是 binary64 数1.879857759511436代表的实值，故任何标记帽点到 $p_1$ 的距离至少 $H_1-h>1.878>L_1$。侧面距离仍由(23)控制。因此无需为见证额外损失 h，仍有

$$\delta_{{\rm hold},1,{\rm marked}}\ge L_1,
\qquad {\delta_{{\rm hold},1,{\rm marked}}\over D_{1,{\rm marked}}}>0.21951,
\qquad {\operatorname{diam}H_{\rm grip}\over D_{1,{\rm marked}}}>0.21603.\tag{26}$$

这部分是明确的固定标记尺寸条件。它没有声称已实际接上标记、标记诱导度量仍为旧平帽度量、或已经完成含反射的 Euclidean 非全等证明；这些输入沿各自已登记配方处理。

## 8. 向外算术、完整来源和复算

新的小源为 scripts/resume_20261120/fullclosed_C0_difference_interval.py，完整12520字节，源码 SHA256

f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0。

它只复用 R656 的准确径向方法，以及 f512 区间核；没有初始化 R656 的 FFT/角数据。所有本次位置差的实数加减乘除、平方、平方根和求和逐步向外，准确输入由 Fraction 转为包围区间。相等的准确二进制自由槽可直接给差0。严格性采用 R656 已说明的 IEEE binary64、正确舍入基本运算、非 FTZ 模型；未把普通 NumPy 三角函数或 BLAS 运算当作向外算术。

Bernstein 凸性、有限角系数 l1、完整单位圆 Lipschitz 界和(17)–(21)已付所有连续区间间隙；本次不存在另外隐藏的角或径向余项。

| 依赖/新输出 | SHA256 |
|---|---|
| 同一准确节点报告 fullclosed-hold-warm.json | fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692 |
| R656 几何源 fullclosed_geometry_interval.py | 2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377 |
| 原向外核 parallel_20261117_arclength_interval_positive.py | f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d |
| 本次完整922胞报告 C0-0241-from-6077-full.json | 76bd3e4d41589e006db1a915dbc5084cb8dc415b79786030273a4627b5aba246 |

完整逐胞 raw 只留 scratch；可公开复核的完整算法、准确参数、候选身份、结果和命令均在这里。没有重跑 R658 的全位置半径界或 R659 的全见证距离界。6077 的重建沿 R658/R659，0241 的实际求解重建沿本日 physical-H² 粗 QP 记录。

令 topic 指向本课题，work 为仓库外的重建工作目录，本次命令为：

~~~sh
python "$topic/scripts/resume_20261120/fullclosed_C0_difference_interval.py" \
 --base "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.npz" \
 --candidate "$work/geometry_path/curvature-qp-physical-h2-next-six.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --geometry-source "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --out "$work/recover_evidence/C0-0241-from-6077-full.json"
~~~

对后继只需更换 candidate，并核其仍为相同准确 S/R 节点的原闭合场；基场和基场证书保持6077。若差上界变松，则所得传递也相应变弱，不能把旧候选的较强数值直接沿用。C0 证据至此已完成，导数、嵌入、完整度量和 reach 各自仍按其真正所需数据处理。
