# Run33：原 run28 正半波物理母体与 R729 全行恢复的完整参数

准备时刻：2026-11-28 08:30:38 UTC。仓库 Rogerhu12/math-research-public；课题 topics/visible-flex-larger-amplitude。

**这是完整源与参数准备，不是第33组已执行的科学结果。** namespace 为 `fixed-fejer-halfwave-R729-bhalf-first`。当前完整源码的 publication、run/job、输入文件、模型、完整点、QP触发、dual读数、接受、final和typed均为 null；后续真实出版和执行应另附实际记录，不能倒填这份准备对象。root 是唯一 ref、request、queue 与 workflow 发布者。

## 1. 单一比较：改变恢复算法，保留原28物理问题

第33组以原28的完整 demanded 正半波家族为物理母体。原第一中央段为正半波，第二中央段为负半波；端层仍为原 S5 归一化 chord 构造。固定 Fejér chart、完整准确标量定义、当前 M160/J923/N2048、全部三组旋转控制、自由核心高模、自由高度以及所有原域、全32段 normal 方程均保留。

本组不采用 R725 cutoff、R726 球面插值或 R728 反号；不引入第23组的动态阻尼政策。R729内核与第32组共享同一完整文件，但这不把第32组的反号/Slerp物理体带入第33组。当前 seed、mean、base、Q、normal 和 demanded arithmetic 的完整身份都由原28继承；只有完整 source/model/report 绑定能确定未来新运行实际读到的模型，不能预填它与旧模型的数值或hash相等。

本组调用原完整QP后，在准确限定的恢复分支尝试另一种解同一有限QP的方法。原目标、变量、约束、阻尼初值、外层搜索和接受规则不换。保留原28全部137个科学 role 的 basename/SHA 对，再增加共享 `common_slack_dual_recovery` 一项，共138项；当前完整运行文件21件，其中新增 pure helper 是实际所需 stdlib 依赖，但不是额外科学 SOURCE_PINS role。

完整源码交付：

- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-common-slack-complete-source-delivery.json — 18278 B；SHA-256 098639542a0d3673a985d2911c09c842f5f08ae24d2a818ba1917212ff654169；Git blob e61d0cadb352470a95a6ecc87b2b923131e09c7b
- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-current-runtime-binding.json — 64691 B；SHA-256 dbda07a05feeb0bfdd1de2e363b9d003c9291e748cd51a2272247690065851b1；Git blob e8e55f1aabf38b5237585693f38496027836a946
- topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_halfwave_R729_family.mjs — 88329 B；SHA-256 42bc81cac8d4a9c6c267c64ca916eb7a50d6962662c0b8b6833fdac61e12fadb；Git blob 4de97fa40d6c3aa45d0196f5138e4bcdbbaf6db0
- topics/visible-flex-larger-amplitude/notes/2026-11-28-run33-halfwave-R729-complete-source-family.md — 21214 B；SHA-256 7f455a7b24c206df77baade1f9b202baa2c5536ae4a6b92310e37520ea5fb434；Git blob bd45ca3ad6e3d02355ee2664d4d19bd02b8093cf

原28源已刊于 3fa8f98f08649da12ee5b8b9ba5889276285bc84；共享R729内核已随32源刊于6c07ca019af58f0102a40a00c63027948ee0332a。当前新33 source publication 在本准备文件中仍为空。这三个来源层次分别记录，不把原28/32的出版冒充新33出版。

## 2. 真正使用的完整参数父

这里直接读取原28目前完整参数，保其64项live；没有误用原源总表中较老的22组48项live参数引用。

- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-complete-parameter-delivery.json — 26835 B；SHA-256 da1fe6a13e4651a93af189bbe963b4397d9ed67c788391b422730aed889840b8；Git blob bb0276deed1e6e487fc7ce2e3264b0f86776d9cd
- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-complete-parameter-binding.json — 45365 B；SHA-256 27a9467deba43fb964f287ad2df0897260c14bf94ccf624aee62344f1643a0c5；Git blob b591d00267e144934bcf1ea7037f762d7f5ba449
- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-science-complete-ready.json — 73514 B；SHA-256 2103f0942aa047757a0e7c04a8af10ae8ba205907f91a3621151f3b5885f984e；Git blob 157b23f71517ebfa5794e9ff9a7ec98f46069e35
- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-pure-complete-ready.json — 59324 B；SHA-256 8b16a2e79a358af068a68395dbef62130133e7b481ec1c2baf1fc34e21491eb6；Git blob cc6bacf16d723ab0df42efe4b93719f4ce03c0c5
- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-complete-launch-delivery.json — 9195 B；SHA-256 016f15cb305b579a2733f7a55117855aac8ce003753760605c882862fc1261db；Git blob c38edf4037a8bc3721a433220520316745ce219b

