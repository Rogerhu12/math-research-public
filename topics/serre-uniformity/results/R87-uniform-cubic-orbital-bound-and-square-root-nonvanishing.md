# R87：三次轨道项的统一估计与平方根非消失范围

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明；全文及局部界、计数、主项和常数已独立复核。** 本文对变化的虚二次域和变化环类导子同时证明：对每个 $\epsilon>0$，有可有效选取的绝对常数 $C_\epsilon$，使
$$
\boxed{
p\ge C_\epsilon\frac{M^{1+\epsilon}}{h(\mathcal O_c)}
\quad\Longrightarrow\quad
\exists g\in S_2(\Gamma_0(p))^{\mathrm{new}}:
L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.
}
$$
其中 $\eta$ 为任意原始三次环类角色，$M=|D_K|c^2$，$p$ 惰性且 $p\nmid M$。正文还给不含隐含常数的有限算术判据。

Siegel 下界进而给对 $K,c,\eta$ 统一的 $p\gg_\nu M^{1/2+\nu}$ 非消失范围；这一删除类数后的常数一般无效。带实际类数的主结论有效。实际小惯性分支若有非 exceptional 分母，因而必须满足对所有虚二次域统一的 $M\gg_\delta p^{2-\delta}$；这仍是必要下界，没有导子上界或 exceptional 排除。

## 1. 对象和明示判据

设 $K$ 判别式为 $-D$，$D>0$，
$$\mathcal O_c=\mathbb Z+c\mathcal O_K,\qquad M=Dc^2,\qquad h=h(\mathcal O_c).$$
$\eta$ 为准确导子 $c$、阶恰为 $3$ 的环类角色。设 $p>37$ 为在 $K$ 惰性的素数，且 $p\nmid M$。令
$$
S_0=\{q:q\mid c,\ q\nmid D\},\qquad
c_0=\prod_{q\in S_0}q^{v_q(c)},\qquad c_D=c/c_0,
$$
$$
\mathcal L_c=\prod_{q\mid c}\left(1-\frac{\chi_K(q)}q\right)^{-1},\qquad
\mathcal T(M)=\max_{1\le m<M}\tau(m).
$$
这里 $\tau$ 为正整数除数个数，$\omega$ 表示不同素因子个数，并取 $\omega(1)=0$。

**定理 87.1。** 在 FW 的测度和单位测试约定下，有
$$
\boxed{
|I_{\mathrm{reg}}(f)|
\le\frac{4c_D^2\,4^{\omega(D)}16^{\omega(c_0)}\mathcal T(M)^2}{p},
\qquad
I_{\mathrm{irreg}}(f)=\frac{4h\mathcal L_c^2}{M}.
}
\tag{87.1}
$$
因此下式为完全有效的非消失充分条件：
$$
\boxed{
p>\frac{c_D^2\,4^{\omega(D)}16^{\omega(c_0)}\mathcal T(M)^2M}
{h\mathcal L_c^2}.
}
\tag{87.2}
$$
不要求 $D$ 为奇数或 $(D,c)=1$。三次角色的特殊性给 $c_D\mid9$，将在第 2 节直接证明。

**推论 87.2。** 对每个 $\epsilon>0$，可有效选取与 $K,c,\eta,p$ 全无关的 $C_\epsilon>0$，使
$$
\boxed{p\ge C_\epsilon M^{1+\epsilon}/h\ \Longrightarrow\ \exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.}
\tag{87.3}
$$

本文不使用 FW Lemma 6.6–6.7 的全局计数步骤。只使用其已发表的谱展开、irregular 主项、轨道支集和局部轨道估计，再用通过零点的整倍数分层给出完整的新计数。

## 2. 分歧交集和单位

### 2.1 $c_D\mid9$

若 $q\mid D$ 且 $q\ne3$，$K_q/\mathbb Q_q$ 为分歧二次扩张。$\mathcal O_{K,q}^{\times}$ 对剩余域单位的像已由 $\mathbb Z_q^{\times}$ 覆盖，其余单位过滤是 pro-$q$ 群。$\eta$ 在 $\mathbb Q_q^{\times}$ 平凡且阶为三，因而在全部 $\mathcal O_{K,q}^{\times}$ 平凡。于是 $q\nmid c$。这也包含 $q=2$。

