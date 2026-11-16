# R840 增补 — 原 Euler 原函数块与完整分歧理想的实际联合交

日期：2026-11-16。**状态：以下同格交空间、保全部零化子的有限呈示、提升选择变换及维数公式已证明。三长高前缀与指定 forcing 的实际联合像仍未判定。**

本注接 [原 Euler 原函数单位块](2026-11-16-r840-actual-euler-primitive-block-and-zero-first-value-kernel.md)，不把它与 R834 的单位块相加。计算始终在同一个原十九角来源中；特别不假设 $f_2=\mathcal E^2F$ 在完整分歧概形上为单位。

## 1. 原来源与两个子格

保 R833/R834 的几何整 $C=(F)\subset X$，并记
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\qquad
N=\mathcal O_C(C),\qquad
\kappa=C^2,\quad\chi=-K_XC,
$$
$$
\mathcal E=Y\partial_Y,\qquad
e=\mathcal EF,\quad f_2=\mathcal E^2F,\quad f_3=\mathcal E^3F .
\tag{1}
$$
假定原范围 $3b<p$、$p>3$、$F_0(t)=F(t,0)\ne0$，且
$e|_C\ne0$。所有 $\mathcal E$ 都是去公共物理载体后的原相对算子；十九角的真实线束框与帽按 R833 保留。

置
$$
\mathcal I=F\mathcal H_2+e\mathcal H_2,\qquad
Z=V(F,e).
\tag{2}
$$
原完全交序列给
$$
\mathcal H_2\twoheadrightarrow H^0(Z,N^2|_Z),\qquad
\ker=F\mathcal H_1+e\mathcal H_1,
$$
$$
\mathcal H_3/\mathcal I
 \simeq H^0(Z,N^3|_Z).
\tag{3}
$$
同时 $\mathcal H_1\twoheadrightarrow H^0(C,N)$，核为 $kF$。这些均来自 R495/R550 的同一真实限制序列。

原函数块为
$$
\mathcal J=
\mathcal E_+^{-1}(F^2\mathcal H_1^{>0})
 \oplus\mathcal H_3^0.
\tag{4}
$$
正 charge 逆逐原列除以 $1,\ldots,3b$，全为单位。等价地，
$$
\boxed{\mathcal J
 =\{W\in\mathcal H_3:\ \mathcal EW\in F^2\mathcal H_1\}.}
\tag{5}
$$
事实上，若 $\mathcal EW=F^2L$，取零 charge 得
$F_0^2L_0=0$，故 $L_0=0$，再用同格的正 charge 逆即得 (4)。因此 (5) 没有扩大原来源。

## 2. 完整零化子及同格选择

定义带正确线束的有限零化子
$$
\boxed{
\mathcal A_2=
\ker\!\left[
 f_2:H^0(Z,N^2|_Z)\longrightarrow H^0(Z,N^3|_Z)
\right].
}
\tag{6}
$$
它包括所有非约化、高分歧、水平及固定角分量，不能先换成零。

选择原 $k$-线性提升
$$
a\longmapsto K_a\in\mathcal H_2,\qquad K_a|_Z=a.
\tag{7}
$$
由 (6) 与 (3)，可以在同一格中线性选择
$$
U_a,V_a\in\mathcal H_2,\qquad
f_2K_a=F U_a+e V_a .
\tag{8}
$$
对 $B\in\mathcal H_1$，令
$$
A_0(a,B)=
 U_a-\mathcal EV_a-\mathcal E^2K_a
 -2f_3B-3f_2\mathcal EB-e\mathcal E^2B
 \in\mathcal H_2,
\tag{9}
$$
并定义真正的有限算子
$$
\boxed{
\mathcal O:\mathcal A_2\oplus\mathcal H_1
 \longrightarrow H^0(Z,N^2|_Z),
\qquad
\mathcal O(a,B)=A_0(a,B)|_Z.
}
\tag{10}
$$

若 $a=0$，取零提升，便准确有
$$
\mathcal O(0,B)=-(2f_3B+3f_2\mathcal EB)|_Z.
\tag{11}
$$
式 (11) 只是完整 (10) 的一个子块；不能用它删除 $\mathcal A_2$。

## 3. 同一个修正的完整呈示

定义
$$
\mathcal X=
\left\{(a,B,C)\in
 \mathcal A_2\oplus\mathcal H_1\oplus\mathcal H_1:
 A_0(a,B)+2eC\in F\mathcal H_1
\right\}.
\tag{12}
$$

