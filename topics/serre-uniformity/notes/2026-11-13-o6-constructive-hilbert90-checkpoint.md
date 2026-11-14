# O6：从一个实际 Norm-one 单位提取所需原像的构造接口

**状态：以下代数构造与支撑结论已证明；其输入单位 $\varepsilon$ 尚未取得。未计算 $X$ 或 $\mathcal L$。**

目标与 R219 完全相同：$L/F$ 循环 $p=43$ 次，生成元为 $\gamma$；
$\tau\gamma\tau=\gamma^{-1}$；$U\in E_F$ 是 R219 已实际写成
$44$ 个有理幂基系数的实单位。本文记录一条不要求完整 $E_L$ 单位基的
构造接口，并明确保留尚缺的输入。

## 1. 可直接验证的输入条件

设已经实际构造一个 $\varepsilon\in E_L$，满足
$$
 N\varepsilon=1,\qquad
 \tau\varepsilon=\gamma^{-1}(\varepsilon^{-1}),\qquad
 \varepsilon\equiv1\pmod{\mathfrak Q},                     \tag{H.1}
$$
其中 $\mathfrak Q=\prod_{Q\mid q}Q$ 是平方自由 $q$ 模。
定义
$$
 D_0=1,\qquad D_j=\prod_{r=0}^{j-1}\gamma^r\varepsilon,
 \qquad Z=\sum_{j=0}^{42}D_j^{-1},\qquad A=NZ.             \tag{H.2}
$$
还须实际找到 $c\in\{1,\ldots,42\}$ 与 $B\in F^\times$，并精确核验
$$
 A=U^c B^{43}.                                            \tag{H.3}
$$
这是一个 **底域** $43$ 次根问题，但它并未在本次被解出；(H.3)
不能由一个有限素点的幂剩余检查替代。

### 1.1 从任意实际 relative unit 作同一角色与实投影

令 $\Pi=\sum_{j=0}^{43}a_j\sigma^j$ 使用 R219 的同一中心整数权。
若已经给出一个实际普通单位 $\varepsilon_0$ 且 $N\varepsilon_0=1$，定义
$$
 \varepsilon_1=\varepsilon_0^{\Pi},\qquad
 \varepsilon=\frac{\varepsilon_1}{\gamma\tau\varepsilon_1}. \tag{H.1a}
$$
则 (H.1) 的三个条件全部成立，且 (H.3) 对某个
$c\in\{0,\ldots,42\}$ 与某个 $B\in F^\times$ 成立。
**需要实际检出的额外条件只剩 $c\ne0$。**

证明如下。Norm 条件直接由群作用给出。
$T=\gamma\tau$ 满足 $T^2=1$，所以 $T\varepsilon=\varepsilon^{-1}$，
这正是 (H.1) 的中间条件。
在每个全分歧 $q$ 素点，$N\varepsilon_0=1$ 使
$\overline\varepsilon_0^{43}=1$，所以全部剩余值构成一个模 $43$ 的向量。
$\Pi\bmod43$ 只保留忠实 $\chi,\chi^{-1}$ 对。
R210 的自由性给该分量上的 Norm 核为
$(\gamma-1)E_{L,\chi}$；$\Gamma$ 在剩余域上平凡，故该核的剩余值为零。
因此 $\overline\varepsilon_1=1$，继而 $\overline\varepsilon=1$。

为了证明 (H.3)，对任意 Norm-one 元素 $e=\gamma Y/Y$ 定义
$$
 \partial(e)=[NY]\in F^\times/F^{\times43}.
$$
Hilbert–90 保证可取 $Y$；两个选择只相差一个底域元素，因而该定义
与选择无关。它是乘法同态，与 $\Delta$ 交换，且
$$
 \partial(\gamma e)=\partial(e),\qquad
 \partial(\tau e)=-\tau\partial(e).
