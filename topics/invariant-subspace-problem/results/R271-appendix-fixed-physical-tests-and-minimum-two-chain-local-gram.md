# R271 附录：真实两费头旗余商的固定物理测试、最小双链表示与局部 Gram

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d；AI-assisted，GPT-6 Astra Pro。

状态：**下述准确公式与等价判据已证明。** 本文将实际 good-top 余源的固定物理坐标，写成同一个原源上的最小裸／平坦双链测试。原低头源旗在完整 primitive 源坐标中是斜条带；真实消元是该条带与负图之交的两费正交投影，不是删除左向量的物理坐标。

新的剩余估计只涉及每个固定有限物理测试空间上的有限维正 Gram。若逐个得到窗口计数阶的上界，即足以排除实际固定非零缺陷；不要求先控制整个左源度量。本文没有证明这些上界，没有由头旗增长推出无权 $N=M$ 或普通 Hilbert ISP。

依赖：

- [完整左 primitive 坐标与边界 Schur](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)。
- [完整源坐标、全部零源旗及增长头观测](R239-appendix-complete-source-schur-coordinates-and-growing-head-observation.md)。
- [真实左截断及同未来带两费](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)。
- [准确两费 good-top 余商](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md)。
- [明确增长的原低头整旗](R271-appendix-dyadic-original-heads-birth-one-repair-and-explicit-growing-quotient.md)。

## 1. 固定同一个原头、切口和左坐标

固定原合法 $m,d=2^m,b$，写 $A=A_m,D=D_m$。所有下式均在这个原物理内积中，所有头和尾旗均保留原 $d$。

原左空间、源映射和费用为
$$
V_b=\mathcal H_{\le b}^{(m)}
 \cap\ker\bigl(P_{\le b-1}^{(m)}(A+D)\bigr),\qquad
E_bv=Av_b,\qquad
L=(E_bE_b^*)^{-1},
$$
$$
\mathscr R_b=\bigoplus_{i=0}^{d-2}e_i
 (\ker D^{d-i-1}\cap\mathcal H_b),\qquad
u(r)=E_b^\dagger r.
\tag{1.1}
$$
在同一个原源空间上，令
$$
B=J_{\rm bare}^{-1},\qquad G=J_{\rm right},\qquad
M_2=B+LGL.
\tag{1.2}
$$
记原裸最小链为 $\mathcal A_b r$，完整平坦链为
$\mathcal C_b r=F_b^*Lr$。则
$$
\alpha(r)^2=\|\mathcal A_br\|^2,\qquad
\lambda_{\rm flat}(r)^2=\|\mathcal C_br\|^2,\qquad
\Xi(r)^2=\langle M_2r,r\rangle.
\tag{1.3}
$$
这里 $\mathcal C_b r$ 使用同一个 $r$ 的原完整左度量；没有重选平坦源。

令 $K_p=\ker D\cap\mathcal H_p$，并使用完整左坐标化
$$
\mathfrak P=\mathbb C^d\otimes\bigoplus_{p=0}^bK_p,\qquad
\mathcal E p=P_{\le b}\sum_{j=0}^{d-1}(-A)^jQ_jp,
\qquad
\mathcal D=\mathcal E^*\mathcal E\succeq I .
\tag{1.4}
$$
这里 $Q_j$ 是原顺次单步 MP 原像，严格增加 $j$ 个尾孔；
$\mathcal E:\mathfrak P\to V_b$ 是有界双射，逆为逐孔 primitive 投影。
以下 $\mathcal D$ 是坐标度量，不是纯尾删除 $D$。

置
$$
\mathcal B=E_b\mathcal E,\qquad
\mathfrak K=\ker\mathcal B
 =\bigoplus_{p=0}^b\ker A^{b-p+1}\otimes K_p,
$$
$$
\mathfrak U=\mathfrak K^\perp
 =\bigoplus_{t=0}^{d-2}H_{\ge t+1}\otimes K_{b-t}.
\tag{1.5}
$$
其中 $H_{\ge j}=\operatorname{span}(e_j,\ldots,e_{d-1})$。按
$\mathfrak P=\mathfrak K\oplus\mathfrak U$ 写 $\mathcal D=(D_{IJ})$。
已有准确源同构为
$$
B_U=\mathcal B|_{\mathfrak U},\qquad \Gamma=B_U^{-1},
\qquad
(\Gamma r)_t=(-1)^t
 \bigl(A^{t+1}|_{H_{\ge t+1}}\bigr)^{-1}P_{\ker D}D^tr.
