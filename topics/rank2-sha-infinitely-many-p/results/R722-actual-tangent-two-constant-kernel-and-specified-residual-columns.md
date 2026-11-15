# R722 — 原切向物理核的常数二余量与两条指定残余列

日期：2026-11-15。**状态：已证明。**

本篇收紧 R543 的实际切向评价核。
在 $T>2\kappa$、$h>\kappa$ 的窗口，来源值层的原 jet 映射已经单射；
即使原有理函数框在 $d$ 角有负部，也不能把它放宽成任意小线束截面。
由此，全部额外物理核至多剩两个方向，替代原临界
$b^2/64+O(b)$ 的上界。

两个方向不是任选的补空间：它们准确由同一截面在原点的值和首 Euler 法向值标记。
本篇给出一个实际饱和单位块及两条明确剩余来源列。
这不表示整个原目标的余核只有二维，也不删除其余 $\mathcal W_D$ 列。
原指定 forcing 是否在全部原像中仍未由这个秩结论判定。

## 1. 同一切向来源、长度和预算

完整保 R543 的
$$
p=6s-1>83,\quad
1\le\ell\le r<h,\quad k=2h+r-s,\quad0\le k<\ell,
$$
$$
P^{\rm fact}=d^{-C_D}t^rQF^3,\quad
\mathcal E=Y\partial_Y,\quad
e=\mathcal EF,\quad a_0=t\partial_tF,\quad
\mathcal V_F=e\,t\partial_t-a_0\mathcal E .
\tag{1}
$$
原因子 $F$、十九角曲面 $X$、几何整曲线 $C$、
$P=(0,1)$、$\kappa=C^2\ge0$、$\chi=-K_XC$ 不变。
$P$ 光滑且 $e(P)$ 为单位。
$\mathcal H_j$ 是同一整角格，约化为 $H^0(X,\mathcal O_X(jC))$。

使用 R517/R543 已付的返回
$$
\mathcal T_2(H)=d^{-C_D}t^rQ\,
Y^2t(t-1)^2h_7^2\,\mathcal V_FH
\quad(H\in\mathcal H_2),
\tag{2}
$$
或 R521/R543 的三 charge 版本
$$
\mathcal T_3(H)=d^{-C_D}t^rQ\,
Y^3t(t-1)^2h_7^3d^2\,\mathcal V_FH .
\tag{3}
$$
二者均有 $t^{r+1}$ 乘原点单位的真实前缀。

保留它们的全部十九角及真实预算：
(2) 进入 $\mathcal W_{D_0+2}$，(3) 进入
$\mathcal W_{D_0+3}$，其中 $D_0=3b+\deg_YQ$、$b=\deg_YF$。
只有相应的 $D_0+2\le D$ 或 $D_0+3\le D$ 已付时，
才能把本篇单位块放入旧 $\mathcal W_D$；
否则结论属于已经声明的扩大后实际矩阵。

对相对 $J$ 或完整原 $M$，分别取
$$
\boxed{T_J=s-r-1,\qquad T_M=s-r-14.}
\tag{4}
$$
原 $M=c_*U_0w^{13}J$ 的整单位、两条十三行及十三自由行
均照 R543 的长度核对保留。以下 $T$ 总是 (4) 中所选的实际长度。

令 $\mathsf A$ 为整矩阵 $J\mathcal T_i$ 或 $M\mathcal T_i$，
$\mathcal K_T=\ker\overline{\mathsf A}$。
保 R537 用于来源核和饱和的条件
$$
p>8b^2+4bu,\qquad u=\max_i(\deg F_i-4i),
\tag{5}
$$
及同一整角提升。
以下新的物理核证明只需要 $T<p$，调用来源商格时才使用 (5)。

## 2. 原值层的 jet 单射，不丢固定零条件

沿用 R543 的边界平凡化
$$
\mathscr D=C-\operatorname{div}_X(F),\qquad
\mathcal H_j=H^0(X,\mathcal O_X(j\mathscr D)).
\tag{6}
$$
它满足 $\mathscr D\sim C$，且其支持避开 $P$。
$\mathscr D$ 在两个 $d$ 角的负部为 $-Z$；
$Z=0$ 等价于 $F(-1/8,0)\ne0$。
本篇不把 $\mathscr D$ 替换成较大的有效除子 $D_+=\mathscr D+Z$。

