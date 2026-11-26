# 根 README 第15条：当日可重算输出的普通提交清理

root于2026-11-26 16:01:41 UTC逐项校验全部79个候选的字节数和SHA后，在同一普通提交中从当前分支删除其完整可重算输出，共1,304,555字节。5个参数输入及全部源码/请求/实际数学结论保留；历史没有改写。本记录仅保来源、实际结论及输出身份，不复制完整报告。

只读快照 `2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd`。范围为课题 `notes/2026-11-26-6a65-*`：84 个 JSON，共 1,315,090 B；其中 5 个参数输入保留，79 个输出候选共 1,304,555 B。这些输出原先全部小于100 KB，均已完整解析确认其角色，不能因“小文件”而免除第15条。

以下路径表省略共同前缀 `topics/visible-flexible-closed-surface/notes/`；表内 SHA 均为文件字节 SHA-256。引用快照没有改写历史，普通删文件不会删除该旧提交。

## 活动输入和科学结论保留

- 本清单不包括 `ci-requests`、源码、原始设计参数与证明/结论 Markdown，不能以输出清理名义删这些输入。
- q2 全 H run 45848177096 的小 Markdown、后继 M12 新任务及其 source/requests 不列入删除；其后实际 q2 发布失败另见专门记录，Markdown 结论仍保留。
- 两个旧 Actions Markdown（`2026-11-26-6a65-actions-metric-45767322734-1.md`、`2026-11-26-6a65-actions-strong-45778054176-1.md`）是已支付结论表、退出事实和输出身份，没有完整 JSON 数据块，保留；旧静态 running 文句另按真实结局解释。
- `m12-up-patch-parameters.json` 虽含拟合来源 SHA，内容是复现实验使用的参数，和另外4个配置一起保留。

| 保留参数输入 | B | SHA-256 |
|---|---:|---|
| `2026-11-26-6a65-cauchy-global-fit01-parameters.json` | 1026 | `1108d78c50df41b9c90f21071fbf63e095333267bec8f15100643c79c441f041` |
| `2026-11-26-6a65-m12-up-patch-parameters.json` | 2965 | `1e0659207c6d0e70f709f25e835aa2e76c99048c63168c4e77e5a06e4f1e1ae7` |
| `2026-11-26-6a65-perimeter-full-rho-fit-baseline-config.json` | 1627 | `967157d268e8465778deac672869ed01cdef90a42b0080401804893378218ad9` |
| `2026-11-26-6a65-physical-clock-full-fit-and-value-config.json` | 3378 | `c130403d727bd938093fccc5fecf713f94c8ea7f06763266cf86b2beed51b8b4` |
| `2026-11-26-6a65-transplant-fit02-parameters.json` | 1539 | `dc06654729944f614d9ea2ed8d26f81b86a8e78267fb26bc84dd86a830b27b61` |

## 已结束 run 与相应结论

2026-11-26T15:49:10.147Z 逐个查询真实 GitHub Actions run API，以下12个均 `completed`，故不存在本清单误删尚在运行 CI 所需输出的这一阻碍。job success 不是数学达标。q1 另实际读取终末 `033-area-012`：状态 `explicitly-released-actual-runner-state-topic-still-incomplete`，30次接受/30次尝试；release 包 SHA `0e9ffb3d88d13153b842e19c26ea070350232b28c8f25245ca3d098de9618d6c`，消费 `ebea72d4db652ca0133817298ffe743a0c346412`，终末报告 SHA `1592f0cab5373d15ddd37fd633079c20d4db33f66d4b13fdf0cd7ea88ecd3bfc`。v5 同样已真实 release 并 success。