\tag{1.6}
$$
固定参数下 $B_U,\Gamma$ 均有界；本文没有赋予 $\Gamma$ 一致小范数。

给定 $a=\Gamma r$，真正最小左原像的 primitive 坐标为
$$
J_{\min}a=
 \begin{pmatrix}-D_{KK}^{-1}D_{KU}a\\a\end{pmatrix},
\qquad
u(r)=\mathcal E J_{\min}a .
\tag{1.7}
$$
这是对全部零源坐标的真实最小化；$D_{KK}\succeq I$，所以该逆有界且范数至多一。

## 2. 原低头源旗准确对应哪条 primitive 条带

令
$$
\mathscr F_h=\mathscr R_b\cap\ker A^h,\qquad
1\le h\le d-1.
\tag{2.1}
$$
则其完整独立坐标像准确为
$$
\boxed{\Gamma\mathscr F_h=\mathfrak S_h
=\bigoplus_{t=0}^{d-2}
 \operatorname{span}\{e_{t+1},\ldots,e_{\min(t+h,d-1)}\}
 \otimes K_{b-t}.}
\tag{2.2}
$$

证明：由源 jet 身份，
$$
P_{\ker D}D^tr=(-1)^tA^{t+1}a_t.
$$
头尾交换，故
$$
P_{\ker D}D^t A^hr=(-1)^tA^{h+t+1}a_t.
\tag{2.3}
$$
$A^h$ 保原源旗，而 $\Gamma$ 对原源单射，因此 $A^hr=0$ 当且仅当
(2.3) 对全部 $t$ 为零。原 regular 头的准确核旗为
$\ker A^\ell=\operatorname{span}(e_0,\ldots,e_{\ell-1})$，
与 $a_t\in H_{\ge t+1}$ 相交即得 (2.2)。反向同理。

所以 $\mathscr F_h$ 不对应左向量中前 $h$ 个物理头的投影。
它对应每个 source jet 层的头指标 $t+1$ 至 $t+h$；
不同 $t$ 的条带位置不同。即使 $h\to\infty$，也不能据此先令
$u(r)$ 的固定物理坐标为零。

## 3. 固定物理测试的准确左对偶行

对一个固定正整数 $n$，取原边界整数坐标空间
$$
\mathscr T_n=\operatorname{span}\{e_0,\ldots,e_{n-1}\}.
\tag{3.1}
$$
当 $d\ge n$ 时，它在当前头／尾分解中位于前 $n$ 个物理头与尾真空。
这里的 $\mathscr T_n$ 不随 $m,b$ 移动。
记其到 $\mathfrak K$ 的自然等距嵌入为 $\iota_n$；
合法 $b\ge4d$ 保证整个第零 primitive 孔层都在 $\mathfrak K$。

对任何 $f\in\mathscr T_n$，有
$$
\boxed{\mathcal E^*f=\iota_nf.}
\tag{3.2}
$$
确实，(1.4) 中每个 $j\ge1$ 项都提高尾孔数，不能与尾真空配对；
$j=0$ 项就是原 primitive 坐标。此式无需一个相似变换。

定义实际对偶行的伴随映射
$$
\boxed{\mathcal A_n=-D_{UK}D_{KK}^{-1}\iota_n:
\mathscr T_n\longrightarrow\mathfrak U.}
\tag{3.3}
$$
则由 (1.7)、(3.2) 得
$$
\boxed{P_{\mathscr T_n}u(r)=\mathcal A_n^*\Gamma r.}
\tag{3.4}
$$
因此固定物理测试只需明确的低孔输入 $\iota_nf$、真实零源逆
$D_{KK}^{-1}$ 和真实交叉块 $D_{UK}$。逆的范数至多一不意味着
整个乘积 (3.3) 小，也不意味着它保持 (2.2)。

同一事实还有原源版本。由于 $\mathcal E$ 是到闭空间 $V_b$ 的同构，
$$
P_{V_b}=\mathcal E\mathcal D^{-1}\mathcal E^*.
$$
所以原真正 Riesz 测试源为
$$
\boxed{t_f=E_bP_{V_b}f
       =\mathcal B\mathcal D^{-1}\iota_nf,}
