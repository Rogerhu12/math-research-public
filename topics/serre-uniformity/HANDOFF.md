# Serre 一致性交接

## 目标、授权与规则

证明绝对常数C使全部无CM E/Q在p>C时模p满射，或完整给p→∞反例族。**主目标OPEN，未达README完成标准；持续研究，不在阶段报告收尾。** 会话serre-public-astra-20261115；沿远端main，旧未推分支不存在。私有QUEUE已推55eeff4d64c2f54f6b30d8ea5b6dd669f86a4b09。

**已读规则提交：40c3bb3c22f46c4a2a8b1051f4a90d9cb5864281**（2026-11-15T19:10:39.271646+00:00；rules run43745726410/job132924494373真实git pull --rebase origin main，两README无diff）。root README SHA6979d793、topic35f82f3d。旧rules run43714581068达50次限额；只重跑新专用rules job，不重跑数学workflow的rules依赖。终端14:34UTC失联，根§8小文本接口回退。完整前H逐字保[此次归档](handoff-archive-2026-11-15-before-R815-projective-method.md)，内接全部前态；open完整前版在[双probe前归档](notes/2026-11-15-open-before-projective-two-probe.md)。

每结论立即推；非快进/引用竞争立即实际pull --rebase再推循环，禁force。每小时及每push前实际pull，两README变化只读diff即遵守并记SHA。PAT只CLI不落文件。root独占main/共享索引，代理只专属稿。新数学只本公开Actions，本地仅纸证/IO/schema/hash/AST。根§15禁raw/机器证书进Git/Release或悬挂blob，一日artifact只保当前必要输入/断点。H<10KB/open<30KB/Markdown<100KB/课题<200MB；日志Asia/Taipei每条≤5行；不添独立测试gate。

## 公开算术当前态（19:09 UTC）

| 任务 | run / job | source commit | 状态 |
|---|---|---|---|
| R787原430位同核续算 | 43737413555 / 132883028161 | 4092d1cc4d1156bc24a10ff820fd39c5713e8ad7 | core93d3d72b / wrapper42157e0d，预算约21:47后 |
| R787新42维双probe | 43748801736 / 132918006043 | e2ac3449ac480c6f00bce197c0bd5202f8b1fda4 | 19:05:49 exit2/894.401s，42候选m0通过/m1全拒；一格及节点预算尽，余5对未执行 |
| R815原425-prime续算 | 43748439850 / 132916821952 | a108ce1e72958b296dcca7ff55710c94e8ed16ef | core80516ff9 / wrapperab725da0，原目标/prime/mode不变 |
| R824准确27+244 | 43732499815 / 132867842693 | 442f3d16a9b914154e8b81bc61597d650044fd61 | core1ece3cf4 / wrapperc5907739，约20:50后 |
| R827首真q4 | 43734420663 / 132873746638 | 400edecfeab313d1858cdb72bf18f8452ab9566a | cored9cf7739 / wrapperdbd8356e，约21:20后 |

**R787原断点**：[430记录](notes/R787-430-digit-checkpoint-and-same-core-continuation.md)保run43708449812、artifact14170087848/438780485B/manifest1b92c4e5/lift00855d88。prime753/free1186/14分支不改，不回退259。首projective run43745966802于71.023573757秒exit2；[实际诊断](notes/R787-projective-first-ended-search.md)保小IO43747260495、5根C0、140行仅因D_bound拒、K59位，准确验算0阶，不证430不足。

**新42方法**：[完整契约](notes/R787-original-projective-two-probe-reconstruction-method.md)17c89271，request7421c941/workflow5c5436fd。直接原lift两probe求D，不累乘；全部42行/84同余保留，无高度或单位硬筛。原free=D不center、Z及内容后D/e，完整129×280+B非零才成功；原1380输入/430lift不重算，RESULT/recipe/carrier兼容，真实新tag独立。失败payload先原子准确残差+SHA清单再退役，当前/成功全保；queue/节点/格/时间预算分开。此次artifact14176445740/195943656B/1fdcdc96，42闭合回执+完整1380输入验证通过。新two-probe ended-IO只取小输出/manifest/queue/LLL，随后同tag接余下探针，不重算首格。

**R815真实断点**：[425记录](notes/R815-425-prime-checkpoint-and-same-core-continuation.md)保原run43719622321/source2a3300a9的BudgetStop。g425prime/last1000008791/模数12707bits，Γ未开始、无完整operator；小IO43747973677实际核manifest892108B/3464项/4e78095e、current561995095B/402379e2与425receipt f136bee8匹配。artifact14174374945/2716759066B/597aaf00，carrier109958828B/051571e1保53原源。新请求ac0870b2仅增resume；冻结849bca27/原Mg六模七准确、Γ五模七嵌套、prime007/每8次RR/16行块均不改，不另Mh。

**R815独立三维共同分母消费者本次激活，run待登记**：[契约](notes/R815-original-projective-rational-multiplier-reconstruction-method.md)ba9ac593。消费425 current，原g首列最小分母d_g，3格(D,n_i,n_j)只生成候选；首列用准确D·v_g、未知列center，weighted界/完整首列/原7点全部commutator加cyclic才认证Mg。425首两个新strict RR失败非首列坐标为首probe，不重做424。det=d_g M²，无M^(2/3)恢复保证。真新core/tag继承Γ、读原Krylov旧tag，不伪装旧resume。core126469e2/wrapper3a0fa603/workflow6e474fae/request226af585，300min/首4probe对/7固定权，全源码已读。首同次AST后数学；原同核run继续。

