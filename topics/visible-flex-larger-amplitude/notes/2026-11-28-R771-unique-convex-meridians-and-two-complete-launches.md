# R771 — 全经线唯一正凸坐标与两支完整球面实验

会话 Astra-larger-e4e2a2bf-20261126；同R764的一个初始完整固定g，E=.44、B=.88、原corrugation=.0025，两真实退幅.30/.42。[完整证明](../results/R771-unique-positive-meridian-coordinates-and-rigid-quotient-width.md)与[全部18源/参数/工作流清单](../computations/r771-complete-positive-convex-meridian-launch-inventory.json)是本条的完整输入。原R769已正常发布 `729d75a549fddd6033dfe2b7bc5c2778457f7478`；R771独立冻结自己的触发提交，未借R769未来数值。

## 已付的数学范围

整meridian长T=E+.132π/2+.0005，真实两端各保.0005/.001开领，不硬钉原中间E。所有目标弦≤T−.005；扣固定领仍有≥.002严格余量。对任意有限的两横向多项式形变，完整凸泛函在B≥0上coercive，B=0处右导数严格负；固定两端不共线令内点Hessian正定，得到全角度/全相位唯一B>0的根。用实际V而非奇异Q作微分，真实水平终端也正则，隐函数给全C²/周期根。单位整经线和真实目标端点准确，两个固定领保原whole二jet；未饱和角域及完整共刚右域的实际终领/帽保全g。B为凸坐标正参数，不是统一正速度下界；物理经线轴向位置|y|≥.88，速度可趋0且末切处为0。

本规定的端点保持族整像held≥.88>.2D0、固定握≥1.40，D0<4.386；初reach≥.132。退幅.42时初始整像任意方向width≥2.13，末整像y-width<2.067，故含反射的全E(3)商Hausdorff≥.0315。这个整体宽度论证无需借用标记或体积；**不证明后续嵌入/厚度**。剩余gss/gsv、角域交叉、被饱和帽部和后续全三维自由修正须真实支付。

## 完整实际输入和原预算

两自然进程各先跑全可行angular形变，再独立读完整连续物理jet，随后跑同固定初g的十一图三Cartesian自由修正。正经线根每一实际s重新求解，p_s/p_ss由同3×3隐式Hessian导出，未用插值根冒充连续解。可行预处理的相邻角离散Gram与高阶真实jet是不同离散方程，以独立真实回报为准。

三可行层(角点,横向各纵模,每整roll细分,Gauss,nfev,LSMR)为(32,2,8,3,10,24)、(64,3,12,4,16,36)、(128,4,16,6,24,48)；两个横向channel、边界±3，curv/.l2/角差权.035/.0015/.001。原全场三层(训练角/径,物理阶,修正角/径,nfev,LSMR,独立角/径)为(24,6,16,6,3,12,12,64,12)、(40,9,24,12,6,20,16,96,18)、(64,12,32,24,12,30,20,144,26)。每层完整0,.15,.30,.45,.60,.75,.90七相（零相直接原场）、六中相；原grip mask保留，正负端自由修正独立。凸坐标原Newton36步×14线搜，必要时有界192评估完整fallback；全部moment残差、正参数、Hessian谱和真假缝费用保留。

每支每层三类原报告：feasible、全连续geometry、整球stage，共两支18个完整逻辑报告和一个索引。真实whole Gram算子/三个独立分量、曲率两号、面积/支撑、held/真实E端弦/两头与帽缝、体积、实际系数与源输出whole hash都按完整报告保留；逐点和f64只在runner。保护的终端区域不能为自由修正结果免检。

ROOT读完整证明、四个新Python源和完整workflow，并核18源身份/引用；稀疏相邻角Jacobian和隐式jet公式与原真实全场检查分开登记。新workflow直接触发实际两支，不加入口fixture/数值准入，不缩任何层/相/变量/预算。Python3.12/NumPy2.2.6/SciPy1.15.3，两个独立单线程进程，355min只是job上限。至少2700秒真实pull/rebase，双README变立即照新规则停止旧源继续；每个完整结论普通推，NFF立即pull/rebase再推；容量不足等整份发布，原raw和报告不裁。

本条发布前实际run/attempt/job、源冻结及PID、原自然返回码、任何场的真实Gram/曲率/商距/精化仍未观测。准备参数的actual维持null。严格存在唯一连续经线不等于全g闭曲面已经得到；原README全部完成标准持续未付，继续后继全域求解。


## 两支三层全部18科学报告：ROOT独立实际终态

固定`40341aeb2e07bbe34ea8647c962140045e10e8a5`，[官方46171324381/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46171324381)、job141060171079全success；17:35:49Z—18:08:17Z，触发/冻结源`576d836ce9dcdf02b8960cdb72bcef55c95b4c57`，两原自然进程exit0。ROOT分别读两支各三层可行形、完整guide和全三Cartesian拟合18原文及总索引19件，全部UTF8长度、SHA256和Git核同；18源实际bytes/SHA与原inventory一致。每层grid、七拟合相/六独立中相/13guide相、11全图，及可行形三层grid和7相全部直接核原文。原中相.225的实际均值词为0.22499999999999998，完整报告保持。这些核验在ROOT执行环境重置前已完成；写入中断后先查main和该文件历史，确认未刊，再恢复该同一结论，未重跑科学。

