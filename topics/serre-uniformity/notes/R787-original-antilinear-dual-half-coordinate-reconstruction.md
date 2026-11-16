# 原单值转置证书的半线性奇偶性：半数坐标提升、严格拒证与原 current 继承

日期：2026-11-16。状态：**以下原来源上的降维命题及消费算法已证明；没有运行新的对称性检查、分支求解、有理重构或零判。** 原正在运行的完整 dual 核保持不变。本篇不把已通过的七项小数域条件重新当成原点接受证书。

目标仍是原短候选 $q$ 的唯一大身份
$$
A_0-qB_0=0.
\tag{HP.1}
$$
准确 $B_0\ne0$ 已由 R840 认证；$q$ 的反共轭身份已由原小数域消费者准确认证。本篇利用这个**已成输入**减少缺失的 row-space 证书未知量，成功出口仍为原全部准确转置方程和原自由列的零障碍。

## 1. 三种坐标与共轭分别固定

记
$$
\varsigma=1+2\zeta,\quad\varsigma^2=-3,\quad
F_b=\mathbf Q(b),\quad L=F_b(\varsigma),\quad
\mathscr T=L[t_\xi]/g(t_\xi),\quad\deg g=20.
\tag{HP.2}
$$
原程序中的字段 `s` 就是此处的 $\varsigma$；本篇不将它用于局部参数。$t_\xi=\xi+\xi^{-1}$ 是原实圆分坐标，不是原商参数 $a^3$，也不是 CM 参数 $z=a-1$。不额外声称 $F_b$ 全实。

以 $c_{\rm coef}$ 表示固定 $b,\xi$、把 $\varsigma$ 变为 $-\varsigma$ 的系数共轭。它固定 $t_\xi$。原全局共轭 $c_Y$ 在同一个原 $v=\xi^{-10}q_Y$ 展开上由 [R802(802.11–12)](../results/R802-original-semilinear-parity-and-degree-seven-relations.md) 给
$$
[v^n](c_YF)=(-1)^n c_{\rm coef}([v^n]F).
\tag{HP.3}
$$
不能以固定 $L$ 的 $\xi\mapsto\xi^{-1}$ 代替 $c_{\rm coef}$。

同一原 R802 给
$$
c_Y(y)=-y,\quad c_{\rm coef}(\kappa)=\kappa,\quad
c_{\rm coef}(R_m)=(-1)^mR_m.
\tag{HP.4}
$$
原整数配对矩阵
$$
\mathsf J_{rs}=[t_\xi^{19}](t_\xi^rt_\xi^s\bmod g),\qquad 0\le r,s<20,
\tag{HP.5}
$$
及其已成整数逆均被 $c_{\rm coef}$ 固定。本篇的 $\mathsf J$ 是转置配对；下文 $J_A$ 才是原1234个选行，不混用两者。

候选已准确满足 $c(q)=-q$，故写成 $q=\varsigma Q$、$Q\in F_b$。这仍不能独立证明(HP.1)。

## 2. 同一个原 CM 评价是等变的

令 $V=H^0(Y_L,5H)$，$\dim_LV=1234$，并令
$$
W=\{B\in V:\text{原全部20个 cusp 的常数块为零}\}.
$$
原准确 $Z$ 给 $B=Zc$，$c\in L^{1214}$；$W$ 在 $c_Y$ 下稳定。这里仅使用原常数块条件和(HP.3)，不需要生成 $c_Y$ 在原1234基上的大矩阵。

原 CM 评价 $e(F)$ 是在 $P_1=\phi(c_1)$ 的同一局部框架下评价：
$$
\Psi_F=F(E_6/E_4^2)^5,
\tag{HP.6}
$$
保留 $F$ 的原 $82^{10}$ 尺度。R790 的正则化和 R837 的实际运输都使用这个框架。原 $E_4,E_6$ 对 $T^{41}$ 不变；标准算术结构也固定它们。因此(HP.6)的框架在原 $c_Y$ 下固定；[R616 §1](../results/R616-original-CM-point-difference-and-explicit-height-basis.md)给 $c_1$ 及 $P_1$ 为原有理点，故
$$
e(c_YF)=c(e(F)).
\tag{HP.7}
$$
这不把几何反射 $P_1\mapsto P_0$ 当成逐系数共轭，也不附加新的 $g_\star$、$\zeta$、$\eta^{12}$ 或 CM period 因子。

