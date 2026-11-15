# 完整权 −2 头部的首次有限有理必要字符系统

日期：2026-11-15。**新消费者及有限测试设计；实际尚未运行。** 本地只执行新增接口的人工例，不读取真实头部研究数据，也不积分真实十四族系数。全部实际原数据消费、状态路径积分和线性规划只能在 Rogerhu12/math-research-public 的公开 Actions 中运行。

独占源码：scripts/literature_character_minus2_finite_necessary.py。它消费已经完成的 literature_character_head_minus2.py 导出；不修改该生产器，不重建任何 forcing、N 响应、旧 40 原基、旧 31 pure 关系、旧 44 阶子式、profile 取值或已有 normal form。

数学来源为 [R140](../results/R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R148](../results/R148-sharp-one-dimensional-highest-action-positivity.md)、[R163](../results/R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md) 和 [R164](../results/R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)。有理路径接口由 tail_cost 的 full-character-rational-action-necessary-system-design-20261115.md 提供；本消费者首轮只用线性必要行，不引入 SDP、cvxpy 或未验证的浮点不可行结论。

## 1. 输入必须是真正完成的完整头部

唯一研究输入组是新的完整 head 主报告、terminal publication receipt 和原式 gzip。CLI 显式给出各小文件 SHA、run、source commit 和 lane；在实际回执出来前不预填它们。生产器必须绑定：

~~~text
literature_character_head_minus2.py
bytes 58856
sha256 fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11
~~~

主 schema：

~~~text
visible-flex-complete-character-head-minus2-v1
~~~

原式 schema 是该值加 -original-expressions。主报告必须 completion=complete、head_generation_complete=true；导出必须：

~~~text
content_scope = complete-fourteen-weight-minus2-families-and-translation-presentation
all_fourteen_families_complete = true
all_planned_contractions_present = true
planned_contractions = completed_contractions
target_weight = -2
~~~

核对 gzip/raw 字节数与 SHA、main/receipt run/source、完整 source_hashes、原生产器源码以及每条正规记录的两模式原 SHA。部分 contraction cache 不能进入正性测试。

实际消费的字段：

| 字段 | 用途 |
|---|---|
| normal_family_records | 全部 U 内正规系数，逐条设一个字符坐标 |
| head_translation_presentation | R163 的完整平移分母等式 |
| static_translation_reference_coefficients | 八参考态的 F0 omega 导数 |
| static_scaling_reference_coefficients | 八参考态的 F0 缩放导数 |
| reference_matrix | 同一八矩基及其有理逆 |
| eight_reference_coordinate_polynomials | 全 m0、m2 的参考坐标，用于同一乘子修正 |
| archived_R_basis_records | 已证完整 R−2 基，字符值固定为零 |
| roots、profile_atoms | 只识别字面原零或原比例关系，不作 primitive/profile 评价 |

原静态参考根 static_reference_i_mode_* 属于原局部环境，不另增为 U 内的字符变量。乘子只使用两个 F0 参考导数列表。

## 2. 一个包含全部真实正字符的有理外部空间

设正规系数原列表为 $Z_0,\ldots,Z_{n-1}$，令 $x_j=\lambda(Z_j)$。n 来自完成的实际导出，事先不知道，也不拿已知 44 维下界替代它。

R163 给 $U_{-2}=R_{-2}+\operatorname{span}\{Z_j\}$。因此对杀 R 的单权字符：

$$
x=0\quad\Longrightarrow\quad\lambda=0.
\tag{1}
$$

首轮加入以下精确等式：

1. 完整 head_translation_presentation 的每条有理组合为零。
2. R163 的八个 F0 参考态原零身份。
3. R164 同一乘子的八条 Lie 兼容式。
4. 全十四族扣掉同一矩阵乘子后，除 $h^{-2-e}k^b$ 外的全部 omega/logh/h 次数系数为零。
5. 已存两模式原向量中，字面为零或准确成比例者的关系；若与某个已发 R 列成比例，其字符值为零。

第 5 项只在共同原 DAG 的原单项式字典上比较准确有理系数。它不作旧 R 的 normal form，不重证旧秩，不称已找齐原函数依赖。比例的有理数、原根引用与每条关系均保存；非相同字面表示没有被认作独立真实函数。

这些等式共同定义一个**外部候选空间**。其维数是外部有理系统的维数，不是 $\mathcal H_{-2}$ 的真实维数。遗漏的真函数关系只能使该外部空间更大；若在这个较大空间已准确排除非零候选，则足以排除所有真实权 −2 正字符。外部可行则尚不产生真实泛函。

没有调用不完备 normalizer 的阴性余式来断言非成员。

## 3. 八矩乘子的唯一有理表达式

