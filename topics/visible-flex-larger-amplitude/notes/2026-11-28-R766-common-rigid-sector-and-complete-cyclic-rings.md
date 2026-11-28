# R766 — 临界曲率零障碍、真实共动右域与两整周期预带的完整公开计算

Astra-larger-e4e2a2bf-20261126（AI）。接R764四整球全部原拟合失败与R765完整等价方程；不重做旧结论。本次[完整证明](../results/R766-critical-curvature-zero-and-common-right-cauchy-ribbons.md)与[13源及全部启动参数](../computations/r766-complete-cyclic-metric-ring-launch-inventory.json)先完整交付，再由真实公开Actions执行。当前run/job/PID/实值均未知，不以源码冒结果。

## 一、实际K为v²时的C²边界障碍

旧R764 prescribed central trace在原右正圆弧的一段正相变成真平中央，而初固定g在其旁的预带满足
`g=(1−κ0 d(v))²ds²+dv², K_g=κ0 d''/(1−κ0d)`。
`κ0=1/.15`，`α=.0025sin(2πv/.44)sin²(πv/.44)`，所以在真实固定角段有 `K_g≥c v²`。

若仍硬接原平中央的全二jet，C²图函数h在y=0的整个Hessian为0。以ω(y)→0控制h_yy和h/y²，Gauss方程正定性给 `h_xx≥c y²/ω(y)`；沿固定长度x区间积分二阶差分，则左端至少 `cb²y²/ω(y)`、又至多 `2y²ω(y)`，矛盾。这付清真实零曲率连接处的障碍，而非仅用非零曲率公式略掉端点。它只排旧硬平中央trace；R764 fully_free能改变该trace，不能据此宣布整个初g无解。旧K=O(v³)、h~v^(5/2)结果不处于这个临界次数。

## 二、完整闭曲线与同一个刚动区域

仍用R764完整初g，B=.88、E=.44、原corrugation .0025、两标准卷与两个真帽。中央新角先用
`εθ=.025+.975exp[−(θ/.025)²]` 将旧moving与original作真实角插值，再用原水平材料区 `[-.95,.15]` 上宽1.10、两端.22的S7 bump闭合。b唯一地解整个上半真实切向的z积分为0；其质量.88、b∈[−.45,.45]，实际两端符号有严格余量，闭合缺口<.310且端控制>.38，导数严格正。phase0回原完整剖面；上下反射闭合而不是接两条任意开曲线。

原右U转从角1.05到π−.38用真实变速 `ψ=x+ω B1(x)`，两端.14的S5圆化负坡，`ψ'>.42`。自π−.38起的整原弯尾、其真实κ0=0开平段、四整右壁elbows及下反射统一保持原切向。全新中央曲率|κ|≤7。握持邻域按其一点和切向真正对齐到旧moving grip，最终通常刚转后整个有内点握径≥1.40。右共动域用另一个刚体Jθ；两刚体由连续真实中央曲线相连，不强令它们相同。

该共动右域跨两**整个**E预带、两后续标准roll及相邻真帽域使用 `Jθ F0`。原曲率零段及两端所有六jet都包含在域内，无除κ。两**整**真正帽面也用同一Jθ，全部三Gram准确；该刚动片并集内部的任意两点继承原.132有序法球。涉及其余自由区域的对不能借用这一结论。

## 三、未付区域是完整预带与后续标准卷

互补预带导向把中央真实位置过渡到刚动原末圈，轴向为 `p(v)−η(s)S5(v/E)`，`η=e(θ/.90)(1−χR)`，e=.13/.14。它允许真正末高退让；互补标准卷再用全长L上的S7接回同一整帽。两端整个原卷都在定义域中，不能只核预带后忽略中间连接。

原初面仍有reach≥.132、D<4.386；新导向final held≥.88及固定握持的分析界见完整证明。自由重建预带/卷的全嵌入、法管、商距及held必须重新支付。尤其“两个真帽与右域同g”不是整壳同g，导向终位移界也不覆盖任意优化场。

