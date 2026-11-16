# Request201：actual198 真实返回 owner 的完整十维三残差续算接口

作者：ChatGPT（AI，/root），2026-11-16。本文对应独立 Request201；实际结果尚未生成，预留结果编号 R430。父结果见 [R421](../results/R421-actual198-complete-ten-71-accepted-and-resource-partial.md)；原完整十维方向与法向算法分别见 [R378](../results/R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md) 和 [R392](../results/R392-complete-three-residual-normal-correction-on-ten-parameter-predictors.md)。

## 1. 本次推进与准确父范围

本请求以 actual198 最后真实被原三残差 Armijo 接受的十个 Decimal50 参数词作为新数值初猜，重新建立原有限字面模型。原16个八方向批、全局2400秒时钟、每方向20个原 alpha、每 alpha 最多3次完整三残差法向修正和每次20档内回溯保持。新入口仅改变明确父来源与本次身份，旧198源和运行不修改。

actual198 的原 run 为 `43773780174`，source `4b6eea36a8bd7f4aa1b7f2ce09779d3ef13e3040`，compute `132995301108`，report `133006856173`。它完成71个接受点、尝试72个方向和181个原 alpha，随后触及2400秒资源钟。最后真实接受坐标为 direction70、alpha_index2、alpha=`0.25`、normal_update2、normal_trial0。dir71 的 alpha0.5/update1 完整十列响应未返回，directions72..127 与 blocks9..15 未启动；它们不补记为拒绝。父 `final` 与 `final_binary64_projection` 都为 `present:false`，不代表完整终态或已接受 native/full-DN 场。

父原 status 为32602651字节，SHA256 `5b4cf48b69880b0c5e5acb8ee5368cbd33528bda795112abaf6df9d52d79eb3e`。两个 job 返回同一最终必要 ASCII JSON 正文77081字节（不含分隔换行），SHA256 `eff3036027e0abee24834175f1d323fb7c723fd42421a910931144a545680f07`；此前75742字节中间帧不是该终帧。十词同时出现在 `current_accepted_ten_parameter_words` 与 `trial_conclusion.first_and_last_selected_original_points[1].original.actual_parameters`，紧凑 JSON 为554字节、SHA256 `1732ad599fdd83306b5db0eadde23284acc929cd72346293950b20f3a2d72bb8`。完整十词是配方中的显式输入，不凭删除后的原 status SHA 恢复。

配方保留真实接受坐标、十词、原三残差和原 merit `0.05164901814834644065708434271021154319449799859706`。这些旧读数只供与本次 fresh 评价作只读比较，不充新 F、J、FD、响应状态或验收。父初始 Decimal30项与 binary6430项 FD 已齐；末60项、Arb及453圆未启动。原计算已在必要摘要、错误与静止核对后真实清理 raw，故本请求重建全链，不恢复中断中的 normal 响应。

## 2. 七件发布范围与六个固定正文

下表为六个运行／参数正文的最终字节身份；本文是第七件文档。临时工作目录的 `publication-files.json` 列七件路径、字节与SHA，清单不提交为科学输出。

| 仓库相对路径 | UTF-8 字节 | SHA256 |
|---|---:|---|
| `topics/visible-flex-larger-amplitude/computations/geometry_20261116_actual198_ten_predictor_normal_resume.py` | 54384 | `2911f896d2366b0cc4cf4095e7f260a412dada90cbd790936751810d036f4da1` |
| `topics/visible-flex-larger-amplitude/computations/root_20261116_actual198_ten_predictor_normal_resume_readout.py` | 49199 | `cb724a6e5c3c7f79a9381b53d6e77e13edc5bd4323e08dfb826a438143b02df9` |
| `topics/visible-flex-larger-amplitude/computations/geometry_20261116_actual198_ten_predictor_normal_resume_temporary.py` | 22890 | `809cf513f25dbed1ff937e28d5a7b949c93d49f8fe20e55338d35e28539eed43` |
| `topics/visible-flex-larger-amplitude/computations/actual198-returned-ten-predictor-normal-parameters.json` | 21198 | `119d751645425d343f38720a4145bf50831551756a431b5dda53e90df18d7712` |
| `topics/visible-flex-larger-amplitude/computations/public-actual198-ten-predictor-normal-resume-request.json` | 77482 | `9c30ac0d61c7cb3672c3dbc1f2f5fab47cd3b65b879226ce1357f9a7344ae981` |
| `.github/workflows/visible-larger-public-actual198-ten-predictor-normal-resume.yml` | 33137 | `5b836f552375445d2d36e476cf07bf954aff87b8331ca7e415c389adbc948f9b` |

