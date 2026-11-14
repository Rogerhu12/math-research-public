# 真 M15/N512 联解之后的下一模态入口：同 g、同原容差（v2：显式冻结 raw-lift 依赖路径）

> v1 原稿及账本保持原字节。tail_theory 全文独审发现 v1 可选 raw-lift 命令未显式给出 closing-tail cache，可能借用旧会话 fallback。本版仅补该环境路径、相应依赖说明和来源绑定；数学、槽位、参数、普通 coupled argv 与执行授权均不变。没有生成未来 M15/M16 输入或运行求解。

2026-11-09，/root/coupled_prefix。**仅静态接口方案；没有假定 M15 已成功，没有生成候选、配置或执行命令。** 若最终完整图仍不能满足原2e-9误差预算，继续真实加密和认证；不放宽或重解释该预算。

## 1. 已有实现足够，不另建升模框架

已有 high-mode-refinement、final-m15-n512-followup 两份方法和四个通用实现：

| 原文件 | 已有能力 |
|---|---|
| db6f-prefix-preserve-restart.py | 固定物理 profile/chart 上保存自适应网格，按真实槽位扩充 prefix Fourier 模态 |
| 950f-tail-warm-remesh.mjs | 将较低模的保存 Q/Pi 初猜放入较高模布局；同 p/depth 走节点复制 |
| db6f-prefix-tail-raw-lift.mjs | 可选：保持旧节点非均值 raw 数据，重新计算新基底的 momentum，仅作 UNSOLVED 初猜 |
| db6f-prefix-affine-lift.py | 若特定补零 cut 的首个真 DN 子问题受阻，可用旧真 DN/J 预测自由新 cut；通用 M>oldM，输出仍 UNSOLVED |

原 freeze-refine.py 已支持这些接口，但它写完输入立即启动，而且没有重指两个 trial I/O 键。因此本方案沿用已审 N512-followup §4 的方式：显式准备并冻结新输入，随后直接调用它原本调用的 flat-coupled driver。无需修改任何现有数学源。

## 2. 可接受的真实 baseline

未来模板 B 为：

    notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15.json.gz

它必须是真正完整的 N512 prefix 联解，不是 affine predictor、单独 s=1 tail、iteration CP 或早期 warm。沿已审 N512-followup §§2、5 核：

- 真实退出／summary／CP已闭，solver_success、actual_nonlinear_tail、fixed_metric 都为真，无 error；原 collocation、最后 actual_outer_checks 和原 scaled/physical BC 已通过。
- 必须读取 B 自己的 tail_seam.tail_record；记该绝对路径为 T15。它真正请求 Jacobian/audit，原残差小于2e-9、完整705项 Jacobian、17键 jets、8键 source audit 与 B.tail_seam 对应，实际 N=512。
- 全部 PP gzip 分片与其声明的 bytes/SHA、槽覆盖和 mesh 绑定正确；原 loader 本身不主动核声明的 SHA。原 frozen_profile、chart、physical port、gauge、warp reference 与冻结 g 一致。
- 全部实际源绑定和原物理参数保持；若实际输出名称与模板不同，只按真实已审记录替换路径，不假造 T15 的调用编号。

“有限联解成功”不要求这个 M15 图已经通过2e-9整图门；正因为它可能仍未过门，才把这份真联解作为下一模态的初猜。它的几何证书和误差数字不自动转移给 M16。

## 3. 本次只升 M；另外两类加密分别记录

首个下一阶取 M16：

| 项目 | M15/N512 → M16 设置 |
|---|---|
| prefix／tail modes | 15 → 16 |
| tail quadrature | 512 → 512 |
| prefix angular / audit-angular | 512 / 1024，保持 |
| physical depth / parts / steps | 12 / 8 / 32，保持；每 raw profile 仍256个基本RK步 |
| auditSteps | 保持原32 |
| tail solveTolerance / maxIterations / floor | 2e-9 / 36 / 默认.05，保持 |
| prefix tol / bc-tol / physical-bc-tol | 2e-9 / 1e-8 / 2e-11，保持 |
| profile、chart、calibration、warp、phase范围 | 全部原冻结定义 |

M16/N512 满足原 engine 的严格合法性条件 N>4M·spacing，即512>192。下一阶仍须核这个条件；背景 calibrationSteps=512不是本次 tail N，不能一起改。

纯升模不是径向再加密。若后来明确需要 RK 对照，p8s32→p8s64 必须重新求真尾并作原 coupled 校正；只提高输出插值网格不支付它。N512→1024则是另外的角规则变化，也须真求解。本方案没有同时执行这两项。seam 的诊断角样本由原 max(512,64M) 自动从960变成1024，这只是原诊断规则，不应误记为 tail N 变化。

