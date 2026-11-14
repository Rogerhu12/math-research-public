# R155 — 非负平尾传入的正 II 分支及不除 n 的完整表示

**状态：已证明。** 本文证明一个准确解必须遵守的分支条件，给出覆盖该分支的局部表示、准确零尾点适配和完整一阶变化。它不宣称已求得新的闭曲面，也不把一次分支代换或残差降低当成同度量解。当前未收敛实体的符号证据见文末绑定的 metric 诊断。

## 1. 正曲率连通区的定号传递

取固定法向约定和正交切标架，记第二基本形式为
$$
S=\begin{pmatrix}l&m\\m&n\end{pmatrix}.
$$
设 $\Omega$ 连通，$S$ 在 $\Omega$ 及所用边界点连续，并准确满足
$$\det S=ln-m^2=K>0\quad\hbox{于 }\Omega.$$
则 $S$ 在整个 $\Omega$ 上或者处处正定，或者处处负定。如果 $\overline\Omega$ 的某个边界点 $q$ 有非零半正定迹 $S(q)$，则只能是正定分支。

**证明。** 实对称矩阵的两个特征值连续，且乘积 $K$ 为正，所以二者同号且均不为零。也可直接用
$$
(l+n)^2=(l-n)^2+4m^2+4K>0
$$
看出迹不可能为零。连续函数 $\operatorname{tr}S$ 在连通集合上的符号恒定。非零半正定 $S(q)$ 有正迹，连续性给出 $q$ 附近内部点的正迹，因而整个 $\Omega$ 为正定。证毕。

特别地，内部处处 $n>0,l>0$。这是准确解在该开区间内的结论，不是向平尾边界额外强加 $n>0$。边界可以在部分角上有 $n=0$，也可以有完整的零矩阵区。只需要一个边界点的迹非零。若整个边界迹都是零，仅凭该零迹不能选分支：$S=\pm\sqrt K I$ 在 $K\downarrow0$ 时都趋于零。本文不会把这个不充分情形用于当前非零正 Bernstein 尾。

结论与正交切标架变化无关；法向若整体反转，正负结论同时反转。本文始终采用 R128/R132 上半尾的既定法向，不能在不同角或不同径向位置任意翻转法向来绕过结论。

## 2. 当前真实末桥满足这个连通条件

