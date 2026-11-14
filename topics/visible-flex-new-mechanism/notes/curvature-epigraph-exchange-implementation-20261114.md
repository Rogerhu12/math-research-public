# 固定度量预算下的实际曲率 epigraph：分批二 jet 与行交换实现

**状态：新独立实现已完成，尚未执行本版本人工 CLI；没有本地研究几何评价或求解。** 已发布的九输入 metric-exchange、R103 helper 和全部旧物理模型源码不改。新增源码为：

- scripts/frame_curvature_epigraph_exchange.py；
- scripts/frame_curvature_epigraph_exchange_audit.py。

本说明消费 notes/curvature-PSD-row-exchange-integration-plan-20261114.md 的已核方案；实际曲率公式依据 results/R103-actual-metric-curvature-semidefinite-gates.md。本轮真实研究仍只允许公开 Rogerhu12/math-research-public 的 Actions。

## 1. 唯一来源和新目标

第十输入是 run 43642966285 的完整 metric-exchange 输出：

- notes/actions-43642966285-1-metric_epigraph_exchange/metric-epigraph-exchange-audit.json.gz；
- decoded 2,111,864 字节；
- decoded SHA256 c7b6b195cab755b425ccce41bf738ba05a30b65d329ed9b14b93f5211866d78e；
- 保存物理态 e407a21488257097f60073f7e46e19f987dc963760957040ee7254a02889beb4；
- 完整固定度量 fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6；
- 163 个物理系数与原 b0、帽高仿射门、参数盒均保持。

该次 384/768 网的实际度量误差分别约 0.2664111742/0.2671465317，最大主曲率分别约 73.35984304/73.35982955；两网已有内条带和镜像等物理门通过。旧 raw metric delta 约 0.26640845723 未覆盖真实最大误差，原失败记录保留。这里只引用已发布 JSON，不重新计算这些候选。

新阶段固定

$$
\bar\eta=\frac{167}{625}=0.2672,
\qquad
\tau_*=\frac{61}{1000},
\qquad
\lambda_{\rm ref}=100.
$$

优化唯一辅助变量 $\zeta=\lambda/\lambda_{\rm ref}$，目标 $\min\zeta$。它不是第 164 个物理系数，不能进入 canonical physical state。旧 metric delta 不参加本阶段求解。

初始 $\lambda$ 按第十输入两档已存曲率最大值 $K_{\max}$ 明确赋值：

$$
\lambda_0=K_{\max}+10^{-6}(1+K_{\max}).
$$

记录原两档数、这次二进制评价、$\zeta_0$ 及乘回 $\lambda_{\rm ref}$ 的末位；新的全值网还必须独立通过该界。若新求值超出它，停止并留下诊断，不能悄悄改变第十输入或旧辅助失败。

## 2. 十一组约束及解析导数

写 $A=X_s$、$T=X_\theta/a$、$w=A\times T$、$q=|w|$。以实际位置二 jet 构造实际第一基本形式 $I$ 和 $K=q\,II$。每一点使用

$$
\widehat H_\pm=\zeta qI\pm \frac{K}{100}.
$$

两个矩阵分别要求迹、行列式非负，共四行。这准确表达该点 $\max_i|\kappa_i|\le100\zeta$，前提为独立正则性 $q>0$。实现不以目标单位度量替换 $I$，也不将法向固定。

若 $\widehat H=(h_{ij})$，辅助列为

$$
\partial_\zeta\operatorname{tr}\widehat H=q(E+G),
$$

$$
\partial_\zeta\det\widehat H
=q(Gh_{11}+Eh_{22}-2Fh_{12}).
$$

物理列完整采用

$$
d\widehat H_\pm
=\zeta(dq\,I+q\,dI)\pm \frac{dK}{100}.
$$

其中 $dq$、$dI$、$dK$ 都包含当前 $X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}$ 的参数导数。库保存选中点的七个中间导数 $dq,dE,dF,dG,dK_{11},dK_{12},dK_{22}$，辅助量变化时只重组小矩阵，不重新评价研究几何。

前七组为：

