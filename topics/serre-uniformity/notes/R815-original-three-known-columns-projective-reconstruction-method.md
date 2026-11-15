# R815：由原三列 0、1、271 恢复真实有理乘法算子

日期：2026-11-15。状态：本文件给出新来源、新搜索身份的准确执行契约；三列共同分母、候选和完整算子须由公开 Actions 实际产生。本任务不修改正在续算的原 R815，不重算原 425 个素数、原 $Wv_g$ 或已完成的标量扫描。

## 1. 原对象与已完成的准确输入

沿 [R813](../results/R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md)、[R817](../results/R817-original-normal-derivation-without-separate-h-multiplier.md) 与 [原两列执行方法](R815-original-two-known-columns-reconstruction-method.md)，固定原正规基 $\beta_0,\ldots,\beta_{271}$、$\beta_0=1$，及其次数
$$
\epsilon=(0,1^{144},2^{127}).
$$
记 $W=M_w$ 为 R806 已准确恢复的乘法矩阵，$v_g=M_g e_0$ 为 R813 已准确恢复的原向量。所有矩阵仍按“输出行、输入列”解释；原 $D_0$、$1/82$ 和截面尺度均通过原来源保留，本任务不再按权数乘入任何尺度。

R806 原 producer 为 run 43707290840、source 75b1d56c821abe34660477ba8b4c7f7b75a4382b；其 group 000 文件的原 SHA256 为 3b2b11873b4c505275845f9d4639215b27273856ff9a21cc771cabf9b504bdfa。原 820 行准确认证已证明该组是原 $W$ 的真实列。2026-11-15 的纯 IO run 43759938598、source 53ef6c84a175645d66bea73c1eeca8b9825e9ca0，仅读取该已成坐标及原 S3 映射，得到：

- 列 0 唯一非零项为 S 行 4、原基行 1、$z$ 次数 0、分子与分母均为 1。
- 列 1 唯一非零项为 S 行 688、原基行 271、$z$ 次数 0、分子与分母均为 1。

因此已有真实等式
$$
We_0=e_1,\qquad We_1=e_{271}.
\tag{R8153.1}
$$
完整列 1 的 IO 文件为 39073 字节，SHA256 为 3c42c6428e4561c91090df8ec95a6c9f9a940c5ae21a1e80a72825738b78006e。上述关系不是从分母长度、基编号或候选 recipe 猜测的。新 core 将在同一已保原 $W$ 的所有多项式系数上直接断言两式；无需重做 R806 求解或矩阵乘法。

真实两列 producer 为 run 43755027718、source e1d8a95631eb11d1df0ccba4a781b05b6dd45c62、core 0008796890a0cfcf0b9aaaa40e26f0d8d26be38f8168c8fe918d86a7585a0ec1。其已完成文件 R815-two-known-columns-exact-original-input.json.gz 为 1608842 字节、SHA256 8907fb65e6724d09ba21cca87b649c45631dc0e0f1c1d477f147447be4f4073c，包含
$$
v_0=v_g=N_0/d_{01},\qquad v_1=Wv_g=N_1/d_{01}.
\tag{R8153.2}
$$
其中 $d_{01}>0$ 是两列联合约分后的最小共同分母，实际 6485 位。该 producer 已准确计算 $Wv_g$、核其次数以及原 425-prime current 中全部 1652 个相应同余。本次只读该文件，不再计算 $Wv_g$。该次候选搜索的有限失败不否定原算子，也不证明原模数精度不足。

## 2. 新第三列的准确含义

函数乘法矩阵交换，故由 (R8153.1)
$$
M_g e_1=WM_g e_0=Wv_g,\qquad
M_g e_{271}=M_gWe_1=WM_g e_1=Wv_1.
\tag{R8153.3}
$$
本次只新增最后一个准确多项式矩阵乘向量。第三个已知输入列为 271，不能误当作列 2。

原 $M_g$ 满足
$$
\deg (M_g)_{ba}\le 3+\epsilon_a-\epsilon_b.
\tag{R8153.4}
$$
因此三列分别有 690、962、1234 个合法系数，总计 2886。存储可统一为
$$
[\text{slot }0,1,2]\,[z\text{ 次数 }0,\ldots,5]\,[b=0,\ldots,271],
$$
三个 slot 对应输入列 $0,1,271$。超出各自真实次数界的项必须为零，不能将其截去后视为已核。