$$
最后一式可直接以 $Y'=(\gamma^{-1}\tau Y)^{-1}$ 为 $\tau e$ 的
Hilbert–90 解核对。
R210 的 $\chi$ 分量单位自由性又表明，普通 Norm-one 单位的
$\partial$ 在 $\chi$ 对上的像来自底域单位：在完成后可取单位 $Y$，
再模 $43$ 返回普通单位的 Kummer 类。
于是 $\partial(\varepsilon_1)$ 只在底域单位的 $\chi$ 对上；
(H.1a) 给
$$
 \partial(\varepsilon)=(1+\tau)\partial(\varepsilon_1).
$$
该 $\chi$ 对在 $\mathbb F_{43}$ 上二维，$\tau$ 交换两个不同的
$\Delta$ 特征，故其 $\tau$ 固定空间一维。
R219 的 $[U]$ 为该固定空间的非零元素。因此
$\partial(\varepsilon)=c[U]$，正是 (H.3) 的存在性。
这一步保证底域开根可行，但仍未给出实际 $\varepsilon_0$ 或 $B$。
若只从真 $K$ 子域的单位组装 $\varepsilon_0$，其忠实 $\chi$
分量只能来自 $F$ 单位；在该分量上 Norm 是乘 $43$，所以 Norm-one
条件迫其为零。因此这种组装无法取得所需的非零 $c$，与上一条
faithful-norm 边界一致。

## 2. 显式输出与普通单位性

由 $N\varepsilon=1$ 有 $D_{43}=1$，且
$\gamma D_j=D_{j+1}/\varepsilon$。故
$$
 \gamma Z=\varepsilon Z.                                  \tag{H.4}
$$
(H.1) 的最后一个条件给 $Z\equiv43\pmod{\mathfrak Q}$；
因 $q\ne43$，所以 $Z\ne0$，且 $Z$ 是每个 $q$ 处的单位。
这里不用对多个 $t$ 尝试通常的 Hilbert–90 求和：$t=1$ 已确定非零。

由 (H.1) 的中间条件及 $D_{43}=1$，逐项可得
$\tau D_j=D_{43-j}$（下标模 $43$），所以 $\tau Z=Z$、$\tau A=A$。
由 $U$ 实且 $B^{43}=A/U^c$，有 $(\tau B/B)^{43}=1$。
$F$ 不含非平凡 $43$ 次单位根，因为 $[F:\mathbb Q]=88$ 不能被
$[\mathbb Q(\mu_{43}):\mathbb Q]=42$ 整除。因此 $\tau B=B$。

取整数 $d,k$ 满足 $cd=1+43k$，定义
$$
 \boxed{X=\frac{Z^d}{B^d U^k}.}                            \tag{H.5}
$$
则直接计算得
$$
 NX=\frac{A^d}{B^{43d}U^{43k}}=U,\qquad\tau X=X.
$$

还必须证明 $X$ 为普通单位，而非只是一条有外支撑的普通 Norm 解。
由 (H.4) 和 $\varepsilon\in E_L$，$\operatorname{div}Z$ 被 $\Gamma$
固定。底域元素 $B,U$ 的除子也被 $\Gamma$ 固定，故
$\operatorname{div}X$ 被 $\Gamma$ 固定。在任何底域素点的上方，
一个 Galois 轨道中所有 $v_Q(X)$ 相同，而
$$
 0=v_\lambda(NX)=\sum_{Q\mid\lambda}f(Q/\lambda)v_Q(X).
$$
所有系数均为正，故该共同赋值为零。逐素点即得
$$
 \boxed{X\in E_L.}                                        \tag{H.6}
$$
因此 (H.1)–(H.3) 一旦以实际元素实现，就不再需要额外的外支撑
Artin 修正。这一结论依赖 $\varepsilon$ 是普通单位；若只给出
Norm-one 的普通非单位元素，则上述除子不变性论证不成立。

## 3. 同一规范下只需求底域 $B$ 的剩余符号

由 $Z\equiv43\pmod{\mathfrak Q}$，所有 $\Delta$ 共轭均有相同约化。
有理数 $43$ 的剩余值落在 $\mathbb F_q^\times$，而 $43\mid q+1$，故
$$
 \ell(\sigma^jZ)=0.
