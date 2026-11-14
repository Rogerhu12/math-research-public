# R219：实际 Norm 目标压成一个实单位方程与 21 个剩余符号

**状态：已证明的计算归约；Norm 原像与 $\mathcal L$ 仍未求值。**
固定 R171/R191/R201 的 $p=43$、同一个 $776$ bit 素数 $q$、
CM 主类、正算术 Artin 生成元 $\sigma$、实 $43$ 挠点和 Weil 根。
本条在 R210 之后把两坐标 Robert Norm 任务改为一个较短的
**普通实单位** Norm 方程，同时明确证明未经投影的 $z$ 不能作目标。

## 1. 带原始 Artin 标签的 Möbius 自同构

令 $F=K(z)$、$K=\mathbb Q(i)$，$z$ 是已推送短目标笔记中
`factors[0]` 的同一个 $44$ 次生成元。
$\sigma=\operatorname{Frob}_{(-1+2i)}$，在 $W$ 上的角色值为
$\omega=8+25i\in\mathbb F_{43^2}$。

R210 的整恒等式
$$
 (1-T)^{44}f_z\!\left(i\frac{1+T}{1-T}\right)
   =-2^{22}f_z(iT)
$$
说明
$$
 T(z)=\frac{iz+1}{z+i}
$$
是 $f_z$ 的另一个根。直接分式计算给 $T^2(z)=1/z$、$T^4(z)=z$。
由于 $F/K$ 的群是循环 $44$ 阶，且 R171 的中央元已有
$\sigma^{22}z=1/z$，$T$ 只可能为 $\sigma^{11}$ 或 $\sigma^{33}$。

本次用 R171 的同一 $P$，逐支构造
$A/\langle\beta^jP\rangle$，$\beta=-1+2i$，重新从三个二挠点和
同一个四挠点的 Vélu 像计算全部 $z_j=\sigma^jz$。
程序核验每条曲线方程、$43$ 阶、$44$ 次回到 $[5]P$、
同一 Miller 配对以及 $44$ 个 $f_z$ 根互异，并精确得到
$$
 \boxed{\frac{iz_j+1}{z_j+i}=z_{j+33}\quad(0\le j<44).}       \tag{219.1}
$$
两个可能的全局自同构有不同的有限约化，故这识别的是全局 Artin
标签，不只是一个有限域内的无标签排列。

对 $u=(z-i)/(z+i)$，(219.1) 给
$$
 u=-i\sigma^{33}z.                                           \tag{219.2}
$$
$-i$ 的阶与 $43$ 互素，在单位的 $43$ 进完成中为零。
若 $\chi(\sigma)=\widehat\omega$ 为 Teichmüller 角色，
$\widehat\omega^{11}=i$、$\widehat\omega^{33}=-i$，所以
$$
 e_\chi[u_0]=15e_\chi[u]=-15i\,e_\chi[z].                    \tag{219.3}
$$
因此 $e_\chi[z]$ 也是 R210 的原始单位基。

## 2. 一个准确的 $11\times4$ 域模型

令
$$
 w=\frac{z-1}{z+1},\qquad s=w^4.
$$
(219.1) 直接给 $\sigma^{33}w=iw$，从而
$$
 F=K(s)(w),\qquad w^4=s,\qquad [K(s):K]=11.                 \tag{219.4}
$$
例如，$w$ 不为零，且其四个 $C_4$ 共轭 $w,iw,-w,-iw$ 互异；
$z=(1+w)/(1-w)$，所以 $[F:K(s)]=4$。
$s\in\mathbb Q(z)\subset\mathbb R$（这里指所固定的嵌入），
故 $[\mathbb Q(s):\mathbb Q]=11$。

独立整数系数运算给
$$
 (1-W)^{44}f_z\!\left(\frac{1+W}{1-W}\right)
 =2^{44}G(W^4),                                             \tag{219.5}
$$
其中 $G$ 按升幂的全部 $12$ 个系数如下；没有把一个非首一模型称为
整生成元的最小首一多项式。

~~~text
-192729625626584369414512726636978197243,
926551488679638982674998852973172521996,
-1874414428789572915209405160403234419792,
2350052361684525486318411178199051936064,
-2683531151086929352415606548399156047360,
3145979246406249445872133724187297347584,
-2848333099199569425680312599725450240000,
1613319075198260809174206959435734745088,
-507415740960987096921712633003832180736,
72895064294055427212667925916949413888,
-2489170610090670880293602591870287872,
115980011003679269424630048315408384
~~~

由 (219.4)，这个次数 $11$ 的模型不可约。
它可供后续相对 Norm 运算采用，尚未用于宣称已算出单位基。

