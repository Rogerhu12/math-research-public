# R518 — 原 S 测试的 E 单位整逆、同源 sigma carry 与同一非零子管

日期：2026-11-14。**状态：已证明。** 本篇接 R515 的同一个原六 sigma
联合。R497 的固定正伴随多项式可以按 $E$ 次数作有限整逆，
使 $E$ 单位上的完整第一来源准确返回原 $S$。这个测试再随
$A$ 的真实核心运输，给原独立 sigma 单位相消域中的完整算术行。

同一个新测试在原五深一单位网格上仍有单位第五阶。
为此只增加一个固定单位 ray $\pi_0\equiv1\bmod1013$，并删去
显示的固定有限小素数集合；没有让测试的固定系数依赖 $p$。
该网格的真实 $A$ 像因此是**同一合格 sigma carry 中非零的
实际子管**。完整补域照常保留，本篇没有从子管非零推出中央非零。

## 1. 原六输入和 E 项

沿用 R515 的全部原周期、canonical lift、整性和固定 ray，
记
$$
\omega^2+\omega+1=0,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad
\kappa=p\lambda^2,\quad d=p-1,\quad b=17.
\tag{1}
$$
原输入是 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$，
$\nu_0=-\nu_\sigma^{\otimes6}/84$，原自由输入为 $x$。
保留 R515 的全部 $(B,A,E,K,Q_1,Q_2)$ 坐标；特别
$$
A=P+15\bar\gamma x,\qquad E=158x-\gamma P,\qquad
Y=\frac{A+c_0B}{15},\qquad c_0=17+14\omega.
\tag{2}
$$
三个 whole 核心是
$$
K_B=\chi I,\qquad K_A=\psi I,\qquad
K_E=\varepsilon I,\qquad
\varepsilon=-\chi\psi,\qquad\chi^2=\psi^2=1.
\tag{3}
$$
每个实际深度核心还含原单位标量 $\lambda$。
$E$ 正交于 $A,B$，故这些是保其余全部输出的真正核心。

原 R497 伴随为 $T_c=\gamma Z-27x$。R515 的完整运输给
$$
\boxed{
T_c=T_0+\tau E,\qquad
T_0=\frac{\gamma c_0}{15}B-\frac{247\gamma}{15\cdot263}A,
\qquad\tau=-\frac{34}{263}.
}
\tag{4}
$$
特别 $T_0$ 是真实平面 $(B,A)$ 的函数；$T_c$ 本身不是。
本篇一直使用 (4)，不把 $E$ 项遗忘。

## 2. 固定原算术测试与有限 E 单位整逆

R497(16)–(20) 给固定有理数 $c_1,\ldots,c_6$ 及
$$
\mathfrak h_b(t)=\sum_{k=1}^6c_kb^{-k}t^{6k},
\qquad
\boxed{Y_*\{\mathfrak h_b(T_c/\Omega)\nu_0\}=\nu_S.}
\tag{5}
$$
这里**没有 $T_c$ 单位指示函数**。$c_k$ 与 $p,\kappa,\lambda$
无关；完整六个整数分子及共同分母在附证书按 R497 原值保存。
(5) 是全部第一测度身份，故允许任意第一连续测试。

展开
$$
\mathfrak h_b((T_0+\tau E)/\Omega)
=\sum_{j=0}^{36}H_j(B,A)(E/\Omega)^j,
$$
$$
H_j(B,A)=
\sum_{\substack{1\le k\le6\\6k\ge j}}
c_kb^{-k}\binom{6k}{j}(T_0/\Omega)^{6k-j}\tau^j.
\tag{6}
$$
定义实际有限多项式
$$
\boxed{
\widehat{\mathfrak h}_p(B,A,E)=
\sum_{j=0}^{36}
\frac{H_j(B,A)(E/\Omega)^j}
 {1-\varepsilon\lambda\kappa^j}.
}
\tag{7}
$$
$j\ge1$ 的分母与 $1$ 模 $p$ 同余；$j=0$ 是
$1-\varepsilon\lambda=1\pm\lambda$，其单位性已由 R410 支付。
删去 (5) 的固定系数分母后，(7) 是整多项式。
$p$ 依赖只在 (7) 显示的有限个整分母中。

对任意完整 $(B,A)$ 测试 $f$，真正的 $E$ 核给
$$
\int_{E\in p\mathcal O}f(B,A)(E/\Omega)^j\,d\nu_0
=\varepsilon\lambda\kappa^j
 \int f(B,A)(E/\Omega)^j\,d\nu_0.
