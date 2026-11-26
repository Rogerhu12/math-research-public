# 完整 Cartesian v5 的同方程块预条件入口与实际发布合同

日期：2026-11-26。会话：Astra-visible-flex-6a65。本文登记可执行的新入口与验证边界；不登记尚未发生的 7760 列大模型接受，不把 Actions 启动或结束当作课题完成。

## 1. 这次真实改变的范围

R239 已给出完整代数证明。新线性入口用每个角通道的实际径向主块构造预条件器，并保留完整物理 Jacobian、跨角通道耦合、全部十三行残差和原 Sobolev LM 二次项。设原方程为

$$
\min_\delta \|J\delta+r\|^2+\lambda\delta^\mathsf{T}S\delta,
\qquad S=L_S L_S^\mathsf{T}.
$$

新预条件器为 $P_m=H_m+\eta S_m$，$\eta=0.1$；取 $T=L_P^{-\mathsf T}$ 后实际解增广问题

$$
\min_z\left\|
\begin{bmatrix}JT\\\sqrt\lambda L_S^\mathsf{T}T\end{bmatrix}z-
\begin{bmatrix}-r\\0\end{bmatrix}\right\|^2,
\qquad \delta=Tz.
$$

调用 LSMR 时额外的 `damp=0`。不能把上述正则项换成 $\lambda\delta^\mathsf{T}P\delta$。每次返回还实报原物理坐标正规方程残差、原正则能量、组装成本与迭代成本。固定有限迭代上限下，新旧求解器给出的近似方向可能不同；完整非线性 Armijo 试步才决定是否接受。

同一新 job 中先由公开 no-z 配方真正计算原 Cauchy INITIAL 和原场密观察，再固定该实际 $g$ 与源场运行 Cartesian 模型。新分支不导入已结束 job 的原件、缓存或接受计数；此前 v4/cold 的一次接受也不算新 v5 的已接受前缀。请求为 20 次完整尝试、`prior_observed_accepted=0`。若完整尝试合法返回但无接受，计数不增加，真实密观察和标量仍按当前合同处理。

训练网格、观察网格、7760 列基、全部十三行、曲率及几何 guide、每步非零状态续算和只读缓存身份来自既有完整入口。缓存必须在同一实际 run/attempt/source epoch 内生成，源、$g$、网格、参数配方、算子字节和缓存形状逐项匹配。不能取 ended-run 的 raw 来绕过这些检查。`minImmersion` 保持原定义：目标归一化 Gram 行列式，即面积比平方。

## 2. 精确源码与请求身份

下表 SHA-256 均以完整 UTF-8 文件字节计算；Git blob 不是 SHA-256 的替代名称。

| 文件 | SHA-256 |
|---|---|
| `scripts/6a65-cartesian-exact-channel-blocks.py` | `d292b35b6121598470968937dab983724aa5250e24ba87942cc50e2e2ec90892` |
| `scripts/6a65-cartesian-independent-experiment-v5.py` | `3894552b05482c6a70faea1c50d0ae6e6451a72b3d5a04f3728155df51aeba1e` |
| `scripts/6a65-actions-cartesian-channel-block-v5-20261126.py` | `5055b47a891bb106557842976a6f4766121edf893605fd7a551a39c223283d29` |
| `scripts/6a65-actions-cartesian-channel-block-bootstrap-v5.py` | `36384dc11e5cfba77f92e09dd2c006b672240f1cd7c62779727237638c7777e6` |
| `ci-requests/6a65-cartesian-channel-block-recipe-20261126.json` | `a5f2880cf52df4c42af2432b8187a7d0b58a8c6d7b60a1b64d05e2450fd0874c` |
| `ci-requests/6a65-cartesian-channel-block-v5.json` | `59e024de320132e79fee3741fad9d6d9662253ca974e20ab34a8cc68a979b69b` |
| 仓库根 `.github/workflows/6a65-cartesian-channel-block-v5.yml` | `5c797e33454977ef9e3f417a739b79b97aae538f58ead359493f574302a1eee7` |

初值仍使用公开 candidate `2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json`，SHA `9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d`；原 Cauchy recipe SHA `4c929d16fa8304918338df1b7952f5219ab12eaf985a450f86ac022f0e4ac517`。原工厂 `value` 的末位置参数是完整输出 JSON 文件名。新 bootstrap 也显式校验它自己、continuation controller、数值入口、helper 的请求哈希，之后由 frozen snapshot 继续执行。

