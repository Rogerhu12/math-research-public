# R112：局部第四密度的几何导数权只有零、二、四

日期：2026-11-14。**纸面已证明。** 使用 [R56](../results/R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](../results/R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R76](../results/R76-local-third-exact-loops-and-weight-three-control.md) 与 [R109](../results/R109-local-density-of-the-complete-fourth-quotient.md)。没有运行新的研究编译或几何计算。

## 1. 导数权与真实局部化

给 $h,k,\omega$ 及其任意整数幂权零，给 $j$ 阶 $s$ 导数权 $j$。代入 $\omega_s=k_s/(2h)$ 及其导数。$\xi$、profile jets 和右端 profile 原函数在此全部为权零；这不是 profile 仿射权。

令 $v$ 为 R109 的真实第四局部生成元：先求全体实际 $s$ 导数并代入 history 微分方程，再把累计历史的值置零。下面的权表始终采用这个次序。

记 $\mathcal P=\operatorname{span}(T,B)$，法框架分量为 $N$；使用 R56 的分子，不把物理公共分母 $z=\xi+\omega$ 单独当作新 profile。几何状态权零，故这个分母不改变此处的导数权。

**结论：**

$$
v=v^{[0]}+v^{[2]}+v^{[4]}.
\tag{1}
$$

R109 所选局部势满足 $N_{\rm pot}=N_{\rm pot}^{[0]}+N_{\rm pot}^{[2]}$，R73 点态算子满足 $m=m^{[0]}+m^{[2]}$，所以完整局部成本同样为

$$
\boxed{
\mathscr L_4=v-\mathcal B_m(N_{\rm pot})
=\mathscr L_4^{[0]}+\mathscr L_4^{[2]}+\mathscr L_4^{[4]}.
}
\tag{2}
$$

## 2. 低阶场的逐项权表

框架连接 $\Omega(k)$ 权零；对几何系数的普通 $s$ 微分升一权。二者必须分开，不能把整个 cov 导数机械视为升一权。

下表中花括号列出可能出现的权，空集表示分量恒零。$K_2,K_3$ 是在累计 history 值为零时的场值；标成“真实导数”的行仍保留这些 history 的非零导数。

| 分子或真实导数 | $\mathcal P$ 分量的权 | $N$ 分量的权 |
|---|---|---|
| 第一阶 $Y$ | $\{0\}$ | 空集 |
| $\nabla_sY$ | $\{1\}$ | $\{0\}$ |
| $K_2$ | $\{1\}$ | $\{0\}$ |
| $\nabla_sZ_2$ 在 history 值零时 | $\{0,2\}$ | $\{1\}$ |
| $K_3$ | $\{0,2\}$ | $\{1\}$ |
| $\nabla_sZ_3$ 在 history 值零时 | $\{1,3\}$ | $\{0,2\}$ |

第一行及其导数直接来自 R73 的

$$
V_f=(-f'/2,0,hf-ef'/2),\quad
\nabla_sV_f=(0,h(f-zf'/2),h_sf-e_sf'/2).
$$

第二恢复的 $P_2,B_2$ 权零，$\eta_{0,2}$ 权一，所以 $K_2$ 的表行成立。真求导还含 $-Y_{W_2'}$，其中 R73 给 $W_2'=m^{[0]}+m^{[2]}$；它位于 $\mathcal P$，给出 $\{0,2\}$，不能因 $W_2=0$ 而删掉。

第三 forcing 的两个分子点积中，$J_3,T_{\xi,3}$ 权一；mixed 点积权零或二。对其 $P_3$ 作真实求导时，除几何系数的权二导数外，还含 $W_2'$ 的权零或二项。因此 $\eta_{0,3}$ 权零或二，$K_3$ 的表行成立。

再求真实 cov 导数时，几何系数导数和连接给表列；额外 history 链式项只有此前的 $W_2'$、$W_2''$ 及 $W_3'$。其中

$$
W_2':\{0,2\},\qquad W_2'':\{1,3\},\qquad
W_3':\{1,3\}
$$

在零累计值处成立，最后一式也正是 R76 的完整局部第三权分解。它们分别补到表中已经列出的分量与权，不新增其他权。这个推导始终保留真实输入历史传递，不把 $K_3$ 当成只依赖静态几何的一阶场。

## 3. 第四 characteristic RHS

第四 forcing 是 $-H(Z_2,Z_2)-2H(Y,Z_3)$。由第 2 节，分子配对的权满足

$$
J_4,T_{\xi,4}:\{0,2\},\qquad T_{s,4}:\{0,2,4\}.
$$

真实 $J_{4,s},(T_{\xi,4})_s$ 权一或三。这既可由表中的两种真实导数点积看出，也可由连接反对称下的精确等式

$$
D_s(V_i\cdot V_j)=
\nabla_sV_i\cdot V_j+V_i\cdot\nabla_sV_j
$$

以及其 $\xi$ 导数形式直接核对。因此

$$
P_4,B_4:\{0,2\},\qquad
(P_4)_s,(B_4)_s:\{1,3\}.
$$

R56 的完整原式为

$$
R_4=\frac{T_{s,4}}{2h^2}+K_0P_4-\lambda(P_4)_s+
\left(kz-\frac{k^2+1}{h}\right)B_4-\frac{h_s}{h^2}(B_4)_s.
$$

其中 $K_0,z,h,k$ 权零，$\lambda,h_s$ 权一，故得到 (1)。没有做周期积分，也没有先假设低阶 ruling 或 period 为零。

R109 的 $P_{\rm acc}$ 权二，$P_h,F_*$ 权零；再用 R73 的点态 $m^{[0]}+m^{[2]}$，得到 (2)。这给后续 consumer 的三个准确有限片，而非经验性的低阶截断。

## 4. 改变实际长度的范围

对固定 scalar 轨迹 $S(\sigma)$，令真实参数 $s=\delta\sigma$。仅作为局部积分的代数恒等，有

$$
\int\mathscr L_{4,\delta}\,ds
=\delta\int\mathscr L_4^{[0]}\,d\sigma
+\delta^{-1}\int\mathscr L_4^{[2]}\,d\sigma
+\delta^{-3}\int\mathscr L_4^{[4]}\,d\sigma.
\tag{3}
$$

但同时实际总二阶矩阵改变为

$$
M_\delta=\delta\int m^{[0]}\,d\sigma+
\delta^{-1}\int m^{[2]}\,d\sigma,
$$

且 frame 的实际 ODE 时长改变。原路径的 $M=0$ 与 frame 端口一般不会对全部 $\delta$ 保留。因此 (3) **不授予三个成本的独立真实可调性**，不允许把其中某一项当成可自由缩放的实际零矩、零第三成本。

完整曲面范围、第四 ruling、受约束局部积分及真实成本商仍须另行支付。
