# R1135：原 Gaussian 两个低行的有限纤维约束

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明，纯纸面。** 本结论使用完整原 $X_{\rm ns}^+(p)$ 的实际 good 角色。
在 $p=4k+3\ge41$ 且 $p\mid B_{p-7},B_{p-11}$ 的分支中，
同一原 marked Gaussian frame 内，所有非对角共同纤维的无序点对至多一个。
该候选由两条明确公式给出，仍需原其余 good 行排除。
另一分支 $p\mid B_{p-7}$、$p\nmid B_{p-5}$ 有一个明确的
degree-one 行组合，其斜率的单位性仍开放。

这里的 $p\mid B_n$ 指 $p$ 整有理数 $B_n$ 为非单位。
没有将 Bernoulli 非单位等同于 Gaussian Hurwitz 系数非单位。
不声称两个 twist frame 合并后至多一个点对，也不声称原圆盘内点已排除。

## 1. 实际输入与完整低行

保持 [R1116](R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)
及 [有限本征重建](../notes/2026-11-28-original-Gaussian-finite-contiguity-and-spectral-reconstruction.md)
的同一规范：
$$
E_a:y^2=x^3+ax,\quad a\in\mathbf F_p^\times,\quad
D\Psi=\delta\in\mathbf F_p^\times,\qquad
\mathscr K(T,U)=T^{-1}+U^{-1}+\sum_{\ell\ge1}P_\ell(T,U),
$$
其中 $P_\ell$ 对称、总次数 $4\ell-1$。同一 centered 总次数 $p$ 层为
$$
M_w=\sum_{h=1}^{k}\frac{w^{2h}}{(2h)!}
 (TU)^{2h}P_{k+1-h}
+\frac{w^{2k+2}}{(2k+2)!}(TU)^{2k+2}(T^{-1}+U^{-1}).
\tag{1135.1}
$$
实际 good 集合及 centered 标签是
$$
\mathcal G_p=\{R:\ 2\le R\le p-3,\ R\ {\rm even},\
 V_{\omega^R}\ne0,\ p\nmid B_R\},\qquad
\Pi_R(z)=N_R\mathcal A_R(\gamma^2z),
\tag{1135.2}
$$
$$
\mathcal A_R(w^2)=[T^{p-R}U^R]M_w,\qquad
\gamma=\delta\lambda\beta_0^{1-p},\qquad
N_R=\frac{(\beta_0^{p+1})^R\delta^{R-1}}{2b_{\omega^R}R!}.
$$
所有尺度均为原来源的单位。比较同一 frame 的两点时，$N_R$ 共同；
跨 frame 时未作未经证明的归一。

写
$$
c_s=[T^{p-4-s}U^s]P_k,\qquad
d_s=[T^{p-8-s}U^s]P_{k-1},\qquad Z=w^2.
$$
(1135.1) 中 $h$ 的支撑立即给完整行
$$
\mathcal A_4(Z)=\frac{c_2}{2}Z-\frac{G_{p-7}}{24}Z^2,\qquad
\mathcal A_6(Z)=\frac{c_4}{2}Z+\frac{d_2}{24}Z^2
                     -\frac{G_{p-11}}{720}Z^3.
\tag{1135.3}
$$
证明中使用 $[U^0]P_\ell(T,U)=-G_{4\ell}T^{4\ell-1}$，
这是原 sigma 核的 $\zeta(T)$ 轴项。更高 $h$ 的最低 $U$ 次数已超过
$4$ 或 $6$；最高 principal 亦不贡献。因此没有遗漏高尾。

原方程 $x''=6x^2+2a$ 给
$$
G_8=\frac{a^2}{525},\qquad G_{12}=-\frac{2a^3}{53625}.
$$
把它们代入 R1116 已付的准确反射
$G_{p+1-r}=-(r-1)!\delta^{1-r}G_r$，得到
$$
G_{p-7}=-\frac{48a^2}{5\delta^7},\qquad
G_{p-11}=\frac{96768a^3}{65\delta^{11}}.
\tag{1135.4}
$$
两者对本范围全部为单位；$96768=2^9 3^3 7$。
只使用 $r=8,12\le p-3$，没有外推未付的高权层。

## 2. 双低指标分支：至多一个无序点对