\qquad
\langle u(r),f\rangle=\langle Lr,t_f\rangle.
\tag{3.5}
$$
式 (3.3) 与 (3.5) 给相同泛函。一般不能把 $t_f$ 放入
$\mathscr F_h$：$\mathcal D^{-1}$ 的跨头项尚未被控制。

## 4. 真实负图与头旗交的两费余空间

令 $\mathscr D\subseteq\mathscr R_b$ 为当前同一个实际 good-top
已经满足的闭线性约束。例如可取
$$
\mathscr D=\ker\iota_0^*(L+B),
$$
也可取已付的完整共同费用负图，或此前精确保留的闭交约束。
本节只需它闭，且实际顶部确实属于它。

在独立坐标中置
$$
\mathfrak D=\Gamma\mathscr D,\qquad
\mathfrak Z_h=\mathfrak D\cap\mathfrak S_h,\qquad
\mathbb M=B_U^*M_2B_U.
\tag{4.1}
$$
这些都是同一固定窗口的实际对象。$\mathbb M$ 有界且严格正，
因为 $B_U$ 为有界同构而 $M_2\succ0$。不需要
$\mathbb M$ 与任意物理头投影交换。

真实两费投影后的坐标 $\widehat a=\Gamma\widehat r$ 满足
$$
\boxed{\widehat a\in\mathfrak D,\qquad
 \iota_{\mathfrak Z_h}^*\mathbb M\widehat a=0.}
\tag{4.2}
$$
记这个闭余空间为 $\mathfrak R_h$。它一般不是
$\mathfrak D\cap\mathfrak S_h^\perp$。

对任意闭子空间 $\mathfrak Y\subseteq\mathfrak U$ 定义
$$
\mathbb R_{\mathfrak Y}
=\iota_{\mathfrak Y}
 (\iota_{\mathfrak Y}^*\mathbb M\iota_{\mathfrak Y})^{-1}
 \iota_{\mathfrak Y}^*,
\tag{4.3}
$$
零空间取零算子。所有逆均有界。定义
$$
\boxed{\mathbb Q_h
 =\mathbb R_{\mathfrak D}-\mathbb R_{\mathfrak Z_h}.}
\tag{4.4}
$$
则 $\mathbb Q_h\succeq0$，其像在 $\mathfrak R_h$，且对任意
$g\in\mathfrak U$、$a\in\mathfrak R_h$，
$$
\boxed{
\langle \mathbb Ma,\mathbb Q_hg\rangle=\langle a,g\rangle,
\qquad
\langle\mathbb M\mathbb Q_hg,\mathbb Q_hg\rangle
 =\langle\mathbb Q_hg,g\rangle.}
\tag{4.5}
$$

证明：$\mathbb R_{\mathfrak D}g$ 是 $\mathfrak D$ 上的两费
Riesz 代表。因 $\mathfrak Z_h\subseteq\mathfrak D$，
$\mathbb R_{\mathfrak Z_h}g$ 恰是它在 $\mathfrak Z_h$ 上的
$\mathbb M$ 正交投影。两者之差就在 (4.2) 中，并给 (4.5)。
第二式也证明正性。这里没有对“负图限制到头旗”的约束行
假定闭值域或使用未证明存在的乘子逆。

## 5. 有限维局部 Gram 与准确最小双链

定义
$$
\boxed{\mathbb K_{n,h}
 =\mathcal A_n^*\mathbb Q_h\mathcal A_n
 \quad\hbox{于 }\mathscr T_n.}
\tag{5.1}
$$
这是原固定物理坐标上的 $n\times n$ 正半定 Gram。
全部跨头、零源 Schur 及负图反馈均包含在 (5.1) 中。

对每个 $f\in\mathscr T_n$ 置
$$
a_f=\mathbb Q_h\mathcal A_nf,\qquad r_f=B_Ua_f.
\tag{5.2}
$$
它给两个来自同一个原源 $r_f$ 的合法测试链
$\mathcal A_br_f,\mathcal C_br_f$。对任何满足 (4.2) 的原余源，
$$
\boxed{
\langle u(\widehat r),f\rangle
 =\langle\mathcal A_b\widehat r,\mathcal A_br_f\rangle
  +\langle\mathcal C_b\widehat r,\mathcal C_br_f\rangle,}
