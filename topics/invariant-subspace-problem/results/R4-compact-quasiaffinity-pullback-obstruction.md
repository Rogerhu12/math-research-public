# R4. 紧拟仿射可以把所有非零向量送成循环向量，且所有真不变子空间的拉回都为零

日期：2026-11-12。状态：**已证明的显式路线障碍；不解决完整 Hilbert 不变子空间问题，不宣称文献新颖性。**

本条给出一个完全自含的矩变换例子。它说明：把一个算子经单射、稠密像、甚至非常紧的交织映射送入熟悉的后移模型，并不足以从该后移的不变子空间拉回原算子的不变子空间。证明不依赖 Beurling 不变子空间分类。

相关经典来源：Bernard Virot, *Modèles d'opérateurs linéaires et translations unilatérales simples*, Bull. Soc. Math. France **100** (1972), 157–175，§4 Proposition 3（核型拟仿射模型）。原文：<https://numdam.org/item/10.24033/bsmf.1734.pdf>。下面只证明具体模型及其拉回障碍，没有把经典模型的存在作为新结果。

## 1. 算子与结论

令
$$
H=L^2([0,1],dt),\qquad K=\ell^2(\mathbb N_0),
$$
内积对第一变量线性。定义
$$
(Tf)(t)=\frac t2 f(t),\qquad
B(a_0,a_1,a_2,\ldots)=(a_1,a_2,\ldots),
$$
以及矩变换
$$
(Xf)_n=\int_0^1 f(t)\left(\frac t2\right)^n\,dt,
\qquad n\ge0.
$$

**定理。** 上述算子满足：

1. $X:H\to K$ 有界、Hilbert–Schmidt，且
   $$\|X\|_{\mathrm{HS}}^2=\log3.$$
2. $X$ 单射、像稠密，但像不闭；即 $X$ 是一个紧拟仿射（compact quasiaffinity）。
3. $BX=XT$。
4. 对每个 $f\ne0$，$Xf$ 都是 $B$ 的循环向量：
   $$\overline{\operatorname{span}\{B^nXf:n\ge0\}}=K.$$
5. 对每个真闭 $B$-不变子空间 $N\subsetneq K$，
   $$X^{-1}(N)=\{0\},\qquad X(H)\cap N=\{0\}.$$
6. $T$ 本身有许多非零真闭不变子空间。具体地，若 $0<|E|<1$，则
   $$M_E=L^2(E)\subset H$$
   是这样的子空间；但 $X(M_E)$ 是 $K$ 中稠密、非闭、$B$-不变的真线性子空间。
7. 若有界算子 $Y:K\to H$ 满足反向交织 $TY=YB$，则 $Y=0$。

因此，在这个例子中，拉回后移的任何真闭不变子空间得到零；把原算子的任何非零不变子空间送过去后取闭包，则得到整个 $K$。

## 2. 有界性和精确的 Hilbert–Schmidt 范数

令 $h_n(t)=(t/2)^n$。这是 $H$ 中的向量，且
$$
\|h_n\|_2^2=\int_0^1(t/2)^{2n}\,dt
=\frac1{4^n(2n+1)}.
$$
因此 $\sum_n|\langle f,h_n\rangle|^2\le\|f\|^2\sum_n\|h_n\|^2<\infty$，先保证 $X$ 定义良好且有界。
对 $K$ 的标准正交基 $e_n$，由定义和内积约定有
$$
X^*e_n=h_n.
$$
因而
$$
\begin{aligned}
\|X\|_{\mathrm{HS}}^2
 &=\sum_{n=0}^{\infty}\frac1{4^n(2n+1)}\\
 &=\int_0^1\frac{dt}{1-t^2/4}
=2\operatorname{arctanh}(1/2)
=\log3.
\end{aligned}
$$
其中交换求和和积分由非负项单调收敛保证。也可以先定义前 $N$ 个坐标的有限秩算子，再由上述平方和收敛得到同一个 $X$。

更具体地，若 $P_N$ 是到 $e_0,\ldots,e_{N-1}$ 的正交投影，则
$$
\begin{aligned}
\|X-P_NX\|^2
&\le\|X-P_NX\|_{\mathrm{HS}}^2\\
&=\sum_{n\ge N}\frac1{4^n(2n+1)}
\le\frac{4}{3}\,\frac{4^{-N}}{2N+1}.
\end{aligned}
$$
所以 $X$ 甚至有指数快的有限秩逼近。下述失败并不是紧性不够强。

## 3. 单射、稠密像，以及复共轭约定

若 $Xf=0$，则 $\int_0^1 f(t)t^n\,dt=0$ 对所有 $n\ge0$ 成立。实单项式的复线性包是 $\mathbb C[t]$，在 $L^2[0,1]$ 中稠密，故 $f=0$。这证明单射性。

对 $y=(y_n)\in K$ 定义解析函数
$$
F_y(z)=\sum_{n=0}^{\infty}y_nz^n,\qquad |z|<1.
$$
Cauchy–Schwarz 不等式给出，在任意 $|z|\le r<1$ 上，
$$
\sum_{n\ge0}|y_nz^n|\le\frac{\|y\|_2}{\sqrt{1-r^2}}.
$$
因此级数在紧子圆盘上一致绝对收敛，而且
$$
(X^*y)(t)=F_y(t/2).
$$
事实上，
$$
\begin{aligned}
\langle Xf,y\rangle_K
&=\sum_{n\ge0}\left(\int_0^1 f(t)(t/2)^n\,dt\right)\overline{y_n}\\
&=\int_0^1 f(t)\overline{F_y(t/2)}\,dt
=\langle f,X^*y\rangle_H.
\end{aligned}
$$
交换积分和级数由上述一致绝对收敛和 $f\in L^1[0,1]$ 保证。

