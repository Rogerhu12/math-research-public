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



## 8. 两个原 Katz 对偶的真实张量及全部系数域

本节以下只使用(K10)已经构造的两份实际测度，不将原
$\mathbf Z_p$ Amice 测度重新命名为它们。记
$$
 \mathscr A_2^\circ
   =\mathscr C\widehat\otimes_{\mathcal O}\mathscr C,\qquad
 \mathscr A^{(2)}=\mathscr A_2^\circ[1/p],
 \tag{T1}
$$
第一式按 $p$-adic 整格完备化，第二式使用此格的 gauge 范数。另记单份 $\mathscr A=\mathscr C[1/p]$。
$\mathscr C$ 仍是(K9)--(K10)的 Galois-equivariant 连续函数空间，
不把它改成任意标量函数的空间。
对 $f\in\mathscr C[1/p]$，这个整格 gauge 的估值是
$\lfloor\inf_\xi v_p(f(\xi))\rfloor$，与可能取非整数的 pointwise
sup 估值分开。乘法保整格，所以(T1)是 Banach 代数。
$\mathscr C$ 在 $\mathcal O$ 上无挠，故其 tensor 无挠；再作分离完备化。

两份实际 Katz 测度有唯一的连续张量泛函
$$
 \boldsymbol\mu=\mu_-\widehat\otimes\mu_+:
       \mathscr A_2^\circ\longrightarrow\mathcal O,\qquad
 \boldsymbol\mu(f\otimes g)=\mu_-(f)\mu_+(g).
 \tag{T2}
$$
它延到(T1)的有理化，按上述整格 gauge 的算子范数至多1。
证明是在代数整 tensor 上定义该泛函，它保每个 $p^m$ 倍整格，
随后完备化。不能仅从 $\mu_\pm(\mathscr C)\subset\mathcal O$
断言它对 fractional pointwise sup 范数的算子范数也为1。
这里也不需要先断言(T1)等于所有二变量 Galois-equivariant 连续函数。

对包含当前除点、Miller 中心、模型同构及全部有限系数的有限域
$F/L$，以下取同一个完成的标量扩张
$F\widehat\otimes_L\mathscr A^{(2)}$ 和
$\boldsymbol\mu_F$。例如
$$
 \boldsymbol\mu_F\bigl(
   (\mathbf e_Q-1)\otimes(\mathbf e_R-1)\bigr)
  =(g_-(Q)-g_-(0))(g_+(R)-g_+(0)).
 \tag{T3}
$$
两点可独立。式中 $Q,R$ 的系数运输准确使用(K11)，不能只将一个
非基域点的 pairing 函数称为 $G_L$-equivariant。
完整 Haar 对偶、相位、两独立 Hall 和及零点项继续按(K18)--(K20)。

## 9. 原 E0、A4、E17 三个微分 frame 中的确切 Gaussian

### 9.1 同一个 Cartier-dual Tate 生成元

置 $t_4=2^{1/3}$、$\vartheta^6=17$，取原实际同构
$$
 j_4:E_0\longrightarrow A_4,\qquad
 (x,y)\longmapsto(t_4^2x,t_4^3y),\qquad
 j_4^*\omega_A=t_4^{-1}\omega_0 .
 \tag{T4}
$$
将 R1063(I12)--(I13)的原 Tate 基 $\alpha_A$ 沿 $j_4^{-1}$
拉回，定义 $\alpha_0$，并令
$\xi_0=e_0(\alpha_{0,2},-)$。
这是一个明确的实际 dual 生成元，不为取得单位另换一个比例。
以原严格坐标的首项归一，$\omega_G=\omega_0$。
写 $c_1(\xi_0)=\varpi_0$，则
$c_1(a\xi_0)=a\varpi_0$；这里 Cartier dual 的
$\mathcal O_L$ 作用按预复合定义。

R1058(1)、(11)给同一个 CM 基
$$
 z_0=-\omega=\frac{1-\delta}{2},\qquad
 \widehat z_0=-\omega^2=\frac{1+\delta}{2},\qquad
 Y_A=\frac{\widehat z_0}{\delta},\qquad
 Y_A^2=-\frac{\omega}{3}.
 \tag{T5}
$$
R1064(R2)--(R5)的 HT/dlog 比较先沿(T4)拉回，遂准确有
$$
 \boxed{\quad \Omega_A\varpi_0=Y_A/t_4.\quad}
 \tag{T6}
$$
具体地，$j_4^*s_A=s_0=\varpi_0\omega_0$，而
$\omega_A=\Omega_A s_A/Y_A$；代入(T4)即得(T6)。
因此没有把另一个形式参数的 $\lambda_G$ 默认为1，也没有将
$E_{17}$ 的 book period 认成 $E_0$ 的 period。

### 9.2 两槽与全部首项尺度

R1063(I11)--(I13)的原函数及同源槽是
$$
 \begin{aligned}
 D_{102,17}(z)&=\vartheta^{-4}D_{102,1}(\vartheta z),&
 S_{17}(z)&=\vartheta^{-6}S_1(\vartheta z),\\
 \ell_-\ell_+&=\frac{\delta\omega}{2\cdot51^2u^2},&
 u&=\vartheta/t_4 .
 \end{aligned}
$$
所以用本篇(K3)的两个 $E_0$ 来源表示同一个双字时，必须同时取
$$
 \boxed{
 c_0^{(0)}=\vartheta^{-10}c_0,\qquad
 L_-=\vartheta\ell_-,\quad L_+=\vartheta\ell_+,\qquad
 L_-L_+=\frac{\delta\omega t_4^2}{2\cdot51^2}.
 }
 \tag{T7}
$$
原 degree17 word、两个 sign、十八核、Artin/Cor、实际 $h$ 及
非 $p$ 幅度仍在 R1063(I12c)、(I14)所给的位置。
(T7)仅改这两个实际 rank-one 函数的模型，未改变原来源。
特别
$$
 \frac{c_0^{(0)}}{L_-^2}
     =\vartheta^{-12}\frac{c_0}{\ell_-^2}
     =17^{-2}\frac{c_0}{\ell_-^2}.
 \tag{T8}
$$
这也逐槽等于 negative $m=-2$ 的 $\vartheta^{-6}$
与 positive $m=0$ 的 $\vartheta^{-6}$ 之积。

