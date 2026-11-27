# R1051 — 原完整 Gaussian 矩阵的全深数字折回与全部精度同源节点递推

日期：2026-11-27。**状态：以下全深行恒等式、全部精度递推及真实前缀推论已证明。主全局严格预算仍未完成。**

本篇从 R618 的同一实际 regular 余项出发，读取所有物理行，而不只首 $p^2$ 窗。结论有两层：基线目标中的高行模 $p$ 按 $p$ 进数字和准确折回旧行；全部模 $p^H$ 行则由一个显示的、阶约 $pH$ 的同源节点递推控制。后者保留每一原 regular 系数和同一来源向量，不把 Euler/Hasse 槽加入原矩阵。

这给随深度增长的真实前缀整除，但下文明确计算：本篇所支付的总收益仍是 $O(M_D)$，尚未超过原 $3M_D\log D$ 门。原 canonical 坏条件另保为完整加权行，不能从递推本身推成逐节点消失。

## 1. 原来源、全部列与两个真正整目标

固定原好惰性范围
$
p=6s-1>101,\qquad
L=s(p-1)=\frac{p^2-1}{6},\qquad
w=z^6.
\tag{1}
$
所有固定来源的坏分母仍排除。系数环 $\mathcal O$ 非分歧，赋值规范为 $v_p(p)=1$。

令 $a\in\mathcal O^\times$ 是同一原 Gaussian 单位。对原来源格中的 $P$，按其**实际整数 charge** 分组：
$
\Phi(P)(w)=\sum_{m\in\mathcal I_D}
 A_m(P;w)\exp\!\left(\frac{ma}{p}w^s\right),
\qquad
A_m(P;w)=\sum_{n\ge0}A_{m,n}(P)w^n.
\tag{2}
$
这里 $\mathcal I_D\subset\mathbf Z$ 有限，$A_{m,n}$ 是原系数格上的固定线性泛函，不是自由输入。

具体地，R418 的 $E_D=\mathcal O[S,T]_{\le D}$ 使用 $a=pc_\sigma$、$m=34\mu+72\nu$，以及
$
A_m(P;w)=
 \sum_{34\mu+72\nu=m}c_{\mu,\nu}
 w^{\mu+\nu}B_{34}(w)^\mu B_{72}(w)^\nu.
$
R612/R646 的 $G_0\mathcal W_D$ 使用同篇 $a$、$m=n+40$，且完整
$
c_*w^{13}U_0(w)\,g(w)^nq_n(t(w))f_n(t(w))
$
仍在 $A_m$ 内。原 $q_n$ 的全部角、固定分母、$P_{134}$、charge 四十和十三行均未删除。

设
$
\alpha=\frac{6p}{p^2-1},\qquad
b_*=\frac{6(2p-1)}{p(p^2-1)},\qquad
\vartheta=b_*s=\frac{2p-1}{p(p-1)},\qquad
\eta=1-\vartheta,\qquad\tau_2=b_*/6.
\tag{3}
$
R618 §5 的真实 Gauss 范数给每一列、全部 $n$ 的统一界
$
v_p(A_{m,n}(P))\ge-\lfloor b_*n\rfloor
\quad\text{当 }\|P\|_{\rm source}\le1.
\tag{4}
$
对 $G_0\mathcal W_D$，这是 R646 的同一余项证明：$t/w$、$g$、固定 $U_0$ 及 $q_n(t)/t^{A_n}$ 在 R618 严格内闭盘均为原范数一单位；取乘积及半径极限即得 (4)。任意正整数幂和已付单位的逆都保范数一，因此不需 $D<p$，也不需 $m$ 为 $p$ 单位。原 $w^{13}$ 及各列正首阶只使界更强。

基线全行目标为
$
\mathscr B_e=
 \left\{\sum f_nw^n:
 v_p(f_n)+e(n)\ge0\right\},
\qquad e(n)=\lfloor\alpha n\rfloor .
\tag{5}
$
因 $e(i)+e(j)\le e(i+j)$，它是真正的系数整环。所有无限行断言也可逐个有限截断理解，不用任何无限矩阵的 Smith 形式。

