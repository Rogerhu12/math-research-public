# 原 delta b² 权十消费者：完整输入、独立验证与运行身份

作者：Astra-ISP-789f / literature_audit，与 /root；AI-assisted GPT-6 Astra Pro。日期：2026-11-16。

本接口只处理同一 $\mathbf F_{127},d=100$ 的 $\delta_{14}b^2e_0$。完整 $200$ 非 Bell 列来自已经实际完成的原 $210$ 来源包；旧权七和权八结果不重算为新目标答案。负证和正证的数学准则见 [独立移位齐次化证明](../results/R150-appendix-original-delta-weight-ten-homogeneous-verification-criterion.md)。

## 1. 当前两个主入口的区别

| 入口 | 源 blob | 字节 / SHA-256 | 用途 |
|---|---|---|---|
| 本地 v2 | `61af7aee865dbe7d2b99aece5fe518c2d69cbe4f` | 40014 / `dc7e36fa9bc98ab11eb1784e8f88e133f99e689b308fabbef00dbf4dde844309` | 消费本地已付父完整 raw 与 manifest 的精确字节；本次只运行 prepare |
| 新执行父桥 | `62b41e937a05480cda5824a4cf91dda5b71b67e4` | 40746 / `433e8942e30cde475bd6e7f13df43b4a6765a876dac495553de5fe6a53fd001f` | 新独立 job 真重建同源父数据后，以其新 raw 身份建立新 binding |
| 独立除法核 | `917418d74e660827f85dedbae1d5acfc54a01f96` | 13935 / `54b082184273e254495be8e1eb788e6569e8ca9cc4b83a1a5d4330304e9d4246` | 不调用 Singular 的完整稀疏除法、S-pair、输入及目标核 |

本地 v1 `d7ce3e045d058d5447659d1e356ff2897f0137d8` 已实际在 $0$ 列处失败：新增 physical 权守卫误用了先六 mean 后十一 Hankel 的顺序。原 chart 的 `coord` 字面顺序是十一 Hankel 导数在前、六 mean 导数在后，权为 $4^{11},5^6$。v2 仅修这两个物理权守卫并使用新 FORMAT/newout；不删除任何乘回，不继承 v1 checkpoint。失败是 exit1，不是预算或数学负结论。本轮 v1 未执行位于错误守卫之后的十七运输复核。

## 2. 完整父证与硬输入

新 $104$ 源生产者为 `9fede0af90889e05eb07cfc87146bec707844794`，22552 字节，SHA-256 `20cb960bc20fea18001488e84dae35518d74f3338697dfed619eaadae6a6b2aa`。其完整数学 binding 为

`41638323f597133aadeb65b2a1639899a162e2afbe6e7f7c477e93fae912cd80`。

| 已付父文件 | 字节 | SHA-256 |
|---|---:|---|
| complete210-sources-manifest.json | 144113 | `74eb5557203192b2b3e37b43189ceaa7ec34afeb698884f336331210d1bcf2ff` |
| 本地 complete210-sources-receipt.json | 32576 | `77724520a9b2aa89086d7bb39e7dcef48bbc1cef2faaef00e9d98fcc588b24ea` |
| complete-original210-source-model.json.gz | 35044 | `ed0b6811561a0799dff2cab99b2c7685a2ed820978be00c397a69f110972fed5` |
| 最终 phase 的完整解码字节 | 148424 | `f8b17d755d1515726632280fe110788dcf03128705172944a67d44f12de14bee` |

来源包实际完整 $106+104$ 列门全部通过，其中新增 $24$ 个 mean、$80$ 个 commutator 二字像均有完整十八原来源，Bell 槽严格为零。实际新增向量 $7034750$ 项、来源 $2707447$ 项。消费者逐个读取父 descriptor 并核压缩、解码双 SHA；旧 seed 的 descriptor 直接读取，不能把语义 `seed-NNN` 键误当实际 phase 键。

