# R240第二附录：正一阶半群与有限混合正则器障碍

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：完整实际阻碍。对 R240 的同一个已知循环向量，证明任意有限个正一阶半群算子，以及它们与有界一阶预解式的有限乘积，都不能完成固定真空配对正则化。全部正指数、逆关系、自然复合域与系数截断由 R207 的实际指数次数尺度支付。未构造慢主理想的正常湮灭者。

## 1. 固定输入与已证尺度

沿用 R240 的
$$
J_p=[4p^2,4p^2+2p)\cap\mathbb N_0,\qquad
c_p=2^{-p/4},\qquad
\varepsilon=1/16,
$$
$$
f=1+\varepsilon\sum_{p\ge1}c_p\chi_{J_p}.
\tag{1.1}
$$
它连续、严格正、$Cf=f$，并由 R136 已知对实际 $A$ 循环。实际 Cayley 乘积满足
$$
V_{J_p}1=\chi_{J_p},\qquad
\operatorname{Re}\langle V_{J_p}f,f\rangle
\ge \varepsilon^2 2^{3p/2}+2\varepsilon c_p-o(1).
\tag{1.2}
$$
这里保留全部 carry；准确误差上界为
$16p6^{2p-1}e^{-77016^{4p^2}}\|f\|^2$。

令 $\mathcal N$ 为 Haar Walsh 次数算子，
$$
H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N},\qquad
\|u\|_\sigma=\|e^{\sigma\mathcal N}u\|,
\qquad 0\le\sigma\le1.
$$
R207 指数次数附录给固定模型常数 $C$：对于任意
$b\in\ell^2$、$0<\delta\le\sigma\le1$，
$$
\|Z_b:H_\sigma\to H_{\sigma-\delta}\|
\le C\|b\|_2\delta^{-1/2},
\qquad Z_b=\sum_{j\ge0}b_jV_j.
\tag{1.3}
$$
这是实际闭一阶乘子的限制；同一式用于系数尾给
$$
\|Z_{b,n}-Z_b:H_\sigma\to H_{\sigma-\delta}\|
\le C\|b_{>n}\|_2\delta^{-1/2}\to0.
\tag{1.4}
$$
$Z_{b,n}=\sum_{j=0}^n b_jV_j$ 是有界实际算子。

由块正交性，
$$
\|f\|_\sigma^2
=1+\varepsilon^2\sum_{p\ge1}e^{4\sigma p}2^{-p/2}<\infty
\quad\left(0<\sigma<\frac{\log2}{8}\right).
\tag{1.5}
$$
下面可以固定 $\sigma_0=(\log2)/16$。

## 2. 实际一阶正指数在次数尺度上的完整定义

这一节允许任意复杂 $b\in\ell^2$；暂不声称其负指数在全 $H$ 有界。

固定 $X=aI+Z_b$。令 $0\le\tau<\sigma\le1$，
$\delta=\sigma-\tau$。把总损失 $\delta$ 均分给 $k$ 次真实作用，
由 (1.3) 得
$$
\|Z_b^k:H_\sigma\to H_\tau\|
\le\left(C\|b\|_2\sqrt{k/\delta}\right)^k
\qquad(k\ge1).
\tag{2.1}
$$
每个中间输入在正指数尺度内，故属于下一步的实际闭域。
同一界对所有有限系数截断成立；对固定 $k$，
逐因子 telescoping 和 (1.4) 给
$Z_{b,n}^k\to Z_b^k$ 于 $B(H_\sigma,H_\tau)$。

