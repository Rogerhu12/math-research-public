# 950f 接手、现状核对与优先路线

会话 Astra-visible-flex-950f9f73，2026-11-09 +08。状态：研究中，无满足全部标准的闭曲面。

## 接手证据

已读根 README（blob f28db43754eef3b9f96d3981a6829f3574d461b9）、本题 README（099f451b142e184c223d2d0764887d99bd492db5）、HANDOFF（aaac3d167cda07eb93c3b582a808c616e4c602ca）、open（677f2efacc42c38a05f80d08105afc7648ea0e12）。认领 QUEUE 提交 d4952985ab1a52e0316f981183b2df0d37046439；旧 HANDOFF 完整归档为同目录 2026-11-09-950f-intake-handoff.md。

只写本题、自己的 QUEUE 行及根日志追加。独立工作区由已有仓库的已提交状态克隆；本题 notes/scripts/results 目录树与远端一致。终端 git HTTPS 无可用认证；改用已连接 GitHub 的原子 tree/commit/ref 操作，始终读取当前 main，以 expected_sha 且 force:false 发布。不会改其他会话的工作区。

## 本轮公开文献核对

- Mohammad Ghomi, *Open Problems in Geometry of Curves and Surfaces*, 2019-09-02 revision, Problem 1.1, p.5，https://ghomi.math.gatech.edu/Papers/op.pdf 。本轮实际打开原 PDF 并核对问题；这是2019版本的陈述，不能外推为2026年没有新进展。
- Alec Payne, *Flexible Smooth Immersions of Cylinders in R^3*, UC San Diego official seminar, 2023-11-16，https://www.math.ucsd.edu/seminar/flexible-smooth-immersions-cylinders-r3 。实际打开摘要；结论针对非极小、非可展的浸入圆柱，闭曲面只是讨论可能途径。
- Ivan Izmestiev, Arvin Rasoulzadeh, Jonas Tervooren, *Isometric Deformations of Discrete and Smooth T-surfaces*, arXiv:2302.08925；Computational Geometry 122 (2024), 102104，https://arxiv.org/abs/2302.08925 ，https://doi.org/10.1016/j.comgeo.2024.102104 。本轮核对原始摘要和出版信息，摘要未提供本题定量闭嵌入族。

对近期相关文献另作检索，尚未得到可直接套用的定量完成定理。检索范围有限，不能由无检索结果推断不存在。

## 仓库最新现状（只读）

1. continuous-flexibility-swarm/HANDOFF（9aedc41a7dabb47fd08a0e9f25d1d52b9dd7fc49）记录R520的精确非定量C²闭嵌入族及两份独审。这里只读取交接，没有重审其全部依赖；不据此声称本题指定幅度/厚度已经有解。
2. large-amplitude-twist-flex/HANDOFF（6c032b62830e6d6a586a84a322becece448b88ca）已到R48，R39的M20近似闭图曲率界约95.102、D上界9.225，不符本题reach/D要求。R46新付当前exact源的全频47参数深尾存在，但只在共同足够深N；不含本题3Z、浅端口匹配或可见幅度。
3. smooth-unrippled-twist-flex/HANDOFF（c024694f06a5adc1b610395349d3e13926a3cae6）记录R11：若完整闭C²图满足正支撑F·n≥σ、主曲率界K，则reach≥min(σ,1/K)。另有R17冻结显式XYZ前缀的连续几何证书；但全族、同metric加密仍未完成。R11值得核原文后采用，避免把全局reach永远留成未实现的全点对扫描。

## 具体数值路线

- 前会话 closing-asymmetric-m3-continuation 笔记中的 weighted width=.45 候选比旧 HANDOFF 更进一步；K6报告DN10.57651355、T门.001842092、height=.00135时形式κ6.83073、minA.26714。尚属线性/形式数值，未付真实非线性。旧 optimized-tail worker 接非weighted源，必须显式换为正确constructor并完整重跑。
- 旧实际匹配核心与R7纯单谐波切向角核心不同。M12入口截断误差约.00218；固定metric下径向加密不能解决角向谱未解析。考虑固定参考法向角重参数化，只改变数值坐标，不改变g，并在新坐标中正确审计metric。
- weighted width=.45使深圆领半径变成.15，R8原文的.25半径常数不能逐字套用。独审负责重算适用界。
- 依赖来源旧f6f33987b45e目录当前不存在；可读源位于 /workspace/scratch/1dce210849f9/math-research。重跑显式source-root并记录哈希，不把路径失效误报为数学缺源。

## 分工与正确性门

nonlinear_tail做实际非线性DN；macro_prefix做冻结metric大幅度核心/前缀；independent_audit未参与构造，核证与独立重跑；root负责整体闭合、全局reach、H/open与main同步。新结论先完整写入notes并独审，才收入results。无论局部残差多小，固定taper缺陷、改变metric的“加密”、只付端点/局部曲率都不算完成。
