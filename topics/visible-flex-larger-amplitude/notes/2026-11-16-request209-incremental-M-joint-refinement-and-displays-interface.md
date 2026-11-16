# Request209 — 同一 job 的联合精化、增量 M 族和多时刻显示接口

作者：AI（geometry）；日期：2026-11-16。

状态：**独立源码、调用合同与条件证明；未执行 request209，没有实际父场或实际数值结论。** 本文对应 [R468 条件证明](../results/R468-same-job-incremental-mode-joint-refinement-and-display-composition.md)，实际结果另记 R469。root 负责唯一 Git 发布与公开 Actions 派发；本地工作只有源文本、JSON、字节身份、完整差异及纸面推导，没有项目 import、AST、compile、科学测试或 fixture。

## 1. 可执行范围和原科学责任

本请求在新公开 job 内真实执行完整的 [request205 子合同](current-C-actual202-accurate-ten-closed-geometry205-request.json)，其154源码、五份原输入及完整来源、C 全根族、准确十族构造、真实 H/J/FD、full453 到相同末十词的 full450、原接受门和第一次全闭面参数均保留。它不读取旧205运行的大场作为新解，也不修改已刊205、207或任何已刊数学核。

原205实际接受的场记为 level0。新增真实次序是 level0 → R456 的五因子112模态精化 → R464/R463 的 M128 精化。第二后继只有前一个实际 owner 接受后才开始；不能在 R456 失败时回退到旧父，再称为联合精化。M 后继采用 R462 的完整旧112族与新模态 union，保原112实际 far/μ、所有候选和误差；全 M deep、新 grid、新 native/J/BVP 及末门仍重算。

每个真正可用的场独立进入几何、必要误差测量及显示。metric、reach、held、误差比较或显示的成功不是下一 BVP 的新增接受条件；这些操作真实消耗同一剩余时间，故它们的资源成本会影响能完成的后继范围。它们不能被称为无成本只读。读取阶段只读取实际输出，不再评价科学场。

源码通过、finite BVP 接受、某次四 Loewner 布尔通过、误差上界改善、严格误差下降、连续嵌入、reach、held 与显示是不同结论。本文不把任意一项替代其余项，也不预填任何一个将来的接受场、K、τ、构造高度或完整证书。

## 2. 原合同、已刊依赖和最终运行身份

原205 request 为97406字节，SHA256 `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`；原 workflow 为95760字节，SHA256 `726d97e1aada5d34ddfa949753ce59c6909122d3de8c39bd5a2160fdb8712c36`。两者在209仍是完整被引用的真实文件，不是拼成的新标签。

编排基线207已刊于 `1e05442404d3867fc09589a523e594202efde7c0`，request 为21956字节、`c798f376a63d552c12ff56b51fba8f11ed46bba4d858ec95df2838cfe3575015`；workflow 为98422字节、`37f426a26c97f637fae74cdcf185fb3ef5fc5025114a7b852613f9417673627e`。209 保留207原75条新增 source pin，作为明确来源闭包，不把旧207三个编排器当209实际运行入口。

关键新增组件已独立发表：R462 `b885a23c53246f59e066197b33bbfce79f6813d8`；R463 `fe22861dc97e556bfa1849b7b3e925ff390c4d57`；R464 `48ff34fb11881ffb9353a0fda21c571207217cab`。所有来源值见本请求的完整 `additional_source_sha256`、`roles`、`additional_exact_source_contracts` 和 `source_view_generation`；它们分别承担原数学源、调用角色和现场生成视图，不能互相代替。

| 文件 | 字节 | 完整 SHA256 |
|---|---:|---|
| `geometry_20261116_request209_owned_roles.py` | 24996 | `0dc290a21ae8a4e12b4d7e828145ef4405127fd7eb0a8109561ba77ac2e82042` |
| `geometry_20261116_request209_joint_refinement.py` | 48374 | `96b969e5e77fe0778146d16605d9a1e4d4ef0dd40bf3660e909449e6ee467d45` |
| `root_20261116_request209_refinement_necessary.py` | 39850 | `acdea641446ff8bbcb7177b59ff6c83365eafd7f0e17fd6512149262eef9cc00` |
| `current-C-actual202-incremental-M-refinement209-request.json` | 36220 | `aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009` |
| `visible-current-C-actual202-incremental-M-refinement209.yml` | 96476 | `1c53b3c27ab531b99308150a7213e15d17717c57cff846b1dbffe0ffc9e5d65a` |

