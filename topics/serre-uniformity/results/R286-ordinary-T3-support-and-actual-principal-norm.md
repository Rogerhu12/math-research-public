# R286：普通 j07 盘的真实 T3 支撑及完整主函数范数

日期：2026-11-13。**状态：已证明且已实算。** 本文在 $47^4$ 精度构造
ORD_j07 真正中心的四条三同源、完整 $41$ 层结构和全部 $73$ 个模型坐标，
再将已保存的实际主函数 $\Phi_C$ 在四个目标上求值。得到

$$
\operatorname{Norm}_{T_3(P)}\Phi_C=2692600,\qquad
\log\operatorname{Norm}_{T_3(P)}\Phi_C=540218\pmod{47^4}.
$$

这里 $C=P-b$，$b=P_{-3}$。这是规范方向 $F_3=9T_3+2$ 所需的一个真实
移动支撑范数，不是完整 $\sigma_{F_3}$ 高度。特别地，本文没有将它单独当作
局部 QC 函数，也没有声称消掉 R267 的两个 F2 候选根。

## 1. 原始输入及四条实际三同源

全部计算在
$R=\mathbf Z/47^4\mathbf Z$、
$R_2=R[i]/(i^2+1)$ 中进行。ORD_j07 的物理模型是

$$
E:y^2=x^3+38x+41.
$$

R231 保存的实际 $41$ 挠点基处于一个 $840$ 次未分歧半坐标环：
记 $P_{41}=(x_P,y_0)$、
$Q_{41}=(x_Q,y_0q)$，其中 $y_0^2=x_P^3+38x_P+41$。
本文重新检查两点的曲线方程、$41$ 阶性及真实 Weil 配对
$e_{41}(P_{41},Q_{41})=\zeta$；所有奇权值保留共同的 $y_0$，偶权乘积在
该半坐标环中精确计算。

非零三阶点的横坐标满足

$$
\psi_3(r)=3r^4+6Ar^2+12Br-A^2=0.
$$

除以单位 $3$ 后，实际首一核多项式为

$$
h(r)=r^4+76r^2+164r+1626079\in R[r].
$$

其模 $47$ 分解是
$(r+10)(r+25)(r^2+12r+17)$。因此四根全部在 $R_2$，且两两之差是单位。
在原 $840$ 次环中找到剩余根并作两次 Newton 提升后，得到以下完整四根：

| 分支 | $r$ 的实部 | $i$ 系数 |
|---|---:|---:|
| 0 | 2150573 | 2391984 |
| 1 | 1758527 | 0 |
| 2 | 2150573 | 2487697 |
| 3 | 3699689 | 0 |

程序逐根核 $h(r)=0$、$\varphi^2(r)=r$、
$r^3+Ar+B$ 为单位，且核全部六个差为单位。
因此这是完整、无重根的四个三阶循环核。

对每根置

$$
t=2(3r^2+A),\qquad v=4(r^3+Ar+B).
$$

归一化 Vélu 映射为

$$
\phi_x(x)=x+\frac{t}{x-r}+\frac{v}{(x-r)^2},\qquad
\phi_y(x,y)=y\left(1-\frac{t}{(x-r)^2}
                    -\frac{2v}{(x-r)^3}\right).
$$

目标模型系数为

$$
A'=A-5t=-9A-30r^2,\qquad
B'=B-7(v+rt)=-27B-42Ar-70r^3.
$$

每支都实际计算并保存原始
$\phi(P_{41}),\phi(Q_{41})$，核目标曲线、目标判别式为单位、
两点均有 $41$ 阶，以及

$$
e_{41}(\phi(P_{41}),\phi(Q_{41}))=\zeta^3.
$$

原始层结构的行列式 $3$ 被明确保留在证书中。

## 2. 固定模型的层标号及 Galois 迹

这里需要保持 R102 模型的原 $\zeta$ 及原 $R_2$ 嵌入。
对原始像基使用向量标号 $(a,b/3)$，其配对就是 $\zeta$；
相应项链是 $\operatorname{diag}(1,3)$ 作用于源项链后的项链。
R121 实际 T3 证书中的这一置换把源标号 $394$ 送到 $401$。

目标项链的 $\mathrm{SL}_2$ 代表是

$$
g_{401}=\begin{pmatrix}30&19\\1&28\end{pmatrix},
$$

所以在保留的原始像基上，实际评价向量矩阵为

$$
G=\begin{pmatrix}1&0\\0&3^{-1}\end{pmatrix}g_{401}
 =\begin{pmatrix}30&19\\14&23\end{pmatrix}\pmod{41}.
$$

