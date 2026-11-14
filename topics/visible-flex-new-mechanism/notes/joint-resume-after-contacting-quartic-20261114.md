# 四次阶段已完成后的单次 joint 恢复：拒绝接触初态，回退原可行高度态

日期：2026-11-14。状态：独立新 runner 与针对性人工入口已编写，**尚未把新的人工检查或恢复求解声称为通过**。本稿不修改任何已冻结求解器；新文件为 [frame_height_joint_resume.py](../scripts/frame_height_joint_resume.py)。研究评价仍只在 `Rogerhu12/math-research-public` 的 GitHub Actions 执行。

## 1. 实际需要恢复的阶段

公开 run `43634358250`、source `fdc99b7dc19ed97e996a51b8d68396c415d91bed` 的[完整报告](actions-43634358250-1-quartic_joint_audit/quartic-joint-audit.json.gz)和[科学摘要](actions-43634358250-1-quartic_joint_audit/quartic-joint-audit-summary.json)已经落盘。完整解压字节为 3,183,049，SHA256 为

`e344e6e0a62be10dfa8dad4f52e4b889191f462b97bb19dd4b1cc0283f6f33dc`。

实际只完成了固定 $T,a$ 的九高度四次优化：46 次目标评价、约 $.173$ 秒，度量成本从 $.0315875456092$ 降到 $.0282824246421$。随后 joint 的 `minimize_invocation_count` 准确为 **0**。

阻断原因不是联合求解迭代失败，而是四次最小点落到分离边界：在 joint 工作网格的 $t=.375,\theta=0$，真实重构的 signed $z$ 为约 $-1.34566\times10^{-8}$，低于原有 $10^{-9}$ 入门容差；384 角的对应细评价恰为 0，768 角约为 $3.52\times10^{-13}$。这些评价没有给连续误差界，但已足以说明“不带正裕量的接触初态”对评价规则敏感。即使放宽数值容差，也不能把不同材料点的镜像接触当成良好嵌入初态。

已发表的几个完整参数身份必须分清：

| 阶段 | 维数 | canonical physical SHA256 |
|---|---:|---|
| 原 accepted height | 162 | `f198ba74dcf3644569bf1ed78eecbc48a0f21ec421205d46a6b159cb00ff0f56` |
| 已完成 quartic 选中态 | 162 | `86480e39e2cb1e8f52237efe97ecd097d1c4830873320f566f351185ba7f37f8` |
| 上项零 $Q$ 扩展后的 joint 初态/最终未动状态 | 163 | `d92e2e659654093e86b92f37d70a49ffb9453a572a386d63da7212b71c79ad37` |

162→163 改变参数空间及身份定义；零新增系数表示同一场，不能因此要求两个 canonical SHA 相同。原 accepted 的细网 signed 高度最小值约 $.0142571$，所以它是有实际来源的回退候选；恢复 runner 仍会在本轮当前网格重新检查，不凭旧摘要直接接受。

## 2. 五份输入与严格复用范围

新 runner 先调用原四输入 loader，完整重建旧 selected、原 enriched $c_0$、short bounded 场及 accepted height 态。第五输入是上述已经完成的 quartic/joint **完整**报告，另有明确的解压字节 SHA。

第五报告必须满足以下条件：原四个输入字节绑定一致；旧 producer 源码 SHA 表一致；完整 accepted 162 态、quartic 的准确 binary64 高度值和两种准确增量、post-quartic 162 态逐项重建；随后零 $Q$ 扩展必须等于报告中的 163 初态。旧 joint 的调用数必须为 0，研究模式还限定为已经观察到的 `initial-joint-height-or-box-gate-failed`。若 joint 已经调用，新 runner 拒绝把它当成尚未执行的恢复任务。

旧四次阶段的结果及输入来源被保留。新程序中没有 `propose_height_quartic` 调用，也不重新构造该阶段的目标来再最小化。引用已有四次结果不等于声称本轮重新求得它。

帽高门也直接从旧 checkpoint 读取：其 physical definition、numerical definition、截距、九个权重、目标、两种 hash 及评价身份均准确重建并保持不变。完整固定 $g$、不可变 $b_0$、高度基及原各参数盒都继续核对。这里不再重放整个旧固定-$T$ 采样多面体，因为 joint 本来就不能在改变 $T$ 后继续使用那些旧行。

## 3. 明确的 warm-start 选择，不投影或放宽容差

顺序固定为：

1. 已发表的 post-quartic 态，零 $Q$ 扩展到 163 维；
2. 原 accepted height 态，零 $Q$ 扩展到同一 163 维空间。

两者的系数都原样使用，不裁剪、不投影、不拟合。用与后续优化共享的同一个 `JointSignedHeightObjective` 缓存，逐候选重新计算当前 $X$、目标和完整 Jacobian，独立检查原帽高、原盒以及新的 signed 高度条件。首个通过者成为 joint 初态；若首个失败，保留其完整原因并尝试第二个；两个都失败则保存小 JSON 和完整诊断，不调用优化器。

