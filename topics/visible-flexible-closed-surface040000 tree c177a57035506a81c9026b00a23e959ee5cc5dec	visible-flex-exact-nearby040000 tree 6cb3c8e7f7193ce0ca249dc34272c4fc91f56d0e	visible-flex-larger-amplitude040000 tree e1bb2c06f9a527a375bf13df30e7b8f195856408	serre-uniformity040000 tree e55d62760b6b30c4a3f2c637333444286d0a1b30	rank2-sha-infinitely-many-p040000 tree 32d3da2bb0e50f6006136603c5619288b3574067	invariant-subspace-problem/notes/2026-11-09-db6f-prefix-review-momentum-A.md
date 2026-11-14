# 独审：有限 momentum 图的 A、Jacobian 与可行域

审稿人：`/root/coupled_prefix`，2026-11-09。状态：**所列实数模型公式及条件推论通过独立核对；不是新候选正分支证书，也不是浮点 Newton 认证。**

## 冻结对象与范围

审查 `2026-11-09-db6f-tail-momentum-A-meaning.md` 全文六节，SHA256：

`6cb920269b5d269fb818a11d6604d2201b665de4d500a752257f61b6a34408d5`。

对照本题冻结依赖：

- `repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs`，SHA256 `182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c`；
- 同目录 `f6tail_momentum_physical_jets.mjs`，SHA256 `2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8`。

此次未更改作者代码或稿件，未运行新的候选求解。作者在较早草稿审查后补入了我建议的点态 moment 求导和实数模型舍入范围；以下是对补全后证明的独立逐式复核，不是未参与任何讨论的全流程独立认证。

## 1. 点态恒等式及 Gram 矩阵

直接代入 $k=L-P_\theta$、$E=1+w^2$ 得

$$
D=ES-w^2(1+k)^2,\qquad A=1+k+EP_\theta.
$$

源码频率为整数 $m_j=j\,\mathrm{spacing}$，且要求 $N>4M\,\mathrm{spacing}$。因此所需二阶乘积频率均严格小于 $N$；在精确三角算术下，$c_0=1$、$c_j=\sqrt2\cos(m_j\theta)$ 的离散 Gram 为单位矩阵。源码初始化的 $I$ 与增量 $AD^{-3/2}-1$ 正好合成

$$
B=\frac1N\sum_\ell A_\ell D_\ell^{-3/2}c_\ell c_\ell^{\mathsf T}.
$$

这个结论不要求 $AD^{-3/2}-1$ 为正。只须节点上的 $A>0,D>0$，整个加权 Gram 即正定。稿中 (3) 的最小本征值下界正确。

## 2. 它确实是 moment Jacobian

独立从源码的 $q,f_c,g_c$ 化简，而非仅辨认 Newton 矩阵外形。令 $s=\sqrt D$，有

$$
\tfrac12+f_c=\frac1{s(1+s)},\qquad 1+g_c=\frac1{Ss}.
$$

源码 $T=2k+k^2+EP^2=(1-D)/w^2$。于是

$$
L+q=T\left(\tfrac12+f_c\right)
+(1+k)P_\theta(1+g_c)
=\frac{s^{-1}-1}{w^2}+\frac{(1+k)P_\theta}{Ss}.
$$

固定 $Q,r,w$ 时，$P,P_\theta,S$ 均不随 $L$ 变。逐项微分并用 $D+w^2(1+k)^2=ES$，得到

$$
\partial_L(L+q)
=\frac{1+k}{D^{3/2}}
+\frac{P_\theta[D+w^2(1+k)^2]}{SD^{3/2}}
=\frac{A}{D^{3/2}}.
$$

离散 Fourier 投影的链式法则因此给出上述 $B$。这一补充完整支付后文沿线段积分 Jacobian 的单调性步骤。

## 3. 法曲率与高频尺度

在稿件明确列出的精确等距高度函数假设下，目标度量 $g=E\,dr^2+r^2d\theta^2$ 的单位角向 Hessian 为

$$
\nabla_g^2u(e_\theta,e_\theta)
=\frac{u_{\theta\theta}}{r^2}+\frac{u_r}{Er}
=\frac{w}{Er}(EP_\theta+1+k).
$$

所选上向法线满足 $n_z=\sqrt{D/E}$，从而

$$
\mathrm{II}(e_\theta,e_\theta)=\frac{wA}{r\sqrt E\sqrt D}.
$$

符号和 $E$、$r$ 因子均正确。固定其他正界时 $A\downarrow0$ 使该方向法曲率趋零；它本身不是第一基本形式退化或曲率上界发散的证明。有限 Galerkin 源的形式二阶量与实际 XYZ 图须继续分别检验，稿件保留了这一限制。

由 $P=u_\theta/(rw)$，单个 $h_m\cos(m\theta)$ 确实给出 $P_{\theta,m}=-m^2h_m\cos(m\theta)/(rw)$。因此小高度高频项在谷内可显著影响 $A$；这只解释灵敏度，不能证明某次迭代的具体失败原因。

## 4. 可行凸域、唯一性及初猜 guard

固定 $Q,r,w$、先检查各角节点 $S>f>0$ 后，$D>f$ 对 $L$ 系数给出两个开半空间，$A>f$ 给出一个开半空间。有限交为凸域，允许为空。在此域内 $D\le E$，故 $B\succeq fE^{-3/2}I$。沿任意两点间线段积分得到稿中强单调不等式；因而同一原 moment 方程在此域内至多有一个 root。推导没有把“至多一个”扩大为存在性。

源码 `root(state,profile,x,guess)` 确实默认 `L=target`，且第一次 `evaluateL` 在任何 Newton 更新之前执行 D/S/A guard。因而初猜被拒绝与真实可行 root 不存在是不同命题。重用候选初猜仍需在新参数下重新检验；若 $S\le f$，只换 $L$ 无法修复。稿件没有改变 floor、原方程或实际运行中的算法。

## 5. 已有 segment4 定位的边界

该节的代码解释与我已保存的 `2026-11-09-db6f-prefix-tail-positive-branch-interpretation.md` 相符：raw0/segment4 的 $x=1/4$ 是 p8 的 shooting 分点，不是 raw-cell 缩放接口；常数 valley、warp、cap 参数不产生 segment5 式径向驻点。现有 depth2 primitive 该段的 16 叶均为 analytic、0 叶为 range。这里不把已有离散最低 A 点提升为连续最小值认证，也不排除一般 RK/角积分/条件数误差。

## 结论与保留缺口

**PASS：** (1)–(5)、点态 moment Jacobian、凸可行域、条件唯一性、初猜 guard 的代码解读，以及已存 segment4 数据的有限范围解释均成立。暂无必须修改的数学步骤。

该审查不支付双精度 `exp(2*logw)` 与 `exp(logw)**2` 的差、三角表与累加舍入、候选连续 $A>0$、实际 XYZ 等距/曲率、全局 Newton 收敛或任何无限尾存在性。原稿已明确实数模型及这些范围；不据此放宽当前数值正支路保护阈值。
