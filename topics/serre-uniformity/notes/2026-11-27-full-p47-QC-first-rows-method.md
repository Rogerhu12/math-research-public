# 原 full47 八CM盘的完整首层QC系数读取

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：有限消费者已实现，只有原CM首log和第三类回执实际齐备后才执行。**
每次请求明确列出要读的CM盘，缺一个原局部值就不启动该盘读取。
本方法直接应用R1103的已证整解析式，
不把全Hecke代数生成性替换成实际两行矩阵的秩。

## 1. 同一个原格与完整trace

仍取 $q=4513$，原 $J=\operatorname{Jac}(X_{\rm ns}^+(47))$。
R1093认证的生成元为
$$
P_0=B_qu_4,\qquad u_4=23y_{1728}-C_\infty,\qquad B_q=q+1-T_q.
$$
完整73列 $\lambda_0=q^{-1}\log P_0$ 的SHA已经登记；
它不是 $\log(u_4)/q$。
令 $H=T_3+T_5$，并在原73维Hodge基上取
$$
L=[\lambda_0,H\lambda_0,\ldots,H^{72}\lambda_0].
$$
R1093付 $L$ 可逆，从而 $M=\mathbf Z_q[H]P_0$、
$\log M=q\operatorname{Lie}$。

R1101提供固定73个小奇Hecke基的准确变基矩阵 $C$，
R1102提供这些基的全部73个原高度 $g_n$。
后继只消费这些小值，不重算任何2/47/奇好局部交数。
按R1102原trace/resolvent式解
$$
m=C^{-1}g,\qquad
\operatorname{Tr}(\kappa H^j)=m_j,\qquad
K=\kappa/a,\qquad a=(T_2-1)/2.
$$
核原 $\kappa$、moments、Gram、resolvent的全部SHA，
以及Norm$(K)=2992$、det$(q^{-1}h)=3972$。
实际高度是
$$
q^{-1}h(xP_0,yP_0)=\operatorname{Tr}(Kxy).
$$
这里的trace保全部73方向/28个整块；
16个一次块只作为既有输入的一部分，绝不取代完整trace。

## 2. 原八个切向和全部23角的实际坐标

八个原coarse参数都取 $z=j-j_{\rm CM}$。
R1105给原95值，经同一个73行Hodge核得到 $e_y$；
其Mordell–Weil格坐标是
$$
b_y=L^{-1}e_y.
$$
完整grid、短heat及coarse三哈希逐项与R1105比较；
Gaussian/cubic的自同构、原KS尺度和原两phase均保留。

R1106给全部实际角的多项式 $R_C=p_C(H)$。
后继只按其原CM76循环评价和完整角纤维再生必要输入，
核全部旧目标/角和/最终坐标的SHA。
未保存的原大矩阵留在runner内存。
代码重新得到的旧同维对象只有在原hash准确一致后才使用。

R1093的73维 $\lambda_0$ 没有作为raw向量保存。
其消费者按原固定47基与源码再生该必要输入，
直接核旧已登记的完整73列SHA；
不另开搜索、不把这个输入再生登记成新高矩结果。

Sage与pure-Python/flint仍用fresh-exec隔离，
只有整数JSON跨进程。
旧实际角、切向与原标记均不通过不明abstract同构搬运。

## 3. 四基本CM首log给完整八列

实际新输入是R1108模平方方法的四列
$$
\lambda_y=q^{-1}\log(23y-C_\infty),\qquad
y=y_{-3},y_{-4},y_{-7},y_{-8}.
$$
每条必须来自完整 $N$ 链和实际 $E'\bmod q=D_0$ 的末端归一；
完整记录、73列SHA、$N$ 的原hash及其余数551都固定。

写 $c_y=L^{-1}\lambda_y$，用R1108原CM Hecke关系取得
$$
\begin{aligned}
c_{-16}&=(T_2-1)c_{-4}/2, &
c_{-12}&=T_2c_{-3}/3,\\
c_{-27}&=(T_3-1)c_{-3}/3, &
c_{-28}&=(T_2-2)c_{-7}.
\end{aligned}
$$
这些是原有理点类和原$T_2,T_3$上的准确等式，
保原23尺度，不从有限域约化类猜首log。
所有多项式运算在实际 $T/q=\mathbf F_q[H]$ 中完成。

