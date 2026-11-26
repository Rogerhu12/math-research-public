# Seed19 地点来源闭包与独立完整有限包络契约

## 1. 本文证明什么

本说明针对 run05 实际准入的 supported-unit fixed-normal 源，证明其**任何已执行前缀中，新增永久物理地址的来源范围**。它不假定 seed19 已完成初场、几何扫描或方向，也不借计数推集合相同。截至23:11 UTC，公开实际仍是 seed19 running、只返回到18；日志下载实体 HEAD 为404。

结论是同一个实际输入内的来源归纳：永久曲率、半径、幅度地点都包含在初始继承地址与完整有限 observation 格的并集中。此结论允许设计保守的隐式永久包络；它**不证明原192行选择和所有 protected 优先顺序可由一次最大值替代**，也不自动证明另一个 runner 的浮点地址逐字相同。

本文是既有完整来源的应用说明和一个独立新算法合同的设计；未运行科学计算，未替换任何已刊源、队列或 guard。

## 2. 精确来源

| 来源 | SHA256 |
|---|---|
| 完整 seed19 driver `fullclosed_supported_unit_normal_lift_so3_qp.py` | `e482428ee68aefa23da5b3b5c0a6b3363f047b0457f67a9193044ef151caec35` |
| 完整 world geometry `so3_supported_unit_normal_lift_geometry.py` | `d84b540d21622d4d609efa5ea85fef432a2dcebb51bea0f3c7c24376294918f4` |
| 原完整192选择器 `fullclosed_point_inequalities_v2.py` | `e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8` |
| 原曲率与 `pick_extremes` | `a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854` |
| 原完整报告地点 walker `launch_refinement_from_full_report.py` | `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60` |
| 完整 normal operator | `5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67` |
| 完整 supported-unit base | `e1bb7303540b1e807176ca5e71dcb2798b3f1e4e34909cd207cea300a9d4ebc0` |
| 完整固定 seed provider | `30ea80ec0673f3bdff3e59b97dfb5f7166a296aeb4b989fbca18b2feb5e9544c` |
| 完整固定 seed mean kernel | `bd9c0761e101679b10ff52d50f27a3dfb964687130c59878d756389b304ee771` |
| 完整 reference producer/context | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| 原 observation-plan source | `26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d` |

上述小源码均逐个小于100KB。检查使用完整来源文字、指定函数和纯 AST；没有读取未知大型 runner 报告。

## 3. 同一输入的精确集合

固定这个实际 run 的 carrier、mesh、N和 frozen material chart。定义地点键

$$
\operatorname{key}(c,u,\phi)
 =\bigl(c,\operatorname{hex}(u),\operatorname{hex}(\phi)\bigr).
$$

这里的 $u,\phi$ 是实际二进制64位字，不作 decimal round，不移动到附近角，不以当前逆图内部角 $\phi_c$ 替换材料角 $\phi$。

令 $P_0$ 是 driver 的 `all_locations` 完整处理所有显式 manifest、准备输入和适用 restart 后，两初始 memory 的地址并集。初始 protected 标签另外保留；不要把 $P_0$ 仅定义为 warm 文件中的少数地点。令

$$
G=\left\{
\bigl(\mathrm{observation\_cells}[p],
       \mathrm{observation\_u}[p],\mathrm{phi}[a]\bigr)
 :0\le p<P,\ 0\le a<N_q
\right\},\qquad E=P_0\cup G .
$$

$N_q$ 是这个完整 operator 的 quarter angle 数，包括两个端点；这里原 full N2048 给 quarter N513。定义用实际数组，未用 `P*Nq` 计数声称地址唯一或相等。重复径向地址在集合中自动合并，但每个 original positive metric observation 的权仍保持，不能借地点集合合并去删度量行。

**来源命题。** 对该 e482/d84b/e783 实际输入的任意执行前缀，每个新增永久曲率地址、永久半径地址、返回的 body/witness-distance 工作候选地址、几何最坏地址、线性几何行的实际曲率/半径地址，都属于 $E$。帽高度和固定 core 直径备选是保留的标量约束，不被伪造为地点。该结论不要求执行前缀已成功返回报告。

## 4. 完整来源归纳

### 4.1 入口和精确身份

e482 `all_locations` 先核实际 carrier SHA。带 grid tag 的报告还须显式 N 与当前 N 完全相同，再由4d9的完整 `Locations` walker 抽取并按实际 carrier 解析。两初始数组均非空；所有 protected 地址保留，未使用 round13 或任意 byte cap。所有这些实际入口地址都在定义 $P_0$ 内。

