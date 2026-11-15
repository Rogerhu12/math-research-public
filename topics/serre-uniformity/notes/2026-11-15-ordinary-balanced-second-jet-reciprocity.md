# 原 ordinary 的平衡二阶 jet 与 scalar 变量的 exact-dual 互反公式

日期：2026-11-15。研究笔记。本文的 §§1–3 是从 R779/R783 完整推得的局部模恒等式，§§4–6 是在所列实际 cocycle 假设下的完整二阶杯积恒等式。**没有计算原 $\Theta$、$b$、$B_1$、$B_{45}$，也没有建立把原巨大 $q$ Robert 乘积直接换成纯 $p$ 数值的显式互反律。** 不另登记结果编号。

## 1. 保留整个局部向量的首 jet

所有对象均为 R783 的原对象，不更换 $q$、正 $\gamma$、$s$、$c=c_s$ 的 $s^{11}$ 移位或未平均 $P_+$。

令
$$
R=k[x,z]/(x^{43},z^{43}),\qquad I=(x,z),\qquad
\overline U=R e_u\oplus R e_q.
$$
这里 $e_u,e_q$ 分别由原 $u_s$ 和任一个满足
$N_Sv_q=w_q=P_+[\alpha_F]$ 的局部 $v_q$ 放到原第零 $\Gamma$ 分支而得。沿用规范识别
$$
N_\Gamma N_S e_u=u,\qquad
N_\Gamma N_S e_q=w_q.
$$

R779 的 exact Euler 关系和不变元是
$$
N_\Gamma c=(1-s^{11})u_s,\qquad
n_R=Qc+\frac{11}{2}u,
$$
$$
Q=-i x^{40}z^{42}+x^{41}z^{41}+i x^{42}z^{40},
\qquad x n_R=z n_R=0.
$$
在 $\overline U$ 中，$N_\Gamma=x^{42}$，而对角嵌入的 $u_s$ 为 $x^{42}e_u$。因此
$$
x^{42}\bigl(c-(1-(1+z)^{11})e_u\bigr)=0.
$$
$R$ 中 $\ker(x^{42})=(x)$，逐坐标得到
$$
c(0,z)=(1-(1+z)^{11})e_u.
\tag{1}
$$
特别 $c$ 的常数项为零。写首 jet 为
$$
c=a x-11z e_u+I^2\overline U,\qquad a\in k e_u\oplus k e_q.
$$
$Q$ 的总次数为 $82$；乘以 $x$ 后，二次或更高的项都因总次数至少 $85$ 而消失。直接有
$$
xQc=(-ia-11e_u)x^{42}z^{42}.
$$
由 $x n_R=0$，而 $u$ 已不变，得到 $a=11i e_u$。所以是整个向量而不只商坐标满足
$$
\boxed{c=11(ix-z)e_u+I^2\overline U.}
\tag{2}
$$
再保留 (1) 的二次项，存在唯一的向量
$A,B\in k e_u\oplus k e_q$，使
$$
\boxed{
c=11(ix-z)e_u+x^2A+xzB-55z^2e_u+I^3\overline U.
}
\tag{3}
$$
其中 $A,B$ 的 $e_q$ 坐标正是 R783 的两个系数。式 (3) 没有求值这两个系数。

## 2. 真正与复共轭相容的 scalar 曲线

在 $k[T]/T^3$ 中作群环同态
$$
x\longmapsto T,\qquad
z\longmapsto(1+T)^i-1
=iT+\binom i2T^2.
\tag{4}
$$
$43>2$，全部二项式分母可逆；群元 $1+x,1+z$ 的两个像的 $43$ 次幂均为一，故这是原 $C_{43}\times C_{43}$ 群环的同态。还因 $\tau\gamma\tau^{-1}=\gamma^{-1}$、$\tau s\tau^{-1}=s$、$\tau i=-i$，在赋予 $T$ 作用
$$
\tau T=(1+T)^{-1}-1
$$
后，(4) 与原 $\tau$ 相容：
$$
\tau((1+T)^i)=(1+T)^i.
$$
在二阶时只写 $z=iT$ 不具有这个相容性；它在 R783 的纯商 $f\in I^2$ 中不改变二次值，却会改变完整 $e_u$ 坐标。

