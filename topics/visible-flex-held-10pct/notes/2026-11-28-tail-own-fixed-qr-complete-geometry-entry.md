# own fixed QR 终场：完整半径、绝对 placement 与闭图几何入口

可信度：**已完成来源适配及源码编译/CLI 实核；尚无本入口的真实 fixed 阳性场或连续证书。** 本条没有重算旧 R90 场，也没有把 QR 首锚贴成固定度量精化返回。

## 1. 实际缺口与新入口

已有 [fixed Cartesian reader](../scripts/resume_20261128/analytic/qr_fixed_actual_cartesian_prefix.py)、[fixed 完整图](../scripts/resume_20261128/analytic/qr_fixed_actual_closed_map.py)、[fixed 完整尾生产器](../scripts/resume_20261128/tail/qr_fixed_complete_tail_geometry_chunks.py) 和 [fixed prefix 连续入口](../scripts/resume_20261128/analytic/qr_fixed_actual_prefix_continuous.py) 能消费自己的真实模型返回。旧 anchor 专属半径/placement/全图几何入口仍要求 `actual_lambda_one_qr_chord_final_physical_height`，不能据此消费 own fixed 返回。

新增单一独立文件 [qr_fixed_geometry_entry.py](../scripts/resume_20261128/tail/qr_fixed_geometry_entry.py)，包含 `radius / placement / definition / geometry` 四个子命令。实际 source kind 为

```
accepted_original_support_qr_anchor_fixed_metric_actual_dn_physical_height
```

模型 KIND 仍来自原 `qr_fixed_support_actual_model.py`，没有修改任何 numerical run、height reference、native packet 或原证书。所有四个阶段先走 `accepted_fixed`，然后才从其 `fixed_problem.original_repository` 选择原 geometry provider；原树与当前树的已审数学源须逐字 SHA 相同，已有缓存若属于另一树则拒绝。完整 `fixed_problem`、字面 frozen profile、物理 quintic、原祖先来源、实际 mean count/GL6、final physical-H bytes 和全部 native/spectrum 来源都由原门保留。

## 2. 各阶段的实际范围

### `radius`

调用原完整 `validate_inputs` 及 own `load_complete_tail`，重验该新场全部段、全谱、共同均值、公共两jet和 canonical index。final H 只能是 own `view.height_reference` 的 `candidate_H`，且必须正好属于同一完整 packet、runtime 和实际 port。没有 raw-H 替代、没有 factor 缩放。

随后直接调用已审 radius helper 的精确 binary-rational 转换和方法哈希核验，并使用原 `ActualCutTarget.perturbation_radius`。只有实得字面 $c=R_c$ 才输出全带 $r(R)=R$、$r'=1$、$r''=0$。若差非零，保留真实非恒等状态并退出 2，不截断差值。四个 evaluator 调用只是公式执行检查，证明根据仍是精确有理差为零，不根据有限采样推断。

### `placement`

直接执行冻结 [tail_actual_placement.py](../scripts/resume_20261128/tail/tail_actual_placement.py) 的原 `main()`；所有逐段几何回执、deep collar、平盘、normal 差、support、radius、K 的计算和门完全复用。只把 `actual_height()` 中原 raw 来源段换成真实 fixed source/table/cut/full-H 门。其余 literal cut 零模、全尾零模、原 R58 积分、primitive cut anchor 及完整高度数学后缀原字节保留。

特别地，同图的

$$
z_b=z_{\rm cut}+\mu_{\rm cut}
$$

取自实际 `exact-defining-jets.npz` 和完整 global mean；不拿 query 小数当精确高度，不重置零模，不搬旧 mean1168。原 K<10 分配为 false 时仍在输出中保持 false；新完整 K<12.3 门另核。新生成的高度/summary 明确记此 adapter、原执行 main 和替换段哈希，历史原 JSON 不改。

输入 `--original-summary` 须依次给真实 complete pipeline 的 `component_certificate_summaries`，即原 certifier 实际写出的 component summary；不要把 pipeline 合并 summary 假当单段 certifier 输出。

### `definition`

实际调用已冻 own fixed `load_closed_map`：完整 finite tail、整个均值、原真实 cut Hermite、相同 phase chart、正短柱和默认 canonical R67 帽都属于这一实际返回。输出 `definition.json` 和重新核验的完整 node index，明确这是构造合同，未作连续 metric/reach 认证。

