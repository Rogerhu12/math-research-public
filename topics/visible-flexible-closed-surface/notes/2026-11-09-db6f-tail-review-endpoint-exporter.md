# 恢复段端点网格扩展独审

审查者 `/root/tail_theory`，2026-11-09。**PASS：小差分源码、真实背景网格提案及一次独立 plan-only 重放。** 没有产生实际新曲面 manifest，没有 angular root、RK、完整导出或连续 metric / 曲率计算。

受审源为 `scripts/db6f-prefix-endpoint-critical-increment-export.mjs`，SHA256 `993dc6a180b917132d8284fae6c6366b45dddd883f9c09ab50b2b1dcf87f593b`。作者为 `coupled_prefix`；审查者没有参与这个扩展实现，但此前实现过其冻结基底 `db6f-tail-critical-increment-export.mjs`，SHA256 `89307bf2ca1b191c9a6850227d597325ec3c1923e2b8067a20bea58991f82175`。因此本审查支付新差分与新提案，不将旧基底的作者自审冒充独审。

## 1. 选择器和数值层宽

新增参数 `--endpoint-ratio` 必须为有限正数且不超过 1；只允许 `grid=critical` 且 critical cells 含 raw cell 0。启用时恰有一个 stage 满足 `rawCell===0 && rawSegment===7 && rawLeft===0`，否则拒绝。它不依赖旧 M12 的 stage 7 编号或某个近似半径。

该 stage 的 profile 给出数值子午曲率
$$
k(x)=\frac{|w(x)\,\partial_x\log w(x)|}
{r_x(x)(1+w(x)^2)^{3/2}}.
$$
实现逐次要求读到的值有限，$r_x,w>0$。只有 $k(0)<.5$ 才从 $2^{-24}$ 起倍增寻找 $k\ge3$ 的括区，再作 45 次二分；最终宽度参数 $\lambda$ 必须在 $(10^{-10},1/4)$ 内。代码把它明示为数值括区提案，没有宣称严格首个交点、单调性、唯一根或源 ODE 误差界。

新增的单向节点为
$$
x_j=\lambda\operatorname{expm1}(j\rho),\qquad 0<x_j<1.
$$
每个提案须有限、严格大于前一个；循环必须实际到达右边界，否则拒绝。节点与原列表取并集后再排序，保存原节点子集、端点 $0,1$、严格递增及有限性检查。旧 `criticalLayers` 和 `makeGrid` 函数逐字未变；未启用端点参数时，原合法 critical / uniform 节点不变。

## 2. 径向增量与后半表示

每个新相邻源节点之间仍使用原 entry 积分，形成独立 binary64 未缩放径向增量；除原正值检查，新版显式拒绝非有限增量。审查者的完整 plan-only 重放实际重新计算了所有这些增量并通过检查。没有把两条接近的显示半径相减来定义长度。

从 `const view=new DataView` 开始，去掉唯一新增的 `report.settings.endpointRatio` 元数据赋值后，新旧源码余文逐字相同。因此 dyadic 精确累加 / 全局归一化、packed Fourier 槽、Fr 的端点与物理中点匹配、RK、stage 迹修正、共享节点、collar 和采样诊断的公式都未被本差分替换。

若未来执行完整导出，原正长度与精确归一化机制继续定义真实物理网格，并由原共享 Fr/Frr 机制定义 C² 图。但本次 plan-only 在 dyadic 归一化之前退出，没有创建那个新图，也未验证其实际数据、锚式、接缝或误差。

尤其，添加一个 stage 的积分分割可能改变浮点未缩放长度的总和，从而改变
$$
\beta=\frac{r_{\rm outer}-r_{\rm inner}}{\sum_j\ell_j}.
$$
所以“其余 575 个 stage 未变”在本报告中只表示其 **source-x 节点哈希**未变，不能推广为最终物理 $r$、Fr 系数或曲面位置逐字不变。背景 $g$ 的物理定义没有因此改变；新图依赖扰动的连续证书仍须重算。

## 3. 真实输入与独立实际重放

输入为真实已闭的小振幅 M15 尾 `prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz`，SHA256 `07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5`。其作用仅是提供同一背景参数和 staged layout；它仍是 $s=.25$、未做最终 audit 的 warm，不能升级成目标或前缀解。

审查者用冻结 `repro/source-root`、D8、深部每 stage 32 步、raw0 base 64、critical ratio .05、endpoint ratio .025、N512、K192 执行唯一一次独立 `--plan-only`；工具 session 80390 实际自然 exit 0。输出文件 `2026-11-09-db6f-tail-review-endpoint-grid-m15-quarter-p8-r0025-grid-plan.json` 与作者文件逐字节相同，SHA256 为 `0a028f17f2d0b7e310ff94205dd8ffd540d7f67532c85d6959b37593f469259e`，408183 bytes。

| 检查项 | 实际结果 |
|---|---:|
| staged profile 数 | 576 |
| 拼接 source-x 总节点数 | 21031 |
| 唯一变化 stage | 15，raw0 / segment7 / rawLeft0 |
| 该 stage 原 / 新节点数 | 65 / 168 |
| 数值层宽 $\lambda$ | .08071321815181332 |
| 其余 source-x 哈希相同的 stage | 575 |
| angular root / RK / 完整导出 | 0 / 0 / 0 |

审查者还直接从保存的两组 stage15 二进节点重算 little-endian float64 SHA256，用 Fraction 检查全部相邻差为正、旧节点为新节点子集、两端恰为 0 和 1，并核七个 plan 来源文件及实际 checkpoint 的哈希。最终数值括区端值确满足低端小于 3、高端不小于 3；这仍只是一项数值诊断。

新 plan 与正式旧 M8 manifest 的 `physicalStats` 逐字段完全相同；三份共有物理构造 / subdivision 源哈希也相同。参数差异恰为此前独审允许的十二个数值 / 运行字段，没有新的物理变化。检查器 `scripts/db6f-tail-review-endpoint-plan.py` 可重放上述文件 / 字节 / Fraction 核查，不重建 profile 或求解任何流；输出 `2026-11-09-db6f-tail-review-endpoint-plan-check.json` 的 SHA256 为 `37a6df2955d8d55ccad75901510649b1820cf846c337533fcbe892b854510c7b`。

## 4. 复现命令与未支付项

独立 plan-only 的完整参数如下；输出前缀必须换成尚未使用的新名：

```bash
node topics/visible-flexible-closed-surface/scripts/db6f-prefix-endpoint-critical-increment-export.mjs \
  topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz \
  topics/visible-flexible-closed-surface/notes/REVIEWER-NEW-ENDPOINT-PREFIX \
  --source-root topics/visible-flexible-closed-surface/repro/source-root \
  --depth 8 --steps 32 --grid critical --critical-ratio 0.05 \
  --critical-base-steps 64 --critical-cells 0 --endpoint-ratio 0.025 \
  --flow-steps 32 --angular-nodes 512 --degree 192 --difference-step 0.00005 \
  --audit-angular-nodes 128 --audit-fractions 0.25,0.5,0.75 --plan-only
```

现有提案只消除了此前没有端点节点的接口缺口。它没有支付源 Galerkin / RK 重求误差、最终联解、实际新 XYZ 图的表示收敛、R6 collar 数值、公共 cut、连续 metric / 曲率 / reach 或最终未参与优化者复核。任何正式新图都必须按它自己的 manifest 和同一背景重新完成这些检查。
