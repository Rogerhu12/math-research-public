# 实际原函数的三次微分权迹：完整尾界与统一单位

日期：2026-11-12。状态：以下 Tate 约化、全部尾项界及
$\operatorname{Tr}(H_i/L^3)\equiv1/12\pmod p$ 均已证明。
这一实际带权迹是每个目标惰性素数处的单位；
尚未证明它等于或控制中央 $J'_p(0)$。

## 1. 固定实际对象及结论

设 $p\ge7$、$p\equiv3\pmod4$，置
$$
 d=p+1,\qquad D=p(p+1),\qquad \varpi^d=p.
 \tag{1}
$$
取有限未分歧系数域 $B/\mathbb Q_p$，使其包含固定 prime-to-$p$
层标记、所需二次剩余域及本题全部常数。
使用
[实际 canonical 邻点](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)
的结论：$K$ 的全部 $d$ 个最近零点 $r_j$ 位于 $B(\varpi)$，
形成同一个 tame Galois 轨道，且 $v_p(r_j)=1/d$。

仍记
$$
 K(0)=J(0)=1,\quad L=tJ,\quad s=1-4t^2,\quad
 M=M_e=t^4+\frac72t^6+\cdots.
$$
这些均是本题已经固定的 PF 周期和实际代数模函数。
置
$$
 I(t)=\int_0^t\frac{M K}{sL^2}\,dt,\qquad I(0)=0.
 \tag{2}
$$
这正是固定惰性原函数的 $t$ 表示，不是另选一个 primitive。

本篇证明
$$
\boxed{\qquad
 \operatorname{Tr}_{B(\varpi)/B}
       \left(\frac{I(r_j)}{L(r_j)^3}\right)
       \equiv\frac1{12}\pmod{p\mathcal O_B}.
\qquad}
\tag{3}
$$
因此左侧是 $\mathcal O_B$ 的单位。
若用真实同源微分 $d_j=b_pL(r_j)$ 作权重，则对应单位为
$b_p^{-3}/12\pmod p$。
这与一次微分权的 $\operatorname{Tr}(I/L)$ 是不同的量。

## 2. 所需系数界全部来自原实际级数

由
[固定周期的完整分母计数](2026-11-12-gauss-manin-period-denominators.md)
及
[实际迭代 GM 的系数计数](2026-11-12-iterated-gm-frobenius-and-complete-inert-jets.md)，
$J$ 的所有系数满足
$$
 v_p([t^j]J)\ge-\frac jD.
 \tag{4}
$$
常数为一，所以逐项展开 $J^{-2}$ 仍满足同一加权界。
$M/t^4,s^{-1}$ 的系数在 $\mathbb Z_p$ 中，因此
$$
 A(t):=\frac{M}{t^4sJ^2}
       =\sum_{j\ge0}A_jt^j,\quad A_0=1,\qquad
 v_p(A_j)\ge-\left\lfloor\frac jD\right\rfloor.
 \tag{5}
$$
$A$ 为偶函数。

写 $K=\sum_{i\ge0}k_it^i$。其非零指标为偶数，且
$$
 k_{2n}=\frac{\prod_{a=1}^n(4a-3)^2}{(2n)!}.
$$
逐 $p^h$ 层的计数给出：每层的负贡献至多为一；
负贡献只可能在奇数 $h$ 出现，且要求 $2n\ge p^h+1$。
若用 $\nu(i)$ 计入这些可能的负层，则
$$
 v_p(k_i)\ge-\nu(i),\qquad
 \nu(i)\ge1\Longrightarrow
 i\ge p^{2\nu(i)-1}+1
      \ge d+(\nu(i)-1)D.
 \tag{6}
$$
最后一个不等式在 $\nu=1$ 是等式；每增加一层，左侧增量
至少为 $D$，所以对所有 $\nu$ 成立。
特别
$$
 k_i\in\mathbb Z_p\ (i<d),\qquad
 v_p(k_d)=-1,\qquad
 \kappa_p:=pk_d\bmod p\ne0.
 \tag{7}
$$
这里没有把 $\nu(i)$ 当成实际精确估值；所需只是上述已证下界。

由 (2)、(5)，
$$
 I'(t)=t^2K(t)A(t),\qquad
 I_m=[t^m]I=\frac1m\sum_{i+j=m-3}k_iA_j.
 \tag{8}
$$
所以 $I$ 是奇函数。

## 3. 唯一的小指标除 $p$ 风险必须用实际中央整性处理

若 $3\le m<d+3$，(8) 中所有 $k_i,A_j$ 都整。
只有奇数 $m=p$ 可能因积分除以 $m$ 引入一个 $p$ 分母。
这一步不能直接从微分的 Gauss 约化推断积分也整。

本题的实际中央展开为
$$
 \mathcal B_1(u)=\sum_{4\mid n}C_nu^n,\qquad
 C_n=\frac{n!}{24\cdot17^{n-4}}\beta_n^2,
 \quad \beta_n=[z^n]A_1(z),
 \tag{9}
$$
并且
$$
 I(t)=H_i(u(t)),\qquad
 H_i(u)=\sum_{4\mid n}\frac{C_n}{n-1}u^{n-1}.
 \tag{10}
$$
对 $n<p$，全局 Hurwitz 整性及 $n!$ 为 $p$ 单位给
$C_n\in\mathbb Z_p$。
对 $n=d=p+1$，实际半权系数 $\beta_d$ 的整性已在
[R54 的惰性半因子](../results/R54-inert-analytic-half-factor-and-central-slope.md)
证明，因而
$$
 C_d\in p\mathbb Z_p.
 \tag{11}
