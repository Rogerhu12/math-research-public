# 实际第二 Green 缺陷的双坐标闭性、统一下界与正角图表示

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下是两条原耦合方程给出的实际闭子空间结论。没有证明缺陷为零，没有证明这些子空间对 $B,S,T,T^*$ 不变，也没有把同 $W$ 的 $\Gamma$ 从闭包范围提升到实际范围。**

沿用[实际除法闭关系](R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)和[最大图域的相反前缀正则性](R271-appendix-maximal-division-graph-opposite-prefix-regularity.md)。两种原模型 $T=T_N,T_Y$ 均保全部 carry。记
$$
S=B^*,\quad M=\ker T,\quad N=\overline{BM},\quad
I=M^\perp,\quad W=M\ominus N,\quad G=G_0^*.
$$
置
$$
\mathcal C=\overline{\{(Sh,T^*h):h\in\mathcal H\}},\qquad
\mathcal E=\operatorname{Graph}G\ominus\mathcal C.
$$
已付的准确方程是
$$
(y,f)\in\mathcal E
\iff T^*y=Sf,\qquad By+Tf=0.                 \tag{0.1}
$$
因此 $y\in\mathcal D(G),\ Gy=f$，以及
$f\in\mathcal D(A_{\max}),\ A_{\max}f=-y$。
这里仍然是 $A_{\max}$，不是 $A_{\min}$。

## 1. 已付前缀估计及两个实际低块下界

采用
$$
V_n e_k=\mathbf1_{\{2^n\mid k\}}e_k,\qquad
Q_n e_k=\mathbf1_{\{2^n\mid k+1\}}e_k.
$$
$V_n$ 读全零低前缀，$Q_n$ 读全一低前缀。记
$$
\gamma_{\rm ex}
=\log2+\operatorname{arsinh}1+\frac25(1-2^{-1/2})>\frac53,
$$
$$
a_n=e^{-\gamma_{\rm ex}n+4(\log n+1)^2},\qquad
b_n=e^{-47n^4}\quad(n\ge2).
$$
对每个 $(y,f)\in\mathcal E$，前稿已经逐项支付
$$
\|V_ny\|\le a_n\|y\|+b_n(\|y\|+\|f\|),\qquad
\|Q_nf\|\le a_n\|f\|+b_n(\|y\|+\|f\|).     \tag{1.1}
$$

原 ruler 移位的正交列还直接给
$$
\|(I-V_n)y\|\le\alpha_{n-1}^{-1}\|By\|,\qquad
\|(I-Q_n)f\|\le\alpha_{n-1}^{-1}\|Sf\|.   \tag{1.2}
$$
第一式的来源是：非零整数 $k$ 不属于 $V_n$ 时
$v_2(k)\le n-1$，故对应 $B$ 权至少为 $\alpha_{n-1}$；
真空在 $V_n$ 中。第二式同理使用 $v_2(k+1)\le n-1$。
这两个下界没有把相反的两种前缀混用。

以下统一取
$$
t_*=6\ge\|T\|.
$$
N 型由 $\sum a_j<2,\ \|N_j\|=1$ 甚至可取 $2$；Y 型直接用完整原逆
$\|Y_j\|\le\|N_j\|\|(I+N_j)^{-1}\|\le3$，所以 $6$ 对两型同时有效。

## 2. 两坐标范数等价

由 (1.1)--(1.2) 及 (0.1)，只要 $a_n+b_n<1$，便有
$$
(1-a_n-b_n)\|y\|
 \le\alpha_{n-1}^{-1}\|By\|+b_n\|f\|
 \le(t_*\alpha_{n-1}^{-1}+b_n)\|f\|,
$$
$$
(1-a_n-b_n)\|f\|
 \le\alpha_{n-1}^{-1}\|Sf\|+b_n\|y\|
 \le(t_*\alpha_{n-1}^{-1}+b_n)\|y\|.        \tag{2.1}
$$

