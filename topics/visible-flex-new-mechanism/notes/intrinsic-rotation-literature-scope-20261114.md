# 内蕴旋转对称文献的适用范围

日期：2026-11-14。针对当前固定旋转不变 g 的非轴对称连接，核对两个可能被误作全局捷径的原始来源。没有新几何计算，也不重复已审过的整体文献。

## 1. Engman 的明确等变范围

Martin Engman，The Spectrum and Isometric Embeddings of Surfaces of Revolution，Canadian Mathematical Bulletin 49(2)，226–236，2006，DOI [10.4153/CMB-2006-023-7](https://doi.org/10.4153/CMB-2006-023-7)。本次直接读出版社正文的摘要、§2、式(2.1)–(2.2)与 Proposition 2.1；可由[出版社页面](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/spectrum-and-isometric-embeddings-of-surfaces-of-revolution/E3025F2D58B7B1D95A3C6E003D128B0E)进入 PDF。

该文明确研究 S¹ 等变的嵌入，即实际像是由一条曲线旋转生成的经典旋转曲面。对 g=ds²+a(s)²dθ²，其条件 |a′|≤1 在这个明确范围内使用；文中的谱障碍同样带等变限定。旧[2002 arXiv v1](https://arxiv.org/abs/math/0201172)的简短表述未逐处保留此限制，本题不据旧摘要扩大结论。

**对当前任务的判断是本次推断。** 直接代入经典旋转参数式 X=(a cosθ,a sinθ,z) 会得到 a′²+z′²=1，因此 |a′|≤1 是这一特定参数式的必要门。当前连接使用完整的空间切向 T 和共同高度原函数，没有要求像集轴对称；不能把这个参数式的限制擅自加成全部连接的不存在判据。文献也没有替当前连接给出存在或收敛证书。

## 2. Freese–Weber 的额外第二形式假设

Daniel Freese、Matthias Weber，On surfaces that are intrinsically surfaces of revolution，Journal of Geometry 108，743–762，2017，DOI [10.1007/s00022-017-0370-6](https://doi.org/10.1007/s00022-017-0370-6)。本次直接核[出版社摘要](https://link.springer.com/article/10.1007/s00022-017-0370-6)与[作者 arXiv 记录](https://arxiv.org/abs/1607.08503)；没有声称已逐页读完付费正文。

该研究除第一基本形式旋转不变外，还要求两个主曲率旋转不变，主方向仅随角变量变化。其常平均曲率结论属于这些合并假设下的类别，不是只从 g 旋转不变就推出的结论。

**对当前核心的判断是本次推断。** 准确非圆椭圆柱的非零主曲率为

$$
\kappa(\varphi)=
\frac{AB}{(A^2\sin^2\varphi+B^2\cos^2\varphi)^{3/2}}.
$$

A≠B 时它随角变化；改用材料弧长角不会使其成为常数。所以当前核心不满足上述主曲率假设，不能用该文的分类直接排除或完成本题的非轴对称连接。

这次核对没有产生新完成候选，也没有更改当前固定 g、物理参数、Actions 预算或完成标准。实际主线继续解完整连接、曲率和非局部 reach。