原最大阶基的参数为
$$
 C_A=-p^2Y_A/\widehat z_0=-p^2/\delta,\qquad
 \rho_A=(17/2)p^2\kappa_A\Omega_A^2,\qquad
 \beta_A=-C_A/\rho_A .
$$
若 $z_-=L_-Z,z_+=L_+W$ 是实际 $E_0$ Lie 槽，则原
$\exp(\beta_A ZW)$ 的系数变成
$$
 \boxed{
 \beta_0=\frac{\beta_A}{L_-L_+}
       =-\frac{204}{\omega\kappa_A t_4^2\Omega_A^2}
       =\frac{612\omega}{\kappa_A}\,\varpi_0^2 .
 }
 \tag{T9}
$$
第二个等号代入(T6)及 $Y_A^2=-\omega/3$。
原参考基 $\kappa_A=1$；其它实际 frame 必须先按
R1063(I12b)--(I12d)运输，不任意将其置一。
$p>211$ 时 $612\omega/\kappa_A$ 是此原基中的单位。
负102的 $\delta^{-1}$ 已在 $L_-$ 中，不能再乘第二次。

## 10. 一份真实有界的双 Katz Gaussian 及其正确算子方向

令 $b_0=612\omega/\kappa_A$。在(T1)上定义
$$
 \mathfrak G_{b_0}
   =\sum_{r\ge0}\frac{b_0^r}{r!}\,
                  c_1^r\otimes c_1^r .
 \tag{T10}
$$
两份 $c_1$ 是同一 $E_0$ 的两个独立 Cartier-dual 变量；
正、负 Weil 模型的反向点标记仍在实际 Hall 测试中，
并未因(T10)而被删除。

由(T6)和 R1064 的原 LT 周期赋值，
$c_1$ 的 pointwise 范数是 $p^{-\tau}$，
$\tau=p/(p^2-1)$。整 tensor 需要另行支付：
$$
 \boxed{
 c_1^r\in p^{\lfloor r\tau\rfloor}\mathscr C,\qquad
 v_{\rm gauge}\!\left(
       \frac{b_0^r}{r!}c_1^r\otimes c_1^r\right)
   \ge 2\lfloor r\tau\rfloor-v_p(r!)
   \ge0 .
 }
 \tag{T11}
$$
最后的不等式可完全按整数证明。令 $m=\lfloor r/p\rfloor$；
$\tau>1/p$ 给 $\lfloor r\tau\rfloor\ge m$，
而 Legendre 公式给
$v_p(r!)=m+v_p(m!)\le2m$（$p>2$）。
并且(T11)的下界至少
$r/(p+1)-2\to+\infty$。
所以(T10)真在 completed integral tensor 中收敛。
同样证明负参数收敛；两级数的乘积可以按此一致尾重排，
逐总次数的 binomial 和使其恰为1。因此
$$
 \boxed{
 \|\mathfrak G_{b_0}\|_{\rm gauge}
  =\|\mathfrak G_{b_0}^{-1}\|_{\rm gauge}=1,\qquad
 \boldsymbol\mu^{\,b_0}(F)
       :=\boldsymbol\mu(\mathfrak G_{b_0}F),\qquad
 \|\boldsymbol\mu^{\,b_0}\|_{\rm gauge}
       =\|\boldsymbol\mu\|_{\rm gauge}.
 }
 \tag{T12}
$$
这是原两份 Katz 对偶的一个实际有界、整格等距 twist。
若另在有理 projective pointwise 范数下计算，单项还有较强的
$2r\tau-v_p(r!)\ge r/(p+1)$ 界，但它不代替(T11)的整格证明。
不从(T12)推导新的 canonical 零或非零。

其 Fourier 算子方向可以完整核清。令 $D_G$ 为原不变微分
$\omega_0$ 的对偶导子；对 universal character，
$$
 D_G\mathbf t_\xi(v)=c_1(\xi)\mathbf t_\xi(v).
$$
先按(K11)的 universal character 系数，在两个形式变量上定义
$$
 F_{b_0}(v,w)=
 \boldsymbol\mu\!\left(
 \mathfrak G_{b_0}(\mathbf e_v\otimes\mathbf e_w)\right).
$$
按系数定义后得到下述整系数双幂级数，可在任意 $\mathbf C_p$ 点的共同闭内盘上评价；也可用完成的 $\mathbf C_p$ 标量扩张。这样不要求先固定的有限 $F$ 包含所有评价点。在任意共同闭内盘逐项求导/积分均一致，且全开盘范数有界。
准确恒等式是
$$
 \boxed{
 F_{b_0}(v,w)
  =\sum_{r\ge0}\frac{b_0^r}{r!}
        (D_{G,v}^rg_-(v))(D_{G,w}^rg_+(w)).
 }
 \tag{T13}
$$
这里的全局收敛直接来自(T11)，不是一般热算子的收敛假设。
更具体地，$D_G^rg_\pm$ 的每个形式系数都是
$\mu_\pm(c_1^rc_k)$，因此全部被
$p^{\lfloor r\tau\rfloor}$ 整除；(T13)的所有形式系数整，
且其 $r$ 尾在整系数 Gauss 范数中一致趋零。
同理负参数给逆操作，限于这些实际 Katz 对偶所构造的对象。乘测试函数不扩大原测度的支撑，所以双 twist 仍支持于 $\mathbb T^\times\times\mathbb T^\times$，其 Fourier 函数在两个变量中分别被 $\psi$ 杀掉。亦可由 $\psi D_G=pD_G\psi$ 与上述一致尾逐式得到该结论。

(T13)是 Fourier 侧的 mixed differential heat。
原 R1060(16a)却是在 coherent 变量上乘
$\exp(\beta_A ZW)$。二者方向不同。
在有限 Lie 多项式测试 $P(X,Y)$ 上，
coherent multiplication 的准确转置是
$\exp(\beta_0\partial_X\partial_Y)P$；
(T10)则是对测试乘 $\exp(b_0 c_1\otimes c_1)$。
(T9)支付真实尺度，但单凭尺度和范数并没有支付这两个
算子之间的 Fourier/Weil 交织。尤其不能把(T12)当作
R1064§11的单变量完整 Maass 测度已经有界。

还可保所有旧项而检查(T13)。因为
$D_G^r\phi=p^r\phi D_G^r$，由(K8)有
$$
 D_G^rg_\pm(Q)
   =pD_G^rf_\pm(Q)-p^{r+1}(D_G^r\psi f_\pm)(0)
       \qquad(Q\in G[p]).
 \tag{T14}