写原 $W=\sum_{i=0}^{3}U_i z^i/d_w$，其中 $d_w>0$ 是原已保整数多项式表示的共同分母。读入 (R8153.2) 的整数数组后，只计算
$$
P_k=\sum_{i+j=k} U_i(N_1)_j,\qquad 0\le k\le7.
\tag{R8153.5}
$$
准确核每个输出行中 $k>5-\epsilon_b$ 时 $P_{k,b}=0$，包括所有第 6、7 次项。接着把三列共同表示为
$$
d_wN_0,\quad d_wN_1,\quad P
\quad\text{除以}\quad d_wd_{01}.
\tag{R8153.6}
$$
取初始分母与全部三个整数数组的正 gcd $c$，逐项除以 $c$，得到
$$
d_{012}=d_wd_{01}/c>0,\qquad
\widetilde N_0,\widetilde N_1,\widetilde N_{271}.
\tag{R8153.7}
$$
其联合 content 为 1，故 $d_{012}$ 是这三列的真实最小共同分母，并且 $d_{01}\mid d_{012}$。这不宣称 $d_{012}$ 已是完整 $272\times272$ 矩阵的分母。

令 $M$ 为同一原 425 个素数之积。新程序准确核 $\gcd(d_{012},M)=1$，再用同一原 current 的固定 layout 对全部 2886 个合法项核
$$
(\widetilde N_a)_{k,b}\equiv
d_{012}\,r_{b,a,k}\pmod M,\qquad a\in\{0,1,271\}.
\tag{R8153.8}
$$
这是新共同标度与原 current 的接缝认证；它不产生新的模图或新的 CRT 素数。两个旧列的准确值来自已完成文件，未重新求解。

新第三列的乘积按 $U_iN_1$ 的四个左系数块原子保存。完成块有独立来源与 SHA，预算续接只计算未完成的块；完成第三列后保存联合约分和全部同余证书。

## 3. 新候选：改变已知列和共同分母，保原未知坐标

先尝试 $D=d_{012}$。其后只从未知输入列 $a\notin\{0,1,271\}$ 选择两项原 residues $r_i,r_j$。对固定权移
$$
0,\ 256,\ -256,\ 1024,\ -1024,\ 4096,\ -4096
$$
构造三维整行格
$$
\begin{pmatrix}
d_{012}w_d&\operatorname{center}(d_{012}r_i)w_n&
                 \operatorname{center}(d_{012}r_j)w_n\\
0&Mw_n&0\\
0&0&Mw_n
\end{pmatrix},
\quad
w_d=2^{\max(s,0)},\quad w_n=2^{\max(-s,0)}.
\tag{R8153.9}
$$
保存全部三条 LLL 行、完整整基变换与行列式 $\pm1$。取消符号后，只将满足 $D>0$、$d_{012}\mid D$、$\gcd(D,M)=1$ 及两个原同余的行作为候选。没有平方根高度界、唯一性矩形或成功保证。

同一个 $D$ 只准确尝试一次。新候选的全部合法系数定义为
$$
N_{ba,k}=
\begin{cases}
(D/d_{012})(\widetilde N_a)_{k,b},&a=0,1,271,\\
\operatorname{center}(D r_{b,a,k}\bmod M),&a\notin\{0,1,271\}.
\end{cases}
\tag{R8153.10}
$$
三列始终取已知的准确值；即使其整数分子超过中心区间也不改为中心剩余。其余系数仅是待验候选。

原两列搜索的 LLL 行、$D$ 与拒绝不能作为这次已尝试的候选，因为 (R8153.7) 与 (R8153.10) 改变了候选矩阵。原拒绝文件只保来源，不变更标签或宣称它们已拒绝新候选。

## 4. 已成标量扫描的复用边界

两列 producer 的实际 scan 文件为 3463 字节、SHA256 3782cd81bae0a5a80e260b80ec8cde0539ee5af97619a8b19652fb5b130fb39d。实际停止位置为 25，四对失败索引为
$$
(10,11),\quad(12,13),\quad(15,17),\quad(20,24).
\tag{R8153.11}
$$
这些分类只依赖原 current、原 strict rational reconstruction 和原全局坐标次序，不依赖当前候选分母。新 core 逐来源核四个 probe 文件、完整 scan25、原 imported-scalar-scan 与原 current 同余；已完成前缀不重复 RR。