**R824/R827边界**：R824首28权五/300权六profile、lower56+244已成，准确272未成；1186归R787，原129/142/280Q、1521打包及κ/246一次保留，r28不补143..155。全生成后才1778纤维minor/1206。R827需真σ∞rank272+τ全多项式Hermite/Bézout；B·d_i只是子理想，单点/函数域rank不够。ell753/branch0/free1186/6724一次不改，尚无D/K1。

## 已成源、真实消费者及期限

[R809六C](results/R809-certified-original-six-Hodge-normal-vectors.md)run43712427063/source91fbd81e，84Q/full1380/S5=1234准确已成；A/B不在scope。真R787关系后原R809可resume该包、只append A/B，basis tag排future源；原R792 core7b7a5483/wrappercdac2e93可直接消费真新R787，workflow已删publish、contents只读。

R806/W、R813/g,h、R820/C、R801/803/805/807、R781 R0..142均已认证，不重算；V6/7/8尾界141/175/195，R805[1,144,127]非272项EPS。五个R824入口R792/R809AB/R804/R811/R825全核pending、pins见归档；不冒名R787或将C-only当AB。冻结849bca27/89579f79不改。双向Laurent/全长1206、272×816全核秩544不可省；K395非实际，导数向量非乘法算子。原b/s/λ/82^10、共轭/唯一Fb立方根、vκ/有限核边界保；当前无I/P/Q/D/eta/height。

R775/R786至Nov16 05:52/05:41UTC，R786 index已在后载体；R790的146CM行07:22、R791 tangent06:37到期，R794 carrier不含它们。真关系发布即消费，临近到期只IO保必要旧输入。R809六C15:52、R78743016:25、R815425 18:33UTC到期；续算保最小bundle/完整current。详见[期限记录](notes/2026-11-15-R815-endpoint-and-input-retention.md)。全部源pins在各certified结果、[旧结果索引](results-archive-2026-11-15-before-R833.md)及上述归档。

## 真正全p缺口与已封闭边界

[R832](results/R832-original-height-explicit-uniform-contact-order-bound.md)已证统一jet界：G=(p−1)²/4，R=21G+4，ord Eij≤R−1+binom(R,2)(6G−4)，不代实际高度/(724.33)/整盘排根，不造巨大最坏窗口。R634逐盘非恒零已成；R616/726只给真β非挠/rank/log。R575真正CM根号负，逆twist秩零撤回。

[原Poincaré](notes/2026-11-15-original-height-Poincare-linearization-and-period-determinant-audit.md)9a54e844：U_i=c(a_iV_i−A_iL_i)，原Q点β非p/rigidification与零阶纤维保；同一第二类修正全函数相消。T_p仍指定degree d_Y+2 period多项式，线性AST不排；η^-不删切向。End⁰(G)=F、非零torus商维≥g+1，无几何幂等元低维捷径，未得高度非零。

sigma须同一primitive/Legendre h的三原单位；R739反例/R741与R737不同密度不拼。旧R808/810、p²/Hirota/固定六维支路闭，保[K,P_T]。R826/828/830/831八原源/两G零/真实conductor-p/old6不可约直接复用。R833/834源全局非零与SS/Serre-dual识别已成，指定uP0,e/配对仍缺，不代原CM值。

[新unitary交叉heat](notes/2026-11-15-sigma-unitary-cross-heat-and-primitive-source.md)173077d4保实际三同源/原36theta/full72及原整段FG；∇=D−M−∂z∂t/6−3Xzt/2，双向Frobenius/两边/角点全保。按整数差的原Legendre×primitive权W水平，指定FG/degree p+1源等于6⁶B⁷Σ原同h项，非零仍未知。μℓ只在共同jet作用，不称原36全局稳定；FG一次横向源零，不能用全向量单位替它。中央p12k+11/h6k+7自动primitive，但f_k/g_k/Legendre仍缺；Legendre关联j2048/3，非原j0，R706零g_N不反证中央。

ordinary p43/776bitq已Gaussian5排除。[Shapiro](notes/2026-11-15-original-Robert-Shapiro-second-class.md)337a9892、[θ-lift](notes/2026-11-15-original-exact-dual-theta-lift-and-shifted-cup.md)7388c4be保唯一K_glob/Θ=i a_q、同Σ θ3/共轭k；C4除T²杯积只复现R779，无独立数值/完整晶体，Θ未知，禁巨大q枚举。

R816/818/819/821/823的cusp/Hom/评价及R729充分大全p c1不分歧均已成，不添高度单位。R707固定p41完整129盘/八CM已闭；原模型/CRT6逆/ζ²一次/246/c0c1标记不改。主目标仍余R317的p2/5mod9完整非分裂正规化子、a³+db³1/p|b，D/bc无统一上界；原eta/beta、实际高度/(724.33)及全p证书未成，继续open.md。
