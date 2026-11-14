# R28 补记：从框架残差到真实主曲率上界

日期：2026-11-14。本文只给可连续验证的曲率传递式，不证明非线性连接器存在，也不把曲率半径当作完整闭面的 reach 下界。沿用 R28 的准确单位正交目标框架与重构，不修改其冻结脚本。

## 1. 假设和归一化

在紧材料带 `I × S1` 上，令 `a>0`，单位向量场 `V,T` 满足 `V·T=0`，并具有 R28 所需的周期、镜面对称和 C2 正则性。记

\[
R=V_\theta-\partial_s(aT),\quad
\delta=-\Pi R,\quad N=V\times T,
\]

其中 `Pi` 是零平均的周期原函数。准确重构满足

\[
X_s=V+\delta,\quad X_\theta=aT,
\]
\[
X_{ss}=V_s-\Pi R_s,\quad
X_{s\theta}=V_\theta-R,\quad
X_{\theta\theta}=aT_\theta.
\tag{1}
\]

假设已获得整个连续区域的上界

\[
\|R\|_\infty\le\varepsilon,\quad
\|R_s\|_\infty\le\varepsilon_s,\quad
e={\pi\over2}\varepsilon<1.
\tag{2}
\]

它们必须是连续上界，不能仅取有限网格最大值。由 R28 的 Green 核范数，

\[
|\delta|\le e,\qquad |\Pi R_s|\le{\pi\over2}\varepsilon_s.
\tag{3}
\]

`R_s` 仍具有零角平均，因为 `R` 在每个 `s` 上零平均且允许微分交换。因此第二个原函数及 (3) 正当。

以准确参考 `ds²+a²dtheta²` 的单位坐标归一化一阶导数，得到三行两列矩阵

\[
\mathcal A=[V+\delta,T]=[V,T]+[\delta,0].
\]

前一矩阵的两列准确正交单位，后一矩阵的算子范数为 `|delta|`。因此对所有 `h in R²`，

\[
|\mathcal A h|\ge(1-e)|h|,
\qquad \widehat g=\mathcal A^T\mathcal A\succeq(1-e)^2I.
\tag{4}
\]

特别地，`e<1` 已保证浸入和正定的实际第一基本形式。

## 2. 实际单位法向的准确表达

在目标正交架 `(V,T,N)` 中写

\[
\delta=xV+yT+zN.
\]

由于 `a>0`，取实际有向单位法向

\[
n={X_s\times X_\theta\over|X_s\times X_\theta|}
  ={(1+x)N-zV\over d},\qquad
d=\sqrt{(1+x)^2+z^2}.
\tag{5}
\]

这里 `1+x≥1-e>0`。从而

\[
n\cdot T=0,\quad |n\cdot N|\le1,\quad
|n\cdot V|={|z|\over d}\le e.
\tag{6}
\]

最后一个较紧上界来自 `x²+z²≤e²`：

\[
e^2(1+x)^2-(1-e^2)z^2
\ge e^2(1+x)^2-(1-e^2)(e^2-x^2)
=(x+e^2)^2\ge0.
\]

于是 `z²≤e²[(1+x)²+z²]`。这也说明直接估计得到的较松上界 `e/(1-e)` 可以在此处替换为 `e`。

式 (5) 明确处理了实际法向与目标 `N` 的差。以下估计没有直接把 `n` 换成 `N`。

## 3. 第二基本形式的三个上界

定义归一化实际第二基本形式

\[
\widehat b=
\begin{pmatrix}
n\cdot X_{ss}&n\cdot X_{s\theta}/a\\
n\cdot X_{s\theta}/a&n\cdot X_{\theta\theta}/a^2
\end{pmatrix}.
\tag{7}
\]

逐点令

\[
A=|N\cdot V_s|+{\pi\over2}\varepsilon_s,
\]
\[
B={|N\cdot V_\theta|+\varepsilon\over a},
\]
\[
C={|N\cdot T_\theta|
       +|V\cdot T_\theta|\,e\over a}.
\tag{8}
\]

