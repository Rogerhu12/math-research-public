# R138 补篇：实际完整根圈 mean 分母严格为正

2026-11-20，visible-exact-astra-ac637-20261120。

**首次实际完成并冻结。** [公开 run 44733403315/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44733403315) 已在同一 Qrepair、准确 $\eta_0,\nu_0$、整个真根区间及完整 $2\pi$ moving 圆周上包围真实物理 periodic frame 的 mean 相容分母。完整保存球严格给
\[
\boxed{\qquad \frac{17}{20}<\mathcal D<\frac{87}{100},
\qquad \frac1{\mathcal D}<\frac{20}{17}.\qquad} \tag{M.1}
\]
因此[完整根型](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md) (U.8)--(U.10) 的 mean 消元现已合法。实际 finite 根型、高尾和体残差吸收仍各自未闭；本次不授正侧全逆或本题最终精确族。

## 1. 唯一新目标与准确对象

本次执行[全圈 mean 合同](../notes/2026-11-20-R138-root-mean-angular-contract.md)。令
\[
\ell=X(r_*,0),\quad \rho=a/m,\quad
q_0=-I_\phi(v-m)/m,
\]
\[
A_0=1/v-q_0v_\phi/v^2,\qquad
B_0=-uA_0-q_0u_\phi/v.
\]
[实际全角转移证明](R138-supplement-actual-root-angular-comparison-and-mean-readout.md) (W.13)--(W.16) 给
\[
\mathcal D=\langle\rho(A_0X+B_0Y)\rangle_\phi\cdot\ell.
\]
这里 $X,Y$ 是同一个全周期物理径向模型，真实 lift、完整 mean 和全部原32个角模式均保留；$\ell$ 是根轴的同一个固定环境向量。

候选、修补、参数和真根完全不变：

- candidate `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`；
- Qrepair `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`；
- $\eta_0=-7789843107295549/4611686018427387904$，
  $\nu_0=-2572625729470897/72057594037927936$；
- $r_*\in[1191984371497/5000000000000,\ 2383968743003/10000000000000]$。

采用局部 $(X(0),Y(0),n(0))=(e_z,e_y,e_x)$，其定向与原 $(X,Y,n=Y\times X)$ 相同，可由一个 proper ambient rotation 实现；因此投影向量准确成为局部 $e_z$。这个操作没有改变实际世界锚，也没有将局部 $e_z$ 冒充原世界竖直方向。

原已成功的轴 $q,s$ **没有读取或重算**。轴源文件只提供原输入 loader 与私有65系数定义；新计算不构建 W2C context，不消费原4650行正区数据，不调用旧 geometry、residual、primitive 或 intrinsic producer。

## 2. 完整保存球和严格有理后果

以下四个完整记录逐字取自[实际小结论](../notes/root_mean_angular_ci/run-44733403315-1/root-mean-conclusion.json)。每个记录的意义是
\[
[(M-R)10^e,(M+R)10^e],
\]
其中 $M,R,e$ 分别为整数中心、非负整数半径和十进指数：

```json
{
  "ideal_mean_denominator": {
    "kind": "complete_decimal_ball_v1",
    "midpoint_integer": "858121691573291287101517706970644893714487143214110869551979679154892561564",
    "radius_integer": "4493694935361202693055580512997955174930222616679362366135434192019783681",
    "decimal_exponent": "-75"
  },
  "complete_mean_direction_coefficient_upper": {
    "kind": "complete_decimal_ball_v1",
    "midpoint_integer": "961019454074446645876812486213084496363071452134386386649097974006652047096",
    "radius_integer": "2",
    "decimal_exponent": "-75"
  },
  "actual_frame_transfer_fee": {
    "kind": "complete_decimal_ball_v1",
    "midpoint_integer": "105712139948189131046449373483439294599937859734782502531400777140731725180",
    "radius_integer": "2",
    "decimal_exponent": "-80"
  },
  "actual_mean_denominator": {
    "kind": "complete_decimal_ball_v1",
    "midpoint_integer": "858121691573291287101517706970644893714487143214110869551979679154892561563",
    "radius_integer": "4494752086473044587234950888639350779647447765370766928251482779190034433",
    "decimal_exponent": "-75"
  }
}
```

实际球约为 $0.8581216916\pm0.0044947521$；**精确结论只以上面的完整整数球为准**。直接有限十进有理比较给
\[
.8581<M10^{-75}<.8582,\qquad
0<R10^{-75}<.0045,
\]
故下端大于 $.8536>.85$、上端小于 $.8627<.87$，证明 (M.1)。没有只消费中心值或未保存的窄球。