此阶段不为模仿旧 query schema 而增加采样。仅原 `PhaseAngleChart.report()` 自带的三项插值诊断转为普通 float 以便 JSON 显示；准确有理 chart 界原样保留，转换不作为向外舍入界。帽仍是已冻 `r=a/2` 默认正幅度，没有接 R89/R96 更大帽，也没有改变最终 frozen g。

### `geometry`

先严格对齐 own fixed cut/placement/radius/definition、原 complete finite/deep summary、同 packet、同 source、同 mean、同常量/normalization、同实际 cut width 和完整 node index，再从冻结 [QR 全图几何源](../scripts/resume_20261128/tail/qr_closed_map_marker_cylinder_geometry.py) 的原 `main()` 提取并执行**完全相同**的 width、chart、帽、柱、radius、support、K、D、reach 标量段。该段字节 SHA 为

```
9d2e31c91fa81858480883b527caceeb22ed43fa5e7018346a3903c9cf0be587
```

没有复写这些公式，也没有继承旧数值。输出保留原全相位 C²、正支撑嵌入和 reach 的数学职责，并带独立 own-fixed schema。明确相位用 `--phase-end`；R87 应传 `4/5`。这不替代准确 held arc/10% 位移、Euclidean 非全等或精化极限的额外义务。

## 3. 可执行接线

下列变量均是将来**实际接受返回和实际生成 summary 中的路径**，不是预造接受文件；`fixed_run` 不能填 anchor run。各 output 必须是新的 scratch 目录。

```bash
python scripts/resume_20261128/tail/qr_fixed_geometry_entry.py radius \
  --source-run "$fixed_run" --geometry-bundle "$bundle" \
  --constants "$constants" --normalization-certificate "$normalization" \
  --outdir "$radius_out"

python scripts/resume_20261128/tail/qr_fixed_geometry_entry.py placement \
  --source-run "$fixed_run" --geometry-bundle "$bundle" \
  --constants "$constants" --normalization-certificate "$normalization" \
  --cut-summary "$cut_summary" --radius-identity "$radius_out/radius-identity.json" \
  --original-summary "$component_0" --original-summary "$component_rest" \
  --disk-reserve-mib 128 --outdir "$placement_out"

python scripts/resume_20261128/tail/qr_fixed_geometry_entry.py definition \
  --source-run "$fixed_run" --geometry-bundle "$bundle" \
  --cut-width "$actual_width" --cylinder-half-length "$actual_half_length" \
  --outdir "$definition_out"

python scripts/resume_20261128/tail/qr_fixed_geometry_entry.py geometry \
  --source-run "$fixed_run" --cut-prefix-report "$cut_summary" \
  --placement-report "$placement_out/summary.json" \
  --complete-original-certificate "$complete_tail_summary" \
  --complete-map-definition "$definition_out/definition.json" \
  --phase-end 4/5 --outdir "$closed_geometry_out"

python scripts/resume_20261128/tail/closed_map_complete_metric.py \
  --closed-geometry "$closed_geometry_out/summary.json" \
  --finite-tail-metric "$complete_same_field_metric" --outdir "$closed_metric_out"
```

命令以课题目录为工作目录；component 数量按真实 complete summary 调整，不能假定永远正好两个。最后直接复用既有 complete metric collector 的全部 18460 类实际库存检查机制，实际 span 总数由该新 manifest 决定；没有固定为旧 1152/18460，也没有重算已通过的原 span。

## 4. 本次真实执行记录与限制

- 新源成功编译；四个子命令 `--help` 都真 exit 0。
- 在隔离命名空间只编译原函数定义，实核唯一来源段替换及原 main 身份；原完整高度数学后缀哈希、原 main 哈希和生成函数哈希见同名 JSON。
- 几何完整标量段实提取并成功编译；未调用它计算任何假输入。
- 未执行 `accepted_fixed` 阳性门、未构造新完整包、未发 native 调用、未重算旧区间/old q=.06 场。

实际小记录在 scratch `held10-tail-preparation/own-fixed-geometry-entry-20261128/preparation.json`；仓库只存 [源码/参数/哈希小记录](2026-11-28-tail-own-fixed-qr-complete-geometry-entry.json)。当前真实主线仍须先达到 λ1，然后完成真正 final physical-H 的完整 DN，才能使用这些入口。