本轮明确采用新的数值求解保护

$$\sigma X_z\ge\frac1{10000},$$

原 signed-height 选择容差仍为 $10^{-9}$，没有放宽。该正值约束是对**当前有限工作网格**的求解保护，不是 reach 下界，也不是连续分离证书；它不会偷偷取代 [R66](../results/R66-core-flat-cap-two-normal-reach-height-gate.md) 的帽高门或[精确镜像点对门](exact-mirror-pair-nonlinear-gate-20261114.md)。后一精确非线性镜像门本轮没有加入。

新 signed 条件及其准确有理值进入本轮目标评价/约束身份。模型、固定度量和系数物理身份的定义没有因这个优化约束改变。旧 quartic 成本仍属于它原来的固定-$T$ 目标；当前 joint 成本只能在同一个 joint 工作网格、同一目标内比较。

## 4. 唯一尚未执行的优化预算

通过 warm 选择后，只执行一次原计划的 SLSQP joint：最多 80 迭代、120 个当前目标评价、300 秒。warm 检查使用同一个目标对象，所以其评价也计入该对象的评价预算；同状态的 objective、Jacobian、signed constraint 与 constraint Jacobian 共用缓存。原 $u,v$ 盒和新增 $Q$ 盒保持 $[-8,8]$，九高度盒保持 $[-1,1]$，完整 $g$ 和 $b_0$ 不参与优化。

当前 sampled signed $z$ 在每次 $u,v$ 变化后真实重算。checkpoint 的 eligible 选择也同时检查帽高、盒、当前 signed 高度，不因 SLSQP 返回 success 就直接选点。不使用 `keep_feasible` 冒称 SLSQP 自动始终可行。

若预算或试探评价异常，已有合格初态/最好合格点保留；最低成本但不合格的试探只作诊断。不会在返回后再投影、改变评价规则继续第二次最小化，或者重新跑已经完成的四次阶段。

## 5. 最终重构和保存

最终选中系数从 checkpoint 的 binary64 列表和准确有理列表交叉重建。检查同一个固定 $g$ 和不可变高度参考后，重新做工作网格完整审计，再做原 160 径向结构网格上的 384→768 角同参数评价，保留六jet、直接度量、曲率、球/条带、真实 signed 高度、帽高和镜像对诊断。

细网若不满足本轮正高度门，必须如实报告；不因粗网 eligible 就声称连续可行。最终角加倍不改参数，也不重新优化。共同高度继续由已冻结的查询无关原函数规则定义，不能逐圈移动来修正检查结果。

每个 checkpoint 保存完整 JSON 和紧凑 summary；summary 与完整文件字节 SHA 绑定。输入失败时同样保存包含 phase、错误、已知输入绑定和两种优化调用数 0 的小报告，避免再次出现没有可读诊断的失败。

## 6. 仅新增分支的人工覆盖

`--check-only` 包含：

- 纯人工数组：quartic 候选失败后准确回退、首候选合格直接保留、两者都失败时不调用优化器；正 guard 为 $10^{-4}$，容差仍 $10^{-9}$。
- 小的人工椭圆 carrier：构造明确标记的无旧优化 fixture，通过完整五文件 IO、解压 SHA、完整状态、零 $Q$、帽高 gate 和最终同态评价路径。此 fixture 明写没有 LP/QP/quartic/joint 求解，不冒称实际 Actions 研究回执。
- 错误第五 SHA、被改变的完整 post-quartic 状态、旧 joint 调用数已经为 1，均应拒绝；错误输入仍应留下失败小 JSON。

人工完整几何路径只评价，不调用 joint optimizer；没有重跑旧全部人工优化套件。截至本稿写入，只做了代码静态解析，新的公开人工回执仍须如实记录。

## 7. 公开命令

先执行新分支人工入口：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_height_joint_resume.py \
  --check-only --out "$RUNNER_TEMP/joint-resume-development.json"
```

唯一真实恢复调用为：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_height_joint_resume.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --short-audit topics/visible-flex-new-mechanism/notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz \
  --height-audit topics/visible-flex-new-mechanism/notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz \
  --prior-joint-audit topics/visible-flex-new-mechanism/notes/actions-43634358250-1-quartic_joint_audit/quartic-joint-audit.json.gz \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --expected-short-sha256 9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c \
  --expected-height-sha256 f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3 \
  --expected-prior-joint-sha256 e344e6e0a62be10dfa8dad4f52e4b889191f462b97bb19dd4b1cc0283f6f33dc \
  --out "$RUNNER_TEMP/quartic-reused-joint-resume.json"
```

这仍是待实际结果判断的一个数值求解步骤，未完成等距、嵌入、全曲面 reach 或课题的其它完成门。