## 3. 一个必要边界：普通 $z$ 不是 Norm

记 $L=FL_q$，$L_q/K$ 为 R191 的导子 $(q)$ 的循环 $43$ 次扩张。
在 R171 固定的素点及 Weil 根下定义
$$
 \ell(a)=\log_\zeta\left(\overline a^{(q^2-1)/43}\right).
$$
本次实际算出的全部 $z_j$ 对数为
~~~text
0,9,31,37,22,35,34,14,19,7,35,19,35,7,19,14,34,35,22,37,31,9,
0,34,12,6,21,8,9,29,24,36,8,24,8,36,24,29,9,8,21,6,12,34
~~~
尤其 $\ell(z_1)=9\ne0$。
若普通 $X\in L^\times$ 满足 $NX=z$，则对 $\sigma X$ 有
$N(\sigma X)=\sigma z$。在固定 $q$ 素点的 tame 全分歧扩张中，
单位 Norm 的剩余值必须是 $43$ 次幂；$\ell(z_1)\ne0$ 给出矛盾。
因此
$$
 \boxed{z\notin N_{L/F}L^\times.}                            \tag{219.6}
$$
这与 $e_\chi[z]$ 是 Norm 并不冲突。实际 Fourier 检查给
$$
 \sum_{j=0}^{43}\omega^{\pm j}\ell(z_j)=0,
$$
而其余 $20$ 个奇次特征方向均非零。正是所需的两个角色投影
消去了局部障碍；不能把投影后的 Norm 存在性替换成 (219.6)
所排除的更强断言。

## 4. 一个可用的普通实单位目标

令 $a_j\in[-21,21]$ 为 $15\operatorname{Re}(\omega^j)$ 模 $43$
的中心整数代表，定义
$$
 U=\prod_{j=0}^{43}(\sigma^jz)^{a_j}.                         \tag{219.7}
$$
全部指数是
~~~text
15,-9,13,2,19,1,-3,-6,-7,-20,-12,0,12,20,7,6,3,-1,-19,-2,-13,9,
-15,9,-13,-2,-19,-1,3,6,7,20,12,0,-12,-20,-7,-6,-3,1,19,2,13,-9
~~~
每个 $z_j$ 都是普通单位；$a_{-j}=a_j$，$\tau z=z$，故
$$
 U\in E_F\cap F^{\langle\tau\rangle}.
$$
模 $43$ 的群环算子
$$
 \sum_j a_j\sigma^j=
 \frac{15}{2}\left(\sum_j\omega^j\sigma^j+
                        \sum_j\omega^{-j}\sigma^j\right)     \tag{219.8}
$$
只投影到 $\chi,\chi^{-1}$，在这两个分量上的标量是
$15\cdot44/2\equiv29\ne0$。

### 定理 219.1

存在普通全局单位 $X\in\mathcal O_L^\times$，使
$$
 NX=U,\qquad\tau X=X.                                      \tag{219.9}
$$

**证明。** R210 给普通单位 Norm 在 $\chi,\chi^{-1}$ 两个整分量
满射。(219.8) 说明 $U$ 在所有其他分量中被 $43$ 整除，而底域
单位嵌入到 $L$ 后的 Norm 是其 $43$ 次幂。因此 $U$ 在单位的
$43$ 进完成中属于 Norm 像。

普通单位 Norm 的余核被 $43$ 杀掉，因为 $N(v)=v^{43}$ 对底域
普通单位成立。它是有限的 $43$ 群；张量 $\mathbb Z_{43}$，再扩到
平坦的 $\mathcal O$，不会杀掉任何非零余核。因此上述完成的
Norm 可返回一个普通单位 $X_0$，且 $NX_0=U$ 精确成立。

由于 $\tau U=U$，取
$$
 X=\frac{(X_0\tau X_0)^{22}}{U}.
$$
它是普通单位并被 $\tau$ 固定，而
$NX=U^{44}/U^{43}=U$。证毕。

这给的是一个普通、精确、实的 Norm 方程，没有仅写完成的形式元素。
本次尚未求出 $X_0$ 或 $X$。

程序还从有限域数据直接检查 (219.7) 在全部 $44$ 个 $q$ 素点
的幂剩余符号均为零，作为 (219.8) 局部含义的实算核对。

## 5. 一旦求得 $X$，21 个符号即给实际 $\mathcal L$

令 $X$ 为任意满足 (219.9) 的普通单位。记
$$
 h_j=\ell(\sigma^jX),\qquad 1\le j\le21.
$$
则 R201 的同一个未知量准确为
$$
 \boxed{\mathcal L=
   4\sum_{j=1}^{21}\operatorname{Im}(\omega^j)h_j-3
   \pmod{43}.}                                             \tag{219.10}