对于任何 $j\ge1$，真实限制空间是
$$
V_j=\operatorname{im}\bigl(
\overline{\mathcal H}_j\longrightarrow
H^0(C,\mathcal O_C(j\mathscr D))\bigr).
$$
其线束次数准确为 $j\kappa$。
因为 $P$ 光滑，非零截面在 $P$ 的消失阶不超过其次数。
所以
$$
\boxed{
n>j\kappa\quad\Longrightarrow\quad
V_j\longrightarrow k[t]/t^n
\text{ 单射。}
}
\tag{7}
$$
这适用于几何整、可能在别处奇异的 $C$：
非零线束截面的零概形长度就是线束次数，
而 $nP$ 是其中长度为 $n$ 的 Cartier 子概形。

特别，设一个实际线性子空间 $V\subset V_j$
中每个截面的原点 jet 都是常数。
在 (7) 的范围，这个子空间到该常数的映射单射，
故 $\dim V\le1$。
即使常数函数本身不属于 $V_j$，结论仍成立。
这里正是 R543 放宽到 $D_+$ 后丢失的约束。

## 3. 真核的两个原常数坐标

假设
$$
\boxed{T>2\kappa,\qquad h>\kappa.}
\tag{8}
$$
置 $H_T=\min(h,T)$，则 $H_T>\kappa$。

R543 从完整原两个 Gaussian 行已证明：
若 $H\in\mathcal K_T$，则
$$
H|_C-H(P)=0\bmod t^T .
\tag{9}
$$
因此由 (7)，第一映射
$$
\lambda_0:\mathcal K_T\to k,\qquad H\mapsto H(P)
$$
的像至多一维，而且
$$
\lambda_0(H)=0\quad\Longrightarrow\quad
H|_C=0\quad\Longrightarrow\quad H=FH_1,\quad H_1\in\overline{\mathcal H}_1 .
\tag{10}
$$
这是同一个实际截面的全局限制核，不在环境多项式环中换取修正。

对 (10) 的同一个 $H_1$，
R543 的正镜轴条件继续给
$$
H_1|_C-H_1(P)=0\bmod t^{H_T}.
\tag{11}
$$
再用 (7)，这个第二值像也至多一维；
若 $H_1(P)=0$，便有 $H_1|_C=0$，从而
$H_1=cF$、$H=cF^2$。

更具体地，以下坐标对整个真核有定义：
$$
\boxed{
\Lambda:\mathcal K_T\longrightarrow k^2,\qquad
H\longmapsto\left(H(P),\frac{(\mathcal EH)(P)}{e(P)}\right).
}
\tag{12}
$$
在 $\ker\lambda_0$ 中，由 $H=FH_1$，
第二坐标准确就是 $H_1(P)$。
所以
$$
\boxed{\ker\Lambda=kF^2,\qquad
\mathcal K_T/kF^2\hookrightarrow k^2.}
\tag{13}
$$
没有把两坐标定义成两个任意独立尾。

由此得到实际加强：

**定理 1。** 在 (8) 和原返回条件下，
$$
\boxed{\dim\mathcal K_T\le3.}
\tag{14}
$$
若 $Z=0$，原来源核为 $k\{1,F,F^2\}$，
这三条来源已属于物理核，因此
$$
\boxed{\mathcal K_T=k\{1,F,F^2\}\qquad(Z=0).}
\tag{15}
$$
若 $Z>0$，原来源核只有 $kF^2$，故
$$
\boxed{
\dim\mathcal K_T-\dim\ker\overline{\mathcal T_i}\le2
\qquad(Z>0).
}
\tag{16}
$$

这里 (13) 只识别两个可能的实际额外方向。
它们是否出现仍由同一个完整评价矩阵决定。

## 4. 明确的原饱和单位块

这一加强还能给一个固定实际子来源，而非仅给核维数。

