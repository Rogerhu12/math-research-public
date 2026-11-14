# R67：同时取小范数类代表与更强的商域增长界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的无条件必要条件。** 本文继续 R63，仍假设实际商域的类数大于一。改进不是增加局部条件，而是同时使用全部理想类的小范数代表：如果类数很大，某个固定的多项式范数界内就必须已经有很多不同的非主分裂素数。因此在这一分支不必使用 R62 逐次避素造成的 $9^t$ 增长。

对全部 $p>37$ 的实际完整非分裂正规化子异常，若 $D=|D_K|$、$h_K>1$，得到完全显式的有限参数界，以及
$$
\boxed{\quad
\liminf\frac{\log D}{(\log\log p)^2}
\ \ge\ \frac1{2\log2}
\quad}
\tag{67.1}
$$
沿任意假想的 $p\to\infty$ 异常序列成立。R63 的同一系数为 $1/(2\log18)$。这里仍是判别式增长的**下界**，不排除判别式同时趋于无穷，也不处理类数一。

## 1. 精确陈述

设 $E/\mathbb Q$ 无 CM，$p>37$，且
$$\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p).$$
令 $K$ 为二次商域，$D=|D_K|$，$h=h_K>1$。由 R5、R62，$K$ 虚二次，$p$ 惰性，$D\ge15$。下文全部对数为实自然对数。

置
$$
B=8D^{5/2},\qquad b=\log B,\qquad
L=\left\lfloor\frac b{\log3}\right\rfloor,\qquad
C=\log(2L+1),\qquad y=\log h.
\tag{67.2}
$$
特别地 $L\ge8$，$C>0$。

**定理 67.1。** 对任何满足
$$2tC\le y\tag{67.3}$$
的正整数 $t$，令 $m_t=\lfloor h^{1/t}\rfloor$，则
$$
\boxed{\quad
\log p<2^{t-1}\bigl(\log4+6tm_tb\bigr).
\quad}
\tag{67.4}
$$
这一式不要求 GRH、有效 Chebotarev、素数在二次型中的渐近分布，或类群有特定结构。

为给每个 $h>1$ 都能使用的显式界，置
$$
a=\log2,\quad t_0=\left\lceil\sqrt{y/a}\right\rceil,\quad
R(C)=\frac C{\sqrt a}+\sqrt{\frac{C^2}{a}+2C}.
\tag{67.5}
$$
若 $y\ge2Ct_0$，有
$$
\log p<
\bigl[\log4+6b(1+\sqrt{y/a})\bigr]
\exp(2\sqrt{ay}).
\tag{67.6}
$$
若 $y<2Ct_0$，有
$$
\log p<28b\exp\bigl(2\sqrt{\log18}\,R(C)\bigr).
\tag{67.7}
$$

**定理 67.2。** 置 $x=\log D$、$Y=x/2+\log x$，并用 (67.2) 中由 $D$ 给出的 $b,C$。则
$$
\boxed{\quad
\log\log p<\max\left\{
\begin{aligned}
&2\sqrt{aY}+\log\bigl[\log4+6b(1+\sqrt{Y/a})\bigr],\\
&2\sqrt{\log18}\,R(C)+\log(28b)
\end{aligned}
\right\}.
\quad}
\tag{67.8}
$$
尤其
$$
\log\log p\le\sqrt{2\log2\,\log D}+O(\log\log D),
\tag{67.9}
$$
这里的 $O$ 常数是绝对且有效的，(67.8) 已给不含隐常数的原式。于是得到 (67.1)；对任意明确的 $0<c<1/(2\log2)$，还可由 (67.8) 有效求出阈值，使阈值以上
$$D>\exp\bigl(c(\log\log p)^2\bigr).\tag{67.10}$$

## 2. 全部类都具有同一个多项式范数界

**引理 67.3。** 每个理想类 $c\in\operatorname{Cl}(K)$ 都有一个整理想代表 $\mathfrak b_c$，满足
$$
N\mathfrak b_c<B,\qquad (N\mathfrak b_c,2D)=1.
\tag{67.11}
$$

