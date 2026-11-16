# R875 — 原17挠点有限 Eisenstein 和与精确 Hom 度数 Gram

日期：2026-11-16。

**状态：下文完整证明原有限和、周期符号、三次压缩、精确有理 Gram 及其整 Hom 必要条件。附带 producer 只在公开 Actions 执行；真实数值结论按成功 run 另行登记，不从 R874 的球区间取整。** 本篇始终使用 R862 的同一原17挠点、余循环、三个 CM 角色、$\Xi_0$ 与 $C_v$。它不构造尚未认证的椭圆坐标，也不宣称原 Frobenius shadow 非零。

## 1. 原来源与度数二次型

保持
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega=i\sqrt3,\quad
\alpha=-1+2\omega,
$$
以及 R873 的三个原新形式和平方角色
$$
F_j=\theta(\beta_j),\quad
B_j=\beta_j^2,\quad
\zeta_j=\zeta\omega^j,\quad \zeta^3=\omega^2,\quad
j=0,1,2.
$$
$F_j$ 的完整导子为 $17\delta$，而 $B_j$ 的导子准确为17。
对素于17的主理想，
$$
B_j((u))=u^2\chi_j(u),\qquad
\chi_j(u)=\zeta_j^{\,2r(u)},\quad
r(u)=\log_\alpha(u\bmod17)\bmod9.
\tag{1}
$$
这里原3处符号在平方后消去，$B_j((\delta))=-3$ 仍在完整
$L$ 函数内。$\chi_j$ 的核正是
$$
G_{32}=\langle\delta\bmod17\rangle\subset\mathbf F_{289}^{\times}.
$$
特别地它在 $\mathbf F_{17}^{\times}$ 和 $\delta$ 上均为1，
但不在整个 $\mu_6$ 上平凡；(1)与 $u^2$ 合在一起才不依赖理想生成元。

保持原实17挠点 $P$ 及
$$
h=\prod_{g\in G_{32}/\{\pm1\}}x([g]P),\quad
v=h^3/2^{32},\quad d=h/2^{11},\quad d^3=v/2.
$$
原目标与原微分是
$$
C_v:Y^2+vY=X^3,\qquad
\kappa^*\omega_0=d\,\omega_v,\qquad
E_0:y^2=x^3+1,\quad\omega_0=\frac{dx}{2y}.
\tag{2}
$$
R864、R869 的原 Gauss 系数及微分为
$$
G_j=1+\frac{u_1}{\alpha\zeta_j}
       +\frac{u_2}{\alpha^2\zeta_j^2},\qquad
H_0=\frac13\sum_jG_jF_j,\qquad
\Xi_0^*\omega_v=H_0(q)\frac{dq}{q}.
\tag{3}
$$
原 $H_0$ 具有实系数，三条 $F_j$ 亦有实系数且线性独立，
所以在这个固定实嵌入下每个 $G_j$ 都是实数。
后文可用 $G_j^2=|G_j|^2$，不是任意换嵌入后省略复共轭。

设
$$
E=\mathbf Q(\vartheta),\quad \vartheta^3-3\vartheta+1=0,\qquad
\mathcal B_E=(1,\vartheta,\vartheta^2-2).
$$
三个实嵌入把后两基元送到
$$
\epsilon_{1,j}=\zeta_j+\zeta_j^{-1},\qquad
\epsilon_{2,j}=\zeta_j^2+\zeta_j^{-2}.
$$
R873 给同一原准 Hom 的度数二次型
$$
q(u)=\sum_{j=0}^2w_j\,u_j^2,\qquad
w_j=\frac{136}{\sqrt3\mathcal A_v}G_j^2L(B_j,2)>0,
\tag{4}
$$
其中 $\mathcal A_v=\int i\omega_v\wedge\bar\omega_v$。
若 $\Xi_0u$ 是实际 Hom，$q(u)$ 才同时是该映射的整数度数。
本篇精确计算(4)，不由它反推整性。

## 2. 实周期、指数3与有限和的负号

记 $\Omega_R$ 为 $\omega_0$ 的最小正实周期。沿 $E_0(\mathbf R)$
的两支积分，
$$
\Omega_R=\int_{-1}^{\infty}\frac{dx}{\sqrt{x^3+1}}.
$$
分别在 $[-1,0]$ 和 $[0,\infty)$ 作 beta 积分，并用
$\Gamma(1/6)\Gamma(5/6)=2\pi$，得
$$
\Omega_R=\frac{\Gamma(1/3)\Gamma(1/6)}{2\sqrt\pi}.
\tag{5}
$$
R873 的完整复面积于是等于
$$
\mathcal A_0=\frac{\Omega_R^2}{\sqrt3}.
\tag{6}
$$

