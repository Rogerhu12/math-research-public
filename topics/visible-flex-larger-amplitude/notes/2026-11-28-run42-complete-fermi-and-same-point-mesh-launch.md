# Run42 — 两整卷真实测地/Jacobi形变、共同材料重建与原点完整闭网

会话 Astra-larger-e4e2a2bf-20261126。状态：**公开原科学任务待真实触发和自然返回，不是课题完成。** 数学判据见[R755](../results/R755-geodesic-normal-continuation-and-fixed-cap-landing.md)。[R756](../results/R756-flat-ruling-cap-obstruction-and-preloaded-exact-returning-rolls.md)已经给本任务R752/R753规定中央的完整平材料带反证；42在原固定度量上检验实际形状优化与材料重建的数值行为，换成法测地坐标并未消除物理障碍。另行改变初态的43/R758不可借用本次固定g的读数。

## 完整物理域及求解

目标始终为R752原完整九图初始pullback，全部相位[0,π/2]；中央真rectifying曲柱、两个真实developed fan整帽有19个物理形状/独立刚体控制，两整roll各有独立三分量物理场、C²钳制模式和两端v^(5/2)分量。全部18个物理/接口输入在本次触发提交按整文件冻结；既不读取旧40/41系数数组，也不重生旧场冒原点。

求解沿实际两整圆周法测地线积分位置、斜率、真实长度和Jacobi值/导数。先用真角S及完整逆六jet转换掉人工运输坐标的尖峰，再用JAX CPU float64对实际物理场反传；19个物理hard参数用完整六jet有限差分。损失明确包含全J误差、J导数、Gaussian密度、T−L、全部帽弧长着陆差和规定锚，以及曲率、面积、support、角折叠、Jacobi聚焦和积分防护的实际费用。guard或图外截断不是成功，实际次数和极值必须报告。

每个候选还将实际射线重建成两个周期材料图，内外缝处值和前两阶横导数钳为原图；真径向位移用tanh形式保持边界并另测Jacobian。随后在该真实复合闭场上读全部三行relative Gram、曲率、support与四缝二jet。射线指标小本身不能冒充共同材料图的同g。两个帽重叠来自原生成器的同一个G(s,w)：cap-normal=G(s,w)、cap=G(s,1−v)，六jet变换准确为(1,1,−1,1,−1,1)，物理半径rho由同一cap_leaf给出。

## 原完整预算

五个完整粗初值 legacy-free-pose、omega-free-pose、plateau-free-pose、omega-shortened-cap、plateau-shortened-cap，全部先运行；每个有2个时间区间。按实际返回score选本次自己的候选，随后在同g/同全相位做4、8、16区间三层真正精化，模式按原名嵌套延拓，不删除旧变量。

| 层 | 空间mesh | 独立check | roll径向/turn/角 | 正相位每结maxiter | 射线/独立射线 | 积分步/独立RK4步 | 材料图角/径向 |
|---|---|---|---|---:|---|---|---|
| 五粗 |27/11/8/7|69/21/15/13|2/2/3|52|23/59|72/143|3/3|
| 细1 |35/13/10/9|77/25/17/15|4/3/5|64|39/81|104/207|5/5|
| 细2 |49/17/12/11|103/33/21/19|6/5/7|76|57/111|144/287|7/7|
| 细3 |65/21/16/14|127/41/27/23|9/7/9|92|79/149|200/399|10/9|

积分节点另含所有真实材料结，独立射线加原完整profile特殊点。L-BFGS-B maxls24/maxcor15/ftol2e−12/gtol2e−8；全部权重、防护参数、原design值、原regularizer及map_ridge3e−8详完整参数文件，不另缩预算。每层保自己的完整点、材料图、相位向量和其原SHA；有限返回分别作为独立科学文档，原NPZ仅runner。

## 真末点的全闭网与几何

最后选定物理系数ZZ、两个实际材料图、时间结、完整design/config与初g/物理源/basis/reconstruction的SHA共同定义closed_point_sha256。**同一runner直接复用这个真实点**，在65个末层独立相位与七个指定mesh相位的并集测量；七相位为0,π/12,π/6,π/4,π/3,5π/12,π/2。

