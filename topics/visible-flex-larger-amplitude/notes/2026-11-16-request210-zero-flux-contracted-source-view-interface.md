# Request210：R471 零非线性通量与完整有限切向的透明源码视图入口

作者：ChatGPT（AI 助手，源码与数学范围说明）。  
日期：2026-11-16。  
状态补正：[R472实际终态](../results/R472-actual210-private-import-closure-failure-before-native.md)已确认 source b418c6e6e5428be5774917210878c41b4245fdf0 / run43807229341 的143公开文件复制、11视图生成及154项声明身份绑定完成，但原physical_test_response递归导入的geometry_20261114_lifted_modes_response未列入私有集合，科学进程在runtime导入期以ModuleNotFoundError返回1，elapsed1.0332460349999906秒；native/H/J/R273/FD/fullDN未起。本文原“完整源码闭包”措辞仅能指已声明身份集合，不能再解释为实际完整递归导入已付。原科学五件与生成视图保持冻结字节；本次只补正说明。16,973B/e299e3cb必要正文两job同字，quiet后removed=true。补齐真实递归来源在独立211完成，不回填210。

## 1. 本次完成的实际接线

本入口把已发表 [R471](../results/R471-zero-nonlinear-split-flux-finite-trace-fast-path.md) 的两个真实科学模块接到原 Request208 完整计算链。唯一新的数值分支是：在实际有限根轨迹、实际方向词和每个用到的角向量均满足 R471 条件时，保留原来以正零初始化的完整非线性 $dFlux$ 数组，省去其原角循环；资格返回 false 时照常执行原完整循环。原 `finiteRootDirection`、原 noJ primal、原根更新、R466 收缩/数值回退、当前完整 H/J、R273、原 FD、完整 fullDN 与最终物理审计没有被绕过。

为避免再复制约 303 KB 的薄适配源，本入口公开一个普通标准库源码生成器和一个显式文字替换计划。在新 Actions 同 job 内，它们从真实已发表的 208 源字节生成 **11 个独立命名、独立 SHA256 的临时源码视图**。这些视图是实际执行的模块，具有真实私有 `HERE` 路径；它们不是指向旧源的假标签，也不是编码科学结果。完整生成源仅在 Actions 临时空间存在，公开库保留可确定重建它们的原源、全部 literal 替换、每项计数和最终完整身份。

原 208 来源：

- 科学组件与 R466 已发表提交：`4d647c2463809a6d4ce18e588bb40ec9148d98f9`。
- 原 208 请求/工作流提交：`9b05bfc5160bf667cde0cb0ba059b0c8b0332bd5`。
- 原请求：40395 B / `435e90b615b1d5416794c490f7ba9493c5425e19c442de02083807dfa935a5fe`。
- 原配方：11195 B / `1c738c956d9868689e0654adf143d08d4d4a06ed0b6239e6b930c2dfb4cad691`。
- 原工作流：32103 B / `101a84f5827b02744b0ce67dd1c7075bea05e087703985f121e15ca807dfe802`。

原 208 运行、请求和所有公开源保持原字节。新入口不消费其状态、根 tape、J、响应缓存或未返现场；原 run43804793905 仅说明已选源码的实际运行来源，不是新计算的已接受父场。

R471 四件已发表于 `d004a4e421408e9b4b7b7dcd871d661f1d28b3e1`。本入口使用：

| 角色 | 原完整字节身份 |
|---|---|
| 零通量资格 helper | geometry_20261116_zero_nonlinear_split_flux.mjs；7111 B；e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde |
| 新完整 variation | geometry_20261116_original64_zero_flux_contracted_finite_trace_variation.mjs；12597 B；d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0 |
| R471 条件证明 | 15466 B；3d1a57be21c549f7f8bfdb9abe99d945d8f10bb92576bf82c1e48c300fb97922 |
| R471 模块接口 | 11811 B；bf631c438a9b470f0fd30903d6a8ea61490f2d9b1297ed5aac18c485be97d634 |

## 2. 公开新增文件与源码闭包

