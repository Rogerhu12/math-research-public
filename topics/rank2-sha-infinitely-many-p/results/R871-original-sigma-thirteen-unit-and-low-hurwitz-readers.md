# R871 — 原 S 十三次单位运输与同源低 Hurwitz 三行

日期：2026-11-16。**状态：下列同一原矩阵的整单位运输、whole 来源、三个低 Hurwitz 读取与全部 carry 行公式已证明。原同一提升的指定组合是否非零仍未判定。**

本篇接 [R861](R861-original-hasse-aligned-gaussian-and-three-hurwitz-readers.md)，把其 $79,p+80,2p+81$ 读取化成 $1,p+2,2p+3$。这不使用新的中央零，也不把 $\mathcal D(S)$ 再当作 whole theta 来源。全部来源坐标保持原样；实际改变的是同一个有限目标的整单位。

## 1. 原 S/w 的完整目标单位

保持 R861 的共同模型 $E_1:y^2=x^3+1$、原好位
$$
p=6s-1>211,\qquad
1\le\ell<s-13,\qquad
a_*=-34\mathcal C_p,\qquad
\mathcal C_p=(p+1)\binom{3s-1}{2s-1}.
$$
仍保原 canonical 单部分的次数与整性门。
目标始终是
$$
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3).
\tag{1}
$$
记
$$
\mathfrak a(t)=t(t-1)h_7(t),\quad
h_7=7+4t+16t^2,\quad d=1+8t,\quad
\rho=d\Theta^{17}.
$$
原 $S=S_{34}$ 准确为
$$
S=\frac{\mathfrak a(t)}7\,\rho,\qquad S(w)=w+O(w^2).
\tag{2}
$$
采用已经 Hasse 对齐的**完整实际** $g$，
$$
\rho=g(w)e^{a_*w^s/p},\qquad
v_S(w)=g(w)\frac{\mathfrak a(t(w))}{7w}.
\tag{3}
$$
$t/w$ 是原确定的整单位，所以 (3) 不是在有零因子的 $\Gamma$ 中任意选 $w$ 的商。
它由原形式来源唯一指定，且 $v_S(0)=1$。

R618 的第二 Gaussian 界保证 (1) 所需全部系数整：
这里普通 $w$ 次数小于 $4s$，而
$6n(2p-1)/(p(p^2-1))<1$ 对所读 $n$ 成立。
因此
$$
\boxed{
V_S=v_S(w)e^{a_*\epsilon}\in\Gamma^\times,
\qquad
\mathsf U_S=V_S^{-13}\in\Gamma^\times.
}
\tag{4}
$$
$g$ 中的实际 $h_\Theta=H_pw^{s-4}B(w)$ 和所有 regular 高尾均在 (3) 中。
指数、逆单位和全部乘法都在 (1) 的真实关系 $w^s=p\epsilon$ 下读取；
没有先令 $w^s=0$。

定义
$$
\boxed{M_B=\mathsf U_S M_{\rm act}^{\rm orig}.}
\tag{5}
$$
这是同一有限自由目标的整自同构，故对每个原源向量 $X$ 和每个 $j$，
$$
M_BX\in p^j\Gamma\quad\Longleftrightarrow\quad
M_{\rm act}^{\rm orig}X\in p^j\Gamma.
\tag{6}
$$
它保持所有 Smith 因子和完整逐页提升。
原 $w^{13}$、三条十三行带、末短块及末端四次 carry 并未删除。
特别 (6) 适用于同一个 $P+pR+p^2S+p^3T$，不允许分块更换修正。

## 2. 实际辅助列 B 是 whole 来源

原列与公共因子沿 R365/R657 为
$$
\Phi_{n,k}=G_0\rho^nq_n(t)t^k,\qquad
G_0=\rho^{40}
 \frac{P_{134}(t)t^{13}(t-1)^{15}h_7^{13}}{d^{17}},
\tag{7}
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\qquad
A_n=\left\lfloor\frac{n+1}{4}\right\rfloor,\quad
B_n=\left\lfloor\frac{n+1}{3}\right\rfloor,\quad
C_n=\left\lfloor\frac n2\right\rfloor,
$$
$$
0\le k\le e_{n+1},\qquad
3A_n+B_n-C_n+e_{n+1}
=\left\lfloor\frac{9n}{2}\right\rfloor+4.
$$
所有原固定单位沿同一 $\Phi$ 保留。

