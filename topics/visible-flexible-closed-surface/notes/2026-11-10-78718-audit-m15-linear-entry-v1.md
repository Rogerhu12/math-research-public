# M15/W15/N512 有界真实 DN 联解入口：完整独立审查

审者：`/root/independent_audit`，会话 `Astra-visible-flex-78718bd0`。审者未参与 M15、seed、warm、节点预算、延拓参数、数值候选选择或优化。审查对象是作者冻结后的固定程序和输入，本文没有启动新的 BVP、DN、Node 或候选计算，也没有修改冻结源。审者正在独占观察的 session 23125 是此前原公开 M14 种子的另一运行，其任何状态均不支付这个 M15 入口。

**结论：新入口的完整源码、来源、纯输入、运行时身份与最终关闭协议审查通过；未发现必须修改的入口阻断项。** 它可由指定执行者 root 按资源排程执行其唯一已绑定命令。这个结论不是 M15 数值成功、连续几何认证、独立全链完成或题目完成。将来只有本实例自己的实际输出、全部原有限门、完整控制历史重放和 root 的自然 exit 0 观察同时通过，才取得新的有限联解。

本审查真实完成了 12 个新源及其必要依赖的全文阅读、7 个派生源的全部 68 项字面变换重建、完整 unified diff 比同、递归 AST 核对和 188/187/190 项来源绑定重散列。独立实际小检查得到 30 个 live 控制函数身份及 30 个篡改拒绝通过；完整 final 负门准确拒绝缺未来 root 出口。首次错误地用 `python3` 别名启动小检查被原祖先命令门拒绝的事实也完整保留，见第 10 节。

## 1. 冻结材料及完整源码范围

作者设计为 [numerical-m15-linear-entry-v1](2026-11-10-78718-numerical-m15-linear-entry-v1.md)，13,252 B，SHA `60cd0210575c9496d351fd32164bac79ddf2cde16b793377d0cdc9f77fd18c76`。本次全文阅读回执 `364ad5`。

12 源清单为 `2026-11-10-78718-numerical-m15-linear-entry-v1-source-manifest.json`，6,237 B，SHA `77e402d9911b2cadf20e2b0004467f1ee8e2ad9ac113b3e13dd3eae66bb55cd8`。其中所有实际源如下，均在本题 `scripts/`。

| 源文件 | bytes | SHA-256 |
|---|---:|---|
| `78718-audit-m15-linear-control-v1.py` | 10,705 | `010acd43f77d1388e53b4ce7b6e8593d9110e07bbc7b38c77a0c26c36dee9d40` |
| `78718-build-m15-linear-entry-v1.py` | 13,490 | `96030b115331c53e352764401002f302214c6dacbcad08ae7abcc60d7e3dc7dc` |
| `78718-check-m15-linear-entry-gates-v1.py` | 2,579 | `ec64153fe3ee9ed89586974ed2ec39ae257cd85b8a6f3123c272fbb2c6641709` |
| `78718-check-m15-linear-protocol-v1.py` | 17,779 | `04679cee4f80d6a7576d9e84d935c6e8232ed474b4ae3cb303fa8153f9ce1400` |
| `78718-check-m15-linear-runtime-v1.py` | 4,957 | `d53cc1012d3a5217c236ca431d9f354101641017445c29661886d452fb77b063` |
| `78718-prefix-audit-m15-linear-v1.py` | 32,584 | `fd41b9ef4c2eea648cbb1ab1c3b638e61bc41d97d99d9213ad0370c042ff147e` |
| `78718-prefix-flat-linear-m15q512-v1.py` | 1,174 | `28391db54e8b40f9df3dbd00b9f23739b78c1c07c321ed64d932bcf2eac37a8f` |
| `78718-prefix-m15-linear-inputs-v1.py` | 22,133 | `28f6c54353d9aff0184115235f728cf07fb90fab46a8bb959da58fc4c7fb06b9` |
| `78718-prefix-prepare-m15-linear-v1.py` | 6,108 | `f76c3b8de7586e55123d79677309ec9d2426bc22ffb4a79934e35083cd71c369` |
| `78718-prefix-spectral-m15-linear-v1.py` | 19,193 | `33aaef9f6abb70c9e1eab6981d977dc16d5dfdb8740c969d773d6d2cbd9b6e81` |
| `78718-prefix-tail-linear-m15q512-v1.py` | 34,790 | `3ff7fe2810f15ee7f352d49739a38d5c42bbaf8980ec78c8c66a429faa35624e` |
| `78718-prepare-m15-linear-guard-v1.py` | 2,720 | `960217a1e55e08df64234bc27aed5243a8fc8fae61a816d5b16c13639aac7bb6` |

