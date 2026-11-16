# R840 联合交增补 — 真实平滑水平块的单位消元与同一零 charge 系数

日期：2026-11-16。**状态：以下原联合算子在移动平滑水平分量上的完整厚值、单位块及零 charge 约束已证明。奇点、固定角、其余分歧分量与真正高前缀仍保留。**

本注接
[完整联合交](2026-11-16-r840-full-primitive-and-ramification-ideal-intersection.md)。
这里计算的是那里的实际 $\mathcal O$，不把所有分歧点假设为简单，
也不将未加前缀的局部消元当作 $W_T$ 满射。

## 1. 同一水平框与真实有限目标

保 $\mathcal H_j=H^0(X,\mathcal O_X(jC))$、$F$、
$e=\mathcal EF$、$f_2=\mathcal E^2F$ 及 $3b<p$。
取一个不在原固定角上的水平点 $Q$，并假定原有限方程在该点满足
$f_t(Q)\ne0$。允许 $Q$ 的剩余域为任意有限扩张 $k_Q/k$。

负水平取 $x=Y$、$f=F$；正水平取 $x=Y^{-1}$、$f=x^bF$。
省略的原载体在此为 $t$ 的单位，仍按同一线束框保留。
在 $\mathcal H_j$ 的此实际框中，
$$
\boxed{\mathcal E_j=jw+\epsilon x\partial_x,\qquad
(w,\epsilon)=
\begin{cases}
(0,+1),&Y=0,\\
(b,-1),&Y=\infty.
\end{cases}}
\tag{1}
$$
这是原线性化的权，不将正水平改成零权。

由 $f_t(Q)\ne0$，原曲线在 $Q$ 的完成局部环为 $k_Q[[x]]$，
写 $t=t(x)$、$\tau=t(x)-t_Q$。令
$$
m=\operatorname{ord}_x\tau
 =\operatorname{ord}_x f(t_Q,x),\qquad 1\le m\le b.
\tag{2}
$$
此处 $x$ 是曲线的参数；$m$ 是底投影的分歧指数，
不是 $C$ 与水平截面的交数。因为 $m<p$，
$$
e_C:=e|_C=x^m v(x),\quad v(0)\ne0,\qquad
Z_Q=\operatorname{Spec}k_Q[x]/(x^m).
\tag{3}
$$
正侧的负号已包含于实际单位 $v$。
以后 $D=x\,d/dx$ 是沿 $C$ 的全导数，且
$$
\boxed{D\tau=-\epsilon\,e_C/f_t.}
\tag{4}
$$
所有 $f_t,v$ 都是同一原方程沿 $C$ 的值。

## 2. 完整联合算子的原局部矩阵

沿用联合交呈示的同一 $W=FH+eK$，先已支付
$\mathcal EW=FJ$，其中 $J\in\mathcal H_2$；
在那个呈示里
$$
J|_Z=\mathcal O(a,B),\qquad
a=K|_Z=(W|_C/e_C)|_Z.
\tag{5}
$$
这里 $J$ 不是相对物理矩阵的名称，只是显示的原商截面。

**定理 1。** 在 (1)–(3) 的实际厚点上，$\mathcal O$ 准确为
$$
\boxed{
J|_{Z_Q}
=-f_t^{-1}(3w+\epsilon D)
 \left\{
 f_t\left(3w+\epsilon D+\epsilon m+
                 \epsilon\,\frac{Dv}{v}\right)a
 \right\}\pmod{x^m}.
}
\tag{6}
$$
这个分量只依赖同一个 $a$，不依赖呈示中自由选取的 $B$ 或提升。
特别 $f_2|_{Z_Q}=0$，所以此整个局部分量本来就在
$\operatorname{ann}_Z(f_2)$ 中，不能先将它删掉再得 (6)。

**证明。** 对原 $N^3$ 框中的任一 $W$，固定 $t$ 偏导与沿曲线全导数给
$$
(\mathcal EW)|_C
=(3w+\epsilon D)W_C+\frac{e_C}{f_t}W_t|_C.
\tag{7}
$$
由 $\mathcal EW=FJ$，左侧为零。代入 $W_C=e_Ca$，得到
$$
W_t|_C
=-f_t\left(3w+\epsilon D+\epsilon m+
                   \epsilon\,\frac{Dv}{v}\right)a.
\tag{8}
$$
在这个框中权 $w$ 为常数，因此 $\mathcal E$ 与固定 $t$ 偏导交换。
对 $\mathcal EW=FJ$ 求 $t$ 导数，再限制到 $C$：
$$
(\mathcal EW_t)|_C=f_tJ|_C.
$$
把 (7) 用于 $W_t$，并模 $e_C$ 读取，便有
$$
f_tJ|_{Z_Q}=(3w+\epsilon D)W_t|_C\pmod{x^m}.
$$
与 (8) 合成即 (6)。

同样把 (7) 的一阶线束版本用于 $e$，得到
$$
f_2|_C
=(w+\epsilon D)e_C+\frac{e_C}{f_t}e_t|_C\in(e_C),
$$
从而 $f_2|_{Z_Q}=0$。这也与完整联合算子的提升改变公式相容。
证毕。

单位 $f_t,v$ 的对数导数无常数项。故在真实基
$1,x,\ldots,x^{m-1}$ 中，(6) 为三角矩阵，对角准确为
$$
\boxed{-(3w+\epsilon j)(3w+\epsilon(j+m)),
\qquad 0\le j<m.}
\tag{9}
$$

**正水平。** 两因子为 $3b-j$ 与 $3b-j-m$，
均在 $1,\ldots,3b$ 内，因此全为单位。于是
$$
\boxed{\mathcal O|_{Z_Q}\text{ 是单位块；若 }\mathcal O=0,\quad
a|_{Z_Q}=0.}
\tag{10}
$$

