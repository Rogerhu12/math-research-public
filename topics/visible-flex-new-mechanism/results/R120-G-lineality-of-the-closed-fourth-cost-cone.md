# R120：真实第四成本闭凸锥的新增 G 直线方向

日期：2026-11-14。**已证明。** 本稿为纸面推导，不运行新的研究计算。使用 [R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R114](R114-constrained-static-costs-and-real-zero-matrix-words.md)、[R115](R115-static-local-fourth-top-weight-payment-and-unresolved-next-block.md)、[R117](R117-static-weight-one-reduction-and-reciprocal-costs.md)、[R118](R118-static-G-exact-separation-and-nonzero-fourth-cost-quotient.md) 及 [R119](R119-positive-static-cone-and-linear-multipliers.md)。

R118 给了真实商中的非零 $[G]$。本稿进一步证明：在**不预先限制总长、scalar 盒或同一个窄物理区间**的 universal 真成本闭凸锥中，$G$ 也是一个双向直线方向。这支付了 R119 特别保留的混合权正泛函问题；证明依赖真实正缩放及最高权极限，不是直接从单个权一查询的两号推出。

## 1. 有限真实空间、实际集合与闭凸锥

固定 scalar 常值 germ $g$、frame 端口 $I\to I$。采用 R105 固定的 canonical 目标、同右 collar 与零传入历史。记

$$
\mathcal S_g=\{V_B:B\text{ 是实际有限同端口路径， }M_B=T_B=0\},
$$

$$
\mathcal U_4=\operatorname{span}_{\mathbb R}\mathcal S_g,\qquad
\mathcal C_g=\overline{\operatorname{cone}(\mathcal S_g)}
\subset\mathcal U_4.
\tag{1}
$$

$\operatorname{cone}$ 只允许有限非负实组合；这已经是实际有限路径集合的一层松弛。外面的闭包是 R105 有限维真实函数空间的普通向量空间拓扑；任取一个真实基得到的范数都给同一闭包。没有把不完备 word 代表的系数空间当作这个拓扑。

路径的 universal 成本是 R105 的无移动极点延拓。每一条有限真实路径仍须在其许可的物理区间使用，不能在 $\xi+\omega=0$ 附近解释为合法曲面。本稿的 $\mathcal C_g$ 允许不同的有限构造随后各自选择共同物理区间。它不是给任意预先指定窄 $I$、统一控制盒或长度上限自动得到的闭锥。

令

$$
\operatorname{lin}\mathcal C_g=\mathcal C_g\cap(-\mathcal C_g).
$$

它是一个真实线性子空间。R101–R102 给

$$
\mathcal R_8\subseteq\operatorname{lin}\mathcal C_g.
\tag{2}
$$

取有限维对偶中的闭锥

$$
\mathcal C_g^*=\{\lambda:\lambda(V)\ge0
\text{ 对每个 }V\in\mathcal S_g\}.
$$

线性与连续性使这个定义等价于在整个 $\mathcal C_g$ 上非负。因此每个 $\lambda\in\mathcal C_g^*$ 都杀 $\mathcal R_8$。

目标是证明

$$
\boxed{\lambda(G)=0\quad\forall\lambda\in\mathcal C_g^*.}
\tag{3}
$$

R118 与 R105 已保证 $G\in\mathcal U_4$、$G\notin\mathcal R_8$。有限维闭凸锥分离随后把 (3) 变成真正的额外 lineality。

## 2. R119 乘子与真实常态缩放

任取 $\lambda\in\mathcal C_g^*$。按 R119，在包含静态局部值的有限 ambient 商中选线性延拓 $\widetilde\lambda$；存在固定 $\mu\in E_8^*$，使

$$
\widetilde\lambda([\ell_0(S)])-\mu(m_0(S))\ge0
\quad\text{对所有允许常态 }S.
\tag{4}
$$

这里使用全部常态及 R114 的有限正规连接前提。$\mu$ 不随状态变化。本文将先在准确零矩表上消掉它，不把某个局部势代表的额外矩阵线性项误作已消失。

固定 $d$，令

$$
h=H>0,\qquad \omega=(d+k)/H.
$$

R114 的全部八坐标随 $H$ 的缩放为：

| $H$ 次数 | 坐标及准确系数 |
|---:|---|
| $1$ | $p_2=-Hk/2$ |
| $0$ | $p_1=-kd,\quad t_1=(k^2+2kd-1)/8$ |
| $-1$ | $p_0=-k(1+d^2)/(2H),\quad s_1=d(k^2+2kd-1)/(4H)$ |
| $-2$ | $r_1=(1+d^2)(k^2+2kd-1)/(8H^2),\quad s_0=d(d+k)(kd-1)/(4H^2)$ |
| $-3$ | $r_0=(1+d^2)(d+k)(kd-1)/(8H^3)$ |