**证明。** 主类取 $\mathcal O_K$。对任意非主类，选取其逆类的原始约化正定二次型
$$Q(X,Y)=uX^2+vXY+wY^2,\qquad v^2-4uw=-D.$$
有 $|v|\le u\le w$、$u<\sqrt D$、$|v|<\sqrt D$、$w\le D$。

这是 R62 引理 62.2 中 $P=1$ 的构造，但现在对**每个类**作一次，故重述必要步骤。若 $Q(z,1)$ 模二不是零函数，取 $s=1$ 及一个使它为奇数的 $z\bmod2$；否则由原始性必为 $u,v$ 奇、$w$ 偶，取 $s=2$、$z$ 奇即可。对每个奇素数 $r\mid D$，$s$ 为单位，且 $Q(z,s)$ 是次数至多二的非零多项式；在 $\mathbb F_r$ 中可选非零值。

CRT 给 $0\le z<\operatorname{rad}(2D)\le2D$，使
$$n=Q(z,s),\qquad(n,2D)=1.$$
因 $s\le2$、$D\ge15$，
$$
n<4D^{5/2}+4D^{3/2}+4D<8D^{5/2}=B.
$$
令 $\theta=(-v+\sqrt{-D})/2$、$\mathfrak a=(u,\theta)$，则
$$\gamma=uz-\theta s\in\mathfrak a,\qquad N\gamma=uQ(z,s).$$
所以 $\mathfrak b=(\gamma)/\mathfrak a$ 为范数 $n$ 的整理想，其类为 $[\mathfrak a]^{-1}$，正是指定的类 $c$。证毕。

这里没有要求这些代表本身为素理想，也没有断言它们的每个素理想因子都非主。

## 3. 类数迫使固定界内已有很多非主分裂素数

记 $\mathcal P_B$ 为满足下列条件的有理素数的集合：

1. $q<B$、$q\nmid2D$；
2. $q$ 在 $K$ 分裂；
3. $q$ 上方的素理想非主。

两支互为逆类，故第三个条件与选择哪一支无关。令 $r=|\mathcal P_B|$。每个 $q\in\mathcal P_B$ 任取一支 $\mathfrak q_q$。

**引理 67.4。** 有
$$
\boxed{\quad h\le(2L+1)^r,\qquad r\ge\frac{\log h}{\log(2L+1)}=\frac yC.\quad}
\tag{67.12}
$$

**证明。** 对任意类 $c$，取引理 67.3 的代表，分解为素理想之积。没有分歧素数和二进素数；惰性素理想为 $(q)$，类平凡；主分裂素理想的因子同样不改变类。

剩余因子来自 $\mathcal P_B$。写 $\mathfrak q_q$、$\bar{\mathfrak q}_q$ 的重数为 $a_q,b_q\ge0$。因两支之积为主理想 $(q)$，
$$c=\prod_{q\in\mathcal P_B}[\mathfrak q_q]^{e_q},\qquad e_q=a_q-b_q.$$
而 $q\ge3$、$N\mathfrak b_c<B$ 给
$$3^{|e_q|}\le q^{a_q+b_q}\le N\mathfrak b_c<B.$$
所以对每个 $q$，都有 $|e_q|\le L$。这说明盒子
$$\{-L,-L+1,\ldots,L\}^{\mathcal P_B}$$
到类群的乘积映射是满射。盒子大小为 $(2L+1)^r$，得到 (67.12)。证毕。

这一步同时处理高阶循环类群和大二挠类群。即使某个类原先有范数很小的分歧代表，也先用 (67.11) 换成与 $2D$ 互素的代表，故不能把分歧二挠类漏出计数。

## 4. 直接在固定界内选择辅助素数

若 (67.3) 成立，引理 67.4 给 $r\ge2t$。于是可以选取 $2t$ 个不同的非主分裂奇素数
$$q_1,\ldots,q_{2t}<B.\tag{67.13}$$
不再逐次把已选素数放进 CRT 模数。

