# R207：完整权 −6 pure 像等于三维响应像

日期：2026-11-15。作者与数学责任：tail_cost；公开源码、参数与实际回执由本课题 root 合并、调度和复核。

**已证明，并由公开 Actions 的完整原式消费给出准确有理证书：**

$$
\boxed{
\pi(U_{-6})=\pi(R_{-6}),\qquad
\dim\pi(U_{-6})=\dim\pi(R_{-6})=3.
}
\tag{1}
$$

这里 $\pi$ 是全部 universal pure profile 函数的投影，保同一右锚、所有原函数常数及任意合法 profile；不是 $q=(c-\xi)^8$ 的幂尾投影。结合 [R203](R203-general-pure-lowest-two-weights-vanish.md) 与 [R202](R202-pure-cost-cone-and-three-remaining-negative-character-weights.md) 的纯锥论证，尚未排除的非零 pure 正仿射字符只可能有权

$$
\boxed{\sigma=-4.}
\tag{2}
$$

(1) 不宣称完整两模式的 $U_{-6}=R_{-6}$，不宣称整个 pure 闭锥已经满，也不支付 mixed period、ruling 或主课题完成。

## 1. 对象、归一和三条准确响应基

沿用 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的有限真实 canonical 成本空间

$$
U=\mathcal U_4,\qquad
R=\mathcal R_8
=\operatorname{span}\{\mathcal B_E(T):E\in E_8,\ T\in W\}.
\tag{3}
$$

真权采用 $P_{H,0}$ 的有限 Laurent 表示。第三势的几何导数权 $0,2$ 与第四局部密度的几何导数权 $0,2,4$ 均不与这个真 profile 权混淆。

本实际读取的是 canonical 相位 $-4$ 的原系数。以下 $\rho_j$ 使用该原系数归一；若把 $\pi$ 记为 R198 的单实 profile 成本，则对本页所有 pure 成本和 $\rho_j$ 同时乘同一个 $16$，(1)、所有成员性及坐标关系完全不变。

[R144](R144-seventh-G-translation-and-230-query-control.md) 已给完整 $R_{-6}$ 的 16 条真实两模式基，来自原 20 列，保留原索引

$$
(0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17).
\tag{4}
$$

本次没有重建这些响应、重跑它们的旧四条原依赖或原评价 minor；仅读其已经公开保存的 pure 原根。得到的 pure 基是

$$
\boxed{
\rho_0=\bigl(\mathcal B_{p_0}(W_{18})\bigr)_{-4},\quad
\rho_2=\bigl(\mathcal B_{r_0}(W_3)\bigr)_{-4},\quad
\rho_3=\bigl(\mathcal B_{r_0}(W_4)\bigr)_{-4}.
}
\tag{5}
$$

$W_{18},W_3,W_4$ 均为冻结 v2 模板原索引；没有在本稿重新编号。其第三真权分别为 $-5,-3,-3$，参数真权分别为 $-1,-3,-3$，故全部总权为 $-6$。

三条 pure 原根身份是：

| R144 原索引 | 完整参数 / 第三模板 | pure 原 SHA-256 |
|---:|---|---|
| 0 | $p_0,\ W_{18}$ | 8db244a0f831835f7f2016a2ab49839a06266fab548ad097b5c920dcf7108900 |
| 2 | $r_0,\ W_3$ | bd99694b03f159ea38c10af4809ce97844903b55894b80621216294bcdf8b619 |
| 3 | $r_0,\ W_4$ | ad2991534f5b50aa2dd86836603bf4e00ce47d68a00fddf2cbe102b025ff6379 |

完整两模式的 16 维没有被当作 pure 的 16 维。pure 的三维性是本次新共同矩阵的实际结论；此外旧 R144 的可逆 $16\times16$ 原评价矩阵中，已经含有三条 pure 行：$t=1/25$ 的实、虚部分和 $t=2/25$ 的实部分。可逆矩阵任意行子集独立，故该旧证据也单独给出 $\dim\pi R_{-6}\ge3$，与本次上界一致。

