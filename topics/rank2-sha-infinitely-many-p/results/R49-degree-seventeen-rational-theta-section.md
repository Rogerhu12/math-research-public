# R49. 次数十七的有理 theta 截面与同一个中心斜率

日期：2026-11-12。**状态：已证明；跨素数的斜率非零仍未证明。**

## 1. 定理

固定 $E:y^2=x^3-17x$、$\Gamma=\Omega_E\mathbb Z[i]$、
$f=34(1+i)$、$Nf=2312$。令 $T_0=(1+i)\Omega_E/2$ 对应 $(0,0)$，
并定义
$$
\vartheta(z)=e^{-\zeta(T_0)z}\frac{\sigma(z+T_0)}{\sigma(T_0)}.
$$
存在固定有理数 $u_2,u_3,u_4$，使同一个实际 theta 因子可以归一为
$$
\boxed{
A_{\mathbb Q}(z)=\vartheta(z)\sigma(z)^{16}
 \bigl(x(z)^6+u_2x(z)^4+u_3x(z)^2+u_4\bigr)
 =\sum_m b_mz^m\in z^4\mathbb Q[[z^4]],\qquad b_4=1.
}
\tag{1}
$$
它是次数十七的 theta 截面。存在固定正有理数
$$
\kappa_{\mathbb Q}=e_4(17Nf)^4
$$
使
$$
\boxed{e_m=\kappa_{\mathbb Q}(17Nf)^{-m}b_m^2\qquad(4\mid m).}
\tag{2}
$$

对全部 R48 所列目标普通素数 $p$，其实际有界测度满足
$$
\int_{\mathbb Z_p}x^m\,d\mu_p=\Omega_p^m m!b_m.
$$
记其单位限制的 principal Mellin 变换为 $J_p$，则完整分支准确为
$$
\boxed{
F_p^{\Theta,-}(T)=\kappa_{\mathbb Q}f\Omega_p
 (1+T)^{\log_p\langle136\rangle/\log_p(1+p)}J_p(T)^2.
}
\tag{3}
$$
因此
$$
\boxed{
J_p(0)=0,\qquad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}\iff J_p'(0)\ne0.
}
\tag{4}
$$
非零常数即使在某个 $p$ 处不是单位，也不改变此零阶判据。

这里证明三个有理参数的存在及准确构造。后续
[R51](R51-explicit-theta-section-and-central-square-constant.md)
已用全局唯一重构和严格包含区间确定其准确值；
(4) 对无穷多个 $p$ 成立仍须证明。

## 2. 固定 dyadic 向量及尺度

[dyadic 完整计算](../notes/2026-11-12-dyadic-vector-and-reference-theta.md)
直接使用 Yang 的标准 splitting 和 Rao 核。两个元素
$$
i,\qquad g=(-3+4i)/5
$$
拓扑生成 $\mathbb Q_2(i)^1$：其 pro-$2$ 部分的对数为
$4i\mathbb Z_2$，而 $\log g$ 生成此格。

在 $\mathbf1_{\mathbb Z_2}$ 上，$i$ 的 splitting 与 Fourier 总标量为一；
$g$ 的 splitting 是 $-\zeta_8^{-1}$，Rao 核的 Gauss 积分为
$\zeta_8^{-3}$，乘积仍为一，且核在 $\mathbb Q_2\setminus\mathbb Z_2$
上为零。因此 R46 的同一平凡等型线可取 $\mathbf1_{\mathbb Z_2}$。
这一步没有把奇剩余特征的公式外推到 $2$。

$17$ 处的有限向量支撑于 $17^{-1}\mathbb Z_{17}$，
在 $17\mathbb Z_{17}$ 平移下不变。其余处为未分歧向量。
所以偶尺度可明确取 $L=34$，R46 给次数 $d=1156$ 的截面 $S_{34}$。
同一有限向量也容许奇尺度 $L=17$；$L=34$ 的枚举只有偶指标，
两种枚举给同一个 Hermite 生成函数，而且 $c_{34}=2c_{17}$。
因此
$$
S_{17}(z)=S_{34}(z/2)
\tag{5}
$$
仍具有已证的代数系数及实结构，不需重新选择一个不相干的 theta 向量。

## 3. 保留半特征的十七次下降

sigma 加法式与半周期准周期式给
$$
\vartheta^2=x\sigma^2,\qquad\vartheta(0)=1,\qquad
\vartheta(iz)=\vartheta(z).
\tag{6}
$$
因此 $\vartheta$ 的 Taylor 系数有理。对
$\lambda=\Omega_E(r+si)$，其完整半特征是
$$
\chi_T(\lambda)=(-1)^{rs},\qquad
\vartheta(z+\lambda)=\chi_T(\lambda)
 \exp\!\left(\frac{\bar\lambda}{A}(z+\lambda/2)\right)\vartheta(z),
\quad A=\Omega_E^2/\pi_{\mathbb C}.
\tag{7}
$$
不能把两生成元上均为正号误写成一般周期没有半特征。

