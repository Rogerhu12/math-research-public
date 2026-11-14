# G 诊断的明确源码闭包重放与原始 PP 解释澄清

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

本澄清适用于冻结的
`2026-11-10-78718-geometry-core-normalized-g-transport-v1.md`、其程序与两个
原报告，以及同 core 的静态重新投影诊断。原文件保持原字节，不追改哈希或
把后来的检查写成此前已经执行。

独立审者指出两项范围问题：`sys.modules` 不是未注册 importlib 模块的完整
清单；保存原始 PP 的各个 binary 系数也不能不经证明就按跨节点精确 $C^2$
解释。作者接受这两项限定。下面给新的真实源码重放，并明确严格恒等式、
精确单点与浮点沿程计算各自的适用对象。

## 1. 原自动源码集合遗漏什么

原 G 程序逐件核对了其收集到的 registered 模块与旧诊断的身份，但动态
加载后未注册到 `sys.modules` 的 adaptive、warped、flat patch、flat law
没有进入该自动集合。loader 单件在入口有比较，却没有进入同一程序的末回
核列表。因此原稿“实际全部动态导入源均已前后核对”之类表述过宽，应以
本段限定替代，不能把缺失记录当成自动存在。

原固定状态诊断的自动列表也有同类范围限制；这不等于这些源已经发生
变化，更不是数学计算已经证明失败。需要的是实际补全来源并重新执行，
而不是补一句说明后回溯声称旧运行受到了未执行的完整监控。

## 2. 明确列出的21件原数学源

新 companion 的 `EXPLICIT_ORIGINAL_SOURCES` 明列下列选定执行路径的源：

- 五件 loader/dynamic：`db6f-prefix-flat-geometry-source.py`、
  `950f-prefix-adaptive-chart-bvp-v2.py`、`950f-prefix-warped-bvp.py`、
  `db6f-prefix-flat-profile.py`、`950f-prefix-flat-accel-screen.py`；均位于 scripts。
- 四件 notes 模块：`fixed_metric_mode3_flow.py`、`fixed_metric_mode3_core.py`、
  `fixed_metric_mode3_bvp.py`、`repo_scan_gentle.py`。
- 十二件 repro/source-root 的 large-amplitude 脚本：`curve_linear_control.py`、
  `construct_rectifying_wavy_core.py`、`construct_reflected_stable_interface.py`、
  `construct_general_reflected_core.py`、`curve_stable_prefix_bvp.py`、
  `f6curve_local_frame.py`、`f6curve_bridge_linear.py`、`f6curve_inward_bvp.py`、
  `f6curve_bidirectional_bridge.py`、`f6curve_domain_newton.py`、
  `f6curve_outward_bvp.py`、`f6curve_outward_bridge_linear.py`。

这份列表针对本次两种只读诊断路径，不声称覆盖尚未执行的所有 BVP/tail
条件分支。所有21件在实际新运行前后均逐件读出字节数和 SHA。
新程序同时用 Python 的 `exec` audit event 观察实际执行的代码来源文件，
所以未注册的 importlib 模块也会被记录。其它 scratch Python 源若实际
执行而不在声明集合，会使该重放失败。

既有身份分成两个先前已绑定的来源文件：

1. 原成功 storage production plan，SHA256
   `232e9c3f3d748a4b9c83673d6627c576b53c80fbadcdff580da5b8c3bdd7cdf9`。
2. 原 fixed-state diagnostic，SHA256
   `53641e7e8ceb2ea822794a9df5404807a5162aa704aa9ee35be99b3c2d86dbfe`。

每件源至少要在其中一件有已有的身份绑定；若两件都列出，两个身份都必须
与当前字节匹配。不是挑选其中较方便的一边来绕过另一边的冲突。
五件动态源与第一件 plan 均相符；四件 notes 模块不在该 plan 中，但在第二
件诊断中，且逐件相符。新报告保留每件源采用了哪些既有绑定的 provenance。

程序另记录 Python/NumPy/SciPy 版本。这里的“源码闭包”特指声明路径的
仓库数学 Python 源，不声称对全部解释器/native 数值库做了形式验证。

## 3. 保留真实失败的 v1，再用 v2 重放

初版 companion 错把21件都要求存在于第一件 plan，真实 **9e24f7 exit1**
在 preflight 遇到 `notes/fixed_metric_mode3_flow.py` 即停止。原因是该条目
不在 plan，不是 SHA 发生变化。尚未执行诊断入口，无新输出或数学求解。
初版原样保留：

`scripts/78718-geometry-core-source-closure-v1.py`，9284 B，SHA256
`33abd1e921f2a0d38ad068f4217297dd8b0512ab72464ebd76b26cb59910ef8c`。

随后另名冻结 v2，将已有身份来源按第2节的准确实际情况写全：

`scripts/78718-geometry-core-source-closure-v2.py`，10241 B，SHA256
`66d741e38f89cf8a9a5a56df0ab158bb4425bb12f157a58fead07e90401a4a92`。

v2 在同一进程里用 `runpy` 执行冻结原诊断入口；原诊断不作任何改动。
入口正常返回后，21件源、入口、companion、两个已有身份文件再次复核。
它还将完整新结果与完整旧结果逐字段比较，**只排除 elapsed seconds**，
不只挑选相同的几个数学数值。

### 3.1 沿程 G 的完整新重放