全文覆盖回执：builder 与全 diff 为 `4d3686/d386a8`；新输入门为 `4e7be1`；preparer 和新闭控制审计器为 `b98a72`；完整 control 为 `a48a82`；protocol 为 `9b6d02`，其中工具展示省略的中段另以 `e0f848` 完整补读；driver 为 `68a611`；final auditor 为 `de50f7`，其中省略的 runtime/restoration 中段另以 `f50ee1` 补读；四个其余小源为 `c27af5`。没有把被工具省略的源码假称已经读完。

原已审控制实现的完整独审 [tail-review-linear-dn-implementation](2026-11-09-db6f-tail-review-linear-dn-implementation.md) 本轮又以 `12096a` 全文读。它明确保存旧 v1 缺 trial 分组的失败，以及有效 v2 的 21 类纯协议与 352 个抽象破坏例结果。本次没有重新解释旧 N256 pilot 为完整 prefix 联解。原 trial-client 与 root tool recorder 在 `220652` 全文读；原 coupled 中的客户端选择、首请求、全部 outer 与最后 seam 调用路径另在 `5aa322` 对照。

## 2. 全部派生变换：没有暗换物理方程

生成账本为 `2026-11-10-78718-numerical-m15-linear-generated-sources-v1.json`，22,268 B，SHA `bc74421b42c62996d0dfbef51fa029a9e397304cb8e86083285abeff91e257d3`；完整 diff 为同 stem `.diff`，32,192 B，SHA `c7e6fe79bbbd6861a8751f2b611ba9635033e48b14bd81326ddbb4489a12ebf4`。

审者在实际 `2f70a8` 中从每个已散列的祖先源读取完整文字，按账本顺序检查每一个 before 的出现次数，逐项替换，再逐字比较当前派生源；七件全部相同。随后独立用递归 AST visitor 对照全部声明函数，并核账本所列 unchanged/changed/added/removed 项，再重建完整 unified diff，与冻结 diff 逐字相同。递归 visitor 也覆盖 try/if 内的局部定义，其结果保存在自己的报告中。这里没有运行会写原路径的 builder，也没有改写任何源来凑 hash。

七条派生路线的作用分别为：

1. 原有效 continuation v2 仅变新 schema/文件身份、运行 quadrature 为 512，以及旧 warm 的 config/ready parameters 比较只容许旧 256 到新 512 和原五项 I/O。Coordinator、完整失败分组、预算、缓存、last-good 和 journal 的函数体不因该数值变化而修改。
2. 新 flat selector 仍加载旧已绑定 `db6f-prefix-flat-coupled.py` 和其中的原 runner，只在原 `db6f_shared_client` 的准确路径被导入时选择另名新 control，并记住实际返回的模块。原 `main`、`solve_with_actual_tail`、BVP、BC、core 参数、profile/warp 与 seam 源不改。
3. 主 driver 将维数和谱权明确改为 M15/W15，输入/auditor 选择另名新版本；保留原 release-LU/direct-CSC 选择与检查，新增实际 control module 的 live typed 身份；首目标包从本实例 last-good 取出，避免延拓产生多个 bootstrap 包时错误写死 `_tail_0001`。
4. final auditor 按 M15 的准确维数扩展槽数、检查九源响应，新增完整闭控制历史重放；原物理 RMS/BC/outer/seam、完整有限性、源身份、恢复和 root 观察门保留。
5. guard 只变被调用 driver 与 schema，原资源 wrapper 不改。
6. 十函数 canonical runtime 小检查只变新 driver/auditor 及 schema。
7. 21 类抽象控制测试只改被测 control 文件路径；没有用抽象 stub 生成实际候选响应。

三件新手写 input/preparer/closed-control 和新小 entry checker 是单独全文审查的程序，并未声称其函数 AST 与旧版本不变。driver 顶部保留的旧历史 `SCOPE` 字符串在导入后立即被 `i.SCOPE` 覆盖，实际 reproduction 使用的是明确 M15/N512 的新范围；它没有造成运行身份回退。

## 3. 旧 seed 的准确身份及有限性

