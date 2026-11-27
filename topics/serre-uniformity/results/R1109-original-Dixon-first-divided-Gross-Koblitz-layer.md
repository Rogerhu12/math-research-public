# R1109 — 原退化 Dixon 函数的完整首 $p$ 除层

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；o1_theta。

**已证明下述完整模 $p^2$ 身份；它与原短 $\eta_k,\nu_k$ 的进一步比较仍未完成。**
本篇直接续 [R1061 §15](./R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)。
该节已经付款的全有限域值是 $1-p$，单位层只给加权半 Dixon 矩。
这里保留全部赋值一项、两位 Gamma 修正及整数阶乘提升，
不把第一位的除 $p$ 单位误认作原无权半和。

全篇只有纸面代数，没有数学程序执行。

## 1. 原函数与统一规范

写
$$
p=6k-1\ge41,\qquad N=k-1,\qquad n=2k-1,\qquad
q=p^2,\quad L=q-1,\quad
a=2L/3,\ c=L/6,\ h=L/2.
$$
沿用 R1061 的 $g_b=g(\omega_q^{-b})$，下标在 $0,\ldots,L-1$ 中读取，
包括 $g_0=-1$。该节的完整、含退化项的 McCarthy 函数为
$$
\mathcal H_q
=-\frac1{p^4L}
 \sum_{j=0}^{L-1}(-1)^j
 g_{a+j}^2g_{c+j}g_{-j}^2g_{h-j}
=1-p.
\tag{G.1}
$$
不在此重做其有限域 Dixon 证明。特别，分母是已经准确计算的
$p^4$，不是只知道它有赋值四。

若 $b=d+pe$，$0\le d,e\le p-1$、$b<L$，Gross–Koblitz 的准确式为
$$
g_b=-\varpi^{d+e}
 \Gamma_p\!\left(\frac bL\right)
 \Gamma_p\!\left(\frac{pb\bmod L}{L}\right),
\qquad \varpi^{p-1}=-p.
\tag{G.2}
$$
在 $b=0$ 时两个 Gamma 因子均为一。
所有下述计算都使用同一个 $\varpi$ 和同一条 Gamma 规范。

## 2. 无未知常数的二位 Gamma 提升

定义真正的整数
$$
W_p=\frac{(p-1)!+1}{p},
\qquad H_d=\sum_{i=1}^{d}\frac1i,\quad H_0=0.
$$
对 $0\le d,e\le p-1$ 有
$$
\boxed{\quad
\Gamma_p(-d-pe)
\equiv\frac1{d!}
 \bigl(1+pe(W_p-H_d)\bigr)\pmod{p^2}.
\quad}
\tag{G.3}
$$

证明：由 Gamma 的整数递推，
$$
\Gamma_p(-M)=
\frac{(-1)^{\lfloor M/p\rfloor}}
 {\prod_{1\le i\le M,\ p\nmid i}i}.
$$
取 $M=d+pe$。每个完整块满足
$$
\prod_{i=1}^{p-1}(ap+i)
\equiv(p-1)!\left(1+apH_{p-1}\right)
\equiv-1+pW_p\pmod{p^2};
$$
这里 $H_{p-1}\equiv0\pmod p$，由 $i\leftrightarrow p-i$ 即得。
剩下的末块为
$$
\prod_{i=1}^{d}(pe+i)
\equiv d!\left(1+peH_d\right)\pmod{p^2}.
$$
取逆、消去两个 $(-1)^e$ 后即得 (G.3)。

Gamma 在模 $p^2$ 相同的整数上取同一模 $p^2$ 值：
长度 $p^2$ 的递推块给出全部模 $p^2$ 单位的乘积 $-1$，
与递推的 $(-1)^{p^2}=-1$ 相消。
后者的单位乘积可由互逆配对证明，唯一自逆单位为 $\pm1$。
再用整数稠密性与 Gamma 的连续性，将此结论传到 $\mathbf Z_p$。
所以 $b/L\equiv-d-pe\pmod{p^2}$ 可合法代入 (G.3)，
旋转的一位同样如此。于是
$$
\Gamma_p(b/L)\Gamma_p((pb\bmod L)/L)
\equiv
\frac{
1+p\{(d+e)W_p-eH_d-dH_e\}}
 {d!\,e!}\pmod{p^2}.
