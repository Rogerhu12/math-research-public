# R46：八平移packet的完整三阶固定度量圆

日期：2026-11-14。literature 推导，repo_sources 独立逐项手核，root 全文复核。**独立完整证明；只作精确符号代数，没有运行新几何研究计算。**

本稿接 [倒行四块构造](R45-reversal-four-block-third-period-cancellation.md)：该构造给真实的闭合周期浸入带、全零二阶算子，以及准确相消的三阶周期函数。本稿进一步用八个明确平移和代数幅度，准确支付此前尚未解决的两条逐 ruling 三阶函数。

**结论。** 存在真实光滑周期浸入带、显式紧支撑 profile 圆和周期光滑校正，使同一个固定度量的 Taylor 等距方程完整满足到三阶，统一误差为 $O(\varepsilon^4)$。这比仅有三矩或二阶周期为零更强。

**边界。** 尚未支付四阶以后、形式级数收敛、固定非零 epsilon 的精确连续等距族、闭面嵌入、reach 或宏观握持位移。本稿不满足课题完成标准。

## 1. 几何、锚和一个三矩配平 packet

使用上述四块几何，其单路径 P 从框架 I 到
$D=\operatorname{diag}(-1,1,-1)$，标量首末为同一常值芽，且准确 $M_P=0$。保留

$$z=\xi+\omega,\quad u=h/z,\quad e=hz-k,\quad
Q=1+e^2,\quad w=h^2-ku,$$

$$\gamma=h_s,\quad\nu=\omega_s=\frac{k_s}{2h},\quad
c=\partial_su|_\xi=\frac\gamma z-\frac{h\nu}{z^2},
\quad u_\xi=-\frac h{z^2}.$$

各处 s 导数均固定 xi，除非另行注明。

先取 R39 的一个显式实 profile pair $(f_0,g_0)$：令偶 bump eta 的支撑为 $[-0.1,0.1]$，

$$b_j(x)=\eta(x-j)+\eta(x+j),$$

$$f_0=\sqrt{19/30}\,b_1+\sqrt{11/30}\,b_4,
\qquad g_0=(b_2+b_3)/\sqrt2.$$

其联合支撑包含于 $[-4.1,4.1]$，f、g 支撑互不相交，并满足

$$I_0(f_0)=I_0(g_0),\quad I_1(f_0)=I_1(g_0),\quad
I_2^*(f_0)=I_2^*(g_0),\tag{1}$$

以及三交叉矩为零。其中

$$I_0(\chi)=\int\chi''^2,\quad I_1(\chi)=\int\xi\chi''^2,
\quad I_2^*(\chi)=\int\xi^2\chi''^2+2\int\chi'^2.$$

可共同缩放该 packet，使后述八个互不交平移都位于同一个正物理活动区间；R39 的准确仿射变换律保持 (1)。两侧留开放零 collar。

二阶 forcing 是 $H_d=(dY_f)^2-(dY_g)^2$。始终用同一右 xi collar 确定 rho，并在 P 的 $s=0$ 取 $W=0$。$M_P=0$ 确保 $W$ 在 P 的另一端也为零。不得对不同 packet 独立改换第二个 s 规范。

## 2. 完整 characteristic 右侧逐点为有限多项式

对单个 profile chi 定义右尾矩

$$J_0(\xi)=\int_\xi^r\chi''^2,\qquad
J_1(\xi)=\int_\xi^r x\chi''^2,$$

$$J_2^*(\xi)=\int_\xi^r x^2\chi''^2+2\int_\xi^r\chi'^2.$$

令 $d=h\omega-k$，

$$r_0=\frac{d^2+1}{8h},\quad r_1=\frac d4,\quad r_2=\frac h8,$$

$$\ell_0=\frac h{2z},\quad \ell_1=-\frac e{2z},\quad
\ell_2=\frac{hz}4-\frac{3k}8+\frac{k^2+1}{8hz}.$$

已知的准确 ruling 原函数是

$$\rho_\chi=r_0J_0+r_1J_1+r_2J_2^*
+\ell_0\chi^2+\ell_1\chi\chi'+\ell_2\chi'^2.\tag{2}$$

定义

