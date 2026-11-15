# R253：同时平移坐标与右锚后，两不交 block 的质心仍阻止例外端芽 ruling

日期：2026-11-15。**已证明，纯纸面结论。** 没有执行新的符号目标、profile 积分、参数搜索或几何计算。

本稿把 [R252](R252-two-further-Gaussian-areas-exclude-the-even-packet-exceptional-family.md) 对现有 R239 双完整 block 圆的结论，推广到例外端芽中的任意实常数平移 $b_0$。证明同时搬移 profile 坐标、左右 collar 和原右锚，并使用两个真实支撑质心。没有只凭平移后某个实部的符号作判断。

来源：[R56 原分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 完整八矩](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R239 所构圆](R239-nonseparable-third-order-circles-paying-four-exceptional-energy-gates.md)、[R248 互补角及完整第四谐波](R248-complete-fourth-harmonics-and-complementary-block-reduction.md)、[R249 Gaussian 真独立性](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)、[R251 参数系数](R251-nonresonant-Gaussian-area-obstruction-and-two-exceptional-curves.md)和 R252。

## 1. 端芽与结论

允许

$$
h_e>0,\qquad \kappa\ne0,\qquad \varepsilon>0,\qquad b_0\in\mathbb R,
$$

并取

$$
H=e^{\varepsilon\sigma^2},\qquad
h=h_eH,\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=b_0+\frac{\kappa}{h}.
\tag{1}
$$

共同 I、profile 圆和全部真实入 history 固定，仍须满足实际物理支 $z=x+\omega\ne0$。不把 (1) 的任意数值参数自动当成已安装的全局闭几何。

**定理。** 对 R239 采用偶微包、两个不交完整 block、R248 已付互补角范围的圆，任何含有 (1) 的真实几何都不能通过允许的二、三阶 homogeneous gauge 完成第四 ruling。结论覆盖全部实 $b_0$ 及全部正 $\varepsilon$。

这里只排这类具体圆与端芽组合，不排任意三矩圆、任意非偶 germ 或 $\kappa=0$。

## 2. 真正同时平移：不产生额外 primitive 常数

记

$$
y=x+b_0,\qquad
\widetilde I=I+b_0,\qquad
\widetilde q(y)=q(y-b_0),\qquad
\widetilde r=r+b_0,
\tag{2}
$$

其中 $r$ 是原右锚，$q=f+ig$。左右 collar 随同坐标平移。对任意原 profile 表达式 $F$，

$$
\int_x^r F(t)\,dt
=\int_y^{\widetilde r}F(v-b_0)\,dv.
\tag{3}
$$

因此所有层数的右 Volterra 原函数都准确搬移，没有换锚误差或附加常数。由于 $b_0$ 不依赖 $\sigma$，

$$
\partial_x=\partial_y,\qquad
\left.\partial_\sigma\right|_x
=\left.\partial_\sigma\right|_y.
$$

R56/R73 中的几何量逐项变为

$$
z=x+\omega=y+\frac{\kappa}{h},\qquad
j=2\varepsilon\kappa\sigma^2,
$$

$$
d=h\omega-k=b_0h+j,\qquad
e=hx+d=hy+j,
\tag{4}
$$

$$
\frac{h_sx+d_s}{h^2}
=\frac{h_sy+j_s}{h^2}.
\tag{5}
$$

$K_0=kz^2-(k^2+1)z/h$、真实 frame、$\alpha_s=h^2T$ 以及所有分子恢复也因此准确写成 $b_0=0$ 的同一公式，profile 为 $\widetilde q$。原物理量

$$
u=\frac h{x+\omega}=\frac h{y+\kappa/h}
$$

没有改变。特别 R56 的 covariant 微分、R73 的真实 $\Psi$、全部累计 history 和积分配对均只被重标，不是被丢弃。

对每个已经固定的 (1) 几何和圆，(2) 是描述同一物理输入的坐标改名，所以不改变其目标度量。不同 $b_0$ 数值配上同一个数值函数 $f(x)$ 时，物理输入可不同；本稿不把这种跨参数变化称为保持同一个目标。

## 3. 三矩、Gaussian 系数与 gauge 空间的准确变换

合法三复矩按三角式变换：

$$
\widetilde I_0=I_0,\qquad
\widetilde I_1=I_1+b_0I_0,\qquad
\widetilde I_2^*=I_2^*+2b_0I_1+b_0^2I_0.
\tag{6}
$$

