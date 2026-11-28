# R725 — 固定宽度的三片端层 cutoff、均值扰动与真实曲率分解

2026-11-28（UTC）。**已证明：不改变端层总长、中央长度或固定度量，可以用一个显式三片 $C^3$ cutoff 降低归一化端层的显式转向系数；原完整凸均值结构仍然成立。** 本文同时给出全部内部切点与端口导数、准确均值根和位置的条件扰动界，以及该转向项进入真实 shape operator 的精确秩一分解。

这不是已经执行的新 seed，也不是当前场的连续曲率或 reach 证书。当前实际有限屏幕没有提供可公开归因的曲率热点；不能据此断言最大曲率来自端层。本文不重证 R709 的全局存在、R711 的 profile 与几何比较、R721 的宽度/profile 单调性、R722 的后验存在或 R724 的两段半波抵消。新内容是在**固定宽度**下改变端层 cutoff 形状的明确构造及其完整变化账。

首次可评判的具体选择是 $\epsilon=1/8$，但本文没有生成新的科学参数、改动现有运行源或启动求解。其余原目标、全变量、固定图、全部32个 normal 阶段、原角/径向域、优化预算和连续费用责任没有被删减。

## 1. 固定的准确对象与假设

使用 [R708](R708-supported-unit-meridian-seed-contraction.md)、[R709](R709-global-convex-mean-closure-without-contraction.md) 和 [R724](R724-paired-halfwave-central-seed-and-complete-source-identity.md) 的准确定义。固定 $S>0$，两个支撑为

$$
U/S=[1/32,15/32]\cup[17/32,31/32],\qquad L=|U|=7S/8.
\tag{1}
$$

四个端层的物理总长为 $b$，各长 $\Delta=b/4$，其中

$$
0<b<L,\qquad L_c=L-b,\qquad \ell=L_c/2.
\tag{2}
$$

本结果比较时，$b,U,\Delta,L_c,\ell$ 均保持不变。固定原准确 $T_0(s,\phi)$、core $\Gamma_0$、帽高 $H_0$、补集积分及

$$
K(\phi)=P(\phi)-\Gamma_0(\phi)-\int_{U^c}T_0(s,\phi)\,ds.
\tag{3}
$$

固定度量仍是原同一个 $g=ds^2+a_{\rm deep}(s)^2d\Theta_0(\phi)^2$；不重新选择 $a_{\rm deep}$ 或参考图。比较两种准确初始 seed 时取同一 $H_0$，不因此删除后续求解中原本自由的高度坐标。

在端层上要求 $|T_0|=1$。需要 R709/R722 的正半球结论时，再要求其完整 $T_{0,z}\ge0$ 及相应存在性条件。需要经典两角导数时，要求真实数据具有所使用的联合连续偏导和共同正分母；不能从有限角工作词推得这些假设。

一个端层由局部坐标 $t\in[0,1]$ 参数化。左端层从外侧 $T_0$ 转向中央方向 $d$，使用 $\chi=C(t)$；右端层取 $\chi=C(1-t)$。$\epsilon$ 是一个固定的、与 $s,\phi,d,v$ 及所有待解变量无关的数。实现可选一个预先公开的有理 $\epsilon$；以下公式定义的是准确有理系数函数，不把工作 Horner 舍入省略。

## 2. 完整三片公式与全部接合

记原五次 smoothstep 及其准确原函数为

$$
S_5(u)=10u^3-15u^4+6u^5,\qquad
G(u)=\int_0^uS_5(v)\,dv=\frac52u^4-3u^5+u^6.
\tag{4}
$$

取 $0<\epsilon<1/2$。定义

$$
C_\epsilon(t)=
\begin{cases}
0,&t\le0,\\[2pt]
\displaystyle\frac{\epsilon}{1-\epsilon}G(t/\epsilon),
 &0\le t\le\epsilon,\\[6pt]
\displaystyle\frac{t-\epsilon/2}{1-\epsilon},
 &\epsilon\le t\le1-\epsilon,\\[6pt]
\displaystyle1-\frac{\epsilon}{1-\epsilon}G((1-t)/\epsilon),
 &1-\epsilon\le t\le1,\\[6pt]
1,&t\ge1.
\end{cases}
\tag{5}
$$

重叠端点的值相同，所以(5)无歧义。下面给出所有一、二、三阶导数，而不只声明“平滑”。

在左片，令 $u=t/\epsilon$：

