# R987 — 原十三处两个实际轨道与归一中央差的准确 3/4

日期：2026-11-26 UTC。**已证明：原 $E_{65^3}$ 来源在两个十三核上的四个六点平均，完整落在原来源与 $E_{125}$ 的两条真实 old 拉回所张成的三维空间；所有相位由原 good-13 trace 固定。两个指定平均各除以其实际非零质量后，其差准确为 $3/4$ 倍的原 old 差，再加一个显示的原算术来源倍数。** 因此，在原算术中央导数为零的坏素数假设下，这两个实际 translated 测试的归一导数差对每个目标普通或惰性素数均非零。这里的非零是固定的两个完整测试，不是从全部 Heisenberg 张成中任选一个未指定项。

本篇保持原单位切域及完整 mixed 对偶。它没有将这两个译像的中央导数赋零，也没有把它们当作新的 $\mathbf Q$ 曲线来源。末节说明当前可以接入 R968 的整个关系，以及尚须由原算术行支付的准确两个测试。

## 1. 三个原来源和全部归一

固定
$$
 K=\mathbf Q(\delta),\quad \delta^2=-3,\quad
 \omega=(-1+\delta)/2,\quad
 \pi=(7+\delta)/2,\quad \bar\pi=(7-\delta)/2,
 \qquad N\pi=13.
 \tag{1}
$$
本篇先在 $E_1:y^2=x^3+1$、$dz=dx/(2y)$ 上写整个来源。
沿 R972、R978 记
$$
 \Phi=\Phi_{*,1}=\sigma^{130}x^2P_\Phi(X),\quad X=x^3,
 \quad \deg P_\Phi=20,\quad [X^{20}]P_\Phi=1,
 \tag{2}
$$
$$
 \Psi=\Psi_{125}=\sigma^{10}x^2(X-8),\qquad
 x_\pi=D_\pi\Psi=\Psi(\pi z),\qquad
 x_{\bar\pi}=D_{\bar\pi}\Psi=\Psi(\bar\pi z).
 \tag{3}
$$
这里的 $x_\pi,x_{\bar\pi}$ 是来源名称，不是 Weierstrass 坐标。
三个完整来源都属于原
$$
 V_{130}=\sigma^{130}x^2K[X]_{\le21},
$$
并且
$$
 \Phi(0)=0,\quad [z^6]\Phi=1,\qquad
 x_\pi(0)=x_{\bar\pi}(0)=1.
 \tag{4}
$$
R978 的原 old 差是
$$
 \Delta_{125}=x_\pi-x_{\bar\pi},\qquad
 [z^6]\Delta_{125}=-21840\delta\ne0.
 \tag{5}
$$
不把 $D_\pi$ 另乘一个未记录的 Hecke 标量。

令 $\Lambda$ 为原 sigma 晶格，$\eta$ 为原准周期的反线性延拓。
所有平移使用 R985 的同一个绝对 lift
$$
 T_{130,u}f(z)=
 \exp[-130\eta(u)(z+u/2)]f(z+u),\qquad u\in E[130].
 \tag{6}
$$
下文 $T_u$ 总指 (6)。对 $u\in E[\pi]$，它还有不含未知 theta 常数的完整代数式
$$
 \boxed{
 T_uf(z)=\sigma(\pi z)^{10}
             \frac{f(z+u)}{\sigma(\pi(z+u))^{10}}.}
 \tag{7}
$$
因为 $\pi u\in\Lambda$，原 sigma 准周期给
$$
 \frac{\sigma(\pi(z+u))^{10}}{\sigma(\pi z)^{10}}
 =\exp[130\eta(u)(z+u/2)].
$$
半特征的十次方为一，且
$\eta(\pi u)\pi=13\eta(u)$；故 (7) 与 (6) 完全同相位。
对 $E[\bar\pi]$ 也成立。商在其 apparent 零点按整截面延拓，不删掉相应核点。

## 2. 原 good-13 trace 固定两个 old 基之间的相位

令
$$
 Q_\pi=\frac1{13}\sum_{u\in E[\pi]}T_u,\qquad
 Q_{\bar\pi}=\frac1{13}\sum_{u\in E[\bar\pi]}T_u.
 \tag{8}
