# R332：固定负矩的真实 Soulé 类、完整局部对数与反射中心的负号

日期：2026-11-13。**状态：以下原 $\Theta$ 负六次矩、原 $\sigma$ 负五次矩的完整 tame 平方、实际全局椭圆单位类、局部 Bloch–Kato 对数及其准确赋值、另一普通素位的零局部化、反射复中心的负号均已证明。局部比较由已发表的 Yager／de Shalit／Venjakob 输入在本文专门推导，不把 2026 年新预印本直接作为未付结论。固定两矩的非零尚未证明；权随 $p$ 变化的单位矩不计为固定权或主目标的无穷素数结论。**

## 1. 同一个原测度、CM type 和两条负权

固定 $K=\mathbf Q(\sqrt{-3})$、$\omega=(-1+\sqrt{-3})/2$，
$E_0:y^2=x^3+1$ 的实际 Hecke 字符记为 $\psi_0$。
其导子为 $(2\sqrt{-3})$，不是原秩二曲线 $E_{17}$ 的导子。
置 $\theta=17^{1/6}>0$，并固定原普通嵌入。以下
$p>7$、$p\equiv1\pmod3$，所以 $p\ge13$。

仍沿 R316 的同一形式群同构和微分，取
$$
\Omega_0=\Omega_{p,0}=\theta\Omega_p,\qquad
\pi_0=\psi_0(\mathfrak p),\quad
\bar\pi_0=\psi_0(\bar{\mathfrak p}),\quad
\pi_0\bar\pi_0=p,
\tag{1}
$$
其中 $v_p(\pi_0)=1$、$v_p(\bar\pi_0)=0$，$\Omega_0$ 为单位。
不要将 $\Omega_0$ 与 $E_{17}$ 的 $\Omega_p$ 混为同一个符号。

R302、R316 给出的实际 Amice 变换满足
$$
\Theta_{17}(\Omega_p\log(1+Z))
 =\Theta_0(\Omega_0\log(1+Z)),
$$
$$
\sigma_{17}(\Omega_p\log(1+Z))
 =\theta^{-1}\sigma_0(\Omega_0\log(1+Z)).
\tag{2}
$$
故其单位测度准确满足
$$
\nu_{\Theta,17}^{\times}=\nu_{\Theta,0}^{\times},\qquad
\nu_{\sigma,0}^{\times}=\theta\nu_{\sigma,17}^{\times}.
\tag{3}
$$
这由形式群同构给出，不是在 $\mathbf Z_p$ 上任意乘一个代数数。
定义
$$
I_\Theta=\int_{\mathbf Z_p^\times}x^{-6}\,d\nu_{\Theta,17}(x),\qquad
I_\sigma=\int_{\mathbf Z_p^\times}x^{-5}\,d\nu_{\sigma,17}(x),\qquad
I_{\sigma,0}=\theta I_\sigma.
\tag{4}
$$
它们分别是 R330 深区和原六 sigma 深区所读的固定负矩。
在 tame 记号下，$x^{-6}=\tau(x)^{-6}\langle x\rangle^{-6}$，
$x^{-5}=\tau(x)^{-5}\langle x\rangle^{-5}$；不能把它们换成 principal 零权质量。

记
$$
\chi_r=\psi_0^{1-r}\bar\psi_0^r,\qquad
V_r=\mathbf Q_p(1)\otimes\chi_r^{-1}
 =\mathbf Q_p(\psi_0^r\bar\psi_0^{1-r}).
\tag{5}
$$
负六次对应 $r=6$、$\chi_6$ 的 type 为 $(-5,6)$；
负五次对应 $r=5$、$\chi_5$ 的 type 为 $(-4,5)$。
两者都满足 $\chi_r\chi_r^c=\mathrm N$。

## 2. 真正全 tame 的平方，含全部固定尺度

令 $\mathcal L_{\mathfrak f}$ 是采用 R295 晶格周期规范的 Katz 测度；
此处下标表示固定的模数，因而包含该模数要求删除的坏 Euler 因子。
当字符原导子即为该模数时写 $\mathcal L^{\rm prim}$。
R302 的全权常数及 R316 的 sigma 全权常数分别是
$$
c_\Theta=\frac{1-\omega}{6},\qquad
c_\sigma=-\frac{\omega(1-\omega)}9.
\tag{6}
$$
对合法非负整数 $m$，置
$\epsilon_m=\psi_0^{m+1}\bar\psi_0^{-m}$。
用原 Euler 因子及同一 $\Omega_0$，实际正权平方为
$$
\epsilon_m(\mathcal L^{\rm prim})
 =c_\Theta\Omega_0\,2^{-m}
 \left(\int_{\mathbf Z_p^\times}x^m\,d\nu_{\Theta,0}\right)^2,
 \qquad m\equiv0\pmod6,
