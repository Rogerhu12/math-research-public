# R686 分批 K 与实际完整 first-geometry 的同场合并入口

2026-11-26，Astra-larger-e4e2a2bf-20261126 / geometry（AI 辅助）。

**状态：只完成源码、参数和报告接口的静态审查，没有运行新的场证书。** 这个工作补齐 R686 的实际消费链，不另立几何定理，不把未运行的条件写进 R666。当前百分之一量级的旧/新设计场不应为了填表反复运行昂贵完整 K；先继续真实求解，待接近要求的实际新候选返回后再调用下面入口。

## 1. 保留已有实际跑通的完整 first 入口

公开 [44758209061/1 stage37](2026-11-20-public-actions-44758209061-1-part-003.md) 已有 canonical R671 父 `7fd352757ca69554b367f08c6a76f343729aef795f68f218e202e2cacd933c21` 的实际完整 first 返回：冻结源 `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225`，本体 `60.314219527001114` 秒，完整阶段 `66.27338581200092` 秒。它不是后来候选的证书，也不是新场耗时保证。

该返回说明先前 5h50m 超时的主要未返工作是 K，不能把完整 first 误当成同样未返。当前保留原 f122 first 的原 producer/schema，继续使用它已经支付的完整 `X,V,T`、scalar/解析尾与全域包围。这样同场 E/W² 下界可由 R686 直接复用，原 R675 非平面消费者也能按真实 first 报告身份继续工作。

将 first 与 K 的 F/V/T 大数组合并缓存，需改变实际 producer 和逐块语义，并牵连 R675 的 embedding-report 校验；现阶段没有依据为一次约一分钟的历史 first 增加这一变化。本文没有声称跨任务共享角数组。R686 已共享**经过验证的同场完整 E/W² 数学下界**，这部分不是原始数组缓存。

### 实际 first 命令

先从**实际返回的新候选**绑定 `$BUNDLE`、`$NODE_REPORT`、`$SCALAR_INPUT`、`$REFERENCE_PROFILE`，分别指其 canonical `final.npz`、准确节点报告、原 scalar input 与自己的 `exact-tail-lift-profiles.npz`。精化网格以后必须使用对应新节点报告，不能继续硬编码旧 J923 的文件。`$GEOM` 为该实际候选在 runner 上的新输出目录。

```sh
python "$TOPIC/scripts/resume_20261120/exact_reference_tail_interval.py" \
  --repo "$GITHUB_WORKSPACE" --bundle "$BUNDLE" \
  --node-report "$NODE_REPORT" --scalar-input "$SCALAR_INPUT" \
  --reference-carrier "$REFERENCE_PROFILE" \
  --mode first --cells all \
  --levels 256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96 \
  --angular-taylor-degree 12 --scalar-degree 5 --radial-block 4 \
  --panels 128 --beta 1/4 --target-support .14 --target-diameter 4.10 \
  --out "$GEOM/first.json"
```

这里 `4.10` 只是**控制同场证书继续细化的目标值**。f122 仍在每个原胞形成真实连续半径上界；其最后的 `continuous_diameter_upper` 才是后继允许消费的 D。细化计划结束而实际 D 未达 4.10 时，不得把 4.10 填入任何几何公式。

真实旧 canonical first 的 D 上端为 `4.118969405015079`，因此标记后使用 $D_m=D+2/1000$ 时，仅知道 $K\le8.1$ 不足以推出 `reach/D >= .03`。另一场 worker03 的紧 D 上界不能搬过来。这就是此处加显式径向半径目标、且下一节仍由**实际 D**计算 K 目标的原因。

当 M 增加时，上述 retained_modes 只是完整角尾的分拆位置，未舍弃高模；源码对全部未保留部分付严格尾界。若实际新场在这个有限计划下仍有未付目标，要按真实返回的未付胞继续更强的分拆/角径向精度，而非把计划结束当成证明通过。这里没有承诺新 M、任意候选在历史一分钟预算内返回。

## 2. 从已返实际 D 推导 K admission

新 launcher [launch_curvature_from_actual_first.py](../scripts/resume_20261126/launch_curvature_from_actual_first.py) 先验证实际 bundle/node、canonical model 与 f122 完整 first 的源和输入身份，再检查原 R650/R661 所需闭合、浸入、正支持与标记条件。