本轮明确选定的 prefix 初猜为 `2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz`，SHA `cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc`。新门要求其状态仍为 `UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS`、`solver_success=false`、2633 节点，配置为原 M15/N512、Z-only global quintic Hermite 初猜。其 preparation 的 SHA `31bc0734…` 只作构造来源；不会因为读到它就声称新解成功。

门逐项与原自验祖先比较 angular chart、完整 chart、warp reference、frozen profile、gauge amplitude、总长、物理 port SHA、tail parameters 与 cut。网格必须有限、严格递增、准确覆盖原物理区间；15 个参数和14个高阶尺度必须有限。两片 PP 的 gzip bytes/SHA、准确文件命名、float64 dtype、所有 `(6,2632,*)` 槽、有限性、连续 state 分片和完整46维都检查，不仅读第一个模态或最后节点。每片均小于5 MB。

旧局部 warm 是该旧 M15 run 的第一份真实 N256 DN，SHA `6f4de10c22fc05cedc87994c274c3643b5390add7bfe0ca71001e02a440a7a86`。其完整七键 response、Jacobian、jets、history、checkpoint、参数与 physical cut 标签按原规则核清。config 与祖先只容许 M15/N256 的声明数值差异，物理参数不改；当前同名 trial 的八源 SHA 逐项等于该旧真实包。

旧整次 matched run 的真实工具虽为 `ff466f` exit 0，但原程序捕获过后续 DN 失败。因此新输入门还硬钉其保存观察为 `mathematical_success=false`，并核它确实绑定第一份真实局部成功包。入口没有将旧进程 exit 0 解释成旧数学联解成功，也没有把 N256 局部成功复制成新的 N512 成功。

输入门在旧 PP 上求出末端物理 H，仅记录与 warm 请求的浮点最大差；当前实际为0.0，但不要求这个偶合成为普遍的 bitwise roundtrip 门。未来原 restart 路径所得首请求可以有自己的准确标签，交给新 control 的真正 bootstrap 处理。

## 4. 新 config、policy、launch 与代码身份闭包

新输入门首先调用已经独审且硬钉 SHA 的 independent-seed8000 祖先阅读器，使原97项、141项及152项来源闭包按原门自验。这不是把原 M14 的成功状态转移给 M15。另加入明确 M15 seed/warm、它们的实际分片、当前本地 trial import 依赖、新源码、canonical core、原 root recorder、原代码证据和完整派生账本。

`expected_config` 从真实旧 warm config 出发，只把 quadrature 设512及五个声明 I/O 改到新 stem；再要求去掉 I/O 后与原新运行祖先 config 只差 modes15。`expected_parameters` 同样以旧实际 resolved parameters 为基，明确 quadrature512 和五个 I/O。比较用禁止 NaN 的 canonical JSON，区分 bool/int/float/string 等实际 JSON 类型；不靠通常的宽松数值近似。

固定 policy 包含原初始/最大步 `1/8`、最小步 `1/1024`、32次物理请求、1024次逻辑推进、不随成功增长步长，以及新 journal、last-good 路径。实际源集合是原八个 trial 源加新 control 第九源；八个原源必须与旧真实包完全相同。新 policy 本身也进入 launch 的散列闭包。

preparer 只解析已存数据、检查有限 PP、生成 config/policy/launch/准备报告。它没有创建 BVP 候选、调用 restart、RHS、Node、Newton、CSC 数值矩阵或 DN。它要求一个完全未用的 M15 stem，在写前以 planned bytes/SHA 运行完整 `validate`，并独占新建元数据文件。program 与 final 仍会重新执行 `validate`，不能仅信任 preparer 自称通过。

实际冻结 launch 为 124,724 B，SHA `dbccb1b7892a0cfda626bf2769270b8bd1c9d3e3ef715c7583d8e731f88fee03`。它不需要全文进入对话；工具内部完整解析并核了所有字段。launch 188 项、policy 187 项、guard 190 项均在 `2f70a8` 重散列通过。guard 的真实 command 也逐值等于 launch 的 command。

## 5. 为什么旧 N256 warm 不支付新 N512 请求

新 `WeightedTailPort` 构造时先核 policy、绑定、准确数值设置、原 branch floor 与 initial-boundary policy，再核旧成功响应及其标签。其 config 比较只容许 `quadrature:256→512` 和五项 I/O；实际 worker ready 后，再对其 resolved parameters 做同一个限定比较。其它物理或数值参数变化都拒绝。

