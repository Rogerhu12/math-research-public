# 实际完整 theta carry 的中央留数源：准确同权作用与全部深度

日期：2026-11-12。状态：下述非齐次项由原两变量 theta、
真实 $[-p]$ 平方 Frobenius 及原 $256$ 标签直接构造。
它的固定 Bol 留数投影、全部中央权的生成式和完整导数门槛均已核定。
没有把固定纤维的同源拉回误认为底参数的 Frobenius，
也没有得到新的跨素数非零结论。

本文连接
[R92 的完整 theta 方程](2026-11-12-original-theta-square-frobenius-and-witt-trace.md)、
[R95 的真实单步分解](2026-11-12-geometric-p-step-theta-and-ramified-witt-carry.md)
与
[R94 的固定权三留数线](2026-11-12-central-principal-parts-pf-bol-residue.md)。

## 1. 换成准确提取原对角的正式单位

仍取原 $E_{17}$、$f=34(1+i)$、$N=68$、原轨道
$\mathcal S$ 和二挠点参考 $T=(0,0)$。
固定惰性 $p\ge7$，写
\[
a=-p,\qquad q=p^2.
\]
因为 $a\equiv1\pmod4$，标量 $a$ 保持原 $\mathcal S$。
这也等价于平方算术 Frobenius 在该原轨道上的作用。

R92 使用整形式群参数中的单位
$U_P=Z(w)\Theta_P(z,w)$。
为了准确取原 $d_m$，本篇改写为
\[
W_P(z,w)=w\Theta_P(z,w)=1+X_P(z,w),\qquad
X_P(z,0)=0.
\tag{1}
\]
这里 $z,w$ 是加法参数。没有把 $W_P$ 声称为全盘整级数。
对 $m\ge1$，原定义准确成为
\[
d_m=[z^m w^{m+1}]\sum_{P\in\mathcal S}W_P(z,w).
\tag{2}
\]

由 R92 的同源公式，
\[
W_{aP}(az,aw)=W_P(z,w)^q E_{p,P}(z,w),
\tag{3}
\]
其中实际非齐次正式修正为
\[
\boxed{\quad
E_{p,P}(z,w)=
 \frac{a\,w^{1-q}}{\Psi_a(w)}
 \frac{\Psi_a(P+z+w)}{\Psi_a(P+z)}.
\quad}
\tag{4}
\]
第一个比值在 $w=0$ 的可去值为一，故
$E_{p,P}(z,0)=1$。
与 R92 的 $D_{a,P}$ 的准确关系是
\[
E_{p,P}
 =\frac{aw}{Z(aw)}
    \left(\frac{Z(w)}w\right)^qD_{a,P}.
\tag{5}
\]
因此公共 $w/Z$ 因子完整保留；不能把 $E_{p,P}$ 直接替成
$D_{a,P}$，也不能由后者在整形式群坐标中的 $1+p$ 整性，
不经换元就宣称前者所有加法系数均整。
这里 $D_{a,P}$ 是曲面上的有理函数；$E_{p,P}$
额外含加法坐标 $w$，本篇没有把这个坐标当作椭圆曲线上的有理函数。

若要从真正 $p$ 同源逐步构造 (4)，R95 的负对偶公式给
$D_{a,P}=D_{\varphi,P}^p\varphi^*D_{-\widehat\varphi,\varphi P}$，
再作 (5)。每枝的 $1+\mathfrak m$ 和整个两步的 $1+p$
仍是两个不同的整格结论。

## 2. 不以中央系数定义的实际非线性源

直接用 (1)、(4) 构造
\[
\boxed{\quad
\begin{aligned}
\mathcal N_{p,P}
={}&(E_{p,P}-1)(1+qX_P)\\
 &+E_{p,P}\sum_{k=2}^{q}\binom qk X_P^k,\qquad
\mathcal N_p=\sum_{P\in\mathcal S}\mathcal N_{p,P}.
\end{aligned}
\quad}
\tag{6}
\]
它是实际有限 binomial 多项式及实际除法函数的组合，
不是把待求 $d_m$ 乘一个常数来命名。
恒等式
\[
(1+X_P)^qE_{p,P}=1+qX_P+\mathcal N_{p,P}
\tag{7}
\]
证明 (6) 保留原标签的逐项指数化与所有交叉项。
如改用 $\sum W_P$ 的 $q$ 次幂书写，必须再减去
$p\,\mathfrak C_q((W_P)_P)$；(6) 已经逐标签保留这些项，
没有把原标签和变成一个范数。