定义半线性作用及评价泛函
$$
\mathfrak c(A,B)=(c_YA,-c_YB),\qquad
\mathcal E_q(A,B)=e(A)-q e(B).
\tag{HP.8}
$$
由(HP.4)、(HP.7)及 $c(q)=-q$，
$$
c_Y(A-yB)=c_YA-y(-c_YB),\qquad
\mathcal E_q(\mathfrak c(A,B))=c(\mathcal E_q(A,B)).
\tag{HP.9}
$$

## 3. 原选行支撑不混坐标，唯一 full-row 证书被迫具有奇偶性

沿原未清分母矩阵，令
$$
\mathcal A(A,B)=\bigl([v^n](A-yB)\bigr)_{0\le n\le127}
                 \in L^{2560},
\qquad \mathcal A=(F_A,-C).
\tag{HP.10}
$$
每个 $n$ 后面是完整 $t_\xi^0,\ldots,t_\xi^{19}$ 的二十坐标。$B\in W$ 已使 $v^{-1}$ 条件准确为零，原129阶全球注入界仍完整保留。

[R824实际 Schur 子式及 RR 结论](../results/R824-certified-original-pole-module-splitting-from-Schur-minor.md)给
$$
\operatorname{rank}_L\mathcal A=2420,\qquad
\ker\mathcal A=\{(yB,B):B\in H^0(5H-E_y)\},
\quad\dim_L\ker\mathcal A=28.
\tag{HP.11}
$$
这里不以模满秩猜测特征零核。原真实1186阶 Schur 子式给下界，原零次数界及 RR 给另一方向。

令 $J_A$ 为原1234个 A 选行，$R[I]$ 为原1186个 Schur 选行在完整2560行中的实际编号，
$$
\mathcal S=J_A\cup R[I],\qquad
\mathcal O=\{0,\ldots,2559\}\setminus\mathcal S.
\tag{HP.12}
$$
原单位子式使 $\mathcal S$ 为 $\mathcal A$ 的一组真实行基；$|\mathcal O|=140$。

在行坐标上定义
$$
\mathfrak d(x)_{n,r}=(-1)^n c(x_{n,r}).
\tag{HP.13}
$$
由(HP.3)，$\mathcal A\mathfrak c=\mathfrak d\mathcal A$。尤其 $\mathfrak d$ 只在每个原编号上乘 $\pm1$ 和共轭，不混合 $n$ 或 $t_\xi$ 坐标。因此任何按原编号指定的零支撑，包括 $\lambda_{\mathcal O}=0$，都被保留。这一步不要求 $\mathcal S$ 在某个未知1234维 involution 矩阵下不变。

**命题 HP.1。** 若(HP.1)成立，则存在唯一支撑于 $\mathcal S$ 的 full-row 证书
$$
\lambda^t\mathcal A=d\mathcal E_q,\qquad
\lambda_{\mathcal O}=0,
\tag{HP.14}
$$
其中 $d$ 是原 dual 目标已选的正整数清分母。它满足
$$
\boxed{c(\lambda_{n,r})=(-1)^n\lambda_{n,r}.}
\tag{HP.15}
$$

**证明。** (HP.1)及原 $B_0\ne0$ 给 $q=y(c_1)$，故 $\mathcal E_q$ 消灭(HP.11)的整个核，而不只是指定自由列1186的一条关系。线性代数于是给行空间证书；行基 $\mathcal S$ 给支撑规范及唯一性。

若 $\lambda$ 满足(HP.14)，则 $\lambda^\sharp_{n,r}=(-1)^n c(\lambda_{n,r})$ 也满足它：对任意 $u=(A,B)$，使用(HP.9)、(HP.13)可得
$$
(\lambda^\sharp)^t\mathcal A(u)
=c\bigl(\lambda^t\mathcal A(\mathfrak c u)\bigr)
=c\bigl(d\mathcal E_q(\mathfrak c u)\bigr)
=d\mathcal E_q(u).
$$
其零支撑仍是 $\mathcal O$，由唯一性 $\lambda^\sharp=\lambda$，即(HP.15)。$\square$

