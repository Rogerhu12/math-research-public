# 原单值零证的无逆清残差转置：确定性解、旧模逆复用与完整接受出口

日期：2026-11-16。状态：本文给出一个可直接实施、严格终止的准确接受算法及最小来源契约；尚未运行新的 dual RHS。它接[原短 CM 候选接受稿](R787-original-short-CM-candidate-exact-acceptance.md)，不改变原点 DAG，也不将短候选、有限精度相等或原非挠证书代替该稿的(A.1)。

## 1. 准确目标及固定来源

目标仍是原候选 $q\in L$ 的单个准确身份
$$
A_0-qB_0=0.
\tag{D1}
$$
$q$ 来自已成 CM 候选文件，解释于原
$L=\mathbf Q(B,s)$、$B=\lambda b$、$s^2=-3$ 的十四坐标；此处仅把它作为给定的准确数域元素，而不预称为原点值。原 $B_0\ne0$ 已有真实单位分支证书。

沿接受稿(A.5)--(A.13)，保持原未清行的
$$
F_Aa-Cc=0,\quad B=Zc,\quad c_f=1,\quad f=1186,
\tag{D2}
$$
以及原 $J$（1234个 A 选行）、$I$（1186个 Schur 选行）、$P$（1186个 Schur 选列）。其他27个自由坐标为零。$Z$ 必须保原 `Z_pivot_integer_rows` 中已带的负号及 `Z_free_diagonal`，不得再换号或再清一次 content。

令 $\mathcal S=J\cup R[I]$，原2560行的补集为 $\mathcal O$，所以
$$
|\mathcal S|=2420,\qquad |\mathcal O|=140.
\tag{D3}
$$
准确 CM 行 $e=e_0$、$E=e_0Z$ 已完成。接受稿(A.9)所需的证书是
$$
F_A^t\lambda=e^t,\qquad
(C^t\lambda)_P=qE_P^t,\qquad
(C^t\lambda)_f=qE_f,
\quad \lambda_{\mathcal O}=0.
\tag{D4}
$$
下面不生成准确 $C$、准确 Schur 矩阵或其数域逆。它只使用原已成 $R_m,\kappa^j$ 的正乘算子。

## 2. 原核心的正清残差，逐指标固定

设
$$
\mathcal T=L[t]/g(t),\quad\deg g=20,
$$
始终使用原 $1,t,\ldots,t^{19}$ 系数坐标。原完整幂五行的 $v^j$ 块为
$F_j\in\mathbf Q^{20\times1234}$，$0\le j\le128$。
对给定 $a,c$，置
$$
A_j=F_ja,\qquad B_j=F_jZc\in\mathcal T.
$$
这里 $F_A$ 是 $F_0,\ldots,F_{127}$ 的叠置。它的第 $m$ 个20行块对应 $A_{m-1}$，不是 $A_m$。

原 R787 核心 `residual()` 已固定的正残差为
$$
H_m(a,c)=246^3\kappa^{m+1}A_{m-1}
       +\sum_{j=0}^{m}R_{m-j}\kappa^j B_j,
\quad1\le m\le128.
\tag{D5}
$$
其第0块是 $R_0B_0$，由于准确 $F_0Z=0$，恒为零，不作新的未知量。
原已有 $R_0,\ldots,R_{128}$ 及 $\kappa^0,\ldots,\kappa^{129}$ 逐项只读。
没有新增 Laurent 递推或重新生成旧幂。

记 $\mu(a)$ 为在原20坐标中乘 $a$ 的矩阵，置
$$
L_m=246^3\mu(\kappa^{m+1}),\qquad
\mathcal L=\operatorname{diag}(L_1,\ldots,L_{128}).
$$
原 $Y_m=-R_m\kappa^{-m-1}/246^3$ 的负号给
$$
H=(H_A,H_B)=\mathcal L(F_A,-C).
\tag{D6}
$$
特别是 $H_B=-\mathcal LC$，不是 $+\mathcal LC$。这决定下文转置 RHS 的符号。

## 3. 一个整数 Frobenius 配对消去所有高精度乘法转置

定义原系数泛函
$$
\varphi(a)=[t^{19}]a,
\qquad J_{rs}=\varphi(t^rt^s),\quad0\le r,s<20,
\tag{D7}
$$
乘积先按同一个首一 $g(t)$ 约化。$J$ 是对称整数矩阵，且在反转列序后为单位三角矩阵：$r+s<19$ 时该系数为零，$r+s=19$ 时为一。因此
$$
\det J=\pm1.
\tag{D8}
$$
它的逆也是整数矩阵，可由这一个三角结构准确求出。

