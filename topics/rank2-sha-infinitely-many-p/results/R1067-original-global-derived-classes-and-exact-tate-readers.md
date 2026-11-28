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
