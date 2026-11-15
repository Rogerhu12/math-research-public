# R167：完整最高 action 的四单项 Gram 充分证书

日期：2026-11-15。**已证明。** 本稿只有纸面恒等式与不等式推导，不新增原式编译、profile 或几何评价，也不对已经被静态门排除的候选另跑最高层测试。

依据 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R137](R137-real-fast-pulse-positivity-and-acceleration-PSD.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R148](R148-sharp-one-dimensional-highest-action-positivity.md)、[R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)、[R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md) 和 [R165](R165-prescribed-h-quadratic-highest-action-and-loglinear-frequency-gate.md)。完整真权 −2 支撑与十个标量的原式来源沿用 R165 的已发 head 元数据。

**主要结论。** 对任意预设的正 h(s)，作 $k=e^r y$、$r=\log h$。完整最高密度减去一个明确的端势导数后，是只含

$$
Z=(y'',\ r'y',\ r''y,\ (r')^2y)^T
$$

的常系数四阶 Gram 型，以及固定 k=0 时的剩余 action。只要一个具有两个自由边界参数的 $4\times4$ 实对称矩阵半正定，再加 R148 的两个标量条件，就能严格证明**完整最高层**在全部真实平端路径上非负。

这是有限的**充分证书**。本稿没有证明其必要性：Gram 家族不可行，不能据此认定存在负路径或排除正字符。最高层证书可行，也不能替代完整静态、二次层和同一矩阵乘子的正性条件。

## 1. 同一个真实字符和完整最高层

令 $\lambda:U\to\mathbb R$ 是真实定义的权 −2 仿射字符，杀掉完整响应空间 R。尚不要求它正。按 R165 的支撑与记号，十个实数

$$
a,b,c,d,e,f,g,j,\ell,m
\tag{1}
$$

均来自同一个 $\lambda$，完整最高层是

$$
\begin{aligned}
L_4^\lambda={}&h^{-4}(a+bk^2)h_{ss}^2
+c h^{-3}k h_{ss}k_{ss}+d h^{-2}k_{ss}^2\\
&+(e h^{-4}k h_s+f h^{-3}k_s)
(h_s k_{ss}-k_s h_{ss})\\
&+g h^{-4}h_s^2k_s^2+j h^{-5}k h_s^3k_s
+h^{-6}(\ell+mk^2)h_s^4.
\end{aligned}
\tag{2}
$$

原导出中的准确索引是

$$
(a,b,c,d,e,f,g,j,\ell,m)
=\lambda(V_{90},V_{91},V_{94},V_{96},V_{97},V_{99},V_{100},V_{101},V_{103},V_{104}).
\tag{3}
$$

这里 $V_i$ 是 run 43665345551 的完整 head 两模式原系数；不是十个独立的控制方向。$d=\lambda(J_6)$，$\ell$ 是完整 D0 的字符值。式 (2) 的 Q4 已包括所有 $N^{[2]}$ 收缩和真实正规化；e、f 两个面积系数均保留。

在有限区间上，令 h>0、k 光滑且在两端开邻域分别为常数。真实水平变量始终由

$$
\omega_s=\frac{k_s}{2h}
\tag{4}
$$

确定。已取 $\lambda$ 的最高正规系数与 $\omega$ 无关，是完整仿射字符协变的结论；它不允许把原路径中的 $\omega$ 任意冻结。

置

$$
r=\log h,\qquad v=r',\qquad z=v'+v^2,\qquad \rho=e^{-2r},
\qquad k=e^r y.
\tag{5}
$$

于是

$$
h_s=hv,\quad h_{ss}=hz,\quad
k_s=e^r(y'+vy),\quad
k_{ss}=e^r(y''+2vy'+zy).
\tag{6}
$$

## 2. 完整共轭：只需要 v、v′ 和四个单项

定义

$$
Z_1=y'',\qquad Z_2=vy',\qquad
Z_3=v'y,\qquad Z_4=v^2y,
\tag{7}
$$

以及

$$
S=Z_1+2Z_2+Z_3+Z_4=y''+2vy'+zy,
\qquad T=y'+vy.
\tag{8}
$$

把 (6) 代入完整 (2)，可逐点写成

$$
\begin{aligned}
L_4^\lambda={}&\rho(a z^2+\ell v^4)
+dS^2+c(Z_3+Z_4)S+b(Z_3+Z_4)^2\\
&+e v y[vS-zT]+fT[vS-zT]
+g v^2T^2+jv^3yT+mv^4y^2.
\end{aligned}
\tag{9}
$$

式 (9) 是原式代入，没有分部积分，也没有消去任何 H 项。共同 $e^{2r}$ 与 $\rho$ 的消去只发生在含 k 的齐次二次部分；第一项仍准确保留。

面积因子的内部恒等式为

$$
vS-zT=v y''+(v^2-v')y'.
\tag{10}
$$

故 e 项准确变成

$$
e(Z_1Z_4+Z_2Z_4-Z_2Z_3).
\tag{11}
$$

f 项则准确变成

$$
f[Z_1Z_2+Z_1Z_4+Z_2^2-v'(y')^2+Z_2Z_4-Z_2Z_3].
\tag{12}
$$

只对 (12) 使用

$$
[v(y')^2]'=v'(y')^2+2vy'y''
=v'(y')^2+2Z_1Z_2,
\tag{13}
$$

即得下面的逐点身份：

$$
\boxed{L_4^\lambda=\rho(a z^2+\ell v^4)+Z^TG_0Z
-\frac{d}{ds}[f v(y')^2].}
\tag{14}
$$

这里 $G_0$ 是常实对称矩阵，其完整上三角如下，未列下三角由对称补齐。

| 元素 | 准确值 |
|---|---|
| $(G_0)_{11}$ | $d$ |
| $(G_0)_{12}$ | $2d+\tfrac32 f$ |
| $(G_0)_{13}$ | $d+\tfrac12 c$ |
| $(G_0)_{14}$ | $d+\tfrac12(c+e+f)$ |
| $(G_0)_{22}$ | $4d+f+g$ |
| $(G_0)_{23}$ | $2d+c-\tfrac12(e+f)$ |
| $(G_0)_{24}$ | $2d+c+g+\tfrac12(e+f+j)$ |
| $(G_0)_{33}$ | $d+c+b$ |
| $(G_0)_{34}$ | $d+c+b$ |
| $(G_0)_{44}$ | $d+c+b+g+j+m$ |

可直接按以下八项核对 (14) 的 Gram 部分：

$$
\begin{aligned}
Z^TG_0Z={}&d(Z_1+2Z_2+Z_3+Z_4)^2
+c(Z_3+Z_4)(Z_1+2Z_2+Z_3+Z_4)\\
&+b(Z_3+Z_4)^2
+e(Z_1Z_4+Z_2Z_4-Z_2Z_3)\\
&+f(3Z_1Z_2+Z_1Z_4+Z_2^2+Z_2Z_4-Z_2Z_3)\\
&+g(Z_2+Z_4)^2+j(Z_2Z_4+Z_4^2)+mZ_4^2.
\end{aligned}
\tag{15}
$$

本身份保留 v 和 v′；不需要把 v″、v‴作为新原系数接口，也没有借用长 log-linear 段的 $v'=0$ 特例。

## 3. 两个完全支付的边界参数

另有两个准确导数身份

$$
[v^2yy']'=Z_1Z_4+Z_2^2+2Z_2Z_3,
\tag{16}
$$

$$
[v^3y^2]'=2Z_2Z_4+3Z_3Z_4.
\tag{17}
$$

相应常对称矩阵为

$$
N_1=\begin{pmatrix}
0&0&0&1/2\\
0&1&1&0\\
0&1&0&0\\
1/2&0&0&0
\end{pmatrix},\qquad
N_2=\begin{pmatrix}
0&0&0&0\\
0&0&0&1\\
0&0&0&3/2\\
0&1&3/2&0
\end{pmatrix}.
\tag{18}
$$

对任意实 $\theta,\eta$ 定义

$$
G_{\theta,\eta}=G_0+\theta N_1+\eta N_2.
\tag{19}
$$

则完整逐点身份升级为

$$
\boxed{
L_4^\lambda=\rho(a z^2+\ell v^4)+Z^TG_{\theta,\eta}Z
-\frac{d}{ds}\bigl[f v(y')^2+\theta v^2yy'+\eta v^3y^2\bigr].
}
\tag{20}
$$

因为 h 的两端是常值 germs，v 在两个端部恒为零；$y=k/h$ 也光滑且平端。因此方括号在两个端部各自为零。左右 h、k 的常值可以不同；不需假设 y 紧支撑或把左端值与右端值相抵。

积分得到

$$
\boxed{
\int L_4^\lambda\,ds
=\int\rho(a z^2+\ell v^4)\,ds
+\int Z^TG_{\theta,\eta}Z\,ds.
}
\tag{21}
$$

$\theta,\eta$ 是可选端势系数，不是新增物理控制或可变 profile 成本。它们可以依赖正在研究的字符，但在一次证书中是固定常数，不能随 s 或状态自由变化，否则 (20) 会产生额外导数项。

## 4. 有限 Gram 充分定理

**定理。** 若十个真实字符标量满足

$$
a\ge0,\qquad \ell+\frac{25}{9}a\ge0,
\tag{22}
$$

并存在两个实数 $\theta,\eta$ 使

$$
\boxed{G_{\theta,\eta}\succeq0,}
\tag{23}
$$

则完整最高 action 对全部真实有限平端路径非负：

$$
\boxed{\int L_4^\lambda\,ds\ge0.}
\tag{24}
$$

**证明。** 由 $h_s=hv,h_{ss}=hz$，(21) 的第一项是

$$
\int[a h^{-4}h_{ss}^2+\ell h^{-6}h_s^4]\,ds.
$$

R148 的完整固定 k=0 一维判据准确说明，(22) 当且仅当这部分对全部正平端 h 非负。第二项由 (23) 逐点非负。真实 $\omega$ 由 (4) 给出，所有端势在 (20) 已单独支付，所以 (24) 成立。证毕。

这是一组有限可核的矩阵条件：一个 $4\times4$ 对称矩阵、两个辅助实数，以及两个已有标量不等式。矩阵元素对十个字符值和 $\theta,\eta$ 都是线性的。若后继找到准确有理 $\theta,\eta$ 及有理半正定证书，可以直接核对矩阵等式与全部所需符号；浮点近似半正定不能冒充精确证书。

本稿不声称有理输入总有有理可行辅助参数。边界解若需要更一般的精确表示，必须把其真实精确身份和非负性一同证实。未能恢复准确参数只表示该次证书未完成。

## 5. 与已付必要门的一致性

R165 的两个频率组合为

$$
\beta=2d+g-e-c,\qquad
\gamma=d+g+b+m+c+j.
\tag{25}
$$

对所有 $\theta,\eta$，本 Gram 家族满足

$$
(G_{\theta,\eta})_{11}=d,\quad
(G_{\theta,\eta})_{44}=\gamma,\quad
(G_{\theta,\eta})_{22}-2(G_{\theta,\eta})_{14}=\beta.
\tag{26}
$$

所以 (23) 自动给 $d\ge0,\gamma\ge0$，且由 1、4 主子矩阵

$$
(G_{\theta,\eta})_{14}\le\sqrt{d\gamma},
$$

得到

$$
\beta+2\sqrt{d\gamma}
=(G_{\theta,\eta})_{22}-2(G_{\theta,\eta})_{14}
+2\sqrt{d\gamma}\ge0.
\tag{27}
$$

因此有限充分证书确实蕴含 R165 的全部 log-linear 频率必要门；它没有丢掉那一族真实路径。

再看条件边界 d=0。若 (23) 成立，半正定矩阵的第一个对角元为零，则其第一行列全为零。因此

$$
\tfrac32 f=0,\qquad \tfrac12 c=0,\qquad
\tfrac12(e+\theta)=0.
$$

即 $f=c=0,\theta=-e$；此时第 2 个对角元非负给

$$
g-e\ge0.
\tag{28}
$$

这与 R165 从任意预设 h、高频 k 直接证明的 d=0 **必要**推论完全一致。本稿并不据此令实际 d 为零，也不把 (28) 升为全部 Gram 或全部最高 action 的充要条件。

## 6. 对后继未排外点的准确用途

假设后继必要系统留下一个准确有理外坐标点。其十个最高标量可直接从已发表 head 的原索引 (3) 读取，不需要重算原响应或另做 profile 积分。

如果该点违反 R165 的频率必要门，可用 R165 已付的真实有限截断定向排除。如果该点满足那些必要门，而又能找到本稿的准确 Gram 证书，则最高 action 这一整层已对该组标量获得充分非负证明；下一次检查应针对完整低层、同一乘子或仍未付的真实函数关系。

如果这两个参数的 Gram 可行性没有得到证书，结论仍是**未决**。本稿没有证明该二参数族穷尽一切可令 action 非负的边界势、非多项式证书或积分不等式。因此以下推断均不合法：

- “Gram 不可行，所以存在负 action 路径”；
- “某个 $G_0$ 不半正定，所以字符不正”；
- “(23) 可行，所以整个真实成本字符已正”；
- “一个外坐标点取得最高层证书，所以该点已经是 U 上的良定义泛函”。

原 R140/R164 的完整条件仍包含静态、二次、最高三个时长层及同一个八矩乘子。这里支付的是最高层的一个有限、完整、可独立核验的充分证书，没有忽略这些其余门，也不赋予任何新的 signed control 或 period/ruling 闭合结论。
