# R90. 同一实际闭图在全域、全部相位上的连续 metric 门

## 1. 真实结论及范围

对 R82 已声明的 `λ=.002/M24`、879 节点、`.12` cut、字面总短柱长度
$$
 \ell=\frac{5764607523034235}{1152921504606846976}
$$
和原 canonical 双帽，现已完成整个闭曲面及所有相位的连续证明：
$$
 \sup_{p\in M,\;t\in[0,1]}
 \left\|g(p)^{-1/2}\bigl(F_t^*\delta-g(p)\bigr)g(p)^{-1/2}\right\|_{op}
 \le 9.97128585114805\times10^{-7}<10^{-6}.
 \tag{1}
$$
同一个界也已实际传递给 R89 更强的固定双帽族；它的目标度量只在两盘上一次性改为新帽的准确图度量，并对全部相位保持固定。

这里使用真正原 raw-H 的 unscaled full-H 尾，accepted packet SHA 为 `81f6eb0f…`，完整几何 bundle 为 `3b312be5…`，整个 mean 为 `161eec0d…`，原前缀 source run 为 `1ad16826…`。本条不把它改称正在另行求解的八轮 coupled final physical-H 场。全部完整 SHA、来源与实际退出码见[实际小记录](../notes/2026-11-28-complete-closed-all-phase-metric.json)。

实际输出已经落盘并返回：

| 完成项 | 真实终态 | 证书 SHA256 |
|---|---|---|
| 1152 段完整有限尾补充 | session 47300，exit 0 | `d06869756f00b1ca37efcd5e67b61da906f5d483aead4d8f8aace9f9e69a6ab6` |
| 原 canonical 完整闭图聚合 | 实际 child exit 0 | `57ef6e7a86ab6ad6206df6134be31c8c9b174858a69482ac7a4c7b0fba49286a` |
| R89 新固定盘目标传递 | 实际 child exit 0 | `8f02cdd036a5ddc06662691365a77de485392ba33c84b6a346346bf7f6d16d54` |

后两项的唯一 watcher session 45524 也真实 exit 0，原样保存两次命令、实际 child 退出码和控制台 SHA；没有把启动、已写中间文件或未知终态当成验收。

## 2. 实际有限场和完整库存

有限尾的定义仍是同一份完整谱合同：512 个原独立角节点导出的 170 个平面模式、25 个含 mean 的高度模式、字面有限次数 254；Gram 的完整频率范围可达 508。径向仍是原共享字面半径节点和完整 Cartesian 两 jet 的准确五次 Hermite 图。保存的有限 Fourier 场就是这里受证的实际图；没有假设它等于连续源 evaluator 的全部 Fourier 展开，也没有把连续源的投影误差设为零。

完整 1152 段具有 **18460 个原始径向 spans**。额外 28 个 stationary 节点已包含在这份实际库存中；没有把它简写成 `1152×16` 而漏掉节点。

原完整几何证书已经付清其中 **17644 个 spans** 的 metric 门。本次一直按原 span 身份直接复用其证书和准确值，仅为原未付的 **816 个 spans** 生成同图的 true-`w` Taylor 补充。最终 816 个 spans 具有 **817 个证明叶**：唯一额外二分是 stage 22 / original span 16 的 `[0,1/2]`、`[1/2,1]`。这是证明区间二分；没有插入新的曲面节点、改变多项式或修改 mean。

相应混合库存为
$$
 17644+816=18460.
$$
所有原 spans 均恰好一次覆盖，全部相邻精确端点相接。旧已过证明没有为统一格式而重算。程序中的 1152 段循环是完整来源核验与 receipt 组装，不意味着对原已过段再次计算 Gram。

## 3. 原未付 spans 的严格 true-background 支付

有限尾沿用 R58 已声明目标
$$
 g_{\rm tail}=(1+w(R)^2)\,dR^2+R^2d\theta^2,
$$
其中 `w` 是受认证的真实背景函数，不是每个 span 上冻结的常数。

已发布的 `tail_metric_true_w_taylor.py` 保留同一实际有限图、完整共享 mean 和全部模式，只在 Gram 证书中用带严格余项的真实 `w` 一阶 Taylor 表达替换过宽的常数包围：锚点值和导数的不确定性都进入误差，跨背景 piece 边界时保留全部一侧二阶导数的 hull。补充项由原字段的完整导数界支付，未忽略相关余项。