| 来源组/run | API conclusion / updated UTC | 候选数 | 对应现有实际结论（课题相对路径） |
|---|---|---:|---|
| 45837984058 | success / 2026-11-26T15:34:01Z | 22 | `notes/2026-11-26-6a65-solver-v5-actual-twenty-step-batch.md` |
| 45825253169 | failure / 2026-11-26T13:35:02Z | 3 | `notes/2026-11-26-6a65-solver-cached-first-acceptance-marker-failure.md` |
| 45812620369 | success / 2026-11-26T12:07:17Z | 1 | `notes/2026-11-26-6a65-cartesian-cold-first-actual-acceptance.md` |
| 45838996926 | success / 2026-11-26T15:45:48Z | 34 | `notes/2026-11-26-6a65-gap105-q1-actual-thirty-step-batch.md` |
| 45803041361 | success / 2026-11-26T11:09:10Z | 1 | `本记录下方“旧45803041361实际结论”及原log.md` |
| 45815969723 | success / 2026-11-26T12:29:15Z | 1 | `results/R234-actual-entire-half-field-all-phase-geometry-and-meshes.md` |
| 45821092388 | success / 2026-11-26T13:15:59Z | 1 | `notes/2026-11-26-6a65-m12-actual-first-source-aligned-h-improvement.md` |
| 45826114835 | success / 2026-11-26T13:47:32Z | 1 | `results/R241-actual-h428-continuous-metric-and-all-phase-geometry.md` |
| 45833090043 | success / 2026-11-26T14:37:39Z | 3 | `results/R245-actual-h487-refinement-and-continuous-geometry.md` |
| 45797640490 | success / 2026-11-26T10:07:00Z | 1 | `notes/2026-11-26-6a65-m12-prefix-fixed-g-refinement.md` |
| 45802097600 | success / 2026-11-26T10:39:50Z | 1 | `notes/2026-11-26-6a65-m12-prefix-fixed-g-refinement.md` |
| 45804794238 | success / 2026-11-26T11:15:13Z | 1 | `notes/2026-11-26-6a65-m12-prefix-radial-refinement-after-6400.md` |

### 旧45803041361实际结论（保存既有结果，不重做计算）

该run的真实source为93721721e33a06c0389498912aecc183f8f4a949。原固定g全半体直到真cuff、半径.6内部口自由，362元/35378列，M32/N384/G6、800 LSMR/1Newton；prepare、原tail查询和solve各自然0，总1882.249134163秒，完整solve1712.492012619秒。一次alpha=1接受，LSMR800/stop7；独立采样metric从8.75957151258433e−9到8.494503545009024e−9，训练末峰1.9112439630930567e−8，独立曲率6.4168726979752995。中央和真cuff修正两jets为0。该run本身没有连续metric或全族reach证书，不能借后续R234/R241的证明。

实际field SHA d703d0065ab0617ee9c28a5cb37129f8c39005fb4b9cc73b7c2b6f04eb91af8e，result SHA ab74ce968c101040fd9b0ed032289de395ec8ac9bf188690696fb68005071e54，grid SHA6abeb5cecef86c8385186324da9dec67a5dadb7b50c4cac05c2cfcbbf8cea3b9，完整执行报告SHA19e86b4d6d7dc8112934c1c5f85b7d44924b5cc6dd19ed97aaf02173ea27ebf7。原log记录和下面冻结source/request足以定位复生；本段只是保存已有真结果。

## 来源提交、入口与请求的可复生身份

复生按下面的实际 source 提交读取当时 workflow 和 request，再执行同一数值入口；输出始终写到 Git 外。这里不执行 `rerun`，也不建议再次触发历史写 JSON 的旧 publisher。若重新计算，可在独立执行器只运行当时 workflow 的数学子命令，沿用原请求参数，结果用新的小 Markdown 结论记录。所有旧 raw 都不能冒作当前活动 runner 的原件。

### 45837984058

- source：`0a26d8e0e3c017df4c0175d542fedf134663136d`；workflow：`.github/workflows/6a65-cartesian-channel-block-v5.yml`。
- 记录的入口 SHA-256：`3894552b05482c6a70faea1c50d0ae6e6451a72b3d5a04f3728155df51aeba1e`。
- request：`ci-requests/6a65-cartesian-channel-block-v5.json`；SHA-256 `59e024de320132e79fee3741fad9d6d9662253ca974e20ab34a8cc68a979b69b`。
- 来源结论：`notes/2026-11-26-6a65-solver-v5-actual-twenty-step-batch.md`。

### 45825253169

- source：`64f20c32b37f50d94bb54fc0a7b6a0bc1ea50eff`；workflow：`.github/workflows/6a65-cartesian-cached-continuation.yml`。
- 记录的入口 SHA-256：`33a392a0738e74608b18de2bb05be14e9c01e1c2db7e3ecdfc926cb7b585a21d`。
- request：`ci-requests/6a65-cartesian-cached-continuation.json`；SHA-256 `514002b09ff7aa91a9e0d0ec82ed7292cc82dac17cc931f0a586fd560202dcc2`。
- 来源结论：`notes/2026-11-26-6a65-solver-cached-first-acceptance-marker-failure.md`。

