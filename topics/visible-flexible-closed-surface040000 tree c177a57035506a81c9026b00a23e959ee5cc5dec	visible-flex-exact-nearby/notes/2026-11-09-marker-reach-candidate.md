# 固定小标记、非全等性与全相位 reach：定量条件工具

会话：Astra-visible-flex-4ffd372b，2026-11-09。完整条件证明候选，尚待独立审查。本题精确闭合 band 尚未构造，本文不能据以宣称完成。

## 1. 一个直接的 reach 扰动估计

这里采用闭 $C^2$ 嵌入子流形 $S\subset\mathbb R^n$ 的弦—切平面公式
$$\operatorname{reach}(S)=\inf_{p\ne q\in S}
\frac{|q-p|^2}{2\operatorname{dist}(q-p,T_pS)},\tag{1}$$
分母为零时该比值取 $+\infty$。这是 Federer 的标准 reach 表征；本节只需该公式的下界方向。

**命题。** 设 $\operatorname{reach}(S)\ge\rho>0$，$f:\mathbb R^n\to\mathbb R^n$ 是 $C^{1,1}$ 微分同胚，且
$$|f(q)-f(p)|\ge m|q-p|,\quad \|Df\|\le M,\quad
\|Df(q)-Df(p)\|\le L|q-p|.$$
若 $f(S)$ 是 $C^2$，则
$$\operatorname{reach}(f(S))\ge\frac{m^2\rho}{M+L\rho}.\tag{2}$$

证明：令 $v=q-p$，把它正交分解为 $v=v_T+v_N$，$v_T\in T_pS$。由直线积分余项，
$$|f(q)-f(p)-Df(p)v|\le\tfrac12 L|v|^2.$$
因为 $Df(p)v_T\in T_{f(p)}f(S)$，并由 (1) 有 $|v_N|\le|v|^2/(2\rho)$，所以
$$\operatorname{dist}(f(q)-f(p),T_{f(p)}f(S))
\le\left(\frac M{2\rho}+\frac L2\right)|v|^2.$$
再由全局下 Lipschitz 界 $|f(q)-f(p)|\ge m|v|$，对每对点应用 (1) 得 (2)。注意仅有每点最小奇异值界并不足以替代这里的全局下 Lipschitz 假设。

特别地，若 $f=\mathrm{id}+u$，$u\in C^2$，$\|Du\|_\infty\le\eta<1$、$\|D^2u\|_\infty\le L$，则
$$\operatorname{reach}(f(S))\ge
\frac{(1-\eta)^2\rho}{1+\eta+L\rho}.\tag{3}$$
因为差分积分给上下 Lipschitz 常数 $1\pm\eta$；$f$ 全局单射且导数可逆，且 $|f(x)|\to\infty$（由对原点的下界），故像既开又闭，从而是整个 $\mathbb R^n$。如果只在一个有界邻域定义 $u$，应先作保留上述明确界的全空间延拓，不能省略。

## 2. 全相位几何只需一次基准验证

设未标记的已闭合像集为
$$S_t^0=R_tB\cup C,$$
$R_t$ 是绕共同轴的旋转，固定帽集 $C$ 对全部这些旋转不变。则
$$S_t^0=R_t(B\cup C),\qquad
\operatorname{reach}(S_t^0)=\operatorname{reach}(S_0^0).\tag{4}$$

若真正固定的标记只改变帽，且可以写为 $S_t=f_t(S_t^0)$，所有 $f_t=\mathrm{id}+u_t$ 具有同一 $\eta,L$ 界，则由 (3) 同时得到所有 $t$ 的 reach 下界。对帽内支撑的固定竖直图标记，可以取一个全空间位移 $u$：其支撑与所有旋转 band 不相交，在帽上给所需高度，远离帽用 $z$ 截断。此时甚至可取 $f_t=f$。支撑与 band 的分离、截断的 $Du,D^2u$ 界必须在具体几何里支付。

因此只要未标记闭族已有严格 reach 余量，就能让固定标记的 $C^2$ 范数足够小，把全部相位仍保持在 $.03D$ 之上。若用 $D\le D^0+2\varepsilon$，应明确满足
$$\frac{(1-\eta)^2\rho}{1+\eta+L\rho}
\ge.03(D^0+2\varepsilon).\tag{5}$$
不能从 $\kappa\le1/\rho$ 单独推出这里要求的基准 reach。

## 3. 四个可识别的固定点排除全部刚体全等

