# R964 — 原 E65 的有理 off-target 来源与两角单位交换子

日期：2026-11-26。**状态：已证明。**

本篇用 R961/R963 已公开核回的完整矩阵与准确系数，给出一个先于
$p$ 固定的有理 whole degree390 来源 $\mathscr G$。它满足
$$
\Pi_{65}\mathscr G=0,\qquad
\Pi_{65}\!\left(\frac{d}{h_7}\mathscr G\right)=Z,
$$
其中 $Z$ 正是原算术 E65 来源。这是实际原矩阵和实际乘法因子的
单位像，不另运行数学计算，也没有未显示的压缩标量。

结论首先位于同一个完整**一变量** principal theta 空间。
第7节明确给出合法的全 joint off-target 提升，并保留尚须支付的
原 $H/2$ 对应；不由边际整除推断每个伴随系数整除。

## 1. 全部原输入与非零系数

保持 $b=1$、
$$
\delta^2=-3,\quad\delta=1+2\omega,\quad
a=7+3\omega,\quad g=3+\omega,\quad X=x^3,
$$
以及 R961 的实际六 sigma 候选
$$
F=-\frac{\sigma(\delta z)\sigma(2\delta z)
             \sigma(gz)\sigma(\bar gz)\sigma(az)\sigma(18z)}
             {84\cdot9a}
=\sigma^{390}P(X).
\tag{1}
$$
$P$ 次数64，最高系数一，质量坐标65为零。
原基始终为 $\sigma^{390}(1,X,\ldots,X^{65})$。

记 $Z=F_{65,1}$，使用原首项 $z^6$ 系数一的规范；
实际整数规范另有 $\widehat Z=175Z$，本篇不改动它。
$\Pi=\Pi_{65}$ 是 R961 的整个66维有理秩一投影，$\Pi Z=Z$。
真实公开返回是
$$
\Pi F=\alpha Z,\qquad
\alpha=\frac{-25+175\delta}{5328}
      =\frac{25\omega}{72a},
\quad
N_{K/\mathbf Q}(\alpha)
=\frac{625}{2^6\,3^4\,37}.
\tag{2}
$$
R963 的同一完整 $h$ 边际给
$$
Q_2=7X^2-4X+16,\quad
R=\frac{X^2+44X+16}{Q_2},\quad
c=-\frac{\omega^2\delta}{2},
$$
$$
\Pi(cRF)=\alpha_h Z,\qquad
\alpha_h=\frac{325-425\delta}{10656}
        =-\frac g2\alpha .
\tag{3}
$$
(2)–(3) 是全部66坐标回乘的等式，不只是最高项比较。
本篇没有重新选择一个向量使投影非零。

## 2. 合法 whole 乘法域

原候选的完整因式分解包含
$$
P=X\,P_S\,R_{37}J_9,\qquad
P_S=\frac{Q_2(X+1)(X-8)}7 .
\tag{4}
$$
所以 $Q_2\mid P$。由于 $Q_2$ 有理，将
$$
F=F^{(0)}+\delta F^{(1)}
\tag{5}
$$
按 $K=\mathbf Q(\delta)$ 的两个有理分量分解以后，
两个分量的完整多项式也都被 $Q_2$ 整除。

因此 $RF^{(i)}$ 以及
$$
S F^{(i)},\qquad S=\frac{X(X-8)}{Q_2},
$$
都是 whole degree390 principal 截面。其多项式次数仍至多64。
本篇的 $S$ 只表示这个有理乘子；与原权17算术来源同名字母须作区分。
此处的分母是由原完整多项式确切约掉，而非在有限样点上忽略极。

同样，R959/R960 已核 $Q_2$ 整除原 $Z$ 的完整多项式，
所以 $RZ$ 是合法 whole 来源。这里只需这些明确的定义域；
没有把乘 $R$ 或 $S$ 当作整个 $\mathcal S_{390}$ 上处处全纯的算子。

## 3. 已有 h 非零必含真正 off-target 贡献

