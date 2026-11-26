# q2 全 H 冷入口：两组源缓存已完成，root 修改活动摘要导致发布冲突

可信度：**实际 Actions 日志和退出事实**。run `45848177096`、job `140007200479`、attempt 1 于 2026-11-26 15:46:17 UTC 结束为 `completed/failure`；controller 的实际退出码为 1。本次尚未启动 single/joint/refined/area/full-normal 的任何 LM，实际接受数为 0。它不是一次全 H 求解失败，也不是已完成的课题。

## 实际原因和责任边界

根会话在提交 `ab2cd23e93eb8b1c2a04131da693376e61a73b46` 中，直接改了这次仍在运行的 CI 摘要
`notes/2026-11-26-6a65-gap105-q2-full-normal-45848177096-1.md`，澄清 own-zero 阶段没有两组 Cartesian 联合求值。该勘误内容正确，但修改了 controller 正在更新的同一文件。根会话应把此类运行期间的勘误写到独立文档，保留 CI 的活动摘要写入权。

15:46:13，CI 结束 prepare 并提交自己的新摘要。15:46:15，实际 `git pull --rebase origin main` 拉到 `177f4e121…`，这个 prepare 更新和上述 root 修改发生同文件 content conflict。已载入的 v5 publisher 只实现自己的 HANDOFF marker 冲突处理，遇到这个 Markdown 冲突直接抛出：

```text
Actual pull/rebase failed outside own HANDOFF marker
```

异常路径随后又在尚未结束的 rebase 中尝试发布失败记录，第二次 pull 因已有 `rebase-merge` 被拒。日志明确记录了这两个连续错误；公开摘要因此仍停在 15:27:02 的 own-zero 回执，不能拿它当运行存活证据。这里不把 root 同文件并发编辑的后果模糊记作数值失败、机器内存不足或全 H 算法失效。

## 已实际完成的计算

触发源码提交为 `e2f9ea985b796d476c0086b66dc64caa895e15f7`。prefix 与 own-zero 均已经返回并成功发布，own-zero 输出 SHA 为 `17b71950c9df9d037751151fb6872b2b6db521c7db8c27b0c4b2988d00709621`。日志实际 value 行给出 metric `2.4894666459332084`、曲率 `26187.37906026061`、held `0.599280262738708`；这属于原 Cauchy 工厂的零自由系数 value，不是新双网格 Cartesian baseline。

prepare 子进程依次完成两组直接源缓存，并回到只在子进程成功退出后才执行的 `publish_stage` 路径：

| 实际源输出 | 形状/时间记录 | SHA-256 |
|---|---|---|
| training jets | 514 径向 × 128 全角；15:37:28 写完 | `355b404258c36f300b41f540792abcdaeeb901513fc5e783db195d644a3bf28b` |
| training radius | 同上 | `b9a8fa1caec9b6aacebe36de64858cf08eb8e2bdce1ec8eccb116d941d874d61` |
| second-grid jets | 343 径向 × 192 全角；15:46:13 写完 | `2291be541c70dd57f014e1143f25eb29f3ee63ac16f96c2c3b378e7df0f420e5` |
| second-grid radius | 同上 | `a449f63b75bdb5f7d2d382242104b1bb0f3370affd310085ba56faa67198ad15` |
| complete prepared | 原 2400 列空间；源程序内部 `1149.3351968560003` 秒 | `c8b28d3a7dfd27db19cb6d6db3873e888921d891beabde921e9b3952b5a97d70` |

这两组数据是源缓存，不是 LM 接受；后来的 5292 列转换和 q=2 full-normal 仍未发生。源程序内部时间不能冒充已丢失的独立外部进程计时回执。未发布的 prepare 提交在日志只出现短 ID `1155d9ec5`，失败记录只有 `50df80f18`；不补造其完整 SHA、child stdout SHA 或其他不可见字段。

## 修复范围

下一显式 source/controller 采用按真实阶段条件生成的摘要：原工厂 own-zero、单训练网格加独立观察、两个共同训练网格分别如实标记。root 不再修改运行中的同一摘要；独立勘误文档可以正常发布。

publisher 对这个已经发生的冲突需要最小恢复：只有严格确认本 job 唯一尚未发布的摘要提交、当前 ledger、允许路径和 commit 身份以后，才能撤回这一个本地未发布提交，真正 pull/rebase 到最新 main、检查双 README、从完整实际 ledger 重新生成自己的摘要及独立 HANDOFF marker，再普通推送。上游独立勘误和其他人的正文必须保留；不得 force、删远端历史或重置其他未发布工作。新实现须用这次同文件并发的本地 bare Git 场景实际核验。

runner 已结束，没有可继续消费的同 job raw。准备成功的 SHA 不能代替其原件；后继科学任务必须在自身 runner 真实生成输入。本次不为工程故障盲目再跑旧 6+9+3+12 冷链；先推进独立 polar 新源的实际完整 baseline/LM，后继 hosted 入口再接经过核验的 publisher。

## 来源和复查

- 实际 run：https://github.com/Rogerhu12/math-research-public/actions/runs/45848177096
- 实际 job：https://github.com/Rogerhu12/math-research-public/actions/runs/45848177096/job/140007200479
- controller SHA：`553bc27496d7971fc4009c6ed90fc9c6e88f5887a92d08b3edb6ed3eff5778fa`。
- request SHA：`e4fb7864b0ab4db017ffada1cf6a231d9b82290aa6794adeab0e0bb74f4d5efd`。
- publisher SHA：`5055b47a891bb106557842976a6f4766121edf893605fd7a551a39c223283d29`。
- 保存到 Git 外的完整解码 job log：25,310 B，SHA `9a1d143693e374d85c63ea502489e637b948cd5b94e9b1de814a23668d35705c`。这指实际解码日志的本地保存字节，不冒充 GitHub 原始压缩归档。

只提交此失败结论及源/请求/输出身份，完整日志与缓存不进入 Git 或 Release。
