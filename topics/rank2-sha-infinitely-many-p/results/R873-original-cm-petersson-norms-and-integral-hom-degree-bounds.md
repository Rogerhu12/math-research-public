# R873 — 原三份 CM 范数、全坏位 AFE 与整 Hom 度数下界

日期：2026-11-16。

**状态：下面的角色、根号、Euler 因子、面积与度数公式由完整符号推导证明。附带 producer 已在公开 Actions 严格完成；第10节记录实际区间和全单位低权排除。不把准同态度数取整，也不声称已得到原坐标或非零 shadow。** R866 附录 A 已证明任何实际整数清分母必须含17，本篇把该条件与同一原 Hom 的解析范数准确联立。

固定 R862、R864、R866 的原来源及其复嵌入。所有下式都使用
$C=X_0(2601)$、原 $\infty$、同一 $\Xi_0$、
原 $q_0/q_2$ 和全部 Artin 系数。三阶商仅用于 R870 的函数表示，
本篇积分的源指数始终为3672。

## 1. 原角色的平方与唯一需要的三个 L 值

沿 R862 的标签，置
$$
(F_0,F_1,F_2)=(g_{10},g_{16},g_4),\qquad
F_j=\theta(\beta_j),\qquad
\mathfrak f_{\beta_j}=(17\delta),
$$
其中 $\delta=1+2\omega$、$\omega^2+\omega+1=0$。
原固定参数为
$$
\alpha=-1+2\omega,\qquad b^3=c=-1-19\omega
=\alpha^3\omega^2,\qquad b_j=\omega^j b.
\tag{1}
$$

记 $\zeta=b/\alpha$，于是 $\zeta^3=\omega^2$；
$\alpha\bmod17$ 生成 $\mathbf F_{289}^\times$。
对素于 $17\delta$ 的 $u=A+B\omega$，原完整主理想公式是
$$
\beta_j((u))=\epsilon_\delta(u)\,u\,
       (\zeta\omega^j)^{r(u)},\qquad
r(u)=\log_\alpha(u\bmod17)\bmod9,
\tag{2}
$$
$\epsilon_\delta(u)$ 是 $A+B\bmod3$ 的 $\pm1$ 提升。
特别地，原二处项为 $\beta_j((2))=-2$。

定义
$$
B_j=\beta_j^2.
$$
平方恰消去 $\epsilon_\delta$，因而(2)唯一延为全部素于17的理想函数：
$$
\boxed{
B_j((u))=u^2(\zeta\omega^j)^{2r(u)},\qquad
\mathfrak f_{B_j}=(17),\qquad\operatorname{type}B_j=(2,0).
}
\tag{3}
$$
乘 $u$ 以 $\mu_6$ 单位时右侧不变，所以确为理想函数。
17处有限角色的阶为9，故该导子准确，不能把17删去。
原3处导子则已经消去，但必须补回其不分歧 Euler 项：
$$
B_j((\delta))=-3.
\tag{4}
$$
这是因为 $\delta\bmod17$ 在 $r$ 的核中，$\delta^2=-3$。
(4)不是原 $F_j$ 的 $a_3$；原 $F_j$ 的确有 $a_3=0$。

令
$$
A_j(m)=
\sum_{\substack{N\mathfrak a=m\\(\mathfrak a,17)=1}}B_j(\mathfrak a),
\qquad
L_j(s)=\sum_{m\ge1}A_j(m)m^{-s}.
\tag{5}
$$
$L_j$ 是 weight3、level867、nebentypus $\chi_{-3}$ 的 CM 新形式
$\theta(B_j)$ 的标准 $L$ 函数。这里
$$
867=|D_K|N\mathfrak f_{B_j}=3\cdot17^2.
$$
$A_j(m)$ 是平方角色的理想和，**不是** $[q^m]F_j$ 的平方。
特别有
$$
A_j(1)=1,\quad A_j(3)=-3,\quad A_j(4)=4,\quad
A_j(3m)=-3A_j(m).
\tag{6}
$$

复共轭交换 $\mathfrak a$ 与 $\overline{\mathfrak a}$，故
$A_j(m)$ 为实数。每个求和项的绝对值为 $m$；
二次域中范数 $m$ 的理想数不超过 $d(m)$，所以
$$
|A_j(m)|\le m\,d(m)\le m^2.
\tag{7}
$$

