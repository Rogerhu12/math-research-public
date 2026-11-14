# R341：原六输入的混合联合测度、三次来源 core 与重叠源交换差

日期：2026-11-13。**状态：已证明。** 本篇把 R340 的三变量身份直接作用于原六个 sigma 输入，得到十三个确切的混合辅助坐标，按十二个原三元组分布。其中三种互补分割给两个辅助坐标的真正联合测度。辅助测度来自原三次截面 $C=y\sigma^3$，其质量、整个 $p$-core、全部环带及真实六次相位范围由同一 sigma 张量身份支付。原中央零因而无损传播到这些辅助深度条件。重叠三元组生成的群确为无限群，但实际来源的两个平均已有非零交换差；本篇不把个别联合身份自动扩成所有辅助坐标的联合独立。

## 1. 同一原目标与三条真正低次来源

沿用 R316、R333、R340 的固定曲线、周期和普通测度：
$$
E:y^2=x^3+b,\qquad b=17,\qquad
\delta^2=-3,\quad \omega=(\delta-1)/2,\quad
\gamma=(5+\delta)/2,
$$
$$
p>7,\qquad p\equiv1\pmod3,\qquad
\nu=\nu_{\sigma,17},\quad \Omega=\Omega_p.
$$
始终取
$$
\nu|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu,\qquad
\lambda=\frac{\varepsilon^3}{\bar\pi},\quad
\kappa=\frac p{\bar\pi^2},\quad t_p=\lambda\kappa.
\tag{1}
$$
原固定秩二来源仍是
$$
\boxed{
S=-\frac1{84}\prod_{j=1}^6\sigma(c_jz),\qquad
\boldsymbol c=(1,2,\delta,2\delta,\gamma,\bar\gamma).
}
\tag{2}
$$
因此在六个同一原输入 $X_1,\ldots,X_6$ 上，
$$
\nu_S=-\frac1{84}Y_*\nu^{\otimes6},\qquad
Y=\sum_{j=1}^6c_jX_j.
\tag{3}
$$
所有输出单位条件及 Mellin 测试始终施加于这个真实 $Y$。

定义三条原 degree 三来源
$$
A=\sigma^3,\qquad B=x\sigma^3=\sigma(\delta z)/\delta,\qquad
C=y\sigma^3=-\frac{\sigma(2z)}{2\sigma(z)}.
\tag{4}
$$
最后一式只是原二挠除法 theta 身份，不作为 Mellin 商使用。
$C$ 的零除子是三个非零二挠点，$C(0)=-1$。
在 $\mu_6$ 下，$A,B,C$ 的型分别为 $3,1,0$。

### 1.1 $C$ 的有界测度与全部原权

