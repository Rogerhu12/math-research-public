# R716 — 原 S34 的 wild 全局 theta 周期与精确中央 L 值

日期：2026-11-15。**状态：以下原固定来源、全部有限 Schwartz 向量、绝对 Heisenberg 位移、全局环面字符及平方常数已证明。新身份识别的是随惰性素数 p 变化、导子恰为 p²、阶恰为 p 的一族真正 Hecke 中央值。它没有证明这些中央值非零，也没有把原 p-adic 中央导数为零推出本族中央值为零。主目标仍未完成。**

本篇只处理原曲线
$$
E:y^2=x^3+17,\qquad K=\mathbf Q(\omega),\qquad
\delta=1+2\omega,\qquad \omega=e^{2\pi i/3}.
$$
保持 R290、R298 的解析微分 $dz=dx/(2y)$、原 Hecke 角色 $\psi=\psi_{17}$、原来源
$$
S(z)=\sigma(z)^{34}\phi(z),\qquad
\phi=x^2\left(x^{12}-\frac{53b}{7}x^9
-\frac{12b^2}{7}x^6-\frac{80b^3}{7}x^3-\frac{128b^4}{7}\right),
\quad b=17.
\tag{1}
$$
特别 $S(z)=z^6+O(z^{12})$。本篇不替换 (1) 的固定多项式。

## 1. 原 Hall 和与结论

令
$$
p\equiv5\pmod6,\qquad p>101,\qquad d=p+1,\qquad q=p^2.
$$
设 $\Omega_{\mathbf R}>0$ 是原 primitive 实周期，并置
$$
s_0=(1-\omega)^{-1}=\frac{3+\delta}{6},\qquad
\Omega_{\rm CM}=s_0\Omega_{\mathbf R},\qquad
\operatorname{Per}(E,dz)=\Omega_{\rm CM}\mathcal O_K.
$$
R703 的幅度在本篇明确使用这个 CM 生成周期：
$$
\mathcal A(v)=
\mathfrak k(\Omega_{\rm CM}v)^{34}
\phi(P(\Omega_{\rm CM}v)),\qquad
\mathfrak k(z)=e^{-\eta_z z/2}\sigma(z).
\tag{2}
$$
极点在 (2) 中已被 $\sigma^{34}$ 消去，格点处仍为零阶六。

对 $v\in(\mathcal O_K/p^2)^\times$ 定义
$$
q_p(v)=\frac{v^p/\bar v-1}{p}\pmod p,\qquad
\chi_{p,r}(v)=
e_p\!\left(\operatorname{Tr}_{\mathbf F_{p^2}/\mathbf F_p}
 \frac{34r}{2\delta}q_p(v)\right),
\quad r\in\mathbf F_p^\times.
\tag{3}
$$
这是 R705 的同一个字符，不是另选的 Gauss 相位。它满足
$$
\chi_{p,r}(\bar v)=\chi_{p,r}(v)^{-1},\qquad
\chi_{p,r}(1+p\delta t)=e_p(34rt),
\tag{4}
$$
并且在 Teichmüller 单位和 $\mathbf Z_p^\times$ 上平凡。其导子恰为 $p^2$、阶恰为 $p$。

对 $v=a+b_0\omega\bmod p$，仍取 R703 的整数代表 $0\le a,b_0<p$。定义
$$
\mathscr S_p(r)=
\sum_{\substack{v\bmod p\\N(v)=r}}
 \chi_{p,r}(v)\mathcal A(v/p).
\tag{5}
$$
在 $N(v)=r$ 上，(3) 正是 R703 的 $e_p(\tau_{34}(v))$，所以 (5) 是已支付完整 $p^2$ 相位的原 Hall 和。

记 $T=K^1$ 为范数一环面。下文定义一个唯一的全局有限阶字符
$$
\eta_{p,r}:T(\mathbf A)/T(\mathbf Q)\longrightarrow\mu_p
\tag{6}
$$
使其在 $T(\mathbf Z_p)$ 上为 $\chi_{p,r}|_T$，在其余有限极大紧子群及无穷环面上平凡。置
$$
\widetilde\eta_{p,r}(z)=\eta_{p,r}(z/\bar z).
\tag{7}
$$
**真实 Hecke twist 是 (7)，其 p 地点为 $\chi_{p,r}^2$，不能漏掉这个平方。**

准确的原来源身份为
$$
\boxed{
\frac{L(\psi\,\widetilde\eta_{p,r},1)}{\Omega_{\mathbf R}}
=\frac{48940416}{p}\,|\mathscr S_p(r)|^2.
}
\tag{8}
$$
全部 $r\ne0$ 都适用；没有挑一个有利测试向量后再将其冒认为 (5)。

