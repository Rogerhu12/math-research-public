# R196：CM/reference Bockstein 差与导子 $p^2q$ 的真正 Norm 域

**状态：已证明。** 固定 R171、R191 的 $p=43$、同一 $q$ 和 Weil 标记。
本文区分 primal $W$、dual $W(1)$ 与 $\eta$ 三通道，计算 actual/reference
差，给出真正 $\kappa_p+2\kappa_q$ 的范数域。没有计算全局 Norm 原像，
没有计算完整 $\Omega_2$。环境中断后源和证书已重建、实际重跑。

## 1. 协变角色与参考格

令 $K=\mathbb Q(i)$、$A:y^2=x^3-x$，
$\psi,\bar\psi$ 为协变 Tate 模的 CM 角色，
$\psi\bar\psi=\chi_{\rm cyc}$。令 $J$ 为乘 $i$，
$D_z(v)=z\bar v$。则
$$
\operatorname{ad}^0(A[p])=\eta\oplus W,\quad
W|_{G_K}=\psi/\bar\psi\bmod p,\quad
W(1)|_{G_K}=\psi^2\bmod p.
\tag{196.1}
$$
$\tau$ 在 $W$ 上为共轭，在 $W(1)$ 上为负共轭。
迹配对使 $\operatorname{ad}^0$ 自对偶，不再额外反转角色。

以 Teichmüller 提升分离第一对数：
$$
\psi=\widehat{\psi_0}(1+p\ell_\psi)\pmod{p^2},\quad
\ell_{\rm cyc}=\ell_\psi+\ell_{\bar\psi}.
\tag{196.2}
$$

## 2. 同一投影与纯 $p$ 射线角色

沿用 R191 的 $r,\sigma,e_j,g$，记
$\mathcal P(x)=\prod_{j=0}^{41}\sigma^j(x)^{e_j}$，并置
$$
a_p=\mathcal P(2-r),\quad a_g=\mathcal P(g),\quad
a_q=a_ga_p^{22},\quad a_h=a_ga_p.
\tag{196.3}
$$
按 R191 的实 Kummer 下降得到
$\kappa_p,\kappa_g,\kappa_q,\kappa_h$。

$\kappa_p$ 精确导子为 $(p)^2$。
因为 $\sum e_j=0$，$\sigma^j r=3^jr+O(r^2)$，
$$
a_p=1-\frac12\sum_j e_j3^j\,r+O(r^2)
    =1+\frac12r+O(r^2)\pmod p.
\tag{196.4}
$$
令 $\alpha^p=a_p$，$t=\alpha-1$ 是 $B_p(\alpha)$ 的一致化元。
$v(\gamma t-t)=v((\zeta_p-1)(1+t))=p$，
所以 $B_p$ 上断点为 $p-1$；
经 tame 次数 $p-1$ 的 $B_p/K_p$ 下降，断点为 $1$，
导子指数为 $2$。在 $p$ 外元素为单位，故不分歧。
$2$ 的唯一素点被复共轭固定，$\eta$ 角色反变，
其未分歧 Frobenius 值为零。
R191 则已证明 $\kappa_q$ 导子恰为 $q$，在 $p,2$ 分裂。

## 3. Artin 方向与限制次数

取 primary $\beta=-1+2i$，$N\beta=5$。
在 $K/(\beta)=\mathbb F_5$ 中 $i=3$。
程序证明 $f\bmod5$ 不可约：
$r^{5^{42}}=r$，且对 $d=21,14,6$，
$\gcd(f,r^{5^d}-r)=1$。
用同一 $\zeta=(S_{44}(r)-ir)/2$ 计算
$a^{(5^{42}-1)/43}$，结果为：

| 元素 | $B$ 剩余域的 $\mu_{43}$ 指数 | $K$ 的 Artin 值 |
|---|---:|---:|
| $a_p$ | 22 | 21 |
| $a_g$ | 19 | 24 |
| $a_q$ | 30 | 13 |
| $a_h$ | 41 | 2 |
| $a_*:=a_pa_q^2$ | 39 | 4 |

第三列必须除以剩余次数 $42=-1\pmod{43}$。
第二列计算的是 $\operatorname{Frob}_\beta^{42}$，
不能把它直接认作底域 Frobenius。

另在 $\mathbb Z[i]/1849$ 精确算得
$$
-\frac{\beta^{1848}-1}{43}=22+11i\pmod{43}.
\tag{196.5}
$$
$1848=-1\pmod{43}$，故这正是 $\ell_\psi(\operatorname{Frob}_\beta)$。
$K$ 类数 $1$，反变 $p^2$ 射线角色只有一条线；上表确定其缩放：
$$
\ell_\psi-\ell_{\bar\psi}=-i\kappa_p.
\tag{196.6}
$$
两边在 $\beta$ 处分别为 $22i$ 和 $-21i=22i$。
同一 $\mathbb F_{q^2}$ 中还独立核验
$$
\beta^{(q^2-1)/43}=\zeta^{13}.
\tag{196.7}
$$
因此原 $\eta$ 角色、Weil 根和 Artin 方向一致。

## 4. Bockstein 的直接比较

若 $\rho_1(g)=(1+pB(g))\rho_0(g)$，在相同模 $p$ 识别下，
对同一逐点提升 $\widetilde c$ 有
$$
\delta_1\widetilde c-\delta_0\widetilde c
 =pB(g)\rho_0(g)c(h).
