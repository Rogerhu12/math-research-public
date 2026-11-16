# R874 — 原整 q 展开的分数 Hecke 理想、全 packet 度数界与实际逆返回

日期：2026-11-16。

**状态：完整原整 q 格、有限9×3呈示、全 packet 范数界和逆 Hecke 返回在下文证明。公开 producer 用精确数域、Smith/Hermite 整矩阵与 R873 的严格范数选择实际候选；其计算结果另按真实 run 登记。整 q 展开只是必要条件，不被提升为已构造的 Hom。** 本篇保持原三条 CM 角色、R864 的定向余循环、$C_v$ 的原微分及 R831/R839 的全 Artin 组合。

R873 已表明只使用原整数倍和整单位会付很大的实际度数。
本篇允许原同一个 Hecke packet 中的任意有理方向，
然后用整对应准确返回原 $\Xi_0$，不把新的方向计为独立算术来源。

## 1. 两个三次整数环与原线性读数

设
$$
F=\mathbf Q(a),\qquad a^3=17,\qquad
E=\mathbf Q(\vartheta),\qquad \vartheta^3-3\vartheta+1=0.
$$
$E$ 是 $\mathbf Q(\zeta_9)^+$，其整数环与一个固定基为
$$
\mathcal O_E=\mathbf Z[\vartheta],\qquad
\mathcal B_E=(1,\vartheta,\vartheta^2-2),\qquad
\operatorname{disc}E=81.
\tag{1}
$$
保持 R867 的真正整 Hecke 对应
$$
\mathscr R=2T_7^2+7T_7-8T_{13}-28,
\tag{2}
$$
它在原三个本征线上取 $\vartheta$ 的三个实共轭值。
$\mathscr R$ 是原 Jacobian 上的整对应；
后面的 $\mathcal O_E$ 作用在其指定 packet 上解释，
不把抽象有理 endomorphism 当作自动整。

另一整数环的固定基是
$$
\boxed{
\mathcal O_F=
\mathbf Z\cdot1+\mathbf Z\cdot a+
 \mathbf Z\cdot\frac{a^2-a+1}{3},\qquad
\operatorname{disc}F=-867.
}
\tag{3}
$$
为核定3处的指数，令 $t=(a^2-a+1)/3$，直接算得
$t^3-t^2+6t-12=0$。该整基的判别式为
$(-27\cdot17^2)/3^2=-867$。
3处的剩余判别式指数为1，不能再有3的整指数；
17处 $a$ 是 Eisenstein 的 tame 均匀化元，按各幂不同的模3赋值
$\mathbf Z_{17}[a]$ 已整闭。其它素数不整除判别式。
这证明(3)，没有把 $\mathbf Z[a]$ 错当作全整数环。

沿 R864、R866，置
$$
\alpha=-1+2\omega,\quad c=-1-19\omega,\quad
u_1=\tau^2\ell,\quad u_2=c/\ell ,
$$
并保原
$$
\Xi_0^*\omega_v=H_0(q)\frac{dq}{q},\qquad
C_v:Y^2+vY=X^3,\quad
v=-122465-47628a-\frac{314892}{17}a^2.
$$
在基(1)上定义真实首系数读数
$$
\boxed{
\begin{aligned}
\lambda(1)&=1,\\
\lambda(\vartheta)&=c_1=\alpha^{-1}u_1+(\alpha/c)u_2,\\
\lambda(\vartheta^2-2)&=c_2=(\alpha^2/c)u_1+\alpha^{-2}u_2.
\end{aligned}}
\tag{4}
$$
这正是 R867 附录 B 的两个未除首项的原输入。
它们在 $F$，因为 R869 的 $\Xi_0$ 已下降到 $F$，
而(2)及其整多项式均定义于 $\mathbf Q$。

