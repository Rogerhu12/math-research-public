# 交接

## 目标、授权与同步

- **未完成：** 普通复可分无限维 Hilbert ISP；全体有界算子的存在定理或完整反例才可收尾。子题完成继续 open，不停在阶段报告或时限。
- **最近成功实际 pull 与已读规则提交：** c92c240c393a8917e8364a3dede0acf0f9161390（2026-11-15 15:36:27 UTC，Actions run43730816689实际pull --rebase成功，两README无差异）。记录：notes/root-terminal-pulls-789f/43730816689-1.json。
- 仅授权 Rogerhu12/math-research-public；根独占 main/H/open/results/log，代理交独占稿。每结论真实终端 push；非快进即 pull --rebase 再推、不 force。至少每小时及每推前实际 pull，核两 README，仅读新差异，已读 commit 记此。
- 已读规则根 21bd547f56590b7f2dd279d0297efb289a9b2783、课题 4d6570e9cf346431ab781a1290076a6321aaaa00。token 仅 CLI、不落文件/日志。可重算矩阵/证书不存 Git/Release/大工件，不分块绕限制；仅源码、参数、run、SHA、小回执。topic≤200MB，API 小 UTF8<100KB；MD≤100KB、H≤10000B、open 尽量≤30KB、log 每条≤5行；数学美元符，不写根 LOG。
- 无额外审核门槛；Actions 约4核16GB/job≤6h/账号≤20，各计算预算自主具体选择。当前本地托管执行不可用，既有 Actions 执行真实 pull/rebase/push；不能拿 API source commit 冒充实际主线推送。

## 完整历史

本次压缩前全部来源、完整数值、未列缺口保[H 全文](notes/2026-11-15-handoff-before-fixed-test-row-and-small-local-e8-789f.md)、[open 全文](notes/2026-11-15-open-before-fixed-test-row-and-small-local-e8-789f.md)及其归档链；未列条目不算关闭。

## R150 当前已证

- 原 A 为4367×6188、泛秩4354。同选 I,J 各4354、总权8770、常数 Q/F31 秩4318/核36。完整前三连接3/9/3，第二24头/第三21头；[17条真第三 cochain](results/R150-appendix-seventeen-explicit-natural-third-left-jets-and-restricted-normal-four-completeness.md)经296072原产品；完整第四 β4∈[3,5]、λ4未构造，来项15缺2、第三21缺4。
- 同选 D∞≥130、cofactor/原来源换列∞≥125。K115=s66(s−2)9(s+6)12F+²F−²E8²，degree115/lc5^6为31单位；q8412…8525，非基/转移/目标费8569/8574/172，统一条件8574。**全局 h0 九目标 Q[s]成员性仍是前提**；同D leading31单位未付，真Q v∞130…243（等于243才单位）、degD8527…8640。
- [完整零谱及原目标](results/R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md)：β1…11=4,0,1,3,1,1,1,1,0,1,1，正谱1⁴,3,4³,5,6,7,8,10,11；δ66/次大55/max11，最后13自由头/965328原产品。旧13泛函与142+4212已给九平方原≤3来源 Q(s)像；现全九 s³t_j 在零点真局部像，t2消去理想恰s³。零子题关闭，不再第十二；末端jet非零不能否泛型像。
- 两端原全常数rank4340，各14正Smith。原完整∞首4/次0，[第三连接上界](results/R150-appendix-infinity-third-connection-one-dimensional-bound-order43-and-cost8663.md)已给β3≤1、δfull∞≥43/次大≥39，根已重新全文核对；不能把完整∞只记成首两页，也不能由zero谱搬运。
- [真实局部投影长度差](results/R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)：len T=δA−δP，T=W/(L∩W)、W=(I²)≤5；差≤e即t^eW⊂L。170原行+54g倍行局部双向生成，g零点只除η单位。E8²首项31单位先剥后给2点δA≤30。
- [负六完整局部闭合](results/R150-appendix-minus-six-local-smith-length12-and-original-nine-target-membership.md)：真P/full谱1⁷,2,3、长度12/次大9/max3，W全在原局部像，九目标无需s+6，已纳K115。实7.521673933秒/raw8191B/0039c5bd…。
- [2点完整投影谱](results/R150-appendix-two-point-complete-projection-length12-and-original-transverse-gap18.md)：原order4实4.637497190秒、全P常133/连接7,1,1，已达泛秩142，所以P正谱恰1⁷,2,3、长度12。full仍仅12…30，T长≤18；不证明h0一阶足够，也不否定九目标。高于3不再提高此P长度；转原W或九目标。实际回执见新session。旧order17超时只说明该次首Schur未成。
- [原Koszul外支撑扭子模](results/R150-appendix-koszul-outside-torsion-embedding-and-selected-minor-test.md)：O1834×1632常rank1603/29正指数；tors cokerO注入同B余核。Fp31 O最大≤21/总长≤243；Q总长≤Fp总长但Q最大不能用21。D≥δfull+σ、cofactor≥δsub+σ−amax、换列≥δfull+σ−amax；真Q δfull+σ≥243才付同D leading单位。新O数值尚未执行。

## 活跃计算、源码与恢复

