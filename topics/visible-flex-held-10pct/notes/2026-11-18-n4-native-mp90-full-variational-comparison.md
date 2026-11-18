# n4：已有原生扩展精度与 MP90 全列变分的只读对照

分类：**数值证据**。已对 stage 43、38、175 的全部 $3\times42\times40=5040$ 个保存条目作逐项对照，分别使用原生 x87 80 位数和其单次转成 binary64 后的数。此条没有重算任何导数、非线性流或根，没有调用 DN/BVP，也没有新增验收阈值。

## 1. 对象、坐标与指标先于比较固定

参照来自 [已完成的保存 MP90 轨迹变分](2026-11-18-n4-saved-mp90-variational-reference-terminal.md)：源 `a939698d…`、plan `d4f43809…`、raw `4ad1e373…`。原生数据来自 [六调用终态](2026-11-18-n4-native-longdouble-pair-terminal.md)：冻结 C++ `916d0a94…`、库 `d31cd86f…`、plan `b30bdac3…`、raw `9853dc0a…`。三个 stage 的 state-only/fullJac 状态逐位相同；此条只使用已有 fullJac 检查点。

两边分别是在各自近似 LD 或 MP90 非线性轨迹及近似返回根上的方程变分，差异包含轨迹和近似根的差异。它不是有限 root 停止算法的导数之差，也不是与未知精确连续流导数的差。

比较规则在 source 和 plan `f47a502b6e1cf8066bd0db23ba7a2bed9001c613c90948f0869d4194e64b053f` 中先固定，再执行：

- 输入列沿用原 stage 的 $Q_{0:20},\pi_{0:20}$，**不作输入端 portRatio 缩放**。
- 输出前 20 行为 $Q$，次 20 行为 $\pi$，第 40、41 行为两 mean（索引均从 0 开始）。原物理输出转换只对 $\pi$ 行除以该 stage 的 `portRatio`，对两边应用同一转换。这三个具体比值都是精确数 1，因此 equation 与 physical-output 两套结果相同；代码仍实际执行并核对两套转换。
- 对指定块 $I\times J$，令 $E=N-M$，报告

$$
 e_{I,J}=\max_{i\in I,j\in J}|E_{ij}|,
 \qquad
 r_{I,J}=\frac{e_{I,J}}{\max_{i\in I,j\in J}|M_{ij}|}.
$$

这里 $M$ 是保存的 MP90 参照。$r$ 是同一块的最大条目尺度比，不是逐分量相对误差，也不是诱导算子范数或条件数。当分母为零时，仅在分子也为零的情况下报告 0，否则报告未定义；不加人为分母地板。

除了全 $42\times40$ 和前 $40\times40$ 块，还完整报告 $Q/Q,Q/\pi,\pi/Q,\pi/\pi$ 四块及两个 mean 行。没有只挑较好的块或按结果更换指标。

## 2. 原生与 binary64 的全矩阵结果

下表为全 $42\times40$，前 $40\times40$ 的最大值在这三个 stage 与它相同。`峰位置` 是非零差的最大绝对值所在零起始行、列；所有这些全矩阵峰均在 $\pi/Q$ 块。

|stage|数值视图|最大绝对差|同块尺度比 $r$|峰位置|
|---|---|---:|---:|---|
|43|native80|$1.3043475122061\times10^{-8}$|$3.5618905971554\times10^{-19}$|(39,19)|
|43|boundary64|$1.6119963714750\times10^{-6}$|$4.4020130099336\times10^{-17}$|(38,18)|
|38|native80|$1.0465954236132\times10^{-8}$|$3.9694655631932\times10^{-19}$|(39,19)|
|38|boundary64|$1.7627722278317\times10^{-6}$|$6.6857388215731\times10^{-17}$|(39,19)|
|175|native80|$1.0700596094999\times10^{-7}$|$2.7508999615996\times10^{-17}$|(39,19)|
|175|boundary64|$1.5542245420586\times10^{-7}$|$3.9955869702104\times10^{-17}$|(38,18)|

三个参照的最大条目分别约为 $3.66195\times10^{10}$、$2.63662\times10^{10}$、$3.88985\times10^9$。所以应同时看绝对差与同块尺度比，不能把绝对差直接当作某一尾残差或前缀 metric。

前两段 native80 全块比约为 $4\times10^{-19}$，第 175 段为 $2.75\times10^{-17}$，**不属于同一精度等级**。本次只读比较没有定位这一差别的来源；不能在未区分两边轨迹、近似根和变分算术之前归因，也不能由前两段外推到全部 stage。

