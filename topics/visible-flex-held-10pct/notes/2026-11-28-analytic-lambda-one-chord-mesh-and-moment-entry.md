# 真7a耦合场的完整网格与活动矩接线；固定g后继边界

2026-11-28 UTC。为让同一冻结 runner 在真正 λ=1 原7a full-DN/8outer 返回后继续使用实际场，新增两个独立来源入口。旧 exporter、活动矩源、memo reader 和任何已执行源保持字节不变。两个新源已实际语法编译通过；没有假造 λ=1 输入、执行接受门、求值网格/积分或追加数值测试。

## 网格

`analytic/chord_export_actual_closed_mesh.py` 明确导入 `chord_actual_closed_map.py`，其 map SHA 与7a接受 provider列入来源记录。`--coupling-summary` 必填；源种类明确为 `actual_lambda_one_chord_final_physical_height`。其余真实 packet、原 background/完整谱、full-height/共享节点门、ring连接和极点拓扑、全谱向量位置、held frame符号、精确有理t、double PLY与每文件严格小于5,000,000字节的代码均保留。

真正完整尾 bundle 到位后，在同一冻结数值树中调用：

```bash
python -u @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/chord_export_actual_closed_mesh.py \
  --source-run @WORK@/lambda-one-actual-dn-01/actual/run.json \
  --coupling-summary @WORK@/lambda-one-actual-dn-01/summary.json \
  --geometry-bundle TRUE_COMPLETE_SAME_PHYSICAL_HEIGHT_BUNDLE \
  --frame held --cylinder-half-length .0025 \
  --times 0 1/4 1/2 3/4 1 \
  --outdir @WORK@/lambda-one-complete-meshes
```

有限网格仍只是已定义整图的可再生采样；所有metric/reach/held/非全等/完成标记保持false，不能靠成功导出晋级数学证明。

## 活动矩

原 `cartesian_third_activity_moment.py` 静态导入memo-only连续入口，故新增 `analytic/chord_cartesian_third_activity_moment.py`，仅把该 import 指向 `chord_coupled_prefix_continuous` 并使 `--coupling-summary` 必填。其完整三jet场提取、原两个连续求积余项、三重/上下反射因子、核心及短柱公式全不改。它只接受由同一个7a连续入口产生的真实本场 tables；有完整尾时传 `--bundle` 支付同一全cut项。它没有借用此前 λ=.064 的实际积分区间。

```bash
python -u @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/chord_cartesian_third_activity_moment.py \
  --tables TRUE_SAME_CHORD_PREFIX_TABLES \
  --coupling-summary @WORK@/lambda-one-actual-dn-01/summary.json \
  --bundle TRUE_COMPLETE_SAME_PHYSICAL_HEIGHT_BUNDLE \
  --radial-parts 1 --outdir @WORK@/lambda-one-complete-prefix-third-moment
```

尾矩的严格粗界仍需要该实际尾自己的完整几何、投影单射与Z/r_star界；网格或这份接口不能替代它。

## 固定g实际DN精化尚需独立模型合同

这里不是另一个memo-only import问题。当前 `fixed_support_literal_driver*` 从真正线性Robin原R53设计或自己已经接受的固定support前缀接入；不能把 `actual_tail_requested=true` 的7a结果伪装成线性锚。旧 `warm_actual_dn_refine_model.py` 与配套step/acceptance/compare/pipeline明确只认v2/v3 phase未知族、lambda1与mean1168，不能只改KIND或放宽一个判断接原support族。

最小诚实后继必须定义原support fixed=True的独立actual-DN模型：由本条7a接受门取得实际锚，冻结最终physical δ、λ、完整profile/bridge/tail、字面chart/gauge/warp与mean_N；把原加性δ设计参数改为 `log(q_aux/q_seed)`，原完整support控制与每阶exact lift仍为未知。首次转接保全真实raw节点/全部state/pscale，原δ冻结在目标g中，而非丢失其变化。外端继续原完整H/J/audit及八次outer，原q分支、RMS/BC/metric门仍须实际支付。

随后必须有独立接受器、频率/径向/时间精化控制器与同g完整六jet/尾C²比较，明确固定源mean不随M偷偷改变。现有原support固定前缀model、字面chart修复、完整lift与原actual-DN外迭代可复用；这不是本次两份来源文件已实现或已运行的功能。当前新增文件没有修改这个数学缺口，也没有把设计δ变化称为固定g精化。
