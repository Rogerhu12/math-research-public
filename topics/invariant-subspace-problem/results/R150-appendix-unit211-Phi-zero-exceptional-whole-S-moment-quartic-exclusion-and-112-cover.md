# Phi=0 例外图：整个 S 矩像四次纤维的原排除与严格 112 点覆盖

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完成范围

在有序图
$$
b=1,\qquad c=\frac12,\qquad\ell=\frac32,\qquad
u=\frac{3+\rho}{2},\qquad Q=1-\rho^2
$$
中，整个四次参数纤维
$$
M_J(\lambda)=420\lambda^4-1884\lambda^3
 +3663\lambda^2-3084\lambda+916=0
$$
已经返回完整原系统并排除。结论保留全部四个复嵌入和相应的全部 $\rho,T,z$，不是只排除其中的 $S=0$ 点。

该四次式本身已经出现在旧
[S0/Lt0 小 J 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-small-J-exclusion.md)
§2。本稿不重做旧 S0 九式。新的数学输入是全四次域中的同一个原 $\rho$ 共同因子，以及用原 S 单位留下的完整 T 五次环境。

令 $\phi=M_J/420$。本次同时证明原固定结式的真实 QQ 下界
$$
\phi^4\mid R.
$$
结合已发表的真实余投影，实际新 Bézout 返回将该有序图不同 $(\rho,\lambda)$ 基点的严格上界从 128 改进到 **112**。

本次只支付 QQ 重数至少 4。完整模结式在 $\bar\phi$ 处的重数为 8；后者尚不是 QQ 重数 8 的证明。另一 B/C 交换图不并入同一个 112 计数，整个例外图也未由此排空。

## 2. 同一四次常数域中的原 T 六次式与 S 单位

仍使用原定义
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K_0=\ell^2B_3-3\ell T A_2+2T^3,
$$
$$
S_n=\ell B_3-A_2T+(3-2\lambda)D.
$$
在原物理图中 $S_n=SD$，两个因子都已由原完整零支排除支付为非零。对于本权重图，
$$
m=\frac{\rho}{2},\qquad M=2\rho^2,\qquad
F_6=\rho^2(2K_0^2-D^3).
$$
括号内对 T 的最高系数为 9。

实际 QQ 因式分解证明 $\phi$ 不可约；故
$$
K=\mathbb Q[\lambda]/(\phi)
$$
保留全部四个复嵌入。本次在 $K[T]$ 中仅对原六次式与原二次 $S_n$ 作低次 Euclidean 运算，每次除法完整乘回。准确返回一个一次公共因子
$$
T-T_*,
$$
其中
$$
T_*=
\frac{25552}{6707}-\frac{153635}{13414}\lambda
+\frac{58044}{6707}\lambda^2-\frac{16170}{6707}\lambda^3.
$$
因此有完整原身份
$$
2K_0^2-D^3=9(T-T_*)q_5(T),
\tag{2.1}
$$
其中 $q_5$ 首一、次数 5。再对 $q_5,S_n$ 作真实 gcd，返回常数一；只删除了上述一次因子，没有遗漏其更高重数或另一个共同 T 分量。

因为被删除的因子整除真实 $S_n$，原 S 单位保证每个原解仍满足 $q_5(T)=0$。这一步不倒置未知商代数的范数。完整 $q_5$ 系数和 (2.1) 的乘回身份保存在本稿精确输入中。

## 3. 新原 QQ 线性像恢复全部同一 rho 根

记已保存的三条同点原必要曲线为
$$
F=F_{26,26},\qquad G=C_{31,50},\qquad H=C_{34,48}.
$$
在整个 K 中，其原 $\rho$ 次数实际保持 $26,31,34$。将 F 首一后，在
$$
\mathcal B_0=K[\rho]/(\widehat F)
$$
中计算原 G、H 的乘法像。源使用全部
$$
\lambda^i\rho^jG,\quad\lambda^i\rho^jH,\qquad
0\le i<4,\quad0\le j<26,
$$
每项按原首一 F 约化且完整乘回，得到新的 $208\times104$ QQ 矩阵。其真实 QQ 秩为 88。

该像是 K 线性子空间，因此其 K 维数为 22。由一元多项式主理想结构，
$$
\deg_\rho\gcd_{K[\rho]}(F,G,H)=26-22=4.
$$
从降序排列的 rref 取得首一四次候选 g 后，源对完整 F、G、H 作短除法，三项余式均为零，全部商乘积也返回。候选的次数恰等于上面已经由真实 QQ 秩支付的 gcd 次数，故它就是完整共同因子，不是仅覆盖部分原根的一个因子。

