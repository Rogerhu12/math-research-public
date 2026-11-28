# R150 补充：全 W 同一 f 的十一条纯 λ,T 原条件实际完整返回

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 范围：当前已刊 W 权图、原 singleton 两值互异且物理 $D\ne0$ 的同点系统。全部既有权单位及规范化沿用下列先行定理。
- 状态：本篇登记首次真实计算给出的完整原理想表示及精确次数；不宣称 W 排空，不新增有限点数界。

## 1. 先行定理与本篇新增内容

[全图 f 唯一恢复定理](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md) 已在整个当前 W 图支付经完整原组合约消后的权首项，并给出

$$
R=f+g(\lambda,T)\in I_4,\qquad \deg_{\lambda,T}g\le2.
\tag{1}
$$

[纯 λ,T 原理想定理](R150-appendix-unit211-W-pure-weight-f-head-exact-lambda-T-original-ideal.md) 已证明同一 $g$ 下的完整消元机制。本篇固定源实际从正确 dual germ Gram 重建全部加权 N/P 和两个个别 N/P 奇部，再逐 $f$ 系数返回六源或十一源组合，得到该机制的完整具体十一式。没有把分别取根的必要行拼成一个虚假的共同解。

源为 [同一 f 的完整 I11 返回源](../notes/2026-11-28-unit211-W-same-f-entire-pure-lambda-T-I11-original-return-8542.py)，输入说明为 [首次输入范围](../notes/2026-11-28-unit211-W-same-f-entire-pure-lambda-T-I11-original-return-8542-input.md)。唯一小回执见 [实际执行与完整 checkpoint](../notes/2026-11-28-unit211-W-same-f-entire-pure-lambda-T-I11-original-return-8542-execution.json)。

本源没有执行旧六个标量、旧首项因式、旧 native 动作矩阵或冻结的 NV 返回门；必要的正确 Gram、首一 $q_f$ 和同一 $g$ 定义只为本次新原条件构造使用。

## 2. 同 f 的完整六式

令 $A_W$ 为当前已付纯权因子局部化后的 $\mathbb Q[e,k]$，所有下列式均在 $A_W[\lambda,T,f]$ 中。原四二次为

$$
I_4=(E_1,E_{B,e},E_{B,o},N_1).
$$

其中 $E_1$ 按真正 dual germ 乘法独立构造，未以加权 singleton 均值替代。已刊首一组合和三条原一次余式为

$$
q_f=f^2+q_1f+q_0,\qquad
r_i=A_i+B_i f\quad(1\le i\le3).
\tag{2}
$$

$q_f$ 与 $r_i$ 对原四式均有完整已付系数来源，且双向生成 $I_4$。把 (1) 代入定义

$$
P_0=g^2-q_1g+q_0,\qquad P_i=A_i-B_i g.
\tag{3}
$$

真正加权原式为 $\mathsf N,\mathsf P$。对每个 $F\in\{\mathsf N,\mathsf P\}$ 作首一短除

$$
F=Q_Fq_f+A_F+B_Ff,\qquad
\widehat F=A_F-B_Fg.
\tag{4}
$$

首次执行完整返回了

$$
\widehat F=F-Q_Fq_f-B_FR,\qquad
F=\bigl[Q_F(f+q_1-g)+B_F\bigr]R+Q_FP_0+\widehat F.
\tag{5}
$$

其六源系数均实际乘回，包括所有 $f$ 次系数。因此在同一个原系数环中有

$$
I_6=(E_1,E_{B,e},E_{B,o},N_1,\mathsf N,\mathsf P)
=(R,P_0,P_1,P_2,P_3,P_N,P_P),
\tag{6}
$$

其中 $P_N=\widehat{\mathsf N},P_P=\widehat{\mathsf P}$。这是真正原理想双向表示，不是假设任何生成环境自由，也不依赖两个 N/P 行各自的不同 $f$ 根。

本次实际还核出 $g$ 的分子双权次数 $(13,17)$、几何总次 $2$；其分母仅依赖权，双次数 $(11,16)$。源保留原 $3\times3$ 权矩阵的可能未付共同因子：先约消完整 $g$ 及四个原乘子，再核它们的最终分母全部已付，最后返回 (1)。没有将未经约消的原行列式强加为单位。

## 3. 个别原值与完整十一式

使用 [完整低 D 原值理想压缩](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md) 和 [纯 λ,T 的六四五原值定理](R150-appendix-unit211-W-pure-lambda-T-six-four-five-entire-value-equivalence.md) 的规范记号。设

$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3,\qquad
A_0=1+T/\ell.
$$

令 $n_o,p_o$ 分别为真正 $N_4(\mathrm{row}_B)$、$P_2(\mathrm{row}_B)$ 的 $\rho$ 奇部。对应两个完整低 D 条件为

$$
\begin{aligned}
N_{\rm low}&=D n_o+
2\lambda P_{02}\left(\frac{KA_0}{m}+\frac{2mD^2}{\ell M}\right),\\
P_{\rm low}&=D p_o+
P_{02}\left[
\frac{K}{2m}\left(3A_0^2+
\left(\frac{3m^2}{\ell^2}+\delta\right)\frac D M\right)
+\frac{6A_0mD^2}{\ell M}
\right].
\end{aligned}
\tag{7}
$$