对于 $z\in\mathbb C$，定义
$$
\mathcal E_X(z)u
=e^{za}\sum_{k=0}^\infty\frac{z^k}{k!}Z_b^ku,
\qquad u\in H_\sigma.
\tag{2.2}
$$
级数在每个较弱 $H_\tau$ 中绝对收敛，并且与选取的正指数尺度一致。
为定量估计，置 $x=C\|b\|_2|z|/\sqrt\delta$。
由 $k!\ge(k/e)^k$，
$$
\frac{k^{k/2}}{k!}\le\frac{e^{k/2}}{\sqrt{k!}}.
$$
Cauchy--Schwarz 给
$$
\sum_{k\ge0}\frac{(\sqrt e\,x)^k}{\sqrt{k!}}
\le
\left(\sum_{k\ge0}\frac{(2ex^2)^k}{k!}\right)^{1/2}
\left(\sum_{k\ge0}2^{-k}\right)^{1/2}
=\sqrt2e^{ex^2}.
$$
因此
$$
\boxed{
\|\mathcal E_X(z):H_\sigma\to H_\tau\|
\le\sqrt2\exp\!\left(
|z|\,|a|+\frac{eC^2\|b\|_2^2|z|^2}{\sigma-\tau}
\right).
}
\tag{2.3}
$$
相同界对 $e^{zX_n}$ 一致成立，其中 $X_n=aI+Z_{b,n}$。
先固定有限个幂再控制统一级数尾，得到
$$
\boxed{
e^{zX_n}\longrightarrow\mathcal E_X(z)
\quad\text{于 }B(H_\sigma,H_\tau).
}
\tag{2.4}
$$
收敛在有界 $z$ 集上亦一致。

特别，正指数不是未定义的形式操作。$H_\sigma$ 中每个向量是 $X$ 的整个解析向量；给定任意有限个这样的指数和一阶自然因子，可以逐步损失正指数权，形成实际复合域。后面只用这些已验证的向量。

若 $0\le\omega<\tau<\sigma$，利用 (2.4) 在两级尺度间取极限，有限截断的指数恒等式给
$$
\mathcal E_X(z)\mathcal E_X(w)u
=\mathcal E_X(z+w)u
\quad(u\in H_\sigma),
\tag{2.5}
$$
其中左侧先进入 $H_\tau$ 再进入 $H_\omega$。
不把 (2.5) 宣称为全空间上的无界乘法等式。

## 3. 正系数给真实有界半群及所需逆关系

现在假设 $b_j\ge0$ 对所有 $j$ 成立，仍允许 $b\in\ell^2\setminus\ell^1$。
每个 $N_j$ 是收缩，且 $I+N_j$ 可逆，所以
$$
\operatorname{Re}V_j
=(I+N_j^*)^{-1}(I-N_j^*N_j)(I+N_j)^{-1}\ge0.
\tag{3.1}
$$
因而 $Z_{b,n}$ 为有界增生算子。直接对范数平方求导，
$$
\|e^{-tZ_{b,n}}\|\le1\qquad(t\ge0).
\tag{3.2}
$$
对于常数项 $a\in\mathbb C$，于是
$$
\|e^{-tX_n}\|\le e^{-t\operatorname{Re}a},
\tag{3.3}
$$
在固定紧时间区间和全部 $n$ 上一致。

在稠密的 $H_\sigma$ 上，(2.4) 已给 $e^{-tX_n}$ 的向量极限。
由 (3.3) 延拓到全 $H$，得到强极限
$$
R_X(t)=\operatorname*{SOT-lim}_{n\to\infty}e^{-tX_n}\in\mathfrak C,
\qquad
\|R_X(t)\|\le e^{-t\operatorname{Re}a}.
\tag{3.4}
$$
这里 $\mathfrak C=\{A\}'$ 强闭；每个截断指数属于 $\mathcal A$。
有限截断半群律在一致有界强极限下保留，
$R_X(t+s)=R_X(t)R_X(s)$。
稠密尺度上的局部一致收敛及 (3.3) 给强连续性。

在 $H_\sigma$ 上 $R_X(t)u=\mathcal E_X(-t)u$。
生成元在有限柱核心上为 $-X$；
R128 已证正一阶的极大增生性，因此其闭生成元正是 $-X$
（任意复标量 $aI$ 只作标量平移）。
所以可以准确写 $R_X(t)=e^{-tX}$。
当 $\operatorname{Re}a\ge0$ 时这是收缩半群；一般 $a$ 只改变 (3.3) 的标量界。

