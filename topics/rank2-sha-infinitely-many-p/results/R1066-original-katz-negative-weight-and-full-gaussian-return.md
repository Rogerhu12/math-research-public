# R1066 — 原 Katz 新来源的负权连接与完整 Gaussian 返回

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

本篇继续
[R1065](R1065-original-hall-katz-unit-measures-and-canonical-return.md)
(W1)–(W26)的同一原 $p^2$ 新字。先支付全部连接系数的统一
Tate 尾，再用原正整数导数的准确归一构造负二值和斜率。
每个新字由此得到一份真正有界的 Galois–Katz 负权测试，
并准确返回 R1062 的完整 Miller 函数
$\mathcal F_{N,Q}(-2)/(NZ_Q)^2$。
本部分没有将各新字非零传给全 Hall、全 source 或原 canonical
中央。后半部分(Z1)–(Z22)在相同对象上支付完整 Gaussian 返回，
保原 Maass、Haar、全部 $h$ 及 $\Lambda,\Lambda'$。

## 1. 原对象与完成系数域

保持 $p>211$、$p\equiv5\pmod6$ 及原全部固定坏位排除，记
$$
 q=p^2,\qquad \Delta=q-1,\qquad d=p+1,\qquad
 \tau=\frac p\Delta,\qquad \eta=1-\frac1{p-1},\qquad
 L=\mathbf Q_{p^2},\quad\mathcal O=\mathcal O_L .
 \tag{N1}
$$
仍用 R663 的严格 LT 坐标
$[p](v)=pv-v^q$、不变微分 $dz$ 和原
$z(v)=v+v^q/(p^q-p)+O(v^{2q-1})$。
原 $E_0$、$T_{\rm g}$、负102的两条三挠字、正34的 canonical
$S$ 均不改变。

记 $\mathbb T=T_pG^\vee$、$\mathbb T^\times=\mathbb T\setminus p\mathbb T$，
$$
 \mathscr C^\times
   =C^0_{\rm Gal}(\mathbb T^\times,\mathcal O_{\mathbf C_p}),
 \qquad X=c_1|_{\mathbb T^\times}.
$$
这里的函数可在 $p\mathbb T$ 上延为0；这与 R1065 的单位支撑
约定一致。原 Cartier-dual period 的准确估值给
$$
 v_p(X(\xi))=\tau\quad(\xi\in\mathbb T^\times),\qquad
 X^{-r}\in p^{-\lceil r\tau\rceil}\mathscr C^\times\quad(r\ge0).
 \tag{N2}
$$
参见 [R1064](R1064-original-book-cartier-dual-period-and-actual-lt-measure-bridge.md)
的同一不变微分和 Cartier-dual period；不把 book period 和该
period 仅凭估值相同相认。

对包含实际除点、Miller 中心和所有代数源系数的有限 $F/L$，
测试放在
$$
 \mathscr B_F^\times
   =(\mathcal O_F\widehat\otimes_{\mathcal O}\mathscr C^\times)[1/p].
$$
原 $\boldsymbol\mu_{N,T}$ 仍是
$\operatorname{Hom}_{\mathcal O}(\mathscr C,\mathcal O_F)$ 的整对象，
并以完成的标量扩张作用于这个代数。
所有估计都可写成明确的 $p^k$ 格包含；
不把 $\mathscr B_F^\times$ 当成任意 $\mathbf C_p$ 测度的测试空间。

## 2. 严格 c_q 恒等式锁住负幂归一

原 universal character 是
$\mathbf t_\xi(v)=\exp(c_1(\xi)z(v))$。
由于 $z(v)$ 在 $1<r<q$ 没有项，准确有
$$
 c_q=\frac{c_1}{p^q-p}+\frac{c_1^q}{q!}.
 \tag{N3}
$$
这是原 $q$ 次系数的完整式，而不是渐近式。
$X=c_1$ 在 units 不为零。令
$$
 U_q=\frac{q!}{p^{p+1}}\in\mathbf Z_p^\times,\qquad
 u=\frac{X^\Delta}{p^p}.
$$
将(N3)重排，得到
$$
 \boxed{
 u=\frac{U_q}{1-p^\Delta}
       +pU_q\,\frac{c_q}{X},\qquad
 U_q\equiv1\pmod p,\qquad
 v_p(u(\xi)-1)\ge1-\tau
       \quad(\xi\in\mathbb T^\times).
 }
 \tag{N4}
$$
其中 $v_p(q!)=p+1$。为核其绝对单位号，把 $1,\ldots,p^2$ 中
非 $p$ 倍数分成 $p$ 组；其乘积模 $p$ 为 $(-1)^p$。
所有 $p$ 倍数除去 $p^{p+1}$ 后贡献 $(p-1)!\equiv-1$。
故 $U_q\equiv(-1)^{p+1}=1$。
再用 $c_q$ 整和(N2)，即得最后的严格界。

因此 $u,u^{-1}\in\mathscr C^\times$，且对每个 $k\ge0$
$$
 (u-1)^k\in
       p^{\lfloor k(1-\tau)\rfloor}\mathscr C^\times.
$$
这个结论同时固定原 dual period 的 residue：
若 $\varpi=c_1(\xi_0)$ 对任一 primitive $\xi_0$，
则 $\varpi^\Delta/p^p$ 的 Teichmüller 部分确为1。
这里不遗留一个待选的 $\lambda\in\mu_\Delta$。

因为 $1-\tau>1/(p-1)$，完整二项式级数
$$
 u^t=\sum_{k\ge0}\binom tk(u-1)^k
       \in\mathscr C^\times\langle t\rangle,\qquad
 \ell=\Delta^{-1}\log u
       \in\mathscr C^\times
 \tag{N5}
$$
在闭单位权盘收敛。其第 $k$ 项的 Gauss 格至少为
$p^{\lfloor k(1-\tau)\rfloor-v_p(k!)}$，趋于无穷；
同一界允许任意固定阶权导数。
本篇用 $\log p=0$ 的原分支。于是 $\ell$ 就是
该分支下的 $\log X$；这个等式由(N4)定义，不需先对
非单位 $X$ 自由作权幂。