特别，最高矩阵项只有 $p_2=-Hk/2$。但是仅知道这个表，不足以把混合权 $\lambda$ 直接限制成只看 profile 权一；其余静态成本也必须处理。

R89 给真实整路径变换

$$
h\mapsto Hh,\quad k\mapsto k,\quad\omega\mapsto\omega/H,
\tag{5}
$$

以及完整成本的准确 profile 拉回 $\mathsf P_H=\mathsf P_{H,0}$。它保完整 frame、水平微分关系、零低阶端条件和全部累计历史。$\mathsf P_H$ 在有限真实空间中按整数权作用：

$$
\mathsf P_H X_w=H^wX_w.
\tag{6}
$$

所有 profile 导数、右积分和共同右锚一起变换。式 (6) 不能靠只替换坐标多项式来得到。

## 3. 两个正整数互反表先准确消乘子

固定 $d=0$。记 $\tau=\tau(2)=2\pi/\sqrt5$。在同一 $h=H$ 上定义两个正时长表：

$$
\begin{aligned}
q_+(H)
&=\tau[\ell_0(H,2,2/H)]
+4\tau[\ell_0(H,-1/2,-1/(2H))],\\
q_-(H)
&=\tau[\ell_0(H,-2,-2/H)]
+4\tau[\ell_0(H,1/2,1/(2H))].
\end{aligned}\tag{7}
$$

方括号表示模 $\mathcal R_8$。每个表都由一个 $|k|=2$ 完整圈和两个 $|k|=1/2$ 完整圈组成；后两个圈总时长是 $4\tau$。它们准确满足

$$
m_0(k)+k^2m_0(-1/k)=0,
$$

所以 (4) 中的八个乘子在 (7) 中逐一相消。由此

$$
\boxed{\widetilde\lambda(q_+(H))\ge0,\qquad
\widetilde\lambda(q_-(H))\ge0\quad\forall H>0.}
\tag{8}
$$

这一步没有使用负时间、负圈数或把真倒行当负第四成本。

R114/R117 的真实连接构造还保证这些商值属于
$\mathcal U_4/\mathcal R_8$：取固定零矩桥，使外 bulk 圈数同时乘正整数 $N$，再串联真倒行付 $T=0$。对某实际成本 $V_{\pm,H,N}$，

$$
[V_{\pm,H,N}]/(2N)\longrightarrow q_\pm(H).
\tag{9}
$$

右侧存在于有限真实 ambient 商，且左侧位于闭子空间 $\mathcal U_4/\mathcal R_8$，故右侧也位于其中。于是 (8) 实际不依赖任意 ambient 延拓的选择。

## 4. 配平成本的协变保全部势与连接

下面的恒等式是主证中处理潜在局部势项的关键：

$$
\boxed{q_\pm(H)=\mathsf P_Hq_\pm(1)
\quad\text{于 }\mathcal U_4/\mathcal R_8.}
\tag{10}
$$

为证明它，先对 $H=1$ 固定 (9) 的整条真实路径及全部连接，再应用 R89 的真实变换 (5)。对每个有限 $N$，变换后的完整成本准确是 $\mathsf P_HV_{\pm,1,N}$。对固定的 $H$，变换后的连接仍有限、固定，不随外 $N$ 增加。

R109 给变换前、后的商极限分别是 (9) 的两端。有限维连续线性算子 $\mathsf P_H$ 与该 $N\to\infty$ 极限交换，得到 (10)。

因此，不需要假定所选局部势 $N$ 在单个静态状态上严格协变。它可能变化的矩阵线性势、端口常势和连接成本在上述真实恒等与零矩商极限中都已处理。若先在单状态上直接删除它们，再把 profile 权等同于 $H$ 次数，会留下没有支付的缺口。

## 5. 最高未付权的真实正极限

R115 的完整静态最高 profile 权为 $2$，且这一块的全部原式属于 $\mathcal R_8$。在商中它准确为零。

权一块由 R117 给

$$
(\ell_0)_{+1}=hkF+hk^3G+h^2k^2\omega H_1,
\qquad H_1\in\mathcal R_8.
$$

在 (7) 中 $hkF$ 因矩配平相消。准确计算

$$
2^3+4(-1/2)^3=\frac{15}{2},\qquad
(-2)^3+4(1/2)^3=-\frac{15}{2}.
$$

令 $\kappa=15\tau/2>0$。因此

$$
q_\pm(1)=\pm\kappa[G]+\sum_{w\le0}q_{\pm,w}.
\tag{11}
$$

