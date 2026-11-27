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


## 6. 实际顶端 cyclic 源与两个有限谱块

本节的谱变量记为 $\lambda$，与原 Cartier 或 Picard 坐标分开。
保持 (J.5)，定义
$$
D_0=-\frac{D}{2\gamma},\qquad
(A,C)=\left(-\frac B X,\frac1X\right),\qquad T=D_0^3.
$$
直接使用 $X^3+B^3=1$ 可得
$$
A^3+C^3=1,\qquad D_0A=C^2,\quad D_0C=-A^2,\qquad
D^3=2vT.
\tag{J.19}
$$
这是原 Fermat 曲线上的明确平移，不是只同构其 Jacobian。
又因 $\eta^p$ 被 $D$ 杀掉，原块及指定输入准确成为
$$
W=\eta^p\operatorname{span}\{C^2,C^5,\ldots,C^p\},
\qquad
\eta=\eta^pC^{3k-1}.
$$

先在特征零定义 $q_{-1}=0,q_0=1$，并令 $a=3n+2$：
$$
\lambda q_n
=-a(a-1)(a-2)q_{n-1}
+2a(a^2+1)q_n-a(a+1)(a+2)q_{n+1}.
\tag{J.20}
$$
三次微分的完整公式
$$
TC^a
=a\{- (a-1)(a-2)C^{a-3}
       +2(a^2+1)C^a-(a+1)(a+2)C^{a+3}\}
$$
逐项证明
$$
C^{3n+2}=q_n(T)C^2,\qquad
\operatorname{lc}(q_n)=\frac{(-1)^n}{(3n+1)!}.
$$
在 $0\le n\le2k-1$ 范围内，构造这些多项式所除的全部因子都小于 $p$。
因此可以严格约化，且 $C^2$ 是整个 $2k$ 维块的 cyclic 向量。
$T^{2k}=0$、$TC^p=0$ 及 Wilson 于是给
$$
\boxed{q_{2k-1}(\lambda)=\lambda^{2k-1},\qquad
T^{2k-1}C^2=C^p.}
\tag{J.21}
$$
这里的完整幂零多项式属于大块；指定向量仍是 $q_N(T)C^2$。

去掉核 $KC^p$ 后，大块维数是 $2N+1$。
以中间向量 $C^{3k-1}$ 为界，左侧 $N$ 阶主块的特征多项式是
$q_N$ 的一个单位倍。右侧按相反顺序写为
$C^{p-3},C^{p-6},\ldots,C^{p-3N}$。
除去共同的 $D_0$ 常数 $C^p$，再作实际平移
$$
(\widetilde A,\widetilde C)=(1/C,-A/C),
$$
便得到 $\widetilde A^3,\widetilde A^6,\ldots,\widetilde A^{3N}$。
这一平移同样保持 $D_0\widetilde A=\widetilde C^2$、
$D_0\widetilde C=-\widetilde A^2$。
故右侧块确是 $T$ 在这些函数上的主块，并在底端模掉常数。

相应地定义 $r_{-1}=0,r_0=1$；令 $a=3n+3$，则
$$
\lambda r_n
=a(a-1)(a-2)r_{n-1}
-2a(a^2+1)r_n+a(a+1)(a+2)r_{n+1}.
\tag{J.22}
$$
它满足
$$
A^{3n+3}=r_n(T)A^3\pmod K,\qquad
\operatorname{lc}(r_n)=\frac2{(3n+2)!}.
$$
特别 $r_N$ 是上述右侧 $N$ 阶主块特征多项式的一个单位倍。
这里的“主块”保留明确的边界投影，不声称两半函数空间各自被 $T$ 保持。

## 7. 两个生成函数与原完整短谱参数

令
$$
F(x)={}_2F_1(1/3,2/3;4/3;x),\qquad
B(x)=(1-x)^{-2/3}.
$$
其逐项身份为 $3xF'+F=B$。
由 (J.20)、(J.22) 可以自足地得到
$$
\boxed{
\sum_{n\ge0}q_n(\lambda)x^n
=B(x)\sum_{\ell\ge0}
 \frac{(-\lambda)^\ell x^\ell F(x)^{3\ell+1}}{(3\ell+1)!},
}
$$
$$
\boxed{
\sum_{n\ge0}r_n(\lambda)x^n
=B(x)\sum_{\ell\ge0}
 \frac{2\lambda^\ell x^\ell F(x)^{3\ell+2}}{(3\ell+2)!}.
}
\tag{J.23}
$$