对 $n_o,p_o$ 仍只作同一首一 $q_f$ 短除，而非直接把复杂三次式反复代入。若 $n_o=Q_nq_f+A_n+B_nf$，则

$$
\widehat N_{\rm low}
=N_{\rm low}-D Q_nq_f-D B_nR,
\tag{8}
$$

$P_{\rm low}$ 同理。首次执行对两个式子分别完整返回了全部十一源的 $f$ 系数，并核反向恒等式。此处 $D$ 只被正乘；没有求 $D$、$b_0$ 或任何几何首项的逆。

已刊完整值身份为

$$
2m\ell^2 V_{\rm low}
=N_5+\frac{2f}{MQ}C_4.
\tag{9}
$$

其尺度全为当前已付权单位。因此 (9) 保留的是整个原 $V_{\rm low}$，并非只保它某个分量。结合 (6)–(9)，在先行定理的同一物理适用域内，

$$
I_{11}
=\bigl(R,P_0,P_1,P_2,P_3,P_N,P_P,
C_4,R_6,\widehat N_{\rm low},\widehat P_{\rm low},N_5\bigr).
\tag{10}
$$

右侧除 $R=f+g$ 外的十一式都只依赖 $\lambda,T$。本次没有对原 $C_4,R_6,N_5$ 的既成值等价证明设置重新执行门，而是使用其已刊原来源，并新核本次两个个别 N/P 的同 f 返回。

## 4. 十一式实际参数与次数

下表记录首次输出的约分分子；分母均为已付纯权多项式。几何次数是 $\lambda,T$ 的总次数，不是分别次数之和。

| 条件 | 分子双权次数 $(e,k)$ | 几何总次 | 分子项数 |
|---|---:|---:|---:|
| $P_0$ | $(28,37)$ | $4$ | 9333 |
| $P_1$ | $(19,25)$ | $3$ | 2823 |
| $P_2$ | $(22,29)$ | $3$ | 3850 |
| $P_3$ | $(24,28)$ | $3$ | 3921 |
| $P_N$ | $(29,40)$ | $4$ | 10874 |
| $P_P$ | $(29,39)$ | $4$ | 10473 |
| $C_4$ | $(15,12)$ | $4$ | 1798 |
| $R_6$ | $(13,12)$ | $6$ | 2904 |
| $\widehat N_{\rm low}$ | $(28,38)$ | $6$ | 18934 |
| $\widehat P_{\rm low}$ | $(31,41)$ | $6$ | 22464 |
| $N_5$ | $(15,15)$ | $5$ | 3538 |

源实际检查了 71 个不同最终权分母，853 个精确多项式除法乘回及相应已付支撑乘回，8 次新的首一 $f$ 短除乘回。六源返回的累计 $f$ 系数计数为 6，十一源为 2；这两个计数是最终纯式返回的系数检查次数，不是遗漏了源向量的其余坐标。每次先对全部六或十一源完整求和并乘回，随后再逐 $f$ 系数核等。

所有分子、分母的完整 SHA256、字节数及首次 checkpoint 已保存在上述小回执。可重算系数没有另存为仓库数据或分片。

## 5. 首次真实执行及边界

唯一执行为 [run 46134694458 / job 140947271529](https://github.com/Rogerhu12/math-research-public/actions/runs/46134694458/job/140947271529)。

- 冻结 source git blob：c0b1f13b94335d0ad6287ea95ffdaffe38ff039f。
- source SHA256：af7a596e927972d2b37752267d001d492c130da650ad4659a2ff627eaa8d9658。
- source commit：af4b6e1c21c77a4ff35c0c090e1485c7eae3efb0。
- 原预算：180 秒、4 GiB；实际 driver 6.894556505 秒、最大 RSS 77880 KiB、内部 exit 0。
- 最后完整数学 checkpoint：6.834533747 秒。
- stdout：14213 字节，SHA256 024faa6b6eb193d67c9fc977cfbb615222bba7b9fa7bd3ca2eae3d0bc0dcdcfb。
- 真 pull：2026-11-28 10:20:28.554601 UTC，由冻结提交更新到 42dd5bdd71dddddb3ad2ac0cea76bd4bf111e779；根与课题 README 两 blob 均未变，分别为 99c5ad8d06e939e6cfbbab1afdeffa5463f15f18、5fbd905291dd044c88d35bd9c07ac0e586ff795a。

本次确实得到 (10) 的全图原条件表示，而没有求十一式的共同零点或新纯权投影。所有 $\lambda,T$ 首项零面、$b_0=0$ 以及实际原组合中的未付内容零面均保留。当前全 W 仍须进一步排除；此前全图 616824 的界来自纯权长度乘 native 六生成环境再乘 $\rho$ 二次，与本篇 f 唯一恢复没有可机械删除的独立二倍因子，故该历史界不在此改写。
