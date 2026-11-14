# R227：坏二进位的正 Hecke 滤波及整个 p≡3 mod8 分支的平方根范围

日期：2026-11-13。

**状态：已证明。** 在 R213 的同一个实际阶四参数上，把二进位的 Gross–Prasad 极大序测试函数换成相对于该极大序的正 Hecke 卷积。允许 $2\mid D$ 或 $2\mid a$。因此在 $p\equiv3\pmod8$ 时，不必选择随 $p$ 增长的小二次非剩余，即可杀掉全部 CM 谱。本文保留准确的实际角色、共轭测试向量、singular 主项、regular 支集和统一误差。

## 1. 对象与结论

保留 R213/R215 的实际小惯性设置，参数 $\theta$ 的阶为四，并加上

$$p\equiv3\pmod8.$$

令 $\Omega=\Xi^{-1}$，$a$ 为准确 prime-to-$p$ 环类导子，并记

$$M=Da^2,\quad h=h(\mathcal O_a),\quad
\mathcal L_a=\prod_{q\mid a}(1-\chi_K(q)/q)^{-1},$$

$$a_D=\prod_{q\mid D}q^{v_q(a)}\mid36,\qquad
a_0=a/a_D,\qquad e=v_2(a_0),\qquad a_{0,\mathrm{odd}}=a_0/2^e.$$

R214 给出 $v_2(a)\le3$；若 $2\mid D$，则 $v_2(a)\le2$。所以始终 $0\le e\le3$。仍记

$$\mathcal T(X)=\max_{1\le m<X}\tau(m).$$

**定理 227.1。** 若

$$\boxed{
p>2160\,2^{2e}\,
\frac{a_D^2\,4^{\omega(D)}16^{\omega(a_{0,\mathrm{odd}})}
\mathcal T(4M)^2M}{h\mathcal L_a^2},
} \tag{227.1}$$

则存在非 CM 的 $f\in\mathcal F_\theta(p^2)$，满足

$$\boxed{a_2(f)\ne0,\qquad
L(\tfrac12,\pi_{f,K}\otimes\Xi)\ne0.} \tag{227.2}$$

还有不含任何除数函数的稳定充分条件

$$\boxed{p\ge4M\quad\Longrightarrow\quad(227.2).} \tag{227.3}$$

**定理 227.2。** 对每个 $\epsilon>0$，有完全有效且与 $K,a,p,\theta$ 无关的常数 $C_\epsilon^{(2)}$，使

$$\boxed{p\ge C_\epsilon^{(2)}M^{1+\epsilon}/h
\quad\Longrightarrow\quad(227.2).} \tag{227.4}$$

沿用 R213 的有限积常数，可以取

$$\boxed{C_\epsilon^{(2)}=
358318080\,X_{\epsilon/4}T_{\epsilon/12}^{\,2}\beta_{\epsilon/4}^{-2}.} \tag{227.5}$$

因此对每个 $\nu>0$，有绝对、一般无效的 $C'_\nu$，使

$$p\ge C'_\nu M^{1/2+\nu}$$

推出 (227.2)。无效性只来自变化二次域的 Siegel 下界。

## 2. 同一共轭极大序上的正卷积

写 $G=\mathrm{PGL}_2(\mathbb Q_2)$。令 $R$ 为 R213/Pi 在二进位选取的 Gross–Prasad 极大序，满足

$$R\cap K_2=\mathbb Z_2+2^n\mathcal O_{K_2},\qquad n=v_2(a).$$

令 $U=R^\times/\mathbb Z_2^\times$，$V=\operatorname{vol}(U)$，并记 $h_j^R$ 为相对于 $U$ 的 Cartan 距离 $j$ 双陪集的特征函数。即选择任何 $g$ 使 $R=gM_2(\mathbb Z_2)g^{-1}$，将标准 $h_j$ 共轭到此处。定义

$$H_2^R=h_2^R+3h_0^R=V^{-1}(h_1^R)^**h_1^R. \tag{227.6}$$

最后一个等式由三正则 Bruhat–Tits 树的长度二路径计数得到，与 R215 相同。它是正卷积；作为函数有 $0\le H_2^R\le3$。

在 R213 的全局测试函数中，仅将二进位的 $h_0^R$ 换成 $H_2^R$，记结果为 $f^{(2)}$。水平 $p^2$ 的每个谱表示在 $2$ 未分歧。其 $U$ 不变直线是标准球面直线的 $\pi_2(g)$ 平移；$h_j^R$ 也是相同的共轭。因此这一替换在**原本被选取的同一测试向量**上准确乘上 $|a_2(f)|^2$，并继续杀死其正交补。没有把一个未共轭的 Hecke 算子施加到分歧环面测试向量上。

于是谱端准确为

