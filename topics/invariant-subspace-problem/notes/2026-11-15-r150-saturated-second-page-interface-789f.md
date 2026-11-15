# R150：完整二次饱和来源的第二页执行合同

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。状态：执行入口冻结；本轮新第二页尚未运行。旧197列及selector均实际已完成，直接复用。

## 1. 对象与本轮范围

原矩阵A为6188个原来源、4367个输出及完整十七式。p=31，原模型仍为模p6=887503681，目标仍为p²h0T。已经证明完整二次饱和矩阵

$B=[A,b_1,\ldots,b_7,pb_8,p^2b_9,R_{2,2},\ldots,R_{2,198}]$

满足 $\operatorname{im}B=(\operatorname{im}A:p^2)$。本次计算B的完整root2局部第二页，保存下一页的完整原来源。

完整第一页源核剥离1834个精确B核及两个精确关系后，必须保

$\theta_1,\theta_2,\theta_5,\theta_6,\theta_7,e_9,\omega_3,\ldots,\omega_{198},te_8,t\zeta_2$

共204个初值。六个旧来源及te8的已知零类只作身份检查，仍保存真实高位。

先独立保存完整第二页，再依据实际像连续进入完整第三页或正来源恢复。本轮两个成功outcome均要求接续：

- second-page-complete-third-continuation-required：第二像未包含任何当前目标，完整第三来源核已保存。
- second-page-target-compatible-global-continuation-required：至少一个局部相容目标须恢复真实全局原来源，余目标继续第三页。

它们均不声称原模p6全恒等式或特征零结果已成立。第二页不充分的dual不被解释为杀死尚未计算的完整第三自由。

## 2. 同一整数carry和精度

[逐层证明](2026-11-15-r150-saturated-pages-integer-carry-and-nested-jet-precision-789f.md)给20→15→10→5。本次先支付到全部204个第二来源的10个有效系数。

从同一旧全局Q和原T96的G/V配对，把q1延伸到root2的20项。原2195和6188来源前10项逐项比较run43653360404的实际字节。

直接形成

$L_2=\widehat K-p\widehat q_1-\sum_{i\le7}p^{2-e_i}\kappa_iC_i$。

原A模p6全部20项乘回并验p²整除；除式前10项模p²与旧T完全比较。解原1034×1021系统的20项q2时，锁住旧全部1021来源的前5项：先核旧低5项身份，右端扣除该前缀后除t5，解余15项，再原20项完整乘回。原3333预基cochain和2195→6188运输均保留。

形成 $L_3=L_2-p^2q_2$，原全部20项p³整除实际核验，前5项D3与旧197真实除式比较。后层使用有形式完成保证的前15项。

按selector的 $\alpha_j=a_j-15b_j,\ \beta_j=17b_j$ 构成196个 $L_{3,j}-\alpha_j\kappa_8-\beta_jL_{3,2}$，再加 $t\kappa_8,tL_{3,2}$。实际七列纠偏后解15项q3并保全部原来源运输。全部198个新L4与六个旧K4一并按原A模p6乘回，逐项验15项p4整除，保10项有效余量；旧六列直接读实际原整数代表，不重旧VQ。

全部204列的前5项root2类显式补root1三项零，经完整原预基/G正规形，保143局部坐标和104自由检验，再映回315维真实torsion坐标。每次p整除都在同一个规范整数t系数表示中完成，不丢carry。

## 3. 完整下一来源核

从完整第二像选实际Krylov基，记录每个基来自哪个204来源及哪个s幂。T(s)为真实来源截面，C为204像坐标，J2为s作用，保存

$I-TC,\qquad T(sI-J_2)$

作为整个多项式来源核的完整生成集。每个生成式实际乘回第二像为零，完整性来自已发布源核定理。root2由t5消去，所以截面次数≤4、生成式次数≤5。第二像维r时保存204+r个来源，最多229个。

下一第三页读取这些真实原L4组合及10项余量，继续付q4和第一页基的原整数纠偏。不能只取第二像的常数核，或删除本页的已知零来源。

## 4. 精确格式