**定理 1。** 投影 $\mathcal X\to\mathcal A_2\oplus\mathcal H_1$ 的像恰为
$\ker\mathcal O$，每个非空纤维准确为 $C+kF$。映射
$$
\begin{aligned}
\mathfrak W(a,B,C)
={}&F\bigl(-V_a-\mathcal EK_a-2f_2B-e\mathcal EB+FC\bigr)\\
 &+eK_a+e^2B
\end{aligned}
\tag{13}
$$
满到整个 $\mathcal I\cap\mathcal J$，且有准确短正合列
$$
\boxed{
0\longrightarrow k
 \xrightarrow{\,c\mapsto(0,cF,2c f_2)\,}
 \mathcal X
 \xrightarrow{\ \mathfrak W\ }
 \mathcal I\cap\mathcal J
 \longrightarrow0.
}
\tag{14}
$$
因而
$$
\boxed{\dim(\mathcal I\cap\mathcal J)=\dim\ker\mathcal O.}
\tag{15}
$$

**证明。**
若 $\mathcal O(a,B)=0$，则 $A_0|_C$ 在零除子
$Z=(e|_C)$ 上消失。因此它能在 $C$ 上准确除以 $e$，得到
$N$ 的截面。用 $\mathcal H_1\twoheadrightarrow H^0(C,N)$
选择 $C$，使
$$
(A_0+2eC)|_C=0.
$$
这等价于 (12)，而 $C$ 的差恰为 $kF$。反向显然。

直接对 (13) 求原 Euler 导数，各项完整相消后得到
$$
\boxed{
\mathcal E\mathfrak W
=F\bigl(A_0(a,B)+2eC\bigr)+F^2\mathcal EC.
}
\tag{16}
$$
若 $A_0+2eC=F L$，则
$\mathcal E\mathfrak W=F^2(L+\mathcal EC)$，由 (5) 属于
$\mathcal J$；式 (13) 同时明确属于 $\mathcal I$。

反过来，取 $W=FH+eK\in\mathcal I\cap\mathcal J$。将
$
\mathcal EW=F\mathcal EH+eH+f_2K+e\mathcal EK
$
限制到 $Z$，得 $f_2K|_Z=0$。故 $a=K|_Z\in\mathcal A_2$。
由 (3)，可以写
$$
K=K_a+F K_1+eB,\qquad K_1,B\in\mathcal H_1.
$$
把 $F eK_1$ 吸收到同一个 $FH$ 中，便可假定
$K=K_a+eB$。由 (8)，条件 $F\mid\mathcal EW$ 在 $C$ 上给
$$
H+V_a+\mathcal EK_a+2f_2B+e\mathcal EB=0.
$$
由于 $e|_C\ne0$ 且 $C$ 整，准确有
$$
H=-V_a-\mathcal EK_a-2f_2B-e\mathcal EB+FC
$$
其中 $C\in\mathcal H_1$。再由 (16)，
$F^2\mid\mathcal EW$ 等价于 (12)。这证明满射。

若 $\mathfrak W=0$，在 $C$ 上有
$e(K_a+eB)|_C=0$，故 $K_a+eB\in F\mathcal H_1$。
限制到 $Z$ 先得 $a=0$，所以 $K_a=0$。
随后 $eB|_C=0$ 迫 $B=cF$。代入 (13) 得
$$
\mathfrak W=F^2(C-2c f_2).
$$
因此其为零准确等价于 $C=2c f_2$，得到 (14)。

另一方面，$\mathcal X\to\ker\mathcal O$ 的核为
$\{(0,0,cF)\}$，也是一维。因此两个准确一维核相消，得到 (15)。
证毕。

这里两个一维方向不同：
$$
(0,cF,2c f_2)\longmapsto0,\qquad
(0,0,cF)\longmapsto cF^3.
\tag{17}
$$
后一方向不是可以删除的参数零方向。在原三长窗中，
$\mathcal E^2(F^3)(t,g)=6e_P^3\eta\bmod t^T$，故它仍必须由同一个第三行处理。

## 4. 提升改变的准确同构

(10) 的矩阵依赖原线性提升，但其核呈示和实际交空间不依赖这些选择。下面给出全部改变，而非只以维数解释。

