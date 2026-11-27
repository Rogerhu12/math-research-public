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
§10 进一步支付两种实际 twist 的公共规范，将纤维约束提升至同一原
Gaussian coarse component 的全部下降支路；仍不声称原圆盘内点已排除。

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


## 10. 两种实际 Gaussian 下降线的完整归一化运输

本节补齐 §2 保留的跨 frame 比较。结论只涉及同一个原
Gaussian coarse component；不把不同 supersingular components
或其它 level 标记合并。

### 10.1 构造原另一 twist，而非假设给定 $\mathbf F_p$ 同构

R1066 §4.3、R1071 §8 已把两条实际下降线固定为同一几何 fine 坐标中的
$t_*^p=t_*$ 与 $t_*^p=-t_*$。这里
$t_*=u_*/p$，$u_*=[T^p][p](T)$ 是 R1071 §17 的原 source 参数。
取 $i^2=-1$，再取 $\alpha\in\mathbf F_{p^2}^{\times}$ 满足
$$
\alpha^p=i\alpha,\qquad
\eta=\alpha^{p+1}\in\mathbf F_p^\times,\qquad
\eta^2=-\alpha^4.
\tag{1135.29}
$$
存在性由 norm-one 元 $i$ 的 Hilbert 90 给出。
$\alpha^4\in\mathbf F_p^\times$ 且
$(\alpha^4)^{(p-1)/2}=-1$，所以 $a'=\alpha^4a$
是原 Gaussian reference 的另一实际 quartic twist。

