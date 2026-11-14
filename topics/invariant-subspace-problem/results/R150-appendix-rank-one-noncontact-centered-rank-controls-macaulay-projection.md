# R150 附录：非接触秩一均值的中心算子秩控制原 Macaulay 投影

## 1. 统一结论

仍使用原六维物理核、原 Hankel 二/三阶矩以及全部十七条中心临界方程。取有限物理源点 $s$，规范 $y=v(s)$，并设

$$
u=v'(s),\quad Y=y^2,\quad T=yu^T+uy^T,\quad
p=Ky,\quad q=Ku,\quad g=u^TKu\ne0.
$$

因此本条的非接触条件为 $s\notin\{0,2,-6\}$；无穷远接触点另已处理。设 $r=\operatorname{rank}A_y$。对[泛参数稿](R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)定义的完整 $224\times155$ 投影矩阵，

$$
\boxed{\operatorname{rank}P(s)\le124+2r.} \tag{1.1}
$$

特别地，$r=9$ 给出 $142$；$r=8$ 给出更锐的 $140$。该结论逐个复源点成立，无需先在函数域构造有极点的核再专门化。

由[精确中心算子秩定理](R150-appendix-rank-one-centered-linear-operator-exact-rank.md)，全部 $P_+$、$P_-$ 和 $E_8$ 根均为非接触 $r=8$ 源点。因此在这三组全部复根上，原 $6188\times4367$ 五次 Macaulay 矩阵都有统一上界

$$
\boxed{\operatorname{rank}\mathcal M_5(s)\le4212+140=4352.} \tag{1.2}
$$

这里尚未给出各组的大矩阵下界，故上界本身不把这些均值的完整临界分类写成已完成。若另证某组原大矩阵的特征零秩达到 $4352$，则本条第 6 节直接给出该组全部临界点 $T_3=0$。

## 2. 原线性代数接口

记 $\mathcal H_2$ 为十一维 Hankel 矩阵空间。原配对

$$
\langle X,Z\rangle_K=\operatorname{tr}(KXKZ)
$$

在此空间非退化，Gram 矩阵为可逆的 $J_2$。$A_y$ 对此配对自伴随，且 $Y,T\in\ker A_y$。

令 $\Pi$ 将任意对称矩阵取为具有相同原物理极线多项式的唯一 Hankel 代表。对 Hankel $X$，

$$
\langle X,\Pi Z\rangle_K=\langle X,Z\rangle_K.
$$

始终使用这个投影表示原十一条 $N(Kv,Kv)=0$ 条件；没有把一般对称矩阵 $N$ 当成 Hankel，也没有补加矩阵条目条件。

按原二项式矩平移，写

$$
M=cY+dT+Z,\qquad Z\in\mathcal N,
$$

其中 $\mathcal N$ 是由九个横向坐标 $z_2,\ldots,z_{10}$ 组成的补空间，$\mathcal H_2=\operatorname{span}(Y,T)\oplus\mathcal N$。设

$$
e=9-r.
$$

则 $A_y|_{\mathcal N}$ 的核有维数 $e$，而 $\ker A_y$ 有维数 $e+2$。

## 3. 原最高恒等式消去两个障碍

对任意 $w\in\mathcal H_2$，若 $A_yw$ 为 $Y$ 的倍数，则

$$
\boxed{p^Twp=0.} \tag{3.1}
$$

证明只需原恒等式

$$
(L_yw)(Kv(t),Kv(t),Kv(t))
=p_y(t)\,w(Kv(t),Kv(t)),
\qquad p_y(t)=y^TKv(t).
$$

左侧在 $t=s$ 的二次项只涉及 $(L_yw)_p=A_yw$，故因 $y^Tp=y^Tq=0$ 而为零。右侧二次项是 $(-g/2)p^Twp$；$g\ne0$ 给出 (3.1)。

特别地，$Y$ 正交于整个 $\ker A_y$。自伴随性因此给出

$$
Y\in\operatorname{im}A_y.
$$

定义

$$
\mathcal U=\{w\in\mathcal N:A_yw\in\mathbb CY\}.
$$

因为 $Y$ 是非零像向量，而横向核维数为 $e$，

$$
\dim\mathcal U=e+1. \tag{3.2}
$$

对任意 $w_c,w_d\in\mathcal U$，令

$$
S=YK w_c+w_cKY+TKw_d+w_dKT.
$$

矩阵等式 $YKY=YKT=TKY=0$ 及 $(KT)^2=gpy^T$ 给出

$$
\langle Y,\Pi S\rangle_K=0,\qquad
\langle T,\Pi S\rangle_K=2g\,p^Tw_dp=0. \tag{3.3}
$$

所以判断 $\Pi S$ 是否属于 $\operatorname{im}A_y$ 时，$\ker A_y$ 中 $Y,T$ 两个障碍恒自动消失。至多只剩 $e$ 个线性障碍。

## 4. 低次数支撑的完整右核计数

完整投影保留二十个纯 $c,d$ 单项式（次数 $1$ 至 $5$），以及九组 $z_jc^\alpha d^\beta$（$\alpha+\beta\le4$），共 $155$ 列。十七式乘纯切向次数至多三的十个单项式，加五十四个 $z_jd^2c^\alpha d^\beta$ 单位行，给出全部 $224$ 行。

除了十个取出 $c^\alpha$ 或 $c^\alpha d$ 系数的显然右核，考虑只支撑于下列单项式的泛函：

$$
d^2,\ cd^2,\ d^3,\quad z_j,\ cz_j,\ dz_j
\quad(2\le j\le10).
$$