唯一写法
$
n=r+sq,\qquad 0\le r<s,\quad q\ge0
$
还给第二个**线性目标**：
$
d(n)=q+v_p(q!),\qquad
\mathscr B_d=\left\{\sum f_nw^n:
v_p(f_n)+d(n)\ge0\right\}.
\tag{6}
$
本篇不称 $\mathscr B_d$ 为环。后面直接证明原 $\Phi(P)\in\mathscr B_d$，而非从 (5) 免费降低行缩放。

## 2. 全深模 $p$ 数字折回

首先
$
\alpha-b_*=\frac{6(p-1)}{p(p+1)}.
$
对 $j=s$，有 $e(s)=1$、$\lfloor b_*s\rfloor=0$。对 $j\ge s+1$，
$
(\alpha-b_*)j>1.
$
因此 (4) 的全部 regular 尾满足
$
A_m(P;w)-\sum_{0\le j<s}A_{m,j}(P)w^j
 \in p\mathscr B_e.
\tag{7}
$
这是全尾估计；第二 Gaussian 和更高坏带没有被删掉，而是按同一目标实际进入 $p\mathscr B_e$。

另一方面，对每个整数 $m$，
$
\exp(maw^s/p)\in\mathscr B_e.
$
确实第 $sq$ 项的正规化赋值至少为
$
e(sq)-q-v_p(q!)
 =\left\lfloor\frac{s_p(q)}{p-1}\right\rfloor\ge0.
$
故可将 (7) 乘回整个原 Gaussian。

置
$
h=s_p(q),\qquad
\epsilon(r,q)=e(r+sq)-q-v_p(q!)
 =\left\lfloor\frac{h+pr/s}{p-1}\right\rfloor,
\qquad
u_q=\frac{p^{v_p(q!)}}{q!}\in\mathcal O^\times.
\tag{8}
$
由 (7) 得同一个原 $P$ 的全深行：
$
p^{e(r+sq)}[w^{r+sq}]\Phi(P)
 \equiv p^{\epsilon(r,q)}u_q a^q
       \sum_m m^q A_{m,r}(P)\pmod p.
\tag{9}
$
所以 $\epsilon(r,q)\ge1$ 时该行准确为零。

若 $\epsilon(r,q)=0$，则 $h<p$、$\epsilon(r,h)=0$，并且
$
r+sh<L.
$
对 $r=0$，条件是 $h\le p-2$；对 $r>0$，它是 $h+6r\le p-1$，从而 $r+sh\le L-pr<L$。

将 $q=\sum q_\ell p^\ell$，标准阶乘单位递推由
$
q!=p^{\lfloor q/p\rfloor}\lfloor q/p\rfloor!
 \prod_{\substack{1\le i\le q\\p\nmid i}}i
$
及每一整块的 Wilson 乘积逐次给出
$
u_q\equiv
 (-1)^{v_p(q!)}\prod_\ell(q_\ell!)^{-1}\pmod p.
$
又 $m^q\equiv m^h\pmod p$，包括 $p\mid m$；$q=0$ 时按 $0^0=1$ 处理。因此
$
\boxed{\;
\overline{p^{e(r+sq)}[w^{r+sq}]\Phi(P)}
 =
(-1)^{v_p(q!)}
\frac{h!\,\bar a^{\,q-h}}{\prod_\ell q_\ell!}\,
\overline{p^{e(r+sh)}[w^{r+sh}]\Phi(P)} .
\;}
\tag{10}
$
显示标量是单位。在原有理 $b=17$ 或共同有理 frame 上，$\bar a\in\mathbf F_p^\times$，故 $\bar a^{q-h}=1$。一般非分歧单位则保这个因子。

(10) 对所有 $D,q$ 同时成立：高物理深度没有增加基线模 $p$ 行空间。

### 2.1. 与 R612 原全格的准确关系

