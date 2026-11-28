# R1210：原最高纯尖点返回的全素数首对数单位

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route。

**已证明。** 以下应用依赖 R1209 对同一个原 Čech 配对的完整比较。本文独立支付其指定返回向量的准确系数及全素数单位性，在原实际纯尖点格上得到明确单位；不将它直接称为整个 Mordell–Weil 空间的法向单位。

## 1. 同一个原纯尖点格与返回

保持
$$
p=12g-1>37,\quad n=2g-1,\quad m=3n+2=(p-1)/2,
\quad r=1-b^3,\quad A(b)=bQ(b^3),
$$
$$
Q_0=Q(0)=\binom mn,\qquad A_1=A(1)=-Q_0.
\tag{1210.1}
$$
原算子及实际整格仍为 R1204–1205 的
$$
\mathscr D T=rT''-4b^2T'-\frac94bT,\qquad
C(T)=-3\gamma^2\mathscr D T,
$$
$$
q=e_{V_m}e_N,\qquad
\operatorname{bot}:q\Gamma/pq\Gamma\xrightarrow{\sim}\ker\mathfrak c,
\qquad \operatorname{im}C=\ker\mathfrak c.
\tag{1210.2}
$$
这里的 $C(T)$ 是返回算子的记号；不要与此前选定的有理简单阿贝尔商 $C$ 混同。选取一个具体原高 PS 输入
$$
T_0(b)=b^2r^{n-1}.
\tag{1210.3}
$$
它属于整个允许空间 $b^2k[b^3]_{\le n-1}$，次数 $3n-1=m-3\le m-2$。R1204 的原 Hodge base change、有限角与特征投影给实际整提升 $\Psi_0$；R1202–1205 给
$$
\Omega_0=q(\pi_0^{e_0-p}\Psi_0)=\pi_0^{-p}U_m\Psi_0\in q\Gamma,
\qquad \operatorname{bot}(\bar\Omega_0)=C(T_0).
\tag{1210.4}
$$
不另造有理 projector 的整性，也不把 packet 的任意底当作纯尖点底。

原点仍为 $P=(p-1)D_0$。R1209 的完整首泛函公式，以该文同一 CM good period 写为
$$
\mathcal V_m(S)=-\frac{8\,2^m\nu}{A_1}\,e_n(S),
\qquad S(b)=\mathsf S(b^3),\qquad\deg\mathsf S\le n.
\tag{1210.5}
$$
它已经包含原 SS、三个支持 CM 支的 analytic 项以及 static node frame。下文只计算这个同一 $e_n$，不再删除任何边界。

## 2. 同一 CM period 中的原 exact primitive

在 $b=1$ 取原 good 坐标
$$
X=v^3=1-b^3,\quad b=(1-X)^{1/3},\quad
F(X)={}_2F_1\!\left(\frac16,\frac16;\frac23;X\right),
$$
$$
q_0(X)=\frac{Q(X)}{Q_0},\quad
G(X)=(1-X)^{1/3}q_0(X),\quad
t=v\frac{G(X)}{F(X)},\quad Y=t^3.
\tag{1210.6}
$$
这里的有限 hypergeometric jet 都截在实际需要的小于 $p$ 的次数；没有引入特征 $p$ 的全局第二水平解。$Q(1-X)=-Q(X)$，因此 $G=A(b)/A_1$，正是原 CM good 的第二解系数。

对一个原高 PS 输入 $T$ 置
$$
R(t)=\frac{T(b(t))}{A(b(t))}.
$$
R1206 的同一函数 $f_T=(r/u)(T/A)'$ 满足
$df_T=\mathscr D T\,db/(uA)$。在 R1209 锁定的实际 fine 参数 $t=cW^m$ 中，它成为
$$
f_T=-\tau^{-1}W^{-m-1}\,tR'(t),\qquad
\frac{S\,db}{uA}=\tau^{-1}W^{-m-1}E_S(t)\,dt,
$$
$$
E_S(t)=-\frac{v^2F(X)^3}{A_1}S(b(t))
       =\sum_{j\ge1} e_{j-1}(S)t^{3j-1}.
\tag{1210.7}
$$
所有 $c,\tau$ 都是原节点单位；它们在以下同源比较中准确消去。
直接对 $f_T$ 求导，使用 $dt=m t\,dW/W$，得
$$
E_{\mathscr DT}(t)=\frac1mR'(t)-tR''(t)
                 =-(tR(t))'',
\tag{1210.8}
$$
其中第二等式用 $m=-1/2$ 于 $k$。此处并没有把 exact centre 微分当成整个原 Picard 对数为零。

因为 $3(n+1)=m+1$，准确有
$$
e_n(\mathscr DT)
=-(m+1)(m+2)[Y^{n+1}]R
=-\frac34[Y^{n+1}]R.
\tag{1210.9}
$$

## 3. 两个有限 jet 给出指定返回值

