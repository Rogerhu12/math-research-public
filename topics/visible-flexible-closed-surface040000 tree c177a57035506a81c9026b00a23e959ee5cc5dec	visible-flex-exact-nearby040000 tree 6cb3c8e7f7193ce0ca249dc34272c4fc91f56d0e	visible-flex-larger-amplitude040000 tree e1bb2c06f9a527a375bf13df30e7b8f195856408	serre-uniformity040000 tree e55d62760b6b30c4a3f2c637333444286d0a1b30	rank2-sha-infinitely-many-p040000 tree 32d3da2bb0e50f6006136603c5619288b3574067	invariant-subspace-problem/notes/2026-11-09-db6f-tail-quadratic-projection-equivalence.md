# 显式低阶三角投影与原有限 N 实数方程的等价性

状态：**本文给出完整代数证明及精确系数核查；待独立全文审查。备选数值算法尚未实施，也未运行新 solver。** `/root/coupled_prefix` 提出剥离低阶项的候选，`/root/tail_theory` 整理证明，2026-11-09。

研究目的仅是判断：在原有限 Fourier/角求积方程中，能否将已经是有限三角多项式的部分改为显式系数投影，而其余非多项式部分仍用原 N 个角点。结论是可以，条件、归一化及不变范围如下。**这不是当前 Newton 阻尼的舍入归因，也不是任何新候选的求解成功。**

## 1. 冻结模型和记号

所核源文件在 `repro/source-root/topics/large-amplitude-twist-flex/scripts/`：

| 源文件 | SHA256 |
|---|---|
| `general_root_tail_momentum.mjs` | `182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c` |
| `f6tail_momentum_split_flux.mjs` | `5d77ca058adb634547c91998002eeffb9de5395a9e1e130f7edd4fa65014f578` |
| `f6tail_fast_split_flux_engine.mjs` | `a1c84ba25846f0bf6e9d35092dbc0281d01f60f3d68700dfad20fd598e27e4b6` |
| `f6tail_fast_momentum.mjs` | `3e3e619f255d104e5f86761346f536d722d1de07f40f7cef73161caba8d6793e` |

令 spacing 为正整数 $\kappa$，$m_j=\kappa j$，采用源的正交归一基

$$
c_0=1,\qquad c_j(\theta)=\sqrt2\cos(m_j\theta),\qquad
s_j(\theta)=\sqrt2\sin(m_j\theta),\quad 1\le j\le M.
$$

这里的模型使用精确等距角点 $\theta_n=2\pi n/N$、精确三角函数及实数算术。记 $\langle f\rangle_N=N^{-1}\sum_n f(\theta_n)$。本文最后专门区分这个模型与保存为 binary64 的 `cs/sn` 表。

固定一个径向点，将源 `g.w2` 记为 $v>0$，令 $E=1+v$。定义

$$
P=\sum_{j=1}^M p_j s_j,\quad
P_\theta=\sum_{j=1}^M m_jp_jc_j,\quad
L=L_0+\sum_{j=1}^M L_jc_j,
$$

$$
K=L-P_\theta,\quad T=2K+K^2+EP^2,\quad
u=vT,\quad D=1-u,\quad S=1-vP^2,\quad
A=1+L+vP_\theta.
$$

另设 $d=\sqrt D>0$，以及奇三角多项式

$$
U=\sum_{j=1}^M u_js_j,\qquad
u_j=-m_jL_j+(m_j^2-1)p_j.
$$

所有恒等式均在原 guard $D,S,A>f>0$ 上使用。把 `g.w2` 作为固定系数 $v$ 后，不需要假设浮点 `exp(2logw)` 与 `exp(logw)**2` 逐位相等。

## 2. 点态恒等式

原代码计算

$$
f_c=\frac{u(2+d)}{2d(1+d)^2},\qquad
g_c=\frac{v\{P^2+ST/(1+d)\}}{Sd},
$$