这五件才是本次新增运行文件；证明与本文另行发表。完整统一差异、文本构建脚本、`source-build-identities.json` 和 `publication-files.json` 只是暂存交付材料，不是新增科学输入或需要执行的前门。没有复制未改动的数值内核到新文件。

## 3. 245 个已刊源、15 个真实生成视图

原205154件加原20775件，再加本次16件，合245个已刊源码；本次新增16件为 R462 三源、R463 两源、R464 七源、R461 原 display 一源和209三源。原同名 source 的 SHA 必须保持；不能因扩 M 改写旧112绑定。生成器自己的基线依赖也在这245件内。

另有15个 source views，合计实际运行闭包为260件。它们的预告文件名、字节数和 SHA 在 request 中完整列明，但**生成之前没有这些文件，也不把它们列成普通 Git 下载槽**。真实过程是：

1. 将原205、207及本次已刊源放在真实 computations 目录，逐字绑定全部245件。
2. 绑定 generator `geometry_20261116_incremental_M_source_views.py`：42983字节、`68ae7071a4e41beedc1dbaea65f14f60e5e0fe0793a1b7f2daaacfd73f9b7bf7`。request 的完整预告表须与该源实际 `VIEWS` 一致。
3. generator 的自身 `HERE`、R463 driver 的 `HERE` 和实际 `cfg.computations` 必须是同一个目录。15个新 basename 必须全不存在；不覆盖旧源、不把已有文件当缓存。
4. generator 先在内存验证全部基线、实际替换次数及所有新 SHA，再独占写新名；实际结果写入 `BASE/source-views/source-view-result.json`。
5. 读该实际 receipt，核 repository/run/source、实际目录、全部 `generated_sources[].actual_source`、完整文件集合、无 current target、无未确认后缀及无错误，再对15个实际文件逐字重核。
6. 只有生成与实际绑定完成后，Actions 才执行原语法预检和新的科学角色。本地没有执行这些预检。

若生成器只写了部分文件，保完整已生成/当前目标/未确认后缀，原 always 读取仍执行，新增科学不开始。所有已生成文件只在本 job 临时 computations；没有把展开的原全文写入 Git。该工程来源失败不是关于 C、BVP 或几何的反证。

| 实际生成文件 | 字节 | 完整 SHA256 |
|---|---:|---|
| `geometry_20261116_continuous_ten_incremental_M_saved_prefix.py` | 19270 | `959b1a2b54fd0da8be14c2228d91ca1d1ef312966d6f4ba40be4bbeff4247ce9` |
| `geometry_20261116_current_C_incremental_M_radial_readout.mjs` | 24141 | `513494eb4569905d45e02326e388fec65e2e42b211ce8e30de31522618295bb9` |
| `geometry_20261116_current_C_incremental_M_shared_field.py` | 49511 | `55a1fb95b574651bac6458034b5f85c46180172189d7a8010758e786087a4c04` |
| `geometry_20261116_continuous_ten_incremental_M_prefix_metric.py` | 32810 | `fd74b6ad9dc1b6069b016dd7fce14e0c35215bc76b045682172e3e10522a7402` |
| `geometry_20261116_current_C_incremental_M_original_cuff_atlas.py` | 29440 | `14f79dcc67488e9bda3c654ca308a59c3d8142eaaf6d350cc3c9277f8bc7b2e5` |
| `geometry_20261116_current_C_incremental_M_accurate_cut_patch.py` | 26131 | `8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2` |
| `geometry_20261116_current_C_incremental_M_fixed_cap_balls.py` | 23668 | `3f43b4bf5e3d4e3134904a772abbf36483e1470174a1df9a3657edf03fbfe811` |
| `geometry_20261116_current_C_incremental_M_live_query_complete_metric.py` | 55099 | `2592d09e9dc471679d4e6d8588a409c3a180132b3b478fc47fbeb1a9d91886f8` |
| `geometry_20261116_current_C_incremental_M_complete_reach_cover.py` | 60498 | `710719dca6ff474c3c73f378b9bba04fad3c5621c86487147d4fe715a47f6f61` |
| `geometry_20261116_current_C_incremental_M_complete_block_reach_cover.py` | 45633 | `afa18a5d303806e1a644186ce326644110f0e6a262b878d988b07b5712606ebe` |
| `geometry_20261116_current_C_incremental_M_held_and_rigidity_inputs.py` | 53822 | `6d3e56b2f8ab636d03d829c7d9bd244cfd7bbf1db0e4cdda6c9329b064440cba` |
| `root_20261116_current_C_incremental_M_native_necessary_api.py` | 52328 | `4f1c2861a63ba50b6cc6bf3eed4ab2cc1b5fc0a3b7c7de6197b00fd0a810fdf4` |
| `root_20261116_continuous_ten_incremental_M_phase_readout.py` | 19706 | `dfda82d609716948994fae95089e8915027a1b0bb1ea59eb1290c213ec9480e6` |
| `geometry_20261116_incremental_M_fixed_target_metric_evidence.py` | 62333 | `0eb5d8171664db099824698a8319e91a0324344b8d915032ebab932c29707f2b` |
| `geometry_20261116_current_C_incremental_M_multitime_display.py` | 41727 | `e0b47bbfd355032bb433302425d09a4e6be0413107e20ac3d96e7c52586e88cf` |