\tag{7}
$$
$$
\epsilon_m(\mathcal L^{\rm prim})
 =c_\sigma\Omega_0
 \left(\int_{\mathbf Z_p^\times}x^m\,d\nu_{\sigma,0}\right)^2,
 \qquad m\equiv1\pmod6.
\tag{8}
$$
这两式分别来自 R302 (4)、R316 (20)，以及已付的完整 $p$-core。
两个阶乘分别来自 Katz 插值和 Yang 平方；恰好组成实际单位矩的平方。

**负权延拓的证明。** 固定任一合法负整数 $m$，令
$$m_a=m+(p-1)p^a.$$
当 $a$ 大时它非负、保持合法的模六型，也保持同一个 tame 分支。
其对应 $p$ 进角色趋于 $\epsilon_m$。整单位测度使右侧矩趋于
$\int x^m d\nu$，而 $2^{-m_a}\to2^{-m}$。
所有变化的 $\Omega_0^{2m_a}$ 已在 (7)–(8) 的矩平方中准确约去；
这里没有对一个任意 $\mathbf C_p$ 单位的变指数周期取未经支付的极限。
Katz 测度的连续性即给所需延拓。

特别地，实际两个点满足
$$
\boxed{\chi_6(\mathcal L_{2\sqrt{-3}})
 =\frac{32}{3}(1-\omega)\Omega_0 I_\Theta^2,}
\tag{9}
$$
$$
\boxed{\chi_5(\mathcal L^{\rm prim}_{\sqrt{-3}})
 =-\frac{\omega(1-\omega)}9\Omega_0 I_{\sigma,0}^2
 =-\frac{\omega(1-\omega)}9\theta^3\Omega_p I_\sigma^2.}
\tag{10}
$$
因子 $2^6=64$、$\theta$、$\theta^3$ 均不能删除。

### 2.1 sigma 必须保留的二处 Euler 因子

$\chi_6$ 的原导子为 $2\sqrt{-3}$，但 $\chi_5$ 的原导子只有
$\sqrt{-3}$。在整个 sigma 支 $m\equiv1\pmod6$，二处单位角色平凡，
uniformizer 的单位化值为 $-1$。其代数字符为 norm-weight one，故
$$
\epsilon_m((2))=-2,\qquad
1-\epsilon_m^{-1}((2))=\frac32.
\tag{11}
$$
这是在 $K$ 的惰性二处，$\mathrm N(2)=4$；不能误用 $\mathrm N(2)=2$。
所以从 $E_0$ 全模数 $2\sqrt{-3}$ 取得的 Katz 值是
$$
\boxed{\chi_5(\mathcal L_{2\sqrt{-3}})
 =\frac32\chi_5(\mathcal L^{\rm prim}_{\sqrt{-3}}).}
\tag{12}
$$
整个支上这个因子为固定的 $3/2$，不藏有权导数或 $p$ 进非单位。

## 3. 反射后的两个复中心准确为负号

正确反射出的经典字符为
$$
\varphi_r=\chi_r^c=\psi_0^r\bar\psi_0^{1-r}
 =\psi_0^{2r-1}\mathrm N^{1-r}.
\tag{13}
$$
因此两个复中心分别是 $L(\psi_0^{11},6)$ 和 $L(\psi_0^9,5)$。
以下给出本地规范内的符号证明，不据零系数或数值猜测根数。

令 $\vartheta=\psi_0\mathrm N^{-1/2}$ 为单位化 Hecke 字符。
R302 §2 支付了其完整坏局部分量：

| 地方 | 单位群上的角色 | uniformizer 值 |
|---|---|---|
| $2$ | 三次 Teichmüller 角色 | $\vartheta_2(2)=-1$ |
| $3$ | 二次角色 | $\vartheta_3(\sqrt{-3})=i$ |

