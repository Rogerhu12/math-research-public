# 正确 Phi 的整 alpha 零支：新原 qV 范数与固定 Q 投影

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**未执行的唯一首次新输入。** 源
`2026-11-28-unit211-Phi-zero-true-alpha-zero-original-norm-and-Q-projections-8542.py`
为 7674 字节，SHA256 **385ce1a1c0c70e404dcf08ed84ea22db4e9350624721d480ef86265853715ee0**。总 120 秒、1 GiB；外驱动 135 秒。嵌套计时请求始终钳在最初截止时刻。不保存系数载荷，不重跑旧三个原线性对的证明门。

## 1. 仅使用已成首一环境

唯一依赖是已刊源

`2026-11-28-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-8542.py`，

blob 22a90daf4fbd8fe1a8cd8ff451ba345807d7f060，SHA256
58cab31654894e8b4a4309f1c6b69619f5ee19591f74256f3128dd2026a4f025。

仅执行到其唯一 `results=[]` 标记之前；必要前缀 9438 字节，SHA256

`7d6fc9ed844a83daccf3978ed572a4b3a803266875c229fb5d3a42e3a75e751c`。

这提供 [已成的整 alpha 零环境](../results/R150-appendix-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-and-weight-conditions.md)：$m,\theta$ 在整支由真原身份支付，

$$
f=u-\frac{\ell\theta}{2m},\qquad t=-\frac{2\ell(1-Q)}m,
$$

$$
q(V)=V^2+q_1V+q_0=E_{Bo}/H,\qquad
H=4u\theta/M^2\ne0.
$$

四个真正原余式为

$$
r_0=E_{Be}\bmod q=a+bV,\qquad r_1,r_2,r_3=N_1,N_S,P_S\bmod q.
$$

此前三个线性对只给 $C_N,C_S,C_P$，尚未用 q 与 $r_0$ 的同 V 相容；这是本次新目标。

## 2. 新范数合成到两个原二次，保所有首项零

定义

$$
n=a^2-q_1ab+q_0b^2.
$$

令 $e_2=[V^2]E_{Be}$，则
$E_{Be}=r_0+e_2q$。由固定 $(2,1)$ Sylvester 身份

$$
n=(a-q_1b-bV)r_0+b^2q
$$

得到完整原式

$$
n=(m_0+m_1V)E_{Be}+(n_0+n_1V)E_{Bo},
$$

$$
m_0=a-q_1b,\quad m_1=-b,\quad
n_0=(b^2-e_2m_0)/H,\quad n_1=-e_2m_1/H.
\tag{1}
$$

唯一 H 逆在整个已成支上已付；不倒 b 或任何新头。源按 $V^0,\ldots,V^3$ 全四坐标返回 (1)，再清四个真实乘子的权分母，取**全部四乘子**的共同内容精除，并重新乘回全四坐标。

所以共同内容零面未被删去；剥除仅作用于新完整原身份的已付权因子。剩余新纯权多项式记 N。只有实际 N 为原单位，才立即排整支；N 恒零则准确保留，不虚构后继投影。

## 3. 三个旧标量只作参数定义

$C_N,C_S,C_P$ 只由 $r_0,r_j$ 的常数行列式再生，剥已付权因子并规范化，然后分别核既成 SHA：

- 9da720bb18618e80ba9db96559e73dd25c9e4600a8e1576e6e8f046d36e61ad1；
- 80c26662a4c2cbde3cb5e55976061cb117ea9a8ad7d9954c50a2b5e22b95ae83；
- c04b14a34183209fa97fc6c34f6b503afedbc212c29bbdcc98a0c9b517c5338f。

不执行旧三个原 pair 的乘子、全二坐标验证、分类或登记门。必要系数再生只服务本次新 N 相容与后续新投影。

## 4. 两个新的固定结式及全部退化纤维

若 N 非恒定且非零，先对这个新 N 作完整 QQ 因式乘回，保全部因子和重数。随后计算

$$
R_N(u)=\operatorname{Res}_Q(N,C_N),\qquad
R_S(u)=\operatorname{Res}_Q(N,C_S)
$$

的完整 QQ 多项式，使用实际符号 Q 次数所定义的固定 Sylvester 行列式。有限同 Q 原根无论首项如何退化，都使对应固定行列式为零；程序不按某个 u 特化后重算或缩小尺寸。

对这两个新投影作完整 QQ 一元 Bézout，所有组合乘回。最终必要 u 多项式只剥已付权因子；剩余因子全部保留。若实际返回已付单位，才排整 alpha 零图。否则只登记真正 u 覆盖，不把必要投影当完整原值解集。

另以 $N,C_N,C_S,C_P$ 的全部 Q 系数作一个新的 QQ[u] 系数组合。只有其实际 gcd 剥原单位后为 1，才证明没有物理共同竖纤维。若同时有非零 u 覆盖 U，令 d 为这四个原条件的最大 Q 次数，便可严格给不同权对数至多 $d\deg U$；没有这个系数返回就不作权点有限性声明。后继仍须原 q、四原值及物理 D 返回。

没有多元模空性提升、随机纤维选取、Norm 逆或泛型主元单位；没有涉及被冻结的 B 大矩阵或已撤回的旧 Phi 紧凑链。每阶段即输出准确已成身份，即使后段触界，也不将未完成目标冒充成功。
