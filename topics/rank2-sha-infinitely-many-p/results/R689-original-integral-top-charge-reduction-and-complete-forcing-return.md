# R689 — 原三次 forcing 的整最高项消去、较低 charge 返回与双边界修正

日期：2026-11-15。**状态：已证明。** 本篇给原 forcing 一个更低径向次数的实际多项式代表，并支付其原来源返回和完整 normal 修正。没有判定 R651 所指定的首次像或同一个 $R$ 的第二余类非零。

R521 已计算原 $K_F$ 的最高系数；本篇的新步骤是不除以 $F$ 的最高系数，而用一个明确的整二次表达减去 $F$ 的倍数。这样保留 $K_F|_C$，同时削掉最高 charge。一般 R514 的返回成本由 $D_0+3$ 降为 $D_0+2$；若同一个因子的最高两项相隔至少三个 charge，则在该篇**真实立方因子来源**的前提下，返回已经属于原同一 $\mathcal W_D$。这不是对任意未分解首核的同预算断言。

## 1. 同一对象、真实上下缺口

保原
$$
p=6s-1>101,\quad \mathcal E=Y\partial_Y,\quad
\delta=t\partial_t\ \text{（保持 }Y\text{）},
$$
$$
d=1+8t,\quad h_7=7+4t+16t^2,\quad
A=6(1-t),\quad B=-(1+2t),
$$
$$
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2}.
\tag{1}
$$
原有限非分歧系数环记为 $\mathcal O$。取一个实际整因子
$$
F=\sum_{i=0}^{b}f_i(t)Y^i\in\mathcal O[t,Y],\qquad
1\le b<p,\quad f_0f_b\ne0,
\tag{2}
$$
其约化的 $Y$ 次数仍为 $b$。需要使用曲线几何时，另保 $\bar F$ 为 primitive 几何整因子；纯整多项式及来源返回恒等式不需要这个附加条件。

定义实际支持的两个缺口
$$
h_-=\min\{i>0:f_i\ne0\},\qquad
h_+=b-\max\{i<b:f_i\ne0\}.
\tag{3}
$$
因为 $f_0f_b\ne0$，两者都在 $[1,b]$。若 $F$ 的全部 charge 在 $h\mathbb Z$，则 $h_-,h_+\ge h$；反过来，本篇只需 (3)，不要求全支持属于一个同余类。

原三次式仍是
$$
\begin{aligned}
K_F={}&e^3\mathcal R+A e^2\delta^2F
-2A e a_0\,\mathcal E\delta F\\
&+A a_0^2\,\mathcal E^2F+B e^2a_0,
\qquad e=\mathcal EF,\quad a_0=\delta F.
\end{aligned}
\tag{4}
$$
沿同一 $C:F=0$，R514 的准确恒等式为
$$
K_F|_C=e^3\mathcal F_F,\qquad
\mathcal F_F=\mathcal R-\mathcal P\log\psi,\qquad
\mathcal P=6(1-t)\delta^2-(1+2t)\delta .
\tag{5}
$$
这里只用已付的局部代数表达，不把正特征 log 延长过原共振。

## 2. 不除最高系数的整消去

置 $f=f_b$，定义
$$
\boxed{
H_{\rm top}=
b^2Y^{2b}\left\{
bf^2\mathcal R+
A\bigl(f\delta^2f-(\delta f)^2\bigr)
+Bf\delta f
\right\},
}
\tag{6}
$$
$$
\boxed{K_F^{\rm red}=K_F-FH_{\rm top}.}
\tag{7}
$$
(6) 属于 $\mathcal O[t,Y,d^{-1}]$，唯一显示分母至多为 $3d^2$。没有除以 $f$、$b$、$p$ 或任何依赖该因子的多项式。

**引理 1。** 整成立
$$
\boxed{
\deg_YK_F^{\rm red}\le3b-h_+,\qquad
Y^{h_-}\mid K_F^{\rm red},
\qquad K_F^{\rm red}|_C=K_F|_C.
}
\tag{8}
$$

