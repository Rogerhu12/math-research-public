# Request174：固定全站 odd 组合的独立十坐标实际试探

作者：OpenAI ChatGPT（amplitude 协作代理）。日期：2026-11-15。

## 1. 实验对象与准确范围

本请求依据[R351](../results/R351-literal-seven-state-adjoint-and-C2-control-response.md)、[R363](../results/R363-local-C2-shapes-and-complete-finite-sample-response-rank.md)、[R366](../results/R366-coincident-inputs-complete-value-and-slope-shape-response.md)和[R370](../results/R370-disjoint-local-shape-box-descent-and-uniform-C2-bounds.md)，从actual157的真实九个Decimal50末参数重建原有限字面模型。它不等待164的新候选，不继承任何164状态，也不使用已经删除的旧raw。

这次只做一个新的方向实验：在全部允许站形成局部odd目录，按实际形成分数确定一次系数，冻结为一个完整分片函数，然后在真正独立的十坐标族里重新求当前完整forward并执行原20档真实试探。没有循环追加相同的小步批次，没有把新增系数塞入旧九维owner。

新函数是
$$
h_\star(s)=\sum_{j}c_j\,\epsilon_j^2 Q((s-s_j)/\epsilon_j),\qquad
Q(t)=t(1-t^2)^3\ \ (|t|<1),
$$
支撑外为零。所有中心、宽度和系数在建立十坐标owner以前一次冻结。任意点profile、原节点/中点表、十列forward、全部FD、真实trial、连续scalar和453圆消费者必须使用这同一个函数。未来同g细化同样只能重新采样这个函数，不能重新生成Kronecker目录或符号。

## 2. 真实父与字面输入

父run43729310294/source c71cbeac7fd13c65cf50c7eb39842e9949737b25，即R340/R350实际157。原status为51842612B / 931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0，原summary为89063B / 7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2。它们只是来源，不会被本次伪造、下载或当作新owner状态消费。

本次九个原参数字符串在独立recipe中完整保存，新增xi初值为准确的0。原radius 0.0000390625仅记录来源。明确的新策略是 $|d\xi|=1$，这是R370有限系数盒的一次全尺度提议，不是继承父radius，也不意味着实际步长一定接受。真实alpha从1至 $2^{-19}$，仍由原二十档判断。

原699节点、698单元、三个低模、全部112末端行及四原输入不变。原十数组/原binding仍与actual157完整字面绑定，canonical_binding_sha256为cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3。沿164r2的已明确序列化修复，live Decimal与recipe字符串通过原encoded/clean完整比较，不删字段或容差比较。

四原input仍从公开历史8bd267107cc8710d371f3b62c02986655ac965b0临时恢复并按原size/SHA核定：

| 原件 | 字节 | SHA256 |
|---|---:|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail_anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail_config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

固定零尾anchor的112×112 slope J全部保留。它不变成当前新g的非线性native解或新g的完整尾响应；本请求始终不宣称nonzero场完成。

## 3. 原逻辑变量、隔离与全站覆盖

173 helper只消费已完成的R351原九维对象，逐原699 node与698 midpoint记录实际坐标、独立的a/b、商q和三列权。一个node的左右cell和末端角色已在R351散射聚合；这里对每个node:index或midpoint:index逻辑变量只计一次。不同逻辑变量即使坐标或形成值相同，也不被猜成别名。

每个允许的互异坐标只构造一个shape；若原三支撑重叠，取实际严格隔离gap最大者，原支撑索引破同值。gap包括其他所有原node/mid坐标及相应允许开支撑端点，并排除固定初末端。epsilon从1按二分取正dyadic，直到严格小于gap/4。因此新闭支撑严格不交，全部在允许的固定初末端之间。

同站有多个不共享q的输入时，采用
$$
\epsilon_j\sum_{\ell:s_\ell=s_j}\frac{w_\ell}{a_\ell}.
$$
不会用一个共同分母替代各项；b不被默称为a的准确导数。本次只使用odd零值jet方向，不声称包含R366独立的非零值jet方向，不能从这个子空间的形成零响应推完整函数空间驻点。

173准确rational构造与独立binary64点采样分开。新表的数值来自声明的binary64函数公式，再由Decimal.from_float准确提升。没有用准确Kronecker值覆盖实际形成表，也没有把有限表当作连续函数。