为付清这两个生成式，先在 $C=0$ 处置
$\xi=C F(C^3)$，则 $D_0=-\partial_\xi$。
把 (J.20) 乘 $A^2C^{3n+1}$ 并求和，三项移位恰好给
$$
\phi=A^2C\sum_{n\ge0}q_n(\lambda)C^{3n},
\qquad
\partial_\xi^3\phi=-\lambda\phi,
\qquad
\phi(0)=0,\quad\phi'(0)=1,\quad\phi''(0)=0.
$$
例如移位所用的完整等式为
$$
T(A^2C^b)
=-b(b-1)(b-2)A^2C^{b-3}
 +2(b+1)((b+1)^2+1)A^2C^b
 -(b+2)(b+3)(b+4)A^2C^{b+3}.
$$
因此 $\phi=\sum_{\ell\ge0}(-\lambda)^\ell
\xi^{3\ell+1}/(3\ell+1)!$，除去 $A^2C$ 就是第一式。

在 $A=0$ 处改取 $\xi=A F(A^3)$，此时 $D_0=\partial_\xi$。
同样将 (J.22) 乘 $A^{3n+2}C^2$ 求和，得到
$$
\psi=A^2C^2\sum_{n\ge0}r_n(\lambda)A^{3n},\qquad
\partial_\xi^3\psi=\lambda\psi,\qquad
\psi(0)=\psi'(0)=0,\quad\psi''(0)=2.
$$
这给第二式，特别保留了系数 $2/(3\ell+2)!$。
两式的最低多项式分别是
$q_1=(20-\lambda)/24$、$r_1=1+\lambda/60$。

这些证明先是特征零形式恒等式。
读取 $q_n$ 到 $n=2k-1$、$r_n$ 到 $n=N$ 时，
$F$ 所需分母 $3j+1$ 至多为 $p-1$；
第一式的最大阶乘是 $(p-1)!$，
第二式的最大阶乘指标是 $3N+2<p$。
所有约化因此都在已经付清的安全范围内。

