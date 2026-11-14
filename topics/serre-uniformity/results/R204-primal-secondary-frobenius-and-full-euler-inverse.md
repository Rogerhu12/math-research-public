# R204：完整 $\Gamma$–Euler 逆与固定 $\{2,p\}$ primal 二阶 Frobenius 值

**状态：已证明。** 固定 R171 的 $p=43$、同一 $q$、实 $P$ 和 Weil 根，
沿用 R189 的 primal 单位类 $c_p$、R196 的 $\kappa_p$、
R198 的实 $p^2$ 标记。本条构造一个支撑仅在 $\{2,p\}$ 的参考
Norm 原始子 $B_p$，满足
$$
\delta B_p=(-i\kappa_p)\cup c_p,
\qquad (B_p)_q=24F_0.
\tag{204.1}
$$
有限坐标是 R168 的规范；$F_0=\operatorname{diag}(1,-1)$。
它是指定 Robert 参考构造的二阶 Frobenius 坐标，
不是任意原始子都相同的绝对不变量，也不是 R201 的 $\mathcal L$。
完整 $\Omega_2$ 仍未计算。两种共轭辅助同源各做 $79464$ 个实际
分母评价，得到相同的规范值 $24$。

## 1. 系数、完整层与原始函数

令 $K=\mathbb Q(i)$、$A:y^2=x^3-x$，
$T=K(A[p])$、$T_2=K(A[p^2])$。
固定
$$
P_2=(i,1-i),\quad \tau P_2=iP_2,\quad
\tau P=P,\quad pR=P,\quad\tau R=R.
\tag{204.2}
$$
primary 元素固定的是 $P_2$，并不固定 $R$。
设
$$
\mathcal T=T_2^{\,1+p\mathbb F_p}=T L_p,\qquad
\Gamma=\operatorname{Gal}(\mathcal T/T)=\langle\gamma\rangle\simeq C_p.
\tag{204.3}
$$
这里只除去标量 $p$ 方向，不能把整个 primal 类放进 $44$ 次域：
$U=W(-1)$ 的标量角色为 $k^{-2}$，通常非平凡。
$\Gamma$ 的生成元由 $\kappa_p(\gamma)=1$ 固定。

$C=\operatorname{Gal}(T/K)=\mathbb F_{p^2}^{\times}$ 阶 $1848$，
在 $\mathcal T$ 中取其唯一 prime-to-$p$ 的 tame 提升。
$U$ 的 $C$ 角色为 $a^{-2p}$，$\tau$ 作用为 $-\bar{\phantom x}$。
对 $\beta=-1+2i$、$\bar\beta=-1-2i$，取
$$
v_\beta(Q)=\frac4{\beta x(Q)^2+1}.
\tag{204.4}
$$
直接 CM 加法公式给非零 $A[\beta]$ 的 $x$ 坐标为
$\beta x^2+1=0$；故
$\operatorname{div}v_\beta=5[O]-A[\beta]$。
它与规范 Robert 函数至多差 $K^\times$ 常数。
下述非平凡 $C$ 投影杀掉这些常数。

在 $T$ 层把 $v_\beta$ 评价在 **$P_2+P$**，
在 $T_2$ 层评价在 **$P_2+R$**。
不能删掉 $P_2$ 或只评价未平移的标记。
取标量 $p$ 方向的 Norm 后，再作 R189 的同一投影：
$$
\Xi_{\beta,0}=\frac1{1848}\sum_{a\in C}
 a^{-2p}[\sigma_a v_\beta(P_2+P)],\quad
\Xi_{\beta,2}=\frac1{1848}\sum_{a\in C}
 a^{-2p}\left[\sigma_a
 N_{T_2/\mathcal T}v_\beta(P_2+R)\right].
\tag{204.5}
$$
可先在 Teichmüller $\mathbb Z_{p^2}$ 系数的单位完成中定义，
再模 $p$；这使群环逆和 Norm 都有精确含义。
函数 Norm 关系来自与 $\beta$ 互素的 $[p]$ 同源。
$[p]P_2=-P_2$，函数偶，标量角色也在 $-1$ 上平凡，故
$$
N_\Gamma\Xi_{\beta,2}=\Xi_{\beta,0}.
\tag{204.6}
$$
支持在 $\{2,p\}$ 外为单位。R198 §1.1 的 Scholl/Robert 分布关系
适用于这里的奇数度同源；规范常数已被所需字符投影消去。