$$
它们是两条原 degree10 退化像的完整投影。
对原 $E_{125}$ primitive 角色，十三是好位。
R973 的实际二、三、五单位角色在 $\pi$ 上分别为
$\omega,-1,-1$。这里保 R973 的 ideal character 约定：好位的
$\psi((\pi))/\pi$ 是所有坏单位值乘积的逆。因此
$$
 \lambda_{13}=\frac{\psi_{125}((\pi))}{\pi}
 =(\omega\cdot(-1)\cdot(-1))^{-1}=\omega^2,
 \qquad
 \theta:=\psi_{125}((\pi))=\omega^2\pi=-1-2\delta,
 \qquad
 t:=\bar\theta=\omega\bar\pi=-1+2\delta.
 \tag{9}
$$
该处无非平凡坏位 Gauss 因子可另改相位。
同一个规范的完整算子是
$$
 N_\pi=\pi^{-1}\operatorname{Tr}_{[\pi]}D_{\bar\pi},
 \qquad N_\pi\Psi=\omega^2\Psi.
 \tag{10}
$$
这也可以在完整 $\sigma^{10}x^2,\sigma^{10}x^5$ 两列上由原 division 函数计算；本篇独立消费者正是重建这整个两列算子及两个额外完整纤维，不只检查一个点的函数值。

原线丛 trace 与 (7) 的 deck average 给
$$
 Q_\pi=\frac1{13}D_\pi\operatorname{Tr}_{[\pi]}.
$$
于是有完整来源身份
$$
 \boxed{
 Q_\pi x_\pi=x_\pi,\qquad
 Q_\pi x_{\bar\pi}=\frac{\theta}{13}x_\pi,\qquad
 Q_{\bar\pi}x_{\bar\pi}=x_{\bar\pi},\qquad
 Q_{\bar\pi}x_\pi=\frac{t}{13}x_{\bar\pi}.}
 \tag{11}
$$
它们保留 $1/13$，也保留 $\theta,t$ 的非实相位。

## 3. 只有十三因子移动时的准确三维空间

R973 先由全部有限 Weil 角色指定 $\Phi$ 的标签为
$(\epsilon,a,b)=(0,0,0)$。固定二、五两个一维向量，只移动十三因子，得到原完整十三维空间
$$
 V_{\rm loc}=v_{2,0}\otimes f_{5,0}\otimes W_{13}
 \subset\mathcal S_{130}.
 \tag{12}
$$
同一 principal 条件允许的十三角色恰为 $b=0,6$。
$b=0$ 重数一，是 $K\Phi$；$b=6$ 重数二，是同一 $E_{125}$ 角色的两条 old 像。
所以
$$
 \boxed{V_{\rm loc}^{\mu_6}
 =K\Phi\oplus Kx_\pi\oplus Kx_{\bar\pi}.}
 \tag{13}
$$
这由全部原有限标签给出，不由三个 low jets 猜整个来源。
两个 old 向量确实独立：若它们相同，(11) 将强迫 $\theta=13$，与 $N\theta=13$ 矛盾。

取两个十三核的非零生成元 $u_\pi,u_{\bar\pi}$。
令 $\zeta$ 为它们在 degree130 Heisenberg 提升中的原始十三次中心根；它相对于通常 $e_{13}$ 保留幂次 $130/13=10$。
取与这两条实际提升相容的 Schrödinger 坐标 $v\in\mathbf F_{13}$，使
$$
 M_s=T_{s u_\pi},\qquad U_r=T_{r u_{\bar\pi}}
$$
分别为 modulation 和 translation。把 $\zeta$ 改成其逆不改变下面的 quadratic Gauss 和，因 $(-1/13)=1$。

写 $\varepsilon(v)=(v/13)$、$\varepsilon(0)=0$，以及
$$
 g=\sum_{v\in\mathbf F_{13}}\varepsilon(v)\zeta^v,
 \qquad g^2=13.
 \tag{14}
$$
不先将这个准确的 Gauss 根换成任意一个数值平方根。
在自然十三极化中，原 primitive 向量是 $\varepsilon$；两个 old 核不变向量是 $\delta_0$ 与 $\mathbf1$。
因此对某些非零常数 $a,c$，三个实际来源有坐标
$$
 \Phi=c\varepsilon,\qquad
 x_\pi=a\delta_0,\qquad
 x_{\bar\pi}=b\mathbf1.
$$
由 (11)，$Q_\pi x_{\bar\pi}=(b/a)x_\pi$，故绝对比例准确为
$$
 \boxed{a/b=t.}
 \tag{15}
