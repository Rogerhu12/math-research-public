# 已发静态局部原式的完整 m=8 纯尾响应商：新消费设计

日期：2026-11-14。状态：源码已静态核读，尚待公开 Actions 的新人工接口检查及研究实际；本文不记录任何未运行的检查为通过。

本设计对应独立脚本 [literature_static_m8_tail_quotient.py](../scripts/literature_static_m8_tail_quotient.py)。已有生产者、成功响应消费器、原数据和旧失败回执均冻结。

## 1. 新目标与确切边界

R116 已实际得到同右锚、完整 $q=(c-\xi)^8$、$r=c-\xi$ 的真实 $\mathcal R_8$ 纯 $-4$ 响应投影秩 $31$，四块反射投影秩 $15$。其完整证书保存全部 288 原列的准确有理多项式。

本次新目标是把已经公开的导数权零局部密度

$$
L^{[0]}=v^{[0]}-\sum_i m_i^{[0]}\,\mathcal B_{E_i}(N^{[0]})
$$

的全部 $-4$ 几何 Laurent 系数，在同一尾族上直接代入，求它们在上述准确响应像中的商。局部原式已经带完整 $-4$ phase 系数，不再额外除以 $16$。

所有输入均为已发完整数据；不重新编译 $W$、第三基、低阶场、第四 forcing、旧 P1 目标或旧有限节点查询，不重算 288 个响应公式。仅把其中已经证明独立的 31 个原多项式按证书原主元顺序作必要的分解，供新目标消元使用；原 257 个依赖不再重验。

本次还单独标出 R117 的完整两模式方向 $G$ 的纯尾投影。$G$ 的完整函数非成员性质与它在本尾族的投影成员性质是两个问题；本次不重复完整两模式 7/8 子式。

## 2. 两份完整输入及公开回执

第一份输入来自 run **43645177423**，source **2f1b809c0b0abb7a26303d36940edc203815f872**，目录：

- notes/actions-43645177423-1-local_fourth_quotient

| 文件 | bytes | SHA-256 |
|---|---:|---|
| local-fourth-quotient.json | 3982 | 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a |
| receipt.json | 31846 | c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba |
| local-fourth-quotient-original-expressions.json.gz | 657195 | ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace |

完整原式解压 3518194 bytes，SHA-256 d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。它含 430 原 roots、3319 原 atoms，content_scope 为 W-and-local-static-density，只含几何导数权零。

3982 bytes 的主报告 completion 为 output_limit，是摘要上限，不是原式导出失败。消费器不篡改该状态，而使用真实终端发布 receipt 的 run/source/output/source-file 身份核对已完成的完整导出。

第二份输入来自 run **43646543691**，source **f0652a013fe546778300f0213e659f63ab96ed07**，目录：

- notes/actions-43646543691-1-full_m8_tail_response_projection

| 文件 | bytes | SHA-256 |
|---|---:|---|
| full-m8-tail-response.json | 9591 | 7237cadaac3c4581862d8aee86b94692f0e2436ab7fdb7e393c7b721125d61a7 |
| receipt.json | 31399 | 640bf2e0f17bfa635dc688581a192855f372bc7aa840c0ad97614d8696e59de1 |
| full-m8-tail-response-certificate.json.gz | 44576 | b0859868f2db2a08ca1b2831e5ab010840eed8e7ebda01fca49d598822d147a4 |

证书解压 274274 bytes，SHA-256 a8b5577903e419d2eabe2c327c2c721401acea2d0845017f86c260b2ddb8c36c。

冻结依赖：

- 原局部生产者 SHA-256 9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0。
- 成功完整响应消费器 SHA-256 e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345。
- 原 $c,r$ 有理适配器 SHA-256 98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b。
- 原 v2 第三 receipt 继续使用 notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json 及 dual.read_receipt 的既定完整来源门。

源码中的字节、hash、run 和 source 已固定，输入路径仅可更换存放位置，不能替换内容。

## 3. 原式、颜色、锚和缩放

使用冻结 decode_expressions 恢复原 DAG，并对全部 430 个 roots 重算原内容 hash。全部原模板仍按真实 v2 retained indices，从 152 条 all_original_control_templates 的 original_template_sha256 核对，且与 R116 证书消费的 36 原模板逐项相同。

只评价 local_roots 中 mode=-4 的 roots。每个非零原式的颜色次数必须严格为 $q^4$；含 $\bar q$ 的 mixed root 会被拒绝。全部 mode=-2 roots 仅作为完整输入解码及 hash 验证的一部分，不执行本次研究代入。

原式中的右 primitive 为

$$
I_cF(\xi)=\int_c^\xi F(t)\,dt,
$$

而冻结尾适配器的 $J$ 为反向积分，因此原 primitive 直接执行 $-J$。不改锚、不把 primitive 常数独立赋值、不删除嵌套 primitive。

原 DAG 在 $q=r^8$ 上的准确代入按完整单项式总次数分块。四次 profile 的真仿射权 $w$ 对应

$$
a+b=32+w
$$

