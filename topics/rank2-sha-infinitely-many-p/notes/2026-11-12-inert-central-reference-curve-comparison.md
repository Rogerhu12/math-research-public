# 惰性中央权的参考曲线比较：消去局部周期后的整判据

日期：2026-11-12。状态：已证明；所需无穷多个中央单位仍开放。

本篇比较两条固定曲线

$$
 E_{17}:y^2=x^3-17x,\qquad E_0:y^2=x^3-x,
 \qquad K=\mathbb Q(i).
$$

其导子生成元分别取

$$
 f_{17}=34(1+i),\qquad f_0=2(1+i).
$$

所有赋值均按 $v_p(p)=1$ 归一化。固定

$$
 p\ge7,\qquad p\equiv3\pmod4,\qquad
 \mathcal O=\mathcal O_{K_p},\quad K_p=\mathbb Q_{p^2}.
 \tag{0.1}
$$

两条曲线的中央系数采用同一 reduced Kronecker theta 规范，
写成 $d_m^{(17)}$ 与 $d_m^{(0)}$。前者就是课题中已有的 $d_m$。

**比较的结论。** 存在一个整幂级数

$$
 A_p(T)\in\mathcal O[[T]],\qquad
 2\le s_p\le\operatorname{ord}_{T=0}A_p(T),
 \tag{0.2}
$$

其中 $s_p$ 是 $E_{17}/\mathbb Q$ 的基层 $p^\infty$-Selmer 余秩。
在第一个保持同一 tame 特征的中央权 $m=p+1$，有一个
$x_p\in p\mathcal O$，$v_p(x_p)=1$，使

$$
 \boxed{\quad
 v_p A_p(x_p)=v_p d_{p+1}^{(17)}+2.
 \quad}                                                       \tag{0.3}
$$

这里没有把惰性 Lubin--Tate 周期视为单位；该周期在两条曲线的
**同一个局部整模、同一个 specialization map** 中抵消。
因此

$$
 \boxed{\quad
 v_p d_{p+1}^{(17)}\le1
 \quad\Longrightarrow\quad
 \Sha(E_{17}/\mathbb Q)[p^\infty]\text{ 有限}.
 \quad}                                                       \tag{0.4}
$$

特别是 $d_{p+1}^{(17)}$ 为单位足够。这尚未证明该条件对无穷多个
惰性素数成立。

## 1. 同一个局部表示与同一个反圆分参数

记 $\varphi_j$ 为 $E_j$ 的 CM Hecke 特征，使用其算术理想上的
type $(1,0)$ 规范。与 Kato 的 type $(-1,0)$ 记号之间只差
他对无穷分量的约定；需要时同时共轭两边。

### 1.1 四次扭转在惰性局部域上消失

群 $\mathbb F_{p^2}^{\times}$ 为循环群，且 $4\mid p+1$。
其子群 $\mathbb F_p^{\times}$ 包含在四次幂子群中。因此可在
$\mathcal O^{\times}$ 中选 $a$ 满足 $a^4=17$，并得到实际代数同构

$$
 F_a:E_0\longrightarrow E_{17},\qquad
 (x,y)\longmapsto(a^2x,a^3y).
 \tag{1.1}
$$

两条曲线在 $p$ 处的上述方程均是光滑整模型，故 (1.1) 同时给出
光滑整模型、形式群及完整 Tate 格的同构。若
$\omega_j=dx/(2y)$，则

$$
 F_a^*\omega_{17}=a^{-1}\omega_0.
 \tag{1.2}
$$

特别是这是单位微分变换；没有把一个有理 Tate 空间同构错误地
当作整同构。它与 $\mathcal O_K$ 的作用及 Weil pairing 相容。

### 1.2 全球中央字符也相同

两条全球 Hecke 特征之比是四次有限特征 $\eta$。因此当 $4\mid m$ 时，

