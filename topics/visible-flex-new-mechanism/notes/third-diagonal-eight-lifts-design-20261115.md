# 八个额外完整第三模板的对角提升：最小原式消费者设计

日期：2026-11-15。状态：**源码已写成；本设计中的新人工及新研究目标均尚未执行。** 全部首次检查和实际运行只在公开仓库 Rogerhu12/math-research-public 自己的 GitHub Actions 中进行。本稿不登记任何新的数值秩或成员结论。

入口脚本：scripts/literature_third_diagonal_eight_lifts.py。建议 lane：third_diagonal_eight_lifts。

源码稳定首版为 26756 B，SHA256 075b106b1fb15fbcf1b2460b501ac7309d2fdfdf249e75fdde6078deabaca1a0；未挂 UTF-8 Git blob 85b70151705ec23d214d1c84b62c33e21274deff。本次环境无终端，按根 README 第 8 条例外仅提交这个小文本对象，由 root 统一挂树、提交、推送和派发；本代理不更新 ref。

## 1. 需要补上的具体内容

R87 已由原函数的准确有理子式证明完整第三空间 $W$ 的 36 个模板独立。R208 已从已发表的全部 151 个对角第三列覆盖推出

$$
\Delta W=\Delta W_{71},
\qquad
\Delta\tau(q)=\tau(q;q,q).
\tag{1}
$$

R247 将完整响应空间写成 Jacobi 商与八个额外第三类的像，给出 $228\le\dim R\le232$，并证明存在

$$
\chi_j=\tau_j-\gamma_j,\qquad
\gamma_j\in W_{71},\qquad
\Delta\chi_j=0,
\tag{2}
$$

使

$$
W=W_{71}\oplus\operatorname{span}\{\chi_j: j\in\mathcal J\},
\quad
\mathcal J=(30,32,34,37,40,100,104,109).
\tag{3}
$$

然而旧 closed-C1 原输出没有保存这八个 $\gamma_j$ 的完整坐标。它保存了 151 个来源标签、若干端点关系和旧 pure P1 目标坐标；五个 companion 原根也不能替代八个 (2)。本次只填这一项具体缺口。

新消费者输出每个 $\gamma_j$ 在原 28 个完整 R71 交换子中的有理坐标，并直接从有颜色的原差 $\chi_j$ 验证其整个对角函数为零。它不生成任何新的第四响应，不计算完整 fixed-circle period 观测商，也不新增实际有符号成本实现。

## 2. 旧 18 个输入的准确角色

沿 E8 原次序

$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)
$$

定义完整第三交换子

$$
C_{ab}(u;v,w)=
\Phi_a(u,\Phi_b(v,w))-\Phi_b(u,\Phi_a(v,w)),
\qquad a<b.
\tag{4}
$$

28 个索引由 Python 的 combinations(range(8),2) 字典序给出。已只读核过两个冻结来源：

- literature_full_phase_bridge_exact.py 的 control_templates：最初 28 个模板正是 (4)，之后才加入局部与闭 C1 系数。
- literature_closed_c1_endpoint.py 的 run_research：其最初 28 列是相同 E8 次序及相同符号的 $\Delta C_{ab}$。

因此 R208 的旧保留索引可直接对应完整 W 导出中的同号原根：

$$
\mathcal I=(0,1,2,3,4,5,6,7,8,9,10,11,12,14,18,20,21,24).
\tag{5}
$$

本次从已经保存的完整原根恢复这 18 个对角输入，各做一次共同词表示。这是为了给八个新目标提供必要的参考坐标，没有恢复其他 133 个旧对角目标、重跑 151 列消元、重跑旧纯 P1 或旧第四 response。

程序不硬编码“18 个真实独立”。共同消元只保留实际遇到的枢轴；若参考之间存在额外准确关系，也不会创造假枢轴。报告中的 reference-restoration 枢轴数只说明这次坐标求解所用输入，不把它包装成重新研究旧空间的目标。

## 3. 原输入及全部来源绑定