$\Pi$ 和 $Z$ 都有理，$R$ 也有理，所以存在 $q\in\mathbf Q$ 满足
$$
\Pi(RZ)=qZ,\qquad \Pi(cRZ)=cqZ.
\tag{6}
$$
另一方面，由 $c=-\omega^2\delta/2$ 与 (3)，
$$
\frac{\alpha_h}{c\alpha}
=\frac{g}{\omega^2\delta}
=1+\frac{2\delta}{3}\notin\mathbf Q.
\tag{7}
$$

取完全指定的合法来源 $B=F-\alpha Z$。则
$\Pi B=0$，其完整多项式被 $Q_2$ 整除，而且
$$
\boxed{
\Pi(cRB)=c\alpha
 \left(1+\frac{2\delta}{3}-q\right)Z\ne0.}
\tag{8}
$$
非零直接来自 (7)，不需要猜测或另算 $q$。
因此即使算术 $Z$ 自分量的压缩 $cq$ 非零，原 $h$ 的目标信号仍有
不可删除的 off-target 贡献；若 $cq=0$，该信号则全部来自 $B$。
原 $\alpha_h/\alpha$ 不能被冒认为 (6) 的实际自压缩。

## 4. 无未知 q 的显式有理单位预像

由 (3)、(7)，准确有
$$
\Pi(RF)=\alpha\left(1+\frac{2\delta}{3}\right)Z.
\tag{9}
$$
写
$$
\alpha=a_0+\delta a_1,\qquad
a_0=-\frac{25}{5328},\quad a_1=\frac{175}{5328}.
$$
因为 $\Pi$ 与 $R$ 有理，(2)、(9) 分别逐实行给
$$
\begin{aligned}
\Pi F^{(0)}&=a_0Z,&
\Pi F^{(1)}&=a_1Z,\\
\Pi(RF^{(0)})&=(a_0-2a_1)Z,&
\Pi(RF^{(1)})&=(a_1+2a_0/3)Z.
\end{aligned}
\tag{10}
$$
所以
$$
\Pi(7F^{(0)}+F^{(1)})=0,\qquad
\Pi\{R(7F^{(0)}+F^{(1)})\}=-\frac{25}{54}Z.
\tag{11}
$$

定义一个明确的有理来源
$$
\boxed{\mathscr G=\frac{324}{25}(7F^{(0)}+F^{(1)}).}
\tag{12}
$$
它非零，首项为 $(2268/25)z^6$，在当前 $p>211$ 为单位；
整性由原候选、(5) 的分量提取及显示的固定单位分母保持。
由 (4) 它是合法的 $Q_2$ 整除来源。
式(11)给
$$
\boxed{\Pi\mathscr G=0,\qquad \Pi(R\mathscr G)=-6Z.}
\tag{13}
$$

而 $R=1-6S$，故最强的原单位关系为
$$
\boxed{
\Pi(S\mathscr G)=Z,\qquad
[\Pi,S]\mathscr G=Z,\qquad
\Pi(cR\mathscr G)=3\omega^2\delta\,Z.}
\tag{14}
$$
交换子在这一明确的合法输入上定义：$S\mathscr G$ whole，
$S\Pi\mathscr G=0$。本篇不将其扩称为所有 whole 来源上的无极算子。
(14) 的系数 $1$ 和 $3\omega^2\delta$ 在当前好素数都是单位，
没有未知 $q$ 的分子所造成的额外坏集。

等价地，若取较小未归一来源
$F_0=a_1F^{(0)}-a_0F^{(1)}$，则
$$
\Pi F_0=0,\qquad
\Pi(RF_0)=-\frac23N(\alpha)Z,\qquad
\Pi(SF_0)=\frac19N(\alpha)Z.
$$
这是 (12)–(14) 的同一身份，不是另一输入或另一结论。

## 5. 原 canonical 格中的完整 rank-two 单位块

