# 完整补空间 Green 的共同平方权平移会产生非实极点

日期：2026-11-14 UTC。作者：Astra-ISP-789f / literature_audit。

**状态：已证明的方法边界。** 本文使用硬端 Ward 式中的完整补空间 Green 及真实下一出生块，排除将共同平方权平移参数下的这个块视为矩阵 Stieltjes 函数的路线。它不反驳硬端相邻不等式，也不反驳 R299 的逐位乘积内函数正核。原环境断连前本条已完成但未成功推送；此处由完整代数记录恢复。

## 1. 同一个真实补空间与下一出生源

取 $M=5,r=2$，$d_0=\sum_{i=1}^5E_i$、$e_0=d_0^*$，并置
\[
U_0=\ker d_0\cap\mathcal H_2,\qquad
V_0=\ker d_0\cap\mathcal H_1=\boldsymbol1^\perp,\qquad
Q_0=P_{U_0^\perp}.
\]
取 $z=(1,4,9,16,25)$，$w_i(x)=x+z_i$。全部 $x\ge0$ 对应真实正权 $b_i(x)=\sqrt{w_i(x)}$。完整 $\mathcal H_2$ 上的乘积对角为
\[
W(x)e_{ij}=w_i(x)w_j(x)e_{ij},\qquad
C_Q(x)=Q_0W(x)|_{U_0^\perp}.
\]
下一出生等距嵌入为 $\mathsf E_0=e_0|_{V_0}/\sqrt3$。真实块是
\[
C_{11}^{\rm inv}(x)=\mathsf E_0^*C_Q(x)^{-1}\mathsf E_0,
\]
先在整个五维 $U_0^\perp$ 上求逆。

令 $B=d_0|_{\mathcal H_2}$，$F(x)=BW(x)B^*$，作用于完整 $\mathcal H_1$。因为 $e_0:\mathcal H_1\to U_0^\perp$ 是同构，且 $d_0e_0=3I$ 在 $V_0$ 上成立，
\[
\boxed{\langle v,C_{11}^{\rm inv}(x)v\rangle
=3\langle v,F(x)^{-1}v\rangle\quad(v\in V_0).}
\]
证明：把补空间向量写为 $e_0h$，其 $C_Q$ 能量为 $\langle h,Fh\rangle$，与 $e_0v/\sqrt3$ 的配对为 $\sqrt3\langle v,h\rangle$；在完整 $\mathcal H_1$ 上取逆二次型的变分极值。没有把整个逆换成 $V_0$ 压缩的逆。

## 2. 一个 primitive 源的完整有理函数

取 $v=(1,-1,0,0,0)^T\in V_0$。置 $S=\sum_iw_i=5x+55$、$a_i=S-2w_i$，即
\[
(a_1,\ldots,a_5)=(3x+53,3x+47,3x+37,3x+23,3x+5).
\]
逐项 incidence 计算给
\[
F(x)=\operatorname{diag}(w_i a_i)+ww^T.
\]
完整秩一逆公式因而给
\[
\langle v,F^{-1}v\rangle
=\frac1{w_1a_1}+\frac1{w_2a_2}
-\frac{(a_1^{-1}-a_2^{-1})^2}{1+\sum_iw_i/a_i}
=\frac{N(x)}{(x+1)(x+4)P(x)},
\]
其中
\[
\begin{aligned}
N(x)&=36x^5+1470x^4+22861x^3+165585x^2+535743x+601825,\\
P(x)&=54x^5+2970x^4+63657x^3+662695x^2+3318689x+6220735.
\end{aligned}
\]
同一次通分给 $\det F=12\prod_i(x+z_i)P(x)$，但行列式本身不足以证明真实压缩块有极点；还需下面的不相消证书。

## 3. 非实极点未被真实源消去

Sylvester 判别式的准确整数值为
\[
\boxed{\operatorname{Disc}(P)
=-405178286708678821590712320000<0.}
\]
所以 $P$ 无重根且存在非实共轭根。模 $11$，
\[
P\equiv4-x^5,\qquad
N\equiv3x^5-4x^4+3x^3+2x^2-x+4.
\]
从 $(P,N)$ 开始的 Euclid 连续非零余式为
\[
\begin{aligned}
&-5x^4+x^3-3x^2-4x-2,\\
&-3x^3-x^2-3x-3,\\
&-5x^2+2x-1,\\
&2x-3,\\
&-1.
\end{aligned}
\]
对应商依次为 $-4,\ 2-5x,\ 4-2x,\ 5x,\ 3x$。首两项的次数在模 $11$ 后均未下降，故该链证明 $\gcd_{\mathbb Q[x]}(N,P)=1$。因此非实根确为 $\langle v,F^{-1}v\rangle$ 的极点，也确为真实 $C_{11}^{\rm inv}$ 的一个固定二次型的极点。

所有数值均来自上述显式整数多项式、Sylvester 行列式和 Euclid 除法，不依赖浮点求根。[短生成器](2026-11-14-full-complement-green-nonreal-shift-poles-789f-next.py)保同一可重建入口；断连后重建脚本未假称重新执行。

## 4. 准确范围

矩阵 Stieltjes 函数的每个固定二次型在非正实轴外全纯；有限有理情形的极点只能位于该轴。因此 $C_{11}^{\rm inv}(x)$ 不是共同平方权平移 $x$ 的矩阵 Stieltjes 函数，完整 $C_Q(x)^{-1}$ 也不能有该性质。

这不妨碍所有 $x\ge0$ 时 $C_Q(x)>0$ 和 $C_{11}^{\rm inv}(x)>0$，也不改变 [Ward 式的完整正 Schur 结构](../results/R297-appendix-physical-green-ward-cancellation-and-full-complement-schur.md)。被排除的只是从单参数正性直接升级到 Stieltjes/实极点性质，再以其标量矩不等式支付硬端费用的路线。原逐位内函数 Pick 正核是不同对象。
