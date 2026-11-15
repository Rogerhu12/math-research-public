# native128 JSON与统计类型显式资格化v2：actual150/152的最小编译修复接口

## 1. 已观察到的问题和独立版本

新入口为 computations/geometry_20261115_native128_qualified_json_components_v2.py。实际原150编译stderr及原152编译stderr都已返回；本接口只处理其中已确定的两类源码问题，不更改原模型或验收阈值。

第一，v1将quoted(改成::quoted(。原条件表达式中原冒号紧接函数调用，形成?"null":::quoted(...)；三个相邻冒号使编译词法失败。v2的完整新token是一个ASCII空格后接::quoted(，即" ::quoted("。这样原条件运算符冒号与全局资格化分开，其他所有调用仍解析到同一全局JSON字符串helper。

第二，stage/exporter同时可见operator_trace128与shared_trace128的BatchStats；仅全局using BatchStats=operator_trace128::BatchStats不足以消除实际歧义。v2只在两个stage使用点、四个exporter使用点写明operator_trace128::BatchStats。它保留header中本类定义、shared_trace128::BatchStats基类及其join调用，亦不改physical文件只使用原shared统计类型的声明。

旧geometry_20261115_native128_qualified_json_components.py（15058字节/e609fb0aeae3142fcdb779004ddc0966e86c87c437da0984f50ffa814fb40d36）及所有旧Git科学源保持原字节。新v2来自该公开源，完整diff单独交付。修改对象仅在未来Actions实际临时compiler目录形成，不修改checkout或任何Git ref。

## 2. 冻结入口与CLI

新源17484字节，SHA256 5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf。

两个CLI保持原参数表：

- python geometry_20261115_native128_qualified_json_components_v2.py --operator-components [原R305/R302全部参数]；
- python geometry_20261115_native128_qualified_json_components_v2.py --strict-field-certificate [原R314/R325全部参数]。

参数位置分派保持首argv标志的原修复；不得因后续参数中包含字符串而选错入口。load_base()、load_baseline()仍暴露同一实际binder接口。原operator Python源码a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef及strict launcher cd73cb044e72052b38c6fc9d6517a7e436517f15777a4ace74333bb8a92af596仍逐SHA装载；各自的数学main、全列、预算和partial语义没有替换。

新schema如下：

| 记录 | schema |
|---|---|
| operator launcher | native-persistent128-qualified-JSON-and-statistics-contracted-trace-components-launch-v2 |
| strict launcher | literal-root-field-certificate-qualified-JSON-and-statistics-launch-v2 |
| 资格化生命周期事件 | native128-explicit-JSON-and-statistics-qualification-v2 |
| compiler input binding | native128-explicit-JSON-and-statistics-compiler-input-v2 |

编排需把实际执行的文件名、SHA及所读schema诚实更新，不能以旧e609身份解释新执行。父150/152仍是原运行证据，不被重标为v2运行。root预留160为完整152责任继任，161为所选字段230列严格消费继任；当前源本身不选择未来run、状态、参数或接受锚。

## 3. 完整源范围和逐字变换

下表原源均从公开提交d1d4c01a283d20a1d20131ece43cdcfb05ce757d逐字取得，完整路径前缀为topics/visible-flex-larger-amplitude/computations/。v2从这些原始未资格化源生成临时副本；不是从失败的::quoted副本再修补。

| 文件 | 原完整SHA256 | quoted调用计数 | v2临时文件字节数 / 完整SHA256 |
|---|---|---:|---|
| geometry_20261115_native_operator_trace128.hpp | 950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0 | 12 | 24653 / 4610e1e851a1f3b51f829355f08ef4555d1dc212b61f193db2edce5bb2a13435 |
| geometry_20261115_native_operator_stage128.cpp | 86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926 | 9 | 10747 / 2f45f84a462e0ee9f9613344994ca3117ffac0bab664c141b24e02b44ea753f8 |
| geometry_20261115_native_boundary128.cpp | c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96 | 4 | 12505 / 37f6aab4604d6c39069486527eacda8c599c69ab496dadbbc74e92175fcd17ff |
| geometry_20261115_native_physical_final128.cpp | a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 | 49 | 18202 / ecf14bf4d5cfd7a9f7796d0fa513822a05ca6cdc5a3ecc291859cff58a91b265 |
| geometry_20261115_literal_root_field_tape128.cpp | 2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb | 2 | 13519 / af2f46fd754ab4282e0e79500c5a19122c30e6a352145b9bef2f686ef2d10a34 |

所有quoted调用先执行同一精确替换，原次数必须等于表中计数，原文不得已有新token。然后只执行以下显式变换：

1. stage：std::vector<BatchStats> stats(p.depth); → std::vector<operator_trace128::BatchStats> stats(p.depth);，恰1处。
2. stage：size_t done=0;BatchStats total; → size_t done=0;operator_trace128::BatchStats total;，恰1处。
3. exporter：BatchStats &stats → operator_trace128::BatchStats &stats，恰3处。
4. exporter：四个空格后BatchStats stats; → 同缩进operator_trace128::BatchStats stats;，恰1处。

每份副本按倒序反转这些类型替换，再反转完整带空格的quoted token；恢复的UTF8字节必须等于原文件。随后核副本全SHA。声明计数、类型字符串、所有原→新完整SHA都写在v2常量中，无正则推断或广泛命名空间替换。额外检查禁止生成:::quoted(。这些检查是准确执行已声明源码的工程身份检查，不是数值接受门。

stage/exporter仍包含原using别名；使用点现在显式选中operator结构。原结构字段和继承关系不变。没有把实际编译失败时被编译器误解析成int的后续报错当成数学类型变化。physical文件中的BatchStats保持原shared结构；其实际150/152错误只涉及quoted词法。

## 4. 数值、编译和父来源的边界

以下内容逐字保留：

- 原F与独立C、完整225维Gram、原根有限迭代/分支与Cholesky/两三角回代及operator传播；
- 全224形状方向、226状态与两个mean、所选230环境列的定义；
- 完整576段、112边界响应、mixed338×112、原物理审计各自参数和未付范围；
- 原binary128状态所有权、current128右端、sigma·z64恢复、固定64chord只作近似模型的标识；
- 原阈值、十档回溯、原32上限、预算、绝对deadline、清理前hook、所有失败/partial/null与最终接受责任；
- 原Python数学launcher正文；strict内存派生仍只有既有两条来源记录插入。

编译调用仅换受控临时源路径；原g++ flags、-O3、-fopenmp、-frounding-math、-ffp-contract=off、-fno-fast-math、-lquadmath等依原调用保持。源必须在RUNNER_TEMP下原launcher建立的compiler目录，且原R283 prefix已存在并绑定。新metadata列出原e609 shim为来源、executed=false，同时记录真实v2文件及每个临时编译源的SHA。

v2没有提高精度、改变运算顺序或吞掉异常。全局JSON helper实现也未修改；加空格只防止合法作用域token与条件冒号连写。BatchStats资格化只使原意图中的现有统计类型明确可解析，不重写任何算术表达式。不能由这份静态差异声称编译已成功，更不能声称完整导数、严格证书或物理audit已完成。

## 5. 原错误和完整读回

v2保留原forward_lines函数，逐行读回和其明确的未转发列表语义没有偷换。原150完整同job runtime以及152继任接线中的清理前全byte分段读回必须继续保留；它承担非UTF8、单行超过局部line帧界及全部原stderr的完整性。不得用forward_lines的摘要代替该全byte通道。

全部编译stdout/stderr及process.json仍由实际原launcher保存到临时目录；父编排应在清理前完整分段读回，保原size/SHA、line/chunk序号与所有原字符。新v2不把任何child returncode改成0，不把certificate/result未生成解释为unresolved=false的证明。成功进入后续数学阶段后，原full result和所有列/未决后缀仍按原完整语义流输出。任何摘要限额造成transport incomplete必须与原数学阶段状态分开。

当前修复的来源是实际150的149行stderr以及root独立读回的实际152 stage99行/audit35行stderr。原150 exporter未生成，严格列全部未运行；原152 stage/audit编译失败及boundary/mixed未起按R337保留。新的160/161须真实重生原输入，不能由被清理raw的hash假恢复。

## 6. 静态支付和剩余实际责任

本地环境仍不可用。已完成的只有读取公开完整小文本、精确计数替换、每份完整逆变换相等、UTF8字节数和SHA256计算；未声称Python AST、C++编译、数值fixture、矩阵或科学执行。上述五份临时C++副本均已按显式替换在内存重建并核整件SHA，保存于协作store；无需把可重得副本额外提交main。

完整diff相对e609为8411字节，SHA2564077a3aeb44c778ce08f64d30253fef4e0a33be47f02a55cf6e3d92ac8fa405b；它用于审读，数学源不复制为新的实际数值对象。未来Actions正常解析、实际编译和原科学入口承担真实执行，错误原文继续完整读回，不增加fixture或新的独立批准流程。
