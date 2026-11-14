# R210：普通类群、自由单位模及实际二阶剩余量的射线判据

**状态：已证明的恢复结果；实际 $\mathcal L$ 尚未计算。**
本稿从 R163、R168、R191、R200、R201 和已推送的短单位多项式
重新推导，不以中断前的内存记录作证据。固定 R171 的 $p=43$、
同一个 **776 bit** 素数 $q$、CM/Weil 标记和算术 Artin 方向。
这里的两个输入分别是 $\gamma_q=0$ 与 $\lambda_q=16\ne0$；
不能将其中一个当成另一个的推论。

本文证明
$$
 \operatorname{Cl}(L)_\chi\simeq\mathcal O/43,
 \qquad \Gamma\text{ 在此类群上平凡作用},
 \qquad E_{L,\chi}\simeq\mathcal O[\Gamma].                 \tag{210.1}
$$
若 $\mathfrak Q$ 是 $L$ 中全部 $q$ 素点的乘积，则
$$
 \operatorname{length}_{\mathcal O}\operatorname{Cl}_{\mathfrak Q}(L)_\chi
 \in\{1,2\}.                                             \tag{210.2}
$$
并在 R201 的**同一完整根规范**下证明
$$
 \operatorname{length}_{\mathcal O}\operatorname{Cl}_{\mathfrak Q}(L)_\chi=2
 \iff \mathcal L=40
 \iff v=0
 \iff \Omega_2^\epsilon=13\epsilon.                       \tag{210.3}
$$
射线长度本身尚未求值；(210.1) 不决定 (210.3) 的真假。

## 1. 域、角色与已有的准确输入

令
$$
 K=\mathbb Q(i),\quad A:y^2=x^3-x,\quad
 F=K(A[43])^{\mathbb F_{43}^{\times}},\quad L=FL_q,
$$
$$
 \Delta=\operatorname{Gal}(F/K)=C_{44},\qquad
 \Gamma=\operatorname{Gal}(L/F)=\langle\gamma\rangle=C_{43}.
$$
$L_q/K$ 是 R191 的导子恰为 $(q)$ 的循环扩张，在 $2,43$ 完全分裂。
$\Delta$ 与 $\Gamma$ 交换，复共轭同时反演两者。
取 $\mathcal O=\mathbb Z_{43}[i]$，$k=\mathcal O/43$，
并取 $\chi:\Delta\to\mathcal O^\times$ 为 R201 的忠实 Teichmüller
角色；其约化在所选生成元上是 $8+25i$。
下标 $\chi$ 表示先张量 $\mathcal O$ 再取整幂等投影。
两个共轭角色 $\chi,\chi^{-1}$ 的论证相同。

记
$$
 E_{M,\chi}=(\mathcal O_M^\times\otimes_{\mathbb Z}\mathcal O)_\chi,
 \qquad
 \operatorname{Cl}(M)_\chi=(\operatorname{Cl}(M)\otimes_{\mathbb Z}\mathcal O)_\chi.
$$
单位群在这些张量中用加法书写；表示普通代数单位时仍用乘法。
这些有限生成单位模等于其相应 $43$ 进完成。本文从不把
$\chi$ 分量的消失扩大为整个类群消失。

使用的已证输入为：

1. R163 给 $\operatorname{Cl}(F)_\chi=0$，且 $E_{F,\chi}$ 为秩一
   自由 $\mathcal O$ 模；R198/R201 的原始 scalar Robert 单位
   $u_0$ 的 $\chi$ 投影生成它。
2. 在 $F$ 中，$q$ 有 $44$ 个素点，各完成为 $K_q=\mathbb Q_{q^2}$；
   它们被 $\Delta$ 正则排列，在 $L/F$ 中均全分歧，且
   $v_{43}(q^2-1)=1$。
3. $\gamma_q=0$ 恰说明原始单位线在全部这些素点的 $43$ 次幂
   剩余符号均为零。因 $u_0$ 是整单位模的基，整个 $E_{F,\chi}$
   都在这个剩余映射的核中。
4. R201 Theorem 201.1 在 $S=\{2,43,q,\infty\}$ 给
   $\operatorname{Cl}_S(L)_\chi=0$。这里确实使用了
   $\lambda_q\ne0$：严格 $43$ Selmer 直线在 $q$ 的有限部分
   是非零倍数，不能下降成在 $S$ 完全分裂的非零类群扩张。