## 2. 本次覆盖的是全部十四族

[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) 与 [R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md) 已证明

$$
U=R+\operatorname{span}
\{\text{完整十四族正规状态系数值}\}.
\tag{6}
$$

十四族为

$$
F_0,\quad Q_{2,0},Q_{2,1},Q_{2,2},\quad
\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2,\quad
Q_{4,0},Q_{4,1},Q_{4,2},Q_{4,3},Q_{4,4}.
\tag{7}
$$

程序没有以“只看静态”“只看最高加速度”或某个单列代替 (7)。本次所用完整代表中，权 $-6$ pure 的非零原状态系数共有 241 条：

| 完整族 | 原状态系数条数 |
|---|---:|
| $F_0$ | 58 |
| $Q_{2,0}$ | 19 |
| $Q_{2,1}$ | 27 |
| $Q_{2,2}$ | 32 |
| $\bar A_{hh}$ | 16 |
| $\bar A_{hk}$ | 12 |
| $\bar A_{kk}$ | 9 |
| $H_1$ | 12 |
| $H_2$ | 9 |
| $Q_{4,0}$ | 4 |
| $Q_{4,1}$ | 6 |
| $Q_{4,2}$ | 9 |
| $Q_{4,3}$ | 12 |
| $Q_{4,4}$ | 16 |
| 合计 | 241 |

仅按**原表达式完全相同或有理成比例**合并后，有 164 个不同的 normalized original columns；241 个 family/state 别名与比例全部在公开 job 日志逐列给出。241 和 164 都是原呈示计数，不是函数维数。

这 164 列与 (4) 的 16 条 pure 响应一起形成 180 列完整新目标。共同函数矩阵只有三条独立原列，即 (5)，其余

$$
180-3=177
\tag{8}
$$

条准确原式关系全部验证为零。164 条 normal 列都落在响应三维像中，没有未完成的新商方向或未决余式。其中 normalized original columns 36 和 163 的非零原表达式实际表示零函数，坐标是空组合；它们仍计入上述原呈示，而不被当作两个不同的非零函数。

## 3. 为何这些较小输入仍是完整原目标

详细源码装配见 [已公开设计](../notes/complete-pure-minus6-projection-design-20261115.md) 和 [新消费者](../scripts/literature_complete_pure_minus6_projection.py)。这里重述完整性所需的数学步骤。

### 3.1 真权选择来自完整协变

完整原几何键顺序是

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}),
\qquad
\kappa(a)=a_0-a_2+a_3+a_5+a_8.
\tag{9}
$$

[R190](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md) 从真实历史 RHS 证明 $v_2,v_4$ 严格缩放协变。不同 $H^\kappa(\log H)^j$ 的有限指数多项式独立性使本权只需 $\kappa=-6$ 的原系数再作真 profile 权投影。这不是从几何指数标签直接猜测 profile 权。

对势，R190 已付

$$
[N^{[2]}(S_H;Hu,w)]=P_H[N^{[2]}(S;u,w)]
\quad\text{模 }W,
\tag{10}
$$

以及

$$
[N^{[0]}(S_H)]-P_H[N^{[0]}(S)]=C_H,\qquad
N^{[0]}(1,1,1)=0.
\tag{11}
$$

因此任意本次所需负第三权 $\sigma\ne0$ 的静态势在模 $W$ 中可准确取为

$$
\sum_{\substack{\kappa(a)=\sigma\\a_7=0}}
\bigl(M_a(S)-M_a(1,1,1)\bigr)\Pi_\sigma N_a^{[0]}.
\tag{12}
$$

(12) 来自在 $S$ 与固定 $S_*=(1,1,1)$ 相减后比较指数多项式；它保留全部参考减项。三个涉及的非恒 log 单项只在模 $W$ 中为零，没有被伪称原式字面零。裸 $\log h$、零权常势例外不进入本次负权集合。

