# 原 41 处域、好约化模型与 sigma 的固定倍率输入

日期：2026-11-16。状态：**纸面证明和已成来源的纯 IO 核对；本篇没有新的 41 进点值、sigma、周期或高度计算。**

本篇补足 [SP 原 CM sigma 与 Poincaré 周期接口](2026-11-16-original-CM-sigma-and-Poincare-period-inputs.md) 的真实 $p=41$ 输入。SP 已给原 $\mu_3$ 补空间、sigma 规范、除法函数和全尾界；这里确定实际分歧、共同好约化扩域及**不依赖未知点坐标的倍率 $42$**。原 R725 模型、R791 相位、R840 的 U.1 准确表达式和 RF 的纤维常数全部保留。

## 1. 原 $b$ 与指定完成处

沿 R725、R735 固定
$$
K=\mathbf Q(s),\quad s=1+2\zeta,\quad s^2=-3,\qquad
C_b:\ y^2=x^3+b,\quad \omega_b=\frac{dx}{2y}.
\tag{41S.1}
$$
$b$ 是原正 $\kappa_4$ 模型的系数，不作 sextic twist 替换。记 $F_{41}(Z)$ 为 R735 已准确输出的首一七次最小多项式。实际证书给出七个非首项系数的 $41$ 进赋值全为 $1$、判别式赋值为 $6$、$F_{41}(b)=0$ 及原模型身份。本文不重新计算这些系数或判别式。全局 $F_b=\mathbf Q(b)$ 的指定实嵌入给 $b>0$，其签名为 $(1,3)$，不称它全实。

固定 R725 的原 $41$ 进嵌入。令
$$
F=F_b\otimes_{\mathbf Q}\mathbf Q_{41}=\mathbf Q_{41}(b),\qquad
K_{41}=\mathbf Q_{41}(s),\qquad L_{41}=F(s).
\tag{41S.2}
$$
Eisenstein 性给 $[F:\mathbf Q_{41}]=7$、$\mathcal O_F=\mathbf Z_{41}[b]$、$v_{41}(b)=1/7$；此扩张温和全分歧。$41\equiv2\pmod3$ 使 $K_{41}/\mathbf Q_{41}$ 未分歧二次，故
$$
[L_{41}:\mathbf Q_{41}]=14,\quad e(L_{41}/\mathbf Q_{41})=7,\quad
\kappa(L_{41})=\mathbf F_{41^2}.
\tag{41S.3}
$$
这是原 $L=F_bK$ 的指定完成处，不换 $s$ 的正 CM 标签。

R781 原字段写作 $B=\lambda b$，实际记录 $\lambda=2^6 3^{180}$，所以 $\lambda$ 是 $41$ 单位。本次纯 IO 已逐对象核对 R781 的 original_b_minimal_polynomial 与 R735 的 minimal_polynomial 完全相同。可用原 $B$ 整多项式表示同一个域，但必须保 $B=\lambda b$，不能将 $B$ 当模型常数。

R781 的实圆分参数是 Laurent 方程的 $20$ 个系数坐标；U.1 将这 $20$ 个系数取出后，$2420$ 阶系统的系数属于原 $L$。这一表示不要求把另一个 $20$ 次圆分扩域并入点值域。原点属于 $L$ 的依据是 R616 的 $c_1\in X(\mathbf Q)$、原同态的 $L$ 定义性及 R791/R841/R844 的准确下降，不是看到一个 $280$ 维文件便自动断言点值域。

## 2. 实际次数 $84$ 的共同好约化扩域

R725.13、725.26 已固定
$$
b=r_0^6,\qquad \alpha_4=\sqrt[3]4,\qquad
r=r_0/\alpha_4,\qquad 16r^6=b.
\tag{41S.4}
$$
$r$ 保持原角色相位。R725.12、725.27–28 给 $H=K(r)$、$[H:K]=42$、$[H:L]=6$。在本处 $\alpha_4$ 为单位，原 $\kappa_{4,41}$ 平凡，无隐藏立方分歧。设
$$
E=L_{41}(r)=H_{41}.
$$
$R^6-b/16$ 对 $L_{41}$ 的整数赋值为 Eisenstein，故
$$
[E:\mathbf Q_{41}]=84,\quad e(E/\mathbf Q_{41})=42,\quad
f(E/\mathbf Q_{41})=2,\quad v_{41}(r)=1/42.
\tag{41S.5}
$$
具体可表示为
$$
G(R)=16^{-7}F_{41}(16R^6),\qquad
E=\mathbf Q_{41}(s)[R]/(G(R)),\quad R\mapsto r.
\tag{41S.6}
$$
$G$ 是 $42$ 次首一 Eisenstein 多项式。原嵌入由 $b=16r^6$、原 $s$ 和 $r_0/\alpha_4$ 指定；这个代数表示不授权另选相位。

