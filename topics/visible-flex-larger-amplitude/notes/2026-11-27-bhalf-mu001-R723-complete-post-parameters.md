# 第20轮 mu001 同源 R723 完整后续参数

## 1. 改动范围

本包只接第20轮的完整参数路径与科学参数投影，不新增或修改任何 runtime。两个独立R723源保持完整原字：

- fixed_fejer_R723_directional_closed_phase_grip_evidence.py，87,670 B，SHA256 1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc；
- fixed_fejer_R723_compatible_r716_centred_volume_moment.py，61,706 B，SHA256 3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b。

完整源码、数学证明、再生器及原第19轮参数在 computations/R723-directional-closed-grip-R716-complete-delivery.json 中：48,223 B，SHA256 b16346ee6f96d8aedc0f89a2ad6598a53b86af05cb1c3171ec1790e53bb896cc，blob 1929f73367894f35c92e6dfa86198a70889c4da0。所有 source-specific guard、原137角色、完整normal32、全角/全径向/六jet、五方向证据角色及完整R716独立unmarked链均不变。

本包没有执行科学，没有写 refs/queue，没有修改第19轮。它不把第19轮结果、旧root、旧费用或mutable progress搬作第20轮输入。

## 2. 第20轮真实科学参数投影

已经完整读取第20轮 science ready，97,019 B：

SHA256 89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca；blob 598b4cdf62021a66b54c22b71171722027f1c0b5。

完整157词 argv 仍在该源文件，并在本包共享绑定中全部保留。相对第19轮，原记录明确的两处变化是：

| 零基 argv 索引 | 第19轮 | 第20轮 |
|---|---|---|
| 37，restoration damping | .01 | .001 |
| 71，独立科学输出目录 | fixed-fejer-meridian-batched-bhalf-first | fixed-fejer-meridian-batched-bhalf-mu001-first |

metric damping 仍为 .01；端层总长仍 $b/S=1/2$，profile $\delta=1/32$。所有变量、原范数、所有root/QP/restoration/line-search预算、active rows、32阶段、方向和acceptance规则保持原字。完整science的458个formal字段、48个live字段，以及pure的完整7词和445个formal字段保留在其完整原文件，未缩减。

第20轮完整科学参数总表为 computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json，50,679 B，SHA256 ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4，blob 8eee403a87c988cb36fb55f6f82eb3ad0e1988db。

父记录给出的正式启动是 run46079535427/1，2026-11-27T22:55:41Z，启动提交85cd235221ace28158625a7ced52a24551b509eb。这是已有启动记录，不是本包重新查询的最新job状态，更不是完整参考、working model、point、snapshot、最终场或费用身份。上述未来物理身份仍为null。

## 3. 完整步骤与历史分开保存

原第19轮R723 closed ready为86,836 B，原R716 ready为97,718 B。继续把每轮完整历史反复内嵌到每个新ready会超过单件100,000 B，因此本包按明确授权作无损共享：

1. 原两个完整父ready原字保留，使用精确path/bytes/SHA256/blob引用其所有顶层与嵌套metadata；没有丢弃任何参数、来源、旧失败、未知peer或证明字段。
2. 一个新的完整 current parameter binding 文件保存第20轮完整科学argv、真实参数差异、当前所有来源/同级参数记录、完整外部未知peer对象、固定137源关系、完整R723物理scope、输出责任以及完整R716消费合同。
3. 新closed ready保留整个当前step；新R716 ready保留整个当前两step对象。任何selector、cleanup、output、parent_bundle及其它step字段均按原完整对象保留，只作明确的namespace/id/scope变化。
4. 新ready以完整字节身份引用上述共享绑定及完整父文件。历史仍是完整文件，而不是删去metadata后的摘要。

全部已有五个受支持peer CLI对仍在原157词科学参数内；其它完整外部peer来源/status对象单独保留。公开terminal不被当作空科学历史。新参数不声称已经消费或迁移任一未知peer的typed集合。

## 4. Closed一步：8 argv，77读数

closed source仍是完整1782，原8个argv词和全部原66+11个selector名称/表达式保持。相对第19轮R723 ready，只有输入geometry路径与新鲜输出路径中的runner namespace改变；script及所有数值参数不变。

输入：

