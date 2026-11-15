# R184：允许二阶齐次 gauge 后，固定圆完整第四 range 的仿射线性判据

日期：2026-11-15。**纸面完整证明；没有新研究计算。** 复用 [R47 单 profile 三矩右逆](R47-fourth-order-range-and-third-gauge.md)、[R56 完整 range 与有限表示](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R83 真实历史传递](R83-true-fourth-transfer-and-zero-lower-history-variations.md)，以及 [R180](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md)–[R181](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)。

本稿固定真实几何、第一 profile 圆及同一个目标度量，允许二阶齐次解和全部第三阶齐次解变化。关键是：二阶 gauge 对第四 forcing 的平方项虽不为零，却全部落在第三 gauge 可以支付的 ruling 空间内；总矩阵 M=0 又使它的第四周期贡献为零。取相应商后，剩余问题准确是同一二阶 gauge 的仿射线性匹配，而非另一个未经处理的二次优化问题。

这一判据没有证明匹配方程已有解。

## 1. 固定数据与全部允许的二阶改动

固定一个真实光滑周期 ruled 几何及共同紧物理区间 I，$h>0$、$\xi+\omega>0$，frame/scalar 周期，全部 profiles 在共同双 collar 为零。假设整个 second 算子为零：

$$A=\Phi_M=0. \tag{1}$$

不要求整个第三算子 T 为零。取实线性无关的 f、g，令

$$\phi_\theta=\cos\theta f+\sin\theta g,\qquad
F=f^2,\qquad D_\theta=F-\phi_\theta^2.$$

固定目标仍为 $g_\varepsilon=g_X+\varepsilon^2(dY_f)^2$。假设选定的 canonical 二阶、三阶恢复

$$Z_\theta=Z_B(D_\theta),\qquad W_\theta=W_B(\phi_\theta,D_\theta)$$

已经完整通过周期与双 collar range，随 $\theta$ 光滑、$2\pi$ 周期，且在 $0,\pi$ 的高阶场为零。R180/R183 提供了具备这些前提、全 T 仍非零的具体低阶构造。

齐次 range 分类表明，任何同周期、同 collar 的另一个二阶解都可写成

$$\widetilde Z_\theta=Z_\theta-Y_{w_\theta}, \tag{2}$$

其中 $w_\theta$ 是同 collar 的实光滑 profile 家族。要求相位光滑、$2\pi$ 周期，且 $w_0=w_\pi=0$，保留两个指定准确种子。

## 2. 二阶 gauge 保持第三 range 的准确线性定义域

记

$$\mathbf w(s)=\left(\frac{d(s)^2+1}{4h(s)},
\frac{d(s)}2,\frac{h(s)}4\right),\qquad d=h\omega-k,$$

$$\mathbf m(a,b)=\left(
\int a''b'',\ \int\xi a''b'',\
\int\xi^2a''b''+2\int a'b'\right).$$

R47 已给原式恒等

$$\int (Y_a)_u\cdot(Y_b)_u\,du
=\mathbf w(s)\cdot\mathbf m(a,b). \tag{3}$$

这里 u 为物理 ruling 坐标，不是新的 scalar 历史。三列几何函数张成固定有限空间

$$\mathcal W=\{s\mapsto\mathbf w(s)\cdot v:v\in\mathbb R^3\}. \tag{4}$$

二阶改动 (2) 使第三 forcing 增加 $2H(Y_{\phi_\theta},Y_{w_\theta})$。其完整周期为 $2A(\phi_\theta,w_\theta)=0$；它的 ruling 为 $2\mathbf w\cdot\mathbf m(\phi_\theta,w_\theta)$。所以新增第三恢复合法，当且仅当

$$\boxed{\mathbf w(s)\cdot
\mathbf m(\phi_\theta,w_\theta)=0
\quad\text{对全部 }s,\theta.} \tag{5}$$

这不是仅在网格上取零，也不把几何三列预先假定独立。如果三列有依赖，(5) 允许相应矩向量落在它们的真实核中。

记满足共同 collar、相位、种子及 (5) 的家族组成实线性空间 $\mathcal D$。六条更强的条件 $\mathbf m(f,w_\theta)=\mathbf m(g,w_\theta)=0$ 足以给 (5)，但不是本稿定义域的额外必要要求。

对任一 $w\in\mathcal D$，第三场可取

$$\widetilde W_\theta
=W_\theta+2Z_B(\phi_\theta,w_\theta)+Y_{\chi_\theta}, \tag{6}$$