由 (2)，$c$ 沿 (4) 的零阶与一阶均严格消失。定义
$$
\mathcal K=[T^2]\,c\bigl(T,(1+T)^i-1\bigr)
\in k e_u\oplus k e_q.
\tag{5}
$$
不把 $\mathcal K$ 当成一个已经算出的数值。它的准确表达为
$$
\mathcal K
=A+iB+\left(55+\frac{11(1+i)}2\right)e_u.
\tag{6}
$$
其中最后的 $11(1+i)/2$ 来自真实 Euler 首项 $-11z e_u$ 与
$\binom i2=-(1+i)/2$；不能删除。

另一方面
$$
Qx^2=-i x^{42}z^{42},\quad
Qxz=x^{42}z^{42},\quad
Qz^2=i x^{42}z^{42},
$$
且 $Q$ 杀掉 (2) 的首项和全部 $I^3$。置
$$
H=B-iA-55i e_u.
$$
则
$$
Qc=x^{42}z^{42}H,\qquad
\mathcal K=iH+\frac{11(1+i)}2e_u.
\tag{7}
$$
将 $e_u,e_q$ 的常数向量按 Norm 基识别为 $u,w_q$ 后，R779 的原局部下降类精确是
$$
\boxed{(n_R)_p=-i\mathcal K+\frac{11i}{2}u.}
\tag{8}
$$
这是完整两坐标版本；其 $w_q$ 坐标给 R783 的 $\Theta$。

具体写
$$
\mathcal K=K_u u+K_qw_q.
$$
R185/R779 的原规范有 $u=i d_0$、$w_q=d_q$，故
$$
\boxed{
d_R=\left(K_u-\frac{11}{2}\right)d_0-iK_qd_q,\qquad
\Theta=-iK_q,\qquad B_R=K_u-\frac{11}{2}.
}
\tag{9}
$$
由 R779 的实下降，$K_u\in\mathbf F_{43}$、
$K_q\in i\mathbf F_{43}$。因此原二阶障碍为零的待判定条件恰为
$$
\boxed{K_q=11i.}
\tag{10}
$$
式 (8) 没有把 $K_u$ 当作无关紧要的相位；若要输出两条 AH 坐标，
必须保留它：
$$
B_1=24\left(K_u-\frac{11}{2}\right)-20iK_q,\qquad
B_{45}=20\left(K_u-\frac{11}{2}\right)-29iK_q.
\tag{11}
$$

## 3. 此完整二阶向量的选择无关性

先保持原 $u_s$，把 $v_q$ 换成另一个精确 Norm 原像。R783 的基论证给
$$
v'_q=a(s)v_q+d(s)u_s,\qquad a(1)=1,\quad d(1)=0.
$$
相应基变换沿 (4) 是 $I_2+O(T)$。而整个 $c$ 沿 (4) 已属于
$T^2(k[T]/T^3)^2$。因而乘这个基变换或其逆不改变 (5) 的二次常数向量。
这证明完整 $\mathcal K$，不只 $K_q$，对辅助 $v_q$ 选择无关。

同样，若只把两个局部基向量共同平移到另一 $\Gamma$ 分支，坐标乘以
$(1+T)^m=1+O(T)$，二阶向量仍不变。此事实不允许更换原 $\gamma$ 的生成方向、原 $q$、原 $c_s$ 或其 $s^{11}$ 相位。

可以用 $\log(1+T)$ 代替 $T$ 作一阶单位的参数变换。由于沿曲线的低两项已为零，二次系数也不变。但任意缩放 $T\mapsto aT$ 会把二次系数乘 $a^2$；原 $\gamma$ 标记不能省略。

这里没有用局部选择来改变全球 Robert 元。R783 关于局部两 Norm 自由度和真实全球 ordinary 扰动的界限继续有效。

## 4. 带两个 scalar 变量的准确 cocycle 方程

以下是独立的一般 cochain 引理，用于准备实际互反比较。

令 $k$ 为特征 $p>3$ 的有限域，$G$ 为一个绝对 Galois 群或其有限支撑商。设
$a,b:G\to(k,+)$ 为连续同态，$V,D$ 为有限 $k[G]$ 模，有完整
$G$ 等变配对
$$
\langle\, ,\,\rangle:V\times D\longrightarrow k(1).
$$
特别 $D$ 是这里使用的**准确 Tate 对偶**。置
$$
\Lambda=k[X,Z]/(X,Z)^3,\qquad
\vartheta(g)=(1+X)^{a(g)}(1+Z)^{b(g)}.
$$
低于 $p$ 的截断二项式恒等式使 $\vartheta$ 为一个真正的角色。定义
$V_\Lambda$ 的作用为原作用乘 $\vartheta$，$D_\Lambda$ 的作用为原作用乘
$\vartheta^{-1}$。二者的配对仍落入未变形的 $\Lambda(1)$。