## 4. 符号、固定函数及实际新方向

173同时保存“原Jet商法则收缩”与“先聚合w/a再乘epsilon”的三向量。174显式选后者的字段 complete_three_rounded_epsilon_sum_weight_over_a，与原F形成点积：
$$
\widehat g_j=\operatorname{fl}_{50}(F^T\widehat{\epsilon_jG_j}),
\qquad c_j=-\operatorname{sign}(\widehat g_j).
$$
形成零分数给系数0。完整score表保原两个形成路径及其差，但只作为诊断，不是准确梯度证书。helper的原Jet-score排序不会偷偷替代本次定义。

所有允许候选都必须有完整有限分数才能定义这个“全部站”组合。某站异常/非有限时保原失败与不完整范围，不将它悄悄删除后仍称全站。空目录或全形成分数零时，保实际no-direction状态，不建造虚假的下降方向，也不宣布准确驻点。

新family把完整中心/epsilon/sign和源身份冻结成独立函数。数学定义SHA与完整来源定义SHA分开，完整账只在Actions临时目录。公开source、真正父、参数recipe、run和输出SHA可重生该实验；不把大形状账送入Git/Release或artifact。

在同一个已冻结函数上，producer再按当前binary64采样做一次完整R351 sampled-shape收缩及698单元forward/全112末端诊断；然后建立新的十维Decimalowner、原xi=0实际evaluate、fresh完整3×10 forward。真正第十列与当前全三残差重新确定xi方向的符号。若它与形成提议不同，翻转的是xi方向，不修改任何冻结shape系数。

原二十档使用完整三残差merit、严格负形成slope及准确提升的原binary64 c_A，保持原实际real/domain异常分类。源中这段完整方向/20trial以及全部最终消费者正文相对164r2逐文本一致；政策中提议尺度明确从0.01变为1，数学函数本身没有被替换成旧九维近似。

## 5. 真正十维与原末端责任

参数顺序固定为原9后接xi。旧九个分量在本次方向里为准确Decimal零，但完整十列forward及原60项Decimal、60项binary64投影FD仍形成。FD扰动旧九参数时不会调用目录选择，也不会改变中心、宽度或符号。

LiteralTenModel保原2422字面算术，仅在原九项之后增加第十个affine表项；完整r传播、三个2×2链、全112末端和原域保持。first9控制数组逐字绑定原输入，非shape数组全部与原model描述器核同。源schema独立，不把10参数发给旧9-only helper。

初末持久参数均为Decimal50；原四输入和新形状表仍是binary64字面样本。当前forward描述的是相应准确实表达的形成变分，不是IEEE离散映射的导数、区间误差界或准确秩证书。旧second模块仅用于实际157来源和binding兼容；本实验不调用新Hessian。

最终scalar/453圆是在明确binary64投影点重新执行，不替换持久owner，不证实两点全值相同。零扩展真实旧/新evaluate结果作字面比较；匹配与不匹配都是诊断，不变成新增接受门。

## 6. 连续分片消费者

FrozenOddSignSum.jet在任意输入站使用同一个冻结片段；严格不交支撑保证最多一个片段非零，零2-jet边界为零。binary64路径和准确rational定义的差别保持声明，不声称全域浮点误差已外包。

ScalarExpression重建完整冻结函数，把所有新支撑端点与旧breakpoints合并排序，并要求在原完整区间内部。每个连续区间用同一个原base expression加固定piece的准确rational多项式；原value与独立returned_ap两列分别计算。原Arb160/depth14策略不变，原所有区间会被实际消费。

最终453圆冻结原六个shape系数和xi，仅保原三个active坐标，沿原FFT/node/mid/RMS/末端流程。当前新增形状自身准确C²，不会修复原base的接口或a/b导数兼容性。未付的全连续metric、非线性native、完整非零fullDN、同g450及闭场族责任全部保留。

## 7. 生命周期与读回

独立producer只允许本公开仓库Actions。原whole-child2400s包含导入/setup/所有最终消费者；producer自身2400s自完成来源setup后计时。90s终止宽限、reader300s、科学step50min/job65min不变，原同进程组及2700s规则同步保持。预算或规则退出按实际partial记录，不解释为域拒绝或不存在下降方向。

