# R213 重建：实际深度零角色的变判别式统一非消失

日期：2026-11-13。

**状态：已证明。** 对 R166、R181 的每个实际深度零参数，本文在其准确的、在 $p$ 分歧的角色上证明统一中心值非消失范围。主要外部输入是 Qinghua Pi 已发表于 *Journal of Number Theory* **191** (2018), 213–245 的相对迹公式；本文逐式匹配 $p$ 处测试函数，并重新证明全球误差计数，不把其依赖于固定二次域的隐含常数用作变化域的统一常数。

## 1. 准确对象与结论

使用 R214 的记号。设实际小惯性分支满足

$$p>37,\quad p\equiv2,5\pmod9,\quad r(I_p)=C^3,\quad n=p+1=3d,$$

$K$ 为正规化子二次商域，判别式 $-D$，$p$ 在 $K$ 惰性。令 $\vartheta$ 为有限 Cartan 的三阶角色，$\eta=\vartheta\circ\lambda$ 的准确环类导子为 $c$。令 $\theta$ 为 $C/Z$ 上阶 $r>2$、$r\mid d$ 的字符，并固定任一符号。置

$$\Xi=(\theta\vartheta^{\pm1})\circ\lambda,\qquad \Omega=\Xi^{-1}.$$

R214 证明 $\Omega|\mathbb A_{\mathbb Q}^{\times}=1$。令 $a$ 为其 prime-to-$p$ 准确环类导子：

$$a=\begin{cases}c,&\theta(z_2)=1,\\bc,&\theta(z_2)=-1.\end{cases}$$

这里 $b,c$ 互素，且

$$a_D:=\prod_{q\mid D}q^{v_q(a)}\mid36.$$

定义

$$a_0=a/a_D,\quad M=Da^2,\quad h=h(\mathcal O_a),\quad
\mathcal L_a=\prod_{q\mid a}(1-\chi_K(q)/q)^{-1},\quad
\mathcal T(M)=\max_{1\le m<M}\tau(m).$$

设 $\mathcal F_\theta(p^2)$ 为平凡 nebentype、权二、准确水平 $p^2$，在 $p$ 具有有限尖点参数 $\{\theta,\theta^{-1}\}$ 的正规化新形式集合。参数相差共轭视为同一自守表示。

**定理 213.1。** 若

$$\boxed{p>
\frac{a_D^2\,4^{\omega(D)}16^{\omega(a_0)}\mathcal T(M)^2M}
{h\mathcal L_a^2},} \tag{213.1}$$

则存在 $f\in\mathcal F_\theta(p^2)$ 使

$$\boxed{L(\tfrac12,\pi_{f,K}\otimes\Xi)\ne0.} \tag{213.2}$$

若 $r>4$，所找到的 $f$ 自动非 CM。$r=4$ 时本定理允许非零值来自 CM 谱；非 CM 非消失必须另外过滤，不能由此定理直接声称。

**定理 213.2。** 对每个 $\epsilon>0$，可有效选取绝对常数 $C_\epsilon$，与 $K,c,b,p,\theta$ 及符号全无关，使

$$\boxed{p\ge C_\epsilon M^{1+\epsilon}/h(\mathcal O_a)
\quad\Longrightarrow\quad (213.2).} \tag{213.3}$$

可取 §6 给出的 $C_\epsilon=2592X_{\epsilon/4}T_{\epsilon/8}^{\,2}\beta_{\epsilon/2}^{-2}$。若 $\theta(z_2)=1$，可把 $2592$ 改成 $162$。

## 2. $p$ 处完整类型及导子归一化

### 2.1 完整的局部角色，不仅是惯性阶

令 $L=K_p$。R166 §4 的实际基本特征取向给

$$\lambda|I_p=\omega_2^u,\qquad u\equiv1\pmod d,\qquad 3\mid u.$$

因此 $\Xi|I_p$ 对应有限字符 $\theta$，且使用 R166 §6 的算术互反约定有

