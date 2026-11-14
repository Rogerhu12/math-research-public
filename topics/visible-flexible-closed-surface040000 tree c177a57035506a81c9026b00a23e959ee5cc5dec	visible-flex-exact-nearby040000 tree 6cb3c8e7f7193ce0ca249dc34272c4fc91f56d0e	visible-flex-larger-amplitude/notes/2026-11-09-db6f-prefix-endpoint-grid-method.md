# 恢复端点网格：最小 exporter 扩展与纯背景计划

2026-11-09，`/root/coupled_prefix`。**已实施并实际完成 profile/grid-only 计划；尚无新 M15 曲面、manifest、source metric 或 full XYZ 结果。** 只读的 source/节点初审已由 `tail_theory` 通过，完整独立 plan 重放另行记录。当前使用已闭 $s=.25$ 的真实 M15 warm，仅提供同一物理背景和 stage 布局，不把它称为完整 M15 联解。

## 1. 冻结来源与最小变化

基线 `scripts/db6f-tail-critical-increment-export.mjs` 保留原字节，SHA256
`89307bf2ca1b191c9a6850227d597325ec3c1923e2b8067a20bea58991f82175`。
新文件为 `scripts/db6f-prefix-endpoint-critical-increment-export.mjs`，SHA256
`993dc6a180b917132d8284fae6c6366b45dddd883f9c09ab50b2b1dcf87f593b`。

原 `criticalLayers` 与 `makeGrid` 两个函数整体逐字不变；它们产生旧均匀节点、源分段点和内部 critical 节点。新 wrapper 只在这些旧节点上追加指定恢复起点的节点，并检查原节点子集、0/1、有限性和严格递增。每个 stage 保存旧/新 source-$x$ 节点的 little-endian float64 SHA256。

从 `const view=new DataView` 开始的原代码——精确增量和/径向归一、Fourier 提取、局部 RK、stage Fr 补偿、quartic Fr 积分表示、实际图采样、分片和 collar——在删去新增的单行 `report.settings.endpointRatio=endpointRatio` 后与基线**全文逐字相同**。局部径向积分公式也保留原式，仅增加非有限增量拒绝门。没有修改 N/Fourier 阶/数据分片/差分步长的默认值或这些公式。

新增 `--endpoint-ratio` 是显式选择：省略它时不产生端点节点；现有合法 critical 网格的节点与原式逐位相同。传入时要求 `--grid critical` 且 `criticalCells` 含 0，比例在 $(0,1]$。初档命令显式使用 `.025`，避免默认隐含变更。

## 2. 标签选择、尺度与节点定义

只选择满足
$$
\text{rawCell}=0,\quad\text{rawSegment}=7,\quad\text{rawLeft}=0
$$
的唯一 stage。代码没有硬编码 stage 7、stage 15 或某个近似物理半径。实际 p8 布局将该标签定位到 stage 15，raw profile 区间为 $[0,1/8]$。

对当前 stage 的原背景 profile，计算浮点提案量
$$
w(x)=\exp(\log w(x)),\qquad
k(x)=\frac{|w(x)(\log w)_x(x)/r_x(x)|}{(1+w(x)^2)^{3/2}}.
$$
先检查所用 profile 的值有限、$r_x,w>0$、$k(0)<.5$。按旧单 stage 实验的相同规则，从 $2^{-24}$ 开始倍增距离，寻找第一对采样括点跨过 $k=3$，再二分45次；中点给尺度 $\lambda$，要求 $10^{-10}<\lambda<1/4$。记录初始/最终括点、两端曲率和迭代数。

这只是决定节点的数值启发式；“第一对倍增采样括点”不被升级为严格证明的第一次阈值穿越，也不是源 ODE 或插值误差界。没有把旧 p4 的近似尺度当成新定义常数。

对 $\rho=.025$，顺序提出
$$
x_k=\lambda\operatorname{expm1}(k\rho),\qquad k=1,2,\ldots,
$$
只加入严格在 $(0,1)$ 内、有限且比前一个新增点大的值。与全部旧节点取并集，去除相同 binary 值，排序；保留 0、1 以及每一个原节点。非选中 stage 不追加节点。

## 3. 已实际完成的纯背景计划

输入 `2026-11-09-db6f-prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz`，SHA256
`07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5`。它是原 $M=15,N=256$, depth12、p8/steps32 的真实 $s=.25$ warm；本次只用其参数与 `rawNode` 布局。

