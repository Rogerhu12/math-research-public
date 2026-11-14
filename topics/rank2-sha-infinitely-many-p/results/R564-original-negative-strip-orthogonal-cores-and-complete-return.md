# R564 — 原负条带的三个正交完整核心及实际四伴随返回

日期：2026-11-14。**状态：已证明。**

R560 把同一个 native 行化为两个实际五变量条带。本篇完整支付
其中负条带的另一根整数 degree $14$ 轴和其真正 degree $42$
单位伴随。它们与原 carry 轴两两正交，三个 whole 核均为
$\beta$，不新增射线，不增加来源。

由此原负条带可以再准确返回一次原来源，保完整
$E/G/Y/W$ 变化、两个 Mellin 单位条件和常数 log 质量。
正条带继续保留；这里没有用一个条带的返回声称全中央非零。

## 1. 同一个原 n 无关行

全部规范、固定坏集、当前 $p\ge71$ 与原准确多项式沿用
[R560](R560-native-single-branch-and-seven-conditional-moments.md)。
特别

$$
\delta=1+2\omega,\quad\gamma=3+\omega,\quad\bar\gamma=2-\omega,
\quad\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad\kappa=p\lambda^2.
$$

本篇的 $D$ 始终是整数 degree $14$ 的 $F-C$，不是 R559/R563 的
$D_{12}=F-c$。原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$，置

$$
D_4=(1,\omega^2,-2\omega,0,0,0),\qquad
D=D_4+c+(2+3\omega)d_0,
$$
$$
X=c-D/14,\quad Z=d_0+(1+3\omega)D/14,\quad a=2+\omega.
\tag{1}
$$

令 $\mu_0=\mathcal P_C\rho_0$、$\mu_h=\mathcal P_Ch$，其中
$h=\eta+\rho_0/2$ 是 R557 的新第三来源。定义两个准确来源

$$
\nu_+=\tfrac32\mu_0-\mu_h=\mathcal P_C(\rho_0-\eta),\qquad
\nu_-=\tfrac32\mu_0+\mu_h=\mathcal P_C(2\rho_0+\eta).
\tag{2}
$$

它们未被另认成新的算术曲线。原两个实际条带是

$$
\mathcal B_\pm=\{Z\text{ unit},\ X\mp aZ\in p\mathcal O\}.
\tag{3}
$$

$\widehat P(D,E,G)$ 是 R536 原七行十列整逆给出的同一个准确
六次多项式，$\ell(Y,W)$ 是 R560 (8) 的两个独立单位指标对数差。
记

$$
J_+=\int_{E\text{ unit},\,\mathcal B_+}
 \widehat P(D,E,G)\ell(Y,W)\,d\nu_+,
$$
$$
J_-=\int_{E\text{ unit},\,\mathcal B_-}
 \widehat P(D,E,G)\ell(Y,W)\,d\nu_-.
\tag{4}
$$

R560 的完整结论正是

$$
\boxed{\mathcal N_n=\frac{\beta^n}{b\Omega^6}(J_++J_-),\qquad
h(\Phi_1-\Phi_2)=\frac{\mathcal N_n}{2\lambda},\quad n\ge1.}
\tag{5}
$$

(4) 的两个积分都在原六输入上。$D$ 已自由恢复，五变量表达也
可用 R560 的七个真实条件系数；本篇不更换那个条件源。

## 2. 两根原整数轴及真正正交框架

定义

$$
\boxed{
V=(-\omega^2,-\omega,2,0,-2\omega,-2\omega),
}
$$
$$
\boxed{
K_{42}=(-\omega^2,-\omega,2,0,-3+3\omega,3).
}
\tag{6}
$$

下标只标记范数；$K_{42}$ 不是 R563 的六度输出 $K$。
完整 Hermitian Gram 精确为

$$
\boxed{
N(D)=N(V)=14,\quad N(K_{42})=42,\qquad
D\perp V,\quad D\perp K_{42},\quad V\perp K_{42}.
}
\tag{7}
$$

三行都在同一个 $\operatorname{span}\{D_4,c,d_0\}$ 内。
相对这个原三坐标的矩阵为

$$
\begin{pmatrix}
1&1&2+3\omega\\
-\omega^2&-2\omega&-2\omega\\
-\omega^2&-3+3\omega&3
\end{pmatrix},
\qquad
\det=-14(1+3\omega),\quad N(\det)=2^2\,7^3.
\tag{8}
$$

故在当前处为同一个三维格的可逆变换，不遗失剩下三个真实输入。
由于 (7) 的所有范数是单位，任意完整正交补也构成整直和；
后文使用的投影都在原格上整。

令 $u^c=(-\omega c+(1-\omega)d_0)/2$。原负条带的真正深方向是

$$
u^c_\perp=u^c+\frac{2+3\omega}{14}D.
$$

直接在原六输入中有

$$
\boxed{14u^c_\perp=\gamma V.}
\tag{9}
$$

再对 $V$ 作真实正交投影，写
$r^\circ=r-\langle r,V\rangle V/14$。对 (1) 的 $Z$，

