# R1076：原固定 primitive 的三次、六次幂与短双障碍

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o2_high_coefficient / root。

**已证明以下完整来源身份；指定系数非同时零仍未证明。**

本文沿用 [R1061 §§11、21](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md) 的全部原规范，不另换曲线、Cartier 标架或
Picard 参数。仍写
$$
p=6k-1,\quad N=k-1,\quad n=2k-1,\quad
E:V^2=U^3+v^2,\quad v=-6s,\quad v^2=-108,
\quad \omega=dU/(2V),
$$
$$
z=(1-V/v)/2,\qquad
\mathscr D=d/\omega,\qquad
\mathscr D\Psi=\delta\in\mathbf F_p^\times,
\qquad \mathscr D^3=-6vL.
$$
这里 $L$ 正是 (1061.87) 的三阶算子。以下新记号
$\mathscr T$ 是一个明确的原函数多项式；它不是另取的
特征 $p$ 原函数。特别保留微分看不见的 $z^p$ 项。

## 1. 一个完全确定的多项式及其安全范围

定义
$$
\mathscr H(z)=
 \sum_{j=0}^{n}
 \frac{(2/3)_j}{(4/3)_j}z^j
 =
 \left[{}_2F_1(1,2/3;4/3;z)\right]_{\le n}
 \quad\hbox{in }\mathbf F_p[z].
\tag{1076.1}
$$
本式只使用所显示的有限系数。若 $H_j=[z^j]\mathscr H$，则
$$
H_0=1,\qquad
(3j+1)H_j=(3j-1)H_{j-1}
\quad(1\le j\le n).
$$
这些分子、分母都非零。下一分子的 $3(n+1)-1=p$ 为零，
而最高项在以下一阶方程中的系数为 $3n+2=p$，所以
$$
\boxed{\quad
3z(1-z)\mathscr H'(z)+(1-2z)\mathscr H(z)=1.
\quad}
\tag{1076.2}
$$
这是整个多项式的恒等式，不只是有限 jet。
它的次数准确为 $n$，且 $\mathscr H(0)=1$。

若从一阶递推继续形式求系数，第一个不能反除的
$3j+1$ 出现在 $j=4k-1$。
因此本节不把特征零的无限超几何级数无条件约到该共振之后。
实际使用的是 (1076.1) 的明确多项式，以及随后次数至多 $k$
的安全读取。

将 (1076.2) 在 $z=1$ 取值，得 $\mathscr H(1)=-1$。
另一方面 $-\mathscr H(1-z)$ 满足同一个方程、次数至多 $n$、
在零点的值也是一。逐个使用上述可逆系数给出唯一性，故
$$
\mathscr H(1-z)=-\mathscr H(z).
\tag{1076.3}
$$

置
$$
\mathscr T(z)=z(1-z)\mathscr H(z)^3\in\mathbf F_p[z].
\tag{1076.4}
$$
直接微分 (1076.2) 得
$$
\boxed{\quad
\mathscr T'=\mathscr H^2,\qquad
\mathscr T(0)=\mathscr T(1)=0,\qquad
\mathscr T(1-z)=-\mathscr T(z).
\quad}
\tag{1076.5}
$$
其次数为 $2+3n=p$，最高系数是 $-H_n^3\ne0$。
$\deg\mathscr T'=2n=4k-2$ 与 $\deg\mathscr T=p$ 并不矛盾；
不能由 $\mathscr T'$ 删去或重新指定最高的 $p$ 次幂项。

## 2. 与原 $\Psi$ 的完整归一化

