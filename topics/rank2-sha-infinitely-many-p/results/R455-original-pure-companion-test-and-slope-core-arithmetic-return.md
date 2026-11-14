# R455 — 保斜轴的纯伴随算术测试与正 sigma 矩非零

日期：2026-11-14。**状态：已证明。** R454 的新残余斜轴固定
$Y$ 和 $T_c=Z-33c$，因此纯 $T_c$ 测试可以原样通过其完整核心。
本篇实际构造一个没有常数项、次数为三十六的固定纯 $T_c$ 测试，
完整抽回原算术来源 $S$。它只用六个正次数 $T_c^{6k}$，$1\le k\le6$。

这个测试在原同深非零管中的第五阶系数只含六个正 sigma 矩与
它们的 log 加权矩。全部法向项的有理主系数准确非零；去掉一个
明确固定整数的素因子后，每个正深度的该管中央都恰有赋值 $5n$。
不存在固定负矩非零假设，也不随 $p$ 增长测试次数。

原算术中央零现在确实可传到每条完整的
$\{T\in p^n,T_c\text{ 单位}\}$ 行，且测试不随 $T$ 缩放改变。
本文保留其中 $Z\notin p^n$ 的完整补域，没有由局部非零推出
总中央非零。主目标未完成。

## 1. 同一个 D 正来源与真实正交输出

使用 R451 的实际残余来源
$$
\mathcal L_+=\mathcal L_0+(\mathcal L_1-\mathcal L_R)/2
$$
及同一个独立 sigma 输入 $c$。原物理输出为
$$
Y=Z+c,\qquad X=H-c.
$$
保持 R454 的固定细分 ray
$$
\pi_0\equiv1428552127+2161889730\omega\pmod{2793510720},
\qquad p>19.
\tag{1}
$$
它仍给 $p\equiv7\pmod{64}$，所以当前素数均至少为七十一。
原周期和核心记号为
$$
\lambda=-\bar\pi_0^{-1},\quad
\lambda_\sigma=-\lambda,\quad
\kappa=p/\bar\pi_0^2,\quad
\eta=\eta_{5,p}\in\{\pm1\},\quad
\chi=\chi_p\in\{\pm1\}.
\tag{2}
$$
$\chi$ 是 R454 用完整奇 degree33 trace 与真实两 sigma 锚
付清的符号，不另作选择。

取
$$
\boxed{T=Z-33H,\qquad T_c=Z-33c.}
\tag{3}
$$
原 $Y,T_c,T$ 是真正正交的三个输出，degree 为
$34,1122,18480$；所有 half-character 已由 R454 支付。
反解中特别有
$$
\boxed{Z=(33Y+T_c)/34,\qquad
c=(Y-T_c)/34,\qquad X=(T_c-T)/33.}
\tag{4}
$$
其中最后一式解释了为何需要新的测试：缩放 $T$ 会改变 $X$，
却严格保持 $T_c$。

写 $\Phi_+$ 为此同一三输入测度。R454 的完整核心为
$$
\boxed{\begin{aligned}
\nu_{\widetilde{\mathcal L}_+}|_{Z\in p^r,T\in p^s}
 &=(\chi\lambda)^r(-\eta\chi\lambda)^s
        [\kappa^r,\kappa^s]_*\nu_{\widetilde{\mathcal L}_+},\\
K_Y\Phi_+&=R_Y\Phi_+,\qquad
K_{T_c}\Phi_+=-\chi R_Y\Phi_+.
\end{aligned}}
\tag{5}
$$
第一式原样保独立 $c$，第二式保 $T$。令
$$
\beta_T=-\eta\chi\lambda,\qquad \alpha_c=-\chi\lambda.
\tag{6}
$$
它们是实际单位，且 $1\pm\beta_T,1\pm\alpha_c$ 都由原
$1\pm\lambda$ 单位结论支付。

## 2. 纯 Tc 的完整两输入来源