$$\boxed{J(f^{(2)})=
\frac{2\mathcal L_a^2}{pa\sqrt D}
\sum_{f\in\mathcal F_\theta(p^2)}
|a_2(f)|^2
\frac{L(\tfrac12,\pi_{f,K}\otimes\Omega)}{L(1,\pi_f,\operatorname{Ad})}.} \tag{227.7}$$

R181 说明全部可能的 CM 谱均来自 $F_p=\mathbb Q(\sqrt{-p})$。因 $p\equiv3\pmod8$，其基本判别式 $-p\equiv5\pmod8$，故 $2$ 在 $F_p$ 惰性。CM 诱导表示在该 Frobenius 上迹为零，所以这些谱项的 $a_2$ 全部为零。证明 $J(f^{(2)})>0$ 即可得出 (227.2)。

## 3. 包含分歧二进位的 singular 主项

令 $T=\mathbb Q_2^\times\backslash K_2^\times$，并令

$$S_j=\mathbb Q_2^\times(\mathbb Z_2+2^j\mathcal O_{K_2})^\times/\mathbb Q_2^\times\subset T.$$

$\Omega_2$ 在 $S_n$ 平凡，且若 $n>0$，在 $S_{n-1}$ 非平凡。原 singular 因子是 $I_2(0,h_0^R)=\operatorname{vol}(S_n)$。下面直接计算替换后的比值

$$A_2=I_2(0,H_2^R)/\operatorname{vol}(S_n).$$

### 3.1 $n=0$

若 $K_2/\mathbb Q_2$ 是未分歧二次域，整个 $T=S_0$ 固定相应顶点，因而 $h_2^R|T=0$，得到 $A_2=3$。

若 $K_2/\mathbb Q_2$ 分歧，$T$ 分成 $S_0$ 与二次域一致化元乘 $S_0$ 两个陪集。它们在树上的位移分别为零与一，故 $h_2^R|T=0$，仍有 $A_2=3$。这一步包含剩余特征二，不使用只在奇剩余特征下陈述的 regular 轨道公式。

若 $K_2=\mathbb Q_2\times\mathbb Q_2$，写 $\Omega_2(x,y)=\chi(x/y)$ 和 $z=\chi(2)$。距离二与环面的交是赋值 $2,-2$ 两个单位陪集。因此

$$A_2=3+z^2+z^{-2}\ge1.$$

### 3.2 $n>0$

在两种域情形，环面中 Cartan 距离二的集合恰为 $S_{n-1}\setminus S_n$。可以直接用 $\mathcal O_{K_2}=\mathbb Z_2[\tau]$ 核准：若 $t=u+v\tau$，相应距离为

$$v_2(Nt)-2\min(v_2(u),v_2(2^{-n}v)). \tag{227.8}$$

单位壳 $v_2(v)=n-1$ 恰给距离二。未分歧情形 $n=1$ 时，整个 $S_0\setminus S_1$ 均在这个距离；分歧情形非单位陪集的距离为 $2n+1\ge3$，不作贡献。

分裂情形可以取对角环面及

$$g_n=\begin{pmatrix}2^n&1\\0&1\end{pmatrix},\qquad
R=g_nM_2(\mathbb Z_2)g_n^{-1}.$$

于是对 $t=\operatorname{diag}(u,1)$，距离等于

$$v_2(u)-2\min\{v_2(u),v_2(u-1)-n,0\}.$$

若 $v_2(u)\ne0$，其值为 $|v_2(u)|+2n\ge3$；若 $u$ 为单位，其值为 $2\max(n-v_2(u-1),0)$。所以距离二同样恰为 $S_{n-1}\setminus S_n$。这里不存在分裂二进位的准确导子 $n=1$，因为 $\mathbb Z_2^\times/(1+2\mathbb Z_2)$ 平凡；故这一壳计算与准确导子的最小性完全一致。

由角色正交性，

$$\int_{S_{n-1}\setminus S_n}\Omega_2(t)\,dt
=-\operatorname{vol}(S_n).$$

因此

$$A_2=3-1=2\qquad(n>0).$$

归纳以上全部情况，

$$\boxed{
A_2=\begin{cases}
2,&n>0,\\
3,&n=0,\ K_2\text{ 是域},\\
3+z^2+z^{-2},&n=0,\ K_2\text{ 分裂},
\end{cases}\qquad A_2\ge1.
} \tag{227.9}$$

这些也与 Feigon–Whitehouse Lemmas 4.4–4.6 的一般 Hecke singular 公式逐项相符。$\Omega^2\ne1$ 仍消去第二个 singular 轨道，所以完整主项为

$$\boxed{I_{\rm irreg}(f^{(2)})=
A_2\frac{4h\mathcal L_a^2}{M}
\ge\frac{4h\mathcal L_a^2}{M}.} \tag{227.10}$$

## 4. 支集只将 M 扩大为 4M

