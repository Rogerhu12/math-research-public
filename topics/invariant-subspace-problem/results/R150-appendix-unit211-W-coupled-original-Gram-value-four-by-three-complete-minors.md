# R150：全余 W 上原 Gram／值方程的四行三列耦合与四个完整参数余子式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。范围严格为已经登记的原一般 LS、Delta=0、W=0 余图及其既有物理、权单位局部化。本结果没有排空整个 W。

## 1. 已有原输入与本结论

沿用以下已发表原理想来源：

- [全 W 首一 T 三次、F 二次与六列环境](R150-appendix-unit211-W-global-monic-T-three-F-two-and-six-column-environment.md)；
- [十三条完整原行的六列返回](R150-appendix-unit211-W-global-monic-three-two-thirteen-original-rows-six-columns.md)；
- [纯 T 三列原参数余子式](R150-appendix-unit211-W-global-pure-T-three-original-parameter-cofactors.md)；
- [原 U 值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)。

记权参数为 e,k，原值参数为 lambda，F=2f-u lambda、S=T-2lambda。已有首一规则为

$$
q_F=F^2+p(S)F+q(S),\qquad q_3(S)=S^3+\beta_2S^2+\beta_1S+\beta_0.
$$

所有系数均在上述已付单位局部化的 QQ[e,k,lambda] 中。q_F 来自原均值的已付线性组合，q_3 来自原两个四次值方程及已经完整关闭的 lambda=3/2 纤维。保留原四次 q_4 的完整余式

$$
r_2=q_4\bmod q_3.
$$

这里不倒置 r_2 的二次首项。当前原 U 图明确规定 lambda=m/U_0 非零，因此 lambda 可作为已付因子；这来自原定义而不是本次计算的数值推断。

本次以原 E1、EBe、N1 三行消去 F，与 r_2 耦合，获得四个对每个原解都为零的参数多项式，lambda 次数分别为 12、12、9、11。所有四个 lambda 首项仍有未付余因子；本结果不将它们首一化。

## 2. 三条原行与无首项除法的消元

先将三条原式按 q_F、q_3 做有序首一约化。程序逐式实际核回

$$
E_i=\overline E_i+U_iq_F+V_iq_3.
$$

约化只产生真实六列 (1,S,S^2,F,FS,FS^2) 中的系数。对这三条特定原式，实际返回进一步满足 F 部分至多对 S 一次。清除系数的已付分母，并且只从公共内容中剥去已付因子，得到

$$
R_i=A_i(S)+B_i(S)F,\qquad
\deg_S A_i\le2,\quad\deg_S B_i\le1,\qquad i=0,1,2,
$$

依次对应 E1、EBe、N1。每个原系数均乘回清分母与剥内容前的表达式。清理并未剥去公共内容中任何未付因子，故 R_i 与相应原余式在当前域上的零点完全相同。

定义三条精确原组合

$$
H_{ij}=B_jR_i-B_iR_j=A_iB_j-A_jB_i,\qquad 0\le i<j\le2.
$$

右端无 F，对 S 次数至多三。实际源码逐项核对等号两侧，再以首一 q_3 约化至 S 二次，保留完整约化迹；没有使用任何 B_i 的逆。因而所有 B_i=0、两个 B_i 同时为零以及三个全零的纤维都仍在本次必要覆盖中。

## 3. 固定四行三列与原常数余子式

令 [g] 表示按 q_3 约化后，在 (1,S,S^2) 中的系数行，并仅做上一节同样的合法清理。取固定矩阵

$$
\mathcal M=
\begin{pmatrix}
[r_2]\\
[S r_2]\\
[H_{01}]\\
[H_{02}]
\end{pmatrix}.
$$

[S r_2] 使用真实首一 q_3 乘法。每个原解有同一个 S，故

$$
\mathcal M(1,S,S^2)^{\mathsf T}=0.
$$

第一坐标恒为 1，不要求这三列在最终原方程商中线性无关。

对任一选定三行 a,b,c，令

$$
\gamma=(b_1c_2-b_2c_1,\ a_2c_1-a_1c_2,\ a_1b_2-a_2b_1).
$$

按列编号 0,1,2，完整乘回给出

$$
\gamma^{\mathsf T}
\begin{pmatrix}a\\b\\c\end{pmatrix}
=(D,0,0),\qquad D=\det(a,b,c).
$$

