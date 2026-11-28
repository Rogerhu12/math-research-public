# R770 / 46：改动真实外端、补偿单位桥与释放整帽共享边界的完整启动

会话 Astra-larger-e4e2a2bf-20261126；2026-11-28 17:03:50 UTC。R767/R768已在c867ffdad12eddb481f35a77ab607a19b0614695登记；旧.18硬端的任意内部误差>.042，不作本任务唯一求解类。此为完整理论与原输入发布；实际run、PID、冻结源及几何值在真实返回后追加。

## 解析构造与明确缺项

[R770完整证明](../results/R770-shortened-rigid-caps-and-compensated-two-edge-bridge.md)与最终13504B源严格沿用R767一个初g/整初像/握区，改变两整个外部真实轴退让为.40sin(t)，平面仍−ΔJ/2。初水平弦≤.37的相应边缘点对在每正相均严格缩短，包含R768被禁的.347弦；未把此估计推广到所有点对。

真实漂移脉冲p=[P(10u)P(10(1−u))]²在两端8阶消失，均值根β<π/2、.005<γ<π由正bulk/单调均值论证确定；h=0使用整函数和γ²坐标。两端.0005宽支持内分别指定实际原/新曲率的入射法方向与初外端出射法方向。共零曲率处的正规化仅乘O(u⁴)量，完整场两jet连续。中间真正非偶三矩自由保端点；局部改边后的三向矩缺陷<2.1e−11，在一对真实支持窗内以归一化单位向量修正，Hessian≥2e−9且|a|<.04的严格凸均值问题给唯一光滑根。桥整长gvv=1；两完整原外卷和两整帽仅刚移，三g与缝六jet准确。

以上仅是参考场的完整物理定义与部分度量结论。桥余gss/gsv及正相全嵌入/reach/无标记刚体商未证明。初reach≥.08/D<2.57与中央held>.55保原适用范围；任意拟合后场的全性质必须独立评估，不能借参考全管。源码的数值求根/积分不代精确恒等式。

## 实际有限维场

46的两族分别为三个非偶参考和三个偶参考；两族最终物理修正都可非偶。中央真场及整个右握区硬保。正/负两侧分别有共享world-F0函数的body/rim三Cartesian通道，贯穿真实桥、完整外卷、cap-normal、polar及Cartesian两整帽；只在桥内部另加C²局部、头部和端分数幂模。共享函数按真实二变量过渡拉回，中央边缘门具有零二jet；各帽的整个位置/法方向/二jet在共享场中可动。不会把旧硬端当作完成约束。

所有时间结点系数共同进入自然左端、右端零导数的三次样条；每个正结点及中点都进入同一个Gauss–Newton正规方程。原初g的正交标架测三行真实Gram，面积屏障及真单位法向四方向曲率惩罚可变，但最终独立报告整主曲率。每方向增量在实际训练点限制欧位移.045、原标架切向变动.23，九次原标量回溯，原CG上限160/rtol.0002/damping.0015。此限制是新算法的原步长定义，未删旧预算，也未声称它构成全局收敛。

| 原阶段 | ns/nv | 积分阶 | 时间区间 | 原迭代 | 独查ns/nv/阶/相 |
|---|---|---:|---:|---:|---|
| 每个六初值 | 20/8 | 8 | 2 | 4 | 27/11/12/7 |
| 两族各细化1 | 28/12 | 10 | 4 | 7 | 37/15/14/17 |
| 两族各细化2 | 38/16 | 12 | 8 | 8 | 49/19/16/33 |
| 两族各细化3 | 50/20 | 16 | 16 | 9 | 65/25/20/65 |

两族各自择优并保全4/8/16，合12完整stage。每族最后同一点再以定义积分阶20读取65相，并加入七原mesh相；保整闭拓扑、每点真二jet、两侧中央/桥内/卷/帽缝、宽0/.003/.01的真实normal→polar与三半径polar→Cartesian过渡、全三Gram、主曲率、双有向法弦、接触候选、直径、held、体积/中心矩。两个索引和14个压缩PLY整身份各对应自身全点。原系数与完整网格仅留runner，不上传raw/Release/artifact；完整源、参数、逻辑报告和整身份公开保留。

