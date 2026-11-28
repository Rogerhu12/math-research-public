# R87 严格 λ0：实际 812 节点的导数方法交接

**性质：工程观察，不是数学失败或接受场。** 原 $\lambda=0/M8$ 求解保持 `tol=2e-7` 及原全部门，在 765 节点网格上实际接受过 $\alpha=1/8192$ 和 $1/131072$ 两个 Newton 步，随后又继续到 **812 节点**。因此不能把它描述为已经停止加密，也没有读到最终 RMS、physical 导出或 metric 返回。

真实七节点参数诊断指出，该 λ0 分支原本没有安装正 λ 的材料参数解析 Jacobian；高支撑模态的有限差分物理扰动约为 $2\times10^{-14}$。下一入口将针对这个具体数值问题使用同一原模型的支撑参数解析导数，原 δ 有限差分、完整方程和接受门保持。当前不把该诊断夸成整个 BVP 的数学失败。

第一次控制前检查仍要求旧 765 维度，因实际网格已变 812 而拒绝；**没有发送信号**。随后按真实 metadata 核验完整 $25\times812$ 状态、8 参数、7 个尺度和全部节点，保存第 10 个完整 nodal checkpoint，SHA `a9104450972ccd21b78d92f399e1092bca3db6471f16b50499e5eb5b89b24861`。此前 765 节点的最后接受迭代 `e13909bf…` 也保留；两者都不是整体接受解。

第二次核验通过后，对唯一自有 TTY 81483 发出 Control-C。工具真实返回 exit 1，随后再次查询为 `Unknown process id 81483`，所以该 **工具会话已终结**。但 observer 没有留下 `finally`/owned-cleanup 回执，其最后 JSON 仍是原 live sample；**内部 child 的退出码和 cleanup 没有观测到，不能补造为 −15、−9 或已观测的完整回收**。没有跨隔离的 PID 名字空间猜测或发送信号。完整快照和小回执路径、SHA 在[同名记录](2026-11-28-design-r87-lambda0-fd-method-handoff.json)。

独立 `observe_owned_original_command_v3.py` 已 compile/help 通过。它新增明确 scope/outdir/nonce 匹配的 `--termination-request`：请求在原 owner 的循环内部读取，调用已有身份绑定的 `cleanup()`，观察真实 join 后才正常 exit 4。原 owned-session 实现不改，也不以这个准备入口倒填旧会话缺失的回执。本条写入时新 BVP 尚未启动；后继只从上述完整 812 节点输入继续一套求解，原旧字段与所有检查点保留。
