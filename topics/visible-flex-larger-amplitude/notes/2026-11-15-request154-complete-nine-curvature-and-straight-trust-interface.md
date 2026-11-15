# Request154：完整九参数二阶曲率与真实直线试探接口

作者：AI assistant；2026-11-15。

**状态：独立可执行源码与唯一 Actions 请求；尚无本次运行结果。** 所有源编写、JSON 字面值提取、SHA、AST/YAML/bash 语法检查均为本地非科学操作。没有导入数学模块、运行模型、构造数值 fixture，或对新方向作本地试算。原 Request149 五源及以前的科学源不改。正式推送、触发及实际结果读取由主控负责。

## 1. 本次要检验什么

[R329](../results/R329-actual149-persistent-decimal50-complete-response-and-small-curved-descent.md) 已真实读取 actual149：参数、原有限模型与完整 normal 变分在 Decimal50 内持续保留；八方向都接受，但全三 merit 仍只微小下降。normal 精度改善不等于完整目标能走较大步。

本次采用 [R332](../results/R332-complete-nine-merit-curvature-and-honest-trust-proposals.md) 的完整目标曲率：对同一有限字面模型重新形成全三残差、完整 3×9 一阶响应以及三张完整 9×9 Hessian。主候选实际路径是 **直线 $q(\alpha)=p+\alpha d$**。仅在主方向形成失败或其 20 个真实直线试探全拒绝后，才另标签执行冻结 actual149 的完整 GN/normal 回退。

这是一个新方向及全局化策略，不是旧小步批次换名。新探索半径为精确十进制字符串 `"0.01"`；原父半径只保留为真实来源。全部三残差、原未加权 merit、原 binary64 `0.2` 的准确 Decimal 提升及原域/最终检查不变。没有增加 inner-target、导数精度、特征值或条件数接受门。

## 2. 真实父来源与持久参数

父运行是 `43720604504`，source `94b139513148f17e2dc04b51235fd9d1f5ad9ade`。原 producer 为 `geometry_20261115_small_core_nine_control_decimal_recipe.py`，SHA `66906f121c52f6dc57894efa368299990eea45f2f1d4fc5e6ce4af2fc5b9536e`，schema `R259-nine-control-persistent-decimal50-complete-three-curved-search-v1`。

| 原记录 | bytes | SHA-256 |
|---|---:|---|
| 原 status | 1,198,865 | `7d743a7102ee161840b4bf70e63554f4071f052a74b64ec4f6df104509ffa02e` |
| 原 primary | 88,956 | `c1f3f1ce7267be8f687fd3e09dd62033fa3f342372aec23170bea753403ac8bb` |
| 逐段重建完整 view | 1,202,255 | `2798213426ac99b352ba6134eaf29a264ccc9714c79af7e44f4fedce4289e850` |

配方逐字复制原 `final.parameters` 九个字符串，顺序仍为 `[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]`：

```json
[
  "0.30552138534925830908363218769912547800881372191833",
  "0.21645011773189881369006670934987844373659546308148",
  "0.34270057352299705888753492758971142696612449096673",
  "-0.063223361377014163543413089246839546163042630000979",
  "-0.017474518192118549114488520725604476285952902242329",
  "0.93761154129728826341840484110192043694902896713822",
  "1.0751306443033354220740429713561560108303082571479",
  "0.68868997944390310960387314323823496556100514955954",
  "0.93854260164735876770353306768909495039407142564921"
]
```

父 `final_relative_trust_radius` 原字符串为 `9.536743164062500529395592033937711917701562924776E-8`。它仍写入 `algorithm_state` 和来源记录，但不是本次初半径。本次另有严格匹配的 `exploration_policy`，明确 `parent_radius_is_provenance_only=true`、`initial_relative_trust_radius="0.01"`。来源参数未经 float 转换，也不以父 J、merit、Hessian、FD 或 owner state 冒成本次新计算。

配方仅是实际来源的小文本，不是已接受非零场或原 status 的替身。producer 允许真实 actual149 或本独立 schema 的未来实际父，但每次仍必须带完整真实来源 tuple 与明确探索策略；当前没有预填未来 run。原父 payload 不需重新取回，SHA 在此只承担来源身份。

## 3. 数学来源与文件边界

五个新 Python 文件均独立新增。完整源码在同名 `computations/` 路径发布，旧文件原字节保留。