$A$ 是三个有界测度的卷积，$B$ 已由 (4) 给原测度。
$C$ 也不需借一个未付的商定义：从 $\zeta''=-2y$ 直接得到
$$
\boxed{
C=-\frac12\bigl(\sigma^2\sigma'''-3\sigma\sigma'\sigma''
                                      +2(\sigma')^3\bigr).
}
\tag{5}
$$
普通 sigma 的每次导数都对应原测度乘 $X/\Omega$，所以 (5) 是有界整测度。
其完全对称的三输入式为
$$
\boxed{
\nu_C=-\frac1{12\Omega^3}(X_1+X_2+X_3)_*
 \left[
 \prod_{i=1}^3(2X_i-X_j-X_k)\,\nu^{\otimes3}
 \right],
\quad \{i,j,k\}=\{1,2,3\}.
}
\tag{6}
$$
乘积内每个因子使用其余两个指标。确切展开为
$$
-\frac1{2\Omega^3}
\left\{\frac{\sum X_i^3}{3}
 -\frac{\sum_{i\ne j}X_i^2X_j}{2}+2X_1X_2X_3\right\}.
$$
所有平方与交叉项都保留。因为 $\int d\nu=0$、$\int X\,d\nu=\Omega$，
(6) 的总质量准确为 $-1$。

以下记各原测度为 $\nu_A,\nu_B,\nu_C$，并设
$$
\mathfrak a=[\delta^{-1}]_*\nu_A,\qquad
\mathfrak b=[\delta^{-1}]_*\nu_B=\delta^{-1}\nu,\qquad
\mathfrak c=[\delta^{-1}]_*\nu_C.
\tag{7}
$$
这些缩放都在同一原 $E_{17}$ frame 内。

## 2. 用整个张量身份支付 $C$ 的全 core

R340 已从原三变量 sigma 加法证明
$$
F=\delta^{-1}
\begin{pmatrix}
1&1&1\\1&\omega&\omega^2\\1&\omega^2&\omega
\end{pmatrix}
\in\operatorname{GL}_3(\mathbf Z_p)
$$
及完整有界测度等式
$$
\boxed{\begin{aligned}
F_*\nu^{\otimes3}
={}&\mathfrak a\otimes\mathfrak c\otimes\mathfrak c
+\mathfrak c\otimes\mathfrak a\otimes\mathfrak c
+\mathfrak c\otimes\mathfrak c\otimes\mathfrak a\\
&-3\mathfrak b^{\otimes3}-3b\,\mathfrak a^{\otimes3}.
\end{aligned}}
\tag{8}
$$
该式包含全部 finite phase、Gaussian 和原 $\delta$ 因子。

**全 core 定理。** 存在由原测度唯一决定的标量 $\lambda_A,\lambda_C$，使
$$
\boxed{
\nu_A|_p=\lambda_A[\kappa]_*\nu_A,\qquad
\nu_C|_p=\lambda_C[\kappa]_*\nu_C,
}
\tag{9}
$$
且
$$
\boxed{
\lambda_A^3=\lambda^3,\qquad
\lambda_A\lambda_C^2=\lambda^3,\qquad
\lambda_C^6=\bar\pi^{-6}.
}
\tag{10}
$$
特别
$$
\boxed{\eta_p:=\bar\pi\lambda_C\in\mu_6,\qquad
\lambda_C=-\nu_C(p\mathbf Z_p).}
\tag{11}
$$
(11) 是实际来源的完整相位规范，不是任意选择的六次单位。

**证明。** 因 $F$ 整可逆，它保持“全部三个坐标在 $p$ 内”的域。
由 (1)，(8) 左端在该域的限制准确为
$\lambda^3[\kappa]_*^{\otimes3}(F_*\nu^{\otimes3})$。
限制与各坐标的 $\mu_6$ 型投影交换。

先取型 $(3,3,3)$，它仅保留 $-3b\,\mathfrak a^{\otimes3}$，所以
$$
(\mathfrak a|_p)^{\otimes3}
=\lambda^3([\kappa]_*\mathfrak a)^{\otimes3}.
$$
非零向量的秩一张量唯一性给
$\mathfrak a|_p=\lambda_A[\kappa]_*\mathfrak a$、
$\lambda_A^3=\lambda^3$。这里 $\mathfrak a$ 的三阶矩非零；
也可选一个非零矩泛函收缩两次，直接得到同一结论。

再取型 $(3,0,0)$，准确只剩 $\mathfrak a\otimes\mathfrak c\otimes\mathfrak c$。
代入上一式、收缩非零 $\mathfrak a$ 后得
$$
(\mathfrak c|_p)^{\otimes2}
=\frac{\lambda^3}{\lambda_A}([\kappa]_*\mathfrak c)^{\otimes2}.
$$
$\mathfrak c$ 的质量为 $-1$，所以同样给唯一的 $\lambda_C$ 和
$\lambda_A\lambda_C^2=\lambda^3$。结合第一式得
$\lambda_C^6=\lambda^6=\bar\pi^{-6}$。
所有缩放 $[\delta^{-1}]_*$ 与深度、$[\kappa]_*$ 交换，故得到 (9)。
最后对 $\nu_C$ 的整个质量取值给 (11)。$\square$

这一证明不依赖未识别的 Katz 值，也不从有限素数的相位样本推广。
本篇不把 $\eta_p$ 擅自换成某个 conductor 二十七角色的猜测公式。

### 2.1 真正质量一的二挠辅助测度

置
$$
\boxed{\rho_2=-\mathfrak c=-[\delta^{-1}]_*\nu_C.}
\tag{12}
$$
它与 R337 的 $\rho=X\nu/\Omega$ 是两个不同的原测度。
由 (9)–(11)，
$$
\boxed{
\rho_2(\mathbf Z_p)=1,\qquad
[\zeta]_*\rho_2=\rho_2\ (\zeta\in\mu_6),\qquad
\rho_2|_p=\lambda_C[\kappa]_*\rho_2.
}
\tag{13}
$$
因此对每个 $n\ge0$，
$$
\boxed{
\rho_2(p^n\mathbf Z_p)=\lambda_C^n,\qquad
\rho_2(p^n\mathbf Z_p^\times)=\lambda_C^n(1-\lambda_C).
}
\tag{14}
$$
$\lambda_C$ 是单位而不是 $p$ 的倍数。特别所有深度质量都是单位。
不能像处理 R337 的 $\rho$ 一样，把这里的无限环带和当作 Banach 范数衰减级数。
准确的任意有限分割是
$$
\rho_2=\sum_{n=0}^{M-1}\lambda_C^n[\kappa^n]_*\rho_2^\times
             +\lambda_C^M[\kappa^M]_*\rho_2,
\tag{15}
$$
最后一项必须保留。

公式 (13) 也给全部矩与 tame。若
$C(z)=\sum c_mz^m$，则
$$
\int_{\mathbf Z_p^\times}X^m\,d\rho_2
=(1-\lambda_C\kappa^m)(-\delta^{-m})\Omega^m m!c_m.
\tag{16}
$$
把第 $n$ 环带输出除以 $p^n$，其完整 tame Mellin 函数准确乘
$$
\lambda_C^n\tau(\bar\pi)^{-2n\ell}
                   \langle\bar\pi\rangle^{-2n(p-1)u}.
\tag{17}
$$
没有删除深度质量或尺度导数。

### 2.2 环带质量的非零与准确可能损失

$1-\lambda_C$ 永不为零：否则 (10) 迫 $\bar\pi^6=1$，与
$N_{K/\mathbf Q}(\bar\pi)=p$ 矛盾。故 (14) 的环带质量也全部非零。

还可不识别 $\eta_p$ 就限定其可能非单位的普通素数。
若 $v_p(1-\lambda_C)>0$，则原 $\pi$ 位整除 $\bar\pi-\eta_p$。
其正整数范数为
$$
N(\bar\pi-\eta_p)=p+1-\operatorname{Tr}(\pi\eta_p).
$$
对 $p>7$，它严格介于零与 $2p$ 之间；故被 $p$ 整除只能等于 $p$，
从而 $\operatorname{Tr}(\pi\eta_p)=1$。
写 $\pi\eta_p=(1+v\delta)/2$，这里 $v$ 是奇整数，得到
$$
\boxed{
4p=1+3v^2,\qquad p=3n^2+3n+1
\quad\text{对某个整数 }n.
}
\tag{18}
$$
所以除这个明确的候选集合外，所有 (14) 的环带质量都是单位。
该集合在 $p\le X$ 中只有 $O(\sqrt X)$ 个整数；本篇只将它作为明确的精度例外，
不假定每个候选素数真的损失单位性。实际损失始终是 $v_p(1-\lambda_C)$。

## 3. 单个原三元组的完整混合联合身份

考虑原 (2) 中任意三个尺度 $c_i,c_j,c_k$。
假定找到真实 CM 单位相位
$$
r_1,r_2,r_3\in\mu_6,\qquad
r_1c_i+r_2c_j+r_3c_k=0.
\tag{19}
$$
可同时乘一个单位令 $r_1=1$。定义原输入的混合辅助坐标
$$
\boxed{
L_{\boldsymbol r}=\delta^{-1}
             (\bar r_1X_i+\bar r_2X_j+\bar r_3X_k).
}
\tag{20}
$$
这只混合原六个输入，没有新增三个叶输入或改变原目标。

令 $\mathsf P_{0,L}$ 为辅助坐标的 $\mu_6$ 平均。
**原联合定理**为
$$
\boxed{
\mathsf P_{0,L}(Y,L_{\boldsymbol r})_*
        \left(-\frac1{84}\nu^{\otimes6}\right)
              =\nu_S\otimes\rho_2.
}
\tag{21}
$$
原 $Y$ 不被平均、不被缩放，所有其余三个原输入取全域。

**证明。** 写 $r_2=\alpha,r_3=\beta$，并取
$$
D=\operatorname{diag}(1,\alpha^{-1}\omega^2,\beta^{-1}\omega),
\qquad T=FD.
$$
$T$ 是原三输入空间的整可逆变换，其第二行正是 (20)。
由 (19)，变换后的实际输出尺度
$\boldsymbol d=(T^{-1})^t(c_i,c_j,c_k)^t$ 满足 $d_2=0$。
因此这三个原因子的输出只依赖新坐标的第一、第三项。

$D_*\nu^{\otimes3}=(\alpha\beta)^{-1}\nu^{\otimes3}$。
对 (8) 的第二坐标取完整 $\mu_6$ 不变投影，$A$、$B$ 的非平凡型被杀掉，
准确只保留
$$
\mathfrak a\otimes\mathfrak c\otimes\mathfrak c
              +\mathfrak c\otimes\mathfrak c\otimes\mathfrak a.
\tag{22}
$$
它在中间辅助坐标上是同一 $\mathfrak c$，在两个 active 坐标上是
$\mathfrak a\otimes\mathfrak c+\mathfrak c\otimes\mathfrak a$。
中间坐标的质量为 $-1$。故将第一、第三坐标按其真正的
$d_1,d_3$ 相加后，联合式恰为原三因子输出测度乘 $-\mathfrak c=\rho_2$；
$(\alpha\beta)^{-1}$ 在原三因子和联合式中是同一实际相位。
附回其余三个原 sigma 输入以及 $-1/84$，即 (21)。$\square$

因此对任何满足 $h(\zeta L)=h(L)$ 的有界连续函数 $h$，
(21) 可直接作用于未平均的原输入域，得到
$$
\boxed{
Y_*\{h(L_{\boldsymbol r})(-1/84)\nu^{\otimes6}\}
                 =\left(\int h\,d\rho_2\right)\nu_S.
}
\tag{23}
$$
这包括 $h$ 为任意深度或 exact 环带的指标。该式先是整个输出测度身份，
随后可取真实 $Y\in\mathbf Z_p^\times$、任意 tame 及全部 Mellin 变量。

## 4. 原六尺度的全部十三个单位法向量

在 (2) 的固定顺序中，归一 $r_1=1$ 后，全部单位相位三项关系如下。
表内相位按该行三个指标的顺序排列；每行的辅助坐标都用 (20)，
不得把相位删成没有尺度的输入和。

| 原指标 | 三个原尺度 | 关系相位 $(r_1,r_2,r_3)$ |
|---|---|---|
| $1,2,3$ | $1,2,\delta$ | $(1,\omega,-1)$ |
| $1,2,3$ | $1,2,\delta$ | $(1,\omega^2,1)$ |
| $1,2,5$ | $1,2,\gamma$ | $(1,-\omega,\omega)$ |
| $1,2,6$ | $1,2,\bar\gamma$ | $(1,-\omega^2,\omega^2)$ |
| $1,3,5$ | $1,\delta,\gamma$ | $(1,-\omega,-1)$ |
| $1,3,6$ | $1,\delta,\bar\gamma$ | $(1,\omega^2,-1)$ |
| $1,4,5$ | $1,2\delta,\gamma$ | $(1,-\omega^2,-\omega)$ |
| $1,4,6$ | $1,2\delta,\bar\gamma$ | $(1,\omega,-\omega^2)$ |
| $1,5,6$ | $1,\gamma,\bar\gamma$ | $(1,\omega^2,\omega)$ |
| $2,3,5$ | $2,\delta,\gamma$ | $(1,-1,\omega)$ |
| $2,3,6$ | $2,\delta,\bar\gamma$ | $(1,1,\omega^2)$ |
| $3,5,6$ | $\delta,\gamma,\bar\gamma$ | $(1,-1,1)$ |
| $4,5,6$ | $2\delta,\gamma,\bar\gamma$ | $(1,-\omega,\omega^2)$ |

每行均为 $\mathbf Z[\omega]$ 内的精确恒等式。
这张表可以完全枚举验证：对二十个有序指标集合
$\{i<j<k\}$，逐一检查 $\alpha,\beta\in\mu_6$ 的三十六种可能
$c_i+\alpha c_j+\beta c_k$。证书只执行这有限固定计算，没有扫描目标素数。

表中恰有三种互补三元组分割：
$$
\boxed{
(123)\mid(456),\qquad
(145)\mid(236),\qquad
(146)\mid(235).
}
\tag{24}
$$
第一种分割可使用 $123$ 的任一合法法向量。
在每一种分割内，两次变换作用于互不相交的原变量，故两个真实投影交换。
逐次应用 (21) 得
$$
\boxed{
\mathsf P_{0,L_1}\mathsf P_{0,L_2}
 (Y,L_1,L_2)_*\left(-\frac1{84}\nu^{\otimes6}\right)
             =\nu_S\otimes\rho_2\otimes\rho_2.
}
\tag{25}
$$
这是在原六输入上得到的两个真正独立辅助坐标；没有借取任意角函数作为额外来源。

## 5. 原完整中央的无损深度传播

令 $J_S(u)$ 为原 principal 完整单位 Mellin 函数，$d=p-1$。
对 (21) 的一个辅助坐标，或 (25) 的两个辅助坐标，分别要求
$$L_i\in p^{n_i}\mathbf Z_p
\quad\text{或}\quad L_i\in p^{n_i}\mathbf Z_p^\times.$$
令 $e$ 为选取环带的坐标数。由 (14)、(23)、(25)，准确有
$$
\boxed{
J_{S;\boldsymbol n,e}(u)
=\lambda_C^{\sum_i n_i}(1-\lambda_C)^eJ_S(u).
}
\tag{26}
$$
所有非单位原输入、原输出 carry 和其他 tame 分支都包含在测度身份中；
比例系数与 $u$ 无关，故
$$
\boxed{
J'_{S;\boldsymbol n,e}(0)
=\lambda_C^{\sum_i n_i}(1-\lambda_C)^eJ_S'(0).
}
\tag{27}
$$
特别仅取深度条件时，不论深度多大，(27) 都由单位标量无损返回原中央。
取环带时系数也总非零，准确损失为 $e\,v_p(1-\lambda_C)$；
除 (18) 的明确候选集合外没有这项损失。

这些是原中央零的真实等价观察。它们直接混合原六个输入，
与 R340 在一个新范数三展开内部产生的辅助坐标不同。
相同的原则仍须保留：如果额外限制尚未处理的原变量，
右端变成这些限制下的原输出测度，不能继续写成同一个 $J_S$。

## 6. 重叠三元组的真实反射群不是有限群

将一行相位向量补零成六维向量 $\boldsymbol r$。
它满足 $\boldsymbol c^t\boldsymbol r=0$、
$\boldsymbol r^*\boldsymbol r=3$。
辅助坐标旋转 $\zeta\in\mu_6$ 在原六变量中的实际变换是
$$
\boxed{
M_{\boldsymbol r}(\zeta)
=1+\frac{\zeta-1}{3}\boldsymbol r\boldsymbol r^*.
}
\tag{28}
$$
这由第3节的 $T^{-1}\operatorname{diag}(1,\zeta,1)T$ 直接得到，
所以不是另选一个保持相同输出的抽象矩阵。
它保持真实 $Y$。两个不交三元组的 (28) 交换，而重叠者一般不交换。

取表中两行
$$
\boldsymbol r=(1,\omega^2,1,0,0,0)^t,\qquad
\boldsymbol s=(1,0,0,-\omega^2,-\omega,0)^t.
\tag{29}
$$
二者都是真正原关系，且
$$
\boldsymbol r^*\boldsymbol r=\boldsymbol s^*\boldsymbol s=3,\qquad
\boldsymbol r^*\boldsymbol s=1.
$$
令 $M_r=M_{\boldsymbol r}(\omega)$、$M_s=M_{\boldsymbol s}(\omega)$。
二者各为三阶复反射。其乘积在 $\operatorname{span}\{\boldsymbol r,\boldsymbol s\}$
上的行列式和迹准确为
$$
\det(M_rM_s)=\omega^2,\qquad
\operatorname{Tr}(M_rM_s)=\frac53\omega.
\tag{30}
$$
在其余四维上乘积为恒等。迹公式直接来自
$\operatorname{Tr}(P_rP_s)=1/9$ 和 $(\omega-1)^2=-3\omega$。

若乘积有限阶，两条二维特征值除以 $\omega$ 仍是单位根，
其和 $5/3$ 必为代数整数，矛盾。因此这两个真实反射已经生成无限群。
这没有赋予其 $p$ 进闭包一个可免费应用于原测度的有界 Haar 平均；
有限商的阶数和其中的 $p$ 因子仍须支付。

## 7. 重叠平均在原来源上已有非零交换差

记原辅助不变投影
$$
\Pi_r=\frac16\sum_{\zeta\in\mu_6}[M_{\boldsymbol r}(\zeta)]_*,
\qquad
\Pi_s=\frac16\sum_{\zeta\in\mu_6}[M_{\boldsymbol s}(\zeta)]_*.
\tag{31}
$$
这正是 (21) 所用的实际投影。不能只因为每个投影分别给联合身份，
便把它们迭代成任意多个辅助坐标的联合身份。

这里可以直接在原来源上支付这个问题。
用 $\Omega$ 归一的六变量 Laplace 变换为
$$
\Phi(\boldsymbol z)=\prod_{i=1}^6\sigma(z_i)
                  =P_6(\boldsymbol z)+\text{更高项},\qquad
P_6=\prod_{i=1}^6z_i.
$$
置
$$
Q_r=1-\boldsymbol r\boldsymbol r^*/3,\qquad
Q_s=1-\boldsymbol s\boldsymbol s^*/3.
$$
第一次六相位平均在 $P_6$ 中最多遇到辅助变量三次，
第二次最多五次，因为两个三元组只占五个原坐标。
因此两个平均都准确只取相应辅助变量的零次项，得到
$$
\boxed{
[\text{六次齐次项}]\,
\widehat{(\Pi_r\Pi_s-\Pi_s\Pi_r)\nu^{\otimes6}}(\boldsymbol z)
=P_6(Q_s^tQ_r^t\boldsymbol z)-P_6(Q_r^tQ_s^t\boldsymbol z).
}
\tag{32}
$$
在一个固定有理测试方向上，实际值是
$$
\boxed{
P_6(Q_s^tQ_r^t(1,2,3,4,5,6)^t)
-P_6(Q_r^tQ_s^t(1,2,3,4,5,6)^t)
=\frac{-96214+105848\omega}{2187}\ne0.
}
\tag{33}
$$
生产证书另直接求和所有三十六项相位，独立核定同一数。
乘回原 (3) 的 $-1/84$ 后，交换差仍非零。
所以这里不只是两个矩阵不交换：实际原六 sigma 测度的交换差已经非零。

同时 $\boldsymbol c^t\boldsymbol r=\boldsymbol c^t\boldsymbol s=0$，
所以每个 (28) 都保持实际输出。沿
$\boldsymbol z=t\boldsymbol c$ 的整个交换差恰为零。
这准确说明新的难点：完整原输出并未改变，
但为控制多个相关输入域而交换投影时，会出现 (32) 的真实剩余来源。
它不能由原 $J_S'=0$ 自动设为零。

## 8. 与原一单位深度域的交叠

相较 R337 的两个辅助正深度域避开一单位线，
本篇的原混合坐标确实触及目标的实际一单位区域。
例如在 (24) 的第一种分割中，若原 $X_1$ 为单位，
其余五个输入均在 $p^N$ 内，则 $123$ 辅助坐标为单位，
$456$ 辅助坐标在 $p^N$ 内。
因此该真实一单位域包含在 (26) 已控制的“一个环带、一个深度”域中。

但这个包含并非等号。例如取
$$
(X_1,\ldots,X_6)=(1,1,0,0,0,0).
\tag{34}
$$
对 $123$ 的相位 $(1,\omega^2,1)$，
辅助坐标为 $(1+\omega)/\delta$，是单位；
$456$ 辅助坐标为零，所以满足任意 $N$ 的深度条件。
真实相加输出为 $3$，也是当前素数处单位。
它却有两个原单位输入，属于仍须保留的补域。

R339 的链式原叶深度域映到原六尺度后也满足相应包含，
但叶条件还限制了该域的更多内部坐标。
既不能由包含关系传递中央零，也不能把三种互补分割的各自联合身份
拼成一个尚未证明的多辅助联合身份。式 (32) 已具体显示后一拼接的来源成本。

因此下一项要支付的是这些实际域的交叠、补域和源交换差。
本篇已付原观察本身及其全部精度，没有将“有足够多线性独立坐标”
当成已经覆盖原独立深度网格。

## 9. 证书与依赖

脚本 check-jzero-active-triple-joints-and-original-reflection-commutator.py
及同名 JSON 核对原 $C$ 的全部三次权、完整固定相位枚举、
每个真实零输出坐标、三种不交分割、两个原反射的无限性判据，
以及三十六项实际原源平均的非零六阶交换差。
全部计算在 $\mathbf Q(\omega)$ 内精确完成，没有目标素数扫描。
全测度、张量 core、单位质量与各个域的证明在正文。

- [R316：同一原 sigma 与普通 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R333：固定六 sigma 原来源与完整负矩族](R333-six-original-sigma-inputs-and-two-quadratic-negative-moment-return.md)。
- [R337：四变量原联合式与十二线域](R337-original-hadamard-domain-transport-and-depth-zero-propagation.md)。
- [R339：原范数三独立深度非零子域](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
- [R340：完整三变量 sigma 身份与原范数三链](R340-original-ternary-fourier-joint-measure-and-collision-domains.md)。

