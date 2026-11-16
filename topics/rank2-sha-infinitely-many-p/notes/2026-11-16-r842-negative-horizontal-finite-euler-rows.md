# R842 续注：真实负水平的一层 Euler 行、二重切点消去与二次值商

日期：2026-11-16。**状态：下列局部有限算子、实际残数系数和二次值商已证明；它们在原高前缀兼容核上的像仍未判定。**

本注接
[R842](../results/R842-original-gres-double-ramification-transpose-and-joint-prefix-extension.md)、
[第一层满射与实际受限类](2026-11-16-r842-first-layer-surjectivity-and-actual-restricted-class.md)
及
[完整边界读取](2026-11-16-r842-actual-boundary-rows-and-horizontal-thickenings.md)。
这里只处理原 $r=2$、$q=Y\widetilde q$ 分支的真实负水平分量。
保同一个 $q$、同一个 $G\in\mathcal H_3$、同一个
$R=qt^rG$；不将删去 mask 后的另一个 cube 替换原来源。

记
$$
C=(F=0),\quad e=\mathcal EF,\quad \mathcal E=Y\partial_Y,\quad
Z=(e|_C),\quad Z_-=C\cap H_-,
$$
$$
W=t^{r+1-s}(1-t)^{3s},\qquad c_s=\frac{3(-1)^s}{17}.
$$
指定边界代表仍是
$$
\mathcal D_R=c_s(\mathcal ER)|_C
\left[-d\left(\frac{WF_t}{e}\right)
+\frac{W'F_t+WF_{tt}}e\,dt\right].
\tag{1}
$$
各偏导保持原 $Y$ 固定。整个 $[b_0]$ 还含正水平、所有固定纤维、
十九角、conductor 和同一个 $P$ 项；本注不删除它们。

## 1. 光滑负水平分歧处，实际 $D_3$ 因子化到一层 $Z$

取一个不在六个固定底纤维上的光滑
$Q\in C\cap H_-$，并假设 $F_t(Q)\ne0$。
在剩余域 $k_Q$ 上用 $x=Y$ 作参数，写
$$
t=t_Q+O(x^m),\qquad
F_Y(t(x),x)=x^{m-1}v(x),\qquad v(0)\ne0.
\tag{2}
$$
原 $t$-映射的次数至多 $b<p$，所以 $1\le m<p$；
首导数没有特征 $p$ 的消失问题。
此时
$$
e|_C=x^m v(x),\qquad
Z_Q=\operatorname{Spec}k_Q[x]/(x^m).
$$
对任一实际 $G$，置 $V=G|_C$。完整链式法则给
$$
x\frac{dV}{dx}
=(\mathcal EG)|_C+x t'(x)G_t|_C
\equiv(\mathcal EG)|_C\pmod{x^m}.
$$
故原映射在此分量准确为
$$
\boxed{
(D_3V)|_{Z_Q}=D_x(V|_{Z_Q}),\qquad D_x=x\partial_x.
}
\tag{3}
$$
它不需要任选额外的 normal 值。矩阵在 $1,x,\ldots,x^{m-1}$
上是 $\operatorname{diag}(0,1,\ldots,m-1)$，全部正特征值是单位。
相同推导对同一个 $\mathcal EG$ 再用一次，给
$$
(\mathcal E^2G)|_{Z_Q}=D_x^2(V|_{Z_Q}).
\tag{4}
$$
因此原兼容对必满足 $V_1=D_xV_0$ 于 $Z_Q$；第二值若实现，
则 $V_2=D_x^2V_0$ 于同一 $Z_Q$。
这是一层的局部身份，不将一般分歧处的 $D_3$ 从 $2Z$ 免费降到 $Z$，
也不将它延伸到奇点。

## 2. 指定边界只读该真实一层，最高 jet 的系数为单位

令
$$
J(x)=x\,\widetilde q(t(x),x)G(t(x),x)
=\sum_{\ell\ge1}J_\ell x^\ell,\qquad
A(x)=\frac{W(t(x))F_t(t(x),x)}{v(x)}.
$$
$A$ 是单位。完整边界注的固定 $t$ 偏导公式准确化为
$$
\boxed{
\operatorname{Res}_Q\mathcal D_R
=c_s t_Q^r
\sum_{\ell=1}^{m}\ell^2J_\ell A_{m-\ell}.
}
\tag{5}
$$
证明中的精度不能略过：$J_t$ 含因子 $x$，
而 $t'(x)$ 的阶是 $m-1$；
因此原固定 $t$ 的 $J_x$ 与总导数 $J'(x)$ 相差 $O(x^m)$。
$t(x)^r-t_Q^r$ 也在 $(x^m)$。
在原所读的 $x^{m-1}$ 行，两项都不贡献。
最后
$$
-[x^{m-1}]J'(x)(xA'(x)-mA(x))
=\sum_{\ell=1}^m\ell^2J_\ell A_{m-\ell}.
$$
这给正号和全部系数，而非只保首项。

等价地，置
$\widetilde q_C=\widetilde q(t(x),x)\bmod x^m$，则
$$
\boxed{
\operatorname{Res}_Q\mathcal D_R
=c_s t_Q^r[x^{m-1}]
A(x)(D_x+1)^2\bigl(\widetilde q_C V\bigr)
\pmod{x^m}.
}
\tag{6}
$$
这里 $(D_x+1)^2$ 在整个实际 $Z_Q$ 上可逆：
其特征值是 $1^2,\ldots,m^2$，均非零。
若再有 $\widetilde q(Q)\ne0$，
(6) 作为整个 $H^0(Z_Q,N^3)$ 上的行非零，
其 $V=x^{m-1}$ 的系数准确是
$$
\boxed{c_s t_Q^r\,m^2 A(0)\widetilde q(Q)\ne0.}
\tag{7}
$$
全部 $q$ 的高 $Y$ 系数仍在 $\widetilde q_C$ 中；
没有以 $q(0,Y)=c_qY$ 推断 $\mathcal Eq=q$。

(7) 不证明该列由 $\mathscr W_T$ 提供。
真实 $V_0$ 还须同时有 $T$ 阶前缀，且其唯一伴随 $V_1$
也有该前缀；(3) 没有支付这样的全局延拓。
所以它也不证明原 $[b_0]$ 或更小三长核上的行非零。

## 3. 光滑的二重水平切点反而整项消失

现在取另一个非固定光滑负水平点，假设 $F_Y(Q)$ 为单位，
并以 $v=t-t_Q$ 为参数。令
$$
\operatorname{ord}_QY=n\ge2.
$$
则原 $q=Y\widetilde q$ 给
$\operatorname{ord}_Q(\mathcal ER)\ge n$。
沿曲线有
$$
\frac{WF_t}{e}=-W\,\frac{Y'(v)}{Y(v)}.
$$
右端至多简单极，所以其微分至多二阶极；
乘 $\mathcal ER$ 后正则。
(1) 第二项则可直接约去已付的 $Y$：
$$
\frac{(\mathcal ER)(W'F_t+WF_{tt})}{YF_Y}\,dv
=
t^r(\widetilde qG+Y\partial_Y(\widetilde qG))
\frac{W'F_t+WF_{tt}}{F_Y}\,dv,
$$
也是正则。因此
$$
\boxed{\operatorname{Res}_Q\mathcal D_R=0.}
\tag{8}
$$
这里 $W$、$q$ 的其余系数都在该非固定点正则。

特别在原 $\deg H=2$ 且 $H$ 为一个二重根时，
若对应曲线点光滑并且该根不在固定底纤维，
该点是 $n=2$ 的水平切点，整个负水平分量由 (8) 消失。
不能把它改成两个单位点值。

奇点不属于 (8)。例如在非固定点的局部坐标 $v=t-t_Q$ 中，
普通节点的二次首部
$F=v^2+\alpha vY+\beta Y^2$（$\beta\ne0$、判别式非零）
有两条支；若 $q=Y$、$G=1$，
(1) 的两支残数和首贡献为
$c_s t_Q^rW(t_Q)\alpha/\beta$。
它不必为零。这个局部计算仅说明为何必须保奇点与 conductor，
不是声称这个局部模型已经是原强接触候选。

## 4. 原 $\deg H=2$ 横截情形的准确二次行

R797 对原未改变的 $q$ 给
$$
F_0=\lambda d^cH,\quad \deg H=2,\quad
A_1=\lambda^3d^{3c}\widetilde q(t,0)\in k^\times,
\quad d=1+8t.
\tag{9}
$$
这里 $c=\operatorname{ord}_dF_0$、$(H,d)=1$，准确沿 R797 §1(4)。
R833 §1(1)–(2) 的原负水平限制给
$F_0/d^{\mu_{d,1}}=\lambda d^{c-\mu_{d,1}}H\in k[t]_{\le z_-}$，
其中 $c\ge\mu_{d,1}$；故
$z_-\ge c-\mu_{d,1}+\deg H\ge2$。
再由 R833 §4(11) 的 $z_-\le2$，准确迫出

$$
z_-=2,\qquad \mu_{d,1}=c,\qquad
\mu_{\infty,1}=u-c-2.
\tag{10}
$$
两个移动根计重已经耗尽负水平的全部交数，
没有额外的固定角或无穷远负水平点。
若 $H(0)=0$，该根本身仍位于固定纤维，不能使用本节的
$W$ 单位公式；下面明确排除这种情形。

设 $H=t^2+h_1t+h_0$ 平方自由，所有根均非固定，
并且 $f_1=F_Y(t,0)$ 在这些根上为单位。
这容许 $H$ 在 $k$ 上不可约。
对原 $G\in\mathcal H_3$，全部十九角准确给
$$
G(t,0)=d^{3c}g_0(t),\qquad \deg g_0\le6.
\tag{11}
$$
在实际有限代数 $\mathcal A=k[t]/H$ 中定义
$$
\boxed{
K_H=
\frac{c_sA_1}{\lambda^2}
\frac{t^rW\,d^c(H')^2}{f_1}\pmod H.
}
\tag{12}
$$
(12) 的所有分母都是 $\mathcal A$ 的单位；
$K_H$ 本身也是单位。
把完整剩余域迹纳入后，全部负水平残数准确是
$$
\boxed{
\mathfrak b_-(G)
=\sum_{H(\alpha)=0}\operatorname{Res}_{(t,Y)=(\alpha,0)}
\mathcal D_R
=[t]\bigl(K_H g_0\bmod H\bigr).
}
\tag{13}
$$
证明是将完整边界注 (14) 的横截值式代入 (9)、(11)，
再使用 monic 二次多项式的原 Lagrange 留数
$$
\sum_{H(\alpha)=0}\frac{P(\alpha)}{H'(\alpha)}
=[t](P\bmod H).
$$
因此所有常数、$d$ 次数和原 $F_Y$ 均保留。
不可约二次情形是同一剩余域迹，不是任意指定两个点。

若 $K_H=k_0+k_1t$、$g_0\bmod H=a_0+a_1t$，
(13) 就是显示行
$$
\boxed{\mathfrak b_-(G)=k_1a_0+(k_0-h_1k_1)a_1.}
\tag{14}
$$
它在整个实际二次值商上非零，核恰为一维。
对真实兼容高前缀核，
只能将 (14) 限制到原
$\mathscr W_T\to H^0(Z_-,N^3)$ 的实际像；
本注没有证明这个像是整个二次商，甚至没有预设它非零。
正水平、十九角及同一个原点补偿也仍参与 $[b_0]$。

## 5. 原物理范围保持

本注只简化指定全局边界式中的一个真实分量。
$\mathscr W_T$、其唯一 $V_1$、原第二值 $V_2$、
同一个 $cF^3$ 尾和最后短行都依 R836/R840 保留。
物理长窗仍为 $T=s-r-13$，不是 $s-r$；
公共 $G_0=w^{13}U_0$、原 $P_{134}$、同一个首次修正及全部 carry
均未改变。奇点和固定底纤维按完整边界注继续读取。

本注没有增加中央零，没有另造全局来源，
也没有由局部单位行推断原 forcing 非零。
