# Request175：完整 Hermite 查询路径的闭步长域包围接口

本文件规定独立的公开 Actions 实验。它从真实 actual98 原父包重建一次原37查询模型与真实新 warm 的原FD，然后执行新的准确有限参考诊断。它不等待 actual170，不使用170的数值结果，不把原37/FD的结论改成区间消费者的结论。当前只是完整源码和接线；没有本地科学执行、未来run、接受场或完成时间预测。实际结论编号预留R372。

## 1. 原来源、所选范围和公开基础

父包仍是实际 run43677587785 的 artifact14147700690，原名 visible-followup-condensedqp-43677587785-1，809042943B，完整ZIP SHA256：

9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a

实际父warm为 warm-001.json.gz，4927052B，SHA b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67；父driver-status.json为3379453B，SHA b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。恢复按原临时运输器验证完整包与所选原字节，不从后来被删除的warm hash伪造继续现场。

原 public-thirty-seven-model-recipe.json 保持 f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea。原37查询为21个LEFT和16个MID，实际24个单元、29个端点node463…491；没有新增或删除query。完整A、AT、B、外部变量、core与parameter支持以及原域/merit门均由原冻结模型执行。

已发表的数学基础：

- R354：results/R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md，20501B，SHA b6e293c20ffb6584f316b3e38877b7e3d4fb61cbad1f008718ab034f605cb183。
- 175设计：notes/2026-11-15-request175-complete-Hermite-query-domain-design.md，14877B，SHA b3094ad14bf332cfb6e891faf1d45eb4774075fe9cea7958788cc2f1474286a2，发布 a12b293129e877c6296728e303bef69dacb06997。该正式设计已经明确选择actual98独立父。
- 170实际发布基线 bf1880f8c2e0381223bf29fd50ffb6e205afc75b，仅复用其源码，不复用数值。端点消费者必须是75046B / 84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a；其t投影使用与原real_project一致的正sin。负sin审稿99ef不参与。

所称“准确参考”始终是给定全部finite字面系数、真正均匀角和明确四则/平方根式的准确实对象。它不等于原FFT或profile程序的IEEE执行顺序，也不自动成为另一个连续标量provider的导数证书。

## 2. 三个新运行源及完整冻结清单

| 文件 | UTF-8字节数 | SHA256 | 小文本blob |
|---|---:|---|---|
| geometry_20261115_R354_thirty_seven_query_scalar_capture.py | 26648 | `0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90` | `6e00e8acb38f2cdaa71598ab912a12be1ebf34fb` |
| exact_20261115_R354_thirty_seven_closed_query_domain.py | 36928 | `cf4fa7b33bfcc13cd68193c3abc9b2da8edae4b90e64c16bcfbcce863a095d89` | `d207ec0f4586cf3ec4984a6f4071a933901b1976` |
| geometry_20261115_R354_thirty_seven_closed_query_same_job.py | 36809 | `825caec6efc3fa7fca5daf9d70a9bed907bb0fe91b3fb39858b9d0da3a66d516` | `9ef807e550b65fb6cd31fef03863eeba37b661e4` |
| public-thirty-seven-R354-closed-query-domain-request.json | 35920 | `a6b9cf0aadb43d89ac072cb2c650a8b125005aabf99322434c108a6983b85419` | `13e627966ee5ac3deee9d65ec0314a77cec0e1b3` |
| visible-larger-public-thirty-seven-R354-closed-query-domain.yml | 10463 | `0fb881b1e2f753c788d2a7854361ccba183b1fbc4b53b9ecc48dd8a9828dd265` | `28720faad25b98db7cce5fc3ecf902dca4addcc7` |

本接口文件独立提供最终身份。表内源字节均保留在小文本对象中；root独占公开分支发布。原科学构造差异可从前后源重建：最初三源/生成模块完整差异blob4696c0532767610093abaa9eeb685841e53580b8仅作为已读版本的来源。此次随后仅改samejob元数据选择/单份读回及依赖pins；capture0a8f4920、consumercf4fa7b3和私有84af生成模块逐字不变。最终完整纯传输diff另交root，无需把可重建diff当新科学数据入仓。

