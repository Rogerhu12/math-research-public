# 围绕保存候选的完整连接根：不用统一小 $\eta$ 的误差门

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**状态：完整条件证明，待合入 R41 的后续一节。** 当前 R41 稳定清单正在由父会话收录，因此本稿独立保存，不改变已发 manifest 的文件 SHA。本稿没有执行新的数值工作。

## 1. 为什么保留这个接口

R41A 的 $\eta\leq1/32$ 是方便的输入充分门，不是精确连接根存在的必要条件。外侧 $0,\ldots,11$ 胞元的保存场已经有正 $D/S/\mathrm{leading}$ 的数值诊断；将来的连续证书应直接使用实际余量与残差，而不是在一个方便的小球失败后改动真实方程。

以下仍用 R41 的同一个完整连接方程，记

$$
z=w^2>0,\quad E=1+z,\quad
T=P_\theta,\quad S=1-zP^2,\quad
\Gamma=1+zG,\quad b=T/S,
$$

$$
A=\Gamma^2+zb^2,\qquad
R=\Gamma^2(1-EP^2)+2G+zG^2.
$$

给定实值候选 $\widehat K$，记 $\widehat y=1+\widehat K$，并定义 R41 的完整有限残差

$$
\mathcal E=(\Gamma^2S^2+zT^2)\widehat y^2
+2TS\widehat y-RS^2,
\qquad e=\mathcal E/S^2.
$$

所有范数在同一个 $W_{\tau,1}$ 中。候选含其 mean；完整根不会丢弃 mean 或高频。

## 2. 可核算的条件

假设

$$
s=\|zP^2\|<1,\qquad c=\|zG\|<1.
\tag{G.1}
$$

因此 $S$ 在 Wiener 代数中可逆，在实角上 $S>0,\Gamma>0$。设

$$
V=A\widehat y+b.
$$

选择一个真实常数 $v_*>0$，并支付

$$
d_V\geq\|V-v_*\|,\qquad
\nu=v_*-d_V>0,\qquad a\geq\|A\|.
\tag{G.2}
$$

其中这些量可只用有限多项式核算：

$$
V=
\frac{(\Gamma^2S^2+zT^2)\widehat y+TS}{S^2},
$$

所以可取

$$
d_V=
\frac{\|(\Gamma^2S^2+zT^2)\widehat y+TS-v_*S^2\|}
{(1-s)^2}.
\tag{G.3}
$$

类似可取
$a=\|\Gamma^2S^2+zT^2\|/(1-s)^2$，或取另一个更小但已证明的上界。令

$$
e_*=\frac{\|\mathcal E\|}{(1-s)^2},\qquad
\xi=\frac{a e_*}{\nu^2}<1,
\tag{G.4}
$$

以及

$$
\delta=\frac{e_*}{\nu(1+\sqrt{1-\xi})}.
\tag{G.5}
$$

对实角上的有限候选另支付下界

$$
\widehat y\geq y_0,\qquad
\widehat D=ES-z\widehat y^2\geq d_0,\qquad
\widehat N=1+zb\widehat y\geq n_0,\qquad
\widehat L=\widehat y+ET\geq\ell_0.
\tag{G.6}
$$

这些下界必须是全角下界。有限实 Laurent 多项式可用常数项减去非零模绝对和；允许更紧的有理全角或连续区间方法。对 $\widehat N$，也可用有限分子 $S+zT\widehat y$ 的正下界除以 $S$ 的正上界，不需要截断 $S^{-1}$。

最后要求

$$
\begin{aligned}
y_0&>\delta,\\
d_0&>z\delta(2\|\widehat y\|+\delta),\\
n_0&>z\|b\|\delta,\\
\ell_0&>\delta.
\end{aligned}
\tag{G.7}
$$

本门没有假设 $\eta\leq1/32$ 或 $\|\widehat K\|\leq1/16$。它用的是实际候选的正余量、Wiener 逆和真实残差。

