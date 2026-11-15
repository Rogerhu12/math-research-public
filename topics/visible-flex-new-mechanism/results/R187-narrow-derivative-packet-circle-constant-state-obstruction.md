# R187：R183 导数分包圆在充分共同窄化时的严格常段障碍

日期：2026-11-15。**完整纸面证明，没有新研究计算。** 来源为 [R183 的具体重叠圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R49 常段最高项不受齐次 gauge 影响](R49-fourth-ruling-leading-coefficient-and-narrow-packets.md)、[R53 完整复相位最高项及真实尾局部化](R53-overlapping-profile-fourth-leading-gate-existence.md)、[R54 常状态 Möbius 迁移](R54-constant-state-helicoid-transfer-and-first-ruling-gauge.md)。

本稿证明：R183 的具体矩形加三个左补偿 packet、再作八包平移的 profile 圆，在整个圆共同收缩得足够窄时，不能延拓至第四阶。几何只需含一个非空开常状态段；R180/R183 的有限真实拼接构造具有共同常值端口，满足这个前提。

结论不扩大到任意宽度的 R183 圆，也不扩大到所有导数分包圆。证明使用 R53 在完整三复矩为零后得到的原式，而不是按导数支撑删除嵌套原函数尾。

## 1. R183 具体补偿保留实／纯虚导数方向

在 R183 的矩形基本 profile 中，

$$
f_0=s_1-s_3,\qquad g_0=s_2-s_4,\qquad q_0=f_0+ig_0,
$$

四个导数包互不相交，分别沿实、纯虚、实、纯虚方向。因此逐点

$$f_0'g_0'=f_0''g_0''=0,$$

三个普通复平方总矩

