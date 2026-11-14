# 固定 61 的 Artin 生成元与完整整数增广比较

日期：2026-11-12。**状态：已证明；R128。**

本篇给 R123/R124、R126 的实际辅助扩张增加一个共同规范：
固定同一个范数为 $61$ 的主理想，其 Artin 元生成每个所选
$C_p$ 商。相应差分与原平衡增广算子在**完整整数**
Mordell–Weil 群上的各次像完全相同。这不证明指定 Heegner 点
不在该像中。

## 1. 固定理想及其真实环类像

固定
$$
 F=\mathbf Q(d),\qquad d^2=-15,\qquad
 \beta=1+2d,\qquad \mathfrak b=(\beta),\qquad N\mathfrak b=61,
 \qquad \gamma=\beta/\bar\beta.
 \tag{1}
$$
$\mathfrak b$ 是 $F$ 的整数环中的素理想，$\gamma$ 不是单位根：
$F$ 中的单位根只有 $\pm1$，而 $\beta/\bar\beta\ne\pm1$。

设 $\ell\equiv-1\pmod {1020}$ 为素数，$\ell\ne61$，且
$$
 \ell+1=pu,\qquad p\text{ 为奇素数},\qquad p\nmid u.
 \tag{2}
$$
记 $\mathcal O_\ell=\mathbf Z+\ell\mathcal O_F$，$H_\ell=F[\ell]$
为环类域，$L=L_{p,\ell}$ 为其中的唯一 $p$ 次子扩张，
$\Gamma=\operatorname{Gal}(L/F)$。

这里 $\ell$ 在 $F$ 惰性，且 $h_F=2$。实际环类正合列为
$$
 1\longrightarrow
 (\mathcal O_F/\ell\mathcal O_F)^\times/
                  (\mathbf Z/\ell\mathbf Z)^\times
 \longrightarrow\operatorname{Pic}(\mathcal O_\ell)
 \longrightarrow\operatorname{Pic}(\mathcal O_F)
 \longrightarrow1.
 \tag{3}
$$
为固定 (1) 在 (3) 中的位置，使用素于 $\ell$ 的
$\mathcal O_F$ 理想描述环类群。其主理想关系是生成元模 $\ell$
为非零有理剩余类的主理想。因此核中 $(\alpha)$ 的类由
$\alpha\bmod\ell$ 确定；两个生成元给相同类恰当其比模 $\ell$
属于 $\mathbf F_\ell^\times$，因为 $\mathcal O_F^\times=\{\pm1\}$。
每个最大阶主理想类均可如此表示，给出 (3) 的核和映射。
延拓、收缩素于导子的可逆理想给其余两项。这个标准描述也见
Cox（1989），§7，式 (7.25)、(7.27)。

特别地，$\mathfrak b$ 的最大阶理想类平凡，其环类像在 (3)
的循环核中。有限域同构
$$
 \mathbf F_{\ell^2}^{\times}/\mathbf F_\ell^\times
 \ \xrightarrow{\ \sim\ }\
 \mathcal T_\ell:=\{x\in\mathbf F_{\ell^2}^{\times}:x^{\ell+1}=1\},
 \qquad [x]\longmapsto x/x^\ell
 \tag{4}
$$
将该像送到 $\gamma\bmod\ell$。若采用反向 Artin 约定，得到
它的逆；下述等价条件不受影响。因为 (3) 的核阶为 $pu$、
余商阶为 $2$，其唯一 $p$ 次商就是 $\Gamma$，核在
$\mathcal T_\ell$ 中是阶 $u$ 的子群。故
$$
 \sigma_{\mathfrak b}:=\operatorname{Art}_{L/F}(\mathfrak b)=1
 \quad\Longleftrightarrow\quad
 \gamma^u\equiv1\pmod\ell
 \quad\Longleftrightarrow\quad
 \beta^u-\bar\beta^u\equiv0\pmod{\ell\mathcal O_F}.
 \tag{5}
$$
这是实际环类商的条件，不是任意选取一个有限域角色。
由于 $\#\Gamma=p$，$\sigma_{\mathfrak b}\ne1$ 即表示它生成 $\Gamma$。

## 2. 一个固定 Lucas 整数乘积吸收全部坏候选

令
$$
 U_0=0,\quad U_1=1,\quad U_{n+2}=2U_{n+1}-61U_n.
 \tag{6}
$$
$\beta,\bar\beta$ 是 $X^2-2X+61$ 的两根，所以
$$
 \beta^n-\bar\beta^n=4d\,U_n,\qquad
 D_n:=N_{F/\mathbf Q}(\beta^n-\bar\beta^n)=240U_n^2>0
 \quad(n\ge1).
 \tag{7}
$$
严格正性来自 $\gamma$ 非单位根。复绝对值给
$$
 0<D_n=|\beta^n-\bar\beta^n|^2\le4\cdot61^n.
 \tag{8}