为保持同一整因子，令 $\widetilde P=(0,\widetilde\psi(0))$
为它的原整 Hensel 点，不先改动 $F$ 以强迫常数为一。
记
$$
e_0=(\mathcal EF)(\widetilde P)\in\mathcal O^\times,\qquad
u_F=\frac{\mathcal EF}{e_0}\in\mathcal H_1,\qquad u_F(\widetilde P)=1.
$$
$\mathcal E$ 保每个原角系数和次数帽，所以 $u_F$ 是实际来源。

定义原有限自由直和因子
$$
\boxed{
\mathcal H_2^{00}
=\{H\in\mathcal H_2:
H(\widetilde P)=0,\;(\mathcal EH)(\widetilde P)=0\}.
}
\tag{17}
$$
它确为余维二的整直和因子。显示的两条整截面是
$$
\begin{aligned}
H^{(1)}&=F u_F,\\
H^{(0)}&=u_F^2-\lambda F u_F,\qquad
\lambda=\frac{2(\mathcal Eu_F)(\widetilde P)}{e_0}.
\end{aligned}
\tag{18}
$$
在同一坐标 $(H(\widetilde P),(\mathcal EH)(\widetilde P)/e_0)$ 中，
$H^{(0)},H^{(1)}$ 分别取 $(1,0),(0,1)$。
所有乘积都在原 $\mathcal H_2$ 中，未增加 charge。

$F^2$ 属于 (17)，其约化非零，故是 primitive 整来源。
由 (13)，
$$
\ker\bigl(\overline{\mathsf A}|_{\overline{\mathcal H}_2^{00}}\bigr)=kF^2.
$$
而 $\mathcal T_i(F^2)=0$ 在整来源中准确成立。
因此得到：

**定理 2。**
$$
\boxed{
\mathsf B:
\mathcal H_2^{00}/\mathcal O F^2
\longrightarrow\text{原 }J\text{ 或 }M\text{ 的整个整目标}
}
\tag{19}
$$
是分裂整单射。其全部 Smith 因子都是单位，
秩准确为
$$
\boxed{
\operatorname{rank}\mathsf B
=\dim\mathcal H_2-3=2\kappa+\chi-2.
}
\tag{20}
$$
证明只需有限自由矩阵：
(19) 的约化满列秩，故有同阶单位子式，
得到整左逆和自由余核。
这次饱和是在原物理评价后证明的。

若上述整数秩为零，就把 (19) 读作零来源；
所有核结论仍成立。

## 5. 两条剩余列是指定的，不是自由补

取 (19) 的任一个整左逆，令
$$
\pi_{\rm u}:\mathscr T\longrightarrow
\mathscr Q_{\rm u}:=\mathscr T/\operatorname{im}\mathsf B
$$
为整个原目标的商映射。由于 (19) 饱和，$\mathscr Q_{\rm u}$ 有限自由。
定义两条**实际**剩余列
$$
\boxed{
c_0=\pi_{\rm u}\mathsf A(H^{(0)}),\qquad
c_1=\pi_{\rm u}\mathsf A(H^{(1)}).
}
\tag{21}
$$
不同单位子式只改变这个商的整基，不改变像或 Bockstein。

它们有特别具体的共同来源。若
$\mathcal T_i(H)=c_{\rm src}\mathcal V_FH$，
则由 $\mathcal V_FF=0$，
$$
\boxed{
\begin{aligned}
\mathcal T_i(H^{(1)})
&=c_{\rm src}F\,\mathcal V_Fu_F,\\
\mathcal T_i(H^{(0)})
&=c_{\rm src}(2u_F-\lambda F)\,\mathcal V_Fu_F.
\end{aligned}}
\tag{22}
$$
$c_{\rm src}$ 是 (2) 或 (3) 的整个原前缀。
所以 (21) 只使用同一个真实 $\mathcal V_F(\mathcal EF)$，
并保全部角因子、$Q$、$t^{r+1}$ 和 Gaussian。