本组新完整文件为：

- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-complete-parameter-binding.json — 30172 B；SHA-256 ca81f91c4e5eb6eed2b36b0e731628b6226ab1730e343ac30d06a52c7167668a；Git blob 63cff3ff35deba4309a41cf01fe4cae6e2433700
- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-science-complete-ready.json — 80928 B；SHA-256 d35579f13e07cf004a333905af411c0a47f2147f42c574b9b0c65af7b02b1798；Git blob 8631722f6367d98f4515adce383f49226f69c3cd
- topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-pure-complete-ready.json — 70074 B；SHA-256 19e226f138e2076dc2834f7b3a2449eef633961c4a80159e5933c7f0fa0e290a；Git blob 86116e5b0605b3fc5d24cf8b998695bf65939401
- topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_halfwave_R729_run33_parameters.mjs — 57335 B；SHA-256 9379faa58cb06be42292e1bd9d6208408f704902a57419951103fd0f59b853c0；Git blob 06056ac04ad0040dfe39785336c8c6b7eb3e8a3f

每一新ready内保存完整实际 `steps[0]` 对象，包括完整脚本、scope、parent_bundle、全部argv、outputs、summary、原cleanup、保留固定缓存选项和live映射。ready之外的大段祖先metadata按完整父文件身份和精确JSON pointer共享；原文件的所有文字、原先未知值、早期状态、父历史和完整参数均被引用，未裁成局部摘要。

共享记录的 `whole_file_required: true` 表示文档/恢复合同要求整文件可复原，不是向科学运行增加预检步骤。实际solver、controller与pure继续读取各自原接口；参数再生器只作完整文本构造。

## 3. 全部预算与原数值词

| 项目 | 本组原值 |
|---|---:|
| 当前布局 | M160、J923、N2048 |
| normal stages | 32 |
| angle block / stage block | 8 / 64 |
| integration order | 8 |
| metric directions / maxiter | 1 / 16 |
| restoration directions / maxiter | 4 / 64 |
| line trials | 15 |
| active rows / envelope near-active rows | 192 / 32 |
| metric damping / restoration damping | .01 / .01 |
| seed boundary total length | 1/2 |
| seed profile delta | 1/32 |
| scalar panels | 128 |

其余实际参数并没有从表中省略：下面列出新science完整157词数组。相对于原28数组，只把其原输出namespace替为本组namespace；每一个数字词、顺序、flag、固定输入路径和5对历史pending CLI原样保留。