对 $T_0$，(1210.6) 给
$$
R=-\frac1{Q_0}X^{n-1}h(X),\qquad
h(X)=\frac{(1-X)^{1/3}}{q_0(X)},\qquad
Y=X\left(\frac G F\right)^3.
\tag{1210.10}
$$
令 $k=n+1$。在特征 $p$ 中 $k=1/6$，且 $3k=m+1=1/2$。Lagrange 的有限系数公式只需下面两个 jet：
$$
F=1+\frac X{24}+\frac{49X^2}{2880}+O(X^3),
$$
$$
q_0=1+\frac{25X}{48}+\frac{3025X^2}{8064}+O(X^3),\qquad
G=1+\frac{3X}{16}+\frac{81X^2}{896}+O(X^3).
\tag{1210.11}
$$
这些值分别由同一 CM Picard–Fuchs 与 Jacobi 递推逐项给出。相关分母仅有素因子 $2,3,5,7$，故在当前全部 $p>37$ 范围内合法。

写 $h=1+h_1X+h_2X^2+\cdots$ 以及
$a=(F/G)^{3k}=1+a_1X+a_2X^2+\cdots$，得到
$$
h_1=-\frac{41}{48},\qquad h_2=-\frac{667}{16128},
\qquad a_1=-\frac7{96},\qquad a_2=-\frac{16567}{645120}.
\tag{1210.12}
$$
例如 $F/G$ 的二阶系数是 $-3713/80640$；取平方根后再减一次二次项，正给上述 $a_2$，没有忽略变量反演的二阶贡献。

Lagrange 公式逐项为
$$
[Y^k]R
=-\frac1{kQ_0}[X^2]\big((k-2)h+Xh'\big)a
=-\frac1{Q_0}\big(h_2-5h_1a_1-11a_2\big).
\tag{1210.13}
$$
原 $k$ 为非零，所有提取次数及除数均在安全范围。最后这个括号准确是
$$
h_2-5h_1a_1-11a_2
=\frac{-26680-200900+182237}{645120}
=-\frac{45343}{645120}.
$$
因此
$$
\boxed{
[Y^{n+1}]R=\frac{45343}{645120Q_0},\qquad
e_n(\mathscr DT_0)=-\frac{45343}{860160Q_0}.
}
\tag{1210.14}
$$

## 4. 全部本分支素数的单位性，无例外扫描

分母 $860160=2^{13}\cdot3\cdot5\cdot7$ 在全部当前素数上为单位；$Q_0$ 的 factorial 参数严格小于 $p$，同样为单位。分子具有准确恒等式
$$
45343=166^2+3\cdot77^2,\qquad \gcd(166,77)=1.
\tag{1210.15}
$$
对 $p\equiv11\pmod{12}$，有 $p\equiv2\pmod3$，所以 $-3$ 在 $\mathbf F_p$ 中不是平方：否则 $(-1+\sqrt{-3})/2$ 将是一个非平凡三次单位根，迫 $3\mid p-1$。若 $p\mid45343$ 且 $77\not\equiv0$，(1210.15) 就给一个 $-3$ 的平方根；若 $77\equiv0$，则亦 $166\equiv0$，与互素矛盾。因此 $45343$ 在整个本分支上为单位。

这个论证不需要声称 $45343$ 是素数，不需要有限素数扫描，也不留下一个未经检查的异常素数集合。

## 5. 原纯尖点格上的完整首值

将 (1210.14) 代入 (1210.5)，并保 $A_1=-Q_0$ 与原返回的 $-3\gamma^2$，得
$$
\boxed{
\mathcal V_m(\mathscr DT_0)
=-\frac{2^m\nu\,45343}{107520Q_0^2},
\qquad
\mathcal V_m(C(T_0))
=\frac{\gamma^2 2^m\nu\,45343}{35840Q_0^2}
\in k^\times.
}
\tag{1210.16}
$$
这正是 (1210.4) 的实际整纯尖点提升的值。故
$$
\boxed{\mathcal V_m|_{\ker\mathfrak c}\ne0.}
\tag{1210.17}
$$
更准确地，原 $q\Gamma$ 上的已归一首对数泛函含一个单位值，因而是本原的。R1196 的同底最高 eigenlift 独立性保证这个结论不依赖对 $\Psi_0$ 所作的允许整提升。

这里不要求 $\mathfrak c(T_*)=0$，也没有将 $T_*=-r^n$ 从整个 packet 直接塞入纯尖点格。使用的是已有真实返回算子及它的明确输入 $T_0$。

## 6. 已付范围与继续的原接口

本篇消去 R1205 (1205.18) 留下的最高纯尖点首列非零问题，且给原格上的明确单位。它仍没有将该值自动运输到一个预先指定的有理简单商 $C$，也没有把对一个点 $P$ 的泛函直接称为整个 Mordell–Weil 空间的消灭子。后续仍须保持原实际 Hecke、极化、$\Pi$ 与 $\Phi$ 的格比较及所有 CM jet。

全部为同一已登记来源上的纸面推导。root 与 global_route 独立核 (1210.11)–(1210.14) 的每个二阶系数与最终符号；没有数学程序执行或新增已完成窗口。

## 来源

- R1204：原 $\pi_0^{-p}U_m$ 的整返回与 $C(T)=-3\gamma^2\mathscr DT$。
- R1205：实际纯尖点秩、$q\Gamma$ 的整基及 $\operatorname{bot}\simeq\ker\mathfrak c$。
- R1206：同一原中心函数域的显示 primitive $f_T$。
- R1208：原 CM node static frame 与 canonical CM 相位；旧 SS 数值的范围更正。
- R1209：一般 $S$ 的完整 CM/SS 收缩及 (1210.5) 的同源顶层公式。