## 固定源、参数与公共执行

完整清单[run46-complete-preloaded-bridge-source-and-launch-delivery.json](../computations/run46-complete-preloaded-bridge-source-and-launch-delivery.json)为25758B/SHA256 80d1e7580a38c673644ea5a143066dca5c2c40574efe238794b68233f5150d0f/Git e7616b0ccd4ce7959c6ec33a8f931c531e84067c，列13科学物理输入（5新+8完整父）、4共享控制父、所有源/参数/observer/workflow的path/bytes/SHA256/Git。root已全文读各新源，参数文件与清单/请求完整对象逐项相同，现有父身份按新main保留；这只是源码和参数核对，未加fixture、微基准或科学准入。

| 新文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| results/R770-shortened-rigid-caps-and-compensated-two-edge-bridge.md | 10293 | a62de7ad629ac19ebd5f12223b06287e25f8d4d6e8d0e69caaeb18836d79d271 | c584d63572ea48152cd497056f81b418c6f97bcc |
| scripts/resume_20261126/r770_compensated_negative_bridge_two_jets.py | 13504 | 572f640a935cf10d64c8f0c828002eac18497d2ea5c32298980c45530f33c8c7 | 0c8ca6ed7f515d0f3ac9856f4eaffb013f285eb9 |
| scripts/resume_20261128/bent_preloaded_bridge_phase.py | 11469 | 9a32455ae600332b62f7cba3619e641d13f19bfaf0a0f9c509559274c8b1db62 | 2d8d324083fcc8d44b681f1654dfcfb7cd2ec2bc |
| scripts/resume_20261128/bent_preloaded_bridge_fields.py | 5037 | c37e7f9455cb4a2caffaff3bbbc8614ea389a8b86b709c897e9b628332d7f67f | 802a18ae4062caca6c1b1c26ccadf85a5e6abb19 |
| scripts/resume_20261128/bent_preloaded_bridge_system.py | 5861 | 507c6a8036b9a86b32b3477a0b7f7622382f134239f47d82a5758f598b1d23ba | bd32e670fcc15c8dee95d4ff846d18053dacbe8a |
| computations/bent-preloaded-bridge-phase-design-v1.json | 4156 | 4c9a47a7421c5ea95c8313067c65280a9dd6ee190b8477dc82e3eb534ff4c962 | cad4cabce135402a0e6562122a2806523e150098 |
| scripts/resume_20261128/closed_body_mesh_r767_terminal.py | 9070 | 2d7b3ffaeb67caf1e1962436b53608e79ffaca9c1c219d9909c3282e34b47720 | 9a3f96430485a976f6caf2ff7873b8cad035741b |
| scripts/resume_20261128/observe_bent_preloaded_bridge_search.py | 1536 | 61ebcf6289aeb241cc80357cad1cab9371923c2a6094dd8f3979a122ea3e75ac | a65bf8db700d208f1ae39050410c52c0b0e7e992 |
| .github/workflows/visible-larger-run46-preloaded-bridge.yml | 3957 | 2f1feedd74f1265accc101f1455d9b711e17309bda5734c273c04889dc861fe8 | f13688651255944b0c194c9c373a242083946d02 |
| computations/run46-preloaded-bridge-request.json | 19444 | 3636ef2ef67f667df6c636c833787157bd1a4e015384c9d7ba2dc46a53e2c244 | 7f85f40d968b2fa8b1d246511cece943126b13f0 |

公开ubuntu-latest、Python3.12.14/numpy2.3.5/scipy1.17.0、原4CPU/16GB；每数值库一线程。workflow超时360min是公共原资源上限，控制不额外切断child。触发提交固定所有科学和控制文件，2700s真正pull/rebase只推进规则/发表工作树，每次双README查差异即遵守；结果普通推遇NFF立即pull/rebase循环。marker为run46-preloaded-bridge。完整请求actual全null直到真实返回；程序成功也不产生精确度量/全相法管证书。

## 原完整12阶段和两套整场终段已真实返回

