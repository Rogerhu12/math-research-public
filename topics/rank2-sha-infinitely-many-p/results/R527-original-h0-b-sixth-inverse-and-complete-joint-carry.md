# R527 — H0/B 六次整逆、完整四输出返回与同源非零管

日期：2026-11-14。**状态：已证明。** R522 的同一个正六次测试可以与 R523 的真实隐藏 sigma 核配合。所得有限整逆准确返回整个
$(Y,W,W',D_H)$ 联合来源，故两条原 $S/T$ 算术线使用同一个测试，而不只是各自找到一条边际。

本篇保偶数 $A$ 深度的实际逆域、原全部四个五 sigma 伴随，以及 carry 的完整补域。新的局部质量并不为零；其准确式也在下文支付。主目标仍未完成。

## 1. 同一个原六输入和六次全函数身份

沿用
$$
\boldsymbol\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0),\quad
\rho_0=-\nu_\sigma^{\otimes6}/84,\quad
h=\omega^2\mathcal T_*\rho_0,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1.
$$
保 R523 的完整固定 ray，包含 $\pi_0\equiv1\bmod31,1013$，
但本篇的非零门槛在 §6 另行显示。

R522 的原整轴是
$$
\boxed{H_0=\xi_1-\xi_3+x,\qquad N(H_0)=3.}
\tag{1}
$$
它与 $Y,W,W'$ 全正交，且
$H_0\mathcal T=\omega^2H_0$。
在原全部 $W$ 四挠来源中，第一轴都是同一个标准 odd
$\mathcal S_3$；$H_0\perp W$ 使该方向没有额外 flat twist。

该空间的偶子空间只有一维，真实规范基为
$$
B_3=-y_{\rm wp}\sigma^3
=1+\frac{3b}{10}z^6+O(z^{12}).
$$
例如用 $x=z^{-2}-bz^4/7+\cdots$、$y_{\rm wp}=x'/2$ 和
$\sigma=z+bz^7/210+\cdots$，第六系数准确是
$2b/7+3b/210=3b/10$。
所以在保任意另外五个完整输出时，
$$
\boxed{\text{第六 }H_0\text{ 矩}
 =216b\Omega^6\cdot\text{第零 }H_0\text{ 矩}.}
\tag{2}
$$
这是 R522 的整个来源身份；不是只在零点核了两个数值。
它对原四态均成立。以下用无 $H_0$ 单位指示的 (2)，
其规范与带额外 $1+\lambda\kappa^6$ 分母的单位版本区分开。

## 2. 同一隐藏 B、正交 E0 及真正四输出

取 R523 已付一层核心 $\beta$ 的同一个
$$
B=103C_H,\qquad N(B)=3193.
$$
定义
$$
\boxed{
\eta=\frac{1-\omega}{103},\qquad
E_0=H_0-\eta B=H_0-(1-\omega)C_H.
}
\tag{3}
$$
精确计算给
$$
E_0\perp B,D_H,\qquad N(E_0)=216/103.
\tag{4}
$$
它与根侧第三伴随的规范关系是
$$
E_*=\frac{-1+4\delta}{7}E_0,\qquad
N\!\left(\frac{-1+4\delta}{7}\right)=1.
\tag{5}
$$
本篇不需要为 $E_0$ 新猜一个一层 scalar。

