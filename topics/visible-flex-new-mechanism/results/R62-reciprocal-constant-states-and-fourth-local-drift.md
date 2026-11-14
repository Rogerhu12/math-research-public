# R62：互反常态的二、三阶逆历史与完整第四局部漂移

日期：2026-11-14。独立准确推导，无新的研究数值。root 与 repo_sources 已全文交叉核对常态二阶分解、两圈与八维导数、第三混合项以及第四漂移分解。

本稿提供一个更小的零二阶 bulk 和高阶控制的准确接口。它不把二、三历史返回当成第四通过，也不删除真实连接段。当前已经冻结的首个完整第四数值输入保持原样。

## 1. 固定 h、d 时的两个 profile 算子

只在本节的常态段取 k、h、omega 为常数，且 $h>0$。固定

$$d=h\omega-k,\qquad e=h\xi+d,\qquad Q=1+e^2,$$

并取共同工作 xi 区间，使所用各状态的 $\xi+\omega$ 都不为零。特别地，对后面的 k=±1 可取 e>1；对应的 u 是各自的

$$u_k=\frac{h^2}{e+k},$$

不是把不同状态中相同 xi 的 u 数值强设为相同。

对任意紧支撑光滑 profile phi，记

$$J_\phi(\xi)=\int_\xi^r
\{Q(\eta)\phi''(\eta)^2+2h^2\phi'(\eta)^2\}\,d\eta.$$

完整常态二阶 characteristic RHS 记为 $\mathscr R_k(\phi,\phi)$。从既有完整恢复式逐项代入，得到

$$\begin{aligned}
\mathscr R_k(\phi,\phi)
={}&\frac{ke}{2}\phi^2-\frac{kQ}{2h}\phi\phi'
+\frac{Q(2ke+k^2-1)}{8h^2}\phi'^2\\
&+\frac{(e+k)(ke-1)}{8h^3}J_\phi.
\end{aligned}\tag{1}$$

定义两个与 k 无关的二次算子

$$\mathcal A_{h,d}[\phi]=\frac{Q\phi'^2}{8h^2}
+\frac{eJ_\phi}{8h^3},$$

$$\mathcal B_{h,d}[\phi]=\frac e2\phi^2-\frac Q{2h}\phi\phi'
+\frac{Qe}{4h^2}\phi'^2+\frac{e^2-1}{8h^3}J_\phi.$$

因 $(e+k)(ke-1)=e(k^2-1)+k(e^2-1)$，准确有

$$\boxed{\mathscr R_k=(k^2-1)\mathcal A_{h,d}+k\mathcal B_{h,d}.}\tag{2}$$

各式按普通对称双线性极化定义 $\mathscr R_k(a,b)$。在后文把 s 依赖的 W、U 代入这个符号时，指**当前 s 的 profile 值**，不把 W_s、U_s 混入静态算子的定义；真实时间导数另行保留。

## 2. 互反曲率给准确相反方向

对任意非零 k，(2) 直接给

$$\boxed{\mathscr R_{-1/k}=-\frac1{k^2}\mathscr R_k.}\tag{3}$$

这里两状态保持同一 h、d，故其 omega 分别为 $(d+k)/h$ 和 $(d-1/k)/h$。这些是不同的真实标量状态；从一个状态走到另一个仍须用真实连接，不能重置 omega。

常曲率 k 的准确 frame 周期是 $T(k)=2\pi/\sqrt{1+k^2}$。若 k=p/q>0 为正有理数，则分别走 q 个 k 圈和 p 个 −1/k 圈，后一个总时长是前一个的 k² 倍，因此 (3) 在整个 xi 函数层面准确积分相消。

特别地，k=+1、−1 的两个完整圈都有

$$T=\sqrt2\pi,$$

且 $\mathscr R_{+1}=\mathcal B_{h,d}$、$\mathscr R_{-1}=-\mathcal B_{h,d}$。两个圈已经支付整个二阶 RHS 的算子积分，不需要额外 k=0 圈。

### 八个常圈仍提供八维零算子修正

沿用 R37 的四个 $(h_i,d_i)$，每组只取两个曲率

$$k_{i,+}=1+\alpha_i+\beta_i,\qquad
k_{i,-}=-1-\alpha_i+\beta_i,$$

各走其真实完整周期。零参数时每组总矩阵为零。沿用 R37 的列向量 $\mathbf w_i,\mathbf A_i,\mathbf B_i$，准确导数为

$$\partial_{\alpha_i}M_{\rm bulk}(0)
=4\sqrt2\pi\,\mathbf w_i\mathbf A_i^T,$$

$$\partial_{\beta_i}M_{\rm bulk}(0)
=\sqrt2\pi\,\mathbf w_i\mathbf B_i^T.\tag{4}$$

这是把 R37 的 $f_A,f_B$ 导数在 a=1 评价，不是数值 Jacobian。四条 $\mathbf w_i$ 的射影一般位置及八维 rank 证明完全保留。

因此，可以用这八个常圈替代 R45 单 P 的十二个常圈，附加同样的真实平滑连接和终点 D 桥，再对

$$N F_{\rm bulk}(p)+G_D(p)=0$$

用同一八维隐函数定理。每个完整圈的 frame 恒为 I，桥的二阶矩阵成本及参数导数独立 N，故充分大有限 N 的准确单 P 零算子存在论证仍成立。

这只改进一种存在构造的 bulk。有限 N 修正后 k 不再严格等于 ±1；连接中的 h、omega 变化也必须真实保留。没有由此得到厚度、嵌入或全高阶相容。

## 3. 真实第三混合项与两个标量历史

本节在一个固定常态内推导。记

$$w=h^2-ku,\qquad
Y_a=uB\,a-\frac{uT+wB}{2h}a',$$

其中 $\xi=h/u-\omega$。对静态 profile a，

$$\partial_sY_a=t_aN,\qquad
t_a=k(Y_a\cdot T)+(Y_a\cdot B).$$

定义真正右 collar 锚定的双线性 normal 恢复

$$r_k(a,b)(u)=\frac12\int_{u_r}^{u}
(Y_a)_u\cdot(Y_b)_u\,dv,$$

其中 $u_r=h/(r+\omega)$。静态二阶算子恰是

$$\mathscr R_k(a,b)=\frac{t_at_b}{2u^2}
+K_0r_k(a,b),\qquad K_0=\frac{wk-u}{u^2}.\tag{5}$$

固定真实第一 profile phi 和目标 profile f，取

$$r=r_k(f,f)-r_k(\phi,\phi),\qquad
d_k=\mathscr R_k(f,f)-\mathscr R_k(\phi,\phi).$$

常态上的任意第二标量历史 W 满足 $W_s=d_k$，对应第二场

$$Z_2=rN-Y_W.\tag{6}$$

真实导数包含 $\partial_sY_W=Y_{d_k}+t_WN$。于是

$$Z_{2,s}=-\{r(kT+B)+Y_{d_k}\}-t_WN,$$

$$Z_{2,u}=r_uN-(Y_W)_u.$$

第三 forcing 是 $-2H(Y_\phi,Z_2)$，$H=\mathcal S/2$。其完整 normal 分量与标量 characteristic RHS 为

$$\rho_3=2r_k(\phi,W),\qquad
U_s=2\mathscr R_k(\phi,W).\tag{7}$$

特别地，局部项 rN 与 $Y_\phi$ 的混合张量虽然有非零 su 分量，其 ss、uu 分量都为零，所以它对 characteristic RHS 的贡献恰为零；这不等于可以删除它的向量恢复。

准确的第三局部混合量为

$$\eta_*=-\frac12t_\phi r_u+\frac12r(t_\phi)_u
+\frac12Y_{d_k}\cdot(Y_\phi)_u-r_k(\phi,d_k).\tag{8}$$

式 (8) 的第三项来自 $Y_{W_s}$；最后一项来自 $\rho_{3,s}/2$。两个都不能漏掉。置

$$G_* =\frac{\eta_*}{h^2}(uT+wB).$$

则完整第三场写成

$$\boxed{Z_3=2r_k(\phi,W)N+G_*-Y_U.}\tag{9}$$

r、d_k、eta_*、G_* 的框架系数均与入段 W、U 无关。又因 $ku+w=h^2$，

$$\partial_sG_*=\eta_*N.\tag{10}$$

这些是同一真实锚的恢复式；若相应 collar/ruling 条件尚未支付，公式保留真实尾，不宣称产生了双 collar 解。

## 4. 完整第四 RHS 的历史部分与局部漂移

第四 forcing 为

$$H_4=-H(Z_2,Z_2)-2H(Y_\phi,Z_3).$$

对常态，完整 characteristic RHS 只依赖 ss、uu 两分量（mixed 仍影响下一次向量恢复）。由 (6)–(10) 得到准确分解

$$\boxed{\mathcal R_{H_4}
=-\mathscr R_k(W,W)+2\mathscr R_k(\phi,U)
+\mathcal J_k(f,\phi).}\tag{11}$$

这里的 $\mathcal J_k$ 不含任何入段二、三历史，其定义完全明确如下。先置两个真实 diagonal 漂移分量

$$\mathcal D_{ss}=-|r(kT+B)+Y_{d_k}|^2
-2t_\phi\{2r_k(\phi,d_k)+\eta_*\},$$

$$\mathcal D_{uu}=-r_u^2
-2(Y_\phi)_u\cdot(G_*)_u.\tag{12}$$

沿同一个右 collar 取

$$\rho_{\mathcal D}(u)=\frac12\int_{u_r}^{u}\mathcal D_{uu}(v)\,dv,$$

再令

$$\boxed{\mathcal J_k(f,\phi)
=\frac{\mathcal D_{ss}}{2u^2}+K_0\rho_{\mathcal D}.}\tag{13}$$

这是一条具体的四次 profile 函数，不是未定义的余项。此处 f、phi 取实 profile，平方为普通欧氏平方；作复通道延拓时须用普通双线性平方，不擅自改成模平方。

**核对 (11)。** 第二场的 ss、uu 平方分别分成静态 $Y_W$ 的平方与 (12) 的前项。由

$$Z_{3,s}=\{2r_k(\phi,d_k)+\eta_*-t_U\}N
-2r_k(\phi,W)(kT+B)-Y_{U_s},$$

$Y_\phi$ 的 s 导数只沿 N，u 导数只在 T/B 平面，所以与 $Z_3$ 的两条 diagonal 配对正好给静态 $-H(Y_\phi,Y_U)$ 加 (12) 的其余项。整个 normal 原函数与 characteristic RHS 都线性，故 (11) 成立。这里没有把 $Y_W$ 的真实时间导数误作静态导数；它的 $Y_{d_k}$ 项已完整进入漂移。

## 5. 相反两段究竟返回什么

暂只比较两个同 (h,d)、相同真实长度 T、k=+1 与 −1 的常态历史方程，暂不插入连接。固定 f、phi，令第四历史的“非漂移部分”为 V。由 (2)、(7)、(11)，系统是

$$W_s=\mathscr R_k(f,f)-\mathscr R_k(\phi,\phi),$$

$$U_s=2\mathscr R_k(\phi,W),$$

$$V_s=-\mathscr R_k(W,W)+2\mathscr R_k(\phi,U).\tag{14}$$

在 k=±1 时，(14) 的**整个三角向量场**互为负号，而不只是第一条方程右侧相反。因此，正段走 T 再负段走 T，对于同一个右 collar 为零的 profile 状态空间中的任意共同入值 W、U、V 都准确返回。这里允许尚未支付的左尾，但不允许更换右锚或任意添加非零右端值。

如果把完整第四漂移也计入，两个常态的净额外 fourth primitive 为

$$\boxed{T\{\mathcal J_{+1}(f,\phi)+\mathcal J_{-1}(f,\phi)\}.}\tag{15}$$

各项在其正确的 $u_k(\xi)$ 上评价，然后作为共同 xi 函数相加。式 (15) 尚未证明为零；它是下一步可直接研究的准确局部算子。第三 mixed 部分即使不进入 (7)，仍通过 (8)、(12) 进入 (15)。

## 6. 真实连接与下一问题

(14) 的理想逆历史不是一条可直接使用的光滑曲面连接。两个常态有不同 k 和 omega，真实的变 h、变 k 桥会改变 W、U 和更高历史；第二常段的入值将不再是理想逆流所需的值。

R37/R45 所说桥的二阶矩阵成本独立 N，仅针对那一条低阶积分。它**不**说明桥的高阶作用为 O(1)：桥可能接收 O(N) 的第二历史及 O(N²) 的第三历史，从而与长常段耦合产生高阶大项。八维零算子修正还会使曲率离开准确 ±1；这些都不能从 (15) 之外删除。

本稿已付的是更小的准确零二阶 bulk、两真实标量历史及第四完整漂移分解。下一步是分析 (15) 的符号或可调整方向，同时把真实桥与修正后的状态纳入完整第四系统。没有声称完整第四 range、无限阶收敛、有限等距族或宏观闭面已完成。
