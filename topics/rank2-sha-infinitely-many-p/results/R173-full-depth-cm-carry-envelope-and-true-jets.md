# R173：全部 CM 共振的非线性分母账本与真实 jet 基线

**已证明；主目标未完成。**

对实际 $a=\vartheta^4,b=\sigma^4$ 的图形
$a=f(b)=1+\sum c_kb^k$，令惰性 $p\ge7$、$r=(p+1)/4$、
$n=\lfloor k/r\rfloor$，并置

$$
e_p(k)=0\ (n=0),\qquad
e_p(k)=n+\left\lfloor\frac{n-1}{p-1}\right\rfloor\ (n\ge1).
$$

R170 的整 CM 递推连同保重数的加权分拆给
$v_p(c_k)\ge-e_p(k)$ 对全部 $k$ 成立。
共振处递推分子实际留有至少一层余量，故一次除 $p$ 不破坏归纳；
此处已计入所有旧分母的非线性传播。

若 $\tau_p=p[s^r]\log a\pmod p\ne0$，第二个共同共振精确满足

$$
p^{p+1}c_{pr}\equiv-\tau_p\pmod p,
\qquad v_p(c_{pr})=-(p+1).
$$

这来自真实 Lagrange 式中的 $q=p$ 阶乘进位，不能按共振个数忽略。

对所有次数 $D$ 与所有真实饱和前缀，

$$
\|\varphi_{D,k}^{ab}\|_p\le p^{e_p(k)},\qquad
\|\varphi_{D,k}^{\mathcal A,B}\|_p\le p^{e_p(k)}.
$$

源参数 $b=w+O(w^2)$ 的运输仅在准确前缀核上进行。
因 $e_p(k)\le4pk/(p^2-1)$，全部惰性成本至多
$2k\log k+O(k)$。这是无条件完整基线，尚非 R159 所需的
严格 $a_I+2b_I<2$；没有以单个坏系数冒称真实 jet 下界。

[完整证明及端点核查](../notes/2026-11-12-full-depth-cm-carry-envelope-and-true-jets.md)。