1. $\bar\eta-e-f^2/\bar\eta\ge0$；
2. $\bar\eta+e-f^2/\bar\eta\ge0$；
3. 当前 signed z 至少 $10^{-4}$；
4. 当前球 $|X|\le101/100$；
5. 当前上条带侧；
6. 当前下条带侧，内半宽固定 38999/100000，外部报告仍单列 39/100；
7. 既有镜像必要点对门 $z^2|X_s\times T|^2-\tau_*^2(X_s\times T)_z^2\ge0$。

这里 $e=|X_s|^2-1$、$f=X_s\cdot T$。前七组对新辅助 $\zeta$ 的导数均为零。帽高仿射门与原参数盒另交给 SLSQP，不合并进局部行池。

曲率行容差为 $10^{-9}$，独立实际主曲率覆盖容差为 $10^{-8}$。其余已有门及其容差沿用；这两类容差只用于浮点求解选择，不是连续误差界。

即使在新 $\lambda$ 下四行都过，仍单独报告最终目标 $\max|\kappa|\le1000/61$ 是否通过。曲率上界与镜像点对都不足以认证全曲面 reach 或嵌入。

## 3. 全值网、行池、预算

完整值网沿用第十输入同一 160 个准确径向节点和 384 个完整周期角点。每个新物理参数向量都重新检查全部十一组、帽高、盒、正则性与独立范数。池只缩减发给 SLSQP 的 Jacobian，不缩小候选的物理判定网格。

初池每个径向层取七旧组的 2/2/1/1/1/1/1 个最紧角点，四曲率组各取一个，总数至多 2080。随后每组补每层至多两个遗漏违反点，另补全组至多 32 个最坏遗漏点。旧池行不移除，索引、哈希、理由、各组全网及遗漏计数均入 checkpoint。最大池 12000 行。

这次明确将最大交换轮数从 6 改为 20：上一实际只有 12 major/13 physical、优化约 15.6 秒就先触发六轮上限，不能把它解释为时间耗尽或收敛。全部交换轮共享：

- 至多 80 个 major iterations；
- 至多 120 次完整值网物理评价；
- 300 秒优化活动时间。

准备十输入、恢复模型、首轮完整值与首批 Jacobian 的耗时另列；总进程壁时从 main 入口计起，异常也保存已耗时间。各轮不能重置这些预算。每轮池大小在一次 minimize 调用内固定；发现遗漏违反行时，以已验证的 callback 异常路径退出、记账、扩大池。新一轮如需给辅助 $\lambda$ 重新赋覆盖界，只改变辅助量，原 trial 及其失败仍保留。

第一次全网初态未通过全部固定预算/物理/曲率辅助门时，不启动优化。

## 4. 完整二 jet 分批不是分片曲面

一次 derivative refresh 把 160 个径向层划为每批最多 16 个 owned 层，再加入 $s=0,L$ 查询端点。每批继续使用同一完整 384 角网、同一个周期 $\Pi$ 与已经修复的查询无关共同高度原函数。

调用的是原 SingleQProblem.geometry 的 full_two_jet_jacobian=True。必须返回：

$$
X,\ X_s,\ X_\theta,\ X_{ss},\ X_{s\theta},\ X_{\theta\theta}
$$

及其完整物理 Jacobian，另含 $T$。先把每一批的全部普通位置二 jet、$T$、共同 center、完整径向 metric 与同态全值缓存逐项比较，再只抽取该批拥有的池点参数导数。比较上限为声明的 $5\cdot10^{-12}$ 相对浮点回放容差；它不是已证明的求积误差界。

每个 owned 径向索引恰好属于一批。重复加入的 0/L 只是查询入口要求与共同规范的保护，不能重复写入同一参数行或改变表面。临时大 Jacobian 在该批提取后释放，保留下来的只是选中点中间导数。所有实际批次、最大差、返回张量字节量与 RSS 都记录。

在 160×384、163 物理变量下：

