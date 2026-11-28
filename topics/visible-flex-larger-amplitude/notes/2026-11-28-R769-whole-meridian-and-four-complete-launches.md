# R769：重新分配完整转角、整长单位速子午线及四原整壳拟合

会话 Astra-larger-e4e2a2bf-20261126。原R766四支全24报告失败已登记6cb633b3d1933a3be865e73a5dc9feff150a84c7，不能借精确首边或局部刚帽作完整等距。R769采用同一个R764初g，新的实际中央边界及两种贯穿整卷/真帽的物理输入；没有改原R766源/预算或把其失败抹掉。

## 完整解析结论

[完整R769证明](../results/R769-closed-curvature-redistribution-and-complete-unit-meridians.md)重新分配原三个实际转角，平移/转动原真握区固定整个中央握片。所有原直线材料仍为直线、所有原零曲率点两边开邻域倍率1；全实际曲率乘a>.09，原全闭曲线通过λ∈[0,.45]唯一单调闭高方程闭合。末λ>.238由原整材料长度估计而非拟合取得。

在真实长E=.44的每个完整预卷使用r=1/a及积分Pv=√(1−r²d'²)，整个gvv准确，另外两行费用恰为r_s(rd d'+P_rPv)和r_s²(d²+P_r²)。这使所有真实零/平段及r常数区三g完整准确，剩余价格明确。原标准卷的整个L=.132π/2+.0005一分不截；两个响应b=1+c(r−1)、c=.5/1把正弦/余弦速度归一化，gvv恒1且正曲格的角因子>.07，三向实际价格显写。两整原曲帽用真normal/polar/Cartesian过渡与外圈S7补偿完全接入，真实六jet缝匹配，不仅是一张rim。

完整normalized参考的整像held≥.88>.2D0（D0<4.386），固定握径1.40，初reach≥.132>.03D0；正相全法管仍未付。新的E中界硬trace却把同一帽上两点分离到原跨帽材料短路允许值之外：d_end+1.30sin λ>.438，剩原roll L<.208。该反证不仅排刚帽，还排保持原g的任意整帽，所以E真实界必须自由。

另外两支从中央到帽贯穿E+L，只用一个真材料弧坐标。将真实三维帽端目标弦C以C4饱和到严格<T−.005，两个真实端轴退让.30/.42；在S²上对原全长速度施加完整三分量流，证明任意严格内弦都有根，初相根局部光滑。度数论本身不证明全相全圈选根光滑，实际源码用全圈已求控制的周期三次插值并独立记录node/中角真实积分残差。整帽连接到实际积分末点，因而即使残差未小，真缝六jet仍接上；没有偷换成理想目标帽。该参考整gvv准确，gss/gsv与帽内价格仍要支付。新R771将单独处理全圈唯一凸分支，不覆盖此原输入。

## 四个完整原任务

原四独立进程为normalized-.5、normalized-1、shoot-.30、shoot-.42，均用同R764零相完整11图g。每一层先读取完整参考几何13相并独立留报告，再在7正/零主相做原whole-free三Cartesian物理求解与6个中相独查；中央/两预带/两完整标准roll/两帽三图全覆盖，固定握mask保留。三层全部执行，不因第一层参考已不等距而删层。

| 原层 | 拟合角/径 | 积分阶 | 修正角/径 | nfev/LSMR | 独查角/径 |
|---:|---|---:|---|---|---|
| 0 | 24/6 | 16 | 6/3 | 12/12 | 64/12 |
| 1 | 40/9 | 24 | 12/6 | 20/16 | 96/18 |
| 2 | 64/12 | 32 | 24/12 | 30/20 | 144/26 |

真正整圈根控96/192/384，加原真实转角断点和反射，全圈midpoint独查；S²原控界±18，每根原72nfev及两个144nfev候选完整保留。所有控制数组/逐根记录完整runner留存并给全words哈希，原全场最终会受whole-free修正，不能继续假定其gvv或参考held准确。严格的强C²全时间、整g收敛、正相嵌入/全reach、刚体商及mesh交付仍独立欠账，本任务返回有限报告不等于完成课题。

## 全部输入与触发