- 旧 run43702348535/job132776011109 保全部大临时输入。session 数学循环约10:07:10起340分钟，到15:47:10才不再开新一轮；job硬截止约16:00:13。请求一次读取后的全部串行步骤继续执行，勿把有限job时限当课题停止理由。
- 原47步参数完整保 commit795c0306493c98aa0a04a11a2751b4cb0949709b 的 notes/2026-11-15-r150-recovery-small-session-request-789f.json（95791B，SHA0e276a814fb747c8c04758cb193529b6af0e4e0278ad24083883317d5ec82a1d）。当前滚动请求只有后继；新job须先真实恢复相应依赖，不能假定旧数组存在。无大数据长期保存。
- 真4318单位18 RHS 输入与旧14主元桥接已付。step49/50：从653续至1205完整digits/34946bits、18次重建未成、单位产品0；step50实1186.227843521秒/raw5290B/0514d6af8471fde6e6e04f57a56ac5b9085db5351a9d74e0b27d1a534021d539。binding2cd043a0fa006deb45f0811412adcd021fb1c0bee395215b812b3d8ad1c5a2af；active slot1 341404739B/eebf82c7…，全部精确 pins 见归档。不能把有限重建未成当无有理解。
- step53 同冻结源码/out续1800秒/4GiB/final仍在跑；原 native 预算尾只存完整digit、不自动尝试最后精度。新增step54 O有限域selector120秒/1GiB/degree21；step55最后实际完整精度独立重建180秒/4GiB，成功才显式 adoption；step56原final180秒；step57新完整精度独立重建120秒；step58原final120秒。原始 active/slot/nextrec 不改，所有新操作来源单独记录。已成单位则适配器明确拒绝重复、下一冻结final直接消费；不得把后继失败空报为数学成功。
- O源码44adf1ef…/SHA6db545a1fb6ccb518d8c057f69dfa6d96ac37bafec67053483040f1ad31d7a1a，真实rebuild目录 selected-natural-u-rebuilt，paid小回执26242B/e57d4bc5…；只算1603单位/29 RHS，不重原4318。适配器cpp5b5a69a4…/8d32e180…，runner883bdce2…/a9d26fcf…；根逐全文及原restore/reconstruct/冻结consumer审过，首次解析编译仍待实际Actions。
- 原单位解必须77724单位产品全真；随后全部4354残差18列、missing2第二/missing4第三及同29×81第四配对才可提升完整β4。旧第一、第二、normal4/5、第三17及所有原SHA见归档/历史request；已成大消元不重算。
- 新独立小session **run43729338969**，45分钟循环/55分钟job；request notes/2026-11-15-r150-local-projection-small-session-request-789f.json，无历史大输入。step1 two-original-projected-order4已成，raw8820B/9c965a0846e84cd6dc3e0302319da87c7cc7f1ed45933633b6190a66627dd5c4，source22889e90bc66c833bac107fb562f254c7cb63758。
- step2 E8原低51×36/正规表示408×288实外限205.0084秒退出124；3.623秒保存了全部224原嵌入、原数域单位及Taylor0…4身份，首Schur未成、phase空。raw11745B/c36cfc7531593ae4c2b160d79763c1e55b358bb189f6e79c93477bd3917c5975，source74cee438adbeabe69be29c661a6545a9c3499bb1；不是新谱或局部成员性否定。改真实小数域/原重复块消元，不盲重复408大RREF。
- step3/4 F±采用原低51×36/三次域153×108，分别90秒/1GiB/order4，源码8b8fe542…/SHA4956f0dc77aa9d16f064e65c4c803625fb221cd81c7f067aeb265c3bd96f07fd。根已核旧两域不可约、低rank25与泛rank27；h0各阶2/full长度上界8，低jet加4 exact核的注入保全224行，实际lower≥6才够局部h0。未预填。小回执目录notes/r150-local-projection-session-789f/。

## 原同w边界：当前真实联合缺口

M=kerT、N=closure BM、W=M⊖N，普通N=M未证。保同w、真u_Q、future、负前缀、完整核旗及自然MP域；ordinary λ、bare α、左μ不能互换。

- [同u完整返回](results/R271-appendix-same-top-sequential-projection-negative-form-and-complete-return-scalar.md)：c_j=−P_(p+j,j)u_(p+j)合法，u⊥整个K，μ_p²=−ΣRe〈P_j u,u〉；跨cut两端partial与内部完整和都保。真G=P_E(DD*)^−1P_E，不能换压缩后求逆。
- 固定R=d、h=2d、Q=L0h²的原误差一致；晚cut future落互不交global孔带，Σ||F_m u_m||²有界。若仅实际同u的合并负部≤c_m Q||F_m u_m||²且Σ1/c_m发散则w=0；允许c_m=O(m logm)，该上界尚未付。
- [原完整模型19/10负部下界](results/R271-appendix-full-model-row-occupation-cancellation-and-nineteen-tenths-negative-bound.md)：C*≥q^(19/5)/(4(x+1)³)，真E3负下界q^(19/10)/(4(x+1)^1.5)−1.5，二次尺度x^(23/10)。已排整个E_h统一QlogQloglogQ，未识别坏向量为实际同w；近线性窗/完整height未排。
- **新已证[固定测试交换行及双线性配对](results/R271-appendix-actual-fixed-test-adjacent-swap-row-and-same-top-bilinear-pairing.md)**：固定finite f同真u_f=(P_V−P_K)f，全部n及j≥x的Σ||P_j^-u_f,n||²≤8||f||²/x，无Q因子；任意不交对高反对称数r能量≤8/(rx)。同一u_w/u_f串链给完整双线性负配对，固定||f−w||≤||w||/8使各late cut左锚≥7||w||²/16。仍须控制真顺次MP合并算子作用于这个低交换能量端；没有把交换投影当顺次MP，也没有声称整个负谱被已展示暗对覆盖。
- 原G_reg同一Neumann forcing、X3输出/carry X7预算、正常有限秩相容链、Haar普通循环性及旧所有开放接口保归档。继续实际来源联合配对，不重做已闭有限分类。
