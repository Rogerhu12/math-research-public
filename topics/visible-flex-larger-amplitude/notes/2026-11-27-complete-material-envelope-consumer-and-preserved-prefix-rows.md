# 完整材料包络消费、原前缀保留与独立 typed 工作行政策

## 1. 本条实际完成的工作

本条交付四份完整小源码。它们把已选定的独立包络政策真正接到完整世界坐标六 jet 真筛和原自由参数协向量，不只给 report 添加一个“历史已处理”字段。

源目录为 `scripts/resume_20261126/`。本文所述版本如下：

| 完整文件 | bytes | SHA256 |
|---|---:|---|
| `complete_material_envelope_memory.py` | 40091 | `c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152` |
| `complete_material_envelope_rows.py` | 13744 | `729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7` |
| `so3_reference_centred_c1_material_envelope_geometry.py` | 65678 | `bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f` |
| `derive_complete_material_envelope_geometry.py` | 22407 | `929ac2189cfe168d5beb9e0f3f09ee91ad69142973f057fdab7495f83718485e` |

完整 geometry 由实际 C1 父体 `353196a4faadc7537d04d6be139c9d9d8f47ee7e25e1f007e33588ac48cfa0ff` 派生；纯标准库 deriver 重新生成整份新体并逐字比较。原父的源守卫、reference-centering、C1、固定 seed、全 free-core/rotation/H 以及六 jet 原参数 pullback 全保留。新的 driver/launcher/reader 单独绑定这些真实新源码；旧锁定代码不被覆盖为另一个身份。

本地只实际执行了 AST、compile、重复字面 dict-key、尾空白和完整 source derivation 比较；没有 F/J/root/QP、数值 fixture 或科学试跑。消费入口的实际数值返回仍须由公开 Actions 给出。本条不宣称课题完成、metric 合格、全 $t$ 几何认证或新机制收敛。

## 2. 为什么需要新的明确政策

run05 的 seed19 确已启动，但 job 终止时只公开返回到18，没有取得 seed19 的完整科学报告及未知末态。不能把缺失报告当空集合，也不能假造它的 protected 晋升、具体 typed 行、排序和数值值。

已刊来源归纳给出物理地址闭包。设 $P_0$ 为完整原11个输入 payload 的已知地址并集，$G_{05}$ 为旧实际 carrier 的径向字与完整 quarter 角字的笛卡尔积。所有相应原几何扫描、真筛和分离产生的物理地址都在 $P_0\cup G_{05}$ 内。这里的地址是固定材料坐标 `(cell,u,phi)`；内部当前法角、mean/normal 根坐标、控制变量和积分中间节点不被偷偷当作物理见证地址。

这只证明地址集合包含关系。旧报告可能把原 radius-only 的 $P_0$ 地点晋为 curvature/protected，所以未知角色变化也可能发生在 $P_0\setminus G_{05}$，并不限于网格。新政策明确将**整个**包络的所有点视为潜在重要点，保留全部已知 protected 前缀，并采用新的当前 typed 分离规则；它不声称重现未知旧标签和排序。

旧05实际1–18的完整来源补篇另列全部实际 producer/schema 及它们的角色路径。本组件不把 seed19 单一源码的归纳冒充全部旧输入归纳，也不拿1250/208/18这三个数代替集合身份。

## 3. 真正消费旧 carrier 与全部原11个 payload

输入不是一个“假定新旧同格”的布尔值。consumer 实际重新读取两个完整 NPZ，并在读取前后核其整文件 bytes/SHA：

- 旧 carrier 必须是原实际 `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`、227202 bytes。
- 新 carrier 必须就是当前完整 field 实际消费的文件；其全部 `observation_cells` 和 `observation_u` 字节须与当前对象中数组逐字一致。
- 两者的实际 mesh 都须匹配原完整 mesh。固定 chart 的160个实际 binary64 core 字、原完整 warm、实际 scalar 参数投影也分别核对。
- 精确读取全部7377个 cell/u、1845 legacy、6个真实 Gauss unit 字，不重新通过一个近似公式猜出它们。验证原未切分载体的全序列：每胞 node/midpoint，末端，再逐胞六个真实 Gauss 字。
- 角数组的513个实际字逐一与 `binary64 pi * j / 1024` 比较；不从“使用同 N”推断角字身份。

旧 carrier 的必要重建器是完整 `ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e`。它只有在整个旧 NPZ 命中原 SHA 与 bytes 后才产生 `material-envelope-carrier-path-binding-v1`。本消费者仍重新散列和读取数组，不以 producer 的 true 代替自己支付实际读取。