$$
使用 $\delta c(g,h)=gc(h)-c(gh)+c(g)$，故
$$
\beta_1(c)=\beta_0(c)+[B\cup c].
\tag{196.8}
$$
这是正号。

取 Kummer 参考格
$$
M_0=\mathbb Z_p(1)\operatorname{Teich}(W(-1)),\qquad
D_0=\mathbb Z_p(1)\operatorname{Teich}(W).
\tag{196.9}
$$
R163、R189 的正确类群型消失与 prime-to-$p$ 平均，
使这里指定的 $S$ 单位 Kummer 类可同规范提升到模 $p^2$；
它们的参考 Bockstein 为零。这不适用于任意类或任意格。

在 $G_K$，$M_0$ 的角色为
$\chi_{\rm cyc}\operatorname{Teich}(\bar\psi^{-2})$，
故 actual primal 差是
$$
-2\ell_{\bar\psi}=-\ell_{\rm cyc}-i\kappa_p.
\tag{196.10}
$$
$D_0$ 与实际 $W(1)$ 的差则是
$$
2\ell_\psi-\ell_{\rm cyc}=-i\kappa_p.
\tag{196.11}
$$
primal 的 cyclotomic 项不可从 dual 公式中省掉。

## 5. 首差与两个 adjoint 通道

令实际首差
$$
c=c_\eta J+c_W,\qquad c_\eta=-\kappa_q.
$$
直接矩阵计算给
$$
[J,D_z]=2D_{iz},\qquad
[D_w,D_z]=(w\bar z-z\bar w)\operatorname{id}.
\tag{196.12}
$$
后者是纯虚线性乘法，属于 $\eta J$；
若写成 $J$ 坐标还须除 $i$。
首差对 dual $W(1)$ 的 $WW$ 块追加 $2ic_\eta$，
所以
$$
\boxed{B_{\rm actual/reference,WW}=-i(\kappa_p+2\kappa_q).}
\tag{196.13}
$$
$W\to\eta$ 非对角块没有消失。
这里只识别 $WW$ 所需 Norm 角色；
完整 lifting 方程的阶数处理留给 R200。

## 6. 真正 Norm 域与平方化

置 $\kappa_*=\kappa_p+2\kappa_q$。
$p$ 处只有 $\kappa_p$，$q$ 处只有 $2\kappa_q$，
所以精确导子为 $(p)^2q$。
对应 Kummer 元素满足全局恒等式
$$
a_*=a_pa_q^2=a_g^2a_p^{45}
 =(a_ga_p)^2a_p^{43}=a_h^2a_p^{43}.
\tag{196.14}
$$
因此 $\kappa_*=2\kappa_h$，且数值核验
$21+2\cdot13=4=2\cdot2$。
取 $a_h$ 的 $43$ 次根再实下降，得到所需循环 $43$ 次域 $L_*/K$。
乘 $2$ 改生成元，不改扩张。

对 $F=K(A[p])^{\mathbb F_p^\times}$，真正 dual $WW$ Norm 域是
$FL_*/F$。它不同于仅有导子 $q$ 或仅有导子 $p^2$ 的扩张；
后两者只是完整计算的构件。

## 7. 普通 Norm 存在性与未完成量

令 $u_0$ 为同一 scalar norm Robert 单位。
$q$ 处它是局部 $p$ 次幂，所以是局部范数。
$p$ 处 $F/K$ 有唯一素点且分解群全：
$$
N_{F_p/K_p}(u_0)=N_{F/K}(u_0)\in\mathcal O_K^\times=\mu_4.
$$
$\kappa_p$ 杀 $\mu_4$，$\kappa_q|_p=0$，
由互反的范数相容性，$u_0$ 在 $p$ 也是局部范数。
$2$ 处扩张分裂，其余处是不分歧扩张上的单位范数。
循环 Hasse 范数定理给普通全局 $X$：
$$
N_{FL_*/F}X=u_0.
\tag{196.15}
$$

这里没有计算 $X$ 或其局部原始子。
普通原像可能有 $S$ 外相消赋值，受支撑修正须另算；
根和 gauge 的变化也影响二阶规范。
primal 的 cyclotomic 项及 $W\to\eta$ 项仍须保留。
因此不能据 (196.15) 推出 $\Omega_2=0$。
R198 完成纯 $p$ 子项；R200 才处理总归约。

## 8. 可重复程序

- [verify_r196_cm_reference.js](../scripts/verify_r196_cm_reference.js)
- [r196_cm_reference_certificate.json](../notes/r196_cm_reference_certificate.json)

~~~sh
node scripts/verify_r196_cm_reference.js notes/r196_cm_reference_certificate.json
~~~

程序内嵌输入，重新证明模 $5$ 不可约、计算全部 $42$ 个投影符号、
五个 Artin 值、CM 对数、同一 $q$ 符号及角色恒等式。
可用 `--certificate <路径>` 生成证书。
所有结果中均保留 `Omega_2_computed:false`。

依赖 R163、R168、R171、R176、R185、R189、R191。
循环范数定理取 J. S. Milne, *Class Field Theory*,
Chapter VIII, Theorem 3.1, printed p.234：
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>。
分歧断点、Bockstein 符号及矩阵括号均已在本文直接证明。