[R1128](R1128-all-prime-linear-good-cuspidal-rank.md) 的实际低角色判据给
$$
p\mid B_{p-7}\Longrightarrow 4\in\mathcal G_p,\qquad
p\mid B_{p-11}\Longrightarrow 6\in\mathcal G_p.
\tag{1135.5}
$$
因为 $B_4=-1/30$、$B_6=1/42$ 在 $p\ge41$ 为单位，
这里确是原出现且 good 的两个角色。

假设两条件同时成立，并令同一原 frame 的两个不同实际点对应
$Z,Z'$。若全部实际 good 坐标相等，令
$S=Z+Z'$、$P=ZZ'$。第一条 (1135.3) 的差除以 $Z-Z'$ 给
$c_2/2-G_{p-7}S/24=0$；第二条给
$c_4/2+d_2S/24-G_{p-11}(S^2-P)/720=0$。
由 (1135.4) 可以准确反除，所以
$$
\boxed{\quad
 S=\frac{12c_2}{G_{p-7}},\qquad
 P=S^2-\frac{30d_2S+360c_4}{G_{p-11}}.\quad}
\tag{1135.6}
$$
因此非对角共同纤维若存在，其无序点对只能是
$X^2-SX+P$ 的两个根，至多一对。

这还是必要条件。须进一步检查判别式非零、两个根属于原实际范围，
并代入所有其余 $R\in\mathcal G_p$ 的原标签。
$P=0$ 和尚未排除的 $S=0$ 均保留。
尤其没有把两条 twist line 的合并范围替换为单条 fine 平方像。

## 3. 一低一高分支：原固定 affine minor

假设 $p\mid B_{p-7}$、$p\nmid B_{p-5}$。
低 $R=4$ 由 (1135.5) 实际出现；$R=p-5$ 是原 forced 角色，
且在本假设下 good。由 $P_\ell$ 对称与原支撑，
$$
\mathcal A_{p-5}(Z)=\frac{c_3}{2}Z+\frac{d_1}{24}Z^2.
\tag{1135.7}
$$
这与第一条 (1135.3) 的准确组合是
$$
d_1\frac{\Pi_4(z)}{N_4}
 +G_{p-7}\frac{\Pi_{p-5}(z)}{N_{p-5}}
 =\frac{\Delta_{\rm low}}2\gamma^2z,\qquad
\Delta_{\rm low}=c_2d_1+G_{p-7}c_3.
\tag{1135.8}
$$
两行的系数矩阵行列式恰为 $\Delta_{\rm low}/48$。
故若 $\Delta_{\rm low}\ne0$，这两个真实行已分离同一 frame 的点。
若 $\Delta_{\rm low}=0$，则完整行严格比例
$$
\mathcal A_{p-5}=-(d_1/G_{p-7})\mathcal A_4.
$$
本篇没有证明 $\Delta_{\rm low}$ 为单位，后续必须处理这个准确退化支。
不以“两条都出现”替代行独立，也不添未出现或非 good 的角色。

## 4. 来源、验证与范围

全部是上述完整核的有限系数恒等式及 R1128 的实际 mask 判据。
root 与 o1_theta 已纸核两条反射、完整支撑、消元与作用域；
没有数学程序执行，没有新增数值窗口。
同一来源的 Newton 节点、完整 good 余核及其固定非观测值
见所引有限重建笔记 §§7–9。后续继续原 $\Delta_{\rm low}$、
唯一剩余点对的其余实际行以及两 twist 的准确运输。


## 5. 原二挠平移给三条完整 Appell 乘积身份

本节仍使用 R1114 的同一个原 Gaussian CM lift、微分
$\omega=dx/(2y)$ 和 tangent-one additive 参数 $t$。
先在 characteristic zero 作恒等式，再只约化下述安全系数。
记 $Q=(0,0)$、$i^2=-1$、$\lambda=1+i$，并置
$$
x_Q(t)=x(t+Q)=a/x(t),\qquad
\zeta_Q(t)=\zeta(t+Q)-\zeta(Q)=\zeta(t)+y(t)/x(t).
\tag{1135.9}
$$
这里 $\lambda$ 是原 CM 同源，不是 (1135.2) 中的节点尺度。
原二挠加法律及 $1+i$ 同源给
$$
\lambda\zeta(\lambda t)=\zeta+\zeta_Q,\qquad
\lambda^2x(\lambda t)=x+x_Q=(\zeta-\zeta_Q)^2,\qquad
xx_Q=a.
$$
所有平移常数已经由 (1135.9) 固定。

