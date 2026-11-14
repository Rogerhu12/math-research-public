# 当前实际 canonical 坐标跨过真实样条节点的完整延拓

2026-11-12，independent-audit。

## 已完成的实际结论

同 R87、R94 的准确 affine 参数族
\[
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000
\]
上，R87 的同一六阶有限 root 坐标延伸到物理 \(r=243/1000\)。
本次完整有向计算覆盖
\[
 1493/6250\le r\le243/1000,\qquad 0\le\theta\le\pi/4
\]
的 1,875 个闭矩形；实际四重及反射对称将此覆盖延伸到整圆。
1875 个格、全部准确 scalar-span 选择以及原函数无限尾均在原完整
报告中保留，没有用有限角节点替代连续角覆盖。

此区间与 R87 的真正 \(0\le r-t\le1/2048\) 领口对每个参数都重叠。
重叠宽度严格大于 \(5.15551920\cdot10^{-6}\)。同一坐标在联合区域
保持 \(J>0,\phi_\theta>0,y_s>0\)，且在最外物理圆周上
\[
 \inf_\theta y(243/1000,\theta)
      >0.00370259713881214.
\]
因此真实平矩形
\[
                    0\le y\le7/2000=0.0035
\]
完整地位于联合坐标像内。这个结果支付扩大截断支撑的**坐标域**。
它没有把下面较粗的系数包络当作小反射余项，也没有授予全部反馈逆。

## 真实变量与换元恒等式

root 坐标由真正 root 系数函数定义；这些函数不是保存球的中点。
对离根位置 \(s=r-t(\delta)\)，直接计算同一个有限多项式
\((y,\phi)=\Psi(s,\theta)\)。实际物理几何则在每一个准确公共
scalar span 内重新生成：

- 样条节点及其反射节点全部以准确 Fraction 排序；
- 每个普通径向闭格显式指定一个真实相邻节点 span；
- native primitive、实际 \(E,K\) 和完整角尾按该 span 重新支付；
- 不把 root 所在样条多项式延拓当成过节点后的真实几何。

对真正 grounded 正 form \(B\)，执行准确变换
\[
 A=\frac1J D\Psi\,B(D\Psi)^T,\qquad
 \tau=A_{11}^{-1/2},\qquad
 C=\tau^2A=\begin{pmatrix}1&E_{12}\\E_{12}&y+E_{22}\end{pmatrix}.
\]
势与实际标量源密度仍为
\[
 V=-\frac{\tau}{J}\operatorname{div}_{s,\theta}
                         (B\nabla_{s,\theta}\tau),\qquad J/\tau.
\]
ordinary 引擎和 R87 的这些代数式相同。它只去掉了原 root 高 jet
引擎为控制宽球而使用的相对宽度 \(1/8\) 启发式；分母 \(J,A_{11}\)
的真实正性门始终保留，没有把失败分母截成正数。

固定 \(s\) 时 \(\phi_\theta>0\)，故每条角圆周映成同一度数一的
角图。固定 \(\phi\) 时
\[
                      \left.\frac{dy}{ds}\right|_\phi
                          =\frac J{\phi_\theta}>0.
\]
因此沿固定 \(\phi\) 的曲线，\(y\) 从 root 的零值严格增加；
不同的 \(s\) 不会在同一 \((y,\phi)\) 相交。结合最外边界的上述
正下界，给联合区域的全局单射及平矩形包含，而不只是局部 Jacobian 门。

## 实际连续包络

下表均为向外舍入后的更宽十进制界；原报告保留有向 Arb 端点。
这里只列普通远领口 \(1493/6250\le r\le243/1000\)，根邻域仍用 R87。