原 CM 周期格 $\Lambda$ 包含 $\Omega_R\mathcal O_K$。
后者的 $i\,dz\wedge d\bar z$ 面积是 $\sqrt3\Omega_R^2$，
由(6)它在 $\Lambda$ 中的指数准确为3。
$\mathcal O_K$ 的唯一范数3素理想是 $(\delta)$；
因此唯一相容的 CM 过格给
$$
\boxed{\Lambda=\Omega\mathcal O_K,\qquad
\Omega=\Omega_R/\delta,\qquad
\mathcal A_0=\sqrt3|\Omega|^2.}
\tag{7}
$$
特别地 $\Omega$ 是纯虚数，
$$
\frac{\bar\Omega^2}{|\Omega|^2}=-1.
\tag{8}
$$
(7)支付了可能漏掉的指数3，而(8)支付后面有限和的绝对负号。

原实非零17挠点满足
$$
P=a\Omega_R/17=\delta a\Omega/17
\quad\text{在 }\mathbf C/\Lambda,\qquad
a\in\mathbf F_{17}^{\times}.
\tag{9}
$$
由(1)，$\chi_j(\delta a)=1$。
所以把 $\Omega u/17$ 的分点标记改为实际 $[u]P$ 时没有隐藏相位。
这只使用原实点的既定规范，不允许另取任意非实点后保同一 Gauss 系数。

## 3. 完整 Hecke 正则化与原17挠点有限和

在 $\operatorname{Re}s>2$，理想和绝对收敛，类数1与六个单位给
$$
L(B_j,s)=\frac16
 \sum_{\substack{u\in\mathcal O_K\setminus\{0\}\\17\nmid u}}
 \frac{\chi_j(u)u^2}{|u|^{2s}}.
\tag{10}
$$
令 $z=s-2$。其求和项变为
$\chi_j(u)\bar u^{-2}|u|^{-2z}$。
先在 $\operatorname{Re}z>0$ 按 $u\bmod17$ 分组，
再用 Hecke 正则化延拓到 $z=0$。

Khuri-Makdisi §2 的定义(2.1)–(2.2)给这同一正则化；
其(3.5)给
$$
x(Q)=G_2(Q)-G_2(0).
$$
在固定格 $\Lambda$ 上取复共轭版本。
因 $\sum_{u\in\mathbf F_{289}^{\times}}\chi_j(u)=0$，
全部与 $Q$ 无关的项，包括 weight2 的非全纯常数，都准确消去。
利用(7)的格缩放和(9)的实际标记，得到
$$
L(B_j,2)=\frac{\bar\Omega^2}{6\cdot17^2}
 \sum_{u\in\mathbf F_{289}^{\times}}
 \chi_j(u)\,\overline{x([u]P)}.
$$
故
$$
\boxed{
\frac{L(B_j,2)}{\mathcal A_0}
=-\frac1{6\cdot289\sqrt3}
 \sum_{u\in\mathbf F_{289}^{\times}}
 \chi_j(u)\,\overline{x([u]P)}.
}
\tag{11}
$$
这是包含原3处 Euler 项的完整值。
没有把条件收敛的格点和任意重排；分组在绝对收敛半平面完成，
其后使用同一解析延拓。

定义九个实际陪集和
$$
T_r=\sum_{g\in G_{32}/\{\pm1\}}x([\alpha^r g]P),
\qquad r=0,\ldots,8.
\tag{12}
$$
因为 $P$ 实、$\bar\alpha=7/\alpha$ 且
$7\in\mathbf F_{17}^{\times}\subset G_{32}$，
$$
\bar T_r=T_{-r}.
$$
每个非零 $x$ 坐标在完整乘法群中恰被 $\pm$ 计两次，所以(11)的和为
$$
2\sum_{r=0}^8\zeta_j^{-2r}T_r.
\tag{13}
$$
把(11)–(13)代回(4)，用 $\mathcal A_v=\mathcal A_0/d^2$，
得到原权的完全代数式
$$
\boxed{
w_j=-\frac8{153}\,d^2G_j^2
       \sum_{r=0}^8\zeta_j^{-2r}T_r.
}
\tag{14}
$$
这里的2只来自 $\pm$；不能再添16或32。
$136/(3\cdot867)=8/153$，所以面积、源指数和有限轨道的常数一致。

## 4. 同一原17分点商中的三次压缩