完整[15源及原参数清单](../computations/r769-complete-normalized-and-shot-meridian-launch-inventory.json)保每件path/bytes/SHA256/Git、三层/四支/全部原相与未来actual空项，父版本43914b1da832b13ffc65f9f3074446217fc065b9。ROOT全文读完新proof及所有物理/求解/控制源；旧父按完整当前身份保留。新文件身份如下。

| 路径 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261126/r769_closed_turn_redistribution_and_complete_rolls.py | 9715 | 5cce0c30754b3d7be84fb4f99c4c099c56c1a869b653686f02d74939bbe5ddb2 | c0129e5322cdb3f462f11173a607da1d6e0fefaa |
| scripts/resume_20261126/r769_full_unit_meridian_shooting.py | 8423 | 2d79955e1d45819e3d20f9a377f88a5404dd5cf3a125bd53e81bcb1e9211a017 | 0a3c50cb136bd13ab3d16a7361bccef3d3d4beb2 |
| scripts/resume_20261126/solve_r769_complete_meridian_spheres.py | 10502 | a37c0d937de63290392eb753f3d9094c0c32449e8cbf808ee55abc6fe36ca1eb | 31b164c4df23ef1cd6e74d032278f290a782a6a0 |
| scripts/resume_20261126/run_r769_all_complete_meridian_fits.py | 12659 | a165f813bd27b93124bf1b0507722ca3b17fa1c5f9a823365e49de59acc2fec1 | 56105cea9bc89f6b8db9830f60cef76a7f818fd7 |
| .github/workflows/visible-larger-r769-whole-sphere-unit-meridians.yml | 4148 | 067b74c3855cddd1663dfa599fa502f935e19a60e7d24d49bae5593bd6952402 | b96ff974fbaa08cd0d28da8382acb9343eea7641 |
| results/R769-closed-curvature-redistribution-and-complete-unit-meridians.md | 21062 | 6e6a6830258aa98d300a84106361272d31a294803526ece90cd309cfe81dc74e | faf4e53983632e45cd9eaa1df3d065f4adc24531 |
| computations/r769-complete-normalized-and-shot-meridian-launch-inventory.json | 7964 | a05544bf4a1911f4c00a6a47dfb001d664a13df94b8b2477845be7fba8cdc45b | cfb5da1cacd121d7ca64e34c7fe38899875f342d |

公开ubuntu-latest4CPU/16GB，每进程一数值线程；Python3.12、numpy2.2.6、scipy1.15.3，355min公共原资源上限。工作流触发时固定15科学/控制源；规则工作树另以2700s真实pull推进，双README有变立即遵守。原所有自然返回后输出24独立完整逻辑报告和index，普通push遇NFF立即真实rebase直到成功。仅严格完整源/参数/逻辑报告/整身份入Git，原raw不上传。实际run、冻结身份、退出与读数待真实返回，未把本发布写成已测成功。


## 四支三层完整实际终态：ROOT逐份原报告核读

结果固定提交`c9b36e0f7348d531bdcd258d8d1b5da9fff6ba78`，[官方46169013968/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46169013968)、job141052938659全部成功，17:10:03Z—17:53:05Z；触发和真实冻结源均`729d75a549fddd6033dfe2b7bc5c2778457f7478`。四原自然进程都exit0。ROOT完整读取24科学文件和12579B总索引，逐件核UTF8 bytes/SHA256/Git，15实际科学/控制源的长度和SHA与原inventory完全同。三层原whole grid、七拟合相、六独立中相、13 guide相和全部11图逐项核同。实际中相第二个是原算术均值0.22499999999999998，而说明中的.225是十进制简写；没有重写原实际词。

原最大nfev12/20/30、LSMR12/16/20和全部空间/角控制保持，所有非零拟合相实际耗尽各自原nfev，status0不是收敛认证。λ末值.30459457915162325，完整转角闭合积分残差−2.7755575615628914e−17、guide中央曲率6.666666666666667只是对应中央构造，不能覆盖全帽。

