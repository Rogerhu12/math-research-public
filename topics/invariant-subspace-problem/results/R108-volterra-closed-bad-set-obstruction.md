# R108：闭坏集与强闭交换子的Volterra对照

主会话已全文核验；完整ISP未解决。

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：已证明的抽象推断障碍；供 R108 登记。

本文构造一个 Volterra 对照，具有与 R88、R101、R104 对应的三项抽象性质：

- 完整交换子等于算子多项式的强算子闭包；
- 一列稠密并的闭层中，任意两个非零有限层向量都被某个实际矩分离；
- 对固定任意非零测试端，第一层的全矩消失空间至多一维，坏测试端集合闭、无内点，并具有相应的维数上半连续性。

但它的坏集合仍含非零向量。因而不能仅由上述抽象事实推出坏集合为空。

**边界：这个对照不是实际 odometer 模型的反例。**
Volterra 本身是非零紧算子，直接违反实际模型 R12 的无紧交换子结论。
这里的闭层也不是原来的 Walsh 次数分解。
本文只定位所列抽象推断的缺口；要利用 R12，必须另外构造真实的非零紧交换子或合法的紧交织因子。

## 1. Volterra 算子与双线性型

在
$$
\mathcal H=L^2(0,1)
$$
上令
$$
(Vf)(t)=\int_0^t f(s)\,ds,
\qquad
B_V(f,g)=\int_0^1f(t)g(1-t)\,dt.
\tag{1.1}
$$
$B_V$ 是连续非退化双线性型，且
$$
B_V(Vf,g)=B_V(f,Vg).
\tag{1.2}
$$
后式直接由 Fubini 及三角区域 $s+r\le1$ 得到。
对应的反线性等距对合为
$$
(C_Vg)(t)=\overline{g(1-t)},\qquad
B_V(f,C_Vg)=\langle f,g\rangle.
\tag{1.3}
$$

$n\ge1$ 时，
$$
(V^nf)(t)=\int_0^t\frac{(t-s)^{n-1}}{(n-1)!}f(s)\,ds.
\tag{1.4}
$$
Young 不等式给
$$
\|V^n\|\le\frac1{n!},
$$
所以 $V$ 拟幂零。
$V$ 的积分核为 $\mathbf1_{\{0<s<t<1\}}$，平方积分为 $1/2$；
因此 $V$ 非零且 Hilbert--Schmidt，特别地是紧算子。

## 2. 精确零矩判据：支撑左端相加

对非零 $f\in L^2(0,1)$，将其在区间外延零，并定义
$$
a(f)=\sup\{a\in[0,1]:f=0\text{ a.e. on }(0,a)\}.
\tag{2.1}
$$
有 $0\le a(f)<1$。

使用经典 Titchmarsh 卷积支撑定理：
若非零可积函数 $f,g$ 的支撑左端有限，则
$$
a(f*g)=a(f)+a(g).
\tag{2.2}
$$
这里卷积支撑可以越过 $1$，所以 $a(f*g)$ 按整个实轴上的左支撑端点理解，
不在 $1$ 处截断；对原来的 $f,g$ 则与 (2.1) 一致。
准确陈述可见 Thomas Ransford 的 Theorem 1.1，
原始来源是 E. C. Titchmarsh 1926 年论文；书目见 §9。
这是本稿唯一调用的非初等经典外部定理。

由 (1.4) 与 Fubini，对 $n\ge1$，
$$
\begin{aligned}
B_V(V^nf,g)
&=\int_{\substack{s,r\ge0\\s+r\le1}}
\frac{(1-s-r)^{n-1}}{(n-1)!}f(s)g(r)\,ds\,dr\\
&=\int_0^1\frac{(1-u)^{n-1}}{(n-1)!}(f*g)(u)\,du.
\end{aligned}
\tag{2.3}
$$
因此所有 $n\ge1$ 的矩为零，当且仅当 $f*g=0$ 在 $(0,1)$ 上几乎处处成立。
“仅当”使用多项式在连续函数中的一致稠密性，以及可积函数定义的有限复测度的唯一性。
这里 $f*g$ 实际连续，因为两端是紧支撑 $L^2$ 函数，平移在 $L^2$ 中连续。