角色 $\psi\widetilde\eta_{p,r}$ 的无穷型仍为 $(1,0)$，原 $2,3,17$ 分量不变，新增有限导子为 $(p^2)$，所以总导子是
$$
(2\delta\cdot17\cdot p^2).
\tag{9}
$$
它的全局根号为 $+1$。式 (8) 允许中央值为零。

## 2. 不改变的原有限向量

使用 R290 的原全局 Schwartz 向量
$$
\Phi=\Phi_\infty\otimes\Phi_2\otimes\Phi_3
       \otimes\Phi_{17}\otimes\bigotimes_{\ell\ne2,3,17}\mathbf1_{\mathbf Z_\ell},
\qquad
\Phi_\infty(x)=e^{-\pi\,51\sqrt3\,x^2}.
\tag{10}
$$
所有加性角色保持
$$
\psi_{{\rm add},\infty}(x)=e^{2\pi ix},\qquad
\psi_{{\rm add},\ell}(x)=e^{-2\pi i\{x\}_\ell}.
$$
二处设
$$
e_j=\mathbf1_{j/2+2\mathbf Z_2},\qquad
t_2=\frac{1+\sqrt3}{\sqrt2},\qquad
\Phi_2=e_0+t_2e_1-e_2+t_2e_3.
\tag{11}
$$
三处
$$
\Phi_3=\mathbf1_{3^{-1}\mathbf Z_3}.
\tag{12}
$$
十七处是 R290 的整条原有限环面特征向量
$$
\Phi_{17}=\sum_{j\bmod17} f_{17}(j)
                 \mathbf1_{j/17+\mathbf Z_{17}}.
\tag{13}
$$
这里 $f_{17}$ 正是 R290 的 $\mathbf F_{289}^1$ 特征 $g\mapsto g^{12}$ 的向量，范数平方为 $9(17-\sqrt{17})$。没有改成任意十七处向量。二处范数平方为 $3+\sqrt3$，三处为 $3$；总范数平方是
$$
\mathcal N_0=
\frac{27(3+\sqrt3)(17-\sqrt{17})}{\sqrt{102\sqrt3}}.
\tag{14}
$$

对有理 Heisenberg 位移，固定
$$
(\rho_v(t,\xi)f)(x)=
\psi_{{\rm add},v}\bigl(\xi(x+t/2)\bigr)f(x+t).
\tag{15}
$$
于是
$$
\rho_v(t,\xi)\rho_v(t',\xi')
=\psi_{{\rm add},v}\bigl((t\xi'-t'\xi)/2\bigr)
 \rho_v(t+t',\xi+\xi').
\tag{16}
$$
这支付后面所有中心相位。

## 3. 原复幅度的精确 Heisenberg 表示

R290 的完整 Fourier 来源为
$$
F(Z)=\sum_{n\in\mathbf Z}a_n
 \exp\!\left(-\frac{\pi\sqrt3}{204}n^2+2\pi inZ\right),
\quad
a_n=v_2(n\bmod4)f_{17}(3n\bmod17).
\tag{17}
$$
R298 给出同一固定非零实数 $C$，使
$$
e^{34\sqrt3\pi Z^2}F(Z)=C\,S(\Omega_{\mathbf R}Z),
\qquad
C_{17}^{(0)}C^2=48940416\,\Omega_{\mathbf R},
\tag{18}
$$
其中
$$
C_{17}^{(0)}
=\frac{\pi\sqrt{102\sqrt3}}
 {153\sqrt3(3+\sqrt3)(17-\sqrt{17})}.
\tag{19}
$$
$C$ 的正负不影响 (8)，但没有逐 p 更换 $C$。

写 $v=x+y\omega$，其中 $x,y$ 暂为实数。因为
$$
s_0v=\frac{x-y}{2}+\frac{\delta(x+y)}6,
$$
原 Klein 修正和 (18) 逐项给
$$
C\mathcal A(v)=
e^{\pi i\,17(x^2-y^2)}
\sum_n a_n e^{\pi in(x-y)}
 \exp\!\left[-\frac{\pi\sqrt3}{204}
                   \{n+34(x+y)\}^2\right].
\tag{20}
$$
这里使用的是原格的 $\eta_1=2\sqrt3\pi$；非全纯修正并未删掉。