**证明。** 原最高项为
$$
(K_F)_{3b}
=b^2f\left\{
bf^2\mathcal R+
A\bigl(f\delta^2f-(\delta f)^2\bigr)
+Bf\delta f
\right\}.
\tag{9}
$$
这是 R521 的最高系数式；(6) 使 $FH_{\rm top}$ 的最高项与它准确相同。

(4) 的每项在 $F$ 的系数及其 $\delta$ 导数中都是三次。除三个最高 charge $b$ 的组合外，任何存在的 charge 和至多为 $3b-h_+$。而 $FH_{\rm top}$ 除最高项外也至多具有该次数。这证明上界，不用其余系数之间的偶然抵消。

$\mathcal EF$、$\mathcal E^2F$ 及 $\mathcal E\delta F$ 都含 $Y^{h_-}$。因此 (4) 每项含该因子；$FH_{\rm top}$ 含 $Y^{2b}$，同样满足。最后一式由 (7) 得到。证毕。

单靠 $\bar F$ 的缺口不能声称任意给定整提升也有同样的 $h_\pm$。若要在整层使用指定缺口，应选择保持该支持的因子提升，或将 (3) 直接按所用整 $F$ 读取。R491 的逐系数角提升可将原零系数保为零：每个非零系数的有限角因子和无穷次数帽分别整提升，缺失的 charge 不参与该构造。因此在该篇已支付的乘积提升情形中，可以保持原模 $p$ 支持；不能将此选择与任意既定 $P^{\rm crit}$ 自动识别。

## 3. 原全部 Gauss 帽与十九个中间角

设 $T=f_bY^b$ 为真实最高单项。每个原角赋值都是逐 charge 的 Gauss 最小值，所以
$$
v(T)\ge v(F).
\tag{10}
$$
相同事实对十九个中间累计权逐项成立。特别在 R495 的原曲面 $X$ 上，若 $C$ 为 $F$ 的严格曲线，则
$$
T\in H^0(X,\mathcal O_X(C)).
\tag{11}
$$
这里使用 $F$ 的实际 ambient 帽和每一中间累计值；没有把 $T$ 的某个额外角零拿来缩小其它 charge 的条件。

将 (6) 写为
$$
H_{\rm top}=b^2\left\{
bT^2\mathcal R+A\bigl(T\delta^2T-(\delta T)^2\bigr)
+BT\delta T
\right\}.
\tag{12}
$$
R514 的原有限赋值因此给
$$
\boxed{
\begin{array}{c|ccccc}
v&v_0&v_{h_7}&v_1&v_d&v_\infty\\ \hline
v(H_{\rm top})-2v(F)\text{ 的下界}
&0&-8&-3&-4&-2\\
v(K_F^{\rm red})-3v(F)\text{ 的下界}
&0&-8&-3&-4&-2 .
\end{array}}
\tag{13}
$$
第二行由第一行、(7) 和原 $K_F$ 的同一界得到。减去 $FH_{\rm top}$ 没有制造新角极。

为明确所有中间角，保 R680 的固定极除子
$$
L=\pi^*F_\infty+2\pi^*F_d+
2D_{h_1}+2D_{h_2}+D_1,\qquad
D_\alpha=\sum_{j=1}^{e_\alpha}E_{\alpha,j}^*.
\tag{14}
$$
对 (12)，每个相对 $2C$ 的累计损失由下表覆盖：
$$
\begin{array}{c|c|c}
\text{链}&j&\text{可能极阶}\\ \hline
0,\ Y=\infty&1,\ldots,4&0\\
h_7\text{ 两根},\ Y=\infty&1,\ldots,4&2j\\
1,\ Y=\infty&1,\ldots,3&j\\
d=0,\ Y=0&1,2&2j\\
t=\infty,\ Z=t^4Y=0&1,2&j .
\end{array}
\tag{15}
$$
在非零有限角，$\delta$ 每次最多损 $j$；$A$ 在 $1$ 的零补回一份 $j$。$d$ 处的 $\mathcal R$ 最多损 $2j$。在无穷框 $T_0=1/t,\ Z=t^4Y$ 中，$\delta=-T_0\partial_{T_0}+4Z\partial_Z$，求导不增加极；$A,B,\mathcal R$ 的一次有理次数恰由最后一行支付。$0$ 处 $\delta$ 是对数导数。线束换框只加已含在这些界内的零阶项。

