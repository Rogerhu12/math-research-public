# 新 prefix 分片存储家族 v1：完整独立审查及未通过项

日期：2026-11-10。会话：Astra-visible-flex-78718bd0。审者：/root/independent_audit。
本稿冻结审查原 v1 家族及 builder-v2，不把后来的另名修正版混入这些 SHA 或实际执行结果。

**结论：字节编码、两个实际 reader、common-cut 的定义基底、完整主认证与 mesh 接线已核清；v1 全家族尚不采为生产准备通过。** 全文审查发现两个报告函数合计三个来源路径仍指旧文件。它们没有改变数值公式；其中一个位于声明的可选局部诊断，必须修正其来源记录；另一个位于本次生产路由排除的 tail CLI，不构成主认证门漏洞，另名派生时一并修正即可。完整缺口与最小传播范围见第 7 节。

没有运行候选优化、主 solver、实际 producer、完整 common-cut 构造或完整 terminal.candidate。审者保持最终原种子全链独跑资格。所有旧源与 v1 新源均未修改；没有编辑 HANDOFF/open/results 或执行 git。

## 1. 全文审查、冻结输入与完整重放

已全文阅读两个 core、14 个 adapter、builder-v2、core checker、reader checker、来源说明、设计、生产路由；完整读完 source ledger-02 的全部 134 处 old/new 片段，并核 builder-v1 与 v2 的全体差异。补读原 whole 的全文、原 exact-bridge 的完整入口与剩余数据入口检索；审查 mesh prepare/plan/build/review 与原拓扑、height sampler 的接口分类。

关键冻结文件：

| 对象 | 大小 | SHA256 |
|---|---:|---|
| byte codec v1 | 11138 B | e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39 |
| storage helper v1 | 5923 B | 83cf59cfe5ab373421e53d0c0d8d2274edfc6a6b266fc2ab6161274b474a4329 |
| builder-v1 | 21154 B | 4c574c493f53f0e90ba3d6db98b64a61a930d9d34a6c9faa7a7df092425f52e8 |
| builder-v2 | 21548 B | 17c63f1c0c2066b42c1f5e9e113e679247b30b317ac103d63176a50bc3233500 |
| source-ledger-02 | 60660 B | 375e716789ef206deecbb62207d8e1c70d9995bfb303f27f0b1c250c174e8634 |
| root reader-check-01 | 12678 B | 480b4761ccfbc5fcf0955fc87793955346b7de9f662fbfffce31836b4cf041c2 |
| numerical chain-source-pins | 10407 B | 0ea6f4eea5442df8d2c4b75e94d95f80db79ce7e3e4f48e2e4a8ba7c26b29d1a |

简称对应本题 scripts 的 78718-prefix-*.py 或 notes 的 2026-11-10-78718-*.json。全部 14 个旧源/新源的大小、完整 SHA 及实际 terminal 34 项来源，逐件列在本人 [source-replay-01](2026-11-10-78718-audit-storage-source-replay-01.json)。

本人实际工具 e5d274，自然 exit 0：不调用 builder 来替自己推断结果，直接对 ledger 的每个冻结旧文件逐字读取；每一步要求 old 片段在当前中间文本唯一出现，再只替换一次；最终全字节必须等于当前新文件，大小/SHA 同时匹配。全部 134 步、14 个完整 adapter 通过。另用独立 AST walker 核函数集合，188 个函数实例 AST 完全相同，其余变更函数集合与 ledger 精确一致；全部变更函数也已全文作语义审查，未以 AST 数量代替此项。

本人核完 terminal 的 13 项新 prefix hard pins 和 21 项原 SOURCES，后者字典与旧 C terminal 完全相同；34 个来源全部实字节匹配。angular 的 11 项来源和 review 对新 exporter 的固定 SHA 也全部匹配。此项验证的是当前文本和声明一致，不能自动发现“报告列出了不实际使用的旧后端”；第 7 节正是全文语义审查补出的缺口。

该 source 重放报告为 21653 B，SHA256 74a693ba4b78ff3b12a3254e063097c75a607fa7f1bef48104b90e1676d928a0。

## 2. builder-v1 的真实失败及 v2 的范围

root 的 47de38 自然 exit 1 记录为 Missing unique HERE assignment，adapters_written=0，ledger_written=false。代码支持这个准确范围：build_all 先在内存构造全部输出；只有完成后 main 才写任何 adapter/ledger。原 continuous 源没有 HERE 和 importlib.util，v1 的统一注入假设不成立。