$n=0$ 的矩是
$$
B_V(f,g)=(f*g)(1).
$$
所以当卷积在 $(0,1)$ 上为零时，连续性也使该值为零。
结合 (2.2)，得到完整判据
$$
\boxed{
B_V(V^nf,g)=0\quad(\forall n\ge0)
\quad\Longleftrightarrow\quad
a(f)+a(g)\ge1.
}
\tag{2.4}
$$

特别地，
$$
\boxed{f\text{ 对 }V\text{ 循环}\quad\Longleftrightarrow\quad a(f)=0.}
\tag{2.5}
$$
若 $a(f)=0$，任意非零 $g$ 都有 $a(g)<1$，所以 (2.4) 排除非零双线性消失端点，轨道稠密。
若 $a(f)>0$，任取非零 $g$ 支撑于 $[1-a(f),1]$，(2.4) 给非零消失端点。

此外，
$$
\overline{\operatorname{span}}\{V^nf:n\ge0\}
=L^2([a(f),1]).
\tag{2.6}
$$
其双线性消失空间由 (2.4) 恰为 $L^2([1-a(f),1])$，
再对保范数反射配对取双重消失空间即可证明 (2.6)。

## 3. 一个闭的解析子空间及边界唯一性

令
$$
e_k(t)=e^{2\pi ikt},\qquad
\mathcal H_p=\overline{\operatorname{span}}\{e_k:k\ge-p\},
\qquad p=0,1,\ldots.
\tag{3.1}
$$
各 $\mathcal H_p$ 都闭且无限维，逐层递增，且并包含全部三角多项式，因而并稠密。

需要的唯一性事实是：
$$
F\in\mathcal H_p,\ F\not\equiv0
\quad\Longrightarrow\quad
F\text{ 不会在正测度集合上为零}.
\tag{3.2}
$$
下面给出所需短证明。
乘以 $e_p$ 后可令 $p=0$，此时
$$
F(t)=\sum_{k\ge0}c_ke^{2\pi ikt},\qquad (c_k)\in\ell^2.
$$
其圆盘解析函数
$H(z)=\sum_{k\ge0}c_kz^k$ 有统一的径向 $L^2$ 范数，
而径向函数在 $L^2$ 中趋向 $F$。
除掉 $H$ 在原点的有限阶零点后可假定 $H(0)\ne0$；
对 $r\ge1/2$，径向 $L^2$ 范数仍一致有界。

Jensen 不等式给
$$
\int_0^{2\pi}\log|H(re^{i\theta})|\frac{d\theta}{2\pi}
\ge\log|H(0)|.
$$
又 $\log^+x\le x^2$，所以
$$
\int\log^-|H(re^{i\theta})|\frac{d\theta}{2\pi}
\le C-\log|H(0)|
$$
一致有界。
从径向 $L^2$ 收敛选取几乎处处收敛的半径子列。
若 $F$ 在一个正测度集合上为零，沿该子列
$\log^-|H|$ 在该集合上趋于无穷，与 Fatou 引理及上述一致积分界矛盾。
这证明 (3.2)。

## 4. 对称中段向量与稠密闭层

固定
$$
0<a<\tfrac12,\qquad h=\mathbf1_{[a,\,1-a]}.
\tag{4.1}
$$
特意使用对称中段，而不是右端指标函数：
$$
C_Vh=h.
$$
定义
$$
\mathcal D_p=\mathcal H_p+\mathbb Ch,\qquad p\ge0.
\tag{4.2}
$$
$h$ 在初段 $(0,a)$ 上为零且非零，由 (3.2) 知 $h\notin\mathcal H_p$。
因此这个和为代数直和。
它是闭空间：闭子空间加有限维空间仍闭。
各 $\mathcal D_p$ 嵌套、无限维，且其并在 $\mathcal H$ 中稠密。

反射共轭逐个保持频率：
$$
C_Ve_k=e_k,
$$
并保持 $h$，故
$$
C_V\mathcal D_p=\mathcal D_p.
\tag{4.3}
$$
这保证后面双线性与通常复内积版本同时成立。