$$
相应地
$$
 \rho=4\sum_{j=1}^{21}\operatorname{Im}(\omega^j)h_j,
 \qquad \Omega_2^\epsilon=\epsilon(13-\rho).                 \tag{219.11}
$$
这些 $h_j$ 尚未计算；上式没有把旧 $z_j$ 的符号充当 Norm 原像符号。

### 5.1 正确的整体比例

在 $\mathcal O$ 完成中令
$$
 P_+=\sum_{j=0}^{43}\widehat\omega^j\sigma^j,
 \qquad P_-=\sum_{j=0}^{43}\widehat\omega^{-j}\sigma^j.
$$
于是 $P_+^2=44P_+$、$P_+P_-=0$。
R185/R201 的同一 dual 基在复坐标表示为
$$
 d_0=\frac{i}{1848}P_+[u_0].
$$
先用 $P_+[u_0]=15P_+[u]$，再用 (219.2) 和
$P_+\sigma^{33}=\widehat\omega^{-33}P_+=iP_+$，得到
$$
 \boxed{d_0=-\frac{15}{1848}P_+[z].}                        \tag{219.12}
$$
这个反向特征因子与 (219.3) 中的 $e_\chi$ 方向不同，已经在公式中
明确处理。模 $43^2$ 时 $-15/1848\equiv15$，但证明先在整完成
中保留分母。

由 (219.8) 可写
$$
 [U]=\frac{15}{2}(P_++P_-)[z]+43Z,
 \qquad Z\in E_F\otimes\mathcal O.
$$
故
$$
 x_d=-\frac1{1848}\left(
       \frac2{44}P_+[X]-\frac2{44}P_+Z\right)               \tag{219.13}
$$
满足 $Nx_d=d_0$ 精确成立，因为底域元素 $P_+Z$ 的 Norm 是
$43P_+Z$。这给出了从一个普通 $X$ 到正确 completed Norm 基的
显式调整，没有把低整数权直接等同于整 Teichmüller 权。

$P_+Z$ 属于底域的目标角色单位分量；由 $\gamma_q=0$，它在全部
$q$ 素点的幂剩余符号为零。因此 (219.13) 的调整不改变所需
剩余值。模 $43$，$-1/1848=1$、$44=1$，所以该值为
$$
 2\sum_{j=0}^{43}\omega^j\ell(\sigma^jX).                  \tag{219.14}
$$
这是按同一个全局 $C_{44}$ 投影得到的值；绝不是未投影的单个点值。

### 5.2 实下降、有限坐标与根规范

$\tau X=X$，且 $\tau\sigma^j=\sigma^{-j}\tau$。
在固定 $q$ 素点上，$\tau$ 对剩余域作用是 $a\mapsto a^q$，
对 Weil 根作用是反演。因此
$$
 \ell(\sigma^{-j}X)=-\ell(\sigma^jX),
 \qquad \ell(X)=\ell(\sigma^{22}X)=0.
$$
(219.14) 的实部为零，虚部由成对的 $j,-j$ 合成，准确为
$4\sum_{j=1}^{21}\operatorname{Im}(\omega^j)h_j$。
这里的 $4$ 来自角色投影的 $2/44$ 和共轭配对的 $2$；不是
未分歧二次的有限 Frobenius 除数。

$x_d$ 是普通单位分量。R210 §7 已证明其正 Norm primitive
在固定全分歧 $q$ 位置的有限坐标为零；这里读取的是奇异坐标，
没有额外的有限坐标除 $2$。
整 $43^2$ Kummer lift 的规范根在 $\mu_{(q^2-1)/43}$ 中，
因此 (219.14) 的虚部正是 R210 的完整 Norm 剩余标量 $\rho$。
R201 已证明低权目标的根修正给 $\rho=\mathcal L+3$，遂得
(219.10)–(219.11)。

若更换普通单位解 $X$，其目标 $\chi$ 分量的差在 Norm 核中。
R210 的自由性给该核为 $(\gamma-1)E_{L,\chi}$，在全分歧素点的
剩余值为零；故 (219.10) 与所取单位解无关。
若改用非单位解，这个结论不能直接套用，仍须加 R200 的外支撑
Artin 修正。

## 6. 与 R207 的实际 43 次模型连接

令 $\theta$ 为 R207 的同一个实 Gaussian trace 生成元。
$L^+=L^{\langle\tau\rangle}$、$H=F^{\langle\tau\rangle}=\mathbb Q(z)$。
由于 $[H:\mathbb Q]=44$、$[\mathbb Q(\theta):\mathbb Q]=43$ 互素，
$$
 L^+=H(\theta),\qquad [L^+:H]=43.
