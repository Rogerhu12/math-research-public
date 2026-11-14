# R133 补充：全实参数正根七列高频图的实际验收

公开 Actions [43617150971](https://github.com/Rogerhu12/math-research-public/actions/runs/43617150971) 已实际通过全部10项检查。新接口算术用时0.001856572秒，实际 child 返回0，worker记录5.000551673秒。它只读取三份已完成的小记录，原根邻域、4650行正区、3594接口、7721行响应包络及外部非线性图均未重算。

## 1. 同一对象、参数区间与参考

固定物理参数为原 $\eta_0,\nu$。中心与显式连续方向分别为

- repair定义 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`；
- $Z$定义 `6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。

结论对整个实 $Q_\delta=Q_0+\delta Z$、$|\delta|\le10^{-8}$ 一致成立，包含已经固定的实 $\delta_*$。两个正片使用完全同一个 $a_\delta=-\gamma m_\delta$、$g_M(r_*)=M^{-1/3}$ 与真实 $p_M(R)=q_*/(-m_\delta(R))$。真实外端已在原证书中落于 $(1/8,1/5)$；此处没有把不同参考架在切口认成同一架。

无穷高频为全部 $|j|\ge97$，物理频率 $|4j|\ge388$。输入定理付过大M32背景和小M96变化的完整band192与shell288；未知修正仍有全部 Fourier 频率。

## 2. 实际接口常数

采用[完整 P1–15 合同](R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md)。下列数均为严格向外放宽的上界：

| 系数 | 实际上界 |
| --- | ---: |
| body完整反馈 $\chi$ | .303291625133 |
| body补支反射 $\chi/(1-\chi)$ | .435320768450 |
| 两端口回路 $\lambda$ | .000581202629 |
| 接口resolvent $(1-\lambda)^{-1}$ | 1.000581540622 |
| 根补支反射 $r_*^{\rm op}$ | .438072896309 |

原 collar常数准确为 $q_c=750/749,\ r_c=1/749,\ B_c=9/1000$。本次实际门给出
$$
 \lambda<1/1500,\qquad r_*^{\rm op}<1/2.
$$
body补支使用准确稳定参考在初端的补支分量为零，因此反射费是 $\chi/(1-\chi)$。没有拿完整Poisson费代替这一步，也没有由体 $L^2$ 范数直接推断端点迹。

## 3. 全七个输入与主要输出

输入次序固定为
$$
 (\|s\|,F_c,F_b,B,J_c,J_s,J_u).
$$
其中普通源是 $L^2_rH_\phi^{1/3}$；$B$保真实外端head、独立even mean、所有body源端口及原加权affine jumps；$J_c$保collar内部跳，$J_s,J_u$保cut两行的真实有符号跳。整个有限head作为独立源输入给出，并未令其为零。

表内系数逐项乘对应输入范数后求和。每项都是向外放宽值：

| 输入 | 根补支迹 $U$ | 整段正区 $Z$ 上确界 | 整段正区原态 $L^2$ |
| --- | ---: | ---: | ---: |
| 根稳定输入 $\|s\|$ | .438072896309 | 1.438072896309 | 3.619588056911 |
| collar普通源 $F_c$ | .012942656067 | .012942656067 | .032576292513 |
| body普通源 $F_b$ | .181398217425 | .181398217425 | .456574088157 |
| 全外端/head/mean/原jump源 $B$ | 1.438072896309 | 1.438072896309 | 3.619588056911 |
| collar加权跳 $J_c$ | 1.438072896309 | 1.438072896309 | 3.619588056911 |
| cut稳定跳 $J_s$ | .436155465781 | 1.436155468575 | 3.614740961962 |
| cut补支跳 $J_u$ | 1.001917430529 | 1.001917433323 | .010227513530 |

原小摘要另外保存body初端稳定迹、collar初端补支迹、两片分别的 $Z$ 上确界：共7输出行×7输入列。整段sup使用有向球并集的向外端点，因此表中最后两行遵守实际并集费用，不拿某一片更小的系数覆盖它。

原态 $L^2$ 使用真实collar长度至多 $9\cdot10^{-6}$ 以及body独立重构因子，准确合成
$$
 \left(9h\,S_c^2+C_b^2S_b^2\right)^{1/2}
$$
后才逐源求和。原两根迹到Airy行的完整因子9另按原合同使用。

## 4. 三个原输入与新原件身份

| 文件或生产者 | SHA256 |
| --- | --- |
| 原fullδ collar process | f919ecd9da5d447cf8950d1b267c28c7c33c2c396b21318b64a45317646745ae |
| 原fullδ body process | 1a0be497981ed6e5f47546892c390fec5820b02671ff9eb83a37af47b26ca395 |
| 原fullδ body summary | 2da26c59fcbf212fc669cd29efdc9eb27489ae5a11f8dc51bea801b733ba9ef9 |
| 新数学source | 65222466f862c85538d78bd822f0b9793ede2dfc1b6058c69d8c97074c93f7c1 |
| 新worker | e64feeda2e0a7df6fc03da6d309fd0c5db8ad20b9d5468259003445e16e1821e |
| 17输入manifest | b5931183c48fb92fbf4dcfb696bf582be52741323b5f051bbdff57922a7302d8 |
| 新完整native | 4e128cf91ce4e136d8574575704f1ebabf925953039eeb9219b00113436be2e9 |
| 新小summary | 410e8f07545c862425673a2c0cc37eebfc6f950217167f2b72c44d5a7b5676e7 |
| 本次仓库process | d35bb44e4cd7d933778d3234b6b0fe6c271fa9a8e744466a3fa9fd40f0e1f454 |

实际目录是
`notes/full_delta_positive_root_graph_ci/run-43617150971-1-full-real-delta-positive-root-graph/`。
完整native为3722字节，小summary为27047字节；artifact为
`visible-exact-full-delta-positive-root-high-graph-43617150971-1`。
仓库process只按本次实际字节核验，不假定它等于final artifact中的出版快照。

worker于16:44:18 UTC执行的最后真实pull读取提交
`ada07519b8addf6a07ac45ab12fd2f15b86f7657`，根和本课题两份README差异均为空。新运行前后均执行了真实pull。

## 5. 已闭范围与后续消费

本次已闭合完整实参数族的“给定整个head”正区高频逆与正根图，可供实际 $\delta_*$ 的根parametrix和有限部证明消费。所有七列仍是完整源合同。

有限head与未知high的耦合Schur、负侧返回、实际完整PDE响应误差、真实参数Schur、非线性存在及无限维邻域转授继续由各自证明完成。order1仍保其独立右high端口；本次没有授予物理H7/6外图。真实原件中的这些scope字段均为false。