完整 v1/v2 diff 只有 storage_import 的一段特殊处理：对这份冻结 continuous 源，先唯一替换原 import numpy/down 函数之间的片段，加入 importlib.util 和 HERE，然后继续原统一 helper 注入。没有更改 interval、三角、有理数、Hermite 或 certificate 数学语句。v1 失败历史和其 SHA 保留。不能把 v2 的成功回执写给 v1。

## 3. 字节存储命题及其源码实现

### 3.1 逻辑对象

P 是原 producer 完全不变的 np.savez 调用之后、原 gzip.compress(..., mtime=0) 得到的完整 bytes。新 data_sha256 始终表示 P，不表示 descriptor，也不表示其中一片。

codec 从头至尾不解码数组。每片是 P 连续的一段，descriptor 记录严格连续 offset、从零递增的 index、正 raw_bytes、raw/stored 长度与 SHA、唯一 basename；所有分片长度相加必须恰为逻辑总长度。解码按该顺序连接。因此，只要每片解压恢复原片，就逐字恢复 P；这一等式来自无损压缩和区间分割，SHA 用于检测文件身份，不替代无损性证明。

P 相同意味着原 gzip/NPZ 头和数组数据全部相同。相同 np.load 接收相同输入后，dtype、shape、Fortran 标志及数组位模式都不变；这个论证包含负零、NaN payload、非本机字节序和空维，不依赖逐项浮点相等。它也不声称后续数学 reader 可以接受任意非有限几何。

### 3.2 长度、路径、读取和写出

codec 的 descriptor 和各 part 行都是闭合字段集合；整数要求 type is int，因此 bool 不冒充数值。SHA 要求小写 64 位十六进制。basename 仅准以字母或数字开头的简单文件名，不接受斜线、上级路径或任意绝对路径。重复文件名、part index 重排、offset 空隙/重叠/越界、总覆盖不足全部拒绝。JSON 拒绝重复字段和 NaN/Infinity。

每片 raw 至多 4600000 B；压缩完成后先检查实际 stored bytes 严格小于 5000000 B。descriptor 的实际 JSON 严格小于 1000000 B。write_bytes 在写第一件之前核完全部冲突；同名现存文件必须全字节相同，不能覆盖不同内容。descriptor 最后写。完整 P 不会先写成超限单件再拆分。

read_bytes 从外部绑定的 descriptor 长度/SHA 开始，读取前核物理文件大小，再核 stored SHA。GzipFile 只请求 raw_bytes+1 字节；超长解压不能被截断后冒充指定长度。截短/损坏 gzip、错误 raw 长度/SHA 以及错误全局长度/SHA 都拒绝。最终全局 payload 重新核验。写入过程中若发生 I/O 失败，代码没有承诺事务性清理；只有完整读取并验证后的闭包可供后续使用。

### 3.3 prefix helper

helper 本身是新显式格式，要求 data_storage 且排除 data_file。其 envelope 闭合，schema、format、codec 固定 SHA、helper 自身 SHA、逻辑总长/摘要和定义基底的 nodes/modes 全部对应。read_payload 返回原 metadata、精确 P 及实际文件闭包：base metadata、descriptor、全部 parts、helper、codec；路径不得重复。

verify_arrays=True 时另核原三数组名和数量，little-endian binary64 的原布局 mesh=(n,)、jets=(3,n,3M+2)、mean_increments=(n−1,)。读取层不转换或重存数组。verify_arrays=False 仍核完整字节身份和基底/存储维数关系；该分支只用标准库，不导入 NumPy/SciPy。数学 reader 继续自己的有限性、递增网格与几何检查。

## 4. 全部 14 份适配的语义审查