定义原 Kronecker 核的三个 Appell 列
$$
\begin{aligned}
C_2&=\zeta^2-x,\\
C_3&=\zeta^3-3x\zeta-2y,\\
C_4&=\zeta^4-6x\zeta^2-8y\zeta-3x^2-\frac{12a}{5},
\qquad C_{2,Q}=\zeta_Q^2-x_Q.
\end{aligned}
\tag{1135.10}
$$
特别，$C_4$ 保留原 sigma 分母给的 $-12a/5$；
它是 $\sigma''''/\sigma-2a/5$，不是单独的
$\sigma''''/\sigma$。原核展开为
$$
\mathscr K(t,U)=U^{-1}+\zeta(t)
+\frac{C_2(t)}2U+\frac{C_3(t)}6U^2+\frac{C_4(t)}{24}U^3+O(U^4).
$$

由 (1135.9) 直接得到完整身份
$$
\boxed{\begin{aligned}
C_2(\lambda t)&=-2i\,\zeta\zeta_Q,\\
C_3(\lambda t)&=-\lambda(\zeta_QC_2+\zeta C_{2,Q}),\\
C_4(\lambda t)&=\frac{8a}{5}-4C_2C_{2,Q}.
\end{aligned}}
\tag{1135.11}
$$
第一式由两平方之差给出。第二式对第一式求导，并用
$C_2'=C_3-\zeta C_2$、$\zeta'=-x$、
$\zeta_Q'=-x_Q$。第三式使用准确的
$C_4=4\zeta C_3-3C_2^2-12a/5$；
代入前两式后，剩余常数是
$4xx_Q-12a/5=8a/5$。因此没有删去较低乘积。

特征 $p=4k+3$ 下 $\lambda^{p+1}=2$，所以
$$
\lambda^{p-7}=\frac18,\qquad
\lambda^{p-6}=\frac{\lambda}{8},\qquad
\lambda^{p-9}=-\frac{i}{16}.
$$
分别读取原 (1135.3)、(1135.7) 所需系数，得到
$$
\boxed{\begin{aligned}
c_2&=-\frac43[t^{p-6}](\zeta_QC_2+\zeta C_{2,Q}),\\
c_3&=-\frac43[t^{p-7}]C_2C_{2,Q},\\
d_1&=16[t^{p-9}]\zeta\zeta_Q .
\end{aligned}}
\tag{1135.12}
$$
例如 $24c_3=[t^{p-7}]C_4$，且 $p-7>0$，
故 (1135.11) 的常数 $8a/5$ 不贡献这次读取。
三式都保留完整原乘积，不把它们当作独立的单位输入。

## 6. 原 $u$ 残数使三余项准确降为两余项

沿 R1114 (1114.5)–(1114.7)，写
$$
\begin{gathered}
u=x^{-1/2}=t+O(t^5),\quad z=-au^4,\quad
R(z)=(1-z)^{-1/2},\\
F(z)={}_2F_1\left(\frac14,\frac12;\frac54;z\right),\qquad
G(z)={}_2F_1\left(\frac34,\frac12;\frac74;z\right),\\
t=uF(z),\quad dt=R(z)\,du,\quad
\zeta=\frac{R(z)^{-1}}u-\frac{au^3}{3}G(z),\quad
\zeta_Q=-\frac{au^3}{3}G(z).
\end{gathered}
\tag{1135.13}
$$
这里 $G(z)$ 是原第二类积分的函数；
$G_{p-3}$ 仍表示原 Hurwitz 数。二者不混用。
最后两式正是 R1114 中已经固定常数的
$\zeta+y/x=-a\int_0^u s^2(1+as^4)^{-1/2}\,ds$。

因此
$$
C_2=au^2-\frac{2a}{3}u^2R^{-1}G+\frac{a^2}{9}u^6G^2,\qquad
C_{2,Q}=-au^2+\frac{a^2}{9}u^6G^2.
$$
相乘时两条 $a^3u^8G^2/9$ 严格相消，准确剩下
$$
\boxed{
C_2C_{2,Q}
=-a^2u^4+\frac{2a^2}{3}u^4R^{-1}G
-\frac{2a^3}{27}u^8R^{-1}G^3
+\frac{a^4}{81}u^{12}G^4 .
}
\tag{1135.14}
$$
这一消去发生在同一原函数乘积内，不使用任何非零猜测。