原11个 payload 也没有被原1250个 tuple 的数字摘要替代。consumer 从当前真实 preparation 所绑定的完整 `supplied-location-provenance.json` 读取原始11份 payload，保原顺序、原 role 特例、四类 indexed location 数组展开及完整4d9 walker；然后用**旧**实际 carrier 解所有 tagged stage。三份全字集合的 count 与 canonical SHA 都必须匹配已公开原证据：curvature、radius 和 protected-curvature，任一不符均不产生“完整原 P0”声明。

当前 preparation 的完整 `locations.json` 也被强制读入，不依赖调用者碰巧再传一次 `--manifest`。所有显式 caller manifest 及真实 restart 完整报告仍按原 walker 全文消费，不能因有包络而被丢弃。历史值、旧几何证书或旧 field 一概不迁移；每个地址在当前场重新读值。

截至真实 run07 第3返回，必要旧 NPZ 已命中原 dc5；旧/新 cell、u、六 Gauss 数组也确实逐字同。这一实际事实允许该次执行的 extra-old 径向集合为空。源码仍保真正的非空并集分支：若以后兼容载体的旧/新径向字不同，将实际调用当前完整 field 在所有 extra-old 径向点及全部角字上读六 jet，不把“新网格已扫”当作旧网格已扫。

## 4. 完整隐式永久集合与真筛

记本次所有实际显式输入的地址并集为 $P$。消费者保持

$$
E=P\cup G_{05}\cup G_{\mathrm{current}}.
$$

所有地址使用 `float.hex()` 的实际字身份。已知 protected 升级只做逻辑或，没有舍入去重、逐次删减或永久集合容量上限。整个隐式格无需展开成数百万个 Python dict；它以完整径向字、固定角字及已读数组身份表示。

每次完整 scan 实际读取：

1. 当前全部7377径向观测 × 全513角的六个世界 jet；
2. 旧格中不属于当前径向字集合的每个径向点 × 全513角的相同六 jet；
3. 所有显式 curvature/radius 地点的并集，包括原非格点、protected 点及后续发现地点。

每一实际点都同时读两个 principal-curvature branch、半径以及到两个 witness 的距离。对这三部分取共同 max 后，才组成完整 reach product、body、两符号 distance、cap 和 H-floor。没有把某点原本只列 radius 当作免读它的 curvature，也没有以 orbit multiplicity 替代两 witness 符号。

新的 geometry 还分别保存 body、distance-plus、distance-minus 的真实最坏地点。原 pooled distance top 的有限工作集继续保留，但不会被错误地叫作两符号各自的 argmax。

原 C1 `fields_torch/grid_fields` 还实际返回 `centered_closure_residual`，shape为 `(angle_block,3)`。新 geometry 明确接收这个第三诊断，同时验证 rho0 和 closure_delta 的原 shape/finite 条件。它们不被当成六个物理 jet，也没有放开任意未知键。该修复只在独立新源码中；原父 body 的旧白名单不被重新标成已经通过。

完整结果都有新的 `material_envelope` scope。只有上述每项完成才给 complete=true。提前失败也返回真实 attempted full-point SHA、实际 complete/partial flags 和错误，不借上一次点的 token；首次 field 尚未读时全局 metadata 是 pending/counter0，而不是“已经全筛”。pure validator 核实这些实际范围，不填补缺项为零或 true。

## 5. 原前缀与新增行的精确关系

新行并不重新选取或替换原已知前缀。先执行原完整 e783 192-cap selector，保当前已知 protected 与必要地点；再执行原完整最多12幅度行构造。随后才在**同一个 mmap 文件末尾**追加新行。

完整记录满足

$$
n_{\mathrm{total}}=n_{\mathrm{original}}+n_{\mathrm{amplitude}}+n_{\mathrm{envelope}}.
$$

其中 original 与 amplitude 字段原义不变。新增 `known_geometry_and_amplitude_prefix_rows`、`envelope_rows_start_index` 和 `known_prefix_bytes` 指明旧前缀的实际边界。代码在扩展前对完整前缀实读 SHA，扩展后再实读同字节范围核对；所有写入仅落在新后缀。没有复制一份第二个完整前缀 cache，也没有声称只按行数就证明逐值未变。

新增 near-active 部分先考虑每个当前/旧额外胞、每个 curvature branch 的实际最大值，再按同一父的物理 $g$ 和精确地址 tie-key 排序，取显式 cap32。`active_band`、全候选计数、真实被取行数及 cap 原值均写 report。32只限制这部分**当前临时**工作行。