删除的仅是原 $106,\ldots,115$ 十个 Bell seed。保留的 $200$ 列完整权分布为 $5^6,6^{20},7^{30},8^{40},9^{24},10^{80}$。每列十坐标全部保留；原十八来源的非零单项式也逐项核权，物理十七梯度的顺序始终是 $4^{11},5^6$。

其它固定小源码为：

- 模型 `cbd03a000da605991e6e49f1b545c2388a10db43`，23879 字节，SHA `4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4`。
- 原四阶图 helper `11f6bf80f1ced7e5a2a21ae0f763ffb7225102d6`，35070 字节，SHA `ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3`。只复用字面 determinant/adjugate 算术。
- 模型纯数学 manifest 仍硬核 30466 字节与 SHA `9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2`。

## 3. 新 job 的身份桥没有放松数学原件

本地父 raw 中的运行时间等 metadata 不能在新 job 冒称同字节。新执行入口因此有独立 FORMAT、源码与输出 binding：读取实际新父 raw 的完整 bytes/SHA，将其纳入本次 semantic，并保旧本地 raw 身份为历史 anchor。

以下仍必须逐字相同：父生产源码；父 semantic binding；完整 144113 字节数学 manifest；其中所有原来源 descriptor；完整最终 phase 的压缩和解码字节；模型 30466 字节数学 manifest。实际新父 raw 必须 status=completed、指向该同一数学 manifest、保全部 $106/104$ 成功门和同一最终 phase。没有白名单式跳过原乘回，也不以相同秩替代来源身份。

当前父生产者的 manifest 只保存 semantic、数学 phase 及 parentMathematics；运行时间与实际父执行身份位于 raw。若新环境不能重现上述数学字节，桥入口立即失败，须报告具体原因；不能将它笼统解释为时间戳后继续。

## 4. 小检查与真实软件执行分开

已完成的本地小检查：两个主初稿 AST、位编码与字面 `wp,C` 比较、十二指数 lane 可除性、正负控制、漏掉必要 S-pair 时拒绝负证、错误行移位时拒绝、完整 binary 往返、数值 marker 的 1/10 边界。冻结 tiny-check 源为 `9c1835b73cf48591ba404f4adc38781b7e6e722b`。实际 $0.048724302$ 秒，九门通过；完整 tiny raw 为 1021 字节、SHA `604ac2a4e209df0c04d55c7e22057fdee8f06c3e21df20e774353443261b4c5e`，只留 TMP。

这些小检查**没有调用 Singular**，也未运行原 $200$ 列候选。真实 candidate 阶段另先调用实际 `Singular -v`，要求版本 4.4.1 并绑定二进制完整 SHA，然后执行同移位小 module 的实际 `std` 正负测试及原 `lift` 单位/十坐标测试。真实 engine 控制不通过时不启动原候选。

本地 Python 为 `/tmp/r150-normal-789f-20261116-1040/venv/bin/python`，3.12.14 / python-flint 0.9.0。本地尚未有可用 Singular；候选计划使用独立 Actions job 的实际安装版本，不能把本地源码测试称为已跑 Singular。

## 5. 实际算法阶段与结论门

1. `prepare`：完整父身份、原十七运输、原二十四 mean、两侧 adjugate、固定 delta 全核。逐列写 compact binary 和单列 ASCII；不构造权十的 $77276\times13808$ 大矩阵。
2. `candidate`：实际 engine 小控制；完整 $2000$ 个输入 SSI 坐标回读；`std` 仅提供候选；只有完整返回并保存、逐列 SSI 回读的候选才记进展。
3. `verify`：十坐标全文导出，所有非零候选列逐项核固定 `zz` 次数与齐次权；零列保序号，重复非零列不删。逐 $200$ 原输入独立除尽，再遍历全部 $n(n-1)/2$ 对并核全部同 lead-component、lcm 权至多 $10$ 的 S-pair 除尽。最后才计算完整不可约目标余式。
4. `final` 的正分支：零余式仍不充分。必须在原 $200$ 列上取得真实 `lift`，单位为 $1$，逐十坐标验证；再 `zz=0` 和同权系数投影，独立十坐标乘回；接完整十八、物理十七乘回与字面 Bell 粘合。