准确写
$$
g(\rho)=\rho^4+a_3(\lambda)\rho^3
 +a_2(\lambda)\rho^2+a_1(\lambda)\rho+a_0(\lambda).
$$
全部 16 个有理系数保存在精确输入中；本次系数列表指纹为
178eb7cd37c9e806038e3cfdb9d52551a2cec36950af60e2f4a203bba2fb013d。

逐项原权单位检查没有删除 g 的任何分量。因此
$$
C=K[\rho]/(g),\qquad \dim_{\mathbb Q}C=16
$$
包含全部原参数求值。这里不假设 g 在 K 上不可约、平方自由，或 C 是域。

## 4. 固定原 Sylvester 的四次 QQ 整除下界

原结式保持固定原次数：
$$
R=\operatorname{Res}^{(26,31)}_\rho(F,G).
$$
其矩阵阶为 57，不因参数特化改成另一个尺寸。

令 $q_F=F/g,\ q_G=G/g$，使用上节完整原短除法。对 $0\le j<4$，原 Sylvester 系数映射的核向量为
$$
\bigl(\rho^j q_G,\ -\rho^j q_F\bigr).
$$
两个块的次数分别小于 $31,26$，所以它们是固定 57 列中的合法向量。源逐个核对完整原乘积
$$
(\rho^j q_G)F-(\rho^j q_F)G=0.
$$
第二个块的最高 $\rho$ 次数彼此不同且最高系数非零，因此四列线性独立。准确核列指纹为
d1128129451e6fd9db1312dc18fea194bcc8eade3638f97b2c5be9514e3f3276。

故原矩阵在 K 上余秩至少 4。局部化于不可约 $\phi$ 后，取模 $\phi$ 的可逆行列基变换，可使至少四行全部被 $\phi$ 整除；变换行列式在该局部环中为单位。因此
$$
\phi^4\mid R
\quad\text{于 }\mathbb Q[\lambda].
\tag{4.1}
$$
这是真 QQ 下界，来源是完整原核乘积和独立性，不是从模 $1009$ 的八次重数猜测。

## 5. 完整 160 维原值环境与全秩返回

保 $z=Qt$。原 P1 在 $\Phi=0$ 上给
$$
f=-P_c/P_f,\qquad P_f=T_0(J-Q),
$$
分母已付。完整原 N1 的 $z^2$ 系数为
$$
-4b^2c^2\ell Q(u-1).
$$
源在整个 C 中求得这一系数、$1-Q$、$P_f$ 的真 QQ 逆，并分别完整乘回。于是 N1 给首一关系
$$
z^2+\alpha(T)z+\beta(T)=0.
$$

建立同一个连续首一扩张
$$
\mathcal A=
C[T,z]/\bigl(q_5(T),\
z^2+\alpha(T)z+\beta(T)\bigr).
$$
它的 QQ 维数为
$$
4\cdot4\cdot5\cdot2=160.
$$
此自由环境保留常数代数的全部分量和可能的非约化结构。

源把三条完整原标量均值 R、W、O 以及完整原 NV 返回放进同一环境，每次约化均回乘两个原首一关系。四个生成元 $\lambda,\rho,T,z$ 的真实乘法也逐项核对。

四条原行分别乘全部 160 个基单项式，得到固定原理想矩阵的 640 行。实际在 $1009$ 处选出的 160 行全部来自原 mean_R 的基乘积；全方阵与其逆满足
$$
B_{160}C_{160}=I_{160}
\quad\text{于 }\mathbb F_{1009}.
$$
全部 $160^2$ 个乘积条目均已实际核对。方阵与逆的 SHA-256 分别为

- 3be6342d214c6f7783df70f318495f7b2960a128172f1f224ecd50f93ade9f48；
- 3affa475211322a5251d93548cd2cd58ff8a42d55cd582cd61bf87043136baf7。

原首一规则和全部矩阵条目都在 $1009$ 处可积，所以这是一个固定 QQ 原乘法矩阵的真实非零行列式证书。原 mean_R 在整个有限 QQ 代数中可逆，却又必须在原解上等于零，矛盾。这排除了整个 $M_J=0$ 原纤维，并非只排有限域点。

