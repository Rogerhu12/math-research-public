# R236 附录：实际 Bell 的全域差分单位、双阶导子与降阶投影接口

日期：2026-11-13（UTC）。作者：central_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明的工具及准确未闭接口。本文不证明 $1<\alpha\le3$ 的全部重数排核。
它把有限位降阶预处理写成原实际算子的完整等式，
不将近核误认为靠近未知核，也不免费归一化高次提升平均。

## 1. 固定行、真实字符与范围

设非零幅度重排满足
$$
\rho_k\le B e^{-\beta_- k^\alpha},\qquad
\rho_N\ge c_0e^{-\beta_+N^\alpha}
\quad\text{沿无穷子序列 }N,
\tag{1.1}
$$
其中 $\alpha>0$、$0<\beta_-\le\beta_+$ 固定。
相位和物理排列任意。
取任意复 $\ell^2$ first 指数权 $w$，令
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad
X=a_*I+\sum_ja_jR_j,\quad s=a_*+\sum_ja_j,\quad Z=X-sI.
$$
所有级数按范数绝对收敛，
$X,Z,G_n$ 都在实际交换代数 $\mathcal A$ 中，
$\chi(X)=s$、$\chi(Z)=\chi(G_n)=0$。

固定非零首一多项式 $q$，定义
$$
\mathcal P(z;\kappa)=
\exp\left(\sum_{n=2}^p\frac{\kappa_n}{n!}\partial_z^n\right)q(z),
\qquad T=\mathcal P(X;G).
\tag{1.2}
$$
若 $q(s)\ne0$，$T$ 本来就是 $\mathcal A$ 单位。
以下设 $q(s)=0$，并记 $m\ge1$ 为该根的重数。
$s$ 是原实际行的字符，没有更改 $a_*$ 或把规范中心平移掉。

记
$$
\mu=\min(\alpha,3),\qquad
\gamma=1+\frac1\mu
=\max\left(1+\frac1\alpha,\frac43\right),\qquad
\kappa_\alpha=\alpha\gamma.
\tag{1.3}
$$
后面所用算子全域有界，所有自然幂域都是 $H$。

## 2. 加入真实 first 中心后的共同对数预算

将 $Z$ 作为第一个零字符坐标，记 $H_1=Z$、$H_n=G_n$（$n\ge2$）。
第一个实际正主控为
$$
M_1=\sum_j|a_j|W_1(N_j),\qquad
W_1(z)=\frac{2Lz}{1-Lz},
$$
其中 $L\ge\max(1,\sup|t_j|,\sup|t_j|^{-1})$。
对 $n\ge2$，使用
$$
W_n(z)=\sum_{\ell=1}^n|c_{n,\ell}|
 \left(\frac{2Lz}{1-Lz}\right)^\ell,\qquad
L_n(1+x)=\sum_{\ell=1}^nc_{n,\ell}x^\ell,
$$
$$
M_n=\sum_j|a_j|^nW_n(N_j).
\tag{2.1}
$$
真实函数非负锥给
$|H_n^kf|\le M_n^k|f|$。
这不是 Hilbert 自伴正性。

有限低位的实际准幂零预解式和高位
$N_j^2=\eta_jN_{j+1}$ 给统一有理分母界；
因此若
$W_n(z)=w_{n,1}z+z^2W_{n,2}(z)$，
则 $\sup_j\|W_{n,2}(N_j)\|<\infty$。
实际偶奇幂估计给
$$
\|e^{zvW_n(N_j)}\|
\le(1+C_n|z|v)
 \exp(C_n|z|v\sqrt{\eta_j}),\qquad v\ge0.
\tag{2.2}
$$

