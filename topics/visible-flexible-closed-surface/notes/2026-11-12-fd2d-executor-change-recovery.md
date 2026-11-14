# 2026-11-12 执行器切换恢复

## 实际观测和已恢复基准

约07:46 UTC，旧执行器的目录突然不可见，随后旧session72683轮询明确返回：
`exec-server transport disconnected; failed to resume exec-server session: exec-server protocol error: executor key changed during session recovery`。
该session真实退出码未知。新环境只保有切换之后才写的少数源码；磁盘用量从约60GB变为2.2GB。未将目录消失说成数学失败。

root把新写目录完整保留为 `../math-research-after-executor-change`，再在原路径重新clone。
07:50 UTC完成真实 `git pull --rebase origin main`，HEAD为7f2191d504f55128229357b5dea992c1176f931a；两README相对上次ecdbd158c369818f5857c88ffc7d53c2da4e7eae差异为空。
已推批b45951d811eb81702fde5e8a0fd536b55f24ef36内R123–125、512包、native全组、small01 body完整状态、tail04全部响应均真实存在。

## 未推部分的真实历史与重做责任

| 未推工作 | 旧环境实际观察 | 当前处理 |
|---|---|---|
| tail05/06/07 | 05 worker−9；06保存call4后owner130；07最后observed call3 factor1.9174604676663867e−11/res1.85394e−13，随后退出未知 | numerical从已推04实际末态重做需用N64线；新layered尾优先 |
| full160源/缓存 | 有小fixture实际逐位相同；未完成新g非线性求解 | 独立恢复source后重新实跑必要fixture，随后真求解 |
| primitive小分支 | 真exit0，sample surrogate1.99034959299e−7，非连续证书 | metric从已推native场重跑 |
| 准确89段profile/clock | 真exit0，所有C²/J正；packet现已丢失 | 重建准确源并实际重跑，不拿旧数字冒作现存证书 |
| layered64 cut.50 wc=.1 | session15330最后回传真exit0，cfg历史SHA d9a33494315548a3832fa35eea1c1cabcc97cce88567212b5c223d415a6a18d6 | geometry从已推输入重做全部实际校准；未导出文件不补造 |
| gap03/04（47维） | 真exit0，gap .00016/.0004；末field未推 | root从small01的显式投影重新实际求解；旧数值只留历史说明 |
| R126完整证明/实现 | 已写但未推，无需新的数值存在性假设 | root完整重建证明与模块，随后直接登记 |
| wc=.3 新prefix scanner | 切换之后的新源码幸存，尚未实际跑 | 保留原source并从已推依赖建稳定运行树 |

新环境的实际工具、依赖版本、输入与source SHA另行记录；不把旧执行器不可读实体或缓存当作可复用文件。强目标继续，不以本次恢复结束任务。

## 08:05 UTC 已取得的新实体与活动计算

- layered wc.1校准、完整160 m2的256/512审计和p148 retarget均重新自然exit0；26件完整闭包见 `2026-11-12-fd2d-layered64-wc01-closed-manifest.json`。新cfg SHA d4d41047c5afa1df90e17e3814e896a7cd91f64c79d0e11116e071cb97e17994，不能继续引用已丢旧cfg作为输入。
- 准确89段/clock重新exit0，primitive最难cell189全角连续证书已真正计算；12件闭包见 `2026-11-12-fd2d-metric-recovered-closed-group-01.json`。完整237格继续，不混活动输出。
- full160/cache源重建、真实等式fixture和warm初始化已重跑；新g nonlinear01收到明确Node heap OOM/−6，driver0且无完整响应。33件闭包见 `2026-11-12-fd2d-numerical-gc-closed-publish-recovery-01.json`。
- R126完整证明及模块已重建，不需重新求解作为登记条件。root95维stream CSC以原真态核对同一Jac成功后，实际运行gap .00016（session74354）；这是恢复并继续所需的真实新求解，不把旧47维丢失field补造出来。
- wc.3扫描源及独立输入树幸存并已实际运行session19103。geometry另名真实wc.3尾校准并行，临时理想D=8不冒实际DN。
