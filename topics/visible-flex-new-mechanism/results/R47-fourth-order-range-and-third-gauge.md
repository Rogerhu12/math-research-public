# R47：四阶完整 range 与第三阶 gauge 的准确作用

日期：2026-11-14。literature 推导，repo_sources 独立逐项手核，root 全文复核。**独立完整证明；未声称四阶条件已通过。**

使用 [倒行四块](R45-reversal-four-block-third-period-cancellation.md) 和
[八 packet 完整三阶圆](R46-eight-packet-complete-third-order-circle.md) 的实际周期浸入带与 f、g。固定该构造选定的二阶解 $Z_d$，允许第三阶解的全部周期、同 collar 齐次自由度。

本稿给这一明确范围内的四阶必要充分条件，并把第三阶 gauge 的可调范围准确算完。它没有排除改变二阶解、几何或 profile 后的其他分支。

## 1. 四阶 forcing 恰好三个通道

简记 $c=\cos\theta$、$s=\sin\theta$，取已经成立的

$$Y_\theta=cY_f+sY_g,\quad Z_\theta=s^2Z_d,
\quad W_\theta=s^2(cW_f+sW_g).$$

目标始终是同一个 $g_\varepsilon=g_X+\varepsilon^2(dY_f)^2$。四阶未知场 $V_\theta$ 必须解

$$\mathcal L_XV_\theta
=-\{(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)\}.$$

定义

$$A=-\mathcal S(Y_f,W_f),$$

$$B=-\mathcal S(Y_f,W_g)-\mathcal S(Y_g,W_f),$$

$$C=-\{(dZ_d)^2+\mathcal S(Y_g,W_g)\}.\tag{1}$$

则完整右侧严格为

$$\boxed{H_{4,\theta}=s^2c^2A+s^3cB+s^4C.}\tag{2}$$

对给定 $W_f,W_g$，全圆四阶可解当且仅当 A、B、C 三个通道都通过完整线性 range。充分性由线性叠加给出；必要性可分别用 $\theta=\pi/2,\pi/4,3\pi/4$ 提取 C、A、B。这里没有遗漏 $(dZ_d)^2$，也没有把它放进错误的 $s^2c^2$ 项。

## 2. 第三阶 gauge 不改变三个四阶周期函数

周期、同 collar 的齐次解恰为 $Y_\psi$。因此可把

$$W_f\mapsto W_f+Y_{\psi_f},\qquad
W_g\mapsto W_g+Y_{\psi_g}.$$

由 (1)，三个 forcing 的改变量是

$$\delta A=-\mathcal S(Y_f,Y_{\psi_f}),$$

$$\delta B=-\mathcal S(Y_f,Y_{\psi_g})
-\mathcal S(Y_g,Y_{\psi_f}),$$

$$\delta C=-\mathcal S(Y_g,Y_{\psi_g}).\tag{3}$$

全零二阶算子的极化恒等式已给

$$\mathscr P\{\mathcal S(Y_\phi,Y_\psi)\}\equiv0$$

对任意紧支撑 profile 成立，且该周期泛函可在尚未支付另一 collar 条件时按同一侧锚定定义。因此

$$\boxed{\mathscr P(A),\ \mathscr P(B),\ \mathscr P(C)
\text{ 全部不受第三阶 gauge 改变。}}\tag{4}$$

这一结论也覆盖任意相位依赖的第三阶 gauge $Y_{\chi_\theta}$，不必预设其具有上述两个通道的三角形式。

在倒行对称规范下，$Y_f,Y_g,W_f,W_g$ 均是反射奇场、$Z_d$ 是偶场，所以 (1) 是反射偶 forcing。故上一阶奇数周期相消不能自动支付 (4)。

## 3. ruling 的可调范围只涉及三个准确交叉矩

对一般 forcing H 定义

$$\mathscr K(H)(s)=\int H_{uu}(s,u)\,du.$$

记几何三列函数

$$\mathbf w(s)=\left(\frac{d(s)^2+1}{4h(s)},\frac{d(s)}2,\frac{h(s)}4\right),
\qquad d=h\omega-k.$$

对两个 profile 定义

$$\mathbf m(\phi,\psi)=\left(
\int\phi''\psi'',\quad
\int\xi\phi''\psi'',\quad
\int\xi^2\phi''\psi''+2\int\phi'\psi'\right).$$

完整 ruling 能量的极化给

$$\int(Y_\phi)_u\cdot(Y_\psi)_u\,du
=\mathbf w(s)\cdot\mathbf m(\phi,\psi).$$

因此 (3) 对三个 ruling 函数的改变量为

$$\delta\mathscr K(A)=-2\mathbf w\cdot\mathbf m(f,\psi_f),$$

$$\delta\mathscr K(B)=-2\mathbf w\cdot
\{\mathbf m(f,\psi_g)+\mathbf m(g,\psi_f)\},$$

$$\delta\mathscr K(C)=-2\mathbf w\cdot\mathbf m(g,\psi_g).\tag{5}$$

系数必须与 s 无关；不能每条 ruling 单独选择新的 profile gauge。

## 4. 交叉矩映射的真实满秩与显式右逆