$$
\boxed{
Z^\circ=Z+\frac{\omega^2}{7}V=\frac{K_{42}}{14}.
}
\tag{10}
$$

因此 (3) 中的负条带准确等价于

$$
\boxed{
\mathcal B_-=\{V\in p\mathcal O,\ K_{42}\text{ unit}\}.
}
\tag{11}
$$

证明：$X+aZ$ 深与 $u^c_\perp$ 深等价，(9) 给 $V$ 深；
这时 $Z$ 与 $Z^\circ=K_{42}/14$ 模 $p$ 相同。
(11) 没有把原输入 $c,d_0$ 当成新的独立测度。

## 3. 三个 whole 核的中心、半特征和绝对符号

$D$ 的完整核已由 R531/R557 支付。对 (6)，原二输入矩阵
$\mathsf H$ 给

$$
V\mathsf H=(-\omega^2,-\omega,2,0,-\omega,-\gamma),
$$
$$
K_{42}\mathsf H=(-\omega^2,-\omega,2,0,6+3\omega,3+3\omega).
\tag{12}
$$

全为整数行。原 $V,V\mathsf H$ 的模二非零系数数分别为 $2,4$；
$K_{42},K_{42}\mathsf H$ 分别为 $4,4$。
非零 $\mathcal O_K/2$ 系数保 sigma 的标准奇半特征，
所以四行的完整半特征均为 standard even。

在当前射线，已经有

$$
g_\pi\equiv15\pmod{28},\qquad
g_\pi\equiv43\pmod{84}.
\tag{13}
$$

后一式由原 $g_\pi\equiv3\bmod4$ 及
$g_\pi\equiv1\bmod21$ 直接得到，没有新增模条件。
$15=1+14$、$43=1+42$ 与恒等在对应完整 Heisenberg 群上交织相同；
其中心分别满足

$$
(15^2-1)/14=16,\qquad (43^2-1)/42=44,
$$

均为偶整数。故整个标准 even 空间上的核是 scalar，
不是只在一条角型上线性对角化。

用真实非零锚

$$
\Theta(\gamma z)\in\mathcal S_{14},\qquad
\Theta(\delta\gamma z)\in\mathcal S_{42}
$$

绝对定标。它们分别由 Norm $7,21$ 的固定 CM 拉回得到，
与原普通 core 严格交换；R316/R533 已付原 $\Theta$ 的标量
$\beta$。因此两根新轴的整个核心都恰为 $\beta$。

还需支付来源投影 $\mathcal P_C$。纯 $C$ 旋转保持
$c,d_0$，把 (6) 的公共首四系数循环成三行

$$
(-\omega^2,-\omega,2,0),\qquad
(1,-\omega,2+\omega,-\omega),\qquad
(2+\omega,-\omega,1,1).
\tag{14}
$$

每行仍为整数，范数保持。对应 $V_j,V_j\mathsf H$ 的奇系数数为
$(2,4),(4,6),(4,6)$；$K_j,K_j\mathsf H$ 为
$(4,4),(6,6),(6,6)$，全是 standard even。
同一 (13) 和同一锚因而支付每个共轭轴的完整 scalar 核。
再用 R560 §3 的真实共轭论证，得到对
$\mu_0,\mu_h,\nu_+,\nu_-$ 的完整三轴身份：

$$
\boxed{
\mu|_{\{D\in p^r,V\in p^s,K_{42}\in p^t\}}
=\beta^{r+s+t}
(P_{D,\kappa^r}P_{V,\kappa^s}P_{K_{42},\kappa^t})_*\mu
}
\tag{15}
$$

对所有 $r,s,t\ge0$ 成立，保三个剩余伴随。
正交性支付实际矩阵交换；没有把不正交的轴当成矩形。

## 4. 所有原观察的准确移动

对任意原行 $r$ 记
$a_r=\langle r,V\rangle/14$，则

$$
r\circ P_{V,t}=r^\circ+t a_rV.
\tag{16}
$$

当前需要的全部系数为：

| 原行 $r$ | $a_r$ |
|---|---:|
| $D$ | $0$ |
| $E$ | $\omega$ |
| $G$ | $2+5\omega$ |
| $Y$ | $(12+11\omega)/14$ |
| $W$ | $(8+19\omega)/14$ |
| $W'$ | $(11+13\omega)/7$ |
| $X,Z$ | $-\omega^2/7$ |
| $L$ | $(-1+2\omega)/7$ |
| $C$ | $\omega/14$ |

这些都由同一个原六行 Gram 得出，脚本逐项保存精确值。
尤其 $V$ 不保持 $Y,W,E,G$，不能沿用 R560 中只缩放 $D$
时的“不移动观察”结论。

(7)、(16) 保 $D$ 自由且保 $K_{42}$。在 $V$ 深一层时，原
$E$ 单位条件变成 $E^\circ$ 单位；两个 Mellin 单位条件
分别变成 $Y^\circ,W^\circ$ 为单位，但各自 log 仍使用
$Y^\circ+\kappa a_YV$、$W^\circ+\kappa a_WV$。