取 $N\varpi=17$，$q=\varpi/\bar\varpi$。
R48 给 $\bar S_{17}(z)=S_{17}(q^{-1}z)$。
其两份准周期格生成
$$
\Gamma+q^{-1}\Gamma=\varpi^{-1}\Gamma.
$$
在该格上，准确乘子是
$$
\widetilde J_{\lambda'}(z)=
 \chi_T(\varpi\lambda')
 \exp\!\left(\frac{17^2}{A}\bar\lambda'(z+\lambda'/2)\right).
\tag{8}
$$
将 $\lambda'=\lambda/\varpi,z=w/\varpi$ 代入，(8) 正是
$\vartheta(w)^{17}$ 的 cocycle。又 $\varpi,\bar\varpi$ 模 $2$
只交换两个坐标或保持它们，故均保持 $\chi_T$。
所以 (8) 在两份原格上的限制都与已知乘子一致；这核清全部交叉符号。

于是
$$
A_{17}(z)=S_{34}(z/(2\varpi))
$$
是与 $\vartheta^{17}$ 同乘子的、$[i]$-不变的实代数截面。
商 $A_{17}/\vartheta^{17}$ 是椭圆函数，唯一可能的极点在 $T_0$，
阶至多十七。$1/x^2$ 是 $E/\mu_4$ 上以 $T_0$ 为唯一极点的坐标，
该处极点阶为四，故
$$
A_{17}=\vartheta^{17}Q(x^{-2}),\qquad \deg Q\le4.
$$
$A_{17}(0)=0$ 又给 $Q(0)=0$。用 (6) 即得 (1) 的四个实代数系数版本。

## 4. 有限平方矩迫使所有参数同时有理

实际 $e_4\ne0$ 已由完整 $7$ 进轨道证书证明，故首系数 $c_1\ne0$。
将 $A_{17}$ 除以 $c_1$，记系数向量为 $u=(1,u_2,u_3,u_4)$。
令
$$
r_{nj}=[z^{4n}]\bigl(\vartheta\sigma^{16}x^{8-2j}\bigr)\in\mathbb Q.
$$
R46 的范数公式及上述实下降给
$$
(r_nu)^2=\frac{e_{4n}}{e_4}(17Nf)^{4n-4}\in\mathbb Q.
\tag{9}
$$
这里不能逐项为平方根选择 Galois 符号。

取 $n=1,\ldots,10$，十列对应
$11,12,13,14,22,23,24,33,34,44$，
对角列为 $r_{ni}^2$，非对角列为 $2r_{ni}r_{nj}$。
[精确递推和行列式证明](../notes/2026-11-12-theta-four-parameter-rationality.md)
在 $\mathbb Q$ 上求全部系数，再模 $101$ 检验，给
$$
\det M_{D=1}=56\bmod101,\qquad
\det M_{D=17}=17^{60}\det M_{D=1}=56\bmod101.
\tag{10}
$$
全部分母均为 $101$ 单位。因此有理行列式非零。
(9) 的十个有理值遂唯一确定 $uu^{\mathsf t}$ 的全部坐标为有理数；
因 $u_1=1$，第一行给 $u_2,u_3,u_4\in\mathbb Q$。
这同时证明全部 Taylor 系数有理和
$\kappa_{\mathbb Q}=e_4(17Nf)^4\in\mathbb Q_{>0}$。

复算脚本
[check-theta-four-parameter-rigidity.py](../scripts/check-theta-four-parameter-rigidity.py)
仅使用标准库 Fraction；根端已独立运行并核对上述两个行列式及全部尺度关系。

## 5. Mellin 参数未改变

R46 的 $S_{34}$ 与新 $A_{17}$ 的系数相差 $(2\varpi)^m$；
因此范数相差 $68^m$，次数由 $1156$ 变成 $17$。
这正给 (2)，没有遗漏阶乘。

普通处 $2\varpi$ 是单位，两个实际测度由乘 $2\varpi$ 的推前关联。
将该推前代入 R48 的整条平方恒等式，指数准确变成
$$
\log_p\langle f^2/17\rangle/\log_p(1+p)
 =\log_p\langle136\rangle/\log_p(1+p),
$$
因为 $f^2/17=136i$，$i$ 为 Teichmüller 单位。
固定标量 $c_1$ 的归一又把 $\kappa$ 改成 $\kappa_{\mathbb Q}$。
于是得到 (3)；R40 给 (4)。

### 全文与来源

- [十七次同源下降及奇半特征全文](../notes/2026-11-12-theta-seventeen-isogeny-descent.md)。
- [有理四参数及精确证书](../notes/2026-11-12-theta-four-parameter-rationality.md)。
- [dyadic 标量与参考 theta](../notes/2026-11-12-dyadic-vector-and-reference-theta.md)。
- T. Yang, *Theta liftings and Hecke L-functions* (1997)，Corollary 2.4、
  (2.28)；*Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves* (1999)，Appendix (A1)–(A3)：准确局部 Weil 规范。
- R46、R48 提供同一实际因子及实结构；R40 提供完整 Selmer 零阶判据。