按物理位选最小 $h\ge1$，
$385\,16^h\ge2\log(2+|z|)$。
标量重排只用于
$$
\sum_k\log(1+C_n|z|B^n e^{-n\beta_-k^\alpha})
\le C_n\big(1+[\log(2+|z|)]^{1+1/\alpha}\big).
\tag{2.3}
$$
这是在 $k\asymp(\log(2+|z|))^{1/\alpha}$ 分头尾的积分或求和比较。
原物理尾的进位仍满足
$$
\sum_{j\ge h}|a_j|^n\sqrt{\eta_j}
\le2B^ne^{-385\,16^h}.
$$

有限物理头明确为 $A U_{n,h}$，且
$$
\|U_{n,h}\|\le C_ne^{125\,16^{h-1}},\qquad
\log(2+|z|\|U_{n,h}\|)
\le C_n+2\log(2+|z|).
$$
R109 的 $\|A^k\|\le K_Ae^{-c_Ak^4}$ 给头部成本
$\exp(C_n(1+\log(2+|z|))^{4/3})$。
因此对全部 $\alpha>0$，真实头尾合并为
$$
\boxed{
\|e^{zM_n}\|\le K_n
 \exp\big(C_n[1+\log(2+|z|)]^\gamma\big),
\qquad 1\le n\le p.
}
\tag{2.4}
$$
$\alpha>3$ 时的 $4/3$ 是物理低头预算，
不能继续把它写成较小的 $1+1/\alpha$。

Cauchy 系数估计取
$R=e^{\lambda k^\mu}$、固定 $\lambda$ 足够小，
并把 $\log(k!)=o(k^{1+\mu})$ 吸收进负项，
得到
$$
\boxed{\|H_n^k\|\le K_ne^{-d_n k^{1+\mu}}\quad(k\ge0).}
\tag{2.5}
$$
实际 Neumann 级数绝对收敛；
对 $\ell=\log^+(1/|z|)$，
优化 $-d_nk^{1+\mu}+k\ell$ 后给
$$
\boxed{
\|(z-H_n)^{-1}\|
\le\frac{K_n'}{|z|}
 \exp\big(C_n'[\log^+(1/|z|)]^\gamma\big).
}
\tag{2.6}
$$
左右乘望远镜证明它是真正的逆，不是形式展开。

故对在
$$
|z_1|\le\varepsilon\delta,\qquad
|z_n|\le\varepsilon\delta^n\quad(2\le n\le p)
$$
的邻域全纯、边界模不超过 $M_F$ 的函数，
共同 Cauchy 演算给
$$
\boxed{
\|F(Z,G)\|\le K M_F
 \exp\big(C_\varepsilon[1+\log(1/\delta)]^\gamma\big).
}
\tag{2.7}
$$
这是包含 $n=1$ 的一次联合预算。

## 3. 所有零字符 Bell 多项式的真实幂界

令 $M=\sum_{n=1}^pM_n$。
这些正算子交换，(2.4) 相乘仍给相同对数幂 $\gamma$，
所以
$$
\|M^k\|\le K e^{-d k^{1+\mu}}.
$$
因为 $q(s)=0$，$T=\mathcal P(s+Z;G)$
是零常数项的有限多项式。
逐点三角不等式给某个无常数项、系数非负的标量多项式 $\Phi$，使
$$
|Tf|\le\Phi(M)|f|,\qquad
|T^kf|\le\Phi(M)^k|f|.
$$
$\Phi^k$ 的次数介于 $k$ 与 $C_pk$，
系数绝对和不超过 $C^k$。
故
$$
\|T^k\|\le K C^k e^{-d k^{1+\mu}}
\le K'e^{-d'k^{1+\mu}}.
$$
得到完整结论
$$
\boxed{
\|T^k\|\le K_Te^{-d_T k^{1+\min(\alpha,3)}}.
}
\tag{3.1}
$$
这是单个算子的幂界。
它不自动给 R151 的解析余尾型趋无穷；
$\alpha>3$ 的旧标准性需用真实解析 $N_j$ 系数展开，
详见相应快类核查笔记。

## 4. 真正全空间可逆的 Bell 差分

定义
$$
\mathscr L_a(z;\kappa)=
-2[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)].
$$
由 Bell 恒等式，
$$
\mathscr L_a=
4a\partial_z\mathcal P+
\sum_{n=2}^p4L_n'(1)a^n\partial_{\kappa_n}\mathcal P.
\tag{4.1}
$$

