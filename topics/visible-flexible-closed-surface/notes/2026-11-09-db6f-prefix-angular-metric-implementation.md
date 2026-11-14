# 前缀第一档角弧证书 wrapper：静态实现与验证计划

作者：`/root/independent_geometry`，2026-11-09。

状态：**实现已写、语法解析通过，待 root 全文独审及下述定向运行。当前没有新数值证书。** 原已推送代码、输入和审稿均未改。本文件不把未执行的命令、未写出的第二档 Taylor 或未来 M15 图当作已经完成。

## 1. 实现与被复用的证明

新文件 `scripts/db6f-audit-prefix-angular-metric.py`，SHA256 `42e7d222c40512fec2d4fd757544d630b3e372487322e27eb3571a06519eb2fb`，实现已审方法 `2026-11-09-db6f-prefix-angular-metric-refinement-method.md` 的第一档；该方法全文独审为 `2026-11-09-db6f-root-review-prefix-angular-metric-method.md`。

它复用已相消的原 Fourier／径向幂系数、原连续 Hermite 图、已审 common-cut v2、原目标供应包，以及已运行两局部算例中的 `traditional` 和 `angular_bound` 函数。所有数学依赖的文件哈希固定检查。没有实现径向细分或角 Taylor，也不运行非线性求解器。

新检查器 `scripts/db6f-audit-prefix-angular-fixtures.py`，SHA256 `0f4b1e146d137564fac1924f13c8b877691803036a284ca754a4feb706bf7643`，只读输出记录，不导入几何／区间后台。它用于独立核查精确覆盖、最大值和既有局部算例的一致性。

## 2. 基线复用与选择

原完整前缀报告只保存全域最大值，没有保存每个原区间的行。因此本最小接口明确使用两层基线：

1. 若原完整严格界在转移到精确目标之后已经达到预算，直接用于每个请求区间。此路径只重核输入和数据哈希、原目标分区和输出分区；不构造几何对象，不重算原 metric 后台。
2. 若原全域界不够，则仅在请求的原 target 区间上重算原系数相消上界。该区间的有效旧界取新重算区间界与原完整界的较小者；二者均属于同一图与目标。已经达到预算的区间保持一整角周期的叶盒。只有仍未达预算者进入角弧 128 分割及逐个未过预算角弧的二分。

因此未来完整 M15 调用无需先生成另一份重复的全域径向细分数据。原区间集合不变；角度只是验证分区。默认调用覆盖全部 target 区间，`--intervals` 则明确请求局部子集。

## 3. 图、目标及精确 bridge 的绑定

当前最小接口只接受已审 common-cut v2 的 `exact-common-cut-prefix`，`ell=0`。它逐项绑定：共同图及原基础图、基础 binary 数组、尾 manifest 及其全部数据分片、common-cut 实现和 tail reader、原完整 metric 报告、analytic target 元数据和数组、目标生成器及 bridge 参数提取器，以及共同图引用的唯一精确 bridge 根证书。

共同图与基础图中的 `frozen_profile`、`chart`、`warp_reference_q`、`ell` 必须一致；目标供应包的轮廓和基础图哈希必须吻合。原报告必须由冻结原 metric 后台产生，完整检查的区间数必须等于原 target 分区长度。物理 cut 半径、斜率和 $-7w/c$ 二阶条件与精确 bridge 证书相等。原 target 分区的端点以保存 binary 数的精确相等关系检查，并要求每段完整落在一个几何多项式跨内。

`--budget` **始终针对原精确目标 $g$**。令 bridge 证书的已审相对目标差上界为 $\eta$。每个叶盒的源目标上界 $\varepsilon$ 都用 Fraction 转成

$$
\varepsilon_{\rm exact}=\varepsilon(1+\eta)+\eta.
$$

判断是否细分、是否达预算和最终最大值都使用这个精确有理数，不在中途把 $\eta$ 忽略。输入预算不得小于或等于这份固定转移界；需要更小预算时应改进原 bridge 证书，而不是修改这里的比较。

这一 wrapper 不重新证明供应器解析包含性或唯一根；它明确以已审供应包、bridge 证书及完整严格基线为输入。其作用是保留这些对象绑定并完成新的角分区验证。

## 4. 角弧、正分母与失败回退

角变量为 $\varphi=3\psi$，覆盖完整 $[0,2\pi]$，端点以 $\pi$ 的有理倍数保存。初始每个弧为 $[2k/N,2(k+1)/N]$，二分使用精确有理中点。三角端点调用原有理 Taylor 代码；调用前先做该代码自身原本就做的精确模 2 化，只为复用相同端点的缓存。内部极值点仍按未约化的原闭弧范围精确检查，不能因缓存约化而漏掉跨周期极值。

