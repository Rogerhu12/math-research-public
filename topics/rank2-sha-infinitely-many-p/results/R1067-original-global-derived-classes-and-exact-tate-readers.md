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
