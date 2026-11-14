# R282 — 真 $T_p$ 的全环带转置、原零的准确传播及新原函数的十六维实际轨道

日期：2026-11-13。**状态：以下完整测度转置、p-depletion、质量与尺度导数、原三零的准确轨道范围、CM5 交换、一个明确普通 ray 类上的有限 Heisenberg 定标，以及 R277 实际奇原函数的全十六角色和非零归一轨道行均已证明。最后的非零行属于已明确的原函数伴随；尚未证明原三曲线中央导数之一非零。**

本篇使用 R263/R266/R280 的同一个
$$
T_p=b_{17}[b_0^2]_*\psi_p,\qquad
\psi_p\nu=(x\mapsto x/p)_*(\nu|_{p\mathbb Z_p}).
\tag{1}
$$
全篇首先区别 $p$-core 与单位 Mellin，再作有限来源计算。

## 1. 全 $u$ 转置必须读原测度的第 $n$ 环带

设 $\nu_G$ 为原普通测度，$d=p-1$。定义
$$
M_G^{[n]}(u)=
\int_{p^n\mathbb Z_p^\times}
 \left\langle x/p^n\right\rangle^{du}\,d\nu_G(x),
\qquad n\ge0,
$$
其中 $M_G^{[0]}=M_G$ 才是原单位 Mellin。
所有单位幂采用原 $p$-adic 分支。

**定理 1。** 对全部原定义域中的 $u$，
$$
\boxed{
M_{T_p^nG}(u)
=b_{17}^{\,n}(b_0^{2nd})^u M_G^{[n]}(u).
}
\tag{2}
$$
特别地
$$
\boxed{
\begin{aligned}
M_{T_p^nG}(0)&=b_{17}^{\,n}M_G^{[n]}(0),\\
M_{T_p^nG}'(0)&=b_{17}^{\,n}
 \left(M_G^{[n]\prime}(0)
 +2nd\log_pb_0\,M_G^{[n]}(0)\right).
\end{aligned}}
\tag{3}
$$

**证明。** (1) 在第一个单位环带上把 $x\in p\mathbb Z_p^\times$
送到 $b_0^2x/p$，并乘真实质量因子 $b_{17}$。
逐次迭代得到 $b_0^{2n}x/p^n$ 和 $b_{17}^n$，即 (2)。
对原解析单位核求导给 (3)。$\square$

p-depletion 在完整 Amice 源上也有精确式：
$$
\boxed{
G^\times(z)=G(z)-b_{17}^{-1}
 (T_pG)(pz/b_0^2).
}
\tag{4}
$$
这是限制到 $\mathbb Z_p^\times$ 的实际变换。
因此对任意正整数 $k$，
$$
\int_{\mathbb Z_p^\times}x^k\,d\nu_G
=\Omega_0^k k!\left(
 [z^k]G-b_{17}^{-1}(p/b_0^2)^k[z^k]T_pG
\right).
\tag{5}
$$
同一参考 $\vartheta$ 满足 $T_p\vartheta=(b_{17}/b_0)\vartheta$，故 principal 正权的无周期比值为
$$
\boxed{
\frac{M_G(j)}{M_\vartheta(j)}
=
\frac{[z^{jd}]G-b_{17}^{-1}(p/b_0^2)^{jd}[z^{jd}]T_pG}
 {(1-b_0^{-1}(p/b_0^2)^{jd})[z^{jd}]\vartheta}.
}
\tag{6}
$$
这保留了真 Euler 因子；对一般 $G$，分子含 $T_pG$ 而非任意指定的标量。

为同时处理非零质量的伴随，令
$$
J_8=M_{S_8},\qquad m_8=J_8(0)=1-b_8^{-1}\in\mathcal O^\times,
$$
并定义线性的归一中央泛函
$$
\mathscr L_p(G)=
\left.\frac d{du}\frac{M_G(u)}{J_8(u)}\right|_{u=0}.
\tag{7}
$$
对原 $A,B,H$，其单位质量为零，所以 $\mathscr L_p(G)=M_G'(0)/m_8$；
对一般伴随却必须保留参考导数。

令 $Q_G^{[n]}=M_G^{[n]}/J_8$。由 (2)，准确有
$$
\boxed{
\mathscr L_p(T_p^nG)=b_{17}^{\,n}
\left(Q_G^{[n]\prime}(0)
 +2nd\log_pb_0\,Q_G^{[n]}(0)\right).
}
\tag{8}
$$
这就是后文所有轨道观察的真实含义。

仅知 $M_G(0)=M_G'(0)=0$ 不提供 (8) 的右端。
例如，任意原单位测度 $\lambda$ 先按 $p$ 缩放，
其单位 Mellin 恒为零，而 (1) 会读取它的非零第一环带。
有限 theta 闭合、可逆矩阵或有限阶本身不会补出缺少的环带条件。