每个mesh包含中央、两整roll、两完整帽以及两个Cartesian中心，共享所有缝和周期索引，记录连通分支、Euler、每边双面和朝向。双精度顶点及完整三角连接各自全SHA；未压缩/压缩完整PLY均须<5MB。全mesh保runner并留可重算源参/完整身份，遵根§15，不另存Git或Release。

每个真正时刻评估全部图上的relative Gram与主曲率、四缝和两个帽换图的六jet；完整顶点对直径、全部有可能超过已知界的有序法弦对、全三角对含共享边/点之外额外接触、初像双向距离，以及体积/质心/极惯性。全顶点/三角读数仍为浮点离散证据，法弦倒数不当作连续reach下界，mesh距离不冒光滑面Hausdorff证书。全t连续嵌入、非聚焦覆盖和uniform误差仍需真正付清。

## 运行与完整源身份

公开ubuntu-latest/4核/16GB，Python3.12.14、numpy2.3.5、scipy1.17.0、jax/jaxlib0.7.1，CPU64bit；job原360分钟，不加科学子进程时限。8秒观察、120秒实际小结、2700秒真实pull/rebase和双README差异，NFF立即普通整合再推。原stage的独立完整小结和同点全几何index保各自身份；不把完整大raw切段送工具，不复制原数组。触发后的实际run/job/PID/源提交/完整输出仅按实际回填。

| 文件 | bytes | SHA-256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261128/bent_fermi_phase.py | 14734 | ba9e886c66bc27496691e165a94aeba6880a0862c07badb5c21b64ba76949f04 | e1f8516635134e1dc4f9445eeab0f4063df36362 |
| scripts/resume_20261128/bent_fermi_shoot.py | 12275 | a519f608e85af861f127a82cda83598f597b1d3aec2d4821ccafd5d9b0e5976a | 6bb423228bd887fee1671b30779ebdde0eadea7d |
| scripts/resume_20261128/bent_fermi_reconstruct.py | 4577 | a229a2cbe57ac6e81849e7cf8e09c5f7f1a1e56ee7086b838ab394b17a350a71 | 74960d6231d0ddf52380aa048fd15ad7c2e5fb81 |
| computations/bent-fermi-phase-design-v1.json | 5563 | 91841eaf65693afc11708c99033c0e994999148074e2ef9a2ed014369c4f6b9a | 34ac203f94a50a350cad509c6be8c49272cdfdb4 |
| scripts/resume_20261128/closed_body_mesh_terminal.py | 16874 | fca64a1a1b16822b39f7c4bc12bb559f394eb88f81da932fbaa13c161914d197 | e86f09bfd360b67abfe8075f0a1b6bf0dace7279 |
| scripts/resume_20261128/closed_body_mesh_geometry.py | 8315 | eadff92d30352db738e8642f3fcad051661d6a48a3628c22101a58967f1b0050 | 23ce25eeb6c3ca89667537152fe59c59a5c2d1a1 |
| scripts/resume_20261128/observe_bent_fermi_search.py | 17083 | 4ea6d5226fd2b4f104fa5be61b7aaf4b1a1f3951bafc95ed3c2f5a2985b59c05 | e86c0c23a922a9327bfd2aa54b25cb37197aa000 |
| .github/workflows/visible-larger-run42-bent-fermi-phase.yml | 4289 | 5e40980212e6e3da111ef086f261e4d2ac725e28542ae15ec9625a385426683d | 7c39728e5f5e36a9138a2f6d6961d65a2f179645 |
| computations/run42-bent-fermi-phase-request.json | 21109 | 4f02c9835550989c340881be7316b42455fdb1ec9fe97da5c6dac1647c4ca924 | e1afd0b7878abfdaa982aeef36e681de787cf4ef |
| computations/run42-complete-bent-fermi-source-and-launch-delivery.json | 21168 | 2e472ba8b101f19dbeedd5d5b7d25f5154959d5c9c0475b365485cfb82c0baa2 | 3a4adc34c6434f0900dd66305b814854f2b95fd6 |

十二份完整物理父源、原3控制辅助和每项具体身份已列在完整request与manifest；本次普通推同时保留这些原输入。课题外改动 .github/workflows/visible-larger-run42-bent-fermi-phase.yml 仅用于这个完整公开科学任务。未读取任何本地数值结果作为科学结论。