\tag{8}
$$
将 (8) 从全域中减去，再逐个 $j$ 使用 (7)，准确得到
$$
\boxed{
(B,A)_*\{{\bf1}_{E\ {\rm unit}}\widehat{\mathfrak h}_p\nu_0\}
=(B,A)_*\{\mathfrak h_b(T_c/\Omega)\nu_0\}.
}
\tag{9}
$$
因此完整第一来源是
$$
\boxed{
Y_*\{{\bf1}_{E\ {\rm unit}}\widehat{\mathfrak h}_p\nu_0\}
=\nu_S.
}
\tag{10}
$$
(8)–(10) 使用同一个原来源；没有使用 $E$ 边际的质量来替代
带 $E^j$ 的来源。若附只依赖 $(B,A)$ 的额外条件，(9) 仍然成立。

## 3. 同一原 sigma carry 中的准确算术行

定义保全部其他坐标的实际 $A$ 缩放
$$
M_{A,r}=I+\frac{\kappa^r-1}{3945}\bar A^{\,t}A,\qquad r\ge0.
\tag{11}
$$
它在 $(B,A,E,K,Q_1,Q_2)$ 中为
$\operatorname{diag}(1,\kappa^r,1,1,1,1)$。
由 (3)，
$$
\nu_0|_{A\in p^r\mathcal O}
=(\psi\lambda)^r(M_{A,r})_*\nu_0.
\tag{12}
$$
在深域内准确使用
$$
Y_r=\frac{A/\kappa^r+c_0B}{15},\qquad
\widehat{\mathfrak h}_{p,r}
=\widehat{\mathfrak h}_p(B,A/\kappa^r,E).
\tag{13}
$$
即第一 Mellin 权和整个多项式同时转置。

令
$$
\Gamma_r=\{A\in p^r\mathcal O,\ E\ {\rm unit},\
                      Y_r\ {\rm unit}\}.
\tag{14}
$$
由 (10)、(12)，对整个 Mellin 变量有
$$
\boxed{
\int_{\Gamma_r}\langle Y_r\rangle^{du}
           \widehat{\mathfrak h}_{p,r}\,d\nu_0
=(\psi\lambda)^r J_S(u).
}
\tag{15}
$$
$r\ge1$ 时，R515 的真实域身份给
$$
\boxed{
\{A\in p^r,\ E\ {\rm unit}\}
=\{P,\mathfrak c\ {\rm unit},\ P+\mathfrak c\in p^r\},
\qquad\mathfrak c=15\bar\gamma x.
}
\tag{16}
$$
所以 (15) 是原独立自由 sigma 与五输入残余的**实际单位
相消域**中的算术行。整逆 (7) 已吸收 R515 无权推前中的
$1-\varepsilon\lambda$，故 (15) 的系数只有
$(\psi\lambda)^r$。没有另添或漏掉该因子。

特别原 $J'_S(0)=0$ 确实推出 (15) 的中央导数为零。
这句话针对准确的 $Y_r$ 与 $\widehat{\mathfrak h}_{p,r}$；
不把它们换成未经运输的 $Y,T_c$ 测试。

## 4. 原五深一单位域的完整第五混合矩

保原独立域
$$
\mathcal D_n=\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n\mathcal O,\
                         x\ {\rm unit}\},\qquad n\ge1.
\tag{17}
$$
在此 $Y$、$A$、$E$ 都是单位：模 $p$ 分别为
$\bar\gamma x,15\bar\gamma x,158x$。
把五个深输入缩放为 $T$、$x$ 不动。准确有
$$
B(T)=TB,\quad A(T)=TP+15\bar\gamma x,\quad
E(T)=158x-\gamma TP,\quad Y(T)=TZ+\bar\gamma x.
\tag{18}
$$
由 (4)，两条用于第五阶计算的测试线是
$$
T_c(T)=\gamma TZ-27x,\qquad
T_0(T)=\gamma T\left(Z-\frac{34}{263}P\right)
                         -\frac{1729}{263}x.
\tag{19}
$$
$T_0$ 含原五输入的 $P$，不能只对 $Z$ 的边际求矩。

按五输入次序 $(\xi_1,\xi_2,\xi_3,c,d_0)$，置
$$
\boldsymbol z=(\delta,2\delta,\gamma,1,2),\qquad
\boldsymbol p=(-19+2\omega,10+29\omega,11-13\omega,32+14\omega,-1-11\omega),
$$
$$
\boldsymbol l=\gamma\left(\boldsymbol z-\frac{34}{263}\boldsymbol p\right),
\qquad t=-1729/263.
\tag{20}
$$
旧 $T_c$ 测试对应 $\boldsymbol l_{\rm old}=\gamma\boldsymbol z$、
$t_{\rm old}=-27$。

