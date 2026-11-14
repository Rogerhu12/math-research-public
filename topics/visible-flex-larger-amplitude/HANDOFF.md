# HANDOFF — visible-flex-larger-amplitude

/root，visible-larger-public-resume-20261114，GPT-6 Astra Pro（AI辅助）。**未完成，继续完整大幅闭族及同g精化，不等阶段确认。** 历史细节见本日migration/recovery notes及Git历史。

## 授权、规则、现场

用户直接授权公开Rogerhu12/math-research-public的commit/push main及本仓Actions；旧发布阻塞已解除。只写公开仓；PAT仅瞬时CLI环境，不入文件/日志/提交，不强推。已读根README全部授权和14规则。每push前实际pull --rebase，非快进立即循环；至少每小时pull，每次检查根/本题README新差异，只读差异立刻执行，已读SHA末行记录。root独占Git/H/open/log/workflow，子线交冻结独立文件。
重计算只用本仓Actions（4CPU/16GB）；本地只读、源码、准备、压缩取回。Rule12证明直接results，不加独审审批门。H<10KB、md<100KB、数据>1MB gzip、单件<5MB；不写根LOG。
clone=/workspace/scratch/e959e57ee07f/math-research-public，本轮目录symlink到/home/agent/vl-e959，迁移逐件SHA一致以避共享overlay满盘。部分克隆/窄检出，git gc/maintenance禁用；不对大树ls-tree -l触发全部blob，不删别人文件。旧B=/workspace/scratch/ffc1334c1988只读；已恢复旧公开clone全部43本地提交至e4e38a4f，R235–237及真RK24/RK48无需重算。
根README在ee26c0a65a2e63c15f2ccfba6714181584416542新加new-mechanism题，Rule1/13改为表列所有题；已读差异并适用，本题README未变。之后每次pull仍检查。PAT的workflow_dispatch接口403；使用用户授权的既有push request触发本仓Actions，须显式选lane避免重复baseline。

## 完成标准

同一固定g的连通闭C²嵌入连续族；固定H含内点、diamH与实际像δhold均≥.2D；含反射商δE>0；全t reach≥.03D；全域metric≤1e−6；同g/参数/t范围精化至机器或原solver容差。D为完整闭F0直径，H可两固定帽之并。交数个<5MB网格并明确严格存在差距。开放前缀、设计代理、有限样点和小幅A不足收尾。

## 真实大核与完整联解入口

主入口仍真.99：notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz，SHA b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff。M96/N1024、423节点、固定前3/释放93核，RMS5.45704e−7/BC3.47e−18；两档共同材料C² metric5.77368e−7、κ6.30138、G≈.960000980454、Dprefix样本3.50037，严格完整核rho>.1638501198935。不是闭面。
run43582043166/source8fa6b3f3b5365bfffd674cdc04f7d77519fa0d76的free3又真接受.996（430nodes/RMS5.45702e−7）及.9975（432nodes/RMS7.01923e−7）。但两者材料metric为4.60534e−6/8.08662e−6，超过目标；完整core rho>.1625537865/.1592190025。最后.997875真Newton未接受：688nodes、RMS1.03996e−5、请求再256>900、reduced condition到5.995e7且回溯失败。四次中间仅预测正性门失败，非新接受。notes/public-actions-43582043166-1-free3/已逐SHA归档artifact14109068159全部62件，最新接受attempt03，attempt06必须保留为失败。详见free3-09975 note。
旧固定32核.99 run43579782197失败和旧.984接受点仍完整保存，不冒新接受、不重跑。当前优先用较好.99初场打通真实物理cut的fullDN，非盲加normal分支网格上限。

## 完整标量、原g真尾与同材料g

