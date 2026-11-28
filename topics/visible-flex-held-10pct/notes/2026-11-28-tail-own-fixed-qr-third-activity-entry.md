# own fixed QR 终场：原三阶活动积分、整尾通量与 R67 合并接线

可信度：**必要来源入口已实现并实际编译/CLI 核验；没有新活动矩数值或非全等阳性结论。** 不重算旧场，不改帽，不把 fixed 返回改成其 anchor KIND。

## 1. 输入合同

新独立入口 [qr_fixed_activity_entry.py](../scripts/resume_20261128/tail/qr_fixed_activity_entry.py) 接已冻 [own fixed 全几何入口](../scripts/resume_20261128/tail/qr_fixed_geometry_entry.py)，提供 `prefix / tail / combine` 三阶段。

三者首先调用真实 `accepted_fixed`，保留完整 `fixed_problem`、原实际 anchor 祖先、frozen profile/chart、q/warp、原 mean count/GL6、完整 physical quintic、同 native runtime/port 以及 **final physical-H**。来源始终是 `accepted_original_support_qr_anchor_fixed_metric_actual_dn_physical_height`。同一真 fixed source 的 complete bundle、全 tail mean、全 Fourier spectrum、同 cut width 与 canonical 帽必须逐项一致。

prefix 表格和 cut 仍由 [qr_fixed_actual_prefix_continuous.py](../scripts/resume_20261128/analytic/qr_fixed_actual_prefix_continuous.py) 的真实来源构造器产生；新入口直接使用其 `FixedActualNewMetric / FixedActualCutMetric`。`FixedActualContext.require_report` 的完整 payload/source 字节合同没有放松。

## 2. 三个阶段复用的数学

### prefix：完整 cut 前缀与 core

直接复用 [原完整 QR moment 源](../scripts/resume_20261128/tail/qr_cartesian_third_activity_moment.py) 的 field extractor、`MomentVerifier`、density、区间二阶导数、径向 midpoint 和周期角 trapezoid 误差公式、完整公共径向分割和全部累计计算。生成的 main 只更换源初始化/构造器/输出身份，并插入原 [durable leaf](../scripts/resume_20261128/tail/qr_cartesian_third_activity_moment_durable.py) 的逐叶 fsync 回执；数学循环和每叶积分不改。

每次运行必须给真实完整 `--bundle`，保留全 Cartesian cut 修补，而不是只积分未修补前缀。三阶密度仍为

$$
2z\,\operatorname{Re}(x+iy)^3\,
(X_{\psi,x}X_{s,y}-X_{\psi,y}X_{s,x}),
$$

其中 2 已计入上下反射。core 边界公式仍为

$$
m_3=\frac15\int\operatorname{Re}(x+iy)^3
(x\,y_\psi-y\,x_\psi)\,d\psi.
$$

原完整三jet、有限 mean、core lift、center 和 cut 都留在 field builder 中。没有删除均值，也没有只用入口 H 或三角截断替代完整场。`durable_entry` 明确为本次真实 own 入口，另列复用的原 storage 源；不冒称执行了旧 anchor gate。尚未有中断需恢复，故没有另搭恢复调度框架。

### tail：整尾、deep collar 与双平盘

先核 own fixed 的真实 placement/absolute-height/radius 合同与同 final physical-H，再**原样执行** [tail_third_activity_flux_bound.py](../scripts/resume_20261128/tail/tail_third_activity_flux_bound.py) 的完整 main。原 complete pipeline 的全部 finite stage、deep、平盘、投影单射、首导数和位置界必须实际已付。

仍取实际完整位置误差 $p$、$r_*=R_c+p$、$Z=H_{\rm pole,hi}+p$，以既有原公式

$$
|A_{3,\rm tail}(0)|\le\frac{4\pi Zr_*^5}{5}
$$

控制上下反射合并的完整复通量。原 $22/7$ 有理上界和向外舍入代码未改。固定帽不计入活动项；柱平移另由 $\ell m_3$ 计入，不重复加一次尾平移。

### combine：完整同图活动区间

复用 [原 QR exact combiner](../scripts/resume_20261128/tail/qr_combine_closed_third_activity.py) 的每叶准确单覆盖、每个 binary64 区间到 Fraction 的转换、准确加法及向外展示。只更换 own 来源门、实际生成 entry 身份和真实 full-map **definition** 回执字段；不伪造旧 sampled query。

准确组合仍为

$$
A_3(\ell)\in [A_{3,\rm prefix}]+[-B_{\rm tail},B_{\rm tail}]
+\ell[m_3],\qquad
\ell=2\,\operatorname{Fraction}(\texttt{cylinder\_half\_length}).
$$

不把字面 binary64 柱长强写为 $1/200$。相位区间从本场 whole geometry 读取，R87 的 $4/5$ 不会退回旧 $9/20$。若上述区间任一符号排除 0，且同 canonical 帽的准确 $B_3/\pi>0$，才给既有 R67 的完整 E(3) 非全等存在结论；若包含 0，保留 `without_separation`，继续别的真实输入/高阶方法。没有指定端点距离下界、没有精化极限或 README 完成声明。

## 3. 执行方式

以课题目录为工作目录，下列变量均从实际已接受 fixed 返回及实际证书填写，不可拿 anchor/旧 q=.06 场代入。

```bash
python scripts/resume_20261128/tail/qr_fixed_activity_entry.py prefix \
  --source-run "$fixed_run" --tables "$same_fixed_tables" \
  --bundle "$same_full_bundle" --cut-width "$actual_width" \
  --radial-parts 1 --outdir "$prefix_moment_out"

python scripts/resume_20261128/tail/qr_fixed_activity_entry.py tail \
  --source-run "$fixed_run" --placement-report "$placement_summary" \
  --complete-original-certificate "$complete_tail_summary" \
  --outdir "$tail_flux_out"

python scripts/resume_20261128/tail/qr_fixed_activity_entry.py combine \
  --source-run "$fixed_run" \
  --prefix-moment-report "$prefix_moment_out/summary.json" \
  --tail-flux-report "$tail_flux_out/summary.json" \
  --closed-geometry-report "$same_closed_geometry" --out "$activity_report"
```

所有科学数组/完整叶证明都留在 scratch，不入 Git/Release。独立新积分只属于这个真实 own 返回；同源几何、尾积分和原背景已付结论仅做严格 SHA/定义复用，不重算。

## 4. 本次实际观察

新源码编译成功；三个子命令 `--help` 真 exit 0。用隔离命名空间只载入原函数定义，实际完成 prefix 与 combiner 生成函数的编译，并记录原 main、替换的 source gate 与新 main 哈希；没有调用任何虚构阳性对象或积分。

实际 scratch 小记录：`held10-tail-preparation/own-fixed-activity-entry-20261128/preparation.json`。仓库 [同名 JSON](2026-11-28-tail-own-fixed-qr-third-activity-entry.json) 只含源、参数、哈希和真实准备执行标量。尚无真实 accepted fixed 场，因此没有本入口的实际 activity interval；下一步仍由真 λ1/final physical-H/fixed 返回触发实际原门计算。