$$
对整数 $V\ge1$ 取 $\mathscr D(V)=\prod_{1\le n\le V}D_n$，则
$$
 \log\mathscr D(V)
 \le \frac{V(V+1)}2\log61+V\log4=O(V^2).
 \tag{9}
$$
由 (5)，任一满足 $u\le V$ 而 $\sigma_{\mathfrak b}=1$ 的辅助
素数都整除这个同一个非零整数 $\mathscr D(V)$。实际上惯性
$\ell$ 的范数给 $\ell^2\mid D_u$，但下面只使用 $\ell\mid D_u$。
对 $\ell\ge Y^\epsilon$、固定 $\epsilon>0$，坏候选数量至多
$$
 O_\epsilon(V^2/\log Y).
 \tag{10}
$$
这里没有随 $p$ 改变代数数，也没有先假设一个非 Wieferich 定理。

## 3. 与两套已证辅助素数选择同时成立

### 3.1 R123/R124 的相对密度一输入

固定 $32/17<\theta<2$。沿 R123 取
$p\in(X,2X]\cap\mathcal P_F$、$X^\theta<\ell\le2X^\theta$、
$\ell\equiv-1\pmod{1020p}$。此时
$u\le V=O(X^{\theta-1})$，所以 (10) 新删去的辅助素数至多
$$
 O(X^{2\theta-2}/\log X).
 \tag{11}
$$
每个候选 $\ell$ 至多属于一个该区间内的 $p$，因为
$\ell+1<X^2$ 对充分大 $X$ 成立；而 R123 的典型输入各有
$\gg X^{\theta-1}/\log X$ 个候选。因此仅由这次删除造成的
失败输入至多 $O(X^{\theta-1})=o(X/\log X)$。

把 (11) 与 R123 已付的实际全迹/首 jet 坏集合，以及 R121、
R124 的固定点分母坏集合取并集，原证明的总预算不变。
所以可在其相对密度一的结论中同时要求
$$
                  \Gamma=\langle\sigma_{\mathfrak b}\rangle.
 \tag{12}
$$
对 R124，两条曲线使用的是同一 $L/F$；(12) 同时适用于它们。
本段保持原输入集合 $\mathcal P_F$，没有扩大其密度结论的范围。

### 3.2 R126 的任意约化型无穷输入

沿 R126 取固定同余类中的
$$
 \ell\le Y,\quad p=P^+(\ell+1)>Y^{667/1000},\quad
 u\le V=O(Y^{333/1000}).
 \tag{13}
$$
这些 $\ell$ 至少为 $Y^{667/1000}-1$。所以 (10) 新删去至多
$$
 O(Y^{666/1000}/\log Y)=o(Y/\log Y)
 \tag{14}
$$
个候选。R126 原有 $\gg Y/\log Y$ 个候选；其全迹、正局部化、
负局部化三类坏集合也均为 $o(Y/\log Y)$。故同时保留 (12)
后，仍有同样数量下界，原无穷多个不同 $p$ 以及
$$
 Q\ne O,\quad r_+=r_-=1,\quad
 \widehat h(Q)\ll p^{666/667}\log p=o(p)
 \tag{15}
$$
全部保持。本段没有增加 $p$ 普通、在 $F$ 分裂或在
$\mathbf Q(i)$ 分裂的条件。

相同证明还允许同时指定有限多个固定主素理想
$(\beta_j)$，只要 $\beta_j/\bar\beta_j$ 非单位根：
将各自的 (9) 取有限乘积，仍为 $O(V^2)$。常数允许依赖这些
固定理想；不对随 $p$ 增长的理想集合作声明。

## 4. 在完整整数 Mordell–Weil 群上的同一增广像

令 $E/F$ 为本题任一固定曲线，
$$
 A=\ker\!\left(N:\operatorname{Res}_{L/F}E\longrightarrow E\right).
 \tag{16}
$$
该核是连通阿贝尔簇。取原生成元 $\tau\in\Gamma$，令
$N_\Gamma=1+\tau+\cdots+\tau^{p-1}$。在 Weil restriction 上，
$N_\Gamma$ 是范数后接对角嵌入；所以其在 $A$ 上为零。因此
$$
 \mathbf Z[T]/(\Phi_p(T))\longrightarrow\operatorname{End}_F(A),
                    \qquad T\longmapsto\tau
 \tag{17}
$$
是一个整环作用，且 $T$ 的像为自同构。

由 (12) 写 $\sigma_{\mathfrak b}=\tau^k$，$1\le k\le p-1$。
令 $l\in\{1,\ldots,p-1\}$ 满足 $kl=1+rp$。整多项式
$$
 u_k(T)=1+T+\cdots+T^{k-1},\qquad
 v_k(T)=1+T^k+\cdots+T^{k(l-1)}
 \tag{18}
$$
满足
$$
 u_k(T)v_k(T)=\sum_{j=0}^{kl-1}T^j
                 \equiv1\pmod{\Phi_p(T)}.
 \tag{19}