plan 命令显式记录 depth8、内段基本32、raw0基本64、内部 critical ratio .05、endpoint ratio .025、flow-steps32；angular512、degree192、差分步长 $5\times10^{-5}$ 采用最终最小流程规定的导出配置。**这些角向选项在本次 plan-only 运行中没有触发 engine、root、RK 或 Fourier 求值，不构成 N512 真求解。**

工具会话 95074 实际自然 exit 0。结果：

| 项目 | 实际值 |
|---|---:|
| stage 总数 | 576 |
| 按共享端点计的提案节点总数 | 21031 |
| 选中标签 | raw0 / segment7 / rawLeft0 |
| 实际 stage / rawRight | 15 / .125 |
| profile 重算 $\lambda$ | .08071321815181332 |
| 选中 stage 旧/新节点数 | 65 / 168 |
| 新增互异节点 | 103 |
| 选中 stage 最小 source-$x$ 跨度 | $1.4141513827392593\times10^{-5}$ |
| 其余 source-$x$ 节点 hash 保持的 stage | 575 |

完整计划为 `2026-11-09-db6f-prefix-endpoint-grid-m15-quarter-p8-r0025-grid-plan.json`，408183 bytes，SHA256 `0a028f17f2d0b7e310ff94205dd8ffd540d7f67532c85d6959b37593f469259e`。其中保存全部 stage 节点身份与目标 stage 的完整旧/新节点；数据没有读入对话。

`scripts/db6f-prefix-check-endpoint-grid-plan.py` 的只读检查实际 exit 0：独立用 Python 的 LE64 packing 重算选中 stage 两个节点 hash；检查严格排序、原节点精确子集和端点。它还核对27项物理参数与旧 M12 真 CP 相同、全部背景构造 `physicalStats` 与旧 M12 critical 计划逐值相同，以及原网格函数和后半公式的字节身份。

这说明本次没有改动冻结背景、calibration 输入或其生成器；不是新的背景区间证书。所有 stage 的原 local radial increment 公式仍被执行并拒绝非正/非有限值，但没有输出实际曲面系数。

## 4. source 网格不变与最终物理图不变的区别

上表中“575 stage 保持”仅指 source-$x$ 节点。细分 stage15 后，独立数值径向积分的分割可能改变其 binary 增量的精确和，随后原归一
$$
\beta=\frac{r_{\rm out}-r_{\rm in}}{\sum_i\ell_i}
$$
也可能微变。因此不能从本计划推断其他 stage 的最终 physical-$r$ 节点、Fr 系数或完整图逐字不变。

plan-only 在 dyadic 归一前退出。本次没有支付新实际图的锚点恒等、共享两 jet、metric、曲率、reach、collar 或固定 $g$ 收敛。真正完整 M15 前缀及其最终真实 audit 尾成功之后，才能据最终 CP 导出新图并执行该图自己的验证。旧 M12 的局部二阶改进也不能直接转用为新 M15 的误差数值。

## 5. 可复现入口

在本题目录执行，需更换未使用的 output stem：

```bash
node scripts/db6f-prefix-endpoint-critical-increment-export.mjs \
  notes/2026-11-09-db6f-prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz \
  notes/2026-11-09-db6f-prefix-endpoint-grid-m15-quarter-p8-r0025-NEW \
  --source-root repro/source-root --depth 8 --steps 32 \
  --angular-nodes 512 --degree 192 --difference-step 0.00005 --flow-steps 32 \
  --grid critical --critical-ratio 0.05 --critical-cells 0 --critical-base-steps 64 \
  --endpoint-ratio 0.025 --audit-angular-nodes 128 \
  --audit-fractions 0.25,0.5,0.75 --plan-only
```

只读原计划检查：

```bash
python scripts/db6f-prefix-check-endpoint-grid-plan.py \
  --output notes/2026-11-09-db6f-prefix-endpoint-grid-plan-check-NEW.json
```

原 plan 已闭后，创建 checker 的首次写入因磁盘可用空间为0失败，仅留下该新路径的0字节文件；它从未作为有效源码或成功结果使用。root 清理自己的可重建 Git 对象并确认空间恢复后，才补写完整 checker 并实际运行。原 plan/source 字节没有改变；这是记录写盘阻塞，不是数学或网格失败。具体观察与闭件身份在配套 execution/publication JSON 中保存。