特别原合法的负幂逼近为
$$
 \boxed{
 p^{-p p^h}X^{\,\Delta p^h-2}
     =X^{-2}u^{p^h}\longrightarrow X^{-2}.
 }
 \tag{N6}
$$
全部项在 $p^{-1}\mathscr C^\times$ 中，且误差的点值估值至少
$h+1-3\tau$，因而误差属于 $p^h\mathscr C^\times$。
这里的 $p^{-p p^h}$ 是确切归一；不将它删掉。
为保持更多原有限角色，可把 $p^h$ 换成共同的
$e_0p^h$（$e_0$ 为固定正整数），相应归一准确改为
$p^{-p e_0p^h}$。这仍是同一序列机制，并非新增算术坏行。

## 3. 原完整连接系数的统一界

沿 R1065(W20)，在同一个原 Lie 变量中定义
$$
 \begin{aligned}
 B_N(z)
   &:=a_N^{-1}(v(z))
     =\left(\frac{\sigma(z)}{h(v(z))}\right)^N
      =\left(\frac z{v(z)}\right)^N E_{\rm c}(z)^N\\
   &=\sum_{r\ge0}b_{N,r}z^r,\qquad b_{N,0}=1,
       \qquad N=34,102.
 \end{aligned}
 \tag{N7}
$$
这是**全部** $T_{\rm g}$ 和 $E_{\rm c}$，不是只保
$\exp(Nc_\sigma z^{p+1})$。

下面给全 $r$ 的界。取 $S=p^{-\tau}<R_E=p^{-1/\Delta}$。
R639(12)、R663 的严格整坐标及整逆表明
$v(z)/z$ 与其逆在闭 $S$ 盘为范数一 Tate 单位；
$T_{\rm g}(w(v(z)))$ 也如此。
R588(3)、(4)、(8)给
$\sigma/z=H_\sigma\exp(c_\sigma z^d)$ 的所有加权系数范数至多1。
确切地，
$$
 v_p(c_\sigma^k/k!)+kd\tau
      =\frac{s_p(k)}{p-1}\ge0 .
$$
R588 的原 $b=17$ 模型与当前 $b=1$ 的运输为同一已付
$p$ 单位缩放，故这个界在原 $E_0$ 规范下不变。
不声称 $\sigma/z$ 在闭 $S$ 边界为 Tate；
这里仅取其完整加权系数范数。

乘上上述两个实际 Tate 单位，由(N7)得
$$
 \boxed{
 b_{N,r}\in L,\qquad
 v_p(b_{N,r})\ge-r\tau,\qquad
 b_{N,r}=0\ \text{除非}\ d\mid r .
 }
 \tag{N8}
$$
最后的支撑不是猜测：R639(1)的原 $E_{\rm c}$ 只含 $z^d$；
R663(4)的逆式使 $v(z)/z$ 只含 $z^\Delta$，而 $d\mid\Delta$。
因 $L/\mathbf Q_p$ 非分歧，估值还可准确写为
$v_p(b_{N,r})\ge-\lfloor r\tau\rfloor$。
全部高阶系数和所有坏带都包含在(N8)中。

定义实际连接的转置族
$$
 \boxed{
 \mathcal A_N(j;X)
   =\sum_{r\ge0}(j)_r\,b_{N,r}(p/X)^r,
 \qquad
 (j)_r=j(j-1)\cdots(j-r+1).
 }
 \tag{N9}
$$
对 $j=m\ge0$，这是截止于 $r=m$ 的有限和；
它恰是 R1065(W22)的有限三角式重新收集，不额外除 $r!$。

现在支付整个权盘。由(N2)、(N8)，第 $r$ 项的系数格至少为
$$
 p^{e_r},\qquad
 e_r=r-\lfloor r\tau\rfloor-\lceil r\tau\rceil.
$$
$(j)_r$ 的全部 ordinary monomial 系数整。
$e_r\to+\infty$，且对全部非零支撑 $r\ge d$，
$$
 e_r\ge p-2 .
$$
例如最早 $r=d$ 时，$\tau d=p/(p-1)$，
准确给 $e_d=d-1-2=p-2$；
一般由 $e_r\ge(1-2\tau)r-1>p-3$ 得出。
所以
$$
 \boxed{
 \mathcal A_N\in1+p^{p-2}\mathscr C^\times\langle j\rangle,\quad
 \mathcal A_N^{-1}\in1+p^{p-2}\mathscr C^\times\langle j\rangle,
 \quad
 \partial_j^k(\mathcal A_N-1)
       \in p^{p-2}\mathscr C^\times\langle j\rangle
       \ (k\ge0).
 }
 \tag{N10}
$$
对所有整数平移 $j\mapsto j-s$ 也有同一界。
这是后继双槽全 Maass 和所需的统一输入，不仅是各固定
整数 $m$ 的收敛。

## 4. 同一新字的全部正整数导数

令 $T\in E[p^2]$ 是 R1065 的实际非旧 Weyl 字，
$Q=pT\ne O$，$\boldsymbol\mu_{N,T}$ 为(W13)那一份整 Katz 测度。
保持 R1062(G1)–(G8)的准确记号
$$
 B_Q=b_{N,T}R_N(Q),\qquad A_Q=NZ_Q,\qquad
 \mathcal F_Q(j)=\mathcal F_{N,Q}(j)
       \in1+\mathfrak m_F^{\ge\eta}\mathcal O_F\langle j\rangle .
$$
$B_Q$ 保整个原中心；不重新取根。

