# R1065 — 原 Hall 来源的整 Katz 单位测度、完整零点项与前五层返回

日期：2026-11-28。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：本篇对原实际 $H_{34},H_{102}$ 构造唯一的整 Galois–Katz 单位测度，并给出同一 tame-zero Hall、完整负二有限测试、零点项和原 canonical 前五层的精确返回。完整 $p$ 核迹的分母在本题严格 LT 坐标中只需一个 $p$，不是两个。没有将此测度认成 R1056/R1064 原 $\mathbf Z_p$ 测度的 flat 完成，也未由整性推出任何一个 canonical 首系数是单位。**

依赖：

- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md) 的原严格 LT 坐标；
- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)、[R660](R660-original-torus-coordinate-and-boundary-resonance-ideal.md) 的完整 $T_{\rm g}$；
- [R1062](R1062-original-translated-miller-jets-and-critical-weight-germs.md) 的实际 $\mathcal F_{N,Q}(-2)$；
- [R1063](R1063-original-tame-zero-hall-and-five-layer-miller-return.md) (H1)–(H27)、§8(J1)–(J10)、§9(I1)–(I22) 的全部来源、中心、Haar、微分与外权；
- Laurent Berger, [Galois measures and the Katz map, arXiv:2504.20558v3](https://arxiv.org/html/2504.20558v3)，Introduction 的 Theorem A 及 §1 的 universal-character 系数。以下迹式、Hall 测试和原系数返回由本篇直接证明。

## 1. 固定原来源与同一严格形式群

保持 R1063 的惰性 $p\equiv5\pmod6$、$p>211$ 和既定固定坏位排除，置
$$
 q=p^2,\qquad \Delta=q-1,\qquad d=p+1,\qquad
 L=\mathbf Q_{p^2},\quad \mathcal O=\mathcal O_L.
 \tag{K1}
$$
估值规范为 $v_p(p)=1$。在原 $E_0:y^2=x^3+1$ 的形式群 $G$ 上，使用 R663/R1063 的严格整坐标 $v$：
$$
 [-p]_G(v)=-pv+v^q,\qquad
 [\zeta]_G(v)=\zeta v\quad(\zeta\in\mu_\Delta).
$$
因 $[-1]_G(v)=-v$，这里准确有
$$
 [p]_G(v)=pv-v^q .
 \tag{K2}
$$
原好参数 $w=x^{-1/2}$ 按同一整坐标运输，
$w(v)/v\in1+v^6\mathcal O[[v^6]]$。形式对数为
$z(v)=v+O(v^q)$；不把这个特征零形式式说成全系数整。

用 R1063(H2)、(H19)、(H23) 的实际两来源定义
$$
 \begin{aligned}
 f_+(v)&=H_{34}(v)
   =v^{34}T_{\rm g}(w(v))^{-34}R_S(w(v))
       \in v^6\mathcal O[[v]],\\
 f_-(v)&=H_{102}(v)
   =v^{102}T_{\rm g}(w(v))^{-102}R_-(w(v))
       \in v^4\mathcal O[[v]].
 \end{aligned}
 \tag{K3}
$$
两首系数均为1。$R_S$ 是原 $S=\sigma^{34}R_S$，$[z^6]S=1$；$R_-$ 是原两个三挠 Weyl 词完整相加、经 $\delta$ 拉回的 $D_-=\sigma^{102}R_-$，$[z^4]D_-=1$。不改成一条裸 degree34 来源。

$T_{\rm g}$ 是原完整整单位，仍依赖 $p$。R639 的
$\log T_{\rm g}=F_{\rm c}-F$，其中 $F=\log(\sigma/z)\in z^6L[[z^6]]$、$F_{\rm c}=\Pi_0F$，表明它在 $\mu_6$ 下不变。因此
$$
 f_+(\zeta v)=f_+(v),\qquad
 f_-(\zeta v)=\zeta^4f_-(v)\quad(\zeta\in\mu_6).
 \tag{K4}
$$
这些是原来源的型，不是另加的投影。

## 2. 完整 $p$ 核迹：实际只需乘一个 $p$

令 $\phi h(v)=h([p]_G(v))$。规范化完整迹 $\psi$ 定义为
$$
 (\psi f)([p]_G(v))
   =\frac1{q}\sum_{Q\in G[p]}f(v\oplus_G v_Q).
 \tag{K5}
$$
这与 Berger 的规范相同，包括原点和全部非零核点。

设 $Y=[p]_G(v)$。由(K2)，
$$
 \mathcal O[[v]]
   \simeq \mathcal O[[Y]][v]/(v^q-pv+Y)
$$
是 $\mathcal O[[Y]]$ 上秩 $q$ 的有限自由代数。Weierstrass 除法给每个 $f\in\mathcal O[[v]]$ 唯一的整分解
$$
 f(v)=\sum_{j=0}^{q-1} A_j(Y)v^j,\qquad
 A_j\in\mathcal O[[Y]] .
 \tag{K6}
$$
这里是完整级数的唯一分解，不是只对有限 Taylor 多项式运算。

多项式 $v^q-pv+Y$ 的 Newton sums 直接给
$$
 \operatorname{Tr}(1)=q,\quad
 \operatorname{Tr}(v^j)=0\ (1\le j<q-1),\quad
 \operatorname{Tr}(v^{q-1})=(q-1)p.
$$
它的 $q$ 个分支正是 $v\oplus_G v_Q$；所以此代数迹就是(K5)的完整形式群迹。于是
$$
 \boxed{\psi f=A_0+\frac{q-1}{p}A_{q-1}.}
 \tag{K7}
$$
特别 $\psi f\in p^{-1}\mathcal O[[v]]$，且 $\psi\phi=1$。定义
$$
 \boxed{
 g_f=p(1-\phi\psi)f
     =pf-p\,\phi A_0-(q-1)\phi A_{q-1}
      \in\mathcal O[[v]],\qquad \psi g_f=0 .
 }
 \tag{K8}
$$
所有原项都保留。按系数 Gauss 范数，
$\|\psi f\|\le p\|f\|$、$\|(1-\phi\psi)f\|\le p\|f\|$、
$\|g_f\|\le\|f\|$。本篇后文取 $g_\pm=g_{f_\pm}$。

这个一个 $p$ 的结论使用本题实际严格坐标(K2)。它没有把原 Katz 理论的 $\psi$ 另行缩放，也没有改掉全核的 $q^{-1}$。

## 3. 真正的 Galois–Katz 测度及点值测试

记 $G^\vee$ 为 Cartier 对偶，$\mathbb T=T_pG^\vee$。
对 $\xi\in\mathbb T$，其 universal formal character 写成
$$
 \mathbf t_\xi(v)=\sum_{k\ge0} c_k(\xi)v^k,\qquad c_0=1.
 \tag{K9}
$$
它满足 $\mathbf t_\xi(v\oplus u)=\mathbf t_\xi(v)\mathbf t_\xi(u)$。
每个 $c_k$ 是整、有界、Galois-equivariant 的连续函数。令
$$
 \mathscr C=C^0_{\rm Gal}(\mathbb T,\mathcal O_{\mathbf C_p}),\qquad
 \mathbb T^\times=\mathbb T\setminus p\mathbb T.
$$
Berger Theorem A 对 $S=\mathcal O$ 断言：Katz 对偶映射
$\mathcal K^*:\operatorname{Hom}_{\mathcal O}(\mathscr C,\mathcal O)
\to\mathcal O[[v]]$ 单射，像恰为所有 $\psi$-integral 级数；其测度支撑于 $\mathbb T^\times$ 当且仅当对应级数被 $\psi$ 杀掉。

(K8)本身整且后续所有 $\psi$ 迭代为0，所以存在唯一整 Galois 测度
$$
 \boxed{
 \mu_f:\mathscr C\longrightarrow\mathcal O,\qquad
 \operatorname{supp}\mu_f\subset\mathbb T^\times,\qquad
 \mu_f(c_k)=[v^k]g_f .
 }
 \tag{K10}
$$
这里的“整测度”是原定理的 Galois-continuous dual，不偷换成在任意标量函数上任意取值的 $\mathbf C_p$ 测度。

### 3.1 非基域挠点须用完整系数运输

取包含当前全部除点和有限中心的有限扩域 $F/L$。
在完成的标量扩张
$\mathcal O_F\widehat\otimes_{\mathcal O}\mathscr C$ 中定义
$$
 \mathbf e_Q=\sum_{k\ge0}v_Q^k\otimes c_k .
 \tag{K11}
$$
因 $v_p(v_Q)>0$ 且 $\|c_k\|\le1$，该和在一致范数下收敛。
$\mu_f$ 的标量扩张逐项给
$$
 \boxed{\mu_{f,F}(\mathbf e_Q)=g_f(v_Q),\qquad
        \mu_f(1)=g_f(0).}
 \tag{K12}
$$
在函数解释中 $\mathbf e_Q(\xi)=\mathbf t_\xi(v_Q)$，是实际 Cartier 配对。对 $Q\in G[p]$，其值在 $\mu_p$ 中并只依赖 $\xi\bmod p\mathbb T$。然而单独固定的非有理 $Q$ 并不使这个函数自动对 $G_L$ 等变；(K11)正是所需的系数运输。有限扩域及有界有限测试可按此扩大，负二测试中的实际有限域系数也在这个标量扩张中保留。下文对这类有限点测试若省去下标 $F$，始终指这里的完成标量扩张 $\mu_{f,F}$，不在原 $\mathscr C$ 上直接代入非等变函数。

### 3.2 原点项的精确式

若 $Q\in G[p]$，则 $\phi\psi f(Q)=\psi f(0)$，所以
$$
 \boxed{
 g_f(Q)-g_f(0)=p(f(Q)-f(0)).
 }
 \tag{K13}
$$
特别本题 $f_\pm(0)=0$，故
$f_\pm(Q)=(g_\pm(Q)-g_\pm(0))/p$。
即使原 $S(0)=0$，也不能因此将 $g_+(0)$ 删除。

更具体，写 $f(v)=\sum_{k\ge0}h_kv^k$。
非零核点满足 $v_Q^\Delta=p$，完整 $\mu_\Delta$ 和只保 $\Delta$ 的倍数。因此
$$
 \boxed{
 g_f(0)=-(q-1)\sum_{a\ge1}h_{a\Delta}p^{a-1}.
 }
 \tag{K14}
$$
该和收敛，并且对任意 $f(0)$ 都成立，因为常数项在 $1-\phi\psi$ 中准确相消。

对负源，(K4)使所有 $h^-_{a\Delta}$ 为0，于是
$$
 \boxed{g_-(0)=\mu_-(1)=0.}
 \tag{K15}
$$
正源的质量则是(K14)的全部高共振和。这一正质量没有被 canonical 质量零或中央坏条件控制。
(K15)只是这个新 Katz 对象的质量身份，不给原中央读者新增零行。

## 4. 完整 tame-zero Hall 与实际负二有限测试

保持 R1063(H10)–(H16) 的同一 $Q=pT\ne0$、Hall 群
$\widehat H=\mu_d$、原 CRT lift、两侧实际 Miller 中心
$\mathscr C_{N,T}$。特别
$$
 \mathscr C_{N,T}
 =b_{N,T}T_{\rm g}(w_Q)^N/v_Q^N
$$
是同一 Hall 轨道上的固定单位；它一般仍有真正 wild 角色，不能设为1。
原正范数为 $r$、负范数为 $r/3$，positive physical 标签
$\chi_r^{-1}$、positive $M$ 标签 $\chi_r$、negative $M$ 标签
$\chi_r^{-1}$，以及原 $e_p/\zeta_p$ 的相反方向均沿 R1063(H10)–(H13)不变。

定义有限的单位对偶测试
$$
 \mathscr E_Q
   =\frac1d\sum_{\zeta\in\mu_d}
        (\mathbf e_{[\zeta]Q}-1).
 \tag{K16}
$$
由(K12)–(K13)，原正 Hall 的准确式是
$$
 \boxed{
 \mathcal H_+^0(T_+)
   =\frac{\mathscr C_{34,T_+}}p\,
      \mu_{+,F}(\mathscr E_{Q_+}).
 }
 \tag{K17}
$$
右边仍是原 R1063(H23) 的那个 Hall 平均。
$\mathscr E_Q$ 是 universal additive pairing 的有限测试；
它本身不被重新命名为原 $\chi_r$。后者与原 wild 中心、真正 level lift 和物理标记一起保留。

负侧定义每个实际点的完整有限系数
$$
 a_Q^-=\frac{\mathcal F_{102,Q}(-2)}{(102Z_Q)^2},
 \qquad
 \mathscr E_Q^-=\frac1d\sum_{\zeta\in\mu_d}
     a_{[\zeta]Q}^-\bigl(\mathbf e_{[\zeta]Q}-1\bigr).
 \tag{K18}
$$
$\mathcal F_{102,Q}$ 正是 R1062 的全 Bell/translated-jet 函数，
$Z_Q$ 正是 R1063(H8)的原代数值。
这是一份有限测试，不断言 $a_Q^-$ 在另一个全盘来自新的有界 primitive。
同一负读数准确为
$$
 \boxed{
 \mathcal H_-^{[-2]}(T)
    =\frac{\mathscr C_{102,T}}p\,
          \mu_{-,F}(\mathscr E_Q^-).
 }
 \tag{K19}
$$
(K15)允许在本式去掉最后的常数1，但保留它使(K13)的来源清楚。
若只讨论 H20 的首五层，仍先把整个
$a_Q^-(g_-(Q)-g_-(0))$ 代回原 H18；不能分开估计 $g_-$ 与
$g_-(0)$ 后擅自保留原 $5/(p-1)$ 误差。

### 4.1 两 Hall 的 Haar 与 whole 来源保持原样

原两个 $d^{-1}$ Hall 平均在完整 coevaluation 中的系数是
R1063(H25)的 $d/p^2$。所以仅将(K17)、(K19)代入，得到
$$
 \boxed{
 \frac d{p^2}\mathcal H_-^{[-2]}\mathcal H_+^0
   =\frac{d\,\mathscr C_{102,T}\mathscr C_{34,T_+}}{p^4}
       \mu_-(\mathscr E_Q^-)\mu_+(\mathscr E_{Q_+}).
 }
 \tag{K20}
$$
两侧 Hall 和是独立的两个完整和，不能改成相关单点纤维。
还须将本篇(K3)的 \(E_0\) 模型与 R1063(I18)的 \(E_{17}\)
常数明确区别。保持原 \(\vartheta^6=17\)。其真实同构给
\[
 S_{17}(z)=\vartheta^{-6}S_1(\vartheta z),\qquad
 D_{102,17}(z)=\vartheta^{-4}D_{102,1}(\vartheta z).
\]
对相应除点及完整 Miller 字，
\(B_{-,17}=\vartheta^{-4}B_{-,1}\)、
\(A_{-,17}=\vartheta A_{-,1}\)，
\(\mathcal F_{-,17}(-2)=\mathcal F_{-,1}(-2)\)；
正槽 \(B_{+,17}=\vartheta^{-6}B_{+,1}\)。
故实际两 Hall 的模型运输是
\[
 \mathcal H_{+,17}^{0}=\vartheta^{-6}\mathcal H_{+,1}^{0},
 \qquad
 \mathcal H_{-,17}^{[-2]}=\vartheta^{-6}\mathcal H_{-,1}^{[-2]}.
 \tag{K20a}
\]
(K20)是 \(E_0\) 中的局部式，不需更改。
若使用 R1063(I18)的 \(c_0,\ell_\pm\)，必须保(K20a)的
\(\vartheta^{-12}=17^{-2}\)；等价地，在本篇模型定义
\[
 c_0^{(0)}=\vartheta^{-10}c_0,\qquad
 L_\pm=\vartheta\ell_\pm,\qquad
 c_0^{(0)}\Omega_A^3\rho_A^{-2}L_-^{-2}
   =17^{-2}c_0\Omega_A^3\rho_A^{-2}\ell_-^{-2}.
 \tag{K20b}
\]
真正 whole 来源是在(K20)上乘左边这个 \(E_0\) prefactor。
原 raw 幅度、十八个 degree17 商、两个 sign、\(h\) 积分、
Artin/Cor 与 \(\lambda,\lambda'\) 均原样保留。
本篇没有再乘一次 \(p\)-Haar。
由于 \(p>211\)，上述模型因子都是 \(p\) 单位，故(K22)–(K29)
在各自已明写的模型中的整性和严格估值门不变。


(K20)给的是已经运输的**值端点**。一般完整临界斜率还含
R1063(I20)的外权导数、$\log U_*$、负侧导数和正侧导数。
不能从(K20)删除这些项，也不能把两份 $\mu_\pm$ 当作原
$\mathbf Z_p$ flat 测度的无偿分解。

### 4.2 全轨道检查

所有非零 $p$-核点恰分成 $p-1$ 个 $\mu_d$ 轨道。
由 $\psi g_f(0)=0$，
$$
 \sum_{Q\in G[p]}g_f(Q)=0.
$$
因此(K16)的全部轨道满足准确检查式
$$
 \sum_{\mathcal O}\mu_f(\mathscr E_{Q_{\mathcal O}})
    =-\frac qd\,\mu_f(1).
 \tag{K21}
$$
这也可由 primitive dual 上的完整有限 Cartier 角色正交得到。
式中没有各轨道不同的原 $\mathscr C_{N,T}$；不能把(K21)当成
加上这些 wild 中心之后的原 Hall 总迹，更不能据此再赋 canonical 零条件。

## 5. 同一个 $g_f$ 的低系数：原 canonical 首行与前五层

置 $b_k=[v^k]g_f$、$h_k=[v^k]f$。
从(K7)写 $\psi f=\sum e_kv^k$，有 $e_k\in p^{-1}\mathcal O$。
当 $1\le k<q$ 时，$(pv-v^q)^j$ 的次数 $k$ 项只有 $j=k$ 的
$p^kv^k$；所以
$$
 [v^k]\phi\psi f=p^ke_k,\qquad
 \boxed{\frac{b_k}{p}-h_k=-p^ke_k\in p^{k-1}\mathcal O.}
 \tag{K22}
$$
尤其所有这些 $b_k/p$ 整。这里没有声称 $g_f/p$ 的全部高系数整。

定义两份真正有限的 divided-Katz 系数行
$$
 \begin{aligned}
 \mathcal B_{+,4}^{\rm K}(W)
   &=\sum_{j=0}^{4}
       \frac{\mu_+(c_{(j+1)d})}{p}W^j,\\
 \mathcal B_{-,4}^{\rm K}(W)
   &=\sum_{j=0}^{4}
       \frac{\mu_-(c_{(j+1)d-2})}{p}W^j .
 \end{aligned}
 \tag{K23}
$$
$5d<q$ 且最小所读次数为 $p-1$。
R1063(H21)、(H23)和(K22)逐项给
$$
 \boxed{
 \mathcal B_{+,4}^{\rm K}\equiv\mathcal B_{34},\qquad
 \mathcal B_{-,4}^{\rm K}\equiv\mathcal B_-
       \pmod{(p,W^5)}.
 }
 \tag{K24}
$$
每个系数差的实际精度更强：正侧为
$p^{(j+1)d-1}$，负侧为 $p^{(j+1)d-3}$。
因此它们在 $W^{p-1}=p$ 的原边界上也严格深于第五层。
原 H27/J9 的五层完整卷积可直接使用这两份 finite 行；
全部 $E_{\rm c}$ 高项、$\widehat3$ 和 $U_5$ 不变。

特别，R1063(H21)–(H23)首项给
$$
 \boxed{
 \frac{\mu_+(c_{p+1})}{p}\equiv s_{p+1},\qquad
 \frac{\mu_-(c_{p-1})}{p}\equiv d_{-,p-1}\pmod p .
 }
 \tag{K25}
$$
右边正是原单参数 Newton 的 canonical 首行和原负 companion 首行，
不是新选的 theta 系数。

### 5.1 准确的 Cartier-dual LT 矩形式

(K9)满足
$\mathbf t_\xi(v)=\exp(c_1(\xi)\log_G(v))$。
由 $\log_G(v)=v+O(v^q)$，对于 $k<q$ 严格有
$$
 c_k(\xi)=\frac{c_1(\xi)^k}{k!}.
$$
因此(K25)可写成
$$
 \boxed{
 s_{p+1}\equiv
   \frac{\mu_+(c_1^{\,p+1})}{p(p+1)!},\qquad
 d_{-,p-1}\equiv
   \frac{\mu_-(c_1^{\,p-1})}{p(p-1)!}
       \pmod p .
 }
 \tag{K26}
$$
两份商的整性由(K22)支付。
$c_1$ 是原 Cartier 对偶的真实线性 character 系数，含其实际
$p$ 进 period；没有将它设为1，也没有将 LT 指数 $k$ 认成原 Mellin 权。
把 $1/k!$ 移出测度是先用 $k!c_k=c_1^k$ 的整函数恒等，
而非免费对所有函数除以 $k!$。

因 $v_p((p+1)!)=1$，正源的准确单位门成为
$$
 \boxed{
 s_{p+1}\in\mathcal O^\times
   \ \Longleftrightarrow\
 v_p\bigl(\mu_+(c_1^{p+1})\bigr)=2.
 }
 \tag{K27}
$$
负源同理为
$d_{-,p-1}\in\mathcal O^\times
\Longleftrightarrow
v_p(\mu_-(c_1^{p-1}))=1$。
测度整且支撑于单位部分本身不决定这些等号。

## 6. 同一对象的模 p Cartier 表达

(K6)模 $p$ 时 $Y=-v^q$。于是
$$
 \overline{A}_{q-1}(Y)
   =\sum_{a\ge0}\bar h_{qa+q-1}(-Y)^a .
$$
由(K8)，$-(q-1)\equiv1\bmod p$，给
$$
 \boxed{\bar g_f(v)=
   \sum_{a\ge0}\bar h_{qa+q-1}v^{qa}.}
 \tag{K28}
$$
在剩余形式盘上，若
$C^2(\bar f(v)\,dv)=B(v)\,dv$，
则(K28)等价于 $\bar g_f=B(v)^q$。
这里是系数级的两次 Cartier 再取 Frobenius；不是把
Frobenius 对微分的拉回写成非零。

(K28)适用于当前真实 $p$ 依赖的 $T_{\rm g}$ 和当前形式坐标。
它没有证明 $\bar f\,dv$ 来自某个固定全局有理微分或固定 theta 连接。
把(K25)进一步解释成一次 Cartier 的全局读数，仍须实际运输
$v^{-2}H_+\,dv$ 或 $H_-\,dv$、原不变微分与完整 gauge；
本篇不把这一步藏在“Cartier”名称中。

## 7. 原严格估值门及仍须支付的算术内容

回 R1063(H23)，$\mathscr C_{34,T}$ 为单位，
$W_+^{p-1}=p$，$\mathcal B_{34}\in\mathcal O[[W]]$。
所以
$$
 \begin{aligned}
 s_{p+1}\in\mathcal O^\times
 &\Longrightarrow
 v_p(\mathcal H_+^0)=\frac1{p-1},\\
 s_{p+1}\in p\mathcal O
 &\Longrightarrow
 v_p(\mathcal H_+^0)\ge\frac2{p-1}.
 \end{aligned}
$$
乘回原 $d$、$\sqrt d$ 及既定 $b=17$ 同构的单位规范后，
R716 的同一个单 Hall $\mathscr S_p(r)$ 因而满足
$$
 \boxed{
 v_p\mathscr S_p(r)<\frac2{p-1}
 \ \Longleftrightarrow\
 s_{p+1}\in\mathcal O^\times
 \ \Longleftrightarrow\
 v_p\mu_+(c_1^{p+1})=2 .
 }
 \tag{K29}
$$
任一个固定允许 $r$ 已足够；首项为单位时全部这些 $r$ 都有同一首估值。

[原 first-wild Rubin 注](../notes/2026-11-15-original-first-wild-rubin-factor-and-central-order.md)
与 R1063(I21)–(I22) 保同一整 Iwasawa 函数 $A_p$：
$v_pA_p(t_{\chi_r^2})=2v_p\mathscr S_p(r)$，
坏中央条件给 $\operatorname{ord}_TA_p\ge4$，
因此必有 $v_p\mathscr S_p(r)\ge2/(p-1)$。
(K29)把排除该坏条件所需的精确单位门落到了
**原实际 Hall 来源构造的那一份 Katz 测度**上。
没有证明这个门对无穷多个 $p$ 成立。

R1064 中从已给原 $\mathbf Z_p$ 测度沿一条 $\mathbf Z_p$ 子线送入
LT Fourier 变换的对象另有其真实单位限制公式。
本篇的 $\mu_\pm$ 则由(K3)、(K8)和 Berger Theorem A 独立确定，
不是那条子线的同名重写。完整 whole 来源的实际
$\lambda/\lambda'$、Maass 与 period 费用仍按 R1063/R1064 保留。