| adapter | 替换数 | 完整核清的实质改动 |
|---|---:|---|
| fullxyz | 6 | 原 np.savez/gzip 之后转交 storage；原 nodal jets、积分、Hermite 与 Fourier 语句保留；reader 的获取 P 一段替换 |
| mirror | 6 | 经 helper 取 P；原 inlet parity 原语句各执行一次；原 np.savez 再生成 P′，转交新存储；补真实 wrapper/logical 身份 |
| continuous | 5 | 补 stdlib loader；原 ExactHermite 获取 P；certificate 追加实际 storage_bindings |
| metric-polynomial | 4 | 指向新 continuous，补正确 backend SHA 和实际 storage_bindings；所有残差、卷积、区间/算子界保持 |
| metric-supplier | 4 | 指向新 polynomial；报告 geometry_storage_bindings；解析目标的数学定义和其自己的存储格式保持 |
| volume-moment | 4 | 指向新 continuous；报告同一个 storage 闭包；原严格角度数与积分语句保持 |
| common-cut | 8 | 新 reader/poly/moment 路径；两处直接载入均先取 defining base，原修正公式不变 |
| angular-arithmetic | 3 | 独立 prefix 副本改导入新 polynomial；原 tail 源文件不动；存在第 7 节未用 CLI 的来源字段遗漏 |
| metric-budget | 5 | 改新 arithmetic/common 导入；原局部计算不变；存在第 7 节实际局部诊断来源遗漏 |
| closed-budget | 4 | 唯一选择新 common，装新 continuous，补 prefix_storage_bindings；原 transfer-v3/全部标量不等式保持 |
| angular-metric | 25 | 新 prefix 文件名和 SHA；同一 base payload、完整覆盖/叶片重读与实际 storage 闭包保持 |
| mesh exporter | 9 | 新 prefix/source 字典；原 tail streaming 与采样公式保持；plan/build 都记录实际 prefix_storage_bindings |
| mesh reviewer | 5 | 新 supplier、明确新 exporter 路径/SHA；实现标签如实改写；原实际 replay/小构件门保留 |
| terminal | 46 | 13 项 prefix 来源迁移及调用名称/SHA；原 SOURCES/标量门、storage 子程序与所有完整候选核验保持 |

“保持”同时由全文 old/new 唯一变换重放与上述函数的完整阅读支付，不是只凭若干 fixture 相等。

mirror 的初始 P 与修改后 P′ 的文件名各含自身 logical SHA。不同内容即使有文件名冲突也会因逐字比较失败，不会覆盖未知片件；同一内容可以安全复用。最终 metadata 仅指最终 payload 的闭包。旧未镜射片件的存在不会加入最终定义，也不能被当成额外几何证书。

## 5. defining base、完整认证与后续消费者

### 5.1 common-cut 的 M24/M64 分离

CommonCutPrefix 先验证 common metadata 的实现和 base/tail/bridge SHA，随后 super().__init__(oldpath) 读取定义基底。此时 self.M、self.meta、storage_bindings 都属于真实 base（生产计划为 M24）。第二次读取也使用 oldpath，并要求返回 metadata 与 bindings 精确相等。直到原 nodal jets/mean increments 取出后，才依据 tail 模数向新 M 补零并构造原 quintic correction；最后才把 self.meta/self.M 改为 common 的扩充版本（计划为至少 M64）。

make 同样先从 args.geometry 的定义基底取 P，再计算扩大模式和 common metadata。它保留 data_storage 中 base 的 M24，不能用 common 的 M64 重解释原 NPZ。修正的 signed planar/height modes、精确 radial anchors、桥根与 mean gauge、宽度和 C² 端点公式全部是原文本。

因此扩充 metadata 与 base storage 的模式数不应相等。新 helper 明确拒绝把扩充 metadata 当定义基底；实际 M24→64 的负测试通过。这不是缺失某个“转换”，而是保护正确定义。

### 5.2 storage 闭包与终门

common 对象的 storage_bindings 仍是 base 的真实闭包；common metadata 自身、tail manifest 和 bridge 由另有字段/hash 绑定。continuous、metric、moment、target、angular、closed-budget 的报告都传递这份 base 闭包。

terminal.prefix_storage 先核新 helper/codec hard pins，要求 base/common 都是显式分片格式且 data_storage 精确相同，再使用 base_path 的 verify_arrays=False 实际重组 P。它核 loaded base 未变、P 的 SHA 同时等于 base/common logical SHA，并逐件绑定实际闭包。

prefix_storage_ledger 要求 reported/actual 长度相同，每行字段恰为 file/bytes/sha256，正大小且小于 5 MB；按 basename、bytes、SHA 排序后全体及重数一致，实际期望键不得重复，再读取实际已解析路径。旧绝对路径失联不会自动放行；迁移仅允许同名、同大小、同内容身份的对应。

完整 candidate 确实调用这两函数，并检查 budget、geometry、moment、target、metric/角界及角界 baseline 的各自 closure。它同时核 common/base 图、bridge、tail、新旧 profile/target 等原身份条件。因此“同一 storage 闭包”没有取代“同一完整曲面定义”。