实际只需三个旧 notes 目录。没有新的 profile、几何、标准圆、端点数值或独立 history 参数。

### 3.1 已发表的完整 W-only 原 DAG

目录：

notes/actions-43645177423-1-local_fourth_quotient

来源 run 43645177423，source 2f1b809c0b0abb7a26303d36940edc203815f872。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| local-fourth-quotient.json | 3982 | 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a |
| receipt.json | 31846 | c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba |
| local-fourth-quotient-W-original-expressions.json.gz | 7377 | 45cbdc8f38a4b5561924badaf9cd68a93a7fa71c6264d95489034703af4ee44a |
| 解压原 DAG | 31750 | 615d848611aaf787bc3ae790b4b1f81fe91338301bcb57afdfd111758cf533bf |

原 DAG schema 为 visible-flex-R109-local-fourth-quotient-static-v1-original-expressions，content_scope 为 W-only，包含 W0 至 W35 与 170 个原 atom。所有 primitive 都是同右锚的真实 $\int_{r_*}^{\xi}$。

这份旧 main 的 completion=output_limit 仅表示其较大的总摘要超限。完整 W-only 导出在后续局部第四研究之前已成功写出；新消费者只要求这份导出的真实来源、原字节、完整 36 根及原 hash 已匹配，不借该 completion 声称旧局部第四已完成，也不因它而重跑 W。

复用冻结的 reader.load_templates，依次核 main、公开 terminal receipt 的 repository/run/source/lane/source-file、gzip 与 raw 字节和 hash、原 root hash、v2 36 个模板身份及三次 degree。新脚本另核 main 所列十个原生产源的实际字节/hash与当前递归源码库存相同。

### 3.2 v2 完整第三模板的原 hash 回执

目录：

notes/actions-43633746055-1-full_phase_bridge_exact

文件 full-phase-bridge-exact.json，157380 B，SHA256

7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960。

来源 run 43633746055，source 26c3f2c0308d179a094d3967cfb7189db426081e。

这个大于 100KB 的既有原报告只由 Actions 终端读取，未通过文本 API 搬运。本次只读已冻结原 hash 和 retained 原索引，不调用 compile_colored_local、raw_decomposition、control_templates、pre_reduce_templates，亦不重算旧 152 个第三模板或其 116 条关系。

### 3.3 旧 18 个输入标签的已发表 main

目录：

notes/actions-43632772378-1-closed_c1_endpoint

文件 closed-C1-endpoint.json，13911 B，SHA256

622cd662e60eed74e58f59bb52981aed6a209eeaf4664bc7304a5e3826b6da86。

来源 run 43632772378，source 31a276f6f4b2361d10bea9a46fea307a951bb639。

只核原完整 main 的字节/hash、schema、completion、repository/run/source、151=28+56+67 的来源计数及 (5) 的索引。不会调用这个旧脚本的任何人工或研究入口。

### 3.4 八个新目标的完整原根

完整 W36 中 retained 位置 28 至 35 对应下表。这是完整外槽 a、对称内槽 b,c 的根，而非已经对角化或已响应的根。

| 原索引 | 原模板 SHA256 |
|---:|---|
| 30 | be8a31110800e396af0d8b2c7d240584f03cd30bcf4e1d1d8f222f2cafc8c199 |
| 32 | c8f4568fbddee3985dfd3245aff22592bb065d22dbdc958fc61433ba20279f79 |
| 34 | 4e76c7b917c4a00138308388d72c40def5837044d287c28242f91d635bf5f312 |
| 37 | 94b42fb4261209e6e6e72c078b6e873dfe08dd477672afdcb0156f95051ead28 |
| 40 | b5155855451e65acb83b0efd8ec51e6467fe343fa80fbeab6c04e1e523c0f368 |
| 100 | 8aa68ac3defca7d0d88ec9b5c67dc7b30bedc569129d6fbd8705314fbe331e2d |
| 104 | 578763eecd81ff4e4bf2f3775b253c4315c6c3d58cfb2e3346524b79d8203f0d |
| 109 | 63ec5cb74cb487c52a3e81f1f0b010352f7df57edabb1f08f42dea9093eb52ee |