运行时spec是文本R150_S2_LOCAL_JET_SPEC_V1，保31、NT、L、ring和全部来源标签。ring=2为纯root2；ring=12只用于旧3+5项CRT。

- R150SP31：packed field来源，保原2195/6188行数、NT/L/stride、阶段、完成行、bound、64字节绑定、全部u16标签、每原行的id/raw/δ及位平面。
- R150SG31/R150SV31：同一G/V的20项，G列保实际主分量、度数、首系数。q3截前15项，仍核完整缓存。
- R150SF31/R150SQ31/R150SN31：原局部RHS、全部1021来源解、3333原预基cochain；动态NT/L和标签均在头内。
- R150SJ61：全部6188原整数source的Taylor系数模p6，保完整原row字典。
- R150SR61：全部4367原输出的真实除式，逐列保p指数。
- R150SD31：完整原4367行的field jets；纯root2和显式root1零的CRT8分别保存。
- R150SE31：同一820标准单项式字典下的全部204列。

15001…15198是196个ω、te8、tζ2；204顺序先7001、7002、7005、7006、7007、7004六旧来源，再加这198列。它们不是物理目标标签，物理目标仍2…10。

整数product用uint64，在每个原多项式项后模p6。每格约化前至多20个小于p12的乘积加一个已约化值，总和<2^64。不能改成p7后沿用此算术范围。

## 5. CLI与30个真实输入

    python3 notes/2026-11-15-r150-saturated-second-page-runner-789f.py \
      --notes-root notes \
      --t96-recovery T96 --all198-recovery ALL198 \
      --seven-recovery SEVEN --current-recovery CURRENT \
      --ninth-recovery NINTH --old200-recovery OLD200 \
      --third197-recovery THIRD197 \
      --selector-receipt SELECTOR_JSON --out OUTPUT \
      --math-seconds 300 --memory-mib 512 --compile-seconds 30

可加--resume-recovery OLD_OUTPUT/recovery。--five-recovery只兼容旧壳，可省略且不访问。本次30输入按contract逐项绑定sha256与bytes：6个旧artifact、完整197 recovery及主线selector，不重旧197/selector数学。

四个C++编译各30秒/512MiB；随后全部数学共用真实300秒时钟，每进程512MiB。Python继续引用已发布精确Schur helper。原G最高度8的高缓存项实际核零，复用零矩阵并省去零乘法；完整输出L项仍逐项乘回。

## 6. 真正可续检查点

VQ保真实来源累加数组。原source transport保H/RHS/backward/forward阶段、游标、全部raw/beta、双slot和逐片SHA。整数product保完整实际累加器、已完成原行及真实source前缀。normal保余量数组和cochain前缀。Schur保单位块、余式、全部解和原G验证计数。绑定采用输入内容、规范标签和源码，不把恢复目录路径当数学数据。

超时是未完成；退出0也不够，runner还核最后marker、必需字段、输出及哈希。所有真实checkpoint、stage-cache、来源和除式完整保存。大于十进制1,000,000字节压缩，每gzip片≤4,500,000字节，保整体重建SHA与逐片SHA。数学时钟之后只保存压缩。

## 7. 回执边界

主回执results/saturated-second-page-pipeline-receipt.json，只有实际全页完成才有：

- all204TrueOriginalSecondSourcesComputed=true
- completeRelevantSaturatedSecondImageComputed=true
- completeNextPolynomialSourceKernelSaved=true

本轮始终：

- completeRelevantSaturatedThirdImageComputed=false
- globalAllOriginalSourceMod31SixDecisionComputed=false
- characteristicZeroIdentityAsserted=false
- allCompatibleTargetsOriginalIdentityVerified=false
- fullOriginalAllNineMod887503681IdentityVerified=false

九个局部相容flag与标签独立保存，不作全局证书。完整下一源核及全部204真实整数carry使后继无需重算本轮。

冻结时只做了有界C++编译和Python AST，没有运行新第二页。实际数学由本次Actions回执报告；本轮完成后立即按真实像继续第三页或全局正来源。