记
$$
H_{33}=S/\sigma.
$$
原 $S$ 在 sigma 的零点上可除，$H_{33}$ 是整的整个 degree33
来源，且 $H_{33}(z)=z^5+\cdots$。R451 的修正差在第二输入为零
时消失，因此完整有
$$
\boxed{\mathcal L_+^{\rm phys}(y,0)=-\frac23H_{33}(y).}
\tag{7}
$$
由实际输出 $Y=c+Z,T_c=Z-33c$，忘却 $T$ 后的整条来源准确是
$$
\boxed{F_b(y,t)=-\frac23\sigma_b(y-33t)H_{33,b}(y+t).}
\tag{8}
$$
它在 $Y,T_c$ 上的 degree 分别为 $34,1122$，交叉项为
$-33+33=0$。两个 odd 半特征在每个轴上成对抵消，所以
$$
F_b\in\mathcal S_{34}\boxtimes\mathcal S_{1122}
$$
是整个无 twist 的截面。原共同 $\mu_6$ 型为零。

这个忘却只用来计算完整的纯 $T_c$ 测试。
后面附加 $T$ 深条件使用的是 (5) 在同一个三输入来源上的完整
核心；不从 (8) 的边际倒推未保留的条件。

## 3. 六个正 Tc 矩的完整来源与固定提取

对 $0\le k\le6$，记
$$
F_{k,b}(y)=(6k)![t^{6k}]F_b(y,t).
$$
它是测试 $(T_c/\Omega)^{6k}$ 后的整个第一输出来源。
写
$$
\boxed{F_{k,b}(y)=\sigma_b(y)^{34}
 \sum_{a=0}^5 M_{ak}\,b^{k+4-a}x_b(y)^{2+3a}.}
\tag{9}
$$
以下给出完全有限的精确规则，指定这个矩阵的每一项。

### 3.1 六维来源格中的完整系数计算

先令 $b=1$、$w=z^6$，用
$$
x(z)=z^{-2}B(w),\qquad\sigma(z)=zA(w),\qquad
B=1+\sum_{n\ge1}q_nw^n.
$$
真实 Weierstrass 方程和 sigma 规范给
$$
q_1=-1/7,\qquad
q_n=\frac{\sum_{i=1}^{n-1}q_iq_{n-i}}{(6n+1)(n-1)}\quad(n\ge2),
$$
$$
\boxed{\log A(w)=-\sum_{n\ge1}\frac{q_nw^n}{6n(6n-1)}.}
\tag{10}
$$
令
$$
(p_0,\ldots,p_4)=(-128/7,-80/7,-12/7,-53/7,1),
$$
$$
\mathcal H(w)=A(w)^{33}
       \sum_{a=0}^4p_aw^{4-a}B(w)^{2+3a}
       =\sum_{j\ge0}r_jw^j.
\tag{11}
$$
那么 $H_{33}(z)=z^5\mathcal H(z^6)$、$r_0=1$。
写 $a_i=[w^i]A$。六个第一输出 Taylor 坐标的完整基矩阵是
$$
\mathsf J_{\ell a}=[w^{\ell-5+a}]A^{34}B^{2+3a},
\qquad0\le\ell,a\le5,
\tag{12}
$$
负下标的系数定义为零；其反对角线为一，故
$\det\mathsf J=-1$。来源 (8) 的对应六个矩坐标为
$$
\boxed{\begin{aligned}
\mathsf V_{\ell k}=-\frac23(6k)!
\sum_{i+j=k+\ell-1}a_ir_j
\sum_{r=0}^{6k}
 \binom{1+6i}{r}\binom{5+6j}{6k-r}(-33)^r,
\end{aligned}}
\tag{13}
$$
其中越界的二项系数为零。完整矩阵就是
$$
\boxed{M=\mathsf J^{-1}\mathsf V.}
\tag{14}
$$
(10)–(14) 只需 $0\le n\le11$ 的有理系数。
由于已经证明整个来源在六维型零格中，而 (12) 是该格的可逆
完整坐标，读取六个坐标足以证明 (9) 的整条函数身份。
这里没有把未知函数的有限 Taylor 相合当作全局证明。

原第一列给 $F_{0,b}=-2S_b/3$。第一个正矩明确为
$$
M_{[:,1]}=
(-85896216576,-402567874560/7,295133363712/7,
166501438848/7,-12258012096,15840)^{\mathsf t}.
\tag{15}
$$
它本身不是原 $S$ 的倍数，不能直接用 $T_c^6$ 代替原算术测试。