5. $F$ 的 $43$ 惯性是全部 $\Delta$；$2$ 惯性在 $\chi$ 下非平凡。
   因 $L_q$ 在两处分裂，$L$ 中 $2,43$ 上方的除子置换模
   都没有 $\chi$ 分量。

第 3 条不能只从“存在一个 Robert 单位”推出；其依据是 R163 的
原始生成性和 R171 对同一单位及同一根的零值核证。

## 2. 普通类群准确为 $\mathcal O/43$

### 2.1 上界及 $\Gamma$ 的作用

$\operatorname{Cl}_S(L)_\chi=0$ 说明普通 $\chi$ 类群由 $S$ 上方
素理想生成。第 5 条消去 $2,43$ 的除子；故只剩 $q$ 上方素点。
其除子模的 $\chi$ 分量恰为一份 $\mathcal O$，$\Gamma$ 固定每个
这样的素点。因此存在 $\Gamma$ 等变满射
$$
 \mathcal O\longrightarrow\operatorname{Cl}(L)_\chi,
$$
且左边的 $\Gamma$ 作用平凡。

设 $\lambda\mid q$ 在 $F$，$Q\mid\lambda$ 在 $L$。
由于全分歧，$\lambda\mathcal O_L=Q^{43}$。
对所有共轭作 $\chi$ 投影，并用 $\operatorname{Cl}(F)_\chi=0$，得
$$
 43\operatorname{Cl}(L)_\chi=0.
$$
所以普通类群只有 $0$ 或 $\mathcal O/43$ 两种可能。
这也已经证明其 $\Gamma$ 作用平凡。

### 2.2 下界：底域射线类域经全分歧基变换成为未分歧扩张

令 $\mathfrak q_F=\prod_{\lambda\mid q}\lambda$。
射线正合列在 $\chi$ 分量为
$$
 E_{F,\chi}\longrightarrow
 \left(\prod_{\lambda\mid q}k_\lambda^\times\otimes\mathcal O\right)_\chi
 \longrightarrow\operatorname{Cl}_{\mathfrak q_F}(F)_\chi
 \longrightarrow\operatorname{Cl}(F)_\chi\longrightarrow0.
                                                               \tag{210.4}
$$
中间剩余模是 $\mathcal O/43$：$\Delta$ 正则排列 $44$ 个剩余域，
各剩余乘法群的 $43$ 部准确阶 $43$。
由 $\gamma_q=0$，单位映射为零；由底域类群消失，得
$$
 \operatorname{Cl}_{\mathfrak q_F}(F)_\chi\simeq\mathcal O/43.
                                                               \tag{210.5}
$$
把共轭的两个特征一起取成 $\mathbb F_{43}$ 上的二维不可约商，
类域论给 $M/F$，其 Galois 模就是该二维 $\Delta$ 型。
它只在 $q$ 上方允许 tame 分歧，且 Galois 群的指数为 $43$。

$M\cap L=F$。否则 $L/F$ 是 $M/F$ 的非零商，但 $\Delta$ 在
$L/F$ 的 $C_{43}$ 上平凡，在上述二维不可约型上没有平凡商。

在每个 $q$ 位置，$ML/F$ 是指数 $43$ 的阿贝尔 tame 扩张。
tame 惯性是循环的，故其阶至多 $43$；而 $L/F$ 的惯性已经有
阶 $43$。因此 $ML/L$ 在该处不分歧。其他有限位置原来就不分歧；
所有域含 $K$，无实位置问题。于是 $ML/L$ 是非零的处处未分歧
阿贝尔扩张，且仍带上述 $\Delta$ 型。
Hilbert 类域论遂给 $\operatorname{Cl}(L)_\chi\ne0$。
结合上界即得 (210.1) 的类群部分。

注意这里使用“指数 $43$ 的 **阿贝尔** 合成扩张”才控制其 tame
惯性阶；不能把这一句话推广到任意连续的两次全分歧扩张。

## 3. Norm 在普通单位分量上满射

我们证明
$$
 N_{L/F}:E_{L,\chi}\longrightarrow E_{F,\chi}
 \quad\text{满射}.                                           \tag{210.6}
$$
先对任意底域单位的 $\chi$ 分量检查局部 Norm：$2,43$ 处分裂；
$q$ 处为 tame 全分歧次数 $43$，单位 Norm 条件恰为剩余值是
$43$ 次幂，这由第 1 节第 3 条保证；其余处是不分歧扩张上的单位，
局部单位 Norm 满射。循环 Hasse Norm 定理给全局 Norm。

