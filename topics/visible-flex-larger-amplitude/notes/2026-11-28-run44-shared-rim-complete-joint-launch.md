# Run44 — 全时间联合的真实两卷、双帽和公共圈六jet求解

会话 Astra-larger-e4e2a2bf-20261126。**同一个R757完整初始g，新的实际物理搜索；源、参数和原预算已完整交付，实际点与证书等待公开原程序返回。课题未完成。**

[R763](../results/R763-terminal-metric-traces-and-free-shared-rim-jets.md)已经证明43三个成对启动在全部原自由度下仍有末圈角误差>.72；这里实际释放那一圈。[R761](../results/R761-paired-track-global-tube-and-positive-volume-gap.md)只为规定的未修正全闭场证明厚度和体积差，不能拿它替本次自由修正后的几何费用。

## 五个完整新启动与两个完整后继

三个released入口分别为原整帽平移并轴向缩短.23（角.78）、缩短.37（角.795），以及缩短.32/开发角.22（中央角.78）的真单位速帽平面开发与原非平高度法向延伸。另两个tube入口为R761全相厚场的角.78和.795。五个入口都有真正全部九图；目标取唯一R757初始全tensor，从未按当前相位重拟合目标。

保五个粗级实际过程，再对released和tube两个家族**各自**最优点完成4/8/16全部时间区间及原空间/频率精化，总计11阶段。两家族最终分别在同一runner原点上完成65检查相位与七个指定整闭网，检查取其并集；各自原终端索引和PLY身份独立。tube副本输出在tube-reference，不覆盖released点，不读取43未来raw。

R759/R761/R763本来就在物理世界坐标中：右握整个头逐点不动，左头作规定平移。所有科学评估和PLY均直接用这一场，**不再施原移相族的后旋转**。中央和固定握不受任何本次端/帽校正，所有强held见证仍须按校正后的完整像和初像真实比较。

## 真正共有的两圈自由与全部帽域

两端各有独立的两整卷内部三向函数、完整填充帽三向多项式，以及整公共圈的三向A(s)、B(s)、C(s)。用同一个r=v−L（卷）/r=w（帽）表示，在该圈依次匹配位置、横一阶、横二阶和所有切向混合导数。两个空间端互不混用系数。它们在中央缝二阶为零，帽圈外的完整内部继续有物理自由。

圈角基含Fourier与真实初剖面切向分量，逐层rim modes4/6/8/11；卷径向/角频率与帽次数3/4/6/8同时上升。Cartesian内部探针的共有圈模式通过真实旧材料图的二维逆给出。已按原R747 cap_leaf核对：JOIN=.00025、RAMP=.0005、LAST=.0005；w≥.00075时d=d_b+.0005、rho=(1−w)/.9995，与代码完全一致。它不是另一个独立Cartesian标签。真正cap-normal和cap图的六jet重叠逐阶段独立实测。

## 原联合科学算法与完整费用

每阶段所有正训练相位一起求解向量自然三次时间样条的节点系数，初节点系数恒为零。用真实线性物理六jet映射及其adjoint，JAX CPU float64对实际三行Gram、主曲率、面积和三维有序法球费用全反传，再按同一自然样条矩阵回传所有时间节点。时间自由没有被逐相局部结果代替。

每级保两完整L-BFGS-B块，每块最大迭代30/35/42/50，maxls22、maxcor13、ftol2e−12、gtol2e−8。两块之间对当前真实物理点重扫三维有序对；pair预算1536/2048/3072/4096。各训练图全行均参与，末圈附近行额外权重；独立全域读数使用真实初g的相对算子误差。有限有序对损失不冒连续reach下界。

各层训练mesh为(25,9,8,7)、(35,13,10,10)、(49,17,13,12)、(65,21,16,15)，独查为(51,15,12,12)、(67,21,16,15)、(91,29,20,18)、(121,39,26,22)。所有正训练相位由2n+1节点统一构成，独查保原中点与两Gauss位置；全部记录实际Gram、曲率、面积、support、有序法球、四缝六jet和两帽重叠。每次真实梯度方向差分、非线性退出状态及预算自然返回均原样存，不用其设置额外准入门。

评分和优化只选出有限候选。所有全t嵌入、reach、未标号刚体商差、连续metric界与精化收敛仍需对那个完整同点补证；非零初构造或者末圈可行不能替全卷存在。

## 完整整文件身份和执行

[完整请求](../computations/run44-shared-rim-phase-request.json)与[完整交付](../computations/run44-complete-shared-rim-source-and-launch-delivery.json)列22个冻结科学输入（18个真实import、两导出和入口/参数），以及三个既有控制父件。新七件如下；所有物理父已在main实读留存，R763完整源为3985B/`dee28269b2031d5c5eb70caaf999f181adc5dbb6`。

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261128/bent_shared_rim_phase.py | 15951 | `85eba7c076be5583e3da380bb418e909cd41aba5fac1564ec69036d942ab2a21` | `68e75f0335be5b5d0382cd58fb1a2e29d55c40b7` |
| scripts/resume_20261128/bent_shared_rim_fields.py | 5952 | `1640e90ef01bb03cd99ae1fb866d66348ed8af33543685573f26c5a4572f1bf9` | `850c8a1f1f9df163d2d462ec8ba6e505151ee674` |
| computations/bent-shared-rim-phase-design-v1.json | 5795 | `2bc4c956d286d273928e298c58bd0799974d751ae93d022a5d730170dfa8c6e2` | `c20ee9f91ea0f1eb664a1be4ab53aa71037c819c` |
| scripts/resume_20261128/observe_bent_shared_rim_search.py | 17265 | `cdcb914a0caac5d16e7bb05a659bfaecd17362a745928285e7a4ab5d717b1879` | `0bb96a0c3338895e85e3b863c58cc68ebaa5294b` |
| .github/workflows/visible-larger-run44-shared-rim-phase.yml | 4785 | `4ea24eb9ebbd702afecb1eff6cad3f4e5f5ee50ff012193c42c02067df80fe95` | `81a2d4b92582259e0ef45f9e3c6ebc69829b7d5f` |
| computations/run44-shared-rim-phase-request.json | 23398 | `15724a14fa96ade39bbb9f50e554cc8ce1cbe3c5b347050d05bacfcaee98a39e` | `e40f8a76a2f05d81e7cfd3c50f03e25cf2489f12` |
| computations/run44-complete-shared-rim-source-and-launch-delivery.json | 23181 | `41daf6f1af1cb12c2cdb2f4b194f61f0a2e5f8b41d220480e52e912aa816b1c5` | `6d7a6868566ad7b3a0de9f1c6abd5b0b3caa8adf` |

普通公开push触发；固定Python3.12.14/NumPy2.3.5/SciPy1.17.0/JAX与JAXlib0.7.1，每库单线程、CPU64位。科学目录冻结trigger提交，发布main独立普通pull/rebase；2700秒真实pull并仅读根及课题README差异，记录读过SHA，变规立即遵守。NFF立即拉取整合再推，禁止force。原平台360分钟，没有新子进程截止或提前科学门。

每阶段原JSON、独立原summary和两组最终原geometry索引全量小件发布。完整系数与NPZ、七个二进制PLY.GZ及更细相位明细在同一原公开runner生成，依根§15保完整字节/SHA和确定源参，不把可重算raw再塞进Git或Release。actual目前均null，不冒任务完成。
