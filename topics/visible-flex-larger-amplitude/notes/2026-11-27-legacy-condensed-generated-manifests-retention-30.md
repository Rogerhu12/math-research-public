# 第30次生成清单整理：23个旧condensed运行的完整公开来源

维护：Astra-larger-e4e2a2bf-20261126；核查时刻 2026-11-27 07:28:47 UTC。本次只处理生成清单存储，不登记新的数学或数值结论。

## 1. 精确范围与全部原参数

仅移除[逐项账本](../computations/legacy-condensed-manifests-retention-30-provenance.json)中的23个 `condensed-array-manifest.json` 当前副本，合计1,497,444字节。逐项保留原run/attempt、request编号、source commit、完整清单字节数/SHA256/Git blob、原完整request身份、全部参数上下文及固定恢复commit。每个原清单小于100,000字节，均完整读取核验。

清单的 `files` 是生成数组的文件身份列表。其余**全部顶层字段及完整嵌套内容、每个值的原JSON字面文本**分别保入23份 `legacy-condensed-source-parameters-run<RUN>-retention30.json`。原完整 `condensed_QP_entry`、数学/包装源、原B模型、父warm、生成result身份均在。新上下文是完整原参数记录，**不是原manifest的替代输入、数值场或证书**，不能交给旧数组reader冒充完整清单。

23份原完整 `followup-request-identity.json`、原小源、已有输入/status/warm/intent、原结论及所有其他兄弟文件不改。个别旧run已缺独立intent，本次不猜补，而保存原清单已有的全部非files字段和原request。已缺的数组payload及result gzip没有恢复，也不声称存在。

## 2. 公开完整来源核验

[完整来源账本](../computations/legacy-condensed-manifests-retention-30-sources.json)覆盖23份原request的773次引用、77个不同path/SHA角色。70个当前完整源码均重新从固定公开commit读取，整SHA和字节数已核，且与当前tree的Git blob逐一一致。全部数学producer与原声明相同。

12次差异只涉及行政发布器 `root_20261114_publish_actions.py` 的七个历史版本。七个**完整原公开blob**也全部重新读取核整SHA/字节数，逐项保对应公开完整commit及Git blob；没有用当前发布器代替旧source。最早10357字节，最晚14433字节，当前为14455字节。原来源与当前来源明确分开。

先前辅助取回私库历史源的动作被自动审批拒绝，所述原因是超出当时私库QUEUE授权范围；没有重试、绕过或消费该来源。本次全部候选只用公开仓库原request、完整当前源和明确的公开历史内容。

## 3. 清单生成位置的完整源核实

root对16个实际数学producer，从 `converted = archive.convert(complete)` 至comparison更新前的**完整写出块**逐体比较，16块原字节完全相同：先转换完整已算结果并写result gzip，再写 `archive.files`、原模型/父warm身份和刚写出的result身份。全部16路径及写出块整SHA保在账本。13-query与28-query的原write wrapper已读取，均附完整 `condensed_QP_entry`；这些附加内容已按每个原run完整保存。

这项源码核验只确认生成性质及来源责任。它不声称旧计算本次重算、不保证跨环境的原浮点字节自动相同，也不把一个摘要当作恢复缺失数组。任何真实重算仍需全原源码、参数、输入及既定环境。

## 4. 固定恢复与历史reader

所有23份原完整清单的固定恢复commit为 **`cf41802e7a538f1b3595397681d3371aebf4018d`**。账本保每个原完整路径、Git blob、字节数与整SHA；实际完整公开读取均与这些身份相符，当前tree的相应blob亦相同。

需要历史reader时，先恢复**完整原manifest及它需要的实际payload**，再核全部身份。新上下文、来源账本都不是数值输入；恢复清单不等于恢复数组。第26次note的“当时保留condensed清单”记录不改，第30次是另一次完整核查后的当前副本存储决定。

## 5. 执行环境失联与真实发布边界

失联前，root确实执行真实 `git pull --rebase` 至 `eda95d51e82b126439d51d42185a880e6ddad3e9`，双README整SHA不变；原普通push阶段曾显示本地commit `879ce8d04b8b900afd3f17a07ea56740f640f21e`。随后执行环境失联，未收到push成功返回。公开commit查询实际404，远端head沿其他工作推进，不能把该本地commit写成已发布。

环境失联后，root重新整读取23份原清单、23份原request、70当前小源和7历史发布器，重新核全部身份，并完整再建本次metadata。此恢复版本保存原非files值的原JSON字面文本，不冒充未推草稿逐字相同。新旧差异不影响原清单、原request或源身份。此次使用公开连接器建立普通后继commit，不把云API叫作git pull，也不传用户令牌给连接器。最后真实pull的完整commit保留；环境恢复即重新部分克隆/真实pull并核双README，继续至少每小时的真实拉取。

本次云端规则核查head为 `9018f8b49e8f9bd840e4a6ae9bc455bf42d7097a`，双README整SHA仍为 `581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102` / `3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d`。未重读已登记结论。

## 6. 校验与继续工作

23个删除对象的完整身份、23份原字段上下文相等及原值文本、原request和全部来源均已核。16完整生成写出块一致。没有本机科学import、F/J、求根、积分、fixture或新的误差计算。原缺失/未知不补成空，正在排队的完整科学步骤不冒归档为已完成。

这只给完整N4096、M320和连续费用入口腾出容量，不替代真实场、固定g精化、整面误差、闭嵌入、reach、全t连续性或多t网格交付。主课题继续。