| 新文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261115_nine_control_decimal_second_variation.py` | 11,219 | `ad568abc8bf35003375d80e303c44df6dcb2f1c75fd41163cf5c0f423ba321a1` |
| `geometry_20261115_nine_control_decimal_ambient_trust.py` | 21,458 | `bb603fc6c32f146552262b38648ddc2e777e5968a1473259ad6d1e6ce2a86115` |
| `geometry_20261115_small_core_nine_control_decimal_curvature_recipe.py` | 27,555 | `3d59811078d82110449216a8ab5dadf905c435e1e45085b96f6d1c8fa04eb0c4` |
| `root_20261115_nine_control_decimal_curvature_scalar_readout.py` | 17,468 | `263dd544395734d1a0e4c227655157f536541be40ff41d0dabce92778d75cb5a` |
| `geometry_20261115_nine_control_decimal_curvature_temporary_batch.py` | 21,744 | `329c8506c04e5cdd9695328a3ebc72e9dcbb34b7857f7bfdba1af06a916a6fea` |

完整 runtime source 表保留原 100 件并加新 model/search/producer/wrapper，共 **104**；support 表保留原 7 件再加新 reader，共 **8**。实际 producer 消费闭包由 actual149 的 **36** 件增至 **39** 件；当前 source SHA 的三项增加是新 model/search/producer。旧 producer 只保身份；不执行其 main。原 146 的 `load_baseline` 仍负责原输入/族建立，不再调用其旧 `recipe_input` 解析持久参数。

新二阶模块继承冻结 `geometry_20261115_nine_control_decimal_literal_model.py`（`2422be0c…`）的 `_evaluate`、`matrix`、`evaluate`、`response`、`description` 原方法，未覆写这些方法。新 ambient 模块直接导入冻结 `geometry_20261115_nine_control_decimal_curved_search.py`（`433d5ddd…`）。只有标签明确的回退使用其 `complete_direction`、`curve_frame`、`curved_candidate` 及其全部 normal 内部流程；`next_radius` 对两条路径均按各自正确预测使用。

相对 149 的 producer/reader/wrapper/recipe/request/workflow 六份完整文本 diff，以及两个新增数学模块的全量 diff 随交付保留。它们是源码差异说明，不另构成科学审核关卡。

## 4. 同一有限表达式的完整二阶传播

`SecondJet` 是原 `Jet` 的子类，每个标量保留值、九个一阶分量和 45 个对称二阶分量。乘法、除法、正平方根按 R332 的完整二阶链式法则传播；对角二阶项同样保两个交叉项。45 个分量按固定 `(i,j), i<=j` 顺序保存，再完整映成 9×9；不是 Hessian-vector 抽样，也不截弱列。

原 `_evaluate` 在这些对象上原样执行：699 节点、698 中点、全部 radius 消元、三条完整 2×2 模链、末端两个大项与完整 112 右残差都参与传播。原值和一阶表达式沿用冻结 149 的写法。当前第二传播还保留其原值与独立 first-forward 原值/完整 J 的实际差值；没有用一致性断言替代真实输出。

本模型仍准确提升本轮实际形成的原 binary64 mesh/h/base/control/频率/目标/完整112×112尾矩阵字面数，并非用高精度重形成连续 metric 或新 native J。actual149 的原字面表 shape/dtype/rawSHA 和原 binding SHA `c201e4b709df8f6cf1be61b0d71b19732b4a3cb78b1e56d799f10db1c7760368` 已保留在 request 的父来源中，供实际读回比较。新 model 保本轮完整 binding 与追加前的原 binding SHA。**同源码和四输入不预称跨运行所有数组逐位相同**；比较仅为来源读回，不是新的科学接受门。

Decimal50 是圆整算术，不是区间。这里传播准确实表达式的形式导数并逐运算舍入，不声称求出了离散 rounding 映射的导数，也不从 50 位字数推出弱方向或 Hessian 的严格误差界。

## 5. 主方向：完整 ambient merit Hessian

在每个当前点固定 $D_j=\max(1,|p_j|)$，形成全部九维

$$
g=(JD)^\top F,\qquad
B=(JD)^\top(JD)+\sum_{k=1}^3 F_k D H_k D.
$$

全部 3×9 J、三张 H、GN 项、三个残差形成的总曲率项、完整 B、尺度和当前 F 均保存。没有用 GN 代替完整 B，也没有用第一残差替代三项总和。

有限 full9 对称 Jacobi 最多 64 sweeps，保全部九列、变换矩阵、对角值、`BQ-Qdiag` 与 `QᵀQ-I`；`1e-40` 只是迭代停止量。它不给特征值包络或严格正交证书。移位起点采用完整有限对角指导与 `1e-35*max(1,||B||F)` 正余量，随后最多 64 次完整 9×9 shifted-Cholesky bracket、64 次 refine。有限 pivots/完整因子、每个实际 shift、完整解、因子形成残差与线性残差全留；不以“残差够小”增加接受门。

候选池包括找到的完整移位解、完整九维 Cauchy 点、全部九个谱列中实际形成负曲率的有向候选。每项记录完整坐标、实际范数、形成 slope/二次值和排除原因。对池内具有有限严格负形成 slope 的候选，选择最小有限二次模型值；这不声称准确 trust 子问题的全局解，也不声称非线性最佳点。谱列指导不等于丢弃其他维度。

选中后用原 first-forward **沿完整实际 d** 再形成三项 action 与 `F·action`。只有这个实际有限 slope 严格为负才进入原回溯；与轴 Jd 的差也保存。若该方向没有提供原负 slope，按明确失败原因进入下述回退；没有伪造零梯度处的负 slope。

半径限制针对相对 predictor z，有限 rescale 后仍记录实际范数；它不是区间不等式证明。此处主候选不做任何 normal 修正，实际参数就是 `p+alpha*d`。二阶预测只用于这一条直线路径和它的 radius ratio。

## 6. 两条路径、完整预算与原接受门

最多八个方向。每个方向先形成新的 full9 曲率候选，按原 20 档 `alpha=1,1/2,...,2^-19` 实际求完整 primal/domain。接受条件仍为有限合法点上的原三项未加权 merit 与原 Armijo：`W(candidate) <= W(current) + ARM*alpha*slope`，其中 ARM 是原 binary64 `0.2` 的准确 Decimal 提升。

主路径若形成失败，或全部 20 档真实拒绝，才以 `original149_normal_fallback` 标签调用原完整 GN 方向和原 normal 曲线。回退有**另外** 20 个外档，每个 normal 保原 12 Newton ×20 内回溯；R299 同轨迹全 merit selector 仍只处理成功完成的原 normal 轨迹，不救回未完成调用。保原 inner 目标 `1e-8`，且该目标仍不是额外 outer 接受门。

因此本次最大每方向 **20+20=40** 个外试探、总共至多 320 个外试探，不冒称仍只有 160 个。若主路径接受，回退不调用，并明确记其未访问全部后缀。方向形成失败、原域失败、merit 拒绝、无负 slope、资源中断分开记录。回退的实际曲线位移可能与 predictor 不同，保其真实参数/位移，不能套用主路径直线曲率。

主路径 radius ratio 用真实直线二阶预测；回退只用冻结 149 的原线性 residual 预测。沿用原接受后 halve/double/retain 规则；两条路径全部失败/拒绝才 quarter。每次接受只采用真实 candidate 的完整 Decimal state，重新形成下一点完整 first9 J；所有拒绝保持原当前点，不把试探或二阶状态当已接受点。

主路径 ambient Hessian 不含 normal 的 $\nabla W\cdot q''$，所以不能对 normal 曲线直接声称二阶预测；路径标签与相应预测表达式均写入每个原 trial/半径记录。

## 7. 初末诊断与最终责任

除八次主方向可能各形成一次完整二阶外，初末点各实际形成一次 full9 second response；最多十次完整 second-forward。完整 full112×9 及 full112×9×9 也保留，而不是只打印三行摘要。

初末新增二阶诊断各为九轴×三个原 step 字面值，共 54 个检查。对轴 j 使用 `h=step*max(1,abs(p_j))`，分别调用冻结原 first-response 在 `p+h e_j` 与 `p-h e_j` 的全部九列；比较 `(J_plus-J_minus)/(2h)` 的完整 3×9 与 H 的对应列。总共另有最多 108 次完整 first9 response；所有原响应、误差矩阵、范数、失败/未完成字段都保存。单轴失败继续剩余轴。它是实际诊断，不证明误差包络，也不改变原候选门。

同时保留冻结 149 的全部责任：

- 初末实际 persistent 点的 54 个完整一阶 FD 检查。
- 明确投影至 binary64 的初末 54 个原一阶 FD 检查；记录每个投影误差，不覆写高精度 owner。
- 原 complete scalar Arb（160 bit/depth14）和原完整 453 圆、两 RMS/BC/域读回，在声明的最终 binary64 投影上运行。
- 实际高精度与投影点各自的三项/完整112停止 flags；原低三容差仍是原 `1e-8` 字面。
- `native_nonlinear_solver_called=false`、`nonzero_field_completed=false`、`success=false` 责任保持。这个候选诊断不能冒非零 full112/native/闭曲面完成。

`*_checks_completed` 只表示既定检查已走完，不等于每个误差有效，更不是精度证书。任一实际异常或墙钟退出保 partial/错误；未完成的 Hessian/FD/Arb/circle 不写成已经付清。

## 8. 唯一可执行接线

发布路径：

- `computations/public-nine-control-decimal-curvature-parameter-recipe.json`
- `computations/public-nine-control-decimal-curvature-request.json`
- `.github/workflows/visible-larger-public-nine-control-decimal-curvature.yml`

workflow 只由该新 request 的 main push 触发，独立 concurrency，原请求不变。参数配方 3188 B，SHA `87037451818101e7308130f19fcf33b53e4728f787711f4708531f4d208deffb`。入口 CLI 是：

```text
geometry_20261115_small_core_nine_control_decimal_curvature_recipe.py
  --accepted <actual original accepted bytes>
  --prepared <actual original prepared bytes>
  --tail-anchor <actual original zero-H anchor bytes>
  --tail-config <actual original T112-config bytes>
  --parameter-recipe <the exact request154 recipe>
  --parameter-recipe-sha256 87037451818101e7308130f19fcf33b53e4728f787711f4708531f4d208deffb
  --out <owned RUNNER_TEMP/science>
  --decimal-digits 50 --candidate-steps 8 --backtracks 20
  --normal-iterations 12 --normal-backtracks 20
  --normal-target-tolerance 1e-8 --candidate-resonance-tolerance 1e-8
  --interval-bits 160 --interval-depth 14