|支系|层|末相独立Gram|最坏图|末相max abs principal|最坏图|
|---|---:|---:|---|---:|---|
|normalized-1000|0|561140.9747023626|cap+|154991066.75312537|cap-|
|normalized-1000|1|556965.2962412438|cap+|633703771.7835166|cap-|
|normalized-1000|2|639584.7209222862|cap-|143707890.66836935|cap-normal-|
|normalized-500|0|322585.2269756064|cap+|1600218998.2992995|cap-|
|normalized-500|1|316604.72065791115|cap-|2411964.153773745|cap+|
|normalized-500|2|325834.5146766248|cap+|123088922237.64725|cap+|
|shoot-300|0|38037286.330403045|cap+|172613300.92832017|cap+|
|shoot-300|1|10733078.895187736|cap+|173657630.26220942|cap+|
|shoot-300|2|8987228.944375103|cap+|3761529780.3417726|cap+|
|shoot-420|0|10790370.446172295|cap+|49993521.83037142|cap-|
|shoot-420|1|10470879.230045192|cap-|14618285.138826031|cap-|
|shoot-420|2|8851803.858247105|cap-|1770309894.6361315|cap-|

最高层各末相系数身份为27816B原数组（不是整场统一point SHA）：

|支系|系数SHA256|最小有限support|preband弦−初路径|
|---|---|---:|---:|
|normalized-1000|`3fd0f177a94abf053a5b71e63508bcba271fbd1b99c77d8f7b5b9d3a1dcd799c`|-1.485390892953573|0.020560033588074456|
|normalized-500|`d556898dd84ae5257b62f80c4337bcf795c6ac80bc77d186f1f1e9ce95d02d5e`|-1.4647953850116646|0.022161887455230567|
|shoot-300|`98b3415dc852548febc542baa972ffb65ef0505e0c5ef244f574c211347dd50c`|-2.069549264169253|0.20090255322504286|
|shoot-420|`2d03d520b11a7dc13c3250b30de0444eb6f3252e124ee12c60508f8aa7aed1d1`|-2.480848490605867|0.16478765431575576|

normalized-500是原response .5支系的文件名，不表示response为负；另支response1。两shoot末层各478独立周期控制，实际最大控制17.999999999999996触原18盒边；.30支高阶独立中点端残差.01410180126766402，.42支.019143070853645628，不能把源中的单位切向或低阶root目标写成已经准确闭合。两控制数组各11472B，SHA分别`4feaa3a0a3aec67b3dd4fe8367877fac93c3c3e683893ed7b660797d77373b19`、`1e59d043bfce34a7f668ee8f655fb3d6c836eb652704dd3f8c406f0017c94522`。

各末相全帽相对误差仍从3.26e5到8.99e6，独立高阶检查与三层精化未趋向机器误差。局部准确中央、whole unit meridian或参考held界都不足以完成全闭球同g与reach。有限负support和有序弦值保原范围，不由有限点推全时自交或严格厚度否定。该原运行已自然结束；继续R771以及后继释放帽/中央的不同准确构造，既不重复四原结论也不把成功退出当完成。

总索引内rules_read_commit是`5222eecc2f6762eee075a565e7b6b42500e7f8e1`；最终发布活动行另记录真实pull `f4a30b2fae7da95b9104b118e1f95f171a63e7ee`。两不同事件不混。现在撤去已闭活动marker，全来源仍在[完整实际身份表](2026-11-28-R769-four-complete-branches-and-final-cap-costs.json)，ROOT以下直接核验该表与全部原文，而不是只凭汇总作者的数值。

### 完整原报告身份