旧 response 仅作为底层初始化文件。新 base client 的 `.calls=0`、`cache_key=None`、`cache_value=None`，新 Coordinator 的 `good=None`。旧705槽 Jacobian、旧 residual 或旧 checkpoint 不会预填成当前成功缓存。若第一次实际目标恰等 seed H，就按调用者真实 flags 做一次新 BOOTSTRAP；若不同，就先在旧 H 做新 N512 的 false/false BOOTSTRAP，再沿固定控制路径向新目标推进。bootstrap 失败直接终止，不伪造 good。

原 worker 的 states 缩放、ratio 门、moment root、RK、Newton、线搜、36轮与 cut postprocessing 仍是原源码。TRACK 的两个 false 只省去调用者未请求的最终返回项，不代表不执行真正原 DN，也不把中间路径割线当作目标的 Jacobian。

## 6. Coordinator 全部状态、失败分类和预算

对每个外部物理目标，origin 固定为该请求开始时最近的真实 good。内部路径为

\[
H(\tau)=H_{\rm origin}+\operatorname{float}(\tau)(H_{\rm goal}-H_{\rm origin}).
\]

控制参数 \(\tau\) 用 Fraction 保存；到1时直接 `goal.copy()`。中间浮点向量若已经等于目标也转为准确目标；若只等于当前 good，则仅记有限的逻辑移动，不增加物理成功或改变实际 call 号。每个外部请求物理预算包含 bootstrap、失败与最后验证；TRACK 预留最后一个验证槽。成功后不增加步长。

每次真正 wire 请求都先由原 base 增加 `.calls`，完整包成功落盘后才更新其成功缓存。Coordinator 验证返回的 response 与已保存包规范化相同，packet 来源/config/目标/flags 完整，good 必须指向当前最新 call。已闭数值失败后核旧成功 cache 未被改写；缓存不能在失败 call 之后拿旧包假装最新结果。

只有 TRACK 阶段、flags 都为 false、并且原失败完整分类成功时才允许折半。原有效 v2 的所有保守分组门保持：

- 首次 progress 前的白名单 momentum 异常必须准确三键失败包、`lastIteration=null`、`checkpoint=null`、当前 call 没有 trial 行。
- aggregate 线搜失败需要从 iteration0 到失败组完整有序记录，trial 从0连续、原 `2^-k` 步、有限 norm、已知错误；此前每组只在末行 accepted，最后组恰十次拒绝，并与末 norm 对应。
- 正常 `converged=false` 必须完整36轮及每轮完整接受组，history/baseNorm/step 对应。最终 residual 与最后 base norm、state-only trialNorm 与下一 full-Jacobian norm 不被错误要求逐位相等。
- 未知错误、缺整组/单行、重复/乱序、部分 gzip、I/O、来源不符、bootstrap 或最后 VALIDATE 失败均终止实例，不能再返回旧 cache。

完成目标后仍执行调用者原 `jacobian/audit` flags；audit=true 强制真实调用，目标 Jacobian 来自目标上的原真 tangent。原 journal flush/fsync、原子 last-good 引用及失败后锁定语义全部保留。该控制程序是有界搜索协议，不证明路径存在或必然收敛。

## 7. 原 main 与每次实际 inner 的接线

原 coupled 在 `db6f_shared_client` 名下导入旧 shared-client 路径，新 selector 仅重定向这一准确分支；其他模块仍走原 loader。新 driver 验证原 `main`、outer solver 和每个物理 callback 的来源。实际 inner 的 owner 必须是 fixed M15、N512；fun、BC、Jacobian 都属于同一对象。

谱权由原 `power2_weights(15)` 算法得到，46项，最大2048；与独立纯输入公式逐项相等。原 release-LU、direct-CSC 的 provenance、默认参数、闭包、源字节、SciPy布局及原十函数 typed identity 保留。每次 inner 前后核 selected Newton 与 CSC，结束恢复原 prepare 引用；失败恢复仍使程序失败。

新增的30项 control 函数 live 记录来自 selector 真正返回、模块名为 `db6f_shared_client` 的运行对象。每项保存 raw 运行记录与递归 canonical code，并与 launch 中的 source/qualname/first line 和从冻结文本编译出的定义比同；完整 final 再核这些保存记录。这里“30项”指明确列出的控制闭包，其他保持原样的 property/类定义仍由整源散列及本次全文审查覆盖，不声称检查了 Python 进程的一切可能对象。

