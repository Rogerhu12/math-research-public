# R785：原 Rosati 等型块高度压缩与外积的规范切向类

日期：2026-11-15。状态：**下列结构压缩、原高度 jet 公式及规范切向类已证明。没有计算任何新的高度值，也没有证明该切向类对实际素数非零或为单位。**

本文接 R724 的实际 Chow–Heegner 高度输入，将其中完整的对称矩阵 $H$ 压成每个活跃简单等型块的一个 Rosati 不变系数域元素。随后把真正需要检测的中心首项写成这些元素、原局部 Poincaré 值和两列原 $Y$-对数数据的准确收缩。压缩不改变 $\eta_h,\chi$、原极化、截面、因子 $2$、清分母及 $p$ 外项；它不把 R728/R732/R781 的函数构造或 Abel 数据称作高度数据。

## 1. 原对象、实际同源与极化次序

采用 R724：
$$
 B=J_Y,\qquad B_\eta=e_\eta B,\qquad
 \eta_h=e_\eta\eta_h,\qquad
 \Lambda_h=\lambda_{p,h}-2\ell_h(\log P_Y),
$$
$$
 P_Y(x)=[\phi(x)-\phi(c_0)].
\tag{785.1}
$$
各活跃简单块记为 $C_\alpha$，次数 $d_\alpha=\dim C_\alpha$，重数为 $m_\alpha$。R596/R724 给一个域
$$
 F_\alpha\hookrightarrow\operatorname{End}_{\mathbb Q}^0(C_\alpha),
 \qquad [F_\alpha:\mathbb Q]=d_\alpha,
$$
以及
$$
 C_\alpha(\mathbb Q)\otimes\mathbb Q\simeq F_\alpha,\qquad
 \log:C_\alpha(\mathbb Q)\otimes\mathbb Q_p
      \xrightarrow{\sim}\operatorname{Lie}(C_\alpha)(\mathbb Q_p).
\tag{785.2}
$$
不假设任何 $p$ 进高度非退化。

取实际有理同源
$$
 \iota:\mathcal C=\prod_\alpha C_\alpha^{m_\alpha}
                     \longrightarrow B_\eta.
\tag{785.3}
$$
其准逆、分母和全部诱导映射必须在实际实现中记录；下面的 $\iota^{-1}$ 只表示有理同态范畴中的准逆，不表示在点上任意选择一个同源原像。

在每个 $C_\alpha$ 上取有理极化 $\lambda_\alpha$，令 $\lambda_0$ 是乘积极化。原 $B$ 的极化限制及拉回为
$$
 \lambda'=\iota^\vee\lambda_Y\iota,\qquad
 M=\lambda_0^{-1}\lambda'.
\tag{785.4}
$$
$M$ 是实际有理自同态；原极化不是未经证明的乘积极化。不同有理简单块间没有非零同态，故 $M$ 按 $\alpha$ 分块。