可给完全指定的常数而不作任何数值试算。取
$$
n_0=256,\qquad C=\frac{10}{\alpha_{255}}. \tag{2.2}
$$
因 $\log256<8$ 和 $\gamma_{\rm ex}>5/3$，
$$
a_{256}<e^{-308/3}<1/8,\qquad b_{256}<1/8.
$$
又 $\alpha_{255}<1$，故 (2.1) 在 $n_0$ 的系数至多
$$
\frac43(6\alpha_{255}^{-1}+1)
\le\frac{10}{\alpha_{255}}=C.
$$
因此
$$
\boxed{C^{-1}\|y\|\le\|f\|\le C\|y\|
\qquad((y,f)\in\mathcal E).}               \tag{2.3}
$$
这里 $C$ 极大，但为实际、有限且两型通用的常数。证明需要的是有界性，不是数值上的有效大小。

## 3. 真正闭的两坐标子空间

定义
$$
Y=\{y:(y,f)\in\mathcal E\text{ for some }f\},\qquad
X=\{f:(y,f)\in\mathcal E\text{ for some }y\}.
$$
$\mathcal E$ 是 $\mathcal H\oplus\mathcal H$ 中的闭子空间，因为 (0.1) 是两个有界算子的核条件。

若 $y_j\in Y$ 在 $\mathcal H$ 中收敛，(2.3) 应用于差对表明相应 $f_j$ 是 Cauchy 列；其极限仍在 $\mathcal E$。故 $Y$ 闭。交换两坐标，同样证明 $X$ 闭。零坐标只对应零对，仍由 (2.3) 可知。

于是
$$
\boxed{
L=G|_Y:Y\longrightarrow X
\text{ 是有界双射},\qquad
\|L\|\le C,\quad\|L^{-1}\|\le C,
\quad\mathcal E=\operatorname{Graph}L.}    \tag{3.1}
$$
这是实际 $\mathcal E$ 上的结论，不是对整个 $G$ 宣称闭值域或有界逆；后者已经被原实际反序列排除。

## 4. 耦合条件进一步给四个真实下界

取
$$
n_1=\max\left\{
256,\ \left\lceil
 \left(\frac{\log(4(1+C))}{47}\right)^{1/4}
 \right\rceil\right\},
\qquad
\beta=\frac{\sqrt3}{2}\alpha_{n_1-1}>0.    \tag{4.1}
$$
当 $n\ge256$ 时，$a_n$ 递减且小于 $1/8$。例如
$$
\frac{d}{dn}\log a_n
=-\gamma_{\rm ex}+\frac{8(\log n+1)}n<0
$$
在此区间成立。定义 (4.1) 保证
$(1+C)b_{n_1}\le1/4$，从而
$$
a_{n_1}+(1+C)b_{n_1}\le1/2.
$$
由 (1.1)、(2.3)，
$$
\|V_{n_1}y\|\le\tfrac12\|y\|,\qquad
\|Q_{n_1}f\|\le\tfrac12\|f\|.
$$
再用实际正交低块得
$$
\boxed{\|By\|\ge\beta\|y\|\quad(y\in Y),\qquad
       \|Sf\|\ge\beta\|f\|\quad(f\in X).}  \tag{4.2}
$$
最后按 (0.1) 配对同一个 $y,f$，得到
$$
\boxed{\|Tf\|\ge\frac{\beta}{C}\|f\|\quad(f\in X),\qquad
       \|T^*y\|\ge\frac{\beta}{C}\|y\|\quad(y\in Y).} \tag{4.3}
$$
所以 $BY,SX,TX,T^*Y$ 也都是闭子空间。这只使用相应有界算子在闭来源子空间上的正下界。

不能由 (4.3) 与 $T$ 的准幂零性推出 $X=0$：本文没有证明 $TX\subset X$，也没有证明其它所需不变性。

## 5. 输出与 $M$ 的正角，以及 $W$ 分量的有界图

先核清实际输出范围。对 $x\in M$，由 (0.1)
$$
\langle f,Bx\rangle
=\langle Sf,x\rangle
=\langle T^*y,x\rangle
=\langle y,Tx\rangle=0.
$$
所以 $X\subset N^\perp=I\oplus W$。