对任意五元 $\boldsymbol l$，定义固定代数系数
$$
C_j(\boldsymbol l)=
j!(5-j)!\!\sum_{\substack{I\subset\{1,\ldots,5\}\\|I|=j}}
\prod_{i\in I}z_i\prod_{i\notin I}l_i,\qquad0\le j\le5.
\tag{21}
$$
它恰是
$[\xi_1\xi_2\xi_3cd_0]Z^j(\sum l_i\xi_i)^{5-j}$。
因为每个独立 sigma 的质量为零、第一矩为 $\Omega$，总次数
小于五全部消失；第五阶只有这个真正的五重混合矩。

写 R497 的固定 sigma 展开
$\sigma_b(z)=z\sum_{m\ge0}a_mb^mz^{6m}$，$a_0=1$。
对 $k=1,\ldots,6$ 令
$$
\begin{aligned}
A_k(\boldsymbol l,t)
&=\sum_{j=1}^5\frac{(-1)^{j-1}}{j\bar\gamma^j}
       \binom{6k}{5-j}t^{6k-5+j}C_j(\boldsymbol l),\\
B_k(\boldsymbol l,t)
&=\binom{6k}{5}t^{6k-5}C_0(\boldsymbol l).
\end{aligned}
\tag{22}
$$
对
$$
\mathcal A_{\boldsymbol l,t}(T)=
d\!\int_{\substack{x\ {\rm unit}\\\text{原五输入全域}}}
 \log\langle \bar\gamma x+TZ\rangle\,
 \mathfrak h_b((tx+T\sum l_i\xi_i)/\Omega)\,d\nu_0
$$
逐项展开得完整身份
$$
\boxed{
[T^5]\mathcal A_{\boldsymbol l,t}
=-\frac d{84}\sum_{k=1}^6 c_kb^{-k}\Omega^{5-6k}
\left\{ A_k I_{6k-5}
+B_k[I_{6k-5,\log}+\log\langle\bar\gamma\rangle I_{6k-5}]
\right\}.
}
\tag{23}
$$
符号 $-1/84$ 是原六 sigma 的真实归一。
(23) 同时保 log 的全部碰撞项和单位尺度的 log 质量项。

由原 sigma 核，所有正矩仍是 R497(29)：
$$
I_{6k-5}=(1+\lambda\kappa^{6k-5})(6k-5)!
                  b^{k-1}a_{k-1}\Omega^{6k-5}.
\tag{24}
$$
两个 log 因子都在 $p\mathcal O$。
因此固定代数常数
$$
\alpha(\boldsymbol l,t)
=-\frac1{84}\sum_{k=1}^6c_k(6k-5)!a_{k-1}
                                  A_k(\boldsymbol l,t)
\tag{25}
$$
满足
$[T^5]\mathcal A_{\boldsymbol l,t}\equiv(d/b)\alpha(\boldsymbol l,t)\bmod p$。

记
$$
\boxed{
\alpha=\alpha(\gamma\boldsymbol z,-27),\qquad
\alpha_0=\alpha\left(\gamma(\boldsymbol z-34\boldsymbol p/263),-1729/263\right).
}
\tag{26}
$$
它们都在固定的 $\mathbf Q(\omega)$ 中；与 $p,\lambda,\kappa,n$
完全无关。附脚本用 (21) 的全部 $32$ 个子集精确计算 (26)，
旧 $\alpha$ 完全重现 R497(31)–(32) 的非零数。$\alpha_0$、
$\alpha_0-\alpha$、全部 $A_k,B_k$ 和六个混合矩均存于 JSON，
没有用浮点拟合或只取总 $Z$ 矩。

## 5. 新整逆测试的首项与一个固定射线引理

在固定系数整的普通处，(7) 的有限展开准确给
$$
\widehat{\mathfrak h}_p
\equiv
\mathfrak h_b(T_c/\Omega)
+\frac{\varepsilon\lambda}{1-\varepsilon\lambda}
                \mathfrak h_b(T_0/\Omega)\pmod p.
\tag{27}
$$
这是先完整展开 (7) 后得到的同系数多项式同余。
其理由是 $j\ge1$ 的整逆模 $p$ 为 $1$，而 $j=0$ 保完整分母。
没有将一个含 $p$ 的多项式系数当成固定代数数。