置
$$
\boxed{\Pi_4=(Y,W,W',D_H).}
\tag{6}
$$
这四个实际行均与 $H_0,B,E_0$ 正交。
其完整 Gram 行列式为
$$
\boxed{\det\operatorname{Gram}(\Pi_4)
=38997504=2^9\,3^3\,7\,13\,31.}
\tag{7}
$$
故 $(\Pi_4,E_0,B)$ 是当前处真正的完整六输入框架。
附证书保全部原行及 Gram；没有把不同来源的四条边际拼在一起。

## 3. 一个六次整逆恢复整个四输出

定义
$$
\boxed{
\widehat P_p=
\frac1{216b\Omega^6}
 \sum_{j=0}^6\binom6j
 \frac{\eta^jE_0^{6-j}B^j}{1+\lambda\kappa^j}.
}
\tag{8}
$$
R523 已付所有分母为单位，包括 $j=0$ 的 $1+\lambda$。
$B$ 核 $\beta$ 对每个真实 $B^j$ 矩的单位限制给因子
$1+\lambda\kappa^j$，而 $E_0$ 和 $\Pi_4$ 全固定。

因此对任意依赖完整 $\Pi_4$ 的连续测试，先逐 $B$ 次数取消
(8) 的分母，再用 $H_0=E_0+\eta B$ 和 (2)，准确得到
$$
\boxed{
(\Pi_4)_*\{{\bf1}_{B\ {\rm unit}}\widehat P_p\,d\nu_\mu\}
=(\Pi_4)_*d\nu_\mu
}
\tag{9}
$$
对原任意四态 $\mu$ 成立。
第一个步骤保所有 $B$ 正交输出；第二个步骤保所有 $H_0$
正交输出，所以 (6) 的四个输出确实同时保留。

这包含真正的 $(Y,W,W')$ 联合和额外 $D_H$。
第一 $Y/W$ 的已付 canonical CM 操作与所忘掉的两个正交方向
交换，故原来源条件可以在这个联合身份中继续使用，保它们的
全部周期和纤维规范。含混合管的测试仍须逐支运输；
(9) 不把投影后的支改回未投影的旧事件。

特别，原 $\rho_0$ 的 $Y$ 来源为 $S$、$W$ 来源为 $6\delta T$；
$h$ 的相应来源为
$$
Y_*h=\omega^2\nu_S,\qquad W_*h=0,\qquad
(W')_*h=-6\delta\omega\,\nu_T.
\tag{10}
$$
最后一式由 $W'=W\mathcal T$、$h=\omega^2\mathcal T_*\rho_0$、
$\mathcal T^2_*\rho_0=-\omega^2(\rho_0+h)$ 直接得到。
这些整条算术来源因此使用同一个 (8)。

## 4. 同源 carry 的完整联合返回与全部移权

保 R523 的
$$
D=31C-B,\qquad A=D+72C=103C_4,\qquad
\Gamma_r=\{A\in p^r,\ C,D\text{ 均为单位}\}
        =\{A\in p^r,\ B\text{ 单位}\}.
\tag{11}
$$
$A$ 与旧 $W,B,D_H$ 正交。它的实际物理缩放为
$$
P_{A,r}=I+\frac{\kappa^r-1}{7416}\bar A^{\,t}A.
\tag{12}
$$
对 $h$，R523 已付所有偶深来源返回；对原全部四态，
R519 已付八的倍数深度返回。

在真实像 $A\in p^r$ 上，记
$$
\Pi_4^{(r)}=\Pi_4\circ P_{A,r}^{-1},\qquad
E_r=E_0\circ P_{A,r}^{-1}.
$$
全部非零变化准确是
$$
\boxed{
\begin{aligned}
Y_r&=Y+(\kappa^{-r}-1)\frac{-1+3\delta}{144}A,\\
W_r&=W,\qquad (D_H)_r=D_H,\\
W'_r&=W'+(\kappa^{-r}-1)\frac{-5+\delta}{144}A,\\
E_r&=E_0+(\kappa^{-r}-1)\frac{113+31\delta}{14832}A.
\end{aligned}}
\tag{13}
$$
$B$ 不变。把 (8) 中 $E_0$ 换成 $E_r$ 得 $\widehat P_{p,r}$。
(9) 和真实 $A$ 核给
$$
\boxed{
(\Pi_4^{(r)})_*
 \{{\bf1}_{\Gamma_r}\widehat P_{p,r}\,d\nu_\mu\}
=\lambda^r(\Pi_4)_*d\nu_\mu.
}
\tag{14}
$$
这里 $r$ 为正偶数时可取 $\mu=h$；$8\mid r$ 时可取原任意四态。
所有逆尺度只用于其显示的实际深域。

例如在 $h$ 上取第一单位 Mellin 权，得到
$$
\boxed{
\int_{\Gamma_r,\ Y_r\ {\rm unit}}
 \langle Y_r\rangle^{du}\widehat P_{p,r}\,dh
=\lambda^r\omega^2J_S(u),\qquad 2\mid r.
}
\tag{15}
$$
同一个 (14) 也给原 $T$ 行，但其真实 $W'_r$ 必须按 (13) 移动。
旧 $W$ 以及 carry、权中的全部 $W$ 伴随均保持；
不能据此把 $Y_r$ 误认为固定。

## 5. 同一个原五深小管上的完整第五阶

仍用 R523 的真实网格
$$
\mathcal D_n^h
=\{\text{五个原 sigma 输入深 }n,\ x\text{ 单位}\}
=\{D,\mathbf R\in p^n,\ C\text{ 单位}\},
\qquad n\ge1.
\tag{16}
$$
$\mathbf R$ 是该篇保留的四个实际五 sigma 伴随。
该域上 $Y,H_0,B,A$ 全为单位。

由 (8)，在固定系数整的普通处，
$$
\boxed{
\widehat P_p\equiv
 \frac{H_0^6-\lambda E_0^6/(1+\lambda)}
      {216b\Omega^6}\pmod p.
}
\tag{17}
$$
这里确实保留了第零 $B$ 次数的校正。

回到 $\mathcal T$ 之前，$H_0\mathcal T=\omega^2H_0$，
故其六次方不变。对于第二项，准确有
$$
(E_0\mathcal T)/\omega^2
=\sum_{i=1}^5\ell_i\xi_i+qx,
\tag{18}
$$
$$
\boxed{
\ell=(1,0,-1,0,0)+\frac{\delta}{103}
 (30\omega,21\omega^2\delta,-\omega,1,-\omega^2\gamma),
\quad
q=\frac{72+31\omega}{103}.
}
\tag{19}
$$
第一 $Y$ 仍为 $Z+\bar\gamma x$，其中
$\boldsymbol z=(\delta,2\delta,\gamma,1,2)$。

为给完整可核查的第五阶，写
$$
\prod_{i=1}^5(\ell_i+z_i s)=\sum_{a=0}^5P_as^a .
$$
log 的全部正次数碰撞给
$$
\boxed{
\alpha_E=
-\frac1{84\cdot216}
 \sum_{a=1}^5\frac{(-1)^{a-1}}a
 \binom6{5-a}q^{1+a}\bar\gamma^{-a}
 a!(5-a)!\,P_a .
}
\tag{20}
$$
log 常数项和加权 sigma 矩保留在完整积分中；
仅在模 $p$ 的单位判断时使用它们属于 $p\mathcal O$。

对 $H_0$ 用同一式（$\ell=(1,0,-1,0,0),q=1$），精确返回
R522 的
$$
\boxed{\alpha_H=\frac{-3221+5000\omega}{27\cdot7^6}.}
\tag{21}
$$
本次固定新系数为
$$
\boxed{
\alpha_E=
\frac{1917260883436470-4830920686898683\delta}
     {30343476665017509336}.
}
\tag{22}
$$
附脚本在特征零严格核 (20)–(22)。

所以新解析积分的完整单位首项满足
$$
\boxed{
[T^5]\widehat{\mathcal A}_p
\equiv\frac{\omega^2d}{b}
 \frac{\alpha_H+\lambda(\alpha_H-\alpha_E)}{1+\lambda}
 \pmod p.
}
\tag{23}
$$

## 6. 原 1013 ray 已足以支付单位

置
$$
D_*=30343476665017509336,
$$
$$
\begin{aligned}
u=D_*\alpha_H
 &=-54649385507539272+23881045930580000\delta,\\
v=D_*(\alpha_H-\alpha_E)
 &=-56566646390975742+28711966617478683\delta.
\end{aligned}
\tag{24}
$$
其完整整数规范为
$$
\begin{aligned}
Nu&=4697468400567058148428961822289984,\\
Nv&=5672916565051319793429134710694031,\\
\operatorname{Tr}(u\bar v)
 &=10296695692273905418894137885519648.
\end{aligned}
$$
沿用 R518、R523 的同一个 Norm–Trace 证明：
若 $p>(Nu+Nv+1)^2$ 而 $u\bar\pi_0-v$ 非单位，
严格迫使 $\operatorname{Tr}(u\bar v\bar\pi_0)=Nv$。
本篇准确的模数表为
$$
\boxed{
\begin{array}{c|ccccc}
\bmod1013&D_*&Nu&Nv&\operatorname{Tr}(u\bar v)&
 \operatorname{Tr}(u\bar v)-Nv\\ \hline
&781&502&530&861&331 .
\end{array}}
\tag{25}
$$
既有 $\pi_0\equiv1\bmod1013$ 排除该迹等式，故 (23) 是单位。
本篇使用的固定门槛准确为
$$
\boxed{
p>
107544884335123685847248088177328787639666998459901300459033311488256.
}
\tag{26}
$$
加上原固定坏素数和 (24) 的分母例外即可；没有新增随深度变化的
坏集，也不需要为本六次测试沿用 R523 三十六次测试的更大门槛。

五个原 sigma 使低于第五阶全部消失。
测试总次数只有六且所有系数整，故高项仍满足
$v_p([T^j]\widehat{\mathcal A}_p)\ge-\lfloor\log_pj\rfloor$。
由同一个普通输入核，得到
$$
\boxed{
v_p\!\left(
 \int_{\mathcal D_n^h}d\log\langle Y\rangle\widehat P_p\,dh
 \right)=5n,\qquad n\ge1.
}
\tag{27}
$$
原完整 log 积分没有用有限 jet 代替；
这里只由已付单位首项和全尾界确定其非零赋值。

## 7. 新的局部质量必须保留

(8) 改变了原无权六次测试的局部质量，不能沿用 R522 的零质量。
给一个完整短公式。令六个变量按五个原输入再加 $x$ 排列。
设 $e_i$ 为 (18) 线性式的六个系数，
$f_i$ 为 $(\eta B\mathcal T)/\omega^2$ 的六个系数。
于是
$$
(e_i+f_i)_{i=1}^6=(1,0,-1,0,0,1).
$$
定义
$$
\prod_{i=1}^6(e_i+f_i s)=\sum_{j=0}^6c_js^j .
$$
精确有
$$
\boxed{
\sum_{j=0}^6c_j=0,\qquad
c_0=\frac{-154355922+75034701\delta}{103^6}\ne0.
}
\tag{28}
$$
附 JSON 给全部七个 $c_j$，且
$N(103^6c_0)=40716369718948287$。

因为测试次数只有六，五个 sigma 的正次数总和只能为五，
所以原小管质量恰有以下全式，无隐藏高尾：
$$
\boxed{
\int_{\mathcal D_n^h}\widehat P_p\,dh
=-\frac{5\omega^2}{126b}\,
 \beta^{5n}\kappa^{5n}(1+\lambda\kappa)
 \sum_{j=0}^6\frac{c_j}{1+\lambda\kappa^j}.
}
\tag{29}
$$
模 $p$ 的和为 $-\lambda c_0/(1+\lambda)$。
在 (26) 下它是单位，因此这条局部质量的赋值同样恰为 $5n$。
完整 (9) 或 (14) 的总质量身份保持，但小管与补域的质量分别
非零；后续若产生 log 缩放项，两部分必须同时保留。

## 8. 同一个 carry 内的非零真实像和完整补域

对正偶数 $r$ 置
$$
\mathcal D_{n,r}^h=P_{A,r}\mathcal D_n^h .
$$
使用 R523 的同一个完整框架，其全部真实条件为
$$
\boxed{
A/\kappa^r\in\mathcal O,\quad B\text{ 单位},\quad
\mathbf R\in(p^n)^4,\quad
31A/\kappa^r-72B\in p^n.
}
\tag{30}
$$
这不是只保两个输出的替代事件。
它自动使 $A/\kappa^r$ 为单位，故属于同一 $\Gamma_r$，且
$A$ 的深度准确为 $r$。原旧 $W$ 深度 $n$ 也保持。

按 (13) 运输整个四输出和测试，(14)、(27) 给
$$
\boxed{
v_p\!\left(
 \int_{\mathcal D_{n,r}^h}d\log\langle Y_r\rangle
                      \widehat P_{p,r}\,dh
 \right)=5n .
}
\tag{31}
$$
局部质量同样按 $\lambda^r$ 缩放，仍为 (29) 的真实非零值乘单位。

然而 (15) 的已知算术中央还含完整补域
$$
\boxed{
\{\Gamma_r,\ Y_r\text{ 单位}\}\setminus\mathcal D_{n,r}^h .
}
\tag{32}
$$
若 $J'_S(0)=0$，这个补域准确补偿 (31)。
$(W')_*h$ 的原 $T$ 行也在同一个 (14) 中，但必须保
$W'_r$ 的实际不同单位管及其补域。
共享的正测试和完整联合身份，使这两条线可以在同一来源中比较；
它们没有使 (32) 自动消失。

## 证书与依赖

- [六次整逆、完整四输出及第五阶证书](../scripts/check-r527-h0-b-joint-carry-and-nonzero-pipe.mjs)；
  [全部精确数据与七个质量系数](../scripts/check-r527-h0-b-joint-carry-and-nonzero-pipe.json)。
  同一 BigInt/CM 函数已在 V8 执行，核了所有原行、正交块、(13)、
  两个首项、整个 Norm–Trace 证书和完整局部质量。
- [R522：同一个 degree3 偶来源与共同 S/T 正测试](R522-common-degree3-even-factor-and-same-st-positive-test.md)。
- [R523：隐藏 B 核、独立 sigma carry 与实际原输入](R523-original-hidden-sigma-core-and-same-source-c-carry.md)。
- [R519：全部原四态的 C4 whole 八层返回](R519-original-c4-eighth-core-and-complete-b0-transport.md)。
- [R518：固定射线的 Norm–Trace 引理](R518-original-e-unit-inverse-and-same-source-arithmetic-carry.md)。

本篇的新结论是 (9)、(14) 的整个四输出联合返回及同一原输入
上的 (27)、(29)、(31)。它没有为新增来源或任意受限混合域另赋
中央零；本课题的固定曲线无穷素数结论仍未闭合。