$$
 \chi_m
 =\left(\frac{\varphi_{17}}{\overline\varphi_{17}}\right)^m
 =\left(\frac{\varphi_0}{\overline\varphi_0}\right)^m.
 \tag{1.3}
$$

这里 $\overline\varphi$ 的有限值与 $\varphi^{-1}$ 相差范数，
所以两边的四次扭转商贡献是 $\eta^{2m}=1$。
更直接地，在避开导子的主理想 $(b)$ 上，两边都等于
$(b/\bar b)^m$；有限单位角色在 $4\mid m$ 时消失。

设 $\kappa$ 是在 $K_p$ 上的 Lubin--Tate 特征，$\tau$ 是未分歧
二次域的非平凡自同构。局部反圆分特征为

$$
 \kappa_{\rm ac}=\kappa/\kappa^\tau.
$$

它在 $\mathbb F_{p^2}^{\times}$ 上的指数是 $1-p$。因而
$\kappa_{\rm ac}^m$ 的 tame 部分消失恰当且仅当 $p+1\mid m$。
对这样的正整数 $m$，(1.3) 是同一个反圆分 $\mathbb Z_p$-扩张
$K_\infty/K$ 的连续特征。类数 $h_K=1$，无需再处理一个有限
非 $p$ 商。

固定 $\Gamma=\operatorname{Gal}(K_\infty/K)$ 的生成元 $\gamma$。
令

$$
 q=\kappa_{\rm ac}(\gamma),\qquad T=\gamma-1,
 \qquad x_m=q^m-1.
 \tag{1.4}
$$

局部类域论给 $\Gamma\simeq(1+p\mathcal O)^{N=1}$。
因 $u\mapsto u/\bar u$ 在其反不变 Lie 格上是乘以 $2$，
可且固定取 $v_p(q-1)=1$。于是

$$
 v_p(x_m)=1+v_p(m).                                         \tag{1.5}
$$

若以逆特征定义 Iwasawa 作用，则同时将 $q$ 换成 $q^{-1}$；
这只是整参数自同构 $T\mapsto(1+T)^{-1}-1$，不改变以下赋值
或中心消失阶。本文用 specialization 到 $\chi_m^{-1}$-扭转表示时
评价于 $\chi_m$ 的规范。

## 2. signed 局部整格：参考椭圆单位本身是原始基

这一节先解决整格问题，随后才比较 de Rham period。

令 $T_j=T_pE_j$，视为秩一 $\mathcal O$-模，并置

$$
 M_j=\varprojlim_n
 H^1(K_{n,p},T_j^{-1}(1)).
 \tag{2.1}
$$

Burungale--Kobayashi--Ota 的局部 Rubin 定理及其上同调表达给

$$
 M_j=M_j^+\oplus M_j^-,\qquad
 M_j^\pm\simeq\mathcal O[[\Gamma]].
 \tag{2.2}
$$

这是完整整模的分解，不是忽略有限模的伪同构。
出处是 [BKO21] Theorem 2.1，以及 [BKO24] §2.2.1 的 (2.3)--(2.9)
和 Theorem 2.1。$+$ 包含平凡特征这一奇偶规范与 [BKO21] §6 一致。

signed 子模由有限阶特征下 dual exponential 的消失定义。
实际整同构 (1.1) 与限制、corestriction、Bloch--Kato 指数映射
相容，故诱导

$$
 F_a^*:M_{17}\xrightarrow{\sim}M_0,
 \qquad F_a^*(M_{17}^\pm)=M_0^\pm.                          \tag{2.3}
$$

最后的等式先由定义得到两个包含关系，再用逆同构得到相等；
不能仅由两个有理 signed 直线相同来推断它。

以 Néron 微分和原始 Betti $\mathcal O_{K,(p)}$-基定义标准的
椭圆单位类 $z_j$，如 [BKO24] Proposition 3.1、(3.2)。记其局部像
为 $\xi_j$。两条曲线的根数均为 $+1$，所以