## 4. 保存态的具体扩模与边界规范

prefix 的原 signed-mode padding 把低15模保留到 M16 的对应三组槽，新增槽为零；自由参数向量增加到16项，旧物理 support 振幅及低模 correction 按原 gauge/scales 恢复，新参数初值为零。固定 q_g=.1 不等于锁住实际 support，后者仍由原 BVP 求解。原入口局部 correction 保留，cut 不在其支撑内。新 prefix 有3M+1=49个槽，原 chart/物理网格从 B 恢复。

tail 每个节点原为30项，新为32项。原 remesh 的实际 copy 是：

    new[j]    = old[j]       for j=0,...,14
    new[16+j] = old[15+j]    for j=0,...,14
    new[15]   = 0
    new[31]   = 0

即两半分别按模式搬移，不能把30项整段复制到新数组开头。旧 rawNode 与 stage 数保持，仍是865节点、13个 raw 节点；同 p8/depth12 的 rawLeft*8 是整数，复制分支不需要额外 RK。tail-theory 已独立只读核对这条窄接口。

这仅保留保存 Q/Pi，不保证新 M16 moment root 下的 raw 斜率保持。可选 raw-lift 在每个节点先用旧 engine 的 toRaw，再对非均值 raw 数据补零，最后调用新 engine 的 initializeFromRaw，重新获得全部新 momentum；新 Pi16 因旧场的非线性高模 moment 可以不为零。node0 的原 portRatio 乘除也由该脚本处理。

raw 的前半是 Q=H/r⁴，不能直接当作物理 H。原 raw 后半记为 V 时，同节点原公式给物理非均值斜率

$$
S_j=r^3\bigl((3j)^2Q_j+\sqrt{12}\,V_j\bigr).
$$

所以在同一 g、同一节点保留 Q/V 才保留相应非均值 H/S；不应再给 raw-lift 输入额外乘 r/w。mean 会由原均值根重算，脚本实际报告 mean-slope 差；它没有保证整个 XYZ 图不变。raw-lift 会调用角向 root／均值根并构造原线性图，**不是纯元数据操作**，也不替代真正 shooting 或证明新 guard 全域成立。

两种初猜都合法，但哪种更好须由实际原求解决定。这里没有运行或比较它们。新 worker 的 cutHeight 标签按旧15模加一个0；新 prefix H 有保存/重建舍入时，原缺省 correctInitialBoundary 对全部16模加线性边界修正，随后仍真求 M16 DN。不能禁用该修正或把旧已解标签移给新 M16。

## 5. 最小新输入和原 coupled 命令

取全新输出 stem O：

    notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m16-d12-p8-s32-q512-outer-from15

将 B.frozen_profile 原值另存 O-frozen-profile.json；从 B.tail_config 完整复制 O-tail-config.json。物理和数值键只改 modes=16；I/O 必须独立：

| 键 | 新值 |
|---|---|
| initialCheckpoint | T15；或经实际转换并绑定的 UNSOLVED raw-lift 文件 |
| traceFile | O-tail-trace.jsonl |
| iterationCheckpointFile | O-tail-iteration.json.gz |
| trialDiagnosticFile，原来存在时 | O-tail-trials.jsonl |
| trialStatePrefix，原来存在时 | O-tail-stage-input |

其余配置逐类型保持，sharedEngines=true 沿原值，correctInitialBoundary 保留原缺省真。普通 shared worker 不消费两个 trial 键，但不能让其旧路径误导接手者；若原二键缺省，可保留缺省并准确记录实际差异。

若选 raw-lift，先另存 O-raw-lift-config.json，其 initialCheckpoint=T15；保留这个实际转换输入，不像旧 driver 那样事后覆写同名 config。下面 vf_tail15 必须填入按 B.tail_seam 解析且已核哈希的 T15：

    VISIBLE_FLEX_SOURCE_ROOT=/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/repro/source-root \
    CLOSING_TAIL_CACHE=/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts \
    node scripts/db6f-prefix-tail-raw-lift.mjs \
      --checkpoint "$vf_tail15" \
      --config notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m16-d12-p8-s32-q512-outer-from15-raw-lift-config.json \
      --out notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m16-d12-p8-s32-q512-outer-from15-raw-lift-warm.json.gz

raw-lift 的间接依赖 `closing_tail_sources.mjs` 不读取 `VISIBLE_FLEX_SOURCE_ROOT`，所以此处另显式设置 `CLOSING_TAIL_CACHE`。该 loader 仍优先邻题 adjacent 路径，并按 `notes/closing_tail_dependency_blobs.json` 的九个 Git-blob SHA1 核验所选目录；邻题目录缺省时使用这里的冻结 repro cache，因而不依赖旧会话的 `/workspace/scratch/f6f33987b45e` fallback。若 adjacent 存在但其九源不匹配，原 loader 明确拒绝，不能跳过校验。普通 shared client 已自行设置该 cache；下面 coupled argv 不作变更。v2 来源账本包含 loader、manifest 和九个真实 cache 文件，本次仅读字节并重算 Git-blob SHA1，没有加载 Node 模块或调用 root。

