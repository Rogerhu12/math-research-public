# R118：静态 G 的原有理分离与真实第四成本商非零

日期：2026-11-14。**已证明。** 唯一新增研究计算在公开仓库 GitHub Actions run **43647225907**、源提交 **b466c3782ae5e3b1a68572065b7505d45e6d8a99** 中执行。本文消费该回执，不重编此前的 forcing、W、局部密度或 word 正规形。

主要结论是

$$
G\notin\mathcal R_8,\qquad
\dim\mathcal R_{8,+1}=7,\qquad
\mathcal U_4/\mathcal R_8\ne0.
\tag{1}
$$

结合 R116 的真实 pure 尾投影秩 $31$，还有

$$
\boxed{\dim\mathcal U_4\ge\dim\mathcal R_8+1\ge32.}
\tag{2}
$$

[R117](R117-static-weight-one-reduction-and-reciprocal-costs.md) 的非零前提现已支付：一个新的权一第四成本查询可以在保留完整真实连接基准的条件下取任意实值。这不等于完整第四成本可控，也不证明该查询能与先前的 $31$ 个尾查询在同一设计中任意联调。

## 1. 固定原式与已经证明的上界

使用 [R109](R109-local-density-of-the-complete-fourth-quotient.md) 的完整两个相位、同一右锚及 [R115](R115-static-local-fourth-top-weight-payment-and-unresolved-next-block.md) 的已公开局部势代表。其静态 profile 权一块为

$$
(\mathscr L_4^{[0]})_{+1}
=hk\,F+hk^3\,G+h^2k^2\omega\,H,\qquad H\in\mathcal R_8.
\tag{3}
$$

势代表的预先化简只改变几何系数乘 $\mathcal R_8$；这不改变本文的商结论。$G$ 由完整导出中几何键 $(1,3,0,0,0,0,0,0)$ 的原根作真实 profile 权一投影得到。两个模式的原式 SHA256 为：

| 模式 | 原式 SHA256 |
|---|---|
| $-4$ | 4608912701e99a514cff0dcb93b896200beeb6e3cbead9a70547b78e00d18c7a |
| $-2$ | 042fc6bef63ef5e1c49b1403c88e4f3d728b9bcce183741a298b2fb2619bcd50 |

$\mathcal R_8=\operatorname{span}\{\mathcal B_P(T):P\in E_8,T\in W\}$ 是真实完整两相位响应空间。R115 的权一块已穷举全部八个原列，并从原式证明

$$
C_6=-C_1+C_3.
\tag{4}
$$

七个保留列如下。$W_j$ 的下标是同一已发表 $36$ 元真实三线性基的下标；最后一栏追溯至原 $152$ 个模板。

| 原列号 | 二阶算子 | 三阶算子 | 原 152 模板号 |
|---:|---|---:|---:|
| 0 | $p_1$ | $W_7$ | 7 |
| 1 | $p_1$ | $W_{17}$ | 17 |
| 2 | $p_2$ | $W_1$ | 1 |
| 3 | $p_2$ | $W_{12}$ | 12 |
| 4 | $p_2$ | $W_{16}$ | 16 |
| 5 | $p_2$ | $W_{35}$ | 109 |
| 7 | $t_1$ | $W_{17}$ | 17 |

被省略的原列 $6$ 是 $\mathcal B_{t_1}(W_7)$。因此，在本次评价以前已有准确上界

$$
\dim\mathcal R_{8,+1}\le7.
\tag{5}
$$

这个上界来自已核的原式关系与完整权分解；没有从模素数秩下降推断有理秩上界。

## 2. 同一个有理 profile 对、同一右原函数

本次原式评价固定 $\xi\in[2,3]$，$t=\xi-2$，取

$$
f(t)=t^8(1-t)^8,\qquad
g(t)=f(t)(1+2t+3t^2+5t^3),\qquad
q=f+ig.
\tag{6}
$$

区间外零延拓是 $C^7$。原根及响应所需 profile jet 不超过六阶，接口在进入研究评价前对此作了明确检查；所以它也足以反证在全部光滑紧支撑 profile 上成立的通用身份。若那样的身份对所有 $C^\infty$ profile 成立，按 $C^6$ 连续性就会在 (6) 上成立。

所有列、目标和两个模式使用同一个 $(f,g)$。每个 Volterra 节点保留真实共同右锚，符号原函数是

$$
Iu(\xi)=\int_3^\xi u(\eta)\,d\eta.
$$

普通复平方始终是普通双线性平方，没有改成模平方；外槽和两个对称内槽的身份也没有混淆。没有用 word 代表评价函数。

选 $24$ 个点 $t=j/25$，在两个模式各取实、虚部，共 $96$ 行。每一个数原本都是明确的有理数，因为 profile、查询点和原始右积分均有理。程序在素数

$$
p=2147483647\equiv3\pmod4
\tag{7}
$$