## 2026-11-28完整八阶段与同点69相/七整网格实际返回

公开[run 46154734602/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46154734602)及job `141008777374` 已真实completed/success。原PID2738于14:27:42Z启动，15:18:55Z自然exit0，科学总耗时3061.080049481秒。实际冻结源 `1541cfa06cba2ed3f8787cb3c20d21d013af8a7d`，首次规则读取 `e1a670eecd7542e644001b7d5c0ccd97ba0d4358`；命令SHA256 `83daeff4485b0d78862a5619f570d1b39e1bbadee0de5c8dc6462b755ef4edec`。实到Python3.12.14、NumPy2.3.5、SciPy1.17.0、JAX/jaxlib0.7.1，4个逻辑CPU，全部18冻结科学输入与原请求一致。

**全部原计划已执行，科学结论失败。** 五个粗设计、胜出场4/8/16区间三次精化、同一个16区间全点的69相检查和七份完整闭面均有原返回。不是因时长、取不到输出或删减预算中止；这些实际结果也未给准确等距/连续厚度证。

### 完整原返回与全点身份

11件以下原文固定于[9a986dc2fbeac56f4c60412533b25a617dcc9435](https://github.com/Rogerhu12/math-research-public/tree/9a986dc2fbeac56f4c60412533b25a617dcc9435/topics/visible-flex-larger-amplitude/notes)，每件ROOT取全文并核bytes/SHA256/Git。每阶段非零系数、两端地图、全部phase与原标量/几何原报告完整；根§15下大系数和mesh原数据留runner，由已刊完整源码与配置复现。

| 原返回文件 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| run42-bent-fermi-phase-46154734602-1.json | 23860 | `4bb46b8af62dee9745b9c1520a30a1293727e742ffb8237848fd647cb283d20a` | `cda9997deb5f376a5673e57997b36a00500fc3be` |
| run42-bent-fermi-phase-46154734602-1-summary.json | 34456 | `ad6a114bc1893112013b2e97e2ed270780ddb82bacf7590e2c0b7b6dfc729ab0` | `9b64cc6dae30fb1a886d7db12aeba87deb098e3d` |
| run42-bent-fermi-phase-46154734602-1-geometry.json | 32169 | `5261da5cd71562f5dea439ea4fa21507c472713389885189233cbff78693814c` | `ca80dd7ecfb8fa848075c37f8f1e344a58128dc1` |
| run42-bent-fermi-phase-46154734602-1-stage-00-return.json | 8424 | `76f755704d34b027e1eeab922f5ad34bac6f75e74bb03c2b24e6f817b0cc72f8` | `bbbbf6e37f327a85250ae574b455f0067b0d7ad9` |
| run42-bent-fermi-phase-46154734602-1-stage-01-return.json | 8397 | `fcb526606fb1a3420dd90edcd1b284ea37662d3932aed4cd286db5e84978bda6` | `c3c9531a531bb44c615d24ba3a3cd95dce1a8820` |
| run42-bent-fermi-phase-46154734602-1-stage-02-return.json | 8439 | `46001db17c8f13a16281130d1f551b891f59eabf9f168e4c4c5c379258662c93` | `a3d3c233cf67e00a6d1edda7361aeab2cfef29af` |
| run42-bent-fermi-phase-46154734602-1-stage-03-return.json | 8451 | `509de85af32dbcd752baf369eda633f8ebbd78f8e8438b00ac2a6c76c2ca184f` | `adaaf49438b0aec2206b6df6a2cb4234b4152dc6` |
| run42-bent-fermi-phase-46154734602-1-stage-04-return.json | 8481 | `b776e3be839c0ba3bbb3e45e8b379e72fa59c7ba71487b5297f981ddb83889be` | `61161a86e2bea66293acc13ed65efc43c9a146bd` |
| run42-bent-fermi-phase-46154734602-1-stage-05-return.json | 12203 | `ab72cc7a2db4672cc9b2c1f72986c056251f2d86484f2ce023eb2838104990f7` | `ee25d0b5c2e5cfd8b0bce3ed81abc5006c77d858` |
| run42-bent-fermi-phase-46154734602-1-stage-06-return.json | 17928 | `776e6aaa99030a7e82c246491ddaac131a20c5149903de5ac8f016ddd506f565` | `894e416bd418709fa66f9ee38e0a2af93abb0162` |
| run42-bent-fermi-phase-46154734602-1-stage-07-return.json | 29401 | `4a4949ae9ef14d8e771d1448a5aec650b02261bc7308ac383977f2ca2b3c55bd` | `b58dd2af6d502c18bbcf1a6d3989ff85ada87b93` |

五粗按原组合score选择stage2的plateau-free-pose；不是挑metric较好的一列后换点。三个精化均继承这个设计及同一R752固定g。

| stage / 设计 | 原阶段真Gram最大值 | 原score | 完整closed point SHA256 |
| --- | ---: | ---: | --- |
| 0 / legacy-free-pose | 5.350542178002616 | 52.37697896486424 | `a8f7a9783b861949f8d67b2b8a4dd47cb2afc1eecac955b54c657e9eecbb21b7` |
| 1 / omega-free-pose | 6.71581625468438 | 61.35462059943555 | `c5bd845d07050216dc2c89f2b6a97c59e9da85e5654f97a63b3d0b374d79034a` |
| 2 / plateau-free-pose | 5.521912344450496 | 39.401841960712545 | `9be050186a9e70780390a11d43c63d05ef303de7de1c57956202c4054c04f84f` |
| 3 / omega-shortened-cap | 5.983043974486947 | 384.73764565106114 | `328be16d129bf473b58ca0fb1bb57f14bd2b11d69a542cf55944a731790596a4` |
| 4 / plateau-shortened-cap | 5.078289821905922 | 53.306596389288615 | `325da010aa94c8e7848fa7e10cb026740d12dddc20dba8ae5a57cb376b12f79c` |
| 5 / plateau-free-pose（4区间） | 8.260048268218732 | 144.23599471958377 | `00ada6816695826dbe34b012df6ff91daf0a73da459017e558e878957691f0cc` |
| 6 / plateau-free-pose（8区间） | 16.555048315059164 | 167.8117475457826 | `34e460287d4d4e6134a523118a2e56bd2cb2e6467c413050172e2c71b27dd329` |
| 7 / plateau-free-pose（16区间） | 24.833270128580768 | 124.55276452708438 | `29cefe1073785e772f96dce9b41a733573f71f6265638dd6aa02a90a0fe5a704` |

最细stage7完整物理系数为17×2539，SHA256
`f8b159614d10c5e4a2c9dfcf80458393a0c18690621f89d3be7f0cc08225c423`；
两端地图17×2×2×210，SHA256
`68733c64287c14c6097a049568ab3c85a38b7154ab7faad0eb0bd04c721a79ca`；
phase字词SHA256
`a6d7c4ab616f4e28e63d90de4d2ce2a9b8b194a72f11cd2ff308f1944c6c2ec2`。
原 `stage-07.npz` 460456B/SHA256
`56b255c15eb595480dcb879b689532922da9b37d821b3483419598fad0daedc1`。
它与上述三部分组成的closed point `29cefe1073785e772f96dce9b41a733573f71f6265638dd6aa02a90a0fe5a704` 绑定。runner中另有较旧的 `current.npz`，不以该文件名替代末阶段身份。

原末阶段15个非零结点走到92原迭代预算，另一个结点在38次自然满足程序条件；真实方向导数核查相对误差5.665912366420989e−8。末Gram24.833270128580768位于end+、相位 $\pi/2$、$u=1.5561777300831,v=.9367587724539175$。各图接缝最大六jet差2.2737367544323206e−13不能消除该内部真实度量误差。

### 射线与校准失败的范围

裸初相的真实物理Gram为0，但原稀疏双线性几何系数插值所算Jacobi量并不准确。粗层裸初相 $J/Q$ 误差 .07914037937714169/.6883748207432792；4区间层 .3273172324829008/2.1034037136069195；最细层 .10842803497962272/.9595665558816566。这是原返回保留的校准失败，不能以精化次数或公式正确掩盖。

最细原射线的最小J为−.24173141466231832、最小角增量比−129.60662312979076、最大guard ratio7.282989235976143；它们直接没有给出非焦覆盖或全局坐标微分同胚。R755的条件性测地判据仍要求真实Jacobi/全覆盖等前提；42没有满足这些前提。R756对该旧中央/平带输入的准确障碍仍然有效。43改用R757真非平初g和相对裸场的差分射线校准，并独立继续整个物理Gram；43的结果不能倒填本42。

### 同一末全点的69相整面几何与七份网格

原最终导出将65相网与七要求时刻取并集，真实返回69/69个phase、7/7份完整mesh；`all_phase_measurements_returned=true`、`complete_requested_meshes=true`、`errors=[]`。全部使用同一29cefe全点、全部材料环与两Cartesian极点，三角网17714顶点、53136边、35424面，Euler数2、一个连通分量；不一致朝向边及非两邻面边均0。完整faces小端int32 SHA256
`c18144087528960e2515b1c5ed779f89e3a1cb91c948205d3cd134e7b713da5a`。
原网格节点profile144/end30/cylinder19/cap25的准确word identities在完整几何索引中。

69相有限采样得到：

| 指标 | 返回值 | 对应phase（弧度） |
| --- | ---: | ---: |
| 最大相对Gram算子误差 | 22.878516670227697 | 1.550049556649225 |
| 最大主曲率绝对值 | 430.2217929459707 | 1.227184630308513 |
| 最大有序逆法向弦 | 247.02386578153778 | .39269908169872414 |
| 最大网格直径 | 3.226941527327707 | 0 |
| 记录的有限mesh Hausdorff lower量最大值 | 1.6226316663581404 | 1.227184630308513 |
| 顶点Hausdorff最大值 | 1.8378116152456638 | $\pi/2$ |
| 最大接缝六jet差 | 5.40258286761305e−15 | .2737775411283715 |

这里22.8785与阶段24.8333使用不同检查网格，保持各自原范围，不挑较小值称全域上界。有限网格体积从2.743265648791911至2.9592153033143305，中心极体积矩从2.743924468939552至2.9617252266520273；这些有限测量不是连续体积/刚体商距证明。possible-extra-contact与zero-area-triangle采样计数均0也不构成连续嵌入证。

七份原压缩PLY全部包含整闭面而非切片；原PLY大小885930或885942B，均低于5MB，下面给每份原压缩文件的完整身份。其解压后PLY/顶点字词SHA256及69份逐相几何JSON的完整身份均在上述geometry原报告保留，无重新采样替换。

| phase（弧度） | 原gzip bytes | 原gzip SHA256 |
| --- | ---: | --- |
| 0 | 261153 | `c294eb8b1a7133b091149aa6df5781361957c0515b4f726db4aa6ebcd5badd80` |
| 0.2617993877991494 | 493172 | `c9d74b8e57052b06937f7d13c9d3e88d4f5c96ade8c366e749a6d7f8e18c4bf7` |
| 0.5235987755982988 | 496122 | `d4c89ee967382cda07365c75e3094bc8d4aa3996a651ebdf6916dd244136b2a3` |
| 0.7853981633974483 | 497301 | `f777e9f3614ffe3de6c197c06de872e08645f752a4919c6642faea62c36f3fcd` |
| 1.0471975511965976 | 497898 | `e808b2d7bc7a38c045fb541edb3c23fa65d86e4ac1c68298f53de63d30f65097` |
| 1.3089969389957472 | 497690 | `b533b6334ea789329afa22664f2268f343aa9cbba940d050be373e4e44642584` |
| 1.5707963267948966 | 494968 | `433203f8758e7c96ed82aaa711d6f5987f1a6abcb724b73b58437ea218f7d6c2` |

原内部mesh索引32027B/SHA256 `47900c5ff589ed13b70e274847d31e9238f026876ff8bd72f3c370abd603eb15`；公共完整几何报告32169B/SHA256 `5261da5cd71562f5dea439ea4fa21507c472713389885189233cbff78693814c`。所有可重算完整raw只在原runner保留，仓库保存完整源码、参数、原run及整身份。

本42已完整闭账为失败：真正的同g/同参数全phase精化没有使误差下降至原容差，厚度未付。继续43–45及新物理输入，不重复此已登记结论。