v2/v4 的选段门逐项核同原 bundle、stage/status、完整 spectrum container、physical parameters、map hash、原字面半径区间和 source knots；额外 stationary 接收节点使用它的真实 `receiverOriginalSource.sourceX`。各原区间的准确实际范围由原 monotone primitive 合同覆盖。

参数 `quadratic_mode_cutoff=12` 仅决定哪些二次乘积显式作有理多项式合并。其余二次项仍在完整严格 remainder 中保留，所有 170/25 模式都存在于同一个实际图中。它没有把未知、图、H 或 Gram 削成 12 模。

每个需补 stage 还实际核验了将 `wpoly` 退化为原常数时，`metric/components/merged/quadratic_remainder` 与原 Gram 内核**准确相同**。因此这里改变的是同图证明的包围方式，而非另换目标度量或放宽门。

各叶取对整个实区间和整个角域有效的 Fourier/多项式上界，合并为归一化 Gram 对称矩阵的 operator 界。完整 phase 的参与沿用原实际 phase/chart 合同；有限尾的角平移与正交坐标变换不改变其归一化 operator 范数，全角界随之覆盖全部相位。没有用几个离散 `t` 或角点替代连续相位证明。

## 4. 完整来源核验及历史终态的区分

v4 在恢复时实际继承了旧 A/B 的 **62 个完整阶段**和已保存 **526 个证据文件**，逐字节核其 SHA、长度、精确覆盖、全部来源和原门。旧 v2 存储交接的真实 exit 130 与旧 v3 session 79580 的未知退出码分开保存；后者到现在仍为 `null`。数学上可继承的已完成证据，不依赖给中断进程编造一个终态。

最终独立 `closed_map_complete_metric_recovery_v2.py` 先要求有限补充已经真实 `complete`，再核原 v2、v3、v4 三套来源合同的所有数学参数完全一致，以及完整 1152/18460 库存。它实际检查 **3122 个不可变证明文件**，逐项核旧证与新 Taylor 两类来源、每个准确分区、全部局部严格门和总数。

完整图仍使用原 `.12` cut 的真实 R79 证书，而不搬旧 `.04` 失败场或更早另一个前缀的数字。完整 radius identity 已真实证明 `c=Rc`，故近切口重参数化准确为恒等，不遗留一个未付的 pseudo-`R` 目标转移。

## 5. 从各连续域到整个闭曲面

同一实际闭图的覆盖分解如下。

| 区域 | 连续 metric operator 上界 |
|---|---:|
| 完整前缀和 `.12` cut（含原补集） | `9.899331346061256e-7` |
| 全部 1152 段 / 18460 spans 的有限尾 | `9.97128585114805e-7` |
| 同源深 collar | `1.4617380072747594e-29` |
| collar 内的未扰动旋转区域 | 对原声明旋转目标准确为 `0` |
| 中央同源短柱、平盘和固定标记图 | 对其声明固定目标准确为 `0` |

上下反射域具有相同 metric 界。中央柱用同一个准确单位速 material core，因此柱内目标为 `ds²+du²`；内侧未扰动旋转区域仍用原 R58 目标，平盘外帽部分用 Cartesian Euclidean 度量，canonical 帽用 `I+df82⊗df82`。前缀使用 R79 的同一个真实弧长目标与共同 phase chart。

公共圆和中央连接的完整 Cartesian `C²` 两 jet、真实弧长转换及目标身份已经在 R79/R82 和完整 node-index 验收中付清。本次 collector 再次绑定这些**同一**证明和字段，故上述闭域覆盖可以在接缝上直接合并；没有未覆盖的边界条带。

全部目标都对相位固定。对于任一点，取所属闭域的 operator 界；在公共边界，各图和目标通过共同两 jet 相容。因此全曲面的上界就是表中最大值，得到(1)。保存的准确最大值为
$$
 \frac{352373167283915878642769742048146729928583323001162610457636353416629463782464725075730745883114220084591668999029648199}
 {353387890533040178113381578125177740001105311530730266394825021409972856707600811564636873774314101999460097341611580797747200}
 <\frac1{1000000}.