把 (27) 代入 (18) 的真实五输入展开，使用 (23)，得
$$
\boxed{
[T^5]\widehat{\mathcal A}_p(T)
\equiv\frac db\,
 \frac{\alpha+\varepsilon\lambda(\alpha_0-\alpha)}
      {1-\varepsilon\lambda}\pmod p.
}
\tag{28}
$$
分母已是单位；下面为两种实际 $\varepsilon$ 同时支付分子的单位性。

### 5.1 固定线性因子的射线单位引理

清 (26) 的同一正整数分母 $D_*$，置
$$
u=D_*\alpha,\qquad v=D_*(\alpha_0-\alpha)\in\mathbf Z[\omega].
\tag{29}
$$
取 $D_*$ 为这两个数的四个有理坐标分母的最小公倍数。
这是明确的固定整数；$u\ne0$，本次精确计算也给 $v\ne0$。
记 $N_u=Nu,N_v=Nv$。

若
$$
p>(N_u+N_v+1)^2,\qquad p\nmid D_*,
\tag{30}
$$
且普通处的 $u\bar\pi_0-\varepsilon v$ 不是单位，那么
$p$ 整除其有理范数，而
$$
N(u\bar\pi_0-\varepsilon v)
=N_up-\varepsilon\operatorname{Tr}(u\bar v\bar\pi_0)+N_v.
\tag{31}
$$
复绝对值给
$$
\left|\varepsilon\operatorname{Tr}(u\bar v\bar\pi_0)-N_v\right|
\le2\sqrt{N_uN_v}\sqrt p+N_v<p
$$
（最后一步由 (30)）。故该 $p$ 整除关系严格迫使
$$
\boxed{\operatorname{Tr}(u\bar v\bar\pi_0)=\varepsilon N_v.}
\tag{32}
$$
这是一个固定整数迹等式，不是仅模 $p$ 的估计。

本次完整整数证书给
$$
\begin{array}{c|ccc}
\bmod1013&\operatorname{Tr}(u\bar v)&N_v&-N_v\\ \hline
&804&834&179.
\end{array}
\tag{33}
$$
$1013\equiv2\bmod3$ 是素数，且不整除
$D_*N_uN_v$。现固定 ray 的模数没有 $1013$ 因子。
增加
$$
\boxed{\pi_0\equiv1\pmod{1013}}
\tag{34}
$$
后，$\bar\pi_0$ 也同余 $1$，(33) 同时排除 (32) 的两个号。
因此在 (30)、(34) 下准确有
$$
\boxed{\alpha+\varepsilon\lambda(\alpha_0-\alpha)\in\mathcal O^\times
\quad(\varepsilon=\pm1).}
\tag{35}
$$
(34) 是与旧 ray 兼容的实单位类，而且仍有
$g_\pi\equiv1\bmod1013$。同一个固定 ray-class 素数定理继续
给无穷多个普通有理素数。删去 (30) 的有限小素数不改变这一点。

为明确有限坏集，本篇沿用所有以前的固定例外，再删去
$D_*$、R497 的共同系数分母、$263$ 的素因子及不满足 (30)
的素数。也可一并删去 $N_uN_v$ 的素因子；它们本已小于 (30)
的门槛。所有整数及门槛均在附 JSON 完整显示。
没有把一个随 $p$ 或深度变化的坏集称为固定有限集。

## 6. 同一个新测试在原网格上仍严格非零

定义 $\widehat{\mathcal A}_p(T)$ 为 (18) 的完整原五输入积分，
使用第一权 $\log\langle TZ+\bar\gamma x\rangle$ 及整个 (7)，
且 $x$ 始终取单位。原五个 sigma 的同时深核心严格给
$$
\boxed{
\widehat C_n:=
\int_{\mathcal D_n}d\log\langle Y\rangle\,
                 \widehat{\mathfrak h}_p\,d\nu_0
=(-\lambda)^{5n}\widehat{\mathcal A}_p(\kappa^n).
}
\tag{36}
$$
低于五阶的项全部由五个独立 sigma 的质量零消失。
(28)、(35) 给第五阶单位。

