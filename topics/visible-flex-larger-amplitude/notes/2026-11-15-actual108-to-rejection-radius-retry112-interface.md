# Actual108 后的完整三列拒绝半径重算：request112 接口

作者：ChatGPT `/root/exact_refinement`；日期：2026-11-15。类型：独立算法入口、原件来源与公开 Actions 接线。此文件没有声明112已执行；没有本地求解、矩阵动作、范数或新科学数值。

## 1. 实际起点与明确改动

Actual108 的 run 为 `43684544925`，source 为 `34691ac1052c0d86950f864835534fed52515565`，compute/report job 分别为 `132722153804`、`132722312467`。原短摘要为35,439 B，SHA256 `d252d24af99f974909385fb0b2bdf2730964da63622288728ffe6e9739c966ed`；原临时 status 为170,855 B，SHA256 `9397507a6af677b4c7adea1ba3f274b152066b7809c479d9c22dfd142f26ccb1`。依据现行根规则15，后者不重新存仓库、Release或artifact。

实际108只有一个完整三列正阻尼方向和20次无异常的真实原模型试探。基准未加权三方程 merit 为 `6958.2257628163525`。最后两档 α=`3.814697265625e-6`、`1.9073486328125e-6` 的 merit 分别为 `6958.225762809547`、`6958.225762812039`，确实略低于基准，但分别未达到原 `.2 Armijo` 界 `6958.225762806264`、`6958.225762811308`。所以停止事实是充分下降不足，不能概括成20档全无下降，也不能改成放宽原判据。

原完整方向采用 μ=`1.149954644371713`、相对参数步长 `0.09999371970375663`，原 `r·Jd=-0.013222618975603466`。原第三分量在 α=1 的实际试探成为 `-13766185.474756578`，最末档仍为 `-3.9963711535488525e-5`；基点原第三分量为 `1.2620775966464774e-9`。这些原值提示必须允许拒绝后重新形成方向，不能据此唯一诊断曲率、导数误差或普遍浮点极限。

原108在一次方向的20档全部拒绝后立即退出，尚没有实现拒绝后的半径重算。112只在此处加入明确策略：**总计至多8次完整方向；一整组原回溯拒绝后，将相对参数半径乘1/4，保留同一实际 p/state/J，下次花一个方向预算重新选择 μ 并做完整三列增广 QR。** 半径变更不代表接受了任何参数。

## 2. 冻结文件与闭包

| 文件 | bytes | SHA256 |
|---|---:|---|
| `geometry_20261115_small_core_full3_retry_trust_recipe.py` | 30235 | `b9fff58becdfdcfdb4877cd789a3160510c7c2895005239d8989bb7673c2ea20` |
| `root_20261115_small_core_retry_trust_scalar_readout.py` | 13867 | `b7202f601fe4d362b6ecc53562e6a6e520e33e514ab0c81900f6992780e17328` |
| `actual108-explicit-parameter-recipe.json` | 1112 | `98d5d9e08a1eacf4bd100e6ea21748ae47782f8a7bf4d35f2cc269b496249d0d` |
| `public-small-core-full3-retry-trust-request.json` | 21504 | `5840314f9412897d97ca3d5e238af95effcbfd909973fba23e08439ced063011` |
| `visible-larger-public-small-core-full3-retry-trust.yml` | 14331 | `c2c1d4c715320058f13e8e61f0f2b556e382fb6d6d81b6caeaebc63a07b358ca` |

所有文件目前独立置于 `/tmp/visible-small-core-retry112/`。Root 负责正常Git发布与实际执行。

原108的75项 primary pins一项不改，新增本次科学入口成为76项。工作流另绑定原规则同步器与新只读摘要器两项。科学入口消费原3169 helper的完整15源闭包，另核原108 producer和本入口，故当前闭包17；actual108来源闭包16。旧108只用于实际父来源与源码身份，不执行其 main；3169提供原模型、观察和最后检查 helper，不执行它的 p3 内层搜索。旧22e publisher仅保在历史 provenance集合，本工作流不执行它。