$$
q=\frac{K^2+EP^2}{2}+KP_\theta
  +Tf_c+(1+K)P_\theta g_c.
$$

### 2.1 二次 moment 项

由于 $K=L-P_\theta$，直接展开得

$$
\frac{K^2}{2}+KP_\theta
=\frac{L^2-P_\theta^2}{2}.
$$

所以

$$
q=q_2+R_q,\qquad
q_2=\frac{L^2+EP^2-P_\theta^2}{2},\qquad
R_q=Tf_c+(1+K)P_\theta g_c. \tag{1}
$$

$q_2$ 是最高谐波编号至多 $2M$ 的偶三角多项式。$R_q$ 一般不是有限三角多项式，不对它使用截断卷积代替原角求和。

### 2.2 Jacobian 中的一次多项式

由 $u=1-d^2$ 可得

$$
\frac12+f_c=\frac1{d(1+d)},\qquad
1+g_c=\frac1{Sd}. \tag{2}
$$

第二式的分子验证为

$$
vP^2+\frac{Su}{1+d}
=vP^2+S(1-d)=1-Sd.
$$

结合 $L-K=P_\theta$，原点态 moment $F=L+q$ 可写成

$$
F=\frac{d^{-1}-1}{v}+\frac{(1+K)P_\theta}{Sd}. \tag{3}
$$

对 $L$ 求导时 $P,P_\theta,S$ 固定，$D_L=-2v(1+K)$。同时

$$
D+v(1+K)^2=ES.
$$

故

$$
\partial_LF
=\frac{1+K}{D^{3/2}}+
 \frac{P_\theta\{D+v(1+K)^2\}}{SD^{3/2}}
=\frac{A}{D^{3/2}}. \tag{4}
$$

原代码令 $a_m=L+vP_\theta$，计算

$$
b_m=a_m+(1+a_m)\operatorname{expm1}\!\left(-\frac32\log1p(-u)\right).
$$

在实数模型中，`expm1` 这一项等于 $D^{-3/2}-1$，所以

$$
b_m=L+R_B,\qquad
R_B=vP_\theta+A\operatorname{expm1}\!\left(-\frac32\log1p(-u)\right). \tag{5}
$$

这同时是 (1) 的导数分解：$\partial_Lq_2=L$，由 (4) 得 $\partial_LR_q=R_B$。因此 moment 和 Jacobian 的相应剥离保持同一实数导数关系。

### 2.3 split flux 的二次部分

现有 split 引擎已将原 flux 的线性项 $U$ 单独投影，其余点态因子是

$$
\text{factor}=\frac{K+u/(1+d)+vP^2d}{Sd}.
$$

利用 $u/(1+d)=1-d$，分子是 $K+1-Sd$，故

$$
\text{factor}=\frac{1+K}{Sd}-1
=K+(1+K)g_c. \tag{6}
$$

完整原 flux 与现有非线性余项分别为

$$
\frac{(1+K)U}{Sd}
=U+UK+U(1+K)g_c, \qquad
U\,\text{factor}=UK+U(1+K)g_c. \tag{7}
$$

$UK$ 是最高谐波编号至多 $2M$ 的奇三角多项式。剩余 $U(1+K)g_c$ 仍保留原 N 点求和。

## 3. 有限 N 的无混叠门

设

$$
N_* = \frac{N}{\gcd(N,\kappa)}.
$$

等比求和给出，对任意整数 $h$，

$$
\left\langle e^{i\kappa h\theta}\right\rangle_N
=\begin{cases}1,&N_*\mid h,\\0,&N_*\nmid h.\end{cases} \tag{8}
$$

因此任意谐波编号范围 $|h|\le d<N_*$ 的三角多项式，其离散平均等于连续平均。

本候选需要的最高编号如下：