| 量 | 严格下界 | 严格上界 |
|---|---:|---:|
| \(y/s\) | 0.8043658602 | 1.0076770706 |
| \(y_s\) | 0.5297766564 | 1.0255747653 |
| \(\phi_\theta\) | 0.05308253965 | 0.29421241561 |
| \(J\) | 0.03147564880 | 0.28847648382 |
| \(A_{11}\) | 0.04696115835 | 1.21171955642 |
| \(\tau\) | 0.9084456246 | 4.6145632901 |
| \(J/\tau\) | 0.00006355105402 | 0.24239568791 |

ordinary source 的 \(C^0\) 与两个**固定物理 \(r\)** 的角导数也已
完整保存。当前全域粗界中
\[
 |E_{12}|<1.666395333,\qquad |E_{22}|<0.595021664,\qquad
 |V|<2.081571858\cdot10^9.
\]
这些界有明显的区间相关性损失，不能从 \(J,A_{11}>0\) 推出
\(C-\operatorname{diag}(1,y)\) 很小。固定物理 \(r\) 的角导数也
不能未经径向链式费用就当成固定 canonical \(y\) 的导数。
后续 strong source/contact 必须照实际所选空间另付这一步。

跨样条节点只使用当前对象真实的有限连续性；在格内的高径向 jet
是单侧多项式导数。本文不授予跨节点的无限径向导数、角解析宽度
或 direct-log 复合门。

## 失联检查点、严格恢复与完整覆盖

旧执行句柄失联且日志停留后，保存了原来的 1,186 个已完成格和
124 个待分裂矩形：

    notes/2026-11-12-canonical-far-lost-session-prefix1186.json.gz

其 SHA256 为
3eec60ff5477331d76dff11e1faaecc0ff71f083a2a26cf99ddb5d0d0cf462e5。
旧会话退出原因未报告，没有把它登记成成功或猜测具体原因。

恢复源 scripts/fourfold_phase_canonical_collar_far_resume.py 首先核对
原数学 evaluator、全部依赖、准确参数对象和根证书 SHA，再用
Fraction 检查 accepted 与 pending 的联合精确矩形拼接以及每个
scalar span 的真实性。它沿用原逐格 evaluator 和原二分规则，
仅改变检查点落盘与进程内存管理。完成后再次执行完整拼接检查。

准确恢复命令：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 MALLOC_ARENA_MAX=2 \
    python -u scripts/fourfold_phase_canonical_collar_far_resume.py \
      --checkpoint notes/2026-11-12-canonical-far-lost-session-prefix1186.json.gz \
      --out notes/2026-11-12-actual-finite-canonical-far-cover-resumed.json.gz

最终全部 3,078 次尝试产生 1,875 个成功叶，failed 与 pending 均为空。
完整报告累计记录的计算时长为 4821.0214 秒；该数只作运行元数据，
没有代替任何数学门。完整文件 SHA256 为
5619c1733811c0232a7d899221e985b72eaab566c0483bd561983807824d573f。

## 小于 5 MB 的准确分片与重放

完整 gzip 为 6,007,300 字节，不能直接按根规矩提交。
目录 notes/2026-11-12-canonical-far-complete-parts 包含两个准确
二进制片，分别为 4,000,000 和 2,007,300 字节。其 manifest 保留
原路径、原字节数、原 SHA 及每片连续 offset；不改原报告的数学身份。

已实际运行逐字节重组验证：

    python scripts/fourfold_phase_root_jets_reassemble.py \
      --manifest notes/2026-11-12-canonical-far-complete-parts/manifest.json \
      --verify-only

删除 --verify-only 即按相同路径准确恢复原 gzip。恢复后聚合命令为：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python -u scripts/fourfold_phase_canonical_far_aggregate.py

聚合源再次独立检查所有准确径向切片上的完整角拼接、同对象/同根、
依赖 SHA、真实 near/far 重叠以及最外 canonical 高度，随后给出
notes/2026-11-12-actual-canonical-far-aggregate.json。分片写入中遇到的
一次 Errno 28 仅影响归档创建；原完整报告此前已写成并保持相同 SHA，
空间恢复后重新完成分片和字节验证。