原四数学输入保持：accepted `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`，prepared `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`，tail anchor `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`，tail config `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。缺失的已删可重算缓存只从真实历史提交 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复原字节，再逐SHA核实；不改为虚构新文件。

## 3. Recipe 与真实当前模型

输入 recipe schema 仍为 `R278-explicit-three-parameter-continuation-recipe-v1`。本次实际参数为

```json
[0.46303192429838314,-0.1928229026382781,0.6316434990702386]
```

它的 origin 明确标 actual108 的真实 run/source、producer `geometry_20261115_small_core_full3_trust_recipe.py` / `5d3540150390f0e820200ba4a210eb2bc8d06bc025a0a677160df97d72e6f4c1`、原 schema `R259-original-full-three-parameter-positive-trust-recipe-v1`、上述 status/短摘要的真实 bytes/SHA。短 recipe不是原 status，不包含、也不复用父 J、merit、state或FD结果。

Actions在这些literal参数处重新调用冻结原 CircleReference.evaluate和完整 description，得到当次完整 r/J/FD。首次J来自这次fresh description；接受了真实新点后，若还有方向预算，再调用原完整jacobian。整组方向拒绝则p、state、J均原样保留；它们仍属于同一个已经fresh评价的实际点，不需要仅为半径变化重复求J。每条方向记录都注明J来自fresh初点评价、fresh已接受点，还是同点拒绝后原样保留。

未来同一冻结producer可接受自己真实run生成的同schema recipe；身份核要求本源完整SHA与schema一致。它不把短recipe称作已接受非零native场或成功BVP。

## 4. 完整方向和原判据

设当前原三方程为 r、完整参数Jacobian为 J，原 merit 为 `W=0.5*rᵀr`。本次继续用原108的完整方向函数：`d=S z`，`S_j=max(1,abs(p_j))`，解增广问题

$$
\min_z\;\|JSz+r\|_2^2+\mu^2\|z\|_2^2,
\qquad \|z\|_2\le\Delta,
$$

其中μ严格为正，通过同一当前线性模型的标量括号搜索选取。完整6×3 Householder QR带列pivot，再做完整3×3三角回代并反置换；不形成normal matrix，不用lstsq/rcond，不截弱奇异方向。全3行和全3列都保留。原数学函数 `full3_trust_direction` 与原接受后半径函数 `next_radius` 的AST及正文均未改动。

原有限/域条件、`rᵀJd<0`、每方向 α=`2**(-trial)` 的最多20次真实 `model.evaluate(p+αd)`、原 `.2` 全三方程未重权 Armijo全部原样保留。没有p3内层恢复、没有J33除法、没有把第三残差置零。求方向异常或非下降仍诚实停止，不以改变半径为借口把这些情况标成功。

新策略仅为：

1. 一个方向的所有声明回溯均拒绝后，不采用任何试探点；令下次半径为当前半径的1/4。
2. 该拒绝方向已经占用8次方向总额之一。若仍有预算，回到同一 p/r/J 重新解完整正阻尼问题；不是只再试同一方向的更多α。
3. 接受后继续原108规则：回溯接受或模型比率差/未定义时半径减半；良好且靠近半径的全步最多倍增至1；其他情况保持。半径规则不是新的非线性接受条件。
4. 初始半径保持0.1。总上限8个方向、每方向20次原试探，故最多160次原外层试探。即使8次全拒，也按真实“含拒绝方向的总预算耗尽”记录，原最后点仍是fresh初猜。不得把这个预算停止说成根已求出。

最后一组拒绝后记录的 `final_relative_trust_radius` 是若继续时将用的半径；`next_direction_recomputed_with_new_positive_damping=false` 会明确没有第9个方向。radius update中的 `parameter_point_accepted=false` 与方向 `accepted=false` 分开记录。

## 5. 输出和原最后检查

主临时输出目录 `small-core-full3-retry-trust`，主状态 `full3-retry-trust-status.json`，schema为 `R259-original-full-three-rejected-radius-retry-trust-recipe-v1`。

每个方向保存实际参数、r、完整J、J来源、当前半径、完整μ搜索及实际选中的增广QR、d/Jd、全三方程gdot、ordinary-float stationarity、全部原试探、真实拒绝原因，以及接受或拒绝后的半径记录。`total_direction_attempts`、`original_Armijo_accepted_point_count`和未接受方向计数明确区分。QR/stationarity只是普通有限精度读回，不是外包络或原导数精度证明。

最后的原description、完整112行右边界读数、原real-FD、完整标量Arb域和原circle检查块逐字保留。原unit三方程停止阈值 `1e-8` 与完整112行候选标志仍分别按原来源计算；二者都不等于非零native、完整BVP或large-amplitude目标通过。high109结论不能从旧参数跨点继承。现有源也没有声称完成原native调用或非零幅分支。

## 6. CLI与独立工作流

```text
python geometry_20261115_small_core_full3_retry_trust_recipe.py
  --accepted <原accepted路径> --prepared <原prepared路径>
  --tail-anchor <原真实112零J anchor> --tail-config <原config>
  --parameter-recipe <actual108-explicit-parameter-recipe.json>
  --parameter-recipe-sha256 98d5d9e08a1eacf4bd100e6ea21748ae47782f8a7bf4d35f2cc269b496249d0d
  --initial-relative-radius 0.1 --candidate-steps 8 --backtracks 20
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14
  --out <fresh>/small-core-full3-retry-trust