程序核 $\det G=3^{-1}$。保存的原始像点没有被更换；
这个矩阵只用于实际 Eisenstein 向量的标号。原始配对的 $3$ 与标号行列式的
$3^{-1}$ 相消，故所有评价确实属于原模型，而非另一个二次下降规范。

在每个目标上，程序由真实群律重新得到全部 $1680$ 个非零挠点的权一值，
再按 R102 的全部 $42$ 个正规化子代表和选定 $73$ 对向量求和。令该乘积和
（包括 $y_0^2$）乘原 $\zeta$ 后为 $z$。核 $\varphi^{40}(z)=z$，
并按

$$
\Re\operatorname{Tr}_{40/2}(z)=\frac{20}{840}\operatorname{Tr}_{840/1}(z),
\qquad
\Im_i\operatorname{Tr}_{40/2}(z)
=-\frac{20}{840}\operatorname{Tr}_{840/1}(iz)
$$

取精确坐标。这一系数来自实际环次数：
在 $\varphi^{40}$ 固定子环上，绝对迹有因子 $840/40$；
$R_2$ 到 $R$ 的迹再有因子 $2$。
每支另外直接累计首个权二值的全部二十项
$\sum_{a=0}^{19}\varphi^{2a}(z)$，与上述迹坐标逐项相等。

四个目标坐标由真实挠点、群律和截面定义得到。到后面的 Hecke 迹核验以前，
程序不使用 Hecke 矩阵求解这些目标。

## 3. 完整四次有限 étale 代数及全局模型核验

设 $S=R_2[r]/(h(r))$。四根之间的差是单位，故四阶 Vandermonde 矩阵可逆。
用它将四个已算出的实际 $73$ 坐标行插值为

$$
W_T(r)=W_0+W_1r+W_2r^2+W_3r^3\in S^{73}.
$$

程序把插值结果在四根重新求值，全部恢复原四支坐标。它在 $S$ 中由真实
$V_1V_1\to V_2$ 乘法重建 $199$ 个二次坐标，并核全部

$$
73\cdot74/2=2701
$$

条实际二次乘法等式；四个多项式系数的真实半线性下降也全部通过。

Newton 和给出

$$
\operatorname{Tr}(1)=4,\quad \operatorname{Tr}(r)=0,\quad
\operatorname{Tr}(r^2)=-4A,\quad \operatorname{Tr}(r^3)=-12B.
$$

因此实际四支总和是 $4W_0-4AW_2-12BW_3$。
最后独立核了完整 $73$ 维空间的等式

$$
\frac{4W_0-4AW_2-12BW_3}{3}=W(P)\,T_3^{(V_1)}
$$

及其全部 $54$ 个典范坐标限制

$$
\frac{\operatorname{Tr}(W_T)K_1}{3}
=W(P)K_1T_3^{(\Omega)}.
$$

这里的 $1/3$ 是 R121 实际归一化 Hecke 拉回迹的因子；原始像基的行列式
$3$、截面的二十项下降迹和此处的 $1/3$ 分别记录。
全部 $73$ 个等式和全部 $54$ 个等式均模 $47^4$ 成立。
这也使权二空间的非尖点部分接受了实际核验。

## 4. 对已保存真实主函数求值

R267 为此同一 ORD_j07 中心保存全部 $457$ 个主函数及真正微小
Abel 终点；R252 给出这些群链和端点主函数通用的准确除子关系。令

$$
\Phi_C=f_{\mathrm{final}}^{-1}\,
       \frac{v_1}{f_c}\,\frac{F_P}{G_Q},
\qquad
\operatorname{div}(\Phi_C)=m(P-b)-A_1(t).
$$

这里 $m$ 是原长链中的完整正整数；所有整数指数均保留，
没有用其模 $47^4$ 余数替换指数。
R267 的单盘归档和完整输入清单提供这些相同字节的主函数。
本文不重跑该群链。

R265 的 Weierstrass 处理器适用于任意一批 $R_2$ 点，因此本文按源哈希复用
其与目标次数无关的逐图方法。四个实际目标由一个单位射影图覆盖，
所有 $W,V_2,V_3$ 展开到 $z^{27}$。
逐点保存初始、负点、最终、family1 四个理想的全部 $73$ 列，并用整个理想
确定它的 Weierstrass 因子，不以某一列的碰巧单位性代替理想判断。

对初始负点及 $454$ 个 AddFlip 步骤，分别保留真实截面单位和首一因子。
若一步输出理想为 $E_{\mathrm{out}}$、输入为 $E_j$、真实截面为 $F$，则核

$$
W_F=W_{E_{\mathrm{out}}}\prod_jW_{E_j}.
$$

全部 $455$ 条等式在每个目标都成立，总计 $1820$ 条。
另外，实际端点传输满足

$$
W_{v_1}W_{F_P}=W_{\mathrm{final}}W_{G_Q}.
$$

