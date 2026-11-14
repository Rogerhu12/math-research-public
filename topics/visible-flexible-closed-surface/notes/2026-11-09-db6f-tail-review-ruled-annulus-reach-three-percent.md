# 鞍环 reach 超过初态直径 3% 的完整独立审查

**结论：接受本稿所列全部证明，环带全族的 reach≥b/5，因此相对初态整个环带直径 D 有 reach/D>2/65>0.03。附属冻结 JavaScript 源已实际独立执行，25 项精确有理门通过。此结论仍不构成闭曲面或可见幅度完成。**

审查人：tail-review-continued-2，未参与本增强证明的推导。  
日期：2026-11-09。  
本稿与先前恢复版 v2 的独审分别封存；不覆写原审稿，也不将本次检查倒计为旧版程序重跑。

## 1. 固定来源与实际执行身份

### 1.1 增强正文

[2026-11-09-db6f-root-ruled-annulus-reach-three-percent.md](https://github.com/Rogerhu12/math-research/blob/907b834ff56c005ae63cb9757ec6b379d4523b57/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-root-ruled-annulus-reach-three-percent.md)

| 项目 | 固定值 |
| --- | --- |
| 作者 | root |
| commit | 907b834ff56c005ae63cb9757ec6b379d4523b57 |
| Git blob | 1185f00e0909752adcfea61aa4de03c68ef0f461 |
| UTF-8 字节数 | 10,122 |
| 本次审读 | 全部 8 节，含所有常数和近远点分支 |

基础族来自 [recovered-v2](https://github.com/Rogerhu12/math-research/blob/456c246b252e102e5a3d29c45b9d4dde7146dcea/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-geometry-explicit-ruled-saddle-annulus-recovered-v2.md)，commit 456c246b252e102e5a3d29c45b9d4dde7146dcea、blob 725771192a0ca6a7b2bf09e0302005e011c4be68。其完整独立纸面审稿已另存于 [v2 review](https://github.com/Rogerhu12/math-research/blob/11756ce532b0ec60074a1e3567c28b90f03fed02/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-ruled-saddle-annulus-recovered-v2.md)，blob 8c4531a5f083e4d2220c56ac47f4850d05c0a544。基础审稿只证明旧下界 169b/17690；新 b/5 结论由本次独立审查支付。

### 1.2 附属源与独立真实执行

[db6f-geometry-ruled-annulus-reach-rationals.js](https://github.com/Rogerhu12/math-research/blob/78e902ebe01074aa486494e2bcdf2fb05f584dfa/topics/visible-flexible-closed-surface/scripts/db6f-geometry-ruled-annulus-reach-rationals.js)

| 项目 | 固定值 |
| --- | --- |
| commit | 78e902ebe01074aa486494e2bcdf2fb05f584dfa |
| Git blob | d0eae43daf679db23f1018927f4591469e4bbc9b |
| UTF-8 字节数 | 3,540 |
| 独立运行身份 | tail-review-ruled-annulus-reach-rationals-01 |
| 实际运行环境 | functions.exec 的全新 JavaScript 隔离运行时 |
| 开始 UTC | 2026-11-09 22:36:00 UTC |
| 返回 UTC | 2026-11-09 22:36:00 UTC |
| 实际结果 | PASS_EXACT_RATIONAL_GATES_ONLY，25 项 |
| solver 调用 | 0 |

审查人先从上述固定 commit 取得并完整阅读源码，再以 new Function 执行同一完整字符串，并调用 ruledAnnulusReachRationalCertificate。工具调用实际完成返回，没有把预期输出、作者回执或仅加载函数算作独立运行。检查器内部使用 BigInt 约分有理数；比较通过整数交叉相乘完成，没有浮点近似或几何采样。

实际返回的范围标记为：

    status: PASS_EXACT_RATIONAL_GATES_ONLY
    checks: 25
    reach_over_b: 1/5
    diameter_over_b_upper: 13/2
    reach_over_initial_diameter_strict_lower: 2/65
    proves_geodesic_existence: false
    proves_full_annulus_theorem: false
    numerical_solver_calls: 0

这是可用 JavaScript 隔离运行时的真实执行，不是失联终端中的 Node/Python 执行。脚本只核有限常数关系；下文的存在性、曲线弦估计、测地线留带和边界 reach 必须由完整数学证明支付。作者旧环境的符号程序仍未由本次执行恢复或重跑。

## 2. 命题和缩时间区间的合法性

基础族具有固定半宽 w=b/20、共同材料域

\[
M=[-w,w]\times(\mathbb R/\ell\mathbb Z)
\]

及共同度量

\[
g=dv^2+(b^2+v^2)\,du^2.
\]

它在原角 θ 中满足 cτ′=b dτ×dτ′，|dτ|=1，kτ=|dτ′|>0，且关于 (τ,θ) 光滑。以下需要的严格不等式在 τ=0 都有统一余量；角域紧，条件数目有限，因此存在同一个正的 ε 使它们对全部 |τ|<ε 同时成立。

缩小 ε 不改变初态 F0、共同度量、半宽、材料 C3 或固定片。基础非平凡性本来就对所有充分小的非零时间成立，故缩小区间不会把族变成恒定族。

本稿只接受这个正区间存在性。它没有产生一个有效可计算的 ε，更没有给出规定的可见幅度。

## 3. 曲率与二阶导数的统一界

可以沿用基础证明的

\[
\|c_\tau'-c_0'\|_\infty\le b/40,\qquad
\|c_\tau''\|_\infty<7b,\qquad
\|d_\tau''\|_\infty\le20.
\]

又因基础速度 2√2≤k0<3，有严格余量选择

\[
14/5\le k_\tau\le31/10.
\]

### 3.1 球面测地曲率界

基础曲率为

\[
\kappa_0=d_{0,z}\Phi(X),\qquad
\Phi(X)=\frac{17+3\eta+X}{(8+X)^{3/2}},
\qquad X=\sigma^2\sin^23\theta.
\]

在 0≤X≤σ² 上，分子为正，且

\[
\Phi'(X)=
\frac{8-\frac32(17+3\eta)-X/2}{(8+X)^{5/2}}<0.
\]

于是

\[
|\kappa_0|\le\sigma\Phi(0)
<\frac{33/2}{16(113/80)}
=\frac{165}{226}<\frac34.
\]

这里分别用了 η<−1/6、σ<1 和 √2>113/80；所有替换方向正确。球面测地曲率由正则 C² 方向数据连续决定，因此 |κτ|≤3/4 可在同一缩小区间内取得。

### 3.2 形算子范数

令 a=√(b²+v²)。基础第二基本形式在正交单位标架下给

\[
S=\begin{pmatrix}
0&-b/a^2\\
-b/a^2&\kappa_\tau/a
\end{pmatrix}.
\]

这是实际形算子，不是未经度量归一的第二基本形式矩阵。对该对称二阶矩阵，

\[
\|S\|=
\frac{|\kappa_\tau|/a+
\sqrt{(\kappa_\tau/a)^2+4b^2/a^4}}2
\le\frac{3+\sqrt{73}}{8b}
<\frac3{2b}.
\]

后一严格不等式等价于 √73<9。故可取全局统一 Λ=3/(2b)，包含边界点及全部时间。

## 4. 水平 Fourier 弦估计及中心线 reach

基础水平式为

\[
ic_{0,W}=Re^{i\theta}+Pe^{7i\theta}+Qe^{-5i\theta}.
\]

对最短角距 δ∈[0,π]，几何级数给

\[
|\sin(n\delta/2)|\le |n|\sin(\delta/2).
\]

三角不等式应用于水平弦，得

\[
|c_0(\theta)-c_0(\phi)|
\ge2(R-7P-5Q)\sin(\delta/2).
\]

这不需要对竖直项作减法。利用基础恒等式，

\[
R-7P-5Q
=\frac{b\sigma(\eta+5)}2
>\frac{9457}{4000}b.
\]

变形差 cτ−c0 沿最短角弧的差值至多 bδ/40；注意这里控制的是差值，无须知道其整体平移。用 δ≤π sin(δ/2) 及 π<22/7，

\[
|c_\tau(\theta)-c_\tau(\phi)|
>
\left(\frac{9457}{2000}-\frac{22}{280}\right)
b\sin(\delta/2)
>\frac{23}{5}b\sin(\delta/2)
\ge\frac{161}{110}b\delta
\]

对 δ>0 成立。它同时排除全圈自交。

单位 ν⊥cτ′(θ) 时，二阶 Taylor 给

\[
2|\nu\cdot(q-p)|\le7b\delta^2.
\]

由上述弦长换元，

\[
2|\nu\cdot(q-p)|
\le\frac{7}{(161/110)^2b}|q-p|^2
\le\frac{|q-p|^2}{3b/10},
\]

其中 (161/110)²/7>3/10 已独立精确检查。因此取 ρc=3b/10。

任意空间点到中心线的最近点存在，最近点差向量垂直中心线切向。对 r<ρc，距离平方与任意另一中心线点之差满足

\[
|z-q|^2-|z-p|^2
\ge(1-r/\rho_c)|q-p|^2>0.
\]

这证明 reach(cτ)≥ρc，不是只从曲率半径猜测 reach。由于 w=b/20<ρc，原正宽嵌入也继续成立。

## 5. 近点的角距与长度比较

### 5.1 近空间点必有小角距

写 x=p+v dτ(θ)、y=q+v̂ dτ(φ)，h=|x−y|。两端分别应用法向弦不等式，得到

\[
(x-y)\cdot(p-q)
\ge(1-w/\rho_c)|p-q|^2
=\frac56|p-q|^2.
\]

两个法向贡献各含 1/(2ρc)，合起来才是 w/ρc；正文未漏掉这项系数。于是 |p−q|≤6h/5。

若 h<2b/5，结合水平弦下界，

\[
\sin(\delta/2)<12/115.
\]

而

\[
\sin(21/200)\ge21/200-(21/200)^3/6>12/115.
\]

最短角距满足 δ/2∈[0,π/2]，该区间上 sin 严格递增，故 δ<21/100。此结论来自全局弦估计，适用于任何近空间点对。

### 5.2 空间弦与冻结切向项

取实现 δ 的有符号最短角 lift 差 Δθ，令 Δv=v̂−v。精确拆分为

\[
y-x=Z+\mathcal R,\qquad
Z=\Delta v\,d_\tau(\theta)
+(c_\tau'(\theta)+\widehat v\,d_\tau'(\theta))\Delta\theta.
\]

d 与 c′、d′ 正交，c′ 与 d′ 也正交，所以

\[
|Z|^2=(\Delta v)^2+
(b^2+\widehat v^2)k_\tau(\theta)^2\delta^2
\ge(\Delta v)^2+(14b\delta/5)^2.
\]

展开使用的是固定的终点系数 v̂，余项因此只涉及 θ 的二阶导数：

\[
|\mathcal R|
\le\frac12(7b+w\cdot20)\delta^2=4b\delta^2.
\]

若 δ>0 且 h<2b/5，

\[
|\mathcal R|/|Z|
\le(10/7)\delta<3/10.
\]

δ=0 时余项为零，单独成立。因此全近点分支均有 |Z|≤10h/7。

### 5.3 比较路径长度

将 v 和原角 lift 同时线性插值，路径仍在 |v|≤w 内。由共同度量在原角中的形式和 kτ≤31/10，其速率不超过

\[
\sqrt{(\Delta v)^2+(25b\delta/8)^2},
\]

因为 √(401/400)<801/800 且 (31/10)(801/800)<25/8。积分的参数区间长度为 1，故该式也是路径长度上界。

又 125/112=(25/8)/(14/5)>1，比较两个二次型得

\[
d_g(P,Q)\le\frac{125}{112}|Z|
\le\frac{625}{392}h=:Ch.
\]

此处只得到内在距离上界。要以第二基本形式控制空间加速度，还必须证明可选择真正的内在最短测地线留在带内；下一节完成该必要步骤。

## 6. 完整圆柱与最短测地线留带

把同一度量延伸到

\[
\widehat M=\mathbb R\times(\mathbb R/\ell\mathbb Z).
\]

因为 g≥dv²+b²du²，每个 g-Cauchy 列先在完整平坦圆柱中收敛；其 v 坐标最终落在一个有限区间，该区间内两度量一致等价，所以也按 g 收敛。因此该完整圆柱确实完备，Hopf–Rinow 给出任意端点间的最短测地线。

按单位弧长参数 s，测地线方程与循环坐标守恒量为

\[
v''=v(u')^2,\qquad
J=(b^2+v^2)u'=\text{常数}.
\]

这些等式可直接由 Christoffel 符号或能量 Euler–Lagrange 方程得到，符号为正 v(u′)²，正文正确。

- 若 J=0，则 u′=0、v″=0，径向线段留在两端 v 坐标之间。
- 若 J≠0，则 u′ 处处非零。若路径越过上界 w>0，因为端点不超过 w，必在内部取得一个正最大值；在那里 v″≤0，却由方程有 v″>0，矛盾。越过 −w 时同理在负内部最小值处矛盾。

因此完整圆柱的最短测地线全程留在 |v|≤w。它的长度既是完整圆柱距离，也是带内距离：完整圆柱可选路径更多，距离不大于带内；而该最短路径本身可在带内使用，反向不等式也成立。于是其长度 L 确实受上一节 L≤Ch 控制。

这项证明处理了带边域的核心问题。不能仅说带内有一条短比较路径，就把它当成内在测地线；正文没有作该跳跃。

## 7. 整个带边闭集的最近点唯一性

取任意空间点 z，选最近环带点 p=Fτ(P)，r=|z−p|<b/5。紧性保证这样的点存在。对任意另一像点 q=Fτ(Q)≠p，记 h=|q−p|。

### 7.1 远点分支

若 h≥2b/5，则 h>2r，直接得到

\[
|z-q|^2-r^2
\ge h^2-2rh>0.
\]

该分支覆盖远角、全局回绕和所有不满足近点条件的情形，不需要局部参数图。

### 7.2 近点分支及边界单侧条件

若 h<2b/5，取已证留带的单位速最短测地线 γ，长度 L≤Ch。由于 p 是整个带边闭集上的最近点，沿这条可行路径的距离平方在起点右导数非负，所以

\[
(z-p)\cdot(F_\tau\circ\gamma)'(0)\le0.
\]

P 位于边界时仍然成立；没有假设 z−p 只沿曲面通常法向。

γ 为单位速内在测地线，其空间加速度等于 II(γ′,γ′)N，范数不超过 Λ。即使端点在边界，显式公式 F=c+vd 在材料坐标上光滑延伸，端点的单侧极限也受同一个界控制。积分二阶余项给

\[
(z-p)\cdot(q-p)\le\frac12r\Lambda L^2
\le\frac12r\Lambda C^2h^2.
\]

因此

\[
|z-q|^2-r^2
\ge(1-r\Lambda C^2)h^2>0,
\]

因为

\[
r\Lambda C^2<
\frac3{10}\left(\frac{625}{392}\right)^2
=\frac{1171875}{1536640}<1.
\]

近远分支覆盖所有 q≠p。故任何距像小于 b/5 的点都有唯一最近点，证明

\[
\operatorname{reach}(F_\tau(M))\ge b/5
\]

对整个缩小后的时间区间成立。

## 8. 直径归一与接受范围

已审基础图的整个初态直径满足 D<13b/2，因此

\[
\frac{\operatorname{reach}(F_\tau(M))}{D}
>\frac{b/5}{13b/2}
=\frac2{65}>\frac3{100}.
\]

严格大于来自初态直径的严格上界；没有将 D 换成半径、宽度或中心线长度。本结论是相对固定初态 D 的全时间统一界。

本次完整纸审与实际有理门重放都通过，未发现阻断本定理的错误。可将该增强结果登记为已独审中间结论；同一环带模块的 0.03D reach 数值阈值因此已有证明。

仍需严格区分：

1. 环带的两条边界仍在，尚未构造无边闭曲面或完成两侧接合；
2. 参数区间只有正存在性，没有有效有限幅度，也未付 0.05D 可见像位移；
3. 基础族原符号程序与 recovered-v2 的哈希绑定及实际独立重跑，仍未由这个常数检查器补齐；
4. 主数值候选、G5、存储 C 整链和 README 的最终完成标准均未因本稿自动通过。

此次没有运行 BVP、tail、RK、producer、网格或连续几何后台，没有改动 HANDOFF、LOG、results 或任何既有源码与审稿。环境失联期间只通过已授权方式保存小文本，所有执行范围均以上述实际返回为准。