上表就是完整15件，不存在隐含的第16件生成核。旧 `completeM` 的视图可以保留在来源闭包，但实际 level2 使用的是 `incrementalM` 和其独立 source/schema。

## 4. 实际命令、路径和 schema

workflow 使用原205 namespace `visible-current-C-actual202-ten450-closed-geometry205`。下文 `BASE` 是其真实 `RUNNER_TEMP` 目录，`COMP` 是该 job 完整 computations 目录，`REPO` 是 `GITHUB_WORKSPACE`。路径由真实 workflow 与原 source 恢复给出，不使用用户目录或可重用旧运行缓存。

源码预备命令为：

```sh
python -u "$COMP/geometry_20261116_request209_owned_roles.py" prepare \
  --request "$REPO/topics/visible-flex-larger-amplitude/notes/current-C-actual202-incremental-M-refinement209-request.json" \
  --request-sha256 aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009 \
  --base "$BASE" --computations "$COMP"
```

workflow 在调用前先核 owner 自身 SHA。owner 先保存本次请求的准确字节到 `BASE/refinement209-request.json`，再做上述生成和绑定。预备状态为 `BASE/source-preparation209/result.json`，生成 stdout 单独留在同目录。入口的 schema 为 `R468-request209-owned-nested-role-v1`；实际准备 receipt 加 `-actual-source-preparation-v1`。完整返回0，错误返回2，错误文本与部分 receipt 保留。

全部新科学编排通过原 rules runner 包装：

```sh
python -u "$COMP/geometry_20261116_request209_joint_refinement.py" rules \
  --request "$BASE/refinement209-request.json" \
  --request-sha256 aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009 \
  --base "$BASE" --computations "$COMP" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --proof-directory "$REPO/topics/visible-flex-larger-amplitude/results"
```

`rules` 加载已冻结的 `root_20261114_current576_rules_runner.py`，保真实2700秒规则同步；它的子进程实际进入 `run`。`run` 要求自己 PID=PGID=SID，是原 runner 真创建的独占 session，随后去掉继承 token 环境。`witness --input --input-sha256 --computations` 是内层科学命令，仅消费本编排真实形成的 input。

runner schema 为 `R468-actual205-contract-incremental-M-refinement-evidence-and-displays-v1`。原 deadline schema 仍为 `request205-owned-job-science-deadline-v1`，原 BVP launcher schema 仍为 `R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1`。209没有把这些原205来源重标为新203或新209场。

必要读取和清理分别为：

