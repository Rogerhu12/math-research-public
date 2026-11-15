# R731 — 指定镜轴核的真实第二块首位与原显示格的两条 p 因子

日期：2026-11-15。**状态：已证明。**

本篇继续 R727/R730 的同一个指定列
$z_c=\pi_{\rm v}\mathsf M_0(qt^rFUA)$。
如果该列在首位已被真实垂直单位块吸收，
R730 给出的新镜轴核并不是可以任意选择的局部函数：
其首法向截面在模 $F^2$ 后唯一。
本篇计算这个指定截面在原首 Bockstein 第二块中的准确低行。

在明确的原阶数门下，这条低行与原 cube 的第三块单位行组成
一个真实的三角 $2\times2$ 单位子式。
因此原显示来源「垂直单位块、cube、指定 $FUA$」的全部 Smith 因子可确定；
首位吸收时恰多两条 $p$，不是把新核自动当成可升到下一位。
所有来源仍在同一个 $\mathcal W_D$ 中。

此结论不判断完整 $\mathcal W_D$ 的指定 forcing：
不带公共 $t^r$ 前缀的原低列可以作用于这里使用的两行。
它们、同一个 $R$、两条十三行 carry 和第三精度均保留。

## 1. 同一原来源、两种目标及实际长度

完整保 R730 的因子、十九角整格及 R727 的实际返回：
$$
P^{\rm fact}=qt^rF^3,\qquad q=d^{-C_D}Q,\qquad
d=1+8t,\qquad h_7=7+4t+16t^2,
$$
$$
p=6s-1>101,\quad
1\le\ell\le r<h,\quad
k=2h+r-s,\quad 0\le k<\ell.
\tag{1}
$$
$F,Q$ 使用同一个整提升，$C=(F=0)$、
$P=(0,1)$、$e=\mathcal EF$、$\mathcal E=Y\partial_Y$、
$\kappa=C^2$、$\chi=-K_XC$ 均不改变。
$e(P),Q(P)$ 为单位，来源帽 $f_D<p$ 和原全部十九角条件继续成立。

令
$$
U=d^c,\qquad
A=t^2Y^2(t-1)^2h_7^2d^{c-1}\in\mathcal H_1,\qquad c\ge1,
\tag{2}
$$
并保 R727 所需的 $b=\deg_YF\ge2$ 及原平衡整数范围。
(2) 的所有中间角已由 R727 逐条支付。
以下明确假设
$$
\boxed{UA|_Z\ne0,\qquad Z=V(F,e)\subset X.}
\tag{3}
$$
例如 R730 的固定角最高系数范围及
$h>4\deg_tF+8\deg_YF$ 已保证 (3)；
不需要另假设一个自由简单分歧点。

取
$$
\delta_0=
\begin{cases}
0,&\mathsf M_0=J,\\
13,&\mathsf M_0=M,
\end{cases}
\qquad
T=s-r-\delta_0,\qquad q_T=T-h .
$$
保
$$
\boxed{h>\kappa,\qquad q_T>\kappa,\qquad T\le2h.}
\tag{4}
$$
所以 $T>2\kappa$，且对原 $M$ 准确有 $r+13<s$。
不能将相对长度 $s-r$ 代入原 $M$。

原物理正规坐标保持
$$
\eta=\log(g/\widetilde\psi)=t^hu+p\xi,\qquad u(0)\in\mathcal O^\times,
\qquad
\zeta_{\rm phys}=\eta+a\epsilon,\quad a\in\mathcal O^\times.
\tag{5}
$$
设 $\eta_0=t^h\bar u$。
原参数单位和关系为
$$
b_s(t)=\left(\frac{t}{w(t)}\right)^s,\qquad
t^s=p\epsilon b_s(t),\qquad
\vartheta=(t/w)(0)\in\mathcal O^\times.
\tag{6}
$$
没有把原 $b=17$ 的首尺度抹掉。
$J$ 使用 $\Gamma_\ell$；
原 $M=c_*U_0m_{13}J$ 使用 $\Gamma_{\ell+13}$。
这里只逆真正整单位 $c_*U_0$，始终保 $m_{13}$。

