# Run54：预弯长腰真实纵向余量、可动腰口与三族全场

Astra-larger-e4e2a2bf-20261126（AI）。[R791完整定量证明](../results/R791-prebent-lever-sphere-one-strain-row-and-global-normal-tube.md)及3940B全九图源已主线2b14d60b41bc26f1b922b04837b7eed2061b48e8。本次以那一个真实初弯.10的g0求完整曲面，不复用R781的目标或直径。ROOT全文读五个新科学件、原全部参数、观察主管和workflow；runtime独立复核所有九图重叠、真实两jet、全部J运算和最坏Gram/矩应力维度。实际run/PID/数值尚未返回。

## 真实宏观参考与允许改变的腰口

同一个名义参考从初弯.10到.65，腰长1.4、半径.11、两头外半径.43、端卷.105，初整个D<3.22，固定右帽条带直径≥.648、全像held>.652、全t reach≥.104、含反射商距>0。全帽/端/flare/其余方向度量精确，唯一余项是完整腰纵向Gram，严格上界<.096。初始腰的正负Gauss曲率胞是真实原g的胞，并无开平带。

R791末节的真实材料路径证明：原外经线长1.411，名义两腰口弦>1.442；任何达到1e−6的修正至少移动其中一个真端点>.015。本次两腰口都有实际三世界坐标自由列，不能把其名义位置当硬边界；这只是允许必要修正，不证明它必然成功。

所有候选保右帽|xi|≤.035条带及左帽实际xi=−(.43−db)、zeta=0见证。初始全像X>−.596，那个实际末见证仍X<−1.248，故同一个无对齐整像held下界继续成立；它不支付新场嵌入、reach或无标记商距。右真条带的内点和两个Z极限保持，握径≥.648。

原初直径下界也可直接由两个真实盘心的Y距离支付：pb≥.105，所有初spine角在[0,.10]，故该距离至少.655+2.355 cos(.10)>2.998>2.99。由此两种半径的用途分开：所有曲率/有序法弦行使用更强的设计半径.03×3.22=.0966；远材料必要弦行仅使用.03×2.99=.0897，仍是题目实际.03D的必要条件。没有把D改成某个较有利的样本直径；每个全网仍回报它自己的样本D。

## 实际非圆列与全角纵向矩

三族各三个粗起点：完整两帽变分固定、自由腰口与帽沿、真实非圆空间环。基场包括第一谐波材料轴向滑移、有限12阶Bessel积分的周期空间环、右帽两个相反发展翼。每个返回的位置和两个材料导数都来自该实际有限位置式，不把截断环称为精确单位速。

新三坐标列包括全空间多项式、整腰谐波、七个真实腰站、两个自由接口和帽翼。帽极图、Cartesian与normal重叠全都用同一真实(s,xi,zeta)多项式；腰/站列在帽恒为零。中央、两端、两帽所有位置/一阶/二阶接合由真实门函数和同一拉回支付；独立读取仍实际检查几何。硬帽只固定该族的整个帽，其他族按实际握持/左见证材料门固定，未用坐标clipping。

在原全域度量、面积、曲率、有序法弦、全近材料弦及96最坏Gram点之外，新增每个真实腰站的纵向归一Gram误差完整角积分：常数以及1/2/3阶cos/sin共七矩。环标签的循环梯形权付整个角圈，实际非线性目标、真实Jacobian及Gram应力的二次变分全部包含这些矩；独立测量报告每矩最大的真实站和时相。没有用少数角度代替整圈自由场。

高斯—牛顿160 CG/容差.0002/阻尼.0015与原九回溯仍全保；两个各五步Krylov试探空间、负Ritz双符号×1/.5/.125均在同一原全目标实际择优。位移.03/切向.2信赖尺度不改。因物理修正对系数线性，Gram和七矩的应力项在所述模型中准确；辅助非光滑惩罚Hessian省略，非负Ritz不当正定证书。

## 全部18阶段及三个完整末场

