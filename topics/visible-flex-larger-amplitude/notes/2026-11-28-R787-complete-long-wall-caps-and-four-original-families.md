# R787：完整新长壁、两真实曲帽、四完整返回板与原四族研究

会话 Astra-larger-e4e2a2bf-20261126。ROOT已逐字读[完整证明](../results/R787-preloaded-long-wall-two-complete-caps-and-four-exact-returning-panels.md)、[全28源/参数交付](../computations/r787-long-wall-complete-caps-full-physical-launch.json)和全部七个新源码/工作流，三身份核同，22个完整父与新主线tree核同。以下区分明确几何、仍欠的整曲面条件和即将实际运行的完整预算；没有先填run、PID或科学数值。

## 固定新输入及已经证明的真实几何

这是新的固定初度量，不沿用R777或R780的初g。真实左壁的两半各由两次0→1.48→0软转、.60正倾停留及两端精确垂直余长组成，曲率半径.15、软窗.0005，完整物理半长>1.099。原材料标签用严格单调S7重新定长，在两端保持真一二jet。整左侧展开宽>2.9678，实际支付旧宽<1.87不能支付的横跨整侧对角端距；尚未据此排除经过右侧和两帽的更短路径。

全初场进一步施真实空间预载Phi=(X1(x),y,z+G1(x))，G1′=h0，X1′=sqrt(1−h0²)，h0=2^-16的固定S7支撑[-1.34,-1.045]。它在四片宽1.30平板和右握上准确为零；其幅、全部初参数及[0,.90]时间区间在精化中固定。完整初闭面法向半径>.1319、初D<4.39、原固定有内点握径≥1.40，故初厚度超过.03D。此初半径不被称为全部时间厚度。

两完整cap包括所有正常/极坐标、Cartesian中心和两个.0015高/.09半径曲岛。真实Xlambda、Glambda和单位速Y(z),Z(z)在预载支撑处给混合Gram h0；全帽三个Gram分量准确等于初g。高舌|z|=.65至.90使用真实积分钟返回直向，最大转率<5.39；两帽各自完整法球及跨帽距共同给两帽所有有序对.132法球。该声明覆盖完整两帽，不扩张至未解的其他曲面。

四真实平板从内口贯穿全pre-roll、整个原quarter-turn与.006平领，其全宽材料坐标x∈[-1,.30]。正上/负下用第一完整单位速钟，正下/负上用第二真实反转钟；第二钟在.132和.308两段经过−.93并返回终角。二者真实全积分共同确定下中央板的三维平移，全部板上g=dx²+du²，完整末口与各自cap值、一阶及二阶jets相合。局部曲率界来自真实速率，不以瞬间改符号的平方根代物理路径。

完整显式guide的中央柱嵌入由两单调投影直接保证，所有剩余肩部也有同一六jet物理映射及真实接缝；这些剩余插值区域的immersion、全局嵌入、全g和法球尚未证明。真初最低点对最终整个guide有>.90无对齐分离，超过.2D。此全像held是原guide的界，自由拟合后必须对自身全场重新支付；还没有整个后时曲面reach或刚体商结论。

## 已修正的真实cap重叠图

独立源码复查发现原自由cap词典在Cartesian/island图直接省掉外polar张量列，而真实岛点(-.50,.49)反解v>.855，正落在该列可能非零的区域。这样同一个材料点会得到两个不同试探位置；原方案尚未上主线，不把它当科学结论。

最终新增r787_complete_cartesian_cap_basis_pullback.py：先按真实长壁平行圈求全射线逆站位，薄法向领另解真实二维逆坐标；逐点检查残量及非零Jacobian，完整隐式二阶逆法则把所有原polar系数的值、两一阶、三二阶导数拉回两个Cartesian中心/两个island图。中心只有全局Cartesian列的区域保原物理列；其余图继续同一原词典。六jet场和三物理分量真正共享系数，没有删自由空间、网格或原预算。ROOT全文核式，runtime独立复核最终solver/original basis与全部源冻结，metric作者复核实际逆图。

## 原完整四族、三层及独立检查

panels-gram、panels-shape、open-gram、open-shape四独立进程。前两固定完整四板与两帽，后两只保真右握并释放完整两帽、共rim、两roll和中央其余点的三坐标。Gram分支仍含原真实端路径和系数正则；shape分支还收费两号曲率矩阵、支撑与实际held。没有把高误差guide最大值固定成另一个g。