按 R73 的坐标顺序

$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)
$$

取单位 $E_j$。八个参考导数列表先通过同一参考矩阵逆转换：

$$
c_j=\sum_i a_i(E_j)\lambda\partial_\omega F_0(S_i^*),\qquad
d_j=\sum_i a_i(E_j)\lambda(h\partial_h-\omega\partial_\omega)F_0(S_i^*).
$$

由 R164，

$$
\begin{aligned}
\mu_{p_0}&=d_{p_0},&
\mu_{p_1}&=d_{p_1}/2,&
\mu_{p_2}&=d_{p_2}/3,&
\mu_{r_0}&=-d_{r_0},\\
\mu_{r_1}&=(c_{s_1}-4c_{p_0})/3,&
\mu_{s_0}&=(c_{s_1}+2c_{p_0})/3,&
\mu_{s_1}&=d_{s_1},&
\mu_{t_1}&=d_{t_1}/2.
\end{aligned}
\tag{2}
$$

不把参考态序号冒充 E8 坐标，也不为各路径单独选择 μ。所有这些量都是同一 x 的有理线性式。

以参考坐标 $a_i(m_0),a_i(m_2)$ 和 $\mu(m_0(S_i^*))$ 实现扣除，不重新生成矩阵原密度。静态和二次层分别使用

$$
a^\lambda(S)=\lambda F_0(S)-\mu m_0(S),\qquad
b_i^\lambda(S)=\lambda F_{2,i}(S)-\mu m_{2,i}(S).
\tag{3}
$$

最高十族仍是 $\lambda$ 作用于完整正规系数。R164 迫十四个标量族均形如 $h^{-2-e}f(k)$。消费者先对全部不符合的状态系数加等式，再提取允许的 k 多项式；没有未经约束就裁掉原项。

八条 Lie 兼容对真实字符自动成立，加入外部空间不表示发现了八个新的独立真实障碍。R162 已证明 J6 不在旧比较空间，首轮绝不加未经证明的 $\lambda(J6)=0$。

八参考态还给一个可解释的冗余推论，无需新增研究门。固定 h=1，令 d=omega−k；k=0 时

$$
\mu m_0=-\{\mu_{r_0}d^3+(\mu_{r_1}+2\mu_{s_0})d^2
+(\mu_{r_0}+2\mu_{s_1})d+\mu_{r_1}+\mu_{t_1}\}/8.
$$

F0 在四个 d 参考值都为零，而 corrected 静态与 omega 无关，故该三次式为常数，迫
$\mu_{r_0}=\mu_{s_1}=0$、$\mu_{r_1}+2\mu_{s_0}=0$。随后 k=1 的四次项已消，同一四点三次论证给
$\mu_{p_0}=0$、$\mu_{r_1}+\mu_{s_0}=0$ 和
$\mu_{p_1}=(\mu_{r_1}-\mu_{s_0}+\mu_{t_1})/4$。于是

$$
\mu\in\operatorname{span}\{p_1^*+4t_1^*,p_2^*\},\qquad c=0,
$$

$$
a(0)=\mu_{t_1}/8,\qquad a(1)=\mu_{p_2}/2,\qquad
\mu m_0=\mu_{p_1}(k^2-1)/2-\mu_{p_2}kh/2.
$$

消费者已加入完整八参考零与 corrected 协变，故准确消元自然包含这个推论；没有另取参考点或新增数据计算。

## 4. 固定且有界的第一张必要测试表

所有半空间均为 $a_\ell(x)\ge0$，系数是准确 Fraction。首轮只使用有限有理点，不把它称为全 k 轴或全部 PSD 方向的判定。

固定状态点：

$$
k\in\{-2,-1,0,1,2\}.
$$

在每点加入：

- 完整修正静态 $a(k)\ge0$；
- 完整 fixed-k sharp 门 $q_4(k)+25A(k)/9\ge0$；
- 加速度二次式 $A(k)v_1^2+B(k)v_1v_2+C(k)v_2^2\ge0$，方向为
  $(1,0),(0,1),(1,1),(1,-1),(1,2),(2,1),(1,-2),(2,-1)$。

sharp 行包含全部原 N2 修正后的 Q4，不引用 pure 或 m8 投影来删除项。

### 六条完整多项式路径

置

$$
\rho(s)=35s^4-84s^5+70s^6-20s^7,\qquad 0\le s\le1,
$$

$$
p=1+\alpha\rho,\qquad k=\kappa+\beta\rho,\qquad h=p^{-2}.
\tag{4}
$$

固定表为：