```sh
python -u "$COMP/root_20261116_request209_refinement_necessary.py" readback \
  --request "$BASE/refinement209-request.json" \
  --request-sha256 aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009 \
  --base "$BASE" --computations "$COMP"

python -u "$COMP/root_20261116_request209_refinement_necessary.py" cleanup \
  --request "$BASE/refinement209-request.json" \
  --request-sha256 aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009 \
  --base "$BASE" --computations "$COMP"
```

reader schema 为 `R468-joint-refinement-one-necessary-readback-v1`；内层 `component` 只是独立 metadata 进程入口，不能改用它执行任何求解。外层 readback 无论 science 成败都安排执行；它仍受原总读取期限限制，不为每个 level 重开2700秒。

## 5. 真实三级父、C 与 union 的输入边界

runner 真读取 `BASE/BVP-launch/result.json`，绑定原227ef601 launcher，读取该实际 result 的 `actual_job_deadline`，再核实际期限文件字节和 recipe SHA。没有结果时不从 namespace 的某个约定文件名推造 deadline、父场或接受。

level0 必须具真实 `current_finite_BVP_accepted`、完整原返回和 quiescence。其两阶段实际 checkpoint、C result、native sampling、原 tail config、geometry、ten recipe、源码与 first procedure 分别绑定。first procedure 来自 `BASE/closed-postsolve/procedure.json`，原 R452 schema/source 保持；首次 A 从 `actual_selected_construction.outputs.first_construction_freeze` 读，B 与首 shared 从实际对应回执读。

level1 的 R456 parent 是该真实 `BVP-launch`。五个显式正整因子全部2：`radial_mesh`、`field_and_native_angles`、`native_steps`、`material_angles`、`physical_angles`。父 mesh 全字词、literal knots 和规定新点完整保；父 Hermite/DY 仅作新初猜，最终新状态与 mesh 以原完整求解实际返回为准。完整 seed 并集超过2400时资源 partial，不能删点。它重求全部450、current H、338×112响应、FD/fullDN/final/audit；原接受门不变；原native最多32次更新、10档trial及2e−9容差等依原完整配置执行，不添加新rank、metric或显示阈值。

level2 的 R464 parent 是**实际 level1 接受目录**，而 old112 far 来源仍是原205实际 sampling result。输入的 `original_far_directory`、`original_far_result_sha256`、`original_sampling_directory`、`original_sampling_result_sha256` 与 accepted parent 是不同字段；`tail_config` 保真实原112配置，不能拿新父 config 标签冒原族绑定。

level2 取 M=128，其余四因子1，从实际 level1 继承角数、steps、材料角及物理角。它保 level1 mesh；因子1不把计数重置为205值。原采样参数完整复制，原 `steps` 被明确移除后由新实际分辨率形成，其他14参数保持。新全 M deep 真实重算，R442 applicability 原证明和参数范围另核；不能把旧112深端证书扩标签。

R462 union 先完整绑定旧112原 input_binding、全部候选族和 raw/误差，再加载新M。旧 Q/Pi 行保同一个真实 far 与 μ 字，Pi 在新128偏移位置重排；新 $m=226,228,\ldots,256$ 实际传播。真实 sample 后调用真实 configure，共用 sampling cap 的剩余时间。configure 原文件留存；派生配置只有声明的可选 `modes` 和 R464 provenance 变化。旧112配置、新父配置、configure输出和新运行配置分别保身份。

旧 far 复用不包含旧 nonlinear response、J、QR factor、敏感度、接受场或新grid其余样本。新 M128物理 BVP 维数514，端点响应386×128，两mean及全部128列真实存在。新原生/RHS/current H/J/FD/fullDN/final/audit仍全部执行。family union 的包围包含不证明所有数值代表属于一个共同准确C realization，严格非共振也不由浮点QR或行单位化自动支付。

若 level1 不接受，level2明确未开始。若 level1接受但其geometry/metric/held/display不完整，level2仍可用实际接受父在剩余预算内求解；这些独立责任不被丢弃，也不变成新BVP前门。

## 6. 角色顺序、同场几何与首构造

完整新角色顺序在 result 中预先列明：`level0_measure`、`level0_display`；随后 level1 的 `solve/geometry/witness/held/measure/display`；随后 level2 的同六项；最后 `compare`。共15个角色，各自保 started、status、实际 exit、cap、error、source/input/output、quiet 和未访理由。

