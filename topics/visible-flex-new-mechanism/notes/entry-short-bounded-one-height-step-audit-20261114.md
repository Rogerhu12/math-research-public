# 短入口与有界高度：两初态、每态至多一个 B7 步的公开审计接口

状态：实现已完成并经独立静态审查；本稿建立时尚无本新 driver 的公开人工执行回执。只有公开人工全主流程通过后，才可接真实输入。没有执行新的研究计算，没有改动已经发布的求解器或原失败输出。

## 1. 已有实际证据与本轮范围

[长入口实际输出](actions-43622984979-1-entry_paired_audit/frame-entry-paired-repair-initial-audit.json) 来自公开 Actions run 43622984979，源提交 ac8ca0437b9617b63522eef5267d1b060144865c，其完整原文为 835599 字节，SHA256 为 f12f9d8fcf90f3548b3e1e12d717f7c87932f901317ec43ca3040f7785129cdf。

该输出只审计了一个新表示，没有优化。长度 $81/500$ 的入口修复在 $121\times768$ 样本网格上给出度量算子误差峰值约 $79.34$、中心速度峰值约 $7.576$。入口外全部五个非位置二 jet 与旧选中场相同，只出现约 $0.33552$ 的共同竖直平移。角向及积分精化差异远小于上述缺口。不能把这次表示修改称为进展或等距近似已经合格。

本接口只做以下有限比较：

1. 固定原已选完整度量、原不可变 $c_0$、核心与物理六帽，把入口长度改为 $\ell=81/1000$，其余原始参数先保持。
2. 在同一短入口上，将固定高度参考换成已明确的有界角均值参考；切向场 $T$ 的当前空间与原始参数相同。
3. 对每个新场至多请求一次已发布单列 B7 helper 的候选，并在确有候选时以完整 geometry 重建一次。
4. 对固定最终状态作有限评价精化，既不重优化，也不重跑原来的 250 次多变量求解。

两个新初态和原长入口都是不同的物理位置场。它们共同使用的完整目标度量是原选中度量；任何“同 $g$”表述都不意味着像集、实际第一基本形式、曲率或高度相同。

## 2. 物理与表示身份

新程序为 scripts/frame_entry_short_bounded_audit.py。它复用已发布的 EntryRepairProblem、BoundedEntryHeightProblem 和 choose_height_coefficient，不复制求解算法。

短入口依旧用现有 $W_2/W_5$ 切向自由权与 $W_4$ 高度权。其右端为

$$
t_c+\ell=\frac9{250}+\frac{81}{1000}=\frac{117}{1000}.
$$

该点恰是现有均匀九自由径向 B 样条的首片右端。相较 $\ell=162/1000$，此次修复不会把首片 Taylor 多项式延续到下一片。这个表示选择有明确理由，但不保证误差下降；缩短后也可能主要回到旧场的入口缺口。

有界高度版本的固定参考使用完整已冻结的 $a'(t)$，包括原来五个 body 度量系数，而不是仅用 seed：

