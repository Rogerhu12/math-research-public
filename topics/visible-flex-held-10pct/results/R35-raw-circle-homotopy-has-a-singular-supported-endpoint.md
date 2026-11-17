# R35. raw 圆化同伦在支撑端点才失去完整控制空间

维护：Astra-held10-7322d0de-20261118。严格分析命题；它解释一个控制坐标的限制，不证明任何非线性边值解存在、唯一或不存在。有限运行和几何诊断另记。

## 1. 精确的函数空间与投影

令周期为 $T=2\pi/3$，在偶、$T$ 周期实函数上使用归一化 $L^2$ 内积。设

$$
L=\operatorname{span}\{1,\cos(3\phi)\},\qquad X=L^\perp.
$$

固定与实际 raw 定义相同的偶 $C^4$ 截止函数 $W$，满足 $0\le W\le1$；在保护开弧 $I$ 上 $W=0$，而在补集的一个开区间上 $W>0$。反射和周期轨道中的保护弧一并理解。令 $\Pi_W f\in L$ 为加权最小二乘投影：

$$
\langle W(f-\Pi_W f),\ell\rangle=0\quad(\ell\in L).
$$

两个低函数在 $W>0$ 的开区间上线性独立，因此其加权 Gram 正定。该投影对任意 $L^2$ 输入均有唯一意义。定义

$$
Bf=W(f-\Pi_W f),\qquad
T_\lambda=(1-\lambda)I+\lambda B\quad(0\le\lambda\le1).
$$

在 $e_j=\cos(3j\phi)$、$j\ge2$ 上，这恰是已发布 raw 控制列的数学定义。它没有逆高矩 Schur 块。

## 2. 所有 lambda<1 的无限控制空间相同

首先 $Bf\perp L$，故 $B:X\to X$。对 $f,g\in X$，加权投影的正交性给

$$
\langle g,Bf\rangle
=\langle W(g-\Pi_W g),f-\Pi_W f\rangle.
$$

右侧关于 $f,g$ 对称，且

$$
0\le\langle f,Bf\rangle
=\min_{\ell\in L}\langle W(f-\ell)^2\rangle
\le\langle Wf^2\rangle\le\|f\|_2^2.
$$

所以 $B$ 是 $X$ 上的有界自伴算子，并且 $0\le B\le I$。于是当 $\lambda<1$ 时

$$
(1-\lambda)\|f\|_2^2
\le\langle f,T_\lambda f\rangle\le\|f\|_2^2.
$$

严格正下界和自伴性保证 $T_\lambda:X\to X$ 双射。具体地，值域闭且其正交补为零；因此它不是仅有单射而未知满射的结论。

取任意支撑于 $I$ 的非零光滑对称函数，并在无限维的这种函数空间中施加两个低矩为零的线性条件，仍有无限维非零子空间。其元素 $f\in X$ 满足 $Wf=0$，从而 $\Pi_Wf=0$、$Bf=0$。因此

$$
\boxed{\|T_\lambda^{-1}\|_{X\to X}=\frac1{1-\lambda}}\qquad(0\le\lambda<1).
$$

特别地，$\lambda=1$ 的 $B$ 有无限维核，其像在保护弧上几乎处处为零（连续输入时逐点为零），不能仍视作对整个 $X$ 的可逆换坐标。

这个结论也适用于 $X\cap C^k$，$0\le k\le4$，但上面的精确逆范数公式只声明于 $L^2$ 范数。若 $r\in X\cap C^k$、$T_\lambda f=r$ 的 $L^2$ 解为 $f$，则

$$
f=\frac{r+\lambda W\Pi_W f}{1-\lambda+\lambda W}.
$$

分母严格正，投影项是两个光滑低函数的有限组合，所以 $f\in C^k$。因此 $T_\lambda$ 对该光滑子空间也双射；不能从 $L^2$ 范数公式直接申领一个同样的 $C^k$ 上界。

## 3. 这不等于整个物理问题不变

上述等价只涉及无限维的高控制函数。若某个期望核心 $h_*$ 与给定背景 $h_{\rm base}(q,\lambda)$ 的低矩匹配，即两者之差属于 $X$，则每个 $\lambda<1$ 都可通过唯一 $f=T_\lambda^{-1}(h_*-h_{\rm base})$ 表示它。**仅仅增大 lambda，不能证明实际核心在保护弧上趋于圆形。** 系数或函数范数可能随 $1/(1-\lambda)$ 增大并抵消圆化。

但是背景的低矩也可能随 $(q,\lambda)$ 改变；还存在完整 Frenet 方程、物理 profile、非线性尾和边界条件。本文没有把这些变化忽略，也没有证明某个 fixed-g BVP 分支就是同一核心的重参数化。

对有限 $X_M=\operatorname{span}\{e_2,\ldots,e_M\}$，$T_\lambda X_M$ 随 lambda 变化，不能由无限维双射推断有限空间相同或有限离散结果相同。有限投影与全度量误差仍须实际检验。R20 已登记的有限谐波圆弧限制也没有因此失效。

## 4. 必须跟踪的实际圆弧缺陷

在三重对称、eta=0 的当前背景中，保护弧上基准曲率半径密度为

$$
\rho_{\rm base}
=(1-\lambda)[1-8q\cos(3\phi)]+\lambda R,
\qquad R=1+8q.
$$

由于 $W$ 及其一、二阶导数在保护弧上均为零，令实际 raw 输入控制为 $f$，则整个核心严格满足

$$
\boxed{\rho-R
=(1-\lambda)\{-8q[1+\cos(3\phi)]+f+f''\}}
\quad\text{on }I.
$$

若 $q$ 和 $\|f+f''\|_{L^\infty(I)}$ 在接近端点的过程中一致有界，则实际圆弧缺陷确实趋零。没有这种控制时，lambda 数值本身不能代替该检查。

写 $\phi=\pi/3+z$、$|z|\le a$，且 $f=\sum_{j=2}^M c_j\cos(3j\phi)$，可直接用真实求解参数得到

$$
\rho-R=(1-\lambda)\left[
8q(\cos(3z)-1)+\sum_{j=2}^M(1-9j^2)c_j(-1)^j\cos(3jz)
\right].
$$

中心 $z=0$ 的缺陷是精确线性组合；它给真实最大缺陷的一个下界。由 $1-\cos x\le x^2/2$ 又有可直接认证的保守上界

$$
\|\rho-R\|_{L^\infty(I)}
\le(1-\lambda)\left[36|q|a^2+\sum_{j=2}^M|1-9j^2|\,|c_j|\right].
$$

该上界不依赖角网格。以后每个实际圆化态应同时记录这些中心/全弧界、采样缺陷和输入控制范数；只有 lambda=1 加上完整原门、全闭几何与同 g 精化，才可能支付本题的实际圆弧条件。

本结果不排除端点上的实际解，也不要求把控制人为截断为旧七矩。后者已经由 R33/R34 单独处理。
