# 原 ψ4 新双槽的单参数 Newton 与 canonical 几何斜率

2026-11-27 UTC。

本注消费[原 ψ4 canonical 正槽与 degree102 负槽](2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)的同一个 binary theta 来源。负槽是实际 wild3 返回后的 degree102 截面，正槽是原 degree34 canonical $S$。本文不把两个 Gaussian 合成一个，也不把新 degree17 图与旧54个 degree34 图认作同一几何类。

纯 Newton 部分给全精度整函数及真实全尾；几何斜率部分明确保持新图的正权比较、固定来源常数、参考端点和共同连续因子。原 canonical 坏条件无条件迫本文指定解析来源的一阶值为零；接回新几何读者还须付清§6列出的实际 cross 与参考端点条件，其反向非零也须保留显示的非退化条件。

## 1. 两个固定来源与原整数坐标

在 $E_0:y^2=x^3+1$ 上用
$$
x=z^{-2}+\cdots,\qquad y=-z^{-3}+\cdots,\qquad
\sigma=z+\cdots,\qquad X=x^3,\qquad dz=dx/(2y).
\tag{1}
$$
正槽严格是 R297 的
$$
S(z)=\frac{\sigma^{34}x^2}{7}
 (7X^4-53X^3-12X^2-80X-128)
=\sum_{m\ge0}s_mz^m,\qquad s_6=1.
\tag{2}
$$
只有 $m\equiv0\bmod6$ 的系数可能非零，而且 $s_0=0$。

负槽保持上述来源文中的完整两个3挠 Weyl 项。记
$$
(r_1,r_4,r_7,r_{10},r_{13},r_{16})
=(256,1376,1216,58,-37,1),
$$
$$
\begin{aligned}
R_{102}={}&
\sum_{a=1,4,7,10,13,16}r_a x^a
 \bigl[
 (-2\delta)^a(y+\delta)^a(y-\delta)^{34-2a}\\
&\hspace{42mm}
 +(2\delta)^a(y-\delta)^a(y+\delta)^{34-2a}
 \bigr],\\
D_-(z)={}&\frac{\sigma(z)^{102}R_{102}(z)}{301056}
          =\sum_{m\ge0}d^-_mz^m .
\end{aligned}
\tag{3}
$$
两个 Weyl 项不能在此分离。每个 $34-2a\ge0$。括号整体在 $y\mapsto-y$ 下为偶，全部 $\delta$ 幂也为偶；再用 $y^2=X+1$ 和 $a\equiv1\bmod3$，得到
$$
D_-=\sigma^{102}xP_{16}(X),\qquad
P_{16}\in\mathbf Z[1/42][X],\quad \deg P_{16}=16,\quad
d^-_4=1.
\tag{4}
$$
这里(4)的最高系数可直接核，不需要另一个有限计算。$a=1$ 项在极阶98的系数是 $-372\cdot256=-95232$；$a=4$ 项是 $288\cdot1376=396288$。其余项的极阶至多92，两项合为301056。式(3)因此从 $z^4$ 起，且仅有 $4\bmod6$ 型。

实际 coherent 负槽并不是 $D_-(Z)$：原来源给每个第 $n$ 槽附带 $\delta^{-n}$，以及固定非零来源常数 $147/\sqrt[3]2$。后一常数连同原 partial Fourier、正槽和实周期规范，均由来源文的实际函数固定；下文把同一整套固定来源幅度记为 $B_k$。本文逐项保留 $\delta^{-n}$，不将它放进一个随 $p$ 可任取的常数。

## 2. 两个完成及全尾

取
$$
p\equiv5\bmod6,\quad p>211,\quad d=p+1=6s,\qquad
c_\sigma=[z^d]\log(\sigma/z),\quad v_p(c_\sigma)=-1,
$$
$$
C_+=34c_\sigma,\qquad C_-=102c_\sigma=3C_+,\qquad
\gamma_\pm=pC_\pm\in\mathcal O^\times .
\tag{5}
$$
当前纯 Newton 系数只需排除 $2,3,7,17$；若使用新几何读者，还保持其实际 level、Artin、整格和 Frobenius 的固定坏位。定义
$$
a_h=C_-^{-h}[z^{dh-2}](D_-e^{-C_-z^d}),\qquad
b_h=C_+^{-h}[z^{dh}](Se^{-C_+z^d}),
\quad h\ge0,
$$
$$
J_-(v)=\sum_{h\ge0}a_h(v)_h,\qquad
J_S(v)=\sum_{h\ge0}b_h(v)_h,\qquad
(v)_h=\prod_{r=0}^{h-1}(v-r).
\tag{6}
$$
负次系数为零，故 $a_0=b_0=0$。$J_S$ 正是同一 Gaussian 和同一 canonical $S$ 的完整原 Newton 函数，不是只取前几项后重新定义的函数。