结合律及交换律给
$$
\mu(a)^tJ=J\mu(a)\qquad(a\in\mathcal T).
\tag{D9}
$$
这是原系数转置的一个明确换基，既不是未经换基的域 trace，也不是 Hermitian adjoint。无需 $g'(t)$ 的逆。$J$ 的全部400项只读原 $t^0,\ldots,t^{38}$ reduction 规则即可生成，属于这个新 dual 接口所需的新小算子。

把转置行未知量写成 $\mu_m=J\chi_m$，$\chi_m\in\mathcal T$。由(D6)、(D9)，
$$
\lambda_m=L_m^t\mu_m
          =246^3J\bigl(\kappa^{m+1}\chi_m\bigr).
\tag{D10}
$$
高精度计算这条式子只需原 $\kappa^{m+1}$ 的正乘，不需计算它的高精度逆。

## 4. 清残差的完整转置只需一次反向卷积

定义
$$
U_j=\sum_{m=\max(1,j)}^{128}R_{m-j}\chi_m,
\qquad0\le j\le128,
\tag{D11}
$$
以及
$$
V_j=J(\kappa^jU_j).
$$
直接转置(D5)，再用(D9)，得到
$$
H_A^t\mu=\sum_{m=1}^{128}F_{m-1}^t\lambda_m,
\qquad
H_B^t\mu=Z^t\sum_{j=0}^{128}F_j^tV_j.
\tag{D12}
$$
第二式中的 $Z^t$ 仍是二十个原稠密行加原 free diagonal 的稀疏算子。它需要已成 $F_{128}$，不能因第一式只到127而把这个真实输入省去。

令 $X_n=\chi_{128-n}$（$0\le n\le127$）、$X_{128}=0$。则
$$
U_j=[v^{128-j}]
 \left(\sum_{a=0}^{128}R_av^a\right)
 \left(\sum_{n=0}^{128}X_nv^n\right).
\tag{D13}
$$
所以所有 $U_j$ 来自一次长度129的原280维域卷积。
当 $j=0$ 时，额外出现的 $m=0$ 项被 $X_{128}=0$ 准确消掉；
当 $j=128$ 时得到 $U_{128}=R_0\chi_{128}$，端点也保留。
可复用冻结原核心的 packed modular-field 乘法，但必须另给新的转置 source/tag，不能把新结果标成旧 primal current。

## 5. 加上140个补集条件，得到一个真正的方阵解

将下列映射视为 $\mathcal T^{128}\simeq L^{2560}$ 上的 $L$ 线性算子：
$$
\Theta(\chi)=
\left(
H_A^t(J\chi),\quad
(H_B^t(J\chi))_P,\quad
\lambda_{\mathcal O}
\right).
\tag{D14}
$$
三个输出的 $L$ 维数分别为 $1234,1186,140$，总数2560。
这里 $J\chi$ 按128个20维块理解，$\lambda$ 用(D10)给出。

**命题 D.1。** $\Theta$ 在原 $L$ 上可逆，并且在旧辅助素数
$\ell=1000000753$ 的原十四个合法分支上均为单位算子。

**证明。** $J$ 幺模；原已成分支证明每个 $\kappa$ 及 $246$ 是单位，所以(D10)在所有分支可逆。若 $\Theta\chi=0$，则 $\lambda_{\mathcal O}=0$。其余两组方程恰是原选行矩阵
$$
M^t\lambda_{\mathcal S}=0,
\qquad
M=\begin{pmatrix}F_0&-C_{J,P}\\F_I&-C_{I,P}\end{pmatrix},
\tag{D15}
$$
其中这里的 $F_0$ 是原 A 选行方阵，不是 cusp 的第0系数块。
原 A minor 和1186阶 Schur minor在十四分支均非零，故 $M$ 在每个分支可逆，特征零也可逆。因此 $\lambda=0$、$\chi=0$，同维数给结论。$\square$

