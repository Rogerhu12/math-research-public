# R574：准确非线性高度方程与核心 shooting 的积分横截性

日期：2026-11-26。状态：已证明的准确非线性接口、有限差边界身份及必要幅度条件；没有宣称非线性解或完成主门。

本文给出 [R571](../results/R571-milder-phase-tail-flat-kernel-and-core-shooting-zero.md)
输入的一个准确非线性接口，以及相位 shooting 导数与该接口线性核的准确积分关系。
它不声称已解非线性方程，也不把有限角谱、有限节点或局部 developing 当成完整闭面。

## 1. 固定径向端点、相位基准和真实连接头

采用当前计算入口的固定数值
$$
r_c=0.22,\quad r_0=0.30,\quad R=0.38,\quad
\ell=0.2,\quad A_w=0.8,\quad \alpha=0.55,\quad\beta=1.1,\quad\lambda=1.
$$
为免把场的径向分量与斜率幅值混淆，后者写作 $A_w$。定义
$$
u=\frac{\ell}{r-r_c},\qquad
w_\varphi(r)=A_w\exp[-u(2-\sin(u+\varphi))],
$$
$$
b(r)=\begin{cases}
0,&r\le r_0,\\
\lambda\dfrac{t^\beta}{(1-t^2)^\alpha},\quad t=\dfrac{r-r_0}{R-r_0},&r_0<r<R,
\end{cases}
\qquad W_\varphi=w_\varphi+b. \tag{1}
$$
相位改变时，$r_c,r_0,R,b$ 都保持固定；数值传递所用的 $\alpha_{17}(\varphi)$
是归一截面，不是物理域端点。背景高度和度量分别为
$$
h_\varphi'=-W_\varphi,\qquad
g_\varphi=E_\varphi\,dr^2+r^2d\theta^2,
\qquad E_\varphi=1+W_\varphi^2. \tag{2}
$$
高度的加法常数是竖直平移规范。尾部可取开平帽高度为零；最终再整体平移上半面使核心高度符合所选闭合方式。

$b$ 在 $r_0$ 的值和一阶导数均为零，所以背景位置是 C2；在该接缝两侧可分别作更高阶微分。
在核心令 $d=R-r$，有
$$
W_\varphi(r)=B d^{-\alpha}(1+o(1)),\qquad
B=\lambda\big((R-r_0)/2\big)^\alpha>0. \tag{3}
$$
这个主项独立于相位。用 $r=R-(R-r_0)x^{1/(1-\alpha)}$，背景准确 C2 接到开放垂直圆柱。

下文先固定相位，省略 $\varphi$ 下标。相位改变同时改变 (2) 的背景高度和度量，属于静态设计；它不冒充同一度量的弯曲。

## 2. 完整的二次 Darboux 方程

