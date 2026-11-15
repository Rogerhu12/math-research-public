# R804 — 原十八阶型四负二值的全局 Soulé 类、共同 Artin 周期与局部化

日期：2026-11-15。**状态：本篇支付 R806 三个实际 finite η 的全局椭圆单位类、完整正 Coleman 特殊化、固定 Artin 周期、另一普通素位的零局部化及准确赋值。它不证明这些类的指定局部化非零，也不把 R801 的线性负二行改成 Katz 值的线性和。**

这里使用原模数 $34\delta$ 的全 ray class 塔，以及已发表的
semilocal Coleman 和 rank-one epsilon 下降。因而不将
Sano–Venjakob 的仅含所列 p-primary 有限角色的公式，未经扩张直接用于十七处分歧角色。
同样，以下全局类不是用一个局部对数的逆像命名出来的。

## 1. 原有限角色、曲线、周期和所选素位

保持 [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)
的完整规范：
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad
E_0:y^2=x^3+1,\quad \theta=17^{1/6}>0,\quad
\Omega_0=\Omega_{p,0}=\theta\Omega_p .
\tag{1}
$$
$\psi_0$ 是 $E_0$ 对原微分 $dx/(2y)$ 的 type-$(1,0)$ 角色，
$\pi_0=\psi_0(\mathfrak p)$、$\bar\pi_0=\psi_0(\bar{\mathfrak p})$，
$v_p(\pi_0)=1$、$\pi_0\bar\pi_0=p$。
沿原 ray 有
$$
\pi_0\equiv1\pmod2,\qquad \pi_0\equiv\delta\pmod{17}.
\tag{2}
$$
所有素数均避开固定 $2,3,5,17$ 及既有有限坏集。

对 $j\in\mathcal J=\{4,10,16\}$，保留 R806 的完整有限角色
$$
\eta_j((a))=
\left[
 \operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
 (a\bmod17)^{16(j-9)}
\right]^{-1}.
\tag{3}
$$
指数的值取原 $\mu_{18}$ 提升。它们具有
$$
\eta_j^c=\eta_j^{-1},\quad\operatorname{ord}\eta_j=18,\quad
\mathfrak f_{\eta_j}=(34),\quad
\eta_j(\delta)=-1,\quad
\eta_j(\mathfrak p)=\eta_j(\bar{\mathfrak p})=-1.
\tag{4}
$$
三条切出同一个固定 cyclic18 域 H/K，且
$$
e_2(H/K)=3,\qquad e_{17}(H/K)=18,\qquad e_3(H/K)=1,
\qquad \eta_j^9=\kappa_{17},
\tag{5}
$$
其中 $\kappa_{17}$ 是 $K(\sqrt{17})/K$ 的二次角色。
全局十八阶角色没有被(5)替换成二次角色。

所需 Katz 点及其对偶表示是
$$
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2,\qquad
V_j=E_{\mathfrak P}(1)\widehat\nu_j^{-1}
=\eta_j^{-1}\widehat\psi_0^2\widehat{\bar\psi}_0^{-1},
\tag{6}
$$
$E=K(\zeta_{18})$，并固定原系数嵌入 $E\hookrightarrow\overline{\mathbf Q}_p$；
$E_{\mathfrak P}$ 是其完成。$\nu_j$ 的 type 是 $(-1,2)$，
真正导子为
$$
\mathfrak f=(34\delta).
\tag{7}
$$

## 2. 同一全局 ray class 塔与真实 η 分量

令
$$
F_n=H\,K(E_0[p^n]),\qquad F_\infty=\bigcup_nF_n,\qquad
\mathscr G=\operatorname{Gal}(F_\infty/K).
$$
它包含于 $K(\mathfrak f p^\infty)$。
$H\cap K(E_0[p^\infty])=K$：前者在17的惯性是整个十八阶群，
后者在17未分歧。因此
$$
\mathscr G\simeq\operatorname{Gal}(H/K)\times
              \operatorname{Gal}(K(E_0[p^\infty])/K)
\tag{8}
$$
是实际全局分解；不要求相应局部扩张也作不相交乘积。

取与 R332 相同的辅助理想 $\mathfrak a=(5)$，以及正 Coleman 的 Kato 椭圆单位规范。
先在完整 $K(\mathfrak f p^n)$ 上构造 norm-compatible 椭圆单位，
再取到 $F_n$ 的实际范数，得到
$$
u_\infty\in H^1_{\rm Iw}(F_\infty/K,\mathbf Z_p(1))
           \otimes_{\mathbf Z_p}\mathcal O_{E_{\mathfrak P}}.
