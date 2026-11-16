# 原 quartic 余乘子的两 charge 全球连接核

日期：2026-11-16。**状态：以下原全球连接核的固定维数界、零 charge 情形的消失及同两个系数的准确矩阵已证明。有限纤维商、完整 $K_1$ 的高前缀像和指定 forcing 仍保留。**

沿用[原有限纤维商](2026-11-16-r872-native-finite-fiber-quotient-and-cubic-ramification.md)的全部真实 Gauss 束
$\mathscr A_m$、整数 $\ell_{m,n}$、同一 $L=E+40$。
本注不把未饱和来源或物理像替换为环境格。

## 1. 实际余乘子的最低 charge 至多二

保原 $r=3$、$p>D+40$、$D\ge4b$，
以及非零同源分解
$$
P=t^3F^4q\in\mathcal W_D,\qquad
q(0,1)\ne0,\qquad \deg_YF(0,Y)=3 .
$$
清原固定分母后，记
$$
A^{(4)}=\frac{d^{C_D}P}{\widehat F^{\,4}}
\in H^0(\mathscr A_4),
\qquad
j=\operatorname{ord}_Y A^{(4)} .
\tag{1}
$$
这里的 $j$ 是实际最低 $Y$ 次数，不是零角亏损或一个任选乘子次数。

由原零纤维证明，
$v_0(\widehat F)=-3$。
因此 $A^{(4)}/t^3$ 在 $t=0$ 的次数帽至多二，且其值不为零，准确有
$$
\boxed{0\le j\le2.}
\tag{2}
$$
若某个更低 $Y$ 系数在 $t=0$ 恰好消失、但全局并不恒零，
$j$ 仍取这个全局最低次数；(2) 不受影响。

$\widehat F(t,0)$ 不恒为零，因为 $F$ 不可约且不是 $Y$。
故同一来源的
$$
\widehat F A^{(4)}\in H^0(\mathscr A_3),\qquad
\widehat F^{\,3}A^{(4)}\in H^0(\mathscr A_1)
$$
也都具有最低 charge $j$。
于是
$$
\boxed{\ell_{m,j}\ge0,\qquad m=1,3,4.}
\tag{3}
$$

## 2. 所有 residual 线束的次数单调性

前注准确公式为
$$
\ell_{m,n}=\beta_{m,n}
-\sum_\nu\alpha_{m,n,\nu}\deg\nu .
$$
当 $n$ 增加一时：

- $\beta_{m,n}$ 增加四或五；
- 三个四步负角合计最多增加三次有限零；
- 三步负角最多增加一次有限零；
- 正角 $d$ 的要求只会不变或下降。

各 $\max(0,\cdot)$ 不改变这些方向与上界，非分裂 $h_7$ 按次数二计算。因此
$$
\boxed{\ell_{m,n+1}\ge\ell_{m,n}.}
\tag{4}
$$
由 (3)–(4)，三束 $\mathscr A_1,\mathscr A_3,\mathscr A_4$
的第一上同调均只可能来自 $n<j$。
原窗口 (2) 因而把整个连接矩阵限制到 **charge 零、一**；
其它 charge 的 $H^1$ 准确为零，不是按近似维数丢弃。

对 $\mathscr A_4$ 的首两步还可精确收紧。
四步角的要求在 $n=0,1,2$ 完全相同，因为
$$
\left\lceil\frac{n-2-4v_\nu(\widehat F)}4\right\rceil
=-v_\nu(\widehat F)+\left\lceil\frac{n-2}4\right\rceil
$$
在这三个 $n$ 上恒定，取 $\max(0,\cdot)$ 后亦然。
又
$$
\beta_{4,n}=\lfloor9n/2\rfloor+C_D+4+2v_\infty(\widehat F),
$$
首两增量分别是四、五。
$d$ 角的首步不变、第二步最多放松一。因此
$$
\boxed{
0\le\ell_{4,1}-\ell_{4,0}\le4,\qquad
0\le\ell_{4,2}-\ell_{4,1}\le6.
}
\tag{5}
$$
三步负角只可能减小这两个增量。

结合 $H^1\mathcal O_{\mathbf P^1}(\ell)$ 的维数
$\max(0,-\ell-1)$，得到
$$
\boxed{
\begin{array}{c|c|c}
j&\text{可能贡献的 charge}&\dim H^1(\mathscr A_4)\\ \hline
0&\text{无}&0\\
1&0&\le3\\
2&0,1&\le14 .
\end{array}}
\tag{6}
$$
例如 $j=2$ 时 $\ell_{4,2}\ge0$，
故 $\ell_{4,1}\ge-6$、$\ell_{4,0}\ge-10$，
两项上界准确为五和九。
这些界不随 $b,D,p$ 增长，但未声明它们总能取到。

