# R815 的独立共同分母消费者：三维候选与原完整算子认证

日期：2026-11-15。状态：**新的计算方法与执行契约；尚未运行这项候选搜索，尚无新的准确算子。**

本任务直接消费原 R815 已结束计算的 425-prime CRT current。
原同核续算仍独立进行。本任务不生成或重做这 425 个素数的 $M_g$ 模像。
新源码、配置标签、来源和运行身份独立；冻结的原 R815 核心及 R811 框架均不修改。

证明与规范沿用
[R813](../results/R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md)、
[R817](../results/R817-original-normal-derivation-without-separate-h-multiplier.md)
和[原 R815 契约](R815-original-normal-derivation-operator-method.md)。
这里仅改变从已成 CRT 寻找 $M_g$ 候选的方法。
一旦准确认证 $M_g$，在同一新标签中直接继承冻结 R815 的 $\Gamma$ 计算及两图输出，
避免向旧标签强装一个来自不同核心的成功阶段。

## 1. 已实际存在的来源

原生产者为 run 43719622321，source
2a3300a9edec73c23e72f23127a0ae7d8222d13e，核心 SHA256
80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d；
其实际结束原因为 BudgetStop。完整算子尚未形成，$\Gamma$ 尚未开始。

原 artifact 14174374945 为 2716759066 字节，
平台 ZIP SHA256 为
597aaf0006481ed9fc47fda4bb6635ff6b1b8aef336d8484ca92a9bbe9e802c4。
原 full manifest 为 892108 字节、3464 项，
SHA256 为
4e78095e2adc217beb86d4f760e6207a4aa60c4492bbfcc739a8544f376842e5。

实际 current 为 R815-target-g-component-00-CRT-current.json.gz，
561995095 字节，SHA256
402379e2b5a0d4b225fda74d798bbb164d77ce7c3001eddca789d0fe602ef27c。
它保存 425 个已消费素数、295936 个加权系数位置；
模数位数为 12707，最后一个素数为 1000008791。
匹配的小 receipt 为 R815-target-g-component-00-CRT-step-000425-receipt.json.gz，
3902 字节，SHA256
f136bee8e383b5fcff03a86bebc5bf8f30f3394d885f8aa4ac1e327ad7a82042。

原 input carrier 为 R815-retained-producer-inputs.tar.gz，
109958828 字节，SHA256
051571e117cdaafe31f9851c664c72583f55181444dbe112bbcbb7f2d2fbf1b3，
包含原 R806 的 45 个文件及 R813 的 8 个文件。
小 IO run 43747973677 已核上述实际身份、manifest 和匹配 receipt；
它没有重哈希 562 MB current 或整个 2.7 GB ZIP。
新消费者实际读取 current 及其他成员时必须逐原 manifest 核 bytes/SHA，
不能把先前的小 IO 描述成大数据已经重新下载验证。

同一来源中已成的原 $M_w$ 整矩阵、两个原向量及 Krylov point cache
按原字节、原配置和共享数学身份读取。
新 $\Gamma$ 在相同 prime/point 使用这些准确缓存，
不重新求已经完成的逆。原 r3 六点插值权不能直接冒充 r2 五点插值权；
仅后者确实尚未生成时才计算。

## 2. 原矩阵、首列与候选的充分认证

始终使用原正规基
$$
\epsilon=(0,1^{144},2^{127}),\qquad \beta_0=1,
$$
以及原 $W=M_w\in\operatorname{Mat}_{272}(\mathbf Q[z])$。
原 R806 已准确认证 $e_0$ 对 $W$ cyclic，且原 $We_0=e_1$。

待求矩阵的原约束为
$$
\deg(M_g)_{ba}\le 3+\epsilon_a-\epsilon_b,\qquad
M_ge_0=v_g,\qquad [M_g,W]=0. \tag{1}
$$
原 $v_g$ 的 690 个允许系数已经在 R813 全 820 行认证。
它们的准确值包括原 column denominator 与 rational scale，
不能再补回已去 content 或任何 $82$ 因子。

**充分认证。**
设 $D>0$，$N(z)$ 为整矩阵，并逐项满足 (1) 的加权界。
若
$$
Ne_0=Dv_g,\qquad
[N(k),W(k)]=0\quad(k=0,1,\ldots,6), \tag{2}
$$
其中第二组在原分母准确清除后对全部 $272^2$ 个条目成立，
则 $N/D$ 就是原 $M_g$。

证明：交换子每项次数至多
$4+\epsilon_a-\epsilon_b\le6$，故七个不同准确点迫完整多项式交换子为零。
设 $C=N/D-M_g$。由 $CW=WC$ 及 $Ce_0=0$ 得
$CW^je_0=0$；原 cyclic 性给 $C=0$。
这里无需高度界、LLL 最短性、概率性成功或 CRT 唯一重构假设。
准确终验点也无需是 Krylov 好点。