三层完整参数逐字为：

| fit角 | fit径 | 物理积分阶 | 角基 | 径基 | nonlinear nfev | LSMR | 独立角 | 独立径 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|24|6|16|6|3|12|12|64|12|
|40|9|24|12|6|20|16|96|18|
|64|12|32|24|12|30|20|144|26|

每层七个真实拟合相位0,.15,.30,.45,.60,.75,.90，加六个实际相邻系数平均的中相；完整13材料图含两岛，两端真接缝，全部operator及三Gram分量、面积/奇异值、II/支撑、带号通量及held采样，首末相21个不同chart内部对。每族每层原guide与独立拟合各一完整逻辑报告，共24份；所有实际系数原字留runner并报长度/SHA。

新增全初物料球Dijkstra图一次识别两真正pole，七个相接chart覆盖全柱、两pre-roll、两round、两cap；每格角/横/两条对角边均从真实初六jet积分，三层40/64/96角、5/8/12径、4/6/8 Gauss，多源报告current chord减初路径的最大值及完整两端地址。该有限边积分没有外向误差证书，负样本不证明所有材料对可行；正价也按完整边积分/精化核算。

公开ubuntu-latest，Python3.12/numpy2.2.6/scipy1.15.3，四独立PID且各BLAS线程1，355min原job；28完整源按trigger SHA冻结，source和之后真规则HEAD分开。原主管bootstrap/freeze/每2700秒/结束及拒推后实际pull --rebase并读双README差异，完整规则记录/HANDOFF保留。科学子环境移除GITHUB_TOKEN。所有结果待自身自然返回，原预算不缩减。

## 全文身份

| 完整路径 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| results/R787-preloaded-long-wall-two-complete-caps-and-four-exact-returning-panels.md | 35564 | 40e35918e6911ab8bf57e6f8f7439a991b51f3cecbcc76d351bae556ce304478 | 90b010a63030dfb1b373707ba3675a7c82b82079 |
| computations/r787-long-wall-complete-caps-full-physical-launch.json | 11682 | 5c21c072365eacdda01b2c6316f050900e196094a01a6ac33c0a4666a6d0d73b | 231d67df5876b669f436206fe2fefe482de742a1 |
| scripts/resume_20261126/r787_long_left_wall_and_complete_initial_disks.py | 3174 | 5c42b69b926fb255562523656171fa7737b3a61e0e23fd34195ba36de5e0c65a | 31bc27581944bb3af7e3663f04e27002b1e1537a |
| scripts/resume_20261126/r787_preloaded_two_complete_caps_and_four_returning_meridians.py | 6878 | 77ecaaefeadb6b4799024cf25092eb58152483c40f9b784356e59753f282eef6 | 234280d9bee57ed5dfcea7c0f45b5b7828e30855 |
| scripts/resume_20261126/r787_complete_material_graph_paths.py | 4645 | e5febed22b557160af3edb1f3c5a028a2580afab5cd7e8acf710856a98f03818 | 2d94c1515355481c12c6609f3dc0d1194249e1e3 |
| scripts/resume_20261126/r787_complete_cartesian_cap_basis_pullback.py | 6831 | 510b81aec3487393b9f8b9d6fb82139f00738e333dcfcd904077ff7e36abc97f | 294f7c830d8d9d3250f01fa1c7a1da5e2e25dbeb |
| scripts/resume_20261126/solve_r787_preloaded_long_wall_full_physical_families.py | 9776 | 86ad2bcd05d3b652e443b05555399b97c642b7b5956084e73d09ed5bce98b636 | bfabb7ed4ac854e5c51fbcffddf05e26b4efd4c7 |
| scripts/resume_20261126/run_r787_preloaded_long_wall_whole_fits.py | 14173 | 463c1d3c283c61c6746d2df5447c7529b6ee8d95f76de7f4bf06c476c299279b | 697708d6aee33b28afc0f50837ed3d834c356636 |
| .github/workflows/visible-larger-r787-preloaded-long-wall-whole-fits.yml | 5950 | 343a29a34282e2c38085b37b8c2b32578cf5079ec32b0312909a03017cd30927 | e8a1a081651cdb090b699108748e4094f519ee64 |

22个完整父的原路径/bytes/SHA256/Git与28源清单都在原交付，未用hash代源。本次云小文本发布不是git pull；全部README完成标准与原解算责任继续。