同样，已保存的 mean 系数预算
\[
\chi_m\ge\left\langle|\rho|\sqrt{A_0^2+B_0^2}\right\rangle_\phi
\]
约为 $.9610194541$，完整上端小于1。真正 periodic-frame 转移费为
$(11/10^7)\chi_m$，约 $1.0571214\cdot10^{-6}$，已完整计入最终 $\mathcal D$ 球。

原真实 mean 相容式
\[
\mathcal D\mu+\mathcal L f+\mathcal H=0
\]
于是有唯一解
\[
\mu=-\frac{\mathcal L f+\mathcal H}{\mathcal D},\qquad
|\mu|\le\frac{20}{17}(|\mathcal L f|+|\mathcal H|).
\]
这保留独立 mean、全部 high-stable 行和根缺陷。$\mathcal L$ 与 $\mathcal H$ 自身在所需范数中的实际预算仍须按根型全文支付，未由本次分母计算自动给出。

## 3. 实际覆盖与定向算术

全部8192个**闭角区间** $[2\pi j/8192,2\pi(j+1)/8192]$ 被实际消费。每个区间保所有角点、完整真根不确定性和 repair coefficient error。常 skew 中心的 Rodrigues 传播保持正交比较；真实连接变化的 $h\delta_\Omega$ 与每步矩阵全部算术半径逐次支付。

均值积分消费整个 cell 内的 frame 和系数包围，规范化 cell 权为准确 $1/8192$。整圈模型本身无需闭合；W.16 的 $11/10^7$ 独立转移费将其送到真实 periodic frame。新数组和轨迹始终只在 child 私有内存中。

最终 strict sign 的程序顺序是：保存并读回 ideal 球和 $\chi_m$ 上界球，形成完整 actual-frame 费用，再保存并读回最终 $\mathcal D$ 球，最后判号。实际 `strict_sign_uses_complete_saved_decimal_ball=true`，没有轴输出中宽展示字段和窄内部判号之间的复用问题。

| 执行项 | 原记录 |
|---|---|
| run / attempt | `44733403315/1` |
| 入口 / 触发提交 | `0436d4ec6983b284c906c6e5c44df314b7772baf` |
| marker 成功推送后的科学 checkout | `bb7d6d77bb341abf1fe3c6d991cac8d2fa62c8ea` |
| runtime | Python `3.12.14`、python-flint `0.9.0`、NumPy `2.3.5` |
| precision / 完成角格 | 320 bits / 8192 |
| child 数量 / 返回码 | 1 / 0 |
| 数学用时 | `1.9066021130000053` 秒 |
| child wall time | `1.997779750999996` 秒 |
| 新完整 target | 1 |
| 旧成功重算 / 旧 producer 调用 | 0 / 0 |
| 新数组 / artifacts / Releases | 0 / 0 / 0 |

## 4. 全部身份与公开小文件

root 已核11个当前输入的全部 bytes/SHA/Git blob，并核 manifest 整个当前表与 execution 回执全等。6个历史原件（原candidate五片、原germ）由 worker 逐字恢复；root 另核全部历史 blob及完整恢复回执与清单全等。科学输出 hash、scope 全对象、全部已保存 README diff 和实际 child 元数据均核过；本机0科学执行。

公开 execution 记录5次实际规则 pull，保第一次与最后三次完整回执，四份全为空diff；读点仍为 `96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1`，全部5次摘要保 hash chain。此结果冻结，后续只读完整球。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| [execution.json](../notes/root_mean_angular_ci/run-44733403315-1/execution.json) | 11783 | `25d6e66fade5f838a33e62da0f502152115a34c5c572c662471b6c9acad38cb5` |
| [report.md](../notes/root_mean_angular_ci/run-44733403315-1/report.md) | 676 | `62d0890f23932d18d7796114499b349845fbe12929b451b91325c6e24371f34c` |
| [root-mean-conclusion.json](../notes/root_mean_angular_ci/run-44733403315-1/root-mean-conclusion.json) | 4131 | `de3a14606aa432fbd1f7707c277a33110f81ce6ca23fdfc6bfdf7e9d497623b4` |

新源 SHA-256 `affc4dd2ead1e74ce91f3c87bbd2fb279c449758a70dfe427ade2b05077febd9`，
worker `95cadbb244774a5c4b9e99de0008959f852bb7bf714ead97518d007ab1c48b02`，
manifest `2b71e82c6822d99dc10ce2167d1b29ca70f0bc832c28938bdb9e9f79d729eb47`。
完整 source/参数/run/hash 和小结论即为后继入口。

本次只关闭完整根型的 mean 分母条件。原低 even96、高 stable97起无限部分、有限角矩阵、真正高尾导数费用、R138 体 residual 三门、完整 low/high/finite $\rho$、两个 RHS、physical/negative 与非线性 matching 继续按各自原合同推进。