每个势代表变化为 $W$ 值，任何 $\mathcal B_E$ 收缩变化都在 $R$。故新正规代表与原代表仅差 $R$ 值状态系数；结合 (6) 仍给准确的完整 $U_{-6}$ pure 像。

### 3.2 只补新的 pure 收缩

110 个新势对角投影来自完整旧因子的原根；另外 12 个第三权 $-3$ 的 typed 投影直接复用已完成的旧缓存。这 12 个旧投影没有重算，旧权 $-2$ 的响应输出也没有冒充本权响应。

对内二槽对称、外槽保真的第三模板 $T$，设 $\tau(q)=T(q;q,q)$。完整 pure 响应准确为

$$
\mathcal B_E(T)_{-4}
=\frac18\bigl(D\tau(q)[E(q,q)]-2E(q,\tau(q))\bigr).
\tag{13}
$$

Fréchet 导数穿过所有真实同锚原函数；外槽没有被擅自与内槽对称化。式 (13) 已在公开九项新人工中，与完整三槽相位公式对一个外槽不对称的人工输入准确比对。

零对角及同原 SHA 合并后，实际新 pure 收缩为

$$
\boxed{134/134\text{ 完整完成}.}
\tag{14}
$$

相对于设计上界 205，这是精确零/同根合并后的实际请求数，不是按预算舍弃的结果。没有新 mixed 收缩。

### 3.3 低阶项与同一个八矩基准一起保留

使用的完整局部式为

$$
L_2=v_2-\mathcal B_{m_0}N^{[2]}-\mathcal B_{m_2}N^{[0]},
\qquad
L_4=v_4-\mathcal B_{m_2}N^{[2]}.
\tag{15}
$$

103 个 pure $v_2$ 原系数、160 个所需 $\beta/C/Q$ 的 pure $v_4$ 原系数，以及旧 197 个 pure 静态系数的本权投影均被完整消费。最后一项是本次新的权 $-6$ 静态投影，没有被遗漏在新工作统计之外。

五个 $\bar A,H$ 族共有 58 个已存本权原根，由 R134 的分层定理直接复用；不重复编它们。所有低阶项使用同一参考映射

$$
\Gamma(E)=\sum_{i=1}^{8}a_i(E)L_0(S_i^*),
\qquad
F_0=L_0-\Gamma m_0,
\qquad
Q_2=\operatorname{IBP}(L_2)-\Gamma m_2.
\tag{16}
$$

全部八个参考静态零值、原 $m_0,m_2$ 和参考逆矩阵均保留。第四速度项使用真实水平 $X,Y$ 微分，面积项 $H_1,H_2$ 不被省略。由此 (7) 是完整范围，不只是形式 raw 系数的部分筛选。

## 4. 共同原函数核如何认证 (1)

新转换统一使用 [R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md) 的固定颜色优先级算法。每个输入仅解码其必要原 atom 闭包，逐根核对旧原 SHA；不注册未选 mixed 分支，不改变右原函数常数。

180 列全部进入同一个新 pure word 字典，每个 surviving letter 通过 R179 余字语法检查。由 [R179](R179-universal-independence-of-fixed-color-remainder-words.md)，该字典在真实 profile 函数上单射。因此本次精确有理矩阵的核正是函数核，秩正是函数秩。

每条新依赖的证明不是只读取消元余数：

1. 保留当前原列非零系数和全部先前独立原列的准确有理坐标；
2. 从每个原列的完整已转换 word 向量重新相加；
3. 准确核对整个 word 和为零；
4. 独立形成同一有理组合的原 DAG 差，记录其 SHA 和项数；
5. 以逐列 R178 同锚转换身份的有理和组成原函数零证明。

这次没有为了每条关系再次对同一原差运行一套不同正规化；不存在混用旧不完备代表、或将新旧映射不相等误判为原式矛盾的问题。全部转换和关系在同一个已证 faithful 的字典中。

由完整 241 条正规系数均落在三维 $\pi R_{-6}$，(6) 给 $\pi U_{-6}\subseteq\pi R_{-6}$；反向包含来自 $R\subseteq U$。三条基独立，故得到 (1)。