由 (2)、(7)，准确有
$$
\boxed{
B_{n,k}:=\frac{\Phi_{n,k}}{S^{13}}
=7^{13}\Theta^{17(n+27)}
d^{n+10}(t-1)^2P_{134}(t)q_n(t)t^k.
}
\tag{8}
$$
这里是实际解析恒等式，不是仅模 $p$ 的局部商。

**Whole 性。** $d$ 的剩余指数
$n+10-C_n\ge0$。式 (8) 中除 $\Theta$ 外的 $t$ 多项式次数至多
$$
150+n+\left\lfloor\frac{9n}{2}\right\rfloor.
$$
代 $\Theta=x\sigma^2,\ t=-x^{-3}$ 后，最低 $x$ 幂至少
$$
17(n+27)-3\left(150+n+\left\lfloor\frac{9n}{2}\right\rfloor\right)
=9+14n-3\left\lfloor\frac{9n}{2}\right\rfloor>0.
\tag{9}
$$
所以
$$
\boxed{
B_{n,k}=\sigma^{\mu_n}R_{B,n,k}(x),\qquad
\mu_n=34(n+27),
}
\tag{10}
$$
是原整 whole 截面，$R_{B,n,k}$ 的极阶至多 $\mu_n$。
固定 $P_{134}$ 没有被省掉，原十九角也没有放宽。
(10) 仅用来计算同一列经 (5) 后的 jet；
没有把 $B_{n,k}$ 添入原算术中央池或另计为免费源列。

若原分解为
$$
\Phi_{n,k}=w^{13}A_{n,k}(w)e^{a_*(n+40)w^s/p},
$$
则
$$
B_{n,k}=\frac{A_{n,k}(w)}{v_S(w)^{13}}
 e^{a_*(n+27)w^s/p}.
$$
故 (5) 的同一列准确是 $w^{13}$ 乘这个实际 $B_{n,k}$ 的原折回。
其低质量
$$
B_{n,k}(0)\ne0
\quad\text{只能发生于 }n=0,1,2,\ k=0.
\tag{11}
$$
这些实际常数不统一改为一。

## 3. 对应的原整左行及全高尾 carry

写
$$
R_{27}(q)=(q-27)(q-28)(q-29)
=q^3-84q^2+2351q-21924=\sum_{j=0}^3c_jq^j.
$$
在变换后的目标上取
$$
\Lambda_{27}
=-21924[\epsilon^0w^{13}]
+\frac{2351}{a_*}[\epsilon w^{13}]
-\frac{168}{a_*^2}[\epsilon^2w^{13}]
+\frac6{a_*^3}[\epsilon^3w^{13}].
\tag{12}
$$
由 (11)，$\bar\Lambda_{27}\bar M_B=0$。
返回原目标的真实整行是
$$
\boxed{\Lambda_S=\Lambda_{27}\mathsf U_S.}
\tag{13}
$$
它不是保持旧 $\Lambda_0$ 不动后任意删除一个共同 $S$。

以下给 (13) 的完整有限行公式。记
$$
v_S(w)^{-13}=\sum_{n\ge0}d_nw^n,\quad d_0=1,\qquad d_n=0\ (n<0),
$$
以及
$$
R_{40}(q)=(q-40)(q-41)(q-42)=\sum_{j=0}^3r_jq^j.
$$
由于 $R_{27}(q-13)=R_{40}(q)$，准确有
$$
\Lambda_{27}e^{-13a_*\epsilon}=\Lambda_0.
$$
对原标准向量 $Z=\sum z_{i,r}\epsilon^iw^r$，
令 $L_i=s$（$0\le i\le2$）、$L_3=\ell+13$。
则
$$
\boxed{
\Lambda_S(Z)=
\sum_{i=0}^3\sum_{d=0}^{3-i}
 p^d\frac{r_{i+d}(i+d)!}{a_*^{i+d}}
 \sum_{r=0}^{L_i-1}d_{ds+13-r}\,z_{i,r}.
}
\tag{14}
$$
证明是唯一原折回：$w^n\epsilon^iw^r$ 到达
$\epsilon^{i+d}w^{13}$ 当且仅当 $n=ds+13-r$，系数是 $p^d$。
它同时保 (3) 的全 $h_\Theta$ 和 regular 高尾。

特别模 $p$，
$$
\bar\Lambda_S-\bar\Lambda_0
=
\sum_{i=0}^3\frac{r_i i!}{a_*^i}
 \sum_{r=0}^{12}\bar d_{13-r}[\epsilon^iw^r].