\tag{G.4}
$$
本证明没有引进未归一的 $\Gamma_p'/\Gamma_p$ 常数。

## 3. 全部赋值零项及其准确有理提升

先把原已付的两个单位矩形重新解释为有理阶乘数，**不先模 $p$ 简化参数**。
矩形 I、II 为
$$
\begin{array}{c|cc}
 &j_0&j_1\\ \hline
{\rm I}&4k-1+r&2k-1+s\\
{\rm II}&4k-1+r&5k-1+s
\end{array}
\quad
0\le r\le n,\quad0\le s\le N.
\tag{G.5}
$$
II 的末角表示 $j=L$，准确代替原 $j=0$ 一次。
其四个循环下标的数字为
$$
\begin{array}{c|c|c}
 &{\rm I}&{\rm II}\\ \hline
a+j &(r,s)&(r,3k+s)\\
c+j &(3k-1+r,3k-1+s)&(3k+r,s)\\
-j &(n-r,4k-1-s)&(n-r,N-s)\\
h-j &(5k-1-r,N-s)&(5k-2-r,4k-2-s).
\end{array}
\tag{G.6}
$$

在 $\mathbf Z_{(p)}$ 中定义
$$
R_r=\frac{(-1)^r}
 {(r!)^2(3k-1+r)!\,(n-r)!^2(5k-1-r)!},
$$
$$
S_s=\frac{(-1)^s}
 {(s!)^2(3k-1+s)!\,(4k-1-s)!^2(N-s)!}.
\tag{G.7}
$$
四组下标的重数始终为 $(2,1,2,1)$。
I 的阶乘首项就是 $R_rS_s$。
在 II 作 $(r,s)\mapsto(n-r,N-s)$ 后，
四组数字依次成为 I 的第三、第四、第一、第二组。
相同重数也随之保持；符号完全相同。
所以两个矩形的完整首项之和在有理数中已经是
$$
U_0=2\left(\sum_{r=0}^{n}R_r\right)
       \left(\sum_{s=0}^{N}S_s\right).
\tag{G.8}
$$
也可由准确的
$R'_r=-R_{n-r}$、$S'_s=(-1)^N S_{N-s}$
直接核对。R1061 的单位层给 $U_0\equiv1\pmod p$，
因此 $(U_0-1)/p$ 在 $\mathbf Z_{(p)}$ 中有定义。

对 I 的四组数字 $(d_i,e_i)$，置
$$
\mathcal C_{r,s}
=\sum_{i=1}^4\mu_i(e_iH_{d_i}+d_iH_{e_i}),
\qquad(\mu_1,\mu_2,\mu_3,\mu_4)=(2,1,2,1).
\tag{G.9}
$$
具体为
$$
\begin{aligned}
\mathcal C_{r,s}={}&
2(sH_r+rH_s)\\
&+(3k-1+s)H_{3k-1+r}
 +(3k-1+r)H_{3k-1+s}\\
&+2\{(4k-1-s)H_{n-r}+(n-r)H_{4k-1-s}\}\\
&+(N-s)H_{5k-1-r}+(5k-1-r)H_{N-s}.
\end{aligned}
\tag{G.10}
$$
II 的上述反射只置换这四组，所以其 Gamma 修正也完全相同。