$$
R219 的目标在全部 $q$ 素点是局部 $43$ 次幂，所以
$\ell(\sigma^jU)=0$。于是 (H.5) 给
$$
 \ell(\sigma^jX)=-d\,\ell(\sigma^jB).
$$
将其代入 R219 的完整投影与根规范，得到
$$
 \boxed{\mathcal L=-4d\sum_{j=1}^{21}
   \operatorname{Im}(\omega^j)\ell(\sigma^jB)-3\pmod{43}.}   \tag{H.7}
$$
这没有重定义 $\mathcal L$，也没有省略 R201 的高低权根修正。
它说明求得 (H.1) 的实际单位后，$Z$ 的全扩张剩余值无需逐项计算；
最终读数只来自 (H.3) 的底域根 $B$。

若 $A$ 在 follow-up 笔记的 $859$ 素点为单位，则 (H.3) 的指数
$c\bmod43$ 也可很快辨认：在 $z\mapsto802+606i$ 下，已实际算出
$$
 \overline U=49+45i,\qquad
 \overline U^{17160}=580+68i\ne1\quad\text{于 }\mathbb F_{859^2}.
$$
该元素的阶为 $43$，所以比较 $\overline A^{17160}$ 的 $43$ 个可能
幂即可确定候选 $c$。这只确定候选指数，仍须在 $F$ 内精确核验
$B^{43}=A/U^c$；若 $A$ 在该点不是单位，这个简化读取不能直接套用。

### 3.1 已实现的底域 $43$ 次根提取，不依赖 PARI

`extract_o6_base_43rd_root.py` 直接在
$F=\mathbb Q(i)[z]/(f_z)$ 中实现底域开根。
选 $\ell=439$（或程序发现的另一个合适素数），程序首先在有限商环
检查 $z^{\ell^2}=z$。因 $f_z$ 首一且整除无重根的
$T^{\ell^2}-T$，这证明约化代数是若干份 $\mathbb F_{\ell^2}$ 的直积。
又 $\gcd(43,\ell^2-1)=1$，因此在其单位群上 $43$ 次幂是双射。
对输入 $V$ 的唯一模 $\ell$ 根可直接取为
$V^{43^{-1}\bmod(\ell^2-1)}$。

随后倍增精度作 Newton 提升；导数 $43B^{42}$ 为单位。
每一步将各高斯坐标作有理重建，但**只有**在精确商环中核验
$B^{43}=V$ 后才接受根。有理重建暂时稳定不被视为认证。
若输入确为全局 $43$ 次幂且所选素数处为单位，唯一全局根与该唯一
局部根相容；足够精度下，有限个有理系数都可重建，因此此方法最终
取得根。代码带有限精度上限；未命中只能报未决，不能报无根。
$F$ 不含非平凡 $\mu_{43}$，所以通过精确等式的根唯一。

本次实际执行的演示输入是 $V=(\sigma z)^{43}$，不是当前 Norm 方程
的未知数据。程序从 $439$ 进精度 $1,2,4,\ldots,128$ 逐步提升，
在 $439^{128}$（$1124$ bit）处重建出 R219 的同一个 $\sigma z$，
并通过完整全局 $43$ 次幂等式。运算约四秒；没有调用 GP、Sage、
数值近似、类群或单位群软件。
证书为 `notes/base_43rd_root_extraction_certificate.json`，其中
`demonstration_only:true`、`actual_norm_preimage_computed:false`、
`actual_L_computed:false` 均明确保留。

~~~sh
python scripts/extract_o6_base_43rd_root.py \
  notes/small_robert_norm_target_certificate.json \
  --check notes/base_43rd_root_extraction_certificate.json
~~~

取得真实的 $A/U^c$ 后，`--target` 可读其高斯有理幂基系数，
`--root-output` 写出经过精确认证的底域根。
这使 (H.3) 的开根步骤成为已有可执行组件；当前仍缺的是实际混合
Norm-one 单位输入，而非把演示根误认为所需原像。

## 4. 已有 $q$-Eisenstein 模型的常数项接口