非零余式只有第 3 项全部完整门通过才是同原有限域 $J_{17}$ 非成员性。软件 `degBound=10`、候选标记、部分输入或部分对均不足。独立证明只使用 $\Phi(\Gamma)\subset\langle G\rangle$，不要求未知反向来源；完整截断标准基性质由齐次最小反例证明，见配套正式准则。

## 6. 本地 prepare 命令与预算

下列 `{parent}` 为现存且完整核 SHA 的 `/tmp/r150-normal-789f-20261116-1040`，`{own}` 为 `/tmp/literature_bell_rank4_789f`。本次明确预算为内层 600 秒、2048 MiB，外层 660 秒。

```text
{python} {own}/2026-11-16-r150-original-delta-weight10-homogeneous127-v2-789f.py
  --model-source {parent}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py
  --chart-source {own}/2026-11-16-r150-original-rank-four-unexpanded-local-source127-v2-789f.py
  --producer-source {parent}/2026-11-16-r150-original-two-round-complete210-sources127-v2-789f.py
  --verifier-source {own}/2026-11-16-r150-shifted-module-weight10-verifier127-789f.py
  --model-out {parent}/original-ten-parameter-module127-v2
  --mean-out {parent}/original-mean-first-frontier127
  --weight8-out {parent}/original-complete-weight8-frontier127
  --producer-out {parent}/original-two-round-complete210-sources127-v2
  --out {own}/original-delta-weight10-homogeneous127-v2
  --through prepare --seconds 600 --memory-mib 2048
```

此 v2 出口不进入 Singular。准备完成的实际身份另行记录；只读原父目录，不改原来源或旧失败文件。

## 7. 独立 Actions 的完整父依赖与预算

新 job 必须在同一个临时工作目录内完成以下实际阶段，不上传本地数组，也不假设上个已结束 job 的缓存仍在。

| 顺序 | 原入口 | 内层秒 / MiB | 必须观察的完整身份 |
|---|---|---:|---|
| 1 | 原 model v2，through seeds | 180 / 2048 | 116 全来源完成，模型数学 manifest 同 paid |
| 2 | 原 50 压缩，through final | 180 / 768 | 全 116 删除关系及原来源完成 |
| 3 | mean30，through final | 180 / 768 | 完整原权七矩阵和 30 来源/关系完成 |
| 4 | weight8，through prepare | 180 / 768 | 全 100 原像与完整权八输入 |
| 5 | weight8，through final | 180 / 768 | 完整原权八 rank/全部 100 来源关系完成 |
| 6 | full210 v2，一次 through final | 900 / 1024 | 本次实际完成全部 106/24/80 门与同 paid 数学 phase |
| 7 | 新执行父桥，through prepare | 600 / 2048 | 全 200 列流式输入完成 |
| 8 | 同桥，through candidate | 600 / 4096 | 真实 engine 控制及完整候选返回 |
| 9 | 同桥，through final | 600 / 4096 | 全部独立负门；仅零余式时继续原 200 lift 和全部原正门 |

前六阶段使用已冻源及参数文件。full210 的原本地执行分为 prepare、mean、final；新 job 使用同一已冻源码的一次 final 调用、明确 900 秒预算，真实生产全部 $104$ 列，不能假称旧前缀存活。特别是其原生产者要求 mean/weight8 的 receipt 已 completed，且读取已核的权八完整关系数学 payload；不能用其 prepare/sources 前缀冒充 final。无需重做十四高列换源，old106 直接来自 50、30 和权八真实保留 26 列。

四父源码依次为模型 `cbd03a000da605991e6e49f1b545c2388a10db43`、压缩 `025821b76d7b9a982a52d0ecc205065097ecd66b`、mean `049028bbcfa486e8335d589c203d7cf682c4d7ac`、weight8 `4e8f554b0979ec9c05d0c8c2dfdb024151de3b6b`，全210生产者为 `9fede0af90889e05eb07cfc87146bec707844794`。完整 argv 与十二个小源码的 SHA 见 [独立九步 request](2026-11-16-r150-original-delta-weight10-session-request-789f.json)，运行器为 [session wrapper](2026-11-16-r150-original-delta-weight10-session-789f.py)。本接口不称新 job 已 dispatch。