设
$$
h(v)=(t(v),\xi(v))
=\left(\frac{x+y}{3},\,51(x-y)\right).
\tag{21}
$$
原有限支撑为 $n/102$，故由 (15) 直接得到
$$
\boxed{
C\mathcal A(v)
=\Theta\bigl(\rho_\infty(h(v))\Phi_\infty\otimes\Phi_f\bigr),
\qquad
\Theta(\varphi)=\sum_{x\in\mathbf Q}\varphi(x).
}
\tag{22}
$$
完成平方中的平移、调制、半中心项分别为
$n+34(x+y)$、$e^{\pi in(x-y)}$ 和 $e^{\pi i17(x^2-y^2)}$。
所以 (22) 不是由有限维唯一性猜出的比例。

### 3.1 全部非 p 地点的位移确实固定原向量

取 $v=a+b_0\omega$ 为整数，使用 $h(v/p)$。

- 在 $3$ 处，$t\in3^{-1}\mathbf Z_3$，$\xi\in3\mathbf Z_3$。平移保 (12)，调制及半中心均为一。
- 在 $17$ 处，$t\in\mathbf Z_{17}$，$\xi\in17\mathbf Z_{17}$。每个 (13) 的陪集分别保持，调制及半中心均为一。
- 在 $2$ 处，$t,\xi\in\mathbf Z_2$ 且 $t\equiv\xi\bmod2$。若同为偶数，(11) 逐项保持；若同为奇数，平移交换 $e_0/e_2$、$e_1/e_3$，调制与半中心在第 $j$ 陪集给 $(-1)^{j+1}$，仍准确恢复 $(1,t_2,-1,t_2)$。
- 在其余 $\ell\ne p$，$t,\xi\in\mathbf Z_\ell$，原标准球保持。二处已经单独处理，因此未遗漏 $1/2$ 中心。

全局 theta 分布对有理 Heisenberg 位移不变；这是对 $\mathbf Q$ 的求和换元及全局加性角色在 $\mathbf Q$ 上平凡。因此 (22) 变成
$$
\boxed{
C\mathcal A(v/p)=
\Theta(\Phi^p\otimes e_v),\qquad
e_v=\rho_p(-h(v/p))\mathbf1_{\mathbf Z_p}.
}
\tag{23}
$$
$\Phi^p$ 表示 (10) 中除 p 外的全部原因子。

## 4. p² 原模型、绝对 Weil 定标与真实本征向量

令
$$
\mathcal V_p=\{f:\operatorname{supp}f\subset p^{-1}\mathbf Z_p,\
                      f(x+py)=f(x)\ (y\in\mathbf Z_p)\}.
$$
在自对偶测度 $\operatorname{vol}(\mathbf Z_p)=1$ 下，(23) 的 $p^2$ 个
$e_v$（$v\bmod p$）是正交范数一基。

确实，两个 Heisenberg 平移的内积非零，必须同时有平移差与调制差属于 $\mathbf Z_p$。矩阵
$$
\begin{pmatrix}1/3&1/3\\51&-51\end{pmatrix}
$$
的行列式为 $-34$，在本篇 p 处是单位，所以这恰好要求两 $v$ 模 p 相同。

对 $\ell\in\mathcal O_K$，(16) 给
$$
e_{v+p\ell}=e_p\!\left(\frac{34}{2}[\ell,v]\right)e_v,
\qquad
[\ell,v]=\frac{\bar\ell v-\bar v\ell}{\delta}.
\tag{24}
$$
另一方面，R703/R705 的同一个原字符在 $N(v)=r$ 上满足
$$
\chi_{p,r}(v+p\ell)
=e_p\!\left(-\frac{34}{2}[\ell,v]\right)\chi_{p,r}(v).
\tag{25}
$$
所以每个 $\chi_{p,r}(v)e_v$ 与代表选择无关。

R290 使用的原环面嵌入为
$$
\iota_{17}(a+b\delta)=
\begin{pmatrix}a&153b\\-b/51&a\end{pmatrix}.
\tag{26}
$$
直接代 (21) 得
$$
h(gv)=\iota_{17}(g)^{-{\rm t}}h(v)\qquad(Ng=1).
\tag{27}
$$
在 (15) 的 Schrödinger 规范中，Weil 协变正是 $g^{-{\rm t}}$ 对
$(t,\xi)$ 的作用。因此 (27) 是完整原极化的匹配，不是把另一个有限环面同构代入。