## 2. 全局根号为正：包括3处不同理想和17处有限和

用 $\mu_j=B_j/N$ 的单位化角色及标准全局加性角色
$\psi_{\mathbf Q}\circ\operatorname{Tr}_{K/\mathbf Q}$。
Tate 局部函数方程给下表：

| 位置 | 原实际输入 | 单位根号 |
|---|---|---:|
| $\infty$ | 复角权2 | $-1$ |
| $\delta\mid3$ | $\mu_j$ 不分歧，$\mu_j(\delta)=-1$；加性角色含不同理想 $\delta$ | $-1$ |
| $17$ | 阶9的剩余角色，平凡于 $\mathbf F_{17}^\times$，均匀化元值1 | $+1$ |
| 其余有限位 | 乘法及加性角色均不分歧 | $+1$ |

17行可直接核出绝对符号。记剩余角色或其逆为 $\chi$，均满足
$\chi(\delta)=1$。非零 trace-zero 元正是
$\delta\mathbf F_{17}^\times$，其 $\chi$ 和为16。
若 trace-one 纤维的 $\chi$ 和为 $T$，因 $\chi$ 在
$\mathbf F_{17}^\times$ 上平凡，每个非零 trace 纤维都有同一和。
全乘法群上的和为0，所以 $16+16T=0$，即 $T=-1$。
故标准有限 Gauss 和准确为
$$
\sum_{x\in\mathbf F_{289}^\times}
 \chi(x)e^{2\pi i\operatorname{Tr}(x)/17}
=16-\sum_{t\in\mathbf F_{17}^\times}e^{2\pi it/17}
=17.
\tag{8}
$$
除以 $\sqrt{289}=17$ 后是 $+1$。
3行虽乘法角色不分歧，却不能忘掉加性不同理想；
它的贡献恰为 $\mu_j(\delta)=-1$。因此
$$
\boxed{W(B_j)=+1\quad(j=0,1,2).}
\tag{9}
$$

置
$$
\mathcal Q=\frac{\sqrt{867}}{2\pi},\qquad
\Lambda_j(s)=\mathcal Q^s\Gamma(s)L_j(s).
$$
同一完整函数方程为
$$
\boxed{\Lambda_j(s)=\Lambda_j(3-s).}
\tag{10}
$$
(9)是三个原平方角色的根号，不是原 weight4 $\lambda_j$ 的根号，
也不对那些原 canonical 类作新的非零断言。

## 3. 精确 AFE 与统一严格尾界

用(10)把 Mellin 积分在1处分开。对
$\vartheta_j(t)=\sum_mA_j(m)e^{-mt/\mathcal Q}$，
反演把区间 $(0,1)$ 的积分变为 $(1,\infty)$ 上的反射项。
在 $s=2$，两个幂正好是 $t$ 和1，故
$$
\begin{aligned}
\mathcal Q^2L_j(2)
&=\int_1^\infty(t+1)\vartheta_j(t)\,dt\\
&=\sum_{m\ge1}A_j(m)e^{-m/\mathcal Q}
  \left(\frac{\mathcal Q^2}{m^2}+\frac{2\mathcal Q}{m}\right).
\end{aligned}
$$
因此
$$
\boxed{
L_j(2)=\sum_{m\ge1}\frac{A_j(m)}{m^2}
 \left(1+\frac{2m}{\mathcal Q}\right)e^{-m/\mathcal Q}.
}
\tag{11}
$$
第二项的系数是2；它包含 $\Gamma(2,x)$ 的一次项和反射
$\Gamma(1,x)$，不可只保其中之一。

设 $r=e^{-1/\mathcal Q}$，截断到 $M$。由(7)和几何级数求导，
所有三个嵌入共用严格上界
$$
\boxed{
\left|L_j(2)-\sum_{m=1}^M
 \frac{A_j(m)}{m^2}\left(1+\frac{2m}{\mathcal Q}\right)r^m
\right|
\le
r^{M+1}\left\{
 \frac1{1-r}
 +\frac2{\mathcal Q}
 \left(\frac{M+1}{1-r}+\frac r{(1-r)^2}\right)
\right\}=:T_M .
}
\tag{12}
$$
这是由原系数绝对界得到的全尾，而不是依据数值稳定性估计误差。
producer 使用 $M=1024$，所有 Gamma、指数及代数嵌入均以
Arb 球运算包围，再将(12)的整个上界加到半径中。

