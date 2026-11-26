# 实际摘要并发冲突的最小发布修复

**可信度：工程接口的实际 Git 回放；不是数学接受或完成证明。** 本结论只保存源码、参数、实际退出及输出 SHA；完整 fixture transcript、合成账本和本地 bare 仓库均只在 scratch，可由下列命令重生。

## 已发生的问题与边界

实际 run `45848177096/1` 的完整 source cache 已自然完成，尚未开始任何 LM，接受数为 0。root 在 `ab2cd23e93eb8b1c2a04131da693376e61a73b46` 直接编辑了仍活动的同一 Markdown 摘要，纠正其 own-zero 阶段的范围；随后 CI 的 prepare 摘要发布对同文件产生真实 rebase 内容冲突。旧 publisher 只支持 HANDOFF 自己标记冲突，导致发布进程退出，不能归咎于 full-H 数值求解。完整实际退出已另记在 `2026-11-26-6a65-solver-q2-cold-active-summary-conflict.md`。

本次只为这一已发生冲突补独立新 helper。结束的 runner 原件不会被复用，旧活动或已结束科学入口均不热改，旧冷链未重跑。未来生成器必须按**实际阶段**解释模型范围；例如原 Cauchy own-zero 的 1788 列不能被尚未发生的 5292 列 Cartesian 描述覆盖。修正范围应进入新 renderer 的条件分支；root 后续说明放独立勘误，或放下述生成块外。

## 可消费接口

新文件 `scripts/6a65-actual-ledger-markdown-publisher.py`：

```python
ActualLedgerMarkdownPublisher(
    owner,
    marker="<!-- 6a65-polar-ci-rules -->",
    rules_changed_error=ControllerRulesChanged,
).publish(reason)
```

每次 publish 创建一个 helper。`owner` 提供原 v5 同契约的 `git()`，以及 `repo/report/out/run_id/attempt/record/last_rules/total_pull_count/last_sync`。`save(status)` 只把完整实际账本保存到 Git 外，并生成一份未包标记的小 Markdown 结论；不得改 HANDOFF 或其他跟踪文件。helper 自己不读取凭据，数值子进程仍由 controller 删除凭据环境变量。

每个真实 run/attempt 使用新的唯一 Markdown 路径。该路径的自动生成正文放在精确的 `6a65-owned-summary RUN/ATTEMPT begin/end` 两标记内。读取上游时，只重建自己的这一块；标记外文字保留原字节顺序，独立勘误和别的文件不改。遇到旧式无标记文件、不同 run 标记或重复块，明确拒绝，不猜测所有权。

发布前先还原本任务刚生成但未提交的摘要，实际执行 `git pull --rebase origin main`，随后立即比较根 README 和课题 README。每次 pull 的真实提交号写入 HANDOFF 的独立标记，同一次发布的冲突 pull 也列出，完整回执留 scratch。README 有新差异时打印差异，停止数值工作，只发布 HANDOFF 的未审回执；不把新的数学摘要夹带过去。HANDOFF 保持小于 10 KB，摘要小于 100 KB。

若普通 push 被明确 NFF/CAS 竞争拒绝，下一条 Git 命令就是 literal pull/rebase。只有以下全部成立，才允许撤回本次未发布提交并重建摘要：

- 已知提交哈希、唯一父提交、精确本次 subject 均匹配；它是相对实际 fetched `origin/main` 的唯一未发布提交，并且不在上游历史中。
- 提交只改本 run 摘要和 HANDOFF；HANDOFF 去掉自己标记后的文本与父提交完全相同。
- rebase 的 `ORIG_HEAD` 是该已知提交，冲突只在自己摘要或 HANDOFF；没有其他跟踪文件修改。

实际冲突时先 abort 本次 rebase，再在上述证明后将**这一条本地未发布提交**退回其父提交，立即重新 literal pull；从仍在 Git 外的完整当前账本生成摘要。成功自动 rebase 也按同一严格证明撤回本次局部摘要，再用新上游重建。普通 push 重试，不 force，不重写远端历史。外部未发布提交、不同路径改动、网络或权限失败均不当作可安全撤回的竞争。