Python 固定 3.12.14 以保持已付 gzip 物理字节；python-flint 固定 0.9.0。Actions 安装后必须真实检查 Singular 4.4.1，不从工作流名称推定版本。拟定整体 110 分钟工作上限、120 分钟 job 硬限；每次内层外加 60 秒且开始前仍须满足完整剩余预算。实际运行需先由 root 审读运行桥、request 和 wrapper。

第七步若 exit75，仅在新增完整原列且相同 binding 时可续一次 1200 秒；第八步空候选没有自动续算。第九步只有新增完整候选列、输入/S-pair 验证前缀或来源前缀，且原 source 明确 `continuationEligible=true`，才可按 600、1200、1800 秒序列续接；所有尝试仍受同 job 剩余时间约束。wrapper 独立重算 semantic binding、检查 frozen source 和同父数学 manifest，不能以任意变化的 JSON 当数学进展。

## 8. 完整前缀续接、失败与存储

每个原输入、候选导出列、已核输入和 S-pair 只在完整单位通过后原子登记。source/binding/实际父执行身份不变才能续。候选未返回完整文件时，`candidateAbsentNoEmptyRetry=true`，即使内层返回 75 也不自动重跑空候选。

相关对可能很多；现版每完整对保存 manifest，性能可能受 I/O 影响，但不能据此跳过对。若有实际瓶颈，再按真实 prefix 冻结独立优化源，保完整门和失败身份。

只有预算异常是 exit75；内存、语法、输入、来源、同权或乘回失败均是 exit1。`completed-diagnostic` 表示候选未通过某个输入或相关对，不能被解释为原目标答案。`completed-negative` 和 `completed-positive` 分别要求 §5 的完整独立负门或原来源正门。

每列 binary 有固定完整 EOF、stored/decoded 双 SHA、weight、term count、leading term；单列解码上限由权十 $77276$ 个实际可用坐标导出。完整 SSI 上限 1 GiB、候选最多 65536 列、单列 ASCII 上限 32 MiB；超过任一明确界即失败，不截断成成功。

所有数学数组、完整 raw、SSI、日志、候选、来源及检查点只在临时目录或完成 job 日志。Git 只存源码、参数、证明与执行身份/bytes/SHA；不创建 raw 的 blob，不使用 Release 或新数据工件。

软件接口参考：[Singular `std`](https://www.singular.uni-kl.de/Manual/4-4/sing_364.htm)、[`degBound`](https://www.singular.uni-kl.de/Manual/4-4/sing_406.htm)、[`lift`](https://www.singular.uni-kl.de/Manual/4-4/sing_293.htm)。本入口的负证独立于软件的完备性声明。

## 9. 已完成的本地 v2 prepare

本地 v2 按 §6 原预算实际 exit0，用时 $275.63286762399366$ 秒，峰值 $154004$ KiB。全部 $200$ 列共 $8037189$ 项，单列 ASCII 合计 $151071880$ 字节，目标 $\delta b^2e_0$ 有 $2604$ 项。完整原父哈希、原十七运输、二十四 mean、两侧 adjugate、全部原来源同权检查通过。原 $200$ 来源乘积身份来自完整父证，本次没有把继承门误称重新做了所有十八乘积。

运行 binding 为 `dfb2420829d6b6243142e1232e4c2bdba4fa45fb1823fe81d119c4101493e488`。完整 raw 为 1667 字节、SHA `4484dbf8234ace6406936d46520925093782aeabeb6426f5114f4fe17c089ed8`；数学 manifest 为 410173 字节、SHA `d6d4a4921c8b874def17e3de84db64c6fa9716cf9ea173a7207e8538f54b41c5`。两者仅留 TMP。没有启动 Singular、没有任何候选或目标成员性结论。