$$
 \xi_j\in M_j^+.
 \tag{2.4}
$$

这里使用 [BKO24] Definition 3.13 的标准类；没有在高权处另乘
一个不知赋值的代数数。该构造对 $E_{17}$ 合法，因为
[BKO24] §3.1.1 只要求相应 Q-curve 在 $p$ 处好约化，
不要求其导子仅支撑在 $K/\mathbb Q$ 的分歧素数。

参考曲线的真实导子点 $S=(i,1-i)$ 满足 $[2]S=(0,0)$。
sigma duplication 给

$$
 d_0^{(0)}=\frac{1+i}{2},\qquad
 \frac{d_0^{(0)}}{f_0}=\frac14.
 \tag{2.5}
$$

见 [参考值笔记](2026-11-12-rank-zero-reference-central-inert-value.md)
§1。这也给 $L(E_0,1)/\Omega_0$ 为 $p$-单位；相位改变只乘
$\mu_4$，不影响这一结论。

[BKO24] Corollary 4.11(i) 的证明明确使用：若
$L(E,1)/\Omega$ 为单位，则 Definition 3.13 的 Rubin 函数
$\mathscr L$ 属于 $\Lambda^\times$。因此

$$
 \boxed{\quad M_0^+=\Lambda\xi_0,\qquad
 \Lambda=\mathcal O[[T]].\quad}                            \tag{2.6}
$$

结合 (2.3)，有唯一 $A_p(T)\in\Lambda$ 使

$$
 F_a^*(\xi_{17})=A_p(T)\xi_0.                              \tag{2.7}
$$

这给出 (0.2) 中所需的整幂级数。如果改选任何一个局部 signed
原始基，则它与 $\xi_0$ 相差 $\Lambda^\times$；这一点来自
自由秩一整模，完全不是对某个未知 $p$-adic period 赋值的假设。
对 $x\in p\mathcal O$，该单位幂级数的值仍是 $\mathcal O^\times$。

## 3. 混合无穷型 reciprocity 的确切来源

所需特征 $\chi_m$ 有无穷型 $(m,-m)$。
它一般仅为 $\mathbb Q_p$-analytic，不是单嵌入
$K_p$-analytic。单一 Lubin--Tate Coates--Wiles 导数的插值范围
不够，因此本篇使用 Kato 的全临界值定理。

### 3.1 使用的定理链

对 $r=2m+1$，Kato [K04] §15.8 把 $V(\varphi_j^r)$ 定义为
CM 椭圆曲线 $H^1$ 的 $r$ 次、在 CM 域上的 tensor power。
相应的 $S(\varphi_j^r)$ 是 $\operatorname{coLie}(E_j)^{\otimes r}$
的下降，且 $\mathrm{per}_{\varphi_j^r}$ 由椭圆曲线自身的
period map 作 tensor 后得到。

Kato Proposition 15.9 给顶临界值的椭圆单位 reciprocity。
进一步，Lemma 15.11 用同一个任意的
$S(\varphi_j^r)\to S(f_j^{(r)})$ 同构分别正规化 étale 与 Betti
比较；式 (15.16.1) **证明**该椭圆单位类映到对应 Betti 向量的
Beilinson--Kato 类。于是 Theorem 12.5(1) 可以用于

$$
 k=2m+2,\qquad r_{\rm crit}=m+1.                            \tag{3.1}
$$

将该定理的 de Rham 结论经 Lemma 15.11 的图拉回 CM tensor
线，所得共同的复 Tate 因子为
$(2\pi i)^{k-r_{\rm crit}-1}=(2\pi i)^m$。

这里必须在完整的二变量射线类塔上核对 specialization，不能只
由有限阶特征的插值公式外推。具体记

$$
 \mathcal G_j=\operatorname{Gal}(K(p^\infty f_j)/K),\qquad
 \mathbf u_j\in
 S^{-1}H^1_{\rm Iw}(K(p^\infty f_j),\mathbb Z_p(1))
 $$

