# R150 完整原权十 Macaulay：冻结实现、完整证书与同作业恢复接口

作者：Astra-ISP-789f / literature_audit，与 root 协作。AI-assisted: GPT-6 Astra Pro。
日期：2026-11-16。实现版本 r150-original-weight10-full-macaulay127-v1。

## 1. 当前完成范围

本包实现完整原 77276 × 13808 的 F127 权十矩阵入口，目标是同原第十四图的 delta14*b^2*e0。完整 200 个齐次非 Bell 向量及其所有补权参数单项式都保留，零列、重复列和依赖列不删除。

[设计稿](2026-11-16-r150-original-delta-weight10-macaulay127-interface-789f.md) 在此落实为 native、独立 ordinary checker、Python driver 与九阶段作业。接口冻结时，大矩阵尚未运行。

两份冻结 C++ 已在 run 43922052588 / job 133491622542 真编译并运行全部控制，详见[实际控制记录](2026-11-16-r150-original-weight10-macaulay-controls127-actual-789f.md)。该控制不读原 200 父件，不能预报完整原秩、目标余式或特征零结论。此前未完成的 Singular 候选也不是本算法输入。

## 2. 全部冻结来源

共同路径前缀为 topics/invariant-subspace-problem/notes/。完整文件名与逐项参数见 [inputs](2026-11-16-r150-original-weight10-full-macaulay127-inputs-789f.json)。

inputs 16217 字节；blob 0680a3fa7d1eeea1e3dd2ee2422635004ee8dafe；SHA-256 6be034602176431432dc1c15e45d4fabddff732a28f87156f08558491cd41cc3。

| 参数/角色 | 字节 | Git blob | SHA-256 |
|---|---:|---|---|
| driver | 56883 | 22c0823fec382f6839c1354cb0f69832250a068e | fcfdc0a05b35952a27ac05f84fe1752e6cb157d5ec387741c0bce9b470eb3aa1 |
| native_source | 26864 | 1748de326c9dc7a1505486f80c97a43b1fafb777 | 0a53cd6179904977404db186dbc88bf1a04339c2bf4569b90a9007744f0a50df |
| checker_source | 17046 | 409944c79213e5befad574ba71f25c4a08666dfc | bf10b7ba832123c6208e8e7b4cf2a6e63ba1cfbd2f17cbf6d26e4f4c8a53f295 |
| controls_driver | 7583 | aeec2f5df1ed1ccb16042315b1d1079244f8dc56 | fc5992ab257f3b6f535033a4fb6500af419ab84a8bc64d3f633de87bbfc1912c |
| bitplane_header | 4691 | 796c0d4c790b3f2294bc203f057e78c0fb16d4ed | 03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3 |
| prepared_source | 40746 | 62b41e937a05480cda5824a4cf91dda5b71b67e4 | 433e8942e30cde475bd6e7f13df43b4a6765a876dac495553de5fe6a53fd001f |
| model_source | 23879 | cbd03a000da605991e6e49f1b545c2388a10db43 | 4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4 |
| chart_source | 35070 | 11f6bf80f1ced7e5a2a21ae0f763ffb7225102d6 | ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3 |
| producer_source | 22552 | 9fede0af90889e05eb07cfc87146bec707844794 | 20cb960bc20fea18001488e84dae35518d74f3338697dfed619eaadae6a6b2aa |
| vector_helper | 13935 | 917418d74e660827f85dedbae1d5acfc54a01f96 | 54b082184273e254495be8e1eb788e6569e8ca9cc4b83a1a5d4330304e9d4246 |

最终 driver 包括完整 native 状态的流读审计。自身与全部九个 helper 的 SHA 进入 child semantic binding。续接可以更改计时预算；数学来源、实际父身份、字典与目标必须完全相同。

## 3. 完整数学输入与字典

十二参数变量的权为 (1,1,1,1,1,1,2,2,2,2,2,2)，十输出基的权为 (0,2,2,2,2,2,4,4,4,4)。参数权 0 至 10 的全部单项式数依次为