{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-continuous-gram-curvature-support-v1/report.json

输出：

{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R723-directional-closed-phase-grip-v1/report.json

support-chunk-rows仍4096，仅影响包装。R723对完整mixed-pair法管、共同beta、方向支撑、曲率、同叶全三维D、全部帽和全相位的条件不变。R718继续使用真实marked sigma；unmarked管仍单独证明。原八角色仍false，不用新route伪造旧beta成功。原R650比较读数仍保留，同时新R723 reach读数明确分开。

## 5. R716两步：直接保留第20轮生产对象

已经完整读取第20轮原R716 ready，89,824 B：

SHA256 acdff6053f81e252bc82a83b5cdd082d24fb888b03e91905fc3ae6c7d7219e48；blob e8df07d79e268650ad82ce1bd586d34fa681490e。

其整个第一个step对象被原样放入本包，包括：

- 原45ca完整producer；
- 10个argv词；
- seconds=600、maximum-angle-blocks=0；
- 全部34个formal selector；
- 第20轮自己的normal-fee输入与矩输出；
- 完整原scope、id、parent_bundle及outputs。

本包没有复制第19轮矩生产步骤到第20轮。若这个完全相同的第20轮producer已排队或已真正返回，root应只接新consumer，不重复排生产步骤；完整两步仍交付以保全部参数。

消费者source仍是完整3c0d，8个argv词，原60+5共65个selector名称和表达式全部保持。只把原第19轮R723 consumer的moment输入、新鲜输出和可选R723主报告路径改为第20轮namespace。

矩输入：

{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-r716-complete-moment-integrals/report.json

新结果：

{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R723-r716-complete-centred-moments/report.json

可选closed输入就是第4节R723最终主报告。它仍需最终complete/status/全字节重核、唯一实际sidecar、完整point/model/target/snapshot/原normal绑定及独立unmarked外管。旧d0fe八角色分支保留为严格不同来源的旧分支，R723不会改写其条件。

全部十二矩、完整下半/平帽/p4实体、一般三相中心张量、真实32段signed half-turn之后才可用的补偿式、正总体积、非零中心不变量及R625/R716定量公式都没有变化。改变restoration damping不自动支付这些任何一项。

## 6. 全源和域没有缩小

科学driver10fa/reader8027/normal76185/packetc750/全部137角色原字共享。原当前M160/J923/N2048、冻结参考M160、完整Fejér dyadic chart与标量、1024闭角胞、所有922原径向单元及实际完整精确切分、32normal段和完整六jet不变。没有以mu001为理由改费用预算或工作域。

全部同场身份由将来真实报告重读，完整准确geometry和normal费用仍为必要数据；prepared input、历史模型或mutable progress不替代它们。本包没有添加新fixture、独立AST/编译、预跑或求解准入门。

## 7. 小完整再生器

reproduce_fixed_fejer_bhalf_mu001_R723_complete_parameters.mjs读取六份完整原JSON文件：

- 完整第19轮R723 closed参数；
- 完整第19轮R723 R716参数；
- 完整第20轮science参数；
- 完整第20轮科学参数总表；
- 完整第20轮moment/mesh参数总表；
- 完整第20轮原R716参数。

每份先核全bytes/SHA256/Git blob，再从完整step对象构造当前steps。当前科学157词与全部原对象逐项相等，实际mu/metric damping位置精确核对；closed与consumer只作完整namespace/id/scope变化，逆变换还原整个原step。第20轮producer逐对象原样保留。原完整metadata文件不变并继续精确引用，因而不需把它们重复塞入超过100KB的新文件。

输出三个完整JSON各有固定bytes/SHA/blob；V8实际进行了完整文本/JSON前后向构造和hash计算。没有执行科学或声称AST/compile。该再生器是可复现来源，不是新的admission步骤。

## 8. 完整新增文件

| 文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json | 27741 | fe5df0cee988753e710c1971fd7952fd1f8b465a58f004473d7310d228ce090b | cd97924e283d44b3662083c12e2588aef3c3d306 |
| fixed-fejer-meridian-batched-bhalf-mu001-first-R723-directional-closed-phase-grip-ready.json | 11483 | b027d255f244b311d6763b316238d93995d8688e9ff5b1f0d6277e22d0094fc5 | 518ee8bfd7c2142ee187bb4fd37ecbd90cf9f32f |
| fixed-fejer-meridian-batched-bhalf-mu001-first-R723-complete-R716-moment-ready.json | 15645 | 0ccb05e741eea9d33488e891e532728b9a8cd071e8a43f21b8d16c8fdff0ffa0 | 8385a3e2abb4ebd1963ebf26ccdd9db4af65209d |
| reproduce_fixed_fejer_bhalf_mu001_R723_complete_parameters.mjs | 50538 | 2c62c3e2b64cc85e28df75850ce88b0012606d67b796f0c9b11e46b8cb262cef | b027d1aa68b11191e7990a8b4764e85a93de8b33 |

说明和最终manifest另列其自身完整身份。所有新增单体均小于100,000 B，原完整文件不删、不缩参数、不改科学source。

## 9. 当前未付状态

本包不声称第20轮已经有完整场或连续费用，也不由第19轮有限几何改善预测第20轮结果。当前参考whole文件、完整working model、point、snapshot、final、normal/geometry、R723证书、矩报告及$\delta_E$都保持未填。

完整readies只是把真实返回后应消费的准确namespace和来源接好。所有原R723/R718/R716条件、source-specific绑定、latefailure失效规则和未知历史责任保持。