令 $M=p-7$。对本式的正规幂级数作真实残数换元：
$$
[t^M]C_2C_{2,Q}
=[u^M]C_2(u)C_{2,Q}(u)F(z)^{6-p}R(z)
=[u^M]C_2(u)C_{2,Q}(u)F(z)^6R(z)\pmod p.
\tag{1135.15}
$$
最后一步只用于此次 $M<p$ 的安全前缀。
所有需要的 $F,G$ 系数最多到 $z^{k-1}$；
由 R1114 (1114.6)，其分母 $4j+1,4j+3,j!$ 均为单位。
未读取 $[z^k]G$ 的首个 $p$ 分母。
在该前缀内 $F^{-p}\equiv1$，且乘积 (1135.14) 从 $u^4$ 起，
故没有高项回流。原整 eigenparameter 与 additive $t$ 的差
同样远高于这里的次数。

为与 R1114 §7 的三个原卷积逐字对齐，令
$$
\begin{aligned}
\mathcal K_p&=[u^{p-11}]F(-au^4)^6G(-au^4),\\
\mathcal V_2&=[u^{p-15}]F(-au^4)^6R(-au^4)G(-au^4)^2,\\
\mathcal V_3&=[u^{p-15}]F(-au^4)^6G(-au^4)^3,\\
\mathcal V_4&=[u^{p-19}]F(-au^4)^6R(-au^4)G(-au^4)^4,\\
\mathcal H_p&=[t^{p-5}]C_2(t),\qquad g=G_{p-3}.
\end{aligned}
\tag{1135.16}
$$
R1114 (1114.23)、(1114.31) 已支付同源的
$$
[u^{p-11}]F^6R=[t^{p-7}]x^{-2}=30a^{-2}g,\qquad
5\mathcal H_p+\frac{8a^2}{45}\mathcal K_p=16g,\qquad
g=\frac{2a}{5\delta^3}\ne0.
$$
将 (1135.14) 全部代入 (1135.12)、(1135.15)，得
$$
\boxed{\begin{aligned}
c_3
&=40g-\frac{8a^2}{9}\mathcal K_p
       +\frac{8a^3}{81}\mathcal V_3-\frac{4a^4}{243}\mathcal V_4\\
&=-40g+25\mathcal H_p
       +\frac{8a^3}{81}\mathcal V_3-\frac{4a^4}{243}\mathcal V_4 .
\end{aligned}}
\tag{1135.17}
$$
这是真正去掉 $\mathcal V_2$ 的完整原系数身份。
与 R1114 (1114.39) 比较，也可精确写出被消去项：
$$
\boxed{
\mathcal V_2
=-\frac{1305}{a^3}g+\frac{3375}{4a^3}\mathcal H_p
 +\frac{34}{9}\mathcal V_3-\frac{11a}{18}\mathcal V_4 .
}
\tag{1135.18}
$$
两种写法完全等价，不另引入新的 primitive 或 frame。

## 7. 新身份支付的范围

(1135.11)–(1135.18) 只消费同一原 sigma 核、
二挠平移及 R1114 的安全残数。本节由 o2_high_coefficient 推导，
o1_theta 已独立纸核三条 norm-two 身份、原 $1/2,1/6,1/24$ 列尺度以及
(1135.14) 的完整乘积消去；没有数学程序执行。

在 $\mathcal H_p=0$ 支，(1135.17) 仍有
$\mathcal V_3,\mathcal V_4$ 两个余项。不能从 $g$ 为单位
断言 $c_3$ 为单位，也未证明 (1135.8) 的
$\Delta_{\rm low}=c_2d_1+G_{p-7}c_3$ 非零。
使用这些列作原标签的分离时，仍须保留 §3 的实际 Bernoulli mask、
全部较低乘积，以及两条 twist frame 的准确运输。


## 8. 另外两条二同源：完整核与原 CM 第二类框架

