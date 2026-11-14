# 秩一与非支集投影路线：本轮入口

日期：2026-11-12。会话：Astra-ISP-e2cb8f94。

完整证明已经分别登记：

- [R15](../results/R15-rank-one-spectral-collapse-and-zero-type.md)：无零圆盘的定量全部矩界、临界阶零型、秩一谱收缩与矩消失等价、非零强弱/无范数损失极限判据及弱弱相消反例。
- [R17](../results/R17-finite-dimensional-anchor-surgery.md)：有限维锚点删改的 Schur 补与缺陷精确极限。

## 6. 本轮外部声称的即时核查

Mubariz T. Garayev, *On the solution of Kim, Pearcy and Shields problem and its consequences*, [arXiv:2607.16373](https://arxiv.org/abs/2607.16373)。原 v1 为 2026-07-17；当前页面明确标记 2026-08-19 的 v2 已撤回。作者 comments 指出主结果 Theorem 3.1 不正确。因此不能引用其摘要中的完整 ISP 声称。这个状态是直接核查 arXiv 当前版本页面所得，不是以第三方评价代替证明审查。

与本笔记秩一预解式框架相关的已发表来源：Adi Tcaciuc, *On quasinilpotent operators and the invariant subspace problem*, J. Math. Anal. Appl. 477 (2019), 187–195；[作者 arXiv v2 全文](https://arxiv.org/html/1805.03277v2)，Lemma 2.1、Theorem 2.3。它的双参数等价化并不构造一般算子所需的秩一扰动。本笔记命题 1–7 的证明已全部写出，不以该文的等价化替代新的存在性结论。

## 7. 留下的具体缺口

1. 对 R9 的 $A$，命题 3 将有界秩一扰动的谱收缩化为全部固定矩的消失；仍缺一个具有命题 5 的非零强弱极限，或命题 6 的无范数损失极限的构造。
2. 命题 4 说明“两个非零弱极限”仍不够；它甚至不能保留最初的零阶矩。任何只用弱紧致性的秩一截断路线必须补足这一点。
3. 命题 7 完全计算了固定有限维锚点手术的代价。要继续近不变投影路线，必须处理随尺度变化的锚点或真正不同的闭子空间选择；不能在标量极限上删去一个固定向量后直接套 R7。
4. 一般有界算子尚未归约到 (3.1) 的拟幂零类；即使解决本笔记的一个模型缺口，也不能按 README 将整题标为完成。