所以 $\vartheta^{11}$ 与 $\vartheta^{-1}$ 在两个坏点的**完整**局部字符相同，
$\vartheta^9$ 与 $\vartheta^{-3}$ 也相同：这里用的是指数相差十二，
不只是单位角色上的模六一致。所有其他有限点字符未分歧，标准加性角色也未分歧，
其局部 epsilon 均为一。

无穷处复局部 Fourier–Gaussian 计算给绝对角权 $a$ 的 epsilon
为 $i^{|a|}$ 或其共轭，取决于统一的 Fourier 符号。
两种约定对本比较给相同结果：
$$
\frac{\epsilon_\infty(\vartheta^{11})}
     {\epsilon_\infty(\vartheta^{-1})}=i^{10}=-1,
\qquad
\frac{\epsilon_\infty(\vartheta^9)}
     {\epsilon_\infty(\vartheta^{-3})}=i^6=-1.
\tag{14}
$$
可直接对复 Gaussian 乘 $z^{|a|}$ 做 Fourier 变换得到此式，
每增加一个角次数乘 $\pm i$；本处增加十或六，均乘负一。

原角色和其复共轭有相同全球 $L$ 函数。
R302 已完整算出 $L(\psi_0,1)>0$；R316 的第一 sigma 权完整算出
$L(\psi_0^3,2)>0$。因而比较用的两条复函数根数均为 $+1$。
(14) 及全部有限点相同遂给
$$
\boxed{W(\psi_0^{11})=W(\psi_0^9)=-1,\qquad
L(\psi_0^{11},6)=L(\psi_0^9,5)=0.}
\tag{15}
$$

同一证明还给每个 $n\ge1$
$$
\boxed{L(\psi_0^{12n-1},6n)=0,\qquad
L(\psi_0^{12n-3},6n-1)=0.}
\tag{16}
$$
它不推出 (9)–(10) 中的 $p$ 进值为零。

## 4. 来自实际全局椭圆单位的两个类

取 $K_n=K(E_0[p^n])$、$K_\infty=\bigcup K_n$，
$\Gamma=\operatorname{Gal}(K_\infty/K)$，并令 $\Sigma$ 包含 $p$、$2$、$3$ 和无穷位。
取原辅助理想 $\mathfrak a=(5)$。令
$$
u_\infty=({}_{\mathfrak a}z_n)_n
 \in\varprojlim_n\mathcal O_{K_n,\Sigma}^{\times}\widehat\otimes\mathbf Z_p
 \subset H^1_{\rm Iw}(K_\infty/K,\mathbf Z_p(1))
\tag{17}
$$
为 Yager／Kato 规范的 norm-compatible 椭圆单位：先在 ray class 塔
$K(p^n2\sqrt{-3})$ 构造，再取到 $K_n$ 的实际范数。
固定符号为
$$
\operatorname{Col}_{\mathfrak p}(\operatorname{loc}_{\mathfrak p}u_\infty)
 =(\mathrm N\mathfrak a-\sigma_{\mathfrak a})\mathcal L_{2\sqrt{-3}}.
\tag{18}
$$
若用 $\sigma_{\mathfrak a}-\mathrm N\mathfrak a$ 的平滑约定，须同时取椭圆单位的逆；
本篇固定 (18)，所以不把原 $-30$ 平滑值误放进下面的类。

选取相容 Tate 基 $\eta\in T_{\pi_0}E_0$ 与
$\eta^{\rm cyc}\in\mathbf Z_p(1)$，使形式周期为 (1)。定义
$$
T_r=\mathbf Z_p(1)\otimes\chi_r^{-1},\qquad
\eta_r=\eta^{\otimes(2r-1)}\otimes
             (\eta^{\rm cyc})^{\otimes(1-r)}\in T_r.
\tag{19}
$$
在 $K_\infty$ 上用 $(\eta^{\rm cyc})^{-1}\otimes\eta_r$ 杯积扭曲，
再由 Iwasawa 上同调降至 $K$，得到
$$
u_r=\operatorname{pr}_K(\operatorname{tw}_{\chi_r}u_\infty)
 \in H^1(\mathcal O_{K,\Sigma},T_r).
