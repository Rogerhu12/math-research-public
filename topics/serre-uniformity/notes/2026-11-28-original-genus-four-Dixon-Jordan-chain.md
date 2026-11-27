# 原固定 genus 4 曲线的 Dixon 平方根与指定 Jordan 长度

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta。

**状态：原来源的精确等价与整递推，未证明指定两量不共零。**
本篇保持同一个 $e,K_4$，将其共同消失改写为固定曲线、固定函数和固定导子的
提前终止：
$$
\boxed{e=K_4=0\quad\Longleftrightarrow\quad D^{p-5}\eta=0.}
\tag{J.1}
$$
随后给出一个不随 $p$ 改换的整多项式序列 $P_j$。
这里研究的是 $P_{p-5}$ 的全部系数模 $p$ 是否为零，
不是另选一个有限和或只比较相同的 CM 字符。
本篇不将整个算子的单 Jordan 块结构当作指定向量的长度下界。

## 1. 原固定曲线、导子及三个分支纤维

保持[原 genus 4 商](2026-11-28-original-genus-four-global-Raynaud-vanishing.md)
的全部规范：
$$
p=6k-1\ge41,\quad N=k-1,\quad
v=-6s,\quad s^2=-3,\quad c=-4/v,
$$
$$
Y:\quad y^3=c(1-\eta^6),\qquad
h=\frac{4\eta\,d\eta}{v y^2},\qquad
u=\eta h,\quad \nu=\eta^{-1}h.
\tag{J.2}
$$
曲线指光滑射影正规化，$g(Y)=4$。
$c,v$ 是固定代数常数的约化；曲线和函数 $\eta,y$ 不依赖于 $k$ 的选择。

到原椭圆曲线的映射及微分为
$$
E:\quad V^2=U^3+v^2,\qquad
U=\frac{4\eta^2}{y^2},\quad
V=v\frac{1+\eta^6}{1-\eta^6},\quad
\frac{dU}{2V}\longmapsto h.
$$
这是 degree 六的可分映射。$\eta=0$ 的三个点记为 $P_i$，
$\eta=\infty$ 的三个点记为 $Q_i$，$\eta^6=1$ 的六个点记为 $R_i$。
前两组分别映到 $(0,v)$、$(0,-v)$，各点的分歧指数为二；
$R_i$ 映到 $O_E$，此映射在这些点不分歧。
由局部参数直接有
$$
\operatorname{div}(\eta)=\sum_iP_i-\sum_iQ_i,\qquad
\operatorname{div}(y)=\sum_iR_i-2\sum_iQ_i,\qquad
\operatorname{div}(h)=\sum_iP_i+\sum_iQ_i.
\tag{J.3}
$$

定义同一不变导子的延拓 $D=h^{-1}d$。曲线方程给
$$
\boxed{D\eta=\frac v4\frac{y^2}{\eta},\qquad Dy=2\eta^4.}
\tag{J.4}
$$
原 $\Psi$ 满足 $D\Psi=\delta$，$\delta\in\mathbf F_p^\times$。
所以 $z=\Psi/\delta$ 是分离变量，$h=dz$。
特征 $p$ 下 $D^p$ 是导子，杀 $z$；函数域对 $K(z)$ 可分，
因此 $D^p=0$。
这里可在含模型常数的完美底域上作证明，再下降全部明确身份。

另取 $\gamma^3=1/c=-v/4$，置 $X=\eta^2$、$B=\gamma y$，得到
$$
X^3+B^3=1,\qquad DX=-2\gamma B^2,\qquad DB=2\gamma X^2.
\tag{J.5}
$$
因此原 $\eta$ 正是固定 Dixon 椭圆函数 $X$ 的平方根。
$Y\to\{X^3+B^3=1\}$ 是实际 degree 二覆盖，后者到原 $E$ 的 degree 为三；
此处不是根据相同 $j$ 值重新识别曲线。

## 2. relative Cartier 的系数与高阶导数