## 4. Rankin–Selberg 归一及3、17的精确抵消

记 $a_j(m)=[q^m]F_j$，并置
$$
D_j(s)=\sum_{m\ge1}|a_j(m)|^2m^{-s}.
$$
在所有好素数上，逐个 Satake 参数求和给
$$
\boxed{
D_j(s)=
\frac{\zeta(s-1)L(\chi_{-3},s-1)L_j(s)}
     {\zeta(2s-2)}.
}
\tag{13}
$$
本题的坏位不添任何未记录常数，证明如下。

在3处，原 $a_j(3^r)=0$ 对 $r\ge1$，所以左侧因子为1。
令 $x=3^{1-s}$。右侧四因子分别给
$$
(1-x)^{-1},\quad1,\quad(1+x)^{-1},\quad1-x^2,
$$
乘积恰为1。(4)在这里不可省去。

在17处，原左侧亦为1；$B_j$ 仍 ramified，所以 $L_{j,17}=1$。
因 $\chi_{-3}(17)=-1$，其余三因子为
$$
(1-x)^{-1}(1+x)^{-1}(1-x^2)=1,
\qquad x=17^{1-s}.
$$
2是好惰性素数，原 $a_j(4)=-2$ 在(13)中照常保留。
所以(13)是完整 primitive 恒等式，而非删坏位后的近似。

源曲线的真实指数是
$$
\mu_C=[\mathrm{SL}_2(\mathbf Z):\Gamma_0(2601)]=3672.
$$
定义与 PARI 官方规范一致的 Petersson 范数
$$
N_j=\frac1{\mu_C}
\int_{\Gamma_0(2601)\backslash\mathfrak H}|F_j(z)|^2\,dx\,dy.
\tag{14}
$$
宽度1的 $\infty$ Eisenstein series 在 $s=1$ 的留数为
$3/(\pi\mu_C)$。完整展开给
$$
\int |F_j(z)|^2y^2E_\infty(z,s)\frac{dx\,dy}{y^2}
=\frac{\Gamma(s+1)}{(4\pi)^{s+1}}D_j(s+1).
$$
比较 $s=1$ 留数，得到
$$
\operatorname{Res}_{s=2}D_j(s)=48\pi N_j.
\tag{15}
$$
再用
$L(\chi_{-3},1)=\pi/(3\sqrt3)$ 和 $\zeta(2)=\pi^2/6$，
由(13)严格得到
$$
\boxed{N_j=\frac{L_j(2)}{24\sqrt3\pi^2}.}
\tag{16}
$$
三条 $F_j$ 有不同的实 Hecke 本征值，Hecke 算子对(14)自伴，
故它们彼此正交。这里没有用三阶商 $X_0(867)$ 的指数1224替代3672。

## 5. 原目标的复面积

固定
$$
E_0:y^2=x^3+1,\qquad\omega_0=\frac{dx}{2y},\qquad
\mathcal A_0=\int_{E_0(\mathbf C)}
 i\omega_0\wedge\overline{\omega_0}.
$$
投到 $x$ 平面有两层，故
$$
\mathcal A_0
=\int_{\mathbf C}\frac{d^2x}{|x^3+1|}
=\frac13\int_{\mathbf C}|u|^{-4/3}|1-u|^{-1}\,d^2u,
\qquad u=-x^3.
\tag{17}
$$
所用复 beta 积分在 $a,b>0,\ a+b<1$ 时为
$$
\int_{\mathbf C}|u|^{2a-2}|1-u|^{2b-2}\,d^2u
=\pi\frac{\Gamma(a)\Gamma(b)\Gamma(1-a-b)}
{\Gamma(1-a)\Gamma(1-b)\Gamma(a+b)}.
\tag{18}
$$
为固定常数，可把两负幂分别写成 Laplace 积分。
先做 $u$ 的平面 Gaussian 积分，结果是
$\pi(s+t)^{-1}\exp(-st/(s+t))$；再置
$s=rx,t=r(1-x)$，先积 $r$ 再积 $x$，
恰给右侧。因此(18)不依赖一个未定周期基或面积约定。