必须保留命题的条件性：对任意反固定的 $q$，只求原选定方阵的前两组等式，所得向量未必满足(HP.15)。本篇不预设这个假命题。

## 4. 清转置未知量准确减半

沿[无逆清转置证明](R787-original-inverse-free-cleared-transpose-value-acceptance.md)(D10)，原行块 $n=m-1$ 与清未知量的关系是
$$
\lambda_{m-1}=246^3\mathsf J(\kappa^{m+1}\chi_m),\qquad1\le m\le128.
\tag{HP.16}
$$
原 $246,\mathsf J,\kappa$ 均在 $c_{\rm coef}$ 下固定；它们在原域中可逆。由命题 HP.1，若(HP.1)成立，则
$$
\boxed{c_{\rm coef}(\chi_m)=(-1)^{m-1}\chi_m,
\qquad\chi_m=\varsigma^{(m-1)\bmod2}\widehat\chi_m,
\quad\widehat\chi_m\in F_b(t_\xi).}
\tag{HP.17}
$$
原字段次序是
`B^i*s^j*t^r, j=0..1 outer, i=0..6, r=0..19 inner; B=lambda*b`。
因此 $m$ 为奇数时只保原0至139坐标，$m$ 为偶数时只保原140至279坐标。
原 $\lambda$ 的局部阶数是 $m-1$，不能把此奇偶性整体错一位。

由此实际待恢复有理坐标数从 $128\cdot280=35840$ 减到
$$
128\cdot140=17920.
\tag{HP.18}
$$
准确成功时仍可将这些坐标嵌回原128×280数组，已知另一半准确为零，再用原完整 verifier。没有删去二十个 cusp 方向，也没有更换原 $B=\lambda b$ 或扭曲模型。

### 正乘与反卷积也可保持同一半字段

写 $\widehat R_a=R_a/\varsigma^{a\bmod2}$。这些是 R802 已证明的原 $F_b(t_\xi)$ 元素，不重新 Laurent 递推。原
$$
U_j=\sum_{m=\max(1,j)}^{128}R_{m-j}\chi_m
=\varsigma^{(j+1)\bmod2}\widehat U_j
\tag{HP.19}
$$
有准确的无逆公式
$$
\widehat U_j=
\begin{cases}
\displaystyle\sum_m\widehat R_{m-j}\widehat\chi_m,&j\text{ 偶},\\[3pt]
\displaystyle\sum_{m\text{ 奇}}\widehat R_{m-j}\widehat\chi_m
-3\sum_{m\text{ 偶}}\widehat R_{m-j}\widehat\chi_m,&j\text{ 奇}.
\end{cases}
\tag{HP.20}
$$
所有和的范围仍为 $\max(1,j)\le m\le128$。$j=0,128$ 两端均保留；不存在额外 $\chi_0$。随后 $V_j=\mathsf J\kappa^jU_j$ 有相同奇偶性。式(HP.20)中的 $-3$ 来自唯一的 $\varsigma^2=-3$，不可丢失。

这给一个可选的140维字段正乘实现。首个消费者也可以直接沿用旧280维算子、把禁用半块置零，只减少七支求解和 RR。两种实现的最终身份都必须回到原完整 $\Theta$；本篇不声称任意目标都落入一个已经构造的2560维 $F_b$ 方阵。

## 5. 模单位性使有限反例真正拒绝 q

令 $\mathcal O_\ell$ 是原积分 $B$、$\varsigma$ 坐标在 $\mathbf Z_\ell$ 上的整阶，$\ell=1000000753$。旧 selection 已证明原 $B$ 七根和 $\varsigma^2+3$ 两根不同，因此
$$
\mathcal O_\ell\simeq\mathbf Z_\ell^{14}.
\tag{HP.21}
$$
旧原十四分支的 A minor、Schur minor、$246$、$\kappa$ 均为单位。由原命题 D.1，清算子 $\Theta$ 在 $\mathcal O_\ell$ 上可逆。原目标
$$
b_q=d(e^t,-qE_P^t,0)
\tag{HP.22}
$$
已经在原十四整数坐标中整。因此无论(HP.1)真假，方阵方程
$$
\Theta\chi=b_q
\tag{HP.23}
$$
都有唯一 $\ell$-整的准确解；模每个 $\ell^n$ 也唯一。

