# R1035 — 原完整多项式行的原生表示及全 R975 返回

状态：表示与原算法的等价性手证完成，基础原生后端已通过真实公开编译验收。完整生产接线继续公开准备检查，原几何对象的实际运行另行验收。没有新增几何 PASS。

## 1. 处理的是已发生的整个分母像运算

唯一旧 v9 的完整终态已在 [原终点链](../notes/2026-11-27-artinian-v7-final-and-successor.md) 消费：原 A0 y0 的全分母算子像停在完整 306 列 Hermite 的第 4 列。其整行约化已经进行约百万次加行；这是实际耗时位置，不是一个抽出的次要矩阵。

R1033 的全剩余核和厚 projector 已接入唯一 v10。本节不改变该运行，也不修改几何输入、维数、原参数、两个特征零 PASS 或任何验收条件。它准备把 R975 已证明的同一个完整算法中的多项式行改为 FLINT 的完整系数表示，消除每次整行加法的数百个 Sage 对象构造。

官方接口只用于精确的多项式加、乘、常数缩放和次数读取：
[FLINT nmod_poly](https://flintlib.org/doc/nmod_poly.html)。
完整 Hermite、全列 gcd、移位 Popov、原生成元返回均仍由原 R975 算法定义。这里不调用一个不同定义的矩阵标准形接口。

## 2. 先核完整下降，再作忠实的系数编码

仍先执行 R956/R975 的原完整输入下降。左侧全部行、全部列以及有 attached 时的全部附列，都必须通过原检查。附列只允许原证明中的同一个常数因子，返回时仍恢复它及原系数域。

若整个输入没有降到素域，新适配器直接调用未经改变的原 R975 后端；不会挑选能下降的行、列、主块或系数。对成功下降的原输入，记
$$
R=\mathbf F_\ell[t].
$$
本实现只接受整个底域确为素域，且 $2\le\ell<2^{63}$。实际原生产参数保持原样，未借这个条件替换输入。

每个多项式逐系数转为 $0,\ldots,\ell-1$ 的唯一整数代表，并在输入时逐项检查返回原域后等于原系数。整个长度保留，零系数不是漏列。由于
$$
\mathbf F_\ell[t]\longrightarrow
\{(a_0,\ldots,a_d):0\le a_i<\ell\}
$$
给出唯一系数表示，解码回同一 $R$ 与编码互逆。FLINT 的全多项式运算在模 $\ell$ 下进行，故该表示忠实保存加法、乘法、零、次数及首系数。

每行拥有独立的全部多项式存储。析构对所有实际初始化的项逐项释放；两个 Bezout 组合先用两条未修改的输入行创建两个新行，再同时替换。没有因可变存储把第二个组合误算在第一个新行上。

## 3. 原全部行操作及 pivot 次序完全相同

设 $R_1,R_2$ 为两条原完整行。原算法仅用以下操作：

1. 交换两条完整行；
2. $R_1\leftarrow R_1+qR_2$，其中行号不同、$q\ne0$；
3. 用非零常数乘整行；
4. 已核完整列 gcd 后，作原 Bezout 二行变换。

前三项在新表示中对每一列执行同一操作。有 attached 时，附列也同时对每一列执行同一操作。没有仅更新 pivot 以后尾段的快捷路径。

第四项用原算法算得的 $u,v,s,t$，其中
$$
su+tv=1,
$$
执行
$$
(R_1,R_2)\longmapsto(sR_1+tR_2,\,-vR_1+uR_2).
$$
对应二乘二块的行列式为一。新实现只替换两次完整线性组合的存储操作；整个列的 gcd、整除、系数次数界、全尾 reset 和移位回退仍由原函数逐项检查。

原 shifted leading 取全部非零列中
$$
(\deg f_j+\sigma_j,\ j)
$$
的字典序最大者，零行返回 $(-1,-1)$；原算法先核 $\min\sigma_j=0$。新实现逐列扫描同一完整范围，用完全相同的顺序比较。

列约化的下一项也扫描全部 pivot 列，保留原排除自身的条件，取
$$
(\deg f_j+\sigma_j,\ j,\ \text{reducer row})
$$
的同一最大项。每列的 pivot 行唯一；因此用后两个量返回实际 reducer 与原字典序一致。原 quotient/remainder 仍在 Sage 的同一 $R$ 中计算。每步之后保留原 leading 严格下降、pivot 未变、整行次数帽和不可再约条件。

由行操作次数作归纳：编码的初始整个矩阵相同；若一步前所有行相同，两个实现选择同一 pivot、同一商、同一 Bezout 系数并得到相同的所有列。故整个操作序列、最终 Hermite 矩阵及全部 attached 结果相同。此结论不是只比较 determinant、秩或有限个样本。

## 4. 原次数帽、全部生成元及双向返回保持

适配器固定原 R975 文件的 SHA256，然后对原函数作 19 组计数严格核对的文本替换。任何原串计数变化立即停止。替换后的完整函数还须通过 Python AST/编译；不会按名字取一个未固定的新版本。

设原最大左次数为 $D$、完整 determinant 次数为 $\Delta$。原 R975 的全程左次数帽
$$
B=\max(D,3\Delta+1)
$$
原样保留。有附列、原附列最大次数为 $D_C$ 时，原
$$
B+(n-1)D-\Delta+D_C
$$
附列次数帽也原样保留。每次整行、Bezout 块及 reset 后的原检查未删除；最大次数元数据仍扫描整个实际行。

最终全部原生行逐项解码为原 $R$ 上的矩阵，随后执行原全部验收：

- 完整方阵确为 monic Hermite，全部剩余生成行确为零；
- 整个对角积次数为原 $\Delta$，全程左右次数帽都成立；
- 对每一条原始生成行作完整 Hermite 除法，余数矩阵确为零；
- 有完整素域下降时恢复原域及附列常数，并再次对每一条原始域生成行做同一除法；
- 全部附列数、行序、域及原变换过程保持。

前向包含由上述每个完整 unimodular 行操作给出；反向包含由每条原生成元的实际零余数给出。于是最终子模就是整个原子模，而非它的饱和、分式域像、投影或截断。

## 5. 固定源码和只编译的公开验收

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| original_pair_reset_row_reduction.py（原 R975） | 26053 | ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f |
| original_native_polynomial_rows.pyx | 9995 | c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922 |
| original_native_pair_reset.py | 10311 | a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28 |
| check-original-native-backend-compile.py | 4352 | ccef11363a0c3f73ffc005adb4551188d2d96c0b94c9ba987b94a6a98b6a3c55 |

按固定串生成的完整函数文本为 25346 字节，SHA256 为
39fa1f64f3a00d36f3df302e27faf5a62839b306400ea242af990a3408504492。
这些是源码及参数身份，不是可重算的结果数据。

新增只编译检查在公开 Actions 的原固定 Sage 镜像中运行：

    sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb

它先核实际 checkout SHA 和上述完整源文件 hash，随后在禁网、源目录只读的临时容器中调用 prepare_backend。该函数编译 Cython 声明并定义经过固定替换的整函数，读取类型大小和源码元数据；不构造任何数学矩阵，也不调用该矩阵算法。Sage 使用的官方入口是
[cython_import](https://doc.sagemath.org/html/en/reference/misc/sage/misc/cython.html)。

这一检查只回答所给镜像中的编译、加载和原串适配是否成立。即使通过，也不称其为原四交、全厚 Norm、18×9 shadow 或主目标的 PASS。尚须等唯一 v10 的真实终态，才可能把经过核定的新后端接到同一完整原对象；不得在旧作业运行时排第二个原几何作业。

编译 stdout/stderr 仅在公开作业日志中给 hash 和必要回执；不把可重算输出写进仓库或 Release。成功后的回执将追加于本节。运行时间是否改善也以同一实际原对象的完整公开回执为准。

## 6. 已消费的公开编译回执

请求 2026-11-27-0757-original-native-compile 的实际 run 为
[45962104875](https://github.com/Rogerhu12/math-research-public/actions/runs/45962104875)，
job 为 140382113685，source 为
a6a3b7e9453a2f2d0babacb26ec85dd42dc20320。
job 于 2026-11-27 07:58:04 UTC 开始、07:58:56 UTC 成功结束；
真正输出标记在 07:58:54.6941821 UTC。

该实际 Sage 10.6 镜像已经完成 Cython 编译、动态加载和全函数适配。
19 组固定串计数全部匹配；生成函数 SHA256 精确等于 §5 所给
39fa1f64f3a00d36f3df302e27faf5a62839b306400ea242af990a3408504492。
完整三项源 pin 与检查脚本 pin 均匹配。原生结构为48字节、
unsigned long 为8字节，符合本后端的完整存储声明。

编译内部 stdout 为1116字节，SHA256
c0344dfaec10aff53a5cb374ccb790b6eeeb1f9e8bcab7ca3627e029f2296024；
stderr 为0字节。宿主检查 stdout 为2184字节，SHA256
754da7dd88056c1324e4ff1d09b35dc59aa4d35cbf3ecfc9e84bb7bd3117d2ba，
exit code 为0。完整 job 日志为10393字节，SHA256
ab8f9436f080310ad77dc5fceb26020a1f68ff302d79a4c2f3b06b7f276881cc。

实际回执明确给出数学实例数为0、原几何工作流未改变、
源只读、容器禁网、临时容器删除和无输出持久化。
这里消费的是实际编译结果，不是仅凭绿色 workflow 推断执行内容。
本节仍不声称原矩阵运行、性能改善或任何几何/主目标 PASS。
唯一 v10 run45956901945 保持运行；08:00 UTC 原 job 日志读取仍为
BlobNotFound404，因此没有把不可读的进行中日志解释为失败或成功。

## 7. 未激活的原生产接线及全部原门

在 §6 的真实编译回执后，准备完整原生产接线。当前重型工作流和
v10 请求都不改动；新增请求路径不在当前工作流的 push 路径中。
这里只触发独立的小型代码准备检查，仍不运行几何矩阵。

新外层完整加载 SHA 固定的 v10 producer，将其 implementation
标识传入下一层。在原 v10 已加载 v9、发出
RANK2_COMPLETE_PROJECTOR_BINDINGS、但尚未调用 v9.main 的那个固定位置，
仅把 v9 的全局 complete_pair_reset_row_hermite 绑定为 §2–4 的完整接口。
原 v9.main 随后仍执行它原有的七处整行绑定和全部身份检查：

- 原主 producer 的完整次数有界求解器；
- 原 row module 的两个完整入口；
- 原 preimage 和 value module 的两个完整入口；
- 原 W 运输 module 的两个完整入口。

每次新接口返回时，继续核原回执中的双子模包含、每原行准确除法、
全程子模保留、不使用分式域核，以及有附列时的同一完整行操作。
输出只记录该完整调用的输入/输出/附列/操作流 hash 和原次数界。
没有选择其中几行，也没有另增一个几何替代输入。

原 R1033 的两个 projector 构造器、完整残差域、所有厚长度、
Norm 和18×9 shadow 的任何代码与验收条件都未改变。
外层只在原全部验收确已完成后打印自己的完成标记；
原 v9/v10 的完成标记和回执仍照常打印。
若某次整个输入未降素域，保留原完整后端，并如实计数；不把
fallback 当作原生运算已经发生。

原 source-dependency hook 也保留：新 hook 先附加新表示与外层的
准确源码依赖，再调用原 R1033 hook，后者继续附加原 projector
依赖并执行原 emit。它在原主 producer.main 之前运行，
所以原完整来源清单实际包含新代码，不是事后补一个无来源的标签。

新 host 的来源清单为原52项加4项，共56项；原两张特征零 PASS、
r=29、q-precision=2453、batch64、minimal、shadow/artinian、
preflight=false、禁网数学容器、只读源码和21000秒时间帽全部保持。
只有请求 schema/implementation 和实际 producer 路径指向新外层。
当前工作流仍指向旧 v10 host，未把此候选排入重型队列。

| 新文件 | 字节数 | SHA256 |
|---|---:|---|
| produce-original-native-row-artinian-shadow.py | 9280 | 4568461d1d77e5f72aeb26528193a48f4442aa575cb52086c21313c69ae8ba10 |
| launch-original-native-row-artinian-shadow.py | 11214 | 740169518ace27fa8b567752584930752521f2780ed78a7471951d89338913c2 |
| check-original-native-production-preparation.py | 7206 | 8595fec07f44dda656edb40db41809999ccc85d61b32a4990eff43f74459be7b |
| ci/original-native-row-artinian-shadow-request.json | 864 | 25c209ac9daf5a11f1b1cec7b87b86f9d1116d3a0923bebf174f14905471e140 |

准备检查还固定当前未修改的工作流 SHA256
24be40c3fc98babefcbaa53b03b16d7904e93da5500b8018c14d2e0645677a06。
它逐源核 hash、Python AST、两个请求仅有 schema/implementation 差异，
随后在同一镜像中实际编译并加载新外层及固定 v10 代码、
定义全部延后 hook。检查明确要求原 v10.main 未调用、
v9 ENTRY 仍为 None、完整矩阵调用记录为空、原 primary 构造器未改变。
这些条件区分代码准备与实际数学验收；没有据此宣称
四交、全厚 Norm、shadow 或无穷 p 已完成。

### 7.1 小型检查的稀疏工作树读取修正

首准备run45963764579/job140387453584/source d990f197a7d196e1400d7cbf997a4cf2c36b7ee8在08:11:35 UTC停止于工作流文件的FileNotFoundError。小型检查只检出本topic，工作流不在工作树；失败发生在Docker/Sage启动前，没有运行数学矩阵。完整日志9156字节，SHA256为9cf5f6269e0132481605fbbb0a03da0f499b2dff403a3f09f308fb5834481781。

修正为对同一个checkout执行git show HEAD:.github/workflows/rank2-sha-original-triangular-artinian-shadow.yml，直接读取该提交中的原文件，随后仍核完全相同的工作流SHA256。没有扩大稀疏检出、改动原workflow、放松pin或删除未激活检查。其余源码、两个原请求及数学代码不改；本节表格给修正后检查器身份。独立小型请求2026-11-27-0813-native-production-preparation-sparse继续公开验收。

### 7.2 已消费的完整生产准备回执

修正后的实际 run 为
[45964030236](https://github.com/Rogerhu12/math-research-public/actions/runs/45964030236)，
job 为140388320652，source为
0026a70fa4c916b34ee40f6be22c84a2176f562b。
job在08:13:37 UTC开始、08:14:34 UTC成功结束；
实际输出标记为08:14:32.8290160 UTC。

公开 Sage 10.6 中的原生编译、固定 v10 代码加载和延后接线准备
全部成功。原全部 source pins、请求参数及两张 char0 PASS 均匹配；
生成整函数 hash 仍是 §5 的39fa1f64…8504492。
实际检查确认 v10.main 未调用、v9 ENTRY 尚为空、
完整行调用记录为空、原 primary 构造器未改。
因此这里仍是0个数学实例的准备结果。

内部编译 stdout 为2732字节，SHA256
73c9e58b730e72b0eeeae2fb38b39eba98048d7819863787d8e698942d1ed3b4，
stderr为0。宿主检查 stdout 为4281字节，SHA256
096fb5f598c1aa1ee10ab38306ad386adc10d3e2999c8439418345986e571119，
exit code为0。完整 job 日志12577字节，SHA256
3c37a5eabd3edc84c8f32398abcf7bb645502a64bc19dec5ca269dbe6d0e34b9。
实际 checker SHA256 为
8595fec07f44dda656edb40db41809999ccc85d61b32a4990eff43f74459be7b。

同 source 的 Actions 列表也仅有这个小型检查，没有新重型 run。
当前 v10 仍是唯一原几何作业；完整原对象的数学验收及原生运算
是否实际被应用，继续由未来真实生产回执判断。
本节未将准备成功写成原四交、全厚 Norm 或 shadow 的完成。
