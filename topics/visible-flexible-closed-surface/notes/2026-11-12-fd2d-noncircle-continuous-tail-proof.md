# 实际非保圈字段的尾部连续线性误差

2026-11-12，Astra-visible-flex-fd2d。
本笔记说明 `fd2d-metric-c2-tail-linear-continuous.py` 的数学对象及连续包围。
完整非线性余项由 R112 §4.1 另付；本文的脚本不会把线性残差冒称为修复后 metric。

## 1. 同一实际尾图与同一目标

采用 R21 的 M12 common 图自身尾 manifest，精确半径由保存的二进增量与有理归一因子累加。
扰动 V 由原有 Fr 数据精确积分定义；区间实现保持原累加顺序。
`StreamingExactIntegratedTail` 只改变存储方式，不改变图、导数或取值。
本次另用 `fd2d-light-tail-definition-reader.py` 逐 shard 读取二进定义，
保留相同的 first/second/midpoint、首个 V0 和原精确径向增量；
每块全部列的有限性、SHA 和共享边界仍逐项检查。
原 verifier 不使用的数值 long-double node values 与诊断位置副本不再分配，
实际 V0 区间的逐节点积分仍由原 Streaming 类按完全相同顺序完成。
背景 packet 为该 manifest 的 `2026-11-09-db6f-audit-transfer-lowmetric-final-m12-critical-r01.json`，
含同一原 g 的连续 w、w_r 包围。该 packet 的解析供应依据仍为 R21 的同背景证明，
不由本次后处理重新声明或替换。

用物理半径 r、材料角 u 写参考目标

\[
g=E_0(r)\,dr^2+r^2du^2=d\sigma^2+r(\sigma)^2du^2,
\qquad E_0=1+w^2,\quad k=\frac{dr}{d\sigma}=-E_0^{-1/2}.
\]

上尾的实际高度是完整原尾高度的反射。这不改变诱导度量；
从 r 改为向 cuff 增长的 σ 时，交叉分量乘 k。
原始尾 verifier 的三个已先消去背景的坐标残差记为

\[
e=|X_r|^2-E_0,\qquad f=\langle X_r,X_u\rangle,
\qquad z=|X_u|^2-r^2.
\]

脚本逐系数使用原 `metric_residuals` 中相同的三个多项式公式。
常数高度规范在所有导数中消失，所以不需要重算深尾高度。

## 2. 字段分量与正确的线性张量

实际字段为

\[
v=p(r,u)\partial_\sigma+q(r,u)\partial_u.
\]

保存的两 jet 对 r 求导，p 本身仍是 **σ 位移**；不能将其误作 r 位移。
因而 `p_sigma=k*p_r`、`q_sigma=k*q_r`。
R112 的三项 Lie 导数与原误差相加，在 g 的正交标架中给

\[
L_{00}=\frac{e+2kE_0p_r}{E_0},\qquad
L_{01}=\frac{-f+\sqrt{E_0}\,p_u-r^2q_r}{r\sqrt{E_0}},
\qquad
L_{11}=\frac{z+2rk p+2r^2q_u}{r^2}.
\tag{1}
\]

首项分子可稳定写成 `e-2*sqrt(E0)*p_r`。
这是实际微分恒等式；既没有使用演化 RHS 替代 X 的真实导数，也没有假定 q 与 p 可分别消尽三个分量。
实际数据中可能有非常小的反对称/对称浮点余项；脚本保留 p、q 的全部 cosine 和 sine 分量。

## 3. 完整覆盖与区间算术

字段每个节点保存同一套值、一阶和二阶 jet；其定义是精确五次 Hermite 插值与有限 Fourier 和。
脚本核对全部保存块的 hash、顺序、数组形状、有限性、节点严格递增和零频 sine 恒零。
区域端点为实际 binary `.4` 与原 cut 半径。
字段是否在端点/接口零两 jet，以及它的全局 C² 与可逆性，由字段导数报告及 R112 的拼接论证共同承担。

先将实际字段节点与背景 packet 的**精确物理**端点合并。
原 packet 已覆盖尾图每个 span，且其 span 编号、局部端点和相邻拼接逐项验证；
因此每个合并区间同时属于唯一一个实际几何多项式、字段多项式和背景包围。
对限制映射 `r=left+(right-left)*x` 使用精确有理系数，再作向外舍入。