## 5. 可直接阅读的两条原式身份与全部响应坐标

以 (5) 为基，R144 的全部 16 条 pure 响应坐标如下。下表是本次新的 pure 原函数关系，不是旧四条完整两模式依赖的重跑。

| R144 原列 | $\rho_0$ 系数 | $\rho_2$ 系数 | $\rho_3$ 系数 |
|---:|---:|---:|---:|
| 0 | $1$ | $0$ | $0$ |
| 1 | $3$ | $0$ | $0$ |
| 2 | $0$ | $1$ | $0$ |
| 3 | $0$ | $0$ | $1$ |
| 4 | $7/2$ | $0$ | $-5/2$ |
| 5 | $-10$ | $-8$ | $6$ |
| 6 | $-3$ | $-8$ | $5$ |
| 7 | $-6$ | $-3$ | $3$ |
| 8 | $-1/128$ | $3/128$ | $-1/64$ |
| 9 | $-3/128$ | $5/128$ | $-1/64$ |
| 11 | $0$ | $-5$ | $3$ |
| 12 | $-3/2$ | $-1$ | $3/2$ |
| 13 | $-3/256$ | $-1/128$ | $3/256$ |
| 15 | $3$ | $6$ | $-3$ |
| 16 | $-3$ | $3$ | $0$ |
| 17 | $-3/128$ | $3/128$ | $0$ |

两个直接来自旧完整加速度层原根的具体新身份为

$$
\boxed{
\bigl[\Pi_{-6}(\bar A_{hh})_{-4}\bigr]_{h^{-8}}
=\frac{6\rho_0+4\rho_2-6\rho_3}{2048},
}
\tag{17}
$$

$$
\boxed{
\bigl[\Pi_{-6}(\bar A_{kk})_{-4}\bigr]_{h^{-6}}
=\frac{-24\rho_0+8\rho_3}{16384}.
}
\tag{18}
$$

状态系数记号在此指其它 $k,\omega,\log h$ 幂均为零的项。它们是已存原 $v_4$ 正规加速度系数，未受势代表更换影响。

式 (17) 对应 normalized original column 0，其原 SHA 为 bc8855a1305314394bcbd3a309c77dafa7f03a195d9d64879d2e4dae4800b03f；family/state 别名的准确比例是 $1/2048$。式 (18) 对应 normalized original column 111，原 SHA 为 dc3f43304b64552fc7a3a17db7ba8650ff9f85b50a68fe0a5098405e3ee3ed69，比例为 $1/16384$。这说明日志中的归一化列和原族系数如何准确对应。

其余 162 条 normalized normal 原列及所有 241 个别名，也已在同一 job 的 MATHEMATICAL_COLUMN 行逐条打印完整有理坐标；并非只保存 hash 后无法阅读。文章保留可阅读的数学结论与代表身份；不把全部机器矩阵重新作为仓库数据保存。

作为一个直接维数推论，R144 的完整 $R_{-6}$ 真维数为 16，故

$$
\dim\ker(\pi|_{R_{-6}})=16-3=13.
\tag{19}
$$

本文没有计算完整两模式 $U_{-6}$ 的全部函数核，因此不把 241 或 164 减去 3 冒充 $\ker(\pi|_{U_{-6}})$ 的维数。

## 6. 对 pure 正字符和实际控制的准确影响

R202 的反证路径是：若 pure 成本闭锥为真子锥，有限仿射与 parity 作用产生一个非零单权 pure 正字符；它的拉回杀 $R$，并且必须杀 $\ker\pi$ 才能从完整 $U$ 下降。

若该字符权为 $-6$，它只读 $\pi U_{-6}$。由 (1) 这个空间完全等于 $\pi R_{-6}$，而后者已被它杀掉，矛盾。因此

$$
\boxed{\text{不存在非零的 pure 权 }-6\text{ 正仿射字符}.}
\tag{20}
$$