每个单位项的加权数字总和是 $4(p-1)$。
由 (G.4)，它的准确首阶修正为
$$
R_rS_s\{1-p(4W_p+\mathcal C_{r,s})\}.
$$
两个矩形合起来遂为
$$
U_0-p\left(
4W_pU_0+
2\sum_{r=0}^n\sum_{s=0}^N R_rS_s\mathcal C_{r,s}\right)
\pmod{p^2}.
\tag{G.11}
$$
原 $j=0$ 的 Gamma 因子也已在末角中付款，没有额外常数项可删。

## 4. 全部赋值一项：三个矩形

为排尽边界，仍令
$x=j/L$、$y=(pj\bmod L)/L$，$j\ne0$。
R1061 的赋值函数完整分段为
$$
f(x)=
\begin{cases}
4&0<x<1/3,\\
2&1/3\le x\le1/2,\\
3&1/2<x<5/6,\\
2&5/6\le x<1,
\end{cases}
$$
$$
f^\vee(y)=
\begin{cases}
4&0<y<1/6,\\
3&1/6\le y\le1/2,\\
4&1/2<y<2/3,\\
2&2/3\le y<1.
\end{cases}
\tag{G.12}
$$
该项的赋值是 $\lambda=f(x)+f^\vee(y)-4$。
因为两个函数均至少为二，$\lambda=1$ 只有
$(f,f^\vee)=(3,2)$ 或 $(2,3)$。

把阈值 $Ac$ 写为低、高两位
$$
Ac=((6-A)k-1)+p(Ak-1)\qquad(1\le A\le5),
$$
逐一保留 (G.12) 的开闭端点，得到互不重叠的三个矩形：
$$
\begin{array}{c|cc|c}
 &j_0&j_1&\text{范围}\\ \hline
{\rm A}&4k-1+r&3k-1+s&0\le r,s\le n\\
{\rm B}&k+r&2k+s&0\le r\le n,\ 0\le s\le N\\
{\rm C}&k-1+r&5k-1+s&0\le r\le n,\ 0\le s\le N.
\end{array}
\tag{G.13}
$$
例如 B 的末角是 $j=h$，C 的首角是 $j=5c$，
都必须保留。它们不是单位矩形的末角。

四组循环数字如下：
$$
\begin{array}{c|c|c|c}
 &{\rm A}&{\rm B}&{\rm C}\\ \hline
a+j&(r,k+s)&(3k+r,s)&(3k-1+r,3k-1+s)\\
c+j&(3k-1+r,4k-1+s)&(r,3k+s)&(r,s)\\
-j&(n-r,3k-1-s)&(5k-2-r,4k-2-s)&(5k-1-r,N-s)\\
h-j&(5k-2-r,6k-2-s)&(n-r,N-s)&(n-r,4k-1-s).
\end{array}
\tag{G.14}
$$
所有数字均在 $0,\ldots,p-1$。
每列的加权总和为 $5(p-1)$，正好给 $\lambda=1$。
其余未列的项赋值至少二，所以对当前模 $p^2$ 读取无贡献。

设 $V_0$ 为三个矩形的**带 $(-1)^j$ 阶乘首项之和**，
尚不包含 Gross–Koblitz 的 $-p$。它有以下完全有理的简化。
A 的首项分离为 $(-1)^k A_r\widehat B_s$，其中
$$
A_r=(5k-1-r)R_r,\qquad
\widehat B_s=
\frac{(-1)^s}
 {(k+s)!^2(4k-1+s)!(3k-1-s)!^2(6k-2-s)!}.
$$
由于 $n$ 为奇数，准确的阶乘反射给
$\widehat B_{n-s}=-\widehat B_s$。
所以 A 的整个贡献为零，甚至不需要模 $p$。

定义
$$
B_r=\frac{(-1)^r}
 {(3k+r)!^2r!(5k-2-r)!^2(n-r)!},\qquad
Y_s=\frac{(-1)^s}
 {s!^2(3k+s)!(4k-2-s)!^2(N-s)!}.