## 3. 两个 mean 行独立报告

第一 mean 行（行 40）的结果如下。

|stage|native80 最大绝对差|native80 同行尺度比|boundary64 最大绝对差|boundary64 同行尺度比|
|---|---:|---:|---:|---:|
|43|$1.8047186394619\times10^{-23}$|$8.5715347043219\times10^{-19}$|$7.2645080471352\times10^{-22}$|$3.4502875669535\times10^{-17}$|
|38|$4.3874009334740\times10^{-23}$|$1.7238068652296\times10^{-18}$|$1.0231889808587\times10^{-21}$|$4.0201025991825\times10^{-17}$|
|175|$1.3087959742954\times10^{-25}$|$7.6239688643620\times10^{-17}$|$1.3087959742969\times10^{-25}$|$7.6239688643705\times10^{-17}$|

第二 mean 行（行 41）的参照与两个数值视图均逐项为零，按预先定义的零分母规则报告差 0、比例 0，而不是除以某个替代地板。所有四场块的紧凑标量见伴随 JSON；完整矩阵差只在 scratch。

## 4. 精确读取与范围

对原生 canonical 10-byte 编码，以小端 `uint64` 读显式 significand $s$，以 `uint16` 读符号/指数 $e$。有限正规数的精确值为

$$
 (-1)^\epsilon s\,2^{e-16383-63};
$$

次正规数使用 $e=1$ 的尺度，另保存零的符号。源拒绝非有限或非 canonical 编码。每个保存的 binary64 值都独立核为该原生有理数的 nearest-even 转换，含正负零；所有 5040 个转换均通过。保存的 MP90 98 位十进制字符串作为**该字符串所代表的精确十进制有理数**读入，不把它当未知真实导数的精确值。

全部逐项相减、取最大值和尺度比均用 `Fraction`，不经 float 求和。紧凑输出中的 32 位有效十进制数只是最近舍入的显示值，不是向外区间界。完整有理数矩阵差、精确统计和序列哈希均保存于 scratch raw。

本条的冻结 capsule/probe 域 floor 始终为 **0.1**。生产原 checkpoint 则在 `response.checkpoint.parameters.projectionFloor` 保存 **0.05**；此次没有改变任一旧源或配置，没有验证完整生产适配器。上述对照不构成原 DN 的 `2e-9` 接受，不构成全尾、全曲面或连续误差认证。

## 5. 来源与执行

新源 `scripts/resume_closed/compare_native_mp90_variational.py`：SHA-256 `ee0d8679a1c3e48ee49290ae09626c6e87d122f8d6e5476196a39bdbf3bab49e`。准备 chunk `f955bb` 真实退出 0，仅绑定文件和指标；只读比较 chunk **`169617`** 真实退出 **0**，源内计时 `0.7626668330049142 s`。数学执行器、共享库、根/流/导数、DN/BVP 的新增调用数均为零。

scratch 目录 `/workspace/scratch/7322d0dee069/closed_work/n4-native-mp90-variational-comparison-v1/`：

|文件|SHA-256|
|---|---|
|`plan.json`|`f47a502b6e1cf8066bd0db23ba7a2bed9001c613c90948f0869d4194e64b053f`|
|`comparison-summary.json`|`7f6e9bef79de787072b83d4821a09413b2d546f806ac0e9b42c7c5f4840810cf`|
|`comparison-raw.json.gz`|`e5dde8256ed1cc482a22ed3056291c4ba86409cb487a03238a0c559a7c848db3`|

伴随入库记录 `scripts/resume_closed/native_mp90_variational_comparison.json` 是该 summary 的原字节副本，SHA 相同；不提交可再生矩阵数组。完整输入、原 stage 检查点、数值源、库和既有运行输出均有哈希绑定，源拒绝覆盖已有比较输出。

只读复现使用未存在的输出目录：

```bash
python topics/visible-flex-held-10pct/scripts/resume_closed/compare_native_mp90_variational.py \
  --prepare /absolute/new/path/comparison
python topics/visible-flex-held-10pct/scripts/resume_closed/compare_native_mp90_variational.py \
  --run-plan /absolute/new/path/comparison/plan.json
```

下一项是显式保留生产 floor 0.05 的同库批接口与原 DN/audit 的实际承接；本条只支付上述三个保存 stage 的完整变分对照。
