# R133：实际完整 5970 格连续局部投影证书

2026-11-14。状态：全部原格和接口已实际验证；本结论为完整局部证书。

## 原始公开过程与对象

公开 [Actions 43594139132](https://github.com/Rogerhu12/math-research-public/actions/runs/43594139132)
已 success。16 个互斥分段全部成功，最后完整消费在 13:52 UTC 完成。
科学输入依旧为固定原物理 eta0、原 nu、零 affine offset 和同一个修复算子定义；
零 offset 不是物理 eta=0。

原 5970 格覆盖精确区间 [0,9/10]。已成功的四个 pilot
0、76、3300、5969 使用原字节，其余 5966 格新验证。
原 916MB frame proposal、成功 pilot 和已完成分段均未重跑。
完整 final native 的每个局部投影、anchor 和接口被恰好消费一次。

| 原件 | 完整 SHA256 |
|---|---|
| 完整局部 native | `3460a4b5636bf6a3d9c160f6141ab5153fc5fc705ca79000c5f10370a978cb69` |
| 真实 weighted 两端 native | `56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25` |
| 完整 cover summary | `59cfa10e56e3cc312b411101749c729eb06367564c6215c89503d320510dccdc` |
| 仓库 final process snapshot | `d0ff157c8fe313fdf2ce8dd66f7a718512adcd3d70230f8010075e958a616633` |
| 原 artifact final process | `16608b57571d17a427857bcfe0127186589b3f79e93d89a7e423ac48a2740af9` |
| 原 88 输入 manifest | `394379df4a2588ad53a85ed91438874a34f30473a746b85cd8db3e83edfcdbf5` |
| 原分段及完整 consumer | `3d4628235a6d48046ac2e17af75cf70ea7bcadf6d5e6856a327426faebfa84fa` |

两个 process SHA 对应不同真实 checkpoint 字节。仓库 snapshot
增加出版/同步信息；原 artifact process 由后续 Green 原样消费，
不得把任一 expected SHA 改成另一份来消除差异。

## 完整覆盖的证据

完整结果位于
[final process](../notes/regular_cut_validator_ci/run-43594139132-1-projectors-complete-5970-consumer/process.json)
和
[覆盖 summary](../notes/regular_cut_validator_ci/run-43594139132-1-projectors-complete-5970-consumer/evidence/complete-5970-cover-summary.json)。

summary 原样记录 22 个实际原文件及其 SHA、各半开 index 区间。
其中四个单格为原 pilot，18 个新增文件因分段跨 pilot 位置而拆开；
这个文件数量不等于 job 数量。所有 index 唯一，合并为 0..5969。
3,876,042 字节 native 完整保存，没有为了减小体积去掉原格或接口。

final process 的真实 phase 是 finish。通用初始化字段 mode 仍为 prepare，
children 为空是因为 final 只消费各真实分段，不代表没运行数值验证。
应结合 phase、完整分段过程及 complete_original_5970_cells_claimed 判读。
它明确保留 global_continuous_inverse_proved=false。

## 同步与下一消费者

final runner 两次实际 pull/rebase 后都核对两 README 的真实差异为空：
33a56d8b71199465307642e891660f94e877c8b8、
a77d37253a5daebd0b43214d8f6d831c802be5b3。
根规则亲读提交仍为 ee26c0a65a2e63c15f2ccfba6714181584416542。
各长段另保其每十分钟实际同步记录。

这条结论关闭完整局部覆盖，后续完整有符号 Green 作业已自动触发。
有限维全局逆仍需全 suffix 无 pole、全部混合 jump、最后 0+→0−
腰接口和真边界闭合；无限 high 反馈、真正参数响应及 Schur 另付。
