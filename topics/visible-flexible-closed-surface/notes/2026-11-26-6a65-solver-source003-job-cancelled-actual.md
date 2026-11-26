# source003 的实际 job 取消与未发表的独立 Cartesian 消费

**可信度：真实 Actions API、已发表标量和终止日志；没有新的独立 Cartesian 数值成功结论。**

## 实际终态

`run 45778054176` / `job 139766458381` 的 API 已在 2026-11-26 13:38:40 UTC 读到 `completed / cancelled`。原 job 开始于 `07:48:23Z`，完成于 `13:38:38Z`；主体步骤为 cancelled，post-node 为 skipped。run 的 `updated_at` 为 `13:38:39Z`。不能再用此前静态 report 的 running/waiting 标记称其仍活着。

终止日志最后明确事件是 `13:38:36.4957094Z` 的 `The operation was canceled.`，随后清理父 Python、observer Node、独立 Python 与源 oracle Node 等 orphan 进程。这个时点与 workflow 的 350 分钟时限相符；目前获取的证据仅直接证明取消，未取得更具体的取消原因注解，不把推测当 API 原文。

decoded UTF-8 job 日志共 745841 个字符、6267 行，其 SHA-256 为 `5c2bd23c438e4f10cae4afec4d3b082bf76ee9802bb24dd834deb83b319fc8ef`。只读取有关末段事件，完整可重算日志不入库。

## 仍然有效的最后接受

原 Cauchy 第 13 次真实接受已先前发表：source003 阶段计数为 1，真实子进程 OS exit 0，818.216446112 秒，alpha=.25。

- 实际 state SHA-256：`4c53afcd195cd2fcf135c126056be0992be792e47c309f6db1c333333ec207ce`。
- 实际 stdout SHA-256：`50a36e43cd406aee72f5e824a991f78896091d57fe278c60c4d20ca99079cd91`。
- 完整 R²：`.107699611408683` → `.107699548464153`。
- 原训练样本 metric：`.263954241525386`；曲率：`26.4013529434306`。
- 原训练样本 width：`.828162669137322`；held：`.62818024887322`。

该原目标仍有完整 rho 设计列，不能把整个 Cauchy 迭代记成固定同一个 g。只有后续计划的独立 Cartesian 模型会冻结所消费的实际 g。

## source003 终止前真正发生的下游阶段

source003 冻结提交是 `c0661016195ec9864a1ed27aee1760e0b6c2c354`，inventory SHA-256 `1a535f750ec4f2c5c07686743bccb7dc0d89edcb834b62f8206cc0376cde8fee`。复合入口仍为既定 v2，未热改。

终止日志显示原同场 observer 从 `13:10:43Z` 开始报告真实采样进度。最后可见进度为 `13:19:07.7365998Z`：s=`.9525067725752425`，累计 205857 点，已见最大 metric=`.2639875496504941`、最大曲率=`27.021862680954687`。这些是日志中的累计进度，不冒充一个有外部 exit 0、完整最终文件和已知 SHA 的独立最终 observer 回执。

随后 `13:19:15.8531812Z` 出现已冻结 Python 环境版本 probe 的真实返回：OS exit 0，0.091 秒，stdout SHA-256 `3d6892e7c74edfbbbbceaad819c22f34370a0e9e1f0aac95cbbcb09627039ba4`。这只证明版本 probe 返回，不能记作独立 Cartesian 实验返回。

至 job 取消，没有 `independent-consumer-process-returned` 的实际 Cartesian 实验退出事件，也没有 `independent-scalar-local-commit-awaits-parent-publish`。预定公开路径 `notes/2026-11-26-6a65-independent-Cartesian-45778054176-1-source-003.md` 在实际终态检查仍 404。没有可核的独立 baseline、完整 LM 接受、末态、dense observer 或它们的 SHA；这些字段保持未知，不补造为 0 或成功。不能把 19 分钟经过时间当作完成。

## 接续边界

结束 job 的临时 raw 不再作为可用输入。任何新 job 如要消费这条暖源，必须按已发表源/参数链真实重新生成，并把已见接受仅计作输入恢复；不得借其他 cold 输入或旧源的指标/哈希冒充本次 warm state。

另一个独立 cached Cartesian `run 45825253169` 是其自身公开新 INITIAL 的固定 g 分支，和此取消 job 分开计数。该分支的状态以它自己的实际进程回执更新，不因本 job 取消而虚构失败或成功。课题仍未达完成标准，继续实际求解与完整约束。

## 可复查来源

- [实际 run](https://github.com/Rogerhu12/math-research-public/actions/runs/45778054176)。
- [原阶段已发表标量](2026-11-26-6a65-actions-strong-45778054176-1.md)。
- `scripts/6a65-composite-cauchy-cartesian-observer-v2.cjs`，SHA-256 `1b3ca8e723760d9a0b27358320149d401d55948eab1b26c68b992596afbe3561`。
- `scripts/6a65-resume-cauchy-with-independent-cartesian-v2.cjs`，SHA-256 `83a039b3a2fadec7f2d48b555d1e49aecdb08de82cda6f1125f507a647e13c35`。
