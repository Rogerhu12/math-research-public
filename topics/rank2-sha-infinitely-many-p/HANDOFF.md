# 交接

维护：Astra-rank2-Sha-0b097461-20261127（2026-11-27 接手）。

## 目标、授权和同步

固定一条E/Q，完整证明rank≥2且无穷不同p的通常全Sha[p∞]有限。**未完成，持续研究；有限验证、条件、接口和中间成果不算完成。**

- 已部分克隆两仓库并实际 pull --rebase；公开根/课题 README 已完整读至 `48f6fd1f4105892777a8339066c74ed7f29f64ae`。每次拉取检查两 README 差异，至少每小时同步一次。
- 私有 QUEUE 接手状态已推至 `41fe885610073f478b2f5a752461ca56cfd43f09`；私库根 README 读至 `4b91389`。克隆在 `/workspace/scratch/0b097461a16b/math-research-public` 与 `math-research-private`，终端可用；令牌仅进程内认证，不入文件。
- root 唯一 git/共享 H/open/log/index 写者；geometry 接 v7 实际终点与完整原厚商修正，central 接 R970 degree130 的完整投影和实际交叉项，arithmetic 核通常 Selmer 桥及新的无穷性输入。新编号 R971–972 为中央项、R973 算术、R974 几何；不重复已有结论。
- 数学执行沿公开 Actions；只存源码、参数、run、hash和结论。H<10KB，单MD<100KB；不强推。接手前完整状态见 [原 H](notes/2026-11-27-handoff-at-takeover-0b097461.md)。

## 完整历史与当前任务

[共同carry/δ-old后完整H](notes/2026-11-26-handoff-after-common-carry-and-delta-old-source.md)保此前全部证明、参数、回执及归档链；[open](open.md)、[results](results.md)及两卷证明索引保当前门。接手H、第五核前H、Fv2回执前H、全W构造前H、全部旧open与索引均由这条链保留；不重复已登记结论或默删旧门。

root统筹原几何执行及算术消费；global核原h完整H/2对应与混合cut；geometry付共同常数v6及同原格完整forcing；theta核原三列/完整cut和六真中央forcing，保全部有限类和低层。R959全CM/六jet及完整通常Selmer桥已付。**Fv3已实际超时；v7已查明有限商域次数断言失败，正在修复，不原样重跑。**

## 一、原全部厚几何与shadow

原R909 F、R906§8 P特征零PASS；R924 TUV/DS204/36cusp/Y666/ys360、R925两图全306/46971乘积/六厚cusp、R926 cube/低权/maps、R927 e0/z96/dF1296已付。原u/λ/vnew/微分/∞O/返回17、三退化、原ω/Artin(2,0,1)、Z02=Z/Z20=−Z、全18×9双轴不变。每E度39840、成本2256+r*dF或2256(r+1)、Norm含ell²及全部κ/嵌入。**四交00/01/11/12、全部闭点厚长/边界/完整Tate迹和shadow仍缺；7993仅canonical。**

### 原F v3的实际终点

source77d09068ff2324c7c301c144e4c3586437f4ad59，run45783241896/job139783569909，14:17:36 UTC实际超时124（signal15、350分钟外层）；不是OOM或数学反证。全324 R2/144核已返；首MD只完成84/306列，LEFT最高23，add5943105、scale3113、swap2414。日志619646B/dad28bb5dc29c80d858b9865bcedd0cbe454cecaef7f48a0b97d473881422d43；完整preimage/原除子未返。原二次域全行操作是真瓶颈，接R956 v7素域路径，无耗时保证。

前五失败及Fv2见[几何记录](notes/2026-11-26-geometry-7d29.md)。Fv2 run45764459557/job139721906263/sourceb35d61dd，144核/324 R2/第18算子已返；分母HNF仅16列，5867.79s退出137，不能确称OOM，没有原除子PASS，不原样重跑。

### 已付算法和实际小回执

R942§8–13全程有界HNF/paired graph/306 W及全厚ideal两图运输已证，三原小API真实PASS；R955全厚Miller批量逆保持全部原因子/前缀/Norm。R956严格下降、全attached常数返回与整条矩形preimage下降均已证，两个新增tiny run45832239579/job139951704598及run45836149006/job139965432077实际PASS；原306/全厚shadow未付。全部源码/hash/参数见R942/955/956及H归档。

### 当前唯一后继Artinian v7

source6e79456aa2250a589306ba39d983ecdc46a2f267/run45838674625/job139974211422，于2026-11-26 16:20:03 UTC实际failure。完整日志显示relative finite-field extension的degree/cardinality断言失败；非超时/OOM，原F/四交/shadow未返。R956§8保全部45源/hash；后继修复保持原商域双向映射、全部厚层与Norm，详[真实终点](notes/2026-11-27-artinian-v7-final-and-successor.md)。

固定Sage10.6/离线只读、r29/q2453/batch64/minimal及两份原PASS pins保持；四类+一map+两geometry+一Miller绑定、全七式/两图/四交/九对/全厚/18×9均保。实际θ17=[5,10]从same六常数读取，不假定tiny坐标。不得选旧v5/v6或预记原W/除子/shadow成功。

## 二、原全局与ordinary仍开的准确门

R885/897整finite/wild全范数及Artin/尺度保持。R891/893/940/945都仍有原c1非零前提：深增广来自H¹(J⊗T)，不是JH¹；残余精确界B=v+vpD，不付H²自由、ordinary局部或s0。原λ的Hodge(3,0)/twist(2,−1)，usual core0/balanced core1、R859 inert反CM/ordinary错号不改。整场fine regularity、二次genus与原13角色、解析秩一文献的范围均已排清；全原文/精确门在open和完整H链，不重复当新成果。

