# 同一辅助素数的整增广条件：全精度、CRT 与高度预算

日期：2026-11-12。状态：本篇的群环恒等式、整局部化判据和高度比较均已证明。
没有证明原 Heegner 点的第二导数必消失，也没有由联合整除推出主目标。

固定本课题的 $E=E_{17}$、$F=\mathbb Q(\sqrt{-15})$，以及一个在
$F$ 和 $\mathbb Q(i)$ 中均惰性的辅助素数 $\ell$。令
$m=\ell+1$，$K=H_\ell^{\langle\tau_3\rangle}$ 是 R105 在类数二迹之后的实际循环扩张，
$\Gamma=\operatorname{Gal}(K/F)=\langle\sigma\rangle\simeq C_m$。
令 $X=\Phi(z_\ell)=(1+\tau_3)P[\ell]$ 为实际类数二迹点；
需要时统一乘 $2$ 清掉已知挠点。
于是 $NX=0$，其中 $N=\sum_{j=0}^{m-1}\sigma^j$。

以下取真实无挠 Mordell--Weil 格
$$
 G=E(K)/E(K)_{\rm tors},\qquad W=\ker(N:G\longrightarrow G),
 \qquad I=\sigma-1.
 \tag{1}
$$
在奇素数处，由 R107 的 $E(F^{\rm ab})_{\rm tors}=E[2]$，
在这个格中判定整除，与实际点的 $p$ 进完成中的判定相同。
本篇没有把任何除以群阶的有理迹当成可应用 Baker 下界的整数点。

## 1. 一次导数的全部精度仍是一次增广除法

先令 $\Gamma=C_n$、$n=p^e$，其中 $p$ 为奇素数。写
$$
 D^{(k)}=\sum_{j=0}^{n-1}\binom jk\sigma^j,
 \qquad D^{(0)}=N.
$$
直接移动求和指标得到
$$
 I D^{(1)}=n-N,\qquad
 I D^{(2)}=\binom n2-\sigma D^{(1)}.
 \tag{2}
$$
在 $W$ 上 $I$ 没有有理核；这是因为 $I$ 的核是 $\Gamma$ 不变部分，
而 $N$ 在该部分是乘 $n$。

对实际 $X\in W$，有准确等价
$$
 \boxed{D^{(1)}X\in nG\quad\Longleftrightarrow\quad X\in IW.}
 \tag{3}
$$
若 $D^{(1)}X=nY$，则 (2) 和 $G$ 无挠给 $IY=X$；再由
$nNY=ND^{(1)}X=0$ 得 $NY=0$，故 $Y\in W$。
反向将 $X=IY$ 代入 (2) 即得 $D^{(1)}X=nY$。

因此，对于同一个 $n=p^e$，一次导出点在所有允许的
$p^M$ 精度 $M\le e$ 消失，最强条件就是 $M=e$ 的 (3)。
低精度条件已被它包含；**增加精度不是再增加一次导数**。
R100/R104 的实际 Kummer 下降把一次类的零性接到 (3)，
但没有仅凭这一步产生 $I^2W$。

## 2. 真正的二阶整数判据

在 $p$ 进完成中还有
$$
 \boxed{\begin{aligned}
 X\in I^2(W\otimes\mathbb Z_p)
 \quad\Longleftrightarrow\quad&
 D^{(1)}X\in p^e(G\otimes\mathbb Z_p),\\
 &D^{(2)}X\in p^e(G\otimes\mathbb Z_p).
 \end{aligned}}
 \tag{4}
$$
证明：先由第一条件写 $X=IY$、$Y\in W\otimes\mathbb Z_p$。
若第二条件成立，置 $Z=D^{(2)}X/n$；同样由取范数知 $Z\in W\otimes\mathbb Z_p$。
第二条 (2) 给
$$
 IZ=\left(\frac{n-1}{2}I-\sigma\right)Y.
 \tag{5}
$$
括号内元素在 $\mathbb Z_p[C_{p^e}]$ 的 augmentation 为 $-1$。
这个群环是局部环，故该元素是单位；与 $I$ 交换后，(5) 给
$Y\in I(W\otimes\mathbb Z_p)$。反向若 $X=I^2V$，则
$$
 D^{(1)}X=nIV,\qquad
 D^{(2)}X=n\left(\frac{n-1}{2}I-\sigma\right)V,
$$
直接给出所需整除。

(4) 的右边第二行是需要另外证明的实际高阶消失条件。
仅说原曲线有可除 Sha、然后引用一次类的所有精度消失，尚未支付它。
当另有 R122/R125 的秩一角色格及符号输入时，可以在其已证明范围
得到相应点的指数至少二；不能不检查格与局部条件就把该结论搬到
所有 $C_{p^e}$ 层。

## 3. 同一 m 的 p-primary CRT 是整的，但只检测相应块