ROOT固定读 `47343a9ff8277efcd0d2d9a522ce328b14133d3a` 的16个完整逻辑文件：总note/summary、12原stage和两geometry，逐件bytes/SHA256/Git核同。官方 [46168504031/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46168504031) job `141051357172` 已success，七步骤全success；触发/冻结源码 `38422f433c00b4d35638d05f917e2205cd2e3818`。真实子进程PID2572，17:04:46Z启动、17:42:58Z自然返回0。Python数值库NumPy2.3.5/SciPy1.17.0；13/13实际冻结path/bytes/SHA256/Git与完整请求逐项同。官方程序成功只说明原完整实验返回。

六粗点、各族4/8/16原细化全部返，原每层4/7/8/9步及7/17/33/65独立相计数逐项核同；全部预算完整。末迭代正负两端CG均用满160并报status160，不能称线性子问题已达其容差。下表抄各完整stage的独立全相峰，不把score或训练目标替代真实Gram：

| 完整阶段 | Gram算子峰 | |K|峰 | 最小相对面积 | 完整点SHA256 |
|---|---:|---:|---:|---|
| 0 non_even-first-odd | 2.745094385416238 | 6283.457748196413 | 0.019351421318468027 | `bde9322163ba5a636ce121c4b5ee178a429a666930c8e3ffbcf327896fc2620b` |
| 1 non_even-countertwist | 2.9326805324342953 | 15116.721326687923 | 0.022684467871570215 | `8e5eb2db35e635390e8b9723c560f215b380daf6ea43b6472a4211cd1a4b82ef` |
| 2 non_even-third-sector | 2.43856479472481 | 254619.35492848832 | 0.004512009807690068 | `38fc6651966488d8363e334f560b8a9a32448bf2f7a42babf9f4ac114b3462ae` |
| 3 even-normal | 2.2825192730187682 | 320087.5047457332 | 0.0030296545691649904 | `e04cd91edeb33005b2389a159d3575cdcadfa6ee553cf307a691e36a147ee0db` |
| 4 even-first-yaw | 2.3776251384345475 | 2827.23178328855 | 0.035129860719979984 | `034c6470d5c2d179f1db9bbc9c5f03d1149300a4a59d397a9ee14314253bee82` |
| 5 even-return-yaw | 2.926512426941019 | 121437.66922836934 | 0.006454036859208569 | `334bef8c6b84d1b4293a4689e0199343a1a5444a443b2f1c4cc84f5a7fae007a` |
| 6 non_even-first-odd-refinement-1 | 1.576039716960652 | 9636.763276820748 | 0.019989353626734867 | `e6440e2d6ef917d9427dd31ca342708c1e851bda3450252f3c3829b3040b7e73` |
| 7 even-first-yaw-refinement-1 | 1.4034631321836584 | 1010342.9925257089 | 0.004091945814968837 | `b0c3ea7324fe2bbefc096f0435b4c871c706c0a5c47fc6e72e320b3b2abf84b1` |
| 8 non_even-first-odd-refinement-2 | 1.5738181325817298 | 15379.135595237789 | 0.02219517372127543 | `6543fd905294cabbccd622f039943752f6c290230e96a9a0197033de48c3818f` |
| 9 even-first-yaw-refinement-2 | 1.5207688748924961 | 27219.335822965244 | 0.014036707366151646 | `3d5014998f7a7ba134db2d4801ffdcb83d87074ddab2680866b8d901caca8575` |
| 10 non_even-first-odd-refinement-3 | 1.4230741971159806 | 394174.5057221898 | 0.0048893848810616525 | `48083de3d0734bc1ca0666788a077739fe8a0426e8c7af21dfb1fae8f4b9d6d7` |
| 11 even-first-yaw-refinement-3 | 1.422002610863204 | 253690.28663323272 | 0.006289305306916953 | `b0b27b11aac60426850bdf3a02be9394624d2aa98f92922c33c955e9b482c779` |

两支原最终点分别为non_even `48083de3d0734bc1ca0666788a077739fe8a0426e8c7af21dfb1fae8f4b9d6d7`、even `b0b27b11aac60426850bdf3a02be9394624d2aa98f92922c33c955e9b482c779`。原末field形状均[16,2,180,3]，actual f64哈希分别 `134204998d935cc44e31103e3b04636cdb2696b5253d3404a34fa48506f5584c`/`1d2f97dfbc91c2b605fed0574ad600ad9f803e2ecf950beb739cd3dcf0529f69`，各原NPZ完整身份仍在stage10/11。