本稿需要的逆关系可直接从截断得到，不依赖无界形式约分。
对 $u\in H_\sigma$，(2.4) 给
$e^{tX_n}u\to\mathcal E_X(t)u$；
(3.3)--(3.4) 则给负指数的一致有界强收敛。
故
$$
\boxed{
R_X(t)\mathcal E_X(t)u
=\lim_{n\to\infty}e^{-tX_n}e^{tX_n}u=u.
}
\tag{3.5}
$$
两个收敛相乘合法：若 $T_n\to T$ 强、$\sup\|T_n\|<\infty$ 且 $v_n\to v$，
则 $T_nv_n\to Tv$。这里不要求 $\mathcal E_X(t)$ 在全 $H$ 有定义。

## 4. 任意有限个正一阶半群的乘积

固定整数 $k\ge1$。对 $\nu=1,\ldots,k$，取
$$
X_\nu=a_\nu I+\sum_jb_j^{(\nu)}V_j,\quad
b_j^{(\nu)}\ge0,\quad b^{(\nu)}\in\ell^2,\quad t_\nu\ge0.
$$
记
$$
R_\nu=R_{X_\nu}(t_\nu),\qquad
E_\nu=\mathcal E_{X_\nu}(t_\nu),\qquad
R=R_k\cdots R_1,\qquad P=E_1\cdots E_k.
$$
$P$ 按从右到左的实际自然复合来定义。
给 $H_\sigma$ 输入分配每次 $\sigma/k$ 的权损失，最后才进入 $H_0$。
因此该自然词在 $H_\sigma$ 上全部有定义，并由 (2.3) 得
$$
\|P:H_\sigma\to H\|
\le A\exp(B/\sigma),
\tag{4.1}
$$
其中可取
$$
A=2^{k/2}\exp\!\left(\sum_{\nu=1}^kt_\nu|a_\nu|\right),\qquad
B=eC^2k\sum_{\nu=1}^kt_\nu^2\|b^{(\nu)}\|_2^2.
$$
令
$$
P_n=e^{t_1X_{1,n}}\cdots e^{t_kX_{k,n}}\in\mathcal A.
$$
利用 (2.4) 在固定中间尺度逐因子 telescoping，
$$
P_n\to P\quad\text{于 }B(H_\sigma,H).
\tag{4.2}
$$

对 $u\in H_\sigma$，自然词中每个 $E_\nu$ 的输入仍有正次数权。
从左侧依次使用 (3.5)，准确得到
$$
RPu=u.
\tag{4.3}
$$
由 (1.5)、(4.2)，于是 $RP_nf\to f$。

若 $u$ 的 Walsh 次数至多 $q$，取
$\sigma=(q+1)^{-1/2}$。有
$\|u\|_\sigma\le e^{\sqrt{q+1}}\|u\|$，所以
$$
\boxed{
\|Pu\|\le A\exp\big((B+1)\sqrt{q+1}\big)\|u\|.
}
\tag{4.4}
$$
此式控制整个有限次数空间，不限制最高物理位。
特别，
$$
\|P\chi_{J_p}\|
\le A\exp\big((B+1)\sqrt{2p+1}\big).
\tag{4.5}
$$
固定 $p$ 时 (4.2) 也给 $P_n\chi_{J_p}\to P\chi_{J_p}$。

## 5. 固定真空表示与配对域的矛盾

定义 $\psi_R(F)=\langle RFf,f\rangle$，$F\in\mathfrak C$。
该泛函未必正。假设某个 $h\in H$ 给
$$
\psi_R(F)=B(Fh,1)\qquad(F\in\mathfrak C).
\tag{5.1}
$$
固定 $p$，取有界测试
$$F_n=P_nV_{J_p}\in\mathcal A.$$
所有有界因子都在交换的 $\mathfrak C$ 中，故
$$
\psi_R(F_n)
=\langle V_{J_p}RP_nf,f\rangle
\longrightarrow\langle V_{J_p}f,f\rangle.
$$
另一方面，$\mathfrak C$ 中的算子均为 $C$ 对称，且 $V_{J_p}1=\chi_{J_p}$，
$$
B(F_nh,1)=B(h,P_n\chi_{J_p})
\longrightarrow B(h,P\chi_{J_p}).
$$
于是
$$
\langle V_{J_p}f,f\rangle=B(h,P\chi_{J_p}).
\tag{5.2}
$$
由 (4.5) 右侧的模至多为 $A\|h\|e^{(B+1)\sqrt{2p+1}}$，
而 (1.2) 的实部按 $2^{3p/2}$ 增长，矛盾。
极限顺序始终是先固定 $p$ 让 $n\to\infty$，再令 $p\to\infty$；
不要求 $h$ 属于任何无界指数的域。