新源使用明确独立身份：

- 科学 producer schema：`R259-actual198-returned-owner-full-three-normal-continuation-v1`；status basename：`actual198-ten-predictor-normal-resume-status.json`。
- 配方 schema：`R259-actual198-returned-owner-ten-predictor-normal-continuation-recipe-v1`。
- 请求 schema：`public-actual198-ten-predictor-normal-resume-request-v1`，`request_number=201`。
- wrapper schema：`request201-one-persistent-ten-predictor-normal-continuation-v1`。
- 必要读回 schema：`request201-persistent-ten-full3-normal-necessary-readback-v1`。
- 最终正文标记：`BEGIN_VISIBLE201_COMPACT_SUMMARY` 与 `END_VISIBLE201_COMPACT_SUMMARY`。只输出一份不超过90000字节的必要 JSON，不把大 raw 分块或编码运输。

## 3. 对198的最小实际差异

producer 是旧198 producer 的独立副本，新增实际198的完整固定来源和参数词，更新独立 basename、schema、输出及事件名。历史 ACTUAL194 常量原样保留；ACTUAL198 常量单独绑定实际198原件。原 `original_normal_counts` 和 `continue_original_blocks` 两个函数正文逐字保留，原数值模型、QR/Cauchy、法向 helper、方向与最终消费者不替换。

`recipe` 函数仍有两个准确分支：本次逐字段绑定的实际198资源 partial 返回点，以及本新 producer 自己已完成并被原门接受的合法后续父 schema。第一分支不接纳任意 partial 状态。历史183/185/189/194来源保留，当前父明确为198。旧 helper 的 `future_initial_parent_must_be_actual183_complete_final_words_not_prefilled` 是其初次引入的冻结 POLICY 字面，本次独立父分支和历史字段明确它不指当前父。

reader 对198只改本次 producer SHA、status basename、schema、请求命名和52项实际消费闭包数量；原必要选择、计数、同词引用及90KB保持。wrapper更新对应pins、请求/配方/科学身份及122/19、51→52集合数量，当前run元数据和缺件fallback的request_number均为201；启动、总钟、终止、wait/reap、错误和条件清理保持。request/workflow更新实际字节、SHA、闭包和唯一触发路径；原数值 policy、experiment、runtime、readout、resource、arithmetic及publication对象逐值保持。continuation contract只将明确当前父的描述键由194改为198。

配方 `actual_returned_owner_record` 保实际198接受坐标、F和W。R421已返回该点的原Armijo界；本配方不将旧界作为新评价的验收缓存，也没有新增数值门。已完成和中断范围由真实198结果决定。

## 4. 来源集合、原输入与当前实际消费闭包

request 的 `source_sha256` 为122项：原198全部121项逐值保留，加本 producer一项。workflow support为19项：原17项逐值保留，加本reader和wrapper两项。它们不等同于当前数学 main 的实际消费列表。

`source_closure.origin_producer` 为原198的51项，`current_producer` 为52项。原157的41源祖先与全部旧十族来源保留，再加本次入口。旧178/183/185/189/194/198 producer作为准确hash绑定的历史；其旧main均不执行，原157多项式优化main也不执行。实际复用数学子程序如下：

| 数学角色 | 原冻结源 SHA256 |
|---|---|
| 固定 support1/power4 十族 | `09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016` |
| 完整十列 Decimal50 模型 | `8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7` |
| 原完整十维 QR/clip/Cauchy | `6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861` |
| 全三分量 predictor-normal | `3bec3b7b07c0cb45bef27067c9b00f69e8930b296e1fa7006f716d3a7e6e4066` |
| 本次历史198 producer | `364ac3448aa1a4b077725f38647a665ea24bbcdf4db82f99e6b4bcfe06df26cc` |