其中 $Z_B(\phi_\theta,w_\theta)$ 使用同一真实右锚和 s 起点。完整 range 与 (1)、(5) 保证它周期、双 collar；$\chi_\theta$ 是尚待选择的全部第三齐次自由度。反过来，任何合法第三解与 (6) 前两项之差都恰为这种 $Y_{\chi_\theta}$。

## 3. 第四周期与 ruling 的完整改变

令原第四 forcing、周期和 ruling 分别为

$$H^0_{4,\theta}=-H(Z_\theta,Z_\theta)-2H(Y_{\phi_\theta},W_\theta),$$

$$V^0_\theta=\mathscr P(H^0_{4,\theta}),\qquad
K^0_\theta(s)=\mathscr K(H^0_{4,\theta})(s).$$

$\mathscr P$ 是整个 $\xi$ 周期函数，$\mathscr K(H)=\int H_{uu}\,du$。将 (2)、(6) 直接代入，得到

$$\begin{aligned}
\Delta H_{4,\theta}={}&2H(Z_\theta,Y_{w_\theta})
-H(Y_{w_\theta},Y_{w_\theta})\\
&-4H(Y_{\phi_\theta},Z_B(\phi_\theta,w_\theta))
-2H(Y_{\phi_\theta},Y_{\chi_\theta}). \tag{7}
\end{aligned}$$

没有省略 gauge 平方。R83 给其完整周期

$$\boxed{\widetilde V_\theta
=V^0_\theta+\mathcal L_\theta(w_\theta),} \tag{8}$$

$$\boxed{\mathcal L_\theta(w)
=2T(w;D_\theta)-4T(\phi_\theta;\phi_\theta,w).} \tag{9}$$

平方项 $-A(w,w)$ 及第三齐次项 $-2A(\phi_\theta,\chi_\theta)$ 都由 (1) 准确为零。式 (8) 因而对 w 是全函数仿射线性，不仅是原点切向。

定义同一二阶 gauge 的线性 ruling 响应

$$\boxed{\begin{aligned}
\mathcal B_\theta(w)(s)={}&
2\int (Z_\theta)_u\cdot(Y_w)_u\,du\\
&-4\int(Y_{\phi_\theta})_u
\cdot (Z_B(\phi_\theta,w))_u\,du .
\end{aligned}} \tag{10}$$

由 (3)、(7)，

$$\boxed{\widetilde K_\theta
=K^0_\theta+\mathcal B_\theta(w_\theta)
-\mathbf w\cdot\mathbf m(w_\theta,w_\theta)
-2\mathbf w\cdot\mathbf m(\phi_\theta,\chi_\theta).} \tag{11}$$

特别地，在同一个真实几何函数商空间中，

$$\boxed{[\widetilde K_\theta]
=[K^0_\theta+\mathcal B_\theta(w_\theta)]
\quad\text{于 }C^\infty(S^1_s)/\mathcal W.} \tag{12}$$

这就是平方项可以从**商问题**中消去的准确原因。它在未取商的 forcing/ruling 中仍然存在。

## 4. 完整第四存在性的必要充分条件

**定理。** 在上述固定几何、目标、第一圆及已付第三 range 的前提下，允许全部二阶、三阶齐次改动，并保持相位光滑、周期及两个准确种子，则完整第四校正存在，当且仅当存在同一个 $w\in\mathcal D$，使

$$\boxed{V^0_\theta+\mathcal L_\theta(w_\theta)=0
\quad\text{于整个 }I,\ \text{对全部 }\theta,} \tag{13}$$

$$\boxed{K^0_\theta+\mathcal B_\theta(w_\theta)
\in\mathcal W
\quad\text{作为整个 }s\text{ 函数，对全部 }\theta.} \tag{14}$$

条件 (5)、(13)、(14) 对未知家族 w 联合为仿射线性。不能对 period 和 ruling 分别选两个不同 w。

**必要性。** 任意完整解的二阶差具有 (2) 形式；第三差 forcing 必须在完整 range 内，所以 w 满足 (5)。由齐次分类，第三差有 (6) 形式。第四完整 range 要求 (8)、(11) 均为零，立即给 (13)、(14)。

**充分性。** 先选满足两式的同一 w。令

$$k_\theta=K^0_\theta+\mathcal B_\theta(w_\theta)
-\mathbf w\cdot\mathbf m(w_\theta,w_\theta)\in\mathcal W.$$