取 $a=1/3,b=1/2$，再用 Gamma 反射式，得到
$$
\boxed{\mathcal A_0=
\frac{\Gamma(1/3)^2\Gamma(1/6)^2}{4\pi\sqrt3}.}
\tag{19}
$$
特别要避免把实周期误当成原 Eisenstein 格的任意一条生成周期；
(17)直接消除了可能的指数3误差。

原目标与尺度是
$$
C_v:Y^2+vY=X^3,\qquad
v=-122465-47628a-\frac{314892}{17}a^2,\quad a^3=17,
$$
$$
d=\frac h{2^{11}},\qquad d^3=\frac v2,\qquad
\kappa(X,Y)=\left(X/d^2,\;2Y/v+1\right),\qquad
\kappa^*\omega_0=d\,\omega_v.
\tag{20}
$$
选原实嵌入时 $v<0$，所以
$$
\boxed{
\mathcal A_v=\frac{\mathcal A_0}{|d|^2}
=\frac{\mathcal A_0}{(-v/2)^{2/3}}.
}
\tag{21}
$$
(20)包含原 $2^{11}$，不把 $C_v$ 当作未缩放的 $E_0$。

还可取整数单位
$$
e=18-7a,\qquad e^{-1}=324+126a+49a^2,\qquad
-av=(e^{-1})^2.
$$
同步同构 $(X,Y)\mapsto(e^2X,e^3Y)$ 给
$$
v_{\rm small}=e^3v=7-\frac{18}{17}a^2,\qquad
\omega_{\rm small}=e^{-1}\omega_v.
\tag{22}
$$
此时面积除以 $|e|^2$，原输入微分也必须变成 $e^{-1}H_0$。
两者在映射度数中完全抵消；较小模型本身不会使原 Hom 度数下降。
$e$ 在17处是单位，亦不能消掉 R866 附录 A 的必要因子17。

## 6. 完整 Gauss 系数与原准同态度数

保持 R864 的实际多项式
$$
\ell(v)=
\frac{21905009-23122022\omega+
(112353990182+54575060764\omega)v+
(305813+148546\omega)v^2}{25505280},
$$
$$
\tau(v)=\alpha^3v/\ell(v)^3,\qquad
u_1=\tau^2\ell,\quad u_2=c/\ell.
\tag{23}
$$
不另选范数解。原 Gauss 系数和完整输入为
$$
G_j=1+\frac{u_1}{b_j}+\frac{u_2}{b_j^2},\qquad
H_0=\frac13\sum_{j=0}^2G_jF_j,\qquad
\Xi_0^*\omega_v=H_0(q)\frac{dq}{q}.
\tag{24}
$$
这些 $G_j$ 均非零，沿 R862 的真实 Hom 定理和首系数识别；
producer 也将逐个用严格球排除0。

对真实映射 $n\Xi_0$，因 $dq/q=2\pi i\,dz$，积分正交分解给
$$
\deg(n\Xi_0)
=n^2\frac{8\pi^2\mu_C}{\mathcal A_v}
   \sum_{j=0}^2\left|\frac{G_j}{3}\right|^2N_j.
$$
结合(16)，设
$$
\boxed{
a_j=\frac{136}{\sqrt3\mathcal A_v}|G_j|^2L_j(2)>0,\qquad
d_0=a_0+a_1+a_2 .
}
\tag{25}
$$
常数136准确等于 $3672/27$。于是
$$
\boxed{\deg(n\Xi_0)=n^2d_0.}
\tag{26}
$$
$d_0$ 是规范准同态的有理正“度数”：任选一个真实清分母 $n$，
以 $\deg(n\Xi_0)/n^2$ 定义，独立于该选择。
**它本身不必是整数。** producer 不通过四舍五入来认证 $n$ 或原 Hom。

## 7. 全部整单位方向的统一下界

R867 的两枚真实整 Hecke 单位记为
$$
U_1=\mathscr R,\qquad U_2=\mathscr R^2-2.
$$
在三条原线上的值分别是
$$
\varepsilon_{1,j}=\zeta\omega^j+(\zeta\omega^j)^{-1},
\qquad
\varepsilon_{2,j}=\varepsilon_{1,j}^2-2.
\tag{27}
$$
两者的范数均为 $-1$，其已显示的整逆作用于同一原 packet。
因此整数 $u,w$ 给
$$
d_{u,w}=\sum_{j=0}^2
 a_j|\varepsilon_{1,j}|^{2u}|\varepsilon_{2,j}|^{2w},
