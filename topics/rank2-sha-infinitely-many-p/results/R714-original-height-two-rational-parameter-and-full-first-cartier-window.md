# R714 — 原高度二整窗的有理参数修正与全部首 Cartier 块

日期：2026-11-15。**状态：下述原参数整窗比较、有理极帽及全部首块的准确返回已证明。**

R636 的有理参数 $Z$ 从 $z^{5p}$ 起与原形式对数不同。
本篇用同一个原 Gaussian 的对数导数，给出一个完全指定的有理
Frobenius 修正。修正后的参数在全部 $p^2$ 以下与原整截断一致。
这不是把原形式对数直接约化成一个全局函数，也不抹掉原 sigma
来源在第六块起的真正 Frobenius 误差。

## 1. 同一原来源与完整有理身份

保持
$$
p=6s-1>101,\qquad q=p^2,\qquad d=p+1,\qquad b=17,
$$
以及 R636、R647 的
$$
E_b:y^2=x^3+b,\quad \omega_E=\frac{dx}{2y},\quad
D x=2y,\quad D y=3x^2,\quad D^p=0.
$$
在原点 $O$，取 $u=x^{-1/2}\sim z$。
这个 $u$ 只在完备局部环中使用；本篇的全局有理函数仍在 $k(E_b)$。
令
$$
c=[z^d]\log(\sigma/z),\quad
\sigma^\circ=\sigma e^{-cz^d},\quad
\zeta^\circ=D\log\sigma^\circ,\quad
r=x^2/y.
$$

R636 的指定 $Z,G$ 及 $c_p\in k^\times$ 满足
$$
DZ=1,\qquad DG=-x+c_p Z^{p-1},\qquad
D^{p-1}G=r^p,
$$
$$
H_G=G+r=\frac{3b}{5}z^5+O(z^{11}),\qquad
\zeta^\circ-G=O(z^{6p-1}).
\tag{1}
$$
这里
$$
c_p=\binom{3s-1}{2s-1}b^s.
$$
全部 $z$ 比较都只在 R614 已付的整窗口内读取。
原规范还给 $[z^p]\zeta^\circ=0$；没有另加一个可选择的原函数。

直接对 $DG$ 作 $p-2$ 次导数，得完整函数域身份
$$
\boxed{
D^{p-2}(-x)=r^p+c_p Z.
}
\tag{2}
$$
因为 $DZ=1$ 且 $(p-1)!=-1$，所以
$D^{p-2}Z^{p-1}=-Z$。式 (2) 的符号因而固定。

## 2. 有限整参数和原对数导数的精度

置 $L=(q-1)/6$。R614、R615 给原
$$
z=u\mathsf H(bu^6)
$$
的全部次数小于 $q$ 的系数整。
令 $z_0(u)$ 为这些系数的约化截断；它的最高可能次数为 $q-6$。
于是
$$
z_0=u+O(u^7),\qquad
Dz_0=1+O(u^{q-1}).
\tag{3}
$$
$z_0$ 不是原对数的无穷约化；次数 $q$ 的原系数已可能有 $p$ 分母。

R614 同时证明
$$
U(z)=\sigma^\circ(z)/z
=\sum_{n\ge0}u_nz^{6n},\qquad u_n\in\mathcal O\quad(n<L).
$$
在特征 $p$ 完备局部环内取真实有限 jet 的整延长
$$
F_0=z_0\sum_{n<L}\bar u_n z_0^{6n},\qquad
\zeta_*=D F_0/F_0.
\tag{4}
$$
$F_0$ 的原点阶为一。它与原 $\sigma^\circ$ 的全部次数小于 $q$
一致，所以 $\zeta_*$ 与原 $\zeta^\circ$ 在次数小于 $q-2$ 一致。
后一个精度包含除去首项 $z$ 再作一次导数的损失。

