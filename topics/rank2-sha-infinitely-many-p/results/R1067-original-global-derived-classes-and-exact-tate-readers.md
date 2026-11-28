# R1067 — 原全域派生类与无损 Tate 读者（§98 起）

会话：Astra-rank2-Sha-0b097461-20261127。**以下各命题已证明；主目标未完成。**

本卷续 [§§74–97](R1067-original-signed-kummer-specialization-and-finite-power-tests.md)；
该卷已接近单文件上限，全部原文、参数和更早各卷索引均保持。
原 E17、signed 反圆分变量、全部驯角色、primitive Euler 及绝对周期一律沿用。
新全域读者须保持真实局部类的精度及全局障碍，不将条件接口写成无穷素数非零。

## 98. 原二阶 Kummer 类的显式反限制、无损 Tate 读者与全局障碍

**已证明。** 沿 §§74–75 的原始相容 CM/Tate 基，取
$\Phi=K_p$、$\mathcal O=\mathcal O_\Phi$、
$W=T_\pi^{-1}(1)$，其 $\mathcal O$ 线性 Tate 对偶为 $T_\pi$。
令 $a_2=[T^2]\mathcal A_p$、$\xi_0=\xi_1|_{T=0}$、
$u=6fH^{\rm ac}(0)\in\mathcal O^\times$。
若 §75 采用归一 $\Delta$ 迹，下文的类和实际限制式同时乘该已知单位。
(AP1)及 $\mathcal A_p\in T^2\Lambda$ 给真正基域类
$C=ua_2\xi_0\in H^1(\Phi,W)$。
对 $R_k=(\mathcal O/p^k)[X]/X^3$，底线
$W/p^k\to W\otimes R_k,\ w\mapsto X^2w$ 是等变映射；
反圆分作用 $(1+X)^{-s}$ 在此底线上为一。
§75(AQ2)的 $H^0/H^2$ 消失使该映射在 $H^1$ 单射。
所以 $d^{\rm ac}$ 的三阶有限像正是 $X^2C_k$，$C_k=C\bmod p^k$。

令 $H_k=G_{\Phi_{k+1}}$，按固定 Tate 基把(AQ3)实际二次
Kummer 元素 $Y_k$ 写成同态 $y_k:H_k\to W/p^k$。
其常、一次项为零，故 $y_k=\operatorname{res}C_k$。
这是原 $a^{-1}$ 及全部驯标记的限制，不是另一个有限群和。
不同 $\Delta$ 迹习惯只使 $y_k,C_k$ 同乘相同可逆因子。

取 $-1\in(\mathcal O/p^{k+1})^\times$ 的任意 $G_\Phi$ 提升 $d$；
也可在完整相容 Tate 塔固定同一个提升。它在 $T_\pi$ 上为
$-1$，在 cyclotomic $(1)$ 上为 $N(-1)=1$，因而在 $W/p^k$
上为 $-1$。商群阿贝尔，故
$[d,g]=dgd^{-1}g^{-1}\in H_k$。
$C_k$ 的 cocycle 代表中恰有一个满足 $c_k(d)=0$，因为改余边界
使该值改变 $(\rho(d)-1)v=-2v$。比较
$dg=[d,g]gd$ 的 cocycle 值，得到准确反限制
$$
 \boxed{\quad c_k(g)=-\frac12\,y_k([d,g])\qquad(g\in G_\Phi).\quad}
 \tag{BN1}
$$
只除以二，没有除塔次数；换提升只改变规范代表，固定提升时各
$k$ 相容。因而可由实际 $Y_k$ 恢复同一基域类的所有精度，
无需取会吞掉精度的固定低层范数。

取 $\mathcal O$ 值 Tate 配对
$$
 B_k:H^1(\Phi,W/p^k)\times H^1(\Phi,T_\pi/p^k)
               \longrightarrow\mathcal O/p^k .
