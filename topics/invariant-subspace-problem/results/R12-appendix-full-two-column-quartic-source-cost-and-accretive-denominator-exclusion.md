# R12 附录：原平方方程的完整前两列、纯尾四次费用及增生分母排除

日期：2026-11-29（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的原算子来源不等式。** 对实际有界交换子方程 $Y^2=CP^2$，本文保留一个完整 dyadic 头后的全部尾算子，证明前两列给出的四次费用。若分母是纯尾 $I\otimes Q$，得到
$$
\boxed{\|Q^4\|\le
28\,\eta_{L-1}\|Y\|^4/\|C\|^2.}
\tag{1}
$$
因此[新头尾单位稿](R12-appendix-accretive-denominator-exact-tail-ranges-and-same-numerator-logarithmic-fees.md)的增生复杂分母 $P_\theta=Z^{-\theta}$，对每个 $\operatorname{Re}\theta>0$，都没有有界分子 $Y^2=CP_\theta^2$。这是该实际分母族的完整排除，不排除一般平坦分母或任意未知旗商上的闭根。

## 1. 原权、完整有限头与尾系数

固定原 Haar 尾 $C=A^{(m_0)}$，$m_0\ge0$。在本文只用
$$
w_j=\alpha_{m_0+j},\qquad c=w_0=\|C\|,\qquad
\eta_j=w_{j+1}/w_j,\qquad
\beta_r=\prod_{h=1}^r w_{v_2(h)},\qquad \beta_0=1
\tag{2}
$$
表示物理权；不把 $w_j$ 与增生行系数 $(j+1)^{-1}$ 混用。原权有
$$
0<\eta_j\le\eta_*<1/4.
$$

固定 $L\ge1$，令 $D=2^L$，$B=A^{(m_0+L)}$。原有限头的准确式为
$$
C=J_L\otimes I+e_{0,D-1}\otimes B,\qquad
C^D=\beta_{D-1}I_D\otimes B.
\tag{3}
$$
其中 $J_Le_r=w_{v_2(r+1)}e_{r+1}$，$0\le r<D-1$。末边 $B$ 完整保留，$\|B\|=w_L$，没有将它删成幂零模型。

[全交换子有限头展开](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md) §1 给每个 $X\in C'$ 唯一表示
$$
X=\sum_{r=0}^{D-1}C^r(I_D\otimes X_r),
\qquad X_r\in B',
\qquad
\|X_r\|\le\|X\|/\beta_r.
\tag{4}
$$
最后的界来自真实第一列 $X_{r0}=\beta_r X_r$。原 R24 的全尾交换性表明 $B'$ 为交换代数，所以以下所有尾系数都彼此交换。这里只把 $C$ 记作代数变量 $z$，以
$$
z^D=b,\qquad b=\beta_{D-1}B
\tag{5}
$$
约简有限乘积。这个记号完全等于 (3)–(4) 的原算子乘法，不是向尾字符取值。

## 2. 两个精确反转和全部费用

$r\in\{0,\ldots,D-1\}$ 时，原二进位反转给
$$
\beta_{D-1}=\beta_r\beta_{D-1-r}.
\tag{6}
$$
因为 $v_2(D-h)=v_2(h)$，等式右侧第二段正是第一段后的完整反向权积。

对 $1\le r<D$，进一步有
$$
\frac{\beta_{D-1}}{\beta_r\beta_{D-r}}
=\frac1{w_{v_2(r)}}.
\tag{7}
$$
对 $2\le r<D$，则有
$$
\frac{\beta_{D-1}}{\beta_r\beta_{D+1-r}}
=\frac1{w_{v_2(r)}w_{v_2(r-1)}}.
\tag{8}
$$
在 (8) 的两下标中恰有一个为 $0$。

置
$$
\tau_L=w_L\sum_{j=0}^{L-1}\frac{2^{L-j-1}}{w_j},
\qquad
\rho_L=2w_L\sum_{j=1}^{L-1}\frac{2^{L-j-1}}{w_j}.
\tag{9}
$$
$L=1$ 时第二和为空，$\rho_1=0$。按 $v_2(r)$ 计数，(7) 的完整和恰给 $\tau_L/w_L$；(8) 的完整和恰给 $\rho_L/(cw_L)$。偶数 $r$ 与其后的奇数 $r+1$ 成对，所以 (8) 确有因子 $2$。