本节用另一条真实辅助同源检查 §6 的两个余项，不把新曲线上的
标准 Weierstrass 系数直接当作原 marked 读数。
取 $e^2=-a$，$Q_e=(e,0)$；同时允许 $e=0$ 表示旧 $Q$。
置 $d_e=3e^2+a$。原二挠加法律为
$$
x_{Q_e}=e+\frac{d_e}{x-e},\qquad
m_e=\frac y{x-e},\qquad
Dm_e=x-x_{Q_e}.
\tag{1135.19}
$$
normalized degree-two quotient $q_e:E_a\to E_e$ 的坐标和微分是
$$
X=x+x_{Q_e}-e,\qquad Y=\frac12DX,\qquad
q_e^*\frac{dX}{2Y}=\omega.
$$
因此
$$
E_e:Y^2=X^3+A_eX+B_e,\quad
A_e=-4a-15e^2,\quad B_e=-7e(3e^2+a).
\tag{1135.20}
$$
对 $e\ne0$，这是 $(A_e,B_e)=(11a,14ae)$；
对 $e=0$，是 $(-4a,0)$。

以下所有 sigma 首项均为 $t$，所有平方根按 $t=0$ 的首项选取。
记 $\zeta_e,\sigma_e,\mathscr K_e$ 为 $E_e$ 的标准 Weierstrass 数据，
并写
$$
\zeta_{Q_e}=\zeta(t+Q_e)-\zeta(Q_e)=\zeta+m_e .
$$
由 (1135.19) 求导并比较 $O$ 首项，严格得到
$$
\zeta_e(t)=\zeta(t)+\zeta_{Q_e}(t)+et,\qquad
\sigma_e(t)=e^{et^2/2}\sigma(t)^2\sqrt{x(t)-e}.
\tag{1135.21}
$$
这里 $et$ 及 $e^{et^2/2}$ 不能删除。

原 CM 第二类框架有一个同源的定标：
$$
q_e^*((X+e)\omega_e)=2x\omega-dm_e.
\tag{1135.22}
$$
所以它对应
$\widehat\zeta_e=\zeta_e-et$、
$\widehat\sigma_e=e^{-et^2/2}\sigma_e$。
这在 de Rham 上正运输原 Gaussian 的 CM 第二类直线；
不是在新曲线上任意选一个线性项。
相应完整核为
$$
\widehat{\mathscr K}_e(T,U)
=e^{-eTU}\mathscr K_e(T,U),\qquad
\mathscr K_{Q_e}(T,U)
=e^{-\zeta(Q_e)U}\mathscr K(T+Q_e,U)
=\mathscr K(T,U)
 \sqrt{\frac{x(T+U)-e}{x(T)-e}} .
$$
(1135.21) 给乘法分布，而同一二同源的线性分布给
$$
\boxed{\begin{aligned}
\sqrt{x(U)-e}\,\widehat{\mathscr K}_e(T,U)
 &=\mathscr K(T,U)\mathscr K_{Q_e}(T,U),\\
\widehat{\mathscr K}_e(T,U)
 &=\mathscr K(T,2U)+\mathscr K_{Q_e}(T,2U).
\end{aligned}}
\tag{1135.23}
$$
第二式可直接按 $T$ 核准：两边在 $O,Q_e$ 的全部 residues 相同；
其沿原 period $\omega_0$ 的 multiplier 都是
$\exp(2\eta_{\omega_0}U)$。
在 $Q_e$ 处使用
$\eta^{E_e}_{Q_e}=2\zeta(Q_e)+eQ_e$，恰由
$e^{-eTU}$ 消去额外相位。
generic $U$ 的这条非平凡 degree-zero line 没有全纯截面，
故差为零。再作有理/形式延拓，包含所有本文读取的系数。
因此 (1135.23) 没有遗漏一个全纯或指数补项。

$e=0$ 时
$\widehat{\mathscr K}_0=\lambda\mathscr K(\lambda T,\lambda U)$，
(1135.23) 正回原 $1+i$ 两种分布；不是另一个归一。

## 9. 完整二挠 trace 只给原偶 band 的对角运输