令 $W=z^2x$、$F=\log(\sigma/z)$、$\mathcal R=p^{-1/(2p)}$。R301 的原圆盘给 $\|W\|_{\mathcal R}\le1$ 及实际去 Gaussian 指数的收敛界。式(4)准确变为
$$
z^2D_-e^{-C_-z^d}
=z^6 e^{102(F-c_\sigma z^d)}
 \sum_{\ell=0}^{16}u_\ell z^{6(16-\ell)}W^{3\ell+1},
\quad u_{16}=1.
\tag{7}
$$
右边全部指数非负且系数整。同样，(2)给 $Se^{-C_+z^d}$ 为 $z^6$ 乘整的非负 $W$ 幂多项式及 $e^{34(F-c_\sigma z^d)}$。因此两个 Gauss 范数都至多 $\mathcal R^6$，从而
$$
v_p(a_h),\ v_p(b_h)
\ge B_{p,h}:=
\left\lceil\frac{h(p-1)+6}{2p}\right\rceil
\qquad(h\ge1).
\tag{8}
$$
这里负槽用了实际 $102$，正槽用了实际 $34$；两者都对相同原 $c_\sigma$ 去 Gaussian。

(8)给整个过收敛级数，并且
$$
J_-(v)=pvK_-(v),\qquad J_S(v)=pvL_S(v),\qquad
K_-,L_S\in\mathcal O\langle v\rangle .
\tag{9}
$$
$L_S(0)=J_S'(0)/p$。端点例如
$$
K_-(0)=\frac1p\sum_{h\ge1}(-1)^{h-1}(h-1)!\,a_h .
\tag{10}
$$
截到 $h\le H$ 后误差赋值至少 $B_{p,H+1}+v_p(H!)-1$；$L_S$ 同式。这保全无限尾。

R614 的更大整窗同样逐项适用(7)：令 $L=(p^2-1)/6=s(p-1)$，真实系数所读指标都是 $hs-1$，所以
$$
\begin{array}{ll}
a_h,b_h\in p^h\mathcal O,&1\le h\le p-1,\\
v_p(a_p),v_p(b_p)\ge p-1,&h=p,\\
v_p(a_h),v_p(b_h)\ge h-2,&p+1\le h\le2p-2 .
\end{array}
\tag{11}
$$
更高项仍用(8)，没有把高度二坏带当成整带。特别以下除 $p$ 的一阶公式都由全尾支持。

## 3. 同一整数权的准确相乘与 δ 因子

对每个整数 $k\ge1$，有限 Gaussian 回卷给
$$
J_-(k)=k!C_-^{-k}d^-_{dk-2},\qquad
J_S(k)=k!C_+^{-k}s_{dk}.
\tag{12}
$$
即使 $p\mid k$，(9)仍给实际整函数；不把 $k$ 当单位约掉。

定义
$$
q_\delta=\delta^{p+1}/3.
\tag{13}
$$
因为 $p$ 惰性，$\delta^p\equiv-\delta\bmod p$，而 $\delta^2=-3$，故 $q_\delta\in1+p\mathcal O$。于是 $q_\delta^{-v}=\exp(-v\log q_\delta)$ 是实际 Tate 解析单位。对整数 $k$，原两个槽是 $n=dk-2$、$n+2=dk$。用(5)、(12)严格得到
$$
\boxed{
\delta^{-(dk-2)}d^-_{dk-2}s_{dk}
=-3q_\delta^{-k}
 \frac{C_+^{2k}}{(k!)^2}\,
 J_-(k)J_S(k).
}
\tag{14}
$$
等号用的是 $\delta^2=-3$ 与 $C_-C_+=3C_+^2$。既没有用模 $p$ 的 $\delta^d\equiv3$ 替换特征零幂，也没有把 $C_-$ 偷换成 $C_+$。

