# R302 — 新 j=0 的原 degree 2 参考、六点 Kronecker 常数与完整全权平方

日期：2026-11-13。**状态：以下 $E_1:y^2=x^3+1$ 的原 Hecke/Schwartz 数据、Hermitian 类、真实 degree 2 来源、全部有限与无穷范数、精确中央值、全权平方以及回到 $E_{17}$ 的固定尺度均已证明。没有任取一个 theta 幂作为参考，也没有用 BSD 或数值认数决定常数。**

本篇给 R290–R301 新曲线路线需要的实际秩零参考。固定
$$
K=\mathbf Q(\delta),\quad \delta^2=-3,\quad
\omega=(-1+\delta)/2,\quad s=(1-\omega)^{-1}=(3+\delta)/6.
$$
令 $\Omega_1>0$ 是 $E_1$ 在微分 $dz=dx/(2y)$ 下的 primitive 实周期，
$$
\operatorname{Per}(E_1,dz)=\Omega_1(\mathbf Z+s\mathbf Z)
=\varpi\mathcal O_K,\qquad \varpi=s\Omega_1.
\tag{1}
$$

## 1. 准确结论

在 $x=z^{-2}+\cdots,y=-z^{-3}+\cdots,\sigma=z+\cdots$ 的规范下，原参考是
$$
\boxed{\Theta(z)=x(z)\sigma(z)^2=\sum_{m\ge0}r_mz^m,\qquad
r_0=1,\quad r_6=-\frac2{15},\quad r_m=0\quad(6\nmid m).}
\tag{2}
$$
记 $\psi_1$ 为本曲线取解析微分 CM type 的实际 Hecke 角色。
对每个 $m\ge0$、$6\mid m$，完整的实周期公式为
$$
\boxed{
\frac{(2\pi/\sqrt3)^m L(\psi_1^{\,2m+1},m+1)}
{m!\Omega_1^{\,2m+1}}
=\frac16\,6^{-m}r_m^2.}
\tag{3}
$$
换成实际 CM 生成周期 $\varpi$ 后，中央常数与权尺度同时变化：
$$
\boxed{
\frac{(2\pi/\sqrt3)^m L(\psi_1^{\,2m+1},m+1)}
{m!\varpi^{\,2m+1}}
=\frac{1-\omega}{6}\,2^{-m}r_m^2.}
\tag{4}
$$
特别地，
$$
\boxed{L(E_1,1)/\Omega_1=1/6,\qquad
L(E_1,1)/\varpi=(1-\omega)/6.}
\tag{5}
$$
这是一个实际实来源的平方，不是两条独立共轭 Mellin 的乘积。

## 2. 完整 Hecke 角色与 Hermitian 类

因为 $h_K=1$ 且
$\mu_6\longrightarrow(\mathcal O_K/(2\delta))^\times$ 是同构，
素于 $2\delta$ 的每个理想有唯一生成元 $a\equiv1\bmod2\delta$，
并且 $\psi_1((a))=a$。对任意素于 $2\delta$ 的生成元，
$$
\psi_1((a))=a\varepsilon_1(a)^{-1},\qquad
\varepsilon_1(a)=\chi_{1,2}(a)\chi_{1,3}(a).
\tag{6}
$$
原单位化 idèle 角色 $\chi_1=\psi_1|\cdot|_K^{-1/2}$ 的坏点分量准确是

| 地方 | 单位角色 | uniformizer |
|---|---|---|
| $2$ | $\chi_{1,2}(u)=\operatorname{Teich}_{\mu_3}(u\bmod2)$ | $\chi_{1,2}(2)=-1$ |
| $3$ | $\chi_{1,3}(u)=u\bmod\delta\in\{\pm1\}$ | $\chi_{1,3}(\delta)=i$ |

无穷处 $\chi_{1,\infty}(z)=(z/|z|)^{-1}$。这与 R290 新曲线在三处
uniformizer 的 $-i$ 不同；原导子是 $(2\delta)$、范数十二，经典 level 为三十六。
这些分量可由 (6) 的主 idèle 积关系直接恢复，亦是 R290 使用的基角色。