p 是原好非分裂地点；原 $\chi=\psi|\cdot|_K^{-1/2}$ 在 p 未分歧，
$\alpha=17$ 为单位。Yang Lemma 2.7 给
$\omega_{17,\chi,p}(g)\mathbf1_{\mathbf Z_p}=\mathbf1_{\mathbf Z_p}$。
它确定绝对 splitting，遂有
$$
\boxed{\omega_{17,\chi,p}(g)e_v=e_{gv}\quad(g\in K_p^1).}
\tag{28}
$$
当 $g\equiv1\bmod p^2$ 时，(24) 的实际平移和相位都平凡，故这确实给 R705 的整个模 $p^2$ 环面，而不是仅模 p 的作用。

定义
$$
\varphi_{p,r}=\frac1{\sqrt{p+1}}
 \sum_{\substack{v\bmod p\\N(v)=r}}\chi_{p,r}(v)e_v.
\tag{29}
$$
正交性、(24)–(28) 给
$$
\boxed{
\|\varphi_{p,r}\|=1,\qquad
\omega_{17,\chi,p}(g)\varphi_{p,r}
=\chi_{p,r}(g)^{-1}\varphi_{p,r}.
}
\tag{30}
$$
由 (23)，其原 theta-null 精确为
$$
\boxed{
\Theta(\Phi^p\otimes\varphi_{p,r})
=\frac{C}{\sqrt{p+1}}\mathscr S_p(r).
}
\tag{31}
$$
这同时支付原有限 Weil 与全局 Schwartz 之间的相位和范数。

## 5. 全局字符、导子、根号与紧商

因为 $h_K=1$，任意范数一 idèle 可乘一个全局范数一元素，令所有有限分量为单位：在分裂素处取所需主理想生成元与其共轭之比即可。
两个这种选择之商属于 $\mathcal O_K^\times=\mu_6$。

(3) 在 $\mu_6$ 上平凡，所以对紧代表 $t^{\rm c}$ 定义
$$
\eta_{p,r}(t)=\chi_{p,r}(t_p^{\rm c})
\tag{32}
$$
与选择无关。它在无穷环面和其余有限紧子群上平凡，唯一地给 (6)。
在好分裂地点，其全环面分量可以是非平凡的**未分歧**字符；
本篇没有将这些分量全称为平凡。

由 (4)，$\eta_{p,r}$ 阶为 p，p 地点导子指数为二。又
$$
\widetilde\eta_{p,r,p}(v)
=\chi_{p,r}(v/\bar v)=\chi_{p,r}(v)^2,
\tag{33}
$$
所以真正 Hecke 角色 (7) 仍恰有导子 $p^2$、阶 p。
其在 $2,3,17$ 处整个分量均平凡，原坏点角色一项未改。

在 p 地点，(29)–(30) 已给实际 Hermitian 类 $\alpha=17$ 中的非零
$\bar\eta_{p,r,p}$ 本征向量。因此 Yang 的局部 theta/epsilon dichotomy
在这里成立，而不必猜一个局部 Gauss 根号。
在其他非分裂地点沿用 R290 原向量及原 dichotomy；分裂地点的条件自动成立；无穷处仍是原零阶 Hermite Gaussian。
故所有局部类仍是同一个全局 $\alpha=17$，相乘得到全局根号 $+1$。

设
$$
\Phi_r=\Phi^p\otimes\varphi_{p,r}.
$$
它的总范数平方仍是 (14)。在无穷及有限紧子群上，
$\omega_{17,\chi}(t)\Phi_r=\bar\eta_{p,r}(t)\Phi_r$。
紧子群满射到 $T(\mathbf Q)\backslash T(\mathbf A)$，核恰为 $\mu_6$，
因此 Yang 的 theta 积分在单位点是 (31) 乘原商体积。
没有多出一个未处理的理想类平均。

## 6. 完整平方常数

对 $\Phi_r/\sqrt{\mathcal N_0}$，Yang Theorems 2.6、2.15 的良好向量条件成立。

在好分裂点，$\chi\widetilde\eta$ 仍未分歧，原标准球由
Corollary 2.14 保持适用；虽然其未分歧参数会变化，这不改变向量或范数。
非分裂 p 地点使用 (29) 的范数一向量。
相对于 R290，Theorem 1.11 的分歧非分裂集合从 $\{2,17\}$ 变成
$\{2,17,p\}$，故
$$
c_{p,r}(0)=
(1+2^{-1})^{-1}(1+17^{-1})^{-1}(1+p^{-1})^{-1}
=\frac{17}{27}(1+p^{-1})^{-1}.
\tag{34}
$$
这就是新增的原 Euler/局部积分因子，不可删去。

