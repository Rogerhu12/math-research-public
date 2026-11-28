# R792 / Run55：原R787同g的完整中央柱、真实两端闭合和剩余整肩

会话 Astra-larger-e4e2a2bf-20261126。ROOT全文审查[29974B完整证明](../results/R792-full-width-rectifying-centers-and-complete-shoulder-boundaries.md)、[32源完整交付](../computations/R792-run55-full-width-centers-and-complete-shoulders-launch.json)及四新Python/工作流；全部三身份核同，28个父逐个等于已发布最终R787等真实源。这里正常启动全部四原研究，actual run/PID/数值未预填。

## 严格正向范围

仍使用R787固定长左壁、真实2^-16预载、原所有曲帽/标记和[0,.90]，不更改初g或以更宽的新材料逃避原目标。真正右区间从原U转角1.15到下板x=.30，左区间从下板x=−1绕整新长壁至上板x=−1；所有右握mark支撑留在固定补区。先按预载后真实曲线长度S重新参数化，两整轴向宽均|y|≤.88。

对每条整个矩形，真实框架满足gamma′=T、T′=kappa N、B′=−eta kappa N，令S=r+y eta(r)，F=gamma(r)+y(B+eta T)。当.88||eta′||<1时该隐式坐标在全宽唯一，准确Fs=T、Fy=B，故三个Gram在整个矩形为(1,0,1)；六jet与唯一非零曲率kappa(1+eta²)/(1+y eta′)都从同一位置式导出，未只解两条边。

每个真实区间内都有预载恒定、非零常曲率的原完整圆弧。三个不同站位的曲率扰动、三个eta扰动分成两个互补三维空间，各转为(1,cos alpha,sin alpha)独立列。改为足够窄但固定正宽的平滑扰动后，真实六维末端位置/旋转映射Jacobian可逆。IFT给原R787指定上下板不同刚位姿在一个正相位区间内的实际完整双侧等距柱，含整握和所有端jets。保持kappa原符号的族也有同一局部结论。不借IFT声称能达到宏观.90。

在两原roll入口，真实中央场与R787 guide之差乘一真实C²窗口，以y=sign[B+e tanh(u/e)]延出，u=0匹配全部六jet；在原quarter末段之前归零，完整原末领与两帽保持。原四平板的差在全部宽度为零，继续准确g；其他肩部三Gram必须实际收费。小相位时整个guide C²接近原闭嵌入，利用远点有序弦和近点统一二阶Taylor两种情况，reach下半连续性与原严格余量给某个正相位全壳reach>.03D。它不证明宏观末相厚度或继承R787 guide原held。

局部真曲入口上L不为零且各实际片解析时，N=(K detg+M²)/L给固定g的Gauss–Codazzi真实非特征Cauchy解，匹配中央整曲线/frame/六jet；紧内子区间有共正宽。该结果不跨kappa=0、不是全圆周共宽，更不支付整个roll到实际帽边界。R794另行处理的整周方向不混入本55。

## 每个有限计算都是真正闭合位置及其导数

真实左右末端分别解三平移与SO(3)姿态，九个旋转矩阵残差约束同一三自由度旋转，并报告实际六维Jacobian奇异值。相对框架按真实初弦与SO3指数中点推进；真实left Jacobian把每步旋转对后续全弦和本步半弦的导数完整累加。原材料的每个钟转点、预载支撑交点都进入积分划分。

eta的三次B样条真实导数控制系数用八次范数缩放，保证全宽1+y eta′正；每端四个零系数留真实开邻域原控制。返回控制的解析公式曲率包络与实际物理样条曲率分开，前者不能代后者。实际弧长C²标量样条若用正Bernstein速度备选，也由同一物理场计算全部g，不偷赋原弧长单位速。

真实gamma/母线用C² quintic及全部节点一二导数表示，隐式r含两阶导数。采用同层零控制样条作差后加准确初位置，所以time0仍准确原g。若终姿态未解准，以真实每端a0+y b0、a1+y b1、a2+y b2残差构造端部向量quintic，在.24l/.76l内边归零。闭合修正实际加入位置并完整求导，原射击残量/最大修正jets单独报告；不把修正后的非等距面沿用解析等距曲率。

每中相先取邻控制词均值，再按该相真实钟/端姿态重新构造、求隐式坐标和闭合修正；独立复读用两倍中央积分cells。即使native射击返回，也仅证明该数值流程返回，不是大幅完整等距存在。