为同一个标准椭圆单位系统；$S^{-1}$ 表示只局部化去除辅助理想的
Euler 算子。等价地，可全程用一份整的辅助椭圆单位，再在两条
路线的末端除以同一个算子。这里该除法确实合法且为单位：
选一个惰性辅助素数 $\ell\equiv1\pmod p$，$\ell\nmid2\cdot17p$。
主理想 $(\ell)$ 在反圆分塔中作用平凡，
$\varphi_j((\ell))=-\ell$，所以 [BKOY25] §5.4.2 的辅助算子
在两条目标角色中的像均为
$\ell^2+\ell^{-1}\equiv2\pmod p$。这样的 $\ell$ 由
Dirichlet 定理存在；它只用于选择同一个标准类的整表达。

$b_j$ 在 étale 侧对应 $T_j^{-1}$ 的基。两条路线的目标都为

$$
 H^1\bigl(K,T_j^{-(2m+1)}(1+m)\bigr),
 \qquad
 \rho_{j,m}=\varphi_j^{-(2m+1)}\chi_{\rm cyc}^{1+m}.
 \tag{3.1a}
$$

第一条路线先用 $b_j$ 扭转，得到基层表示 $T_j^{-1}(1)$ 的
二变量 Iwasawa 类，再沿反圆分塔限制，最后在 $\chi_m$ 评价。
由于

$$
 \chi_m^{-1}
   =\varphi_j^{-2m}\chi_{\rm cyc}^{m},
 $$

目标向量是 $\mathbf u_j\otimes b_j^{\otimes(2m+1)}
\otimes\zeta^{\otimes m}$。
第二条路线先将同一个 $\mathbf u_j$ 乘
$b_j^{\otimes(2m+1)}\otimes\zeta^{-1}$，得到
$V(\varphi_j^{2m+1})$ 的 cyclotomic Iwasawa 类。
Kato (15.16.1) 把它识别为对应高权 Beilinson--Kato 类。
Theorem 12.5 的中心 specialization 再乘
$\zeta^{k-r_{\rm crit}}=\zeta^{m+1}$，得到同一个向量。
也就是说，以下两条复合是对同一 $\mathcal O[[\mathcal G_j]]$
上同调类按同一角色 $\rho_{j,m}$ 作基变换：

$$
 \begin{aligned}
 \mathbf u_j
 &\longmapsto\mathbf u_j\otimes b_j
   \longmapsto
   \mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m},
 \\
 \mathbf u_j
 &\longmapsto\mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{-1}
   \longmapsto
   \mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m}.
 \end{aligned}                                               \tag{3.1b}
$$

射线类塔到两个一变量塔的 norm、tensor twist 与最终
specialization 都由同一群环基变换给出，故 (3.1b) 同时与局部化
及 dual exponential 交换。这明确证明所用的高权中央值就是
(2.7) 的反圆分评价，没有把 cyclotomic 单权角色误认为
$K_p$-analytic 的反圆分混合角色。

Kato 在 §15.11 末尾特别指出，他没有假设高权 modular motive
的 Betti 与 étale 同构互相兼容。本篇也不作这一假设：
使用的是已证明的 (15.16.1)，再使用定义性两张 period 图。
若任意改变 $S(\varphi_j^r)\to S(f_j^{(r)})$ 的缩放，两个图及
zeta element 的对应同时改变，该缩放在拉回后消去。
因此本步骤无需任何高权 modular motive 的整格比较。

这条混合型 specialization 也在已发表的 [BKOY25]
Proposition 5.10 中明确写出：

$$
 T_j^{-1}(1)\longmapsto T_j^{-(1+2m)}(1+m),
 \qquad
 \varphi_j^{1+2m}\text{ 在 }s=1+m\text{ 的值}.               \tag{3.2}
$$