**命题 HP.2。** 设一个来源完整的 current 已在全部原35840坐标认证(HP.23)模 $\ell^n$。若其在(HP.17)禁止的半块有一个非零剩余类，则(HP.1)不成立。

**证明。** 若(HP.1)成立，命题 HP.1及(HP.16)给该唯一准确解的禁用半块为零；由(HP.21)–(HP.23)的模唯一性，任一正确 current 的相应剩余类必须为零，矛盾。$\square$

这里所需的是**正确、完整认证的原方阵解**。普通 RR 候选的错误残差、缺失分支、IO来源失败、或一个未满足原方程的数组，都不能按此命题拒绝 $q$。这个拒证也不依赖给 dual 坐标猜测高度。

## 6. 每一新数位只用七个已有逆，仍完整认证十四分支

原14根按相同 $B$ 根和 $\pm\varsigma$ 成七对。选择一个原 $\varsigma$ 根，对七个 $B$ 根各取一个原分支；另一支不另解大线性系统。选择过程和原 branch ID 必须在公开 Actions 记录。

假设已成 $\chi^{(n)}$ 满足原全部模方程和(HP.17)。沿旧核心求**正残差**，先在原整数坐标除去 $\ell^n$：
$$
r_n=-\frac{\Theta\chi^{(n)}-b_q}{\ell^n}\pmod\ell.
\tag{HP.24}
$$
完整可除性必须先核，不能先在某分支模 $\ell$ 求值。

对七个代表分支，直接读原 `A_inverse_mod_prime`、`Schur_minor_inverse_mod_prime`、`C_J_pivot_columns`、`inverse_original_clear_multipliers`，使用原(D19)–(D20)的转置解法取得 $\delta_m$。对其配对的另一支规定
$$
\delta_m(B_i,-\varsigma_*)=(-1)^{m-1}\delta_m(B_i,\varsigma_*).
\tag{HP.25}
$$
再用旧 `inverse_evaluation_matrix` 回到原十四坐标。这里不求新的7×7或14×14逆；插值的非零半块是原 $B$ 坐标，另一半必须为零。

此后执行完整检查
$$
\Theta\delta=r_n\pmod\ell
\quad\text{全部2560×14坐标}.
\tag{HP.26}
$$

- 若通过，提交 $\chi^{(n+1)}=\chi^{(n)}+\ell^n\delta$。原方程完整成立，奇偶性保持。
- 若不通过，只有在七个代表分支确实解了原 RHS、全部来源及原 current 已认证时，才把非零原残差登记为 **(HP.1) 的严格反证**。

第二点的证明不是“候选残差非零”。若(HP.1)成立，准确 $\ell$-整解与旧 current 之差可除 $\ell^n$，其下一位仍有(HP.17)的奇偶性。七个单位分支的唯一解必为(HP.25)所补的下一位，故它必通过(HP.26)。反例因而不可能来自真 $q=y(c_1)$。

初始一步可取 $\chi^{(0)}=0$、$r_0=b_q\bmod\ell$，沿同一方法处理。不假设任意反固定 $q$ 都能通过这个首步。

## 7. 准确接受与严格终止

只对17920个保留坐标尝试原严格 RR；恢复后将禁用半块准确补零。准确接受继续执行原完整
$$
\Theta\chi=b_q,\qquad
\Delta=(H_B^t(\mathsf J\chi))_f+dqE_f,
\quad f=1186.
\tag{HP.27}
$$
由原(D18)，$d(A_0-qB_0)=-\Delta$。因此完整第一式成功后，只有 $\Delta=0$ 才接受原值；$\Delta\ne0$ 则严格拒绝。RR失败或其准确乘回失败只表示继续，不使用命题 HP.2 的标签。

**命题 HP.3。** 在无外部预算限制的精确算术意义下，上述半坐标算法对当前反固定候选严格终止。

**证明。** 取(HP.23)的唯一准确有理坐标解。若它没有(HP.17)的奇偶性，则某禁用坐标是非零 $\ell$-整数，在有限精度下可见。七支补全算法不可能无限保持全方程，否则模唯一性迫该坐标在任意精度都为零。因此有限步发生(HP.26)的严格拒证。