\tag{9}
$$
等价地，可使用 Robert 单位的 Kummer 类乘固定 $-1/12$；
这正是 Kato 正 Coleman 规范，且12在当前素数为单位。
本篇固定
$$
\boxed{
\operatorname{Col}_{\mathfrak p}
       (\operatorname{loc}_{\mathfrak p}u_\infty)
=(25-\sigma_{(5)})\,\mathcal L_{\mathfrak f}.
}
\tag{10}
$$
$\mathcal L_{\mathfrak f}$ 是原周期规范下全 ray class Katz 测度的实际推前。
范数与 semilocal Coleman 交换；(10)并未插入一个未说明的
$[K(\mathfrak f):K]$ 或18因子。

这个构造的已发表来源是 de Shalit II.4.11–4.14：
其固定非 p 模数可以是任意这里的 $\mathfrak f$，并非只取 $\psi_0$ 的导子。
局部 Coleman 的全部不分歧共轭及全局诱导由
Loeffler–Zerbes §6.4、Theorem 6.11 保持；
其 group-ring 标号与 R332 的正 Coleman 规范相同。
在本篇点，2、3、17均真正分歧，故
$\nu_j(\mathcal L_{\mathfrak f})$ 正是 R806 的 primitive Katz 值，
没有 R332 sigma 情形那样另需删除二处的 $3/2$ 因子。

有限角色投影可以明确写为
$$
e_{\eta_j}=\frac1{18}
\sum_{g\in\operatorname{Gal}(H/K)}\eta_j(g)^{-1}g .
\tag{11}
$$
它在单位来源上取 $\eta_j$-等型分量；
随后张量 $\eta_j^{-1}$ 才下降到 K。
因 $\nu_j|_{\operatorname{Gal}(H/K)}=\eta_j$，
$\nu_j(e_{\eta_j})=1$，所以(10)的该特殊化不产生额外18。
这保留的是原完整十八阶分量，而非只取其在
$\mathfrak p$ 上的二次限制。

取原相容 Tate 基 $\xi_{\rm LT}\in T_{\pi_0}E_0$、
$\xi_{\rm cyc}\in\mathbf Z_p(1)$。
令 $e_j$ 是 $\eta_j^{-1}$ 的固定系数基，并置
$$
T_j=\mathcal O_{E_{\mathfrak P}}(1)\widehat\nu_j^{-1},\qquad
v_j=e_j\otimes\xi_{\rm LT}^{\otimes3}
                  \otimes\xi_{\rm cyc}^{\otimes(-1)}.
\tag{12}
$$
这个基在 $F_\infty$ 上平凡，故杯积
$\xi_{\rm cyc}^{-1}\otimes v_j$ 给真正的 Iwasawa 扭曲。
定义
$$
\boxed{
z_j=\frac1{30}\,
 \operatorname{pr}_K\operatorname{tw}_{\nu_j}
          (e_{\eta_j}u_\infty)
\in H^1(\mathcal O_{K,\Sigma},V_j),
}
\tag{13}
$$
$\Sigma$ 包含 $p,2,3,17,\infty$。
这里 $\operatorname{pr}_K$ 是实际 Iwasawa 上同调特殊化／corestriction，
不是只在局部群中选一个类。
因为 $\eta_j((5))=1$ 且
$\psi_0((5))=\bar\psi_0((5))=-5$，
$$
25-\nu_j((5))=25-(-5)=30.
\tag{14}
$$
(13)的平滑因子由同一个全局单位来源确切给出。

## 3. 原 ray 上明确的共同 Artin 周期

在原所选 $K_{\mathfrak p}=\mathbf Q_p$ 上，
$\eta_j$ 未分歧且算术 Frobenius 值为 $-1$。
由(5)，三个 $\eta_j$ 的局部限制都等于
$\kappa_{17}|_{G_{K_{\mathfrak p}}}$。
还可直接从(2)核对：
$p\equiv3\bmod17$，故
$(17/p)=(3/17)=-1$。
因此 $\sqrt{17}=\theta^3$ 位于该普通位的非平凡不分歧二次扩张，
其 Frobenius 值为负。