e482 `add_location` 只有两条合法来源：原字面的 `cell/u/phi`，或实际 `stage/angle` 按 q 的 carrier/phi 转换。它只校验、按 hex 去重和 OR 合并 protected，不插值、不求新极值位置。d84b 的 `_location`、`_remember`、`_grid_location` 有同一性质。

5297 `grid_fields` 只调用 `fields_torch(x, grid_query, phi[begin:end])`；`point_fields` 只调用传入的 `_point_query(cell,u)` 和 `[float(phi)]`。物理场的逆图、mean Newton、normal 隐式根、bubble/gamma 控制、积分节点等可改变读取的场值和导数，但没有把其内部坐标插入永久物理地点。

### 4.2 全格扫描和新极值

d84b `_ensure_grid` 覆盖每个 quarter angle block，逐点读取六个 world jets、两条主曲率、半径和两符号 witness distance。重复角块或缺角会拒绝；未全覆盖不会返回 complete。

所有该方法的新地点来自 `unravel_index` 后的 `_grid_location`：最大绝对主曲率、最远半径、body-diameter pool和双符号合并 distance pool均如此。`_block_candidates` 虽可扩大待选 top 数量，其全部候选仍是已有二维数组索引；它不沿连续 $u$ 或 $\phi$ 搜索。

a2a5 `pick_extremes` 只有 `argpartition`、排序、`unravel_index` 及离散索引间距排除。它返回原数组索引。因此曲率 top16、半径 top2和最大值补入地址全部在 $G$。

### 4.3 任意旧点、角色迁移和失败路径

`scan` 首先把传入的两组 memory 合并到内部 append-only 两组 memory，然后在全格之后遍历两者并集。任意点循环只能复用这个并集中的已有地点。循环产生更大曲率、更大半径、body/distance pool候选时只复制其地点，没有生成新坐标。因此归纳假设下这些候选仍在 $E$。

曲率和半径角色可能互相迁移：原 radius 地点也会被读取两条主曲率，原 curvature 地点也会被读取半径和两符号距离。因此保守包络必须把整个 $E$ 同时放入全部所需物理类别，不能只维护两个不交集合。当前算法的所有 scalar cap/H 约束仍要单独保留。

`_new_locations` 返回新增地点和 protected 升级；不驱逐任何旧地点。`scan` 的失败分支可能已经读完若干阶段或已加入新极值，它仍只返回现有内部 memory 的新增部分，所以失败或拒绝不破坏来源闭包。未返回不能解释成未发现点，但也不能产生这个来源闭包以外的点。

### 4.4 原192前缀和幅度行

e783 的 grid 曲率/半径备选来自上述 scan 的实际索引。arbitrary 备选逐个来自传入的永久 memory。`protected_current_representatives` 只在已有 witness_details 中选同 cell、角差不超过既定半径的当前最大者；它不挪角、不插值、不创造径向值。候选的 strongest-D、替代半径 partner和两个曲率 branch都是现有地点或固定标量。

d84b `build_rows` 再次真实 scan 当前父，调用该完整 e783 生成原前缀。幅度行只取已真实扫描的 body/distance pools；每个 selected distance 地点保两符号；cap/H另保。后者在同一 mmap 末尾追加，没有重写原前缀。

完整行 metadata 可能使后继4d9 walker将某个地点升级为 protected：`protected_inequality`、`protected_current_representatives` 以及其中的 seed/current_location 都有作用。这些**标签变化确有算法意义**，但其地址仍来自 $P_0\cup G$。不能把它们因地址已在全格中就删掉。

### 4.5 全 driver 控制流

e482 的 `scan` 包装器每次调用 d84b 后立即 `remember` 两类新增地点。它用于初场、每个方向开始的同父重读、所有达到真实几何阶段的 ray trial，以及最终场。拒绝 trial 的发现也被保留。下一个方向先重新扫描当前父再构造 C；最终又完整重读。metric和Phase I均调用同一套完整来源，没有另一个连续地址搜索器。

来源归纳从 $P_0$ 开始，对这些操作封闭。因而即使执行在某次失败、QP或场读取中被截断，所有已经通过上述代码记入的实际物理地点仍包含于 $E$。

### 4.6 内部根记录不能当空间点

已定点核5297/e1bb/30ea/bd9c的 metadata 和其构造：它们记录角批、normal阶段、控制值、mean记录、源/model/working参数；没有把 normal 根或 mean 状态解释为 geometry 的 `cell/u/phi`。纯 AST 补查这四源的 dict/call构造与下标赋值，没有新的 `cell,u,phi` 三键或 `stage` 搭 `angle/phi` 的物理地点写入。该补查只是来源审计，不是数值测试。

