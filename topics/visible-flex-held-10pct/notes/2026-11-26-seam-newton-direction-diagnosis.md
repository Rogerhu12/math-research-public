# 实际唯一接受步的参数方向与一次原 collocation LU 诊断

维护：Astra-held10-06bbeb39-20261126。2026-11-26。

可信度：第 1 节由实际保存的小记录与原 Newton 更新式直接推得；第 2 节是已读源码的链式核对；第 3 节的新诊断入口已编译并通过 CLI，但尚未执行真实 LU。没有新 BVP、$\lambda$ 进展、实际尾耦合或完成结论。

## 1. 小的返回参数掩盖了大幅原方向

输入是已保存的 `2026-11-26-warm-v3-anchor-actual.json` 与 `2026-11-26-warm-v3-first-lambda-failure.json`。前者实际原参数向量全为零；后者记载

$$
\text{accepted\_steps}=1,\qquad
\alpha=2^{-20},\qquad
\text{no\_step}=3.
$$

原更新为 $p_{\mathrm{new}}=p-\alpha d_p$。径向网格加密本身不改变参数，故唯一被接受方向的参数分量满足

$$
d_p=-2^{20}p_{\mathrm{return}}.
$$

这是从真实返回参数推得的方向；**尚不知道该接受步位于第几个 adaptive mesh 或哪一次 Jacobian，不能称它是首个 631 节点上的已观测方向。** 它也不提供状态方向 $d_y$。

精确 binary 有理数运算给出

$$
\max_j |(d_p)_j|\approx6.610210638732021,\qquad
\sum_j |(d_p)_j|\approx76.70912772807789,
$$

而首分量 $(d_p)_0\approx0.09459551589230289$。因此 raw 中 $10^{-6}$ 量级的参数不表示未缩放 Newton 方向很小。按未阻断的辅助坐标公式，完整该方向会给出 $q_{\mathrm{aux}}\approx0.054584450146097536$，仍位于原正辅助域；这里没有把这个反事实完整步说成已通过核心或 Frenet 域。

原循环最多取 21 级 $1,2^{-1},\ldots,2^{-20}$。实际统计

$$
27\ {\rm domain\ rejects}+56\ {\rm merit\ rejects}+1\ {\rm accept}=84
$$

恰好等于四次线搜索的 $4\times21$：三次彻底无步，另一次也直到最后一级才接受。这个记录不能单独区分核心曲率域、Frenet 域、线性系统误差、原函数与 Jacobian 的偏差或 merit 的控制权重。

必要精确小标量与源 SHA 在小记录 `2026-11-26-seam-newton-direction-readiness.json` 中。该推导不复跑任何旧场。

## 2. 源码核对排除了两个直接猜测

沿 `warm_complement_core_factory_v3`、`950f-prefix-warped-bvp`、`exact_core_lift`、`analytic_adaptive_core_jac` 的实际定义，旧参数尺度的导数链是

$$
d_1=c\log(q_{\mathrm{aux}}/q_g),\qquad
d_j=c\,c^{\mathrm{legacy}}_j/s_j,\qquad
c^{\mathrm{legacy}}_j=s_jp_j.
$$

provider 的 `input_chain` 再乘 BVP 的 $[q_{\mathrm{aux}},s_2,\ldots,s_M]$，数学上逐列得到 $c$。未见把高阶 `pscale` 漏乘一次或多乘一次的源码证据。实际二进制 exp/log、积分与投影误差仍须用原函数方向差分观察，不能以该公式宣称实算 Jacobian 已验证。

解析 exact-lift 参数列保留了对流项 $v\,\delta F_\psi$，以及径向 lift 项的 $-h'\delta H$。固定 $\delta$ 时 cut 已超出 lift 支持窗，$h=h'=0$，cut chart 也归零；该线性 DN 尾端对核心参数的直接导数为零，与原 boundary Jacobian 的零参数尾块相容。未发现一处可直接据此改掉的参数列符号错误。

原 merit 是固定当前 LU 后的

$$
\Phi(\widetilde y,\widetilde p)
=\|J_{\mathrm{base}}^{-1}F(\widetilde y,\widetilde p)\|_2^2,
$$

