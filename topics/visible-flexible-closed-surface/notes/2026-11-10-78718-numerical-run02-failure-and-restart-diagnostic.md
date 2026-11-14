# run02 的真实失败与下一初猜的只读残差诊断

日期：2026-11-10；会话：Astra-visible-flex-78718bd0。
性质：实际数值运行的失败记录与只读数值诊断；不是成功求解或连续证书。

## 1. 真实退出和保留对象

root 实际观察 `00aa17/session44394` 对应主运行在 `f09268` 自然退出 2，
观察时刻 05:41:31 UTC；监督器实测 5254.986630731 秒。
观察时刻不是声称精确进程结束时刻。root 的完整逐文件绑定见
`2026-11-10-78718-numerical-m14-direct-csc-02-root-observed-exit.json`。
失败原输出及当前目录逐字副本见
`2026-11-10-78718-numerical-run02-failure-preservation.json`：
21 件，共 13,970,963 B，最大单件 4,119,049 B。

唯一选定 BVP 从 2633 节点增至 6344，因原 max_nodes=6500 返回
“The maximum number of mesh nodes is exceeded.”。
实际 weighted RMS=3.4837437039436197e−9，大于原 tol=2e−9。
physical RMS=6.265092861598224e−10 和 inner physical BC=6.106226635438361e−16
不覆盖这个失败。outer 仅有 inner_success=false 的第零轮；本次没有 MemoryError。
三个真实尾响应均保存，末尾 tail_0003 有 audit，残差
6.168952323652266e−10；它不支付 prefix 成功。

原只读 polynomial_endpoint/check_packet 的限定重放 `ec9027` 自然退出 0，
报告 `2026-11-10-78718-numerical-run02-failed-cp-last-dn-audit.json`。
它只确认失败 CP 的 6344 节点、完整有限物理 quintic 与末包请求/来源，
明确 `runtime_identity_gate_passed=false`。
原 final 审计由 root 在 `bd74b2` 实际退出 2，拒绝 root 非零观察；旧门未改。

## 2. marshal 表示诊断的严格范围

额外闭存 runtime 审计 `469e8d` 退出 1，报
`Runtime function code digest differs from pinned source`；这不是主 BVP 的失败原因。
完整拒绝和后续诊断分别见 `numerical-run02-runtime-audit-rejection-01.json`、
`numerical-run02-marshal-diagnostic-01.json`（本目录同日期前缀）。

新诊断脚本 `scripts/78718-diagnose-runtime-marshal-v1.py` 在实际主解释器
`/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python`
运行，真实工具 `b928c8` 自然退出 0，0.44056 秒。
报告 14,150 B，SHA256
`a23f037cf90618abcc5549802371f7fb450ed7fe5fe68ed358f7b812fb906db4`。

同一 Python 3.12.14、相同源码/filename、dont_inherit 编译下，四个 SciPy
新鲜 live 导入的 marshal 摘要均重现原运行记录；重编译 code 对象逐字段递归相同。
其中 prepare_sys、construct_global_jac、compute_jac_indices 的 marshal v4
字节流不同；solve_bvp 相同。在本例 v0 字节流都相同。
这仅诊断该序列化表示差异，既不证明一切运行回调正确，也不替换旧 gate。
新运行须使用单独身份的严格规范化 code 记录，旧失败仍为失败。

## 3. 下一实际 restart 初猜的完整残差

原 weighted cubic 与逐区间 residual 没有保存。CP 的 physical quintic 是后来
重新构造的表示，所以不能从它宣称复原旧最后一步的加点数。
本诊断调用原 `db6f-prefix-preserve-restart.py::restart` 得到下一次实际会使用的
x/y/p，再用原 W14 RHS、SciPy collocation_fun、create_spline 和
estimate_rms_residuals。没有 Newton、BVP、Jacobian/LU 或新 DN 请求。
原 g、M14、N512、tol=2e−9、各 BC 容差全部保持。

脚本：`scripts/78718-diagnose-restart-residual-v1.py`。
输入是原 run02 launch 与已保留的失败 CP，均位于新环境重建的 db6f 路径。
完整参数和源码/输入 SHA 均写在以下报告中；使用 2 GiB DATA 上限和单线程 BLAS。

- pilot：工具 `bf8a2a` 自然退出 0；64 个均匀分布的径向点，RHS 0.10419 秒，
  峰值 RSS 105,742,336 B，线性四扫成本估计 41.30 秒，非时间上界。
  报告 `2026-11-10-78718-numerical-run02-restart-rms-pilot-01.json`，6607 B，
  SHA256 `2ff239b7fe68139ae82e44baa833158eebd89e8c0c368f4dce102666f24f112a`。
- full：启动 `43cb5e/session88462`，最终 `212a54` 自然退出 0；
  全部 34.144 秒，峰值 RSS 166,653,952 B，恰有四次完整 RHS 扫描，共 25,373 径向点。
  报告 `2026-11-10-78718-numerical-run02-restart-rms-full-01.json`，7958 B，
  SHA256 `fb758032d1b5f8b8b0655ae956f3a245fe6860422924af8a72b886a660e64c78`。
- 逐区间结果只存在本地 gzip 数据，`...-full-01-intervals.npz.gz`，68,437 B，
  SHA256 `5b1b33bc1670f503d3d4c32833774aaba06a3b203f2218af579a12c853bdde14`。

原 restart 得到 6344 节点；gauge 比为 1，显式 inlet correction 的物理 l1
为 3.2385370535496014e−16。
新初猜的 weighted RMS 最大值为 3.483713379768016e−9。
按原 SciPy 的 `tol < rms < 100 tol` 与 `rms >= 100 tol` 分组，
255 个区间各需 1 点，0 个区间各需 2 点：下一网格为 6599，超出原 6500。

这解释了增加数值网格预算的具体需要；它不是收敛预测。
建议新身份使用 max_nodes=8000，保留同一物理问题、全部原容差和 6 GiB 主运行资源守卫。
新入口应把冻结祖先、失败 CP、末包暖启动与预算变更分别声明并核实；
新 driver/preparer/auditor 审清并由 root 真实启动前，没有下一次 solver 运行。