$$
定义
$$
 h_{13}=c/a,\qquad k_{13}=h_{13}/6.
 \tag{16}
$$
$h_{13}$ 非零。它的代数性及可计算的准确规范将在第5节由原核质量给出。式 (16) 的六不能省略：$k_{13}$ 是下面两个六点平均之差的规范，$h_{13}$ 才是直接的 $c/a$。

## 4. 四个六点平均的完整恒等式

十三处的全局 $\mu_6$ 像恰为
$$
 H=(\mathbf F_{13}^{\times})^2=\{1,3,4,9,10,12\}.
$$
令 $s_+,r_+$ 为平方，$s_-,r_-$ 为非平方。定义实际 orbit averages
$$
 \mathcal M_\pm=\frac16\sum_{t_0\in H}T_{t_0s_\pm u_\pi}\Phi,
 \qquad
 \mathcal U_\pm=\frac16\sum_{t_0\in H}T_{t_0r_\pm u_{\bar\pi}}\Phi.
 \tag{17}
$$
它们也是 $\Pi_0T_{s_\pm u_\pi}\Phi$ 与 $\Pi_0T_{r_\pm u_{\bar\pi}}\Phi$，不在这一步删去 nonprincipal 部分之后再错误复合另一个局部平移。

以下两个有限计算支付全部坐标。若 $A$ 是对平方单位的平均，$s,r\ne0$，则
$$
 A M_s\varepsilon
 =-\frac{\varepsilon}{12}
    +\frac{\varepsilon(s)g}{12}\mathbf1_{\mathbf F_{13}^{\times}},
 \tag{18}
$$
$$
 A U_r\varepsilon
 =-\frac{\varepsilon}{12}
    +\frac{\varepsilon(r)}{12}(13\delta_0-\mathbf1).
 \tag{19}
$$
对 (18)，非零 $v$ 的平方轨道加性和为
$(-1+\varepsilon(sv)g)/2$，再除以六并乘 $\varepsilon(v)$；在 $v=0$ 两边均为零。
对 (19)，在 $v\ne0$ 使用
$$
 \sum_{t_0\ne0}\varepsilon(t_0v+r)=-\varepsilon(r),\qquad
 \sum_{t_0\ne0}\varepsilon(t_0)\varepsilon(t_0v+r)
 =-\varepsilon(v),
$$
第二式是非退化 quadratic 字符和。
在 $v=0$ 的值恰为 $\varepsilon(r)$，所以 (19) 的 $13\delta_0$ 也不可删除。

将 (15)–(16) 代回整个有限张量，得到完整 degree130 来源身份
$$
 \boxed{
 \mathcal M_\pm=-\frac{\Phi}{12}
       \pm\frac{g h_{13}}{12}
                (t x_{\bar\pi}-x_\pi),}
 \tag{20}
$$
$$
 \boxed{
 \mathcal U_\pm=-\frac{\Phi}{12}
       \pm\frac{h_{13}}{12}
                (13x_\pi-tx_{\bar\pi}).}
 \tag{21}
$$
特别
$$
 \mathcal M_++\mathcal M_-
 =\mathcal U_++\mathcal U_-=-\Phi/6.
 \tag{22}
$$
若以 $\mathcal M=\mathcal M_+-\mathcal M_-$、
$\mathcal U=\mathcal U_+-\mathcal U_-$ 记差，(20)–(21) 正是
$$
 \mathcal M=g k_{13}(t x_{\bar\pi}-x_\pi),\qquad
 \mathcal U=k_{13}(13x_\pi-tx_{\bar\pi}).
 \tag{23}
$$
这解释了第5节常数式中的十二与七十二的区别。

两个正 orbit 的准确质量是
$$
 m_M:=\mathcal M_+(0)=\frac{g h_{13}(t-1)}{12}
                   =\frac{g h_{13}\omega}{3},
$$
$$
 m_U:=\mathcal U_+(0)=\frac{h_{13}(13-t)}{12}
                   =\frac{h_{13}\bar\pi}{3}.
 \tag{24}
$$
它们均非零。原算术来源的质量零没有传到这些十三译像。

现在用
$$
 (13-t)(t-1)=16t
$$
消去两个 old 系数，得到本篇最短的完整来源关系
$$
 \boxed{
 \frac{\mathcal U_+}{m_U}-\frac{\mathcal M_+}{m_M}
 =\frac34\Delta_{125}
  +\frac1{12}\left(\frac1{m_M}-\frac1{m_U}\right)\Phi.}
 \tag{25}