下执行这些有理运算；它先验证素性，逐次拒绝分母模 $p$ 为零，并保 $i^2=-1$ 的域运算。实际完整成功回执意味着这些检查全部通过。全部有理分母检查信息保存在完整报告，不以未经验证的浮点值代替。

## 3. 真有理 $7/8$ 分离子式

令 $A$ 为七个保留原列在 $96$ 行上的有理评价矩阵，$b$ 为原式 $G$ 的评价列。选中的七个控制行是

$$
J=(0,2,3,6,7,10,11),
$$

额外行是 $r=14$。这些行对应：

| 次序 | 原行号 | $\xi$ | 模式 | 分量 |
|---:|---:|---:|---:|---|
| 1 | 0 | $51/25$ | $-4$ | 实部 |
| 2 | 2 | $51/25$ | $-2$ | 实部 |
| 3 | 3 | $51/25$ | $-2$ | 虚部 |
| 4 | 6 | $52/25$ | $-2$ | 实部 |
| 5 | 7 | $52/25$ | $-2$ | 虚部 |
| 6 | 10 | $53/25$ | $-2$ | 实部 |
| 7 | 11 | $53/25$ | $-2$ | 虚部 |
| 8 | 14 | $54/25$ | $-2$ | 实部 |

实际精确模结果为

$$
\begin{aligned}
\det A_J&\equiv1896063777\ne0,\\
\det\begin{pmatrix}A_J&b_J\\ A_r&b_r\end{pmatrix}
&\equiv2093208697\ne0
\pmod p.
\end{aligned}\tag{8}
$$

原始 $8\times8$ 模矩阵也完整保存在小主报告的
checkpoint.dual_certificate.modular_augmented_matrix 中。式 (8) 证明相应特征零有理行列式非零，因而证明七控制列真实独立，并且 $G$ 不在它们的实线性张成中。实系数也不例外：第一组七行已强迫唯一系数 $A_J^{-1}b_J\in\mathbb Q^7$，额外一行否定这组系数。

准确的有理泛函定义为

$$
\boxed{
\Lambda_1(X)=\operatorname{ev}_r(X)
-A_rA_J^{-1}\operatorname{ev}_J(X).
}
\tag{9}
$$

这里 $A_J,A_r$ 指原有理矩阵，绝非打印出的模系数。按定义

$$
\Lambda_1(C_j)=0\quad(j=0,1,2,3,4,5,7),
\qquad \Lambda_1(G)\ne0.
\tag{10}
$$

其模 $p$ 核验值为

$$
\Lambda_1(G)\equiv772720911\ne0.
\tag{11}
$$

控制列的七个泛函值全部是 $0$。式 (8) 与 (11) 满足

$$
1896063777\cdot772720911
\equiv2093208697\pmod p.
$$

这只是准确有理泛函的一个可复查约化，不赋予它实数正负号。

结合 (4)–(5)，得到

$$
\boxed{
\dim\mathcal R_{8,+1}=7,\qquad
G\notin\mathcal R_{8,+1}.
}
\tag{12}
$$

[R94](R94-scaling-blocks-for-total-P1-membership.md)、R105 和 R117 所用的真实整权分解是有限维实函数空间中的直和分解。因为 $G$ 为纯权一，若 $G\in\mathcal R_8$，投影到权一就会与 (12) 矛盾。因此 (1) 的第一条成立。这里排除的是通用算子身份；没有把同一个测试对上其他权的偶然相消也排除。

## 4. 真实第四成本商由此确实非零

由 [R114](R114-constrained-static-costs-and-real-zero-matrix-words.md) 和 R117，准确归一化静态门为

$$
[\mathcal P(\mathscr L_4^{[0]})_{+1}]
=h(k^3-k)[G]\quad\bmod\mathcal R_8.
\tag{13}
$$

本次已证 $[G]\ne0$，所以所有正时长常态矩阵配平成本不可能全落在 $\mathcal R_8$。

这里还有更具体的真实原料：固定 $h,d$，一个 $k=2$ 完整圈和两个 $k=-1/2$ 完整圈，准确保 frame 恒等且矩阵总和为零。它的静态权一成本为

$$
\frac{15}{2}h\tau(2)[G],\qquad
\tau(2)=\frac{2\pi}{\sqrt5}.
\tag{14}
$$

用 R70 的真实零矩桥连接，固定全部有限桥族，将两 bulk 圈数同时乘整数 $N$。R109 在商中保所有真实连接为 $O(1)$，没有删除原成本中的二、三次历史项。充分大有限 $N$ 已使权一商非零。再接真倒行后 $M=T=0$，第四成本加倍。

故真实成本空间确有

$$
\mathcal R_8\subsetneqq\mathcal U_4.
\tag{15}
$$

这是对“$\mathcal U_4=\mathcal R_8$”的准确否定。R116 已给 $\mathcal R_8$ 的真实 pure 尾评价投影秩 $31$，所以 $\dim\mathcal R_8\ge31$，再由 (15) 得 (2)。本文不据此断言 $\dim\mathcal U_4=32$ 或 $\dim\mathcal R_8=31$。