回到任意 $m$。对 $p^e\Vert m$，令
$$
 u_p=m/p^e,\quad U_p=\langle\sigma^{p^e}\rangle,
 \quad Q_p=N_{U_p}X,
 \quad e_p=\frac1{u_p}N_{U_p}\in\mathbb Z_p[\Gamma].
 \tag{6}
$$
$Q_p$ 是真正的整数迹，定义在 $K^{U_p}$ 上。
$e_p$ 在这里仅用于证明 $p$ 进整格分解，不当成整数点。

在 $(1-e_p)\mathbb Z_p[\Gamma]$ 上，$\sigma-1$ 是单位。
一个直接证明是：模 $p$ 后 $\Gamma$ 的 prime-to-$p$ 部分有阶 $u_p$，
在其非平凡角色上 $\sigma-1$ 没有零特征值；该有限自由 $\mathbb Z_p$
代数中的逆由模 $p$ 可逆性提升。等价地，相关因子在 $T=1$ 的值
是 $p$ 进单位。

在 $e_p$ 块上，可用 $\sigma_p=\sigma^{u_p}$ 作为 $C_{p^e}$ 生成元。
因为 $u_p$ 与 $p$ 互素，$\sigma_p-1$ 与 $\sigma-1$ 只差单位。
对所有 $k\ge0$，因此有准确等价
$$
 \boxed{
 X\in I^k(W\otimes\mathbb Z_p)
 \quad\Longleftrightarrow\quad
 Q_p\in(\sigma_p-1)^k(W^{U_p}\otimes\mathbb Z_p).
 }
 \tag{7}
$$
这里用 $N_{U_p}=u_pe_p$、$u_p\in\mathbb Z_p^\times$，以及
prime-to-$p$ 不变部分与 $p$ 进完成交换。由实际点解释不变部分时，
可能的挠点误差是 $2$ 初级，在本篇的奇素数处可逆。

由于 $ID=m$ 在 $W$ 上成立，$m^kW\subset I^kW$。
所以 $W/I^kW$ 是仅支撑于 $p\mid m$ 的有限群。
令 $S$ 是任何固定有限素数集合；逐个有限群初级部分判定给
$$
 \begin{aligned}
 X\in I^k(W\otimes\mathbb Z[S^{-1}])
 \quad\Longleftrightarrow\quad
 \text{(7) 对每个 }p\mid m,\ p\notin S\text{ 成立}.
 \end{aligned}
 \tag{8}
$$
若要回到完整整数格，可乘
$m_S^k$，其中 $m_S=\prod_{p\in S}p^{v_p(m)}$。
只有在另行把这些小素数赋值限定为有界时，这才是统一的固定倍数。

**不能省略的范围。** 若 $e>1$，只知道次数 $p$ 商上的一个 $Q$，
并不等于知道 (6) 的整个次数 $p^e$ 商。前者的范数中还含
$p^{e-1}$，不能作为 $\mathbb Z_p$ 中可逆的平均来处理。
同样，(7) 在 $p$ 处只限制 prime-to-$p$ 部分平凡的块；
具有真正混合导子的角色处，$I$ 本来就是局部单位。

## 4. 低导子投影的真实高度：正交和，不是乘积

在 $W_\mathbb Q=W\otimes\mathbb Q$ 上使用 Néron--Tate 二次型。
Galois 作用为等距作用，故每个 $e_p$ 是正交投影。
若 $p\ne q$，两个投影之积是到 $\Gamma$ 不变部分的投影，
在 $W_\mathbb Q$ 上为零。于是实际整数迹满足
$$
 \boxed{\quad
 \sum_{p\mid m}\frac{\widehat h(Q_p)}{u_p^2}
       \le \widehat h(X).
 \quad}                                                     \tag{9}
$$
余下的非负项恰来自混合导子部分。
这是真实点之间的准确高度比较，不需要猜测各角色的高度相等。

若每个非零 $Q_p$ 使用 Baker 的固定下界 $c_E>0$，(9) 只给
$$
 \widehat h(X)\ge c_E\sum_{Q_p\ne0}u_p^{-2}.
 \tag{10}
$$
不能把右边的有理点 $e_pX=Q_p/u_p$ 直接套同一个下界。
完整低导子投影 $\sum e_p$ 的可用整清分母为
$D=\operatorname{lcm}_{p\mid m}u_p$；若 $m$ 至少含两个不同素因子，
$D=m$。因此直接取 $D\sum e_pX$ 的高度上界是
$D^2\widehat h(X)$，而非原来的 $O(\log\ell)$。

这个分母在整个循环正规表示的增广格上确实是必要的：固定
$p^e\Vert m$，并在另一个素数 $q\mid m$ 的非平凡角色块中考察
$p$-群方向，低导子投影等于 $N_{C_{p^e}}/p^e$，其分母正是
$p^e$。对每个 $p$ 都如此。对某个实际 MW 子空间，若已证明
相应混合块或整粘合消失，分母可以变小；本篇没有假设这一点。

