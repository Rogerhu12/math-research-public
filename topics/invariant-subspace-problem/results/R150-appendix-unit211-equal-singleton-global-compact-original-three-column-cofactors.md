# R150 unit211：整个 h=k 图的紧凑原五行、三列与全 Delta 必要 cofactor

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 1. 完成的原返回

在当前原 h=k 碰撞图上，新的紧凑输入将全部其余三均值、原 N1 与原 NV 送到同一个自由原变量 z=Qt 的三列 (1,z,z²)，并返回三个固定原常数 cofactor。所有 Delta=0 点完整保留；没有倒置 Delta、几何首项或商代数范数。

三个新的必要参数多项式在 (lambda,u,Q) 中的次数分别为

$$
 (62,17,9),\qquad(80,20,11),\qquad(61,16,9).
$$

它们不是已排空证明，不把多变量 gcd=1 当作无公共零点，也不反称三个 cofactor 已替代五条原行。下一输入在完整 Delta=0 面先作原相容的固定 Q 投影，仍保所有 Q 首项零点。

## 2. 同一个原自由参数与合法的 P1 除法

沿用[整个Q=1−u的独立碰撞排除](R150-appendix-unit211-equal-singleton-Q1u-Delta-zero-and-entire-face-exclusion.md)及其中各先前原结论。在剩余 h=k 图中，T0 与 J−Q 已分别整面排除，故

$$
 P_f=T_0(J-Q)
$$

是真实原单位。原参数仍为

$$
 A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,\quad \ell=A^3/B^2,
$$
$$
 T=A^2/B,\quad h=k=1+\xi,\quad
 \rho^2=1-Q,\quad \rho(b-c)=u-\ell.
$$

保留自由 z=Qt，只从原 P1 解

$$
 f=-\frac{P_c+bc\Phi z}{P_f}. \tag{1}
$$

原 NV 行为

$$
 E_{NV}=N_Ff+bcS\xi z+N_C.
$$

程序对全部系数准确返回

$$
 P_f E_{NV}=T_n-bc\Delta z,\qquad
 T_n=P_fN_C-P_cN_F. \tag{2}
$$

所以 (2) 在 Delta零面仍是原相容条件 Tn=0，而非一个被除法删除的分支。Delta非零时可再恢复原 z，但本篇没有做这个局部化。

## 3. 全部三均值与 N1 的紧凑原来源

直接调用[已证明的自由原 Gram 标量恒等式](R150-appendix-unit211-compact-original-scalar-means-and-N1-identities.md)，取

$$
 R=R_2/(2\rho),\quad W=W_4/(4\rho^2),
 \quad O=O_8/\rho,\quad N=N_1^*.
$$

这些乘除只涉及原非零 rho。再使用同一个原 E0/N0 恢复

$$
 V_n=Jf-G+bc z,\quad W_*=T_0+4uf,\quad
 Y_*=QW_*-2V_n.
$$

这里 Y_* 对应通用恒等式正文中的辅助量 N；本页原 N1 行始终记 N，不把它与极化项 Nv 混同。原恒等式正文中的实际 P1 来源 Pj=3wP02 仍用于 N1。

将 rho²=1−Q、rho(b−c)=u−ell 代入，四式的 rho 都消去，成为 lambda,u,Q 的有理系数、z 至多二次的多项式。代入 (1) 仍至多二次。原 NV 仅一次。

原 bc、Q、rho、ell 均为已付单位，所以在原 E0 下 R=W=O=0 与其余三个原均值 E1=EB=EC=0 等价。此等价来自两个个别均值的实际差与原加权和，不是把一条二次扩张等式的两个系数擅自设零。

本次未重新组装旧统一缩放 Gram，也未重算旧八式投影。它使用已完成的原标量恒等式，产生新的全 Delta 同点输入。

## 4. 五条原行的全部三列返回

将每一条原有理多项式 p 写作