## 四、四个公开原完整周期三边计算

两退让e=.13/.14 × 两真实三角对角模式forward/alternating各独立进程，每个进程计算两个真实符号端、整个材料周和整个v∈[0,.44]。三层为 `(96,12,16,16),(192,24,24,24),(384,48,32,32)`，依次是角区间、纵区间、物理积分阶、每遍非线性预算；另真实握持锚点及其反射也进入角环。

每个新环顶点Q_i先落在同时满足原子午边a_i与原跨三角对角b_i的真实三维交圆上，再以完整循环 `|Q_(i+1)−Q_i|²=c_i²` 解所有角变量，包括末首接边。两个真实非线性遍的reg=.001/0，原16/24/32 nfev、内部180步及全部tolerance见inventory。共动右域硬固定，但三项实际价格仍全部重算。若圆不存在，则用同样完整三边的Cartesian三向问题、两倍原nfev继续，记录fallback与真实残差，不删角、不删纵带，也不声称该分支已离散准确。

三边准确仅为三角片的离散Gram准确；最终场另做完整连续检查。周期角三次/纵向五次样条重建C²场，记录并平滑付回原polygon与真实central的偏差，中央端D=D_v=D_vv=0；预带末真D、D_v、D_vv在整个标准卷按
`(1−S7(w/L))(D+wD_v+w²D_vv/2)`
连到刚动整帽，并用相同角权。此处真实末二jet来自已算物理场，不能把它替成原导向的零值。

每层13个真实积分相 `0,.075,...,.90` 与12个独立连续中相，后者使用同一真实系数词的S5时间插值。独立11个整壳图检查全relative Gram算子和三分量、主曲率、support、相对面积、原held witness及真实弯尾/zero/flat/right-wall六jet。每层“完整环价格”和“完整重建整壳”各一小报告，共四×三×二=24科学报告，另总index。参数不减，未知字段不补猜。

## 五、完整来源与真实运行边界

完整13个源与workflow/proof的bytes、SHA256、Git blob均在inventory；十个原父在实际main逐项核对并保持。新四运行源（几何、solver、controller、workflow）的最终身份为：

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| `r766_positive_boundary_curvature_and_exact_signed_ribbons.py` | 7769 | `df177787c3e825258d480a9a1134f3652ef2dfebe2eae3fe2aa3026b20f26454` | `b570f579890526fa8f72fff691589f83ceeadc4c` |
| `solve_r766_cyclic_pre_rolls_and_closed_caps.py` | 17628 | `d1f24002e6efcf31ec6cb32994da3633a9067164d49e5a76d77c72c26c12060f` | `cf7bde1f74306aae93401e528b647f30651823fe` |
| `run_r766_all_cyclic_metric_rings.py` | 11758 | `4bee0fc20ff2ca4fa522ce8837200d0d0680c7cbbd045fa16044b85fd52494df` | `59b3979bebba3091f3d4216b4fc3ddc6746b88f9` |
| `visible-larger-r766-cyclic-metric-rings.yml` | 3885 | `edf8f5680fe58821b1d1ded4627d27247799a5ebd28f8f213072e252a5fcafb6` | `223dd094abca34db8dfab0bcbd462201ac01e3e8` |

证明 21216B / `d9a8ce7dffcf3a87d3482d04db202438eb86c2cdbac73b67d27fe3b1389a2b4e` / `cd5a00e4818f929d438f8c82f40100579a621cbc`。
inventory 6658B / `9f7dd9bd6d4ecf6f7f508352348540a22e9695417882aa7958bcbb838254e9fd` / `4cd61e3663ba477cb494429f2767d42bafd8ae48`。
旧草稿几何和掩码变量修正前solver未发布、未执行，不作为任何实值输入。

公开Python3.12、NumPy2.2.6、SciPy1.15.3，四独立进程各一BLAS线程，原355分钟完整运输窗口；触发GITHUB_SHA冻结全部13Python，规则HEAD单记，每2700秒真pull并仅读README差异，若规则改变即按真实变化处置。非快进原pull/rebase再推循环；题200MB与H10KB均核。全部每环浮点词/位移词/raw留runner，只刊完整小结论和whole identities，不在此加本地AST、fixture或准入试跑。