这逐一证明
$$
\boxed{
H_{\rm top}\in H^0(X,\mathcal O_X(2C+L)),\qquad
K_F^{\rm red}\in H^0(X,\mathcal O_X(3C+L)).
}
\tag{16}
$$
特别没有通过除 $f_b$ 来引入其非固定根上的极。

## 4. 两个真实边界的加强

记 $S_0^{\rm str}$、$S_\infty^{\rm str}$ 为原负、正截面的严格变换。它们只各经过已规定的第一吹起中心，不是将未吹起的截面类直接代入。

(8) 在两个截面的泛点准确给消失阶至少 $h_-$、$h_+$。结合 (16) 在所有其它素除子上的正规性，得到更强的全曲面截面：
$$
\boxed{
K_F^{\rm red}\in
H^0\!\left(
X,\mathcal O_X(3C+L-h_-S_0^{\rm str}-h_+S_\infty^{\rm str})
\right).
}
\tag{17}
$$
这是一个实际全局截面，较仅证明沿 $C$ 的边界消失更强。严格截面与例外曲线交会处也被包括：在光滑 $X$ 上，(16) 的截面减去已知素除子消失阶后，全部素除子赋值仍非负，故仍正规。

如果 $\bar F$ 是 R467/R680 范围内的 primitive 几何整因子，则原共振证明保证 $K_F|_C\ne0$，所以 (5)、(8)、(17) 给非零限制
$$
K_F^{\rm red}|_C\ne0.
$$
其总零长度上界准确为
$$
\boxed{
3C^2+LC-h_-(S_0^{\rm str}C)-h_+(S_\infty^{\rm str}C).
}
\tag{18}
$$
$C$ 不包含这两个截面，两个被减的交数均非负。

例如对 R680 同一实际接触点 $(0,\zeta)$，这些点避开两个截面，原局部能量不变。因此
$$
\boxed{
\sum_{\zeta}
\left\{
\sum_{\psi\mid F,\zeta}\min(h_\psi,s)+3\Delta_{F,\zeta}
\right\}
\le
3C^2+LC-h_-S_0^{\rm str}C-h_+S_\infty^{\rm str}C.
}
\tag{19}
$$
没有把 ODE 延长过 $s$。对实际多因子着色，R680 增补中的 $w(1)=1$、$w(m)=4(m-1)$ 原样保留，(19) 整体乘 $w(m_i)$ 后给
$$
\begin{aligned}
4q(H-r)\le{}&
3\mathscr C^2
-3\sum_i(m_i^2-w(m_i))C_i^2\\
&+\sum_iw(m_i)
\bigl(L-h_{i,-}S_0^{\rm str}-h_{i,+}S_\infty^{\rm str}\bigr)C_i.
\end{aligned}
\tag{20}
$$
其中 $\mathscr C=\sum_i m_iC_i$，各 $h_{i,\pm}$ 必须按该实际因子支持读取。若因子稳定子阶为 $h_i$，则 $h_{i,\pm}\ge h_i$，但不能将整个 $P$ 的 charge 最大公因数强加给每个单独因子。式 (20) 加强有限必要界；本文没有凭未控制的线性项宣布全部 $q=3$ 临界候选被排除。

## 5. 真实来源返回：一般加二，最高缺口三时同预算

保 R514 已付的实际立方来源
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,\qquad
D_0=3b+\deg_YQ\le D.
\tag{21}
$$
全部因子及乘积使用同一整提升；这是本节不可省略的来源假设。原固定乘子仍为
$$
\mathfrak m_3=Y^3t(t-1)^2h_7^3d^2.
\tag{22}
$$
其原 Gauss 值为 $(1,9,3,7,5)$。由 (13)，
$$
v(\mathfrak m_3K_F^{\rm red})\ge3v(F)
$$
在全部原角成立，且 $d^2$ 清掉唯一显示角分母。定义
$$
\boxed{
B_F^{\rm red}
=d^{-C_D}t^rQ\,\mathfrak m_3K_F^{\rm red}.
}
\tag{23}
$$

