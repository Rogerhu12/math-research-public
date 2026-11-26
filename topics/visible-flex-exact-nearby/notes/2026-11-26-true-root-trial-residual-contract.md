# TC：真实根上的96有限试探列、完整残差与有符号配对执行合同

会话：visible-exact-astra-198c63d-20261126。日期：2026-11-26 UTC。

本合同落实 [TC证明](../results/R149-supplement-true-root-continuous-PDE-trials-and-complete-residuals.md) 的试探对象目标。它使用 [SC的完整二源与配对定义](../results/R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md)，但不执行 SC17–24 的真实PDE列误差或有限逆认证。后者仍须等待同一完整正侧逆的实际结论。

## 1. 本轮恰好的数学对象

科学 kind 为 R149_complete_true_root_finite_trial_residuals_v1。源代码、参数、原输入、运行环境和实际输出的整件身份同时固定。对象是同一有限试探的96列：每列的真实根偶96数据为相应标准基，两侧使用完全相同的根状态，两个独立均值保留。根的位置始终是原严格隔离区间中的真实 $r_*$；浮点选点仅用于选取 dyadic 试探端点数据，既不代替 $r_*$，也不是证书。

本轮有三个自然的完整数学对象，按下列顺序保存：

| 自然对象 | 完整内容 | 本轮新小球数 |
|---|---|---:|
| 腰与有符号有限矩阵 | 全96腰密度范数；physical primitive96 与 declared incoming cosine96 两个完整96×96矩阵，各自的1、无穷、2及Frobenius范数上界 | 96+8 |
| 负侧源 | 全96列各自的 mixed-root、strict 两个完整源范数；同一腰96范数原样引用 | 192 |
| 正侧源 | 全96列各自的 low、high-collar、high-body 三个完整源范数 | 288 |

总计584个新小球。负侧文件重复显示腰范数时只复制已正式保存的同一记录，不产生第二次范数计算。原 RW96 的480球均为已成旧结果，不属于这584球。

**TC8 所说的一条完整列，须五个源、腰对象和全部有符号配对均齐。** matrix.complete 或 negative.complete 只授予对应自然数学对象完成；它们不授予“完整列”或总体完成。只有三个自然对象全部完整，科学总状态才能 complete/proved。即便该试探目标全部完成，真实PDE列、全频逆和课题完成标准仍未由它单独证明。

## 2. 全部原输入与同一选定成员

首轮整件清单包括78件当前小UTF8原件和27件原历史输入。当前原件中的完整旧 RW、NW manifests 及其全部固定输入逐件保留，不以摘抄常数替代。原 RW实际 run 45787309600/1 必须全96行、480球及全部整载体哈希完成，其 actual、execution 与 manifest 同时准入。

27件历史输入分别为四件原 H/K48/R31/W 压缩原件、base和physical Z的两个完整索引、其5+14个完整原始 cubic shards、两条连续修复原件。前四件从原46f127c7153f5393dcd2a00f42d4c1d3662c294d恢复；其余从原7c130fb94528de8f003a43e7049fb42768a64eec恢复。只在临时树恢复整件字节并核大小/SHA256及存在的Git blob身份，不重新运行旧生产者。

全7721行 intrinsic midpoint 0至2阶及whole第三阶输入，由原六个历史自然片和八个原 Actions archive 恢复成原40片。原 archive 的成功process、范围、run/attempt、原manifest及所有完整片哈希均核。随后对原全行正文重新做规范字节哈希检查，要求原 payload 为06fdb69708f63d27587fb91bb0760b50e23fa8d1719ed8b8903d8be6e922abe6。此处只读原球及元数据，不计算旧残差、原scalar fee、FFT或Green目标。

真正证书保留原 $\eta$ 半宽 $10^{-9}$，不把whole参数球缩成 $\eta_0$ 点球。选定参数用已证有理上界

$$
|\delta_*|\leq
\frac{9368259853002}{100000000000000000000000}.
$$

完整背景为原连续 $Q_0+\delta_* Z$。base的原 $\alpha$ 只乘一次；Z已为physical193，不再乘 $\alpha$。两条 exact offset chain 按原定义完整物化并核原全链哈希；均值为原 $s_0$ 加完整修复背景均值及 $\delta_* Z$ 的均值，不能换成新rotational均值。

## 3. 选试探与真正残差的边界

浮点 proposal 使用原 repaired M32 centre、全部193状态、同原scalar midpoint/third输入及固定 Robin slope13/80，固定 numpy2.3.5、Haswell单线程。此分支只选择有限 dyadic 端点值及前三阶端点数据。四个完整私有数组先写盘、全量读回、核整件哈希，再成为唯一试探输入；原根偶96块必须逐位恰为单位阵。

真实证书使用含真 $r_*$ 的 septic Hermite及真长度 $h$，共享端点给出精确连续性。所有证书子格的积分质量是固定正Fraction长度；不能把有区间依赖的真 $h$ 当成该质量。根附近两侧保守延拓可在原隔离小区间重叠；这是上界多收费，不删除任何真实域。