R207 的 $P_\theta$ 在 $q$ Eisenstein。设一个实际解写成
$$
 X=\sum_{r=0}^{42}x_r\theta^r,\qquad x_r\in F.
$$
在每个 $q$ 素点，取 $v_Q(\theta)=1$，则
$$
 v_Q(x_r\theta^r)=43v_\lambda(x_r)+r.
$$
这些数按 $43$ 取模两两不同，最小项不能相消。因此 $X$ 为局部
单位当且仅当所有 $x_r$ 在 $\lambda$ 整，且 $x_0$ 为单位；此时
$$
 \overline X=\overline{x_0}.
$$
所以 R219 的 $21$ 个符号也可直接从实际原像的常数系数读出。
若 $\tau X=X$，则各 $x_r\in H$，因为 $\tau\theta=\theta$ 且基
$1,\theta,\ldots,\theta^{42}$ 的表示唯一。
对有外支撑的非单位原像，这只是原始局部读数，仍不能替代所需
Artin 修正。

## 5. 尚缺的内容与本次能力核对

本次没有取得满足 (H.1) 且产生非零 $c$ 的实际混合单位
$\varepsilon$。R210 的 $E_{L,\chi}\simeq\mathcal O[\Gamma]$
保证这种角色方向的单位存在，但不给它的值。
不能把 $\mathrm{Cl}(L)_\chi\simeq\mathcal O/43$ 直接解释为已得到
一个可计算的 elliptic-unit 生成元，亦不能未经证明把原来
$43\nmid[F:K]$ 时使用的 finite Gras 公式直接套到 $43\mid[L:K]$。

查阅 Chapdelaine–Kučera，*Annihilators of the Ideal Class Group of a Cyclic
Extension of an Imaginary Quadratic Field*，Canad. J. Math. 71 (2019),
1395–1419；预印本 <https://arxiv.org/pdf/1705.10905> 的 §1、Theorem 10。
该文的设置要求虚二次底域上的循环 $p$ 次幂扩张，且至少两个
分歧素点。这里 $L_q/K$ 只有 $q$ 一个分歧素点，$L/K$ 次数含
$44$，而 $L/F$ 的底域不是虚二次域；该定理不能直接提供当前输入。

本地能力核对已进一步推进：最初 PATH 没有 GP/Sage/Magma，系统
库目录未发现 libpari，apt 元数据因配置文件权限不能读取。随后已在
普通用户可写目录成功安装 `cypari2==2.2.4` 的预编译 wheel，实际
调用其 bundled PARI 得到 `version()=[2,17,2]` 及
`bnfinit(x^2+1).no=1`。这确认目前已有可执行的 PARI 2.17.2；
此前“没有 PARI”已不再是阻塞，也没有改动系统权限或网络配置。
依赖仅置于当前会话的 `agent-o6/pari-deps`，不作为研究数据提交。

已读取同版本 `rnfisnorminit`、`rnfisnorm`、`bnfinit` 与 `bnfunits`
的实际 Python 接口文档。相对 Norm 方法需要上域类群／单位数据；
软件可用本身不等于已取得该数据或 Norm 解。当前尚未对本课题的
$L/F$ 实际运行成功相对 Norm 求解，$X$ 与 $\mathcal L$ 仍未求出。
后续将利用这项现有能力构造实际混合单位或可验证的 Norm 原像。

PARI 官方 `rnfisnorminit` 文档也已核对：
<https://pari.math.u-bordeaux.fr/dochtml/ref/Relative_extensions_of_number_fields_and__backslashZ_K_minusmodules.html>。
$L^+/H$ 的 $43$ 次实扩张不是 Galois，不能把它标为 `flag=1`。
循环扩张是 $L/F$；无论采用何种求解器，具体正解都须以精确 Norm
等式及单位/外支撑状态核验。

R219 已由父会话推送为 `942be9a25e0b1e99433ff094315d7309f54407c5`。
本文只记录当前构造接口及精确缺口；R202 仍保留给实际求出的
$\mathcal L$，主问题没有完成。