原nfev12/20/30和LSMR12/16/20未改；一部分前相按原ftol条件status2自然返回，一部分耗尽原nfev为status0。两种状态都不表示全相对Gram达到1e−6。原可行形层(32,2,8,3,10,24)/(64,3,12,4,16,36)/(128,4,16,6,24,48)均完成，不能把较低的内部目标函数等同全域准确。

|支系|层|末相独立全Gram|图|max abs principal|图|
|---|---:|---:|---|---:|---|
|convex-300|0|22585.450980310146|cap+|3596197.4246914256|cap+|
|convex-300|1|54857.96401356767|cap+|3576061.7971554846|cap+|
|convex-300|2|79257.89712057449|cap-|3541344.7186910454|cap+|
|convex-420|0|15545.688369679763|cap-|502022286.8721503|cap-|
|convex-420|1|32424.16993724268|cap-|468118993035.0242|cap-|
|convex-420|2|47203.38139296087|cap-|15649125.40434073|cap-|

最高层guide各655真实全周期角点；.30/.42的凸root最大残差分别2.4631527945896476e−13、2.998575811734132e−13，但另一个更高阶求积独立端残差分别9.848218962113484e−8、2.897455817208022e−5，二者不是同一量。两支fallback0；最小Hessian特征值5.301952772280309e−5、2.8480912898146998e−5；最小正轴参数.008854233285119431、.002751757650463096。完整隐导数、实际root次数10349/10682、所有接缝与角价地址在guide原文保留。

限制为两个水平形变通道的可行形最高层末角Gram/shear分别(.9337915645275823,.7377482252740323)与(1.2002798115918671,.951164766776754)，原源里的正B凸根和严格g_vv不消去这些项。放开完整三Cartesian的全11图拟合后，最高层全帽Gram仍79257.89712057449与47203.38139296087。

最高层末物理系数各为27816B原数组；.30支SHA256 `074cfba5f73cf9bc1d5333e448f1ec7cd8f87b09dfe980c845056fb4033400cf`，.42支`b31bbfc4a2cd1060121c9b3e866295a46a151252a9ab5d32acdce41f75182b00`。对应最小有限support −1.1529849115169803/−1.736839409026401；preband弦−初路径−.0028204659539947663/+.03395856001235792。两求积的signed-volume分别[11.28913383591944,11.28586198612238]、[10.504433236895487,10.420508149020371]。相位和系数身份不可与guide、另一层或另一支互换。

有限support/volume/样本held不能替代全时管或E(3)商距证明。精化后的误差没有趋于零，更没有趋于原求解器容差；题目完成标准未达到。R771的解析唯一正B根、准确经线速度、参考握/位移/商距仍只属于原证明限定场，不传给全自由修正场。

总索引rules_read_commit为`ab576dce2179aed57f437830b555876db055566d`；最后发布活动行的另次真实pull为`c2bd1e8fbcdb84c4bfff6d880f64d18870242f24`。两事件分记。两自然原任务已完，撤活动marker；[完整实际身份表](2026-11-28-R771-complete-positive-meridians-and-remaining-cap-errors.json)与以下全部原文保留。后续正在改变帽及中央真实输入，不能停在这个局部结果。

### 19份完整原文三身份