这是未来可选命令，不是本次运行。旧 raw-lift 没有输出拒覆盖／完整来源门，调用前须先核同 g、输入闭合、未使用的输出 stem，并保留实际转换配置、源码、输出 hash 和退出；其报告仍只能称 UNSOLVED。随后单独写最终 O-tail-config，把 initialCheckpoint 指向该 warm。直接 padding 则不需要这一转换文件。

真正 coupled 的原命令模板，cwd 为本题目录：

    python scripts/db6f-prefix-flat-coupled.py \
      --source-root repro/source-root \
      --profile notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m16-d12-p8-s32-q512-outer-from15-frozen-profile.json \
      --chart notes/2026-11-09-950f-prefix-adaptive-chart.json \
      --linear-port notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json \
      --tail-config notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m16-d12-p8-s32-q512-outer-from15-tail-config.json \
      --out-prefix notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m16-d12-p8-s32-q512-outer-from15 \
      --restart notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15.json.gz \
      --amplitude .1 --warp-reference .1 --modes 16 \
      --angular 512 --audit-angular 1024 --nodes 1601 --max-nodes 4500 \
      --tol 2e-9 --bc-tol 1e-8 --physical-bc-tol 2e-11 --node-heap 1536 \
      --fixed --warmup-scales --lagged-tail --preserve-restart-mesh

空 warmup 列表避免先重复整轮同 H 探测；原 outer 本身仍立即作真 DN/J。root 持有实际进程并保存 argv/来源/退出。直调 driver 不会自动产生 freeze-refine reproduction；配置、所有 PP/尾输入及实际 shared 八源必须另绑定。需要拒绝原因诊断时可选已审 flat-trial-coupled wrapper，但须明确记录那次实际 trial 八源，不能与普通 shared 来源混同。

## 6. 若新增补零 cut 的首个 DN 真受阻，已有后备接口

首次 prefix restart 的新增 H16 是零。该特定 Dirichlet 子问题的失败不自动否定允许新 cut 共同变化的 M16 联解。只有实际出现这个阻塞，才考虑现成 affine-lift 预测，而非反复从同一失败态盲跑或放宽 guard。

原 linear-port 有96项，linearSlope[15]=205.94394394816572；这是物理 dS16/dH16，不额外乘 mode/r/w。现有 affine-lift 对任意 M>oldM 已通用：取真正 M15/N512 最后 DN/J 的15×15低模块，新增线性斜率，交叉块仅在辅助 surrogate 中定义为0。原2e-9/BC容差由 B 继承。

    python scripts/db6f-prefix-affine-lift.py \
      --source-root repro/source-root \
      --checkpoint notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q512-outer-from15.json.gz \
      --linear-port notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json \
      --out-prefix notes/2026-11-09-db6f-prefix-m16-affine-cut-predictor-from15q512 \
      --modes 16 --angular 512 --max-nodes 4500

它会运行辅助 BVP，并非本次静态检查。输出 actual_nonlinear_tail=False、UNSOLVED，不能给 audit，也不能直接交给要求真 baseline 的 freeze-refine。若辅助结果可用，后续原 coupled 以它为 --restart，仍用原 M16 config、T15或已绑定 raw-lift 作尾初猜，在新预测 H 上真正求 DN，再按原 BC/Jacobian/source audit 验收。这里没有声称预测必成功或能恢复正分支。

## 7. 新阶验收与继续加密

M16 的实际最后 tail_seam 必须指向本次真正最后响应，不能猜调用编号。schema 相应变为：49个 prefix 槽，865×32个 tail shape 值，13×32 rawStates，800项原物理高度 Jacobian，三条长度16的 jets 向量及原14个标量、8项 source audit。身份与数值类型要求沿原已审定义，不能调用硬编码 M15／continuation02 的整套准备门来验 M16。

最终必须有完整 prefix 成功、原 tol/最后真 outer BC、真正 seam audit及闭合退出。随后新图的 XYZ、公共 C²接缝和连续整图误差按已有流程重新支付；M15/M12数值不得借用。若仍未达原2e-9门，保留真实结果继续下一模态或针对已定位误差作真实 RK/角加密。两者都不是调低 guard、改变 g 或重解释 G5。

本轮只读源及既有小元数据（包括 linear-port 长度/第16项），没有运行上述命令或生成未来文件。完整来源 SHA 列于同名 sources.json。