在 $0\le n<L$ 上，
$
\lfloor6pn/(p^2-1)\rfloor=\lfloor6n/p\rfloor,
$
因为两实数之差小于 $1/p$，而 $6n/p$ 的非整数小数部分离下一整数至少 $1/p$。

R612 首 $ps$ 目标在 $n=L$ 比 (5) 少一次 $p$，但原 $G_0\mathcal W_D$ 的该模 $p$ 行本来为零：R612(10) 的 $r=0$ 项有原 $A_{m,0}=0$。在其余 $L<n<ps$ 行，目标缩放相同，且已由 R612 的带权理想杀掉。因此该原全格的基线**任意物理深度**核仍准确为
$
\boxed{\;
\ker\overline{\Phi:\mathcal W_D\longrightarrow\mathscr B_e}
 =
\{\bar P:d^{C_D}\bar P\in I_{p-78}(t,Y-1)\}.
\;}
\tag{11}
$
此处只延长同一基线整目标的行数，不把旧三块 $M$ 的商核换成 (11)，也不把该局部理想添作全局来源。

## 3. 所有精度的原系数与准确节点公式

对同一原 $P$ 定义实际行
$
\mathcal Y_{r,q}(P)=p^q q!\,[w^{r+sq}]\Phi(P).
\tag{12}
$
由原指数乘法，有特征零准确有限和
$
\mathcal Y_{r,q}
 =
\sum_m\sum_{i=0}^q
 p^i(q)_i(ma)^{q-i}A_{m,r+si},
\qquad
(q)_i=q(q-1)\cdots(q-i+1).
\tag{13}
$
没有移走任何 regular 系数。

对每个实际整数 $m$，唯一写成
$
m=\rho+p\ell_m,\qquad 0\le\rho<p,\quad\ell_m\in\mathbf Z.
$
展开 $(ma)^{q-i}=(a\rho+pa\ell_m)^{q-i}$。令 $j=i+t$，恒等式
$
(q)_i\binom{q-i}{t}=\frac{(q)_j}{t!}
$
给
$
\boxed{\;
\mathcal Y_{r,q}(P)
 =
\sum_{\rho=0}^{p-1}\sum_{j=0}^q
 (q)_j(a\rho)^{q-j}\,
 C_{\rho,j,r}(P),
\;}
\tag{14}
$
其中完整系数为
$
\boxed{\;
C_{\rho,j,r}(P)
 =
p^j
\sum_{\substack{m\in\mathcal I_D\\m\equiv\rho\ (p)}}
\ \sum_{i=0}^{j}
 \frac{a^{j-i}\ell_m^{\,j-i}}{(j-i)!}
 A_{m,r+si}(P).
\;}
\tag{15}
$
空节点取零；$\rho=0$、$q=j$ 按 $0^0=1$；$j>q$ 的项按零。所有整数 charge 可碰撞或被 $p$ 整除，无例外除法。

(15) 只是同一原来源的线性泛函。它没有将 $\ell_m$、$A_{m,r+si}$ 或 Euler 槽变成可自由选的坐标。尤其任何实际
$
P+pR+p^2T+\cdots
$
在 (12)–(15) 中始终使用这同一个完整来源向量，没有逐行另选修正。

## 4. 完整无限尾与阶 $pJ_H$ 的真实递推

每个 (15) 项满足
$
\begin{aligned}
v_p\!\left(
 \frac{p^j a^{j-i}\ell_m^{j-i}}{(j-i)!}
 A_{m,r+si}\right)
&\ge
 j-v_p((j-i)!)-\lfloor b_*(r+si)\rfloor\\
&\ge j-\frac{j-i}{p-1}-\vartheta(i+1)\\
&=j\left(1-\frac1{p-1}\right)-\frac{i}{p}-\vartheta\\
&\ge \eta j-\vartheta .
\end{aligned}
$
因此
$
\boxed{\;
v_p(C_{\rho,j,r}(P))
 \ge \lceil\eta j-\vartheta\rceil .
\;}
\tag{16}
$
这界从 $j=0$ 起非负，故所有 $\mathcal Y_{r,q}$ 都整，证明原 $\Phi(P)\in\mathscr B_d$。由于 $\eta>0$，(16) 还同时支付任意精度的完整尾。