## 2. 原三零可以合法传播到哪些轨道

R263 的完整 Euler 比较已经证明
$$
T_pS_D=\mu_D S_D,\qquad
\mu_D=b_{17}/b_D,\qquad D=17,34^2,136.
\tag{9}
$$
这里 $S_D$ 分别是同一原 $S_A,S_B,S_H$；
原单位缩放已经保留。因此全部 $u$ 都有
$$
\frac{M_{T_p^nS_D}(u)}{J_8(u)}
=\mu_D^n\frac{M_{S_D}(u)}{J_8(u)}.
\tag{10}
$$
原完整零及质量零确实推出这些轨道全部 $\mathscr L_p=0$，
并由 (2) 反推出它们各自的原环带零。

若再作 R280 的真实范数二拉回，则
$$
M_{S_D(\alpha z)}(u)=(\alpha^d)^uM_{S_D}(u),\qquad \alpha=1+i.
$$
求导多出的 $d\log_p\alpha$ 乘原质量准确为零。
故在 $18+17$ 块中，已授权的零轨道仍只有
$$
\boxed{
\operatorname{span}\{S_A,S_B\}\ \text{的两条原线，和}\ 
\operatorname{span}\{S_H\}\ \text{的一条原线}.
}
\tag{11}
$$
各 $\mu_D$ 相异时，从一个三源和的全部轨道可以恢复这三条线；
相位相同时轨道更小，不会因此得到新的原函数行。

R277 的 $S_*=S_A+S_B+\kappa S_H$ 本身及其 $T_p$ 轨道属于 (11)。
但它的角原函数分量 $G_{\rm e},G_{\rm o}$ 并不是 (11) 中的来源；
(9) 不为它们提供全 Euler 标量或完整零。
以下明确计算其中真正的奇分量 $G_{\rm o}=WP_R$。

## 3. 真 $T_p$ 与固定 CM5 算子交换

R248 在 $\mathcal H_+=W\mathbb Q(i)[U]_{\le16}$ 上给出
$$
\mathscr M_5=[2+i]_*[2-i]^*,\qquad
\mathscr N=\mathscr M_5/(2+i),
$$
$$
\mathscr N^{16}=1,\qquad
\det(X-\mathscr N)=(X-1)(X^{16}-1).
\tag{12}
$$
零角色秩二，其余十五个角色各秩一。
零角色准确由 $S_8(\beta z),S_8(\bar\beta z)$ 张成，$\beta=4-i$。

**定理 2。** 对所有当前普通 $p\ne5,17$，
$$
\boxed{T_p\mathscr N=\mathscr NT_p.}
\tag{13}
$$
而且在零角色二维空间上，$T_p$ 是同一标量
$$
\mu_8=b_{17}/b_8.
\tag{14}
$$

**证明。** 先作共同 $[2]$ 拉回，放入无 twist 的正空间 $\mathcal S_{272}$。
对 Gaussian 整数 $a$ 定义真实
$\mathscr M_a=[a]_*[\bar a]^*$，采用 R266 的同一个 sigma frame 与正有限平坦迹。
若 $a,c$ 的相关 CM 核互素，两次迹的双纤维可唯一写为
$$
ac\,t=z,\qquad w=ct,\qquad v=\bar a t.
$$
两层原 frame 比的乘积准确伸缩为
$$
\frac{\sigma(\bar a ct)}{\sigma(act)}
\frac{\sigma(\bar c\bar a t)}{\sigma(c\bar a t)}
=\frac{\sigma(\bar a\bar c t)}{\sigma(act)}.
$$
交换 $a,c$ 得到同一个有限平坦纤维、同一个比和同一个被拉回函数。
因此 $\mathscr M_a\mathscr M_c=\mathscr M_c\mathscr M_a$，没有未定相位。
R266 的实际 $T_p=(b_{17}/p)\mathscr M_\pi$，故得到 (13)。
共同 $[2]$ 拉回是原单位缩放，恒等式返回原 $\mathcal H_+$。

最后，完整 Euler 给 $T_pS_8=\mu_8S_8$。
$T_p$ 与 $\beta,\bar\beta\in\mathbb Z_p^\times$ 的缩放交换，
所以在两个明确的零角色基向量上都是 $\mu_8$。$\square$

由 (13)，每条非零角色线各自稳定。
所以 $T_p$ 在 $\mathcal H_+$ 上是这些十六个角色投影的标量和；
这并未把任一个新角色的 $M_G$ 宣称为原 $M_H$ 的倍数。

## 4. 一个明确普通 ray 类上的全部有限矩阵定标

