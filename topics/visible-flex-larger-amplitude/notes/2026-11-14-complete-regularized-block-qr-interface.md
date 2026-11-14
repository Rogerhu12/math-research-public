# 完整正则模型的分块平方根 QR：接口与费用

日期：2026-11-14。本文是源码和代数设计；没有运行新的 QR、线性模型或科学计算。动机是 actual30 的完整 $H$ 内层 PCG 未达到其原残差精度，而不是已经证明 QR 能解决后续非线性域问题。actual36 属于不同的 native 块系统，本接口不混用它的 Jacobian。

## 1. 固定对象与现有入口

使用同一次 `CompleteLinearization` 已产生的 `L/R/P/BY/BC/BP`、`chart.inlet`、`chart.scale` 及该模型固定的行权重 $W_r$。不再次调用 `flow.jac`，不重新计算 RHS 或边界，不改变原数学方程。所读源为：

| 源 | SHA-256 |
|---|---|
| `geometry_20261114_constrained_collocation.py` | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| `geometry_20261114_full_metric_inequality_correction.py` | `d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c` |
| `geometry_20261114_full_metric_projection_warm.py` | `8fb6411e7b876713725a80c2dbe9e322cc277001b0692ccc59e0edd59ec4e8b0` |

当前 $m=699$，物理块维数 $n=338$，独立物理节点数 $N=m-1=698$。全局变量 $u$ 含 $109$ 个自由 core 系数和 $3$ 个 scalar 控制，共 $d=112$。总未知量 $Nn+d=236036$。以下公式也适用于同类接口中其他满足相同块结构的维数。

令 $z=(x_1,\ldots,x_N,u)$ 为原算法的 **scaled-z** 坐标，$S=\operatorname{diag}(\texttt{chart.scale})$，且

$$
A=W_r J S^{-1},\qquad H=A^TA+\lambda^2 I,\qquad \lambda>0.
$$

此处 $J$ 是现有 `CompleteLinearization` 的有限数组算子；它不是被默认认证为精确连续方程导数。原残差 $b=W_rR$ 和全角 $B$ 的模型身份保持不变。

分块后，interval 0 的行是

$$
\widehat R_0x_1+G_0u,
\quad
\widehat R_0=W_0R_0S_1^{-1},
\quad
G_0=W_0\bigl[L_0E S_c^{-1},\ P_0 S_p^{-1}\bigr],
$$

其中 $E=\texttt{chart.inlet}$，已经包含入口 $t_j=-2j c_j$ 的完整链。其余 interval $i=1,\ldots,N-1$ 为

$$
\widehat L_i x_i+\widehat R_i x_{i+1}+G_i u,
\quad
G_i=W_i[0,\ P_iS_p^{-1}],
$$

而最后全部 $d$ 个边界行为

$$
F x_N+G_bu,
\quad F=W_b BY S_N^{-1},
\quad G_b=W_b[BC S_c^{-1},\ BP S_p^{-1}].
$$

`P_i` 必须使用原源已保存的 `L_parameter + R_parameter`，不能只取一个端点。上述 core 的零列来自原源已经逐块检查的“局部 RHS 无显式 core 依赖”，不是新增删列。

目标矩形平方根为

$$
\mathcal M=\begin{bmatrix}A\\ \lambda I\end{bmatrix}.
$$

若使用原正对角预条件器 $C$，只能令 $z=C^{-1}t$，同时因子化

$$
\mathcal M C^{-1}=\begin{bmatrix}AC^{-1}\\ \lambda C^{-1}\end{bmatrix}.
$$

不能在这种坐标下仍添 $\lambda I$，也不能在正则行再乘一次 $S^{-1}$。默认可不使用 $C$，以减少坐标转换；是否选择 $C$ 是后续真实运行的显式参数。

## 2. 保全所有纯 global 行的局部 QR

这里只写 $C=I$ 的形式；使用 $C$ 时所有对应列都统一除以其实际对角元。

初始携带行为 $[T_1,V_1]=[\widehat R_0,G_0]$。另维护仅作用于 $u$ 的平方根 $Z_1=\lambda I_d$。这将 global 正则行只加入一次。

在第 $i<N$ 个物理节点，将全部相关行写为

$$
\mathcal F_i=
\begin{bmatrix}
T_i&0&V_i\\
\lambda I_n&0&0\\
\widehat L_i&\widehat R_i&G_i
\end{bmatrix},
$$

列顺序为 $(x_i,x_{i+1},u)$，尺寸 $3n\times(2n+d)$。仅对前 $n$ 列做 Householder QR，并将同一正交变换作用于其余所有列，得到

$$
Q_i^T\mathcal F_i=
\begin{bmatrix}
D_i&U_i&V_i^{\rm out}\\
0&\widehat T_i&\widehat V_i
\end{bmatrix}.
$$