$$\boxed{\Omega_p|\mathcal O_L^{\times}=\theta,\qquad\Omega_p(p)=1.} \tag{213.4}$$

第二式由 R214 的中心平凡性给出。由于 $L/\mathbb Q_p$ 不分歧，$L^{\times}=p^{\mathbb Z}\mathcal O_L^{\times}$；这两式确定完整局部角色。它的阶 $r>2$，所以不经范数因子化，是深度零 admissible pair 的正则角色。$\Omega$ 在 $p$ 的 Hecke 理想导子指数恰为一。

Pi 的局部 pair 正是 $(L/\mathbb Q_p,\Omega_p)$，其 division-side Jacquet–Langlands 表示是

$$\sigma_p=\operatorname{Ind}_{L^{\times}U_B^1}^{B_p^{\times}}\Omega_p,$$

维数二，限制到 $L^{\times}$ 为 $\Omega_p\oplus\Omega_p^{-1}$。其 $\mathrm{GL}_2$ 对应表示的有限尖点型是 $\{\theta,\theta^{-1}\}$；采用局部 Langlands 时的未分歧 rectifier 不改变这个有限类型。因而迹公式筛选的正是 $\mathcal F_\theta(p^2)$。

### 2.2 环类导子与 Hecke 理想导子

对中心平凡的角色，在分裂或不分歧二次处，环类导子指数 $t$ 使 Hecke 导子范数为 $q^{2t}$，直接由两个分量或剩余次数二可见。在分歧二次处也相同，但应给出理由。

设 $F/\mathbb Q_q$ 分歧二次，$U_0=\mathcal O_F^{\times}$，$U_j=1+\mathfrak p_F^j$（$j\ge1$）。对 $k\ge1$，$U_{2k}/U_{2k+1}$ 是一维剩余域向量空间，中心群 $1+q^k\mathbb Z_q$ 在其中满射：$q^k$ 的 $F$ 赋值恰为 $2k$，其首项系数为一个非零剩余域元，而两域剩余域相同。因此中心平凡角色若杀死 $U_{2k+1}$，便也杀死 $U_{2k}$。当 $k=0$，$U_0/U_1$ 的剩余单位同样由中心单位覆盖。故非零 Hecke 导子指数必为偶数 $2t$，而其环类导子指数正是 $t$。论证包含 $q=2$。

所以本文角色的完整导子范数是

$$\boxed{\mathrm N\mathfrak f(\Omega)=p^2a^2.} \tag{213.5}$$

注意后文几何误差的参数是 $M=Da^2$，没有再乘 $p^2$。取消这一 $p^2$ 来自深度零 $p$ 处实际支集，而非把 $\Omega_p$ 当成不分歧。

## 3. 同一测试函数的谱端、主项和支集

取 $B=B_{p,\infty}$。在 Pi 的记号中取 $F=\mathbb Q$、$E=K$、$\mathfrak N_1=1$、$\mathfrak N_2=p$、$\mathfrak N_3=1$、$k=1,m=0$。两个 division 位置恰为 $p,\infty$。其余有限处取与环类导子 $a$ 相容的 Gross–Prasad 极大序单位特征函数。

### 3.1 $p$ 处实际矩阵系数

选择 $\sigma_p$ 的 $\Omega_p$ 特征线上的单位向量。Pi 式 (3.1) 的反向矩阵系数为

$$f_p(zu)=\Omega_p(z)^{-1}\quad(z\in L^{\times},u\in U_B^1),
\qquad f_p(g)=0\quad(g\notin L^{\times}U_B^1). \tag{213.6}$$

它在 $L^{\times}$ 上与轨道积分里的 $\Omega_p$ 抵消。由于 $\Omega_p$ 正则，该矩阵系数不作用于 division 代数的一维表示；也不作用于其他深度零类型。无穷处权二 Jacquet–Langlands 表示平凡。

Pi Proposition 5.1 因而给