```json
[
  "--repo",
  "{repo}",
  "--reference-bundle",
  "{work}/fixed-fejer-reference/reference.npz",
  "--preparation-report",
  "{work}/fixed-fejer-reference/report.json",
  "--carrier",
  "{work}/fixed-fejer-reference/observations.npz",
  "--node-report",
  "{work}/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
  "--scalar-input",
  "{work}/fixed-fejer-r690-inputs/fixed-scalar-input.json",
  "--angles",
  "2048",
  "--stage-block",
  "64",
  "--angle-block",
  "8",
  "--integration-order",
  "8",
  "--norm-kind",
  "jet-sum",
  "--radial-norm-length",
  ".05",
  "--angular-transition",
  "24",
  "--torch-threads",
  "4",
  "--damping",
  ".01",
  "--directions",
  "1",
  "--maxiter",
  "16",
  "--restoration-directions",
  "4",
  "--restoration-damping",
  ".01",
  "--restoration-maxiter",
  "64",
  "--line-trials",
  "15",
  "--active-rows",
  "192",
  "--qp-atol",
  "0",
  "--qp-rtol",
  "1e-6",
  "--reach-ratio",
  ".03",
  "--reach-safety-factor",
  ".992",
  "--active-band",
  ".025",
  "--marked-diameter-budget",
  "4.2",
  "--witness-lower-budget",
  ".9",
  "--amplitude-height-floor",
  "1.01",
  "--spectral-p",
  "4",
  "--spectral-epsilon",
  ".001",
  "--spectral-scale",
  ".05",
  "--legacy-fraction",
  ".5",
  "--target",
  "1e-9",
  "--outdir",
  "{work}/fixed-fejer-halfwave-R729-bhalf-first",
  "--panels",
  "128",
  "--endpoint-bubble-1-left",
  "1/32",
  "--endpoint-bubble-1-middle",
  "1/4",
  "--endpoint-bubble-1-right",
  "15/32",
  "--endpoint-bubble-2-left",
  "17/32",
  "--endpoint-bubble-2-middle",
  "3/4",
  "--endpoint-bubble-2-right",
  "31/32",
  "--endpoint-root-tolerance",
  "2e-12",
  "--endpoint-root-iterations",
  "24",
  "--endpoint-root-backtracks",
  "18",
  "--endpoint-root-armijo",
  "1e-4",
  "--moment-definition-sha256",
  "05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e",
  "--moment-input",
  "{repo}/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json",
  "--moment-input-sha256",
  "df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c",
  "--endpoint-control-radius",
  "2",
  "--gamma-left",
  "1/16",
  "--gamma-middle",
  "1/8",
  "--gamma-right",
  "3/16",
  "--moment-input-binding",
  "supported-smooth-triangle-reference",
  "--normal-stages",
  "32",
  "--seed-boundary-total-length",
  "1/2",
  "--seed-profile-delta",
  "1/32",
  "--seed-radial-quadrature-order",
  "8",
  "--seed-profile-quadrature-order",
  "16",
  "--seed-mean-maxiter",
  "128",
  "--seed-mean-tolerance",
  "2e-12",
  "--seed-mean-backtracks",
  "24",
  "--seed-mean-armijo",
  "1e-4",
  "--seed-scalar-iterations",
  "64",
  "--manifest",
  "{work}/fixed-fejer-reference/locations.json",
  "--material-envelope-binding",
  "{work}/fixed-fejer-reference/material-envelope-carrier-binding.json",
  "--envelope-near-active-rows",
  "32",
  "--independent-envelope-branch",
  "--pending-parallel-envelope-run",
  "45909290354/1",
  "--pending-parallel-envelope-source",
  "45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
  "--pending-parallel-envelope-run",
  "45929088658/1",
  "--pending-parallel-envelope-source",
  "45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
  "--pending-parallel-envelope-run",
  "45943410994/1",
  "--pending-parallel-envelope-source",
  "45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
  "--pending-parallel-envelope-run",
  "45972294636/1",
  "--pending-parallel-envelope-source",
  "45972294636/1=c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1",
  "--pending-parallel-envelope-run",
  "46011377225/1",
  "--pending-parallel-envelope-source",
  "46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
]
```

新pure完整7词为：

```json
[
  "--repo",
  "{repo}",
  "--report",
  "{work}/fixed-fejer-halfwave-R729-bhalf-first/report.json",
  "--output",
  "{work}/postprocess/fixed-fejer-halfwave-R729-bhalf-first-readout.json",
  "--verify-final-bundle"
]
```

固定reference输入producer的两步仍是原完整generic maker/reference步骤。这里的半宽1/2是科学种子边界总长，不是改maker的固定标量或mesh宽度。第33组仍将在它自己的runner读取、生成和严格绑定全部必要输入；旧28原始NPZ、model、root packet和final不会跨runner搬入。

## 4. 唯一新算法及其有限预算解释

R729的完整证明与运行体是：

- topics/visible-flex-larger-amplitude/results/R729-common-slack-all-row-dual-coercivity-and-feasible-recovery.md — 16220 B；SHA-256 d6104084c6a96651e478ab4c0b7f25124ca5859ae03e49fdb4d3a35c9264c87a；Git blob a66c19196b798957a6f905c23e47b2b500b60dd8
- topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R729_common_slack_dual_recovery.py — 54333 B；SHA-256 2dfe85c432d91f561a5f9d413f02cbc7d939edab2ea896e7fe4b3f810bc41863；Git blob 2877ba8d6503974b6aa84621997bdc051f523929

旧 `qp.solve` 仍先按原参数运行。完整旧 `record['qp']`、history、transitions、multipliers、状态、face梯度、容差和原计数保留。仅当 phase 为 restoration，且原状态为 `dependent_blocker_at_zero_step` 或 `dependent_blocker_after_feasible_step`，才进入新恢复。metric方向及其他原状态保持原流程。

增广变量为完整物理坐标与共同slack增量，原目标仍是：

$$
f(z,t)=\tfrac12(\tau_0+t)^2
       +\tfrac{\mu^2}{2}(\|z\|^2+t^2).
$$

全部行写成 $C_i=(u_i^T,-\beta_i)$，包括最后的slack非负行；实际 $\beta_i>0$。完整流式列构造 $CH^{-1}C^T$，其中 $H=\mathrm{diag}(\mu^2I,1+\mu^2)$。没有独立行筛选、rank删行、top rows、坐标截断、目标代换或几何域缩小。

