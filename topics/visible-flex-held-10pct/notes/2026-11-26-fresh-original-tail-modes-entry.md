# Fresh 原恢复 → 低模至完整 M24 DN 入口

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

独立 `seam_recover_original_tail_modes.py` 从当前恢复 harness 复制，去除全部
v5 依赖及设计调用。原 ports/solve/q=.006→.06/λ0/λ.002 M8→16→24 恢复块
**6801字节逐字保留**，SHA 为
`c6eb048d90ffa2863234455b68c324a43869ff7a5a10b88a6d2c7141dcc4dd9a`。
原 chart/setup 检查及全部恢复输入 pin 保持；只有真实 M24 finite pass 才进入尾。

`--work` 须已有原 recovery setup 的源、chart、port、native/chord 和清单。
不在这里重复新增 bootstrap。调用只有：

~~~bash
python seam_recover_original_tail_modes.py \
  --repo REPOSITORY --work FRESH_RUNNER_WORK --outdir NEW_RECOVERY_DIRECTORY
~~~

最后直接运行固定 SHA
`c558a38fcb6b0a8ba93f45431614d8d5d8b9b997d9cca078cd0ba1e023e13a0a`
的 `seam_tail_low_modes_to_full.py`，传原 repo/work、最后真实 M24
`previous`、`work/m24-tail-settings.json` 与
`out/tail-lowm-to-full`。

父保留子实际 status/code；即使子启动失败、没有 summary，也不造成功或将该
实际 code 统一改成2。原恢复阶段仍仅允许原 code0。子 summary 只投影
status/result/error/source_hashes；移除父1 MB停止门和原始 last_log_lines，
完整场仅在 runner。父不宣称 λ1、prefix coupling、固定 g 精化或闭面完成。

本地仅执行 compile/help（均0）、恢复块字节/SHA及来源/分支检查，全部通过；
未执行恢复、BVP、DN 或 CI。检查记录：
`notes/2026-11-26-fresh-original-tail-modes-source-checks.json`。

- 新 harness SHA：`a9d3774fbd1878b96cb29b0349e829f34ed8fe8b5a84b3978ca2a5656cbc8910`。
- 检查 JSON SHA：`b8961a7ac05c2a578be96e3987dbfdf51db1a31dd52756c3e4d7b2afe878e184`。
- 被复制原 harness SHA：`5b02d772bfa5b17360ee505cc040f5e2f6cc6651d696174a05f1a0fdcd66a05e`。