## 4. 新运算的严格边界

### 4.1 一次必要输入恢复

原 DAG 全 36 根均解码并核身份；只有 (5) 的 18 个参考与八个目标被取对角。其余十根不取对角，也不作词转换。

对角替换用 ColoredRing.substitute 同时令 a=b=c=q。它递归作用于全部真实 jets 和全部嵌套原函数，保持原 $\int_{r_*}^{\xi}$ 号、共同右端和左尾。

参考输入的词 map 使用 R178 的固定单颜色 q 次序，最高 profile degree=3。所有最终存留 letter 都检查：

- 坐标次数非负，只有 q 颜色；
- 原函数 letter 有正 profile 次数；
- q 最高 jet 为零，或该最高 jet 出现至少两次；
- 整个局部因子加词的总 profile 次数准确为三。

这正是 R179 的规范余词语法。不使用旧可能有 cycle fallback 的 map，亦不把非规范行当独立函数。

### 4.2 八个目标的有理坐标

对每个目标的真实对角原根 $t_j=\Delta\tau_j$，求

$$
[t_j]_{\rm word}=\sum_{i\in\mathcal I} c_{ji}
[\Delta C_i]_{\rm word},
\qquad c_{ji}\in\mathbb Q.
\tag{6}
$$

消元复用已冻结 ColoredRing 模块中的 JointSpan；目标不会被加入参考 basis。因此第一个目标成功不会改变后面目标允许使用的参考空间。

这里求出的组合不按标签匹配、不对任何 profile 采样、不取模素数，也没有独立赋 primitive 值。

### 4.3 必须通过的新原差

词坐标成功后，回到原 a;b,c 三颜色函数，先构造

$$
\gamma_j=\sum_{i\in\mathcal I}c_{ji}C_i,\qquad
\chi_j=\tau_j-\gamma_j.
\tag{7}
$$

再对 $\chi_j$ 单独做同右锚的真实三槽对角替换，并送入**另一个独立词 map**，核

$$
\Delta\chi_j=0.
\tag{8}
$$

第二个 map 只处理这八个新原差；不会把 18 个旧参考作为独立科学目标再跑一遍。新原差可共享它们实际出现的已完成 primitive cache，这不替代其原式输入。

(8) 的零证不依赖“两个标签相等”或代表秩的解释。即使不使用 R179 的独立性，sound 转换为零已经给原函数恒等式。R179 只明确共同词坐标的语法解释。

任何残余都准确保存于临时报告并标未完成；不能称 $\chi_j$ 的整个完整函数为零，更不能据此声称完整响应或固定圆商的非成员。R208 已有包含性，若参考或新原差未闭合，应先定位接口、归一或来源差别，不删除残项或默认旧理论错误。

## 5. 成功输出的含义

每个新目标立即向 stdout 打印：

1. 原索引、retained 位置、原完整/对角 root hash。
2. 在原 28 个交换子次序下的完整有理向量，以及每个非零系数对应 E8 pair。
3. $\gamma_j$ 与 $\chi_j$ 的完整有颜色原 root hash。
4. 从完整 $\chi_j$ 再取对角的原 hash、原项数，以及 fresh word 零 hash。
5. 保留右锚与完整 a;b,c 槽的范围说明。

全部八项成功后，(3) 的具体补空间已给出。其线性独立性继承 R87 的完整 28+8 原模板独立，而非来自“$\chi_j$ 原项非零”的不可靠判断。

由 R83 的完整响应公式及 R208 的 pure 投影公式，

$$
\Delta\chi_j=0
\ \Longrightarrow\
\pi\mathcal B_E(\chi_j)=0
\quad(E\in E_8).
\tag{9}
$$

于是获得 64 个**可直接重建的完整 pure 零响应定义**；本消费者没有计算这 64 根、证明其独立性、把它们在某固定圆的 gauge 商中判值，或支付实际负成本。

