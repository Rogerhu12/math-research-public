# 旧公开 Actions 的真实终态及同场几何边界

2026-11-26，Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：已核实的运行记录；没有新的科学计算，没有新曲率或 reach 证书。**
本条接续 2026-11-20 的已发布结果，不重跑已登记的科学结论。

## 1. 两条旧作业均已终止

2026-11-26 直接读取 GitHub 的 run、job、check-run annotations 和实际 job
日志，得到以下终态：

| 运行 | job | 真实终态 | 终止时间 UTC | 科学范围 |
| --- | --- | --- | --- | --- |
| [44772201880/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44772201880) | 136412503714 | completed / cancelled | 2026-11-20 22:09:40 | 公开记录只到阶段30；完整K的阶段31未返回 |
| [44758209061/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44758209061) | 136363458452 | completed / success | 2026-11-20 20:29:57 | 42个阶段已发布；controller以 budget_checkpoint 正常退出 |

几何 job 的 check-run annotation 明确给出原因：
`The job has exceeded the maximum execution time of 5h50m0s`。
这是执行硬时限，不是某个几何不等式的数学拒绝。
job 启于16:19:24，科学step启于16:19:46。

几何实际日志最后给出：

- 21:53:12，控制器发布阶段30及规则同步到
  `f0548477576caa2373d1626227a284ccfa9767d0`。
- 随后 `followup_budget_admission_closed`，活动步骤仍是
  `continue-complete-sixjet-curvature-03`，子进程PID7032。
- 22:09:37，GitHub取消该step，清理时终止父进程PID2595和子进程PID7032。
- 没有完整K的 `followup_returned`，也没有后续同场几何组合的实际返回。

这说明旧 HANDOFF 所写的 running 已过时；不能继续把它当活动任务等待。
但不能由此断言旧K程序一个胞也没有算完：其科学stdout与中途JSON在runner本地，
控制器在子进程自然退出后才汇总。公开 job 日志没有可恢复的逐胞K记录；
现有已发布小结不支持恢复任何新的旧K上界或已覆盖集合。

求解 job 的最后科学返回为阶段42
`actual-R671-PCG-SOC-returned-attribution-02`，对应已发布的
[PCG/SOC结果](2026-11-20-actual-coarse-PCG-and-parent-row-SOC-result.md)。
20:29:46控制器报告 `followup_controller_checkpoint`、
`reason=budget_checkpoint`、`actual_returned_steps=14`、
`research_complete=false`，随后正常退出。success只说明该作业正常结束，
不改变README未完成的事实。

## 2. 同场几何的已付与未付

几何worker03的实际末场仍为
`756936ee8b18ddace1673d02db678dd3db3c20944b82dce60af2404ddef390bc`，
node报告为
`8c0aa79e011b5c98db72caa3c10b82839a9fb90b2f272d722ff079040512c0e6`。
其已付范围保持
[原实际首jet/半径结果](2026-11-20-geometry03-actual-field-and-radius-return.md)：

- 922个原胞全部首jet连续覆盖；支持下界 `0.2965427454452786`。
- body直径上界 `4.099300336920071`；原四marker后直径上界
  `4.101300336920072`。
- 完整像握持变化比例下界 `0.22886895328877543`，握持区直径比例下界
  `0.21944259772886254`。
- 原四marker条件下全族闭嵌入、固定握持区和含反射非全等结论按原报告保留。
- **没有本场已返回的完整K、reach组合、共同g的全域误差证书或固定g精化收敛。**

该场的已发布有限点max是 `0.013601420431375466`，已显著大于目标。
它不是求解run2的c4a3、7fd或3ef8场；不能跨场移动上述证书。
较新的3ef8场仍须自己的连续几何核，不能继承7fd/756936ee的几何结论。

R666继续只保留给实际同场完整曲率及reach的科学返回，本运行终态不占该编号。

## 3. 后继执行的具体责任

现有f476入口
`actions_resume_closed_curvature.py`能在**同一runner**导入8ca中途报告，
或从逐胞原子journal精确续接；它不实现跨job紧凑摘要导入。
旧run的runner-local文件没有可用的已发布副本，不能以其文件名或SHA伪造seed。

今后对新求解场运行K时，应让新场、首jet、K及最终组合留在同一个实际工作目录，
从真实bundle/node记录身份；计算仍只在本公开仓库Actions。
优先改进逐胞/分组覆盖与小结发布，避免长子进程直到硬时限才丢失返回。
小结只保存具有明确域的统一上界、覆盖胞集合、准确输入及源SHA、run及实际成本；
不保存可重算数组、逐点报告、逐胞raw或分块数据。
这项后继实现与新的科学数值仍待实际完成，不由本条预报。

## 4. 可核验来源与日志身份

直接读取的API：

- `GET /repos/Rogerhu12/math-research-public/actions/runs/44772201880`
- `GET /repos/Rogerhu12/math-research-public/actions/runs/44758209061`
- 两个run对应的 `/jobs?per_page=100`。
- `GET /repos/Rogerhu12/math-research-public/check-runs/136412503714/annotations`
- 两个job对应的 `/actions/jobs/<job_id>/logs`。

job日志仅在本次读取时于内存提取终态；不将日志原文提交。
几何日志79,686字节，SHA256
`e783a24f1c27f9ed3c29188d8478e51974057e63a40a5e2bce7117e038a2d53c`；
求解日志255,052字节，SHA256
`ca0849c41a0170f97add6c795f2ed7e56bd8312f4b6b999ee060de237ab82eff`。
日志端点未采用Range响应，实际返回完整上述小文本；工具输出只保留末段。