这不授权手工修改活动生成块。块内旧文字可能被新的实际账本取代；需要永久保留的独立人工解释应在块外或单独的勘误文件。

## 一次真实 bare-Git 核验

`scripts/6a65-actual-ledger-markdown-publisher-fixture.py` 创建本地 bare remote 和两个独立 clone。所有内容都是明确标识的合成接口输入，未访问公有 ref、未读外部凭据、未评价曲面。

fixture 首先普通发布 own-zero 合成摘要。第二次发布改为 prepare，在 runner 已提交但尚未推送时，上游 clone 同时编辑同一生成行、在生成块外加入人工段落、写独立 erratum，并改 HANDOFF 的其他作者正文。实际结果为：

| 核验 | 真实返回 |
|---|---|
| 外部进程 | OS exit 0；0.8639726260007592 s |
| 实际 Git | `git version 2.56.1` |
| 非快进拒绝 | 1 次；紧接的 Git 命令确为 `pull --rebase origin main` |
| 实际同文件内容冲突 | 1 次；日志含 `CONFLICT (content)` |
| 撤回范围 | 只撤回这次唯一未发布 own 摘要/H 标记提交 |
| 当前账本 | 最新 prepare 记录和接受数 0 在最终摘要中，未回退至旧 own-zero |
| 并发外部内容 | 摘要块外人工段落、独立 erratum、HANDOFF 其他作者正文逐字保留 |
| 规则回执 | 冲突前、冲突 pull、重试 pull 的全部实际 SHA 均在 HANDOFF |
| 历史与现场 | 上游并发提交是最终提交祖先；没有 force；没有残留 rebase |
| 不安全边界 | 额外无关未发布用户提交被拒；HEAD 与其文件 SHA 未改变 |

本地合成 initial commit 为 `7c18590b1a235ebaa99b0abcbd456f4b9909b382`，上游并发 commit 为 `b7cd7faa01e864a4e0c6a5cf80bf9fda868df1f9`，最终成功普通发布为 `bf785dd83d59d30143762ad3ff28f8ab36087f70`。这些是本次本地 fixture 的 Git 身份，不是公有 main 提交。

## 可复生命令与身份

从含源码的 topic 执行，`PREFIX` 必须为新的 Git 外路径：

```bash
python scripts/6a65-actual-ledger-markdown-publisher-fixture.py \
  --publisher scripts/6a65-actual-ledger-markdown-publisher.py \
  --prefix /tmp/visible-flex-owned-publication-fixture-new
```

| 文件或实际输出 | SHA-256 |
|---|---|
| publisher，15744 B | `57a597c15dd430b569c50865736292b65b27ab89f719dd19cedb77c04547f462` |
| fixture，11387 B | `7606c04b8acdce633ad17a6ba4449cef89dcb42abcf4217bf4c1a5cd914aa99b` |
| 完整 fixture receipt，只留 scratch | `837cfbc5d16ba05cea77449d8cdb132d03c9a5bc7aaba0aa82c4ee90408463ae` |
| 外部退出回执，只留 scratch | `111b1c414ba6c4239ef23e5c72080a0f0906e8b3dc8f53845c1f6c92533e1578` |
| 完整 Git transcript，只留 scratch | `b98fce37e1efce63aadf41879e6be45062c92ba01e300830e2a11af303484bef` |
| 实际 stdout，只留 scratch | `a51b06e8ef7ee2dcc059fd13060317d91d58b3d49233dad20cc5f000132bbfdd` |

实际时间、临时路径和本地 Git commit 因重生时刻而变化，故以上输出 SHA 绑定本次真实回放，不宣称未来逐字重现。数学输入、全行目标、接受判据和已结束 run 状态均未因这个工程核验改变。
