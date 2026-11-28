# R150：碰撞Delta零的完整C2常数代数及四次原权覆盖

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

只在附加完整条件（不依赖已撤回的七 lambda 全覆盖）
$$C_2(\lambda)=\lambda^2-\lambda+\tfrac13=0$$
上，原h=k、Delta=0相容式现已准确化成
$$
Q=3+3\lambda+(\tfrac52-15\lambda)u+(-\tfrac{11}2+12\lambda)u^2,
\tag{1}
$$
$$
133u^2+(-132+234\lambda)u+20-108\lambda=0.
\tag{2}
$$
全部两个lambda嵌入和两个u根都保留。原Gram还须在这个完整常数代数中返回，本页不把相容覆盖当作排空。

## 1. 原两式的完整降次

在QQ[lambda]/C2上，原值常数为
$$
\xi=-(1+\lambda),\quad
\ell=(11-9\lambda)/49,\quad T=(\lambda-2)/7,
$$
$$w=(6\lambda-5)/7,\quad S=1-4\lambda,\quad\eta=2-3\lambda.$$
准确有xi·eta=4lambda-3、eta-S=-xi、ell·xi=T。因此原NF满足
$$N_F=(4\lambda-3)(J-Q),$$
原Delta与Tnum满足
$$
\Delta=(J-Q)\xi\{\eta\Phi-ST_0\},
$$
$$
T_{\rm num}=Q\eta(J-Q)\{T_0wu-\xi P_{02}(\ell+T)\}.
\tag{3}
$$
其中J-Q、Q在本碰撞原域已支付；xi、eta在整个C2常数域均非零。

由于
$$\eta\Phi-ST_0
=2(u-1)(\xi u+2\eta)+(T+\eta)Q,$$
且
$$T+\eta=(12-20\lambda)/7$$
在完整C2常数代数中有精确QQ Bézout逆，原Delta=0完整等价于(1)。这一步不除任何u参数首项，也不选择一个lambda根。

## 2. 原Q图上的完整u相容

把同一个(1)代入所有原定义，实际核原Delta恒零、NF因式及(3)的完整Tnum身份。对
$$I(u)=T_0wu-\xi P_{02}(\ell+T)$$
的完整K[u]多项式，逐个与原单位
u、u-1、Q、1-Q、u-ell、bc分子、T0、J-Q、Phi、P02、u+Q-1作精确gcd和除法。

实际只剥一个u-1因子；全部除法和总乘积都返回。剩余首一式正是(2)除以133。因此原两条相容式在当前物理域必落于(1)、(2)，全部u首项退化仍保留；没有用一般点的gcd或随机值代替整域运算。

## 3. 不选根的四次QQ常数代数

记
$$A(u)=133u^2-132u+20,\quad B(u)=234u-108.$$
(2)即A+B·lambda=0。若B=0，则u=6/13，而
$$A(6/13)=-2128/169\ne0.$$
故在整个相容纤维上B非零，准确恢复
$$\lambda=-A(u)/B(u).$$
把它代入C2，完整整数身份为
$$
3A^2+3AB+B^2=399\,\Psi_4(u),
$$
$$
\Psi_4(u)=133u^4-30u^3-32u^2-24u+16.
\tag{4}
$$
因此可在完整QQ[u]/Psi4上处理全部原候选，再以同一(1)恢复Q。这里不声明Psi4不可约；下一原输入须保留其全部QQ因子，并逐个返回全部原Gram条件。

此四次覆盖与lambda1/3的独立原排除不同；C4(lambda)常数纤维也仍独立保留。

## 4. 实际返回身份

源：
[2026-11-27-unit211-equal-singleton-complete-C2-Delta-zero-original-return-8542.py](../notes/2026-11-27-unit211-equal-singleton-complete-C2-Delta-zero-original-return-8542.py)。

源SHA256：
6769f67d9d34995be4e4f90ad8d93d122b608a3312144d5822a5aa6b89a06f5a。

实际run46030198815/job140611767985；驱动0.092380266秒、源0.015484977秒、最大子进程RSS34420KiB、exit0。完整C2 Q图、原两相容乘积、51个常数逆和33个多项式除法均返回。源明确输出二次u残式未闭，未进入其仅处理线性残式的Gram分支。

stdout1206字节，SHA256
8e4ea9868dc1ae06c04500028d42b218957ff1405a1ad623a83c01f30967131d。
真实pull为2026-11-27 16:03:00.705408 UTC，读到e708f1b258568cb7ef3d2dc5e5776a03f34a50dc，两README未变。

(4) 的全部原八 Gram 返回已由[整个 C2 条件排除](R150-appendix-unit211-equal-singleton-Delta-zero-entire-C2-lambda-exclusion.md)完成；当前正确覆盖整合见[三个小因子及4788界](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)。旧578投影的全覆盖已撤回，本次相容门不重跑。普通Hilbert ISP未完成。
