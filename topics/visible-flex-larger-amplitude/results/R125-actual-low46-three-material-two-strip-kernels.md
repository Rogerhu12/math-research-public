# R125：实际低 46 模、三材料、两种角权的完整分块正核

作者：`/root/geometry_audit`（AI-assisted），2026-11-13。

**完整证明与实际消费已完成。** 本条在原固定真实外胞元 11、10 上，
沿原 10793 个材料叶及全部 10878 个已认证几何子片，完成

\[
25\text{ 个目标块}\times25\text{ 个源块}\times3\text{ 种材料}
\times46\text{ 个模}\times(P,K)\times2\text{ 种目标角权}
\]

的 345000 个正核系数，以及 3450 个逐源块、逐材料、逐模的真实切口
系数。固定角权 \(\sigma_0=1/64\) 与实际共同角权 \(\sigma(x)\)
分别保存。新的运算消费既有真实 Green 列和正积分，不重算 ODE，也
不求新的源积分。本条给后续低频接收的算子界，尚未证明低反馈或全频
方程闭合。

## 1. 固定对象、两个目标范数和源范数

沿用 R105/R119 的物理场、规范和真实 Green 恒等式。令

\[
F=\sqrt{rw^3},\qquad Y_m=F(P_m,K_m),\qquad
c_{\rm bg}=s+|\ell|,\quad s=r_x/r,\ \ell=w_x/w.
\]

\(f_m\) 是原 source-x 第二方程的 cosine 源幅度，即
\((P_m,K_m)_x=A_m(P_m,K_m)+(0,f_m)\)。它未再乘 \(r_x\)。
原无迹列记为 \(\phi_m,\chi_m\)，物理列为
\(\widehat\phi_m=\phi_m/F\)、\(\widehat\chi_m=\chi_m/F\)，真实
Wronskian 为 \(W_m\)。全部 \(W_m\) 的原区间都严格排除零。

原两个胞元的径向顺序分成 \(J_0,\ldots,J_{24}\)。这恰为已完成
中高模消费的同一 `comparison_partition`：18 个原 segment 中，仅
cell10/segment3 按原父叶索引分为八块。分块不改变材料、方程或原叶。

对 \(\nu=\sigma_0\) 或 \(\nu=\sigma(\cdot)\)，定义目标块范数

\[
\|u\|_{X_{i,\nu}}=
\sum_{m=2,4,\ldots,92}(1+m)
\left(\sup_{x\in J_i}\frac{e^{m\nu(x)}|P_m(x)|}{V(x)}
+\sup_{x\in J_i}\frac{e^{m\nu(x)}|K_m(x)|}{V(x)}\right).
\tag{125.1}
\]

每模每分量先取径向 supremum，然后求和。三种材料用 \(p=2,1,0\)
标记。在源块 \(J_j\) 上设

\[
a_{j,p,m}=\sup_{y\in J_j}
 \frac{e^{m\sigma(y)}|f_m(y)|}{c_{\rm bg}(y)V(y)^p},
\qquad q_{j,p}=\sum_{m=2,4,\ldots,92}a_{j,p,m}.
\tag{125.2}
\]

这里的源范数是 \(\sum_m\sup_y\)，不以 \(\sup_y\sum_m\) 替代。
原 parity 下，一个 cosine 幅度的两个 signed Fourier 半幅质量之和
等于该幅度模，所以 (125.1)–(125.2) 不另乘 2。

## 2. 同一个实际共同条带逐原叶重放

读取已经固定的原叶文件，逐项保留 \(dx_I,V_I,c_I\) 以及实际
`common_entry_jump` 和 `common_continuous_loss`。从原
\(18/125\) 开始，按原 18 组、各组原父叶顺序，先扣该叶入口 jump，
再扣完整 continuous loss，得到

\[
\sigma_{I,\max}=\sigma_{I,\mathrm{before}}-j_I,
\qquad
\sigma_{I,\min}=\sigma_{I,\max}-d_I.
\tag{125.3}
\]