取 $\alpha,i$ 的不分歧 Teichmüller 提升，令
$$
\varphi:E_a\longrightarrow E_{a'},\qquad
(x,y)\longmapsto(\alpha^2x,\alpha^3y).
\tag{1135.30}
$$
这是实际不分歧二次扩张上的同构。
其 Frobenius cocycle 在坐标上准确为
$(x',y')\mapsto(-x',-iy')$，微分乘 $-i$；
在 fine deformation tangent 上作用为 $-1$，
所以它正实现上述第二条下降线。
$\varphi$ 与原 $\mathbf Z_p[i]$ 作用相容，故运输同一个 canonical
non-split Cartan；它也保留 Weil pairing。

先取实际全标记 $P'_v=\varphi(P_v)$。
两边使用同一个 $\varpi,\rho$ 及同一个实际 Weil root。
原微分满足 $\varphi^*\omega'=\alpha^{-1}\omega$，
于是运输原 universal formal-group eigenparameter 得
$T'=\alpha^{-1}T$。
在 R1071 使用的有限精度内，这正是同一 tangent 归一的实际坐标：
CM 中心处两者与相应 logarithm 的差在 $T^{p^2}$；
在 $p$-close deformation 上可能的 $p$ 倍整级数误差
由 R1071 §§6、17 的原误差估计消去，不改变以下 source 或 profile。

对 $[p]$ 级数作这个真实坐标改变，得到
$$
u_*'=\alpha^{p-1}u_*,\qquad
t_*'=it_*,\qquad z'=(t_*')^2=-z,\quad z=t_*^2 .
\tag{1135.31}
$$
这里 source 等式在所需模 $p^2$ 精度成立，
$t_*$ 等式在模 $p$ 成立。
特别 $t_*^p=-t_*$ 时 $(it_*)^p=it_*$，
故第二条几何线正被运输成新 reference 的实际 $\mathbf F_p$ fine line。
没有把复代数同构冒作一个原本未给定的 $\mathbf F_p$ marked 同构。

### 10.2 微分、torsion source 和 Kummer 分母一起运输

以下 $\gamma=\delta\lambda_{\rm src}\beta_0^{1-p}$
仍指 (1135.2) 的 Kronecker gauge 尺度。
为区别原 R1071 的 Weil 相位，另记
$\gamma_W=(\zeta_p-1)/\varpi^{p+1}$。
同标记运输保留 $\zeta_p$，所以
$\gamma_W'=\gamma_W$、$b_{\omega^R}'=b_{\omega^R}$；
不能把下面 $\gamma$ 的权变化套到 $\gamma_W$。
从同一 full-level 展开
$$
T(P_v)=\varpi\beta_0(v+\lambda_{\rm src}\rho t_*v^p)+O(p\varpi)
$$
直接读出
$$
\beta_0'=\alpha^{-1}\beta_0,\qquad
\lambda_{\rm src}'=\alpha^{1-p}\lambda_{\rm src}.
$$
另一方面，relative Cartier 与 (1135.30) 相容。
因 $\varphi^*(x'\omega')=\alpha x\omega$ 而
$\varphi^{(p)*}\omega'^{(p)}=\alpha^{-p}\omega^{(p)}$，
其实际系数给 $\delta'=\alpha^{p+1}\delta=\eta\delta$。
因此完整尺度为
$$
\boxed{\quad
\gamma'=\eta\gamma,\qquad
N_R'=\eta^{-1}N_R .
\quad}
\tag{1135.32}
$$
第二式使用
$(\beta_0'^{\,p+1})^R\delta'^{\,R-1}
=\eta^{-1}(\beta_0^{p+1})^R\delta^{R-1}$；
两边实际 Weil root 相同，所以 $b_{\omega^R}$ 相同。

若已有标记另差一个 Cartan 乘法 $b\in\mathbf F_{p^2}^\times$，
则原 R1071 §14 的准确运输是
$$
\beta_0'=\alpha^{-1}b\beta_0,\quad
\lambda_{\rm src}'=\alpha^{1-p}b^{p-1}\lambda_{\rm src},\quad
b_{\omega^R}'=N(b)^R b_{\omega^R}.
$$
$\gamma'$ 中两个 $b$ 因子相消，而 $N_R'$ 中的
$N(b)^R$ 与真实 Weil 相位分母相消，所以 (1135.32) 不变。
这同时支付实际标记和固定 global Kummer basis，
没有逐点任意重标标签。

### 10.3 完整 centered 核和常数项的比较

同一 homothety 的 characteristic-zero sigma 规范给
$$
\mathscr K_{a'}(T,U)=\alpha\,\mathscr K_a(\alpha T,\alpha U).
$$
在总次数 $p$ 的 centered 层上，因 $\alpha^{p+1}=\eta$，
$$
\boxed{\quad
\mathcal A_R^{a'}(Z')=\eta\,
        \mathcal A_R^a(Z'/\alpha^4).
\quad}
\tag{1135.33}
$$
这里完整 (1135.1) 中的所有 $h$ 以及 principal 都一起运输，
没有只比较一个首项。其依据也可逐项看成
$(w')^{2h}\alpha^{4(k+1-h)}
=\alpha^{p+1}(w'/\alpha^2)^{2h}$。

结合 $\gamma'^2=\eta^2\gamma^2=-\alpha^4\gamma^2$
与 (1135.32)，得到实际标签的准确等式
$$
\boxed{\quad
\Pi_R'(z')=\Pi_R(-z')
\qquad(R\in\mathcal G_p).
\quad}
\tag{1135.34}
$$
原 $p$-整数 division product 也验证常数层没有遗漏：
$\psi_c^{E_{a'}}(\varphi P)=\alpha^{c^2-1}\psi_c^{E_a}(P)$，
而原 exponent 的总和为零。因此同标记的 $M_\chi$ 严格相等。
若随后改 Cartan 标记，上一小节的实际 Weil 相位比较同样处理
其固定 global basis。故 (1135.34) 不只是一个未知常数差意义下的断言。

也可直接在 R1071 (1071.20) 的完整原 profile 上交叉核对。
由同一 $\psi_c$ 的上述 homothety，
其 regular factor 满足 $F_c'(T')=F_c(\alpha T')$，因而
$A_d'=\alpha^dA_d$。再用
$\beta_0'=\alpha^{-1}\beta_0$、$\lambda_{\rm src}'t_*'
=\lambda_{\rm src}t_*$ 以及固定的 $b_{\omega^R}$，
每个真实系数
$\beta_0^d(\lambda_{\rm src}t_*)^iA_d$ 均逐项不变。
这也包括 $i=0$ 的原常数项，并不要求把未知高核 band 约化。

这些比较均在实际不分歧二次扩张完成。
对原定义域上的 Kummer 类，restriction 后的等式亦可由
restriction–corestriction 的次数 $2$ 下传，因为 $p$ 为奇数。
无需引入新的点、改换原 cusp leading 归一或假设 full-level
标记在 $\mathbf Q_p$ 上有理。

### 10.4 对原共同纤维范围的精确提升

第一条 fine line 的 $z=t_*^2$ 给 $\mathbf F_p$ 的平方值，
第二条给非平方值；$z=0$ 是共同 CM 中心。
(1135.34) 把两者准确放进同一个原多项式
$\Pi_R(z)=N_R\mathcal A_R(\gamma^2z)$，
定义在同一 coarse component 的全部 $z\in\mathbf F_p$ 上。

因此 §2 在 $p\mid B_{p-7},B_{p-11}$ 下的 (1135.6)
现在可同时用于两种实际下降线：
该同一原 Gaussian coarse component 内的非对角共同纤维
仍至多一个无序点对。两个根必须属于
$\gamma^2\mathbf F_p$，并通过全部其余实际 good 行。
**$S=0$ 和 $P=0$ 仍须保留**；
不能因为某一条 fine line 的平方像不含某根，
就把另一条 line 贡献的真实点删去。

同样，在 §3 的实际分支中，
$\Delta_{\rm low}\ne0$ 的 degree-one 组合会分离该 component
全部 coarse 点，而不再只限单条 fine line。
本节没有证明 $\Delta_{\rm low}$ 非零，
没有合并不同 coarse components，也没有据此排除圆盘内全局有理点。


o1 已按 R1071 §§2、6、8、12、14 与 R1116 §8 独核本节完整
actual twist/source 运输；Weil 相位与 Kronecker gauge 分别标明。
本节无数学程序执行。


## 11. 全部实际 good 行的坐标代数只有一个导子障碍

本节保持 §2 的两个实际条件
$p\mid B_{p-7}$、$p\mid B_{p-11}$，并保留完整 $\mathcal G_p$。
在 R1071 (1071.33) 已支付的 $t_*$ source 中，
(1071.36) 给 $\lambda=-\beta_0^{p-1}$，故
$\gamma=-\delta\in\mathbf F_p^\times$。
这不是删去 Weil 相位或重选标签基。
结合 §10，两种实际下降线在同一 coarse component 上可统一写成
$z\in\mathbf F_p$、$Z=\delta^2z$。
各 $N_R$ 仍是原非零尺度；它们和已减去的原常数不改变纤维等式。

令 $S,P$ 为 (1135.6) 的实际两系数，并置
$$
W=Z-\frac S2,\qquad d=\frac{S^2}{4}-P,\qquad
\mathscr A=\mathbf F_p[
  \mathcal A_R(W+S/2):R\in\mathcal G_p]\subset\mathbf F_p[W].
\tag{1135.35}
$$
这里的 $W$ 只是平移后的 coarse 坐标，不是 (1135.1) 的 gauge 参数 $w$。
由 (1135.3) 减常数、反除两个已证单位，再减去一个
$\mathcal A_4$ 的倍数，可以准确取到
$$
X=W^2,\qquad Y=W(W^2-d).
$$
具体地，$\mathcal A_4$ 的二次系数是 $-G_{p-7}/24$；
$\mathcal A_6$ 的三次系数是 $-G_{p-11}/720$。
平移并消去其偶数项后，后者的一次系数与三次系数之比为
$$
\frac{3S^2}{4}
-\frac{30d_2S+360c_4}{G_{p-11}}
=P-\frac{S^2}{4}=-d.
$$
因此两个原低行生成的子代数恰为
$$
\mathscr A_0=\mathbf F_p[X,Y]
=\mathbf F_p[W^2,W(W^2-d)]
\simeq\frac{\mathbf F_p[X,Y]}{(Y^2-X(X-d)^2)}
\ \subset\ \mathscr A\ \subset\ \mathbf F_p[W].
\tag{1135.36}
$$

### 11.1 余维一、准确导子与全部 good 行的二分

每个多项式唯一写成
$f(W)=E(W^2)+W\,O(W^2)$。由 (1135.36)，
$$
\begin{aligned}
\mathscr A_0
 &=\mathbf F_p[W^2]\oplus
       W(W^2-d)\mathbf F_p[W^2],\\
f\in\mathscr A_0
 &\Longleftrightarrow O(d)=0,\\
\mathbf F_p[W]/\mathscr A_0
 &\simeq \mathbf F_p\cdot[W],\\
\operatorname{cond}_{\mathbf F_p[W]}(\mathscr A_0)
 &=(W^2-d)\mathbf F_p[W].
\end{aligned}
\tag{1135.37}
$$
最后一式也可直接核定：若 $f=E+WO$ 已在 $\mathscr A_0$，
再要求 $Wf$ 在其中，恰同时要求 $E(d)=O(d)=0$。
因 $\mathbf F_p[W]$ 作为 $\mathbf F_p[W^2]$-模由 $1,W$ 生成，
这正是完整导子条件。

$W$ 整于 $\mathscr A_0$，两者分式域相同
（$W=Y/(X-d)$）；故 $\mathbf F_p[W]$ 是其有限正规化。
更强的是，中间的实际 good 代数只能有两种可能：
$$
\boxed{\qquad
\mathscr A=\mathscr A_0
\quad\text{或}\quad
\mathscr A=\mathbf F_p[W].
\qquad}
\tag{1135.38}
$$
这是余维一的结论，也有明确的原行构造。
若某个实际 good 行
$f_R(W)=E_R(W^2)+W O_R(W^2)$ 满足 $O_R(d)\ne0$，
则
$$
W=\frac{1}{O_R(d)}
 \left(
 f_R-E_R(W^2)
 -Y\,\frac{O_R(W^2)-O_R(d)}{W^2-d}
 \right)\in\mathscr A.
\tag{1135.39}
$$
显示商是多项式。因此一次非零读取就给完整的多项式 coarse 坐标恢复，
而不只是分式域生成或一般位置的单射。
反之，若全部实际 good 行的 $O_R(d)$ 都为零，它们都落在同一个
$\mathscr A_0$ 中。本式没有补入任何缺席或 Bernoulli-bad 的行。

若原 $R=p-5$ 也为 good，则其旧二次行在同一个商中的类准确为
$
[\mathcal A_{p-5}(W+S/2)]
 =\frac{\Delta_{\rm low}}{2G_{p-7}}[W].
$
确实，平移后的奇系数为
$c_3/2+d_1S/24=(c_2d_1+G_{p-7}c_3)/(2G_{p-7})$。
因此此前的 affine minor 正是这个同一导子类；这条识别不要求 $d\ne0$，
也不宣称 $\Delta_{\rm low}$ 已为单位。

### 11.2 分裂节点、非分裂节点及 d=0 的尖点边界

若 $d\ne0$，(1135.36) 的像只有一个普通二重点 $(X,Y)=(d,0)$；
正规化的两个几何原像是 $W=\pm\sqrt d$。
它在 $\mathbf F_p$ 上分裂当且仅当 $d$ 是平方。
若 $d=0$，像为 $Y^2=X^3$，其唯一奇点是尖点，
正规化原像只有 $W=0$。

所以原全部 good 标签在该 component 的 $\mathbf F_p$ coarse 参数上满足：
$$
\boxed{\begin{array}{ll}
d=0\text{ 或 }d\text{ 非平方}:&
 \text{两个低行已在 }\mathbf F_p\text{ 点上单射};\\[2pt]
d\in(\mathbf F_p^\times)^2,\ \mathscr A=\mathbf F_p[W]:&
 \text{全部 good 行给闭嵌入，因而分离全部点};\\[2pt]
d\in(\mathbf F_p^\times)^2,\ \mathscr A=\mathscr A_0:&
 \text{唯一非对角纤维恰为 }
 Z=S/2\pm\sqrt d .
\end{array}}
\tag{1135.40}
$$
第一行不声称 $d=0$ 时坐标代数已经正规：
尖点正规化虽不是闭嵌入，却不会合并两个不同的域值点。
本判别包括 $S=0$、$P=0$，也包括由两种 twist 贡献的跨线比较。
它仅涉及同一原 coarse component 的实际标签，
没有合并其他 components，也没有由此宣称圆盘内全局有理点唯一。

### 11.3 真向量场稳定性须支付的准确门

导子还给后续使用微分关系的一个明确检验。
对多项式 $f(W)$，直接在 $X,Y$ 两生成元上计算可得
$$
f(W)\frac d{dW}(\mathscr A_0)\subseteq\mathscr A_0
\quad\Longleftrightarrow\quad
\begin{cases}
W^2-d\mid f(W),&d\ne0,\\
W\mid f(W),&d=0.
\end{cases}
\tag{1135.41}
$$
证明中写 $f=E(W^2)+W O(W^2)$。
作用于 $X$ 要求 $E(d)=0$；
作用于 $Y$ 再要求 $2d\,O(d)=0$。
$p>37$ 保证这些检验没有特征 $2,3$ 的例外。

例如，如果以后能证明原完整 good 代数在某个系数为非零一次多项式的
实际向量场下稳定，$d\ne0$ 时就不能是 $\mathscr A_0$。
但本节没有证明这种稳定性：完整 Kronecker/Fay 的全行微分关系，
并不自动保持 $\mathcal G_p$ 的真实 mask。
当前尚未支付的量仍是某个实际 $O_R(d)$ 的非零，
或一个足以迫使它非零的原算子闭性。
这里得到的是准确的一维导子障碍及其全部点域边界，
不是已经消去该障碍。

本节只用原两个单位最高系数、§10 的实际两 twist 运输及显示多项式代数；
没有数学程序执行或新增有限窗口。


## 12. 原低行 minor 的模参数 Wronskian 与准确 cusp 阶

本节给 (1135.8) 的同一个 $\Delta_{\rm low}$ 一个完整的模参数来源，
并证明在原分支 $p\mid B_{p-7}$ 中，相应权多项式在 cusp 的阶准确为一或二。
这不等于它在 Gaussian 点 $b=0$ 的值为单位。

先在一般短模型 $y^2=x^3+ax+b$ 上取
$$
F_*=G_{p-7},\qquad G_*=G_{p-9},\qquad
K_*=\partial G_*,
\qquad
\partial=6b\,\partial_a-\frac{4a^2}{3}\,\partial_b .
\tag{1135.42}
$$
这里 $F_*,G_*,K_*$ 是原 lattice Eisenstein 权多项式；
$K_*$ 不是 §§5–7 的混合系数 $K_p$，也不是 Kronecker 核。
所有模参数微分都先在 $(a,b)$ 上完成，再取 $b=0$。
$F_*$、$K_*$ 的权都是 $p-7$。

### 12.1 三个原系数的完整 heat 读取

对 R1116 (1116.42) 的同一个核系数
$f_n^{v,0}=[T^{v+n-1}U^n]\mathscr K(T,U)$，逐次取 $w=0$，
并保留 $\partial_w f_n=f_{n-1}$，得到
$$
\begin{aligned}
f_0^{v,0}&=-G_v,&
f_1^{v,0}&=-\frac{\partial G_v}{v},\\
f_2^{v,0}
 &=-\frac{\partial^2G_v+(av/3)G_v}{2v(v+1)},\\
f_3^{v,0}
 &=-\frac{\partial^3G_v+2vbG_v+
                ((3v+2)/3)a\,\partial G_v}
              {6v(v+1)(v+2)} .
\end{aligned}
\tag{1135.43}
$$
最后一行的 $2vbG_v$ 来自 $\partial a=6b$；
$a\,\partial G_v$ 的两个贡献为 $v/3$ 与 $2(v+1)/3$。
没有在微分以前将 $b$ 冻结为零。

原 $c_2$ 是 $v=p-7,n=2$，原 $d_1,c_3$ 分别是
$v=p-9,n=1,3$。所以在 $\mathbf F_p$ 中准确得到
$$
\boxed{\quad
d_1=\frac{K_*}{9},\qquad
c_2=-\frac{\partial^2F_*-(7a/3)F_*}{84},\qquad
c_3=\frac{\partial^2K_*-(25a/3)K_*}{3024},
\quad}
\tag{1135.44}
$$
右侧全部最后取 $b=0$。所有分母在当前 $p\ge41$ 下为单位。

定义原权 $2p-10$ 多项式
$$
\mathscr W=
F_*\partial^2K_*-4K_*\partial^2F_*+aF_*K_*.
$$
将 (1135.44) 代入 $\Delta_{\rm low}=F_*c_3+c_2d_1$，得到
$$
\boxed{\qquad
3024\,\Delta_{\rm low}=\mathscr W(a,0).
\qquad}
\tag{1135.45}
$$
其中 $aF_*K_*$ 的系数准确为 $(-25+28)/3=1$。
(1135.4) 给 $F_*(a,0)$ 为单位。
又 $p-7\equiv0\pmod4$，故 $F_*$、$K_*$ 对 $b$ 都是偶多项式，
在 $b=0$ 有 $\partial F_*=\partial K_*=0$。于是还可写成
$$
\mathscr W(a,0)
=F_*^5\left[
 \partial^2\!\left(\frac{K_*}{F_*^4}\right)
       +a\frac{K_*}{F_*^4}
 \right]_{b=0}.
\tag{1135.46}
$$
这只是原 minor 的准确二阶模参数式，未把此前的 $V_3,V_4$ 余项设为零。

### 12.2 原 bad-Bernoulli 分支的首项不发生额外抵消

使用原 Tate convention
$$
a=-E_4/48,\qquad b=E_6/864,\qquad
\theta=q\,d/dq,\qquad
\partial f=\theta f-\frac{\operatorname{wt}(f)}{12}E_2f .
$$
此处的 $q$ 是真正 Tate 参数，与 §11 的 coarse 坐标 $W$ 无关。
原 lattice 规范为
$$
G_d=\frac{2\mathcal E_d}{(d-1)!},\qquad
\mathcal E_d=-\frac{B_d}{2d}+\sum_{n\ge1}\sigma_{d-1}(n)q^n.
$$
权 $p-9,p-7$ 都小于 $p-1$，故由 R1129 的同一
$q$-expansion/权环来源，它们是 $p$ 整权多项式。
$\partial$ 的系数也 $p$ 整，所以 $\mathscr W$ 的定义不要求读取
一个新高权 $G_{2p-10}$ 或反除任何 Bernoulli 非单位。

以下沿用实际分支 $p\mid B_{p-7}$。
记 $F_i=[q^i]F_*$、$G_i=[q^i]G_*$、$K_i=[q^i]K_*$，则
$$
F_0=0,\qquad
F_1=\frac2{(p-8)!}\in\mathbf F_p^\times,\qquad
G_0=-\frac{B_{p-9}}{(p-9)!},\qquad
G_1=\frac2{(p-10)!}\in\mathbf F_p^\times .
$$
先用权 $p-7\equiv-7$、$p-9\equiv-9$，以及
$E_2(0)=1$、$a(0)=-1/48$，逐项得到
$$
K_0=\frac34G_0,\qquad
[q^0]\partial^2K_*=\frac{35}{144}K_0,\qquad
[q^1]\partial^2F_*=\frac{323}{144}F_1.
$$
最后一个 $323=19\cdot17$ 来自
$(1+7/12)(1+5/12)$；含 $F_0$ 的其余项已经准确为零。
若 $G_0\ne0$，从定义直接读出
$$
[q]\mathscr W
 =\frac{35-4\cdot323-3}{144}F_1K_0
 =-\frac{105}{16}F_1G_0\ne0.
$$
若 $G_0=0$，则 $K_0=0$、$K_1=7G_1/4$，且
$[q]\partial^2K_*=323K_1/144$。这时两乘积首次都在 $q^2$，
$$
[q^2]\mathscr W
 =\frac{323-4\cdot323-3}{144}F_1K_1
 =-\frac{189}{16}F_1G_1\ne0.
$$
因此有完整的实际二分
$$
\boxed{\begin{array}{c|c|c}
\text{条件}&\operatorname{ord}_{q=0}\mathscr W&
 \text{首系数}\\ \hline
p\nmid B_{p-9}&1&-105F_1G_0/16\\
p\mid B_{p-9}&2&-189F_1G_1/16 .
\end{array}}
\tag{1135.47}
$$
$105$、$189$ 的素因子均小于 $41$，所以所示非零不含隐蔽例外。
这里没有假设 $p-9$ 是实际 good 角色，也没有增加一个观测行。

### 12.3 非零多项式与 Gaussian 指定值的边界

由 (1135.47)，$\mathscr W$ 的约化确是非零权 $2p-10$ 多项式。
若以 $\varepsilon\in\{1,2\}$ 表示该表的准确 cusp 阶，
则 level-one 权环中的 cusp 理想给
$$
\mathscr W=\Delta_E^\varepsilon\,\mathscr W_0,\qquad
\Delta_E=-16(4a^3+27b^2),\qquad
\operatorname{wt}(\mathscr W_0)=2p-10-12\varepsilon .
\tag{1135.48}
$$
这里 $\Delta_E=q+O(q^2)$ 是相同 Tate 规范的 discriminant，
且 $\mathscr W_0$ 非零、cusp 常数为单位。
在 Gaussian 点 $\Delta_E(a,0)=-64a^3$ 为单位，
所以除去这个已知 cusp 因子不会改变目标的 $b$ 阶或零性。

例如，写 $p=4k+3$，同权性使 $\mathscr W_0$ 的单项式恰为
$a^{\,2k-1-3\varepsilon-3j}b^{2j}$。
对任意固定的原 $a\ne0$，每个 $b$ 次数只有一个 $a$ 单项式，
故 $\mathscr W_0(a,b)$ 仍是非零多项式，且
$$
\operatorname{ord}_{b=0}\mathscr W(a,b)
\ \text{为偶数，至多}\
2\left\lfloor\frac{2k-1-3\varepsilon}{3}\right\rfloor .
\tag{1135.49}
$$
本界允许正的偶数阶；它没有证明 $\mathscr W(a,0)\ne0$。

所以本节新增的是原 minor 的完整 heat/Wronskian 来源、
其非零权多项式性质和准确 cusp 阶，而非指定 Gaussian 单位。
(1135.45) 仍须在同一个原 $a$、同一个 actual-good mask 下读取。
未证明 §11 的剩余节点被分离，也没有从非零 $q$ 首项跳过
$\mathscr W(a,0)$ 这一步。全文为纸面计算，无数学程序执行。


## 13. 原模参数导子的固定判别式曲线与 Hasse 差项

本节仍在 §12 的同一 $\mathbf F_p[a,b]$ 权环中工作。
它把原 $\partial$、$F_*,G_*,K_*$ 与 $\mathscr W$ 放在一条明确的
固定判别式曲线上，给出准确的 $p$ 次导子、原函数的极阶和
Hasse 候选与原 Eisenstein 来源的完整 cusp 差。
这些对象不是底层 Gaussian 椭圆的另一种随意坐标。

### 13.1 固定判别式纤维及实际不变导子

直接计算
$\partial(4a^3+27b^2)=72a^2b-72a^2b=0$，
故 $\partial\Delta_E=0$。
固定原 Gaussian 点 $a=a_{\rm G}\ne0,b=0$ 的
$\Delta_0=-64a_{\rm G}^3\in\mathbf F_p^\times$。
在 $\Delta_E=\Delta_0$ 上置
$$
X=-\frac{4a}{3},\qquad Y=-4b.
$$
准确得到光滑射影椭圆曲线及其不变微分
$$
\boxed{\quad
\mathcal C_{\Delta_0}:\ 
Y^2=X^3-\frac{\Delta_0}{27},\qquad
\partial X=2Y,\quad \partial Y=3X^2,\qquad
\omega_{\Delta_0}=\frac{dX}{2Y}.
\quad}
\tag{1135.50}
$$
$\omega_{\Delta_0}(\partial)=1$。
因此这里的原模参数 $\partial$ 真正是
$\mathcal C_{\Delta_0}$ 的不变导子，而不是对指定点作一个形式类比。
Gaussian 位置 $b=0$ 正是 $Y=0$ 的三个非零二挠点；
所给 $a_{\rm G}$ 指定其中一个。

这条固定判别式曲线的 reduction 型别须与底层 Gaussian 椭圆分开。
设 $m=(p-1)/2$。不变导子的 restricted $p$ 次幂是
$$
\boxed{\quad
\partial^p=
\begin{cases}
0,&p\equiv11\pmod{12},\\[2pt]
\displaystyle
\binom{m}{(p-1)/3}
 \left(-\frac{\Delta_0}{27}\right)^{(p-1)/6}\partial,
 &p\equiv7\pmod{12}.
\end{cases}
\quad}
\tag{1135.51}
$$
第二行的系数为单位。

这里可直接支付归一。$\partial^p$ 仍是平移不变导子，故等于
一个常数乘 $\partial$。对 $\omega_{\Delta_0}$ 用 $X$ 计算 relative
Cartier，常数正是
$[X^{p-1}](X^3-\Delta_0/27)^m$；
该多项式的次数小于 $2p-1$，因此只读这一项。
若需将 Cartier 读数与 restricted 导子逐项比较，在 $O$ 处先以
$1,\ldots,p-1$ 的单位分母把微分正规化成
$(1+c\,t^{p-1})dt$ 模 $t^p$。此时
$\partial^p(t)|_O=-c(p-1)!=c$，而 Cartier 常数也是 $c$。
最后读二项式即得 (1135.51)。
所以 $p\equiv11\pmod{12}$ 时该曲线 supersingular，
$p\equiv7\pmod{12}$ 时 ordinary；底层 Gaussian 椭圆在本篇两种情形下
仍然 supersingular，二者不能混称同一 Frobenius。

### 13.2 原 cusp 阶给固定曲线上的准确极阶

取 $\mathcal C_{\Delta_0}$ 的原 $O$ 参数 $s=-X/Y$。
这里只需要首项
$$
X=s^{-2}+O(s^4),\quad Y=-s^{-3}+O(s^3),\quad
a=-\frac34s^{-2}+O(s^4),\quad
b=\frac14s^{-3}+O(s^3),\quad
\partial s=1+O(s^6).
$$
对权为 $w$ 的非零同权多项式 $M(a,b)$，若其准确 Tate cusp 阶为
$\epsilon$，写 $M=\Delta_E^\epsilon M_0$。
$M_0$ 的 cusp 常数是 $[q^\epsilon]M\ne0$。
原 Tate cusp 的 $a_{\rm c}=-1/48,b_{\rm c}=1/864$ 与上述首项满足
$-3/4=6^2a_{\rm c}$、$1/4=6^3b_{\rm c}$。
因此在 $n=w/2-6\epsilon>0$ 时，有完整首项
$$
\boxed{\quad
M|_{\mathcal C_{\Delta_0}}
=\Delta_0^\epsilon\,6^n[q^\epsilon]M\,s^{-n}
     +\text{较低极阶项}.
\quad}
\tag{1135.52}
$$
这不仅是极阶上界；所示首系数为单位时，极阶恰为 $n$。

现在保持原分支 $p\mid B_{p-7}$，令
$\epsilon_G=0$（若 $p\nmid B_{p-9}$）或
$\epsilon_G=1$（若 $p\mid B_{p-9}$）。
原 $F_*$ 的 cusp 阶恰一，$G_*$ 的 cusp 阶恰 $\epsilon_G$，
因为二者 $q^1$ 系数均为单位。
由 (1135.52)，它们在同一曲线上只有 $O$ 处的极点，并且
$$
\begin{array}{c|c}
\text{原函数}&O\text{ 处准确极阶}\\ \hline
F_*&n_F=(p-19)/2\\
G_*&n_G=(p-9)/2-6\epsilon_G\\
K_*=\partial G_*&n_K=n_G+1\\
\mathscr W&p-11-6\epsilon_G .
\end{array}
\tag{1135.53}
$$
前两个极阶为正且小于 $p$，所以微分的最高系数
$-n_G$ 不消失，第三行也准确。

第四行还可不经过 §12 的 cusp 读取而直接核定。
若 $F_*\sim f\,s^{-n_F}$、$K_*\sim k\,s^{-n_K}$，
则 (1135.50) 给 $\mathscr W$ 的最高系数为
$$
fk\left\{
n_K(n_K+1)-4n_F(n_F+1)-\frac34
\right\}
=
\begin{cases}
-315\,fk,&\epsilon_G=0,\\
-243\,fk,&\epsilon_G=1.
\end{cases}
$$
两系数在当前范围均为单位，故不存在最高极项的额外抵消。
极阶 $n_F+n_K+2$ 正是表中第四行，也与 (1135.47)–(1135.48)
的准确 cusp 阶一致。这里仍没有把非零函数的指定值当成非零。

$F_*,K_*,\mathscr W$ 对 $b$ 为偶，$G_*$ 为奇。
在几何三次自同构 $(X,Y)\mapsto(\zeta_3X,Y)$ 下，
每个同权多项式 $M$ 都按 $\zeta_3^w$ 作用，
因为其每个单项式的 $a$ 指数模三等于权 $w$。
因此 $\mathscr W$ 若在指定 Gaussian 点为零，
也在其余两个 $Y=0$ 点为零。
$Y$ 在这些点为 uniformizer，而偶性使每个零至少为二重。

更精确地，原权 $2p-10$ 使
$\mathscr W(a,0)$ 只能是 $a^{(p-5)/2}$ 的一个标量倍。
所以对任何原 $a_{\rm G}\ne0$，
$$
\boxed{\quad
\mathscr W(a_{\rm G},0)=0
\ \Longleftrightarrow\
b^2\mid\mathscr W\ \text{于 }\mathbf F_p[a,b].
\quad}
\tag{1135.54}
$$
在固定曲线上，这给三个非零二挠点的共同二重零，
但 (1135.53) 的总极阶仍容许这些零。
(1135.54) 是原全权多项式的因子判据，
不是将 $b^2$ 偷换成整个 Hasse 因子。

### 13.3 Hasse 候选的同一权与准确偏导

为避免与实际行 $\mathcal A_R$ 混淆，记
$$
\mathsf A=E_{p-1}\bmod p,\qquad
\beta=E_{p+1}/12\bmod p .
$$
它们是同一原权环中的 Hasse 多项式及其导数。
$q$ 展开 $\mathsf A=1$、$\beta=E_2/12$，
连同固定权的 $q$-expansion 原理给
$$
\partial\mathsf A=\beta,\qquad
\partial\beta=\frac a3\mathsf A,\qquad
\partial^2\mathsf A=\frac a3\mathsf A=-\frac X4\mathsf A.
\tag{1135.55}
$$
例如第二式由
$\theta E_2=(E_2^2-E_4)/12$ 及 $a=-E_4/48$ 得到，
不以普通 $q$ 导数替代模参数导数。
因此 $\mathsf A$ 在 (1135.50) 上确是一个原
Lamé 方程的解，但本节没有把 $F_*,G_*$ 宣称为它的偏导。

原 Euler 身份
$4a\mathsf A_a+6b\mathsf A_b=(p-1)\mathsf A=-\mathsf A$
与第一条 (1135.55) 构成两个线性方程。
它们的 determinant 为 $\Delta_E/12$，解得
$$
\boxed{\quad
\mathsf A_b=\frac{48a\beta+72b\mathsf A}{\Delta_E},\qquad
\mathsf A_a=\frac{16a^2\mathsf A-72b\beta}{\Delta_E}.
\quad}
\tag{1135.56}
$$
虽然显示式反除 $\Delta_E$，左侧本来是权多项式；
在固定 $\Delta_0\ne0$ 上更没有新的极点。
$\mathsf A_b$ 的权是 $p-7$，$\mathsf A_{aa}$ 的权是 $p-9$，
确与 $F_*,G_*$ 分别同权。仅此还不证明两组相等。

### 13.4 原 cusp 常数及完整 cusp 差

对权 $r$ 的任意同权多项式 $f$，同样解 Euler/Serre 两式，
再代原 Tate convention，得到
$$
\partial_a f
=\frac{(r/72)(\theta E_6)f-(E_6/12)\theta f}{\Delta_E},
\qquad
\partial_b f
=\frac{(r/4)(\theta E_4)f-E_4\theta f}{\Delta_E}.
\tag{1135.57}
$$
权 $r$ 在 $\mathbf F_p$ 中读取；$\theta$ 只在本显示式中作用于
实际 $q$ 展开。对 $\mathsf A$ 使用 $r=p-1=-1$、$\theta\mathsf A=0$，
可自足核准
$$
\begin{aligned}
\mathsf A_b&=-\frac{\theta E_4}{4\Delta_E}
             =-60-2520q+O(q^2),\\
\mathsf A_a&=-\frac{\theta E_6}{72\Delta_E}
             =7+630q+18480q^2+O(q^3),\\
\mathsf A_{aa}&=\frac{385}{2}+66220q+O(q^2).
\end{aligned}
\tag{1135.58}
$$
最后一行是将第二行作为权 $p-5=-5$ 代入 (1135.57)。
所需原级数仅为
$E_4=1+240q+2160q^2+\cdots$、
$E_6=1-504q-16632q^2-122976q^3+\cdots$、
$\Delta_E=q-24q^2+252q^3+\cdots$。
例如 $\partial_a\mathsf A_a$ 的分子在 $q,q^2$ 的系数分别是
$385/2,61600$；除以 $\Delta_E$ 后的 $q^1$ 系数为
$61600+24(385/2)=66220$。这是有限纸面系数运算。

原 Eisenstein 规范给
$[q^0]F_*=-B_{p-7}/(p-7)!$、
$[q^0]G_*=-B_{p-9}/(p-9)!$。
于是可以精确写成
$$
\boxed{\begin{aligned}
F_*&=\frac{B_{p-7}}{60(p-7)!}\,\mathsf A_b+\mathcal S_F,\\
G_*&=-\frac{2B_{p-9}}{385(p-9)!}\,\mathsf A_{aa}+\mathcal S_G,
\end{aligned}}
\tag{1135.59}
$$
其中 $\mathcal S_F,\mathcal S_G$ 是同一权环中准确的 cusp 多项式，
分别被 $\Delta_E$ 整除；本式由显示式定义它们，不省略任何差项。
所有分母在 $p\ge41$ 下为单位。

在本节实际分支 $p\mid B_{p-7}$，
第一行的 Hasse 系数为零，且 $\mathcal S_F=F_*$ 的 $q^1$ 系数为单位。
特别 $F_*$ 不可能是 $\mathsf A_b$ 的任何标量倍：
非零标量倍有非零 cusp 常数，零标量倍又不可能有该 $q^1$ 项。
若还 $p\mid B_{p-9}$，同理 $G_*=\mathcal S_G$，
也不是 $\mathsf A_{aa}$ 的标量倍。
所以这个准确比较给出了具体原 cusp 差，而非只提醒“可能有差”。

### 13.5 Gaussian Hasse 值不能代替原 jet

最后取原 $b=0$、$a=a_{\rm G}\ne0$。
底层 Gaussian 椭圆 supersingular，故 $\mathsf A(a_{\rm G},0)=0$，
而 $\beta=-\delta$ 是原已付的单位。
(1135.56) 于是给
$$
\boxed{\quad
\mathsf A_b(a_{\rm G},0)=-\frac{3\beta}{4a_{\rm G}^2},
\qquad
\partial\mathsf A_{aa}(a_{\rm G},0)
 =\frac{77\beta}{16a_{\rm G}^2}.
\quad}
\tag{1135.60}
$$
第二式也可不用反除判别式求导：
$p=4k+3$ 时同权性给
$\mathsf A=b\,a^{k-1}(h_0+O(b^2/a^3))$，
所以
$\partial\mathsf A_{aa}|_{b=0}
=-(4/3)(k-1)(k-2)\mathsf A_b$。
代 $(k-1)(k-2)=77/16\bmod p$ 即得所示常数。

两值都是单位，但 (1135.59) 的完整 cusp 差及其
$\partial$、$\partial^2$ jets 仍然存在。
因此本节没有将 (1135.60) 用作原 $K_*$ 或
$\mathscr W(a_{\rm G},0)$ 的单位证明。

新增结论是同一原导子的实际固定曲线、
(1135.51) 的 restricted $p$ 次结构、
(1135.52)–(1135.54) 的原函数准确除子界和因子判据，
以及 (1135.56)–(1135.60) 的真实 Hasse/cusp 分解。
下一步可在这条曲线上研究原 $F_*,G_*$ 的特定 Cartier 或 CM 关系；
不能只凭总极阶、Lamé 候选或 Hasse 单位替代指定取值。
本节无数学程序执行，实际 good mask 与同一 coarse component 的范围不变。