令 $M_+=M_{[:,1:7]}$。全部六列的有理数分母整除七；作为一个
短的严格秩证书，它们模 $101$ 恰为
$$
\begin{pmatrix}
14&12&10&79&99&65\\
26&8&71&68&67&24\\
0&98&87&43&50&37\\
65&69&9&10&99&28\\
61&50&70&79&76&66\\
84&0&100&3&88&34
\end{pmatrix},
\qquad \det\equiv61\pmod{101}.
\tag{16}
$$
这是固定有理矩阵的非零行列式证书，证明其特征零满秩；不是对
目标普通素数的有限扫描。所有特征零系数另完整保存在 JSON 中。

### 3.2 显式无常数算术测试

定义一个固定正整数
$$
L=175514690237655836782990466851591024084630843593462278353768087591349931614071412490240
\tag{17}
$$
和六个整数
$$
\begin{aligned}
N_1={}&64525673881817497042715371790319755143050188359348269398537755464644595548160,\\
N_2={}&92812750343666993527368317773512221689552651053162027988235059200,\\
N_3={}&-51761048015703592573373573845333807192766448323788800,\\
N_4={}&22466365074358601486025583226083415961600,\\
N_5={}&-13308642071886515602651932672,\\
N_6={}&-406079714546741.
\end{aligned}
\tag{18}
$$
写 $c_k=N_k/L$。按 (10)–(14) 的完整有理运算，准确有
$$
\boxed{M_+(c_1,\ldots,c_6)^{\mathsf t}
=(-128/7,-80/7,-12/7,-53/7,1,0)^{\mathsf t}.}
\tag{19}
$$
定义纯伴随多项式
$$
\boxed{\mathfrak h_b(t)=\sum_{k=1}^6c_kb^{-k}t^{6k}.}
\tag{20}
$$
它没有常数项。由 (9)、(19)，在原 $b=17$ 和原周期中，完整
测度身份为
$$
\boxed{(Y)_*\{\mathfrak h_b(T_c/\Omega)\nu_{\Phi_+}\}=\nu_S.}
\tag{21}
$$
特别对整条 principal 参数，
$$
\boxed{\int\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{dz}
        \mathfrak h_b(T_c/\Omega)\,d\nu_{\Phi_+}=J_S(z),
\qquad d=p-1.}
\tag{22}
$$
这里的周期、实际 $S$ 以及它的中央零均未改变。

## 4. 与新斜轴相容的真实零传播

测试 (20) 只依赖 $T_c$；(5) 的 $T$ 核心保持 $Y,T_c$。
因此对每个 $n\ge0$，同一个完整测试准确满足
$$
\boxed{\int_{T\in p^n}\mathbf1_{Y\ {\rm unit}}
 \langle Y\rangle^{dz}\mathfrak h_b(T_c/\Omega)\,d\nu_{\Phi_+}
=\beta_T^nJ_S(z).}
\tag{23}
$$
这是真正的原算术行在细斜线 $U-280X=9T$ 上的传播。
没有把会随此核心改变的 $X$ 测试保留为一个未经运输的旧函数。

还可同时保 $T_c$ 单位。每条 $T_c^{6k}$ 的第一来源 (9) 为
型零，故 $K_{T_c}$ 的 $R_Y$ 对它准确为一。它在 $T_c$ 单位域
上的来源因子就是 $1-\alpha_c\kappa^{6k}$。定义
$$
\boxed{\mathfrak h_{b,p}^{\times}(t)=
\sum_{k=1}^6\frac{c_kb^{-k}}{1-\alpha_c\kappa^{6k}}t^{6k},
\qquad \alpha_c=-\chi\lambda.}
\tag{24}
$$
所有新增分母都是单位。完整有
$$
\boxed{(Y)_*\left\{\mathbf1_{T_c\ {\rm unit}}
 \mathfrak h_{b,p}^{\times}(T_c/\Omega)\nu_{\Phi_+}\right\}=\nu_S,}
\tag{25}
$$
并且
$$
\boxed{\int_{T\in p^n,T_c\ {\rm unit}}
 \mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{dz}
 \mathfrak h_{b,p}^{\times}(T_c/\Omega)\,d\nu_{\Phi_+}
=\beta_T^nJ_S(z).}
\tag{26}
$$
原 $J'_S(0)=0$ 于是确实使 (23)、(26) 的完整中央均为零。
每个式子都有原来源身份支撑，不是仅因这些域可以合法测试。

## 5. 同深管的完整第五阶，只用六个正 sigma 矩

