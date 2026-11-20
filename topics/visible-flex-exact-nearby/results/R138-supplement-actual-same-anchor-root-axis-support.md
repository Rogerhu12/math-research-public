# R138 补篇：同一物理外锚到真根的两标量实际包围

2026-11-20，visible-exact-astra-ac637-20261120。

**首次实际完成并冻结。** [公开 run 44730968113/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44730968113) 完成原全部 4650 闭行上的新二维正交 ODE 消费者，并支付真根 collar 与连续修补费。对原 Qrepair、准确 $\eta_0,\nu_0$ 和同一个全周期外端物理锚，令
\[
G=F-\tfrac12e_z,\qquad
q=G(r_*,0)\cdot X(r_*,0),\qquad
s=G(r_*,0)\cdot n(r_*,0).
\]
保存的完整中心球与误差球严格推出
\[
\boxed{\quad -89/250<q<-3/500,\qquad 97/100<s<33/25.\quad} \tag{A.1}
\]
这只是同一真根轴初值，不授全根圈、mean 分母、根边界型正性、全逆或本课题最终精确族。原全域 support $G\cdot n>2/5$ 仍按其独立证明使用。

## 1. 固定对象与完整新目标

使用[两标量公开合同](../notes/2026-11-20-R138-root-axis-support-contract.md)和[真实根全角型补篇](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md) (U.17)--(U.21)。新源只在反射轴上消费原候选的完整 dyadic 定义，方程为
\[
(q,s)'=eK v_{\rm axis}
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}(q,s)+(e,0).
\]
逐闭行的冻结 skew 传播准确正交；真实系数变动与全部区间算术费用线性累加。轴投影经过原3595个候选片段，保留全部3594个内部接口；最后一片为2549。这是原定义的消费，不是候选重拟合或旧几何重算。

固定身份：

- candidate `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`；
- continuous repair `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`；
- $\eta_0=-7789843107295549/4611686018427387904$，
  $\nu_0=-2572625729470897/72057594037927936$；
- 真根完整区间
  $[1191984371497/5000000000000,\ 2383968743003/10000000000000]$；
- 原 positive gzip `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`，
  原 root germ `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`。

完整外锚和 $p=e_z/2$ 没有重选；轴初值可放在局部正交坐标中，不能把局部坐标轴误认成另一个世界锚。

## 2. 保存的完整球

下列原文来自[实际小结论](../notes/root_axis_support_ci/run-44730968113-1/axis-support-conclusion.json)，不重新评估旧数据：

**径向体传播后的 nominal q：**

```text
[-0.1806777904003410754929896921547542852942886015902062395374951579391818009917845867087700477120538024 +/- 4.68e-101]
```

**径向体传播后的 nominal s：**

```text
[1.144739189554633775484054122405058626719614295931515075820564914236731296483741954234160442987318750 +/- 1.98e-100]
```

**全4650闭行的 axis error：**

```text
[0.1743534411756401896756622503842710641507189759063508286547973433206596476725518312789132432165235458 +/- 9.61e-102]
```

**真根 collar fee：**

```text
[1.109242866008173490696711272179482815742176721247905850528911757310562113543152534430653389325096494e-5 +/- 9.47e-106]
```

**完整误差（含 collar 与 repair）：**

```text
[0.1743645336043003354105692174969928589788763976735633077133026324382327532936872628042575497504171422 +/- 3.89e-101]
```

修补费为 $16\cdot4\cdot10^{-18}=6.4\cdot10^{-17}$，已计入最后一球。真根 collar 用整个既有根区间与原 germ 的 whole bound，不代入根中点。