每个未来真实方向使用原 `restoration_maxiter` 减去原QP已付 `advances` 的非负剩余整数，作为新完整dual sweeps上限。每个sweep按原顺序访问全部实际行。**新sweep不是旧CG advance**；29项新逐方向投影分别给原advances、允许sweeps、开始/完成sweeps、坐标访问、非零更新和未完整一轮访问数。不能把旧2advance或未来214次坐标更新写成一种相同单位。

有限候选的物理部分求得后，按全部原行作最优slack修复：

$$
t(z)=\max\left(-\frac{\tau_0}{1+\mu^2},
       \max_i\frac{u_i^Tz-b_i}{\beta_i}\right).
$$

原完整C与原物理行必须再次真读。候选与原完整有限可行方向、零步按同一原目标比较，全部错误和原结果保留。实际有限容差可行不等于有向舍入严格证书；数值gap、stationarity、互补与C/Gram差异均明确只是实际数值诊断。R729的准确无限循环收敛不能变成“剩余有限sweeps一定收敛”或“本曲面必可行”。

最后被选中的方向继续进入原完整外层line search、Phi、全六族、永久material地址和真实接受判据。不会因为dual目标改善、slack降低或原算法遇到dependent blocker，就直接计为非线性接受或课题完成。

## 5. 旧诊断与新实际方向分开

原 `restoration_qp_*` formal字段仍来自原CG返回对象。特别是旧face Pg、旧step norm、旧slack与旧状态不能暗指新恢复后的方向。

新增 science 全局字段指向 `R729_common_slack_recovery_definition`；每个方向的新完整记录为 `restoration_directions.i.R729_common_slack_fallback`。pure保原完整检查，并独立消费 `R729_common_slack_recovery` 与 `actual_restoration_directions.i.R729_common_slack_fallback`。后一个前缀是完整现reader的真实键，不是省略 `actual_` 的假路径。

实际被交给外层的方向另记来源、是否采用、自己的完整point、coordinate norm、原目标值、共同slack、完整线性余量与物理g、最终C真读、dual梯度、选中primal stationarity、互补、数值gap/恒等式缺陷和完整流式读取计数。原外层 `actual_QP_seconds` 包围旧QP及新恢复；完整旧QP report里的计时仍是原尝试，新kernel另有自己的seconds。没有把新花费藏成“原QP加速”。

新的pure文件因完整父文本接近100KB，把原 `canonical` 与 `frame_reuse_metadata` 两个完整函数原字移到严格whole-pin的stdlib helper。其原验证内容、参数、结果与异常不删，helper实际来源也入pure输出。它不调用torch或新增F/J/root，不更改科学字段。

## 6. 全正式投影和live映射

| 内容 | 原完整数量 | 本组完整数量 |
|---|---:|---:|
| science argv | 157 | 157 |
| pure argv | 7 | 7 |
| science formal selectors | 458 | 575 |
| pure formal selectors | 445 | 564 |
| science live selectors | 64 | 64 |

science增加 $4\times29+1=117$ 项；pure增加 $4\times29+3=119$ 项。四个方向index为0、1、2、3，29项完整对应关系在共享binding的 `/complete_R729_formal_selector_correspondence` 中。ready内每个真实selector也完整展开，没有仅给生成规则而省执行字段。

原903项正式选择器全部保留。新方向未发生、未触发或某诊断尚未产出时，原controller保真实missing/summary error；不补0，不据缺字段宣失败或通过。原正常与数学live分别6项和58项，全部原名称和JSON路径不变，只文件namespace改变。R729的新诊断在正式自然返回里读取，不挤掉现有热点、K、D、alpha或六g live，也不把旧live字段偷换成新算法值。

现有transport仍64项、public16384B、完整文件95000B。单个完整science step紧凑 73571 B，pure step 62744 B；二者合排会超过95000B，完整pure应在science自然返回后原样续排。不能为适应queue把任一步骤、selector或原预算截短。

## 7. 第28组真实证据与严格输入边界

本次已完整取回并核whole bytes/SHA的实际小卷与文字说明：

- topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46108296054-1-part-001.md — 54607 B；SHA-256 cc7459afedbf3343c6f3c0e94cc608379a2ebfbd042408f729adcbfa87e55340；Git blob cf58c9ce632ef210c5351dbfdcc997f49bbe9e8c
- topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46108296054-1-part-002.md — 32987 B；SHA-256 208937df3fc07468949757e57960eca6f3549f9c40ebd0670b623eb3a0db8017；Git blob 68a8ad5d6c64d0ed835f3b1bb74c8694f44b6773
- topics/visible-flex-larger-amplitude/notes/2026-11-28-run28-complete-demanded-halfwave-launch-and-continuation.md — 64689 B；SHA-256 b8450341e87e0e9999dcced5a0ae7c2a87f11f73de46de28598be87e89b5e68f；Git blob 52c2cb55f8c68555834ac10c7395741d6ec2996c

