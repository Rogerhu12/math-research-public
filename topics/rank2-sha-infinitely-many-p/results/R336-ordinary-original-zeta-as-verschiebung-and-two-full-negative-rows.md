# R336 — 原普通 ζ 的精确曲率、真实 Verschiebung 覆盖与两个完整负矩行

日期：2026-11-13。**状态：以下有理原函数、曲率的符号、原 σ 的
Artin–Schreier 方程、真实可分 $p$ 同源、其核多项式的完整 norm-three
方程，以及两个原负矩的完整 Laurent/Lagrange 行均已证明。尚未证明
两个固定负矩对所有充分大普通 $p$ 联合非零；也没有由核多项式底部
系数非零直接推出这两个行非零。主目标未完成。**

本文接 R330、R332、R333。所有系数和测度仍来自 R316 的原
degree-one σ 与 degree-two Θ；没有更换 Schwartz 向量或普通周期。

## 1. 原规范、整性与准确 Hasse 标量

取
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
\omega_E=\frac{dx}{2y}=dz,\qquad
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad \sigma=z+\cdots.
\tag{1}
$$
固定普通素数 $p>7$，写
$$
p=6s+1,\qquad D=\frac{d}{dz},\qquad
H=\binom{3s}{s}b^s\in\mathbf F_p^\times.
\tag{2}
$$
以下特征 $p$ 的函数恒等式在 $E_b/\mathbf F_p$ 上成立；需要几何
点时把常数域扩大到 $k=\overline{\mathbf F}_p$。$H\ne0$，因为
$3s<p$ 且 $p\nmid b$。同样的证明适用于任意整单位 $b$。

R300、R316 已支付原 Mazur–Tate sigma 整性以及三次 CM 消去
Gaussian 修正。因此把 σ 写入原整形式参数后可以约化；其
对数导数也可以在形式 Laurent 域中约化。下文的 ζ 始终是
$$
\zeta=D\log\sigma,\qquad D\zeta=-x.
\tag{3}
$$
它不是任意选择的 $-x\omega_E$ 的特征 $p$ 原函数。

先准确核定
$$
\boxed{D^p=HD.}
\tag{4}
$$
$D^p$ 是平移不变导子，所以是 $D$ 的常数倍。Cartier 算子的
原规范为
$$
\mathcal C\left(\sum a_j u^jdu\right)
=\sum a_{pj+p-1}^{1/p}u^jdu.
$$
在本曲线上
$$
\omega_E=\frac{(x^3+b)^{3s}}{2y^p}\,dx,
\qquad \mathcal C\omega_E=H^{1/p}\omega_E:
\tag{5}
$$
多项式次数 $9s<2p-1$，唯一要读的次数是 $p-1=6s$，其系数恰是
$\binom{3s}{2s}b^s$。这里 Cartier 与不变导子的对偶规范没有额外
$2$：若局部 $D=a\partial_u$，直接展开 Leibniz 公式给
$$
\frac{D^pu}{Du}=-a^p\partial_u^{p-1}(a^{-1}).
$$
把 $a^{-1}$ 按 $1,u,\ldots,u^{p-1}$ 分解为 $p$ 次幂系数后，右端
正是 $((\mathcal C\omega_E)(D))^p$。这证明 (4) 与 (5) 的归一一致。

## 2. 一个真正的有理 ζ 原函数

只在原点的形式盘使用
$$
u=x^{-1/2}=z+\cdots,\qquad v=-y/x^{3/2}=1+\cdots,
\qquad v^2=1+bu^6,
\tag{6}
$$
于是 $Du=v,Dv=3bu^5$。定义
$$
a_0=1,\qquad
a_n=-b\frac{6n-4}{6n-1}a_{n-1}\quad(1\le n\le2s),
\qquad P_p(T)=\sum_{n=0}^{2s}a_nT^n,
\tag{7}
$$
$$
\boxed{Z=-\frac yx P_p(x^{-3})=\frac vu P_p(u^6).}
\tag{8}
$$
虽然 (6) 是局部记号，(8) 是 $\mathbf F_p(E_b)$ 中的真正有理函数。
所有 $6n-1$ 在该范围内都非零：首个可被 $p$ 整除的这种分母
位于 $n=5s+1>2s$。