待真实run返回再核source、所有退出、24件是否全部存在及每件来源；程序成功仍不等于README完成。课题工作继续至全标准。

## 2026-11-28：四自然进程、原十二层与24整逻辑报告全部返回

官方run46165595977/1、job141042306386已completed/success；root独立读官方run及十个job步骤，均success。四进程alternating-130/140、forward-130/140自然exit0；触发/科学冻结保持43914b1da832b13ffc65f9f3074446217fc065b9。完整index在2e27068e0126f7079eb72cdcbb827a8e9d71f203：11128B/SHA256 8db6e248d65a0b37942d7039bd3eb4f363922711dc7e73da8472b2301fcfedc7/Git72fdb9ba6597b7fd60f4338e784ab8acabcfa452，记真实双README pull到ad73bb14ba73d3d5b6e6f2d64c689a486084c358；13实源bytes/SHA各在该index，保持触发包。ROOT另完整读24份原报告，全bytes/SHA/Git一致，run/attempt/source及每rings13相、每surface25相逐一一致。

原3层(96,12,16,16)、(192,24,24,24)、(384,48,32,32)均执行，两侧完整每环及原fallback保留。下表只列实际末θ=.9，全部13环相和12中相的完整值仍在原报告：

| 分支 | 层 | 全11图Gram op | 最大绝对主曲率 | 最小支撑 | 全图样held见证 |
|---|---:|---:|---:|---:|---:|
| alternating-130 | 0 | 10.261579585920776 | 202.82864938138437 | -0.6048894795352315 | 1.6699659641447968 |
| alternating-130 | 1 | 101817.76855500357 | 409572.008957608 | -2.4130400297960697 | 1.6699659641447968 |
| alternating-130 | 2 | 436366.45105950057 | 99964.08717367916 | -2.328205574090502 | 1.666083598282757 |
| alternating-140 | 0 | 8.980248841816344 | 94.24961229819397 | -0.0493479274352443 | 1.6699659641447968 |
| alternating-140 | 1 | 123234.19979096668 | 189632.8194820956 | -2.2934092300464775 | 1.6699659641447968 |
| alternating-140 | 2 | 220749.2186458966 | 412832.89216297603 | -2.3508058588523832 | 1.666083598282757 |
| forward-130 | 0 | 8.666812547807549 | 102.73485264448769 | 0.041213268306059495 | 1.6699659641447968 |
| forward-130 | 1 | 122292.73209652254 | 328465.550052896 | -2.358267460606314 | 1.6699659641447968 |
| forward-130 | 2 | 134603.21209295682 | 129211.60139413847 | -2.3572274890924874 | 1.666083598282757 |
| forward-140 | 0 | 8.64739143603103 | 100.2753978237894 | 0.06800793006116895 | 1.6699659641447968 |
| forward-140 | 1 | 2052.6929281586918 | 14115.244938520926 | -2.0151172865803577 | 1.6699659641447968 |
| forward-140 | 2 | 457166.83422903426 | 158414.76143733552 | -2.337521797215297 | 1.408046653549295 |

四路末层整壳均未达到1e−6或厚度标准；细化从粗层g约9–10升到10^5级，不构成收敛。主失败在从循环点列延拓到完整C²标准roll的连续三Gram：alternating130末层round− frame11=436366.3906321675、frame12=8257.072723940799、frame22=2880.400239070837，整op436366.45105950057；同一场preband+曲率99964.08717367916。不能把离散边价格或精确中央/刚帽误作完整度量。

完整三边实际价格确有区别。alternating130末层正/负首边均约5.5e−14，但上环边最大1.2261989049334/6.994263715264912；forward140末层两侧分别发生1/2次真实Cartesian回退，三边最大[.10963513127883373,1.1618636354403873,14.517585570492356]与[.0977138660296899,1.321678464557921,10.048713444005346]，故连首边准确也只适用于未回退的相应行。中层forward140上环边达548.5730534400741，所有失败行均被保留。每行原record/全部浮点系数words的整字节和SHA留逻辑报告，原raw在runner；没有删难行、限缩原环长或停止后续原层。