## 5. 新增一个可单独支付的权一查询

令 $\Pi_1$ 为真实函数空间的权一投影，取

$$
\lambda=\Lambda_1\circ\Pi_1.
$$

把它限制或延拓到 R105 的有限真实成本空间，则

$$
\lambda(\mathcal R_8)=0,\qquad \lambda(G)\ne0.
$$

严格说 (9) 的固定多项式对只分离权一块；$\Pi_1$ 负责其他权，不假装同一组未经投影的八行会消灭全部 $\mathcal R_8$。

R117 第 4 节的真实紧控制族现在适用。正互反对的 $h$ 在 $h_0$ 两侧变化，负互反对固定 $h_0$；每条连接真实保零矩，接倒行付零第三历史。对 $\kappa=15\tau(2)/2>0$，

$$
\lambda(V_N(h))
=2N\kappa(h-h_0)\lambda(G)+E(h).
\tag{16}
$$

$E(h)$ 是未删去的所有真实连接与校 frame 的完整基准，连续、有界，且独立于外 bulk 圈数 $N$。先固定有限紧控制族和共同物理区间，再选任意给定目标 $y$；充分大有限 $N$ 使区间两端位于 $y$ 两侧，介值定理给 $\lambda(V_N(h))=y$。

若要在同一合法 $C^\infty$ 三矩圆上表示这个查询，使用 [R96](R96-single-profile-faithfulness-for-affine-Volterra-spaces.md) 对相关有限真实函数空间的忠实表示，并遵守“控制族、共同物理区间、合法圆、查询、有限 $N$”的选择顺序。当前有理测试对 (6) 本身没有被称为三矩圆。

这证明单个新增标量可取任意实值。它**不**证明能与 R116 的 $31$ 个投影查询同设计任意联调：未取商的原第四成本仍可含 $N^2,N^3$ 的 $\mathcal R_8$ 历史；再插 R102 控制词也带有完整基准成本。不能把两个分别可控的结论直接合成更高维满射。

## 6. 运行、来源与持久化

新增脚本是 [literature_static_G_rational_dual.py](../scripts/literature_static_G_rational_dual.py)，16444 字节，SHA256：

0872f0fc8b561a547342d530239e35c6ac9a37a5bddc5c472bf16c0df73ac477。

本次先 py_compile，再公开运行人工接口检查，再执行原式评价。人工检查耗时 0.031700371 秒，全部通过；包含原右锚符号、普通复平方、外槽/内槽、完整两个相位公式及受约束输入/小报告持久化。研究评价耗时 **6.593979373 秒**、峰值 RSS **123.9140625 MiB**，completion=complete。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| [小主报告](../notes/actions-43647225907-1-static_g_rational_dual/static-G-rational-dual.json) | 13817 | 743594e95eedda896410cc20a30949675899e075bacc262fa5192388dbeba7f9 |
| [人工检查报告](../notes/actions-43647225907-1-static_g_rational_dual/static-G-development.json) | 7467 | 39e75105d2f6d9e04133af8522f11baa55a0f4b1d4cb5452b63eb841849aadbb |
| [完整报告 gzip](../notes/actions-43647225907-1-static_g_rational_dual/static-G-rational-dual-complete-report.json.gz) | 8381 | 40bf4fe4b3b60475122175c9f91de79332b10287232830a2ab4805ca28d68c64 |
| [终端发布回执](../notes/actions-43647225907-1-static_g_rational_dual/receipt.json) | 32065 | 6392f3554aa656c4ab7cadc11c56ed2e4ee5d8a250b857a7d9a1014e8be0e4cc |

完整报告未压缩为 38711 字节，SHA256 为
8a3b72218851c6c0ca713e6d19fcc27ff3e8cc877d0143a87f9186e2a13d4003。
它由 Actions 终端直接写入并发布；本次分析没有通过 API 读取 gzip 或分片大型数据。小主报告已保留全部决定性的分离矩阵、行标签、行列式及 Cramer 定义。

输入继续绑定 run 43645177423 的完整原导出及真实 publisher 回执。原 $152\to36$ 模板关系和权一 $8\to7$ 原式关系只消费已经发布的准确证书，没有重新运行旧编译。此次没有计算尚未支付的其他局部几何导数权。

## 7. 已完成与仍未完成

已完成的是：准确证明通用 $G$ 非成员、完整权一响应真实维数七、真实第四成本商非零、$\dim\mathcal U_4\ge32$，以及激活 R117 的单个新增成本查询控制。

这些结论不排除特殊合法圆上的相消，不给完整第四成本的有符号可达性，不支付第四 ruling、所有更高阶条件或级数收敛。没有得到闭嵌入曲面、定量 reach、宏观位移或连续有限等距族。下一步应处理真正的商方向及其同时控制，而不是继续把已证非成员的 $G$ 放回同七维响应重复拟合。
