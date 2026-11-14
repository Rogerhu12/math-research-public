# 独审：共享 Hermite 容器的无损字节分片

审查人：`/root/tail_review_continued_2`，2026-11-09。

结论：**PASS，范围为存储 codec、旧真实包的字节恒等性、拒绝协议与
当前消费者清单。** 这是可供另行适配的存储接口；正式新 producer、
geometry metadata、reader/consumer/source gate 整链尚未实现。本审
没有写分片或新几何，没有运行 source、solver、flow、RK、Hermite
求值或任何连续后端。G5 与 README 完成状态仍为 false。

## 1. 封存对象和完整阅读

全文阅读作者说明、完整 codec 和测试脚本；逐件重核作者 6 件封存、
21 个源码/旧数据来源及 6 个列出的 runtime reader 源码文件。
进一步核读了原 producer/mirror 的写盘位置、两个 Hermite reader、
common-cut 两处直接读取、angular/terminal 的直接数据门，以及
supplier/polynomial/moment/closed-budget/mesh 的调用关系。

| 作者对象 | SHA-256 |
|---|---|
| `db6f-prefix-shared-jet-byte-shards.py` | `a9414f8080cd417cbaccd81393f9e4b2bd000721ff624af59fa39fc8d07c9e41` |
| `db6f-prefix-check-shared-jet-byte-shards.py` | `b8613a6988e659be8d23bda1aa1e92abf0c9c98c9f67641030f9aa9763558c43` |
| `2026-11-09-db6f-prefix-shared-jet-byte-storage.md` | `94b744e5c9fc591d3f7ba6f0059f13bd305635ed486573a0ebf3222c253e7a43` |
| 作者旧包检查报告 | `342c315ecf640bd1ee68176bc00359bc5192441807e39473e74d2cb971061eec` |
| 作者来源清单 | `93d2fb1bb3753ab1ebf57d01535354d8a33f46ef06d8f104755f7b6002b65cee` |
| 作者 6 件 publication，共 49050 B | `4b7fbcbf61da527ee73f3aa2f85567242321058b9d51b9fec88dcc0fbec023f6` |

本审独立来源清单共 32 个唯一实际文件。它是此存储审查的来源
索引，没有把未来 M14 对象或尚未实现的 reader 当作已存在输入。

## 2. 原大小门与实际旧包

原 `950f-root-fullxyz-hermite.py::build` 在完成保存数组后用
`np.savez`、gzip 形成单个文件，先 `write_bytes`，再检查
`stat().st_size >= 5000000`。原 mirror 先调用 base build，再读取
同一 NPZ 做规定的入口 height 二 jet 置零，重新保存，并同样在
写后检查大小。独立 AST 检查确认两处顺序，因此原入口均不是
自动分片器，尺寸失败可能已经留下单个超限文件。

旧真实 metadata SHA 为
`da43f85ee6715254cca3daddd609c80e23bdf97916acb9ba2034282c3c237c7d`，
原 `.npz.gz` 为 **3112330 B**，SHA
`359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`。
source 模数 12、base 表示模数 24、节点 2570；三数组分别为：

| 数组 | 形状 | 原数据字节数 |
|---|---|---:|
| `mesh` | `(2570,)` | 20560 |
| `jets` | `(3,2570,74)` | 4564320 |
| `mean_increments` | `(2569,)` | 20552 |
| 合计 | little-endian binary64 | 4605432 |

总原始字节公式

\[
8\bigl(3n(3M+2)+2n-1\bigr)
\]

与这份实际数据一致，但不是 gzip 文件大小公式。只知未来 BVP
节点数不能推出压缩大小；内存失败数组形状推断的 mesh 数更不能
冒充已经保存的 finite-map 节点。作者对此的限制正确。

改变 modes、节点、mean 求积或 Fourier 提取会改变有限图。保持
数学数据字节、只改变容器切分，才是本批所证明的无损操作。

## 3. 字节恒等性的证明与实际 gate