右侧生成函数不仅匹配两个系数，还准确给出
[R1076 §4](../results/R1076-original-primitive-cubic-and-sixth-power-obstructions.md)
的整个原短谱多项式。
在次数至多 $k$ 的范围，R1076 的原多项式 $\mathscr T(x)$ 满足
$\mathscr T=xF(x)^3$；Euler 变换与该篇明确的共振界保证这一步安全。
又
$$
BF^{3\ell+2}
=F^{3\ell+3}+\frac{x}{\ell+1}(F^{3\ell+3})',
$$
所以 $N=k-1$ 时
$$
\boxed{
r_N(\lambda)
=k[x^k]\sum_{a=1}^k
 \frac{6\lambda^{a-1}}{(3a)!}\mathscr T(x)^a
=\eta_k(\lambda/3).
}
\tag{J.24}
$$
此处 $\eta_k(\cdot)$ 是 R1076.15–17 的同一个谱多项式；
它的参数在那篇取为 $L$ 的谱参数，本篇取为 $D_0^3$ 的谱参数，
比例 $1/3$ 已在 (J.24) 写明。
故
$$
\boxed{r_N(0)=\eta_k,\qquad r_N'(0)=\nu_k/3.}
\tag{J.25}
$$
这些读数不是半截 Dixon 和的辅助变量导数。
所有 $(3a)!$ 都满足 $3a\le3k<p$。
R1076.16 的最高截断误差仍保留，不把短谱式扩大成无限齐次解。

## 8. 左右原尺度与互倒平方根

令
$$
\Gamma=(2v)^{2k}\in\mathbf F_p^\times.
$$
由 (J.19)、(J.21) 及原 (J.7)，
$$
D^{p-2}\eta
=(2v)^{2k-1}q_N(0)\eta^{-p}
=-\frac e\delta\eta^{-p}.
$$
与 R1076.13 的 $e=-\delta^2\eta_k/(4v)$ 比较，得到
$$
\boxed{q_N(0)=\frac{\delta}{2\Gamma}\eta_k
       =\frac{\delta}{2\Gamma}r_N(0).}
\tag{J.26}
$$
若 $e=0$，则 $q_N(0)=0$，同一展开的下一项及 (J.10) 给
$$
D^{p-5}\eta
=(2v)^{2k-2}q_N'(0)\eta^{-p}
=-\frac{K_4}{6\delta^2}\eta^{-p}.
$$
此时 R1076.13 中 $K_4=-\delta^3\nu_k/(4v^2)$，所以
$$
\boxed{e=0\ \Longrightarrow\
q_N'(0)=\frac{\delta}{6\Gamma}\nu_k
       =\frac{\delta}{2\Gamma}r_N'(0).}
\tag{J.27}
$$
因此两个谱块在指定零谱处给出同一个完整双障碍；
并没有从大块的幂零性或主块的邻接系数单位推出根的简单性。

还有一个保持实际 Dixon 参数的读法。
令 $\sigma_D(\tau)$ 为 $\theta(w)=wF(w^3)$ 在原点的形式逆，
即满足 $\sigma_D'= (1-\sigma_D^3)^{2/3}$、
$\sigma_D(0)=0,\sigma_D'(0)=1$ 的原 Dixon 函数。
这里 $\sigma_D$ 不表示 Weierstrass sigma 函数。
定义首项为一的两个互倒平方根
$$
B_+(\tau)=\left(\frac{\sigma_D(\tau)}{\tau}\right)^{1/2},
\qquad B_-(\tau)=B_+(\tau)^{-1}.
$$
对 (J.23) 先在特征零作 Lagrange 反演，
左侧出现的幂是 $(\tau/\sigma_D)^{3N+2}$，
右侧是 $(\tau/\sigma_D)^{3N+3}$。
因为 $3N+2=(p-1)/2$、$3N+3=(p+1)/2$，
在所需的 $\tau$ 次数 $3N<p$ 内，这两个幂分别约为 $B_+$、$B_-$。
准确地，
$$
\boxed{
\begin{aligned}
q_N(\lambda)
 &=\sum_{\ell=0}^N\frac{(-\lambda)^\ell}{(3\ell+1)!}
       [\tau^{3(N-\ell)}]B_+(\tau),\\
r_N(\lambda)
 &=\sum_{\ell=0}^N\frac{2\lambda^\ell}{(3\ell+2)!}
       [\tau^{3(N-\ell)}]B_-(\tau).
\end{aligned}}
\tag{J.28}
$$
$\theta$、其形式逆及平方根所用系数全低于 $p$，
所以本式不需要将完整特征零椭圆对数跨过首个 $p$ 分母约化。
它保留了真正的原参数及全部谱阶乘。

特别原问题成为这个明确互倒平方根的一对相邻系数是否共零。
(J.26)–(J.27) 还给另一平方根对应系数的准确比较。
目前没有把这些互倒关系的其余卷积项删去，故未据 (J.28) 宣布非同时零。

### 本次补充的来源范围

(J.19)–(J.28) 均从原曲线、导子及完整短谱归一逐式证明。
Conrad–Flajolet 的原文
[《The Fermat Cubic, Elliptic Functions, Continued Fractions, and a Combinatorial Excursion》](https://www.mat.univie.ac.at/~slc/s/s54conflaj.pdf)
Figure 3（印刷第 10 页）给出的 $\mathrm{sm}^2$、$\mathrm{sm}^3$
连分数三项系数与 (J.20)、(J.22) 相符，谱符号由本篇的 $D_0^3$ 固定。
该文 §6.3 的另一族生成式不作为 (J.23) 的替代证明。
这里没有使用特征零正性、一般 OPS 根简单性或别的 Hankel 矩阵来推本篇的指定非零。
两个生成式及 (J.24)–(J.25) 已由 o2_high_coefficient 独立纸核；
原短谱参数与全部有限分母另由本文显示式逐项核定。
无数学执行或新素数窗口。