保持 R864 的定向自同构
$$
\sigma(P)=[\alpha]P,\qquad
\sigma(h)=\alpha h/\ell(v),\qquad
\tau(v)=\alpha^3v/\ell(v)^3,
$$
其中
$$
\ell(v)=\frac{
21905009-23122022\omega+
(112353990182+54575060764\omega)v+
(305813+148546\omega)v^2}{25505280},
$$
$$
v^3+367395v^2+147v+\frac1{17}=0,\quad
N\ell=c=-1-19\omega=\alpha^3\omega^2.
\tag{15}
$$
因此
$$
\tau^3=1,\qquad \sigma^3h=\omega h.
\tag{16}
$$

$T_0$ 与 $h$ 都被 $G_{32}$ 固定。
在 $\mu_3$ 的 CM 作用下，$x$ 乘 $\omega$，
故 $T_0$ 乘 $\omega$，而16项乘积 $h$ 亦乘 $\omega^{16}=\omega$。
所以 $T_0/h$ 落在 $K(v)$。
原 $P$ 实又使这个商被复共轭固定，故它准确落在
$F=\mathbf Q(v)=\mathbf Q(\sqrt[3]{17})$：
$$
\boxed{T_0=h\,t(v),\qquad t(V)\in\mathbf Q[V],\quad \deg t\le2.}
\tag{17}
$$
这并非只凭三个数值猜插值。producer 在
$\mathbf Q[x]/(\Psi_{17}/17)$ 的全部144个坐标验证(17)。

令
$$
t_0=t(v),\qquad
t_1=\frac{\alpha}{\ell(v)}t(\tau v),\qquad
t_2=\frac{\alpha^2}{\ell(v)\ell(\tau v)}t(\tau^2v).
\tag{18}
$$
于是 $T_r=h\,t_r$ 对 $r=0,1,2$ 成立。
同一 $H_{32}$ 固定域由 $h$ 生成，(16)说明
$\sigma^3$ 正是该域上的 $\mu_3$ 作用，故
$$
T_{r+3}=\omega T_r.
$$
又 $\zeta_j^{-6}=\omega^2$，于是九项 Fourier 和严格缩为
$$
\sum_{r=0}^8\zeta_j^{-2r}T_r
=3h\bigl(t_0+\zeta_j^{-2}t_1+\zeta_j^{-4}t_2\bigr).
\tag{19}
$$
$h^3/2^{22}=2^{10}v$ 给
$$
\boxed{
w_j=-\frac{8192}{51}\,vG_j^2
 \bigl(t_0+\zeta_j^{-2}t_1+\zeta_j^{-4}t_2\bigr).
}
\tag{20}
$$
这里仍是原 $h$ 的绝对乘积规范，不另缩放 $h$。

## 5. 六个精确有理 Gram 值

在
$$
\mathcal L=K[V]/(V^3+367395V^2+147V+1/17),\qquad
\mathcal B=\mathcal L[Z]/(Z^3-\omega^2)
$$
中，以 $1,Z,Z^2$ 表示元素。其三个根正是原 $\zeta_j$，
所以
$$
\operatorname{Tr}_{\mathcal B/\mathcal L}(A_0+A_1Z+A_2Z^2)=3A_0.
\tag{21}
$$
记 $u_1=\ell(\tau^2v)$、$u_2=c/\ell(v)$。原三个函数在这个小代数中为
$$
\begin{aligned}
\mathscr G(Z)&=1+\frac{\omega u_2}{\alpha^2}Z
                 +\frac{\omega u_1}{\alpha}Z^2,\\
\mathscr T(Z)&=t_0+\omega t_1Z+\omega^2t_2Z^2,\\
\mathscr W(Z)&=-\frac{8192}{51}v\,\mathscr G(Z)^2\mathscr T(Z).
\end{aligned}
\tag{22}
$$
这是用 $Z^{-1}=\omega Z^2$、$Z^{-2}=\omega Z$ 得到的原式，
不是改换角色。

令
$$
e_0(Z)=1,\quad e_1(Z)=Z+\omega Z^2,\quad
e_2(Z)=\omega Z+Z^2.
$$
相对于 $\mathcal B_E$ 的 Gram 矩阵准确为
$$
\boxed{
Q_{ab}=\operatorname{Tr}_{\mathcal B/\mathcal L}
  \bigl(\mathscr W e_ae_b\bigr)
=3[Z^0]\bigl(\mathscr W e_ae_b\bmod Z^3-\omega^2\bigr).
}
\tag{23}
$$
producer 首先要求(23)的 $V,V^2$ 系数均为0，再要求剩余
$K$ 元素的 $\omega$ 系数为0。因此每个有理值是精确消元的结果，
而非球区间的有理重建或四舍五入。