这里的“$\chi$ 分量”可以严格在完成模中使用。普通 Hasse Norm
定理是 $F^\times/NL^\times$ 到局部 Norm 余核的单射；这个余核被
$43$ 杀掉。先张量平坦的 $\mathcal O$，再取 $\Delta$ 的整直和
因子，仍然是单射。因此未假设一个任意非 $\chi$ 普通单位也是
Norm；得到的是所需 $\chi$ 通道中的真正 Norm 原像。

取原像 $X\in(L^\times\otimes\mathcal O)_\chi$。
R201 §3 的除子修正用 $\operatorname{Cl}_S(L)_\chi=0$，将 $X$
改为同一 Norm 的 $S$ 单位，方法为
$$
 \operatorname{div}_{S^c}(X)=(\gamma-1)D,
 \qquad \operatorname{div}_{S^c}(Y)=D,
 \qquad X\longmapsto X+(1-\gamma)Y.
$$
在 $q$ 上，因为剩余次数 $f=1$，Norm 对除子系数是恒等映射。
底域目标是普通单位，故修正后的 $X$ 在每个 $q$ 位置的 $\chi$
赋值都是零。$2,43$ 的除子没有 $\chi$ 分量。
所以这个 $S$ 单位原像实际上属于 **普通单位分量** $E_{L,\chi}$，
证明 (210.6)。

这不声称每个没有投影的普通 Norm 原像都是单位。
使用未投影或非单位的原像时，R200 附记中的外支撑 Artin 修正仍须保留。

## 4. 普通单位模自由：一个不需要类群软件的整证明

令 $R=\mathcal O[\Gamma]$，$N=\sum_{j=0}^{42}\gamma^j$，
$\mathcal E=E_{L,\chi}$。Dirichlet 单位定理的对数表示给
$$
 \operatorname{rank}_{\mathcal O}\mathcal E=43.
                                                               \tag{210.7}
$$
具体地，$L/K$ 为阿贝尔扩张、$K$ 虚二次，复嵌入对的置换表示
是 $\Delta\times\Gamma$ 的正则表示；单位的实对数表示去掉一份
平凡表示。取非平凡 $\chi$ 后恰留下 $\Gamma$ 的正则表示。
不需要也没有假设 $F^{\langle\tau\rangle}$ 是全实域。

$L$ 不含 $43$ 次单位根，因为
$42\nmid[L:\mathbb Q]=2\cdot44\cdot43$。
所以 $\mathcal E$ 无 $43$ 挠元。
由平坦基变换，
$$
 \mathcal E^\Gamma=E_{F,\chi}.
$$
取其基 $u$。由 (210.6) 选 $x\in\mathcal E$ 使 $Nx=u$。
$u\notin43\mathcal E$：若 $u=43y$，则 $\mathcal E$ 无挠保证
$y\in\mathcal E^\Gamma$，违背 $u$ 是不变量模的基。

模 $43$ 后，$s=\gamma-1$ 满足
$$
 k[\Gamma]=k[s]/(s^{43}),\qquad N=s^{42}.
$$
因此 $s^{42}\bar x=\bar u\ne0$，$\bar x$ 的循环子模长度为 $43$。
结合 (210.7)，映射
$$
 k[\Gamma]\longrightarrow\mathcal E/43\mathcal E,
 \qquad a\longmapsto a\bar x
$$
为同构。原映射 $R\to\mathcal E$ 是同秩自由 $\mathcal O$ 模之间
的映射，行列式模 $43$ 非零，故本身为同构。
这证明 (210.1) 的自由性，而没有把有限域维数误当作整自由性。

任意两个满足 $Nx=u$ 的生成元相差
$(\gamma-1)\mathcal E$。这由自由模中
$\ker N=(\gamma-1)R$ 立即得到。
因此它们在全分歧 $q$ 素点的剩余值相同。

## 5. 短 Robert 元其实是普通单位

沿用已推送笔记 `2026-11-13-small-robert-norm-target.md` 的
同一个 $44$ 次整生成元 $z$，令
$$
 u_{\rm short}=\frac{z-i}{z+i}.
$$
令 $f_z(T)\in\mathbb Z[T]$ 是该笔记证书 `factors[0]` 中的首一
倒数多项式，次数 $44$，常数项 $1$。本次从该已推输入逐个整数系数
重算，得到精确恒等式
$$
 (1-T)^{44}f_z\!\left(i\frac{1+T}{1-T}\right)
       =-2^{22}f_z(iT).                                    \tag{210.8}
