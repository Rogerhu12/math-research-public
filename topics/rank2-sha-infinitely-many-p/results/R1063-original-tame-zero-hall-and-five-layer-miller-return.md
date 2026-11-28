# R1063 — 原 tame-zero Hall 投影与完整 Miller 负二读数的前五层

日期：2026-11-28。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：本篇支付同一实际 Hall 角色、Miller 中心、严格 LT 坐标和负二连接高项的五层返回。正源保持原 canonical $S$，负源保持两个三挠 Weyl 词完整相加的 $D_{102}$。这里的 tame-zero 输出是为对准 R716 原 Hall covector 而明确施加的新操作；不声称它已经包含在 R1061(C18) 的未投影来源内。§9现另付整个 non-$p$/$h$/Artin 输出整列、原十八商微分及全外权到两 Hall 来源的准确接合；单图仍不得由单字式替代。**

本篇不证明下面两个首系数中的任何一个在无穷多个 $p$ 上为单位，也不把一个 paired 读数直接命名为原 Iwasawa 值或通常全 Sha 的判据。

## 1. 固定原来源、微分与真实边界坐标

取惰性素数 $p\equiv5\pmod6$、$p>211$，避开原固定来源和有限幅度的坏位。置
$$
 d=p+1,\qquad \Delta=p^2-1,\qquad
 s=d/6,\qquad \eta=1-\frac1{p-1}.
 \tag{H1}
$$
所有估值满足 $v_p(p)=1$。在原共同模型
$E_0:y^2=x^3+1$ 上保不变微分及 $D=d/dz$，
并取 R1061(C7) 的好参数 $w=x^{-1/2}$。
它满足
$$
 Dw=\sqrt{1+w^6},\qquad w=z+\cdots .
$$
正、负实际来源分别为
$$
 S=\sigma^{34}R_S,\quad [z^6]S=1,\qquad
 D_-=\sigma^{102}R_-,\quad [z^4]D_-=1.
 \tag{H2}
$$
$R_S$ 是原完整 canonical 多项式；$R_-$ 是
[原 psi4 来源注](../notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)
(20)--(28) 的两个三挠 Weyl 词经 $\delta$ 拉回后得到的完整多项式。
不保其中一支，也不把它改成一份裸 degree34 来源。
实际 raw 幅度和 coherent 参数中的 $\delta^{-1}$ 按该注§§10--11另保。
本篇的 $D_-$ 只是其中首4项为1的既定规范，未重新选择平方根或 Artin 基。

使用 [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)
(2)--(4) 的严格整坐标 $v=h(w)$，而非 R660 仅按 $\mu_d$ 平均的旧坐标：
$$
 [-p](v)=-pv+v^{p^2},\qquad
 v([\zeta]Q)=\zeta v(Q)\quad(\zeta\in\mu_\Delta).
 \tag{H3}
$$
R663 的逐系数唯一构造同样适用于这个已固定的 $b=1$ 模型。
因 $[-p]$ 的原系数在 $\mathbf Q_p$，构造的每个唯一系数也在
$\mathbf Q_p$；所以该坐标还与原复共轭相容。
由 $\mu_6$ 和整性，
$$
 w(v)/v\in1+v^6\mathcal O[[v^6]],\qquad
 z(v)=v+O(v^{p^2}).
 \tag{H4}
$$
后一个式子是特征零形式式，不声称其全部系数整。
对非零 $Q\in E[p]$，
$$
 v_Q^\Delta=p,\qquad W=v_Q^d,\qquad W^{p-1}=p .
 \tag{H5}
$$
同一个实际 $T_{\rm g}$ 始终按这个坐标完整运输；不得只保其首项。

R660/R663 最初以 $b=17$ 书写。使用本篇共同模型时，先沿既定
$\vartheta^6=17$ 的实际同构运输 sigma、微分、Klein 值和来源，
再按(H3)取严格坐标。两个模型的严格 LT 坐标不被免费认成
$\vartheta$ 倍；下面所有 $\mathcal B$ 都在明写的 $E_0,v$ 中定义。
返回 R716 的 $E_{17}$ 时，仍保
$S_{17}(z)=\vartheta^{-6}S_1(\vartheta z)$ 及相应的真实参数运输。

## 2. 同一个 $Z_Q$ 等于已收敛的 zeta Laurent 函数

令
$$
 \Xi(w)=
 \sum_{j\ge0}\binom{-1/2}{j}\frac{w^{6j-1}}{1-6j}.
 \tag{H6}
$$
这是 [R660](R660-original-torus-coordinate-and-boundary-resonance-ideal.md)
(2) 在 $b=1$ 的原函数。分母估值只按指标对数增长，所以
(H6)在 $0<|w|<1$ 收敛，且 $D\Xi=-x$。
这不是在首挠点代入可能不收敛的 sigma 级数。

取 R1061 的同一有理除点函数
$r_p=\sigma(pz)/\sigma(z)^{p^2}$。
在原点的正式 Laurent 环，
$$
 D\log r_p=p\,\Xi([p]w)-p^2\Xi(w).
 \tag{H7}
$$
各项在开形式盘上为明确的亚纯函数：$\Xi$ 只有原点单极，
$[p](w)$ 是同一整形式群函数，$r_p$ 是同一有理函数。
乘掉它们的有限极除子后，两侧是同盘内收敛的相同级数，
故(H7)在其共同定义域成立；无须借用模曲线上另一个
未付的 ordinary/supersingular 共同延拓。

在 $Q\ne O$ 的局部不变时间 $h$ 中，
$[p](Q+h)=[p]h$。因 $\Xi$ 是奇函数，
$p\Xi([p]h)=h^{-1}+O(h)$ 的常数项为0。
另一方面，$D\log r_p(Q+h)$ 的常数项为
$D^2r_p(Q)/(2Dr_p(Q))$。与 R1061(C1)比较，得精确式
$$
 \boxed{Z_Q=\Xi(w_Q).}
 \tag{H8}
$$
这固定的是原代数 $Z_Q$，没有改变其 quasi-period 或积分常数。

置
$$
 \kappa_0=-\binom{-1/2}{s}\in\mathbf Z_p^\times .
$$
$2s<p$，故该数是单位；其模 $p$ 值恰为 R1061(C6) 的
$pc_\sigma$。在(H6)中，指数 $6j-1=p$ 的项准确为
$\kappa_0w^p/p$。
其余分母不被 $p$ 整除的项，相对该项的估值至少 $\eta$。
分母恰含一次 $p$ 的下一个可能指数是 $7p$，相对估值至少
$6p/\Delta$。若分母含 $p^a$、$a\ge2$，指数至少为
$5p^a$（$a$ 偶）或 $p^a$（$a$ 奇），均给更深的界。
分子二项式整，不降低这些界。

由(H4)，$(w/v)^p-1$ 的次数小于 $6p$ 的各项都被 $p$ 整除，
其余项至少有 $v^{6p}$。因此在非零首挠点上
$$
 \boxed{
 Z_Q=\frac{\kappa_0}{p}v_Q^p(1+\epsilon_Q),\qquad
 v_p(\epsilon_Q)\ge\frac{6p}{\Delta}.
 }
 \tag{H9}
$$
这比只给 $pZ_Q/v_Q^p$ 的剩余类更强，且保同一个原参数。
这里没有把 $\kappa_0$ 在全部精度上替换为 $pc_\sigma$。

## 3. R716 的 physical 角色与本题两侧标记

先锁定加性角色方向。R716 使用
$e_p(a)=\exp(2\pi ia/p)$；R1054 的
$\zeta_p=\psi_p(1/p)$ 则是 $e_p^{-1}$。
写原 R716 标签 $v=x+y\omega$，其
$h(v)=((x+y)/3,51(x-y))$。
由 R716(23)--(25) 的实际 Heisenberg 定义，原点向量准确为
$$
 e_v=W_+\bigl((x+y)/3,\,-51(x-y)\bigr)v_0 .
 \tag{H10}
$$
它的中心号也包括在(H10)中，不只是平移位置相同。

令 $s_0=(1-\omega)^{-1}$，$\Omega_{\rm CM}=\Omega_0s_0$。
R1061 的有限坐标 $u=b/51+\delta a$ 在(H10)变为
$$
 u=-(x-y)+\delta(x+y)/3=-2\overline{s_0v},\qquad
 Nu=4Nv/3 .
 \tag{H11}
$$
其 positive 物理位移准确为
$-\Omega_0\bar u/(2p)=\Omega_{\rm CM}v/p$。
因此原 physical torus 的 $g$ 对应有限矩阵 $M(\bar g)$，
不能把它改成 $M(g)$。

保 R716(3)--(4) 的角色
$$
 \chi_r(v)=
 e_p\!\left(\operatorname{Tr}
          \frac{34r}{2\delta}q_p(v)\right),\qquad
 \chi_r(1+p\delta t)=e_p(34rt).
 \tag{H12}
$$
它在全 Teichmüller 群和 $\mathbf Z_p^\times$ 上平凡。
原 physical 正向量特征是 $\chi_r^{-1}$；
按(H11)改用 $M$ 标签后为正 $\chi_r$、负 $\chi_r^{-1}$。
这是同一角色的坐标返回，不是把原 Hecke twist $\chi_r^2$
换成逆角色后不再返回。

固定 positive 原范数 $Nv_+=r$。
实际反线性图 $\gamma_{102}$ 的范数为3，故其 negative 点
在同一 $\Omega_{\rm CM}$ 标记下满足 $Nv_-=r/3$。
于是 negative charge102 的主单位幅度
$102(r/3)=34r$，恰与(H12)相同；
两个物理方向则按(H11)相反。
R1061(E9)的 paired 中心准确成为
$$
 \sigma_l(\mathfrak b_p)/\mathfrak b_p
 =\zeta_p^{51lNu}=e_p(-68lr)=\chi_r^{-2}(1+p\delta l).
 \tag{H13}
$$
所以原中心并没有下降成一个可随意删除的 tame 单位。

本篇从这里开始明确施加(H12)的 **tame-zero、非平凡 wild
输出投影**。它是对准原 Hall covector 的新操作。
R1061§22的 Norm-fiber covector与本操作须保持其各自完整顺序；
不把其中任一个说成当前未投影 whole 来源已经做过的操作。

## 4. 原 Miller 中心恰由完整 $T_{\rm g}$ 支付 Hall 变化

令 $\widehat H=\mu_d$ 为 norm-one Hall 群，使用
R705(13) 的真正 CRT level lift，并同时固定本题全部原 tame level。
因这些 level 与 $p$ 互素，R1061§21的实际局部域和
totally ramified 除点域允许这个固定；不改变任何 $2,3,17$ 标记。
原 Hall 角色在该群上平凡。

本节须区分三个对象：好参数 $w$、R696 的绝对 Kummer 根
$\mathfrak w_Q$、以及原 Klein 值
$k_Q=e^{-\eta_Qq/2}\sigma(q)$。
沿上述实际 level，R705(14)给 $k_Q,\mathfrak w_Q$ 的准确
Galois 等变，连全部相位。R696(5)、(15)给
$$
 \mathfrak w_Q=\rho_Q/k_Q,\quad
 \rho_Q\in\mu_{6p^2},\qquad
 \frac{\mathfrak w_Q}{h(\mathfrak w_Q)}
   =\zeta\,\frac{G(Q)}{G(hQ)},\quad
 G(Q)=T_{\rm g}(w_Q),\quad h\leftrightarrow\zeta\in\mu_d .
 \tag{H14}
$$
norm-one Hall 固定 $\mu_{p^2}$，原 tame 基固定 $\mu_6$，
所以它固定这里的 $\rho_Q$。由此
$$
 \frac{k_{hQ}}{k_Q}
       =\zeta\,\frac{G(Q)}{G(hQ)} .
 \tag{H15}