先定义最终比较上界
$$\mathcal U_t=(4B^{6tm_t})^{2^{t-1}}.\tag{67.14}$$
因为 $t\ge1,m_t\ge1,B>1$，有 $\mathcal U_t>4B$。若
$$p\le4\max_iq_i,$$
则已经有 $p<4B<\mathcal U_t$，从而得到 (67.4)。这个分支也包含潜在乘法约化导致 $p\mid q_i-1$ 的情形。

以下假设 $p>4\max_iq_i$。R63 的实际局部好约化构造给整数迹 $a_i$ 及 Frobenius 根 $\pi_i$，满足
$$\pi_i^2-a_i\pi_i+q_i=0.$$
其二次域 $F_i=\mathbb Q(\pi_i)$ 虚二次、$p$ 惰性，且 $F_i\ne K$：否则 $\pi_i$ 的范数为 $q_i$，便使 $q_i$ 上方的素理想主，矛盾。

R62 引理 62.3 的平方类超平面选择给其中 $t$ 个指标，使
$$K\cap F=\mathbb Q,\qquad F=F_1\cdots F_t.$$
重新编号后，所选 $q_1,\ldots,q_t$ 仍各小于 $B$。其最大实子域满足
$$[F^+:\mathbb Q]\le2^{t-1}.\tag{67.15}$$

固定各 $q_i$ 上方的一支 $\mathfrak q_i$。因 $(m_t+1)^t>h$，类群中有非零关系
$$\prod_{i=1}^t[\mathfrak q_i]^{u_i}=1,\qquad |u_i|\le m_t.$$
将负指数换成共轭支，得到有向整理想
$$
\mathfrak r=\prod_i\mathfrak q_i^{\max(u_i,0)}
\bar{\mathfrak q}_i^{\max(-u_i,0)}=(\alpha),
$$
其范数满足
$$N=\prod_iq_i^{|u_i|}<B^{tm_t}.\tag{67.16}$$
关系非零、每个有理素数只占一支，故 $\mathfrak r\ne\bar{\mathfrak r}$。

现在使用 R63 的**十二次幂实迹范数引理**，它已经覆盖全部 $p>37$：主理想公式是 $\lambda^{12}((\alpha))=\alpha^{12}\bmod p$；比较实际局部 Frobenius 根乘积的十二次幂实迹，若差为零，就会迫使非实的 $\alpha^{12}$ 落在 $K\cap F=\mathbb Q$，矛盾。该引理给
$$
p<(4N^6)^{[F^+:\mathbb Q]}
<(4B^{6tm_t})^{2^{t-1}}=\mathcal U_t.
$$
取对数得到 (67.4)。这一步沿用 R63 的实际有限惯性、总分歧好约化扩张、共同剩余嵌入和非零性证明；没有把抽象二次域中的任意代数整数代替实际 Frobenius 根。

## 5. 参数优化及少素数分支

取 $t_0=\lceil\sqrt{y/a}\rceil$。若 $y\ge2Ct_0$，定理 67.1 可用。由于
$$
a(t_0-1)<\sqrt{ay},\qquad
\frac y{t_0}\le\sqrt{ay},\qquad
t_0\le1+\sqrt{y/a},
$$
有
$$
2^{t_0-1}m_{t_0}\le
\exp\bigl(a(t_0-1)+y/t_0\bigr)
<\exp(2\sqrt{ay}).
$$
同时 $2^{t_0-1}<\exp(\sqrt{ay})\le\exp(2\sqrt{ay})$，将两项分别代入 (67.4) 即得 (67.6)。这里指数底数只剩 $2$，来自真实多二次实子域的次数。

若 $y<2Ct_0$，则
$$y<2C(1+\sqrt{y/a}).$$
令 $w=\sqrt y>0$，解二次不等式
$$w^2-\frac{2C}{\sqrt a}w-2C<0$$
得到
$$\sqrt y<R(C).\tag{67.17}$$
R63 已证明全部参数都满足
$$\log p<28b\exp(2\sqrt{\log18\,y}).$$
代入 (67.17) 就得到 (67.7)。因此“小范数界内数量的已知下界不够使用最优 $t$”不会留下一个未处理分支；它本身强迫类数参数小，旧界已经足够。