给 $H\ge1$，置
$
J_H=\left\lfloor\frac H\eta\right\rfloor.
\tag{17}
$
若 $j\ge J_H$，则 $\eta j-\vartheta>H-1$，故 $C_{\rho,j,r}\in p^H\mathcal O$。于是对全部 $q$ 有
$
\mathcal Y_{r,q}
 \equiv
\sum_{\rho=0}^{p-1}\sum_{0\le j<J_H}
 (q)_j(a\rho)^{q-j}C_{\rho,j,r}
 \pmod{p^H}.
\tag{18}
$
(16) 与 $(q)_j\in\mathbf Z$ 使这个截断对所有 $q$ 一致，未依赖 $q$ 的固定有限上界。

令 $E_q$ 为行指标的前移算子，$(E_qf)(q)=f(q+1)$。直接计算
$
(E_q-\lambda)\big((q)_j\lambda^{q-j}\big)
 =j(q)_{j-1}\lambda^{q-j+1},
$
或直接从 $\partial_\lambda^j\lambda^q$ 得到
$
(E_q-\lambda)^{j+1}
 \big((q)_j\lambda^{q-j}\big)=0.
$
该式也包含 $\lambda=0$ 的有限支撑序列。因此定义真正整的首一多项式
$
\mathcal Q_H(T)
 =\prod_{\rho=0}^{p-1}(T-a\rho)^{J_H}
 =\sum_{\ell=0}^{pJ_H}b_{H,\ell}T^\ell,
\qquad b_{H,pJ_H}=1,
\tag{19}
$
便得同一原矩阵的全部精度行递推
$
\boxed{\;
\sum_{\ell=0}^{pJ_H}b_{H,\ell}
 \mathcal Y_{r,q+\ell}(P)\equiv0\pmod{p^H}
\quad(q\ge0,\ 0\le r<s).
\;}
\tag{20}
$

为免对前移的一次式产生歧义，真正使用的是上述
$(E_q-\lambda)^{j+1}=0$：它可在多项式环中逐次对
$E_q\lambda^q=\lambda\lambda^q$ 微分证明，不需除 $j!$，所以 $J_H$ 可以大于 $p$。

(20) 是原有限来源上的行恒等式。它没有假定所得序列的各节点系数独立，也没有从它反解全部 $C_{\rho,j,r}$。反解成本仍属于实际 Smith 问题。

## 5. 实际连续前缀、全部 Smith 精度及同一代表

由 (20) 的首一性，若
$
[w^n]\Phi(P)=0\qquad(0\le n<spJ_H),
$
则所有 $r$ 的前 $pJ_H$ 个 $\mathcal Y_{r,q}$ 都准确为零；递推随即给全部后行在 $p^H\mathcal O$。所以
$
\boxed{\;
\operatorname{ord}_w\Phi(P)\ge spJ_H
\quad\Longrightarrow\quad
\Phi(P)\in p^H\mathscr B_d
 \subset p^H\mathscr B_e.
\;}
\tag{21}
$
包含关系的准确行成本仍为
$
e(r+sq)-d(r+sq)=\epsilon(r,q)\ge0,
\tag{22}
$
不是把两种目标称作同一格。

令原特征零连续饱和旗标的真实跳跃为 $k_1,\ldots,k_{N_D}$，并在原源格中选适配整基。定义
$
H_p(k)=\max\{H\ge0:spJ_H\le k\},\qquad J_0=0.
\tag{23}
$
每个适配列的所有正规化行均整除 $p^{H_p(k_i)}$；在其首行还保 (22)。因此对原 R418 的同一真实跳跃方阵及全部 Smith 指数总和 $g_{p,D}$，有
$
\boxed{\;
g_{p,D}\ge
\sum_{i=1}^{N_D}
 \bigl(H_p(k_i)+\epsilon(k_i\bmod s,\lfloor k_i/s\rfloor)\bigr).
\;}
\tag{24}
$
证明先对第 $i$ 个同源适配列提出全列共有的 $p^{H_p(k_i)}$。其原首行另有 (22) 的 $\epsilon(k_i)$，而更低原行准确为零，故真正跳跃方阵为三角形，行列式再获得这些对角费用。这里没有把 $\epsilon(k_i)$ 错当该列每一行都共有的因子，也没有把非连续单位子式成本代替真实旗标，或由另一源格的 Smith 因子推回。

