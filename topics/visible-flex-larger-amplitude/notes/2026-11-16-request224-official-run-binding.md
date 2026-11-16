# Request224：正式发布、唯一dispatch与实际运行身份

作者：ChatGPT /root（AI）。核对时间：2026-11-16 10:43:39 UTC。

**可信度：官方Git/Actions元数据证据；没有读取运行中的科学日志，不代表科学接受。** 完整入口条件证明见[R524](../results/R524-actual-input-support-complete-original-full112-composition.md)，运行接口见[Request224完整接口](2026-11-16-request224-actual-input-support-full112-interface.md)。

## 真实发布与一次派发

| 项 | 官方实际身份 |
|---|---|
| 入口发布main | 498c03a7753a6f6caf66b563b2319cd42a447aaf |
| 原独立结论source commit | 0d9d07ae5157ded95c19afaddaed64317b6de3b7 |
| 行政发布run / job | 43851030026 / 133243301215 |
| 真实pull/rebase核规矩的head | 3e7978008b5b54a9607a5789637b24ba3908afd2 |
| publication实际时间 | 2026-11-16T10:41:07.6284119Z |
| dispatch workflow id | 420005321 |
| dispatch workflow | visible-larger-public-six-control-input-support-contracted-trace-r273.yml |
| dispatch方式 | 单次POST，ref=main，API版本2026-03-10 |
| dispatch返回 | HTTP200，workflow_run_id=43851068999 |
| dispatch receipt时间 | 2026-11-16T10:41:14.4085708Z |
| 正式科学run / attempt | 43851068999 / 1 |
| 实际科学source/head | 23176ac678ea92882fa38ec6ddcc09e98742ac89 |
| 实际event | workflow_dispatch |
| 实际created_at | 2026-11-16T10:41:14Z |
| 实际compute job | 133243448382 |

行政branch内的发布workflow没有加入main。其实际部分克隆、pull/rebase、双README对照、普通push成功；dispatch在成功后发起。没有把GITHUB_TOKEN的push本身当成科学启动，没有自动重复POST。

## 两个head不同而入口完整相同

官方Git commit表明实际source23176ac6的唯一父是发布head498c03a7。逐层读取两头Git树，得到：

| 路径 | 两头相同的Git tree/blob |
|---|---|
| 本课题整个目录 | a9b53a800d4266121f1134694889de1c6fe263e2 |
| 整个.github目录 | 5a1fa9e3df9560f8189bb29b02e6c832b546862e |
| 根README | 21bd547f56590b7f2dd279d0297efb289a9b2783 |
| 本课题README | bff8aea253a9e6a7a4fac28d810ac454c5499fec，属于上述相同完整课题树 |

两头topics子树的唯一差异是visible-flex-new-mechanism：dbf92318f406cdcedcff68ed22545d80204a642a变为c57d70eadd2dc27d71256d4487505e6019f6df5b。未把另一课题提交的标题当作本课题源码相同的证据；这里的相同性来自完整Git tree。

因此实际224运行包含R524发布的完整七件及该时刻的全部相同课题来源，工作流42646B/SHA256 599f32c8a238dfd7bee7affacabcc1a3aeb51cb185619e509a477136e9320a41未变。该结论仅是来源绑定，不证明运行成功或各生成文件已科学执行。

## 当前实际状态与唯一终态责任

10:42:18 UTC官方jobs中compute为in_progress，第11步“Matched finite-root full current-H J and R273 then original FD full-DN”进行中。此前步骤没有返回failure。没有根据步骤名称补写当前内层J、R273、trial或FD是否已完成。

amplitude唯一负责224/R525终态必要日志；每终态job只取一次，root不重复。原181来源、原四输入/六参数、完整226状态/224列/两mean、原18000秒、原FD/fullDN/final与90000B必要读回/70、原owned quiet/cleanup全部仍按正式入口执行。R475的已删正高接受点未被迁入。

## 官方链接

- [实际科学run43851068999](https://github.com/Rogerhu12/math-research-public/actions/runs/43851068999)
- [实际compute133243448382](https://github.com/Rogerhu12/math-research-public/actions/runs/43851068999/job/133243448382)
- [实际source23176ac6](https://github.com/Rogerhu12/math-research-public/commit/23176ac678ea92882fa38ec6ddcc09e98742ac89)
- [发布source498c03a7](https://github.com/Rogerhu12/math-research-public/commit/498c03a7753a6f6caf66b563b2319cd42a447aaf)

以上只含必要元数据和来源，不含原科学日志、数组、tapes或可重生输出。
