# 精确 M32 修补后的完整外图与已缓存正区：公开消费合同

本次新增两项数值消费：修补后的完整 regular $H^s$ 外图，以及原
$4650$ 个闭区间上的新标量 Riccati/Volterra 比较。旧系数生产、
端点场、帽矩阵和目标原函数不重算。所有新算术只在公开仓库 Actions 中执行。
本文不预先宣布任何数值门通过。

## 1. 身份和范围

原中心 SHA256 为
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`；
精确修补定义为
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
修补 native
`6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc`
保留所有 $65$ 个实槽、全部均值和 $6143$ 个准确接口。
偏移只含原 $32$ 个 moving 模；这不是对未知方向的频率截断。

原完整正区 native
`ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`
从四个原 binary parts 逐字节恢复，完整原区间为

$$
[r_b,R]=[0.2384058742994,25/8].
$$

新报告仅声明固定物理 $\eta_0$ 与原 $\nu$，
即仿射参数偏移 $\eta=0$；不自动继承更宽参数域。
根 collar 由独立消费者转授，完整负区、高低反馈、参数 Schur 及非线性闭合仍分别保留。

## 2. 外端物理角变化已经付清

原实际修补帽背景 native
`35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff`
证明固定物理角下的完整 $\Delta C(R)$ 的 $A_{1/64}$ 范数。
它包括无限物理 Fourier 尾和真实均值；不是只比较两个 reciprocal 函数而漏掉角变化。

因此直接由 Fourier Cauchy 界，

$$
\|(\Delta Z)_\theta\|_{A^0}
\le64\|\Delta C\|_{A_{1/64}},
\qquad
\|\bar Z_\theta\|_{A^0}
\le\|Z_\theta\|_{A^0}+64\|\Delta C\|_{A_{1/64}}.
\tag{O.1}
$$

非均值投影在 Wiener 空间的范数为 $1$，角导数消掉均值，
所以 (O.1) 没有遗漏一个额外 mean 费。
$\bar Z$ 自身使用同一已成 native 的完整外端上界。

对原 right-offset 向量的全部 $65$ 个精确有理数，
新消费者实际计算 $E_{u,\sigma}$、$E_{v\ne0,\sigma}$，
$\sigma=1/8$，并保持 $e_0=\langle e_v\rangle$。
由准确角差公式，

$$
\|\bar\psi-\psi\|_{A_\sigma}
\le
\frac{E_{v\ne0,\sigma}
+|e_0|\,\|v-m\|_{A_\sigma}/m_-}
{4(m_--|e_0|)}.
\tag{O.2}
$$

原 $\|u\|_{A_\sigma}$、$\|v-m\|_{A_\sigma}$ 与 $\|\psi\|_{A_\sigma}$
分别加上这些实际费用；$|m|$ 的上下界也准确增减 $|e_0|$。
新参考终端保持真正的

$$
\bar p_M(R)=q_*/(-\bar m_R),
\qquad \frac18<\bar p_M(R)<\frac15.
\tag{O.3}
$$

$q_*=(1+w_R^2)^{-1/2}$ 属于未改的真实外部度量；
新均值不被替换回旧中心均值。

## 3. 完整 $H^s$、Hilbert 与 affine 外端各列重新验算

原
[R133 完整 regular $H^s$ 外图](../results/R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
的 (S.10)–(S.18) 在同一真实 long Banach module 与复背景球中成立。
使用新 $\bar Z_\theta$ 后，重新计算

$$
\bar\Xi=
\frac{\|\bar Z_\theta\|_{A^0}}{\rho_Z}
+\frac{\|(f_B)_\theta\|_{\dot A^2}}{\rho_B},
\qquad
\|D_Zd\|_{H^1}\le T_0+\bar\Xi\,\bar T,
\tag{O.4}
$$

并保留 $D_{f_B}d$、$D_Zc_0$、$D_{f_B}c_0$ 的完整列。
新的 $H^{1/6}$ 界来自同一算子的 $L^2$/$H^1$ 插值。
不把只适用于 Hilbert 共轭的结论转授给整个非线性 DN。

对新角预算 $\bar P$，按
[无导损 Hilbert 接线](../results/R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md)
(L.13)–(L.19) 重新计算

$$
\epsilon_1=\bar P/\sigma,\quad
\epsilon_2=2\bar P/(4\sigma^2),\quad
\epsilon_3=6\bar P/(16\sigma^3),
$$

$$
K_0=\frac{\epsilon_2}{1-\epsilon_1}+(1+\pi)\epsilon_1,
$$

$$
K_1=\frac{\epsilon_3}{3(1-\epsilon_1)}
+\frac{\epsilon_2^2}{2(1-\epsilon_1)^2}
+(2+\pi)\epsilon_1+\epsilon_1^2 .
\tag{O.5}
$$

以 $\pi<22/7$ 外包，完整 Hilbert 共轭费用是 $K_0+4K_1$。
没有使用同阶 $\mathcal C-I$ 小量。

随后全部重付 (S.21)–(S.38)：完整乘子、$1/v$、
非均值 $h_2$ 图的 onto 性、独立 mean 输出、低模输入到高模外图、
$f_B$、普通 Robin 残差与独立 mean 残差。
即使重付后的界落在原显示预算内，也是新输入下的实际验证，
不把旧报告自动标为已修补。

新外图只给 $H^{1/6}$ 所需的全高终端反馈；$s=1$ 主体的右高端口
仍独立，未支付的物理 $H^{7/6}$ 非线性外图不会被声明为已成。

## 4. 4650 原闭行只做准确膨胀和新标量比较

逐行膨胀遵循已证明的
[完整 M32 repair 转授合同](../results/R133-supplement-exact-M32-repair-transfer-of-cached-positive-high-rows.md)。
该公开正文 SHA256 为
`a6c604bc4bb11522f5cc7538dc8f9ed857dfc61474e80a3c350b9310295f6dba`。

新消费者保留每个原 intrinsic enclosure、原候选片号、原右接口与原行摘要，
并另存全部新 bounds。完整 reaction、primitive、signed mean-own rate、
mean feedback 和 mean-rank 行均按 (A.3)–(A.9) 膨胀。
新 principal speed 为 $-\gamma\bar m$；
从未将其乘未知角导数的变化称为 $L^2$ 有界扰动。

全区间新参考为

$$
\bar g_M'=M\bar a(K-\bar g_M^2),\quad
\bar g_M(r_*)=M^{-1/3},\qquad
\bar p_M'=M\bar a(\bar p_M^2-K),\quad
\bar p_M(R)=q_*/(-\bar m_R).
\tag{P.1}
$$

在内切面 $r_b$ 取 $g=0$ 只用于保守下比较；
它没有改变 (P.1) 的真实根初值。
每个 lower-flow 在降低 speed 或 frequency 前准确 reset 至
$\min(b,\sqrt{K_-})$，然后使用原已证的标量公式。

对所有 $|j|\ge97$、物理频率 $M\ge388$，
使用新 $p_-,g_-$ 得到全闭行的 $W_-$、damping、frame 和完整 remainder。
两个 order $s=0,1$ 分别执行全前向与后向 Volterra sweep，
每格端内 supremum 都保留；不是仅检查若干径向节点。
$s=0$ 的终端费用直接来自本次实际新 outer native，
$s=1$ 保留独立右高端口。

普通源列、两个原始迹、full head-to-high、high-to-head、
head generator 和独立 mean 行均保存。
新中心的值跳跃由 exact repair 身份准确为零；
任意方向或准解的 affine jump 仍是独立源，不能据此删除。

## 5. 可审核结果和后续接线

新数学源：

- `scripts/fourfold_codazzi_repaired_regular_Hs_outer.py`；
- `scripts/fourfold_codazzi_repaired_positive_high_Volterra.py`。

新 wrapper：
`scripts/fourfold_codazzi_repaired_positive_CI.py`。
它只恢复原 $6.22$ MB 压缩 native 的准确字节，再运行新外图及新标量比较。
先完成的外图会立即保存和发布；若后续失败，
其实际成功过程与失败后缀都保留。匹配源和完整输入的旧成功外图可以复用，
不会为了重复发布再运行。

新 native 保存全 $4650$ 行的膨胀和两个 order 的所有比较行；
另提供小型 UTF-8 JSON 摘要，供仅集成可用时审查真实退出码、
输入身份、全部源列和最终费用。结果仍需与根 collar、负区及真正全局 Schur 接合。