| 被精确投影的项 | 自身次数 | 乘测试基后的最大次数 |
|---|---:|---:|
| $q_2c_i$，$0\le i\le M$ | $q_2$ 至多 $2M$ | $3M$ |
| $Lc_ic_j$，$0\le i,j\le M$ | $L$ 至多 $M$ | $3M$ |
| $UKs_j$，$1\le j\le M$ | $UK$ 至多 $2M$ | $3M$ |

所以充分条件为

$$
N_*>3M. \tag{9}
$$

原 engine 已强制 $N>4M\kappa$。因为 $\gcd(N,\kappa)\le\kappa$，原门严格蕴含 (9)，无须更改实际 N。当前 M15、spacing3、N256 有 $N_*=256>45$。

严格大于号不能普遍改为大于等于。若 $N_*=3M$，则 $c_M^3$ 的连续平均为 0，但离散平均为 $\sqrt2/2$，因为 $\cos^3 x=(3\cos x+\cos3x)/4$ 的最高项发生 alias。

若 (9) 不成立，可以研究按模 $N_*$ 累加的循环卷积，但那是另一个需要显式核对的公式；不得直接将无混叠连续投影公式套上。本文既不降低现有 N，也不改变原 engine 的参数校验。

## 4. 归一化后的显式系数

### 4.1 $q_2$ 的卷积

令 $z=e^{i\kappa\theta}$，用 Laurent 系数记函数。正交归一基要求

$$
\widehat L_0=L_0,\quad \widehat L_{\pm j}=L_j/\sqrt2,
\quad \widehat P_{\pm j}=\mp i p_j/\sqrt2,
$$

$$
\widehat{P_\theta}_{\pm j}=m_jp_j/\sqrt2.
$$

以 $*$ 表示通常的有限系数卷积，则

$$
\widehat{q_2}
=\frac12\left(\widehat L*\widehat L
 +E\widehat P*\widehat P
 -\widehat{P_\theta}*\widehat{P_\theta}\right). \tag{10}
$$

在 (9) 下，其离散投影就是

$$
\langle q_2c_0\rangle_N=\widehat{q_2}_0,
\qquad
\langle q_2c_j\rangle_N=\sqrt2\widehat{q_2}_j
\quad (j>0). \tag{11}
$$

不能把输入的 $L_j,p_j$ 当作未经归一化的普通 cosine/sine 系数，或省略输出的 $\sqrt2$。

### 4.2 Jacobian 的显式矩阵

定义 $B^L_{ij}=\langle Lc_ic_j\rangle_N$，将超出 $[1,M]$ 的 $L_k$ 置零。由 $c_ic_j$ 的乘积恒等式及 (9)，

$$
B^L_{00}=L_0,\qquad B^L_{0j}=B^L_{j0}=L_j \quad(j>0),
$$

$$
B^L_{ii}=L_0+\frac{L_{2i}}{\sqrt2}\quad(i>0),
$$

$$
B^L_{ij}=\frac{L_{i+j}+L_{|i-j|}}{\sqrt2}
\quad(i,j>0,\ i\ne j). \tag{12}
$$

原 Jacobian 可写为

$$
B_{ij}=\delta_{ij}+B^L_{ij}+\langle R_Bc_ic_j\rangle_N. \tag{13}
$$

这与原代码先置单位矩阵再累加 $b_mc_ic_j$ 完全相同。由于 (9) 也支付基的离散正交性，(13) 与 (4) 的有限 N 投影 Jacobian 一致。本文选择只剥离 $L$；虽然 $vP_\theta$ 也可同样解析投影，当前候选不需要额外扩大修改范围。

### 4.3 $UK$ 的显式 sine 系数

令 $k_0=L_0$、$k_\ell=L_\ell-m_\ell p_\ell$。对 $1\le j\le M$，

$$
\langle UKs_j\rangle_N
=k_0u_j+\frac1{\sqrt2}\sum_{k=1}^M\sum_{\ell=1}^M
u_kk_\ell\left[
\mathbf1_{j=k+\ell}
 +\operatorname{sgn}(k-\ell)\mathbf1_{j=|k-\ell|}
\right]. \tag{14}
$$

