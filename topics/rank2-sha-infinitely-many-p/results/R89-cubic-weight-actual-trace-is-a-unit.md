# R89：实际三次微分权迹在每个惰性素数处为单位

日期：2026-11-12。状态：全部系数界、唯一小指标风险及真实域迹均已根端独审。
完整证明见[三次权迹与完整尾界](../notes/2026-11-12-actual-weighted-primitive-trace-unit.md)。

令 $d=p+1$、$D=pd$、$\varpi^d=p$，$p\ge7$ 惰性。
$B$ 是含实际级结构及常数的有限非分歧基域。
全部 $K$ 零点 $r$ 是 $B(\varpi)/B$ 的同一个 Galois 轨道。
原实际原函数为

$$
I(t)=H_i(u(t)),\qquad I'=\frac{M_eK}{sL^2},\qquad I(0)=0.
$$

本结果证明

$$
\operatorname{Tr}_{B(\varpi)/B}\frac{I(r)}{L(r)^3}
\equiv\frac1{12}\pmod p.
$$

若改用实际同源微分 $c=bL(r)$，则对应单位为 $b^{-3}/12$。

## 完整尾项不能由直接积分约化代替

周期系数满足 $v_p([t^j]J)\ge-j/D$。
写 $A=M_e/(t^4sJ^2)$，则 $A_0=1$、
$v_p(A_j)\ge-\lfloor j/D\rfloor$。
$K$ 的 $\nu$ 个可能负层要求指标至少 $d+(\nu-1)D$，故

$$
v_p(I_m)\ge-1-\left\lfloor\frac{m-d-3}{D}\right\rfloor-v_p(m)
\qquad(m\ge d+3).
$$

在较小奇指标中，积分除数唯一的 $p$ 风险为 $m=p$。
实际展开 $H_i=\sum C_nu^{n-1}/(n-1)$、已证 $C_d\in p\mathbb Z_p$
及 $u(t)$ 到次数 $p$ 的整性共同给 $I_p\in\mathbb Z_p$。
这不假设中央单位或 $\Sha$ 有限。

因此缩放后只有 $m=3,d+3$ 留在约化中，完整尾界同时保证 Tate 收敛：

$$
\overline{\varpi^{-3}I(\varpi X)}
=\frac{X^3}{3}+\frac{\kappa_pX^{d+3}}4,
\qquad \kappa_p=p[t^d]K\bmod p.
$$

实际根满足 $\bar X^d=-\kappa_p^{-1}$，$L(\varpi X)/\varpi$ 约化为 $X$，
所以每个 $I(r)/L(r)^3$ 都整且约化为 $1/12$。
求和属于 $B$，误差由 $\varpi\mathcal O_{B(\varpi)}\cap B=p\mathcal O_B$
升为模 $p$，得所述迹单位。

同一函数的不同权迹有不同性质：$I/L^2$ 为奇函数而迹零，
$\operatorname{Tr}(I/L)\in p\mathcal O_B$，三次权则为单位。
还没有证明这个非零单位控制指定中央 Bockstein 或完整 $J'_p(0)$。
