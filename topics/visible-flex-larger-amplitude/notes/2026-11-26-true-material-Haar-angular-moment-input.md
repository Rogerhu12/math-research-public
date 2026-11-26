# R691 准确材料 Haar 角矩：可运行的完整积分与冻结接口

**状态：完整解析公式与误差证明，源码已写；尚无本入口的 Actions 科学返回。** 此入口准备一个明确真实场的准确角矩，不替代当前固定深谷 $g_n$ 分支，也不把新目标的有限误差当作原目标下降。

源：`scripts/resume_20261126/material_haar_moments.py`，32690 B，SHA-256

`1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010`。

只做了 AST/compile 和源码数学检查。科学计算仅在公开仓库 Actions；可重算角矩 carrier、积分累加 journal 均留在 runner scratch，公开参数/run/小 summary/SHA。

## 1. 数学目标保持为准确积分

实际 bundle 的全部 core 系数为 $c_j$，$\nu_j=2j$，

$$
\rho=1+\sum_{j=1}^M(1-\nu_j^2)c_j\cos(\nu_j\phi),\qquad
\delta=\Theta-\phi=\sum_{j=1}^M
\frac{(1-\nu_j^2)c_j}{\nu_j}\sin(\nu_j\phi).
$$

角矩定义中的平均始终是

$$
\langle u\rangle=\frac1{2\pi}\int_0^{2\pi}u(\phi)\,d\phi.
$$

同一固定场的完整材料平均为

$$
E_*=\langle \rho_*|F_{*,s}|^2\rangle,\qquad
C_*=\langle |F_{*,\phi}|^2/\rho_*\rangle.
$$

$Q$ 个求积节点和导数阶数 $p$ 是工作精度参数，**不进入准确 angular identity**。提高 $Q$ 或重新算更紧的角矩盒，仍包围上述同一个积分。源码不把求积中点定义成另一个有限均值目标。

输入核对 actual bundle 的完整有限 $q$ 布局、literal affine core/cap、canonical factory 源与 model 维数。完整的冻结 scalar/node/$H$ 身份仍需冻结消费者独立绑定；单独角矩报告明确不声称已完成这个全场冻结。

## 2. 只需有限个准确角矩

R691 的物理移动基为

$$
R_j=\cos(2j\phi)e_r(\phi),\quad
T_j=\sin(2j\phi)e_t(\phi),\quad
Z_j=\cos(2j\phi)e_z.
$$

保留全部 $R_0,\ldots,R_M,T_1,\ldots,T_M,Z_0,\ldots,Z_M$。令 $D_j=\partial_\phi B_j$，定义

$$
P_{ij}=\langle\rho B_i\cdot B_j\rangle,\quad
Q_{ij}=\langle D_i\cdot D_j/\rho\rangle,\quad
\ell_i=\langle D_i\cdot e_t(\Theta)\rangle,\quad
b_i=\langle\rho B_i\cdot e_z\rangle.
$$

准确分部积分给出同一个

$$
\ell_i=\langle\rho B_i\cdot e_r(\Theta)\rangle.
$$

实现只存一份 $\ell$，不以两个不同离散求积数替代这个恒等式。基中的 $e_r,e_t$ 连接项完整保留；例如 $R_0$ 的角导数不为零。

所需 moment 向量是

$$
\gamma_k(w)=\langle w\cos(2k\phi)\rangle,\quad
c_k=\langle\cos\delta\cos(2k\phi)\rangle,\quad
s_k=\langle\sin\delta\sin(2k\phi)\rangle.
$$

$\gamma_0(\rho)=1$、$\gamma_k(\rho)=(1-(2k)^2)c_k^{\rm core}/2$ 对 $1\le k\le M$ 准确成立，其他非零频率为零。数值包围只需：

| 向量 | 指标范围 | 用途 |
|---|---|---|
| $\gamma_k(1/\rho)$ | $0\le k\le2M$ | 全部 $Q$ |
| $\gamma_k(1/\rho^2)$ | $0\le k\le3M$ | 全部 core 方向的 $\delta Q$ |
| $c_k,s_k$ | $0\le k\le2M$ | $\ell$ 及全部 core 方向的 $\delta\ell$ |

记

$$
C_{ij}(w)=\tfrac12(\gamma_{|i-j|}(w)+\gamma_{i+j}(w)),\quad
S_{ij}(w)=\tfrac12(\gamma_{|i-j|}(w)-\gamma_{i+j}(w)).
$$

