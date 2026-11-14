# HANDOFF — visible-flex-larger-amplitude

/root，visible-larger-public-resume-20261114，GPT-6 Astra Pro（AI辅助）。**未完成，继续完整大幅闭族及同g精化，不等阶段确认。** 历史细节见本日migration/recovery notes及Git历史。

## 授权、规则、现场

用户直接授权公开Rogerhu12/math-research-public的commit/push main及本仓Actions；旧发布阻塞已解除。只写公开仓；PAT仅瞬时CLI环境，不入文件/日志/提交，不强推。已读根README全部授权和14规则。每push前实际pull --rebase，非快进立即循环；至少每小时pull，每次检查根/本题README新差异并立刻执行，已读SHA末行记录。root独占Git/H/open/log/workflow，子线交冻结独立文件。
重计算只用本仓Actions（4CPU/16GB）；本地只读、源码、准备、压缩取回。Rule12完整证明直接results，不加独审审批门。H<10KB、md<100KB、数据>1MB gzip、单件<5MB；不写根LOG。
clone=/workspace/scratch/e959e57ee07f/math-research-public，本轮目录symlink到/home/agent/vl-e959，迁移逐件SHA一致以避共享overlay满盘。部分克隆/窄检出，禁git gc/maintenance；不对大树ls-tree -l触发全部blob，不删别人文件。旧B=/workspace/scratch/ffc1334c1988只读；已恢复旧公开clone全部43本地提交至e4e38a4f，R235–237及真RK24/RK48无需重算。
已读根README在ee26c0a65a2e63c15f2ccfba6714181584416542的新课题表与Rule1/13范围差异，本题README未变；之后每pull仍检查。PAT workflow_dispatch接口403，使用既有push request明确lane，不重复baseline。

## 完成标准

同一固定g的连通闭C²嵌入连续族；固定H含内点、diamH与实际像δhold均≥.2D；含反射商δE>0；全t reach≥.03D；全域metric≤1e−6；同g/参数/t范围精化至机器或原solver容差。D为完整闭F0直径，H可两固定帽之并。交数个<5MB网格并明确严格存在差距。开放前缀、设计代理、有限样点、小幅A都不足收尾。

## 真实大核与完整DN主线

主输入真.99：notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz，SHA b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff。M96/N1024、423节点、固定前3/释放93核，RMS5.45704e−7/BC3.47e−18；两档材料C² metric5.77368e−7、κ6.30138、G≈.960000980454、Dprefix样本3.50037，严格完整核rho>.1638501198935。不是闭面。
run43582043166/free3真接受.996/.9975，但材料metric4.60534e−6/8.08662e−6已超标；.997875真Newton RMS1.03996e−5/condition5.995e7且回溯失败，非仅预测失败。全部62件已归档（attempt03接受、06失败）；不盲加网格，仍以较好.99打通cut。
CompleteProfile从.99以AngleConnector/coast/原finitebridge接真实r=.3，s_end=2.271004035438285。物理状态完整3M+2（含z0），全部H96及core换角导数、c′=p′=0增广389维（左293/右96）。原QR/Newton/容差不变。
原690点warm：notes/public-actions-43582043166-1-coupling/preparation/prepared-compact.json.gz（3710347B），仅删重复alias，manifest可重构原JSON。节点和中点域通过，maxcol=.00711059，末点H96准确0，mean1.60408100852；**RMS两Lobatto点后来实测不通过，不能称全域有效。**
首完整DN run43584222071：690节点reduced condition7.153e17、linear相对残差.57657，无接受Newton步；SciPy插值878节点RMS NaN/BC.001964，非新H尾失败。690checkpoint未改；878pending不是改进warm。原FD Richardson max7.28036e−9通过5e−5门。R244证明圆形段紧支scalar控制是非均值设计核方向，有限投影是否精确有核另论。
新v2 prefix3 schema=complete-prefix-controls-scalar-profile-v2，3支持(.05,.30)/(.35,.60)/(.65,.90)乘原prefix_end，完整序列化supports/poly/p*/两源SHA；绝不以旧prefix/turn/coast解释新p。full_dn_prefix_controls.py保原690点，插新点用原analytic seed；加入实际RMS两fraction .5±.5√(3/7)域检查，真正QR后才记录SVD/近核/分块linear残差。
**request04/run43585737152/source085dcb54实际前置失败**：原690点有331坏RMS点，新696点仍331，加到1027有846，超max_nodes1200；未启动QR/新H尾/接受步。首坏s1.45441467、β²−.00337326，坏点均在taper_end1.2856后的圆形warm段。非舍入小负数，不直接加预算。request06仅circleprobe，以原真实warm/RMS报告比较同96核/同a的五组M/N、原RHS与真实Lobatto域；不重启BVP/tail、不称lift为接受。

## 真尾、接缝与冻结g