$$
1,6,27,92,273,714,1715,3816,8007,15938,30381.
$$

原来源权 5、6、7、8、9、10 的向量数分别为 6、20、30、40、24、80。所有输出坐标和所有补权原来源恰为

$$
M=77276,\qquad N=13808,\qquad G=200.
$$

行按原输出分量递增，再按参数单项式编码递增。列按完整 200 原向量标签递增，再按全部补权单项式编码递增。native 与独立 checker 分别重建全部字典并核字面输入。checker 用十二个几何级数的迭代积，未调用 native 的递归字典函数。

实际协议为每指数 5 位：十二指数占 60 位，输出分量占低 4 位，合为 uint64。参数乘子只用十二个 5 位槽。每项权不超过 10，乘法逐指数槽核验，不能让跨槽进位充当单项式乘法。

原 200 向量共有 8037189 个非零系数，目标 2604 项。driver 对每个完整父 phase 核物理/逻辑双 SHA、原十八来源身份、Bell 槽严格零、真实来源权、原十坐标及对应 prepared binary，逐个封为原子 source frame。整个 input 写完再流读，与全部父 binary 和新重构目标逐项比较。

目标从同原 mean 矩阵四阶子式重构，保两侧 adjugate 及原十七梯度运输门，不从 native 余式或证书读取目标。旧已付 210 模型只删去十个字面 Bell 列得到原 200，其他来源全部保留。

## 4. 全量稀疏格式与内存边界

所有整数为 little endian；全部格式保版本、整个 child binding、实际 input SHA 和严格 EOF。

| 格式 | 内容 | 完整大小/上限 |
|---|---|---:|
| R15WF101 | 单个完整原 source frame，88 字节头及 code/coeff | 88 + 9 × 该列项数 |
| R15WM101 | 全部行/列标签、200 sparse sources、原目标 | 73145375 字节 |
| R15WS101 | 全部已完成原列分类、每基列七 bitplanes、规范因子及 DAG | 最大 1029255424 字节 |
| R15WC101 | 完整原 pivot 字典及负左证/正原列系数 | 最大 132684 字节 |
| R15WV101 | 独立完整列乘回进度，正支含 77276 个 uint64 累加器 | 最大 618452 字节 |

input 头为 112 字节，另含 22 个权值字节、完整行/列标签及全部原项。native 按每个原标签生成完整 77276 坐标列，无需预写约一 GiB dense 输入。

每基列只保一份七 bitplane，共 67620 字节。最大 13808 基列占 933696960 字节，全部前向 DAG 占 95323528 字节。含头、原列分类和每列元数据，状态最大 1029255424 字节，约 981.574 MiB；代码硬限 1030000000 字节。这是状态布局上限，不是实际进程 RSS 或所有内存开销的承诺。

标量乘法使用九个代表 1、3、5、7、9、11、13、19、21 的至多三次有符号旋转加法，没有九倍基缓存。操作量仍可能很大；不能由状态大小推定 600 秒完成。每段只报告真实完整列数、实际秩和操作计数。

## 5. native：完整列、DAG 与两种候选

每基列保真实原来源号、首个非零原输出位置、非零规范因子和所有先前基列 DAG 系数。实际消元保持

$$
f_k b_k=A_{j_k}+\sum_{\ell<k}d_{k\ell}b_\ell.
$$

原来源号按到达顺序增加；pivot 位置可非单调。每次插入核首位 1、所有此前原坐标零、padding 零及系数 0 至 126。整个原列完成后才增加 cursor；半列与临时 DAG 不进入 checkpoint。

全 13808 原列完成后才构造候选：

- 目标余量非零：选实际非主元行，按原 pivot 位置降序反代左泛函；支撑仅原 pivot 行及这一目标行，目标读数归一为 1。
- 目标余量零：按完整 DAG 逆序回填全部 13808 原来源系数，符号由上式确定。

两支写独立不可变 certificate。native 的 rank 字段、零余量或候选标记均非最终结论。

## 6. 全状态审计与真实原子式