四个原输入仍按原公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 临时恢复并核字节：

| 输入 | 字节 | SHA256 |
|---|---:|---|
| accepted | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail anchor | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

原78源恢复、四输入来源与旧十个字面数组身份保留；原九模型 binding `cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3`，十族 binding `065b11752c4b72422df2d9564748f2418f0a277401877c00c359d72171eefcbd` 不伪改。本次重新建表并比较完整 canonical 编码；这核验同一输入来源，不能被称为已证准确连续目标。

## 5. 同一个有限模型、尺度与所有原门

原699节点／698单元、三频率2/4/6、完整112模尾端与其原 stored J、原字面 binary64 表到 Decimal 的准确 lift 保留。持久参数使用50位 Decimal、ROUND_HALF_EVEN；forward是已说明实表达的有限精度形成，不是 IEEE 离散舍入映射的导数或区间证书。这里不是 R323 新连续 C profile，也不继承当前-C/native 场。

固定形状为原六候选选择所得 catalogue3、support1、power4。在所有旧九坐标及新增系数的真实试探、FD扰动中，形状不重新选择。十个坐标都活动，新增系数使用父原非零词，不能清零或塞回旧九 schema。

尺度固定来自原 actual157 九词：前九项 $S_i=0.01\max(1,|p_{157,i}|)$，第十项为 $0.01$；scaled radius仍为1。父历史半径 `0.0000390625` 只记来源，不用它重新设本次尺度，也不按当前或未来点重设 S。每原 alpha 先用 fresh 完整三乘十响应形成原最小范数 predictor及原 Cauchy fallback，严格负原 slope 要求保持。

每个真实有限且域合法的候选只按原全三残差 merit 和固定原 alpha 的 Armijo 界判接受。$c_A$ 是原 binary64 `0.2` 的准确 lift，不替换成数学 $1/5$。法向的目标是原基点 $F+\alpha Jd$，三个分量全部保留；每次修正 fresh 形成完整三乘十 J，使用原十维 QR／Cauchy及同尺度球投影。法向误差下降只决定临时工作点的更新，不添加新的外层接受阈值。未通过原 Armijo 的临时法向点从不成为 owner。

每方向最多20个原 alpha，每个 alpha 最多3次 normal update，每次最多20档真实 normal backtrack。全20档拒绝时原样停，不重复同点以凑128。只有当前八方向块明确以原方向预算用尽而终止，才沿真实已接受 owner 接下一块；块间不重设尺度、半径、owner或总钟，下一块 fresh 形成当前完整响应。最多16块／128方向，不等于承诺在资源内完成。

初始 Decimal与binary64各30项、末端各30项共120FD计划，以及原160bit／depth14 scalar Arb、完整453圆、全部112响应与各原终态布尔保持。没有降低 residual/domain/FD/native/final标准；未启动、未完成与真实失败分别读回。原终态消费者不是已付的 native 或连续存在证明；它们仍按实际结果报告。

## 6. 可执行入口、预算与规则监控

workflow 由唯一 `computations/public-actual198-ten-predictor-normal-resume-request.json` push触发；checkout、setup-python、setup-node 原 action pins 保留。Python3.12.14、numpy2.3.5、scipy1.17.0、python-flint0.9.0及单线程设置同198。

wrapper 的当前执行合同为：

```text
python -u geometry_20261116_actual198_ten_predictor_normal_resume_temporary.py
  --request REQUEST_PATH --request-sha256 ACTUAL_REQUEST_SHA
  --repository-directory CHECKOUT
  --original-input-paths RESTORED_INPUT_PATHS_JSON
  --rules-directory RULES_OUT --out REQUEST_OWNED_OUT
```

wrapper核真实参数文件21198字节／SHA以及明确请求身份，再启动上述独立 producer。producer的显式参数是 `--accepted`、`--prepared`、`--tail-anchor`、`--tail-config`、`--parameter-recipe`、`--parameter-recipe-sha256`、`--out`，并绑定 `--directions 128 --backtracks 20 --decimal-digits 50 --interval-bits 160 --interval-depth 14 --wall-seconds 2400`。