上部 $n$ 行成为最终三角因子的当前行块；下部仍有 $2n$ 行，不能直接丢弃。对 $[\widehat T_i,\widehat V_i]$ 的前 $n$ 列再做 QR，得到

$$
\widetilde Q_i^T[\widehat T_i,\widehat V_i]
=\begin{bmatrix}T_{i+1}&V_{i+1}\\0&E_i\end{bmatrix}.
$$

接着将全部纯 global 行 $E_i$ 与已有 $Z_i$ 堆叠，做 $d$ 列 QR：

$$
\operatorname{qr}\begin{bmatrix}Z_i\\E_i\end{bmatrix}
=\begin{bmatrix}Z_{i+1}\\0\end{bmatrix}.
$$

这一步是保持完整 $H$ 的必要部分。不能只留下 $T_{i+1},V_{i+1}$ 而遗漏 $E_i$，也不能仅保留它的对角近似。第二次 QR 的 $T_{i+1}$ 可以秩亏；它只是携带行，算法不对它求逆、不因秩亏删行。下一节点自己的正则行仍被加入。

最后节点堆叠

$$
\begin{bmatrix}
T_N&V_N\\
\lambda I_n&0\\
F&G_b\\
0&Z_N
\end{bmatrix}
$$

并对全部 $n+d$ 列 QR。这保留最后边界、最后物理正则和已经累计的全部 global 信息。

每个物理节点的 $\lambda I_n$ 恰加入一次，global $\lambda I_d$ 恰加入一次。当前消元 front 的物理列有独立正则行，故精确实数算术下其最小奇异值至少为 $\lambda$；不用局部 ridge 或奇异值截断。带 $C$ 时对应下界由实际 $\lambda C_i^{-1}$ 给出。此代数性质不是浮点因子精度证明。

如果只消费 $H$，压缩后真正全零的系数行对 $\mathcal M^T\mathcal M$ 无贡献，可以省存。若以后还要用 QR 直接求原最小二乘线性项，必须将 $[-b;0]$ 经过完全相同的变换，并累计零系数行留下的 RHS 平方常数；不能把这些常数也删去后声称目标值不变。本最小组件只提供 $H^{-1}$ 候选，完整目标值继续由原 $A,b$ 计算。

## 3. 因子结构与两个完整三角求解

最终 $R$ 的第 $i$ 个物理行只涉及 $x_i$、$x_{i+1}$ 和 $u$，即块 $D_i,U_i,V_i^{\rm out}$；最后 global 块为 $R_g$。在精确算术下

$$
R^TR=H.
$$

求 $Hv=h$，先解 $R^Ty=h$：

$$
D_i^T y_i=h_i-U_{i-1}^T y_{i-1},
\qquad
R_g^T y_g=h_g-\sum_{i=1}^N(V_i^{\rm out})^Ty_i,
$$

其中首块没有前项。再解 $Rv=y$：

$$
R_gv_g=y_g,\qquad
D_iv_i=y_i-U_iv_{i+1}-V_i^{\rm out}v_g,
$$

末块没有 $U_N$。全部 global 变量参与两次求解。

若因子属于 $\mathcal M C^{-1}$，应先解 $R^Ty=C^{-1}h$、$Rt=y$，最后返回 $v=C^{-1}t$。恢复后仍检查原坐标中的

$$
r_H=A^T(Av)+\lambda^2v-h.
$$

该残差必须使用原 `CompleteLinearization.operator(weights)` 的完整 `matvec/rmatvec`，不能以三角系统自身的小残差或预条件坐标的残差替代。原 full-H helper 仍可把未足够精确的候选仅作为有限基向量，随后用真实 $A$ 构造 Gram、核全部 $B$ 行、径向修复并做原非线性回溯；不宣称 QP 最优。

## 4. 真实数组模型与浮点范围

源数组 `L/R/P/BY/BC/BP/E/Wr/S` 和可选 $C$ 必须按实际 dtype、shape、原 bytes 固定身份。首次 core 块 $L_0E$、行列缩放、QR 和三角解本身都会舍入。即使表达式在精确实数算术下等价，也不能把组装后的浮点块视为原 Python `matvec` 的逐位等价实现。

因此组件需报告：源与输入摘要、全部因子摘要、当前使用的坐标变换、原算子与生成因子在实际返回方向上的作用差、原 $r_H$、RSS 和耗时。不能由“采用 QR”推断导数精确，不能由精确模型的 $\lambda>0$ 推断浮点有效秩或剩余有效数字。QR 避免显式形成 $A^TA$ 后再加 $\lambda^2I$ 的损失机制，仍需原算子读回。

未完成因子化、非有限因子、零三角对角或 LAPACK 失败须保全实际失败位置，不通过新增 ridge/clip 掩盖；后续优化入口可保留原 C 候选。它们不是新增科学完成门。

## 5. 内存、工作量及最小接入

用 full binary64 块保存，而不做三角打包，当前因子需要：

