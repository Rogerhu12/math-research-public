# R150 unit211：h=k 上整个 Phi=0 碰撞面的原排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 1. 完整结论

在原 unit211 一般 LS 的 h=k 碰撞图中，**整个 Phi=0 面没有原复解**。此前已完成的[ell≠1 原排除](R150-appendix-unit211-equal-singleton-Phi-zero-ell-nonone-original-exclusion.md)与本篇的完整 ell=1,u=2 四次常数代数返回互补，没有丢失任何参数头零。

此后可以在尚未排空的 h=k 图支付 Phi≠0。已有整个等权、T0=0、J=Q 的独立原碰撞排除，合计支付 u−ell、T0、J−Q、Pf、Phi。这里仍没有排空整个 h=k；不以这些局部结论宣布 unit211 或普通 Hilbert ISP 完成。

本结论直接使用 D=0 的原碰撞参数，不借用旧 D≠0 值图上的 Phi、权重或几何范数排除。

## 2. 互补图的完整来源

沿用[整个 J=Q 碰撞证明](R150-appendix-unit211-equal-singleton-entire-JQ-zero-original-exclusion.md)中的

$$
 A=2\lambda^2-2\lambda+1,\quad
 B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
 \ell=A^3/B^2,\quad T=A^2/B,\quad \xi=B/A,
$$
$$
 S=2\xi+3-2\lambda,\quad \eta=\xi+3-2\lambda,\quad w=\lambda-1-T.
$$

原 Phi 条件是

$$
 (1-\ell)Q=2(u-1)(u-2). \tag{1}
$$

ell≠1 图已经由完整八原式、固定11阶与9阶 QQ 结式得到 R143/R80 的 Bézout 单位。原首项为零的所有 lambda 纤维均保留。这里只补其真正的互补 ell=1。

由 (1) 及原 u≠1，ell=1 时必须 u=2。原二、三矩给

$$
 B^2-A^3=\lambda^2\phi_4(\lambda),\qquad
 \phi_4=8\lambda^4-24\lambda^3+24\lambda^2-12\lambda+3.
$$

原 lambda≠0 已付，故保留 phi4 的全部复根。实际用的是首一常数代数

$$
 K=\mathbb Q[\lambda]/
 \bigl(\lambda^4-3\lambda^3+3\lambda^2-\tfrac32\lambda+\tfrac38\bigr).
 \tag{2}
$$

源准确核验 phi4 与其导数互素。计算不选择某一根或某一复嵌入，也不以数值近似替代 K。每一次常数逆都由 QQ 扩展 Euclid 给出真实乘积1；若某常数不是整个 K 的单位，代码按 gcd 将全部常数因子分成两支继续。本次实际无任何这种分拆。

## 3. 自由原 Q 与唯一同点 Gram 参数

在整个 (2) 上仍保留原 Q 为自由变量。令 rho²=d=1−Q，p=1+rho、q=1−rho，原权按

$$
 b=\frac12+\frac{\rho}{2d},\qquad
 c=\frac12-\frac{\rho}{2d}.
$$

它们准确满足 b+c=1、bp+cq=2，且

$$
 bc=-\frac{Q}{4(1-Q)},\qquad
 T_0=-Q-4,\qquad J-Q=-4,\qquad
 P_{02}=2Q,\qquad P_f=4(Q+4),\qquad \Phi=0. \tag{3}
$$

原 Q≠0、rho≠0 已付；此前整个 T0=0 碰撞排除支付 Q+4≠0。因而本篇所有 Q 分母只从

$$
 Q,\quad 1-Q,\quad Q+4
$$

产生，并在构造后逐个 gcd 剥除确认。K 中的 A、B、S、xi 等常数逆均真实乘回；没有把一般函数域非零冒充整个常数代数单位。

以原 Pc、NF、NC 的同一公式，两个仿射条件给

$$
 f=-P_c/P_f,\qquad
 t=-\frac{N_C+N_Ff}{bcQS\xi}. \tag{4}
$$

因为 Delta=−SxiPf≠0，(4) 在整个本面有效；不倒 NF。源把 (3)、(4) 的全部原身份准确乘回，然后重建 H=1 的未缩放原 Gram。

