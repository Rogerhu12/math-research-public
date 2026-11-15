# Observed m10：首次启动的稀疏检出缺项与最小修复

日期：2026-11-15。本文只消费已经完成的公开 Actions 原日志并修改工作流接线，没有在本地执行新人工或科学计算。

## 已观察结果

首次 run [43747845778](https://github.com/Rogerhu12/math-research-public/actions/runs/43747845778)，job 132914985984，source 8ad75d67d80cf6874024badda234dbd1e6682391，结论 failure。

失败发生于工作流在恢复原 source 之后逐文件核 request.source_sha256 的 read_bytes。新工作流的 sparse-checkout 包含根 README、自己及完整 topic，但 request 准确保留了原119项绑定，其中另有旧工作流：

.github/workflows/visible-expanded-pool-soc.yml

该文件未被检出，原错误为 FileNotFoundError。不是文件 hash 不匹配，也不是数学门或 SOC 求解失败。原 m10 driver 尚未启动，因此新七项人工、旧十项只读复用、新 ordinary geometry、原 J 恢复、新 primary 和新 SOC 都为0。不能把这次 workflow failure 写成新分支已尝试。

原完整 job log：93233 B，SHA256 db1935eb3fbe2dce710693c602b5c8239140a287b802de8af81541e02b83ab49。日志保留在 Actions；没有把可重算 payload 入仓库。

## 本次两个真实 pull 与规则

public 实际 git pull --rebase 于 2026-11-15T18:38:24.629000Z 完成，before/after 均为 8ad75d67d80cf6874024badda234dbd1e6682391。

| README | 已读 blob | 本次差异 |
|---|---|---|
| 根 README | 21bd547f56590b7f2dd279d0297efb289a9b2783 | 空 |
| 本课题 README | d0432faff569c8e9af7ed4809847e12880976c11 | 空 |

private 实际 pull 于 2026-11-15T18:38:27.612816Z 完成，before/after 均为 13740b17afafb30dfadf735b1e15d7b43ba06e2e。根 blob 5ba164843b1f5802184178a82d786264404873a3 无差；本课题 README 不存在；QUEUE 本会话唯一行仍进行中。两处规则均未变，不重复阅读原全文。HANDOFF 更新至这次实际读过的提交；下次实际 public pull 最迟19:38:24 UTC。

## 修复范围

仅在新工作流 sparse-checkout 增加上面的旧工作流路径，保持全部原122绑定，不删除前驱来源。topic 中的祖 request 已由完整 topic 检出；源清单没有其它未覆盖外目录文件。

修复后的新工作流为3973B，SHA256 97bb49675db6d7bf5c4d09d3b5c39a16b01bf47d2c9b29dc4ea715b605ad7f92。新 request 只更新这一个工作流绑定，并加入首轮中断的 run/job/source/原因/零执行与日志元数据：59711B，SHA256 68bae58ac467fcd445500af32cb575e81d1bd23574982a4a7a3a9d6cd8825b8f。

两新 Python 源仍完全冻结：

- audit 54699B / 5a69407ea22297c0af8558643f45aa8a50588670697143d5ed23c2b63126685e；
- development 12600B / 918702d5f6a6a25014fe2f0bc8235a60fafa38bc8c87d8c1bb8dbb3d6fdea5ca。

旧117科学依赖、source cfg、reference163、x/y、两池、bank、预算、真实验收门全部不改。下一启动仍是该新七项和固定历史 m10 分支的首次执行，不是重跑已完成科学，也不恢复整个旧优化。新实际结果仍待消费，不能由这项接线修复推断成功。