加性角色仍固定为
$\psi_{\rm add,\infty}(x)=e^{2\pi ix}$、
$\psi_{\rm add,\ell}(x)=e^{-2\pi i\{x\}_\ell}$，
$\psi_{K,v}=\psi_{\rm add,v}\circ\operatorname{Tr}$。
Yang 的局部条件为
$$
\epsilon\left(\tfrac12,\chi_{1,v},\tfrac12\psi_{K,v}\right)
\chi_{1,v}(\delta)=\epsilon_{K_v/\mathbf Q_v}(\alpha).
\tag{7}
$$
二处的原 $\mathbf F_4$ Gauss 和为 $2$；将加性角色从 $\psi_K$ 改成
$\psi_K/2$ 后，左边为 $+1$。三处剩余 Gauss 和为 $i\sqrt3$，
$\chi_{1,3}(\delta)^2=-1$ 给 epsilon 为 $-i$，再乘
$\chi_{1,3}(\delta)=i$，左边也是 $+1$。其他有限点和无穷点同样为 $+1$。
因此正确的全局 Hermitian 类是
$$
\boxed{\alpha=1.}
\tag{8}
$$
在原 $X=\mathbf Q\delta$ 极化和 Yang 标准基中，
$$
\iota_1(x+y\delta)=
\begin{pmatrix}x&9y\\-y/3&x\end{pmatrix}.
\tag{9}
$$
本篇的全部 Gaussian、有限积分和周期都使用 (9)。

## 3. 两处真正的 Schwartz 向量

### 3.1 二处的原四陪集向量

设
$$
e_b=\mathbf1_{b/2+2\mathbf Z_2},\quad
f_A=e_0-e_2,\quad f_B=e_1+e_3,\quad
t=\frac{1+\sqrt3}{\sqrt2}.
$$
原向量是
$$
\boxed{\phi_{1,2}=f_A+t f_B,\qquad
v_2=(1,t,-1,t),\qquad\|\phi_{1,2}\|^2=3+\sqrt3.}
\tag{10}
$$
这不是只将 R290 的向量保留不验。对
$g_*=(-11+4\delta)/13$ 与 $z_8=e^{\pi i/4}$，
Yang Appendix (A1)–(A3) 的实际 splitting 在 $\alpha=1$ 下给
$$
\mu(\omega)=-\omega^2z_8,\qquad
\mu(g_*)=z_8^{-3},\qquad\mu(-g_*)=-z_8=z_8^{-3}.
$$
在偶列 $(f_A,f_B)$ 上，原 $\omega$ 矩阵仍准确为
$$
\frac{\omega^2}{\sqrt2}
\begin{pmatrix}-z_8&i\\i&iz_8\end{pmatrix},
\qquad
M_\omega\binom1t=\binom1t.
\tag{11}
$$
直接代入 (9)，其 Rao 核在偶函数上有二次系数
$\frac32(u^2-4uv+v^2)$。展开 $v=b/2+2a$ 后，奇数四分之一陪集
按 $f_A,f_B$ 分别相消；余下四个陪集的矩阵项是
$$
\frac{\mu(\omega)}{2\sqrt2}
z_8^{-3(a^2+b^2-4ab)}.
$$
这准确给 (11)。对于 $g_*$，原支撑条件为
$a\equiv3b+2\bmod4$，保留 $\alpha=1$ 的完整相位是
$$
\mu(g_*)\,z_8^{-3(11a^2-26ab+11b^2)/4}.
$$
四个非零相位为 $-1,1,-1,1$，所以完整矩阵为
$$
\begin{pmatrix}0&0&-1&0\\0&1&0&0\\-1&0&0&0\\0&0&0&1\end{pmatrix}.
\tag{12}
$$
它固定 $f_A,f_B$，负生成元的相位也已保留。
$\mu_3,-1,g_*$ 拓扑生成整个 $K_2^1$：其主单位部分经对数为
$4\delta\mathbf Z_2$，而 $\log g_*/(4\delta)$ 是单位。
故 (10) 是整个原环面的不变向量。每个 $e_b$ 的自对偶体积为 $1/2$，
给出所写范数。

也可比较 R290：$\alpha=17$ 与 $\alpha=1$ 属于同一个二进平方类，
且 $17\equiv1\bmod16$，故 splitting 和上述有限相位相同；
这里已经用 $\alpha=1$ 直接计算了这些相位。

### 3.2 三处及所有其余地点