假设实际给定了 cocycles
$$
W=\sum_{r+s\le2}X^rZ^s w_{rs}\in Z^1(G,V_\Lambda),\qquad
D^\flat=\sum_{r+s\le2}X^rZ^s d_{rs}\in Z^1(G,D_\Lambda).
\tag{12}
$$
这里假设的是完整 cocycle，不是仅给 $w_{00},d_{00}$ 就自动声称所有提升存在。

对原未变形作用采用非齐次 differential。展开 (12) 给
$$
\delta w_{00}=0,\qquad
\delta w_{10}=-a\cup w_{00},\qquad
\delta w_{01}=-b\cup w_{00},
$$
$$
\delta w_{20}=-a\cup w_{10}-\binom a2\cup w_{00},
$$
$$
\delta w_{11}=-a\cup w_{01}-b\cup w_{10}-ab\cup w_{00},
\tag{13}
$$
以及交换 $a,b$ 的 $02$ 公式。这里 $\binom a2(g)=a(g)(a(g)-1)/2$、
$ab(g)=a(g)b(g)$ 是点值函数；没有把它们误称为加性角色。

对偶公式是
$$
\delta d_{00}=0,\qquad
\delta d_{10}=a\cup d_{00},\qquad
\delta d_{01}=b\cup d_{00},
$$
$$
\delta d_{20}=a\cup d_{10}-\binom{-a}2\cup d_{00},
$$
$$
\delta d_{11}=a\cup d_{01}+b\cup d_{10}-ab\cup d_{00}.
\tag{14}
$$
全部符号来自 $\vartheta^{-1}$，不由一个未标记的一维空间比较决定。

## 5. 完整二阶 reciprocity，包括交叉项

简写
$$
P(u,v)(g,h)=\langle u(g),g v(h)\rangle
$$
，其中右侧的 $g$ 是未变形作用；下面 $aP$ 等符号表示在 $(g,h)$ 上乘
$a(g)$，不是另一个未经说明的三次杯积。

真正的全局杯积 cocycle 是
$$
\mathcal C(g,h)=
\langle W(g),\vartheta(g)^{-1}gD^\flat(h)\rangle.
\tag{15}
$$
由准确对偶和 (12)，$\delta\mathcal C=0$。其一次系数为
$$
\mathcal C_{10}=P(w_{10},d_{00})+P(w_{00},d_{10})
-aP(w_{00},d_{00}),
\tag{16}
$$
以及交换 $a,b$ 的 $01$ 公式。二次系数精确为
$$
\begin{aligned}
\mathcal C_{20}={}&
P(w_{20},d_{00})+P(w_{10},d_{10})+P(w_{00},d_{20})\\
&-a\{P(w_{10},d_{00})+P(w_{00},d_{10})\}
+\binom{-a}2P(w_{00},d_{00}),
\end{aligned}
\tag{17}
$$
$$
\begin{aligned}
\mathcal C_{11}={}&
P(w_{11},d_{00})+P(w_{10},d_{01})
+P(w_{01},d_{10})+P(w_{00},d_{11})\\
&-a\{P(w_{01},d_{00})+P(w_{00},d_{01})\}\\
&-b\{P(w_{10},d_{00})+P(w_{00},d_{10})\}
+abP(w_{00},d_{00}).
\end{aligned}
\tag{18}
$$
$\mathcal C_{02}$ 由 (17) 交换两方向得到。每一个显示的
$\mathcal C_{rs}$ 都是 $k(1)$ 值的 $2$-cocycle；这既由 (15) 逐系数推出，
也可将 (13)–(14) 代入 Leibniz 公式直接核验。

若这些是数域的完整受支撑 cocycles，则全局 reciprocity 逐系数给
$$
\boxed{\sum_v\operatorname{inv}_v\mathcal C_{20,v}=0,\qquad
\sum_v\operatorname{inv}_v\mathcal C_{11,v}=0,\qquad
\sum_v\operatorname{inv}_v\mathcal C_{02,v}=0.}
\tag{19}
$$
只在实际未分歧或已有局部 coboundary 证明的地方删去项。不因零阶类为零而删除整个二阶局部表达。