原固定 primitive 写为
$$
\Psi=VU S(U^3),\qquad
S(X)=\sum_{j=0}^{N}a_jX^j,\qquad
a_N=-1,\qquad \delta=2v^2a_0.
$$
由 $U^3=-4v^2z(1-z)$，
$$
\widetilde H(z):=\frac{2v}{\delta}V S(U^3)
$$
是次数至多 $2N+1=n$ 的多项式，且 $\widetilde H(0)=1$。
又
$$
\mathscr D(UH(z))
 =2v\{3z(1-z)H'(z)+(1-2z)H(z)\}.
$$
因此 $\mathscr D\Psi=\delta$ 迫 $\widetilde H$ 满足 (1076.2)。
上一节的有限多项式唯一性遂给出准确的原恒等式
$$
\boxed{\quad
\Psi=\frac{\delta}{2v}U\mathscr H(z),
\qquad
\mathscr T(z)=-\frac{2v}{\delta^3}\Psi^3.
\quad}
\tag{1076.6}
$$
没有增添任何未知 $p$ 次幂或常数。

原 $a_N=-1$ 还直接给
$$
H_n=\frac{(4v^2)^k}{\delta}.
$$
利用 $v^p=-v$ 及 $6k=p+1$，得到
$$
[z^p]\mathscr T=-H_n^3
 =\frac{4v^2}{\delta^3}\in\mathbf F_p^\times.
\tag{1076.7}
$$
所以微分盲项本身也已由原 source 固定，而不是事后选取。

因 $\mathscr D\Psi=\delta$，对所有正整数 $a$ 都可直接微分
(1076.6)，得到多项式恒等式
$$
L(\mathscr T^a)
 =\frac{(3a)(3a-1)(3a-2)}3\,\mathscr T^{a-1}.
\tag{1076.8}
$$
本节后续只使用 $1\le a\le k$；此时 $3a\le3k<p$。
特别地，
$$
\boxed{\qquad L\mathscr T=2,\qquad
L(\mathscr T^2)=40\mathscr T.\qquad}
\tag{1076.9}
$$
这些是原固定 $\Psi$ 的三次、六次幂读数，
不是只具有同一个 shadow 的辅助解。

## 3. 完整的 $h,\eta,\nu$ 对应

保持 R1061 §21 的三个短余核泛函：
$$
h_j=\frac{(1/3)_j}{(2/3)_j},\qquad
\eta_0=0,\quad\eta_1=1,\quad \eta L=0,
$$
$$
\nu_0=\nu_1=0,\qquad \nu L=\eta,
\qquad 0\le j\le k.
$$
其中 $h_0=1$ 且 $hL=0$。后一式可直接由
$$
\frac{h_{j-1}}{h_j}=\frac{3j-1}{3j-2},\qquad
\frac{h_{j+1}}{h_j}=\frac{3j+1}{3j+2}
$$
代入 (1061.87) 验证；所有显示分母在所需范围内都是单位。

本节两个非平凡余核恰有以下原多项式读取：
$$
\boxed{\quad
\eta_j=j[z^j]\mathscr T,\qquad
\nu_j=\frac j{40}[z^j]\mathscr T^2
\quad(0\le j\le k).
\quad}
\tag{1076.10}
$$
为付清整条递推，记
$$
A_j=j(3j-1)(3j-2),\quad
B_j=-2j(9j^2+1),\quad
C_j=j(3j+1)(3j+2).
$$
若 $F=\sum F_jz^j$，则
$$
[z^j]LF=C_{j-1}F_{j-1}+B_jF_j+A_{j+1}F_{j+1}.
$$
乘以 $j$ 后，使用
$jC_{j-1}=(j-1)A_j$ 和
$jA_{j+1}=(j+1)C_j$，
即得到 R1061 §21 对 $jF_j$ 的左核递推。
(1076.9) 分别给右端零和 $\eta_j$。
初值由 $\mathscr T=z+O(z^2)$ 给出；
$C_j$ 在 $1\le j\le k-1$ 均可逆，故逐项唯一确定到 $j=k$。
这证明了 (1076.10)，未仅比较几个初始项。

尤其原 forcing 中的常数仍准确是
$$
h=h_k=\frac{(1/3)_k}{(2/3)_k}
 =2^{1-2k},\qquad h^3=2,
\tag{1076.11}
$$
即 (1061.21)–(1061.23) 的同一个常数。
它不是 $\mathscr H$ 的某个未付取值。
因此 $h(z^k-h)=0$，
而 $\eta(z^k-h)=\eta_k$、
$\nu(z^k-h)=\nu_k$，因为 $\eta_0=\nu_0=0$。
R1061 §21 的短像维数及完整三余核遂准确变为
$$
\begin{aligned}
e=K_4=0
&\Longleftrightarrow
 [z^k]\mathscr T=[z^k]\mathscr T^2=0\\
&\Longleftrightarrow
 z^k-h\in L^2\mathbf F_p[z]_{\le k-2}\\
&\Longleftrightarrow
 \exists G\in K[V],\ \deg G\le k-2,\
 \mathscr D^6G=z^k-h.
\end{aligned}
\tag{1076.12}
$$
最后一步只用 $\mathscr D^6=36v^2L^2$ 和这个单位尺度。
其像域不能扩大为任意极阶的有理原函数。

代回已经付清的实际相对 Cartier/平移标度 (1061.95)–(1061.96)，还得到
$$
\boxed{\quad
e=-\frac{k\delta^2}{4v}[z^k]\mathscr T,\qquad
K_4=-\frac{k\delta^3}{160v^2}[z^k]\mathscr T^2
       -\frac{2ve}{\delta^2}.
\quad}
\tag{1076.13}
$$
原第四 jet 保持
$$
96v^4H_p'(0)
 =8ve-\frac{k\delta^5}{160v^2}[z^k]\mathscr T^2.
\tag{1076.14}
$$
这里 $H_p$ 是原 FM 输出 $t_{U^m}=UH_p(U^3)$ 中的多项式；
与本节的 $\mathscr H$ 不混用。

## 4. 谱参数与截断边界

若需要同时保留整个短谱参数，而不仅它的零、一阶项，令 $\lambda$
为独立形式变量，定义
$$
\mathscr F_\lambda(z)
 =\sum_{a=1}^k
   \frac{6(3\lambda)^{a-1}}{(3a)!}\mathscr T(z)^a.
\tag{1076.15}
$$
所有阶乘指标 $3a<p$，所以本式有严格的模 $p$ 意义。
由 (1076.8)，
$$
L\mathscr F_\lambda
 =2+\lambda\mathscr F_\lambda
   -\lambda\,\frac{6(3\lambda)^{k-1}}{(3k)!}\mathscr T^k.
\tag{1076.16}
$$
末项的 $z$ 阶准确为 $k$；不得把该式写成不带误差的齐次方程。
但它不影响 $1\le j\le k-1$ 的左核递推，因而
$$
\eta_j(\lambda):=j[z^j]\mathscr F_\lambda
$$
准确给出以 $\eta_0(\lambda)=0,\eta_1(\lambda)=1$
归一的短谱递推，且
$$
\eta_j(0)=\eta_j,\qquad
\left.\partial_\lambda\eta_j(\lambda)\right|_{\lambda=0}
 =\nu_j\quad(0\le j\le k).
\tag{1076.17}
$$
这同时解释了为何本次第二障碍是指定谱导数，而不是
R1061 §15 半截 Dixon 多项式的参数导数 $D_N'(1)$。
两者未经另一个原来源身份不能互换。

当前未证明 (1076.12) 的两个指定系数不能同时为零。
(1076.7) 的最高系数单位、$\mathscr H$ 的简单根性质、
整个 $L$ 在较大空间的单 Jordan 块，以及特征零的正交/Hankel
正性，都不替代这个指定读数。
下一目标仍是 $e=0\Rightarrow\nu_k\ne0$，或用原完整 MW 消去族
支付真正的最低功能非零。

本节由 o2_high_coefficient 逐式纸推；只写小文本，没有数学程序执行。


## 5. 原输入与继续范围

原 $\Psi$ 的唯一 leading、$\delta$、短三阶 $L$、三个完整余核及相对 Cartier/平移尺度均来自 R1061 §§11–12、21。本篇给出同一个 $\Psi$ 的确定多项式表达与两项实际读取，并未重做旧计算窗口。root 逐式核对有限递推、归一化、最高 $p$ 次幂、左/右递推转换、全部阶乘范围及谱参数误差。没有数学程序执行；原 $e/f_N$、$K_4$ 指定非零及完整全局排除继续开放。