原准确的微分等式及其同一 Gaussian 约化给
$$
D\zeta_*=-x+c_p z_0^{p-1}+O(u^{q-3}).
\tag{5}
$$
不把这个有限等式称为全局连接身份。
另一方面，$\zeta_*$ 是 (4) 的实际对数导数，且 $D^p=0$，
故在整个完备局部域内有
$$
\boxed{D^{p-1}\zeta_*+\zeta_*^p=0.}
\tag{6}
$$
这是 R636 所用的同一对数导数身份；
它也直接来自 $(D-D F_0/F_0)^p=F_0D^pF_0^{-1}$。

为精确支付 (5) 的高阶求导，记 $\partial_0=d/dz_0$。
由 (3)，
$$
D=(1+O(z_0^{q-1}))\partial_0.
$$
对一个阶数为 $a$ 的 Laurent 级数，$n$ 次导数最多损失 $n$ 阶。
因此 (5) 的误差在 $p-2$ 次导数后为
$O(u^{q-p-1})$；同时
$$
D^{p-2}z_0^{p-1}=-z_0+O(u^q).
\tag{7}
$$
后一式中，至少出现一次 $D-\partial_0$ 的每个词，
阶数至少为 $(p-1)+(q-1)-(p-2)=q$。
所以 (7) 没有隐去一个位于目标窗内的导数误差。

结合 (2)、(5)–(7)，得到
$$
\boxed{
(\zeta_*+r)^p=c_p(z_0-Z)+O(u^{q-p-1}).
}
\tag{8}
$$

## 3. 全部高度二整窗的指定有理修正

定义同一曲线上的有理函数
$$
\boxed{
Z_1=Z+c_p^{-1}H_G^p.
}
\tag{9}
$$
因为 (1)、(4) 给 $\zeta_*-G=O(u^{6p-1})$，
其 $p$ 次幂从 $6p^2-p$ 起，严格高于 (8) 的窗口。
所以 (8) 首先证明
$$
z_0-Z_1=O(u^{q-p-1}).
\tag{10}
$$

不能在此直接声称精度为 $q$。补足剩余精度要用原六重型和导数。

$Z_1$ 满足 $DZ_1=1$，所以由 (3)
$$
D(z_0-Z_1)=O(u^{q-1}).
\tag{11}
$$
$D$ 在局部是一个单位乘 $d/du$。
因此 $z_0-Z_1$ 的次数小于 $q$ 的非零项，次数必须被 $p$ 整除。
同时 $z_0,Z$ 都为 $\mu_6$ 型1，而 $H_G$ 为型 $-1$；
因为 $p\equiv-1\bmod6$，$H_G^p$ 也为型1。
所以这些次数还必须同余 $1\bmod6$。

在 (10) 的区间
$$
q-p-1\le n<q
$$
中，唯一的 $p$ 倍数是 $q-p$。
但 $q-p\equiv2\bmod6$，不符合型1。
故区间中全部系数为零，得到完整结论
$$
\boxed{
Z_1=z_0+O(u^q),\qquad DZ_1=1,\qquad dZ_1=\omega_E.
}
\tag{12}
$$

特别，(12) 恢复原对数的**全部整次数 $<p^2$**。
没有对首个可能不整的 $u^{p^2}$ 系数作任何约化断言。
原 $Z=z-\kappa_5z^{5p}+\cdots$ 的首差也被完整保留：
(9) 的首修正恰为
$c_p^{-1}(3b/5)^p z^{5p}=\kappa_5z^{5p}$。

### 3.1 真实极点成本

令 $\mathcal D_2$ 为三个非零二挠点之和。
R636 给
$$
Z_\infty\le p\mathcal D_2,\qquad
(H_G)_\infty\le p(p-1)\mathcal D_2.
$$
$H_G$ 在 $O$ 的两个简单极已准确相消。因此
$$
\boxed{
(Z_1)_\infty\le(p^3-p^2)\mathcal D_2.
}
\tag{13}
$$
它在 $O$ 有准确一阶零。
其它零点的完整除子仍须保留，且
$\deg(Z_1)_0\le3(p^3-p^2)$。
新参数不能作为一个没有全局成本的固定低阶来源加入旧格。

