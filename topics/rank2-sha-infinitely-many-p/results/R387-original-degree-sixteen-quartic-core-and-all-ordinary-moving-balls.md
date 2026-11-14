# R387：原 degree16 四次双谱、全部普通 core 与十二球返回

日期：2026-11-14。**状态：已证明。** 本篇继续 R381 的同一对来源，不增加任意参考空间。原 $D_{16}$ 与它的真实伴随组成两个四次角色的共同特征线；这给全部普通素数的完整二维 core。利用同 degree、同标签的实际球值，奇偶交换只对原比值施一个明确的分式线性变换。因此 R381 的十二球整返回推广到每个普通 $p>17$，且仍保任意第三坐标、全部 tame、原单位输出和完整补域。

本篇同时自证 $E_{24}:y^2=x^3+24$ 的秩至少二，并用同一个真实 CM7 算子严格区分它与旧 $D_{16}$。两条新对角线的质量为一，不把它们当作两条新的有理 rank-two 椭圆曲线，也不预赋其中央斜率。原主目标仍未完成。

## 1. 同一原来源及主结论

沿用 R379、R381 的原微分与 sigma 规范：
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad X=x^3,
$$
$$
x=z^{-2}+\cdots,\qquad y=-z^{-3}+\cdots,\qquad
\Theta=x\sigma^2,\qquad dz=\frac{dx}{2y}.
$$
定义
$$
\begin{aligned}
D&=\sigma^{16}x^2(X+b),\\
E&=\sigma^{16}x^2(X^2-28b^2),\\
H&=E+20bD=\sigma^{16}x^2(X^2+20bX-8b^2),\\
K_4&=\Theta(2z)^2=\sigma^{16}x^2(X-8b)^2.
\end{aligned}
\tag{1}
$$
这里 $D$ 就是 R381 的 $D_{16}$，$E$ 就是该篇 $E_{16}$，而
$$D(0)=0,\qquad H(0)=E(0)=K_4(0)=1.$$
它们都是原 degree16、$\mu_6$ 不变的全纯截面。特别
$$
D=\sigma^6\Theta^5+b\sigma^{12}\Theta^2,\qquad
E=\Theta^8-28b^2\sigma^{12}\Theta^2,
\tag{2}
$$
所以 R316 的真实有界测度给出它们自己的有界测度；没有取 Mellin 商。

取 $\iota^2=-1$、$s=\delta/\iota$，故 $s^2=3$。两条准确对角线是
$$
\boxed{F_+=H+24bsD,\qquad F_-=H-24bsD.}
\tag{3}
$$
以下证明它们的完整原 core，并以此计算 (1) 的真实球值，而不是只认一个有限样本的本征值。

对普通 $p>17$，固定原目标的嵌入和周期，记
$$
\pi=\psi_{17}(\mathfrak p),\quad
\pi_0=\psi_0(\mathfrak p)=\varepsilon\pi,\quad
\kappa=p/\bar\pi^2,\quad
\lambda_0=\varepsilon/\bar\pi=1/\bar\pi_0 .
\tag{4}
$$
$\psi_0$ 属于 $y^2=x^3+1$。第3节定义一个完全明确的四次理想角色 $\rho$；
令 $\rho_p=\rho(\mathfrak p)\in\{1,-1,\iota,-\iota\}$。主 core 是
$$
\boxed{
\nu_{F_\pm}|_{p\mathbf Z_p}
 =\lambda_\pm[\kappa]_*\nu_{F_\pm},\qquad
\lambda_+=\lambda_0\rho_p,\quad
\lambda_-=\lambda_0\rho_p^{-1}.
}
\tag{5}
$$
而且
$$\boxed{1-\lambda_+,\ 1-\lambda_-\in\mathcal O^\times.}\tag{6}$$
所有系数可在一个固定包含 $\iota$ 的有限扩张中读取；回到 $(D,H)$ 的矩阵仍在原 $K$ 中。

