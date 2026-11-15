# 第 71 轮：实际 cusp11 与普通12 的新 with-J 完整 primal 逐位吻合原 no-J

作者：geometry；日期：2026-11-15。分类：真实公开 Actions 数值结果与完整原件字节核验。

## 1. 已完成的具体事实

在实际 61 失败末状态的完全相同原始输入上，第 71 轮分别执行原 no-J stage 流和独立的新 captured-root variational 流。stage11 和 stage12 的 **全部 226 个返回状态字、两个独立均值状态字、端口转换后的 224 个形状输出字，以及原 meanHeight 求和的返回数值记录，全部逐位相同**。两段都实际产生了新的完整 226×224 tangent 和 224×224 post-port J，没有读取或复用旧保存 J。

这给出了 R275 原 primal 条件恒等论证的两个真实案例：一个包含原 cusp 的拆步分支，另一个是不拆步的普通分支。它足以支持从真实失败末状态使用新实现继续完整原生流程；没有证明所有 576 段已跑新流，没有证明新 J 的精度或原生方程已达到容差。这里 `native_accepted=false`、`task_completed=false`，完整 native evaluate、native solve 和 nonlinear trial 次数全部为 0。[原始 summary](public-actions-43656397000-1-modelresponse/noj-matched-variational-probe/summary.json)；[R275](../results/R275-original-noJ-primal-identity-and-complete-variational-chain.md)。

## 2. 实际运行与输入身份

