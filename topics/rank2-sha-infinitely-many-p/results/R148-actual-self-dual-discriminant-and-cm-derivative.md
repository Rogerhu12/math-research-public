# R148：原自对偶 Hecke 判别式的总迹与 CM 导数

状态：**已证明**。日期：2026-11-12。

[完整证明](../notes/2026-11-12-actual-self-dual-discriminant-and-cm-derivative.md)。
沿用 R142、R145 的同一 $E389$ newform、原 $U$ 迹 $B$ 及
$n=N_\Gamma B,A=D_1B,F_2=D_2B$。不更换 CM 纤维。

## 结论和证明

**1. 自对偶卷积。**
令 $P_B(T)=\sum_j(\tau^jB)T^j$，$X=T-1$。原两矩展开直接给
$$
 P_B(T)P_B(T^{-1})
      =n^2-\mathscr D X^2+O(X^3),\qquad
                 \mathscr D=A^2-nA-2nF_2.
\tag{1}
$$
在原 CM 点 $n=0$ 时，其二阶项就是 $-A^2$，
自对偶形式没有另外给出 $d\mathscr D$ 的非零性。

**2. 素于 $p$ 的真实总迹。**
对 $G=\mathrm{PSL}_2(\mathbb F_\ell)$、$Z=\widetilde X/T_0$，
有 $[Z:X_{\rm src}]=\ell(\ell-1)$，素于 $p$。
把原 $\tau^jU$ 块标记写作 $j(v)$，则
$$
 \mathscr D=\sum_{v,w}Q_{vw}h_vh_w,\qquad
               Q_{vw}=-(j(v)-j(w))^2/2.
$$
$Q$ 的对角和每行和均为零，且 $T_0$-不变。
coset 和 $\sum_{G/T_0}\gamma Q$ 被双传递的 $G$ 固定，
故非对角条目是同一 $c$；行和 $\ell c=0$ 迫它为零。
所以准确得到
$$
           \operatorname{Tr}_{Z/X_{\rm src}}\mathscr D=0,\qquad
           \operatorname{Tr}_{Z/X_{\rm src}}\mathcal C=0,
                    \quad \mathcal C=\mathscr D/n^2.
\tag{2}
$$
证明没有从含因子 $p$ 的大群总迹除以 $p$。

**3. 原微分判别式。**
令撇号是 source Igusa 导数，
$\mathcal C_1=((A')^2-n'A'-2n'F_2')/(n')^2$、$x=A/n$。
直接对 $n\mathcal C=A^2/n-A-2F_2$ 微分得
$$
                  (n\mathcal C)'=
                       n'\mathcal C_1-\frac{n^2}{n'}(x')^2.
\tag{3}
$$
因此在 R141 的简单总迹 CM 点，如果实际二阶行失败，
R142 给 $x,\mathcal C$ 正则，继而
$\mathcal C(z)=\mathcal C_1(z)$。
用整 AS 坐标 $y=-A'/n'$ 时，
$a=A-nA'/n'$ 至少有二阶零，且
$g'(z)=-n'(z)\mathcal C_1(z)/2$。

**4. 不能省略的 CM Frobenius 修正。**
在原 split 完成中，取
$\omega_{\rm ST}=\Omega\omega_0$、
$\Omega^{p-1}=A_{c,p}$，并令
$\beta_p=a_p(E)/A_{c,p}^2\ne0,1$。
运输每个同源目标微分后，原权二 $U$ 行为 $H_{\rm alg}$，
导数行除以共同非零比例后为
$(1-\beta_p\tau^h)H_{\rm alg}$，
其中 $\tau^h$ 是实际算术 Frobenius。
这个算子可逆，因为其 $p$ 次幂是 $1-\beta_p$。

设 $\mathcal C_H$ 是 $H_{\rm alg}$ 的同一归一二次不变量。
由
$\tau^hU_1=U_1-hv$、
$\tau^hV_2=V_2-hU_1+h(h+1)v/2$
代入归一矩，得到
$$
              \mathcal C_1(z)=
                 \mathcal C_H(z)
                  +\frac{\beta_p h^2}{(1-\beta_p)^2}.
\tag{4}
$$
完全分裂时 $h=0$，但 deck 作用仍保留在整个置换模上。
等式先在原完成证明，再拉回 fine-level 常数扩张；
不把扩张后的底系数 Frobenius 擅自设为恒等。

**5. 准确的剩余效力界。**
在原非平凡纤维 $\mathcal P=\mathbb F_{p^p}$、
$I=\ker N_\Gamma=\Delta\mathcal P$ 内，
$$
              \ker(D_2|_I)=\Delta^3\mathcal P,\qquad
                       \dim\Delta^3\mathcal P=p-3.
\tag{5}
$$
可选非零、非恒定 $b$ 于此空间，仍保留原算术 Frobenius。
另选迹为规定单位的第一 jet $b_1$；
可逆算子 $1-\beta_p\tau^h$ 给与原导数关系相容的唯一权二行值。
将每个 $\tau^jU$ 块赋值 $\tau^jb/u$，其完整 $U$ 迹是原
$\tau^jb$，并与 Frobenius 相容；非恒定性使全 $G$ 评价在
不可约 heart 上非零，而原两矩仍为零。

所以覆盖、heart、source simple zero、算术 Frobenius 和
以上自对偶/微分约束没有单独排除指定两行的 annihilator。
这不是固定 newform 的反例：尚须利用其额外全 Hecke/CM 值信息。
R145 的实际目标仍是 $\mathcal C$ 在原 ordinary CM 点有极点，
不是在其余几何 Cartan 标记处找到极点。

## 来源

具体对象和原 $Q$ 单位见 R134、R139、R141、R142、R145。
原始输入为 Katz（1977）§II、Buium–Poonen（2009）
Theorems 3.5、3.17，以及 Saunders（2022）§3；
各来源的准确规范和公开全文链接已载所链完整笔记及 R141、R145。
(1)–(5) 的其余部分均由本卡及完整笔记直接证明。