## 2. 正 Artin 与必须保留的 $\Gamma$ 因子

primary $\beta$ 的 Galois 作用是 $P\mapsto\beta P$，
这是 R171、R196 固定的正 CM Artin 方向。
对单位投影，tame 特征值为 $\bar\beta^2$。
R196 精确给
$$
\kappa_p(\operatorname{Frob}_\beta)=21,\qquad
\kappa_p(\operatorname{Frob}_{\bar\beta})=22.
\tag{204.7}
$$
因此真正的 Euler 算子为
$$
E_\beta=5-\bar\beta^2\gamma^{21},\qquad
E_{\bar\beta}=5-\beta^2\gamma^{22}.
\tag{204.8}
$$
其增广分别为
$$
e_\beta=8-4i,\qquad e_{\bar\beta}=8+4i,\qquad
N(e_\beta)=80.
\tag{204.9}
$$
$p=43\nmid80$，所以它们在完整 $p$ 进 $\Gamma$ 群环中可逆。

这里的 Artin 方向也可自含核验。
对两个 primary 辅助元素 $\beta,\delta$，比较
$$
\frac{v_\beta(Q)^{N\delta}}{v_\beta(\delta Q)}
\quad\text{和}\quad
\frac{v_\delta(Q)^{N\beta}}{v_\delta(\beta Q)}.
$$
二者除子同为
$$
N\beta N\delta[O]-N\delta A[\beta]
 -N\beta A[\delta]+A[\beta\delta].
$$
故相差 $K^\times$ 常数，投影后消失。
评价 $Q=P_2+R$ 时 primary 元素固定 $P_2$，
所以对应算子是正作用 $\sigma_\beta:R\mapsto\beta R$：
$$
(N\delta-\sigma_\delta)\Xi_\beta
 =(N\beta-\sigma_\beta)\Xi_\delta.
\tag{204.10}
$$
这证明 (204.8)，并排除只凭数值吻合选择正负号。

定义
$$
Z_2=E_\beta^{-1}\Xi_{\beta,2}
    =E_{\bar\beta}^{-1}\Xi_{\bar\beta,2},\qquad
Z_0=e_\beta^{-1}\Xi_{\beta,0}.
\tag{204.11}
$$
(204.10) 给辅助无关性，(204.6) 给 $N_\Gamma Z_2=Z_0$。
$Z_0$ 的 Kummer 类正是 R189 的 $c_p$ 参考类。
完成中的张量定义足够构造模 $p$ 原始子：
取有限普通单位幂代表，误差 $p$ 次幂或底域单位的 Norm 修正
在 $D$-Kummer 类中消失，因为
$\sum_{j=0}^{p-1}j=p(p-1)/2$ 被 $p$ 整除。
因此没有把形式投影错误当作一个未证明存在的普通 Norm 解。

## 3. $\tau$、实标记与 $q$ 素点

从 (204.2) 精确得到
$$
\tau(P_2+aR)=iP_2+\bar aR
           =i(P_2-i\bar aR).
\tag{204.12}
$$
$v_{\bar\beta}(iQ)=v_{\bar\beta}(Q)$，
所以标签替换是 $a\mapsto-i\bar a$。
$U$ 的 $-\bar{\phantom x}$ 与该标签的
$\chi(-i)=(-i)^{-2p}=-1$ 相消，
得 $\tau\Xi_{\beta,2}=\Xi_{\bar\beta,2}$。
同时 $\tau\gamma\tau^{-1}=\gamma^{-1}$，
故 $\tau E_\beta=E_{\bar\beta}$，(204.11) 按同一规范下降。
这一步使用完整 $p^2$ 层的实 $R$，没有忽略 $\Gamma$ 作用。

