# R443 新科学入口设计：原 Q／三尾 current 联合核的完整 self 像

日期：2026-11-16。状态：**源码与设计仅经静态阅读；未执行、未编译、未运行人工或科学检查。** 首次执行仅由 root 在公开 Actions 发起。本文不是 R443 结果报告。

入口：

- scripts/literature_joint_kernel_complete_self.py
- computations/request-joint-kernel-complete-self.json
- .github/workflows/visible-joint-kernel-complete-self.yml

## 1. 唯一新问题与停止边界

R434 已经完整支付原 144 个 B(E,Z) 标签的 whole-Q 映射、85 维系数核及其三真实尾 current 像。其 current 消元的 53 条 dependent 关系，精确给出这个 85 列空间中三尾 current 同时为零的系数核。这里的“53”是原系数空间事实，不是已经知道的 self 像维数。

本次只计算这 53 条关系的完整 self partial，并回答：

1. 其真实同锚 primitive 与其它项合并、再限制到 Af=0 后，是否确实成为局部三阶以下的 Laurent jet current？
2. 若是，其完整 formal self 像、核、原始系数证书是什么？
3. 把原 R435 的 K0…K10 加入后，与 R440/R441 已付的二十二维 formal current 空间相比，是否还有新方向？

没有新 profile、母形、Af 根或实际点的评价。没有新的实际根秩、实际路径截面、完整 period 或十三行解决断言。即使 union 像仍恰为22，也只说明本次原144联合核加K轨道这个明确模块没有第23个 formal current，不能推广成整个 R 的分类。

**旧工作零重跑：**

- 0 原18算子构造或递推；
- 0 原144 whole-Q 映射；
- 0 原Q秩、原39-current秩及其核；
- 0 原三尾 current 构造；
- 0 旧人工套件／旧 source certificate；
- 0 第四 forcing 编译或原根恢复；
- 0 旧22维独立性秩目标。

原22维是已付事实。本次新的 self 像和 K＋53 union 像是唯一新线性代数问题；已付11条非K current 是其成员比较目标。程序不另跑一个22列秩。

## 2. 固定已付输入：全部来自原公开 stdout

repository：Rogerhu12/math-research-public。

- run 43796872698；
- job 133067569306；
- source commit 563defb46bc785295265c3f48fcad3fc8897c617；
- 原 stdout 1,322,512 B；
- 原 stdout SHA256：1edd4dd8ac34e2a9fe6fc1cf7ae08dc2d91fa279c02e6c32365bff9830e013b1；
- 1020 个 CURRENT_Q_RECORD；
- 原完整记录 JSONL：1,170,464 B；
- JSONL SHA256：dd936dc713d3461cfbf2652c4e88c89ac4b918eb7949bb379f3b940d62cb8ec7；
- 记录身份链：673061557c1b53e78bf300d18e11e510d091378ad3431e159f6049404cde5101；
- 原完整 final report：15,639 B；
- final SHA256：c4b4031bddacca0c84050c7efdf8b43f80e7553553305d55dd52637f96af292d。

原请求准确路径是：

computations/request-complete-response-self-current.json

按上述 source commit 读取，原请求9,269 B，SHA256
fd6e8526d6f7e9492911848b17a852d64a31654513a267ba61e5bdb9390ffb01。

消费的三个数学记录种类：

- 18 条 science.original_operator：label、完整 a,b,c 的局部有理系数表；
- 85 条 science.complete_kernel_current_column：原 kernel_index、original_combination，以及已完成Q零／三个原矩标志；
- science.current_image_elimination_step 中 kind=dependent 的53条：kernel_column_combination。

53条关系的索引属于85列，**不属于144标签**。新源码先按原顺序将每条关系通过85列 original_combination 展开到原144标签，然后才进入新的 self 算法。每个新 current 输出同时含原 dependent 记录 sequence/SHA、85列组合和完整144组合，保证53→85→144可直接复核。

只检查日志／请求／记录身份、原执行成功状态、索引／字段和完成标志，不重新检查旧Q坐标为零或旧current关系为零。那已经是原报告的精确结果。

原完整日志只存在内存。新 Actions 从 GET run、GET job 确认 source/status/conclusion，再读一次原 job logs。302至签名 HTTPS 时完全移除 Authorization；不打印签名 URL或token。原读取上限8 MiB，实际身份须精确吻合。原日志／JSONL／payload不提交、不制 artifact、不转存blob。

## 3. 新 self mapper：完整原锚，因子是2而不是1/2

记 u,p=u′,r=u″,t=u‴；I=-J，I在原共同右端取零。

原第三核系数满足
$$
\mathscr A_\tau=D^2(a_\tau D^2)+D(b_\tau D)+c_\tau,\qquad
h_\tau=(a_\tau r)'+b_\tau p,\qquad h_\tau'=-c_\tau u.
$$