源闭包是170原100个逐basename/SHA保留，再加175三源，共103。原90数学/模型依赖、原37worker、158/166/170来源均不被改写；旧170 runtime和capture仅作来源，新的runtime与capture承担本次执行。三个原参数文件仍逐字不变：source-dependencies.json、public-thirty-seven-model-recipe.json、public-thirty-five-model-recipe.json。R354与正式175设计另外逐原字节核，不伪计为新的科学模块。

## 3. 原模型、FD与资源参数保持

原模型的一次执行参数：

~~~
--iterations 1 --damping 270 --lsmr-iterations 200
--projection-sweeps 200 --line-search-steps 17
--budget-seconds 1200 --angles 4096 --jac-workers 2
--condensed-budget-seconds 600
--condensed-trial-reserve-seconds 90
--condensed-recovery-reserve-seconds 30
--condensed-max-working 512 --condensed-dual-sweeps 200
--condensed-store-root
~~~

FD仍针对这一原模型真正产生的新warm，沿原交接允许范围运行原4096角FD；没有把actual98旧FD换标签。原模型/FD尝试及其完整原文件、全部访问试步和拒因先在Actions内保存，再启动175诊断；末端有界摘要统一返回原必要标量与拒因。诊断缺项、未决、预算截止或程序异常不回写原模型/FD判定。

全部scientific执行仍由原3b8 rules runner每2700秒真实pull/rebase/规则变化stop控制。根README固定21bd547f56590b7f2dd279d0297efb289a9b2783、课题README固定bff8aea253a9e6a7a4fac28d810ac454c5499fec；startup按实际读回字节建立BASELINES，保唯一规则同步行，不伪称pull发生。科学checkout固定触发source；规则镜像与科学源分开。

全局10800秒从原恢复、运输、78源、fullJ/QR/model/FD之前开始。预留300秒给读回清理，消费者额外预留60秒收尾；实际消费者上限为5400秒与当时真实剩余量的较小值。单科学step190分钟、job215分钟、always读回15分钟。临时未压缩ledger总上限8589934592B。所有原时间上限仍存在，新增诊断不侵占原求解接受语义。并未测量175成本，也不保证在本预算内走完所有端点、角点或37×17域。

运行环境仍Python3.12.14、numpy2.3.5、scipy1.17.0、python-flint0.8.0；原科学线程配置保持。非三角区间用自己的320bit整数网格向外算术；真正角表用Arb384的准确有理倍pi，随后向外落到320bit网格。

## 4. 查询标量缓存的真实观察位置

capture在原angular_values已经返回后，读取该次原scalar_jets实际刚使用的 singleton station缓存：

~~~
key = np.array([station]).tobytes(order="C")
baseline, controls = flow._base_cache[key]
~~~

它不再调用profile、base_jet、control_jets、scalar_jets、RHS、J或角查询。复制完整stations[1]、baseline[1,3]、controls[1,3,3]；绑定原AugmentedFlow.scalar_jets文件SHA、station完整字节（包括负零）、原angular return index、context和query453原word。原已经返回的rounded scalar[3]继续独立保留。

所有原domain-build和trial-selected返回都保留，包括重复站点/observer额外调用。每个base-domain query通过原实际index、stationword、完整queryword与自己的缓存配对，不能仅按四舍五入坐标或总call数匹配。原B report中的explicit scalar_control_jets身份与它自己的完整实际call配对仍沿166；如果它与singleton cache的controls word不同，只输出byte-equality=false，不强制替换，也不新增原模型门。

三字段记作(a,nu,mu)，这里只按原字面槽位命名。a与nu用于域判据，mu仍完整保存；不把nu或mu自动解释成另一个准确空间导数。准确参考使用b+C*p；不能从原rounded scalar反解b。参数三行全保，所有115个常量RHS行全保，因而新的标量参考沿步长次数至多1。

原capture safe记录异常的方式不改：记录缺字段会导致独立诊断明确绑定失败，原模型函数仍返回其真实原对象。观察器不会因读取缓存失败而伪造模型拒绝或成功。

## 5. 固定84af的13个显式唯一替换

新consumer不是复制并偷偷修改旧数值正文。它先核公开84af文件完整75046B/SHA，再在内存生成私有module。每个替换都在SOURCE_REPLACEMENTS中给出完整old/new和required count=1，实际逐项count核同后才形成：