几何上其有理性亦有独立理由。R862 的原 Hom 定理给共同整数
$m>0$，使三条 $\Xi_0e_a$ 都在乘 $m$ 后成为实际 $F$-Hom。
以原 Jacobian 与 $C_v$ 的主极化定义配对，
$$
Q_{ab}=\frac1{m^2}\,[\, (m\Xi_0e_a)_*(m\Xi_0e_b)^*\,].
\tag{24}
$$
因 $[F:\mathbf Q]=3$，$F$ 不含 $K$，
所以 $\operatorname{End}_F(C_v)=\mathbf Z$，
括号确为整数。
(24)与复微分积分的极化恒等式给同一(23)。
没有用只有 Betti 意义的同构来宣称整格相同。

更一般，若 $f=\Xi_0u$ 是实际 $F$-Hom，
原 $\mathscr R$ 及其整多项式给 $f\mathcal O_E$ 的全部实际 Hom，
从而
$$
\boxed{Q|_{u\mathcal O_E}\text{ 的整个 Gram 矩阵均为整数。}}
\tag{25}
$$
(25)比只要求一个度数是整数更强，仍然只是必要条件。
它与 R874 的整 $q$ 理想结合使用，不代替椭圆方程证书。

## 6. 原候选与完整逆 Hecke 返回

保持 R874 公开计算所得的同一候选
$$
u=\frac{915+1097\vartheta+2962(\vartheta^2-2)}{55569},
\qquad N_{E/\mathbf Q}u=-\frac{17}{55569}.
\tag{26}
$$
它生成 R874 的完整整 $q$ 分数理想，并有
$$
\lambda(u)=\frac{68+7a-13a^2}{3},\qquad a^3=17,
$$
$$
\boxed{\frac{17}{u}=106+59\vartheta+185(\vartheta^2-2)\in\mathcal O_E.}
\tag{27}
$$
本篇 producer 用(23)准确输出 $q(u)$ 与整个
$u\mathcal O_E$ 的 Gram；
并在精确数域里重新检查(26)、(27)及原9个整 $q$ 条件。

R874 的球区间接近376，本篇不从该事实断言精确值。
只有公开运行对(23)的有限代数验证完成，才能将其输出登记为
精确准度数。即使输出是整数，也不能因此称 $\Xi_0u$ 已是整 Hom：
R870 的全椭圆恒等式或另一完整整性证明仍须支付。
一旦实际坐标证明成功，(27)才准确返回原 $17\Xi_0$，
以及 R867 的其它原 Hom 与原端点 Artin 组合。

## 7. 公开 producer 与认证范围

脚本：
```
scripts/check-r875-original-exact-eisenstein-degree-gram.py
```
在固定 Sage 镜像中无参数运行：
```
sage -python scripts/check-r875-original-exact-eisenstein-degree-gram.py
```

它不读取旧输出表，顺次执行：

1. 从 $E_0$ 生成原 $\Psi_{17}$，核次数144、首系数17、
   常数 $-2^{96}$；用
   $x([\delta]P)=-(x(P)^3+4)/(3x(P)^2)$
   在同16项轨道同时生成 $h$ 与 $T_0$。
2. 在全部144个坐标中解出并核验(17)；
   不只比较前几个系数或一个复嵌入。
3. 用 R864 的实际七范数有理映射逐项核
   $\sigma(h)=\alpha h/\ell$ 与 $T_0$ 的同源变换，
   防止把 $\sigma$ 换成其逆。
4. 在三元数组代数中执行(21)–(23)，强制六项完整下降到
   $\mathbf Q$，并核正定性。
5. 输出原准度数、完整 Gram、同一候选理想基的 Gram、
   原候选精确度数、9个整 $q$ 坐标和(27)的整数回送。
   不把任何一步自动升级为实际 Hom。
6. 大的144维分点向量只输出 SHA256；仓库只保脚本、
   参数、真实 run 和输出 hash，不保可重算数据。

## 8. 原文与同源引用

- [R862](R862-original-seventeen-torsion-product-and-complete-cubic-hom-matrix.md)、
  [R864](R864-original-seventeen-torsion-exact-field-and-cocycle.md)：
  原17挠点、满像、$h$、定向 $\ell,\tau$ 与原三条 Hom。
- [R869](R869-original-modular-input-and-cubic-field-descent.md)：
  同一 $H_0,\Xi_0$ 到 $F$ 的下降。
- [R873](R873-original-cm-petersson-norms-and-integral-hom-degree-bounds.md)：
  原完整 $B_j$、3/17 Euler、面积及(4)的常数。
