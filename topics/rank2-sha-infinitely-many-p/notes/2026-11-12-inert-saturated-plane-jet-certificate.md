# 实际 Euler 图像的一个饱和平面 jet 证书

日期：2026-11-12。状态：下面的局部判据与 $p=103,D=6$ 的精确证书
均已证明；没有据此证明目标中央 Stokes 常数非零。

本文计算的是 R62 的**整个固定图像**，而不是中央投影。
中央常数的消失不改变这个图像的整体半径。目的仅在于落实一个此前
未检查的环节：在 $D$ 与接触阶平方根同阶时，首个非中央坏系数能否
被真实的饱和前缀格吸收。这个实例的答案是否定的。

## 1. 固定图像及第一个坏系数

在 $E_0:y^2=x^3-x$ 上使用已经认证的实际截面

$$
A_1(z)=\sum_m\beta_mz^m
 =\theta(z)^{17}\left(V+\frac35V^2-\frac15V^3+\frac15V^4\right),
\qquad V=x(z)^{-2},\qquad A_1=z^4+O(z^8).
$$

令

$$
\mathscr H(z)=\int_0^z A_1(t)\,dt/t,\qquad
f_0(z)=\theta((4-i)z),\qquad
w=z^4,\qquad Y(w)=\frac{4\mathscr H(z)}{f_0(z)}.
\tag{1.1}
$$

这些对象与素数无关，$Y\in\mathbb Q(i)[[w]]$，且

$$
Y(w)=w+\left(-\frac{1513}{120}+20i\right)w^2+\cdots.
\tag{1.2}
$$

固定惰性 $p\ge7$，置 $d=p+1$、$a=17c$，其中 $v_p(c)=-1$，
$\rho=p^{-1/(2p)}$。R54、R62 给出

$$
A_1=e^{az^d}G,\qquad f_0=e^{az^d}G_0,\qquad
\|G\|_\rho\le\rho^4,\quad\|G_0\|_\rho=\|G_0^{-1}\|_\rho=1.
\tag{1.3}
$$

在 $K_p=\mathbb Q_p(i)$ 中取 $v_p(p)=1$，令 $\mathcal O$ 为整数环。
由于 $p$ 惰性，$K_p/\mathbb Q_p$ 未分歧二次，所有系数赋值是整数。
(1.3) 因而保证 $G,G_0,G_0^{-1}$ 在次数 $\le d+4<2p$ 的系数均整。
又因为 $G$ 起于 $z^4$，在这个范围内 $e^{az^d}$ 对 $A_1$ 的首个
非整贡献恰为 $az^{d+4}$。积分分母是四的倍数且小于 $2p$，不被 $p$
整除。设

$$
N=\frac{p+5}{4}.
$$

于是 $[w^n]Y\in\mathcal O$ 对 $n<N$ 成立，而

$$
\begin{aligned}
p[w^N]Y
&\equiv pa\left(\frac4{d+4}-1\right)
 =-pa\frac d{d+4}\\
&\equiv-\frac{17pc}{5}\pmod p.
\end{aligned}
\tag{1.4}
$$

右边为单位。这是永久存在的 $j=4$ 非中央 Stokes 块的首坏项；
论证没有使用 $J_{A,p}'(0)$ 的非零性。

## 2. 饱和前缀与梯度的通用判据

下面的引理不要求 $Y$ 来自 theta 函数。设

$$
Y(0)=0,\quad [w^n]Y\in\mathcal O\ (n<N),\quad
[w^N]Y\in p^{-1}\mathcal O,\quad
\kappa:=p[w^N]Y\bmod p\ne0.
$$

取 $L_D=\mathcal O[w,y]_{\le D}$，以总次数不超过 $D$ 的单项式为整基，
并采用这个基的系数最大范数。记

$$
B_{<N}:L_D\longrightarrow\mathcal O^N,\qquad
P\longmapsto\bigl([w^n]P(w,Y(w))\bigr)_{0\le n<N}.
$$

假设 $B_{<N}\bmod p$ 的行秩为 $N$。于是 $B_{<N}$ 满射，
$\Lambda_N=\ker B_{<N}$ 是 $L_D$ 的饱和直和子格，而且

$$
\Lambda_N/p\Lambda_N=\ker(B_{<N}\bmod p).
\tag{2.1}
$$

新一行 $\lambda_N(P)=[w^N]P(w,Y(w))$ 满足准确的剩余公式

$$
\boxed{\quad
p\lambda_N(P)\equiv\kappa P_y(0,0)\pmod p
\quad(P\in L_D).
\quad}
\tag{2.2}
$$

**证明。** 写 $Y=Y_{<N}+y_Nw^N+O(w^{N+1})$。在次数 $N$，
Taylor 展开的新项只有 $y_Nw^N P_y(0,Y(0))$；所有其他项是整的。
因为 $Y(0)=0$，得到 (2.2)。行秩条件给单位子式，从而可用整基变换
把前缀化成 $(I_N\ 0)$，证明 (2.1)。$\square$