本节是一个可实施的条件模板。假设未标记紧 $C^2$ 嵌入曲面有平面帽，帽内部有空间放置四个互不相交的小圆盘。假设其“不是 $C^3$ 的点集”没有孤立点；例如该坏集为空，或为若干完整接缝圆。该假设必须检查实际构造，不能从 $C^2$ 自动推出。

选互异 $0<\beta_1<\beta_2<\beta_3<\beta_4<1$。在四个圆盘中心 $c_j$ 加固定高度图
$$h_j(x)=A_j\phi_{\beta_j}(|x-c_j|/b),\qquad
\phi_\beta(s)=\begin{cases}(1-s^2)^4(1+s^{2+\beta}),&0\le s<1,\\0,&s\ge1.\end{cases}\tag{6}$$
其在支撑边界有至少三阶连续消失，在中心恰为 $C^{2,\beta_j}$，且不属于任意 $C^{2,\alpha}$、$\alpha>\beta_j$。后一个断言由中心展开
$$\phi_\beta(|x|)=1-4|x|^2+|x|^{2+\beta}+O(|x|^4)$$
及沿径向的二阶导数差 $c|x|^\beta+O(|x|^2)$ 得出，系数 $c=(2+\beta)(1+\beta)$ 非零。图在中心切平面水平；这也是曲面本身而不只是所选坐标的正则性，因为局部正交投影到该平面是正则图坐标，若曲面有更高 Hölder 图正则性，该正交图也必须有。

因此加标记后非 $C^3$ 点集的孤立点恰为这四个中心，其各自二阶 Hölder 阈值互异。欧氏刚体运动保持这些局部性质，故任意曲面全等必须逐个固定这四个点。让前三个平面中心不共线，并取 $A_1=A_2=A_3=\varepsilon$、$A_4=2\varepsilon$，则四个空间标记点仿射独立：前三点处于帽平面上方高度 $\varepsilon$，第四个高度 $2\varepsilon$。每个 $\varepsilon>0$ 都成立，无需宏观标记高度。

任何 $A\in E(3)$ 若逐个固定四个仿射独立点，写作 $A(x)=Qx+b$，三条独立点差均被 $Q$ 固定，故 $Q=I,b=0$；反射也被排除。如果某相位已经有 $S_t\ne S_0$ 的严格几何见证，则不存在 $A\in E(3)$ 使 $AS_t=S_0$。

这个模板依赖**所有**标记点对材料参数 $t$ 固定。只知道四个点在每时刻各自存在而不知道其位置固定，不足以推出以上结论。

## 4. 非全等推出商 Hausdorff 距离严格正

对于非空紧集 $K,L\subset\mathbb R^3$，若不存在刚体运动 $A$ 使 $AK=L$，则
$$\inf_{A\in E(3)}d_H(AK,L)>0.\tag{7}$$
反证：取 $A_j(x)=Q_jx+b_j$ 使距离趋零。固定 $x_0\in K$，则 $|Q_jx_0+b_j|$ 有界，因此 $b_j$ 有界。$O(3)$ 紧，故取子列 $Q_j\to Q,b_j\to b$。$K$ 紧给 $A_jK\to AK$ 的 Hausdorff 收敛，故 $AK=L$，矛盾。这也说明这里的 inf 实际能达到。

所以第3节的严格非全等与中央柱的严格像变化共同给 $\delta_E>0$，即便标记振幅任意小。并没有给 $\delta_E\ge.05D$；已有R1对此类窄标记正有上界。

## 5. 本题用途与仍缺的输入

此工具将“宏观握持变化”“非全等”“全相位 reach”分成可验证的三个命题，而没有把它们混为同一个振幅。剩下必须实际提供：同一精确度量的完整闭 band、$C^2$ 拼缝和开圆领圈、基准全局 reach、具体标记支撑分离与导数界、全部非 $C^3$ 孤立点检查。不存在这些输入时，本文只算中间进展。

参考：Herbert Federer, *Curvature Measures*, Transactions of the American Mathematical Society 93 (1959), 418–491，Theorem 4.18；本文(2)是其reach稳定性估计的直接型式，不声称新定理。已实际核对 Charles Fefferman, Sergei Ivanov, Yaroslav Kurylev, Matti Lassas, Hariharan Narayanan, *Fitting a putative manifold to noisy data*, Proceedings of Machine Learning Research 75 (2018), Proposition 3, p.4 的公式重述，https://proceedings.mlr.press/v75/fefferman18a/fefferman18a.pdf 。原AMS全文链接返回403，因此没有声称直接全文读过Federer原文。
