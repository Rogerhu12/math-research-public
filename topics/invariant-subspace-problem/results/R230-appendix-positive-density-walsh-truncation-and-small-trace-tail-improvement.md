# R230 附录：正密度截断、有界交叉代表与小迹尾改进

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_complex；AI 辅助：GPT-6 Astra Pro。状态：以下分解、预算与渐近结论完整证明；一般正常正湮灭者与普通 ISP 仍开。

本稿使用真实正密度的正常性，加强
[实际次数选择器](R230-appendix-actual-cayley-selectors-and-sparse-walsh-escape.md)、
[完整二次矩谱范数](R230-appendix-complete-quadratic-moment-spectral-norm-and-effective-rank.md)
与
[所有固定阶实际矩张量](R230-appendix-all-fixed-order-actual-moment-tensors-and-injective-norm.md)。

关键分解是：固定一个有限 Walsh 投影 $P$，把正密度压到其正交补，得到迹趋小的正密度 $\sigma_P$。
原密度与 $\sigma_P$ 的差在全部实际交换子代数上有一个 $H$ 中的固定真空代表。
其有限头代表在头长增加时一致有界，并强收敛。
这只控制低部和交叉项；不声称小迹的 $\sigma_P$ 自身已有 $H$ 真空代表。

因此，任何发散的规范正头矩，都可以用任意小迹的正密度承担其全部发散部分。
这把已有的固定次数观测界从 $O$ 改为 $o$，并允许原预算中的若干严格小阶条件提高到同阶有界条件。

## 1. 实际乘子、头代表与有限 Walsh 投影

在原 Haar 空间 $H$ 上使用真空 $\Omega$、Walsh 基 $\chi_F$、
$$
C\chi_F=(-1)^{|F|}\chi_F,\qquad
B(u,v)=\langle u,Cv\rangle,
\tag{1.1}
$$
内积对第一变量线性，$C$ 对标量共轭。
实际算子
$$
V_j=(I-N_j)(I+N_j)^{-1}\in\mathcal A,\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}
$$
两两交换、共同 $C$ 对称，并满足
$$
V_F\Omega=\chi_F,\qquad \|V_j\|\le3.
\tag{1.2}
$$
原 $\{A\}'$ 也共同 $C$ 对称，并与这些实际乘子交换。

对有限 Walsh 多项式 $a=\sum_Fa_F\chi_F$，定义有界实际乘子
$$
X_a=\sum_Fa_FV_F,\qquad X_a\Omega=a.
\tag{1.3}
$$
有限头 $[0,m)$ 中相应乘子记为 $X_a^{[m]}$，使用 $V_F^{[m]}$。
若 $a$ 的指标全在该头内，则
$X_a^{[m]}\Omega=a$、$\|V_j^{[m]}\|\le3$。

令 $\Lambda$ 是有限个有限位集组成的集合，
$P_\Lambda$ 为投影到
$\operatorname{span}\{\chi_F:F\in\Lambda\}$。
它与 $C$ 交换。
定义明确预算
$$
K_\Lambda=\left(\sum_{F\in\Lambda}9^{|F|}\right)^{1/2}.
\tag{1.4}
$$
对所有 $a\in\operatorname{Ran}P_\Lambda$，Cauchy--Schwarz 给
$$
\boxed{
\|X_a\|,\ \|X_{Ca}\|,\ \|X_a^{[m]}\|,\
\|X_{Ca}^{[m]}\|
\le K_\Lambda\|a\|.
}
\tag{1.5}
$$
有限头要求包含 $\Lambda$ 中所有位。
该预算取决于真实有界乘子的有限线性组合，不使用一般 $\ell^2$ 级数的未经定义乘子。

对任意正迹类 $\theta$，记
$$
\varphi_\theta(R)=\operatorname{Tr}(\theta R),\qquad
v_m(\theta)=\sum_{F\subset[0,m)}
(-1)^{|F|}\varphi_\theta(V_F^{[m]})\chi_F.
\tag{1.6}
$$
原规范头矩证明给
$$
\Phi_{v_m(\theta)}(R)
:=\langle Rv_m(\theta),\Omega\rangle
=\varphi_\theta(R)\quad(R\in\mathcal A_m),
\tag{1.7}
$$
以及
$$
\|\Phi_{v_m(\theta)}|_{\mathcal A_m}\|
=\operatorname{Tr}\theta,\qquad
\|v_m(\theta)\|\le10^{m/2}\operatorname{Tr}\theta.
\tag{1.8}
$$

