# R840 联合交增补 — 原单尾／双尾的完整厚 jet 与同一个底导数标号

日期：2026-11-16。**状态：以下原有限尾行的准确 jet 形式、单位转置和全局选择相容已证明。它仍不是同一高前缀的可解性或指定 forcing 的非零判定。**

本注接 [完整联合交](2026-11-16-r840-full-primitive-and-ramification-ideal-intersection.md) 与 [非水平厚块](2026-11-16-r840-nonhorizontal-confluent-joint-operator-and-two-tails.md)。把后者尚以“最后两行”表示的部分写成同一真实截面的明确厚 jet。没有增加新的来源列或独立点参数。

## 1. 同一实际来源

保原 $\mathcal H_j=H^0(X,\mathcal O_X(jC))$、$C=(F)$、$\mathcal E=Y\partial_Y$、
$e=\mathcal EF$ 及 $3b<p$。在完整联合交的呈示中，先取同一个
$$
W=FH+eK\in\mathcal H_3,\qquad
\mathcal EW=FJ,\qquad H,K,J\in\mathcal H_2.
\tag{1}
$$
这里 $J$ 是商截面；原函数子空间仍记为 $\mathcal J$。
完整有限算子是
$$
\mathcal O(a,B)=J|_Z,\qquad Z=V(F,e).
\tag{2}
$$
$\mathcal O=0$ 给的是完整呈示中可用同一 $F^2C$ 修正的条件；
该修正仍须实际选取以令 $J|_C=0$。
不能把尚未修正的 $J|_Z=0$ 直接当成 $J|_C=0$。

取原移动非水平点 $Q$，要求 $F_t(Q)\ne0$、
$Y_Q\ne0,\infty$，且不在原固定角。用同一剩余域 $k_Q$ 和原坐标
$$
x=Y-Y_Q,\quad u=Y_Q+x,\quad
\tau=t(x)-t_Q,\quad \mathscr D=u\,\frac d{dx}.
$$
设
$$
2\le m=\operatorname{ord}_x\tau\le b,\qquad
e_C=x^{m-1}v(x),\quad v(0)\ne0.
\tag{3}
$$
原非水平厚块已付
$$
\mathscr D\tau=-e_C/F_t,\qquad
Z_Q=\operatorname{Spec}k_Q[x]/(x^{m-1}),\qquad
\operatorname{ann}_{Z_Q}(f_2)=(x)/(x^{m-1}).
\tag{4}
$$
本注只作小于 $2m+1$ 的有限运算；$3b<p$ 保所有用到的整数为单位。
没有在正特征中使用完整形式导数的核仅由常数组成。

## 2. 完整尾行的三个等价式

记 $W_C=W|_C$，并置
$$
\boxed{\lambda_Q=W_t(Q)\in k_Q.}
\tag{5}
$$
这是 (1) 的真实固定 $t$ 偏导值。

**定理。** 对同一个 (1)，下列条件准确等价：
$$
\boxed{\mathcal O_Q(a,B)=0;}
\tag{6a}
$$
$$
\boxed{(W_t)|_C-\lambda_Q\in (x^m);}
\tag{6b}
$$
$$
\boxed{W_C-\lambda_Q\tau\in (x^{2m});}
\tag{6c}
$$
$$
\boxed{K_C-\lambda_Q\,\tau/e_C\in (x^{m+1}).}
\tag{6d}
$$
其中 (6d) 使用真正的 $K_C=W_C/e_C$；$\tau/e_C$ 正规且恰为一次零。

**证明。** 将 $\mathcal EW=FJ$ 限制到 $C$，以及在固定 $t$ 框中先对 $t$ 求导再限制，分别得到
$$
\mathscr D W_C=-\frac{e_C}{F_t}(W_t)|_C,
\qquad
\mathscr D((W_t)|_C)
 =F_tJ|_C-\frac{e_C}{F_t}(W_{tt})|_C.
\tag{7}
$$
第二式完整保留同一个 $W_{tt}$。它在 $Q$ 正规，而 $F_t,u$ 均为单位。
所以 $J|_C\in(x^{m-1})$ 当且仅当
$d((W_t)|_C)/dx\in(x^{m-1})$。
因 $m<p$，这个有限条件准确等价于 (6b)。

由第一式及 (4)，
$$
\frac d{dx}(W_C-\lambda_Q\tau)
 =\tau'(x)\big((W_t)|_C-\lambda_Q\big).