逐项恒等式是
$$
D(vu^{6n-1})=(6n-1)u^{6n-2}+(6n+2)bu^{6n+4}.
\tag{9}
$$
(7) 消去相邻项，最后一项的系数为 $12s+2=2p$，所以
$$
\boxed{DZ=-x.}
\tag{10}
$$
它在 $O$ 是一阶极，在 $Q_\pm=(0,\pm\sqrt b)$ 至多为 $p$ 阶极。
写为超几何多项式也没有额外选择：
$$
a_n=(-b)^n\frac{(1/3)_n}{(5/6)_n}
       =(-b)^n\frac{(-2s)_n}{(s+1)_n}\quad\bmod p.
\tag{11}
$$
特别
$$
a_{2s}=\frac{b^{2s}}{\binom{3s}{s}},\qquad
Ha_{2s}=b^{3s}.
\tag{12}
$$
这也核对了三挠点处最高极与 (2) 的实际 Hasse 标量。

## 3. 完整 pole/μ6 证明及曲率负号

先证明
$$
D^{p-1}x=Hx.
\tag{13}
$$
由 (4)，两边之差被 $D$ 杀掉，因而属于 $k(E_b)^p$。它仅在 $O$
有极，阶至多 $p+1$；其 $p$ 次根至多在 $O$ 有一阶极。椭圆曲线
不存在这种非恒有理函数，所以差是常数。两项都有非平凡的
$\mu_6$ 型 $r^{-2}$，故常数为零。这里没有把 $D$ 的整个核错认成
常数域。

由 (10)、(13)，
$$
G=D^{p-2}x+HZ
$$
也属于 $k(E_b)^p$。其 $p$ 次根仅可能在 $O,Q_+,Q_-$ 各有一阶极。
Riemann–Roch 给出准确的三维空间
$$
L(O+Q_++Q_-)=\langle1,x^{-1},y/x\rangle.
\tag{14}
$$
$G$ 以及它的 $p$ 次根的 $\mu_6$ 型均为 $r^{-1}$，所以这个根只能
是 $c\,y/x$。在 $O$，$D^{p-2}x$ 的首项是
$$
(-1)^{p-2}(p-1)!\,u^{-p}=u^{-p},
$$
而 $(y/x)^p$ 的首项是 $-u^{-p}$；$HZ$ 仅一阶极。因此 $c=-1$，得到
$$
\boxed{D^{p-2}x+HZ=-\left(\frac yx\right)^p.}
\tag{15}
$$
令
$$
L_0=Z+y/x=\frac vu(P_p(u^6)-1).
\tag{16}
$$
则准确的标量障碍为
$$
q(Z):=Z^p-HZ-D^{p-2}x=L_0^p.
\tag{17}
$$
若连接取 $\nabla_Z=D-Z$，其 restricted $p$-curvature 是
$$
\boxed{\nabla_Z^p-H\nabla_Z=-L_0^p.}
\tag{18}
$$
负号必须保留。事实上 Jacobson–Leibniz 公式为
$(D+f)^p=D^p+D^{p-1}f+f^p$；代入 $f=-Z$，再用 $DZ=-x$，
直接给 (18)。(17) 的正号不能直接当作这个连接的曲率符号。

## 4. 原 σ 的准确 AS 方程与完整原支

原整 σ 在形式域中是 $D-\zeta$ 的非零水平解，所以该连接的曲率
严格为零，而不是只在若干初始系数上为零。因此
$$
\boxed{\zeta^p-H\zeta=D^{p-2}x.}
\tag{19}
$$
设
$$
A=\sigma/u,\qquad \Theta=x\sigma^2=A^2,\qquad
L=D\log A=\zeta+y/x.
\tag{20}
$$
由 (15)、(19) 得到三个完全相同的形式：
$$
\boxed{L^p-HL=-HL_0,\qquad
\zeta-Z=H^{-1}L^p,\qquad L=L_0+H^{-1}L^p.}
\tag{21}
$$
特别原条件 $L\in u^5k[[u^6]]$ 指定唯一支，并且
$$
\boxed{L=\sum_{j\ge0}H^{-j}L_0^{p^j}.}
\tag{22}
$$
这里 $H\in\mathbf F_p$，故反复 Frobenius 后的系数准确为 $H^{-j}$。
该式在 $u$-进拓扑收敛。由于
$$
L_0=-\frac{2b}{5}u^5+\cdots,
$$
原 ζ 与有理 $Z$ 的第一处差异准确在 $u^{5p}$，其系数非零。
不能把 $Z$ 当作原 ζ 的全部约化；(21) 给出了欠缺的整项。