$$
M_0(q_0)=\int(q_0'')^2,\quad
M_1(q_0)=\int\xi(q_0'')^2,\quad
M_2(q_0)=\int\xi^2(q_0'')^2+2\int(q_0')^2
$$

都是实数。R183 左补偿的矩阵为实可逆矩阵，故唯一解 $z_j$ 也全为实数。每个 $\beta_j^2=z_j$ 可取实或纯虚平方根；事实上任何该方程的复平方根都属于这两类。零系数不产生额外方向。

加入三个互不交补偿包后，所有正阶导数仍逐包沿实或纯虚方向。随后八个完整包的平移、非零实幅度 $a_j=(-1)^j\binom7j^{1/3}$ 及共同实归一化保留该性质。

把这一个固定、已完整三矩配平的 raw profile 记作

$$q_{\rm raw}=f_{\rm raw}+ig_{\rm raw}.$$

于是

$$
\boxed{
q_{\rm raw}''(\xi)\text{ 在每一点为实数或纯虚数},\qquad
I_4:=\int(q_{\rm raw}'')^4
=\int\bigl((f_{\rm raw}'')^4+(g_{\rm raw}'')^4\bigr)>0.} \tag{1}
$$

严格正性只用 raw 圆非零且紧支撑。这里并未说 $f_{\rm raw},g_{\rm raw}$ 的值或支撑不交；它们仍有 R183 的三个射影平台，不能由常数 GL(2) 换基变成不交 profiles。

## 2. 标准常状态上的完整 pure 最高次

先取 $(k,h,\omega)=(0,1,0)$ 常状态，令 $x=\xi$、$Q=1+x^2$。对于满足三个复零矩的任意复 profile q，R53 定义

$$
V=\mathcal R_0(q,q),\qquad
\mathcal F(q)=E(V,V)+2E(q,\mathcal R_0(q,V)).
$$

在整个 fourth ruling 的空间 $\sigma^2$ 系数中，相位 $e^{-4i\theta}$ 的复幅为

$$K_4=-\frac18\mathcal F(q). \tag{2}$$

全部乘法都是普通复双线性乘法。R53 的真实尾消去给

$$
\mathcal F(q)=\frac1{128}\int
\mathcal Q(x,q,q',q'')\,dx, \tag{3}
$$

$$
\begin{aligned}
\mathcal Q(x,z,p,r)={}&
2Qr^2\left[
\left(z-xp+\frac{x^2-1}{6}r\right)^2
+\left(p-\frac x3r\right)^2\right]\\
&+\frac{Q^3r^4}{36}
+4p^2\left(z-\frac x3p\right)^2
+\frac{2(x^2+3)}9p^4 .
\end{aligned} \tag{4}
$$

三个原复矩使真实总尾为零，才允许使用 (3)。该身份保留 $\mathcal R_0$ 的左仿射尾及其嵌套作用；不要求 $f,g$ 不交，也不要求二阶 cross forcing 为零。

式 (4) 中 $r^4$ 的总系数是

$$
2Q\left(\frac{(x^2-1)^2}{36}+\frac{x^2}{9}\right)
+\frac{Q^3}{36}=\frac{Q^3}{12}. \tag{5}
$$

这只是最高导数项的系数，不是把普通复平方变成正模平方。

## 3. 共同窄化的严格非零首项

固定一个物理内部点 c，令

$$q_\lambda(\xi)=q_{\rm raw}\!\left(\frac{\xi-c}{\lambda}\right),
\qquad\lambda>0. \tag{6}$$

三个复零矩在共同仿射变换下仍准确为零。固定 raw 支撑后，取 $\lambda$ 足够小就可保持同一物理区间及双 collar。

将 $\xi=c+\lambda y$ 代入 (3)–(5)。四个二阶导数给 $\lambda^{-8}$，积分给 $\lambda$；其余项的总导数阶数至多七。因此

$$
\boxed{
\mathcal F(q_\lambda)
=\frac{(1+c^2)^3}{1536\,\lambda^7}I_4
+O(\lambda^{-6}).} \tag{7}
$$

余项是固定 raw profile 的有限导数积分乘光滑几何系数的组合；在固定 raw 支撑上有统一界。由 (1)，

$$
\operatorname{Re}\mathcal F(q_\lambda)>0
\quad\text{对全部充分小的正 }\lambda. \tag{8}
$$

虚部的首项为零不影响结论。故 (2) 的 real pure 最高次不为零，全部相位的 $\sigma^2$ 条件不可能同时成立。

若还要求 $\int(f_\lambda'')^2=1$，可以同乘实正幅度 $\rho_\lambda$。四阶量乘 $\rho_\lambda^4>0$，所以严格符号保持。特别地，I0 归一时 $\rho_\lambda$ 为固定正常数乘 $\lambda^{3/2}$，首项阶数改为 $\lambda^{-1}$；不能把未归一的 $\lambda^{-7}$ 幅度冒给归一圆。

## 4. 任意固定常状态上的准确正因子

现固定任意常状态 $(k,h,\omega)$，其中 $h>0$。在共同物理点 c 令

$$
e_c=h(c+\omega)-k,\qquad
a=\sqrt{1+k^2},\qquad D_c=1-ke_c.
$$

先取 $D_c\ne0$，以便 R54 的标准图在窄化支撑上有效。有限多个常状态只有有限个需避开的点，故这与选共同内部 c 兼容。

R54 的迁移是

$$
x=\frac{e+k}{1-ke},\qquad
\psi(x)=\frac{(1+kx)^2}{a}\,q(\xi(x)),
\qquad e=h(\xi+\omega)-k. \tag{9}
$$

在中心 c 记 $x_c=(e_c+k)/D_c$。准确有

$$
x'_c=\frac{ha^2}{D_c^2}>0,\qquad
C_c:=\frac{(1+kx_c)^2}{a}=\frac{a^3}{D_c^2},
$$

$$1+x_c^2=\frac{a^2(1+e_c^2)}{D_c^2}. \tag{10}$$

迁移后的 $\psi_\lambda$ 不必逐点保持实／纯虚导数；本证明只取其真正主项。用原 raw 变量 y 参数化迁移后的积分，

$$
\psi_\lambda''=
\frac{C_c}{(x'_c)^2\lambda^2}q_{\rm raw}''(y)
+O(\lambda^{-1}),\qquad
dx=\lambda(x'_c+O(\lambda))\,dy.
$$

所以标准 $\mathcal F$ 的首项系数为

$$
\frac{(1+x_c^2)^3C_c^4}{1536(x'_c)^7}
=\frac{a^4(1+e_c^2)^3}{1536h^7}. \tag{11}
$$

原三复矩保证该状态 $E_{\rm orig}(q,q)=0$；R54 的 $E_{\rm orig}=(h^2/a^2)E_{\rm standard}$ 因而支付迁移后 (3) 所需的总尾条件。没有假定迁移后另外两个标准矩也分别为零。

原 fourth ruling 的 $\sigma^2$ 系数是标准值乘 $h^2$。因此原相位最高次复幅满足

$$
\boxed{
K_{4,\rm orig}(q_\lambda)
=-\frac{(1+k^2)^2(1+e_c^2)^3}
{12288\,h^5\,\lambda^7}\,I_4
+O(\lambda^{-6}).} \tag{12}
$$

其 real 首系数严格负。这个推导只使用真实坐标迁移及已证明的完整 R53 公式；没有忽略常段入历史，也没有以不同状态各选一个新 profile。

若给定有限多个常状态，可在共同 c 避开它们的图极点后，取一个统一小 $\lambda$ 使 (12) 在每个状态都非零。实际上只要一个非空常段就足够排除第四 range。

## 5. 为什么 R180–R185 的全部 gauge 不能改变这个门

在常段上，以 $\sigma=s-s_0$ 记真实空间参数。二阶恢复的最高项是一次，三阶恢复的最高项是二次。任意同 collar 二阶齐次 profile $Y_{w_\theta}$ 在该旋转标架中只改变二阶常数项；其真实第三补偿 $2Z_B(\phi_\theta,w_\theta)$ 至多一次。第三齐次 profile 同样只改变常数项。

因此任意允许的二、三阶 gauge 只能改变 fourth ruling 的 $\sigma^1,\sigma^0$ 项，不能改变 $\sigma^2$ 项。这包括 R184 的整个光滑相位定义域，不只 R180 的仿射斜率或 R185 的十个方向。

常段上的 $\mathcal W$ 由常值几何三列生成，限制到该段只含常函数。故 (12) 不为零意味着 fourth ruling 不可能落在 $\mathcal W$，R184 的完整联合条件必失败。即使另有办法把整个 fourth period 清零，这个 ruling 障碍仍在。

## 6. 对具体构造的范围与下一分支

R180/R183 的有限真实路径在拼接处具有共同常值 scalar germs，故包含非空常状态开区间。固定这条几何之后，把 R183 的整个 raw 圆共同窄化得足够小，就落入上述排除范围。已经完整支付的二、三阶 range、真正重叠性、不可换基成不交、六矩右逆与有符号周期线仍都成立；这些事实不与第四阶失败矛盾。

本稿没有证明任意宽度的 $\operatorname{Re}\mathcal F$ 都有定号。式 (4) 的低导数混合项在重叠平台上仍有真实贡献，不能仅由 (1) 就把它们全部宣为正。也没有排除使用非轴向复导数 packet 的不同圆，或没有开常状态段的不同几何。

因此，当前充分窄化的 R183 类不应再作为第四完整求解的数值候选。剩余有意义的纸面问题是全宽度的完整符号、改变导数相位设计后同时支付实际常状态门，或准确构造不含常状态开段的几何。任何后继真实研究计算都须先说明它离开了本稿已排除的范围。