R1065(W22)给所有 $m\ge0$ 的准确等式
$$
 \boxed{
 \begin{aligned}
 \boldsymbol\mu_{N,T}
       \bigl(X^m\mathcal A_N(m;X)\bigr)
   &=D_{z'}^mF_{N,T}^\sigma(0)\\
   &=p^m B_QA_Q^m\mathcal F_Q(m).
 \end{aligned}
 }
 \tag{N11}
$$
$z'$ 是覆盖变量，物理参数为 $z=pz'$。
左侧的 $r!$ 已经通过
$\binom mr r!=(m)_r$ 完整计入(N9)，没有漏掉阶乘。
Taylor 系数仍须在整个式子外除 $m!$；
物理导数仍须除 $p^m$。

还需锁住点端归一的 Teichmüller 部分。置
$$
 v_Q^*= \frac{(pA_Q)^\Delta}{p^p}.
$$
由 R1061(C13)与原严格坐标的整首项，
$$
 \frac{pA_Q}{v_Q^p}
      \equiv N d\kappa_\sigma
          \in\mathbf F_q^\times\pmod{\mathfrak m_F},
 \qquad v_Q^\Delta=p.
$$
于是
$$
 \boxed{
 v_Q^*\in1+\mathfrak m_F,\qquad
 \operatorname{Teich}(v_Q^*)=1 .
 }
 \tag{N12}
$$
原 $\kappa_\sigma=pc_\sigma$、$N$ 和 $d$ 都是指定单位，
不是可替换的归一常数。
(N12)保实际 point $Q$，不把 $Z_Q$ 换成首估值模型。

## 5. 负二值的合法极限与全 germ 恒等式

对当前有限组真实字，取一个共同 $e\ge2$，
使所有 $(v_Q^*)^{p^e}$ 都属于 $1+p^2\mathcal O_F$；
必要时增大 $e$，同时保持原全部有限角色的 $p$ 部分。
取固定 prime-to-$p$ 的 $e_1$，使
$$
 D=\Delta e_1p^e
$$
还保持 R1059/R1062 的全部原 finite/Teich 分量。
这是共同选择，不对不同 $Q$ 偷换不相容的权支。

令 $j=-2+Dt$。由(N5)、(N10)，下面确为同一完成系数域上的
Tate 测试：
$$
 \mathcal J_N(t;X)
  =(p/X)^2\,u^{\,e_1p^et}\,
                     \mathcal A_N(-2+Dt;X)
       \in p\,\mathscr C^\times\langle t\rangle .
 \tag{N13}
$$
当 $t=n\ge1$ 为整数，设 $m=-2+Dn\ge0$。逐项代入(N11)，
没有任何未审的插值公式，准确得到
$$
 \begin{aligned}
 \boldsymbol\mu_{N,T}(\mathcal J_N(n;X))
 &=p^2p^{-p e_1p^en}\,
          D_{z'}^mF_{N,T}^{\sigma}(0)\\
 &=\frac{B_Q}{A_Q^2}
        (v_Q^*)^{e_1p^en}\mathcal F_Q(-2+Dn).
 \end{aligned}
$$
两边均在闭 $t$ 单位盘 Tate：
左边由真实整测度和(N13)，右边由(N12)后的共同 $e$
及 R1062(G6)。整数正点在 $\mathbf Z_p$ 中稠密，因此得到
完整 germ 等式
$$
 \boxed{
 \boldsymbol\mu_{N,T}(\mathcal J_N(t;X))
   =\frac{B_Q}{A_Q^2}
       (v_Q^*)^{e_1p^et}\mathcal F_Q(-2+Dt).
 }
 \tag{N14}
$$
右边幂是同一个原整数支的指数延拓，
其基点值为1；所有可能的 $p$ 幂根单位已由共同 $e$ 支付。

在 $t=0$，得到真正的同源负二读者
$$
 \boxed{
 \boldsymbol\mu_{N,T}
       \bigl((p/X)^2\mathcal A_N(-2;X)\bigr)
   =\frac{b_{N,T}R_N(Q)}{(NZ_Q)^2}
                    \mathcal F_{N,Q}(-2).
 }
 \tag{N15}
$$
左侧是有界的完成系数测试，右侧是原全部 Miller 修正，
不是只留 $(NZ_Q)^{-2}$。
它在 R1065(W16)中逐个原 Hall lift 代入，正好返回同一个
完整负 Hall。原 $d$、两条独立 Hall 及 $p^{-2}$ Haar 不改变。

特别，$e_1=1,e=0$ 的单字负幂底式是(N6)，对应
$m_h=\Delta p^h-2$ 与归一 $p^{-p p^h}$；
回物理负二还须乘 $p^2$，如(N13)–(N15)。
全合法权支只将 $p^h$ 换成共同的 $e_1p^{e+h}$。
这里从未插值非单位 $p^m$ 或 $A_Q^m$；
正整数比较列准确是
$p^2p^{-p e_1p^en}D_{z'}^mF^\sigma(0)$。
它不是此前已排除连续性的 literal usual toric 正权列。

## 6. 完整斜率：连接导数、point 尺度和原外权

对(N14)求 $t$ 导数，再除**真实** $D$。
由 $D=\Delta e_1p^e$，
$e_1p^e/D=1/\Delta$，全部 $p^e$ 费用在同一式中相消。
于是同一个原权参数 $j$ 的斜率测试为
$$
 \mathcal J_{N,1}(X)
  =(p/X)^2\left[
       \ell\,\mathcal A_N(-2;X)
        +(\partial_j\mathcal A_N)(-2;X)\right]
       \in p\mathscr C^\times ,
 \qquad \ell=\Delta^{-1}\log u .
 \tag{N16}
$$
其准确返回是
$$
 \boxed{
 \boldsymbol\mu_{N,T}(\mathcal J_{N,1})
   =\frac{B_Q}{A_Q^2}\left[
       \mathcal F'_Q(-2)
       +\frac{\log v_Q^*}{\Delta}\mathcal F_Q(-2)
                    \right]
   =\frac{B_Q}{A_Q^2}
       \left[\mathcal F'_Q(-2)
                     +\log A_Q\,\mathcal F_Q(-2)\right].
 }
 \tag{N17}
$$
最后等号严格使用 $\log p=0$；
$\log A_Q$ 是实际有限域内的原 point 尺度，不设为0，
也不假其估值非负。
若只读 R1062 的 normalized $\mathcal F'_Q$，
须从(N16)中相应减去
$(\log A_Q)(p/X)^2\mathcal A_N(-2;X)$。
两种读者不同，不能把这个常数项略去。

(N16)保全 $\partial_j\mathcal A_N$，包括所有落阶项。
(N10)使所有这些项一致收敛，故求导和测度求值可交换。
在真正双槽中，还必须保正侧 $j+2$ 的权导数、原
$\rho,L_\pm,\Omega$ 先合非单位幂后形成的共同单位底数，
以及原外权
$\Lambda_i'(-2)\mathcal R_i(-2)+
 \Lambda_i(-2)\mathcal R_i'(-2)$。
(N17)只支付这条实际新字的连接部分，不擅自把它命名为
canonical $J'_S$。

## 7. 一个严格非零约束及其准确范围

由(N10)，整个连接与裸 inverse-Lie 测试的差极深：
$$
 (p/X)^2\bigl(\mathcal A_N(-2;X)-1\bigr)
        \in p^{p-1}\mathscr C^\times .
$$
因此对原实际新字，
$$
 \boxed{
 p^2\,\boldsymbol\mu_{N,T}(X^{-2})
  =\frac{B_Q}{A_Q^2}\mathcal F_Q(-2)
                       \pmod{p^{p-1}\mathcal O_F}.
 }
 \tag{N18}
$$
这是已经支付全部连接后得到的同余，绝不是一开始把
$\mathcal A_N$ 设为1。

若原源首项为 $z^a$、首系数为单位，R1062(G3)、(G6)和
原 Miller 中心给
$$
 v_p(B_Q)=a/\Delta,\qquad
 v_p(A_Q)=-1+\tau,\qquad
 v_p(\mathcal F_Q(-2))=0.
$$
对本题 $(N,a)=(102,4),(34,6)$，
$$
 \boxed{
 v_p\!\left(
 \boldsymbol\mu_{N,T}
       ((p/X)^2\mathcal A_N(-2;X))\right)
       =2+\frac{a-2p}{\Delta},\qquad
 v_p\boldsymbol\mu_{N,T}(X^{-2})
       =\frac{a-2p}{\Delta}.
 }
 \tag{N19}
$$
第一值严格在1和2之间，而 $p-1>2$，所以(N18)确实给第二个
准确估值，并证明每份实际新字的这个 inverse-Lie 矩非零。
其来源和中心就是(W13)的那些，不是另造一份单位测度。

这个结论只对个别真实新字及其已付线性组合逐项使用。
完整 tame-zero Hall 仍会作其实际有限角平均，原三挠、
finite/source、Artin/Cor 和冻结外权也都仍在。
它们可以消掉某些首层；(N19)没有给它们添加非零结论。
原正 Hall 的严格低矩门仍是 R1065(K29)，不能用这里的
inverse 矩或高阶 $c_{6q},c_{4q}$ 单位来替代。

## 8. 与实际全来源及后继 Gaussian 的接合

上述 $\boldsymbol\mu_{N,T}$ 先属于尚未作无穷圆周投影的
实际有限 theta 字。对每个已经完成原 graded 代数化的字，
先按 R1065(W4)、(W22)、(W26)运输其整框架、完整连接、
Cartier coset 及全部中心，再用(N14)–(N17)。
原 $E_{17}\leftrightarrow E_0$ 模型比较仍按 R1065(K20a)–(K20b)：
$c_0^{(0)}=\vartheta^{-10}c_0$、$L_\pm=\vartheta\ell_\pm$，
端点的 $17^{-2}$ 不得删除。

有限 $h$ 作用在原固定 finite level 上是已经指定的矩阵；
无穷 $h$ 的作用仍是完整 coherent 核的差2角投影。
(N8)–(N10)是同一原 gauge 的全阶界，
不依赖被单独读出的 section 系数。
所以在已经支付的有限来源返回中，它只损原那些固定矩阵和
实际外幅度的范数，可以逐有限槽使用，再按原完整高尾取极限。
这里不定义一个关于实 $h$ 的 $\mathbf C_p$ 积分，也不把
仅有整个槽代数化的被积项擅自拆成可分别嵌入的两个复周期。

后继若要把原 coherent cross Gaussian 和完整 Maass 精确互逆，
必须在上述同一对新字测度上证明其双级数的绝对收敛和逐字
正确参数；不能拿乘法测试
$\exp(612\omega c_1\otimes c_1)$ 的有界性直接代替另一方向的
逆 Lie 读者。本篇(N10)提供所需的
$\mathcal A_-(j-r)\mathcal A_+(j+2-r)$ 全 $r$ 统一有界输入。
原 $p^{-r-s}$ 覆盖费、完整 $p^{-2}$ Haar、所有 old 列、
$\Lambda,\Lambda'$ 和整个 $\mathfrak T_{\rm orig}$ 均继续保留。
本篇没有恢复旧 usual/flat cross，也没有声称已经证明无穷多个
$p$ 的 canonical 首单位。

## 依赖与证明方式

- R663(4)、R1065(K2)、(K9)：原严格 LT 对数和实际 universal character。
- [R588](R588-actual-wild-kummer-disc-and-nonlinear-primitive-radius.md)
  (3)、(4)、(8)：同一完整 sigma 的系数半径界。
- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)
  (1)、(11)–(13)：全部 $E_{\rm c},T_{\rm g}$ 和实际整坐标。
- [R1061](R1061-original-p-square-antilinear-gluing-and-full-theta-descent.md)
  (C5)、(C13)：完整物理导数、$p$ 幂和原 $Z_Q$ residue。
- [R1062](R1062-original-translated-miller-jets-and-critical-weight-germs.md)
  (G1)–(G14)：真实 $\mathcal F_{N,Q}$、共同合法权支及全部原尺度。
- R1065(W1)–(W26)：原新字的整 Katz 测度、完整 kernel character、
  对偶 coset、Miller 中心和原连接有限转置。

本部分全部为同一原来源的手证；没有新增数学运行或用有限扫描
代替全参数结论。



## 后继：原 coherent Gaussian 在新 Katz 双来源上的完整转置

本部分继续本稿(N1)–(N19)已经证明的实际负权连接；记其转置为
$\mathscr A_N(j;X)$，$N=102,34$。所有 Tate 模、原 theta
中心、$[p]$ 拉回框架和不变微分仍是
[R1065](R1065-original-hall-katz-unit-measures-and-canonical-return.md)
(W1)–(W26)的那些。下文的完整来源返回仍采用
[R1060](R1060-original-full-gaussian-transpose-and-critical-slope.md)
(1)–(16b)的同一个 $\mathcal T_i$，不是追加两个 output-torus
投影。

这里严格区分两个算子。R1065(T8)的整测试乘子
$\exp(b_0c_1^-\otimes c_1^+)$ 在 Fourier 侧对应 mixed-$D_G$
heat。原 coherent Gaussian 却是在 **Lie 变量**上乘
$\exp(\beta ZW)$；它的真实转置是下面含逆矩的完整移位收缩。
二者不因固定常数相同而被认作同一操作。

### 一、同一实际 frame 和完成 tensor

固定 $p>211$ 惰性，置
$q=p^2$、$\Delta=q-1$、$d=p+1$、$\tau=p/\Delta$。
令 $\mathscr C^\times$ 为原
$C^0_{\rm Gal}(\mathbb T,\mathcal O_{\mathbf C_p})$
在单位域上的直因子；单位 cut 是 Galois 不变的 clopen
indicator。以下使用完成的整数 tensor，再作真正的
$\mathbf C_p$ 标量扩张。其范数是这个整数格的 gauge，
不是未经比较的点值上确界。置
$$
 \mathscr B_{\mathbf C_p}
 =\mathbf C_p\widehat\otimes_L
   \Bigl[\bigl(\mathscr C^\times\widehat\otimes_{\mathcal O_L}
                         \mathscr C^\times\bigr)[1/p]\Bigr],
 \qquad
 X=c_1\otimes1,\quad Y=1\otimes c_1 .
 \tag{Z1}
$$
每个实际新字的
$\boldsymbol\mu_{-,T}\widehat\otimes\boldsymbol\mu_{+,MT}$
先在原有限完成系数上定义，再连续延至(Z1)；
这不把任意 $\mathbf C_p$ 值函数空间认成原 Galois-dual
空间。特别，对 $r\ge0$，
$$
 c_1^{-r}1_{\mathbb T^\times}
       \in p^{-\lceil r\tau\rceil}\mathscr C^\times .
 \tag{Z2}
$$
因为 $v_p(c_1(\xi))=\tau$ 在整个 $\mathbb T^\times$ 上恒定，
乘所显示的整数 $p$ 幂才是原整 Galois-equivariant 函数。

采用 R1063(I13)、(I18a)和 R1065(T1)–(T5)的原模型。
在 $E_0$ Lie 变量中
$$
 \begin{gathered}
 c_0^{(0)}=\vartheta^{-10}c_0,\qquad
 L_\pm=\vartheta\ell_\pm,\qquad \vartheta^6=17,\\
 L_-L_+=\frac{\delta\omega t_4^2}{2\cdot51^2},\qquad
 \Omega_A\varpi_0=\frac{Y_A}{t_4},\qquad
 Y_A=\frac{-\omega^2}{\delta},\quad Y_A^2=-\frac{\omega}{3},\\
 C=-\frac{p^2}{\delta},\qquad
 \rho=\frac{17}{2}p^2\kappa_A\Omega_A^2,\qquad
 \beta_0=\frac{-C}{\rho L_-L_+}
             =\frac{612\omega}{\kappa_A}\varpi_0^2 .
 \end{gathered}
 \tag{Z3}
$$
$\kappa_A=1$ 是原参考标记；其它已付单位标记仍保其实际
$\kappa_A$。这里 $\beta_0$ 一般不在固定有限域 $F$，故始终
作为(Z1)的 $\mathbf C_p$ 外标量，不偷偷当成 $F$ 系数。
原 $17^{-2}$ endpoint 费用已经在 $c_0^{(0)},L_\pm$ 中：
$c_0^{(0)}/L_-^2=17^{-2}c_0/\ell_-^2$。
本部分不再收一次 $\delta$ 或 $\vartheta$。

原(N8)–(N11)的完整连接给
$$
 \begin{gathered}
 a_N^{-1}(v(z))=\sum_{r\ge0}b_{N,r}z^r,\qquad
 \mathscr A_N(j;X)
     =\sum_{r\ge0}(j)_r\,b_{N,r}(p/X)^r,\\
 (j)_r=j(j-1)\cdots(j-r+1),\qquad
 \mathscr A_N(j;X)\in1+p^{p-2}
                     \mathscr C^\times\langle j\rangle .
 \end{gathered}
 \tag{Z4}
$$
第二行包括全部 $j-s$、所有 $s\in\mathbf Z_{\ge0}$，以及固定阶
权导数的统一界。它使用完整 $a_N$，不把它换成首项
$\exp(-Nc_\sigma z^d)$。对每个非负整数 $m$，原(W22)恰为
$$
 D^mF_{N,T}^{\sigma}(0)
   =(\boldsymbol\mu_{N,T})_F
            \bigl(c_1^m\mathscr A_N(m;c_1)\bigr).
 \tag{Z5}
$$
$F^\sigma$ 用覆盖 Lie 参数，故返回物理底层导数仍另乘
$p^{-m}$。式(Z5)是未除幂导数，没有遗漏一个 $m!$。

### 二、真正共同单位基及其 Teich 分支

不能只凭点值为单位就在(Z1)中写权指数。原(N3)–(N5)已经给出
原 universal-character 的准确系数
$$
 c_q=\frac{c_1}{p^q-p}+\frac{c_1^q}{q!}.
$$
令 $U_q=q!/p^{p+1}\equiv1\pmod p$，则在单位域上
$$
 u=\frac{c_1^\Delta}{p^p}
    =\frac{U_q}{1-p^\Delta}
          +pU_q\frac{c_q}{c_1},\qquad
 v_{\rm pt}(u-1)\ge1-\tau .
 \tag{Z6}
$$
这里 $u,u^{-1}$ 均属于原 $\mathscr C^\times$ 的单位。
点值估计的实际 gauge 消费是
$(u-1)^k\in p^{\lfloor k(1-\tau)\rfloor}\mathscr C^\times$。
因此
$\sum_k\binom{x}{k}(u-1)^k$
在整个 $|x|\le1$ Tate 盘收敛：
其第 $k$ 项的 gauge 至少
$\lfloor k(1-\tau)\rfloor-v_p(k!)\to+\infty$。
该下界非负；负指数给其整逆。这里用的是逐幂的真实整格，
不是将一个分数点值估计直接当作 tensor 整性。

定义
$$
 \alpha=\frac{\rho L_-L_+}{p^2},\qquad
 U=\alpha XY,\qquad
 a_0=\alpha\varpi_0^2
          =\frac{\kappa_A}{612\omega\delta}\in\mathcal O_L^\times .
 \tag{Z7}
$$
最后一个等式由(Z3)逐项得出。在参考及其实际 $L$-单位
标记上 $a_0^\Delta\in1+p\mathcal O_L$。
置 $u_0=\varpi_0^\Delta/p^p$；同(Z6)在原生成元上评价给
$v_p(u_0-1)\ge1-\tau$。所以
$$
 U^\Delta=\theta\,(u\otimes u),\qquad
 \theta=\alpha^\Delta p^{2p}
             =a_0^\Delta/u_0^2,\qquad
 v_p(\theta-1)\ge1-\tau .
 \tag{Z8}
$$
按(Z6)逐因子展开，$(U^\Delta)^x$ 是真实的
$\mathscr B_{\mathbf C_p}\langle x\rangle$ 单位，逆为
$(U^\Delta)^{-x}$。这没有从
$\|U^\Delta-1\|_{\rm pt}<1$ 免费推到完成 tensor。
对每个 $s\ge0$，还准确有
$$
 v_{\rm gauge}(U^{-s})
 \ge 2s\tau-2\lceil s\tau\rceil\ge-2 .
 \tag{Z9}
$$
故所有移位使用同一个界；无需不断扩大负权预算。

保原 R1059 及(N13)的同一个合法负二分支。
令 $e_1$ 为已固定的 prime-to-$p$ 整数，$e$ 为已支付的共同深度，
写 $j=-2+\Delta e_1p^e z$，$|z|\le1$。定义
$$
 U^{[-2-s]}(j-s)
     =U^{-2-s}(U^\Delta)^{e_1p^ez}\qquad(s\ge0).
 \tag{Z10}
$$
在合法非负整数 $n\equiv-2\pmod{\Delta e_1p^e}$ 上，
本式就是 $U^{n-s}$。它保全部原 Teich 相位。
$e_1$ 保留原有限角色的 prime-to-$p$ 部分，$e$ 保留原 $p$ 部分；
两者对全部实际字共同选择。不用单纯增加 $e$ 冒充 $e_1$，
不重选源角色，也不以 $p^j$ 作解析函数。

### 三、由原 new word 到全部 raw 移位权

先固定一个尚未加外权的实际新 word。
令
$\boldsymbol\nu_T=
 \boldsymbol\mu_{102,T}\widehat\otimes
 \boldsymbol\mu_{34,MT}$，
以及 $P_0=\Omega_A^3L_+^2/p^2$。
其所有移位 raw germ 定义为
$$
 \mathcal R_{T,s}(j)
 =P_0\,(\boldsymbol\nu_T)_{\mathbf C_p}
 \left[
 Y^2\,U^{-2-s}(U^\Delta)^{(j+2)/\Delta}\,
 \mathscr A_{102}(j-s;X)\,
 \mathscr A_{34}(j+2-s;Y)
 \right].
 \tag{Z11}
$$
这里 $(j+2)/\Delta=e_1p^ez$。由(Z4)、(Z8)、(Z9)，
它们在整个固定权盘一致有界，界不依赖 $s$。
固定实际 source 幅度先乘回原值；没有把该幅度从正权平方
重新取根。固定有限系数域的 trace 和 Artin 权也按原操作。

为核(Z11)的物理来源，将该 word 的已经代数化 coherent
函数写为
$F_{-,T}^\sigma(L_-Z/p)F_{+,MT}^\sigma(L_+W/p)$，
并保它的原固定幅度。由(Z5)，其 $(n,n+2)$ 未除幂槽准确给
$$
 \Omega_A^3\rho^n
  \left(\frac{L_-}{p}\right)^n
  \left(\frac{L_+}{p}\right)^{n+2}
 \boldsymbol\nu_T
  \bigl(X^nY^{n+2}
    \mathscr A_{102}(n;X)\mathscr A_{34}(n+2;Y)\bigr)
 =\mathcal R_{T,0}(n).
 \tag{Z12}
$$
这包括原 $a=17/2$，因为它已在 $\rho$ 中。
对 $n-s\ge0$ 同理返回 $\mathcal R_{T,s}(n)$。
(W17)的 Haar $p^{-2}$ 尚未乘入(Z12)；
它和两个物理 $p^{-n}$ 是不同费用。

### 四、原 coherent multiplication 的正确有界测试

置
$$
 \Theta=\frac{\beta_0p^2}{XY}=-\frac C U,\qquad
 c_r(j)=\binom jr\binom{j+2}{r}r!
       =\frac{(j)_r(j+2)_r}{r!}.
 \tag{Z13}
$$
这是原 coherent Gaussian 的逆矩参数，
不是 $\exp(b_0XY)$ 的参数。
为每个 $s\ge0$ 定义
$$
 \begin{aligned}
 \mathscr G_s(j;X,Y)
   &=\sum_{r\ge0}c_r(j-s)\Theta^r
       \mathscr A_{102}(j-s-r;X)
       \mathscr A_{34}(j+2-s-r;Y),\\
 \mathcal M_{T,s}(j)
   &=P_0(\boldsymbol\nu_T)_{\mathbf C_p}
       \left[Y^2U^{-2-s}(U^\Delta)^{(j+2)/\Delta}
                     \mathscr G_s(j;X,Y)\right].
 \end{aligned}
 \tag{Z14}
$$
这些都是同一固定权盘上的真实收敛级数。具体地，
(Z2)与 $v_p(\beta_0)=2\tau$ 给
$$
 \begin{aligned}
 v_{\rm gauge}(\Theta^r)
   &\ge 2r+2r\tau-2\lceil r\tau\rceil,\\
 v_{\rm Gauss}\bigl(c_r(j-s)\Theta^r\bigr)
   &\ge 2r+2r\tau-2\lceil r\tau\rceil-v_p(r!)\\
   &\ge2r-2-v_p(r!)\longrightarrow+\infty .
 \end{aligned}
 \tag{Z15}
$$
第一项 $r=1$ 的真实下界为 $2\tau>0$，不能只用最后的粗界0。
所有 $s$ 及固定阶权导数使用同一个界。
特别 $\mathscr G_s$ 是一个真实
$1+\mathfrak m_{\mathbf C_p}$ 的完成 tensor Tate 单位：
$r=0$ 的两连接因子由(Z4)为 $1+p^{p-2}$，
其余项由(Z15)严格小于1。
这个单位结论没有将其经 $\boldsymbol\nu_T$ 的值宣称为单位；
一个有界对偶可以在一个可逆测试上取零。

在每个非负整数 $n$ 上，$c_r(n)=0$ 对 $r>n$。
对原函数乘 $\exp(\beta_0z_-z_+)$ 并读 $(n,n+2)$ 槽，
Leibniz 公式逐项给(Z14)：一次收缩各减少一阶导数，
贡献 $\beta_0$，返回覆盖导数则多 $p^2$，
且去掉 $XY$，恰是(Z13)。
因此(Z14)给原 R1060(16b)的 **Amice 普通矩** $m_n$，
而(Z12)给其 **unflat raw 行** $R_n$。
这两者的命名不能互换。

### 五、完整移位族上的两个相反 Maass 变换

在上述一致有界移位族上，令
$$
 (\mathcal S_D\mathcal F)_s(j)
    =\sum_{r\ge0}c_r(j-s)D^r\mathcal F_{s+r}(j),
       \qquad v_p(D)\ge2 .
 \tag{Z16}
$$
(Z14)精确说
$\mathcal M_T=\mathcal S_{-C}\mathcal R_T$。
各级数一致收敛，且
$$
 \boxed{\quad
 \mathcal S_D\mathcal S_E=\mathcal S_{D+E},
 \qquad
 \mathcal S_C\mathcal M_T=\mathcal R_T .
 \quad}
 \tag{Z17}
$$
完整证明是
$$
 c_r(j-s)c_t(j-s-r)
       =\binom{r+t}{r}c_{r+t}(j-s).
$$
双级数第 $(r,t)$ 项的估值至少
$2(r+t)-v_p(r!)-v_p(t!)$ 加同一个固定常数，
故可交换、按 $r+t$ 合并。该层内的有限二项和为
$(D+E)^{r+t}$，于是得(Z17)。对权导数也可逐项作同样运算。

这支付的是本题实际 Katz 新来源、真实 connection 及原 Gaussian
的完整交织。没有据此声称任意 bounded 测度都能作全
$\exp(CL)^*$；也没有把 $\mathcal S_C$ 换成一个不同 polarisation
的 Weil operator。原有限 Weil 字已经在
$\boldsymbol\nu_T$ 内，(Z17)作用于其同一 coherent 导数族。

### 六、负二端点、斜率和两个 E 费用

记
$\ell_U=\Delta^{-1}\log(U^\Delta)$，
其意义由(Z6)–(Z10)的收敛级数固定。
在 $j=-2$，$\mathscr A_{34}(0;Y)=1$，
所以(Z11)给
$$
 \boxed{
 \mathcal R_{T,0}(-2)
   =\frac{\Omega_A^3p^2}{\rho^2L_-^2}\,
      \boldsymbol\mu_{102,T}
           \bigl(X^{-2}\mathscr A_{102}(-2;X)\bigr)
      \boldsymbol\mu_{34,MT}(1).
 }
 \tag{Z18}
$$
原(N15)已经证明的实际负二连接返回是
$$
 \boldsymbol\mu_{102,T}
       \bigl(X^{-2}\mathscr A_{102}(-2;X)\bigr)
  =p^{-2}b_{102,T}R_-(Q)
       (102Z_Q)^{-2}\mathcal F_{102,Q}(-2).
$$
故(Z18)正返 R1062 的同一个 primitive。
此处两个 $p^2$ 相消；原 W17 的 Haar $p^{-2}$ 仍另保。
再乘原 $c_0^{(0)}$ 后恰是 R1063(I18a)，
不产生新的 $17$ 或 $\delta$ 费用。

原 raw 斜率也由同一个双对偶明确给出：
$$
 \begin{aligned}
 \mathcal R_{T,0}'(-2)
 =P_0(\boldsymbol\nu_T)_{\mathbf C_p}
 \bigl[Y^2U^{-2}\{
 &\ell_U\,\mathscr A_{102}(-2;X)
       +\partial_j\mathscr A_{102}(-2;X)\\
 &+\mathscr A_{102}(-2;X)
                \partial_j\mathscr A_{34}(0;Y)\}\bigr].
 \end{aligned}
 \tag{Z19}
$$
这是对原指数 $j$ 求导；若用参数 $z$，另乘
$\Delta e_1p^e$。$\ell_U$ 和连接导数不能删除。

另一方面，$c_r(-2)=0$ 对 $r>0$，而
$$
 c_r'(-2)=-(r+1)(r-1)!\qquad(r\ge1).
$$
因此两步斜率各自是
$$
 \begin{aligned}
 \mathcal M_{T,0}'(-2)
 &=\mathcal R_{T,0}'(-2)
    -\sum_{r\ge1}(r+1)(r-1)!(-C)^r\mathcal R_{T,r}(-2),\\
 \mathcal R_{T,0}'(-2)
 &=\mathcal M_{T,0}'(-2)
    -\sum_{r\ge1}(r+1)(r-1)!C^r\mathcal M_{T,r}(-2).
 \end{aligned}
 \tag{Z20}
$$
第一行是 coherent inverse Gaussian，第二行才是原完整
log$-E$ reader。它们经(Z17)的 **完整移位双卷积** 精确返回
(Z19)，不是断言 $E(t)+E(-t)=0$，
也不是将两行中的移位来源认成同一列后逐项消去。

### 七、原 finite h、圆周投影、old 和冻结外权

先在 R1065(W17)的真正有限 Heisenberg 模上保留
$$
 (p^{-2}-1)\,\phi f_-\otimes\phi f_+
   +p^{-2}\sum_{v\ne0}A_{-,\widetilde v}\otimes A_{+,M\widetilde v}.
 \tag{Z21}
$$
(Z11)–(Z20)只为第二项给新的显式 Katz 表达。
它没有替第一项制造单位支撑，也不通过除一个
$c_1$ 将 old 偷偷删除。若消费已有的原 old 平坦极限，
必须仍用它已经支付的实际来源、正权界和原极限；
本部分不增加一个 old=0 假设或结论。

对实际有限 $h$，W26 已确定对偶图
$-g_+^{-T}M^{-T}g_-^T$。
先按该式运输整份 theta 字、框架、中心及其 Katz 对偶，
再用本部分的同一个自然导数收缩。
(Z12)、(Z14)均为该字的实际坐标恒等式；
任何已付的同源/微分变量改变，都对
$\rho,C,L_\pm,X,Y$ 同时运输。
关键关系 $\Theta=-C/U$ 是几何 contraction 的等式，因而保留。
不把未运输的 $M$ 或 $612\omega$ 直接复制到另一未对齐框架。
原全18个核、full2/full9、两条三挠词、17角色和 Artin/Cor
仍由原 finite operator 完整作用；没有另添输出 torus。

无穷圆周只按原差2 angular projector 消费。
在 coherent 多项式上，它投影到 $W$ 次数减 $Z$ 次数为2；
$ZW$ 权为0，且一次 contraction 同时减少两边一次数。
故该 projector 与每个有限 Gaussian 收缩严格交换。
这个证明逐有限槽成立，先完成原复 period 的代数化再使用
(Z1)；不为一个连续实圆周上的每项新定义
$\mathbf C_p$ 测度，也不把投影后的 $W^2F(ZW)$
认作固定阿贝尔曲面上的全局 section。
各实际有限矩阵的范数仅贡献一个固定常数，
(Z4)、(Z9)、(Z15)的尾界不依赖移位权；
因此在原已经代数化的完整有限来源上可通过这些尾界作极限。

由此，原 whole 来源的每个有限整数槽和
R1060 的有限 $P_{2,H},K_{H,C}$ reader 都可逐项使用
(Z11)–(Z21)。若要写原平坦 germ，仍按 R1059
选择合法非负整数 $n_l\to j$ 且 $n_l\to+\infty$：
先保(Z21)全部项及实际 $\mathcal T_i$，再取原已付极限。
(Z11)的新项由已证解析性返回其值，old 按原自身界返回。
这里不把一个有限正整数上的 raw $R_n$ 免费认成
flat 值；这个区别正是 unit restriction 的费用。

这里须区别两个记号：$\mathcal M_{A_i}$ 始终指
R1060(3)中**已经施完整 Maass**的原 germ；
它不是(Z14)的 ordinary-moment 移位族 $\mathcal M_{T,s}$。
在已付全来源返回中，新部分准确是
$
 \begin{aligned}
 \mathcal M_{A_i}^{\rm new}(j)
 &=p^{-2}\mathcal T_i\!
      \left[\sum_{v\ne0}
          (\mathcal S_{C_i}\boldsymbol{\mathcal M}_{i,v})_0(j)\right]\\
 &=p^{-2}\mathcal T_i\!
      \left[\sum_{v\ne0}\mathcal R_{i,v,0}(j)\right],\\
 \mathcal M_{A_i}(j)
 &=(p^{-2}-1)\mathcal M_{{\rm old},i}(j)
                      +\mathcal M_{A_i}^{\rm new}(j).
 \end{aligned}
 \tag{Z21a}
$
$\mathcal T_i$ 仍包括全部已指定的有限 $h$、graded 运输和
差2 angular projector；old 记号也指其原完整 Maass germ。
因此下式的每个新项导数准确作用于
$\mathcal S_{C_i}\boldsymbol{\mathcal M}_{i,v}=\boldsymbol{\mathcal R}_{i,v}$，
而不是直接作用于(Z14)的 ordinary $\mathcal M_{T,0}$。
其完整 $E$ 费用由(Z20)第二行和(Z17)支付。
这里的 $\mathcal T_i[\cdot]$ 表示仅在原 $\mathcal T_i$ 内把 $p$ 处输入展开成(W17)，其余完整算子照原顺序保留；不再额外施一次 $p^2$ 投影或再收一份 Haar。

最终临界来源仍是
$$
 \sum_i\left\{
 \Lambda_i'(-2)\mathcal M_{A_i}(-2)
       +\Lambda_i(-2)\mathcal M_{A_i}'(-2)\right\}.
 \tag{Z22}
$$
$\Lambda_i(-2),\Lambda_i'(-2)$ 一开始就冻结。
本部分的权导数只对同一个内部来源和原实际 period 作用；
不在第 $n$ 槽把外权换成 $\Lambda_i(n)$。
原单个 Hall 的严格估值门
$v_p(\mathrm{Hall})<2/(p-1)$ 仍未由这些有界测试支付。
本结论给的是实际新 $p^2$ 来源到完整 coherent Gaussian、
Maass 与临界斜率的同源返回，不把对偶非零、整范数或测试可逆
升级为原 canonical 非零，更不升级为无穷多个目标 $p$。