\tag{G.15}
$$
B 的贡献为 $(-1)^k(\sum B_r)(\sum Y_s)$。
C 的相应两因子为
$$
B'_r=\frac{(-1)^r}
 {(3k-1+r)!^2r!(5k-1-r)!^2(n-r)!},
$$
$$
Y'_s=\frac{(-1)^s}
 {(3k-1+s)!^2s!(N-s)!^2(4k-1-s)!}.
$$
直接反射给 $B_{n-r}=-B'_r$、$Y'_s=(-1)^NY_{N-s}$。
因此 C 与 B 的贡献相同，得到
$$
\boxed{\quad
V_0=2(-1)^k
 \left(\sum_{r=0}^{n}B_r\right)
 \left(\sum_{s=0}^{N}Y_s\right).
\quad}
\tag{G.16}
$$
没有把这些两个完整和冒称原 $\eta_k$ 或 $\nu_k$。

## 5. 完整首除层身份

单位项的 $\varpi$ 次幂除以 $p^4$ 后为 $+1$；
赋值一项则为
$\varpi^{5(p-1)}/p^4=-p$。
另一个整体因子
$-1/L=1/(1-p^2)\equiv1\pmod{p^2}$。
所以 (G.1)、(G.11)、(G.16) 准确给
$$
1-p\equiv U_0-p\left(
4W_pU_0+
2\sum_{r=0}^n\sum_{s=0}^N R_rS_s\mathcal C_{r,s}
+V_0\right)\pmod{p^2}.
\tag{G.17}
$$
利用 $U_0\equiv1\pmod p$，其首除层为
$$
\boxed{\quad
\frac{U_0-1}{p}\equiv
2\sum_{r=0}^n\sum_{s=0}^N R_rS_s\mathcal C_{r,s}
+4W_p
+2(-1)^k\left(\sum_{r=0}^nB_r\right)
              \left(\sum_{s=0}^NY_s\right)
-1\pmod p.
\quad}
\tag{G.18}
$$
每一项的分母都是显式的模 $p$ 单位。
其中 $(U_0-1)/p$ 必须由 (G.7)–(G.8) 的**原有理数提升**读取，
不能把 R1061 的模 $p$ Dixon 产品随意提升后再除以 $p$。

尤其，准确的有理参数是
$$
\frac{S_s}{S_0}
=\frac{(1-4k)_s^2(1-k)_s}{(s!)^2(3k)_s},
$$
只在模 $p$ 后才能把 $1-4k$ 改成 $2k$。
直接对那个简化后的 Dixon 产品作参数微分，
会漏掉本篇明确保留的第一位修正。

(G.18) 是同一个原有限域函数的完整一阶 $p$-adic 信息。
它还没有证明无权半和 $D_N(1)$ 非零，也没有把任何 harmonic 参数
导数识别成 [R1076](./R1076-original-primitive-cubic-and-sixth-power-obstructions.md)
的实际短谱导数 $\nu_k$。
后继需要在这些完整项上证明真正的来源比较，不能略去 $V_0$、
第二位的 $H_{d_i}$ 或原有理提升中的除 $p$ 边界。

## 来源

- R1061 §15，尤其 (1061.38)–(1061.42)：同一个原 McCarthy 函数、
  退化 Dixon 值、完整循环数字及 Gross–Koblitz 规范。
- D. McCarthy, *Transformations of well-poised hypergeometric functions
  over finite fields*, Theorem 4.2 及 (4.5)–(4.7)；
  [作者原文](https://dermotmccarthymath.github.io/publications/Hyp%20Trans.pdf)。
- A. M. Robert, *The Gross–Koblitz formula revisited*,
  Rend. Sem. Mat. Univ. Padova 105 (2001), Theorem 4；
  [原文](https://www.numdam.org/article/RSMUP_2001__105__157_0.pdf)。

新增二位 Gamma 提升、三个赋值一矩形、完整反射及 (G.18)
由本篇逐式证明。原 $\eta_k,\nu_k$ 非同时零与课题主目标继续开放。