在 R198 的 $q$ 素点，$\mathcal T/T$ 完全分裂。
$q$ Frobenius 在反循环层上是一个 involution；
在保持残余素点的 $\Gamma$ 共轭中，
因 $p$ 为奇数，恰有一个使其为所选全局 $\tau$。
等价地，令 $H=\langle P\rangle$、$E_H=A/H$，
选唯一实 $Q=\phi_HR$，对偶满足 $\widehat\phi_HQ=P$。
其他原像是 $Q+tS$，$S=\phi_H(iP)$，共轭变为 $Q-tS$。
程序实际检查这个实 $Q$ 与对偶等式。
因此此处 $\kappa_p$ 的 cocycle 可规范为零。
这很重要：$c_{p,q}\ne0$，不能像 R198 的 dual 零类一样
任意改变 $\kappa_p$ 的局部零阶规范后仍声称数值不变。

## 4. 完整 Euler 逆的导数公式

在 $\mathbb F_{p^2}[\Gamma]$ 写
$$
D=\sum_{j=0}^{p-1}j\gamma^j,\qquad
N=\sum_{j=0}^{p-1}\gamma^j.
$$
则
$$
D(\gamma-1)=-N,\qquad
D(\gamma^k-1)=-kN,\qquad N(\gamma^k-1)=0.
\tag{204.13}
$$
若 $E=e-b(\gamma^k-1)$，则所有二次及更高项经左乘 $D$ 后消失，
故精确有
$$
\boxed{DE^{-1}=e^{-1}D-kbe^{-2}N.}
\tag{204.14}
$$
因此在本例
$$
DZ_2=e_\beta^{-1}D\Xi_{\beta,2}
 -21\bar\beta^2e_\beta^{-2}\Xi_{\beta,0}.
\tag{204.15}
$$
只除增广 $e_\beta$ 会遗漏第二项。
由于 $c_{p,q}$ 的有限值为 $10$，该项在此处确实不为零。

## 5. 实际有限域求值

保留 R198 的 $44$ 条 tame CM 轨道
$P_j=\beta^jP$、$E_j=A/\langle P_j\rangle$、
$S_j=\phi_j(iP_j)$，以及
$$
Q_{j+1}=\beta_jQ_j-11S_{j+1}.
\tag{204.16}
$$
$\Gamma$ 分支为 $Q_j+21tS_j$。
每条轨道上，辅助 $\beta$ 的诱导核由
$T_j=\phi_j(T_\beta)$、$2T_j$ 的 $x$ 坐标给出，
对应分母
$$
d_{\beta,j}(X)=(X-x(T_j))(X-x(2T_j)).
\tag{204.17}
$$
取 $w_k=k^{-2}\pmod{43}$ 的整数代表。
标量 $p$ Norm 通过 Vélu 商给
$$
v_{j,t}=
\prod_{k=1}^{42}
 d_{\beta,j}\!\left(x(\phi_jP_2+k(Q_j+21tS_j))\right)^{w_k}.
\tag{204.18}
$$
同源规范常数与 $k$ 无关，因
$\sum k^{-2}=0\pmod{43}$ 而在此 Kummer 商中消失。
全 $C$ 投影的轨道权为
$$
(\beta^{-2p})^j=(36+5i)^j.
\tag{204.19}
$$
原函数是分母的倒数，但 $1848^{-1}=-1$，
两个负号抵消；所以程序的正分母对数就是 $\Xi$ 的局部值。

程序分别用 $T_\beta$ 和其共轭 $T_{\bar\beta}$，各做
$44\cdot43\cdot42=79464$ 次分母评价。
每一条轨道都检查 $N$ 的符号与低层相同；
全部 $P,Q,S$ 在 $44$ 步后为原来的 $[5]$。
结果为：

| 量 | $\beta$ | $\bar\beta$ |
|---|---:|---:|
| 原始低层投影 | $31+6i$ | $31-6i$ |
| 原始 $D$ 投影 | $10+6i$ | $33+6i$ |
| $e^{-1}$ 倍低层 | $20$ | $20$ |
| $e^{-1}$ 倍原始 $D$ | $5+14i$ | $38+14i$ |
| (204.14) 的减项 | $5+19i$ | $38+19i$ |
| 完整 $DZ_2$ | $38i$ | $38i$ |