- [R874](R874-original-cusp-integral-hecke-ideal-and-low-degree-return.md)：
  完整整 $q$ 理想、原候选及实际逆 Hecke。
- K. Khuri-Makdisi, *Moduli interpretation of Eisenstein series*,
  International Journal of Number Theory **8** (2012), 715–748；
  [作者 arXiv v6](https://arxiv.org/pdf/0903.1439)，
  §2 定义2.1、(2.1)–(2.2)、Remark2.5，
  §3 印页8式(3.5)。
  本篇只引用原 Hecke 正则化和分点 $x$ 坐标恒等式；
  原角色、真实周期、全部有限常数和(20)–(27)在上文自行推导。

本篇把严格解析范数变为同一原17分点代数中的可验证有理数。
原候选的实际坐标与原 shadow 的非零，仍由后续完整来源证书处理。


## 9. 公开精确结果：原 Gram 和候选理想 Gram

**已证明（有限代数证书）。** 源提交
`247d0b4114f2087f52f83422692c4caba7079fc5`，
[run43835263367](https://github.com/Rogerhu12/math-research-public/actions/runs/43835263367)、
job133190184002，于2026-11-16 08:56:59 UTC完成；
Sage10.6，无参数，精确部分21.105572414秒。
完整输出SHA256为
`52a7062047848ae5dc88ca5f943d875be4245a02aac58b6ad4a0ab5d37ce5468`，
脚本SHA256为
`bb9fa2ef4d385003cef3f0cc27e5d5f5d72cffb95803073aed73e74f77f184a0`。
固定镜像及原分点多项式、$h,T_0$ 的哈希在同次公开日志；
只保数学结论，不保存可重算输出表。

(17)中的多项式准确是
$$
\boxed{
t(V)=\frac{53529481}{967311360}
 +\frac{74139759899}{483655680}V
 +\frac{403597}{967311360}V^2.
}
\tag{28}
$$
原 $\mathcal B_E$ 上的有理 Gram 为
$$
\boxed{
Q=\frac1{17}
\begin{pmatrix}
1389480&-355512&100464\\
-355512&2879424&-1744992\\
100464&-1744992&3034008
\end{pmatrix}.
}
\tag{29}
$$
因此原 $q(1)=1389480/17$ 是准确准度数；
这由(23)的全代数下降证明，没有由R873的小球作有理识别。

在 R874 的整 q 理想基 $u(1,\vartheta,\vartheta^2-2)$ 上，
$$
\boxed{
Q_I=
\begin{pmatrix}
376&-40&-88\\
-40&664&-416\\
-88&-416&880
\end{pmatrix},\qquad
\det Q_I=145156608.
}
\tag{30}
$$
其所有条目确为整数，故(25)没有排除本候选。
特别
$$
\boxed{q(u)=376.}
\tag{31}
$$
(31)仍只称准度数；它没有认证原函数坐标或全 Hom 格。
原 $q$ 整性、(27)的返回17以及所有原尺度继续完整保留。

## 10. 整个必要理想的准确最小准度数

(30)还直接证明一个全格结论，无需另作有限向量扫描：
$$
\boxed{\min_{0\ne v\in I_\infty}q(v)=376.}
\tag{32}
$$

证明如下。R874的理想生成结论给
$v=u e$、$e\in\mathcal O_E\setminus\{0\}$，
所以 $|N(e)|\ge1$。
原三正权的AM–GM界与
$\operatorname{disc}\mathcal B_E=81$ 给
$$
q(v)^3\ge
27w_0w_1w_2|N(u)|^2
=\frac{\det Q_I}{3}
=48385536>360^3.
\tag{33}
$$
因此 $q(v)>360$。
另一方面(30)的每项都被8整除，故 $q(v)\in8\mathbf Z$。
写 $e=x+y\vartheta+z(\vartheta^2-2)$，则
$$
\frac{q(ue)}8
=47x^2+83y^2+110z^2-10xy-22xz-104yz
\equiv2(x-y-z)^2\pmod3.
\tag{34}
$$
(33)以上的第一个8倍数是368，但 $368/8=46\equiv1\bmod3$，
不可能满足(34)。所以 $q(v)\ge376$，
而(31)在 $v=u$ 达到该值，证明(32)。

这是对全部分数理想的严格最小值，不依赖R874有限LLL窗口。
任何该 packet 的实际非零 Hom 因必要整 q 条件也有度数至少376；
最小准方向是否已是实际 Hom，仍须正在运行的完整坐标证书。