CompleteProfile用AngleConnector/coast/原finitebridge从.99接到真实r=.3；完整s_end=2.271004035438285。3个内支C² scalar控制不改入/出jet。full_dn_boundary/augmented/solve用全部材料H96、完整core换角导数、c′=p′=0增广389维（左293/右96）。原QR/Newton及门未改。
run43582043166 coupling真实RHS在零控制逐位相同；690节点θ圆warm域已通过，无补点，maxcol=.00711059，尚非解。已发布notes/public-actions-43582043166-1-coupling/preparation/prepared-compact.json.gz（3710347B）；仅删完全重复alias，manifest可逐字恢复原JSON。末点H96准确全0，原mean=1.60408100852。warm重启精确保留旧节点，禁止插值噪声破坏零缓存。
BC原FD粗步5.04965e−5略超5e−5，半步1.26187e−5约四倍收缩；新增第三步/Richardson并保原门，待Actions真执行。完整DN已准备通过mainline request02的push触发，待核实际运行。
**T96原g真zeroH/J/full audit已完成**：run43582043166 artifact14109122474，notes/public-actions-43582043166-1-tailzero/zero-H-T96/。M96/N1024、物理深度8/576stage/577×192state、RK12、原tol2e−9；真exit0/805.484s，residual0、metric9.992e−16、fullD0、minA=minD1、holonomy0，全部27840 J保存。未用零解代数跳过variational。真实tangent chart condition1.391e17，mode96真slopeJ589.6397 vs ready587.3800，不能把零残差当导数稳定。
seeded_zero_tail_client.py已对完成bundle及本批coupling ready/config/source逐项结构核对PASS（SHA a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776）。只复用准确零H/audit=False初响应，当前worker仍启动核源；任何新H或audit=True走原真解。环境VISIBLE_FLEX_COMPLETED_ZERO_TAIL_DIR指上述zero目录。zero_tail_response_audit.py待Actions消费原J，不再求零尾。
R239条件证明：同完整高度/非均值斜率、连续正分支与turning number决定均值，单SE2及同Darboux分支决定六jet；有限DFT不自动付假设。新prefix已含物理z0，不得再加旧A mean；完整φ→θ谱不限96，接缝必须真正核全角。
R240证明共同材料θ下g=ds²+a(s)²dθ²与c无关。真实设计后冻结完整a(s;p*)/尾帽g/区间/t范围，释放全部core，K0/k0/T=M，增广386维（左290右96），同g升M=T。帽中心用固定图册，不硬延非线性角变换。
旧.984材料谱N4096/T96高度C²截断.00253633，T768约5.92449e−9但仅一网；原φ96不等于θ96。此处非物理上尾cut，不能据此移植新cut结论。

## A的已完成基准与全t几何

A仍唯一旧完整小幅组装：G=.2506381129，Dcloud3.9774592667，Hdiam3.9695633777，九phase像点云幅度.2506381375= .06301463338D，明确不达.2。三mesh各解压3745773B、73442顶点/146880面、Euler2、每边2面/零退化。有限空间与全phase消元不等于连续空间reach。
原g全H32/RK24与RK48真solve/J/audit已成功（resid8.36178e−11/1.67236e−10）；run43579782197真实完成所有RK48真16+源节点读出/两共同网格/finitecollar/闭组装。notes/public-actions-43579782197-1-rk48/reports/已发布；24→48同f8二jet差7.03e−6，48f8→16二jet差.0029138，未机器稳定。外cut.01外metric2.16149e−8→2.07608e−9，原prefixcut平台4.77033e−8未重解。finitecollar全域metric界1.00139e−18不代无限尾，也不移植新H。
R238条件定理：非平面局部胚识别四个不同支持圆及仿射独立圆心，排含反射全等；实际A前缀2589片/标记代数已过，tail/collar仍需同场。R242已证精确warped度量+角解析的平面带迫使a′非零整数；|a′|<1排除，不能套有限缺陷或无解析控制C²极限。
R241完整参数块门同时排自交/瓶颈，给reach。v2真实D+=3.980751407764145、Ktau=.9994116104，曲率/标记和所有prefix-tail/cap/self已付，余33712仅prefix-prefix；法向锥付392296对。v3仅失败父块角分2，原同PPoly/mean真评价子中心，待Actions。held-Hausdorff消费者用同闭包的完整活动点/半径cover及整帽盘距离，不用材料点位移冒像距离。
原RK48完整9245节点的四角原字节已抽取并逐hash核，notes/2026-11-14-public-RK48-cardinal-tail-packet/；exact-cardinal消费者待Actions。它定义共享nodal C²规范形，与旧rounded表示的差异需付，不冒全等结论已完成。

## 紧接执行

逐结论普通push并保持本H最新；取回包有失败仍保原日志。request02已设精确push lane选择，运行geometry v3、cardinal、coupling（含新FD/zero-J代数消费及缓存零响应的真完整DN），不重跑已完free3/zeroH。新真实coupled field后做完整六jet/实际角谱/C²闭组装/大幅见证/全t覆盖；设计定型才固定同g精化。任何分项完成继续open下一项。
原publisher缺identity已修；遇README变动正确退出保artifact，由root读差异后归档。公开源仅78实际消费件，逐件匹配原91清单SHA（12未迁移MD+1未用client排除），只取公开repo，无私仓secret。临时传输分支仅上传本题大blob帮助繁忙main普通rebase推送，成功主线含全部数据，禁止force。

规则同步记录：2026-11-14T10:13:01.114821+00:00 实际pull --rebase成功；双README自5810723无变化，已读提交 371edd6ded181f3e3045c6101b9fab26d4fe4c5c。