任意 $0\ne f\in\mathcal D_p$ 唯一写成
$$
f=F+ch,\qquad F\in\mathcal H_p.
$$
若 $F\ne0$，则 $f$ 不可能在任何初段 $(0,\epsilon)$ 上为零：
否则在 $(0,\min(a,\epsilon))$ 上，$h=0$，从而 $F=0$，
违反 (3.2)。
所以
$$
a(f)=0\quad(F\ne0).
$$
若 $F=0$，则 $c\ne0$ 且 $a(f)=a$。因此
$$
\boxed{
f\in\mathcal D_p\setminus\{0\}
\quad\Longrightarrow\quad a(f)\in\{0,a\},
}
\tag{4.4}
$$
其中不循环的向量恰为 $\mathbb Ch\setminus\{0\}$。

## 5. 任意两有限层非零向量都被实际矩分离

由 (4.4)，若
$$
0\ne f\in\mathcal D_p,\qquad 0\ne g\in\mathcal D_q,
$$
则
$$
a(f)+a(g)\le2a<1.
$$
所以 (2.4) 给
$$
\boxed{
\exists n\ge0:\quad B_V(V^nf,g)\ne0.
}
\tag{5.1}
$$
通过 (4.3)，对 $C_Vg$ 应用同一结论，即得
$$
\boxed{
\exists n\ge0:\quad\langle V^nf,g\rangle\ne0.
}
\tag{5.2}
$$
这是一列闭的无限维层、其并稠密、两端任意有限层的完整实际矩分离。
它仍与 $\mathbb Ch$ 中的每个非零向量不循环相容，
因为其轨道消失端点只能出现在这列闭层的并之外。

## 6. 第一层零矩空间和闭坏集的精确计算

把 $\mathcal D_0$ 作为第一层，对任意 $g\in\mathcal H$ 定义
$$
\mathcal Z_g^{V}
=\{f\in\mathcal D_0:
B_V(V^nf,g)=0\text{ 对全部 }n\ge0\}.
\tag{6.1}
$$
若 $g\ne0$，则任何 $F+ch$ 中 $F\ne0$ 的向量都循环，
不可能在该空间中。唯一可能是 $ch$。
由 (2.4)，
$$
\boxed{
\mathcal Z_g^V=
\begin{cases}
\mathbb Ch,&g\ne0,\ a(g)\ge1-a,\\
\{0\},&g\ne0,\ a(g)<1-a.
\end{cases}
}
\tag{6.2}
$$
因此非零测试端处的维数总是 $0$ 或 $1$。

对应坏集合精确为
$$
\boxed{
\mathcal B^V
=\{g:\mathcal Z_g^V\ne\{0\}\}
=L^2([1-a,1]).
}
\tag{6.3}
$$
它是非零、真、闭的无限维线性子空间，所以也是闭复锥且没有内点。
维数在非零点上半连续：坏子空间外的点有一个不碰到该闭子空间的邻域；
坏子空间内的维数为最大值 $1$。
这精确实现了“每个非零端点的零矩空间有限维、坏集合闭且无内点，
但坏集合不为空”的情形。

由于 (4.4) 与 $a<1/2$，
$$
\mathcal B^V\cap\bigcup_{p\ge0}\mathcal D_p=\{0\},
$$
而右侧的层并仍稠密。这明确展示了不能把闭坏集与稠密好类的零交
升级成坏集为零。

## 7. 完整交换子确为多项式的强闭包

这里给自含证明，不把 Volterra 交换子分类作为额外黑箱。

令
$$
\mathcal A_V=\overline{\mathbb C[I,V]}^{\|\cdot\|}.
$$
对 $k\in L^1(0,1)$，记截断卷积算子
$$
(K_kf)(t)=\int_0^t k(t-s)f(s)\,ds.
$$
有 $\|K_k\|\le\|k\|_1$。
当 $k$ 是多项式时，$K_k$ 是无常数项的 $V$ 多项式。
多项式在 $L^1(0,1)$ 中稠密，故
$$
K_k\in\mathcal A_V\qquad(k\in L^1(0,1)).
\tag{7.1}
$$