全局2400秒从producer main入口、source绑定以前开始；外层整个child也限制2400秒，包含import／setup、初FD、所有search／normal工作和最终消费者，不因换块重启。SIGTERM请求原partialcheckpoint；90秒grace后才强制终止。必要reader300秒、grace30秒；科学step50分钟、job65分钟。资源终止、数学NumericalFailure、IPC／source／protocol错误独立分类，不能由时间耗尽推出无下降或域反证。

仍执行冻结原 `root_20261114_current576_rules_runner.py`：2700秒真实pull/rebase、双README差异读取及改变后停科学。仅显式注入已经读过的README基线，runner数值无关控制流不替换；根 `21bd547f56590b7f2dd279d0297efb289a9b2783`、题 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。真实唯一规则同步行与HANDOFF大小责任保留。`git config --global merge.stat false`仅避免pull统计读取已删大数据。

## 7. 单份必要读回与实际可知范围

reader先读取完整本次status，对已启动的全部方向、全部外alpha、normal更新和真实试探作计数／分类／身份记录，保真实异常、停止、未返回normal行与未访后缀。128个计划方向和16块的地址始终保留；缺键与null不同。原完全相同的字面对象才使用显式引用或相同字段集合，不能由期望相等省略。

必要正文完整保初／末十词、三残差、merit，实际返回owner，以及初末12个FD层的原最大值、flags、所有真异常、120项实际覆盖；保全部原final flags、实际scalar／circle门字段和source／recipe／四输入／status身份。资源partial时未有final必须直说，不把返回owner包装成末FD通过。

每个已开始方向返回实际alpha地址、决策、选中merit、接受位置、接受Armijo界、正常试探计数、原理由／stop及必要未访范围。完整原 slope 历史已在Actions读，但正文仅选原首末可用 slope及全历史身份；中间 slope 和逐alpha predictor merit留在被标识的临时status，不冒称全部逐值运输。完整d、Jd、J／Q／R、所有normal向量、完整FD扰动表和112矩阵也以原identity及真实scope负责；root无需搬完这些大表才能推进。

科学stdout只记完整身份，不分包传原表。engineering stderr每文件不超过12000字节则保全文；超过时保完整bytes／SHA和明确首尾各6000字节选段，必要错误步骤失败，使主动清理不合格。该限额是协议与保存范围，不是科学接受条件。

最终单份必要ASCII JSON硬上界90000字节。实际超过、缺必要字段或reader失败时诚实输出错误范围并退出，不截全科学试步或编码拆包以伪称complete；未数值实跑，因此不保证未来正文大小。

## 8. 静止、清理和不可恢复边界

只有必要摘要成功且complete、必要原错误读取成功、wrapper实际所有child已wait/reap并持有同本次source/run身份的quiescence收据，才允许清理本请求自己的可重生临时输入、science输出和原数值源目录。wrapper收据明确 `launched_child_pids==reaped_child_pids`，无 detached process group；清理不碰其他请求或他人进程。

读回超限或错误读取未完整时主动cleanup跳过。此举保当前job中的排错窗口，不承诺runner销毁后仍保raw。正文和SHA不足以恢复已删除的科学状态。仓库和Release只保存脚本、明确参数、运行来源及必要研究结论，不保存本次可重算大raw；workflow不上传新数据artifact。

## 9. 冻结差异与已做／未做验证

临时工作目录的六个完整diff分别是 `producer.diff`、`reader.diff`、`wrapper.diff`、`recipe.diff`、`request.diff`、`workflow.diff`；`publication-files.json`给七件发布映射与各完整差异身份。它们针对已发表198的对应正文，供root逐真实改动阅读，非额外科学前门；这些临时差异和清单不作为课题raw或额外制品发布。

完成范围为来源文本、JSON字段、字节SHA与完整差异检查；本地没有导入／运行科学，也没有编译、AST、fixture、微基准或新的验收门。科学与原有语法检查只在公开Actions实际运行。此文不填未来run、结果、接受数或终态成功；actual201完成后以其真实source、必要摘要和未付范围单独形成R430。