$$
代入 $T=u_{\rm short}$ 后左边为零，所以 $f_z(iu_{\rm short})=0$。
$f_z(iT)$ 属于 $\mathbb Z[i][T]$，首一且常数项 $1$。
因此 $u_{\rm short}$ 和其逆都整，是 **普通全局单位**。
这补足此前只证明它在 $\{2,43\}$ 外为单位的范围。

旧笔记的精确变换
$$
 \sigma_i u_{\rm short}=-u_{\rm short}^{-1},\qquad
 \sigma_i u_0=-u_0u_{\rm short}^{-30},\qquad \chi(i)=-1
$$
在奇数 $43$ 的整完成上给
$$
 e_\chi[u_0]=15e_\chi[u_{\rm short}].                       \tag{210.9}
$$
由 $15\in\mathcal O^\times$，短单位的投影仍是 $E_{F,\chi}$ 的基。
(210.8) 的 45 个 Gaussian 整数系数等式和所有数值 gauge 换算由
附带程序直接核验；没有重跑已有的 1848 个 Robert 值。

## 6. 射线长度准确测量 Norm 基的剩余零性

令 $\mathfrak Q=\prod_{Q\mid q}Q$；这是 $L$ 中的 squarefree 模，
不是 $q\mathcal O_L=\mathfrak Q^{43}$。
因为 $q\ne43$，提高这些模指数只增加 $q$ 群，不改变下述 $43$ 部。
射线正合列和第 2 节给
$$
 E_{L,\chi}\xrightarrow{\mathrm{red}}
 k\longrightarrow\operatorname{Cl}_{\mathfrak Q}(L)_\chi
 \longrightarrow k\longrightarrow0.                       \tag{210.10}
$$
$\Gamma$ 在剩余域上平凡作用。由第 4 节，$E_{L,\chi}=Rx$，
所以 $\mathrm{red}$ 由单个 $\rho_x=\mathrm{red}(x)\in k$ 决定。
换 $R$ 基只将 $\rho_x$ 乘以非零标量，其零性不变。
因此
$$
 \begin{aligned}
 \rho_x=0&\iff
 \operatorname{length}_{\mathcal O}\operatorname{Cl}_{\mathfrak Q}(L)_\chi=2,\\
 \rho_x\ne0&\iff
 \operatorname{length}_{\mathcal O}\operatorname{Cl}_{\mathfrak Q}(L)_\chi=1.
 \end{aligned}                                               \tag{210.11}
$$
长度二不等于已经识别其完整群结构；本文没有将它擅自写成
$\mathcal O/43^2$ 或 $k\oplus k$。

## 7. 普通单位 Norm 与 R201 完整根 gauge 的接合

这里先说明为什么在普通单位 Norm 模型里不再有一个隐藏的有限坐标。
在固定 $q$ 的完成上，令 $X$ 为单位 Norm 原像、$NX=U$，并取
$$
 A_X=\prod_{j=0}^{42}(\gamma^jX)^j.
$$
全分歧使每个 $\gamma^jX$ 的剩余值相同，故
$$
 \overline{A_X}=\overline X^{43\cdot42/2}
$$
是剩余域中的 $43$ 次幂。因剩余特征为 $q\ne43$，Hensel 引理
给 $A_X$ 在 $L_Q$ 中的 $43$ 次根。底域单位 $U$ 也在本地是
$43$ 次幂。R191 的正 primitive
$$
 Q_X(g)=\frac{\alpha B_{c(g)}}{g\alpha\,(g\beta)^{c(g)}},
 \quad\alpha^{43}=A_X,\quad\beta^{43}=U
$$
于是对一个在 $L_Q$ 上平凡的算术 Frobenius 提升取值为零。
此提升存在，因为 $L_Q/F_\lambda$ 全分歧。
故其有限坐标为零；奇异坐标由 $\overline X/\overline\beta$ 读取。
从 $F_\lambda=\mathbb Q_{q^2}$ 回到 $\mathbb Q_q$ 时限制次数为二，
不会把零有限坐标变成非零。
同一论证逐坐标适用于 $\mathcal O$ 完成、$\chi/\tau$ 投影及
R200 的乘 $-2i$ 作用。

因第 3 节的 Norm 基属于普通单位分量，以上模型没有外支撑项。
而任何非单位模型依然要用 R200 附记的正号 Artin 修正，不能删去。

