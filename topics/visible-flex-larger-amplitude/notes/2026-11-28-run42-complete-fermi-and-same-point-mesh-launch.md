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
