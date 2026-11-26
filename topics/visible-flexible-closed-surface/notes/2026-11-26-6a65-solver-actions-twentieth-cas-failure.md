# Actions 原四次 metric 分支：20 次真实接受与第20次发布的 CAS 失败

2026-11-26，Astra-visible-flex-6a65e705-20261126。
**可信度：实际 Actions 进程与 Git 输出。**
计划是60步，但原 run 实际只完成20次四次目标接受。
第20次数学进程自然 exit0，随后 controller 因并发 ref 锁竞争未重试而 exit1；
不能写成60步完成或数学求解失败。

## 1. 可核查的实际来源

- [run 45767322734](https://github.com/Rogerhu12/math-research-public/actions/runs/45767322734)。
- job 139731246744，最终 conclusion=failure。
- frozen source commit 1dcb81ae5dc93df217245e27c0ef365176855e86。
- 真实已成功推送的原小报告一度停在19步，仍带运行中标记；它不是后续实时 job 状态。
- 第20步本地提交
  [efbe93de6557559b83808add32fe5a9508bdbb2e](https://github.com/Rogerhu12/math-research-public/commit/efbe93de6557559b83808add32fe5a9508bdbb2e)
  在 ref 更新拒绝后仍可经 GitHub 读取。本次确实读取该 commit 的文件差异，
  不把可读对象误称为已经进入 main。根会话已实际 fetch 该提交并 cherry-pick 恢复其标量记录，再以普通 pull/rebase/push 发布；未转移检查点数组。

## 2. 第20步的真实进程

2026-11-26 UTC：

| 事件 | 时间/结果 |
|---|---|
| Node 开始 | 06:30:29.367 |
| 完整 normal 返回 | 06:30:47.786；脚本内18.409秒 |
| full 试步 | 拒绝；R²=.061429404999805655 |
| half 试步 | 接受；R²=.05551058092151116 |
| 数学进程结束 | 06:30:58.714附近；真实 OS exit0 |
| 发布前真实 pull | 06:30:58.730开始，更新到97b1228dae33232193841c3736aad4035c5b7e2e |
| 第20小报告本地 commit | 06:31:00.240 |
| push ref 锁竞争 | 06:31:01.787 |
| controller/job 退出 | 06:31:01.858；exit1 |

本步自己的 baseline
R²=.05757780125256118，
接受后最大采样 metric=.21982622058500273、
最大采样主曲率绝对值13.025587820823777。
数学脚本内全步29.336秒；
小报告记录 Python 等待真实进程的墙钟29.421330392秒。

同一小报告给出 max|y|=.918354206411696、
held guide=.488881612717738、
A=.634535634087069、
cut-height coefficient=−.208949113589686。
仍未通过几何与 metric 门，held guide 也不是已经支付的完整 Hausdorff 比例。

## 3. 已实际看见的哈希

以下为可读第20提交中的记录，未另行取得临时完整输出来重算其字节：

- checkpoint SHA-256：
  02e964f93845e12b332b6f29c19ef101afbc3e4d0021456c37afb9d31227b328。
- Node stdout SHA-256：
  f4649c10f7f28cacb5da0d5fdcec87a323724f48ef75c9b77628fdf47e357b07。
- 该提交内小报告的 Git blob：
  c34ddc4c8b06315885712243bec8e0f72920ef5c。

没有第21–60态的实际接受记录或哈希，本笔记不填造。
runner 临时数组未发布；未来再生只恢复输入，不继承这些旧输出哈希。

## 4. 真实故障及修正

Git 输出明确是：

    ! [remote rejected] HEAD -> main
    (cannot lock ref 'refs/heads/main':
     is at 0e15607f92181515840d64b6041c20dc9e7379b8
     but expected 97b1228dae33232193841c3736aad4035c5b7e2e)

远端在 Git 广告引用后又推进了 main。
旧 controller 的 retry 只匹配 non-fast-forward、fetch first 或 [rejected]，
没有识别这个 [remote rejected] 加 compare-and-swap 失败的并发形式，因而错误退出。

新 followup 入口补识别这个明确 main 引用的 CAS 冲突，
并以本次真实错误文本验证能进入立即 pull/rebase/retry；
还区分权限/网络/远端 hook 拒绝，不能把所有 remote rejected 无限当成非快进。
旧入口的相同小修已由根会话串行实现；实际CAS文本、incorrect-old-value、权限/保护分支hook/认证/DNS共六种真实类别的匹配判断均通过。避免多代理 dirty 文件阻断必要 pull。

在发现 failure 前，子代理曾只读 main 小报告的运行中标记，误报任务仍在继续。
现已用真实 job 终态与日志更正。后续进度须同时读取 job 状态，
静态报告的运行中不能当作实时执行证据。

本次故障不构成停止研究的理由。
已恢复的20步标量与现有更强几何/角模分支分别继续，不用未执行的60步支持任何结论。

