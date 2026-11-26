# 新 epoch：实际重生 gap 支后继续 q=2 全 H 求解

状态：**执行配方与发布接线准备**。数学 helper 的 126 非零列核验见独立 note；这里没有重跑旧科学输入，也没有把语法 / 发布格式检查称作 5292 列接受。

## 实际输入链

新 workflow 只由 `ci-requests/6a65-gap105-q2-full-normal-cold-20261126.json` 的 push 触发，`ubuntu-latest`，350 分钟，NumPy 2.3.5 / SciPy 1.17.0 / Node 22.23.5。部分克隆保留触发提交，先 unshallow，再查触发提交确为 origin/main 祖先；不把旧 depth=1 历史问题带入新 run。

所有数值源码、candidate 和物理 recipe 在首次 live pull 前复制到 runner 的冻结目录。新 run 真实重生 prefix、原 factory 的 own-zero INITIAL/value、完整 source cache，然后逐个子进程执行原 single 6、joint 9、refined 3、q=1 area 12 个尝试。每个返回只依据实际保存的父态、source、prepared、entry 字节与计数继续。如果重生中有真实拒步，该阶段如实记载，再进入下一个已明确的新模型；不伪称重现 30 个接受。

随后，独立 q=2 全物理法矩阵入口先做自己的完整 baseline，再尝试至多 40 个完整步骤。只使用本 run 尚存的实际非零父态。全部 5292 列、两网格的原 13 行、q=2 面积行、原固定 $g$ 和共同 $\lambda S$ 保留；预条件默认 $\eta=\lambda$，增广 LSMR 的 damp 为 0。旧段重生不算新科学接受，新段使用 `fullBandAcceptedSteps` 单列。每步保留完整目标重评、真实试步、物理 normal 残差及组装 / 带因子成本。

## 结论发布和同 job 保留

发布工作树只更新**一个小 Markdown 结论页**及本 run 的独立 HANDOFF marker。完整 JSON ledger、报告、checkpoint、source cache、日志与数组只留 RUNNER_TEMP；本页不复制可重算的 Actions 输出。每个实际返回的结论普通 commit/push，随后再推进下一步。MD 写出本步实际 baseline / 返回、实际退出、计数、run、参数与输出 SHA-256。

复用已实际核过的 v5 Git/publish/process 方法，Git 身份在初始化持久配置。数值子进程去除全部 publication token 和 Git credential 环境。运行中及等待中每 45 分钟真实 `pull --rebase`；每次 pull 立即查双 README，实际 SHA 写进 HANDOFF。NFF/CAS 按已验证的明确文本分类立即 rebase 重试，不 force；相同的 own marker 重复可合并，不同内容不随意删除。HANDOFF 10KB 限制保持。

真实自然 exit 0 但 full-normal 拒绝时，写真实未接受状态，保留当前数组，并等待匹配的小包。预算耗尽也保留同 job 输入。receiver 只允许当前模型追加有限尝试或明确 release，严格匹配 run、attempt、epoch、request、state、prepared；literal pull 后再次核 packet SHA，防止将 fetch 时的旧包用在变化后的工作树。已拒绝的相同模型不重复运行。当前旧 q=1 job 的 receiver 没有修改。

## 本次实际接线检查

新 controller 编译实际成功。独立小 fixture 自然 **exit 0**：核对 21 个实际源码 pin、3 个 Bash heredoc block 的 `bash -n`、350 分钟 / unshallow / ancestor / 入口绑定；用明确合成对象实际调用 Markdown renderer，验证 public 测试目录只有一个 `.md`，完整 ledger 在目录外，合成失败前保存态不会被写成自然退出。合成 MD 为 2443 字节。此 fixture 没有网络、Git 发布、数值 child 或研究接受，没有重做旧 Git 并发实验。

```sh
python 6a65-gap105-q2-full-normal-controller-fixture.py \
  --controller /path/to/6a65-actions-gap105-q2-full-normal-cold.py \
  --request /path/to/6a65-gap105-q2-full-normal-cold-20261126.json \
  --workflow /path/to/6a65-gap105-q2-full-normal-cold.yml \
  --scripts /path/to/topics/visible-flexible-closed-surface/scripts \
  --output /outside-git/q2-full-normal-controller-fixture01-report.json
```

| 文件 | SHA-256 |
|---|---|
| 新 cold controller | `553bc27496d7971fc4009c6ed90fc9c6e88f5887a92d08b3edb6ed3eff5778fa` |
| 小请求 | `e4fb7864b0ab4db017ffada1cf6a231d9b82290aa6794adeab0e0bb74f4d5efd` |
| 新 workflow | `1e8ab32d543496c0eb1a58d6ce37fa26ff31341bdc1f16a74ad5582a598f38fc` |
| 接线 fixture | `9a4082d8252051e32c65943168aebab11479b5a10150eeb48635e53ca50a8c26` |
| 实际完整 scratch fixture 回执 | `ef3202384fc1daf03cd85b8b7c7062bd4f800a5f53dd2ade2d36dafb3638b886` |

实际新 Actions run 尚未在本 note 中报告；发布后只有其实际返回才能补接受、曲率、面积或完成判断。两个参与目标的网格不是第三独立观察，连续 metric / reach / 全时间证明仍须另行支付。
