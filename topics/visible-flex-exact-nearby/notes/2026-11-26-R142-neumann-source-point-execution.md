# R142：实际 PS εtrue 后的四源／全径向观察入口

2026-11-26，visible-exact-astra-198c63d-20261126。

本入口只补原来未成的四个源响应、193 atoms 和5696个全径向 point 子盒。它消费真实已成 PS 的六个 defect 球；原比较 Green 和 defect 不再是新目标。

## 文件与实际前件

- `scripts/fourfold_codazzi_low_centre_neumann_prefix_admission.py` 是纯 metadata／完整 decimal 球准入。它逐项核原 actual/execution/manifest、source SHA、完整字段、gate前缀、原21历史输入、同155/1424/193对象以及 PS 六球与155源母格前缀。PS 保存六球后发生的 late failure 原样保留。
- `scripts/fourfold_codazzi_low_centre_neumann_continuation_owner.py` 执行剩余数学目标，复用已发布的 PS 逐母格三平方模块和独立 point-only Z。
- `scripts/make_low193_neumann_source_point_manifest.py` 仅在实际完整 εtrue 前件存在时，按还缺的目标生成 manifest/workflow。每次恢复保留前一 manifest 的全部文件 bytes/blob/SHA。
- 证明为 `results/R142-supplement-saved-Neumann-source-and-point-continuation.md`。
- 公共 worker 继续使用原 `fourfold_codazzi_collar_volterra_dual_public_worker.py`，不复制另一套重矩阵工作框架。

没有实际 εtrue 前件时，不生成可执行科学文件。完整 εfalse 必须走独立 R149 分支，不能改其 gate。本说明没有预填 actual，也没有新数值结果。

## 已成与尚缺的准确边界

首个合法 NS 运行通常有四源加point五个目标；恢复时只登记尚缺的原目标。科学 kind 为 `complete_R142_low193_neumann_source_point_continuation_v1`，不冒充原 R142 六目标。

每个源母格的三个平方先整件保存、读回并核包含，才推进母格游标。完整155格后，尚缺的六个 comparison 球也先正式保存读回，实际源 lift 才读取这些球。已成的 comparison、实际源或完整母格在恢复时均不重算。

point 只接受做完四个闭子盒的完整 refined cell；保存 weighted/raw最大上界、matching最小正下界和完整 witness。恢复只观察剩余格。为新观察必须物化的全域 Z、左右源协方差和A/B另付真实运行费用；它们不使旧 body/atoms defect 目标重新登记。

两个直接 whole 引用分别为 `completed_prior_low_defect`（原 PS actual/execution/manifest）和 `completed_prior_neumann_prefix`（本次消费的直接前缀）。原 PS 引用在多次恢复后仍可直接取得。所有原执行失败、旧 target数和 failure对象保留。

如果数学输出已经全部齐全，metadata 路由明确禁止重复科学执行；若执行后处理尚失败，完整原结果及该具体状态仍需独立处理，不能重跑五个已付目标。

## 保存事务与预算

候选文件必须完整 bytes 相同、完整解析对象相同，并包含每个新有向标量，才以同一批 bytes 原子替换正式输出。目标标记与正式数学记录同时接受。预算中断只丢弃尚未接受的当前母格／当前point cell。异常 complete=false、proved=false，不删除已保存的完整数学前缀。

NS 新科学预算19600秒、worker child20100秒、公共 job360分钟；原前件保持各自原资源值。Python3.12.14、python-flint0.9.0、320-bit definition／768-bit directed及单线程环境不变。首次从PS manifest产生94个当前输入；以后每次合法自续接增加新的整件 outcome/manifest 引用，不可因容量而删其来源。

生成器调用时明确提供真实 `--previous-actual`、`--previous-execution`、`--previous-manifest`，以及全新 `--manifest-out` 和 `--workflow-out`。未提供实际文件时只返回 readiness。新workflow只在其路径首次push main、run_attempt=1时启动，pip安装行使用YAML block scalar。

## 后续58／224／32

physical consumer 显式识别新 NS kind，先核完整成功低结果、原 PS 六球、四个完整实际源及全径向 point。此后仍执行原 B4–B21 的58门、原224端口和原32 WPN记录，不改变数学公式、真实 mean／height／jump 或输入尺度。

NS 自身的 full CFB、正侧整体逆、七端口、两 WPN 行、负侧连接、真实 ν／phase 和非线性完成标志保持 false。只有对应实际后继门成功，才取得各自结论。