真正用于原域的结论是：对 $N\ge49$ 和每个单位中心 $t$，置
$$
d_N(t)=\nu_D(t+p^N\mathbf Z_p),\quad
e_N(t)=\nu_E(t+p^N\mathbf Z_p).
$$
则
$$
\boxed{
d_N(t),\ d_N(2t),\
\Delta_N(t):=e_N(t)d_N(2t)-e_N(2t)d_N(t)
\in\mathcal O^\times .
}
\tag{7}
$$
(7) 对本篇全部普通素数成立，不再需要 R379 的特殊完全分裂族。
其结果仍是十二个原小球的有权返回，不是其中任何单叶的零传播。

## 2. 完整 CM7、CM13 迹与原中心锚

先在 $b=1$ 上计算；固定 homothety 在第4节传回 $b=17$。
整个 $\mu_6$ 不变块准确为
$$
V=\operatorname{span}\{\sigma^{16}x^2,\sigma^{16}x^5,\sigma^{16}x^8\}.
\tag{8}
$$
原因是 $\sigma^{16}L(16O)$ 的原单项式基只有这三个单项式的总型为零。
(1) 中 $(D,H,K_4)$ 对 (8) 的行列式是 $108$，在一般 $b$ 时是
$108b^2$。因此它们在所有本篇素数给同一个完整整格。

令
$$
\gamma=3+\omega,\quad\gamma_{13}=4+\omega,\qquad
\varpi_7=\omega\gamma=-1+2\omega,\quad
\varpi_{13}=-\omega^2\gamma_{13}=3+4\omega.
$$
后两个是原 $\psi_0$ 的 primary 生成元，均 $\equiv1\pmod{2\delta}$。
采用 R300、R358 的原迹
$$
\mathscr M_a(\sigma^{16}f)
=\sigma^{16}\operatorname{Tr}_{[a]}
       \left[(r_{\bar a}/r_a)^{16}f\circ[\bar a]\right],
\quad r_a=\frac{\sigma(az)}{\sigma(z)^{Na}} .
\tag{9}
$$
$ r_a $ 的首项常数是 $a$，不改成 monic division。

准确的完整三维结果为
$$
\boxed{
\begin{array}{c|ccc}
 &D&H&K_4\\ \hline
\varpi_7^{-1}\mathscr M_\gamma
 &\delta H/(72b)&24b\delta D&-K_4\\
\varpi_{13}^{-1}\mathscr M_{\gamma_{13}}
 &\delta H/(72b)&24b\delta D&+K_4 .
\end{array}}
\tag{10}
$$
这里两行的 type0 来源在从 $a$ 换成实际 $\varpi$ 时不变；
这是 R358 的准确单位律
$\mathscr M_{ua}G=u^{-2k}\mathscr M_aG$ 对 $k=0$ 的应用。

为给 (10) 一份可复算的完整特征零证明，所需原 division 输入只有
$$
r_\gamma=\gamma\left(x^3+\frac{4+12\omega}{7}\right),\qquad
r_{\gamma_{13}}=\gamma_{13}
 \left(x^6+(8+12\omega)x^3+\frac{64+48\omega}{13}\right).
