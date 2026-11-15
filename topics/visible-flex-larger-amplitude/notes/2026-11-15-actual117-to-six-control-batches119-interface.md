# Request119：从实际117六参数开始的临时独立八方向批次

**状态：源码与真实输入字段已接通，尚未执行 request119。** 本文件不填未来 run、source commit、方向、残差或成功标志。新的文件只编排冻结入口的独立进程；没有导入模型来代算任何科学量，也没有改冻结搜索、family、reader 或原117 workflow。

## 1. 真实初猜与两个不同的来源层级

实际117是 run `43691986785`，source `8e52679dcf3b934c2c488915c4b9622be6e6bf3c`。原小摘要完整读回为88,323 bytes，SHA-256 `14b3c8afe2a4fb03537a6d16dd4c55d44a37d750750ee25aef3bf157a026ac6b`。它绑定的原 `six-control-curved-status.json` 为1,210,862 bytes，SHA `d6d16e0da855325b97fc130a052743a8a9b51154382aecb29313e7be40011cef`；原完整求值 trace 为1,232,299 bytes，SHA `675c87731dab70fd8baa2603c7eda70b5c97129c721276a6dd2f647aeaee2b57`。

原摘要记录八个方向、十二个外层试步、八个原接受点，原完整三方程 merit 从 `1234.283357373182` 到 `1056.4579275781548`。unit、full112候选及非零非线性场标志仍为 false。下一初猜逐字来自原 `final.parameters`：

```json
[0.42123313016645575,0.2168136988206389,0.5629172159488391,-0.1326982215718915,0.00881492232668194,0.08635618490039039]
```

本次准备只读到了上述完整原摘要及其原 status 身份，不声称重新取得了117的完整 status payload。初始 recipe 如实保留该 status 与摘要的原 bytes/SHA，并且只使用这六个数作新初猜。它不是一个伪装的 parent status。冻结 e154 入口本身仍报告它没有读取 parent status/摘要、没有复用旧 J/merit/数组；这些原字段不改。

**新批次之间更强的实际来源事实由外层 wrapper 另记。** 每批结束后，wrapper 真正完整读取本批 status bytes，核原 e154 schema、全24个 consumed sources、原四输入、当前 recipe/family 及完整 trace bytes；再完整读取原3e2c reader通过独立 `GITHUB_OUTPUT` 返回的摘要 bytes。二者身份相符且原 final 字段完整时，才按原五字段 recipe schema 写下一份短参数文件。这份 origin 记录当前真实 `GITHUB_RUN_ID/GITHUB_SHA`、e154原 producer/schema、这批真实 status bytes/SHA、真实原摘要 bytes/SHA，以及 `parameter_field="final.parameters"`。

因此外层 `subsequent_recipe_status_and_summary_payloads_fully_read_in_this_run=true` 与下一原 child 自身的 `reported_origin_status_and_log_payloads_read=false` 没有冲突：前者说明 wrapper 实际做的读取；后者说明冻结 child 只读了给它的短 recipe。没有改动原 child 的自述。

原116→117首次引入两个 odd controls 的 recipe、原116来源及旧117 request SHA，完整保留在新 request 的 `first_introduction_history`。119使用已经存在的六维 family，既不再次声明引入新控制，也不套回旧四维父 schema。

## 2. 文件与固定身份

| 角色 | 文件 | bytes | SHA-256 |
|---|---|---:|---|
| 新薄编排器 | `geometry_20261115_six_control_temporary_batches.py` | 31337 | `b9db240d4ad1d1a12135e8a44db1a034b7bd6721d197ca8273aec9bed7eda4da` |
| 原117真实六参数 recipe | `actual117-explicit-six-control-parameter-recipe.json` | 1898 | `e930b7c9297e7c791647c2c013f80e641e40e8ae4d7e7b04dabc8b5b6a0f37f6` |
| 独立请求 | `public-six-control-batch-request.json` | 39308 | `7a99ec41d99c1f499b35b15ecd59c86c3af57421a5242eff5023a4a7355c4f3f` |
| 独立 workflow | `visible-larger-public-six-control-batches.yml` | 14719 | `66ba3f930f3da6afdf53ada2df7e3ca61d6921ded951e4628d54e6daad2f6b78` |
| 未改原搜索 | `geometry_20261115_small_core_six_control_curved_recipe.py` | 53497 | `e154afe28c588ce0c2ae936d4304b67ec84e2b46c96b03e48ce4113e2401a761` |
| 未改原 family | `geometry_20261115_small_core_six_control_family.py` | 39524 | `79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf` |
| 未改原摘要 reader | `root_20261115_small_core_six_control_curved_scalar_readout.py` | 19347 | `3e2c0515ee9759162e3736915674c86ca9a56441f2a7561df9dc09d37fea4d45` |

前三个运行文件放在题目 `computations/`；workflow放 `.github/workflows/`。原117的81个 primary pins逐项保留，只有新 wrapper 一个增加项，所以新 primary count 是82；两个 workflow support pins仍为原 rules runner与原 scalar reader。数学 producer 的 closure始终是原24个源，不能把工程 wrapper算成第25个科学源。