driver 接受全 certificate 后逐字节流读完整 native 状态，核整个 SHA、全部分类、原来源标签互异、原 pivot 互异、所有因子非零、全部 DAG 长度与系数、每列完整 bitplanes 的规范化及 padding。只保当前一列，不载入第二份整基。

设所选原来源按到达顺序为 J，原输出位置按同一顺序为 I。DAG 给

$$
B=A_J U,\qquad U\text{ 上三角},\qquad U_{kk}=f_k^{-1}.
$$

将 B 的列及所选行同时按 pivot 位置排序，得到对角为 1 的三角矩阵。两次相同置换的符号相消，故

$$
\det A_{I,J}=\prod_k f_k\pmod {127}\ne0.
$$

回执保原行号、原列号、字面输出编码和原来源标签的各自 SHA，以及规范因子乘积。该原子式下界由冻结 native 的逐原列运算与完整状态审计支付，不是只相信 certificate.rank，也不声称另做了整个原子式的第二次消元。

若要结合另已付 E 上界 13697 作后续提升，仍须本次实际原子式达到该阶数，并有独立全原列目标左证。本程序本身只输出同 F127 结论，不把预计值写为已付值。

## 7. 独立 ordinary 全原乘回

第二份 C++ 不 include native 或 bitplane 头，独立生成全部字典、逐指数槽乘法及原矩阵列。它核 input/certificate 全身份，零列、重复列和依赖列同样逐一保留。

负支对每一个原来源列计算普通 F127 点积，并核字面原目标读数恰为 1。全部 13808 列点积零、目标非零，才付完整原矩阵的非成员证书；结合已付完整 200 列呈示，才得同 F127 原十七梯度理想非成员性。它不排更高 Bell 幂，不排加 b-1 后成员性，不自动升 E。

正支保完整 77276 坐标累加器，逐原来源普通乘回。整列乘积完成后才提交，未完成列的局部更新不写入恢复状态。全原来源完成、全目标坐标相等，才进入多项式原来源回填。

独立验算 cursor 已为 N 而最后目标检查尚未完成时，下次只完成目标检查是合法后继。

## 8. 正支十/十八/十七原来源

driver 按全部 13808 标签合成 200 个参数多项式系数，核准确补权、无 moment 变量、原标签唯一。逐原来源回读真实 phase，累积原十坐标和原十八来源。一个完整原来源事务结束才更新 prefix；每十个来源或预算边界原子登记。

最终必须同时核：

1. 全十坐标等于字面目标向量。
2. 全十八来源乘回 delta14*b^2，Bell 槽严格零。
3. 经实际常 Jacobian 运输，全十七物理梯度乘回同一目标。
4. 原来源加权总权准确为 10；物理梯度次序前十一项权 4、后六项权 5。
5. 完整原乘回字面 Bell 粘合：

$$
\delta_{14}=\delta_{14}b^2-\delta_{14}(b+1)(b-1).
$$

只有全部门真才付同 F127 原图 Bell 来源。多项式数组、累积值、certificate 及 final phase 均只保 TMP/作业日志，不入 Git、Release 或新工件。

## 9. 同绑定完整阶段恢复

每次 generation 用新文件名；临时文件 flush/fsync/rename 后才登记完整 SHA。旧完整 checkpoint 保留。恢复前重新核全部文件身份、固定格式、字典及同 semantic binding。

有效新进度为完整 source frame、input/audit、原矩阵整列、certificate、完整 native 子式审计、独立原列乘回或完整原来源回填。开始未完成工作、generation 增加和计时日志不算进度。

代码 75 仅表示真实预算中断；内存、格式、来源、编译或数学验证失败不改写为 75。wrapper 必须同时看到 source 的 continuationEligible 与独立核全 SHA 后真实进度签名改变，才使用下一个冻结预算。

特别保留两种后继：

- native 的 initialCompleteColumns 已为 N，下一段可以只构造完整 certificate，不必再增加原列；
- checker 的 initialVerifiedColumns 已为 N，下一段可以只核目标而完成验算。