$$
这些式子在 $b=1$ 模型上是原除点身份的同构运输；
除点函数、Klein 值和参数须一起运输，不把某个新根认成旧根。

令 $T\in E[p^2]$、$pT=Q$，并保 R1061(E4) 的实际对称 lift。
R1061(C4)--(C5)的常数为 $b_{N,T}=\epsilon_T k_Q^N$，
其中 $\epsilon_T$ 是该实际字的中心，属于 $\mu_{p^2}$。
Galois 自然性和(H14)固定了整个轨道的中心；
它不是每个点可重新选择的相位。
当改用原小矩形代表时，R716(24)--(25)的
$\chi_r$ 反相位恰好抵消 theta 准周期，所得值仍为同一值。
因此
$$
 \boxed{
 \mathscr C_{N,T}
   :=\frac{b_{N,T}G(Q)^N}{v_Q^N},\qquad
 h(\mathscr C_{N,T})=\mathscr C_{N,T},\qquad
 v_p(\mathscr C_{N,T})=0 .
 }
 \tag{H16}
$$
估值来自 $v_p(b_{N,T})=N/\Delta$、$v_p(v_Q)=1/\Delta$ 和
$G(Q)$ 整单位。这里仅证明它对 Hall 固定。
两个实际 $\mathscr C$ 的乘积仍保(H13)的真正 wild 角色，
绝不把它们改成1，亦不将 $b_N$ 无条件写成
$\mathfrak w_Q^{-N}$。
原正、负全部三挠词和中心均在(H16)中保留。

## 5. 负二 Hall 读数的五层精确式

使用 [R1062](R1062-original-translated-miller-jets-and-critical-weight-germs.md)
(G4)--(G8) 的同一个函数 $\mathcal F_{N,Q}$。
它已付
$$
 \mathcal F_{N,Q}(-2)\in
 1+\mathfrak m^{\ge\eta}.
 \tag{H17}
$$
定义当前已经运输到同一物理 frame 的 negative Hall 读数
$$
 \mathcal H_-^{[-2]}(T)
  =\frac1d\sum_{h\in\widehat H}
   \frac{b_{102,hT}R_-(hQ)}
        {(102Z_{hQ})^2}\mathcal F_{102,hQ}(-2).
 \tag{H18}
$$
它是 R1062(G14)中的实际标记项的 Hall 平均；
这里没有自行给局部 primitive 添加常数或一次项，
也不称未完成 whole 接合的字已经是全局 AJ。

在严格坐标中定义完整整级数
$$
 H_-(v)=v^{102}T_{\rm g}(w(v))^{-102}R_-(w(v))
       \in v^4\mathcal O[[v]],\qquad
 \mathcal B_-(W)=
 \sum_{k\ge0}[v^{(k+1)d-2}]H_-(v)\,W^k .
 \tag{H19}
$$
首项为1及整性使用(H2)的真实多项式和 $T_{\rm g}^{\pm1}$ 的整性。
这不是仅按同一 charge 选的一份新有界来源。

代(H9)、(H16)--(H17)入(H18)。
主项是
$\mathscr C_{102,T}p^2/(102^2\kappa_0^2)$
乘 $v^{-2p}H_-(v)$ 的完整 $\mu_d$ 平均。
投影恰只保指数为 $d$ 的倍数；
由于 $H_-$ 从4次开始，首个可能指数是 $-d$。
所以主项严格为 $v^{-d}\mathcal B_-(W)$。

逆平方中的相对误差至少 $6p/\Delta$；
$\mathcal F(-2)-1$ 的界 $\eta$ 更深。
提出 $v^{-d}$ 后，最浅可能误差的指数是
$$
 4-2p+d+6p=5d .
$$
Hall 平均的分母 $d$ 是单位，且误差对 Hall 不变，
属于同一完成的 Hall 固定域；因此它确实在 $W^5$ 理想中。
得
$$
 \boxed{
 \mathcal H_-^{[-2]}(T)=
 \mathscr C_{102,T}\frac{p^2}{102^2\kappa_0^2}\,
 W^{-1}\bigl(\mathcal B_-(W)+\varepsilon_-(W)\bigr),
 \qquad v_p(\varepsilon_-(W))\ge\frac5{p-1}.
 }
 \tag{H20}
$$
这里的余项是在当前实际根 $W$ 的完成域中的元素；
不需要假称所有负二数据在全 $W$ 盘属于同一个先验整函数。
恰到第四层的 $\mathcal B_-$ 系数由(H19)完整确定。

令
$$
 F_{\rm c}=\Pi_0\log(\sigma/z),\qquad E_{\rm c}=e^{F_{\rm c}}.
$$
R660 的原完整身份给
$$
 H_-(v)=(v/z(v))^{102}E_{\rm c}(z(v))^{-102}D_-(z(v)).
$$
由(H4)，对 $0\le k\le4$，确切有
$$
 \boxed{
 b_{-,k}:=[W^k]\mathcal B_-
   =[z^{(k+1)d-2}]E_{\rm c}^{-102}D_- .
 }
 \tag{H21}
$$
所读次数至多 $5d-2<p^2$，没有漏掉严格 LT 的后继项。
特别
$$
 b_{-,0}=d_{-,p-1},\qquad
 b_{-,1}=d_{-,2p}-102c_\sigma d_{-,p-1},
 \quad d_{-,j}=[z^j]D_- .
 \tag{H22}
$$
两式的右边是完整组合；后式不允许把两项分别当成整单位。
第三至第五项使用(H21)的全部 $F_{\rm c}$，
不能只用第一 Gaussian $c_\sigma z^d$ 代替。

## 6. 原 canonical 正 Hall 以及真实反 CM 的边界变量

同样定义
$$
 \mathcal H_+^0(T_+)
   =\frac1d\sum_{h\in\widehat H}
       b_{34,hT_+}R_S(hQ_+).
$$
(H16)和 R663(9)--(13)的同一完整投影直接给 **精确式**
$$
 \boxed{
 \mathcal H_+^0(T_+)=
 \mathscr C_{34,T_+}\,W_+\mathcal B_{34}(W_+),\qquad
 \mathcal B_{34}(W)\in\mathcal O[[W]] .
 }
 \tag{H23}
$$
在本篇共同模型上
$$
 b_{+,k}:=[W^k]\mathcal B_{34}
  =[z^{(k+1)d}]E_{\rm c}^{-34}S\quad(0\le k\le4);
$$
特别 $b_{+,0}=s_d$、
$b_{+,1}=s_{2d}-34c_\sigma s_d$，$s_j=[z^j]S$。
这是原 canonical 行；没有把 $H_3,H_5$ 的质量代入。

令 $Q_+=\gamma_{102}Q$。
原实际图为
$\gamma_{102}=\delta\bar t_0\circ c$，范数3。
(H3)在 $E[p]$ 上给
$$
 \boxed{W_+=\widehat3\,W.}
 \tag{H24}
$$
这里 $\widehat3$ 是 $\mathbf Z_p^\times$ 中3的 Teichmüller lift。
证明时，复共轭把一个严格 LT 生成元送到其
$\mu_\Delta$ 倍；由共轭平方为1，该倍数范数为1。
$\delta\bar t_0$ 的模 $p$ 范数为3，作用在 $E[p]$ 上可用其
Teichmüller 提升替换，故取 $d$ 次幂得到(H24)。
这只是在这些实际挠点上的等式，不声称原整 CM 作用
$[\delta]$ 在整个形式盘是线性映射。
也不在全部精度上把 $\widehat3$ 换成整数3。

## 7. Haar、原 period 和五层完整卷积

在 R1054/R1061 的 Haar 规范中，真正 coevaluation 为
$p^{-2}(1\otimes\rho_+(t_0))C_{\rm Haar}$。
对(H12)的单条 canonical 角色，$t_0\in\mu_6$ 的值为1，
其两侧 Haar-正交规范向量各是 $d^{-1/2}$ 倍的完整 Hall 和。
所以从这两个向量回到(H18)、(H23)的两个 $d^{-1}$ 平均，
准确得到
$$
 \frac d{p^2}\,\mathcal H_-^{[-2]}\mathcal H_+^0 .
 \tag{H25}
$$
negative Hall 向量始终取 R1061(4)–(5) 原 Haar 双线性配对下
positive Hall 向量的严格对偶；两者在同一实际 orbit 基上的
$1/\sqrt d$ 幅度和互逆相位由(H10)–(16)的原 Weyl 中心锁定。
这里不是各自重新选一份 norm1 本征向量。
没有把坐标基上的 $p^{-1}$ coevaluation 当作 Haar 公式。

若该真实 graded 字的 $c_0,\ell_\pm,\Omega,\kappa,\rho$
已经按 R1062(G9)完成来源运输，则其基点项的确切系数为
$$
 \boxed{
 \begin{split}
 \mathcal R_{\rm Hall}(-2)
 &=\Omega^3\rho^{-2}\,
 \frac{d\,c_0\ell_-^{-2}}{102^2\kappa_0^2}\,
 \mathscr C_{102,T}\mathscr C_{34,T_+}\,
 \widehat3\\
 &\quad\cdot
 \mathcal B_{34}(\widehat3W)
       \bigl(\mathcal B_-(W)+\varepsilon_-(W)\bigr).
 \end{split}}
 \tag{H26}
$$
负侧 $p^2$ 恰与(H25)的 $p^{-2}$ 抵消。
在原 $\rho=(17/2)p^2\kappa\Omega^2$ 规范中
$$
 \Omega^3\rho^{-2}=(17/2)^{-2}p^{-4}\kappa^{-2}\Omega^{-1}.
$$
因此不能又把这个读数称为一个未付的 $p$ 进单位；
也不能在已含 $\delta$ 的 $\ell_-^{-2}$ 外再乘一次
$\delta^{-2}$。
原 raw $s_-/s_+$、$\vartheta$ 同构尺度、Artin/Cor 和
全部 $h$ 权若属于当前实际字，仍必须在 $c_0,\ell_\pm$
的精确来源式中出现，不能因固定而丢掉。
尚未完成这份运输的整个 $H_i$，仍保持原
$\mathfrak T_{\rm orig}$，不得直接套(H26)。

移去(H26)明写的实际非零前因子，前五层是完整卷积
$$
 \boxed{
 \sum_{k=0}^4
   \left(\sum_{i+j=k}b_{-,i}b_{+,j}\widehat3^{\,j}\right)W^k
      \pmod{W^5}.
 }
 \tag{H27}
$$
特别首层是
$d_{-,p-1}s_{p+1}$，其余四层包含(H21)和(H23)中的全部
Miller/gauge 完成项。这里没有假设两个首系数中的任何一个为单位。
若首层被 $p$ 整除，不能据第五层的误差界直接宣称其余层非零；
必须保(H27)的真实系数和同一根关系 $W^{p-1}=p$。

### 与主目标的准确范围

R716及
[原 first-wild Rubin 注](../notes/2026-11-15-original-first-wild-rubin-factor-and-central-order.md)
针对的是同一 canonical **单个** Hall：
$v_pA_p(t_{\chi^2})=2v_p\mathscr S_p(r)$。
用于排除坏中央阶的充分界是
$v_p\mathscr S_p(r)<2/(p-1)$，等价的 Iwasawa 值界是
$v_pA_p(t_{\chi^2})<4/(p-1)$。
本篇的 paired(H26)不能未经同来源证明便替代其中任一个量。