因此新行在**真实饱和核**上的范数恰为 $p$，当且仅当

$$
\exists\bar P\in\ker(B_{<N}\bmod p):
\quad\bar P_y(0,0)\ne0.
\tag{2.3}
$$

若 (2.3) 失败，新行在 $\Lambda_N$ 上是整的。这里没有把某个
未饱和的高接触多项式直接当作规范化的 jet。

特别地，当 $\operatorname{rank}L_D=N+1$ 且 (2.3) 成立时，
把末行乘 $p$ 得到的方阵

$$
\widetilde B=
\begin{pmatrix}B_{<N}\\p\lambda_N\end{pmatrix}
\in\operatorname{GL}_{N+1}(\mathcal O).
\tag{2.4}
$$

原矩阵就是 $\operatorname{diag}(1,\ldots,1,p^{-1})\widetilde B$。
故其 $p$ 进 Smith 指数准确为 $(-1,0,\ldots,0)$。前缀的最大子式
最小赋值为 $0$，完整方阵行列式赋值为 $-1$，相应新 jet 的对数范数
准确为 $\log p$。

## 3. 实际 $p=103,D=6$ 的完整核证书

此时 $N=27$，$\dim L_6=28$，次数与接触阶的平方根同阶。
采用单项式顺序

$$
(1;\ w,y;\ w^2,wy,y^2;\ \ldots;\ w^6,w^5y,\ldots,y^6).
\tag{3.1}
$$

全部计算在 $\mathbb F_{103^2}=\mathbb F_{103}[i]$ 中进行，$i^2=-1$。
输入来自 R57 的整数流，先准确除以阶乘取得**普通 Taylor 系数**；
没有把 Hurwitz 格直接当作本节的普通系数格。

精确结果为

$$
103[w^{27}]Y\equiv29,\qquad
\det B_{0\ldots26,\,0\ldots26}=1+34i\ne0.
\tag{3.2}
$$

故前缀满行秩，其核只有一维。把最后一列 $y^6$ 的系数规范为 $1$，
约化核向量为下列分次数排列的系数；每对整数 $(a,b)$ 表示 $a+bi$：

| 总次数 | 按 (3.1) 顺序的核系数 |
|---|---|
| 0 | $(0,0)$ |
| 1 | $(58,43),(45,60)$ |
| 2 | $(74,9),(65,48),(19,57)$ |
| 3 | $(86,75),(21,13),(53,48),(74,92)$ |
| 4 | $(11,92),(6,18),(44,92),(20,13),(51,20)$ |
| 5 | $(26,0),(5,9),(79,24),(32,63),(83,82),(20,36)$ |
| 6 | $(35,36),(19,24),(71,47),(84,87),(42,72),(35,48),(1,0)$ |

尤其

$$
\bar P_y(0,0)=45+60i\ne0,\qquad
103\lambda_{27}(P)\equiv29(45+60i)=69+92i\ne0.
\tag{3.3}
$$

这里的 $P$ 是由单位前缀子式唯一提升、并保持 $y^6$ 系数为 $1$ 的
真正整核向量，不是只满足模 $103$ 消失的替代物。

完整矩阵末行乘 $103$ 后的行列式是

$$
\det\widetilde B=31+69i\ne0\quad\text{于 }\mathbb F_{103^2}.
\tag{3.4}
$$

所以原普通系数矩阵的 Smith 指数是一个 $-1$ 与二十七个 $0$，
而第 $27$ 阶新 jet 在饱和核上的范数准确等于 $103$。

## 4. 复算与范围

运行

```bash
python topics/rank2-sha-infinitely-many-p/scripts/check-inert-saturated-plane-jet.py
```

脚本先用固定整数 ODE 重建 $A_1$ 与 $\theta$ 到 $z^{108}$，再用
$(4-i)^4=161-240i$ 重建 $f_0$，并以 $\mathbb Q(i)$ 的精确有理运算
求 $Y$。它逐项断言所有前缀系数整，随后在剩余域作高斯消元，输出
全部核系数、单位前缀子式、末行梯度及完整 Smith 指数。

这个例子落实了一个真实的 $D\asymp\sqrt N$ 饱和高接触格，说明
全局整数流中的一个分母确实可以在普通 jet 的饱和之后仍存在。
它没有给出无穷素数的前缀秩与梯度定理；(2.3) 是今后可复用的准确
检验条件。尤其坏项来自 $\mathcal S_4\equiv1$，即使假设中央
$\mathcal S_0=0$，本例的机制也不改变，不能据此完成主课题。

相关完整证明见
[全余类 Stokes 分解](2026-11-12-inert-euler-primitive-stokes-decomposition.md)、
[精确滤子与有限 Newton 投影](2026-11-12-stokes-filters-in-integer-flow-field.md)、
[全局分母和 Hurwitz 饱和](2026-11-12-first-filter-denominator-and-hurwitz-saturation.md)。