公开 [run43656397000](https://github.com/Rogerhu12/math-research-public/actions/runs/43656397000)，source `3df227cb306922ee7eed7bf61764c6dc7c5a3eb9`，job `132635751719`，结论 success。科学步骤于 2026-11-15 00:06:31Z 开始、00:06:52Z 结束；publisher 也实际成功。producer 报告两案例核心流程耗时 **3.997s**，launcher 整体 **19.900148261s**；两者范围不同，不拆猜单段或单种计算时间。

完整 artifact `14138501210`，名 `visible-mainline-modelresponse-43656397000-1`，1772764 字节，ZIP SHA256 `aeb4413fba6d369a384260ba021ee18cf30aa7d32a7ad285bd5c163db1e05ec8`。根会话唯一下包并核 size/SHA/CRC，本核验没有再次下载。

原父件是实际 61 的最后一次 fresh with-J snapshot：

| 对象 | SHA256 |
|---|---|
| 原失败 native result | `b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef` |
| iteration003 snapshot result | `5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286` |
| 完整577×224原始状态 | `b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013` |

两 stage 的完整初值都取原 node `stage+1` 的 224 个字，并保留原 core 新建的两个 `+0` 均值积分状态。原完整 H、target、σ、profile、port 和原12步参数未更改。实际 source 为：launcher `51e4ae727e05e5cfaeb7a104617eef94dee2a4d1a9671bd2897f77e0dc4b62d1`，hook `f80b2a1ba38f546144d9ec21f344bc1483fd259dcbef35b8d12f2ab66b9b11fb`，新 flow `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。[launcher 原报告](public-actions-43656397000-1-modelresponse/noj-matched-variational-probe/launcher-result.json)。

## 3. 两个真实案例

| 真实记录 | stage11 | stage12 |
|---|---:|---:|
| rawCell / rawSegment | 0 / 7 | 0 / 7 |
| 原 profile cusp | 0.9577179846526143 | 无 |
| 实际内部步数 | 13 | 12 |
| 原 no-J RHS counter 增量 | 52 | 48 |
| 新流原 root / RHS 次数 | 52 / 52 | 48 / 48 |
| 新 captured local-J 次数 | 52 | 48 |
| tangent 阶段额外原 root/RHS 重算 | false | false |
| 全226 state逐位相同 | true | true |
| 两个独立均值状态分别逐位相同 | true | true |
| post-port224输出逐位相同 | true | true |
| 原 meanHeight 返回和逐位相同 | true | true |
| 原 portRatio | 1 | 1 |
| producer minA | 0.9999999999869661 | 0.9999999999994033 |
| producer minD | 0.9999999999999885 | 0.9999999999999988 |
| producer maxRootRelative | 7.899111427052261e-14 | 5.2399674131638593e-14 |

表中 scalar 均照录实际原返回，未本地重求 guard 或范数。原 no-J 和候选均真实返回，原 guard 没有抛错；没有另外添加 A/D 或 root 误差阈值。[stage11](public-actions-43656397000-1-modelresponse/noj-matched-variational-probe/stage-011-result.json)；[stage12](public-actions-43656397000-1-modelresponse/noj-matched-variational-probe/stage-012-result.json)。

stage11 的 ordinary index0–10 保原 `h=0.08333333333333333`，最后 ordinary index11 真实拆为两个子步：原记录 `(x,h)` 是 `(0.9166666666666666,0.04105131798594763)` 与 `(0.9577179846526143,0.04228201534738574)`。对应 h bits 分别为 `b0286aa8ad04a53f` 与 `00824002fda5a53f`。stage12 的12步均为原 local-cusp wrapper 的 unsplit 分支，其 h bits 全为 `555555555555b53f`。这些来自保存的 schedule 原记录，本地没有重建 grid 或重算 h。

两份记录共25步、100个 field，保全部 x/h 的数值与 IEEE 字、各 field 的 geometry 五列、root err/scale、A/D、状态/RHS/local-J 的 SHA，以及相邻完整 state/tangent 的输入输出 hash。实际均值总增量为 stage11 `0.00017477984919618542`（`fdf9fb78a3e8263f`），stage12 `0.0003036888125163783`（`995596840de7333f`）；这些与第69轮原 no-J 相应 mean 字一致。

## 4. 旧 with-J 差异仍真实存在；新流对齐了哪个对象

本次重新执行的原 no-J 输出，与第 69 轮同状态全段 evaluate 的对应输出 row 逐字相同。新候选又与本次原 no-J 逐位相同。因此它对齐的是原来实际用于试步验收的 primal，而不是把旧 with-J 输出重新命名。

本次原报告再次保留了旧保存 with-J 对当前原 no-J 的实际差：

| 段 | 不同输出字数 | 最大原σ归一差 | 该路径差最大分量 |
|---|---:|---:|---|
| 11 | 203 | 6.144400021985094e-5 | Pi104，frequency208 |
| 12 | 203 | 6.638335060581278e-7 | Pi76，frequency152 |

这里的“最大分量”是两个实现的**输出路径差**，不是第69轮原 residual norm 的 argmax。原 same-state no-J/with-J norm 共同 argmax 是 stage11/Pi75，这两个定位不可混用。新候选和原 no-J 的不同输出字数则均为0。[第69轮结论](2026-11-14-actual69-same-state-noJ-withJ-discrepancy.md)。

## 5. 完整字节核验范围

配套 [字节审计](2026-11-15-actual71-noJ-primal-stage-byte-audit.json) 已完成，结果 PASS。实际读入本 probe 的35个文件，核了 manifest 中14个 raw阵、总计 **1,630,816字节**，包括两段完整输入、两套完整返回 state、两个新 full tangent、两个新 post-port J 和四份 post-port out。

逐项核验包括：

- launcher/spec/summary/stage报告/manifest 的 SHA、大小、schema 与 source/module 身份；gzip 全解压 SHA/大小。
- 14阵全部完整 raw SHA、shape、C-order、binary64 字分类；两段 full226 和 post-port 输出字节相等，两个均值分量原字直接相等。
- 两个实际 port 均为1，所以新 post-port J 原 bytes 与 full tangent 前224行直接选择出的 bytes 相同；没有在本地重算矩阵或除法。
- 25步完整 state/tangent hash 链、首末点与实际完整 raw 阵的 SHA、每 field0 的 state hash 和相应 step input hash、全部100个 local-J 哈希记录的格式/来源、实际 ordinary/substep 顺序。
- 1142个 numberRecord 的 JSON值/IEEE bytes/分类一致；原 evaluate 和5种实际 engine 方法文本的 SHA 一致。仅是源码与数据身份，不重复执行方法。
- 与第69轮已存原始 b34…状态相比，两段初值的224字完整吻合 node12/node13，新增两个均值字确为 `+0`。本次原/新 post-port输出及报告 meanHeight 字也与第69轮对应原 no-J 行一致。

阶段内部的完整 state/RHS/local-A **只有 SHA 记录，未另导出全部 payload**。本核验确认这些记录和链的字节/引用一致，没有声称独立重算它们或重新核验旧61全 J。原完整新 tangent/J payload 已全数核过；未做 Jacobian 作用、norm、差值、SVD、FD 或科学数值重算。

新完整 post-port J 的实际身份为：

| 段 | 新224×224 J SHA256 |
|---|---|
| 11 | `1bbd15a65a59b437ef5354403b1df21e950ac248b627915c731a9d8340090b2b` |
| 12 | `b8356dacd5ae64fdea15393ea190ab754f0bf7e55fb710e0b1698d9367bbae9a` |

## 6. 后继与边界

下一执行对象是从同一真实失败61末状态启动的完整 current576 单请求。每轮 fresh with-J 使用独立新 flow，原 core 仍保完整32次上限、十次 no-J 试探、strict norm 下降、2e-9容差、全部原 guard，非线性校正用完整 R273 eta1；最终 endpoint sensitivity/J/audit 不用阻尼替代。

该续解会产生新的真实状态/J/残差与当前矩阵身份，不能假定沿用第61轮下降历史；也不能由两个 stage 的逐位一致推断最终 native、prefix 联解或闭场已完成。这里不再增加测试门，实际续解的全部原验收仍决定其结论。[续解接口](2026-11-15-noJ-primal-current576-native-continuation-interface.md)。

本次主要小原件：summary12744B/SHA `4198f3e8969ee28d38a2c6135eee3b07ebcde9382411fed3996831ab1af11e65`；launcher-result1875B/SHA `1c37361c6cbb1d0b0d51159c3b8c5dad8409262152d9939ecced7e3755a97f97`；array-manifest3785B/SHA `40abad123f6826492310e05eae85e336668101615db97e4bd1beb69ddc2c20b7`。公开原报告和 artifact 保留所有失败/返回事实，本文只消费这些已产生的证据。