1. 独立说明行。
2. 独立result schema。
3. 新capture schema。
4. 新capture basename。
5. 新capture SHA。
6. result请求号175。
7. 初始化query_domain_175与完整源适配receipt。
8. 在原端点/原pointwise Hermite工作全部返回之后接新的query extension。
9. finally加入完整新范围收尾。
10. result中的准确query域flag使用实际新结果。
11. summary请求号175。
12. summary加入实际新域flag和小摘要。
13. 由有界summary传输函数保存完整JSON并打印固定上限事件。

生成module为75461B / 1ee36bde82ec5c7e235bfeaab0567d22e6cc09b8f2702e03963c61f3c058017f。原def require起到def main之前的完整数值函数区域逐字相同，区域SHA 78fe50b3977092a0022d6cd586ef9fd76c4530ba46b14de4bd981f80de873e22。这是纯字符串/字节比对，未执行这些函数。

公开84af文件不写回，私有module仅在Actions内compile/exec。__file__明确指本次新producer，traceback filename明确标_generated175；result保存原源、新源、生成源、正式设计、每个old/new字节SHA和实际次数。全部literal-J/P动作、原q1形成、准确全338投影、两mean、闭段M和旧pointwise eta函数正文不变。

## 6. 从准确端点到完整453闭段family

对每个真实query，左右端点仍按它实际原A调用的J/P/b/C字节绑定。相同node出现在不同chunk且字节不同，保为不同变体；只有全身份字节相同才复用工作，同时保每个call origin。没有用Bz反造任何原输入。

用原已保存字面h、Hermite权重、q0/q1和准确形成差，记左/右端点准确参考误差的初值/方向值为e0/e1。对每个闭段[0,A]，原R354给出完整端点M，必须该端点所有2048角的严格域和二阶界都已实际形成，才允许使用。

令wL、wR分别为h10、h11，保留wR真实负号。定义完整453向量：

$$
G_0=\delta_0+h(w_L e_{0,L}+w_R e_{0,R}),\qquad
G_1=\delta_1+h(w_L e_{1,L}+w_R e_{1,R}).
$$

M是原完整RHS输出分量的统一上界经真实有限投影行和形成的界：两个mean行0、225用M，其他336个物理行用2M，所有115个常量RHS行用0。新consumer将

$$
\gamma\ \ge\ \frac{|h|}{2}
\bigl(|w_L|M_L+|w_R|M_R\bigr)
$$

用原320bit向外算术实际包围；G2的mean盒是[-gamma,gamma]，其他物理行是[-2gamma,2gamma]，常量行精确0。程序用带符号完整区间积形成共同gamma，没有假定wR正。

对闭段内每个t，准确query误差被下式系数family包含：

$$
Y_H^\ast(t)-(q_0+tq_1)\in G_0+tG_1+t^2G_2.
$$

这是逐点余项family，实际余项系数可随t改变；绝不宣称准确query是一条固定二次多项式，也不对这个可变family冒做微分。定义H0=q0+G0、H1=q1+G1；H2=G2。每个真实query的准确参数路径仍仿射，因为三参数RHS为零。

消费者先对全部37×17组准备完整453维family、闭段gap和path包围，再开始query角域。每行使用完整二次系数的Bernstein与Horner交集；不只保存最大行，不丢constant行或两个mean。完整向量写临时ledger；compact结果保完整计数、两mean、physical/constant最大界和原行号。

若某个端点的准确全投影或全2048闭段M未形成，相关query/step明确不可用；不将缺角贡献当0，不从旧模型范数代入M，也不伪造后续域结论。

## 7. 完整查询角表达与15个P系数

对每个query和真正均匀角theta_n=2*pi*n/2048，n=0…2047，保所有频率0,2,…224及338个物理系数。H0/H1经完整角jet线性映射形成d0/d1、e0/e1。G2的完整投影pattern通过每一角导数行的绝对行和传播；没有只取几个低模或控制列。

z均值在453state/gap完整保留，在角一、二阶导数中严格为0；r均值对d_t、e_r的贡献原样保留。t坐标正sin约定继承最终84af及原FFT，不再使用99ef稿。

d、e的系数family次数至多2。所有三scalar字段通过自己的原singleton b/C与H0/H1的450…452参数行形成，次数至多1。形成：