存在固定 $\varepsilon,a_0>0$，
使 $0<\delta\le|a|\le a_0$ 时，
在
$|z_1|\le2\varepsilon\delta$、
$|\kappa_n|\le2\varepsilon\delta^n$
上有
$$
\boxed{
|\mathscr L_a(s+z_1;\kappa)|\ge c_q|a|^m
\ge c_q\delta^m.
}
\tag{4.2}
$$
证明保留根重数：
$q(s-2a)$ 的模至少为 $c|a|^m$；
移动 $z_1$ 的误差为
$O(\varepsilon\delta|a|^{m-1})$。
将全部累积量乘积按总 Bell 权 $k$ 分组，
其 $q^{(k)}$ 系数是 $O(\varepsilon\delta^k)$；
每组因而至多为
$O(\varepsilon\delta^k|a|^{(m-k)_+})=O(\varepsilon|a|^m)$，
高于 $m$ 的权用 $|a|\le1$。
$\mathcal P(s+z_1;\kappa)$ 本身也是 $O(\varepsilon\delta^m)$。
取 $\varepsilon$ 足够小即得 (4.2)。
其它标量根由固定 $a_0$ 排除。

所以
$$
L_a:=\mathscr L_a(X;G)\in\mathcal A^\times
$$
是真正的全空间单位：
其字符就是 $-2q(s-2a)\ne0$，
也可直接由 (4.2) 的共同全纯倒数求值来验证。
对有限集合 $F$，置
$$
L_F=\prod_{j\in F}L_{a_j},\qquad
\mathcal R_F=L_F^{-1}.
$$
对 $\ell=1,2$，共同演算而非逐位重复演算给
$$
\boxed{
\|\mathcal R_F^\ell\|
\le K C_q^{\ell r}\delta^{-\ell mr}
 \exp\big(C_\varepsilon[1+\log(1/\delta)]^\gamma\big),
\qquad r=|F|.
}
\tag{4.3}
$$
这里是完整 $H$ 上的逆，没有只模 $\ker T$ 的余式，也没有 $TS_F$ 余项。

## 5. 任意跨度的真实多重仿射截断

下面给出比单纯符号反射更适合降阶矩阵的截断。

对 $j<k$，令
$$
N_j^{[k]}=
E_j+\eta_jE_j^*E_{j+1}+\cdots+
(\eta_j\cdots\eta_{k-2})E_j^*\cdots E_{k-2}^*E_{k-1}.
$$
真实递推给
$$
N_j-N_j^{[k]}
=(\eta_j\cdots\eta_{k-1})E_j^*\cdots E_{k-1}^*N_k,
\qquad
\|N_j-N_j^{[k]}\|\le\eta_{k-1}.
\tag{5.1}
$$
所有项保持函数非负锥，且
$0\le N_j^{[k]}\le N_j$，所以 $\|N_j^{[k]}\|\le1$。

以下有限 $F$ 满足 $\min F\ge1$；后面的全部高位应用都有此条件。
给定这样的 $F$：
若 $j\in F$，置 $\widetilde N_j=E_j$；
若 $j\notin F$，在 $j$ 后存在第一个选中位 $k$，
置 $\widetilde N_j=N_j^{[k]}$；
若不存在这样的 $k$，保留 $\widetilde N_j=N_j$。

这组算子两两交换。
同一未选区间内由递推逐次验证交换；
不同区间的物理支撑不交。
每个未选 $\widetilde N_j$ 与选中位的全部矩阵代数交换，
而选中 $\widetilde N_j=E_j$。

