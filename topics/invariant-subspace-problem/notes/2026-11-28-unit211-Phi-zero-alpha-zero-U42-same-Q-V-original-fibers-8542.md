# 真正 $\Phi=0$、$\alpha=0$：$U_{42}$ 全常数域上的同 $Q,V$ 原理想新输入

日期：2026-11-28（Asia/Taipei）。这是已刊 $378$ 权点覆盖之后的新同点目标；不是旧两个结果式或旧规范化检验的复现。

## 1. 已付来源与范围

范围始终是纠错后的原 $\Phi=0$、$D\ne0$ 图及其整个 $\alpha=0$ 支。这里
$$
\delta=1-Q,\quad s=u-1,\quad
L=Q-2(u-1)(u-2),\quad K=Q+4(u-1),\quad
\ell=L/Q,\quad m=u-\ell,\quad\theta=u-L,
$$
$$
M_n=2uL-L^2-u^2Q,\qquad
A=4(u-1)^2-Q,\qquad
\mathcal U=uQ\delta sKLM_nA(uQ-L)\theta .
$$
这些因子在此支的原单位来源见[整个 $\alpha=0$ 的真实首一二次](../results/R150-appendix-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-and-weight-conditions.md)。其中 $m,\theta$ 的支付来自本支的真实 $R$、$t$、$f-u$，不是对一般图的附加假设。

该结果给原奇均值
$$
E_{Bo}=Hq_V,\qquad H=\frac{4u\theta}{M^2},\qquad
q_V=V^2+q_1V+q_0,
$$
以及四条原余式
$$
r_0=E_{Be}\bmod q_V,\quad r_1=N_1\bmod q_V,\quad
r_2=N_S\bmod q_V,\quad r_3=P_S\bmod q_V
$$
都为 $V$ 一次式。全部系数仅有已付权分母。

[同 $Q$ 之前的规范范数与投影](../results/R150-appendix-unit211-Phi-zero-true-alpha-zero-original-norm-Q42-and-378-weights.md) 给四条必要权式 $N,C_N,C_S,C_P$ 及 $U_{42}(u)=0$。$N$ 对 $Q$ 的次数为 $9$，并且其自身前五个 $Q$ 系数有真正 $\mathbb Q[u]$ Bézout 恒等式 $1$；因此任意常数域中 $N$ 不会整条为零。

## 2. 仅再生必要参数定义

唯一运行依赖是：

    2026-11-28-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-8542.py

其完整 SHA256 为：

    58cab31654894e8b4a4309f1c6b69619f5ee19591f74256f3128dd2026a4f025

只读取 results=[] 以前的 $9438$ 字节，前缀 SHA256 为：

    7d6fc9ed844a83daccf3978ed572a4b3a803266875c229fb5d3a42e3a75e751c

新源用 AST 保留该前缀的系数赋值、原 Gram 函数和首一二次算术定义，明确省去旧顶层 assert、say 及三个纯分母检查循环；函数和类内部的算术检查保持原样。旧文件没有改写。这些省去的是已经完成的证明检查，不是绕过本次失败。新输入会打印省去的顶层行号，并逐次独立返回本次新增的整除、Bézout、完整原列组合和正目标。

$N$ 由旧四个规范乘子的实际公内容定义，$C_N,C_S,C_P$ 由已刊交叉式定义。$U_{42}$ 只按既定两个固定结果式的 gcd 及原单位去因子定义再生；不计算旧结果式 Bézout、旧竖直排除或旧原四坐标规范证书。四条件与 $U_{42}$ 均核对已刊 SHA，其中：

    U42 SHA256 a2ad5fc1085bdb07f18030adf2aba55be3165c43aa773f31f71df30ffae03a65

这些再生值仅是新输入参数，不重新登记旧结论。

## 3. 新的同 $Q$ 全域返回

首次完整因式分解
$$
U_{42}=c\prod_\phi \phi^{e_\phi}
$$
并乘回。对每个完整不可约因子取
$$
K_\phi=\mathbb Q[u]/(\phi).
$$
不选择某一个复嵌入。每次 $K_\phi$ 逆都由完整 $\mathbb Q[u]$ Bézout 及双向乘回确认。

