# R705 — 原 wild 角色、全 p² 范数一群与绝对 Weil 投影

日期：2026-11-15。**状态：原相位的完整乘法角色身份、原根域实际次数、有限 Weil 模型及同一原迹的单重角色投影已证明。以下没有证明该投影非零，也没有从酉性推出非平凡最大值界。**

本篇接 R703 的原始相位，不改原 $p^2$ 提升或固定 theta 幅度。
它把原全 $H$ 迹识别为一个完全指定的、导子 $p^2$ 的 wild torus 投影，
并给该角色在整个有限环上的准确 Fourier 变换。
原小矩形代表、物理准周期及全部归一因子均保留。

## 1. 同一有限环及原相位

沿用 R696/R700/R703：
$$
p=6s-1>101,\quad d=p+1,\quad
R=\mathbf Z[\omega]/p^2,\quad \bar R=\mathbf F_{p^2},\quad
\delta=1+2\omega,\quad m\in\{34,72\}.
$$
$\bar v$ 始终表示复共轭；将一个 $R$ 元素约化到剩余域时会另行说明。
记
$$
[u,v]=\frac{\bar u v-\bar v u}{\delta},\qquad
e_{p^j}(a)=\exp(2\pi ia/p^j).
\tag{1}
$$
这就是 R703 的整数行列式配对。$N,\operatorname{Tr}$ 为同一个
二次环的范数、迹。

对 $v\in R^\times$ 定义
$$
q_p(v)=\frac{v^p/\bar v-1}{p}\pmod p\in\mathbf F_{p^2}.
\tag{2}
$$
由于 $v^p\equiv\bar v\bmod p$，(2) 合法且只依 $v\bmod p^2$。
乘法直接给
$$
q_p(vw)=q_p(v)+q_p(w),\qquad
q_p(\bar v)=\overline{q_p(v)}.
\tag{3}
$$
对任意 $z\in\mathbf F_{p^2}$，
$$
q_p(1+pz)=-\bar z.
\tag{4}
$$
Teichmüller 单位满足 $v^p=\bar v$，故其 $q_p$ 为零。

固定 $r\in\mathbf F_p^\times$，取其任意有理整数提升，并置
$$
\beta_r=\frac{mr}{2\delta}\in R,\qquad
\boxed{\;
\chi_{m,r}(v)=
 e_p\!\left(\frac{mr}{2\delta}
               (q_p(v)-\overline{q_p(v)})\right)
 =e_p(\operatorname{Tr}(\beta_rq_p(v))).
\;}
\tag{5}
$$
(3) 证明它是一个真实乘法角色。它不依 $r$ 的所取提升。
在主单位上，(4) 及 $\bar\beta_r=-\beta_r$ 给
$$
\boxed{\chi_{m,r}(1+pz)=e_p(\operatorname{Tr}(\beta_rz)).}
\tag{6}
$$
特别地
$$
\chi_{m,r}(1+p\delta t)=e_p(mrt).
\tag{7}
$$
因 $p\nmid mr$，其阶恰为 $p$，导子恰为 $p^2$。
它在整个 Teichmüller 群和整个 $(\mathbf Z/p^2)^\times$ 上恒为 1，
也满足
$$
\chi_{m,r}(\bar v)=\chi_{m,r}(v)^{-1},\qquad
\chi_{m,r}(\delta)=1.
\tag{8}
$$
最后一式是因为 $\delta^p/\bar\delta=-\delta^{p-1}$ 为有理数，
故 $q_p(\delta)$ 为有理数。

### 与 R703 的实际整数代表相位完全相同

若 $Nv\equiv r\bmod p$，则
$$
q_p(v)-\overline{q_p(v)}
 =\frac{v^{p+1}-\bar v^{\,p+1}}{pNv}\pmod p.
$$
因此 R703(18) 的相位准确满足
$$
\boxed{e_p(\tau_m(v))=\chi_{m,r}(v).}
\tag{9}
$$
这是同一整数代表上先除 $p$ 再约化的恒等，
没有把 $\tau_m$ 替换成一个自由选择的模 $p$ 多项式。

