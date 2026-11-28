# 新输入：正确整 B 的实际终端原乘子取消

日期：2026-11-28（Asia/Taipei）。未执行。源 SHA256 73d4dd4167d48b5a5878338bdfe85dc6c59a194b97fa2ae23309e2c2226eac35；120 秒、1 GiB，嵌套前缀共享绝对截止。

## 1. 不重复已成的 C315 门

[已成 C315 原身份](../results/R150-appendix-unit211-Phi-zero-true-Bzero-C315-original-ideal-weight-cover.md)使用可达 DAG 边分母的 LCM，得到 $C_{315}^{22}\in I_6$。本次目标不同：真正反传终端原系数，允许其完整分子分母约消，并返回一次幂的实际原目标。

只取相同原 $I_4=(E_1,E_{\rm e},E_{\rm o},N_1)$ 的必要定义。源从已刊 whole-I6 文件在 newValues/quotients 标记前截断，并明确删除两行 NS、PS 定义。不会执行旧三个 cofactor、完整十二行门、C315 清 LCM、正幂单位目标或旧因式判定。

当前原权环仍为
$$
A=\mathbb Q[x,1/(xF(x+1)H\beta JC_2)].
$$
$H_3$ 不倒；所有当前原点均在先前严格支付的范围。完整保留全部终端未付 x 零集。

## 2. 唯一必要七行与真正新终端目标

已成首一 $q=\omega^2+q_1\omega+q_0$ 和四条原线性余式 $\ell_0,\ldots,\ell_3$。只再生
$$
\ell_0,\omega\ell_0,\ell_1,\omega\ell_1,
\ell_2,\omega\ell_2,\ell_3
\tag{1}
$$
七个必要行，其中 $\omega$ 倍按 q 返回两列。此前日志已经确定在第七行达到 degree $(0,0)$；这里再生这些必要行及已定 leading 消元，以取得新终端系数输入，不执行后五行或旧粗覆盖算法。

每个有理权尺度和两列 DAG 边仍完整返回。真正新步骤是从终端 $e_0$ 沿可达 DAG 反向累计，形成七个实际、已约分
$$
\Omega_j\in\mathbb Q(x)[\lambda],\qquad
\sum_{j=0}^6\Omega_jr_j=(1,0).
\tag{2}
$$
源将 (2) 全两列乘回，而不是从泛型 rank 直接宣称全图单位。

## 3. 返回四个原二次并取消全部实际分母

设 $F_i'$ 为四个原二次经同一点中心坐标代入后的多项式，$\ell_i=F_i'-a_iq$，并有已付原来源 $q=\sum_i\tau_iF_i'$。

先把 (2) 的成对系数组成
$$
\beta_0=\Omega_0+\omega\Omega_1,\quad
\beta_1=\Omega_2+\omega\Omega_3,\quad
\beta_2=\Omega_4+\omega\Omega_5,\quad
\beta_3=\Omega_6.
$$
在完整 $\omega$ 多项式环计算并首一短除
$$
\sum_i\beta_iF_i'-1=k(\omega)q.
$$
余式必须实际为零。故真正四原乘子为
$$
B_i=\beta_i-k\tau_i,\qquad
\boxed{\sum_i B_iF_i'=1.}
\tag{3}
$$
源码将 (3) 的全部 $\omega$ 系数完整乘回。随后只取这些最终 $B_i$ 的实际约分后 pure-x 分母 LCM，剥已付支持，得到 $C_{\rm new}$，再全式返回
$$
C_{\rm new}=\sum_i(C_{\rm new}B_i)F_i'.
\tag{4}
$$
各 $C_{\rm new}B_i$ 的剩余分母须全部属于 A。因为被消去的原线性式 L 本就属于 $I_4$，且中心坐标两向变换只用已付权，坐标代入的核是 $(L)$，(4) 精确提升到
$$
C_{\rm new}\in I_4.
\tag{5}
$$
该提升不假原模自由，也不增加任何物理头或 D 逆。整个 $C_{\rm new}=0$ 始终保留；只有它为非零常数才排空整个 B。LCM 变小或 QQ(x) 上为 1 本身不作排空依据。

## 4. 后继精确支持

源先输出已完成的 (4)–(5)，再对这个新终端多项式作完整 QQ[x] 因式分解、因子乘回和平方自由支持检查。不重算旧315多项式。

若 $C_{\rm new}=\gamma\prod\phi_i^{e_i}$，则 $\prod\phi_i$ 给全部必要不同 x 值，最大 $e_i$ 次幂对原 $C_{\rm new}$ 的整除也实际乘回。只给不同权参数点界；固定权处的完整几何纤维没有据此自动变成有限。若最后因式步骤触资源边界，前面已经完整输出的原身份不因可选支持分类而撤销，但实际退出必须准确保留。

## 5. 两个准确依赖

- 2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py，完整 SHA b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56；
- 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，完整 SHA 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

第一份按明确标记取 I4 前缀，并按唯一两行 NS/PS 赋值过滤；原前缀与实际使用前缀 SHA 均输出。第二份仍仅提供 R 算术。无历史 JSON、矩阵缓存或额外远端载荷。