原四数学输入及其实际历史恢复引用保持117原样：

| 输入 | 原SHA-256 |
|---|---|
| accepted96 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared112/699 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 实际T112零H anchor/J | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| T112 config | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

历史恢复仍使用 commit `8bd267107cc8710d371f3b62c02986655ac965b0`。缺文件时只在启动阶段按原 path/bytes/SHA恢复一次；原78公共源同样只恢复一次。批间不重新下载或恢复这些输入。runtime仍Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0，BLAS/OMP/MKL均为1线程。

## 3. 每批完全保留的原科学责任

每批均由新进程执行同一个 e154 文件，参数固定为：

```text
--initial-relative-radius 0.1
--candidate-steps 8
--backtracks 20
--normal-iterations 12
--normal-backtracks 20
--normal-target-tolerance 1e-8
--candidate-resonance-tolerance 1e-8
--interval-bits 160
--interval-depth 14
```

原外层完整三方程、全六参数、原 unit 方程、全112 residual、完整实际零H尾J、原域检查、原完整三方程 Armijo、十二乘二十的 two-normal correction以及全部原初始/末端检查都由原入口自己执行。每批有新的完整初始描述/J与六列差分，末端仍有原完整六列差分、实际标量 Arb 域、完整原 circle/FFT/node/mid/RMS检查。wrapper不计算 J、残差、merit、方向、rank、谱、domain证书或参数位移。

原117最后记录的相对 trust radius是 `.0125`。119每批明确重置到原入口要求的 `.1`，随后在该批内部完全沿原半径更新公式。**这不是携带旧 trust state，也不是单次连续64方向求解。** 下一批的完整初态/J/FD/domain都新形成。family的函数公式不变，但搜索参数变化意味着实际 $g$ 随参数变化；不声称这些搜索点已经是同一个固定 $g$ 下的已接受场。

## 4. CLI与真实数据路径

运行wrapper的唯一科学编排CLI：

```text
python geometry_20261115_six_control_temporary_batches.py
  --request <computations/public-six-control-batch-request.json>
  --request-sha256 <这份真实request原bytes的SHA256>
  --repository-directory <固定科学checkout>
  --rules-directory <VISIBLE_OUT/rule-sync>
  --out <VISIBLE_OUT/six-control-temporary-batches>
```

`--out`必须是新独立目录。wrapper每次启动都要求 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。没有用于本地科学的绕行入口。父请求中的短参数记录是初猜，不是native成功缓存。

临时树的含义如下：

| 路径 | 责任与生命周期 |
|---|---|
| `recipes/batch-001.json` | 原117初始recipe原bytes复制 |
| `recipes/after-batch-NNN.json` | 从该新批完整真实status+原summary生成的六参数own-schema小recipe |
| `batch-NNN/science/` | 原child独占输出目录，含完整status、trace、原domain/circle临时payload |
| `batch-NNN/science.stdout`、`science.stderr` | 原科学stdout/stderr完整重定向；只记录bytes/SHA，不打印或上传内容 |
| `batch-NNN/reader-github-output.txt` | 本批独立空文件，只由原3e2c reader写入其原协议 |
| `batch-NNN/reader.stdout`、`reader.stderr` | reader进程的真实工程日志，记录bytes/SHA |
| `chain-metadata.json` | 小型原来源、参数、状态、退出码、summary/status/trace/output SHA及清理记录；原子替换写出 |

初始recipe不会带原 merit、J、数组或证书。后续recipe也只有原严格五字段：`schema/origin/literal_parameters/input_sha256/family`。新 origin采用当前实际run/source和当前e154身份，status bytes/SHA来自完整实际文件读取，summary bytes/SHA来自本批reader真实返回。原float字面值由标准JSON圆回，比较完整六个binary64词，包括负零；不本地求参数增量。

## 5. 单批读回与逐份stdout协议

每批原科学进程退出以后，wrapper才调用原3e2c reader，并为它设置一个新的临时 `GITHUB_OUTPUT`。读者仍使用它自己的原三个key：

```text
scalar_summary<<VISIBLE117_<原随机delimiter>
<原compact JSON>
VISIBLE117_<同delimiter>
scalar_summary_bytes=<原字节数>
scalar_summary_sha256=<原SHA256>
```

wrapper完整解析这个协议，核byte数、SHA、当前run/source；不会将reader schema从“request117原producer读回”改标签成新数学源。它分别打印：

```text
BEGIN_VISIBLE119_BATCH_001_ORIGINAL117_SUMMARY
<这一批原reader完整返回的JSON>
END_VISIBLE119_BATCH_001_ORIGINAL117_SUMMARY
```

随后是这份原摘要独立的bytes/SHA事件。后续批次用自己的编号，互不拼接成一个被90KB上限截断的大摘要。每一份仍受原reader的90,000-byte预算及其原fallback规则约束；没有扩预算、分块绕界或截除原试步来假装完整。

原3e2c可能在极大readout时返回自己的 over-budget/exception schema。wrapper会完整打印这个实际返回，明确标为工程读回不完整，然后结束后续批次。不会从缺少完整原trial表的fallback假称已经有完整读回，更不会把这一工程停止称为原方程/原Armijo拒绝。原科学进程结果仍按原退出码和status保存到小元数据。

