# R179：与第一变量相离的 CM Hecke 框架及共同形式端点

日期：2026-11-13。**状态：已证明并完成实际计算。**

本结果在 R170 的同一实际曲线上另选一张 Abel 图，使第二变量及其二同源像都避开第一变量。两条 CM 类在这张图上的实际 $T_2$ 主函数均已构造；另在 R141 的第二张固定图上构造 $3mD_b,3mD_u,3mD_c$ 的全部正负完整理想。这里不把形式对数相等当作主函数已经求出，也不把这些函数或端点当作完整全局高度。

## 1. 同一曲线与实际支撑条件

取 $X=X_{\rm ns}^+(41)$，$g=54$，$\deg\mathcal L=126$，局部环
$$R_2=(\mathbf Z/47^4)[i]/(i^2+1),\qquad47^4=4879681.$$
所有截面使用 R102/R110 的原 $73,199,325$ 维基。$m=\#J(\mathbf F_{47})$ 为 R121 已准确计算的整数，$m\equiv9\pmod{47}$。第一变量保持 R141 的 family0，记其 54 个固定点的支撑为 $S_0$。

R170 的三条真实二同源分支已经给出全部 820 个源点及目标点的三阶展开。对每个点，将 73 个 weight2 坐标在模47的第一个非零坐标处归一；得到长度146的准确有限域字节向量。比较的是完整归一化坐标，不是可能碰撞的短哈希。

归一化基不是逐项定义于 $\mathbf Q_{47}$ 的基。其 Frobenius 矩阵 $A_1$ 满足
$$W A_1=\overline{W_\tau}.$$
因此目标坐标的实际 Frobenius 是 $\overline{vA_1}$；程序对全部源点和三分支的集合逐项核对这一作用，不能直接把每个坐标取共轭。选点程序的初次检查发现这一基变换需要保留；修正后的完整运行才产生本文证书。

按 Frobenius 二元轨道加入点，同时要求每步典范微分取值秩等于已选点数。选定的54点为

```
114,320,322,358,252,487,199,458,110,730,511,673,149,641,
134,745,80,397,599,612,30,298,469,616,236,369,208,430,
63,651,171,686,132,762,427,722,231,274,79,151,263,791,
174,257,202,731,71,290,556,578,601,732,299,569
```

记其支撑为 $S$。完整检查给
$$|S\cup T_2S|=216,$$
$$\boxed{S\cap S_0=T_2S\cap S_0=S\cap T_2S_0=S\cap T_2S=\varnothing.}\tag{179.1}$$
这里 $T_2S$ 包含全部三条对应分支。该结论是模47上的支撑不交，因而相应剩余盘上的形式移动也不交。54阶典范取值矩阵有单位行列式，证书保存其完整逆并检查双侧乘积。

各目标分支分开解码，取出完整项目坐标后立即释放，最后才截取选定的54行。三条原分支的 SHA、原完整目标文件的 SHA、项链排列、源展开 SHA 都保留。没有重跑 GP，也没有用一个形式对应替代真实二同源。实际峰值83.07 MiB。

## 2. 两个 CM 类与新图的准确框架

记
$$C_u=u-b=P_{-12}-P_{-3},\qquad C_c=c-b=P_{-7}-P_{-3}.$$
R167 已给出 $\log(mC_P)$ 的准确54维向量。R131 的真实 $T_2$ 微分矩阵给
$$\log(T_2mC_P)=\log(mC_P)T_2.$$
将这两个向量分别用 R136/R167 的积分 Abel 逆代入上述新图，得到参数 $t_P,s_P\in47R_2^{54}$。每一步只对单位矩阵求逆，三次截断由已证尾项界足以保留模 $47^4$ 的全部值。

同一个有理截面 $v_S$ 的零除子写成
$$\operatorname{div}_{\mathcal L}(v_S)=S+Z_S,\qquad\deg Z_S=72.$$
程序构造完整的 $H^0(2\mathcal L-Z_S)$，再在54个移动点施加条件，得到完整73维点理想及 Frobenius。真正使用的度零除子框架为
$$A_S(Y)=\sum_{j\in S}P_j(t_j)-\sum_{j\in S}P_j(0).$$
Makdisi 点的完整除子代表额外含 $\operatorname{div}(v_S/f_0)$；这个主函数在与其他代表比较时必须保留。本文没有把它设为一。

新图端点的完整点 SHA 如下。

