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