取原好素数处的整数系数环 $\mathcal O$。
用 $P_Z$ 表示 $Z=\sigma^{390}P_Z(X)$ 的完整有理多项式。
R960 与 (4) 分别给
$$
P_Z,\ P_{\mathscr G}\in
X(X+1)Q_2\,\mathcal O[X]_{\le60}.
$$
在原 $t=-1/X$、$\Theta=x\sigma^2$ 中，
$\sigma^{390}P=\Theta^{195}(-t)^{65}P(-1/t)$。
所以这恰是同一个 canonical 格
$$
\boxed{
\mathcal B_6(195)=
\Theta^{195}\,t(t-1)h_7(t)\,\mathcal O[t]_{\le60}
=\sigma^{390}X(X+1)Q_2\,\mathcal O[X]_{\le60},}
\tag{15}
$$
符号可吸收于整基。其秩为61，$Z,\mathscr G$ 都属于其中。
这是 canonical 正规化格；未把它认作六个算术来源在该权的多项式像。

记 $\ell(v)$ 为 $\Pi v=\ell(v)Z$ 的系数。
由于 $Z$ 最高坐标64为一，它是原整投影矩阵的真实第64行。
在 (15) 上，$S=d/h_7$ 的极被完整 $Q_2$ 因子约掉，
所以 $\ell S$ 也是整行。定义
$$
M(v)=(\ell(v),\ell(Sv)),\qquad q_S=\ell(SZ)\in\mathcal O.
$$
(14)给整个真实单位块
$$
\boxed{
M(Z,\mathscr G)=
\begin{pmatrix}1&0\\q_S&1\end{pmatrix}.}
\tag{16}
$$
因此 $M:\mathcal B_6(195)\to\mathcal O^2$ 整满射，并且
$$
\boxed{
\mathcal B_6(195)=
\mathcal OZ\oplus\mathcal O\mathscr G\oplus\ker M,
\qquad \operatorname{rank}_{\mathcal O}\ker M=59.}
\tag{17}
$$
分解无需计算 $q_S$：
从任意 $v$ 减去
$\ell(v)Z+\{\ell(Sv)-q_S\ell(v)\}\mathscr G$
以后，两行都为零；(16)也证明和式是直和。

同样，在
$\sigma^{390}Q_2\mathcal O[X]_{\le62}$
这个63维完整合法域上，核秩为61；若包括质量顶列，使用
$\sigma^{390}Q_2\mathcal O[X]_{\le63}$，域秩64、核秩62。
这些是明确列出的格，未认作原 $J_6$ 的某个受迫核。

在以上任一合法域，整个交换子的准确公式为
$$
[\Pi,S]v=\ell(Sv)Z-\ell(v)SZ.
$$
由 (16)，其整个像恰为
$$
\boxed{\operatorname{im}[\Pi,S]=\mathcal OZ+\mathcal O\,SZ,}
\tag{18}
$$
秩准确为二。它在原
$\sigma^{390}\mathcal O[X]_{\le64}$ 中还是 primitive 子格。
证明：写 $T_Z=P_Z/Q_2$，其次数62，最高系数 $1/7$ 为单位。
乘 $T_Z$ 把 $\mathcal O[X]_{\le2}$ primitive 嵌入
$\mathcal O[X]_{\le64}$，因为可用其单位最高系数作整多项式除法。
在二次多项式格中，$Q_2$ 与 $X(X-8)$ 的常数/最高项二阶 minor
是16，为单位。乘回 $T_Z$ 得 (18) 的 primitive 性。
故这是真实全交换子的一整个 rank-two 单位块，而不只是单个非零标量。

本节没有令 $M$ 等于中央矩阵或 divided-Frobenius 矩阵，
也没有令 $\mathscr G$ 的中央为零。
向原六源代数返回仍须保 R960 的导子和全部成本，
且不能将投影或中央运算穿过该导子乘法。

## 6. 真实两角商的位置

用原 $t=-1/X$，
$$
h_7(t)=7+4t+16t^2,\qquad d(t)=1+8t.
$$
原乘法因子恰为
$$
\boxed{
S=\frac{d(t)}{h_7(t)},\qquad
R=\frac{1-44t+16t^2}{h_7(t)}
 =1-\frac{6d(t)}{h_7(t)}.}