$$
最后一步把前 $rp$ 项分成 $r$ 个长度 $p$ 的块，并使用
$T^p\equiv1$。所以 $u_k(\tau)$ 的逆就是整同源
$v_k(\tau)$；它们实际是 $F$ 上的阿贝尔簇自同构。
这比仅在 $\mathbf Z_p[\zeta_p]$ 中证明单位更强。

对原平衡算子及固定 Artin 差分
$$
 \delta=\tau^{(p-1)/2}(\tau-1),\qquad
 \Delta_{61}=\sigma_{\mathfrak b}-1
 \tag{20}
$$
有
$$
 \Delta_{61}
   =\tau^{-(p-1)/2}u_k(\tau)\,\delta.
 \tag{21}
$$
其中乘子是与 $\delta$ 交换的整自同构。因此对所有 $n\ge0$，
$$
 \boxed{\Delta_{61}^{\,n}A(F)=\delta^nA(F).}
 \tag{22}
$$
等式包含全部挠点，不需先去挠或张量 $\mathbf Z_p$。通过
$A(F)=\ker(N:E(L)\to E(F))$，它正作用于既有的真实范数零点。
特别地，对实际完整 Heegner 点，
$$
 Q\in\delta^2A(F)\quad\Longleftrightarrow\quad
 Q\in(\operatorname{Art}_{L/F}(\mathfrak b)-1)^2A(F).
 \tag{23}
$$
整数群与其 $p$ 进完成之间还可给出准确等价。分圆恒等式
$$
 \prod_{j=1}^{p-1}(1-T^j)\equiv p\pmod{\Phi_p(T)}
$$
及 (18)–(21) 说明在 $A$ 上
$[p]=\epsilon\delta^{p-1}$，其中 $\epsilon$ 是整自同构。
故若 $r(p-1)\ge n$，则
$p^rA(F)\subset\delta^nA(F)$。Mordell–Weil 有限生成性遂使
$A(F)/\delta^nA(F)$ 为有限 $p$ 群。张量 $\mathbf Z_p$ 的右正合性，
以及有限 $p$ 群与其 $\mathbf Z_p$ 张量相同，给
$$
 \frac{A(F)}{\delta^nA(F)}
 \ \xrightarrow{\ \sim\ }\
 \frac{A(F)\otimes\mathbf Z_p}
      {\delta^n(A(F)\otimes\mathbf Z_p)}.
 \tag{24}
$$
因此 R119–R126 中实际指数 $a$ 满足完整的双向判据
$$
 \boxed{a\ge n
 \quad\Longleftrightarrow\quad Q\in\delta^nA(F)
 \quad\Longleftrightarrow\quad Q\in\Delta_{61}^{\,n}A(F).}
 \tag{25}
$$
这里使用了真实有限 $p$ 商，而非把一般整数可除性无条件
与某一个完备后的可除性等同。

## 5. 新规范的用途与尚未证明的输入

所有 $L/F$ 都在 $61$ 处不分歧。因而可以固定同一素理想
$\mathfrak b$ 的 Artin 元于这些扩张的合成域，再限制到各
$L$；(20) 的差分不再依赖为每个 $p$ 任意选一个生成元。
不需要在会于 $61$ 分歧的整个 $F^{\rm ab}$ 上声称一个
规范 Frobenius。

现在尚需证明的是：对于原固定模参数化的实际 $Q$，
固定差分 $\Delta_{61}$ 的整数像不能包含它，或给出能排除
$a=2$ 的真实全局饱和证书。(22) 本身只是把这个问题规范到
一个固定 Artin 操作；没有检测它，也不改变主目标未完成的状态。

## 依据与定位

- David A. Cox，*Primes of the Form $x^2+ny^2$*（1989），
  §7、式 (7.25)、(7.27)，印 pp.147–148：
  [原书扫描](https://www.math.utoronto.ca/~ila/Cox-Primes_of_the_form_x2%2Bny2.pdf)。
  此处只使用素于导子理想的环类正合列；第 1 节已写出本题所需映射。
- [R123](../results/R123-sparse-zero-moments-and-explicit-modulus.md)：
  实际零矩与显式 $1020p$ 同余，沿用其已核的 Mikawa–Fouvry 输入。
- [R124](../results/R124-two-curve-negative-localization.md)：
  两条固定曲线的共同辅助素数及固定分母乘积。
- [R126](../results/R126-large-prime-factors-and-two-local-signs.md)：
  已核 Fouvry（1985）、Fouvry–Tenenbaum（1996）勘误的
  固定进程大素因子输入；第 3.2 节只增加一个更小的坏集合。
- [R119](../results/R119-character-spectrum-and-norm-one-sha-finite.md)、
  [R122](../results/R122-finite-norm-sha-delta-layers-and-local-signs.md)：
  实际范数一簇、平衡 $\delta$ 与整格指数。第 4 节的自同构证明
  直接在整数群环中完成，不附加 Selmer 或高度猜想。