$$
\beta_*(t,\theta)
=-\frac{\sigma\pi}{2}
+\sigma\arctan\frac{a'(t)}{k(\theta)},
\qquad
b_*(t)=\left\langle
-\frac{\sin\beta_{\rm blend}(t,\theta)}
{\sqrt{1+v_{\rm ref}(t,\theta)^2}}
\right\rangle_\theta .
$$

这里 $k$ 是材料角转速，$\sigma$ 是端口侧号。固定参考严格有 $|b_*|\le1$；当前高度自由列另加在其上，因此这不是对总 $|b|$ 的声明。固定参考匹配已推导的 $b_6,b_7$，现有 $W_4$ 自由高度首项仍可改变总 $b_7$。本版本没有新增 $Q=k_\theta/k^3$ 角列，也没有宣称付清 $u_5,v_8$ 或完整 Cauchy 系列。

两个初态均保留原始 162 个 binary64 参数；完整有理参数记录、布局、固定 $g$、核心、六帽与原不可变 $c_0$ 都在输出中逐项保存。新增模型身份明确表示本轮高度参考或入口表示已经改变。

## 3. 严格读入与来源约定

研究入口必须同时满足：

- GITHUB_ACTIONS 的值为 true；
- GITHUB_REPOSITORY 精确为 Rogerhu12/math-research-public；
- 三份输入均位于本课题已经发布的 notes 路径；
- 三份解码后原文字节 SHA256 与明确给定值一致；
- 原 selected 报告由现有严格 loader 完整重放，原始 $c_0$ 原文、各源代码、参数 Fraction、原布局和冻结完整 $g$ 均匹配；
- 原长入口输出必须处于完成状态、没有参数步骤或优化，原 22 个源码 SHA 与当前冻结实现一致；
- 由其原配置重新构造的完整 state_record 与原输出逐项一致。此处只重放身份，不重新计算长入口的 geometry。

程序可读取原文或 gzip 存储。SHA 参数始终绑定解码后的原文字节；同时单独保存 gzip 文件本身的 SHA 与字节数，不混用两类身份。

当前三份输入的解码后 SHA256 分别为：

| 输入 | SHA256 |
|---|---|
| 原选中 independent-height 报告 | c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 |
| 原 enriched $c_0$ 报告 | 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 |
| 原长入口完成审计 | f12f9d8fcf90f3548b3e1e12d717f7c87932f901317ec43ca3040f7785129cdf |

## 4. 固定网格与一次高度提案

默认位置审计以原 $121$ 个均匀径向点为底，合并全部 seed/原场/body 度量/高度基结构节点，并补入

$$
t_c+\frac{j\ell}{24},\qquad j=0,\ldots,24.
$$

因此包含 24 个 collar 小区间的 25 个端点，尤其不会漏掉缩短后修复层、平台端和首样条片边界。全部节点先作为准确有理数合并，再转为评价用 binary64。角向首档为完整均匀 384 点。每个样本仍使用相同权重，因此新的非均匀径向网格的平均成本不能直接与旧均匀网格成本相减；程序另外重算原选中未修复场在这个相同新网格上的成本。

默认只用高度 local 列 4，即原 full quintic B7。其准确支撑为 $[198/1000,684/1000]$，完全位于新入口右端之后；原函数的尾端增益仍为 $81/1000$。程序从真实基定义取出这些数并检查，不仅依靠注释。

helper 使用当前新场实际评价所得的帽高，默认要求所选 upper 分支满足 R66 高度下限再加 $1/1000$ 的设计余量，同时要求固定样本落在原球目标内，并可选择样本 $\sigma z\ge0$。它不会把旧场的帽高代入，也不会因抬高而改变 $y$ 条带超界。

当可行区间为空时，完整保存具体固定失败或上下界见证，不改参数。当有候选时：

- 只替换一个明确的高度 binary64 系数；
- 用 Fraction.from_float 核该新旧系数之差与 helper 的准确记录一致；
- 重新调用完整 geometry，核全部六个位置二 jet 与有限变化公式；
- 重新报告真实 $E,F,G$、曲率、面积、球、条带、signed-height、单一帽高、端口与镜合对法弦样本；
- 不再迭代选择第二个步骤，也不在细网格上重新选系数。

helper 最小化的是准确展开的有限样本 direct-metric 四次目标。完整 smooth-positive 球/条带目标在重建后另读；其成本可能升高。当前高度积分和样本边界都不是区间证书，即使保存了准确系数，也不能把这个数值步骤称为连续可行点。

## 5. 固定状态评价账

所有评价精化均保持完整新模型、原 $c_0$、完整 $g$ 与准确参数向量不变。

- 每个最终状态作 $\Pi$ 角数 $384\to768$ 对比，保存六个位置二 jet 和 direct metric 差，并重新保存细档完整诊断。
- 仅有界参考的新积分作固定高度均值角数加倍。
- 仅有界参考的新固定分区原函数作 GL 阶数 $8\to12$。
- 没有再对已检查过的原长入口做完整五因素扫描，没有热阶数扫描，也没有变规则后再求解。

此版所有比较仍调用原完整 geometry 路径。尚未采用新的 split-prefix 或 height-only 快捷评价，以便先取得可靠人工主流程回执。每个初态、提案、重建、评价档之后，先原子保存完整报告，再保存同文件 stem 加 -summary.json 的科学摘要。摘要绑定该次完整报告的原文字节 SHA256、字节数与阶段状态，并保留输入与源码 SHA、场/g/状态哈希及参数块统计、每个初态/一步后/角加倍态的全部 sampled/regional/height/mirror 指标、可行区间和所选提案、六 jet 变化及积分精化标量。完整 canonical 状态、准确参数和逐径向行仍留在完整报告；摘要只服务于进展和科学缺口的直接检查。若公开 runner 未能完成，已有阶段数据不会被冒称为完整研究成功。

镜合对诊断还保存

$$
\rho_{\rm mirror}(p)
=\frac{|z|}{|n_z|}
=\frac{|z|\lVert X_s\times T\rVert}
{|(X_s\times T)_z|},
$$

仅在分母非零、曲面浸入、两镜像材料点确为不同点时作为必要法弦上界。$n_z=0$ 的点不提供这一有限界；非中缝 $z=0$ 则会导致镜合重合。该采样诊断不取代完整闭面 reach 证明。

## 6. 人工检查与部署顺序

本新 driver 的 check-only 不读取实际候选，也不设置伪造的 Actions 环境变量。它从现有人工 carrier 构造一个确实有九条高度控制的人工报告，走严格 selected loader 和 prior 身份重放，再走两模型、成功高度步骤、不可达帽高空集、稀疏接口与全部所选评价比较。为可靠覆盖成功分支，人工步骤单独使用明确标注的低阈值并关闭人工球区间；这条覆盖选项不能由研究 CLI 触发。

人工检查还覆盖 gzip 原文字节回转、错误 SHA、改坏的 prior 参数、错误仓库、未发布输入路径，以及输出 JSON 原样回读。另检查 checkpoint 摘要绑定当前完整报告的 SHA/状态、保留各 case 的指标与状态哈希，并不含巨大 canonical 与逐径向字段。人工成功也只证明这条实现路径，没有实际几何结论。

先运行：

    python topics/visible-flex-new-mechanism/scripts/frame_entry_short_bounded_audit.py \
      --check-only \
      --out topics/visible-flex-new-mechanism/notes/frame-entry-short-bounded-development-check.json

公开人工成功后，固定默认研究参数的命令为：

    python topics/visible-flex-new-mechanism/scripts/frame_entry_short_bounded_audit.py \
      --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
      --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
      --prior-entry-audit topics/visible-flex-new-mechanism/notes/actions-43622984979-1-entry_paired_audit/frame-entry-paired-repair-initial-audit.json \
      --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
      --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
      --expected-prior-sha256 f12f9d8fcf90f3548b3e1e12d717f7c87932f901317ec43ca3040f7785129cdf \
      --entry-length 81/1000 --entry-mean-nodes 1024 \
      --radial-nodes 121 --angular-nodes 384 --collar-subdivisions 24 \
      --uniform-panels 120 --primitive-order 8 --refined-primitive-order 12 \
      --height-column 4 --height-bound 1 --tau 61/1000 \
      --height-margin 1/1000 --minimum-signed-height 0 \
      --out topics/visible-flex-new-mechanism/notes/frame-entry-short-bounded-initial-audit.json

当前源码为 43424 字节，SHA256 为 b16e1df72225e1c68f7b83b028a3910233a773d3fd437d220191868d2559cc63。以上数值参数是这次初态比较的明确设计选择，不是从未运行的新场中挑选的最优参数。