完整理想给出 $W_{\mathrm{initial}}=W_{f_b}$、
$W_{\mathrm{family1}}=W_{v_1}$，故全部 distinguished 因子确实相消；
最终得到的是 $\Phi_C$ 的真实单位值。
$v_1/f_c$ 完整保留。即使某个原 $f_c$ 不是单位，R252 的最终 $f_c$ 整数指数
为零及这些真实首一因子恒等式仍给出正确的消去规则。

每点一共处理 $460$ 个截面。四点残阶分布合计为

| 残阶 | 截面数 |
|---|---:|
| 0 | 1799 |
| 1 | 28 |
| 2 | 12 |
| 3 | 1 |

最高残阶为 $3$，远低于二十七阶展开所允许的 Weierstrass 精度界；
实际准备和全部精确首一多项式除法均通过。
最后的单位值分别用正向群链和 R252 的完整整数指数乘积计算，两者完全一致。

## 5. 实际值及其范围

四支的值和对数如下，所有数均取模 $47^4=4879681$：

| 分支 | $\Phi_C$ | $\log\Phi_C$ |
|---|---|---|
| 0 | $1754289+1136554i$ | $4728059+1428988i$ |
| 1 | $662727$ | $4562243$ |
| 2 | $1754289+3743127i$ | $4728059+3450693i$ |
| 3 | $4367202$ | $1160900$ |

两条非实分支互为共轭。四个值的乘积和四个对数的和分别是

$$
2692600,\qquad 540218.
$$

程序还对乘积直接取 $47$ 进单位对数，得到同一个 $540218$，且范数及对数
的虚部都为零。

完整 $F_3$ 规范高度还需要固定支撑、
$\Delta^*T_3$ 的准确项、第二变量微小积分及规范截面坐标。
因此此结论严格保持
complete_actual_local_sigma_F3_height=false、
complete_all53_local_QC_heights=false、
complete_common_roots=false。
当前实算只填补真实 $T_3(P)$ 支撑及其主函数范数。

## 6. 冻结输入、产物及重建

| 产物 | SHA-256 |
|---|---|
| p41_ordinary_t3_split_support47.py | 63dc334ce2c10cfbb8b14911cf9f8bec26bc9bf553e2ccc5332f386cd03ea448 |
| p41_ordinary_t3_split_norm47.py | aa5ee96e0b8e5f52939d3ecfa5160fd35c6f8d00199d88e973f92b1a90965a56 |
| ORD_j07_actual_T3_support47.json.gz | a629f04511e2b0cf37689e38e3cdbc899cd7b89b921298f65e7c0116390ac136 |
| ORD_j07_actual_T3_principal_norm47.json.gz | 4876d596c4a8e47fe31520f858c122d8b6b8a9428ca8fd44451c90b62e8038a6 |
| ORD_j07_T3_chart0_jets27.json.gz | 90fe7b145537d3e38960fc0a4905852a6e5889d86276886824208656ed2d25e3 |

支撑执行器绑定 R231 的全部普通实际点输入及 R121 完整真实 T3 输入。
范数执行器再绑定此支撑、R267 的 j07 主函数/乘法/第二类证书、
R241 的 based-points 及 R265 的准备器源码。完整哈希边和四支原始挠点均在
机器证书中。所有新文件由 R286-handoff-manifest.json 按字节封存。

在课题脚本目录已装齐这些已发布依赖，并将 R267 的归档解到 work 后，
可先运行支撑执行器：

~~~sh
OPENBLAS_NUM_THREADS=1 python scripts/p41_ordinary_t3_split_support47.py \
  --script-dir scripts --ordinary-lifts scripts/data/p41_ordinary_point_lifts47.json.gz \
  --j 7 --output work/ORD_j07_actual_T3_support47.json.gz
~~~

再运行真实范数执行器：

~~~sh
OPENBLAS_NUM_THREADS=1 python scripts/p41_ordinary_t3_split_norm47.py \
  --script-dir scripts --support work/ORD_j07_actual_T3_support47.json.gz \
  --principal-expression scripts/data/ORD_j07_actual_principal_function47.json.gz \
  --transport-directory work/ordinary-principal-transports/ORD_j07 \
  --based-points scripts/data/p41_all19_based_points47.json.gz \
  --second-kind-certificate scripts/data/ORD_j07_second_kind_complete47.json.gz \
  --multiplication scripts/data/ORD_j07_multiply47.json.gz \
  --cache-dir work --output work/ORD_j07_actual_T3_principal_norm47.json.gz
~~~

本次四支支撑从头实算约 $85$ 秒；范数也已实际执行完成。
记录的是实际完成的计算及代数身份，而非仅给出待执行方案。