## 5. AS 覆盖就是实际可分 p 同源

考虑 (19) 定义的函数域扩张。它在 $E_b\setminus\{O\}$ 上 étale，
因为右端无极，且左端对 ζ 的导数是 $-H$。在 $O$，原整 σ 给出的
Laurent 支 ζ 使方程在完成域中分裂；因此这里也没有分歧。

该覆盖几何连通。若有全局有理根，它在 $O$ 外不能有极，而在 $O$
只能有一阶极，因为右端的极阶恰为 $p$。这与 (14) 的一点评价版
$L(O)=k$ 矛盾。把 ζ 乘常数后是标准 AS 方程，次数为素数 $p$，
无全局根就给不可约次数 $p$。因此其光滑完备化是连通 étale
$p$ 覆盖；Hurwitz 给 genus 一。

选定原 Laurent 支上方的点为原点，覆盖成为椭圆曲线的可分
$p$ 同源。其对偶是纯不可分次数 $p$，因而在保原点的同构下，
这正是标准
$$
V:E_b^{(p)}\longrightarrow E_b,\qquad
V^*\omega_E=H\omega_{E^{(p)}}.
\tag{23}
$$
在本固定 $b\in\mathbf F_p$ 的方程中，$E_b^{(p)}$ 仍用同一方程。
它也是 R300、R316 所选 $[\bar\pi]$ 的真实约化；$[\pi]$ 约化为
Frobenius，且 $\bar\pi\equiv H\pmod p$。

