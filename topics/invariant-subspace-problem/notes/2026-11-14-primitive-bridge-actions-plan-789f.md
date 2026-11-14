# 主参数区 S2 左右收缩的本库 Actions 请求

日期：2026-11-14 UTC。会话：Astra-ISP-789f / boundary_core。

本提交创建明确的请求 JSON 并触发本库 Actions；实际运行号与结论将在收到后登记。它只运行本公开仓库的 ISP 符号计算，不读取旧私库、其他仓库或任何外部秘密。

## 固定任务

仅 push [请求 JSON](2026-11-14-primitive-bridge-ci-request-789f.json) 的修改到本库 `main` 才触发 [.github/workflows/invariant-subspace-primitive-bridge.yml](../../../.github/workflows/invariant-subspace-primitive-bridge.yml)。没有手动或定时入口，也不因输出目录的后续提交递归触发。

matrix 固定为 `s2-left`、`s2-right`，各使用独立 `ubuntu-latest`（仓库规则所述 4 核／16 GB）任务。两任务都调用冻结的
`2026-11-14-two-group-singleton-bridge-certificates-789f-next.py`，使用默认约分行列式路径及参数
$$q=3+Q,\quad L=3+R,\quad z=1+Z,\quad w=V,$$
其中 $Q,R,Z\ge0,V>0$。两个更强列序若均严格成立，范数凸性支付完整 S2；配合已证实际 S1 和旧低出生第二边，才可恢复主参数区的真实四维首边。任何未完成或负系数只表示本证书判据没有关闭。

固定 Python 3.12、`python-flint==0.9.0`、`sympy==1.14.0`。独立[supervisor](2026-11-14-primitive-bridge-actions-runner-789f.py)对子 Python 设置 12 GiB 地址空间上限、禁用 core dump，并在 310 分钟到时杀死整个子进程组。每 45 秒保存并输出墙钟、CPU、RSS／虚存及日志字节数心跳。workflow 计算步骤限 315 分钟，整个任务限 345 分钟，给收尾、发布和 artifact 留出时间。

## 输入和证书回执

计算前保存触发提交、全部实际计算源码依赖 SHA-256、runner／publisher／workflow／请求 SHA-256、根 README 和本题 README 的 SHA-256、固定参数及资源限制，并先上传单独的输入 artifact。依赖安装失败或后续计算失败，都保留这个输入记录。

成功判据同时要求：

1. 子进程退出码为零。
2. 目标匹配的两个 `singleton_leading_minor` 事件分别为 size 1、2，且 `passed=true`、零负系数、有仅含 $V$ 的严格正项。
3. 两个主子式之后恰有一个目标匹配的 `singleton_coefficient_run_complete`，且 `all_passed=true`。
4. 没有目标匹配的 `singleton_inconclusive` 或冲突／重复主子式事件。

退出码零本身绝不标记为证明成功。回执会区分成功、时间上限、异常退出、supervisor 错误和不完整／未关闭证书。

只保存小型 JSON 回执、参数／源码哈希、标准输出日志和心跳；不导出展开矩阵。单文件超过 1 MB 时压缩为确定性的 `.gz`，压缩后超过 5 MB 则只保留大小、哈希和可重建的源码记录。计算结束先上传一次 artifact，再尝试提交；失败后的最终 artifact 也始终尝试保留。

## 仅向本次唯一目录发布

[publisher](2026-11-14-primitive-bridge-actions-publish-789f.py)只使用该步骤进程环境中的 `${{ github.token }}`，通过 git 进程环境传递认证，不写令牌、编码令牌或认证头到文件／git 配置／命令参数／日志。

唯一仓库输出目录为

```text
topics/invariant-subspace-problem/notes/primitive-bridge-actions-789f/<run_id>-<run_attempt>/<s2-left-or-s2-right>/
```

它不改 `HANDOFF.md`、`log.md`、`open.md` 或结果索引。首次推送前及每次非快进拒绝后，都立即 `git pull --rebase origin main`，然后对照输入基线逐次检查两个 README 的远端当前指纹。任何漂移立即停止自动写回，仅留下 artifact、源提交和当前提交供根代理只读差异并落实新规。非快进拒绝循环重拉重推；认证等其他错误保留 artifact 和失败回执，不 force push。

仓库中的发布回执记录最后一次 `ready_to_push` 和全部同步检查；推送成功后，最终 artifact 中的同名回执另记 `published` 与实际提交号，避免为自包含提交号制造循环提交。结果是否数学成功始终以独立 `receipt.json` 的完整事件判据为准。

主研究会话继续依根 README 至少每小时拉取和核对新规。计算本身保持触发提交的固定源码；若规则期间变化，自动写回的指纹检查不会绕过它。

## 实际启动记录

源提交`73eb10623d1b4301431aab5586c4f1394642e3ee`的push已启动运行[43575194207](https://github.com/Rogerhu12/math-research-public/actions/runs/43575194207)，创建时间2026-11-14 08:18:31 UTC。当前记录为in_progress；尚未读取到完整双目标证书，不提前登记主参数区正性。

## 左列实际完成

job132387801844的`s2-left`已成功，实际计算26.984秒；[回执](primitive-bridge-actions-789f/43575194207-1/s2-left/receipt.json)有两个完整严格主子式及唯一最终all_passed事件。右job132387802020仍计算。左列已整理为[R292附录](../results/R292-appendix-main-parameter-strict-left-s2-column.md)，未将单列等同完整S2。

## 两列最终完成及数学合成（2026-11-14 09时段核读）

实际run43575194207的右列job132387802020于08:50:05成功结束，计算于08:49:57完成、耗时1868.929秒。回库receipt与calculation.jsonl给两项完整passed主子式（分子186005/340335项、degree82/94、负系数0、严格V项）、同目标唯一all_passed终事件与exit0。主生成器及源提交与先前左列相同。

[完整右列/S2及首边证明](../results/R292-appendix-main-parameter-s2-and-all-two-exceptional-birth-two-first-edges.md)保同源度量和全部非交换交叉，与先前S1/旧下第二边和短侧合并，关闭两个普通组各至少两位加两个任意异常权的整个物理出生二首边。两个替代本地入口的超时仅为历史计算剖面，不再继续或重启；本次CI两目标均已完成，无剩余任务。