令实际 first 给出的完整上界为 D。准确四标记参数仍是高度 $h=1/1000$、R661 的互异支撑圆与自身诱导帽度量。由已证明的 R650/R661 公式，

$$
D_m=D+2h,\qquad \sigma_m=\min(\sigma,64/267),\qquad
K_m=\max(K,5),\qquad
\operatorname{reach}\ge\min(\sigma_m,1/K_m).
$$

因此在实际已付

$$\sigma_m\ge(3/100)D_m,\qquad 5\le\frac{100}{3D_m}$$

之后，只须令 R686 的准确目标为

$$\boxed{K_{\rm target}=\frac{100}{3(D+2/1000)}}.$$

launcher 将实际 binary D 端点按其**准确 Fraction 值**读取，直接把该有理数传给 R686 的 `--target`。没有把往返十进制 D 当成未经说明的另一有理数，没有代入愿望值 4.10，也没有默认强制旧 8.1。当前不另加经验安全因子；是否通过仍由完整外包 K 与精确阈值比较决定。

若现有正支持界不够，或仅 R661 的标记 K≤5 已使该路线的目标无从支付，launcher 明确拒绝这次昂贵 K admission。其含义是当前已给证据不足以用这组 R650/R661 界证明目标，不是证明实际曲面达不到目标。

```sh
python "$TOPIC/scripts/resume_20261126/launch_curvature_from_actual_first.py" \
  --repo "$GITHUB_WORKSPACE" --bundle "$BUNDLE" \
  --node-report "$NODE_REPORT" --scalar-input "$SCALAR_INPUT" \
  --reference-carrier "$REFERENCE_PROFILE" --first-geometry "$GEOM/first.json" \
  --journal "$GEOM/K-journal" --out "$GEOM/K-batch-01.json" \
  --budget-seconds 600 --workers 4 --radial-block 4 \
  --levels 256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96 \
  --taylor-degree 12 --scalar-degree 5 --panels 128
```

它写一个小 `K-batch-01-admission.json`，保留实际 D、标记 D、支持界、推导出的准确目标、first SHA、实际候选 SHA 与准确子进程命令；K 结果本身仍由修正后的 R686 原 producer 写出，schema/source 不被 launcher 替换。

后继使用同一实际 first 与 journal，加 `--resume` 并换 `K-batch-02.json` 等新的输出路径。R686 的预算仍是停止 admission 后让有限个在途小块自然返回，不以硬 timeout 丢掉已经算出的块。每个小批结束即可公开其 compact 覆盖域和统一上界；并不等待整个 K 通过才发表真实已付范围。

同 journal 的 first 报告身份不能悄悄替换。若另取更强 first 报告或改源/参数导致 binding 改变，必须明确处理新的身份；此入口不把旧 journal 的记录伪装为另一个输入组合。当前实际串联先把 D 支付到足够好的水平，再固定该 first 供所有 K 小批使用。

## 3. 原 R675 的同场非平面入口

完整 first 已返回后，可按原新模型证明源继续：

```sh
python "$TOPIC/scripts/resume_20261120/exact_reference_tail_nonplanarity_v2.py" \
  --repo "$GITHUB_WORKSPACE" --bundle "$BUNDLE" \
  --node-report "$NODE_REPORT" --embedding-report "$GEOM/first.json" \
  --out "$GEOM/nonplanarity.json"
```

它必须读同一实际 first 的内容 SHA，保留 v2 原有的“非零高 Z 或准确解析尾”互斥覆盖，不能把解析尾覆盖伪称为所有胞均有非零高 Z。新合并器直接消费实际 v1/v2 原报告，不改写任何 flag，也不重复计算其 q 系数结论。

没有非平面报告时，合并器仍可单独处理已付 reach/held/grip，但严格不宣称正 Euclidean shape distance；完整几何目标 flag 保持 false。

## 4. 新 compact K 消费者及准确边界

[batched_curvature_geometry_combine.py](../scripts/resume_20261126/batched_curvature_geometry_combine.py) 使用新 schema

`R686-R674-R675-exact-R650-geometry-combination-v1`。

它不将 R686 报告伪装成原 f122 curvature producer。验证包括：