## 6. 消去类数、渐近系数与有效性

R58/R62 的基本理想计数给
$$h<\sqrt D\log D,$$
故
$$y<Y=\tfrac12x+\log x,\qquad x=\log D.$$
(67.6) 的右边随 $y$ 单调增加；(67.7) 已经只依赖 $D$。分别取对数并用较大者统一两分支，得到 (67.8)。

当 $x\to\infty$，
$$
b=\tfrac52x+\log8=O(x),\qquad
C=\log(2\lfloor b/\log3\rfloor+1)=O(\log x),
$$
且
$$R(C)=O(C)=O(\log x).$$
所以 (67.8) 的第二项为 $O(\log x)$。第一项中
$$
2\sqrt{aY}=\sqrt{2ax}+O\!\left(\frac{\log x}{\sqrt x}\right),
$$
而对数因子为 $O(\log x)$。这证明 (67.9)，并保留明确有效的原式 (67.8)。

沿假想 $p\to\infty$ 异常序列，R63 的固定 $D$ 显式界首先强迫 $D\to\infty$。将 (67.9) 除以 $\sqrt{\log D}$ 得
$$
\limsup\frac{\log\log p}{\sqrt{\log D}}
\le\sqrt{2\log2}.
$$
两边为正，平方、倒数后得到 (67.1)。

关于有效阈值，给定 $0<c<1/(2\log2)$，以 (67.8) 的显式右端逐项作初等上界即可找出 $x_0$，使全部 $x\ge x_0$ 时该右端小于 $\sqrt{x/c}$。例如先用 $b\le4x$、$C\le\log(9x)$、$R(C)\le2C/\sqrt a+\sqrt{2C}$（均在本题 $x\ge\log15$ 范围成立），再以 $\log x/\sqrt x\to0$ 的明确单调尾界处理余项。对 $x<x_0$，R63 的右端又给明确的 $p$ 上界。因此可有效转为“所有充分大的实际 $p$”所用的阈值，而不只是一个无效渐近陈述。

## 7. 本结果完成和未完成的接口

本结果把“反复构造任意多个非主分裂素数”的粗增长，替换为一个由全部小范数类代表强迫的数量下界。它既不假定类群循环，也不漏掉由分歧素理想生成的二挠部分；不使用素数分布定理。所有辅助素数仍为实际局部整数 Frobenius 比较可用的分裂素数，交域条件也仍经过 R62 的选择论证。

它没有给 $D$ 的上界，没有排除 $h=1$，也没有识别 QC 函数的共同根。尤其 (67.1) 允许 $D$ 比所示下界增长得更快，不能把这个必要条件写成 Serre 一致性的证明。对有限参数，(67.8) 与 R63 原有界可以取较小者，本文不宣称新的有限常数在每个小参数上都更优。

## 8. 依赖及来源

- [R62](R62-many-prime-relations-and-effective-quotient-bound.md) 引理 62.2：原始约化二次型、模二例外处理和 CRT 小范数代表；引理 62.3：平方类空间的超平面选择。
- [R63](R63-all-prime-classes-and-quotient-discriminant-growth.md)：全部 $p>37$ 的十二次幂主理想式、真实局部好约化整数迹及非零实迹范数界；本文少素数分支也使用该文已证显式界。
- [R58](R58-ring-class-splitting-and-small-split-primes.md)、R62：Minkowski 理想类代表及 $h<\sqrt D\log D$ 的初等计数界。背景来源为 J. S. Milne, *Algebraic Number Theory*, v3.08，Theorem 4.3，[作者讲义](https://www.jmilne.org/math/CourseNotes/ANT.pdf)。

新输入是引理 67.3–67.4 的同时类代表计数，以及它与真实多素数范数界的两分支优化；完整证明均已写出。
