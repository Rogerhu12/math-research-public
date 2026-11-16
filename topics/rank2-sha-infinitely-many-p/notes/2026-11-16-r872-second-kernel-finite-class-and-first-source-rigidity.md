# 同一第二核的有限类、平方返回与首来源多项式刚性

日期：2026-11-16。**状态：以下原第二核的真实平方返回、完整首来源系数的有限类刚性已证明。没有求出全 $K_1$ 或 $\ker\beta_1$ 的有限像，没有把两个返回分量分别认成可提升。**

本注接[同修正的有限类与 normal 返回](2026-11-16-r872-same-corrector-finite-class-and-normal-return.md)、[三条原 carry](2026-11-16-r828-three-native-carry-recursions-and-last-block-tails.md)、[真有限纤维商](2026-11-16-r872-native-finite-fiber-quotient-and-cubic-ramification.md)及[平方／立方因子层](2026-11-16-r872-tail-adjustments-in-cubic-and-square-factor-lattices.md)。重点是固定同一个 $P$ 后真正允许改变 $R$ 的第二核；不是一般首核的局部两值可赋性。

## 1. 原窗口及全球类

严格保原
$$
p=6s-1>211,\qquad r=3,\qquad \tau=1,\qquad
s=2h+2,\qquad 1<\ell\le h-1,\qquad h<s-4,
$$
同一个几何整原因子 $F$、$C=(F)$、$F(0,1)=0$、
$e_0=(EF)(0,1)\ne0$ 及
$$
\deg_YF(0,Y)=3,\qquad D\ge4\deg_YF,\qquad p>D+40 .
$$
来源始终为原 $\mathcal W_D$，目标始终为
$$
\Gamma_4=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3).
$$
全部 $c_*U_0/P_{134}$、十九角、实际 $g$、总 charge 四十和三条十三行带保持。

置
$$
L=E+40,\quad
\mathscr V_i=\mathcal W_D\cap F^ik(t)[Y],\quad
\mathscr J_3=L^{-1}\mathscr V_3,\quad
K_1=\ker\bar M,
$$
$$
K_2=\ker\!\left(\beta_1:K_1\longrightarrow
                              \operatorname{coker}\bar M\right),\qquad
\mathfrak o_D(Z)=[Z]\in
\mathcal W_D/(\mathscr V_1+\mathscr J_3).
\tag{1}
$$
这里 $K_2$ 指全部原首 Bockstein 类为零，等价于存在同源整提升
$\widetilde Z+pZ_1$ 通过原 $M$ 的 $p^2$ 精度。
$\mathfrak o_D$ 保完整有限纤维及真实 $H^1$ 连接核；不只读物理零纤维的低商。

以下记
$$
d_D=B_D\cdot C,\qquad \kappa=C^2.
$$

## 2. 全首 carry 在 actual 轴上给三条 s 长行

取 $Z\in K_2$。三条原 carry 注(3)、(6)、(9)–(11)在同一提升上给
$$
W_0^{\rm ref}(Z),W_1^{\rm ref}(Z)\in w^s,
\qquad
W_2^{\rm ref}(Z)+h_0w^{s-4}B\,W_3^{\rm ref}(Z)\in w^s .
\tag{2}
$$
这一步只用第一轮完整三条带，但其适用性由完整 $K_2$ 支付。
不能反向把 (2) 当成 $\beta_1=0$ 的充分条件。

令 $\vartheta=h_0w^{s-4}B$。
原实际高轴和整个公共来源框同时运输时，模 $w^s$ 准确有
$$
W_i^{\rm act}
=W_i^{\rm ref}+\vartheta W_{i+1}^{\rm ref}
\pmod{w^s}\qquad(0\le i\le2).
\tag{3}
$$
二次 $\vartheta$ 项从 $2s-8>s$ 起；从 $w^s$ 开始的其它实际高轴亦不入本式。
对 $i=0,1$，补项还因原长前缀 $s-13$ 而在 $w^s$ 内。
所以 (2) 给
$$
\boxed{
W_0^{\rm act}(Z),\ W_1^{\rm act}(Z),\
W_2^{\rm act}(Z)\in w^s,\qquad
W_3^{\rm act}(Z)\in w^\ell .
}
\tag{4}
$$
特别，$\ell=2,3$ 时不能在参考 $g_0$ 上直接删掉 (2) 的第二项。
式 (3) 保的正是原 actual $g$ 与 charge 四十框的联合运输；
它没有删除下一除 $p$ 页的任何高尾。