由于
$$
\frac{w_{L-1}}{w_{L-1-h}}\le\eta_*^h,
$$
有
$$
\tau_L
=\eta_{L-1}\sum_{h=0}^{L-1}
2^h\frac{w_{L-1}}{w_{L-1-h}}
\le\frac{\eta_{L-1}}{1-2\eta_*}
\le2\eta_{L-1},
\qquad
0\le\rho_L\le2\tau_L.
\tag{10}
$$
这一步消去了全部巨大 $\beta_r^{-1}$；不能分别粗估它们后丢掉 (6)。

## 3. 一般原双源方程的对角四次界

设
$$
Y,P\in C',\qquad Y^2=CP^2,\qquad
M=\|Y\|,\quad K=\|P\|.
\tag{11}
$$
按 (4) 写其尾系数为 $A_r,D_r$。定义实际尾算子
$$
E_0=b\sum_{r=1}^{D-1}A_rA_{D-r},
\qquad
E_1=b\sum_{r=2}^{D-1}A_rA_{D+1-r},
$$
$$
F_0=b\sum_{r=0}^{D-1}D_rD_{D-1-r},
\qquad
F_1=b\sum_{r=1}^{D-1}D_rD_{D-r}.
\tag{12}
$$
空和仍取 $0$。准确比较 (11) 的系数 $z^0,z^1$ 得
$$
A_0^2=F_0-E_0,\qquad
D_0^2=2A_0A_1+E_1-F_1.
\tag{13}
$$
例如 $zP^2$ 的常数项来自 $z^{D-1}$ 乘 $z$ 后的完整回绕，正是 $F_0$；其一次项是 $D_0^2+F_1$。这两项均未省略。

由 (4)、(6)–(9)，
$$
\|E_0\|\le\tau_LM^2,\qquad
\|E_1\|\le\rho_LM^2/c,
$$
$$
\|F_0\|\le D w_L K^2,\qquad
\|F_1\|\le\tau_LK^2.
\tag{14}
$$
设
$$
e_L=\rho_LM^2/c+\tau_LK^2.
$$
所有尾系数交换，平方 (13) 第二式、代回第一式，并用
$\|A_0\|\le M$、$\|A_1\|\le M/c$，得到完整的原来源界
$$
\boxed{
\|D_0^4\|
\le
\frac{4M^2}{c^2}(D w_L K^2+\tau_LM^2)
+\frac{4M^2}{c}\,e_L+e_L^2.
}
\tag{15}
$$
$D_0$ 是同一 $P$ 在当前原有限头的真实常数尾系数，不是任意另选的源，也不是标量喷射。

(15) 只控制这个四次方；一般不能从它反推 $\|D_0\|$ 小，亦不由此宣称 $P$ 属于某个新的有界主理想。

## 4. 纯尾分母给完整四次费用

现在假设分母准确为
$$
P=I_D\otimes Q,\qquad Q\in B'.
\tag{16}
$$
即 $D_0=Q$ 而 $D_r=0$（$r\ge1$）。因此 $F_0=F_1=0$，(13) 化成
$$
A_0^2=-E_0,\qquad Q^2=2A_0A_1+E_1.
$$
平方第二式的完整同源身份为
$$
Q^4=-4E_0A_1^2+4A_0A_1E_1+E_1^2.
\tag{17}
$$
据 (14)，
$$
\boxed{
\|Q^4\|
\le\frac{M^4}{c^2}
(4\tau_L+4\rho_L+\rho_L^2).
}
\tag{18}
$$
再用 (10) 及 $\eta_{L-1}<1/4$，
$$
4\tau_L+4\rho_L+\rho_L^2
\le12\tau_L+4\tau_L^2
\le24\eta_{L-1}+16\eta_{L-1}^2
\le28\eta_{L-1}.
$$
这证明 (1)。特别，只要 $\|Q^4\|\ge1/2$，任何这样的实际分子都满足
$$
\boxed{
\|Y\|\ge
\sqrt c\,(56\eta_{L-1})^{-1/4}.
}
\tag{19}
$$
这里没有对 $Q$ 求逆、没有假定其像闭，也没有将压缩逆与完整逆交换。$L=1$ 的 $\rho_1=0$ 自动给更紧的真实首位界。