所有状态、weights、完整score/shape表、FD扰动和scalar/圆raw只在request-owned临时目录。完整小结和实际错误在清理前输出。没有artifact、Release或可重算raw入Git。

reader输出单份真正结论，原硬90000B不变；实际字节尚待Actions，不能保证低于该上限，也不再预报40–60KB。它保：

- 完整来源、父、literal状态/输入/shape账身份和实际规则记录；
- catalogue实际覆盖、重复逻辑变量范围、skipped/未访问范围及真实异常；
- 冻结形状piece/sign计数、形成组合三响应/score及整体身份；
- 组合R351实际三响应、local-forward三响应、逐分量差与完整112身份；
- 原九伴随对照、初末完整3×10响应/J、12层FD原max/flags/120列覆盖及所有真实异常；
- 所有20档已执行原alpha/merit/F3/slope/Armijo/域/理由/xi和完整未访问计划；
- 原scalar/453圆小门、所有final flags及未付责任。

本次只加一种实际逐字重复引用：先完整解析原status、全部120列/12层FD及全部异常，再比较完整规范编码字节；覆盖不完整时不启用引用。fresh旧九forward、旧九伴随比较中的原reference-forward矩阵，只有确实逐字等于保留的initial完整3×10前九列，才能改为明确同摘要reference、列区间0:9与原value identity；完整伴随实际矩阵及所有差值不因“接近”省略。原final或final_binary64_projection完整对象只有确实逐字等于对应initial、且本对象无真实异常/失败，才以明确reference和原完整/紧凑identity表示；否则完整保留。不比较浮点近似相等，不用SHA相同代替原字节比较，不把未来接受后末态假定等于初态。

这一修订只减重复metadata。初始完整3×10和新列、全部20试探、所有差值、FD实际失败原文、Arb/圆门和未访责任保持。被引用末态的所有FD仍已经真实读取、统计；对partial明确记录覆盖不完整，不声称120已付。新reader schema为request174-fixed-all-station-odd-signsum-original-compact-word-reference-v2；引用schema为same-summary-byte-identical-reference-v1，使用同摘要JSON pointer，没有跨文件数据依赖。

实际r3基准的单份89762B已接近硬限；其中六候选9509B、20trial22983B、initial/final各6409B、两个binary投影各4263B、旧九伴随比较4455B。174删去六候选而新增站目录/固定函数摘要，因此这些旧字节不是174总大小预测。旧r3保留的两份重复旧九forward与initial前九列逐字同，初末保留描述也逐字同；这只说明新规则有实际重复可减，不能为未来174承诺总字节。

大weight/shape/score表和完整FD扰动表只给真实身份。固定旧九参数不逐trial重复；若某条记录偏离固定原词，完整异常参数保留。相应科学大表不被描述为root逐值审过。超限或字段缺失仍诚实fallback，没有数据编码、字典压缩或拆份绕过工具限制。

空目录/全零分数等可能没有完整十维final消费者，这种原情况会明确no-direction/未付；wrapper不把它冒成成功的完整科学诊断。即使Armijo接受一个点，本请求的success/nonzero/native flags也不被伪改成true。

## 8. 来源闭包与独立调度

保原actual157的107个scientific pins与9个support pins。新增当前family/model/producer、R351、173及wrapper共6个science条目，得到113；加当前纯读回reader得到10个support。真正producer消费原41加family/model/R351/173/producer，得到46。wrapper和reader不冒成producer内数学调用。

164源仅为本次文本差异基线，不导入或执行；它们不混入当前46消费表。旧157优化main和旧polynomial optimizer不运行。本次原setup/完整方程通过冻结来源闭包正常导入。

唯一push触发：
topics/visible-flex-larger-amplitude/computations/public-local-odd-signsum-ten-control-request.json。

独立workflow：
.github/workflows/visible-larger-public-local-odd-signsum-ten-control.yml。

与164的workflow、并发组、输出根、status/schema全部分开。没有未来run数值，没有从164失败或未读点继承。

## 9. 可执行接口

由冻结wrapper按request和四原input路径生成实际命令。producer的科学参数为：

