# R230 附录：标量 Fourier 抽取与任意复多项式右滤子障碍

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：以下结论完整证明。** 纯模型中，先证明共同相位作用在
$\overline{\mathbb C[D_m]}^{\|\cdot\|}$ 上是连续等距自同构群，
再用 Bochner Fourier 系数投影控制每个齐次项。
因此所有首阶至少 $q=2^m$ 的标量多项式及其范数闭包，
无论系数相位及相消程度，归一化真空矩都趋零。
实际模型中，所有同一 $U_m$ 的复多项式右因子、次数至多 $q^3$，
均可统一提升；不对系数大小或相消另加假设。
指数的复测度组合也有清楚的相对输出误差条件。

这是指定标量函数演算类的上界，不是完整尾交换子单位球的上界。
不同坐标的独立相位、超出实际误差预算的标量函数、非 UHF 右因子
及一般真正常湮灭态仍未处理。本文不使用纯 $D_m$ 的零核结论。

## 1. 记号及真实输入

固定 $S=S_N$ 或 $S=S_Y$，相应统一取 $X_j=N_j$ 或 $Y_j$。
在原 Haar 尾空间中置
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_{j\ge0}a_j<2,\qquad q=2^m,
$$
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad
U_m=\sum_{j\ge m}a_jX_j\in\mathcal B_m\subset A'.
\tag{1.1}
$$
尾真空为 $\Omega$，真空态为 $\omega_m$。
对任意整数 $k\ge0$，
$$
h_{m,k}:=\omega_m(D_m^k)
=k!2^{-k}e_k(a_j:j\ge m)>0
\quad(k\ge1),\qquad h_{m,0}=1.
\tag{1.2}
$$

沿用 R253 的实际 $P_m=I_{<m}\otimes Q_m\in S\mathcal A$，以及
$$
\|Q_m-D_m^q\|\le e_m,\qquad
e_m=13a_\Sigma q(3a_\Sigma)^{q-1}
 \exp\!\left(-\frac{770}{16}q^4\right).
\tag{1.3}
$$
复指数右因子源稿已经完整核实
$$
\zeta_m:=\|U_m-D_m\|
\le4a_\Sigma e^{-770q^4},
\qquad
\|U_m\|\le3a_\Sigma<6,\quad \|D_m\|\le a_\Sigma<2.
\tag{1.4}
$$
这些是实际 carry 估计，不把 $D_m$ 作为实际交换子。

以下记
$$
\beta=1+1/\sqrt2,\quad
\ell(k)=\left\lfloor k^{2/3}/4\right\rfloor,\quad
c=\frac{\log\beta}{4}>0.
\tag{1.5}
$$
当 $m\ge8$ 且 $k\ge q=2^m$ 时，$\ell(k)\ge m$。
例如 $m=8$ 时成立，此后 $2^{2m/3}$ 的逐步增长因子
$2^{2/3}>3/2$ 保持该不等式。

## 2. 所有 $k\ge2^m$ 的统一真空比

**引理 2.1。** 对所有 $m\ge8$、所有整数 $k\ge2^m$，
$$
\boxed{\quad
\frac{h_{m,k}}{\|D_m^k\|}
\le\frac43\beta^{-\ell(k)}.
\quad}
\tag{2.1}
$$

本节重做计数，使常数的 $k$ 一致性明确；不只在 $k=2^m$ 使用旧式。

按概率
$$
\pi_{m,k}(F)=a_F/e_k(a),\qquad |F|=k,
$$
选择有限 $k$ 元尾集合，记 $p_j=\mathbb P(j\in F)$。
固定 $j$，在剔除 $j$ 的无限正权序列上记
$$
C_j=\frac{e_{k-1}(a_{\ne j})}{e_k(a_{\ne j})}>0.
$$
对这个剔除序列重新选取 $k$ 个指标，其各入选概率 $p_\nu^{(j)}$ 满足
$$
p_\nu^{(j)}
=\frac{a_\nu e_{k-1}(a_{\ne j,\nu})}{e_k(a_{\ne j})}
\le\min(1,a_\nu C_j).
$$
由 Tonelli 及每次恰选 $k$ 个，
$$
k=\sum_{\nu\ne j}p_\nu^{(j)}
\le\sum_{n=1}^{\infty}\min(1,C_j/n^2)
\le\int_0^\infty\min(1,C_j/x^2)\,dx=2\sqrt{C_j}.
$$
所以 $C_j\ge k^2/4$。而准确的原分布赔率为
$$
\frac{p_j}{1-p_j}=a_jC_j.
$$
因此对每个 $j\ge m$ 都有
$$
\boxed{\quad
1-p_j\le\frac4{a_jk^2}
=\frac{4(j+1)^2}{k^2}.
\quad}
\tag{2.2}
$$
这里不需要 $k=2^m$，也没有使用尚未证明的无穷核事实。