在已经准确返回原正 Hall 的规范中，$s_{p+1}$ 为单位确使
(H23)的正 Hall 具有首阶 $1/(p-1)$；这仍是一个带明确前提的
原读者结论。本篇未证明该前提对无穷多个 $p$ 成立。
已经支付的是原 wild 角色不改名、全部中心不丢失、真实反 CM
边界变量、完整负二连接误差，以及同一 canonical 行在前五层
的准确位置。

## 8. 前五层恰回原单参数 Newton 的有限除 p jet

本节使用 J 标签。它比较的是同一来源的五层整剩余行，
不宣称两个完整 $p$ 进 germ 相等，也不恢复已经撤回的
usual-depletion/flat 正权比较。

令 $c=c_\sigma$、$C_-=102c$、$C_+=34c$，
$\gamma_\pm=pC_\pm$，故 $\gamma_-=3\gamma_+$。
保持
[原 psi4 单参数 Newton 注](../notes/2026-11-27-original-psi4-double-slot-newton-and-canonical-slope.md)
(5)--(11)的准确来源，定义
$$
 \begin{aligned}
 g_h^-&=[z^{dh-2}](D_-e^{-C_-z^d}),\\
 g_h^+&=[z^{dh}](Se^{-C_+z^d}),\\
 J_-(u)&=\sum_{h\ge1}C_-^{-h}g_h^-(u)_h,\qquad
 J_S(u)=\sum_{h\ge1}C_+^{-h}g_h^+(u)_h,\\
 K_-(u)&=J_-(u)/(pu),\qquad
 L_S(u)=J_S(u)/(pu),\qquad
 (u)_h=u(u-1)\cdots(u-h+1).
 \end{aligned}
 \tag{J1}
$$
这里 $u$ 专指原 Newton 权参数，与(H3)的严格 LT 点坐标 $v$
不同。质量零 $S(0)=0$ 是(J1)原已付的事实，
没有为 $S$ 追加一个新的算术零条件。

### 8.1 全尾支付的真实有限除 p jet

R614 的整窗作用于
$D_-=\sigma^{102}xP_{16}(x^3)$ 和
$S=\sigma^{34}x^2P_4(x^3)$ 时，所读 $z^6$ 指标均为
$hs-1$。因此 $1\le h\le p-1$ 时 $g_h^\pm$ 整，
Newton 系数在 $p^h\mathcal O$ 中。
原单参数注(11)还完整保留 $h=p$ 的 $p^{p-1}$ 界、
$p+1\le h\le2p-2$ 的 $p^{h-2}$ 界；
更高项由其(8)的整个过收敛尾控制。
当前只需 $0\le r\le4$，故这些高尾除以 $p^{r+1}$ 后
仍在 $p\mathcal O$，不以无限尾为零。

$(u)_h/u$ 是次数 $h-1$ 的整多项式。
它的 $u^r$ 系数在 $h\le r$ 时为0，在 $h=r+1$ 时为1；
$h\ge r+2$ 的整个系数乘上 $p^{h-1}$ 后更深至少一位。
所以严格有
$$
 \boxed{
 \frac{K_-^{(r)}(0)}{r!p^r}
     \equiv\frac{g^-_{r+1}}{\gamma_-^{r+1}},\qquad
 \frac{L_S^{(r)}(0)}{r!p^r}
     \equiv\frac{g^+_{r+1}}{\gamma_+^{r+1}}
       \pmod p,\quad 0\le r\le4.
 }
 \tag{J2}
$$
左侧都是实际整数值的有限系数。
对这些函数定义
$$
 \operatorname{Jet}^{[p]}_4F(X)
     =\sum_{r=0}^4\frac{F^{(r)}(0)}{r!p^r}X^r .
 \tag{J3}
$$
只在 $\mathcal O[X]/(X^5)$ 使用这个有限 jet；
不主张 $F(X/p)$ 在任何原先未付的新盘上收敛。
Leibniz 公式使(J3)在模 $X^5$ 下保持乘法。

### 8.2 完整 Ec 费用是明确的整单位卷积

写
$$
 f_j=[z^{jd}]\log(\sigma/z),\qquad f_1=c .
$$
这里 $f_2,f_3,f_4$ 全整。
例如 R614(2)准确给
$$
 f_j=-\frac{X_{js}}{6js(6js-1)},
 \qquad z^2x(z)=1+\sum_{n\ge1}X_nz^{6n}.
$$
$j=2,3,4$ 时 $js<(p^2-1)/6$，故 $X_{js}$ 整，
而两个显示分母的模 $p$ 值为 $j$ 和 $j-1$，均非零。
这不把 $f_1$ 的一次分母删掉。

定义下列实际单位（只需模 $W^5$）：
$$
 U_5(W)=
 \exp\!\left(
   -\sum_{j=2}^4(102+34\widehat3^{\,j})f_jW^j
 \right)\pmod{W^5}
 \in1+W^2\mathcal O[W]/(W^5).
 \tag{J4}
$$
(H21)、(H23)的完整中央完成恰给
$$
 \boxed{
 \mathcal B_-(W)\mathcal B_{34}(\widehat3W)
 \equiv U_5(W)
       \left(\sum_{h=1}^5g_h^-W^{h-1}\right)
       \left(\sum_{h=1}^5g_h^+
                        \widehat3^{\,h-1}W^{h-1}\right)
             \pmod{W^5}.
 }
 \tag{J5}
$$
这是特征零的有限系数等式。证明只是把
$E_{\rm c}^{-N}=e^{-Nc z^d}
 \exp(-N\sum_{j\ge2}f_j z^{jd})$
代入(H21)、(H23)，再按 $d$ 的整数倍平移指标；
低于原首项的指标准确为0。没有省略任何 $f_j$ 或原多项式项。
例如
$$
 \overline U_5
 =1-408\bar f_2W^2-1020\bar f_3W^3
   +(83232\bar f_2^2-2856\bar f_4)W^4
       \quad\text{于 }(\mathcal O/p)[W]/(W^5).
 \tag{J6}
$$
这些整数来自同一个 $102+34\cdot3^j$；
不是重新选择一个可以改变原 $J$ 的 Gaussian。

### 8.3 同一个 canonical 读者，保 δ 的整对数

由(J2)及 $\widehat3\equiv3=\gamma_-/\gamma_+\pmod p$，
(J5)在剩余环中准确成为
$$
 \boxed{
 \overline{\mathcal B_-(W)\mathcal B_{34}(\widehat3W)}
 =\bar\gamma_-\bar\gamma_+\,
   \bar U_5(W)\,
   \overline{\operatorname{Jet}^{[p]}_4(K_-L_S)}
                          (\bar\gamma_-W).
 }
 \tag{J7}
$$
等号始终模 $W^5$。例如第 $k$ 项原来的整卷积
$\sum_{i+j=k}3^j g^-_{i+1}g^+_{j+1}$
准确等于
$\gamma_-\gamma_+\gamma_-^k
 (K_-L_S)^{(k)}(0)/(k!p^k)$ 模 $p$；
两个 charge 的比例正好支付这个 $3^j$。

还可以返回原单参数注(20)的两个真零因子的除商。
保其同一个
$$
 q_\delta=\delta^d/3\in1+p\mathcal O,\qquad
 \lambda_\delta=\log(q_\delta)/p\in\mathcal O,\qquad
 \mathcal A_{\rm can}(u)
      =-3q_\delta^{-u}K_-(u)L_S(u).
 \tag{J8}
$$
它不是一份新的 theta 来源。
由于 $\log q_\delta$ 被 $p$ 整除，
$\operatorname{Jet}^{[p]}_4(q_\delta^u)
   =\exp(\lambda_\delta X)\bmod X^5$；
当前阶乘 $1!,\ldots,4!$ 均为单位。
所以(J7)等价于
$$
 \boxed{
 \overline{\mathcal B_-(W)\mathcal B_{34}(\widehat3W)}
 =-\bar\gamma_+^{\,2}\,
   \bar U_5(W)e^{\,\bar\lambda_\delta\bar\gamma_-W}\,
   \overline{\operatorname{Jet}^{[p]}_4\mathcal A_{\rm can}}
                                  (\bar\gamma_-W)
        \pmod{W^5}.
 }
 \tag{J9}
$$
这保留原 $\delta^{-n}$ 对权导数产生的整对数，
没有把 $q_\delta$ 因为模 $p$ 等于1就在所有精度设为1。
(J9)只是一份全系数支付的有限剩余读数；
它不把 $p^{\rm weight}$、Gamma 或所有高权共同因子
插值成新的函数。

原 canonical 坏必要条件为 $J_S'(0)=0$。
它准确给
$$
 \mathcal A_{\rm can}(0)
   =-3K_-(0)J_S'(0)/p=0 .
 \tag{J10}
$$
因此本篇首层为0的必要性现在既有 Hall 来源，也有同一个
原 Newton 来源，且所有中心、charge、Gaussian 和
$\delta$ 费用已经列清。
它不迫 $\mathcal A_{\rm can}'(0)$ 或其它四个除 $p$ jet 为0：
例如坏条件下
$\mathcal A_{\rm can}'(0)
 =-3K_-(0)J_S''(0)/(2p)$，
其实际值仍未由 $J_S'(0)=0$ 决定。

最后，由(J9)中的两个单位及 $\gamma_\pm$ 为单位，
若五个剩余系数中有非零项，其首个位置与
$\operatorname{Jet}^{[p]}_4\mathcal A_{\rm can}$ 的首非零位置相同。
在 $W^{p-1}=p$ 的实际根上，若该位置为 $k\le4$，
(H27)移去全部显示前因子后的估值恰为 $k/(p-1)$：
较低系数被 $p$ 整除、较高项更深，而
$5/(p-1)<1$，所以不能发生同估值的抵消。
这没有证明那五项必有一项非零。
它也不提高 R716 的单 Hall 严格阈值；
首位置 $k\ge1$ 仍可能与原坏中央阶相容。

## 9. 原 Hall 输出、同源两槽及同一 Rubin 幂级数的精确门

2026-11-28。本文沿 R1054、R1059、R1060、R1061(F)、
R1062 和 R716 的同一来源。I 标签保持本节的独立索引。

**范围。** 本文支付一个确切的新有限输出：从原非零 Norm 纤维
再作原 tame-zero Hall 投影，保全部非 p 来源、两条三挠词、
actual CM 微分、Haar、外权及其导数。它不是把原未投影
reader 改名。最后给同一整 Rubin 系数的必要估值门；
没有由 Hall 非零直接推出原 canonical 导数非零。

### 9.1. 从原 Norm 纤维到唯一的原 Hall 线

令 d=p+1，p>211 为当前原惰性好素数。
保持 R716 的 additive character，尤其
\[
 \zeta_p=e_p^{-1},\qquad
 \chi_r(1+p\delta l)=e_p^{34rl},\qquad r\in\mathbf F_p^\times .
 \tag{I1}
\]
\(\chi_r\) 在 Teichmüller 子群和有理单位上平凡。
记 \(T_2=(\mathcal O_K/p^2)^1\)，\(T_1=\ker(T_2\to T_2\bmod p)\)。

R716 的实际正模型中，
\[
 e_v=W_+\bigl((x+y)/3,-51(x-y)\bigr)v_0,\quad v=x+y\omega,
\]
且 physical CM \(g\) 对应 R1054 的 \(M(\bar g)\)。
因此原 physical Hall 特征 \(\chi_r^{-1}\)，在 R1054 的
\(M\)-标号中，正线是 \(\chi_r\)、负对偶线是
\(\vartheta_r=\chi_r^{-1}\)；这里不再作一次共轭。