$$K_0=kz^2-\frac{k^2+1}{h}z,
\qquad\lambda=\frac c{u^2}=\frac{\gamma z-h\nu}{h^2}.$$

完整 characteristic 右侧为

$$\mathcal R_\chi
=\frac{|D_sY_\chi|^2}{2u^2}+K_0\rho_\chi-\lambda(\rho_\chi)_s.
\tag{3}$$

**逐点恒等式：**

$$\boxed{\mathcal R_\chi
=a_0\chi^2+a_1\chi\chi'+a_2\chi'^2
+\sum_{j=0}^2\beta_jJ_j,}\tag{4}$$

这里 $J_2$ 表示 $J_2^*$，并且

$$a_0=\frac{ke}2,\qquad a_1=-\frac{kQ}{2h},$$

$$\begin{aligned}
a_2={}&\frac{khz^3}4-\frac{(5k^2+1+\gamma^2/h^2)z^2}8
+\frac{k(k^2+1)z}{2h}-\frac{(k^2+1)^2}{8h^2}\\
&+\frac{\gamma z\nu}{4h}-\frac{k\gamma\nu}{4h^2}
+\frac{(k^2+1)\gamma^2}{8h^4},
\end{aligned}$$

$$\beta_j=K_0r_j-\lambda(r_j)_s.\tag{5}$$

所以 $a_0,a_1,a_2$ 对 xi 的次数分别不超过 1、2、3；每个 beta 的次数不超过 2。

这比仅在全周期积分后成立的关系更强。(4) 直接由 (2) 代入 (3) 得到：$D_sY$ 的 T、N、B 分量依次为

$$\frac{\nu}{2z^2}\chi',\quad
\frac h z\chi-\frac h2\chi',\quad
c\chi+\left(-\frac\gamma2+\frac{k_s}{2z}-\frac{k\nu}{2z^2}\right)\chi'.$$

按 $\chi^2,\chi\chi',\chi'^2,J_0,J_1,J_2^*$ 收集即为 (4)–(5)。其中原来周期分部积分产生的总 s 导数，已经由 (3) 的 $-\lambda\rho_s$ 逐点支付；没有再丢掉某个只在积分后为零的项。

## 3. 第三 ruling 的有理分母准确消失

对于一般二阶差 forcing $H_d$，记

$$\eta_0=\frac{(H_d)_{s\xi}-c\rho_\xi}{2u_\xi}-\frac{\rho_s}2,
\qquad W_s=\mathcal R_{H_d},\quad W(0,\xi)=0.$$

恢复中的 $\eta=kp+q$ 为

$$\eta=\eta_0-uW+\frac h2W_\xi.$$

对单个平方 forcing $(dY_\chi)^2$，直接计算得到

$$\boxed{\begin{aligned}
\eta_{0,\chi}={}&-\frac{\gamma e}{8h}\chi'^2
+\frac{\gamma Q}{8h^2}\chi'\chi''
-\frac{(\gamma z-h\nu)Q}{16h^2}\chi''^2\\
&-\frac12\sum_{j=0}^2(r_j)_sJ_j.
\end{aligned}}\tag{6}$$

差 forcing 取 f 式减 g 式即可。式 (6) 的所有 xi 系数都是多项式，最高次数 3。

可直接验证 (6)：$Y=P T+Q_B B$，其中
$P=-\chi'/(2z)$、$Q_B=h\chi/z-e\chi'/(2z)$；
$(dY^2)_{s\xi}=P_sP_\xi+(Q_B)_s(Q_B)_\xi$，
$2u_\xi\rho_\xi=P_\xi^2+(Q_B)_\xi^2$。代入 eta0 后，包含 $\chi^2$、$\chi\chi'$、$\chi\chi''$ 的系数全部取消；剩下三项局部导数及 (2) 尾系数的 s 导数正好为 (6)。

现取任意 profile phi，定义其规范第三 ruling 函数

$$K_\phi(s)=-2\int (Y_\phi)_u\cdot(Z_d)_u\,du.$$

由于 phi 在两端全平，分部积分没有端项。由