则

\[
|\widehat b_{11}|\le A,\qquad
|\widehat b_{12}|\le B,\qquad
|\widehat b_{22}|\le C.
\tag{9}
\]

证明逐项如下。

因为 `|V|=1`，有 `V·Vs=0`，故 `Vs` 仅含 `T,N` 分量。由 `n·T=0` 和 (6)，

\[
|n\cdot V_s|=|(n\cdot N)(N\cdot V_s)|\le|N\cdot V_s|.
\]

此外 `n` 是实际单位法向，(3) 直接给

\[
|n\cdot\Pi R_s|\le|\Pi R_s|\le\pi\varepsilon_s/2.
\]

结合 (1) 即得第一项。这说明 `A` 没有漏掉法向误差：`Vs` 的 `V` 分量准确为零，而误差向量 `Pi Rs` 用其完整欧氏范数控制。

同理由 `V·Vtheta=0`，有

\[
|n\cdot V_\theta|\le|N\cdot V_\theta|,\qquad
|n\cdot R|\le\varepsilon,
\]

从而得到第二项。

最后 `T·Ttheta=0`，因此

\[
n\cdot T_\theta=(n\cdot N)(N\cdot T_\theta)
+(n\cdot V)(V\cdot T_\theta).
\]

由 (6) 及 `Xthetatheta=a Ttheta` 得第三项。正是这一项必须保留目标联络分量 `V·Ttheta` 与法向差的乘积；单用 `|N·Ttheta|/a` 一般不正确。

## 4. 真实 shape operator 的上界

对任意二维实向量 `h`，(9) 给

\[
|h^T\widehat b h|
\le A h_1^2+2B|h_1h_2|+C h_2^2
\le\Lambda |h|^2,
\]

其中

\[
\Lambda={A+C+\sqrt{(A-C)^2+4B^2}\over2}
\tag{10}
\]

是非负对称矩阵 `[[A,B],[B,C]]` 的最大特征值。因此 `||bhat||op≤Lambda`。

实际主曲率是对称矩阵

\[
\widehat g^{-1/2}\widehat b\widehat g^{-1/2}
\]

的特征值，而不是未经归一化的 `Xss,Xst,Xtt` 的特征值。结合 (4)，准确得到

\[
\boxed{
\max\{|\kappa_1|,|\kappa_2|\}
\le {A+C+\sqrt{(A-C)^2+4B^2}\over2(1-e)^2}.}
\tag{11}
\]

可逐 cell 使用同一全区 `epsilon,epsilon_s` 和该 cell 上 `A,B,C` 的连续上界。也可先取全域上界 `A*,B*,C*` 再代入；非负矩阵的最大特征值对每个非负元素单调，因此这种替换保持安全。

若只需要较简单的形式，也有

\[
\max|\kappa_i|\le{\sqrt{A^2+2B^2+C^2}\over(1-e)^2},
\]

但 (11) 通常更紧。

## 5. 适用边界

该证明只要求准确单位正交框架、真实周期重构、`a>0`，以及 (2) 和一阶框架量的连续上界。不要求数值残差已经恒零。它直接控制实际重构面的 shape operator，而不是参考度量的形式曲率 `-a''/a`。

`Rs` 涉及框架的二阶场导数。若端口通过 `a ΠT` 做位置 C2 硬拼，仍应使用已经独立推导的真实材料二 jet；新增 `cosine_core_high_jets.py` 给出该输入，不会使未认证的微分误差自动变成连续上界。

曲率上界可作为完整闭面法弦／近对角覆盖证明的一个输入。它没有排除非局部自交、近接或不同边界组件的冲突；`1/K` 不能单独宣称为完整 reach 下界。当前也没有在任何真实连接器上应用本式取得题目要求的完整几何证书。