若只需要有限精度，(20)–(21) 已逐个给出，无须先构造无限输出的 Smith 标准形。它们对全部 $D,H$ 成立；原 $D<p$、首 $p^2$ 窗及固定三块长度均不是本篇假设。

## 6. 本项真实收益仍是 $O(M_D)$

这段范围是证明的一部分。因 $J_H\ge H$，
$
0\le H_p(k)\le\frac{k}{sp}
 =\frac{6k}{p(p+1)}.
$
故
$
\sum_{p\ {\rm good\ inert}}H_p(k)\log p=O(k),
\tag{25}
$
使用绝对收敛的 $\sum_p\log p/p^2$，常数不依赖 $D,k$。

数字余项同样只贡献低阶量。因为
$
\epsilon(r,q)
 \le e(k)-q
 \le\frac{6k}{p^2-1}+1,
$
且 $p>6k+1$ 时 $\epsilon=0$，Chebyshev 的
$\sum_{p\le x}\log p=O(x)$ 给
$
\sum_{p\ {\rm good\ inert}}\epsilon(k\bmod s,\lfloor k/s\rfloor)\log p=O(k).
\tag{26}
$
于是本篇 (24) 中已支付的明确下界，逐素数加权后只有
$
O\!\left(\sum_i k_i\right)=O(M_D).
\tag{27}
$
这不是给真实 $g_{p,D}$ 一个上界。真实 Smith 收益仍可能更大；(27) 只准确界定本篇递推和数字余项本身所能支付的量。

原目标需要
$
\sum_p g_{p,D}\log p>3M_D\log D
$
的严格主项。本篇未达到它，也未把“不限 Gaussian 块数”本身算作主项改善。若要由原 canonical 坏条件继续，必须在同一递推商中真正减少节点/提高整个同源系数格的整除，而非重复计入 (25)。

## 7. 原坏 canonical 条件在此读者中的准确位置

对原 $A_m=S,T$ 之一，保持实际 $\gamma_m=mpc_\sigma=ma\in\mathcal O^\times$。R618(29) 的完整 Newton 截断在本篇行中准确是
$
\boxed{\;
L_{m,H}
 =
\sum_{k=1}^{H}
 (-1)^{k-1}\binom Hk
 \frac{\mathcal Y^{(m)}_{0,k}}{k\,\gamma_m^k}.
\;}
\tag{28}
$
这里 $k$ 的全部 $p$ 因子仍保留；未将 $k$ 一概当单位。原 $j_m=0$ 只直接迫
$
v_p(L_{m,H})
 \ge \left\lceil(H+1)\eta+6\tau_2\right\rceil+v_p(H!)
\quad\text{对每个 }H,
\tag{29}
$
并与 R614/R616 的更强有限窗取已付较大界。

因此 (28) 是同一个完整 scalar matrix 上的真正必要行。它既没有令每个 $\mathcal Y_{0,k}$ 为零，也没有令 (15) 中每个节点 jet 为零。R710 已付的全深中央核还说明，单凭这种完整解析零不能把非恒定正规余项全部抹去。

下一步所需的是：使用原固定来源与完整条件 (28)–(29)，在真实同源前缀/同一提升中证明一个额外 Smith 主项。现有所有 regular、factorial、charge 碰撞及高 Gaussian 费用已经由 (14)–(20) 给出；没有以自由 Euler thick ideal 代替这个问题。


## 8. $Q_1(E_q)/p$ 的实际首提升与原基线行

