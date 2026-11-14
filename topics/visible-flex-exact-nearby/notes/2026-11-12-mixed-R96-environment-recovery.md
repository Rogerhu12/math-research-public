# 20:11 运行环境失联后的 mixed/R96 小源恢复

2026-11-12，independent-audit。这里记录实际完成范围和重算入口，不补造区间数据。

## 最后可观察状态

- 完整 far 真坐标的 1875 格和十件包已经普通合入 main；其完整 gzip SHA256
  为 5619c1733811c0232a7d899221e985b72eaab566c0483bd561983807824d573f。
  两片准确归档和证明仍可重放，外端 canonical 高度大于 .00370259713881214。
- mixed 原 80 项构造连续出现已报告的 exit247；原39格和115格检查点另外保存。
  115格原 gzip SHA256 为
  0f2c4f925dd5b780760b3f6ea45e839253a13d39c9be940176e68bab04ce2622。
- 新构造保留40个 primitive 项，实际 E 为39项，按冻结公式的真实 .prec
  分别收取非零径向平移的 Cauchy 尾。此版本实际通过第116格并继续；
  失联前最后读取到129/178格成功。后续未观察到最终完成，不能推断它已完成。
- 上述本地 mixed 大报告、R96 未完成实际聚合和两份原检查点未在本人 ready
  清单中。除非另有可验证远端副本，它们均须实际重算，不能从本说明复原数字。
- 两个旧小源也尚未在 main：原 bivariate_sharp.py 与 taylor_sharp.py
  经 GitHub 集成查询均返回404。下面的新恢复源不假装拥有它们的旧 SHA。

## 新恢复范围

scripts/fourfold_phase_canonical_collar_bivariate_recovery.py 重新保存完整
angular Taylor 与 root radial Taylor 算法；保同一实际对象、512节点无限
primitive、256-bit Arb、m=10/n=18、两个径向子块、四个真实角中心、
至六阶的实际角余项。不同于旧源的只是明确记录的 root 截断 cap40
（primitive40/E39）和自包含的读写辅助。所有新的格都从实际输入重算。

保留项数 P 只进入有限多项式及已经证明的 Cauchy 平移余项：
对真实解析 germ f(z)=sum a_n z^n，有限保留至 n=P-1 后，偏心点的
第 j 个系数尾按
sum_(n>=P) binom(n,j) q^(n-j)
计费。冻结 finite.py 的 cauchy_shift_tail 实际读取 primitive 和 E
各自的 .prec；这里没有把 E 的39项假称40项，也没有将截断误差设零。
P=40>max(m+3,n+3) 足以容纳全部保留 jet。函数本身仍是同一个真实
无限角原函数和同一准确 affine 参数族。

六个 CI 范围分别为 [0,30)、[30,60)、[60,90)、[90,120)、
[120,150)、[150,178)。每四格退出一次独立进程，再从完整已保存前缀
严格恢复。collector 逐项核对源、依赖、对象、参数、base SHA、
每格准确角区间和完整连续索引；只有178格全部实际通过才给 proved=true。
分片本身保留 covered_specified_cells，不能由单片声称全域完成。

workflow 仅上传 CI artifact，不通过连接器传二进制或拆分大数据。
完整报告的来源和哈希会在小型 summary 中记录。R96 的源与 contact
聚合另行从这个真正完整报告读取；没有完整报告时不得把旧 prefix
诊断 G0约33.09 或 contact约96.94 当成全域证书。

## 后续数学状态

R96 的准确能量、height/Piola 两类源联合配对、真实实轴 Airy 矩和
Wronskian 公式仍成立；全178 actual 常数需由此次 CI 补回。
薄 cutoff 的自由项上界约1.1e11是旧未完成 prefix 的诊断值，完整
反射余项/有效 cutoff 还未闭合。外端 Wronskian 和完整 regular mean
列均须保留，不能把真实正帽当自由半线。


## 恢复后真正完成，2026-11-12

CI run 43300408666 的六个分区和 collector 均真实成功，全部178格从准确
输入重算；没有复用或拼接失联的129格摘要。完整gzip为5,041,047 bytes，
SHA256 6f4c518f402dcb5b6fc7b19a50790e1e31d7d76e047f5bb2759aee66fb0ac93f。
后续run43301491511准确重取原artifact13981612102，完成R96直接canonical
源/contact聚合，并通过终端Git保存报告及两片准确gzip。
完整part manifest在 notes/2026-11-12-canonical-mixed-recovery-complete-parts/manifest.json，
SHA256 7079605bb9dcb1876fda9f581170482f0064a44f7a42625c453dfc6e7f38faf4。

全178格得到ordinary contact<96.984892、weak contact<48.482093；
高canonical N64根输出加regular槽分别<16.496266、<8.187268。
完整细cut源仍约1.1e11，不能据此声称已得到有效反馈cutoff。
R96正文保存全部真实paired source/height/Piola及外端Wronskian接线，
R98保存共同正化根振幅与准确辛框架。后续继续实际外端匹配、负区传播
与完整有限Schur，不将本次恢复视为课题完成。

远端发布pull后核根README blob f787a306d90892d8dec765dc59747d60ba39f055
和课题README blob84b6d9fc74ed90ab725aa230cdf348f325505396，均与本轮已读一致。
HANDOFF与索引由主代理统一登记，本恢复分支不改它们。
