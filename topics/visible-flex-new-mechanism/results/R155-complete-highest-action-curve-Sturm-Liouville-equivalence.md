# R155：完整最高第四 action 的真实曲线族 Sturm–Liouville 判据

日期：2026-11-15。**已证明。** 纸面推导，无新原式评价或研究计算。

依据 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R137](R137-real-fast-pulse-positivity-and-acceleration-PSD.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md) 与 [R152](R152-fixed-h-Sturm-Liouville-highest-action.md)。

本稿不再只限制固定 h 或固定 k：它把完整正规最高层在**全部真实水平平端路径**上的非负性，准确等价为一族一维 Sturm–Liouville 二次型非负。每条状态曲线上的全部面积项、速度四次项、真实 $\omega$ 导数和边界势都保留。

这是最高层的充要判据，仍不是包含 $L_0,L_2$ 和同一矩阵乘子的完整成本正性定理，也不是一个已经解决的有限维可控性结论。

## 1. 完整正规最高层及实际水平状态

令 $\mathscr D$ 是 $\{h>0\}$ 中任意开状态域，坐标为

$$S=(h,k,\omega).$$

若需要固定物理 profile 带，可取 $\mathscr D$ 为同一严格非零 $\xi+\omega$ 分支内的开域；后面的所有重参数都不离开已经选择的状态曲线像。

在 $\mathscr D$ 上给定光滑实对称矩阵 $\mathsf A(S)$、实二元向量 $\mathsf H(S)$，以及速度变量的实齐次四次式 $\widehat Q_4(S;v)$。它们可以是完整原系数在某个实泛函 $\lambda$ 下的评价。写

$$
\mathsf A=
\begin{pmatrix}
\bar A_{hh}&\bar A_{hk}/2\\
\bar A_{hk}/2&\bar A_{kk}
\end{pmatrix},
\qquad
\mathsf H=(H_1,H_2).
$$

对真实水平路径 $S(s)$，令

$$
v=(h_s,k_s),\qquad a=(h_{ss},k_{ss}),
\qquad
\omega_s=\frac{k_s}{2h}.
\tag{1}
$$

完整最高层为

$$
\boxed{
L_4(S;v,a)
=a^T\mathsf A(S)a+
(\mathsf H(S)\cdot v)\det(v,a)+
\widehat Q_4(S;v).
}
\tag{2}
$$

这里

$$
\widehat Q_4
=Q_4^v-D_0P_{3v}-\mathcal B_{m_2}(N_2)
\tag{3}
$$

是 R129、R134、R140 的完整正规速度四次式。不能省略 N2、三阶势的真实状态导数或任何已知 pure 投影看不见的项。

本定理不预先要求 $\mathsf A$ 正定或半正定，也不要求仿射字符条件。它对给定的全部实系数 (2) 成立；正字符只是后续的一种应用。

## 2. 固定真实状态曲线上的三个系数

令 $J\subset\mathbb R$ 为开参数区间，并取任意光滑真实水平曲线

$$
\Gamma(t)=(h(t),k(t),\omega(t))\in\mathscr D,
\qquad
\omega_t=\frac{k_t}{2h}.
\tag{4}
$$

不要求 $\Gamma$ 单射或其速度处处非零。以下每个测试只使用其某个紧参数子区间，所以涉及的状态与系数都在紧集内。

记

$$
V=(h_t,k_t),\qquad A=(h_{tt},k_{tt}).
$$

定义

$$
a_\Gamma=V^T\mathsf A(\Gamma)V,
\tag{5}
$$

$$
b_\Gamma=2V^T\mathsf A(\Gamma)A,
\tag{6}
$$

$$
c_\Gamma=A^T\mathsf A(\Gamma)A+
(\mathsf H(\Gamma)\cdot V)\det(V,A)+
\widehat Q_4(\Gamma;V),
\tag{7}
$$

以及准确的一维势

$$
\boxed{
e_\Gamma=c_\Gamma-\frac13\frac{d}{dt}b_\Gamma.
}
\tag{8}
$$

导数 (8) 是沿实际水平曲线的**总导数**。特别对任何状态系数 F，

$$
\frac{d}{dt}F(\Gamma(t))
=h_t\,\partial_hF+
k_t\left(\partial_k+\frac1{2h}\partial_\omega\right)F.
\tag{9}
$$

它也作用于 (6) 中的 V、A。因此若 $B=(h_{ttt},k_{ttt})$，则

$$
b_\Gamma'
=2A^T\mathsf A A
+2V^T\left(h_t\partial_h\mathsf A+
k_t\left(\partial_k+\frac1{2h}\partial_\omega\right)\mathsf A\right)A
+2V^T\mathsf A B.
\tag{10}
$$

