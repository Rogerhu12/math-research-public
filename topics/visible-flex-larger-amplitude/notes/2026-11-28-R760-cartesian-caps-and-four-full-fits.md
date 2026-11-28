# R760 — 真 Cartesian 初帽、较缓返回墙与四项完整物理求解

会话 Astra-larger-e4e2a2bf-20261126。**全课题未完成；本件登记一个真正改变初g的输入和四个完整实际过程，不把原R758的失败读数移作新输入的费用。** 旧初帽的严格K>21000障碍已另见[R760原输入排除](../results/R760-original-R758-cap-intrinsic-curvature-obstruction.md)，原四路全部返回见[R758全记录](2026-11-28-R758-curved-crown-four-complete-fits.md)。

## 新输入的已证明范围

[完整初始厚度与活动两端证明](../results/R760-cartesian-cap-join-initial-global-reach-and-exact-active-ends.md)定义以下唯一新初场：

- 真实上返回弯段长 .95、初截高 .92、最大角速度5.4，四段平滑转向1.44/.71，初/全相位缩放分别<.356/<.833。原真实固定圆握及左右两半闭合保留。
- 两帽采用真实宽 .007 的法向平面领、1.5e−6端平高度，内部完整椭圆碗采用物理Cartesian二次函数和q宽 .014 的紧支撑延拓；两个支撑分离。领物理Hessian范数<.5、整个Cartesian碗<1.87，整体初帽梯度<.00075。
- 原完整闭曲面初始reach≥.132、D0<4.01、固定握径≥1.40。基线全相嵌入与初末整像held>1.09按完整证明；两完整活动右卷和真正曲帽领严格保持新初g，两个主曲率均≤1/.132。
- 初相之外的**整个**帽环带/过渡区同g、全t reach、优化后嵌入及刚体商位移仍欠。刚性内椭圆不能替整帽，准确活动右卷不能替其余整圆周。

新metric取本源码九图完整F0的pullback。R758只作为实际旧点对照及完整旧collar-clock/expj父函数；它的初metric不再作为目标。

## 四个原完整实际过程

两个signed半面各有outer_locked/free_end一项，共四个独立进程，每个数值库单线程。一个mode的两半在共同中央重叠一致，合起来覆盖九图全部真实闭面。所有空间三个分量均参与，不只拟合法向高度。每个原两径向/角包另有15个固定初始物理(x,z)高斯局部模式，共30个三分量函数；物理基函数的完整六jet参与独立metric和曲率读数。

每个相位先给整个内椭圆冠独立SE(3)姿态：24条真实原径向路径和24×24条完整初椭圆内部投影弦上真图长度，对对应新空间弦的正超额作六坐标拟合。有限旋转用真实旋转矩阵，原姿态预算96 nfev；姿态只是科学初候选，全部后续真实非线性拟合继续。各阶段同时返回这个原姿态和路径费用，不能用短弦必要条件代替存在。相位间使用五次端平插值作用于旋转向量和所有物理系数。

三原空间层仍为(角节点,横区间,积分阶,Fourier阶,径向阶,nfev,LSMR,独查角节点,独查横区间)：
(24,6,16,2,2,12,12,64,12)，
(40,9,24,3,3,20,16,96,18)，
(64,12,32,5,4,30,20,144,26)。
每层七拟合相位0,.15,.30,.45,.60,.75,.90和六独立中间相，不删低分/失败行。每支21拟合+18中相，四支全部返回原训练与独查五图的metric、绝对主曲率、support、面积/退化计数、全系数身份和真实路径费用。固定g/几何都重算为本R760，不读R758未来/旧优化系数。

科学程序还在旧R758与新R760各自真实右赤道rho=.84、七相位直接转换物理Cartesian梯度/Hessian并计算K；这是两套真实字段各自的诊断，旧高值原样保留。没有合成fixture、额外准入或缩短科学预算。

## 源码与普通启动