$$
这不是一个未经证明的实域线性不交假设：互素次数已直接给出。
$K$ 使两边同时二次扩张，故对 $X\in L^+$，
$N_{L/F}X=N_{L^+/H}X$。

因此下一项需要实际求解的单方程为
$$
 \operatorname{Res}_T\left(P_\theta(T),
                  \sum_{k=0}^{42}x_kT^k\right)=U,
 \qquad x_k\in\mathbb Q(z),                               \tag{219.15}
$$
并取所得到的普通单位解。
它比原始两组 $1848$ 次 torsion 值的表示更短，但仍是一个真正的
全局 Norm 方程；本条没有把存在性或域模型当成已经获得的解。

### 6.1 已实际生成的单个 $\mathbb Q(z)$ 元素

本次还把 (219.7) 从共轭乘积转成一个完整的幂基输入。证书
`notes/o6_single_real_norm_target_certificate.json` 中，
`labeled_sigma_exact` 存储 $D_\sigma$ 以及全部 $44$ 对整数
$(A_k,B_k)$，`ordinary_real_norm_target_exact` 存储 $D_U$ 与全部
$44$ 个整数 $C_k$，均按升幂排列。它们准确满足
$$
 \sigma z=\frac{\sum_{k=0}^{43}(A_k+iB_k)z^k}{D_\sigma},
 \qquad
 U=\frac{\sum_{k=0}^{43}C_kz^k}{D_U},
 \qquad D_U=D_\sigma/12.                                  \tag{219.16}
$$
$D_\sigma$ 为 $449$ bit、其分子最大为 $519$ bit；
$D_U$ 为 $445$ bit、$C_k$ 最大为 $4738$ bit。
这些系数已全部写入证书，不需要下一轮重新猜测或重建目标。
分母来自幂基表示；$U$ 仍是由全局整单位的乘积得到的普通单位，
没有把幂基分母误当作有限素点的实际支撑。

**全局验证。** 最初用原 $q$ 的带标号根作 Hensel 提升并插值，
得到有理系数候选。随后在精确商环
$\mathbb Q(i)[Z]/(f_z)$ 中直接检查
$$
 f_z(S(Z))=0,\qquad S(Z)=D_\sigma^{-1}\sum_k(A_k+iB_k)Z^k.
$$
因此 $Z\mapsto S(Z)$ 是 $F/K$ 的一个自同构。
再于原 $q$ 检查全部 $44$ 个 $S(z_j)=z_{j+1}$，就把它唯一识别为
同一个正算术 Artin 生成元；认证没有依赖有理重建的稳定性猜测。

程序继续在同一精确商环递推 $44$ 个共轭，检查它们互异、周期恰为
$44$、中央元为倒数、$33$ 次元为 (219.1) 的 Möbius 变换，以及
$\overline{\sigma^jz}=\sigma^{-j}z$。最后以
$a_{j+22}=-a_j$ 将负指数换成其倒数共轭，实际相乘生成全部 $C_k$，
并检查虚部逐系数为零。
所以 (219.16) 是已算出的精确普通实单位输入，而非仅存在性结论。

(219.15) 的 **Norm 原像** 仍未求出；完整目标的生成没有改变
$\mathcal L$ 未知的状态。

## 7. 已执行的精确验证

- 程序：`scripts/verify_o6_single_real_norm_target.py`。
- 证书：`notes/o6_single_real_norm_target_certificate.json`。
- 已推输入：`notes/small_robert_norm_target_certificate.json`，SHA256
  `340b387727696e12cecf75cbdf08b4a09b5416c2f42d2191ddafe041d5b14104`。

~~~sh
python scripts/verify_o6_single_real_norm_target.py \
  notes/small_robert_norm_target_certificate.json \
  --check notes/o6_single_real_norm_target_certificate.json
~~~

本次标准库实现实际重算全部 $44$ 个 Vélu 分支、同一 Weil 配对、
全部 Möbius 标签、$44$ 个幂符号与 Fourier 投影、完整 $11$ 次模型
的整数恒等式、(219.8) 的卷积归一化，以及 (219.16) 的全局精确
自同构和实际普通实单位系数。结果 `PASS`。
没有重跑 R191 的大主化或 R207 的 $1325$ 素数 CRT。
证书明确保留 `actual_norm_preimage_computed:false`、
`actual_L_computed:false`。

主要依赖均为仓库内给出完整证明的 R163、R171、R185、R191、
R200、R201、R207、R210。本文的新算术恒等式、Norm 返回普通实单位
的步骤和 (219.10) 的完整比例均在上文证明。
R202 继续只留给实际求出的 $\mathcal L$；主问题仍开放。