$$\boxed{
J(f)=\frac{2\mathcal L_a^2}{pa\sqrt D}
\sum_{g\in\mathcal F_\theta(p^2)}
\frac{L(\tfrac12,\pi_{g,K}\otimes\Omega)}{L(1,\pi_g,\operatorname{Ad})}.
} \tag{213.7}$$

所有 $L$ 函数、测度都沿用该文的完成函数归一化。这里用到 $\mathrm N\mathfrak f(\Omega)=p^2a^2$，及 $S'(\Omega)$ 恰为 $a$ 的素支集。式 (213.7) 的前因子严格正；等价的谱分解是正权的环面周期平方和。不存在把“根数 $+1$”当成非消失的步骤。

### 3.2 正主项逐处匹配

记 $T_q=\mathbb Q_q^{\times}\backslash K_q^{\times}$。Pi Lemma 6.1 给 $p$ 处 singular 项

$$I_p(0,f_p)=\operatorname{vol}(T_p)=1.$$

这是 (213.6) 和 $\Omega_p$ 抵消后的完整环面积分，不是只积单位商。无穷处为二；其余有限处为相应环类序单位商体积。因此

$$I(0,f)=\frac{2\mathcal L_a}{a\sqrt D}.$$

全局环面商体积为 $2L(1,\chi_K)$，故

$$I_{\rm irreg}(f)=\frac{4L(1,\chi_K)\mathcal L_a}{a\sqrt D}. \tag{213.8}$$

没有另一个 $\infty$ singular 轨道，因为 $\Omega^2\ne1$，在 $p$ 已可检测。又因三次子角色 $\eta$ 非平凡，$K=\mathbb Q(i),\mathbb Q(\sqrt{-3})$ 时必有 $c>1$，从而 $a>1$。所以始终有 $\mathcal O_a^{\times}=\{\pm1\}$。若 $u_K=|\mathcal O_K^{\times}|/2$，则

$$h=\frac{h_Ka}{u_K\mathcal L_a},\qquad
L(1,\chi_K)=\frac{h_K}{u_K\sqrt D}.$$

代入 (213.8) 得准确主项

$$\boxed{I_{\rm irreg}(f)=\frac{4h\mathcal L_a^2}{M}.} \tag{213.9}$$

### 3.3 $p$ 处 regular 项和全局参数

Pi Lemma 6.2 给

$$I_p(\xi,f_p)=\begin{cases}1,&v_p(\xi)\ge1,\\0,&v_p(\xi)\le0.\end{cases} \tag{213.10}$$

其直接局部理由是把 division 代数写成 $L\oplus L\Pi$，$\Pi^2=p$。regular 代表具有形式 $1+\Pi z x$，其中 $z\bar z=1$，而 $\xi=p x\bar x$。当 $v_p(\xi)\ge1$，该代表属于 $U_B^1$，矩阵系数值为一；其他环面变量的相位恰被 $\Omega_p$ 抵消。否则不在 (213.6) 的支集中。

结合该文 Lemma 6.3，所有可能贡献的 global regular 参数满足

$$\xi<0,\quad v_p(\xi)\ge1,\quad M/(1-\xi)\in\mathbb Z.$$

等价地，它们都在下面的有限整数族中：

$$\boxed{\xi=\frac{y}{y-M},\qquad0<y<M,\qquad p\mid y.} \tag{213.11}$$

仍需满足全局范数条件的实际参数只占子集。对全部这些 $y$ 取绝对值上界是合法的扩大；特别 $p\ge M$ 时 regular 族为空，立即给稳定范围内的非消失，与 Pi Theorem 1.1 的专门化一致。

## 4. 每个局部误差中保留变化域依赖

对 $q\mid D$，自对偶测度给 $\operatorname{vol}(T_q)=2q^{-v_q(D)/2}$。相应单位测试的绝对值不超过一，故直接双重积分给

$$|I_q(\xi)|\le4q^{-v_q(D)}. \tag{213.12}$$

这对二进分歧也成立；没有使用未给出的 $C(K_q,\mathbb Q_q)$。在 $p$ 处由 (213.10) 上界为一，在无穷处上界为四。

