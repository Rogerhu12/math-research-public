# R1063 — 原 tame-zero Hall 投影与完整 Miller 负二读数的前五层

日期：2026-11-28。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：本篇支付同一实际 Hall 角色、Miller 中心、严格 LT 坐标和负二连接高项的五层返回。正源保持原 canonical $S$，负源保持两个三挠 Weyl 词完整相加的 $D_{102}$。这里的 tame-zero 输出是为对准 R716 原 Hall covector 而明确施加的新操作；不声称它已经包含在 R1061(C18) 的未投影来源内。整个 non-$p$/$h$/Artin 来源到这两条来源的接合另须逐字保留，不能由本篇的单字式替代。**

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