最终chain报告不含八份摘要全文；只含来源、六参数、原标量字段和SHA。各批原merit仅按原字段复制，不在wrapper内跨不同参数模型相减、比较或求比值。原科学stdout/stderr也不会作为逃避90KB摘要界限的第二条数据发布渠道。

## 6. 编排停止条件与资源含义

只有一批完成原final检查、原完整summary可读，且原 `search_stop_reason` 精确等于

```text
explicit total direction budget completed, counting accepted and rejected directions
```

同时原 `total_direction_attempts=8`、接受点数大于零，才可能开始下一批。下列情况结束编排，保其真实状态：

| 情形 | 编排动作与含义 |
|---|---|
| 原 `original_unit_stopping_tolerance_met=true` | 停止；只报告原unit标志，不升级成非零native/BVP/闭场完成 |
| 原 `low_mode_candidate_has_small_full_recorded_right_residual=true` | 停止；只报告原full112候选标志，不升级完成标准 |
| 原接受点数为0 | 停止；没有通过新方向或新容差替换它 |
| 原停止原因不是明确八方向预算结束 | 停止并保原reason；不机械追加下一批 |
| child异常、非零退出、原final不完整 | 诚实工程/科学原异常读回；不继续计算 |
| 原reader未给完整正常摘要 | 明确工程摘要范围后停止；不改child的科学接受结果 |
| 批间已经达到3600秒 | 不再启动下一整批；标资源限制下的部分链 |
| 已完成最多8个独立批次 | 结束本次显式编排预算；不是根存在或全题完成证明 |

3600秒只在启动下一批前检查，不给已启动child增加新的内部timeout、不减少它的8方向/20回溯/12乘20或末端检查。因而最后一批可以越过这个批间时刻后正常完成。外层 science step75min、compute job90min仍是资源上限；外部终止、SIGTERM/SIGINT或规则变化都如实记录为partial，不能冒“全部回溯拒绝”或“无根”。

原 `root_20261114_current576_rules_runner.py`（SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`）包住**整个wrapper**，其2700秒实际规则同步周期不改。runner的原进程组仍包含wrapper和各科学/reader子进程；wrapper不给child新建脱离进程组。源checkout不由规则同步改写。token只供规则runner；科学及reader子进程从环境移除GitHub/GH/MR token和Git认证配置，不打印任何凭据。

## 7. 原文件保全与清理的准确范围

正常结束的批次，以及科学失败但原reader与完整status已读完的批次，均在读回之后由wrapper执行该批独占目录 `rmtree`。先保存小chain元数据和下一短recipe，才删除可重算raw；删除后再记录 `raw_cleanup_completed=true`。以后批次不会访问旧批J、status、trace或domain/circle文件。

**本workflow没有另一个always raw删除步骤。** 如果包装异常、外部强杀或工程读回失败发生在完整读取之前，尚未读完的 `batch-NNN/` 会保留在这个runner的临时目录。always的 `--report-only` 只读现有 `chain-metadata.json` 和真实规则回执，标明原进程/读取停在哪一阶段；不假称原status已完整取得或该目录已清理，也不为了最终清理抢先删除未读现场。它们随后随ephemeral runner销毁，不上传artifact/Release、不进入Git。

原78恢复树在 `$RUNNER_TEMP/six-control-batches119-original-source`，原四数学输入的恢复副本在当前固定科学checkout中的原路径。wrapper既不删除原78共享树，也不猜哪些输入原来已经存在而去删共享文件。这两类启动输入仍只存在本次ephemeral runner，其来源path/历史ref/SHA已经在请求中保留。没有一个清理行为改动历史Git对象或已发布数据。

## 8. Workflow与静态范围

独立唯一push trigger为：

```text
topics/visible-flex-larger-amplitude/computations/public-six-control-batch-request.json
```

它没有改原117的trigger、workflow或科学源。新concurrency group是 `visible-larger-public-six-control-batches`，不取消正在运行的同组请求。原checkout/setup action pins、四输入恢复、78restore、两README显式baseline与唯一规则同步行条件全部保留。

science结束后，always `--report-only` 将真正的规则 `sync-*-completed.json` 与已存在的 `runner-result.json` 收入最终小chain报告；它不会补造未发生的pull或未完成的child。独立report job只打印该compact chain元数据及SHA；各批原摘要已在compute log分别完整打印。没有旧publisher、artifact上传、Release上传或raw提交。

源级检查只进行了新wrapper AST、七个workflow shell片段 `bash -n`、四个inline Python AST、真实117原JSON字段/字节SHA以及源pin/参数diff。没有import或运行新wrapper、原科学源、模型、QR、FD、Arb或任何未来输出。三份原 e154/79464/3e2c 文件字节保持不变。静态receipt是交接说明，不是额外科学验收门。

与root已经全文读过的wrapper31,337B、workflow14,719B版本相比，最终运行源、recipe、request与workflow**没有后续字节修改**；本接口只明确了未读完失败目录的runner生命周期，未增加强制清理或新的数值条件。