完整 pure 零响应空间仍是 R247 的

$$
R_{\mathrm p0}
=(R_{71}\cap\ker\pi)
+\mathcal B(E_8,\operatorname{span}\chi_j).
\tag{10}
$$

不能删掉第一项，也不能把这 64 个形式生成方向误写成整个 $R_{\mathrm p0}$ 的维数或固定圆观测像。

## 6. 源码与复用边界

新脚本未修改任何旧源。关键复用源固定如下：

| 源码 | 字节数 | SHA256 |
|---|---:|---|
| literature_full_m8_tail_response_projection.py | 32096 | e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345 |
| literature_color_priority_words.py | 21642 | ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9 |
| literature_colored_profile_algebra.py | 15738 | c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f |
| literature_pure_bulk_exact_membership.py | 33718 | f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70 |
| literature_local_fourth_quotient.py | 38857 | 9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0 |

reader 的名字含 m8，但本次只调用其原输入读取/绑定函数。没有调用其 research、m8 evaluator、旧 probe、full_response、四块投影或旧 288 列目标。

源码库存递归静态读取当前脚本的本地 literature_ import 树，保存每件的字节/hash。它只读源，不调用任何额外研究入口。生产 main 原 source_hashes 中十件旧数学源还逐项核同当前库存。root 的公开 request 应按同一递归源码树绑定。

## 7. 新人工范围，均未执行

--toy-only 定义了八项新的小人工，只验证本消费者新增接口：

- 一个目标用同一组准确有理系数由固定参考表示。
- 人工冗余参考不会产生假枢轴，也不强制预设秩。
- 从 target 减 full-colored 组合后，保留非零有颜色 hook，fresh 对角为零。
- 三槽替换穿过两个嵌套原 primitive，保共同右锚。
- 人工非成员残余不会被置零，也不会加入参考 basis。
- 原 $\int_{r_*}^{\xi}$ 的正号与微分原函数匹配。
- 非规范 letter 不获 R179 语法通过标记。
- 旧输入索引次序被更改时拒绝，即使未打开任何旧研究目标。

这些只是在源码中定义了待执行检查。没有执行旧 10/31/40/70/151 人工，没有把源码阅读当成 passed。

## 8. 预算、失败与可观察性

建议实际：120 秒，512 MiB polling threshold；外层 Actions 保留其真实 wall-clock 硬截止。其余默认：

| 预算 | 上限 |
|---|---:|
| profile/coefficient nodes | 300000 |
| profile atoms | 40000 |
| 单原表达式/词表达式 terms | 40000 |
| 每个词 map 的 primitive calls | 150000 |
| 每个词 map 的总 cache entries | 150000 |
| 被监测 rational 调用次数 | 1000000 |
| 被监测 rational 位长 | 8192 bits |
| 内存 proof 序列化大小 | 8000000 B |
| 临时 main | 95000 B |

时间与 resident memory 由继承的 Limits 轮询；512 MiB 不是程序宣称已安装的操作系统硬限。rational 次数及最大位长只覆盖 MonitoredLimits.rational 的监测点，不冒充所有原 DAG 加乘的总运算数或总最大位长。

只在八个新原差全部成功后标 complete。budget/输入/实现失败明确保存 phase、已成功目标和错误，不把未做目标记成零。每个成功目标在构造完后立即打印，所以后续退出不会抹掉其已完成坐标。

本小消费者没有设计外存续算数据或伪装可恢复的 checkpoint。若真的预算退出，由 root 根据真实停止位置决定必要后继；不会私下重跑旧 151 或扩大任务。

## 9. 根 README 第 15 条与输出

本次不保存可重算的 machine proof、DAG、词行或 Actions 输出 payload 到仓库、Release 或 artifact。

程序仅在 runner 的临时输出目录写一个 main JSON。最终给 metadata-only publisher 的是它的名称、bytes、SHA、源码、参数、run/source 与人类结论。完整数学摘要和全部八个准确坐标直接打印到 stdout，避免“成功但关键结果只留在不可读临时文件”的缺口。

