# 共享 Hermite 容器的单件预算与无损存储接口

2026-11-09，`/root/coupled_prefix`。

**状态：来源核查、存储层恒等性及旧 M12 包的纯字节检查完成；尚未适配或执行任何新几何生产者/数学消费者。**
本文补充 `root-final-m14-w14-entry-and-export` 的文件接口，不能替代其中真正关闭的
M14 输入、实际新图的连续证书、独立全流程或 G5。

## 1. 实际的大小门在哪里

`scripts/950f-root-fullxyz-hermite.py` 的 `build` 先把 `mesh,jets,mean_increments`
以 `np.savez` 装入内存，再 gzip，并在 145–150 行把一个 `-data.npz.gz` 写到磁盘，
随后才拒绝大小 $\ge5,000,000$ 字节。`db6f-root-mirror-hermite.py` 的 44–60 行
读取同一个包、执行已审中央镜像两 jet 修正、重新保存，亦在写完之后才作同一大小检查。
因此旧入口不是“自动分片”入口，也不能在失败时假定没有留下超大临时文件。

已经审过且此次只读使用的真实旧包是：

- metadata：`notes/2026-11-09-db6f-root-flat17-coupled-m12f24.json`，
  SHA256 `da43f85ee6715254cca3daddd609c80e23bdf97916acb9ba2034282c3c237c7d`；
- data：`notes/2026-11-09-db6f-root-flat17-coupled-m12f24-data.npz.gz`，
  **3,112,330 字节**，SHA256
  `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`；
- source modes = 12，保存的 base representation modes = 24，节点数 = 2570。

保存数组是 little-endian binary64：`mesh` 为 $(n,)$，`jets` 为
$(3,n,3M+2)$，`mean_increments` 为 $(n-1,)$。三数组的总原始字节数为
$$
8\bigl(3n(3M+2)+2n-1\bigr).
$$
这不是压缩文件大小公式。仅由未来 BVP 的节点数，不能严格推出 gzip 包会否过门；
更不能把先前失败时由 Jacobian 结构推断出的 5047 或 6344 当成已经保存的新图节点。

原构造取 `M=max(source_M,args.modes)`，其 `subdivide` 只增加表示节点。
降低 `--modes`、丢节点、重算 mean、改变 Fourier 提取或积分设置都会改变有限表示，
不是无损存储修复。特别是，不能为文件门把原已选表示阶 24 默降到 14，再把所得称为同图。
若以后研究另一表示阶，应另存新图并独立比较/认证，本文没有实施这种改变。

## 2. 只分割已经定义好的容器字节

新增 `scripts/db6f-prefix-shared-jet-byte-shards.py` 是纯存储模块。令 $B$ 为
最终镜像修正后原本应保存的**整个 gzip-NPZ 字节串**。它按连续、无重叠的区间
$$
[0,l_0),\ [l_0,l_0+l_1),\ldots,
\qquad \sum_i l_i=|B|,
$$
切开 $B$，再把每块独立 gzip 为 `.bin.gz`。默认原始块上限为 4,000,000 字节，
实际压缩块必须严格小于 5,000,000；这个判断在任何未来写文件之前进行，
不以某个未经检查的压缩率作为保证。

新 descriptor 明确使用独立 schema
`db6f-shared-hermite-logical-byte-shards-v1`。它登记：

1. 原逻辑容器的字节数和 SHA256、base 节点数及 base 表示阶；
2. 三个原数组的精确 dtype、shape、C-order 字节数/哈希；
3. 每片的连续 index/offset、原始片长/哈希、压缩片长/哈希和简单 basename。

类型门排除 Python 的 `bool==int` 混淆；未知字段、重复 JSON 键、非有限 JSON token、
路径越界名称、重名、缺片、额外片、索引不连续、字节空洞/重叠和末端覆盖不足均拒绝。
解码必须先按外层绑定的 descriptor SHA 和原逻辑 SHA 验证，再解压、按 descriptor
顺序连接，并核三数组。`allow_pickle=False`、有限性、严格递增 mesh 与保存形状均检查。
映射自身的枚举次序不影响连接次序。

**恒等性。** 每片是原字节串的精确切片；gzip 的解码返回该切片。连续完备分割的
连接严格等于 $B$。所以原 NPZ 的所有位、条目顺序、保存的正负零和 mean 增量均不变。
数学等价来自这个切片/连接恒等式；哈希是外层来源核查与损坏检测，不用“近似数值相等”
替代逐字节相等。当前测试还直接使用 `restored == original`，而非只比较哈希。

模块不导入几何源码，不求值 Hermite，不调用 source/root/RK/区间后台，不写文件。
`encode_bytes` 返回内存 descriptor 和内存分片；`decode_bytes` 返回内存中的原容器。
另有 `read_bytes` 为未来显式适配提供从已绑定 descriptor/分片读回的接口；此次没有调用
该磁盘入口，也没有生成任何分片或新几何 metadata。

## 3. mean 与公共 cut 的两个易混接口

原精确定义使用 `mean_increments` 的**精确有理和**。`jets[0,:,-1]` 中的累计值
只是显示量，不能因分片而重算并替换。本文连显示值也保持原位，没有重新序列化数组。

公共 cut 图的 `modes` 可高于保存数组的 base 表示阶。例如旧 M12 base 为 24，
其 critical-r01 公共图为 64，但仍引用同一个 base data。未来 storage reader 必须用
**base metadata 的 `nodes,modes`** 核原数组形状；不能拿公共 cut 的 64 去要求原包
有 $3\cdot64+2$ 槽。公共 cut 自己的补零、两 jet 修正和全 Fourier 账本留在原数学层。

## 4. 真实消费者和最小显式适配边界