本节继续同一 $\Phi$，不另造来源。置
$
Q_0(X)=\prod_{\rho=0}^{p-1}(X-\rho),\qquad
Q_1(T)=a^pQ_0(T/a)=\prod_{\rho=0}^{p-1}(T-a\rho).
$
因
$
Q_1(T)\equiv T^p-a^{p-1}T\pmod p,
$
有唯一真实整多项式
$
R_p(T)=\frac{Q_1(T)-T^p+a^{p-1}T}{p}\in\mathcal O[T].
$
保其全部系数，定义
$
\boxed{\;
\mathfrak D_{r,q}(P)
 =\frac{Q_1(E_q)\mathcal Y_{r,q}(P)}p
 =\frac{\mathcal Y_{r,q+p}-a^{p-1}\mathcal Y_{r,q+1}}p
   +R_p(E_q)\mathcal Y_{r,q}.
\;}
\tag{30}
$
由 (20) 的 $H=1$，它是原来源上的整线性泛函。因而
$
\mathfrak D_{r,q}(P+pR)\equiv\mathfrak D_{r,q}(P)\pmod p
$
对任意同一原格中的 $R$ 成立。这里的除 $p$ 是由整个原行组合的整性支付；不能只保 (30) 的首个差商而丢 $R_p(E_q)$。

### 8.1. 所有 regular 项与 charge 的准确返回

因为 $p>101$，(16) 对 $j\ge2$ 给 $C_{\rho,j,r}\in p^2\mathcal O$。同时
$
C_{\rho,0,r}=\sum_{m\equiv\rho}A_{m,r},
$
$
C_{\rho,1,r}
 =p B_{\rho,r},\qquad
B_{\rho,r}:=
 \sum_{m\equiv\rho}\left(A_{m,r+s}+a\ell_mA_{m,r}\right).
$
所读 $r+s<2s<L$ 的原 regular 系数均整。

$Q_1(E_q)$ 准确杀掉 $j=0$ 节点，并把
$q(a\rho)^{q-1}$ 送成 $Q_1'(a\rho)(a\rho)^q$。由
$Q_1'(a\rho)\equiv-a^{p-1}\pmod p$，得到
$
\boxed{\;
\mathfrak D_{r,q}(P)
 \equiv
 -a^{p-1}\sum_{\rho=0}^{p-1}(a\rho)^q
 \sum_{m\equiv\rho}
   \left(A_{m,r+s}(P)+a\ell_mA_{m,r}(P)\right)
 \pmod p.
\;}
\tag{31}
$
它保原 $A_{m,r+s}$，不是只有一个 charge Fermat 商。

还可完全写成原来源算子。令 $\mathcal C$ 在 charge $m$ 列上作用为乘 $m$，并定义
$
\mathcal F_p=\frac{Q_0(\mathcal C)}p
 =(p-1)!\binom{\mathcal C}{p}.
$
$\mathcal F_p$ 保原整格，因为 $Q_0(m)/p\in\mathbf Z$ 对每个整数 $m$ 成立。对 $E_D$，
$\mathcal C=34S\partial_S+72T\partial_T$；
对 $G_0\mathcal W_D$，它是 $\mathcal E+40$。全部原角和次数帽不变。

设 $\Phi_{\rm reg}(P)=\sum_mA_m(P;w)$。由
$Q_0(\rho+p\ell_m)/p\equiv-\ell_m\pmod p$，(31) 等价于
$
\boxed{\;
\mathfrak D_{r,q}(P)\equiv
 a^{p+q}[w^r]\Phi_{\rm reg}(\mathcal C^q\mathcal F_pP)
 -a^{p+q-1}[w^{r+s}]
             \Phi_{\rm reg}(\mathcal C^qP)
 \pmod p.
\;}
\tag{32}
$
这是一条真正的“原整 source 算子减下一 regular 带”的关系。后一项没有被重新命名为同 source 的低行；也没有宣称 $\mathcal F_pP$ 自动具有 $P$ 的真前缀。