换代表 $v\mapsto v+p\ell$ 时，(6) 给
$$
\boxed{
\chi_{m,r}(v+p\ell)
 =\chi_{m,r}(v)e_p\!\left(-\frac m2[\ell,v]\right).
}
\tag{10}
$$
这里用了 $Nv=r\bmod p$。
(10) 正好抵消 R703 中原 theta 幅度的准周期相位。

## 2. 全范数一群及原根域的实际 p 次数

置
$$
\mathcal T=\ker\!\left(N:R^\times\longrightarrow
                                  (\mathbf Z/p^2)^\times\right).
$$
其阶为 $p(p+1)$，并准确分解为
$$
\mathcal T=\widehat H\times\mathcal U,\qquad
\mathcal U=\{1+p\delta t:t\in\mathbf F_p\}.
\tag{11}
$$
这里 $\widehat H$ 是 R703 的唯一阶 $p+1$ Teichmüller 提升。
角色
$$
\theta_r=\chi_{m,r}|_{\mathcal T}
\tag{12}
$$
在 $\widehat H$ 上恒为 1，在 $\mathcal U$ 上为 (7)。

R703 已证明 $F_2=K_0(E[p^2])$ 与 $K_0(E[12])$ 线性无交。
所以每个 $g\in\mathcal T$ 都有唯一完整层作用
$$
g_N\equiv1\bmod12,\qquad g_N\equiv g\bmod p^2,
\qquad \det(g_N)=1\bmod12p^2.
\tag{13}
$$
R703§4 的绝对定标证明对这里整个 $\mathcal T$ 原样有效：
Klein 比的共同乘子先约去；
原倍点给公共因子 $c_g^3=1$，
原除点式 $a_{T_v}=\xi_vk_v^{-p}$ 又给 $c_g^p=1$。
因此
$$
\boxed{g(k_v)=k_{g_Nv},\qquad g(w_v)=w_{g_Nv}.}
\tag{14}
$$
两式保全部相位，而非仅某个幂。

取 $u_t=1+p\delta t\in\mathcal U$。
在 (13) 的真正整数提升中，
$g_Nv=v+p\ell$，$\ell$ 为 $12$ 的倍数，且
$\ell\equiv\delta tv\bmod p$。
R703 的准周期式给
$$
\frac{k_{g_Nv}}{k_v}
 =e_p([\ell,v]/2)=e_p(-rt),
\qquad Nv\equiv r\ne0.
$$
同时 $N(g_N)=1\bmod p^2$ 保原 $\rho_v$。
故
$$
\boxed{u_t(w_v)=e_p(rt)w_v.}
\tag{15}
$$
这是原根 $w_v^p=a_{T_v}$ 的非平凡 Galois 作用。
R696 的 $W=F(w_v)$ 因而满足更准确的
$$
\boxed{[W:F]=p.}
\tag{16}
$$
$\mathcal T$ 到 $\operatorname{Gal}(W/F^H)$ 的限制为同构：
其 Hall 部分在 $F$ 上忠实，主单位部分由 (15) 忠实。

若
$$
\mathcal T_{m,T_v}
 =\operatorname{Tr}_{W/W^{\widehat H}}
       \bigl(w_v^{-m}\phi_m(T_v)\bigr)
$$
是 R696 的原迹，则 $u_t$ 固定 $T_v$ 并与 Hall 作用交换，故
$$
\boxed{
u_t(\mathcal T_{m,T_v})
 =e_p(-mrt)\mathcal T_{m,T_v}.
}
\tag{17}
$$
(17) 支付其真实 wild 角色；它不保证这个迹非零。

## 3. 原 theta 样本所在的绝对有限模型