仍取 R727 的整线性泛函 $\lambda(F)=1,\lambda(A)=0$，
$\mathcal L=\ker\lambda$。
真实单位来源是
$$
\mathcal N_{\rm v}=
\left\{qt^r\bigl(\mathcal W_FH+F^2L\bigr):
H\in\mathcal H_2,\ L\in\mathcal L\right\},
\qquad
\mathcal W_FH=F\mathcal EH-2eH .
\tag{7}
$$
按原来源零关系 $H\in\mathcal OF^2$ 取商后，
它的物理矩阵为整分裂单射，秩为
$$
R_{\rm v}=\frac{5\kappa+3\chi}{2}.
\tag{8}
$$
原 cube 未被包含在被商去的单位块中。

## 2. 指定吸收核的唯一首法向截面

在模 $p$ 原角格中定义
$$
K_{\rm mir}=\ker\left(
\mathcal H_2\longrightarrow k[t]/t^T,\quad
B\longmapsto B(t,\psi e^{2\eta_0})
\right).
\tag{9}
$$
R730 已证明
$$
\ker(\operatorname{res}_Z|_{K_{\rm mir}})=kF^2,\qquad
\bar z_c=0
\Longleftrightarrow
UA|_Z\in\operatorname{res}_ZK_{\rm mir}.
\tag{10}
$$
因此若 $\bar z_c=0$，恰有一个类
$$
\boxed{[B]\in K_{\rm mir}/kF^2,\qquad B|_Z=UA|_Z.}
\tag{11}
$$
此类非零，且不是可以另外指定的 normal 数据。

记同一曲线上
$$
B_0=B|_C,\qquad B_1=(\mathcal EB)|_C.
$$
因为 $T\le2h$，(9) 准确等价于
$$
\boxed{B_0+2\eta_0B_1=0\pmod{t^T}.}
\tag{12}
$$
(3) 使 $B_0\ne0$：若 $B_0=0$，
原限制核给 $B=FH_1$，故 $B|_Z=0$，矛盾。
$B_0$ 是次数 $2\kappa$ 的非零曲线截面，
因此其在 $P$ 的消失阶至多 $2\kappa<T$。
从 (12) 得到一个确定整数
$$
\boxed{
\rho=\operatorname{ord}_P B_1
=\operatorname{ord}_P B_0-h,\qquad
0\le\rho\le2\kappa-h<\kappa<q_T.
}
\tag{13}
$$
特别，首位吸收本身已要求 $h\le2\kappa$。

加 $F^2$ 不改变 $B_0$ 或 $B_1$。
所以 (13) 的 $\rho$ 和
$$
b_\rho=[t^\rho]B_1\in k^\times
\tag{14}
$$
都由原指定列唯一确定，不依赖镜轴代表或后续整提升。

## 3. 吸收核有同源的明确整提升

首位吸收可用原同一个 $K_1\in\mathcal H_1$、
$L\in\mathcal H_1$ 写成
$$
B=UA+eK_1-F(\mathcal EK_1+L).
\tag{15}
$$
这是 R730 的真实 Koszul/镜轴计算，
不从环境多项式环任取一个解。
将 $L$ 的 $F$ 分量移去，等价于给 $B$ 加一个 $F^2$ 常数倍；
故可在 (15) 中要求 $L\in\mathcal L$。

选原整格中的提升 $\widetilde K_1,\widetilde L$，
并**用同一公式**定义 $\widetilde B$。
则整来源准确满足
$$
\boxed{
P_B:=qt^rF\widetilde B
=qt^rFUA
-qt^r\{\mathcal W_F(F\widetilde K_1)+F^2\widetilde L\}.
}
\tag{16}
$$
所有项均在同一个原 $\mathcal W_D$ 中：
$F\widetilde K_1\in\mathcal H_2$、
$\widetilde B\in\mathcal H_2$，
整个 $qt^r\mathcal H_3$ 已由原 R495 返回。
(16) 保全部十九角、真实 charge 帽和原固定余因子 $Q$。