设 $C$ 是任意有界算子且 $CV=VC$，令 $h_C=C1\in L^2(0,1)\subset L^1(0,1)$。
对稠密的多项式向量 $V^n1=t^n/n!$，
$$
CV(V^n1)=V^{n+1}h_C=K_{h_C}(V^n1).
$$
两侧都是有界算子，故
$$
\boxed{CV=K_{h_C}\in\mathcal A_V.}
\tag{7.2}
$$

对 $\epsilon>0$，设
$$
Q_\epsilon=V(\epsilon I+V)^{-1}.
\tag{7.3}
$$
由 $\|V^n\|\le1/n!$，$(\epsilon I+V)^{-1}$ 的幂级数在范数中收敛，
所以属于 $\mathcal A_V$。
直接展开核或解一阶卷积方程可得
$$
(Q_\epsilon f)(t)
=\int_0^t\epsilon^{-1}e^{-(t-s)/\epsilon}f(s)\,ds.
\tag{7.4}
$$
该因果近单位的 $L^1$ 范数不超过 $1$，
且 $Q_\epsilon f\to f$ 在 $L^2(0,1)$ 中成立：
对连续函数可直接验证，再由收缩范数和稠密性延拓。
于是 $Q_\epsilon\to I$ 强收敛。

由 (7.2)，
$$
CQ_\epsilon=(CV)(\epsilon I+V)^{-1}\in\mathcal A_V,
$$
并且 $CQ_\epsilon\to C$ 强收敛。因此
$$
\{V\}'\subseteq\overline{\mathcal A_V}^{\rm SOT}
=\overline{\mathbb C[I,V]}^{\rm SOT}.
$$
反向包含显然，因为与固定有界 $V$ 交换的条件在强极限下保持。
所以
$$
\boxed{\{V\}'=\overline{\mathbb C[I,V]}^{\rm SOT}.}
\tag{7.5}
$$
因此完整交换子强闭包这一抽象性质也没有消除 §6 的非零坏集合。

## 8. 本对照不能替代实际 R12

实际 odometer 模型还有本对照没有的结构。
尤其 R12 排除任意非零闭不变限制上的非零紧交换子；
而这里 $V$ 本身就是非零紧交换子。
在非零尾不变空间 $L^2([c,1])$、$c<1$ 上，
$V$ 的限制也仍是非零紧积分算子。

此外，$\mathcal D_p$ 是为检验逻辑关系构造的闭解析层，
不是 Walsh 次数层；本稿没有要求它满足实际高位进位恒等式、
R84 的具体合成估计或 R97 的平方零创建结构。

所以准确结论仅为：

> R88 型强闭交换子等式、R101 型稠密闭层双端分离和 R104 型有限维零矩／闭坏集性质，三者本身并不足以推出坏集合为空。

若要从实际有限维 $\mathcal Z_g$ 推导矛盾，必须加入新接口。
例如由该有限维空间构造非零紧算子，并证明它确实与实际 $A$
或某个非零不变限制交换，才可调用 R12。
单纯的正交投影到 $\mathcal Z_g$ 虽然有限秩，却没有已知的交换性；
$\mathcal Z_g\subset H_{\le1}$ 也没有被证明为 $A$ 不变。
因此不能把这个投影直接当作所需的紧交换子。

## 9. 原始文献与核查范围

- E. C. Titchmarsh, *The Zeros of Certain Integral Functions*,
  Proceedings of the London Mathematical Society, Series 2,
  **25** (1926), 283--302.
  DOI：[10.1112/plms/s2-25.1.283](https://doi.org/10.1112/plms/s2-25.1.283)。
  出版者元数据已核对。
- Thomas Ransford, *Letter to the editor: A short complex-variable proof of the Titchmarsh convolution theorem*,
  Journal of Fourier Analysis and Applications **25** (2019), 2697--2702.
  DOI：[10.1007/s00041-019-09679-9](https://doi.org/10.1007/s00041-019-09679-9)；
  [作者公开全文 arXiv:2011.05420](https://arxiv.org/abs/2011.05420)。
  已阅读全文，所用支撑左端相加式准确见 Theorem 1.1（公开稿第 1 页）。

除该经典支撑定理外，本文的矩判据、解析层唯一性、
坏集合、普通内积版本及强闭交换子等式均已在正文给出证明。
