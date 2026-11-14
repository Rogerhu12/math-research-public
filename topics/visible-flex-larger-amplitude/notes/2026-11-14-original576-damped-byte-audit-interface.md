# 原 576 段 R273 输出的纯字节审计接口

- 分类：实现接口；仅 AST 和源码检查，尚无此入口的实际审计结果。
- 作者：ChatGPT（exact_refinement）。
- 日期：2026-11-14。

## 1. 对象与边界

新源 `computations/exact_20261114_audit_original576_damped_bytes.py`（36895 字节，SHA-256 `d57c01143168b53fe6e562647104204f661b8f59a94babcc5c71e232a90d1425`）只审计[原 576 段 R273 入口](2026-11-14-original576-damped-chain-and-actual57-comparison-interface.md)已经完成的输出。它使用标准库，只导入冻结的旧字节审计工具 `exact_20261114_audit_damped_chain_bytes.py`（SHA-256 `5618d29c41d95d668c959b05cee8295ce4285b2a50961277f557f8cfb717b440`）中的字节、JSON、gzip、行序和 IEEE 分类函数。

不导入 NumPy、SciPy、求解器、矩阵适配器或精确算术内核；不运行 RHS、J、ODE、QR、回代、矩阵作用、$\sigma z$、范数、分数运算、残差或非线性试探。报告中的科学数字直接复制实际 Actions 报告，并记录对应文件身份。它不重选最大值，不替代任何科学计算，不是运行或接受门。

## 2. 完整读取范围

1. 原 576 输出的全文件清单、全部 array descriptor 的实际大小和 SHA、所有 gzip 完整 CRC；每个 binary64 数组的 shape、有限/非有限分类及负零计数。
2. 全部 577 个 R/S/仿射因子和纯常数 payload；节点次序、块列范围、下三角实际零字节、每个罚块和所有常数行的完整结构。只核保存对象，不重新相乘验证因子分解。
3. 全部 576 个形成系数记录的原 J/尺度身份，以及形成模型的规范 JSON 哈希。形成 V/rho 的完整 payload 没有独立导出，因此这里不冒称重新验证了这些数值系数。
4. 完整 `[577,224]` 的 $z$ 和原坐标方向、checkpoint 每个词及负零 sidecar。恢复到零只按已存 $z/\delta$ 的 IEEE bits 分类，不计算 $\sigma z$。
5. 新方向与 actual57 原方向的两份独立完整原 576 整数行账：各 129248 行、cut/stage/far 次序、每个 block 的 J/方向/尺度身份、保存的逐块最大记录、保存的全局最大记录及其所在行。所有有理表达只查语法和原样对应，不重新约分、比较有理数大小或计算其小数。
6. 两份最坏行见证的原 $J$ 行、当前/下一方向、残差、far G 和尺度 bits。stage 的原 J 行从 actual28 对应 chunk 逐字取出比较，不形成点积。
7. actual28 完整原 capture 的小文件、manifest、全部 raw chunks、完整 576 J 串、每个单块及全部数组的累计 SHA；与新 binding 和九个导出非 J 数组逐字对照。
8. actual57 选择性取入的五件：固定 result、input binding、完整 manifest 的文件、已经保存的 577 节点方向、对应 checkpoint。manifest 其余 payload 没有被提取，不宣称重新审计它们，也不重复 1373 到 577 的限制操作。

factor 报告的真实源码身份保留借用类 `9b951f…`；新 entry/source `e1a35b…`、adapter `c78dfc…` 和原内核 `0bc8f9…` 分列。两个精确账必须绑定同一个实际原 576 矩阵身份；actual57 的来源仍明确是其原 1372 目标。

## 3. CLI

实际 result SHA 由已完成公开 Actions 原件读取，不能预填未来值。示例中的变量由调用方填入真实路径和 SHA：

```bash
python computations/exact_20261114_audit_original576_damped_bytes.py \
  --directory "$ACTUAL59/native-original576-damped-chain-qr" \
  --expected-result-sha256 "$ACTUAL59_RESULT_SHA256" \
  --expected-eta-text 1 \
  --capture-directory "$CAP28/native-correction-capture" \
  --reference57-directory "$CAP57/native-damped-chain-qr" \
  --source-directory computations \
  --out-summary /tmp/actual59-byte-audit/summary.json \
  --out-detail /tmp/actual59-byte-audit/detail.json.gz
```

`--source-directory` 可选；提供时逐文件核本次 producer、adapter、借用 factor、原 reader、精确内核、字节工具的源码 SHA。省略时报告明确只绑定保存的源码清单，不声称读取了当前源码文件。

审计输出必须是两个不存在的同目录文件，并位于所有输入目录外。保留 `summary.json` 和 `detail.json.gz` 的相对关系即可连同原字节归档，避免重命名后破坏 `complete_byte_detail.file`。

## 4. 报告及实际执行范围

`summary.json` 汇总完整原件数、数组数、全部因子和常数行、两个整数行账的字节核对、两份最坏原行操作数、actual28 来源与 actual57 五件输入。`copied_Actions_scientific_reports` 仅复制原 factor/model/solve/两个 exact 摘要。`detail.json.gz` 保存全部文件、数组、因子及来源清单，不把大 payload 写入报告。

任何字节、行序或身份不一致会报告实际错误并停止声称“完整审计通过”，但这不修改原计算结果或其接受规则。该入口只在真实结果存在后读取原件；源码与 AST 检查成功本身不算一次审计结果。

本地允许运行的仅是上述 byte/structure 审计。所有科学计算仍只在本公开仓库的 Actions 上执行。