整来源准确分解为
$$
\mathcal H_2=\mathcal H_2^{00}
\oplus\mathcal O H^{(0)}\oplus\mathcal O H^{(1)}.
\tag{23}
$$
故整个切向矩阵的单位块以外，准确就是 (21) 这个两列矩阵。
特别，对任意指定原目标 $v$，
$$
\boxed{
v\in\operatorname{im}\mathsf A
\quad\Longleftrightarrow\quad
\pi_{\rm u}v\in\mathcal O c_0+\mathcal O c_1.
}
\tag{24}
$$
同一式在模 $p$、模 $p^2$、模 $p^3$ 下均成立，
因为商掉的是同一个整饱和单位块。

在 $Z>0$ 情形，(12) 的实际像准确为
$$
\boxed{
I_T:=\operatorname{im}\Lambda
=\ker\bigl(k^2\xrightarrow{(\bar c_0,\bar c_1)}
\overline{\mathscr Q}_{\rm u}\bigr).
}
\tag{25}
$$
因而
$\dim I_T=\dim\mathcal K_T-1\le2$。
这是由真实两列计算的像，不是预设所有 $(c_0,c_1)$ 都可实现。

在 $Z=0$ 时，(15) 给 $I_T=k^2$，
而 (21) 两列已经整地属于单位块的像。
可用原 $1,F$ 与 (18) 的差在 (17) 中直接核定。
所以此时所有原非零 Smith 因子均为单位。

在 $Z>0$ 时，去除来源关系 $F^2$ 后，
至多两个来源方向还可能给非单位或额外零因子。
没有因此宣称两个因子都存在、都是 $p$，或特征零物理满列秩已经成立。
其准确阶数由 (21) 的完整整两列决定。

## 6. 旧临界窗口确实满足新门

在 R543 的满主阶低 $\ell$ 范围，
$$
D=3b,\quad
\kappa=\frac{47}{12}b^2+O(b),\quad
h=\frac{141}{32}b^2+O(b),\quad
T_J,T_M=\frac{141}{16}b^2+O(b).
$$
准确相减得到
$$
\boxed{
h-\kappa=\frac{47}{96}b^2+O(b)>0,\qquad
T-2\kappa=\frac{47}{48}b^2+O(b)>0
}
\tag{26}
$$
对充分大 $b$ 成立。十三行只改变 $O(b)$ 项。

因此此前 $K_+=53b^2/12+O(b)$ 导致的微小正余量，
在保持真实值空间后不再产生二次量级的例外方向。
原切向限制至少有
$$
\boxed{
2\kappa+\chi-2=\frac{47}{6}b^2+O(b)
}
\tag{27}
$$
个实际单位 Smith 因子。
$Z>0$ 时余下至多两个；$Z=0$ 时无额外方向。

(26) 是对已存在、满足原返回的实际候选的结论。
它没有证明这样的原首核一定存在，
也没有把固定两个或三个 charge 的扩大当成旧预算的列。

## 7. 原指定 forcing 与同 R 仍须经过全部列

(21)–(24) 将**切向子来源**的全部非单位问题压到两条指定列。
但 $\mathscr Q_{\rm u}$ 通常仍有许多目标行；
“剩两列”不等于“整个目标只剩两条标量条件”。

若要判断原 $\mu J(P^{\rm fact})/p$，
必须把它及其余每一条真正 $\mathcal W_D$ 列
同时投到这个同一个整商。
不能只检验 (21) 后删除其它来源，
也不能把两个原中央标量直接指定为 (12) 的任意坐标。

进入下一位时，(19) 允许真正的整 Schur 消元；
保留完整商、两条实际列和全部其余列，
就保留同一个 $P_2=P^{\rm fact}+pR$、
原 $U_1/p$、两条十三行 carry 及原 $d_2$。
如果在原坐标中读边界，须用该整基变换的逆恢复它们。
本篇未改 $P_{134}/U_0$，未提前删去原低行高尾。

依赖：[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R517](R517-actual-tangent-return-full-gamma-transpose-and-ramification-differential.md)；
[R537](R537-actual-tangent-kernel-inseparable-degree-and-source-saturation.md)；
[R543](R543-actual-tangent-jet-kernel-small-remainders-and-unit-smith-block.md)；
[R552](R552-full-third-source-contact-tail-and-actual-affine-forcing.md)。