在 $K_\phi[Q]$ 中计算新的
$$
g=\gcd(N,C_N,C_S,C_P),
$$
每步保留四原输入的真实 Bézout 组合并完整乘回。若 $g=1$，该整个常数纤维已被原条件排除。

若 $g$ 非常数，只移除与原 $\mathcal U$ 共同的完整主因子：反复取 $c_i=\gcd(g_i,\mathcal U)$，并实际返回 $g_i=c_i g_{i+1}$。移去的乘积除尽某个 $\mathcal U$ 正幂，故其所有点都不在原单位图内。保留 $g_{\rm good}$ 的全部重数，并实际返回
$$
\gcd(g_{\rm good},\mathcal U)=1.
$$
任何意外非单位都保留整个原 $\phi$，不选择一个分量继续宣称全域成功。

## 4. 新的完整同 $Q,V$ 原理想

若 $d_Q=\deg g_{\rm good}>0$，定义真正多项式代数
$$
B_\phi=
\left(K_\phi[Q]/(g_{\rm good})\right)[V]/(q_V).
$$
它在 $K_\phi$ 上有基
$$
Q^j,\ VQ^j,\qquad 0\le j<d_Q,
$$
维数 $2d_Q\le18$。$Q$ 商不假设是域或约化代数；原分母只在整个商中用 Bézout 确认逆。$V$ 乘法以真实首一 $q_V$ 逐次约化并完整返回两坐标。

四个原 $r_i$ 乘以上述全部 $2d_Q$ 基，给 $2d_Q$ 行、$8d_Q$ 列矩阵。这是整个原理想作为 $K_\phi$ 线性空间的矩阵，已经包含全体基倍；不是仅把一个次数容器冒称完整代数。高斯消元只选择原列，并保存各阶梯列的原组合，逐次检查全部 $2d_Q$ 坐标。

先尝试真正目标 $1$。若未返，使用同一个原点的
$$
D_{\rm val}=\ell(2\lambda^2-2\lambda+1)-T^2
          =bc(h-k)^2,
$$
其中 $\lambda,T$ 是本支已刊的 $V$ 仿射恢复式。只尝试 $D_{\rm val}$ 的正幂，不倒 $D_{\rm val}$ 或其范数。若原理想商的剩余 $K_\phi$ 维数为 $r$，只需试 $1\le n\le r$；只有某次完整原列组合实际返回 $D_{\rm val}^n$ 才判当前物理 $D\ne0$ 纤维排除。未返就保留，不把泛域秩或期望的幂零性当结论。

$u$ 因子的所有复嵌入均保留。若需要把已返物理单位结论表述到 $\phi^{e_\phi}$，可在原单位局部化中用幂零理想 $(\phi)$ 提升：模 $\phi$ 的单位恒等式提升成 $1+\phi r$，其有限几何级数给逆。源输出的点数不把这种提升偷换为精确方案长度。

## 5. 可登记结论的边界

每个完整因子独立输出实际同 $Q$ 次数、原列秩、余商维数、完整目标返回和所有未付范围。如果剩余维数为 $r$，其不同 $(u,Q,V)$ 点至多 $(\deg\phi)r$，不同权对至多 $(\deg\phi)\min(d_Q,r)$。已刊原恢复只再需要 $\rho^2=1-Q$，故完整固定规范点至多 $2(\deg\phi)r$。这是点数上界，不是精确长度。

所有因子只有在实际单位或正 $D$ 目标全返之后，才能合成整个 $\alpha=0$ 排除。尚未运行，当前仍只有已刊的 $378/1512$ 上界；不预报排空或整个 $\Phi$ 关闭。

## 6. 首次执行身份

新源：

    2026-11-28-unit211-Phi-zero-alpha-zero-U42-same-Q-V-original-fibers-8542.py

SHA256：

    610fec2409090215538d62bf9f701b399ac2dcf72b9f2d6760319d1eb4f4168e

总上限 $120$ 秒、内存 $1$ GiB，外层 $135$ 秒。所有嵌套 alarm 都钳制到最初绝对截止时刻，包括传入 $0$。每个完成因子立即打印小回执；不保存或传输系数载荷。没有重新启动旧 B 大矩阵、旧 $\alpha$ pair 或已冻结的错误紧凑式门。