$$
于是 (10) 到次数 $p$ 的所有系数都整。
$K$ 的首个分母在次数 $p+1$，而 $J$ 的首个分母更晚，
故 $u(t)=tJ/K$ 到次数 $p$ 也整。代入 (10) 得到
$$
\boxed{\qquad I_p\in\mathbb Z_p.\qquad}
\tag{12}
$$
这个输入只用已经无条件证明的第一层整性，不假设
$C_d/p$ 非零，也不假设 $J'_p(0)$ 非零或 Sha 有限。

## 4. 全部较大指标的严格尾界

令 $m\ge d+3$ 为奇数，写
$$
 r=m-d-3\ge0,\qquad e=v_p(m).
$$
对 (8) 的每一项，如果 $\nu(i)=0$，则
$$
 \left\lfloor\frac jD\right\rfloor
 \le1+\left\lfloor\frac rD\right\rfloor.
$$
若 $\nu(i)\ge1$，由 (6) 有
$i+j\ge d+(\nu(i)-1+\lfloor j/D\rfloor)D$。
两种情形合起来都给
$$
\boxed{\quad
 v_p(I_m)\ge
 -1-\left\lfloor\frac{m-d-3}{D}\right\rfloor-v_p(m).
\quad}
\tag{13}
$$
因此缩放后的系数满足
$$
 v_p(I_m)+\frac{m-3}{d}
 \ge\frac rd-\left\lfloor\frac rD\right\rfloor-e.
 \tag{14}
$$

若 $r=0$，$m=p+4$ 与 $p$ 互素，右边为零。
若 $r>0,e=0$，右边至少为
$r(p-1)/(pd)>0$。

若 $e=1$，这里 $m$ 为奇数非常重要：
$m\ge p+4$ 且 $p\mid m$ 迫使 $m\ge3p$，不是 $2p$。
故 $r\ge2p-4$，并且对 $p\ge7$，
$$
 \frac{r(p-1)}{p(p+1)}
 \ge\frac{(2p-4)(p-1)}{p(p+1)}>1=e.
$$
若 $e\ge2$，则 $m\ge p^e$，而
$$
 \frac{(p^e-p-4)(p-1)}{p(p+1)}>e.
$$
最后一个不等式在 $p=7,e=2$ 已严格成立；
增大 $p$ 保持成立，$e$ 每增一时左侧增量大于一。
所以 (14) 在所有 $m>d+3$ 处严格为正。
同一界随 $m$ 至少线性增长再减去 $\log_p m$，故趋于无穷。
这证明所需的 Tate 收敛，不能只写“每项有正赋值”代替收敛。

对 $3<m<d+3$，除 $m=p$ 外系数整；
$m=p$ 则用 (12)。其缩放赋值同样严格正。
因此所有指标均已处理，没有略去积分造成的潜在共振项。

## 5. 准确 Tate 约化及完整有限迹

由以上全部界，
$\varpi^{-3}I(\varpi X)$ 属于闭单位盘的 Tate 代数。
只有 $m=3$ 与 $m=d+3$ 能留下非零约化。
前者为 $I_3=1/3$。后者由 (8) 得
$$
 pI_{d+3}\equiv\frac{\kappa_p}{p+4}
       \equiv\frac{\kappa_p}{4}\pmod p,
$$
因为 (8) 中只有 $k_dA_0$ 含一个 $p$ 分母。
于是
$$
\boxed{\qquad
 \overline{\varpi^{-3}I(\varpi X)}
       =\frac{X^3}{3}+\frac{\kappa_pX^{d+3}}4.
\qquad}
\tag{15}
$$
这不是对任意 $M=t^4+\cdots$ 的形式积分都自动成立；
小指标 $m=p$ 已在 §3 用实际 $C_d$ 的整性严格处理。

真实邻点满足
$$
 \overline{K(\varpi X)}=1+\kappa_pX^d,\qquad
 \overline{L(\varpi X)/\varpi}=X.
$$
在任一根上 $X^d=-\kappa_p^{-1}$，所以
$$
 \overline{\frac{I(r_j)}{\varpi^3}}
      =\frac{\bar X_j^3}{12},\qquad
 \overline{\frac{I(r_j)}{L(r_j)^3}}=\frac1{12}.
 \tag{16}
$$
每一项 $I(r_j)/L(r_j)^3$ 都整。全部根恰为同一个
$B(\varpi)/B$ 的 Galois 轨道，因此其和是真正的域迹。
将 (16) 求和，迹与 $d/12$ 的差属于
$\varpi\mathcal O_{B(\varpi)}\cap B=p\mathcal O_B$。
再用 $d=p+1\equiv1\pmod p$，得到 (3)。

## 6. 与中央行仍需区分的准确事项

同一估值分析只给
$$
 \operatorname{Tr}_{B(\varpi)/B}(I/L)\in p\mathcal O_B.
$$
它除以 $p$ 后的实际值需要再保留一层精度；
本篇没有从最低 Gauss 约化猜测那个值。
$I/L^2$ 为奇函数，其迹由正负根配对恒为零；
$I/L^3$ 则由 (3) 是单位。

因此同一个原函数的不同微分权迹可以分别恒零、被 $p$ 整除、
或恒为单位。只有先证明指定权迹与实际中央 Bockstein 或完整
$J'_p(0)$ 的准确比较，才能把其中的非零用于 Sha。
本篇付清了三次权的全尾界和实际有限域迹；没有预先假定
这个尚未建立的比较。
