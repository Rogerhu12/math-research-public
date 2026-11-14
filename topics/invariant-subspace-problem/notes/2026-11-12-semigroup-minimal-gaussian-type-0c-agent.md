# R80 的补充：二阶最小型整轨道与 Gaussian 衰减障碍

日期：2026-11-12（UTC）。子任务：literature。**状态：已证明的补充引理，暂不占结果号。**

沿用 R80 的实际 R20 半群
$$
S(t)=\operatorname*{s-lim}_{N\to\infty}
\prod_{j<N}e^{-tu_j}e^{2tu_jN_j},
\qquad u_j\ge0,\quad u\in\ell^2.
$$
其常向量轨道的整延拓记作 $\mathfrak s(z)$。本条将 R80 的二阶有限型界加强为二阶最小型，并把“不能超二阶衰减”加强为“不能有任何固定正系数的 Gaussian 衰减”。

## 1. 整轨道为二阶最小型

R80 的精确分解为
$$
\mathfrak s(z)=R(z)\mathfrak v(z),\qquad
\mathfrak v(z)=\bigotimes_{j\ge0}
e^{-zu_j}(1,1+2zu_j).
$$
该笔记 (2.16) 已给
$$
\log\|R(z)\|
\le C\left(1+r\sqrt{\log(2+r)}
+[\log(2+r)]^{7/3}\right)=o(r^2),
\qquad r=|z|\to\infty. \tag{1.1}
$$

给任意 $\varepsilon>0$，取固定 $J$ 使
$$
\sum_{j\ge J}u_j^2<\varepsilon.
$$
R80 的逐因子估计给
$$
\log\left\|\bigotimes_{j\ge J}
e^{-zu_j}(1,1+2zu_j)\right\|
\le\varepsilon r^2.
$$
有限头部则满足
$$
\begin{aligned}
\log\left\|\bigotimes_{j<J}
e^{-zu_j}(1,1+2zu_j)\right\|
&\le\sum_{j<J}
\left[ru_j+\log(1+2ru_j)\right]\\
&=O_J(r+\log(2+r))=o(r^2).
\end{aligned}
$$
所以 $\limsup_{r\to\infty}r^{-2}\log\|\mathfrak v(z)\|\le\varepsilon$，其中上界一致于 $|z|=r$。让 $\varepsilon\downarrow0$，再结合 (1.1)，得到
$$
\boxed{
\forall\varepsilon>0\ \exists C_\varepsilon<\infty:
\quad
\|\mathfrak s(z)\|\le C_\varepsilon e^{\varepsilon|z|^2}
\quad(z\in\mathbb C).
} \tag{1.2}
$$
这不宣称整函数的精确阶一定为二；“二阶最小型”在这里指 (1.2) 的上界，包括实际阶低于二的情形。

## 2. 标量最小型不能沿正实轴 Gaussian 衰减

**引理。** 若整函数 $f$ 对所有 $\varepsilon>0$ 满足
$$
|f(z)|\le C_\varepsilon e^{\varepsilon|z|^2},
$$
并且存在 $c,C>0$ 使
$$
|f(t)|\le Ce^{-ct^2}\qquad(t\ge0),
$$
则 $f\equiv0$。

**证明。** 若非零，取 $y>0$ 使 $f(iy)\ne0$，并使用 R80 已自含推导的上半圆盘调和测度：
$$
k_R(x)=\frac y\pi
\left[\frac1{x^2+y^2}
-\frac{R^2}{R^4+y^2x^2}\right],
\qquad
\omega_R(\text{圆弧})\le\frac{4y}{\pi R}.
$$
固定 $\varepsilon>0$，记 $L_\varepsilon=\log C_\varepsilon$，则在圆弧上
$\log|f|\le L_\varepsilon+\varepsilon R^2$，故圆弧贡献至多
$$
\frac{4y}{\pi R}L_\varepsilon+\frac{4y\varepsilon}{\pi}R.
$$
负半直径的贡献至多
$$
\frac y\pi\int_{-R}^0
\frac{L_\varepsilon+\varepsilon x^2}{x^2+y^2}\,dx
\le O_\varepsilon(1)+\frac{y\varepsilon}{\pi}R.
$$
这里如果 $L_\varepsilon<0$，用其正部作上界即可。

取固定 $T$ 使 $\log|f(x)|\le-(c/2)x^2$ 对 $x\ge T$ 成立。对 $T\le x\le R/2$，
$$
k_R(x)\ge\frac{y}{2\pi(x^2+y^2)}.
$$
于是该区间的贡献至多
$$
-\frac{cy}{4\pi}
\int_T^{R/2}\frac{x^2}{x^2+y^2}\,dx
=-\frac{cy}{8\pi}R+O_{c,y,T}(1).
$$
正半直径其余的大 $x$ 部分非正，小区间贡献有固定上界。次调和均值因而给
$$
\log|f(iy)|
\le
\left(\frac{5y\varepsilon}{\pi}
-\frac{cy}{8\pi}\right)R
+O_\varepsilon(1)+o(1).
$$
取 $0<\varepsilon<c/40$，右边趋于 $-\infty$，矛盾。边界零点如 R80 一样先截断 $\max(\log|f|,-M)$ 再作单调极限。证毕。

## 3. 实际半群的逐向量 Gaussian 障碍

**定理。** 若存在 $c,C>0$ 使
$$
\|S(t)x\|\le Ce^{-ct^2}\qquad(t\ge0),
$$
则 $x=0$。

证明完全沿 R80：对每个一变量多项式 $P$，
$$
f_P(z)=B(x,P(A)\mathfrak s(z))
$$
满足 (1.2)，而
$$
f_P(t)=B(S(t)x,P(A)1)
$$
具有 Gaussian 衰减。第 2 节给 $f_P\equiv0$；在零处评价并用 $1$ 对 $A$ 循环及 $B$ 非退化，即得 $x=0$。

因此，如果某个与 $S(1)$ 及其可逆因子交换的算子 $K$ 满足
$$
\|K^n\|\le C_0^n e^{-c_0n^2},
$$
则任何把 $Y^dx$ 化为 $KQx$、并可交换迭代的关系，同样可由此排除非零 $x$。该句是一个工具的适用条件，不宣称当前任意 $K$ 都满足此幂估计。