\tag{5.3}
$$
$$
\boxed{\|\mathcal A_br_f\|^2+\|\mathcal C_br_f\|^2
       =\langle\mathbb K_{n,h}f,f\rangle.}
\tag{5.4}
$$
这些等式直接由 (1.3)、(3.4)、(4.5) 得到。没有把裸链改成完整
右最小链，也没有用 $\lambda(r_f)$ 代替已经正确出现的平坦链费用。

更准确地，(5.4) 是所有在整个 $\mathfrak R_h$ 上表示同一泛函的
双链对中的最小范数平方；允许比较的双链对不必事先来自同一个源。
证明如下。映射
$$
a\longmapsto
(\mathcal A_bB_Ua,\mathcal C_bB_Ua)
$$
把 $\mathfrak R_h$ 的 $\mathbb M$ Hilbert 范数等距送到两个原链空间
的直和，像闭。式 (4.5) 给此闭像中的 Riesz 代表，恰为 (5.2) 的
双链。任何其他表示与它之差垂直该闭像，故只能增加范数平方。

于是有准确最佳常数
$$
\boxed{
\sup_{\substack{0\ne\widehat a\in\mathfrak R_h}}
\frac{\|P_{\mathscr T_n}u(B_U\widehat a)\|^2}
 {\langle\mathbb M\widehat a,\widehat a\rangle}
 =\|\mathbb K_{n,h}\|.}
\tag{5.5}
$$
对单个 $f$，相应的标量最佳常数就是
$\langle\mathbb K_{n,h}f,f\rangle$。若余空间为零，两边均按零解释。

对固定窗口及固定 $\mathfrak D$，$h$ 增加时
$\mathfrak Z_h$ 嵌套增加，因此
$$
0\preceq\mathbb K_{n,h+1}\preceq\mathbb K_{n,h}.
\tag{5.6}
$$
$h=d-1$ 时 $\mathfrak Z_h=\mathfrak D$，局部 Gram 为零。
这个逐窗口的终点不提供同时 $m,b,h$ 增长时的一致速率。

## 6. 一个保留原两链的可构造上界证书

式 (5.1) 不要求实际计算整个逆。它等价于下述明确的双测试任务。

设
$$
\widetilde{\mathcal A}=\mathcal A_bB_U,\qquad
\widetilde{\mathcal C}=\mathcal C_bB_U,\qquad
\mathbb M=\widetilde{\mathcal A}^*\widetilde{\mathcal A}
          +\widetilde{\mathcal C}^*\widetilde{\mathcal C}.
$$
若能在原空间中构造线性映射
$$
Z:\mathscr T_n\to\mathfrak Z_h,\quad
Y:\mathscr T_n\to\mathfrak D^\perp,\quad
V_b:\mathscr T_n\to\hbox{原裸链空间},\quad
V_f:\mathscr T_n\to\hbox{原完整链空间},
$$
满足准确恒等式
$$
\boxed{
\mathcal A_n=\mathbb M Z+Y
             +\widetilde{\mathcal A}^*V_b
             +\widetilde{\mathcal C}^*V_f,}
\tag{6.1}
$$
则
$$
\boxed{\mathbb K_{n,h}\preceq V_b^*V_b+V_f^*V_f.}
\tag{6.2}
$$
因为 (4.2) 杀掉前两项，最后两项是同一个余源的原双费用配对，
其范数界由 (5.4) 的最小性给出。$V_f$ 在此表示测试链，不是
重新选择一个较便宜的实际平坦源。

也可完全在源坐标中写成
$$
\boxed{
\langle\mathbb K_{n,h}f,f\rangle
=\min_{\substack{z\in\mathfrak Z_h\\y\in\mathfrak D^\perp}}
 \|\mathbb M^{-1/2}(\mathcal A_nf-\mathbb Mz-y)\|^2.}