$$ (Y_\phi)_{uu}=\frac{z^4}{h^2}V_0\phi''',
\qquad V_0=-\frac{uT+wB}{2h},$$

以及 (12) 型二阶恢复，严格得到

$$\boxed{K_\phi(s)=\int\phi'''(\xi)
\left[eW-\frac Q{2h}W_\xi-\frac Q{h^2}\eta_0\right]d\xi.}\tag{7}$$

例如，直接恢复 $p,q$ 给

$$\frac{2z^2}{h}\,V_0\cdot Z_d
=eW-\frac Q{2h}W_\xi-\frac Q{h^2}\eta_0.$$

(7) 中不再有 $(\xi+\omega)^{-1}$ 等分母；不能在得到这一消去之前，凭直觉把平移依赖当成有限多项式。

## 4. 每个配平 packet 的二阶校正准确局部化

把 $(f_0,g_0)$ 共同平移 t，记 $f_t(\xi)=f_0(\xi-t)$、$g_t(\xi)=g_0(\xi-t)$。所有二阶量取两平方之差。

在该 packet 的右侧，三尾差都为零。在其左侧，三尾差分别等于三总矩差，而 (1) 及平移公式使它们也全为零。因此

$$\Delta J_0,\quad\Delta J_1,\quad\Delta J_2^*$$

均只支撑在本 packet 的联合包络内。由 (2)、(4)、(6)，rho、R、eta0 同样只支撑在此包络内。W 用同一 $s=0$ 零锚积分，因此 W 与 $W_\xi$ 也不向其他 packet 传播。恢复的 $Z_d$ 亦在此包络外为零。

这准确处理了尾积分的非局部性：结论依赖**每一个完整 packet 都已经三矩配平**。若只平移单个未配平 bump，其尾项一般不能如此局部化。

## 5. 平移参数的次数不超过六

在一条固定真实几何上，令 $K_{\phi,t}(s)$ 为平移 packet 的规范第三 ruling，$\phi=f_0$ 或 $g_0$。代换 $x=\xi-t$ 后，三尾差严格变换为

$$\Delta J_{0,t}(x+t)=\Delta J_0(x),$$

$$\Delta J_{1,t}(x+t)=\Delta J_1(x)+t\Delta J_0(x),$$

$$\Delta J_{2,t}^*(x+t)=\Delta J_2^*(x)
+2t\Delta J_1(x)+t^2\Delta J_0(x).\tag{8}$$

在固定 x 下，(4) 的局部三项平移次数至多 3；beta 项的系数至多 2，尾项至多 2，故完整 R 的 t 次数至多 4。对同一 s 区间积分不增加该次数，于是

$$W_t(s,x+t),\quad \partial_\xi W_t(s,x+t)$$

的 t 次数都至多 4。式 (6) 的局部项最高次数 3，尾项最高次数 2，故 eta0 的 t 次数至多 3。

