# Serre 一致性交接

## 目标、授权与现行规则

证明绝对常数C使所有无CM E/Q在p>C时模p满射，或完整给p→∞反例族。**主目标OPEN，未达README完成标准；持续研究，不在阶段报告收尾。** 会话serre-public-astra-20261115；沿远端main，旧未推分支不存在。私有QUEUE已推55eeff4d64c2f54f6b30d8ea5b6dd669f86a4b09。

**已读规则提交：c7982f5f61c1b91dad1d9cbd2e70956fff07fc56**（2026-11-15T18:48:29.243804+00:00；双probe run43748801736/rules job132917932629真实git pull --rebase origin main，两README无diff）。旧rules run43714581068达50次限额，不再重跑；新run可继续。14:34UTC终端失联，根§8小文本接口回退。此前完整H逐字保[此次归档](handoff-archive-2026-11-15-before-projective-two-probe.md)，内接原全部归档；[结果全索引](results-archive-2026-11-15-before-R833.md)与各结果保源pins。

每结论立即推；非快进/引用竞争立即实际pull --rebase循环重推，禁force；每小时及每push前实际pull，比较两README，变化只读diff即遵守并记SHA。PAT只CLI不落文件。root独占main/共享索引，代理只专属稿。新数学只公开Actions，本地仅纸证/IO/schema/hash/AST。根§15禁raw/机器证书进Git/Release或悬挂blob，仅一日必要活跃artifact。H<10KB/open<30KB/Markdown<100KB/课题<200MB；日志Asia/Taipei每条≤5行；不添独立测试gate。

## 实际运行与端点

**R787原430位同核续算**：run43737413555/job132883028161/source4092d1cc4d1156bc24a10ff820fd39c5713e8ad7，core93d3d72b/wrapper42157e0d，约21:47UTC预算端点。[430断点](notes/R787-430-digit-checkpoint-and-same-core-continuation.md)保原run43708449812、artifact14170087848/438780485B/manifest1b92c4e5/lift00855d88；prime753/free1186/14分支不变，不回退259。无A/B，后继R792/804/809未激活。

**原430位projective首轮及不同42维后继**：旧run43745966802/source d71d40bb/core e0a5ad95/wrapperb2c4efda在71.023573757秒exit2；小IO43747260495真核5根全C0失败、140行仅因D_bound拒绝，K59位，无子节点/准确验算。[首轮记录](notes/R787-projective-first-ended-search.md)保artifact14173922406/189847233B/37d11e283、manifest422319cd及全部pins；不证430不足，盲增旧节点无用。

**新双probe已计算**：run43748801736/job132918006043/sourcee2ac3449ac480c6f00bce197c0bd5202f8b1fda4，已AST过。[方法](notes/R787-original-projective-two-probe-reconstruction-method.md)17c89271、core73bac3a2/47438B、wrapperfe276ba3/43795B、workflow5c5436fd。首(C0,C1)的直接42格，最多42候选/一格，原归一lift直接求D，不累乘；全部42短行/84同余保留，单位性只诊断，无高度界硬筛。原free=D（不center）、Z/内容后D/e及完整129×280+B非零才成功。原1380输入/430lift不重算，原数学RESULT/recipe/carrier沿用、新tag/source独立。closed失败候选先完整非零残差及SHA清单再删不再消费的大payload；当前/成功完整保留，queue按真next_candidate续接。节点/格/时间预算分开。旧Dixon run继续，尚无A/B或后继消费者。

**R815原425素数同核续算已请求**：原run43719622321/job132828560965/source2a3300a9edec73c23e72f23127a0ae7d8222d13e真实BudgetStop，g完成425prime/最后1000008791/模数12707bits，Γ未开始，无完整operator。小IO run43747973677已成：manifest892108B/3464项/4e78095e，current561995095B/402379e2与425小receipt f136bee8匹配；carrier109958828B/051571e1保53原源。artifact14174374945/2716759066B/597aaf00到Nov16 18:33UTC。[425断点](notes/R815-425-prime-checkpoint-and-same-core-continuation.md)保全pins。新原请求ac0870b2只增resume，core80516ff9/wrapperab725da0/框架849bca27及g/Γ、prime007、每8prime重构、16行块/嵌套mode不变。续算run43748439850/job132916821952/sourcea108ce1e72958b296dcca7ff55710c94e8ed16ef已进入计算；不重算425prime、不另Mh。

**R824准确27+244续算**：run43732499815/job132867842693/source442f3d16a9b914154e8b81bc61597d650044fd61；core1ece3cf4/wrapperc5907739/requestec04ad32，约20:50UTC端点。1186归R787，旧129/142/280Q全式、1521打包与κ/246一次保留；真实272全生成后才1778纤维minor/总余长1206。首轮28权五/300权六profile及lower56+244已成，准确5/6仍待，r28无需补143..155。

**R827首真实q4**：run43734420663/job132873746638/source400edecfeab313d1858cdb72bf18f8452ab9566a；core d9cf7739/helper38baf6b4/wrapperdbd8356e/request1804789d，约21:20UTC端点。六来源真，ell753/branch0/free1186/integral_B=lambda*b/6724一次不改。[R827](results/R827-original-global-modular-surjectivity-and-derivative-termination.md)需真σ∞rank272与τ整多项式Hermite/Bézout；272个B·d仅子理想，额外零可使检验失败，单点/函数域rank不够。当前未得D/K1。