\tag{20}
$$
由于 $\psi_0((5))=\bar\psi_0((5))=-5$、$\mathrm N(5)=25$，
$$\mathrm N\mathfrak a-\chi_r(\mathfrak a)=25-(-5)=30.$$
置
$$
z_r^{(2\sqrt{-3})}=\frac1{30}u_r,\qquad
\boxed{z_6=z_6^{(2\sqrt{-3})},\quad
z_5^{\rm prim}=\frac23 z_5^{(2\sqrt{-3})}=\frac1{45}u_5.}
\tag{21}
$$
所有这些除数在当前素数均为单位。sigma 的 $2/3$ 正是 (12) 的原 Euler 归一，
也可由删除二处导子的椭圆单位范数关系 $1-\sigma_2^{-1}$ 得到。
类 (21) 真实来自原全局单位，未以局部对数的逆像代替全局构造。

## 5. 已发表局部输入的专门推导

下面只用三个已发表输入：Yager 的实际 Coleman 像 (18)；
de Shalit 的 Lubin–Tate／乘法 Coleman 比较；
Venjakob 2013 Theorem 2.13 的 rank-one epsilon 下降。
本节将所需特殊化及其符号、周期、Euler 全部计算出来。

### 5.1 Coleman 规范及比较

对局部 norm-compatible 单位 $u$，其 Coleman 级数 $g_u$ 给
$(1-\varphi/p)\log g_u$，经 Mellin 变换及全部不分歧共轭的规范迹得到
$\operatorname{Col}(u)$。不分歧迹中使用 $\sigma^{-1}$ 作为群环标号。
de Shalit, Proposition I.3.9 的比较允许在最大不分歧扩张上把原
$\widehat E_0$ 换成 $\widehat{\mathbf G}_m$，保持这一 Coleman 图。
这是同一局部单位塔的比较，不是假定两种形式坐标的导数相等。

设 $\Lambda=\mathbf Z_p[[\Gamma_{\mathfrak p}]]$，
$\mathbb T=\mathbf Z_p(1)\otimes\Lambda^{\iota}$。
在去掉两个平凡特征的泛型分量后，Kummer 与局部 Euler 特征把
rank-one epsilon 元素看成从 $H^1$ 到
$\widehat{\mathbf Q}_p^{\rm ur}\otimes\mathbb T$ 的线性泛函。
Venjakob 的构造使用负 Coleman 及 $-\eta^{\rm cyc}$；
结合该文 Proposition 2.12 的变基因子，换回这里固定的正 Coleman 时，
特征为 $\nu$ 的特殊化保留因子 $-\nu(\sigma_{-1})$。
这同时说明不能凭“相差一个单位”删去本篇的最终正负号。

### 5.2 对 $V_r$ 逐项特殊化

在 $K_{\mathfrak p}=\mathbf Q_p$ 上有
$$
V_r=\mathbf Q_p(r)\otimes\bar\psi_0^{1-2r},
\tag{22}
$$
其中第二项未分歧，算术 Frobenius 值为 $\bar\pi_0^{1-2r}$。
令
$$
q_r=\frac{\bar\pi_0^{r-1}}{\pi_0^r},\qquad
a_r=\frac{\pi_0^{r-1}}{\bar\pi_0^r}.
\tag{23}
$$
其 $D_{\rm cris}$ 的 Frobenius 标量为
$p^{-r}\bar\pi_0^{2r-1}=q_r$。
所以 Venjakob 的原 Euler 比准确是
$$
\boxed{E_r=\frac{1-p^{-r}\bar\pi_0^{2r-1}}
                   {1-p^{r-1}\bar\pi_0^{1-2r}}
       =\frac{1-q_r}{1-a_r}.}
\tag{24}
$$
这是同一 $\mathfrak p$ 上
$(1-\chi_r(\mathfrak p)/p)/(1-\chi_r^{-1}(\mathfrak p))$，
**分母不是** $1-\chi_r^{-1}(\bar{\mathfrak p})$。

取原 de Rham 基
$$
d_r=t_{\rm LT}^{1-2r}t^{r-1}\otimes\eta_r,
\qquad t^r d_r=\Omega_0^{1-2r}\otimes\eta_r.
\tag{25}
$$
用 $\log_r$ 表示把 $d_r$ 送至一后的 Bloch–Kato 对数。
$r\ge2$ 时 $H^0(V_r)=H^2(V_r)=0$，局部 $H^1$ 一维，
$H_f^1=H^1$；$q_r$ 的赋值为 $-r$，故 $1-\varphi$ 可逆，
Bloch–Kato 指数及其逆对数为同构。

