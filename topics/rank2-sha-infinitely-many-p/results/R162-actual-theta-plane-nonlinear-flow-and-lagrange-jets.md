# R162. 实际 theta 平面的固定非线性方程与全深度矩阵

**状态：已证明；惰性饱和 jet 预算的严格改善仍未证明。**

在共同 $E_0:y^2=x^3-x$ 上，令 $s=x^{-2}=u^4$、
$\vartheta=\sigma/u$。R117 的原两行准确为

$$
A_2=\vartheta^{68}P(s),\qquad B=\vartheta^{68}Q(s),
\qquad V(s)=Q(s)/P(s)-1,
$$

其中 $P,Q\in s\mathbb Z[1/5][s]$ 是完整证明中显示的固定次数十六
多项式，首项均为 $s$，$V=-22s+\cdots$。
原正 theta 连接由同一个固定级数 $W=68\log\vartheta$ 保留，且

$$
4s(1-s)W''+(3-5s)W'=17,\qquad W(0)=0,
$$

$$
[s^m]W=\frac{17}{m}\prod_{j=0}^{m-1}\frac{4j+1}{4j+3}.
$$

代入固定有理参数 $V(s)$ 给出 R155 原 $F(V)$ 的明确二阶非线性方程。
没有据此声称固定阶数的标量线性 Mellin 递推。

采用 R158/R159 的真实平面源 $P_0(A_2,B)$。整基变换
$(X,Y)\mapsto(X,Y-X)$ 后，其列为
$A_2^jV^c$、$0\le c\le j\le D$。改用第一个坐标本身
$X=A_2=w+\cdots$ 作为输出参数，全部准确前缀核及其第 $k$ 阶
范数均不变；无需假设逆级数的高阶系数整。

写 $p_0=P(s)/s$。对 $n=k-j>0,c\ge1$，原矩阵的每一条目准确为

$$
\boxed{\quad
[X^{k-j}]V(s(X))^c
=\frac c n[s^{n-1}]
 V(s)^{c-1}V'(s)\,p_0(s)^{-n}e^{-nW(s)}.
\quad}
$$

这是同一个留数核的 Lagrange 公式，保留真实的 $n=k-j$ 指数及
$1/n$ 分母。若 $G=\log p_0+W$、
$e^{-nG}=\sum_m u_m(n)s^m$，则

$$
u_0(n)=1,\qquad
m u_m(n)=-n\sum_{h=1}^m h[s^h]G\,u_{m-h}(n),
$$

并有准确的 binomial 卷积
$u_m(n+n')=\sum_hu_h(n)u_{m-h}(n')$。
对固定 $m$，$u_m(n)$ 是次数至多 $m$ 的有理多项式。
这些式子为任意 $D,k$ 给出同一实际有限矩阵，不含未定周期。

下一步仍须共同消元全部列 $c\le j\le D$，证明 R159 平面所需的
严格惰性预算 $a_I+2b_I<2$。两个原中央导数的零性未被扩成
任意列的新整除；本结果未支付这个严格界。

见[完整证明](../notes/2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。
