# 原 quartic 的负水平全范围与双层首项截除

日期：2026-11-16。**状态：下列原余乘子最低 charge 对负水平交数的完整限制，以及端点 $z_-=3$ 的整块消失已证明。没有把它扩展为完整 $K_1$ 的尾像结论。**

沿用[全球负水平与首项临界值](2026-11-16-r872-global-negative-horizontal-and-primitive-leading-moment.md)和[原两 charge 连接核](2026-11-16-r872-quartic-two-charge-global-connecting-kernel.md)的同一原格。
记 $C=(F=0)$、$z_-=C\cdot H_-$。
[R815](../results/R815-complete-original-mori-nef-cones-and-s-fibration.md)(6)–(8) 给
$$
H_-^2=-6.
$$
原来源的准确值是 $B_D\cdot H_-=4$。
$R_0=(t,Y)=(0,0)$ 不属于十九个吹起中心。

## 1. quartic 余乘子的实际最低 charge

取原同源截面
$$
P=t^3F^4q\in\mathcal W_D,\qquad q(0,1)\ne0,
$$
以及原清分母框中的真实残束截面
$$
A^{(4)}=d^{C_D}P/\widehat F^4
\in H^0(X,\mathcal O_X(B_D-4C)).
$$
令 $j$ 为它沿严格 $H_-$ 的准确零阶。
这等于原有理多项式的最低 $Y$ 次数；原 $t$ 单位和固定
$d$ 框不改变它。两 charge 连接核注已付 $0\le j\le2$。

去掉这个**准确**的 $jH_-$ 后，限制到 $H_-$ 不是零截面。
其线束次数是
$$
(B_D-4C-jH_-)\cdot H_-=4-4z_-+6j .
$$
在未吹起的 $R_0$，原 $A^{(4)}$ 含 $t^3$。
除去 $Y^j$ 仍保留这个 $t^3$：
在原正则局部环中，$t$ 与 $Y$ 是互素参数。
因此这个非零限制还含 $3R_0$，必要地
$$
\boxed{4-4z_-+6j\ge3,\qquad 4z_-\le1+6j.}
\tag{1}
$$
这里 $F$ 在 $R_0$ 消失所贡献的 $4C$ 已在残束中扣除；
不能用一个“取最大值”的局部零阶替代真实相加。

准确范围是
$$
\boxed{
\begin{array}{c|c}
j&\text{可能的 }z_-\\ \hline
0&0\\
1&0,1\\
2&0,1,2,3 .
\end{array}}
\tag{2}
$$
故本 quartic 窗口中总有 $z_-\le3$。
这是原来源成员性所迫，不假设存在任一表中因子。

## 2. z_-=3 时整个 primitive 格含两层 H_-

任取原 $J\in\mathscr J_3$，写
$$
LJ=F^3A,\qquad
A\in H^0(X,\mathcal O_X(B_D-3C)),\qquad A\in t^2 .
\tag{3}
$$
先限制到 $H_-$ 并扣 $2R_0$。
其次数为 $2-3z_-$，故 $z_-\ge1$ 时 $A$ 含 $H_-$，
与已经发布的零 charge 结论一致。

再去一层 $H_-$。这个全球截面在 $R_0$ 仍含 $t^2$，
因为除去的是参数 $Y$，不是 $t$。
其限制线束的次数现在准确是
$$
(B_D-3C-H_-)\cdot H_- -2
=8-3z_- .
$$
当 $z_-=3$ 时该数为 $-1$，故第二个限制也恒为零。
于是
$$
\boxed{
z_-=3\quad\Longrightarrow\quad
A\in H^0(X,\mathcal O_X(B_D-3C-2H_-)).
}
\tag{4}
$$
原单项式框中这就是 $Y^2\mid A$。
$L^{-1}$ 逐 charge 对角、全部 $40,\ldots,40+D$ 为单位，
所以同时有
$$
\boxed{[Y^0]J=[Y^1]J=0.}
\tag{5}
$$
没有对其它 exceptional 分量使用这个水平论证。

原零角 $t^2$ 帽只允许
$$
[t^2]A\in k+kY .
$$
式 (4) 因而进一步迫
$$
\boxed{
z_-=3\quad\Longrightarrow\quad
A\in t^3,\qquad J\in t^3
\quad\text{对全部 }J\in\mathscr J_3 .
}
\tag{6}
$$
这一端点不需要先取 $J\in K_1$，也不需要临界值 $v_1(F_0)$ 非零。
它比单独在底 DVR 上观察两个 $t^2$ 列更强。

## 3. 原读取和同一修正的边界

由 (6)，当再取 $J\in K_1$ 时，
原 $\tau=1,2,3$ 的 native 首 Bockstein 全部为
$$
\boxed{
\bar\Lambda_0\beta_1(J)
=\frac{5042}{a}[w^s]W_0(J).
}
\tag{7}
$$
normal 首值真正消去，但同一个第 $s$ 值项仍保留。

(5) 也只对这个已付的全球 primitive 子格成立。
原整来源的前两 charge 是准确的多项式列
$$
[Y^0]\mathcal W_D=k[t]_{\le4},\qquad
[Y^1]\mathcal W_D=k[t]_{\le8}.
$$
第二式直接取原 $n=1$ 的全部角帽：
其 $q_1=1$，剩余次数为 $8$。
不能把它放宽成环境负水平法向线束的全部截面。

在 $K_1$ 中常数 $t^0$ 多项式整体为零，故 $z_-=3$ 时这些真实读取下降到
$$
K_1/(\mathscr J_3\cap K_1)
\longrightarrow
t\,k[t]_{\le4}\ \oplus\ t\,k[t]_{\le8}.
\tag{8}
$$
没有证明 (8) 满射，也没有把它与 $\Pi$ 或其它有限纤维值分开指定。
固定 $P$ 后改 $R$，或固定 $P,R$ 后改 $S$，必须使用同一个来源向量，
并同时保 (7)、全部高前缀、normal 和三条十三行 carry。

## 4. 原好素数上的第十四条必要值行

在本窗口，5042其实始终是单位。若原$p=6s-1>211$整除
$5042=2\cdot2521$，则$p$整除2521，商为至多11的正整数。
2521不被$2,3,5,7,11$整除（分别余$1,1,1,1,2$），
故该商只能是1。但2521模6为1，与$p$模6为5矛盾。

因此，在(6)的自动端点，或前注$z_-\ge1,\ v_1(F_0)\ne0$的实际条件下，
若同一个$J\in\mathscr J_3\cap K_1$能够通过完整首Bockstein，
原三条carry带先给$W_0\in w^s$，再由(7)严格得到
\[
\boxed{W_0(J)\in w^{s+1}.}
\]
相对于最初$T=s-13$的值门，这是十四条而非十三条后续必要值行。
它仍只是完整$\beta_1(J)=0$的必要条件，不证明其余行可解，
也不能用于不属于该原primitive子格的其它修正。

无新增数学数值运行。