**负水平。** 对角为 $-j(j+m)$，除 $j=0$ 外全部为单位。因此秩恰为
$m-1$。其一维核具有原明确单位生成元：
$$
\boxed{\ker\mathcal O|_{Z_Q}
 =k_Q\cdot\frac{\tau}{e_C}\pmod{x^m}.}
\tag{11}
$$
事实上由 (4)，
$$
f_t\left(D+m+\frac{Dv}{v}\right)\frac{\tau}{e_C}
=\frac{f_tD\tau}{e_C}=-1,
$$
外层 $D$ 正好杀掉它；而
$(\tau/e_C)(0)=-1/(m f_t(Q))\ne0$。
这付出了完整厚值，不只是其约化点值。

## 3. 原函数块的实际水平值与同一 $G_0$

现在取真正原函数块的截面
$$
W=\mathcal E_+^{-1}(F^2L)+G_0,\qquad
L\in\mathcal H_1^{>0},\quad G_0\in\mathcal H_3^0.
\tag{12}
$$

**定理 2。** 同一 $W$ 在上述移动平滑水平点满足：

- 正水平：
$$
\boxed{W|_C\in x^{2m}k_Q[[x]]=(e_C^2).}
\tag{13}
$$
- 负水平：
$$
\boxed{
W|_C=G_0(t(x))+O(x^{2m+1}).
}
\tag{14}
$$

**证明。** 在固定 $t$ 的局部展开中赋
$\operatorname{wt}(t-t_Q)=m,\operatorname{wt}(x)=1$。
由 (2) 和 $f_t(Q)\ne0$，实际 $f$ 的每个单项权至少为 $m$。

负水平的 $L$ 没有零 charge，所以 $L\in(x)$，
$f^2L$ 的每个单项权至少为 $2m+1$。
原 $\mathcal E_+^{-1}$ 仅把 $x^n$ 系数除以 $n$，
$1\le n\le3b<p$，保持每个单项的加权阶。
代入 $\tau=t(x)-t_Q$ 后准确得到 (14)。

正水平在原框中，$(3b-x\partial_x)W=f^2l$，
其中 $l=x^bL$ 正则。
右端每个单项权至少为 $2m$。
对所有 $x^j$、$0\le j<3b$，原逆仅除以单位 $3b-j$，
不改变加权阶。
缺少的 $x^{3b}$ 分量是原零 charge 项 $x^{3b}G_0(t)$；
它的阶至少为 $3b\ge3m>2m$。
右端在该分量为零，正是实际 $L_0=0$。
所以 (13) 保留了全部原列与唯一零 charge 分量。证毕。

由 (13)，整个原 $\mathcal J$ 在这些正水平 $Z_Q$ 上的值为零；
由 (14)，其负水平 $Z_Q$ 上的值准确是常数
$G_0(t_Q)$，不是任意的 $m$ 个厚值。
因此联合交注式 (23) 的实际有限像已经受到这些真正来源限制。

若再有 $W\in\mathcal I$，负水平先由
$W|_{Z_Q}=0$ 得 $G_0(t_Q)=0$。
把 (14) 严格截到 $<2m$，再除以 $e_C$，得到
$$
\boxed{
a|_{Z_Q}
=G_0'(t_Q)\,\frac{t(x)-t_Q}{e_C(x)}
 \pmod{x^m}.
}
\tag{15}
$$
这里线性展开只用到模 $x^{2m}$；二次项
$G_0''(t_Q)\tau^2/2$ 在 $x^{2m}$ 处不能删为更长精度。
式 (15) 正是 (11) 的核线，但其系数不是各点独立可选。

R833 的原完整零 charge 格为
$$
G_0=d^{3\mu_{d,1}}P_0(t),\qquad
\deg P_0\le3z_-,
$$
其中 $z_-=C.H_-\le2$ 在原 $r=2$ 全 profile 已付。
因而 (14)、(15) 的所有值与导数来自同一个最多七维的实际全局空间。
固定 $d^{3\mu_{d,1}}$ 因子必须保在导数中；不能把 $G_0$ 本身称作次数至多六的普通多项式。
这里 $z_-\le2$ 也不限制 (2) 的分歧指数 $m$ 为至多二。

## 4. 与真正高前缀联立的范围

这些块可以直接在完整 $\mathcal O$ 的原矩阵中消元：

1. 正水平的实际 $a$ 列由 (10) 唯一消去。
2. 负水平的 $m$ 个厚值只可能沿 (11)，若它来自交中的原 $W$，
   其系数还必须满足同一 $G_0$ 的 (15)。
3. 其它非固定分歧、所有奇点、固定角及其 conductor 完整保留。
   本注没有将其中的 $f_2$ 认成单位。

对 $\mathcal I+\mathcal J$ 中的三长核，原限制值在这些正水平 $Z_Q$
为零，负水平值来自同一 $G_0(t_Q)$。但同一个 $K,H$ 仍须满足联合交注的
(25)、(26)，随后通过真正第三行的 $3\eta$ 镜轴以及原第四短行。
不存在从 (10) 或 (15) 到 $W_T$ 满射的推论。

所有结论均为原目标剩余特征 $p$ 上的手算恒等式；
没有辅助素数、随机纤维或新数学程序运行。
公共 $q_{\rm src}t^r$、完整 $G_0/U_0$、总 charge 四十、
原十三行 carry 及同一个更高精度修正仍按 R834/R836 运输。
本注没有证明指定 trace 非零，也没有关闭全 $\mathcal W_D$ 的实际余核。
