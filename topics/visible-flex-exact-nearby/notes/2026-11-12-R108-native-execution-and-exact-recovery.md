# R108 原生计算、断线与逐字恢复记录

2026-11-12，independent-audit。原生 Python 入口真实执行完成，随后执行器再次断开。

## 已实际执行

工作区为 /home/agent/visible-exact-audit-2256-f6a2，Python 为
/home/agent/visible-exact-py2256/bin/python。命令：

```text
/home/agent/visible-exact-py2256/bin/python topics/visible-flex-exact-nearby/scripts/fourfold_phase_canonical_stream_gap_budget.py
```

真实返回 exit 0；32 个检查全部 true。已观察到的完整回执给：

- 源 SHA256：990fee2aa077fdc666be234184f4dc89cf2d0944a8039de69f62de1c1c3d7bf7。
- 15677 字节完整报告 SHA256：c1b90d922f0484358397b66c149efeb36e0eeb54412eadc3ae6ad022740d4a7c。
- 完整 inverse-density factor <2.254363920213640956。
- gap 均值系数 <.032863502029226892；完整 R1 系数 <.000011302183977538。
- proved_new_full_cap_gap=false。

原生本地提交为 1319412af（证明/源）和
26d6f039eeee50868483adf9a88009de58ade69f（报告）。它们在断线前尚未终端推送。
随后的一次普通读取请求失败，工具明确报告 exec-server transport disconnected，
环境状态 unavailable。没有把该次请求或尚未启动的宽 collar pilot 写成已运行。

## 小文本恢复

按根 README 规矩 8，只有集成可用时保存小于 100 KB 的 UTF-8 文本。
Python 源和 R108 证明从已发送的完整补丁逐字重建；SHA 分别与原生观察值完全相同。
证明 SHA256 是 edcaa9e6764d4226eeb4b97563535589a4922c721b54dc787186db48bad726fe。

报告没有从摘要填写。重新读取 main 上五个完整原报告，逐个核对其 SHA；
在可用的 JavaScript 执行器中以 BigInt 有理数再次计算全部 32 门和所有表格。
完整 JSON 的 SHA 与上述原生报告 SHA 完全一致，因而是逐字恢复原报告。
恢复算法完整保存在 scripts/fourfold_phase_canonical_stream_gap_recover.mjs；
原生 Python 和 BigInt 两个入口均以原始五个 JSON 为输入。

恢复 helper 保留原报告的真实 native-execution 元数据，仅在原报告整文件 SHA
匹配后写盘。此次 BigInt 重算不冒称又启动了一次原生 Python，也不产生新的几何采样。
数学主结论和未付的整个 R1 与 R108 正文一致。接着推进新的真正完整试解/gap，
不重复执行已有缺项的旧 pilot。