| 类 | $mC_P$ | $T_2mC_P$ |
|---|---|---|
| $C_u$ | `f9dd4a86272ba8eaab287870424b942443ec5b026a21339165eae3ac3c5c917e` | `97a119f86e1335990262c676d140ad869e1f2430da68c8c5898d93d79752a4c4` |
| $C_c$ | `3d9cc573f482c0dfc4ef5203cf19078c9fdd6530e8d0c4bf23f1e6ce525f7656` | `6c02e43f57f532d2c2b73ad546598f07c6aea320bc57714209746dc0e03bc219` |

## 3. 两个实际 Hecke 主函数

对上述每个 $P$，定义两个实际216次有效除子
$$Z_+=T_2\Bigl(\sum P_j(t_j)\Bigr)+\sum P_j(0),$$
$$Z_-=T_2\Bigl(\sum P_j(0)\Bigr)+\sum P_j(s_j).$$
由 (179.1)，它们的216个剩余支撑各不重复。$H^0(3\mathcal L-Z_\pm)$ 的完整限制矩阵都恰有216阶单位子式，核的秩为109。保存的核及 Frobenius 矩阵满足全部整下降等式。

选 $s_0,g\in H^0(3\mathcal L-Z_-)$，在全部820个忠实评价点解
$$g n=s_0 u,\quad n\in H^0(3\mathcal L-Z_+),\quad u\in H^0(3\mathcal L).\tag{179.2}$$
实际 $820\times434$ 矩阵秩为433；单位核是一条直和线。按 R170 的一维下降及半迹规范，将其生成为 $\mathbf Q_{47}$ 有理的 $(n,u)$。全820个乘法式、两个216点零条件、Frobenius和模47的 $n\equiv s_0$ 都逐项通过。

为何 (179.2) 的函数就是所需主函数，不能只由核秩猜测。实际 Hecke 对应与形式 Abel 同构先给
$$[Z_+-Z_-]=0$$
于形式 Picard 群。于是存在主函数 $k$；把它模47规范为一后，$ks_0$ 和 $kg$ 都是相应的整截面，给 (179.2) 的非零单位核向量。因核为秩一直和，算出的向量与该向量仅差单位标量。由此
$$\boxed{\rho_{T,P}=n/s_0,\qquad
\operatorname{div}\rho_{T,P}=T_2A_S(mC_P)-A_S(T_2mC_P).}\tag{179.3}$$
这里的单位核唯一性与已经知道的实际主性共同给出准确除子；不需要另行假设随机截面的剩余零集互不相交。

所有乘法式是 $6\mathcal L$ 的截面等式，次数756小于820，故全部真实点上的相等给全曲线相等。模 $47^4$ 上逐层使用相同的单位模型，检查亦保留整精度。数值运算采用已归一化的 int64 矩阵，内积长度至多820，界 $2\cdot820(47^4-1)^2<2^{63}$ 排除整数溢出。

## 4. 共同平移的准确形式端点

R162 在八个 Hecke 域中的准确坐标及清挠整数关系给
$$D_b=-\kappa_2,\qquad D_P=(27T_2+4)C_P-\kappa_2$$
在有理点空间中的坐标；乘其明确的47单位整数 $e$ 后是实际 $J(\mathbf Q)$ 中的等式。R178 已独立以真实整数除子和主函数构造 $3D_b$，不能省掉这里的因子3。

将 R162 的坐标先写入八域幂基，再用 R167 已核的 $T_3$ 幂基逆矩阵，得到 $\kappa_2,D_u,D_c$ 的实际对数。程序独立核对原 $C_u,C_c$ 向量与 R167 完全相同，并核对
$$\log D_P=27\log(C_P)T_2+4\log C_P-\log\kappa_2.$$

由于 $m=\#J(\mathbf F_{47})$，每个实际 $mD$ 都在形式群中。该群上 $e$ 可逆且形式对数单射；所以清挠等式足以准确识别 $3mD$，没有忽略未知挠点。随后在 R141 的 family1 中对每个正负对数构造完整点理想，而不是仅输出对数。

| 实际类 | 正点完整 SHA | 负点完整 SHA |
|---|---|---|
| $3mD_b$ | `4e625d66b78c5c547cfe0800924abc9ec47902c3b83e81007006bd9f58715ff9` | `25f380d63edf67c04bd0e28889a756c2b8e6587548f09da46f98abd3ba3bad96` |
| $3mD_u$ | `1d3d65dba586d391a8b94dfe8436d472ccd841344961753f5e36ccacceb4c058` | `4ea64b6ef439dfcbefbf65e8646663030d137f6398382ea86b35ae816b2d3a85` |
| $3mD_c$ | `e5847fa33d341ddbf660df10f666c06b7218f451eca9ad9a2d6adee279e2cd9c` | `71179b383d94a9d316081aac31ff19b87e73fa787837a045c81e778efb73b1f2` |