- 单个全网三向量 Jacobian 为 240,353,280 字节；
- 七个完整二 jet Jacobian 合计约 1.68 GB，尚未计中间数组；
- 18 查询层的一组三向量 Jacobian 为 27,039,744 字节，七组约 189 MB；
- 十一组全网普通行值约 5.41 MB；
- 2080 行、164 列的初池 Jacobian 约 2.73 MB。

实现从不构造完整十一组约束 Jacobian。实际总 RSS 仍包括旧 field/grid 缓存、周期算子、抽点副本与 SLSQP，不能把 189 MB 说成进程峰值上界。小人工对照可故意使用单一全 toy 批；metadata 如实记录是否曾请求覆盖全部 toy 径向点，不冒充实际大网分批。

## 5. 两类 best 和最终精化

每次完整值评价分别保存：

- best_physical_curvature_point：通过全部既有物理门和固定 $\bar\eta$ 的真实曲率最小态；
- best_auxiliary_feasible_lambda_point：再通过当前 $\lambda$ 的四 PSD 行与独立 $\max|\kappa|\le\lambda$ 的最小辅助态；
- best_auxiliary_feasible_curvature_point；
- lowest_lambda_trial_may_be_ineligible。

最终选择第一项；当前 raw $\zeta,\lambda$ 原样保存。不存在“把辅助量调大后倒改旧接受历史”的步骤。若优化返回错误、预算或没有收敛，仍可审计已完成筛选的 best；status 和 solver/error 不能被“有 best”改写成成功收敛。

最终严格冻结同一完整物理态、同 g、同 b0，在 384 与 768 角网独立评价 metric、主曲率、镜像、球、条带、帽高和全部端口位置二 jet。独立主曲率使用实际 $I$ 的 Cholesky congruence，避免只看 PSD 行代数余量。更细网的新违反如实为失败，不能用工作网通过替代。

## 6. 人工检查范围与当前状态

本版本 --check-only 编排：

- 十一组完整方向 Jacobian（包括辅助曲率列）；
- 分批与单 toy 批的选行 Jacobian、普通六 jet 一致；
- 辅助量独自变化复用几何与中间导数；
- 遗漏曲率行被全网识别并加入；
- 实际小数组 SLSQP callback 触发行交换，预算共享；
- 实际物理更好但辅助覆盖失败的分账；
- 正则失败不作平滑替换；
- 注入 batch 异常仍保存已有合格 best；
- 完整十输入人工 IO、同态冻结、精化、summary 绑定；
- 错 SHA、错 full-state、错准确网格、来源 finer physical failure 拒绝。

CLI 本身不调用任何真实候选。当前环境断连，完整源码通过 README 的小文本 GitHub 集成例外保全为未挂分支 blobs，**没有获得本版人工执行回执**。部署应在同一公开 Actions job 先运行这项人工 CLI，再进入唯一实际曲率阶段。

## 7. CLI

从 topic 目录先执行：

    python scripts/frame_curvature_epigraph_exchange_audit.py --check-only --out "$RUNNER_TEMP/curvature-exchange-development.json"

实际入口保持原九个输入标志及 SHA，增加：

    --exchange-audit notes/actions-43642966285-1-metric_epigraph_exchange/metric-epigraph-exchange-audit.json.gz
    --expected-exchange-sha256 c7b6b195cab755b425ccce41bf738ba05a30b65d329ed9b14b93f5211866d78e

完整参数名称为 input/anchor-input/short-audit/height-audit/prior-joint-audit/resume-audit/epigraph-audit/trial-audit/dense-audit/exchange-audit，各自 expected 输入 SHA 的名称沿原入口；输出例如：

    --out "$RUNNER_TEMP/curvature-epigraph-exchange-audit.json"

真实入口检查 GITHUB_ACTIONS、精确仓库名与 topic/notes 路径。十个已发布输入的 decoded 字节哈希、旧源码、全布局、准确系数、来源嵌套、完整 g/b0、网格及双方物理门均核后才进入新几何。完整 report 保留 canonical 和分布；同 stem -summary.json 仅删大型重复内容，保来源哈希、全局/分区科学量、所有门、轮数/时钟、内存与辅助失败，绑定完整输出字节 SHA。