## 4. 全八原式的 K[Q] 单位

实际重建 E0、N0、P1、NV、全部原矩与两个孤立值的原目标。两个原 B/C 行同时保留，rho≠0 支付其偶、奇系数提取。得到

| 原行 | Q 分子次数 | 原 Q 分母完整返回 |
|---|---:|---|
| E1 | 4 | 是 |
| EBe | 6 | 是 |
| EBo | 5 | 是 |
| N1 | 4 | 是 |
| NBe | 8 | 是 |
| NBo | 7 | 是 |
| PBe | 8 | 是 |
| PBo | 7 | 是 |

本次没有从这八个分子再剥任何非恒定 Q 因子。其完整系数按 Q 升幂、各系数按 lambda 升幂存入小回执。

仅 E1 与 EBe 两个完整分子已足够。K[Q] 的真实扩展 Euclid 给次数分别至多5、3的 a(Q)、b(Q)，完整乘回

$$
 a(Q)E_1(Q)+b(Q)E_{Be}(Q)=1. \tag{5}
$$

例如 E1 的 Q 升幂系数为

$$
\begin{aligned}
&15456-39424\lambda+65984\lambda^2-28928\lambda^3,\\
&5880-14912\lambda+25472\lambda^2-11136\lambda^3,\\
&3300-8284\lambda+14024\lambda^2-6128\lambda^3,\\
&1023/2-1296\lambda+2248\lambda^2-976\lambda^3,\\
&957/8-(1173/4)\lambda+(2007/4)\lambda^2-222\lambda^3 .
\end{aligned}
$$

完整两行、a,b 的所有有理数系数及常数多项式共5263字节，SHA256 为

fd599d85faeafb3ca63e8319d7b5bba7cae1b09c662a6a24f30ffa8f8eaa76dd。

它们保存在随文回执的 fullCertificate 中，可在整个 (2) 上直接复算 (5)。全次执行共19451次实际常数逆、13318次实际多项式除法，全部乘积或除法身份返回；这包括构造阶段，不是只计最后两行。没有取有限域样本、单个 lambda 根或单个 Q 值。

若有原复点，其 lambda 对应 (2) 的某个嵌入，且原 E1=EBe=0；将 (5) 在该嵌入和其 Q 上求值便得1=0。故整个 ell=1,u=2 纤维被排除。与互补 ell≠1 图合并，得到第1节的完整结论。

## 5. 实际运行及首次失败的保留

成功源：

[2026-11-27-unit211-equal-singleton-Phi-zero-ell-one-complete-quartic-original-return-8542.py](../notes/2026-11-27-unit211-equal-singleton-Phi-zero-ell-one-complete-quartic-original-return-8542.py)

- blob98a1160f5bbd043d086c7ecc36b5268cb778af46，13709字节；
- SHA256 af8215e2cc4e17797e507cc32d1217e202fbe59cb76f4a762ae3ed7056b701bc；
- 实际 run46017199172、job140567258560；Python3.12.14、python-flint0.9.0、单线程；
- 源9.891444144秒，驱动9.967132103秒，峰值35672KiB，源退出0；
- stdout17911字节，SHA256 1843e5806d55bb76e5cb3650169db1671c9d7b2fa63859794a55505ef98b0e16；
- 实际pull时间2026-11-27 14:35:04.273387 UTC，提交56a5d643432fb781d762785bb463fc96d50cde3f；两README无差异。

[成功小回执及全部小证书](../notes/2026-11-27-unit211-equal-singleton-entire-Phi-zero-original-exclusion-receipt-8542.json)保存本次完整身份。

此前7f9源的局部变量遮蔽失败仍保[原说明与准确回执](../notes/2026-11-27-unit211-equal-singleton-Phi-zero-ell-one-first-shadow-failure-8542.md)：run46016731411、内层退出1，仅原参数返回，Gram未完成。新源只修正原 Gram 单位向量名称，实际重新完成的是先前中断的原输入；不把旧失败改写为成功，也没有重放已成的 ell≠1 投影。