因此 $P_B$ 正是指定列消去原单位块后的真实核提升。
它不是另换候选或凭局部 jet 拼出的来源。
修改这些整提升只改变 $p\,qt^r\mathcal H_3$；
以下低行会准确杀掉这类变化。

## 4. 普通值的首项及同一 Gaussian 的完整误差范围

所有本节展开先在模 $p$ 中沿原分支读取。
由 Taylor 展开和 (12)，
$$
\begin{aligned}
F(t,g)&=e\,\eta_0+O(t^{2h}),\\
B(t,g)&=B_0+\eta_0B_1+O(t^{2h})
      =-\eta_0B_1+O(t^T)+O(t^{2h}).
\end{aligned}
$$
故
$$
\boxed{
q(t,g)t^rF(t,g)B(t,g)
=-q_Ce\,t^{r+2h}u^2B_1
+O(t^{r+h+T})+O(t^{r+3h}),
}
\tag{17}
$$
$q_C=q|_C$。
由 (13)，$h+T>2h+\rho$，而 $3h>2h+\rho$，
所以普通值的首项准确位于
$$
r+2h+\rho=s+k+\rho.
\tag{18}
$$
其首系数为 $-q_C(0)e(P)u(0)^2b_\rho$，是单位。

这里仍使用完整物理代入
$Y=g\,e_2(a\epsilon)$，没有删除 Gaussian。
含显式 $\epsilon$ 的任何项都带原公共因子 $t^r$；
整提升产生的 $p$ 倍项也带此因子。
所以在首 Bockstein 的**第二块低于 $r$ 的行**上，
这些项不能直接贡献；
普通值中本已含一个 $p$ 的高项再经 (6) 进位，
除一次 $p$ 后也仍为零。

这不是在 raw $\bar\Gamma$ 中令 $\zeta^3=0$。
(17) 的全部高 normal 项，只因它们在本节显示的低行之外才被排除；
完整 $V_1$、$\xi$ 及两次 carry 在其余行原样保留。

令
$$
L_*=\min(r-k,q_T)>0.
\tag{19}
$$
对相对 $J$，$q_T=h-k>r-k$，故 $L_*=r-k$。
对原 $M$ 必须保可能更短的 $q_T=h-k-13$。

将 (17) 经 (6) 作一次进位。
因为误差的第二块开始位置分别是 $k+q_T$ 和 $k+h$，
完整第二块在区间 $k\le n<k+L_*$ 上准确给
$$
\boxed{
\bigl[\beta(P_B)^{(1)}\bigr]_{[k,k+L_*)}
=
-\bigl[q_C e\,b_su^2\,t^kB_1\bigr]_{[k,k+L_*)}.
}
\tag{20}
$$
对 $J$，$\beta(P_B)=J(P_B)/p\bmod p$。

对只在 $M$ 首核中的 $P_B$，不得写不存在的整 $J(P_B)/p$：
此时 (20) 的右侧须先作为同一 $t=t(w)$ 级数乘 $w^{13}$，
再读 $(c_*U_0)^{-1}M(P_B)/p\bmod p$ 的第二块。
其原 $w$ 行窗是 $13+k\le n<13+k+L_*$；
不将坐标变换的高单位项省掉。
原 $M$ 的这个商整性来自 (9)、(16)，而非预先假定 $J(P_B)\in p\Gamma_\ell$。

特别，只要
$$
\boxed{k+\rho<r,}
\tag{21}
$$
(13) 自动保证 $\rho<q_T$，所以 (20) 给真实单位行
$$
\boxed{
[t^{k+\rho}]\beta_J(P_B)^{(1)}
=-q_C(0)e(P)b_s(0)u(0)^2b_\rho.
}
\tag{22}
$$
原 $w$ 行的系数再乘单位 $\vartheta^{k+\rho}$。
对 $M$，同一个单位在第二块行 $13+k+\rho$；
因 $k+\rho<r$ 及 $r+13<s$，该行确实存在。