对 $q\nmid Dap$，置 $r_q=v_q(y)$、$t_q=v_q(M-y)$。其最小值为零。Pi Lemmas 6.4–6.5 的惰性上界为一，分裂上界不超过

$$1+|r_q-t_q|\le(r_q+1)(t_q+1).$$

对 $q\mid a_0$，置 $n_q=v_q(a)$、$L_q=(1-\chi_K(q)/q)^{-1}\le2$ 及

$$j_q=\min(v_q(y),2n_q).$$

Pi Lemma 6.6 在未分歧二次代数的常数恰为一，给与 R87 §4.4 相同的有限权：

$$B_q(j)=\begin{cases}
L_q^2q^{-2n_q+j/2},&0\le j<2n_q,\\
L_qq^{-n_q},&j=2n_q.
\end{cases}$$

末项容许另乘 $(r_q+1)(t_q+1)$。由各素数支集互不交，所有这些因子可一起包进一个除数函数乘积，得到

$$\boxed{|I(\xi_y,f)|\le
\frac{4\,4^{\omega(D)}}D\tau(y)\tau(M-y)
\prod_{q\mid a_0}B_q(j_q).} \tag{213.13}$$

以上局部界只使用中心平凡和准确导子，没有三次阶数限制；字符阶及其在 $p$ 的分歧已由真正的 (213.6) 处理。

## 5. 独立的整数倍计数

固定全部 $j_q$ 后，每个允许的 $y$ 都是

$$p\prod_{q\mid a_0}q^{j_q}$$

的正整数倍。因此位于严格区间 $(0,M)$ 内的数目至多

$$M\Big/\left(p\prod_{q\mid a_0}q^{j_q}\right).$$

这个进程通过零点，没有可遗漏的平移或单元素 $+1$。对 (213.13) 分层求和得到

$$|I_{\rm reg}(f)|\le
\frac{4\,4^{\omega(D)}M\mathcal T(M)^2}{Dp}
\prod_{q\mid a_0}\sum_{j=0}^{2n_q}q^{-j}B_q(j).$$

逐素数有

$$\begin{aligned}
\sum_{j=0}^{2n}q^{-j}B_q(j)
&=q^{-2n}\left(L_q^2\sum_{j=0}^{2n-1}q^{-j/2}+L_qq^{-n}\right)\\
&\le q^{-2n}\left(\frac4{1-1/\sqrt2}+1\right)<16q^{-2n}.
\end{aligned}$$

从而

$$\boxed{|I_{\rm reg}(f)|\le
\frac{4a_D^2\,4^{\omega(D)}16^{\omega(a_0)}\mathcal T(M)^2}{p}.} \tag{213.14}$$

(213.1) 使 (213.9) 严格大于 (213.14)，所以 $J(f)>0$。由 (213.7)，存在非零中心值。$\Omega=\Xi^{-1}$ 与 $\Xi$ 的基变换 $L$ 函数相同：$\pi_{g,K}$ 在 $\operatorname{Gal}(K/\mathbb Q)$ 下不变，而中心平凡角色满足 $\Xi^\sigma=\Xi^{-1}$。这证明 (213.2)。

R181 的二次自扭曲论证说明：平凡中心角色、水平 $p^2$ 的 CM 新形式若有这种深度零类型，其有限参数只能为阶四。因此 $r>4$ 时所找到的 $g$ 自动非 CM。定理 213.1 得证。

## 6. 有效统一常数与共同导子

沿用 R87 §7 的完全显式有限积：对 $u>0$，

$$T_u=\prod_{q\le2^{1/u}}\max_{e\ge0}(e+1)q^{-ue},\quad
X_u=16^{\pi(16^{1/u})},\quad
\beta_u=\prod_{q\le2^{1/u}}(1-1/q),$$

所有乘积均取素数。逐素数估计给

$$\mathcal T(M)^2\le T_{\epsilon/8}^2M^{\epsilon/4},$$

