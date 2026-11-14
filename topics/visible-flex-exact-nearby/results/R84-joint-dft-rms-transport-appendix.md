# R84 附录：准确节点选择后的二维 DFT 均方误差传递

**状态：已证明。** 本附录改变有限近似的构造方式，避免把同一个参数盒造成的
节点不确定性分别放大到每个 Fourier 系数。真实解析 alias、无限角尾、无限时间尾
和后续系数舍入仍全部支付；没有宣称它们为零。

## 1. 归一化 DFT 的有限误差

设时间圆有 $N_t$ 个节点 $u_a=\rho e^{2\pi ia/N_t}$，
角圆有 $N$ 个节点 $x_b=2\pi b/N$。
对任一真实实参数 $p\in I$，实际样值为 $v_{ab}(p)$。
从各个有向包含球选出一个准确 dyadic 数 $z_{ab}$，并已付

$$
|v_{ab}(p)-z_{ab}|\le e_{ab}
\quad(\text{对全部 }p\in I).
$$

定义归一化二维 DFT

$$
\widehat v_{ik}(p)=\frac1{N_tN}
 \sum_{a,b}v_{ab}(p)e^{-2\pi i(ia/N_t+kb/N)},
$$

及相同的 $\widehat z_{ik}$。准确 Parseval 恒等式给

$$
\sum_{i=0}^{N_t-1}\sum_{k=0}^{N-1}
 |\widehat v_{ik}(p)-\widehat z_{ik}|^2
=\frac1{N_tN}\sum_{a,b}|v_{ab}(p)-z_{ab}|^2
\le\epsilon^2,\qquad
\epsilon=\left(\frac{\sum_{a,b}e_{ab}^2}{N_tN}\right)^{1/2}.
\tag{A1}
$$

这对每个实参数分别成立，不要求复参数域，不要求节点误差独立，也不假定误差互相抵消。
即使各个球使用同一参数，逐节点上界仍给 (A1)。

保留 $0\le i<m\le N_t$、$|k|\le K<N/2$，
把时间系数除以 $\rho^i$，用频率比例 $\nu$ 解释角函数。
在 $|u|\le r$、角条带宽 $s$，保留矩形的加权系数误差不超过

$$
\epsilon
\left[
\left(\sum_{i=0}^{m-1}(r/\rho)^{2i}\right)
\left(1+2\sum_{k=1}^K e^{2\nu ks}\right)
\right]^{1/2}.
\tag{A2}
$$

证明：对保留指标的误差系数和权重
$(r/\rho)^i e^{\nu|k|s}$ 用 Cauchy–Schwarz；
第一个平方和至多是 (A1) 的完整平方和。
因此 (A2) 控制整个有限矩形的 $\sum_i r^i A_s$ 误差，也控制全实时间上的
$A_s$ 范数和复角 sup。所有正负模及零模都包含在内。
实际物理角 $\nu=4$，归一化标签角 $\nu=1$。

## 2. 实性和准确有限对象

源对实时间、实角、实参数为实。若 $N_t$ 为偶数，则代码只求上半时间圆，
下半节点选为上半准确 dyadic 节点的共轭。
两个实时间节点选准确实数；实际包含误差仍按整个球与所选数之差支付。
故选定数组本身准确满足共轭关系，其时间 DFT 对每个实角节点为实。
负角 Fourier 模定义为正模的共轭；这些都是选定有限对象的准确性质。

实现不在包含球上免费去掉半径。它先记录 $|v-z|$ 的有向上界，
然后才对准确 $z$ 做 DFT。DFT 根单位和运算误差用球算术包住，
后续 Fourier 系数选取、实部投影和 dyadic 舍入按原完整系数费用另付。
这些额外费用与 (A2) 不同，不能只付其中之一。

## 3. 解析补集仍是同一个真实源

真实节点的 DFT 本来包含角 alias 和正时间 alias；
(A1)–(A2) 仅比较两个**有限 DFT 数组**，未消除任何 alias。
真实场在已付双盘上的 Cauchy 系数界仍用于：

- 真实时间 DFT 的所有 $i+\ell N_t$ 项；
- 角采样折叠的所有 $k+\ell N$ 项；
- 未保留的真实时间阶和角 Fourier 模。

因此可把 (A2) 作为一个独立有限节点误差项加到 R67/R84 的原完整重建预算中。
在中心场和实参数盒场上证明完全相同，差别仅在实际 $e_{ab}$ 的大小。
对有限参考密度同样成立；其真实 $f-P$ 复合费仍只按已证明的标签 sup 合同计入。

实际入口：
scripts/fourfold_joint_dft_l2_noise.py，
以及接入它的 scripts/fourfold_parameter_density_pipeline_l2_v2.py。
源码中的 joint_circle_midpoint_l2 支付 (A1)；
joint_retained_rectangle_error 支付 (A2)。
完整叶是否通过由其实际报告决定；本有限代数引理本身不授予缺失的场域或参数盒。