### 45812620369

- source：`964fc70641136798ac3caa09db831e2f5347f47c`；workflow：`.github/workflows/6a65-cartesian-independent-cold.yml`。
- 主入口 SHA 未单列于此报告；由上述冻结 workflow/source 读取，不能补造。
- request：`ci-requests/6a65-cartesian-independent-cold.json`；SHA-256 `1366860591bceb210aa56eda63951105fc1c57bfa25926bc2d701216cba20540`。
- 来源结论：`notes/2026-11-26-6a65-cartesian-cold-first-actual-acceptance.md`。

### 45838996926

- source：`1dd2ae1757346004be6a7641e492a562648baccc`；workflow：`.github/workflows/6a65-gap105-whole-branch-cold.yml`。
- 主入口 SHA 未单列于此报告；由上述冻结 workflow/source 读取，不能补造。
- request：`ci-requests/6a65-gap105-whole-branch-cold-20261126.json`；SHA-256 `6630723f4f8723f5c9630f0f67fc1a4c967efa814c4a1adbc16bf17d36844ebf`。
- 来源结论：`notes/2026-11-26-6a65-gap105-q1-actual-thirty-step-batch.md`。

### 45803041361

- source：`93721721e33a06c0389498912aecc183f8f4a949`；workflow：`.github/workflows/6a65-m12-entire-half-fixed-g.yml`。
- 记录的入口 SHA-256：`d5f0c967bbec9cd45382afdde8418d974635af734d6fa4aa98aab1d0a0d41f3d`。
- request：`ci-requests/6a65-m12-entire-half-fixed-g.json`；SHA-256 `60e9b0c9b9ac4fab27d12a90d9d17d096069ddf571f053726919ab3ca1ca3e82`。
- 来源结论：`本记录下方“旧45803041361实际结论”及原log.md`。

### 45815969723

- source：`3a751a836c60a4f33efa9e0ddd3060a188621adc`；workflow：`.github/workflows/6a65-m12-entire-half-fixed-g.yml`。
- 记录的入口 SHA-256：`6c92f75e752d5c581b7642a576905c3c6fa436a174a8f4ff711e38d862a98136`。
- request：`ci-requests/6a65-m12-entire-half-fixed-g.json`；SHA-256 `7b75e569f994d7dad25bc99b06c6a1f76e00e0bc3ae47fca51d227c64bde16a8`。
- 来源结论：`results/R234-actual-entire-half-field-all-phase-geometry-and-meshes.md`。

### 45821092388

- source：`cd31d2b00bcf8470c3856c8ac22e88e89b83ab8d`；workflow：`.github/workflows/6a65-m12-entire-half-fixed-g.yml`。
- 记录的入口 SHA-256：`44e3f2082c6f5bbcef9cc88f3450ffb10c4146abfc7eaa42f51105ff50a58648`。
- request：`ci-requests/6a65-m12-entire-half-fixed-g.json`；SHA-256 `8c658670ec93b6e41839b4b220b26eda9ef1ae3bbbdb039e7c315cd0c6a5209d`。
- 来源结论：`notes/2026-11-26-6a65-m12-actual-first-source-aligned-h-improvement.md`。

### 45826114835

- source：`f878ec7a2766c1d2a00f06c8d05893828986f7a5`；workflow：`.github/workflows/6a65-m12-entire-half-fixed-g.yml`。
- 记录的入口 SHA-256：`44e3f2082c6f5bbcef9cc88f3450ffb10c4146abfc7eaa42f51105ff50a58648`。
- request：`ci-requests/6a65-m12-entire-half-fixed-g.json`；SHA-256 `8853909858c52870632958a2cb0be4746e5f7cd1b0290487f74eafd2d17c5481`。
- 来源结论：`results/R241-actual-h428-continuous-metric-and-all-phase-geometry.md`。

### 45833090043

- source：`a060a8d1cb7bf95d6b8d5087467cf63377e3867e`；workflow：`.github/workflows/6a65-m12-entire-half-fixed-g.yml`。
- 记录的入口 SHA-256：`3475fbded48a20474e143091dfde0c4077212c1372c76f52693d472c1c9bdfbc`。
- request：`ci-requests/6a65-m12-entire-half-fixed-g.json`；SHA-256 `86a0683fe8e20d4ae39fa81459cdfbbef125570ae68146a18d139bc36a27fda9`。
- 来源结论：`results/R245-actual-h487-refinement-and-continuous-geometry.md`。