因此 $\phi_f(R\,\cdot)$ 不存在固定第二向量 $1$ 的 $H$ 表示。
单端配对域引理说，对 $g\in\operatorname{Dom}X_f$，
$$B(Fg,f)=B(FX_fg,1).$$
结合 $Cf=f$，若 $Rf\in\operatorname{Dom}X_f$ 就会得到被排除的 (5.1)。
故
$$
\boxed{
Rf\notin\operatorname{Dom}X_f,\qquad
RH\not\subseteq\operatorname{Dom}X_f.
}
\tag{5.3}
$$

## 6. 同时允许有限个有界一阶预解式

还可以在上述有限乘积中插入任意有限个一阶预解式
$$
R_\nu=(a_\nu I+Z_{b^{(\nu)}})^{-1}\in\mathfrak C,
$$
其中 $b^{(\nu)}\in\ell^2$ 可以复杂，但必须真的存在有界全域逆。
其逆测试因子为实际闭一阶
$P_\nu=a_\nu I+Z_{b^{(\nu)}}$，截断是有界 $P_{\nu,n}$。
由 (1.3)--(1.4)，它从 $H_\sigma$ 到 $H_{\sigma-\delta}$ 的成本
为 $|a_\nu|+C\|b^{(\nu)}\|_2\delta^{-1/2}$，
截断在同一尺度间范数收敛。
该因子的逆关系只在已验证的一阶域上使用。

对任意固定有限混合词，分配相等的正权损失后，所有中间域和逐因子消去均合法。
若有 $m$ 个线性逆测试因子，所得总正向测试 $P$ 满足
$$
\|P:H_\sigma\to H\|
\le A'\sigma^{-m/2}\exp(B'/\sigma),
\tag{6.1}
$$
并有真实截断 $P_n\in\mathcal A$，
$P_n\to P$ 于 $B(H_\sigma,H)$、$RP_nf\to f$。
对次数至多 $q$ 选 $\sigma=(q+1)^{-1/2}$，得到
$$
\|Pu\|
\le A'(q+1)^{m/4}
\exp\big((B'+1)\sqrt{q+1}\big)\|u\|.
\tag{6.2}
$$
这一成本仍为 $e^{o(q)}$。第5节的测试论证原样成立。

所以 (5.3) 同时覆盖正一阶半群和任意实际有界一阶预解式组成的全部有限乘积与有限幂，顺序任意。只用到这些有界因子在 $\mathfrak C$ 中交换，不对任意无界词进行全空间交换或约分。

## 7. 精确范围与仍待解决的接口

本稿没有声称一般复杂一阶生成有界半群；半群因子只在已经构造的非负实系数类中使用。
若某个其他实际一阶另外已知生成有界强连续半群，
可在解析域上重新验证 (3.5) 后使用同一检测准则，但不以此假设代替证明。

没有排除真正无穷乘积、有限线性组合、适配于某个假想湮灭见证的更一般交换子正则器，也没有排除改变第二向量的分解。
R240 的 $f$ 本身连续严格正且循环，其正秩一态不可能湮灭目标慢主理想；R235 也独立排除了这一保函数正锥密度。
因此结论只排除“这类常用正则器可对每个有限秩正常态自动完成配对域条件”的普遍命题。

主问题仍是：对于假想的有限秩正慢理想湮灭态，能否利用它的额外湮灭方程构造一个满足配对域且状态取值非零的 $R\in\mathfrak C$。本稿的反例不能替代这一步。