令 $\mathcal V_m$ 为所有函数 $A:R\to\mathbf C$ 中满足
$$
\boxed{
A(v+p\ell)=e_p\!\left(\frac m2[\ell,v]\right)A(v)
\quad(v,\ell\in R)
}
\tag{18}
$$
的向量空间。右边只依 $\ell\bmod p$；
逐剩余类自由指定一个值可唯一恢复整个函数，所以
$$
\dim_\mathbf C\mathcal V_m=p^2.
$$
使用标准内积
$$
\boxed{
\langle A,B\rangle
 =\sum_{u\in\mathbf F_{p^2}}A(\widetilde u)
                              \overline{B(\widetilde u)}.
}
\tag{19}
$$
因 (18) 中相位模一，(19) 与每个代表 $\widetilde u$ 的选择无关。
内积对第一变量线性。

对 $t\in R$ 定义
$$
(\mathsf D_tA)(v)=
 e_{p^2}\!\left(\frac m2[t,v]\right)A(v+t).
\tag{20}
$$
直接代入 (18) 即见它保持 $\mathcal V_m$，且
$$
\mathsf D_t\mathsf D_s
 =e_{p^2}\!\left(\frac m2[s,t]\right)\mathsf D_{t+s}.
\tag{21}
$$
这些是不可约的 Heisenberg 算子。
事实上
$$
(\mathsf D_{p\ell}A)(v)=e_p(m[\ell,v])A(v),
$$
其 $p^2$ 个联合特征空间分别由 $v\bmod p$ 标记且各一维；
全部 $\mathsf D_t$ 在这些空间上传递作用。
所以任何共同不变子空间只能为零或整个空间。

设 $\operatorname{Sp}(R,[\, ,\,])=\operatorname{SL}_2(\mathbf Z/p^2)$。
对该群定义
$$
\boxed{
(\mathsf W(g)A)(v)=A(g^{-1}v).
}
\tag{22}
$$
它保持 (18)、(19)，严格满足群乘法，并有
$$
\mathsf W(g)\mathsf D_t\mathsf W(g)^{-1}=\mathsf D_{gt}.
\tag{23}
$$
(20)–(23) 因而给一个明确的、真正而非仅射影的有限 Weil 模型。
其绝对归一已固定：
支持于 $pR$、在该集合取值 1 的一维旧向量被全部
$\mathsf W(g)$ 固定。这里未在每个 $g$ 上另选根单位。

### 原固定来源的实际向量

定义
$$
\boxed{
A_m(v)=\mathfrak k(\Omega v/p)^m\phi_m(T_v).
}
\tag{24}
$$
在 $v\bmod p=0$ 的点按原零阶 6 延拓为 0。
因 $m$ 为偶数，(24) 对 $v\bmod p^2$ 周期；
R703 的准周期式准确给 (18)。
因此 (24) 是 $\mathcal V_m$ 的一个实际向量。

R700 的固定复界给
$$
|A_m(v)|\le C_m,\qquad \|A_m\|_2\le pC_m.
\tag{25}
$$
没有把这个向量归一成某个坐标基向量或低频基向量。
它包含原固定 theta 函数在全部 $p^2$ 个剩余类上的实际样本。

## 4. 真正单重 torus 角色及原迹内积

在 $Nv=r\bmod p$ 上定义
$$
G_r(v)=\chi_{m,r}(v)^{-1},
$$
其余点定义为零。
由 (10)，$G_r\in\mathcal V_m$，并且
$$
\boxed{
\|G_r\|_2^2=p+1,\qquad
\mathsf W(t)G_r=\theta_r(t)G_r
\quad(t\in\mathcal T).
}
\tag{26}
$$

该 $\theta_r$ 特征空间恰为一维，而非只包含这个向量。
确实，主单位 $u_t$ 在坐标 $v\bmod p$ 上的作用为
$e_p(mN(v)t)$。
指定非平凡主单位角色 $e_p(mrt)$ 恰迫支撑在
$N(v)=r$ 的 $p+1$ 个点上。
Hall 群在这些点上传递且自由作用，故每个 Hall 角色各出现一次。

