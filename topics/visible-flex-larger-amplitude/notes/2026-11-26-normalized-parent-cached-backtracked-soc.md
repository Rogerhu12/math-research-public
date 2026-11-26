# 完整规范化父场：缓存、内点恢复和后退锚的全部约束 SOC

**状态：完整新实现及纯源码绑定已完成；尚未对这个新入口执行科学计算。**
这份记录是已刊完整算法的明确复合和新后退锚策略，不把有限修正或预算返回称为存在、等距、reach 或精化收敛结论。

## 1. 具体问题和来源

run02 的真实 46–48 阶段记录见[实际记录第 5 卷](2026-11-26-public-actions-45800076687-1-part-005.md)。
当前已知完整内点父是 `793bde458be303034d3f3a0b1b7f9fd17d7cf84ec99fc1b3bb5313ce10008044`，其完整报告为 `bb5c52e02af18b02cd2aed9a9d64fe6bb687f8f1f1510fe0792684ff241f9241`。
这不是最初被冻结的深谷父：原深谷 `d021a50a492b941004ee75f5cba138d5b5bc07092073a642a027bde4f97bb478` 只定义固定单位子午方向 $T_0$、原 chart 和同一个标量问题。
真实规范化父表示的完整模型为 `ad01742ce5051188bafddf8e93046468788eb27e7ec948c26903578742f5bb92`，准确标量身份为 `0a223b986f35263c168e26d30295fd84048e134c6b053ba90c7cd39beaf1f5cb`。

实际 48 的纯读数已确认：原度量 QP 用完 16 advances，最终投影梯度 `4.769888394947521`，容差 `5.208014191841168e-6`；原全步真实 Phi 下降但最大物理约束超量 `0.002834877771912603`，最后原射线只接受 $\alpha=1/16$。
这里同时有内层未收敛和真实几何回溯限制，不能只据一个现象归因。
本入口的 ready 明确使用完整 `1 × 64` metric、`4 × 64` restoration，实际初始两种阻尼均为 `.01`；这是一个可完整返回的调用预算，不是问题的能力上限或结束条件。

另一条独立 direct-axisymmetric 链的真实 17–18 表明：一个较大锚的全半空间数值可行修正仍能有很大的真实曲率或 Phi；达到有限半空间可行不等于小修正，也不等于最小范数收敛。
新策略因此先完成原射线的真回溯，再选择靠近真实 fallback 的锚。它不把那条不同输入的数值结论移给本规范化父问题。

## 2. 物理场、全变量和原求解范数保持准确身份

实际物理源仍是完整 `so3_closed_meridian_operator.py` (`234ac8db…`) 和完整父向量源 `so3_parent_meridian_jet.py` (`d3f25bb7…`)；世界六 jet 几何仍是完整 `so3_closed_meridian_geometry.py` (`72f38259…`)。
这与直接准确轴对称输入的 `7f26…` 不是同一 source/model。本 helper 独立检查完整对象来源、`parent_meridian_kernel_sha256`、冻结父完整模型、当前准确深谷标量身份；没有把旧 7f guard 改标签后冒用。

原全部自由 core、所有共享 quintic 旋转 jet 和自由 $H$ 均保留，实际 $F=F_{\rm raw}+h\Delta$ 及其完整角向/core/H 链、全部六 jet 不变。
径向 Gram 仍需完整 $F_s=T+h'\Delta$，并不恒等于一。
本问题的原完整 $g$、全原正权角/径向观测、全部 mean 和 cross 行、`jet-sum` 范数、其角频率/径向参数以及实际阻尼单位均保持。
新增源码没有替换原 operator/provider 的任何方法，也不缓存当前自由场的 F/J。

`CommonSlackRows` 的完整 AST 与已刊 cached/interior `174b79f4…` 逐字语义相同。
严格正的内点搜索 margin (`1e-8`) 只收紧 Phase I 搜索模型；原物理 $g\le0$ 与真实非线性接受不变。
所有原 typed C 和幅度行都在公共松弛模型中，残余松弛从不当作物理可行。

