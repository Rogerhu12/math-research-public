# R406：两条完整自然通量的首次实际值、权零一维像与真实零矩成本障碍

日期：2026-11-15。**本稿消费唯一一次新公开 Actions 的完整原日志；两条新通量的完整局部式及零判定已经执行，函数空间与实际成本后果是下文的纸面推论。没有在本地执行研究、profile 评价或人工检查，也没有重做旧 pure/self 成员及旧秩。**

本次首次新观察得到
$$
\boxed{
n_6(u)=\Lambda_u(C_6)\equiv0,\qquad
n_2(u)=\Lambda_u(C_2)=\int L(x,u,u',u'')\,dx\not\equiv0,
}
\tag{1}
$$
其中完整的十二项密度 $L$ 列于(9)。这不是某个有限 profile 族的零或非零测试：$J_6$ 的**整个真实左端 word 表为空**，而 $H_*$ 的完整通量已经化为局部密度，其完整 Euler 多项式非零。

结合 [R404](R404-natural-weight-zero-image-at-most-two-and-single-function-kernel-criterion.md)，立即得到
$$
\boxed{n_4=0,\qquad
\mathcal N(U_0)=\mathbb R n_2,\qquad
\dim\frac{(E,\mathcal N)(U_0)}{(E,\mathcal N)(\mathcal R_0)}=1.}
\tag{2}
$$
这里 $E=(\pi,\mathcal Q)$，$\mathcal N(V)(u)=\Lambda_u(V)$。

更进一步，原正字符 $\lambda_+$ 不仅能经过增强映射 $(E,\mathcal N)$ 下降，实际上能经过**完整自然函数映射 $\mathcal N$ 单独下降**。对任意真实正时长、同一常数端 germ、闭 frame、$M=0$ 的 canonical 成本 $V_B$，下降的泛函满足
$$
\boxed{
\ell_+(\mathcal N(V_B))
=\lambda_+(V_B)
=L_B+\int_B(h_s/h)^2\,ds>0.
}
\tag{3}
$$
因此这种实际成本不可能对全部实紧输入同时具有自然通量零。式(3)不要求 $h$ 非恒定，也不要求第三矩 $\mathbf T$ 为零；例如 $\mathbf T=\tau H$ 的原几何同样适用。

这仍是 **universal canonical 自然函数** 的障碍。它不排除某个特殊固定 profile、有限多个固定读出、某一第一圆的全部已指定包上通量为零，也不自动覆盖新增独立二阶 gauge。

## 1. 原目标、原空间与通量规范

沿用 [R400](R400-weight-zero-natural-flux-kernel-and-three-static-function-criterion.md) 的真实完整成本空间 $U$、响应空间 $\mathcal R$、有限真权分解及共同右锚。原映射是
$$
\begin{aligned}
E(V)&=(\pi V,\mathcal Q(V)),\\
\mathcal Q(V)(u)&=\frac14[x^2]_{\rm left}V(u^2,0),\\
\mathcal N(V)(u)&=\Lambda_u(V).
\end{aligned}
\tag{4}
$$
$\mathcal Q$ 只读整个 self 输出的左二次系数；它与总通量不同。

为了固定所有校正项和常数，[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 的定义为
$$
\begin{aligned}
\Lambda_u(V)
={}&\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),\\
\mu(u)={}&
\left(\int(u'')^2,\ \int x(u'')^2,\
\int\{x^2(u'')^2+2(u')^2\}\right).
\end{aligned}
\tag{5}
$$
$\mathscr G$ 是原 pure 输出的有序 $2+2$ 三矩真尾映射。它不能由非紧 self 的尾中删去。R344/R352 已证明
$$
\mathcal N(\mathcal R)=0.
\tag{6}
$$
当整个 $\pi V=0$ 时，(5)后两项才同时为零。

本次不重新计算该 pure-zero 身份，而是使用已付的两个完整代表：
$$
\begin{aligned}
H_*={}&C_2+\frac{649}{768}R_2-\frac{73}{3072}R_3
+\frac{649}{1536}R_4-\frac{821}{768}R_5
+\frac1{64}R_7+\frac{187}{1024}R_9,\\
J_6={}&C_6-\frac5{384}R_2+\frac5{1536}R_3
-\frac5{768}R_4+\frac1{384}R_5+\frac1{512}R_9.
\end{aligned}
\tag{7}
$$
这里 $R_j$ 是 R126 原 old-column 标签，不是压缩列位置。原 static normal 记录为
$$
C_2:F_0(0,2,0,0),\qquad C_6:F_0(1,1,1,0),
$$
状态键依次是 $(h,k,\omega,\log h)$ 的幂。

[R316](R316-complete-weight-zero-self-membership-and-positive-character-representative.md) 与 [R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md) 已付
$$
E(H_*)=E(J_6)=0,\qquad
\lambda_+(H_*)=1,\quad\lambda_+(J_6)=0.
$$
所以(6)给
$$
n_2=\Lambda_\cdot(H_*),\qquad
n_6=\Lambda_\cdot(J_6),
$$
并且本次两目标都准确等于 raw self 总通量。

## 2. 唯一公开执行及其输入边界

首次、唯一新运行：

| 项目 | 准确身份 |
|---|---|
| run | 43775998866 |
| job | 133002325378 |
| source | d47749f7289ba0965e912a0e0e026bc619ebd4cb |
| [公开 job](https://github.com/Rogerhu12/math-research-public/actions/runs/43775998866/job/133002325378) | success |
| 新入口 | [literature_weight_zero_natural_flux.py](../scripts/literature_weight_zero_natural_flux.py) |
| 请求 | [request-weight-zero-natural-flux.json](../computations/request-weight-zero-natural-flux.json) |
| 设计 | [weight-zero-natural-flux-two-target-design-20261115.md](../notes/weight-zero-natural-flux-two-target-design-20261115.md) |

新入口为 42478 B，SHA256 为
$$
\texttt{be12b9338cf5558eacb4d05b43f201871fae5d4262dd330304eaa56df3c2e12f}.
$$
执行时完整请求为 8446 B，SHA256 为
$$
\texttt{ad26ae977549b084dce83a7c96c5c43fe3955af7d8399907c696b7468e9c1c1d}.
$$
冻结 workflow 为 3996 B，SHA256 为
$$
\texttt{1bcc261939e9cbeab100603c5d8827a04c385c7e22ae90b8521aba0b4d9fe5d9}.
$$
完整源闭包由实际请求和两个报告逐文件保存身份；运行只用标准库，没有换研究库版本。

本次只新增两个完整 $\Omega$ 读出。必要输入恢复准确为原 $C_2,C_6$ 的两个 mixed 根和(7)所需六个响应 mixed 根。原 $N_0$、同一个 $\Gamma$、参考态归一和全部历史都保留；没有重新编译 forcing。原 pure 根、旧 pure/self normal form、旧 Euler、旧同权秩、旧 profile 评价及其他 static/response 根均未重做。

两个 static mixed 根与原身份逐字节匹配：

| 原记录 | mixed 根 SHA256 |
|---|---|
| $C_2$ | b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f |
| $C_6$ | 5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02 |
| 同一原 $\Gamma$ | c6276335dd47380509870798123478dc1b5a25ad83f3eef15d30cedcef4ece0b |

六个恢复响应恰为 $R_2,R_3,R_4,R_5,R_7,R_9$；它们的原 quadratic/W 下标和 mixed SHA 全列于实际主报告。旧 R316、R329 的成员回执只读复用，没有重新求它们的成员系数。旧 R329 日志确含两个同名 COMPLETE_REPORT；本次按既有主报告的字节数及 SHA 选取，未错误要求整份旧日志只有一个同名标记。

### 2.1 原锚、外乘及左端符号

设 $M_{-2}$ 为(7)对应的原完整 mixed 系数。原规范给
$$
V(u^2,0)=-4M_{-2}(u,u),\qquad
\Omega_u(V)=-4\int u'''M_{-2}(u,u).
\tag{8}
$$
消费器先作完整全局对角代入，再外乘 $u'''$，最后取同一个右锚的原函数。使用原 signed 积分 $I_r^x=-J$，其左端值为负的全区间积分；因此计算的 $4I_r^x(u'''M_{-2})$ 左值正是(8)。

没有把每一层 $J$ 的右锚无条件缩到 profile 支撑端，也没有把单包 self 输出假设为紧。整个有序 word 表归约完成后才置左 collar 上的外部 profile jets 为零；有序常数和多字余项仍进入完整左端表。仅在该表没有任何非局部余项时，才使用后面的局部 Euler 判据。

## 3. 两个完整局部结果

设
$$
p=u',\qquad r=u'',\qquad t=u''',\qquad w=u^{(4)}.
$$
实际输出给
$$
\boxed{\begin{aligned}
L={}&u^2p^3-xup^4
+\frac32x^2u^2pr^2+\frac3{10}x^2p^5\\
&-\frac12x^3u^2r^3-3x^3up^2r^2
+\frac32x^4upr^3+\frac32x^4p^3r^2\\
&-\frac14x^5ur^4-x^5p^2r^3
+\frac5{16}x^6pr^4-\frac3{80}x^7r^5.
\end{aligned}}
\tag{9}
$$
于是
$$
\boxed{\Lambda_u(H_*)=\int L,\qquad
\Lambda_u(J_6)=0
\quad\text{对所有实 }u\in C_c^\infty(I).}
\tag{10}
$$
(9)保留十二个准确有理系数；没有以主项或相差未证明总导数的短式代替完整密度。

原完整输出规模为：

| 层 | $H_*$ | $J_6$ |
|---|---:|---:|
| 完整 mixed 项数 | 2497 | 2198 |
| 完整全局对角项数 | 246 | 175 |
| 新完整原函数 word 项数 | 88 | 65 |
| 完整左端单字项数 | 12 | 0 |
| 完整左端非局部余项数 | 0 | 0 |
| 完整局部 Euler 项数 | 24 | 0 |

特别，$J_6$ 的整个左端表已经为空。它不只是“某个非零局部密度的 Euler 为零”，更不是有限输入上的数值零。

$H_*$ 的完整新 word 表 SHA256 为
$$
\texttt{642e351c42698d9b2ea9bfefc761c39cb4de9b7e885e2a6752adfa22c8740ec2},
$$
完整左表 SHA256 为
$$
\texttt{bf502add6a272e2e9d05d7764fca3272e00c3235dab2ea40f1abbc36c8bf66cd}.
$$
$J_6$ 的完整新 word 表 SHA256 为
$$
\texttt{55800c90b9332700df004590aaa5a75fc6c27d08925e7fc877527aca8aed9fc5},
$$
空左表及空 Euler 的共同 SHA256 为
$$
\texttt{4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945}.
$$

## 4. 完整 Euler 证书及真实非零性

对于(9)，原完整 Euler 算子为
$$
\mathscr E(L)=L_u-D_xL_p+D_x^2L_r.
\tag{11}
$$
实际二十四项可以不丢任何项地分组为
$$
\boxed{
\mathscr E(L)=A_4\,w+A_{33}\,t^2+A_3\,t,
}
\tag{12}
$$
其中
$$
\begin{aligned}
A_4={}&3x^2u^2p-3x^3u^2r-6x^3up^2
+9x^4upr+3x^4p^3\\
&-3x^5ur^2-6x^5p^2r+\frac{15}{4}x^6pr^2
-\frac34x^7r^3,\\[1mm]
A_{33}={}&-3x^3u^2+9x^4up-6x^5ur
-6x^5p^2+\frac{15}{2}x^6pr-\frac94x^7r^2,\\[1mm]
A_3={}&12xu^2p-12x^2u^2r-24x^2up^2
+36x^3upr+12x^3p^3\\
&-12x^4ur^2-24x^4p^2r+15x^5pr^2-3x^6r^3.
\end{aligned}
\tag{13}
$$
完整 Euler 序列 SHA256 为
$$
\texttt{5f663db9acab1b881d3727972732a254b0ef5206699d03a3d41614617acb5c97}.
$$

最高 $w$ 系数还能直接由(9)的 $L_{rr}$ 手工核对：
$$
\boxed{
A_4=L_{rr}
=3x^2(p-xr)\left(u-xp+\frac{x^2r}{2}\right)^2.
}
\tag{14}
$$
这不是零多项式。例如在任意 $x_0\ne0$ 的内点，取自由 jets
$p=1,r=0,u=1+x_0$，其值为 $3x_0^2$。
紧光滑函数可以在该内点实现这些有限 jets；这里只使用自由 jets 证明多项式非零，没有执行一个新的 profile 评价。

还须说明为什么非零 Euler 是完整泛函的证书。密度(9)在 profile jets 中齐次五次。对真实紧 $u$，全部分部积分端项为零，故
$$
5\int L=\int u\,\mathscr E(L).
\tag{15}
$$
若 $\mathscr E(L)=0$，(15)给整个泛函为零。反过来，若 $\int L$ 对全部紧 $u$ 恒零，则对任意紧变分作一阶变分，基本引理给 $\mathscr E(L)[u]=0$；再用内点自由 jets，得到其多项式恒零。这与(14)矛盾。

因此(10)中第一条是一个严格非零的 universal 函数。完整判定是
$$
\boxed{n_6=0,\qquad n_2\ne0,\qquad
n_2\notin\operatorname{span}\{n_6\}.}
\tag{16}
$$
没有把“非零 NF”直接当作“非零泛函”。本次也没有求某一个指定 profile 的非零数值；证明的是完整函数身份及其否定。

## 5. 原权零自然像恰为一维

R404 原完整函数关系为
$$
C_{20}=C_4+c_0C_6+R_*,
\qquad R_*\in\mathcal R_0,
\tag{17}
$$
其中 $C_{20}$ 是完整正规加速度平方 $\bar A_{hh}$ 的原系数。R350 已付
$\mathcal N(C_{20})=0$；因此
$$
n_4=-c_0n_6.
$$
代入本次 $n_6=0$，准确得到 $n_4=0$。不需要重新计算 $c_0$，也没有从旧两头看不到的方向中猜出它。

由 R196 的真基
$$
U_0=\mathcal R_0\oplus
\operatorname{span}\{C_2,C_4,C_6\}
$$
及(6)，每个 $V_0\in U_0$ 满足
$$
\boxed{\mathcal N(V_0)=\lambda_+(V_0)\,n_2.}
\tag{18}
$$
故
$$
\boxed{
\begin{aligned}
\mathcal N(U_0)&=\mathbb R n_2,\\
(E,\mathcal N)(U_0)&=E(U_0)\oplus\mathbb R n_2,\\
(E,\mathcal N)(\mathcal R_0)&=E(U_0)\oplus\{0\}.
\end{aligned}}
\tag{19}
$$
第二、三式使用已付的 $E(U_0)=E(\mathcal R_0)$：先减一个匹配 E 的真实响应，再用 $H_*$ 提供任意 $n_2$ 系数。因此(19)中的直和是真像，而不只是一个外部包含。

这给增强权零商的准确维数一。它不声称整个 $\mathcal N(U)$ 只有一维；R393 的其他真权自然函数仍在原范围内。

在旧 $E$ 核中，R400 的准确表示还给
$$
\boxed{
U_0\cap\ker(E,\mathcal N)
=(\mathcal R_0\cap\ker E)
\oplus\operatorname{span}\{J_4,J_6\}.
}
\tag{20}
$$
其中直和来自原三个商类独立。特别，(20)中 $\lambda_+$ 恒为零。

## 6. 正字符实际经过完整自然映射单独下降

这一步比只用 R404 的增强核判据略强，所需协变已在
[R365 独立第 5 节](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)
从原同锚输运证明：
$$
\Lambda_u(P_{H,c}V)
=H^2\Lambda_{C_{H,c}u}(V),
\qquad (C_{H,c}u)(x)=u((x-c)/H).
\tag{21}
$$
该节的协变不依赖 R365 后来更正的旧 H 非零结论。

因此 $\ker\mathcal N$ 自身就对真实正缩放稳定。原 $U$ 只有有限个真权，有限个 $H=1$ 附近的正缩放线性组合可以取出 $\Pi_0V$。于是
$$
\mathcal N(V)=0
\ \Longrightarrow\
\mathcal N(\Pi_0V)=0
\ \overset{(18)}{\Longrightarrow}\
\lambda_+(V)n_2=0.
$$
由 $n_2\ne0$，
$$
\boxed{\ker\mathcal N\subseteq\ker\lambda_+.}
\tag{22}
$$
所以存在唯一的良定义线性泛函
$$
\boxed{
\ell_+:\mathcal N(U)\longrightarrow\mathbb R,\qquad
\ell_+(\mathcal N(V))=\lambda_+(V).
}
\tag{23}
$$
它非零，因为 $\ell_+(n_2)=1$。
(21)及原 $\lambda_+$ 的仿射不变性，还给这个下降泛函在真实自然像上的相应不变性。没有把两个固定 profiles 的核误当作(22)。

可把(23)写成一个可核的有限读出。选定一个真实紧 $u_*$ 满足 $n_2(u_*)\ne0$，取
$u_H(x)=u_*(x/H)$。由(21)，成本真权 $\sigma$ 对应自然函数缩放幂 $\sigma-2$，故
$$
\boxed{
\lambda_+(V)
=\frac{[H^{-2}]\Lambda_{u_H}(V)}
{n_2(u_*)}.
}
\tag{24}
$$
方括号是原有限 Laurent 展开的准确系数。只用足够多个固定正 $H$ 的值就能通过有限线性插值取出它；选在 1 附近可保所有支持和 collars。这里不进行新数值插值或求秩。

(24)不是一个任意单 profile 的值；其他成本真权会在同一 profile 上混合。它说明完整自然函数确实包含原正字符，却不宣称 R390 的那两个固定读出已包含该字符。

## 7. 真正实际的 canonical 障碍及其长度来源

[R196 第 7 节](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)
给完整 normal 字符值和同一个八矩乘子：
$$
\lambda_+F_0=k^2-hk,\qquad
\mu_+=(0,0,2,0,0,0,0,0),\qquad
\mu_+m_0=-hk,\quad\mu_+m_2=0.
\tag{25}
$$
原 R109 局部化保留全部历史。对同端口常数 germ、闭 frame、$M_B=0$ 的 canonical 成本，$\lambda_+$ 杀掉全部响应历史差；原 $\Gamma M_B$ 和 $\mu_+M_B$ 也为零。因此
$$
\lambda_+(V_B)=\int_B k^2\,ds.
\tag{26}
$$
这是实际成本恒等式，不是把一个静态 normal 系数的符号直接解释成某个闭路径成本。

原八矩密度还满足
$$
p_1+4t_1
=\frac12\left\{k^2-1-(h_s/h)^2\right\}.
\tag{27}
$$
这里 $p_1,t_1$ 是矩阵坐标，不是 profile 导数。
零八矩使(27)积分为零，于是
$$
\lambda_+(V_B)=L_B+\int_B(h_s/h)^2\,ds>0
\quad(L_B>0).
\tag{28}
$$
结合(23)，得到首段(3)。

原 $U$ 的定义即使先取 $M=\mathbf T=0$ 字，也不会在这里把非零第三矩的闭路漏掉：原真倒行在 $M=0$ 时满足
$\mathbf T_{B^R}=-\mathbf T_B$、$V_{B^R}=V_B$，
而同端口拼接 $BB^R$ 的成本为 $2V_B$。故闭 frame 的 $M=0$ 成本属于同一线性 $U$，且(26)可直接使用 R196 的完整局部化结论。特别，$\mathbf T_B=\tau H$ 不构成例外。

所以准确的禁止结论是
$$
\boxed{
\begin{gathered}
B\text{ 为上述正时长真实 }M=0\text{ canonical 闭成本}\\
\Longrightarrow\quad
\mathcal N(V_B)\ne0,\qquad
(E,\mathcal N)(V_B)\ne0.
\end{gathered}}
\tag{29}
$$
常 $h$ 时(28)仍等于 $L_B$；非恒定 $h$ 只增加非负项。不能把本结论弱写成只禁止 $h_s\ne0$，也不能把它强写成所有固定圆上的 period 都不可能为零。

由于所有实际成本在下降泛函上严格为正，完整增强实际成本锥不可能是整个线性像。因而不能把 R333 的 whole E 截面与完整自然函数任意指定的截面直接拼接。这是已经证实的必要障碍，不再是 R400/R404 中的待定分支。

## 8. 精确实际收据与费用

本稿已直接读取完整原 job 日志及其中两个新报告，并核对：

| 对象 | 字节数 | SHA256 |
|---|---:|---|
| 原完整 job log | 123807 | fffe1b37deb54839af548cd50b155b956c4338744490f02668f8967f239ceda2 |
| 新科学报告 JSON 加 LF | 31231 | 776e3f3fbe1872c877018a5b22a792203eac09265d589391d59223b7c11f758c |
| 八项新人工报告 JSON 加 LF | 15799 | 178ae038bf708e2afbba1069a28e65063c3ead5c6fb4956fa341bc78c8b79436 |

原日志与完整输出可从上述公开 job 及冻结请求重取。表中对象是 stdout/runner 临时输出的准确身份，不声称它们被作为可重算 payload 新增提交。完整密度和数学推论证明以本稿保留；其余原词表不另上传 artifact、Release 或数据文件。

实际结果为：
$$
\text{outcome}=\text{n6\_zero\_n2\_nonzero},
\qquad n_2\in\operatorname{span}\{n_6\}\text{ 为 false}.
$$

| 费用 | 实际值 |
|---|---:|
| 总研究 elapsed | 6.656628646 s |
| 已付回执只读 | 1.699476147 s |
| 两 static 加六 response 的必要输入恢复 | 4.239038564 s |
| 两条新完整观察 | 0.712408647 s |
| 峰值 RSS | 114136 KiB |
| 新 primitive 调用 | 458 |
| 固定颜色 IBP | 313 |
| 严格下降检查 | 646 |
| 非空余 word 的多项式 IBP | 28 |
| shuffle 调用 | 9 |
| 最大 word 长度 | 3 |
| cache 峰值 | 1586 |
| cycle fallback | 0 |

上述三个子费用来自原报告，末位相加可能与总计因其他极小开销略有差别。独立 literal monitor 记 10 次、最大整数位数 0；原报告明确它**不是完整 DAG 算术计数器**，本稿不拿它冒充整个研究的有理运算总数。

八项新人工全部通过，范围只有：准确 MAIN framing、外乘符号与五次 Euler、$3+2$ 有序余项保留、完整五次总导数、最高 jet、原共同右锚、真权偏移、完整两函数关系判据。人工 elapsed 为 0.008901954 s。旧人工套件及旧研究目标没有重复执行。

## 9. 与其他已付结论相容的边界

本次已经结清两条原完整函数、自然权零一维像、原正字符的自然下降及实际 universal 零障碍。下列范围仍须区别：

- R333 的 whole pure 与左二次 self 联合控制仍成立；其代表 $H_*$ 恰具有本稿的非零自然通量，不构成矛盾。
- R390 的两个固定自然读出、R392 的响应 E 分量与固定两读出联合控制，仍按其原有限目标成立。它们没有要求(29)中的整个自然函数为零。
- R389/R397/R405 等对指定微包、指定 period 的条件性范围与同纤维局部不变性，不由本稿自动变成不可能，也不自动获得所有余量为零。指定包上的有限总通量可以落在非零 universal 自然函数的零集。
- 原共同二阶修正 $w$、内部退化点、全部平台/端 germ、固定 $g$ 的主目标和更广的非 canonical 输出，不由本稿直接排除。要应用(28)，须给该固定输出或允许 gauge 上的实际因子化，不能用 universal 空间结论替代。
- 其余低层 $F_0/\widehat Q_2$ 的全自然函数像没有由“一维权零”全部求清；未知 $c_0$ 的数值也没有执行新研究。它已不影响本稿结论，因为 $n_6=0$。

本稿只用一次新的公开观察确定原待定函数，再以已付真实空间、同锚协变和完整实际 action 推出(18)–(29)。没有重新运行旧秩，也没有将一个线性 normal 记录冒作实际可任意取正负的闭路径。