FW Lemma 4.11 适用于任意有限素数处的极大序双陪集：若相对 Cartan 距离是 $j$，则原来的 $v_q(Da^2)$ 支集上限只增加 $j$。其证明只用矩阵行列式与积分条件，包含剩余特征二。当前只含 $j=0,2$，故所有 regular 参数满足

$$\xi<0,\qquad v_p(\xi)\ge1,\qquad \frac{4M}{1-\xi}\in\mathbb Z.$$

因此它们都落在

$$\boxed{\xi_y=\frac{y}{y-4M},\qquad0<y<4M,\qquad p\mid y.} \tag{227.11}$$

当 $p\ge4M$ 时无这样的整数，(227.10) 立即给出 (227.3)。此处 $2\mid D$ 或 $2\mid a$ 不会再增加额外导子平方；这些原有指数已经包含在 $M=Da^2$ 中。

## 5. 二进位 regular 积分的统一常数

若 $K_2$ 未分歧且非分裂，$\operatorname{vol}(T)=1$，故

$$|I_2(\xi,H_2^R)|\le3.$$

若 $K_2$ 分歧，写 $d_2=v_2(D)$。同一测度给 $\operatorname{vol}(T)=2\cdot2^{-d_2/2}$，故

$$|I_2(\xi,H_2^R)|\le12\cdot2^{-d_2}. \tag{227.12}$$

这两条都直接使用紧环面体积，允许任意准确二进角色。

剩下分裂情形。使用 §3.2 的 $g_n$，其相对于标准球面顶点的距离恰为 $n$。若一个矩阵在 $H_2^R$ 支集中，树的三角不等式使其相对于标准顶点的 Cartan 距离至多

$$L=2n+2\le8.$$

在对角环面中可取 regular 代表 $\begin{pmatrix}1&\xi\\1&1\end{pmatrix}$。写两环面变量赋值为 $m_1,m_2$，并置 $s=v_2(\xi)$、$k=v_2(1-\xi)$。标准 Cartan 距离为

$$d=m_1+m_2+k-2\min(m_1+m_2,m_1+s,m_2,0). \tag{227.13}$$

令 $N_j(s,k)$ 为此值等于 $j$ 的整数对数目。下面给出对所有 $j\ge0$ 的界，避免将可能很大的 $|k|$ 误计成平方损失。设最低赋值为 $\ell$，则

$$k-j\le\ell\le0,\qquad
\ell-s\le m_1\le\ell+j-k,\qquad
m_2=2\ell+j-k-m_1.$$

若 $\ell$ 不是两端点，最小值必须由中间两个矩阵元达到，因此 $m_1$ 只能取上述区间的端点。利用 $k>0\Rightarrow s=0$、$k=0\Rightarrow s\ge0$、$k<0\Rightarrow s=k$，得到

$$\boxed{N_j(s,k)\le4(j+1)(1+|s|).} \tag{227.14}$$

详细说，若 $k>j$ 则无解；若 $j-k\ge1$，两个端点的全部区间加上内部的至多两个值，给上界 $2(j-k+s+1)+2(j-k-1)$。当 $k\le0$ 代入上述两种恒等关系，该值至多 $4j+2|s|$；当 $k>0$ 则至多 $4j$。若 $j=k$ 只有一个 $\ell$，解数为 $s+1$，也满足 (227.14)。

每个赋值对的两个单位商总体积为一；取绝对值后角色相位不再影响上界。因此

$$\begin{aligned}
|I_2(\xi,H_2^R)|
&\le3\sum_{j=0}^{L}N_j(s,k)\\
&\le6(L+1)(L+2)(1+|s|)\\
&\le540(1+|v_2(\xi)|).
\end{aligned} \tag{227.15}$$

对 (227.11)，置 $r=v_2(y)$、$t=v_2(4M-y)$，则 $1+|v_2(\xi_y)|\le(r+1)(t+1)$。所以 (227.15) 可与其他素数的因子一起包进一份 $\tau(y)\tau(4M-y)$，不需要重复的除数函数。

## 6. 全球整数倍求和

在奇素数处，沿用 R213 的逐处界与权

$$B_q(j)=\begin{cases}
L_q^2q^{-2n_q+j/2},&0\le j<2n_q,\\
L_qq^{-n_q},&j=2n_q,
\end{cases}\quad
L_q=(1-\chi_K(q)/q)^{-1},\quad n_q=v_q(a).$$

在 $2\mid a_0$ 时故意舍去原先的 $B_2$ 权，改用 §5 的统一界；其代价稍后精确留下 $2^{2e}\le64$。结合 (227.12)–(227.15) 及无穷处、$p$ 处的原界，得到

$$|I(\xi_y,f^{(2)})|\le
\frac{4\cdot540\cdot4^{\omega(D)}}D
\tau(y)\tau(4M-y)
\prod_{q\mid a_{0,\mathrm{odd}}}B_q(\min(v_q(y),2n_q)). \tag{227.16}$$