\tag{15}
$$
$i=0$ 的这十三行在所有原 $M$ 列上**整地恒零**，
其余正是原最前三条十三行。
因 $s-4>13$，(15) 所用 $d_1,\ldots,d_{13}$ 是
固定特征零 $(S/w)^{-13}$ 的低系数，不读取新的高轴。

但整式 (14) 还包含 $d\ge1$ 的 $p,p^2,p^3$ 高尾项。
它们一般混入原长行，不能据 (15) 提前删掉。
对于已经满足 $M X\in p^j\Gamma$ 的同一个 $X$，
读取下一位 $\Lambda_S M X/p^j\bmod p$ 时才可使用 (15)：
与旧左行的差由该位的同一十三行带确定。
如果这些带也在原下一页被杀，两个指定标量在该页相同。
这不是把未完成的带方程视为已经成立。

## 4. 三个实际 Hurwitz 读取降至 1,p+2,2p+3

对同一个 whole $B_\Phi$，设
$$
q=n+27,\qquad \mu=34q,\qquad J_j(B_\Phi)=D_z^jB_\Phi(0).
$$
定义原 whole 整行
$$
\mathcal D_{\mu,p,k}(R_{B,\Phi})
=\left.\frac{J_{p+k}-\mathscr H_pJ_{k+1}
-\mu k(L_2\mathscr H_p)J_{k-1}}p\right|_{\rm CM}.
\tag{16}
$$
使用 R856 的整性，必须先在全部参数上作整商，再特化。
在 CM 点 $\mathscr H_p=0$，且 $\mu\mathcal C_p=-a_*q$，所以
$$
J_{p+k}=\mu\mathcal C_p\,kJ_{k-1}
+p\mathcal D_{\mu,p,k}(R_{B,\Phi}).
\tag{17}
$$

令
$$
n_j=j(p+1),\quad k_j=(j-1)p+j,\quad
u_j=\frac{(j(p+1))!}{p^j}\in\mathcal O^\times
\quad(0\le j\le3).
\tag{18}
$$
这里 $u_0=1$，且 $u_j\equiv(-1)^j(j!)^2\bmod p$。
由 $n_j=p+k_j,\ k_j-1=n_{j-1}$，
$$
J_{n_j}=(\mu\mathcal C_p)^j\prod_{h=1}^jk_h\,J_0
+p\sum_{\ell=1}^j
 (\mu\mathcal C_p)^{j-\ell}
 \prod_{h=\ell+1}^jk_h\,
 \mathcal D_{\mu,p,k_\ell}(R_{B,\Phi}).
\tag{19}
$$
因此真正读取的是
$$
\boxed{k_1=1,\qquad k_2=p+2,\qquad k_3=2p+3.}
\tag{20}
$$

原行号没有改变，因为变换后的列是 $w^{13}B_\Phi$：
$$
[\epsilon^jw^{13}]M_B(\Phi)
=p^j[w^{js}]B_\Phi
=\frac{J_{j(p+1)}(B_\Phi)}{u_j}.
\tag{21}
$$
这是 (20) 与 R861 的七十八阶偏移不同的确切原因；
没有从原目标删去 $w^{13}$。

定义
$$
\mathscr P^B_p(q)=
\sum_{j=0}^3\frac{c_j(-1)^jj!\,q^j
                         \prod_{h=1}^jk_h}{u_j},
$$
$$
\rho^B_{q,p}=
\begin{cases}
\mathscr P^B_p(q)/p,&q=27,28,29,\\
0,&\text{其余实际 charge},
\end{cases}
\tag{22}
$$
以及
$$
\gamma^B_{\ell,p}(q)=
\sum_{j=\ell}^3\frac{c_jj!}{a_*^ju_j}
 (-a_*q)^{j-\ell}\prod_{h=\ell+1}^jk_h.
\tag{23}
$$
因 $\mathscr P^B_p(q)\equiv R_{27}(q)\bmod p$，
(22) 在显示的三种情形整；其它情形的 $J_0$ 由 (11) 整地为零。