$$
所以(T13)在每一对实际除点的值均保两个旧项及其交叉项。
没有将 $r=0$ 的(K13)错误扩成任意导数无旧项的等式。
原 $T_{\rm g}$、两个三挠词和每个 Miller 字若另作运输，
仍须在(T14)的同一来源内逐项进行。

## 11. 原完整 Hall 临界 germ 的双 Katz 测试

本节返回的是 R1063(I17)已经支付的原 whole 列
$\mathcal B_r(j)$，不是单个 Weyl 字。
其原实际外权为
$$
 \Lambda^{(r)}_{1;i,t}(j)=
 b_{1,i}^{\rm orig}B_i\,
 \nu_r(\mathfrak a_{i,t})^{-1}
 \mathfrak j_{h_i}(j;y_i)\mathfrak j_t(j;y_{i,t}).
 \tag{T15}
$$
这包括十八核、full2/full9、先 $Q_\tau/e_A^-$ 后 sign、
所有原 projector/紧商测度和 Artin/Cor。
非紧 ideal 代表必须先按 R1063(I12d)将两个 Norm/Hodge
因子完整抵消，才回到(T15)。
以下使用 I16--I17 的确切 whole seesaw 等式；
不在其前对任一单图或未积分的 $h_\infty$ 核套 rank-one 分解。

### 11.1 同一原两 Hall 轨道上的解析测试

把 I16--I17 用(T7)全改到 $E_0$。
在负、正两个独立 Hall 轨道选定实际参考点 $Q_*,R_*$，写
$$
 A_{-,Q}=102Z_Q,\qquad A_{+,R}=34Z_R,\qquad
 U_*=\rho_A L_-L_+ A_{-,Q_*}A_{+,R_*}.
$$
所有 $A_{-,Q}/A_{-,Q_*}$、$A_{+,R}/A_{+,R_*}$ 及 $U_*$
都是原 I17/G12 所付的单位。特别不单独插值非单位 $A_{\pm,*}$。
仍取同一共同 Teich/深主单位权盘 $j=-2+p^e u$；
所有根单位按原合法正整数子列固定。

记
$$
 \begin{aligned}
 a_Q(j)&=A_{-,Q_*}^{-2}
    \left(\frac{A_{-,Q}}{A_{-,Q_*}}\right)^{[-2]}(j)
              \mathcal F_{102,Q}(j),\\
 b_R(j)&=
   \exp\!\left((j+2)\log\frac{A_{+,R}}{A_{+,R_*}}\right)
              \mathcal F_{34,R}(j+2),\\
 \mathscr E_-(j)&=\frac1d\sum_{Q\in\mathcal O_-}
                          a_Q(j)(\mathbf e_Q-1),\\
 \mathscr E_+(j)&=\frac1d\sum_{R\in\mathcal O_+}
                          b_R(j)(\mathbf e_R-1).
 \end{aligned}
 \tag{T16}
$$
其中 $\mathcal F$ 正是 R1062(G4)--(G8)，不是新选的 primitive。
原 R716 小矩形代表中的 $\chi_r$ 相位，
按 R1063(H14)--(H16)与 theta 准周期相消后才写成
(T16)的实际对称 lift；$\mathscr C_{102,T}$、
$\mathscr C_{34,T_+}$ 仍为那两个真实 wild 中心单位。
负 Haar 向量是正向量在原双线性 Haar 配对中的准确对偶。
没有任选相位或将两轨道改成相关单和。

有限个除点和完整 $\mathcal F$ 给(T16)在
$F\widehat\otimes\mathscr A$ 中的 Banach 值解析函数。
若需要缩小共同权盘，按 G12 对全部字同时缩小。
在基点，
$$
 \boxed{\quad
 \mathscr E_-(-2)=\mathscr E_Q^- \text{ of (K18)},\qquad
 \mathscr E_+(-2)=\mathscr E_{Q_+}\text{ of (K16)} .
 \quad} \tag{T17}
$$
因为 $A_*^{-2}(A_Q/A_*)^{-2}=A_Q^{-2}$、
$\mathcal F_{34,R}(0)=1$。
此处的 $-1$ 常数项继续保留；负质量恰为0由(K15)支付，
正质量不省。

### 11.2 全权、period、Haar 和模型费用的同一恒等式

令
$$
 K_0=
 \frac{d\,c_0^{(0)}\Omega_A^3
       \mathscr C_{102,T}\mathscr C_{34,T_+}}
      {p^4\rho_A^2L_-^2},\qquad
 U_*^{[0]}(j+2)=\exp((j+2)\log U_*).
 \tag{T18}
$$
它们使用(T7)的 $E_0$ frame。
$K_0$ 确实与 $j$ 无关：I17中全部随权项已是
$U_*^{[-2]}(j)$、两个 $A/A_*$ 比及 $\mathcal F$；
(T15)的原 tensor cocycle 正是 I12c--I17支付这些项的
实际返回，不能再额外删去或重计一次。
其他未经 I12d 支付的附加外权不属于本结论。

直接将(K13)代入该同一 I17，得到
$$
 \boxed{
 \mathcal B_r(j)=K_0\,U_*^{[0]}(j+2)\,
   \boldsymbol\mu_F\bigl(
             \mathscr E_-(j)\otimes\mathscr E_+(j)\bigr).
 }
 \tag{T19}
$$
验证系数时，I17的两个 $d^{-1/2}$ Hall 和各变成
$\sqrt d\,\mathscr C_\pm/p$ 倍的(K10)测试。
负测试的定义另外提出 $A_{-,Q_*}^{-2}$，所以需乘回
$A_{-,Q_*}^2$。
再用
$U_*=\rho_A L_-L_+ A_{-,Q_*}A_{+,R_*}$，
恰将原
$(L_+A_{+,R_*})^2U_*^{[-2]}(j)A_{-,Q_*}^2$
化为
$(\rho_A^2L_-^2)^{-1}U_*^{[0]}(j+2)$。
这逐项给出(T18)，没有丢一次 $d$、$p^2$ 或负 $\delta$。

$\Omega_A$ 与 $U_*$ 可以是原 $\mathbf C_p$ period 数据。
(T16)的有限代数测试先在 $F$ 中定义；这些外部 period
随后按原 I17乘回，不将它们虚称为有限域元素。
式(T19)也没有给一份新 scalar ST descent。