在 (9) 的原极化下，
$$
n((\delta/4)\psi_K)=-2=2(-1).
$$
三处角色导子为一，且 (7) 已付，Yang 1999 Proposition 1.2(1) 的
splitting 差为平凡；Corollary 1.4(1) 的真实 Schrödinger 转模给
$$
\boxed{\phi_{1,3}=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
\|\phi_{1,3}\|^2=3.}
\tag{13}
$$
不能在保持同一 Gaussian 的同时把它换成 $\mathbf1_{\mathbf Z_3}$。
所有其余有限地点，**包括十七处**，使用
$\phi_{1,\ell}=\mathbf1_{\mathbf Z_\ell}$。
好非分裂点用 Yang Lemma 2.7；好分裂点用 Corollary 2.14 的实际极化变换。
因此原 finite norm 是 $3(3+\sqrt3)$。

## 4. 原 Hermite 来源及 degree 2 的唯一识别

令
$$
\kappa_\infty=|\delta^3|=3\sqrt3,\qquad
\sum_{m\ge0}H_m(x)\frac{T^m}{m!}
=\exp(xT-T^2/(8\pi)).
$$
有理支撑准确为 $x=n/6$。在二处 $2x=n/3\equiv3n\bmod4$，
而 $v_2(3n)=v_2(n)$，故实际 Hermite 系数是
$$
b_m^{(1)}=\sum_{n\in\mathbf Z}v_2(n\bmod4)
H_m\left(\frac{\sqrt{3\sqrt3}}6 n\right)
\exp\left(-\frac{\pi\sqrt3}{12}n^2\right).
\tag{14}
$$
它们都是实数。原有限向量在全部地方被 rational $\omega$ 的实际 Weil
作用固定；全球 theta 求和不变性与 Hermite 型给 $3\nmid m$ 时系数零。
偶性另给奇权零，所以
$$\mathcal B_1(T)=\sum b_m^{(1)}T^m/m!\in\mathbf R[[T^6]].\tag{15}$$

写 $\tau_0=\delta/3$，定义
$$
F_1(Z)=\sum_{n\in\mathbf Z}v_2(n\bmod4)
e^{\pi i\tau_0n^2/4+2\pi inZ},\qquad
h_1=\frac{\sqrt{3\sqrt3}}{12\pi i}.
$$
则
$$
\mathcal B_1(T)=e^{-T^2/(8\pi)}F_1(h_1T).
\tag{16}
$$
由原有限恒等式 $v_2(n+2)(-1)^n=-v_2(n)$，逐项换元得到
$$
F_1(Z+1)=F_1(Z),\qquad
F_1(Z+s)=e^{-2\pi is-4\pi iZ}F_1(Z).
\tag{17}
$$
因此矩形模型 degree 四的原来源下降到最大整环格
$\Lambda=\mathbf Z+s\mathbf Z$ 上的 degree 二，线丛为 $\mathcal O(2O)$。
该格的准周期 $\eta_1=2\sqrt3\pi$，所以原 reduced frame 是
$$
\mathcal S_1(Z)=e^{2\sqrt3\pi Z^2}F_1(Z)\in
\sigma_\Lambda^2L(2O),\qquad
2\sqrt3\pi h_1^2=-\frac1{8\pi}.
\tag{18}
$$
全部 Hermite Gaussian 恰好相消，没有余下一个二次指数。

空间 $L(2O)$ 的完整基是 $1,x$。$\sigma^2$ 的 $\omega$ 特征为
$\omega^2$，而 $x\sigma^2$ 的特征为一。由 (15)，实际来源只能在后者
一维线上。又 $F_1$ 的零次 Fourier 系数为一，故它不恒为零。
因此存在固定实数 $C_1\ne0$，使
$$
\boxed{\mathcal B_1(T)=C_1\Theta(\Omega_1h_1T),\qquad
\Theta=x\sigma^2,\qquad C_1=b_0^{(1)}.}
\tag{19}
$$
这证明 (2) 中来源的身份与质量一；没有用低阶数值拟合。
$r_6=-2/15$ 由
$x=z^{-2}-z^4/7+\cdots$、
$\log(\sigma/z)=z^6/210+\cdots$ 直接得到。

## 5. 同一有限来源的全部权与 Yang 范数

全权角色是
$$
\chi_{1,m}=\chi_1^{\,2m+1}.
$$
二处三次单位角色不变要求 $3\mid m$，三处统一化元
$i^{2m+1}=i$ 要求 $m$ 偶。故同一原有限数据的准确公共周期是 $6\mid m$。
好分裂点的未分歧参数虽变化，原标准球保持适用。局部 dichotomy 仍是
同一 $\alpha=1$，无穷处取 (14) 的第 $m$ Hermite 向量。

