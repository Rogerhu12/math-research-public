# R128 多参数平坦尾：准确函数、全部端口导数及实际检查

这是 R128 显式尾的函数参数化入口，不改变已经冻结的单参数 provider。没有运行新的前缀 BVP，没有将非平旧尾的数值响应转移到此新物理度量。

## 准确定义

参数顺序为 `coefficients=[A,b0,...,b(K-1)]`，总数为 `K+1`。令

\[
q=(|y|-c)/(a-c),\quad B_j(q)=1024q^5(1-q)^5T_j(2q-1)\quad(0<q<1),
\]

并将每个 \(B_j\) 在区间外定义为零。\(S_9\) 是 R128 的夹断九次 smoothstep。

\[
\alpha(y)=\operatorname{sgn}(y)
\left[A S_9(q)+\sum_{j=0}^{K-1}b_j B_j(q)\right].
\]

所有泡函数及其前四阶导数在两端为零，故 \(\alpha\in C^4\)，生成曲线至少 \(C^5\)。对所有有限参数向量，令
\[
Y(y)=\int_0^y\cos\alpha(v)dv,\qquad
W(y)=\int_0^y\sin\alpha(v)dv,
\]
则
\[
F(r,u)=(r\cos u,Y(r\sin u),Z_c-W(r\sin u))
\]
仍准确满足共同 \(dr^2+r^2du^2\)，且整个 \(r\le c\) 领圈逐材料点固定。\(\alpha\) 变号或曲率变号不破坏此度量恒等式；是否保持嵌入及具体几何预算是另外的实际条件，代码不删参数、不截角、不以布尔筛查替换曲面。

所有参数共用同一个材料 \(u\)、同一个 \(q(y)\)。参数 JVP 无隐藏的坐标重标项。新输入若在固定图册 \(u=U(\xi)\) 取样，\(l,m,n\) 只复合 \(U\)，不能乘 \(U_\xi\)；其 \(\xi\) 导数才乘 \(U_\xi\)。

## 导数与接口

源码：`scripts/fd2d_flat_developable_family.py`，SHA256
`c2d2afb3ed558f50aef20629b323c7bc1475561e5d2c2d8e105260d2b0ebb2eb`。

```python
from fd2d_flat_developable_family import FlatDevelopableFamily
family = FlatDevelopableFamily(
    coefficients, cut_radius=.8, flat_radius=.34,
    cuff_radius=.32, plane_height=1.25)
q = family.curve(y)
cut = family.cut_port(u, position_jets=False)  # 只算准确形状/导数，无位置求积
full = family.cut_port(u)                     # 完整 Cartesian 两jet/Jac
directional = family.jvp(r, u, direction)
```

`curve(y)` 返回 `alpha,kappa,kappa_y`，其中 \(\kappa=\alpha_y\)、\(\kappa_y=\alpha_{yy}\)，以及这三个字段各自的 `*_jacobian`，最后一维严格按参数顺序。它还给生成曲线 `X=Y,Z=W` 和全部位置 Jacobian。`curve(y,integrate=False)` 或 `angle_jets(y)` 不做任何积分。

`cut_port` 和一般的 `evaluate(r,u)` 给：

- 准确 `l,m,n` 及 `l_u,m_u,n_u,l_s,m_s,n_s`；
- 每项对应的 `*_jacobian`，最后一维为参数；
- 默认还给 `X,X_r,X_u,X_rr,X_ru,X_uu,X_s,X_ss,X_su,e1,e2,N` 及全部 Jacobian；向量 Jacobian 的最后两维为 `(3,K+1)`；
- `gc_values=[n,m,X,e1,e2,N]` 与末维为参数的 `gc_values_jacobian`；
- `height_jet` 的 `H,Hr,Hu,Hrr,Hru,Huu`，及同结构 `height_jet_jacobian`。

这里始终 \(s=a-r\)，所以 \(r_s=-1\)，上半内向法向 \(N=e_1\times e_2\) 满足 \(N_z=-\cos\alpha\)。令 \(p=\sin u,q_0=\cos u\)，准确的形状导数为
\[
\begin{aligned}
l_s&=-\kappa_y p^3,&m_s&=\kappa_y p^2q_0,&n_s&=-\kappa_y p q_0^2,\\
l_u&=r\kappa_y q_0p^2+2\kappa pq_0,\\
m_u&=-r\kappa_y pq_0^2-\kappa(q_0^2-p^2),\\
n_u&=r\kappa_y q_0^3-2\kappa pq_0.
\end{aligned}
\]
因此 \(K=0,c=-1/r\) 的两条 Codazzi 恒等式准确相消。\(\kappa\) 对全部参数线性，故 \(l,m,n\) 及其一导也对参数线性；位置和标架保留真实非线性三角函数。

