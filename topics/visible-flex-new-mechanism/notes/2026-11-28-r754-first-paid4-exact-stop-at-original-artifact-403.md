# R754：首轮4接纳和7全算子保留；父工件HTTP403处准确续接

会话 Astra-new-mechanism-8cdb3418-20261128；2026-11-28 19:26:17 UTC。完整作业及上传自然结束后只读一次原日志。本记录不把基础设施失败改写为科学成功，也不重做失败前已付场或矩阵。

## 原运行、原失败及其准确位置

[run46179020787](https://github.com/Rogerhu12/math-research-public/actions/runs/46179020787) / job141084139107，head **551fdb544a4fbde3409e663e7d458ad67c115c6c**。2026-11-28 **19:02:08至19:14:28 UTC**自然完成，作业conclusion=failure，上传步骤success。request SHA256 **dc5aa8c364e9f14e205973913e91f9f5b6552a7ec4b5cae94d99f1e50122e36d**。

原error严格为 `OSError('signed artifact range failed: 403')`。19:13:08失败于下个phase .02的setup，调用链为phase_pulses→Paid.acquire→Parent.receipt→原ZIP.open→RangedArchive.fetch。这是同一已验证父工件的后续签名读地址返回403；首launcher只交一个地址并在科学前移除了账户凭据，科学阶段不能续取地址。不是新三curl、J或完整谱运算抛出的错误。

原输入身份 **cbe3599a59cc97a6b6d4238d909ab0602926cc84d4f0f5c627fa928cefbc1786**。原4接纳、3条完成记录，next为 **phase_index3 / .02 / iteration0 / backtrack0**，active_operation=null。保留的成对场仍是.008/degree5/iteration8，不把它误当下一相位场。只更换科学前的运输方式；全部R754科学源码、R746父收据、原level1和iterations8不变，按原continuation恢复。

## 两个真实非零场仍未通过

| 相位 | 度 | 工作网绝对curl峰 | 独立网绝对curl峰 | finite_fit |
|---:|---:|---:|---:|---|
| 0.0 | 3 | 0.0 | 0.0 | true |
| 0.002 | 5 | 0.2163651439206715 | 0.2163651439206715 | false |
| 0.008 | 5 | 0.8668306137727922 | 0.8668306137727922 | false |

.002 q1371的SHA **52e3009ec08e1f26eca70b0d2fd5a357026827935549431e9aaec1cfabd07c76**；.008 q1371的SHA **8263a5f5775094a6b70d6580701c6cb654feb7e9c7d6e4edf6358e2bec7214b6**。这两个值虽小于R746原两相位的63.735和130.450，仍是实际未拟合场；旋度不是metric误差，工作/独立两网相同峰也不证明全连续控制。非零物理资格明确deferred/null；只原零场资格精确采用，完整全壳资格未授。

首轮共 **7个完整J**（degree3一个、degree5六个），真实330/1371列，共 **8556物理列**；7次完整TSQR/SVD、152叶、155归并，10个原Householder子树准确运输。32个候选指标单位、284个原点真实新场和284个witness真实场全保留。不能因transport失败再跑首轮三相位。

## 全费用及原采用

本allocation wall **625.5517658140001秒**，归档/原输入运输计 **483.2021830150002秒**。以下是原cost_summary的全部类账；不与wall重复相加。

| 原单位类型 | 已保存 | 科学秒 | 归档秒 |
|---|---:|---:|---:|
| forced_sleeve | 1 | 1.498800000376832e-05 | 2.138006367000031 |
| full_sparse_jacobian | 7 | 0.1538156440001046 | 13.606450261999896 |
| qualification | 1 | 8.695999997598847e-05 | 10.312174603000017 |
| r754_additional_native_frame | 6 | 0.26020918499995105 | 0.12565085699986867 |
| r754_angular_all | 13 | 3.512623327000057 | 1.1877598760000296 |
| r754_appended_euler_columns | 14 | 0.222910402000025 | 0.2822618889997557 |
| r754_augmented_checks | 14 | 0.3128435849999107 | 0.006628134000209229 |
| r754_augmented_row_group | 14 | 5.314000020462117e-06 | 13.614886179000024 |
| r754_deferred_physical | 2 | 0.00019103900001482543 | 0.013502894000055221 |
| r754_exact_witness | 3 | 0.030434959999979583 | 0.001974236999956247 |
| r754_initial_candidate_score | 32 | 0.13815368399991712 | 0.02075210900000002 |
| r754_left_meridian_columns | 14 | 6.909783337999869 | 0.2575466530000483 |
| r754_old_columns_unpaid | 13 | 7.133470271000277 | 12.78593340700013 |
| r754_original_node_field | 284 | 52.18614163900102 | 25.165962971000226 |
| r754_parent_frame_extension | 6 | 1.313668470999957 | 0.6839533949999179 |
| r754_same_true_core_seed | 6 | 0.00010603000004039131 | 4.29844535899997 |
| r754_transported_householder | 10 | 0.008617557999940573 | 16.784983941999997 |
| r754_witness_field | 284 | 0.6373824479993573 | 0.1748282559995289 |
| sampled_all_pose_hull | 1 | 0.10363934099999028 | 0.003311109999998507 |
| sampled_shell_hull | 1 | 9.998999985327828e-06 | 0.004299411000005193 |
| tsqr_leaf | 152 | 40.61156091399971 | 8.618911982000299 |
| tsqr_merge | 155 | 17.048929585000423 | 10.206776719999795 |
| tsqr_scale | 7 | 0.5498459339999329 | 0.0067414770001335 |
| tsqr_svd | 7 | 7.741594452000072 | 13.351287397000078 |

原R746采用计数为curl10、forced_sleeve1、full_sparse_jacobian1、native_frame6、native_nodes6、nine_angular_derivatives1、phase_pulses3、phase_ring3、qualification1、r746_zero_core_seed6、sampled_shell_hull1、source_build1、TSQR叶4/归并6/scale1。它们的原费用不注销；新类中的`r754_old_columns_unpaid`仅指原从未付过的改变行，而非删除原列。所有新类failed=0，失败在下一个原件读取，完整next与所有成功单位已上传。

## 原工件与恢复

原artifact **15277750701**，`visible-r754-paid-46179020787-1`，**2793862555B**，官方完整ZIP SHA256 **86ff4bdc73479c1e2bfcbd0373a997dedf313d90614ac3b0f69a6291146858ff**，到期2026-12-28 **19:13:08 UTC**。原日志FINAL **133305B / SHA b1ff7ccbb4fd88b01b3498dd5fa6e94af938f8108ff40797ee3419fa3604e41f**；原工件terminal预期为同字面加换行，需在恢复时按 2b36e2e73a85913ecc755262be51ccb6e4118d6728f049b111ab0034725f27f1 核验。

根已保存原FINAL。首次本地纯元数据接收因未带该接收器所需GH_TOKEN而401；改正确环境名后，GitHub REST明确返回账户API rate limit exceeded/remaining0。均未运行科学、未替换输入、不继续密集重试；原工件ID/官方SHA与自然完成事实已由完成元数据绑定。采用[不可变恢复收据](../computations/r754-original-first-failed-checkpoint-20261128.json)，在下一公开Actions作业的行政阶段接收并全SHA核整个原R746 ZIP和这份原失败checkpoint，随后删除恢复用ZIP节省空间，按每个原成员恢复全部已付数据。新的科学入口使用既有`--parent-zip`；同一父收据原样进入身份，科学前账户凭据照原driver移除。

原单的“只惰性206读取、不全量下载”是已被本次403否定的运输设计，不是课题数学限制。新的完整预接收只在公开Actions执行，按实际磁盘容量检查后开始；不会在本地下载这两个多GB工件，也不会修改原科学源码绕过输入身份。下一步仍是尚未付的.02，不是另起同一首轮。课题完成标准保持未达，继续完整固定g的实际场与连续资格工作。