## 5. 整族增生复杂分母均无平方分子

回到前稿的同一
$$
Z=I+\sum_{j\ge0}(j+1)^{-1}V_j,\qquad
P_\theta=Z^{-\theta},\qquad
\operatorname{Re}\theta>0.
$$
假设存在一个有界 $Y\in C'$ 满足
$$
Y^2=CP_\theta^2.
\tag{20}
$$
由已付头尾单位，任意 $L$ 都有同一 $U_L$ 及准确来源
$$
Y_L=YU_L^\theta,\qquad
Y_L^2=CQ_{\theta,L}^2,\qquad
Q_{\theta,L}=I_{<L}\otimes(Z^{[L]})^{-\theta}.
\tag{21}
$$
对固定整数 $m>\operatorname{Re}\theta$，
$$
\|Y_L\|\le
\|Y\|\bigl(1+3D_{\theta/m}(1+\log L)\bigr)^m.
\tag{22}
$$
另一方面 $Q_{\theta,L}\to I$ 强*，且一致有界，故
$Q_{\theta,L}^4\to I$ 强*；特别充分大 $L$ 时 $\|Q_{\theta,L}^4\|\ge1/2$。范数与其纯尾因子的范数相同。

(19)、(22) 矛盾。具体地，[原径向权](R9-radial-odometer-and-nilpotent-approximants.md) (1.7) 给
$$
-\log\eta_{L-1}
=
1400\,16^{m_0+L-1}
-630\,8^{m_0+L-1}
+300\,2^{m_0+L-1},
\tag{23}
$$
因此任意固定 $k$ 都有
$\eta_{L-1}(1+\log L)^k\to0$。将 (22) 直接代 (1) 也会使
$\|Q_{\theta,L}^4\|\to0$，与强极限 $I$ 冲突。

于是
$$
\boxed{
\text{对每个 }\operatorname{Re}\theta>0，
\text{不存在有界 }Y\in C'\text{ 满足 }Y^2=CP_\theta^2.
}
\tag{24}
$$
这里包括全部复参数，而不只是原正实分数幂。

## 6. 真闭根域的对应排除及范围

设 $S$ 是原 $C$ 的稠密闭稳定根：
$$
D(S^2)=D(S),\qquad S^2x=Cx\quad(x\in D(S)).
\tag{25}
$$
那么不存在 $\operatorname{Re}\theta>0$ 使
$$
\operatorname{Ran}P_\theta\subset D(S).
\tag{26}
$$

若 (26) 成立，$Y=SP_\theta$ 全域闭，故有界。由 (25)，$D(S)$ 保持于 $C$，且 $SC=CS$ 在该域成立。[R88 的原全交换子多项式强逼近](R88-riesz-basis-bounded-multipliers-strong-closure.md)作用于闭图 $\Gamma S$，故每个 $F\in C'$ 都保持该图，即
$F(D(S))\subset D(S)$、$SF=FS$ 在 $D(S)$ 上。特别 $P_\theta$ 与 $S$ 实际域交换，进而
$$
Y\in C',\qquad Y^2=CP_\theta^2,
$$
与 (24) 矛盾。

这排除的是 (26) 的实际像包含，不能把前稿
$D((I+\mathcal N)^k)\subset\operatorname{Ran}P_\theta$
倒置后声称排除所有包含有限孔向量的根域。

本文还没有：
- 证明一般平坦 $P$ 不存在平方分子；
- 将 (15) 的四次范数界反转成 $D_0$ 的范数界；
- 将原全空间的有限头代数强加给任意未知旗商；
- 给出原普通不变子空间，或证明其不存在。

后继实际分母必须继续支付同分子的来源，不能只因“平坦、全旗准亲和、有强单位”而认为平方根费用已付。普通 ISP 未完成。