## 4. 同一有理 sigma 模型的全部首 Cartier 块

继续 R647 的原指定函数
$$
P_2=-(D-2G)^{p-1}Z^{p+1},\qquad
\widehat A_m=P_2^{m/2}\phi_m,\qquad m=34,72.
\tag{14}
$$
原第三来源 $m=136$ 另保 $p>136$ 与其独立算术假设。
(14) 中仍是原 $Z$，没有暗中把 $P_2$ 也换成另一个模型。
这些函数在 $O$ 的首项为 $z^6$。

对全部 $1\le h\le p-1$，定义实际有理微分
$$
\alpha_{m,h}=Z_1^{-h-1}\widehat A_m\omega_E,\qquad
a_{m,h}^{\rm pole}=\operatorname{Res}_O\alpha_{m,h}.
$$
其原点阶至少为 $5-h>-p$，所以 Cartier 输出至多有简单极。
在完美剩余域中置
$$
B^{(1)}_{m,h}
=\frac{\mathcal C(\alpha_{m,h})}{\omega_E}
-\frac{(a_{m,h}^{\rm pole})^{1/p}}{Z_1}.
\tag{15}
$$
这是在 $O$ 正则的指定函数，不是任意选择一个有限部。
定义
$$
\boxed{
\mathcal T^{(1)}_{m,h}
=\left(
\frac{D^{h-1}B^{(1)}_{m,h}(O)}{(h-1)!}
\right)^p.
}
\tag{16}
$$
这里 $(h-1)!$ 始终为单位。

由于 $dZ_1=\omega_E$，原点的 Cartier 公式准确给
$$
\boxed{
\mathcal T^{(1)}_{m,h}
=[Z_1^{h(p+1)}]\widehat A_m.
}
\tag{17}
$$
证明中输入项的指数为
$h(p+1)-(h+1)=ph-1$；
Cartier 正好把它送到输出的 $Z_1^{h-1}$ 项。
(15) 已先去掉唯一可能的负次项，因而 (16) 的求值确有定义。

由 (12)，且 $\widehat A_m$ 的原点阶为六，
把 $Z_1$ 换成原已付有限参数 $z$ 所产生的首个误差至少为 $q+5$。
所以对于全部 $h\le p-1$，(17) 还有准确形式
$$
\boxed{
\mathcal T^{(1)}_{m,h}
=[z^{h(p+1)}]\widehat A_m.
}
\tag{18}
$$
右侧只表示同一有理函数的原有限整参数展开。
$h(p+1)\le q-1$，没有越过 (12) 的端点。
原微分 $\omega_E$ 与 $dz_0$ 的差同样从相对次数 $q-1$ 起，
乘六阶零后不能贡献这个窗口内的留数。

若使用全局极帽，R647 的 $M_p=p^3-p^2+2p$ 给
$$
(\alpha_{m,h})_\infty
\le\frac m2M_p\mathcal D_2+(h+1)(Z_1)_0.
\tag{19}
$$
尤其所有额外 $Z_1$ 零点均在，没有因改参数删掉其它极。

## 5. 原前六块及共同 Frobenius 误差

令
$$
A_m^\circ=(\sigma^\circ)^m\phi_m,\qquad
g_{m,h}=[z^{h(p+1)}]A_m^\circ.
$$
R614 与原完整非负幂分子保证这里 $h\le p-1$ 全整。
定义真实模型差
$$
\Delta_{m,h}
=[z^{h(p+1)}](\widehat A_m-A_m^\circ).
\tag{20}
$$
(18) 对全部首块准确返回
$$
\boxed{\mathcal T^{(1)}_{m,h}=\bar g_{m,h}+\Delta_{m,h}.}
\tag{21}
$$
(20) 由同一原来源唯一决定，不是可以配合中央假设自由选择的变量。