## 3. 同一两个系数的连接矩阵

记
$$
f_0(t)=[Y^0]\widehat F,\qquad
f_1(t)=[Y^1]\widehat F .
$$
它们不是上一注的零纤维三次多项式 $F_0(Y)$。

前注的连接核来自同一个箭头
$$
A\longmapsto
\left(\widehat F^{\,3}A,\;
-4(E\widehat F)A-\widehat F LA\right)
:\mathscr A_4\longrightarrow\mathscr A_1\oplus\mathscr A_3.
\tag{7}
$$
由 (2)–(4)，只需保一个实际上同调代表
$A=a_0+a_1Y$，其中不存在的 $H^1$ 项置零。
其两目标的全部可能非零 charge 准确是
$$
\boxed{
\begin{array}{c|cc}
& n=0&n=1\\ \hline
\mathscr A_1&
f_0^3a_0&
f_0^3a_1+3f_0^2f_1a_0\\
\mathscr A_3&
-40f_0a_0&
-41f_0a_1-44f_1a_0 .
\end{array}}
\tag{8}
$$
每一格都按对应的原固定角框投影到其真正 Laurent 余类。
不能先在裸 $k[t,t^{-1}]$ 中删项，再忘记目标框的固定乘子。

事实上 $\mathscr A_1$ 的两行在该实际低 charge 范围内冗余。
若 $\mathscr A_3$ 的行均为零，
先有 $[f_0a_0]_{3,0}=0$。
乘 $\widehat F^{\,2}$ 给 $\mathscr A_3\to\mathscr A_1$ 的真实束态射，
所以其 charge 零、一的相应分量给
$$
[f_0^3a_0]_{1,0}=0,\qquad
[f_0^2f_1a_0]_{1,1}=0 .
$$
这里第二式可用该乘法的 charge 一系数
$2f_0f_1$，并除原单位二。
再将 $\mathscr A_3$ 的 charge 一等式乘 $f_0^2$，
由于 $41$ 为单位，得 $[f_0^3a_1]_{1,1}=0$。
于是 (8) 的 $\mathscr A_1$ 行也为零。

因此原全球连接核准确为
$$
\boxed{
\mathscr E_D=
\left\{(a_0,a_1)\in H^1(\mathscr A_4):
\begin{array}{l}
[f_0a_0]_{3,0}=0,\\
[41f_0a_1+44f_1a_0]_{3,1}=0
\end{array}
\right\},
}
\tag{9}
$$
并删除本来就没有的目标项。
这些系数是原 charge 四十所产生，不能把 $40$ 改为零。

在 $j=1$ 时只剩一条准确核：
$$
\boxed{
\mathscr E_D=
\ker\!\left[
H^1(\mathscr A_{4,0})
\xrightarrow{\ f_0\ }
H^1(\mathscr A_{3,0})
\right],\qquad \dim\mathscr E_D\le3.
}
\tag{10}
$$
在 $j=2$ 时保 (9) 的同一 $a_0,a_1$，且维数至多十四。
$f_0$ 不一定是单位，这些核仍可能非零。

## 4. 对全来源 finite-fiber 返回的准确加强

若原余乘子的零 charge **不恒为零**，则 $j=0$。
这比只在 $D=4b$ 时使用单项线束更一般：
$$
\boxed{
[Y^0](P/F^4)\ne0
\quad\Longrightarrow\quad
H^1(\mathscr V_4)=0,\quad \mathscr E_D=0
}
\tag{11}
$$
对本窗口全部 $D$ 成立。
此时一个原来源能否在同预算写成
$\mathscr V_1+\mathscr J_3$，确切只剩前注的
**实际有限纤维值**，不再另有全球连接类。

若余乘子的最低 charge 为一或二，则 (9)–(10) 是必须保的有限小矩阵。
它们没有把 $\mathscr T_D$ 的固定十九角、其它分歧或水平贡献删掉，
也没有把物理 $t=0$ 的二／三行商当整个有限层。

最终仍须让同一个 $W\in K_1$ 同时满足全部长前缀、短块、
原 $\Pi$、负水平读取和同一 $R,S$ 的 carry。
本注支付的是那个原全球拼接障碍的准确固定大小与真实系数，
不声称指定 forcing 已落像或已非零。

无新增数学数值运行。