令 $Y=\psi(t)$ 为同一个 $F$ 的物理分支，令
$\eta=\log(g/\psi)$，仅按本节所需有限 Taylor 阶数使用。
有 $\operatorname{ord}_w\eta=h$，且原 $t/w$ 为单位。
为明确公共 charge，局部取
$$
\Phi(t,Y)=Y^{40}Z(t,Y).
$$
去掉 (4) 的同一公共 $t$-单位后，
$\mathcal D_i=(E^i\Phi)(t,g)$ 满足相同的消失阶。

首核的原 $t^0$ 三次矩矩阵作用于次数至多二的来源多项式，
给 $Z(0,Y)=0$；因此 $\Phi$ 及其每个 $E$ 导数均含 $t$。
有限 Euler Taylor 给
$$
\begin{aligned}
\Phi|_C
 &=\mathcal D_0-\eta\mathcal D_1
                 +\frac{\eta^2}{2}\mathcal D_2
                 +O(w^{3h+1}),\\
(E\Phi)|_C
 &=\mathcal D_1-\eta\mathcal D_2
                 +\frac{\eta^2}{2}\mathcal D_3
                 +O(w^{3h+1}).
\end{aligned}
\tag{5}
$$
第一式各项阶至少 $s$。
第二式额外一项的阶至少 $2h+\ell\ge2h+2=s$。
又 $3h+1>s$，故准确得到
$$
\boxed{Z|_C\in w^s,\qquad (EZ)|_C\in w^s.}
\tag{6}
$$
这里始终是原多项式先作 $E$ 再限制；
没有在 $k(C)$ 上把横向 $E$ 当作一个已定义的导子。

## 3. 第二核的零全球类必须回到平方层

假定 $Z\in K_2$ 且 $\mathfrak o_D(Z)=0$。
则有真正同预算分解
$$
Z=V+J,\qquad V=FH\in\mathscr V_1,\qquad J\in\mathscr J_3 .
\tag{7}
$$
全来源正合列已保证这包含实际 $H^1$ 拼接条件；
不是从某个低纤维余类为零直接选择 (7)。

由 $J|_C=Z|_C\in w^s$，原 primitive 前缀判据给 $J\in K_1$；
因此同一个 $V\in K_1$。
又 $LJ=F^3A$，所以
$$
(EJ)|_C=-40J|_C .
$$
结合 (6)，得到
$$
\boxed{V|_C=0,\qquad (EV)|_C\in w^s,\qquad H|_C\in w^s.}
\tag{8}
$$
最后一步用 $EV|_C=eH|_C$ 及 $e(P)\ne0$。

整个 $\mathscr J_3$ 已由原零角迫含 $t^2$，
而 $Z\in K_1$ 含 $t$。所以 $t\mid V$；
$F(0,Y)\ne0$ 又给 $t\mid H$。
若 $F\nmid H$，则 $H|_C$ 为非零截面。
它的真实线束是 $\mathcal O_C(B_D-C)$，其有效除子含严格零纤维
$f_0$，且 $C\cdot f_0=3$。
在 $P$，移去这个严格纤维后仍有至少 $s-1$ 阶零。
因此
$$
d_D-\kappa-3\ge s-1,\qquad
\boxed{d_D\ge\kappa+s+2.}
\tag{9}
$$
其余十九角、所有其它分支和奇点均留在同一有效除子中；
此处不把 $f_0$ 换成总纤维。

**定理。** 在准确反门
$$
\boxed{d_D<\kappa+s+2}
\tag{10}
$$
下，第二核的零全球类具有真实平方返回：
$$
\boxed{
\begin{aligned}
K_2\cap(\mathscr V_1+\mathscr J_3)
=\{V+J:\;&V\in K_1\cap\mathscr V_2,\quad
             J\in K_1\cap\mathscr J_3,\\
        &\beta_1(V)+\beta_1(J)=0\}.
\end{aligned}}
\tag{11}
$$
证明的正向是 (7)–(9) 迫 $F\mid H$；
反向直接用同一原来源及 $\beta_1$ 的线性。

