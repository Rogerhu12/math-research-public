# R787：固定 C 的下一模层障碍、共享残差与真实来源契约

日期：2026-11-15。状态：**纸面证明与尚未执行的最小接口。没有新的模层、候选拒绝或准确函数结果。**

本篇接
[56维增量格方法](R787-original-incremental-three-probe-reconstruction-method.md)第7–8节，
并逐项对照冻结
[原R787关系方法](R787-original-power5-relation-solver-method.md)及其固定 SHA 的核心
的 rational_blocks、branch_laurent、residual、correction 与 lift。
原题的 $L$、$B_{\rm fld}=\lambda b$、$s^2=-3$、原129阶、
$Z'$、原自由列1186、原指数与 $82^{10}$ 尺度不变。
本篇不执行任何新的 LLL，不求14支 Schur 逆，也不构造特征零 $1234$ 阶逆。

## 1. 实际已有的四组数据

固定
$$
\ell=1000000753,\qquad M=\ell^{430}.
$$
430来源仍是 run43708449812，
source ac5998f333ab49c4747874e2e44b7ca4ccfa3acf；
原核心 SHA256 为
93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04。
实际 retained manifest SHA256 为
1b92c4e594f4d1d14cfd4b62fda8513511dc879a7c6e2c7d9f60de52dd5ca689；
原430 stage SHA256 为
00855d88fec4c18ec7cbfd4927dd72042d8e0372d1ac95498a0e5fcd9f118029。
这些输入已经在当前原1380件 carrier 内。

需要读取的已有字段如下，均保持原 configuration 和 file/bytes/SHA。

| 来源 | 原字段及用途 |
|---|---|
| 原430 lift | A_L_coordinates、C_L_coordinates、modulus、digits、chart_sha256、full_original_modular_relations_verified |
| 原 rational-blocks | A_pivot_rows、A_remaining_rows、A_inverse_mod_prime、Z_pivot_integer_rows、Z_free_diagonal 及原常数列次序 |
| 原 selection | evaluation_matrix、inverse_evaluation_matrix、roots_B_s、kappa_inverse_at_each_L_branch 和原单位条件 |
| 原1234 real rows、R781 field/R0…128/κ0…129 | 实际整数 $t$ 坐标、原整阶、$g_t$ 及逆自由 Laurent 归一化 |

关键来源事实是：selection 自己已经保存全部14支
kappa_inverse_at_each_L_branch，每支20个系数。
所以本接口**无需下载14个 branch 大文件**来寻找逆 clear multiplier，
也无需再次求任何 $\kappa$ 的逆。
rational-blocks 中只有 A_inverse_mod_prime；
原字段 A_inverse_over_Q_computed=False 仍如实保留。

## 2. 原清分母方程与还原顺序

令
$$
\mathcal O=\mathbf Z[B_{\rm fld},s],\qquad
\omega=(1,B_{\rm fld},\ldots,B_{\rm fld}^6,s,\ldots,sB_{\rm fld}^6).
$$
$t=\xi+\xi^{-1}$ 满足原首一20次 $g_t$。
计算保持 $\omega_i t^r$ 的原280坐标次序；
只在 $\ell$ 处局部化原已认证为单位的有理分母。
不要求 $g_t\bmod\ell$ 不可约。

设 $F_n$ 是已成第 $n$ 个 $20\times1234$ 整数块。
对列向量 $a,c$ 定义
$$
A(v)=\sum_{n=0}^{128}F_na\,v^n,\qquad
B(v)=\sum_{n=0}^{128}F_nZ'c\,v^n.
$$
每个20维块解释为 $t$ 多项式。
准确 $E_0Z'=0$ 保证 $B_0=0$。
原 $Y(v)=v\,y(v)$ 的系数是
$$
Y_m=-\frac{R_m}{246^3\kappa^{m+1}},
\qquad 0\le m\le128. \tag{1}
$$
因此，对 $1\le m\le128$，
$$
E_m(a,c)=A_{m-1}-(YB)_m, \tag{2}
$$
其原清分母形式为
$$
T_m(a,c)=246^3\kappa^{m+1}A_{m-1}
 +\sum_{j=0}^{m}R_{m-j}\kappa^j B_j
 =246^3\kappa^{m+1}E_m(a,c). \tag{3}
$$
$m=0$ 的方程由 $B_0=0$ 构造性满足。
按 $m-1$ 外、$t^r$ 内排列 (2)，得到
$$
E(a,c)=F_Aa-C_yc\in L^{2560}, \tag{4}
$$
其中 $F_A$ 是原 $F_0,\ldots,F_{127}$ 的叠放，
$C_yc$ 是 $(YB)_1,\ldots,(YB)_{128}$ 的原坐标。