若 $2\mid D$，(227.12) 所多的因子只是 $3$，已被 $540$ 覆盖；若 $2\nmid D$，则 (227.15) 或紧性界直接适用。

固定全部奇素数的层 $j_q$ 后，每个 $y$ 是 $p\prod q^{j_q}$ 的正整数倍，个数至多 $4M/(p\prod q^{j_q})$。R213 的几何级数估计给

$$\sum_{j=0}^{2n_q}q^{-j}B_q(j)<16q^{-2n_q}.$$

于是

$$\boxed{|I_{\rm reg}(f^{(2)})|\le
\frac{16\cdot540\cdot2^{2e}a_D^2
4^{\omega(D)}16^{\omega(a_{0,\mathrm{odd}})}\mathcal T(4M)^2}{p}.} \tag{227.17}$$

与主项 (227.10) 比较，(227.1) 正好使误差严格更小，故 $J(f^{(2)})>0$。式 (227.7) 中所有 CM 项为零，因此存在满足 (227.2) 的非 CM 新形式。$\Omega$ 与 $\Xi$ 的中心值由基变换的 Galois 不变性相同，仍追踪原实际类型。定理 227.1 得证。

## 7. 统一常数与整性接口

因为 $M\ge3$，有 $4M\le M^3$。采用 R213/R215 同样的有限积，

$$\mathcal T(4M)^2\le T_{\epsilon/12}^2M^{\epsilon/2},$$

$$4^{\omega(D)}16^{\omega(a_{0,\mathrm{odd}})}
\le X_{\epsilon/4}M^{\epsilon/4},\qquad
\mathcal L_a^{-2}\le\beta_{\epsilon/4}^{-2}M^{\epsilon/4}.$$

再用 $2^{2e}\le64$ 和 $a_D^2\le1296$，(227.1) 右侧不超过

$$179159040\,X_{\epsilon/4}T_{\epsilon/12}^2\beta_{\epsilon/4}^{-2}
M^{1+\epsilon}/h.$$

增加因子二保证严格性，得到 (227.5)，证明定理 227.2。与 R213 相同，统一 Siegel 下界给平方根形式。

在本同余类 $v_2(p+1)=2$，R226 已精确证明阶四参数有 $\theta(z_2)=-1$，所以其准确导子为 $a=bc$，即 $M=M^*=D(bc)^2$。其他需要的参数阶大于四，用 R213 已可自动得到非 CM 非消失。因此 R226 的整性表中，整个 $p\equiv3\pmod8$ 一行可以严格加强为

$$\boxed{
p\ge C_\nu(M^*)^{1/2+\nu}
\quad\Longrightarrow\quad j(E)\in\mathbb Z.
} \tag{227.18}$$

这里仍使用 R87 的旧 Steinberg 参数及 R177/R181 的完整 Mellin 行接口；新输入只负责原先可能全落在 CM 上的阶四参数，且两个三次符号均逐个适用。

特别，对本同余类的非整 $j$ 实际异常表示，对每个 $\delta>0$ 有

$$\boxed{M^*\gg_\delta p^{2-\delta}.} \tag{227.19}$$

结合 R220 的同一全局二次扭曲导子，得到

$$N_{E'}\gg_\delta D T p^{4-\delta}\gg_\delta Dp^{5-\delta},$$

因为非整 $j$ 时的 Tate 素数乘积 $T$ 非空，且其中每个素数至少为 $2p-1$。这些下界一般无效。它们仍不给变化共同导子的上界，也不排除整 $j$ 异常分支。

## 来源与证明范围

- R213：实际 $p$ 分歧角色、准确谱端与主项，以及奇素数处的逐层误差；R214：$a_D\mid36$、$v_2(a)\le3$；R215：正卷积归一化；R226：同一实际类型的二进分支与整性接口。
- Feigon–Whitehouse, *Averages of central L-values of Hilbert modular forms with an application to subconvexity*, Duke Math. J. **149** (2009), 347–410，[作者全文](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)，[DOI](https://doi.org/10.1215/00127094-2009-041)。作者稿 pp.24–26，Lemmas 4.3–4.6 给一般共轭球面 Hecke 的 singular 公式；p.29，Lemma 4.11 给任意双陪集的行列式支集。本文 §3 和 §5 对所需二进 singular 及 regular 界均重新给出了直接证明；不调用只允许奇剩余特征的 Lemma 4.12。
- Qinghua Pi, JNT **191** (2018), 213–245，[作者稿](https://arxiv.org/abs/1707.07307)，§2.4 的相同 Gross–Prasad 极大序测试与正谱分解。这里只在 $2$ 共轭球面 Hecke 代数中替换一个局部因子，保留其余全部实际测试函数。