## 3. 先前拒绝地址在本父重新线性化

原 selector 上限仍为 192，保其实际返回的全部行，再保全部所选幅度行（双支距离、完整 cap/H 标量行）。实际行数按本次报告返回，不把上限 192 写成每次实际恰好 192。
当前 restart 报告及本次已经返回的真实拒绝记录提供地址；新父重新计算其完整物理值、协向量和同一坐标转置。
不继承旧父协向量、bound、曲率值或通过结论。所有地址用完整二进制 `cell/u/phi` 身份去重，既有 curvature/radius 两套永久集不截断。

曲率新行包括实际两条主曲率分支，以及当前父真实直径控制项的导数；双支幅度用真实 current witness，并保所有 free core 的 $dp$ 链。
若所选父分支不具已用协向量的条件，helper 诚实返回不能构成该修正，不伪造导数。
若新行在当前父有正违反，不把负 bound 的 QP 原点称为可行；报告明确需要真实恢复或其他父。

原 mmap 前缀在原位扩容，既有行字节不被重写。完整 pre-QP 新前缀再冻结并实际 SHA 绑定；之后每次 SOC 扩展只追加，新旧所有行一起进入投影。
实际 used/capacity bytes、全前缀 SHA 和新增行数分别记录，没有第二份隐藏的原 2GB 行缓存。

## 4. 唯一后退锚、真正 fallback 和最后才更新的父

固定一次真实当前父 $x$ 和该父完整 QP 方向 $z_0$；$T$ 为原坐标 lift。
原射线按 $\alpha=1,1/2,\ldots$ 顺序读真实残差/Phi/域；只在域与实际下降通过时支付完整几何。每次已读的新地址立即进入永久记忆。

第一次满足原全部真实接受条件的射线点 $y_f=x+\alpha_fTz_0$ 先作为 **候选 fallback** 保存，不设置最终 `accepted`，也不更新 $x$。
在此前已经实际读过的射线中，取最近的较大 $\alpha_a>\alpha_f$，要求其 Phi 与域通过、全几何完整返回而真实违反为正；这就是本方向唯一的锚 $d=\alpha_a z_0$，$y_a=x+Td$。
若没有这样的真实 fallback 或 eligible 大射线，本方向不启用该策略；这不是不可行或不存在结论。

此后每轮都用同一个原 $x$、同一个 $d$、同一个原父 A。新的拒绝点仅提供需追加的约束地点，不替代锚。
原父、锚点、锚方向、fallback 完整 word vector 均单独记录 SHA；不把不同锚的 $Cd$、余项或原预测混用。

若得到同时满足同一基线实际 Phi 下降、域、完整真实几何的 corrected 候选，就停止这一组修正轮。
将该候选与原 fallback 按**已经实际读得的同 Phi**由小到大排列，再逐个用当前全部永久地址完整重读残差、Phi、域及几何。
只有此时通过的候选能标成唯一 `accepted`，并更新 $x$。
原候选读数保存在 `pre_selection_true_read`，最后选择读数独立保存；不能留下原 ray 与 corrected 双接受。

这解决了一个必要的记忆问题：拒绝的 SOC 可能新增一个使旧 fallback 失败的位置，所以不能沿用其先前 `passed`。
若两候选的最终当前记忆读数都失败，则继续剩余原射线回溯预算，但不再换第二个 SOC 锚；全部新地点保留。
如果原剩余预算也不能接受，仍返回未接受方向，并由后续当前父真读/恢复负责。没有用公共松弛或投影成功代替实际场值。

## 5. 每一行都保留的修正公式

把每个本父固定 typed 约束写成 $g_i(x)\le0$，其严格正归一化数为 $s_i$。
实际缓存是 $C_i=Dg_i(x)T/s_i$、$b_i=-g_i(x)/s_i$。
曲率行的分支和直径控制地点也包含在这个固定函数的描述中；全局最大曲率/直径仍由之后完整真筛独立负责。