原science自然0，用时 10456.962818394999 s；完整439项formal返回、19项原summary错误。原pure自然0，用时 348.8245757200002 s；423项formal返回、22项原summary错误。完整原错误数组保留在各whole小卷，未“清理”为不存在。

这是真正28自己的source b1a8554a9d88dc176f7295eab4bed9f73f65e3f2、driver d1c99f555e480a0b37fcefee98e1261033bed0b4bb6a7f681f8da345e5ae46ab，不是拿25同数值作代证。原最终point a28ae9998fb54207f0ccccd1a9abdf0e89beff1025f5e01334b856b21d3da3cf；原model 61c6542b3cfe39dea9fbf8c002c8ea204f5dad193ddaffe94bc7c908822682d7。原4个restoration被接受、metric0，最终Phi 681.6450227773521、max relative Gram 0.40616533555531326、有限正g 0.5225620087197518，geometry_passed为false。原停止文字为 `declared_restoration_budget; actual_violation_remains_and_is_not_accepted`。

原第一个方向真实QP为 `dependent_blocker_at_zero_step`，advances=2，face Pg=0.529460169023458，容差=5.305849371949155e-7。其物理行192+11+10=213，增广非负slack行后214。这里只描述原第一个方向，不猜其阻挡行、rank余量、其他方向或新R729行为。原首方向accepted alpha=1也不替未来alpha。

完整原report 51908815 B / 53af35f6e91a6d4021d40fcf7b5a091fa74fd9d49b645b9c5c89c2f2d47cb1fa，完整原pure 8681463 B / 4d543b0c7d2ab5a090d5406a8e48a5e6905956a13e9e9d68a09040b259d66cea 都留原runner。此次没有读取大raw。原final bundle 25d9e9a7868e51d0e96509ee61606fdb068ef58fd63513b1fe294c380b3317fb、typed数量13及hash b0f7d5a2346b27ada6e6619877da8d2c3ad05ab1f6345dfd00405356d3f86ed3 是原whole小卷的真实投影；它们不是33的新输入。

原 `final_mu=0.01` 仍按原字段含义记录，不能假称额外读取了最终restoration阻尼。33的两个初始CLI均严格使用原 `.01`。若以后另做28最终点到新算法source的续跑，必须形成完整字段等价、全部13成员/typed真读、来源转换合同；本独立初输入分支没有放松旧same-source guard，也不等待那项可选工作。

## 8. 全历史与peer责任

原28的5对pending CLI逐词、顺序和source哈希全保。原28 binding中的15个external对象和完整发现史以whole文件加pointer保存；后续已完整登记的28、29、31外部责任通过原32共享历史完整保留，当前metadata列18对。没有把新的a359 driver分配给任何旧run，也没有向原 PARENT_FAMILIES 偷增一项。

旧run失败、取消、自然完成或尚未知的记录各留原文；较新28完整返回作为独立附录，与冻结父对象并存，不把早先null回写成今天已知。未知typed不等于空集合；公开进度、旧错误字段、原report记录均不充当新字段输入。

共享binding下 `/complete_peer_responsibility` 包含全部精确whole记录与完整当前pair列表。参数父是28物理/数值父；32的文件只贡献同R729 formal路径与已记录外部历史，不贡献R728物理源或运行值。

## 9. 完整文字再生与恢复

再生命令为：

```text
node reproduce_fixed_fejer_halfwave_R729_run33_parameters.mjs --source-directory <complete-run28-parameter-directory> --generated-directory <complete-text-output-directory>
```

输入是原28完整science、pure、binding三whole文件。再生器把完整当前共享metadata写出，并从原两step作严格namespace映射、真实脚本/scope替换和明确的新selector追加；每个其他step字段逐值保全。所有当前输出whole byte/SHA/Git blob已固化。它不读取科学raw、root、field或checkpoint，也不启动科学求值。

原文件可由列出的完整Git blob恢复。字符串和历史里的原source哈希不作广域替换；当前新source表单独完整引用。紧凑JSON只是序列化，完整字段值、顺序性argv、所有selector与metadata均保，没有数值输出编码、压缩、分块或数据差分。

本次只完成整源阅读、完整JS文字/JSON构造和whole身份核算；未运行Python、AST、compile、fixture、benchmark或科学函数，未动ref/queue/当前job。未来真实source出版、独立run33开始、完整初值、方向、几何、接受和自然返回必须继续按自己的实际输出登记。