| 内容 | bytes |
|---|---:|
| $N$ 个 $338\times338$ 对角块 | 637,938,496 |
| $N-1$ 个相邻上块 | 637,024,544 |
| $N$ 个 $338\times112$ global 块 | 211,387,904 |
| 最后 $112\times112$ 块 | 100,352 |
| 合计 | 1,486,451,296 |

现有 $L/R/P$ 和边界系数约需 1,281,942,368 B。两者合计约 2.77 GB；还要加现有程序状态、全角 B、BLAS workspace 和数组临时量。最大常规 front 为 $1014\times788$，约 6.4 MB。无需建立约 891 GB 的全稠密矩形矩阵，也无需建立全 $H$。

因子化工作量为 $O(N(n^3+n^2d+nd^2))$；普通稠密局部 Householder 的常数不小，当前尺寸可能在 $10^{12}$ 量级浮点运算范围。每个后续 RHS 的两次三角求解为 $O(N(n^2+nd)+d^2)$，不再需要几百次完整 $A/A^T$。这些是维数推导的预算，未给实测时间或保证比 actual30 更快。

独立组件为 `exact_20261114_regularized_block_qr.py`，直接接同一 live linearization 和固定模型，不改冻结 helper。最小后继插入点为 full-H helper 的两类 `_pcg` 调用：无约束中心 $H^{-1}(-A^Tb)$ 和新增活动行 $H^{-1}B_i^T$。薄入口需在唯一 `CompleteLinearization` 创建时保留对象，并将其返回的同一个原 A 对象、同一 Wr/S/λ 与因子绑定；不能只拿一个不知来源的黑盒 A 冒同一模型。

因子可以留在 RAM 或独立 `RUNNER_TEMP` 文件；大因子仅作可选 artifact，不复制 Git。有限预算在完整局部 QR 之间检查，开始后的原模型残差读回和失败保全仍需完成并记账。原 C 候选、同一完整目标比较、全部原域和原回溯仍由上层原入口保留。

## 6. 可调用接口及当前验证范围

新模块已写出，当前仅做 Python AST 和源码检查；没有本地导入运行、toy 数值或实际候选因子化。所有构造、factor、solve 入口核 `GITHUB_ACTIONS=true` 和准确公开仓库名。

```python
from exact_20261114_regularized_block_qr import RegularizedBlockQR

# linear 是唯一原 CompleteLinearization；A 是这同一固定模型的算子。
with RegularizedBlockQR(
    linear, weights, damping,
    deadline=absolute_monotonic_deadline,
    original_operator=A,
    column_preconditioner=None,  # 或本模型已经固定的原 C
    storage_directory=None,     # 或 RUNNER_TEMP 下尚不存在的独立目录
    input_identity=complete_original_model_identity,
) as factor:
    factor.factorize()
    reply = factor.solve_H(rhs, label="full-H-original-row",
                           relative_tolerance=1e-8)
    candidate = reply["candidate"]
    original_residual = reply["original_residual"]
    diagnostics = reply["report"]
```

`original_operator` 省略时，由冻结原类构造其同系数算子，不重新产生 J。显式传入 A 时，A 与其来源的关联仍是调用方的模型身份责任；组件在实际返回方向上额外比较传入 A/AT 和冻结原类重建的 A/AT，不能把有限个作用核对说成对任意黑盒的独立恒等证明。

`solve_H` 返回候选、原完整残差、因子正规作用残差及 JSON 可写报告。`relative_tolerance` 仅给内层读数标记；未达到也会如实返回有限候选，供原 full-H 有限基算法处理，不新增 BVP 接受门。报告保留每次求解的原 RHS/候选/原残差摘要、因子摘要、原 A/AT 调用次数、额外原源作用检查、RSS、耗时和越过 deadline 完成既有求解与读回的事实。每次求解前重新核全部原系数 bytes，防止原对象属性替换或模型变化后复用旧因子。

后继薄接 `_pcg` 时，还须把这些 A/AT 调用计入上层总工作账。QR 因子化本身是新的显式 $N$ 块工作预算，不能假称已被旧 1200 次 H-action 上限支付。没有在本稿接该薄入口或触发运行。

可选文件存储会保 `diagonal/next-physical/global-border/global-diagonal.f64le` 和 `factor-status.json`；失败的部分因子明确标为不完整，不能求解。RAM 因子只保存摘要，关闭对象后释放因子引用。源码/输入身份错误、非有限值和 LAPACK 失败保留其实际原因；普通进度回调失败只记诊断，不成为数学否决。

实现所需低层接口按官方 SciPy 文档核对：[`dgeqrf`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lapack.dgeqrf.html)、[`dormqr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lapack.dormqr.html)、[`dtrtrs`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lapack.dtrtrs.html)。实际 Actions 必须记录所用 NumPy/SciPy/LAPACK 版本；本文没有执行导入数值检查或新 fixture。