在**同一个**锚 $d$ 真读 $r_i=g_i(x+Td)/s_i$，取明确非负搜索 inward 量

$$
\eta=\tau\lVert d\rVert^3+f\max(0,\max_i r_i),\qquad \tau=0,\quad f=1/8
$$

作为本 ready 的有限算法参数。全部原行及每一条已追加行同时要求

$$
C_ie\le\min\{b_i-C_id,\ -r_i-\eta\}.
$$

因此准确代数上 $C_i(d+e)\le b_i$，且锚处一次线性修正满足 $r_i+C_ie\le-\eta$。
这只证明所述完整半空间关系；观测 inward 项不被称为已证明的三阶余项界，非线性新场仍必须真筛。

调用仍是已刊完整 R683 `a2c6d334…` 投影核，所有行保留，数值预算最多 20,000 sweeps。
无论该核是否达到其最小范数停止条件，都另行重读完整 $Ce$、$C(d+e)$、所有固定非线性行和前缀 SHA。
只有满足实际读回容差的提案才继续；`sweep_limit_feasible` 明确是有限数值可行而非最小范数收敛，更不推出修正相对锚小。
完整记录 `correction_norm`、`correction_over_anchor_norm`、每轮新行、投影状态和直接线性违约。

对 $z=d+e$，外层保原父完整 A 并独立计算 $Az$、真实单位的半坡度与预测，再读新场真实 Phi/域/全几何。
没有把原 $\alpha z_0$ 的预测借给修正点。SOC 接受时保同一个实际 $\mu$，原射线原有阻尼更新规则保持；两种预测比值分列。

## 6. 数值 T0 缓存的完整来源合同

此前[缓存说明](2026-11-26-normalized-parent-cache-adoption.md)仍适用。
新 cache binder 只扩展明确的 producer 集合：原 7e/0f、已刊完整 cached 174b、以及本新完整 source/schema。
原 `4e9ed694…` manifest 必须按原报告中真实 `reference_cache` source SHA 核；新 manifest 按 `50a9a480…` 核，不能换标签。

相同原冻结父完整模型、四输入 bytes、同 run、全部 radial query 与 literal angle、原 provider/operator/source/runtime 及每个实际 NPZ 数组 shape/type/bytes 都要匹配。
只安装已识别不可变 T0 四 jet words 到原 plain `_cache`；未知/缺失项仍由完整原 provider 真算。
旧报告没有历史 cache checksum，首次接纳是新显式数值输入绑定，绝不补造旧承诺。
原方法字节、当前自由场、目标、范数不改；缓存也不继承任何物理或连续证书。

完整 manifest、每缓存文件 SHA/数组记录和原始数据只留 runner。公开记录只有紧凑 scalar/provenance 摘要。

## 7. 完整源码与独立归因

下表六源均放在 `scripts/resume_20261126/`；本地只做纯 stdlib AST/compile、重复字面键、尾空白及纯 argv 检查，没有科学运行。

| 完整源码 | bytes | SHA256 |
|---|---:|---|
| `complete_normalized_parent_so3_rows_soc.py` | 40993 | `e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021` |
| `so3_frozen_parent_cache_for_soc.py` | 26541 | `50a9a4802fb23d01659de4a5ff2e1429f52837c59d6b4c563ae72f54836a4abe` |
| `fullclosed_so3_cached_interior_separation_soc.py` | 75064 | `01b2a7777fea1979083c95d881da006d11885014c90c7f2dba7afd53d283aea9` |
| `launch_so3_cached_interior_separation_soc.py` | 11596 | `d0ba8ccd02a811c51cd7006f1c299ad4b7eff57c195ee3a772c38fef1431a434` |
| `derive_normalized_parent_cached_soc.py` | 47226 | `3fe49982ca054a7dc29b78f0c6c1b5818924e242757f1cf64335ab6d910424b8` |
| `read_so3_cached_interior_separation_soc_report.py` | 55153 | `9e92afc2441e18f15c48cf06d14c7827a6cfc2d864a1826d03734b418093cc28` |