所有截断的 $(I\pm t_j\widetilde N_j)^{-1}$ 有统一界。
高 $j$ 使用截断的真实平方关系
$(N_j^{[k]})^2=\eta_jN_{j+1}^{[k]}$，
最短截断平方为零；
有限低 $j$ 则由 $N_j^{[k]}\to N_j$、
实际逆连续性和有限个剩余截断取最大值。
因此固定有理函数的逆差具有统一 Lipschitz 常数。

把 $X,G_n$ 中的 $N_j$ 同时换成 $\widetilde N_j$，
所得变量记为 $\widetilde X,\widetilde G_n$，
并置 $\widetilde T=\mathcal P(\widetilde X;\widetilde G)$。
设 $h=\min F$。
利用 $\sum|a_j|^n<\infty$，按每个截断端点分组，
(5.1) 给
$$
\boxed{
\|X-\widetilde X\|+\sum_{n=2}^p\|G_n-\widetilde G_n\|
+\|T-\widetilde T\|
\le C\sum_{k\in F}\eta_{k-1}
\le\epsilon_h,\qquad
\epsilon_h\le C e^{-385\,16^{h-1}}.
}
\tag{5.2}
$$
选中位本身的误差 $\|N_j-E_j\|\le\eta_j$ 也吸入右侧。
这个估计不含 $\max F$，没有用最大位之前的头范数。

## 6. 双阶导子的精确最高项

在截断模型中写
$$
\widetilde X=X_0-2\sum_{j\in F}a_jt_jE_j,\qquad
\widetilde G_n=G_{n,0}
 -2L_n'(1)\sum_{j\in F}a_j^nt_jE_j.
$$
$X_0,G_{n,0}$ 与选中位全部矩阵交换，且彼此交换。
令 $T_0=\mathcal P(X_0;G_0)$、$W_F=\widetilde T-T_0$。
$W_F$ 是选中平方零变量的无常数项多重仿射多项式。
其一次系数是
$$
B_j=-\frac{t_j}{2}\mathscr L_{a_j}(X_0;G_0).
\tag{6.1}
$$
因此
$$
W_F^{r+1}=0,\qquad
W_F^r=r!E_F\prod_{j\in F}B_j,\qquad
E_F=\prod_{j\in F}E_j.
$$

记 $\delta_T B=[T,B]$。
$T_0$ 与 $E_F^*$ 及 $W_F$ 交换，故
$$
\delta_{\widetilde T}^{2r}(E_F^*)
=\sum_{k=0}^{2r}(-1)^k\binom{2r}{k}
 W_F^{2r-k}E_F^*W_F^k.
$$
除 $k=r$ 外，至少一个幂指数超过 $r$，所以全部为零。
再用 $E_FE_F^*E_F=E_F$，得到精确等式
$$
\boxed{
\delta_{\widetilde T}^{2r}(E_F^*)
=(-1)^r(2r)!\frac{t_F^2}{4^r}
 E_F\prod_{j\in F}\mathscr L_{a_j}(X_0;G_0)^2,
\qquad t_F=\prod_{j\in F}t_j.
}
\tag{6.2}
$$
它不假定某个非交换 companion 矩阵的差分与原矩阵交换。

乘上 $E_F$ 后，
$\mathscr L_{a_j}(X_0;G_0)$ 可换成
$\mathscr L_{a_j}(\widetilde X;\widetilde G)$：
所有差项都含选中 $E_j$，于是产生真实平方零。
再由 (5.2) 的有限多项式逆差比较到实际 $L_{a_j}$。

另一方面，$\delta_T,\delta_{\widetilde T}$ 是作用于 $B(H)$ 的有界导子，
$\|\delta_T-\delta_{\widetilde T}\|\le2\|T-\widetilde T\|$。
真实非交换幂差控制其 $2r$ 次幂之差。
由于 $\mathcal R_F$ 与 $T$ 交换，
$$
\delta_T^{2r}(E_F^*\mathcal R_F^2)
=\delta_T^{2r}(E_F^*)\mathcal R_F^2.
$$
合并得到完整原模型估计
$$
\boxed{
\left\|
\delta_T^{2r}(E_F^*\mathcal R_F^2)
-(-1)^r(2r)!\frac{t_F^2}{4^r}E_F
\right\|
\le\epsilon_h e^{Cr\log(r+2)}\|\mathcal R_F^2\|.
}
\tag{6.3}
$$
这是全 $H$ 算子范数估计，不要求输入在 $\ker T$ 中。

