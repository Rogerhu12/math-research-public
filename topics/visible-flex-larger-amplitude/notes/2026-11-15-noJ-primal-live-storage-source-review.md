# noJ-primal live 字节存储草稿：独立源码核对

类型：工程源码审阅；作者：ChatGPT / amplitude；日期：2026-11-15 UTC。

完整读了 `native_closed_iteration_bytes.mjs`、`native_live_artifact_supervisor.mjs`、`native_restore_artifact_batches.mjs` 及其接口。**未发现确定的字段、关闭边界、SDK参数或删除顺序阻断。** 此结论只针对[回执](2026-11-15-native-live-storage-source-review-receipt.json)锁定的三个草稿，不是已完成上传或恢复的运行结果。

## 关闭边界和原调用

`discoverClosed`读取原JSONL中已经完整换行的成功项；它核returned-correction、qr-exit、call/iteration/sequence、snapshot/result/current-state以及原descriptor。不是用mtime稳定或“QR某个阶段完成”代替关闭。

冻结hook `0e802785…` 的 `currentCorrection` 在同步子进程退出后执行 `checkedCurrentDirection`，恢复完整delta到独立内存，核当前state/target/scales未变，写returned-correction并追加完整JSONL，最后返回内存delta。后续十次原试探仍使用内存数据。`finishRequestContext`、`finishAll`使用已保存的ctx记录，不再次打开旧因子/J载荷。因此该草稿观察的边界与冻结client `7aa2aba1…` 一致；它仍不能宣称这一轮native线搜索已经接受。

## 保全和删除

相对路径检查拒绝绝对路径、点段、反斜线、NUL和symlink；源文件只接受普通文件并在流式hash前后核inode/size/mtime。批次枚举关闭目录全部普通文件，使用同文件系统硬链接且不chmod共享inode。每批另保原spec/intents/request和原完整JSONL行的base64。

supervisor先Finalize取得真实artifact id/digest，再下载并检查完整ZIP digest与全部成员路径集合、bytes、SHA。核过的manifest/receipt/catalog原子写入并fsync后，才重新核源并unlink明确的 `snapshot/large-arrays/` 或 `qr/large-arrays/` 文件；原科学JSON/descriptor不改。staging链接和下载副本随后移除。未验证或未关闭目录不进入该删除流程。

storage错误独立记录，不调用kill/pause/restart或修改科学参数；原子命令exit/signal与存储exit86分开。实际系统取消行为尚没有运行回执，接口没有提前声称验证过。

## SDK和凭据接口

亲核了已保存的7份官方源码的size/SHA，对应 [actions/toolkit固定提交](https://github.com/actions/toolkit/tree/c40bccc9c31c29df15c93abbea5b18bb474a4add/packages/artifact) 的 `@actions/artifact` 2.3.2。官方upload返回裸hex `digest` 和真实id；官方download将收到的流式SHA表示成 `sha256:<hex>` 并返回 `digestMismatch`。草稿的参数与显式false检查匹配这两个实现。

运行时要求真实完整lock receipt及包2.3.2/version/integrity，并在接口中明确这不代替受控 `npm ci` 的全依赖构建。子链argv/cwd保持，`shell:false`；四个artifact runtime凭据从child环境删去，原规则同步需要的GH_TOKEN/GITHUB_TOKEN保留。新token不序列化，工程error内容作已知token和URL清理。未安装或执行SDK，没有网络上传/下载。

## Restore及部署范围

restore锁catalog原SHA，按每批原artifact和manifestSHA重下载；核完整成员后才复制，存在目标必须逐字相同，不能覆盖不同内容；partial批次不静默跳过。

以下两项属于未来workflow接线范围，不应由本次源码核对替代：

- 普通最终artifact必须保storage catalog、verified/eviction receipts及active/failed/partial原件；三份草稿本身没有提供这个workflow。
- restore恢复的是已封存members。仍在追加的call JSONL和调用/全局最终summary由普通最终artifact另行保留；batch manifest中的原行base64不在当前restore中重建为整本JSONL。完整live目录需合并两类原件后再交旧reader。

本次没有导入存储或科学模块，没有执行fixture、子命令、SDK或数学计算，也没有改这三份草稿、冻结科学源或Git。无新增数学门；实际上传、取消及还原的工程证据留待真实接线产生。
