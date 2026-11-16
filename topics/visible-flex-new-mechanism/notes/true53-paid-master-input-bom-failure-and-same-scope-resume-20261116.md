# true53 有限主问题：首次输入失败与同账户续行

**分类：已观察的实现失败；不产生有限规划、不可行性或全网格方向结论。**

## 原始运行与未开始的科学

源提交 `01614a9cbbc2ce1cfe93318915dee05292dc586a`；
公开 Actions run `43816639046`、research job `133130076418`。
原始 `TRUE53_PAID_MASTER_COMPLETE` 报
`new-finite-master-input-solve-or-output-error`，抛出
`ValueError: original complete source records missing`。
原日志原字节长度与 SHA 检查已通过，失败在行解析后的四记录完整性门；
没有进入 assemble、有限 LP 或任何 Newton 系统。

`FINAL_CLOCK` 为本次 **5.828010012 秒**，祖先加本次
**1600.268237108 秒／128 个 ordinary values**。
有限 LP 0、迭代 0、Newton 系统 0；新 geometry、hard J、JVP、gradient、
scalar、actual 全为 0。实际点仍 accepted53，物理 SHA
`9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e`。
CI 成功仅说明错误报告完整发出，不说明科学成功。

## 唯一输入缺陷与修复口径

原 run43811870681 的已付 read-only 报告已记录：
MODEL 与 COMPLETE 的 `timestamp_prefix` 各自以 U+FEFF 开始。
对整个串只做 `decode("utf-8-sig")` 仅去除串首 BOM；
原实现对每行直接使用锚首 `TIME_PREFIX.match`，故漏掉这两个中间带 BOM 的行。
PROJECTION_RESULT 与 FINAL_CLOCK 的时间前缀没有这个字符。

修正为对每行 **timestamp 之前的** BOM 使用 `lstrip("\ufeff")` 后再匹配。
不改 JSON payload；四记录仍逐个检查原来的完整 JSON+LF 长度和 SHA，
原 raw log 指纹、MODEL binding、原始数组及选定点全部保持。
这是有确切失败证据的输入修复，不重跑已完成有限求解。

继续同一个新 finite-master 任务，原上限仍为 1 次 LP／96 次迭代／
192 个系统／240 秒；已经失败的 **5.828010012 秒**计入该 240 秒，
续行的 ledger 起点相应提前，实际新增耗时和同任务累计耗时分别报告。
原日志此前已读一次，本次续行再读一次并如实记账。
旧 HiGHS64、cone32、Hildreth／完整分离配额均保持原观察边界；
不把这次失败记为零，也不增加或重置它们的科学账户。

若续行获得 finite positive primal，下一任务仍是同一确切方向的完整双网格
分离、原 scalar guard、真实圆整、原始 actual 门；有限规划不替代这些门。

## 本次实际 pull 与规则

run43816639046 在科学开始前实际执行公开
`git pull --rebase ... main`：
2026-11-16 06:25:49.056606 → 06:25:49.474729 UTC，
before=after=`01614a9cbbc2ce1cfe93318915dee05292dc586a`，返回码 0。
根 README blob `21bd547f56590b7f2dd279d0297efb289a9b2783`、
本题 README blob `d0432faff569c8e9af7ed4809847e12880976c11`，
两份 diff 均空，root 已读这两个 diff；下次实际 pull 不晚于 07:25:49 UTC。

同 run 私有实际 pull 为 06:25:51.896233 → 06:25:52.492655 UTC，
before=after=`914004a08eca6ae9769bf2e2a4846dac599c3cb4`；
私有根 blob `5ba164843b1f5802184178a82d786264404873a3` 未变、私有本题 README
不存在，QUEUE 本会话仍唯一进行中。只发表此元数据，不发表私有内容。

## 原输出指纹

原生接口解码串重新按 UTF-8 编码：100052 B，SHA-256 `ea9833d042b55fc803e1b5fd866be0ffb83f09f9bff1bb7392ad32ee82bf57b2`（不擅称服务器下载原字节）。

- COMPLETE JSON+LF：4946 B，SHA-256 `3321fb6dae43e6f1d12d068737e74c3f41e17a16973d6198b48ae938db086661`。
- FINAL_CLOCK JSON+LF：1385 B，SHA-256 `9c5e533ec4948fb9b8bbc2189cbb185ab75f25b3c0b35a61f3863925e9499e16`。

本条只保存源、参数、运行编号、指纹与人读失败结论；数组与原输出不入 Git。
主完成门未达到，继续原任务。