## 4. 两个原对应的完整Chow–Heegner类

固定
$$
Z_A=13R_0+4R_2,\qquad Z_B=2R_4-7R_0.
$$
R1078/R1106的原fixed-cycle给
$$
\begin{array}{c|cc}
 &F_4&F_3\\ \hline
Z_A&13R_{20}+4R_5&13R_4\\
Z_B&-7R_{20}&2R_{12}-7R_4 .
\end{array}
$$
两个对应的cusp系数都为8；
虽然最后的degree-zero类公式中它会消去，
实际第三类除子中没有删除该项。

R1103证明
$$
23d_{Z,y}=\tfrac12F_4(Z)u_4+\tfrac23F_3(Z)u_3-2Zu_y.
$$
因此实际格坐标准确为
$$
d=\frac{\tfrac12F_4c_{-4}+\tfrac23F_3c_{-3}-2Zc_y}{23}.
$$
所有$\tfrac12,\tfrac23,\tfrac1{23}$都在程序中保留。

另一个实际输入是同一 $D_{Z,y}$ 在目标自身 $y$ 的
$$
\alpha_{Z,y}
 =N^{-1}d\log\bar f_{D_{Z,y}}/dz\bigm|_y.
$$
有限Miller执行用完整 $6D$，所以其输出已经除以
$6\epsilon N$；消费者不再除六，也不删符号。
必须用本盘自己的 $\alpha$，
不能用某条记录对其它CM点的导数冒替本盘第三类除子。

## 5. 新的两行矩阵及准确完成判据

R1103在整个原盘 $z=qt$ 上给
$$
\bar f_{Z,y}(t)=t(B_{Z,y}+A_{Z,y}t),
$$
其中
$$
A_{Z,y}=-\operatorname{Tr}(KZb_y^2),\qquad
B_{Z,y}=\operatorname{Tr}(Kb_yd)-\alpha_{Z,y}.
$$
本次新计算只进行这两个完整trace及两行矩阵的读取。
每行分别输出全局线性项和实际局部$\alpha$，
以便准确辨认它们的差；同时保 $b_y,d$ 的原坐标hash。

对每个请求的盘，构造
$$
\begin{pmatrix}A_{A,y}&B_{A,y}\\A_{B,y}&B_{B,y}\end{pmatrix}
$$
并实际求两个多项式 $t(B+At)$ 的gcd。

**可宣称整个原4513盘只余原CM点的充分且本程序使用的条件**：
gcd恰为$t$，而且至少一条$B$非零。
对这两个至多二次的原方程，这等价于
矩阵rank2，或两条$A$都为零而某条$B$非零。

理由完全沿R1103：共同剩余零只有$t=0$；
至少一条方程在零处的导数为单位。
整restricted-analytic全尾和Hensel唯一性因而控制整个原盘，
不是只得到一个未知大小的更深邻域。

若gcd是$t^2$，即使剩余根集合也只有零，
程序仍不宣称唯一，因为零可能是重根。
rank1且有额外剩余根、或全部首项为零，也保持未决；
继续其它对应或更高精度，不把这次首层失败当作理论不可能。

## 6. 已付全局支撑与范围

全部非$q$局部项沿R1103 §6.1的整Poincaré刚化消失；
坏47项沿R1074原whole-tube支撑证明。
原全局高度的各2/47/奇好交数已由R1102统一付清。
这些来源和原整尾证明固定在请求中；
当前程序不会用仅在一组测试点消失来替换它们。

每次只对列明的CM盘输出唯一/未决。
所有八盘都成功之后，才可结合R1074/R1086关闭本固定level47的分类。
有限level47仍不达到课题README的Serre绝对一致性完成标准。

## 7. 执行与保存

计划固定Sage10.6、python-flint0.9.0隔离、数学2400秒/reserve60。
执行请求必须已经含四个完整CM首log和各指定盘两条完整$\alpha$记录；
本说明未提供的数值不预填、不用猜值。

只提交源码、参数、小的$(A,B)$结果、run/job及SHA；
完整旧95×836矩阵、全角目标值、CM高长级数和trace中间矩阵不保存。
未执行或未完成时没有新盘排除结论。