因此下面一切格或 scalar RR 操作只生成候选。
充分搜索失败不能解释为原矩阵不存在，也不能证明 425-prime 模数不足。

## 3. 原最小首列分母与三维格

把原已成 $v_g$ 写成
$$
v_g=P_g/d_g,\quad d_g>0,\quad
\gcd(d_g,\text{全部 }P_g\text{ 系数})=1. \tag{3}
$$
原 R815 original-vector 已作这个共同 content 约分。
读取后仍核该 gcd；这样 $d_g$ 正是所有约分后首列系数分母的最小公倍数。
它不是未经约分的原 column denominator。

若 $D M_g$ 全整，则必有 $d_g\mid D$。
记已成 current 模数为 $M$，两个所选非首列系数的原余数为 $r_i,r_j$。
使用行格
$$
\mathcal L_{ij}=
\mathbf Z(d_g,d_gr_i,d_gr_j)
+\mathbf Z(0,M,0)+\mathbf Z(0,0,M). \tag{4}
$$
其中第二、三坐标可先取模 $M$ 的平衡代表，
不改变整数行格。每个格向量 $(D,n_i,n_j)$ 满足
$$
d_g\mid D,\qquad n_i\equiv Dr_i,\quad n_j\equiv Dr_j\pmod M. \tag{5}
$$
只考虑 $D\ne0$，同时反号使 $D>0$，并核 $\gcd(D,M)=1$。
在这些检查之外不以 $\sqrt M$、矩形唯一性或估计高度拒绝候选。

可以把三列乘固定正整数权后调用准确整数 LLL。
解码必须逐坐标整除权，并准确核原行变换、格同余和正化符号。
每个已试三维格的输入、LLL 原行、变换见证、候选及拒因均保存，
不能只留下“所有短行未通过”的不可追查计数。
本首策略只消费每个约化基的三行，不声称枚举全部短格向量。

未加权格行列式为 $d_gM^2$。
所以常说的 $M^{2/3}$ 只能是 $d_g=1$ 或适当尺度下的平衡启发；
加入真实 $d_g$ 后尤其不能把它写成一个保证可恢复的分母高度范围。
本方法的正确性完全来自 (2)。

## 4. 确定性探针与已知首列的准确提升

原冻结代码只逐系数使用
$$
|n|,d\le\lfloor\sqrt{(M-1)/2}\rfloor
$$
的 scalar RR，再合并每块分母；它没有 (4) 的共同分母搜索。

首轮探针按原 flatten 顺序
“输出行、输入列、幂次升序”读取实际 425 current，
排除首列，选择前两个 strict scalar RR 失败的位置。
425 尚未由原每 8-prime 策略执行此项尝试；
不重新调用旧 424 阶段或删除它的拒绝记录。
探针扫描记录已完成游标及真实位置。后继 probe pair 沿同一确定顺序继续，
不凭候选值挑选有利坐标。

若扫描至末尾不足两个失败位置，记录实际情况；
允许配一个已扫描、非零且不同的非首列位置，
或在所有位置均通过时以这些新 425 scalar RR 的实际分母公倍数生成候选。
不得预填存在两个失败条目，更不得把这种边界当作数学失败。

令候选 $D$ 满足 (5)。对于非首列所有位置，暂取
$$
N_\nu=\operatorname{center}_M(D r_\nu). \tag{6}
$$
对首列则直接置
$$
Ne_0=(D/d_g)P_g. \tag{7}
$$
这是原已知向量的准确整提升，**不要求其系数在平衡区间内**。
如果强制对首列也用 (6)，会因已知大分子而无谓排除可用 $D$。

输入阶段完整核原 current 的 690 个首列余数与 (3) 相符；
候选阶段完整核 (7)、加权零与全部模同余。
因此首列在本策略中是构造性约束，不再称作独立的廉价候选筛。
(6) 对未知列可能选到错误提升；只有 (2) 的全部准确恒等式能接受它。

为减小明显错误候选的实际成本，可把 (2) 中少数 scalar entries
先准确计算，例如 $k=0,1$、探针所在输出行与输入列 $0$。
一个非零项已是同一完整终验的准确反证，应记录原分母与整数残差。
全部这些早期项为零仍不能宣称通过；随后完整运行七点、全部行列及全部行块。
这只是同一必要终验的执行次序，没有增加独立检验门。

## 5. 原完整认证、两图与 Gamma