选择固定线性右逆 $S:\mathcal W\to\mathbb R^3$，满足
$\mathbf w(s)\cdot S(k)=k(s)$；此处 $S(k)$ 是与 s 无关的三维向量，不是逐 s 选取的向量。令 $v_\theta=S(k_\theta)/2$。

R47 第 4 节已经证明：对任意非零紧支撑实 profile $\phi$，$\chi\mapsto\mathbf m(\phi,\chi)$ 到 $\mathbb R^3$ 满射。其三个 adjoint 密度是

$$L_0\phi=\phi'''',\quad
L_1\phi=\xi\phi''''+2\phi''',\quad
L_2\phi=\xi^2\phi''''+4\xi\phi'''.$$

因为 f、g 实线性无关，每个 $\phi_\theta$ 都非零。相应 Gram 矩阵

$$G^\theta_{ij}=\int(L_i\phi_\theta)(L_j\phi_\theta)$$

对全部 $\theta$ 严格正定；它随相位光滑且周期，紧圆上其逆也光滑有界。准确取

$$\boxed{\chi_\theta
=\sum_{j=0}^2[(G^\theta)^{-1}v_\theta]_j L_j\phi_\theta.} \tag{15}$$

则 $\mathbf m(\phi_\theta,\chi_\theta)=v_\theta$，(11) 全零。所有 $\chi_\theta$ 的支撑仍在固定双 collar 以内；这是全局同一 profile 家族，不是逐 ruling 重选 gauge。即使 f、g 的六个联合密度有关系，单 $\phi_\theta$ 的满射已经足够。

在 $\theta=0,\pi$，原 forcing 为零，w 为零，故 $k_\theta=v_\theta=\chi_\theta=0$；指定种子保持。第三齐次改变不影响 (13)。于是第四 forcing 的完整周期及全部 ruling 同时为零，R56 的完整 range 恢复给光滑、周期、双 collar 的第四场；恢复对光滑相位资料线性，故可取一个光滑周期的全相位家族。$\square$

## 5. 非零 hook 几何的固定圆不变量

若进一步 $T=\kappa\mathfrak H$，R180 的循环恒等式使 (9) 简化为

$$\mathcal L_\theta(w)=2\kappa L_f(w),
\qquad L_f(w)=\mathfrak H(w;f,f), \tag{16}$$

其线性算子不再依赖 $\theta$。周期方程就是

$$2\kappa L_f(w_\theta)=-V^0_\theta. \tag{17}$$

R181 的通量身份立即给新的固定圆必要门。若 $[a,b]$ 是 f 的一个平端支撑包，则

$$\boxed{\int_a^b f'''(\xi)V^0_\theta(\xi)\,d\xi=0
\quad\text{对全部 }\theta.} \tag{18}$$

更强地，置 $p=f'$、$q=f''$、$A_f=6pq'-2q^2$。从该包左端 a 到任一内部 $A_f(x_0)=0$，必须有

$$\boxed{\int_a^{x_0}f'(\xi)
\partial_\xi^2V^0_\theta(\xi)\,d\xi=0.} \tag{19}$$

这些量对所有允许的二阶 gauge 不变；并不要求它来自 universal U 上的正字符，也不要求固定圆 faithful。若某个具体几何/profile 的原值不为零，即可排除用本稿 gauge 类支付第四周期。本文没有评价任何具体 $V^0$，不声称 (18)、(19) 实际非零，也不把它们作为完整可解的充分条件。

## 6. 实现边界与后续可计算接口

这一新问题的未知量是 w，而不是另行优化目标度量、第一圆或全路径。指定一个有限 w 试空间后，R56 的有限分离变量恢复给 (5)、(13)、(14) 的真实全函数线性映射；冗余 profile/几何生成元必须使用其真实函数关系，不能把采样零或逐系数零误当完整必要条件。

若采用有限相位谐波试空间，它只是一个明确充分搜索类；本稿没有证明任意光滑相位解都能改为该有限谐波形式。特别地，任意相位二阶 gauge 可以改变 pure 第四模式，R180 的 pure 不变只针对其特定 $\sin^2\theta$ 选择。

完整第四 forcing 的 gauge 平方通过 (15) 真实支付，而不是删除；由此可得第四形式校正的充分性。更高阶、形式级数收敛、有限非零参数的精确等距族、嵌入与 reach 仍分别未付。R180/R183 的低阶例是否满足联合线性方程，当前仍是开放问题。