\tag{8}
$$
$\tau'$ 的阶恰为 $m-1$。由于 $W_C(Q)=0$（来自 $W=FH+eK$）、
$\tau(Q)=0$，且 $2m<p$，有限系数积分给 (6b)$\Rightarrow$(6c)。
反之，对 (6c) 求导，再除以 $\tau'$，得到 (6b)。
最后 $e_C$ 的阶为 $m-1$，所以 (6c) 与 (6d) 等价。证毕。

特别地，误差必须写为 $x^{2m}$，不能擅自改成 $x^{2m+1}$。
真正 $W\in\mathcal J$ 时已有更长 Taylor 式
$W_C=\lambda_Q\tau+\tfrac12W_{tt}(Q)\tau^2+O(x^{2m+1})$；
其中实际 $\tau^2$ 项正好从 $2m$ 开始，属于本注保留的后续高尾。

## 3. 与原单尾、双尾的单位对应

先在 $m\ge3$ 时执行已付的 $m-3$ 个原单位低行消元。于是
$K_C\bmod x^{m-1}$ 落在唯一核线
$k_Q\,\tau/e_C$，而 (7) 表明其标号准确为 (5)。

定义两个真实尾系数
$$
\boxed{
\Xi_Q(a,B)=
\left[
\frac{K_C-\lambda_Q\tau/e_C}{x^{m-1}}
\right]_{<2}
\in k_Q[x]/x^2.
}
\tag{9}
$$
式中分子在原低行满足后才具有显示整除性。
两个系数来自同一 $K_C$ 的 $x^{m-1},x^m$ 项，
不能在不同点独立指定。

在非水平厚块注的完整微分表达中，作用于 $x^j$ 的首系数为
$$
-Y_Q^2(j-1)(j+m-1)x^{j-2}.
$$
因此原第 $m-3,m-2$ 行到 (9) 的变换是下三角单位变换，
两个对角因子准确为
$$
\boxed{
-Y_Q^2(m-2)(2m-2),\qquad
-Y_Q^2(m-1)(2m-1).
}
\tag{10}
$$
它们在 $m\ge3$、$3b<p$ 下均为单位。
故 (6) 正是两个原尾行同时为零，而非额外的厚 jet 条件。

当 $m=2$ 时，原零化子本来为零。由 (7)，
$\lambda_Q=W_t(Q)$ 已使 $K_C-\lambda_Q\tau/e_C$ 的一次项消失；
所以 (9) 的常数项自动为零。唯一剩余系数是其一次项，
对应原唯一目标行，单位因子为
$$
\boxed{-3Y_Q^2.}
\tag{11}
$$
这样简单分歧点仍只有原一个行，不能误添第二个条件。

## 4. 全局选择与后续前缀

完整联合交的提升改变保持同一个 $W$。
沿 $C$，$K_C=W_C/e_C$ 因 $C$ 整而唯一，所以
$\lambda_Q$ 和 (9) 随那些改变准确不变。
在局部框或参数改变时，它们按同一实际单位 jet 变换；
其零条件及原单尾／双尾的数目不变。
所有非有理点均保其实际剩余域；原域上的矩阵由同一个有限映射下降，
不把共轭点拆成独立来源。

完整呈示中的 $C\mapsto C+cF$ 改变 $W$ 为 $W+cF^3$。
它不改变 $W_C$ 或 $(W_t)|_C$，因而 (5)、(9) 看不见这个方向。
但它在原第三长行中仍产生 $6ce_P^3\eta$，并继续进入同一第四短行。
因此本注没有删除最后的同一个 $c$。

同时必须区分两种出现的 $K$。
本注 (1) 的 $K$ 用来识别冗余来源
$\mathcal I\cap\mathcal J$；在真正三长核中，给定一个
$W\in\mathcal J$ 后，还要用同一个全局修正
$G=F H_{\rm corr}+eK_{\rm corr}+W$ 满足
$$
e(K_{\rm corr})_C+W_C\in H^0(C,N^3(-TP)),
$$
$$
e(H_{\rm corr})_C+f_2(K_{\rm corr})_C
       +e(\mathcal EK_{\rm corr})_C
 \in H^0(C,N^3(-TP)),
\qquad T=s-r-13.
\tag{12}
$$
(9) 只支付前一个来源商的准确尾矩阵，
不直接约束任意 (12) 的 $K_{\rm corr}$。
其后仍须保同一个第三 $3\eta$ 镜轴、原第四短行、
全部十九角和物理十三带。没有从局部 (6) 推出
$W_T$ 的满射、指定 trace 为零或原 $M$ 的新 Smith 因子。
无新数学程序运行。