## 5. 整个负条带的准确返回

取固定四维补空间

$$
\mathcal Q=\{r:r\perp D,V\}.
$$

$E^\circ,G^\circ,Y^\circ,W^\circ,K_{42}$ 都属于这个同一空间；
它们之间的线性联系按原行保留，不被当成五个独立输入。
设

$$
\mathcal A=\{E^\circ\text{ unit},\ K_{42}\text{ unit}\}.
$$

对 $t\in p\mathcal O$，定义完整测试

$$
\ell_t=(p-1)\left[
 \mathbf1_{Y^\circ\text{ unit}}\log\langle Y^\circ+t a_YV\rangle
-\mathbf1_{W^\circ\text{ unit}}\log\langle W^\circ+t a_WV\rangle
\right],
$$
$$
\mathcal F_-(t)=
\int_{\mathcal A}
 \widehat P\bigl(D,E^\circ+\omega tV,
                    G^\circ+(2+5\omega)tV\bigr)\,\ell_t\,d\nu_- .
\tag{17}
$$

不含单位指标的 log 项均按零处理。(17) 是原六输入上的积分，
$D,V$ 两轴完整自由，四个真实伴随全部保留。

由 (11)、(15) 的一次 $V$ 核，严格有

$$
\boxed{
J_-=\beta\,\mathcal F_-(\kappa),\qquad
\mathcal N_n=\frac{\beta^n}{b\Omega^6}
 \left[J_++\beta\,\mathcal F_-(\kappa)\right].
}
\tag{18}
$$

这是整个原负条带，不是它的某个深子域。
$\widehat P$ 仍为原补偿多项式，(16) 中的全部移动均已进入 (17)。
$K_{42}$ 单位来自真正的 $Z$ 单位事件；本篇没有删除它，
也没有把 $E^\circ$ 单位并入一个不同的独立单位轴。

## 6. 首两行及正确的全尾

(17) 在 $t\in p\mathcal O$ 有均匀收敛展开
$\mathcal F_-(t)=\sum_{r\ge0}F_rt^r$。
记 $P^\circ=\widehat P(D,E^\circ,G^\circ)$，
$g_V=2+5\omega$ 和
$\ell_0=\ell(Y^\circ,W^\circ)$，则常数项准确为

$$
\boxed{F_0=\int_{\mathcal A}P^\circ\ell_0\,d\nu_-\in p\mathcal O.}
\tag{19}
$$

它包含真实条件质量与原 log，不预设为零。
第一项为

$$
\boxed{
\begin{aligned}
F_1=\int_{\mathcal A} V\bigg[
 &\{\omega\partial_E\widehat P+g_V\partial_G\widehat P\}
       (D,E^\circ,G^\circ)\,\ell_0\\
 &+(p-1)P^\circ
 \left\{\mathbf1_{Y^\circ\text{ unit}}\frac{a_Y}{Y^\circ}
       -\mathbf1_{W^\circ\text{ unit}}\frac{a_W}{W^\circ}\right\}
 \bigg]\,d\nu_- .
\end{aligned}}
\tag{20}
$$

所有分母只在其单位域中取逆。
第一行属于 $p\mathcal O$；第二行一般只在 $\mathcal O$ 中。
因此不能把移动 log 的一阶项再免费乘一个 $p$。

$\widehat P$ 的系数整且次数六，全部源有界整；log 的第 $j$
阶只带 $1/j$。故

$$
v_p(F_r)\ge-\lfloor\log_pr\rfloor\quad(r\ge1).
\tag{21}
$$

对 $r\ge2$，$r-\lfloor\log_pr\rfloor\ge2$，从而

$$
\boxed{
J_-=\beta\{F_0+\kappa F_1\}+p^2\mathcal O .
}
\tag{22}
$$

常数项与线性项都可能处在同一个 $p$ 阶，必须一起保留。
(20) 中所需的 $D$ 条件矩仍准确由 R560 (25)–(26) 的七条源读取；
其第六矩质量校正 $-672b\Omega^6\Lambda_0$ 没有消失。

## 7. 完整剩余范围

(18) 中的 $J_+$ 是原正条带，仍需完整处理；它没有被 (15)
或 (22) 覆盖。即使再对某个轴使用整单位逆，也必须同时运输
(16) 的观察与 (17) 的全部紧开事件。

本篇没有证明 $F_0+\kappa F_1$ 非零，也没有把 R562 的固定
四单位测试换成这里的 $\widehat P\ell_t$。
原 $S/T$ 中央零只通过已付完整算术行使用，不能给
$\nu_-$ 的新观察或任意单独条件源赋零。
原无穷素数的主目标仍未完成。

配套脚本计算整个原整数行、三轴 Gram/行列式、所有 $C$ 共轭
及原 $\mathsf H$ 下半特征、(9)–(10) 与全部物理移动系数。
whole 核的证明、完整条带等价以及均匀级数证明在本文，
不依赖有限素数扫描。