没有把 $\omega$ 固定，也没有把 V、A 误作与 t 无关。三阶曲线导数出现在 (10)，但只是固定参数曲线产生的一维系数；它不新增原 action 的未知 jet。

## 3. 真实重参数与准确边界消去

令 $t=t(s)$ 是任意光滑函数，其像在 J 的紧子区间中，且在 s 的两端开邻域为常数。允许 t 转向。复合路径

$$
S(s)=\Gamma(t(s))
$$

仍真实水平，因为

$$
\omega_s=\omega_t t_s
=\frac{k_t t_s}{2h}
=\frac{k_s}{2h}.
\tag{11}
$$

记 $\dot t=t_s,\ddot t=t_{ss}$。实际速度与加速度为

$$
v=V\dot t,\qquad
a=V\ddot t+A\dot t^2.
\tag{12}
$$

对面积因子，

$$
\det(v,a)
=\dot t^3\det(V,A).
\tag{13}
$$

所以它与 $\mathsf H\cdot v$ 相乘后是完整的 $\dot t^4$ 项；它不是零，也没有落入混合 $\ddot t\dot t^2$ 项。

将 (12)、(13) 逐项代入 (2)，得到

$$
\boxed{
L_4(S(s))
=a_\Gamma(t)\ddot t^2
+b_\Gamma(t)\ddot t\,\dot t^2
+c_\Gamma(t)\dot t^4.
}
\tag{14}
$$

由于 t 平端，$\dot t=0$ 在两个端部，故准确总导数

$$
\frac{d}{ds}\left[b_\Gamma(t)\dot t^3\right]
=b_\Gamma'(t)\dot t^4
+3b_\Gamma(t)\ddot t\,\dot t^2
$$

的端点值为零。因而

$$
\boxed{
\int L_4(\Gamma\circ t)\,ds
=\int\left[a_\Gamma(t)\ddot t^2+
e_\Gamma(t)\dot t^4\right]ds.
}
\tag{15}
$$

这个积分身份没有遗失原两端势，也没有用负物理时长。t 可以下降或任意转向。

对固定 $\Gamma$，R152 已把 (15) 对全部有限时间平端 t 的非负性，准确等价为

$$
\boxed{
\mathscr Q_\Gamma[\psi]
=\int_J\left[
\frac49a_\Gamma(t)(\psi_t)^2+
e_\Gamma(t)\psi^2\right]dt\ge0
\quad
(\psi\in C_c^\infty(J;\mathbb R)).
}
\tag{16}
$$

R152 的证明允许任意连续 $a_\Gamma,e_\Gamma$，所以这里无需预先假设 $a_\Gamma\ge0$。

## 4. 全部最高 action 的充要定理

**定理。** 对给定状态域 $\mathscr D$ 和完整系数 (2)，下列两条等价：

1. 每一条有限时间、两端开邻域 scalar 常值、满足 (1)、像在 $\mathscr D$ 内的光滑真实路径 P，都有
   $$
   \int_P L_4\,ds\ge0;
   \tag{17}
   $$
2. 每一条像在 $\mathscr D$ 内的光滑真实水平曲线 $\Gamma:J\to\mathscr D$，其 (16) 对全部实光滑紧支撑测试函数非负。

这里条件 2 是曲线族上的准确二次型条件，不是假定 $\mathsf A$、$\mathsf H$、$\widehat Q_4$ 的形式系数可以独立实现。

### 4.1 必要性：负二次型能由真实有限平端路径实现

假设 (17) 成立，但某条 $\Gamma$ 的某个测试函数使 (16) 为负。只取包含其支撑的紧参数区间 $[a,b]\subset J$。

R152 第 5 节从这个负测试函数构造实际有限时间单调平端 $t_\varepsilon(s)$，其像就是 $[a,b]$，并且