R647 的
$P_2-(\sigma^\circ)^2=O(z^{6p+2})$ 直接给
$$
\boxed{\mathcal T^{(1)}_{m,h}=\bar g_{m,h}\quad(1\le h\le5).}
\tag{22}
$$
置 R711 的原实际系数
$$
\eta_p=[z^{6p+2}]\{P_2-(\sigma^\circ)^2\}.
$$
完整幂展开在第六块给
$$
\boxed{\mathcal T^{(1)}_{m,6}=\bar g_{m,6}+\frac m2\eta_p.}
\tag{23}
$$
因此相对于 R711 的旧 $Z$ 观察，
$$
\mathcal T^{(1)}_{m,5}=\mathcal T_{m,5}-6\kappa_5,
$$
$$
\mathcal T^{(1)}_{m,6}
=\mathcal T_{m,6}-7\kappa_5\bar a_m^+.
\tag{24}
$$
旧坐标修正被 (9) 支付；真正 sigma 模型误差 $\eta_p$ 没有消失。

对两个原 $m,m'$，(23) 给完全指定的消误差式
$$
\boxed{
m'\mathcal T^{(1)}_{m,6}
-m\mathcal T^{(1)}_{m',6}
=m'\bar g_{m,6}-m\bar g_{m',6}.
}
\tag{25}
$$
若这两个实际 $j_m,j_{m'}$ 均为零，
仍须用 R711 的真实商
$\mathscr B_{m,6}=L_{m,5}/p^6$，得到
$$
\boxed{
m'\mathcal T^{(1)}_{m,6}
-m\mathcal T^{(1)}_{m',6}
=\frac{m'\bar\gamma_m^6\overline{\mathscr B_{m,6}}
       -m\bar\gamma_{m'}^6\overline{\mathscr B_{m',6}}}{120}.
}
\tag{26}
$$
这里 $\gamma_m=pmc$。两个原低位除商均保留。
第三条仍只在独立假设其原 $j_{136}=0$ 后加入。

## 6. 对 R708 全首前缀的实际范围

R708 把原首迹零化为 $1\le h\le J$ 的原
$\bar g_{m,h}=0$，其中 $J\le p-1$，可取约 $3p/4$ 的短前缀。
(12)、(15)–(21) 已为**全部这个前缀**付清 $z/Z_1$ 的坐标精度、
Cartier 简单极和其它全局极点：
$$
\bar g_{m,h}=0
\quad\Longleftrightarrow\quad
\mathcal T^{(1)}_{m,h}=\Delta_{m,h}.
$$

但第六块及以后不能把 $\Delta_{m,h}$ 设为零。
它们仍来自同一个原 $(\sigma^\circ)^2/P_2$，
若要用多来源消去，必须保其全部卷积和实际 Frobenius 系数。
(25) 只完成第六块的一条共同误差消去式。

本篇也没有从原 $j_m=0$ 推出 R708 的逐行前缀零；
R710 已显示只有同连接整性与零初值时这个推论不成立。
后续仍须原固定 $\phi_m$ 的算术或全局约束。
本篇提供一个与整个高度二原整窗一致的指定有理参数，
而非新的中央零、免费全局预算或主目标非零结论。

## 依赖

- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：
  原 sigma 的完整 addition 整窗和原分子的真实整性。
- [R615](R615-original-weierstrass-zeta-cartier-and-p-multiple-congruence.md)：
  原 $z(u)$ 的二项式参数及高度二端点。
- [R636](R636-original-rational-cartier-return-for-two-critical-rows.md)：
  原 $Z,G$、准确曲率和首 Frobenius 差。
- [R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)：
  原共同 $P_2$、三条完整分子及真实极帽。
- [R711](R711-original-sixth-cartier-row-and-shared-frobenius-error.md)：
  原第六块、实际 $\eta_p$ 和两个低位商。
- [R708](R708-original-mod-p-prefix-and-integral-gaussian-return.md)、
  [R710](R710-original-all-order-central-kernel-and-exact-boundary-remainder.md)：
  原边界短前缀与完整中央进位的不同要求。

本篇为全参数证明，无新增数值执行或素数扫描。