\qquad
\deg(n\Xi_0U_1^uU_2^w)=n^2d_{u,w}
\tag{28}
$$
（后式只在实际整时称映射度数）。

置
$$
g=(a_0a_1a_2)^{1/3}.
$$
因两个单位的三嵌入绝对范数都是1，三个(28)加项的乘积恒为
$a_0a_1a_2$。AM–GM 直接证明
$$
\boxed{d_{u,w}\ge3g\qquad\text{对全部 }(u,w)\in\mathbf Z^2.}
\tag{29}
$$
这里是整个单位格的下界，不是有限窗口的最小值。
R866 附录 A 又给任何真实整数候选的 $17\mid n$，所以
$$
\boxed{
\deg(n\Xi_0U_1^uU_2^w)\ge17^2\cdot3g.
}
\tag{30}
$$
不需要分别判断各单位变形后的首系数，因为整单位逆将其整性
准确返回 $\Xi_0$。

R867 附录 C 的三同源备选 $\Psi=\varphi\Xi_0/3$ 的准度数是
$d_0/3$；且 $\widehat\varphi\Psi=\Xi_0$，故实际整数
$n\Psi U_1^uU_2^w$ 仍要求 $17\mid n$。于是
$$
\boxed{\deg(n\Psi U_1^uU_2^w)\ge17^2g.}
\tag{31}
$$
R870 的权 $k$ 证书给真实度数上界 $102k$。
因此只要严格球区间证明(30)或(31)的右边大于 $102k$，
就排除了该权下所有整数清分母和全部上述整单位方向。
不需逐个加大单位窗口，也不需把未知 $n$ 预置为17。

这个排除仅针对所显示的原 Hom 整单位轨道及三同源备选。
它不排其它非单位 Hecke 组合、其它整 Hom 或任意坐标算法；
也不证明原 shadow 为零或非零。

## 8. 可公开执行的 producer 与准确输出

脚本路径建议为
`scripts/check-r873-original-cm-petersson-degree.py`，
固定 Sage 镜像中运行：
```
sage -python scripts/check-r873-original-cm-petersson-degree.py --M 1024 --bits 384 --unit-window 6 --top 6
```

producer 不读取旧数据表，具体执行：

1. 在精确 $\mathbf Q(\zeta_9)$ 中枚举
   $A^2-AB+B^2\le1024$ 的每个 $\mu_6$ 轨道一次。
   原 $F_j$ 删且仅删 $17\delta$ 倍数；平方角色只删17倍数。
   逐轨道核主理想公式的单位不变性。
2. 采用 $\omega=\zeta_9^3,\ \zeta=\zeta_9^2$；
   三嵌入指数 $(1,7,4)$ 固定 $\omega$，
   对应原 $b,\omega b,\omega^2b$。
   原 $a_4=-2$、平方角色 $A_3=-3,A_4=4$、全部
   $A_{3m}=-3A_m$ 和共轭实性均精确检查。
3. 由(23)恢复原 $\tau$ 和全部 $G_j$，
   核 $\tau^3v=v$、$N\ell=c$、$\sum G_j=3$，
   并对照实际
   $$
   [q^7]H_0=
   \frac{1378521263+57978976034v+157811v^2}{531360}.
   $$
4. 用(11)、(12)和 Sage 的 RealBallField/ComplexBallField
   得三个完整 $L_j(2)$、$N_j$、(19)–(21)面积和(25)正权。
   全部严格比较使用球区间的端点含义，不用浮点显示值决定结论。
5. 输出 $d_0,g,3g,17^2g,17^2\cdot3g$，以及对
   $k=2,4,6,8$ 的真实度数帽的严格比较。
   有限单位窗只列后续候选及其完整未归一首项，不认证全局最小值。

精确系数全表只在运行内存中生成，输出其 SHA256。
仓库只保脚本、参数、公开 run 与输出哈希；不提交可重算数据表。
实际执行与严格数学结论见第10节；完整可重算输出不入库。

## 9. 来源与核验边界

- [R862](R862-original-seventeen-torsion-product-and-complete-cubic-hom-matrix.md)：
  原 $\beta_j$、全部 Gauss 系数、Hom 与其固定微分。
- [R864](R864-original-seventeen-torsion-exact-field-and-cocycle.md)：
  原17挠点乘积及 $\ell,\tau,v$ 的公开精确证书。