## 原全部科学预算

四原独立进程：signed-rolls-gram、signed-rolls-shape、open-whole-gram、open-whole-shape。signed保实际闭合中央、整帽/末领/四平板，仅在两完整曲肩三方向修复；open还释放非握中央、两全帽和共同入/出口的三物理分量。所有自由帽使用最终R787真实polar inverse二jet，共用物理系数。各有Gram主目标及增加曲率/支撑/面积/分离代价的原shape目标。

| 层 | 原中央cells | 独立cells | 每侧kappa/eta各自由词 | 每侧原max_nfev | 原whole fit角/径 | 原whole nfev/LSMR | 独立角/径 |
|---:|---:|---:|---:|---:|---|---|---|
|0|160+全部真knots|320+全部真knots|9|70|24/6|12/12|64/12|
|1|320+全部真knots|640+全部真knots|15|110|40/9|20/16|96/18|
|2|640+全部真knots|1280+全部真knots|23|160|64/12|30/20|144/26|

原积分16/24/32阶、角/径物理基6/3、12/6、24/12，七原拟合相0,.15,...,.90与六实际中相不减。每分支每层各有一完整双侧13相shoot、一完整13相guide、一完整13相独立whole fit，共36完整逻辑报告；全部13图、两真端、所有三Gram/全operator、曲率/支撑/面积、带号体积、真实六jet接缝和held样本。保原R787七chart全球路径图及首末21类不同内部对，原控制字留runner并公布完整长度/SHA。

公开ubuntu-latest、Python3.12/numpy2.2.6/scipy1.15.3、四PID各BLAS1、原355min。32源冻结triggerSHA，每2700秒真实pull/rebase及双README差异/每次提交写ledger/HANDOFF；原失败与全部自然返回保持，拒推立即重新合并再推。发布前ROOT只给workflow含冒号的完整name加YAML双引号并重签清单；无科学参数/算法/预算变更，也没有额外fixture或准入运行。

## 完整发布件身份

| 完整路径 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| results/R792-full-width-rectifying-centers-and-complete-shoulder-boundaries.md | 29974 | 526f289da3dac462a480dab95eeb36c35da62a0e5637a51922483a630d221eee | 0d4b242837928280c848cd2bc54322fb76ac92da |
| computations/R792-run55-full-width-centers-and-complete-shoulders-launch.json | 14883 | 75474b30f80ccc5c5b097937472fb70d7fb131e25f97ef65100b93c3639c9a20 | 0e5f363f971b23ae2dcc2344005784552dca4d0c |
| scripts/resume_20261126/r792_full_width_rectifying_center_shooting.py | 8568 | 0743cecbf2d9042b86315a59daeac4203d690d84b3cc2f132ad24bb90dfb6adc | 759580efc2a72a8ce29b0483c3c3ec6515a38f43 |
| scripts/resume_20261126/r792_rectifying_central_cylinder_and_complete_closed_shoulders.py | 5395 | 3508ca268173e5ac7099f48d09b4be8090cc4b8ce6f728b944113984f52f8f36 | acce4f81b67ccec0f56524ef46acc08e176711df |
| scripts/resume_20261126/solve_r792_full_width_centers_with_complete_shoulders.py | 8189 | 179abd288f627911679adabfc6abc3bae5f477a4803215a958df9aacff51d80d | da369367a225a4accfd5ce3d901ce548b986c6c6 |
| scripts/resume_20261126/run_r792_rectifying_central_cylinder_complete_families.py | 14907 | c7e7281c88b6a9b416b682a107a958195efa04461e3f7272a75e89cf435240a6 | 362a8e9429e7f9052c3656b906ecdf87a683938a |
| .github/workflows/visible-larger-r792-run55-entire-rectifying-spheres.yml | 6523 | 00ec3f4a21e1fe7f54a5661f8bf3d1ec1bbb71025c8ac1ae08db7cee2ac37f4d | 052656eca97ffb63129cc8353e41d890fdbc4fde |

原28个完整父的长度/SHA/Git与全部实参在完整交付，含最终R787六个实际源及原控制器。全宏观区间两端射击、两整肩同g、全部时刻全局reach/嵌入、held与商距仍待同一最后解支付；固定输入精化至机器/原容差及完整mesh责任继续。root此次为云读发布，非git pull。