若该唯一解满足奇偶性，则所有步骤均为它的准确提升；有限个保留有理坐标在足够精度满足严格 RR 的充分界，故最终恢复并通过原全部(HP.27)，再由 $\Delta$ 给准确答案。这里没有宣称该充分精度小于旧完整 dual，更没有把原 primal 的518位当成新 dual 位数。$\square$

## 8. 已成 current 的条件式继承：不重旧位、不改旧 tag

本篇尚未取得一个停止后可消费的新 dual current，故不预填 run、artifact、digits 或 SHA。来源必须是原 **cleared-dual** 运行的完成阶段，不能取原 primal `A_L_coordinates/C_L_coordinates` 替代。

冻结核心的真实 current schema 是：

| 字段 | 必须保留的含义 |
|---|---|
| `prime`, `digits`, `modulus` | 原 $\ell$ 和准确 $\ell^n$，新 dual 自己的数位 |
| `chi_integer_coordinates` | 原128×280、整数代表均在 $[0,\ell^n)$ |
| `exact_target` | 同一个已成 $q,d,e,eZ$ 目标阶段的真实 spec |
| `full_square_modular_identity_verified` | 已完成的全部35840坐标模方程为真 |
| `previous_completed_checkpoint_sha256` | 原 current 历史链，不换成 primal 来源 |
| `configuration` | 旧核心/全部原源/配对来源/目标策略的原身份 |

新消费者把这个 current、其目标、原 source audit、run/core/public 回执和完整 manifest 作为单独外源保存；旧字节及旧 configuration 原样保留。逐项核同一个原 $B,\varsigma,t_\xi$、$\kappa/R$、全128原块、$Z$、$\mathcal S,\mathcal O,P,f$ 及原目标 $q,d$，不重新清 content 或分母。

由于原整数代表已在 $[0,\ell^n)$，检查禁用半块是否全为字符串整数0即可记录本精度奇偶性；此新检查仍只在公开 Actions 执行。若存在非零项，按命题 HP.2保存原索引、来源和真实剩余类作严格拒证。若全零，将允许的140坐标逐块保留，登记独立新身份的 import spec，然后只计算第 $n+1$ 位。

不重新调用旧 `initial_current()`，不重算旧 $\mathsf J,\mathsf J^{-1}$、旧前缀、原十四逆、旧 CM 响应或原 $n$ 位残差。已经实际失败的 RR 尝试也不在同一数位重复；后继从下一个新增数位按新策略继续。原 source bound 证明只允许这种明确继承，不能伪装新核心为旧核心或改写旧 current 的 tag。

## 9. 节省与范围

确定的节省是：准确未知坐标减半、每位只需七个原分支的大转置求解、RR只恢复保留半块；正乘还可用(HP.20)进一步减少字段算术。原128块、二十 cusp 坐标、完整十四分支输出和最终自由列障碍始终保留。

这不是另一组局部必要条件接受捷径，也不是新的候选搜索。它以原完整单位算子为基础，给对指定 $q$ 可严格终止的较小准确证书算法。当前完整 dual 不因此重启；只有真实新 current 到达、完成来源认证之后才可作新的消费者。

所有新算术只在本公开仓库 Actions。Git仅保存源码、参数、纸面证明与简明 run/SHA 登记；机器向量、残差、模逆和来源回执仅在一日 active artifact/carrier 中续传。

## 原来源

- [R802](../results/R802-original-semilinear-parity-and-degree-seven-relations.md)：真实扭曲共轭、同一 $v$ 参数、$\kappa/R$ 奇偶性。
- [R824实际原 Schur 秩](../results/R824-certified-original-pole-module-splitting-from-Schur-minor.md)：完整核28、原行秩2420及十四合法分支。
- [R790原 CM 框架](../results/R790-original-CM-fiber-regularization-and-155-jet-evaluation.md)与 [R837原框架运输](R837-original-fixed-branch-pencil-method.md)：$E_4,E_6$ 固定与原 $E_6/E_4^2$ 正则评价。
- [原单值接受稿](R787-original-short-CM-candidate-exact-acceptance.md)、[无逆清转置证明](R787-original-inverse-free-cleared-transpose-value-acceptance.md)：原负号、选行、单位 $\Theta$、完整接受和自由列障碍。
- [已成七项小数域检查](R792-CM-candidate-small-field-ended-and-A1-boundary.md)：只提供本篇所用准确 $c(q)=-q$；未代替(HP.1)。
