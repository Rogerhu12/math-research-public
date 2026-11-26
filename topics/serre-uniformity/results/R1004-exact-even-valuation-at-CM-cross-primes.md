# R1004：CM 交叉素数的精确偶赋值与任意层下界

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 本文严格保留 R320/R326 的实际 CM 同余分支；它不覆盖 R1003 恢复的其它 Serre 异常分支。root 核对了 R320 引理320.1–320.3的同一整数迹、全部奇偶性及以下范数恒等式。没有执行新的素数窗口，也没有引用未重建的新预印本。

## 1. 原对象和精确结论

本节是在 R320 的原固定 CM 迹上得到的完整证明，不使用 BFL。它把 R320 的一次 $p\to p^2$ 提升解释为一个**准确的赋值奇偶性**，给出任意高同余层的正确幅度；不会把该局部提升冒充全局层数提升。

### 1.1 命题

固定 $p>37$ 且 $p\equiv5\pmod {12}$。取 R320 的实际整数 $a$、原符号 $\varepsilon$ 和好素数
$$
q\mid 2a^3-1,\qquad q\equiv1\pmod {12},\qquad q\ne p.
$$
令原 CM 曲线
$$
G:y^2=x^3+3x,\qquad J_\varepsilon:y^2=x^3-2\varepsilon
$$
在 $q$ 的实际整数迹分别为 $g_q,j_{\varepsilon,q}$，并令
$$
D_\varepsilon(q)=\frac{g_q-j_{\varepsilon,q}}4\in\mathbb Z\setminus\{0\}.
$$
则有
$$
\boxed{v_p(D_\varepsilon(q))\in2\mathbb Z_{\ge0}.}
\tag{1004.1}
$$
若这同一对实际全局曲线满足 $H_a[p^n]\simeq B_a[p^n]$，则
$$
\boxed{p^{2\lceil n/2\rceil}\mid D_\varepsilon(q),}
\tag{1004.2}
$$
且有明确的大小限制
$$
\boxed{q\ge p^{4\lceil n/2\rceil}
            +8p^{2\lceil n/2\rceil}+4.}
\tag{1004.3}
$$
当 $n=1,2$ 时 (1004.3) 都只是 R320 的 $p^4+8p^2+4$；不能把 $n=2$ 误提高为 $p^8$。当 $n=3,4$ 时才得到 $p^8+8p^4+4$。

## 2. 完整证明

R320 引理320.2–320.3 在同一 Frobenius 取向上给出整数
$$
q=x^2+y^2=u^2+3v^2,
\qquad g_q=2x,\quad j_{\varepsilon,q}=2u,
\tag{1004.4}
$$
其中 $x,u$ 为奇数，$y,v$ 为非零偶数，且 $x-u\ne0$。这些性质只用两个原 CM 曲线在 $q$ 的具体约化及 $2$ 为模 $q$ 立方；不预先使用模 $p$ 同构。

由于 $(3/p)=-1$，对任意不全为零的整数 $y,v$，二次型 $3v^2-y^2$ 满足
$$
v_p(3v^2-y^2)=2\min\{v_p(y),v_p(v)\}.
\tag{1004.5}
$$
确实，令 $t=\min\{v_p(y),v_p(v)\}$ 并提出 $p^{2t}$，剩下至少一个坐标模 $p$ 非零。如果剩余二次型为零，则非零解给 $3$ 为平方，矛盾。故没有进一步的 $p$ 进消去。

由两个范数相等，
$$
(x-u)(x+u)=3v^2-y^2.
\tag{1004.6}
$$
若 $p\nmid x-u$，(1004.1) 直接成立。若 $p\mid x-u$，则由 (1004.5) 必有 $p\mid y,v$：这是把 (1004.6) 降模 $p$ 后的各向异性。又因 $q=x^2+y^2$ 且 $q\ne p$ 为素数，$p\nmid x$。所以 $u\equiv x\pmod p$ 给 $p\nmid x+u$。因此
$$
v_p(x-u)=2t,\qquad
t=\min\{v_p(y),v_p(v)\}\ge1.
\tag{1004.7}
$$
因 $D_\varepsilon(q)=(x-u)/2$ 且 $p$ 为奇数，得到 (1004.1)。

若给定全局 $p^n$ 同构，限制到 $q$ 的未分歧分解群，仍是 R320 引理320.1 的**同两个整数迹**，故 $p^n\mid g_q-j_{\varepsilon,q}$。结合 (1004.7)，得 $2t\ge n$，即 (1004.2)。

为证明精确大小界，写
$$
y=2p^t s,\qquad v=2p^t w,\qquad
x-u=2p^{2t}h,\qquad z=(x+u)/2,
\tag{1004.8}
$$
其中 $s,w,h$ 非零整数，$p\nmid h$，且 $z\ne0$。
若 $z=0$，则 (1004.6) 迫 $s^2=3w^2$，与 $s,w\ne0$ 矛盾。
代回 (1004.4)–(1004.6)，得到
$$
hz=3w^2-s^2,
\qquad q=z^2+p^{4t}h^2+2p^{2t}s^2+6p^{2t}w^2.
\tag{1004.9}
$$
因 $x=z+p^{2t}h$ 为奇数，$z,h$ 奇偶相反。
若 $|h|=1$，$z$ 为非零偶数，因此 $z^2\ge4$；若 $|h|\ge2$，则 $p^{4t}h^2\ge4p^{4t}$、$z^2\ge1$。两种情形均给
$$
q\ge p^{4t}+8p^{2t}+4.
$$
由 $t\ge\lceil n/2\rceil$ 得 (1004.3)。证毕。

## 3. 对实际有限检测的含义及边界

R320 的 $G_1(a)$ 若不是空集合 gcd，则
$$
v_p(G_1(a))\in2\mathbb Z_{\ge0},
$$
因为它是非空有限组偶数赋值的最小值。故仅以这些 $q\equiv1\pmod {12}$、$q\mid2a^3-1$ 的固定 CM 交叉迹差为输入时，要求全部迹差被 $p^{2t-1}$ 整除与要求被 $p^{2t}$ 整除完全等价。这是检测阈值的严格盲点，不声称已有两条实际曲线实现两个不同的全局深度。

R326 的真正全局同余整数 $\mathcal C$ 使用全部好素数；它的赋值不因本节而必须为偶数。尤其从 $p\mid\mathcal C$ 不能推出 $p^2\mid\mathcal C$，因为定义 $\mathcal C$ 的其它迹差没有 (1004.4) 的双 CM 范数结构。

因此本节给出了新的精确全局必要约束及检测器的奇偶盲点，并没有得到 $a,d,c$ 的统一上界，也没有关闭任一完整惯性/变化商域支路。


## 4. 来源

- [R320](R320-good-prime-cm-crossing-and-quartic-frobenius-barrier.md)：完整特化、固定两条CM曲线、实际迹的范数和奇偶性。
- [R326](R326-exact-global-congruence-modulus-and-all-p-power-levels.md)：同一全局同构在所有p次幂层的判别及其仍然依赖导子的界限。