基点是修正模型后(K20)的同一个值。
完整斜率则是
$$
 \boxed{
 \begin{aligned}
 \mathcal B_r'(-2)=K_0\Bigl\{
 &\boldsymbol\mu_F\bigl(
 \mathscr E_-'(-2)\otimes\mathscr E_+(-2)
  +\mathscr E_-(-2)\otimes\mathscr E_+'(-2)\bigr)\\
 &+(\log U_*)\,\boldsymbol\mu_F\bigl(
          \mathscr E_-(-2)\otimes\mathscr E_+(-2)\bigr)\Bigr\}.
 \end{aligned}}
 \tag{T20}
$$
明确地，
$$
 \begin{aligned}
 a_Q'(-2)&=a_Q(-2)
  \left(\log\frac{A_{-,Q}}{A_{-,Q_*}}
       +\frac{\mathcal F_{102,Q}'(-2)}
                    {\mathcal F_{102,Q}(-2)}\right),\\
 b_R'(-2)&=\log\frac{A_{+,R}}{A_{+,R_*}}
                  +\mathcal F_{34,R}'(0).
 \end{aligned}
$$
分母 $\mathcal F_{102,Q}(-2)$ 是 G8 已付的单位。
$\log U_*$ 及单位比的 log 没有被假定具有非负估值。
按 I20 写回原 ordered source，(T20)准确等于
$\sum_{i,t}(\Lambda_{1;i,t}^{(r)\prime}M_{A_{i,t}}
+\Lambda_{1;i,t}^{(r)}M_{A_{i,t}}')$ 在 $j=-2$ 的值。
它保全部 $\lambda/\lambda'$、两个原 sign 和 Artin/Cor，
不由端点0抹去任一导数项。

## 12. 后继交织的确切范围

(T19)--(T20)不要求原单变量
$\exp(CL)^*\nu$ 已经有界；它们在同一个已构造的双 Katz
对偶上，以有限而完整的实际除点测试返回原整个临界 germ。
这比只返回(K20)的值多保两侧导数及外权导数，但仍没有
证明该指定测试不在泛函的核中。

(T10)--(T14)则给一份确切的整 Gaussian dual twist，其常数
$612\omega/\kappa_A$ 和两模型尺度全部已付。
若要将它用于原 R1060 coherent multiplication，
下一步必须用实际 Fourier/Weil/Miller 次序证明相应交织；
不能仅因两个 Gaussian 都是单位而认同它们。
两份 Katz 测度的整性、支撑于单位以及(T12)的等距性，
也没有单独支付(K29)的
$v_p\mu_+(c_1^{p+1})=2$，更未支付其对无穷多个 $p$ 成立。

本附节是纸笔恒等式及完整既有来源的运输，无新增数学执行。

## 13. 原 p² 新字的拉回框架与整单位

本节继续(K1)–(K3)的同一个严格 LT 坐标、完整
$T_{\rm g}$ 及 $E_0$ 模型。它处理
[R1054](R1054-original-p-square-depleted-source-and-exact-conductor-blocks.md)
(58)–(65)的真正 $p^2$ Weyl 字；
不是对(K8)已经构造的 $\mu_\pm$ 换一个名字。
新结论是：将这些字放回**实际 $[p]$ 拉回框架**后，
每个非旧字本身已是整的 $\psi=0$ 级数，不必再乘一个 $p$。
原整体来源的 $p^{-2}$ Haar、覆盖变量及全部外权仍保留。

置
$$
 \mathscr T(v)=T_{\rm g}(w(v)),\qquad h(v)=v/\mathscr T(v),
 \qquad P(v)=[p]_G(v)=pv-v^{p^2}.
 \tag{W1}
$$
对 $N=34,102$，令 $\mathcal L_N=\mathcal O_E(NO)$，
$s_N^0$ 是其原 canonical section；在解析 sigma 框架中为
$\sigma(z)^N$。形式邻域上的整不消失框架为
$$
 e_N=h(v)^{-N}s_N^0,\qquad
 s_N=\sigma^N R_N=f_N(v)e_N,\qquad f_N=h^NR_N .
 \tag{W2}
$$
$h/v$ 为整单位，所以(W2)确是整线丛的框架，而不是把 sigma
级数代入边界挠点的定义。这里负侧仍是原两条三挠字完整相加后的
$R_-$；其 $\delta$ 拉回和中心不改变。

[R1061](R1061-original-p-square-antilinear-gluing-and-full-theta-descent.md)
(27)、(30)已给原 division function
$r_p=\sigma(pz)/\sigma(z)^{p^2}$。运输到同一严格坐标后准确有
$$
 r_p(v)=u_p(v)\frac{P(v)}{v^{p^2}},
 \qquad u_p(v)\in\mathcal O[[v]]^\times,\quad u_p(0)=1.
 \tag{W3}
$$
坐标运输的首导数为1，故保留这个常数。特别
$v^{p^2-1}r_p=u_p(v)(p-v^{p^2-1})$；
原首 $p$ 没有被删除，符号也与(K2)相同。

在原刚性化
$[p]^*\mathcal L_N\simeq\mathcal L_{Np^2}$ 下，
$[p]^*s_N^0=r_p^N s_{Np^2}^0$。因此(W2)给出全部框架差：
$$
 \boxed{
 [p]^*e_N=B_{N,p}(v)e_{Np^2},\qquad
 B_{N,p}(v)
 =\left(r_p(v)\frac{h(v)^{p^2}}{h(P(v))}\right)^N
 =\left(u_p(v)\frac{\mathscr T(P(v))}
                         {\mathscr T(v)^{p^2}}\right)^N
 \in1+v\mathcal O[[v]] .
 }
 \tag{W4}
$$
分子、分母中的同一个 $P(v)$ 在(W3)代入后才相消。
这同时证明 $B_{N,p}(0)=1$；没有另选一个根或重归一首项。
特别，degree-$Np^2$ 的标准 $T_{\rm g}$ 框架与原 $[p]$ 拉回框架
相差的是(W4)这个明确整单位，不能预先认成同一个。

## 14. 每个原 Miller lift 的整性与准确中心

先固定一个原实际有限/CM 字，尚未作无穷圆周投影。
在一个有限扩域 $F/L$ 中放入全部实际 $p^2$ 挠点、原 Miller
根与非 $p$ 系数；记其整数环为 $\mathcal O_F$。
取原 theta lift 的 $T\in E[p^2]$，置 $Q=[p]T$。
定义 $A_{N,T}$ 与 $F_{N,T}^{\rm K}$ 为同一个实际 section 的
两个系数：
$$
 \mathsf W_T([p]^*s_N)
 =A_{N,T}(v)[p]^*e_N
 =F_{N,T}^{\rm K}(v)e_{Np^2},\qquad
 A_{N,T}=B_{N,p}^{-1}F_{N,T}^{\rm K}.
 \tag{W5}
$$
所有 $\mathsf W_T$ 都沿 R1054(56)、(59)的实际 lift，不自行换相位。

存在由该 lift 唯一确定的 multiplier $m_{N,T}(v)$，使
$$
 A_{N,T}(v)=m_{N,T}(v)\,f_N\bigl(P(v)\oplus_G v_Q\bigr).
 \tag{W6}
$$
下面证明**原** $m_{N,T}$ 是整单位，而不只证明有另一个整 lift。

在好整模型上，$\mathcal M=[p]^*\mathcal L_N$ 的极化核包含
$E[p^2]$：其极化映射为 $[Np^2]$。因此
$\tau_T^*\mathcal M\otimes\mathcal M^{-1}$ 在相对 Picard 群中为0。
由于椭圆 scheme 有零截面且其全局函数来自底环，该线丛来自
$\operatorname{Spec}\mathcal O_F$；后者的 Picard 群为0。
故存在一个整 theta lift。这个论证是相对 Picard 精确列的直接
应用，参见 [Stacks 44.4.2–44.4.3](https://stacks.math.columbia.edu/tag/0B9K)；
对本处也可用 theta-group 的 $\mathbf G_m$-torsor 描述。
在(W2)及其实际拉回的整框架中，该整 lift 的 multiplier 必属
$\mathcal O_F[[v]]^\times$。

另一方面，原 lift 和这个整 lift 在 generic fibre 的比为
$F^\times$ 中的一个常数。R1061(25)、(28)、(31)给原常数
$b_{N,T}=\epsilon_Tc_Q^N$，其中 $\epsilon_T$ 是实际中心分量；
对 $Q\ne O$，
$$
 \boxed{
 m_{N,T}(0)
  =\frac{b_{N,T}}{h(v_Q)^N}
  =\epsilon_T
       \left(\frac{c_Q\,\mathscr T(v_Q)}{v_Q}\right)^N
  =\mathscr C_{N,T}\in\mathcal O_F^\times .
 }
 \tag{W7}
$$
这里 $v_p(c_Q)=v_p(v_Q)=1/(p^2-1)$，且
$\mathscr T(v_Q)$ 为单位；这正是 R1063(H16)保留的原 Hall 中心。
一个整 lift 的对应首值也是单位，所以两 lift 的常数比为单位。
原 lift 本身因而整。该证明不改 $\epsilon_T$，也不将
$\mathscr C_{N,T}$ 设为1。

$Q=O$ 时使用原 old stabilizer：R1061(28)的准周期、
half-character 和中心严格相消，整个 $[p]^*H^0(\mathcal L_N)$
被固定。其原拉回线性化在 $[p]^*e_N$ 上就是形式群平移。
例如可用全局 section $\sigma^Nx^{N/2}$ 核定此线性化；
其在 $e_N$ 中的系数为整单位，故不可能遗留一个非平凡框架
multiplier。于是 $m_{N,T}=1$ 对这些原 old lifts 成立。

由(W6)、(K3)和完整形式群加法，
$$
 \boxed{
 m_{N,T}\in\mathcal O_F[[v]]^\times,\qquad
 A_{N,T}\in\mathcal O_F[[v]],\qquad
 A_{N,0}=\phi f_N .
 }
 \tag{W8}
$$
$v_Q$ 在极大理想中，故(W6)的有常数项复合在
$\mathcal O_F[[v]]$ 内收敛。这没有使用 sigma 在边界的原点
展开，也没有借原最大阶点的半径界给新邻点。

## 15. 完整核的真实 character 与无额外 p 的 Katz 测度

用 R1054(56)的原定义
$$
 W_\pm(a,b)f(A)=
 \zeta^{\,\pm b(A-a/2)}f(A-a),\qquad
 \zeta=\psi_p(1/p^2),\quad \zeta_p=\zeta^p .
 \tag{W9}
$$
记 $\beta_\pm$ 为 R1061(7)的实际点标记；
包括负侧 $\delta$、正侧反 CM 方向及全部 CRT 中心。
对 $S=\beta_\pm(pr,ps)\in E[p]$ 和
$T=\beta_\pm(a,b)\in E[p^2]$，逐项相乘(W9)给
$$
 W_\pm(pr,ps)W_\pm(a,b)
 =\zeta_p^{\,\pm(as-br)}
       W_\pm(a,b)W_\pm(pr,ps).
$$
因为 $W_\pm(pr,ps)$ 在原 old 输入上恒等，且在拉回框架中是
普通核平移，得到
$$
 \boxed{
 A_{\pm,a,b}(v\oplus_G v_S)
   =\chi^\pm_{a,b}(r,s)\,A_{\pm,a,b}(v),\qquad
 \chi^\pm_{a,b}(r,s)=\zeta_p^{\,\pm(as-br)} .
 }
 \tag{W10}
$$
这里 $A_{-,a,b}$ 用 $N=102$，$A_{+,a,b}$ 用 $N=34$。
实际 $\beta_\pm$ 已含极化和 $N$ 的归一；不得在(W10)再额外
乘一次 $N$。若对原 $h$ 字先作 Egorov 运输，就对
$(r,s),(a,b)$ 和 $\beta_\pm$ 一起作同一个真实运输。

当 $(a,b)\not\equiv(0,0)\pmod p$ 时，(W10)是完整
$\mathbf F_p^2$ 上的非平凡 character；这恰等价于
$Q=[p]T\ne O$。使用(K5)的整个核，遂有
$$
 \boxed{
 \psi A_{N,T}=0\quad(Q\ne O),\qquad
 \psi A_{N,0}=f_N .
 }
 \tag{W11}
$$
本式的裸核迹作用于(W5)的 **$A_{N,T}$**。
在标准 degree-$Np^2$ 框架中，准确的等式是
$$
 \frac1{p^2}\sum_{S\in E[p]}
 \frac{B_{N,p}(v)}{B_{N,p}(v\oplus v_S)}
              F_{N,T}^{\rm K}(v\oplus v_S)=0
 \qquad(Q\ne O).
 \tag{W12}
$$
不能从(W12)删除 $B$，再断言裸 $\psi F_{N,T}^{\rm K}=0$。
这就是全 Weyl 有权迹与裸形式群迹之间需要支付的框架差。

令 $\mathscr C=C^0_{\rm Gal}(\mathbb T,\mathcal O_{\mathbf C_p})$
如(K9)。将 Berger Theorem A 用于完整平坦
$\mathcal O$-代数 $\mathcal O_F$，由(W8)、(W11)得到唯一
$$
 \boxed{
 \begin{gathered}
 \boldsymbol\mu_{N,T}\in
       \operatorname{Hom}_{\mathcal O}(\mathscr C,\mathcal O_F),
 \quad
 \operatorname{supp}\boldsymbol\mu_{N,T}
       \subset\mathbb T^\times,\qquad
 \|\boldsymbol\mu_{N,T}\|\le1,\\
 \mathcal K^*\boldsymbol\mu_{N,T}=A_{N,T},\qquad
 \boldsymbol\mu_{N,T}(c_k)=[v^k]A_{N,T}
       \quad(Q\ne O).
 \end{gathered}
 }
 \tag{W13}
$$
这里的范数沿(T1)–(T2)的原整格 gauge；系数扩张按固定 $F$ 中的乘法返回 $\mathcal O_F$，不把它改成普通 $\mathbf C_p$ 测度的点值范数。$\mathcal O_F$ 对 $\mathcal O$ 平坦且 $p$-进完备分离，满足该定理对 $S$ 的全部条件。

这里没有乘 $p$。理由是这些实际新字已经整且 $\psi=0$，
其全部后继 $\psi$ 迭代自动整；不是改善(K8)对任意整函数所需的
分母界。旧字 $\phi f_N$ 不在这个结论内。

对本题首项为1的实际 $f_+,f_-$，这些新测度还确实非零且范数为1。
模 $\mathcal O_F$ 的极大理想，$v_Q$ 变成0、$P(v)$ 变成
$-v^q$，所以
$\overline A_{N,T}=\overline m_{N,T}\,\overline f_N(-v^q)\ne0$。
其首剩余次数在正侧为 $6q$、负侧为 $4q$；对应
$\boldsymbol\mu_{N,T}(c_{6q})$ 或
$\boldsymbol\mu_{N,T}(c_{4q})$ 为单位。
这是高阶 universal-character 系数 $c_k$ 的结论，
不把 $k\ge q$ 的 $c_k$ 改成 $c_1^k/k!$，
也不据此断言(K29)的低阶原 canonical 矩为单位。


(W10)还支付了这份测度的准确有限特征。
用(K11)的完整系数扩张 $\mathbf e_S$，对任意 $c\in\mathscr C$ 有
$$
 (\boldsymbol\mu_{N,T})_F
        \bigl((\mathbf e_S-\chi_{T}(S))\,c\bigr)=0.
 \tag{W14}
$$
证明：Katz 变换把乘 $\mathbf e_S$ 变成
$A(v)\mapsto A(v\oplus v_S)$，再用(W10)及原 Katz 单射。
所有非基域挠点与中心同时在完成的系数扩张中运输。
这里不把一个未作系数运输的非等变函数塞进
$C^0_{\rm Gal}$，也不略去(W10)的相反两条 character。

## 16. 与原 Hall 测度的准确关系

$\boldsymbol\mu_{N,T}$ 的质量给同一个实际 Miller 字的原值：
$$
 \boxed{
 \boldsymbol\mu_{N,T}(1)
 =b_{N,T}R_N(Q)
 =\mathscr C_{N,T}f_N(v_Q)
 =\frac{\mathscr C_{N,T}}p\,
           \mu_{N,F}(\mathbf e_Q-1).
 }
 \tag{W15}
$$
最后一项的 $\mu_N$ 是(K8)、(K10)以
$g_N=p(1-\phi\psi)f_N$ 构造的**旧测度**。
新 $\boldsymbol\mu_{N,T}$ 则由真实 $p^2$ Weyl 字 $A_{N,T}$ 构造。
(W15)只给它们在这个实际有限读者上的关系，不将两份测度相认；
右边的除 $p$ 已由(K13)的完整函数等式支付。

取 R1063 原 tame-zero Hall 的共同 lifts $T_\zeta$，
$[p]T_\zeta=\zeta Q$、$\zeta\in\mu_d$。
原 $\mathscr C_{N,T_\zeta}$ 及所有 wild 相位仍是指定的那些。
于是原正 Hall 与负二有限 Hall 精确成为
$$
 \begin{aligned}
 \mathcal H_+^0
  &=\frac1d\sum_{\zeta\in\mu_d}
             \boldsymbol\mu_{34,T_\zeta}(1),\\
 \mathcal H_-^{[-2]}
  &=\frac1d\sum_{\zeta\in\mu_d}
       \frac{\mathcal F_{102,\zeta Q}(-2)}
                  {(102Z_{\zeta Q})^2}
             \boldsymbol\mu_{102,T_\zeta}(1).
 \end{aligned}
 \tag{W16}
$$
这与(K17)、(K19)逐项一致。实际 $a_Q^-=
(102Z_Q)^{-2}\mathcal F_{102,Q}(-2)$ 是一个有限的已付系数；
没有从单位支撑免费推出一个新的全局 inverse-Bol 算子。
两条 Hall 仍独立，R1063 的 $d/p^2$ 成对 Haar 不改变。
换到原 $E_{17}$ 来源时仍用(K20a)–(K20b)：
$c_0^{(0)}=\vartheta^{-10}c_0$、$L_\pm=\vartheta\ell_\pm$，
endpoint 相对 $c_0/\ell_-^2$ 的 $17^{-2}$ 必须保留。

## 17. 整个原 p² 输入的 old/new 分解

在两个真实拉回框架上记 $\phi f_\pm(v_\pm)=f_\pm(P(v_\pm))$，
并始终按 R1054(59)在 $\mathbf Z/p^2\mathbf Z$ 中共同选 lift。
其原有限矩阵的全部返回为
$$
 \begin{aligned}
 \mathcal K_p^{\rm pb}
 &=\frac1{p^2}\left[
       \phi f_-\otimes\phi f_+
       +\sum_{v\in\mathbf F_p^2\setminus\{0\}}
          A_{-,\widetilde v}\otimes A_{+,M\widetilde v}
                    \right],\\
 \mathcal A_p^{\rm pb}
 &=-\phi f_-\otimes\phi f_++\mathcal K_p^{\rm pb}\\
 &=\left(p^{-2}-1\right)\phi f_-\otimes\phi f_+
       +\frac1{p^2}
        \sum_{v\in\mathbf F_p^2\setminus\{0\}}
          A_{-,\widetilde v}\otimes A_{+,M\widetilde v}.
 \end{aligned}
 \tag{W17}
$$
$M$ 可逆，故最后每一项的两边都是真正新字。
零字、旧项负号和所有 $p^2-1$ 个非零字都在(W17)中。
这不借某个整体旧项的平坦极限为零而提前删掉它。

令 $\Pi_0=\phi\psi$、$\Pi_\times=1-\phi\psi$，
分别作用于两个拉回框架中的标量级数。由(W11)，
$$
 \begin{aligned}
 (\Pi_0\otimes\Pi_0)\mathcal K_p^{\rm pb}
       &=p^{-2}\phi f_-\otimes\phi f_+,\\
 (\Pi_0\otimes\Pi_\times)\mathcal K_p^{\rm pb}
       &=(\Pi_\times\otimes\Pi_0)\mathcal K_p^{\rm pb}=0,\\
 (\Pi_\times\otimes\Pi_\times)\mathcal K_p^{\rm pb}
       &=\frac1{p^2}\sum_{v\ne0}
           A_{-,\widetilde v}\otimes A_{+,M\widetilde v}.
 \end{aligned}
 \tag{W18}
$$
这里的 $\Pi_0$ 在当前有限 Heisenberg 模上就是完整 old
projector，因而是对真实输入的分解，不是给原 canonical
条件增加一个可自由操作的测试。

特别，原新部分乘回其**已有** Haar 分母 $p^2$ 后，准确是整
Galois–Katz 双对偶
$$
 \boxed{
 \boldsymbol\nu_{\rm new}
   =\sum_{v\in\mathbf F_p^2\setminus\{0\}}
       \boldsymbol\mu_{102,\widetilde v}
          \widehat\otimes
       \boldsymbol\mu_{34,M\widetilde v},
 \quad \|\boldsymbol\nu_{\rm new}\|\le1,\quad
 \operatorname{supp}\boldsymbol\nu_{\rm new}
       \subset\mathbb T^\times\times\mathbb T^\times .
 }
 \tag{W19}
$$
其 Katz 变换是 $p^2$ 乘(W18)最后一行。
本式用两份完成的对偶及全部系数运输；不声称是原单条
$\mathbf Z_p$ Amice 测度的提升。

## 18. 全有限 jet、原连接与物理 p 幂的返回

为把(W13)真正接回原有限 reader，需要保原 sigma/完成框架。
在同一个形式参数和不变微分 $dz$ 下置
$$
 a_N(v)=\left(\frac{h(v)}{\sigma(z(v))}\right)^N
       =\left(\frac v{z(v)}\right)^N
                    E_{\rm c}(z(v))^{-N},\qquad
 \alpha_{N,p}(v)=a_N(P(v)),\qquad \alpha_{N,p}(0)=1 .
 \tag{W20}
$$
这里 $E_{\rm c}$ 是原**完整** completion；等式来自
$\mathscr T=\exp(F_{\rm c}-F)$，不只是其首
$\exp(c_\sigma z^{p+1})$。本节只在有限 jet 中使用(W20)，
不另声称整个 $a_N$ 在单位盘有界。

令 $F_{N,T}^{\sigma}(z)$ 是 R1061(28)的完整解析 section 函数，
仍用覆盖参数 $z$。由框架的定义严格有
$$
 A_{N,T}(v)=\alpha_{N,p}(v)F_{N,T}^{\sigma}(z(v)),
 \qquad
 \nabla_{N,p}=\alpha_{N,p}D\alpha_{N,p}^{-1},
 \quad D=d/dz .
 \tag{W21}
$$
因此对每个非负整数 $m$，
$$
 \boxed{
 \begin{aligned}
 p^m b_{N,T}\,\mathcal A_{N,m}(Q)
   &=D^mF_{N,T}^{\sigma}(0)
     =(\nabla_{N,p}^{\,m}A_{N,T})(0)\\
   &=\sum_{j=0}^{m}\binom mj
        D^{m-j}\!\left(\alpha_{N,p}^{-1}\right)(0)
               \boldsymbol\mu_{N,T}(c_1^j).
 \end{aligned}
 }
 \tag{W22}
$$
$\mathcal A_{N,m}$ 是 R1061(C2)、(C5)的同一个完整多项式：
$\mathcal A_{N,0}=R_N$，
$\mathcal A_{N,m+1}=(\mathcal D+NZ)\mathcal A_{N,m}$。
第一行保真实 $Z_Q$、$c_Q$ 和实际 lift，不只保其首估值。

(W22)中没有 $j!$：原 universal character 在不变微分下满足
$D^j\mathbf t_\xi(0)=c_1(\xi)^j$。
若改读 Taylor 系数，则在整个等式外再除原 $m!$；
若返回物理底层导数，则乘原 $p^{-m}$。
两个 coherent 槽因而仍有 $p^{-r-s}$，这与(W17)的
$p^{-2}$ Haar 是不同费用。
将 $D$ 换成裸 $\partial_v$ 会引入不变微分的系数，
本节始终没有作这个替换。

(W22)是每一阶原 Maass 有限转置可以直接消费的等式。
需代回 R1060 的全部 $c_i(n)$、$\rho_i,\Omega_i,\kappa_i$
和有限三角系数；不能只留下 $j=m$。
它也不把原负二 endpoint 改成
$\boldsymbol\mu_{N,T}(c_1^{-2})$：
(W20)的连接、原 Maass 修正和外权导数仍须完整运输。
有限负二 Hall 已由(W16)准确给出。

## 19. 原全来源与适用范围

(W17)先对原有限 Schwartz 模成立，再经
R1054(61)–(65)的整个 $\mathfrak T_{\rm orig}$ 返回实际 theta 来源。
对每一个实际 $h$ 字，先运输其 Heisenberg 参数、线丛及整框架，
再使用(W4)–(W22)。原 $p$-primary old projector是全部核
Weyl 的平均；实际 Egorov 运输置换这些核元素，故这个 finite
old/new 分解与已经指定的有限 $h$ 运输相容。
非 $p$ Schwartz、full2/full9、原两条三挠字和其 $\kappa^p$
角色、Artin/Cor 均留在同一线性返回内。

随后仍作原整个无穷圆周投影。上述逐字的整线丛证明不把
圆周投影后的 $W^2F(ZW)$ 免费视作固定 $E\times E$ 上的
全局 section；也不从各独立 rank-one 级数的整性重新定义
原 whole 测度。R1060/R1059 的实际外权始终是
$\Lambda_i(-2),\Lambda_i'(-2)$，连同真实 period 及模型倍率；
不能在第 $n$ 槽将它们替成另一份 $\lambda_i(n)$。

本节由原 source 支付的是：

- 原 $[p]$ 框架差(W4)为有明确常数的整单位；
- 全部非旧 $p^2$ 字在该框架中为整的 $\psi=0$ 对象，
  其准确 kernel characters 和中心由(W7)、(W10)保留；
- 原新双来源确有(W19)这份整 Katz 双对偶，并经(W22)返回
  同一个原有限 jet 及全部物理覆盖费用。

这不新增 canonical 中央零，也没有由 $\psi=0$ 或整范数推出
(K29)的原首矩是单位。它提供实际新 $p^2$ 来源的整单位测度，
而非把(K8)的人工 depletion 或原 flat 完成移名。

## 20. 唯一 primitive 对偶剩余类及其原 h 运输

(W14)可进一步确定每份新测度的整个有限支撑。
继续固定包含全部 $E[p]$ 标记和 $\mu_p$ 的 $F$，
在有理化的完成系数代数
$$
 \mathscr C_{F,\mathbf Q}
 =(\mathcal O_F\widehat\otimes_{\mathcal O}\mathscr C)[1/p]
$$
中工作。对 $\xi\in\mathbb T/p\mathbb T$，
以原 Cartier 配对写 $\langle\xi,S\rangle\in\mu_p$，置
$$
 \mathbf p_\xi
   =\frac1{p^2}\sum_{S\in G[p]}
            \langle\xi,S\rangle^{-1}\mathbf e_S .
 \tag{W23}
$$
这是一个**有限** $p^2$ 项和。由
$\mathbf e_{S+R}=\mathbf e_S\mathbf e_R$ 及完美 Cartier 配对，
$\mathbf p_\xi$ 两两正交、和为1。
在由全部 $\mathbf e_S$ 生成的有限 $F$-代数上，
它们准确是 $\mathbb T/p\mathbb T$ 各剩余类的 indicator。
其证明只用有限 Fourier 正交：对任意 $\xi'$，
(W23)取值为 $\delta_{\xi,\xi'}$，且这些 $p^2$ 个剩余类
全由 Tate 模实现。因此该有限代数就是 $F^{\,p^2}$。

不能因为 indicator 的点值为0、1，就把(W23)在原整完成
tensor 格中的 $p^{-2}$ 系数删掉。以下先在
$\mathscr C_{F,\mathbf Q}$ 证明等式，再回到已经独立构造的
整测度；不以(W23)重新制造一份“整测度”。

令 $\xi_T$ 为由(W10)唯一确定的剩余类：
$\langle\xi_T,S\rangle=\chi_T(S)$。
对每个 $c\in\mathscr C_{F,\mathbf Q}$，
(W14)逐项代入(W23)准确给
$$
 \boxed{
 (\boldsymbol\mu_{N,T})_F(\mathbf p_\xi c)
  =\delta_{\xi,\xi_T}
           (\boldsymbol\mu_{N,T})_F(c).
 }
 \tag{W24}
$$
这就是在完成系数的 Galois-dual 意义下，
$\boldsymbol\mu_{N,T}$ 支撑于唯一 coset
$\xi_T+p\mathbb T$ 的确切陈述。
$T$ 非旧当且仅当 $\xi_T\ne0$，所以该 coset 全在
$\mathbb T^\times$ 中。
这里没有将整个 $\mathscr C_{F,\mathbf Q}$ 认成任意
$\mathbf C_p$ 值连续函数的空间。
(W24)对于实际整输入的取值没有增加分母：
它等于原已经整的 $\boldsymbol\mu_{N,T}(c)$ 或0。
这不声称 $\mathbf p_\xi$ 在整个整 tensor 格上算子范数为1。

还可把成对图写出，避免只称“两份单位支撑”。
取与原 $\beta_\pm$ 对偶的坐标，使
$$
 \langle(x,y),\beta_\pm(pr,ps)\rangle
       =\zeta_p^{xr+ys},\qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$
由(W10)，对原参数 $v=(a,b)^T$，
负侧剩余类为 $\xi_-=-Jv=(b,-a)^T$，
正侧 $Mv$ 的剩余类为 $\xi_+=JMv$。
于是(W19)的全部实际 paired cosets 为
$$
 \boxed{
 \xi_+=-M^{-T}\xi_-,\qquad
 \xi_-\in\mathbf F_p^2\setminus\{0\}.
 }
 \tag{W25}
$$
这是因为 $\det M=1$ 且 $JMJ=-M^{-T}$。
两对偶坐标分别由原正负 theta 结构确定；
(W25)不把两个物理 Weil pairings 同向认同。

在一个原实际有限 $h$ 字下，若其 Egorov 矩阵为
$g_\pm$，所有参数、中心和 theta 标记同时按原作用运输。
对应对偶剩余坐标为
$\xi_\pm\mapsto g_\pm^{-T}\xi_\pm$；
所以新图严格为
$$
 -g_+^{-T}M^{-T}g_-^T
       =-(g_+Mg_-^{-1})^{-T}.
 \tag{W26}
$$
原非 $p$ 操作作用在 multiplicity/有限来源上，
全中心仍乘原标量；既不删除该相位，也不改变上述
kernel character 的判别。完整 $h$ 和 Artin/Cor 应将这些
实际图及其测度一起线性相加，随后才作指定的无穷投影和
$\Lambda,\Lambda'$ 读者。原 $p^{-2}$ Haar 仍如(W17)；
(W24)不再向每一份已经处于该 component 的测度额外收一次
$p^{-2}$。这把后继双 Katz 测试的有限 carrier 固定为原真实图，
没有从该支撑关系推出任何原低矩或 canonical 非零。
