# R297 — 新 j=0 原来源的唯一质量核、真实 CM7 乘积与完整三次角多项式

日期：2026-11-13。**状态：以下完整 CM13 迹矩阵、原实际来源的唯一识别、准确四次多项式、全部固定挠点零除子、真实 CM7 theta 乘积及原角表达均已证明。这里识别的是 R290 的原 Schwartz 特征线，不是一个仅有相同次数的候选。主目标所需的跨素数中央非零尚未证明。**

R292 已将原来源准确放入 $H^0(E,\mathcal O(34O))$，付出 Hermite/sigma 的全部 Gaussian，证明其实际 $\mu_6$ 不变性及原点质量零。本篇使用这个已付来源继续，而不重新选择 theta 幂。

## 1. 结论与原归一

写
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
\delta=\sqrt{-3},\quad \omega=(-1+\delta)/2,
$$
$$
\gamma_{13}=4+\omega=(7+\delta)/2,\qquad
\gamma_7=3+\omega=(5+\delta)/2.
\tag{1}
$$
Weierstrass 规范为 $x=z^{-2}+\cdots,y=-z^{-3}+\cdots,\sigma=z+\cdots$。

**定理 1。** R290 的实际来源线中，唯一满足 $[z^6]S=1$ 的来源准确为
$$
\boxed{
S(z)=\frac17\sigma^{34}x^2
\bigl(7x^{12}-53b x^9-12b^2x^6-80b^3x^3-128b^4\bigr).
}
\tag{2}
$$
因此它在原点恰好六阶消失，而不只是至少六阶。其 CM13 原始迹本征值准确为
$$
\boxed{M_{\gamma_{13}}S=-\gamma_{13}S,
\qquad M_\gamma=[\gamma]_*[\bar\gamma]^*.}
\tag{3}
$$
“原始迹”不含额外除 $13$、未写明的 Weil 标量或 Euler 因子。

本篇的首项一规范与 R290 原 Hermite 函数之间仍有一个固定非零整体常数和 R292 已显示的固定参数尺度。该常数由原全权范数公式另行保留；(2) 不把它无证设成一。来源线及原点六阶非零则已经完全确定。

## 2. 两个真实 sigma division 多项式

先在 $E_b$ 上证明准确式
$$
\boxed{
\frac{\sigma(\gamma_{13}z)}{\sigma(z)^{13}}
=\gamma_{13}\left(x^6+(2+6\delta)b x^3
 +\frac{40+24\delta}{13}b^2\right)=:Q_{13}(x),
}
\tag{4}
$$
$$
\boxed{
\frac{\sigma(\gamma_7z)}{\sigma(z)^7}
=\gamma_7\left(x^3+\frac{-2+6\delta}{7}b\right)=:Q_7(x).
}
\tag{5}
$$
两条共轭式将 $\delta$ 改成 $-\delta$。

这些比值是实际椭圆函数。事实上在 equianharmonic 格上准周期具有反线性形式 $B\bar\lambda$，所以分子、分母的指数准周期由 $\gamma\bar\gamma=\operatorname N\gamma$ 完全抵消；奇范数的半特征也相同。比值是偶函数，在 $\mu_3$ 下不变，唯一的极在 $O$，阶数分别为十二和六。因此它们必分别为 $x^6,x^3,1$ 和 $x^3,1$ 的组合。

为确定全部系数，由原微分方程直接得到
$$
x=z^{-2}-\frac b7z^4+\frac{b^2}{637}z^{10}+\cdots,
$$
$$
\log\frac\sigma z=\frac b{210}z^6-\frac{b^2}{84084}z^{12}+\cdots.
\tag{6}
$$
把 $z$ 改成 $\gamma z$，再减去 $\operatorname N\gamma$ 倍的原式，比较足够的两项或三项，便得到 (4)、(5)。这是有限维极空间中的完整确定，不是截断后猜测恒等式。