\tag{19}
$$
其中 $h_7(-1/8)=27/4$，故 $d$ 在
$\mathcal O[t]/(h_7)$ 中是单位；当前好素数处该商仍是完整二次
étale 商。于是 (14) 将新增的非零 CM 耦合定位在原两角分母方向，
并保留原 $d/h_7$，而非用一个任意三列向量替代。

在原 C24 三列 $E_j/C_{24}=7(-t)^j/h_7$ 中，$R$ 准确对应
$(1,44,16)/7$，其未归一三列方向为 $(1,44,16)$；
$R$ 的分子模 $h_7$ 为 $-6d$。
这个指定类与原合法向量 $c_*=(1,-4/7,16/7)$ 的角色不同。
以上只说明作用因子的实际两角类为单位；
没有证明整个交换子或 $\ell S$ 仅通过有限 $\mathcal O[t]/(h_7)$ 商。
更高 $h_7$ 因子的输入仍可能有 CM 贡献，不在这里删除。

没有据此额外宣称所有伙伴在两角的值、或任何原
divided-Frobenius 行已经非零。

## 7. 全 joint 的合法 off-target 对象与仍保的对应

这里专门防止把 (4) 错升为六变量逐伴随系数整除。
令 $\mathcal F_\rho=(9a)^{-1}(L_h)_*\rho_{\rm raw}$ 是 R963 的整个
同框架来源，其第一边际为 $\omega^2F$。
置 $\mathcal X=\omega^{-2}\mathcal F_\rho$。
先在原代数 theta 格上按系数分解
$\mathcal X=\mathcal X^{(0)}+\delta\mathcal X^{(1)}$；
这不是任意指定 $\mathbf C_p$ 上的共轭。

令 $\mathcal P$ 为完整第一角和原 E65 谱投影，并定义
$$
\mathcal Y=\frac{324}{25}(7\mathcal X^{(0)}
                              +\mathcal X^{(1)}),\qquad
\boxed{\mathcal B_{\rm off}=(I-\mathcal P)\mathcal Y.}
\tag{20}
$$
这些全在 R963 的同一个六变量 whole 张量格中。
第一边际和谱投影交换，所以 $\mathcal B_{\rm off}$ 的第一边际
准确为 $\mathscr G$，并且
$$
\mathcal P\mathcal B_{\rm off}=0
$$
是**整个张量**的等式。特别它是一个非零的明确整 joint 来源。

但 $\mathcal P\mathcal Y$ 的第一边际为零，不使该整个张量为零。
同样，$\mathscr G$ 的 $Q_2$ 整除不使
$\mathcal B_{\rm off}$ 的每个伴随系数都被 $Q_2$ 整除。
因此不能直接把 $S$ 乘到 (20) 后套用 (14) 作为无修正的 whole
joint 身份。

全 joint 的实际原操作仍是 R963 的
$\eta=\omega^2H_*\rho_{\rm raw}$ 与 $h=\eta+\rho_{\rm raw}/2$，
包括原 $H$ 的 $1/2$、两个整框架 $L_h,L_hH$、
全部有限 CM 纤维与 Mellin 观察。继续消费 R548(40) 时，
必须明确这些 whole 对应在 (20) 上的作用及所有余项。
本文没有让 CM 投影、两角除法或中央 divided jet 免费交换，
也没有将六条曲线的坏中央条件传播到 $\mathscr G$ 或任意乘积。

## 依据

- [R961：原 E65 同六 sigma 的完整66维投影](R961-original-e65-common-six-sigma-cm-projection.md)。
- [R963：原 h 的两态、完整共同框架与实际非零投影](R963-original-h-e65-full-cm-projection.md)。
- 原公开源 a39e5a6f88c9695ae43abcc6358679a422c4d5e8，
  run 45823614454、job 139921952585，2026-11-26 12:57:50 UTC：
  R963 三条完整66坐标回乘及全部框架检查 PASS。
- [原 C24 同三列与完整差矩阵](../notes/2026-11-16-original-common-odd-degree24-and-three-row-pairing.md)。