用 $t_0,t_c,t_d\in\mathbb C$ 表示三个纯切向取值，用 $w_0,w_c,w_d\in\mathcal N$ 表示三组横向取值。原 $N$ 及其 $c,d$ 乘子的零条件恰为

$$
6A_yw_c+4g t_cY=0,\qquad
6A_yw_d+4g t_dY=0, \tag{4.1}
$$

$$
6A_yw_0+4g t_0Y+
4\Pi(YKw_c+w_cKY+TKw_d+w_dKT)=0. \tag{4.2}
$$

更高纯切向乘子和五十四个单位行都在该泛函的支撑以外，自动取零。

完整六维均值梯度的交叉恒等式为

$$
\mathcal B_\Gamma(Y,Z)=-12(A_yZ)_p,\qquad
\mathcal B_\Gamma(T,Z)=-24(A_yZ)_q.
$$

因此 (4.1) 也自动消去六个 $\Gamma$；其允许乘子同样不增加条件。这一步包含完整均值梯度，并非只取均值曲线的切向导数。

现在作精确维数计数。由 (4.1)，$w_c,w_d$ 可取于 $\mathcal U$，而 $t_c,t_d$ 由它们唯一确定，所以起初有 $2e+2$ 个参数。由 (3.3)，使 (4.2) 可解的条件至多为 $e$ 条，故可解对 $(w_c,w_d)$ 的空间至少有 $e+2$ 维。

对每个可解对，$(w_0,t_0)$ 的解纤维具有维数

$$
\dim\ker\bigl[(w,t)\mapsto6A_yw+4gtY\bigr]
=10-r=e+1,
$$

因为 $Y\in\operatorname{im}A_y$。因此上述低次数泛函的空间至少有

$$
(e+2)+(e+1)=2e+3
$$

维。泛函的取值与参数一一对应。其支撑与先前十个纯切向系数泛函不相交，故总右核维数至少为 $13+2e$。这证明

$$
\operatorname{rank}P(s)\le155-(13+2e)
=142-2(9-r)=124+2r.
$$

这是维数下界；若某个额外障碍也自动为零，右核只会更多，因此不需假设障碍恰有 $e$ 条。

## 5. 两个三次域的精确计算记录

作为原系数重算记录，$P_\pm$ 两组已另外完成精确数域计算。令 $\theta=5s$，对应首一三次为

$$
F_+(\theta)=\theta^3-25\theta^2+160\theta-200,
$$

$$
F_-(\theta)=\theta^3+135\theta^2+4320\theta+21600.
$$

它们在 $\mathbb F_{11}$ 均无根，所以在 $\mathbb Q$ 上不可约。只保留纯切向次数至多三的九列及横向切向次数至多一的二十七列，原十七式乘 $1,c,d$ 得 $51\times36$ 小矩阵。两域中均精确有秩 $25$、十一独立核。零扩至完整 $155$ 列并加 $c^4,c^5,c^3d,c^4d$ 四个纯坐标核后，分别得到十五个完整右核。

两域均已将十五核直接代入全部 $224$ 行：每域 $3360$ 个数域等式、即 $10080$ 个整数系数等式全部为零；自由坐标的 $225$ 项对角核对也全部通过。输入没有将各参数处 primitive 行直接插值：先乘回各行 scale 得固定 $D=\det J_3$ 倍原式，再按已知次数界 $25$ 用 $s=0,\ldots,25$ 做整系数 Newton 重建，额外 $s=26$ 的全部 $476$ 个系数也精确相符。之后统一乘 $5^{25}$，在首一三次域中约减。

这些计算与第 4 节的解析证明一致。[完整确定性重建器](../notes/2026-11-14-rank-one-cubic-number-field-projection-verify.js) 从已发表的原 $J_3$ 数据和原整数系统生成器重建两域全部矩阵与核；[参数、校验计数及 SHA256 回执](../notes/2026-11-14-rank-one-cubic-number-field-projection-verification.json) 记录该统一入口在代码模式中的实际完整执行。两族的规范完整核 JSON 分别为 $94636$、$124325$ 字节，按根 README §8 只保存可忠实重建的入口与哈希，不上传或分块保存大核。

重建器导出 `verifyRankOneCubicNumberFieldProjections(data, buildSystem, report)`；`data` 是原六模式精确 JSON，`buildSystem` 是已发表的 `buildRankOneCenteredIntegerSystem`，`report` 可省略。作为普通 Node.js 文件直接运行时，它自动读取相邻的原数据和生成器，输出全部检查回执。上界解析证明及对 $E_8$ 的适用性均不依赖重跑作为额外门槛。

## 6. 大矩阵下界的直接使用规则

对上述任一非接触 $r=8$ 源点，如果另行证明原大矩阵在特征零有秩至少 $4352$，则

$$
4352\le\dim\mathcal L_5\le4212+\dim\pi(\mathcal L_5)
\le4212+140=4352.
$$

于是 $(I^2)_{\le5}\subseteq\mathcal L_5$，所有复数临界点的九个横向坐标都为零。$g\ne0$ 再从原 $N=4gd^2Y$ 迫使 $d=0$，最后得到

$$
H=h y^2,\qquad V=(6h-1)y^3/4,\qquad T_3=0.
$$

对不可约代数均值，良好素数的简单剩余根处一个原固定整模型最大子式非零，可给出该数域的下界并覆盖全部复共轭根；须明确使用原固定倍式及相应整模型。若模素数秩不足，只能更换素数或继续分析，不能据此推断复数存在或不存在。

本条提供已证明的统一上界及完整提升接口；三组代数均值的大秩证书、一般有限集合 $\Sigma$ 的显式控制及原 ISP 的自然幂/实际逆仍须各自完成。
