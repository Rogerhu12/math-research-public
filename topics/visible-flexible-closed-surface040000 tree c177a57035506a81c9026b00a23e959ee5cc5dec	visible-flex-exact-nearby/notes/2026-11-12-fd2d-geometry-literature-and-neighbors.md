# 2026-11-12：固定帽建设的原始文献与相邻课题核对

会话 Astra-visible-flex-fd2d / constructive_geometry。此为范围核对，不把检索未发现解释成不存在定理。

## 原始文献

1. Victor Alexandrov, *On the total mean curvature of non-rigid surfaces*, 2008 预印本，Siberian Mathematical Journal 50 (2009), 757–759；[arXiv:0812.0053](https://arxiv.org/abs/0812.0053)。作者摘要证明闭光滑曲面的总平均曲率在无穷小弯曲下驻定。本文不是连续有限幅闭嵌入族的构造；不能用它支付本课题的全时几何或有限幅误差。
2. Simon D. Guest, Elizbar Kebadze, Sergio Pellegrino, *A Zero-Stiffness Elastic Shell Structure*, Journal of Mechanics of Materials and Structures 6 (2011), 203–212，[作者库](https://authors.library.caltech.edu/records/5x3vw-rdj36)，DOI 10.2140/jomms.2011.6.203。摘要明确区分 inextensional 理想模型与薄弹性实物；原壳沿纵向为直线、横向恒曲率，利用残余应力获得扭转路径上的中性稳定。它没有给闭无边界 C² 等距族。
3. W. Hamouche, C. Maurini, S. Vidoli, A. Vincenti, *Multi-parameter actuation of a neutrally stable shell: a flexible gear-less motor*, Proceedings of the Royal Society A 473 (2017), 20170364，DOI 10.1098/rspa.2017.0364，[开放原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5582190/)，[PubMed 28878569](https://pubmed.ncbi.nlm.nih.gov/28878569/)。已读出版摘要及原文 §1–2 的检索内容：平铜圆盘经塑性弯曲成为圆柱壳，控制曲率轴方位；实物处于近似不可伸展的弹性模型。再次直接 open 时 PMC 返回验证页，故本轮不声称已完整读过全文。这里的相位旋转思想相关，但圆盘有边、预应力/能量陈述不等于本题的闭合与共同精确度量。
4. Sjaak Kok, Ali Amoozandeh Nobaveh, Giuseppe Radaelli, *Neutrally stable double-curved shells by inflection point propagation*, Journal of the Mechanics and Physics of Solids 170 (2023), 105133，[DOI](https://doi.org/10.1016/j.jmps.2022.105133)，[作者存档](https://pure.tudelft.nl/ws/portalfiles/portal/141023244/1_s2.0_S0022509622003052_main.pdf)。出版摘要及 §2.1 描述环面负曲率片加锥形翼片，通过厚度优化得到近常能量、近零载荷区间；不提供闭曲面上误差随固定几何加密趋零的证据。未下载或提交 PDF，未逐页渲染。

这些来源不能直接替换当前闭图求解，也没有理由把中性稳定、有限阶等距和精确有限弯曲混成同一完成证据。本轮继续本仓库的真实几何构造。

## 相邻课题

主代理从 `origin/main` 提交 `40ae00d37077e199c86aa9afe996b327940e4368` 按单文件提取的四个 HANDOFF 已逐个只读核对。只作当前工作选择，不修改相邻目录。

| 课题 | 当前可转用信息 | 不可转授的缺口 |
|---|---|---|
| visible-flex-larger-amplitude | q085 强前缀恢复；低 H4 真非线性尾容量；q040 的同固定 g 频率加密 | 其强活动前缀与实际尾未成一张满足本题所有门的闭图；source 的有限 R6 taper 不自动是精确无限非轴对称闭合 |
| visible-flex-exact-nearby | k4 背景及真实径向全频 Green/尾控制；严格背景几何 | 有限幅候选未收敛；实际非径向全频逆与非线性收敛仍缺；背景几何不可转到有限幅图 |
| explicit-flexible-closed-surface | R149 为完整固定材料、共同精确 g 的 90 来源片嵌入族 | 亏格 1、两个真实边界圈；不提供本题可直接采用的闭面 |
| smooth-unrippled-twist-flex | phase-state01 的高精度前缀与正在推进的新 H 真尾；严格曲线/全时装配接口 | 全新前缀/尾/补丁连续覆盖及完整闭图仍未结清，旧图界不能转授新图 |

本轮大固定帽设计不重复这些课题的 BVP：它补 R107 中原先只有分离圆顶/横杆的固定帽连接，并给与平圆盘活动核拼接时的全局 reach 保持条件。仍须求出同一短 n2 活动核后才能组合为本题的完整候选。
