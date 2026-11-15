# R834 增补 — 三条真实长行的全 H3 单位秩

日期：2026-11-15。**状态：下列有限秩界和临界常数已证明。**

本注只细化 [R834](../results/R834-original-three-long-euler-blocks-and-complete-ramification-ideal.md)
已经证明的原三长窗核单射，不给新增来源或中央条件。
所有来源必须经 R834(21) 整返回同一 $\mathcal W_D$；
在完整原 $M$ 中始终取 $T=T_M=s-r-13$，并保其三条十三行 carry。

## 1. 有限的实际界

沿用 R834 的 $C,N,\kappa,\chi,\mathcal H_3,h,T$，要求
$$
h<T\le2h,\qquad T>2\kappa.
\tag{1}
$$
由 R834(30)，原三个长行的核 $K_{3,T}$ 单射进入
$$
V_T=H^0(C,N^3(-TP)).
\tag{2}
$$
原第四短行只会进一步缩小核。因此
$$
\boxed{
\operatorname{rank}_k\bar M|_{q_{\rm src}t^r\mathcal H_3}
\ge 1+\frac{9\kappa+3\chi}{2}-h^0(C,N^3(-TP)).
}
\tag{3}
$$
这里使用的是整个已付 $\mathcal H_3$，不是把不同单位子块的秩相加。

写 $a=\deg_tF,\ b=\deg_YF$。
在 R805 的完整原 profile 范围，
$F(t,0)=\lambda d^cH(t)$、$\deg H=z$，
且 $a,b<p$、$0<h<s$，已证明正规化亏格 $\gamma$ 满足
$$
\gamma\ge
G_F:=\max\left\{0,
\left\lceil\frac{h-2a-10b-2z+6}{6}\right\rceil\right\}.
\tag{4}
$$
该式没有要求最高 $Y$ 系数为固定角 $S$-unit。

令 $\mathcal C(G,d,A)$ 是 R743(19) 的有限整数上界。为明确规范，对
$d>0$ 置
$$
\mathcal C(G,d,A)=1+\max\left(
\{0,1\}\cup
\left\{
j\in\mathbf Z:2\le j\le d,\
\begin{array}{l}
\exists\,1\le\nu\le\lfloor d/j\rfloor,\\
G\le\nu\pi(\lfloor d/\nu\rfloor,j)+(\nu-1)(A-1)
\end{array}
\right\}\right),
\tag{5}
$$
其中
$$
\pi(E,j)=\sum_{i\ge1}\max\{E-1-i(j-1),0\}.
$$
另置 $\mathcal C(G,d,A)=0$ 对 $d<0$，
$\mathcal C(G,0,A)=1$。
R743 的证明保原奇点下降、正特征可分次数及 primitive 函数：
对任意次数 $0\le d<p$ 的原曲线线束，其截面维数至多 (5)，
其中 $A=a+b$。

原曲线是整 Gorenstein 曲线，故 Riemann–Roch 精确给
$$
h^0(C,N^3(-TP))
=\frac{5\kappa+\chi-2T}{2}
+h^0(C,\omega_CN^{-3}(TP)).
\tag{6}
$$
右边残余线束次数为
$$
d_T=T-2\kappa-\chi.
\tag{7}
$$
实际物理长度 $T<s<p$ 保 $d_T<p$；
当 $d_T<0$ 时后项为零。
结合 (4)–(7) 得真正有限上界
$$
h^0(C,N^3(-TP))
\le B_T:=
\frac{5\kappa+\chi-2T}{2}
+\mathcal C(G_F,d_T,a+b).
\tag{8}
$$
于是
$$
\boxed{
\operatorname{rank}_k\bar M|_{q_{\rm src}t^r\mathcal H_3}
\ge1+2\kappa+\chi+T-\mathcal C(G_F,d_T,a+b).
}
\tag{9}
$$
可同时取 R834 的理想块秩界，以及原 Clifford 界中的较强者。
若 $T>3\kappa$，(2) 已直接为零，整个 $\mathcal H_3$ 单射，
不必使用 (8)。

式 (3)、(9) 给原目标素数 $p$ 的单位子式，因而是整单位 Smith 因子下界。
相应的约化核维数至多 $B_T$；
这同时计入可能的正赋值 Smith 对角和零对角，
不额外声称特征零矩阵已满列秩。
也没有删除原完整 $\mathcal W_D$ 的其它列。

## 2. 原二次临界区的常数

考虑满足所有上述来源与长度门的实际因子族，并要求
$$
\kappa\to\infty,\qquad
h/\kappa\to9/8,\qquad T/\kappa\to9/4,\qquad
a+b+z+\chi=o(\kappa).
\tag{10}
$$
原满主阶 profile 的 $a+b+\chi=O(b)$、$z\le2$ 满足最后一项。
从 (4)、(7) 得
$$
G_F\ge3\kappa/16+o(\kappa),\qquad
d_T=\kappa/4+o(\kappa).
\tag{11}
$$

R743 已逐个保留 (5) 中的全部复合次数。
简述其精确常数：若 (5) 中的 $j/\kappa\to x>0$，
则 $\nu$ 有界；沿子列固定 $\nu$ 后，
$$
\lim\frac{\nu\pi(\lfloor d_T/\nu\rfloor,j)}{\kappa}
=\Phi(1/4,\nu x)
\le\Phi(1/4,x),\qquad
\Phi(d,x)=\sum_{i\ge1}(d-ix)_+.
$$
而 $(\nu-1)(a+b-1)=o(\kappa)$。
在 $x=5/48$ 时，
$$
\Phi(1/4,5/48)=7/48+2/48=3/16;
$$
$x$ 再大则严格小于 $3/16$，不合 (11)。
若 $j=o(\kappa)$，所需上界本来成立。
因此
$$
\mathcal C(G_F,d_T,a+b)\le5\kappa/48+o(\kappa),
$$
$$
h^0(C,N^3(-TP))\le17\kappa/48+o(\kappa).
\tag{12}
$$
代入 (3) 得
$$
\boxed{
\operatorname{rank}_k\bar M|_{q_{\rm src}t^r\mathcal H_3}
\ge\frac{199}{48}\kappa+o(\kappa).
}
\tag{13}
$$
由于 $\dim\mathcal H_3=9\kappa/2+o(\kappa)$，
这是同一真实子格至少 $199/216+o(1)$ 的单位比例。

原 R743 的 $359\kappa/96+o(\kappa)$ 是旧两条长行的界。
本篇三条真实长行先排掉其全部镜轴理想核，
使 (13) 比那个界增加
$$
\frac{199}{48}-\frac{359}{96}=\frac{13}{32}
$$
倍的 $\kappa$ 主项。
这个比较涉及两个明确不同的目标行集合，
不是将旧目标的单位秩直接改写。

## 3. 不跨越的范围

(13) 仍只适用于 R834(21) 的同预算完整 $\mathcal H_3$。
它不证明整个 $\mathcal W_D$ 满列，不证明指定 forcing 被排，
也不把约化秩下界变成 $p^2,p^3,p^4$ 的完整 lifting 结论。
四中央的必要高轴系统继续使用实际值和全部 native 项。

本注没有提供所有 $D,k$ 的统一饱和旗标估值，
因此不能据 $199/216$ 的这个单窗比例改写 R418 的全局
$(a_I,b_I)=(0,3)$，亦未越过严格门 $a_I+2b_I<3$。
原受限 $D_3$ 值方程、同一余 normal、第四短行和指定中央非零仍开放。