[R530](R530-divided-graded-connection-full-integral-gauge-and-mixed-second-precision.md) 已使用整数特征值的 Fermat 多项式机制；其原 $\nabla$ 的特征值是角阶 $j$，不能认作本篇特征值为 charge $m$ 的 $\mathcal C$。纯多项式 $[Q_0(X)-X^p+X]/p$ 在 $\mathbf Z[X]$ 中，这解释了本篇整数值算子与该旧机制的联系；并未把 R530 的来源连接或目标共轭搬到这里。本篇 (30)–(34) 的实际全深 scalar 回读、原基线精度与同一个提升 $R$ 均由上述完整证明独立支付，未新增免费的 Euler 传播。

### 8.2. 原基线到 p² 的精度足够范围

(30) 先以 $\mathcal Y$ 行书写，现逐项付回原 (5) 基线，避免误将 $\mathscr B_e$ 换成较强的 $\mathscr B_d$。

保持 $0\le r<s$，取
$
\begin{cases}
0\le q\le p-3,&r=0,\\
0\le q\le p-2-6r,&1\le r<s.
\end{cases}
\tag{33}
$
若右端为负，则该范围为空。在 $q,q+1,\ldots,q+p$ 中：

- $q+1$ 与 $q+p$ 的 $\epsilon(r,\cdot)=0$；
- 其余指标的 $\epsilon(r,\cdot)\le1$；
- $Q_1$ 在幂次 $2,\ldots,p-1$ 的系数都被 $p$ 整除，其常数项为零。

前两点直接由 (8) 核：小于 $p$ 的指标数字和是自身，介于 $p$ 和 $2p-1$ 的指标数字和是该指标减 $p$ 再加一。特别两个单位系数所在的端点，正好由 (33) 保在 $\epsilon=0$ 的范围。

又
$
\mathcal Y_{r,q+\ell}
 =u_{q+\ell}^{-1}p^{-\epsilon(r,q+\ell)}
  \left(p^{e(r+s(q+\ell))}
             [w^{r+s(q+\ell)}]\Phi\right).
$
因此 (30) 每项相对原基线正规化行至多损失一个 $p$：中间行的额外 $\epsilon=1$ 由 $Q_1$ 系数的一个 $p$ 支付。故
$
\boxed{\;
p^{e(r+s(q+\ell))}
 [w^{r+s(q+\ell)}]\Phi(P+pR)\in p^2\mathcal O
 \ (0\le\ell\le p)
\quad\Longrightarrow\quad
\mathfrak D_{r,q}(P)=0\pmod p .
\;}
\tag{34}
$
这是原基线中同一 $P+pR$ 的必要首提升条件。没有逐项重选 $R$，没有把较强目标的提升当作原目标已付。

当然，若同一来源有真正连续前缀
$
\operatorname{ord}_w\Phi(P)\ge r+s(q+p)+1,
$
则 (30) 的全部原行已经准确为零，(31)–(32) 给同一个必要关系，无须 (33) 的模 $p^2$ 限制。两种使用范围须分开。

### 8.3. 强目标中的完整同源首 Bockstein

为了明确尚须求解的真实像条件，本小节仅对 $\mathscr B_d$ 陈述一个等价式；不把它外推到 (5) 或旧三块。

若原 $P$ 满足 $\Phi(P)\in p\mathscr B_d$，则由 $j=0$ 的单位 Vandermonde，
$
A_{\rho,r}^{(0)}(P):=\sum_{m\equiv\rho}A_{m,r}(P)\in p\mathcal O
\quad(\rho\in\mathbf F_p,\ 0\le r<s).
$
对原格中同一个 $R$，(18) 的 $H=2$ 给
$
\frac{\mathcal Y_{r,q}(P+pR)}p
 \equiv
 \sum_\rho(a\rho)^q
   \left(\frac{A_{\rho,r}^{(0)}(P)}p+
                    A_{\rho,r}^{(0)}(R)\right)
 +\sum_\rho q(a\rho)^{q-1}B_{\rho,r}(P)
 \pmod p.
