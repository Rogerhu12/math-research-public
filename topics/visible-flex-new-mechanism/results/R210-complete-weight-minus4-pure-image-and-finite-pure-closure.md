# R210：完整权 −4 pure 像等于九维响应像，及真实闭 hook 的全 pure 消去

日期：2026-11-15。作者及推导责任：tail_cost；root 阅读原源码、公开实际和本文后登记。**本稿包含已经完成的公开精确原式计算，以及由既有真实控制定理推出的有限路径结论。** 不是阶段性的矩阵观察；同时没有宣称 mixed period、第四 ruling 或原课题的完整有限等距族已经完成。

主要来源：[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R139](R139-fifth-G-translation-separation-and-188-query-control.md)、[R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)、[R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md)、[R179](R179-universal-independence-of-fixed-color-remainder-words.md)、[R190](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md)、[R202](R202-pure-cost-cone-and-three-remaining-negative-character-weights.md)、[R203](R203-general-pure-lowest-two-weights-vanish.md)、[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md)、[R207](R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md)。

实现与全部输入/参数见[本次完整设计](../notes/complete-pure-minus4-projection-design-20261115.md)及 [consumer](../scripts/literature_complete_pure_minus4_projection.py)。公开实际为 [run 43688302217](https://github.com/Rogerhu12/math-research-public/actions/runs/43688302217)，数学输出在 [job 132733352458](https://github.com/Rogerhu12/math-research-public/actions/runs/43688302217/job/132733352458)；[receipt](../notes/actions-43688302217-1-complete_pure_minus4_projection/receipt.json) 只保存来源与 SHA，不保存可重算 payload。

## 1. 完整新结论

固定 canonical 规则、同一右锚、真实 scalar/frame 端口。令 $U=\mathcal U_4$、$R=\mathcal R_8$，$\pi V=V_{-4}$ 表示完整 universal pure 相位系数。以下空间下标 $-4$ 则是 profile 真缩放权，两种标签不混同。

**定理 A。**

$$
\boxed{
\pi(U_{-4})=\pi(R_{-4}),\qquad
\dim\pi(U_{-4})=\dim\pi(R_{-4})=9.
}
\tag{1}
$$

计算覆盖全部十四族的 **152** 条原状态系数；字面比例合并后是 **123** 个不同原呈示，再加 R139 的 **40** 个已存完整响应 pure 原根。新共同矩阵共有 163 列，真实秩为 9；**154 条原函数依赖全部准确为零**。

这里 123 不是函数维数，也不是非零函数个数：归一原列 33、122 是 terms 非空而真实函数为零的两个原呈示。40 是旧完整两 mode 响应块的真实维数，不曾假定其 pure 投影独立；本次确切给出 pure 秩 9。

**定理 B。** 对 R202 的完整 pure 成本空间及实际零矩零第三半群，记

$$
P=\pi U,\qquad
S=\{\pi V_C:C\text{ 有限真实，同 scalar/frame， }M_C=T_C=0\},
\qquad C_{\rm p}=\overline{\operatorname{cone}(S)}.
\tag{2}
$$

则

$$
\boxed{C_{\rm p}=P,\qquad S=P.}
\tag{3}
$$

第一等号由最后可能的 pure 正字符权消失得到；第二等号使用 R206 已证明的真实有限控制机制，不能仅从闭锥或线性 span 猜出。

**定理 C。** R180/R183 的闭 hook 几何可以真实地选择为

$$
M=0,\qquad T=\kappa\mathfrak H\ne0,\qquad
F_{\rm end}=F_{\rm start},\quad
\alpha_{\rm end}=\alpha_{\rm start},\qquad
\boxed{\pi V=0\text{ 对全部共同右锚 profiles}.}
\tag{4}
$$

完整基准、frame 桥成本和新增控制的真实位移均支付。因而 R198 的最右单 profile period 必要门可以整函数归零，而不止一个查询归零。第 7 节给准确拼接，保留非零第三 hook，未将它倒行消掉。

## 2. 本次实际的来源、规模与规则

| 项目 | 公开准确值 |
|---|---|
| source commit | 1b032593b46210e7a0599a224d5c2110fe1d1606 |
| run / job | 43688302217 / 132733352458 |
| lane | complete_pure_minus4_projection |
| source | 43687 bytes；be5d2ffa861968dddd9db085cfef0ecc06d9c96a6f1ca719905e8544458bc946 |
| 真实数学用时 | 4.263189255000043 秒 |
| peak RSS | 317.54296875 MiB |
| 新 pure 收缩 | 127 / 127 |
| 精确整数操作 | 6994 |
| 实际最大整数位数 | 21 |
| 新人工 | 4 项全过，0.002819264999970983 秒，29.20703125 MiB |
| 实际摘要 | 53292 bytes；aeea36d3c46f934ec784460367813ef7902f85f1c3492e575152fd6906e7a76a |
| 新人工摘要 | 8134 bytes；6ac6f37307eb0c996506616f9f748f0ea863b031db4052e029ab104801bdd050 |
| 内存完整证明 | 274008 bytes；0b952fc5dbc65dc3ed5d2e5e0e961b393146e27abecf747777b499c5715b7278 |
| 已发布 receipt | 47378 bytes；f739e4a0ccdcf5ea102a9deb5794486b8f9f022975764e23fd14b16ec6d722c4 |

实际 completion 为 complete，phase 为 complete_pure_minus4_image_decided；163/163 列均完成。公开实际前的四项人工只检查新缓存分区、可变响应块的全矩阵成员/非成员接口和本权参考减项，没有加载研究输入、没有重旧权 $-6$ 的九项人工。

发布者实际 pull 从 source 前进到 10e7e508fe2638c58f117ae1e00f09e01120010c，根与课题 README 无差。根 README §15 已执行：内存证明不写文件，原结果/开发 output 只在 runner 临时存在；repo、Release、artifact 都没有新增可重算 payload。所有 123 条新列的准确坐标及完整别名、全部 40 原响应的坐标直接保留在公开 job stdout。本文记录数学结论与少量可直接核对的身份，不把 SHA 本身当数学证明。

预算是 240 秒、1024 MiB、8192-bit、150000 terms、600000 IBP 调用、300000 cache entries、95000-byte 临时摘要和 8000000-byte 内存证明；实际没有触及资源退出。完整 CLI 位于设计 §10，28 个实际参数与公开 request 一致。

## 3. 完整输入与真正新增工作的边界

### 3.1 全十四族而非单列

R130/R163 的真实生成定理给

$$
U=R+\operatorname{span}\left\{
F_0,\ Q_{2,0},Q_{2,1},Q_{2,2},\
\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2,\
Q_{4,0},\ldots,Q_{4,4}
\text{ 的全部状态系数值}\right\}.
\tag{5}
$$

本次准确的非空原状态记录数为：

| 族 | 原状态系数数目 |
|---|---:|
| $F_0$ | 47 |
| $Q_{2,0}$ | 12 |
| $Q_{2,1}$ | 19 |
| $Q_{2,2}$ | 23 |
| $\bar A_{hh}$ | 9 |
| $\bar A_{hk}$ | 6 |
| $\bar A_{kk}$ | 4 |
| $H_1$ | 6 |
| $H_2$ | 4 |
| $Q_{4,0}$ | 1 |
| $Q_{4,1}$ | 2 |
| $Q_{4,2}$ | 4 |
| $Q_{4,3}$ | 6 |
| $Q_{4,4}$ | 9 |
| 合计 | 152 |

这些是实际原呈示清单，不表示状态系数可以独立实际控制。

旧五份输入为完整 derivative factors（43651096112）、完整静态原密度（43645177423）、完整 A/H 原导出（43654534244）、已存权 $-2$ 输入缓存（43665345551）及 R139 完整 $R_{-4}$ 原响应（43654534244）。原 run/source、main/receipt、packed/raw SHA、原根 SHA 与完整覆盖语义均由冻结输入接口绑定。

### 3.2 44 个已存请求、70 个必要恢复

负权缩放选择后的势请求有 49 个 $N^{[0]}$、65 个 $N^{[2]}$，共 114。旧完整缓存已覆盖其中 44 个：35 个非空 typed 根准确复用，9 个准确空投影沿原完整请求身份使用。

余下 70 个 pure 对角输入曾在 R207 runner 中临时构造，但依根 §15 未保存。本次从相同旧原根恢复这 70 个必要中间依赖；不重跑权 $-6$ 的收缩、十四族、矩阵或目标。不存在把“未存”或“不在请求中”当成零的操作。

新原投影另包含 197 个完整静态 pure 根、62 个 $v_2$ 根、78 个 $v_4$ 的 $\beta/C/Q$ 根。29 个 A/H 已存正规根和 40 个已存响应 pure 根直接消费，不重新构造旧两 mode 响应、旧 profile 评价、旧依赖或旧 forcing/W。

按八参数权及原 $m_0,m_2$ 支撑，新的 pure 收缩上界为 164；去掉准确零对角输入并按原 SHA 合并后，真实新计划为 127 个，并全部完成。它们的输出真权均为 $-4$，不是复算 R207 的权 $-6$ 输出。

### 3.3 不丢静态参考、低阶矩修正或动态端势

R190 的负权常势 cocycle 给，本次所需的 $\sigma=-1,\ldots,-5$ 中，

$$
[\Pi_\sigma N^{[0]}(S)]
=\sum_{\substack{\kappa(a)=\sigma\\a_7=0}}
\bigl(M_a(S)-M_a(S_*)\bigr)
[\Pi_\sigma N_a^{[0]}],
\qquad S_*=(1,1,1).
\tag{6}
$$

所有选中零 log 单项在 $S_*$ 为 1，程序逐项保参考减项。四个非恒 $k^2\omega^j\log h$，$j=1,\ldots,4$，仅在模 $W$ 的势代表中消去，不宣原根字面零；裸 $\log h$ 的零权常势例外未被使用。

局部原式始终是

$$
L_2=v_2-\mathcal B_{m_0}N^{[2]}-\mathcal B_{m_2}N^{[0]},
\qquad L_4=v_4-\mathcal B_{m_2}N^{[2]}.
\tag{7}
$$

沿真实 $D_s\omega=k_s/(2h)$ 作 R129 水平 IBP，保全部系数导数、面积项与四次速度项。使用同八参考态定义同一个 $\Gamma$，同时减

$$
F_0=L_0-\Gamma m_0,\qquad
Q_2=\operatorname{IBP}(L_2)-\Gamma m_2.
\tag{8}
$$

八个 $F_0(S_i^*)$ 逐原式检查为零。改变势代表造成的差只属 $R$，因此完整 (5) 的像未改变。全工作未以任何 profile jet 上界裁剪原词；R208/R209 的独立纸面结果不是本次矩阵结论的假定过滤。

## 4. 九个原响应基与可核对的身份

完整矩阵先放 R139 的 40 个原响应 pure 根，随后放 123 个新归一原呈示。实际真独立的 global 列为

$$
\mathcal I=(0,1,2,3,8,9,12,14,16).
\tag{9}
$$

记相应 pure 原函数为 $\rho_j$，$j\in\mathcal I$。下表给准确旧原下标与算子标签；$W_i$ 沿原 v2 三阶模板编号，不重编号。

| 本次 global $j$ | R139 原列 | $\rho_j$ |
|---:|---:|---|
| 0 | 0 | $(\mathcal B_{p_0}W_3)_{-4}$ |
| 1 | 1 | $(\mathcal B_{p_0}W_4)_{-4}$ |
| 2 | 2 | $(\mathcal B_{p_0}W_8)_{-4}$ |
| 3 | 3 | $(\mathcal B_{p_0}W_{21})_{-4}$ |
| 8 | 8 | $(\mathcal B_{p_1}W_2)_{-4}$ |
| 9 | 9 | $(\mathcal B_{p_1}W_{20})_{-4}$ |
| 12 | 12 | $(\mathcal B_{p_2}W_{18})_{-4}$ |
| 14 | 15 | $(\mathcal B_{r_0}W_6)_{-4}$ |
| 16 | 17 | $(\mathcal B_{r_0}W_{14})_{-4}$ |

这九个原根 SHA 依序为：

    d5a5b50489d3017d47afc09ceaad86895715a6b6ecad5d499fd90e88723fdab0
    9314e044000e3fc7b977ce994255d3c0a414c476bafeeaa5fbf03a3ae5c6848d
    b8466f56a8f8988a770e5c2302fa899974a191f31df132d71283adff52a950e8
    4b4cf4fae45d00f1acc6abf8bf6c77e7b838c21a4258740f3e2280b7dfa14563
    650c9daa66c46851a1afda435165ec0007961d672b90c2111f6d32473e9142b5
    05d70716c3d6a43e36e58e7cae968d6df5fef63c2af26b2ddc645c8f244dc425
    b78f861dc9eda994027734d9183c76de68275a59de1c51b166c18af837f7c99c
    93c48a84a7bf48ce26ef27628912b27c3a8dea4f52f8fb13c144351f3c1510db
    7205ad3fb3649e7e423da40abeb8390d34b6ba6dd8a3d7ea242b902b36786671

它们的独立性来自**新的完整 pure 函数矩阵**，不是从旧完整两 mode 独立性推 pure 独立。

例如 normalized original 0 对应 $F_0$ 的状态键 $(-4,0,0,0)$，其原比例为 $1/2048$，准确给

$$
\boxed{
[F_{0,-4}]_{h^{-4}}
=\frac{-16\rho_0+128\rho_2+12\rho_3-160\rho_8-32\rho_9
+60\rho_{12}-20\rho_{14}+28\rho_{16}}{2048}.
}
\tag{10}
$$

此归一原列 SHA 为 5cce088086f2d19cba3e69ddb397799ae8bc66f6896a23ad10defec4df0b3174。

另一个直接复用旧完整 A 原根的身份是 normalized original 76：

$$
\boxed{
[\bar A_{hh,-4}]_{h^{-6}}
=\frac{8\rho_0-32\rho_2-2\rho_3+40\rho_8+8\rho_9
-14\rho_{12}+6\rho_{14}-6\rho_{16}}{1024}.
}
\tag{11}
$$

其归一原 SHA 为 f47e9614c2c3371296c5d0424567a3d06fcdd107d1eef60286df71ffeffe7cf1。

原列 33 对应 $F_0$ 中 $h^2k^2\omega^6$ 的比例 $1/1024$，原列 122 对应 $Q_{4,4}$ 中 $h^{-4}\omega^4$ 的比例 $1/4096$，二者的完整真函数都为零。相应非空原呈示 SHA 为

    0a0ac0338f5669c683f299706483e4fd657fb0584a07c8984e4026847cb55ca9
    1b7bde92abf4058c4683b3acaf1bbabc2298a0d67b6d4f922420a75aecd48aad

全部其它原呈示也在 (9) 的同一九维基中；公开 stdout 的 MATHEMATICAL_COLUMN 逐条给准确坐标、原 SHA 和所有状态别名。没有遗漏仅因原表达式项数多而未处理的列。

## 5. 为什么这是完整函数证明

每个旧 pure 响应和新 normal 原列都经一次 R178 同右锚转换。程序没有把 Volterra 原函数当独立变量：相反，先执行已证的完整 shuffle/分部积分转换，再要求所有余字属于 R179 的真实单射语法。

每条新依赖保存准确原列有理组合；独立重加全部原列转换后的完整 word 向量，准确为零；同时形成原 DAG 差并记录 SHA/项数。其证明是所有同锚转换身份的同一有理和，不是只信消元余式标签。没有对已成关系重跑另一个 NF，也没有把非零 NF 误解为非成员。

R179 给两向等价：这些完整余词向量相等当且仅当真实 universal profile 函数相等。因此：

1. 九个非零 pivot 给真实下界 9；
2. 154 条完整原函数关系给上界 9；
3. 原 40 列已经是 R139 的完整 $R_{-4}$ 张成组；
4. (5) 的全部十四族均已进入同一矩阵。

四点合起来证明 (1)，不是只证明一个 163 列子空间的偶然秩。所有表达式保同一个右锚；结果对全部合法共同 collar profiles 成立，不是仅固定幂尾或特定多项式采样成立。

## 6. 从最后候选权到实际有限 pure 支付

### 6.1 pure 闭锥已满

若 $C_{\rm p}\ne P$，R202 的完整有限维、真实仿射及反号论证给一个非零 pure 正仿射分离字符。其可能真权最初只剩 $-8,-6,-4$：

- R203 给 $\pi U_{-8}=0$，所以权 $-8$ 字符不能非零；
- R207 给 $\pi U_{-6}=\pi R_{-6}$；
- 本稿 (1) 给 $\pi U_{-4}=\pi R_{-4}$。

任何 pure 正分离泛函都杀真实响应 lineality $\pi R$。后两等号因此也排除相应非零字符，矛盾。于是

$$
C_{\rm p}=P.
\tag{12}
$$

这一步无需再计算所有奇权的完整像，也没有宣称所有权的 $\pi U_\sigma=\pi R_\sigma$。所用的是 R202 已付的单一偶权分离字符定理。

### 6.2 闭锥满不是实际负路径；R206 支付差距

[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 已给整个权零像等号，因此 $Q=P/\pi R$ 的缩放生成元没有零权、在 Q 上可逆。R206 用 (12) 构造：

1. 有限个实际成本商值的严格正配平；
2. 真实小缩放、端口桥与真倒行夹心，完整保 $2V_{\rm bridge}$；
3. floor 整数复制和统一 $C^1$ 局部截面，准确支付任意固定紧商目标；
4. 先清响应 prototypes 的商基准，再连续清全部剩余商成本；
5. 最后用有限复制与 Brouwer 同时付响应分量。

这些都已在 R206 完整证明，真实复制次数有限，未使用负路径或实数次拼接。由 (12) 可直接应用其等价定理，得

$$
\boxed{S=P.}
\tag{13}
$$

所以对每个指定 $p\in P$，存在一条真实有限同端口、frame $I\to I$、$M=T=0$ 路径 C，使 $\pi V_C=p$ 准确成立。所需有限紧控制族先选定，再取共同物理区间；没有保证任意预给窄区间、统一长度、reach 或位移。

本结论不与 [R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 的完整 canonical 正字符矛盾。R201 已给 pure 为零而 $\lambda_+$ 非零的完整函数，所以该正字符不能下降为 pure 泛函。新控制一般仍有未消去的完整 mixed 成本。

## 7. 非零第三 hook、空间闭合及全 pure 零同时实现

这一步把 (13) 直接用在原机制上，避免把一个未闭路径的函数解冒作已闭几何。

### 7.1 固定整个原闭 hook 基准

按 [R180](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md) §6，先取同 scalar germ 的真实第三环 $L_t$，frame $I\to I$、$M=0$、$T=t\mathfrak H$，$t\ne0$。取 R72 的两个真实 frame 桥 $C_j:I\to g_j$，各 $M=T=0$，其中

$$
g_1=\operatorname{diag}(1,-1,-1),\qquad
g_2=\operatorname{diag}(-1,1,-1).
$$

令 $P_1=L_tC_1$、$P_2=C_2$，依 Klein 八边词

$$
1,2,1,2,2,1,2,1
\tag{14}
$$

闭合，得到原基准 $X_0$。每种 prototype 在四个 ambient 左旋位置
$\mathcal G=\{I,g_1,g_2,g_1g_2\}$ 各出现一次。因 $\sum_{g\in\mathcal G}g=0$，两类真实位移分别相消，全部 frame/scalar germs 也准确相接：

$$
M_{X_0}=0,\qquad T_{X_0}=4t\mathfrak H=:\kappa\mathfrak H\ne0.
\tag{15}
$$

令 $V_0=V_{X_0}$；它包括第三环、frame 桥以及整个有限词的完整 canonical 成本，没有删任何基准。

### 7.2 准确证明 $V_0\in U$

虽然 $T_{X_0}\ne0$，不能直接用“U 定义为 $M=T=0$ 成本的 span”将 $V_0$ 塞入 U。使用 [R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)/[R84](R84-fourth-cost-semigroup-and-frame-length-bound.md) 的真实倒行：$X_0$ 首末 frame I、同 scalar 端口、M0，所以

$$
M_{X_0^{\rm rev}}=0,\qquad
T_{X_0^{\rm rev}}=-T_{X_0},\qquad
V_{X_0^{\rm rev}}=V_0.
$$

真实字 $X_0X_0^{\rm rev}$ 的 $M=T=0$，完整成本为 $2V_0$，故 $V_0\in U$，于是 $\pi V_0\in P$。此处取半倍只证明线性空间归属，不当作半条实际路径。

### 7.3 用一个实际控制修正四个副本

由 (13)，选择一条同 scalar germ、frame $I\to I$ 的真实有限 D，满足

$$
M_D=T_D=0,\qquad
\boxed{\pi V_D=-\tfrac14\pi V_0.}
\tag{16}
$$

把第一类 prototype 改成 $\widetilde P_1=DP_1$，第二类仍为 $P_2$，再用完全相同的八边词 (14)。D 不改变第一类的末 frame 或第三算子；ambient 左旋不改变 scalar 成本。M0 段之间的完整第四传递是准确加法，所以新闭路径 X 有

$$
M_X=0,\qquad T_X=\kappa\mathfrak H,\qquad
\pi V_X=\pi V_0+4\pi V_D=0.
\tag{17}
$$

D 可以有任意真实位移。它被吸收到第一类 prototype 的新位移中，该新位移仍在 $\mathcal G$ 四个左旋位置各出现一次，故空间位移继续准确相消；没有把 D 位移设零，也没有复用未更新的闭合位置。

所有辅助路径及控制紧族有限。选定它们后，取共同合法 I，保持 $h>0$、$\xi+\omega>0$ 的正间隙、共同右锚和双 collar。由此得到 (4) 的有限光滑闭正则浸入带；这里未承诺嵌入、厚度或宏观幅度。

### 7.4 固定圆与最右 period 门的准确升级

在最终几何上选择 R183 的重叠导数分包圆，或 [R199](R199-faithful-monotone-step-for-the-complete-universal-pure-space.md) 的全权 pure 忠实单调末 step 圆。M0、同非零第三 hook 及八包七阶有限差分的全部低阶论证仍成立，所以完整二、三阶 range 保持。

由 [R198](R198-rightmost-single-profile-period-obstruction-under-all-second-gauges.md)，最右 f=0 区间的不可校正单 profile 成本是 $16\pi V_X(g)$。式 (17) 现在使它作为整个函数准确为零；不需要再靠某一个末 step 的采样或首项消去。

这一步消除了那个必要门，尚未解完整 period。由 [R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md)，pure 零后仍有完整的 balanced mixed 表；R184 要求同一个二阶 gauge 同时满足 period 和 ruling 商条件。两者均未被 (17) 自动支付。

另外，没有把精确 pure 零仅凭连续性迁移到 R189 的无开常段几何：零条件不是开条件。若后续需要此几何性质，必须在其真实约束族中重新保留精确校正或给出相应控制论证；本稿不偷加该结论。

## 8. 已付与未付

本稿已经完成三个不同层次：完整权 $-4$ 的真 pure 函数像、完整 pure 成本的真实有限支付、以及保持非零第三 hook 与真实空间闭合的 universal pure 零构造。最后一步包含全部桥和基准，并保持原低阶合法圆条件。

接下来的实际数学目标是该最终几何与同一圆上的完整 balanced mixed period 及第四 ruling 联合匹配；不能分开选两个不同的 w。完整第四解、所有阶恢复或收敛、同 g 的有限连续嵌入族、全域全时 reach 和宏观幅度仍未完成。此处不重复已结案的 pure 负权计算，也不再以单纯 pure 读出来追 R196 的完整正字符。
