# RET98：官方已取消的 run26 控制器输出完整保全

本批仅退出现树中 run26（46103106086/1）的两份控制器 Markdown 输出，共 58,669 字节。固定恢复提交为 `42f7da37489a2ef8953610eab0b1b2a7c9e6cbb9`。完整来源、恢复及删除清单见 `computations/terminal-run26-retention98-complete-provenance.json`（25688 字节，SHA256 `9e57758bcb21d2ffc8881e3cc1deee1ba662ff6b418bad7822ce35a167d6d401`，Git blob `788c8c58ec9520c63fb225d4f94e57c9a88fefe0`）。此交付只创建无引用完整 blobs；正式普通提交由 root 执行。

## 一、保留范围与全文恢复

原人工记录 `notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md` 的全部 91,974 字节继续原样留树：原叙述、数值表、初态、每次已记试探/拒绝/接受、时间顺序、官方全部 jobs/steps、末观察与未知项均不裁剪。该完整文件的 SHA256 为 `104c6ae58c14578ba0e73c1a616f34446c53c71073d9680db9b8a7bd3a58969f`，Git blob 为 `73f910f6206252a8b68d4f938d29db15fcbb0c88`。

旧分卷的两个完整 JSON 块分别是 maker 与 reference 的实际返回；旧索引第一完整 JSON 块是最后实际有界进度，第二块是原请求全文。台账对每块记录完整原文件身份、从 1 开始的块序号、原块字节及 SHA256。所有原 input_files、source、command、outputs、metrics、cleanup、summary_errors、missing_outputs、null 和原数字字面均属于该完整恢复范围，不以新摘要代替。完整原人工记录第 17 块保官方 jobs 全对象，第 18 块保最终输出身份。

准确恢复采用：

```sh
git show 42f7da37489a2ef8953610eab0b1b2a7c9e6cbb9:FULL_REPOSITORY_PATH > RESTORE_DESTINATION
```

对完整恢复文件核台账中的旧 bytes、SHA256 与 Git blob 后，旧 whole-hash 读者继续读取原字。历史链接使用固定提交；不将新台账或后来文件冒称旧全文。此处未声称能重演官方取消、时间戳或数值求解的每个工作字。

## 二、实际结果和未返回边界

两必要输入分别自然返回 0，耗时 6.187592959 秒与 578.258992014 秒，原 summary_errors 与 missing_outputs 均为空。完整 2218 叶标量的 accuracy_reached=false 照实保留；e640 是参数投影，d492 是实际标量身份，两者不混用。

科学最后完整当前点是 `c283e51d5b21f8f3e87671f9d92e1d2c34f24a667ebdfe6aff0945c991b9726c`，accepted=1，Phi=590.9577876003335，Gram=0.41647635913647313。六个带符号量为：

| 家族 | 实际值 |
|---|---:|
| reach | 0.013246488697677083 |
| body diameter | -0.04135006228341065 |
| distance plus | 0.1284444767098446 |
| distance minus | -3.0936218589052737 |
| cap diameter | -0.0669413866072589 |
| height floor | -1.0414354841839788 |

最大项仍是 distance plus，故未宣告可行。有限曲率 K=8.152275570136034，原 witness 的 cell/u/phi/branch/s 与 D_point_lower 均在台账及原全文保留；有限观察不是完整连续证书。

后续点 `0cb1e6ffa94fc057a40635613701e421d39e42d7298bd566a35b6cc2c7074cd3` 只已观察到 09:16:01.995670+00:00 的 trial-start 和随后 normal-chain-enter。其自身 Phi、Gram、geometry、是否接受、最终报告、全 13 成员 checkpoint、最终 typed/history 和 pure 返回均未知；不得把 c283 的数值搬给它。原 11 项 NoneType 观察错误随完整原进度块保全。

官方 job 140849792210 于 09:20:01Z 完成，结论 cancelled；科学 workflow step 于 09:19:56Z 取消。官方未提供取消原因，本批不归因于时间预算、数学失败或其它运行的故障。

## 三、完整 producer、资源和科学参数仍在

保留原完整 controller、geometry-location followups、请求、三步队列、workflow、maker/reference、137 角色绑定及全部 22 runtime 来源，完整 source delivery、parameter binding/delivery、science/pure ready。台账给 13 个当前 topic 保留 guard，外部 workflow 和历史 whole 记录单列，避免历史版本误作当前 guard。

完整队列仍含 6/26/157 个 argv 字与 14/62/458 个正式读数；科学 64 个实时字段和原所有 outputs、清理、peer 未完成责任、范数、阈值、预算都保留。原 7 字 pure 和 445 个正式读数仍是计划，未冒实际执行。R725 的固定 epsilon=1/8、paired halfwave、b/S=1/2、delta=1/32 和 M160/J923/N2048、全 32 normal 阶段不变，不混入 R726 球面插值场。

原控制器先恢复固定 60321451 历史 accepted099 输入，由完整 maker 只消费明确标量参数投影，再实际重建本 run 的固定输入和参考。旧历史 gzip 只记完整恢复身份，本批未读取其正文。原源码/参数可重做数学工作；旧公开输出的精确字节由固定 Git 恢复。

## 四、实施边界

本批不运行科学、AST、fixture、benchmark 或重放，不读取大于等于 100,000 字节或二进制正文，不修改任何 source/proof、实际 CLI 输入、request、queue、workflow、引用或活 run。Root 正式提交前仅对两删除文件和 13 当前保留文件核 fresh path/blob/size；这不是新的科学准入门。正式收益以完整 delivery 的全部新增字节计，不把整人工记录或原参数删除计作收益。