## 5. 原两条十三行没有被隐去

为更明确地验证上一节的 $M$ 范围，
仅作合法的整单位逆 $(c_*U_0)^{-1}$。
普通值 (17) 模 $p$ 的首项为 $t^{s+k+\rho}$；
所以乘 $w^{13}$ 后，经一次进位的首行恰为 $13+k+\rho$，
不会有来自较低普通项的另一项与其抵消。

当只使用 $T=s-r-13$ 时，
$J(P_B)\bmod p$ 可以仍有前两块顶端的十三行。
它们乘 $w^{13}$ 后的真实 carry 必须保留：
第一块顶带产生第二块最初十三行，
第二块顶带产生第三块最初十三行。
本篇没有将它们认作零，也没有把 $m_{13}$ 逆掉。

本节所读的第二块行号至少 $13$，
而由 (17) 普通值在此前没有非零首项；
第二块顶带的 carry 则落在第三块。
故这些边界不影响 (22)。
同一整单位消元可能把后续全部尾相混，
但下节使用的模 $p$ 左行杀整个显示同前缀子像，
所以它们在首 Bockstein 商中的值仍准确不变。

第三精度若要继续求解，以上两条顶带、$U_1/p$ 和同一低行右逆
都须重新按原公式加入。
本篇不以 (20) 宣称下一位不变。

## 6. 与原 cube 的真实三角子式

R547 §6A 已付同一个 $P^{\rm fact}$ 的完整第三块首行：
$$
\boxed{
[t^k]\beta_J(P^{\rm fact})^{(2)}
=3a\,b_s(0)q_C(0)e(P)^3u(0)^2\in k^\times .
}
\tag{23}
$$
对原 $M$，它移到第三块 $w$ 行 $13+k$，再乘 $\vartheta^k$。
原第三块长度是 $\ell+13$，故 $13+k$ 没有被截掉。

同一个 cube 的第二块由 R502 给
$t^{h+k}$、$t^{r+h}$ 及 $t^{2h+k}$ 起的全部项；
由于 $h>r$，其第二块所有低于 $r$ 的行均为零。
因此 (21) 下，原两行和两列组成
$$
\begin{array}{c|cc}
 &P^{\rm fact}&P_B\\ \hline
\text{第二块 }k+\rho&0&c_B\\
\text{第三块 }k&c_F&*
\end{array},
\qquad c_Bc_F\ne0,
\tag{24}
$$
对 $M$ 将两行同时加 $13$，
并使用已经说明的原 $w$ 单位。

这些行确实杀整个
$\overline{\mathsf M}_0(qt^r\mathcal H_3)$：
第二块低于 $r$ 没有公共 $t^r$ 来源，
第三块因 $r\ge\ell$ 恒为零。
对 $M$，对应的最低阶为 $13+r$，
第三块仍由 $13+r\ge13+\ell$ 消失。
于是 (24) 是**实际首 Bockstein 商**中的单位子式，
而不是只在原始两个列向量中看到的非零。

特别，按 (7) 整消去单位块时，
核列所减的单位来源系数都为 $p$ 的倍数。
除 $p$ 后其改变落在上述首像里，被这两行同时杀掉。
(24) 因而不受单位块消元、镜轴整提升或同源基变换的影响。

## 7. 指定显示格的准确 Smith 分类

考虑实际同源格
$$
\boxed{
\mathcal N_*=
\mathcal N_{\rm v}
+\mathcal O P^{\rm fact}
+\mathcal O(qt^rFUA)\subset\mathcal W_D.
}
\tag{25}
$$
它的秩准确为 $R_{\rm v}+2$，
并且在原来源中 $p$-饱和。