但其作者版中只说存在非零 $\omega_{\psi,\gamma}$，并采用一个
不宜直接与本课题 $d_m$ 比赋值的 $L^{\rm alg}$ 简写。
本篇不用“存在非零”推出单位关系，也不采用该简写的字面周期幂。
此外其 §5.4.1 为 epsilon 证明选了特殊全球化；
这里对 $E_{17}$ 的推广依据是 [K04] 本身对任意导子的定理链，
而非忽略 [BKOY25] 的全球化条件。

### 3.2 只在实际 CM tensor 格上比较

选兼容的 Betti 基 $b_0,b_{17}$，使实际代数同构 (1.1) 满足
$F_a^*b_{17}=b_0$。它们都是原始格向量。
比较定理对代数曲线和代数同构的自然性，给出兼容的 Tate 基。
Weil pairing 又使所用 cyclotomic Tate 基相同。

于是用于 (3.2) 的 twist 向量分别是

$$
 b_j^{\otimes 2m}\otimes\zeta^{\otimes m},
$$

并在 $F_a$ 下完全对应。所有 tensor 都在秩一 CM 整格上作，
没有使用 $r!$ 分母的 symmetric-power projector。

在 de Rham 一侧，(1.2) 的 $r$ 次 tensor 给出

$$
 F_a^*(\omega_{17}^{\otimes r})=a^{-r}\omega_0^{\otimes r}.
 \tag{3.3}
$$

同一个 Tate twist $1+m$ 不改变两边的比。因此这两个规范的
de Rham 向量之比是一个明确的 $p$-单位，且不是某个任意
选择的 $\mathbb C_p^\times$ 常数。

Kato 的 canonical CM-pair 用晶格 $f_j\mathcal O_K$，而这里
用 $\Omega_j\mathcal O_K$。相应 Betti 向量之间的换元是
$f_j$ 的整数幂；在本篇 $p$ 处均为单位。
若通过公共四次扭转域作下降，投影仅除以 $4$；若经完整导子域
下降，其额外有限度数为 $2$ 的幂。它们也都是单位。
直接使用 CM tensor 定义不需要再引入有限 Artin Gauss 和；
即使改用该种规范，导子只支撑在 $2,17$ 的 Gauss 和在 $p$ 处
仍是单位。

## 4. 相对 period 引理及每个非单位因子的抵消

**相对 period 引理。** 设 $m>0$ 且 $p+1\mid m$。
如果 $d_m^{(0)}\ne0$，则

$$
 v_p A_p(x_m)=v_p d_m^{(17)}-v_p d_m^{(0)}.                  \tag{4.1}
$$

约定零的赋值为 $+\infty$。

**证明。** 对 (2.7) 施同一个 $\chi_m$ specialization，
再施同一个 dual exponential。由 §1 与 §3.2 的相容性，左边的
标量比恰为 $A_p(x_m)$。§3.1 的 Kato 定理链把两个向量的比写成
同一临界规范下的两个复 $L$ 值之比；§3.2 保证所用局部
de Rham 格的比较只乘单位。

为完整核查，令 $\Omega_j$ 为 Néron 微分对应的方格周期。
本课题已证明的中央 theta--Hecke 公式是

$$
 d_m^{(j)}
 = f_j^{m+1}\bar f_j^{-m}
       \frac{\pi^m}{m!\,\Omega_j^{2m+1}}
                L_{f_j}(\varphi_j^{2m+1},m+1).              \tag{4.2}
$$

在这里同时共轭 Hecke 特征与 CM 嵌入只共轭代数值；
$p$ 惰性时这保持赋值。

Kato 公式使用的标量因而与 (4.2) 相差

$$
 (2i)^m m!\,\frac{\bar f_j^m}{f_j^{m+1}}
 $$