每个新 accepted field 的几何五阶段仍是 `radial_replay`、`original_cuff_atlas`、`shared_field`、`metric`、`reach`。它们使用真实新CP、当前场完整R249/准确cut/帽来源；first A 的 W/H/all signed markers 固定。H常数不是帽目标度量的参数；固定它是构造一致责任。共同材料目标仍须完整 first B、当前 rho、准确逆与同一C/DAG/十词等合同，不因只固定W/H和十词就自动成立。

metric用同C live-query来源，reach用R435完整块/root-pair责任。reach不借metric通过；旧四门OR/R282叶责任、两反射、全phase、两帽及所有未访块保持。source字节相同也不能把旧场证书转给新场。

held前置只需要同场 shared、atlas及真实witness plan，不要求metric/reach成功。新的 witness 实际加载本级 accurate cut field、绑定真实 R413 attachment，解析唯一 left=0且正宽的prefix片，取radial0、physical q为0、1/4、1/2、3/4、upper四点；不复用旧pieceindex。它是新的科学操作，由120秒上限与原绝对钟约束。

level2使用 R464 post 的 kind `R464-incremental-M` 与 schema `R464-current-C-incremental-M-live-query-block-geometry-v1`；held只接该真实tuple。held必要schema为 `R464-current-C-incremental-M-held-after-shared-v1-necessary-v1`，原frame为 `BEGIN_R464_INCREMENTAL_M_HELD_NECESSARY` / `END_R464_INCREMENTAL_M_HELD_NECESSARY`。不能给旧R451 post后贴这个schema。

## 7. 固定目标误差与实际时间细分

三级measure和compare全部使用新 evidence view `0eb5d817…`，避免同一序列混合旧R459和新schema。实际family对应：

| level | 求解来源 | evidence family | display family |
|---|---|---|---|
| 0 | 本job原205真实接受450 | `original112` | `current112` |
| 1 | 本jobR456真实接受五因子450 | `resolution112` | `resolution112` |
| 2 | 本jobR464/R463真实接受M128 | `incrementalM` | `incrementalM` |

误差量是全闭域广义谱opnorm，保上下界、全域责任与固定目标签名。所有闭piece、真实C查询、准确目标正定、两反射和帽均保；不是把某个eta布尔值当真实误差数字。全t上界沿已证共同材料相位共轭以及全角圈覆盖；共同q图方向是当前Theta的逆接首Theta，不能倒置，也不能凭固定g自身旋转对称代替同时拉回。

本次另外真实执行time subdivisions 4/8/16下的嵌套点查询，四个witness为公共prefix u=1/2、q=0和1/4、两side。有限t点不替全t证明。first B缺失时该公共材料measurement明确未付，但求解和独立held/display继续其可用职责。

每levelmeasurement cap300秒，interval bits256、sqrt128、initial angular depth2、depth20、cells100000、measurement width goal1/100000000、metric reference eta1/1000000、inverse80、phase-query cells100000。宽度goal是求值分辨率，不是接受门；机器/native/solver容差不得不经量纲证明就作为这个相对metric的终点。

compare保实际结果：`U_new<L_old`可证明严格下降；只有上界减小则仅称包围改善；重叠、domain/cover未付或缺值则未能判定。任何结果都不拒原BVP或阻下一level，预算允许时仍执行原计划。两次success本身不宣称已完成README所要求的真实加密误差继续下降至机器精度或原solver容差；不增设无限精化或跨级C²收敛门。

## 8. 三组有限显示和文件范围

三个level全部调用同一新 display view `e0b47bbf…`，mode为 `physical-angle-image`，实际时间集合依次为 `{0,1/2,1}`、`{0,1/4,1/2,3/4,1}`、`{0,1/8,1/4,3/8,1/2,5/8,3/4,7/8,1}`，共计划3/5/9frame，严格嵌套。它们不同于上一节的metric time-subdivision点查询。