原 selection 的第 $b$ 支评价行记为
$$
e_b=(B_b^i s_b^j)_{j=0,1;\ i=0,\ldots,6};
$$
它只定义模 $\ell$ 的映射。
设 $h_b(t)$ 是该 selection 中已有的 $\kappa_b^{-1}$。
则 (3) 的逆 clear multiplier 恰为
$$
\gamma_{m,b}(t)=246^{-3}h_b(t)^{m+1}\pmod{g_t,\ell},
\qquad 1\le m\le128. \tag{5}
$$
首项的幂是2，末项是129。
可以从已有 $h_b$ 顺序相乘得到 (5)，没有新的数域逆。

若 $(a,c)$ 已满足模 $M$ 的原系统，
先在原280坐标环模 $M\ell$ 求 (3)，每个标准整数代表可被 $M$ 整除。
随后依次：

1. 逐整坐标除以 $M$，得到模 $\ell$ 的280维向量；
2. 用原 $e_b$ 评价14个 $L$ 坐标；
3. 在 $\mathbf F_\ell[t]/(g_t)$ 乘 (5)；
4. 展开20个 $t$ 系数，进入 (4) 的2560行。

这个次序不可调换。
特别不能把只在模 $\ell$ 为根的 $B_b,s_b$
直接当作模 $M\ell$ 的根使用；
那不定义原整阶的高精度代数映射。
本接口保持高精度运算在280坐标环里，除 $M$ 后才分支。

冻结 correction 把上述还原结果再取负作为 rhs。
本篇的 $\rho$ 和下文 $\rho_0$ 使用**未取负的残差**；
若直接消费该旧 rhs 约定，必须保这一负号。

## 3. 固定 C 的唯一分子与下一位障碍

令原行集为 $J$、补集为 $\mathcal R$：
$$
|J|=1234,\quad |\mathcal R|=1326,\quad F_\star=F_A[J].
$$
这里 $F_\star$ 是原固定方块；前节 $F_n$ 继续表示20行的级数系数块。
设
$$
U_0=(F_\star\bmod\ell)^{-1},
$$
直接读取 A_inverse_mod_prime。对任何原分支定义
$$
P(x)=x_{\mathcal R}-F_A[\mathcal R]U_0x_J. \tag{6}
$$
它只使用这一个有理系数模逆，且 $P(F_Au)=0$。