terminal 的 BOUND=1/500000000、FACTOR=195883/20000、M12 严格下界、height/positive-alpha SHA、21 项原 SOURCES、全部 background transfer、tail/collar 完整覆盖、原 exact max/reach/非全等标量与 root-independent proof dependencies 保持。新 prefix 来源另列 13 项；原 tail/reference 家族没有改成新 arithmetic 副本。它仍不支付 G5、最终独跑或 README 完成。

### 5.3 whole、bridge、target 与 mesh

原 whole 只读取并重新 hash closed-budget 七项 JSON 输入、真实 tail 包/行和精确标量；没有 prefix NPZ 读取，也不把预算 wrapper 固定成旧来源。新预算保留同名七 inputs；额外 storage ledger 由 terminal 消费。原 whole 1e−6 门仍须后续固定 2e−9 终门，未把前者冒充后者。

原 exact-bridge 的入口只用 geometry/target/tail/metric JSON 和原精确根/转移计算，不读取 prefix NPZ；因此该接口无需存储派生。

所有剩余 np.load/data_file 逐类核清：target 的解析系数包、tail 背景包/行、固定 M12 点包、mesh fixed-vertex mask 都是不同对象，仍走原格式。此次存储改动只为 prefix nodal P；没有证明任意未来 target 包都不会触及文件大小限制。

新 mesh.prepare 由 common implementation SHA 选新 common，将新 ExactHermite 安装为 prefix，tail 继续原 StreamingExactIntegratedTail。source_sha256 包含新 prefix/poly/supplier/helper/codec 与原 tail 来源。plan/build 的 geometry/whole/tail 身份、材料角逆变换、完整反射、固定帽、相位网格、顶点和 PLY 限额门保持；新 reviewer 钉准确的新 exporter SHA，仍要求另一次真实 mesh manifest 与字节重放。原拓扑程序只读取 PLY；原 height sampler 的 radii schema 不变。

未运行这些实际生产命令；本节支付完整源码/接口对应，不支付未来新图的连续证书或网格结果。

## 6. 实际检查与独立执行范围

### 6.1 root 已完成的 core 检查

已全文读 core checker，并重核已有 root 报告绑定的三份实字节来源。该报告为 5204 B，SHA256 7c3743f0a0925add77daa8cae9e5ce5926d5110f98e68bb795c7d9ad7d6a5a50，状态 PASS_SYNTHETIC_EXACT_BYTE_STORAGE_ONLY，4 个正例、23 个拒绝。

正例涵盖任意形状/dtype/C-F 布局/NaN 位模式；真正跨两条 4600000 B 边界的高熵 NPZ 实际磁盘往返；prefix helper 布局；迁移后 fresh 标准库子进程。拒绝涵盖缺片/多片/重排、offset 缝隙/重叠、bool 整数、路径越界、重名、长度限额、local/global 摘要、损坏 gzip、重复 JSON/nonfinite、空串、内容冲突、混合 legacy/new 格式、扩充模数、bool nodes 和错 helper 身份。

本人没有重复这些已充分的 core 执行，也没有把它们说成本人新回执。

### 6.2 本人完整 reader/source/真实 terminal storage 重放

本人实际使用 primary Python，工具 **313f38，自然 exit 0**，命令为本题 scripts/78718-check-storage-readers-v1.py，source-ledger=ledger-02；独有 scratch-dir 位于仓库外的 audit-storage-reader-fixtures-01，报告写本人 notes。

报告：[audit-storage-readers-check-01.json](2026-11-10-78718-audit-storage-readers-check-01.json)，12732 B，SHA256 a1fc17051140e4f99c73ed887fffff04ba3ce2282822ecef63f493d3dea5e759。

实际完成：

1. 再纯执行 builder-v2 的 build_all，14 份完整 adapter/2 core 全字节及全部 transformations 与 ledger/current source 相同，导入全部 16 新源。
2. 核 21 项原 terminal 家族字典、阈值与新 prefix/角界来源。
3. 用 M2/5 节点及 M24/11 节点两套有限二进制有理 fixture，同一个 P 同时供原 single-file reader 和新分片 reader；257 B 小片强制实际多片读取。
4. 原/新 SharedHermite 的 mesh/jets/increments/h/c、0/1/2 阶实际点值、三个 Fourier basis 数值及零符号相同；binary64 还逐字相同。longdouble 未定义 padding 不作为数值差异。
5. 原/新 ExactHermite 的 inlet 精确有理数据、完整 h/power 上下端，以及全段/中半段的 0/1/2 阶 ranges binary64 全字节相同。
6. 两 reader 的实际 storage_bindings 与 helper 相同；把 M64 metadata 当 base 明确拒绝。
7. 每套 fixture 在 fresh primary 子进程真正调用新 terminal.prefix_storage 和 prefix_storage_ledger。迁移旧路径通过；省一项、common logical SHA 改变、common storage reference 改变均拒绝；子进程确实没有导入 NumPy/SciPy。