$$
Q=d\cdot d,\qquad C=d\times e,\qquad W=C\cdot C,\qquad
P=a^2W-\nu^2Q^3.
$$

Q共5系数，W共9系数，P共15系数、最高次数14。源码明确require这些长度，不沿用端点affine路径的9个P系数截断。每一角/每一步的完整P、Q、W和a/nu系数都进入原临时ledger。

当前首个175实验明确只做每一[0,2^-j]的完整粗Bernstein包围，再与Horner包围相交；j=0…16。没有在预算外隐式添加adaptive subdivision、额外角点或额外query。设计允许后继针对真实未决改进，本次如区间过宽就报告未决，不把节点数量增加当已经付过。

## 8. 严格通过、严格反证和未决

每个query/角/闭段的准确域结论只从实际向外包围形成：

- a下界>0、P下界>0、nu整个盒严格位于(-1,1)时，准确参考在整个闭段符合所声明域。
- a上界<=0、P上界<=0，或nu全盒在[1,+inf)或(-inf,-1]内，可以给整个闭段的严格反证。
- 如果整个闭段仍未决，程序另用同一完整多项式在准确闭端点0和A形成点包围。某个端点严格失败可以反证“全闭段均有效”，但明确不声称每个t均失败。
- 仅a/P下界非正、nu盒触边、负Bernstein系数、宽区间或预算截止都只写unresolved。没有把区间依赖当原数学失败。

P>0与真实Q/W平方范数恒等式排除Q=W=0；源码若记录Q/W数值上下界，它们来自完整实际包围，不凭逻辑排除编一个正数。

这些是声明的准确finite参考域。原实际浮点query可能因原scalar/cache/FFT/形成误差与它不同。175保留原170在已访问alpha处的pointwise eta读数，却没有付IEEE程序在整段上的统一执行误差；所以准确query域通过也不能自动宣称原程序全部试步安全，更不能替代原699节点、698 midpoint、RMS或native门。

## 9. 完整范围、原试步和原子提交

全部17档alpha都是准确二幂2^-j。原真实访问/未访问与原是否返回query分开读，不额外调用原试步。准确参考可以为未被原回溯访问的档位计算声明域，但不能给它补写原非线性结果。

新结果query_domain_175保存全部37×17组的：

- typed query、interval、station原word和左右变体；
- 原trial_visited，完整453uniform gap是否实际可用；
- 完整已提交角数，strict/refuted/unresolved分别的全部连续角范围；
- 尚未访问的明确角后缀、缺端点原因；
- 每组全2048域是否成立，原IEEE域仍未获证；
- 每个真实angular return的singleton缓存及原B explicit身份。

同一个角的全部17个可算步骤先组成完整记录，ledger.write成功之后才推进所有计数。如果信号、时间或字节上限在该事务前触发，当前角仍在明确未访问范围内；不会混用半角的15项系数与已支付计数。

全部453gap的ledger事务同样先写后标为available。unresolved/refuted的大逐角系数表只留在RUNNER_TEMP，保压缩/未压缩bytes/SHA、完整行数和实际覆盖范围，不把可重算大表编码或搬入Git。完整原结果保所有失败/未决/未访范围；对外必要摘要保全域计数、每步全部query分类及未访角后缀元数据，长区间见证和逐角科学表留在Actions内部并记整体bytes/SHA。

若前置端点阶段耗尽预算，新query阶段明确未开始，保全37/17/2048范围；不能把query计数0记作已检查全域。

## 10. 结果语义与异常传输

独立诊断仍有自己的exit：0表示新声明准确query全闭段域确实全通过；3表示准确范围不可用、未决或资源部分完成；2表示输入/独立程序错误。原模型或FD非零状态优先保留在外层pipeline，不被诊断exit覆盖。scientific_completed只表示本次所有请求的新计算均已访问，并不等于原程序、native或用户目标接受。

完整result.json始终保独立科学状态和所有原结论。旧170 pointwise Hermite_transfer与新175 uniform family字段分开，不再把前者叫整段gap。

科学consumer的summary-complete.json/result.json及原bounded summary逻辑保持冻结；它们作为子进程日志/临时文件留在同job。新的samejob不调用旧helper.stream_complete_json、stream_bytes或worker.print_batch，不把629个pair的长区间bounds、全scalar-cache words、完整科学trial对象拆包返回。