|文件|bytes|SHA256|Git blob|
|---|---:|---|---|
|[r771-convex-meridian-46171324381-1-convex-300-level-0-feasible.json](r771-convex-meridian-46171324381-1-convex-300-level-0-feasible.json)|6488|`e541bf13818ad48caac7dc3d25b3d3952299c3e63489f021740c40231ac3722d`|`d00735dfc99ad0cffce6c665c7bdc8a5e3542b3e`|
|[r771-convex-meridian-46171324381-1-convex-300-level-0-geometry.json](r771-convex-meridian-46171324381-1-convex-300-level-0-geometry.json)|44472|`6fdf5c33a4282147e3ca9ec223670640acc8626da6e7b5a3db625b8769d92093`|`2dc5f0a7fad414a483e9957ef66d2c488d6657bb`|
|[r771-convex-meridian-46171324381-1-convex-300-level-0.json](r771-convex-meridian-46171324381-1-convex-300-level-0.json)|53827|`ab66f68a2a5ee0ec708e402ba79c62aee82208978504b768c76c4cd5725f42ce`|`b38fec3b8c5288baae8952deb039872267c60f36`|
|[r771-convex-meridian-46171324381-1-convex-300-level-1-feasible.json](r771-convex-meridian-46171324381-1-convex-300-level-1-feasible.json)|6461|`f0a71b44d8c6a318bb0e1d42255e5478d9ea0fa9b6cbded98662ca95edfb9311`|`3a22679632c97015abd2a56197f4043d7a5a25e5`|
|[r771-convex-meridian-46171324381-1-convex-300-level-1-geometry.json](r771-convex-meridian-46171324381-1-convex-300-level-1-geometry.json)|44412|`30954e9fed47f53f6a4a86354d84cf6c92653b212b360efd2d27fd5023441da7`|`cce2fc79e63c0c303a38f4fbc41fb4c4fe8ef7a8`|
|[r771-convex-meridian-46171324381-1-convex-300-level-1.json](r771-convex-meridian-46171324381-1-convex-300-level-1.json)|53896|`579412afc62e353ab7ce9329b10ffbf48ccc07642fe3c1c70cbd8c824ae27ac8`|`d8492c49b799877acb087ffa719108dff52acdf8`|
|[r771-convex-meridian-46171324381-1-convex-300-level-2-feasible.json](r771-convex-meridian-46171324381-1-convex-300-level-2-feasible.json)|6433|`32e00089801b7ef8bd2cd89a89c0af488683776e392105575f7f0b4fcbc69bb6`|`273358da758d27a7ed34d228664efddd17b3cacc`|
|[r771-convex-meridian-46171324381-1-convex-300-level-2-geometry.json](r771-convex-meridian-46171324381-1-convex-300-level-2-geometry.json)|44435|`6f21e268e5825ea0b452d1bf6624a6699672161e1a4e799afa09fb2b75b4fc1b`|`fba3abbcd98c2e2773bbda8a581c9de3ce92409e`|
|[r771-convex-meridian-46171324381-1-convex-300-level-2.json](r771-convex-meridian-46171324381-1-convex-300-level-2.json)|54043|`736900fe9ab0af51c36e00ceab92b070143bf7d2ad4a51d41738d11f2e3cb8a6`|`a34db8af9f448525150d4a6c450efb1ddf1351df`|
|[r771-convex-meridian-46171324381-1-convex-420-level-0-feasible.json](r771-convex-meridian-46171324381-1-convex-420-level-0-feasible.json)|6487|`70d26f76bde68130751e8b3607fa77db9aa17b119a9d00bc0ecc9e31c6b16772`|`0bacc7b2c14e228886cdc22b6f26533913dc0cde`|
|[r771-convex-meridian-46171324381-1-convex-420-level-0-geometry.json](r771-convex-meridian-46171324381-1-convex-420-level-0-geometry.json)|44487|`f653eb08878dc65ff4097d813d270871db64241d335e13c8d6a3437a3d33ceaf`|`253e8e96372c2c9ff8047119668d7ad589afd2cb`|
|[r771-convex-meridian-46171324381-1-convex-420-level-0.json](r771-convex-meridian-46171324381-1-convex-420-level-0.json)|53700|`f4027899645df3df06918ed01877a1591735b5c01f6488d158d43ab2c10f2870`|`bc5c2af142617bf2d2162a7f734c8e7772121e16`|
|[r771-convex-meridian-46171324381-1-convex-420-level-1-feasible.json](r771-convex-meridian-46171324381-1-convex-420-level-1-feasible.json)|6457|`e0ad24b047669f4615aa0e790e68f0115f63adc70255a005967cd4aa6e7a5065`|`b929b3a05aec61d642aeb99a91c5ab85ba49cb3c`|
|[r771-convex-meridian-46171324381-1-convex-420-level-1-geometry.json](r771-convex-meridian-46171324381-1-convex-420-level-1-geometry.json)|44417|`5a266b3dc700bfc45b934ed9baacfc296e398e217fab5dea442180adcef8f102`|`6d585d9da410f1d11127a83388494c028ae95dfe`|
|[r771-convex-meridian-46171324381-1-convex-420-level-1.json](r771-convex-meridian-46171324381-1-convex-420-level-1.json)|53707|`fd00c144f9662bd9ea836b560a8ffccb83c645b6307d67d726e6b1e44d546210`|`edd70adc045692681eb174b2439f8014e6cce40f`|
|[r771-convex-meridian-46171324381-1-convex-420-level-2-feasible.json](r771-convex-meridian-46171324381-1-convex-420-level-2-feasible.json)|6417|`e5382fdcdb75e614c59f407c4d9528db045aa8d7393d6da3a6688e4d61d057df`|`13b46621565d67e590834a2c9529d2e15fa2cb61`|
|[r771-convex-meridian-46171324381-1-convex-420-level-2-geometry.json](r771-convex-meridian-46171324381-1-convex-420-level-2-geometry.json)|44465|`79e6d203cdebb18589cd2490a8903fe84933e7742e810a5cc47f9b5916669c10`|`b0010b82961531e6624716925c06892154f35228`|
|[r771-convex-meridian-46171324381-1-convex-420-level-2.json](r771-convex-meridian-46171324381-1-convex-420-level-2.json)|53801|`671c79928c9fec45b9cd2bdfff636990cba94b65d7a6eb9494446bd52c7c1bc2`|`3156c5c746f3e8efd8366468c647c98d4bcdd477`|
|[r771-convex-meridian-46171324381-1-index.json](r771-convex-meridian-46171324381-1-index.json)|9353|`81be9305ad07ae637a0a290b81855a5e1447d82ad1280f95a0cc94d8fe707858`|`47b0150986617d36d41ebf06a72a8e3efb3974e8`|