还有一个可直接核对的行列式说明。对真实循环轨道子空间
$V=\mathbb Q[\Gamma]X$，每个非零有理不可约角色块只出现一次。
设其低导子块集合为 $\mathcal D\subset\{p^r:p^r\mid m\}$，则
$$
 \dim V_{\rm low}=\sum_{d\in\mathcal D}\varphi(d),\qquad
 |\det(I|V_{\rm low})|=
       \prod_{p^r\in\mathcal D}p.
 \tag{11}
$$
这是 $\Phi_{p^r}(1)=p$ 的直接结果；混合导子满足 $\Phi_d(1)=1$。
因此 $I^2$ 子格的 Gram 行列式变化是 $\prod p^4$，
其按**整个**低导子空间维数取的几何平均为
$$
 \exp\!\left(
 \frac{4\sum_{p^r\in\mathcal D}\log p}
      {\sum_{p^r\in\mathcal D}\varphi(p^r)}\right).
 \tag{12}
$$
它不是把不同维数空间的平均各乘一次而得到的
$\prod p^{4/(p-1)}$。
例如 $m$ 是到 $B$ 的 primorial、所有素导子块均出现时，(12) 的
对数为 $O(\log B/B)$，趋于零；而 $\log m\asymp B$。
这里仅用素数定理作该例的数量说明；准确等式是 (11)--(12)。
本篇并未从某个 Gram 行列式下界推出未证明的单点高度下界。

## 5. 一个实际固定映射校准：联合 I² 本身不违背小高度

本节只校准上述高度论证，不把新点替代原点。
固定 $\mathfrak b=(1+2\sqrt{-15})$，$N\mathfrak b=61$，并令
$s=\operatorname{Art}(\mathfrak b)$（反向约定只将其倒置）。
对同一个实际 $X$，点
$$
                         X'=(s-1)^2X                       \tag{13}
$$
在整个 $C_m$ 的整格中都属于 $I^2W$，因为 $s=\sigma^j$。
这并非一个抽象格模型：沿 $\mathfrak b^2$ 的水平 $61$-同源链，
(13) 正是固定代数映射
$$
 \Phi\circ d_2-2\Phi\circ d_1+\Phi\circ d_0:
 X_0(61^2\cdot3N_E)\longrightarrow E
 \tag{14}
$$
在相应 CM 点的值。这里 $\Phi$ 是 R105 的原类数二迹映射，
$d_i$ 是三条标准退化映射。统一采用使水平链对应 $s^i$ 的标记。
若采用另一 Artin 方向，所得为 $(s^{-1}-1)^2X$，结论相同。

(14) 的拉回微分的 $q^1$ 系数与 $\Phi^*\omega_E$ 相同且非零：
三项分别是原级数、$61$ 倍的 $q\mapsto q^{61}$ 级数、
$61^2$ 倍的 $q\mapsto q^{61^2}$ 级数，带系数 $1,-2,1$。
故 (14) 非恒定。R102/R105 对固定非恒定模映射的高度比较于是给
$$
                       \widehat h(X')\asymp\log\ell
 \tag{15}
$$
对充分大的相应 CM 点成立。也可直接由 (13) 的固定系数和
$\widehat h(X)=O(\log\ell)$ 得其所需上界。

在 R126/R128 已选的实际 $p$ 商上，$s$ 是生成元，
$Q'_p=(s-1)^2Q_p$ 的整指数为 $a'_p=a_p+2$。
它仍然是非挠实际点；其高度仍为 $O(u_p^2\log\ell)$。
因此，仅凭同一个固定映射的高度量级、所有这些增广像条件和
范数零性，不能得到矛盾。真正需要保留的是**原** Heegner
映射的算术原始性，不能把 (14) 的新退化组合当成原始类。

## 6. 当前可使用的结论与来源范围

已付的是 (3)、(4)、(7)--(9) 的完整整数/完成格接口。
若反设原曲线初级 Sha 对所有大 $p$ 有非零可除部分，已用的一次
Kolyvagin 判据只给其相应一次类消失；不能在此处自行增加 (4)
的二阶消失。即使某条更强定理将它付清，联合得到的整 $I^2$
及低导子高度仍须按 (9)--(12) 处理。

群环微分的背景见 Henri Darmon，*A refined conjecture of
Mazur--Tate type for Heegner points*（1992），§3.1；
[作者保存的发表版](https://www.math.mcgill.ca/darmon/pub/Articles/Research/05.Refined-conjecture/pub5.pdf)。
上述 (2)--(4) 已在文内直接证明，不依赖其高阶消失定理。
该文主定理的系数环须倒置非满 $\mathrm{GL}_2(\mathbb Z_p)$
像的素数（作者重排版 §2.1，Theorem 2.4 前），故不能直接把它
当成本题 CM 曲线在所有 $p$ 的二阶消失输入。
实际 Heegner 点及高度只用 R102、R104--105、R107、R126、R128
中已证明并标明原始来源的接口。