如这次仍未完成任何新阶段，不能凭再次启动而续跑。外层强停若发生于 checkpoint 写出前，未完整文件不消费，先前完整状态仍有效。

## 10. CLI、模式及输出

完整 CLI 中花括号由受审 wrapper 展开：

```text
python {scripts}/2026-11-16-r150-original-weight10-full-macaulay127-789f.py \
  --native-source {scripts}/2026-11-16-r150-original-weight10-full-macaulay127-789f.cpp \
  --checker-source {scripts}/2026-11-16-r150-original-weight10-full-ordinary-verifier127-789f.cpp \
  --controls-driver {scripts}/2026-11-16-r150-original-weight10-macaulay-controls127-789f.py \
  --bitplane-header {scripts}/2026-11-15-r150-original-f127-bitplane-789f.hpp \
  --prepared-source {scripts}/2026-11-16-r150-original-delta-weight10-runtime-parent127-789f.py \
  --model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --chart-source {scripts}/2026-11-16-r150-original-rank-four-unexpanded-local-source127-v2-789f.py \
  --producer-source {scripts}/2026-11-16-r150-original-two-round-complete210-sources127-v2-789f.py \
  --vector-helper {scripts}/2026-11-16-r150-shifted-module-weight10-verifier127-789f.py \
  --prepared-out {work}/original-delta-weight10-homogeneous127-runtime \
  --model-out {work}/original-ten-parameter-module127-v2 \
  --mean-out {work}/original-mean-first-frontier127 \
  --weight8-out {work}/original-complete-weight8-frontier127 \
  --producer-out {work}/original-two-round-complete210-sources127-v2 \
  --controls-out {work}/weight10-macaulay-controls127 \
  --out {work}/original-weight10-full-macaulay127 \
  --through final \
  --seconds 600 \
  --memory-mib 2048
```

模式 controls、input、columns、verify、final 分别是：只编译控制；封完整输入；全原列与子式审计；独立原矩阵乘回；完成对应支路所有实际门。columns 尚不含独立证书验证；verify 正支尚不含十/十八/十七原来源回填。

controls 仅需四个冻结源文件，不要求原 200 父目录，也可直接运行已付小控制器。完整 driver 的 --controls-out 要明确验证实际小回执、manifest、同来源 semantic binding、全部二进制及控制日志 SHA，才桥接编译产物，不把旧计时冒作本次编译身份。

完整输出名为 full-weight10-macaulay-manifest.json 和 full-weight10-macaulay-receipt.json。所有 sourceframe/input/state/certificate/ordinary progress/positive phase 均在新独立 out。外部只发布来源、参数、run 与 bytes/SHA。

## 11. 新作业的完整父重建

结束作业的 TMP 不能假定存活。新 request 在同一个 job 顺序完成：

| 步骤 | 原任务 | 秒 / MiB |
|---|---|---:|
| 1 | 两份冻结 C++ 实际编译及 controls | 120 / 1024 |
| 2 | 原 field model116 | 180 / 2048 |
| 3 | 原参数来源压缩50，final | 180 / 768 |
| 4 | 原 mean 第一轮30，final | 180 / 768 |
| 5 | 完整权八输入 prepare | 180 / 768 |
| 6 | 完整权八 rank/relations final | 180 / 768 |
| 7 | 完整210原来源 final | 900 / 1024 |
| 8 | runtime-parent 完整200输入 prepare | 600 / 2048 |
| 9 | 本完整 Macaulay final | 首段600 / 2048 |

步骤 2–8 原算法、来源 pin 与完整数学 gates 保持原样。计时回执必须来自新 job，不能与旧 elapsed 字节强行相等；已付数学 manifest、全部 source phases 的物理/逻辑 SHA 则仍原样硬核。child binding 同时保本次实际 prepared/210 回执与旧数学身份。全数据同 job TMP，不以未核缓存跨 binding。