\tag{6.3}
$$
最小值确实取得：可取
$$
z=\mathbb R_{\mathfrak Z_h}\mathcal A_nf,\qquad
y=\mathcal A_nf-\mathbb M\mathbb R_{\mathfrak D}\mathcal A_nf.
$$
由 (4.3)，此 $y\in\mathfrak D^\perp$，剩余量为
$\mathbb M\mathbb Q_h\mathcal A_nf$。任意其他 $(z,y)$ 的差与这个
剩余量在 $\mathbb M^{-1}$ 内积中正交，故其范数平方不小。
这也逐项保留了头旗交与负图湮灭子，没有将它们置换成物理投影。

## 7. 对实际固定缺陷，局部界已经足够

沿原 good-top 构造，令
$$
Q_m=\lfloor e^{d^3/4}\rfloor,\qquad
K_m^{\rm win}\asymp Q_m/d,\qquad
\varepsilon_m\longrightarrow0.
$$
采用已付原低头旗
$$
h_m=2^{\lfloor3m/4-2\rfloor}
$$
或任何已经支付的头宽。当前原顶部在同一个负图中作真正两费投影后，
已有
$$
u_m=E_{b_m}^\dagger\widehat r_m\longrightarrow w,\qquad
\Xi_{b_m}(\widehat r_m)^2
 \le \frac{2\varepsilon_m^2}{K_m^{\rm win}},
\qquad
\Gamma\widehat r_m\in\mathfrak R_{h_m}.
\tag{7.1}
$$
各窗口的约束 $\mathfrak D$ 可以包含先前确已保留的闭交；
所有下式均用该窗口真实约束定义 (5.1)。

若对每个固定 $n$，存在常数 $C_n<\infty$，并沿一个无限 $m$
子序列成立
$$
\boxed{\|\mathbb K_{n,h_m}\|\le C_nK_m^{\rm win},}
\tag{7.2}
$$
则 (5.5)、(7.1) 给
$$
\|P_{\mathscr T_n}u_m\|^2\le2C_n\varepsilon_m^2\longrightarrow0
$$
于该子序列。因此 $P_{\mathscr T_n}w=0$。不同 $n$ 可以使用不同
无限子序列和不同常数；因为同一个 $u_m$ 强趋于同一个 $w$，
这仍对每个 $n$ 给零。$\bigcup_n\mathscr T_n$ 稠密，于是 $w=0$。

更弱的 $\varepsilon_m^2\|\mathbb K_{n,h_m}\|/K_m^{\rm win}\to0$
也足够，但它依赖实际尾量；(7.2) 不要求额外尾速率。

反过来，若同一个实际 $w\ne0$ 存在，可固定一个有限支撑单位
$f$，使 $c=|\langle w,f\rangle|>0$。取固定 $n$ 含其支撑。
由 (7.1)，充分大 $m$ 有 $|\langle u_m,f\rangle|\ge c/2$。
单个测试的最佳常数于是满足
$$
\boxed{
\langle\mathbb K_{n,h_m}f,f\rangle
\ge \frac{c^2K_m^{\rm win}}{8\varepsilon_m^2}.}
\tag{7.3}
$$
若某个 $\varepsilon_m=0$，则 (7.1) 已给 $\Xi=0$、$\widehat r_m=0$，
不会产生非零极限；上述不等式只用于其余正尾量的尺度。

因此非零实际缺陷不仅要求整个左／两费比放大，还要求同一个固定
有限物理测试方向的最小双链费用，比窗口计数 $K_m^{\rm win}$
增长得更快。这是固定方向的必要条件，没有把随 $m$ 改变的
环境坏方向认作实际 $W$ 来源。

## 8. 尚缺的具体估计

本文把所需推论从“低头源旗逐渐覆盖”改写成准确可检验的原矩阵
问题 (5.1)、(6.1) 或 (6.3)。特别保留：

- 左测试的真正交叉行 $-D_{UK}D_{KK}^{-1}\iota_n$；
- 原两费度量 $\mathbb M$；
- 真实负图 $\mathfrak D$ 与斜条带的闭交 $\mathfrak Z_h$；
- 同一个原测试源产生的裸链和完整平坦链。

尚未构造满足 (7.2) 的双测试，也未证明局部逆的跨头部分由现有
头旗费用支付。逐窗口的正性、$D_{KK}^{-1}$ 的收缩性以及
$h_m\to\infty$ 均不自动给 (7.2)。无权 $N=M$ 和普通复 Hilbert ISP
继续开放。