```

`--backtracks 20` 分别限制主、备用路径，不能读成二者合计 20；status/request 明列最大 40。新探索半径由严格配方策略给定，不添加一个可以暗改的默认 CLI。

四原数学输入维持原 file/bytes/SHA，由历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复到 request-owned RUNNER_TEMP。原 78 public numerical source 只恢复一次。原 tail anchor 只参与原 finite coefficient/projection责任，不冒当前非零已接受尾；没有本次 native 请求。

Python 3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、BLAS 单线程；高精度算术为标准库 Decimal50/ROUND_HALF_EVEN。完整科学 step 75min、compute job90min、report10min。没有新增隐蔽 child timeout；原规则 runner 同进程组及 2700s 真 pull/rebase/README差异停止保持。更大的二阶成本没有本地 benchmark，不保证一定在墙钟内付完。

根/题 reviewed README blob 仍为 `21bd547f56590b7f2dd279d0297efb289a9b2783` / `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。固定 runner SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` 不改，只按既有真实文本覆盖其旧 baseline 数据；H 唯一规则行及大小检查照旧。

## 9. 完整输出、异常和清理

科学 schema 为 `R259-nine-control-persistent-decimal50-ambient-curvature-trust-v1`，status 为 `nine-control-decimal50-curvature-status.json`。wrapper schema 为 `nine-control-persistent-decimal50-ambient-curvature-single-batch-v1`；reader primary schema 为 `original-nine-control-decimal50-curvature-segmented-complete-readback-v1`。

reader 从 status 逐字段搬运，除明确映射 `schema`/`searches` 为 producer schema/outer searches 外，没有数值白名单或截断。全 Hessian、全谱/shift/factor/线性残差、全部真实主 trial、回退 normal 轨迹及 R299 池、全部初末 FD、原标量/圆/错误字段都进入完整 scalar view。超过 90KB 的对象按原有可逆 JSON 结构分段，每段与整组都有 bytes/SHA；不是省掉不利记录以凑 bound。

primary 与单个 segment 均 <=90000B；独立 report 只转一个有界 chain index。八个计划方向的实际执行/未执行、每条路径的 trial 计数与所有未访问后缀保留。若 chain 本身超界，诚实输出其完整身份、错误 schema 和未完成范围；不冒科学完成。分段内容保在 compute 日志，不拼成过大的跨 job输出。

resource signal 时 producer 尽可能写真实 owner/partial；wrapper 的 report-only 只读取既有 status，不重新运行科学。生产者在 status 建立前出错也由 workflow `always` 读完整 stderr；包括 reader stderr 与失败 child stdout，按 12000 原 bytes 的 UTF-8 surrogateescape/ASCII JSON 分段完整输出后才清理。每份日志保整份与各段 SHA，不能仅留编译/调用错误哈希。

清理仅 request-owned RUNNER_TEMP 下本次 scientific/inputs/source-cache；先按原属主处理只读权限，拒 symlink 越界，不动活跃其他请求或共享 checkout。没有 raw main/Release/artifact 上传。仓库只保存源码、配方、请求、接口、证明及以后真实紧凑结果；临时静态检查回执不必入库。

## 10. 此刻实际完成的静态范围

已对本地独立源与公开 root clone 的 104+8 份文件逐字核 SHA；原100+7、四输入对象和历史 commit 保持。5 个新 Python AST、9 个 bash 块的 `bash -n`、6 个 inline Python AST 通过；只解析/语法，不执行其 main 或模型。当前 producer 36→39 闭包、新源/reader/配方身份、唯一触发路径、75/90min预算均按源码检查。

这些结果只排除已见的源接线/语法差异，不证明新曲率准确、谱指导稳定、20 档内必接受或能达到原目标。实际运行将直接回答完整曲率在较大探索球内能否供原全三 merit 接受；所有失败原因和误差读数照实保留，不用新增门掩盖结果。