R766严格共动右域及原帽结论未被这次失败改写：末alternating130中央g≤6.661338147750939e−16、两polar帽约6.24e−14，真实右域预带六jet差2.5134354233319334e−14。它们覆盖原证明限定域；互补自由域巨大误差不付。初相整图误差亦在机器量级。所谓样held只是原有限图值，未由该数产生全相嵌入/reach/δE证书。

该四支完整有限周期求解失败已闭；新R769/771改全长单位速场并释放真实外边界、R767–770/46更换预载初g及端姿继续，原历史结果/全部预算不可重写为全自由类不存在。

### 原24报告与index完整身份

| 公开notes文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| r766-cyclic-ring-46165595977-1-index.json | 11128 | 8db6e248d65a0b37942d7039bd3eb4f363922711dc7e73da8472b2301fcfedc7 | 72fdb9ba6597b7fd60f4338e784ab8acabcfa452 |
| r766-cyclic-ring-46165595977-1-alternating-130-level-0-rings.json | 13899 | 27c10e961dbe966436ec13406d88686ebacef94155570c2749d12308e8efefa4 | a64143e4e07c0bb250771cc92d2dcfa8115ecd53 |
| r766-cyclic-ring-46165595977-1-alternating-130-level-0-surface.json | 48484 | 566182e5058fe7ebc702b970e74fca046931469f211b203dcff773ee8be4b17d | 58c4f8ec65316fb16fdb9fd07b46dcf6c323d040 |
| r766-cyclic-ring-46165595977-1-alternating-130-level-1-rings.json | 13965 | d79a477ca3c76765f571e284c86684d7264e4f94bc306e9f8f1be02fef4c6abb | 92c760d57da107a0d041cf289d4c1f65f3185b83 |
| r766-cyclic-ring-46165595977-1-alternating-130-level-1-surface.json | 48309 | 16f12f4f3c035a14f672c73f4977617570a610af1acae10504f8210c5a1ec890 | 6aacbe6bd097b227a16e53f2f8a05aa9c1394673 |
| r766-cyclic-ring-46165595977-1-alternating-130-level-2-rings.json | 13976 | 9eb1ce510af33d0975f90b751ce63ad85627111cc27387ebf60bb599614c35f7 | dabccf868a8d558e4f1b7c2e91265a1a6bebf09b |
| r766-cyclic-ring-46165595977-1-alternating-130-level-2-surface.json | 48489 | c598c65cc4aacddd43d303c8c6d55a9f8c4c292d747f9a3c54de0e80030b4da7 | 2021af26b07b1a6f79224c6975f1bcce44fe4536 |
| r766-cyclic-ring-46165595977-1-alternating-140-level-0-rings.json | 13902 | 1c90b3593ed14c3454fdf9751d9972d8b14a26f9e035dcd3e5f717801492d40c | 2cf366d25584f647624b3527032ef4b88abf5d04 |
| r766-cyclic-ring-46165595977-1-alternating-140-level-0-surface.json | 48468 | 915cac57428b7de28edcf6fb12bf31873a2433e8d03aaa7cfbe72650a926d9ac | c3e5146ba0fa00f28b85574895bf6bec22bf450d |
| r766-cyclic-ring-46165595977-1-alternating-140-level-1-rings.json | 13960 | 173fae673d3220eb3ef7d7d1d583982f0a2e7fe4226f3ffa8caa3bbccd3826d1 | 6ac21b25c935d3c63bf34ed8ba7533dc134f740c |
| r766-cyclic-ring-46165595977-1-alternating-140-level-1-surface.json | 48275 | fad73e5f19dee9c3b864695e57e60d9d3e39e9e7b9521a1e6a6e688122c41ab2 | ed1b7db50de3e0f11c505cc9e63d7ea3a136e242 |
| r766-cyclic-ring-46165595977-1-alternating-140-level-2-rings.json | 13989 | f3845fbba223eb9b0d84f902442b180c994a95df6417c896cd20c0916c86a387 | 85c9ef44585d3464eda8c2194dd587aad5e1196b |
| r766-cyclic-ring-46165595977-1-alternating-140-level-2-surface.json | 48457 | d040075328d74c304795448f3fb42d1ceb59d64683f5ad6f3e953fa0fbed454f | e10aa6e314a7fc4103cdbddfe8bc300d40fbbfad |
| r766-cyclic-ring-46165595977-1-forward-130-level-0-rings.json | 13885 | f3b2c1b0a3dea2db4c38dab5f86b9f12118006f551def1e511e0db10476a7ceb | 6ddd0dcec7336de09d7ab588f9ca11038e7ccc8d |
| r766-cyclic-ring-46165595977-1-forward-130-level-0-surface.json | 48482 | e4b7649ad90bc91effe59848cd09d242708cec127eb099c26943b8e5a91cce24 | 98c1fabb47451357ddc55c00add68786ffec45f3 |
| r766-cyclic-ring-46165595977-1-forward-130-level-1-rings.json | 13935 | 9e9d6d05f191e5c1470f91369061dc5e90a6f65c92014847e07c3a9b16d11041 | e9bc399a169ca35f708a3fab1c12948199dcb577 |
| r766-cyclic-ring-46165595977-1-forward-130-level-1-surface.json | 48344 | 24adc47480447b0d78506a3de66547fb26c1bda9eeee16975c2f30d77a58b902 | 33da2a742504de0108f024a7d3d4f0363e73a6e8 |
| r766-cyclic-ring-46165595977-1-forward-130-level-2-rings.json | 13967 | 4b37a00773d7ba39893b0f3c266322bddc46190de9bfea2d935a238daa2780e7 | c8d0ccab887097f8d053f031f2f7add470382746 |
| r766-cyclic-ring-46165595977-1-forward-130-level-2-surface.json | 48547 | 5a0a9964c22dcf02b0afbf89ca3adf025114d7891242e33e3d51231a86aae4c6 | d4ae5a769e5b84388cf491a25fb7b5ce45c19dd5 |
| r766-cyclic-ring-46165595977-1-forward-140-level-0-rings.json | 13885 | ecb059f941700fae4b8c2f629bba4a5030a5a13bb0253de1e1c61116eb57349e | bfc274818a4eadf4408a8a1f826f978bf8c5082d |
| r766-cyclic-ring-46165595977-1-forward-140-level-0-surface.json | 48480 | e7014a0de1aa5b1b10c3ad1571dd7685d9cbdf11a11f205f4953bca9e3bd0efa | 34b6c47966003998aebfabccb53d36ed635e341c |
| r766-cyclic-ring-46165595977-1-forward-140-level-1-rings.json | 13935 | 13784f045e5e70a27ef1f771f967665ac5bbd25f9b2c8c34bb59f2f35e90f911 | 90440265287c849fc83c4e03971c5777b7143063 |
| r766-cyclic-ring-46165595977-1-forward-140-level-1-surface.json | 48334 | 8c22b1441a22fa0fe5a4b4360a36f32b920fd28cb0408b3e4064db0d1665b50d | a407322da7e8d14f5be28d88592ab6351af0a8d2 |
| r766-cyclic-ring-46165595977-1-forward-140-level-2-rings.json | 13955 | 8db7d718df3a7d0ca66e293cecb06b78a18e56ab9eeeca8d3a52ab43e53290b6 | 5a432bf98f2418fc1b22d0130dbc5ed1a0b8f3b5 |
| r766-cyclic-ring-46165595977-1-forward-140-level-2-surface.json | 48560 | 8747ff4f2a33f6cf92e2ae4d998f8016c533a2a8c70ddaee74fb29a9961d0ccf | 018a0cbc6f33135a2276944a522a4f035061e8f6 |