$$
表中非零小数均取在对应准确有理界之上；实际记录保留原数值展示和准确分数，验收以准确比较为准。

最大值来自 **stage 94 / span 12 的原已过证书**。新 Taylor 的最大值在 stage 22 / span 16，严格小于 `8.095755e-7`。这也确认新补充没有用一个接近阈值的原失败上界冒充已过；全局最大者本来就在原已付集合中。

## 6. R89 更强双帽的同一固定目标

R89 保持两个完整平盘外的图及全部导数不变，只将固定图高度替换为准确 Fraction 定义的 `f89`。两个盘上的新目标为
$$
 g_{89}=I+df_{89}\otimes df_{89}.
$$
新盘的诱导度量与它准确相同，且相位不参与 `f89`；两盘 metric 误差严格为零。圆周上 `f89,Df89,D²f89` 都为零，原平盘目标和图的两 jet 准确吻合，所以这一定义与外部同一个目标拼成公共固定 `g89`。

真实入口 `sharp_marker_complete_metric_transfer.py` 已读取上节**已完成**的 canonical 全图证明、R89 准确 Bernstein/几何证书和真实完整构造器报告，逐项核同 source run、full-H packet、bundle、mean、cut、短柱、原 query、准确新幅度/半径和 source SHA。它实际返回新目标上的全图界仍为(1)，没有重新跑 native、BVP、Gram、活动矩或已付连续叶。

这里 `g89` 是明确设计一次的新度量；本条不声称它是旧 canonical 目标的固定问题精化。对选定 R89 族而言，全部 `t` 用的是同一个 `g89`。

## 7. 几何和非全等结论保持，未付事项不混入

补充过程没有改变实际图，故 R82/R80 的完整 `C²` 嵌入、全相位几何与 reach 继续适用；R89 又已独立支付新图的全部几何传递，保持 `K≤123/10`、正支撑和同一全直径/reach 预算。原完整尾在 stage 82 的 `K<10` 分配失败记录仍为 false；本条没有把它改成成功。

R84/R88 的原 canonical 非全等与定量端点下界，以及 R89 更强的完整欧氏群下界，也分别保持各自已证范围。原 native `normalizedFullDefect≈1.9643e-5` 仍是其原始 audit 字段；本条没有拿它代替连续 metric，而是对已声明的完整实际有限图独立付清了(1)。

**这里仍不是本题 README 完成。** 当前受证的是准确 `λ=.002` 输入所定义的族；准确 `λ=1` 的握持区和 `δ_hold/D≥.1` 未由本条获得。固定完整度量、参数和 phase 范围下的 mesh/mode/time refinement 下降到机器精度或求解容差仍需原问题的完整后继。未完成的 generic 八轮 coupled physical-H 也不继承本条 raw-H 场的证书。

## 8. 实际执行和复现

完整有限尾从保存的原已付证据恢复，源码为 `tail_metric_complete_supplement_recovery_v4.py`；它记录的阶段循环耗时 `2020.789238448` 秒不含启动预检，也不是所有历史求解/证书耗时总和。

随后真实顺序执行的两个入口分别为

~~~bash
python scripts/resume_20261128/tail/closed_map_complete_metric_recovery_v2.py \
  --closed-geometry <R82真实完整geometry报告> \
  --finite-tail-metric <v4真实complete summary> \
  --outdir <新的输出目录> --disk-reserve-mib 16

python scripts/resume_20261128/tail/sharp_marker_complete_metric_transfer.py \
  --canonical-metric <上一步真实summary> \
  --exact-marker-proof <R89准确Bernstein和几何证书> \
  --actual-constructor <R89成功完整构造器报告> \
  --out <新的输出JSON>
~~~

实际绝对路径 CLI、退出码及日志 SHA 已完整保存在 successor terminal 小记录中；两次真实墙钟分别为 `1.5857060979978996` 和 `0.03894778300309554` 秒。前者只核验已有证明及组合全域，后者只核验明确固定图替换的精确传递，因此没有把原计算成本隐去或冒称瞬时重算了全部连续证书。

完整数组、每个 span/leaf 证据和 receipt 继续保留在 scratch；入库只含数学源、完整证明文本及小标量/身份记录。实际全部数据的可恢复和原 SHA 合同保持。