九粗全部执行，各五迭代、24×14空间/两个时间区间/阶8，独立33×19/阶12/七基本相。三族各自选择后完整4/8/16区间：空间28×20、38×28、50×38，七/八/九迭代，独立37×25、49×35、65×47，17/33/65基本相、阶14/16/20。额外真实相.15、.35、π/4、π/3进入训练和独立目标。时间系数沿原自然左边界、右端零导数立方时钟，初值为零。

定义空间列一直使用固定初物料阶20；工作基场/目标按原层求积加密，最高物理场与最终验证阶20，参数保持。三末场各测原65均匀相加.15/.35/π/3及七个完整闭网的并集。全部九图、完整中央/两卷/两填充盘、接缝和真实材料见证都在场。实际去重相数、NPZ、21个全PLY及三个完整几何index由各自真实返回填写；raw仅留定义runner，有限样本不代全t证明。

16实际冻结科学输入=五新件+11整父，四共用主管保持；公开四核16GB/Python3.12.14/numpy2.3.5/scipy1.17.0、数值线程1、原job360min且不新增子进程截断。每2700秒及每次普通报告真实pull/rebase/读双README差异，quiet周期也即写HANDOFF。所有原读取身份与原预算见[完整请求](../computations/run54-prebent-waist-request.json)、[完整交付](../computations/run54-complete-prebent-waist-source-and-launch-delivery.json)。

## ROOT整件身份复核

九件新文件完整三身份如下。16科学输入与请求direct lineage/manifest全部逐项一致，11父和4共用源与主线身份核同；参数在两交付副本完全相同。原R791理论范围与拟合结果明确分开。

| 完整文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261128/bent_prebent_waist_phase.py | 15396 | 56f524b63f6799db75aae54c143c019c8d2c72acf82b78e9db9431fad049664b | 54147059a6b17567f3f7444e056c307e0dbc13f3 |
| scripts/resume_20261128/bent_prebent_waist_fields.py | 7879 | 6e825f59a1ec0ee9a4a181a0de584ff1c6d5bf7a3640444dfd6d65da5db93a1e | b40eb7f1675a4b7cdd813aacff404548bb2f2c68 |
| scripts/resume_20261128/bent_prebent_waist_normal.py | 10881 | a2f14d9b52cc42877cff8223350075dc457869472acd3f053861c54efa35a2f5 | 12fb2b3923b993adb5845fe555db389ead2e8bac |
| scripts/resume_20261128/bent_prebent_waist_stress.py | 6449 | 60e37feffd1af8d5ee25cdfc6a066411b9eaaf0e51e6bd767844c462ddc2e242 | 3c41072c8a47f5838bb72132d87b336c49292d60 |
| computations/bent-prebent-waist-phase-design-v1.json | 8716 | 2720cb9fc4dd5b318dc33e647c1aeb1d978ae2e1bb781e7ffaf3c021d8f925e9 | 6d87f6ab7a1103d4ee5ca89eb03d924b79b7e307 |
| scripts/resume_20261128/observe_bent_prebent_waist_search.py | 1485 | 3a8624deb5ed6cae5dc18ee1671a8cac3a225f627a85bd76525addd56c3d6d11 | 72f99d3bd3d49e901f890eeddb3a025e5ee5a6bc |
| .github/workflows/visible-larger-run54-prebent-waist.yml | 4233 | 8121839039c05c3e365e77d9c19a899ef68a0a2208c53352c0557a8184a6aab1 | 7debf26501f29b3130d058c5d6f7194c40d37a7d |
| computations/run54-prebent-waist-request.json | 26959 | a9dcf1952383786ad1c4aa7f1c642b28a7b95d86f68540b53ba61b777d0d1c8c | 9ea19201b3eb80bb84fca6f63cdaf7f6033da73d |
| computations/run54-complete-prebent-waist-source-and-launch-delivery.json | 34398 | 536a90a16289c1d1ce95d8a8f7478ec59b4287247b7a2a97a75f0a4c9d44232b | 88cc14ce869987e92af3890d7083eccc15fe4759 |

本次root云端发布非pull。尚无候选达到全题完成标准；科学工作按全部原预算继续。