下面证明，每块 $M_\alpha$ 是 $F_\alpha$ 上的 Hermitian 矩阵。本文始终使用
$$
 h_{\lambda'}(x,y)=h_{\lambda_0}(x,M y).
\tag{785.5}
$$
所以 $M$ 作用于第二变量，不取逆，不移到两侧各一次。式 (785.5) 中的高度均为 R724 的 theta 极化后双线性配对；Poincaré 配对是它的两倍。

## 2. 活跃简单块的全部有理自同态域

**引理 785.1。** 在 (785.2) 下，
$$
 \operatorname{End}_{\mathbb Q}^0(C_\alpha)=F_\alpha.
\tag{785.6}
$$

**证明。** $C_\alpha$ 在 $\mathbb Q$ 上单，故
$D_\alpha=\operatorname{End}_{\mathbb Q}^0(C_\alpha)$ 是有限维除环。
非零有理自同态是同源，因而在
$W_\alpha=C_\alpha(\mathbb Q)\otimes\mathbb Q$ 上可逆。
所以 $W_\alpha$ 是非零左 $D_\alpha$-向量空间。于是
$$
 \dim_{\mathbb Q}D_\alpha
 \le \dim_{\mathbb Q}W_\alpha=d_\alpha.
$$
另一方面，$F_\alpha\subset D_\alpha$ 已有维数 $d_\alpha$。
两者相等，得到 (785.6)。$\square$

令 $*$ 为 $\lambda_\alpha$ 的 Rosati 在 $F_\alpha$ 上的限制。
它可以为恒等；下面的证明也保留非平凡 involution 的写法，
不额外假设系数域全实。因为域交换，换一个有理极化不改变这个 involution。
乘积上 Rosati 是共轭转置 $N\mapsto N^{*t}$。
由 (785.4)，
$$
 M_\alpha\in M_{m_\alpha}(F_\alpha),\qquad
 M_\alpha^{*t}=M_\alpha.
\tag{785.7}
$$
其正定性是原极化的实性质；没有把它解释为 $p$ 进符号或单位性。

## 3. 允许且确实相容的 Hodge splitting

原 $h_Y$ 不预先假定 $F_\alpha$ 相容。本节构造一个相容的参考 splitting，
再用 R724 (724.4)–(724.7) 在原 $\Lambda$ 中精确比较。

$V_\alpha=H^1_{\rm dR}(C_\alpha/\mathbb Q)$ 是秩二的 $F_\alpha$-模，
Hodge 子空间是秩一的 $F_\alpha$-子模。极化交替配对可唯一写成
$$
 \langle u,v\rangle=\operatorname{Tr}_{F_\alpha/\mathbb Q}\Psi(u,v),
$$
其中 $\Psi$ 是非退化的 $*$-skew-Hermitian 形式：
$$
 \Psi(a u,b v)=a^*b\,\Psi(u,v),\qquad
 \Psi(v,u)=-\Psi(u,v)^*.
\tag{785.8}
$$
例如以
$\operatorname{Tr}(a\Psi(u,v))=\langle u,a v\rangle$
定义 $\Psi$，由迹配对非退化立即得到这些性质。

取 Hodge 线的生成元 $e$，取 $f$ 使 $\Psi(e,f)=1$。
令 $b=\Psi(f,f)$，则 $b^*=-b$。
置
$$
 f'=f+\frac b2e.
$$
直接计算给 $\Psi(f',f')=b+b^*/2-b/2=0$。
故 $F_\alpha f'$ 是定义在 $\mathbb Q$ 上的
$F_\alpha$-稳定 Lagrangian 补空间。恒等 involution 情形只是 $b=0$。

在全部 $m_\alpha$ 个重数副本使用同一个补空间。
它稳定于 $M_{m_\alpha}(F_\alpha)$，从而稳定于实际 $M_\alpha$。
因此该补空间不仅对 $\lambda_0$ 各向同性，
也对 $\lambda'=\lambda_0M$ 各向同性：
$$
 \langle u,v\rangle_{\lambda'}=\langle u,Mv\rangle_{\lambda_0}=0.
$$
经实际 $\iota$ 运输，并在不活跃块上取相容补空间，
得到 $Y$ 上的参考 splitting。

这个改变没有删去原 Picard 项。若对应的高度差是
$D(\log P,\log Q)$，R724 精确给
$$
 \lambda_{p,h}-\lambda^{\rm ref}_{p,h}
       =2D(\log P_Y,\log\eta_h),\qquad
 \ell_h-\ell_h^{\rm ref}=D(\,\cdot\,,\log\eta_h).
\tag{785.9}
$$
所以 $\Lambda_h$ 作为同一截面上的局部函数不变。
此后都在这个明确的参考 splitting 中计算右侧两项，
不能只改其中一项。

相容性还给
$$
 h_\alpha(aP,Q)=h_\alpha(P,a^*Q).
\tag{785.10}
$$
其局部理由是同一 Poincaré 双扩张的
$(a\times1)^*\mathcal P\simeq(1\times a^\vee)^*\mathcal P$
保持刚性化；补空间相容使两边曲率相同，规范 Poincaré log 的唯一性
使该同构为等距。$p$ 外规范局部项也具有同一函子性。
这同时证明 (785.5)，没有只从全局数值相等反推局部规范。

## 4. 每个活跃块只有一个真实高度元素

从原 $\eta_h$ 的实际同源投影选非零
$P_\alpha\in C_\alpha(\mathbb Q)\otimes\mathbb Q$。
若要用实际群点，先清分母并把该整数保留在全部坐标中。
由 (785.2)，
$$
 C_\alpha(\mathbb Q)\otimes\mathbb Q=F_\alpha P_\alpha.
$$
记 $F_{\alpha,p}=F_\alpha\otimes\mathbb Q_p$。

**定理 785.2。** 存在唯一
$$
 \mathfrak c_\alpha\in F_{\alpha,p},\qquad
 \mathfrak c_\alpha^*=\mathfrak c_\alpha,
\tag{785.11}
$$
使
$$
 h_\alpha(xP_\alpha,yP_\alpha)
     =\operatorname{Tr}_{F_{\alpha,p}/\mathbb Q_p}
                 (\mathfrak c_\alpha x^*y).
\tag{785.12}
$$
进而在原 $B_\eta$ 上，
$$
 \boxed{\quad
 h_Y\!\left(\iota(\mathbf x_\alpha P_\alpha)_\alpha,
            \iota(\mathbf y_\alpha P_\alpha)_\alpha\right)
 =\sum_\alpha\operatorname{Tr}
       (\mathfrak c_\alpha\mathbf x_\alpha^{*t}
                            M_\alpha\mathbf y_\alpha).
 \quad}
\tag{785.13}
$$

**证明。** $t\mapsto h_\alpha(P_\alpha,tP_\alpha)$
是 $F_{\alpha,p}$ 上的 $\mathbb Q_p$-线性泛函。
迹配对非退化给唯一 $\mathfrak c_\alpha$。
对称性和 (785.10) 给
$h_\alpha(P_\alpha,t^*P_\alpha)
 =h_\alpha(tP_\alpha,P_\alpha)
 =h_\alpha(P_\alpha,tP_\alpha)$，
所以 $\mathfrak c_\alpha^*=\mathfrak c_\alpha$。
再由 (785.10)，
$h_\alpha(xP_\alpha,yP_\alpha)
 =h_\alpha(P_\alpha,x^*yP_\alpha)$，得到 (785.12)。
乘积极化使不同副本正交，随后用 (785.5)，得到 (785.13)。$\square$

因此不必计算 R724 原先可使用的
$b\times b$ 全矩阵，$b=\sum_\alpha m_\alpha d_\alpha$。
所需真实高度参数的数目至多
$$
 \sum_\alpha d_\alpha\le b,
$$
精确的 Rosati 对称参数维数是
$$
 D_{\rm ht}=\sum_\alpha
      \dim_{\mathbb Q}F_\alpha^{*=1}.
\tag{785.14}
$$
可用基元 $f_j\in F_\alpha$ 的真实配对
$h_\alpha(P_\alpha,f_jP_\alpha)$
及准确的迹矩阵恢复 $\mathfrak c_\alpha$；
不反演高度矩阵，也不假设其中任何数非零。
如只取 $F_\alpha^{*=1}$ 的基，限制的迹配对仍非退化，
可用恰 $D_{\rm ht}$ 个标量。

这些配对可全部在原 Jacobian $J_Y$ 上实现。
令 $j_{\alpha,1}:C_\alpha\to B_\eta\hookrightarrow B$
为实际 $\iota$ 的第一副本映射。
正极化使 $M_{\alpha,11}\ne0$，故
$$
 h_\alpha(P_\alpha,fP_\alpha)
 =h_Y\bigl(j_{\alpha,1}P_\alpha,\,
           j_{\alpha,1}(M_{\alpha,11}^{-1}fP_\alpha)\bigr).
\tag{785.14a}
$$
右侧两个有理点张量清分母后，可直接用 R724 的原 Jacobian
Poincaré 求值，并按双线性除回；不需要另援引一般阿贝尔簇高度的比较。
$M_{\alpha,11}^{-1}$ 的分母完整保留，不假设它在 $p$ 处整。

这是待计算输入的严格减少，不是已经得到这些标量。
实际 $M_\alpha,\iota,P_\alpha$、原 Poincaré 局部值和非 $p$ 项仍须生成。
改变 $P_\alpha$ 为 $uP_\alpha$ 时，
$\mathfrak c_\alpha$ 变为 $u^*u\mathfrak c_\alpha$，
点和对数的坐标同时除以 $u$，所以 (785.13) 不变。

## 5. 原 $\ell_h$ 与全部高度 jet 的压缩公式

置
$$
 \ell_\alpha=\log P_\alpha\in\operatorname{Lie}(C_\alpha)(\mathbb Q_p).
$$
由 (785.2)，乘法
$F_{\alpha,p}\to\operatorname{Lie}(C_\alpha)$，$u\mapsto u\ell_\alpha$，
是同构。这里的“除以 $\ell_\alpha$”指这个同构的逆，
不把 $\ell_\alpha$ 当成已知单位。

对原 $\eta_h$ 记准确坐标
$$
 \iota^{-1}\eta_h=(\boldsymbol\xi_{h,\alpha}P_\alpha)_\alpha,
 \qquad \boldsymbol\xi_{h,\alpha}\in F_\alpha^{m_\alpha}
\tag{785.15}
$$
（对 $p$ 进线性组合的 $h$ 按线性延拓）。
对 $v\in\operatorname{Lie}(B)$，定义
$$
 \iota_*^{-1}e_\eta v
       =(\mathbf z_\alpha(v)\ell_\alpha)_\alpha.
\tag{785.16}
$$
于是
$$
 \boxed{\quad
 \ell_h(v)=\sum_\alpha\operatorname{Tr}
   \bigl(\mathfrak c_\alpha
          \boldsymbol\xi_{h,\alpha}^{*t}
          M_\alpha\mathbf z_\alpha(v)\bigr).
 \quad}
\tag{785.17}
$$
这是 R724 (724.12) 的相同泛函：两者在
$B(\mathbb Q)\otimes\mathbb Q_p$ 的对数像上均等于
$P\mapsto h_Y(P,\eta_h)$，在活跃块上对数为同构，
不活跃块按原块相容 splitting 为零。
原 $P_Y$ 没有被别的投影点替代。

令 $z=a-1$，并在同一个 $c_1$ 盘上写
$$
 \mathbf z_\alpha(\log P_Y(c_1+z))
      =\sum_{k\ge0}\mathbf z_{\alpha,k}z^k,\qquad
 \lambda_{p,i}(c_1+z)=\sum_{k\ge0}\lambda_{i,k}z^k.
\tag{785.18}
$$
尤其两列原数据是
$$
 (\mathbf z_{\alpha,0}\ell_\alpha)_\alpha
      =\iota_*^{-1}e_\eta\log P_Y(c_1),
$$
$$
 (\mathbf z_{\alpha,1}\ell_\alpha)_\alpha
      =\iota_*^{-1}e_\eta
          \left.\frac{d}{dz}\log P_Y(c_1+z)\right|_{z=0}.
\tag{785.19}
$$
$\mathbf z_{\alpha,0}$ 是原有理点
$\iota^{-1}e_\eta P_Y(c_1)$ 的 Mordell–Weil 坐标；
它不等于零列的默认值。
定义
$$
 \Theta_{i,k}
  =\sum_\alpha\operatorname{Tr}
       (\mathfrak c_\alpha\boldsymbol\xi_{i,\alpha}^{*t}
                           M_\alpha\mathbf z_{\alpha,k}).
\tag{785.20}
$$
则对全部 $k\ge0$，
$$
 \boxed{[z^k]\Lambda_i=\lambda_{i,k}-2\Theta_{i,k}.}
\tag{785.21}
$$

原 $\lambda_{i,k}$ 必须用 R724 (724.15)–(724.23)
在同一参考 splitting、原 tensor 表示和原截面上求值。
它包含 universal-extension 修正
$\Delta_Q=\log_I Z-r(\log Q)$、第二类周期、
Picard 因子和截面标量；(785.21) 没有把它替换为任意同曲率原函数。
当前 R781 准确 Laurent 前缀提供的是原函数恢复输入，
并不提供 $\lambda_{i,k}$ 或 $\mathfrak c_\alpha$。

## 6. 真正决定首个外积系数的规范切向类

在 R729 给共同 Abel 首阶 $m=1$ 的范围内，
采用 R634 的同一加权迹坐标：
$$
 t_i=1+T_i z+O(z^2),\qquad r=g-1\ge2.
$$
原坏靶为 R696 的零。置
$$
 d_i=\Lambda_i(c_1),\qquad g_i=[z]\Lambda_i,\qquad
 v_i=T_i-T_g,\qquad s_i=2d_iT_i-g_i.
\tag{785.22}
$$
这里 $g_i$ 是高度的一次系数，不是 genus。
使用 R634 的切向结论及 R729 的 $m=1$，只取已证的向量
$(v_i)_{i=1}^r\ne0$，不预设每个 $v_i\ne0$ 或所有 $T_i$ 两两不同。
$V_i=t_i^2-t_g^2$、$W_i=d_it_i^2-\Lambda_i$
满足
$$
 V_i=2v_i z+O(z^2),\qquad W_i=s_i z+O(z^2).
$$
因此
$$
 [z^2]E_{ij}=2(s_i v_j-s_j v_i).
\tag{785.23}
$$

选一个已认证 $v_{i_0}\ne0$ 的下标 $i_0$，允许其余 $v_i=0$，定义 $r-1$ 个数
$$
 \varepsilon_i=s_i-\frac{v_i}{v_{i_0}}s_{i_0},
 \qquad i\ne i_0.
\tag{785.24}
$$
它们表示一个准确的商空间类
$$
 \mathscr T_p=[(s_i)_{i=1}^r]
       \in\mathbb Q_p^r/\mathbb Q_p(v_i)_{i=1}^r.
\tag{785.25}
$$
若为坐标分裂作了有限扩域，同一公式在该域中成立。
有
$$
 [z^2]E_{i_0i}=-2v_{i_0}\varepsilon_i.
\tag{785.26}
$$

**定理 785.3。**
$\mathscr T_p\ne0$ 当且仅当至少一个真实 $E_{ij}$
在 $c_1$ 的零阶恰为二。
$\mathscr T_p$ 在 R724 允许的 $Y$ splitting 改变下不变，
也在 R699 允许的 $F$ 相容 $A$ splitting 改变下不变。

**证明。** 前一断言直接由 (785.23)–(785.26)。
$Y$ 变化在整个 $\Lambda$ 中按 (785.9) 抵消。
对 $A$ 变化，R699 给
$\Lambda_i'-\Lambda_i=r_i t_i^2-r_g t_g^2$，
从而
$$
 d_i'-d_i=r_i-r_g,\qquad
 g_i'-g_i=2r_iT_i-2r_gT_g,
$$
$$
 s_i'-s_i=-2r_g(T_i-T_g)=-2r_gv_i.
$$
差向量恰在被商掉的直线中，故 (785.25) 不变。$\square$

特别，“$g_h$ 不全为零”既不是正确的充要条件，
也不代替 $\mathscr T_p\ne0$。
原 $\kappa$ 已包含在 R634 的坐标中，没有在这里去掉。

将 (785.21) 代入，必须同时保留两列：
$$
 s_i
 =2T_i\lambda_{i,0}-\lambda_{i,1}
       +2\Theta_{i,1}-4T_i\Theta_{i,0}.
\tag{785.27}
$$
最后一项来自 $d_i t_i^2$ 的 CM 标定；
仅计算切向列 $\mathbf z_{\alpha,1}$ 会漏掉它。
令 $q_i=v_i/v_{i_0}$，可进一步写成
$$
\begin{split}
 \varepsilon_i={}&
 2T_i\lambda_{i,0}-\lambda_{i,1}
 -q_i(2T_{i_0}\lambda_{i_0,0}-\lambda_{i_0,1})\\
 &+2\sum_\alpha\operatorname{Tr}\Bigl(
 \mathfrak c_\alpha
 \bigl[
  (\boldsymbol\xi_{i,\alpha}^{*t}
       -q_i\boldsymbol\xi_{i_0,\alpha}^{*t})
       M_\alpha\mathbf z_{\alpha,1}\\
 &\hspace{43mm}
 -2(T_i\boldsymbol\xi_{i,\alpha}^{*t}
       -q_iT_{i_0}\boldsymbol\xi_{i_0,\alpha}^{*t})
       M_\alpha\mathbf z_{\alpha,0}
 \bigr]\Bigr).
\end{split}
\tag{785.28}
$$
式中全部值属于同一次相容选择。改变 splitting 会同时改变
$\mathfrak c_\alpha$ 和原 $\lambda_{i,k}$；
不能固定后者而把前者当作可自由调整的实际参数。

## 7. 对原证书的用途与尚缺的真实量

R724 在 $m=1$ 时使用
$F_{ij}(u)=u^{-2}E_{ij}(p^4u)$。
因此
$$
 F_{ij}(0)=p^8[z^2]E_{ij}.
$$
若 $\mathscr T_p=0$，这些 $F_{ij}$ 全在中心为零，
所规定的闭盘单位理想 Bézout 证书不可能成立。
此时必须先准确证明并处理更高共同中心因子；
不能凭有限精度“看起来零”多除一次 $u$。

若 $\mathscr T_p\ne0$，只得到中心已无共同零及某个外积准确首阶为二。
仍须对非中心根使用 R703/R716 的完整尾与 R724 的有限 Bézout 不等式。
本定理没有证明深度四盘已经无根。

对一次真实首项计算，最少的尚未输出数据可明确列成：

1. 原同源与极化的准确 $\iota,M_\alpha$、$\eta_h$ 坐标
   $\boldsymbol\xi_{h,\alpha}$、真实 $\ell_\alpha=\log P_\alpha$；
2. 每块 (785.11) 的 $D_{\rm ht}$ 个真实高度参数，
   保留所有非 $p$ 局部贡献；
3. 同一原 $P_Y(c_1)$ 与原切向量的两列 (785.19)；
4. 同一原 Poincaré/截面求值的
   $\lambda_{i,0},\lambda_{i,1}$，以及原 Abel 的 $T_i$。

实际需要判定的中心量只有 $r-1$ 个 $\varepsilon_i$，
但这些数尚未生成；此处的“最少”指 (785.25) 中的准确商空间坐标，
不是宣称每项算法成本已最优。

Rosati 关系对任意
$\mathfrak c_\alpha=\mathfrak c_\alpha^*$
都允许 (785.12) 这样的对称配对，因而它本身不给这些数非零、
赋值上界或单位性。实 Néron–Tate 正定性也不给这个
$\mathbb Q_p$-值配对一个序或符号。
此外，原 $F^0=\ker\operatorname{Tr}(\kappa\,\cdot)$
中的非零 $h$ 不可能全正，所以不能把这族次数零线丛直接当作
正定实高度的一族正方向。

本结果提供统一于 $p$ 的结构压缩和一个真正 splitting 不变的首项对象，
未证明其对全部充分大 $p$ 非零，未给其相对尾所需统一赋值控制，
也未证明原完整 Bézout 证书存在。Serre 主目标仍开放。

## 来源与核对范围

- [R724](R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md)
  §§2–6：原 $Y$ splitting 抵消、活跃 GL₂ 型块、真实 Poincaré 规范及因子 $2$。
- [R596](R596-fixed-Chow-Heegner-class-log-factorization.md)：
  原 $\eta_h$ 的活跃部分、秩与对数同构。
- [R634](R634-CM-calibration-eliminates-actual-height-matrix.md)、
  [R699](R699-actual-height-finite-jets-and-complete-exterior-tail.md)：
  实际加权迹坐标、外积、允许的 $A$ splitting 变更。
- Besser–Müller–Srinivasan，
  *p-adic adelic metrics and Quadratic Chabauty I*，
  [arXiv:2112.03873v4](https://arxiv.org/html/2112.03873v4)，
  Proposition 4.30 与 Lemma 4.37：
  原点两轴刚性化及相同曲率确定 Poincaré log。
  本文的同态相容性按这个唯一性逐项核对，
  没有援引任意阿贝尔簇与其他高度理论尚未证明的比较。