## 同一真实点的两套闭网几何

两个终段都按原65相与7指定mesh时刻并集做69/69完整测量、69份细报告及7/7真正PLY.GZ闭网，errors=[]。每网22916顶点、45828三角、68742边、1组件、Euler=2、无缺双incident边/定向冲突、零零面积triangle。全faces i32身份 `de1b7f60238d7401cb30a7709cd09393f248d92683fa90e475110b1890ccf779`；完整14网字节/SHA256和每时刻顶点hash都保两index，raw未通过API取回或重复发布。

| 同点终段有限量 | non_even | even |
|---|---:|---:|
| 69相全Gram算子峰 | 1.426950971540192 | 1.4219372085533144 |
| 69相主曲率绝对峰 | 883724.3665781836 | 36017.07835596919 |
| 全对有序逆法球弦峰 | 8354.736458596884 | 7364.684888385221 |
| 69相直径峰 | 2.336740715823402 | 2.3366303212729505 |
| 69相finite-mesh Hausdorff下界峰 | .5809006534240537 | .5998040163978433 |
| 疑似额外三角接触对峰 | 568 | 474 |
| 全六jet接缝峰 | 2.8203280999412093e-10 | 2.816728379290958e-10 |

同点65相独立stage10最坏Gram1.4230741971在end−、t1.055378782065321、u1.9521663103256524、v.33；K394174.5057在end+、tπ/4、u3.85391350703255、v.33，最小相对面积.00488938。even stage11的K253690.2866和相对面积.00628931在另一end−地址；整网不同空间采样的K峰不同，不能相互挑小值。终段area_density_min约.00036是未归一物理面积密度，不能与stage相对面积混为同量。

两套终网初相直径同为2.3362980641406104、离散signed volume .9990564118122753。末相non_even Gram1.1131482258、K7288.7442、held有限网下界.58090065、volume.68596879；even末Gram1.22193514、K2042.6389、held下界.59699709、volume.72381766。体积为有限polyhedron量，不证明光滑商距离；疑似接触是候选计数，不直接宣告某个严格交点。小缝跳、闭网Euler及大有限held均不能支付全度量或管半径。

这两条完整有限细化的三Gram未接近1e−6，且曲率/有序弦严重排除这些实际点达到所需厚度；此处原12阶段全部完成。R767初几何及R770参考整经向/边界二jet证明仍按原局部范围保留；本结果不否定一般同g的全自由类，也不再把这12个已登记结果当尚在运行。后继不同真实输入继续。

## ROOT实读整件身份