这不是对所有完整两模式权 $-6$ 正泛函的排除；一个不能经 pure 投影下降的 full 泛函不受本结论消去。

R145 已排奇权，R190 支付 $+2$，R188 排 full 权 $-2$ 正字符，R201 支付 pure 权 $0$，R203 消去 pure 权 $-8$。结合 (20)，剩余可能性严格缩为 (2)。

[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md) 已证明，只要剩余 pure 闭锥障碍全部排除，就能在真实共同 germ、frame/M/T 条件及全部固定桥成本下完成实际有限 pure 控制。本稿只支付其中权 $-6$ 的完整新门；没有提前使用尚未证明的权 $-4$ 结论。

## 7. 本仓库 Actions 的完整实际来源

- run：[43687004289](https://github.com/Rogerhu12/math-research-public/actions/runs/43687004289)；
- job：[132729516347](https://github.com/Rogerhu12/math-research-public/actions/runs/43687004289/job/132729516347)；
- source：28b2c1fdf6cd7f2743c4803e10dafdc35aaae5c5；
- lane：complete_pure_minus6_projection；
- 脚本：literature_complete_pure_minus6_projection.py，51380 bytes；
- 脚本 SHA-256：c57776cfc75ed437bf3b7f8cbcae45072b295892ecee6c93c6297519eee22c2e；
- 公开 metadata receipt：[本次回执](../notes/actions-43687004289-1-complete_pure_minus6_projection/receipt.json)，46559 bytes；
- receipt SHA-256：69b1e8797c09c54cf402f50d57b7ef8be52958cb96605acc7c852ca68e417277。

最终 source 的九项新人工在公开 Actions 真正全部通过，耗时 0.005744362999998032 秒，peak RSS 29.671875 MiB。随后真实完整消费完成：

| 实际项目 | 结果 |
|---|---:|
| pure 响应原列 | 16 |
| normalized normal 原列 | 164 |
| 原 family/state 系数 | 241 |
| 新共同矩阵总列数 | 180 |
| 准确原函数秩 | 3 |
| 完整验证原关系 | 177 |
| 新 pure 收缩 | 134 / 134 |
| 实际耗时 | 3.685329779 秒 |
| peak RSS | 317.1875 MiB |
| 精确整数操作 | 2338 |
| 最大整数位长 | 18 |

没有预算失败、未完成分支或降精度判断。其完整临时报告和内存证明身份是：

| 对象 | bytes | SHA-256 | 保存状态 |
|---|---:|---|---|
| 最终 source 的公开新人工摘要 | 8401 | aa1985d4a66c6d1e0a123f14cb5ea061732dfe53ee699b495dec7b13643dbc9e | 仅 runner 临时；receipt 记录 metadata |
| 完整数学摘要 | 44353 | ec68303004367ca70e5da4cf4e7b2bc91683a55283e00ce800bf89a6a6890852 | 仅 runner 临时；全部数学坐标直接 stdout |
| 完整证明 | 228675 | e3f615a07dd49dba0e2d5850815ef386a4be33d70fbe28de15cdf13915694af2 | 只在内存构造，未保存 |

遵守最新根 README §15，没有提交新数据/证书，没有 Release asset 或 artifact。metadata 的 SHA 本身不代替数学核验；(1) 的证据是上述全目标装配、同锚 sound 转换、R179 单射、完整原关系及公开实际逐列坐标。

实际参数为已发设计 §10 的五个旧输入目录及

    --max-seconds 240 --memory-mib 1024 --integer-bits 8192
    --max-terms 150000 --max-IBP-calls 600000 --max-cache-entries 300000
    --max-summary-bytes 95000 --max-certificate-bytes 8000000
    --output @OUT@/complete-pure-minus6-result.json

receipt 还记录发布前真实 pull 从 source 前进至 2e1aa88d3784bf2fe25064dadd01e1b69b55d68f，根 README 与课题 README 均无差，未 force。旧原根来自前述五份已经发表的输入；没有新的私人计算或仓库外 Actions。