这里 $\operatorname{sgn}(0)=0$。它来自

$$
s_kc_\ell=\frac1{\sqrt2}
\left(s_{k+\ell}+\operatorname{sgn}(k-\ell)s_{|k-\ell|}\right).
$$

最外层原 RHS 的 `pref*frequency[j]` 仍在原位置；(14) 没有额外乘除 $m_j,r,w$。

## 5. 原有限 N 方程究竟保持什么

结合 (1)、(5)、(7) 和 (9)，三个被替换的投影在精确实数有限 N 模型中相等。其余部分仍用相同 N、相同角点、相同点态表达式求和。因此这不改变实数 moment 方程、其 Jacobian 或实数 split RHS。

若以后另建候选实现，以下范围须保持并审查：

1. 每个角点的 $P,P_\theta,L,K,U,D,S,A,d$ 和原 guard 仍按原定义计算，不跳过危险角点，不修改 floor。
2. `rows.quad` 仍保存完整点态 $q$，`maxQuad` 仍是完整 $q$ 的最大绝对值。它们用于原 root 停止尺度及 fast Jacobian 的其他公式，不得改为仅存 $R_q$。可以保留原点态 $q$ 的计算行，只改变 moment 的累加分解。
3. 原 root、Newton 接受规则、容差、初猜、RK 以及物理 profile 都保持。卷积并不支付任何本来未过的残差门。
4. fast Jacobian 的原实数导数式仍是同一 RHS 的导数；但必须显式绑定派生 base 的 import。只替换公开对象上的函数名，不保证改变内部闭包调用。state-only 和 variational 路径需要独立数值一致性检查。
5. 非多项式余项的原 N 点 alias 并未消失。本结论只避免对已经可精确有限投影的低阶项再次做角求和，不能把整套非线性投影称作连续角积分。

### binary64 的必要区别

原代码的角点、`Math.sin/cos`、`Math.sqrt(2)` 和累加都带舍入。若把这些已舍入表项本身视作精确任意常数，有限矩阵未必严格正交，(8) 也不再是这些常数表的恒等式。所以替换后的程序**不承诺与原程序逐位相同**，其数值输出变化属于一种等价实数模型的浮点评估变化。

显式卷积本身若用 binary64，也仍有乘加舍入，不能称为严格区间认证或无误差计算。它可能减少低阶大项投向高模时的角求和消去，但该收益、实际误差和对 shooting 条件数的影响都需要另行量测。本证明没有把现有 M15 阻尼归因于舍入，也没有证明这种候选一定改善求解。

## 6. 精确独立核查脚本

`scripts/db6f-tail-quadratic-projection-equivalence.py`，SHA `5e13055cfdfb23caa996ae926c6b312fd45b0e4b7263a13dfe914a30fcc22c1b`，实际运行退出码 0，耗时约 1.21 秒。输出 `notes/2026-11-09-db6f-tail-quadratic-projection-equivalence.json`，SHA `61ae039718391a04f6237b028bcaec291899869c3e154bd69470d05d820d297c`。

脚本不依赖三角库的数值求值：用有理多变量多项式清分母验证七个恒等式；用有理复 Laurent 系数与显式 $a+b\sqrt2$ 形式验证 M15 的全部 4096 个 $c_ic_jc_k$、3600 个 $s_js_kc_\ell$ 的连续/离散投影，以及 $N_*=3M$ 的 alias 反例。它没有实现候选 momentum engine，没有求解任何尾，也没有修改冻结源。

因此现在可采用的结论只有：**所列规范化公式在明确的原有限 N 实数模型上严格等价，当前角网格满足条件。** 是否值得实施及任何实施后的数值结论，仍须与正在运行的 continuation 分开保存和审查。
