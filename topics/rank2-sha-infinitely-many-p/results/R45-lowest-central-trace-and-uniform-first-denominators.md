# R45. 最低中央迹的全局准确值及统一首层分母

日期：2026-11-12。**状态：已证明；不宣称主问题完成。**

固定
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
f=34(1+i),\quad P_f=\Omega_E/f,\quad F=K(E[\mathfrak f]).
$$
沿用固定 Kronecker 对角 $d_m$ 及有理系数
$e_m=d_m/f^{2m+1}$。$\Omega_E>0$ 是 $dx/(2y)$ 的最小正实周期。

## 1. 定理

有准确等式
$$
\boxed{
d_1=64(-1+i),\qquad N_{K/\mathbb Q}(d_1)=2^{13},
\qquad e_1=\frac4{17^3}.
}
\tag{1}
$$
特别地，$d_1$ 在每个奇素位均为单位。
范数及单位性不需要旧 CLS 特值输入；该输入仅用于最后选定四种
CM 单位方向中的一个。

对每个好普通素数 $p\ge7,\ p\ne17$，以及每个
$m\ge1,\ m\equiv1\pmod{p-1}$，有
$$
\boxed{v_p(e_m)=-2v_p(m!).}
\tag{2}
$$
因此 $v_p(e_p)=-2$，整个中央对角级数的 $p$ 进收敛半径和
形式图像的 size 都准确为 $p^{-2/(p-1)}$。

对每个惰性素数 $p\ge7$，有
$$
\boxed{
p^2e_{p+2}\equiv
\frac{\kappa_p^2}{(Nf)^2}\frac4{17^3}\pmod p,
\qquad v_p(e_{p+2})=-2,
}
\tag{3}
$$
其中
$$
\kappa_p=-\frac{(-1)^{(p+1)/4}}2
\binom{(p+1)/2}{(p+1)/4}17^{(p+1)/4}
\in\mathbb F_p^\times.
$$
所以 R44 中两条分母列可以统一取固定最低指标 $m_0=1$，
不再需要排除一个未显式确定的有限素数集合。

这些是非中心 tame 分支的严格结论；它们没有证明
$d_{p-1}\notin p^4$ 的无穷性。

## 2. 全局分母界

由 $C_2=U^2-X$ 及 $DU=-X,DX=2Y$，
$$
d_1(S)=-\operatorname{Tr}_{F/K}(U_Sx(S)+y(S))
\tag{4}
$$
对任意 primitive $\mathfrak f$ 轨道成立。
若 $n\equiv1\pmod{68}$，sigma 除法公式给
$$
U_S=-\frac{D\log\Psi_n(S)}{n(n-1)}.
\tag{5}
$$
在一个整的好模型上，若 $n$ 为剩余特征单位且
$[n]\bar S=\bar S\ne O$，则 $\Psi_n(S)$ 是单位：
它的约化零点是非零 $n$-torsion，而该点不属于此集合。
其整系数及 $O$ 处单位首项排除了竖直因子。

若变量变换为
$$
x=u^2X+r,\qquad y=u^3Y+s u^2X+t,
$$
则 $D_{\rm orig}=uD_{\rm good}$，两 division functions 只差常数。
故
$$
v(U_S)\ge v(u)-v(n(n-1)).
\tag{6}
$$

在剩余特征不为 $2,17$ 的地方，原模型好，
prime-to-$p$ torsion $S$ 约化非零。
对 $p\notin\{3,23\}$ 取 $n=69$；对 $p=3,23$ 取 $n=137$。
所用的 $n(n-1)$ 都是单位，故 $U_S,x(S),y(S)$ 整。

在 $17$ 处，取 $a^4=17$，用
$x=a^2X,y=a^3Y$ 变到 $Y^2=X^3-X$。
$[17]S$ 的非零 $\lambda^3$ 分量保证 $S$ 的约化非 $O$。
取 $n=69$，(6) 给
$$
v_{17}(U_S)\ge-3/4,\quad
v_{17}(x(S))\ge1/2,\quad v_{17}(y(S))\ge3/4.
$$
迹在 $K$ 中且每个 $17$ 素位的赋值为整数，
所以 $d_1(S)$ 在 $17$ 处整。

在 $2$ 处，取非零 $3$-torsion 点 $(r,t)$，并令
$$
3r^4-102r^2-289=0,\quad
s=\frac{3r^2-17}{2t},\quad u^3=2t.
$$
由 $(r^2-17)^2=1156/3$ 和 $s^2=3r$，
$$
v_2(r)=v_2(s)=0,\qquad v_2(t)=v_2(u)=1/2.
$$
上面的变量变换准确给
$$
Y^2+\frac{2s}{u}XY+Y=X^3.
$$
其判别式 $(2s/u)^3-27$ 是单位，故为好模型。
$[4]S$ 的非零 $17$-torsion 分量保证 $S$ 约化非 $O$。
取 $n=69$，得到
$$
v_2(U_S)\ge-3/2,\quad v_2(x(S))\ge0,\quad
v_2(y(S))\ge1/2.
$$
于是对四个 primitive 轨道均有
$$
\boxed{4d_1(S)\in\mathbb Z[i].}
\tag{7}
$$
这里只使用好模型上约化非零，没有错误地假定其约化阶仍为 $68$。

## 3. 严格复界与单个局部同余