取 $J_{m,k}=\{m,\ldots,m+\ell(k)-1\}$。
由于 $m\le\ell(k)$，并集界给
$$
\mathbb P(J_{m,k}\nsubseteq F)
\le\frac4{k^2}\sum_{j=m}^{m+\ell(k)-1}(j+1)^2
\le\frac{16\ell(k)^3}{k^2}\le\frac14.
\tag{2.3}
$$
在 $J_{m,k}$ 上使用 R237 的同一对物理偏转单位向量
$$
u_j=\cos(\pi/8)e_0+\sin(\pi/8)e_1,\quad
v_j=\sin(\pi/8)e_0+\cos(\pi/8)e_1,
$$
其他位保持 Haar 真空。它们只改有限个位。
所有 $\langle E_Fu,v\rangle\ge0$；
$J_{m,k}\subseteq F$ 时，其与 $\omega_m(E_F)$ 的比值为
$\beta^{\ell(k)}$。故
$$
\|D_m^k\|\ge\langle D_m^ku,v\rangle
\ge(3/4)\beta^{\ell(k)}h_{m,k}.
$$
这证明 (2.1)。

### 2.1 可求和的完整次数尾

令
$$
\Gamma_q:=\frac43\sum_{k=q}^{\infty}\beta^{-\ell(k)}.
\tag{2.4}
$$
整数 floor 在这个定义中保留。因为
$\beta^{-\ell(k)}\le\beta e^{-ck^{2/3}}$，递减积分比较给
$$
\begin{aligned}
\Gamma_q
&\le\frac{4\beta}{3}
\left(e^{-cq^{2/3}}+\int_q^\infty e^{-cx^{2/3}}dx\right)\\
&\le\frac{4\beta}{3}e^{-cq^{2/3}}
\left(1+\frac{3q^{1/3}}{2c}
        +\frac{3\sqrt\pi}{4c^{3/2}}\right).
\end{aligned}
\tag{2.5}
$$
最后一步令 $y=x^{2/3}$，再用
$\sqrt{q^{2/3}+t}\le q^{1/3}+\sqrt t$。
因此
$$
\boxed{\quad
\Gamma_q=O\!\left((1+q^{1/3})e^{-cq^{2/3}}\right)\longrightarrow0.
\quad}
\tag{2.6}
$$
此处的常数独立于 $m$ 和全部 $k\ge2^m$。

## 3. 范数闭标量代数上的共同相位作用

令
$$
\mathscr A_m^0=\overline{\mathbb C[D_m]}^{\|\cdot\|},\qquad
\mathscr I_{m,q}^0
=\overline{D_m^q\mathbb C[D_m]}^{\|\cdot\|}.
\tag{3.1}
$$

**引理 3.1。** 在 $\mathscr A_m^0$ 上存在连续的等距自同构群
$$
\alpha_\theta(p(D_m))=p(e^{i\theta}D_m).
\tag{3.2}
$$
这里“连续”指对每个固定代数元素，随 $\theta$ 在算子范数中连续。

证明。对有限截断
$D_{m,M}=\sum_{m\le j<M}a_jE_j$，有限物理对角酉将每个 $E_j$
同时转到 $e^{i\theta}E_j$，故
$$
\|p(e^{i\theta}D_{m,M})\|=\|p(D_{m,M})\|.
$$
令 $M\to\infty$，得到
$$
\|p(e^{i\theta}D_m)\|=\|p(D_m)\|.
\tag{3.3}
$$
特别若两个多项式在 $D_m$ 上相等，其相位变换也相等；
所以映射良定义。它在多项式上乘法保持且等距，
故唯一延拓到 (3.1)，逆为 $\alpha_{-\theta}$。
多项式上连续，再用等距性和范数逼近得全部元素的连续性。

全过程只使用有限位酉及范数极限。
没有把统一无限相位旋转当作当前 Haar 不完全张量积上的酉。
也没有假定此相位作用在该表示中是 WOT 正常的。

对整数 $k$ 定义 Bochner 系数投影
$$
\mathcal F_k(V)=\frac1{2\pi}\int_0^{2\pi}
 e^{-ik\theta}\alpha_\theta(V)\,d\theta.
