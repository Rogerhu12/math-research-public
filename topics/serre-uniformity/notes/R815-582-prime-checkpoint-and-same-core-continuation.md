# R815 原 Mg/Γ 的582素数断点与同核续算

**状态：实际断点，原 Mg/Γ 仍未恢复。** 本轮沿原425素数断点继续，没有重新启动原素数序列；自然预算停止保留了582个完整素数的 CRT 状态。

## 实际结束与可恢复位置

公开 [run43748439850](https://github.com/Rogerhu12/math-research-public/actions/runs/43748439850)，compute job132916821952，source a108ce1e72958b296dcca7ff55710c94e8ed16ef。数学进程于2026-11-15T23:47:59.301559+00:00结束，退出码1，外层run error=null。core记录 BudgetStop: Complete original operator stages and latest CRT states retained.；最新原子阶段的core elapsed为18011.639080828秒。这是预算断点，不是准确恒等式反例。

当前仍为target=g、field_component=0；已完成582个素数，最后1000011869（index581），coefficient_count=295936，模数17401 bits。这个位数只是当前CRT模数，未声称达到系数高度界，也未声称原重构不可能。

| 原文件 | bytes | SHA256 |
|---|---:|---|
| R815-target-g-component-00-CRT-current.json.gz | 769309011 | 67e7fe984535be03c77971f4d4bbd234d2159c34ba3c0d7360f1cac8d8dce01f |
| R815-target-g-component-00-CRT-step-000582-receipt.json.gz | 3899 | 5a5858848233f141512859a74b3a8de7e40c84c694ac33b5054c6895fb15c0bb |
| core-receipt.json | 549 | b1c43fd3e7ded69a59bfdd1ff726f6c5f5cc36097eb6982a5d4c245831212257 |
| run-receipt.json | 591 | 9cca117a5139e720a48552df686b638f16fb28eb4a78d254464e8593d7d2d202 |
| public-actions-input.json | 10258 | a90dfa5bf2a55350b06cd7b3acdc4058e0028694a8b421b099da837e76442919 |
| retained-inputs-receipt.json | 16388 | 7de014be25e8d963d651662a7670ba32c7fef4a1a571eb9854edb8a6868c28a0 |
| R815-retained-producer-inputs.tar.gz | 109958828 | 051571e117cdaafe31f9851c664c72583f55181444dbe112bbcbb7f2d2fbf1b3 |

已逐字段比较最后step的current_full_CRT_checkpoint与真实full manifest的current spec，完全一致。basis configuration为b92034874a9afe85d74112e8b429de1f0be67ef10dc4fabc7c5d92c741e64cec，target configuration为88c00c7f1d65fb8ae4f2350ee26fa4f6b8d2cd73612b15ca7d3d183fc7720ca6。Γ尚未开始，final Mg/Γ与原指数证书均未得。

## 实际载体和读取范围

artifact14186797329，名称serre-global-R815-original-normal-derivation-operators-43748439850-1，3627197324 bytes，平台ZIP SHA256为e07f91b7b739c9fe2294e7eb1e17474ebae1f3187e6dfe5e6e48a12b7fcd31f9；实际到期2026-11-16T23:48:02Z。ZIP有4742成员；full manifest为1220633 bytes、4740条、SHA256 460daad85b36b2cf84651b32f554b74d47d609af9b29aed82cffb5e0e996f652。reference为368 bytes、ad7c645bb8b36e9d828ecaf9ba10e7dd835ec8b2a7a32732d33c9249d0e6b1ff。

本次本地操作严格是读取和SHA核对：11个Range请求、894481 bytes，取manifest/reference及6件小原文件（所选小文件63809 bytes）。没有下载或本地hash整个3.627GB ZIP、769MB current、109MB输入载体，亦没有执行CRT或重构算术。这些完整SHA和阶段恢复交由原公开Actions wrapper执行。

实际原输入收据确认仍为53件，R806的45件与R813的8件，每件原size/SHA已由生产者核过，且本轮恢复复用了原输入载体；没有重算旧W、g/h或Fourier数据。本地也比较了真实public-actions-input.job与本轮仓库请求.job，除随后明确修改的resume外不引入隐藏变更。

## 唯一请求变动与继续要求

[原公开请求](R815-public-original-normal-derivation-operators-request.json)只把job.resume从425素数producer更新到本记录的582素数producer、artifact及manifest。新请求10033 bytes，SHA256 9155a3ef28ef213309612dca701f58f9c60240fd30d8ef47b081fbb94b22af77；其余job字段和会话字段逐键保持。

冻结核心与包装器保持：

- 原core：80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d。
- 原wrapper：ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454。
- 原R811框架：849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3。

targets=[g,Gamma]、prime_start=1000000007、16行块、每8素数重构、300分钟自然预算，以及deterministic_integer_points_with_weighted_degree_bound均不变。下一次必须从当前完整阶段之后继续；仍须原七个准确点的完整commutator/嵌套commutator、首列、两图转换及指数规范通过，才接受完整算子。

[三准确列及49旧拒](R815-three-known-columns-ended-and-denominator-boundary.md)和[九维固定调度](R815-eight-probe-ended-and-fixed-schedule-boundary.md)仍关闭，不重复同一候选或旧格。当前没有独立Mh，也没有极理想、eta或高度结论。Git仅保存本说明、参数和代码，机器阶段仍只在一日活跃Actions artifact。