这还给出整个限制的准确分解：
$$
\boxed{
\mathcal V_m|_{\mathcal T}
 =\mathbf1\ \oplus\
   \bigoplus_{\substack{\theta\in\widehat{\mathcal T}\\
                       \theta|_{\mathcal U}\ne1}}\theta.
}
\tag{27}
$$
所有非平凡的 tame-only 角色均不出现；
每个 wild 角色均单重。
维数为 $1+(p-1)(p+1)=p^2$。

真正正交投影为
$$
\boxed{
\mathsf P_r=
 \frac1{p(p+1)}\sum_{t\in\mathcal T}
             \overline{\theta_r(t)}\,\mathsf W(t).
}
\tag{28}
$$
由 (19)、(26)，
$$
\mathsf P_r A_m
  =\frac{\langle A_m,G_r\rangle}{p+1}G_r.
\tag{29}
$$
R703 的原和与原迹因而准确为
$$
\boxed{
\begin{aligned}
\mathscr S_{p,m}(r)&=\langle A_m,G_r\rangle,\\
\mathcal T_{m,T_v}
 &=\rho_v^{-m}\chi_{m,r}(v)^{-1}
                       \langle A_m,G_r\rangle\\
 &=(p+1)\rho_v^{-m}(\mathsf P_rA_m)(v),
 \qquad Nv=r\bmod p.
\end{aligned}}
\tag{30}
$$
也可展开成全 $p^2$ 范数一群的同一加权和：
$$
\boxed{
\mathcal T_{m,T_v}
 =\frac{\rho_v^{-m}}p
   \sum_{t\in\mathcal T}\chi_{m,r}(t)A_m(tv).
}
\tag{31}
$$
在每个主单位纤维上，
$\chi_{m,r}(1+p\delta a)=e_p(mra)$ 与
$A_m((1+p\delta a)v)=e_p(-mra)A_m(v)$
严格抵消；除去 $p$ 后正好恢复原 Hall 和。
(31) 不是将原 $p+1$ 项任意换成了另一种提升。

## 5. 完整有限环 Fourier 变换的绝对 Gauss 常数

为与可能的环上角色和定理准确比较，把
$$
f_r(v)=\mathbf1_{\{Nv=r\bmod p\}}\chi_{m,r}(v)
\tag{32}
$$
定义在整个 $R$ 上。对非单位其值为零。
记
$$
\mathcal G_r(\xi)=
 \sum_{v\in R}f_r(v)e_{p^2}(\operatorname{Tr}(\xi v)).
\tag{33}
$$
则有完全精确的变换式
$$
\boxed{
\mathcal G_r(\xi)=
 p^2\,\mathbf1_{\{N\xi=m^2r/12\bmod p\}}\,
             \chi_{m,r}(\xi)^{-1}.
}
\tag{34}
$$
非单位 $\xi$ 时右边为零。

证明不需要任何未定 Gauss 相位。
将所有单位唯一写成 $v=u(1+pz)$，
$u$ 为非零 Teichmüller 单位，$z\in\mathbf F_{p^2}$。
由 (6)，内层完整求和为
$$
\sum_z e_p(\operatorname{Tr}((\beta_r+\xi u)z)).
$$
它恰在 $\xi u=-\beta_r\bmod p$ 时为 $p^2$，否则为零。
该 $u$ 存在且 $Nu=r$ 的条件就是
$N\xi=N\beta_r/r=m^2r/12$。

在存活情形写 $\xi u=-\beta_r+pz_0$。
$\operatorname{Tr}\beta_r=0$，故余下加法相位为
$e_p(\operatorname{Tr}z_0)$。
同时 $\chi(u)=1$，且由 (8)
$\chi(-\beta_r)=1$，所以
$$
\chi(\xi)=
 \chi(-\beta_r)
 \chi(1-pz_0/\beta_r)
 =e_p(-\operatorname{Tr}z_0).
$$
这证明 (34)，包括绝对常数 $+1$。

(33) 是整个两维有限环加法群上的 Fourier 变换；
不要将这个 $p^4$ 维函数空间上的变换，
未经定义就当作第3节 $\mathcal V_m$ 的某一个单一矩阵。
第3节的 Weil 模型与本节的完整环 Fourier 式均已明确给出。