全部运算使用准确有理数。逐叶核对 \(j_I,d_I\ge0\) 以及
\(1/64<\sigma_{I,\min}\le\sigma_{I,\max}\)。因此原叶内部的真实
\(\sigma(x)\) 位于该区间；接口两侧仍由相邻原叶各自覆盖。

每叶还准确核对

\[
0<V_I\le2^{-40},\qquad
c_{\rm bg}(x)\le s_I^{\rm upper}+|\ell|_I^{\rm upper}\le c_I.
\tag{125.4}
\]

所有 10793 个父叶的索引、准确 \(dx\) 和各组 \([0,1]\) 覆盖均
核对。原真实几何的 10878 个子片必须完整细分这些同一父叶，且每片
保存的 \(V\) 与该父叶逐字节数值相同。全 18 组和所有几何分块 SHA
再次核验；没有只抽取端点或重新划一个不同的材料问题。

## 3. 原真实 Green 核及一次物理归一

对支撑在任意源块的 \(f_m\)，原 Green 恒等式为

\[
(\mathcal G_m f_m)(x)=\frac1{W_m}
\left[
\widehat\chi_m(x)\int_b^x\phi_{1,m}(y)F(y)f_m(y)\,dy
+\widehat\phi_m(x)\int_x^R\chi_{1,m}(y)F(y)f_m(y)\,dy
\right].
\tag{125.5}
\]

原几何子片 \(I\) 已保存四个物理列的正包围
\(\Phi_{P,I,m},\Phi_{K,I,m},\Chi_{P,I,m},\Chi_{K,I,m}\)，分别控制
\(|\widehat\phi_{P,K}|/V\)、\(|\widehat\chi_{P,K}|/V\)。它还保存

\[
A^\phi_{I,m}\ge\int_I|\phi_{1,m}|F\,dx,
\qquad A^\chi_{I,m}\ge\int_I|\chi_{1,m}|F\,dx.
\tag{125.6}
\]

因此每个子片的源质量由以下准确向上取整的 dyadic 数控制：

\[
\alpha^\phi_{I,p,m}=
\operatorname{up}_{128}\left(c_I V_I^p
 e^{-m\sigma_{I,\min}}A^\phi_{I,m}\right),
\quad
\alpha^\chi_{I,p,m}=
\operatorname{up}_{128}\left(c_I V_I^p
 e^{-m\sigma_{I,\min}}A^\chi_{I,m}\right).
\tag{125.7}
\]

Arb 以 256 bit 包围指数及正乘积，随后向上存为 128 bit dyadic。
所有输出显式拒绝非有限值。源角权使用原父叶的最小宽度，方向正确。
\(A^\phi,A^\chi\) 已含整个正积分，故 (125.7) 不再乘 \(dx\)、
\(F\) 或 \(r_x\)。

令 \(w_m=\inf|W_m|>0\)。对目标子片定义

\[
\omega_{I,m}^{(0)}=(1+m)e^{m/64}/w_m,
\qquad
\omega_{I,m}^{(\sigma)}=(1+m)e^{m\sigma_{I,\max}}/w_m.
\tag{125.8}
\]

将它们分别乘四个原物理列，并对每个目标块取最大值，得到
\(\bar\Phi_{i,m,C}^{(\nu)},\bar\Chi_{i,m,C}^{(\nu)}\)，其中
\(C=P,K\)。这一阶段已除 \(w_m\) 一次；后面的场核不再除它。
共同角权取入口 jump 后、continuous loss 前的最大宽度，覆盖该叶
全部目标位置。物理列已经包含原 \(F^{-1}\) 和目标 \(V^{-1}\)，
也不再加 balanced frame 换范数费用。

## 4. 非对角块与有序对角块

第一遍按原径向顺序保存全部 (125.7)，并用准确 `fmpq` 求和