$$
 p=\frac{g_p}{d_p}
      (\widehat p_0+\widehat p_1z+\widehat p_2z^2),
 \qquad g_p/d_p\ \hbox{为原单位}. \tag{3}
$$

共同分母 d_p 是实际系数分母的 lcm。分子公共内容只剥与此前已付原单位相交的因子；未付内容保留。程序实际检查14种不同系数分母，并把 (3) 全部系数乘回。没有以一般秩或随机点核验代替恒等式。

原允许的单位包括 A、B、Q、1−Q、lambda、u、u−1、bc、ell、u−ell、P02、S、T0、J−Q、Phi、u+Q−1。最后一项已由独立 h=k 两 Delta 图完整支付。名单不含 Delta 或新的参数首项。

五个完整行依次为 R、W、O、N1、NV，固定列为 (1,z,z²)；NV 的末列实际恒为零。各系数的次数、摘要及分母信息保在小回执，全部大系数由冻结源再生。

## 5. 三个固定原常数 cofactor

对三行 a,b,c，定义多项式行

$$
 \gamma=(b_1c_2-b_2c_1,\ 
         c_1a_2-c_2a_1,\ 
         a_1b_2-a_2b_1).
$$

新源对三列逐一准确核回

$$
 \gamma\begin{pmatrix}a\\b\\c\end{pmatrix}
       =(\det(a,b,c),0,0). \tag{4}
$$

实际三组为 (R,W,O)、(R,W,N1)、(NV,R,W)。由于每个原点有首项为1的非零评价列 (1,z,z²)^t，(4) 迫相应行列式为零。无需把这三列视为原最终商的自由基底。

随后仅剥原单位并乘回，得到三个全图必要多项式：

| 原三行 | 原det次数 (lambda,u,Q) | 必要多项式次数 | 项数 | 必要多项式SHA256 |
|---|---|---|---:|---|
| R,W,O | (129,31,22) | (62,17,9) | 5933 | 9403fd667daefd68e6b71b497071959b63590c2ddf28a6e8f2fa703df4615512 |
| R,W,N1 | (129,32,23) | (80,20,11) | 9174 | 8c5998f06c4815d3e20173caa8ec85f84e9a336d5bdf4122d39ee97f0d3c8cda |
| NV,R,W | (104,26,18) | (61,16,9) | 5098 | 1550d469c24e1f1054370dae87dba2425ef87bb92e2e5802cc107b1ad04cf892 |

(4) 完全是原参数环的多项式恒等式，故任何临时主元、原最高次系数或 Delta 变零时都仍成立。三份 cofactor 证书编码分别1837687、1867278、922754字节，全部已经逐列乘回，只保源和摘要，不保存可重算的大矩阵。

这些只是必要条件。所有个别谱 N/P、其余原相容条件及普通 ISP 完成标准仍按各自原范围保留；不存在从三行列式同时为零反推全部原方程成立的断言。

## 6. 实际新执行

[冻结紧凑原返回源](../notes/2026-11-27-unit211-equal-singleton-global-compact-original-three-column-cofactors-8542.py)：

- blob5afa07ac91f958eabc0788290f658fcae21f8284，11226字节；
- SHA256 7bd915c3505e7c7e6bdd1aff7ec85362a29a2771b9f65f4ff5f8b8d067482bd8；
- 实际run46023475765 / job140588775738；
- 源5.621393478秒，驱动5.701043520秒，峰值90476KiB，内层退出0；
- stdout20511字节，SHA256 0fa41f99ca1f18f03d66509710a8243b8611a62d885d63178c8340249935a82a；
- 实际pull为2026-11-27 15:17:02.804059 UTC，提交155846f67d9fff97adba79dfb57ddb1cf16ade78，两README无差异；
- Python3.12.14、python-flint0.9.0、单线程，180秒/4GiB。

[实际五行、三cofactor及小回执](../notes/2026-11-27-unit211-equal-singleton-global-compact-original-three-column-cofactors-receipt-8542.json)。后续只再生必要输入，不以重放本次原证明证书作为下一条新投影的门槛。