## 6. 新完整余投影与 112 个不同基点

在已发表的
[整个矩像六次纤维与 128 点覆盖](R150-appendix-unit211-Phi-zero-exceptional-whole-moment-image-fiber-exclusion-and-128-cover.md)
之后，已有真正首一的余投影
$$
R^\#=\frac{R}{\phi_1^{10}\phi_6^2\phi_D^3},
\qquad \deg R^\#=1993,
$$
它在 $\mathbb Z_{(1009)}[\lambda]$ 中；全部被删除的整原纤维均已排除。

本稿的四次 $\phi$ 与那些已付因子不同。结合 (4.1)，定义
$$
R^{\flat}=R^\#/\phi^4,\qquad
\deg R^{\flat}=1993-16=1977.
$$
$\phi$ 首一且在 $1009$ 处可积，故 $R^{\flat}$ 仍是该局部整数环中的首一多项式。整四次原纤维已由上节排除，因此每个剩余原点仍使 $R^{\flat}$ 为零。

源从完整已存的模 R 中进行实际整除并乘回，没有直接对以前打印的 gcd 相除。再对新的完整模 $R^{\flat}$ 与原固定
$$
S=\operatorname{Res}^{(26,34)}_\rho(F,H)
$$
的完整模约化作 xgcd。实际结果为：

| 项目 | 次数 |
|---|---:|
| 新完整模 $R^{\flat}$ | 1977 |
| 原完整模 S | 2050 |
| 新实际 gcd | 112 |
| Bézout 第一标签 | 1937 |
| Bézout 第二标签 | 1864 |

完整 Bézout 组合逐系数乘回。QQ 中的首一公共因子作为首一 $R^{\flat}$ 的因子，在 $\mathbb Z_{(1009)}$ 中可积且约化保度，故其 QQ 次数至多 112。

上引 128 稿 §6 已用原 F26 的实际 QQ 不可约因式记录支付：每个复 $\lambda_0$ 的 F 纤维都是非零的一元多项式，没有整条共同竖线。固定 $57/60$ 阶原 Sylvester 矩阵中，同一个 $\lambda_0$ 上 r 个不同原 $\rho$ 根给 r 个独立 Vandermonde 核列，所以两行列式的消失阶均至少 r。被剥因子在剩余纤维上非零，不改变这些阶数。对所有 $\lambda_0$ 求和，得到不同有序 $(\rho,\lambda)$ 基点总数至多 112。

## 7. 可再生输入及实际身份

唯一新源：

[2026-11-27-unit211-Phi-zero-exceptional-whole-S-moment-quartic-original-linear-values-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-exceptional-whole-S-moment-quartic-original-linear-values-input-8542.py)

源 SHA-256：
b7116bbaeba341aa5356aae2a4ad2a3516f29e896b62f14d49384210272b7d82。

精确新输入：

[2026-11-27-unit211-Phi-zero-exceptional-whole-S-quartic-gcd-and-original-values-exact-input-8542.json](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-exceptional-whole-S-quartic-gcd-and-original-values-exact-input-8542.json)

其中保完整 g 四次、T 五次、原 N1 与 160 维原行载荷。41353 字节载荷的 SHA-256 为
34b737b8d2bbdecbbdd14307862c3de0de30f6054aa00b12aade4a4ea6749892。

实际 run 46044724644 / job 140661012844，源提交 a26f3d9f4982a850bb21825afb37d7f6ba627a2b：

| 项目 | 返回 |
|---|---:|
| 驱动总时间 | 5.218445731 秒 |
| 峰值子进程 RSS | 171388 KiB |
| 内层退出码 | 0 |
| 完整同一 rho 四次 | 3.837675093 秒 |
| 固定原核四次 QQ 下界 | 3.880585586 秒 |
| 完整原 160 维全秩 | 5.137682628 秒 |
| 新完整余项 112 次 gcd | 5.145597656 秒 |

stdout 为 33931 字节，SHA-256 为
4a314d3b19b35ba8585aebc59a82d0069f745b223015d6ca566fa099ed33c0dc。

此前 bb35 二权参数 lambda 模块的 120 秒中止记录保持不变。本次使用不同的完整常数纤维输入，没有把其成功改写为旧模块成功。QQ 的更高 $\phi$ 重数、其余基点及一般原头图继续保留；普通 Hilbert ISP 未因此完成。