\tag{3.4}
$$
立即有
$$
\boxed{\quad\|\mathcal F_k(V)\|\le\|V\|.\quad}
\tag{3.5}
$$
若 $p(z)=\sum p_kz^k$，则
$$
\mathcal F_k(p(D_m))=p_kD_m^k.
$$
因此
$$
\boxed{\quad
|p_k|\,\|D_m^k\|\le\|p(D_m)\|.
\quad}
\tag{3.6}
$$
该界保持每个复系数的真实相位；它不因不同次数之间的相消而失效。

对一般 $V\in\mathscr I_{m,q}^0$，由范数逼近，
$\mathcal F_k(V)=0$ 当 $k<q$，而
$\mathcal F_k(V)\in\mathbb C D_m^k$ 当 $k\ge q$。
连续群作用的 Fejér 平均在范数中趋于 $V$：
用 Fejér 核非负、积分为1、远离0的质量趋零，
直接估计 $\int F_N(\theta)(\alpha_\theta(V)-V)\,d\theta$ 即可。

## 4. 全部纯标量复函数的统一障碍

**定理 4.1。** 对所有 $m\ge8$、$q=2^m$，以及所有
$V\in\mathscr I_{m,q}^0$，
$$
\boxed{\quad
|\omega_m(V)|\le\Gamma_q\|V\|.
\quad}
\tag{4.1}
$$

对多项式 $V=p(D_m)$、$p_0=\cdots=p_{q-1}=0$，
由 (3.6)、(2.1) 直接得
$$
|\omega_m(V)|
\le\sum_{k\ge q}|p_k|h_{m,k}
\le\|V\|\sum_{k\ge q}\frac{h_{m,k}}{\|D_m^k\|}
\le\Gamma_q\|V\|.
$$
范数连续性把结论传给闭包。
也可对一般 $V$ 使用 §3 的 Fejér 平均：
(2.4)、(3.5) 保证真空 Fourier 系数绝对可和，
从而 $\omega_m(V)=\sum_{k\ge q}\omega_m(\mathcal F_k(V))$，得到相同界。

这个结论涵盖任意次数、任意复系数及任意相消程度。
特别，上一指数源稿中的纯复测度混合
$$
D_m^q\int e^{zD_m}\,d\sigma(z)
$$
只要积分按范数存在，便属于 $\mathscr I_{m,q}^0$。
它不需要先对混合的算子相消比作任何上界。

更一般，任意在0附近全纯的标量函数 $f$ 都满足
$D_m^q f(D_m)\in\mathscr I_{m,q}^0$。
确实，$D_m$ 拟幂零：把有限头幂零和与小范数尾和分开，
其交换性给 $r(D_m)$ 不超过任意尾范数，故 $r(D_m)=0$。
因此 $f$ 在0处的幂级数在 $D_m$ 上绝对范数收敛。

$\mathscr I_{m,q}^0$ 单位球的 WOT 闭包仍满足
$|\omega_m(V)|\le\Gamma_q$，因为真空矩 WOT 连续。
这只是该单位球闭包上的界；若极限范数变小，不把它免费代入 (4.1)
的右侧。也没有声称任意强闭代数元素存在同范数的此类标量多项式逼近；
不在此调用实际 $A'$ 的 R88 来替代纯 $D_m$ 标量代数的不同问题。

## 5. 全部实际标量多项式：任意系数的自动相对预算

考虑任意非零复多项式
$$
p(z)=\sum_{n=0}^{N}b_nz^n.
$$
定义
$$
R_0=D_m^q p(D_m),\qquad
G=p(U_m)\in\mathcal B_m,\qquad R=Q_mG.
\tag{5.1}
$$
$R$ 是真实主理想尾测试；完整空间中的 $I_{<m}\otimes R\in S\mathcal A$。

先有 $R_0\ne0$。若 $n_0$ 是 $p$ 的首阶，
写 $p(z)=z^{n_0}r(z)$、$r(0)\ne0$。
拟幂零性使 $r(D_m)$ 可逆，且 $D_m^{q+n_0}\ne0$
（其真空矩严格正），故 $R_0\ne0$。

对每个 $k\ge m$，在 $e_k(a_j:j\ge m)$ 中只保留前 $k$ 个指标，
再用 $k!\ge(k/e)^k$，得到
$$
h_{m,k}\ge k!2^{-k}(m+k)^{-2k}
\ge(8ek)^{-k}.
\tag{5.2}
$$
对 $R_0$ 作相位 Fourier 抽取，
$$
|b_n|\,\|D_m^{q+n}\|\le\|R_0\|,
$$
所以
$$
|b_n|\le(8e(q+n))^{q+n}\|R_0\|.
\tag{5.3}
$$
令 $K=q+N$ 并置
$$
B_{q,N}=(N+1)(8eK)^K6^N.
\tag{5.4}
$$
于是
$$
\boxed{\quad
\|p(U_m)\|\le B_{q,N}\|R_0\|.
\quad}
\tag{5.5}
$$
这是由输出范数反控全部系数的估计；
没有对 $b_n$ 的大小、相位或条件数作假设。