$C_+^{2k}/(k!)^2$ 仅在合法整数权使用；本注不把它延拓为 $v$ 的函数。在原正权比较中逐项消去这个共同因子后，完整解析来源是
$$
\mathcal N(v)=-3q_\delta^{-v}J_-(v)J_S(v).
\tag{15}
$$
有限 theta 槽的 $n!$、$(n+2)!$ 和原 geometric Gamma 若出现在正权公式中，仍须先与(14)逐项合并，不能把(14)中的 $k!$ 当作那些阶乘。

## 4. canonical 坏条件实际迫哪一个一阶值为零

保持负槽的原 $pv$ 正则化，定义
$$
\mathcal R_{\rm can}(v)
:=\frac{\mathcal N(v)}{pv}
=-3q_\delta^{-v}K_-(v)J_S(v)
\in pv\,\mathcal O\langle v\rangle .
\tag{16}
$$
它的端点自动为零，但一阶准确为
$$
\boxed{
\mathcal R_{\rm can}(0)=0,\qquad
\mathcal R_{\rm can}'(0)
=-3K_-(0)J_S'(0).
}
\tag{17}
$$
$q_\delta$ 的导数项在这里因真正的 $J_S(0)=0$ 消失，不是因为把 $\log q_\delta$ 当零。比如二阶仍保
$$
\mathcal R_{\rm can}''(0)
=-3\left[
 K_-(0)J_S''(0)
 +2\{K_-'(0)-(\log q_\delta)K_-(0)\}J_S'(0)
 \right].
\tag{18}
$$

原 canonical 坏条件所给的完整必要行 $J_S'(0)=0$，因此确实推出
$$
\mathcal R_{\rm can}\in v^2\mathcal O\langle v\rangle.
\tag{19}
$$
若 $K_-(0)\ne0$，(17)在系数域中给双向等价；若要求剩余整格上的等价，则须另有 $K_-(0)\in\mathcal O^\times$。固定正权 $d^-_4=s_6=1$ 只锁来源和非零 anchor，不证明任意惰性 $p$ 的 $K_-(0)$ 为单位。

还可以对两个真实零因子同时正规化：
$$
\frac{\mathcal N(v)}{p^2v^2}
=-3q_\delta^{-v}K_-(v)L_S(v).
\tag{20}
$$
其 augmentation 为 $-3K_-(0)J_S'(0)/p$。这与(17)是同一一阶信息；不能把(20)命名为另一个已证非零几何端点。

## 5. 首层实际系数及没有消失的费用

由(8)、(11)，整个 Tate 代数中
$$
K_-(v)\equiv\frac{d^-_{p-1}}{\gamma_-}\pmod p,\qquad
L_S(v)\equiv\frac{s_{p+1}}{\gamma_+}\pmod p .
\tag{21}
$$
因此
$$
\boxed{
\frac{\mathcal R_{\rm can}'(0)}p
\equiv-\frac{d^-_{p-1}s_{p+1}}{\gamma_+^2}\pmod p.
}
\tag{22}
$$
这里只消去了已知的 $\gamma_-=3\gamma_+$；两个实际来源系数均保留。特别它不是旧三条 PB4 的某一 $d_{j,p-1}$，也不是由 $d^-_4=1$ 自动得出的单位。

在所有精度中，$J_S'(0)$ 仍是(10)对应的完整无限和。坏条件只能在保留这些低卷积和高尾之后使用；(22)本身只是必要首层，不可替代(17)。

## 6. 原参数与接回新几何读者的准确条件

上述来源文使用的原参数为
$$
u\in\mathbf Z_p,\qquad
n(u)=(p^2-1)u-2,\qquad v=(p-1)u.
\tag{23}
$$
新表示是 $\pi_4=\operatorname{AI}(\nu_4^2)$。canonical 分支的两个因子为 $\eta_1\psi_4^{2n+1}$ 与 $\eta_1\psi_4^{2n+5}$，其中 $\eta_1=\psi_{17}/\psi_4$。正槽 $m=n+2\equiv0\bmod6$，$\eta_1^6=1$，故第二因子严格为 $\psi_{17}^{2m+1}$。这支付原 $S$，没有仅凭相同无穷型替换来源。

几何端必须用实际 full2 sign、完整3处向量及18个带权 cyclic17 商，并保 full9、Cor、Frobenius 和 fixed-base $p^2$ 返回；新来源文支付所需的全部局部向量和实际同源类型，尚未支付新 fulllevel 图的完整 fp／权族比较。它们并不是旧 R1049 的54个 degree34 图；以下明确以这个新的实际比较为前提，不将其视为已经由旧文自动完成。

精确的后继条件如下。须先构造这些新图的完整正权族 $\mathcal L_k(u)$，按实际 Fourier、$\sigma$ 和实周期运输固定 $B_k\ne0$；再在各原有限分支上，把全部公共正权 Gamma、Tate、Euler 与(14)同一整数幂逐项消去，证明真实连续 cross
$$
R_k(v)=-3q_\delta^{-v}K_{-,k}(v)J_{\beta,k}(v),
\quad
\frac{\mathcal L_k(u)}{B_k}R_r(v)
=\frac{\mathcal L_r(u)}{B_r}R_k(v).
\tag{24}
$$
canonical 分支 $k=1$ 的 $J_{\beta,1}$ 正是 $J_S$。其他两个分支的正槽是 R306 的实际 $H_3,H_5$，其真空不能拿 $S$ 的零真空代替。

若已独立付清上述完整正权比较和连续性，且某个参考 $R_r(0)$ 为单位，则(24)定义真实共同连续因子
$$
F_{\rm new}(u)=\frac{\mathcal L_r(u)}{B_rR_r((p-1)u)} .
\tag{25}
$$
本注不从一个正权 anchor 断言 $F_{\rm new}(0)$ 为单位。若参考只在系数域中非零，可在一个足够小邻域作同样的有理连续定义，但不声称其整单位性。

由于 $R_1(0)=0$，即使不知道 $F_{\rm new}$ 可微，(24)–(25)仍给真正导数
$$
\boxed{
\mathcal L_1(0)=0,\qquad
\mathcal L_1'(0)
=-3(p-1)B_1F_{\rm new}(0)\,
 K_-(0)J_S'(0).
}
\tag{26}
$$
证明是差商：$F_{\rm new}(u)\to F_{\rm new}(0)$，而 $R_1((p-1)u)/u$ 有(17)给出的极限。没有对未知公共周期求导。

所以一旦以上实际比较前提付清，原坏条件确实迫这个同源几何斜率 $\mathcal L_1'(0)=0$。目前无条件已付的是(14)–(22)；本节没有另行宣称新几何 cross 已完成。若要反过来迫原 canonical 非零，还须证明(26)的实际左边非零，并控制 $F_{\rm new}(0)$ 与 $K_-(0)$。本注没有把这两项尚缺的非退化性，藏进“共同周期”或 n4 的非零 anchor 中。

## 7. 原依据与结论边界

- [原 ψ4 canonical 正槽与 degree102 负槽](2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)：实际 finite tensor、两个完整 Weyl 项、$\delta^{-n}$、新 full2/full9/degree17 所需的有限向量；本文不重复该有限来源证明，也不以它替代新的几何正权比较。
- R297、R306：原 $S,H_3,H_5$ 的真实 Schwartz 与整来源；R989 的 canonical 坏条件保持原完整读者。
- R301 §§2–6：同一高度二圆盘、$pc_\sigma$ 及过收敛 Newton 全尾。
- R614(9)、(18)、(21)–(23)：同一完成后的整窗、两坏带和完整高尾；(7)显示本次 negative102 符合全部非负整数幂条件。
- [原 type4 负二 Newton](2026-11-27-original-type-four-inert-negative-two-newton-and-signed-line.md) §§2–3：本次复用同一个有限 Gaussian 回卷证明，不把旧三条 degree34 来源换成新的102来源。
- [原 canonical 二阶导数 Newton](2026-11-27-original-canonical-second-derivative-newton-and-full-connection.md)：它保留完整 $\zeta$／heat 费用，本注不删除那些补源，也不把其 CM 单点零作横向微分。

本注的新增实质是(14)的两个真实 completion 与 $\delta$ 因子全归一、(17)的无条件同源一阶必要零，以及(26)在显示实际几何比较条件下的准确返回。一个新的非零常数、另一条点的非零，均不能替代(26)尚需的真实几何斜率非零。
