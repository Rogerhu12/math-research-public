# 接手、文献与执行环境核对

2026-11-10，Astra-visible-flex-78718bd0。状态：执行/来源核对，不是新增闭面存在结论。

## 文献（本轮实际打开原始来源）

1. Mohammad Ghomi, *Open Problems in Geometry of Curves and Surfaces*, 2019-09-02修订，§1.1 Problem 1.1，PDF第5页：
   https://ghomi.math.gatech.edu/Papers/op.pdf 。当时列C²闭曲面连续等距柔性为开放问题；
   本轮仅引用其历史陈述，不由2019文献推出2026完整现状。
2. I. Kh. Sabitov, *Bendable Surfaces without Visible Deformations of Their Shape*,
   Mathematical Notes 110 (2021), 126–134，DOI 10.1134/S0001434621070130；
   https://www.mathnet.ru/eng/mzm13037 。期刊原始摘要明确圆柱/锥面的滑移弯曲可非刚体，
   但像作为集合不变；因此这个结果本身不给本题Hausdorff像位移。
3. Michael T. Anderson, *Local rigidity of surfaces in space forms*, arXiv:0709.3202，
   https://arxiv.org/abs/0709.3202 。原始arXiv页面标明2009-09-06 v3撤回。
   作者旧网站PDF仍能搜到主定理摘要，但不能把撤回稿当成一般刚性定理。
4. Alec Payne, *Flexible Smooth Immersions of Cylinders in R³*, UCSD报告，2023-11-16，
   https://math.ucsd.edu/seminar/flexible-smooth-immersions-cylinders-r3 。院系原始摘要说明
   与Andrew Sageman-Furnas合作的非极小、非可展柔性柱面；闭曲面方向只描述为探索。
   不把有边/浸入结果当本题闭嵌入解。

这是有限范围核查；未宣称穷尽所有2026结果。仓库R520作为已审来源保留其准确范围；
本题独立量化比例和G5仍按自己的README执行。

## 新环境与实际前置检查

本次从main部分克隆（blob:none、depth1、稀疏检出），没有完整下载数据仓库。
旧执行器checkout在本环境起初不存在；不能据此推断旧session89004的退出原因。
新环境逐字恢复来源与新stem执行必须明确分开记录。

六份冻结SciPy源码哈希相同。root亲自执行两条原已审小检查并观察自然退出：

- pure checker：工具dff588，exit0，0.188秒；报告
  `2026-11-10-78718-numerical-csc-pure-check.json`，SHA256
  `7fc3661ae2e408f9bb52f05adf01c5021998853b90a1ec3f8df2cf2876d92b04`。
- 小矩阵字节/别名副作用：工具c817a1，exit0，0.407秒；15例；报告
  `2026-11-10-78718-numerical-csc-byte-check.json`，SHA256
  `8b518f10f94c5cd590e65cef1fa2e05c47fe2aa7dfd31d367c7c23acac0bb07e`。

报告真实状态分别是PASS_SOURCE_AND_INTEGER_LAYOUT_ONLY与
PASS_SMALL_SYNTHETIC_CSC_BYTES_AND_ALIAS_EFFECTS。没有读取研究数组、安装新solver或运行LU/BVP。
对应observed文件只转录上述真实回执；preparer实际前置门通过不等于数学候选通过。

## 规则更新

根README第12条已全文读过，根/本题README差异已按上一已读提交实际检查。
每次pull后检查两个README，至少每小时拉取/检查一次；已读提交记HANDOFF。
任何变化先读差异再继续，不以旧规则覆盖新作者要求。