已发表 epsilon 下降的其余因子在此逐项为：
未分歧局部 epsilon 为一；$\Gamma^*(r)=(r-1)!$；
$\nu(\sigma_{-1})=(-1)^r$；原 $t^r d_r$ 是 (25)。
于是对任意上述局部 Iwasawa 单位 $u$，有准确式
$$
\boxed{
\chi_r(\operatorname{Col}_{\mathfrak p}(u))
 =\frac{(-1)^{r-1}}{(r-1)!}\,
   \Omega_0^{1-2r}\frac{1-q_r}{1-a_r}\,
   \log_r\!\left(\operatorname{pr}_K
              \operatorname{tw}_{\chi_r}u\right).}
\tag{26}
$$
这里的特殊化与杯积相容性来自 epsilon 下降的基变换；
对 $\mathbb T$ 先按 $\chi_r$ 张量再做 Kummer 投影，
正是 (19)–(20) 的局部化。因此没有省略一个全局／局部控制同构。
把 (18) 及 $30$ 代入 (26)，即得原实际 Soulé 类的完整互反式。
这给出了本文所需两点的证明，不借用新预印本来代替这一步。

## 6. 两条固定负矩的准确局部类与赋值

联立 (9)、(21)、(26)，得到
$$
\boxed{
\log_6(\operatorname{loc}_{\mathfrak p}z_6)
 =-1280(1-\omega)\Omega_0^{12}
   \frac{1-\pi_0^5/\bar\pi_0^6}{1-\bar\pi_0^5/\pi_0^6}
   I_\Theta^2.}
\tag{27}
$$
联立 (10)、(12)、(21)、(26)，得到
$$
\boxed{
\log_5(\operatorname{loc}_{\mathfrak p}z_5^{\rm prim})
 =-\frac83\omega(1-\omega)\Omega_0^{10}
   \frac{1-\pi_0^4/\bar\pi_0^5}{1-\bar\pi_0^4/\pi_0^5}
   I_{\sigma,0}^2.}
\tag{28}
$$
若直接使用全模数类 $z_5^{(2\sqrt{-3})}$，右边再乘 $3/2$；
若使用原 $E_{17}$ 的 $I_\sigma$，右边再乘 $\theta^2$。
这两个真实规范差不可混用。

由于 $v_p(q_r)=-r$、$v_p(a_r)=r-1>0$，
$$
\frac{1-a_r}{1-q_r}=p^r e_{r,p},\quad
e_{r,p}=
\frac{1-p^{r-1}/\bar\pi_0^{2r-1}}
     {p^r-\bar\pi_0^{2r-1}}\in\mathcal O_p^\times.
\tag{29}
$$
所有固定有理常数和 $1-\omega$ 在当前 $p$ 均为单位。因此，
约定零的赋值为 $+\infty$，
$$
\boxed{
v_p\!\left(\log_6\operatorname{loc}_{\mathfrak p}z_6\right)
 =6+2v_p(I_\Theta),\qquad
v_p\!\left(\log_5\operatorname{loc}_{\mathfrak p}z_5^{\rm prim}\right)
 =5+2v_p(I_\sigma).}
\tag{30}
$$
这也给准确的双向非零判据：
$$
I_\Theta\ne0\ \Longleftrightarrow\
 \operatorname{loc}_{\mathfrak p}z_6\ne0,
\qquad
I_\sigma\ne0\ \Longleftrightarrow\
 \operatorname{loc}_{\mathfrak p}z_5^{\rm prim}\ne0.
\tag{31}
$$
单位判据分别是 $p^{-6}\log_6$ 和 $p^{-5}\log_5$ 为单位；
不能由未除去此准确 $p$ 因子的对数整性倒推出单位性。

### 6.1 另一普通素位及整个 Selmer 条件

在 $\bar{\mathfrak p}$ 上，(5) 的 type 交换，$V_r$ 的局部 Tate 权为
$1-r\le-1$。此时局部 $H_f^1=0$，而 Bloch–Kato 对偶指数是整个
$H^1$ 到一维 de Rham 空间的同构。
按相反 CM type 使用同一 Yager 单位与已发表 epsilon 下降，
对应 Katz 点位于经典象限；其复插值值正是 (15) 的零值。
Euler 因子非零，故该对偶指数为零，进而
$$
\boxed{\operatorname{loc}_{\bar{\mathfrak p}}z_6=0,
\qquad\operatorname{loc}_{\bar{\mathfrak p}}z_5^{\rm prim}=0.}
\tag{32}
$$
此论证是对实际类 (21) 的另一局部化，不是把两个不同全局类的局部值相认。
具体地，换 CM type 只把 (19) 的基换为其相容的共轭基；
椭圆单位 (17) 的 Kummer 类保持，(18) 在另一个选定 place 应用。
Yager 的恒等式在指定的另一个 place 评价同一 (17)，
因此这一步不需要额外假设两个独立 Soulé 类相等。