\tag{11}
$$
对任一 $q=r_a$、$n=Na$，由 $-\partial_z^2\log\sigma(az)=a^2x(az)$，
$$
x(az)=\frac{U_a}{V_a},\quad
U_a=nxq^2-4(x^3+1)(q''q-q'^2)-6x^2q'q,\quad V_a=a^2q^2.
\tag{12}
$$
对目标横坐标 $h=2,3,4$，取首一的
$f_h=U_a-hV_a$。它的 degree 为 $n$，且是完整 $[a]$ 纤维的横坐标代数。
这些目标不在二挠点，故由特征零同源的非分歧性知纤维可分。
在 $\mathbf Q(\omega)[x]/(f_h)$ 中准确计算
$$
[x^{n-1}]
\left[
 f_h'
 \left(\frac{q_{\bar a}}{q_a}\right)^{16}
 \left(\frac{U_{\bar a}}{V_{\bar a}}\right)^{2+3j}
 \bmod f_h
\right],\quad j=0,1,2.
\tag{13}
$$
三点的 $(h^2,h^5,h^8)$ 矩阵可逆，因 (8) 已付，(13) 确定整个算子。
随附脚本还在 $h=5$ 的完整纤维逐列核对。它输出原基的两张矩阵，
不是仅验候选向量的低阶系数。

绝对标量也有同 degree 的原锚：
$$
\sigma(4z)=-4\sigma^{16}y(X^2+20bX-8b^2).
\tag{14}
$$
CM7 的三个完整纤维连同真实
$$
\frac{y(\bar aP)}{y(aP)}
=\frac a{\bar a}\frac{(U_{\bar a}/V_{\bar a})'}
                         {(U_a/V_a)'}
$$
给 $\mathscr M_\gamma\sigma(4z)=\gamma\sigma(4z)$。
CM13 的符号也由 R358 已付的 $\sigma(2z)$ 行及实际 $[2]$ 拉回给出
$\mathscr M_{\gamma_{13}}\sigma(4z)=-\gamma_{13}\sigma(4z)$。
换成 primary 元素后，两者都是
$\mathscr M_{\varpi}\sigma(4z)=\varpi\sigma(4z)$。
一般普通素数的同一锚由 R316 的 $\sigma$ 测度及单位尺度四直接给出。

记 (10) 在 $(D,H)$ 上的归一算子为 $J$，则
$$
JD=\frac{\delta}{72b}H,\qquad JH=24b\delta D,\qquad J^2=-1.
\tag{15}
$$
所以 (3) 的本征值分别为 $\iota,-\iota$。
原 CM7 的完整谱是
$$
-\varpi_7,\quad \iota\varpi_7,\quad-\iota\varpi_7 .
\tag{16}
$$
作为独立的原点接口，在 (8) 中原质量行与其前两次 CM7 运输的行列式为
$$
\det\begin{pmatrix}e_2\\e_2\mathscr M_\gamma\\e_2\mathscr M_\gamma^2\end{pmatrix}
=\frac{17-20\omega}{3888}\ne0.
\tag{17}
$$
因此整个原块没有非零的、所有 CM7 运输都保持质量零的子空间。
这不把质量的非零值当作中央导数。

## 3. 全部有限 dyadic 相位及真正四次角色

使用原对称 Heisenberg lift
$$
(\mathsf T_vG)(z)=
e^{-16\eta_v(z+v/2)}G(z+v).
$$
完整交织按模三十二读取：
$$
\mathscr M_a\mathsf T_v=
  \mathsf T_{a\bar a^{-1}v}\mathscr M_a.
\tag{18}
$$
两个原标准平移的交换子是 primitive 十六次根，所以整个十六维表示不可约。
以 (14) 的同一原锚归一后，同一 ratio 给同一算子；乘积也仍固定锚。
于是归一作用是真正的有限表示，包含中心相位。

全部可能的 primary ratio 是
$$
H_{32}=\{a/\bar a\bmod32:a\equiv1\pmod2\}.
$$
$a\equiv1\pmod2$ 有 $256$ 个可逆类，ratio 核恰为十六个奇有理标量，
所以 $|H_{32}|=16$。具体
$$
g_7=27+8\omega,\qquad
g_{13}=29+8\omega,\qquad
H_{32}=\langle g_7,-1\rangle\simeq C_8\times C_2,
$$
$$
g_7^4=17,\qquad g_{13}=-g_7^3.
\tag{19}
$$
全十六个类由固定模三十二整数计算直接列出，证书没有扫描目标素数。

ratio $-1$ 由 $G(z)\mapsto G(-z)$ 实现。该算子在原锚 $\sigma(4z)$ 上为负，
所以锚定后的算子是 $-G(-z)$。在 (8) 上它准确为 $-1$。
再由 (10)、(15)，本块的 $g_7^4$ 作用为一；因此作用下降到 $H_{16}$，
而不是忽略这个中心后猜测下降。

唯一需要的四次特征为
$$
\boxed{\rho(g_7)=\iota,\qquad\rho(-1)=-1.}
\tag{20}
$$
两条 $F_\pm$ 上的完整特征是 $\rho,\rho^{-1}$；
第三条 $K_4$ 是已付的 $(-1/p)$ 特征。
若 $a=A+B\omega$ 是任意奇单位，先用唯一 $\mu_3$ 单位使 $a\equiv1\pmod2$，
再将 $a/\bar a\bmod16$ 代入 (20)。
这个定义在全部全局 $\mu_6$ 单位上平凡，因此由 $K$ 的类数一
定义一个真正的理想角色。它的 conductor 准确为 $16\mathcal O_K$：
$1+16\mathcal O_K$ 在核中，而
$$
\frac{1+8\omega}{1+8\bar\omega}\equiv9=g_7^2\pmod{16},
\qquad \rho(9)=-1.
\tag{21}
$$
从 (19) 的范数类，或直接使用 R358 的完整八类表，
$$
\boxed{\rho(\mathfrak p)^2=\left(\frac{-2}{p}\right).}
\tag{22}
$$

故原共同 Hecke 谱可以准确记为
$$
\psi_+=\psi_0\rho,\qquad\psi_-=\psi_0\rho^{-1}.
\tag{23}
$$
它们的 conductor 是 $16\delta$，对应 weight-two Hecke theta series
的经典 level 是 $3N(16\delta)=2304$。
此处 (23) 识别实际 CM 算子的谱，不另冒认一个未付的 Yang 全权平方常数。

写 $\pi_0=A+B\delta$，则 $A,B\in\mathbf Z$、$A\equiv1\pmod3$。
其 good-prime 系数为
$\rho_p\pi_0+\rho_p^{-1}\bar\pi_0$，
因此都在 $\mathbf Q(s)$ 中；在七处为 $\mp2s$，故系数域准确是
$\mathbf Q(\sqrt3)$。特别这两条不是两条定义于 $\mathbf Q$ 的
sextic-twist 椭圆曲线，不能据此加入原有理 rank-two 候选池。

## 4. 原周期、全部二维 core 与每个环带

R300 的原正式群 trace 在 $\mathcal S_{16}$ 给
$T_{p,0}=\pi_0^{-1}\mathscr M_{\pi_0}$。
(18)–(20) 和原锚于是支付全部普通素数上的特征，而不只七、十三两点。

令 $\theta=17^{1/6}$，原正式同构给
$$
\Omega_{p,0}=\theta\Omega_p,\quad
D_b(z)=b^{-1}D_0(\theta z),\quad
H_b(z)=H_0(\theta z),\quad F_{\pm,b}(z)=F_{\pm,0}(\theta z).
\tag{24}
$$
又 $p/\bar\pi_0^2=\varepsilon^2\kappa$。全部来源的 $\mu_6$ 型都是零，
所以 $[\varepsilon^2]_*$ 在原测度上为一，(5) 连同其原周期成立。

也可完全在原 $K$ 中写矩阵。置
$$
u_p=(\rho_p+\rho_p^{-1})/2,\qquad
v_p=(\rho_p-\rho_p^{-1})/(2\iota).
$$
它们是 $0,\pm1$，原算子为 $R_p=u_p+v_pJ$。于是
$$
\boxed{
\begin{aligned}
\nu_D|_p&=\lambda_0[\kappa]_*
 \left(u_p\nu_D+v_p\frac{\delta}{72b}\nu_H\right),\\
\nu_H|_p&=\lambda_0[\kappa]_*
 \left(u_p\nu_H+24b\delta v_p\nu_D\right).
\end{aligned}}
\tag{25}
$$
这保留了 $D$ 的原质量零与 $H$ 的质量一。
特别不能在 $\rho_p=\pm\iota$ 时把 $D$ 错写成标量 core。

对任意 $n\ge0$，
$$
\nu_G|_{p^n\mathbf Z_p}
 =\lambda_0^n[\kappa^n]_*\nu_{R_p^nG},
\qquad G\in\operatorname{span}(D,H).
\tag{26}
$$
定义原单位 Mellin
$$
M_{G,\ell}(u)=\int_{\mathbf Z_p^\times}
 \omega_p(x)^\ell\langle x\rangle^{du}\,d\nu_G(x),
\qquad d=p-1.
$$
原第 $n$ 环带以 $x/p^n$ 为变量时，准确有
$$
\boxed{
M^{[n]}_{G,\ell}(u)=
\lambda_0^n\omega_p(\bar\pi)^{-2n\ell}
 \langle\bar\pi\rangle^{-2ndu}M_{R_p^nG,\ell}(u).
}
\tag{27}
$$
中央导数因此保留
$$
\lambda_0^n\omega_p(\bar\pi)^{-2n\ell}
\left(M'_{R_p^nG,\ell}(0)
 -2nd\log_p(\bar\pi)M_{R_p^nG,\ell}(0)\right).
\tag{28}
$$
(27)–(28) 是全部 tame 的原式，不把非单位输出或非零质量删去。

## 5. 两条真实参考的单位质量

(5) 和 $F_\pm(0)=1$ 给
$$
M_{F_\pm,0}(0)=m_\pm:=1-\lambda_\pm.
$$
下面直接证明 (6)，不借未知的中心秩或高度。

若 $\rho_p=\pm1$，非单位会迫 $2A\equiv\pm1\pmod p$。
$p>7$ 时 $|2A|\le2\sqrt p<p-1$，所以只能 $2A=\pm1$，与偶性矛盾。
若 $\rho_p=\pm\iota$，非单位迫
$$p\mid4A^2+1.$$
因为 $p=A^2+3B^2$ 且 $B\ne0$，
$$0<4A^2+1<4p.$$
左边为奇数，故只能等于 $p$ 或 $3p$。
然而 $A^2\equiv1\pmod3$、$p\equiv1\pmod3$，
左边模三为二，两个右边模三分别为一、零，矛盾。

两条相对斜率仍记为
$\mathcal S_\pm=M'_{F_\pm,0}(0)/m_\pm$，不赋已知值。
原实际关系是
$$
\boxed{
M'_{D,0}(0)=
\frac{m_+\mathcal S_+-m_-\mathcal S_-}{48bs}.
}
\tag{29}
$$
在 R379 的完全分裂族上 $\rho_p=1$，它化成相同单位质量乘两条斜率之差。
(29) 没有消掉这两条未知的完整导数。

## 6. 同一联合来源及原点辅助域的准确奇偶运输

保留 R379、R381 的原定义
$$
A_8=\sigma(z)\sigma(2z)\sigma(\delta z),\qquad
C_{18}=\sigma^{18}(X-8b)
       \left(X^2-\frac{4bX}{7}+\frac{16b^2}{7}\right),
$$
$$
S=-A_8^2C_{18}/12=DC_{18}.
\tag{30}
$$
完整反对称 theta identity 可直接改写为
$$
\boxed{
\mathcal P_{\mu_6,u}[A_8(z+u)A_8(z-u)]
=\frac{F_-(z)F_+(u)-F_+(z)F_-(u)}{4bs}.
}
\tag{31}
$$
这是 R381 原式 $12(E\otimes D-D\otimes E)$，
利用 $H=E+20bD$ 和 (3) 后的同一来源，未加任意列。

在三原输入 $(a,b_1,c)$ 上使用
$-\nu_{A_8}\otimes\nu_{A_8}\otimes\nu_{C_{18}}/12$，并置
$$
Y=a+b_1+c,\quad Q=a-b_1,\quad R=9(a+b_1)-8c .
$$
记其真联合为 $\mathcal J$。若
$$
\eta_G=(u+c,\,9u-8c)_*(\nu_G\otimes\nu_{C_{18}}),
$$
则保任意 $(Y,R)$ 的完整式是
$$
\boxed{
\mathcal P_Q\mathcal J
 =\frac{\eta_{F_+}\otimes\nu_{F_-}
            -\eta_{F_-}\otimes\nu_{F_+}}{48bs}
 =\eta_D\otimes\nu_E-\eta_E\otimes\nu_D .
}
\tag{32}
$$
这里每个 $\eta_G$ 都是原加法推前；没有将其 Mellin 写成两因子的乘积。

由 (5)，对所有 $n\ge0$，
$$
\boxed{
\operatorname{pr}_{Y,R*}
 (1_{Q\in p^n\mathbf Z_p}\mathcal J)
 =\frac{\lambda_-^n\eta_{F_+}
                -\lambda_+^n\eta_{F_-}}{48bs}.
}
\tag{33}
$$
若 $\rho_p^{2n}=1$，右边准确为
$\lambda_0^n\rho_p^n\eta_D$。
若 $\rho_p^{2n}=-1$，右边准确为
$$-\frac{\lambda_+^n}{24bs}\eta_H.$$
因此第二种情形确实留下原质量一伴随来源；不能把所有深度都改成原 $S$。
对 $Y$ 的所有单位 tame 测试，(33) 原样成立，不新增尺度因子。

## 7. 同标签球值、分式线性交换与单位行列式

R376 的真正 theta-group 球公式可同时用于 $F_+,F_-$：
它们有相同 degree16、相同原 period、相同刻画球标签的配对。
因此存在与 $G$ 无关的原单位因子 $u_N(t)$ 和同一个 étale 点 $P_t$，使
$$
\boxed{
\nu_G(t+p^N\mathbf Z_p)
 =\lambda_0^N u_N(t) f_{R_p^NG}(P_t),
\quad G=\sigma^{16}f_G\in\operatorname{span}(D,H).
}
\tag{34}
$$
$P_t$ 的原 étale 阶恰为 $p^N$，整数尺度给
$P_{2t}=2P_t$。这里使用的是 R376 未重标的完整 vertical/frame 抵消，
不是把两条不同 core 的球值直接当同一个标量。

$D,H$ 的全部零都为固定 prime-to-$p$ 挠点：
$$
\begin{array}{c|c}
D& O\text{ 六阶；两个非零三挠点各二阶；三个非零二挠点各二阶}\\
H&\text{两个上述三挠点各二阶；十二个四挠但非二挠点各一阶}.
\end{array}
\tag{35}
$$
第二行由准确原恒等式
$$
\boxed{H=-\frac{x^2}{4y}\sigma(4z)}
\tag{36}
$$
得到；二挠处的零与 $y$ 正好相消，原点值为一。
在全部本篇素数，这些除子与非零原 étale $p$-power 点不相交，
而整模型的因子均为单位。

若 $\rho_p^{2N}=1$，$R_p^N$ 是标量；否则它是 $\pm J$。
由 (15)、(34)–(36)，$d_N(t)$ 对每个非零标签都是单位。
令
$$
r(P)=\frac{E(P)}{D(P)}
     =\frac{X(P)^2-28b^2}{X(P)+b},\qquad
r_0=r+20b=H/D.
$$
同 degree 的全部球因子现在准确抵消：
$$
\boxed{
\frac{e_N(t)}{d_N(t)}
=\begin{cases}
r(P_t),&\rho_p^{2N}=1,\\
\dfrac{1728b^2}{r(P_t)+20b}-20b,
       &\rho_p^{2N}=-1.
\end{cases}}
\tag{37}
$$
后一行保留了原交换矩阵的常数 $1728$。
因为 $r_0(P_t)$、$r_0(2P_t)$ 都是单位，奇数交换时的差为
$$
-\frac{1728b^2}{r_0(P_t)r_0(2P_t)}
       \bigl(r(P_t)-r(2P_t)\bigr).
\tag{38}
$$
这就是与旧单位判据完全相同的原有理差，乘的仍是一个真实单位。

为完整说明深度界，$r-r\circ[2]$ 的极总阶为四十八：
四个二挠点各六阶，另十二个四挠点各二阶。
原点六阶主项的系数为 $1-2^{-6}=63/64$，
所以 $p>17$ 时约化不为零。
若 $P_t$ 是其约化零点，零除子的固定 degree48 使
$P_t\in E(\mathbf F_{p^e})$、某个 $e\le48$。
但 $P_t$ 的阶为 $p^N$，而
$$
\#E(\mathbf F_{p^e})\le p^e+1+2p^{e/2}<p^{e+1}
$$
迫 $N\le e$。所以 $N\ge49$ 时
$r(P_t)-r(2P_t)$ 是单位。
结合 (34)、(37)、(38) 即证明 (7)。

## 8. 原十二球权与全部中央补域

设
$$
\chi_N(Q;t)=\frac16\sum_{\zeta\in\mu_6}
                  1_{Q-\zeta t\in p^N\mathbf Z_p},
$$
$$
\boxed{
W_N(Q;t)=
\frac{d_N(2t)\chi_N(Q;t)-d_N(t)\chi_N(Q;2t)}
     {\Delta_N(t)}.
}
\tag{39}
$$
十二个球互不相交，因为 $2^6-1=63$ 是单位。
(7) 证明每个实际权为单位，且它只依赖 $(Q,t)\bmod p^N$。
准确有
$$
\int W_N(Q;t)\,d\nu_E(Q)=1,\qquad
\int W_N(Q;t)\,d\nu_D(Q)=0 .
\tag{40}
$$
因此 (32) 给：对任意原 $(Y,R)$ 域 $\mathcal B$、
任意连续单位中心 $t=t(Y,R)$，
$$
\boxed{
\operatorname{pr}_{Y,R*}
 \left(1_{\mathcal B}W_N(Q;t(Y,R))\,\mathcal J\right)
 =1_{\mathcal B}\eta_D .
}
\tag{41}
$$
这是同一完整联合的点点有限恒等式，不是从一个已知中央零自由乘上
$Y$ 依赖权。取 $t=Y$、$Y\in\mathbf Z_p^\times$，再积分全部 $R$，
$$
\boxed{
Y_*\left(1_{Y\in\mathbf Z_p^\times}W_N(Q;Y)\mathcal J\right)
=\nu_S^\times .
}
\tag{42}
$$
故对全部 tame $\ell$、完整 $u$，
$$
\int 1_{Y\in\mathbf Z_p^\times}W_N(Q;Y)
 \omega_p(Y)^\ell\langle Y\rangle^{du}\,d\mathcal J
=M_{S,\ell}(u).
\tag{43}
$$
(41)–(43) 对每个普通 $p>17$、每个 $N\ge49$ 成立。

原单叶只占其中一部分：若还限制 $R-9Y\in p^N$，
$Q\simeq\pm Y$ 给两条单个 $A_8$ 输入为单位的叶；
其余四个 $Q\simeq\zeta Y$ 以及六个
$Q\simeq2\zeta Y$ 都必须保留。
本篇没有把这些补域赋成零，也没有将随 $Y\bmod p^N$ 变化的权
换成常数。R384 第二移动中心的特殊素数族前提亦未在此擅自推广。

## 9. E24 的独立秩证书与真实来源区别

这里给候选曲线自身的短证书，以免把正确的秩事实和错误的旧来源识别混在一起。
令
$$E_{24}:y^2=x^3+24,\qquad P=(-2,4),\quad Q=(1,5).$$
直接计数得到
$$\#E_{24}(\mathbf F_5)=6,\qquad\#E_{24}(\mathbf F_7)=13.$$
两个都是好约化，故有理 torsion 为零。
在 $\mathbf F_{19}$ 中，
$$
3P=(0,9),\quad3Q=(0,10),\quad
P+Q=(18,2),\quad 3(P+Q)=O,\quad9P=9Q=O.
$$
$P+Q$ 不在 $\langle3P\rangle$，所以 $\langle P,Q\rangle$
的约化含 $C_9\times C_3$。
若 $E_{24}(\mathbf Q)$ 的秩至多一且 torsion 为零，它的每个有限约化像均为循环群，
矛盾。因此
$$\boxed{\operatorname{rank}E_{24}(\mathbf Q)\ge2.}\tag{44}$$

但在 $\mathfrak q=(3+\omega)$，有 $\omega\equiv4\pmod{\mathfrak q}$、
$24\equiv3=-\omega$。原六次剩余公式准确给
$$
\psi_{24}(\mathfrak q)
 =\psi_0(\mathfrak q)(24/\mathfrak q)_6^{-1}
 =\varpi_7(-\omega^2)=-\gamma .
\tag{45}
$$
它不在 (16) 的整个原 type0 谱中。
所以旧 $D_{16}$ 不能识别为该曲线的原单一 Hecke 来源，
甚至这个原三维块中也没有其同一 CM7 特征线。

真正不同的坏点输入已经由 R389 自证：
$$
\mathfrak f_{\psi_{24}}=8\delta^4,\qquad
N(E_{24})=15552,\qquad \alpha_{\rm Hermitian}=1.
\tag{46}
$$
特别三处有 $K_3(\delta^{1/3})/K_3$ 的实际野三次角色、conductor exponent 四；
它不是旧 ground Schwartz 的 conductor-one 角色。
(44) 不支付这个新野 Schwartz 与旧 $D,H$ 的运输，
(45) 也不排除用正确的新来源继续研究 $E_{24}$。

## 10. 证书、同步和已付范围

生产证书为
[check-jzero-degree-sixteen-quartic-core-and-moving-balls.js](../scripts/check-jzero-degree-sixteen-quartic-core-and-moving-balls.js)。
它用有理 BigInt 的 $\mathbf Q(\omega)$ 算术完成
两张完整原 CM 迹、原 $\sigma(4z)$ 锚、全部模三十二相位、
精确 conductor 末层，以及 (44) 的固定三个有限域证书，
共五十三项通过。它不扫描目标 $p$，也不以小数识别来源。

完整结论是：同一原十二球来源现在对全部普通大素数有整的、无损的返回，
且每条参考斜率和每个单位补域都有明确去向。
仍未证明原 $M'_{S,0}(0)$ 对无穷 $p$ 非零。

本次终端不可用，采用已获授权的 GitHub 集成提交小文本；API 同步没有称为 git pull。
2026-11-14 01:48:33 UTC 读取 API main c7b31b2743b57ce65b8eb242e59dd50bca04eb74，从上次已读 c1f9accb5dca96c74b4b0474a61011a52dc8dbbf 比较，两份 README 均无变化；读号交根代理记入 HANDOFF。

### 引用

- [R297：原 CM division 与真实来源](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R300：原全 theta 迹和单 Euler 测度](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)。
- [R316：原 sigma/Theta 测度及周期](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R358：全部有限 dyadic 相位和原中心锚](R358-original-collision-reference-absolute-cores-and-unit-tubes.md)。
- [R376：原加法球 theta-group 公式](R376-original-additive-ball-theta-group-formula-and-integral-torsion-values.md)。
- [R379：同一 S 的三输入正交返回](R379-original-third-joint-core-unit-collisions-and-three-input-return.md)。
- [R381：原反对称联合和完整十二球返回](R381-original-antisymmetric-joint-twelve-balls-and-complete-reference-elimination.md)。
- [R384：原第二移动中心和全部双返回](R384-original-second-moving-center-integral-interpolation-and-double-return.md)。
- [R389：E24 的原 wild 局部角色与实际 Hermitian 类](R389-e24-primitive-wild-local-data-and-actual-hermitian-class.md)。
