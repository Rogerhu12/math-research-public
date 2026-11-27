# 五个独立正权的完整 S2 与六位出生二首边

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f / stable_kernel_return。

**状态：全文结论已证明。** 对五个任意独立正权，R275 的同源 S2 严格成立；相应完整费用 $\mathsf K=A^*G_uA$ 满足
$$
\operatorname{Tr}_{L}(\mathsf K^2)<\frac14.
$$
结合已刊的五位完整 S1、同一个低出生源上的严格 $1/2$ 首末边及 R275 的完整一位递推，得到六个任意独立正权的出生二首边严格成立。下面不把这条有限结论提升为全部出生、无限联合来源或 $N=\overline{B\ker T}=\ker T$。

## 1. 同一个物理源和待证正块

取五个任意 $b_i>0$，在通常物理 Boolean Hilbert 空间上令
$$
d=\sum_{i=1}^{5}b_iE_i,\qquad
\mathcal C=\sum_{i=1}^{5}b_i^3E_i,\qquad
e=\sum_{i=1}^{5}b_i^{-1}E_i^*.
$$
令
$$
K=\ker d\cap\mathcal H_2,\quad \dim K=5,\qquad
L=\ker d\cap\mathcal H_1,\quad \dim L=4.
$$
全部伴随使用原物理内积。完整归一最小逆记为
$$
\mathcal J_{j,r}=(d^j/j!)^\dagger|_{\ker d\cap\mathcal H_r}.
$$
置
$$
G_u=\mathcal J_{1,2}^*\mathcal J_{1,2},\quad C_u=G_u^{-1},
\qquad L_j=\mathcal J_{j,1}^*\mathcal J_{j,1}\quad(j=1,2,3),
\qquad \mathcal B=\mathcal C|_K.
$$
这里五位出生二确为高度一硬端；没有构造或使用非法的上出生第二 Gram。令
$$
A=\frac12\left(C_u\mathcal B^*L_2+
\mathcal B^*L_2L_3^{-1}L_2\right),\qquad
\mathsf K=A^*G_uA\succeq0\quad\hbox{在 }L\hbox{ 上}.
\tag{1.1}
$$
要证明的正是 [R275 §4](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 的原 S2：
$$
\mathsf K+L_1L_2^{-1}L_1\prec I_L.
\tag{1.2}
$$

## 2. 一次完整 MP 投影，保留两个交叉项

记
$$
d_+=d:\mathcal H_3\longrightarrow\mathcal H_2,\qquad
R_2=d^2/2:\mathcal H_3\longrightarrow\mathcal H_1.
$$
五位正权下 $d_+$ 可逆，$R_2$ 满行秩，并且
$$
\operatorname{Ran}\mathcal J_{1,2}=\ker R_2,\qquad
P=I-R_2^*(R_2R_2^*)^{-1}R_2
$$
是这个完整五维子空间的物理正交投影。

[R297 的 Ward 消逆式](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md) 以及[同源单投影推导](../notes/2026-11-28-odd-hard-top-s2-one-projection-source-8542.md) 给
$$
A=C_u\left(\mathcal B^*+(e^*|_K)^*L_1L_3^{-1}\right)L_2.
$$
因 $\mathcal J_{1,2}^*d_+^*=P_K$，有
$$
P\,d_+^*=\mathcal J_{1,2}C_uP_K.
$$
因此对同一个 $f\in L$，令
$$
V=d_+^*(\mathcal C^*+eL_1L_3^{-1})L_2:L\longrightarrow\mathcal H_3,
$$
即得
$$
\boxed{\quad \mathcal J_{1,2}A=PV,\qquad
\mathsf K=V^*PV
=V^*V-(R_2V)^*(R_2R_2^*)^{-1}(R_2V).\quad}
\tag{2.1}
$$
这是整个上来源上的 MP 投影，没有先删去 primitive 分量，也没有交换压缩与逆。

为明确完整交叉项，令 $E=L_3^{-1}$，将 $d_+P d_+^*$ 分别夹在 $\mathcal C,\mathcal C^*$、$\mathcal C,e$、$e^*,\mathcal C^*$、$e^*,e$ 之间并压到同一个 $L$，所得四块记为 $K_{cc},K_{ce},K_{ec},K_{ee}$。于是
$$
\boxed{\quad
\mathsf K=L_2\left(
K_{cc}+K_{ce}L_1E+EL_1K_{ec}+EL_1K_{ee}L_1E
\right)L_2,\qquad K_{ec}=K_{ce}^*.
\quad}
\tag{2.2}
$$
后续精确标量使用全部四块；两个混合项均保留。

## 3. 唯一精确标量参数

置 $z_i=b_i^2$，$S=e_1(z)$、$Z=e_2(z)$、$W=e_3(z)$、$U=e_4(z)$、$V_5=e_5(z)$，并令
$$
\delta=S^2W-4SU+12V_5,\qquad
\epsilon=U^2Z-4SUV_5+12V_5^2.
\tag{3.1}
$$
[伴随矩阵来源推导](../notes/2026-11-28-five-bit-s2-companion-moment-source-8542.md) 把 (2.2) 写在五点求值的 companion 坐标中；对应的[十四条原五变量整数身份](../notes/2026-11-28-five-bit-s2-companion-identity-return-8542.md) 已逐项核实实际物理伴随及完整投影。该相似在互异 $z_i$ 上可逆，不是酉变换；所有实际伴随均单独写出，未使用 companion 矩阵的普通转置。

修正后原源码的首次实际运行 run **46046216601**、job **140666034355** 给出
$$
\boxed{\quad
\operatorname{Tr}_{L}(\mathsf K^2)
=\frac{N(S,Z,W,U,V_5)}
{D(S,Z,W,U,V_5)},\qquad
D=S^2U^4\delta^4\epsilon^6.
\quad}
\tag{3.2}
$$
完整五维零延拓的平方迹恰等于四维 $L$ 上的这个迹；这里没有换用 companion 坐标的 Frobenius 范数。

唯一完整参数保存在[精确输入](../notes/2026-11-28-five-bit-s2-companion-exact-scalar-input-8542.json)：一个 75,666 字节的 JSON，内含原输出的 zlib/base64 数据，原文 208,454 字节，SHA256 为
$$
\texttt{2d7078584c2aea20d9e80f0dda7700f446b6471aeb3e17ef9eb8d237f415f909}.
$$
其中 2,841 条指数记录同时保存 $N,D,D-4N,3D-16N$ 的完整整数系数，变量加权次数为 $(1,2,3,4,5)$，总加权次数均为 98。$N$ 有 2,836 项，$D$ 有 210 项。原输出状态准确为 `EXACT_SCALAR_READY`，没有用 elementary 变量中的系数符号直接宣称正性。

原运行中，实际费用在 0.042708492 秒形成，完整费用检查点在 0.071654778 秒写成；标量在 0.114375519 秒形成，原程序在 0.161813406 秒结束。整个子进程耗时 0.233007961 秒，最大 RSS 为 46,236 KiB，退出码 0。此前 56996cf0 版本的 `fmpz` 序列化失败仍单独保留；本次只修三处 JSON 整数转换，没有改变数学输入或资源上限。

分母在实际正权上严格正。事实上，若 $M_\lambda$ 表示五变量归一对称单项式均值，则
$$
\delta=30M_{(3,1,1,0,0)}
+60M_{(2,2,1,0,0)}
+60M_{(2,1,1,1,0)}
+12M_{(1,1,1,1,1)}>0,
$$
而
$$
\epsilon=V_5^3\delta(z_1^{-1},\ldots,z_5^{-1})>0.
$$
故 (3.2) 的精确有理恒等式由互异正权连续延拓到全部正权，包括任何重复权；最终分母没有 Vandermonde 因子。

## 4. 6,936 个完整正轨道的整数证书

定义
$$
M_\lambda(z)=\frac1{5!}\sum_{\sigma\in S_5}
z_{\sigma(1)}^{\lambda_1}\cdots z_{\sigma(5)}^{\lambda_5},
\qquad \lambda_1\ge\cdots\ge\lambda_5\ge0.
$$
若 $\lambda$ 有 $m_\lambda$ 个不同排列，则
$$
m_\lambda=\frac{5!}{\prod_a(\#\{i:\lambda_i=a\})!}.
$$
每个实际单项式在 $w_\lambda M_\lambda$ 中的系数恰为 $w_\lambda/m_\lambda$。

以下两个身份给出了不依靠浮点的完整变量替换：
$$
S^n=\sum_{\lambda\vdash n,\ \ell(\lambda)\le5}
\frac{n!}{\lambda_1!\cdots\lambda_5!}\,m_\lambda M_\lambda,
\tag{4.1}
$$
$$
M_\lambda e_k
=\sum_{\substack{I\subset\{1,\ldots,5\}\\|I|=k}}
M_{\operatorname{sort}(\lambda+\mathbf1_I)}.
\tag{4.2}
$$
第二式按对称平均直接成立，重复产生的分拆按重数累加。对五个 elementary 变量采用多变量 Horner，并在每一步用 (4.2)，便精确得到原 $z_1,\ldots,z_5$ 多项式。这里没有把 elementary 变量当成相互独立的正变量来处理符号。

[整数证书源码](../notes/2026-11-28-five-bit-s2-quarter-positive-certificate-8542.mjs) 从唯一精确输入执行如下完整检查：

1. 解压原数据，核对原字节数、SHA256 和原数学源码的 SHA256；所有 JSON 整数先保留十进制字符串，再转为 BigInt，绝不经过双精度整数。
2. 核对四列完整系数的原 SHA256、加权次数及逐行恒等式 $G=D-4N$、$H=3D-16N$。
3. 在 elementary 多项式环内乘回 $S^2U^4\delta^4\epsilon^6$，逐项核对完整 $D$。
4. 按 (4.1)–(4.2) 展开同一个 $G=D-4N$，核对所有输出分拆、次数、轨道重数、整数整除、等权质量及全部正系数。

完整证书核心已在纯 V8 BigInt 中实际执行，耗时 3,942 毫秒。结果见[完整回执](../notes/2026-11-28-five-bit-s2-quarter-positive-certificate-8542.json)：

| 项目 | 精确结果 |
|---|---:|
| elementary 完整指数记录 | 2,841 |
| Horner 节点 | 3,719 |
| 非零原变量对称单项式轨道 | 6,936 |
| 负轨道 | 0 |
| 非零原变量单项式 | 658,965 |
| 最小实际单项式系数 | 1 |
| 最小归一均值权 | 120 |
| 等权质量 $G(1,1,1,1,1)$ | 194,522,647,344,910,860,816,000,000 |

按源码规定的分拆字典序将全部轨道及整数均值权序列化，其 SHA256 为
$$
\texttt{e3e56baa555398974263be2c245423a7f355533bdf793093dbd3ac9064d1b43f}.
$$
因此存在完整且全部严格正的整数 $c_\lambda$，使
$$
D(e(z))-4N(e(z))
=\sum_{\lambda}c_\lambda\sum_{\mu\in\operatorname{Orb}(\lambda)}z^\mu>0
\quad(z_i>0).
\tag{4.3}
$$
严格性来自非空正系数和正变量。故 (3.2) 给
$$
\boxed{\operatorname{Tr}_{L}(\mathsf K^2)<\frac14.}
\tag{4.4}
$$
本证书只支付 $D-4N$。保存的 $3D-16N$ 另一列不在本定理的已证范围内。

## 5. 同一个四维低源上的严格 S2

因为 $\mathsf K=A^*G_uA\succeq0$，其物理特征值非负，故
$$
\|\mathsf K\|^2
=\max_j\lambda_j(\mathsf K)^2
\le\sum_j\lambda_j(\mathsf K)^2
=\operatorname{Tr}_L(\mathsf K^2)<\frac14.
$$
所以 $\mathsf K\prec\frac12I_L$。

[四、五位出生一的严格 half 定理](R271-appendix-four-five-sites-birth-one-half-first-last-edges.md) 正是在这里同一个实际 $L$ 上给
$$
L_1L_2^{-1}L_1\prec\frac12I_L.
$$
两项相加即得原 (1.2)，从而五位全部独立正权的 S2 严格成立。此处没有使用五维延拓的单位算子替换四维 $I_L$，也没有以两个不同来源的费用相加。

## 6. 六个独立正权的出生二首边

现在取任意六个正权，将任意一个指定为新位 $a>0$，其余五个作为上述旧系统。令 $t=a^2$。旧上出生为二，旧下出生为一。

三项原假设均已在同一组旧五位权上支付：

- [R298](R298-five-independent-positive-weights-birth-two-hard-top-strengthened-s1.md) 给完整硬端 S1，且其标准化创新费用不超过 $743/782<1$。因上高度为一，$F=C_u^2$，所以 $F-\Delta L_3^{-1}\Delta^*$ 正定。
- 本文 §5 给完整严格 S2。
- 同一个 [half 定理](R271-appendix-four-five-sites-birth-one-half-first-last-edges.md) 的倒数权末边给 $L_2L_3^{-1}L_2\prec\frac12L_1$，特别支付 R275 所需的旧低出生第二边。

因此 [R275 §4 的完整平方分解](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 对每个 $t>0$ 给其真实三块铅笔严格正。原有可逆源同余和完整 Schur 补返回新的九维 primitive 空间
$$
K_2^{(6)}=\ker d^{(6)}\cap\mathcal H_2^{(6)},\qquad \dim K_2^{(6)}=9,
$$
得到
$$
\boxed{\quad
\Gamma_{1,2}^{(6)}
\bigl(\Gamma_{2,2}^{(6)}\bigr)^{-1}
\Gamma_{1,2}^{(6)}
\prec I_{K_2^{(6)}}\qquad
\text{对全部六个独立正权。}\quad}
\tag{6.1}
$$
这里新出生二的合法高度恰为二，(6.1) 是它唯一的非端点相邻边。严格性可直接由严格 S2 的完整正块和 $t>0$ 下的可逆分块同余得到，未依赖数值抽样。

## 7. 精确范围

本结果闭合了五位硬端 S2 及六位出生二完整首边；没有声称任意位数、任意出生的 S1/S2 归纳已闭，也没有将该 primitive 正性转作原边界物理头的完整 Gram。原同 $W$ 的 Green/实际范围来源、primitive 联合费用以及 $N=M$ 仍须另行完成。此前两个 180 秒资源失败及首次 JSON 实现失败均保留，不改变为数学反例或本次成功运行。