$\lambda:E\to F$ 是 $\mathbf Q$-线性同构。
可不依靠一个浮点矩阵说明其单射：
在 $L=K(a)$ 上，$T(v)=\tau^2(\ell)\tau^2(v)$ 满足 $T^3=c$，
其轨道 $1,T1,T^21$ 恰为 $1,u_1,u_2$。
$c=\alpha^3\omega^2$ 在 $K$ 中不是立方，故 $X^3-c$ 不可约。
任一非零向量的 $T$-循环空间因而维数3；
所以 $1,u_1,u_2$ 是 $K$-基。
从原 $1,b,b^2$ 换到(1)是可逆的 $K$-基变换，
便给(4)的单射，进而由维数给同构。

## 2. 目标的一个全局最小模型

令
$$
X'=a^2X,\qquad Y'=a^3Y.
$$
原模型变为
$$
\boxed{
E':Y'^2+17vY'=X'^3,\qquad
\omega_{\min}=\frac{dX'}{2Y'+17v}=\frac{\omega_v}{a}.
}
\tag{5}
$$
$17v$ 是 $\mathcal O_F$ 整数，且
$$
N_{F/\mathbf Q}(17v)=-17^2.
\tag{6}
$$
因此除了17上方的位，它在所有有限位都是单位。

在17处，R866 附录 A 已给
$\operatorname{ord}_a(17v)=2$、
$\operatorname{ord}_a\Delta(E')=8$。
在3上方任意位 $\mathfrak q$，
$$
\operatorname{ord}_{\mathfrak q}\Delta(E')
=3e(\mathfrak q/3)\le9,
$$
因为 $17v$ 是该处单位。在其余位判别式是单位。
每处的判别式赋值都小于12，所以整 Weierstrass 模型(5)处处最小：
任何更小整模型会使赋值减少一个正的12倍，不可能。
特别地 $\omega_{\min}$ 是全局 Néron 不变微分的一枚生成元。

这同时处理了坏3处；没有从17处的单个必要条件猜全局最小性。
源的 $\infty$ 光滑整盘则由 R866 附录 A 引用的
Česnavičius–Neururer–Saha 原陈述给出，对所有有限位均是原
$\mathcal O_F[[q]]$，参数宽度仍为1。

## 3. 全部 q 系数恰由一个整数环控制

对 $u\in E$，把原准同态记为 $\Xi_u=\Xi_0\circ u$，
其中 $u$ 通过(2)作用。设原本征形式的第 $m$ 个 Hecke 系数为
$a_m\in E$，三个共轭对应 R862 的固定次序。
则完整 Fourier 输入为
$$
\boxed{
H_u(q)=\sum_{m\ge1}\lambda(ua_m)q^m,\qquad
\Xi_u^*\omega_{\min}
=\frac{H_u(q)}a\,\frac{dq}{q}.
}
\tag{7}
$$
(7)是全部 Gauss 系数的同一个线性恒等式，不只首项。

原 CM 理想公式表明每个 $a_m$ 是代数整数；
又 $a_m\in E$，所以 $a_m\in\mathcal O_E$。
反向也有准确的整生成：
$$
\boxed{
\operatorname{span}_{\mathbf Z}\{a_m:m\ge1\}=\mathcal O_E.
}
\tag{8}
$$
首先 $a_1=1$。因 $7\nmid2601$，权2 Hecke 关系给
$a_7^2=a_{49}+7$。故(2)准确化为
$$
\vartheta=2a_{49}+7a_7-8a_{13}-14a_1.
\tag{9}
$$
再把 $\mathscr R^2-2$ 展开。
所有涉及的好 Hecke 乘积都满足
$T_mT_n=\sum_{d\mid(m,n)}d\,T_{mn/d^2}$，
所以 $\vartheta^2-2$ 也是 $a_m$ 的整线性组合。
所需下标至多 $49^2=2401$。三枚基(1)均在左侧，证明(8)。
不需要数值枚举出一个偶然的整秩证书。

于是(7)的全部 Néron-normalized q 系数整，当且仅当
$$
\boxed{
u\in I_\infty:=
\{u\in E:\lambda(u\mathcal O_E)\subset a\mathcal O_F\}.
}
\tag{10}
$$
特别地，对任何真实 $\Xi_u$，Néron 映射性质作用于原整光滑
$\infty$ 邻域，必得 $u\in I_\infty$。

反过来，(10)只认证整 Fourier 微分。
它没有保证形式积分在椭圆形式群中整，更没有保证原有理函数坐标存在。
真实 Hom 仍须经 R870 或 R866 的完整函数恒等式认证。

## 4. 同一个分数理想的准确9×3矩阵

在基(1)上，乘 $\vartheta$ 与 $\vartheta^2-2$ 的列矩阵是
$$
M_1=
\begin{pmatrix}
0&2&-1\\1&0&1\\0&1&0
\end{pmatrix},\qquad
M_2=
\begin{pmatrix}
0&-1&2\\0&1&-1\\1&0&-1
\end{pmatrix}.
\tag{11}
$$
令 $M_0=I_3$。若 $z=A+Ba+Ca^2\in F$，
其在整数基(3)上的坐标为
$$
\operatorname{coord}_{\mathcal O_F}(z)
=(A-C,\ B+C,\ 3C)^{\mathsf t}.
\tag{12}
$$
对 $k=0,1,2$ 定义 $B_k$ 的第 $j$ 列为
$$
\operatorname{coord}_{\mathcal O_F}
 \left(\frac1a\sum_{i=0}^2
       \lambda(\mathcal B_{E,i})(M_k)_{ij}\right),
\qquad
B=\begin{pmatrix}B_0\\B_1\\B_2\end{pmatrix}\in M_{9,3}(\mathbf Q).
\tag{13}
$$
于是(10)准确等价于
$$
\boxed{
I_\infty=\{\mathcal B_E x:x\in\mathbf Q^3,\ Bx\in\mathbf Z^9\}.
}
\tag{14}
$$

$B_0$ 因 $\lambda$ 同构而可逆。
因此(14)包含一个有限指数整数格，又包含在
$B_0^{-1}\mathbf Z^3$ 中，是完整秩3格。
此外，对任意 $v\in\mathcal O_E$，
$\lambda(uv\mathcal O_E)\subset\lambda(u\mathcal O_E)$。
故
$$
\boxed{I_\infty\text{ 是 }E\text{ 中的非零分数 }\mathcal O_E
\text{ 理想}.}
\tag{15}
$$
它不是任意9条无联系的同余约束。

producer 的精确算法如下。置
$C=(B_1;B_2)B_0^{-1}$，取正整数 $D$ 清其分母，
并作整数 Smith 分解
$$
U(DC)V=S,\qquad U,V\text{ unimodular}.
$$
令
$$
d_i=\frac D{\gcd(D,S_{ii})}\quad(i=1,2,3),
$$
其中 $S_{ii}=0$ 时取 $d_i=1$。
则一组列基是
$$
\boxed{
L=B_0^{-1}V\operatorname{diag}(d_1,d_2,d_3).
}
\tag{16}
$$
原因是令 $z=B_0x$，条件成为
$z\in\mathbf Z^3$、$DCz\in D\mathbf Z^6$；
左右 unimodular 变换把它准确化为三个对角整除。
随后只作列 Hermite 基变换，不改变格或行列式绝对值。
运行同时核 $BL$ 整、$L^{-1}M_1L$ 与 $L^{-1}M_2L$ 整，
所以有限输出确实有(15)的理想稳定性。

## 5. 一个具体范数17的非单位方向

R867 的两枚单位之外，有
$$
u_0=\vartheta^2+1=3+(\vartheta^2-2),\qquad
\boxed{N_{E/\mathbf Q}(u_0)=17.}
\tag{17}
$$
其两个共轭是 $3-\vartheta-(\vartheta^2-2)$ 和 $3+\vartheta$；
三者的乘积为17。这是实际整 Hecke 对应
$\mathscr R^2+1$，并非把整数倍17重新命名。

它恰消原17处的坏分支。由 R864 的完整 $\ell$，在 $a$ 模下
$$
\ell\equiv12(\omega-1),\qquad
\ell/\alpha\equiv11+9\omega,\qquad
(\ell/\alpha)+(\ell/\alpha)^{-1}\equiv13=-4\bmod17.
\tag{18}
$$
在这里 $\ell/\alpha$ 是被原 Gauss 系数选中的 $\zeta_9$ 根。
$u_0$ 的该剩余值为 $(-4)^2+1=0$。
更准确，三个
$$
G_j=1+u_1/b_j+u_2/b_j^2
$$
在 $a$ 模下恰是被该根选中的3和其余两枚0。
因为所有本征 Fourier 系数在17整，(18)证明
$$
H_{u_0}(q)/a\quad\text{在17的所有 q 系数均整}.
\tag{19}
$$
这是全 q 断言，不只质量或首项。
然而(19)没有判其3处与其它位的条件，
也没有证明 $\Xi_{u_0}$ 是真实 Hom。
producer 将把(17)作为原分支校准，明确输出它是否通过全部九条(13)。

## 6. 任意成功方向都有真正整 Hecke 逆返回

对任意非零 $u\in I_\infty$，在基(1)上写
$u^{-1}=r_0+r_1\vartheta+r_2(\vartheta^2-2)$。
取正整数 $m$ 清掉三个有理分母，则
$$
T_u=m u^{-1}\in\mathcal O_E
$$
由(2)给原 Jacobian 上的真实整 Hecke 对应。
如果原坐标证书确实构造了 $\Xi_u$，就有完整同源恒等式
$$
\boxed{\Xi_u\circ T_u=m\Xi_0.}
\tag{20}
$$
同一微分、基点与特征零 Hom 单射固定该等式，
不是有限 Fourier 近似。

即使尚未认证 $\Xi_u$，由于 $I_\infty$ 是理想，
$uT_u=m\in I_\infty$。
第一块(13)于是给 $m/a\in\mathcal O_F$。
对有理数 $r$，$r/a$ 在所有有限位整准确迫
$r\in17\mathbf Z$：17处需要 $3v_{17}(r)-1\ge0$，
其它位 $a$ 是单位，禁止有理分母。
所以
$$
\boxed{m\in17\mathbf Z.}
\tag{21}
$$
producer 将此作为实际返回整数的严格核对。

成功的(20)随后接 R867 的整 T7/13 公式，
恢复原三条 Hom 所需的共同整数倍及 R866 的
$2^{11}\kappa$、R862/R839 的全部 Artin 系数。
允许非单位方向的意义是先重建一个较低度的真实映射，
再付(20)的整数成本；不把该成本从原 shadow 中删去。

## 7. 分数理想给整个 packet 的严格度数下界

令 R873 的原三个正权为 $a_0,a_1,a_2$，
为避免与常数域的 $a$ 混淆，本节改写成 $w_0,w_1,w_2$。
对任意 $u\in E$，规范准度数是
$$
\mathfrak d(u)=\sum_{j=0}^2 w_j|\sigma_j(u)|^2,
\qquad
g=(w_0w_1w_2)^{1/3}.
\tag{22}
$$
若 $\Xi_u$ 真实，它就是该映射的度数。
保持原三个 $\sigma_j$ 与 R862 的标签，不按 LLL 输出重标。

以基(1)计，设
$$
N(I_\infty)=|\det L|.
$$
对 $0\ne u\in I_\infty$，主理想 $(u)\subset I_\infty$，
且二者都是秩3格。因此
$$
|N_{E/\mathbf Q}(u)|
=N(I_\infty)\,[I_\infty:(u)]
\ge N(I_\infty).
\tag{23}
$$
AM–GM 随即给
$$
\boxed{
\mathfrak d(u)\ge
3g\,N(I_\infty)^{2/3}
\qquad(0\ne u\in I_\infty).
}
\tag{24}
$$
该界覆盖整个分数理想，包括非单位和有理分数方向。
它不需要证明理想主化，也不是只取单位范数1。

如果(24)的严格球下界大于 R870 的 $102k$，
就排除该权下整个原 packet 的全部真实候选。
若没有排除，LLL 只用于选择更合适的原 $u$，不提供存在性证明。
本篇没有把可除因子、Manin 理想或全 Hom 格饱和等同于(10)。

## 8. 原低权证书的实际输入

对所选 $u$，保完整
$$
H_u=q\,f_u(Q),\qquad Q=q^3,\qquad f_u(0)=\lambda(u)\ne0.
$$
不能把 $H_u$ 除以 $\lambda(u)$ 而不同时改变原准同态。
R870 的 formal-group 递推和严格恒等式逐项换为该输入。
若 $A,B\in M_k(\Gamma_0(867))$，记
$$
C_{A,B}=(Q A')B-A(Q B').
$$
原 $Y=A/B$ 的完整证书是
$$
\boxed{
C_{A,B}^3
=H_u(q)^3 A^2(A+vB)^2B^2.
}
\tag{25}
$$
$H_u^3$ 是 $Q$ 上的实际 weight6 形式，未添新的周期。
相同的 $612(k+1)$ Sturm 门和非零分母条件认证(25)；
再用
$$
X=H_u(q)\frac{Y(Y+v)}{D_QY}
$$
恢复同一 $\Xi_u$，其首部为
$X\sim\lambda(u)^{-2}q^{-2}$、
$Y\sim-\lambda(u)^{-3}q^{-3}$。
完成这一步之后才可用(20)回到原 Hom 和原交点 shadow。

## 9. 公开 producer

脚本为
`scripts/check-r874-original-cusp-integral-hecke-lattice.py`。
执行参数：
```
sage -python scripts/check-r874-original-cusp-integral-hecke-lattice.py --M 1024 --bits 384 --radius 2 --top 12
```
它仅读同目录已提交的 R873 producer 中的精确理想系数生成函数，
不读旧输出数据，不将曾输出的近似正权当作新严格输入。

程序依次给出：

- (4) 在原 $F$ 中的精确坐标、(13) 全9×3矩阵、(16)的实际列基；
- 分数理想的范数、Smith/Hermite 证书和两枚整单位的稳定性；
- 对(17)的完整全局九条件结果；
- 同一 AFE 的严格球正权与(24)的全 packet 下界；
- 真实分数理想中经整数 LLL 选择的有限候选，及每个候选的
  原未归一首项、严格度数球、实际整数 $m$ 和返回多项式 $T_u$。

LLL 使用高精度球中点取整得到的正定近似来选择基，
但所有候选均在精确理想基中产生，最后以原严格正权重新计算度数。
它不声称所列候选是全局最短向量。
精确全报告仅在公开日志，仓库保脚本、参数、run和哈希。

本篇尚未执行并通过任何新的(25)，所以仍未给非零原 shadow。
当前新增的是可核验的真正整 q 格和能回原对象的非单位来源，
而不是再次放大一个已经被 R866/R873 排除的整数单位候选。

## 10. 来源

- [R862](R862-original-seventeen-torsion-product-and-complete-cubic-hom-matrix.md)、
  [R864](R864-original-seventeen-torsion-exact-field-and-cocycle.md)：
  原固定角色、Gauss 矩阵、余循环及绝对尺度。
- [R866](R866-original-modular-function-certificate-and-level-nine-model.md)
  附录 A：CNS 原文的 smooth 整 q 盘与 Néron 论证。
- [R867](R867-original-single-hom-and-integral-hecke-three-basis.md)：
  真实整 Hecke 对应及 packet 中的全部多项式关系。
- [R869](R869-original-modular-input-and-cubic-field-descent.md)：
  原 $H_0,\Xi_0$ 的 $F$ 下降。
- [R870](R870-original-low-weight-quotient-and-exact-elliptic-coordinate-certificate.md)：
  原低权椭圆恒等式和有限认证界。
- [R873](R873-original-cm-petersson-norms-and-integral-hom-degree-bounds.md)：
  原全坏位范数、复面积与严格正权。
- K. Česnavičius, M. Neururer, A. Saha,
  *The Manin constant and the modular degree*，
  <https://arxiv.org/pdf/1911.09446v3>，印刷第4页：
  全局 $\infty$ 光滑开子概形及 $\mathbf Z[[q]]$ 完成。

(1)是实九次分圆子域的标准整数环；
(3)、全局最小性、(8)及矩阵/理想/逆返回均已在本文直接支付。


## 11. 实际完整格、主生成元与第一候选

**已证明（精确数域/整矩阵运算及 R873 的严格球证书）。**
修复相对域坐标接口后的源提交
`16d843db59fac18cecbbc4c47b32692bf87e0f67`，
[run43834068620](https://github.com/Rogerhu12/math-research-public/actions/runs/43834068620)、
job133186195650，于2026-11-16 08:47:59 UTC完成PASS；
Sage10.6，计算4.013177878秒。参数为
`--M 1024 --bits 384 --radius 2 --top 12`。
首次失败及其纯接口修复见
[运行记录](../notes/2026-11-16-r874-relative-field-api-repair.md)。

完整输出SHA256：
`4a4541c8a99e20c48b4c1bb78d437c3fd9a0498d248ccc78f1fe6cd411a55019`；
精确格报告SHA256：
`b69b72ffb224a8bd7b6ccaddccf95c416a4bdda9005cf36ad81dce223ba041cb`；
producer SHA256：
`74a48b5f326bdf97e89ec61bbd9e90ecb5513ec475af667e772560c7fcaa4c54`。
依赖的固定镜像、R873脚本及精确系数流哈希均在同次公开日志。
不保存可重算的完整矩阵/候选输出文件。

(4)的原首系数化简为
$$
\boxed{c_1=-497+237a-17a^2,\qquad c_2=609-44a-75a^2.}
\tag{26}
$$
全9×3约束给一组准确列基
$$
L=\begin{pmatrix}
1/18523&0&0\\
3058/18523&1/3&0\\
229486/18523&44/3&17
\end{pmatrix},\qquad
\boxed{N(I_\infty)=17/55569.}
\tag{27}
$$
Smith阶段的清分母为1，三个对角元均为1；
故本例全部 Hecke 条件事实上已由第一块
$B_0x\in\mathbf Z^3$支付。这个结论来自全矩阵，
不是提前假设首项足够。

特别(17)的非单位 $\vartheta^2+1$ 通过全部九条条件；
它在3处以及其它有限位的全 q 整性现也已付。
它仍未被认作实际 Hom。

LLL选择得到
$$
\boxed{
u_*=\frac{915+1097\vartheta+2962(\vartheta^2-2)}{55569},
\qquad N(u_*)=-\frac{17}{55569}.
}
\tag{28}
$$
其精确坐标满足(14)，而(23)的指数恰为1，所以
$$
\boxed{I_\infty=u_*\mathcal O_E.}
\tag{29}
$$
原首项及实际返回算子为
$$
\boxed{
\lambda(u_*)=\frac{68+7a-13a^2}{3},\qquad
u_*\bigl(106+59\vartheta+185(\vartheta^2-2)\bigr)=17.
}
\tag{30}
$$
后一恒等式通过 $\vartheta^3-3\vartheta+1=0$ 精确核验。
因此只要完整构造 $\Xi_{u_*}$，原整算子
$106+59\mathscr R+185(\mathscr R^2-2)$
便准确返回 $17\Xi_0$。

整个 packet 的严格下界为
$$
364.3945<3g\,N(I_\infty)^{2/3}<364.3946.
\tag{31}
$$
故权2的度数帽204排除全 $I_\infty$ 中的非零真实映射，
不再只排单位方向。权4以上没有由此被排除。

第一候选的完整球给
$$
\boxed{|\mathfrak d(u_*)-376|<10^{-88}.}
\tag{32}
$$
(32)是严格有理区间断言，**没有**由近似值推出准度数恰等于376，
没有将 $u_*$ 认证为全局最短，也没有认定 $\Xi_{u_*}$ 已整。
若后续(25)认证实际映射，整数度数才将使(32)识别其度数为376。
后两个所列候选分别有包住664、712的严格小区间，尚不需要展开搜索。

下一实际计算使用(28)的完整原 $H_{u_*}$。
权4帽408尚可能容纳该度数，但其 Riemann–Roch 保证范围只有323；
权6的保证范围527可容纳(32)，前提始终是实际映射存在。
依次执行真实低核和完整椭圆恒等式，不能以该范围代替整性证明。


## 12. 当前坐标候选的准确小目标与唯一二处非最小尺度

这里仍用 (28) 的同一 $u_*$，记
$\lambda=\lambda(u_*)$。令
$$
e=18-7a,\qquad
t=\frac{a^2-a+1}{3},\qquad
\beta=\frac{a^2+2a+7}{3}=t+a+2.
\tag{33}
$$
R864 附录 A 已付 $e$ 为范数一整数单位及
$e^3v=7-18a^2/17$。直接在 $a^3=17$ 中相乘，得到
$$
\boxed{\lambda=e\,a\,\beta,\qquad
\beta^2=13+5a+2a^2,\qquad
\beta^3=\frac{244+95a+37a^2}{3}.}
\tag{34}
$$
后一式也等于 $7\beta^2-5\beta+2$。因此 $\beta$ 是整数，
$\beta^3-7\beta^2+5\beta-2=0$，且 $N(\beta)=2$。
其次数确为三，因为 $t+a+2$ 不是有理数；所以这个首一三次式
就是它的最小多项式。

当前 producer 的目标并不是另选曲线。它准确是原坐标同构
$(X,Y)\mapsto(\lambda^2X,\lambda^3Y)$ 所给的
$C_{v_{\rm new}}$，其中
$$
\boxed{
v_{\rm new}=\lambda^3v
=\beta^3(119-18a^2)
=\frac{-34-17a+11a^2}{3}
=11t-2a-15.
}
\tag{35}
$$
用 (34) 乘 $119-18a^2$，常数、$a$、$a^2$ 系数分别为
$-34/3,-17/3,11/3$，所以这里是精确小式，不是小数识别。
全模型在 $\mathcal O_F$ 上整，且
$$
N(v_{\rm new})=-2312,\qquad
v_{\rm new}^3+34v_{\rm new}^2+1445v_{\rm new}+2312=0.
\tag{36}
$$
例如迹为 $-34$，平方迹为 $-1734$，两两积和为1445；
范数也由 $N(\lambda)^3N(v)=34^3(-1/17)$ 直接给出。
没有改变原 $F$ 的嵌入或原 $H_{u_*}$。

若要同时使用小参数和全局最小微分，可改为
$$
\boxed{
C_{\min,\mathrm{sm}}:\quad
Y^2+(119-18a^2)Y=X^3,\qquad
(X,Y)=((ae)^2X_{\rm orig},(ae)^3Y_{\rm orig}).
}
\tag{37}
$$
(37)只是 (5) 经过整数单位 $e$ 的同构，故处处最小。
从当前 $C_{v_{\rm new}}$ 到 (37) 的实际同构是
$(X,Y)\mapsto(X/\beta^2,Y/\beta^3)$。
于是同一准映射拉回 (37) 的 Néron 微分时首系数恰为 $\beta$；
当前首系数一的微分则是它除以 $\beta$。这不把任意系数除法
当作目标椭圆群的 endomorphism。

二处唯一的区别也准确可读：
$\mathcal O_F$ 的指数只含3，所以模2的分解由
$$
a^3-17\equiv(a+1)(a^2+a+1)
$$
给出。$\beta\bmod2=a^2+1$ 只在一次因子处为零。
再由 $N(\beta)=2$，其在这唯一范数2素理想处赋值为1，
在其它所有有限位是单位。因此 (35) 的模型只在该二处
比 (37) 多一个真正的缩放，判别式多12阶；其余位仍最小。
对 R859 的全部 $r>3$ 惰性好素数，这两个小模型的返回是整单位同构，
但二处的尺度仍不能从特征零证书、原 Néron 规范中删去。

本节是显示的三次域恒等式和整数范数推导，没有新增数值执行。
它简化实际坐标及其有限域消费；实际 $\Xi_{u_*}$ 的整性
仍只由完整曲线证书决定。R875 已独立将其准度数准确识别为376，
并证明这是整个 $I_\infty$ 的最小值，不能反过来以 (35) 认定映射存在。