在该前缀中新增已知列 271 尚未出现。因而本次可以据实际文件复用 (R8153.11)，为新 $d_{012}$ 构造新的格；这不是复用旧 LLL。之后仍沿同一原全局次序扫描，从第 25 项起才可发生新的 strict RR。未来遇到列 0、1、271 都跳过。第一、第二个非零 probe 只能由实际原 residue 零性选出，不把旧列 1 的首非零位置搬成新未知列。

所有运行限制仅控制预算和可尝试的 pair 数；固定权、列集合、候选定义及验证规则由新源码 SHA 与数学 tag 锁定。

## 5. 准确拒绝与唯一成功出口

由 (R8153.3)，强制三列后的候选自动满足
$$
[N/D,W]e_0=0,\qquad [N/D,W]e_1=0.
\tag{R8153.12}
$$
故不能再把列 0、1 的交换子当作有辨识力的早期测试。本次从真实未知列 2、3 选固定早期项，例如在 $z=0,1$ 的输出行 0；仍准确保留每一非零整数残差、坐标与来源。这些只是原完整交换子的条目，早期通过不构成成功证书。

唯一成功出口仍为原 R817 的准确判据：

1. 每项满足 (R8153.4)，三列逐系数等于已知值，特别第一列为原 $v_g$。
2. 在七个固定不同有理点 $z=0,\ldots,6$，准确检查完整 $272\times272$ 交换子 $[N/D,W]$ 为零。
3. 保留原 R806 的真实 cyclic 证书及正规基、原向量/场/尺度身份。

交换子各项次数至多 6，七点为零即多项式恒零。$e_0$ 对原 $W$ 循环，故同第一列且与 $W$ 交换的算子唯一；成功候选因此就是原 $M_g$。不依赖 LLL 最短性或任何猜测高度界。

联合已知列之外的中心代表可能错误；任一早期或完整准确残差非零都只拒绝该有限候选。候选耗尽不得写成原算子不存在、模数精度不足或固定原高度已解决。

## 6. 与原 $\Gamma$ 和两图的衔接

新 $M_g$ 若成功，沿冻结 80516ff9 核心继续原 $\Gamma$ 的已审算法、七点嵌套交换子与两图运输。新数学 tag 使用新真实 core/method/source；原425 current、原 $W$、原 $v_g,v_h$ 及 Krylov cache 均以显式旧来源读取，不伪装为新标签自产。

只在 $M_g$ 与 $\Gamma$ 都具完整准确证书时，原名最终证书的 complete 才为 true。$M_g$ 候选耗尽或预算结束均诚实保存 false endpoint 与可续 current。后续消费者仍必须核真实新 source/core，不能把本任务当作旧 80516ff9 的输出。

## 7. 文件、身份和断点约定

核心为 scripts/R815_three_known_columns_reconstruction.py；RESULT 仍为 R815-original-normal-derivation-operators，FINAL 仍为 p41-original-normal-derivation-operator-certificate.json。CLI 沿原 projective 参数，projective-method 指向本文件。新 mode 为 three-known-columns-0-1-271-and-three-dimensional-Q-common-denominator。

retained/R815 保存原425来源；retained/R806、R813 保存原53输入；retained/R815P2 保存实际已结束两列来源的最小小文件，包含准确两列、audit、scan、四个 probes、imported scan 和原完整 metadata。旧3037成员 carrier 原样复用，P2小载体独立保存；所有成员逐 bytes/SHA 认证。

新完整阶段仍为 output 根目录 R815-*.json.gz。准确第三列新增四个乘积 checkpoint 及最终三列 stage，均有同一数学 tag 和原输入 spec。新 stage manifest 只列新标签的实际完整阶段；old source spec 通过显式 resolver 核验。complete=false 的 probe-current 单列 current_checkpoints。硬断后已完成乘积、候选定义、early/full 证书和队列均按真实指纹回用；已关闭失败大 payload 只能先保存 bytes/SHA 历史再删。false FINAL 只记当时状态，不能覆盖后来推进的 current。

Git 只保存本方法、脚本、参数和运行/输出 hash。完整整数数组、LLL 行、候选、矩阵及载体只用于一日 active artifact。首次运行的真实 $d_{012}$、乘积次数消去、候选数、失败位置或成功状态均留待 Actions 回执，不预填数值。