在 (7) 中，e、Q 的 t 次数分别为 1、2；$\phi'''(x)$ 不含 t。因此积分前最高次数是 $2+4=6$。支撑局部化允许把 x 积分固定在原 packet 区间，故

$$\boxed{K_{\phi,t}(s)\text{ 是 t 的次数至多六的多项式。}}\tag{9}$$

其系数可以是 s 的任意真实函数；(9) 不要求常 k、常 h，也不只是常圈上的近似。只需所考虑的平移 packet 留在共同物理区间。所得多项式恒等式随后按代数延拓成立，无须让超出物理区间的 profile 具有几何意义。

## 6. 八个明确幅度准确消掉全部 s 的两条 ruling

选择八个互不交 packet，平移量为

$$t_j=t_*+jL,\qquad j=0,\ldots,7,$$

L 大于一个 packet 的包络宽度。取准确的实代数幅度

$$a_j=(-1)^j\binom7j^{1/3},$$

并定义

$$\boxed{f=\sum_{j=0}^7a_jf_0(\xi-t_j),\qquad
g=\sum_{j=0}^7a_jg_0(\xi-t_j).}\tag{10}$$

可先在原坐标取 $L=10,t_*=0$，再共同缩放整个构造至任意给定紧活动区间。原联合支撑在 $[-4.1,74.1]$ 内；例如以其中心 35 为中心，取小于活动宽度的 $1/80$ 的共同缩放，即有严格外 collar。

因为 packet 彼此不交，二次矩只按 $a_j^2$ 加权；每一 packet 的 f、g 已经三矩相等，所以全局三矩仍相等，且全局 f、g 的交叉项仍逐点为零。

根据 §4，规范二阶解准确分解为

$$Z_d=\sum_j a_j^2 Z_{d,t_j},$$

各项只支撑于自己的 packet。于是三阶 forcing 没有跨 packet 乘积，其两条 ruling 分别为

$$K_f(s)=\sum_{j=0}^7a_j^3 K_{f_0,t_j}(s),\qquad
K_g(s)=\sum_{j=0}^7a_j^3 K_{g_0,t_j}(s).\tag{11}$$

而 $a_j^3=(-1)^j\binom7j$。第七有限差分准确消去所有次数不超过六的多项式：

$$\sum_{j=0}^7(-1)^j\binom7j(t_*+jL)^m=0,
\qquad m=0,\ldots,6.$$

将 (9) 代入 (11)，对每个真实 s 立即得到

$$\boxed{K_f(s)=K_g(s)=0.}\tag{12}$$

因此这不是在有限 s 网格上配平，也不需要调整二阶齐次 gauge。

## 7. 完整三阶固定度量圆

四块倒行几何已经使两条三阶周期函数准确为零；(12) 又支付全部逐 ruling 条件。完整 range 定理因而给真实光滑、周期、外 collar 为零的 $W_f,W_g$：

$$\mathcal L_XW_f=-\mathcal S(Y_f,Z_d),\qquad
\mathcal L_XW_g=-\mathcal S(Y_g,Z_d).$$

令

$$Y_\theta=\cos\theta Y_f+\sin\theta Y_g,\quad
Z_\theta=\sin^2\theta Z_d,$$

$$W_\theta=\sin^2\theta(\cos\theta W_f+\sin\theta W_g).$$

则对同一个
$g_\varepsilon=(X+\varepsilon Y_f)^*e=g_X+\varepsilon^2(dY_f)^2$，

$$F^{[3]}_{\varepsilon,\theta}
=X+\varepsilon Y_\theta+\varepsilon^2Z_\theta+\varepsilon^3W_\theta$$

的准确误差为

$$\begin{aligned}
(F^{[3]}_{\varepsilon,\theta})^*e-g_\varepsilon
={}&\varepsilon^4\{(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)\}\\
&+\varepsilon^5\mathcal S(Z_\theta,W_\theta)
+\varepsilon^6(dW_\theta)^2.
\end{aligned}\tag{13}$$

在固定紧带及全部 theta 上，这给统一 $O(\varepsilon^4)$。$\theta=0,\pi$ 的高阶项都为零，仍接到两个准确等距端点 $X\pm\varepsilon Y_f$。这条有限 Taylor 路径本身不是精确有限等距族。

**局部化的边界。** 二阶 packet 解彼此不相交已在 §4 证明；第三阶 ruling 是跨 packet 积分相消，所以三阶 rho 与 $W_f,W_g$ 可能在 packet 间的空隙中非零。不能把二阶局部化未经证明沿用到四阶，也不能据此声称所有阶都能用同一有限差分消去。

## 8. 精确代数证书与下一方程

`scripts/literature_third_ruling_packet_certificate.py` 只进行 SymPy 精确有理代数与整数有限差分：核对 (4)、(6)、(7) 的三项差均恒为 0，并给权重

$$1,-7,21,-35,35,-21,7,-1$$

的 0 至 6 次离散矩全部为 0。它不替代上述支撑、平移次数、锚或完整 range 的证明。

本地已运行这一纯代数证书，输出
`notes/literature-third-ruling-packet-certificate-20261114.json`（984 字节），SHA256
`fcec25ed0ed7b813ea5f8ceb088fa39b83f630daf4ce7121740830a2d74f24fd`。

下一准确方程是

$$\mathcal L_X Z_{4,\theta}
=-\{(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)\}.$$

它属于倒行偶 forcing，周期障碍不由前述奇对称自动消失；ruling 与周期都须重新支付。即使继续得到任意有限阶，也仍须证明收敛或直接求固定参数的精确有限解。闭面、嵌入和题目要求的比例亦需独立构造。