若
$$
C_{\mathrm{rel}}(g h)=b\,h',
$$
令 $F^\sharp b$ 表示输出**系数**沿 relative Frobenius 的拉回。
在 $z=\Psi/\delta$ 的 $p$ 基中展开，Cartier 只读 $z^{p-1}$ 项，
Wilson 给
$$
\boxed{F^\sharp b=-D^{p-1}g.}
\tag{J.6}
$$
这里不写成 differential 的 literal Frobenius 拉回；
$F^*(h')=0$ 与 (J.6) 不是同一个操作。
relative Cartier 对底域常数线性，故外部的 $e,\delta,K_4$ 不擅取 $p$ 次根。

原 genus 4 全基已经证明 Cartier 为零，特别
$C(u)=C(\nu)=0$。
保持 R1061 的原 $F_Q=\eta^{-(p+1)}$，以及
$\nu=\eta^pF_Qh$。
同一原源给
$$
C_{\mathrm{rel}}(\Psi\nu)=e\,u',\qquad
C_{\mathrm{rel}}(\Psi u)=-e\,\nu'.
$$
第二式也由原完整 Raynaud 表及 absolute/relative 转换得到；
其负号与 $e^p=-e$ 相容。
把 $g=\Psi\eta^{\pm1}$ 代入 (J.6)，并用
$D^{p-1}\eta^{\pm1}=0$，得
$$
\boxed{
D^{p-2}\eta=-\frac e\delta\,\eta^{-p},\qquad
D^{p-2}\eta^{-1}=\frac e\delta\,\eta^p.
}
\tag{J.7}
$$

现在假设 $e=0$。R1061.66–70 的实际 Picard source 在 $R=-Q$ 给
$$
C_{\mathrm{rel}}(\Psi^jF_Q\omega)=0
\qquad(0\le j\le3).
$$
原因是原 $t_f=\Phi(U^m)$ 的零至三阶导数均为零，
所以完整 $(D_R+h_Z)^j t_f$ 的第三类项也逐项为零。
乘上 $\eta^p$，再逐个使用 (J.6) 和 Leibniz 法则，得到
$$
D^{p-1}\eta^{-1}
=D^{p-2}\eta^{-1}
=D^{p-3}\eta^{-1}
=D^{p-4}\eta^{-1}=0.
\tag{J.8}
$$
这一步使用全部低插入，绝不是从一个高阶导数为零反向推出低阶导数为零。

R1061.70–74 保留全部项的第四阶式，在 $e=0$ 时准确化为
$$
C_{\mathrm{rel}}(F_Q\Psi^4\omega)=4\delta^2K_4\omega'.
$$
于是 (J.8) 消去 Leibniz 展开的前四项，仅剩
$$
-24\delta^4D^{p-5}\eta^{-1}=4\delta^2K_4\eta^p.
$$
因此
$$
\boxed{
e=0\quad\Longrightarrow\quad
D^{p-5}\eta^{-1}=-\frac{K_4}{6\delta^2}\eta^p.
}
\tag{J.9}
$$
全部除数在当前 $p\ge41$ 下为单位。

原曲线有明确反射
$$
\iota(\eta,y)=(-\eta^{-1},-y/\eta^2).
$$
它固定 $U$、将 $V$ 送到 $-V$，且 $\iota^*h=-h$，
所以 $\iota^*D=-D\iota^*$。
由于 $p-5$ 为偶数，(J.9) 也给
$$
e=0\quad\Longrightarrow\quad
D^{p-5}\eta=-\frac{K_4}{6\delta^2}\eta^{-p}.
\tag{J.10}
$$
若右边两量为零，则 (J.1) 的正向成立。
反向，$D^{p-5}\eta=0$ 先蕴含 $D^{p-2}\eta=0$，由 (J.7) 得 $e=0$；
再使用 (J.10) 得 $K_4=0$。这证明 (J.1)。

## 3. 一个固定的整多项式序列

令 $t=\eta^6$。在特征零的整形式计算后，再作约化，定义
$$
D^j\eta=\eta^{1-2j}y^{-j}P_j(t),\qquad P_0(t)=1.
$$
由 (J.4) 直接得
$$
\boxed{
P_{j+1}(t)=
-6t(1-t)P_j'(t)
+\bigl[(2j-1)+(1-4j)t\bigr]P_j(t).
}
\tag{J.11}
$$
因此 $P_j\in\mathbf Z[t]$、$\deg P_j\le j$。
这个递推没有任何依赖于 $p$ 的系数，也没有数学程序执行。

$\eta^6=1$ 处的正则性在整递推内准确表现为
$$
(1-t)^{\lceil j/3\rceil}\mid P_j(t).
$$
更具体地，写 $A_j=P_j/(1-t)^{\lceil j/3\rceil}$。
对任意 $\ell\ge0$，三个一步算子依次是
$$
\begin{aligned}
A_{3\ell+1}
&=(-6t\partial_t+6\ell-1)A_{3\ell},\\
A_{3\ell+2}
&=\bigl[-6t(1-t)\partial_t+6\ell+1+(3-6\ell)t\bigr]A_{3\ell+1},\\
A_{3\ell+3}
&=\bigl[-6t(1-t)\partial_t+6\ell+3-(6\ell+1)t\bigr]A_{3\ell+2}.
\end{aligned}
\tag{J.12}
$$
这同时给该整除性的归纳证明，没有只凭特殊纤维估计。

置 $B_\ell=A_{3\ell}$，则
$$
D^{3\ell}\eta=c^{-\ell}\eta\,t^{-\ell}B_\ell(t),
\qquad \deg B_\ell\le2\ell.
$$
两端的整系数准确为
$$
B_\ell(0)=-(6\ell-3)!!,\qquad
[t^{2\ell}]B_\ell=(-1)^\ell(6\ell-1)!!
\quad(\ell\ge1).
\tag{J.13}
$$
第一式来自 (J.11) 的常数项，第二式来自其最高次项。
特别 $B_k(0)=-(p-2)!!$ 在模 $p$ 下为单位，
而名义最高项恰首次含因子 $p$。

## 4. 原 Laurent 块与精确两端界

对任意整数 $a$，三次微分可直接合并为
$$
\boxed{
cD^3\eta^a
=a\left[
-(a-2)(a-4)\eta^{a-6}
+2(a^2+4)\eta^a
-(a+2)(a+4)\eta^{a+6}
\right].
}
\tag{J.14}
$$
因而在特征 $p=6k-1$ 下，实际空间
$$
W=\operatorname{span}_K\{\eta^{6r+1}:-k\le r\le k-1\}
$$
被 $cD^3$ 保持。最底列 $r=-k$ 因 $6r+1=-p$ 全为零；
最顶 $r=k-1$ 的上溢系数含 $6r+5=p$。
其余上下相邻系数均为单位。
这不是把已有矩阵任意搬到另一条曲线：每一列就是 (J.14) 的原函数导数。

从 $\eta\in W$ 出发，对所有 $\ell\ge k$，(J.13) 的 Laurent 支撑进一步给
$$
\boxed{
B_\ell(t)=t^{\ell-k}R_\ell(t),\qquad
\deg R_\ell\le2k-1.
}
\tag{J.15}
$$
其中 $\ell=k$ 时 $R_k(0)$ 已知为单位。
逐行解核确有 $\ker(cD^3|_W)=K\eta^{-p}$；
结合 nilpotence，整个 $2k$ 维块是一个 Jordan 块。
但指定输入是中间的 $\eta$，不是已知的 cyclic 顶端。
因此这一事实本身不证明 (J.1) 左边不可能。

## 5. 终止位置及原两标量的完整系数读法

令 $L$ 为最小正整数，使 $D^L\eta=0$，并写 $d=L-1$。
由 $C(u)=0$ 有 $d\le p-2$。
$P_d\ne0$ 且 $P_{d+1}=0$，所以 (J.11) 给
$$
6t(1-t)P_d'=[(2d-1)+(1-4d)t]P_d.
$$
若 $P_d$ 在 $t\ne0,1$ 有重数 $a$ 的零点，
则 $1\le a\le d<p$，左边在那里有准确低一阶的非零项，矛盾。
所以
$$
P_d=Ct^\alpha(1-t)^\beta,\qquad
6\alpha\equiv2d-1,\quad3\beta\equiv d\pmod p,
\quad \alpha+\beta\le d.
$$
取 $0\le\alpha,\beta<p$ 的代表。若 $d=3r+1$，则
$(\alpha,\beta)=(r+k,r+2k)$，总次数超过 $d$；
若 $d=3r+2$，则是 $(r+3k,r+4k)$，仍超过 $d$。
若 $d=3r$，则 $\beta=r$、$\alpha\equiv r-k$；
$r<k$ 的代表同样违反次数界。
准确剩下
$$
\boxed{
d=3r,\quad k\le r\le2k-1,\qquad
P_d=Ct^{r-k}(1-t)^r,\qquad
D^d\eta=Cc^{-r}\eta^{-p}.
}
\tag{J.16}
$$
因此允许的最小长度为 $3k+1,3k+4,\ldots,p-1$。
原两个读数将最后两种长度准确区分：
$$
\begin{array}{c|c}
\text{原读数}&\text{最小长度 }L\\ \hline
e\ne0&p-1\\
e=0,\ K_4\ne0&p-4\\
e=K_4=0&L\le p-7.
\end{array}
\tag{J.17}
$$
前两行用 (J.7)–(J.10)；最后一行还使用 (J.16) 的步长三。
没有从这些允许值本身排除第三行。

特别 (J.7)、(J.10) 给完整多项式身份
$$
\boxed{
P_{p-2}=-\frac e\delta c^{2k-1}
t^{k-1}(1-t)^{2k-1},
}
$$
$$
\boxed{
e=0\ \Longrightarrow\
P_{p-5}=-\frac{K_4}{6\delta^2}c^{2k-2}
t^{k-2}(1-t)^{2k-2}.
}
\tag{J.18}
$$
它们保持原标量，而非仅零性。
最终 (J.1) 也等价于
$$
P_{p-5}(t)\equiv0\pmod p,
$$
即这个固定整多项式的所有系数都被 $p$ 整除。
在本文范围内，尚未证明该整系数条件不可能发生；
也没有用一般有限维 nilpotent/配对非退化性来替代这一指定条件。

## 来源与审计范围

- [原 genus 4 商与完整 Raynaud 表](2026-11-28-original-genus-four-global-Raynaud-vanishing.md)：
  原模型、四基 Cartier 为零、微分尺度和 $e$。
- [R1061](../results/R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)，
  §§19.2–19.4，(1061.66)–(1061.74)：完整第三类插入及原 $K_4$。
- [R1137](../results/R1137-original-Lame-conjugation-with-complete-boundaries.md)：
  原指定源与高极边界保持不变；本篇不将其非局部 $\Lambda$ 换成 $D$。

o1_theta 纸面推导。o2_high_coefficient 已独立核准 (J.4)、(J.6)–(J.10)
的 relative 约定、$-24\delta^4$ 与 $6\delta^2$ 常数及反射。
整递推、全部边界、终止位置及完整系数已由 root/o2 按同一全文独立纸核。
无数学执行、编译或新素数窗口。