接受式为 $\Phi(z-\alpha d)<(1-0.4\alpha)\Phi(z)$。它采用拼接的所有状态节点与参数的 Euclidean 平方和。不能用核心 basis 条件数代替这个完整 BVP 线性系统的实际行为。新入口直接测量这个对象。

## 3. 新入口：一次真实方向，原判据逐级记录

新增 `scripts/resume_20261126/seam_probe_original_newton_direction.py`，SHA-256 `d9b3a7ade73f064f3d07ebfef361c0e07e12cba4c6f461ff5fc0ae05b40809d8`。其工作为：

1. 读真实接受的 v2 或 v3 锚及其原 raw 数组，调用对应正式模型。以原 warm step 的同 $M$、`refine=1`、目标 $\lambda=.004$、原 chart、完整 lift 系数 $1$ 与原尺度重建初始化；不重采样原节点。目标 dictionary 只是几何定义，不冒称已接受记录。
2. 使用原 `split_rhs(...,8)`、分块原解析 Jacobian、SciPy 原 `wrap_functions/prepare_sys`，按原 residual 的 Fortran 展平次序拼接 collocation 与 BC。
3. 只组装和分解一次完整原稀疏 Jacobian，算 $d=J^{-1}F$。分别记录 $\|d_y\|_2^2$ 与 $\|d_p\|_2^2$，同时原总成本仍按原来的单次 `step@step` 计算；记录实际 $Jd-F$，不从 basis 条件数推测逆。
4. 始终从同一初始化点沿同一 $d$ 检查全部 21 级原 $\alpha$，记录实际异常全文及核心/Frenet/辅助/坐标类别、原 residual、状态/参数成本和原 Armijo ratio。首个满足点只记录；之后的点明确是同一基点的诊断，不应用任何更新。
5. 默认在 $\alpha=2^{-18},2^{-20}$ 用原函数检查方向差分。负向有效时记录 $(F(z)-F(z-\alpha d))/\alpha$ 与 $Jd$ 的差；正负都有效时另记录中心差分。域失败照实记录，不夹根、不改单边结果成中心差分。
6. 恢复模型在基点参数的缓存；不调用 `solve_bvp`，不改部署 Newton，不做 mesh refinement，不接受新场，也不调用 DN。

实际调用形式（路径应由所在 runner 的真实恢复记录给出）：

~~~bash
python topics/visible-flex-held-10pct/scripts/resume_20261126/seam_probe_original_newton_direction.py \
  --source-run /runner/warm-v3-design/reexpressed-anchor/run.json \
  --homotopy .004 \
  --outdir /runner/warm-one-newton-direction
~~~

输出的小 `summary.json` 留完整标量诊断及输入/源哈希，不导出大型 LU 或场数组。当前只实际完成 Python 编译和 `--help`，均 exit $0$；真实锚/源依赖在原 runner 上恢复后才能执行。该诊断计算的是一个**新的、明确初始化网格上的方向**，不将其混同第 1 节位置未知的那次旧接受方向。

若原函数方向差分与 $Jd$ 不一致，应先定位 Jacobian/算术链；若 $Jd-F$ 大，应先处理线性解误差；若这些相容而域/merit仍迫使极小步，才能据实际状态/控制成本与域错误决定不改变原问题的 Newton 数值调整。这里尚未采纳或部署任何调整。


部署只另加 `observation.json` 的有限诊断投影，以便既有worker的status/progress/result白名单读取完整21级统计；完整报告和输入身份仍留runner。数学运算与原判据不改。新请求排在当前v3父链自然返回之后，未抢占实际求解，也未称诊断已经执行。

同一个 LU 另对有效方向差分向量作三角回代，记录 $d^T J^{-1}(DFd)/\|d\|^2$ 的有限差分估计，不新增分解。若 $J=DF$，理想值为1，原merit沿负方向的归一导数为−2；原0.4 Armijo的一阶条件是该alignment大于0.2。因此原空间的Jv误差小仍不足够，需要同时看其被原LU逆放大的结果。该估计不是严格导数区间，也未改变更新。