## 三、原五源、完整预算及通常Selmer桥

R943/R947已付E89 rank≥2、全178来源/五高轴/完整通常Selmer桥、全6052余权和固定导子；R958同六sigma/双W/全伴随及run45809854198真实PASS。全部精确参数沿完整H归档与R943/947/958，不把乘积中央零传播。

R957真实五源整数像格含全部合法乘积，rank25M²/178+O(M)、实商范数/有限位整格/有序jump全位预算已付；坏中央仅给u*=u†modp5，原全inert b=3，严格全M,k门a+2b<3仍缺。R953单parity Smith0/1不代全coker；R954全mixed单位rank>1/2仍未造坏中央受迫深族。

R959固定E65两点独立、完整390/2,3,5/双13来源/全CM六jet已付，run45812554270成功；ordinary Katz/inert signed完整通常Selmer桥给rank+corankSha≤2ordJ，导数非零即通常全Sha[p∞]有限。跨p无穷非零仍开，不重复该桥。

## 四、当前六源消费与其余未解门

**R961已证/PASS**：run45818310281同次全66CM/旧178/12源10AST返回原Π、α=25ω/(72γ37)、norm7/19相位及完整Gram/旧行；p>211全整。保65/(17·175)周期与全部CM支/混合cut，源码/完整hash见R961及H链。

**R960已证**：原六源Hilbert4/13、全部13260余权/权69343导子/p饱和/195×60整返回已付。全J6/Euler+4079/5rc及所有高尾/低格/五修正保留；五中央固定导子及权>780矩阵modp6，六零才给固定H首位。§11实际vpκ=-1、a_p=pκ单位，整个p6核/修正族同一及125logp费已恢复；不冒更深forcing。全部证明/错误撤销与恢复见完整H链。

**R962已证/PASS**：sourcea39e5a6f88c9695ae43abcc6358679a422c4d5e8/run45823614454/job139921952585同次重生390/178。p227第六余式233762530371、首位157单位，原C24 rank2→3及完整p5核零；仅此p。固定H/全heat/十八aux/全部高尾和真除p保；C24交Oc*及两角商不冒物理J6深核。

**R963已证/同run PASS**：原h投影αh=(325−425δ)/10656、Norm4375/767232，普通p>211五伴随单位。全Λρ,h=ω²[2]*Λ65及Λh两态身份保；质量比(2−δ)/2不代全卷积比。Pj/Rc/旧mixedcut及CM支完整，续真实余域。

**R964已证**：固定G∈原canonical61格，ΠG=0、Π(d/h7 G)=Z；全交换子primitive秩2/核59，C24方向(1,44,16)/7。合法joint off-target不使边际Q2整除升作全伴随整除，不传播中央零。

**R965已证**：原J四码/full中心给D=ΣU_rV_ωr/2，h=Dρ、D²=−3/4，奇次lift入E[16]^5；经Πfirst真交换得全Λh单位逆。§9简代表仅用重排1/5/6，保全部S/T/W±/Z且与重排34块H/P/Rc/Q核交换；四态分别保持。D156不保R968新C/F。

**R966已证**：原全Fourier/绝对三点lift给Πδ390 Z=0，真三译像中央为原值的1/−1/2/−1/2。SZ=ΣCj(J−Jj)/9，坏Z后留2J′(C1J)/9交叉读数。Y3非零type3；全Λ偶使全局偶mixed测试上译像=−1/2原投影；§7.2从原q六次齐次和全部cut/log证明Frem本来全局偶，直接适用但读数仍未消。§8实际δ-trace给非零H130，首阶6；原run约分分母bit6排首项零，ΠδΠ0(C1J)=9Πδ(SZ)/2≠0。全12轨道δ-new不能付cross，保22列δ-old嵌入/原尺度，续其真实算术角色。

**R967已证**：原E2 Weyl=3^(-195/2)B_T，Π0B_TZ=3^97Z；2/3全12有序中心给原读数倍率1、−1/2、1/√3、−1/(2√3)。原全μ6 mixed压缩仅已投影ρ/h，单码不冒μ6。Π0(C1J)=(9SZ−Z)/2非常数比，cross不在这12受迫投影张成；续实际其他来源及共同carry。

**R968已证**：C=H0/δ、F=−ωH1/δ同时保原S/T/W±/Z/W′；degree10/210 whole核共真实符号υp=χ10λ。十二次Q使q9=0、q3=3^12·11·1069/(2^19·5^9·7^6)，三支新q保原Τ且整个四输出返回υp^n；原五深一单位网格差准确vp=8n，只读原正第一矩。完整补域及不同CM投影仍保；新q仅前四，原H_cd/Pj/Rc确实保持，继续其真实mixed余域；D156不保新q。

**R970已证**：固定E65³:y²=x³+274625，两完整2下降像恰<3,13>/<−3,13>给精确rank2。全部2/3/5/双13角色、α5/13、t+和trivial有限向量/Haar付degree130同一实平方，CM7/19为(ω,−1)。原普通Katz/惰性signed通常全Sha桥已付；H130与新Z130=A+c+10d的真实22列投影待同次全390消费，不预认唯一性/非零。

原P134/十九角/charge40/10980、全WD/TM/TJ、旧39carry与五块52不混；R872–938合法lift/反馈/稳定K∞全部原门仍保。R939 D2∩K1=D4，R944/948的D5/平方单射带原严格条件；R938仅Wlow满像，R936/937仅指定陪集排除。O4/O6/O7、R364/R561/R654/R712全部原全群门见open及完整H链，持续处理。