- [run46-preloaded-bridge-46168504031-1.json](run46-preloaded-bridge-46168504031-1.json)：21006B，SHA256 `2ce516026b58a5ccd8d54e00b1de687cd9f487af44046bbe06857400126788ee`，Git `206f1622c9be29426718eda72beb2b45341ff50d`。
- [run46-preloaded-bridge-46168504031-1-summary.json](run46-preloaded-bridge-46168504031-1-summary.json)：15574B，SHA256 `c897a6620ff76304939d1ec7a5456195937c97b82c6c499ded37630033667fe0`，Git `aa8a4a953983457a2c96252da9f29ec1246820dc`。
- [run46-preloaded-bridge-46168504031-1-stage-00-return.json](run46-preloaded-bridge-46168504031-1-stage-00-return.json)：11742B，SHA256 `519e7777a2c4c9a2148be43b9abb3c63ac2d1d3f8f38d608f69b04daad022017`，Git `55e73a0ba396fc7bae381efe21b5a1b5a3df73b2`。
- [run46-preloaded-bridge-46168504031-1-stage-01-return.json](run46-preloaded-bridge-46168504031-1-stage-01-return.json)：11765B，SHA256 `66b8ab5a91b0456e39d3b5bd5f89a4d8ed9e3041facf4cef22166f524d66fc5e`，Git `f15d77efb311095d3d9900959842b3151ede8a83`。
- [run46-preloaded-bridge-46168504031-1-stage-02-return.json](run46-preloaded-bridge-46168504031-1-stage-02-return.json)：11728B，SHA256 `8bc28fb7afc05c14d784c3f8a0f3ec94246c0837a0c86f8c7e57a1aa30c2f388`，Git `d854e84322fd74ffb1ac7bfbb49c526913e2a767`。
- [run46-preloaded-bridge-46168504031-1-stage-03-return.json](run46-preloaded-bridge-46168504031-1-stage-03-return.json)：11652B，SHA256 `c370cabcba432386d50bc803635c4116cfde0deac90f9fe57432382b19172543`，Git `4ef4c08955f634b2015ce011ccaa5c5ef9766ac0`。
- [run46-preloaded-bridge-46168504031-1-stage-04-return.json](run46-preloaded-bridge-46168504031-1-stage-04-return.json)：11681B，SHA256 `e6602dca5327a7c33a8c4a8a9144610ade7ec731ce75f52ab23b547fbaaad213`，Git `b6d024d60a5992a41c2084ce8cd1e9cd9778950e`。
- [run46-preloaded-bridge-46168504031-1-stage-05-return.json](run46-preloaded-bridge-46168504031-1-stage-05-return.json)：11746B，SHA256 `f96c499a71466365ffba765451c0b344695824c85ffdcfd08002558efe7aeaef`，Git `6253e903b704a51e40f7a755ded422b745fb104c`。
- [run46-preloaded-bridge-46168504031-1-stage-06-return.json](run46-preloaded-bridge-46168504031-1-stage-06-return.json)：15453B，SHA256 `dfb7859fad08761fd83e0e1dd41e76c00a9a75d854a4b4bcbf357c72903b6820`，Git `1287457a53f493393976d907d251420f9eb30ebb`。
- [run46-preloaded-bridge-46168504031-1-stage-07-return.json](run46-preloaded-bridge-46168504031-1-stage-07-return.json)：15499B，SHA256 `62e39e09fe9cf2a7fae5129bf6517b82c2105903162ef70c88f1689e09977e20`，Git `1c1f515e18c83b9d023d9c64fd270ec36d9efd06`。
- [run46-preloaded-bridge-46168504031-1-stage-08-return.json](run46-preloaded-bridge-46168504031-1-stage-08-return.json)：18179B，SHA256 `475bf7a232e166af8a01a47cf9b40a56179a52b571565cfcd4f45c6bba0ce5e0`，Git `a41bcacfb35296b8332431306088498a935625e8`。
- [run46-preloaded-bridge-46168504031-1-stage-09-return.json](run46-preloaded-bridge-46168504031-1-stage-09-return.json)：18129B，SHA256 `b8218567ebb7f818576deaebd01f71f7de36a641bbc7cb1bc397784467dc08e3`，Git `333dc53ea432901e8ffb651ef92ccebac20e70b3`。
- [run46-preloaded-bridge-46168504031-1-stage-10-return.json](run46-preloaded-bridge-46168504031-1-stage-10-return.json)：22089B，SHA256 `04fb89ad6a90455dee3b1564ba776be283dac1d4b604ec2ec0657922d051e161`，Git `2b59621cb2c6d17fe60ca644314539deb956022f`。
- [run46-preloaded-bridge-46168504031-1-stage-11-return.json](run46-preloaded-bridge-46168504031-1-stage-11-return.json)：22165B，SHA256 `f6de6ade5976ac2e1bec2c2c53faf17258f8af7d39d94516aeac426b1c1f4225`，Git `4b327a68a77922c88e7cee59a2d2a1e12faa4d4f`。
- [run46-preloaded-bridge-46168504031-1-geometry.json](run46-preloaded-bridge-46168504031-1-geometry.json)：32674B，SHA256 `9e27fd2dd3a617d9f95a2979d2f05af02dd01354a2a533539e4e0d925f0c8966`，Git `af8c98842014626120175b16745765368601d901`。
- [run46-preloaded-bridge-46168504031-1-even-geometry.json](run46-preloaded-bridge-46168504031-1-even-geometry.json)：32674B，SHA256 `f4ae494b27965d5f9dfb114c4041a722c5a7ba0a3965bcd97e2b5ec27df3f51f`，Git `2d7322c2eb81655e422e79b6179716c77aabacc7`。
