# 真正58的full62新范围：原后端成功，严格metric终门失败

日期：2026-11-16。**完整原公开Actions观察与费用闭账。当前实际接受仍为58。**

原64变量SLSQP真实返回status0/success=true，把两网后缀最大曲率降到目标约16.39344262295082；准确原172盒、h区间与实际舍入后范数都通过。但细网最大η为 **0.26600531463999494**，严格预算为 **0.26600531463999305**，原无容差metric终门为false。因此qualified=false，0完整body预测、0原actualpair、0新接受；不能用backend成功、极小误差或PSD容差代替这个原门。未修返回向量、h或阈值。

本范围就此关闭，未用余额不延长或重启。下一问题同时处理完整body的前缀与后缀，并明确内部严格余量；这不是把本失败点追认成59。主课题的全域全时metric/reach/嵌入/幅度门仍未满足。

## 1. 固定源与完整原返回

- [公开run43916013327](https://github.com/Rogerhu12/math-research-public/actions/runs/43916013327)；
- research job133470222034，report job133471963940；二者完成success只表示程序完成，不代替数学接受；
- source868f2f6b5ba55affa26cc5f9d42186a565ea0a43；
- workflow .github/workflows/visible-true58-full62-whole-suffix.yml；
- 原[设计](true58-full62-whole-suffix-design-20261116.md)与[模型合同](true58-full62-whole-suffix-model-contract-20261116.md)；
- request85793B，SHA256 a6ba3811d6acd125d24018be293aa4bc9614502ef569f00c2d105a5d2f9a19b2；
- 382源逐项绑定，原370源未改；
- model binding728b1a01ccf8a6d0c877ea28faee4ff766d1a29543d8182edff7d16a9db3964a。

原51加尾高度2和完整body9，共62实际方向，K/h加至64变量；63非零物理行、474线性与145152非线性行。q153…156后缀零列固定。唯一初点true58；原g/b0/reference/盒/14门不改，九个物理高度通过独立一次RN后原exact affine map恢复，不独立舍入物理高度。

| 原返回字段 | 原值 |
|---|---:|
| status / success | 0 / true |
| message | Optimization terminated successfully |
| nit / nfev / njev | 54 / 70 / 52 |
| raw K | 16.393442622950822 |
| raw h | 26.075975493509613 |
| backend elapsed seconds | 64.95742960299998 |
| solver local elapsed seconds | 65.794852703 |
| solver ledger elapsed seconds | 65.87506455599998 |
| solver clock limit | 1200 |
| observed solver overrun | 0 |

原OptimizeResult的实际全部字段fun/jac/message/multipliers/nfev/nit/njev/status/success/x先输出于NONLINEAR_RESULT，再筛候选。multipliers只是原QP近似返回，不是严格证书。

原raw64数组512B，SHA256
b75bb28df605af2a9cac0f897dbbc94732e550a799d319ba6747d1ffb67c7b24。
一次舍入后q168数组1344B，SHA256
ba19a49d79be1f0f40c172491a875cc967a78df0688e50149b61d139ab39b810。
原准确物理172身份
655df422a291f4cdfa8bb2caa83431122e090c16a94d36cb32d094bb6a35f929。

完整raw64、其binary64准确分数、实际q168和准确physical172留在原stdout，不以Git保存科学向量。它们是实际失败返回，区别于旧full51无返回的最后callback。

## 2. 准确盒、范数和原线性门

原返回：
K=2307171940251279/140737488355328，
h=7339734594743255/281474976710656。

未舍入准确物理范数为
7339663963397351/281474976710656；
h减此范数为
4414459119/17592186044416>0。

独立一次RN后实际physical172的准确范数为
29358655853589405/1125899906842624；
原h减此范数为
282525383615/1125899906842624>0。

两层准确原172盒均通过，违反索引均为空；K/h准确区间、原显式hmax、
实际rounded norm≤raw h全通过。原未缩放线性最大违反量为0，原线性容差1e−9不变。
本次失败**不是**原盒或范数失败。源码总状态字符串同时覆盖“suffix或box失败”，具体原因必须读原细门，不能单凭字符串归因。

原最大scaled residual为1.942890293094024e−15，低于solver模型容差1e−9。
这不改变下一节无容差的直接metric预算判定。

## 3. 两网完整21行的原终门

| 量 | coarse384 | fine768 |
|---|---:|---:|
| 最大η | 0.2660052737794828 | 0.26600531463999494 |
| 严格η预算 | 0.26600531463999305 | 0.26600531463999305 |
| η门 | true | **false** |
| 最大绝对主曲率 | 16.393442622950843 | 16.393442622950815 |
| 当前K直接曲率门 | true | true |
| 原hard58曲率门 | true | true |
| 原四条未平方PSD门 | true | true |
| 最小normal area | 0.8584841942926644 | 0.8584552554802735 |
| 原面积门 | true | true |
| 全后缀联合门 | true | **false** |

原PSD最小值按原次序保持：

| PSD行 | coarse | fine |
|---|---:|---:|
| minus determinant | −2.200455470736504e−17 | 2.0046522296963912e−17 |
| minus trace | 0.11100515031521767 | 0.11100707700652959 |
| plus determinant | 0.000005345312505798905 | 5.668970026304214e−17 |
| plus trace | 0.11721606597951147 | 0.11721506737567042 |

这些PSD true 使用原PSD门定义，不能把它的容差移借到metric严格门。

coarse η峰在径向139、s=.765、θ5.8904862254808625（角360）；
fine η峰在径向143、s=.795、θ4.655120364303626（角569）。
coarse曲率峰在径向143、s=.795、θ3.8124535848251138（角233）、principal1；
fine曲率峰在径向144、s=.8025、θ4.818744981678094（角589）、principal1。

全部值是声明的q_R scalar增量后缀模型，其浮点结合顺序不等同canonical完整body。
后缀只覆盖21径向行，未查询其余body的新当前几何，也不能从此推断全body最大η。
本次资格false，所以按照原协议完全没有执行canonical预测或原14门actual。
把η辅助量当δhold、有限后缀当连续reach或把K到目标当主课题完成，均不成立。

## 4. 初始真58及J可用性的准确边界

原初始z0/K58/h0实际后缀门均true，scaled violation0。
初始η coarse/fine为.265998600016377/.2659994610038927；
初始最大曲率57.998792638483124/57.9997782607126。
这些是该增量模型确实新付的必要初值，不由全body峰位置推测，也不重跑旧ordinary基准。

初始J已实际形成，shape145626×64、74560512B，
SHA256 5828e31671639bb66c1623d9cb1499550c2b89c7a57c760d1f3ffefd6cc4043e。
最后完整J为第52次，关联**value69**：
backend64 binding142021901a0fb090493b71fdbb38e1bd08fa23e4952a873f918d5e31ae4844f5，
matrix SHA256 98d69b823f46bd8baa181eb7cf5fa3e2223887621d0736380e12163e54abfd2c。

原返回的筛选值是**value70**。未为报告在原返回处增算J；
因此不能把第69点的末J移配成第70点导数。两张大J及大派生几何只输出
真实已算的binding/完成范围/成本，**没有数组正文，不是后继免费输入**。
原q168/172小返回正文则完整存在。未填的partial内存没有hash或伪补值。

## 5. 全部新费用、计次及余额关闭

最终权威FINAL_CLOCK在COMPLETE写完并flush后取得：

| 项目 | 原最终值 |
|---|---:|
| 本次新科研秒 | 115.53521002299999 |
| 原祖先已闭秒 | 3642.4396103470003 |
| 累计科研秒 | **3757.97482037** |
| 原full值累计 | **147** |
| 新ordinary actual值 | 0 |
| 新完整后缀几何点 | 70 |
| 新完整J | 52 |
| K无关导数输入块 | 1248 |
| 新model / prepare / solver | 1 / 1 / 1 |
| 完整body预测 / 原actualpair / 新接受 | 0 / 0 / 0 |
| scope exhausted / overrun | false / 0 |
| 关闭的未用秒 | 1684.464789977 |
| 原进程秒 | 115.53528307099998 |

阶段采样只作分解，不与权威新钟相加：
原五日志读取33.60436152秒，运行时导入1.2302737449999768秒，
model本地.10540124999999989秒，solver ledger65.87506455599998秒。
此外原输入恢复、准确映射/序列化/所有输出等均包含在同一个最终115.53521002299999秒内。

不同literal backend64为70，callback访问299、重复229。
value started/completed70/70、failed0、cache hits55；
geometry started/completed70/70、failed0、cache hits52、paid seed hits0；
J started/completed52/52、failed0、cache hits1；
导数block started/completed1248/1248、failed0、cache hits0。
本次淘汰后真实重算均为0。

callback计数分别为objective70、objective_J52、
constraint_value71、constraint_J52、initial_value1、initial_J1、
iteration52、requested_analytic_J52、returned_vector1。
原backend的nit54保其原值，不用callback52代替它。

各新组件的实际执行包括140次current-K PSD组装/读取、70次实际高度输入、
1248次K相关PSD J组装、420次完整θ primitive、140次direct curvature、
832次完整角J kernel、416次高度J输入、832次virtual位置J输入、
140次scalar增量、140次frame、140次位置二jets。
新固定metric rows和未保存的paid-seed I/II各2次，均已入钟。
其它完整组件原表保于BODY_SOLUTION/SOLVE_TRACE，没有为写本note新增科学。

缓存只在当前进程RAM：0磁盘write/read/bytes/IOseconds，清理完成；
淘汰final J52、geometry69、physical derivative blocks1248。
峰RSS1295888KiB；COMPLETE前科学stdout2973344B。
没有artifact、Release、Git payload或跨run缓存。

## 6. 原stdout、全部当前记录与只读报告

原research完整job log为3395530B，SHA256
c436813e829af5c1c2c7f636d69a199eba4f071395a728abd82995c1f34c251f。

下表均为原JSON+LF身份；记录正文保在原Actions输出。

| 当前tag | bytes | SHA256 |
|---|---:|---|
| PUBLIC_PULL | 2718 | ee00a097a5f413e668de0485047b065a09d16b8842731725af05aa8b459ea4e4 |
| PRIVATE_PULL | 584 | 8ce7b4aa5f2163df10ad8fbf5adff06e83e6c6173f561c5843289ec56ecb1e57 |
| REQUEST | 6726 | a42c6912784a3cab296a1a3d53250bfe9dac5037ae460fd49c082781394cdd0d |
| INPUT | 229677 | 8b7d01fac1e5eddf2b5cf40262d3d0f9a3b0bafb59e27cb69cd33ddf19d26525 |
| MODEL | 190056 | bf5e98f9692ee1f1d6f19c20a13533a1dedbf4ff1ebbdadbb3e42e3dd8ce2935 |
| NONLINEAR_RESULT | 1175909 | 645cf1177c6df7907e58b2247098b153256cdf21c853beb3b6495c87a280898d |
| SOLVE_TRACE | 1267330 | 45b78019734dd47d8e9567a7187364474b2bd437b2f30a0ec6da7a1be6e772a6 |
| BODY_SOLUTION | 103421 | 7d824a6b892ad75c69c45c890240e0cd8acadc869e6d40b5a01a8b519626d17b |
| COMPLETE | 277795 | f5fd3c226627321f9676688d65ca526d3c3e61ab9cf2a1299bdbcdc5318ea865 |
| FINAL_CLOCK | 6684 | 423abbc12eecb6c900e797a58a7d016fa9782e85d31f39cf93620f56b08b06cf |

十条记录全部取得，唯一tag均一次；原OptimizeResult与失败返回在内。
这些是原输出的读取/身份，不是数值复算。

report job原log2455700B，
SHA256 d7e0ec617f701eb75c24f8d4ae8287d279684d5593ca183737be7d44154db83c。
READ_ONLY_REPORT为2326171B，
SHA256 eb0bc8f36edbd86ed2a3275dfdd232324dc98eff4fd255430af069dc16e1a999。
observer耗时3.2548800900000003秒，与所有科研账分列。

报告semantic_read_is_incomplete=false；
必需记录缺失、当前producer缺失收据、parse errors均为空；
source/run身份均match，所有7处当前producer收据都有相应正文。
完整原返回被保留，大科学数组只绑定的边界也明确保留。
不能因报告success而撤去原fine metric false。

## 7. 四次真实pull与逐次README核对

| job/仓 | 实际pull开始→结束UTC | 读过main SHA |
|---|---|---|
| research/public | 17:13:39.352312→17:13:41.913299 | 665dd92b8703fa7118d90fbee0eba7f07e2d60ee |
| research/private | 17:13:44.739714→17:13:45.400564 | 2fd824fd658df7255505eea1498698f918d46b4a |
| report/public | 17:16:03.475263→17:16:04.536661 | 25265e7eaca1b00a879311032a8520546516416c |
| report/private | 17:16:07.517829→17:16:08.318992 | 5f99e48d3c18028b006b07e3394a9f586f753c2a |

两次public为真实git pull --rebase，rc0、passed=true；
每次根及本题README均空diff，读后身份：
根blob21bd547f56590b7f2dd279d0297efb289a9b2783，
题blobd0432faff569c8e9af7ed4809847e12880976c11；
根SHA256 6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9，
题SHA256 e685cff0e67e6851a7911d4e9efbae0e7d326e093927af177f716f059b8c566b。

private只发表同步元数据：每次真实pull，根blob
5ba164843b1f5802184178a82d786264404873a3未变，本题README不存在；
QUEUE会话Astra-new-mechanism-9974ea84唯一进行中。私有正文未输出，MR_TOKEN在科学/报告子进程前已移除。

H以最新17:16:04/17:16:08记录下一次真实pull不晚于18:16:04/18:16:08。
本地执行环境仍不可用，源码/本note用根8小UTF8 API非force发布；它不冒真实pull/rebase。

## 8. 已闭观察与下一实际问题

本次已经回答：原11个新增高度/body方向可以使后端在同一原盒里返回达到曲率目标的点，
而本次原返回未过严格fine metric门。没有得到其全body值或连续证书，
也没有证明该62维集合不可行、驻点严格最优或全局无解。

下一任务将原106个前缀/其它方向与这62个后缀方向放在同一完整168场中，
研究原全body约束和整个后缀的联合修复，并在内部模型明确留严格余量，
原接受标准不松动。这个新问题不得重用本次只有binding的J/geometry；
任何新全body值、原requested导数或实际候选都须在新公开scope内实付。
本次原失败向量可作为明确标识的已知未接受数据，不是被接受58或新59。

原完整主门、固定g/H、全时C²嵌入、δhold和全域reach依旧有效。
完成这个数值子问题的记录不结束主课题；继续open。