- [R866](R866-original-modular-function-certificate-and-level-nine-model.md)
  附录 A：原 smooth 整 $q$ 盘及真实 $17\mid n$。
- [R867](R867-original-single-hom-and-integral-hecke-three-basis.md)
  附录 A–C：实际整单位、三同源和全部源尺度。
- [R870](R870-original-low-weight-quotient-and-exact-elliptic-coordinate-certificate.md)：
  权 $k$ 的严格椭圆恒等式与 degree 帽 $102k$。
- J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-functions*，
  1950，§§2.4–2.5 的局部因子与 §§4.4–4.5 的完整函数方程：
  <https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf>。
  本题所需根号的每个非平凡因子已在第2节明确算出。
- PARI 官方 `mfpetersson` 规范：
  <https://pari.math.u-bordeaux.fr/dochtml/html/Modular_forms.html#mfpetersson>。
  本文没有调用它来代替坏位核对；(13)–(16)自含固定全部常数。
- Sage 官方 Arb 球算术：
  <https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/real_arb.html>、
  <https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/complex_arb.html>。
  `add_error` 增加上界半径，严格正性及大小比较按包含区间的语义执行。

主目标及原端点 shadow 的实际非零仍开放。
本篇提供的是同原 Hom 的完整、可严格执行的度数计算与全单位下界，
不用新的辅助角色取代原来源。


## 10. 已执行的严格区间与全单位低权排除

**已证明（上述解析推导加公开 Arb 区间证书）。** 源提交
`39cc6b4ebb82938774b21d2c3546d174a822514d`，
[run43832670630](https://github.com/Rogerhu12/math-research-public/actions/runs/43832670630)、
job133181502585，于2026-11-16 08:38:07 UTC输出PASS；
Sage10.6，计算3.861710652秒。精确参数为
`--M 1024 --bits 384 --unit-window 6 --top 6`；
固定镜像及完整来源在脚本和
`ci/original-cm-norm-request.json` 中。

完整输出SHA256为
`39d8f442e20a9f94a610461fed63634338a88f8c6f8eff670675c15a441d82a4`；
脚本SHA256为
`b1cf0a9b1b8bc8ff5dd5f8b082c710749662d330af73cb981a8e9f9abb16c769`；
原精确系数流SHA256为
`3a7ee7dffe840a5c566dadca6d2c5f47a9d4e51889c136cfdbfac6ea1ad8bbb5`。
完整系数与球输出只在运行日志中，不作为数据文件保存。

从严格球外扩得到如下方便引用的有理开区间；顺序始终是
$(g_{10},g_{16},g_4)$：

| 量 | 第0份 | 第1份 | 第2份 |
|---|---|---|---|
| $L_j(2)$ | $(1.1211479,1.1211480)$ | $(1.3314537,1.3314538)$ | $(0.8372664,0.8372665)$ |
| $N_j$ | $(0.00273269,0.00273270)$ | $(0.00324529,0.00324530)$ | $(0.00204076,0.00204077)$ |
| $a_j$ | $(27757.6315,27757.6316)$ | $(33196.6080,33196.6081)$ | $(20779.8781,20779.8782)$ |

同一运行的完整尾界满足 $T_{1024}<2.344\cdot10^{-92}$；
所有显示球的误差已包括该完整尾，不从有限差值猜误差。
面积及度数给
$$
10.2162314<\mathcal A_0<10.2162315,\qquad
0.0031614663<\mathcal A_v<0.0031614664,
$$
$$
81734.1176<d_0<81734.1177,\qquad
26753.0337<g<26753.0338,
$$
以及严格较强的联合球比较
$$
80259<3g<80260,\qquad
23194880<17^2\,3g<23194881,\qquad
7731626<17^2g<7731627.
\tag{32}
$$

(32)结合(30)–(31)严格排除权 $k=2,4,6,8$
下**全部整数 $n$、全部 $(u,w)\in\mathbf Z^2$ 的原单位轨道和三同源备选**，
因为这些权的真实度数帽至多816。有限单位窗口的排序不参与此排除；
也没有把准度数的显示值识别为某个有理数或整数。

下一实际搜索因此转到一般有理 Hecke 组合的整微分必要格，
而非扩大此已排除轨道的低权矩阵。
这不是所有原 Hom 的度数排除；主目标、原坐标和原非零 shadow 仍开放。