还有一个可实际递推的严格三角性：
固定总次数 $D>0$，$\mathcal N_{p,P}$ 的 $D$ 次齐次部分
仅用到 $E_{p,P}$ 的次数至多 $D$ 部分和 $X_P$
的次数严格小于 $D$ 部分。
因为 $E_{p,P}-1$、$X_P$ 均无常数项，
所有含 $X_P$ 的项至少另乘一个正次数因子。
这里较低的输入是全部混合 jet，不仅是较低的中央系数。

由 (3)、(7) 及 $a\mathcal S=\mathcal S$，取原准确对角得到
\[
\boxed{\quad
[z^m w^{m+1}]\mathcal N_p
  =(a^{2m+1}-q)d_m
  =-p^2(1+p^{2m-1})d_m
\qquad(m\ge1).
\quad}
\tag{8}
\]
特别这里是同一个 $m$。真实同源在加法变量中是
$(z,w)\mapsto(-pz,-pw)$，不把双指标 $(m,m+1)$
改成 $(qm,qm+1)$。

### 2.1 全标签的有限置换算子与二次初值

也可在取轨道和之前逐总次数求解。设
$\mathbf W_D=( [W_P]_D )_{P\in\mathcal S}$，
$P_a$ 是把 $P$ 送到 $aP$ 的置换矩阵。
(3)、(7) 准确给
\[
(a^DP_a-qI)\mathbf W_D=\mathbf N_D.
\tag{9}
\]
对 $D\ge3$，它在原未分歧系数域上的逆是
\[
(a^DP_a-qI)^{-1}
 =-\frac1q\sum_{j\ge0}(a^D/q)^jP_a^j.
\tag{10}
\]
由于 $v_p(a^D/q)=D-2>0$，此和收敛，且整体恰付至多
两层 $p$ 的线性格成本。$D=1$ 时可改写为
\[
(aP_a-qI)^{-1}
 =a^{-1}(I-(q/a)P_a^{-1})^{-1}P_a^{-1},
\]
其中 $q/a=-p$，付至多一层 $p$。

$D=2$ 时的核是 $P_a$ 不变部分，须使用原 theta 的真实
二次初值。R92 已准确给
\[
[\log W_P]_2=-x(P)(zw+w^2/2);
\tag{11}
\]
因为 $w/Z(w)=1+O(w^4)$，它与 R92 的规范一致。
由 (11) 及已求得的一次项确定 $[W_P]_2$ 后，
(9)–(10) 给所有更高混合 jet 的唯一重建。
这与 R92 的二次歧义分类完全吻合。

因此 (8) 不是仅仅观察两个任意标量相等：
(4)、(6)、(9) 给出准确有限标签算法。
但 (10) 是逐总次数的算法，其 $E$ 输入、所需混合 jet
和最后取对角的次数都随 $m$ 增长。
它还不是一条仅在固定个数中央系数之间闭合的线性递推。

## 3. 真正投影到 R94 的固定留数线

沿用全权一规范
\[
q_0=-f^2/\sqrt{17},\qquad
e_m=d_m/f^{2m+1},\qquad
e_4=\frac{25}{2^9\,17^{10}}.
\]
对 $4\mid m$、$m\ge4$，定义准确尺度
\[
\kappa_m=\frac{m!\,q_0^{m-4}}
                  {24\,e_4\,f^{2m+1}}.
\tag{12}
\]
R47/R51 的同一中央 Borel 公式给
\[
C_m=\kappa_m d_m,\qquad
\mathcal B_1(u)=\sum_{4\mid m}C_mu^m=K(t(u))M_e(t(u)),
\qquad C_4=1.
\tag{13}
\]
虽然 (12) 可先在固定代数系数域中写出，(13) 的 $C_m$ 均有理。

R94 的主部及其 Bol 留数是
\[
f_m=t^{-m-1}
 \left[\frac{M_eK^{m-1}}{(1-4t^2)J^{m+1}}\right]_{\le m},
\qquad
[f_m\omega\,dt]=C_m\mathfrak c_0.
\tag{14}
\]
所以实际 theta 源的准确留数投影为
\[
\boxed{\quad
\kappa_m[z^m w^{m+1}]\mathcal N_p\;\mathfrak c_0
  =-p^2(1+p^{2m-1})[f_m\omega\,dt].
\quad}
\tag{15}
\]
乘子中的 $1+p^{2m-1}$ 是 $p$ 单位，没有未计算的周期或角色。

这也明确排除一种过强简化：
不能把完整 theta carry 的中央部分一概称为 Bol exact。
实际固定 $m=4$ 已有
\[
f_4=t^{-1},\qquad
\kappa_4[z^4w^5]\mathcal N_p\;\mathfrak c_0
 =-p^2(1+p^7)\mathfrak c_0\ne0.
\tag{16}
\]
这使用的正是原实际对象，不是另造局部模型。
它没有据此推断移动临界权的源模 $p$ 非零。