(19)–(23) 给完整整读取
$$
\boxed{
\frac{\Lambda_S M(\Phi)}p
=
\rho^B_{q,p}J_0(B_\Phi)
+\sum_{\ell=1}^3\gamma^B_{\ell,p}(q)
                  \mathcal D_{34q,p,k_\ell}(R_{B,\Phi}).
}
\tag{24}
$$
其首剩余系数为
$$
\boxed{
\gamma^B_{1,p}(q)\equiv-\frac{q^2-84q+2351}{a_*},\quad
\gamma^B_{2,p}(q)\equiv\frac{q-84}{2a_*^2},\quad
\gamma^B_{3,p}(q)\equiv-\frac1{6a_*^3}.
}
\tag{25}
$$
不能将 (22) 的低质量项从后两位删除。
也不能因 (25) 最后一项为单位便断言指定和非零。

## 5. 真首核的一条 D1 与同一 R,S 的完整后两位

对真正 $\bar P\in K_1$，变换后同一个首核的前三条常数行
逐个杀掉 charge $27,28,29$ 的 $J_0$ 组合。
写
$$
B_\Phi=A^B_\Phi(w)e^{a_*q_\Phi w^s/p}.
$$
由 (16)，
$$
\mathcal D_{34q,p,1}(R_{B,\Phi})
=u_1[w^s]A^B_\Phi
-\mu\mathcal C_p\frac{u_1+1}{p}A^B_\Phi(0).
\tag{26}
$$
这里 $(u_1+1)/p$ 是准确整数，不能先删质量项。
原常数三行消去它后，
$$
\boxed{
\bar\Lambda_S\beta_1(\bar P)=
\frac1{a_*u_1}
 \sum_\Phi P_\Phi R_{27}'(q_\Phi)
               \mathcal D_{34q_\Phi,p,1}(R_{B,\Phi})
 \pmod p.
}
\tag{27}
$$
$R_{27}'(27+n)=3n^2-6n+2$，仍是同一来源的实际 charge 权。

令 (24) 对原向量 $X$ 的线性组合为
$\mathcal H_B(X)\in\mathcal O$。
完整提升必要地满足
$$
\boxed{
M(P+pR+p^2S+p^3T)\in p^4\Gamma
\quad\Longrightarrow\quad
\mathcal H_B(P)+p\mathcal H_B(R)+p^2\mathcal H_B(S)
\in p^3\mathcal O.
}
\tag{28}
$$
每次除 $p$ 仍由前一页支付；$P,R,S,T$ 都是原同一格中的同一组修正。
(5)–(6) 保证该整运输不会损失其它 normal 或 carry。
但 (28) 本身仍只是一条投影，不能替代完整四块。

对 R865 的 actual quartic $k_{\rm carry}>13$，
(27) 的首位仍为零：它对应
$$
a_*^{-1}[w^s]\,
v_S^{-13}c_*U_0
 (3\mathcal E^2-6\mathcal E+2)\bar P(t,\bar g),
$$
其最低阶是 $s+k_{\rm carry}-13>s$。
因此这次整运输不伪造一个新的首位单位。
它把真正后两位中的高热读取换成了 (20)，而非自动解出它们。

## 6. 原四中央的授权边界

(27) 的 Hurwitz 指标现在与原四算术来源的第一行相同，
但其实际 whole 截面是 (8)，degree 为 $34(n+27)$，
并且可能质量非零。
原四中央仅属于 $S_{34},T_{72},U_{136},V_{66}$；
它们不直接给 (16) 的这些 $B_\Phi$ 添零。

本篇也没有对 $\mathcal D(S)$ 再使用 R856 的 whole Frobenius。
所有应用都只对已在 (9)–(10) 证明 whole 的 $B_\Phi$ 进行。
$S^{13}$ 的整链已经吸入真实目标单位，
无需把单个 $D_7(S)$ 或 $D_{p+8}(S)$ 冒充四原 $D_1$ 的组合。

接下来的指定问题是：(24)/(28) 的实际 $D_1,D_{p+2},D_{2p+3}$
能否由原全部前缀、同一 $R,S$ 和四中央的真实关系判定。
来源、角帽、十三行和所需 $p$ 位均不因读取指标降低而免费增加。
本篇为完整符号证明，无新增数学数值执行。

依赖：[R365](R365-whole-original-conductor-carrier-and-total-charge-connection.md)、
[R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)、
[R657](R657-original-long-ordered-prefix-and-quadratic-contact-bound.md)、
[R856](R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)、
[R861](R861-original-hasse-aligned-gaussian-and-three-hurwitz-readers.md)、
[R865](R865-actual-high-axis-product-and-first-divided-row.md)。