后续工具 d8bf33 逐字段比较本人和 root reader 报告：只差 seconds 与两处 fixture 目录；33 项 source/ledger 绑定全部再次匹配。

这些小例支持实际接线和读取等价；一般等价由第 3—5 节的字节/源码论证给出。报告准确标记 full_producer_executed=false、full_common_cut_or_candidate_gate_executed=false、new_candidate_or_geometric_certificate=false、production_ready=false，BVP/Newton/DN 为零。本次成功没有覆盖两个尚未调用的错误来源报告表达式。

## 7. 两个报告函数、三个旧路径：完整缺口清单

### F1：声明路由中的局部诊断来源记录不完整

文件 78718-prefix-metric-budget-storage-v1.py，SHA256 656e11ca0226ca1647a968c76afb4566b076ba0e9b4c0836bf263cf097ced091。

真实导入链是：

metric-budget-v1 → angular-arithmetic-v1 → metric-polynomial-v1 → continuous-hermite-v1。

但 main 的 result.backend_sha256 字典仍计算以下旧文件的 hash：

- db6f-audit-metric-polynomial.py；
- db6f-audit-continuous-hermite.py。

必须改为真实使用的两个新 prefix 文件名。否则报告不能忠实记录它所用的后端；不能以两份文件的数学函数相同掩盖整个源码 SHA 与存储入口的不同。该 main 只作局部诊断，未供正式终门当连续证书；正式 angular 的 11 项 hard pins 本身正确。因此未发现由此放宽数学终门，但完整家族的来源审查尚未通过。

这是源表达式的直接结论，未调用真实候选的 main 来制造报告。

### F2：声明生产路由之外的 arithmetic tail CLI 有同类遗漏

文件 78718-prefix-angular-arithmetic-storage-v1.py，SHA256 3ade215b643345920eafe9a1e3c7ce477ed6e46913e47bf712f309d800636ece。

run 的 interval_backend_sha256 仍计算 db6f-audit-continuous-hermite.py；实际 poly.base 来自新 continuous。应改为真实新后端。当前生产计划明确要求 tail 认证使用原 tail 程序，不运行这个新 prefix 副本的 tail CLI，所以 F2 不构成已声明主认证路径的漏洞，也不因此增加任何数学门。另名修正版可顺便修正它的公开报告准确性。

### 最小修正与传播

完整消除三处错误的另名派生只需要四个 adapter：

- arithmetic-v2：修 interval backend 报告的一个路径；
- metric-budget-v2：修两个 backend 报告路径，并指向 arithmetic-v2；
- angular-metric-v2：改实际 helper 路径，以及 budget/arithmetic 两项文件名和 hard pins；
- terminal-error-v2：改三个新 prefix 依赖名字/摘要，并改 angular 识别与调用名称。

其余 10 adapter 加 2 core 保持原字节，包括 fullxyz、mirror、continuous、polynomial、supplier、moment、common、closed-budget、mesh exporter/reviewer。不要把原 tail/reference SOURCES 改为新 prefix 家族。builder 须另 v3；reader checker 须另 v2 绑定新 builder/terminal，重新生成来源 ledger、完整差分和新 source-pins/路由记录。

若只考虑 F1 的声明路由，可只派生 budget/angular/terminal；同时修 F2 的上述四文件方案不会改变任何数学计算，且避免遗留已知误报。本审不代写或调参新源。所有 v1 文件与本次实际成功报告作为历史记录保留，不能把修正版回执覆盖给 v1。

## 8. 最终限定结论

对 v1 已完整核完字节层、原数学文本不变、定义基底、source/consumer/hash 连接与实际 reader/终门存储小执行。除第 7 节完整列出的来源记录遗漏，未发现其他实质存储接线缺口。当前不采“全家族 production ready”；修正版须以新名字和新 SHA 单独核完整传播后再定。

本审没有创建新曲面，没有支付主问题 G5、固定误差终门、网格交付或最终原种子全链独跑。存储层通过与未来候选是否成功是各自独立的判断。