## 2. 正截断与实际固定真空代表

固定 $\rho\ge0$、$\tau=\operatorname{Tr}\rho>0$。
取任意正平方分解
$$
\rho=\sum_i f_i\otimes f_i,\qquad
\sum_i\|f_i\|^2=\tau.
\tag{2.1}
$$
允许可数无穷项，且级数在迹范数中收敛。

令
$$
a_i=P_\Lambda f_i,\qquad
b_i=(I-P_\Lambda)f_i,\qquad
\sigma_\Lambda=(I-P_\Lambda)\rho(I-P_\Lambda)
=\sum_i b_i\otimes b_i.
\tag{2.2}
$$
$\sigma_\Lambda$ 是正迹类。
置
$$
\delta_\Lambda=\operatorname{Tr}\sigma_\Lambda
=\sum_i\|b_i\|^2,\qquad
A_\Lambda=\sum_i\|a_i\|^2=\tau-\delta_\Lambda.
\tag{2.3}
$$
这里 $b_i$ 可保留任意头尾纠缠，没有纯远尾张量假设。

定义
$$
h_\Lambda
=\sum_i\left[
 X_{a_i}Ca_i+X_{a_i}Cb_i+X_{Ca_i}b_i
\right].
\tag{2.4}
$$
由 (1.5)，此级数在 $H$ 中绝对收敛，并有
$$
\boxed{
\|h_\Lambda\|
\le H_\Lambda:=
K_\Lambda\left(A_\Lambda+
2\sqrt{A_\Lambda\delta_\Lambda}\right)
\le2\tau K_\Lambda.
}
\tag{2.5}
$$
最后一步使用
$2\sqrt{A_\Lambda\delta_\Lambda}\le A_\Lambda+\delta_\Lambda=\tau$。

对任意 $R\in\{A\}'$，交换性与共同 $C$ 对称性逐项给
$$
\begin{aligned}
\langle Ra_i,a_i\rangle
 &=B(RX_{a_i}Ca_i,\Omega),\\
\langle Ra_i,b_i\rangle
 &=B(RX_{a_i}Cb_i,\Omega),\\
\langle Rb_i,a_i\rangle
 &=B(RX_{Ca_i}b_i,\Omega).
\end{aligned}
\tag{2.6}
$$
例如第二式由 $a_i=X_{a_i}\Omega$、转置 $RX_{a_i}$ 和对称性直接得到。
所有转置都作用于有界实际算子。