以及在 $p$ 的去 Euler 因子。前一个式子中，$m!$ 对两条曲线
**完全相同**；即使 $m\ge p$，也不能将它先误称为单位。
两导子之比 $f_{17}/f_0=17$，所有导子幂都是当前位的单位。
复周期比 $\Omega_0/\Omega_{17}$ 是 $17$ 的四次根，
并由同一个代数同构 (1.1) 在 de Rham 侧产生 (3.3)。

还须核 $p$ 因子。两条曲线在惰性好素数处均有

$$
 \varphi_j((p))=-p.
$$

因为 $2m+1$ 为奇数，在 $s=m+1$ 时去掉的因子均为

$$
 1-\frac{(-p)^{2m+1}}{p^{2m+2}}=1+\frac1p.                 \tag{4.3}
$$

它的赋值为 $-1$，也**不是单位**，但两边完全相同，故精确抵消。
可能改用的 Gamma、Tate 或 dual-exponential 规范只依赖同一个
局部表示及同一个 $m$，同样在相对式中抵消。

最后，$p+1\mid m$ 蕴含 $4\mid m$，所以
$2m+1\equiv1\pmod8$。两条 $\varphi_j^{2m+1}$ 的有限特征
分别与原 $\varphi_j$ 相同，primitive conductor 仍为 $f_j$。
全程使用各自 primitive conductor。**没有**为了统一记号而
给 $E_0$ 再去掉 $17$ 的 Euler 因子；后者可能不是 $p$-单位。

剩余比较因子均为已说明的 $p$-单位，因此得到 (4.1)。
$d_m^{(0)}\ne0$ 还确保参考 dual exponential 非零，故取比合法。
$\square$

注意 (4.1) 并不需要给惰性 Lubin--Tate period 或 signed logarithm
在该高权的绝对赋值。它们属于同一个局部 specialization map，
由参考向量消去；若两条曲线的局部 Tate 格仅有理同构，
这一步就不能证明整赋值结论。

## 5. 第一个中央权及 Selmer 控制

[参考值笔记](2026-11-12-rank-zero-reference-central-inert-value.md)
完整证明了对每个 (0.1) 的 $p$，

$$
 v_p d_{p+1}^{(0)}=-2.
 \tag{5.1}
$$

其证明使用真实点 $S=(i,1-i)$、sigma duplication 和中央
代数微分递推，不使用未核的 theta 向量归一。
令 $m=p+1$。由 (1.5)、(4.1)、(5.1)，即得

$$
 v_p(x_p)=1,\qquad
 v_p A_p(x_p)=v_p d_{p+1}^{(17)}+2.                          \tag{5.2}
$$

另一方面，$A_p$ 是 $E_{17}$ 的 Rubin 函数在一个实际原始
局部 signed 基下的表示。改变该基只乘 $\Lambda^\times$。
[BKO21] Theorem 6.1 的反圆分 signed 主猜想及 Theorem 6.2
对平凡特征的控制给

$$
 \operatorname{corank}_{\mathcal O}
       \operatorname{Sel}_{p^\infty}(E_{17}/K)
 \le \operatorname{ord}_{T=0}A_p(T).                         \tag{5.3}
$$

此处根数为 $+$，平凡特征属于 $\Xi^+$，故不出现另一个符号中的
“$+1$”修正。[BKO24] Definition 3.13 是同一局部椭圆单位
构造的上同调规范；逆参数或局部基改变不改变 (5.3) 的中心阶。

为明确维数，$E_{17}$ 的 $-1$ 二次扭转与 $E_{17}$ 有相同的
$\mathbb Q$ 方程。$K/\mathbb Q$ 的限制与 corestriction 以及
两个特征投影在奇数 $p$ 上均为整同构。因此

$$
 \operatorname{corank}_{\mathbb Z_p}
       \operatorname{Sel}_{p^\infty}(E_{17}/K)=2s_p,
 \qquad
 \operatorname{corank}_{\mathcal O}
       \operatorname{Sel}_{p^\infty}(E_{17}/K)=s_p.            \tag{5.4}