的 $c^a r^b$ 行，因而先取原式真权再代入，与代入后按总次数分块相同。未出现在响应像中的权和行仍完整保留，不能把一般局部成本截到响应支撑。

## 4. 准确商计算和完整证书

每个原几何系数的代入多项式，以及每个非零真权分量，都写入新完整 gzip 证书。对分量 $T$ 得到

$$
T=\sum_{j\in J_w}\lambda_j\,P_j+R,
$$

其中 $P_j$ 是 R116 已发的原基列，$R$ 是使用原主元顺序得到的完整余多项式。每个差式均以有理数准确验证为零，保存所有 $\lambda_j$、全部 $R$ 行，以及落在响应行支撑外的子集。

“余多项式在原行支撑内”不等于“在原响应空间中”：原响应秩为 31，原行支撑数为 45。因此人工接口检查特意包含支撑内但非成员的例子。

对同权全部新余项求准确商秩，保存独立新系数和完整依赖。这是静态几何系数的形式 span 投影结论。四块的偶总次数作用仅给出该系数商的偶权部分维数；未评价任何真实闭路径，不把它当成整条路径已实现的障碍。

## 5. 单列 G 的同源检查

取原 geometry_key

$$
(1,3,0,0,0,0,0,0)
$$

对应的完整 $-4$ 原 root，再作 ScalingGrading.project(root,1)。其原式 SHA-256 必须为：

- 4608912701e99a514cff0dcb93b896200beeb6e3cbead9a70547b78e00d18c7a。

该 hash 属于真权 $1$ 投影后的原式，不是未经权投影的完整 geometry root。研究代入仍复用上文已算完整多项式的总次数 $33$ 分量，不重复原研究公式。报告将完整给出 $G$ 的纯尾多项式、相对于已发 weight=1 原基列的系数和余项。

无论结果为成员还是非成员，都只对该纯尾投影成立。特别地，纯尾成员不能推翻完整两模式 $G\notin\mathcal R_8$ 的真函数证明。

## 6. 开发检查、预算和公开命令

新脚本先在公开 Actions 执行 py_compile，再执行 --toy-only。七项人工检查只用小手造多项式及颜色，检查准确成员、支撑内非成员、支撑外余项、零目标、完整权分解和 pure/mixed 颜色门；没有读取研究输入或评价 $m=8$ 研究目标。当前尚未运行，不预写 passed。

建议 lane 名 static_m8_tail_quotient。命令从 topic 目录执行：

~~~bash
python3 -m py_compile scripts/literature_static_m8_tail_quotient.py
python3 scripts/literature_static_m8_tail_quotient.py \
  --toy-only --out computations/run-static-m8-tail-quotient/static-m8-tail-quotient-development.json
python3 scripts/literature_static_m8_tail_quotient.py \
  --local-report notes/actions-43645177423-1-local_fourth_quotient/local-fourth-quotient.json \
  --local-publication-receipt notes/actions-43645177423-1-local_fourth_quotient/receipt.json \
  --local-export notes/actions-43645177423-1-local_fourth_quotient/local-fourth-quotient-original-expressions.json.gz \
  --response-report notes/actions-43646543691-1-full_m8_tail_response_projection/full-m8-tail-response.json \
  --response-publication-receipt notes/actions-43646543691-1-full_m8_tail_response_projection/receipt.json \
  --response-certificate notes/actions-43646543691-1-full_m8_tail_response_projection/full-m8-tail-response-certificate.json.gz \
  --third-receipt notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json \
  --max-seconds 240 --memory-mib 1024 --max-operations 10000000 \
  --out computations/run-static-m8-tail-quotient/static-m8-tail-quotient.json
~~~

sparse checkout 必须包含 topic/scripts、以上三个 notes 数据目录，以及正常 README/request/publisher 依赖。完整旧 gzip 不经 API 读取、拆分或编码；Actions 自己读完整文件。新增完整 gzip 同样由公开 Actions 的终端 Git 发布。

总研究时间预算 240 秒、RSS 1024 MiB、多项式操作及有理消元操作各至多 10000000；中间多项式至多 5000 项、总次数 80、有理数位数 8192。输出完整证书原文上限 40 MB、gzip 上限 4.8 MB。主报告保持 95 KB 以下；若摘要过大，完整报告另存 gzip，短报告仍保留来源、核心秩、G 和完整证书身份。失败照实输出 incomplete，不缩窄目标冒完成。

## 7. 尚未支付的实际条件

所有几何 Laurent 系数在本次代数中保留，不任意设为自由可实现控制。尤其未施加真实 $M=0$ 的几何零矩约束，未把局部密度积分成实际基准成本，也未计算其导数权 $2,4$ 部分。

因此，非零局部余项不能直接宣称周期非零、符号障碍、真实路径不可行或完整第四商维数。成员结论同样不能宣称其余导数权、完整 mixed mode、ruling 或全部 pure tail 已被支付。新输出的用途是识别下一项真实商门的具体分量，继续与完整函数方向及几何约束联调。