余项的估值仍可直接控制：测试的总次数至多三十六，所有
(7) 系数整；对 $T^r$ 的 log 展开，分母只可能为
$1,\ldots,r$。原单位上的正负 sigma 矩均整，故
$$
v_p([T^r]\widehat{\mathcal A}_p)\ge-\lfloor\log_pr\rfloor.
\tag{37}
$$
$p\ge71$、$n\ge1$、$r>5$ 时
$rn-\lfloor\log_pr\rfloor>5n$。
因此在上述一个固定无限 ray 及固定有限例外之外，
$$
\boxed{v_p(\widehat C_n)=5n,\qquad\widehat C_n\ne0
\quad\text{对每个 }n\ge1.}
\tag{38}
$$
原 $n$ 门与 $p$ 门已分别显示；没有交换两者的量词。
整个 log 碰撞项仍在 (23)、(36) 内，只在模 $p$ 的单位判断时
使用其属于 $p\mathcal O$。

## 7. 同一合格 sigma carry 内的真实非零子管

对 $r,n\ge1$，定义真正的六输入域
$$
\boxed{\mathcal D_{r,n}=M_{A,r}\mathcal D_n.}
\tag{39}
$$
为了显示每一个隐藏条件，设
$$
\xi_j^{(r)}
=\xi_j+\frac{\kappa^{-r}-1}{3945}\bar A_j A,\qquad j=1,\ldots,6.
\tag{40}
$$
这里 $A_j$ 是 R515(16) 的全部六个实际系数。
那么 (39) 准确等价于
$$
\xi_j^{(r)}\in p^n\mathcal O\quad(j\ne x),\qquad
\xi_x^{(r)}\ {\rm unit}.
\tag{41}
$$
(40) 在 $A$ 深 $r$ 的实际像格上整，绝不在无条件全格上删除
它的分母或原输入条件。

由 (17) 的模 $p$ 值，(39) 自动满足
$A\in p^r\mathcal O^\times$、$E$ 单位、$Y_r$ 单位，
故
$$
\mathcal D_{r,n}\subset\Gamma_r
$$
确实是 (16) 的那个原 sigma 单位相消域中的子管。
同时 (12)、(13) 给完整原积分
$$
\boxed{
\int_{\mathcal D_{r,n}}
d\log\langle Y_r\rangle\,\widehat{\mathfrak h}_{p,r}\,d\nu_0
=(\psi\lambda)^r\widehat C_n,\qquad
v_p=5n.
}
\tag{42}
$$
这不是在另一个辅助来源上计算非零，也不是把两个边际拼成域：
(15) 与 (42) 的来源、第一权、有限多项式、全部归一完全相同。

## 8. 尚保留的准确补域

令
$$
\mathcal B_{r,n}=\Gamma_r\setminus\mathcal D_{r,n}.
$$
则原完整中央的准确分拆为
$$
\boxed{
(\psi\lambda)^r J'_S(0)
=(\psi\lambda)^r\widehat C_n+
\int_{\mathcal B_{r,n}}
 d\log\langle Y_r\rangle\,\widehat{\mathfrak h}_{p,r}\,d\nu_0.
}
\tag{43}
$$
若原 $J'_S(0)=0$，这里只迫使完整补域项等于
$-(\psi\lambda)^r\widehat C_n$，其赋值同样是 $5n$。
(43) 未排除这个补偿。

R515 的旧 $W$ 含 $E,K$，原几何 $\mathcal T,\mathcal U$ 也保
非零隐藏交叉。因此不能以 (9) 的平面推前替换 (41) 或
$\mathcal B_{r,n}$ 中的旧 $W$、隐藏交域条件。
下一步需要的是真正同域的混合核心或几何关系。
本篇已经支付的新增接口，是原正算术测试的有限 $E$ 单位整逆，
以及同一合格 sigma carry 中仍严格非零的完整六输入子管。

## 精确证书与依赖

- [BigInt 有理和 CM 混合矩脚本](../scripts/check-r518-original-e-unit-arithmetic-carry.js)；
  [全部固定系数、混合矩、两首项、固定整数和射线证书](../scripts/check-r518-original-e-unit-arithmetic-carry.json)。
  同一 JavaScript 主体已在当前 V8 实际执行；旧 R497 首项、
  全部 $32$ 个混合子集以及 (33) 的两个号检查通过。
  不含浮点计算，未声称在不可用环境执行 Python。
- [R515：同一原二维来源、E 完整核心及真实 sigma carry](R515-original-two-dimensional-st-source-and-same-source-sigma-carry.md)。
- [R497：固定正伴随多项式、全部第一来源与原五深网格](R497-original-degree918-positive-companion-and-six-sigma-arithmetic-grid.md)。
- [R410：原 fixed ray 的 1±lambda 整分母](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)。