\[
T^\phi_{j,p,m}=\sum_{I\subset J_j}\alpha^\phi_{I,p,m},
\qquad T^\chi_{j,p,m}=\sum_{I\subset J_j}\alpha^\chi_{I,p,m}.
\tag{125.9}
\]

若 \(j<i\)，整个源块位于目标左侧，只出现 (125.5) 的第一支；
若 \(j>i\)，只出现第二支。故每分量的正核可取

\[
K^{(\nu)}_{i,j,p,m,C}=
\begin{cases}
\operatorname{up}_{128}(T^\phi_{j,p,m}\bar\Chi^{(\nu)}_{i,m,C}),&j<i,\\
\operatorname{up}_{128}(T^\chi_{j,p,m}\bar\Phi^{(\nu)}_{i,m,C}),&j>i.
\end{cases}
\tag{125.10}
\]

对 \(i=j\)，第二遍再次完整读取原几何。在当前子片 \(I\) 之前的
准确 \(\phi\) 和记为 \(P_I\)，之后的准确 \(\chi\) 和记为
\(S_I\)。对该片任意 \(x\)，左右两个部分积分分别被

\[
P_I+\alpha^\phi_{I,p,m},\qquad S_I+\alpha^\chi_{I,p,m}
\]

控制。把该片的四个原列乘 (125.8)，按 (125.5) 加两支，分别对
\(P,K\) 在目标块所有子片取最大值，得到有序对角界。

程序从 \(\chi\) 后缀中只减去本身保存的同一个 dyadic 项，因此
这是已知准确正数和的重组，不是从两个相关未知区间任意相减。每个
源块、每材料、每模的最后后缀均准确为零，前缀均准确等于原完整和。
当前片在两个部分积分中都付完整正贡献只会放宽上界。

另保留完整块的粗上界
\(T^\phi\bar\Chi+T^\chi\bar\Phi\)，并与有序对角界取较小者。
两者都控制同一个完整算子，所以这个最小值合法。

由 (125.5)–(125.10)，对每 \(m,C\) 都有相应的径向分量上界。
加 P/K 后再求模态和，即得

\[
\|\mathcal G(f|_{J_j})\|_{X_{i,\nu}}
\le\sum_m\bigl(K^{(\nu)}_{i,j,p,m,P}
                 +K^{(\nu)}_{i,j,p,m,K}\bigr)a_{j,p,m}
\le\Gamma^{(\nu)}_{i,j,p}\,q_{j,p},
\tag{125.11}
\]

其中 \(\Gamma\) 是每模 P/K 正核之和的最大值。输出文件另保存
该和的模态总和：它可消费每模各自一个帽，不能把同一份共同源质量
复制 46 次后仍称 (125.11) 的最大列界。程序和聚合索引都明确区分
`max_mode` 与 `sum_modes`。

## 5. 原 46 轴的真实切口核

R105/R119 同一 canonical 高度读出满足源修正恒等式

\[
\delta Q_m(b)=W_m^{-1}\int_b^R\chi_{1,m}F f_m\,dx.
\tag{125.12}
\]

令 \(a_m^{\rm axis}>0\) 为 R100 原轴；前六个为原半轴，其余四十
个为原加权 \(\ell^1\) 轴。读出至原归一参数的源核为

\[
C_{j,p,m}=\operatorname{up}_{128}
\left(\frac{T^\chi_{j,p,m}}{w_m a_m^{\rm axis}}\right).
\tag{125.13}
\]

这是真实 cut 的原始轴读出，不是场强范数，因此不加 \((1+m)\) 或
目标角权。源角权已在 (125.7) 支付。全部 46 轴逐行核同一个冻结的
R100 ledger，没有以新轴或新增模式替换。

所有 3450 个 (125.13) 都保存。对 S 的 \(\ell^\infty\) 读出和
T 的 \(\ell^1\) 读出，都另保存逐模最大值和总和；哪一个可用取决
于输入是共同质量还是独立逐模帽，与第 4 节的区别相同。

## 6. 三材料的直接接口