对格 $\mathbb Z[i]$，选 torsion 代表 $w$ 使
$|\Re w|,|\Im w|\le1/2$。
因为 $w\in f^{-1}\mathbb Z[i]\setminus\mathbb Z[i]$，
$$
|w|<1,\qquad |w-\gamma|>1/49
\quad(\gamma\in\mathbb Z[i]).
$$
格上按 $\max(|\Re\gamma|,|\Im\gamma|)=n$ 分层给
$\sum_{\gamma\ne0}|\gamma|^{-3}<16$。
将 $|\gamma|<2$ 的八个非零格点单列，
对其余点用 $|w-\gamma|\ge|\gamma|/2$，
从 Weierstrass 的绝对收敛格点展开逐项得到
$$
|\wp_0(w)|<21777,\qquad
|\wp_0'(w)/2|<1058969,\qquad
|\zeta_0(w)-\pi\bar w|<493.
\tag{8}
$$
每个常数的逐项计算见
[完整全局迹证明](../notes/2026-11-12-central-theta-d1-exact-global-trace.md)
第2节；所用格点展开为 NIST DLMF 23.2.4–23.2.5。

又
$$
\Omega_E=17^{-1/4}\int_1^\infty\frac{dx}{\sqrt{x^3-x}}>2/3.
$$
对全部 $256$ 个共轭求和，(8) 因而给
$$
|d_1(S)|<
256\frac{27}{8}(493\cdot21777+1058969)
=B:=10190905920.
\tag{9}
$$

在精确无分歧环 $(\mathbb Z/3^{24})[A]/(g_3)$ 中，
固定 primitive 轨道及 $U=-r_{34}/34$ 的加法链给
$$
d_1^{\rm raw}\equiv64+64i\pmod{3^{24}},
\qquad 3^{24}=282429536481.
\tag{10}
$$
多项式 $g_3$、torsion Hensel 提升、256点轨道、
所有单位逆元及两生成元循环均在
[精确有限环脚本](../scripts/check-central-theta-inert.py) 中逐项核验。
这里只评价整数多项式 $-UX-Y$，没有丢失精度。

由 (7)，$Z=4d_1^{\rm raw}-256(1+i)\in\mathbb Z[i]$。
若它非零，(10) 迫使 $|Z|\ge3^{24}$；但
$$
|Z|<4B+512=40763624192<3^{24}.
$$
因此
$$
d_1^{\rm raw}=64(1+i)
$$
是全局等式。四个 primitive 轨道只差 $\mu_4$，
所以规范的 $d_1$ 必是其四个单位倍数，范数已无条件确定为 $2^{13}$。

固定周期方向沿用已审阅的 $p=13$ 轨道校准。
同一模 $13^5$ 计算给
$$
d_1^{\rm raw}\equiv243720,\qquad
d_1(P_f)\equiv127445=64(-1+i),
\quad i\equiv228249.
$$
校准点旋转 $\epsilon=-i$；权三的迹必须乘
$\epsilon^{-3}=-i$，不能沿用权13、25的乘子 $i$。
四个候选模13已互不相同，故选出 (1)。
最后 $f^3=78608(-1+i)$，得到 $e_1=4/17^3$。

全局证书
[check-central-theta-d1.py](../scripts/check-central-theta-d1.py)
已由独立根端重新执行，准确同余、单位方向和整数不等式全部通过。
旧 CLS 数据仅在这最后的方向校准中作为明确来源输入。

## 4. 推出全部好素数的固定首层分母

普通处完整 theta 矩为
$$
M_m=\Omega_p^{2m}(m!)^2d_m\in\mathcal O,\qquad
M_{m+p-1}\equiv M_m\pmod p\quad(m\ge1).
$$
由 (1)，$M_1$ 是单位。
所以每个 $m\equiv1\pmod{p-1}$ 的 $M_m$ 都是单位。
$f,\Omega_p$ 均为单位，立即得到 (2)。

全体矩的整性给 $v_p(e_m)\ge-2v_p(m!)$；
沿上述无穷指标，Legendre 公式达到半径
$p^{-2/(p-1)}$。
图像 size 的相同等式由
[普通 size 证明](../notes/2026-11-12-central-diagonal-ordinary-size-budget.md)
中整线性变换消去 $e_1Z$ 后的准确公式得到：
$v_p(m!)/(m-1)\le1/(p-1)$，并在该列趋近等号。

惰性处已独立证明
$$
p^2e_{p+1+s}\equiv
\kappa_p^2(Nf)^{-2}e_s\pmod p,\qquad0\le s\le p-3.
$$
取 $s=1$，由 (1) 与 $\kappa_p\ne0$ 得 (3)。
其递推证明见
[惰性中央平移](../notes/2026-11-12-central-diagonal-inert-shift.md)，
与本文的有限环认证相互独立。

## 5. 主问题仍缺什么

R40 的准确有限性条件仍是实际中央分支的二次系数非零，
或某个 $n\ge0$ 满足
$$
v_p(d_{(p-1)p^n})+2(p^n-1)<4(n+1).
$$
本文控制的 ordinary 列属于 $m\equiv1$，不是这个中心 tame 类。
由固定首层单位性推出目标中心非零需要新的关系；
本结果没有省略这一缺口。

### 来源

- NIST, *Digital Library of Mathematical Functions*，2010年至今，
  [23.2.4–23.2.5](https://dlmf.nist.gov/23.2)，用于 (8) 的定义展开。
- 本课题固定 theta 对角、实际扭点轨道、普通完整矩、惰性平移及
  $p=13$ 证书，均已在上面给出对应链接与明确使用位置。
- 完整全局迹笔记与两份可重复精确脚本给出本文所有新计算；
  没有使用浮点数识别、额外 Sha 假设或未经证明的高度上界。