若 $3\mid D$，令 $\mathfrak p$ 为局部极大理想，$U^j=1+\mathfrak p^j$。绝对分歧指数为二，$3$ 进对数在 $U^2$ 上给同构，并有
$$
(U^2)^3=U^4=1+9\mathcal O_{K,3}.
$$
三阶角色杀死这个立方群，又杀死 $\mathbb Z_3^{\times}$，故在 $(\mathbb Z_3+9\mathcal O_{K,3})^{\times}$ 平凡。因此准确环类导子在三处的指数至多为二，
$$\boxed{c_D\mid9.}\tag{87.4}$$
这一证明只使用角色的阶及其中心平凡性，并不要求它来自椭圆曲线。

### 2.2 $\mathcal O_c^{\times}=\{\pm1\}$

只有 $K=\mathbb Q(i),\mathbb Q(\sqrt{-3})$ 的极大序有额外单位。其 $c>1$ 子序均只有 $\pm1$；若 $c=1$，其类群平凡，不可能有三阶角色。因此在本文所有情形中
$$u_c=|\mathcal O_c^{\times}|/2=1.$$
记 $u_K=|\mathcal O_K^{\times}|/2$，环类数公式成为
$$\boxed{h=\frac{h_Kc}{u_K\mathcal L_c}.}\tag{87.5}$$

## 3. 相对迹公式及 regular 参数的实际区间

取 FW 的 $F=\mathbb Q,E=K,N=p,k=1,m=0$，各有限处取极大序单位的特征函数，额外 Hecke 测试也取单位。这里的四元数代数为 $B_{p,\infty}$。

FW Lemma 3.6 使一维谱贡献为零，因为三阶角色不是阶至多二角色的范数组合。Proposition 3.9 因而给
$$
I(f)=\sum_{g\in\mathcal F(p,2)}b_g
 L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right),\qquad b_g>0.
\tag{87.6}
$$
$\mathcal F(p,2)$ 为准确水平 $p$ 的权二新形式集合。只要 $I(f)>0$，其中就有一个非零中心值。

FW §2 的导子范数为 $c^2$。由其 Lemmas 4.10–4.11、4.21，可能贡献的 regular 参数 $\xi\in\mathbb Q$ 满足
$$
\xi<0,\qquad v_p(\xi)\ge1,\qquad \frac{M}{1-\xi}\in\mathbb Z.
$$
所以可以唯一写为
$$
\boxed{\xi=\xi_y=\frac{y}{y-M},\qquad 0<y<M,\qquad p\mid y.}\tag{87.7}
$$
确切地，置 $m=M/(1-\xi)$，则 $0<m<M$，取 $y=M-m$。因 $p\nmid M$，$v_p(\xi)\ge1$ 迫使 $p\mid y$。

并不是每个这样的 $y$ 都满足剩余的全局范数条件。下文对所有 (87.7) 的整数取非负上界，只扩大和，因而不需删除不支持的参数。特别 $p\ge M$ 时这个整数集合为空，regular 部分为零。

## 4. 各处轨道项的统一上界

以下 $I_q(\xi)$ 采用 FW 原来的局部测度。所有 Haar 体积在全局估计前保留，不能把随 $D$ 变化的因子放进一个未说明的常数。

### 4.1 $q\mid D$：直接用紧环面体积

令 $d_q=v_q(D)$。因 $K_q/\mathbb Q_q$ 分歧，
$$T_q=\mathbb Q_q^{\times}\backslash K_q^{\times}$$
紧，且
$$
\operatorname{vol}(\mathcal O_{K,q}^{\times})=q^{-d_q/2},\qquad
\operatorname{vol}(\mathbb Z_q^{\times})=1,
$$
$$\operatorname{vol}(T_q)=2q^{-d_q/2}.$$
前两式由 FW 的自对偶加法测度和乘法测度定义给出；商的赋值部分恰有两个陪集。

局部轨道积分原本是在 $T_q\times T_q$ 上积分。测试函数绝对值不超过一，$\eta$ 为酉角色，因此不论 $\eta_q$ 是否分歧，
$$
\boxed{|I_q(\xi)|\le\operatorname{vol}(T_q)^2=4q^{-d_q}.}
\tag{87.8}
$$
该论证对偶素数及三处也成立，不需要引入随局部二次域变化的未知常数。乘遍 $q\mid D$ 得
$$\prod_{q\mid D}|I_q(\xi)|\le4^{\omega(D)}/D.$$

### 4.2 水平和无穷处

$p$ 在 $K$ 不分歧惰性，$\operatorname{vol}(T_p)=1$，所以 $|I_p(\xi)|\le1$。其支集条件 $p\mid y$ 已保留在 (87.7)。