不用 $D_m$ 与 $U_m$ 交换，准确望远镜恒等式给
$$
U_m^n-D_m^n
=\sum_{r=0}^{n-1}U_m^r(U_m-D_m)D_m^{n-1-r}.
$$
由 (1.4)，
$$
\|U_m^n-D_m^n\|\le n6^{n-1}\zeta_m.
$$
结合 (5.3)--(5.4)，
$$
\boxed{\quad
\|p(U_m)-p(D_m)\|
\le \zeta_m N B_{q,N}\|R_0\|.
\quad}
\tag{5.6}
$$
因此所有实际重复幂和 carry 都包含在
$$
\boxed{\quad
\frac{\|Q_mp(U_m)-D_m^qp(D_m)\|}{\|R_0\|}
\le \eta_{m,N}:=
B_{q,N}\bigl(e_m+a_\Sigma^q\zeta_m N\bigr).
\quad}
\tag{5.7}
$$

**定理 5.1。** 若整数预算 $N_m\ge0$ 满足
$$
(q+N_m)\log(q+N_m+2)=o(q^4),\qquad q=2^m,
\tag{5.8}
$$
则对所有次数至多 $N_m$ 的非零复多项式，
一致有 $Q_mp(U_m)\ne0$，且
$$
\boxed{\quad
\frac{|\omega_m(Q_mp(U_m))|}{\|Q_mp(U_m)\|}
\le\frac{\Gamma_q+\eta_{m,N_m}}{1-\eta_{m,N_m}}
\longrightarrow0.
\quad}
\tag{5.9}
$$
特别覆盖任意次数至多 $q^3$ 的全部复多项式。

证明。由 (5.4)，
$$
\log B_{q,N}
=\log(N+1)+(q+N)\log(8e(q+N))+N\log6.
$$
(5.8)、(1.3)--(1.4) 因而给
$$
\eta_{m,N_m}
\le
\exp\!\left(-\frac{770}{16}q^4+o(q^4)\right)\longrightarrow0.
$$
第二个 carry 项有更强的 $-770q^4$ 主负指数。
(5.7) 给实际输出范数至少
$(1-\eta_{m,N_m})\|R_0\|>0$。
其真空矩至多
$(\Gamma_q+\eta_{m,N_m})\|R_0\|$，用 (4.1) 即得 (5.9)。

此外把实际输出归一化为1时，(5.5)、(5.7) 自动给
$$
\boxed{\quad
\frac{\|p(U_m)\|}{\|Q_mp(U_m)\|}
\le\frac{B_{q,N_m}}{1-\eta_{m,N_m}}.
\quad}
\tag{5.10}
$$
$N_m\le q^3$ 时右边为 $\exp(O(q^3\log q))$，
仍被真实 $q^4$ 误差支付。
这不是只对系数已受控的多项式成立，而是对全部复系数统一成立。

这里的“标量”明确指同一个慢尾和 $U_m$ 的函数。
它不是任意有限多变量 $p(N_m,N_{m+1},\ldots)$ 的结论，
也不把尾交换子所有元素免费认作 $U_m$ 的这种函数。

## 6. 实际复指数混合：相对输出误差的准确范围

令 $\sigma_m$ 是支撑在 $|z|\le q^6$ 的有限复 Borel 测度，并置
$$
G_{m,\sigma}=\int e^{zU_m}\,d\sigma_m(z)\in\mathcal B_m,
\quad
R_{m,\sigma}=Q_mG_{m,\sigma},
$$
$$
R^0_{m,\sigma}=D_m^q\int e^{zD_m}\,d\sigma_m(z)
\in\mathscr I_{m,q}^0.
\tag{6.1}
$$
假设 $R_{m,\sigma}\ne0$。
上一指数源稿的全算子比较为
$$
\|R_{m,\sigma}-R^0_{m,\sigma}\|
\le\Delta_m^*\|\sigma_m\|_{\rm TV},
$$
$$
\Delta_m^*
=e_m e^{16q^3}+a_\Sigma^q q^6\zeta_m e^{17q^3}.
\tag{6.2}
$$
其主负指数准确为
$$
\log\Delta_m^*
=-\frac{770}{16}q^4+16q^3+O(q\log q).
\tag{6.3}
$$
(6.3) 允许的 $O(q\log q)$ 比直接预因子估计稍宽，但足够且保持主项。