两种辅助的完整群环归一化完全一致。
未经 Euler 校正的两值既不相等，也没有正确的实下降。
这提供了独立数值交叉核验，但 Artin 方向的证明是 §2 的
全局函数等式，而非仅依赖这次吻合。

## 6. 正原始子与 $i/2$ 因子

在 $\kappa_p$ 分裂的 $q$ 点，R191 正 Norm 原始子为
$-\kappa(DZ_2)$，故其 $K_q$ 值为
$$
-38i=5i.
$$
实际 primal 的纯 $p$ reference 差是 $-i\kappa_p$；
乘 $-i$ 后得到 $K_q$ 的有限值 $5$。
从未分歧二次 $K_q$ 返回 $\mathbb Q_q$，
有限 Frobenius 坐标除 $2$：
$$
\boxed{(B_p)_q=(5/2)F_0=24F_0.}
\tag{204.20}
$$
$\tau$ 平均不再带另一个 $2$：§3 已给完整下降，
这里的除 $2$ 仅来自 Frobenius 限制。

可以把这个构造称为一个固定 $\{2,p\}$ 的二阶参考扩张，
但需明确其定义。令 $j(x,y)=-ixy$，
在 $\eta\oplus W\oplus W$ 上用群律
$$
(x,y,z)(x',y',z')
 =(x+x',y+y',z+z'-j(x,y')).
\tag{204.21}
$$
带残余 Galois 作用的
$(\kappa_p,c_p,B_p)$ 是该有限群的非交换 cocycle，
因为 $\delta B_p=j(\kappa_p\cup c_p)$。
取其半直积表示的核即得有限扩张，支撑在 $\{2,p\}$；
$q$ 的第三个、正原始子坐标按上述实标记是 $24$。
若改用正号交叉项的群律，第三坐标应写为 $-B_p$，
不能悄悄改变“Frobenius 值”的符号。

这个标记参考扩张不是实际椭圆曲线的 Tate 模。
另一个普通原始子可以加全局 $H^1(W)$，
其 $q$ 值未必仍为 $24$；本条固定的是 (204.11) 的 Robert 构造。
辅助 $\beta$ 与 $\bar\beta$ 的更换无歧义，由 (204.10) 保证。

## 7. 未完成的主障碍

R201 的 $\mathcal L$ 来自 $q$-ray Norm 见证和固定的
$C_{44}/\tau$、$S$ 支撑、模 $p^2$ 根规范。
本条是纯 $p$ 扩张上的 primal 二阶值。
尚未证明一个互反公式把它直接等同于 $\mathcal L$，
也未处理由此桥接可能带来的 finite/singular 或 reference 修正。
因此不据 $24$ 宣称 $\mathcal L=24$、$\Omega_2\ne0$，
更不把它当作 Serre 一致性的统一排除。

## 8. 源与证书

- [verify_r204_primal_secondary_frobenius.js](../scripts/verify_r204_primal_secondary_frobenius.js)
- [r204_primal_secondary_frobenius_certificate.json](../notes/r204_primal_secondary_frobenius_certificate.json)

~~~sh
node scripts/verify_r204_primal_secondary_frobenius.js notes/r204_primal_secondary_frobenius_certificate.json
~~~

源内嵌精确 $q,P,Q,T_\beta,\zeta$，验证 Miller 配对、两次
$43$ 同源、所有点方程及阶，再完成两种辅助的 $88$ 行计算。
传 JSON 时比较全部行；`--certificate <路径>` 生成证书。
本轮实际重跑输出含
~~~text
status=PASS
denominator_evaluations=158928
all_88_weighted_norm_symbols_equal=true
corrected_D=(0,38) for both auxiliaries
positive_primal_secondary_Frobenius=24
actual_L_computed=false
~~~

主要来源：R189、R191、R196、R198；
A. J. Scholl, *An introduction to Kato's Euler systems* (1998),
Theorem 1.2.1(iii)、Remark(iv),(v)，printed pp.384–386：
<https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf>。
Euler 交叉关系、完整逆公式、标记下降及正原始子符号
均已在本条直接证明。