无穷处 $k=1,m=0$ 的有限维表示平凡；FW Lemma 4.14 给
$$|I_\infty(\xi)|=\operatorname{vol}(\mathbb R^{\times}\backslash\mathbb C^{\times})^2=4.$$

### 4.3 $q\nmid Dcp$ 的未分歧处

记
$$r_q=v_q(y),\qquad t_q=v_q(M-y).$$
因 $q\nmid M$，$\min(r_q,t_q)=0$。FW Lemmas 4.12–4.13 给：惰性处绝对值不超过一，分裂处不超过
$$1+|r_q-t_q|\le(r_q+1)(t_q+1).$$
这些素数的乘积因而可由相应的除数因子控制。

### 4.4 $q\in S_0$ 的变化导子处

此时 $K_q$ 分裂或不分歧惰性，置
$$n=n_q=v_q(c)\ge1,\qquad L_q=(1-\chi_K(q)/q)^{-1}\le2.$$
因 $q\nmid D$，有 $v_q(M)=2n$。定义截断赋值
$$\boxed{j_q=\min\{v_q(y),2n\}\in\{0,1,\ldots,2n\}.}\tag{87.9}$$

若 $j_q<2n$，则 $r_q=t_q=j_q$，以及
$$v_q(1-\xi)=2n-j_q>0.$$
FW Lemma 4.19 的未分歧局部常数为一，单位体积也为一，给
$$
|I_q(\xi)|\le L_q^2q^{-2n+j_q/2}.
\tag{87.10}
$$
若某个赋值奇偶使轨道本来为零，这个非负上界仍成立。

若 $j_q=2n$，则 $r_q,t_q\ge2n$，且至少一个等于 $2n$。同一局部估计给
$$
|I_q(\xi)|\le L_qq^{-n}(1+|r_q-t_q|)
\le L_qq^{-n}(r_q+1)(t_q+1).
\tag{87.11}
$$
这里对惰性情形容许同一个较大的界。

定义不含最后除数因子的权
$$
b_q(j)=
\begin{cases}
L_q^2q^{-2n+j/2},&0\le j<2n,\\
L_qq^{-n},&j=2n.
\end{cases}
\tag{87.12}
$$
第 4.3 节和 (87.11) 的额外整数因子位于彼此不交的素数集，故可同时包在一个全局乘积中：
$$
\boxed{
|I(\xi_y,f)|
\le\frac{4\,4^{\omega(D)}}D\,
\tau(y)\tau(M-y)\prod_{q\in S_0}b_q(j_q).
}
\tag{87.13}
$$
未使用的素数除数因子只会增大右边，没有对相同素数重复消耗两份除数估计。

## 5. 通过零点的整倍数计数

固定一个向量 $\mathbf j=(j_q)_{q\in S_0}$。满足 (87.7)、(87.9) 的每个整数 $y$ 都是
$$p\prod_{q\in S_0}q^{j_q}$$
的正整数倍。因 $p\nmid c_0$，这些因子互素。所以其数目至多为
$$
\boxed{
\frac{M}{p\prod_{q\in S_0}q^{j_q}}.
}
\tag{87.14}
$$
这个上界没有遗漏 $+1$：数的是严格位于 $(0,M)$ 内的**正整数倍**，进程通过零点；计数最多为该长度比的下取整。即使集合只有一个元素，(87.14) 仍然成立。

由 (87.13)、$\tau(y),\tau(M-y)\le\mathcal T(M)$，以及对有限个 $\mathbf j$ 求和，
$$
\begin{aligned}
|I_{\mathrm{reg}}(f)|
&\le\frac{4\,4^{\omega(D)}}D\mathcal T(M)^2
\sum_{\mathbf j}
\frac{M}{p\prod_q q^{j_q}}\prod_qb_q(j_q)\\
&=\frac{4\,4^{\omega(D)}M\mathcal T(M)^2}{Dp}
\prod_{q\in S_0}\left(\sum_{j=0}^{2n_q}q^{-j}b_q(j)\right).
\end{aligned}
\tag{87.15}
$$
每个局部有限和满足
$$
\begin{aligned}
\sum_{j=0}^{2n}q^{-j}b_q(j)
&=q^{-2n}\left(L_q^2\sum_{j=0}^{2n-1}q^{-j/2}+L_qq^{-n}\right)\\
&\le q^{-2n}\left(\frac4{1-1/\sqrt2}+1\right)\\
&=(9+4\sqrt2)q^{-2n}<16q^{-2n}.
\end{aligned}
\tag{87.16}
$$
$S_0$ 为空时按空积为一处理。利用 $M/(Dc_0^2)=c_D^2$，便得
$$
|I_{\mathrm{reg}}(f)|
\le\frac{4c_D^2\,4^{\omega(D)}16^{\omega(c_0)}\mathcal T(M)^2}{p}.
$$
这证明 (87.1) 的第一式，全部变化域依赖都已显式写出。

