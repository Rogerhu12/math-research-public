# 2026-11-26：实际角峰入口的传递依赖遗漏与最小修复

本次为明确启动失败，未发生模型求值、接口 parity/方向检查、峰定位或优化。没有把失败算作科学进展，也没有据此重复已经完成的优化。两个 job 自然终态后才分别完整读取一次原 stdout。

## 原运行收据

Run `45784057434`，source `908290d8b1ad1ad33f14d973b348edfeabb7b6dd`，request `request-inverse-theta-peak-20261126.json` 原 SHA256 `d2bb7db82d24e499d40a1314a3f539124ff2be70209d0b8b1c0bd0692a1837db`（17444 B）。两个 job 均自然 failure、child returncode 1。

| lane | job | 完整原 UTF-8 日志 B | 原日志 SHA256 | child wall 秒 |
|---|---:|---:|---|---:|
| B030 | 139786269714 | 146906 | d1fcca1a37de74466787f24b9100e71724aac5d2fbedd5e6c3caff15c1ebb45a | .682827 |
| B038 | 139786269362 | 147576 | c7dead9b0cd7ce660d6e65aac4ab6c6663c8ca32957c68aba211e5ce46892890 | .588092 |

B030 child 为 `08:33:10.287091–08:33:10.969918 UTC`；B038 为 `08:33:10.398365–08:33:10.986457 UTC`。合计 import/启动 wall 成本 `1.270919` 秒实际发生，模型科学调用为零。两份完整原日志仅在 scratch，未写入仓库、artifact 或 raw blob。

两 job 的公共实际 pull 都从 source 到 `14e63940b9366c4ebcdbcd3480a0ab4300d63c10`，公根/topic 两 README diff 空，blob 分别 `282e86b03385d3b6245ce7100ae2e2af7b103c2d`、`d0432faff569c8e9af7ed4809847e12880976c11`。私库实际 pull 到 `f136cc8dd6a15e6894947d543600205b771e3d04`，根 blob `5ba164843b1f5802184178a82d786264404873a3`，QUEUE 检查通过。运行时 Python/numpy/scipy 版本与请求相符；凭据在 child 前移除。

## 准确失败位置

两个原 traceback 同样经过：

1. `inverse_r566_theta_peak_exchange_20261126.py` 导入 angular oracle；
2. angular oracle 导入已发布的 block Jacobian；
3. block source 对 `inverse_hard_exchange_resume_20261126.py` 读取绑定内容作 SHA256 核查；
4. sparse checkout 中缺该文件，`Path.read_bytes()` 抛 `FileNotFoundError`。

遗漏来自本次 workflow/source map 的打包，既有 block source 实际确实导入并绑定该 resume 模块。失败发生在任何 `THETA_PEAK_DEFINITION` 之前；原日志无任何 THETA_PEAK 科学记录。numpy/scipy 已导入和读取部分源码 hash，不等于构造了科学模型。

## 最小修复与后继身份

仅在 workflow 的 sparse checkout 增加既有文件 `scripts/inverse_hard_exchange_resume_20261126.py`，并在请求 source map 增加其原 SHA256 `befd444bfb96efc6721d1b0bad20deb25b32e915c1f789ab4d285085c2afcce4`。请求 schema 改为 `inverse-r566-retained-uniform-and-actual-angular-peak-exchange-request-v2-complete-import-closure`，绑定修复后的 workflow 并显式保留失败 run 号。

科学 driver `6094c15ff2696d6b64e9eac09ce60b54a59a64c545cb88fb7734df8bb185f757`、oracle `46eea6c6da4a94c82106e8a57ff98e70bf8f85bd2d0ef35c26cb649a0ee2f0a7`、两份精确来源 q、网格、trust 及所有求解参数均未改变。原旧 run 仍失败；新请求才是修复后的启动身份。首次正式科学 job 中的必要 parity/方向检查成功后继续同一次优化，不另开本地或独立科学预检。

本地修复只做静态传递依赖清单、hash 和 AST 核对，没有导入模型或执行数值求值。所有课题科学门仍未完成。