其中 $I_2^*$ 的 $2(q')^2$ 项不变。因此合法三矩圆在新坐标仍合法。

R252 的三个四次积分满足

$$
\boxed{
\widetilde M_4=M_4,\qquad
\widetilde N_1=N_1,\qquad
\widetilde M_1=M_1+b_0M_4.
}
\tag{7}
$$

变换后不需要 $\widetilde I$ 位于正半轴：R252 的原算子及全部分部积分没有除以 profile 坐标。实际非零分母仍是 (4) 中的 $z$，它没有改变。

在 y 坐标重新表达完整八矩后，R251/R252 的 $a,b,c,d_-,e_-$ 准确沿用。这里没有宣称原 x 坐标的各八矩分量逐个不变；它们按上述算子共轭变换。

偶部 gauge 空间也没有新增自由度。旧坐标的生成函数可写成

$$
h,\quad d=b_0h+j,\quad \frac{1+d^2}{h}.
$$

因为

$$
\frac{1+d^2}{h}
=\frac{1+j^2}{h}+2b_0j+b_0^2h,
$$

其张成恰是

$$
\mathcal W_e
=\operatorname{span}_{\mathbb R}
\left\{h,\ j,\ \frac{1+j^2}{h}\right\}.
\tag{8}
$$

这与 R224/R249 的空间相同。所有真实中心入值及允许 gauge 的偶部范围均保持。

令 $c$ 为 R251 的 $E_{-3}$ 系数。R252 的两条完整面积必要门现在给：

$$
c\ne0
\quad\Longrightarrow\quad M_4(q)=0;
\tag{9}
$$

$$
c=0,\quad N_1(q)=0
\quad\Longrightarrow\quad M_1(q)+b_0M_4(q)=0.
\tag{10}
$$

式 (9)、(10) 仍来自整个原第四 ruling 的真实面积系数。不是将某个单独 profile 积分条件先验地当成其充分性。

## 4. 两个完整 block 的真实质心严格不同

对 R239 的两个未旋转完整 block，分别写

$$
q_{0,j}
=\sum_i(1+i s_{ji})a_{ji}u_{ji},
\qquad s_{ji}\in\{-1,1\},\quad j=1,2.
$$

每个 block 内的微包支撑互不交、实 profile 非零；R239 的偶微包保证 $N_1(q_{0,j})=0$。令

$$
\rho_j(x)=\sum_i a_{ji}^4(u_{ji}''(x))^4.
$$

则 $\rho_j\ge0$，连续紧支撑且不恒零。普通复四次方给

$$
M_{4,j}:=M_4(q_{0,j})=-4\int_I\rho_j<0,
$$

$$
M_{1,j}:=M_1(q_{0,j})=-4\int_Ix\rho_j.
\tag{11}
$$

因此

$$
\mu_j:=\frac{M_{1,j}}{M_{4,j}}
=\frac{\int_Ix\rho_j}{\int_I\rho_j}
\tag{12}
$$

是一个真正正密度的质心，尽管 (11) 的两个四次量带有共同负号。

按左右次序标记两个完整 block 的紧包络为
$[L_1,R_1]$、$[L_2,R_2]$，R235/R239 的放置保留正间隙
$R_1<L_2$。非零连续密度在包络内部有非空正集，故

$$
L_1<\mu_1<R_1<L_2<\mu_2<R_2.
\tag{13}
$$

所以 $\mu_1\ne\mu_2$。这一步只需要两个真实支撑包络不交，不需要对它们的尺度、积分值或对称中心作数值求积。

## 5. 复 $2\times2$ 条件不能由一个平移支付

R239 的最终圆为

$$
q=A_1e^{-i\alpha}q_{0,1}
+A_2e^{-i\beta}q_{0,2},
\qquad
\beta=\frac\pi2-\alpha,\qquad A_1A_2\ne0,
\tag{14}
$$

两 block 支撑互不交。R248 已付

$$
\sin4\alpha\ne0,\qquad \cos4\alpha>\frac12.
\tag{15}
$$

因此 $N_1(q)=0$，而

$$
\operatorname{Re}M_4(q)
=\cos4\alpha\{A_1^4M_{4,1}+A_2^4M_{4,2}\}<0.
\tag{16}
$$

这已排除 $c\ne0$ 的全部参数。

若 $c=0$，设两个真实数

$$
K_j=M_{1,j}+b_0M_{4,j},\qquad j=1,2.
$$

式 (10) 准确为

$$
A_1^4e^{-4i\alpha}K_1
+A_2^4e^{4i\alpha}K_2=0.
\tag{17}
$$

实部与虚部给

$$
\begin{pmatrix}
A_1^4\cos4\alpha&A_2^4\cos4\alpha\\
-A_1^4\sin4\alpha&A_2^4\sin4\alpha
\end{pmatrix}
\begin{pmatrix}K_1\\K_2\end{pmatrix}=0.
\tag{18}
$$

其行列式为
$2A_1^4A_2^4\sin4\alpha\cos4\alpha\ne0$，所以
$K_1=K_2=0$。由 $M_{4,j}\ne0$，这要求

$$
b_0=-\mu_1=-\mu_2,
$$

与 (13) 矛盾。此证明没有假设 $M_1+b_0M_4$ 的实部保持原符号；$b_0$ 任意正负都被同一个复二式排除。

## 6. 结论的实际范围

原 R239 圆在整个 (1) 族内都有不可由允许 gauge 修复的第四偶谐波。因此，仅移动端芽的常数 $\omega$ 平移参数，也不能救回该构造。

本稿没有宣称原六能量零在任意 $b_0$ 下自动保持；无需这个额外主张，完整面积门已经足以否定。也没有假设单个微包的 Volterra 尾为零：§4–5 只拆局部四次积分，真正的原算子与所有 history 在 §2–3 已整体搬移。

对于一般 profile 圆，$M_4$、$N_1$ 及 $M_1+b_0M_4$ 仍可能满足新的必要关系。其他端芽、其他圆、完整 period/joint 的建设性可解性以及主课题的最终要求均未由本稿解决。