首个 inner 之前，原 outer 已实际请求所需真实 DN。新 driver 读取本实例 policy 绑定的 last-good，重散列其准确 packet，在该首 inner 的实际 `sigma*q*y[iz:,-1]` 上要求 Jac=true、audit=false，全部新九源和N512字段通过，才写 first-request binding。它不再预设第一目标一定是物理 call1；这是 bootstrap/延拓可能先产生多个包时必要的正确接线。

原 outer 仍最多8轮：inner 仅临时用 affine slope DN；每个 inner 成功后在其真实物理末高重新调用原非线性尾，再用原完整 BC 判 `<=1e-8`。最后保存 PP 后，用它自己的端点重新请求 Jac=true/audit=true，完整原 mean/nonmean seam 保留；首包或中间 TRACK 成功都不能跳过这些门。

## 8. 新闭控制审计器如何重放实际历史

这件新手写审计器没有构造真正 `WeightedTailPort`。它先核 policy 的实际散列与 launch 内容，读取已闭 journal 和 last-good；journal 每行必须有正确 policy SHA 和 UTC 字符串。仅时间字符串不参与行为重放，其余事件全部保留。任何 terminal-failure、未闭外请求、外请求重叠或编号错误都拒绝。

它枚举本实例从 `_tail_0001` 到 CP 所报 `tail_calls` 的全部真实包，要求实际四位序号集合与期望序列完全相同，不能缺口或多出未报告调用。每包完整 envelope、config、九源、请求 flags/有限目标、原成功或失败 schema 均核；正常包按原完整 response validator 检查，失败 CP 若存在仍核完整参数/有限 states 与标签。每包散列保存为不可替换的闭输入。

原 trial log 若存在就整件绑定，并要求每行 call 号属于真实包集合；需要折半时仍由原冻结 classifier 和完整 trial 分组决定。不是只检查 journal 说了“允许折半”便相信它。

`RecordedPort` 只顺序消费这些已闭实际 response，精确模拟原缓存条件和实际 call 增长。请求高度与 flags 必须规范化等于对应原包。对一个外请求，它从**实际 terminal return 引用的唯一包**取目标，再同时核 begin/end 的目标 digest 和 flags；调用原冻结 Coordinator，以相同 seed H、相同 policy 和相同包序列重新运行纯控制协议。没有捏造 H 或从未来猜一个成功响应。

通过条件包括：返回响应与实际目标包逐字段相同；物理 call 总数恰等CP所报；最后 good 的 call 是最新 call；重现的全部非时间 journal 事件逐字段相同；最后实际 last-good 文件恰等于重放所得最后一次真正持久化引用。全部 packet、journal、trial、policy、last-good 文件再次核 hash，列入 final 必需闭文件。

这证明的是保存历史确实遵循声明控制协议，并与实际包身份闭合。它不把 protocol replay 叫作新 DN，也不把数值 packet 升级为精确连续解。新 M15 未运行，故本次没有也不能给这段未来成功 history 一份伪造的正向运行例。

## 9. 原有限出口、root 自然观察与资源门

原完整 finite 门仍要求：最终 CP/summary一致且solver_success；同一个 frozen g/warp/port/cut；物理 RMS `<=2e-9`、原 BC 与 true outer；所有46维、15参数、完整quintic槽有限；本实例最后真实tail响应；705项Jacobian；完整17项cutJets、8项audit；865×30 states、13个rawNode及13×30准确mirror；1024 prefix audit与原 `64M=960` seam采样；全部谱坐标返回、物理残差门、runtime前后和恢复记录。

程序内部通过 `check_outputs` 后才自报成功和请求 exit0。CLI `final` 另要求 observer恰为root、真实工具自然exit0、有效session/receipt、同stem，再完整重放上述 finite/控制门，逐字段比同内部保存的闭输出报告。它把 reproduction、launch及所有控制/数值必需闭文件逐件与root观察的实际文件身份比较。原 recorder 已全文核：complete 分支只接受无仍运行session的整数exit及receipt，并散列本stem全部文件，所以 journal、last-good、policy与所有tail包均可进入实际观察，不因扩展名被遗漏。

真实事件来自root亲手取得的工具返回。代码字段和hash不能密码学证明调用者身份；本审查不以guard中的child exit、reproduction自报success、mtime或文件存在填造自然退出。Unknown handle只能按实际情况记unavailable。