还可把全部权同时写成一个准确生成式。对任意双变量正式级数
$F$，令
\[
\mathscr H(F)(u)=
\sum_{\substack{m\ge4\\4\mid m}}
 \kappa_m[z^m w^{m+1}]F\;u^m.
\]
则 (8) 等价于
\[
\boxed{\qquad
\mathscr H(\mathcal N_p)(u)
  =-p^2\mathcal B_1(u)-p\mathcal B_1(p^2u).
\qquad}
\tag{17}
\]
这只是形式恒等式，不需要断言某个共同复或 $p$ 进收敛圆盘。
它准确描述公共参考和全部 carry 在真实中央生成函数上
留下的非齐次项。

## 4. 对完整中心导数保留完全相同的精度

取完整惰性测试的权
\[
m_n=(p+1)p^n,\qquad
S_{p,n}=p^{p^n}C_{m_n}\in\mathbb Z_p,\qquad n\ge0.
\tag{18}
\]
[完整 GM 证书](2026-11-12-iterated-gm-frobenius-and-complete-inert-jets.md)
已经证明
\[
J'_p(0)\ne0
\quad\Longleftrightarrow\quad
\exists n\ge0:\ S_{p,n}\not\equiv0\pmod{p^{4n+4}}.
\tag{19}
\]
对 (6) 的实际源定义
\[
T_{p,n}=
p^{p^n-2}\kappa_{m_n}
 [z^{m_n}w^{m_n+1}]\mathcal N_p.
\tag{20}
\]
$n=0$ 时其中有一个 $p^{-1}$；其整性须由下面的准确等式证明，
不能从逐项 (6) 声称。
(15) 直接给
\[
\boxed{\quad
T_{p,n}=-(1+p^{2m_n-1})S_{p,n}.
\quad}
\tag{21}
\]
所以 $T_{p,n}$ 整，且
\[
v_p(T_{p,n})=v_p(S_{p,n}),\qquad
T_{p,n}\not\equiv0\pmod{p^{4n+4}}
\ \Longleftrightarrow\
S_{p,n}\not\equiv0\pmod{p^{4n+4}}.
\tag{22}
\]
全部深度都保留，未退回 $m=p+1$ 的首层单位测试。

结论是精确的：若只把 R92/R95 的非齐次项原样投影到
R94 指定中央留数线，这个源的完整非零问题就是原完整中心问题，
相差一个已核定单位。对该源使用“已知整数修正”“某个 norm”
或“低阶 remainder”的名称不会自动提供新的非零输入。

## 5. 与底参数平方 Frobenius 的尚待比较之处

R94 的真正底参数 Frobenius 使用 $t\mapsto t^q$ 及秩二
Gauss–Manin 晶体。其固定留数基满足
\[
\Phi^2(\mathfrak c_0)=-p^3\mathfrak c_0.
\tag{23}
\]
这与 (8) 的 $a^{2m+1}$ 来自不同拉回：
(8) 在固定椭圆纤维的两个加法变量上作用；
(23) 同时拉回底参数的微分和纤维晶体。

[准确 GM 主部差](2026-11-12-gm-frobenius-principal-part-and-central-defect.md)
另行在 cochain 层计算
$f_{mq}\omega\,dt-\Phi^2(f_m\omega\,dt)$。
其留数为 $(C_{mq}+p^3C_m)\mathfrak c_0$。
要把它与 (6) 识别，必须证明真实 theta 的 heat/相对 Frobenius
比较如何运输公共参考、全部混合 jet 和主部截断。
不能仅因两边在原点使用同一 $[-p]$ 纤维端同源，
就令 (6) 消失或把 (23) 当成 $C_{mq}=-p^3C_m$。

本篇没有排除以后建立更强的相对比较。
它已经确定了现有真实 theta 方程的完整中央源、准确尺度、
非 exact 实例和全部导数深度；任何新的有限维闭合关系须
处理这些具体项。

## 来源与验证范围

本篇不使用新增的外部定理。全部原 theta、除法函数和参考规范
来自上述 R92/R95 完整证明；Borel 尺度来自
[全权一规范](2026-11-12-full-weight-one-gm-critical-rows.md)，
固定留数及格来自 R94，完整深度来自 (19) 所链原证明。
新增恒等式均由 (3)、有限 binomial 展开、真实标签置换和逐项
系数提取直接证明。没有用一次数值样例替代全权公式。