若 $X^*y=0$，则 $F_y(t/2)=0$ a.e.。连续性先给出 $F_y=0$ 在整个实区间 $[0,1/2]$ 上成立，再由解析函数恒等定理得 $F_y\equiv0$，即 $y=0$。所以
$$
\overline{X(H)}=(\ker X^*)^\perp=K.
$$

$X(H)$ 不闭。否则稠密性使 $X$ 满射，结合单射和开映射定理，$X^{-1}$ 有界。于是 $I_H=X^{-1}X$ 紧，这与无限维 Hilbert 空间单位球不相对紧矛盾。

## 4. 交织关系

对任意 $n\ge0$，
$$
(BXf)_n=(Xf)_{n+1}
=\int_0^1f(t)(t/2)^{n+1}\,dt
=(XTf)_n.
$$
因此 $BX=XT$，继而 $B^nX=XT^n$。

## 5. 每个非零像向量都循环：直接证明

固定 $f\ne0$。设 $y\in K$ 与所有 $B^nXf$ 正交。由交织和伴随公式，
$$
\begin{aligned}
0
&=\langle B^nXf,y\rangle_K\\
&=\langle XT^nf,y\rangle_K\\
&=\int_0^1 (t/2)^n f(t)\overline{F_y(t/2)}\,dt
\qquad(n\ge0).
\end{aligned}
$$
函数 $F_y(t/2)$ 在 $[0,1]$ 上有界，所以
$$
h(t)=f(t)\overline{F_y(t/2)}\in L^2[0,1].
$$
上式表明 $h$ 与每个实单项式正交。由多项式稠密性，$h=0$ a.e.。

若 $y\ne0$，则 $F_y$ 不是零解析函数。它在紧区间 $[0,1/2]$ 上的零点只有有限个：若有无限多个，紧性给出位于单位圆盘内部的聚点，违反恒等定理。因此 $F_y(t/2)\ne0$ a.e.，由 $h=0$ 推出 $f=0$，矛盾。

故正交补中的 $y$ 只能为零。这证明
$$
\overline{\operatorname{span}\{B^nXf:n\ge0\}}=K.
$$

## 6. 真闭不变子空间的拉回为零，非零不变子空间之像稠密

设 $N\subsetneq K$ 闭且 $BN\subset N$。若有 $f\ne0$ 且 $Xf\in N$，则 $N$ 包含 $Xf$ 的全部轨道及其闭线性包。第 5 节给出该闭包为 $K$，与 $N$ 真矛盾。因此 $X^{-1}(N)=\{0\}$。由 $X$ 单射，也有 $X(H)\cap N=\{0\}$。

对任意 $E$ 满足 $0<|E|<1$，$M_E$ 显然非零、真、闭，并在乘法算子 $T$ 下不变。交织关系给出
$$
B\,X(M_E)=XT(M_E)\subset X(M_E).
$$
取任意 $0\ne f\in M_E$，其像的 $B$-循环闭包为 $K$，且包含在 $\overline{X(M_E)}$ 中，故 $\overline{X(M_E)}=K$。另一方面，$X(M_E)\subset X(H)\ne K$，因此它是稠密真子空间，必不闭。∎

## 7. 反向交织完全不存在

乘法算子 $T=M_{t/2}$ 没有特征值：$Tf=\lambda f$ 迫使 $f$ 支持在至多单点的集合 $\{t:t/2=\lambda\}$ 上，所以 $f=0$。

对每个 $|\lambda|<1$，后移 $B$ 有特征向量
$$
k_\lambda=(1,\lambda,\lambda^2,\ldots),\qquad Bk_\lambda=\lambda k_\lambda.
$$
这些向量的线性包稠密于 $K$：若 $y$ 与全部 $k_\lambda$ 正交，则解析幂级数 $\sum_n\overline{y_n}\lambda^n$ 恒为零，故 $y=0$。

若 $TY=YB$，则
$$
T(Yk_\lambda)=\lambda Yk_\lambda.
$$
由 $T$ 没有特征值，$Yk_\lambda=0$。稠密性和 $Y$ 有界给出 $Y=0$。这证明定理第 7 条。

## 8. 对普适模型路线的限制

此例中的 $T$ 和 $B$ 都有非平凡闭不变子空间。所证内容是**不变子空间运输的失败**，不是对 ISP 的反例。

它具体排除以下充分条件：仅由 $BX=XT$，再加 $X$ 单射、稠密像、紧、Hilbert–Schmidt、有限秩逼近极快，就认为存在某个真闭 $B$-不变子空间 $N$ 满足 $X^{-1}(N)\ne0$。这些条件在本例中全部成立，而所有这样的拉回都为零。

Rota 的普适模型要求的是到一个**闭**不变子空间的有界同构。在本例中，$X$ 的逆只定义在非闭像上且不有界；不能用拟仿射替换该同构。一般的双向拟相似运输定理还包含另一方向的交织映射，而第 7 节证明本例中连非零有界反向交织都不存在。

完整问题仍要求找到能保证非零真闭子空间的附加机制。这个例子表明，若继续使用单向紧交织，必须额外证明所选模型子空间确实与 $X(H)$ 非零相交，不能把这一步当作稠密性的推论。

该现象对标准标量观察模型的一般形式，见 [R6](R6-observation-model-no-pullback.md)：当 $T$ 无特征值且 $T^*$ 有循环向量时，所有非零观察像都对标量后移循环，因此所有真闭模型子空间的拉回一律为零。