在每个 $v\nmid p$，$V_r$ 纯权一。
在潜在未分歧扩张上其 Frobenius 复绝对值为 $q_v^{1/2}$；
$V_r^*(1)$ 同样为权一。因此两者均无不变向量，局部 Euler 特征公式给
$H^1(K_v,V_r)=0$。结合 (32) 和 $\mathfrak p$ 处的 $H_f^1=H^1$，
$$
z_6\in H_f^1(K,V_6),\qquad
z_5^{\rm prim}\in H_f^1(K,V_5).
\tag{33}
$$
这里仍保留整个 Selmer 群。设
$$
H^1_{f,0}(K,V_r)=
\ker\!\left(H_f^1(K,V_r)\longrightarrow H^1(K_{\mathfrak p},V_r)\right).
\tag{34}
$$
尚未证明实际类 (21) 在 (34) 的商中非零。
即便单独知道全局类非零，也须排除它落入这个核。
$E_0$ 的秩零与已知有限 Sha 不能直接解决 (34)：
$V_6$、$V_5$ 的 CM type 差分别为十一、九，
并非 $E_0$ 的差一表示作一个共同 Tate twist。

## 7. 新稿的准确区域与已付的功能方程范围

Sano–Venjakob 的预印本 *On extended interpolation properties of the Katz
$p$-adic $L$-function*，arXiv:2610.36607v1（2026-10-27），
Theorem 2.4.1 的两点特殊化与本文 (26) 相同。
本文已从已发表局部输入推导该特殊化；这里仅登记新稿范围，
不从它未声称的全局非零推出结论。

| 点 | Deligne critical 区域 | 所选 $\mathfrak p$-Katz 的经典插值 | 新稿相关结论 |
|---|---|---|---|
| $(-5,6)$、$(-4,5)$ | 另一 critical 象限 | 区外 | Th. 2.4.1 的局部 log |
| $(6,-5)$、$(5,-4)$ | 经典 critical 象限 | 区内 | Cor. 2.4.5 的对偶指数 |
| $k,j\le0$、非 $(0,0)$ | 新稿另列的 Beilinson 区域 | 另一区域 | Cor. 2.4.7 |

尤其，原负矩点不是 Deligne 意义的非临界点；其问题在于选定普通 CM type
的插值象限。Corollary 2.4.5(ii) 的 TNC 结论明列复值非零为前提，
在本篇反射点由 (15) 精确失效。Corollary 2.4.7 的两个指数都非正，
也不适用于本篇两点；其中的 $p$ 进 regulator 本身亦不能被自动换成非零。

角色上的正确 Katz 对偶 involution 是
$$
\nu\longmapsto\mathrm N(\nu^c)^{-1}.
\tag{35}
$$
对 (5) 它固定原角色，并不把 $(-5,6)$ 送去 $(6,-5)$。
裸共轭 $\nu\mapsto\nu^c$ 则同时交换 $\mathfrak p$ 与
$\bar{\mathfrak p}$ 的 Katz 数据。
所以用反射后的复临界值给原负矩赋值，缺少的正是这一步普通局部比较；
(27)–(32) 已把它写为实际局部类，而非一个已知正临界单位。

已发表的 Agboola 2026, *On values of the Katz two-variable p-adic L-function*，
§11 给高权的相应特殊值／高度关系，但相关非零推论保留
restricted Selmer 秩、零点阶或高度非退化假设；它没有为本篇两条固定类
提供所有大普通 $p$ 的无条件局部非零。

## 8. 全负族中一个无条件单位输入及其量词

同一原 $\mu_6$ 型还给一个明确、无需猜想的边界。
令 $h=(p-1)/6$。单位群上的 Fermat 同余直接给
$$
\int x^{-6h}\,d\nu_\Theta
 \equiv \int1\,d\nu_\Theta
 =1-\bar\pi_0^{-1}\pmod p,