下表是本入口新增的五个运行/参数文件；本接口是第六个发表文件。准确完整源码视图与逐文件完整差异作为主控临时阅读材料，不重复入库。

| 文件 | Bytes | SHA256 |
|---|---:|---|
| root_20261116_zero_flux_contracted_source_views.py | 15871 | d07ec0105b261f044b1ce3def30853bd7a5f0345603280d032416b40e9091039 |
| request210-zero-flux-contracted-source-plan.json | 35215 | bc167385010dbcb29e561bca39f0b133716360d0fbcb600b0a84de275137bed0 |
| actual119-batch3-zero-flux-contracted-trace210-lambda0p001-recipe.json | 13544 | 67d7db28500af90f3995d2eb9557b3f55c4e39403f82b47d6b66d7d4d82b4f28 |
| public-six-control-zero-flux-contracted-trace-r273-request.json | 67622 | 5b6e87877abdeaa8c089ca1cbfb2df85769a9dc6c28b7869cbd816c6cb919fed |
| visible-larger-public-six-control-zero-flux-contracted-trace-r273.yml | 37506 | 818a97f7dbaad4d6c4f40befde72871a26f943a7a84674a6efe03b1c0ae9b5eb |

新请求分开声明：

1. `published_source_sha256`：原 208 的 **140 个 source pins 逐键保留**，再加 R471 两源和生成器，共 143 个真实公开源。
2. `generated_source_sha256`：11 个独立生成视图。
3. `source_sha256`：前两集合无重名的完整并集，共 **154 项**，是本次实际私有源码目录的完整声明。
4. `source_views.plan`：独立公开 source plan 的完整 file/bytes/SHA；它不是忽略身份的运行时自由替换器。
5. 新配方、请求、证明等各自按完整 descriptor 绑定，不伪计为 154 个科学源码成员。

原 145 的 115、195 的 127 和 208 的 140 份既有 source pins 全保。原 c6a1 fullDN、原 family、原 full response、原物理边界/审计、原 R273 factor 和 dyadic residual、原 3b8 规则 runner、原 source-dependencies 清单等仍使用真实旧字节。旧 195/208 入口作为来源保留，不作为当前入口再次执行。

R471 variation 仍直接导入原 R466 helper：
`geometry_20261116_recorded_factor_contracted_solve.mjs`，
11427 B / `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59`。

## 3. 源码视图的确定性合同

生成器 CLI 为：

```text
root_20261116_zero_flux_contracted_source_views.py
  --request <真实 public request210>
  --expected-request-sha256 <新请求完整 SHA>
  --public-computations <GITHUB_WORKSPACE/题目/computations>
  --out <RUNNER_TEMP/visible-original64-zero-flux-contracted-trace210/runtime-source-views/computations>
```

生成器只使用标准库、源文本和 JSON 元数据，不导入任何科学模块，不运行科学构造器，不执行生成源码、不做 AST、编译或对拍。它执行的实际顺序是：

1. 核真实公开 Actions repository、`GITHUB_WORKSPACE`、`RUNNER_TEMP`、新 request210 schema/number 和已选完整 request SHA。生成器自身必须位于声明的真实 public computations 路径，且字节匹配新请求的公开 pin。
2. 从原公开 208 request 的真实 file/bytes/SHA读取旧 source map，确认其恰有 140 项且全部原样位于新公开 map。
3. 核完整 source plan：原 208 请求、全部生成输出 SHA 与新 request 一致。计划列出 49 个共享 literal patch 定义；每个视图另列实际使用顺序和每项准确 occurrence count。
4. 在全新的私有目录复制 143 个实际公开源，逐件按真实原字节 SHA 核对，源文件不是符号链接。公开文件不写回、不改名、不修改。
5. 每个视图从其声明的 **原公开 base** 全文开始，仅按列出的 literal 替换依序操作。每个 before 必须正好出现声明次数；每个完整输出必须同时匹配声明 bytes 和 SHA。输出名必须是单 basename，不能逃出私有目录。
6. 全部 11 视图都写完后，按真实原字节复制新 request、recipe 和 source plan 到私有目录，分别保存 public/private 身份。
7. 只有以上工作全部完成，才写 `runtime-source-views/source-views.json` 完整 receipt，并向 `GITHUB_ENV` 写实际 `VISIBLE_COMPUTATIONS` 和 `VISIBLE_RUNTIME_SOURCE_VIEW_RECEIPT`。