新完整件及全文证明：

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261126/r760_cartesian_curved_crown_and_lower_rate_walls.py | 10422 | `a20f2ee98d901cadb6290edbbb8ad1f8a52d5b6035e6507c171ddea93febf919` | `ec2e06753824f38d3c8ace40a8cf4deec0e51f23` |
| scripts/resume_20261126/solve_r760_curved_crown_middle_annuli.py | 20834 | `0e1e4d9f76221c43938b3c839c95f8ad51e487df1edf52b952d6f913cba2ed72` | `1bb5c19e45cc7e6e6b306309f5cae91a9875e346` |
| scripts/resume_20261126/run_r760_all_curved_crown_fits.py | 10818 | `f36a3fe3dd438ecfd9ea761171fce9a642bc6f379a9a5dca36787c7634791c65` | `6555d340f9054617aa7836716fc5ec095f1145bf` |
| .github/workflows/visible-larger-r760-curved-crown-physical-fits.yml | 3488 | `9d11c5b5e9c5b890e752f8050145828fc6c37263de91256f181f15b4be893279` | `387a2bfbda573887cafccb2a38c02ba31bc7ee8c` |
| results/R760-cartesian-cap-join-initial-global-reach-and-exact-active-ends.md | 13736 | `fb99639bd1f217165d98bce6007b18a9ab627210a832adca866f290ae64ce5e7` | `14fadd02ee0f46206a19dacb5d9eceb74835028c` |

所有七个既有原父：

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| r740_rolled_disk_seed.py | 10834 | `b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f` | `72ef28649a33d115ef9a646a581f61dc3f3ddece` |
| r742_tilted_disk_two_jets.py | 9706 | `5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd` | `eacaa69d88eae15963aee90d948391abfb9c745a` |
| r744_extruded_closed_two_jets.py | 10327 | `35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24` | `729efd888029dbaf9953617edfde81c0c7394fdd` |
| r754_coherent_mirror_bowed_walls_two_jets.py | 9754 | `aedac63cfc0ecab05108b7d1d8ea62d5fcc0ee48e3a60c09c6fe7214e829eb96` | `0f20d4a812f5f3c32526277548fc641b75864ddd` |
| r756_return_elbows_preloaded_exact_rolls.py | 8933 | `39e166b6482078f39dc8bd2ee360a7a42ec02650145c85f5ebd78d7e32ec5a38` | `3daf3aa1a455c8886cd7dd92ab2f3ff0f541883d` |
| publish_r734_exact_conclusion.py | 10589 | `a18fb8ef978c8220c5fa918ed25b348ac35b3d2b24758324bf73d51351a0b4dc` | `c07d8a51f944dbacddabd127522d673174498839` |
| r758_curved_outer_collars_and_fixed_elliptical_crowns.py | 6352 | `54554808a73d93149a297a7302093d0afcd0b8d433b2d119223a2a2792ff40bf` | `c88481deaffb78453316a31bd6e607ca774226ab` |

公开workflow由本次普通main推送触发。controller将上述七父加三份新Python共十源从trigger SHA冻结在独立科学目录；规则/发布main另作真pull，禁止把后来规则HEAD偷换成科学源。固定Python3.12、NumPy2.2.6、SciPy1.15.3，避免已登记旧Python3.14/NumPy2.2.6别名破坏；原平台355分钟和全部拟合预算保留，没有新子进程截止。

两个bootstrap原源先冻结再真实pull，2700秒至少再次pull并仅读根和本题README差异；变规立即处理。NFF立即正常pull/rebase再推，无force。每个完整分支原JSON与完整索引在同原runner自然返回后发布，小件保全身份；可重算完整系数依根§15留runner。索引的final指标及last_tracked路径明确只指最细最后.90相，全部其他相位读原分支文件。

当前实际run/job/四支自然返回、全点、误差、reach与最终证书尚未返回。达到README全部标准前继续下一未付问题；初始厚度已证明或局部精确等距均不是收尾。