每级原显示grid参数为 prefix8、tail8、cap4、angle32，interval256/sqrt128/inverse80，cap120秒。真实定义中的全部模态、所有piece与帽仍在；这些只是显示采样分辨率，不裁掉科学模态。physical-image使用当前准确角逆，first B缺失不需伪造共同材料标签；顶点不因此被说成跨level同一首q的对应点。

每个实际顶点的外向坐标误差保存在同job临时原件，实际frame有原PLY及gzip字节身份与各自严格小于5,000,000字节的限制。大小限制原样保，不升限；不保证所有计划frame能完成。必要摘要保每frame文件身份、状态、完整当前未完范围、点误差极值及其地址，不把完整顶点/三角数组回传到chat或job output。显示不能认证面内、全t嵌入、reach或度量；没有上传raw artifact或提交显示大件。

## 9. 一个原始期限、明确资源上限

原namespace创建时间为T0，新科学实际截止为T0+18900秒，必要读取仍只到T0+21600秒。原job timeout360分钟不变；较早的job/step终止也可先发生。旧205前序每个既有预算和startup-clip保持原范围，不能把本次新owner的绝对钟反写成旧整个job一直存在的新增杀钟。

本次新增角色每次调用都用真实剩余裁剪显式cap。只有measurement与compare以`measurement=True`使用终测余额；display仍调用默认`remaining(measurement=False)`，和求解/几何/held一样保末900秒measurement与关闭预留。每子进程关闭预留30秒。新增source生成、input绑定、原阶段setup已耗时间全部计入原namespace，不在任何level重开时钟。

| 角色或资源 | 明示上限／策略 |
|---|---|
| 原205science/读取 | 原18900/2700，原sampling reserve3600和BVP max7200不变 |
| R456 sampling / BVP | 900 / 7200秒，另受真实剩余限制 |
| R464 full-M deep / union sampling / BVP | 300 / 12000 / 7200秒，内部实际余额再裁剪 |
| 每级 radial / atlas / shared / metric / reach | 600 / 120 / 300 / 600 / 600秒 |
| 每级 witness / held / measure / display | 120 / 300 / 300 / 120秒 |
| compare | 120秒 |
| max_nodes | 2400，完整seed不够容量即partial，不丢点 |
| 开始free-space / 运行stop reserve | 8GiB / 2GiB |
| 原规则同步 | 原2700秒真实pull语义 |
| 新readback step | 最多40分钟，仍剪到原读取终点 |

以上cap相加可以超过剩余时间，因此它们不是整链完工保证。M采样内部原14400/1800等子预算按外层实际可用秒数裁剪并写入回执，不把裁剪隐藏为原参数完全未变。终止、未开始、未返与科学拒绝分开记录。

所有新科学子进程用真实 PID/start ticks、PGID/SID、observed descendant sessions和原内部owner收据，TERM→等待→KILL→确认quiet。父rules Python可能继承共享runner PGID，仅核父PID和start ticks；不能要求runner公共组消失。未知scope保留原件而非猜quiet。

## 10. 必要读回：一份新增90KB，原七范围不变

`BASE/refinement209/result.json` 保存实际编排状态。新reader先核完整source preparation和实际十五源receipt，再停止或确认本链旧子进程quiet，调用原对应frozen必要reader，最后核所有读取子进程quiet。原205七份必要读取保持；新增整链只形成一份≤90000字节的必要摘要。

新增摘要保存以下真实范围：

- 全部15角色的实际source/input/output身份、started/status/exit、cap与剩余、异常、未开始原因、当前作用域和未访后缀。
- source prepare和generator的完整结果状态、15实际文件身份、current target、unconfirmed尾缀、原错误及actualcomp。仅当两处实际列表canonical全等，才把prepare里的重复列表改成指向摘要内完整列表的明确引用；不相等或异常时保原文。
- 两个求解owner的原完整necessary范围，包括全部原终门/FD/新J/BVP接受或未返、sampling/deep与子程错误及未开始阶段，绝不把scope hash变成假完成。
- R464的 `actual_new_sampling` 保真实嵌套对象：`actual_original_R462_readback_exit`、`original_result_identity`、`original_necessary_identity`、`complete_original_necessary_scope` 等；不能按旧sampler的 `.original` 假扁平筛选。原112绑定、全新m状态/误差/后缀、真实μ/far字词与完整raw身份按R462原necessary保存。
- 每级五几何/held实际结果与所有明确partial责任；measurement和compare真实上下界、目标签名、source、时间查询/未付与错误。
- display的 `necessary-summary.json`，所有已返frame、`current_frame`、原文件身份、点误差max及地址；完整成功网格正文仅身份。
- 原新规则metadata、父rules返回、ownedquiet、读取进程return/timeout/错误。必要stderr按原UTF8-surrogateescape完整保；只有实际bytes相等才一次正文加多个来源路径。