guard继续硬钉原6GiB资源wrapper与原disk guard：RLIMIT_DATA每进程6GiB、Node heap1536MiB、磁盘512/768MiB阈值。guard仅生成元数据，其传给wrapper的command与launch逐值相同。它不是总RSS上界、收敛保证或数学验收；何时启动由root决定。本审者没有选择资源预算或并开第二套重BVP。

## 10. 本审者真实执行、首次拒绝与范围

真实记录保存在 [audit-m15-linear-observed-checks-01](2026-11-10-78718-audit-m15-linear-observed-checks-01.json)，1,932 B，SHA `22ffc27ba41131b518f444f5ac07f9821a79d7dca68d786cd01e8730a6119c10`。

| 实际工具返回 | exit | 范围与结果 |
|---|---:|---|
| `2f70a8` | 0 | 12冻结源、10作者纯证据、7派生/68变换、完整diff/递归AST、188/187/190绑定逐字/逐hash通过；0 solver |
| `47cef4` | 1 | 首次小入口命令用了环境变量，其实际解释器为 `…/bin/python3`，原祖先要求 `…/bin/python`，准确拒绝 `Actual selector command identity differs`；没有生成报告 |
| `96fa4d` | 0 | 只读确认上述两个实际 `sys.executable` 字面路径不等及输出不存在；没有改门或源 |
| `115355` / session56381 → `39330d` | 0 | 改用设计提供的完整冻结 `…/bin/python` 命令；188输入、30 live函数、30逐个篡改拒绝通过，0 port/solver |
| `971b01` / session29360 → `b02fd4` | 2 | 完整final负门准确拒缺未来root真实自然出口；0新候选成功 |

首个失败是本审者调用的解释器字面身份不符，不是数学求解失败，也没有被删去或重写成成功。按冻结命令重跑是执行同一已声明入口，不是放宽原门。

独立实际正检查报告 [audit-m15-linear-entry-check-01](2026-11-10-78718-audit-m15-linear-entry-check-01.json)，51,807 B，SHA `b83056e9f8e940bdd314a2db905c3a8f6d0507a0646a6fb46881ebf3e68c2692`，与作者的同类报告逐字相同。它确实加载了新控制源的30个函数并从live code捕获typed记录，但未构造port、RHS、矩阵或候选。

独立负final报告 [audit-m15-linear-negative-final-01](2026-11-10-78718-audit-m15-linear-negative-final-01.json)，535 B，SHA `d5c4f36f7f8518b6bec297ce99f5e59b84fd28b24dcd3aa2309ab2219b7261c5`，明确 `ready=false` 和 missing root actual tool-exit observation。它不是成功证书。

自己的完整变换/身份记录 [audit-m15-linear-source-check-01](2026-11-10-78718-audit-m15-linear-source-check-01.json)，5,731 B，SHA `40a910b2757a2be0e9a91a132102121270afd9a1d81fdcec861f2955ea03f165`。原21类protocol与十函数CSC实际小检查的作者自然回执、报告身份也全部在本次冻结manifest中核过；其相关函数的源码保持关系已经完整证明，因此未无必要地重跑旧充分测试，且没有把作者执行冒称本审者执行。

本审者实际通过的两个命令，cwd为本题目录：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-check-m15-linear-entry-gates-v1.py \
  --launch notes/2026-11-10-78718-numerical-m15-linear-01-launch.json \
  --out notes/2026-11-10-78718-audit-m15-linear-entry-check-01.json

/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-prefix-audit-m15-linear-v1.py \
  --launch notes/2026-11-10-78718-numerical-m15-linear-01-launch.json \
  --mode final \
  --out notes/2026-11-10-78718-audit-m15-linear-negative-final-01.json
```

## 11. 准许采纳的准确结论

该M15入口明确变更有限表示维数、相应谱权、warm到新N512的求积身份以及有界真实DN调用路径；它保持原固定物理问题、目标请求、完整原finite门与真实出口要求。源码和纯输入协议可据此正式采纳为可执行的新入口。

入口通过不预言有限计算成功。若未来成功，必须以它自己的CP、末tail、exact bridge/common定义和实际存储身份重新完成连续metric/reach、全时、网格及其他原门；原整图 `2e-9` 不变。M14的root-only后链不能直接冒充M15后链，另名M15计划器应另外审查。旧独立M14会话也不能替它提供M15自然出口或全链证据。

本文件没有支付这些未来门，没有增加README之外的新总体门，也没有作阶段性课题收尾。主研究和审者原公开种子的真实独立观察继续。