真实 **24f857 / session66805 → 7c2bb2 自然 exit0**，约30.996秒。
执行原 `core-g-transport-v1.py --orders 4 8`；所有21件原源均被实际 `exec`
观察到，前后身份相同，完整非时间输出与原结果相同。

新数学报告为
`notes/2026-11-10-78718-geometry-core-g-transport-source-closed-v2.json`，15043 B，SHA256
`fb4e98a83a3b51e956fc3c520ecae092524e7abe49fe98519eaef19de676b4c7`。

明确闭包回执为
`notes/2026-11-10-78718-geometry-core-g-transport-source-closure-v2.json`，24297 B，SHA256
`85a62d9d78e29a76e26247ad490a71f4967dd6af2e60886a90e8b56ce0334cb2`。

### 3.2 同 core 重新投影的完整新重放

真实 **6fbe09 自然 exit0**，约0.841秒。执行冻结原
`core-reprojection-v1.py`；同样实际观察21件原源，完整非时间输出相同。

新数学报告为
`notes/2026-11-10-78718-geometry-core-reprojection-source-closed-v2.json`，22713 B，SHA256
`e444b5f414e1eda44fa2ac45f4528107a282fb291d996ce622f300d74a14b79f`。

闭包回执为
`notes/2026-11-10-78718-geometry-core-reprojection-source-closure-v2.json`，24268 B，SHA256
`c568bf24d8b47a26cb3c772f4ed26b9113b7a53b922e235cef9c8ea97531950f`。

这两次新运行支付的是新的实际来源检查，不是追溯声称旧程序从未遗漏。
原单点数值与所有浮点积分/重新投影结果在新的明确来源执行下已经重现。
仍为零 BVP、零 tail 请求、零新候选。

## 4. 泛型 C² 恒等式与 raw PP 分段对象必须分开

原 G 稿第2–4节对真正 $C^2$ 的 $F,\Theta$ 给出的材料导数、Frenet 代数、
投影重构与归一化恒等式保持其声明假设：
$$
D_s\left(\frac{|D_uF|^2}{a^2}-1\right)
=\frac2{a^2}D_uF\cdot D_u(F_s-W).
\tag{1}
$$
它不需要额外的全题 $C^3$ 门；在正根域内较弱导数可按原稿的乘积弱式解释。

但当前 CP 是保存各区间 binary PP 系数的原始表。把每个系数当作准确
dyadic 实数后，“曾由浮点 quintic Hermite 公式生成”本身不证明相邻表块
的0、1、2阶 jets 在实数意义准确相等。原稿把这份 CP 直接说成跨节点已
精确 $C^2$、没有额外节点源，范围过宽；此处撤回对 raw CP 的该推断。

对于这份表，(1) 和轴点公式可在各个开放 span 内使用。若把分段函数的
导数在整个区间作分布解释，还须包含相应的节点 jump。以一条轴上的
$\Gamma=G/a^2-1$ 为例，采用 PPoly 在节点取右块值的约定，从首节点到
另一个 native 节点 $s_N$ 应写
$$
\Gamma(s_N^+)-\Gamma(s_0^+)
=\sum_{k=0}^{N-1}\int_{s_k}^{s_{k+1}}
\partial_s\Gamma_k\,ds
+\sum_{k=1}^{N}\bigl(\Gamma(s_k^+)-\Gamma(s_k^-)\bigr).
\tag{2}
$$
如果右端采用左块值，就不包含最后一个 jump。图本身若有其它参数分段，
同样要按其真实一侧定义处理；不能先设节点 jump 为零。

原4/8 Gauss 计算积分的是 span 内的三项导数：总导数、projected-source
贡献、保存 PP 导数减 RHS 贡献。它报告的端点闭合差约
$2.6\times10^{-18}$/$1.85\times10^{-20}$ 仍只是浮点观测，包含潜在总 jump
以及数值积分/舍入影响；不能由这个小值证明各个 jump 严格为零或 raw CP
精确 $C^2$。本文没有新做该 jump 的精确全表包围。

后续生产若用 shared-jet 数据重新定义一个精确 $C^2$ 地图，那是明确的
另一个表示/构造，需按它自己的对象身份和误差转移论证。这里不会把 raw
PP 和该后续定义默认为同一个精确对象。

## 5. 不受这一范围修正影响的有限结论

入口 $s=0$ 的两轴公式只使用第一个块的常数系数、已知 $a(0)=1$、冻结
chart 首值、gauge $q$ 和完整 Cartesian 向量基。
其准确 Fraction 值不需要相邻 PP 块精确 $C^2$，因此原 CP 入口
$\psi=0$ 的
$$
-1.34\cdot10^{-8}<\Gamma(0,0)<-1.33\cdot10^{-8}
$$
仍是该有限对象的准确单点结论。明确来源的新重放也已重新计算同一分数。
它暂不等同于最终 common 图的另一个对象证书。

各 span 的归一化输运公式、两材料轴上 $\rho_s$ 与 Cartesian 旋转项、
不交换 $D_u$ 与采样投影的做法，也没有因上述解释而改变。
原小量积分只保持其实际浮点诊断身份；当前 core 的更高阶重新投影也保持
静态诊断身份，不是新求解的曲面。

这不是给全题增设“机器 C²”门或新的光滑性目标。它只是把已有完成标准
所涉及的精确对象、数值表示和诊断范围说准确；M15 真重求与原终门继续。