原 CM 行与 $q$ 的有理坐标都有限。选择一个明确正整数 $d$，使
$$
d(e^t,-qE_P^t,0)
$$
在原十四维整数坐标中整；$d$ 只清目标的有理分母，不改原模型 $b$，不重新插入原关系已经清去的 content。求唯一准确解
$$
\Theta\chi=d(e^t,-qE_P^t,0).
\tag{D16}
$$
因(D6)，其 $\lambda$ 满足(D4)前两组方程的 $d$ 倍和补集零条件。
只余一个准确标量：
$$
\Delta=(H_B^t(J\chi))_f+dqE_f.
\tag{D17}
$$
将(D5)作用于同一个原归一关系，得到完整符号恒等式
$$
\boxed{d(A_0-qB_0)=-\Delta.}
\tag{D18}
$$
因此在(D16)已准确乘回后，$\Delta=0$ 才接受原值，$\Delta\ne0$ 则严格拒绝该 $q$。这个边界不依赖任何数值高度估计。

## 6. 原模逆可给任意新的转置 RHS，不需重求14个大逆

本段只在 $\mathbf F_\ell$ 的每个原分支上执行。已有来源给
$$
F_0^{-1},\quad S^{-1},\quad C_{J,P},\quad
(246^3\kappa^{m+1})^{-1}\ (1\le m\le128).
\tag{D19}
$$
最后一列正是原 `inverse_original_clear_multipliers[m-1]`。原 `branch_laurent()` 的循环先在 $m=1$ 保存 $1/(246^3\kappa^2)$，到 $m=128$ 保存 $1/(246^3\kappa^{129})$；不能整体错一位。

对任意新 RHS $(b_A,b_P,b_{\mathcal O})$，精确按以下步骤应用 $\Theta^{-1}\bmod\ell$：

1. 置 $\lambda^{\rm out}_{\mathcal O}=b_{\mathcal O}$，其余坐标零。
   对每个20维块，用(D19)及整数 $J^{-1}$ 得
   $\chi_m^{\rm out}=(246^3\kappa^{m+1})^{-1}J^{-1}\lambda_m^{\rm out}$。
2. 用(D10)--(D13)求该向量对前两组方程的贡献，将其从
   $(b_A,b_P)$ 中减去，得到 $(\widehat b_A,\widehat b_P)$。
3. 只读旧模逆，作
$$
u_0=F_0^{-t}\widehat b_A,\qquad
t=S^{-t}(C_{J,P}^tu_0+\widehat b_P),\qquad
u=u_0+F_0^{-t}F_I^tt.
\tag{D20}
$$
   令 $\lambda_J^{\rm sel}=u$、$\lambda_{R[I]}^{\rm sel}=-t$，其余为零。
4. 对 $\lambda=\lambda^{\rm out}+\lambda^{\rm sel}$ 再使用
   $\chi_m=(246^3\kappa^{m+1})^{-1}J^{-1}\lambda_m$，输出所求解。

由原 $M$ 的逐块乘法，(D20)确实解
$M^t(u,-t)^t=(\widehat b_A,\widehat b_P)^t$。
因此以上是一个实际已有数据上的模求解公式，不是要求调用一个未生成的准确 $M^{-1}$。
十四分支的结果再用原 `inverse_evaluation_matrix` 回到同一个
$(B^0,\ldots,B^6,sB^0,\ldots,sB^6)$ 次序；每个 $t$ 系数都使用同一既有矩阵。
旧 `A_inverse_over_Q_computed=false` 始终保留。

## 7. 确定性提升与准确终止，不声称快速

所有原算子系数的有理分母都在该 $\ell$ 为单位；这须由实际来源逐项核验。
于是(D14)是原 $\mathbf Z_\ell$ 整阶上的单位线性算子。
先用§6解模 $\ell$ 的(D16)，得到新 dual current $\chi^{(1)}$。

若已知模 $\ell^n$ 的代表 $\chi^{(n)}$，用正乘公式(D10)--(D13)
在模 $\ell^{n+1}$ 下求正残差
$$
\Theta\chi^{(n)}-d(e^t,-qE_P^t,0).
\tag{D21}
$$
先逐个原整数坐标核其可除 $\ell^n$，再除掉 $\ell^n$，
将所得模 $\ell$ 向量的**负值**送入§6；得到下一位修正。
不能先把整残差在分支模 $\ell$ 评价而丢掉待除的一层。
完成修正后完整核(D16)模 $\ell^{n+1}$，再原子提交新 current。

按固定的有限间隔尝试严格有理重构，共 $2560\cdot14=35840$ 个有理坐标。
只有全部坐标恢复后才进行准确(D16)乘回，最后准确求(D17)。
若重构未成或准确乘回不符，只继续同一 RHS 的下一位；不把它解释为原候选错误。

**命题 D.2。** 在无外部预算限制、精确整数算术可继续的意义下，该算法严格终止，并对给定 $q$ 给(D1)的准确是/否答案。