必须区分保存格式与证明。文件里的合并展示字段为
`q = [+/- 0.356]`、`s = [1e+0 +/- 0.320]`；这些 Arb 字符串是正确但较宽的外包，单靠前者不能证明 $q<0$。更紧包围来自**同时保存**的 `nominal_q`、`nominal_s` 与 `complete_axis_error`。按源中已证的误差合同，
\[
|q-q_{\rm nom}|\le E,\qquad |s-s_{\rm nom}|\le E.
\]
上面完整十进球直接给
\[
-.180678<q_{\rm nom}<-.180677,\qquad
1.144739<s_{\rm nom}<1.144740,\qquad 0<E<.174365.
\]
相加减这些有限十进有理数即证明 (A.1)。这也独立核实了原两个 sign flags，但后继不得仅把 flags 当严格球。后继应读回三个完整球再构造所需包围；不能用显示上较宽的 `q` 球推出负性。

## 3. 完整执行与身份核对

| 项目 | 实际记录 |
|---|---|
| 公开 run / attempt | `44730968113/1` |
| 触发与入口提交 | `dee7beeb925403c54d4aa84c796b824f3e1e489d` |
| marker 实际推送后科学 checkout | `8a9bd75c2f688ee454979950a5944569e617c0ea` |
| runtime | Python `3.12.14`、python-flint `0.9.0`、NumPy `2.3.5` |
| directed arithmetic | 320 bits |
| scientific child 数量 / 返回码 | 1 / 0 |
| 完成原闭行 / 新标量坐标 | 4650 / 2 |
| 数学用时 | `1.5079489569999964` 秒 |
| child wall time | `1.608078293999995` 秒 |
| 旧完成目标重算 / 原 producer 调用 | 0 / 0 |
| 新数组 / artifacts / Releases | 0 / 0 / 0 |

root 已对 manifest 的11个当前输入逐件核 bytes、SHA-256 和 Git blob，并核 execution 整个当前回执表与 manifest 逐项全等。10个历史原件（positive四分片、candidate五分片、germ）由公开 worker 逐字恢复并核 bytes/SHA；root 另核全部历史 Git blob 标识与清单、回执一致。原6,223,338B positive整对象身份和全部原接口保留，没有在本机导入或执行新科学模块。

5次实际 pull 的全部摘要串成 hash chain；完整 execution 保留第一次与最近三次的完整规则回执，四份均为空 diff，两个 README 的已读提交为 `96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1`。两次结果发布尝试后成功。执行前与 marker 发布时全 topic 分别为198739691B和198740219B；后续发布仍按当前树再次核容量。

| 公开小文件 | bytes | SHA-256 |
|---|---:|---|
| [axis-support-conclusion.json](../notes/root_axis_support_ci/run-44730968113-1/axis-support-conclusion.json) | 2963 | `b300ea209acb2239a93a87aa3f14d6d9c5f0ed3b5b88ea44b415e5078ea0cd92` |
| [execution.json](../notes/root_axis_support_ci/run-44730968113-1/execution.json) | 13491 | `a8979dff609fd41e88be754e09e8fbb2a56528f101c729208e5e54a9ef1de73f` |
| [report.md](../notes/root_axis_support_ci/run-44730968113-1/report.md) | 500 | `37c47f7efdd7675f0b00ea3ef8d693996e212105d68500197a2b3cb0fcb3094e` |

原科学源 `fourfold_codazzi_root_axis_support.py` 为16558B，
SHA-256 `d152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79`；
公开 worker 为28672B，
SHA-256 `80aa654930a8542a0b7d02a5f4d3f693e8f074777a3ee15609de3a1bdf0f5091`；
manifest 为9741B，
SHA-256 `e5ffef8c89e55b0f6c78f3564d455439483bd9556a05ba1f7a5acc307ceb08f8`。
这些源、参数、run、hash 和小结论构成复用入口，不发布新的轴数组或角数组。

## 4. 后续仍须支付

本次只完成两个新的轴标量及其误差，不计入 R139 原50条目标，不重跑已有成功。完整根角 ODE、真实 periodic frame 转移、完整 mean 分母离零、finite 根型与真正高频余项仍各自待付。R138 的体 residual 预算和吸收严格门、R141 的完整 low/high 反馈、原 finite $\rho$ 与两 RHS、真实 physical/negative/非线性 matching 也不自动关闭。
