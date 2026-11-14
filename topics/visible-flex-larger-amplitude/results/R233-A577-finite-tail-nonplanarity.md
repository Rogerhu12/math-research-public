# R233. A 的 576 个有限 Hermite 尾片全部无开放平面片

作者：geometry_design，AI 辅助，2026-11-14。

**状态：对 R230 明确定义的有限场已证明。** 这不把该有限场认作原精确 ODE 尾部，也不补出尚欠的 metric、嵌入或 reach 估计。

## 明确对象及结论

使用本轮实际生成的全部 A 节点数据，见 [577 节点读出](../notes/2026-11-14-geometry-resume-actual-A-577.md)。对每个保存的 binary64 样本取其准确有理值，按 R230 (1.3)–(1.4) 定义全部512角样本的实 cardinal 插值；半径及平均高度亦取其准确 binary64 有理值。按 R230 (2.1)–(3.2) 选共享二阶数据并作五次 Hermite 拼接。

**结论。** 对这个原始有限场，其全部576个开径向片均不含映入同一平面的非空参数开集。对先按 R230 (5.1) 作显式半转对称投影、再作同一拼接的有限场，同一结论亦成立。两个场的结论分别成立，不把投影费用设为零。

## 完整证明与准确计算

在每个节点取角 $0,\pi/2,\pi,3\pi/2$。cardinal 多项式在这四个点的值准确等于保存样本；圆框三角值准确为 $0,\pm1$。公共平均高度在点差 determinant 中准确抵销。按照 R230 (6.1)–(6.3)，仅用整数及 Fraction 四则运算计算原始四点 determinant $D_j$ 和投影四点 determinant $D_{\pi,j}$。

本轮准确计算得到：577 个 $D_j$ 全部非零，577 个 $D_{\pi,j}$ 全部非零；576 个准确相邻半径差全部严格正。所有577个原节点压缩和解压字节都按实际 reader 的 SHA256 核对，没有填补数据或插值缺失节点。完整报告的 SHA256 为 `564f843ad14709695b74e4ae951813d7569931f462cd94d2782fb9c5adad40f0`；原始 JSON 1369037 字节，压缩186856字节，廉价表留在工作目录，源码及参数可重生。小摘要见 [cardinal summary](../notes/2026-11-14-geometry-resume-A577-cardinal-summary.json)。

现在固定任意一个开径向片。其 Cartesian 各分量是径向五次多项式与有限三角多项式的组合，因此在该连通开片上实解析。若一个非空参数开集映入平面 $v\cdot x=c$，则实解析函数 $v\cdot F-c$ 在这个开集为零，故在整片恒为零。连续延拓至任一端点圆周，该圆周都应落在同一个平面。这与端点四点 determinant 严格非零矛盾。原始场与投影场各自使用对应的非零 determinant，得全部576片的结论。径向接缝仅为有限条一维参数线，不存在只藏在接缝中的二维开集。证毕。

## 实际执行与复现

消费者 [geometry_20261114_actual_A_tail_cardinal_nonplanarity.py](../computations/geometry_20261114_actual_A_tail_cardinal_nonplanarity.py) 是原 R230 消费者的独立副本，只把 reader 的名字和源 SHA 更新为本轮修正了跨题源路径的 reader；准确 determinant 算法和所有原样本规则未变。

实际终端退出0、计算墙钟约5.058秒；这次同时直接读取输出的覆盖布尔量，原始/投影覆盖均为576，两个 uncovered 列表及两个 exact-zero-node 列表全部为空。

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_actual_A_tail_cardinal_nonplanarity.py \
  --complete WORK/nodes/complete.json \
  --owned WORK/owned-resource.json \
  --out WORK/cardinal-nonplanarity.json
```

这里 WORK 是前项实际完整 reader 的输出目录。不得将尚未实际获得 owned 0 的节点读取或不完整节点表替代本项输入。以后改变 accepted A、节点或场的定义，须对新对象重新消费相应数据；本条不是任意其他尾或真无限尾的非平面性定理。