$$
C_\epsilon'=\frac{S_5(u)}{1-\epsilon},\quad
C_\epsilon''=\frac{S_5'(u)}{\epsilon(1-\epsilon)},\quad
C_\epsilon'''=\frac{S_5''(u)}{\epsilon^2(1-\epsilon)}.
\tag{6}
$$

在中片：

$$
C_\epsilon'=\frac1{1-\epsilon},\qquad
C_\epsilon''=C_\epsilon'''=0.
\tag{7}
$$

在右片，令 $u=(1-t)/\epsilon$：

$$
C_\epsilon'=\frac{S_5(u)}{1-\epsilon},\quad
C_\epsilon''=-\frac{S_5'(u)}{\epsilon(1-\epsilon)},\quad
C_\epsilon'''=\frac{S_5''(u)}{\epsilon^2(1-\epsilon)}.
\tag{8}
$$

原多项式满足

$$
S_5(0)=0,\quad S_5(1)=1,\quad
S_5'(u)=30u^2(1-u)^2,\quad
S_5''(u)=60u(1-u)(1-2u).
\tag{9}
$$

故所有接点的左右极限如下。表中后三列是对 $t$ 的导数。

| 接点 | $C_\epsilon$ | $C_\epsilon'$ | $C_\epsilon''$ | $C_\epsilon'''$ |
|---|---:|---:|---:|---:|
| $0$ | $0$ | $0$ | $0$ | $0$ |
| $\epsilon$ | $\epsilon/[2(1-\epsilon)]$ | $1/(1-\epsilon)$ | $0$ | $0$ |
| $1-\epsilon$ | $1-\epsilon/[2(1-\epsilon)]$ | $1/(1-\epsilon)$ | $0$ | $0$ |
| $1$ | $1$ | $0$ | $0$ | $0$ |

例如 $G(1)=1/2$ 给出两个内部切点的值；$S_5'(0)=S_5'(1)=S_5''(0)=S_5''(1)=0$ 给出全部导数匹配。常延拓的导数也为零。因此 $C_\epsilon\in C^3(\mathbb R)$，每个开片内是多项式。

**不声称 $C^4$。** 在 $t=0$ 的右侧四阶导数为 $60/[\epsilon^3(1-\epsilon)]$，左侧为零；内部接点通常也有四阶跳变。第10节据实际六jet入口说明当前所需材料阶数为何已足够；若以后增加更高材料导数任务，必须独立升级函数，不能由本结果虚构那些导数。

若一条物理端层为 $[a,a+\Delta]$，新增内部切点准确为

$$
a+\epsilon\Delta,\qquad a+(1-\epsilon)\Delta.
\tag{10}
$$

右端层使用反向坐标，仍保留其两个真实 affine 切点及正确的奇数阶导数符号。四条端层共八个新增内部切点；重复于原节点时按准确地址合并，不按近似浮点距离合并。原全部径向节点、support、中央半波六片、scalar、控制和尾段切点仍须全部保留。

## 3. 积分归一化、峰值及高阶代价

由(9)，$S_5$ 在 $[0,1]$ 单调增加且值域为 $[0,1]$。于是(6)–(8)给出

$$
0\le C_\epsilon\le1,\quad C_\epsilon'\ge0,\quad
C_\epsilon(1-t)=1-C_\epsilon(t).
\tag{11}
$$

(11)最后一式由(5)逐片代入直接验证。进一步，

$$
\int_0^1C_\epsilon'(t)\,dt
=\frac{\epsilon/2+(1-2\epsilon)+\epsilon/2}{1-\epsilon}=1,
\qquad
\int_0^1C_\epsilon(t)\,dt=\frac12.
\tag{12}
$$

因此这不是没有归一化的“压低 derivative”构造。它仍完整经过从0到1的全部转向。

**定理1（固定宽度的峰值）。** 对(5)，

$$
\|C_\epsilon'\|_\infty=\frac1{1-\epsilon}.
\tag{13}
$$

该最大值在整个中片达到。任何绝对连续 $C$ 满足 $C(0)=0,C(1)=1$，都有 $\|C'\|_\infty\ge1$；这是 $1=\int C'\le\|C'\|_\infty$。若又要求 $C'$ 连续、两端为零且 $C'\ge0$，则最大值严格大于1：否则积分为1迫使连续函数 $C'\equiv1$，与端值矛盾。故这一类的下确界是1，而 $C_\epsilon$ 当 $\epsilon\downarrow0$ 接近它。本文没有将这个导数峰值极值问题说成完整曲率的极值问题。

原 $S_5$ 的导数峰值为 $15/8$。所以

$$
0<\epsilon<7/15
\quad\Longrightarrow\quad
\|C_\epsilon'\|_\infty<15/8.
\tag{14}
$$

对明确的有理选择 $\epsilon=1/8$，

$$
\|C_{1/8}'\|_\infty=\frac87,\qquad
\frac{\|C_{1/8}'\|_\infty}{\|S_5'\|_\infty}=\frac{64}{105}.
\tag{15}
$$

代价不可省略：

$$
\|C_\epsilon''\|_\infty
=\frac{15}{8\epsilon(1-\epsilon)},\qquad
\|C_\epsilon'''\|_\infty
=\frac{10\sqrt3}{3\epsilon^2(1-\epsilon)}.
\tag{16}
$$

第一式由 $S_5'$ 在 $1/2$ 达到 $15/8$；第二式由(9)在 $u=(3\pm\sqrt3)/6$ 达到绝对值 $10\sqrt3/3$。每物理端层的第 $j$ 阶导数还要乘 $\Delta^{-j}$。当 $\epsilon$ 很小时，高阶变化和准确分片成本增加。仅因(13)趋于1而不断缩小 $\epsilon$ 没有得到全几何收益保证。

## 4. 真正端层转向项：收益的精确范围

在固定角度，令 $|d|=|T_0|=1$，$T_0\cdot d=\cos\theta$，$\theta<\pi$。定义

$$
Y=(1-\chi)T_0+\chi d,\qquad T_b=N(Y)=Y/|Y|,\qquad
P_{T_b}=I-T_bT_b^{T}.
\tag{17}
$$

这是原完整归一化 blend，未改成球面插值或额外角度参数。直接微分得到 R721 所使用的准确分解

$$
(T_b)_s=\frac{P_{T_b}}{|Y|}
\bigl[(1-\chi)T_{0,s}+\chi_s(d-T_0)\bigr].
\tag{18}
$$

两个分量分别来自原参考在端层的实际径向变化和 cutoff 的转向。因为

$$
|Y|^2=1-2\chi(1-\chi)(1-\cos\theta),\qquad
Y\times(d-T_0)=T_0\times d,
$$

第二个分量的**准确范数**是

$$
\left|\frac{\chi_sP_{T_b}(d-T_0)}{|Y|}\right|
=\frac{|\chi_s|\sin\theta}{|Y|^2}.
\tag{19}
$$

这里保留了方向投影，不把 $|d-T_0|\le2$ 的粗界称为准确主曲率。

若整个端层已有共同界
$|T_{0,s}|\le U_s$、$|Y|\ge\nu>0$、$\theta\le\theta_*<\pi$，则
$|Y|^2\ge\cos^2(\theta/2)$，故

$$
|(T_b)_s|
\le \frac{U_s}{\nu}
+2\|\chi_s\|_\infty\tan(\theta_*/2).
\tag{20}
$$

代入 $\Delta=b/4$ 与(13)得

$$
\boxed{\quad
|(T_b)_s|\le
\frac{U_s}{\nu}+
\frac{8}{b(1-\epsilon)}\tan(\theta_*/2).
\quad}
\tag{21}
$$

原 $S_5$ 在同一组**已经成立的共同界**下给
$U_s/\nu+(15/b)\tan(\theta_*/2)$。$\epsilon=1/8$ 的显式转向系数是 $64/(7b)$，比值为 $64/105$。

若在一个端层中 $T_0$ 和 $d$ 都不随 $s$ 改变，(21)的第二项是准确最大值：在 $t=1/2$，同时有 $\chi=1/2$ 和 $\chi_s=1/[\Delta(1-\epsilon)]$。一般真实 $T_{0,s}\ne0$ 时，只可使用(18)–(21)，不能删去第一项，也不能把两个向量的三角界当成其真实和。

**收益没有自动传到两个实际不同 seed 的共同 $U_s,\nu,\theta_*$。** $T_0$ 与物理端层相同，故原参考的 $U_s$ 可共用；但准确 $d$ 会改变，新的角度与分母界必须成立。本文没有把工作保存的近单位 $d$ 当成(17)的准确单位向量。

## 5. 原凸均值条件在哪个范围保留

新的 $C_\epsilon$ 仍满足 $0\le\chi\le1$，并且不依赖待解方向或角变量。因此 R709 的势函数仍是

$$
\psi_{s,\phi}(y)=
\begin{cases}
\bigl(|(1-\chi)T_0+\chi y|-(1-\chi)\bigr)/\chi,&\chi>0,\\
T_0\cdot y,&\chi=0,
\end{cases}
\qquad
\Psi(y,\phi)=\int_E\psi_{s,\phi}(y)\,ds.
\tag{22}
$$

这不是新的存在性定理假设。逐片的范数反三角不等式仍给
$|\psi(y_1)-\psi(y_0)|\le|y_1-y_0|$；$\chi\to0$ 的有限延拓仍是 $T_0\cdot y$。所以 $\Psi$ 在整个闭单位球连续、凸且 $b$-Lipschitz，包括可能出现 $Y=0$ 的点。正分母区域上

$$
B(d,\phi)=\nabla_d\Psi(d,\phi),\qquad
M=D_dB=\int_E\frac{\chi}{|Y|}P_{T_b}\,ds\succeq0.
\tag{23}
$$

上述性质只用到了 $\chi$ 的取值域和不依赖 $d$，不要求原五次 $S_5$ 的具体形状。R709 已证明的全局根结论因此可以对新 $B$ 直接实例化，而不改它的真实前提。

具体地，若整个角圈有同源准确界

$$
0<k_-\le|K|\le k_+<L,\quad K_z\ge k_z>0,\quad
|T_0|=1,\quad T_{0,z}\ge0\ \hbox{于 }E,
$$

并满足

$$
b<k_-,\qquad b<k_z,\qquad k_++2b<L,
\tag{24}
$$

及中央正长度，则新完整方程

$$
L_cv+B(v/|v|,\phi)=K(\phi)
\tag{25}
$$

有 R709 的唯一正径向根。其原界

$$
r_-=\frac{k_--b}{L_c},\quad
r_+=\frac{k_++b}{L_c},\quad
\zeta=\frac{k_z-b}{k_++b},\quad
\nu=\sqrt{\frac{1-\sqrt{1-\zeta^2}}2}
\tag{26}
$$

以及完整非对称均值 Jacobian 的逆界照原成立。**本比较不改变(24)中任何几何量，所以已成立的粗条件不因 cutoff 形状变化而丢失；尚未成立的粗条件也不会因(13)更小而自动获得。**

若实际候选只能通过 [R722](R722-posterior-convex-mean-root-existence.md)，则必须对新 $B$ 重新包围完整残差与相应帽界。旧 $B$ 的真实根、旧后验 residual、旧 root-domain attribution 或旧 R709 布尔值，均不能改名后供新源使用。(22)(23)说明 R722 的凸性结构仍适用，不声称其数值条件已经满足。

由于 $K,L_c$ 不变，准确均值变化只出现在 $B$。设新根存在，记 $v=rd$。新的 $r,d$ 一般不等于原值；原辅助十二片 $A_\delta$ 关系 $A_\delta(\lambda)=r$ 的公式保持，但其输入 $r$、输出 $\lambda$ 和相应两角 jet 均必须重取。R724 的正负半波跨段抵消对这个新共同 $d,w,\lambda$ 仍按原公式成立，不要求把新方向等同于旧方向。

## 6. 两个准确正根的条件稳定界

以下是改变 cutoff 时可实际接入的比较公式，**不是仅凭工作候选证明新根存在**。

固定同一个角度、同一个 $K,L_c$。设两种 cutoff 已各有准确根

$$
\alpha_i d_i+B_i(d_i)=K,\qquad |d_i|=1,\qquad
\alpha_i=L_cr_i>0,\quad i=0,1.
\tag{27}
$$

假设 $B_1$ 是(22)对应的凸梯度，且以下所用值有定义。令

$$
e_B=|B_1(d_0)-B_0(d_0)|.
$$

**定理2（方向稳定）。**

$$
\boxed{\qquad
|d_1-d_0|\le \frac{2e_B}{\alpha_0+\alpha_1}.
\qquad}
\tag{28}
$$

**证明。** 从(27)相减并与 $\delta d=d_1-d_0$ 点乘。单位性给

$$
(\alpha_1d_1-\alpha_0d_0)\cdot\delta d
=\frac{\alpha_0+\alpha_1}{2}|\delta d|^2.
$$

凸梯度的单调性给
$(B_1(d_1)-B_1(d_0))\cdot\delta d\ge0$。剩余项绝对值不超过 $e_B|\delta d|$。若 $\delta d=0$ 结论成立；否则除以其范数和正分母即得(28)。证毕。

再假设 $T_{0,z}\ge0$ 且两个方向均满足 $(d_i)_z\ge\zeta_*>0$。连接两方向的整条直线段上 $y_z\ge\zeta_*$。对 $\chi>0$，

$$
Y_z\ge\chi\zeta_*,\qquad
\left\|\frac{\chi}{|Y|}P_{N(Y)}\right\|\le\frac1{\zeta_*};
$$

$\chi=0$ 的方向导数为零。故

$$
|B_1(d_1)-B_1(d_0)|\le\frac b{\zeta_*}|d_1-d_0|,
$$

并由反三角不等式得到

$$
|\alpha_1-\alpha_0|
\le e_B+\frac b{\zeta_*}|d_1-d_0|,\qquad
|r_1-r_0|\le
\frac{e_B+(b/\zeta_*)|d_1-d_0|}{L_c}.
\tag{29}
$$

这条线段估计不要求线段上 $y$ 仍为单位向量；其正垂直分量正是排除归一化奇点的理由。不能省掉这个共同假设而使用 $b/\zeta_*$。

### 6.1 从准确 cutoff 差取得 $e_B$

假设在全部端层上，准确 $d_0$ 与 $T_0$ 的夹角不超过 $\theta_*<\pi$。由(19)对 cutoff 值本身积分，

$$
|N((1-\chi_1)T_0+\chi_1d_0)
 -N((1-\chi_0)T_0+\chi_0d_0)|
\le 2\tan(\theta_*/2)|\chi_1-\chi_0|.
$$

因此四个等长端层使用同一局部形状时，

$$
e_B\le 2b\tan(\theta_*/2)
       \int_0^1|C_1(t)-C_0(t)|\,dt.
\tag{30}
$$

这是完整三分量积分的范数界，不是只比较其垂直分量。

一个完全有理的可用上界为

$$
\int_0^1|C_\epsilon-S_5|\,dt
\le \frac3{32}+
\frac{\epsilon(7-8\epsilon)}{28(1-\epsilon)}.
\tag{31}
$$

**证明。** 在 $[0,1/2]$，
$t-S_5(t)=t(1-t)(1-2t)(1+3t-3t^2)\ge0$；反射对称后直接积分得
$\int_0^1|t-S_5(t)|dt=3/32$。
又因为 $G(u)/u\le G(1)=1/2<1-\epsilon$（$G(u)/u$ 是递增函数 $S_5$ 的前段平均值），左片有 $C_\epsilon(t)\le t$；中片到 $1/2$ 也有同一不等式。用对称性和 $\int_0^1G(u)du=1/7$ 得

$$
\begin{aligned}
\int_0^1|t-C_\epsilon(t)|dt
&=2\left[
\frac{\epsilon^2}{2}-\frac{\epsilon^2}{7(1-\epsilon)}
+\frac{\epsilon}{1-\epsilon}
 \left(\frac18-\frac\epsilon2+\frac{\epsilon^2}{2}\right)\right]\\
&=\frac{\epsilon(7-8\epsilon)}{28(1-\epsilon)}.
\end{aligned}
$$

最后使用与恒等函数 $t$ 的三角不等式。证毕。$\epsilon=1/8$ 时(31)为 $195/1568$；这是一个未声称尖锐的符号上界，不是当前根变化的实测值。

若需要在旧、新形状之间作条件连续比较，可定义
$C_\eta=(1-\eta)S_5+\eta C_\epsilon$，$0\le\eta\le1$。其取值、单调性、对称性及原端口前两导数保留；$0\le\eta<1$ 的常延拓一般仅 $C^2$，与原源相同。其 derivative 峰值满足

$$
\|C_\eta'\|_\infty\le(1-\eta)\frac{15}{8}
+\frac{\eta}{1-\epsilon},
\tag{32}
$$

而(30)中相对旧形状的右端可乘 $\eta$。这不在当前任务中新增参数扫描或求解步骤。

## 7. 角 jet、幅度根和位置变化不能省略

由于 $\chi$ 不依赖 $\phi$，新端层仍有完整公式

$$
Y_\phi=(1-\chi)T_{0,\phi}+\chi d_\phi,\quad
Y_{\phi\phi}=(1-\chi)T_{0,\phi\phi}+\chi d_{\phi\phi},
$$

$$
(T_b)_\phi=DN(Y)Y_\phi,\qquad
(T_b)_{\phi\phi}=D^2N(Y)[Y_\phi,Y_\phi]+DN(Y)Y_{\phi\phi}.
\tag{33}
$$

没有 $\chi_s$ 直接项出现在(33)，但 $\chi,Y,d_\phi,d_{\phi\phi}$ 都可能改变。不能据此把 Gram 或角曲率保持为旧值。

若新完整均值方程记为 $F(v,\phi)=0$，则原 R709/R710 的全部关系仍是

$$
Jv_\phi=-F_\phi,\qquad
Jv_{\phi\phi}
=-F_{\phi\phi}-2F_{v\phi}v_\phi-F_{vv}[v_\phi,v_\phi].
\tag{34}
$$

所有右端都必须对**新的完整** $B$ 计算，保全部三分量和两个角阶数。切点与 $\epsilon$ 的角度独立性避免了额外的移动角边界项；若将来令 cutoff 依赖角度，(33)(34)不再是全部变化账。

下面给出条件位置比较，明确为何“端层更省导数”不等于“位移不受损”。设(27)及共同 $\zeta_*>0$ 成立，记
$e_d=|d_1-d_0|$、$e_\lambda=|\lambda_1-\lambda_0|$。两投影架

$$
w_i=N(e_r-(e_r\cdot d_i)d_i)
$$

均须真实有定义。若两条被归一化向量的长度不小于 $q_*>0$，则

$$
|w_1-w_0|\le\frac{2e_d}{q_*}.
\tag{35}
$$

证明是投影差范数至多 $2e_d$，再使用
$|N(x)-N(y)|\le2|x-y|/(|x|+|y|)$。后一式可平方验证：差额化为 $(|x|-|y|)^2(1+\cos\angle(x,y))/2\ge0$。

固定 $\delta$，若两条准确幅度根及连接它们的完整区间都在 $A_\delta$ 的合法域内，并有
$|A_\delta'|\ge a_*>0$，则

$$
e_\lambda\le |r_1-r_0|/a_*.
\tag{36}
$$

这不是一个已知的实际 $a_*$；若没有共同区间或下界，不可使用(36)。

令
$I_\chi=\int_0^1|C_1-C_0|dt$，
$C_\theta=2\tan(\theta_*/2)$，并在所有角度取共同上界。端层差可拆成先改方向、再改 cutoff：

$$
\int_E|T_{b,1}-T_{b,0}|\,ds
\le \frac b{\zeta_*}e_d+C_\theta b I_\chi.
\tag{37}
$$

中央半波满足 $|f|\le1$。将
$T_i=\cos(\lambda_i f)d_i+\sin(\lambda_i f)w_i$
先改变幅度、再改变两个单位架，得到

$$
|T_1-T_0|\le e_\lambda+e_d+|w_1-w_0|.
$$

因此从共同 core 锚定的准确位置可用

$$
\boxed{\quad
e_0:=\sup_{s,\phi}|F_1-F_0|
\le C_\theta bI_\chi+\frac b{\zeta_*}e_d
 +L_c(e_\lambda+e_d+e_w).
\quad}
\tag{38}
$$

这里 $e_w$ 可取(35)，并要求所有量是同一整角域的界。两个新旧 seed 的完整准确均值均闭合，所以最终帽端位置相同；中间位置仍可改变，不能把总积分零误作每一部分积分零。

(38)可进入 R711 已登记的 $D_1\le D_0+2e_0$ 与固定 witness 距离至少减 $e_0$ 的比较接口。本文不重新认领这些几何转移定理。对于真实
$g_+=1-|F-q_+|^2/L_{\rm wit}^2$，即使某个 derivative 系数下降，也不能断言新 $g_+$ 下降；必须有新的位置、方向或上述完整有利余量。

## 8. 转向项进入真实 principal curvature 的准确位置

本节给一个可用的局部诊断恒等式，避免把 $|T_s|$ 当成完整 shape operator。设任一真实 $C^2$ 浸入在某点有
$V=F_s,W=F_\phi$，$V\times W\ne0$。任选一致单位法向 $n$，记

$$
a=|V|,\quad c=\frac{V\cdot W}{a^2},\quad
q=\frac{|V\times W|}{a},\quad
h_{ss}=n\cdot F_{ss},\
h_{s\phi}=n\cdot F_{s\phi},\
h_{\phi\phi}=n\cdot F_{\phi\phi}.
$$

在正交切向基
$e_1=V/a$、$e_2=(W-cV)/q$
下，shape operator 的对称矩阵准确为

$$
{\cal S}=
\begin{pmatrix}
h_{ss}/a^2 & (h_{s\phi}-ch_{ss})/(aq)\\
(h_{s\phi}-ch_{ss})/(aq) &
(h_{\phi\phi}-2ch_{s\phi}+c^2h_{ss})/q^2
\end{pmatrix}.
\tag{39}
$$

**证明。** 将第二基本形式的材料矩阵
$\bigl(\begin{smallmatrix}h_{ss}&h_{s\phi}\\h_{s\phi}&h_{\phi\phi}\end{smallmatrix}\bigr)$
分别作用于材料方向 $(1/a,0)$、$(-c/q,1/q)$ 即得各项。故特征值正是两条有符号 principal curvature，$K=\|{\cal S}\|_{\rm op}$。

(39)中的纯 $F_{ss}$ 项是

$$
h_{ss}\,u u^T,\qquad u=(1/a,-c/q)^T,
\qquad
\|h_{ss}uu^T\|_{\rm op}
=|h_{ss}|\frac{G_{\phi\phi}}{\det G}.
\tag{40}
$$

等号末步使用
$G_{\phi\phi}=q^2+c^2a^2$、$\det G=a^2q^2$。因此即使 $|F_{ss}|$ 下降，真实法向投影、Gram 和余下混合/角二阶项仍不可省略。

对于未加当前外层旋转与 closure lift 的准确单位 seed，(18)在一点给
$F_{ss}=A+\chi_s B_*$
，其中
$A=(1-\chi)DN(Y)T_{0,s}$、
$B_*=DN(Y)(d-T_0)$。
**若仅作代数上的偏项分析，暂将同一点所有其他 jet 固定**，改变 $\chi_s$ 在(39)中的贡献为

$$
\delta\chi_s\,(n\cdot B_*)\,u u^T.
\tag{41}
$$

其范数是
$|\delta\chi_s\,n\cdot B_*|G_{\phi\phi}/\det G$。
(41)并不是两个完整新旧场的差公式；实际改 cutoff 还会改变 $F,F_\phi$、法向、$d$、幅度根和全部角 jet。不同矩阵项可能抵消，所以不从一个 rank-one 分量的绝对值减小推出 $\|{\cal S}\|_{\rm op}$ 单调。

当前正常场还包含全部控制旋转、32个隐式 normal 阶段以及实际 raw-defect lift。特别工作字段中有
$F_{ss}=T_s+h''\Delta_{\rm raw}$。
这些项在(39)中全部保留。本文没有把准确 seed 的(21)或(41)替换成工作场的 whole-$K$ 界。

## 9. 完整端口、对称和相位范围

假设准确 $T_0$、新根和投影架具有所需联合正则性，且归一化分母不为零。

在外侧端口，$\chi$ 及前三阶径向导数均为零，故归一化端层与原 $T_0$ 的径向 jets 至三阶匹配。在中央侧，$1-\chi$ 及前三阶导数均为零，故端层为 $d$，前三径向导数为零。内部两个 cut 的 $\chi$ 及前三导数逐项相同，所以通过光滑归一化映射后同样匹配。R724 中央半波的原平端口保持，没有改其六片或峰值公式。

对完整场实际必需的 $T,T_s,T_\phi,T_{\phi\phi}$，这些接合给出原 $C^2$ 位置参数化所需连续性。若要更高联合材料/角阶数，必须由真实 $T_0$ 和根分支另有相应正则性；本结果不从两个角导数虚构任意高角光滑。

新 cutoff 是纯径向标量，故原正交协变公式在其旧完整前提下保留：如果 $T_0,K,e_r$ 对某个给定角变换与正交矩阵 $Q$ 协变，那么新 $B(Qd)=QB(d)$；相应唯一准确根也按 $Q$ 变换，投影架与两段半波随后协变。若没有准确唯一分支，不能只凭 Fourier 模式声称工作根已具有半转。

原 core 反射、帽、固定标记区和物理相位链没有改变公式。它们仍需要原完整端口、强 $C^2$ 参数性、同场全角/全径向 Gram、全相位 embedding/outwardness 和混合点对条件。新的 cutoff 不改变这些责任，也不自动给出未标记全等或非全等结论。

## 10. 实际源码所需的材料导数阶数

本节依据下表完整来源的真实函数正文，而不是从“sixjet”名称推测。全部文件均为当前已锁的完整文本；本次未执行源码、AST 或数值。

| 完整来源 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| [paired seed](../scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_reference.py) | 43697 | cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0 | cc877246e546b8294826ad38d33b3eb2f7434f25 |
| [paired base](../scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_operator.py) | 40803 | b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6 | 350c2e057e6af15e663d0fdb463a518bebc36234 |
| [paired normal](../scripts/resume_20261126/fixed_fejer_paired_halfwave_normal_lift.py) | 96271 | c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac | f285b87e4705b534935dab238d531be22af90740 |
| [detached meridian helper](../scripts/resume_20261126/fixed_fejer_paired_halfwave_detached_meridian_values.py) | 41135 | f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e | 7075bca30d05c045023b7823b8f80b75bfd34d4f |
| [准确 paired radial](../scripts/resume_20261126/fixed_fejer_paired_halfwave_R722_accurate_reference_control_radial_boxes.py) | 50745 | 2baef8e83025dee6e0b74f8084e0d055a7cd15a091599cf5b343ff97b4f2963f | 5f92e643f7b331c88c3d5af068429ba8bb597af0 |

完整科学来源表为
[fixed-fejer-paired-halfwave-current-complete-runtime-binding.json](../computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json)，
67013 B，SHA256
6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638，
blob 4f20af6e3663bdf69aca7193bc29624dc706411c。
它保全部137个角色以及18个当前运行体；本文没有另造别名来源。

实际调用关系如下。

1. Seed 的 evaluate 输出 T0、T0_s、T0_phi、T0_phiphi。边界代码准确对应(17)(18)(33)；只读取 cutoff 的值和一阶材料导数。
2. Base 的 _parent 读取上述四项；_meridians/rotated_jets 使用 omega 的径向一阶和角0/1/2阶，生成 T、Ts、Tp、Tpp。
3. Normal 的 _corrected_jets 在 need_s 时读取 Ts、控制的 Ws；角 order=2 时读取 Tpp。没有从 seed 读取 T0_ss 或 cutoff 四阶导数。
4. Detached helper 的 fields_torch 无论缓存命中或原完整支路，均先执行原 _implicit_jet_value、全部32阶段，再由 T/Tp/Tpp 的积分给 F/Fphi/Fphiphi；直接给 Fs=T+hp·defect，Fss=Ts+hpp·defect，Fsphi=Tp+hp·angular_defect。缓存不是跳过数学条件的另一场。
5. 准确 radial 的 reference_piece 使用 cutoff 返回的 chi/chis，形成原三角 jet 与 Ts；AccurateAngleOracle.corrected、evaluate 和 physical_cells 继续保所有原 closure、frame、完整径向积分和原六jet。未要求 cutoff 的四阶材料导数。

Normal metadata 中的 maximum_required_mixed_exponential_derivative_order=4 描述旋转系数/控制/角隐式图的混合导数责任，不能据这个数把它解释成“必须对 cutoff 求四阶材料导数”。本节的材料阶数结论来自上述实际读取关系。

因此对当前这套完整六jet及其原物理 $C^2$ 接合，(5)的 $C^3$ 足够，且比原 $S_5$ 常延拓的 $C^2$ 更强。该结论不豁免参数导数、角根正则、scalar 或 source guard 的任何其他责任。

## 11. 最低实质改动清单：尚未实施的新来源

这里列的是未来实现必须完整做到的事项，不是一个运行前新增测试门，也不声称已经生成新科学体。

- **新 seed 本体。** 以当前完整 seed 为父，仅在边界 cutoff 的定义、值/导数求值、完整 _prepare_plan 分片及其真实定义 metadata 中引入(5)(10)。原中央半波六片、外部 T0、全部 _means/角公式、所有控制、预算和失败路径保持。新准确定义必须明确有理 epsilon；工作舍入不被当成准确多项式。
- **均值积分的真实节点与参数。** 四个边界上把两个新增 cut 加入原全部准确节点并集，保每片原完整 Gauss 规则及完整权重。原 f848 辅助十二片 A_delta 内核和 solve_mean_jets 的数学可复用：它实际接受完整 boundary_chi/weights，而不要求这些值必须来自 S5。但新输入节点、顺序、权重和所有结果需有新来源，不能继承旧 mean 工作词或缓存。
- **准确 WholeMean 与径向 source。** 当前准确边界积分实现中仍有 S5 专属求值，必须显式改成(5)的完整三片 enclosure，并重做同点全角新 B/R722 attribution。准确 radial 的 boundary cutoff 与 make_plan 同步；不能只换 seed hash。尤其原 radial 的 _s5 还供 bubble/lift 使用，不能全局替换而误改 Q、gamma 或 raw-defect lift。
- **实际参考校准与外层源守卫。** 基于新 seed 实际重建完整 reference calibration、源 schema/身份和所有必要下游绑定。可以原字共享真正未变的数学核；不能用来源别名把旧场冒作新场。原32阶段、所有 unknown/typed 历史、全变量/Norm/阈值/预算必须保持。
- **准确连续消费者。** 其 full radial cover 必须包含八个新 boundary cut、原中央六片、原全部节点/support/控制/scalar与尾段；整圆、所有32阶段根盒、同点/模型/target/源码、全部六jet、全phase/上下片/帽及 mixed 条件仍按原完整接口付费。旧 R709/R722、R723、R716 或 mesh 附证不能因定理形式仍适用而自动继承 true。

**外层工作积分边界。** 当前 base/helper 仍使用原每个 whole mesh cell 的完整 Gauss 规则及原 partial Lagrange 规则。Seed 的新 plan 含切点，不等于所有外层旋转积分已自动按它分片。若后续为保持原预算而保留该规则，必须明确保持原工作规则，并由新准确全域费用实际包围它的误差；若要改外层分片，则是另一个需完整来源与参数记录的实际改动。本文没有借“完整 cuts”标签省掉这一区别。

## 12. 已有有限热点的实际来源及未付范围

当前完整有限 screen 已计算两条 principal curvature 的真实数值公式，不是一个等待本结果“去掉三角界”的粗 K。其 whole-source：

- [so3_fixed_fejer_halfwave_geometry.py](../scripts/resume_20261126/so3_fixed_fejer_halfwave_geometry.py)，88164 B，SHA256 494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b，blob 602ef5d9e322a3301ede97a811fa9b10044bc61b；
- [fixed_fejer_complete_geometry_trial_progress.py](../scripts/resume_20261126/fixed_fejer_complete_geometry_trial_progress.py)，39500 B，SHA256 321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5，blob 8173d3576958dc5c476466dd4c5012c5ed81b0c1。

完整 scan 已返回 worst（cell/u/phi/branch）、maximum_absolute_principal_curvature，以及 amplitude.worst_by_family 中 body_diameter/distance_plus/distance_minus 的实际 location。当前网格位置另含 stage/angle/s；历史或永久 literal 点只保证 cell/u/phi，可以按该实际 mesh 与 affine 地址解释 s。_collect_complete_grid 选择真实绝对主曲率最大值，scan 再与全历史/永久点合并。

当前 observer 的 _geometry 只摘 Kmax、Dpoint 和六族 g 等标量，尚未转录这些已有位置。它的 trial.phase 是 metric/restoration，不是物理 flex 时间；原 worst 没有自动标注 seed piece 或 flex-time。未来只读转录可使用已有 location 与完整真实 seed 分片归属，不新增 F/J/root，也不能补造尚未返回的最大点。

真正 reach 屏幕仍是
$.03\,D_{\rm screen}K_{\max}-.992$，
distance_plus 仍是
$1-|F-q_+|^2/L_{\rm wit}^2$。
本结果只给一个不压缩中央长度的明确新 cutoff 方向、其准确代价和可消费比较公式。它未证明当前 $\nu,\theta_*,e_B,r,\lambda,\sigma$ 已付，未给实际 $D/K$ 或 wholeimage 改善比例。新的真实完整场、根与误差、连续 Gram、全闭相位曲率/支撑/reach、握持以及不变量仍待同来源完整计算和相应证据。