下表来自此次实际源码读取，具体哈希列在同名 `-sources.json`。它不是说这些适配已经实现。

| 来源/入口 | 当前实际依赖 | 若采用分片，必要的独立新版本 |
|---|---|---|
| `950f-root-fullxyz-hermite.py::build` 与 mirror `build` | 单文件写入、镜像后重保存、写后大小门 | 新 producer 先在内存完成原两步表示，再调用 codec；新源与存储身份明确绑定，保存前检查每片 |
| `SharedHermite.__init__` | `data_file` 的 SHA、gzip、NPZ | 将读取的少数语句替为已核原逻辑字节；之后原 mean/多项式构造逐字保留 |
| `db6f-audit-continuous-hermite.py::ExactHermite.__init__` | 同一直接读取 | 新 storage-aware 读取入口；原 Fraction/interval Hermite 公式保持，需实际绑定新源码 |
| `db6f-root-common-cut-v2.py::install` 的类及 `make` | 各自再次直接读取 base NPZ，不能只改 superclass | 两处都从已绑定 base storage 读取；原完整 Z、径向链式、公共 cut 两 jet 公式和 schema 数学门保留 |
| `db6f-audit-prefix-angular-metric.py::validate_inputs` | base 文件 hash、直接 mesh 读取、baseline/target/source 身份门 | 新验证器分别核 logical SHA、descriptor/全部片 SHA 和新真实 source 身份；不能让 descriptor 冒充原 NPZ |
| `db6f-audit-terminal-error-gate.py::candidate` | 414 行直接要求 base `data_file`；同时严格核 mirror/common/backend 来源 | 新 verifier 显式核存储闭包与 logical SHA，并接受经过审查的实际新 producer/reader 身份；原 exact budget/完整覆盖门不能删 |
| supplier / metric polynomial / volume moment | 通过 `ExactHermite` 取得几何 | 接入新显式 reader 后完整重算本次图；自身 target NPZ 仍是另一种数据，不由此 codec 接管 |
| `db6f-audit-closed-budget-transfer-v3.py` | 312–313 行安装 common-cut 并构造 `ExactHermite` | 保留全部转包/whole 参数门，显式加载新 common/reader 来源 |
| `db6f-export-closed-mesh.py::prepare` | 仅接受冻结 common/v2 两个名字，再构造 `ExactHermite` | 独立新版本明确登记新 common 实现；不是任意放宽源码白名单；全闭图/帽/mesh 门照旧 |
| `db6f-root-whole-metric-reach-v2.py` | 读本次 prefix 报告与 tail packet/rows，未直接解码 prefix NPZ | 下游本次报告的来源和存储闭包仍需贯通；不得把自己的 tail `data_file` 错换成 prefix codec |

一个最小的外层新存储身份可保留 `data_sha256` 表示原逻辑容器，并新增显式
`data_storage`，包含新 schema、descriptor 路径/哈希、storage implementation 哈希。
不保留一个虚假的物理 `data_file` 指向 JSON descriptor。旧消费者应自然拒绝该新入口，
而不是通过全局替换 `Path.read_bytes`、`np.load` 或偷偷创建一个超大还原文件来兼容。
本文**未**创建这种新 geometry metadata，也未宣称旧 verifier 能直接接受它。

实现真正 producer 时，宜另存最小代码副本，把旧 base 的保存阶段分离成内存 payload
返回，并在新 mirror 中执行原有 parity 操作后再写小片。不能先调用旧 `build` 写出超限
文件再事后补救。这里提议的重排只涉及 I/O；必须在那一新版本上逐式/逐行核实原数学
和源身份，本文的存储测试不预付这项审核。

新 metadata 的字节/哈希必会不同，即使原逻辑数组字节全同。随后所有证书应诚实绑定
真实 metadata、producer、reader 和 storage helper；不能伪报冻结旧文件的 SHA。
本题未来 M14 本来就是新图，仍须重新计算 metric、曲率、位置、moment、closed budget
和网格。当前旧 M12 存储往返没有转移任何旧数值证书给未来 M14。

## 5. 实际纯验证与复跑

`scripts/db6f-prefix-check-shared-jet-byte-shards.py` 只接受上述固定旧 M12 的
metadata/data SHA。它在内存中以 1,000,000 字节切片强制产生四片，实际工具回执
**6842a7 / exit0**。结果：原逻辑字节 3,112,330；四个 gzip 片合计 3,112,978；
最大片 1,000,323。原容器、三数组 C-order 字节严格相同，37 个针对结构、类型、损坏、
JSON 与 shape 的负例均拒绝。编码额外 648 字节说明分片并不节省总存储；目的是满足单件门。

未写出四片或还原容器，未执行任何正式几何 reader、源求解、Newton、RK、interval
证书、future candidate 或 solver。只写了小型检查报告。

在本题目录可独立复跑（`--out` 必须未存在）：

```bash
python scripts/db6f-prefix-check-shared-jet-byte-shards.py \
  --out notes/independent-old-m12-byte-storage-check.json
```

测试是旧真实数据的存储层正例，不是未来 M14 的假 positive packet。源码中的可选磁盘
reader 仍需在真正启用时审查/绑定；目前所有旧数学后台、原包和活动/失败运行源均未修改。

## 6. 结论的限度

原单件大小门确有具体触发风险，已有一个不损失任何表示精度的储存编码方案，并已用
旧真实包作逐字往返核对。尚未知道未来真 M14 保存图的压缩大小，也尚未交付新 producer
及整条 verifier 的储存适配。因此本批不能被标为“未来导出接口已经全通”。
保留原表示设置，待实际需要时启用经过完整审查的新存储链；不能用降阶、旧证书或放松
单件门来代替。G5 与真实闭图独立复跑仍开。