每项保存199乘73点矩阵、73阶 Frobenius、全部54个参数及单位限制核。负点同时供实际形式纤维的第二变量逆函数使用，无需再做同一形式指数计算。

## 5. 恢复文件与完整边界

全部准确文件名、字节数和源码 SHA 记录在 `notes/2026-11-13-r179-stable-files.json`。主要压缩证书为：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `p41_t2_cm_abel_select47_checkpoint.json.gz` | 27572 | `ec9db4f567c7e1c763f1cb2b95436d7ee1371f281bb732073e45d266c2f6b0aa` |
| `p41_t2_cm_restricted_cubic47_checkpoint.json.gz` | 521050 | `2500d3ab98b59a39f82e816b63e10b8a4c295000bb93d1f40b63818d6859afcd` |
| `p41_t2_cm_abel_base47_checkpoint.json.gz` | 84583 | `0b646549701e60684180427e207e795d8b2533855c697e69a579d7b48e7523e2` |
| `p41_t2_cm12_formal_transport47_checkpoint.json.gz` | 788093 | `8cf96627c7f84688744edf1c920cd4865b00edaf8747aea124a6c6a95f371c84` |
| `p41_t2_cm7_formal_transport47_checkpoint.json.gz` | 788306 | `291caf117d32e1b2f4e1d90d53eee0904ac3528b5e93d87425667ecbdd0552b5` |
| `p41_translation_formal_endpoints47_checkpoint.json.gz` | 812787 | `58d3464c9fad59d6bffae089f96b0085013c95d3a73d6868d126ab45d652d70b` |
| `p41_hecke3_abel_bases_checkpoint.json.gz` | 160316 | `2c0c16acee560af04582de86e345fe3ded57c8c0d5f8c5f56b2631aaf00e3a8d` |

最后一项是原 R141 的完整两张 Abel 基，现直接保存；其字节 SHA 与 R145、R167 各自独立记录的输入相同。它只补恢复依赖，不更改旧图。

从课题目录运行 `scripts/p41_t2_cm_abel_select47.py --script-dir scripts` 可重建新选点及紧凑展开；`scripts/p41_t2_cm_formal_transport47.py --script-dir scripts --class-name x12 --output /tmp/r179-cm12-replay.json.gz` 和相应 `x7` 给两条主函数。前者默认使用新的 `/tmp/p41_t2_cm_*` 输入；可用 `--selection`、`--restricted`、`--base` 指定已保存的仓库文件或独立重放路径。共同端点用

```
python -B scripts/p41_translation_formal_endpoints47.py --script-dir scripts --bases scripts/data/p41_hecke3_abel_bases_checkpoint.json.gz --output /tmp/r179-common-endpoints-replay.json.gz
```

重建。各驱动保留所有输入摘要，并使用已发表在仓库中的真实数据；没有依赖新的未保存 GP 输出。

本结果补齐 R178 式(8.1)所需的两个 $\rho_T$ 和三组最终形式点。后续仍须计算 CM 及共同长链的完整函数范数、真实终点换框、形式短组合函数 $F_\Sigma$ 和实际形式纤维。支撑不交保证最终函数取值有定义，但不保证每个中间 Miller 截面都是单位；若出现非单位，必须用 R159/R160 的整盘消去，不能直接除47。54个全局高度差与全部 QC 盘亦仍未完成。

## 来源

- [R131](R131-actual-hecke-actions-on-the-level41-model-at47.md)：真实 Hecke 微分矩阵；具体源文件也由证书 SHA 绑定。
- [R136](R136-actual-formal-exponential-and-disjoint-abel-charts-at47.md)、[R167](R167-integral-hecke-contraction-and-actual-cm-formal-endpoints.md)：整 Abel 逆、尾项界及两个 CM 的实际对数。
- [R170](R170-actual-t2-formal-divisor-transport-at47.md)：三条真实目标展开、主函数关系矩阵及完整主性证明。
- [R162](R162-small-hecke-cm-relations-and-torsion-free-transport.md)、[R178](R178-actual-common-translation-divisor-and-initial-transport.md)：清挠坐标、真实 $3D_b$ 及完整双变量规范。