## 7. 允许线性阶数的全域平均

沿 (1.1) 的 $N$，按已付的删除法，
在排序前 $N$ 位中删前 $N/4$ 排序位及前 $N/4$ 物理位，
选 $Q_N=\lfloor N/4\rfloor$ 个剩余实际位组成 $I_N$。
于是
$$
\min I_N\ge h_N=\lfloor N/4\rfloor,\qquad
\delta_N=c_0e^{-\beta_+N^\alpha}\le|a_j|
\le B e^{-\beta_-(N/4)^\alpha}\to0.
$$
任意 $1\le r\le Q_N$ 都允许；$r$ 不再预先固定为 $O(\sqrt{Q_N})$。

定义
$$
\mathcal U_{N,r}
=(-1)^r\frac{r!}{(2r)!}
 \left(\frac8{Q_N}\right)^r
 \sum_{\substack{F\subset I_N\\|F|=r}}
 t_F^{-2}E_F^*\mathcal R_F^2.
\tag{7.1}
$$
有
$$
\|\mathcal U_{N,r}\|
\le\frac{(8L^2)^r}{(2r)!}
 \sup_F\|\mathcal R_F^2\|
\le
\exp\big(CN^{\kappa_\alpha}+CrN^\alpha+Cr+C\big).
\tag{7.2}
$$
(6.3) 求和后主项准确为
$$
r!\left(\frac2{Q_N}\right)^r\sum_{|F|=r}E_F=C_{I_N}^r,
\qquad C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
$$
所以
$$
\boxed{
\sup_{1\le r\le Q_N}
\|\delta_T^{2r}(\mathcal U_{N,r})-C_{I_N}^r\|
\longrightarrow0.
}
\tag{7.3}
$$
一个统一误差上界是
$$
\epsilon_{h_N}
\exp\big(CN^{\kappa_\alpha}+CN^{1+\alpha}+CN\log(N+2)+C\big),
$$
真实物理进位的双指数衰减支付了全部增长。
(7.3) 没有把 $r\asymp Q_N$ 的纯提升平均误说成非零弱极限。

## 8. 有界降阶伪逆的真实范数

固定 $Q,r$，令
$$
S_Q=\sum_{j\in I}E_j,\qquad C_Q=2S_Q/Q,\qquad
V_{Q,r}=(C_Q^r)^\dagger.
$$
这里是已知有限位矩阵的 Moore--Penrose 逆，随后张量其余位的恒等。

有完整估计
$$
\boxed{
\|V_{Q,r}\|\le\frac{(Q/2)^r}{r!}\le e^{Q/2}.
}
\tag{8.1}
$$
为证明第一式，使用 $S_Q,S_Q^*$ 的正交有限链。
若 $v$ 在第 $h$ 层、$S_Q^*v=0$，
交换关系 $[S_Q^*,S_Q]=Q I-2\mathsf N$ 给
$$
\|S_Q^kv\|^2=k!\frac{(Q-2h)!}{(Q-2h-k)!}\|v\|^2.
$$
归一化后得到长度 $L+1$、$L=Q-2h$ 的链，
其第 $k$ 步权为 $\sqrt{(k+1)(L-k)}$。
取所有最低向量的正交基，所得链穷尽全空间：
否则不变正交补的最低非零占据层又给一个遗漏的最低向量。

在每条长度至少 $r+1$ 的链上，
$S_Q^r$ 的每个非零奇异值为
$$
\left(\frac{(k+r)!}{k!}
      \frac{(L-k)!}{(L-k-r)!}\right)^{1/2}\ge r!.