## 已成输入与准确关系后继

[R809六C](results/R809-certified-original-six-Hodge-normal-vectors.md)run43712427063/source91fbd81e，84Q/full1380/S5=1234已成；artifact14168728276至Nov16 15:52UTC，A/B不在scope。原wrapper允许直接resume六C成功包、追加真R787后仅求A/B，basis tag排future源，毋须新adapter。原R792 workflow已按根§15移除publish、contents降read，core7b7a5483/wrappercdac2e93不改；真projective成功时可直接消费。

R806/W、R813/g,h、R820/C、R801/803/805/807与R781 R0..142均已认证；V6/7/8尾界141/175/195保原。R805[1,144,127]非272项EPS。五个R824入口R792/R809AB/R804/R811/R825全核pending，完整pins见归档；不冒名R787或将C-only当AB。冻结849bca27/89579f79不改，双向Laurent/全长1206、272×816全核秩544不可省；K395非实际，导数向量非乘法算子。

原b/s/λ/82^10一次，内容/分母不重插；原共轭/唯一Fb立方根、vκ及同源有限核保留。真实A/B可共乘非常数但比值须同原y。当前无I/P/Q/D/eta/高度。R775/R786至Nov16 05:52/05:41UTC，R786 index已保后载体；R790的146CM行至07:22、R791 tangent至06:37，R794 carrier不含后二者。关系发布即消费；到期前只IO保必要真实输入，不重算。全部原子完整stage/current及最小bundle需续接，原[期限核对](notes/2026-11-15-R815-endpoint-and-input-retention.md)保API边界。

## 全p高度、sigma及ordinary边界

[R832](results/R832-original-height-explicit-uniform-contact-order-bound.md)已证全p统一jet截止：G=(p−1)²/4，R=21G+4，ord Eij≤R−1+binom(R,2)(6G−4)。不代实际高度/整盘无根，(724.33)仍缺；不生成最坏巨大窗口。R634逐盘非恒零已成，R785原T_p未知；R616/726仅给真正商非挠/rank/log，R575真正CM根号负、逆twist秩零撤回。

[原Poincaré/period审计](notes/2026-11-15-original-height-Poincare-linearization-and-period-determinant-audit.md)9a54e844保原Q点β/非p/rigidification；U_i=c(a_iV_i−A_iL_i)线性化，同一第二类修正全函数相消，零阶实际纤维仍保。T_p仍次数d_Y+2的指定period多项式，线性AST不排；η^-不删切向。End⁰(G)=F且非零torus商维≥g+1，无几何幂等元低维捷径。完整论证见原note及归档，未得新高度非零。

sigma仍缺同一primitive/Legendre可见h的三个原单位。R739反例、R741/R737不同密度不可拼；旧R808/810、p²/Hirota/固定六维支路关闭，保[K,P_T]。R826/828八原源及两G零、R830真实权6/conductor-p、R831 old6不可约全保。R833/834真源全局非零、SS/Serre-dual识别已成，但指定uP0,e和配对未知，不能替原CM/同h非零；全部常数与边界见归档及原结果。

[原unitary交叉heat](notes/2026-11-15-sigma-unitary-cross-heat-and-primitive-source.md)1df7c782已核：实际H/J/C三同源、完整36theta及full72整模型；原CM整段FG不换。∇=D−M−∂z∂t/6−3Xzt/2，双向Frobenius及两边/角点全保，P0曲率6B²zt。首p按整数差的原Legendre×primitive权W真正水平，∇^(p−1)(W Lz²Lt³R)指定FG/度p+1准确等于6⁶B⁷Σ原同h项；非零仍未知。μℓ仅有共同jet作用，不称原36全局稳定；原FG一次横向源为零，不能用全向量单位替它。旧R739反例仍有效。

ordinary p43/776bitq已Gaussian5排除。[Shapiro二阶](notes/2026-11-15-original-Robert-Shapiro-second-class.md)337a9892给唯一K_glob/Θ=i a_q；[exact-dual θ-lift](notes/2026-11-15-original-exact-dual-theta-lift-and-shifted-cup.md)7388c4be保同Σ θ3、原共轭k结构与首阶flat/strict-p条件。真C4除T²的杯积只恢复旧R779，未获独立数值/完整晶体；Θ未知，禁巨大q挠点枚举。

## 主目标仍开放

R816/818/819/821/823全cusp单轨道/原Hom域秩一与评价、整格cusp像O及原y简单极已成；R729充分大全p的c1不分歧不添单位/高度。R707原p41完整129盘/八CM分类已闭；原b=r0⁶/LK7/ML40/αs/CRT6逆/ζ²一次/246/c14424/c0[2876,2822,2823]不改。仍余R317的p2/5mod9完整非分裂正规化子、a³+db³1/p|b；D/bc无统一上界。原eta/beta、实际高度jets/(724.33)与全p证书未成，继续open.md。
