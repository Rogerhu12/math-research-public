# 正确 h=k、Delta=0 的全部 Q 纤维与1444个三参数点界

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：完整证明。** 在[正确 Delta=0 的722基点图](R150-appendix-unit211-h-equals-k-corrected-Delta-zero-722-base-cover.md)中，每个固定 $(\lambda,u)$ 上的原 $\Delta(Q)$ 都不是零多项式。因此每个基点至多有两个不同 $Q$，完整不同三参数点满足
$$
\boxed{\#\{(\lambda,u,Q)\}\le1444.}
$$
全部 Q 二次首项退化都在此界内。这个结论仍不计数剩余 $z$ 或完整 Gram 纤维，也不排除 $P_f=0$ 补图。

## 1. 只用正确原 Delta 的定义

沿[正确五原行](R150-appendix-unit211-h-equals-k-corrected-five-original-rows-and-three-physical-cofactor-conditions.md)，写
$$
A=2\lambda^2-2\lambda+1,\qquad
B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\xi=B/A,\qquad \ell=A^3/B^2,\qquad
c_\lambda=3-2\lambda,\qquad d_\lambda=3-4\lambda,
$$
$$
\eta=\xi+c_\lambda,\qquad S=2\xi+c_\lambda.
$$
这里 $AB\ne0$。与真实原值 $N_4(V)$、原 $P_1$ 相接的量为
$$
j_0=-2u(u-1),\qquad \phi_0=-2(u-1)(u-2),
$$
$$
J=j_0+\ell Q,\qquad T_0=j_0-\ell Q,\qquad
\Phi=\phi_0+(1-\ell)Q,
$$
$$
P_f=T_0(J-Q),\qquad
N_F=d_\lambda Q+J\xi\eta,\qquad
\Delta=\Phi N_F-S\xi P_f.
\tag{1}
$$
这些定义与旧错误 $R_{\rm bad}$ 无关；本稿不借其任何投影。

有
$$
\ell\xi^2=A,\qquad
P_f=j_0^2-j_0Q+\ell(1-\ell)Q^2,\qquad
N_F=j_0\xi\eta+(d_\lambda+\ell\xi\eta)Q.
\tag{2}
$$
因此 $\Delta$ 对 $Q$ 至多二次；其分母只在 $A,B$ 内，与 $Q$ 无关。

在当前物理图中，独立的[正确零基点 mean 来源](../notes/2026-11-28-unit211-original-u-zero-scaling-static-audit-8542.md)和[整个对称 u=1 排除](R150-appendix-unit211-h-equals-k-entire-symmetric-u-one-original-exclusion.md)已经支付
$$
u(u-1)\ne0.
\tag{3}
$$
不会把另一规范的旧 $u=1$ 直接移到这里。

## 2. 原三系数的精确相容条件

令
$$
\Delta(Q)=\Delta_0+\Delta_1Q+\Delta_2Q^2.
$$
由 (1)–(2) 直接收集系数：
$$
\Delta_2=(1-\ell)(d_\lambda-A),
\tag{4}
$$
$$
\Delta_0=-4\xi u(u-1)^2(u\xi+2\eta),
\tag{5}
$$
$$
\Delta_1=-2(u-1)
\bigl[(u-2)d_\lambda+u\xi(\eta+S)-2\ell\xi\eta\bigr].
\tag{6}
$$
例如常数项是 $\xi j_0(\phi_0\eta-Sj_0)$，
而 $\phi_0\eta-Sj_0=2(u-1)(u\xi+2\eta)$，给 (5)。
一次项也可先写成
$\phi_0(d_\lambda+\ell\xi\eta)+j_0[(1-\ell)\xi\eta+S\xi]$，
再用 $\phi_0-j_0=4(u-1)$，得到 (6)。
没有除 $\ell-1$ 或任何新首项。

若 $\Delta$ 在某个固定 $(\lambda,u)$ 上恒为零，由 (3)、(5)、$\xi\ne0$，
$$
u=u_*=-\frac{2\eta}{\xi}=-\frac{2H}{B},
\qquad H=B+c_\lambda A.
\tag{7}
$$
再置
$$
I=H+B=2B+c_\lambda A,\qquad E=\lambda^2+\lambda-1,
$$
$$
F=A^2I\,d_\lambda+A^3H+BH(H+I),\qquad
G=(B^2-A^3)E.
\tag{8}
$$
由 $d_\lambda-A=-2E$，(4) 是
$$
\Delta_2=-2G/B^2.
\tag{9}
$$
把 (7) 代入 (6)，使用
$\eta=H/A,\ S=I/A,\ \ell\xi\eta=AH/B$，准确得到
$$
\Delta_1(\lambda,u_*)=\frac{4(u_*-1)}{BA^2}F.
\tag{10}
$$
由于 $u_*-1$ 在此假设下仍由 (3) 非零，整零 Q 纤维必须满足
$$
F(\lambda)=G(\lambda)=0.
\tag{11}
$$

## 3. 新纯 lambda Bézout 已完整返回一

(8) 中的两个明确有理多项式实际均为八次。本次唯一新计算是在
$\mathbb Q[\lambda]$ 对这对多项式作精确欧氏 Bézout。程序保存并递推两个原多项式的实际组合系数，每步多项式除法都完整乘回；末尾另独立检查
$$
X(\lambda)F(\lambda)+Y(\lambda)G(\lambda)=1.
\tag{12}
$$
实际首一 gcd 是一，未剥除任何原因子。代码虽保留已有权支持的通用分支，本次该分支循环次数为零；本证明因此不需要额外支付 $I$、$\lambda$、$\ell-1$ 或 $E$。

(12) 与 (11) 矛盾。所以对每一对满足 $ABu(u-1)\ne0$ 的复参数，原 $\Delta(Q)$ 都不是零多项式。
这是包括全部特殊 $\lambda$ 的准确声明；没有从泛型次数推到所有纤维。

本次没有重跑722投影、独立旧 P 的结式、旧 cofactor、原 Q 结式或任何冻结的 Loww 门。计算只涉及这个新的原系数相容问题。

## 4. 从722到1444的完整纤维合成

前篇在原
$$
h=k,\quad\Delta=0,\quad ABQ(1-Q)P_f\,bcP_{02}\ne0
$$
图上证明不同 $(\lambda,u)$ 基点至多722。
它保留所有 u 首项退化；本稿只处理此前未付的 Q 纤维。

固定其中任一基点，第3节证明 $\Delta(Q)$ 是次数至多二的非零多项式。
若它降成一次，至多一个 Q；若降成非零常数，无 Q；二次情形至多两个不同复 Q。
因而不同 $(\lambda,u,Q)$ 总数至多 $2\cdot722=1444$。

这里不把 Q 的二次首项当单位，不挑一个复根，也不需要对 Q 多项式做平方自由化。
(4) 的 $\ell=1$ 与 $E=0$ 整首项零纤维都已经由 (5)–(12) 覆盖。

原 $z$、完整 Gram、其非退化限制以及 $P_f=0$ 补图仍需后续原条件处理。
旧848/578和旧整 Delta=0 排空仍撤回；这个新有限三参数界不恢复它们。

## 5. 可读源与唯一实际记录

[自含新源](../notes/2026-11-28-unit211-h-equals-k-Delta-Q-fiber-coefficient-Bezout-8542.js)只用 BigInt 有理数和一元多项式，完整给 (8) 和欧氏组合递推。

- 源 Git blob：83b7fc55532c274c365e29f6e8158c7c6e7b5116，3392 B。
- SHA256：596019950292d1247f5205a624dc8e7fe0aa8950f652a2867b08be8800ccf454。
- 唯一 V8 实际：2毫秒，49次有理多项式乘法，9次完整除法乘回。
- 两输入次数8、8；实际 gcd 次数0，规范系数为1。
- 最终完整 Bézout 多项式乘回成功；已付支持剥除零次。
- root 与 r150_open_geometry 分别全文静核 (1)–(10)、源码及图范围；没有再执行。

[小回执](../notes/2026-11-28-unit211-h-equals-k-Delta-Q-fiber-coefficient-Bezout-8542-execution.json)保准确实际状态。程序没有执行完整原 Gram；它验证 (12)，与本文的原系数推导共同证明所有 Q 纤维结论。普通复 Hilbert ISP 仍未完成。