### 45797640490

- source：`8b5358e307ebe3439a47b6861a1647848bf2ecf7`；workflow：`.github/workflows/6a65-m12-fixed-g-joint-prefix.yml`。
- 记录的入口 SHA-256：`ddca0e263e7ff8e28b959b18da2439de6245d05914b6612efe9840bd661c7edd`。
- request：`ci-requests/6a65-m12-fixed-g-joint-prefix.json`；SHA-256 `622dc339980476c5ba0f9b83da2fbb72e9c535b804143c143931053920dd006b`。
- 来源结论：`notes/2026-11-26-6a65-m12-prefix-fixed-g-refinement.md`。

### 45802097600

- source：`9c5f7ee324397ea545fdff7d6030db7be0ad627a`；workflow：`.github/workflows/6a65-m12-fixed-g-joint-prefix.yml`。
- 记录的入口 SHA-256：`ddca0e263e7ff8e28b959b18da2439de6245d05914b6612efe9840bd661c7edd`。
- request：`ci-requests/6a65-m12-fixed-g-joint-prefix.json`；SHA-256 `dbd021e304a47ea4b5c6c9d640b37dd7cd2cc69a35c4a9f42320bb7c8538c88f`。
- 来源结论：`notes/2026-11-26-6a65-m12-prefix-fixed-g-refinement.md`。

### 45804794238

- source：`f7d3ebbba996804026f63889bc231fe0311b1272`；workflow：`.github/workflows/6a65-m12-fixed-g-joint-prefix.yml`。
- 记录的入口 SHA-256：`89d3f03e752dce04007166a8e540e3e49f1621ed725cd8e6b43475ea8101776a`。
- request：`ci-requests/6a65-m12-fixed-g-joint-prefix.json`；SHA-256 `666c3512a63ae31f50aad9fb80fbbd47f9d865bf54c238aadebc33d958ad978d`。
- 来源结论：`notes/2026-11-26-6a65-m12-prefix-radial-refinement-after-6400.md`。

## 本地报告/fixture 对应

| 组 | 输出角色 | 现有结论 |
|---|---|---|
| L1 | 实际旧 baseline 数值的派生抄录，不是新的设计输入；对应原 baseline SHA 在该记录与 R222 中 | `results/R222-central-gap-conditional-held-and-ramp-budget.md / notes/2026-11-26-6a65-geometry-central-gap-held-budget.md` |
| L2 | 本地可重算诊断/fixture；无新 Actions run；记录的入口 SHA `18daedc0da9897602d5a3c07deb055d2855aa1049590d69e9e74509f67787f35` | `results/R236-local-bernstein-angular-continuous-metric-budget.md / notes/2026-11-26-6a65-local-bernstein-angular-metric-budget.md` |
| L3 | 本地可重算诊断/fixture；无新 Actions run | `notes/2026-11-26-6a65-m12-element190-source-aligned-h-preparation.md` |
| L4 | 本地可重算诊断/fixture；无新 Actions run；记录的入口 SHA `a7577dc4e7b644d606dabc22f04bcf5eb75bb74c47a6d682ade349718341eae0` | `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` |
| L5 | 本地可重算诊断/fixture；无新 Actions run | `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` |
| L6 | 本地可重算诊断/fixture；无新 Actions run；记录的入口 SHA `c74e35dbe4afcd768b4788a7d33d817395873b0e635ad5a0475e36b47363249b` | `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` |
| L7 | 本地可重算诊断/fixture；无新 Actions run | `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` |
| L8 | 本地可重算诊断/fixture；无新 Actions run | `notes/2026-11-26-6a65-m12-whole-continuous-geometry-and-stl-entry.md` |
| L9 | 本地可重算诊断/fixture；无新 Actions run；记录的入口 SHA `63506a11d80e1d14e7e4b7dc7a5419b90fc198948772f76f2a6d9aa7ccd88e51` | `results/R235-reflected-third-jet-compatibility-and-exact-local-patch.md` |

## 79 个已移出当前分支的输出身份