原 E8 完整二次输出 q_E=Phi_E(u,u) 直接使用 R434 已冻结的 quadratic_operators 纯构造接口。它保 P、S、J2 的真实右锚和全部左二次尾：

$$
P=J(r^2),\quad S=J(xr^2),\quad J_2=J(x^2r^2+2p^2).
$$

绝不把某个单包 q_E 当左紧。也绝不把旧 Q 列的 whole_word_rows／left_word_rows 或 integral-density 输出当成新的 I(cq_E)。

对于一个新的53关系，先在原 expression ring中组装

$$
C_{\rm int}=\sum_{E,\tau}\lambda_{E,\tau}c_\tau q_E,
$$
$$
P_{\rm cur}=\sum_{E,\tau}\lambda_{E,\tau}
\{a_\tau(pq_E''-rq_E')+q_Eh_\tau\},
$$
$$
\boxed{F=2\{P_{\rm cur}+uI(C_{\rm int})\}.}
$$

这正是 self=2K_\tau(q_E) 的完整 partial。R434 的三尾表使用 K/4；本稿没有复用其缩放。

对应第二导表达式保为

$$
S''=2\sum_{E,\tau}\lambda_{E,\tau}
\{(a_\tau q_E'')'+b_\tau q_E'\}+2I(C_{\rm int}).
$$

原恒等 F′=pS″ 来自上式及 h′=-cu。左平端 u=p=r=0，因此 F的积分常数确为零；q_E及I(cq_E)可以有非零左尾，也不改变这个真实常数。每个新的完整 current 另用 fresh mapper 检查这条新 source derivative 恒等；这不是旧Q、三尾或18算子的重新科学检查。

输出保完整 Af之前的 right-word rows；原自伴三重右恢复常数没有重新选取。

## 4. 同锚 word 约化的准确逻辑

重用原七个已绑定模块中的纯代数接口：

- 原 ColoredRing、Expr 的精确有理微分与单右锚积分；
- R178固定颜色优先的同锚分部积分；
- 原全深度 shuffle；
- 原有理稀疏列消元和持续进度记录类。

**不调用**旧 original_operators、map_Q、current_record、development、science 或 main。

新 mapper 的 profile weight 上限为5，而旧Q/current入口的4不适用于本题。所有新／fresh mapper共用primitive调用和cache累计上限。

每一步 IBP/shuffle 都是同一个零右 collar 上的原函数恒等。多字、内层 primitive、三角对角局部项均保。不会用左右锚交换、删常平台或只取principal。

但是：R178 的 sound word representative 不在这里被冒称任意非局部函数的独立坐标。**只要 Af后仍有非局部字，就完整输出并将全像结论保留为 unresolved。** 不对这些字做“非零所以新函数非零／不属于旧空间”的判断。

## 5. Af只作用外部jet；忠实性何时成立

先完成整个 F的同锚 word约化，然后在每一项的**外部**局部系数使用
$$
t=\frac{r^2}{3p}.
$$

- 原 integral letter内部的t、u4等完全不变；
- 不对 Af=0微分；
- 不置u4、u5为任何函数；
- 不把不同 actual packet的原 primitive替换成共同局部常数；
- 允许保留精确 p的负整数幂，绝不把分母截掉；
- 所有 surviving nonlocal、高外jet或Laurent项完整列出。

新结果行格式为

[显式x次,u次,p次,r次,未替换的外高jet表,原内word,精确有理系数]。

每个 current 的总profile次数应为5；这个结构在包括全部内word时检查。

R431真实简单p零与简单Af零保证在本题的Af根上p不为0。因而p的负次幂是这一原根域上的精确表达，不是奇点被抹掉。若只剩局部三阶以下项，则Af之后就是x,u,p,r的有限Laurent polynomial。

这个局部情形的字面系数是忠实的：在p≠0的开jet域，x,u,p,r可自由指定，以t=r²/(3p)取Af=0，再独立选u4使Af′≠0，并由紧支撑光滑jet实现。一个有限Laurent polynomial在该开域恒零当且仅当其完整系数为零。故该矩阵的rank是这些 universal formal Af-current函数的真实线性维数，不只是表示上界。

这不授R431已经冻结的有限母库在这些 formal方向上满秩。固定q约束／共同cap／真实中心／宽度可以使其实际评价降秩。

如果有非局部或高外jet残余，本入口仍完成并打印53份准确映射，但**不执行／不宣全self函数像秩**，退出为 unresolved structural interface。高jet也不因为是“低阶余项”而删除。高jet局部性可能另有忠实理论，但本次不自动扩展已评审的根域接口。

## 6. 唯一新像及与已付22维的比较

只有53个current都通过第5节完整局部接口，才做新科学消元。

### 6.1 新53像

将所有局部Laurent单项式统一编号。精确有理消元输出：

- 新 self 像维数及basis的53列索引；
- 新 self 核关系；
- 每个pivot／依赖的完整原144系数；
- 每个normalized basis的全部current坐标。

这里不用旧Q/current秩推self秩。

### 6.2 加入原K轨道

R435已发表完整生成式
$$
w=1-zx,\quad A_z=w^2r+2zwp+2z^2u,
$$
$$
F_z=\frac{A_z^3}{15}\left(4A_z^2-10z^2uA_z-\frac{20}{3}w^4r^2\right).
$$

程序只把这份准确多项式身份取z系数并乘n!，作为11个已付输入current。不编译它们的forcing，不重证旧轨道或旧11维秩。

接着计算一个新的 union像：

span(K0…K10,new 53 self currents)。

该union消元输出同时保K轨道系数与新53→原144系数。它不是把K假装属于原144模块。

### 6.3 原另外11条的精确成员比较

R436/R438的P/S七条、R440的Xi0/1/2、R441的ur4共11条，直接使用已发表完整local表作为新53像的比较目标。每个MEMBER给原53及144证书；非MEMBER在这里标为 source-comparison unresolved，不贸然撤回旧原式或将其解释成数学新障碍。

已付22维独立性不重跑。只有：

1. 53 current全部真实局部化；
2. 11条比较目标全部属于新53像，证书完整；
3. 新union恰为22维；

同时成立，才能宣本明确augmented模块没有第23个formal current。随后R441的16镜对像／6blind可在相同原对应组上继续消费，但不新增实际点或实际秩。

如果union大于22，报告准确差维、完整新basis和cost证书，不先说镜对实际秩增加，也不将未知actual目标置为local current。

任何这些结论都不扩大全R、原Z之外其它第三类、固定库偶然更大的C核，或全部四阶period问题。

## 7. 两个且仅两个新的 adapter checks

首次公开Actions先执行两条新开发检查，不运行旧driver的development：

1. invented quadratic self Green。取a=0、b=xu²、c=-up-2xp²-xur及w=J(u²)+xup，检查新self current与完整second source的导数一致。此处w有真正原primitive，检测self因子2和同锚组合。
2. Af外jet保护。制造含外A·I(u²)、外pt·I(r²)、内I(t²)及外u4的五次表达式；准确检查外A消去、外pt代入、**内t不代、外高jet不删**。期望表达式是独立列出的精确字表。

两条均为新adapter所必需，不是旧18/144/85/53题目的再测试。没有本地执行，包括py_compile也没有运行。

## 8. 有限费用与真实失败记录

冻结上限：

- 新science 180秒，development20秒；
- memory 1024MiB；
- nodes500000，atoms60000，terms80000；
- 同阶段所有新／fresh mapper总primitive调用500000、总cache300000；
- 有理数8192bits，受监控有理运算5000000；
- 数学stdout2500000B，独立预留final131072B；
- 原日志读取8MiB；API JSON每次2MiB。

这些是停止上限，不是实际耗时预测；不能把未运行数写成成本。旧报告的原成本只作输入来源，不从本次收费中减造数字。

复用的 PhaseProgress会保started/interrupted stage、已完成单元、真实time/RSS、rational及shared mapper计数。发生结构、stdout、预算或Python错误时，所有已完成数学记录仍在原stdout；不以零成本替换失败阶段。一个已完成记录若超stdout余量，完整保在runner临时JSONL并记bytes/hash，立刻停止后续研究，报告finite failure。

新完整机器结果只在原公开stdout及runner临时文件，不提交、不上传artifact、不做Release、不存结果blob。代码、设计、参数、回执metadata及后续人类证明可由root按原规则发布。

## 9. 新记录协议与root接入

新记录：
SELF_KERNEL_RECORD {sequence,kind,payload_bytes,payload_sha256,payload}

最终：
COMPLETE_SELF_KERNEL_REPORT
SELF_KERNEL_REPORT_IDENTITY

请求的schema、entry_point、domain、limits、paid_input须逐字取源码常量。source_manifest恰含：

- 旧driver与六个冻结代数依赖，共七项；
- 本新driver；
- 本设计；
- 新workflow；
- 原规则reader。

合计十一项。每项bind bytes/SHA；请求另给同一source_sha256映射。旧七项的hash在源码固定，不允许当前checkout静默替换成新版算法。

root的workflow仍在任何新adapter／science前完成原实际public/private pull、双README／私有队列规则读取与准确diff；保持同一sourcecommit的reviewed源绑定。入口有GITHUB_ACTIONS及repository闸，不接受本地执行。

GITHUB_TOKEN只需contents:read、actions:read。新入口自身无git写、无push、无dispatch、无artifact上传。workflow不得额外加入旧测试或重新生成R434数据。

当前交付是未执行的源码／设计。R443结果必须等唯一公开实际完成后，再由root及代理读取原stdout与全部新证书撰写；本设计没有预设新self维数、locality或旧六blind是否完整。