现在取 R201 的完整 Teichmüller 单位投影，其低整数权坐标为
$U,V$，高权坐标为 $U_2=UZ_U^{43}$、$V_2=VZ_V^{43}$。
已有完整证书在同一 Weil 根下给
$$
 \ell(Z_U)=0,\qquad\ell(Z_V)=3,
 \qquad \ell(a)=\log_\zeta(a^{(q^2-1)/43}).                  \tag{210.12}
$$
取低权 Norm 原像 $X_V$，高权原像是 $X_V Z_V$，因为
$Z_V\in F$ 的 Norm 正好是 $Z_V^{43}$。
其投影后的幂剩余对数因而从 $\mathcal L$ 变为
$$
 \rho:=\mathcal L+3.                                       \tag{210.13}
$$
这里 $\rho$ 是按 R201 全部 $C_{44}/\tau$ 投影规范后的标量，
不是任意单个未投影共轭点的对数。
完整 Teichmüller 的底域投影是 $E_{F,\chi}$ 的基，因此相应高权
Norm 原像正是第 4 节的 $R$ 基；$\rho=0$ 等价于 (210.11)
中剩余映射为零。这个零性不受选取共轭特征或非零下降基的影响。

R201 的低权根修正为 $\beta_V\zeta^6$，准确给
$$
 v=-4\mathcal L-12=-4\rho,\qquad
 \Omega_2^\epsilon=\epsilon(10-\mathcal L)
                    =\epsilon(13-\rho).                    \tag{210.14}
$$
结合 (210.11)，即得 (210.3)。所有 $43$ 个剩余值的换算也由
程序逐一核查。

## 8. 对实际二阶计算的含义及仍未完成的量

若该射线 $\chi$ 类群长度是二，(210.3) 立即给
$\Omega_2^\epsilon=13\epsilon\ne0$，固定完整局部型的第二层 lift
不存在。若长度是一，只知道 $\rho\ne0$；第二层可积性的准确条件
仍为 $\rho=13$，等价于 $\mathcal L=10$，不能仅凭非零决定。

本次没有找到普通 Norm 基 $x$，没有计算其 $q$ 剩余值，也没有
计算 $\operatorname{Cl}_{\mathfrak Q}(L)_\chi$ 的实际长度。
尤其不能从 $E_{L,\chi}$ 的抽象自由性推出 $\rho=0$、
$\rho=13$ 或任意其他数值。R202 继续保留给实际 $\mathcal L$。

同一个 $q$ 早已被 Gaussian $5$ 的一阶整数迹条件排除为实际
椭圆曲线支撑；本条研究的是同一规范二阶算法，未增加已排除曲线的
范围。变 $p$、变支撑的全局一致性目标仍开放。

## 9. 实际复算与出处

程序 `scripts/verify_r210_unit_transform.py` 的输入是已推送
`notes/small_robert_norm_target_certificate.json`，其 SHA256 为
`340b387727696e12cecf75cbdf08b4a09b5416c2f42d2191ddafe041d5b14104`。
新证书为 `notes/r210_unit_transform_certificate.json`。

~~~sh
python scripts/verify_r210_unit_transform.py \
  notes/small_robert_norm_target_certificate.json \
  --check notes/r210_unit_transform_certificate.json
~~~

实际整数输出为 `PASS`；原始变换内容为 $2^{22}$，全部 45 个系数
等式通过。程序明确保留
`actual_norm_preimage_computed:false`、
`actual_ray_length_computed:false`、`actual_L_computed:false`。
上述类群及自由性是 §§2–4 的证明结论，不冒称软件计算出的类数。

除上述仓库内已证输入外，标准工具采用：

- P. Stevenhagen, *Class Field Theory*, §3 printed p.3 的射线正合列，
  §4 Theorem 4.1 的类域对应：
  <https://websites.math.leidenuniv.nl/algebra/Stevenhagen-CFT.pdf>。
- K. S. Kedlaya, *Notes on Class Field Theory*, Theorem 7.2.10
  （循环 Hasse Norm 定理；在线原文）：
  <https://kskedlaya.org/cft/sec_ideles-cohom2.html>。
- 亦可沿用 R191/R201 已核的 J. S. Milne,
  *Class Field Theory*, Chapter VIII, Theorem 3.1, printed p.234。

本条新证明中的整自由性用显式 $k[s]/s^{43}$ 论证，
不另假设局部自由、类群算法输出或未求出的基本单位。
