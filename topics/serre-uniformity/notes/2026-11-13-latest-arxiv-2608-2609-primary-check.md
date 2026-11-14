# 两条近期 arXiv 线索的主来源核对

日期：2026-11-13。性质：**文献范围核对，不是新增数学定理或论文正确性认证。**

本轮已直接读取 arXiv 官方摘要页、官方 API 和两个指定版本的完整 PDF；
下载文件只供核读，不作为仓库数学结果上传。
网页检索工具的 PDF/HTML DisabledError 未表示原论文不存在，
同一官方地址通过终端请求能够正常取得。

## 1. arXiv:2608.19354 不是一篇声称证明 Serre 一致性的论文

- 正确标题：Abbey Bourdon，*On the Finiteness of Isolated $j$-invariants for $X_1(N)$*。
- 官方版本：2608.19354v1，2026-08-19 18:18:26 UTC。
- 官方摘要页：[arXiv](https://arxiv.org/abs/2608.19354)；
  [指定版本 PDF](https://arxiv.org/pdf/2608.19354v1)。
- 作者本人研究页的第 15 项也把此文列作预印本：
  [Abbey Bourdon: Research](https://users.wfu.edu/bourdoam/research.html)。
- 已核正文第 4–5 页、Theorem 5 后的段落：作者明确把一般 Serre
  一致性列为尚未解决的问题，Theorem 5 汇总已有像分类的进展。
  文章研究孤立 $j$ 不变量的有限性及有理 $j$ 情形的挠点界，
  没有声称解决本仓库的主要目标。

二手站中名为 “Serre’s Uniformity Conjecture over the rational numbers”
的内容是一个开放问题页面，引用上述论文作为来源；
不能把该页面标题当成 arXiv:2608.19354 的论文标题。

本地核读副本：bourdon-2026-isolated-j.pdf；提取文本
bourdon-2026-isolated-j.txt。

## 2. arXiv:2609.35460 是带明确秩前提的固定 $7$-进工作

- 正确标题：Tho Nguyen Xuan，*Complete classification of $7$-adic Galois images for non-CM elliptic curves over $\mathbb Q$*。
- 官方初稿时间：2026-09-28 15:48:56 UTC；
  本轮核读 2609.35460v2，更新于 2026-09-29 11:48:47 UTC。
- 官方摘要页：[arXiv](https://arxiv.org/abs/2609.35460)；
  [指定版本 PDF](https://arxiv.org/pdf/2609.35460v2)。
- 正文第 2 页 Main Theorem（Theorem 10.1）明确假设所讨论亏格三曲线
  的 Jacobian 满足 $\operatorname{rank}J(\mathbb Q)\le3$，
  并把该上界引自 Furio–Lombardo 的 fake $2$-Selmer 计算。
  文中另证明反向下界三。
- 第 3 页 “What is assumed and what is computed” 说明：
  若所引用的类群、单位计算没有作无条件认证，其主定理会继承相应的
  Generalised Riemann Hypothesis 依赖。这是作者自己列出的条件，
  本记录没有替其判定该计算是否已经认证。
- 第 4 页 §2.1 明确保留一般非分裂 Cartan 情形为开放问题。

因此这条线索既不是一般 Serre 一致性证明，也不能把标题中的
“complete classification” 脱离正文的秩前提。
本轮只核对主来源身份和定理范围，没有核验全部计算，
也没有声称发现其证明中的其他缺口。

本地核读副本：xuan-2026-7adic.pdf；提取文本 xuan-2026-7adic.txt。

## 3. 对当前研究的影响

两篇文献都不使本课题达到完成标准。
当前一般完整非分裂正规化子问题保持 OPEN。
本记录不把尚未完整核证的最新预印本结论作为本仓库证明链输入。

官方 API 核读地址：
[arXiv API](https://export.arxiv.org/api/query?id_list=2608.19354,2609.35460)；
提取元数据保存在 latest-2026-arxiv-metadata.json，供版本复核。