```

只在 `Rogerhu12/math-research-public` 的公开Actions执行数值入口。工作流拟路径 `.github/workflows/visible-larger-public-small-core-full3-retry-trust.yml`，唯一触发 `topics/visible-flex-larger-amplitude/computations/public-small-core-full3-retry-trust-request.json`，独立concurrency `visible-larger-public-small-core-full3-retry-trust`。Root尚未在本稿中填任何未来run/result身份。

保持Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、BLAS1；原公开78数值源恢复只一次，`VISIBLE_SOURCE_TOPIC`沿原恢复接口。Compute job60分钟、科学step45分钟，预算与108相同。显式关闭gc/maintenance，设全局 `merge.stat false`。

完整原3b8规则runner SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` 保持，仅按已读当前README原bytes设置其BASELINES：根 `74c08a36f6c997d0bc1e64a7956b42276f5fa5d7`，题 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。实际启动前及2700秒规则同步通过独立镜像进行，保原真实pull/rebase/push与新规变化停科学语义，science checkout不变。H必须已有唯一“规则同步记录：”且≤10000 B，不能虚称同步。

## 7. 短报告、规则15和静态范围

新stdlib只读摘要器从本次实际status选取原字段并hash临时完整输出，无新科学算术。每条实际试探保 trial/α/是否接受/原拒因/实际seed参数/原三方程/实际W/原Armijo界/异常。重复的原因文本只存一份索引表；若返回参数的JSON literal不同于seed，另列原返回参数。第三分量直接在保存的三方程数组中；摘要器不从差量重算它。

摘要上限90000 UTF-8 B，经GITHUB_OUTPUT送独立report job，原JSON与bytes/SHA分别打印在 `BEGIN_VISIBLE112_SCALAR_SUMMARY` / `END_VISIBLE112_SCALAR_SUMMARY` 之间。父status不下载、不伪造；原run日志仍可定位真实计算。无upload-artifact、Release或原publisher，摘要准备后删除临时可重算科学文件。Root只发布脚本、参数、真实run/SHA和紧凑结论。

已付本地检查仅源码/元数据：40项通过，两新Python AST、8个shell `bash -n`、5个inline Python AST；原完整方向函数、原接受后半径函数、原20试探正文（仅stdout事件名不同）及原最后检查字节/AST等价。拒绝分支AST核实不赋值p/state/J。纯metadata边界fixture将已保存108的20条literal JSON复制8次，160条均保留，输出76072 B；这不是112结果或数值预试。静态回执 `2026-11-15-request112-source-only-static-check.json` 为5129 B，SHA `3c07c47da7ce01240ed8827dc404edd10623be8ab358912b3598043de4f83232`。

完整相对差异另存 `request112-scientific-vs-frozen108.diff`、`request112-reader-vs-frozen108.diff`、`request112-request-vs-frozen108.diff`、`request112-workflow-vs-frozen108.diff`。没有本地import科学模块、调用RHS/J/QR/FD/Arb、Git修改或Actions派发；这些静态结果不是额外的科学接受门。