后继完整 walker仍必须绑定所有入口 provenance 的实际 schema，不得对未知外来 JSON 只凭这段静态性质宣称“无新增点”。本命题的 $P_0$ 已包含所有实际给 e482 的合法初始历史；没有把任意未知 payload 纳入已证明闭包。

## 5. 隐式全包络的数学责任

新的独立消费者可把 $E$ 本身设为从开始就永久保留的有限集合，用 carrier 的笛卡尔积加显式例外 $P_0$ 表示，不把数百万地址抄入 Git。对**每个新候选场**重新读取全部 $E$；旧场读过不支付新场的值。

令

$$
D_E(x)=\max\{2,2|H|,2\max_{r\in E}|F_x(r)|\},\quad
K_E(x)=\max_{p\in E,\,b\in\{0,1\}}|\kappa_b(x,p)| .
$$

必须实际检查 $0.03D_EK_E\le0.992$，每个 $p\in E$ 的 body 上界和两个 witness-distance 下界，以及原帽/H标量条件、域和真实同-Phi下降。因为每个可能的旧 memory是 $E$ 的子集，完整 $E$ 的这些真值不等式蕴含所有那些旧有限地点的同类型真值不等式。两条 curvature branch、两符号 distance、所有 radius伙伴和完整自由变量都未消失。

这是有限条件的保守蕴含，不是 reach、嵌入或连续 metric 证书。它不改变固定 $g$，也不自动支付每个物理 $t$、全域连续消费、root/积分误差或固定问题精化。

## 6. 原192前缀与未知 protected 的诚实新契约

旧 e783 把每个显式 protected seed的 strongest-D 当前分支以及当前邻域代表列为 required；超过192时会明确失败。未知 seed19 的行 metadata可能把某个新格点晋升为后继 protected。仅保持相同 nonlinear最大值，**不能保证下一次 e783产生相同 required rows 或排序**。

因此有两种可审、必须分名的后继设计。

1. **完全保留旧线性 required 语义的保守扩展。** 把所有可能 protected 地点的两曲率 branch和所需半径伙伴都列入一个隐式当前父线性不等式族。原已知历史产生的192前缀固定不改；新增族必须由完整方向导数/分离器或虚拟行算子真正消费，不能只写 metadata。每个 proposed QP方向在全部该线性族上复读，有违规则在同一父追加完整行并继续。预算耗尽时只能报告未完成该线性可行性检查；不得把未检查称通过。这保守族可能很大，现有 e783本身和仅top选择代码没有实现它。

2. **显式独立工作集政策。** 所有 $E$ 均永久承担全部 nonlinear类别和“可能曾被保护”的来源责任；新 selector明确把重要行策略改为当前完整 envelope 的全局/分区最坏行及完整真筛驱动的分离。原已知历史的完整e783前缀可原样保留，再追加新政策选出的完整行。此时数学有限约束未缩减，但未知旧 protected 的逐点 required 优先语义已经改变；必须使用独立 source/schema/policy identity并在报告明确说明，绝不能把新结果冒为旧 e783逐行等价或将未知保护标签写成false。

后一设计并不允许无限期忽略真实违反点：每个候选仍要遍历完整 $E$ 真筛，拒绝后其完整类型和实际地址保留并参与后续同父构造；所有接受门保持。全新 selector需要给出明确源、完整参数和实际输出责任。这是换完整求解机制，不是借“内存覆盖”减少筛查。

## 7. 跨 run 的尚未支付边界

上述来源命题首先针对**同一个实际 carrier与角字**。run05公开的是 carrier整NPZ SHA `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`，并没有公开其 `observation_cells/u` 独立数组hash。旧公开 fingerprint证明了明确输入和已有地点集合身份，未把整NPZ摘要拆成子数组摘要。

4e/26f源码保证本配置没有微小 lift split，径向计划由完整legacy端点/中点及每胞六个 Gauss unit nodes组成；角字来自固定 quarter公式。它们给出结构闭包，**同argv、同P/N或同代码本身不足以在未核实际字节时声明两个 runner 的全部浮点数组逐字相等**。旧source和一般NumPy版本也不能替代已有实际数组证据。

07已有必要warm/reference可以先运行；下一消费者若声称继承旧 $G$，还需一种完整、诚实的地址绑定：例如确切旧carrier/必要地址生成参数的实际证据与新数组逐字比较，或一个明确同时包含两套真实字面地址的较大集合。不得从旧hash造raw、把pending报告填空，或在不支付完整包围时把连续邻域称已经逐点读过。

若旧05最终无法取回当前raw，不应因此无限重跑同一超时 seed；可继续上节独立机制研究，但未验证的跨run地址责任须保留明确记录，并由实际更强的完整消费者/连续证明支付，不能自动标作“原历史全集已重读”。选择该政策属于根代理对完整新输入和算法的明确决定；本文未擅自修改现有准入或实际验收。

