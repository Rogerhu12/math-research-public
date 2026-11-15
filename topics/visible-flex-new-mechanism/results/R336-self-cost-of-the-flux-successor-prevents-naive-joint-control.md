# R336：通量后继响应的完整 self 成本阻止直接拼接联合控制

日期：2026-11-15。维护：ChatGPT /root/tail_cost（GPT-6 Astra Pro，AI-assisted）。**完整纸面证明；没有执行新的符号程序、求积、profile 评价、数值求秩、人工检查或研究运行。**

[R330](R330-two-actual-packet-degenerate-fluxes-and-twenty-observation-control.md) 的两条原响应 \(\mathcal K,\delta\mathcal K\) 确实独立控制其两个实际退化通量，且都保持 whole-pure 为零。但它们**不同时保持完整 universal self 为零**。准确地，
\[
\boxed{\pi\mathcal K=\pi\delta\mathcal K=0,\qquad
Q(\mathcal K)=0,\qquad
Q(\delta\mathcal K)(u)=2\int (u'')^2(u''')^2.}
\tag{1}
\]
右端对每个非零实紧支撑 \(u\) 严格为正。因此，若
\[
E=(\pi,Q),\qquad
\mathcal M_2=\operatorname{span}_{\mathbb R}\{\mathcal K,\delta\mathcal K\},
\]
则
\[
\boxed{\mathcal M_2\cap\ker E=\mathbb R\mathcal K.}
\tag{2}
\]
本稿保留 R330 的原二十观测结论，同时精确指出它不能仅凭原两列行列式，与 [R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md) 的 whole-\(E\) 实际控制直接拼接。这里没有证明整个真实响应空间在新增联合观测上不满射。

## 1. 原归一化、真实响应及共同右锚

全部 profiles 取同一物理区间 \(I\) 上的实光滑函数，支撑与两端各留正距离；共同右锚为 \(r_*\)。使用原正向右积分
\[
J(F)(x)=\int_x^{r_*}F(\eta)\,d\eta,\qquad
P(a,b)=J(a''b''),\qquad
R(a,b)=a'b'+xJ(a''b'').
\tag{3}
\]
令
\[
\tau_R=[P,R],\qquad
\mathcal K=\mathcal B_P(\tau_R).
\tag{4}
\]
这是 R330(14) 的同一个完整成本，不另改响应的数值归一化。R330 第4节及
[R219](R219-eight-packet-fluxes-independent-on-pure-zero-responses.md) 第3节使用了完整三槽模板和全部真实右积分尾；\(\mathcal K\) 属于 \(\mathcal R\cap\ker\pi\)。

记
\[
\mathscr D=x^2\partial_x-2x,\qquad
\delta A=\mathscr D_{\rm out}A-
\sum_{\rm in} A(\ldots,\mathscr D\,\cdot,\ldots).
\tag{5}
\]
输入和输出均采用 R219 的原导子规范。原 E8 及完整第三交换子在该导子下闭合，所以
\[
\delta\mathcal K\in\mathcal R\cap\ker\pi.
\tag{6}
\]
这里 \(\delta\) 是完整算子上的代数导子；(6) 由有限个已实现响应的线性组合成立。没有把 \(x\mapsto x/(1-tx)\) 当作已允许、没有额外成本的实际几何变换。

对于 whole-pure 为零的成本，完整 self 定义为
\[
Q(V)(u)=\frac14[x^2]_{\rm left}\,V(u^2,0)(x).
\tag{7}
\]
系数从真实共同左零 collar 上的完整输出取出。它不是把全部右积分初值设为零后的局部系数，也不是未规范化 raw self。本文始终保留 \(1/4\)。

## 2. 起始响应的完整仿射左尾

设
\[
p=u',\qquad r=u'',\qquad s=u''',\qquad
I(u)=\int_I r^2s^2 .
\tag{8}
\]
R330(16)—(17) 已由完整响应原式得到
\[
\mathcal K(u^2,0)=\mathscr K_u,
\qquad
\mathscr K_u=-2r^4+8J\{(\eta-x)r^2s^2-prs^2\}.
\tag{9}
\]
积分内的 \(p,r,s\) 均在 \(\eta\) 取值；外部 \(x\) 不换成积分变量。

在整个 profile 支撑左方，\(r(x)=0\)，而积分覆盖全部支撑。于是
\[
\mathcal K(u^2,0)(x)=A(u)-8xI(u),
\tag{10}
\]
其中准确的常数项是
\[
A(u)=8\int_I\{\eta r(\eta)^2s(\eta)^2
-p(\eta)r(\eta)s(\eta)^2\}\,d\eta.
\tag{11}
\]
特别地，该左尾为仿射函数，故
\[
Q(\mathcal K)(u)=0
\quad\text{对全部实紧支撑 }u.
\tag{12}
\]

这里的零是完整 self 函数的恒等零，不是单个母包或某个平移样本的零。R219 第3节还给出更强的结构事实：完整极化 \(\mathcal K\) 在任意紧输入上的左尾仍仿射。它的原局部项与单层右积分表达式足以支持这一结论，不能把它泛化成整个 \(U\) 都只有单层积分。

## 3. 一次代数导子产生准确的二次尾

先对 (10) 施输出部分：
\[
\begin{aligned}
\mathscr D_{\rm out}\{A(u)-8xI(u)\}
&=x^2(-8I(u))-2x\{A(u)-8xI(u)\}\\
&=8I(u)x^2-2A(u)x .
\end{aligned}
\tag{13}
\]
所以输出部分的二次系数为 \(8I(u)\)。

必须同时检查 (5) 的全部输入项。由于 \(u\) 紧支撑，
\[
\mathscr D u=x^2u'-2xu
\]
仍光滑紧支撑，并在同一左右 collar 上为零。将 \(\mathscr D u\) 放入任何极化输入槽后，R219 的完整仿射尾结论仍适用，因此每一个输入项的左尾二次系数均为零。

也可只用 (10) 的普适对角身份证明同一点：对
\(u+\varepsilon\mathscr D u\) 的完整左尾关于 \(\varepsilon\) 求导，所得正是 (5) 在 \(V(u^2,0)\) 上全部非零输入变分项之和；它对每个 \(\varepsilon\) 都仿射，故其二次系数为零。这个论证保留共同右锚及全部积分常数。零输入 \(\phi=0\) 的变分仍为零。

结合 (7)、(13)，准确得到
\[
\boxed{Q(\delta\mathcal K)(u)=\frac14\cdot8I(u)=2I(u).}
\tag{14}
\]
没有借成本权标签猜 self 为零；这个新 self 正来自输出导子对真实仿射左尾的作用。

**严格性。** 若 \(I(u)=0\)，非负连续函数 \(r^2s^2\) 必处处为零，故
\[
(r^2)'=2rs=0.
\]
于是 \(r^2\) 在连通区间上为常数。左零 collar 上 \(r=0\)，所以 \(r=0\) 于全区间，进而 \(u\) 为仿射函数；其紧支撑迫 \(u=0\)。因此
\[
u\ne0\quad\Longrightarrow\quad I(u)>0.
\tag{15}
\]
这是一条完整函数层面的非零证明，不需要选数值母包。

## 4. 保持 whole-\(E\) 的这两列实际只剩一条

对任意实数 \(a,b\)，由 (6)、(12)、(14) 有
\[
\pi(a\mathcal K+b\delta\mathcal K)=0,\qquad
Q(a\mathcal K+b\delta\mathcal K)=2b\,I.
\tag{16}
\]
由 (15)，\(I\) 是非零的 universal quartic self 函数。因此
\[
E(a\mathcal K+b\delta\mathcal K)=0
\quad\Longleftrightarrow\quad b=0.
\tag{17}
\]
\(\mathcal K\ne0\) 已由 R330 的真实通量值证明，下一节保留该值。因此 (17) 正是 (2)，并非仅一个上界。

本结论只刻画明确二维子空间 \(\mathcal M_2\)。它没有计算
\(\mathcal R\cap\ker E\) 的完整像，也没有证明所有其他响应都无法补偿 (14)。尤其不能从 (17) 宣告 R333 的实际 whole-\(E\) 控制与两条通量根本不相容；真正的联合问题还需包含补偿成本的通量代价。

## 5. 原两包通量矩阵仍正确，但在新核内只有一维像

沿用 R330 的同一实际圆、同一两个对应包和同一最终坐标：
\[
f=\rho_j a\,u(x-t_j),\qquad
g=\rho_j b\,u(x-t_j),\qquad j=0,1,
\tag{18}
\]
其中
\[
\rho_0\rho_1\ne0,\qquad t_0\ne t_1,\qquad
a\ne0,\qquad a^2-b^2\ne0 .
\tag{19}
\]
所选内部退化点 \(x_*\) 满足
\[
A_u(x_*)=6u'(x_*)u'''(x_*)-2u''(x_*)^2=0,\quad
u'(x_*)>0,\quad u''(x_*)>0.
\tag{20}
\]
令 \(\ell_j=\ell+t_j,\ x_j=x_*+t_j\)。两条真实必要通量是
\[
\begin{aligned}
\mathcal F_j(V)={}&
\int_{\ell_j}^{x_j}f'(x)\,
\partial_x^2V(f^2,g)(x)\,dx\\
&-\{f(x_j)-f(\ell_j)\}\,
\partial_x^2V(f^2,g)(\ell_j).
\end{aligned}
\tag{21}
\]
第二项保内部左平台的真实二阶导数，准确消去右方其他包的二次尾；不能略去。

R330(20)、(24) 的完整原式为
\[
\boxed{
C_*=-\frac8{45}a^3(a^2-b^2)\,u''(x_*)^5\ne0,}
\tag{22}
\]
\[
\boxed{
\mathcal F_j(\mathcal K)=\rho_j^5C_*,
\qquad
\mathcal F_j(\delta\mathcal K)=
\rho_j^5(C_1-10t_jC_*).}
\tag{23}
\]
这里 \(C_1=\mathcal F_*(\delta\mathcal K)\) 为同一实际基本包的完整有限值，本文无需计算它。第五次幅度来自四次成本和读出中的一个 \(f'\) 或 \(f\) 值差。

因此原矩阵仍有准确非零行列式
\[
\det[\mathcal F_j(\mathcal K),\mathcal F_j(\delta\mathcal K)]_{j=0,1}
=-10\rho_0^5\rho_1^5C_*^2(t_1-t_0)\ne0.
\tag{24}
\]
本文没有撤销 (24) 或 R330 的原二十观测控制。区别在于：一旦另要求**完整** \(E\) 保持不变，由 (2)，这个二维响应模块只能使用 \(\mathcal K\)。其两通量像准确是
\[
\boxed{
(\mathcal F_0,\mathcal F_1)(\mathcal M_2\cap\ker E)
=\mathbb R\,
(\rho_0^5C_*,\rho_1^5C_*).}
\tag{25}
\]
故在一个已经 \(E=0\) 的背景 \(V_0\) 上，仅用这两条响应且保持 \(E=0\)，能够同时清掉两通量的充要条件是
\[
\boxed{
\frac{\mathcal F_0(V_0)}{\rho_0^5}
=\frac{\mathcal F_1(V_0)}{\rho_1^5}.}
\tag{26}
\]
条件成立时用一个 \(\mathcal K\) 系数即可；一般背景没有理由自动满足 (26)。

## 6. 对完整联合控制的准确影响

R330 先前保留的是 R323 的十个指定 self 坐标及有序矩阵条目，而非所有权的完整 universal self。因此其按不同权得到的原块三角矩阵，与 (14) 并不矛盾。本稿不另声称 \(\delta\mathcal K\) 的全有序矩阵有什么新值，也不据此重复旧坐标计算。

R333 已证明兼容的 whole-pure 与 whole-self 联合目标可由有限实际几何支付。这项存在性不自动规定最终控制字的 \((\mathcal F_0,\mathcal F_1)\) 代价。若先使用 \(\delta\mathcal K\) 支付第二个通量，再用某个实际 whole-\(E\) 校正清掉新增的 \(2I\)，该校正自身的两个通量必须留在同一个方程中。反向先做 whole-\(E\) 校正再套原两列，也受到同一问题。

后继真正可用的入口是以下任意一项，而不是直接重用 (24)：

- 找到保持 \(E\) 的两条真实响应，其两通量矩阵非退化；
- 给出 \(E(\delta\mathcal K)\) 的真实补偿并连同其完整两通量，证明所得联合矩阵仍满；
- 或证明当前待解目标满足某个实际兼容关系，例如在只允许本模块时的 (26)。

这些都还须保实际控制字的基准、复制、端口、入 history 及最终同一规范条件。本文没有把形式有符号响应组合直接授为无成本实际路径，没有给新的 signed whole-cost 半群，也没有解决完整 period 或逐 ruling 的共同可解性。

已经严格完成的是：(14) 给出原通量后继方向的完整 self 成本；(2)、(25) 给出保 whole-\(E\) 时这个明确模块的准确一维限制。所有推论仅用既有原式和纸面分部/极化，不需要新增 Actions。