候选按原 16 行块保存共同正分母及加权整系数。
完整终验复用冻结 R811 的整数矩阵乘法、七个准确点、
每个 $16\times272$ 行块见证、首列和 weighted 支持核验。
来源引用改为实际外部 current；新的候选序号不能冒充新的 CRT prime count。
成功索引明确保 actual_CRT_prime_count=425 和 original_external_CRT_source，
同时另记新候选编号及新来源。

成功 $M_g$ 的原第二图矩阵逐项按
$$
M_g^\sigma(t)=t^3D_\epsilon(t)M_g(1/t)D_\epsilon(t)^{-1},
\qquad D_\epsilon(t)=\operatorname{diag}(t^{-\epsilon_a}) \tag{8}
$$
运输。每个 entry 的准确反转指数为
$3+\epsilon_a-\epsilon_b-k$，原单位列及所有分母保留。
原第二图导子的底变量矩阵仍为 $-M_g^\sigma$。

随后在这个新消费者内继续冻结 R815 的 $\Gamma$ 实现，
不重新求准确 $M_g$。
保原 R817 的
$$
H=\Gamma W-W\Gamma+M_gW',\qquad
\Gamma e_0=0,\quad \Gamma e_1=v_h,\quad [H,W]=0. \tag{9}
$$
$\Gamma$ 五点模插值、strict scalar RR、七点准确嵌套交换子、
两图负一次项准确相消以及当前 CRT/小历史机制均不变。
不独立 CRT $M_h$。

新消费者不借用旧 R815 的数学标签，也不要求旧 same-core resume
接受不同 core 的阶段。原冻结核心只作为按 SHA 读取的实现依赖。
真正的初始化、receipt、configuration.source_sha256 和最终 run 身份
都指向新核心；$\Gamma$ 每个阶段另指向此任务中已经认证的真实 $M_g$ 索引。

## 6. 最小源闭包与断点

直接来源仅为上述已结束 R815 artifact。
从实际 full manifest 读取并哈希核：

- current、匹配 425 receipt、原 public input/run/core receipt 与 input receipt；
- 原 $W$ 整矩阵及 g/h original-vector；
- 原已成 shared Krylov point cache，保全部原配置和共享身份；
- 原 input carrier 的完整 53 个 R806/R813 成员及各原 manifest/证书链。

不下载或恢复已经删除的旧完整模像，不回退到较早 current。
新数值计算只读取 current；原 425 模逆、模像和 CRT 更新均不重新运行。
Gamma 复用实际同 prime/point 的原 Krylov 文件，
仅新 degree2 grid、尚不存在的 Gamma 模像/CRT/准确终验属于新增算术。

原输入缓存放在单独 retained/R815 来源目录。
原字节和 configuration 不改；
读取适配器按完整旧标签、实际源 SHA 与 shared mathematical identity 明确接纳，
不能去掉旧标签后改写为新任务自产。
新 Gamma 若以后需要不在旧范围内的 prime/point，才生成新 point stage。

探针扫描、LLL 完整格阶段、每候选构造块、准确终验块、
成功 $M_g$ 与 Gamma current 均原子保存。
已完成候选不得重复；在写最终拒绝 receipt 之后才可裁掉不再消费的大候选块，
receipt 保全部实际被删文件的 bytes/SHA。
已接受候选、当前候选和源 current 不能提前删除。
原源 current 是只读输入，不能被继承的 CRT cleanup 当新任务 current 删除。

如果搜索控制达到本次上限，输出诚实的 candidate_search_exhausted 或
search_budget_reached；没有成功 $M_g$ 就不开始 Gamma。
失败 FINAL 可作为后续继续搜索的真实断点，不能装成旧 R815 成功证书。

## 7. 固定接口与诚实完成范围

数学 RESULT 保持 R815-original-normal-derivation-operators；
FINAL 保持 p41-original-normal-derivation-operator-certificate.json。
新文件名使用 R815_projective，真实新 core/wrapper/method/source 全部单独绑定。

数学标签额外固定：本方法 SHA、冻结 R815 核心 SHA、
原 425 source/current/receipt、确定性探针规则、三维格行方向及固定权策略。
预算、允许追加的 probe-pair 数量是执行控制，不改变已经完成阶段的身份。
不能借增加预算改变已经试过的格或坐标规范。

只有原 g/Gamma 都完整准确认证，才写原 FINAL complete=true，
保原 operator_indices、两图块、actual_input_producers 和原 R813/R817 最终字段。
若只有 g 已成，独立的 g 索引如实可读，完整 FINAL 仍不称两算子完成。
将来 R825 等消费者应填本任务真实 source/core/manifest/证书，
不继续使用旧 80516ff9 的 producer 身份。

本任务不输出原极理想、D、eta、beta、原 A 的核前像或高度。
未证明搜索成功、分母高度界或任何 Serre-uniformity 完成结论。
