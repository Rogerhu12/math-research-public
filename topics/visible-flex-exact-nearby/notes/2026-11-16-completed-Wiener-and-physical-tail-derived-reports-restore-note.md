# 五份已成派生报告的原字节恢复说明

2026-11-16。本文只登记普通清理的五个已成派生 JSON；不运行任何科学、不改写原证明或已成结论。所有相对路径均以 `topics/visible-flex-exact-nearby/` 为前缀。

## 1. 精确恢复身份

以下五件合计 **464459 B**。每件恢复提交均固定为 `19d7802877185806e000d9890e9f7dac389d0977`；恢复到表中原路径后，先核完整 Git blob、字节数和 SHA256，再供原消费者读取。恢复是取回原字节，不重跑生产源、不用摘要重造完整报告。

| 原路径 | Git blob | 字节 | SHA256 | 来源 |
|---|---|---:|---|---|
| `notes/2026-11-12-ci-canonical-v0-scaled-Wiener.json` | `936a3e8f9989acc42c9d1e34110d3a252824a2da` | 156284 | `3709417eec2b87e21f81f83c05dc83e113fd881984ea2e7de6678cbafe85db68` | V0 |
| `notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json` | `31a100ed2c37a928c54ca090a281abc9755eaf1a` | 49852 | `66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8` | V0 |
| `notes/2026-11-12-ci-canonical-v1-scaled-Wiener.json` | `37240b68cf180639a47a9d5a444d5440d1e2ede9` | 107059 | `c736ccff24d8cacc607d5a8f016f66b72a2565112e989ea01e4078c5dc9e1ae6` | V1 |
| `notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json` | `9c114c1c56fd6cc8142cf17dd117050499b40e74` | 35066 | `c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b` | V1 |
| `notes/2026-11-12-actual-canonical-physical-column-weighted-tails.json` | `8156bc55f932e7ebe1a146eb9261e30b9740840f` | 116198 | `bfc7ea9c2d27e2937bd69b8f238cb6cfd3a19e056a9dc115e8a4c022e2b39ac6` | PT |

三个大报告的 SHA256 逐字来自下列已全文读的小 manifest/summary；没有重新下载或本机重哈希其正文。两个 summary 已全文读取并独立核其字节和 SHA256。表中大报告 Git/size 由 root 的服务器元数据锁定；实际删除前仍由 root fresh guard 核同一对象。未清理任何源码、NPZ、gzip/native、对象定义、方向、原失败结果或本文列出的独立小证明与 manifest。

## 2. 已成范围与实际参数

**V0。** 完成 run `43304292862`，320-bit Arb；先前 `43303990088` 的变量覆盖失败仍是失败且不转授证书。真实 affine 家族中心为 `-7789843107295549/4611686018427387904`，半宽 `1/1000000000`；完整准确参数端点由两 summary 的 `identity` 原字保留。原配置为物理/canonical 各 16384 节点、Taylor 16 阶、保留 canonical `|k|<=4096`。小表的 90 行为 cutoff `[16,32,52,64,96,128,192,256,512]` × 权阶 `0..4` × 矩 `0,1`。同一真实 `v0` 的有限参照、全部低系数 L2 费、双侧无限解析尾与原高剪切范数都保留；准确常数 5050 仅加入零系数，矩 0 保真实均值。总结不是全反馈逆或非线性解完成证书。

**V1。** 完成数学 run `43299719198`，320-bit Arb；Git 发布权限失败后 `43300446121` 只取回同一已算 artifact，未从摘要重造。家族与物理/canonical 网格、Taylor 阶、保留模式同 V0。60 行为 cutoff `[52,64,96,128,192,256]` × 权阶 `0..4` × 矩 `0,1`，对象是完整实际 `(v1 composed with H^-1)/3` 的 scaled Wiener 界及其高空间算子界，矩 0 保均值。原 frame/完整无限尾、原成功与失败状态、实际新计算和原本地字节未恢复的区别保持；不授全反馈强逆。

两 summary 是各源在完整报告保存后按字段抽取的派生报告，`report_sha256` 绑定各自上表大报告。它们各保完整所选行的有限参照、误差和真尾，但不是完整报告的替代证明。保留各独立 nominal coefficient NPZ：V0 SHA `890b7d6296a62711bc0aabe76a4cc5a1864e06a263729863a9b17f487a63935f`；V1 SHA `5c0653d5844e5de2259e2e856ef5efeed0577b2d84b355cb18078fef2dfe8615`。准确中心对象 SHA `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`、原方向 SHA `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab` 及原 fit/nominal/native 均不在删除范围。