下面完整付出固定 residue 描述，避免只在十七端猜测相位。
设
$$
N=272,\qquad 2N=544,\qquad
\gamma_5=-1+2i=i(2+i).
$$
$\gamma_5$ 是 $E_0$ 在范数五素位的实际 primary Frobenius；
不能用非 primary 的 $2+i$ 作为原 $\pi_0$ 的模 $544$ 同余目标。

考虑所有满足
$$
\boxed{\pi_0\equiv\gamma_5\pmod{544\mathbb Z[i]}}
\tag{15}
$$
的普通好素位，排除有限坏素数。

### 4.1 对称 Heisenberg lift 的完整相位

令 $\Gamma$ 为原平方格、$\eta_\lambda$ 为 sigma quasi-period。
对 $v\in N^{-1}\Gamma$ 定义实际对称 lift
$$
(\mathsf T_vG)(z)
=e^{-N\eta_v(z+v/2)}G(z+v),\qquad G\in\mathcal S_N.
\tag{16}
$$
$N$ 为偶数，原 sigma 半特征的 $N$ 次幂为一。
由 Legendre 关系直接检查
$$
\mathsf T_{v+2\lambda}=\mathsf T_v\quad(\lambda\in\Gamma),
$$
$$
\mathsf T_v\mathsf T_w
=e^{N(\eta_vw-\eta_wv)/2}\mathsf T_{v+w}.
\tag{17}
$$
对两个标准 $N$ 挠生成元，交换子是 primitive 的 $N$ 次根单位。
在 $N$ 维 $\mathcal S_N$ 上，此表示不可约：
一个生成元的特征向量被另一个生成元循环到 $N$ 个不同特征值，
已用满全部维数。任何共同不变子空间都包含整个循环基。

选 Gaussian $d_a$ 满足
$\bar a d_a\equiv1\bmod2N$，并置 $q=d_av$。
于是 $\bar a q-v\in2\Gamma$。平方格的
$\eta_{a q}=\bar a\eta_q$ 给精确 pull/trace 协变
$$
[\bar a]^*\mathsf T_v^N
=\mathsf T_q^{N\mathrm N(a)}[\bar a]^*,\qquad
[a]_*\mathsf T_q^{N\mathrm N(a)}
=\mathsf T_{aq}^N[a]_*,
$$
其中上标 $N\mathrm N(a)$ 表示 theta 次数 $N$ 乘 Gaussian norm $\mathrm N(a)$。
从而
$$
\boxed{
\mathscr M_a\mathsf T_v
=\mathsf T_{a d_av}\mathscr M_a.
}
\tag{18}
$$
这保留了原中心和半相位；模 $2N$ 的选择正是确保 (17) 无额外符号所需的成本。

由 (15)，$\mathscr M_{\pi_0}$ 与 $\mathscr M_{\gamma_5}$
在整个 $\mathcal S_{272}$ 上实现同一个 Heisenberg 自同构。
二者都非零：在已付 CM 参考 $S_8(2\beta z)$ 上有非零本征值。
不可约性使这两个交织相差一个标量。

### 4.2 用真正 CM 参考确定标量

在原偶来源上，
$\mathscr M_{\gamma_5}=\mathscr M_{2+i}$：
在迹中作 $w\mapsto iw$ 后，剩余 $[-1]^*$ 对原偶来源作用为一。
R248 已固定
$$
\mathscr M_{\gamma_5}S_8(\beta z)=(2+i)S_8(\beta z).
$$
另一方面
$$
\mathscr M_{\pi_0}S_8(\beta z)
=\frac p{b_8}S_8(\beta z),
$$
由原 $T_p$ 和 (14) 得出。因此在 (15) 的全部素位上，
$$
\boxed{
T_p\big|_{\mathcal H_+}=\mu_8\,\mathscr N.
}
\tag{19}
$$
这是全部十七维矩阵的相等，包括十二个额外型，
不是只在原 $H$ 特征线上检查的猜测。
四次扭曲的真实 Hecke 比值给 $\mu_8\in\mu_4$，所以还得到
$$
\boxed{T_p^{16}=1\quad\text{于 }\mathcal H_+.}
\tag{20}
$$

(15) 是非空的正密度 ray 类条件。
确切地，在 $K=\mathbb Q(i)$ 的模 $544$ ray class 群中取
主理想 $(\gamma_5)$ 的类。
Chebotarev 给该类正密度的素理想；
度二的有理惰性素理想在按范数计数中密度零，因此有正密度的度一普通素位。
因 $544$ 含原 $E_0$ CM conductor，primary 生成元的单位已经唯一固定，
这些素位正好具有 (15) 的实际 Frobenius 代表。
这和 R263 使用的普通 Chebotarev 输入同属已明确的有限类域论条件，
未附加任何关于中央值或 Wieferich 性质的假设。

