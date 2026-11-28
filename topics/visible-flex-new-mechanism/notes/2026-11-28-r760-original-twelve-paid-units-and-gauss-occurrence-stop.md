# R760：原12个成功付费单元保全于第一真实Gauss重号检查

会话 Astra-new-mechanism-8cdb3418-20261128；2026-11-28 19:51:05 UTC。整份作业自然完成及工件上传完成后，只读一次原日志；没有读运行中日志或重跑原场。

[run46181796301](https://github.com/Rogerhu12/math-research-public/actions/runs/46181796301) / job141092792865 / head **d2414100f68ed127210d746d59d064a0c5278eb0**。2026-11-28 **19:33:31至19:39:01 UTC**，job=failure，原上传success。request SHA **15c5bab056bd853d984acdff3ddabaf77e60a6e549729b6233dd676d8fb08f1b**。科学输入身份 **19e2aa6665a8843ac23a5c05615a0674985fab2f7aca8d420a4330fb830d1404**。

## 真实失败点与已经付完的部分

原错误为 `ValueError('R760 original and refined material quadratures must be strictly increasing')`。原下一单位是 `r750_true_ray_kernel`，key=(phase0, degree3, train, level1, order10, 359角标SHA5686fbcfa672719200f0bd7b680b08a54bad52dca9b932c1959e767e911618da, batch0:8)。失败在初候选field→relative position→kernel→matched_rows；还未完成第一相位或任何GN算子。

已接纳0、全J0、finished_phase_records0，phase_index0/iteration0/backtrack0，retained_paired_field=null。这不是非零三矩场失败，也未提供有限网拟合结果。已完整付费 **12单位**：两native_frame、两native_nodes、一actual_release_probe、一真实ray_rule、一完整terminal-moment profile、一真实curl_rows、两完整native_seed_jets、两phase_parameter。所有单位均在原20成员工件；原失败kernel没有成功NPZ，正是恢复后的未付入口。

首科学allocation wall **25.82385439899997秒**，归档/原输入读取 **12.440591074999816秒**。原类账如下，saved与failed都保留，不与wall再相加：

| 单位 | saved | failed | 科学秒 | 归档秒 |
|---|---:|---:|---:|---:|
| native_frame | 2 | 0 | 11.52230270800004 | 7.2122713599999315 |
| native_nodes | 2 | 0 | 0.001886035999973501 | 0.0014802579999582122 |
| r750_actual_release_probe | 1 | 0 | 0.015171150000014677 | 0.0011249570000018139 |
| r750_ray_rule | 1 | 0 | 0.0018734819999508545 | 0.0012083419999839862 |
| r750_true_ray_kernel | 0 | 1 | 0.0012885320000464162 | 0.008116078999989895 |
| r760_actual_full_terminal_moments | 1 | 0 | 0.022813621000011608 | 0.0011793890000149077 |
| r760_curl_rows | 1 | 0 | 0.12769144600002846 | 0.013162265999994816 |
| r760_full_native_seed_jets | 2 | 0 | 1.6581655890000206 | 0.0013131590000057258 |
| r760_meridian_phase_parameter | 2 | 0 | 0.020729104999986703 | 0.0009735249999494044 |

原R750采用source_build1、native_nodes2、native_frame2、phase_pulses1、curl1、ray_rule1及原ray_kernel1，未重付原9步/17J/17010列和旧536ray核等账。

## 已完成的原数据运输与规则同步

前置行政阶段实际接收原R750 **7114742915B**，107区段、253.733495106秒，核完整ZIP SHA49762b330eaf3dc254caf9002b50ab1b730b85ba0aea7c324f37911b8001c38e及强ETag，单次取得地址，整体行政253.734030182秒，新科学0、旧日志0。开始时runner实际free90106724352B；本次没有签名地址中途失效。

科学前真正公开pull在19:38:13.809321Z至 **bcc3f65811b8c90d9eeddd5d0e3b7830584580c9**，两README差异为空；私pull19:38:18.826409Z至 **5a21729f196fca00220aa3051f80216648064d78**，根blob和本会话QUEUE均符合。两个实际pull记录保留在原日志。账户凭据在新科学前清除。

## 原工件、原字节及最小后继

artifact **15277979068**，`visible-r760-paid-46181796301-1`，**57530937B**，SHA **4b6e60590fcd6612cbcf05ab95f27df2f839a803392aec258b574209847370fc**，2026-12-28 **19:38:55 UTC**到期。根用官方工件读取一次后纯I/O下载、全SHA与四原文校验，1.330640172秒，新科学0；原FINAL12454B/SHA d5641d85d66d44a55c95dce184819e77a522a4d553b171e74c2e814088eb2baf，工件terminal12455B/SHA9d9315be84e0da3866fe4380d0050016f921fc923f03314cec5c618cfefe7635。input4567B、continuation1813B、source3780B及其SHA见[完整原收据](../computations/r760-first-original-checkpoint-20261128.json)。

静态定位：真实cuts严格升序，不能推出浮点映射后的所有Gauss半径严格递增。极短真实区间的不同点可舍入成同一半径；它们仍是不同的正权积分项。原matched_rows不但不应拒绝这种情况，searchsorted也不能重复采用同一个旧权重贡献。

后继仅加一个新软件身份的外包层，不改原九个科学模块。首先按两真实面板端点与面板内Gauss序号一对一匹配，再对相同(r,weight)的剩余重号保重匹配；只有几何值可以对同r多次引用，原积分权贡献只采用一次。每个数值.npy字节准确继承，NPZ中的科学semantic身份升级有明示逐件SHA映射和全部原metadata备份；不是伪称源哈希未改。新包层必须核全部12成功单位与唯一失败记录，原失败费用单独存，之后从未完成的首积分核继续。原359/各角测点不减少，423/1752全列不缩减。工作/独立/连续资格及完整课题完成标准仍未达。