于是
$$
\boxed{\sqrt{17}\,e_j\in D_{\rm dR}(\eta_j^{-1})}
\tag{15}
$$
是三个有限因子的同一个明确不分歧基。
$\sqrt{17}$ 是固定代数 p 单位；它不是待选的 $\mathbf C_p$ 周期。
(15)只作局部平凡化，并未把全局 $H/K$ 的十七处十八阶惯性删掉。

记 $t_{\rm LT}$、$t_{\rm cyc}$ 为与(12)相容的原 period；
规范为 $t_{\rm LT}=\Omega_0t_{\rm cyc}$。
本篇 de Rham 基固定为
$$
d_j=\sqrt{17}\,t_{\rm LT}^{-3}t_{\rm cyc}\otimes v_j,
\qquad
\boxed{t_{\rm cyc}^{2}d_j=\sqrt{17}\,\Omega_0^{-3}\otimes v_j.}
\tag{16}
$$
令 $\log_j$ 为把 $d_j$ 送至一后的 Bloch–Kato 对数。
这样所有 Artin、CM 与 Tate 基变换均有明确位置。

## 4. 两个方向不同的 Euler 比与完整局部下降

在 $\mathfrak p$ 上，(6)准确为
$$
V_j=E_{\mathfrak P}(2)
       \otimes(\eta_j^{-1}\bar\psi_0^{-3}).
$$
不分歧因子的算术 Frobenius 值为 $-\bar\pi_0^{-3}$，
所以 $D_{\rm cris}$ 上的标量是
$$
q_j=-p^{-2}\bar\pi_0^3=-\frac{\bar\pi_0}{\pi_0^2}.
$$
同一所选素位还给
$$
a_j=\nu_j(\mathfrak p)^{-1}
   =-\frac{\pi_0}{\bar\pi_0^2},\qquad
q_j=\frac{\nu_j(\mathfrak p)}p .
\tag{17}
$$
**两个值均来自同一 $\mathfrak p$**，不把分母改成另一普通素位。

为避免方向混淆，分别定义
$$
\mathcal E_{\rm Col}=\frac{1-q_j}{1-a_j}
=\frac{1+\bar\pi_0/\pi_0^2}{1+\pi_0/\bar\pi_0^2},
$$
$$
\boxed{
\mathcal E_{\log}=\mathcal E_{\rm Col}^{-1}
=\frac{1+\pi_0/\bar\pi_0^2}{1+\bar\pi_0/\pi_0^2}
=p^2\,\frac{1+p/\bar\pi_0^3}{p^2+\bar\pi_0^3}.
}
\tag{18}
$$
因此 $\mathcal E_{\rm Col}\in p^{-2}\mathcal O^\times$，
而 $\mathcal E_{\log}\in p^2\mathcal O^\times$。
两者的分子、分母都非零。

现在将 Venjakob 2013 Theorem 2.13 的原 rank-one epsilon 元素
沿 $\mathscr G\to\widehat\nu_j$ 特殊化。
该定理允许任意不分歧有限系数因子；
(4)在 p 正是这种因子，故十七处的分歧不阻碍这一步局部下降。
全局的十七处分量已经在(9)–(13)中保留。

逐项的局部因子为：

- 本地 Tate 指数为2，故 $\Gamma^*(2)=1!$；
- 所选 $\sigma_{-1}$ 上 $V_j$ 的值为 $(-1)^2=1$；
- 未分歧 rank-one 的本地 epsilon 为1；
- 原正 Coleman 对应的前置号是 $-V_j(\sigma_{-1})=-1$；
- 原 Euler 比正是 $\mathcal E_{\rm Col}$；
- 由(16)，$t_{\rm cyc}^2$ 与 de Rham 基的转换为
  $\sqrt{17}\Omega_0^{-3}$。

Kummer、扭曲、有限幂等元与 semilocal 诱导均与该下降相容。
因此把(10)、(13)、(14)代入，准确得到
$$
\boxed{
\mathcal K^{\rm prim}_{34\delta}(\widehat\nu_j)
=-\sqrt{17}\,\Omega_0^{-3}\,
 \mathcal E_{\rm Col}\,
 \log_j(\operatorname{loc}_{\mathfrak p}z_j).
}
\tag{19}
$$
等价、反方向的式子为
$$
\boxed{
\log_j(\operatorname{loc}_{\mathfrak p}z_j)
=-\frac{\Omega_0^3}{\sqrt{17}}\,
 \mathcal E_{\log}\,
 \mathcal K^{\rm prim}_{34\delta}(\widehat\nu_j).
}
\tag{20}
$$
这同时核定号、Artin 周期和 $p^{+2}$ 所在的方向，
而不是仅凭目标赋值事后调换 Euler 因子。