完整 pure deriver 从已刊 174b/9b87 的全部字节和明确完整 literal edits 重建 driver/launcher，并核整个返回 body，而不是仅核头部或名字。
所有既有顶层物理/坐标接口、完整 CommonSlackRows，以及全部原内部 statistics/scan/remember/cache save 函数 AST 保持。
独立 helper 与原 02875 相比只有来源/模型入口 `__init__` 改变；其全部 26 个其他完整函数逐 AST 相同。cache helper 仅 producer/manifest 来源扩展，完整科学 T0 计算方法不变。

新完整 reader 同时核规范化父 canonical/source、严格内点恢复、原完整缓存、全部 SOC 行/前缀、同锚 SHA、最近 eligible 射线、首次真实 fallback、候选 Phi 顺序、最后全部记忆读回和唯一接受。
原纯 `6982…` 或 direct-axisymmetric `f686…` reader 不被用来冒认此新 schema。
solver 已独立静态核完整主循环、normalized helper 和新 reader，没有发现阻断；这是源码审查事实，不是新科学运行成功。

## 8. 可直接执行但尚未排程的完整请求

参数文件为 `computations/resume-20261126-normalized-cached-backtracked-soc-ready.json`，包含完整 science 和纯 reader 两步。
它只引用上文已经实际返回的 793b/bb5c，原 frozen deep 父、原 carrier/node/scalar 路径保持；当前并行 cached 1×64 后继的未返回结果不写作已知父。
后继若换为真正返回的新 same-input 父，必须在新请求中显式绑定完整实际 checkpoint/report 和全部地址，不能仅换输出名或捏造 SHA。

其科学参数完整为：$M=160,J=923,N=2048$，全原 positive measure；Gauss integration 8、原 inverse 18 次/容差 $2\times10^{-12}$，angle block 8、stage block 64；原 `jet-sum` length `.05`、angular transition 24；metric `1×64`，restoration `4×64`，两初始 $\mu=.01$；$p=4,\epsilon=.001,c=.05$，原混合权 `.5`；原 selector 上限 192、`.03` reach 比例、`.992` 数值安全系数、幅度 budgets `4.2/.9/1.01`；原 15 个 ray 预算，最多 8 SOC rounds；target `1e-9` 只作为本数值入口参数，不宣称是 README 原求解 floor。

两步仅返回 scalar dot-path 摘要，完整 report/raw cache 留在 runner，cleanup 仅删本新输出的 `rows-*`。
完整 reader 可核 final bundle 和 cache 文件实际 SHA；不重算 F/J，也不跑 fixture。

仍未支付的任务包括：新场连续 metric/reach/幅度、全相位族与含反射欧氏商责任、严格求积/正规化/逆图误差、以及同一固定问题的真实精化下降和有意义 solver floor。
这套入口用于继续真实求解，不能据实现完成或单个预算返回宣布课题完成。

## 9. 本次完整发布与运行交接

2026-11-26 16:02:05 UTC，root已通读完整说明、原helper唯一构造来源差异、cache完整来源差异、新driver全部验收主循环与新reader的同锚/全部行/永久记忆/唯一接受/缓存来源合同；本次六源全部实际stdlib AST/compile通过，没有本地科学计算。完整参数18,292B，SHA `ed8329e90aa79940ca930ffec3281015f66f13b26949e86529832ed1035c2057`。

本次只刊完整可复现源与ready，不将它加入已到准入时限的02队列。下一独立公开runner要从完整原再生链生成自己真实的父/checkpoint/报告/缓存，再按新请求的实际来源接入；不得用历史SHA造raw、冒尚未返回49或跨run接纳旧缓存。runner结束不是研究完成，接续编排正在完成。