|文件|bytes|SHA256|Git blob|
|---|---:|---|---|
|[r769-meridian-whole-46169013968-1-index.json](r769-meridian-whole-46169013968-1-index.json)|12579|`ad22c6ca0a047f762530dd3176ecd6bbfe29b9203519f5c6b8c62a76b6228205`|`0e6c4c05feb67c642f86147a28347d4a15817dc7`|
|[r769-meridian-whole-46169013968-1-normalized-1000-level-0-geometry.json](r769-meridian-whole-46169013968-1-normalized-1000-level-0-geometry.json)|37586|`7b3431fde2804043a8821f973e872233166fc3245f711b4aa5194be6002d8e54`|`78d4371831d21d143622167871eb9b36c61f3da6`|
|[r769-meridian-whole-46169013968-1-normalized-1000-level-0.json](r769-meridian-whole-46169013968-1-normalized-1000-level-0.json)|52239|`5b405f30454fa2ff7add61aa7abb120d7892331809267ea638b474863ad26273`|`c19ae8134a843095b96838588798215bc67ba8c3`|
|[r769-meridian-whole-46169013968-1-normalized-1000-level-1-geometry.json](r769-meridian-whole-46169013968-1-normalized-1000-level-1-geometry.json)|37613|`63b29a9a7afe70c6351cb903592b3e1b5ddc02d1dd0869f65182b6e11da2c764`|`2e263ea16675eea10428d23efa6529803f6b613a`|
|[r769-meridian-whole-46169013968-1-normalized-1000-level-1.json](r769-meridian-whole-46169013968-1-normalized-1000-level-1.json)|51978|`d0d25aa1a762d4b0573e9e0918958232ac7f7433aec3758a513d88cad40786b8`|`931e62a5ed56209774718ec1dca7e501222e0639`|
|[r769-meridian-whole-46169013968-1-normalized-1000-level-2-geometry.json](r769-meridian-whole-46169013968-1-normalized-1000-level-2-geometry.json)|37635|`a53130897d89afb8ad957055b14ac2dbdba5cfa4c082a347b318342feb4ec30e`|`1a32341e57ea5c54d6d9245f5a4c352b42184ebd`|
|[r769-meridian-whole-46169013968-1-normalized-1000-level-2.json](r769-meridian-whole-46169013968-1-normalized-1000-level-2.json)|52038|`bbee0d8129842e14f1953ad780799eb9812393ac00a8b8182e84d02c10019122`|`509f4fd4e1f32ffb8932f0d2ece7266a0d27bc6d`|
|[r769-meridian-whole-46169013968-1-normalized-500-level-0-geometry.json](r769-meridian-whole-46169013968-1-normalized-500-level-0-geometry.json)|37590|`afd758ecc09924d7b0bc130d2a7d06ae31e495011a3e8b799cd8008b47ae52d9`|`6fb8189caf86b353eee52186bc8944fbe6444431`|
|[r769-meridian-whole-46169013968-1-normalized-500-level-0.json](r769-meridian-whole-46169013968-1-normalized-500-level-0.json)|52051|`17d472433e17aca8a8431d016e507d2ac6c7ec9aeea5184fca8868649992c88d`|`6d7ab53a72ae004f6ba64a0dfbf25af867dedb40`|
|[r769-meridian-whole-46169013968-1-normalized-500-level-1-geometry.json](r769-meridian-whole-46169013968-1-normalized-500-level-1-geometry.json)|37579|`05373955803fd095151178b7f3c9978ab92e5ad609c896c98038f0b8c3001376`|`55a3f02342e44474a60bd2ae75c1e64ae7330e43`|
|[r769-meridian-whole-46169013968-1-normalized-500-level-1.json](r769-meridian-whole-46169013968-1-normalized-500-level-1.json)|52084|`5f07775346b8d46a40777b8bbdc7a2abf1942a07b9c1f44f615e932a72bc3438`|`ff718cf687d8f572acfc2b99df1ef212280c1d55`|
|[r769-meridian-whole-46169013968-1-normalized-500-level-2-geometry.json](r769-meridian-whole-46169013968-1-normalized-500-level-2-geometry.json)|37609|`07cdf05e1b086e4e56f57f5b19ba0c47b5b741c586744a079dac5a38cc8e511d`|`6e6faad321c55e828becbe1cf35a5c45070279d9`|
|[r769-meridian-whole-46169013968-1-normalized-500-level-2.json](r769-meridian-whole-46169013968-1-normalized-500-level-2.json)|52217|`86df624122ba8b94aeaa49b7fbcfffa77f82e2fc0f546e1a5b72cb8497bc5e13`|`342c8c091a2a3de443823584901ebb2908d0d5d8`|
|[r769-meridian-whole-46169013968-1-shoot-300-level-0-geometry.json](r769-meridian-whole-46169013968-1-shoot-300-level-0-geometry.json)|42087|`efbc353808f36d2f7cdf1a64b3bc16cb04a93ec13d4bbbc5211f3b401c805b61`|`5b6b39803b6130874e4a38bfd6d80831d5720848`|
|[r769-meridian-whole-46169013968-1-shoot-300-level-0.json](r769-meridian-whole-46169013968-1-shoot-300-level-0.json)|51715|`888e1d72260c904468b8be3c3f62f9c2dcbfc9f3bec807ff3d6694fda82d5c18`|`c7af13e298731b09535fadfe937499d2ec534823`|
|[r769-meridian-whole-46169013968-1-shoot-300-level-1-geometry.json](r769-meridian-whole-46169013968-1-shoot-300-level-1-geometry.json)|42082|`c9c950a480e0175a08ce3e0d0a448e54b014dfc8d169b44480512fe5dbdfd15e`|`831f8fb1750fec73bb44df1c8024cb8bbbccabbc`|
|[r769-meridian-whole-46169013968-1-shoot-300-level-1.json](r769-meridian-whole-46169013968-1-shoot-300-level-1.json)|51651|`ae06c97d1e2aa75ea6e14bc1672e402c3f66e7560ef40a93dc3486d68aeba33a`|`7d77369f34160d4088dff130be13e5a5784dc0c0`|
|[r769-meridian-whole-46169013968-1-shoot-300-level-2-geometry.json](r769-meridian-whole-46169013968-1-shoot-300-level-2-geometry.json)|42230|`bda91732ec38430308d541cc252f788ab140f35f2ccdb98e33f28d3c406c1ad7`|`a5718d1d26cff904e2ff1cc70a4e14b90f4d9050`|
|[r769-meridian-whole-46169013968-1-shoot-300-level-2.json](r769-meridian-whole-46169013968-1-shoot-300-level-2.json)|51845|`f92b894562452d462a468779d791887fe0162df36800bac78c858b0b85081133`|`e0ee76d5d71ce8326c2ef58fdc138d977ffd0051`|
|[r769-meridian-whole-46169013968-1-shoot-420-level-0-geometry.json](r769-meridian-whole-46169013968-1-shoot-420-level-0-geometry.json)|41979|`71f2a67e02541af2402bdeadaa4d099cff8a342c68fae4682f55143fbfd5d9a6`|`e385f147dfe7355cee656d5dd08b4c206734b612`|
|[r769-meridian-whole-46169013968-1-shoot-420-level-0.json](r769-meridian-whole-46169013968-1-shoot-420-level-0.json)|51701|`d09e5167d42a3822cae633d8ad0e9ad2035cd14950fc97642a4e2dd21db51f94`|`e127cac751251c7bb01600d9bb0558562831a9f5`|
|[r769-meridian-whole-46169013968-1-shoot-420-level-1-geometry.json](r769-meridian-whole-46169013968-1-shoot-420-level-1-geometry.json)|41984|`12dd929fc12c9f120c6082e4188ce36a45d95d4f6e11b7c10e4be4bdab6b22c3`|`0bd01e4f6e3acc3dd16defff859255968a5c4702`|
|[r769-meridian-whole-46169013968-1-shoot-420-level-1.json](r769-meridian-whole-46169013968-1-shoot-420-level-1.json)|51689|`9b8bb162f9b26f2a81fc4b266b09d6a14ddb8c76c707824f286d822ff702d575`|`9ffb11595f4171d1a07ad635cfbfbb72f3bda0b5`|
|[r769-meridian-whole-46169013968-1-shoot-420-level-2-geometry.json](r769-meridian-whole-46169013968-1-shoot-420-level-2-geometry.json)|42062|`1e1457ab4891364e636d6dab092e9d1812d94445f028559d85a85ba9cccedf74`|`ade0ba7c066edee686d4b61e50e07ba0114509f2`|
|[r769-meridian-whole-46169013968-1-shoot-420-level-2.json](r769-meridian-whole-46169013968-1-shoot-420-level-2.json)|51752|`99d1413eafe7301863a36425ee2374b4a6f7e2c65ad34bfabe63c8f0e89f934d`|`e6042488ff699a098053f6a48cc00a50b69543ca`|