置
$$
\delta=\frac{\beta}{6C}>0.
$$
因为 $Tf=T P_I f$，(4.3) 给
$$
\boxed{\|P_I f\|\ge\delta\|f\|\quad(f\in X).} \tag{5.1}
$$
特别地，$X\cap M=\{0\}$；这比单独从两方程检查交为零强，因为 (5.1) 是统一正角。
对完整缺陷对还得到
$$
\boxed{
\|(y,f)\|_{\mathcal H\oplus\mathcal H}
\le \frac{\sqrt{1+C^2}}{\delta}\|P_I f\|.} \tag{5.2}
$$

令
$$
F=P_I X\subset I.
$$
由于 $X$ 闭且 (5.1) 给有界逆，$F$ 是真正闭子空间。定义
$$
Z:F\longrightarrow W,\qquad
Zv=P_M(P_I|_X)^{-1}v.
$$
这是有界算子，且
$$
\boxed{
X=\{v+Zv:v\in F\},\qquad
\|Z\|\le\sqrt{\delta^{-2}-1}.}             \tag{5.3}
$$
这里 $P_M f=P_W f$，因为 $f\in N^\perp$。
精确范数式
$\|v+Zv\|^2=\|v\|^2+\|Zv\|^2$ 与 (5.1) 给 (5.3)。

此外 $T|_F$ 也有下界：由 $TZv=0$ 和 (4.3)，
$$
\|Tv\|=\|T(v+Zv)\|
\ge\frac{\beta}{C}\|v+Zv\|
\ge\frac{\beta}{C}\|v\|.                  \tag{5.4}
$$
这仍不把 $F$ 当成不变子空间，不推出 $F\subset\operatorname{Ran}T^*$。

## 6. 两道范围问题在新闭图中的准确位置

记 $J=\overline{\operatorname{Ran}G}$。原闭关系已给
$I\subset J\subset N^\perp$。由于
$\operatorname{Graph}G=\mathcal C\oplus\mathcal E$，而 $\mathcal C$ 的第二坐标闭包恰为 $I$，(5.3) 直接给
$$
\boxed{J=I\oplus\overline{Z(F)}.}          \tag{6.1}
$$
确切地，$\mathcal C$ 的第二坐标都在 $I$；反向包含来自
$T^*\mathcal H$ 已在其中且稠密于 $I$。
对 $v\in F$，$v+Zv\in X\subset J$ 且 $v\in I\subset J$，故 $Zv\in J$；
这同时证明 (6.1) 的两向包含。

所以：

- 完整图核心 $\mathcal E=0$ 等价于 $F=0$；
- 第一**范围**恒等式 $J=I$ 等价于 $Z=0$，不要求先把 $F=0$ 证明出来；
- 第二范围恒等式 $J=N^\perp$ 等价于 $\overline{Z(F)}=W$。

这些是同一个实际闭图的范围身份，不能把 $F$ 或 $Z(F)$ 的闭性多写出来；本文只证明 $F$ 闭，未证明 $Z(F)$ 闭。

## 7. 保留的真实端点

这里的正下界建立在同一缺陷对同时满足两式 (0.1) 上；它不适用于只满足第一式的一般最大图来源，因而不与已登记的实际非闭值域及五坐标反序列矛盾。

原链同伦仍给
$$
\operatorname{diag}(S,S)(y,f)=(Sy,T^*y)\in\mathcal C,\qquad
\operatorname{diag}(T^*,T^*)(y,f)=(Sf,T^*f)\in\mathcal C.
$$
投回 $\mathcal E$ 后两式都是零，伴随压缩亦然。
这没有给予 $X,Y,F$ 的不变性。

尚需从原方程和同一来源证明 $Z=0$、或 $F=0$、或支付其它足以完成两道范围桥的实际输入。本文没有支付同 $W$ 的 $\Gamma$、完整 $C_2$ 费用或 $N=M$。