计划中的完整输出身份是当前源的身份；没有把生成源冒作某个不存在的 Git blob。原 base、替换内容/顺序/计数、完整输出 SHA 足以将它与实际生成文件联系起来。该合同是正常源码集成绑定，不是额外数学接受门、科学 fixture 或独立数值核验。

生成器还提供 `bound_source_view_receipt(comp, request_file, request)`。实际新 runner 和 reader 使用这个标准库函数核本 job/run/source、真实私有路径、原 public request/recipe/plan 与私有副本、完整 154 源以及成功 receipt。它返回必要来源元数据；不会代算任何 root、矩阵、残差、FD、域或审计。

## 4. 真实路径与导入

| 责任 | 实际路径/来源 |
|---|---|
| Git 与规则同步 | 原真实 `GITHUB_WORKSPACE`，从不改成临时源码目录 |
| 公开源输入 | `GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations` |
| 新实际模块目录 | `RUNNER_TEMP/visible-original64-zero-flux-contracted-trace210/runtime-source-views/computations` |
| 新 request/recipe | 该私有目录中的原字节副本 |
| 78 原 source 恢复 | 原 `prepare_public_source(Path.cwd(), ...)` 明确收到真实仓库，输出独立 `original-public-source` |
| 原数学输入 | 原历史 commit 恢复到新 namespace 的 `mathematical-inputs` |
| 两冻结 ready | 原真实文件恢复到新 namespace 的 `frozen-geometry-inputs`，经原环境变量显式传入 |
| Node 原 source root/topic | 恢复的真实 `VISIBLE_FLEX_SOURCE_ROOT`/`VISIBLE_FLEX_SOURCE_TOPIC`，不指向生成源目录 |
| 科学/规则/reader 导入 | 实际私有 `VISIBLE_COMPUTATIONS` 和相应 `PYTHONPATH` |
| 生成 receipt | `runtime-source-views/source-views.json`，完整 source/run/job 与 public/private 身份 |

已逐文本检查的实际 caller 边界如下。

原 3b8 rules runner 的仓库来源是 `GITHUB_WORKSPACE`；复制它不会把 Git 操作转到私有目录。原 public_resume 的函数明确接受 repo，工作流仍调用 `prepare_public_source(Path.cwd(),...)`，不调用依赖 `__file__.parents` 默认 repo 的旧 CLI。

新 protocol base 有一个真实必要修正：原 `REPO = HERE.parents[2]` 在私有目录会指错，因此新视图显式使用 `Path(os.environ['GITHUB_WORKSPACE']).resolve()`。其 `public_asset` 的安全相对路径、原 Git 读取和完整身份规则不放宽。当前四输入、base config 和两 ready 仍按原合同显式给入。

原 family/prepare/fullDN 的相邻源检查实际走它们自己的 `HERE`；声明的143份公开source已复制到同一私有目录；R472确认其中仍漏原physical response递归依赖，不能称完整可执行闭包。新 full112、client、hook、system、QR、height、loader 和 flow 都以新独立 basename 真正加载，不存在只在 receipt 上改来源名的转发。