| 路径 | alpha | kappa | beta |
|---|---:|---:|---:|
| h_axis | 1 | 0 | 0 |
| k_axis | 0 | 0 | 1 |
| mixed_plus | 1 | 0 | 1 |
| mixed_minus | 1 | 0 | −1 |
| decreasing_p | −1/2 | 0 | 1 |
| crossing_k | 1 | 1 | −2 |

$\rho'=140s^3(1-s)^3$，故 $0\le\rho\le1$。每条都有明确正下界
$p\ge\min(1,1+\alpha)>0$，没有数值找最小值。

定义

$$
Z=6(p')^2-2pp'',\qquad D=-2pp'k''-k'Z.
\tag{5}
$$

三个完整积分层是

$$
A_P=\int_0^1p^4a(k)\,ds,
$$

$$
B_P=\int_0^1\sum_{i=0}^2b_i(k)(-2p')^ip^{4-i}(k')^{2-i}\,ds,
$$

$$
\begin{aligned}
C_P=\int_0^1\{&
A(k)Z^2+B(k)p^2Zk''+C(k)p^4(k'')^2\\
&+p[-2H_1(k)p'+H_2(k)pk']D\\
&+\sum_{i=0}^4q_i(k)(-2p')^ip^{4-i}(k')^{4-i}\}\,ds.
\end{aligned}
\tag{6}
$$

这些是 s 的有理系数多项式，按 $\int_0^1s^j\,ds=1/(j+1)$ 精确积分，不调用数值求积。面积项完整保留；mixed_plus 上 $D=-6(\rho')^3$ 非零。

真实时长缩放的必要式是

$$
\delta A_P+\delta^{-1}B_P+\delta^{-3}C_P\ge0.
$$

首轮加入两个极限行 $A_P\ge0,C_P\ge0$，以及

$$
t^2A_P+tB_P+C_P\ge0,\qquad
t\in\{1/16,1/4,1,4,16\},\quad t=\delta^2>0.
\tag{7}
$$

不加入 $B_P\ge0$。例如 $A=C=1,B=-1$ 满足完整时长条件，不能被错误排除。t 有理足以使所有行有理；实际时长 $\sqrt t$ 可以为任意正实数。

### 平端正则性为何合法

将 (4) 接常值，得到 C3 函数，并非 C∞。取其 C∞ 常领近似在 C² 中收敛，保 p 的统一正下界；必要时把积分区间扩大一个趋零的小量。完整正规 action 只含至二阶 jets，系数在该紧状态区域连续，新增常领积分趋零，所以 (6) 是真实光滑开平端路径不等式的合法极限。

omega 按

$$
\omega'=\tfrac12p^2k'
$$

真实积分，仍为有理多项式原函数；mixed_plus 时
$\omega=\omega_0+[(1+\rho)^3-1]/6$。
R140 允许末 omega、frame 和位置不预先指定，所以不用研究 ODE 求解来重新支付这条路径的合法性。全部实际系数积分仍仅在公开 Actions。

## 5. 全生成坐标的精确零证书

先对所有等式作 Fraction 高斯消元，得

$$
x=B y,
\tag{8}
$$

其中 y 就是若干原 normal 坐标，不存在未覆盖的自由方向。完整等式、RREF、free-index 列表与 B 都保存。它们的秩只称为外部等式秩。

将必要半空间代入 (8) 得

$$
A_{\rm out}y\ge0.
\tag{9}
$$

若没有自由坐标，等式已迫 x=0。否则，对**每个**自由坐标 j、两个符号 $\varepsilon=\pm1$，寻找准确证书

$$
\varepsilon e_j=\sum_\ell u_{\ell,j,\varepsilon}(A_{\rm out})_\ell,\qquad
u_{\ell,j,\varepsilon}\in\mathbb Q_{\ge0}.
\tag{10}
$$

式 (10) 的右侧对每个可行 y 非负；两个符号共同迫 $y_j=0$。所有 j 完成后，x=0，再由 (1) 严格排除全部非零权 −2 正字符。

这等价于在覆盖全部坐标的盒上证明各正负方向最优值均为零，但证书无需把盒的不齐次边界混入 (10)。不存在只规范化 $\lambda(J)$、$\lambda(D0)$ 或 $\lambda(J6)$ 而漏掉其余方向的问题。

### 浮点只提出支持集

SciPy HiGHS 只用归一化行提出 (10) 的非负支持集。随后：

1. 在这个支持集上，以 Fraction 解准确等式；
2. 精确检查每个系数非负；
3. 用已保存原有理半空间重新求和，逐项验证目标恰为 $\varepsilon e_j$；
4. 只有这三步全部成功，才保存该符号的 Farkas 证书。

既不把浮点状态 infeasible 当作证明，也不把接近零的余量设零。支持重构失败可留下未决，不能宣称正字符存在。

若某方向未取得证书，可用同一有限系统的盒 LP 找一个候选，并在 Q 上重构、逐行核其可行性。成功也仅证明这个**外部必要系统**留有非零点；没有证明它定义真实 U 上的泛函，更没有证明所有路径非负。若重构也失败，只保存浮点建议，明确未决。

不重复扫描旧基、旧 normal form 或其他仿射权；首个未排除外部点已经是后续设计新路径的具体入口。

## 6. 输出与逐项可核格式

小主报告 schema：

~~~text
visible-flex-character-minus2-finite-rational-necessary-v1
~~~

完整证书同 stem 加 -certificate.json.gz，schema 再加 -certificate。证书包括：

- 完整正规坐标 metadata、来源 run/source/main/receipt/export；
- 每条等式及其出处，R163 分母原行号和 R164 状态协变键；
- 所有必要半空间的准确有理系数、测试状态/方向/路径/时长；
- 六条路径的准确 A、B、C，p、k、Z、D 和 omega′ 多项式；
- 同一 μ、c、d 的 normal 坐标表达式；
- RREF、全部 free 坐标及 x=B y；
- 每个已成 (10) 的准确非负乘子与目标；
- 若有，经过逐有理行验证的非零外部候选；
- 所有尚未取得证书或预算退出的具体状态。

验证者可从已绑定 head 重新构造等式/路径行，使用普通 Fraction 消元核 (8)，然后逐项核 (10)。验证不需要 profile 评价、原 Volterra 运算或对浮点求解器的信任。

唯一能令 positive_character_excluded=true 的情况是：输入完整、全部自由坐标的两个符号证书完成（或准确等式已无自由坐标），且完整证书成功保存。该字段只指权 −2。含必要不等式的外部系统只保证全部真实正字符嵌入：证书使用 all_true_positive_characters_embed_in_this_outer_system，checkpoint 使用 all_true_positive_characters_embed_in_the_test；成功 outcome 为 all_true_positive_weight_minus2_characters_excluded_by_exact_outer_system。它们不声称任意不具正性的字符也满足这些半空间。true_character_existence、all_positive_characters_excluded、complete_period_or_ruling_paid 始终不由此任务授予。

## 7. 来源、预算、人工与 CLI

独立源码不 import 旧研究 compiler；只以字节身份绑定冻结 head 生产器。研究入口强制检查 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY 为本公开仓库。参数允许明确传入实际文件位置，但不能改变来源身份。

缺省预算：

| 项目 | 上限 |
|---|---:|
| elapsed time | 240 s |
| 轮询 RSS | 1024 MiB |
| 有理数 numerator/denominator 位长 | 16384 bits |
| 完整 normal 坐标接口 | 5000 |
| head gzip / raw | 4.8 MB / 40 MB |
| 小主报告 | 95000 B |
| 完整新证书 gzip | 4500000 B |
| 总新输出 | 不超过 4.8 MB |

内存和时间为显式轮询，LP 每次另有剩余预算内的短 time limit。实际 head 的未知维数、实际 LP 结论、原式关系数量均不预填。若首轮预算不足，保已成的小报告及已构造系统；不假称未处理坐标为零。

新的人工例只用虚构系数、原单项式和小矩阵，覆盖：
非对角参考基转换、14 项分母抵消、rho 与非退化面积项、符号保持、负中间层、完整坐标参数化、原比例关系、错误 Farkas 权重拒绝、HiGHS 支持的准确重构、留有正锥时不误排除、来源 SHA 篡改拒绝。没有读取真实头部数据或进行实际字符测试。

部署前核读仅将上述三个报告标签明确为 positive，没有改变算法、半空间、路径表或人工例。既存人工报告保留其原源码身份，不改写为新版本的执行回执；公开首次 development 将执行本次标签修订后的源码。

CLI：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_finite_necessary.py \
  --toy-only --output WORK/character-minus2-finite-necessary-development.json

python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_finite_necessary.py \
  --head-report HEAD/character-head-minus2.json \
  --head-publication HEAD/receipt.json \
  --head-export HEAD/character-head-minus2-original-expressions.json.gz \
  --head-report-sha256 ACTUAL_MAIN_SHA \
  --head-publication-sha256 ACTUAL_RECEIPT_SHA \
  --head-run ACTUAL_RUN \
  --head-commit ACTUAL_SOURCE \
  --head-lane ACTUAL_HEAD_LANE \
  --output WORK/character-minus2-finite-necessary.json
~~~

HEAD 由已完成的公开回执绑定。若生产器只发表 partial contraction cache，本命令明确拒绝，而不是用缺失项继续形成虚假的必要系统。