在同一刚化下，乘二同源的线性分布为
$$
\sum_{Q\in E[2]}\mathscr K_Q(T,2U)=2\mathscr K(2T,U),
\qquad \mathscr K_O=\mathscr K.
$$
它同样由四个二挠点的 residues、multipliers 和 $O$ 首项唯一确定。
把 (1135.23) 对三个非零二挠点求和，得到
$$
\boxed{\quad
\widehat{\mathscr K}_0+\widehat{\mathscr K}_e+
\widehat{\mathscr K}_{-e}
=2\mathscr K(T,2U)+2\mathscr K(2T,U).
\quad}
\tag{1135.24}
$$
原 CM $i$ 交换 $e,-e$，而精确的 gauge 也同时运输：
$$
\widehat{\mathscr K}_{-e}(T,U)
=i\,\widehat{\mathscr K}_e(iT,iU).
$$
所以在总次数 $4\ell-1$ 上，两者的 band 相同。
记这一 band 为 $\widehat P_{\ell,e}$。由
$\widehat{\mathscr K}_0=\lambda\mathscr K(\lambda T,\lambda U)$，
得到完整的逐系数公式
$$
\boxed{\quad
\widehat P_{\ell,e}(T,U)
=P_\ell(T,2U)+P_\ell(2T,U)
-\frac{(-4)^\ell}{2}P_\ell(T,U).
\quad}
\tag{1135.25}
$$
只在 $1\le\ell\le k$ 的原安全范围约化；
所有权不超过 $p-3$。新曲线其他 parity 的 band 不被偷偷加入。

特别，按原 $c_2,c_3,d_1$ 的指数定义相应带帽系数，并令
$h=G_{p-7}$、$\widehat h=G_{p-7}(E_e)$，则
$$
\boxed{
\widehat c_2=\frac{137}{32}c_2,\qquad
\widehat c_3=\frac{529}{64}c_3,\qquad
\widehat d_1=\frac{497}{256}d_1,\qquad
\widehat h=\frac{121}{128}h .
}
\tag{1135.26}
$$
例如最高 band 的 $U^s$ 列因子为
$2^s+2^{p-4-s}+1/4$，因为 $(-4)^k=-1/2$；
下一 band 则用 $(-4)^{k-1}=1/8$。
本式是等式，不据此反除全部因子；
当前 $p\equiv3\pmod4$、$p\ge41$ 范围内仍须保留
$p=71$ 时 $497=7\cdot71$ 给的零因子。

这也精确解释新曲线旁单位的范围。
由 (1135.22) 和 supersingular Cartier，
$\beta_e=2\beta=-2\delta$。
写 $\sigma=e^p/e\in\{\pm1\}$。
一般 SS 的完整 Frobenius 反射
$G_{p-5}(E_e)^p=120\beta_e^{p-6}G_6(E_e)$、
$G_6=-B_e/35$ 给
$$
g_e:=G_{p-5}(E_e)=\frac{3\sigma ae}{2\delta^5}\ne0.
\tag{1135.27}
$$
这里保留了 $B_e^p=\sigma B_e$；不能因原 $a\in\mathbf F_p$
就把新 $B_e$ 也当成 $\mathbf F_p$ 系数。

令标准 Weierstrass 读数
$\mathcal H_p(E_e)=[t^{p-5}](\zeta_e^2-X)$。
原 CM 框架的同一列则是
$$
\widehat{\mathcal H}_p(E_e)
=[t^{p-5}](\widehat\zeta_e^2-X)
=\mathcal H_p(E_e)+2e\,g_e.
$$
(1135.25) 在最高 band 的 $U^1$ 列准确给
$$
\boxed{\quad
\widehat{\mathcal H}_p(E_e)
=\frac{37}{16}\mathcal H_p(E_a),\qquad
\mathcal H_p(E_e)=\frac{37}{16}\mathcal H_p(E_a)-2e\,g_e .
\quad}
\tag{1135.28}
$$
所以即使 $\mathcal H_p(E_a)=0$ 时标准
$\mathcal H_p(E_e)=-2e\,g_e$ 为单位，真实 CM 框架中的该列仍为零。
新 $g_e$ 位于另一 CM parity 的高权层；
(1135.24) 没有把它运输为原 $\Delta_{\rm low}$ 的单位。

本节的结论是完整 trace 和框架补项均已结算：
仅将原偶 band 换到另外两条二同源曲线，所得仍是
(1135.25) 的对角运输，并未增加一个原共同纤维条件。
后续仍须处理同一实际 good mask 下的原行列式或剩余点对，
不把 (1135.27) 的旁读数替代它。
本节为纯纸面推导，没有数学程序执行。