原 loader 的 sourceRoot/topic 仍是被恢复的原求根/分裂源码。它保留原 exact capacity/observer splice 和逆向恢复检查，随后明确导入新的私有 flow。新 hook 逐个核 loader/flow/variation/R466 helper/**R471 helper** 的实际 SHA。新 full/client 的真实 PINS 同样包含 R471 helper。

新 reader 依赖标准库生成器模块。因此实际科学 PYRUN、规则父进程读回 PYRULEOWNER、清理 PYCLEAN 都显式使用私有 `PYTHONPATH`；reader 文件作为脚本运行时，其真实父目录也是该私有目录。未用公开模块假装私有 `__file__`，也未改任何既有 path 检查来绕过真实来源。

## 5. 11 个实际生成视图

下表均由 source plan 从对应正式 208 baseline 生成。完整 baseline bytes/SHA、literal patch 顺序/计数和每份全差异均另有明确记录。

| 实际临时文件 | Bytes | SHA256 |
|---|---:|---|
| geometry_20261116_original64_zero_flux_contracted_finite_trace_flow.mjs | 9463 | 800a1a5f3bed422ecb343284416cc143b8932c498d4e6f5dae788f65087fa1c2 |
| geometry_20261116_original64_zero_flux_contracted_finite_trace_loader.mjs | 11289 | fccf2c7c528a377300bba85dad976ae407ed4f0ec141ce1066ce52541ab92f61 |
| exact_20261116_original64_zero_flux_contracted_finite_trace_tail_base.py | 20250 | b58896d529b979910d5bcb8955bd2ff8629c0bf3c387476e7b1df314e8311530 |
| geometry_20261116_zero_flux_contracted_trace_r273_tail_client_hook.mjs | 54780 | d02da6b8d7bbb4a6ce1a30d3ed55559401e75a312d811258ed671b339de19971 |
| exact_20261116_zero_flux_contracted_trace_r273_current576_system.py | 29325 | 4197aa0ac5f29a947f753380489797efe2ef8c9c1d5375ca39e80deb1cd90180 |
| exact_20261116_zero_flux_contracted_trace_r273_current576_chain_qr.py | 22065 | 099a0d2919cb3d3569d827e6d8fa90461d7b67c9fa31a7ead189d9b0476f7dcd |
| geometry_20261116_zero_flux_contracted_trace_r273_tail_client.py | 20837 | 2936e1bb32043c9cd7a5487ff4767c5d25cf6ab0d96f3054a0f8bd5911329104 |
| geometry_20261116_zero_flux_contracted_trace_r273_height_path.py | 23989 | 6f2a0d42921a92689d62b58766152175d91b8fed8850959942d4255b07c6e4ea |
| geometry_20261116_six_control_zero_flux_contracted_trace_r273_full112.py | 50182 | 79d174b34c8bd3574db189c727c0fba633f82bca85d09c1b000ee8d56c870dcf |
| root_20261116_six_control_zero_flux_contracted_trace_r273_run.py | 14904 | 6cbb2404a314061916d9e6e68ebee77a2bdb1379b86a869b161998bdb13e14dd |
| root_20261116_six_control_zero_flux_contracted_trace_r273_scalar_readout.py | 45743 | a13fe1105958d7439c609b4d8cf229c0c5c29ac79224c206235a3ebab1e801a6 |

这些视图合计 302827 B。它们保存在主控临时 review 目录和未来 Actions 私有源码目录；这 302827 B 不作为重复源码新增到公开库。

除新 R471 科学模块外，视图改变限于实际模块名称/导入、独立 schema/backend/环境键、来源 SHA/PINS、真实 public repository 定位、source-view receipt 和必要统计读回。完整 noJ 状态、原根和 RK 算术仍由原 reversible source splice 与原 flow 正文保持。R273 数学 factor、完整 current576 行和原 final gates 不因此重写。

## 6. R471 的准确适用范围

R471 的资格判断发生在原 `finiteRootDirection` 已返回之后。它从实际 tape/state/root/direction/tables 检查条件，不根据“零场”标签或旧结果推断：

- 实际无外给根初猜、成功空更新轨迹、原 iteration0 返回，以及完整实际零 shape 状态/返回根；
- 完整 $J=M+1$、$K=2M$、$K+2$ state、所有 $J K$ sparse 初始方向词；
- 每个实际 angular row 的所用零 primal 量、实际原 `angularPartials` factor 和完整有限偏导；
- 每个实际 frequency/cosine/sine/形成系数以及全部 shape direction pairs 的必要有限性。

mean 状态本身不要求零。R471 不以未用到的 $q$ 或 $b_m$ 作为新资格门，不假定离散三角正交，也不把原括号改成解析简式。原 `+0` 累积的有符号零责任见已发表 R471 证明。

资格 false 只选择原完整 nonlinear angular loop，属于同一数值实现的内部算法分支，不是 BVP/native/FD 接受条件。资源或其它异常没有被捕获后重跑。资格 true 仅保留原已初始化的完整 $M\times K$ 正零 $dFlux$；之后原全部矩阵装配、linear 项、$+dFlux$、两个 mean 行和最终 finiteArray 检查逐原正文继续。

因此，**零更新根分支没有借 R465 新公式改写**；原 `finiteRootDirection` 的 $Dt$ 返回仍完全执行。变化只可能发生在它之后的非线性 flux 形成阶段。新 policy 的 `zero_update_path_scope` 明确限制“原零更新路径保留”这一措辞，不能把它误解为后续所有旧角循环都必定执行。

R471 的局部正零结论不等于完整运行逐字相等或加速保证。实际资源检查次数、计算耗时和何时遇到原预算仍可能不同；当前没有运行时间、收敛、全 J 完成或下一步接受的预填结果。

## 7. R465/R466 与完整有限根责任

新 variation 继续逐次消费原真实有限根更新、原选中 alpha、原 recorded $R,z,s$ 和完整 literal Gram 225 slots。R466 的名义系数收缩以及显式旧因子循环 fallback 原字节保留。

该模型在每个实际基点固定缺陷 $E_0=R_0R_0^\top-C_0$、$a_0=R_0z_0-F_0$、$b_0=R_0^\top s_0-z_0$。准确实模型与旧名义递推的关系、一般变缺陷导数和新浮点运算顺序的边界仍由 [R465](../results/R465-recorded-factor-backsolve-defect-and-complete-column-contraction.md) 与 [R466](../results/R466-recorded-factor-contracted-finite-trace-implementation.md) 给出。本入口没有把有限因子当成准确 $C$ 分解，没有无条件置零一般缺陷导数，没有新增 IEEE 导数或误差界。

原 30 次根循环和 20 档内部回溯保持；成功返回的已接受更新数仍为 0..29，原第30次更新后的 iteration-limit throw 也没有转成成功。原 30 项实际返回直方图、原 root evaluation、line trial、normal/fallback、accepted update 和 complete local J 计数都保留。R471 不绕过这些统计和实际根调用。

每个 current stage 仍承担全部 224 shape 方向、226 state rows 及两个 mean。原 noJ RK 四个 primal field 全部完成后，才用实际 tape 形成对应切向。当前完整 stage 变分不代替 endpoint 338×112 response；后者、原 finite second derivative、height path endpoint J、原 FD 和独立 final audit 仍各自必须实际返回。

## 8. 参数、初猜与接受条件

新配方继续选 actual119 第三批真实六词：

```text
p1     0.41654476801167684
p2     0.23884336093393582
p3     0.5270922473095916
theta1 -0.13437878055563054
theta2 -0.005765450212224129
theta3  0.4141025261683763
lambda 0.001
```

原三 active=[0,1,2]、三 frozen=[3,4,5]；新入口从 fresh-circle-low-three-linear 初猜开始。actual119 的原 status/summary 身份和选择范围仍完整留在 recipe.origin/request.parameter_recipe。它不是原第八批点，也不是 native parent。

原四数学输入、两冻结 ready、历史 `8bd267107cc8710d371f3b62c02986655ac965b0`、全部源恢复和原无 initialCheckpoint 约束不变。不从旧 SHA 构造已清状态，不复用当前 H 的旧响应/J，不把失败场当可续 pair。

| 原责任 | 保持的实际值 |
|---|---|
| 物理/尾 modes | 全112 |
| field/native quadrature | 2048 |
| 每节点物理未知量 | 338 |
| core 完整未知量/自由高模 | 112/109 |
| 三 active 后增广未知量 | 453 |
| 全 current original rows | 129248 |
| 全 current stage/penalty node | 576/577 |
| 完整 shape/state | 224/226 |
| 原 native | 至多32轮、每轮原10档、tol2e−9 |
| 原 outer | 至多8轮、原17档 |
| 原域/RMS/BC/FD门 | 原实现不变；RMS1e−6、BC1e−11、FD5e−5 |
| 原离散容量 | max_nodes1200，material_angles=physical_angles4096 |
| R273 | eta CLI文字1，2 exact workers，factor容量2GiB |
| Node | heap6144 |
| 高度路径 | 先真H=0；首正s=1/64，成功增量×2、最大1/4；最多64请求含zero及endpointJ |
| 失败策略 | 首正H原数学拒绝后停止，不额外反复减半；零/中间请求jacobian=false，endpoint=true，原内部withJ责任保留 |

新 source-view schema 说明当前不同来源，不能据此削减完整112、224、225、226、338×112及原453/fullDN相关责任。原全 residual、域、merit、trial、finalJ、sensitivity、物理审计仍按原 driver 决定；没有加入低三元达到阈值才允许本实验的额外前门。

## 9. 原钟与执行顺序

计算 job350分钟、science step330分钟、科学 wrapper18000秒保持原合同。生成/源码绑定/输入恢复是原科学启动前的源码准备；原 wrapper 一旦启动科学 child，使用同一绝对 monotonic deadline 向 finite root、R273 factor 和原 height path 传递，没有按 root/方向/FD 重启钟。R273 原末60秒传输余量不变。

实际顺序：

1. 正常 checkout/runtime 与新 private source views。
2. 原源码闭包、原配方和正常 Actions 语法检查；原 Python AST/compile、Node `--check` 仅在公开 Actions 进行。
3. 恢复原四数学输入、两 ready、78 原源。
4. 原 3b8 规则同步 runner 调用实际新 private runner；原 README 同步、pull/rebase/变化停止逻辑保持。
5. 新 runner 启动一个实际独占 process group 内的完整 full112 driver；原输入preflight、zeroH、正H/currentJ/R273/原试步、endpoint/FD/fullDN/final audit 依真实原控制流执行。
6. always 必要 reader：先按原 PID/start/PGID/SID/boot 身份确认或停止本请求自己拥有的进程组，再读本次实际记录。
7. 原规则父进程独立身份确认；完整必要 marker 与 fresh quiet 齐时才删除整 namespace，包含临时生成源码。

18000秒是有限资源上限，不保证完整 zeroH、正H J、原32轮或所有 final责任可在本 run 内完成。预算终止是资源 partial，不能填成数学拒绝、完整 J 或 native success。新 R471 支路未测，不给加速比例或预算必成结论。

## 10. 必要读回与新统计

新 reader 保持原单份 ASCII JSON ≤90000B，原科学结论与传输完成独立。原逐次 native call、所有已返回 iteration/trial 的必要值与失败地址、current R273、FD门、全DN/最终域、源/输入/参数、末phase和已知未返回范围照原读者保留。不通过数组打包或语义分段绕90KB。

新字段只增加：

- public/private source-view receipt 的完整身份、真实目录、run/source、原208请求、源计数及完整 source map canonical SHA；
- R471 的真实 scope 和 source/proof；
- `zero_nonlinear_flux` 的8个实际整数计数；
- 原 fallback reason counts、缺计数范围、声明scope分组，以及每个已记录 engine 的真实 `last_observation`（含 unfinished phase/angle/direction_pair/sparse_row/原原因/原位置）；
- 明确 full per-call eligibility history 未记录，不从计数反推独立状态数、全角逐值、全部J或 native接受。

原 `factor_contraction` 的完整计数、原原因和最后数值 fallback/unfinished 地址不删。根返回、更新、iteration直方图等原计数也不因新增资格分支重计。counter 是累计实际调用，不能代替“全部576 stage完成”的真实完成记录。

完整角/方向数组、根 tape、因子/Gram/Q/Gamma、全部精确行账和大科学 JSON 都只留 Actions 临时。新 readback 不搬它们，不由其 SHA 还原内容。必要摘要超90000时沿原明确70/transport_partial，不拆包、不升限、不截断成成功。

## 11. 失败、未开始与清理边界

需要明确区分四类事实：

1. **源码生成失败。** 生成器只有全部成功才写完整 receipt。在此之前发生真实源缺失、计数、SHA、路径或I/O错误时，可能有临时部分文件，但不存在可声称完成的 receipt。Actions 该步真实 stderr/traceback 保持在原日志，后续正常依赖的科学步骤不启动。always reader可能尚无可执行的新私有 reader，不能据此声称生成过必要科学摘要。工作流专门记录 `source_view_generation_outcome`；非success时清理明确 `removed=false`、`complete_source_view_receipt_claimed=false`，保留临时 namespace 至 runner销毁。不会制造一个成功 source receipt、科学结果或旧run替代品。
2. **R471资格false。** 这不是退出或新数学拒绝，实际执行原完整 angular loop。原false原因与计数照真实字段返回。
3. **实际科学/资源失败。** 沿原 selected-root/noJ/R273/driver 的原错误和预算控制，所有未返回阶段保持未付；没有捕获错误后换算法重跑整段的额外机制。
4. **读回/quiet失败。** 原 summary/marker 或实际拥有组静止未成立时不删仍活跃或未读raw，不把hash身份当内容完成。清理状态必须按本次原日志填写，本文不预填未来 `removed`。

新生成器不创建科学 child，不新增独占进程组，也没有取代原 runner 的 group owner。生成失败时“保留直到runner销毁”是正常错误保留规则，不是声称有可跨job续接的状态。下一实验仍须重新生成原输入和当前场。

## 12. 来源条件与本地完成范围

此次严格可检查的源码组成关系是：

- 对全部原140公开源，新请求保存旧SHA并在实际生成时逐字核。
- 对11个view，原完整base + 有序literal替换及计数 + 完整新输出SHA决定唯一源文本。
- 生成器、sourceplan、recipe/request/workflow分别有独立完整身份，真实运行不借未知中间稿。
- 新科学正文来自已发表R471两源；R466原helper仍固定 SHA256 2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59 的原字节。
- 已列 full112→protocol→Node capacity→finite-trace loader→flow→R471variation→原helper/source 的名称/身份组成仍保；R472实际在更早的原physical response递归导入失败，故全链实际导入闭合未付。原源码恢复仍是真实repo/source-root，不伪搬其仓库身份。
- R471提供局部资格分支条件证明；R465/R466继续限定名义切向/因子缺陷范围。它们不提供新 native结果、连续闭面、全误差界或性能结果。

源码、所有baseline完整差异和参数文本已完成；本地没有执行生成器，也没有运行其生成模块。主控对源码的必要阅读不构成另一次科学 gate。未来 Actions原正常语法通过后直接进入原完整计算，不另建fixture、对拍或审核步骤。

根提供的原208 source tree元数据是：topic tree `dfd45860420f4195615573af1c13e30f45d50785`，9224 blobs、198353626 B、9598 entries、truncated=false。本入口避免把302827B薄源再复制入Git；最终公开增量以本次六文件实际bytes求和，源生成所用source metadata不编码科学数据。该容量说明是该已读tree时点，不冒动态main的未来大小。

## 13. 发表和实际结果责任

公开发表六件：生成器、sourceplan、新recipe、新request、新workflow和本接口。R471已发表四件不重复新增。临时 `generated-review-only/`、11view全文、`all-generated-views-relative-to-published208.diff`、三个入口完整diff和manifest仅供完整源级核对，不作为论文证据档案或大数据提交。

主控唯一Git/ref/dispatch；新实际source/run/job必须取官方元数据后绑定。206/R455、207/R460、208/R467及未来210/R472的实际结果分别由既定唯一owner读取；运行中只查metadata，不下载大日志。本文没有读取未来210现场，也不将208当前任何未返回阶段预写为成功。