**引理。** 对任意非零 $\phi\in C_c^\infty(I)$，线性映射
$\psi\mapsto\mathbf m(\phi,\psi)$ 从 $C_c^\infty(I)$ 到 $\mathbb R^3$ 满射，而且可把 psi 的支撑限制在 phi 的支撑中。

分部积分后，三个线性泛函的密度为

$$L_0\phi=\phi'''',\qquad
L_1\phi=\xi\phi''''+2\phi''',$$

$$L_2\phi=\xi^2\phi''''+4\xi\phi'''.\tag{6}$$

若它们有非平凡线性关系，存在非零二次以下多项式 P 使

$$P\phi''''+2P'\phi'''=0.$$

在 $P\ne0$ 的每个连通分支上，

$$\frac d{d\xi}\{P^2\phi'''\}=0.$$

分支端点若是 P 的零点，因 $\phi'''$ 有界，常数必须为零；若该分支延伸到无穷远，则 phi 的紧支撑也迫该常数为零。因此 $\phi'''$ 在 $P\ne0$ 上全零，连续性使其处处为零。紧支撑的二次多项式只能为零，与假设矛盾。故 (6) 线性无关。

于是 Gram 矩阵

$$G^\phi_{ij}=\int(L_i\phi)(L_j\phi)$$

严格正定。对任意给定 $v\in\mathbb R^3$，准确取

$$\psi=\sum_{j=0}^2[(G^\phi)^{-1}v]_jL_j\phi\tag{7}$$

就有 $\mathbf m(\phi,\psi)=v$，且其支撑不超出 phi。

当前 f、g 的支撑互不相交，所以可分别用 (7) 支付 f、g 的任意三个交叉矩，彼此没有交叉影响。因此

$$\psi\longmapsto
\bigl(\mathbf m(f,\psi),\mathbf m(g,\psi)\bigr)$$

是一个准确满射到 $\mathbb R^6$ 的映射，而不只是某个离散矩阵看起来满秩。

## 5. 允许全部第三阶 gauge 后的完整四阶判据

固定 $Z_d$ 与任意一组第三阶解 $W_f,W_g$，形成 (1)。令

$$\mathcal W=\{s\mapsto\mathbf w(s)\cdot v:\ v\in\mathbb R^3\}.$$

**定理。** 在这一固定二阶解的范围内，允许任意周期、同 collar、相位依赖的第三阶 gauge 后，全部 theta 的四阶方程有解，当且仅当

$$\boxed{\mathscr P(A)=\mathscr P(B)=\mathscr P(C)\equiv0,}\tag{8}
$$

并且

$$\boxed{\mathscr K(A),\mathscr K(B),\mathscr K(C)\in\mathcal W.}\tag{9}$$

**必要性。** 任意第三阶 gauge 对周期的改变量为零，对 ruling 的改变量都落在固定空间 $\mathcal W$。在函数商空间中，用 $\pi/2,\pi/4,3\pi/4$ 三个相位分离 (2)，即得 (8)–(9)。这一步不需要 gauge 预先有两个固定 profile 通道。

**充分性。** 写
$\mathscr K(A)=2\mathbf w\cdot v_A$、
$\mathscr K(B)=2\mathbf w\cdot v_B$、
$\mathscr K(C)=2\mathbf w\cdot v_C$。
由 §4，可准确选

$$\mathbf m(f,\psi_f)=v_A,\qquad \mathbf m(g,\psi_f)=0,$$

$$\mathbf m(f,\psi_g)=v_B,\qquad \mathbf m(g,\psi_g)=v_C.$$

用这两个 profile 修正第三阶解，(5) 同时消去三个完整 ruling 函数，(4) 保持其周期函数为零。完整 range 定理给三个四阶解，按 (2) 线性组合即得全相位解。

因此第四阶可调自由度的用途已经明确：它可准确清除 (9) 中的三个有限维分量，却不能改变 (8)，也不能清除落在 $\mathcal W$ 之外的 ruling 函数。这里只算完了条件，尚未证明本构造实际满足它们。

## 6. 下一实际计算可压缩完整圈，但不能改设计

在单个常 k、h、omega 的区间，固定 xi 时二阶 characteristic RHS 与 s 无关，因此 $W_2$ 对 s 为一次多项式。二阶场的标架分量及其协变一阶导数也至多一次；第三 forcing、rho3 和 characteristic RHS 至多一次，故 $W_3$ 及第三场标架分量至多二次。第四 forcing 与其 characteristic RHS 至多二次。

因此在这些长常段上，只要保留真正的段首积分常数、ruling 积分与 profile 导数，就可用准确的 s 多项式积分处理 N 个完整圈，无需按 N 逐圈采样。光滑连接仍须按同一冻结控制积分与加密；任何段首常数都不能为方便而重置。

先前八块有限 N 数值候选不是本稿单 P 零算子倒行构造，不能直接用于确认 (8)–(9)。若开发新四块运行器，应把新目标、控制参数、profile 的八 packet 幅度/位置、所有归一化和上下 collar 一次冻结，再做独立加密。其完整四阶周期残差与 ruling 商空间残差都必须原样保存。

即便 (8)–(9) 成功，仍然只有四阶形式解。继续到固定参数的精确族与题目要求的闭面比例，需要额外的收敛或非线性求解论证。