T96原g真zeroH/J/full audit已完成：run43582043166/artifact14109122474，notes/public-actions-43582043166-1-tailzero/zero-H-T96/。M96/N1024、深度8/576stage/577×192state/RK12/tol2e−9，真exit0/805.484s、resid0、metric9.992e−16/fullD0/minA=minD1/holonomy0，全部27840 J保存。tangent chart condition1.391e17；真mode96 slopeJ589.6397 vs ready587.3800，零残差不证J稳定。
seeded_zero_tail_client.py仅在完整bundle/config/source/ready逐项核对后复用exact零H且audit=False首响应，worker仍初始化核源；任何新H或audit=True走原真worker。run43584222071精确命中1次、无新H请求；独立J消费Darboux二阶相对差1.32053e−12、height I/mean0/模间0，ready与真shooting相对差.011685保留。勿重算805s零尾。
R239连续条件给均值唯一及单SE2后的六jet；有限DFT不自动付假设。新physical含z0，不再加旧A mean。原φ96可有无限θ谱；新complete_material_tail_packet独立入口严格认v1/v2并锁scalar源/全部p*/supports，只有真正接受fullDN和真实最终tail来源才消费。
large_core_saved_prefix/closed_assembly接口已发布：自己的完整mean、同一SE2、全角cut二jet差的Hermite修补，区分符号C²身份与字面浮点残差。core witness也随配准变，原G不能直接当新像幅度。真接受后workflow自动readout两级及自身tail closed all；当前尚无该新闭面。
R240：共同材料θ下g=ds²+a(s)²dθ²与c无关；设计定型后冻结完整a(s;p*)/尾帽g/区间/t范围，释放全部core，K0/k0/T=M，增广4M+2（左3M+2右M），同g升M。完整scalar必须先按原design维数/p*/supports重建再升field_modes；新M的H须实算，不padding旧H。Ntail>8M，M128需2048；新M/RK不能复用旧zero缓存。帽中心固定图册。

## 旧完整A基准、全t几何与精化

A仅旧小幅完整组装：G=.2506381129，Dcloud3.9774592667，Hdiam3.9695633777，九phase像点云幅度.2506381375=.06301463338D，未达.2。三mesh解压3745773B/73442顶点/146880面，Euler2/每边2面/零退化。点云/全phase消元不自动给连续空间reach。
原g全H32/RK24与RK48真solve/J/audit已成功；run43579782197完成RK48真16+源节点读出/共同网格/finitecollar/闭组装。24→48同f8二jet差7.03e−6，48f8→16差.0029138，未机器稳定；原prefixcut metric平台4.77033e−8未重解。外cut.01外metric降至2.07608e−9，finitecollar界1.00139e−18仅自己的原H和背景。
post43旧GW35件源/结果及原transfer已逐SHA恢复，notes/2026-11-14-post43-GW-recovery/；明确旧本地历史，不冒本轮Actions。GW是不同有限rr重构，旧f8→16二jet.0017739032174/κ差.0006781771仍不收敛；最坏在stage28 cusp附近。R245完整证明P=Q+ES、六jet锐界及共享C¹速度积分；Q只比较场，完整ΣE=0才保两端，不能继承旧g。run43586618658/gwcompat真重现rr差.0017739032174，有理shadow同值，消费端求值差仅1e−17；Q层差反升.00204906，不铺全场替换。原节点升序/降序已核，不存在半径不同的节点别名；下一核速度/二阶来源，无新ODE。
R238条件定理排含反射全等；R242精确warped度量+角解析时平面带迫使a′非零整数，不能套有限缺陷/任意C²极限。R243用真9245原节点/9246小段全有理非零见证证明共享C²四角规范形无平片；原renderer同一性/全接缝/δE仍须付。
R241参数块门同时排自交/瓶颈。旧A v2真D+=3.980751407764145、Ktau=.9994116104，曲率/标记和所有prefix-tail/cap/self已付；余33712prefix对。v3 q2剩1948；q4真剩328父对；**run43586618658/q8真付全部33712父对/2157568子对，uncovered=0，numerical_cover_budget_passed=true**。77.565s，同场/同包络未改；停止旧A可选加密，连续interval certificate仍false。held完整表面cover给δhold/D+≥.05388898465、H/D+≥.996873，正像变但不达.2；全连续包络假设仍按实际严格程度记录。

## 当前执行与保全

request05/run43586618658/sourceb96924e0两lane均success；原bot发布，回执在本轮actions-debug。request06仅circleprobe已备，同原失败warm做M/N短诊断，不重做成功baseline。实际q8解决旧A条件空间覆盖，GW诊断排除单纯消费端求值解释，主线仍完整大核DN。
旧post43 geometry26件和strong90件已逐SHA归档，各有recovery-manifest；均历史非新Actions。R246完整证明旧.984有限场三分量<1e−6及浸入，直接operator仅<2e−6，明确不付新scalar/闭面门。强支旧完整H审计已成，但R6因磁盘SIGTERM143无接受步；全raw前缀分块未全迁，原只读索引仍在manifest，不重启旧支。旧18分钟strictmetric不重复；新场需自身公式适配。
每结论普通pull/README差异检查/commit/push；非快进立即rebase到成功。公开源78件逐原91清单匹配，只读公开仓，无private secret。临时自有transport分支只帮助大blob送达繁忙main，仍普通push，禁止force。任何分项完成继续open下一项。

规则同步记录：2026-11-14T10:45:54.085441+00:00 实际pull --rebase成功；双README自8522706无变化，已读提交 5b8efcf6bd2f1c63d9a2508d9e8ba9a3e95dc545。