## 3. 完整构造与证明

由 (G.2)，$V$ 在 Wiener 代数中可逆，且
$\|V^{-1}\|\leq1/\nu$，实角上 $V\geq\nu$。定义

$$
q=\frac{Ae}{V^2},\qquad \|q\|\leq\xi<1,
\qquad s_q=\sqrt{1-q},
\tag{G.8}
$$

其中根号由以 $1$ 为中心的完整二项级数定义。实角上 $q$ 为实数且 $|q|\leq\xi$，故 $s_q>0$。

定义

$$
K=\widehat K-\frac{e}{V(1+s_q)}.
\tag{G.9}
$$

函数

$$
\frac1{1+\sqrt{1-q}}
=\frac{1-\sqrt{1-q}}q
$$

在 $|q|<1$ 的幂级数具有非负系数，$q=0$ 处取连续值 $1/2$。因此

$$
\|(1+s_q)^{-1}\|
\leq\frac1{1+\sqrt{1-\xi}},
\qquad
\|K-\widehat K\|\leq\delta.
\tag{G.10}
$$

这个估计控制完整无限角频谱。

令 $y=1+K$、$\Delta y=y-\widehat y$。由
$e=A\widehat y^2+2b\widehat y-R$，

$$
Ay^2+2by-R=e+2V\Delta y+A(\Delta y)^2.
\tag{G.11}
$$

代入 (G.9)，利用 $1-s_q^2=q=Ae/V^2$，右端恒等于零。又

$$
Ay+b=V+A\Delta y=Vs_q>0
\tag{G.12}
$$

在实角上成立。这选中了二次式的上根分支，而不是另一个可能的代数根。

(G.7) 与 (G.10) 给出

$$
y>0,\qquad
D=ES-zy^2>0,\qquad
N=1+zby>0,\qquad
L=y+ET>0.
\tag{G.13}
$$

具体地，
$|D-\widehat D|\leq z\delta(2\|\widehat y\|+\delta)$，
$|N-\widehat N|\leq z\|b\|\delta$，
其余两项的变化至多 $\delta$。于是平方后的二次方程可恢复原连接恒等式

$$
\frac{1+zby}{\sqrt{ES-zy^2}}=\Gamma.
\tag{G.14}
$$

在这些正号条件下有

$$
Ay+b=\frac{\Gamma(y+ET)}{\sqrt D}.
\tag{G.15}
$$

该恒等式可由 (G.14) 直接化简，或比较
$\Gamma^2D-(1+zby)^2$ 对 $y$ 的导数。因此正 leading 分支等价于 (G.12) 的上根分支；对每个实角恰有一个该分支的根。构造在同一个 Wiener 代数内解析，保留实值与 $\pi$ 周期。

若 $G_0=0$，完整转角平均仍精确为 $1$；高度径向 mean 由新 $K_0$ 给出。全部 R41 单 cut Darboux/半周闭合/真实径向流等价仍可使用，前提仍是各自的径向正则性和误差条件，而不是把端点结果当成整个径向解。

## 4. 对后续实际工作的用法

对给定真实径向点或已经有同函数包络的整面板：

1. 用完整 $H$、同规范 $\Pi$ 与真实 $r,w,\mu$ 定义 $P,G$。
2. 用保存的 finite-root $L$ 定义候选 $\widehat K$，明确其所有系数的真实解释。
3. 以严格有限卷积核算 (G.1)–(G.4)；用候选的全角 $D/N/L$ 余量付 (G.6)–(G.7)。
4. 用 (G.10) 将候选强范数、mean、正分支转给完整根。

这条路径的结果仍然是角向代数认证。把 $r$ 上的候选导数代入 R41.41 得到径向残差并支付其完整 Green/非线性修正，是接合强前缀与深尾所需的下一层；当前没有数值账本声称这一层已经完成。