自对偶测度给原全局向量的范数平方
$$
\mathcal N_m^{(1)}
=\frac{3(3+\sqrt3)}{\sqrt{6\sqrt3}}\frac{m!}{(4\pi)^m}.
\tag{20}
$$
Yang Theorem 1.11 中此时 $S_1=\{2\}$，没有十七处坏位，也没有坏分裂点；
其因子是
$$c(0)=(1+2^{-1})^{-1}=2/3.\tag{21}$$
$h_K=1$ 和原单位群 $\mu_6$ 给“紧子群体积乘积/商体积”为六，故
Theorems 2.6、2.15 的原规范准确给
$$
L(\psi_1^{\,2m+1},m+1)
=\frac2{6c(0)}\frac{\pi}{3\sqrt3}
\frac{(b_m^{(1)})^2}{\mathcal N_m^{(1)}}
=C_{\rm Y}\frac{(4\pi)^m}{m!}(b_m^{(1)})^2,
\tag{22}
$$
其中
$$
\boxed{C_{\rm Y}=\frac{\pi\sqrt{6\sqrt3}}
{18\sqrt3(3+\sqrt3)}>0.}
\tag{23}
$$
这保留了二处范数、三处球的体积、无穷 Hermite 范数、$c(0)$ 和全部单位群。

代入 (19)，并使用
$$
\frac{2\pi}{\sqrt3}\,4\pi h_1^2=-\frac16,\qquad 6\mid m,
$$
得到全权等式
$$
\frac{(2\pi/\sqrt3)^mL(\psi_1^{\,2m+1},m+1)}
{m!\Omega_1^{\,2m+1}}
=\frac{C_{\rm Y}C_1^2}{\Omega_1}\,6^{-m}r_m^2.
\tag{24}
$$
剩下的整体常数由下一节的准确 $m=0$ 原 ray 和支付。

## 6. 六个原导子点完整确定中央常数

置 $\Gamma_1=\varpi\mathcal O_K$、
$A=\operatorname{area}(\mathbf C/\Gamma_1)/\pi$，并记
$$
\xi(z)=\zeta(z)-\bar z/A.
$$
在此三次 CM 格上 reduced theta 就是 $\sigma$。
Bannai–Kobayashi 的 Kronecker 展开 Theorem 1.17 在 $(a,b)=(0,1)$
给出 $e_{0,1}^*(Q,0)=\xi(Q)$，亦即原
$$
e^{-\bar Qw/A}\frac{\sigma(Q+z+w)}{\sigma(Q+z)\sigma(w)}
$$
的 $z^0w^0$ 系数。这一固定公式包含反全纯修正，不能只用裸 $\zeta$ 值。

设
$$
f_1=2\delta,\qquad Q=\varpi/f_1.
$$
实际分支给
$$
\boxed{Q=(2\omega,3),\qquad \xi(Q)=-\omega^2.}
\tag{25}
$$
以下完全代数地核定所需分支和值。$2Q\equiv2\Omega_1/3$，
所以 $2Q=(0,1)$；$\delta Q=\Omega_1s/2$ 的横坐标是 $-\omega$。
点 $(2\omega,3)$ 满足这些条件；也可写成
$$Q=(-\omega,0)+(0,-1).$$
第一加点是二挠点，由 $\xi$ 的奇性、周期性得其值零；
第二加点由三次 CM 固定，由 $\xi(\omega z)=\omega^{-1}\xi(z)$ 得其值零。
原 zeta 加法式于是给
$$
\xi(Q)=\frac{0-(-1)}{-\omega-0}=-\omega^2.
$$
全部 primitive $f_1$ 点正是 $uQ$，$u\in\mu_6$，而
$\xi(uQ)=u^{-1}\xi(Q)$。

现在使用原 Hecke 角色 (6)。对理想取复共轭后，其完整格和是
$$
L(\psi_1,1)=\frac16
\sum_{\substack{a\ne0\\(a,f_1)=1}}^{*}\frac{\varepsilon_1(a)}a.
\tag{26}
$$
星号表示 Eisenstein–Kronecker 解析延拓。按 $a\bmod f_1$ 的有限陪集
分解先在绝对收敛的加权和中作，再继续至该点；不是重新排列条件收敛级数。
由于 $(\mathcal O_K/f_1)^\times$ 的六个代表可取 $u\in\mu_6$，
$\varepsilon_1(u)=u$，(26) 准确化为
$$
\frac{L(\psi_1,1)}{\varpi}
=\frac1{6f_1}\sum_{u\in\mu_6}u\,\xi(uQ)
=\frac{\xi(Q)}{f_1}
=-\frac{\omega^2}{2\delta}
=\frac{1-\omega}{6}.
\tag{27}
$$
乘 $s=\varpi/\Omega_1$ 得实值 $1/6$。这证明 (5)，也把 (24) 中的固定
常数准确确定为 $C_{\rm Y}C_1^2/\Omega_1=1/6$，所以 (3) 得证。
$s^2=-\omega^2/3$、$s^{2m}=3^{-m}$ 对 $6\mid m$ 成立；换周期给 (4)。