| 文件路径（上述 notes 前缀） | B | SHA-256 | 来源组 |
|---|---:|---|---|
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-001.json` | 22283 | `bdc20a537f792ced878253310e8a1f21b0ac4ae9b5fbeea5652800b27157c639` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-002.json` | 21906 | `fe0714b3dc182db9890f21c8920784450dc94fb6de00094e7ac9be9c645cba24` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-003.json` | 21988 | `1e2c0c1d29686ece768a781b4d534faef3351f01bdb6bac7b78f1c5654906850` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-004.json` | 21694 | `b21d7f113616b5a8f6efe80e237a75f4c42e4a8b8be758d64567ee0afda053aa` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-005.json` | 21684 | `79e671c2c640800ddc3a5a16aa7e9b1e48f075d055d66f2a3c85521cc35ab88b` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-006.json` | 22083 | `cbc5531ebfd9179433cc5cefb7e243a2478191e6d4ac3053a9f1a5d515596b5a` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-007.json` | 21705 | `126e566d8d836761b24c086ca24ae1921e46f6c08814e426a51441199ebbcb5f` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-008.json` | 22082 | `3976e114250a79adb72e7dad123eb5c5e24dc853cd2e546215000d6ba983b1da` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-009.json` | 21668 | `7726b4af08f342586dddb24c0ddd5b53602ff826921b0a88a879859e7a2c9d52` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-010.json` | 22427 | `db70cd89acc1c73125100b5b9787407140d247a4d7b9dc5949d78b7528294b08` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-011.json` | 21910 | `4802672fbb8a1101b570b97ae958b831fe59d05f655467fac84d1f59a7811237` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-012.json` | 22034 | `ac6b106cc67900edbebd2937350009fd814659b882c6028a51f9236dd98bd354` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-013.json` | 21653 | `07a7a34f350d4abb69f796a3266ddfd6cf0767946cbb367cd2cee109581b800c` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-014.json` | 22031 | `5839ed995545b1de30a65cddfabe141fb31672a488e3724da8d817c102b4cfc0` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-015.json` | 22022 | `a0f870fea100d00c988cfe4d4aaaf1f678dbd7a949729e517fab4f4cf31d40a1` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-016.json` | 22798 | `25202ccdb7d7ade4b19db1bac5d61ae87d817a082169ff064b116deba5d1e8bf` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-017.json` | 21658 | `62e711924988ae0df8ef7bed451ce4f294aa95f4f7c199c08726831f16b71f31` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-018.json` | 22798 | `9239b03266661ac191048d318098affe55a70aa31e96d8a294992a466cb39ed9` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-019.json` | 22428 | `669236c9da1df3a50ff864086e52f1a28da0ce25b2bcbd85ed4d0a38c9ac0562` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-attempt-020.json` | 22837 | `136b5efd494e91655da662b81b0a4db9b9bb859772e27756ef5bd1d209f8fe12` | 45837984058 |
| `2026-11-26-6a65-Cartesian-block-continuation-45837984058-1-start.json` | 2016 | `db43441c10cda9b35866431813193eec43e275f97b8bbf36943b587e30d1ef72` | 45837984058 |
| `2026-11-26-6a65-Cartesian-continuation-45825253169-1-attempt-001.json` | 2260 | `023c4a2cc7426ac7348fbba53c0b449599b8f2c311f5ed08fa753d8157d8c264` | 45825253169 |
| `2026-11-26-6a65-Cartesian-continuation-45825253169-1-start.json` | 2013 | `864c048b5f2c190ea76b72aee83a31ae6955efabb6db4162ac353fbc0bb70197` | 45825253169 |
| `2026-11-26-6a65-cartesian-block-bootstrap-45837984058-1.json` | 32945 | `038a8bbcae95e6fcdbf10091cce6a963d60f8539569a7a442d6305a7816da709` | 45837984058 |
| `2026-11-26-6a65-cartesian-cold-45812620369-1.json` | 57030 | `a4d288b38f629ccc114615133cc6c4e9b50c7ceed305ad5085ac94d73a5902da` | 45812620369 |
| `2026-11-26-6a65-cartesian-cold-45825253169-1.json` | 32049 | `89793e51c8d90b925081b0543cabeb8746e941e25beae63bfd078274ac6bdcda` | 45825253169 |
| `2026-11-26-6a65-central-gap-recorded-observations.json` | 1086 | `b3dc47bb68288cd2dde48449b0e042169aac44e916f6264c2bb9144bebfa7ca1` | L1 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-001-prefix.json` | 5254 | `eed091ba22ec4207954d42ed382ea6aa00e792f9fdae7785a8f070720e548b79` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-002-own-zero.json` | 7133 | `700651e94f11d83d70f5ba3712646eda3a96555ee351437deb02ee25d71ded7e` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-003-prepare.json` | 6210 | `7e405e638fe3a99829f58e837c1827a47662cdb34f9a10091f57ee514c108f76` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-004-single-001.json` | 8390 | `82ff1ded4e0e39542476a29f37ed452e2481e8d030bde566ec4d238d508d85a2` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-005-single-002.json` | 8389 | `9d048227c2e603ad4689094605ed4050ee01353eb1a0f019b86c64ede79cbcc3` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-006-single-003.json` | 8386 | `54ffafc484f8fc90f296266ddebc8cbe7d0e2f491296d9884f33c73462137b08` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-007-single-004.json` | 8384 | `d06a57cc796bdbf44c1b112037e114174becd3b0dc893f49b30d4165f565d3a8` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-008-single-005.json` | 8386 | `f723bcca59513ba6133c800117c0a77b7db629c32d4ec972e46bed58f356e276` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-009-single-006.json` | 8387 | `f6604c9c3ab60efa53d1232fb84d5065367a0faacba8d5e051a1003783850b93` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-010-joint-001.json` | 9524 | `27697db4dff8dd340d78fe02c95767b7014b0dd894f7cd7c6f622d4387361679` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-011-joint-002.json` | 9469 | `06e0fc7528b0d7c4c1110502a31607eb12aeae8e46b4cf492509366d1bfa98f4` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-012-joint-003.json` | 9447 | `a47b0df8e3ac52902c505c3c3230f3c923e1810c86b99d86b055d93719253a03` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-013-joint-004.json` | 9443 | `70f01f4fe8ec6982ac8796878b65c9e297f551e5b83ea20e632827ee2db299a0` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-014-joint-005.json` | 9690 | `6c776d251ac17b570e0e81a67725992d6b8b6dff1e0a19239666ad5dc9b0863a` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-015-joint-006.json` | 9450 | `d7d41af7bf9f06d5b893b925b220c1be294dc0af7099fbdbc4dfd25b20252b12` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-016-joint-007.json` | 9450 | `b00d0f7297169fc8b38fd62c4269cf257dbe658d69b96d6eab27ed743faaeccc` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-017-joint-008.json` | 9453 | `20993fb955a2f690950a34b46a9f596916a3880bd90ce8a0efd7046af5f65f1a` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-018-joint-009.json` | 9444 | `1b1a4008a2fcf6729fdaf27e224b9dcfca404ab2dc9ec36cab8a21773a37be3c` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-019-refined-001.json` | 9524 | `b6e180e66c4a4157f1189ac6485d40e5818c9451c206d274145978b88115cd42` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-020-refined-002.json` | 9521 | `5014e5abc4fe3c0d85dca43023af6bfdbbc1086582e628c71c7e3b952de1160b` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-021-refined-003.json` | 9528 | `e019ce0b7a9baf3c1037289deb7e51f3c03bfd2f526ee5be2cfe35b815d516e9` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-022-area-001.json` | 14372 | `715cd0e67ca7b12145469a888a4967373d16d885bb7eeeb4407c44da9c99320b` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-023-area-002.json` | 14367 | `0ae2038002c236dc222327869de19e6adfd2efc20efb64ce8a07f2cda1311e41` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-024-area-003.json` | 14382 | `0824ff6a4b3c14a02285ae72b047a1a13b092d287e7b7da3a49fe9cbe927248c` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-025-area-004.json` | 14378 | `1948045e41a7418b1d5080a29856979058ff776a2bafd2314323ffab0a873aaf` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-026-area-005.json` | 14365 | `90942f4f327f96599b26d2e7681cadece2e2b1cbd4a11a4d9f06edc140960ea5` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-027-area-006.json` | 14370 | `0afc37e200704233a16794c55175fbe28f8df0ba0313f01c7d2a324755edd8a3` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-028-area-007.json` | 14367 | `7cea39ffc86395844f8606a232c5b7f12a2311316fdbf9db4276a1a6facf5d90` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-029-area-008.json` | 14372 | `f6c54493820fd316f40d0a93b340d110e518a5dac5d733391b752d89e074269e` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-030-area-009.json` | 14604 | `bcce1b32396713d6516d488c567a02271a3bcaeec3f1a2e03ab3ba603812a6a6` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-031-area-010.json` | 14369 | `68ae4fa5f144d4a600d85a5e576d482001a3498117fbe19de6881b397e978feb` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-032-area-011.json` | 14374 | `19664c4532d01c46160411c1fe05dcf9df7f74cb335d3cdaba497f491d82da56` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-033-area-012.json` | 16083 | `1592f0cab5373d15ddd37fd633079c20d4db33f66d4b13fdf0cd7ea88ecd3bfc` | 45838996926 |
| `2026-11-26-6a65-gap105-cold-45838996926-1-start.json` | 4069 | `5ed99b7a60b87c792ec121ff9202eae33432f66f4529fb463d92b3e864d979b0` | 45838996926 |
| `2026-11-26-6a65-localized-metric-checker-validation.json` | 1782 | `b932c94e1c9869025f78777fe582a4a43880a53a04b2fef31cf0dbe065a68d2b` | L2 |
| `2026-11-26-6a65-m12-element190-h-preparation-receipt.json` | 2746 | `a542199eff0f7d25baed0f6e255ccfdf8b5125f526d547209f7792030a912f44` | L3 |
| `2026-11-26-6a65-m12-entire-half-ci-45803041361-1.json` | 11608 | `5ffa39c5aac0ff858dae58d72ee5c26f033f45d12614a400d49cd6b57257a9d4` | 45803041361 |
| `2026-11-26-6a65-m12-entire-half-ci-45815969723-1.json` | 63301 | `5839f93cf870b13ebe2ee1138ac4882a3ba717b2e9e859fab8947ec1efa0da93` | 45815969723 |
| `2026-11-26-6a65-m12-entire-half-ci-45821092388-1.json` | 70453 | `d4acda90de06f0da69eb499cc12237a30bfd52cb355bcb78a0e213df77ae2fcb` | 45821092388 |
| `2026-11-26-6a65-m12-entire-half-ci-45826114835-1.json` | 87010 | `6e3070d97ad3b6414492f64340a84557c321823c3d4a083e20f4566332886829` | 45826114835 |
| `2026-11-26-6a65-m12-entire-half-ci-45833090043-1-continuous.json` | 51437 | `79c96c0dcba370288bc1dddf00759d6054f46c2e344fa1c4cb2d6788385a5076` | 45833090043 |
| `2026-11-26-6a65-m12-entire-half-ci-45833090043-1-localized-metric.json` | 15822 | `0a964fa588cc9e765745d2b8ce7a15cbb070446b2e6a1a5e00806697555770be` | 45833090043 |
| `2026-11-26-6a65-m12-entire-half-ci-45833090043-1.json` | 32200 | `0ccc326aee24f64348f181c509ff3ff102ef4a4a95523fb4b87cb9be9b6dbc2b` | 45833090043 |
| `2026-11-26-6a65-m12-global-prefix-ci-45797640490-1.json` | 5734 | `d41806381919604596ece336eefc6fa406ceb89c02c9f0ab53b11d265ff82e4c` | 45797640490 |
| `2026-11-26-6a65-m12-global-prefix-ci-45802097600-1.json` | 5827 | `1bffc2053838d33ab57bebba30a65fccff40a91a5778b8dc24e2b5df3ebdc56d` | 45802097600 |
| `2026-11-26-6a65-m12-global-prefix-ci-45804794238-1.json` | 6120 | `e0cc184798f625edc8ae65cf7b974495005a4a42a62a6f1fb54123bcd16c4dcf` | 45804794238 |
| `2026-11-26-6a65-m12-live-rules-supervisor-check.json` | 796 | `b4a5478ac8def5f77ef358fcc3f1a6c87dd2b7dd1d0a1c84d8662a2e4c700e97` | L4 |
| `2026-11-26-6a65-m12-two-hotspot-frozen-source-receipt.json` | 2008 | `533882d41353e7d06ba3ab214e67a757f51bd80a19fff49f80500897a5fa394e` | L5 |
| `2026-11-26-6a65-m12-two-hotspot-prepare-check.json` | 2143 | `afe704f865916389f55d9c5639b342a5149b832e8124fa69759092e6dc489603` | L6 |
| `2026-11-26-6a65-m12-two-hotspot-scalar-format-budget.json` | 1121 | `81d6346b98a7739a0cc091663c8afa33f104c31a8121b81a99e7d4544df0914f` | L7 |
| `2026-11-26-6a65-m12-whole-source-cx-receipt.json` | 4821 | `7bae12c1def36552c4cd9543d37f726780453f4e6ad41654e6ce8b65f598b84d` | L8 |
| `2026-11-26-6a65-original-third-jet-jump-and-local-patch.json` | 7204 | `e669fe6c5cfe019becf37f51509b58686e5985a5da373b736b4c51ee17ba0748` | L9 |

## 相对 Markdown 链接的具体替换

扫描课题中每个不超过100 KB的 Markdown，实际找到下列15处指向候选文件的相对链接，涉及10个文档；未发现源码/JSON配置中的候选完整文件名依赖；这不冒称已经排除所有可能动态拼接路径。本次普通删除把每个目标改成下列固定历史提交 URL，保持文档已有数学陈述与真实边界不动。表外完整路径的纯文本提及也可加上“历史快照”说明；不重写实际结论。

| 文档（课题相对路径） | 旧相对目标 | 新目标 |
|---|---|---|
| `notes/2026-11-26-6a65-cartesian-cold-first-actual-acceptance.md` | `2026-11-26-6a65-cartesian-cold-45812620369-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-cartesian-cold-45812620369-1.json |
| `notes/2026-11-26-6a65-m12-actual-first-source-aligned-h-improvement.md` | `2026-11-26-6a65-m12-entire-half-ci-45821092388-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-entire-half-ci-45821092388-1.json |
| `notes/2026-11-26-6a65-m12-entire-half-cold-entry.md` | `2026-11-26-6a65-m12-global-prefix-ci-45797640490-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-global-prefix-ci-45797640490-1.json |
| `notes/2026-11-26-6a65-m12-prefix-fixed-g-refinement.md` | `2026-11-26-6a65-m12-global-prefix-ci-45797640490-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-global-prefix-ci-45797640490-1.json |
| `notes/2026-11-26-6a65-m12-prefix-fixed-g-refinement.md` | `2026-11-26-6a65-m12-global-prefix-ci-45802097600-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-global-prefix-ci-45802097600-1.json |
| `notes/2026-11-26-6a65-m12-prefix-radial-refinement-after-6400.md` | `2026-11-26-6a65-m12-global-prefix-ci-45804794238-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-global-prefix-ci-45804794238-1.json |
| `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` | `2026-11-26-6a65-m12-entire-half-ci-45821092388-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-entire-half-ci-45821092388-1.json |
| `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` | `2026-11-26-6a65-m12-two-hotspot-prepare-check.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-two-hotspot-prepare-check.json |
| `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` | `2026-11-26-6a65-m12-two-hotspot-frozen-source-receipt.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-two-hotspot-frozen-source-receipt.json |
| `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` | `2026-11-26-6a65-m12-live-rules-supervisor-check.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-live-rules-supervisor-check.json |
| `notes/2026-11-26-6a65-m12-two-hotspot-source-aligned-h.md` | `2026-11-26-6a65-m12-two-hotspot-scalar-format-budget.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-two-hotspot-scalar-format-budget.json |
| `results/R222-central-gap-conditional-held-and-ramp-budget.md` | `../notes/2026-11-26-6a65-central-gap-recorded-observations.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-central-gap-recorded-observations.json |
| `results/R234-actual-entire-half-field-all-phase-geometry-and-meshes.md` | `../notes/2026-11-26-6a65-m12-entire-half-ci-45815969723-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-entire-half-ci-45815969723-1.json |
| `results/R235-reflected-third-jet-compatibility-and-exact-local-patch.md` | `../notes/2026-11-26-6a65-original-third-jet-jump-and-local-patch.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-original-third-jet-jump-and-local-patch.json |
| `results/R241-actual-h428-continuous-metric-and-all-phase-geometry.md` | `../notes/2026-11-26-6a65-m12-entire-half-ci-45826114835-1.json` | https://github.com/Rogerhu12/math-research-public/blob/2dc56cacb8bc67fd2670fb2962d1503e2b5d7dbd/topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-entire-half-ci-45826114835-1.json |

本次root已重新读取并校验79项字节/哈希全部一致；逐个历史路径存在。现有15处相对链接已改为上述实际历史提交地址。源码、请求和所见workflow中未找到这些完整文件名的输入依赖；没有声称排除任意动态拼接。这里只清理可重算输出，不改变实际数学结论或课题状态。
