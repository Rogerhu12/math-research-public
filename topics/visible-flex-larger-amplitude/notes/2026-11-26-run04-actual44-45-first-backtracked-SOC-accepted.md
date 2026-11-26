# run04 实际44/45：完整后退锚 SOC 首次通过真筛并接受

日期：2026-11-26。范围：公开 Actions [45857104277/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45857104277) 的实际44科学方向和45纯归因；这不是旧41失败的补造结果，不是研究完成或连续几何证书。

原证据为[第4卷](2026-11-26-public-actions-45857104277-1-part-004.md)，截至19:56:58 UTC的索引确认两步均completed/0。亲读版本 Git blob 为 `c33113b0841d32cbfa030e8250c14e0154778cb6`，完整公开紧凑卷54,901字节，SHA256 `c1b0b7ad80577cbcd4851dd2f1ab001623994851bbe27dbeb69f99b7fb287e63`。科学raw仍仅runner；没有从大报告搬运数组，也没有本地重算F、J、QP、根或几何。

## 1. 确实接受的结果

实际44从同一固定模型、目标和范数的实际40末父继续，真实接受的是SOC修正候选。实际45完整source-body归因明确给出accepted_SOC=1、accepted_original_ray=0；不是把“有一个方向”当作“接受了一个方向”。

| 项 | 实际值 |
|---|---|
| restart checkpoint | `51c8b09be1b1d5baef8c0f5b18f294130727429aeb01485e1b78a72d442d509a` |
| restart report | `78fa207b9032f3455ab3037189f0896f2533e4534c8e573d67a326444f442b22` |
| 完整原物理父bundle | `fcce34129466c5e19df169308c38b76795feff7f7b2384bbcdb10189461d6375` |
| 当前完整模型 | `ac2cfc0d46a75a2070dfd9b208e3802c895a7bd35a9df5ab60d1016c81aebf19` |
| 固定scalar目标身份 | `2612418a7f6dd3718ec340a37e7793bbedee0a3423f90a4a15c028cdb80492df` |
| 当前完整坐标范数身份 | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |
| 新final checkpoint | `9c9f4726d6f6edd23bb874e84aa0f7de91347729de408a11eb5073c3f808a011` |
| 同Phi initial→final | 0.005735011506412643 → 0.005665053856316854 |
| max relative Gram initial→final | 0.03526432751600142 → 0.03513609110016425 |
| 真有限约束最大g initial→final | −2.3109635316487243e−9 → −3.6401591740897743e−7 |
| 完整metric/restoration方向 | 1 / 0 |
| metric/restoration末阻尼 | 0.01 / 0.01 |
| 全永久地点末计数 | curvature2063 / radius2012 |
| 最终全部永久地点真读 | true |

这里的Phi字段明确来自`centered_phi_normalized`。新入口对实际40点的初次浮点读数为上述initial；与40报告的微小末位差异不能当作一步优化收益。唯一同版本比较是44自身initial→final。该范数是本normalized-parent分支的jet-sum范数，不能与direct-axisymmetric integral的Phi/Pg做跨目标或跨坐标相减。

## 2. 完整锚、内层未驻与真回读

原完整QP运行64 advances，返回`iteration_limit`，最终面投影梯度1.3111335722837292，容差0.000004488897214745175。因此该方向远未达到其声明驻点判据；这次真接受并没有把iteration limit改叫收敛。

原ray回溯找到真可行fallback在alpha=0.0078125。随后选择紧邻的较大、Phi真下降但几何拒绝的ray作为固定修正锚，alpha=0.015625。实际45给出：

- accepted step kind：`complete_separation_SOC`，accepted ray alpha为null；
- 实际SOC候选数1、SOC projection calls1；
- 实际最终候选完整回读1；
- accepted original ray0、accepted SOC1；
- 原QP实际秒1171.7448172740005，整个方向1622.1816664889993秒。

这些字段证明本次采用了已声明的后退锚策略及其独立真筛。它们没有公开修正范数、全部新增线性行数量、投影sweeps、最终每类约束和逐地址表；不能从一个已接受候选反推这些未读量，也不能把有限行投影本身称作全局几何证明。完整代码保同原父/同锚、全部原C前缀及新增行，所有拒绝发现点永久保留，候选选择后按最新永久集合重读；actual45的whole_body_match=true核到实际完整892f源。

## 3. 来源和完整输出

| 项 | 实际SHA256 / 身份 |
|---|---|
| 实际44 source commit | `d55c2d28d22240f9f172fb9e43582c9ed7d96c5a` |
| 完整launcher | `6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e` |
| 完整driver | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| 全行helper | `e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021` |
| 原projection | `a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e` |
| 实际45 source commit | `d7c321d2b6ab3c447855d874163f6bad9909c39c` |
| 完整pure reader | `009e1e1d54ccd41e8ac2b4e6efe43541ebc327b7a6f3d4fa743e145517c897e6` |

科学输出目录为`so3-closed-actual-profile-cached-backtracked-SOC-v2-first`：

- report：`08e30bd4176b73697a9008904bf23d5fecb0a46bcc493f06463299c877679fa5`，23,846,858字节，仅runner；
- command：`5ba18e53f64d8ef3f4764e86d98dc55826f9e2672679d9032e4bb4aa2885466c`，15,215字节；
- initial-new-field等于上述51c8 restart字节；final等于上述9c9f，二者各10,720,258字节；
- pure summary：`fc15d13d7b0e5c5d0a45a6d00088bdf5e4b894501c3d2524324c14b267470045`，155,917字节，仅runner纯消费。只读了公开紧凑映射，没有通过connector整读它。

实际44控制器耗时1994.287288255秒，driver实际总时1986.2209937879998秒，初次完整setup和场读358.14907669999957秒，峰RSS2,996,600KiB。实际45耗时5.942284280001331秒。两步summary_errors与missing_outputs均空。

## 4. 原cache与永久地址责任

本次cache实际adopted1643、fresh6，45重新核文件bytes共1649；44另记录missing_planned_files=7。不能仅从这几个计数推断哪些规划query未使用或每个文件的计算成本；完整实际manifest继续负责逐文件与逐query归属。

cache setup6.577464305000831秒；完整manifest SHA为`0f38a8983f3d5e251cd9cc8943ad80adf1af618fc6aec072167ff4abe272b030`，completed_run_snapshot=true。原234ac/d3f物理provider、同run/fixed-parent身份、查询地址、每文件字节继续由完整50a9核；未把当前自由场、旧父场或另一run cache互换。

原全空间1,333,370自由变量、45,324,288正权metric行，原全部可用geometry前缀/幅度行、完整原freecore/H均保。全局body/held-set幅度与reach仍需后继同场连续证书；实际45明确continuous_certified=false、isometry_accepted=false。当前max约0.035仍远高于题目阈值。本条登记的新增数值结论仅是：在这个真实父、完整预算和实际最新记忆上，后退锚的完整SOC首次返回并真接受，且同Phi与最大metric误差都下降。

## 5. 可直接接续的完整责任

已准备独立两步参数`resume-20261126-run04-actual44-backtracked-SOC-next64-ready.json`：以本次9c9f/08e3作为严格restart，采用本次已完成cache，显式保39/40/44所有报告地点，同源、同范数、同固定g、实际末mu0.01、1×64与restoration4×64以及8轮SOC政策不变。这是待root实际排队的新完整方向；本note不宣称它已运行。另支direct integral后退SOC需要独立真实源绑定，不能借892f的normalized-parent标签或这次场的证书。