大型成功系数/列/因子/曲面ledger/逐顶点数组只在RUNNER_TEMP，回传的是原身份与原必要scope，不宣称逐值独核。尚在原大ledger里的每条成功见证并未因为读回摘要就变成chat已读正文。若某原错误文本本身超过90KB，明确标未回传byte-range，不能只返回SHA却称完整。

实际尝试正文先写 `BASE/refinement209-readback/attempted-necessary-summary.json`；若超限，`summary.json` 只写原attempted身份、section字节数与范围，不分包、不编码、不提高90KB，返回70并保raw。任意极端失败列表可能超限，未声称预先必能适配。否则 `summary.json` 是完整必要对象；complete返回0，缺scope/error返回2。

完整frame为 `BEGIN_REQUEST209_REFINEMENT_NECESSARY` / `END_REQUEST209_REFINEMENT_NECESSARY`；step outputs 为 `refinement_summary`、`refinement_summary_bytes`、`refinement_summary_sha256`。新report只重复这份原必要对象及其身份；原205五份report正文仍照旧。第一次closed/held/combined三体仍只在compute，不再把它们全复制进report挤近1MB。

## 11. 原条件全部保留的清理

只有新reader实际complete且quiet才写 `BASE/refinement209-readback-complete.json`，schema为 `request209-refinement-necessary-readback-complete-v1`；字段保repository/run/source、reader真实身份、`complete=true`、`quiescent=true`、必要summary真实receipt以及原refinement result。

最终cleanup需八个实际step outcomes全部success：C、cut、construction、far、BVP、rules、closed和新增refinement。还逐一核原BVP必要marker/summary、rules marker、construction marker、closed marker及各实际文件SHA，新marker/summary和reader身份，以及原205owner与全部新增owner/读取子进程的quiet。不以step绿色替文件范围，也不让新marker代替原七条件。

科学partial可以已完整读回；这时允许按原约定清掉本job所有者的临时raw。source生成失败、必要scope未知、summary70、marker缺失或process不quiet则明确 `request209_cleanup_skipped`，raw只留到runner销毁；不得主动删除未读输出。成功事件为 `request209_original205_and_refinement_raw_removed`。没有把临时raw上传artifact、切块入Git或留下虚假的可恢复checkpoint。

## 12. 差异、规则同步和当前未付

本次workflow仅独立改名/trigger/request路径、245+15预备入口、新增union/display实际角色及必要读取/清理标签；原205科学和原七读取正文保留。将原207冗长inline来源处理移到独立owner后，workflow96476字节，仍小于100KB；这是代码组织，不缩科学范围。

原规则baseline保持根 `21bd547f56590b7f2dd279d0297efb289a9b2783`、题 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`；实际job继续原rules runner真实拉取/比较，正文不把本地读source或API查head冒作git pull。任何后续规则变化仍按原运行停止与partial语义处理。

当前没有209 run/job/source提交、真实接受父、三个完整测量、误差下降、显示文件、全域几何证书或共同准确C realization。两级有限计划不是收敛定理；新旧M的公共材料拉回、准确target、全域cover与solver容差量纲仍需实际支付。R464对新增来源的程序注册不扩大R462条件命题，也不替尚未实现的任意M→径向下一轮来源组合。

发布文件仅本接口§2五件、R468证明和本文七件。暂存manifest、完整diff和源码生成审读展开物不发表为新数学结果。完成本请求以后，任何已返进展与仍未付范围须按R469真实结果继续处理，不能把一次阶段结束称为课题完成。