和式只有有限个真实整数权；没有把低权成本设成零。由 (6)、(10)，

$$
H^{-1}q_\pm(H)
=\pm\kappa[G]+\sum_{w\le0}H^{w-1}q_{\pm,w}
\longrightarrow\pm\kappa[G].
\tag{12}
$$

这是真实正缩放 $H\to+\infty$、再乘正实数 $H^{-1}$ 的有限维极限。局部系数可能出现的 $\log h$ 不在这里被擅自删去：式 (10) 先以完整真实路径证明配平商的协变，随后使用 R105 已证的有限 Laurent 表示。

把 (8) 乘 $H^{-1}>0$ 并取极限，得到

$$
\kappa\lambda(G)\ge0,\qquad-\kappa\lambda(G)\ge0.
$$

这就证明了 (3)，包括任意混合 profile 权的非负泛函。

## 6. 闭凸锥的额外 lineality

对有限维闭凸锥，分离定理给

$$
\mathcal C_g=(\mathcal C_g^*)^*.
$$

由 (3)，$G$ 与 $-G$ 都满足全部 $\lambda\in\mathcal C_g^*$ 的非负不等式，故

$$
\boxed{
\mathcal R_8+\mathbb RG
\subseteq\operatorname{lin}\mathcal C_g.
}
\tag{13}
$$

R118 已证 $G\notin\mathcal R_8$，所以这是严格扩张。结合 R116 的秩下界，

$$
\boxed{
\dim\operatorname{lin}\mathcal C_g
\ge\dim\mathcal R_8+1\ge32.
}
\tag{14}
$$

(13) 只属于闭凸锥。它不证明存在实际有限路径恰好具有成本 $G$ 或 $-G$，不证明某非零实际路径存在成本逆元，也不把实数正组合自动转成整数重复。R118/R117 已给的单查询实际控制比一个闭锥两号更强，但仍不能从 (13) 自动升级成全函数控制。

## 7. 补证：端口与完整仿射作用保持这个闭锥

这个补证进一步说明 (13) 不只对一个人为选取的端口成立。

设 $g_0,g_1$ 为两个 constant scalar germs。取 R70 的实际零矩阵、frame $I\to I$ 桥 $B:g_0\to g_1$。对任一 $X$ 在 $g_1$ 上满足 $M_X=T_X=0$，真实词

$$
B\,X^n\,B^R
$$

在 $g_0$ 上也满足 $M=T=0$。R83 对所有零矩阵段的真实可加性给

$$
V_{BX^nB^R}=2V_B+nV_X.
$$

乘正数 $1/n$ 并取 $n\to\infty$，得到 $V_X\in\mathcal C_{g_0}$。反向同理，所以

$$
\mathcal C_{g_0}=\mathcal C_{g_1}.
\tag{15}
$$

这里没有用实际成本相减；常桥成本通过正归一极限消去。也没有要求 $T_B=0$，因为 $T_{B^R}=-T_B$ 且 $T_X=0$。空间位移自由，不是本算子论证的额外端点约束。

R89 把每个真实成本变成另一个真实成本，只是可能改变 germ。用 (15)，再用连续性和真实逆仿射变换，得到

$$
\mathsf P_{H,d}\mathcal C_g=\mathcal C_g
\quad(H>0,\ d\in\mathbb R).
\tag{16}
$$

故整个有限仿射轨道空间也在 lineality 中：

$$
\boxed{
\mathcal R_8+
\operatorname{span}\{\mathsf P_{H,d}G:H>0,\ d\in\mathbb R\}
\subseteq\operatorname{lin}\mathcal C_g.
}
\tag{17}
$$

R105 的有限 Laurent/多项式表示保证这个 span 有限；本稿没有计算其新维数，也没有把不同仿射轨道值未经核验就称为独立。

## 8. 准确适用范围与下一门

本结论针对 universal 真成本闭凸锥及其所有连续非负泛函。证明用任意大但各自有限的 $H$ 和整数 $N$；没有给它们统一的几何尺寸、总长、控制盒或同一窄物理区间。

对一个预先固定的 $I$，若尚未证明上述所有变换和连接都能在其许可范围内执行，不能直接把 (13)–(17) 移过去。任何实际单圆、多查询或曲面构造仍须先固定所需有限紧控制族，随后选择共同物理区间，并支付真实基准。

因此 R119 的全路径非负门现可进一步加上 $\lambda(G)=0$，甚至消掉 (17) 的整个真实轨道空间；它没有变成所有实际有限成本都可取负的结论。完整 $\mathcal U_4/\mathcal R_8$ 的其余方向、同时可达性、第四 ruling、更高阶与闭面厚度目标仍未支付。