每个合并区间上的 w 取完整多项式及其原 remainder 包围。
由其连续 range 得到严格的 `sqrt(E0)` 与 k 常区间。
把这两个小区间乘入 (1) 的有限多项式系数后，**先相加抵消，再取范围**。
允许常区间各系数独立取值会扩大集合，但包含每个 r 的真实共同取值，所以包围仍有效。

对每个径向幂多项式作 Bernstein 变换，以系数凸包包围整个径向区间。
角变量使用覆盖完整三重周期的连续闭弧，正弦/余弦端点用有理 Taylor 包围，
并把弧内极值 ±1 纳入。全部有限 Fourier 模都参与求和。
因此结论不依赖角采样或径向采样点。

对真实对称矩阵 `[[a,b],[b,c]]` 同时采用

\[
\max(|a|+|b|,|b|+|c|),\qquad
\frac{|a+c|+\sqrt{(a-c)^2+4b^2}}2
\]

两个有效上界的较小者。每个式子的区间运算均向外舍入。
所有合并径向区间与所有角弧的最大值即所报 `linear_operator_upper`。
若仅选择一段径向区间作诊断，报告会明确 `complete_tail_activity_domain=false`，
不能用该局部最大值替代全域结果。

## 4. 与深尾、前缀及全时证书组合

字段支撑内侧的原图不改变。已有完整尾证书逐行按精确半径分组，
在 cuff 至 binary `.4` 的全部范围给 `1.1313778765583975e-9`；
该值取自 `2026-11-12-fd2d-metric-m12-tail-gauge-support-regions.json`，
没有把不利的原始行丢掉，也没有重新求原尾。

尾部完整线性结果、实际字段一二阶界与原图误差一旦具备，就可直接代入 R112 的精确非线性后验。
前缀在自己的 native s,u 及冻结 g0 中作同一后验，末尾再计入唯一精确桥的目标转移；
这里的尾部则直接相对原 g。取两个后验与未变深尾/帽部分的最大值。
字段在两侧 cut 的开邻域恒零，故这两种局部写法在同一闭材料流形上拼成 C² 微分同胚。

正确的全时新族由 R112 的材料相位公式定义；它保持旧族逐时像集，
所以旧族的全时嵌入、reach、D、固定帽、held 和 Euclidean quotient 几何结论均可直接用于这个已定义的新族。
是否达到原 `2e-9` 还须实际连续报告和真实后验结果，不能由本笔记的恒等式单独推出。

## 5. 已完成区间的准确复用与全角绝对和

最初完整尾计算主动以 exit130 结束，已完成的1043个区间均作为独立gzip member闭存，
SHA及实际最大值保存在 `2026-11-12-fd2d-metric-m12-tail-linear-full-01-intentional-stop.json`。
这不是数学失败，也不是外部进程退出。随后normal区间入口逐一核对完整精确端点、背景行、
几何span及原数学engine SHA，复用1043盒后计算另764盒；在stopfile请求下正常exit0，
共1807盒的完整记录为 `2026-11-12-fd2d-metric-m12-tail-linear-full-02.json`。
它明确 `complete_tail_activity_domain=false`，不能据此支付全尾。

normal运算在非零极小区间上扩大到±2^-400，并扩大正下溢余量，不丢任何真实模态；
准确舍入证明见 `2026-11-12-fd2d-metric-normal-interval-arithmetic-proof.md`。
最早checkpoint只在header记定义路径和engine SHA；输入hash是在接续时核对既有不可变字段记录后记入，
后续入口则在开始时直接绑定全部定义输入hash。不得倒写最早header已含它没有记录的字段。

对后续真实区间，`fd2d-metric-c2-tail-linear-fourier-resume.py` 可先用更便宜的完整全角包围。
设径向Bernstein hull已给各实际实Fourier系数区间Cj，则

\[
c_0(r)+\sum_{j\ge1}c_j(r)\cos(3ju)
\in C_0+[-S,S],\qquad
S=\sum_{j\ge1}\max(|\inf C_j|,|\sup C_j|).
\]

sine分量同理且零频项为零。正求和、加法和张量范数均继续向外舍入。
若此全角界已足够，就无需再把角域切成弧；否则仍使用原完整连续弧包围。
径向多项式、全部真实Fourier系数、目标及字段完全不变。
该规则只选择有效区间包围方式，并不是删去小系数、角采样或新增求解假设。
每个完成区间均记采用的包围方式；最终仍必须覆盖全部5030个精确径向区间。