(2)、(20) 给全 $u$ 的真实环带周期
$$
\boxed{
M_G^{[n+16]}(u)
=b_{17}^{-16}(b_0^{-32d})^uM_G^{[n]}(u),
\qquad G\in\mathcal H_+.
}
\tag{21}
$$
它联系相隔十六层的环带，**不是**说所有环带都等于原单位行。

## 5. R277 实际奇原函数的全十六角色

令
$$
G_R=WP_R,\qquad P_R(U)=U^{16}R_H(1/U),
$$
其中 $R_H$ 是 R277 的固定角原函数多项式。
固定 CM5 精确计算给
$$
\boxed{\dim\operatorname{span}
\{P_R,\mathscr NP_R,\ldots,\mathscr N^{15}P_R\}=16.}
\tag{22}
$$
因为 (12) 的零角色虽为二维，但一个输入在其中只贡献一个向量，
(22) 等价于全部十六个角色投影都非零。

它在五个已明确来源上的投影为
$$
\begin{aligned}
\Pi_0G_R&=aS_8(\beta z)+bS_8(\bar\beta z),\\
a&=\frac{585163679521633}{117767877427200}
 +\frac{12521105325811}{11776787742720}i,\qquad b=\bar a,\\
\Pi_4G_R&=\frac{194308153049}{1394032640}\,H,\\
\Pi_8G_R&=\frac{93406817523291}{19627979571200}\,S_{2312},\\
\Pi_{12}G_R&=\frac{43939268024957}{9813989785600}\,S_{39304}.
\end{aligned}
\tag{23}
$$
剩余十二个角色的合计余项非零，完整十七个 Gaussian 系数在证书中列出。
因此 $G_R$ 不在旧五维池内，也不是单条已知 CM 参考。
本篇不为十二个额外型重新命名曲线或预设其完整中央值。

[固定精确脚本](../scripts/check-original-odd-primitive-cm5-orbit.py)
及 [完整证书](../scripts/check-original-odd-primitive-cm5-orbit.json)
给 (22)–(23)。
证书用实际 $17\times17$ R248 矩阵、原 $P_R$ 的十七个系数计算；
Krylov 矩阵的实化秩为三十二，并给出一个非零三十二阶有理 minor。
其余投影按原固定参考多项式逐项重构。全部为精确有理运算，无目标素数扫描。

## 6. 在真 $T_p$ 轨道中得到一条完整非零归一行

原单位缩放和同一个 $J_8$ 给
$$
\frac{M_{\Pi_0G_R}(u)}{J_8(u)}
=a(\beta^d)^u+b(\bar\beta^d)^u.
$$
因此
$$
\boxed{
\mathscr L_p(\Pi_0G_R)
=d\bigl(a\log_p\beta+b\log_p\bar\beta\bigr)\ne0.
}
\tag{24}
$$
非零由已在 R245/R246 使用的 Brumer 定理得到：
$\beta,\bar\beta$ 在两个不同十七素位的赋值证明其乘法独立，
故对 $p\ne17$ 两个原 $p$-adic 对数在代数系数上独立；
(23) 的 $a,b$ 非零。

而
$$
\Pi_0=\frac1{16}\sum_{j=0}^{15}\mathscr N^j.
$$
所以对每个允许普通 $p$，至少一个**固定 CM5 轨道**行
$\mathscr L_p(\mathscr N^jG_R)$ 非零。
在 (15) 的正密度普通类上，(19) 更把它准确变成原真实 $T_p$ 轨道：
$$
\boxed{
\exists\,0\le j<16:\quad \mathscr L_p(T_p^jG_R)\ne0.
}
\tag{25}
$$
这个轨道在特征零中有十六维，且每条观察都可由 (8) 读取为原测度的指定环带。

(25) 是实际原函数伴随的完整归一非零，不是一个孤立权系数的非零。
但 $G_R$ 的质量非零；这里使用的是 (7) 的质量修正泛函，
不是擅自删除 $J_8'$ 后的原始导数。
更关键的是，原三中央零只合法传播到 (11)，并未证明
$\mathscr L_p(T_p^jG_R)=0$。
R277 给的仍是包括 $C_*$、$pN_*$、moving log、原点下一位和
R270 tame $-4$ 项的完整聚合。

因此，现在缺少的比较已经具体化：
要把 (25) 中至少一条真实环带观察，接回 R277 的原三源消极组合及
R278 的完整连接，并证明原三零确实消掉该同一观察。
不能用 $T_p$ 的闭合、有限阶、可逆性或十六维轨道代替这一步。

