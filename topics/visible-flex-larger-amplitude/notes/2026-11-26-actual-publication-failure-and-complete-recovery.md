# 独立03的实际发布终止与原科学设置恢复

## 实际终态和严格未知的部分

[run45811843606/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45811843606) / job139881404152 已实际 failure，API更新时间2026-11-26 12:21:48 UTC。root和solver分别读取终态完整日志（取得的文字113706字符）；以下只记紧凑异常与来源，不将完整日志或科学raw搬入Git。

v2参考准备stage6已真实完成，完整身份及数值边界见[原修复记录](2026-11-26-axisymmetric-import-failure-repair.md)。其后stage7在12:08:57.5885021 UTC真实启动 `complete-independent-axisymmetric-SO3-v2-first-20261126`；checkout `d215cec97446060cb05b6a75a03d94071adb9972`、launcher `a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690`、父reference `3cb4a0ad8bb126a71c1f088e240a70fb7ae3852f7720837f5fb5bd2278efe2f0`。

12:21:42 UTC，控制器真实pull至 `35bfee3c6887163fdf7291c49855c00986200ce3`，双README无差异。随后调用栈到 `run_step → finish_record → publish → Publisher.render`，在单条compact record的58000B守卫抛出 `RuntimeError: One compact record exceeds its declared metadata bound; raw arrays do not belong in summaries`。这句话是守卫固定错误文字，不能据此推断科学数组已被写进摘要。

由实际调用栈和完整run_step控制流可知科学子进程已自然退出；然而原 `followup_returned`、原失败trace事件排在发布之后，所以终态日志和已刊卷没有该子进程的退出码、report、末bundle或Phi。其科学结果**未返回，成功与失败均不能推定**。后继纯reader和两条零闭合step未获执行；不声明它们失败或已产生场。原记录全部保留，不以未知SHA或新run回填旧结果。

## 完整修复范围

原render把 `cleanup_generated.deleted/skipped` 的完整逐缓存清单（含每个缓存目录的全部files路径）放进一条公开记录；列表长度不受科学summary标量选择限制。这里的清理对象本来只是明确模式匹配的可重建缓存，完整清理事实继续留于runner status/journal。

新控制器只在公开副本中把deleted/skipped分别换成实际记录数、已有bytes字段之和及其覆盖记录数、显式files列表项数、完整原metadata的规范JSON字节数和SHA256、原scope。完整来源/输入/命令/输出身份、全部科学标量与错误边界仍保留。未提高或删除58000/60000/95000/10000/200000000字节守卫；没有把raw拆分或换名当参数上传。

新followup模块仅改变返回记录顺序：先save完整实际record，再输出原本就有的真实return事件和至多6000B失败尾，最后执行普通publish与原poll-reset。所有科学子进程命令、输入、行、自由变量、几何筛、源守卫、token隔离、预算与NFF pull/rebase循环均不变。旧完整控制源保原路径，新文件各自有完整body。

|完整新源|字节|SHA256|
|---|---:|---|
|public_actions_followups_compact_metadata.py|26177|`3cb1e706ab43dac6e952ce00b41e83055112d2ee65edb37682d1f05e94f2ee3f`|
|public_actions_controller_parallel03_compact_metadata.py|19006|`68a3e8ce77cddb822d646e20af7d94aff9d682f6174f544a322f5ed92ce2ba53`|

root逐diff审查、solver逐完整AST比较与compile实际通过；这都是编排源码检查，没有科学fixture。唯一题外修改为原 `.github/workflows/visible-larger-axisymmetric-so3-20261126.yml` 的controller路径，必要用途是让新公开run使用该完整修复。

## 03b 真实恢复请求

原request路径更新为 `visible-larger-resume-20261126-03b`，完整新队列 `computations/resume-20261126-followups-03b.json` 只含已刊v2准确参考准备、原完整606e hDelta首方向、纯读出、完整b4d7零Delta首方向与纯读出。source、科学argv、所有预算及工作输出相对路径逐项沿原参数，只给step新ID及明确恢复scope；原03队列和记录不删除。新job必须重建实际warm/参考输入，所有返回identity仍按新run实际读，既有科学结论不重宣、旧未返结果不填造。

02 run45800076687 的39已实际6.164027589999932秒exit1，仅command.json返，report/initial/final缺；40仅缺final setup失败。立即追加已刊ef017纯日志读取器，定位原真实异常，不先猜成profile、导入或数值问题。02无需重建父或重放已返方向。

两条完整实际求解均继续；发布终态、准备成功、静态通过和一次预算都不是本题完成。

## 02 的真实外层异常与进一步纯读取

stage41已实际exit0：原stage39 log SHA `6276a0471e8ae6d22c03cd74046aba82c8ab7641be0a6cf4fd8abe7d1e100311`、4332B，ef017读取产物SHA `e1267a0fb975699ba2b4aa238cc1679c229ede2d4ede75644f5605adc0d24c8b`、6978B。该读取器选择最后Traceback，所以实际仅确认外层启动器 `subprocess.CalledProcessError`；未返回内层第一原因，不能把静态profile矛盾当成已观测异常。继续追加已刊完整ef60 v2纯读取器，读取同一runner已存的全部异常块，仍无F/J、科学数组或重跑。