## 6. 正主项的准确类数表达

FW Proposition 4.20 在当前单位测试下给
$$
I_{\mathrm{irreg}}(f)=\frac{4L(1,\chi_K)\mathcal L_c}{c\sqrt D}.
$$
其 $L$ 为完成函数，包含无穷处 $L_\infty(1,\chi_K)=1/\pi$。普通二次类数公式因此给
$$L(1,\chi_K)=\frac{h_K}{u_K\sqrt D}.$$
用 (87.5)，
$$
\begin{aligned}
I_{\mathrm{irreg}}(f)
&=\frac{4h_K\mathcal L_c}{u_KcD}\\
&=\frac{4h\mathcal L_c^2}{c^2D}
=\frac{4h\mathcal L_c^2}{M}.
\end{aligned}
\tag{87.17}
$$
这证明第二式。若 (87.2) 成立，则 $I_{\mathrm{irreg}}>|I_{\mathrm{reg}}|$，因而 $I(f)>0$。由 (87.6)，存在所需的实际新形式中心值。定理 87.1 得证。

## 7. 对所有域统一而有效的小幂常数

以下给出 (87.3) 的一个明确、远非最优的常数。对 $u>0$ 定义
$$
T_u=\prod_{\substack{q\ \mathrm{素数}\\q\le2^{1/u}}}\max_{e\ge0}(e+1)q^{-ue},\qquad
X_u=16^{\pi(16^{1/u})},
$$
$$\beta_u=\prod_{\substack{q\ \mathrm{素数}\\q\le2^{1/u}}}(1-1/q)>0.$$
这些均可有效计算；每个关于 $e$ 的最大值在有限处达到。直接逐素数估计给
$$
\tau(m)\le T_um^u,\qquad
16^{\omega(m)}\le X_um^u,\qquad
\frac{\phi(c)}c\ge\beta_uc^{-u}.
\tag{87.18}
$$
第一式使用 $(e+1)\le2^e$ 处理大素数；第二式使用 $16\le q^u$；第三式使用 $1-1/q\ge1/2>q^{-u}$。小素数贡献已分别放进有限积。

给定 $\epsilon>0$，
$$\mathcal T(M)^2\le T_{\epsilon/8}^2M^{\epsilon/4},$$
$$4^{\omega(D)}16^{\omega(c_0)}\le16^{\omega(Dc_0)}\le X_{\epsilon/4}M^{\epsilon/4},$$
其中 $(D,c_0)=1$。又因 $\mathcal L_c\ge\phi(c)/c$，
$$\mathcal L_c^{-2}\le\beta_{\epsilon/2}^{-2}c^\epsilon\le\beta_{\epsilon/2}^{-2}M^{\epsilon/2}.$$
加上 $c_D^2\le81$，(87.2) 的右侧不超过
$$81X_{\epsilon/4}T_{\epsilon/8}^2\beta_{\epsilon/2}^{-2}\frac{M^{1+\epsilon}}h.$$
因此可以取
$$
\boxed{C_\epsilon=162X_{\epsilon/4}T_{\epsilon/8}^2\beta_{\epsilon/2}^{-2}.}
\tag{87.19}
$$
在 (87.3) 的非严格条件下，它仍比 (87.2) 的右侧至少多一个因子二。推论 87.2 得证。

没有计算这些巨大有限积的十进制展开；本节给的是完整有效定义和证明，并不声称此粗常数适合直接处理很小的层。

## 8. 平方根指数及实际分支

R83 §7 已由普通 Siegel 下界、环类数公式和有效 $\phi(c)$ 界证明：对每个 $a>0$，有对 $K,c$ 统一的 $A_a>0$，使
$$h(\mathcal O_c)\ge A_aM^{1/2-a}.$$
$A_a$ 一般无效。给定 $\nu>0$，在 (87.3) 取 $\epsilon=\nu/2$，在上式取 $a=\nu/2$，得到
$$
\boxed{
p\ge C'_\nu M^{1/2+\nu}\quad\Longrightarrow\quad
\exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0,
}
\tag{87.20}
$$
其中 $C'_\nu=C_{\nu/2}/A_{\nu/2}$，对 $K,c,\eta$ 全部统一，但一般无效。未使用 GRH。

