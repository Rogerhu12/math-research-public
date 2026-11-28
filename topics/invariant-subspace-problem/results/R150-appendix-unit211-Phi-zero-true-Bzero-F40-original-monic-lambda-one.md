# R150：正确 Phi 整 B 的 F40 纤维获得原首一 lambda 一次式

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**已证明。** 在当前正确 $\Phi=0$ 的整 B 曲线上，最后完整 $F_{40}$ 权纤维的原 $I_4$ 给出首一关系

$$
h_1(\lambda)=\lambda-\lambda_*(x)=0.
$$

保整个 $K_{40}=\mathbb Q[x]/(F_{40})$，原点仍满足同一个首一 $\omega$ 二次。因此必要的 $(x,\lambda,\omega)$ 代数是一个 **80 维 QQ 代数的商**，维数和不同点数至多 80。没有证明这个余商本身恰为 80 维，也没有排除 $F_{40}$。

结合 [整 F34 原排除](R150-appendix-unit211-Phi-zero-true-Bzero-entire-F34-fixed-original-norm-exclusion.md)及 [完整二次因子原排除](R150-appendix-unit211-Phi-zero-true-Bzero-terminal-quadratic-complete-original-exclusion.md)，当前整 B 的不同权对至多 40 个。完整原值方程仍须在此新的有限环境中返回。

## 1. 已定原输入，不选择复嵌入

沿用 [整 B 的正确原十二行呈示](R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)及 [C76 一次原覆盖](R150-appendix-unit211-Phi-zero-true-Bzero-terminal-C76-original-ideal-cover.md)。$F_{40}$ 是 C76 的唯一 40 次 QQ 因子，原多项式字典 SHA256 为

`ba88a205beb579a18de711c9fd61514716099afeed94954736246cedf733a16a`。

在整个 $K_{40}$ 中，实际原分母都已有真逆乘回。原四式 $(E_1,E_{Be},E_{Bo},N_1)$ 在同一个

$$
q_\omega=\omega^2+q_1(\lambda)\omega+q_0(\lambda),
\quad \deg q_1\le1,\quad\deg q_0\le2
$$

下为 $r_i=a_i+b_i\omega$，四对次数是 $(4,3),(4,3),(4,3),(3,2)$。$q_\omega$ 及四余行都有完整原 $I_4$ 来源；没有假设二生成元自由。

已成首一 $g_6$ 的准确 SHA256 为

`9a94efc0ec88870b215b47b5175bbc4832b9c3f75c66d14e16d59ab845198cfe`。

其必要输入由已定原行对 (0,3) 的 $a_0b_3-b_0a_3$ 首一化给出。本次仅再生这一既定对象并核身份，不运行旧六对证明或 480 维大矩阵。

## 2. 四个新固定范数及真正原一次返回

定义

$$
n_i=a_i^2-q_1a_ib_i+q_0b_i^2.
$$

实际逐三坐标返回

$$
n_i=(a_i-q_1b_i-b_i\omega)r_i+b_i^2q_\omega.
\tag{1}
$$

所有 $b_i=0$ 支均包含；这是固定二次对一次的原 Sylvester 身份，而非倒置范数。本次四个 $n_i$ 的 $\lambda$ 次数为 $8,8,8,6$，对原首一 $g_6$ 的余式均为 5 次。

逐条将四个 $n_i$ 加入 $(g_6)$ 的实际首一 gcd 次数为

$$
1,\ 1,\ 1,\ 1.
$$

因此最终单一对象

$$
h_1=\operatorname{monic\,gcd}(g_6,n_0,n_1,n_2,n_3)
    =\operatorname{monic\,gcd}(g_6,n_0)
\tag{2}
$$

对整个 $K_{40}$ 成立。这里 (2) 第二个表达式只是这个已成对象的较小**参数定义**：首步和末步首一 gcd 同为一次，后继整除迫使它们相同；不是另一次新结论或再执行门。

每次 Euclid 均将首一短除的商运输回 $g_6,n_i$，最后组合 (1) 与 $g_6$ 的原 (0,3) 来源，准确得到

$$
\sum_{i=0}^3(M_{i0}+M_{i1}\omega)r_i+Hq_\omega=h_1.
\tag{3}
$$

源码把整个 (3) 的三坐标实际乘回为 $(h_1,0,0)$。四个 (1) 加 (3) 共 15 个原坐标返回；没有依据模数、随机值、单个复根或 gcd 标志推断 (3)。

最终 $h_1$ 的规范原 K 系数序列长 15829 字节，SHA256：

`da857429ce495f99a8122be93572a2ea843d686399306736f686cc563b0851ee`。

其首项恰为 1，故 $\lambda_*=-h_1[0]$ 是唯一确定的 K 元素。仓库只保源、函数定义、哈希和小回执，不保这段可重算的系数载荷。

## 3. 80 维环境及仍未完成的条件

由 (3)，全部原点都进入

$$
\mathcal A
=K_{40}[\lambda,\omega]/(h_1,q_\omega)
\simeq K_{40}[\omega]/\bigl(q_\omega(\lambda_*,\omega)\bigr).
$$

第二个式子仍首一二次，故 $\mathcal A$ 在 $K_{40}$ 上自由秩 2，在 QQ 上维数 $40\cdot2=80$。原四行和完整 NS/PS 将进一步取商；本次没有假定它们在 $\mathcal A$ 中全零，也没有计算这个进一步商的精确维数。

所有 $\omega$ 重根都保留；整个 K 的所有复嵌入也保留。原物理开集不能增加点数，但本篇没有据此给完整谱规范坐标的点数界。尤其没有用 $D_{\rm val}=0$ 的模迹象排除原点。

后继新目标是**在已成 $\lambda=\lambda_*$ 上**回完整原值，属于这个 80 维环境；它不同于已冻结的 480 维 QQ 原矩阵。任何 $b_i(\lambda_*)$ 只有在整个 K 真逆并乘回后才能用于恢复 $\omega$。未得到真逆的首项零分量必须保留。

## 4. 唯一新实际身份

源：[固定原范数输入](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-large-fixed-original-norms-8542.py)，选择 `ISP_B_FACTOR_DEGREE=40`。源 blob `f7aa6e677ca3d4e2a59c146f0c35e7ec4fdc6cc9`，SHA256：

`c6e8acc0e71c119fd76f8213f2934daacc8ec728cb44b5a51f8541413e3a6eef`。

run **46125572734**，job **140919309079**；source/pull 均为 `85e32a6c96a40c236c915030017a0972b06493ed`，真实 pull 时间 2026-11-28 08:23:30.959787 UTC，两 README 无变。数学末阶段 13.577532679 秒，驱动 13.608183498 秒，RSS 55960 KiB，exit 0；界 120 秒/1 GiB、外 135 秒。

stdout 4658 字节，SHA256 `61c5fdd4b56580f0ed29b30d4314c7dd0ed94bc92805f4989423271fef815ed6`。[小回执](../notes/2026-11-28-unit211-Phi-zero-B-F40-fixed-norm-lambda-one-execution-8542.json)保存实际阶段。

旧 run 46124522483 的 1 GiB 内存失败保持冻结；没有重跑其 I6 大矩阵、正目标、旧完整来源证明或全部六对 gcd。新结果没有声称整 F40、整 B、一般 Phi 或普通 ISP 已完成。
