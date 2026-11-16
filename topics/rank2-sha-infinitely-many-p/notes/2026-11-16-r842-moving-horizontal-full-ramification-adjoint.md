# 原 R842 移动水平的完整分歧转置与同源补零块

日期：2026-11-16。**状态：下列两个原水平局部块及其完整转置已证明；在原受限空间上的实际像、同一全局延拓及指定剩余类仍未判定。**

接 [R842](../results/R842-original-gres-double-ramification-transpose-and-joint-prefix-extension.md)
和 [实际边界注第7节](2026-11-16-r842-actual-boundary-rows-and-horizontal-thickenings.md)。
本注只处理未经过十九个固定吹起中心的移动水平点，
且要求所示原 $f_t$ 为单位。固定角的例外框、奇点及 conductor
仍使用实际边界注的全部原式，不能套用本注的 $0,3b$ 权。

## 1. 同一原水平框与真实第一层

保持原 $3b<p$。在 $Y=0$ 取 $x=Y,f=F$；
在 $Y=\infty$ 取 $x=Y^{-1},f=x^bF$。
设 $Q$ 为该原图内的移动水平点，$f_t(Q)\ne0$。
于是 $x$ 是曲线的局部参数，$t=t(x)$，
$$
m=\operatorname{ord}_x(t-t_Q)\le b<p,\qquad
f_x(t(x),x)=x^{m-1}v(x),\quad v(0)\ne0.
\tag{1}
$$
$1\le m\le b$ 用的是原 $t$ 投影的次数，
并没有把高分歧点改成横截点。

用统一记号
$$
(\epsilon,w)=
\begin{cases}
(1,0),&Y=0,\\
(-1,3b),&Y=\infty.
\end{cases}
$$
在对应的真 $N^3$ 单位框中，原 $\mathcal EG$ 为
$(w+\epsilon x\partial_x)G_U$，偏导保持固定 $t$。
原 $e$ 的本地系数在 $C$ 上是
$$
e_U=\epsilon x f_x=\epsilon x^m v(x),\qquad
Z_Q=\operatorname{Spec}k[[x]]/(x^m).
\tag{2}
$$
这里 $k$ 是该点的剩余域。

由于 $t'=-f_x/f_t$，
固定 $t$ 偏导与沿曲线的全导数之差乘 $x$ 后属于 $(x^m)$。
所以 R842 的原有限算子在此真正因子化为
$$
\boxed{
\mathfrak d:
\mathcal O_{2Z_Q}\longrightarrow\mathcal O_{Z_Q},
\qquad
\mathfrak d=(w+\epsilon D_x)\circ\iota,\quad
D_x=x\,d/dx.
}
\tag{3}
$$
不是在整个 $2Z$ 上假定 Euler 保持所有分歧理想。
(3) 只在当前两个水平的真实局部块成立。

## 2. 原对偶化密度给出全部分歧转置

取真正的单位二形式 $dt\wedge dx$。
其伴随生成元为 $dx/f_t$。
记
$$
g(x)=f_t(t(x),x)v(x)\in k[[x]]^\times.
\tag{4}
$$
第一层配对的准确密度是
$$
\frac{dx}{f_t e_U}
=\frac{\epsilon^{-1}}{x^m g(x)}\,dx.
$$
所以在相同真框中，对 $\nu\in k[[x]]/(x^m)$，
$$
\boxed{
\mathfrak d^\vee\nu
=e_Ug\left[w+\epsilon(m-1)-\epsilon D_x\right]
 \left(\frac{\nu}{g}\right)
\pmod{e_U^2}.
}
\tag{5}
$$