对 (4) 求两次对数导数，准确有
$$
x(\gamma z)=\frac1{\gamma^2}
\left(13x-\partial_z^2\log Q_{13}(x)\right).
\tag{7}
$$
在 $b=1$ 的同源缩放模型上，令 $Q=Q_{13}$，则右边的分子、分母为
$$
\begin{aligned}
N_\gamma&=13xQ^2
-4(x^3+1)(Q''Q-(Q')^2)-6x^2Q'Q,\\
D_\gamma&=\gamma^2Q^2.
\end{aligned}
\tag{8}
$$
这里的撇号是 $\partial_x$。约去真实公因子后，次数准确为十三和十二。共轭式给 $x(\bar\gamma z)$，下节在全部纤维中保留 (4) 的 leading constant $\gamma$。

## 3. 保留质量列的完整六维 CM13 矩阵

在 $b=1$ 模型上，取
$$
e_j=4^{-j}\sigma^{34}x^{2+3j},\qquad 0\le j\le5.
\tag{9}
$$
它们是实际偶 $\mu_3$ 不变空间的完整六维基。最后一列 $e_5$ 的原点值为 $4^{-5}$；前五列原点值为零。不能在计算迹算子前删掉这一质量列。

在这组基中，原始迹的准确矩阵为
$$
\boxed{\widehat M=\frac{A+\delta B}{13122},}
\tag{10}
$$
其中
$$
A=\begin{pmatrix}
-14805&-2304&432&-720&495&41310\\
-84672&-24417&5796&-4050&-9252&479043\\
10296&-137538&46782&-5085&-23517&1114299\\
-285642&-161334&46710&-1071&40698&3550365\\
275265&-50634&-2817&8775&-18999&1398420\\
-450&378&-90&72&162&12510
\end{pmatrix},
$$
$$
B=\begin{pmatrix}
-13165&1840&-514&250&275&-91970\\
-149792&35315&-6608&2300&424&77843\\
-321646&81046&-20680&10435&9737&1752343\\
349454&-57650&23714&-3377&23234&2345473\\
139873&-23554&6469&1157&2107&-718828\\
-3370&262&2&40&-118&-200
\end{pmatrix}.
$$

给出完整的原迹计算。设目标横坐标为 $a$，令
$$
f_a=(N_\gamma-aD_\gamma)^{\rm monic},\qquad
x_b=N_{\bar\gamma}/D_{\bar\gamma}\quad\text{于 }K[x]/(f_a).
$$
若输入为 $\sigma^{34}P(x)$，则输出除以目标 $\sigma^{34}$ 的准确值是
$$
\boxed{
\operatorname{Tr}_{f_a}
\left[(Q_{\bar\gamma}/Q_\gamma)^{34}P(x_b)\right].
}
\tag{11}
$$
这是 $[\gamma]$ 全部十三个逆像的迹。偶性使这十三个 $x$ 根恰好编码所需十三个点，不额外除二。其 sigma frame 比来自
$\sigma(\bar\gamma w)/\sigma(\gamma w)=Q_{\bar\gamma}(x(w))/Q_\gamma(x(w))$，所以全部 carrier 指数为 $34$。

对首一 $f_a$，(11) 可准确计算为
$$
[x^{12}]\left(\bigl[(Q_{\bar\gamma}/Q_\gamma)^{34}P(x_b)\bigr]f_a'\bmod f_a\right).
\tag{12}
$$
六个固定目标 $a=2,3,4,5,6,7$ 逐列确定矩阵，另一个完整纤维 $a=8$ 验证全部六列。所有纤维可分、所用分母在商环中可逆。

计算足以确定全局算子，是因为真实 pull/trace 保持 degree-$34$ 正截面，并与偶性及 $\mu_3$ 作用交换；输出必在 (9) 中。六个求值构成非零 Vandermonde 矩阵 $4^{-j}a^{2+3j}$。因此 (10) 是完整来源矩阵，未用几个局部系数替代整个迹。

## 4. 原来源的唯一质量核

记 $\ell=(0,0,0,0,0,1)$，构造
$$
\mathcal O=\begin{pmatrix}
\ell\\ \ell\widehat M\\ \ell\widehat M^2\\
\ell\widehat M^3\\ \ell\widehat M^4\\ \ell\widehat M^5
\end{pmatrix}.
\tag{13}
$$
$4^{-5}\ell$ 才是 (9) 的原质量；这里只在求其零核时约去固定非零因子。

精确计算给
$$
\boxed{\operatorname{rank}\mathcal O=5,\qquad
\ker\mathcal O=K\cdot(-2,-5,-3,-53,28,0)^{\mathsf t}.}
\tag{14}
$$
一个直接的非零证书是 (13) 前五行及第 $0,1,2,3,5$ 列的子式：
$$
-\frac{32(993727+2945775\delta)}{3^{21}}\ne0.
\tag{15}
$$
又由 (10) 逐项相乘，(14) 的向量满足
$$
\widehat M(-2,-5,-3,-53,28,0)^{\mathsf t}
=-\frac{7+\delta}{2}(-2,-5,-3,-53,28,0)^{\mathsf t}.
\tag{16}
$$
这也给出秩不超过五及原始本征值；无需预猜相位。

现在连接实际来源。R290 原二、三、十七处向量都在整个所指定紧环面的本征线上。对 $\gamma_{13}/\bar\gamma_{13}$ 也成立；十七处其约化为 $g_0^{14}$，而非任意假设成单位特征。真实代数算子 (11) 在原 theta 结构上实现相同的 Heisenberg 自同构，故与该有限 Weil 算子只差一个共同非零标量。于是实际来源 $S$ 是 (10) 的某条本征线。

这里“只差标量”可直接用 Heisenberg 协变与不可约性证明：pull/trace 将每个真实 $34$ 挠平移送到 $\gamma/\bar\gamma$ 所指定的平移，整个 Heisenberg 表示不可约；(10) 非零，故相应 intertwiner 非零。无需事先确定此标量，也无需从未经定标的裸 Weyl 矩阵读取本征值。

R292 已证明实际 $S\ne0$、$S(0)=0$。因此对每个 $k$，其坐标向量属于 $\ker(\ell\widehat M^k)$，从而必须是 (14) 的唯一一条线。换回未缩放的基并归一 $x^{14}$ 的系数为一，就得到
$$
\left(-\frac{128}7,-\frac{80}7,-\frac{12}7,-\frac{53}7,1,0\right).
$$
最后以 $E_b\simeq E_1$ 的固定六次缩放返回 $b=17$。首项一规范满足
$S_b(z)=b^{-1}S_1(b^{1/6}z)$，正得到 (2)、(3)。定理 1 得证。

## 5. 排除 CM13 猜测，识别真正的 CM7 乘积

先前符合次数及原点阶的 CM13 候选
$\sigma^8x^2\sigma(\gamma_{13}z)\sigma(\bar\gamma_{13}z)$ 并不等于实际来源。
由 (4)，它在 $b=1$ 的角多项式为
$$
P_{13}^{\rm cand}=13x^{14}+52x^{11}+1536x^8+1024x^5+256x^2.
$$
用 (11) 的两个完整纤维计算，
$$
\left.\frac{M_\gamma P_{13}^{\rm cand}}{P_{13}^{\rm cand}}\right|_{x=2}
=1+2\delta,
$$
$$
\left.\frac{M_\gamma P_{13}^{\rm cand}}{P_{13}^{\rm cand}}\right|_{x=3}
=\frac{-47003651+56705429\delta}{18159794}.
$$
其差为 $(65163445-20385841\delta)/18159794\ne0$，所以候选甚至不是任何标量的原 $M_\gamma$ 本征向量。

实际多项式则有准确因式
$$
\boxed{
7X^4-53bX^3-12b^2X^2-80b^3X-128b^4
=(X+b)(X-8b)(7X^2-4bX+16b^2).
}
\tag{17}
$$
由 (5)，最后的因子是
$$
Q_7(x)Q_{\bar7}(x)=7x^6-4b x^3+16b^2.
$$
因此真正的来源乘积为
$$
\boxed{
S=\frac17\sigma^{20}x^2y^2(x^3-8b)
\sigma(\gamma_7z)\sigma(\bar\gamma_7z).
}
\tag{18}
$$
它不是根据总次数猜出的乘积，而是由原矩阵唯一确定 (2) 后才因式分解得到。

用 R288 的原 $\theta_\pm$，还可完全等价地写成
$$
\boxed{
S=\frac1{28}\sigma(z)^2\sigma(2z)^2
\theta_+(z)\theta_-(z)\theta_+(2z)\theta_-(2z)
\sigma(\gamma_7z)\sigma(\bar\gamma_7z).
}
\tag{19}
$$
证明只用准确恒等式
$$
\sigma(2z)=-2y\sigma^4,\quad
\theta_+\theta_-=x\sigma^2,\quad
\theta_+(2z)\theta_-(2z)=x(x^3-8b)\sigma^8.
$$
(19) 总 degree 为 $2+8+2+8+7+7=34$；原点阶为六，leading constant 为 $4\cdot7/28=1$。所有常数、CM 方向和 theta 特征均显式保留。

## 6. 完整零除子只有固定挠点

由 (18)，$S$ 的 degree-$34$ 零除子准确如下。

| 实际点集 | 每点重数 | 总重数 |
|---|---:|---:|
| $O$ | $6$ | $6$ |
| $T=(0,\sqrt b),-T$ | $2$ | $4$ |
| 三个非零二挠点 | $2$ | $6$ |
| $[2]^{-1}\{T,-T\}\setminus\{T,-T\}$ | $1$ | $6$ |
| $\ker[\gamma_7]\setminus\{O\}$ | $1$ | $6$ |
| $\ker[\bar\gamma_7]\setminus\{O\}$ | $1$ | $6$ |

第二行来自 $x^2$，第三行来自 $y^2$。准确倍点式
$$
x(2z)=\frac{x(x^3-8b)}{4y^2}
$$
识别第四行的六点。最后两行由真正的 sigma division 式 (5) 给出；两个范数七 CM 核的交只有 $O$，且与非零二、三、六挠点不交。因此上表各项没有遗漏或重复，重数之和为 $34$。

特别，原新来源没有非挠零除子。该事实提供实际固定 $2/3/7$ 挠点的 elliptic-unit 比较输入，但不把这些来源的完整中央导数自动识别成单个固定对数。

## 7. 原三次角表达

令 $a^3=2\sqrt b$，沿 R288 的同一覆盖取
$$
q=u^3,\qquad v^3=1-q,\qquad
x^3=\frac{4b(1-q)}{q^2},\qquad
\sigma=\frac ua\theta_-.
$$
定义固定的八次多项式
$$
\boxed{
Q_8(q)=(q-2)^2(1+q)(1-2q)
(q^4+q^3+6q^2-14q+7).
}
\tag{20}
$$
括号在这里表示整个第四次多项式因子，$Q_8(0)=28$。准确有
$$
\boxed{
S=\frac{q^2v^2}{112b}\theta_-^{34}Q_8(q)
=\frac{q^2}{112b}\theta_+^2\theta_-^{32}Q_8(q).
}
\tag{21}
$$
为直接核常数，(17) 三个因子分别变为
$$
b\frac{(q-2)^2}{q^2},\quad
4b\frac{(1+q)(1-2q)}{q^2},\quad
16b^2\frac{q^4+q^3+6q^2-14q+7}{q^4},
$$
而 $\sigma^{34}x^2=q^{10}v^2\theta_-^{34}/(1024b^5)$。连同 (2) 的 $1/7$ 正得 (21)。又 $q^2\sim4bz^6$，其 leading constant 是 $4b\cdot28/(112b)=1$。

这已经是实际原 Schwartz 来源的三次角公式。$\theta_-^{34}$ 在基曲线上具有非平凡三挠特征，而 $\theta_+^2\theta_-^{32}$ 的平坦类为 $30T=0$，恰好恢复 (2) 的 untwisted 线丛；不能把 (21) 的 $v^2$ 或 theta 比删掉。

## 8. 精确证书与后继范围

- [check-jzero-actual-cm13-matrix-and-theta-source.py](../scripts/check-jzero-actual-cm13-matrix-and-theta-source.py)
- [check-jzero-actual-cm13-matrix-and-theta-source.json](../scripts/check-jzero-actual-cm13-matrix-and-theta-source.json)

脚本重新计算六个完整 CM13 纤维和第七个核验纤维，保留全部 sigma 比的 $34$ 次方，给出 (10)、(14)–(16) 和未缩放矩阵。它还精确核对被排除的 CM13 候选、真实 CM7 因子、(20)、(21) 及首项一归一。这里的目标横坐标不是 Sha 素数实验。

后续可以把 (21) 的真实 $v^2Q_8$ 角因子加入 R291 全部强迫，并把 (19) 的固定挠点乘积送入原完整普通/惰性中央转置。原点六阶非零、全 torsion 除子和矩阵本征性都不单独支付跨素数的完整中央非零。