~~~text
--parameter-recipe <local-odd-signsum-ten-control-actual157-parameters.json>
--parameter-recipe-sha256 4d9c0e3194f4d7d06356fff21cd92dae64a9866ad29715f54c1b351ca0071a6b
--backtracks 20 --decimal-digits 50
--interval-bits 160 --interval-depth 14 --wall-seconds 2400
~~~

另有原accepted/prepared/tail-anchor/tail-config与新owned out路径，全部由workflow恢复的原字节指明；没有默认输入或隐式替代旧native包。

新producer schema：
R259-all-station-fixed-odd-signsum-ten-control-one-real-full3-direction-v1。

新status：
local-odd-signsum-ten-control-status.json。

## 10. 最终文件身份

下表除workflow外均相对topics/visible-flex-larger-amplitude。173与R351已公开，不在本次新文件中重发。

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| computations/geometry_20261115_local_odd_signsum_ten_control_family.py | 26725 | ae05a01f11f25b77e39aaf77c2603dcd09a78d4155ade6aff6df9bcad2bd9df6 | 5acef6ee98fa22e390a350eaf20d9e4c173322bb |
| computations/geometry_20261115_local_odd_signsum_ten_decimal_model.py | 10486 | 694f1cb5351c4b71e90684967e1fa3d974861f84f23c2183ace7f8c4a6a07d90 | 09ba7af11e093d2b5641c710eaee6ae5bc500f40 |
| computations/geometry_20261115_local_odd_signsum_ten_control_recipe.py | 37149 | 975bb25f1dd879bd88dc1a3b1df451836cadceca1695820050bfe3842efd949f | 38c6a0b66a6f94d153d9f61cbd687730627f13d5 |
| computations/root_20261115_local_odd_signsum_ten_control_scalar_readout.py | 35962 | fad015510fcd230211dbff2c12c487a1df4a61d8bdebd6fa97e1f64c8f520037 | fb8a0377c1322870ae578b78f2a867922ab45686 |
| computations/geometry_20261115_local_odd_signsum_ten_control_temporary.py | 19328 | 8d8981b5d91b53e2fd7c083c93a93a3840152fa5e396d65d59a1a20921b939b5 | c8e45d8fe2a3751ade47d4d7e168faaa093ab39d |
| computations/local-odd-signsum-ten-control-actual157-parameters.json | 8225 | 4d9c0e3194f4d7d06356fff21cd92dae64a9866ad29715f54c1b351ca0071a6b | b6ac0e724893e94b861c48b3564452690063d9a9 |
| computations/public-local-odd-signsum-ten-control-request.json | 43626 | 1e61b40ebabecc917d52cb2cabc782c493fcf53a58a3e82b959ac06d770ccd5b | 684ccb72992b100ee5f1e71c79fe57a5b9489191 |
| .github/workflows/visible-larger-public-local-odd-signsum-ten-control.yml | 21392 | 11f08242dd73c990909cc13f763887f5216e72ead21663822dd699e29770e640 | e019ffe4440c4105c3fbabc209e2d72d03286f52 |

完整科学三件差异：51046B / 5bb29a23ef1ebc9bd6cf1e437df37629a982c6edcb63c96e05847a654877caa3，blob125d1fa877db26d60e968008803fd996d27d4238。reader/wrapper/recipe/request/workflow最终完整五件差异：74944B / 5973ffe395635e0ce446906d6bcf7b13932aeadb40e5755cfb09db5a0eaffd4b，blobda866a743dc7823d43f37927144b83dc6e9a3bb0。相对root已全文读的首版174，只有本次逐字重复引用及两个pin/reader schema/大小措辞的四运行件最小差异：11751B / d5331dc5bb7d3217a4618a0f6d780f0a3dd6ee8ebe79c4b3bcbb2eb4ffa3299c，blobc9fb899f0d5b94e0822b70ef1f9c4e4d50016b02。三科学源及参数recipe逐字保持。

当前只完成源文本、JSON、来源闭包和完整差异的检查。明确核对113/10与41→46、七当前pin、policy/contract、recipe实际字节和完整父binding，以及原20trial/最终段逐文本保持。没有本地导入科学、运行模型、构造fixture或声称本地Python AST执行。原Actions AST/pin责任保留。

本接口与R370证明只定义一个可以执行、可以拒绝、可以如实partial的新实验；不是实际结果、斜率准确证书或完成课题声明。