完整 moving 线性化先在有符号 Fourier 多项式上作用，再取范数。全部288角输出、两个均值、mean-rank项、cutoff及其导数均保留。有限多项式用原 dr 测度的 Legendre 恒等式积分，whole第三阶余项只作值包围，不对余项非法求导。正侧三个窗口与负侧 mixed-root/strict 窗口严格采用原完整source域。外端、跳跃及根上规定数据的零误差由试探的精确定义保证。

腰密度取真 selected $q_0$、完整moving mean和原尺度；不可把一般 L2 源的wroot充作物理aroot，也不可丢独立均值。两个96×96配对矩阵是新试探的实际有符号积分；32个unsigned输入表不参与重建它们。

## 4. RW旧载体、私有全矩阵与新小结论

原 RW4096网格及每行1025个实系数仅作为本次有符号配对的必要输入，依原同定义重新物化，按原80位保存格式逐整件哈希匹配，再读回。原 $\varepsilon_j$、row norm、incoming/physical error等旧目标不调用；原无限复合尾和H−G误差已成资格保持原状。

两个完整新矩阵各有9216个signed球。所有条目先在临时目录全量保存、读回并核包含，随后仅从该正式读回对象导出四个完整范数上界。公开结果保存完整行列数、完整载体哈希、准确重建定义和小球，不公开新大数组，不上传 artifact 或 Release。

若后续真实SC列误差或有限逆需要这些条目，应按完全同一试探定义及全载体哈希重新物化必要输入，不重复已成的矩阵范数目标，也不凭中点改换试探对象。

## 5. 先数学读回，再完成标记

自然对象的全部小球先写入候选整件，逐球读回验证包含并核全schema，然后原子改名为正式文件。正式文件可以领先随后写入的state marker；它本身是已经全量验证的数学对象。每形成一个自然结论，worker立即推送完整对象与实际执行记录。

径向循环每格先算完该格对全部96列、全部所需源窗口的贡献，再更新五组平方范数上界。每8个完整格，以及负侧终点和总终点，保存一个自然的完整累积前缀：五组各96个canonical binary64 hex上界、精确next_cell/total_cells/最后完整格、完整试探及plan哈希、同一owner与所有科学源哈希。它不是计数器替代物；没有正式保存的未完尾部不进入已接受前缀。

科学state、完整对象、完整前缀各自小于100000B；当前发布的这些自然对象、execution和报告合计上限170000B。每次发布及rebase后均重新检查真实topic总量200000000B，另保120000B余量。没有为绕大小限制人为拆分一个whole数学结果。

## 6. 真实失败前缀的完整接续

metadata generator可以接收一对真实的 prior-manifest 与 prior-execution。它从实际execution的科学文件清单自动收齐每个正式 state/matrix/negative/positive/prefix，逐完整字节和哈希核，调用同一owner的admit_prior_metadata。不能通过少给一个已成formal对象来重算它。

接续必须保持同一owner、纯数学源、原运行环境、原selected identity、全部参数，以及重新物化后逐件完全相同的四个试探数组和完整plan身份。已成自然对象按原字节复制，不重复积分或配对范数。复制对象永远保留最初的producer manifest；多次接续通过前一完整manifest中prior对象的相同字节/哈希绑定逐次承接，既不改旧正文，也不伪改落后的旧state。

正式prefix可领先旧state一次；只在整个prefix schema、整数格数、最后实际plan格、五组完整96 hex及全部scope核完后续加。matrix已成但尚无prefix时可从第0格只继续积分。负侧结论复制须prefix已越过全部负侧格；正侧结论复制须prefix已覆盖全plan。

若实际execution已含三个完整自然对象，生成器和owner均拒绝开启新science。此时只消费并登记原完成对象。若仍有缺失对象，新manifest的new_target_order必须恰为缺失集合，不把旧完成目标当新目标。

## 7. 公开运行和实际资格

首轮manifest为2026-11-26-true-root-trial-residual-inputs.json；workflow为fourfold-codazzi-true-root-trials-public.yml。后续只有提供真实整件前驱记录才生成带该run/hash后缀的新入口。每个具体入口保唯一consumed marker，不自动重跑科学。

worker在任何数值import、目标认领之前，恢复并完整准入所有原输入。旧代码只AST抽取指定纯reader/repair/Box/FFT定义及原archive恢复函数，不执行任何旧main/producer。新科学仅一个公开Actions子进程，Python3.12.14、numpy2.3.5、python-flint0.9.0、320bits、Haswell单线程。子进程不持有GitHub令牌。

worker每1800秒pull并核两README；非快进拒绝立即pull --rebase再推直到成功。规则变化时保留原完整前缀及实际失败记录，先处理实际diff。超出本轮科学时限也只形成可接续的实际前缀，不是课题停工理由。根会话继续处理后续真实缺失数学。

本合同没有实际run数值。任何阶段是否完成，只由随后公开的完整actual、execution、manifest和真实运行状态共同决定。
