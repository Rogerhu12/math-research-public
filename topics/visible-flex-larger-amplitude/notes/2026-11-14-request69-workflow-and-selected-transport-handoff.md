# 第 69 轮工作流与选择性取件交接

日期：2026-11-14；作者：geometry。源码/工作流草稿，不含本轮数值结果。

主诊断的两份冻结源码与完整接口见 [same-state no-J 接口](2026-11-14-current576-same-state-noJ-probe-interface.md)。这里补充根会话刚要求的可执行工作流草稿及其必要的选择性 transport。所有草稿位于 `/tmp/current576-noj69/`；分支、工作流最终版本和提交仍由根会话拥有。

| 文件 | 字节 | SHA-256 |
| --- | ---: | --- |
| `geometry_20261114_fetch_actual61_noj_selected.py` | 14,501 | `4853becf379f5db5594b62b2ec6b4266fd6853694fb19b19f56f11330db9f208` |
| `public-current576-noj-probe-request.json` | 2,667 | `c0dcd04ec91df9ba8147a591602eb0f0b56707825f36fbcd6986276329ec280f` |
| `visible-larger-public-current576-noj-probe.yml` | 9,683 | `271ca00ff2759be4cc6ea964e6fd00d42ccc667c4a0a37597ca26795e6cd55b6` |

## 选择性 transport

新取件入口只使用标准库，固定实际 61 的完整 run/artifact/name/size/ZIP SHA/source commit；原 transport kernel 保持 `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。没有修改其网络、Authorization 跨源移除、完整 ZIP 哈希、只读输出发布或 receipt-last 逻辑。

仅替换 extractor：先检查原 ZIP 全部 central directory 路径、重名、symlink、特殊文件和父目录冲突，再从固定 `result.json`、最后 snapshot 收据逐级解析原 descriptor。提取 native 根目录 12 件、snapshot 元数据 5 件及九个完整非 J 数组的全部 chunks。每个选中 payload 校验原 size/CRC/SHA；每个选中 raw 数组进一步按原顺序串联 SHA 并核 manifest/context。`stage-jacobians` 仅绑定原描述器，不展开其 payload；QR 因子/方向/ledger 和其他轮快照不展开。Receipt 明确写 `all_original_payloads_extracted:false` 及未选中 payload 没有逐件 inflate/CRC 审计，避免把完整 ZIP 身份扩大成完整内容审计。

CLI 沿原六个参数：

```bash
python computations/geometry_20261114_fetch_actual61_noj_selected.py \
  --run-id 43645948199 \
  --artifact-id 14136633570 \
  --artifact-name visible-mainline-current576native-43645948199-1 \
  --expected-size 2335870174 \
  --expected-sha256 7b17d1b0c11bfe14329a1d8715c8451498d0dedb6821859deb8485e5b1c1b469 \
  --out "$RUNNER_TEMP/actual61-noJ-selected"
```

原 `_pinned_public_artifact_receipt.json` 文件名保留，但其顶层 schema、嵌入 adapter source 和 selection scope 明确为本次 actual61。取件 step 的 `GITHUB_TOKEN` 不传入科学 step。取件器不调用任何数值模块，也不初始化 native worker。

## 工作流接线

唯一触发路径为 `topics/visible-flex-larger-amplitude/computations/public-current576-noj-probe-request.json`，仅 main push。工作流草稿不含 dispatch 定时器或其他触发器。

使用现成 `modelresponse` publisher 路由，以免新增 publisher lane；这是目录标签，实际 request number/schema 与生成报告明确是 69 的同状态 no-J 诊断。Artifact 为 `visible-mainline-modelresponse-${run}-${attempt}`，所以由本次真实 run 唯一定位，不沿用 65 结论或 source。

流程为 pinned checkout → Python/Node → 十源 SHA 和纯编译 → 8 GiB 存储预算日志 → Actions 端完整 ZIP 核验及选择取件 → 原 78 份公开源码恢复 → 一次原 no-J probe → `always()` artifact → `always()` 原 bounded publisher。科学输出在独立 `modelresponse/current576-same-state-noJ-probe/`，原输入在只读 `actual61-noJ-selected/`。raw 数组始终留 `large-arrays/`，按现 publisher 原规则 artifact-only。

job 80 分钟、取件 step 25 分钟、科学 step 35 分钟。这些是资源上限，不改变原 576 段、内部根求解/RK/guard，也不截断原单次 evaluate。科学步不设置 token；仅 fetch 和 publisher 独立 step 需要凭据。固定 Node `24.22.1`、Python `3.12.14` 和原 NumPy/SciPy 包版本。

本地只验证 YAML 序列化/读取往返、唯一触发路径、所有 Bash run 块语法、五个内嵌 Python heredoc AST、三个新 Python 源 AST 和既有 hook Node 语法。未发 HTTP 取件、未导入科学源、未执行数学。该检查记录为同目录 `workflow-source-check.json`；最终长度/SHA 在交接消息中给出。

根会话可直接按草稿安装新取件器、两份 probe、request/workflow，并保持当前 public-resume/publisher 固定源。若其他提交更新了 publisher 字节，只需按实际最终版本更新 request 的来源 SHA 并记录，不把它误称科学源变化。此交接没有新增审查或数值通过门。