$$
这条式子不含一个未指定的 proportionality 常数。
其中 $3/4$ 来自原 $\psi_{125}(\pi)+\overline{\psi_{125}(\pi)}=-2$ 与两个实际 raw pull 的同一质量一规范。

## 5. canonical 核质量给绝对代数常数

原 R978 的完整 division 函数是
$$
 \sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X),\qquad
 R_\pi(X)=X^2+(2+6\delta)X+(40+24\delta)/13.
 \tag{26}
$$
非零 $\pi$-kernel 的两个 $\mu_6$ 轨道对应 $R_\pi$ 的两个根。
其判别式及根准确为
$$
 \operatorname{disc}R_\pi=-432/\pi,
 \qquad
 t_\pm=-1-3\delta\pm6\delta/\sqrt\pi.
 \tag{27}
$$
对 $u\in E[\pi]\setminus\{0\}$、$X(u)=t_u$，把 (2)、(26) 代入 (7)，原点极限给
$$
 \boxed{
 (T_u\Phi)(0)=
 \frac{P_\Phi(t_u)}
      {6^{10}t_u^6(t_u+1)^5R_\pi'(t_u)^{10}}.}
 \tag{28}
$$
证明中分子 $x(u)^2$ 与
$X'(u)^{10}=(6x(u)^2y(u))^{10}$ 相除，正好留下
$t_u^{-6}(t_u+1)^{-5}$。前因子
$\sigma^{130}R_\pi(X)^{10}$ 的首项是 $z^{10}$，没有额外 $\pi^{10}$。
所以 (28) 是 canonical lift 的真实质量，不是另选 theta 常数。

在完整二次代数 $K[X]/R_\pi$ 中将右边化为
$$
 A_0+\beta_{13}X.
$$
原 primitive trace-zero 给
$$
 2A_0-(2+6\delta)\beta_{13}=0,
 \quad
 A_0+\beta_{13}t_\pm
   =\pm6\delta\beta_{13}/\sqrt\pi.
 \tag{29}
$$
(20)、(24) 已证明两质量非零，因此 $\beta_{13}\ne0$。
选 $t_+$ 对应 (17) 的正 $\pi$-orbit，令
$s=g/\sqrt\pi$，则 $s^2=\bar\pi$。
由 (24)、(29) 精确得到
$$
 \boxed{
 h_{13}s=\frac{72\delta\beta_{13}}{\pi(t-1)},
 \qquad
 k_{13}s=\frac{12\delta\beta_{13}}{\pi(t-1)}.}
 \tag{30}
$$
它们都在 $K$ 中。在 conjugate kernel 多项式中指定根
$X=-1+3\delta-6\delta/s$；这个轨道相对所选 Weyl-dual 正轨道的准确符号是
$$
 \epsilon_{\rm dual}=-\pi\frac{\bar\beta_{13}}{\beta_{13}}
                      \frac{t-1}{13-t}\in\{1,-1\}.
 \tag{30a}
$$
这里的根用 $s=g/\sqrt\pi$ 定义；若任意选 Gauss 根的符号，它不必是原正 $\pi$-orbit 的复共轭。独立消费者按这个明确根返回 $\epsilon_{\rm dual}$，不以符号吞掉 (30) 的六倍规范。

公开原完整执行已返回以下准确值，回执见第9节：
$$
 \boxed{
 \beta_{13}=-\frac{1+2\delta}{997920},\qquad
 A_0=\frac{17-5\delta}{997920},\qquad
 h_{13}s=-\frac{3+\delta}{110880},\qquad
 k_{13}s=-\frac{3+\delta}{665280}.}
 \tag{30b}
$$
令 $r=\sqrt\pi$、$s=g/r$，并保 $rs=g$。于是两个指定 Weyl-dual 正轨道的质量没有未定比例或符号：
$$
 \boxed{
 m_M=\frac{(3-\delta)r}{332640}
     =\frac{6-\delta}{166320r},\qquad
 m_U=-\frac{(3+\delta)s}{332640}
     =-\frac{6+\delta}{166320s}.}
 \tag{30c}
$$
这里 $\pi$ 核的正轨道是 (27) 的 $t_+$。消费者指定的
$\bar\pi$ 核根 $-1+3\delta-6\delta/s$ 的质量是
$+(6+\delta)/(166320s)=-m_U$；实际返回
$\epsilon_{\rm dual}=-1$。因此不能把这个指定的共轭核根未经换号便叫作 $\mathcal U_+$；(17)、(21) 的正号始终按同一 Weyl-dual 平方轨道规定。

这也把固定坏集合完全落实。纸笔分解为
$$
 332640=2^5 3^3\cdot5\cdot7\cdot11,\quad
 997920=3\cdot332640,\quad
 110880=332640/3,\quad665280=2\cdot332640.
 \tag{30d}
$$
又 $N_{K/\mathbf Q}(3\pm\delta)=12$，$r^2=\pi$、$s^2=\bar\pi$ 只添十三处。原 $\Phi$ 的最小分母 $385=5\cdot7\cdot11$、原 $\Psi$ 的整系数、两个 canonical kernel lifts 与六点平均均在 $\mathbf Z[1/(2\cdot3\cdot5\cdot7\cdot11\cdot13)]$ 的上述固定有限扩张上定义。因此 $m_M,m_U$ 在这六个有理素数之外确为单位；返回 $b=17$ 后，局部身份及其两个质量归一只需固定集合
$$
 S_{\rm new}=\{2,3,5,7,11,13,17\}.
 \tag{30e}
$$
本篇没有新添一个 $p>211$ 的坏素数。与第8节共同 carry 联用时仍保留 R968 原固定范围；若另消费该篇八阶局部首差的单位性，原来排除的 $p\mid1069$ 仍保留。

## 6. 返回共同 b=17 后的完整普通 Mellin

对任意固定单位模型 $b$，取相容六次根 $\vartheta_b^6=b$。
原算术来源与译像保持整体齐次度 $-1$：
$$
 \Phi_b(z)=b^{-1}\Phi(\vartheta_bz),\qquad
 \mathcal M_{+,b}(z)=b^{-1}\mathcal M_+(\vartheta_bz),\qquad
 \mathcal U_{+,b}(z)=b^{-1}\mathcal U_+(\vartheta_bz).
 \tag{31}
$$
原 degree10 的质量一来源则是
$$
 \Psi_b=\sigma_b^{10}x_b^2(x_b^3-8b)=\Psi(\vartheta_bz),
$$
故其两 raw pull $x_{\pi,b},x_{\bar\pi,b}$ 的质量仍为一。
(20)–(21) 的 old 部分在模型 $b$ 上准确多 $1/b$，而两个译像的质量为 $m_M/b,m_U/b$。
因此 (25) 返回为
$$
 \boxed{
 \frac{\mathcal U_{+,b}}{m_U/b}-\frac{\mathcal M_{+,b}}{m_M/b}
 =\frac34\Delta_{125,b}
  +\frac b{12}\left(\frac1{m_M}-\frac1{m_U}\right)\Phi_b.}
 \tag{32}
$$
当前共同模型始终取 $b=17$。

沿 R968 的同一普通 ray，置 $d=p-1$，使用准确变量
$$
 J_A(v)=\int_{\mathbf Z_p^\times}\langle Y\rangle^{dv}\,d\nu_A(Y),
 \qquad j_A=J_A'(0),\qquad
 \upsilon_p=\chi_{10}\lambda_p.
 \tag{33}
$$
R978 已付
$$
 J_{x_{\pi,b}}(v)=\langle\pi\rangle^{dv}J_{\Psi_b}(v),
 \quad
 J_{x_{\bar\pi,b}}(v)=\langle\bar\pi\rangle^{dv}J_{\Psi_b}(v),
 \quad J_{\Psi_b}(0)=1-\upsilon_p.
 \tag{34}
$$
对整个 (32) 应用同一线性读者，得到完整函数身份
$$
 \frac{J_{\mathcal U_{+,b}}(v)}{m_U/b}
 -\frac{J_{\mathcal M_{+,b}}(v)}{m_M/b}
 =\frac34\bigl(\langle\pi\rangle^{dv}
                -\langle\bar\pi\rangle^{dv}\bigr)J_{\Psi_b}(v)
  +C_bJ_{\Phi_b}(v),
 \tag{35}
$$
其中
$$
 C_b=\frac b{12}\left(m_M^{-1}-m_U^{-1}\right).
$$
用实际 (30c) 还可完全写成
$$
 C_b=2310b\left(\frac{3+\delta}{r}
                  +\frac{3-\delta}{s}\right),
 \qquad r^2=\pi,\ s^2=\bar\pi,\ rs=g.
 \tag{35a}
$$
所以
$$
 \boxed{
 \frac{j_{\mathcal U_{+,b}}}{m_U/b}
 -\frac{j_{\mathcal M_{+,b}}}{m_M/b}
 =\frac34(p-1)\log_p(\pi/\bar\pi)(1-\upsilon_p)
   +C_bj_{\Phi_b}.}
 \tag{36}
$$
这没有漏掉两个 base 导数；它们在 (35) 的差因子于 $v=0$ 为零后准确相消。
质量一是整个来源的质量，不能将式中分母再误换为单位部分质量。

原算术 rank 下界只迫 $J_{\Phi_b}(0)=0$；它不迫 $j_{\Phi_b}=0$。
若原联合坏素数假设给 $j_{\Phi_b}=0$，则 (36) 左边严格非零。
因为 $1-\upsilon_p$ 已是原 ray 的单位，而
$\pi/\bar\pi$ 在两个十三素理想处的赋值为 $1,-1$，不是根单位。
它在每个好普通目标位为单位，$p$-adic 对数零将迫它为根单位，矛盾。
若改用指数 $u$ 而非 $(p-1)v$，应删去显示的 $p-1$；本篇始终使用 (33)。

## 7. 同一个两源关系的完整惰性读者

令 $p\equiv5\pmod6$、$d=p+1$，沿 R978 保持原 degree10 与130 Gaussian。
在 (13) 的三维空间上，该篇与 R970 的完整 Newton 函数均已定义，且
$$
 J_{130,x_{\pi,b}}(v)=q_\pi^vJ_{10,\Psi_b}(v),\qquad
 q_\pi=\pi^{p+1}/13\in1+p\mathcal O,
$$
$$
 J_{130,x_{\bar\pi,b}}(v)=q_{\bar\pi}^vJ_{10,\Psi_b}(v),
 \qquad J_{10,\Psi_b}(0)=1.
 \tag{37}
$$
式 (20)–(21) 因而同时证明这四个实际译像的完整 Newton 级数收敛；不从一个任意质量非零形式级数猜该结论。
同样的线性消元给
$$
 \boxed{
 \frac{j_{\mathcal U_{+,b}}^{\rm in}}{m_U/b}
 -\frac{j_{\mathcal M_{+,b}}^{\rm in}}{m_M/b}
 =\frac34(p+1)\log_p(\pi/\bar\pi)+C_bj_{\Phi_b}^{\rm in}.}
 \tag{38}
$$
这里没有普通的 $1-\upsilon_p$。当原惰性坏中央为零时，左边对每个足够大的好惰性素数非零。其非零证明仍是同一非根单位的局部对数，不提出一个未经证明的统一赋值上界。

## 8. 原 mixed cut 的实际对偶与共同 C/F

式 (20)–(25) 是第一轴的 whole 截面身份。若应用于原完整六 sigma 状态，必须使用 R985 的真实伴随实现及全部对偶测试；不能由第一边际相同宣称两个 joint 状态相同。

这里可把对偶完全写出。对任一 even $N$ 的全 theta 空间，取标准基
$$
 B_j\in\{\sigma^Nx^a:0\le a\le N/2\}
       \cup\{\sigma^Nx^ay:0\le a\le N/2-2\},
$$
按其不同原点首阶 $r_j$ 排列。
首阶集合是 $\{0,\ldots,N-2,N\}$；原 $y$ 的首项符号也保留在
$$
 J_{ij}=[z^{r_i}]B_j
$$
这个可逆三角矩阵内。对同一个普通周期 $\Omega_p$，置
$$
 q_j(Y)=\sum_i(J^{-1})_{ji}
           \frac{Y^{r_i}}{r_i!\Omega_p^{r_i}}.
 \tag{39}
$$
原 Amice 矩公式使 $\nu_f(q_j)$ 恰为 $f$ 在 $B_j$ 中的坐标。
对任意完整连续 mixed 测试 $\tau(Y,Z)$，实际 finite theta transpose 是
$$
 \boxed{
 T_u^\dagger\tau(Y,Z)
 =\sum_jq_j(Y)\int\tau(y,Z)\,d\nu_{T_uB_j}(y).}
 \tag{40}
$$
逐个 $B_j$ 展开就给
$\langle T_u\mu,\tau\rangle=\langle\mu,T_u^\dagger\tau\rangle$。
各个轨道平均按 (17) 同样平均这整个核。
对原 $\tau={\bf1}_{aY+bZ\,{\rm unit}}
\langle aY+bZ\rangle^{dv}h(Z)$，内层是
$$
 h(Z)\int_{ay+bZ\,{\rm unit}}
               \langle ay+bZ\rangle^{dv}\,d\nu_{T_uB_j}(y).
 \tag{41}
$$
深度条件也原样留在这个内积分内。式 (40) 绝不是物理变量 $Y\mapsto Y+u$。

为固定整个来源，可用 R972 的实际 $P_*\mathcal F_{10,b}
=\Phi_b\otimes\Lambda_*$，再除以已付非零伴随质量 $\alpha_*=-11/2$，得到
$\Phi_b\otimes\widehat\Lambda_*$、$\widehat\Lambda_*(0)=1$。
对这同一个 joint 来源施 (17) 的第一轴算子，两个译像始终带同一个完整伴随；并未把它们和另一个边际相同的 raw joint 状态混认。

以下只从 R968 的原四输出身份推出所需读数，绝不把它升级成任意六变量 joint scalar。
记原秩四投影为 $\pi_{CF}$、原 $F_{10}$ 第一行为 $a_{10}$。
R971 已付 $a_{10}\pi_{CF}=a_{10}$；R968 付的是
$$
 (\pi_{CF})_*(\mathfrak q_{n,p}^{\rm new}\rho)
       =\upsilon_p^n(\pi_{CF})_*\rho.
 \tag{41a}
$$
把原整框架和固定归一记为
$\rho_{10}=c_{10}(L_{10})_*\rho$。
对于任意只动第一轴的有限 theta 算子 $B$ 和连续函数 $f(Y)$，
(40) 给 $B^\dagger f$ 是只含 $Y$ 的有限多项式。
所以 $(B^\dagger f)(a_{10}\xi)$ 确实是原四输出上的完整测试。
另一方面，共同 $C,F$ 在这个框架中不读第一轴，故逐个核准确有
$B^\dagger(\mathfrak q^{\rm new}f)
=\mathfrak q^{\rm new}B^\dagger f$。
于是在原对象上逐步得到
$$
 \begin{aligned}
 \langle B\rho_{10},\mathfrak q^{\rm new}f\rangle
 &=\langle\rho_{10},\mathfrak q^{\rm new}B^\dagger f\rangle\\
 &=\upsilon_p^n\langle\rho_{10},B^\dagger f\rangle
  =\upsilon_p^n\langle B\rho_{10},f\rangle.
 \end{aligned}
 \tag{41b}
$$
这适用于 $B=P_*$ 及 (17) 的第一轴平均与 $P_*$ 的实际复合，也保固定的 $\alpha_*^{-1}$。
故对 (36) 显示的两个第一边际中央，carry 的读数确实同时乘 $\upsilon_p^n$。
对于额外依赖被忘掉的 $C,F$ 或其余补变量的 mixed 测试，仍须用 (40)–(41) 的原 full adjoint；(41b) 不给这种任意测试一个 scalar。
因此，若原 canonical 坏中央为零，两个明确第一轴读数的 carry 差准确为
$$
 \frac34\upsilon_p^n(p-1)
    \log_p(\pi/\bar\pi)(1-\upsilon_p)\ne0.
 \tag{42}
$$
这支付了一个实际的非零差和全部 cut 变换；它没有将两个内积分分别替换成原 canonical 中央。

特别，若 $P_*$ 是原 rank-one 投影，算术坏中央只对完整
$\Phi\otimes\Lambda$ 和独立 companion 测试付零。
真实 companion 操作与 $P_*$ 交换，给 $P_*T_u$ 的左固定像；(17) 读的却是 $\Pi_0T_uP_*$。
要使 (42) 与已付零相矛盾，须在原 joint 状态及 (41) 的完整域上支付这两个指定测试的零，或支付等价的两个交换子组合。
第4节的有限角色已经把这个问题从全十三轨道压到明确的两个平均；不再需要任选全部130平方个平移来寻找一个非零项。

## 9. 独立完整22执行的来源门

本篇轻入口是 scripts/check-original-degree130-thirteen-torsion-entry.py；只调用原未改动的 norm7、norm19 full-fiber 公式，参数分别为 $(130,2,a)$。
两个公式都给完整22列，包含质量列；使用 $a=1,\ldots,24$，前22行重建，另外两条完整纤维回乘。
随后核整个矩阵的交换、共轭逆、十二次幂，并要求其 canonical hash 准确等于 R972/R976 原66限制所得
$$
\text{aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113}.
$$
这里是独立重建原22算子，没有伪造66维 context，也没有读取生成矩阵表。
R972/R976 已付的完整 pull/trace 交织仍是原来源门，不因本次省去重生66维而改变。

消费者 scripts/check-original-thirteen-torsion-forced-pair.py 再重建原 good-13 在整个 level10 两列上的四条完整纤维，核 (10)；锁定同一 $\Phi$ 的完整22坐标 hash；最后在两个实际 quadratic kernel 代数中对 (28) 作完整除法与回乘，返回 (29)–(30) 的准确常数和 Weyl-dual 轨道符号。
本次公开原完整执行是
[run45898016632](https://github.com/Rogerhu12/math-research-public/actions/runs/45898016632)，job140176625597，源提交
`05bed6026bd3b75f7f77b1927f55f72e4ed689cb`，2026-11-26 21:25:14–21:25:33 UTC，全部 PASS。
原完整数学入口耗时9.615498707秒，十三核消费者耗时0.129072532秒。
48条原 full-fiber、全部22列及质量列、各两个额外纤维、完整交换/共轭逆/十二次幂、原66限制的 canonical hash，均逐项返回；另四条 good-13 完整 level10 纤维也全部回乘。

| 实际固定对象 | 字节数 | SHA256 |
|---|---:|---|
| 独立 direct22 入口 `check-original-degree130-thirteen-torsion-entry.py` | 5792 | `dd4c858aed133196c03923e2dd76c59ebe72f51309e3e332ef34f74f311c4ba3` |
| 原十三核消费者 `check-original-thirteen-torsion-forced-pair.py` | 11563 | `550d182490d957b31898fda76c18999e2eaffc59f796eefd6b1dd75c26092104` |
| 精确 stdout | 3161 | `28d6484230677e55926863a204d4760fd35a9a77e22f2439021172ff8a373067` |
| 完整 job 日志 | 19218 | `edc808ff6fe24b43ff6cdf54a916b319df2666dc7dd66ac1e61f968ed14e716c` |

原 complete degree130 矩阵的 hash 正是上列 `aed9d071…`；实际 $\Phi$ 的完整22坐标 hash 为
`510b32718ce9ff51aee4a4de86cc5c362f7f0242a94b7d72df4effc0f95a4497`。
完整 level10 good-13 算子 hash 为
`064f23e1b663c72059c80997ef086e10e55b16583a29a52702fc6ae8c73731be`；实际返回 $N_\pi\Psi=\omega^2\Psi$、$\psi_{125}(\pi)=-1-2\delta$、$a/b=-1+2\delta$。
两个 quadratic kernel 的完整有理质量函数均完成除法与回乘，两条 trace 为零、两质量非零、共轭质量一致均为真；返回的 $A_0,\beta_{13},h_{13}s,k_{13}s$ 及 $\epsilon_{\rm dual}=-1$ 就是 (30b)–(30c)，没有由低 jet 或输出缓存代替原来源。

数学入口所列五个实际源码的 manifest hash 为
`38d52a26ccf51273a42fc180a9d874917f1bf768706cce8b23ab75615c497355`；workflow 的七项精确来源 manifest hash 为
`c38fa4c25b3e1b864263159078f5828b7abd7a4f56d4c03101ccb1142b5a4600`。五个实际执行源码的 AST 门与七项 manifest 门均通过。此回执核的是本篇已给出的完整有限身份及绝对相位；它没有将两个 translated 中央导数赋零。

## 依赖

- R970、R973：原 $E_{65^3}$ 与 $E_{125}$ 的完整有限角色、全平方及通常 Selmer 范围。
- R972、R976：整个66到22的原 pull/trace 交织、原 $\Phi$ 与全部质量列。
- R978：真实两13-old raw pull、质量一 $\Psi_{125}$、完整普通及惰性差函数。
- R985：原 canonical Heisenberg lift、真实完整伴随与有限 theta 测度对偶。
- R968：同一 $C,F$ 的 whole carry、全部实际域及完整补域。

无穷多个素数的通常全 Sha 结论仍需原算术测试的最终联合非零；本篇新增的是原两个具体十三测试、其固定 $3/4$ 关系和可直接与共同 carry 联立的完整非零读数。