为核(19)中的 Katz 规范，可在原经典正权上直接比较。
Coleman 插值中的
$$
\frac{1-\chi(\mathfrak p)/p}{1-\chi^{-1}(\mathfrak p)}
 L_{\Sigma}(\chi^{-1},0)
$$
约去 $L_\Sigma$ 内同一个 $\mathfrak p$ 因子，剩
$$
(1-\chi(\mathfrak p)/p)(1-\chi^{-1}(\bar{\mathfrak p}))
L^{\rm prim}(\chi^{-1},0).
$$
原 $\chi\chi^c=\mathrm N$ 使两个 ordinary 因子相同；
这恰是 R806(30) 的平方因子。
因2、3、17的导子均准确，比较没有额外坏处 Euler。
既有 CM 周期和(16)保持同一 Tate 基；未通过选择另一个
Katz 测度的 scalar 来吸收 $\sqrt{17}$。

## 5. 原三个负二矩、准确赋值与局部非零判据

R806 保留的原物理测度是
$$
I_{j,-2,p}=\int_{\mathbf Z_p^\times}x^{-2}\,d\nu_{D_{j,17}}(x),
$$
以及固定代数常数 $c_j\ne0$。其完整平方为
$$
\mathcal K^{\rm prim}_{34\delta}(\widehat\nu_j)
=34^2c_j\theta^9\Omega_p\,I_{j,-2,p}^{\,2}.
\tag{21}
$$
把(1)、$\sqrt{17}=\theta^3$ 和(21)代入(20)，得到
$$
\boxed{
\log_j(\operatorname{loc}_{\mathfrak p}z_j)
=-34^2c_j\theta^9\Omega_p^4\,
 \frac{1+\pi_0/\bar\pi_0^2}{1+\bar\pi_0/\pi_0^2}
 I_{j,-2,p}^{\,2}.
}
\tag{22}
$$
特别是 $\Omega_0^3/\sqrt{17}=\Omega_p^3$；
这说明(22)的 $\theta^9$ 与四次 $\Omega_p$ 均不可删除。
如果改用未包含(15)的另一个局部基，必须同步改变 scalar 对数，
不能直接照搬(22)。

删去三个固定 $c_j$ 的有限非单位支撑后，(18)和原周期单位性给
$$
\boxed{
v_p\!\left(\log_j\operatorname{loc}_{\mathfrak p}z_j\right)
=2+2v_p(I_{j,-2,p}).
}
\tag{23}
$$
零值双方允许 $+\infty$。
这里 $H^0(K_{\mathfrak p},V_j)=
H^0(K_{\mathfrak p},V_j^*(1))=0$，局部 $H^1$ 一维；
Tate 指数2使 $H_f^1=H^1$，而 $1-q_j$ 可逆。
所以 Bloch–Kato 对数是同构，从而
$$
\boxed{
I_{j,-2,p}\ne0
\iff\operatorname{loc}_{\mathfrak p}z_j\ne0.
}
\tag{24}
$$
单位判据是 $p^{-2}\log_j$ 为单位，不能从未经除去 $p^2$
的对数整性推出它。

## 6. 同一个全局类的另一普通局部化与完整 Selmer 群

在 $\bar{\mathfrak p}$ 上，(6)的本地 Tate 指数为 $-1$，
$H_f^1=0$，对偶指数是局部 $H^1$ 到一维 de Rham 空间的同构。
对同一个(9)的 semilocal 全局单位来源，在这个 place 使用
经典象限的 Coleman 插值。所读复值是
$$
L(\nu_j^{-1},0)=L(\eta_j^{-1}\psi_0^3,2).
$$
R806 已逐2、3、17、无穷位计算该 weight4 中心的根数为 $-1$，
故该复值为零。Euler 因子不为零，所以
$$
\boxed{\operatorname{loc}_{\bar{\mathfrak p}}z_j=0.}
\tag{25}
$$
这不是把另一个共轭 Soulé 类同本类相认：
同一 norm-compatible 单位的 semilocal 诱导包含两个普通位，
在各位评价同一个扭曲和同一个全局特殊化；
换基只改其相容 de Rham 表示，不改(13)。