若同一源块上某个非负已付包络满足 \(R(y)\le S_jV(y)\) 及
\(R(y)\le R_j^{\max}\)，则逐点

\[
VR\le\min(S_jV^2,R_j^{\max}V),
\quad
R^2\le\min(S_j^2V^2,S_jR_j^{\max}V,(R_j^{\max})^2).
\]

正算子分别消费各个合法支配后，可对同一个核系数取

\[
\Gamma_{VR}\le\min(S_j\Gamma_2,R_j^{\max}\Gamma_1),
\quad
\Gamma_{R^2}\le\min(S_j^2\Gamma_2,
S_jR_j^{\max}\Gamma_1,(R_j^{\max})^2\Gamma_0).
\tag{125.14}
\]

这保留源块位置和目标角权。实际 PDE 应用仍须先证明相应的
\(\sum_m\sup_y\) 源质量；(125.14) 本身不会把仅有 pointwise 量
自动变成这个范数，也不包含任何尚未支付的低反馈常数。

## 7. 正式执行、完整索引与保存

生产源为
[`root_low_block_three_material_kernels.py`](../computations/root_low_block_three_material_kernels.py)，
SHA256 为
`13daf8abed64b73681b7db6f768d745c6945a582a2a1e1c202ce7b78bd6c8d5a`。
它从独立 scratch 源启动，冻结帮助源为已独立审阅的
`root_outer_full_linear_centre_source.py`，SHA `987435e9…`。

| 阶段 | formal exit | wall 秒 | 峰 RSS KiB | 实际核验 |
| --- | ---: | ---: | ---: | --- |
| 两遍三材料、两角权 Green 消费 | 0 | 411.422247171402 | 79068 | 21 个汇总门；全 10793/10878 覆盖和全部准确前后缀 |
| 原结果的 Fraction 聚合索引 | 0 | 4.395544767379761 | 24296 | 356250 个非负性及 P/K/模态聚合比较 |

主摘要 SHA 为
`6375e1ada4c9124482f9d8f92875c0f4cb26e31354e7037f1e3aa5d74fde7a95`。
25 个 target 压缩包合计 8097752 B，最大单包 325946 B；其中保留全部
逐模 P/K 值。原正源的 99 个可再生工作块保留完整位置、逐项 dyadic
和 SHA；实际主结果不以这些工作块缺省来删减任何源。

轻量聚合入口
[`root_low_block_kernel_aggregate_index.py`](../computations/root_low_block_kernel_aggregate_index.py)
再次核每个目标包和 cut 包的 SHA、所有模式、两分量及 max/sum
关系，未重新计算 Green。它给可直接加载的
[`2026-11-13-root-low-three-material-kernels-r1-aggregate.json.gz`](../notes/2026-11-13-root-low-three-material-kernels-r1-aggregate.json.gz)，
SHA `a5f45c021cf54576fa10647724127001ec793b9b70a5951cc7ff4cb8d79152c2`。

其布局是

```text
Gamma_max_mode[norm][target_block][source_block][power_index]
Gamma_sum_modes[norm][target_block][source_block][power_index]
norm = "sigma0" 或 "common_sigma"
power_index = 0,1,2，分别对应 p = 2,1,0
每个值 = [准确整数 mantissa, binary_exponent]
```

`cut_max_mode[S或T][source_block][power_index]` 和 `cut_sum_modes`
同理。完整每模 cut 保存于同前缀 `-cut.json.gz`，SHA 为
`3ddbc28f8ef2687c551fd6263758f4bb1540502b5ecbdcf4e7052b126b2212b9`。
稳定 manifest 给出原工作路径、仓库文件、每个 SHA 和资源记录。

本条算子始终属于上述旧固定真实度量和原 46 模 Green 问题。与同时
运行的 strong q098/q106 数值几何对象没有转借关系。原完整 mean、
逆分母和高频源质量要由后续同对象的非线性分析支付；本条没有独自
宣告低中高联解、全频外 PDE、闭面或大幅度完成门成立。