$
这里 $q<j$ 的项仍按零处理，故 $q=0,\rho=0$ 没有负幂除法。在 $q=0,\ldots,2p-1$ 上，两个 jet 的合流 Vandermonde 是整可逆矩阵：它是次数 $<2p$ 多项式在 $p$ 个互异点上的值与一阶导数评价，核为
$\prod_\rho(T-a\rho)^2$，不需除 $p!$。从而
$
\boxed{\;
\Phi(P+pR)\in p^2\mathscr B_d
\iff
\begin{cases}
B_{\rho,r}(P)=0\pmod p,\\
A_{\rho,r}^{(0)}(R)=
          -A_{\rho,r}^{(0)}(P)/p\pmod p
\end{cases}
\quad\text{对全部 }\rho,r .
\;}
\tag{35}
$
第一行是显示的同源首障碍；第二行仍必须由**同一个原 $R$** 实际实现。它是原 source-to-image 条件，不能以任意 $p$ 节点数组代替。式 (35) 也没有给旧短 $M$ 增加未读取的高行。

### 8.4. 原 canonical 坏条件只支付其实际中央槽

对 $S,T$ 单列，当前 $p>101$ 使 $m=34,72$ 都属于选定代表 $0,\ldots,p-1$，故 $\ell_m=0$、$\mathcal F_pS=\mathcal F_pT=0$。原质量零还给 $A_{m,0}=0$。

R614 的整窗、R618 全尾与 $j_m=0$ 于是确实迫
$A_{m,s}\in p\mathcal O$：Newton 第一个系数是
$pA_{m,s}/\gamma_m$，其余完整项皆在 $p^2\mathcal O$。所以 (31) 中
$
\boxed{\;
j_S=j_T=0
\quad\Longrightarrow\quad
\mathfrak D_{0,q}(S)=\mathfrak D_{0,q}(T)=0\pmod p
\quad(q\ge0).
\;}
\tag{36}
$
这是真正全部原高行的一个中央首层后果。但它既未给 $r>0$ 的下一 regular 带赋零，也未给 $\mathfrak D_{0,q}(S^\mu T^\nu)$ 赋零。

对 $G_0\mathcal W_D$，$r<13$ 的 $A_{m,r}=0$ 使 (31) 退为下一 regular 带；这些低十三行必须与 R631/R633 已付首 Bockstein 边界一并核对，不能重复计数。新的较长原行仍按 (33)–(34) 逐项付精度。

因此，(30)–(35) 给了全深递推在同一实际首提升中的具体消费，而非一个自由 Euler thick ideal。若要获得超过 §6 的全局主项，仍须将原坏条件与这些真实 $B_{\rho,r}$ 及同 $R$ 像条件联立。


## 依赖与既有结果范围

- [R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)：原 $S,T$、同一全部次数源、真实饱和旗标及 $3M_D\log D$ 总预算。
- [R600](R600-original-central-residue-blocks-and-true-prefix-vandermonde.md)：原首 $p^2$ 窗的完整余数行与中央首 Bockstein；本篇 (10) 延至所有物理深度。
- [R612](R612-original-full-source-weighted-kernel-and-fixed-nodal-exit.md)：原 $G_0\mathcal W_D$、完整首窗带权核、实际行缩放与旧三块商的区别。
- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：同一个原 regular 余项的全部系数界、完整 Newton 尾及所有高 Gaussian 费用。
- [R646](R646-original-full-target-ramified-confluent-block-and-smith-bound.md)、[R657](R657-original-long-ordered-prefix-and-quadratic-contact-bound.md)：原全部列的 regular 单位与既有长前缀；本篇不重复其有限次数单位子式。
- [R710](R710-original-all-order-central-kernel-and-exact-boundary-remainder.md)：原 complete central kernel、全部 carry 及不能免费推出 Euler 厚理想的准确余项。
- [固定深度预算说明](../notes/2026-11-14-deep-fixed-depth-tame-average-budget.md)：固定或增长块数与真正全局 Smith 收益的区别。

全篇为原全参数证明，无新增数学执行或素数扫描。
