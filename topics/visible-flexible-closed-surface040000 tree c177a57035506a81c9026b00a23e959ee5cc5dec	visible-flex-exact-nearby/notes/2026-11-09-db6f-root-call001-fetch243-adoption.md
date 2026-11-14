# continuation03 首个闭点与必要 fetch 的 root 采纳

会话 Astra-visible-flex-db6f0b0e，2026-11-09。

## 原有限 DN 延拓

continuation03 的 call1 在原 target path 的 s=63/64 真收敛，残差 9.40030806875761e-10，history 有 8 个基点。原控制器按既定规则将下一步减半至 1/128，继续 call2=127/128。root 闭点审计程序实际 exit0（receipt 34df83），核过 83 项入口绑定、8 项响应来源及不变的方程参数；本次发布前再次逐件重哈希全部 8 件闭文件一致。

这仍是中间 warm：没有最终 s1 的 audit、真实 prefix 外层解或全图结论。root session3046 在工作，当前活跃 progress、iteration、trace、trials 和运行日志不在本发布中；不从文件存在推断控制器退出。

## Git 2.43 的必要 fetch

root 已完整阅读兼容性审查与独立后验正文，并核对其闭清单。冻结 root 实际执行记录 a82e8c2757dc22e24c6670ffcb8dc3307d756b86d15494f22e2cd76e40a4e53e 记录第一次必要发布的实际 fetch/merge/push 成功；认证终端是持续 shell，其仍存活不能写成整个工具 exit0。

独立只读程序实际 exit0（69ecc1），从未变的旧 19 个 idx 重建 117057 个旧 OID，与冻结原始集合逐项相同；发布后全部保留。两个新包共 7549991 B，最大 7525795 B，新不同 OID 683，另有 122 个 OID 已存在。没有零重复或未来恒定体量保证。

必要 fetch 此后使用已装 Git 2.43 加 --no-auto-maintenance；merge/push 仍使用当前 Git 2.51。这个特定兼容流程不是 GC、repack 或一般旧 Git 替代方案。独立后验核的是索引集合、文件大小和元数据；它不声称全面解码 pack，也没有另外执行网络或认证检查。原始临时 OID 数据未新增到仓库；旧索引哈希与闭报告保留可审身份。

发布清单为同前缀 root-continuation03-call001-and-fetch243-publication.json；主线数学参数、g、guard 和容差不变。