1. 修正后的 R686 producer `ee3744b39bcb3183931b73f25a34ca390c523a2456737915cf359a7f1c4e7d31`，完整 R672/f122 角径向核及依赖源身份；当前真实 bundle、node、scalar/model、H/width/S/R、全部 M/J 和参数 binding。
2. `valid_cell_ranges`、`target_paid_cell_ranges` 及补集为唯一有序范围；对象版和标量 JSON 版 `uniform_domains` 一致；胞号、数量与真实 J 对应。
3. 仅在 valid 域等于全部 `0..J-2`、统一 K 有限非负、统一 E/W² 严格为正且准确帽/镜像范围均已付时，才消费完整 K。部分块、部分胞、失败块或没返回的记录不补零。
4. 若 K 使用了 optional first 下界，其记录必须指向本次实际供给的 first 内容 SHA。完整 first 按原冻结验证器重新核对，同一 bundle/model 的约束不因 compact 数据而放松。
5. R675 若提供，则必须与这个 actual first、同一 bundle/node/model 一致，且其原非平面域完整。

```sh
python "$TOPIC/scripts/resume_20261126/batched_curvature_geometry_combine.py" \
  --repo "$GITHUB_WORKSPACE" --bundle "$BUNDLE" --node-report "$NODE_REPORT" \
  --first-geometry "$GEOM/first.json" --curvature "$GEOM/K-batch-LAST.json" \
  --nonplanarity "$GEOM/nonplanarity.json" --out "$GEOM/geometry-combination.json"
```

这里 `LAST` 必须换成已经实际返回的小批文件。消费者也可在一个真实部分小批之后调用；此时完整 K/reach 保持未付，结果不会假装研究完成。

最后仅应用原 R650/R661 的准确有理公式：

$$
d_m=\min(d_{\rm witness},H-h),\quad
\frac{A_H}{D_m}\ge\frac{d_m}{D_m},\quad
\frac{\operatorname{diam}H_{\rm grip}}{D_m}\ge\frac{9/10}{D_m},
$$

$$
\frac{\operatorname{reach}}{D_m}\ge
\frac{\min(\min(\sigma,64/267),1/\max(K,5))}{D_m}.
$$

此处三项 D、K、支持及 witness 全来自被核验的**同一实际场**。R675 非平面与正 image-change witness 还同时支付时，R661 的四个不共面固定标记给包含反射分支的正 Euclidean shape distance。它没有数值商距离下界。

消费者不求值任何场、不调用 scalar oracle、不运行 Fourier transform，不重复区间覆盖；它只组合已实际返回的数学界。几何与选用哪个固定目标度量无关，所以新均值路线不需要改写这些几何式；`metric_certified`、`fixed_metric_refinement_certified`、`topic_completion_certified` 始终 false，由实际固定目标上界/求解精化另行支付。

## 5. 源码、summary 与验证范围

| 文件 | SHA256 |
|---|---|
| `batched_curvature_geometry_combine.py` | `bbcd337e4d4c486a2413b422da8b000264c6c960913b4778103a349ccd477b21` |
| `launch_curvature_from_actual_first.py` | `818eb6119d70d9aff66d0b5b199dd80670622b0fdf79e9d40eb1ff6c89af0897` |
| [resume-20261126-same-field-geometry-summary-fields.json](../computations/resume-20261126-same-field-geometry-summary-fields.json) | `0cf1037f0087e420e67d4177ebb00ba22ba07cdbb1239bc4a1b755eff8230ae5` |

两小源已作 AST 解析，summary JSON 已作语法检查。没有本地科学运行，没有新 first/K/合并数值返回。

统一 summary 文件的四个顶层 role 为 `first_geometry`、`curvature_admission`、`curvature`、`geometry_combination`。控制器把对应字典放到其实际输出文件名下即可；每个值都是已有控制器支持的点分路径，最终读数为标量，不发布 raw q、逐角/逐胞表或科学数组。first 的真实 bundle/node/profile SHA、K 与合并的独立 producer、各自完整域和准确阈值会同列发表。

旧冻结 helper `exact_reference_tail_geometry_combine_v2.py` SHA `521187ae2df4225ddbda6efd8326db760d2f1bd5bd184a74f3a816408ad19e6c` 只用于其已刊 identity/nonplanarity 验证及准确有理 helper；没有修改旧文件或把新 K 的范围改名成旧报告。所有 raw 报告与 journal 保持 runner-local，公开必要的小结和真实内容身份。