另一部分是新政策实际分离出的永久 typed 行：完整 scan 若 reach 正违反，保存其真实全局最坏地点及实际 lower-D partner，并保两个 branch × 两个符号；若 body、distance-plus、distance-minus、cap 或 H-floor 正违反，保存该家族实际最坏行。所有这些已发生分离记录不驱逐、不受32限制，并在后续每次构造于当前完整父点重新计算。

没有宣称每个网格正违反点都已被逐行 materialize。其他点仍属于每个候选必须真实读取的整个 $E$。永久 typed 集合只指新政策实际选出的最坏分离地址；全网格逻辑约束与有限线性工作集清楚分开。

## 6. 完整原参数导数与 common slack

对固定的一对实际物理地址和所选 principal branch，使用两个有符号必要不等式

$$
g=\rho D_{\ell}\sigma\kappa_j-s_{\mathrm{safe}}\le0,
\qquad j\in\{0,1\},\quad\sigma\in\{-1,1\}.
$$

当 $D_{\ell}>0$ 时，两符号合取等价于该 branch 的绝对值版本。其完整 free-parameter 微分是

$$
dg=\rho\sigma\left(D_{\ell}\,d\kappa_j+\kappa_j\,dD_{\ell}\right).
$$

直径 lower partner 保真实三类：固定 core 的常数2；cap 的固定符号 $2\sigma_H H$；实际半径点的 $2|F|$。后一类的 F-covector 是 $4F/D_{\ell}$。从真实六 jet 广义 principal-eigenvalue cotangent 出发，调用当前新场完整 point_vjp，再经过原全部 H² 坐标 transpose；不漏 free core、所有 rotation 自由度或 H。

数值所选 eigenvalue 必须有严格正 finite principal gap 才使用这条 simple-branch 导数。gap 不可用是该数值线性行构造的责任，不是数学几何不可行证明。原 nonlinear screen 仍同时读两 branch；阈值不放宽。

body、两个 witness 距离、cap 和 H-floor 直接复用完整当前 `_amplitude_row`。特别是 witness $p=(0,1+\sum c,0)$ 的全部 free-core 额外导数在坐标 transpose 之前支付，未冻结 $p$。

每行只除以其真实正坐标梯度范数；零梯度保 scale1。原 common-slack Phase I 接收完整新总行数，故正违反的零步不被假称可行。原母范数、阻尼、目标、全空间变量和真实候选接受门保持；新有限线性行不代替真正非线性复读。

## 7. 同父、重启与费用

新增行要求当前 scan、current full-point SHA、q model、envelope model 和原 row-prefix 当前点全相同。固定某历史 partner 时只保地址/branch，导数与物理值全部在当前父重算。第一次根或 field 失败不会产生虚构 rows。

完整新源的 restart 仍由 driver 原 schema/source/model/norm 守卫约束。consumer 额外恢复整份 typed memory，核其 canonical SHA、每个 family、branch/sign/partner 形状和首次发现点；不从 report 中只取一个计数。当前 counters 明示进程范围，已恢复的永久约束计入相应 memory。

费用由真实 report 记录：完整 current/extra覆盖、永久点读取、追加 row 数、实际 mmap bytes/allocated bytes、完整前缀两次实读、真实新协向量及耗时。旧/新径向字完全相同时 extra为空可以少做相同地址重复读，但这来自实际字比较；不以 source相同或 NumPy版本相同代替。

没有先行宣称该实现更快或更易收敛。选择32和每胞最大策略是一项显式新线性政策，不是严格全域可行定理。

## 8. 完整入口合同

消费者返回

```python
load_memory(args, preparation, q, history, *, restart=None, source_report_path=None)
    -> witnesses, radius_witnesses, history_record, envelope
```

新增参数为 `--material-envelope-binding`（当前 carrier不等原dc5时必须提供实际 path-binding）及 `--envelope-near-active-rows`（正整数，首值32）。真实 run07 的绑定路径为

`{work}/run05-actual-observation-carrier-restored/material-envelope-carrier-binding.json`。

GeometryScreen 显式接收 `envelope=envelope`。report 初始保存完整 metadata，每次 save_report 再取独立新 snapshot；旧 trial 的 metadata 不被原地修改。两份 pure validator 均只用标准库，读取 source-closed 实际字典，不调用 field、J、root或数组求值。

当前 geometry 仍为原 R715/C1 工作场；原 closure lift、当前 raw defect、全部 $F_s$ 行和所有外层参数链不删。全 $s,\phi,t$ 连续误差、准确根分支、数值求积、真正 reach 和固定参数精化仍须分别支付。本条是持续求解所需的完整消费与线性入口，不能当作课题 README 完成标准已满足。