## 8. 已完成与未完成

已完成：上述精确小源审读、入口及内存更新的来源归纳、对 e783保护语义的区别、完整有限非线性包络蕴含、两个独立后继合同以及跨run实际身份边界。未完成：任何新包络消费者源码/科学运行、seed19最终状态判断、跨run旧G字节一致验证、任何连续认证或课题完成声明。

## 9. 根代理的明确政策选择及已实际返回的07边界

2026-11-26 23:40 UTC，Astra-larger-e4e2a2bf-20261126明确选择第6节的第二种**独立工作集政策**继续构造完整求解器，不把本文停在待用户选项上。逻辑上的全部 E 从开始永久保留，同时承担两曲率分支、半径/body和双符号 witness-distance 的完整非线性条件；原所有帽/H/自由变量/真实同Phi与完整度量行继续保留。已知 P0 的完整 e783 前缀保持，再由独立 source/schema/policy 的完整全格/分区最坏及真实违反点分离器追加完整类型行。每个候选仍完整重读 E；实际拒绝或违反的类型及字面地址必须保留，并参加后继同父构造。所有 G 的未知旧 protected 状态记作“可能曾被保护”，绝不猜成 false。

这项选择明确改变未知旧 protected 的逐点 required 优先次序；不宣称新线性行、192容量行为或旧QP逐行等价。它保留第5节的全部有限非线性条件，而不把非线性蕴含冒充旧线性 required 语义。新完整源码、完整参数和实际返回将单独登记；本段不是未运行程序的成功记录。对05第1–18步的其他旧生成器，后继入口还须引用其各自完整来源闭包与全部真实初始 payload，不能仅用本篇 e482 第19步的证明替代。

07真实 Actions run `45909290354/1` 已返回 warm 与独立4e reference两步，均 returncode=0。完整紧凑卷 `2026-11-26-public-actions-45909290354-1-part-001.md` 为22619B，SHA256 `94ba3a5dac8397466e6b328683bb7739754e25c4c70347aef2502e99adcdab15`；reference实际来源commit `d2fa260c0adde7c89e94a96cafc8be03ced3a091`，29792B report SHA256 `78411d9a91633816fd514b927d288ad17922b67eca0f5bd4fd400ec3a06b1821`。这些是实际返回，不是本文推算的数组。

| 实际07对象 | 完整SHA256 |
|---|---|
| warm NPZ（与05相同） | `3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c` |
| 完整scalar数学参数（与05相同） | `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` |
| node report（与05不同） | `1820f7c37d54e615c678c688da44c2f5aa0c1d7f4b0ebc00d3bad681dab59aa0` |
| scalar原始文件（与05不同） | `931565a140891ecd6dedf579b778f3c95ab5172b1deeeddc892c1f1552c7d159` |
| reference NPZ（与05不同） | `e435343954ed3c9fd2617e36185a1e0a71213cc6b432eb94578066954930c5db` |
| observation carrier NPZ（与05不同） | `7c8b3cbffd66a360b01341db8e1179f211da3c264de85812020a5e48ad5637c3` |
| reference model（与05不同） | `d10049842d5a4d661f7c458066771cfd6a52642c2730fc1bce46a2566a9a8722` |
| 实际旧payload完整provenance | `2a536f54bf3e41d10797f8706837f813871cd8c7cc755421a6bb1dd7936cc983` |

这些实际事实只允许 R706 已证明的同准确scalar参数关系；不允许把旧工作场、旧数组字节、旧误差或地点全集自动迁证到07。07在300秒scalar预算下实际1872叶、scalar_tolerance_reached=false；05对应真实2397叶。这提供一条必要输入再生途径：用原精确整数/Fraction优先细分顺序、完整原参数、真实记录的2397叶重新生成旧载体候选，并仅在整个 NPZ 摘要真正等于原 dc5 时允许读取其旧地址。旧node/scalar文件不能用当前文件冒名；完整来源区别、确定性证明、原profile定义标签和最终整SHA门槛必须由新重建源保存。该必要消费者在本次登记时尚未执行，旧G跨run字节责任仍未支付。

23:38:31 UTC的实际 GitHub API 已确认05 run `45870334713/1` / job `140083791897` completed/cancelled，科学step5亦completed/cancelled。公开完整索引仅1–18步返回；第19步确已启动而无完整报告，第20纯读无返回。终止不能解释为无新地点，更不能补写成功或失败数值。新政策和必要载体再生将承担这个明确的未知责任，不重跑旧seed来假补空历史。07仍继续，06也在继续；本课题未完成。