$$
这给 (8.1) 第一式。
第二式由 $r!\ge(r/e)^r$ 及
$x\log(e/(2x))\le1/2$（$0<x\le1$）得到。

令 $P^{\rm ran}_{Q,r}=C_Q^rV_{Q,r}$。
这是实际正交投影，范数为 1。
参考真空只在全对称链上有分量；
该链第 $k$ 层向量在 $k\ge r$ 时属于像，
在 $k<r$ 时与像正交，因此
$$
\|(I-P^{\rm ran}_{Q,r})\Omega_I\|^2
=\mathbb P\{\operatorname{Bin}(Q,1/2)<r\}.
\tag{8.2}
$$
没有声称像等于全部 $k\ge r$ 层。

固定 $0<\eta<1/2$，取 $r_N=\lfloor\eta Q_N\rfloor$。
(8.2)、高位移出固定柱及一致投影界给
$$
P^{\rm ran}_{Q_N,r_N}\longrightarrow I\quad\text{强收敛}.
$$
结合 (7.3) 的明确误差和 (8.1)，更有实际全空间结论
$$
\boxed{
\big[\delta_T^{2r_N}(\mathcal U_{N,r_N})\big]V_{Q_N,r_N}
\longrightarrow I\quad\text{强收敛}.
}
\tag{8.3}
$$
这里“高阶导子之后再乘降阶逆”是必要次序；
这个产品本身不是一个已经证明属于同阶导子像的算子。

## 9. 未知核配对中的全部剩余交换子

令 $M=\ker T$、$B(f,g)=\langle f,Cg\rangle$，
并固定有限局部矩阵 $D$。
写 $U_N=\mathcal U_{N,r_N}$、$V_N=V_{Q_N,r_N}$。
对 $f,g\in M$，全域有界 Leibniz 公式准确给
$$
\boxed{
B\big(D[\delta_T^{2r}U_N]V_Nf,g\big)
=
\sum_{k=0}^{2r}\binom{2r}{k}
 B\big((\delta_T^{2r-k}D)U_N(\delta_T^kV_N)f,g\big).
}
\tag{9.1}
$$
证明是展开中间导子，
在左侧用
$B(DT^\ell h,g)=(-1)^\ell B((\delta_T^\ell D)h,g)$，
在右侧用 $T^kV_Nf=(\delta_T^kV_N)f$。
两种符号相乘为 $(-1)^{2r}=1$。
不能只保留 $k=0$ 项。

左侧由 (8.3) 趋于 $B(Df,g)$。
对固定 $D$，有限低头的实际除法给
$T=T_{\rm tail}+A U_h$，
其中 $T_{\rm tail}$ 与 $D$ 交换，$U_h\in\mathcal A$ 有界。
因此
$$
\|\delta_T^\ell D\|
\le\|D\|[2\|U_h\|]^\ell
 e^{-(5/6)\ell^4+105\ell^3}.
\tag{9.2}
$$
但这不适用于随 $N$ 变化的 $V_N$；
对后者，目前只能直接使用
$$
\|\delta_T^kV_N\|\le(2\|T\|)^k\|V_N\|,
\qquad
(\delta_T^kV_N)f=T^kV_Nf\quad(f\in M).
\tag{9.3}
$$
(3.1) 还给
$\|T^kV_Nf\|\le K_Te^{-d_Tk^{1+\mu}}\|V_N\|\|f\|$，
但其常数须与 (7.2) 比较，不能只比较幂指数后自动吸收。

## 10. 对 $1<\alpha<3$ 的准确剩余短段