保原同深域
$$
\boxed{\mathscr D_n=
\{Z,H\in p^n,c\text{ 单位}\}
=\{T,Z\in p^n,Y\text{ 单位}\},\quad n\ge1.}
\tag{27}
$$
它在 $\{T\in p^n,T_c\text{ 单位},Y\text{ 单位}\}$ 内，因为
$T_c\equiv-33c\pmod p$。

先使用固定的 (20)。令 $\nu_H=\nu_{-2H_{33}/3}$ 为 (7) 的同一
完整 $Z$ 边际，定义
$$
\boxed{\mathcal A(T_0)=d\int_{c\ {\rm unit}}\int
 \log_p\langle c+T_0Z\rangle
 \mathfrak h_b\left(\frac{T_0Z-33c}{\Omega}\right)
                                     d\nu_H(Z)d\nu_\sigma(c).}
\tag{28}
$$
将 (5) 用于两个真实残余输出，(27) 的中央值准确为
$$
\boxed{\mathcal C_n
=(\chi\lambda)^n\beta_T^n\mathcal A(\kappa^n)
=(-\eta)^n\lambda^{2n}\mathcal A(\kappa^n).}
\tag{29}
$$
这对每个 $n\ge1$ 成立，不再要求深度为偶数。

原 $H_{33}=z^5+O(z^{11})$ 给
$$
\mu_5(\nu_H)=-80\Omega^5,\qquad
\mu_r(\nu_H)=0\quad(0\le r<5).
\tag{30}
$$
对 $m>0$，写
$$
I_m=\int_{c\ {\rm unit}}c^m\,d\nu_\sigma,\qquad
I_{m,\log}=\int_{c\ {\rm unit}}c^m\log_p\langle c\rangle\,d\nu_\sigma.
$$
后者在 $p\mathcal O$ 中。对于 $1\le k\le6$，定义准确整数/有理数
$$
\begin{aligned}
A_k&=\sum_{a=1}^5\frac{(-1)^{a-1}}a
               \binom{6k}{5-a}(-33)^{6k-5+a},\\
B_k&=\binom{6k}{5}(-33)^{6k-5}.
\end{aligned}
\tag{31}
$$
完整展开 log 与多项式，不省去任何同阶法向项，得到
$$
\boxed{[T_0^5]\mathcal A
=-80d\sum_{k=1}^6 c_k b^{-k}\Omega^{5-6k}
       \{A_k I_{6k-5}+B_k I_{6k-5,\log}\}.}
\tag{32}
$$
六个指数依次是 $1,7,13,19,25,31$，全部为正。
与 R450 的特定六次测试不同，这里的 log 加权项未被声称整条
消失；(32) 把它们全部保留。

原 sigma 核心对这些正矩准确给
$$
I_{6k-5}=(1-\lambda_\sigma\kappa^{6k-5})
 (6k-5)!\,b^{k-1}a_{k-1}\Omega^{6k-5},
\tag{33}
$$
其中 $a_{k-1}$ 是 (10) 的固定 sigma 系数。
因此在所有显示系数都整的素数处，(32) 模 $p$ 的值为
$$
\boxed{[T_0^5]\mathcal A\equiv\frac d b\,\alpha\pmod p,}
\tag{34}
$$
固定有理数准确是
$$
\boxed{\begin{aligned}
\alpha&=-80\sum_{k=1}^6c_k A_k(6k-5)!a_{k-1}\\
&=-\frac{135188347596868709906380397884740707393526598671052246381035814315}
{13559034699200566332243539122188477010090222459025420929220870144}\ne0.
\end{aligned}}
\tag{35}
$$
这是完整有理运算，不是根据若干目标素数的模 $p$ 值推断。

## 6. 一个显示的固定有限坏集与每个深度的单位首项

记 (35) 分子的绝对值为 $N_\alpha$。式 (17) 的 $L$ 同时是
六个 $c_k$ 与 $\alpha$ 分母的公倍数。固定排除
$$
\boxed{\mathcal E=\{\text{素数 }p:p\mid 17LN_\alpha\}.}
\tag{36}
$$
右侧三个整数已在 (17)、(35) 完整显示；精确脚本也输出其乘积。
无须猜测或假定这个大整数的素因子分解。该集合有限，删除它后
R454 的同一个固定 ray 仍有无穷多个不同素数。