式 (11) 明确保留联合首 Bockstein 方程。
一般不能把 $V$、$J$ 分别放进 $K_2$。
两种分解的差仍是同一个 $\mathscr V_4$；
其两项 Bockstein 同时反向改变，故联合式与选择无关。
也没有先把 $\beta_1(\mathscr V_4)$ 赋零。

## 4. 真第一来源系数由完整有限类决定

对任意 $V\in K_1\cap\mathscr V_2$，原平方因子层注(16)–(17)
已由真实四行及原六次帽证明 $t^2\mid V$。
具体地，若
$$
V=t\,v_1(Y)+O(t^2),
$$
则 $\deg v_1\le6$、$(Y-1)^4\mid v_1$；
而 $F^2\mid V$ 及 $\deg F(0,Y)=3$ 迫
$v_1=cF(0,Y)^2$。
$F(0,Y)$ 在 $1$ 恰为单根，所以 $c=0$。

同一个 $J$ 本来已含 $t^2$，故 (11) 进一步给
$$
\boxed{
Z\in K_2,\quad \mathfrak o_D(Z)=0,\quad (10)
\quad\Longrightarrow\quad t^2\mid Z.
}
\tag{12}
$$
因此在实际像 $\mathfrak o_D(K_2)$ 上有一个**良定义的线性读取**
$$
\boxed{
\mathfrak a_1:\mathfrak o_D(K_2)
 \longrightarrow (Y-1)^4k[Y]_{\le2},\qquad
\mathfrak a_1(\mathfrak o_D(Z))=[t]Z .
}
\tag{13}
$$
若两个原第二核来源具有同一全球类，它们之差适用 (12)，
所以整个首来源多项式相同。
没有证明 (13) 满射，亦没有把其目标当成三个自由参数。

这比只读物理零纤维的第一二次块更完整。
若 $F_0=(Y-1)G_0$、$G_0$ monic 度二，则
$$
[t]Z=(Y-1)^4a_2(Y),\qquad \deg a_2\le2,
$$
原低纤维第一项只读
$$
\beta_{\rm low,1}=\operatorname{rem}_{G_0}((Y-1)^4a_2).
\tag{14}
$$
因 $G_0(1)\ne0$，(14) 确定 $a_2\bmod G_0$，但看不见
$a_2\mapsto a_2+cG_0$。
式 (13) 表明这个剩余 $c$ 也不能在固定**完整**有限类和第二页时自由移动。
该结论包括 $G_0$ 重根或等于 $Y^2$ 的情形；
不依赖额外的非物理平方自由假设。

## 5. 对同一 P、R、S 的直接含义

固定同一个原 $P^{\rm fact}$。
设两个真实同源提升
$$
M(P^{\rm fact}+pR+p^2S)\in p^3,\qquad
M(P^{\rm fact}+pR'+p^2S')\in p^3
$$
都通过原全部目标行。
相减后，$\bar R'-\bar R\in K_2$，并同时保原 $S'-S$ 为其第二页补偿。

所以在 (10) 下，
$$
\boxed{
\mathfrak o_D(\bar R')=\mathfrak o_D(\bar R)
\quad\Longrightarrow\quad
[t]\bar R'=[t]\bar R .
}
\tag{15}
$$
原已付首修正式是
$[t]\bar R=(Y-1)^3A(Y)$，$\deg A\le3$，
且 $A(1)$ 为同一 $P^{\rm fact}$ 的指定非零值。
(15) 固定的是整个六次多项式，而非只有这个已知第三导数。

因此处理原有限类之后，不能另拿一个“保持该类”的修正去自由选择
其余 $t^1$ 系数或近支低 normal。
若确实改变它们，必须同时移动同一个全球有限类，且仍通过完整
$\beta_1$ 和同 $S$ 的全部 carry。

本文没有判定 $\mathfrak o_D(K_2)$ 的具体像，也没有证明
$\mathfrak o_D(R)$ 已落或不落任何新的指定小子空间。
其它真实有限纤维、两 charge 的 $H^1$ 连接核、原三尾 $\Pi$、
全部 normal、高尾及下一页继续联立。
无数学数值执行。