令 (B) 为镜像等原数学操作结束后的整个原 gzip-NPZ 字节串。
`encode_bytes` 只按连续的 `[offset,offset+raw_bytes)` 切片，独立
gzip 各片；默认 raw 上限 4000000 B。它在返回任何待写数据之前
逐片要求实际 stored bytes 严格小于 5000000 B，模块本身不写文件。

`decode_bytes` 先校验 descriptor 的类型、字段、schema、base
维数、外层给定的逻辑 SHA、全部 index/offset/覆盖关系，后按
descriptor 指定的顺序解压并连接。每片解压结果就是该原字节切片，
且所有连续片完整覆盖 (B)，故连接结果严格等于 (B)。这不是
近似值比较；它保留 NPZ 条目、header、所有数组位模式、正负零和
原 gzip 元数据。哈希承担来源和损坏检测，数学恒等性来自切片/
解码/连接关系及实际 `restored == original`。

源码的几个容易漏掉的门已经保留：

- 所有整数使用 `type(value) is int`，排除 bool；数组 shape 也逐项
  检查严格整数和基于 base metadata 的尺寸。
- descriptor、每数组账本和每片记录都要求精确键集合，未知字段
  不被忽略。独立 JSON parser 拒绝重复键与 NaN/Infinity token。
- part 必须是简单 gzip basename，不能有目录分隔或父目录跳转；
  文件名唯一、index 严格顺序、offset 连续，raw 长度正且≤4000000，
  stored 长度正且<5000000。总和须恰好等于逻辑长度。
- 外部 mapping 必须恰好包含全部片名；其枚举次序不参与重组。
  stored/raw 的长度、SHA，以及最后整个逻辑字节串的长度、外层
  SHA 均重核。
- 原 NPZ 只允许 `mesh,jets,mean_increments` 三数组，
  `allow_pickle=False`，dtype `<f8`，形状严格匹配，值有限，mesh
  严格递增。重组后重新核数组 C-order 字节账本。

codec 使用标准库压缩/哈希和 NumPy 的保存数组读取，没有导入
任何本题几何、source、solver 或区间模块；没有 `np.savez` 或任何
文件写方法。NumPy 在这里不构造或求值多项式。

可选磁盘 `read_bytes` 接口另从**外层**接收 descriptor SHA 和
logical SHA，核 descriptor 后才按其受限文件名读各片，最后仍走
同一解码门。外层不能只信 descriptor 自己声称的逻辑 hash。
该路径已完整静态审查，**本次没有实际调用它**，没有写 descriptor
或片文件来假造一个新 geometry 入口。

## 4. mean 定义与 base/common-cut 的形状区别

原 mean 的定义是 `mean_increments` 的精确有理和，保存累计高度
只是显示值。整个容器按字节保存，连显示值也不重算，因此不会把
独立舍入的累计值反过来当作定义，亦不会在片边界引入重置。

独立读取旧 metadata 证实：critical-r01 common-cut 的 modes=64，
其 `base_geometry_sha256` 正是上述 M24 base，`data_sha256` 仍是
同一 3112330 B 容器。原 jets 末维 74，不是 194。未来读取存储层
必须使用 base 的 `(nodes,modes)=(2570,24)` 核形状；公共 cut 的
高模补零与完整两 jet 修正属于数学层，不能把其 M64 传给原容器
形状检查。作者 §3 指出的接口区别准确且必要。

## 5. 实际消费者清单与未支付的适配

作者清单与当前 M14 条件管线的实际源码相符，尤其没有漏掉只改
superclass 不能覆盖的额外读盘点：