准确 profile 输入为
`notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json`，
SHA256 `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
其最后一片是长度 $L=0.026$ 的 `phase_bridge`，起相位 $p_0=-1.45$，两端相位导数为零，终端命名常数准确为 $-\pi/2$。JSON 中相位小数只是求值表示。R136 的积分定义与源 `fd2d_frozen_ellipse_candidate.py::phase` 给出
$$
p(t)=p_0+\Delta(3t^2-2t^3),\qquad
p_s=\frac{6\Delta}{L}t(1-t),\qquad
\Delta=-\pi/2-p_0<0,
$$
其中 $0\le t\le1$。在整个开片上 $p_s<0$、$-\pi/2<p<p_0$，故 $\cos p>0$。因为 $a_s=\sin p$，
$$a_{ss}=\cos p\,p_s<0,\qquad K=-a_{ss}/a>0.$$
半径的严格正下界 $a\ge4/5$ 已由 R136 支付。

当前物理 $s$ 的末端显示值是 $S=1.4889731783581288$，所有七个外设计 bump 的支撑在 $S-0.02$ 之前结束。因而最后 $0.02$ 上真实 $a_\delta$ 与基准桥完全一致；这里的正 $K$ 不能由当前 $\delta$ 改变。这给出连通开柱
$$\Omega=(S-0.02,S)\times\mathbb S^1.$$
这些位置是实际 reader 的求值记录；证明所用对象是准确积分 profile 和准确紧支撑定义，并不把显示小数的末位当作额外几何假设。

R128/R132 的准确平尾具有
$$
l=\kappa\sin^2u,\qquad m=-\kappa\sin u\cos u,\qquad
n=\kappa\cos^2u,\qquad\kappa\ge0.
$$
所以每一点的 $S$ 都半正定。正 Bernstein 控制若全部非负且至少一个为正，则在 $0<q<1$ 的弯曲区 $\kappa>0$：各 Bernstein 基在该开区间为正，乘子 $630q^4(1-q)^4$ 也为正。当前 16 个控制满足这个条件，因而准确 cut 迹有非零点。第 1 节遂证明：任何按既定法向准确接到这个尾部、并准确实现当前目标度量的连续 II，都必须在整个末 $0.02$ 开柱上正定。

这里没有要求 cut 的 $n$ 处处正，也没有用 $l=(K+m^2)/n$ 去除准确平尾的零角。完整位置、标架和两 jet 接合仍需 R124/R129 等实际条件；本节只是这些条件成立时必遵守的 II 分支。

## 3. 不除 n 的完整正支坐标

令 $d,m$ 独立，定义
$$
h=\sqrt{d^2+4m^2+4K},\qquad
n=\frac{h+d}{2},\qquad l=\frac{h-d}{2}.
\tag{1}
$$
对 $K>0$，有 $h>|d|$，所以 $l,n>0$，且
$$ln-m^2=\frac{h^2-d^2}{4}-m^2=K.$$
反之，任意正定 $S$ 满足 $d=n-l$、$h=n+l>0$，从行列式恒等式立即恢复 (1)。故 (1) 没有遗漏正定 II；它也不对 $m$、主方向或尾部的零 $n$ 作额外限制。

在 $K=0$，同一值公式给出所有半正定秩一或零矩阵。当 $h>0$ 时，包括 $n=0$ 的点，平方根作为 $(d,m,K)$ 的函数都在邻域光滑；这里分母是 $h$，不是 $n$。

对角变量 $\xi$，目标 $K=K(s)$ 与角无关。记 $d_\xi=n_\xi-l_\xi$，则在 $h>0$ 处
$$
h_\xi=\frac{d d_\xi+4m m_\xi}{h},\qquad
Dh=\frac{d\,Dd+4m\,Dm+2\,DK}{h},
\tag{2}
$$
$$
D h_\xi=
\frac{Dd\,d_\xi+d\,D d_\xi+4Dm\,m_\xi+4m\,D m_\xi}{h}
-\frac{h_\xi}{h}Dh.
\tag{3}
$$
这些是完整的参数变化，不遗漏外设计引起的 $DK$。

## 4. 准确平尾与零矩阵点

准确尾迹直接写成
$$
d=\kappa\cos(2u),\qquad m=-\frac{\kappa}{2}\sin(2u),\qquad h=\kappa.
\tag{4}
$$
因此在 $\kappa=0$ 或 $n=0$ 的角上，都可直接用上式和原尾的乘积法则计算值、角 jet 以及尾参数变化，无须通过 (2) 除以零。例：若 $u=U(\xi)$，
$$
\begin{aligned}
n_\xi&=\kappa_\xi\cos^2u-2\kappa\sin u\cos u\,U_\xi,\\
m_\xi&=-\kappa_\xi\sin u\cos u
-\kappa(\cos^2u-\sin^2u)U_\xi,\\
l_\xi&=\kappa_\xi\sin^2u+2\kappa\sin u\cos u\,U_\xi.
\end{aligned}
\tag{5}
$$

对一般 $(d,m,K)\to(0,0,0)$，只能自动断言 (1) 连续，不能断言这个三变量平方根在原点可微。准确尾的特殊公式 (4) 支付其实际边界 jet；内部场和参数的高阶正则仍须按实际表示检查。本文不要求 II 沿径向为 $C^2$，更不因此给原题增添 $C^3$ 或 $C^4$ 曲面条件。原题所需 $C^2$ 曲面的 II 只需连续；最终浸入正则性与接合按实际方程另行支付。

在下面窗口代换中，准确 cut 可直接保留原尾值和原尾参数 jet。对准确尾族，这是代换的恒等迹，而非任意方向上的平方根延拓。若原场连续趋于准确尾迹，则代换差也趋于零，包括全零尾点；所以这种端点处理不会产生值跳。

## 5. 窗混合及其真实 Gauss 缺陷

给定旧三场 $(n_0,m,l_0)$，令 $d=n_0-l_0$、$h_0=n_0+l_0$，而 $h$ 由 (1) 给出。取固定、与角和未知参数无关的径向连续窗 $0\le w\le1$，其非零区置于 $K\ge0$ 的区域。定义
$$
E=\frac w2(h-h_0),\qquad n_*=n_0+E,\quad l_*=l_0+E,\quad m_*=m.
\tag{6}
$$
窗为零的地方完全不求平方根，也可以有负 $K$；窗为一的地方是准确正支。准确 cut 的 (6) 恒有 $E=0$，可直接取原尾。

设 $G_0=n_0l_0-m^2-K$，则准确恒等式为
$$
G_*=(1-w)G_0-\frac{w(1-w)}4(h-h_0)^2.
\tag{7}
$$
**证明。** 新迹是 $h_*=(1-w)h_0+wh$，差 $d$ 不变；利用
$$h_*^2=(1-w)h_0^2+wh^2-w(1-w)(h-h_0)^2$$
并减去 $h^2$ 后除以四即得。证毕。

因此 rim 的 Gauss 缺陷不能沿用 R153 的 $(1-w)G_0$ 缩放；(7) 的额外项必须真实计算。尤其若旧场恰在负定分支，连续窗口不可能在 $K>0$ 内把它无缺陷地翻为正支。这是拓扑定号的同一事实，不是求解障碍的结论：初猜可改变，剩余实际方程继续求解。

## 6. 完整增量 jet 和参数 Jacobian

角向 $E_\xi=w(h_\xi-n_{0,\xi}-l_{0,\xi})/2$。以 $(n_0,m,l_0,K)$ 为值变量，(6) 的梯度是
$$
g_n=\frac w2\left(\frac dh-1\right),\quad
g_m=\frac{2wm}{h},\quad
g_l=\frac w2\left(-\frac dh-1\right),\quad g_K=\frac wh.
\tag{8}
$$
令
$$
\begin{aligned}
b_n&=\frac w2\left(\frac{d_\xi}{h}-\frac{h_\xi d}{h^2}\right),
&b_l&=-b_n,\\
b_m&=2w\left(\frac{m_\xi}{h}-\frac{h_\xi m}{h^2}\right),
&b_K&=-\frac{w h_\xi}{h^2}.
\end{aligned}
\tag{9}
$$
则全部方向满足
$$DE=g_nDn_0+g_mDm+g_lDl_0+g_KDK,$$
$$
DE_\xi=b_nDn_0+b_mDm+b_lDl_0+b_KDK
+g_nDn_{0,\xi}+g_mDm_\xi+g_lDl_{0,\xi}.
\tag{10}
$$
这包括径向有限元值、角 Fourier jet、尾参数、中央参数及 profile 参数的所有列。若改用依赖未知参数的窗，须另外加入 $Dw(h-h_0)/2$ 和 $Dw(h_\xi-h_{0,\xi})/2$；本次 helper 明确使用固定窗，不含这类额外自由度。

## 7. 积分 Codazzi 不要求 K 的额外径向导数

固定物理角的正交 Codazzi 方程为
$$
n_s=\frac1a m_u+c(l-n),\qquad
m_s=\frac1a l_u-2cm,\qquad c=a_s/a.
\tag{11}
$$
直接对 (1) 作径向微分会显式引入 $K_s$。当前真实积分实现不必这样做：$n,m$ 的左右端值就是实际值，右侧只需要角导数及 $a,c$。这是对同一 (11) 的积分，而不是删除了径向质量项。

若固定计算角满足 $u=U(s,\xi)$，记
$$v=U_s/U_\xi,\qquad b^{-1}=1/(aU_\xi).$$
则右端分别为
$$
F_n=v n_\xi+b^{-1}m_\xi+c(l-n),\qquad
F_m=v m_\xi+b^{-1}l_\xi-2cm.
\tag{12}
$$
(6) 的变化准确为
$$\Delta F_n=vE_\xi,\qquad\Delta F_m=b^{-1}E_\xi.$$
因此在长度 $\Delta s$ 的格上，若 $Q$ 表示同一实际径向平均求积，实际残差增量必须是
$$
\Delta C_n=\frac{E_R-E_L}{\Delta s}-Q(vE_\xi),\qquad
\Delta C_m=-Q(b^{-1}E_\xi).
\tag{13}
$$
其中 $c$ 项因 $\Delta l=\Delta n$ 准确消去。窗的径向变化已包含在两个准确端点的 $E$ 之差中；不需要另写 $E_s$。完整 Jacobian 对 (13) 逐项微分，并在 $v,b^{-1}$ 随参数改变时包含其变化。若 atlas 固定而仅 $a$ 变，仍必须付 $D(b^{-1})$。

在连续积分版本，(13) 把 $Q$ 换成准确平均积分。若原字段有足够的内部角正则与可积右端，(11) 的积分等价关系并不要求 $K_s$ 或 II 的径向二阶导数；在零尾点用第 4 节准确边界值。这不自动证明任意有限字段满足 Codazzi，也不替代 R129 的真实残差和接合条件。R152 对原 affine lifting 的准确积分不能直接套给这个新增非线性 $E$，必须在选定真实求积上重新计算它和它的全部变化。

## 8. 正支中的精确曲率域

令 $R=\sqrt{d^2+4m^2}$。正支的主曲率为
$$\lambda_\pm=\frac{\sqrt{R^2+4K}\pm R}{2}.$$
对 $C>0,K\ge0$，准确等价关系是
$$
\lambda_+\le C
\quad\Longleftrightarrow\quad
K\le C^2\ \hbox{且}\ R\le C-K/C.
\tag{14}
$$
证明只需把 $\sqrt{R^2+4K}\le2C-R$ 两边平方；右边在所列域内至少为 $C>0$，没有引入伪根。故曲率约束在 $(d,2m)$ 平面是明确圆盘。可据此设计有界初猜，但投影后的角、径向方程必须重新计算；(14) 不是 Codazzi 或全局 reach 的证明。

## 9. 实际旧字段的准确反例范围

`notes/2026-11-12-fd2d-metric-gauss14-late-node118.md` 第 3 节直接用原二进制系数的有理和证明，在真实两格
$$[s_{117},s_{119}]=[1.4689731783581288,1.4759731783581287]$$
内，保存字段每个径向位置都满足
$$n(s,0)<-1/16,\qquad n(s,\pi/6)>1/40.$$
各角值的径向部分是准确 P1 凸组合，尾的附加 $n$ 项非负；所以这不是径向或角网格外推。角函数连续，在每个这样的角圈上必有 $n=0$；第 2 节的 $K>0$ 遂给
$$G=nl-m^2-K=-m^2-K<0.$$
它既违背正确分支，也不可能是准确 Gauss 场。证据只排除这份未收敛保存字段，不排除同一物理目标或新设计的解，亦无须再加密该同一字段来重复验证准确符号事实。

诊断主输入 SHA256 为 `9bebfd806d5bb014f0aca395c3424baeadba9907b92e7692099631f3d2d7d786`；诊断说明 SHA256 为 `86b2c04afc63cbf6637c198f669bcaf3f50e5a3115845f40a5b2521561426060`；对应报告 SHA256 为 `6fd1157abaa19f65e3b72beae8995059fc5ab020229230d9c269aa289d11135f`。其求解、有限谱诊断和准确有理证据在该独立闭组中分开记录。

## 10. 可直接消费的代码和实际执行

`scripts/fd2d_gc_positive_trace_branch.py` 实现 (6)、(8)–(10)，数组末轴顺序为 $(n,m,l)$。主要 API：

- `positive_trace_delta(values, angular, K, weight, exact_tail_mask=...)` 返回 $E,E_\xi$、实际字段与全部偏导。
- `trace_delta_direction` 同时处理所有参数方向；`trace_delta_state_columns` 给局部 Fourier 列。
- `exact_rank_one_tail_trace` 直接实现 (5)，保留 $\kappa=0$ 与 $n=0$。
- `positive_branch_curvature_domain` 计算 (14)，明确只是有限输入求值，不冒连续证书。

`exact_tail_mask` 必须由调用方绑定准确平尾值及参数 jet；它只在 $K=0$ 允许，并令所有增量与增量方向为零。一般活跃点没有人为的正 $n$ 或正 $h$ 下界；只有真正除法所需 $h>0$。未声明准确尾迹的全零点不会被代码静默填成可微平方根。

helper SHA256 为 `03fed0c9e4660caf7496098c36ddde1cf06fc89a8db649e8b23c8eaebd5097bb`。实际小检查使用独立旋转生成的正定矩阵、非零秩一和全零尾点、负 $K$ 非活跃域，以及 48 点六个完整值/角 jet/metric 参数方向。执行 session **30539**，初始 chunk **ee9b65**，完成 chunk **c344b5**，自然 exit **0**。$E$ 的中心差分误差最大 $2.965\times10^{-10}$，$E_\xi$ 为 $2.590\times10^{-10}$，窗口 Gauss 恒等式误差 $2.221\times10^{-15}$。这只验证实际有限实现与已证公式一致，不替代数学证明或后续真实 BVP。

完整有限报告为 `notes/2026-11-12-fd2d-positive-trace-branch-check-01.json`；本组没有运行新的 BVP、修改主活动源或公共索引。