\tag{36}
$$
$$
\int x^{1-6h}\,d\nu_{\sigma,0}
 \equiv\int x\,d\nu_{\sigma,0}
 =\Omega_0\left(1-\pi_0/\bar\pi_0^2\right)\pmod p.
\tag{37}
$$
两者都是单位，前者的单位性已由 R316 的有理二挠和 Hasse 界完整证明。
所以对每个当前 $p$，两族
$I_{-6n}(\Theta)$、$I_{1-6n}(\sigma)$ 在 $1\le n\le h$ 各至少有一个单位。

上述证明同时延伸到所有 $r=6n$ 的 Theta 族和 $r=6n-1$ 的 sigma 族：
类仍用 (17)–(21)，原 primitive 二处归一仍分别为一和 $2/3$。
一般对数赋值为
$$
v_p(\log_r\operatorname{loc}z_r^{\rm prim})
 =r+v_p((r-1)!)+2v_p(I_{-r}).
\tag{38}
$$
因此在 (36)–(37) 选取的 $r=p-1$、$p-2$ 上，
实际全局类有非零局部化，对数赋值准确为 $p-1$、$p-2$。
它们是**权随 $p$ 变化**的实际非零类；不能用鸽笼原理从这个增长的范围
抽出一个固定负权对无穷多个 $p$ 非零。

(16) 与 (36)–(37) 也具体说明：所有这些反射复中心为零，
而原负矩族对每个 $p$ 确有单位。二者之间不存在可省略的直接数值反射。
后继要付的是 (27)–(31) 中固定两条类的局部不消失，
或在原同 sigma 六核中对完整负矩族进行真正的中央消去；
不能把现有的移动权非零改称原目标中央导数非零。

## 9. 证书与出处

精确常数与坏局部型证书：
[check-jzero-fixed-negative-moments-soule-and-root-signs.py](../scripts/check-jzero-fixed-negative-moments-soule-and-root-signs.py)
及同名 JSON，**37 项精确检查全部 PASS**。它只核原角色、完整坏位相位、Euler 比、实际周期次数、
固定有理常数及一般根数比较；没有素数扫描，也不以计算代替 (26) 的局部证明。

已发表主输入：

- R. I. Yager, *On two-variable $p$-adic $L$-functions*, Annals of Mathematics
  **115** (1982), 411–449，[原期刊页](https://annals.math.princeton.edu/1982/115-2/p08)。
- E. de Shalit, *Iwasawa Theory of Elliptic Curves with Complex Multiplication*,
  Academic Press, 1987，Proposition I.3.9、Theorem II.4.14。
  本文只用其同一 Coleman 变换与实际椭圆单位像。
- O. Venjakob, *On Kato's local epsilon-isomorphism conjecture for rank-one
  Iwasawa modules*, Algebra & Number Theory **7** (2013), 2369–2416，
  §2.4、Proposition 2.12、Theorem 2.13，
  [已发表全文](https://msp.org/ant/2013/7-10/ant-v7-n10-p01-p.pdf)。
- D. Loeffler and S. L. Zerbes, *Iwasawa theory and $p$-adic $L$-functions over
  $\mathbf Z_p^2$-extensions*, International Journal of Number Theory **10**
  (2014), 2045–2095，§6.4、Theorem 6.11，
  [作者全文](https://arxiv.org/abs/1108.5954)。
- M. Bertolini, H. Darmon and K. Prasanna, *$p$-adic Rankin $L$-series and rational
  points on CM elliptic curves*, Pacific Journal of Mathematics **260** (2012),
  261–303，§3A 的两 critical 象限及 §1 的复共轭／$p$ 进共轭区别，
  [作者全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/52.BDP2/bdp-pjm.pdf)。
- A. Agboola, *On values of the Katz two-variable $p$-adic $L$-function*,
  Annales mathématiques du Québec (2026)，§11，
  [期刊全文](https://doi.org/10.1007/s40316-026-00273-2)。

仅作现状核对的新稿：T. Sano and O. Venjakob，
*On extended interpolation properties of the Katz $p$-adic $L$-function*，
2026，Theorem 2.4.1、Corollaries 2.4.5、2.4.7，
[arXiv:2610.36607](https://arxiv.org/abs/2610.36607)。

仓库直接输入：[R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)、
[R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)、
[R330](R330-original-target-seven-eight-carry-and-sixfold-central-difference.md)。