各配对级数绝对收敛，所以
$$
\boxed{
\varphi_\rho(R)-\varphi_{\sigma_\Lambda}(R)
=B(Rh_\Lambda,\Omega)
=\Phi_{h_\Lambda}(R)
\quad(R\in\{A\}').
}
\tag{2.7}
$$
取 $R=I$ 还得
$$
\langle h_\Lambda,\Omega\rangle=A_\Lambda.
\tag{2.8}
$$
若另一向量给同一个实际泛函，取 $R=A^n$ 并用 $\Omega$ 的循环性及共同 $C$ 对称性，即知两向量相等。
所以 $h_\Lambda$ 不依赖 (2.1) 所选的正平方分解。

这是低部与交叉项的完整实际分解。
未对 $b_i$ 或 $\sigma_\Lambda$ 的自乘项给一个不存在的统一 $H$ 界。

## 3. 有限头差的准确公式与统一预算

令 $\Pi_m$ 为投影到前 $m$ 位 Walsh 柱空间，后面为真空。
固定 $m$，使 $\operatorname{Ran}P_\Lambda\subset\operatorname{Ran}\Pi_m$。
由于有限头算子只作用于前 $m$ 位，且 $a_i$ 后面全为真空，
$$
\langle R a_i,(I-\Pi_m)b_i\rangle
=\langle R(I-\Pi_m)b_i,a_i\rangle=0
\quad(R\in\mathcal A_m).
\tag{3.1}
$$
因此 (2.6) 在有限头中准确给
$$
h_{\Lambda,m}
=\sum_i\left[
X_{a_i}^{[m]}Ca_i+
X_{a_i}^{[m]}C\Pi_m b_i+
X_{Ca_i}^{[m]}\Pi_m b_i
\right]\in\operatorname{Ran}\Pi_m,
\tag{3.2}
$$
并且由规范头代表的唯一性，
$$
\boxed{
v_m(\rho)-v_m(\sigma_\Lambda)=h_{\Lambda,m},
\qquad
\|h_{\Lambda,m}\|\le H_\Lambda.
}
\tag{3.3}
$$
此处 $v_m(\sigma_\Lambda)$ 仍使用完整的正密度 $\sigma_\Lambda$。
没有把它擅自改成只由 $\Pi_m b_i$ 构成的密度；只有交叉配对允许 (3.1)。

### 3.1 固定投影后的强极限

已有准确实际头差为
$$
\|V_j-V_j^{[m]}\|\le18\prod_{s=j}^{m-1}\eta_s
\le18\eta_{m-1}
\quad(j<m).
\tag{3.4}
$$
有序望远镜给
$$
\|V_F-V_F^{[m]}\|
\le18|F|3^{|F|-1}\eta_{m-1}.
\tag{3.5}
$$
空集的差为零。
定义
$$
D_{\Lambda,m}
=6\eta_{m-1}
\left(\sum_{F\in\Lambda}|F|^2\,9^{|F|}\right)^{1/2}.
\tag{3.6}
$$
则对 $a\in\operatorname{Ran}P_\Lambda$，
$$
\|X_a-X_a^{[m]}\|,\ 
\|X_{Ca}-X_{Ca}^{[m]}\|
\le D_{\Lambda,m}\|a\|.
\tag{3.7}
$$

记正常尾质量
$$
\delta_m^{\rm head}=\operatorname{Tr}\rho(I-\Pi_m)
=\sum_i\|(I-\Pi_m)f_i\|^2\longrightarrow0.
\tag{3.8}
$$
因 $a_i\in\operatorname{Ran}\Pi_m$，
$(I-\Pi_m)b_i=(I-\Pi_m)f_i$。
将 (3.2) 与 (2.4) 相减，先比较算子，再比较输入，
得到
$$
\boxed{
\|h_{\Lambda,m}-h_\Lambda\|
\le
D_{\Lambda,m}
\left(A_\Lambda+2\sqrt{A_\Lambda\delta_\Lambda}\right)
+2K_\Lambda\sqrt{A_\Lambda\delta_m^{\rm head}}
\longrightarrow0.
}
\tag{3.9}
$$
这里 $\Lambda$ 固定。
无需给 $\delta_m^{\rm head}$ 任何速度，也没有乘上一个随 $m$ 增长的全矩常数。

## 4. 与真湮灭关系的准确接合

若实际 $S\in\mathcal A$ 在全 $H$ 单射，且
$$
\varphi_\rho(SR)=0\quad(R\in\{A\}'),
\tag{4.1}
$$
则原规范头矩定理给
$$
V_m:=\|v_m(\rho)\|\longrightarrow\infty.
\tag{4.2}
$$
从 (3.3)，对每个固定 $\Lambda$，
$$
\bigl|\|v_m(\sigma_\Lambda)\|-V_m\bigr|
\le H_\Lambda,
\qquad
\frac{\|v_m(\sigma_\Lambda)\|}{V_m}\longrightarrow1.
\tag{4.3}
$$
所以正尾虽然可以具有任意小的迹，仍承担相同的发散阶。

$\sigma_\Lambda$ 本身没有被证明湮灭 $S$。
准确的关系是
$$
\boxed{
\varphi_{\sigma_\Lambda}(SR)
=-\Phi_{h_\Lambda}(SR)
=-\Phi_{Sh_\Lambda}(R)
\quad(R\in\{A\}').
}
\tag{4.4}
$$
后续观测只使用 $\sigma_\Lambda\ge0$ 与其迹，
不把 (4.4) 的右端丢弃。

实际上，本稿以下的渐近转移只需同一固定正密度满足 $V_m\to\infty$。
真湮灭条件只用来保证 (4.2)。

### 4.1 一个明确实际源序列与固定真空近似成本

取 $P_\Lambda=\Pi_p$，简记 $h_p=h_\Lambda$、$\sigma_p=\sigma_\Lambda$。
因为 (2.7) 的残差是正密度 $\sigma_p$ 在实际代数上的限制，准确有
$$
\boxed{
\|\varphi_\rho-\Phi_{h_p}\|_{\{A\}'_*}
=\delta_p,\qquad
\|h_p\|\le2\tau10^{p/2},\qquad
\langle h_p,\Omega\rangle=\tau-\delta_p.
}
\tag{4.5}
$$
这里的范数是正常泛函在 $\{A\}'$ 单位球上的上确界。
上界 $\delta_p$ 来自正迹类范数，下界由测试 $R=I$ 达到。

在真湮灭假设 (4.1) 下，还必有
$$
\boxed{\|h_p\|\longrightarrow\infty,\qquad
h_p/\|h_p\|\rightharpoonup0.}
\tag{4.6}
$$
若有有界子列，取弱极限 $h$。
(4.5) 的正常泛函范数收敛给
$\Phi_h=\varphi_\rho$ 于全部实际 $\{A\}'$。
把 $SA^n$ 代入并用真空循环性，得到 $Sh=0$。
单射性迫 $h=0$，但常数矩趋于 $\tau>0$，矛盾。
故范数发散。
又对每个固定 $R\in\{A\}'$，
$|\Phi_{h_p}(R)|\le(\tau+\delta_p)\|R\|$，
除以发散范数后趋零；
$\{R^*\Omega:R\in\mathcal A\}$ 稠密给归一弱零。

为明确上界针对的对象，定义固定真空泛函近似成本
$$
c_{\Omega,\varphi_\rho}(\epsilon)
=\inf\left\{\|h\|:
\|\varphi_\rho-\Phi_h\|_{\{A\}'_*}\le\epsilon\right\}.
\tag{4.7}
$$
空集时取 $+\infty$。
由 (4.5)，
$$
\boxed{
c_{\Omega,\varphi_\rho}(\delta_p)
\le2\tau10^{p/2},
}
\tag{4.8}
$$
而每个 $\epsilon>0$ 都可取 $\delta_p\le\epsilon$ 得到一个实际源。
在真湮灭假设下，同一个有界弱子列论证还给
$c_{\Omega,\varphi_\rho}(\epsilon)\to\infty$ 当 $\epsilon\downarrow0$。

这是 [R244 的实际聚合与对偶成本接口](R244-appendix-aggregate-transpose-source-budget-and-exact-dual-cost.md)
中固定真空泛函近似的一条明确见证专属上界。
它的误差是原密度真实的 $\delta_p$，没有给该尾质量额外速度。
它也不是最小秩模块论证中删除一个源的 $C_i(\epsilon)$ 上界：
这里只近似整个泛函，没有重构被删除的原源向量。

## 5. 正密度专属的 little-o 转移原理

设 $\mathcal T_m:H_m\to Y_m$ 为线性观测，$Y_m$ 是赋范空间。
假设有与 $m$ 无关的常数 $C,D$ 和
$$
0<\alpha<1,\qquad \beta=1-\alpha,
$$
使
$$
\|\mathcal T_m h\|_{Y_m}\le D\|h\|,
\tag{5.1}
$$
并且对每个正迹类 $\theta$ 都有统一估计
$$
\|\mathcal T_m v_m(\theta)\|_{Y_m}
\le C(\operatorname{Tr}\theta)^\alpha
        \|v_m(\theta)\|^\beta.
\tag{5.2}
$$
观测可以随 $m$ 或当前固定 $\rho$ 选择，只要 (5.1)--(5.2) 的常数对这种选择统一。

**定理 5.1。** 若固定 $\rho\ge0$、$\tau>0$ 满足 $V_m\to\infty$，则
$$
\boxed{
\|\mathcal T_m v_m(\rho)\|_{Y_m}
=o(\tau^\alpha V_m^\beta).
}
\tag{5.3}
$$

证明先取 $\Lambda$ 为前 $p$ 位的全部 Walsh 集合，故
$P_\Lambda=\Pi_p$。
记
$$
\delta_p=\operatorname{Tr}\rho(I-\Pi_p),\qquad
H_p=10^{p/2}\left[(\tau-\delta_p)
+2\sqrt{(\tau-\delta_p)\delta_p}\right]
\le2\tau10^{p/2}.
\tag{5.4}
$$
对固定 $p$、$m\ge p$，(3.3)、(5.1)--(5.2) 给
$$
\|\mathcal T_m v_m(\rho)\|
\le C\delta_p^\alpha(V_m+H_p)^\beta+DH_p.
\tag{5.5}
$$
先除以 $\tau^\alpha V_m^\beta$，再令 $m\to\infty$，
$$
\limsup_m
\frac{\|\mathcal T_m v_m(\rho)\|}
     {\tau^\alpha V_m^\beta}
\le C(\delta_p/\tau)^\alpha.
$$
最后 $p\to\infty$，正常性给 $\delta_p\to0$，遂得 (5.3)。

### 5.1 一个已经支付全部费用的变化头选择

这里还可以给出明确的变化 $p$，不免费交换两重极限。
置
$$
x_m=V_m/\tau\ge1,\qquad
p_m=\left\lfloor\frac{\beta}{\log10}\log x_m\right\rfloor.
\tag{5.6}
$$
由 (1.8) 的 $x_m\le10^{m/2}$，
$$
0\le p_m\le\beta m/2<m
$$
对 $m>0$ 成立。
并且
$$
H_{p_m}\le2\tau x_m^{\beta/2}.
\tag{5.7}
$$
(5.5) 现给出完全量化的界
$$
\boxed{
\frac{\|\mathcal T_m v_m(\rho)\|}
     {\tau^\alpha V_m^\beta}
\le
C\left(\frac{\delta_{p_m}}{\tau}\right)^\alpha
  \left(1+2x_m^{\beta/2-1}\right)^\beta
+2D\,x_m^{-\beta/2}.
}
\tag{5.8}
$$
$x_m\to\infty$ 使 $p_m\to\infty$，所以右端趋零。
第一项只用正常尾趋零；第二项完整支付有限头交叉代表的成本。
没有要求原尾质量按幂或指数衰减。

(5.8) 不给一个对所有正密度统一的收敛速度：
$\delta_p$ 始终是当前同一原 $\rho$ 的真实尾质量。
也不能据此任意提高 $\beta$ 的改善程度。

## 6. 一次层、稀疏层与完整次数组合费用

### 6.1 一次层

已证实际估计为
$$
\|P_1v_m(\theta)\|^2
\le80(\operatorname{Tr}\theta)\|v_m(\theta)\|.
$$
取 $\alpha=\beta=1/2$、
$C=\sqrt{80}$、$D=1$，定理 5.1 给
$$
\boxed{\|P_1v_m(\rho)\|^2=o(\tau V_m).}
\tag{6.1}
$$
这是对旧 $80\tau V_m$ 上界的严格小阶加强。

### 6.2 任意变化的稀疏单项族

固定 $d\ge2$。
若 $\mathcal F_m$ 中所有集合满足 $2\le|F|\le d$，
并可分成 $h_m\ge1$ 个两两不交子族，则旧实际估计是
$$
\|P_{\mathcal F_m}v_m(\theta)\|^2
\le h_m A_d(\operatorname{Tr}\theta)
             \|v_m(\theta)\|,
\qquad
A_d=256\,9^d(d+1)^{3/2}.
$$
对线性观测 $h_m^{-1/2}P_{\mathcal F_m}$ 应用定理 5.1：
其 Hilbert 算子范数至多 $1$，常数 $C=\sqrt{A_d}$ 与族统一。
所以
$$
\boxed{
\|P_{\mathcal F_m}v_m(\rho)\|^2
=o(h_m\tau V_m).
}
\tag{6.2}
$$
允许 $h_m$、族及其位置依赖当前密度。
$d$ 在本条固定。

### 6.3 全部固定次数仍保留组合因子

对固定 $k\ge2$、$m\ge k$，令
$$
c_{m,k}=\frac{\binom mk}{\lfloor m/k\rfloor}.
$$
完整次数层已有平方界
$A_k c_{m,k}(\operatorname{Tr}\theta)\|v_m(\theta)\|$。
取观测 $c_{m,k}^{-1/2}P_k$，同样得到
$$
\boxed{\|P_kv_m(\rho)\|^2=o(c_{m,k}\tau V_m).}
\tag{6.3}
$$
没有删除 $c_{m,k}$。
由于固定 $k$ 时 $c_{m,k}=O_k(m^{k-1})$，
若固定 $d$ 且另有
$$
V_m/\tau\ge c\,m^{d-1}\quad\text{最终成立},\qquad c>0,
\tag{6.4}
$$
则 $\|P_{\le d}v_m(\rho)\|/V_m\to0$。
这将原来的严格超越 $m^{d-1}$ 条件放宽到 (6.4)，但未证明该增长条件。

反过来，如果在某子序列上
$\|P_kv_m(\rho)\|\ge\delta V_m$、$\delta>0$，
则该子序列必须满足
$$
V_m/(\tau c_{m,k})\longrightarrow0.
\tag{6.5}
$$
特别，二次层保留固定比例时必须有 $V_m=o(\tau m)$。

### 6.4 正常性的固定次数 Cesàro 界

还有一个不使用湮灭式、也不要求正性的固定次数约束。
设 $\psi$ 为任意迹类正常泛函，固定 $k\ge1$。
当不同有限集合 $F$ 在 $1\le |F|\le k$ 中离开每个有限子族时，
$$
\boxed{\psi(V_F)\longrightarrow0.}
\tag{6.6}
$$
这里是实际乘子 $V_F$，不是纯位替代。

证明如下。$V_F\Omega=\chi_F$，不同 $\chi_F$ 构成正交族，
且 $\|V_F\|\le3^k$。对每个固定多项式 $p$，
$$
V_Fp(A)\Omega=p(A)\chi_F\rightharpoonup0.
$$
$p(A)\Omega$ 稠密和统一算子范数界将其延到每个输入向量，
故 $V_F\to0$ 于 WOT。再以有限秩泛函在迹范数中逼近 $\psi$：
有限秩部分由 WOT 趋零，余项由 $3^k$ 一致控制，
得到 (6.6)。此论证也证明“只有限多个例外”的 $c_0$ 量词。

令
$$
H_m(\psi)=
\sum_{F\subseteq[0,m)}(-1)^{|F|}\psi(V_F)\chi_F.
$$
$H_m$ 的符号与本稿真实头代表 $v_m$ 相同，
但前者保完整 carry，后者使用 $V_F^{[m]}$。
由 (6.6)，任意 $\varepsilon>0$ 之外只留下有限多个系数，
所以
$$
\frac{\|P_kH_m(\psi)\|^2}{\binom mk}\longrightarrow0.
\tag{6.7}
$$
准确地，有限例外的平方和除以 $\binom mk$ 趋零，
其余平均至多 $\varepsilon^2$。

原实际头差给
$$
\|V_F-V_F^{[m]}\|
\le18k\,3^{k-1}\eta_{m-1}\qquad(|F|=k,\ F\subseteq[0,m)).
$$
因此对由同一正常泛函定义的头代表，
$$
\|P_k(v_m(\psi)-H_m(\psi))\|
\le18k\,3^{k-1}\|\psi\|_1\eta_{m-1}\sqrt{\binom mk}.
\tag{6.8}
$$
这里 $\|\psi\|_1$ 可取其给定迹类代表的迹范数。
实际 carry 已支付，故
$$
\boxed{
\|P_kv_m(\psi)\|=o\!\left(\sqrt{\binom mk}\right)
=o(m^{k/2})
\quad(k\text{ 固定}).
}
\tag{6.9}
$$
这是次数层的未归一化 Cesàro 界，
不声称该整个无限次数层平方可和。

对正 $\rho$ 还可直接用本稿的小迹尾核对：
固定 $p$，$\sigma_p=(I-\Pi_p)\rho(I-\Pi_p)$，
$\delta_p=\operatorname{Tr}\sigma_p$，由 §3，
$$
\|P_kv_m(\rho)\|
\le3^k\delta_p\sqrt{\binom mk}+2\tau\,10^{p/2}
\qquad(m\ge p).
\tag{6.10}
$$
先令 $m\to\infty$，再令 $p\to\infty$，同样得到 (6.9)。
无需假定 $\delta_p$ 的速度。

现在回到同一个非零正湮灭见证，$V_m=\|v_m(\rho)\|\to\infty$。
若固定 $k\ge2$ 的某子序列满足
$\|P_kv_m(\rho)\|\ge\delta V_m$、$\delta>0$，则必须有
$$
\boxed{V_m=o(\tau m^{k/2})}
\tag{6.11}
$$
沿该子序列成立。$k=2$ 时与 (6.5) 同阶；
$k\ge3$ 时比 $o(\tau m^{k-1})$ 更强。

如果固定 $d\ge2$ 且另有
$$
V_m/\tau\ge c\,m^{d/2}\quad\text{最终成立},\qquad c>0,
\tag{6.12}
$$
则 (6.9) 对有限多个 $1\le k\le d$ 同时适用，
而零次系数为 $\tau$，从而
$\|P_{\le d}v_m(\rho)\|/V_m\to0$。
这改进了 (6.4) 的充分增长门槛，仍未证明实际 $V_m$ 满足该门槛。

### 6.5 $c_0$ 不可免费加强为平方可和：旧正秩一例的一次层

[完整块 Gram 障碍](R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)
§§1、4 已给同一个连续严格正、非湮灭向量
$$
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
|B_i|=q_i=16^i,\quad c_i=2^{-i-2},\qquad
\|f\|^2=\lambda=\frac{49}{48},
\tag{6.13}
$$
其中 $B_i$ 互不交。这里只读取其一次层，不另构造反例。

纯位 $D_j$ 在 $\{1,\chi_j\}$ 基中是
$\left(\begin{smallmatrix}0&-1\\1&2\end{smallmatrix}\right)$。
对于 $j\in B_i$，写 $f=u+\chi_jv$，
其中 $u,v$ 为不依赖第 $j$ 位的实函数，$\|v\|^2=c_i^2$。
则两个交叉实配对抵消，故
$$
\langle D_jf,f\rangle=2c_i^2,\qquad
\sum_j|\langle D_jf,f\rangle|^2
=\sum_{i\ge1}4q_ic_i^4
=\sum_{i\ge1}\frac1{64}=\infty.
\tag{6.14}
$$
旧实际差 $\|V_j-D_j\|\le8\eta_j$ 给
$$
|\langle V_jf,f\rangle-\langle D_jf,f\rangle|
\le8\lambda\eta_j,
$$
其误差序列在 $\ell^2$ 中。
因此这个正秩一正常态的实际一次矩也不在 $\ell^2$，
同时仍满足 (6.6)。

特别，对任何非负 $a\in\ell^2$ 及 $t>0$，
$e^{-2ta_j}\ge e^{-2t\|a\|_2}>0$，
所以仅一次层就给
$$
\sum_j e^{-4ta_j}|\langle V_jf,f\rangle|^2=\infty.
\tag{6.15}
$$
这与实际热矩判据相容，也说明一般正常性本身不能提供一个有效正热权的完整平方和上界。
该 $f$ 从未被称为湮灭者；真湮灭式的额外结构仍须使用。

## 7. 完整二次矩与更高有效秩

令 $B_m(v)$ 为零对角复对称矩阵，
$(B_m(v))_{ij}=\widehat v(\{i,j\})$、$i\ne j$。
它是线性观测，且
$$
\|B_m(h)\|_{\rm op}
\le\|B_m(h)\|_{\rm HS}
=\sqrt2\|P_2h\|\le\sqrt2\|h\|.
\tag{7.1}
$$
已有实际谱范数界为
$$
\|B_m(v_m(\theta))\|_{\rm op}
\le690(\operatorname{Tr}\theta)^{1/3}
       \|v_m(\theta)\|^{2/3}.
$$
所以
$$
\boxed{
\|B_m(v_m(\rho))\|_{\rm op}
=o(\tau^{1/3}V_m^{2/3}).
}
\tag{7.2}
$$

实际全二阶矩矩阵
$M_m(h)_{ij}=\Phi_h(V_i^{[m]}V_j^{[m]})$
的对角范数至多 $9\|h\|$，故
$\|M_m(h)\|_{\rm op}\le(9+\sqrt2)\|h\|$。
用原 $699$ 界同样得到 (7.2) 的全二阶矩版本。

### 7.1 同阶有界的低秩预算现在也足够

任意秩至多 $r_m$ 的正交投影 $Q_m$ 满足
$$
\|Q_mB_m\|_{\rm HS}^2\le r_m\|B_m\|_{\rm op}^2.
$$
由 (7.2)，只要
$$
r_m=O((V_m/\tau)^{2/3}),
\tag{7.3}
$$
便有 $\|Q_mB_m\|_{\rm HS}/V_m\to0$。
投影可随 $m$ 与当前密度变化，右投影同理。
旧结论要求严格小阶秩预算；这里使用正常性允许同阶有界预算。

若二次层仍保留比例 $\|P_2v_m\|\ge\delta V_m$，
由 $\|B_m\|_{\rm HS}^2=2\|P_2v_m\|^2$ 得
$$
\boxed{
\frac{r_{\rm eff}(B_m)}
     {(V_m/\tau)^{2/3}}
\longrightarrow\infty
}
\tag{7.4}
$$
沿该子序列成立。
这不把原 $\rho$ 的有限秩替换为二次矩阵秩。

## 8. 所有固定阶无重复矩张量

令 $T_{k,m}(v)$ 是有序无重复张量：
不同的 $i_1,\ldots,i_k<m$ 上取
$\widehat v(\{i_1,\ldots,i_k\})$，碰撞指标上取零。
其注入范数与 Hilbert--Schmidt 范数满足
$$
\|T_{k,m}(h)\|_\varepsilon
\le\|T_{k,m}(h)\|_{\rm HS}
=\sqrt{k!}\,\|P_kh\|
\le\sqrt{k!}\,\|h\|.
\tag{8.1}
$$
[固定阶完整定理](R230-appendix-all-fixed-order-actual-moment-tensors-and-injective-norm.md)
给出与 $m$ 无关的明确常数 $\Lambda_k$：
$$
\|T_{k,m}(v_m(\theta))\|_\varepsilon
\le\Lambda_k(\operatorname{Tr}\theta)^{1/(k+1)}
          \|v_m(\theta)\|^{k/(k+1)}.
$$
对每个固定 $k$，定理 5.1 因而给
$$
\boxed{
\|T_{k,m}(v_m(\rho))\|_\varepsilon
=o\!\left(\tau^{1/(k+1)}V_m^{k/(k+1)}\right).
}
\tag{8.2}
$$

### 8.1 射影分解预算的端点

对任意有限张量 $Z_m$，
$$
|\langle T_{k,m}(v_m),Z_m\rangle|
\le\|T_{k,m}(v_m)\|_\varepsilon\|Z_m\|_\pi.
$$
所以现在只需
$$
\|Z_m\|_\pi=O((V_m/\tau)^{1/(k+1)})
\tag{8.3}
$$
就有配对除以 $V_m$ 趋零。
保留的是实际射影范数预算；不以一般张量秩替代。

### 8.2 正交纯张量方向的端点

如果某子空间有 $r_m$ 个正交归一的纯张量构成的基，
则投影能量至多
$r_m\|T_{k,m}(v_m)\|_\varepsilon^2$。
故条件
$$
r_m=O((V_m/\tau)^{2/(k+1)})
\tag{8.4}
$$
已足使该投影的 Hilbert--Schmidt 范数除以 $V_m$ 趋零。
仍然要求明确的正交纯张量基。
本条不包含无条件数预算的一般低形式秩展开。

所有这些 $k$ 都固定。
没有把未知增长的 $\Lambda_k$ 免费带入任意变化次数 $k_m$。

## 9. 尚未关闭的部分

真实正密度的低部与交叉项现在有准确的实际 $H$ 代表，
其余全部发散可放到迹任意小的正压缩中。
显式 (5.8) 展示了有限头与正常尾的费用怎样同时支付，
不依赖一个未证的尾速度。

这没有给小迹正尾的完整 $H$ 真空代表，也没有给其高重叠矩平方和的统一上界。
一般完整次数层仍需 (6.3) 的组合因子；
一般张量仍需 (8.3) 的真实射影分解预算。
$\sigma_\Lambda$ 满足的是带固定 $H$ 余项的 (4.4)，并非原零湮灭式。

因而本稿提高了真实正常见证必须满足的渐近约束，
但没有证明一般正常正湮灭者不存在，没有关闭普通 ISP。