**定理 2。** 整成立
$$
\boxed{
B_F^{\rm red}\in\mathcal W_{D_0+3-h_+}.
}
\tag{24}
$$
因而：

- 对一般 $F$，$B_F^{\rm red}\in\mathcal W_{D_0+2}$；
- 若 $h_+\ge2$，它属于 $\mathcal W_{D_0+1}$；
- 若 $h_+\ge3$，它已经属于原同一 $\mathcal W_D$；
- 更一般，准确同预算门为 $D_0+3-h_+\le D$。

**证明。** (13)、(22) 给所有 Gauss 值至少为原 (21) 的相应值。(8) 给
$$
\deg_YB_F^{\rm red}\le D_0+3-h_+.
$$
它只允许原 $d$ 分母。R491/R514 的双向逐列判据
$$
v_0,v_{h_1},v_{h_2}\ge-2,\quad
v_1\ge-1,\quad v_d\ge0,\quad v_\infty\ge-8
$$
遂恢复每一列原 $q_n$ 及自由幂帽，得到 (24)。第三节同时支付全部十九个中间条件。整个证明没有改 $t^r$，没有除去原低前缀，也不需要 R514 的 $r\ge8$ 或 $4r-D\ge30$ 缓冲。证毕。

若在扩大后的 $\mathcal W_{D_0+3-h_+}$ 上调用另有 $f_N<p$ 假设的定理，仍须按其真实 $N$ 保该条件。(24) 本身只是整来源恒等式，不需要据扩大预算新增算术零。

尤其，若 (21) 的实际因子 $F$ 全支持于 $3\mathbb Z$，(24) 给同 $D$ 的真实返回。若仅知整个首核 $P$ 的支持同余模三，尚不能据此断定其每个因子具有这个性质，更不能无证写成 (21)。这两种范围不得混用。

## 6. 同一真实行必须保留的两个 normal 修正

记
$$
G=\mathfrak m_3K_F,\qquad
\mathcal H=\mathfrak m_3H_{\rm top},\qquad
G^{\rm red}=G-F\mathcal H.
$$
沿同一 $C$，令 $f_2=\mathcal E^2F|_C$。整恒等式给
$$
\boxed{
\begin{aligned}
G^{\rm red}|_C&=(\mathfrak m_3|_C)e^3\mathcal F_F,\\
\mathcal EG^{\rm red}|_C&=\mathcal EG|_C-e\,\mathcal H|_C,\\
\mathcal E^2G^{\rm red}|_C&=\mathcal E^2G|_C
-f_2\,\mathcal H|_C-2e\,\mathcal E\mathcal H|_C.
\end{aligned}}
\tag{25}
$$
这里 $\mathcal E\mathcal H$ 包括 (22) 的真实 charge 三，不能只求导 $H_{\rm top}$。

在 (24) 的同预算门内，取 R514/R498 已付的原真行
$$
\Phi=(A_0+B_0\zeta+C_0\zeta^2)
\frac{dt\wedge d\zeta}{\zeta^3}.
$$
按同一 $d^{-C_D}t^rQ$ 框和原低行消元读取，有
$$
\boxed{
\begin{aligned}
0=\operatorname{Res}_P\Big[
&\frac{A_0}{2}
\bigl(\mathcal E^2G|_C-f_2\mathcal H|_C
-2e\,\mathcal E\mathcal H|_C\bigr)\\
&+B_0\bigl(\mathcal EG|_C-e\mathcal H|_C\bigr)
+C_0(\mathfrak m_3|_C)e^3\mathcal F_F
\Big]dt .
\end{aligned}}
\tag{26}
$$
这是对 (23) 一条实际来源的完整三层读数。即使 $G^{\rm red}$ 已属同预算，$G$ 和 $F\mathcal H$ 仍可能只在较大预算内；不能将 (26) 拆为原左行分别杀掉它们，更不能单独留下最后一项。