$$
\int\left[
a_\Gamma(t_\varepsilon)(t_\varepsilon'')^2+
e_\Gamma(t_\varepsilon)(t_\varepsilon')^4
\right]ds<0.
\tag{18}
$$

为明确这里没有无限时间缺口，R152 的构造是：把测试函数非负光滑化为 f，取一条固定真实平端参数路径 $\kappa:[0,1]\to[a,b]$，置

$$
\psi_*=(\kappa'\circ\kappa^{-1})^{3/2},\qquad
\psi_\varepsilon=f+\varepsilon\psi_*,
$$

再反解 $ds/dt=\psi_\varepsilon^{-2/3}$。由于

$$
\int_a^b\psi_*^{-2/3}dt=1,
\qquad T_\varepsilon\le\varepsilon^{-2/3}<\infty,
$$

每一个所用 $\varepsilon>0$ 都给有限时间。端部 f 为零，反函数准确是 $\kappa$ 的有限时间缩放，所以所有端 jets 为零；再接常值开段即为平端。

复合 $P_\varepsilon=\Gamma\circ t_\varepsilon$ 的全部 scalar 端 jets 也为零。其像始终在原紧曲线像 $\Gamma([a,b])\subset\mathscr D$，水平关系由 (11) 保持。由 (15)、(18)，其完整最高 action 为负，矛盾。

这里没有通过缩短参数改变 h,k,ω 的端状态，也没有用只形式存在的速度剖面冒真实平端路径。

### 4.2 充分性：原路径本身给一个合法测试

反向假设全部 (16) 非负。取任意满足 (17) 范围的真实平端 P，参数为 $s\in[0,L]$。令

$$
\Gamma(t)=P(t)
$$

并在两端稍向外按常值延拓，成为一个定义在开参数区间 J 上的光滑水平曲线。

因为 P 在两个端部开邻域 scalar 常值，那里 $V=A=B=0$，且

$$
a_\Gamma=b_\Gamma=c_\Gamma=e_\Gamma=0.
\tag{19}
$$

这些一维系数共同支撑在 $(0,L)$ 内的一个紧集。取

$$
\psi\in C_c^\infty((0,L)),\qquad
\psi=1
$$

于包含这个共同支撑的邻域。于是 $\psi'$ 的支撑上 $a_\Gamma=0$，并由 (8) 的边界总导数，

$$
\mathscr Q_\Gamma[\psi]
=\int_0^L e_\Gamma\,dt
=\int_0^L c_\Gamma\,dt.
\tag{20}
$$

把 $\Gamma=P$ 的实际速度和加速度代入 (7)，正好是原路径的完整最高层：

$$
c_\Gamma(t)=L_4(P(t)).
\tag{21}
$$

因此

$$
\int_P L_4\,ds=\mathscr Q_\Gamma[\psi]\ge0.
$$

这支付充分性。它不要求把原路径切成有限条规则弧；原路径可以有零速度、累积转向、自交或任意多个停顿。条件 2 允许这样的光滑 $\Gamma$，而所有重参数内部的可数弧和零速度细节已经在 R152 中完整处理。

## 5. 已有一维门是该定理的具体子类

取 $h=H$ 固定，以参数 t=k、并令 $\omega=\omega_*+(t-k_*)/(2H)$。则

$$
V=(0,1),\quad A=0,\quad
a_\Gamma=A_{kk}(H,t,\omega(t)),\quad b_\Gamma=0.
$$

面积项准确为零，(16) 恢复 R152 的固定 h 门。在仿射字符范围，系数独立于 $\omega$，恰成为其 $H^\sigma$ 倍。

取 k、ω 固定，以参数 t=h>0，则

$$
V=(1,0),\quad A=0,\quad
a_\Gamma=A_{hh}(t,k_0,\omega_0),\quad b_\Gamma=0,
$$

而 $e_\Gamma=[u^4]\widehat Q_4((t,k_0,\omega_0);u,0)$。仿射字符使这两个系数成为相应幂次；R148 已对这类幂系数二次型支付 sharp 必要充分常数。

对一般弯曲状态路径，(7)、(8) 中的

$$
(\mathsf H\cdot V)\det(V,A)
$$

必须保留，$b_\Gamma'$ 也必须按 (9)、(10) 求完整水平总导数。不能从两个坐标轴门推断完整 (16) 已经成立。

## 6. 解释与边界

对 R137/R140 的真实成本正泛函，(17) 是已经支付的必要条件，因此本定理给出同一个泛函必须满足的全部最高层曲线二次型门。反向若这些门全部成立，就准确恢复最高层在全部真实水平平端路径上的非负性；它没有恢复完整 $L_0,L_2,L_4$ action 的非负性，也没有自动找到 R140 的同一个矩阵乘子。

该判据没有将无穷曲线族降成有限个待检系数，也没有宣称存在或不存在满足它的非零正泛函。它提供的是完整、没有丢掉面积或端势的变分等价。

所有实际实现只改变给定状态曲线的行进速度，保持其有限紧状态像；若这个像原本有固定物理间隙，有限时间 cap 不改变该间隙。框架终态、中心位移、M/T 补偿及宏观长度仍按原真实几何处理。本文不把曲线重参数视作同一有限曲面的固定度量形变。

完整 ruling、成本半群的有符号逆元、嵌入与 reach、有限等距族都没有由本稿支付。

