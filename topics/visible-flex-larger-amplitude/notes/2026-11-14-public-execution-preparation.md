# 新公开仓的待执行实际 BVP

2026-11-14，/root。**仅在本地准备，尚未公开推送、触发或运行 Actions。** 新仓首次公开推送被自动审批拒绝；直接用户公开授权尚未收到。此处记录已经做成的具体执行方案，以便取得所需授权后继续原任务，不把配置准备当成科学结果。

## 目标和内容

目标仓库为公开的 `Rogerhu12/math-research-public`，分支 `main`。原私仓的正式迁移通知已读；本地研究和只读同步已迁移，新公开上传仍受真实审批拒绝限制。已有结论按单条本地 commit 保存，尚无本轮成功公开 push。

新增题外文件 `.github/workflows/visible-larger-public-actual-bvp.yml`，只由 `workflow_dispatch` 触发。它执行五个已写完的实际问题，最多四个并发：R225 的 M128 短端 BVP，以及 full、half、trust2、trust2-fixedsize 四个强线问题。四个强线计划保留生产 1280 角、35 参数、完整新 H 非线性尾及原所有接受条件，采用四线程独立 Flow 的已验证 RHS；它们是不同 warm 设计，不是已接受解。R225 计划保 M128/N1536，初始径向步长 .005、短端 .99475、264 节点，使用原生频率 seed、原条件及逐块 CSC 组装，未以降低频率规避资源失败。这里的 half 是原 full 方案的半步；本地后来运行的 margin325 半步是另一个设计，未被混为同一作业。

每个 runner 使用原规则指定的本公开仓 Actions 资源，设置原 Python/NumPy/SciPy/Node 版本。单次平台任务限制为六小时；数值步骤留出末尾上传检查点的时间。若平台截断，必须消费真实检查点和退出状态继续任务，不把平台时长视作本题终止条件。

## 输入与凭证处理

`root_20261114_public_prepare.py` 恢复原 pinned revision 的 91 个输入文件，每件核 SHA。能在当前公开树找到完全相同字节时直接使用；其余从原私仓的准确 revision 读取。12 件输入属于未迁移私题，使用已有 `MR_TOKEN` Actions secret；不把原私题源码目录、私有历史或凭证复制到输出 artifact。

凭证仅由 Actions 环境提供，恢复时通过瞬时 Git 环境使用；数值子进程启动前移除 token 及临时 Git 配置变量。workflow 不包含明文凭证，checkout 不持久化认证。只上传指定计算输出目录，不上传源恢复目录或整个工作区。

原 7 个 A raw 包按现有 recipe 准确重建。该准备过程已在本地真实完成：91 个文件和 7 个 raw 均核验，退出 0，耗时 494.923968356 秒。它只证明可恢复输入；没有将本地准备回执当成 BVP 已启动或已解。R225 计划完全使用当前公开题内文件，明确跳过原私仓依赖及 A raw 恢复；它的264节点 prepare-only 已真实执行，边界残差0、初始collocation最大5.88685e−9，仍未计算大J或取得BVP接受解。

## 输出与继续

workflow 只有 `contents: read`，计算结果及实际失败由 artifact 保存。随后由本题维护者读取实际数值结果，整理必要小包，按每条结论普通 commit/push；每次 push 前仍须实际 pull/rebase 并检查双 README，遇非快进继续重拉重推。没有 force push、自动改根 README 或向他人发送消息的动作。

计划、驱动和恢复器可以直接审阅：R225 的 `2026-11-14-geometry-resume-R225-short-end-actual-actions-plan-r2.json`，四个 `2026-11-14-strong-resume-loop-*-actual-actions-plan-r1.json`，总索引 `2026-11-14-strong-resume-public-actual-start-plans.json`，以及上述 workflow 与两个 `root_20261114_public_*` 源。实际公开授权前，这些均留在本地。