always readback只形成**一份不超过90000B**的必要ASCII JSON摘要：原模型/FD的原状态、全部已访问17槽中的trial标量/接受/拒因、全部37 selected query原minima/负数与非有限计数；原RMS/中点域保计数、所列失败interval范围及首个原失败点。每trial的完整原选取对象另保canonical bytes/SHA，原大嵌套对象不重新输出。

新准确诊断保全域计数和flags；对17个trial_index分别列全部37 query的proved/refuted/unresolved/unvisited集合与gap_available/pair_not_reached集合。集合只是原metadata整数连续范围，不重算任何不等式。各query的已完成/通过/反证/未决角计数、原未访角后缀和missing-endpoint理由按相同记录分组；即使完全未进入query阶段，也明确17×37未访。旧pointwise transfer的pending按step/query压缩，endpoint参考未访按variant/node/角范围记录。原实际输入binding、全result、ledger和原报告保bytes/SHA；完整interval见证只在Actions内部处理。

原pipeline/capture/diagnostic异常及实际失败日志中的必要原error字段、traceback文字和行位置进入同一摘要。全失败日志本身只记bytes/SHA，不以错误名义搬科学stdout。日志含UTF-8异常字节时原文字经surrogateescape和JSONASCII保存，不对原错误正文静默截尾；必要摘要实际超界则整体报告读回未完。

若必要摘要超过90000B，明确summary_complete=false、transport_complete=false、readback_complete=false、exit70，保原科学exit、原结果与摘要候选身份和未返回范围，**无任何新segment/begin/reassemble绕过上限**。科学consumer可能已完成与读回未完分开。只有实际单摘要打印成功且code=0才写readback-complete.json；读回失败不删除尚未读的临时文件。根8的科学表限制不被解释为新的科学接受门。

完成readback成功才生成readback-complete.json和进入显式cleanup。workflow同时要求实际complete_readback outcome=success；否则保尚未读临时对象到runner销毁并明确未付范围。没有upload-artifact、Release或Git raw输出。

## 11. 直接CLI与触发接线

科学runner由新workflow唯一独立trigger public-thirty-seven-R354-closed-query-domain-request.json触发；concurrency group独立，cancel-in-progress=false，不取消170或其他现场。

~~~
python -u geometry_20261115_R354_thirty_seven_closed_query_same_job.py \
  --repo-root "$GITHUB_WORKSPACE" \
  --request "$VISIBLE_COMPUTATIONS/public-thirty-seven-R354-closed-query-domain-request.json" \
  --work "$RUNNER_TEMP/visible-R354-175"
~~~

原模型结束后，runtime实际调用：

~~~
python -u exact_20261115_R354_thirty_seven_closed_query_domain.py \
  --capture <原model输出>/R354-query-domain-capture \
  --model-directory <原model输出> \
  --code-directory "$VISIBLE_COMPUTATIONS" \
  --seconds <global剩余裁剪且最多5400> \
  --max-ledger-bytes 8589934592 \
  --out "$RUNNER_TEMP/visible-R354-175/post-model-diagnostic"
~~~

读回和清理沿同一runtime的--mode readback / --mode cleanup，后一项必须前者真实成功。工作流逐SHA绑定最终requesta6b9cf0a…与103源/三个原参数，正式设计与R354原字节也核同；没有因旧request摘要SHA而误指审稿。实际runtime source为825caec6…，capture为0a8f4920…，consumer为cf4fa7b3…。

## 12. 已完成的源工作与未付责任

本次已完成完整源码、原基线精确差异、13项字符串替换计数、生成module字节身份、全部103旧新source映射和三个原参数逐键保留。原数值函数区域纯字节相同已核，不能把这种源等价说成本地数学验证。

终端未恢复，所以没有本地Python AST、bash-n、科学import或试跑。公开Actions的正常source syntax步骤解析各Python原文本；私有生成module在真正科学进程内按明确source身份compile。没有新增fixture或等待审批门。

尚未付：任何实际175数值、完成用时、全部准确query通过、全IEEE执行误差、完整网格/RMS/native/fullDN、最终338响应、物理audit以及课题整体目标。即使准确query全部通过，这些仍依原责任继续；若175给出未决，也不能反写原模型/FD为失败。