完整两阶端口匹配只要求实际曲面 \(C^2\)。上述可选 `l_s` 不应自动增加为必须匹配的 \(C^3\) 接合条件，尤其在旋转参考 \(n\sim\tau^2,l\sim\tau\) 接到平尾的角弧上。

## 表示与计算

Chebyshev 递推同时给 \(T_j(2q-1)\) 的 \(q\) 一、二导，不以有限差分代替。位置用 Gauss–Legendre 原函数；默认阶数 `max(96,K+32)`，可独立加密。所有位置积分按 32 个 \(y\) 点分块，源码没有无界点缓存。`position_jets=False` 的边界路径完全不调用 Gauss–Legendre。

严格数学定义始终是上面的连续积分。固定求积数给它的数值代表，最终实际图的误差仍应随求积或角/径向离散化加密检查；不因源码提供公式就把有限数组声明为精确数。

`plane_height` 只平移位置的竖直分量，不改变形状端口。若前缀先解形状后作刚体对齐，其实际 cuff 高度必须由重建确定并满足帽预算，不能把构造函数默认值 1.25 当成真实前缀已经达到的高度。

## 可用的解析充分界

在 \([0,1]\) 上 \(|B_j|\le1\)。记 \(p_0=1024q^5(1-q)^5\)，则
\[
\max |p_0'|={81920\over19683},\qquad
|\partial_q T_j(2q-1)|\le2j^2.
\]
第二式由 \(T_j'(x)=jU_{j-1}(x)\) 及
\(|\sin(j\theta)|\le j|\sin\theta|\) 得到，两端取连续极限。因此
\[
|\alpha|\le |A|+\sum|b_j|,
\quad
|\kappa|\le {1\over a-c}
\left[{315\over128}|A|+\sum|b_j|\left({81920\over19683}+2j^2\right)\right].
\]
若前者严格小于 \(\pi/2\)，水平投影严格单调，R128 的全片嵌入证明适用。

更具体地，在 \(0<q<1\)，
\[
\left|{B_j'\over S_9'}\right|
\le {512\over63}+{256\over315}j^2.
\]
所以
\[
A\ge\sum|b_j|\left({512\over63}+{256\over315}j^2\right)
\]
是全域 \(\kappa\ge0\) 的一个充分条件。若它成立，则 \(0\le\alpha(y)\le A\) 对 \(y\ge0\) 成立，
可用更紧的角界 \(|\alpha|\le A\)，并保留 R128 的正支撑证明及其球包。
这只是一个可计算的充分窗，不满足它不表示实际曲率必变号；模块如实返回 `sufficient_bounds()`，不据此中止求解。

原单参的 \(\max Z\le AL/2\) 不能直接照搬到有泡函数的族。由
\(\int_0^1p_0=256/693\)，可用准确通用界
\[
|W(y)|\le (a-c)\left({|A|\over2}+{256\over693}\sum|b_j|\right),
\qquad |y|\le a.
\]
若曲率非负，则 \(W\ge0\)，后者给实际高度和 held 的保守预算。更紧窗口应使用真实系数的连续积分包围。

## 实际检查与范围

`fd2d-flat-developable-family-check.py` 已自然退出 0：session 5836，启动 chunk `8d2924`，结束 `f3c425`，3.545 秒。实际输入有 47 个泡函数和 48 个完整参数，未只检查首列。

- 与已冻结单参源相比，零泡位置/完整两阶向量逐位一致；形状重排差至多 \(4.45\times10^{-16}\)。
- 独立 Clenshaw/库 Chebyshev 微分核与显式递推的组合二导差至多 \(4.92\times10^{-17}\)。
- 19 径向点、256 材料角的真 Codazzi 残差至多 \(4.56\times10^{-15}\)，Gauss 残差至多 \(1.78\times10^{-15}\)。全部 48 个解析方向的相消误差至多 \(6.40\times10^{-12}\)；高阶导数列自身量级较大。
- 实际位置两jet给 metric 差至多 \(6.67\times10^{-16}\)，II 差至多 \(4.45\times10^{-16}\)。固定 collar 的全部参数 Jacobian 准确返回零。
- 全参数方向差分的非线性位置/标架/两jet误差随步长减半约缩小四倍；\(\kappa_y\) 的空间方向及全列差分同样呈二阶缩小。
- 64/96/128 相对 192 阶求积的全部位置 Jacobian 差至多 \(2.25\times10^{-15}\)。48 阶的高列差约 \(1.84\times10^{-12}\)，报告保留这项实际加密差。
- 128 角、48 参数的 shape-only 边界调用中位约 1.50 毫秒；整个检查峰 RSS 为 103,768 KiB。这是性能读数，不是系统资源保证。

报告还包含一个真实曲率变号但投影仍正的参数例，确认模块没有把这种合法等距图暗中裁剪成凸分支。所有数值检查的范围均在报告中标明；没有从这些有限点核验宣称新的强目标闭核完成。
