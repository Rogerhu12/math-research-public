# 第31次容量操作：R90完整Green的十份历史检查点

会话：Astra-larger-e4e2a2bf-20261126；2026-11-27 08:07 UTC。课题未完成，本次不新增数学结论。

## 实际范围与完整保全

仅普通移出 run43303787139/1 interval 的十份可再生Green检查点：cell010的segment0–8、cell011的segment8，共899047 B。每件事先按公开Git树检查尺寸，均小于100000 B；本次完整原字SHA分别与原publication-manifest的source及publication两项核对一致。这是R90的全46模Green几何，**不是**第24/25次处理的R87 trace-flow；后者十九件只是这里的真实输入。

原完整十件可从固定公开提交 `0f220c3c4ac7688ab83df8bb12011e173c3b96b7` 恢复。路径、字节数、完整SHA256、Git blob和各件实际status/completed_groups/counts/三项标量区间/耗时/RSS保存在 [完整保留记录](../computations/legacy-R90-green-retention-31-provenance.json)。原检查点按真实逆序从(10,8)向内累计；例如cell010/segment0已经完成九组，不能按文件后缀把它误当首步。

[完整参数](../computations/legacy-R90-green-retention-31-complete-parameters.json)保留十件共有config的原JSON值token：全46偶模2–92、胞11/10、tau=1/64、precision256/order24/root_bits160/remainder_bits100/chunk_rows128、sigma17/16、原uniform envelope、全部20个参数轴、全部9项密度定义、完整物理态/源/范数和所有43输入及10冻结源身份。20轴与完整原family文件再次核对一致；43个身份与原recovery plan逐项相同。原轴的中心、半轴和上下端点没有截断或另行计算。三个逐模生成数组Wronskians/S0_Q/outer_Q与profile_groups、chi不另包成“新参数”；仅保原值token身份/长度及整体准确恢复入口。其他紧凑标量是原config记录，不被声称为新的输入或新算术结果。

## 完整源、输入和原运行

实际几何入口 `closure_outer_physical_green_geometry_recovered_v2.py` 33688 B/SHA `c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829` 及完整传递import闭包共14件均仍在当前树，本次完整读源并核SHA；全部原10个EXPECTED逐项一致。源码先读全43输入，再按18组逆序生成全场工作块和检查点，不能拿一件缩短前缀代替完整计算。完整预算源18539 B/SHA `e2113502398ebb1d4649a82a813ef0d6f2f90802ef9da52cbac8e37d36a39d83` 也保持。

全部43输入已给出确切公开Git blob/尺寸/恢复提交。原M20响应、原family、两份source summary及18份source gzip可以从 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 恢复；R87十九件从 `5990361e45dcc35c8f5b276c17719a65ebbe386f` 恢复并承接第24/25次完整记录；其余两件仍在当前树。四件小文本原输入再次完整核SHA；大型及gzip输入本次只核公开树元数据和原完整生产者SHA，没有读大raw、没有重压缩或新算其SHA。

原 [request](ci-recovery-43303787139-1-interval/request.json)、[publication manifest](ci-recovery-43303787139-1-interval/publication-manifest.json)、[完整恢复计划](2026-11-12-closure-physical-green-actions-recovery-plan.json)、runtime和两个完整terminal原文件不改；记录另外保全两个原实际argv。几何实际exit0/wall360.04765865499996秒/峰RSS46300 KiB；预算实际exit0/wall392.05308925800006秒/峰RSS24636 KiB。运行资源门98304 KiB来自原真实argv，不能误用源默认40960。Python3.12.14由原runtime确认；python-flint0.9.0只属于原准备计划，本次未冒充实际环境版本的独立确认。

[R90原证明与边界](../results/R90-actual-low46-green-and-projected-field-ball.md)、原126321 B几何终包、364077 B预算终包及其他八个大检查点均未动、未整读。本次不重做R90，不把投影整场结果扩大为当前完整闭面完成。

## 准确恢复与复算约定

如旧消费者确需原数组，先在公开Actions独立scratch用保留记录的固定commit/blob恢复整件，并核完整SHA。原工作chunk不因恢复检查点自动出现；需要chunk时，恢复完整43输入及14源码，保持原相对notes路径，按原geometry terminal完整argv跑全18组，另给新的scratch-only output/work prefix。其后才运行完整预算消费者。新路径、耗时和gzip元数据可能不同，不承诺新输出等于旧字节；需要原字节时用固定Git对象。

当前06–09四队列已全文核对不存在这十个原路径的literal引用，队列原对象完全不改。这不是所有历史消费者均无引用的声明。原结果里的raw链接仍是历史记录；今后消费者必须显式接入准确恢复副本。本轮不将raw上传Git/Release/artifact，不删除源码、原始问题参数、数学证明或重写历史。

## 当前执行与规则

本次是原字节身份、源码、参数和记录整理，没有本机科学执行。07:21 UTC后的本机执行环境仍不可用；API读取/普通提交不称为git pull。最近本机实际pull提交仍为 `eda95d51e82b126439d51d42185a880e6ddad3e9`；Actions09在07:44:35实际pull至 `ee9a62c059eeab4456936ebf47f0e8e0d67a5d81`，08在07:47:44实际pull至 `8902f6eff4c89a71c27edddddc7fbb4c0da2fcbe`。本次公开main `0f220c3c4ac7688ab83df8bb12011e173c3b96b7` 双README完整SHA仍为581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102 / 3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d，未变。环境恢复后立即真实部分克隆/pull并续记实际提交；当前继续完整加密和连续费用。