证明直接作一次原残数分部：
$$
\operatorname{Res}
(wV+\epsilon xV')\frac{\nu\,dx}{f_te_U}
=
\operatorname{Res}
Vg\left[w+\epsilon(m-1)-\epsilon D_x\right]
(\nu/g)\frac{dx}{f_te_U}.
$$
再使用 $\iota^\vee=e_U$，即得 (5)。
它包括 $f_t$ 与 $v$ 的全单位连接，
不能将 $g$ 删掉后对 $\nu$ 作裸 $D_x$。

(5) 也与 R842 的真框公式逐项相符。
负水平的参数是 $D=x\partial_x,a=0,c=1$；
正水平为 $D=-x\partial_x,a=b,c=-1$。
将同一个 $f_x=x^{m-1}v$ 代入
$\nu f_2-e_U(D\nu+(c-a)\nu)$，
再以 $t'=-f_x/f_t$ 将固定偏导换成全导数，
所有余差在除去一个 $e_U$ 后属于 $(x^m)$，
准确得到 (5)。
这里没有遗漏正水平 $N^3$ 的 $3b$。

## 3. 完整局部秩与实际补零条件

乘单位 $g$ 共轭后，(5) 的第一层算子是显示的对角算子。

在负水平，
$$
(m-1-D_x)x^j=(m-1-j)x^j,\qquad0\le j<m.
$$
因此
$$
\operatorname{rank}(\mathfrak d^\vee/e_U)=m-1,\qquad
\ker(\mathfrak d^\vee/e_U)=k\cdot g x^{m-1}.
\tag{6}
$$
这条核向量在原第一层残数配对中恰读取 $V(Q)$：
其密度是 $dx/x$。
所以这个局部余维一确实是原约化负水平值，
不是任意给定的高 jet。
它不声称原 $\mathscr W_T$ 对该值的限制满射。

在正水平，
$$
(3b+1-m+D_x)x^j=(3b+1-m+j)x^j .
$$
由于 $m\le b$ 且 $3b<p$，全部系数介于 $2b+1$ 与 $3b$，
故都是原单位：
$$
\boxed{\operatorname{rank}(\mathfrak d^\vee/e_U)=m
\quad\text{于正水平}.}
\tag{7}
$$
这里的逆仅为该已固定局部块上的对角逆，
不允许把全局 $\nu$ 的各分量独立选择。

原 $\lambda_0,\lambda_1$ 在水平边界的 $2Z_Q$ 上补零。
因此，若 $w_0,w_1$ 是同一全局 $\omega_0,\omega_1$
在本节真框中的系数，其必要且充分的局部相容式为
$$
\boxed{
\begin{gathered}
w_1\in(e_U),\qquad w_0\in(e_U),\\
\frac{w_0}{e_Ug}
+\left[w+\epsilon(m-1)-\epsilon D_x\right]
\left(\frac{w_1}{e_Ug}\right)=0
\quad\bmod x^m .
\end{gathered}
}
\tag{8}
$$
其中唯一的本地有限分量仍是 $\nu=w_1/e_U\bmod e_U$。
(8) 只是原两个联合延拓式在这个实际块上的消元。

$m=1$ 时，(8) 准确回到已付横截表：
$$
\begin{array}{c|c}
Y=0&w_1\in(e_U),\quad w_0\in(e_U^2)\\
Y=\infty&w_1\in(e_U),\quad w_0+3bw_1\in(e_U^2).
\end{array}
\tag{9}
$$
对 $m>1$，(5)、(8) 中的单位 $g$ 与完整 Euler 多项式都须保留。

## 4. 与真实全来源和其余边界的范围

对真正实现的同一三值 $V_0,V_1,V_2$，
(3) 也给
$$
V_1=(w+\epsilon D_x)V_0,\qquad
V_2=(w+\epsilon D_x)^2V_0\pmod{x^m}.
\tag{10}
$$
所有等式都在原同一个 $N^3$ 单位框中。
它们不把正水平的整个 $\mathcal D_{qt^rG}$
缩成这 $m$ 个值：
实际边界注 (39) 仍保原 $q$、$N_*=3b+\deg_Yq$、
高 jet、Weierstrass 单位 $U$、$\mathcal P_x$ 逆及全部截断成本。

尤其，(7) 不能替代
$\mathcal Q'_T=H^0(\omega_CN^{-2}(TP))$ 的真实限制像；
(6) 也不能替代 $\mathscr W_T$ 的实际值像。
原 $[b_0]$、同一 $\omega_0,\omega_1$、$P$ 项、
固定十九角、奇点和所有 conductor 分支仍须共同满足。
本注没有增加来源、改变 $q$，也没有给指定 forcing 非零或新的中央零。