式 (5) 特别给 $L(E_1,1)>0$。因此已发表的 CM rank-zero 定理
（Coates–Wiles）给 $\operatorname{rank}E_1(\mathbf Q)=0$。
该已知定理只用于给参考命名；(2)–(5) 的值与常数均已由以上原公式独立计算。

## 7. 回到实际 $E_{17}$ frame 时保留六次尺度

取固定正实 $\theta=17^{1/6}$。同构
$(X,Y)\mapsto(\theta^2X,\theta^3Y)$ 将 $E_1$ 映到 $E_{17}$，微分乘
$\theta^{-1}$。因此
$$
\Omega_{17}=\Omega_1/\theta,\quad
x_{17}(z)=\theta^2x_1(\theta z),\quad
\sigma_{17}(z)=\theta^{-1}\sigma_1(\theta z).
$$
真正的共同 frame 参考是
$$
\boxed{\Theta_{17}(z)=x_{17}(z)\sigma_{17}(z)^2
=\Theta_1(\theta z),\qquad
r_{m,17}=\theta^mr_m.}
\tag{28}
$$
因为只出现 $6\mid m$，其系数仍有理，$r_{m,17}=17^{m/6}r_m$。
但在复周期规范中，整体 $\theta$ 不能删去：
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\psi_1^{\,2m+1},m+1)}
{m!\Omega_{17}^{\,2m+1}}
=\frac{\theta}{6}\,6^{-m}r_{m,17}^2,}
\tag{29}
$$
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\psi_1^{\,2m+1},m+1)}
{m!(s\Omega_{17})^{\,2m+1}}
=\frac{\theta(1-\omega)}{6}\,2^{-m}r_{m,17}^2.}
\tag{30}
$$
因此与 R298 的原新来源 $S=\sum s_mz^m$ 比较，可无除零地写成
$$
\boxed{
L(\psi_{17}^{\,2m+1},m+1)\,r_{m,17}^2
=\frac{6\kappa_0}{\theta}\,17^{-m}
L(\psi_1^{\,2m+1},m+1)\,s_m^2,\quad 6\mid m,
}
\tag{31}
$$
$\kappa_0=48940416$。式 (31) 未假设每个参考系数 $r_m$ 都非零。
在后续 ordinary 或高度二 Mellin 中，$\theta$ 的嵌入、固定单位缩放、
参考质量与自己的 Euler 因子仍须按原规范保留。

## 8. 证书与出处

[精确脚本](../scripts/check-jzero-original-degree-two-reference.py) 和
[数据](../scripts/check-jzero-original-degree-two-reference.json)
在 $\mathbf Q(\zeta_{24})$ 中直接核 $\alpha=1$ 的原二处矩阵、
完整六点的加法与 reduced zeta 值，并精确检查所有 Gaussian、范数和周期
常数。没有任何数值 L 值或拟合步骤。

1. T. Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew. Math. **485** (1997), 25–53，Theorem 1.11、Corollary 2.14、Theorems 2.6、2.15；[作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
2. T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*, Compositio Math. **117** (1999), 337–359，Lemma 1.1、Proposition 1.2(1)、Corollary 1.4(1)、Appendix (A1)–(A3)；[作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
3. K. Bannai, S. Kobayashi, *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*, Duke Math. J. **153** (2010), 229–295，Theorem 1.17；[作者稿](https://arxiv.org/pdf/math/0610163)，DOI 10.1215/00127094-2010-024。
4. J. Coates, A. Wiles, *On the conjecture of Birch and Swinnerton-Dyer*, Invent. Math. **39** (1977), 223–251；[出版记录](https://doi.org/10.1007/BF01402975)。
5. [R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)、[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、[R298](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md) 固定新曲线的原来源与尺度；本篇在同一极化下完整支付其基曲线参考。