$$
先用 $\mathcal O$ 线性评价
$W\otimes_{\mathcal O}T_\pi\to\mathcal O(1)$，
再用 $\operatorname{inv}_\Phi\otimes\mathcal O$。
等价地，按 $\mathcal O/\mathbf Z_p$ 的迹对偶基保留两个普通杯积。
$\Phi/\mathbf Q_p$ 未分歧，迹对偶不损整度；只取一个普通迹
可能遗漏 $\mathcal O$ 分量，不能替代此配对。
相容极限 $B$ 与 Bloch–Kato exp/dual-exp 对偶，对形式点 $P'$ 给主理想
$$
 \bigl(B(C,\kappa P')\bigr)
       =(a_2)\bigl(p^{-1}\log_{\omega_1}P'\bigr)\quad\text{于 }\Phi .
 \tag{BN2}
$$
确实 BKO Proposition 3.1, (3.3) 在 $n=0$ 给
$$
 \exp^*\xi_0
 =\frac{L_{pf_1}(E_1,1)}{\varpi_1}\omega_1
 =\left(1+\frac1p\right)\frac{1-\omega_K}{6}\,\omega_1 .
$$
R303 (15)给原 primitive 参考值，惰性
$\psi_1((p))=-p$ 的 $p$ Euler 因子不可删。
$\kappa P'$ 对应的 exp 输入为 $\log_{\omega_1}P'$。
以所有 $b\in\mathcal O$ 乘第二变量，迹对偶恢复完整
$\mathcal O$ 值；采用 BKO 共轭标号时同时共轭两格。
$u$、原对偶基及 $(1-\omega_K)/6$ 都是单位，故得到(BN2)。
外部输入见 A. Burungale–S. Kobayashi–K. Ota,
*p-adic L-functions and rational points on CM elliptic curves at inert primes*,
JIMJ 23 (2024), §3.1.1、Proposition 3.1, pp.1430–1431；
[原刊全文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)。

固定代数点 $Q=(3,2\sqrt7)\in E_1(\mathbf Q(\sqrt7))$ 在全部本节
$\Phi$ 中有嵌入；$\mathbf F_p^\times$ 的元素在 $\mathbf F_{p^2}$
中均为平方，且 $p\nmid14$。其七次二次扭曲上对应
$P=(21,98)\in\{Y^2=X^3+343\}(\mathbf Q)$，
$[2]P$ 的 $x=57/16$，由 Nagell–Lutz 得 $P,Q$ 非挠。
$\operatorname{Frob}_{p^2}=[-p]$ 使 $P'=[p+1]Q$ 落在形式盘。
当前未分歧位的形式对数单射，故它非零；(BN2)的精确费用为
$v_p(a_2)+v_p(\log P')-1$。这是同一个固定全局点，
局部额外整度可随 $p$ 改变。

若要每个 $k$ 完全不损原模数，可用同一明确代数配方
$$
 P_p^\star=(p^{-2},-p^{-3}\sqrt{1+p^6})\in E_1(\mathbf Q_p),
       \qquad\sqrt{1+p^6}\equiv1\bmod p .
$$
它是至多二次全局代数点的指定局部嵌入。
$t=-x/y=p/\sqrt{1+p^6}$，故
$\log_{\omega_1}P_p^\star\equiv p\bmod p^2$：
$\omega_1$ 的首项为 $dt$，其余积分项的赋值至少
$n-v_p(n)\ge2$，$n\ge2$。
(BN1)–(BN2)于是给同一原模数的充要读者
$$
 \boxed{\quad
 (B_k(c_k,\kappa_k(P_p^\star)))=(a_2\bmod p^k)
                     \quad\text{于 }\mathcal O/p^k .
 \quad} \tag{BN3}
$$
杯积及不变量在 $\Phi$ 取。若将双方同时限制到
$\Phi_{k+1}$ 再取当地不变量，值会乘塔次数，不能用于(BN3)。
这里没有证明这些符号在无穷素数非零。

最后说明不能把此非零候选直接改成其它坏位的贡献。
取原目标曲线的有理点 $P_{17}=(2,5)$；其倍点
$x([2]P_{17})=-64/25$，同样由 Nagell–Lutz 得非挠。
令
$C_{17}=(F_\theta^*)^{-1}C\in H^1(K_p,V_{17}')$，
其中 $V_{17}'$ 是 $T_pE_{17}$ 的 $\mathcal O$ 线性 Tate 对偶
张量 $\mathbf Q_p$。逆映射与配对用 R303 (9) 的同一整局部
同构。$B(C_{17},\kappa([p+1]P_{17}))$ 对应
$E_1$ 上 $F_\theta^{-1}P_{17}$ 的读者，原微分因子为单位，
形式对数非零。因此该特征零配对非零恰当 $a_2\ne0$。

对任意固定有限 $S$，包含 $p$、无穷及坏处，也允许任加有限
多个辅助位，有准确等价
$$
 a_2=0\quad\Longleftrightarrow\quad
 C_{17}\in\operatorname{im}
 \bigl(H^1(G_{K,S},V_{17}')\longrightarrow H^1(K_p,V_{17}')\bigr).
 \tag{BN4}
$$
若 $a_2=0$，取零全局类。反之，将假定提升与全局
$\kappa([p+1]P_{17})$ 作 Tate 乘积。有限 $v\nmid p$ 处，
$E_{17}(K_v)$ 有有限指数的 pro-剩余特征开子群，
所以其有理 $p$ 进 Kummer 像为零；$K$ 无实位。
$S$ 外无贡献，固定 $S$ 内全部非 $p$ 项为零。
全局不变量和为零，而惰性 $p$ 在 $K$ 只有一个素位。
故该唯一 $p$ 位的完整 $\mathcal O$ 值配对为零，得 $a_2=0$。
也可将第二点分别乘 $\mathcal O_K$ 的迹对偶两个基，恢复同一结论。

(BN4)只论各自有限分歧的有理全域提升；不交换不断增大的分歧集合
和无限局部求和。原 Robert 全域系统存在，但其非零二阶派生
局部类有这个真实全域障碍。后续若使用全局 Bockstein，必须保留它；
直接假定普通一阶全域提升会迫使待证读数为零。

## 99. 全域零次消失、真实一次派生类与紧支撑一级 Bockstein

**已证明。** 保持 §98 的原素数范围。现用目标曲线自身的
$T_{17}=T_pE_{17}$、$V=T_{17}\otimes\mathbf Q_p$、
$W=V^\vee(1)$，对偶在 $\Phi$ 上取。以 $U$ 表示反圆分增广参数，
避免与 Tate 格混淆。取 BKO Proposition 3.1 的全域标准椭圆单位
$Z\in H^1_{\rm Iw}(K_\infty/K,T_{17}^\vee(1))$，
其局部化是 R303 (16) 的 $\xi_{17}$。
不将仅局部为真的 $F_\theta$ 同构用于全域。
BKO (3.1)以 Weil 配对和复共轭在全域将
$T_{17}^\vee(1)$ 换成 $T_{17}$，并反演 $\Gamma$；
$U\mapsto(1+U)^{-1}-1$ 只以单位改变增广阶，最后按原坐标运输。

令 $\mathscr D=\Lambda_{(U)}$，这是留数域为 $\Phi$ 的 DVR。
按 Agboola–Howard II 的原惯例，$S_{\rm rel}$ 为紧 Tate 格的
relaxed 全域逆极限，$X_{\rm str}$ 为离散 strict Selmer 群之对偶，
$\mathcal C$ 为全部实际 twisted elliptic units 生成的子模。
其 Proposition 3.3 给
$S_{\rm rel}$ 无挠秩一、$X_{\rm str}$ torsion，以及
$$
 \operatorname{char}_\Lambda X_{\rm str}
       =\operatorname{char}_\Lambda(S_{\rm rel}/\mathcal C).
$$
原刊 §3 的 $\mathcal C$ 包含各辅助理想平滑的标准 Robert 系统。
R303 §4.1 取的好惰性 $\ell\equiv1\bmod p$，其辅助 Euler
在此反圆表示上为单位：惰性理想的反圆群元为一，原规范常项
模 $p$ 为二。故 $Z\in\mathcal C_{\mathscr D}$，相容 Betti
生成元仅带入单位；不要求一个辅助系统整生成全部 $\mathcal C$。

原两个有理独立点保证 $E_{17}(K)$ 的 $\mathcal O_K$ 秩至少二。
确实若两点有 $K$ 线性关系，清分母后将关系及其复共轭相减，
先消去虚部，再消去实部，便违反原有理独立性。
当地 $E_{17}(\Phi)\otimes\mathbf Q_p$ 是 $\Phi$ 维一，
因此基域 strict Selmer 中有至少一维可除的 Mordell–Weil
方向；可取当地对数核的整格再张 $\Phi/\mathcal O$，
或用普通与严格局部像的 corank 差。
又 $E_{17}(D_\infty)[p]=0$：$D_\infty/K$ 是 pro-$p$，
原惰性惯性在 $E[p]$ 上的非平凡 tame 标量不会消失。
膨胀限制使基域 strict Selmer 单射进入
$\operatorname{Sel}_{\rm str}(D_\infty)^\Gamma$。
于是 $X_{\rm str}/UX_{\rm str}$ 有正 $\mathcal O$ 秩，
$\operatorname{length}_{\mathscr D}X_{\rm str}\ge1$，
从而 $\mathcal C_{\mathscr D}\subset U S_{{\rm rel},\mathscr D}$。

清去常项非零的分母再特化，得 $Z_0=0$ 于有理全域 $H^1$。
其整版本亦为零，因为
$H^1(G_{K,S},T_{17}^\vee(1))$ 无 $p$ 挠；
这由同一非平凡 $\Delta$ 型给
$H^0(T_{17}^\vee(1)/p)=0$。
在原全域 Iwasawa 表示的 $U$ 乘法正合列中，
$H^0(T_{17}^\vee(1))=0$，因此有唯一整全域类
$Z'$ 满足 $Z=UZ'$。置 $z_1=Z'|_{U=0}$。
原局部 $\operatorname{loc}_pZ\in U^2H^1_{\rm Iw}$ 且当地
Iwasawa $H^1$ 无 $U$ 挠，故 $\operatorname{loc}_pz_1=0$。

对有限 $v\nmid p$，$V,W$ 的有理局部 $H^i$ 在 $i=0,1,2$
全为零：当地 $p$ 幂挠有限给 $H^0=0$，局部对偶给 $H^2=0$，
而剩余特征不同于 $p$ 的 Euler 特征为零，给 $H^1=0$。
任何有限反圆分喷流按过滤亦全部如此。故 $z_1$ 位于有理
全域 strict 核，具有唯一
$z_1^c\in H_c^1(G_{K,S},W)$；
无穷位使用 modified Tate 约定，当地 $H^0$ 同样不造成歧义。

在如今已证明的 Rubin 分解下，Agboola–Howard II
Theorem 4.2 及(4.1)给 $S_+=S_{\rm rel}$，并有
$$
 \operatorname{char}(X_{+,{\rm tor}})
 \operatorname{char}(H^1_+/\operatorname{loc}S_{\rm rel})
     =\operatorname{char}(S_{\rm rel}/\mathcal C).
$$
$H^1_+$ 是原当地 signed 自由秩一直线；Theorem 3.6 的
$S_{\rm str}=0$ 使这里的全域局部化为单射。
令
$A=\operatorname{length}_{\mathscr D}(S_{\rm rel}/\mathcal C)$、
$B=\operatorname{length}_{\mathscr D}(H^1_+/\operatorname{loc}S_{\rm rel})$、
$A_Z=\operatorname{ord}_{S_{{\rm rel},\mathscr D}}Z$。
于是 $B\le A\le A_Z$，且
$\operatorname{ord}_U\mathcal A_p=A_Z+B$。

还有 $B\ge1$。否则某个全域 relaxed 元素清去常项非零的分母后，
在平凡权有非零当地 $H^1_+(0)$ 值。R303 的真实参考
$\xi_{1,0}$ 经 $F_\theta$ 运输生成该线，dual-exp 非零；
§98 的原有理非挠点 $P_{17}$ 当地对数非零。
两者完整 $\mathcal O$ 值 Tate 配对非零，与全域互反矛盾。
该 signed 特化线确实嵌入全部当地 $H^1$，
由 BKO 整直和及(AQ2)的基变换保证。

$U$ 乘法长正合列使全域 Iwasawa $H^1/U$ 嵌入平凡权全域
$H^1$，在 $\mathscr D$ 清分母后仍成立。
若 $z_1=0$ 可再次在整个全域 $H^1$ 除以 $U$；
在非 $p$ 位有限喷流的有理局部群全部为零，
所以该商在 $\mathscr D$ 仍属于 relaxed 模。
因此 $z_1\ne0$ 恰当 $A_Z=1$。结合上述长度不等式得到
$$
 \boxed{\quad
 z_1\ne0\ \Longleftrightarrow\ A_Z=B=1
 \ \Longleftrightarrow\ \operatorname{ord}_U\mathcal A_p=2
 \ \Longleftrightarrow\ a_2\ne0 .
 \quad} \tag{BO1}
$$
此时通常完整 $\Sha[p^\infty]$ 有限，且
$X_{+,{\rm tor},\mathscr D}=0$。
也可独立由 $A\le1$、基域 strict 单射及当地维数至多一，
得到通常 Selmer 的 $\Phi$ 维数恰为二，从而完整结论成立。
这是一阶全域与二阶当地的准确等价，不是更弱条件的非零证明。

当 $z_1\ne0$，其 strict 线就是原 Mordell–Weil 的当地对数核，
在原独立点 $P_1,P_2$ 的基中形如
$\lambda_p(\log P_2\,P_1-\log P_1\,P_2)$。
若两个系数都为代数数，$p$ 进解析子群定理及点的
$\operatorname{End}(E)$ 独立性会使它们同为零。
尚未识别 $\lambda_p$ 为固定非零代数数，不能用那个显然非零的
对数核向量替代实际 $z_1$。

### 原二阶局部障碍的完整紧支撑配对

置 $R_n=\Phi[U]/U^n$，
$W_n=W\otimes R_n$ 扭以 $(1+U)^{-s}$，
$V_n=V\otimes R_n$ 扭以 $(1+U)^s$，
用 $[U^{n-1}]\operatorname{eval}$ 作完美对偶。
记 $Z_r$ 为真实 $Z$ 的 $r$ 阶像，则
$\operatorname{loc}_pZ_3=U^2C_{\rm std}$，
$C_{\rm std}=(F_\theta^*)^{-1}(a_2\xi_{1,0})$；
它与 §98 实际 $d$ 给出的类只差已知局部单位 $u$。
$Z_2$ 的全部实际局部化为零，故有唯一紧支撑提升 $Z_2^c$。
由 $0\to W\xrightarrow{U^2}W_3\to W_2\to0$ 的紧支撑连接，
$$
 \partial^cZ_2^c=\delta_{\rm loc}(C_{\rm std})
                           \in H_c^2(G_{K,S},W). \tag{BO2}
$$
取 cone 约定 $d(z,b)=(dz,\operatorname{loc}z-db)$。
以真实 $Z_3$ 的全域 cocycle 提升 $z$，以任意 $b_3$ 提升
各处的当地零化 $b_2$。则
$U^{-2}(\operatorname{loc}z_3-db_3)$ 在 $p$ 位代表
$C_{\rm std}$，其它位的类为零，直接给(BO2)。

对偶列为 $0\to V_2\xrightarrow U V_3\to V\to0$。
对实际 $P=P_{17}$ 或 $[p+1]P_{17}$ 及其全域 Kummer
cocycle $c_P$，以常数一阶 cochain 提升，取微分并除以 $U$，
得到准确二阶 cocycle
$$
 (g,h)\longmapsto
 \left(s(g)+U\binom{s(g)}2\right)\,g c_P(h).
$$
因为 $Z_0=0$，有 $Z_2^c=Uz_1^c$，
顶系数对偶仅保留这条 cocycle 的常项。
Poitou–Tate 的连接对偶，亦可由同一 cone 的 Leibniz 公式核得，
$$
 \boxed{\quad
 (B(C_{\rm std},\kappa P))
      =(\langle z_1^c,\ s\cup\kappa(P)\rangle_{\rm PT}).
 \quad} \tag{BO3}
$$
这里写 $\Phi$ 标量的主分式理想，消除整体 cone 符号习惯；
特别右侧准确非零当且仅当 $a_2\ne0$。
它保留真实全域一次类、固定有理点和普通一级 Bockstein，
没有假设二阶局部类可作为普通全域一阶类提升。

主要原文：A. Agboola–B. Howard,
*Anticyclotomic Iwasawa theory of CM elliptic curves II*,
Mathematical Research Letters 12 (2005), 611–622，
§2、Proposition 3.3、Theorems 3.6、4.2及(4.1)，
[作者原刊](https://web.math.ucsb.edu/~agboola/papers/bisi_mrl_2005.pdf)；
BKO §3.1.1–§3.1.2 的原全域类及共轭同构见 §98 的链接。
原文中 Rubin 分解当时列为 conjecture，本题所需分解已由 BKO
采用的证明支付，并非沿用未证假设。仍须对无穷多个 $p$
证明真实 $z_1$ 或(BO3)配对非零。

## 100. 固定103的全域一次Robert幂余数及由原Mordell点预选的辅助素

沿§99，$E=E_{17}$、$T_E=T_pE$、$W_0=\operatorname{Hom}_{\mathcal O}(T_E,\mathcal O)(1)$、$W=W_0[1/p]$，$U=\gamma-1$，$z_1=(Z/U)|_0$。取相容CM Tate基$e$，其作用角色为$\rho:G_K\to\mathcal O^\times$；$e^{-1}$是未加Tate$(1)$的对偶基。置$j=k+1$、$L_j=K(p^j\mathfrak f_{17})$、$B_j=\operatorname{Gal}(L_j/K)$、$\mathfrak f_{17}=(34\delta)$。该层含$E[p^k]$和$\mu_{p^k}$，且$s(G_{L_j})\subset p^k\mathbb Z_p$。

### 固定原函数、全部有限权及准确平滑常数

所有$p,j$用同一辅助理想$\mathfrak a=(103)$。按canonical pair $(\mathbb C/\mathfrak m,1\bmod\mathfrak m)$，$\mathfrak m=p^j\mathfrak f_{17}$，原Robert函数$\;{}_{\mathfrak a}\theta$由
$N\mathfrak a[0]-\sum_{R\in E[\mathfrak a]}[R]$及全部互素整数乘法的范数条件唯一规范。取实际逆值$u_j={}_{\mathfrak a}\theta(1)^{-1}\in L_j^\times$。复缩放到原格$\varpi_{17}\mathcal O_K$后，它是固定$E$上同一$\;{}_{103}\theta$在$\varpi_{17}/(p^j34\delta)$的逆值；格生成元的$\mu_6$变化与函数自然性同时运输。模数含多个不同素因子，所以$u_j$是全局单位，且在原射线塔范数相容。

明确采用Wan–Xiang–Xu附录A的一套算术Frobenius标号：$\rho(\sigma_{\mathfrak l})=\psi_{17}(\mathfrak l)$，目标$W_0$的角色为$\rho_{\rm targ}=\epsilon_{\rm cyc}\rho^{-1}$。其(A.141)是
$\;{}_{\mathfrak a}\mathbf z=(N\mathfrak a-\sigma_{\mathfrak a})\mathbf z$，
(A.143)的群环专化为$[g]\mapsto\epsilon_{\rm cyc}(g)\rho_{\rm targ}(g)^{-1}=\rho(g)$。
理想$(103)$实，反圆pro-$p$投影平凡；$103\equiv1\bmod34\delta$给
$\psi_{17}((103))=103$。故**整条原反圆线**的平滑算子为
\[
 b=103^2-103\in\mathcal O^\times\qquad(p>211).
\]
这正是§99同一个未平滑标准$Z$：Kato §15.5以相同逆Robert值定义源，§15.6中(15.6.3)之前的定义除去$N\mathfrak a-\operatorname{Art}_{\mathfrak a}$；Proposition 15.9在每个有限反圆层、全部有限角色及同一Betti基下给BKO Proposition 3.1所引用的原互反式。因此可直接取BKO的Kato构造，非仅寻找一个有相似局部值的类。Kato(15.9.1–2)还直接给平滑因子$N\mathfrak a-\psi(\mathfrak a)\chi(\mathfrak a)^{-1}$，在此即$b$；见[原刊§15.5–15.9](https://archive.numdam.org/item/AST_2004__295__117_0.pdf)。

**原位更正。** R303 §4.1的惰性辅助素数因子写成$\ell^2+\ell^{-1}$是该明确目标角色下的误值，应为$\ell^2+\ell$。对其全部混合权，$\epsilon_{\rm cyc}/(\psi^{-(2m+1)}\epsilon_{\rm cyc}^{m+1})$在$(\ell)$的值恒为$-\ell$，所以原算子准确给$\ell^2+\ell$。本次同时改正R303该行并保留更正说明；原用$\ell\equiv1\bmod p$，两个数皆模$p$为二，既有单位性与相对赋值结论不受影响。此处没有用新文的秩一BSD结论。[Wan–Xiang–Xu全文](https://arxiv.org/html/2611.29641v1)的(A.135)、(A.137)、(A.140)–(A.145)只作相同原源及角色方向的交叉核对。

将$u_j$的Kummer类配$e^{-1}$，corestrict到$K$，取$(1+X)^{-s}$与$X^2=0$，再限制回$L_j$。Mackey的常项为$bZ_0=0$，一次项为
\[
 Y^g_k=-\sum_{a\in B_j}\rho(a)^{-1}s(a)[a]u_j
 \in \bigl(L_j^\times/(L_j^\times)^{p^k}\bigr)
                  \otimes_{\mathbb Z/p^k}(\mathcal O/p^k). \tag{BP1}
\]
单位群采用加法记号。Tate$(1)$由单位Kummer本身给出，不再乘范数。全射线群的驯部分和$p$两方向均保留；$j=k+1$保证角色和反圆指数确切通过该层。再乘原$e^{-1}$，其Kummer同态正是$\operatorname{res}(bz_1\bmod p^k)$。$B_j$阿贝尔，且存在在$W_0/p^k$上为$-1$的驯元素；Sah引理（或对该中央元素直接作余边界）给$H^1(B_j,W_0/p^k)=0$。所以(BP1)非零恰当$z_1\bmod p^k$非零。

用$\mathcal O$的$\mathbb Z_p$整基$(1,\delta)$，将
$\alpha_a=-\rho(a)^{-1}s(a)$写成$A_a+B_a\delta\bmod p^k$。定义
$U_0=\prod_a([a]u_j)^{A_a}$及
$U_1=\prod_a([a]u_j)^{B_a}$；整数提升只改$p^k$次幂。对避开坏位且在$L_j/K$完全分裂的素$v$及指定上方$w$，(BP1)在算术$\operatorname{Frob}_w$的两实际乘法坐标为
\[
 \bigl(\bar U_0^{(Nv-1)/p^k},\ \bar U_1^{(Nv-1)/p^k}\bigr). \tag{BP2}
\]
用$\mu_{p^k}$、$(1,\delta)$及$e^{-1}$回到$W_0/p^k$的同一$\mathcal O$坐标。一般$v$必须保两分量。Chebotarev作用于这两个实际单位Kummer扩张的正规闭包，给(BP1)非零等价于某$v,w$的(BP2)非平凡；这不证明该非零对无穷$p$发生。

### 仅由原两个点预先选择参考素

取原两个$\operatorname{End}(E)$独立有理点$P_1,P_2$（原秩证明见R294）。为不预借“生成全部$E(K)$”，置
\[
 M=E(K)/{\rm tors},\quad
 M_0=\mathcal O_KP_1+\mathcal O_KP_2,\quad
 M_{\rm sat}=M\cap(KP_1+KP_2).
\]
后两者是同一$K$平面的满格，指数有限。另去这个固定指数的素因子后，两点在$M/pM$的$\mathcal O_K/p$类独立：若组合落入$pM$，除$p$后的点仍在同一平面。两有理点的$\mathbb Q$独立蕴含$\mathcal O_K$独立，因将关系与复共轭相减可先消出虚部、再消实部。

令$m$是两个非零$\log_{\omega_{17}}([p+1]P_i)$的最小赋值，置
$\ell_i=p^{-m}\log_{\omega_{17}}([p+1]P_i)\in\mathbb Z_p$。至少一个$\ell_i$为单位，且
\[
 X_p=\ell_2\kappa(P_1)-\ell_1\kappa(P_2)
\]
是当地log为零的原始整全域类；原始性由上述模$p$独立和Kummer单射给出。沿BKO(3.1)的固定Weil/CM对偶及$K/\mathbb Q$复共轭，将它运输到$W_0$，记$X'_p$。具体，在$W$端的位$w$读它时，应将$T_E$端$cwc^{-1}$处的点值，以同一对偶基同构送回；Galois及系数共轭同时运输。反圆生成元取逆则一次派生另乘$-1$，整套选择同时改变。

存在唯一$\lambda_p\in\mathcal O$使
\[
                         z_1=\lambda_p X'_p. \tag{BP3}
\]
若$z_1=0$取$\lambda_p=0$。若非零，(BO1)已给通常Selmer的$\Phi$维数及$E(K)$的$\mathcal O_K$秩恰为$2$，通常全$\Sha[p^\infty]$有限。此时上述平面才是全部有理MW，严格线是其log核；整$z_1$与原始$X'_p$迫使系数整。$X'_p\ne0$本身不推出$\lambda_p\ne0$。

令$H=G_{K^{\rm ab}}$。它固定全部CM扭点。$\operatorname{Gal}(K^{\rm ab}/K)$阿贝尔且有在$E[p]$上为$-1$的元素，所以相应$H^1$为零；两个点的Kummer限制到$H$仍在$\mathbb F_{p^2}$上线性独立。联合像在原惰性惯性的全部$\mathbb F_{p^2}^\times$同时标量下稳定，故为$\mathbb F_{p^2}$子空间；没有非零线性关系使像为$\mathbb F_{p^2}^2$。闭加法像和Nakayama进一步给
$H\to T_pE^2$满射。

因而给定$k$，仅用$L_j$与两原点的$p^k$除点扩张就能预选$v,w$，使$X'_p(\operatorname{Frob}_w)$在$\mathcal O/p^k$中为单位。任一通过此参考门的素，无论未知目标的值为何，都有
\[
 (\mathrm{BP2})\text{ 经整基运输}
   =b(\lambda_p\bmod p^k)X'_p(\operatorname{Frob}_w). \tag{BP4}
\]
右侧两个参考因子均可逆，准确返回$\lambda_p\bmod p^k$。若
$\pi_v=\psi_{17}(v)\equiv1\bmod p^k$，点门可直接在有限域读：
\[
 \operatorname{Frob}_vR-R
   =[(\pi_v-1)/p^k]\bar P_i,\qquad[p^k]R=\bar P_i .
\]
按$\ell_2,-\ell_1$组合并验精确阶$p^k$；位及CM基依上文一起运输。没有预先选择任何未知目标单位的非平凡Kummer根。

### 固定两个参考自同构与准确的范数一单坐标

甚至可对全部所余$p$固定两个参考自同构。$H\to\prod_pT_pE^2$的闭像逐$p$满；任意有限组模幂的像由异素$p$群无公共非平凡商而满，紧性给整个乘积满。各$p$取固定复共轭$c$不动的$\mathcal O$-Tate生成元$e_p$：模$p$的半线性不动空间是一维$\mathbb F_p$，用$(1+c)/2$提升一个非零不动元即可。可选固定$h_1,h_2\in H$满足
$\kappa(P_j)(h_i)=\delta_{ij}e_p/2$，同时对所有$p$成立；这里只断言存在，不声称有有限字表达。

置$\tau_i=ch_i\in G_{\mathbb Q}$。因为$P_j$有理且$H$固定扭点，
$\kappa(P_j)(chc^{-1})=c\kappa(P_j)(h)$；由此
$\tau_i^2$固定$K^{\rm ab}$且
$\kappa(P_j)(\tau_i^2)=\delta_{ij}e_p$。
在$L_j$、$\mu_{102p^j}$和两点的$p^k$除点的$\mathbb Q$正规闭包中按Chebotarev选Frobenius共轭于$\tau_i$，再选上方素使代表正是$\tau_i$。有无限多个有理素$\ell$满足
\[
 \ell\text{惰性于 }K,\qquad
 \ell\equiv-1\bmod102p^j,\qquad
 v=(\ell)\text{在 }L_j/K\text{完全分裂}.
\]
此时$\pi_v=-\ell$，参考门只用$E_{17}(\mathbb F_\ell)$中的原两点和整数$-(\ell+1)/p^k$。两列中选对应单位$\ell_2$或$-\ell_1$的一列即可通过。两个原标量在$\mathbb F_{\ell^2}$内给
\[
 \left((\bar U_0^{\ell-1})^{(\ell+1)/p^k},
       (\bar U_1^{\ell-1})^{(\ell+1)/p^k}\right). \tag{BP5}
\]
其底数在范数一循环群。

这里可准确支付第二坐标。$\bar{\mathfrak m}=\mathfrak m$，canonical pair
$(\mathbb C/\mathfrak m,1)$在复共轭后对应同一pair；$(103)$的除子和全部范数规范也相同，唯一性给实际代数单位$cu_j=u_j$。又
$\rho(cac^{-1})=\overline{\rho(a)}$、$s(cac^{-1})=-s(a)$，所以
$\alpha_{cac^{-1}}=-\bar\alpha_a$。可选配对整数提升
$A_{cac^{-1}}=-A_a$、$B_{cac^{-1}}=B_a$；固定轨道的$s=0\bmod p^k$，取零提升。因此在$L_j$中准确有
$cU_0=U_0^{-1}$、$cU_1=U_1$。所选上方有理Frobenius在$L_j$恰为$c$，(BP5)进一步成为
\[
                \left((\bar U_0^{-2})^{(\ell+1)/p^k},1\right). \tag{BP6}
\]
先保全两整数分量，再以原pair和准确Frobenius证明这一分量可消；对一般$K$分裂素仍用(BP2)。

本节固定了103的原函数、全部整一次权、原两点、预先可验的参考素、共轭及每个整精度。仍须对无穷多个$p$证明某个$k$的真实第一幂余数非平凡，不能以参考点满性代替此目标。

## 101. 全部整精度的原循环邻曲线与第二位的真实加权单位

取§75的$k\ge1$、$j=k+1$，$A_j=(\mathcal O/p^j)^\times$及与§74同相容的$Q_j$。下面只用$[p]$生成循环子群，不改$\pi=-p$的Tate作用。以$\mathscr Y_k$表示(AQ3)用原$r_j$代$d_j$后的二次项。由(AP1)、(AQ2)及同一限制单射，
\[
 \mathscr Y_k=0\quad\Longleftrightarrow\quad
 [T^2]\mathcal A_p\in p^k\mathcal O .
\]
等式均在原$\Phi_j$的模$p^k$ Kummer群张量外部$\mathcal O/p^k$中；全驯标记可先在原未分歧分裂域作乘积，再按(AO1)下降。单位群用加法记号。

令$J_k=\{1+p^ki:i\in\mathbb F_p\}\subset A_j$。对$a\in A_j/J_k$任选提升，置
\[
 C_a=\langle[p^ka]Q_j\rangle_{\mathbb Z},
 \qquad\phi_a:E_1\longrightarrow E_1/C_a .
\]
$\langle[p^k]Q_j\rangle$是原相容第一层的有理线；商曲线仅依$a\bmod p$给出的$\mathbb F_p$线。准确有
\[
 \mathscr Y_k=e_\tau\sum_{a\in A_j/J_k}
  a^{-1}\binom{-s(a)}2
  \sum_t\varepsilon(t)\,
  \Theta_{E_1/C_a,(c)}
      \bigl(\phi_a(T_{t,j}+[a]Q_j)\bigr). \tag{BQ1}
\]
在$J_k$陪集上，$a^{-1}\bmod p^k$和反圆指数不变，内点遍历
$T_{t,j}+[a]Q_j+C_a$。任一阶素于$c$的循环子群$C$，将所有平移的$\Theta_{E,(c)}$相乘，所得除子等于商同源拉回的$\Theta_{E/C,(c)}$除子，因为同源在$E[c]$上同构。两函数之比是与点无关的常数，由$\sum_t\varepsilon(t)=0$准确消去。因此无需选商曲线微分尺度或丢弃底域常数。规范范数本身见Kato，*p-adic Hodge theory and values of zeta functions of modular forms*，Proposition 1.3(4)及§1.10的证明：[原刊](https://archive.numdam.org/item/AST_2004__295__117_0.pdf)；这里的除子比较也直接适用于原(AN2)的十二次幂规范。

全部$\Delta$作用同时移动同源与全标记。$p$惰性使
$\mathbb F_{p^2}^\times/\mathbb F_p^\times$走尽$p+1$个方向；每条上
$\phi_a([a]Q_j)$恰有阶$p^k$。所以各$k$均可用同一组$p+1$条导子$p$的CM邻曲线，不能把其它方向删除。

### 完整实主单位方向与所有Tate校正

取
\[
 J=(1+p\mathbb Z_p)/(1+p^{k+1}\mathbb Z_p),\qquad
 C_a[d]=\langle[p^{k+1-d}a]Q_j\rangle ,
\]
其中$C_a[d]$的阶为$p^d$。对$a\in A_j/J$固定提升，$\phi_{a,d}$为相应商同源，写
\[
 F_{a,d}(i)=\sum_t\varepsilon(t)\,
 \Theta_{E_1/C_a[d],(c)}
 \bigl(\phi_{a,d}(T_{t,j}+[a(1+pi)]Q_j)\bigr).
\]
同一个原量等于
\[
 e_\tau\sum_{a\in A_j/J}a^{-1}\binom{-s(a)}2
 \left\{F_{a,k}(0)+
 \sum_{m=1}^{k-1}(-p)^m
   \sum_{i=0}^{p^{k-m}-1}i^mF_{a,m}(i)\right\}. \tag{BQ2}
\]
证明是把实陪集写成$a(1+pi)$，$i\bmod p^k$。反圆指数固定，但完整Tate因子乘
\[
 (1+pi)^{-1}=\sum_{0\le m<k}(-pi)^m\bmod p^k.
\]
常数项沿全$C_a[k]$作无权范数。$m\ge1$时，$i^m$只须模$p^{k-m}$；每个$i\bmod p^{k-m}$的纤维，其真实平移差走尽$C_a[m]$。用前段相同除子比较即得(BQ2)。改变代表只重排原全和。商后野部分的阶为$p^{k+1-m}$，常数项为$p$。

这些商曲线的端环可直接从格核对：在$p$处，原CM格除以该循环群后，经数乘化为$\mathbb Z_p+p^d\mathcal O_p$，乘子环恰为自身；其它素处仍为原极大格。整体端环因此是$\mathbb Z+p^d\mathcal O$。

### 第二精度新增项的实际函数域非幂性

$k=1$复得(AR2)。$k=2$保导子$p^2$的第一项和导子$p$的$-p$加权项。在
$E'=E_1/C_a[1]$上令
$D=\phi_{a,1}([pa]Q_3)$，它阶为$p$。取$f=\Theta_{E',(c)}$，后项使用真正的有理函数
\[
 S_D(Z)=\prod_{i=0}^{p-1}f(Z+[i]D)^i,\qquad
 \frac{S_D(Z+D)}{S_D(Z)}
   =\frac{f(Z)^p}{\prod_{i=0}^{p-1}f(Z+[i]D)}. \tag{BQ3}
\]
后式逐项换标即可验证。在
$Z=\phi_{a,1}(T_{t,3}+[a]Q_3)$求值后再作全部原驯和，正是(BQ2)首个Tate校正的平移边界；没有以相对曲线导数替代$\Phi_j$的Kummer幂条件。

让$Z$在$E'$移动，先对所有$t$作
$S_D(Z+\phi_{a,1}T_{t,3})$的原权张量和，其函数域模$p$ Kummer类非零。在
\[
 Z=-\phi_{a,1}T_{t,3}-D
\]
只有这个标记的$i=1$原点除子贡献。不同标记之差是阶素于$pc$的非零挠点；其群与$E'[c]$及$\langle D\rangle$无交，故没有其它项贡献同一除子。原(AN2)的原点阶为$12(c^2-1)$，$c=103,\ p>211$时为$p$单位，于是该赋值为
$12(c^2-1)\varepsilon(t)\ne0\bmod p$。

这保留全驯张量，但尚未施外部$a$的反圆合成，也未证明原指定$Z$的算术求值仍非幂。故不据函数域结论宣称(BQ1)在原局部域非零；跨$p$主缺口仍须继续。

## 102. 通常全Sha的严格控制、循环模等价及更弱的全域三行门

保持§§98–100的原$E=E_{17}$、$K=\mathbb Q(\sqrt{-3})$、惰性$p>211$及$(17/p)=1$。$U=\gamma-1$、$\Phi=K_p$、$\mathcal O=\mathcal O_\Phi$；$Z$始终是目标模型的同一全域标准椭圆单位类。用§100固定103的真实系统及corestriction，除$b=103^2-103$，保留原$T_E^{-1}(1)$基。$\mathscr D=\Lambda_{(U)}$及$A,B,A_Z,X_{\rm str}$沿§99。

置$s=\operatorname{corank}_{\mathcal O}\operatorname{Sel}_{p^\infty}(E/K)$。原R294和R303(27)给
\[
 s=2+\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]
   =\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q).
\]
其中$K/\mathbb Q$的两味分解与$E$及其$-3$扭转之间的原三同源保留，未改成只看一味。

固定根数为$+1$，这里补原典核对以免由秩预设奇偶：对$\alpha=17$，Várilly-Alvarado的Lemma 4.1给$W_2=-1$、$W_3=+1$，因为$v_2(\alpha)=v_3(\alpha)=0$、$\alpha_3=8\bmod9$；Proposition 4.3给$v_{17}(\Delta)=2$、$e=6$时$W_{17}=(-1/17)=+1$。其余有限位良好，$W_\infty=-1$，故全根数为正。这里只用该论文无条件的局部根数公式，不用其关于有理点稠密性的条件定理：[原刊Lemma 4.1、Propositions 4.3–4.4](https://msp.org/ant/2011/5-5/ant-v5-n5-p04-s.pdf)。Nekovář，*On the parity of ranks of Selmer groups IV*，Theorem 1(a)，取$k=k_0=k'=\mathbb Q$，给每个当前$p$的$s$为偶数；见[作者全文](https://webusers.imj-prg.fr/~jan.nekovar/pu/parity4app.pdf)。这是$p^\infty$-Selmer奇偶定理，不假设$\Sha$有限。

### 基域严格群的准确余秩控制

基域strict群是usual Selmer在唯一$p$位的局部Kummer像之核。该像的$\mathcal O$余秩恰一：当地Kummer线至多一维，原有理非挠点$P_{17}$的非零形式对数及CM倍达到一。对$v\nmid p$，$E(K_v)\otimes\mathbb Q_p/\mathbb Z_p=0$。有
\[
 \dim_\Phi\bigl((X_{\rm str}/UX_{\rm str})\otimes_{\mathcal O}\Phi\bigr)
                         =s-1. \tag{BR1}
\]

证明。全域与$p$位的$E(D_\infty)[p^\infty]$及
$E(D_{\infty,p})[p^\infty]$均为零：反圆塔为pro-$p$，原惰性惯性的非平凡tame标量在剩余Tate格上仍存在。膨胀限制在全域给到不变量的同构，在$p$位给单射。所以塔上strict不变量有基域提升，并且其$p$位限制为零。

其它有限位只需固定有限$S$。每个$v\nmid p$的$H^1(K_v,E[p^\infty])$有限；由$H^i(K_v,V)=0$及局部对偶、紧Tate格的有限生成性可得。因而下降到基域strict至多有有限余核。$S$外好约化处的未分歧条件沿未分歧塔由惯性群识别保持。取对偶再有理化即得(BR1)。全域或当地的$H^2$没有被假定为零；所用的是上述不变量消失和非$p$位的有限误差。

把有限长$\mathscr D$-模$X_{{\rm str},\mathscr D}$写成
$\bigoplus_i\mathscr D/U^{e_i}$，每个$e_i\ge1$，(BR1)给其项数$s-1$，§99主特征等式给总长度$A$。于是
\[
 \boxed{\quad
 s-1\le A\le A_Z,\qquad
 \Sha(E/\mathbb Q)[p^\infty]\text{有限}
 \ \Longleftrightarrow\
 X_{{\rm str},\mathscr D}\text{循环}
 \ \Longleftrightarrow\
 \operatorname{Fitt}_{1,\Lambda}(X_{\rm str})\not\subset(U).
 \quad} \tag{BR2}
\]
循环模在这里非零，因为$s\ge2$。Fitting等价是DVR上最小生成元数的通常判据。余秩零的$\Sha[p^\infty]$有限，沿用通常Selmer的有限余生成性，不把“有限”加强为“零”。

特别地，**$A_Z\le2$已经足够**：由$s\le3$且$s$偶、$s\ge2$，得$s=2$。这比原$a_2\ne0$充分门弱。若§99的真实$z_1=0$，$U$长正合列给唯一整全域写法
$Z=U^2Z''$，置$z_2=Z''|_0$。同样的基变换单射、非$p$位有理jet消失及整$H^1$无$p$挠给
\[
 z_2\ne0\quad\Longleftrightarrow\quad A_Z=2
                   \qquad\text{（在 }z_1=0\text{ 支）}.
\]
此时$1\le B\le A\le2$，而
$\operatorname{ord}_U\mathcal A_p=A_Z+B$由R303(6)为偶数，故
$A=B=2$、$\operatorname{ord}_U\mathcal A_p=4$。因此原局部二次系数可以为零，而主任务的通常全$\Sha[p^\infty]$仍有限。

反过来，通常$\Sha[p^\infty]$无限迫$s\ge4$，于是$A_Z\ge3$，且$Z$在**整个整全域**Iwasawa $H^1$中可除$U^3$。为核最后的整性，先在$\mathscr D$清去分母；该分母在$\Phi[U]/U^3$中可逆，故截断类有理为零。有限整jet的$H^1$无$p$挠，因为剩余tame型没有不变量；所以整截断也为零，再用$U^3$长正合列。此处不以仅局部为零替代全域整除。

### 同一103源在全部整精度的完整三行

对$k\ge1$取$j=k+1$、$L_j=K(\mathfrak fp^j)$、$\mathfrak f=(34\delta)$及
$R_k=(\mathcal O/p^k)[U]/U^3$。记§100同一原单位为$u_j$。按
$\psi_{17}((x))=x/\varepsilon(x)$，把真全射线群写成
\[
 G_j=\frac{(\mathcal O_K/\mathfrak f)^\times
                  \times(\mathcal O_K/p^j)^\times}{\mu_6},
\]
以$[t,a]$标号，反圆指数为$s(a)$。原截断限制至$L_j$，在§100的同一对偶基下准确为
\[
 \mathcal Y_k=b^{-1}\sum_{[t,a]\in G_j}
   \varepsilon(t)a^{-1}(1+U)^{-s(a)}[t,a]u_j
 \in
 \bigl(L_j^\times/(L_j^\times)^{p^k}\bigr)
            \otimes_{\mathbb Z/p^k}R_k . \tag{BR3}
\]
三行权依次是$1,-s(a),\binom{-s(a)}2$。$\varepsilon(u)=u$使完整Tate系数对角$\mu_6$相容；$s(1+p^j\mathcal O)\subset p^k\mathbb Z_p$且$2$可逆保证提升无关。证明直接用§100的整平滑除法及Mackey的$\operatorname{res}\operatorname{cor}$；cyclotomic$(1)$已在真单位Kummer中，没有第二个范数权。

在$W_{R_k}$上，$d=[1,-1]\in G_j$作用为$-1$，反圆和cyclotomic作用则为一。$G_j$阿贝尔，故$H^1(G_j,W_{R_k})=0$，限制到$L_j$仍单射。这里$L_j$平凡化整个$W_{R_k}$，并未借全域$H^2$消失。

全域整$H^1_{\rm Iw}/U^3$由$U^3$正合列单射到截断系数的$H^1$；后者是有限生成$\mathcal O$模，所有模$p^k$检测将它分离。结合上段的有理阶与整$U^3$可除性，得到
\[
 \boxed{\quad
  (\exists k\ge1:\ \mathcal Y_k\ne0)
       \ \Longleftrightarrow\ A_Z\le2
       \ \Longrightarrow\
          \Sha(E/\mathbb Q)[p^\infty]\text{有限}.
 \quad} \tag{BR4}
\]
若$z_1=0$，常项和一次项已全为零，原二次项是$b z_2\bmod p^k$的限制（未除$b$的Mackey式）或$z_2$的限制（如(BR3)）。

所以在每个实际坏$p$，三个完整全域幂条件必须对**所有**$k$同时成立。仅在$p$位为幂是较弱的旧当地坏条件。还须对无穷$p$排除这个全域三行同时消失，或直接证明(BR2)的循环性；本节没有用更弱门本身宣称已完成。

## 103. 原全域对数的奇偶二读者及完整驯角色的野Jordan长度

沿(BP1)–(BP6)、(BR1)–(BR3)，保持原$E$、全射线群、Tate基、固定103和原两点。$p>211$及原惰性范围不变。令
\[
 L=\log(1+U)=U-U^2/2\pmod{U^3},\qquad U=L+L^2/2\pmod{L^3}.
\]
因$2$可逆，这给$(\mathcal O/p^k)[U]/U^3$与$(\mathcal O/p^k)[L]/L^3$的整同构。$j=k+1$，$B_j,G_{L_j},u_j$沿§100；在$G_{L_j}$上Tate因子、反圆指数及$\mu_{p^k}$均平凡模$p^k$。

将真实平滑原类$bZ$模$(p^k,L^3)$作Mackey限制，在Kummer外配$e^{-1}$后是
\[
 \sum_{a\in B_j}\rho(a)^{-1}[a]u_j\exp(-s(a)L).
\]
常项为$bZ_0=0$。单位群用加法，两个原行准确为
\[
 Y^o_k=-\sum_{a\in B_j}\rho(a)^{-1}s(a)[a]u_j,\qquad
 Y^e_k=\frac12\sum_{a\in B_j}\rho(a)^{-1}s(a)^2[a]u_j. \tag{BS1}
\]
它们在$(L_j^\times/(L_j^\times)^{p^k})\otimes_{\mathbb Z/p^k}(\mathcal O/p^k)$中。二次行与原$U^2$行的关系是
$Y^e_k=Y^{(U^2)}_k+Y^o_k/2$，因为$\binom{-s}2=(s^2+s)/2$。这里是全域固定103的行；§101当地十二次幂规范仍要按其原转换，不能静默互换。

$B_j$中有中央驯元素在$W_0/p$上为$-1$、$s=0$，取其二阶Teichmüller提升，则在整个$W_0/p^k\otimes(\mathcal O/p^k)[L]/L^3$上亦为$-1$。故限制对整截断$H^1$单射。§99给$Z\in U H^1$，若$z_1=0$则§102给$Z\in U^2H^1$。第一行检测$bz_1\bmod p^k$；若$z_1=0$，第二行检测$bz_2$，其中$z_2=(Z/U^2)|_0$。一般未判$z_1=0$时只把完整二行作为一个截断类。准确地，
\[
 \exists k:\ (Y^o_k,Y^e_k)\ne(0,0)
       \quad\Longleftrightarrow\quad A_Z\le2.
\]
反向若全部$k$两行都零，有限自由系数的截断$H^1$为有限生成$\mathcal O$模，$p$进分离；中央$-1$已消去限制核。故整截断为零，由长正合列得$Z\in U^3H^1$。不假设全域$H^2=0$，并允许$A_Z=2$、通常全$\Sha[p^\infty]$有限而$a_2=0$。

### 原参考素上的两个不同坐标

按$(1,\delta)$分解
\[
 -\rho(a)^{-1}s(a)=A_a+B_a\delta,\qquad
 \rho(a)^{-1}s(a)^2/2=C_a+D_a\delta.
\]
令$U_0,U_1$为(BP2)奇行两单位，另令
$V_0=\prod_a([a]u_j)^{C_a}$、$V_1=\prod_a([a]u_j)^{D_a}$。
一般完全分裂素位先保留四个单位的$(Nv-1)/p^k$次幂，不预删坐标。

原$c u_j=u_j$；$c$共轭$\rho$且使$s$变号。因此奇权在$a\mapsto cac^{-1}$时为负共轭，偶权为正共轭。成对选整指数提升；固定轨道的$s=0\bmod p^k$，其四个指数可取零。于是有准确单位恒等式
\[
 cU_0=U_0^{-1},\quad cU_1=U_1,\qquad
 cV_0=V_0,\quad cV_1=V_1^{-1}.
\]
沿(BP5)事先由原两点预选的惰性有理素$\ell$，置$n=(\ell+1)/p^k$。四个真实幂余数依序化成
\[
 \left((\bar U_0^{-2})^n,1;\;1,(\bar V_1^{-2})^n\right). \tag{BS2}
\]
这是先配原Tate基与$(1,\delta)$再用$\mathrm{Frob}=c$所得，偶行准确保留$\delta$坐标。

若$z_1\ne0$，§100的原始$X'_p$参考列在足够大$k$读出奇行。若$z_1=0,z_2\ne0$，§102给通常Selmer维数二及全$\Sha[p^\infty]$有限；原当地signed阶为四，故$\operatorname{loc}_p z_2=0$。按§100同一个饱和MW/对数核，有唯一$\lambda_2\in\mathcal O$使$z_2=\lambda_2X'_p$；若$z_2=0$取$\lambda_2=0$。同一个原MW参考列和足够大$k$遂在第二行读出$b\lambda_2X'_p$。两种存在检测允许取§100两个预选列的并集；哪个参考列为单位只取决于$\ell_1,\ell_2$。在这个事先可验族中某次(BS2)非平凡，便足以推出通常全$\Sha[p^\infty]$有限。预选素的存在本身不保证目标幂余数非平凡。

### 全原驯角色的准确野长度

令$k_0=\mathbb F_{p^2}$、$\chi=\rho\bmod p$，$B_1$表示$B_j$的规范素于$p$的Sylow子群，$N=p^{j-1}$。原固定$\mathfrak f=34\delta$的单位群阶素于当前$p$。CRT给
\[
 P_j=\operatorname{Gal}(L_j/L_1)=\langle r\rangle\times\langle a\rangle
             \simeq(\mathbb Z/N)^2,
 \quad s(r)=0,\quad s(a)=1\bmod N,
\]
其中$r$为实主单位，$a$为反圆主单位。置
\[
 e_\chi=|B_1|^{-1}\sum_{g\in B_1}\chi(g)^{-1}g,\quad
 D=a-1,\quad v_j=e_\chi N_{\langle r\rangle}[u_j]
 \in (L_j^\times/(L_j^\times)^p)\otimes_{\mathbb F_p}k_0 .
\]
这里$N_{\langle r\rangle}$是群环全和，$e_\chi$包括原$\mathfrak f$及全部$p$驯角色。$j=1$的扭后Mackey常项给
$|B_1|e_\chi[u_1]\otimes e^{-1}=\operatorname{res}(bZ_0)=0$，故$e_\chi[u_1]=0$；未令未经投影的底层单位范数为零。

记
\[
 \mathscr H=H^1\!\left(G_{K,S},
    (W_0/p)\otimes_{k_0}k_0[[U]]^\#\right),\qquad
 r_p=\max\{h:\bar Z\in U^h\mathscr H\}.
\]
这是有限生成、$U$进分离的模，且$r_p\ge1$。原局部基$\xi_1$及原$\mu=0$定理给$\operatorname{loc}(\bar Z)\ne0$，故$r_p$有限。所用$\mu=0$正是R1070已登记的原标准化：Burungale–He–Kobayashi–Ota，*Hecke L-values, definite Shimura sets and Mod $\ell$ non-vanishing*，Theorems 1.5、6.10，适用于本来的$K$上Q曲线及所有当前好惰性$p$；[原文](https://arxiv.org/pdf/2408.13932)。这里只需原局部像非零，不额外宣称在未核饱和性的位置比较$U$阶。

每个$1\le h\le N$，系数乘$U^h$的长正合列给
$\ker(\mathscr H\to H^1(k_0[X]/X^h))=U^h\mathscr H$，不需要$H^2$消失。$G_{L_j}$上$s\in N\mathbb Z_p$且$(1+X)^N=1\bmod X^h$，故真实Mackey限制在$e^{-1}$基下为
\[
 |B_1|\sum_{i=0}^{N-1}(1+X)^{-i}a^i v_j .
\]
中央$-1$使此限制仍单射。在$k_0[X]/X^N$中，因$N$为$p$幂，
$\sum_{i<N}z^i=(z-1)^{N-1}$。取$z=a/(1+X)$，用
$(D-X)^{N-1}=\sum_{l<N}D^{N-1-l}X^l$及
$(1+X)^{-(N-1)}=1+X$，得到
\[
 \sum_{i=0}^{N-1}(1+X)^{-i}a^iv_j
   =(1+X)\sum_{l=0}^{N-1}D^{N-1-l}v_jX^l. \tag{BS3}
\]
若$d_j=\dim_{k_0}k_0[D]v_j$，则$D^N=0$，且$D^tv_j\ne0$恰在$0\le t<d_j$。右端首格为$N-d_j$；$d_j=0$时整式为零。比较全部$h$准确给
\[
                 d_j=\max(0,p^{j-1}-r_p). \tag{BS4}
\]
因此真正原$\chi$分量于每个足够深的$j$都有实际单Jordan块，余亏恒为$r_p$。特别在$j=2$，
\[
              D^{p-3}v_2\ne0\quad\Longleftrightarrow\quad r_p\le2
\]
是§102整全域三阶截断非零的充分测试。特征零条件$A_Z\le2$允许模$p$头格因$p$整除而延后，故全部$k$的(BS1)仍是无损判据。深层非零和准确亏数没有证明$r_p\le2$或$A_Z\le2$发生于无穷多个$p$。

## 104. 原全域增广喷流的一条固定有理函数

保持(BP1)–(BP4)的目标$E=E_{17}$、$\mathfrak f=34\delta$、$j=k+1$、$c=103$、$b=c^2-c$及原Betti基$\varpi_{17}$。写$A_j=(\mathcal O_K/p^j)^\times$、$A_f=(\mathcal O_K/\mathfrak f)^\times$。在$L_j=K(\mathfrak fp^j)$的模$p^k$ Kummer张量中用加法记号，置
\[
 \mathcal U_{r,k}
   =\sum_{b'\in B_j}\rho(b')^{-1}\binom{-s(b')}r[b']u_j,
 \qquad r=0,1,2,
\]
其中$u_j=(\;{}_c\theta)^{-1}(\varpi_{17}/(\mathfrak fp^j))$。函数的点值在加法式中表示其乘法Kummer类。常、一次喷流消失时下一系数的全域识别依§§99–103。

R303(10)给
$\varpi_{17}=(1-\omega)^{-1}\Omega_{17}$、
$\bar\varpi_{17}=-\omega\varpi_{17}$，其中$\Omega_{17}$为实周期。
置$T_t=[t]\varpi_{17}/\mathfrak f$，故
$\bar T_t=T_{\omega\bar t}$。定义
\[
 A_t=\varepsilon(t)+\bar\varepsilon(t),\qquad
 B_t=(\varepsilon(t)-\bar\varepsilon(t))/\delta,\qquad
 I_t=(A_t+3B_t)/2\in\{\pm1,\pm2\}.
\]
有唯一$M\in\mathbb Q(E)^\times$满足
\[
 \operatorname{div}M=\sum_{t\in A_f}I_t[T_t],
                   \qquad M(O)=1. \tag{BT1}
\]
写$P_w=[\mathfrak f^{-1}w]\varpi_{17}/p^j$，其中逆取模$p^j$。
原三个行准确为
\[
 \boxed{\quad
 \mathcal U_{r,k}/b
    =\frac{\varepsilon(p)^j(1+\omega)}6
      \sum_{w\in A_j}w^{-1}\binom{-s(w)}r\,M(P_w).
 \quad} \tag{BT2}
\]
原惰性范围$\varepsilon(p)=-1$。$M$的零极全为固定primitive $\mathfrak f$挠点，上述值均有定义；$I_{-t}=-I_t$给
$M(-P)=M(P)^{-1}$。

### 固定函数的有理下降及原周期相位

负号给(BT1)除子的次数零。$G_K$的原CM标量模$\mathfrak f$是$a/\varepsilon(a)$，其$\varepsilon$值为一，故保持$I_t$。原有理曲线的Hecke共轭相容性给
$\varepsilon(\bar t)=\bar\varepsilon(t)$。于$t\mapsto\omega\bar t$，
\[
 A'=(-A+3B)/2,\qquad B'=(A+B)/2,\qquad I'=I .
\]
所以此除子在$\mathbb Q$上定义，其Picard类是有理挠点。

这里$E_{17}(\mathbb Q)_{\rm tor}=0$可直接验证：五处立方为置换，故约化有六点；七处$17=3$，非零立方$\pm1$各三次，$3\pm1$都是非零平方而$3$非平方，故约化有十三点。两处均好，且$p>2$的第一形式群在$p\mathbb Z_p$无挠，故有理挠点在两处皆单射约化。六与十三互素，所述Picard类为零。于有理原点定标给唯一$M$并实现有理下降。没有把$\varpi_{17}$误当实周期。

### 保留完整CRT、原Kato函数及所有Tate权

Ray CRT给$B_j=(A_j\times A_f)/\mu_6$。两标签$w,t$满足
$\rho(b')=w/\varepsilon(t)\bmod p^j$、$s(b')=s(w)$。
规范$(\;{}_c\theta)^{-1}$在$\mu_6$下不变，故真实共轭评价点是
$T_{p^{-j}t}+P_w$，即$[a]\varpi_{17}/(\mathfrak fp^j)$的两个CRT分量。

该函数与
$\psi_c(z)=\sigma(cz)/\sigma(z)^{c^2}$同除子，差为常数。这里始终是Kato原函数；(AN2)的Rubin函数另有十二次幂。配对$t,-t$后，偶性给
$\psi_c(P_w+T)/\psi_c(P_w-T)$的半个带权和，常数消失。再除对角$\mu_6$的重数得$1/12$；重标$t\mapsto p^{-j}t$提出$\varepsilon(p)^j$。

$\mathfrak f\cap\mathbb Z=102\mathbb Z$，故$m=102$为每个$T_t$的准确整数阶。令
$\operatorname{div}h_T=m[-T]-m[T]$、$h_T(O)=1$。
$cT=T$给准确函数恒等式
\[
 \left(\frac{\psi_c(P+T)}{\psi_c(P-T)}\right)^m
       =\frac{h_T([c]P)}{h_T(P)^{c^2}}. \tag{BT3}
\]
比较除子后在$P=O$比较，两边均一。在$w\mapsto cw$重排中
$s(c)=0$，逆Tate权多$c$，因此
\[
 \mathcal U_{r,k}/b
    =-\frac{\varepsilon(p)^j}{12m}
       \sum_{w,t}w^{-1}\binom{-s(w)}r
                   \varepsilon(t)h_{T_t}(P_w). \tag{BT4}
\]
所有分母对当前$p$可逆。

(BT1)和奇性给
$\prod_t h_{T_t}(P)^{I_t}=M(P)^{-2m}$，常数仍在$O$定标。
又$I_{\omega t}=(A_t-3B_t)/2$，所以
\[
 \varepsilon(t)=\frac12\left(
       (1+\delta/3)I_t+(1-\delta/3)I_{\omega t}\right).
\]
第二项重标$t$把$M(P)$变为$M([\omega]P)$，因为
$h_{T_t}(P)=h_{T_{\omega t}}([\omega]P)$。再重排$w\mapsto\omega w$，逆Tate权多$\omega$，而$s(\omega)=0$。代入
$1+\delta/3+\omega(1-\delta/3)=2(1+\omega)$即证(BT2)。

### 固定十八条同源上的完整各支

置$C_t=\langle2T_t\rangle$、$q_t:E\to E'_t=E/C_t$、
$\phi_t=q_t^\vee$。$\phi_t^*([-T_t]-[T_t])$的Picard类为
$q_t(-2T_t)=O$，故有唯一$g_t$以该除子为除子、且$g_t(O')=1$。
有
\[
                  g_t^m=\phi_t^*h_{T_t}.
\]
$P_w$的唯一$p^j$挠提升为
$[51^{-1}\bmod p^j]q_t(P_w)$，仍在同一全域。因此(BT4)可用各$g_t$的完整和，只余分母十二。

$C_t=E[\delta]\oplus L_t$，其中$L_t$为$E[17]$的一条
$\mathbb F_{17}$线；$17$惰性，primitive标签走尽十八条。三处的CM理想同源不改局部极大环，十七处邻格缩放后为
$\mathbb Z_{17}+17\mathcal O_{17}$，其它处原格不变，所以邻曲线端环为$\mathbb Z+17\mathcal O_K$。各向相位已在(BT2)合成，未指定任何单支非零。

### 真正二变量整体和所有好素的范数相容

令$G_j=(1+p\mathcal O)/(1+p^j\mathcal O)$、
$g_w=\langle w\rangle\in G_j$。把(BT2)的测试权换成有限群环中的
$w^{-1}[g_w]^{-1}$。因$\varepsilon(t)\in\mu_6$，有
$g_{\rho(b')}=g_w$。同一除子证明逐项给
\[
 \sum_{b'\in B_j}\rho(b')^{-1}[g_{\rho(b')}]^{-1}[b']u_j
   =\frac{\varepsilon(p)^j(1+\omega)}6\,
      (c^2-c[g_c])
       \sum_{w\in A_j}w^{-1}[g_w]^{-1}M(P_w). \tag{BT5}
\]
左侧$[b']u_j$是Galois共轭，其余$[g]$是群环基。确实，
$w\mapsto cw$使系数多$c[g_c]$，而$w\mapsto\omega w$仍只多$\omega$。
$c^2-c[g_c]$在$p$群的有限局部群环为单位，其增广为
$c^2-c\in\mathcal O^\times$。反圆限制$[g_c]=1$恢复(BT2)；
二变量喷流中必须保留整个单位，不能仅除常数$b$。

还有固定函数的精确范数恒等式。对任意
$\alpha\in\mathcal O_K$、$(\alpha,\mathfrak f)=1$，函数域范数满足
\[
 [\alpha]_*M=M\circ[\varepsilon(\alpha)^{-1}]. \tag{BT6}
\]
推前除子的$T_t$系数为$I_{\alpha^{-1}t}$，它只依赖
$\varepsilon(\alpha)^{-1}\varepsilon(t)$，正是右侧拉回除子的系数。
原点处的范数值是$\prod_{Q\in E[\alpha]}M(Q)=1$：
核的阶为奇数、与原零极支撑不交，$Q,-Q$两两抵消，$M(O)=1$。
所以比较除子后的常数准确为一。

特别对任何原好素理想$\mathfrak p$，
$\pi=\psi_{17}(\mathfrak p)=\alpha/\varepsilon(\alpha)$满足
$\varepsilon(\pi)=1$，故$[\pi]_*M=M$。在惰性处$\pi=-p$，在普通分裂处取同一实际CM Frobenius。这是同一个固定$\mathbb Q$函数的真实Coleman范数系统；普通处的完整Tate分量识别仍须保其所选嵌入，不以范数恒等式代替该识别。

### 任意固定短列表在全阿贝尔域中的模$p$独立性

任取固定相异正整数$a_1,\ldots,a_r$。对所有充分大的本节惰性$p$、
每个$j\ge1$及每个本原$P\in E[p^j]$，有
\[
 M([a_1]P),\ldots,M([a_r]P)
 \quad\text{在}\quad
 (K^{\rm ab})^\times/((K^{\rm ab})^\times)^p
 \quad\text{中}\quad\mathbb F_p\text{线性独立}. \tag{BT7}
\]
各点及点值在$K^{\rm ab}$中，来自原CM射线作用。挠点的$x$高度一致有界，因为$h(x)-2\widehat h$有界；曲线方程与固定有理函数高度不等式给全部这些非零有限$M$值统一高度上界$H$。

若有非零关系，在$[0,p)^r$中取其$p$个标量倍的整代表，分入
$N^r<p$个等盒，其中$N\asymp p^{1/r}$。两点同盒给一个非零标量倍的整提升
$|n_i|\ll_r p^{1-1/r}$；$r=1$直接取一。置
$F(Z)=\prod_iM([a_i]Z)^{n_i}$。则
$F(P)=\beta^p$、$\beta\in(K^{\rm ab})^\times$，且
$h(\beta)\ll_{r,H}p^{-1/r}$。

Amoroso–Zannier，*A relative Dobrowolski lower bound over abelian extensions*，Ann. Scuola Norm. Sup. Pisa 29 (2000), 711–727，印页712 Theorem 1.1取$D=1$，给固定$K$的阿贝尔扩张中非单位根的正高度下界；见[原刊全文](https://www.numdam.org/item/ASNSP_2000_4_29_3_711_0.pdf)。因此充分大$p$时$\beta$必为单位根。

原$p$处CM惯性走尽$(\mathcal O_K/p^j)^\times$。所以$P$的$G_K$轨包括至少$p^{j-1}(p-1)$个实本原点
$[u]\Omega_{17}/p^j$，其中$u\in(\mathbb Z/p^j)^\times$、
$\Omega_{17}=(1-\omega)\varpi_{17}$。因$F\in\mathbb Q(E)$，这些点的$F$值都是实单位根$\pm1$。若$F$非恒定，两纤维总点数不超过
\[
 2\deg F\le2\deg M\sum_i|n_i|a_i^2
                 \ll_{(a_i)}p^{1-1/r},
\]
与前述实点数矛盾。

最后$F$确实非恒定：取$n_i\ne0$中最大$a=a_i$，选择整数阶恰为$102a$的$Z$且$[a]Z=T_1$。这可在$(\mathbb Q/\mathbb Z)^2$中将阶102的$T_1$写成$(1/102,0)$后直接取到。每个较小$b<a$满足
$\operatorname{ord}([b]Z)=102a/\gcd(102a,b)>102$，故只有$a$项在$Z$有零极，且阶数非零。矛盾证明(BT7)。

(BT7)已包含完整原驯源；(BT5)角向全和的长度随$p$增长，不能以固定短列表独立宣称其增广喷流跨$p$非零。尚需付此最后的完整非抵消。

### 固定短列表的全部整精度关系阶一致有界

(BT7)还可保全部精度。固定同一$a_1,\ldots,a_r$，令$j=k+1$，
$P\in E[p^{k+1}]$本原。存在只依赖该固定列表的常数$C_A$，
使任一关系
\[
 \prod_iM([a_i]P)^{n_i}\in((K^{\rm ab})^\times)^{p^k}
\]
的系数向量$(n_i\bmod p^k)$之加法阶$d$至多$C_A$。
在原充分好惰性$p$范围，该常数与$p,k$无关。

证明与(BT7)的高度和原最大标量孤立零极相同，但盒子数改为$d$：
取该向量的$d$个不同倍，在$[0,p^k)^r$中分盒，得到一个非零倍的整提升
$|n'_i|\ll_r p^k d^{-1/r}$。其乘积是某$\beta^{p^k}$、
$\beta\in K^{\rm ab}$，于是$h(\beta)\ll_A d^{-1/r}$。
$d$充分大时，原Amoroso–Zannier高度隙迫$\beta$为单位根。
所得非恒定$F=\prod M([a_i]Z)^{n'_i}$在至少$p^k(p-1)$个实本原点取$\pm1$，
而其次数至多常数乘$p^k d^{-1/r}$。因$p-1$有固定正下界，
$d$充分大即矛盾。有限的小$d$统一吸收进$C_A$。

所以对一个固定$p$，$k\to\infty$时也不能出现系数向量阶趋于无穷的
固定支撑关系。此强化仍没有从真实完整角向长和构造出这样的固定支撑；
§107的支撑界明确说明仅靠六个权的形式倍不足。

## 105. 同一全射线Robert类的二变量行列式与六个完整全域幂条件

先取$p>211$在$K$惰性，保持§100的
$W_0=T_{17}^{-1}(1)$及原相容Betti/Tate基。本节的全域论证不需
$(17/p)=1$；该旧限制只在另行调用§98的特定当地单变量比较时保留。
令$K_\infty^{(2)}$为两条$\mathbb Z_p$塔合成，
\[
 \Gamma=\Gamma_+\times\Gamma_-\simeq\mathbb Z_p^2,\qquad
 \Lambda_2=\mathcal O[[U_+,U_-]],\qquad I=(U_+,U_-).
\]
保持反圆逆约定，普遍群元作用为
$(1+U_+)^{-s_+}(1+U_-)^{-s_-}$，原单变量$U$是$U_-$的限制。
$\boldsymbol Z$为同一$(\;{}_{103}\theta)^{-1}$全射线系统，扭以完整
$T_{17}^{-1}$后保留两个变量的真实全域类。固定平滑与未平滑类相差
(BT5)整个$c^2-c[g_c]$，其常项$c^2-c$为单位；下面有限和列已平滑源。

### 原典给的正是这个行列式格

Johnson-Leung–Kings，*On the equivariant main conjecture for imaginary quadratic fields*，Crelle 653 (2011), 75–114；见[作者全文](https://epub.uni-regensburg.de/13800/1/MP52.pdf)。
Definition 3.2的$\;{}_{\mathfrak a}\zeta_{\mathfrak m}$是同一Kato逆theta值的真范数；在$\mathfrak m=\mathfrak fp^j$的已分歧塔内，其分布正是§100的$u_j$。Definition 3.5的(8)–(9)和Lemma 3.7先张量指定基再作真实迹。

在CRT标签$[(t,a)]$上取有限角色
$\chi=\varepsilon(t)\tau(a)^{-1}$。$\varepsilon(u)=u$使它对角$\mu_6$平凡；各局部原导子保留。取含$\chi$值数域的指定$p$位系数分量，再按Lemmas 4.7、6.1扭以
$\varrho=\langle a\rangle^{-1}$，便从有限角色变为完整
$T_{17}^{-1}$。这一无限阶扭转也可逐有限模直接张量后取迹，群环自同构给同一对象。作者的左右环约定以同步反演变量转换，保持$I$。

Theorem 5.1给一般$H^1$秩一、$H^2$挠，且真实$\boldsymbol Z$在分式域的$H^1$线上生成
\[
 \operatorname{Det}_{\Lambda_2}^{-1}
       R\Gamma(\mathcal O_K[1/p],\Lambda_2(W_0))
\]
的格，固定平滑只乘上述单位。这是特定字符的$\Lambda$定理，对惰性$p$无条件；不调用另一等变$\Omega$定理的未证$\mu$假设。

### 基域维数与真实有符号子式

置
\[
 R=\widehat{(\Lambda_2)_I}=\Phi[[U_+,U_-]],\qquad \mathfrak m=IR .
\]
原文Lemma 4.3及固定截断的有限自由消解给导出基变换；闭点纤维为
$W=W_0\otimes\mathbb Q_p$的全域上同调。

先核原文$j_*$与这里$G_{K,S}$的条件。每个真正坏位
$v\mid2\cdot3\cdot17$的原有限CM惯性角色非平凡。若wild惯性作用非平凡，因其为pro-$\ell$、$\ell\ne p$，在特征零平均后其全部上同调为零；若wild平凡，tame惯性阿贝尔，有限素于$p$的非平凡标量仍使全部惯性上同调为零。反圆/圆分塔在这些位未分歧，故有限jet不改变这一消失。原$j_*$与加入这些$S$位的局部修正为零。

沿§102置
$s=2+\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]$。
基域通常CM Selmer的$\Phi$维数为$s$。唯一$p$位的Kummer线维一，真实有理非挠点的非零形式对数张满它。任一全域$W$类与这个对偶Tate格上的全域MW类满足全局互反；非$p$位有理上同调为零，所以其$p$处像正交于该Kummer线。当地Tate对偶中这一正交补就是$W$的Kummer线。因此relaxed全域$H^1$没有多出非有限当地类，等于usual Selmer，维数$s$。

所有当地$H^2(W)$由对偶$H^0(V)$为零；Poitou–Tate给全域
$H^2(W)$对偶于基域$V$的strict核，维数$s-1$。同样也可由
$H^0(W)=0$和虚二次域秩一系数Euler特征$-1$从$H^1$维数得到。
未假设全域$H^2$消失。

将完美复形中单位微分分裂后，在$R$上有极小模型
\[
                  R^s\xrightarrow{\ D\ }R^{s-1},
                    \qquad \text{次数为 }1,2,\quad D_{ij}\in\mathfrak m.
\]
Theorem 5.1给$D$一般秩$s-1$。在分式域任取一个非零极大子式展开，行列式生成元在$R^s$中的闭链代表正是
$D$的$s-1$阶有符号子式向量，乘同一个$R$单位。换$R$基只乘单位并同步变换源向量。每一子式都在$\mathfrak m^{s-1}$，所以
\[
 \boldsymbol Z\longmapsto0
       \quad\text{于}\quad
 H^1\!\left(K,W\otimes_\Phi R/\mathfrak m^{s-1}\right). \tag{BU1}
\]
这是**系数截断的上同调像**；$I$非主，不能擅自加强成
$\boldsymbol Z\in I^{s-1}H^1_{\rm Iw}$。

### 全部精度的六行与通常全Sha

若通常全$\Sha[p^\infty]$无限，§102的无条件Selmer奇偶给$s\ge4$。
三阶整系数的$H^1$无$p$挠：模$p$各分次都有非平凡驯标量$-1$，故
$H^0$为零；对系数乘$p$的长正合列即证。于是(BU1)有理为零提升为
\[
 \boldsymbol Z\longmapsto0
   \quad\text{于}\quad
 H^1\!\left(K,W_0\otimes_{\mathcal O}
                  \mathcal O[U_+,U_-]/I^3\right) . \tag{BU2}
\]
对每个$k\ge1$取$j=k+1$、$L_j=K(\mathfrak fp^j)$。
在其原Kummer张量中，真实限制为
\[
 \mathcal J_k=
 \sum_{[t,a]\in G_j}\varepsilon(t)a^{-1}
       (1+U_+)^{-s_+(a)}(1+U_-)^{-s_-(a)}[t,a]u_j
                    \pmod{(p^k,I^3)}. \tag{BU3}
\]
六项对应$1,U_+,U_-,U_+^2,U_+U_-,U_-^2$。
两个指数是$\log\langle a\rangle$在实/虚$p$阶整基中的坐标；
$1+p^{k+1}\mathcal O$给指数$p^k$倍，且$2$可逆，所以提升无关。
这是§100同一全陪集Mackey和。中央$d=[1,-1]$在$W_0$为$-1$、在两个pro-$p$商平凡；$L_j$平凡化全部截断系数，限制仍无核。
用未平滑源时乘整个$c^2-c[g_c]$的逆，不仅除其常项。

因此
\[
 \Sha(E/\mathbb Q)[p^\infty]\text{无限}
      \ \Longrightarrow\ (\forall k\ge1)\ \mathcal J_k=0, \tag{BU4}
\]
而任一$k$的任一真实混合行非零便充分推出通常全$\Sha[p^\infty]$有限。
只知道旧当地$a_2=0$不满足这里的前提。

### 普通分裂素的同一完整源

若$p=\mathfrak p\bar{\mathfrak p}$分裂，取原CM直因子
$V=V_{\mathfrak p}$、$W_0=T_{\mathfrak p}^{-1}(1)$、系数域$\mathbb Q_p$；
两变量仍保完整$\mathfrak fp^j=\mathfrak f\mathfrak p^j\bar{\mathfrak p}^{\,j}$塔。
为避免凭空删掉另一$p$位的Euler因子，直接用上述原文
Theorems 5.4、5.5：Gillard结果使完整$\Omega$行列式等式在所有
$p\nmid6$的分裂处无条件成立，而其$\zeta=\varprojlim\zeta_{\mathfrak fp^n}$从定义起就是此两位同时升的源。取
$\chi=\varepsilon(t)\tau(a_{\mathfrak p})^{-1}$的素于$p$有限直因子，
再扭$\langle a_{\mathfrak p}\rangle^{-1}$；§7.1的(18)导出基变换和
Lemma 6.1将该等式传到原所选CM行。没有以单侧raw theta源替换原完整源。Definition 3.2已对有理整数$p$两处取范数；Proposition 3.3(2)在$\mathfrak q\mid p\mathfrak m$时为已分歧相容支，也不会在这里额外丢掉$\bar{\mathfrak p}$因子。

基域维数仍准确。复共轭交换$V,V^c$，
\[
 [H^1_f(K,V)\oplus H^1_f(K,V^c)]^{c=+1}
                         \simeq H^1_f(K,V),
\]
逆由$x\mapsto x+cx$给出。$[K:\mathbb Q]=2$可逆，二次下降把左边与
$\mathbb Q$上完整$V_pE$的usual Selmer识别，故其维数为同一$s$。
局部对数使$V$的Kummer像在$\mathfrak p$维一、在$\bar{\mathfrak p}$维零；
真实有理非挠点在第一处的对数非零。故两处合计的strict核维$s-1$，
Poitou–Tate、当地$H^2=0$及Euler特征给同一极小模型。

整截断无$p$挠可在CRT取
$a_{\mathfrak p}=1,a_{\bar{\mathfrak p}}=-1,t=1$的驯元素：
它在$W_0=T_{\mathfrak p}^{-1}(1)$作用为$-1$，在$\Gamma$平凡。
Nekovář奇偶适用全部奇$p$，所以(BU2)–(BU4)在该原分量也成立，
有限和的$a^{-1}$取其$\mathfrak p$分量。交换两处得到共轭分量。
这同时保留两个ordinary位的当地限制，没有把某个单侧Taylor格当作完整全域六行。

本节扩大了真实坏$p$必须满足的条件，还没有证明这些条件在无穷$p$中被违反。

## 106. 全部野方向的原始迹与同一驯微分五个单独必要零

置$q=p^2$、$b=q-1$，取任一充分大的惰性$p$。本节假设
$\Sha(E_{17}/\mathbb Q)[p^\infty]$无限，使用§105真正完整的六个全域行零。
保持原$E_1,\nu,r_2,\varepsilon$，以$s$为严格LT变量，$\omega_1=ds\bmod p$，
$Y=s^b$。这里没有将仅$a_2=0$当成假设，也不需原$(17/p)=1$子列。

### 物理模型、周期相位和同一原样本

惰性给$6\mid p+1$，所以
$\mathbb F_p^\times\subset(\mathbb F_{p^2}^\times)^6$。Hensel提升得到
$\theta=17^{1/6}\in\mathcal O_\Phi^\times$。同一所选代数根给
\[
 i_\theta:E_{17}\longrightarrow E_1,\qquad
 (x,y)\longmapsto(x/\theta^2,y/\theta^3),\qquad
 i_\theta^*\omega_1=\theta\omega_{17}.
\]
所有驯、野标记同时运输，CM作用可交换。用同一LT对数及各自归一不变微分，
\[
 s_1(i_\theta P)=[\theta]_{\rm LT}s_{17}(P).
\]
这是导数为单位的完整形式群作用，不能将一般$\theta$静默当成Teichmüller标量。
运输使原野标签乘同一单位，外部逆Tate权及所有jet一起只改可逆标量和群环元。
因此先把真实物理源运到规范$E_1$，再在该模型上取下述系数；不预设两模型的单格相等。

若代数根改为$u\theta$、$u\in\mu_6$，同一标记重排及
$\varepsilon(ut)=u\varepsilon(t)$与对角$\mu_6$相容。
原第三种微分满足$[u]^*\kappa_{uP}=\kappa_P$，因为$X(uP)=u^{-1}X(P)$、
斜率同权而$\omega_1$乘$u$；故$[u]^*\nu=u\nu$。
在$s\mapsto us$下，下面各$[s^{jb}]\nu/ds$至多乘非零单位。
两模型的$q$-Frobenius均为$[-p]$，而$\bar\theta^q=\bar\theta$，
所以原Frobenius重标和$\varepsilon(-p)=1$完全保持。

还须核对全射线规范。$L_2=K(\mathfrak fp^2)$上的CM对
$(\mathbb C/(\mathfrak fp^2\mathcal O_K),1)$经原周期及上述同一模型运输，
评价于$\varpi/(\mathfrak fp^2)$。主要理想的CM互反使$[(t,a)]$评价于
$x_0\varpi/(\mathfrak fp^2)$，其中$x_0\equiv t\bmod\mathfrak f$、
$x_0\equiv a\bmod p^2$。CRT准确给
\[
                  T_{p^{-2}t}+[\mathfrak f^{-1}a]Q_2 .
\]
整个群迹是全双和除六，原外权仍为
$\varepsilon(t)\tau(a)^{-1}$。$\mathfrak f^{-1}$是一个完整野/驯群元，
与各差分交换；移入六项截断时乘可逆群环元，不能只抽一个二次项而删掉较低项的搬移。

真Kato $\;{}_{103}\theta$的除子是
$103^2[O]-\sum_{E[103]}[P]$；(AN2)原Rubin函数为其十二倍除子。
二者之比的常数被完整驯权或外部$\Delta$投影杀掉，逆theta源因此保留
$-1/12$的准确转换。可先在未分歧驯分裂域操作，随后按原$[-p]$和
$\varepsilon(-p)=1$下降。后一恒等式也直接来自$E_{17}$的好惰性约化
$a_p=0$、$\psi_{17}((p))=-p$，并非额外假设$\sqrt{17}\in\mathbb Q_p$。

### 任一方向的真实范数都消去头三格

取$h,l\in\mathbb F_q$对$\mathbb F_p$线性独立，在第一主单位层取
$g_h=1+ph,g_l=1+pl$。置
\[
 N_h=\sum_{i=0}^{p-1}g_h^i,\qquad Z_l=g_l-1,\qquad
 F_h=\Phi_2^{\langle g_h\rangle},\quad
 y_h=N_h r_2,\quad t_h=N_hs .
\]
§105取$k=1$，并在两个整变量中任意可逆换基。完整一次、二次行零与
§76的有限群环恒等式给
\[
                  Z_l^{p-2}y_h=Z_l^{p-3}y_h=0
           \quad\text{于模 }p\text{ 的真实Kummer张量}. \tag{BV1}
\]
其中$g_l$、$\Delta$与$\mathfrak f^{-1}$的剩余因子皆可逆。限制
$F_h\to\Phi_2$在$e_\tau$中无核：可能的循环$p$ Kummer核型为
$\tau^{p+1}$，与此型不同。故(BV1)在$F_h$本身成立。

$t_h$是素元，且$[a]t_h=a^pt_h$对$a\in\Delta$成立。
$\Phi_2/\Phi_1$的每个非零野元有同一下断点$b$；§77的different塔公式
对任意$h$给$F_h/\Phi_1$亦只有这个断点。因此
\[
 g_lt_h=t_h(1+\lambda_l t_h^b+\cdots),\qquad\lambda_l\ne0.
\]
原$r_2\in U_2$由$L(E_{17},1)=0$给出；该零在上面的完整模型运输中保留。
§79的$N_hU_2\subset U_2(F_h)$只用这个断点，故对全部$h$适用。

在原$e_\tau$的乘法嵌入中，$d\log y_h$只容
$t_h^{p+ib-1}dt_h$。记其头三格为$L_0,L_1,L_2$。
$U_2$与Cartier恒等式先给$L_0=0$。再对(BV1)分别取微分并读
$t_h^{(p-1)q}dt_h$：§§78–79的最低项乘子只把原非零$\lambda$
换成$\lambda_l$，先后给$L_1=L_2=0$。乘积中的因子分别为
$-2,\ldots,-(p-1)$及$-3,\ldots,-(p-1)$，均可逆。

拉回$\Phi_2$，有$t_h=s^p+\cdots$及
$v_{\Phi_2}(dt_h/ds)=(p-1)q$。后一阶数也可由
$t_h'/t_h=\sum_i(g_h^is)^{-1}$、首差$-hs^q$及
$(p-1)!\ne0$核出。于是原完整方向迹
\[
 T_hB=\sum_{i=0}^{p-1} B([1+pih]s),
              \qquad B\,ds=e_\tau d\log r_2 ,
\]
至$s^{3pb}$含该项全部为零。对应$L_i$的首可能次数恰为
$p(i+1)b$，所以没有漏掉低阶补偿。

同窗中原函数恒等式给
\[
 T_hB=12(c^2-[c]^*)\,T_h\operatorname{proj}_{\Delta}\nu .
\]
若右边未平滑微分的第一个非零项为$s^{n-1}ds$，
则$\Delta$型强制$n\equiv1\bmod b$，在该首项上的对角因子为
$12(c^2-c^n)=12(c^2-c)\ne0\bmod p$。
依次数递推可反平滑整个窗，故$\nu$的每个$\Delta$方向迹也在此窗全零；
不只消掉四槽某个总和。

### 两个低次多项式分离五个原系数

记
\[
                       B'_j=[s^{jb}]\,\nu/ds.
\]
$B'_0=0$来自同一中央值，$C^2\nu=\nu$再给$B'_1=0$。
取$r=h^{p-1}\in\mu_{p+1}$。同一LT加法与§81的逐幂展开给
\[
 \frac{[1+pih]s}{s}
    =1-ihY-ih^pY^{p+1}
      +(D_hi-i^2h^{2p}/2)Y^{2p+1}
                  +O(Y^{3p+1}), \tag{BV2}
\]
其中$D_h$不必另求。模$p^2$相同的两个单位作用之差从$s^{q^2}$开始，
高于此窗；$Y^{p+1}$来自加法律的$s^{q-p}([pih]s)^p$项，
$Y^{2p+1}$的二次极化为$-ijh^{2p}$，其余部分对$i$可加。

取$[Y^{2p}]$，通常幂的次数$p-1,2p-2$分别保留$j=p+1,2$；
含一个高项的唯一余项含已零的$B'_1$。有限域幂和故准确给
\[
                   -rB'_{p+1}+r^2B'_2=0
                     \qquad(\forall r\in\mu_{p+1}).
\]
因此$B'_{p+1}=B'_2=0$。

再取$[Y^{3p}]$。全部含$Y^{p+1}$或$Y^{2p+1}$的列仅可能带
$B'_{p+1},B'_2,B'_1$，此时均已零；$D_h$项也在其中。
通常幂的次数$p-1,2p-2,3p-3$分别给
\[
       -rB'_{2p+1}+2r^2B'_{p+2}-r^3B'_3=0
                     \qquad(\forall r\in\mu_{p+1}).
\]
$p>3$，次数至多三的多项式有$p+1$个根，只能各系数为零。
故得到五个**同一物理微分的单独必要零**
\[
 \boxed{\quad
 \Sha(E_{17}/\mathbb Q)[p^\infty]\text{无限}
 \ \Longrightarrow\
 B'_2=B'_3=B'_{p+1}=B'_{p+2}=B'_{2p+1}=0 .
 \quad} \tag{BV3}
\]
按§88在(BD1)前已付的准确Frobenius重标，两次Cartier后的原四行逐个为零。
每行内部的$H,H^2,D_{ij}$及其全部混项仍在，不能由(BV3)删掉它们或直接宣称
固定联络的所有$p$曲率为零。任一这些真实单格在无穷惰性$p$非零已足主目标，
该跨素数非零仍待继续证明。

## 107. 原首野层六个低次权的形式关系与准确最小支撑

固定§104的同一$M\in\mathbb Q(E_{17})^\times$及全部原$\mathfrak f$除子，
沿§§105–106的真实二变量三阶截断。置$k=\mathbb F_q$、$q=p^2$、
$\Omega=k^\times$、$V=(k,+)$。在$j=2$唯一写
$w=\omega(a)(1+pz)$，其中$a\in\Omega,z\in V$，$\omega$为乘法Teichmüller提升。
两个主单位的对数坐标模$p$是$z$在固定$\mathbb F_p$基下的$x,y$；
改变原整基给$\mathrm{GL}_2(\mathbb F_p)$换元。模$p$原Tate权为$a^{-1}$，
原$\mathfrak f,\varepsilon$及真实有理函数权已经完整进入$M$。

在自由带标号源$k[\Omega\times V]$中，对六个次数至多二的原系数作平移、
群环乘及$k$线性组合，所得空间准确为
\[
 \mathcal J=\left\{
    \sum_{a,z}a^{-1}P(x(z),y(z))[(a,z)]:
       P\in k[X,Y],\ \deg_{\rm tot}P\le2\right\}. \tag{BW1}
\]
确实，左乘$[(b,t)]$将系数变为$b\,a^{-1}P(z-t)$，故该六维空间本身已是理想。
实/反圆逆号只改一次行符号；因为$2$可逆，二项式坐标与
$(1,x,y,x^2,xy,y^2)$同张。六个多项式在$\mathbb F_p^2$上独立，
因为各变量次数小于$p$，故维数准确为六。完整平滑
$103^2-103[g_{103}]$在$k[V]$中的增广为单位，增广理想幂零，
所以它是单位并将$\mathcal J$双射到自身。

这里只描述自由源上的权空间；当原全域截断确实零时，这些向量的像才是
实际单位Kummer群的关系。没有声称实际评价映射的全部核就是$\mathcal J$。

若$P\ne0$，其在$\mathbb F_p^2$的零点至多$2p$。例如按$Y$的次数
$d\le2$取首系数$A(X)$，$\deg A\le2-d$；至多$2-d$条竖线
容$p$个零点，其余各至多$d$个，立即得此界。于是
\[
 \min_{0\ne v\in\mathcal J}|\operatorname{supp}v|
                       =(q-1)(q-2p). \tag{BW2}
\]
等号由$P=(X-b)(X-c)$、$b\ne c\in\mathbb F_p$达到。

若使用$\mathcal O$的两个整数坐标并允许$\mathbb F_p$平移/线性组合，
相应行可写为
$\operatorname{Tr}_{k/\mathbb F_p}(a^{-1}P(z))$，因为任一线性坐标均为
$\operatorname{Tr}(\lambda\,\cdot)$。对每个$P(z)\ne0$，$\Omega$中
恰有$p-1$个$a$使迹为零，恰$q-p$个使迹非零。因此完整迹空间的
非零行最小支撑为
\[
                            (q-p)(q-2p). \tag{BW3}
\]
同一两平行直线的$P$给等号。迹配对非退化也表明$P$到迹行的映射
在$\mathbb F_p$上单射；此空间的$\mathbb F_p$维数是十二，不能与
(BW1)的$k$维数六混淆。

即使再允许原$[p]$推前，把每个$a$的常数野权范数并回首$p$层，
在$p^2$层也只是对每个$a$减常数$\beta_a$。对正次数$P$，
$a^{-1}P-\beta_a$仍非恒定，因而仍至少保留(BW2)那么多个原标签。
在整数坐标中，设$P$的正次系数在$k$内张成$d$维$\mathbb F_p$空间，
$d=1$或$2$。至多$p^{2-d}-1$个$a$使
$\operatorname{Tr}(a^{-1}P)$为常数；其它每个$a$即使任减常数也
至少留下$q-2p$个位置，故原层总支撑仍至少为(BW3)。未在此数中
加入新产生的$p$层项。

所以仅凭这六个原权、其平移与全部群环倍，不能从$I^3$全坏条件抽出
(BT7)适用的固定有限列表关系：任一非零形式行的原$p^2$标签数至少随$p$四次增长。
这不限制利用$M$的除子、CM、循环商或Weil互反所得的另外源恒等式。
例如$M(-P)=M(P)^{-1}$本来就是另一种短函数关系，未被排除。
后续必须引入这些真实几何关系，不能把形式支撑界误当作实际单位群独立性定理。

## 108. 原固定M的首野循环商与完整驯除子上的Miller互反

沿§§104–107，在$E=E_{17}$上记
$D_f=\operatorname{div}M=\sum_t I_t[T_t]$，$M(O)=1$、
$I_{-t}=-I_t$。固定$j=2$的原$p^2$点$P=P_{w=1}$；
它是(BT2)的野点，不是MW基点。于是$P_w=[w]P$。
令$k=\mathbb F_{p^2}$、$\Omega=k^\times$，
$\omega(a)\in(\mathcal O_K/p^2)^\times$为乘法Teichmüller提升。
对$z\in k$置$R_z=[p\widetilde z]P$，提升任意；
$R:k\to E[p]$是$\mathbb F_p$线性同构。

全部点和CM作用在原$L_2$中定义：原表示模$p^2$通过射线群，
而$\psi((a))=a/\varepsilon(a)$在$a\equiv1\bmod\mathfrak f$时
模$\mathfrak f$为一，所以$E[\mathfrak f]$也由$K(\mathfrak f)$定义。
以下函数与除子均在特征零，只对目标Kummer类取模$p$。

对非零$\mathbb F_p$线性泛函$\lambda:k\to\mathbb F_p$、
$d=1,2$，取已除§104可逆平滑的原完整行
\[
 Y_{\lambda,d}
  =\sum_{a\in\Omega}a^{-1}\sum_{z\in k}\lambda(z)^d
       [\,M([\omega(a)]P+[a]R_z)\,]
  \in(L_2^\times/(L_2^\times)^p)\otimes_{\mathbb F_p}k. \tag{BX1}
\]
这正是$w=\omega(a)(1+pz)$的原权。常数行已另付；
两独立$\lambda$的一次幂与所有方向的平方，由$2$可逆的极化
张成其余五维。此式保留全部$\Omega$和所有$\mathfrak f$点。

任选$\lambda(z_0)=1$，置
\[
 C_a=[a]R_{\ker\lambda},\quad
 \phi_a:E\to E_a=E/C_a,\quad
 S_a=\phi_a([a]R_{z_0}),\quad
 Q_a=\phi_a([\omega(a)]P).
\]
$S_a$恰有阶$p$，与$z_0$的选择无关。令$M_a$为真实函数域范数，
\[
 M_a(\phi_aX)=\prod_{R\in C_a}M(X+R),\qquad
 \operatorname{div}M_a=\sum_t I_t[\phi_aT_t],\quad M_a(O)=1.
\]
不同$\mathfrak f$点不碰撞；原点归一由$p$奇及$R,-R$互逆直接给出。
在$\lambda(z)=i$的整个切片上，原乘积恰为$M_a(Q_a+[i]S_a)$。
并且$[p]Q_a=[\lambda(1)]S_a$。若$\lambda(1)\ne0$，$Q_a$阶为$p^2$且
$S_a$在其循环群中；若$\lambda(1)=0$，$Q_a,S_a$为独立$p$挠点：
否则$Q_a\in\phi_a(E[p])$会迫$[\omega(a)]P\in E[p]$。两类方向都保留。

### 两种准确整提升和主除子

取整数$b_i\equiv i^d\bmod p$，使$b_0=0$、$\sum_i b_i=0$。
$d=1$取对称代表，正部次数准确为$(p^2-1)/8$。
$d=2$令$r_i\in\{0,\ldots,p-1\}$为$i^2\bmod p$，
$R=p^{-1}\sum_i r_i$。因$\sum i^2=0\bmod p$，$R$为整数；
$r_i=r_{-i}$、$r_0=0$且$p$奇又给$R$为偶数。将最大的$R$项
按$\pm i$成对各减$p$，得$b_i=b_{-i}$，仍$b_0=0$。
未减的最小$p-R$项之平均不超过全体平均$R$，所以
\[
 \sum_{b_i>0}b_i\le R(p-R)\le(p^2-1)/4 .
\]
两种$d$都满足$\sum_i ib_i\equiv\sum_i i^{d+1}=0\bmod p$。
因此$E_a$上的除子$\sum_i b_i[iS_a]$整次数零、群和为$O$，
故为主除子。取唯一$g_{S_a,d}$以它为除子且$g_{S_a,d}(O)=1$。
函数定义在$L_2$，次数是上述正部次数；唯一性还给
\[
 g_{S,1}(-Z)=g_{S,1}(Z)^{-1},\qquad
 g_{S,2}(-Z)=g_{S,2}(Z).
\]
主除子判据参Sutherland 18.783 (2025)
[Lecture 23, Corollary 23.19](https://ocw.mit.edu/courses/18-783-elliptic-curves-fall-2025/mit18_783_f25_lec23.pdf)。

对$M_a$与$Z\mapsto g_{S_a,d}(Z-Q_a)$使用Weil互反，准确得到
\[
 \prod_{i\in\mathbb F_p}M_a(Q_a+iS_a)^{b_i}
    =\prod_tg_{S_a,d}(\phi_aT_t-Q_a)^{I_t}
                       \qquad\text{于 }L_2^\times . \tag{BX2}
\]
两个除子不交：移动点均为$p$幂挠，而原$T_t$保留非零的
$\mathfrak f$之17分量。此处使用的标准式是
$f(\operatorname{div}g)=g(\operatorname{div}f)$；
参Poonen，[Lectures on rational points on curves, Theorem 1.9.5](https://math.mit.edu/~poonen/papers/curves.pdf)。
任何Miller归一常数也因$\sum I_t=0$在完整驯评价中消失。
(BX2)是所选整提升的准确值；改变提升只在(BX1)的模$p$ Kummer类中相同。

### 每条线一个Miller函数及全部原角权

取$\Omega/\mathbb F_p^\times$的$p+1$个代表$a_L$。
写$a=a_Ln$，$n\in\mathbb F_p^\times$。准确有
$\omega(a)=\omega(a_L)\omega(n)\bmod p^2$；
$\omega(n)$是$(\mathbb Z/p^2)^\times$中的乘法Teichmüller提升，
通常不是最小正整数$n$。于是
\[
 C_a=C_L,\quad E_a=E_L,\quad
 S_a=[n]S_L,\qquad Q_a=[\omega(n)]Q_L.
\]
在$S_L$上可直接用$n$，因为其阶为$p$。

置
\[
 F_{L,d}(Q)=\prod_tg_{S_L,d}(\phi_LT_t-Q)^{I_t}.
\]
若$c_n$是$n^{-d}\bmod p$的任一整提升，则
\[
 \operatorname{div}\!\left(g_{[n]S_L,d}/g_{S_L,d}^{c_n}\right)
                         =pD ,
\]
因为$[iS_L]$的两重数之差为$b_{i/n}-c_nb_i\equiv0$。
$D$是支撑于$\langle S_L\rangle$的整有理除子，**不需要$D$为主**。
将此商平移$Z-Q$，对$M_L$再次应用Weil互反，得到
\[
 \prod_t
  \left(g_{[n]S_L,d}/g_{S_L,d}^{c_n}\right)
                         (\phi_LT_t-Q)^{I_t}
   =\left(\prod_R M_L(Q+R)^{\operatorname{ord}_R D}\right)^p .
                                                               \tag{BX3}
\]
故在原$L_2$中真正只差一个$p$次幂，不借代数闭包任取根，
也不把$D$误判为主除子。

代回(BX1)，同一实际Kummer行准确为
\[
 Y_{\lambda,d}
   =\sum_{L\in\Omega/\mathbb F_p^\times}a_L^{-1}
        \sum_{n\in\mathbb F_p^\times}n^{-1-d}
          [\,F_{L,d}([\omega(n)]Q_L)\,]. \tag{BX4}
\]
每线仅需一个$g$，线性、平方行分别保留$n^{-2},n^{-3}$的真角权。
原$I_{-t}=-I_t$及$g$的奇偶给
$F_{L,1}(-Q)=F_{L,1}(Q)$、
$F_{L,2}(-Q)=F_{L,2}(Q)^{-1}$，所以$n,-n$配对在两行均同向，
可取任一$\pm$代表再乘二。

这一步确实利用原固定除子，超过§107形式群环倍的范围。
$g$与$E_L$仍随$p,C_L$变化；(BX4)保留固定$I_t$的全部驯支撑及
$p+1$条线，尚未证明完整角色和在无穷$p$非零。

## 109. 普通两位完整范数与原固定M的两个高度一系数

取$p>211$普通分裂，$\pi=\psi_{17}(\mathfrak p)$、
$\alpha=\psi_{17}(\bar{\mathfrak p})=\bar\pi$，在$\mathfrak p$嵌入中工作。
先假设$\alpha-1\in\mathbb Z_p^\times$，下文给固定分裂列保证它。
保持(BT1)同一$M\in\mathbb Q(E_{17})^\times$、
(BT5)整个平滑单位及(BU2)两个野变量。§104的逐除子证明在所选普通CM行
逐字成立：逆Tate权取$\mathfrak p$分量，$\varepsilon(p)=1$，
所有$\mathfrak f$和另一$p$位仍保留。

令$P_j,R_j$为原
$[\mathfrak f^{-1}]\varpi_{17}/p^j$的$\pi^j,\alpha^j$主分量，
两者皆本原。固定$\pi$方向标量$w$，把另一野变量取零、其驯测试取原标量一。
整个étale方向的真实乘积为
\[
 \prod_{v\in(\mathbb Z/p^j)^\times}
       M([w]P_j+[v]R_j)
      =\frac{M([\alpha^jw]P_j)}
             {M([\alpha^{j-1}w]P_j)}. \tag{BY1}
\]
这是从完整$E[\alpha^j]$中除去$E[\alpha^{j-1}]$的两个函数域范数；
(BT6)保证每次常数准确为一。

在$w$重标后，原逆Tate/群环权使(BY1)贡献
\[
 \alpha^{j-1}[g_\alpha]^{j-1}(\alpha[g_\alpha]-1),
                  \qquad g_\alpha=\langle\alpha\rangle .
\]
其常项$\alpha^{j-1}(\alpha-1)$为单位。因此若通常全
$\Sha[p^\infty]$无限，(BU4)给每个$k$、$j=k+1$的真实单变量截断
\[
 \sum_w w^{-1}[g_w]^{-1}M([w]P_j)
                         =0\pmod{p^k,(g-1)^3} \tag{BY2}
\]
于原完整射线层Kummer张量。固定平滑及$\varepsilon(p)^j(1+\omega)/6$
均为单位；全过程没有先删高阶项或未经证明地忽略étale因子。

若$p$完全分裂于一个固定有限正规域$\mathscr M$，其中含
$K,\theta=17^{1/6}$，则$E_{17}/\mathbb F_p\simeq E_1$。
$E_1(\mathbb F_p)$有显式2、3挠点，故点数被六整除；
$p\equiv1\bmod6$给$a_p\equiv2\bmod6$。由Hasse界和$p>211$，
$a_p\equiv1\bmod p$只可能$a_p=1$，与前式矛盾。
而$\alpha\bmod p=a_p\bmod p$，遂在此固定分裂列始终有
$\alpha-1\in\mathbb Z_p^\times$。交换两CM嵌入也成立；
需要时将$\theta$并入原固定标记域，仍保持其为固定有限域。

### 原微分的头两项准确消失

$s$取原$E_{17}$在$\mathfrak p$处的导数一严格LT坐标，
$[\pi]s=\pi s+s^p$。其存在来自$[\pi]$在特殊纤维为实际Frobenius。
置$b=p-1$，
\[
                  B_j^{\rm ord}=[s^{jb}]\,d\log M/ds .
\]
由原102挠除子函数有
$d\log M=-\sum_t I_t\kappa_{T_t}$；这是比较$M^{102}$
与同除子函数乘积后求微分，没有增加全纯差。
首常数为$-\sum_tI_tX(T_t)=0$：
$I_t$是$\varepsilon,\bar\varepsilon$的固定线性组合，
前者用原$L(E_{17},1)=0$，后者由六次单位的非平凡权消去。
故$B_0^{\rm ord}=0$。Cartier固定$d\log M$，再给
$B_1^{\rm ord}=0\bmod p$。

令$\Delta=\mu_{p-1}$，在整形式单位群取
\[
 U(s)=\prod_{u\in\Delta}
       M([u]s)^{u^{-1}/(p-1)}\in1+s\mathbb Z_p[[s]].
\]
$p$进整指数用二项式级数解释；$[u]s=us$，所以其模$p$对数微分
准确保留所有$B_j^{\rm ord}$。

### 保全非分歧扩张的Kummer首阶检测

取$j=2,k=1$、$g=1+p$、$F=K_{\mathfrak p}(E[\pi^2])$。
允许任意有限非分歧扩张后，$\xi=s(P_2)$仍为素元，$e=p(p-1)$。
原全$L_2$在当地相对于$F$至多多出未分歧扩张：
固定$\mathfrak f$及étale $\alpha^2$挠都如此。以下检测在这些扩张后仍成立，
无需声称一般限制映射单射。

$\mathbb F_p[C_p]$中的三个实际测试
$\sum_i\binom{-i}r g^i$、$r=0,1,2$，依序形成
$(g-1)^{p-1},(g-1)^{p-2},(g-1)^{p-3}$的上三角单位基。
模$p$野逆Tate权已是驯权。因此(BY2)迫
$(g-1)^{p-3}U(\xi)$为当地$p$次幂。

实际作用为
\[
                 g\xi=\xi+A\xi^p+O(\xi^{p+1}),
                     \qquad A\bmod p=\alpha\ne0 .
\]
确实$[p]=[\alpha][\pi]$，代入LT加法的首项即得。
假设$B_2^{\rm ord}$或$B_3^{\rm ord}$为第一个非零项，分别令
$n=2p-1$或$3p-2$。在剩余域形式级数中除去一个形式$p$次幂后，
$U$的首项为$1+B s^n$、$B\ne0$。
把该根整提升后代$\xi$，$p$整误差的阶至少$e>3p$，
所以同一Kummer类确有首项$1+B\xi^n$。

连续作用$g-1$共$p-3$次，首阶为
\[
       n+(p-3)b=
       \begin{cases}
          p^2-2p+2,&n=2p-1,\\
          p^2-p+1,&n=3p-2,
        \end{cases}
\]
首系数为$B A^{p-3}\prod_{i=0}^{p-4}(n+ib)$，各因子模$p$非零。
$g$固定非分歧系数，更高项和原$p$整误差不改变该首阶。
两个阶数都小于$pe/(p-1)=p^2$且不被$p$整除。

单位的$p$次幂在这个界以下的非零首阶必被$p$整除：
直接比较$(1+x)^p$中的$x^p$与$px$，在交界$p^2$以下只有前者能给首项。
这与(BY2)矛盾。故在上述完整普通范围有
\[
 \boxed{\quad
 \Sha(E_{17}/\mathbb Q)[p^\infty]\text{无限}
            \ \Longrightarrow\
 B_2^{\rm ord}=B_3^{\rm ord}=0\bmod p .
 \quad} \tag{BY3}
\]

### 原不变对数中的精确两个整组合

令$f(z)=D\log M(z)=\sum f_nz^n$，其中$z$是原不变对数；
写LT对数
\[
 \ell(s)=s+\ell_1s^{b+1}+\ell_2s^{2b+1}+\cdots,\qquad
 \ell_1=(\pi-\pi^p)^{-1},\quad
 \ell_2=\frac{p\pi^{p-1}\ell_1}{\pi-\pi^{2p-1}}.
\]
这些值由$\ell(\pi s+s^p)=\pi\ell(s)$逐次比较。
因$f_0=0$，原两个整行准确为
\[
 \begin{split}
 B_2^{\rm ord}&=f_{2b}+(2b+1)\ell_1f_b,\\
 B_3^{\rm ord}&=f_{3b}+(3b+1)\ell_1f_{2b}
             +(3b+1)(\ell_2+b\ell_1^2/2)f_b .
 \end{split} \tag{BY4}
\]
这是$[s^{jb}]f(\ell(s))\ell'(s)$的完整系数；所有显示组合整，
不能先将带分母的个别项取模$p$。
它们来自同一固定有理除子的原完整源，尚未证明与AQ全部曲率相同，
也没有由这些必要零本身宣称跨$p$非零。