**PT。** R92 补充明确为同一真实 affine 家族 `delta5 +/- 1/2500000` 的已完成有向常数，不能混作 V0/V1 的窄家族参数。256-bit Arb；物理外条带 `1/256`，内条带 `7/2048`，canonical `|k|<=61` 共 123 列、剪切差秩上界 246；常数分解 5050 和阈值 2048。源的默认物理 cutoffs 为 `[64,256,512,1024,2048,3072,4096]`；完整已读证明明确列出实际完成的 512、1024、2048、3072、4096 行，本说明不靠默认值猜另两行执行身份。准确剪切差含常数对角、两个剩余势交叉项和双 d 项；每列独立权、正负全部模式及均值保留。已成内容是全物理 L2 有限角替代尾和高输出齐次 H^(1/3) 尾；不是有限物理列条目、完整耦合反馈逆、实际 R31 或非线性零解。

## 3. 完整生产源与小证据

三份生产源已全文读取，下面哈希与摘要/ready manifest 原值一致；恢复报告时不执行这些源。

| 来源 | 生产源路径 | Git blob / 字节 | SHA256 |
|---|---|---|---|
| V0 | `scripts/fourfold_phase_canonical_v0_wiener_ci.py` | `a59f0c53b7d43f66af75f6c4a70039d7b3e58905` / 13376 | `197fd0ad59c00e8cd56909728a270b371d64f6f17cb3337a180303e13ebb5a29` |
| V1 | `scripts/fourfold_phase_canonical_v1_wiener_ci_v1.py` | `1cfa2a1f0513e22e5c5202681477c62a4bb533b0` / 12930 | `2d5ee3ff7a16008cdbeeb760b455ce53b0d919c7f7db3ee8d3883828bd5269c4` |
| PT | `scripts/fourfold_phase_canonical_physical_low_columns_constant_split_v2.py` | `ee8967ec4ea0d7d642d6e2b3c9a06908d9c65810` / 10185 | `8f2e05921933827547ab9464821bad6a788d6c1119da9b11e834829f83d1ddd3` |

保留并全文核对的小证明/清单（Git blob、字节、SHA256）：

- `notes/2026-11-12-ci-canonical-v0-manifest.json`：`1e21ff2bcb3efe014ec61f47a5d5fe08e7bd9dfc` / 895 / `2bc95c558938a8fdb02abd28e0b6b641b67afb169eec44f67f560dc59fc35559`。
- `notes/2026-11-12-actual-v0-and-common-root-budget.md`：`d74bccbbb9798df161bd383fc8ebf1309700bc6d` / 6713 / `34ea229dba7593db331cd02f20f415b55bc72b531e62cd427b966e515ad03575`。
- `notes/2026-11-12-ci-root-r99-manifest.json`：`9b8dd742d386a0b7f3196c3531eefe73aa2d18ad` / 1358 / `6cfbdbb5b8cfda111e535929450106ab2cd597b4186f1b0c738c621b6bd28822`。
- `results/R99-actual-root-cauchy-frame-and-canonical-v1.md`：`9da3d8a83e336218d0dcffa4c200b9326ea26c9f` / 14774 / `df19c58b1359f215684871a66208408417f36870c99b0522eccf79d231f4a479`。
- `notes/2026-11-12-R92-weighted-column-tail-ready-manifest.json`：`1a3daf64a206fce0e1823113134d650b3008dcc3` / 1205 / `b94aa03d849f2efcbb6bbb856e1ae4b040c1240d07f8995712be1b2a7c09d340`。
- `results/R92-supplement-constant-split-and-weighted-physical-tails.md`：`1bd49c869e9c7ea790ca4711e6c87d8b0fcb0fb8` / 5207 / `16af0b5fe6dc71bf99ce26270929b4c08f421855a1fec3474c8ce57c2b756bcc`。

## 4. 依赖与明确排除

原历史消费者确有依赖：共同根预算和 canonical stream-gap 源读取 V0/V1 两 summary；旧物理列 manifest 的 `physical_tail_path` 引用 PT。未来恢复这些原消费者时须先按本表取回所需 JSON；不声称历史无依赖。Root 已确认当前 WJR/WSM/WPS 的冻结输入不消费这五件，本次不作全仓传递依赖不存在的断言。

`high-boundary-columns-cap-parameter-batch.json`（root 元数据 Git `a4536a7ab9693932e72296f287d39dd15a0d8f43`、100886 B）**跳过**：当前小证据未锁其完整 SHA256、生产源/参数及完成身份，不纳本次清理。意外返回 239529 B 的 `data/root_finite_grid/physical_columns4096/manifest.json` 只检查了依赖头字段，不称全文审计，不重复读取、不纳删除范围。五项之外所有报告、原 native、失败证据及其他当前输入保持原范围。