此后 $\mathfrak h_b$ 的全部系数整、$\alpha$ 是单位；
原周期为单位，六个正 sigma 矩整有界。由 (34)，
$[T_0^5]\mathcal A$ 是单位。低于五阶的全部项由 (30) 消失。

高阶估计也保完整测试。测试次数固定为三十六，log 展开中对
总 $Z$ 次数 $r$ 的可能分母只有 $a=r-j$，$0\le j\le36$、
$a\ge1$；log 常数项没有这样的分母，且仍保在内。
所有单位 $c$ 的正、负矩与原 $Z$ 矩都整，故
$$
v_p([T_0^r]\mathcal A)\ge-\lfloor\log_pr\rfloor.
\tag{37}
$$
对 $p\ge71,n\ge1,r>5$，
$rn-\lfloor\log_pr\rfloor>5n$。于是完整严格结论是
$$
\boxed{v_p(\mathcal C_n)=5n
\quad\text{对每个 }p\text{ 属于 (1) 且 }p\notin\mathcal E,
\text{每个 }n\ge1.}
\tag{38}
$$

式 (24) 的测试与固定 (20) 的系数差在 $p^6\mathcal O$ 中。
按 (30)–(37) 重新读取全部项，单位第五阶不变、此前仍无低阶。
而 (27) 本身已有 $T_c$ 单位，所以 (38) 对实际测试
$\mathbf1_{T_c\ {\rm unit}}\mathfrak h_{b,p}^{\times}(T_c/\Omega)$
同样成立。以下记这个值为 $\mathcal C_n^{\times}$。

## 7. 已传播的原中央与仍保留的一个准确补域

现在测试已经真正保持新 $T$ 核心，原完整中央已由 (26) 支付。
在同一个实际 $\Phi_+$ 中，有精确不交分拆
$$
\{T\in p^n,T_c\text{ 单位},Y\text{ 单位}\}
=\mathscr D_n\ \sqcup\ \mathscr R_n,
$$
$$
\boxed{\mathscr R_n=
\{T\in p^n,T_c\text{ 单位},Y\text{ 单位},Z\notin p^n\},
\qquad Z=(33Y+T_c)/34.}
\tag{39}
$$
所以同一原中央满足
$$
\boxed{\beta_T^nJ'_S(0)
=\mathcal C_n^{\times}
 +\int_{\mathscr R_n}d\log_p\langle Y\rangle
       \mathfrak h_{b,p}^{\times}(T_c/\Omega)\,d\nu_{\Phi_+}.}
\tag{40}
$$
第一项由 (38) 非零；第二项仍保真实 $Z,c$ 单位、深度及相加
carry 的所有分支。原 $J'_S(0)=0$ 只会使第二项等于第一项的负值，
并没有被 (38) 排除。

本篇的推进是：正次数的固定测试完整回到 $S$，它在新细斜轴
核心下严格保持，且可同时支持于另一个伴随单位域；真实非零管
也使用这个同一个算术测试。后续必须处理 (39) 的实际补域，
不能把 (26) 的完整零继续免费分配给 $Z$ 的不同深度。

## 精确文件与依赖

[完整脚本](../scripts/check-r455-pure-companion-arithmetic-test.py)
从 Weierstrass 递推重建全部 sigma 与 $S/\sigma$ 系数、六维
完整坐标、七列来源、显示的六项测试和全部第五阶碰撞。
[完整有理数据](../scripts/check-r455-pure-companion-arithmetic-test.json)
保留每一列、基矩阵、精确行列式、测试系数、六条 log 系数和
固定坏整数。所有计算在特征零准确完成；模 $101$ 仅是固定
行列式的简短非零证书。

- [R454：奇 degree33 绝对符号、真实残余斜轴和 Tc 核心](R454-original-odd33-core-and-exact-residual-slope-transport.md)。
- [R451：同一个 D 正来源与其原算术行](R451-original-dplus-source-and-complete-u-shell-zero-propagation.md)。
- [R450：原六维型零格、全部周期与正矩提取规范](R450-original-sixth-companion-moments-and-exact-arithmetic-extraction.md)。
- [R441：同一原目标管、完整正矩与高尾方法](R441-original-sixth-moment-row-and-uniform-same-depth-nonvanishing.md)。
- [R307：原 S 的完整多项式和共周期算术身份](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)。