## 3. 小型实际验证与大模型未支付部分

新 helper 和有限 fixture 已在执行环境失联前真实运行：91 个非零 Cartesian 系数、360 点、4680 行，实际自然退出 0。实际报告 SHA `ceb0a8cd4aadc0d8ce4ede85e5c35f44a91f5a39601fec14b7a2a7f9a2eede8d`。主块相对误差 $5.865\times10^{-16}$；原正规方程稠密对照相对方向误差 $1.667\times10^{-15}$；增广伴随差 $1.419\times10^{-15}$。该有限 fixture 没有产生 Cauchy 大模型非线性接受。完整命令、成本和精确报告身份已在另条有限核记录中登记，不再重算。

同一 v5 controller 的真实本地 bare-Git fixture 已运行：实际制造 NFF、HANDOFF 并发内容与逐字相同 own-marker 重复；保留 root 非 marker 文本，立即 pull/rebase 后推送成功。实际报告 SHA `36540a74542d517aa460a9be219e49491695ecec3fa4e0ba7f41c60cd623a496`。README 差异回执先写 HANDOFF 并发表，再明确停下等待 root 应用规则；权限或网络错误不当作 NFF。不同内容的多个 own-marker 仍保留并明确拒绝，需要 root 判决；没有把未运行的额外分支测试说成已通过。

v5 数值入口在失联前的 `py_compile` 与 `--help` 已真实通过。本文列出的新 bootstrap、workflow、请求是在执行环境 unavailable 后依据已读取的公开原文作受限文本替换和逐项接口审核；它们尚未在本地执行 Python/YAML 语法检查。workflow 在任何数值生成前显式执行四个新 Python 文件的 `py_compile`。这项未来运行不能提前登记为成功。新的完整 7760 列块组装、完整 LSMR/试步、第二步只读缓存复用与最终密观察也尚未支付，必须等待真实新 run 回执。

## 4. 发布、规则与原件保留合同

新 bootstrap 只继承旧 ColdController 的公开 no-z 配方冻结、原工厂调用、原场观察与小摘要抽取。发布改为调用上表已核 v5 publisher 的原方法，提供明确的 `report/record/save/git/last_rules/total_pull_count/own_count` 接口；生成原源时 `own_count=0`，未实例化任何虚构的 Cartesian baseline。进入真正 continuation 后才使用自己的完整模型 schema 与计数。

每次实际 pull 检查根 README 与本题 README 的差异，并把该次实际提交 SHA 写入本题 HANDOFF 独立 marker。相同字节的自己 marker 允许合并；其他会话内容不删除，不把不同收据伪装成重复。每次新接受和失败均普通 commit/push，指定并发 ref 失败立即 pull --rebase 再推，绝不 force。45 分钟数值运行 watchdog 继续做真实 pull 与回执；仅 fetch 的等待轮询不冒充 pull。

原 Cauchy 和后续数值子进程去掉 `GH_TOKEN/GITHUB_TOKEN/MR_TOKEN/VISIBLE_FLEX_TOKEN/M12_RECOVERY_TOKEN/CART_COLD_TOKEN/CART_CONTINUATION_TOKEN` 及 Git 配置注入环境。凭据只留在显式发布父进程。全部原始数组、源缓存、完整向量、checkpoints 和子进程日志留在该 runner 的临时目录；没有上传 artifact/release/Git raw。

新 workflow 逐字保留已修复的部分克隆、unshallow、trigger ancestor 和精确 HEAD 核对段。它只由自己的 workflow/request 路径或显式 dispatch 触发；日常标量发表不会再启动副本。350 分钟平台期限仍可能在某次尚未返回的完整步骤中结束；这种情况只登记实际可见的退出/取消和已发表阶段，不补造缺失状态、不称完成。

复算入口由该 workflow 调用：

```bash
python topics/visible-flexible-closed-surface/scripts/6a65-actions-cartesian-channel-block-bootstrap-v5.py \
  --request topics/visible-flexible-closed-surface/ci-requests/6a65-cartesian-channel-block-v5.json \
  --directory "$RUNNER_TEMP/visible-flex-cartesian-channel-block-v5-$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT"
```

此合同用于推进真实完整优化；它本身不支付连续度量、reach、全部时间嵌入、同 $g$ 网格收敛或强固定帽门槛。