对 $v\nmid p$，$V_j$ 及 $V_j^*(1)$ 都纯权一；
在潜在未分歧扩张上，Frobenius 复绝对值为
$(\mathrm Nv)^{1/2}$，故二者都无不变向量。
由局部 Tate 对偶和 Euler 特征，$H^1(K_v,V_j)=0$。
因此(13)实际满足全部 Bloch–Kato 条件：
$$
\boxed{z_j\in H_f^1(K,V_j).}
\tag{26}
$$
定义真正的严格核
$$
H_{f,0}^1(K,V_j)=
\ker\!\left(H_f^1(K,V_j)\longrightarrow
                   H^1(K_{\mathfrak p},V_j)\right).
\tag{27}
$$
本篇没有证明 $z_j$ 在该商中非零。
单独的全局类非零也不能代替(24)中的局部非零；
$V_j$ 的 CM type 差为3，既不是原秩一椭圆点表示，
也不是一个差一表示的共同 Tate twist。

## 7. 同一原二阶行及投影连接仍保留全部线性信息

原 R801/R806 实际来源为
$$
G_{2,N}=\sum_{j\in\mathcal J}\alpha_{j,N}D_{j,17},
$$
其所有系数、原 $q_N^*$、58行、$2!$、E 深及 Y-unit 都固定。
准确原值是
$$
\mathcal I_{2,N}
=\lambda^{2N}\Omega_p^2
   \sum_{j\in\mathcal J}\alpha_{j,N}I_{j,-2,p}.
\tag{28}
$$
(22)识别各 $I_j$ 的平方与真实全局类的局部对数，
不把(28)变成三条 $z_j$ 的线性局部化，也不为平方根选择未经支付的相容符号。
有限角色互异本身不使这些高权对数平方根在
$\overline{\mathbf Q}$ 上线性独立。

[R807](R807-original-projected-connection-and-native-second-source.md)
另外给同一个 $G_{2,N}$ 的唯一旧 primitive 型五预像
$$
G_{2,N}=P_4\nabla_{34}P_{-,N}.
$$
其完整半周期交换子及
degree1 × degree33 和变量卷积均仍保留。
这个 finite theta 连接不是将(6)与旧点表示同一化的 Galois-equivariant 映射，
故(22)也没有删除 R807 的 ζ 伴随、半周期 unit 转置或原 W 外部。

本篇后续的实际新问题是：证明(13)至少一个指定类不落入(27)，
或用同一个原来源的完整线性关系控制(28)及其原中央补域。
原三中央同时为零的排除尚未完成。

## 8. 已发表输入与本篇的扩张步骤

本篇未作数值扫描，也未使用新的有限数据文件。

- de Shalit，*Iwasawa Theory of Elliptic Curves with Complex Multiplication*，
  1987，I.3.8–3.9、II.4.11–4.14：
  任意固定非 p 模数的原椭圆单位测度、全部 finite ray class 角色及周期规范。
- Loeffler–Zerbes，*Iwasawa theory and p-adic L-functions over
  Z_p^2-extensions*，IJNT 10 (2014)，§6.4、Theorem 6.11，
  [作者全文](https://arxiv.org/pdf/1108.5954)：
  完整不分歧共轭与 semilocal Coleman 比较。
- Venjakob，*On Kato's local epsilon-isomorphism conjecture for rank-one
  Iwasawa modules*，ANT 7 (2013)，Proposition 2.12、Theorem 2.13，
  [期刊全文](https://msp.org/ant/2013/7-10/ant-v7-n10-p01-p.pdf)：
  任意有限不分歧系数的 rank-one 下降、负 Coleman 换号及基变换。
- [R332](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md)：
  原正 Coleman、Tate 基、同一 $\mathfrak p$ 的 Euler 方向及完整 Selmer 论证。
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)：
  原完整十八阶角色、三个标准 theta 截面、固定 $c_j$、平方(21)及反射 root。

Sano–Venjakob，*On extended interpolation properties of the Katz p-adic
L-function*，[2610.36607v1](https://arxiv.org/pdf/2610.36607)，
Theorem 3.3.2、§3.4，将上述局部输入写成完全相同的显式式。
本文实际扩张的步骤是(8)–(14)中的全局 $34\delta$ ray class η 分量
与(15)–(16)的固定 Artin 基，而非未经核对地援引其仅列 p-primary
角色的 §3.6。其带非零前提的其他定理不用于(24)后的非消失。