在这个区间 $\kappa_\alpha=1+\alpha<4$，
$r_N\asymp N$。
由 (7.2)，可固定 $K_0$ 使
$\|U_N\|\le e^{K_0N^{1+\alpha}}$。
结合 (8.1)、(9.2)、(9.3) 和
$\binom{2r}{k}\le2^{2r}$，
存在足够大的固定 $C_0$，使
$$
L_N=\left\lceil C_0N^{(1+\alpha)/4}\right\rceil=o(r_N)
$$
满足
$$
\boxed{
\sum_{0\le k\le2r-L_N}\binom{2r}{k}
 B((\delta_T^{2r-k}D)U_N(\delta_T^kV_N)f,g)
\longrightarrow0.
}
\tag{10.1}
$$
确实，$\ell=2r-k\ge L_N$ 的
$-(5/6)\ell^4$ 可支付 $K_0N^{1+\alpha}$；
$105\ell^3$、固定局部常数、二项式以及 $\|V_N\|$
只产生严格较低阶成本。
$C_0$ 可先依赖 $K_0$ 选取，
固定 $D$ 的常数不改变这个主幂比较。

于是排核尚需控制、且完整保留下来的正是
$$
\boxed{
\sum_{\ell=0}^{L_N-1}\binom{2r}{\ell}
 B\big((\delta_T^\ell D)U_N
       (\delta_T^{2r-\ell}V_N)f,g\big).
}
\tag{10.2}
$$
若能证明它趋零，(9.1) 就会给全部局部 $B(Df,g)=0$，
再由实际局部不可约性排除 $M$。
本文没有证明 (10.2) 趋零。

因此本文确实构造了允许线性提升次数的有界强近似恒等 (8.3)，
并把它接到原核的完整配对公式；
没有把降阶逆近保持未知核当作已知事实。
剩余短段含少量局部导数与接近最高阶的伪逆导数，
需要新的实际估计或准确消去。

$\alpha=3$ 时 $L_N$ 一般与 $N$ 同阶，
上述短段缩减不能自动用于端点；
$\alpha>3$ 的原循环结论已经由既有快类处理。
普通 ISP 和其余开放接口的完成状态不由本文改变。


## 11. 全等向有限核不支付端点的背景因式化

2026-11-13 补充。[完整两位及四位校准](R236-appendix-finite-isotropic-kernel-endpoint-calibrations.md)保留本稿的实际正交 Moore–Penrose 逆和完整 Leibniz 配对。四位平方零模型取系数(1,2,3,4)、r=1<Q/2=2及T0=0；有在全部纯位下不变的子模M⊂kerT，且整个M对原互补位配对全等向。一个单位f∈M仍满足

$$
\mathcal B\bigl(U(\operatorname{ad}_T^2V)f,f\bigr)
=\mathcal B(P_{\operatorname{Ran}C_4}f,f)
=\frac{35(1+2i\sqrt3)}{819}\ne0.
$$

因此，单凭核关系、全等向、纯位不变及有限平方零代数，不能把§10的最高端项普遍因式化为含正次T0的项。投影不保持等向M；全等向不等于局部等向。该有限校准没有原A的全部无限结构，不说明原Haar核存在，也不推翻[全池背景预解](R236-appendix-deleted-pool-bell-background-resolvents-and-exact-product-gain.md)已证的背景估计。真正未付的是一个使用额外实际结构的端点连接。


## 12. 固定阶的全部广义核推论

[完整证明](R236-appendix-fixed-order-double-commutators-and-generalized-kernel-isotropy.md)直接使用§7：对每个固定r，δ_T^(2r)U_(N,r)强趋I，不需右侧伪逆。对f∈kerT^n、g∈kerT^m先固定2r≥n+m−1，再展开并逐项转置，每项至少有一端幂为零。因此全部n,m均有B(kerT^n,kerT^m)=0，等价kerT^n⊂closure RanT^m。

闭广义核空间仍全等向并包含于全部有限闭像；非零时为无限维真A不变空间。这里仅使用本稿的有界Bell分支及真实算子幂，不给实像/原像预算，也未证明未知限制稠密或局部等向。§10的增长阶数伪逆端段仍未完成。