因此 D 在每个原解处为零。此次实际处理四行矩阵的全部四个三行选择，每个证书的三个列恒等式均以完整 QQ[e,k,lambda] 多项式核回。

原 D 中只剥已付因子和非零有理常数，所得 C 仍是全当前域必要式。整个剥除过程逐因子核对乘回；没有使用多变量 gcd 为 1 判断空性。

| 三行选择 | 原 D 次数 (e,k,lambda) | 剩余 C 次数 (e,k,lambda) | C 项数 | C 总次数 |
|---|---:|---:|---:|---:|
| r2, S r2, H01 | (48,60,15) | (35,43,12) | 14989 | 74 |
| r2, S r2, H02 | (49,62,15) | (36,45,12) | 15957 | 77 |
| r2, H01, H02 | (44,60,11) | (35,45,9) | 11666 | 72 |
| S r2, H01, H02 | (50,67,13) | (41,52,11) | 18960 | 85 |

四条 C 的完整规范系数 SHA256 依次为：

- ce2cc60a32937e22f4ded160a75c6d59010181a931f147ae38152effa5c3d0b9；
- 3fcb6afe7a2de1bdd0c71bfba2ede43fdf69c5c185d18b01cf63714fcaefce79；
- f67755b11337d9dd303575f0deef8d42a6d55485b4d987c1c399861e149117c6；
- 79553f094557960ea4256c1e81562d5d7dfb8d949d9205b26ef9cfacfa9686e0。

这些大而可重算的系数不存缓存。固定源码、全部原式定义、参数、系数长度与 SHA 可再生它们。

## 4. 全部尚未支付的首项面

每条 C 对 lambda 的首项再剥去已付权因子后，余式仍非恒定：

| 选择次序 | 未付首项次数 (e,k) | 项数 | SHA256 |
|---|---:|---:|---|
| 第一条 | (26,33) | 665 | 4da2e0e21e970921f677c8e78ca8516b64ee3916987267f067f9ab23d5b36a16 |
| 第二条 | (28,37) | 794 | 78b4319d37bd91741bb0b9b9e39cc9fe1e20fe8eb536d677cd5113a4c3f92705 |
| 第三条 | (25,32) | 621 | d1e1f5ea663143508a6a8d087a703eaac47a05d767522e36ab5c5669ea359bd2 |
| 第四条 | (28,34) | 729 | c898dcc0508bd56bf1085c98d8ce6a965fa9061cd0e6428fb07bf8c27958262f |

全部这些整零面仍保留。也没有倒置 A143、B239、r_2 首项、任一 B_i、物理 D 或任何范数。本结果既不证明四曲线交集有限，也不证明任何原解不存在；完整个别 N/P 和 N4(V) 仍须返回。

## 5. 唯一实际执行与精确再生边界

源码：

[2026-11-27-unit211-W-coupled-original-Gram-value-four-by-three-minors-8542.py](../notes/2026-11-27-unit211-W-coupled-original-Gram-value-four-by-three-minors-8542.py)

SHA256 f5c0226e4dfc8d0f80da5358d3b4a3718e2ad9c834555a2335f1e58162bb0b41；5834 字节。固定依赖为已经登记的 50564e... 纯 T 构造，后者继续固定 394bb2...、af928...、00c08... 的原式构造前缀。源码止于这些旧源的构造段，不重放先前的十三行大门或任何旧完整 cofactor 门。

Actions run 46031519936，job 140616263057；真实 inner exit=0：

- 原构造、三个 H 全部迹和四个完整 cofactor：3.956601753 秒；
- 驱动墙钟：3.992801873 秒；
- 峰值 RSS：91328 KiB；
- stdout：11430 字节，SHA256 fef8b334b4b6645e0e82b4a9bcb3197169f6464fa3a34e400e5a464dc2946319；
- 限额：180 秒、4 GiB；
- 四个常数余子式证书大小依次 888576、940813、542755、918143 字节，SHA 均在小回执中。完整证书在实际运行中逐列返回，没有将这些可重算数据写入仓库。

真实 pull 时间为 2026-11-27 16:12:04.555253 UTC，前后 main 均为 4bcf0ccd2d663f0b1aec4f264efd48959106e875；两 README blob 未变。完整驱动回执及数学输出保存在同 stem 的 receipt JSON 中。此结论只使用上述实际成功身份，不把 workflow 绿灯本身作为数学证据。