完整非零块为

$$
P_{RR}=P_{ZZ}=C(\rho),\qquad P_{TT}=S(\rho),
$$

$$
Q_{RR,ij}=\nu_i\nu_jS_{ij}(1/\rho)+C_{ij}(1/\rho),\quad
Q_{TT,ij}=S_{ij}(1/\rho)+\nu_i\nu_jC_{ij}(1/\rho),
$$

$$
Q_{RT,ij}=\nu_iS_{ij}(1/\rho)+\nu_jC_{ij}(1/\rho),\qquad
Q_{ZZ,ij}=\nu_i\nu_jS_{ij}(1/\rho).
$$

其余由对称或零交叉块给出，并有

$$
\ell_{R_j}=c_j+\nu_js_j,\qquad
\ell_{T_j}=\nu_jc_j+s_j,\qquad
\ell_{Z_j}=0,\qquad b_{Z_j}=\gamma_j(\rho).
$$

若 $u=q_s$，$d=h_sH+k_s$，则每个径向点的完整目标只需

$$
E_*=u^TPu+2f_s\ell^Tu+2d\,b^Tu+f_s^2+d^2,\qquad
C_*=q^TQq+2f\ell^Tq+f^2.
$$

不需要在每个新的 $s$ 重做数千角节点的物理场。

## 3. 连续 $\rho$ 正下界与全部求积尾

源码采用 R690 同一 72 位整数向外三角算术，全部 $c_j$ 从实际 binary64 字解释为准确有理数。角节点为准确 $2\pi j/Q$，$\pi$ 使用已包围的 Machin 公式。没有把 libm 或普通 FFT 误差当零。

$\rho$ 为准确偶函数且 $\pi$ 周期，所有所需 integrand 都是偶且 $\pi$ 周期。因此完整 $Q$ 个节点可由 $j=0,\ldots,Q/4$ 的精确 orbit 枚举：两个端点各重数2，内部各重数4，总和准确为 $Q$。这只是相同完整求积的对称计算，不删角域。

令

$$
L_1=\sum_j \nu_j |(1-\nu_j^2)c_j|.
$$

每个真实角到最近完整节点的距离不超过 $\pi/Q$，故

$$
\rho_{\min}\ge\min_j \underline{\rho(\phi_j)}-\frac{\overline\pi}{Q}L_1.
$$

仅当该实际向外下界为正，才计算 reciprocal moments。负/未支付的下界只说明当前工作包围不足，不声称该场几何不可能。

设 $D_k\ge\|\rho^{(k)}\|_\infty$，$\rho\ge r>0$。由 $(\rho/\rho)^{(j)}=0$ 得

$$
A_0=1/r,\qquad
A_j=\frac1r\sum_{k=1}^j{j\choose k}D_k A_{j-k}
\ge\|(1/\rho)^{(j)}\|_\infty.
$$

从乘积公式，

$$
A^{(2)}_j=\sum_{k=0}^j{j\choose k}A_kA_{j-k}
\ge\|(1/\rho^2)^{(j)}\|_\infty.
$$

$\sin\delta,\cos\delta$ 的导数使用完整 Bell 递推：若
$T_k\ge\|\delta^{(k)}\|_\infty$，

$$
B_0=1,\qquad B_j=\sum_{k=1}^j{j-1\choose k-1}T_kB_{j-k}.
$$

所有这些界由**全部**有限 core 模的准确系数求出。

对任意 $2\pi$ 周期 $C^p$ 函数 $v$，$p\ge2$，分部积分给出
$|\widehat v_n|\le\|v^{(p)}\|_\infty/|n|^p$。完整等距求积的第 $n$ 个 Fourier 系数误差恰为 $\sum_{k\ne0}\widehat v_{n+kQ}$，故当 $|n|\le n_0<Q$，

$$
|\text{误差}|
\le \frac{2\zeta(p)\|v^{(p)}\|_\infty}{(Q-n_0)^p}
\le \frac{4\|v^{(p)}\|_\infty}{(Q-n_0)^p}.
$$

最后一步由 $\zeta(p)\le1+1/(p-1)\le2$。实部/虚部得到 cosine/sine moment 的同一误差界。源码分别取物理频率上限 $n_0=4M,6M,4M$，并把上述完整尾加到每个整数求积盒。要求 $Q>6M$。准确 $s_0=0$ 直接置零，来自被积测试函数为零。

