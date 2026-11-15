# R133：整数上界修复与唯一28阶段原字节续接

2026-11-15。公开 [43675967042/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43675967042) 在修复原 leading 字段名后，通过10个身份/域门并完成28个自然阶段，随后在尚未完成的 phase_comparison 中因 int 没有 upper 方法而退出1。此次只修复该类型入口，并逐字继承成功阶段。

## 实际边界

原 SCI f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739，原 algebra 1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53，原244输入 manifest 76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a。

- 失败 native：24929 B，SHA256 b46953d23b021359d1f98a55e820a28d2cfbce5fe2f7b93e3841d47fe0fe6d35。
- [process](correlated_adjacent_piece_first_Airy_sources_ci/run-43675967042-1/consumers/process.json)：5410 B，SHA256 da9445d1a11f4d956a949b36fbfb45a7a417f0465c66208a09e141170b79e573。
- [publication](correlated_adjacent_piece_first_Airy_sources_ci/run-43675967042-1/publication.json)：10445 B，SHA256 e1944e1f94564ba0aa4c2fb3ad5bdaab5506f9c6c8484c97e31732eee3c24017。
- [worker](correlated_adjacent_piece_first_Airy_sources_ci/run-43675967042-1/worker-process.json)：4431 B，SHA256 968e9c931bbd79fa330c1f34145c2b7d9268fd2f3c1cb791f64fea594d3295da。
- 真实 SCI 用时10.236884446000033秒，实际返回1；错误准确为 AttributeError: 'int' object has no attribute 'upper'。
- 已完成25个参考范数阶段、1个完整 holomorphic-majorants 阶段、1个真正2548 signed-cubic差、1个原 intrinsic 消费。完整新源行、完整新case均为0，不能将其当成已得两邻片最终缩界。

原 worker 两次真 pull 的 README 差异为空，末次04:16:24.877143 UTC到 cc59132a457e053012818c8ecc55433180e3dab5。原失败完整保留；没有把成功前缀或失败名称改写成新来源。

## 唯一数学代码修复

algebra.up 原先直接返回 abs(v).upper()。现在只在此前增加：

    if isinstance(v,(int,Q)):v=ex(v)

其中 Q 是原 Fraction，ex 是原 exact-rational 到 Arb 的有向实现。原 Arb/acb 输入仍走同一旧表达式；没有添加浮点中转或修改原球。失败来自尚未完成的 phase_comparison 构造 scalar(1)，先前成功的28阶段均未经过这条失败路径。

25个范数使用原 producer joint_coefficient_norms 和 whole.up；majorants 使用原 reference_majorants/whole.decode/whole.up；signed cubic差只用 Fraction 和原 dyadic 系数；intrinsic 阶段直接消费原闭球与原 Arb 操作。各已执行算法、参数与数据保持原样。

## 严格限定的原字节继承

唯一 prefix-policy 固定原 run、attempt、native、process、publication、SCI、algebra、manifest 和四个 runtime 版本，并要求原10门、28个准确阶段名和原失败边界一致。每个阶段须同时匹配：

1. 原 native 中的 file/bytes/SHA256/stage_kind；
2. 原 publication 的同一原字节收据；
3. 当前 manifest 对该原文件的精确 pin；
4. 文件本身的原 SHA256、旧 source/manifest/algebra/runtime header 与 payload SHA256。

旧 header、旧 payload 和整个 gzip 文件都不改写。仅上述28个精确 name 加原 byte receipt 可使用旧身份；任何其他新阶段仍须严格匹配当前 source、manifest、algebra、runtime。CI、worker、SCI 共用这一个明确 policy，未开放通用跨源 resume。

原 SCI、algebra、manifest 三个完整文本分别按原 blob 逐字归档到 notes/adjacent_piece_scalar_coercion_inputs/。Actions 用 AST 核原 SCI 全部顶层参数赋值和11个相关数学函数不变；helper 全文本必须恰好等于上述一行扩展。旧成功阶段在任何新算术之前复制，已完成 builder 不再调用。stdout 单独列继承阶段数，避免把28原阶段记成新增数学。

完整原输入、28逐阶段收据和五个新代码文件元数据见 [输入清单](2026-11-15-R133-adjacent-scalar-coercion-accepted-prefix-inputs.json)。

## 新执行件

当前279个 pin 中，原244项的241项逐字相同，只更新 SCI/algebra/CI 三个代码文件；新增加固定28原阶段、6个原记录/归档和policy。六个原始完整外部case、数学参数、旧输入角色、完整 mean/seam 仍原样。

| 文件角色 | 字节数 | SHA256 |
| --- | ---: | --- |
| SCI | 53824 | fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d |
| algebra | 24511 | 071065fcdad85536af613d0d198b0034f27ee575b6b2a1c31752cb6ea4a9bc0b |
| prefix policy | 11789 | b5706e3bdf98c0fad96e43b552208f9ee953b472947e4fb3965ef076faaa8a97 |
| CI | 20191 | 41282a7fb1f63f1a307a7ff721e4e1c553388613feb3c033013a9dfc10aaa2f5 |
| worker | 28288 | 602321a58faf7135750609832618a481bb548fb0101941498db29b6b7acf3c11 |
| 279-input manifest | 94694 | 57b978dbff16590d593686a8c7b98b8374aae532b500ec88cf975d3ab3821695 |
| workflow | 6595 | d4be03c56b66bc03e98c825519bba6f00c9941359685681418290929e0f98946 |

本次文本与出处检查不运行数学。Python AST 和真实后续计算只在本公开仓库 Actions 执行。该部署不宣称新的完整源界、修正 seam、正权端口或强返回已成；继续读取新 actual process 决定结果。