$\mathcal O_E$ 可用整基 $s^j r^i$，$j=0,1$、$0\le i<42$。各 $r^i$ 的赋值权为 $i/42$，$1,s$ 是未分歧二次域的整基。若有理系数误差满足 $v_{41}(\Delta c_{ij})+i/42\ge N$，则元素误差至少为 $N$。后继必须记这种绝对精度，不能将普通系数位数等同于元素赋值精度。

准确同构仍是
$$
\varphi_r:E_{27}\longrightarrow C_b,\qquad
E_{27}:\ Y^2=X^3+16,\qquad
(X,Y)\longmapsto(r^2X,r^3Y),\qquad
\varphi_r^*\omega_b=r^{-1}\omega_{27}.
\tag{41S.7}
$$
$E_{27}$ 在 $41$ 好约化；原 $C_b/L_{41}$ 是 R725/R735 的类型 II 最小模型。没有把原 Néron 微分改为好约化微分。

$H/K$ 的原循环 Galois 作用把七个 $b_\tau=\tau(b)$、$r_\tau=\tau(r)$ 放在同一个 $E$ 中。每个分量使用自己的 $r_\tau$ 和原 $\rho_\tau$ 运输，并保 $16r_\tau^6=b_\tau$。原同态在 $L$ 定义且 $c_1$ 为 $\mathbf Q$ 点，所以六个原 $f,g_j$ 点、其 $[1-\zeta^2]$ 实下降点及七个真实共轭均在相应 $C_{b_\tau}(L_{41})$ 中；经 (41S.7) 后才视为 $E_{27}(E)$ 的点。

## 3. 固定倍率 $42$ 消去整个归约群