例如在 $w_{00,v}=0$ 的精确 cochain gauge，
$$
\mathcal C_{20,v}
=P(w_{20},d_{00})+P(w_{10},d_{10})-aP(w_{10},d_{00}).
\tag{20}
$$
仍有两个低阶交叉项。若改为 $d_{00,v}=0$，则
$$
\mathcal C_{20,v}
=P(w_{10},d_{10})+P(w_{00},d_{20})-aP(w_{00},d_{10}).
\tag{21}
$$
这也不能简化为最后一个未知 primitive 的普通配对。若实际
$a_v=b_v=0$，则全部作用修正消失，且 $w_{rs},d_{rs}$ 各自成为未变形作用的 cocycle。

沿与 §2 相同的曲线 $Z=(1+X)^i-1$，准确二次 reciprocity cocycle 是
$$
\boxed{
\mathcal C_{\rm diag,2}
=\mathcal C_{20}+i\mathcal C_{11}-\mathcal C_{02}
+\binom i2\mathcal C_{01}.
}
\tag{22}
$$
最后一项由变量本身的二次系数产生。除非已证明相应一次项在所需局部规范中消失，不能只保留前三项。

(17)–(22) 是这条路线所需的二阶形式恒等式；它们本身不构造尚未知的全球 $w_{20},w_{11},d_{20},d_{11}$，也不求它们的 Frobenius 值。

## 6. 接到原 Robert 数据时必须完成的准确接口

在原 $G_{K,S}$ 上可取两个实际加性角色为 $\kappa_q,\kappa_S$，再保留原
$\tau$ 下降。由于这里先在 $K$ 上写 (19)，回到 $\mathbf Q$ 时要使用原
R168/R200 的二次 restriction 与算术 Frobenius 规范；不能凭此再添加或删除一个 $2$。

如果要从 (19) 真正求 (10)，仍须给出以下同一对象上的输入：

1. 由原 $c_s$ 的 Kummer/Shapiro 实现得到 (12) 中准确的系数，包含原
   $s^{11}$ 和 Euler $1-s^{11}$；必须证明所选映射的完整二阶系数正是
   (5)，而不只证明一阶 Galois 角色相同。
2. 对偶一侧必须是准确 Tate 对偶。R200 已说明把普通 Kummer dual
   直接当 exact dual 会漏掉 cyclotomic 项。二阶时 (17)–(22) 还显示
   相应的一次交叉项也不能省略。
3. 在 $q$ 的完整 Kummer-zero gauge 和 $p$ 的规定局部型中实际求出
   (20)–(21) 的完整组合，或证明可用原纯 $p$ 系统的哪些准确值替换它。

R204 的 $24F_0$ 是 $B_p(c_p^{\rm Rob})_q$；R743/R746 需要的是原
ramified 类 $w$ 的 primitive。尤其 $c_p^{\rm Rob}$ 在 $q$ 只有 finite
坐标，它与另一个 finite 坐标的普通局部配对为零。把一个纯 $p$ 数值
放进 (17) 或 (18) 而跳过这些交叉项，不会自动读出原 $K_q$。

以上把二阶修正项全部写出，并使原完整两坐标的平衡 jet 目标成为 (5)。
没有把存在有限形式运算或一般 reciprocity 恒等式登记为巨大 $q$ 原
Robert 产品的可行计算算法。

## 依赖

- [R779](../results/R779-original-real-Robert-class-and-two-p-local-obstruction-coordinates.md)：原 $Q,n_R$、精确不变性、实际下降和两 AH 坐标。
- [R783](../results/R783-canonical-quadratic-Robert-local-coefficient-and-norm-freedom.md)：同一半局部自由单位格、精确 Norm 基及 $\Theta=13b$。
- [R200](../results/R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md)：exact dual、完整 Kummer-zero gauge、原互反与支持规范。
- [R743](../results/R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md) 与 [R746](../results/R746-original-ordinary-coefficient-as-a-strict-p-bockstein-condition.md)：原 ramified $w$、两种不同局部泛函及全局 primitive 的准确范围。
- [R204](../results/R204-primal-secondary-frobenius-and-full-euler-inverse.md)：仅复用其明确的纯 $p$ primitive 定义与值，不把 $24$ 代入 $\Theta$。