固定准确整向量 $c'$。
只要 $(a',c')$ 满足模 $M$，令
$$
\rho=\frac{E(a',c')}{M}\pmod\ell
$$
按第2节实际还原。下一位只能是
$$
\delta a=-U_0\rho_J,\qquad
\Omega(c')=P(\rho). \tag{7}
$$
若任一原支的任一 $\Omega$ 坐标非零，
就不存在准确 $a^*\in L^{1234}$ 使 $E(a^*,c')=0$。

证明：原 $F_\star$ 在 $\ell$ 处为单位。
如果准确分子存在，它必为
$$
a^*=F_\star^{-1}(C_yc')_J, \tag{8}
$$
且在 $\ell$ 处整，并与 $a'$ 模 $M$ 相同。
其下一位必须是 (7) 的 $\delta a$；
剩余行则必须为零。
因此一次非零障碍已是对固定 $c'$ 的严格否定。

若把 $a'$ 改成 $a'+Mu$，$\rho$ 增加 $F_Au$，
(6) 恰好杀掉这个变化。
故 (7) 不会把独立中心提升 $A$ 的错误误当成 $C$ 的错误。

这里使用的是**去共同 content 前**的原整对。
若先除含 $\ell$ 的 content，就必须相应降低可用精度。
整个推导没有除以代数 $D$，
所以不需要把 $D$ 为模 $\ell$ 单位列为接受条件。

## 4. 一次共享高精度残差与每个 D 的小模计算

原430向量记为 $(\bar a,\bar c)$。
对原非零代数分母 $D\in\mathcal O$，
使用冻结候选规则定义 $c'$：
非自由坐标取 $\operatorname{center}_M(D\bar c_i)$，
选定自由坐标准确取 $D$，其余自由坐标为零。
有准确整恒等式
$$
c'=D\bar c-Mq_c,\qquad q_c\in\mathcal O^{1214}. \tag{9}
$$
同样，若使用原中心提升的分子，
$$
a'=D\bar a-Mq_a.
$$
定义共享来源
$$
\rho_0=\frac{E(\bar a,\bar c)}M\bmod\ell,\qquad
\Omega_0=P(\rho_0). \tag{10}
$$
由线性性，
$$
\frac{E(a',c')}{M}
 =D\rho_0-F_Aq_a+C_yq_c \pmod\ell.
$$
因 $P$ 的系数在 $\mathbf F_\ell$ 中，
它与原 $L$ 标量 $D$ 的作用相容；
再用 $P(F_Aq_a)=0$，得到
$$
\boxed{\ \Omega(c')=D\Omega_0+P(C_yq_c)\pmod\ell.\ } \tag{11}
$$

(11) 给一个真正的批量接口：
共享 $\Omega_0$ 只取一次；每个候选不再做高精度 $A$、
不再求14支 Schur 逆，也不重新生成完整 $C_y$ 矩阵。
$q_c$ 可逐行从原430坐标、真实 $D$ 和确定的中心代表求出；
不必建立旧已拒候选的完整 A/B payload。
选定自由列及其他自由列的 $q_c$ 都为零。
$q_c$ 的模 $\ell$ 值就足够。

对某一实际支 $b$，只需：

1. 用原 $e_b$ 评价 $q_c$，得到1214列；
2. 用原 $Z_p,Z_d$ 展开一个原 $Z'q_c$ 向量；
3. 以已有 $F_n$ 计算它的原20维系数 $G_n$；
4. 用 (1)、原 $R_m$ 和已有 $h_b$ 做一个 $Y_bG$ 卷积；
5. 对所得2560行施加 (6)，再加 $D_b\Omega_{0,b}$。

这只有一个右端。
可以消费原 convolution_matrix 的39步 $t$ 打包公式，
但不能重新生成其1214个原列或原14个 Schur 方块。
先试 branch0 合法；非零已经足够否定这个固定 $c'$。
若它为零，可以按原固定顺序继续其他支；
只要尚有支未检查，报告范围就须精确保留。

(10) 可以从原430数据直接按 (3) 在模 $M\ell$ 计算一次。
这只是一个新共同源阶段，并不是声称旧系统已升到431位。
若相同源阶段在后继真实 artifact 已存在，应直接消费其原字节。
不得因为尚未能读仍运行 job 的文件，就伪称已经取得这个模层。

## 5. 更小的前缀必要条件

原 $J$ 是从69个 $A$ 系数块中选出，故
$$
J\subset\{0,\ldots,1379\}.
$$
令
$$
\mathcal R_{\rm pre}=\{0,\ldots,1379\}\setminus J,
\qquad |\mathcal R_{\rm pre}|=146.
$$
可以先把 (6) 的输出限制在 $\mathcal R_{\rm pre}$。
这仍然消去 $F_Au$，任何一个非零值仍严格否定固定 $c'$。

注意输入阶数有一位错开：
$A$ 的前69块对应 $m=1,\ldots,69$；
$(YB)_m$ 需要 $B_0,\ldots,B_{69}$，
所以要读已成 $F$ 的 $q_Y^0,\ldots,q_Y^{69}$ **70块**，
以及原 $R_0,\ldots,R_{69}$ 和 $\kappa$ 至70次幂。
这些全在原129阶闭包内，不添加新尾、不重新计算已成前缀。

这一模式可同时用于共同 (10) 和每个候选的 (11)，
因而不必先完成全部128个非构造性方程才有严格否定。
如果146行全零，只能报告“该前缀必要条件通过”。
其余1180行没有检查，不能写成完整 $\Omega=0$，
更不能声称 $C$ 真实或准确函数已恢复。

若要进一步缩短前缀，可以从实际 A_pivot_rows 读出其最大行，
然后固定所需的实际范围；该实际数值不得预填。

## 6. 已发布更深 current 时，连共享431残差也可省去

这一分支有明确前提：必须有**已经结束并真实发布**、
与原 normalized chart 相同的原提升 current，精度 $n\ge431$。
在撰写时，不把仍运行中的原 same-core 后继当作可读来源。

若后来实际获得 $(a_n,c_n)$，先逐项核：

- 同一个原 mathematical configuration、整阶、原 prime 和 chart；
- 原 free pattern（选定列为1，其余自由列为0）；
- 真实 full_original_modular_relations_verified=true；
- 原来源 SHA/manifest/运行链；
- $c_n\bmod M=\bar c$，需要分子来源时同样核 $a_n\bmod M=\bar a$。

取
$$
\delta c=\frac{(c_n\bmod M\ell)-\bar c}{M}\pmod\ell. \tag{12}
$$
原两个完成模关系相减给
$$
\rho_0+F_A\delta a-C_y\delta c=0\pmod\ell.
$$
于是
$$
\Omega_0=P(C_y\delta c),\qquad
\Omega(c')=P\bigl(C_y(D\delta c+q_c)\bigr). \tag{13}
$$
因此不再计算 (10) 的高精度共同残差，
也不需要恢复或重做该原 Dixon 步。

还可以利用原已认证单位 Schur minor。
向量 $D\delta c+q_c$ 的全部自由坐标为零；
原 Schur 主元列在每个实际支为单射。
故在该支
$$
\Omega_b(c')=0
\quad\Longleftrightarrow\quad
(D\delta c+q_c)_b=0. \tag{14}
$$
这里仅引用真实已有的单位 minor 结论；
如果消费器没有绑定它，就只使用 (13) 的单向必要检验，
不能平白增加 (14) 的等价断言。

更一般，在已经认证的精度 $n$，
任何准确关系且自由模式为 $D$ 的 $c'$ 都必须满足
$$
c'\equiv D c_n\pmod{\ell^n}. \tag{15}
$$
证明：原同一单位主元块使给定自由坐标的解在每一模层唯一。
这对可能非单位的 $D$ 也成立，不需除以 $D$。
因此 (15) 任何一项不符，都严格否定这个固定 $c'$；
只作整阶乘法和同余比较，不用任何新 $A$ 逆或投影矩阵。
(12)–(14) 正是 (15) 的下一位写法。

这些是消费未来真实已成模层的条件公式，
不是一份该模层已经完成的结论，也不是启动另一个并行原 Dixon 求解器。

## 7. 准确唯一性与有限通过的边界

对于固定 $c'$，(8) 说明特征零分子至多一个。
但它不说明这个分子通过剩余1326行。
在任何有限个模层通过 (7)、(11)、(13) 或 (15)，
都只给必要条件；本篇没有给使某个有限精度自动充分的高度界。

如果确有一个 $c'$ 值得继续，可以用已有 $U_0$
对固定右端作新的14个原 $L$ 坐标 RHS 的分子 Dixon：
每次保持 $c'$ 完全不动，按 (7) 更新 $a$；
一旦剩余行障碍非零就严格结束该固定 $c'$。
该模式不需要14支1186阶 Schur 逆，也不重新求 $F_\star^{-1}\bmod\ell$。
它仍有高精度残差及准确重构成本；
现有来源不支持预称它比56维格便宜。

最终正面出口保持原129阶准确式、
$B\ne0$、原自由模式和原全球几何判据。
没有任何 $\Omega=0$、小格长度、单位诊断或有限位数
可以替代这个出口。
原当前直接中心提升 $A$ 的失败，
与严格否定固定 $C$ 的障碍，是两种不同结论。

## 8. 尚未执行的来源与阶段契约

若以后落实本接口，首先固定 source_mode：
from_original_430_cleared_residual 或 from_published_deeper_normalized_lift。
两者不得混标签；后一模式在真 source 到达前保持 pending。

共同数学身份至少绑定：
原430 manifest/lift/selection/chart/rational-blocks，
原 R781 field/R/κ、原 real-row 来源，
原 prime/field/变量次序，
正残差与原 correction 负 rhs 的符号约定，
输出行范围（146前缀或1326全量），
以及实际新深 current 来源（若使用）。
同一个来源标签不能在运行后从前缀切换为完整结论。

共同阶段保实际 $\rho_0$ 或 $\delta c$ 的源、原 $h_b$ 的 SHA链、
实际还原指数、$U_0$ 的原来源和各已完支的 $\Omega_0$。
候选阶段保真实14整数 $D$、未除content规则、
$q_c\bmod\ell$ 的来源、已查支/已查行范围，
以及首个准确非零阻碍。
旧42或56候选只按原 D 源引用，不把其旧 A/B 拒绝重标为新 $C$ 拒绝。

预算与允许处理的候选数量可增；
已完成共同源、同一候选同一支的完整决定须原子保存并复用。
源码、参数、纸面证明及简明运行/SHA登记可入 Git；
机器回执与向量、残差、矩阵只在一日 active artifact/carrier 续传。

本篇没有实际生成 $\Omega_0$、$\Omega(c')$、更深 current、
新 $C$ 拒绝或原准确函数。