因此 R66 的实际小惯性分支若存在一个非 exceptional 的分母素数，R69/R72 的实际秩零商和尖点论证迫使全部相关中心值为零。必须同时满足 (87.2)–(87.3) 的逆否必要条件，特别对每个 $\epsilon>0$，
$$\boxed{p<C_\epsilon M^{1+\epsilon}/h(\mathcal O_c).}\tag{87.21}$$
由 (87.20)，对 $0<\delta<2$ 取 $\nu=\delta/[2(2-\delta)]$，有
$$\frac1{1/2+\nu}=2-\delta,$$
从而
$$\boxed{M\gg_\delta p^{2-\delta}.}\tag{87.22}$$
此处常数对所有虚二次底域统一，一般无效；类数一有限底域的有效版本仍由 R84 给出。

R87 在量词上加强 R84，并将 R83/R86 的统一渐近指数分别从 $7/8,5/6$ 推到 $1/2$ 加任意小量。R81 的 $M<3p$ 仍提供小参数下更实用、无隐含常数的范围。四者都不提供变化导子 $M$ 的上界，也不处理全部分母 exceptional 的情形。

## 9. 为什么不能省略单元素计数边界

本文计数不借用 FW Lemma 6.6 的形如
$$|S_{r,t}(a)|\le c(\mathbb Q)\,a/(p q^{\max(r,t)})$$
的一般平移进程估计。该引理定义中 $a\in\mathbb Q$ 可任取。固定一个允许的导子素数 $q$，取 $t\to\infty$ 和与 $q$ 不同的惰性素数 $p>q^{2t}$，置
$$a=p+q^t,\qquad y=p.$$
则 $y\in p\mathbb Z$，$|y|<a$，$v_q(y)=v_q(a)=0$，$v_q(y-a)=t$，所以所计集合非空；但
$$\frac a{p q^t}=q^{-t}+p^{-1}<2q^{-t}\longrightarrow0.$$
因此在这个任意 $a$ 的一般性下，任何只依赖 $\mathbb Q$ 的常数都不足以去掉单元素的边界项。可以固定 $K=\mathbb Q(\sqrt{-17})$ 及准确导子七的三次角色，使 $q=7$；惰性素数任意大。该角色确实存在：判别式 $-68$ 的四个约化型为 $[1,0,17]$、$[2,2,9]$、$[3,2,6]$、$[3,-2,6]$，故 $h_K=4$；七分裂使 $h(\mathcal O_7)=24$，其三阶角色不能降至阶数为四的极大序类群，因此准确导子为七。

一个处于其后续应用形状 $a=Dc^2$ 的具体小检查是
$$D=68,\quad c=7,\quad p=61,\quad a=3332,\quad y=2989.$$
有 $v_7(y)=2,v_7(y-a)=3$，而 $4a/(61\cdot7^3)<1$。这直接指出原证明从 $n<|S|\le n+1$ 走到 $n+1\le2n$ 时 $|S|=1,n=0$ 的问题。

以上不声称 FW Lemma 6.7 的最终结论为假。本篇对所需三次角色重新证明了它在 $F=\mathbb Q$ 的估计，并给出随 $K$ 统一的加强；使用的是 (87.14) 中通过零点的整倍数及截断赋值，完整覆盖单元素情形。正主项和已发表局部轨道公式的使用不受该计数问题影响。

## 10. 来源与检查范围

- B. Feigon, D. Whitehouse, *Averages of central L-values of Hilbert modular forms with an application to subconvexity*, **Duke Math. J. 149** (2009), 347–410。[作者全文](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)，[作者出版目录](https://bfeigon.ccny.cuny.edu/papers.html)，[DOI](https://doi.org/10.1215/00127094-2009-041)。使用 §2.1 的测度、Lemma 3.6 与 Proposition 3.9 的谱端、Lemmas 4.10–4.14/4.19/4.21 的局部和支集输入，以及 Proposition 4.20 的正主项。本文全球计数独立于其 Lemmas 6.6–6.7。
- [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际三次分支；本篇 §2.1 重新证明一般三阶角色的 $c_D\mid9$，所以主定理不限于实际异常族。
- [R83](R83-small-auxiliary-cm-orders-and-uniform-period-bound.md) §7：含非极大序的完整 Siegel 推论及其无效性；本篇只有 §8 使用它。
- [R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)、[R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：实际中心值到分母限制的接口。

这里的统一量词来自逐处体积、有限赋值和整数倍计数，不来自有限样本或数值 $L$ 值猜测。
