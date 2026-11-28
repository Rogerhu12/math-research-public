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