定义实际相对输出误差
$$
\varepsilon^{\rm rel}_m
=\frac{\Delta_m^*\|\sigma_m\|_{\rm TV}}
       {\|R_{m,\sigma}\|}.
\tag{6.4}
$$
由 (4.1) 及
$\|R^0_{m,\sigma}\|\le\|R_{m,\sigma}\|
+\Delta_m^*\|\sigma_m\|_{\rm TV}$，准确有
$$
\boxed{\quad
\frac{|\omega_m(R_{m,\sigma})|}{\|R_{m,\sigma}\|}
\le
\Gamma_q+(1+\Gamma_q)\varepsilon^{\rm rel}_m.
\quad}
\tag{6.5}
$$
即使纯混合发生任意强的相消，(6.5) 仍成立；
不需要给纯混合的相消条件数加上界。

所以只要 $\varepsilon^{\rm rel}_m\to0$，这些实际混合的真空比也趋零。
一个清楚的充分条件是，实际输出已归一化为1，并且
$$
\|\sigma_m\|_{\rm TV}\le e^{Cq^3}
$$
对某固定 $C$ 成立。更一般，
$$
\limsup_m\frac1{q^4}
\log^+\!\left(
\frac{\|\sigma_m\|_{\rm TV}}{\|R_{m,\sigma}\|}
\right)
<\frac{770}{16}
\tag{6.6}
$$
同样足够。

这里的 TV 条件是这个 Bochner 指数表示的充分预算，
不是任意 $A'$ 元素必满足的条件。若误差相对于输出被放大到不可控，
本文没有给实际混合的比值上界。
也没有假定每个尾交换子都具有这个复测度表示。

## 7. 与真正常湮灭条件的接口

若 $\rho\ge0$ 真正湮灭 $S\mathcal A$，则本稿每个实际右因子均满足
$$
\operatorname{Tr}\bigl(\rho(I_{<m}\otimes Q_mG_m)\bigr)=0
$$
这个精确等式，因为 $G_m\in\mathcal B_m\subset A'$，
且 $P_m=I_{<m}\otimes Q_m\in S\mathcal A$。
具体地，本稿多项式、指数及其 Bochner 范数积分均由 $U_m\in\mathcal A$
得到 $G_m\in\mathcal A$；对一般 $G\in A'$ 的同一真湮灭等式，
可用 R88 有界 SOT 多项式逼近及正常迹连续性，亦见 R235 全右测试。
R235 对纯 $T_m=I_{<m}\otimes D_m^q$ 的右测试还给
$$
\left|\frac{\operatorname{Tr}(\rho T_mG_m)}{h_{m,q}}\right|
\le\operatorname{Tr}(\rho)\,\frac{e_m}{h_{m,q}}\,\|G_m\|.
\tag{7.1}
$$
本稿没有将 (7.1) 的非正交叉约化换成某个局部正密度。

R253 希望找到实际尾理想元素，其真空矩相对于输出范数非消失，
再与任意正常态的尾真空逼近矛盾。
本稿证明，§5 的全部预算内标量多项式及 §6 满足相对误差条件的
标量复指数混合，统一不能完成这一步。
这不是用某个固定非湮灭态替代未知真密度；
其限制对象是完整的一类真实主理想测试。

上一指数源稿 §8 给出的相消量下界仍正确，
但在“同一个 $D_m$ 的标量混合”中仅有该相消并不足够：
本稿的逐次 Fourier 系数控制进一步排除了全部纯标量混合。
真正未覆盖的方向包括多坐标复相位、不能由上述预算比较的实际标量函数，
以及针对真密度构造的更一般 $A'$ 右因子。
没有把 (5.9) 或 (6.5) 宣布为完整理想范数 $q_m\to0$。

## 已证依赖

- R253：真实相位乘积 $Q_m$、原 Haar 尾代数、$e_m$。
- R237 正右因子附录：有限物理偏转向量；本稿 §2 对所有 $k\ge q$
  重新给出不依赖固定基数的完整遗漏界与求和。
- 复指数右因子及完整 Gram 源稿：实际 $\zeta_m$、$q^6$ 参数盘的
  $\Delta_m^*$，仅在 §6 引用。
- 本稿新步骤：纯标量范数闭代数的等距相位群及 Fourier 系数控制；
  完整次数可求和界；任意复系数的实际多项式自动相对 carry 预算。


完整依赖：[复指数及完整 Gram](R230-appendix-complex-exponential-tail-right-filters-and-full-gram.md)。
[完整工作源](../notes/2026-11-13-scalar-tail-fourier-extraction-and-arbitrary-polynomial-right-filter-obstruction-normal-complex.md)。