$$

R4 的精确秩证明给 $s_p\ge2$。R7/R24 已核的 $p$-parity 定理
与根数 $+1$ 给 $s_p$ 为偶数；这些输入不假设 $\Sha[p^\infty]$
有限。因此 (0.2) 成立。

若 $A_p=T^rB$，其中 $B\in\mathcal O[[T]]$，那么

$$
 v_p A_p(x_p)\ge r\,v_p(x_p)=r.
$$

与 (5.2)--(5.4) 合并，得到

$$
 2\le s_p\le r\le v_p d_{p+1}^{(17)}+2.                    \tag{5.5}
$$

特别是本比较还独立推出 $d_{p+1}^{(17)}$ 对所有 (0.1) 的 $p$
都是整的。若其赋值至多 $1$，则 $s_p\le3$；偶性迫使 $s_p=2$。
Kummer 正合列与余有限生成性随后给
$\Sha(E_{17}/\mathbb Q)[p^\infty]$ 有限，证明 (0.4)。

这只控制基层 $p^\infty$-Selmer 余秩，**不**声称 $\Sha[p^\infty]=0$，
也不预先假设 $p$-adic 高度非退化。

## 6. 当前真实的跨素数缺口

现在需要证明，例如

$$
 d_{p+1}^{(17)}\in\mathcal O_{K_p}^{\times}
 \quad\text{对无穷多个 }p\equiv3\pmod4.                    \tag{6.1}
$$

已有 $p=7,11$ 的精确有限环证书检验了这一局部单位条件；它们是
接口的有限检验，不证明 (6.1)。
已证明的 $v_p d_{p+2}^{(17)}=-2$ 位于另一个 tame 特征，不能代入
(5.5)。固定最低值 $e_1=4/17^3$、固定 sigma 截面以及中央平方
公式可继续用于研究 (6.1)，但其中任何一个单独都没有给出无穷性。

## 一手来源

- **[K04]** K. Kato, *p-adic Hodge theory and values of zeta functions of
  modular forms*, Astérisque **295** (2004), 117--290：Theorem 12.5(1)，
  §15.8，Proposition 15.9，Lemma 15.11，(15.16.1)。
  [Numdam 原文](https://www.numdam.org/item/AST_2004__295__117_0.pdf)。
- **[BKO21]** A. Burungale, S. Kobayashi, K. Ota, *Rubin's conjecture on
  local units in the anticyclotomic tower at inert primes*, Annals of
  Mathematics **194** (2021), 943--966：Theorems 2.1, 6.1, 6.2。
  [期刊](https://annals.math.princeton.edu/2021/194-3/p08)，
  [作者全文](https://par.nsf.gov/servlets/purl/10336626)。
- **[BKO24]** A. Burungale, S. Kobayashi, K. Ota, *p-adic L-functions and
  rational points on CM elliptic curves at inert primes*, Journal of the
  Institute of Mathematics of Jussieu **23** (2024), 1417--1460：
  §2.2.1，§3.1.1，Proposition 3.1，Definition 3.13，
  Corollary 4.11(i) 的证明。
  [期刊全文](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/padic-lfunctions-and-rational-points-on-cm-elliptic-curves-at-inert-primes/7F847A218FE1F6DBB390CC0279089C34)。
- **[BKOY25]** A. Burungale, S. Kobayashi, K. Ota, S. Yasuda,
  *Kato's epsilon conjecture for anticyclotomic CM deformations at inert
  primes*, Journal of Number Theory **270** (2025), 17--67：
  §5.4.2，Proposition 5.10。本篇只以它核对 mixed-character
  specialization 的范围，赋值比较直接回到 [K04]。
  [DOI](https://doi.org/10.1016/j.jnt.2024.06.014)，
  [作者版](https://drive.google.com/file/d/151q-D_EkyGxJdp_tjTnr0JleQ4rzotTv/view)。