全部其他测度、无穷范数、单位群、$L(1,\epsilon_{K/\mathbf Q})$
与 R290 相同，因而其准确平方公式给
$$
L(\psi\widetilde\eta_{p,r},1)
=C_{17}^{(0)}(1+p^{-1})
 \left|\Theta(\Phi_r)\right|^2.
\tag{35}
$$
代入 (18)、(31)：
$$
C_{17}^{(0)}(1+p^{-1})\frac{C^2}{p+1}
=\frac{48940416\,\Omega_{\mathbf R}}p.
$$
这证明 (8)。最后一步的 $p^{-1}$ 同时使用了
p 地点的良好向量因子及原范数为 $p+1$ 的完整 Hall 轨道，
并非只用一个根号或有限特征识别。

## 7. 原全 H 迹及边界的准确算术意义

保持 R696/R703 的原点 $T_v$、原根 $w_v$、Hall 子群及原迹
$$
\mathcal T_{34,T_v}
=\operatorname{Tr}_{W/W^{\widetilde H}}
       (w_v^{-34}\phi(T_v)).
$$
R703 (20) 给它与 (5) 只差已指定的模一因子。因此
$$
\boxed{
\frac{L(\psi\widetilde\eta_{p,r},1)}{\Omega_{\mathbf R}}
=\frac{48940416}{p}\,|\mathcal T_{34,T_v}|^2,
\qquad r=N(v)\bmod p.
}
\tag{36}
$$
R696 的准确非零乘子又把这个迹接到同一个
$\mathcal B_{34}(v_T^{p+1})$，所以
$$
\boxed{
\mathcal B_{34}(v_T^{p+1})=0
\iff \mathcal T_{34,T_v}=0
\iff L(\psi\widetilde\eta_{p,r},1)=0.
}
\tag{37}
$$
这是原固定 $\phi$ 的身份，不是任意 forcing 的表示。
所有 $r\ne0$ 对应同一阶 p 角色的非平凡幂；原全局 Galois 作用
也保持 (37) 的零/非零。可以使用 R707/R708 已证明的原高度及前缀结论，
但不能把它们误作 (37) 某一端已非零。

## 8. 与原目标之间仍须支付的两件事

第一，(37) 的中央 L 值属于一族**变化的** Hecke 角色；
不是固定 $\psi$ 自己的中央值，也不是原 $j_{34}$。
本篇没有将
$$
j_{34}=0
$$
变成 (37) 的任一项为零。R710 已说明，同一中央连接和整性本身
仍容许非零边界余数；原固定来源的额外限制不能省去。

第二，已检视的 Rohrlich 固定反循环塔定理，以及 Jia 对它的推广，
固定一个有限允许分歧素数集，结论是该固定塔中除有限多个角色外
具有最小允许消失阶。这里却令惰性 p 变化，并只取每个 p 的
第一个 wild 导子 $p^2$、tame 部分平凡的 p−1 个字符。
固定塔的有限例外数没有在所引定理中给出可覆盖这个量词的统一界。
所以本篇不从固定塔非消失推出 (8) 对无穷多个 p 非零。

本篇新支付的是：原固定幅度的完整 wild toric projection 恰是哪一个
全局周期，以及其全部实际角色、导子、根号、坏点向量和常数。
没有用可任选测试向量的存在性替换原幅度。

## 依赖与原始文献

- [R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)：原 Hermitian 类、全部有限 Schwartz 向量、全局极化与平方测度。
- [R298](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md)：原固定 S34、全部周期及 $\kappa_0=48940416$。
- [R703](R703-original-hall-phase-and-finite-fourier-return.md)、[R705](R705-original-wild-character-and-absolute-weil-projection.md)：完整原 Hall 相位、$p^2$ 字符及有限表示。第3–6节另付它们与全局原向量的准确匹配。
- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)、[R707](R707-original-theta-average-and-three-quarter-trace-height.md)：同一个原迹、所有共轭及原高度。
- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)、[R710](R710-original-all-order-central-kernel-and-exact-boundary-remainder.md)：原边界和完整中央连接；本篇不增加其消失假设。
- T. Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew. Math. **485** (1997), 25–53，Lemma 1.2、Theorem 1.11、Corollary 2.4、Lemma 2.7、Corollary 2.14、Theorems 2.6、2.15；[作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。本篇第4–6节对其良好向量逐处核对。
- H. Jia, *On L-functions of Hecke characters and anticyclotomic towers*, arXiv:2412.05867v1 (2024)，Introduction、Theorem 1；[作者全文](https://arxiv.org/html/2412.05867v1)。这里只核对固定有限分歧集合的量词，未将其作为本族非消失输入。

本篇没有数值扫描，没有新增可重算数据文件。