所有角范围作用于已经相消的 $E_r,F_r,G_r$。局部 $a,\rho$ 均有严格正下界后，复用已审归一化式和最大绝对行和界。如果该局部范围暂不能证明正分母，不执行除法。到达最大深度仍未达预算时，可以保留原区间已经有效的完整界及其正分母证据，并明确记为 `original_fallback`；它不使未达预算的叶变成通过。

对每个叶，实际采用角弧界与同一区间有效旧界中的较小者。每种来源、候选角弧界、正分母下界、精确物理区间、角端点、深度及目标转移均保存在叶记录中。

## 5. 输出接口与覆盖重读

叶记录和每区间摘要分别按最多 512 项写成 gzip 分片，每件检查小于 5 MB；原文件拒绝覆盖。最终主报告只在全部请求区间完成且输出重读通过后写出。中途中断若只留下分片而没有完成主报告，不产生可使用的完成证书。

主程序重新读取每个实际写出的 gzip 叶，重核 SHA、记录数、原物理端点、有理角端点顺序、全周期无缝覆盖、正分母、精确目标转移和预算布尔值。最终最大值与计算过程的最大值必须相等。

局部选择会输出 `entire_prefix_covered=False`，且**不提供**可直接交给闭预算程序的 `metric_operator_upper` 或完整精确目标上界字段。它只有明确的 `selected_*` 界。这样两局部测试不能被误接成完整前缀证书。

完整覆盖时才提供 `metric_operator_upper`，其含义仍是原 analytic target 下的源上界，与原闭预算接口相容；既有闭预算据同一个 $\eta$ 转移一次。新报告同时提供已经转移的 `exact_target_metric_operator_upper` 供精确核对。不得将后者再次当成源上界而重复转移。完整覆盖与是否达到请求预算分别记录；有原有效界回退并不强迫 `target_met=True`。

本 wrapper 始终不声明全闭曲面认证、G5、实际误差下降或未生成的 M15 图。实际曲率、尾、帽等仍必须由同一图自己的证书支付。

## 6. 定向验证计划（尚未运行）

只做以下两个执行调用和一次只读检查，不运行全域 M12 新扫描。

第一调用选原 M12 target 区间 **0 与 74**，初始 128 角弧，最大二分深度 1，精确目标预算 $10^{-8}$。检查器将逐位比较两个原区间界及初始 128 弧最大值与既有 `2026-11-09-db6f-audit-m12-prefix-metric-budget.json`。再检查真正二分后的全部叶无缝覆盖，正分母通过，并满足已包含 $\eta$ 的预算。此处不是凭已有数值预先断言通过，必须等待实际退出码和记录。

第二调用不选择局部区间，使用宽松预算 $10^{-6}$。这验证原完整 2575 区间的继承组装接口；要求几何对象没有构造，原区间后台和角后端计算计数均为零，完整源界与原报告相同，转移后的精确有理数与既有 closed-budget 相同。它没有改善全域 M12 的上界。

待静态审查后可运行以下命令；输出名称是新文件，不能覆盖已存在结果：

```sh
python scripts/db6f-audit-prefix-angular-metric.py \
  --geometry notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json \
  --target notes/2026-11-09-db6f-root-flat17-m12-target.json \
  --baseline notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01-metric.json \
  --bridge notes/2026-11-09-db6f-root-exact-bridge-m12.json \
  --intervals 0 74 --budget 1e-8 --initial-arcs 128 --max-depth 1 \
  --out notes/2026-11-09-db6f-audit-prefix-angular-local-fixture.json

python scripts/db6f-audit-prefix-angular-metric.py \
  --geometry notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json \
  --target notes/2026-11-09-db6f-root-flat17-m12-target.json \
  --baseline notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01-metric.json \
  --bridge notes/2026-11-09-db6f-root-exact-bridge-m12.json \
  --budget 1e-6 --initial-arcs 128 --max-depth 1 \
  --out notes/2026-11-09-db6f-audit-prefix-angular-inherited-fixture.json

python scripts/db6f-audit-prefix-angular-fixtures.py \
  --local notes/2026-11-09-db6f-audit-prefix-angular-local-fixture.json \
  --inherited notes/2026-11-09-db6f-audit-prefix-angular-inherited-fixture.json \
  --old-local notes/2026-11-09-db6f-audit-m12-prefix-metric-budget.json \
  --old-global notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01-metric.json \
  --closed-budget notes/2026-11-09-db6f-root-closed-budget-m12-critical-r01.json \
  --out notes/2026-11-09-db6f-audit-prefix-angular-fixture-check.json
```