原 physical Galois 字给
\[
 \zeta_p^{51lN(u)}
 =e_p^{-68lr}=\chi_r(1+p\delta l)^{-2},
 \qquad N(u)=4r/3 .
\]
所以 F8 的准确 Norm 参数为 \(b=68r\)，不是 \(34r\)。
在此 Norm 字后施加
\[
 P_{\mathrm{tame},0}^{-}
   =\frac1d\sum_{\tau\in\mu_d}
           \rho_-(\tau)\otimes1
 \tag{I2}
\]
才得到 R716 的原 Hall 输出。
(I2) 是额外明确的有限算子；它没有被默认加入 F8 或原 frozen
reader。

取 \(a_l\) 为 E15 的实际 Cayley lift，并对每个
\(\tau\in\mu_d\) 取 Teichmüller lift \(t_\tau\) 满足
\(t_\tau/\bar t_\tau=\tau\)。
这些 lift 存在于原非分裂二次域的单位群中。
不能只取范数一平方根：其平方只覆盖半个 tame torus。
令 \(t_{\tau,l}=t_\tau a_l\)。
在已锁定的共同 weight component 上，真实 Hall germ 是
\[
 \boxed{
 {\cal H}_{i,r}(j)=
 \frac1{pd}\sum_{\tau,l}
       \zeta_p^{-68rl}\,
       j_{t_{\tau,l}}(j)\,
       M_{A_{i,t_{\tau,l}}}(j).
 }
 \tag{I3}
\]
\(A_{i,t}\) 是原实际 bounded source，不是形式换元所造的测度；
\(j_t(j)=N(t)^{-j}\bar t^{\,3+2j}\)，
\(\kappa_t=N(t)\)、\(\Omega_t=\Omega/\bar t\) 仍按 R1054/R1059。
Teich lift 的 \(j_t'\) 为零，但其根单位值不能删；
wild 部分 \(j_t'/j_t=-\log(t/\bar t)\) 全留。
于是(I3)在实际值和斜率上正是(I2)作用于 F8--F11，
而不只是正整数形式恒等式。

R716 以自对偶 Haar 给
\[
 \varphi_{+,r}
   =d^{-1/2}\sum_{N(v)=r}\chi_r(v)e_v,\qquad
 \|\varphi_{+,r}\|=1.
\]
负向量 \(\varphi_{-,r}\) 定义为原负模型中的准确 Haar 对偶；
这里同时固定所有 Weyl 中心相位，不能再任选一个本征向量。
R1054 的完整 coevaluation 是
\[
 K=p^{-2}(1\otimes\rho_+(t_0)){\cal C}_{\mathrm{Haar}},
 \qquad t_0=(1+\delta)/2 .
\]
因为 \(\chi_r(t_0)=1\)，且原旧 \(v_0\otimes v_0\) 被非平凡
wild 投影杀掉，得到
\[
 \boxed{
 (P^-_{\vartheta_r}\otimes1)
       (K-v_0\otimes v_0)
       =p^{-2}\varphi_{-,r}\otimes\varphi_{+,r}.
 }
 \tag{I4}
\]
若各 Hall 和改用 \(d^{-1}\) 平均，(I4)前因子相应为
\(d/p^2\)。\(p^{-1}\) 是 counting-coevaluation 规范的数，
不是本式的 Haar 数。

### 9.2. 同一个完整 source，以及全局外权的方向

现在先取目标 \(k=1\)，即原 \(S_{34}\)/\(\psi_{17}\)；
\(k=3,5\) 同理保各自原十七向量，不能混作一个角色。
置 \(\eta_k=\psi_k/\psi_4\)、\(\mu=\nu_0\)。
原实际两个 norm-one characters 的 Hilbert90 拉回是
\[
 \widetilde\alpha_{1,k,n}
   =\eta_k^{-1}\nu_4^{-(2n+1)}\nu_0,\qquad
 \widetilde\alpha_{2,k,n}
   =\eta_k\nu_4^{2n+5}\nu_0 .
 \tag{I5}
\]
R716(32)以类数一的紧代表定义了全局 \(\eta_r\)，其 Hilbert90
拉回记为 \(\nu_r=\widetilde\eta_r\)。
\(\eta_r\) 在无穷和所有非 p 有限紧子群上平凡；在 p 处为
\(\chi_r\)。\(\nu_r\) 的 p 分量是 \(\chi_r^2\)，恰有导子
\(p^2\)、阶 p。非 p 好分裂处可有非平凡未分歧值，不能把整个
分量误称平凡。

真正 Hall 双槽使用
\[
 \alpha_{1,k,n}^{(r)}=\alpha_{1,k,n}\eta_r^{-1},
 \qquad
 \alpha_{2,k,n}^{(r)}=\alpha_{2,k,n}\eta_r .
 \tag{I6}
\]
两者乘积不变，所以 binary input 仍是同一 \(\nu_4^2\) 来源。
正槽的 physical eigenvalue 是 \(\chi_r^{-1}\)，其 theta 积分
乘 \(\eta_r\)，与 R716(30)--(33)的方向一致。
负槽使用准确对偶，未把负 Hermitian 线换成另一条正线。

若旧全局 toric character 为 \(\xi_{k,n}\)，则
\[
 \boxed{
 \xi_{k,n}^{(r)}=\xi_{k,n}\nu_r^{-1},\qquad
 \lambda_{i}^{(r)}(\mathfrak a,n)
   =\lambda_i(\mathfrak a,n)\nu_r(\mathfrak a)^{-1}.
 }
 \tag{I7}
\]
沿原 \(a_p=t^{-1}\) 的 marked convention，新增局部权为
\(\nu_r(t)\)，准确等于
\(\vartheta_r(t/\bar t)^{-1}\)。
这核对了(I3)与全局 toric 权的同一方向。
不能把(I7)的好分裂未分歧值从 Artin/Cor 重标中删除。

在完整 source 端，输入 \(h_p\) 是两输出的 diagonal action，
与(I2)、(I4)交换；非 p 算子在其他张量因子。
原 \(h_\infty\) 积分仍是完整的差2槽投影。
对固定 \((n,n+2)\) 槽，(I5)--(I6)正是其真实无穷角色；
没有在低 Maass 槽提前换成第 n 槽的输出角色。

由 \(h_K=1\)，范数一 idèle 可乘全局范数一主元，使有限分量
全为单位，两个选择差 \(\mu_6\)。\(\eta_r\) 在 \(\mu_6\) 及非 p 的有限紧单位群上平凡，
故这一重排不改无穷/非 p Schwartz，也不产生新的 Satake
归一。原 full2、full9、十七 projector、两三挠词和 fixed
Artin/Cor 均原样保留。原未平方 seesaw 的紧双积分可逐项交换；
(I4)于是变成两个指定 Hall rank-one theta lifts 的乘积。
这一步只对实际(I7)的输出 covector成立；不能拿它去替原
frozen \(\Lambda(-2)\)、\(\Lambda'(-2)\) 的所有低槽。

### 9.3. 固定 Hall 来源的真正正整数支

正槽的原代数 Hecke character 为
\[
 \eta_k\psi_4^{2n+5}\nu_r=\psi_k^{2n+5}\nu_r
       \quad(n\equiv4\bmod6).
\]
若再令 \(n+2\equiv0\bmod p\)，则
\[
 \boxed{
 \psi_k^{2n+5}\nu_r=(\psi_k\nu_r)^{2n+5}.
 }
 \tag{I8}
\]
因此此共同合法子列确实使用一个固定 Hall finite vector，
不是每个 n 重新选择一个向量。

可以取 \(n=-2+Dp^\ell\)，其中 prime-to-p 的 D 同时倍于18、
原所有有限/Teich 周期，并在必要时扩大 \(\ell\)。
若 \(\lambda_k=\psi_4^4/\psi_k\)，则此支上负槽的共轭正权因子
同样可写成
\[
 \eta_k\psi_4^{2n+1}\nu_r
   =(\lambda_k\nu_r^{-1})^{(2n+1)/3}.
 \tag{I9}
\]
这里 \(n\equiv-2\bmod18\) 及
\((2n+1)/3\equiv-1\bmod p\) 同时保持。
(I9)只是完整角色与 Hermite 支的身份，不把负二槽称为普通
Taylor 系数。

原 compact 代表和 prime-to-p ideal 代表中，(I7)的所有随 n
改变的有限因子都是已经指定的 p-adic 单位幂。
原 \(j_t,\kappa_t\) 也如此。
故在 R1059 同一个足够小的 weight component 上它们有真实
解析延拓。全部 factorial、\(p^{2n}\)、book period 均仍在
R1054/R1060 的实际 slot normalization 中；本节不加入
Whittaker Gamma，也不使用已撤回的 usual/flat cross。

### 9.4. 原非 p raw 幅度和实际微分，不另选 period

原 degree102 负来源及正34来源使用同一个十七向量。
在 \(b=1\) 模型，已付 raw 比为
\[
 \frac{s_{-,k}}{s_{+,k}}
   =\frac{r_k}{2^{1/3}(1+\sqrt3)},\qquad
 (r_1,r_3,r_5)=(-7,624,1224),
 \tag{I10}
\]
负 coherent 变量是 \(\Omega_0 h_\infty T/\delta\)，正为
\(\Omega_0 h_\infty T\)，其中
\[
 h_\infty=\frac{\sqrt{51\sqrt3}}{204\pi i},\qquad
 b_H=\frac{2(\omega-1)}{\sqrt{51\sqrt3}} .
\]
两三挠 Weyl 词及其 Gaussian 始终包含在负102函数中，
未把普通三盖 trace 当作这两个有权词。

为与 R716 的同一 \(E_{17}\) 比较，取原实
\(\vartheta^6=17\)、\(\Omega_{\mathbf R}=\Omega_0/\vartheta\)。
两个首项规范准确给
\[
 S_{17}(z)=\vartheta^{-6}S_1(\vartheta z),\qquad
 D_{102,17}(z)=\vartheta^{-4}D_{102,1}(\vartheta z).
\]
因此在相同 raw Fourier 函数下
\[
 s_{+,17}=C,\qquad
 \boxed{
 s_{-,17}
   =-\frac{7\vartheta^{-2}C}{2^{1/3}(1+\sqrt3)} .
 }
 \tag{I11}
\]
这里 C 正是 R716(17)--(18)、(23)、(31)的原有符号幅度；
没有重新开平方选相位。

还须区别 binary source period 和 rank-one 输出 period。
原新图已经固定 \(A=A_4:y^2=x^3+4\)、\(\omega_A=dx/(2y)\)，
以及全部十八个规范商
\(\lambda_C:A\to A_C=A/C\)，其微分为
\(\lambda_C^*\omega_C=\omega_A\)。
这正是新图文稿§5(20)、§6.1的实际输入，不另找同度同源。

写 \(t_4=2^{1/3}>0\)、\(u=\vartheta/t_4\)，
\(\lambda_A=\Omega_0/(t_4\delta)\)。
取这条原曲线的标准格
\(\lambda_A(\mathbf Z+\omega\mathbf Z)\)。
全部商格和相应实际 classical matrices 是
\[
\begin{array}{c|c|c|c}
 C&\alpha_C&\tau_C&g_C\\ \hline
 C_\infty&1/17&17\omega&
       \left(\begin{smallmatrix}17&0\\0&1\end{smallmatrix}\right)\\
 C_a\ (a=0,\ldots,16)&1&(\omega+a)/17&
       \left(\begin{smallmatrix}1&a\\0&17\end{smallmatrix}\right).
\end{array}
\]
具体地 \(\Lambda_C=\lambda_A\alpha_C
(\mathbf Z+\tau_C\mathbf Z)\)，
\(2\pi i\gamma_C=\lambda_A\alpha_C\)。
原双同源后再作真实 homothety
\[
 \iota:A_4\longrightarrow E_{17},\qquad
 (x,y)\longmapsto(u^2x,u^3y),\qquad
 \iota^*\omega_{17}=u^{-1}\omega_A
\]
给 \(\phi_C=\iota\widehat\lambda_C\)，
其实际解析倍率 \(a_C=17\alpha_C\)，实际微分倍率
\(c_C=17u^{-1}\)。所以
\[
 \boxed{
 \Gamma_C=\frac{\Omega_{\mathbf R}}{2\pi i\gamma_C}
          =\delta\frac{c_C}{a_C}
          =\frac{\delta u^{-1}}{\alpha_C},
 \quad
 \Gamma_A=\delta u^{-1}.
 }
 \tag{I12}
\]
十七条 \(\Gamma_C=\Gamma_A\)，另一路为
\(17\Gamma_A\)。这些是明确代数数，p>211 时均为单位。
原 full2/full9 换基和 sign 不改变曲线及微分；其实际 finite
source phase仍随原 word 保留。若为读取另一个 classical
component而改格基，则按该实际矩阵同时变 \(\gamma_C\) 和
slash multiplier，不能只改其中一个。

这一表还支付全部升权的共同 frame，而非只支付首项。
若 \(g_C=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\)，
逐项有
\[
 \frac{\gamma_C}{c\omega+d}=\frac{\gamma_A}{17}.
\]
令 \(B_C\) 表示该实际 n=0 classical word已经给出的
完整幅度：
\((T_C f)(\tau)=B_C(c\tau+d)^{-3}f(g_C\tau)\)。
\(B_C\) 包含原 normalized slash 的 determinant、有限
Weil/level相位；这是既定 operator 的 n=0 数据，不重新
定标一个本征向量。
Maaß covariance给所有 n 的同一恒等式
\[
 \begin{split}
 \delta_3^n(T_Cf)(\omega)
 &=B_C\,17^n(c\omega+d)^{-3-2n}
                         \delta_3^nf(\tau_C)\\
 &=B_C\,\gamma_A^{3+2n}\,17^{-3-n}
                    (\mathcal D_3^nf)(A_C,\omega_C).
 \end{split}
 \tag{I12a}
\]
第二行先在复数域的同一微分比较中成立，再只对代数 CM
系数作原 p-adic embedding。
因此完整十八项回到同一个 \(\gamma_A\)。
没有在单图上套两个 rank-one 函数的分离公式。

p-adic side也可逐项核同一个因子。
临时使用真实 direct-push Tate frame
\(\alpha_C^{\rm d}=\lambda_{C,*}\alpha_A\)。
R1059(A0a)--(A0c)及 Poincaré 配对准确给
\[
 \lambda_C^*e_{C,j}^{\rm d}=17e_{A,j},\qquad
 \kappa_C^{\rm d}=17\kappa_A,\qquad
 \Omega_C^{\rm d}=\Omega_A/17.
\]
于是
\[
 R_{C,n}^{\rm d}
 =p^{2n}\kappa_A^n\Omega_A^{3+2n}
       17^{-3-n}(\mathcal D_3^nf)(A_C,\omega_C).
 \tag{I12b}
\]
(I12a)与(I12b)正是同一个 source 的 common-frame比较。
其中 \(17^n\)、\(17^{-3-n}\) 已包含原17 word；
绝不能再向 I16 的 \(a^n=(17/2)^n\) 另乘一次 \(17^n\)。

若原实际 Tate frame是
\(\alpha_C^{\rm act}=\alpha_C^{\rm d}h_C\)，
保这个原已给矩阵 \(h_C\in{\rm GL}_2(\mathbf Z_p)\)及其
对有限来源的实际作用。令
\[
 J_{h_C}(y)=\frac{\det h_C}
       {(h_C)_{11}+(h_C)_{21}\widehat z(y)},\qquad
 {\mathfrak j}_{h_C}(n;y)
       =(\det h_C)^{-n}J_{h_C}(y)^{3+2n}.
\]
这是同一个 tensor pullback；实际 source与level也同时运输，
不是用标量去替换另一个函数。
完整 point-word于是以
\({\mathfrak j}_{h_C}R^{\rm act}_{C,n}=R^{\rm d}_{C,n}\)
返回(I12b)。多段 word依原次序取 cocycle，\(J\)在各段
实际点评价，不能把不同点的因子随意交换。
在原惰性 CM 点的余域，\(\widehat z\notin\mathbf F_p\)，
故这些 unit matrices的实际分母均为单位。

为把上述步骤与原外权连起来，令 \(b_{k,i}^{\rm orig}\)
表示原完整非 p 有限项：十八核权、full2/full9、
先 \(Q_\tau/e_A^-\) 后 sign、\(1/2\)、\(1/6\)、
全部 Artin/Cor、以及原紧商测度的既定系数。
逐项展开矩阵时保全部列。
在 direct-push参考 frame，(I12a)--(I12b)使该项的
正权系数准确为 \(b_{k,i}^{\rm orig}B_i\)，不另添随 n
变化的标量。
回 actual frame并加 Hall 时，真正系数为
\[
 \boxed{
 \Lambda^{(r)}_{k;i,t}(j)=
 b_{k,i}^{\rm orig}B_i\,
 \nu_r(\mathfrak a_{i,t})^{-1}\,
 {\mathfrak j}_{h_i}(j;y_i)\,
 {\mathfrak j}_{t}(j;y_{i,t}),
 }
 \tag{I12c}
\]
其中 p torus 的原 \(1/[p(p+1)]\) 测度按(I3)只出现一次。
(I3)的 \(\zeta_p^{-68rl}\) 已是此处 \(\nu_r(\mathfrak a)^{-1}\)
的 p 分量，不能在(I12c)以外再乘一次。
\(\mathfrak a_{i,t}\) 是原实际 idèle，不另造代表；
若采用新的 prime-to-p integral代表，principal scalar及
微分必须同时乘回。
这里采用原 compact norm-one代表，必须明确其与 integral-ideal
写法的全部 Norm/avatar费用。若原 prime-to-p ideal为
\(\mathfrak a=(\beta)\)，改用 \(\beta^{-1}\mathfrak a\) 的紧
代表时，p 标记为 \(t=\beta\)。
令 \(R_{\rm int},R_{\rm cmp}\) 分别为这两个表示中同一完整
toric tensor的裸标量，\(\ell_{\rm int},\ell_{\rm cmp}\) 为
其真正对偶 covector。R1054 已锁的 right-action和原全局
character在 \(K^\times\) 平凡，逐项给
\[
 \begin{split}
 R_{\rm cmp}(j)&=
     {\mathfrak j}_\beta(j)^{-1}R_{\rm int}(j),
       &{\mathfrak j}_\beta(j)^{-1}
          &=N(\beta)^j\bar\beta^{-3-2j},\\
 \ell_{\rm cmp}(j)&=
     {\mathfrak j}_\beta(j)\ell_{\rm int}(j),
       &{\mathfrak j}_\beta(j)
          &=N(\beta)^{-j}\bar\beta^{3+2j}.
 \end{split}
 \tag{I12d}
\]
两行是反变的一对，不能把第一行称为对偶权的变换。
若紧表示中的非 p Fourier/projector系数为 b，则原 ideal
表示中 \(\ell_{\rm int}={\mathfrak j}_\beta^{-1}b\)；
返回紧表示时恰乘 \(\mathfrak j_\beta\)。
这正支付 integral-ideal公式中的 \(N(\mathfrak a)^j\)及
全部 Hodge/avatar，而不是只保孤立的 AI
\(\iota(\mathfrak a_p)^{-1}\) 项。
无穷 weight、CM微分和全局 principal reciprocity同时在
(I12d)内；不能只改一个 p 分量而不改非 p/无穷相位。

原 source的每个紧 norm-one代表满足 Norm=1。
在当前固定合法分量，全部非 p有限角色值也固定，所以该
表示中的 \(b_{k,i}^{\rm orig}B_i\) 确为 n=0常数。
若坚持使用 integral代表，则必须把(I12d)两行完整保回。
两导数的
\(\log N(\beta)-2\log\bar\beta\)及其相反数准确抵消。
因此(I12c)中没有再悬空一项未列的
\(N(\mathfrak a)^j\)或 avatar导数。
这并不授权丢掉另一个非 seesaw读者额外指定的解析外权：
若添加 \(w_i(j)\)，左边必须乘 \(w_i\)，求导保 \(w_i'\)，
而 I16 的单乘积式不能未经重新计算就继续使用。

(I12c)是同一原 finite word的展开，不是任取可用的权。
其导数完整包括
\[
 -\log\det h_i+2\log J_{h_i}
       -\log N(t)+2\log\bar t
\]
这些就是当前 compact seesaw covector的全部 weight导数；
若采用 integral代表，(I12d)还要求把两项相消显示出来，
不能在已回紧表示后再次重计。
(I12c)逐项仍保持原完整有限矩阵的次序。

仅在完成这份全非 p/Artin输出以后，才调用原未平方
seesaw给出的 rank-one finite函数。
此时 binary source共同 period是 \(\gamma_A\)，即(I12)的
\(\Gamma_A=\delta u^{-1}\)，而不是某一路商点的 \(\Gamma_C\)。
原 \(-\delta f_4(\tau/6)\) 的实际 component transport仍带
\(-6\delta\) 与 \(Z/\sqrt6,W/\sqrt6\)；
在原§33 frame，结合
\(h_\infty(-ib_H)=(1-\omega)/(102\pi)\)，得到
\[
 \boxed{
 \ell_-=-\frac{i(\omega-1)\Gamma_A}{51\sqrt6\,\delta},
 \qquad
 \ell_+=-\frac{i(\omega-1)\Gamma_A}{51\sqrt6}.
 }
 \tag{I13}
\]
特别
\(\ell_-\ell_+=\delta\omega/(2\cdot51^2u^2)\)，
是明确的 p 单位。未完成实际 arch/component运输的单图
仍用 R1060 的完整 \(\mathfrak T_i\)，不得提前套(I13)。

共同幅度由同一全 raw 函数固定：它是原 Gaussian/Fourier
常数 \(C_a\)、原紧 torus测度因子，以及
\[
 (-6\delta)\,\frac{s_{-,17}s_{+,17}}{\gamma_A}
 \tag{I14}
\]
的乘积。
\(C_a\) 就是原双核(33)的 Gaussian integral常数；若以
其显示的 \(dx\,dy\) 规范写，它为
\(1/[a\sqrt{\sqrt3-3i}\sqrt{\sqrt3+i}]\)，两根取原收敛
Gaussian的支，其他已固定 Weil因子仍随原算子。
各紧 quotient volume用原 Haar；改概率 projector时必须
在左右两边各按同一个原体积乘回，不能重计。
这里已经直接代数的是 Gaussian/Fourier常数及原 Haar volumes，
它们的坏 p 只来自原固定分母/范数；raw 幅度
\(s_{-,17}s_{+,17}/\gamma_A\) 的代数性另由下面(I15)支付。
没有引入一个来源外 Gamma。
完整有限 projector的幅度也已经包含原 Fourier
\(s_{-,17},s_{+,17}\)，不在(I14)再加一次 \(1/18\) 或
十七投影的范数。

(I14)的代数化可直接检查。R716给
\[
 C_{17}^{(0)}C^2=48940416\,\Omega_{\mathbf R},\qquad
 C_{17}^{(0)}=
 \frac{\pi\sqrt{102\sqrt3}}
      {153\sqrt3(3+\sqrt3)(17-\sqrt{17})},
\]
所以
\[
 \frac{C^2}{\gamma_A}
 =\frac{48940416\,(2\pi i)\Gamma_A}{C_{17}^{(0)}}
 \in\overline{\mathbf Q}.
 \tag{I15}
\]
原 quotient volumes、Gaussian/Haar常数和(I11)、(I15)
全部保留后，记得到的固定幅度为 \(c_0\)。
只有这些整槽系数完成代数化后才作
\(\overline{\mathbf Q}\to\mathbf C_p\)嵌入。
没有把复 period本身嵌入 \(\mathbf C_p\)。

#### 9.4a. 同一共同幅度的固定坏素数

(I14)的 \(c_0\) 不是逐 \(p\) 重选的幅度。保留原测度后，
其共同 quotient-volume 因子只来自原紧商的 \(\mu _6\)；
R290 §7 给紧体积乘积除以商体积准确为6。
原有限 Fourier、full2/full9/17 和正交 projector 的测度
分别只引入2、3、17的幂及其平方根。
新增 \(p\) 处的 Haar 费用已全部显列在(I3)、(I4)、(I16)，
不再计入 \(c_0\)。

因此可直接核固定系数的整性，而不把 raw theta-null称为单位：
\[
 48940416=2^7\,3^3\,7^2\,17^2,\qquad
 N_{\mathbf Q(\sqrt3)/\mathbf Q}(3+\sqrt3)=6,\qquad
 N_{\mathbf Q(\sqrt{17})/\mathbf Q}(17-\sqrt{17})=2^4\,17.
\]
(I12)的 \(\Gamma_A=\delta\,2^{1/3}/17^{1/6}\) 及(I11)的
canonical 比值 \(-7\vartheta^{-2}/[2^{1/3}(1+\sqrt3)]\)
均是仅在2、3、7、17处可能非单位的代数数；
这里 \(N(1+\sqrt3)=-2\)。
(I14) Gaussian根下的
\(\sqrt3-3i,\sqrt3+i\) 与其复共轭之积分别为12与4，
而 \(a=17/2\)，故该准确 Gaussian幅度也只涉及同一固定坏集。
结合(I15)，真正代数化的 \(C^2/\gamma_A\) 和 \(c_0\)
均是所用固定系数域中、在
\(\mathbf Z[1/(2\cdot3\cdot7\cdot17)]\) 上的整单位。
结论不涉及单独的复周期在 \(p\) 进域中的像。

当前 \(p>211\)，所以
\[
 v_p(c_0)=v_p(\ell_-)=v_p(\ell_+)=0.
\]
(I18)的全部显式非单位费用因而为
\[
 {\cal B}_r(-2)
 =p^{-6}\Omega_A^{-1}
   \frac{c_0}{(17/2)^2\kappa_A^2\ell_-^2}\,
   H_{-,r}^{[-2]}H_{+,r}^{[0]},
 \qquad
 \frac{c_0}{(17/2)^2\kappa_A^2\ell_-^2}\in
       \mathcal O_{\mathbf C_p}^{\times}.
\]
这里使用原基准 \(\kappa_A=1\)；换原实际 frame仍按(I12b)–(I12c)
运输。这个单位账本不声明两个 Hall 因子的估值，更不推出(I22)
所需的严格上界。

### 9.5. 全 Hall 正权有限返回与临界 germ

用 \(B_{-,v},A_{-,v}=102Z_{Q_{-,v}}\) 和
\(B_{+,w},A_{+,w}=34Z_{Q_{+,w}}\) 表示 R1062 的实际
translated data，包含原 Miller 中心和三挠词。
正点可按 R716 写成
\(Q_{+,w}=\Omega_{\rm CM}w/p\)、\(N(w)=r\)。
对应负点的 Norm 是 \(r/3\)，所以
\(102(r/3)=34r\)；不能在负102坐标仍直接用同一个 r。

令 \(\epsilon^-_v,\epsilon^+_w\) 为(I4)这两个确切 Haar 向量
中未含显示的 \(d^{-1/2}\) 的字系数。正系数是 R716 的 \(\chi_r(w)\)，负系数由准确
对偶给定，所有 root cocycles保留。
定义此处 \({\cal B}_r(j)\) 为**完成全原非 p/十七/两sign/
Artin输出的整列**，即原全部 actual source之和
\(\sum_{i,t}\Lambda^{(r)}_{1;i,t}(j)M_{A_{i,t}}(j)\)，
系数准确使用(I12c)及(I3)的一次 Haar。
它不是十八个单图中的任一个。其正整数返回为
\[
 \boxed{
 {\cal B}_r(n)=
 \frac{c_0}{p^2}\Omega_A^3\rho_A^n
 \ell_-^{\,n}\ell_+^{\,n+2}
 \left\{\frac1{\sqrt d}\sum_v
 \epsilon^-_v B_{-,v}A_{-,v}^{\,n}{\cal F}_{-,v}(n)\right\}
 \left\{\frac1{\sqrt d}\sum_w
 \epsilon^+_w B_{+,w}A_{+,w}^{\,n+2}{\cal F}_{+,w}(n+2)\right\}.
 }
 \tag{I16}
\]
这里 \(\rho_A=(17/2)p^2\kappa_A\Omega_A^2\)。
(I16)是(I4)--(I9)的未平方 seesaw 后，再逐字代入 G7；
不是将某个任意 seed 当成整个 \(\mathfrak T_{\rm orig}\)。

两求和是独立的 Hall 轨道。R1062 G1--G14 的两槽 Leibniz
与估值证明对每一对非零点原样成立；并不调用其中仅适用于
反线性图 Norm 纤维的 G17 非零结论。
所有 finite words为实际 finite sums，全部高阶系数仍保留。

取固定非零参考点 \(v_*,w_*\)，置
\[
 U_*=\rho_A\ell_-\ell_+
                A_{-,v_*}A_{+,w_*}.
\]
这才是真正单位；不能分别插值两个非单位 \(A_\pm\)。
各 \(A_{-,v}/A_{-,v_*}\)、\(A_{+,w}/A_{+,w_*}\) 也为单位。
共同选 R1062 G12 的 Teich/深主单位分量，定义
\[
 \begin{split}
 N(j)&=\frac1{\sqrt d}\sum_v\epsilon^-_vB_{-,v}
  \left(\frac{A_{-,v}}{A_{-,v_*}}\right)^{[-2]}(j)
           {\cal F}_{-,v}(j),\\
 P(j+2)&=\frac1{\sqrt d}\sum_w\epsilon^+_wB_{+,w}
  \exp\!\left((j+2)\log\frac{A_{+,w}}{A_{+,w_*}}\right)
           {\cal F}_{+,w}(j+2).
 \end{split}
\]
所有根单位在共同合法子列上按原整数基点固定。
由(I3)的实际 bounded 来源、R1059 的全 Maass 一致尾以及
(I7)的解析外权，原正整数逼近给真正的 germ 恒等式
\[
 \boxed{
 {\cal B}_r(j)=
 \frac{c_0}{p^2}\Omega_A^3
   (\ell_+A_{+,w_*})^2
   U_*^{[-2]}(j)\,N(j)P(j+2).
 }
 \tag{I17}
\]
没有从一列非连续 usual 值制造 p-adic 函数。
(I17)左端始终是同一 full Hall covector的实际 Amice/Maass
极限，而非给右端另起一个名字。

特别记
\[
 H_{-,r}^{[-2]}=
  \frac1{\sqrt d}\sum_v\epsilon^-_v
        B_{-,v}A_{-,v}^{-2}{\cal F}_{-,v}(-2),\qquad
 H_{+,r}^{[0]}=
  \frac1{\sqrt d}\sum_w\epsilon^+_w B_{+,w}.
\]
则
\[
 \boxed{
 {\cal B}_r(-2)=
 \frac{c_0\Omega_A^3}
      {p^2\rho_A^2\ell_-^2}\,
 H_{-,r}^{[-2]}H_{+,r}^{[0]} .
 }
 \tag{I18}
\]


**与前文 \(E_0\) 严格坐标的实际模型对照。**
(I13)–(I18)的 \(\ell_\pm,c_0,B_\pm,A_\pm\) 在 \(E_{17}\) 规范中。
若使用(H18)、(H23)的首项一 \(E_0:y^2=x^3+1\) 来源，
(I11)给 \(B_{-,17}=\vartheta^{-4}B_{-,0}\)、
\(B_{+,17}=\vartheta^{-6}B_{+,0}\)、
\(A_{\pm,17}=\vartheta A_{\pm,0}\)，而完整 \({\cal F}_\pm\)
在此对应下相同。因此在同一个 \(d^{-1/2}\) 规范中，
\[
 H_{-,r,17}^{[-2]}=\vartheta^{-6}H_{-,r,0}^{[-2]},
 \qquad H_{+,r,17}^{[0]}=\vartheta^{-6}H_{+,r,0}^{[0]}.
\]
明确置
\[
 c_0^{(0)}=\vartheta^{-10}c_0,\qquad L_\pm=\vartheta\ell_\pm .
\]
则同一个整列的(I18)在 \(E_0\) 中准确为
\[
 {\cal B}_r(-2)=
 \frac{c_0^{(0)}\Omega_A^3}{p^2\rho_A^2L_-^2}
 H_{-,r,0}^{[-2]}H_{+,r,0}^{[0]},\qquad
 \frac{c_0^{(0)}}{L_-^2}=17^{-2}\frac{c_0}{\ell_-^2}.
 \tag{I18a}
\]
若改用(H18)、(H23)的 \(d^{-1}\) 平均，两因子共同再给原来的
\(d\)，不增加另一个 \(p\)-Haar。(H26)中“已经完成来源运输”的
\(c_0,\ell_\pm\) 必须使用本式的对应模型；不能将(I13)的
\(E_{17}\) 数值与 \(E_0\) Hall 直接混用。该固定 \(17^{-2}\)
在当前所有允许 \(p\) 处是单位，全部严格估值门不变。

负二保全部 \({\cal F}_{-,v}(-2)\)，正槽准确是原 translated
theta value。按 R716(23)、(31)的同一 Heisenberg/lattice
规范，目标正槽为
\[
 \boxed{H_{+,r}^{[0]}=\mathscr S_p(r)/\sqrt{p+1}.}
 \tag{I19}
\]
raw 幅度 C 已在 \(c_0\) 中，不能在(I19)再乘一次 C。

斜率由(I17)真正求导。它含 \(N'P+NP'\) 和
\((\log U_*)NP\)；原 full output weights的导数必须
同时按(I7)、(I12c)保留。在左端写回原输入时就是
\[
 \sum_{i,t}\{\Lambda_{1;i,t}^{(r)\prime}(-2)M_{A_{i,t}}(-2)
              +\Lambda_{1;i,t}^{(r)}(-2)M_{A_{i,t}}'(-2)\}.
 \tag{I20}
\]
因 \(\nu_r\) 在选定分量是有限固定角色，其导数为零；
(I12c)的 \(\mathfrak j_{h_i}'\)、\(\mathfrak j_t'\) 全部保留。
采用非紧代表时，(I12d)的 Norm/Hodge两项也须先完整运输再相消。
这些费用已由同一恒等式进入(I17)，不能再删一次，也不能在
右端额外重计一次。任何另添的 \(w_i(j)\) 必须按(I12d)后的
明确范围重算，不把它无声吞入常数。

### 9.6. tame-zero为何删掉已知最低层

在原 canonical seed 中，负来源首阶4、正来源首阶6。
正整数槽为 \((n,n+2)\)。
对 physical tame \(a\in\mu_{p+1}\)，两个各自的最低 residue
权同为
\[
 a^{4-n},\qquad a^{6-(n+2)}=a^{4-n}.
\]
在临界合法分量 \(n\equiv-2\bmod(p+1)\)，二者均为 \(a^6\)。
当前 \(p+1>6\)，所以各自 tame-zero 平均为零。
原反向 paired graph中这两个权可相消，因此 R1062 G17的
Norm 纤维值可非零；(I2)以后已不保持这种相关求和。
这就是 G17不能直接证明(I19)非零或为单位的具体原因。
R1063的全 Miller--Hall 后继层正是需要读取的实际余项，
而不是给更多独立 canonical 零行。

### 9.7. 同一个整 Rubin 系数给出的严格门

最后保持 R716 和原 first-wild Rubin 笔记的整基。
令
\[
 A_p(T)\in\mathcal O_{K_p}[[T]],\qquad \mu(A_p)=0,
 \qquad e=\operatorname{ord}_{u=0}J_p(u).
\]
原比较已付
\[
 \operatorname{ord}_{T=0}A_p=2e,\qquad
 v_p([T^{2e}]A_p)=2v_p([u^e]J_p)-2e .
\]
对本节同一个 \(\nu_r=\widetilde\eta_r\)，取
\(t_{\nu_r}=\nu_r(\gamma)-1\)。原 R716 的完整平方及 Rubin
integral-basis 比较给
\[
 \boxed{
 v_p A_p(t_{\nu_r})
       =2v_p\mathcal T_{34,T_r},
 \qquad
 v_p(t_{\nu_r})=\frac1{p-1}.
 }
 \tag{I21}
\]
原 Hall trace \(\mathcal T_{34,T_r}\) 与
\(\mathscr S_p(r)\) 的准确 root phase是单位；
二者估值相同。这里不是另一个正则化函数或另选的 Iwasawa
变量。

整系数逐项估值立即给
\[
 v_p\mathcal T_{34,T_r}\ge\frac e{p-1}.
\]
因此
\[
 \boxed{
 J_p'(0)=0\ \Longrightarrow\
 v_p\mathcal T_{34,T_r}\ge\frac2{p-1}
 \quad\hbox{对所有原 }r\ne0 .
 }
 \tag{I22}
\]
反过来，只要某个原 r 被证明满足严格界
\(v_p\mathcal T_{34,T_r}<2/(p-1)\)，就排除原 canonical 坏条件。
若精确为 \(1/(p-1)\)，则 \(A_p\) 的二次系数为单位，
且原 \(J_p'\) 的估值为1。
这比“Hall 非零”强；后者本身不足以排除四阶中央零。

若 first-wild Hall 值为零，原精确同变量身份给
\(\Phi_p(1+T)\mid A_p(T)\)；
再有 \(J_p'=0\) 时原 \(\lambda_p\ge p+3\)。
现有 \(\mu=0\) 并不排这个范围。
故(I16)--(I20)支付的是同一来源的真实 Hall 两槽和全部临界
费用，(I22)支付的是主门所需的准确数值目标；本文没有声称
所需严格上界已经由最低 Norm 层得到。

### 原始依赖

- R716，原 wild 全局 theta period 与准确中央 L 值，特别(23)--(36)。
- 原 first-wild Rubin note：
  notes/2026-11-15-original-first-wild-rubin-factor-and-central-order.md。
- 原 psi4 source：
  notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md，
  §§7、10--11 的完整 raw 幅度。
- 原 unsquared source：
  notes/2026-11-27-original-unsquared-toric-theta-source-and-newton-pullback.md，
  §§10--11 的正常序及未平方 seesaw；未使用该文已条件化的旧 usual/flat 应用。
- R1054 §§8--10；R1059 全临界 germ；R1060 全有限转置与实际 graded 比较。
- R1061 §§21--22(E/F)；R1062 G1--G14；
  R1063 原 Miller--Hall 精确根与五层归一。

## 10. 原负二 Hall 的全部首剩余窗与同一 Newton 长 jet

本节使用 L 标签。保持本篇(H1)–(H27)、(J1)–(J10)和§9
的实际来源、中心、模型比较、Haar 及完整外权。新结论把原五层
比较扩大到实际首挠点环的整个模 \(p\) 窗，并列出末层唯一的
连接修正。这里不增加任何 canonical 坏条件。

### 10.1 严格 LT 微分与 zeta 的一次分母相消

仍置 \(q=p^2,\Delta=q-1,d=p+1\)，使用原严格坐标
\([p](v)=pv-v^q\)。令 \(g(v)=z'(v)\) 为不变微分的系数。
它在原好模型的整形式群中属于
\(1+v\mathcal O_L[[v]]\)。对
\(z([p]v)=pz(v)\) 微分，得
\[
 g(v)=(1-pv^\Delta)g(pv-v^q).
\]
约化后 \( \bar g(v)=\bar g(-v^q)\)；
若存在最低正次数，它在右侧的次数会扩大 \(q\) 倍，矛盾。
再用严格 LT 的 \(\mu_\Delta\) 型，准确得到
\[
 \boxed{g(v)\in1+pv^\Delta\mathcal O_L[[v^\Delta]],
 \qquad D=g(v)^{-1}\partial_v\equiv\partial_v\pmod p.}
 \tag{L1}
\]

令
\[
 \Xi_v(v)=\Xi(w(v))
       =v^{-1}+\sum_{n\ge1}\xi_n v^n .
\]
(H8)已经证明它在所有实际非零首挠点满足
\(\Xi_v(v_Q)=Z_Q\)。其导数是同一整 Laurent 函数
\[
 \partial_v\Xi_v=-x(v)g(v).
\]
因此 \(n\xi_n\in\mathcal O_L\)，并且只在
\(n\equiv-1\pmod6\) 有项。

复用 R887§11（(47)前，引用R856(6)、(21)）的原特征 \(p\)
\(D^{p-1}x=-c_p\) 常数身份。由(L1)，在完整局部约化中
\(\partial_v^{p-1}\bar x\) 是常数。
所以 \([v^{kp-1}]x(v)\equiv0\pmod p\) 对 \(k\ne1\) 成立。
当 \(v_p(n)=1,\ n=kp\ne p\) 时，\(k\) 是单位，
而 \(g\equiv1\pmod p\)，故
\[
 \boxed{\xi_n\in\mathcal O_L
       \quad\text{若 }v_p(n)\le1,\ n\ne p;\qquad
       v_p(\xi_n)\ge-v_p(n)\quad(n\ge1).}
 \tag{L2}
\]
这是在原严格坐标中的系数结论。它解释了原 \(7p,13p,\ldots\)
的一次分母为何相消；没有另选一个 zeta primitive。

置
\[
 \kappa_*:=dp c_\sigma,\qquad
 c_\sigma=[z^d]\log(\sigma/z).
\]
由于 \(z(v)=v+O(v^q)\)，在次数 \(p<q-2\) 精确有
\(\xi_p=dc_\sigma=\kappa_*/p\)。
原 Hasse 归一给 \(\kappa_*\in\mathcal O_L^\times\)，且
\(\kappa_*\equiv\kappa_0\pmod p\)。
这里的 \(\kappa_*\) 是原指定系数，不替换为任意同余单位。

若 \(v_p(n)=a\ge2\)，\(\mu_6\) 型使最小可能的正 \(n\)
至少为 \(5p^a\)（\(a\) 偶）或 \(p^a\)（\(a\) 奇）。
结合(L2)及 \(v_p(v_Q)=1/\Delta\)，这些全部高分母项收敛，
且比下式显示的余界更深。于是
\[
 \boxed{
 Z_Q=\frac{\kappa_*}{p}v_Q^p(1+\epsilon_Q),
 \qquad v_p(\epsilon_Q)\ge
 \eta:=1-\frac1{p-1}.
 }
 \tag{L3}
\]
最低余项来自 \(\Xi_v\) 的 \(v^{-1}\)：
其相对估值为
\(1-(p+1)/\Delta=\eta\)。
其它整项至少从 \(v^5\) 起；高分母项按上述 \(a\) 分类全部保留。
这把(H9)的粗界加强到同一个实际 \(Z_Q\) 的完整界。

### 10.2 完整 h-gauge 消去及其真正的下一项

保持
\[
 h(v)=v/T_{\rm g}(w(v)),\qquad f_N=h^NR_N,
 \qquad N=102,\quad f_N\in v^4\mathcal O_L[[v]].
\]
定义实际连接余项
\[
 \Gamma(v):=\Xi_v(v)-D\log h(v)-\frac{\kappa_*}{p}v^p.
 \tag{L4}
\]
不能把(L4)只写成 \(D\log E_{\rm c}\)：
准确的形式恒等式是
\[
 \Xi_v-D\log h
 =D\log(z(v)/v)+D\log E_{\rm c}(z(v)).
\]
其中两个式子在 \(v^{q-2}\) 可以分别出现一次分母，
但它们的真实和由(L2)及整 \(D\log h\) 支付。

原 \(E_{\rm c}\) 只含 \(z^d\)，
\(z(v)/v\) 只含 \(v^\Delta\)，故(L4)是 \(\mu_d\) 型 \(-1\)。
它没有极项；其 \(v^p\) 项已经准确减掉。
因此首个可能次数为 \(2d-1\)。
\(D\log h\) 是整 Laurent 级数，故(L2)同样控制(L4)的
全部高系数。对所有实际 \(Q\ne O\)，得到
\[
 \boxed{v_p(\Gamma(v_Q))\ge(2d-1)/\Delta.}
 \tag{L5}
\]
例如 \(a=2\) 的高分母项估值至少
\(5q/\Delta-2\)，而 \(a\ge3\) 的估值至少
\(p^a/\Delta-a\)；二者均严格高于(L5)。
这里无需在首挠点代入不收敛的裸 sigma 级数。

用 R1062(G4)–(G8)的同一函数：
\[
 \mathcal F_{N,Q}(-2)
 =1-\frac{2}{NZ_Q}\frac{DR_N(Q)}{R_N(Q)}
       +O_{\ge2\eta}.
\]
这一式保完整第一个落阶项；其余项的界来自
\(\binom{-2}{k}=(-1)^k(k+1)\) 及原 \(a_{Q,k}\) 的
\(k\eta\) 界，不用新的有限截断假设。
将它与(L3)的逆平方一起展开，准确的一次修正为
\[
 \begin{aligned}
 f_N(v_Q)&-\frac{2p}{N\kappa_*}v_Q^{-p}Df_N(v_Q)\\
 &-\frac{2p}{\kappa_*}v_Q^{-p}\Gamma(v_Q)f_N(v_Q).
 \end{aligned}
 \tag{L6}
\]
这是因为
\[
 \Xi_v-\kappa_*v^p/p+\frac1N D\log R_N
       =\frac1N D\log f_N+\Gamma .
\]
所以 h 的全部导数确实相消；没有先删掉 \(T_{\rm g}\)。

### 10.3 在实际首挠点环中的完整模 p 比较

令 \(\mathcal O_H\) 为原首挠点域的 Hall 固定整数环。
避开既定有限常数域的坏位后，
\(\mathcal O_H=\mathcal O_0[W]\)，
\(W=v_Q^d,\ W^{p-1}=p\)，\(\mathcal O_0\) 在 \(p\) 非分歧。
所有中心先按(H16)提出来，剩余式确在这个 Hall 固定环中。
以下同余是在 \(\mathcal O_H/p\)，
即实际的 \((\mathcal O_0/p)[W]/(W^{p-1})\) 中，
不是自由形式变量 \(W\) 上的无界断言。

按本篇原来源定义
\[
 \mathcal P_-(W):=
 \frac{N^2\kappa_*^2W}{\mathscr C_{N,T}p^2}
              \mathcal H_-^{[-2]}(T).
\]
(L3)–(L6)表明该值整。
归一后的二次及以上余项估值至少
\[
 \frac{5-p}{\Delta}+2\eta
       =\frac{2p^2-3p+1}{\Delta}>1.
\]
\(\Gamma\) 项由(L5)给至少 \(1+6/\Delta>1\)。
(L1)允许把一次导数 \(D f_N\) 换成 \(\partial_v f_N\)；
其误差也严格高于1。全部这些余项仍在同一个 Hall 固定环。

写 \(b_{-,j}=[v^{(j+1)d-2}]f_N\)，即(H19)的真实系数。
Hall 正交逐项给
\[
 \frac1d\sum_{h\in\mu_d}v_{hQ}^{d-2p}f_N(v_{hQ})
        =\mathcal B_-(W),
\]
\[
 \frac1d\sum_{h\in\mu_d}v_{hQ}^{d-3p}
           \partial_vf_N(v_{hQ})
   =W^{-1}\{(d-2)\mathcal B_-(W)+dW\mathcal B_-'(W)\}.
\]
于是完整结论为
\[
 \boxed{
 \begin{aligned}
 \mathcal P_-(W)
 &\equiv\mathcal B_-(W)
 -\frac{2p}{N\kappa_*}W^{-1}
       \{(d-2)\mathcal B_-+dW\mathcal B_-'\}\\
 &\equiv\mathcal B_-(W)
       -\frac{2(p-1)}{N\kappa_*}
                      b_{-,0}W^{p-2}
       \pmod{p\mathcal O_H}.
 \end{aligned}}
 \tag{L7}
\]
原负二 primitive 至此保到整个首剩余窗。
它的最后一层并不一般为零；(L7)明确给出了该层连接修正。
若改回(H20)的 \(\kappa_0\) 显示方式，须保
\((\kappa_0/\kappa_*)^2\) 的真实常数；
它模 \(p\) 为1，所以不改变(L7)。

正 Hall 保(H23)的精确式和(H24)的
\(W_+=\widehat3 W\)。令
\(\mathcal P(W)=\mathcal B_{34}(\widehat3W)\mathcal P_-(W)\)。
原 paired 值准确是它乘
\[
 \Omega_A^3\rho_A^{-2}\,
 \frac{d\,c_0^{(0)}L_-^{-2}\widehat3}
             {102^2\kappa_*^2}\,
 \mathscr C_{102,T}\mathscr C_{34,T_+};
\]
这是(H25)、(H26)、(I18a)的同一 Haar 与 E0 frame，未改
\(c_0^{(0)}=\vartheta^{-10}c_0,\ L_-=\vartheta\ell_-\)。
因此
\[
 \boxed{
 \mathcal P(W)\equiv
  \mathcal B_-(W)\mathcal B_{34}(\widehat3W)
 -\frac{2(p-1)}{102\kappa_*}
       b_{-,0}b_{+,0}W^{p-2}\pmod p .
 }
 \tag{L8}
\]

### 10.4 原 Newton 两个端点尾与 p−2 阶除 p jet

本节继续(J1)的同一个 \(J_-,J_S,K_-,L_S\)。
对全部 \(0\le r\le p-2\)，仍准确有
\[
 \boxed{
 \frac{K_-^{(r)}(0)}{r!p^r}
       \equiv \frac{g^-_{r+1}}{\gamma_-^{r+1}},\qquad
 \frac{L_S^{(r)}(0)}{r!p^r}
       \equiv \frac{g^+_{r+1}}{\gamma_+^{r+1}}
       \pmod p .
 }
 \tag{L9}
\]
这里须支付(J2)五阶范围之外的尾端，而非直接外推。

原 \(1\le h\le p-1\) 的全部整窗仍给 \(p^h\)；
\(h=p\) 给 \(p^{p-1}\)；
\(p+1\le h\le2p-2\) 给 \(p^{h-2}\)。
除去 \(pu\) 后再除 \(p^r\)，仅 \(r=p-2\) 时的
\(h=p,p+1\) 可能未自动多一位 \(p\)。
但它们的真实多项式满足
\[
 \frac{(u)_p}{u}\equiv u^{p-1}-1,\qquad
 \frac{(u)_{p+1}}u\equiv u^p-u\pmod p .
\]
两者的 \(u^{p-2}\) 系数都是0，恰给所需的额外一位。
对全部 \(h\ge2p-1\)，必须用同一原来源的较强实际盘，
而不能仅外推本篇§8.1的短 jet 叙述。
令 R618(12)的
\[
 \tau_2=\frac{2p-1}{p(p^2-1)},\qquad
 R_2=p^{-\tau_2},\qquad
 \eta_p=1-d\tau_2>0,\qquad
 U=(\sigma/z)e^{-c_\sigma z^d}.
\]
原单参数 Newton 注(7)准确给
\[
 z^2D_-e^{-102c_\sigma z^d}
 =z^6U^{102}\sum_{\ell=0}^{16}
     u_\ell z^{6(16-\ell)}W_0^{3\ell+1},
 \qquad W_0=z^2x,\quad u_{16}=1.
\]
全部 \(u_\ell\) 在当前素数处整，所有显示次数非负。
这里的 \(W_0\) 与本节首挠点 \(W=v_Q^d\) 不同。
原 \(Se^{-34c_\sigma z^d}\) 也准确为 \(z^6U^{34}\)
乘整的非负 \(z^6,W_0\) 幂多项式。
R618§§4–5已付：在每个严格内闭盘 \(R<R_2\)，
\(U,W_0\) 范数至多1。因此这两个**实际**分子的范数
至多 \(R^6\)，包括负侧原 charge102 和首阶4经 \(z^2\)
补齐的全部费用。
对每个系数取 \(R\uparrow R_2\)，再乘原 \(C_\pm^{-h}\)，得
\[
 v_p(a_h),\,v_p(b_h)\ge
       \left\lceil h\eta_p+6\tau_2\right\rceil
          \qquad(h\ge1).
\]
这只是消费 R618 同一原 \(U\) 的内盘范数，
不把102次来源额外断言为新的最大半径。
在 \(h=2p-1\) 处，括号精确为
\[
 (2p-1)\eta_p+6\tau_2
 =2p-5+\frac{11p-7}{p(p^2-1)};
\]
故其 ceiling 为 \(2p-4\)，此后随 \(h\) 单调且趋于无穷。
\((u)_h/u\) 的全部系数整，所以对 \(r\le p-2\)，
整个 \(h\ge2p-1\) 尾在除去 \(p^{r+1}\) 后至少有
\[
 2p-4-(r+1)\ge p-3\ge1
\]
位 \(p\)，并一致收敛。
特别 \(h=2p-1\) 的 \(u^{p-2}\) 系数虽模 \(p\) 非零，
其真实 \(a_h,b_h\) 仍已足够深。
这证明(L9)，包括实际端点和全部无限尾。

定义
\(\operatorname{Jet}_{p-2}^{[p]}F(X)
=\sum_{r=0}^{p-2}F^{(r)}(0)X^r/(r!p^r)\)。
只在模 \(X^{p-1}\) 下使用它；这不是把 \(F(X/p)\)
免费延长到新解析盘。Leibniz 仍给这个有限 jet 的乘法性。

本次坐标比较也仍在实际整窗内：负侧最大所读次数为
\((p-1)d-2=q-3\)，正侧为 \((p-1)d=q-1\)。
准确的 \(z(v)=v+O(v^q)\) 和
\(f_N=(v/z(v))^NE_{\rm c}(z(v))^{-N}F_N(z(v))\)
表明，负、正来源首阶分别为4、6时，
这两个坐标误差首次在 \(q+3,q+5\)；
故均不进入所读窗口。
这里只用特征零形式次数，没有把 \(v^q\) 的原一次分母认成单位。

原 \(\mathcal B_-,\mathcal B_{34}\) 的全部系数整，故先在形式级数中取模 \(W^{p-1}\)，再代实际 \(W^{p-1}=p\)，准确决定模 \(p\) 的值。这里不把 \(E_{\rm c}\) 的各非整高项分别在边界求值或删掉；下面只比较完整乘积的有限系数。

在此窗口只需 \(f_2,\ldots,f_{p-2}\)，其中
\(f_j=[z^{jd}]\log(\sigma/z)\)。
R614 的真实分母 \(jd(jd-1)\) 在
\(2\le j\le p-2\) 都为单位，且 \(js<(q-1)/6\)，
故这些系数全整。
不使用首个端点 \(f_{p-1}\) 的整性。
令
\[
 U_{p-1}(W)=
 \exp\!\left[-\sum_{j=2}^{p-2}
          (102+34\widehat3^{\,j})f_jW^j\right]\pmod{W^{p-1}} .
\]
这里所有实际阶乘小于 \(p\)，所以这是常数1的整单位。
(J5)–(J9)的全部系数证明随(L9)准确给
\[
 \overline{\mathcal B_-\mathcal B_{34}(\widehat3W)}
 =-\bar\gamma_+^2\bar U_{p-1}(W)
       e^{\bar\lambda_\delta\bar\gamma_-W}
       \overline{\operatorname{Jet}_{p-2}^{[p]}
                      \mathcal A_{\rm can}}(\bar\gamma_-W)
        \pmod{W^{p-1}},
\]
其中 \(\lambda_\delta=\log q_\delta/p\) 和
\(\mathcal A_{\rm can}=-3q_\delta^{-u}K_-L_S\) 都仍为(J8)原值。
由 \(\gamma_-=3\gamma_+\)、\(102\kappa_*=d\gamma_-\)，
(L8)最终成为
\[
 \boxed{
 \begin{aligned}
 \overline{\mathcal P}(W)
 ={}&-\bar\gamma_+^2\bar U_{p-1}(W)
       e^{\bar\lambda_\delta\bar\gamma_-W}
       \overline{\operatorname{Jet}_{p-2}^{[p]}
                   \mathcal A_{\rm can}}(\bar\gamma_-W)\\
 &-\frac{2\bar\gamma_+}{3}\,
          \overline{\mathcal A_{\rm can}(0)}\,W^{p-2}
       \qquad\text{于 }(\mathcal O_0/p)[W]/(W^{p-1}).
 \end{aligned}}
 \tag{L10}
\]

### 10.5 首个实际未消项与原坏条件

原必要条件仍仅为 \(J_S'(0)=0\)。它给
\(\mathcal A_{\rm can}(0)=0\)，并由(L9)给
\(b_{+,0}=s_{p+1}\equiv0\pmod p\)。
因此(L10)中的末层连接修正和首层同时消失；
其余 \(p-2\) 个有限 jet 没有被赋零。

若在同一实际输入上，\(1\le k\le p-2\) 是
\[
 \overline{\mathcal A_{\rm can}^{(k)}(0)/(k!p^k)}\ne0
\]
的首个位置，则所有已显示单位的常数项都为1，
所以原归一 paired Hall 的首层系数准确为
\[
 -\bar\gamma_+^2\bar\gamma_-^{\,k}\,
       \overline{\mathcal A_{\rm can}^{(k)}(0)/(k!p^k)}.
\]
在实际 \(W^{p-1}=p\) 上，其估值严格是 \(k/(p-1)\)。
若整个有限 jet 都为零，本节只给该归一读数属于 \(p\mathcal O_H\)。

这支付了全部首剩余窗及唯一末层修正，
并把首个未消项定位在同一个 canonical Newton 函数中。
它没有证明该位置必为0或1，也不把 paired 估值替换成
R716 的单 Hall 严格阈值。
原 fixed sources、所有 finite/\(h\)/Artin/Cor、真实 period、
\(\Lambda,\Lambda'\) 和 old 列仍按前文保留。
本节全部为原完整来源的手证，没有新增数学运行或素数扫描。