令 $D'$ 是源曲线的不变导子。实际核的 Miller 多项式可取
$$
f_V(x')=\prod_{\{Q,-Q\}\subset\ker V\setminus\{0\}}
(x'-x'(Q)),
\qquad
\operatorname{div}(f_V)=\sum_{Q\ne0}(Q)-(p-1)(O').
\tag{24}
$$
核受 $\mu_6$ 保持，且 $Q_\pm$ 的阶为三，故不在核中。于是
$$
\boxed{f_V=P(X'),\qquad X'=x'^3,\quad
P\text{ monic},\quad\deg P=s,\quad P(0)\ne0.}
\tag{25}
$$
这是实际 kernel polynomial，不是任意 degree-$s$ 多项式。

在源曲线上，$V^*(\zeta\omega_E)$ 与 $d\log f_V$ 有相同的简单极和
留数；在 $O'$，$-(p-1)=1$ 也在特征 $p$ 中给留数一。它们之差
是 holomorphic differential。两者都在 $\mu_6$ 下不变，而任何
非零 holomorphic differential 有非平凡型 $r$，所以
$$
\boxed{V^*(\zeta\omega_E)=d\log f_V.}
\tag{26}
$$
因此 $V^*\sigma=f_V g^p$，其中 $g$ 是原点附近的实际局部函数。
在 $u'=x'^{-1/2}$ 中，$g=Hu'+O(u'^7)$；这是由 (23) 的首项和
$\mu_6$ 型一确定的。故
$$
V^*\sigma=H u'^pP(u'^{-6})(1+O(u'^{6p})).
\tag{27}
$$
这里保留了真实 $p$ 次幂因子；没有把全部 σ 当作一个全局有理函数。

## 6. 完整 norm-three 方程及真正底部单位

下文把源坐标的撇号省去。由 (26) 连续微分，
$$
H^2(x\circ V)f_V^2=(D f_V)^2-f_VD^2f_V=xT_P(X),
\tag{28}
$$
其中
$$
\boxed{T_P(X)=36X(X+b)(P'^2-PP'')
-6(7X+4b)PP'.}
\tag{29}
$$
它准确为 monic degree $2s$：首项系数 $-6s=1\pmod p$。这里使用
$DX=6x^2y$、$D^2X=6x(7X+4b)$。

取 $\delta^2=-3$，保持原
$$
\sigma(\delta z)=\delta\sigma(z)\Theta(z)=\delta x(z)\sigma(z)^3,
\qquad x(\delta z)^3=-\frac{(X+4b)^3}{27X^2}.
\tag{30}
$$
R316 的真实 CM division 身份为
$$
\sigma(\bar\pi z)=\bar\pi\sigma(z)^p f_{\bar\pi}(x(z)).
\tag{31}
$$
其 monic 多项式整，约化就是 (25)：非零 étale 核点不在形式核中，
所以它们的 $x$ 坐标整。把 (30)、(31) 按两种次序复合，保留
$\delta^p,\bar\pi^3$ 后再约化，利用 $\delta^{p-1}=1$ 得
$$
\boxed{
X^{2s}P\left(-\frac{(X+4b)^3}{27X^2}\right)=P(X)T_P(X).
}
\tag{32}
$$
左边的分母被 $X^{2s}$ 全部消掉。这是整个原核多项式方程，不只是
无穷远处的一个系数关系。

再核真正的底部系数。写 $\epsilon_3=b^{(p-1)/2}\in\{\pm1\}$。
Frobenius 在 $Q_\pm$ 上作用为 $\epsilon_3$；由于 $p\equiv1\pmod3$，
$V\circ\operatorname{Frob}=[p]$ 迫 $VQ_\pm=\epsilon_3Q_\pm$。
在 $Q=Q_+$，(26) 的函数式为
$$
D\log f_V=H(\zeta\circ V).
$$
两边再微分两次，在 $x=0$ 的局部参数中比较二次项，得到
$$
48y(Q)^3\frac{P'(0)}{P(0)}=-2H^3y(VQ).
$$
所以
$$
\boxed{\frac{P'(0)}{P(0)}=-\frac{H^3\epsilon_3}{24b}\ne0.}
\tag{33}
$$
(32) 在 $X=0$ 给
$$
-24bP(0)^2P'(0)=(-64b^3/27)^s.
$$
用 $\epsilon_3=b^{3s}$、$(-27)^s=1$、$64^s=2^{p-1}=1$ 化简，得
$$
\boxed{(HP(0))^3=1.}
\tag{34}
$$
因此底部的两个系数确实都是单位；它们的范围由真实同源而非一个
任意有限模型支付。

## 7. 两个原负矩读到哪些完整行

写
$$
\frac{\sigma(z)}z=C(q)=\sum_{j\ge0}c_jq^j,\qquad
\Theta(z)=B(q)=\sum_{j\ge0}d_jq^j,\qquad q=z^6.
\tag{35}
$$
所需共同下标是 $n=s-1$。R316 的同一普通周期记为 $\Omega_p$，则
$$
\boxed{
I_{\sigma,-5}\equiv\Omega_p^{p-6}(p-6)!\,c_{s-1},\qquad
I_{\Theta,-6}\equiv\Omega_p^{p-7}(p-7)!\,d_{s-1}\pmod p.
}
\tag{36}
$$
证明只用单位上的 $x^{-5}=x^{p-6}$、$x^{-6}=x^{p-7}\pmod p$，以及
整有界测度在非单位上的正权矩为零模 $p$；所有周期因子均保留。

真实 CM pullback 给出准确的有限 Laurent 行
$$
\boxed{
c_{s-1}=H^6[z^{-6}]P(x(z)^3),
\qquad
d_{s-1}=H^6[z^{-p-7}]x(z)T_P(x(z)^3)
\quad\bmod p.
}
\tag{37}
$$
为核定形式反演没有被省略，直接用特征零 (31)。在所需范围
$q^{<s}$，$C(q)$ 整，所以 $C(q)^p=C(q)^{2p}=1\pmod{(p,q^s)}$。
比较 (31) 的 $z^{p-6}$ 系数给
$\bar\pi^{p-6}c_{s-1}=\bar\pi[z^{-6}]P$。比较其平方再乘
$x(\bar\pi z)$ 的 $z^{p-7}$ 系数，并用 (28)，得到第二行。
$\bar\pi\equiv H$、$H^{p-1}=1$ 给共同因子 $H^6$。
只需 $q^{<s}$：最高极与目标极的差均为 $p-7$，因此更高处
可能有分母的系数不会进入 (37)。

还可以把 (37) 完全写回原 $u$ 坐标，明确保留椭圆对数因子。令
$$
t=-bu^6,\qquad z=u h(t),\qquad
h(t)=\sum_{j\ge0}\frac{(1/2)_j}{j!(6j+1)}t^j,
\tag{38}
$$
并在 $\mathbf F_p[t]/(t^s)$ 中置
$$
E_p(t)=\exp\left(\sum_{j=1}^{s-1}
\frac{(1/3)_j}{(5/6)_j}\frac{t^j}{6j}\right).
\tag{39}
$$
这些有限系数的全部分母是单位。由 (21)，$A=E_p(t)\pmod{t^s}$。
Cauchy 系数换元精确给
$$
\boxed{
c_{s-1}=(-b)^{s-1}[t^{s-1}]E_p(t)h(t)^5(1-t)^{-1/2},
}
\tag{40}
$$
$$
\boxed{
d_{s-1}=(-b)^{s-1}[t^{s-1}]E_p(t)^2h(t)^6(1-t)^{-1/2}
\quad\bmod p.
}
\tag{41}
$$
这里实际换元先产生 $h^{5-p}$ 和 $h^{6-p}$；只在本有限范围内
用 Frobenius 把它们分别化为 $h^5,h^6$。这些式子是模 $p$ 的
完整行，不能当作有理数上的相等系数公式，也不能删去 $h$。

## 8. 原 norm-three 行的消元及尚欠的非零输入

由 (30)，$C(-27q)=C(q)B(q)$。在 $n=s-1$，
$(-27)^n=-1/27$，因此完整顶项关系为
$$
\boxed{d_n+\frac{28}{27}c_n+
\sum_{j=1}^{n-1}c_jd_{n-j}=0\quad\bmod p.}
\tag{42}
$$
$28/27$ 对本全部 $p>7$ 是单位。若两个指定原行都为零，则真实
较低项卷积必须为零；(42) 本身没有证明该卷积非零。

尤其 (34) 不直接解决这个问题。第一条 Laurent 行
$[z^{-6}]P(x^3)$ 完全不读 $P(0)$，且每个正次数单项式均可能通过
实际 $x(z)$ 的低阶项贡献。第二行仅读 $T_P$ 次数至少 $s+1$ 的
部分；在 (29) 中，与 $P(0)$ 配对的项次数至多为 $s$，所以这条
行也不读 $P(0)$。准确的非零 $P'(0)/P(0)$ 仍须通过完整 (32) 和
(37)–(41) 才能传到原观察，不能把两种行直接认作相同。

本结果实际新增的是：原 ζ 的完整曲率及真实原支不再未知；它们
来自确定的可分 $p$ 同源，两个原固定负矩也都有带全部坐标因子的
实际核多项式公式。本文没有以这些新有限来源的存在替代跨 $p$
非消失，也没有将负矩的一个非零深区贡献替代整个 $J_S'$。

## 9. 可复现证书与引用范围

[精确脚本](../scripts/check-jzero-ordinary-as-verschiebung-and-two-negative-rows.py)
和 [JSON](../scripts/check-jzero-ordinary-as-verschiebung-and-two-negative-rows.json)
核定符号/递推，并只重建一个实际普通纤维 $p=13,b=17$：从标准
division-polynomial 递推取真实可分核，核定原曲线方程、完整 (32)、
(33)–(34)、第一 AS 修正 $u^{65}$，以及 (37)–(41) 的原系数。
该有限证书不承担无穷素数推断；各全 $p$ 命题的证明在上文。

所用原来源：

- [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)：
  原 σ 整性、同一 CM 嵌入及完整 prime core。
- [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：
  两条原低次来源、同一普通周期及全部 CM division 规范。
- [R330](R330-original-target-seven-eight-carry-and-sixfold-central-difference.md)、
  [R332](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md)、
  [R333](R333-six-original-sigma-inputs-and-two-quadratic-negative-moment-return.md)：
  两固定负矩在原完整中央式中的具体位置；其全 carry 继续保留。