参考词行、目标词行和 fresh 原差证明组织为内存 proof，只报告其 bytes/SHA。八个完整 $\chi_j$ 的重建已经由原 W36、打印的有理坐标及冻结新源码准确确定，无须保存新大 DAG。Actions 结束后该内存数据消失，不创建下载或分块绕行。

失败小 main 同样只发布元数据；数学完整性判断不能由 job success 代替读取实际 summary。

## 10. 实际 CLI

开发入口，同一公开仓库：

~~~text
python topics/visible-flex-new-mechanism/scripts/literature_third_diagonal_eight_lifts.py
  --toy-only
  --max-seconds 30
  --max-memory-mib 512
  --output @OUT@/third-diagonal-eight-lifts-development.json
~~~

研究入口：

~~~text
python topics/visible-flex-new-mechanism/scripts/literature_third_diagonal_eight_lifts.py
  --w-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient
  --third-directory topics/visible-flex-new-mechanism/notes/actions-43633746055-1-full_phase_bridge_exact
  --reference-directory topics/visible-flex-new-mechanism/notes/actions-43632772378-1-closed_c1_endpoint
  --max-seconds 120
  --max-memory-mib 512
  --max-nodes 300000
  --max-atoms 40000
  --max-terms 40000
  --max-word-calls 150000
  --max-cache-entries 150000
  --max-rational-bits 8192
  --max-monitored-rational-operations 1000000
  --max-proof-bytes 8000000
  --max-summary-bytes 95000
  --output @OUT@/third-diagonal-eight-lifts.json
~~~

当前公开 dispatcher 仅展开 @OUT@；三个旧目录在 request 中使用上列完整仓库相对路径，或直接采用脚本的等价默认值。两种入口都要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。不会提供私有计算捷径。

root 统一安排该单一新 lane；原 SOC 请求在 source 9ca83546823ea077bd8b9e6ef2d10344788518e5 的历史中冻结；root 后续以新的 request 切换到本单 lane，既有 SOC 源码保持不变。成功后直接登记八个准确提升，并据 (10) 设计真正需要的后继完整 period 观测，不停在“补了八个列坐标”的阶段，也不提前声称其像满射。

## 11. 已核当前公开接线方式

已只读核 main 的 continuation workflow（Git blob fbb473541fd4d6ae9a42e787a8fe8f105b548c09）与 metadata-only publisher（Git blob ef73128f1a1a657a75456f2f078548159287aaab）。只需以下窄变更，由 root 完成：

1. .github/workflows/visible-new-mechanism-continuation.yml 的 allowed 集合加入 third_diagonal_eight_lifts；scripts 映射该 lane 到 literature_third_diagonal_eight_lifts.py；flags 映射到 --toy-only。
2. sparse-checkout 新增 /topics/visible-flex-new-mechanism/notes/actions-43632772378-1-closed_c1_endpoint/。W-only 与 v2 两目录已经在当前 sparse 列表中。
3. topics/visible-flex-new-mechanism/scripts/publish_actions.py 的 --lane choices 和 complete_research_compilation_without_candidate_geometry 集合加入该 lane，其他 metadata-only 发布、pull/rebase 与 README 检查均保持。
4. topics/visible-flex-new-mechanism/computations/request-continuation.json 使用现有 jobs[lane].development 与 jobs[lane].research 两个字符串 argv；source_sha256 绑定新 driver、所用递归源、变更后的 workflow/publisher 以及现有 printer。首跑没有 completed_development shortcut。
5. 现有通用步骤已对新 driver 做公开 py_compile，随后 development 再 research；无需扩大 max_args=90（本次研究 30 个字符串），无需给其他 lane 加分支。新脚本自己打印完整数学结果，故 print_research_outcomes.py 不需修改。

此说明只是一份静态接线清单，尚未修改 workflow、publisher、request 或任何 ref，更没有派发 Actions。