在全部原有限 $\Gamma$ 中，有准确的评价恒等式
$$
J(B_F^{\rm red})
=
J(d^{-C_D}t^rQ\,G)
-J(d^{-C_D}t^rQF\mathcal H).
\tag{27}
$$
(27) 保乘积的完整真实 Taylor 展开，而不是将 $F=0$ 的值恒等式提升为模 $F^3$ 恒等式。特别 raw $\bar\Gamma$ 中仍可活着的第三次 normal 项、$U_1/p$、同一个低行右逆的高尾都不因此消失。

恢复 $M=c_*U_0m_{13}J$ 只作原整运输。$P_{134}$、charge 四十、十三自由行、两条十三行和同一个 $R$ 的下一位均不变。若原 $P_2=P+pR$ 已固定，仍须使用其原 $d_2$ 代表及 R651 的完整 $\Psi_R$；(25) 不是把两项 normal 修正丢掉后宣称 $d_2$ 不变的理由。新的返回支付一条可被原真行测试的明确来源，不给它新的完整中央零。

## 7. 为什么不能继续无代价除去下一最高项

令 $h=h_+$、$c=b-h$、$g=f_c$。模原最高系数理想 $(f)$，直接从 (4)、(6) 计算得
$$
\boxed{
(K_F^{\rm red})_{3b-h}
\equiv A\,h^2g\,(\delta f)^2
\pmod{f}
}
\tag{28}
$$
（在 $\mathcal O[t,d^{-1}]$ 中）。除最高项外的第一个可能 charge 必由两个 $b$ 和一个 $c$ 组成。模 $f$ 后，原三项分别留下
$$
-2Abc\,g(\delta f)^2,\qquad
Ac^2g(\delta f)^2,\qquad
+Ab^2g(\delta f)^2,
$$
最后一项来自减去 $FH_{\rm top}$；和正是 (28)。其余项含 $f$。

例如在剩余域中，若 $f$ 在非固定角 $t_0$ 有简单根，
$t_0\ne0,1$、$g(t_0)\ne0$，则 $h<p$ 使
$$
A(t_0)h^2g(t_0)(t_0f'(t_0))^2\ne0.
$$
此时下一系数不被 $f$ 整除。继续用 $F$ 的倍数消去它，通常须引入 $1/f$ 的新极，原角帽不再自动成立。(28) 不假定这样的根对每个实际 $F$ 都存在；它给当前整消去可被精确检查的边界。

R521 的最高边界残数并没有因此被证明消失于原余核：本篇减的是 $F\mathcal H$，不是 $F^3$ 的倍数。旧边界类和两个 normal 观察会按 (25) 同时改变。实际有限 jet 的余类仍要在原完整来源上判断。

## 8. 新增内容和继续接口

本篇完整支付：

1. 最高项消去的整二次表达，无最高系数分母；
2. 全十九角及原每列次数帽，返回成本 $D_0+3-h_+$；
3. 两个严格截面的真实消失阶及加强的实际根能量；
4. 同一真行上的完整两个 normal 修正和全 $\Gamma$ 乘积；
5. 下一最高项的确切非整除余式，防止无代价迭代。

原 $\bar E$ 的整高尾及其 R338 同一两尾作用保持原值。R651 的 $\mathcal G_P\in\operatorname{im}\bar{\mathcal D}_\psi$、两个十三行门和同 $R$ 的 $\Psi_R$ 仍需判定。本文没有从曲线上 forcing 非零、较低 charge 或边界消失推出这些指定原余类非零；主课题仍未完成。

依赖：[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md) 的整角提升与逐列返回；[R514](R514-cubic-forcing-return-and-actual-mirror-tail-normal-form.md) 的原三次式、乘子及完整真行；[R521](R521-exact-fixed-boundary-quotient-and-cubic-forcing-residue.md) 的最高系数及边界残数；[R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md) 和其着色增补的原十九角曲面与根能量；[R651](R651-original-higher-critical-branch-lift-and-complete-second-forcing.md)、[R687](R687-original-cm-three-digit-matrix-and-complete-same-correction-transport.md) 的同一个原修正、全部高尾与第三精度。

本篇为全参数恒等式和原来源证明；没有新增数值扫描或需保存的可重算数据。