步骤 8 仅在完整 prepared prefix 新增时用 600、1200 秒同源续。步骤 9 先保四段预算 600、900、1200、1800 秒；之后最多预置三个额外 1800 秒段。每一段，包括额外段，都必须由上一轮真实代码75、source continuationEligible、全部完整阶段SHA和改变的真实进度签名支付；失败、空进度、只有新日志或generation都不会进入下一段。各段外层加60秒。额外三段不是一定启动的承诺，原170分钟deadline始终优先。

每次完整进度守卫通过后，worker发布一个小执行身份：run/task/已完attempt/下一attempt/下一预算、前后签名SHA、同sourceSHA、eligible及deadline布尔。文件在 notes/r150-original-weight10-macaulay-execution-789f/，名称含 resume-decision；无数学数组。每次真实下一段开始前再核整个进度签名未改变，且原step重新核timeout加120秒能装入deadline。若当前已有新进度但预算表用尽或剩余时间不足，则只发布相应停止决定，不启动新数学。

same-job 工作上限 170 分钟，workflow 硬限 180 分钟；实际 deadline 还扣除自 workflow 启动已耗时间，保至硬限前约两分钟。每段启动前检查 timeout 加 120 秒仍在 deadline 内，否则不启动新的数学任务。约一 GiB checkpoint 保在同 job 各段之间。

每个步骤及每次续段开始都实际 pull/read 两 README。长算进行中若距上次实际 pull 达 28 分钟，再真实 pull/read；不把运行一小时当可跳过规则检查。worker 的数学脚本是固定 TMP 副本，规则拉取不热改正在运行的源。

Python3.12.14、python-flint0.9.0 固定；不安装或调用 Singular。源码和身份可发布，数学数组不得上传。

## 12. Wrapper、request 与 workflow

| 文件 | 字节 | Git blob | SHA-256 |
|---|---:|---|---|
| notes/2026-11-16-r150-original-weight10-macaulay-session-789f.py | 26120 | bafe782e233c67b384952eab2de074a3d12c929d | 192a6f0e0fd1a56e2372541b9fd5b1cb6c63688a7d5795268b8889c703b94202 |
| notes/2026-11-16-r150-original-weight10-macaulay-session-request-789f.json | 26887 | 282104c71789e2cbc91de7f6f5307e692f0451fb | 2dc4a2725835c6aa3f3c09f4b48dad893e8da2165266e2634ca3b1da49744e50 |
| .github/workflows/invariant-subspace-r150-original-weight10-macaulay-session.yml | 1851 | 370b8da936cb1d5a93b94f579fff31091e8c4c99 | 3bd7639a34831d1800284a37d1bb3d62143e9e4b6e5105cf83031aa0c47705d1 |

冻结模板 request（blob92c5eb276d43aa5569547613ffe02151d9e74da1）的 rootMustRefreshActualRuleReadBeforeDispatch=true 是规则交接门。root 已核 run43926430589 于2026-11-16 18:12:55 UTC的真实pull --rebase，原提交1e85aa7c462cb0d62a0d80e745622a6874497378，两README blob均未变；本表列本次启用request，已登记该真实读取并清除此标记。启用仅更新规则读取和作者/执行身份，九个数学任务、全部source/CLI/完整进度守卫不变。publisher在实际dispatch前仍再次pull并核两README；若有新差异则停止待root读差异并遵守。

wrapper 保已审 pull/rebase、两 README 比对、仅来源/参数/运行/哈希发布、H marker 冲突恢复及 non-fast-forward 重试。新增只为本格式与同绑定完整阶段进度守卫。root 独占主线/HANDOFF 和 dispatch，运行中不热改冻结计算源。

## 13. 严格结论边界

原列前缀只支付该完整计算状态。完整秩或零余式也不直接给最终正负结论。

负结论须完整原输入、全部 native 状态身份、独立 ordinary 对全13808原来源列的零点积和原目标读数1。正结论另须全部十坐标、十八来源、十七物理梯度及字面 Bell 粘合乘回。

新的特征零结论、所有更高 Bell 幂、整个原理想判空或 ISP 完成都不是本程序预设结果。
