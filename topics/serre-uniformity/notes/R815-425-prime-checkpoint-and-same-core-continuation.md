# R815 原 Mg/Γ 的425素数断点与同核续算

**状态：真实阶段记录，原算子尚未完成。** 首轮在自然预算检查处结束，保留当前 CRT；不是准确恒等式失败，也不把未完成标志当作算子已恢复。

## 实际结束来源

原公开 [run43719622321](https://github.com/Rogerhu12/math-research-public/actions/runs/43719622321)，job132828560965，source `2a3300a9edec73c23e72f23127a0ae7d8222d13e`。数学进程在2026-11-15 18:33:50 UTC以1退出；run receipt 的外层 error 为 null。原 core receipt 与数学日志均明确为 `BudgetStop: Complete original operator stages and latest CRT states retained.`，并非某个 commutator 检查不成立。最终 verify 因 complete=false 返回失败是正确语义。

| 项目 | 实际值 |
|---|---|
| core SHA256 | 80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d |
| wrapper SHA256 | ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454 |
| 冻结框架 SHA256 | 849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3 |
| artifact | 14174374945；2716759066 bytes；3466文件 |
| artifact ZIP SHA256 | 597aaf0006481ed9fc47fda4bb6635ff6b1b8aef336d8484ca92a9bbe9e802c4 |
| full manifest | 892108 bytes；3464条；4e78095e2adc217beb86d4f760e6207a4aa60c4492bbfcc739a8544f376842e5 |
| core receipt | 549 bytes；b1c43fd3e7ded69a59bfdd1ff726f6c5f5cc36097eb6982a5d4c245831212257 |
| run receipt | 591 bytes；7d55b2fbe8e13da956293cd35c6c7832180e7f13ff92b6fcf21e0ef4f116069d |
| artifact 到期UTC | 2026-11-16T18:33:51Z |

## 真正完成的 CRT 位置

当前 target 只有 `g`，field_component=0。最新已原子完成 **425个素数**，最后一个为1000008791，模数长度12707 bits；这是 CRT 模数位数，不是已知系数高度界。该步记录的 core elapsed 为17990.078718832003秒，coefficient_count=295936。

当前文件 `R815-target-g-component-00-CRT-current.json.gz` 为561995095 bytes，SHA256 `402379e2b5a0d4b225fda74d798bbb164d77ce7c3001eddca789d0fe602ef27c`。最新小收据 `R815-target-g-component-00-CRT-step-000425-receipt.json.gz` 为3902 bytes，SHA256 `f136bee8e383b5fcff03a86bebc5bf8f30f3394d885f8aa4ac1e327ad7a82042`；其 checkpoint spec 与发布 manifest 中的 current 完全一致。

尚无完整 Mg index、Γ index 或最终算子证书；Γ 尚未开始。不能把425模素数当作特征零结果。

## 小IO的准确覆盖

已成功 [run43747973677](https://github.com/Rogerhu12/math-research-public/actions/runs/43747973677)，job132915386231，source `4781aac81b53ad3179a51e53909e45d89f5ffe87`。冻结只读脚本 SHA `0f587776b08bed675b0fce4014214c0ec4302c63286d234eaf7e431e9e25390e`；实际只用27个 Range 请求、506992 bytes 读取reference/manifest及6件小原文件。它没有下载或重新hash 562MB current、整个2.72GB ZIP或输入载体；这些完整核验由同核续算 wrapper 执行。

原输入载体仍是53件：R806的45件、R813的8件。载体 `R815-retained-producer-inputs.tar.gz` 为109958828 bytes，SHA256 `051571e117cdaafe31f9851c664c72583f55181444dbe112bbcbb7f2d2fbf1b3`；原全成员校验收据为17272 bytes、SHA256 `4aa031ebd61b94eeeebc9de7406ed6b0e852a67c15c64de33b10e817f500eb9f`。小IO只确认这个真实覆盖和已绑定的来源身份，不冒称重核所有内部 raw。

小IO artifact14175345855、1019384 bytes、ZIP SHA256 `edc5ef9b11eb4919d2ca5e39ea0a4d11442525e19039f5f9ac7278f6016887f6`，到期2026-11-16T18:39:41Z。

## 立即同核续接

[原请求](R815-public-original-normal-derivation-operators-request.json)只把原 `resume:null` 改为上述真实 producer/run/source/artifact/manifest。新请求10032 bytes、SHA256 `ac0870b286bbb472cc2550c343cb13e2b8b64fd357563f40e9210ca50ebc48a2`；除 resume 外逐键相同。

保留原 core、wrapper、冻结框架、53件来源、targets=[g,Gamma]、首prime1000000007、每8素数重构、16行块和嵌套准确模式。原 wrapper 会全ZIP/manifest核验，恢复完整阶段及各target唯一 current，从425之后继续；不回到首素数，不重算原W、g、h或已成 CRT 阶段。仍须原七个准确点的全部 commutator/嵌套 commutator、首列、两图转换和原指数规则通过，才称完整算子恢复。

本记录不声明 Mh、极理想、D、eta 或高度已得。机器数据只在一日活跃artifact，Git保留来源、代码和本说明。