设同一度量的待求嵌入竖直坐标为
$$
Z=h+f.
$$
在 $r_c<r<R$ 的光滑部分，Christoffel 项和曲率为
$$
\Gamma^r_{rr}=\frac{E'}{2E},\quad
\Gamma^r_{\theta\theta}=-\frac rE,\quad
\Gamma^\theta_{r\theta}=\frac1r,\qquad
K_g=\frac{W W'}{rE^2}.
$$
因此高度的 Darboux 方程正是
$$
\left(Z_{rr}-\frac{W W'}E Z_r\right)
\left(Z_{\theta\theta}+\frac rE Z_r\right)
-\left(Z_{r\theta}-\frac{Z_\theta}r\right)^2
=\frac{r W W'}E
\left(1-\frac{Z_r^2}E-\frac{Z_\theta^2}{r^2}\right). \tag{4}
$$
代入 $Z=h+f$、$h'=-W$、$h''=-W'$。背景 Hessian 的两个对角项为
$-W'/E$ 和 $-rW/E$，混合项为零。常数项两边相同。全部一次项之差为
$$
-\frac rE\left((Wf_r)_r+\frac{W'}r f_{\theta\theta}\right).
$$
二次项中的 $f_r^2$ 项准确相消，剩下的方程为
$$
L_W f=\mathcal N_W(f),\qquad
L_W f=(Wf_r)_r+\frac{W'}r f_{\theta\theta}, \tag{5}
$$
$$
\boxed{
\mathcal N_W(f)=\frac Er f_{rr}f_{\theta\theta}
+f_rf_{rr}-\frac{WW'}r f_rf_{\theta\theta}
-\frac Er\left(f_{r\theta}-\frac{f_\theta}r\right)^2
+\frac{WW'}{r^2}f_\theta^2.} \tag{6}
$$
这不是丢弃高阶项的 Taylor 式：(5)–(6) 与 (4) 准确等价，非线性恰为二次。
它在 $r_0$ 以连续的 $W,W'$ 和二阶高度 jets 拼接，不需要 $b''$。

对角模 $f=F(r)\cos(j\theta)$，一次方程准确为
$$
L_{W,j}F=(WF')'-\frac{j^2W'}rF=0, \tag{7}
$$
与本次真实尾及连接头的场方程一致。

## 3. Darboux 解到嵌入：哪些部分成立，哪些还要支付

在开帽及其连接体内部定义二维张量
$$
\gamma=g-dZ\otimes dZ.
$$
若 $\gamma$ 正定且所需导数存在，写 $q=|\nabla Z|_g^2$、
$H_{ij}=(\nabla_g^2Z)_{ij}$，逆矩阵恒等式先给
$\gamma^{ij}=g^{ij}+Z^iZ^j/(1-q)$。代入连接公式得
$$
\widetilde\Gamma^k_{ij}-\Gamma^k_{ij}
=-\frac{Z^k}{1-q}H_{ij}.
$$
再代入曲率公式，三阶高度项由 Hessian 的交换公式相消，得到
$$
K_\gamma=
\frac{K_g(1-|\nabla Z|_g^2)
-\det(\nabla_g^2 Z)/\det g}
{(1-|\nabla Z|_g^2)^2}. \tag{8}
$$
故 (4) 令 $\gamma$ 平坦。含整块开平帽的上半面参数域是一个单连通圆盘；若帽上 $Z$ 为常数，帽上的 $\gamma$ 就是原 Euclidean 度量。
从帽上的标准平面坐标出发，平行移动一个正交标架并积分其闭对偶一形式，给出一个单值的平面 developing map $Y$，满足 $dY\cdot dY=\gamma$。
于是 $(Y,Z)$ 的诱导度量准确等于 $g$。
单连通性在这里解决的是 developing 的单值性；单值局部等距映射仍可能有重叠。

在当前 $r_0$ 接缝上，须有同一 C2 高度和相容的一、二 jets；可在两侧分别构造 developing，再用一个平面刚体配准。
若 $\gamma$ 的 C1 jets 连续，则两侧所得位置二 jets 连续，不能独立重置第二侧的材料相位。

核心边界不在 (8) 的正定区域：轴对称背景在那里 $|\nabla h|_g\to1$。
非线性候选还须实际证明 developing 的 C2 极限、边界的闭合正规曲线，以及向开放广义圆柱的二 jets 匹配。
此外仍须证明整个上半面单射、上下块相互分离、完整闭合后的 reach 和宏观像变化。
这些都不由单独的 Darboux 残差、平坦性或无单值障碍推出。

本文未证明任何有限 Fourier 空间中存在非径向解。以有限角谱近似时，二次项产生的高频残差也必须进入完整度量检查；固定有限角阶的非零残差极小值不是准确非径向解。

## 4. 核心归一与准确通量

对任一满足 (7) 的真实角模，记它在 $e_r,e_\theta,e_z$ 方向的场为
$$
V=\mathcal A\cos(j\theta)e_r
-\frac{\mathcal A}{j}\sin(j\theta)e_\theta
+F\cos(j\theta)e_z,
$$
$$
\mathcal A=\frac{W(j^2F-rF')}{j^2-1},\qquad
\mathcal A'=WF'. \tag{9}
$$
这与计算入口的 regular-$x$ 系统准确相同。设在核心有
$C_{\rm core}=F(R)=0$，并把同一真场除以其有符号
$A_{\rm core}=\mathcal A(R)\ne0$，从而 $\mathcal A(R)=1$。
因为 $\mathcal A,F$ 在 regular-$x$ 方程中有有限极限，(9) 等价于
$$
F'=\frac{j^2}rF-\frac{j^2-1}{rW}\mathcal A. \tag{10}
$$
由 (3)、$F(R)=0$ 和这个一阶式，先得 $F=O(d^{1+\alpha})$；再代回得到
$$
F(r)=\frac{j^2-1}{RB(1+\alpha)}d^{1+\alpha}(1+o(1)),\qquad
\boxed{\lim_{r\uparrow R}WF'=-\frac{j^2-1}{R}.} \tag{11}
$$
这里 $WF\to0$。对未满足核心零条件的相邻相位，仍有
$F(r)\to C_{\rm core}$、$F'(r)\to j^2C_{\rm core}/R$；因此不能把每个相位的 $WF'$ 都误称为有限。

## 5. 有限差 Wronskian 先证明，导数随后得到

令 $\varphi_*$ 是一个真实的 $j=2$ 核心零相位。
R571 已有的连续参数 flat 场和 $A_{\rm core}(\varphi_*)\ne0$ 保证在其某邻域可使用有符号核心归一。
写
$$
F_*=F_{\varphi_*},\quad W_*=W_{\varphi_*},\quad
\mathcal A_\varphi(R)=1,\quad c(\varphi)=F_\varphi(R)
=C_{\rm core}/A_{\rm core}.
$$
$c(\varphi_*)=0$。以下公式对任一固定角模的相应 flat 分支同样成立；本次已证明存在的分支是 $j=2$。

令 $\Delta W=W_\varphi-W_*=w_\varphi-w_*$。相位独立的连接头恰好相消。
两个 Sturm 方程给出
$$
L_{*,j}F_\varphi
=-\left((\Delta W F_\varphi')'
-\frac{j^2\Delta W'}r F_\varphi\right).
$$
乘 $F_*$ 并积分。内端所有边界项因 R571 一致全平估计而为零。
核心 Wronskian 可直接用 (9) 算，避免分别把可能发散的通量当成有限：
$$
W_*(F_*F_\varphi'-F_*'F_\varphi)
=\frac{j^2-1}{r}\left(
\mathcal A_*F_\varphi-\frac{W_*}{W_\varphi}F_*\mathcal A_\varphi\right)
\longrightarrow \frac{j^2-1}{R}c(\varphi). \tag{12}
$$
这里 $W_*/W_\varphi\to1$，但因为 $F_*(R)=0$，第二项也可直接用 (11) 控制。
得到准确有限差恒等式
$$
\boxed{
\int_{r_c}^{R}F_*\left((\Delta W F_\varphi')'
-\frac{j^2\Delta W'}rF_\varphi\right)dr
=-\frac{j^2-1}{R}c(\varphi).} \tag{13}
$$
分部积分时额外的 $[F_*\Delta W F_\varphi']$ 也为零：
内端全平，外端 $F_*=O(d^{1+\alpha})$、$\Delta W$ 有界、$F_\varphi'$ 一致有界。
故左侧还准确等于
$$
-\int_{r_c}^{R}\Delta W F_*'F_\varphi'\,dr
-j^2\int_{r_c}^{R}\frac{\Delta W'}rF_*F_\varphi\,dr. \tag{14}
$$

这个证明先只使用连续参数分支，并未假设其相位导数已经存在。
在任意远离端点的紧区间，连续依赖给出 $F_\varphi,F_\varphi'$ 的一致收敛。
内端可用 R571 对紧相位区间一致的 $\exp(-c/(r-r_c)^2)$ 全平界；核心的 (10) 给出一致有界的 $F_\varphi'$。
同时 $\Delta W/(\varphi-\varphi_*)$ 和
$\Delta W'/(\varphi-\varphi_*)$ 在闭径向区间一致趋于
$\dot w_*,\dot w_*'$，其中
$$
\dot w_*=u\cos(u+\varphi_*)w_*.
$$
因此 (14) 可用支配收敛除以 $\varphi-\varphi_*$。
这同时证明 $c$ 在真实零处可微，并给出
$$
D:=\int_{r_c}^{R}F_*(\partial_\varphi L_{\varphi,j})_*F_*\,dr
=-\int_{r_c}^{R}\dot w_*(F_*')^2\,dr
-j^2\int_{r_c}^{R}\frac{\dot w_*'}rF_*^2\,dr
=-\frac{j^2-1}{R}c'(\varphi_*). \tag{15}
$$
特别地，本次 $j=2$、$A_{\rm core}=1$ 时
$$
\boxed{D=-\frac3R\,\partial_\varphi(C_{\rm core}/A_{\rm core})\big|_{\varphi_*}.} \tag{16}
$$

若换成有符号核心幅值 $a\ne1$ 的 $F_*$，积分 $D$ 乘 $a^2$；不能把外口 Cauchy 归一场的积分与 (16) 的右侧混用。
数值 alpha 截面的相位移动和人为 log 尺度在核心有符号归一后全部消掉。
本恒等式没有证明 $D\ne0$；当前 run 的两个相位步长及容差/末端比较只能提供数值证据。

## 6. 二阶源、均值响应和三阶幅度分母

令 $f_1=F(r)\cos(j\theta)$，则 (6) 的准确二阶源仅含均值和 $2j$ 模。定义
$$
P=F'F''-\frac{j^2E}{r}FF''+\frac{j^2WW'}rFF',
$$
$$
Q=-\frac{j^2E}{r}(F'-F/r)^2+\frac{j^2WW'}{r^2}F^2.
$$
有
$$
\mathcal N_W(f_1)=N_0+N_{2j}\cos(2j\theta),\qquad
N_0=(P+Q)/2,\quad N_{2j}=(P-Q)/2. \tag{17}
$$
若 $f=\varepsilon f_1+\varepsilon^2 f_2+\cdots$，二阶方程为
$$
(W F_0')'=N_0,\qquad
L_{W,2j}F_{2j}=N_{2j}. \tag{18}
$$
第一式的帽上零规范响应有明确表达
$$
F_0(r)=\int_{r_c}^{r}\frac1{W(t)}
\left(\int_{r_c}^{t}N_0(v)\,dv\right)dt. \tag{19}
$$
R571 场的平方衰减压过 $1/W$ 及其任意固定阶导数，所以 (19) 在帽端全平。
核心 (11) 给 $F'=O(d^\alpha)$、$F''=O(d^{\alpha-1})$，(17) 中各项均有界，故内层积分有有限极限，$F_0'=O(d^\alpha)$。
令 $m=(1-\alpha)^{-1}=20/9$，则 $d=(R-r_0)x^m$，
$F_{0,x}=O(x^{2m-2})$、$F_{0,xx}=O(x^{2m-3})$。
因此 $F_0$ 在 regular-$x$ 核心有常数极限且一、二 $x$ 导数趋于零；该常数可由上半面的竖直平移规范处理。

第二式是真实的受迫 $j=4$ 问题。只知道一个 $j=4$ 齐次 shooting 值非零，还不能跳过受迫 flat 解的存在、估计和核心匹配；这些必须在后继实际解算中支付。
核心曲线的 $4,6,\ldots$ 次谐波须允许作为未知量，不能只调一个 $\varphi$ 又把整个核心预定为一条指定椭圆。

形式上，在旋转 $\theta\mapsto\theta+\pi/2$ 对应
$\varepsilon\mapsto-\varepsilon$ 的分支上，可取
$\varphi=\varphi_*+\varepsilon^2\mu+\cdots$。
设 $\mathcal B$ 是 (6) 的极化双线性形式，且二阶问题已真正解出。
三阶 $j=2$ 方程右侧为
$[2\mathcal B(f_1,f_2)]_2-\mu(\partial_\varphi L_2)_*F$。
若三阶场在帽端全平且核心非均值高度为零，Green 恒等式的边界项为零，必要幅度条件是
$$
\mu D=\int_{r_c}^{R}F\,[2\mathcal B(f_1,f_2)]_2\,dr. \tag{20}
$$
所以 (16) 给出的正是这个条件的分母。本文只证明该准确接口和必要条件，未由有限模响应推得全频率有界逆，也未证明该形式级数收敛。

## 7. 下一实际门的边界

后继必须结合具体输入原运行的核心归一 C2 代价、相位根的容差/末端稳定性和有限高模响应。
若它们支持继续，下一输入应真正求受迫二阶响应和完整非线性 BVP，并允许核心高模随解生成。
若核心归一场仍极硬，应改更慢相位或联合设计末段振荡及连接头；不能靠任意缩小幅值把宏观变化问题藏掉。

无论采用哪种求解器，最终候选仍须先固定同一张 $g$，再作空间/角向精化；相位设计改变背景不是这个精化。
本文尚未给出本课题完成所需的有限非线性闭面。