**证明。** 命题 D.1给唯一 $\chi\in L^{2560}$。在固定十四维有理基中，它有有限个有理坐标；(D16)的整目标和模单位性使各坐标在 $\ell$ 整。对每个既约分数 $a/b$，存在有限 $n$ 使标准唯一重构条件 $2|a|b<\ell^n$ 及采用的严格矩形界同时成立。有限多个坐标可取共同 $n$。逐位提升唯一逼近该解，故在某次尝试全部恢复准确，并通过完整(D16)。此后(D17)是有限的准确数域运算，必能判其为零或非零。再由(D18)给结论。$\square$

这不是 dual 高度上界，也不是现实时间承诺。未知量35840个有理坐标，
比只用2420个 $L$ 行的直接转置多140个 $L$ 块；新增这些块换来
不生成高精度 $\kappa^{-1}$ 或准确大 Schur 矩阵的清残差路径。
旧518位 primal current 不是这份新 RHS 的518位解，不能冒称从518位续起。
确定的复用只是原矩阵/前缀/完整十四个模逆，不保证新 witness 比 primal 更短。

## 8. 实际输入形状与最小实施契约

| 输入 | 原形状或实际字段 | 作用 |
|---|---|---|
| 原 R787 rational-blocks | A 选行1234、补行1326、`A_inverse_mod_prime` 1234平方、原20行稀疏 $Z$ | 固定单位图及(D20) |
| 原 chart | rank1186、1186个选行/选列、free1186 | 固定 $\mathcal S,\mathcal O,P,f$ |
| 同一 selection | 十四个原根、评价及逆评价矩阵、全部分母/κ单位 | 同一原 $L$ 的分支与坐标回收 |
| 十四个 complete branch | `Schur_minor_inverse_mod_prime` 1186平方、`C_J_pivot_columns` 1234×1186、128个20维 `inverse_original_clear_multipliers` | 只读模求解器；不重新选支、求逆或 LLL |
| 原1234条 real-power5 行 | 每条129×20，原尺度/次序 | 两个准确转置矩阵乘法及其模版本 |
| 原 R781 carrier | 字段、$R_0..R_{128}$、$\kappa^0..\kappa^{129}$、同一个 $g(t)$ | 正乘、反向卷积与配对 $J$ |
| 原 R840/R841 carrier | 准确 $e_0,e_0Z$、原候选 $q$、原 $B_0$ 非零和单位图身份 | 目标 RHS 及最终原值解释 |

原大数据可从已结束的 R787 run `43737413555`、source
`4092d1cc4d1156bc24a10ff820fd39c5713e8ad7` 的实际 manifest
`7a22beb22912c1d5c4c56a5faa577a529f6c5dab5bb4ea5251e9cd5c4264ba3f`
选取。新任务不需要下载其大 `dixon-00000518` current；但必须实际取得
上述十四个 complete branch，不能假设它们在目前约1MB的 CM 小载体内。
父 run 可因预算结束；消费的是其同标签、逐 SHA 核过的 complete 阶段，不伪造成功父证书。

推荐独立 scope 顺序：

1. 仅新的配对 $J,J^{-1}$、选行补集140项及目标 $d(e,-qE_P,0)$。
2. 完整十四分支的新转置首 RHS；准确乘回其模 $\ell$ 身份。
3. 同 RHS 的增量 current；每次完整模乘回后原子写入，旧位只读。
4. 准确坐标候选及(D16)全乘回；成功后只追加(D17)的一项接受/拒绝证书。

新的模转置及准确 verifier 共用同一个清算子函数，分别给定模整数或准确有理后端。
按 $j$ 和原列分块保存完整结果；反向卷积与后续矩阵乘法的数组不得全部重复嵌入每个 receipt。
每个 current 绑定 source/core/proof、旧 chart/全部分支 SHA、目标 $q$ 和 $d$；
预算与最大追加位数只作运行控制，不改变数学身份。

只有(D16)、(D17)真正完成且 $\Delta=0$ 才输出
`original_value_rowspace_zero_A1_proved=true`。
若小域(A.2)--(A.3)也实际通过，后继才接受准确 $x,y,y'$；
否则只接受(D1)已经证明的那个 $y$ 值。
原非挠和 Hom 字点值 DAG 不依赖本任务，继续使用它们已有的准确表达式。

所有新增算术仅公开 Actions。源码、参数、纸面证明和简明 run/SHA 登记可入 Git；
机器回执、向量、current 与算子数组仅在一日 active artifact/carrier 续传。
