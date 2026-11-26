# run05 实际17/18：只改原H字的完整 normal 入口仍在首次场读失败

日期：2026-11-26。原证据是公开 Actions [45870334713/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45870334713) 的实际17科学与18完整纯归因；[第5卷](2026-11-26-public-actions-45870334713-1-part-005.md) 已实际返回，亲读 Git blob `2d8a10f76d6dda7d4f435245d9dc761643102ae6`。没有本地科学执行，也未经connector整读533KB report或452KB pure结果。

## 1. 实际结论

完整32阶段共同分割normal算法在替换H后的真实原初点上完成29阶段，第30阶段没有让每个角返回原阶段方程，首次场读失败。实际17 failed/1，18完整pure completed/0；metric/restoration方向及各accepted均0，最终原endpoint没有复读，未生成初/末场bundle、Phi、metric max或几何g。

这与15原H完成26阶段、在27失败是两次实际返回的区别；不能将“完成更多离散阶段”冒作metric改善、连续可达性或已满足闭合。两次都没有完整初始场，且后继仍须支付原endpoint、全角、metric和真几何责任。

## 2. 显式单坐标输入确实采用

实际reference bundle `59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f`，原reference初点SHA `cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3`。原H字`0x1.f27228dabd944p+0`，此次采用`0x1.ec0bc59b655d2p+0`，精确有理值`4328082246413033/2251799813685248`；新完整初点SHA `efe12015c07babb2ebe02ca2f9689faa2433e37485249610ee7126a07ba8bd93`。

非H摘要前后完全相同：`f92b24aa8cfddc5ccc0dfc9c620a1464022f09aa34b4e125f4d2e4b096ddcb6c`。actual_original_initial_verified=true、root_cache_empty_before_height=true、nonheight_byte_identical=true，initial_point_mode为`explicit-height-fresh-original-reference-seed`。此固定采用字来自已登记观察，literal_is_current_reference_integral_claimed=false；没有重命名成05当前精确Jstar或Istar。

完整normal模型在改H前后均为`a796b40802022f1d72717d227f417c4741b2a20f3c9e616540a86ba17c603a03`；固定scalar身份`e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`未变。当前Q definition `976f9ad62cb67e36a7aa9c8a755671d4e815cbea01af28ace3b31e2031c54452`、18个常量字、wide bubble与gamma支持、norm、全部自由变量和外预算均保。输入绑定仍先核原base.initial，之后才显式改当前自由H。

## 3. 完整空间、历史及实际根工作

原变量1,333,370，全正权metric行45,324,288；6controls、每normal增量3维，每阶段角隐式9维，metric维192、sixjet维288。32个共同精确节点首0末1，common_partition=true、per_angle_adaptation=false、stationary_KKT_selection=false、exact_ODE_solution_claimed=false。控制球2，原endpoint容差2e−12，全部原根/线筛参数和旧真实几何阈值未放宽。

本次消费reference locations及本run实际3/17/21/26/30的完整报告，并加入本run gamma-H12与原H normal15两个实际失败报告，共8个明确manifest输入；这些名称中的3/17/21/26/30是重建路线标签，实际05编号分别3/4/5/6/8。所有适用永久地址保留，初始curvature/radius各1851；不单凭计数相同宣称集合等号。

实际17记录：

| 项 | 实际值 |
|---|---|
| failure reason | A declared fixed normal plane did not return every original stage equation |
| failure_stage / completed_stages | 30 / 29 |
| requested angular order | 1 |
| final_original_endpoint_reread | false |
| final_original_endpoint_passed | null |
| 当前已完成root | 0 |
| root failure / jet upgrades | 1 / 0 |
| current grid roots / second jets | false / false |
| closure jet角求值 | 4832 |
| frame reverse角积 | 1440 |
| stage equation角求值 | 4352 |
| stage matrix角求值 | 1040 |
| stage angular matrix角求值 | 0 |
| 3×3solve attempts | 1026 |
| 隐式solve attempts / matrix角行 | 0 / 3120 |
| stage root attempts / successes | 240 / 232 |
| stage Newton updates | 786 |
| stage backtrack evaluations | 1560 |

不能将已完成root=0误写成没有尝试Newton；完整阶段与逐角成功数也不是同一计数口径。18 bound_snapshots=1、cross_point_backfill=false，current residual/controls及所有场统计null。现有公开compact没有第30阶段逐角残差/矩阵/具体触球归因，不能猜其数值失败种类。

## 4. 完整实际来源、输出与耗时

| 角色 | 完整SHA256 / 提交 |
|---|---|
| 科学17 source commit | `429b7a0cc9f73ff88971cd87ee7591927d0cfcdb` |
| launcher | `b7e56936ba3746fe44c5322464d9c391670df2ea529448132b5c4fbf0018e9f2` |
| driver | `e8e096f9a2a2acd5b08e907aa2b9df1fc9a402d033f67e1420f072dc579c6fe7` |
| endpoint | `42ea8ec5920e3815b99c83c41448efb38ee37860f4d9362ddea6bce2418d39fe` |
| geometry | `255760e188d13f22ffef86c029f35f5d1629384411d2e32f03f75df60f4ab71c` |
| new input binder | `ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39` |
| base | `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf` |
| 纯18 source commit | `19e9fc9dfed3e30b9079789427dd1561104c9abf` |
| 完整reader | `f8261f971d7993534d7e020efaef5ca480c51ba2d2da7861d18e6a18d2af799b` |

科学目录`zero-closure-fixed-normal-lift-explicit-H-first`：report SHA `a89f220415bc5d5e170fea8646a8af30fc206895e1f7087799b5e6a9ae1865b7`，533,538字节；command SHA `dc93c062f7b41010eb1cb036ba995a3ec30d6f138cf5dab7cb2209733b23f4be`，17,331字节。pure18输出 SHA `08dbad61ad19ab477a771fc0d3328584e2bbd82ca6b46d3519aee80ec7ff5055`，452,206字节。大raw只由runner完整pure消费，公开卷保必要紧凑字段。

17控制器20.80212606799978秒，driver18.734408999998777秒、峰RSS1,087,096KiB；18耗时5.803280145999452秒。17预设3个final字段缺失与实际首次场失败一致；18 summary_errors/missing_outputs均空，以明确null/零方向解释，没有把未产final补为成功。

本条只登记这个准确H输入、完整common-partition算法和真实初读失败。没有删除历史、改变固定g或松题目完成标准；后继supported-unit seed与direct integral完整方向各自继续原责任。