在 $\mathbf F_{41}$ 上立方映射为双射。因此对二次特征 $\chi$，
$$
\sum_{x\in\mathbf F_{41}}\chi(x^3+16)
=\sum_{u\in\mathbf F_{41}}\chi(u+16)=0.
\tag{41S.8}
$$
故 $\#E_{27}(\mathbf F_{41})=42$、Frobenius 迹为零。Frobenius 特征方程给
$$
\pi^2+[41]=0.
\tag{41S.9}
$$
对 $\overline Q\in E_{27}(\mathbf F_{41^2})$ 有 $\pi^2\overline Q=\overline Q$，所以
$$
[42]\overline Q=O.
\tag{41S.10}
$$
这不是点扫描或群阶猜测。特征方程可参见 Sutherland 的 [MIT 18.783 Lecture 8, §8.2](https://math.mit.edu/classes/18.783/2022/LectureNotes8.pdf)，其引用原 Theorem 6.18。

**具体倍率结论。** 对任意原非挠 $P\in C_b(L_{41})$，设 $Q=\varphi_r^{-1}P$，则
$$
[42]Q\in\widehat E_{27}(\mathfrak m_E)\setminus\{O\}.
\tag{41S.11}
$$
此结论逐字适用于七个共轭，同时覆盖未实下降的 $f(c_1),g_j(c_1)$ 和六个实下降点。它们的非挠性及原 Hom 字非零已由 R843/R844 认证，无需再做点值零测试。若 RF/SP 改用未下降点组织求值，三同源、纤维、角色及 trace 的比较仍须原样运输。

记好约化参数 $T=-X/Y$、原参数 $\xi_b=-x/y$，有 $T=r\xi_b$。从 (41S.11) 得 $v_{41}(T)\ge1/42$，故
$$
v_{41}\bigl(\xi_b([42]P)\bigr)\ge0,\qquad
v_{41}(b)+6v_{41}\bigl(\xi_b([42]P)\bigr)
=6v_{41}\bigl(T([42]Q)\bigr)\ge\frac17.
\tag{41S.12}
$$
形式分支还满足 $T^2X\equiv1\pmod{\mathfrak m_E}$。因 $\xi_b^2x=T^2X$，
$$
v_{41}\bigl(\xi_b([42]P)^2x([42]P)-1\bigr)>0.
\tag{41S.13}
$$
SP.26 的两个收敛条件因而同时成立；不能只凭第一条件选原分支。

## 4. 可选逐层加深与统一全尾界

$42$ 已足够收敛。若实际精度需求确有必要，可只追加原 $[41]$，不重做已成 $[42]$。R725 §2 已证原好约化形式群高度 $2$：$[41](T)$ 的线性项为 $41T$，次数 $2,\ldots,41^2-1$ 的系数被 $41$ 整除，其余系数整，模 $41$ 首个非零次数为 $41^2$。

当 $v_{41}(T)\ge1/42$ 时，$(41^2-1)v_{41}(T)>1$，所以线性项严格有最小赋值，得到
$$
v_{41}([41](T))=1+v_{41}(T).
\tag{41S.14}
$$
令 $n_a=42\cdot41^a$，归纳得
$$
v_{41}(\xi_b([n_a]P))\ge a,\qquad
A_a:=v_{41}(b)+6v_{41}(\xi_b([n_a]P))\ge\frac17+6a.
\tag{41S.15}
$$
这里没有生成新形式群系数。

将此代入 SP.27，对 $m,n\ge1$ 有
$$
v_{41}\!\left(F_m b^m\xi^{6m}\right)
\ge\frac m7+6ma-v_{41}(m)
-\max_{1\le n\le m}v_{41}(6n-1),
\tag{41S.16}
$$
$$
v_{41}\!\left(\frac{H_n b^n\xi^{6n-1}}{6n-1}\right)
\ge\frac n7+(6n-1)a-v_{41}(6n-1).
\tag{41S.17}
$$
$\xi=\xi_b([n_a]P)$；第一式用 $41\nmid6$。截断须使这些式子对整个余尾成立，可按 SP.28 的对数上界与最终单调性处理，不能只看最后保留项。

原 $\mathcal Z_b$ 的有理项 $(3u-2)/\xi$ 仍按真实点 ball 求逆，不以尾估计替代。SP.21 中除 $n_a^2$ 损失 $2a$ 个单位精度；SP.22 两项分别按 $a$、$2a$ 运输。初次 $a=0$ 没有该整数除法损失。是否加深由真实精度与成本决定，本篇没有执行选择。

## 5. sigma、除法函数与帧的准确缩放

记 $\sigma_{16},\mathcal L_{16},\mathcal Z_{16}$ 为同一 SP 规范在 $E_{27}$ 上的对象。由
$$
\xi_b^2x=T^2X,\qquad b\xi_b^6=16T^6,\qquad
\sigma_b(\xi_b)=r^{-1}\sigma_{16}(T)
\tag{41S.18}
$$
及 SP 的 cubical 延拓，得到
$$
\boxed{\quad\mathcal L_b(P)=\mathcal L_{16}(Q)-\log_E r,\qquad
\mathcal Z_b(P)=r\,\mathcal Z_{16}(Q).\quad}
\tag{41S.19}
$$
第三式保了 $\sigma/\xi\to1$ 的原帧，故 $-\log_E r$ 不能因改用好模型而消失。

SP 的规范是 $\psi_n\xi^{n^2-1}\to n$，所以
$$
\psi_{b,n}(P)=r^{n^2-1}\psi_{16,n}(Q),\qquad
D_{\omega_b}\log\psi_{b,n}(P)
=r\,D_{\omega_{27}}\log\psi_{16,n}(Q).
\tag{41S.20}
$$
例如 $\psi_{b,2}=-2y=r^3(-2Y)$，与 $n^2-1=3$ 一致。倍率 $42$ 给具体入口
$$
\mathcal L_b(P)=
\frac{\log_E T([42]Q)+F_{16}(T([42]Q))
-\log_E\psi_{16,42}(Q)}{42^2}-\log_E r,
\tag{41S.21}
$$
$$
\mathcal Z_b(P)=r\left[
\frac{\mathcal Z_{16}([42]Q)}{42}
-\frac{D_{\omega_{27}}\log\psi_{16,42}(Q)}{42^2}
\right].
\tag{41S.22}
$$
同一原曲线参数 $z=a-1$ 下，若 $P^*\omega_b=h\,dz$，则
$Q^*\omega_{27}=rh\,dz$，故
$$
\mathcal Z_b(P)h=\mathcal Z_{16}(Q)(rh).
\tag{41S.23}
$$
$h$ 仍取原 R791/R846 切向规范；没有丢 $82$ 尺度或将模参数化常数称为 $41$ 单位。

设 $a_0=F_{41}(0)$，则 $N_{F_b/\mathbf Q}(b)=-a_0$。七个原共轭的常数可保为
$$
\sum_{\tau=0}^{6}\log_E r_\tau
=\frac16\log_{41}(-a_0)-\frac76\log_{41}(16).
\tag{41S.24}
$$
它只来自 $\prod_\tau r_\tau^6=(-a_0)/16^7$，有限单位根的对数为零。这里 $a_0$ 是首一多项式的真实常数系数，**不是共同清分母后的整数分子**。此式消费既成原范数的表达式，没有新求数值对数，也不能据此删除 RF 的其他常数。

## 6. 角色 trace 与精度

沿 SP.6 保原角色与分支：
$$
\chi_E=\frac1{84}\chi_{41}\circ N_{E/\mathbf Q_{41}}.
\tag{41S.25}
$$
$84$、$42$ 都是 $41$ 单位。若元素误差 $\epsilon$ 满足 $v_{41}(\epsilon)\ge N$，每个共轭有同一下界，因此
$$
v_{41}\!\left(\frac1{84}\operatorname{Tr}_{E/\mathbf Q_{41}}\epsilon\right)\ge N.
\tag{41S.26}
$$
故本具体规范化 trace 自身不必扣整数精度。若原 $\operatorname{tr}_{\chi,E}$ 还带指定有理角色尺度 $c_\chi$，须再加 $v_{41}(c_\chi)$；本文不将该原尺度改为 $1$。同样，
$$
\chi_E(r)=\frac1{42}\chi_{41}(-a_0)-\frac16\chi_{41}(16).
\tag{41S.27}
$$
这与七项求和 (41S.24) 不同，不能将两个操作混为一次。

坐标运输仍有实际损失：$X=r^{-2}x$、$Y=r^{-3}y$ 分别使绝对误差下界减 $2/42$、$3/42$；$\xi_b=r^{-1}T$ 减 $1/42$，$\mathcal Z_b=r\mathcal Z_{16}$ 加 $1/42$。这以 $r$ 为准确域生成元；若另用近似 $r$，还要计其真实 ball 误差。

R728 的 inverse different $F'_{41}(b)^{-1}$ 和原 Néron/Weil trace 格按原定义保留。元素误差论证不把带负赋值的对偶基当整基，更不证明原 $J_X\to A$ 的格在 $41$ 饱和。

## 7. 原乘法 DAG 与尚未计算的数值入口

对每个原点和共轭可固定使用
$$
P,\ 2P,\ 4P,\ 5P,\ 10P,\ 20P,\ 21P,\ 42P.
\tag{41S.28}
$$
这里只新增五次 doubling 和两次加法。非挠性保证 doubling 的 $y\ne0$，且 $4P\ne\pm P$、$20P\ne\pm P$；两个 secant 分母因而准确非零。零判来自 R843/R844 原 Hom 字，不用有限精度近零猜测。原 $\psi_{42}$ 及其对数导数按 SP.15/24 的规范作记忆化除法函数递推，不必展开高次除法多项式。每个已成节点携带原点 ID、模型和 $r_\tau$；optional $41$ 加深只追加新节点。

finite-precision affine 运算只对已知有限赋值的分母求逆。若当前 ball 尚不确定一个已证明非零的分母，则增加输入精度，不把不确定零当准确零，也不拿非 primitive 射影坐标的公共因子作形式参数证书。有限个真实分母均非零，精度递增有严格终止依据；本篇没有预填其实际损失。

### 7.1 必须来自 U.1 或实际通过 A.1 的原点

辅助 $\ell=1000000753$ 的 $518$ 位响应不能变成 $41$ 处输入。当前短 $14$ 坐标候选尚未通过 A.1，不能作为本消费者的原点。合法路径是：

1. 读取 R840 的 exact-source-bound-implicit-expression；其中 unit_chart_solve、operator_recipe、linear_responses 及全部源 SHA 准确定义 $A_0,A_1,B_0,B_1$。在原 $L_{41}$ 求这个同一系统的有限精度值，再沿 R841/R844/R846 原 DAG 求点与切向。
2. 以后若 A.1 有准确成功证书，才使用其绑定同一原点的展开坐标；当前没有这条成功来源。

U.1 原行序、free column $1186$、其他 free 坐标为零、原带符号 $Z$ 和全部 $129\times280$ 关系身份必须保留。R840 的辅助单位 witness 已证明 $B_0$ 准确非零，**不证明它在 $41$ 是单位**。原 $2420$ 图的行列式也只是准确非零，不能将辅助 $\ell$ 模逆当成 $41$ 模逆。

可执行的入口是：从旧准确系数构造同一 $2420$ 矩阵与四条响应泛函，在 $L_{41}$ 用绝对精度消元共用求解；pivot 或分母未确定就增加源精度。系数皆准确数域数，行列式及最终分母准确非零，故这个有限系统的求值严格可终止。它只新算目标地方的响应，不重生原 q 前缀，也不要求先展开全部 $2420$ 个有理数域坐标。本文不虚报其尚未运行的成本或成功精度。

### 7.2 最小来源责任

| 输入 | 已成来源 | 后继保留 |
|---|---|---|
| 原域和模型 | R735 证书、R781 字段 | $F_{41}$、$B=\lambda b$、原 $s,\kappa_4$ |
| 四准确响应 | R840 U.1 和完整系数闭包 | 原行序、$Z$、free $1186$、全局关系 |
| 六组点及共轭 | R841/R844 准确节点 | 旧节点原字节、七共轭、$\rho$ 尺度 |
| 非零分母 | R843 非挠、R844 Hom 字 | 原点身份，不重非挠计算 |
| 原一阶 | R791/R846 | $z=a-1$、$h$、$82$ 和同源尺度 |
| line-log 和角色 | SP/RF | $\psi_2=-2y$、$-\log r_\tau$、原 $\nu/\kappa$、真 trace |

GLOBAL 当前 carrier 保留 U.1 原 $1234$ 行、R781 准确 Laurent、字段和来源；POINTS 当前 carrier 保留点/切向/非挠闭包。后继只取实际需要的原成员并续传，不能因单独旧 artifact 到期重算。机器对象、新 ball/series 只在一日 active artifact/carrier；Git 只存源码、参数、证明及简明运行/SHA 登记。

真正的 $41$ 消费器应分别输出原域/嵌入身份、四响应实际 ball、各 $[42]$ ball 和原 $u\equiv1$ 分支、规范除法函数及其对数导数、实际全尾界、原帧和 trace 运输。尚未完成的 ball、run、artifact、精度都不能预填成功。对称椭圆部分完成也不抹去原 $Y$-Picard 周期、全局线性校正或非 $p$ 项；本文没有宣称原高度或全 $p$ 主目标完成。

## 8. 本次已核来源定位

- R735：run $43608152850$，source $ff405af51e13bb966fecd066a14513eee0947702$。p41-original-CM-model-certificate.json，$19620$ bytes，SHA256 $752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574$。
- R781-original-real-field-input.json.gz：$833786$ bytes，SHA256 $528720fe45edf23c1d065c034bd4d8be3c2e2905e45079d9e4a5c71015f7b5b1$。本次只读核原多项式对象一致，无系数重算。
- R840 的 R787-implicit-CM-exact-source-bound-implicit-expression.json.gz：$72708$ bytes，SHA256 $21cc66ed9a40a856edea495080ef2e375aefea6c6f17d6c26741b85e2f174342$。
- R841 的 R792-CM-DAG-original-point-program.json.gz：$7239$ bytes，SHA256 $acaf1a1eea1346461c267209c236ae737b9f762cbfc794a9eaaf7c2ca93bbbb1$。
- R844 的 R792-Hom-word-DAG-five-addition-point-program.json.gz：$68403$ bytes，SHA256 $97a8fb3f185660468e6637358c9c29b34bfe8630599f36fa7e7f58ef6acb582b$。原 base/g 和 real_base/real_g 各七分量均保原 curve_b 与 same_target_conversion，不能混用模型。
- R791-original-Hom-Galois-matrices.json.gz：$15617$ bytes，SHA256 $f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183$。原 $T^7=\zeta^2$、$\sigma(b)$、$\rho$ 均不另选。

本篇新增的是具体共同倍率、盘界与本实际扩域的尺度/精度专门化。上述登记均是既成来源，没有新的点值或周期运行。
