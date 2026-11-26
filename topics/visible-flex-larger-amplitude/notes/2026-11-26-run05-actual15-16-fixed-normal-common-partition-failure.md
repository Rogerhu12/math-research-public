# run05 实际15/16：完整共同分割 normal 入口在第27阶段首次场读失败

日期：2026-11-26。只登记公开 Actions [45870334713/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45870334713) 实际15科学返回与16完整纯归因。原公开[第4卷](2026-11-26-public-actions-45870334713-1-part-004.md) Git blob `5205e2774cfe2338fe0c793e8fa2dbcf2691570a`，46,074字节，SHA256 `a405b9e062fad5884b29bfd2b42ff6b9e60b3ec37dfeda6b7d745e186e8df25b`。所有科学raw仅runner，未经connector整读494KB科学报告或413KB纯报告。

## 1. 实际结论与输入区别

完整normal选择算法在声明的32个共同阶段中完成26个，在第27阶段没能让每个角返回其原阶段方程解；首次场读失败，未进入metric或restoration QP。失败不是未加载源码、文件缺失，也不是把未实际执行字段称失败。16完整来源/模型/snapshot纯归因成功，给出明确初始失败和所有未产场字段null。

本次用实际原`base.initial`，没有沿用12 gamma-H的替换H，没有从失败gamma继承场或根。原reference初点摘要为`cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3`，reference bundle `59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f`。固定scalar目标身份为`e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`，新完整normal模型为`a796b40802022f1d72717d227f417c4741b2a20f3c9e616540a86ba17c603a03`。

同18字Q按本实际reference严格绑定definition `976f9ad62cb67e36a7aa9c8a755671d4e815cbea01af28ace3b31e2031c54452`；原18字来源05dc/df11不冒成本run矩逆。所有同g历史输入均保：reference locations、实际3/17/21/26/30报告以及紧前gamma-H12报告。初始curvature/radius各1851，计数本身不是集合等号证明；完整walker/source责任继续保。

## 2. 声明的完整算法与实际失败边界

原1,333,370变量、45,324,288metric行、全freecore/H、原geometry/幅度与全部永久真筛保留。端点可用族仍为6controls；normal每阶段增量3维，角隐式每阶段9维。共同节点为所有精确`Fraction(i,32)`，首0末1，common_partition=true、per_angle_adaptation=false。metric完整隐式维192、sixjet完整隐式维288；stationary_KKT_selection=false、exact_ODE_solution_claimed=false。

控制球2，物理endpoint容差2e−12，根迭代24、回溯18、Armijo1e−4；wide两bubble和gamma1/16、1/8、3/16不变。声明外预算仍1×16 metric、4×64restoration、mu.01；本次没有执行这些外方向。原 jet-sum完整范数不变，未把direct integral的范数/阻尼暗带过来。

实际15 returned failed/1，控制器20.795726030999504秒。16返回completed/0，5.798183805000008秒：

| 项 | 实际值 |
|---|---|
| stop | actual_initial_zero_closure_field_read_failed |
| failure reason | A declared fixed normal plane did not return every original stage equation |
| failure_stage / completed_stages | 27 / 26 |
| requested angular order | 1 |
| same_branch_upgrade | false |
| final_original_endpoint_reread | false |
| final_original_endpoint_passed | null |
| current root count | 0 |
| current grid roots / second jets | false / false |
| metric/restoration/各accepted | 全0 |
| root failures / jet upgrades | 1 / 0 |

当前原endpoint residual、controls、physical-z norm、gamma norm、初/末Phi、maxmetric、g、末mu及初/末bundle均未产生。不能将第27阶段的失败夸成共同分割模型不存在，也不能在未读最终原endpoint的情况下称零闭合实现成功。

## 3. 真实计算量，不把零completed roots冒未尝试

实际记录的closure jet角求值4528，frame reverse angle products1296，stage equation角求值4096，stage matrix角求值952，stage angular matrix角求值0；3×3solve attempts936，implicit solve attempts0，implicit matrix角行2856。stage root attempts216、successes208、Newton updates720、backtrack evaluations1552。完成26个全角阶段与上述逐角成功数的口径不同；不能把根count0解释为没做任何求解。

这次compact未给第27阶段各失败角的具体残差、矩阵条件或触球原因；若需要该层归因，必须用完整既有报告的受限纯读，不从现有计数猜具体cause。原current point/order、所有此前frame/control与零control target导数由完整源绑定，失败时未从其他点补回snapshot。16 bound_snapshots=1、cross_point_backfill=false。

## 4. 完整来源与保存输出

| 角色 | 完整身份 |
|---|---|
| 实际15 source commit | `e5ed0423fd4baac96013d00d1e4ce20a3a596a61` |
| launcher | `c5f139bac6ecb50aa4b31de0aa8f5da4f2feafc2b26bc821826fc31a0c6f5c46` |
| driver | `68a6e483a4916d72411d08647622a1e539b26f9eca3c1449b4e7399bec17dd38` |
| endpoint | `42ea8ec5920e3815b99c83c41448efb38ee37860f4d9362ddea6bce2418d39fe` |
| geometry | `255760e188d13f22ffef86c029f35f5d1629384411d2e32f03f75df60f4ab71c` |
| new input binder | `ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39` |
| base | `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf` |
| 实际16 source commit | `4f0f91f87ae5cb2e9bb8c67095aa3c4ee339299d` |
| 完整reader | `8381cd9e034fda5917cae5f221f0c3f5420953cab6ca8dd809c82f3de0f7e1e8` |

目录`zero-closure-fixed-normal-lift-first`：report `6080d2e2953fef432658b7be26ba2e6dd466816327a80df4f2d662172ba24cbc`，494,948字节；command `28c1ad8a4542deb012bd9843abd636687db22b7cbdd7dac258b7da66e2a1a911`，16,636字节。pure16输出`26fd4f8e80d62210a443ae9974ede0a4577b3bd02b25630c057e5266f91fa393`，413,185字节，仍只runner消费。driver total15.665222816000096秒、峰RSS1,087,636KiB。

15预设final bundle/两个final position字段共3项缺失与真实首次场失败一致；16完整pure以null和zero-directions解释，summary_errors/missing_outputs均空，不把空值补零当场。不继承12任何根证书；后继normal-H或supported-unit机制必须保全部适用历史、准确源/模型/初点绑定，并自己完成原endpoint、全角、metric与真几何责任。研究完成标准未改变。