## 4. 可实际执行的输入准备

对已决定要研究的真实 frozen 候选输入：

~~~sh
python "$TOPIC/scripts/resume_20261126/material_haar_moments.py" \
  --repo "$REPO" --bundle "$ACTUAL_FROZEN_BUNDLE" \
  --angles 8192 --derivative-order 12 --target-moment-error 1e-14 \
  --admission-seconds 900 --maximum-new-orbits 4096 \
  --moments "$WORK/true-Haar/moments.json" \
  --journal "$WORK/true-Haar/journal.json" \
  --out "$WORK/true-Haar/batch-0001.json"
~~~

这是构造新准确目标的实际输入工作，未附加独立 fixture。它与原 fixed-$g_n$ 分支分开，不把当前深谷目标自动更换为 Haar 平均。

每一个完整 quarter orbit 的四组 moment 累加完成后才能退出；每64个 orbit 和退出时保存 runner journal。只在全部 orbit 完成、总权重等于 $Q$ 时输出完整 moment carrier。下一批读取同一 journal 和新 out 路径。未完成求积不会宣称完整积分已有界。

requested moment error 是实际工作目标。未达到时仍保存真实完整积分盒；进一步提高 $Q$ 或 $p$ 是加紧同一个数学目标的工作精度，不改定义。公开 report/summary 只含实际尺寸、身份、整体宽度、完整尾界与覆盖计数；可重算向量和 journal 不提交。

## 5. 冻结消费者和 moving 设计的不同职责

`MomentKernel` 核完整 source、准确角 identity、实际 carrier、正 $\rho$ 与全部向量维数，提供：

- `interval_blocks()`：全部 $P,Q,\ell,b$ 的向外整数系数；
- `midpoint_matrices()`、`numerical_means(...)`：实际数值工作载体，不冒严格全场证书；
- `enclose_means(q,q_s,f,f_s,d)`：调用方提供完整准确径向系数/标量盒后，支付全部角矩和算术误差的 $E_*,C_*$ 包围；
- `core_direction_vectors(\delta c)`：全部 core 角矩方向变化；不假装调用方的 $\delta q,\delta q_s,\delta H$ 或原自由量 pullback 已完成。

冻结消费者必须将**同一个**实际 $F_*$ 的 q/core/$H$/准确 scalar/节点/eta/source 全部冻结，并在每个新 $s$ 计算其完整连续公式。当前求解场的 core 可以改变，但目标角矩仍用 frozen core，目标不随当前场移动。精化时提高 moment 精度也不能用当前 core 重建另一个目标。

moving 设计则必须增加所有目标导数。对 $a_k=(1-\nu_k^2)c_k$，$\dot a_k=(1-\nu_k^2)\dot c_k$，

$$
\dot\gamma_j(1/\rho)=
-\frac12\sum_k\dot a_k
\left[\gamma_{|j-k|}(1/\rho^2)+\gamma_{j+k}(1/\rho^2)\right].
$$

再以准确 $\dot\Theta=\sum_k(\dot a_k/\nu_k)\sin\nu_k\phi$ 支付 $\dot\ell$。源码使用

$$
A_{ik}=\tfrac12(c_{|i-k|}-c_{i+k}),\quad
B_{ik}=\tfrac12\left(s_{i+k}+\operatorname{sign}(k-i)s_{|k-i|}\right),
$$

$$
\dot\ell_{R_i}=\sum_k\frac{\dot a_k}{\nu_k}(\nu_i A_{ik}-B_{ik}),\qquad
\dot\ell_{T_i}=\sum_k\frac{\dot a_k}{\nu_k}(A_{ik}-\nu_i B_{ik}).
$$

$\dot P,\dot b$ 则由准确有限 $\dot\rho$ 矩给出。这些是 R691 完整 moving mean 微分链的角部分；只有接回所有 $\dot q,\dot q_s,\dot H$、原端口耦合和实际 J/J* 后才能称完整 moving solver。本源明确尚未执行它。

准确材料 Haar 平均支付了 R691 的末端必要相容项，**不证明**任意 frozen 场的 Haar 度量已有非轴对称精确 flex。该入口不会把这个必要条件提升为充分存在性，也不自动满足 README 的幅度、reach、全域误差或加密要求。