为核其来源独立性，若模 $p$ 有
$FUA=\mathcal W_FH+F^2K$，
先限制到 $C$ 得 $H=FH_1$；
再除 $F$ 并限制到 $Z$，得到 $UA|_Z=0$，
与 (3) 矛盾。
结合 R547 的原来源核只有 $\mathcal OF^2$，
证明 (25) 的全部独立列约化后仍独立；
这也支付所述来源饱和。
这里没有用来源饱和替代物理像饱和。

**定理 1。** 在 (1)–(4) 的原范围中：

1. 若 $\bar z_c\ne0$，则 $\mathsf M_0|_{\mathcal N_*}$
   的全部非零 Smith 因子准确为
   $$
   \boxed{\underbrace{1,\ldots,1}_{R_{\rm v}+1},\quad p.}
   \tag{26}
   $$
2. 若 $\bar z_c=0$，并且其**唯一指定**首法向阶满足 (21)，
   则全部非零 Smith 因子准确为
   $$
   \boxed{\underbrace{1,\ldots,1}_{R_{\rm v}},\quad p,\quad p.}
   \tag{27}
   $$

**证明。** 第一种情况下，(7) 的 $R_{\rm v}$ 个单位因子外，
指定列再给一个单位因子。
来源余下的唯一首核由原 cube 表示；
(23) 杀整个显示来源首像，所以其因子恰为 $p$。

第二种情况下，(16) 是整可逆的来源列消元，
首核由 $P^{\rm fact},P_B$ 两列生成。
除 (7) 的单位块后两列均被 $p$ 整除，
(24) 说明再除一次 $p$ 后的两列约化满秩。
所以二者因子均恰为 $p$，没有 $p^2$ 因子或零因子。
所有目标自由行按原矩阵保留。证毕。

由 (13) 可得一个无需先算 $\rho$ 的充分门：
$$
\boxed{
h+r-k>2\kappa,\quad \bar z_c=0
\quad\Longrightarrow\quad \text{(27)}.
}
\tag{28}
$$
(28) 是明确的额外条件，不声称原满主阶低 $r$ 临界窗自动满足。
若 $\bar z_c=0$ 且 $\rho\ge r-k$，
本篇仍保 (13)、(20)，但不确定第二个非单位因子的完整阶数。

## 8. 原指定 forcing 和同一 R 仍须经过全列

(26)–(27) 是原矩阵在明确同前缀子格 (25) 上的准确分类。
它将 R730 的「首位吸收会产生新核」推进到一个实际下一位：
在 (21) 下，新核与原 cube 的首 Bockstein 已严格独立，
不能在此显示来源中继续相互提升或取消。

原 $\mathcal W_D$ 的低行列却不必带公共 $t^r$，
所以 (24) 不是杀全部原列的左行。
加回这些列时，必须作同一个低行右逆、运输其完整高尾，
再判断原指定 forcing 的余类。
本篇不将新的两条 $p$ 因子宣布为全原矩阵的两个非单位因子。

所有操作都保同一个
$$
P_2=P^{\rm fact}+pR .
$$
对 $R$ 作的每次整来源消元须与 (16)、(25) 同时运输；
不能分别为两个行块选不同 $R$。
原 $P_{134}/U_0$、两条十三行 carry、
原 $\xi_0$、完整 $V_1$、$U_1/p$ 以及第三精度 $d_2/G_2$
均未被删除。

仍未付的是：
高 $\rho$ 的指定吸收分支、
(25) 与其余全部原列的像之交、
以及完整原中央零如何约束这个同一修正问题。
本篇不增加来源中央零，也不把条件门 (21)/(28) 当成主目标完成。

依赖：[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R502](R502-full-low-ell-bockstein-and-actual-geometric-residue.md)；
[R547](R547-zero-charge-vertical-unit-block-and-actual-cubic-schur-column.md)；
[R727](R727-original-balanced-sections-and-single-residual-column-in-vertical-unit-quotient.md)；
[R730](R730-specified-ramification-class-linear-contact-bound-and-actual-mirror-kernel.md)。