| 入口 | 当前形式及未来必须保留的边界 |
|---|---|
| base build、mirror build | 两次原数学构造后各自保存单包；未来应在内存完成相同原操作，再写小片，不能先调用旧 build 产生超限文件。 |
| `SharedHermite`、`ExactHermite` | 直接读 `data_file`、核 SHA、gzip/NPZ；仅存储读取可替换，之后原 mean、Hermite/Fraction/interval 公式须保留。 |
| common-cut v2 | 类初始化及 `make` 都另读一次 base NPZ；两处都须适配，并使用 base 模数。 |
| angular metric | 直接核 base data 文件并读取 mesh，还核 baseline、target 和严格 source identity；target NPZ 是另一种数据，不可混用此 codec。 |
| terminal candidate | 直接要求 base `data_file` 和哈希，且 pin mirror/common/backend 来源；须显式验证新存储闭包与真实新来源，原 normal 终门/覆盖门仍保留。 |
| supplier、polynomial、moment | 通过 `ExactHermite` 获取几何；采用新的明确 reader 后仍须实际重新认证这张图。 |
| closed-budget、mesh | 安装并构造 common/ExactHermite，且具有明确来源选择；新版本应登记已审新实现，不能任意扩大白名单。 |
| whole | 不直接解码 prefix NPZ，只消费本次证书和独立尾 packet/rows；不能把 tail 的 `data_file` 误接 prefix codec。 |

旧 `data_file` 不可指向 JSON descriptor 后仍声称它是原 NPZ。
一种候选 outer schema 是保留 logical `data_sha256`，另明确登记
`data_storage` 的 schema、descriptor path/SHA、implementation
SHA；这只是说明中的设计，当前没有生成这种新 geometry metadata。
全局 monkeypatch `Path.read_bytes`/`np.load` 或落一个超大还原文件
都不是本审批准的方案。

即使原数组完全相同，metadata/source/storage identity 仍会改变，
所有后续报告必须诚实绑定新身份。尤其 normal terminal 当前严格
pin 原 reader/producer，它不会因为 codec 单独通过就自动接受
未来新图。实际 producer/reader/consumer 小差分、完整新来源和
真实新图后端必须在以后另付，本审没有预先支付这些工作。

## 6. 独立实际执行与可重核证据

在新输出名上实际复跑作者旧包检查：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/db6f-prefix-check-shared-jet-byte-shards.py \
  --out notes/2026-11-09-db6f-tail-review-shared-jet-byte-shards-replay.json
```

cwd 为本题目录。实际 receipt **`dd5b69 / exit0`**。8806 B 报告
与作者原报告逐字相同，SHA
`342c315ecf640bd1ee68176bc00359bc5192441807e39473e74d2cb971061eec`。
四个内存片合计 3112978 B、最大片 1000323 B，原容器逐字同；37
个不同负例全部拒绝。增加的 648 B 是存储开销，不是压缩收益。

另写了独立**纯标准库**检查器
`db6f-tail-review-shared-jet-byte-storage.py`，不导入 codec 或 NumPy。
它直接读取原 gzip/ZIP/NPY header 与 payload，核三项 C-order
binary64 的 shape、有限性、mesh 单调和实际字节哈希，得到上表
4605432 B。它还以原容器的精确 byte offsets 独立提取四片，重做
gzip 并核 stored/raw 的实际长度/SHA/解码恒等，核所有冻结来源、
实际 base/common 绑定、两处原写后大小门和 codec 无写入/无后端
导入。全部只在内存操作；没有保存数组或分片。

该独立检查实际 receipt **`6813e3 / exit0`**。检查报告 SHA 为
`c268ba9bd2f0837de8786dc12b205ba8a8eb8f8b06e30c7e581e8f7ed640462c`，
32 文件来源清单 SHA 为
`63064a66243ddff60d37d7c49b9a83598fd050544ba41b1c8e63e2a4d717754e`。
来源和原包均未被修改，只有小型审查报告落盘。

本批确认有一个保留全部原表示位模式的存储方案，且实际旧包正例
与拒绝协议通过。它不推测未来真 M14 的 gzip 大小，不宣称正式
导出链已适配，不向未来图转移旧 M12 的 metric/κ/预算。研究仍须
继续完成真实候选和整个已规定的闭图认证/独立复跑。