## 6. 原小矩形 section 的准确 completion

原 R703 的
$$
K_{p,m}(r;k,l)=
 \sum_{\substack{0\le a,b<p\\a^2-ab+b^2=r\bmod p}}
 \chi_{m,r}(a+b\omega)e_p(ka+lb)
\tag{35}
$$
仍使用原指定小矩形代表。
置
$$
\lambda_{k,l}=\frac{(k-l)-(k+2l)\omega}{3}\bmod p,
$$
则
$\operatorname{Tr}(\lambda_{k,l}(a+b\omega))=ka+lb$。
对实际矩形 $B_p=\{a+b\omega:0\le a,b<p\}\subset R$ 定义
$$
\mathcal D_p(\xi)=
 \sum_{v\in B_p}e_{p^2}(\operatorname{Tr}(\xi v))
 =
 \left(\sum_{a=0}^{p-1}e_{p^2}(a\operatorname{Tr}\xi)\right)
 \left(\sum_{b=0}^{p-1}e_{p^2}(b\operatorname{Tr}(\xi\omega))\right).
\tag{36}
$$
由整个 $R$ 上的 Fourier 反演和 (34)，
$$
\boxed{
K_{p,m}(r;k,l)=
 \frac1{p^2}
 \sum_{\substack{\xi\in R^\times\\
                 N\xi=m^2r/12\bmod p}}
  \chi_{m,r}(\xi)^{-1}
  \mathcal D_p(p\lambda_{k,l}-\xi).
}
\tag{37}
$$
所有 Dirichlet 核都保留。
(37) 支付真正 primitive ring character 的 completion，
并不把小矩形换成整个范数一轨道或删除截断权。

## 7. 已付识别能用于什么，尚未能用于什么

原迹现有三个完全一致的表述：

1. R696 的原代数全 Hall 迹；
2. R703 保 $p^2$ 相位的固定 theta 加权和；
3. (30) 的、具有明确绝对归一的单重 wild Weil 投影。

原目标需要控制的是同一 $A_m$ 的实际投影，
不是对任选单位向量的抽象投影范数。
例如仅用 (25)、(26) 和 Cauchy–Schwarz，只得
$$
|\mathscr S_{p,m}(r)|\le p\sqrt{p+1}\,C_m,
$$
比 R700 逐项的 $(p+1)C_m$ 界更弱。
因此单重性、酉性或 (34) 的完整 Gauss 常数，
都不能直接提供所需的 $p^{1-\epsilon}$ 界。

同样，(34) 处理全部主单位纤维，
而 (35) 在每个剩余类只取一个小矩形代表。
从 (34) 返回 (35) 必须保 (36)–(37) 的全部权。
不能只引用一个完整 Gauss 和的大小，
就给原 incomplete torus 和平方根估计。

任何进一步可用的有限 Weil 本征函数、toric period
或 prime-power character sum 定理，
至少须匹配：

- 这里的导子 $p^2$ 与阶 $p$ pure-wild 角色；
- tame 部分恒 1 的 $\theta_r$；
- (19)、(24) 的实际 theta 向量及其标准范数；
- (35) 的指定矩形 section，或等价地 (37) 的完整截断核；
- 所有 $r\ne0$ 与全部绝对嵌入。

本篇未添加新的中央零，未声明原投影非零。
若随后得到所需统一幂次节省，R703(25)、R700 的固定分母
会把它严格传回同一个原边界；这一步的接口已完整支付。

## 依赖

- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)：
  原共同根域、完整层下降及同一全迹。
- [R700](R700-original-fixed-denominator-and-logarithmic-trace-height.md)：
  固定分母、全部复共轭及固定 theta 幅度界。
- [R703](R703-original-hall-phase-and-finite-fourier-return.md)：
  原完整 Klein 相位、真正 Hall 提升、实际矩形 Fourier 返回。

本篇全部有限群及 Fourier 恒等均由显示公式证明，
没有数值扫描或新增可重算数据文件。