先保持 $K_a$ 不变。原完整 Koszul syzygy 说明另一组 (8) 必形如
$$
U'_a=U_a+eD_a,\qquad
V'_a=V_a-FD_a,\qquad D_a\in\mathcal H_1.
\tag{18}
$$
于是
$$
A'_0=A_0+2eD_a+F\mathcal ED_a.
$$
所以 $\mathcal O'=\mathcal O$，而新参数 $(a,B,C')$ 与旧参数
$(a,B,C'+D_a)$ 给完全相同的 $W$。

一般改变 $K_a$，由 (3) 可线性写为
$$
K'_a=K_a+F A_a+e B_a,\qquad A_a,B_a\in\mathcal H_1.
\tag{19}
$$
先取相容分解
$$
U'_a=U_a+f_2A_a,\qquad
V'_a=V_a+f_2B_a.
$$
逐项求导给
$$
A'_0(a,B')
=A_0(a,B'+B_a)-2e\mathcal EA_a-F\mathcal E^2A_a.
\tag{20}
$$
因此
$$
\boxed{\mathcal O'(a,B')=\mathcal O(a,B'+B_a),}
\tag{21}
$$
而给相同 $W$ 的参数变换为
$$
\boxed{
(a,B',C')\longmapsto
(a,B'+B_a,C'-\mathcal EA_a).
}
\tag{22}
$$
再合 (18) 即涵盖任意选择。所有变换都在原
$\mathcal H_1,\mathcal H_2$ 中，不靠新增局部列或删除零化子。

## 5. 原有限商与三长前缀的准确后继

完整 Koszul 商把联合来源准确写为
$$
(\mathcal I+\mathcal J)/\mathcal I
 \simeq
\operatorname{im}\!\left[
 \mathcal H_1^{>0}\oplus\mathcal H_3^0
 \longrightarrow H^0(Z,N^3|_Z)
\right],
$$
$$
(L,G_0)\longmapsto
\bigl(\mathcal E_+^{-1}(F^2L)+G_0\bigr)|_Z .
\tag{23}
$$
其核由 (12)–(14) 完整支付。若用 R833 的
$z_-=C.H_-$ 与 $\dim\mathcal H_1=1+(\kappa+\chi)/2$，则
$$
\dim\mathcal J=1+\frac{\kappa+\chi}{2}+2z_-,
$$
$$
\boxed{
\dim\frac{\mathcal I+\mathcal J}{\mathcal I}
=1+\frac{\kappa+\chi}{2}+2z_--\dim\ker\mathcal O .
}
\tag{24}
$$
这是实际来源商的维数，不是原物理矩阵新增的单位秩。

现保原物理 $T=T_M=s-r-13$ 与
$h<T\le2h,\ T>2\kappa$，以及已付的整返回
$q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D}$。
对某个同一
$$
W=\mathcal E_+^{-1}(F^2L)+G_0\in\mathcal J
$$
尝试加入 $FH+eK$ 满足三条长行时，先在同一真实形式支上写
$g=\psi e^\eta$，其中 $\operatorname{ord}_t\eta=h$。因 $T\le2h$，
$\eta^2=0\bmod t^T$；三条行逐次等价于
$V_0=V_1=0$ 与 $V_2+\eta V_3=0\bmod t^T$，
其中 $V_i=(\mathcal E^i(W+FH+eK))|_C$。
因此前两条必要条件为
$$
eK|_C+W|_C\in H^0(C,N^3(-TP)),
\tag{25}
$$
$$
eH|_C+f_2K|_C+e(\mathcal EK)|_C
 \in H^0(C,N^3(-TP)).
\tag{26}
$$
式 (25) 若可解，$K|_C$ 唯一：两个解的差是
$N^2$ 的截面，消失阶 $T>2\kappa$。固定真正 $K$ 提升后，
(26) 若可解，$H|_C$ 同样唯一。

同一 $W$ 下，两组满足(25)–(26)的 $FH+eK$ 之差恰为
$F^2L_1$，$L_1\in\mathcal H_1$。第三条长行仍须用 R836
的同一 $3\eta$ 镜轴读取 $L_1$；不可换成任意 $Z$ 值。
而 R834 已证 $\mathcal I\cap K_{3,T}=0$，所以一个 (23) 的商类
至多对应一个三长核元素。它是否实际对应，仍由 (25)、(26)、
第三条完整行及第四短行共同决定。

本注没有证明 (10) 非退化，也没有证明 (23) 的像与实际三长核相交为零。
尤其 $\mathcal A_2$、原两种提升及所有高前缀须同时保留。
公共 $G_0/U_0$、总 charge 四十、原十三行 carry、同一个完整修正及下一位
仍按 R834/R836/R840 运输；(24) 不能用来直接相加两个已知单位块的秩。

依赖：[R833](../results/R833-original-euler-image-and-negative-horizontal-cokernel.md)、
[R834](../results/R834-original-three-long-euler-blocks-and-complete-ramification-ideal.md)、
[R836](../results/R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)、
[R840](../results/R840-original-double-ramification-euler-image-and-unique-normal-tail.md)。
无新数学程序运行。