$$4^{\omega(D)}16^{\omega(a_0)}\le X_{\epsilon/4}M^{\epsilon/4},$$

$$\mathcal L_a^{-2}\le\beta_{\epsilon/2}^{-2}M^{\epsilon/2}.$$

因 $a_D\mid36$，(213.1) 的右侧不超过

$$1296X_{\epsilon/4}T_{\epsilon/8}^2\beta_{\epsilon/2}^{-2}M^{1+\epsilon}/h.$$

故可取

$$\boxed{C_\epsilon=2592X_{\epsilon/4}T_{\epsilon/8}^2\beta_{\epsilon/2}^{-2}.} \tag{213.15}$$

多出的因子二确保非严格 (213.3) 仍推出严格 (213.1)。若 $a=c$，使用 $a_D\mid9$，系数改为 $162$。

令 $a^*=bc$、$M^*=D(a^*)^2$。所有角色共享一个更易陈述的充分条件：

$$p\ge C_\epsilon(M^*)^{1+\epsilon}/h(\mathcal O_{a^*}). \tag{213.16}$$

确实，环类数公式给

$$\frac{(Da^2)^{1+\epsilon}}{h(\mathcal O_a)}
=\frac{u_KD^{1+\epsilon}}{h_K}\,a^{1+2\epsilon}\mathcal L_a.$$

在 $a\mid a^*$ 下，右侧单调不减：已有素数增加指数显然增大；新增素数 $q$ 的比值为 $q^{1+2\epsilon}/(1-\chi_K(q)/q)>1$。故 (213.16) 对每个参数均推出 (213.3)。这是一条对全部参数统一的逐个存在性陈述，不需要额外乘参数数目。

此处不会在 $a=1$ 发生遗漏单位指标的跳变：§3.2 已利用实际三次子角色证明全部 $a\ge c$ 和 $a^*$ 都满足 $u_a=u_{a^*}=1$。若 $K$ 为有额外单位的两个域，则 $c>1$；其余域从极大序起就只有 $\pm1$。

## 7. 推论及仍然缺少的全局输入

普通 Siegel 下界与环类数公式给 $h(\mathcal O_a)\gg_\delta M^{1/2-\delta}$，常数对变化的 $K,a$ 统一但一般无效。因此对每个 $\nu>0$，存在绝对、一般无效的 $C'_\nu$ 使

$$p\ge C'_\nu M^{1/2+\nu}$$

推出每个指定实际类型的中心非消失；$r>4$ 时同样得到非 CM 新形式。

这里没有给 $M$ 或 $M^*$ 的上界。在 $r=4$ 上必须去掉 CM 谱后再次证明正贡献；仅有非 CM 类型空间的正维数不能完成这一步。即使结合全部非 CM 秩零商得出某个范围内的 $j$ 整性，整 $j$ 的实际异常曲线仍须另外排除。本定理不满足主题 README 的主目标完成标准。

## 来源与使用范围

- Qinghua Pi, *Central values of twisted base change L-functions associated to Hilbert modular forms*, **Journal of Number Theory 191** (2018), 213–245，[原刊 DOI](https://doi.org/10.1016/j.jnt.2018.03.005)，[作者稿 arXiv:1707.07307v2](https://arxiv.org/abs/1707.07307)。本文所列编号按作者稿：§2.3–2.4 的测度与迹公式、式 (3.1)、Propositions 3.1/5.1、Lemmas 6.1–6.6、式 (7.1)。使用已经发表的局部、谱和主项公式；全球变化域误差由本文 §4–5 独立给出。
- R87：同一测度的体积、环类数表达和有限乘积常数；本篇重新写出针对实际在 $p$ 分歧角色所需的计数。
- R166 §4、§6；R181：实际基本特征取向、完整局部类型和阶四 CM 边界。
- R214：transfer 中心平凡性、准确 prime-to-$p$ 导子 $a=c$ 或 $bc$ 及 $a_D\mid36$。此处不使用错误的整个比值 $bc/c\mid36$。
