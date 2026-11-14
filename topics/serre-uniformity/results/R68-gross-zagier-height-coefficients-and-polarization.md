# R68. Gross–Zagier 高度系数的实际 Hecke 同源传输

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明。** 本文给出经典 Heegner 点的两种 $\ell$ 进 Gross–Zagier 公式与 R47 实际高度坐标之间的准确接口。主要内容有三项。

1. 对实际解析秩一因子，所选经典 Heegner 投影一旦非挠，R47 已证明的对数定理使它的**每个系数嵌入对数均非零**。因此 BDP 分母的非消失无需另加 $\ell$ 进高度非退化猜想。
2. 从 $J_0(p^2)$ 传到 $J_{\rm ns}^+(p)$ 时，高度的倍率是实际 Rosati 复合的因子 $\kappa_f$，微分坐标还有切映射标量 $a_f$。一般倍率是 $\kappa_f/a_f^2$，不能把一个不存在的曲线映射的次数填进公式。
3. R47 的 Mordell–Weil 坐标系数 $c_f$ 与微分对数坐标系数 $\gamma_f$ 不同。选经典 Heegner 投影作 Mordell–Weil 基时，$c_f$ 直接由圆分导数给出；使用微分坐标时，才出现圆分导数与 BDP 值的比。

下面关于 GZ 数值的陈述保留其明示适用条件。本文不证明所选的类数一虚二次域对每一因子的中心扭曲值均非零，不计算规范平移 $\xi$ 或辅助局部高度，也不声称得到 CM 根的简单性。来源中已有的 GZ 定理仅作已发表输入；新的传输、分母非零和坐标辨认在本文完整证明。

## 1. 实际对象与统一的高度约定

固定层素数 $p>37$，记
$$
J_0=J_0(p^2),\qquad J=J_{\rm ns}^+(p),\qquad
T_A=\prod_{f\in\mathcal F_A}E_f.
\tag{1.1}
$$
$\mathcal F_A$ 是 R45 中满足 $L'(f,1)\ne0$ 的实际 $p^2$-new、Fricke $+$ Galois 轨道。每个 $E_f$ 的次数等于对应简单因子的维数，且该因子的有理 Mordell–Weil 模是秩一 $E_f$-模。这里沿用 R45 的实际商，在同源范畴与 $e_AJ\subset J$ 识别。

在 $J_0$ 和 $J$ 上使用同一圆分字符、同一相容普通 splitting 的 Coleman–Gross／Mazur–Tate 全局高度，写作 $h_0,h_J$。对 R47 的符号，使用其 (3.1)–(3.2) 的 Poincaré 高度；R43 (1.3) 已将它与相同次数零除子的 Coleman–Gross 配对识别。R43 的 Nekovář 局部项负号来自第二个除子 $D_Z=-E$，不能在本文再给全局自高度额外加负号。

高度对同态及对偶的函子性为
$$
h_J(qP,Q)=h_0(P,q^\dagger Q),
\tag{1.2}
$$
其中 $q^\dagger$ 是由两端相应极化定义的 Rosati 伴随。若同时将两端自对偶识别取相反号，$q^\dagger$ 不变；若改变全局字符，高度与本文圆分 $L$ 导数同时变号。

在普通辅助素数 $\ell\ne p$ 处，单位根 splitting 与同源相容。这是下面用 (1.2) 将 GZ 高度搬到实际 $J$ 的 splitting；R49 已证明最终真实 QC 方程不依赖换用哪一个 Hecke 相容 splitting。

## 2. Rosati 倍率与微分倍率必须分开

由 Chen–Edixhoven 同源选一个定义于 $\mathbb Q$ 的 Hecke 相容映射
$$
q:J_0\longrightarrow J
\tag{2.1}
$$
在同源范畴中满足：它消去不属于 $\mathcal F_A$ 的部分，并将相应 $J_0$ 子因子同源地映到 $e_AJ$。允许先使用有理同态，再乘整数成为真正同态。任取这种实际 $q$，不预先假定其极化倍率为 $1$。

令 $e_0\in\operatorname{End}_{\mathbb Q}^0(J_0)$ 是相应因子的幂等元。Hecke 相容性和简单因子的重数一给
$$
q^\dagger q=\kappa e_0,\qquad
q q^\dagger=\kappa e_A,
\qquad \kappa=(\kappa_f)_f\in T_A^\times,
\tag{2.2}
$$
两处的 $T_A$ 经 $q$ 的 Hecke 识别相同。每个 $\kappa_f$ 为 Rosati 对称的非零元素；使用正极化时它在实嵌入下为正。

**证明 (2.2)。** $q^\dagger q$ 与 Hecke 作用交换，消去 $1-e_0$ 部分，并在每个 $\mathbb Q$-单、重数一因子上属于其交换的 $\mathbb Q$-自同态域 $E_f$。它在该因子上为同源，故非零。恒等式
$$q(q^\dagger q)=(q q^\dagger)q$$
及 $q$ 在保留因子上的可逆性给两个元素相同。正性为 Rosati 伴随的正性，后续公式只需要非零性。证毕。

以下将标量扩张到一个使有关 $E_f$ 分裂的有限扩张 $L/\mathbb Q_\ell$；这是**系数扩张**，不是假设 $\ell$ 在各 $E_f$ 中完全分裂。记 $\sigma:E_f\hookrightarrow L$。在源因子取标准特征微分
$$\omega_{0,f,\sigma}=f^\sigma(z)\,dz\cdot 2\pi i=f^\sigma\,dq_{\rm exp}/q_{\rm exp},$$
其中 $q_{\rm exp}$ 是尖点展开变量，和同态 $q$ 不同。目标上取非零特征微分 $\omega_{J,f,\sigma}$，定义其真实切映射标量
$$
q^*\omega_{J,f,\sigma}=a_{f,\sigma}\omega_{0,f,\sigma},
\qquad a_{f,\sigma}\ne0.
\tag{2.3}
$$
这些微分和标量可以选为相容的共轭族。也可直接定义 $\omega_{J,f,\sigma}$ 为 $q^*$ 下 $\omega_{0,f,\sigma}$ 的原像，此时 $a_{f,\sigma}=1$；这只是明确选择了坐标。

### 命题 1：一般传输公式

若源和目标的高度在这些微分对数坐标中分别为
$$
h_0(P,Q)=\sum_{f,\sigma}\gamma_{0,f,\sigma}
\log_{\omega_{0,f,\sigma}}P\,
\log_{\omega_{0,f,\sigma}}Q,
$$
以及相同形式的 $\gamma_{J,f,\sigma}$，则
$$
\boxed{\quad
\gamma_{J,f,\sigma}
=\frac{\sigma(\kappa_f)}{a_{f,\sigma}^{2}}
\gamma_{0,f,\sigma}.
\quad}
\tag{2.4}
$$
相反，若使用 Mordell–Weil 基 $P_{J,f}=qP_{0,f}$，R47 的迹系数满足
$$
\boxed{\quad c_{J,f}=\kappa_fc_{0,f}.\quad}
\tag{2.5}
$$
**证明。** 由 (1.2) 和 (2.2)，
$$h_J(qP,qQ)=h_0(P,\kappa Q).$$
逐 $\sigma$ 分量，右侧高度系数乘 $\sigma(\kappa_f)$。对数的函子性与 (2.3) 给
$$\log_{\omega_{J,f,\sigma}}qP
=a_{f,\sigma}\log_{\omega_{0,f,\sigma}}P.$$
所以两个对数共贡献 $a_{f,\sigma}^2$，得到 (2.4)。Mordell–Weil 坐标 $xP_{0,f}\mapsto xqP_{0,f}$ 的 $x$ 本身未变化，故此时只乘 $\kappa_f$，得到 (2.5)。两种结论不冲突。证毕。

### 极化倍率是有限、明确的数据

设 $M$ 是 $q^*:H^1_{\rm dR}(J)\to H^1_{\rm dR}(J_0)$ 的矩阵，$C_J,C_0$ 是极化诱导交替配对的矩阵。其伴随矩阵为
$$N=C_J^{-1}M^{\mathsf T}C_0.$$
于是 $NM$ 是 $(q q^\dagger)^*$ 的矩阵；限制到实际 $A$ 后，读取其 Hecke 特征值即可得到 $\kappa_f$。这也给出在已知同源矩阵时核算 (2.2) 的纯有限线性代数方法。

如果 $q=\varphi_*$ 来自实际曲线映射 $\varphi:X_0(p^2)\to Y$，则 $\varphi_*\varphi^*=[\deg\varphi]$，才可以把 $\kappa$ 写成 $\deg\varphi$。本课题没有以 Chen 同源推出这样一个曲线映射。

## 3. 核对过的两条 GZ 输入及其范围

先在 Hashimoto (2023) §3–4 所陈述的计算条件下使用两条公式：

- $f\in\mathcal F_A$，故 $L'(f,1)\ne0$；
- $K=\mathbb Q(\sqrt D)$ 类数一，$D<-3$ 为奇基本判别式，$p$ 在 $K$ 中分裂；
- $\ell>2$、$\ell\ne p$，在 $K$ 中分裂；有关 $f^\sigma$ 在辅助处普通；
- 选定的 $K$ 满足 $L(f\otimes\epsilon_K,1)\ne0$。

Hashimoto 为将所有值写在 $\mathbb Q_\ell$ 中，还采用 $\ell$ 在 $E_f$ 中完全分裂的便利假设。**本节按该已核对的表述使用其圆分公式。** 命题 1、下一节的对数非零论证、以及 §5 的内在迹表达不需要这个便利假设。若在不完全分裂的 $\ell$ 处直接计算圆分 $L$ 函数，必须使用对应的系数扩张版本并保持下列规范化；不能只把代码的 $\mathbb Q_\ell$ 输入类型改掉就当作完成。BDP 原文 Theorem 5.13 已在一般系数嵌入下陈述，并没有系数字段完全分裂条件。

在选定的 $K$ 上，令
$$y_K=[P_K-\infty]\in J_0(K),\qquad y_f=e_{0,f}y_K.$$
经典 Heegner 共轭公式与 Fricke $+$ 性给
$$y_f\in J_0(\mathbb Q)\otimes\mathbb Q$$
（尖点挠类在张量 $\mathbb Q$ 后消失）。$L(f\otimes\epsilon_K,1)\ne0$ 与 $L'(f,1)\ne0$ 由经典 Gross–Zagier 保证 $y_f\ne0$。不同 $f$ 可以选不同的 $K$；无需为了简化记号强加一个共同的类数一域。

记
$$
u_{f,\sigma}=\log_{\omega_{0,f,\sigma}}y_f,
\quad E_{f,\sigma}=\frac{1-\sigma(a_\ell(f))+\ell}{\ell},
\quad U_{f,\sigma}=1-\alpha_{f,\sigma}^{-1},
\tag{3.1}
$$
其中 $\alpha_{f,\sigma}$ 为 $X^2-\sigma(a_\ell(f))X+\ell$ 的普通单位根。以 Hashimoto 的精确规范化写
$$B_{f,\sigma}=L_{\ell,\rm anti}(f^\sigma/K,1),\qquad
C_{f,\sigma}=L'_{\ell,\rm cyc}(f^\sigma/K,1).$$
其 (3.0.1) 和 Theorem 4.2 给
$$
\boxed{\quad B_{f,\sigma}=E_{f,\sigma}^2u_{f,\sigma}^2,\quad}
\tag{3.2}
$$
$$
\boxed{\quad
C_{f,\sigma}=U_{f,\sigma}^4
h_{0,K}(y_{f,\sigma},y_{f,\sigma}).
\quad}
\tag{3.3}
$$
这里 $y_{f,\sigma}$ 表示标量扩张后的单一特征投影。所用 $K$ 上高度是未除以 $[K:\mathbb Q]$ 的规范；对来自有理点的配对，
$$h_{0,K}=2h_{0,\mathbb Q}.$$
因而 (3.3) 转到有理全局高度时，必须出现 $1/2$。这是 Hashimoto Corollary 4.5 的相同因子。

没有要求 $C_{f,\sigma}\ne0$。普通性给单位根的存在，不意味着 $U_{f,\sigma}$ 是整数单位。它与 $E_{f,\sigma}$ 都非零：若任一个为零，就有 $\sigma(a_\ell(f))=\ell+1$；这与权二新形式的每个复嵌入上的 Weil 界 $|a_\ell|\le2\sqrt\ell<\ell+1$ 矛盾。

## 4. BDP 分母非零在实际商上是定理

### 命题 2：每个 Heegner 对数分量非零

在 §3 的经典 Heegner 条件和 $L(f\otimes\epsilon_K,1)\ne0$ 下，对**每个**辅助素数 $\ell$ 和每个系数嵌入 $\sigma$，
$$u_{f,\sigma}\ne0.$$
于是当 BDP 公式适用时，
$$\boxed{B_{f,\sigma}\ne0.}\tag{4.1}$$
这不需要假设圆分 $\ell$ 进高度非退化，也不需要已知 $C_{f,\sigma}\ne0$。

**证明。** $f$ 的源简单因子在 $\mathbb Q$ 上单，维数 $[E_f:\mathbb Q]$，且 $y_f$ 为非零有理 Mordell–Weil 向量。取正整数清除幂等元及下降分母，得到该简单因子上的非挠有理点。R47 命题 2 的解析子群论证说明：这个点的对数在每个 $E_f\otimes\mathbb Q_\ell$ 域分量均非零；进一步扩标量到各 $\sigma$ 后，其一维特征分量仍非零。$\omega_{0,f,\sigma}$ 是该分量上的非零线性泛函，故其值 $u_{f,\sigma}$ 非零。除回所乘整数不改变非零性。

这条论证本身未使用普通性或完全分裂性；二者只属于所调用 GZ 公式的具体适用范围。最后由 (3.2) 和 $E_{f,\sigma}\ne0$ 得 (4.1)。证毕。

**逻辑方向。** 这里的非零输入是选定 $K$ 的**复**中心扭曲值，以及已知 $L'(f,1)\ne0$。它们先给一个非挠有理 Heegner 投影，再给所有对数分量非零。没有从非挠性推出其 $\ell$ 进自高度非零。若 $C_{f,\sigma}=0$，下面的相应高度系数可以为零而没有矛盾。

## 5. R47 两种坐标中的准确系数

取
$$P_f^0=q y_f\in e_fJ(\mathbb Q)\otimes\mathbb Q.$$
选整数 $m_f>0$，使 $P_f=m_fP_f^0$ 是实际非挠有理点。它是 R47 可用的 Mordell–Weil 基。

### 定理 3：Heegner 基中的 $c_f$

以 $P_f$ 为 R47 的基，则其迹系数满足
$$
\boxed{\quad
\sigma(c_f)=\frac{m_f^2\sigma(\kappa_f)}2
C_{f,\sigma}U_{f,\sigma}^{-4}.
\quad}\tag{5.1}
$$
因此在这种基下，计算 $c_f$ 不需要另除 BDP 值。但是计算局部函数的 $z_f(x)$ 仍须知道该基的对数。

若使用目标特征微分的对数
$$\mathcal L_{f,\sigma}(P)=\log_{\omega_{J,f,\sigma}}P,$$
则相同全局高度的微分坐标系数为
$$
\boxed{\quad
\gamma_{f,\sigma}
=\frac{\sigma(\kappa_f)}{2a_{f,\sigma}^{2}}
\frac{C_{f,\sigma}U_{f,\sigma}^{-4}}
{B_{f,\sigma}E_{f,\sigma}^{-2}}.
\quad}\tag{5.2}
$$
分母由命题 2 非零；式 (5.2) 不依赖于清分母整数 $m_f$。

**证明。** 不同特征分量在高度下正交。由 (3.3) 和 $K/\mathbb Q$ 的二次扩张规范，源 Heegner 基 $y_f$ 的高度迹系数在 $\sigma$ 处为
$$\tfrac12C_{f,\sigma}U_{f,\sigma}^{-4}.$$
命题 1 搬到 $q y_f$ 时乘 $\sigma(\kappa_f)$；换成 $P_f=m_f qy_f$ 时自高度再乘 $m_f^2$，证明 (5.1)。

另一方面，
$$\mathcal L_{f,\sigma}(P_f)
=m_fa_{f,\sigma}u_{f,\sigma}.$$
从 Mordell–Weil 坐标换成微分对数坐标，需要将 (5.1) 除以该值的平方。利用 (3.2) 得 (5.2)。最后，秩一 $E_f$-模中的所有点都是该基的 $E_f$ 倍数，Hecke 平衡性把在基上验证的等式推广到整个高度配对。R47 的对数同构再将它唯一延拓为局部 Lie 空间上的双线性表达式。证毕。

这些特征值来自原来的 $\mathbb Q_\ell$-双线性高度，故作为相容元组下降为 $E_f\otimes\mathbb Q_\ell$ 中的元素；正确的内在公式是迹，而非只取一个任意系数嵌入。完全分裂仅使这条迹写成 $\mathbb Q_\ell$ 中的坐标和。

若换另一个满足条件的 Heegner 域，所得非挠基与原基相差 $t_f\in E_f^\times$。高度系数乘 $t_f^2$，基对数平方也乘 $t_f^2$，所以 (5.2) 不变。这提供不同 Heegner 域之间的精确一致性检验，不意味着任取一个类数一域必满足所需非零条件。

## 6. 规范平移和 CM 根导数还需要什么

记 R47 的实际平移为 $\eta_{D,2F}$，全部尖点除子次数
$$d=(p-1)/2,\qquad u_D(x)=[dx-D].$$
用上述 Heegner 基，仍须计算
$$
\xi_{2F,f}
=\frac{\log(e_f\eta_{D,2F})}{\log(P_f)}\in E_f.
\tag{6.1}
$$
自高度的 $L$ 值公式并不识别 $\eta_{D,2F}$ 在这条秩一 $E_f$-模中的倍数。已知 $c_f$ 不等于已知 $\xi_{2F,f}$，也不等于已知完整混合高度。

固定一个局部参数 $t$，把 $z_f,\xi,c_f,F$ 扩标量后记为各 $\sigma$ 分量。R54 真实函数的导数恰为
$$
\boxed{\quad
\frac{d\mathcal Q_F}{dt}(x)
=\sum_{f,\sigma}\sigma(c_f)\,z'_{f,\sigma}(x)
\bigl(4\sigma(F_f)z_{f,\sigma}(x)-\sigma(\xi_{2F,f})\bigr)
-\frac{d}{dt}\lambda_\ell(\widetilde s_{2F}(x)).
\quad}\tag{6.2}
$$
这是对完整函数求导，不是只对 Hecke 二次微分求导。$z_f$ 已含 $u_D$，所以在 (6.2) 外面不得再乘 $d^2$；若将其微分展开到 $X$ 上，$du_D=d\,di_b$ 只在 $z'_f$ 中贡献一次 $d$。

公式 (5.1) 或 (5.2) 给出了 (6.2) 的实际全局系数输入，但并未给出最后一个局部导数，也未排除它与全局项相消。即使一个 $C_{f,\sigma}$ 已算得非零，仍不能据此声称某个实际方向在 CM 点导数非零。反过来，所有 $c_f$ 中某些为零也不迫使真实 QC 函数恒定，因为其局部项仍有 R49 证明的独立性。

## 7. $p=41$ 的实际输入范围

DLF §5.3 的已发表非消失计算给 $p=41$ 的实际 $A=J$，维数 $54$。LMFDB 的 newspace $1681.2.a$ 明列 Fricke $+$ 因子
$$
1681.2.a.\{a,b,d,e,f,h,i,k\},
$$
维数依次为
$$2,3,3,4,4,8,12,18.$$
这条数据库分解用于定位有限计算输入；R68 的定理不依赖把数据库的数值秩当作证明。

对于奇判别式、类数一的候选，$K=\mathbb Q(\sqrt{-43})$ 和 $\mathbb Q(\sqrt{-163})$ 都满足 $41$ 分裂，因而满足经典水平 $41^2$ 的局部 Heegner 条件。它们是否对某个指定 $f$ 给非零 $L(f\otimes\epsilon_K,1)$，必须另行核验；本文不把分裂条件当作该中心值非零的证明。

R64 为坏靶集提供的 $K=\mathbb Q(\sqrt{-3})$ 的 CM 曲线点则在 $41$ 惰性。其用途是非分裂 Cartan 曲线上的实际 CM 点，不能直接代入本节要求 $41$ 分裂的经典 $X_0(41^2)$ Heegner 公式。这两类 CM 输入可以服务于同一个 $A_f$，但其之间的传输由 (2.1)–(2.3) 及实际点坐标决定。

因此，$p=41$ 的数值实施需要：选定的 Hecke 同源及其 $\kappa_f,a_{f,\sigma}$；逐因子有效 Heegner 域与相应两个规范化 $L$ 值；实际平移的坐标；实际辅助局部高度及其精度界。R68 消掉的是独立的“BDP 分母或对数是否非零”假设，并固定高度系数的准确尺度，不把这些尚未计算的有限数据视作已经获得。

## 8. 已核对的原始来源

- S. Hashimoto, **Quadratic Chabauty and $p$-adic Gross–Zagier**, *Transactions of the AMS* **376** (2023), 3725–3760，DOI [10.1090/tran/8862](https://doi.org/10.1090/tran/8862)；[作者版 v3](https://arxiv.org/abs/2206.08595v3)。本文核对的页码是作者版：§2.2 pp.4–5（Heegner 投影及有理性），Assumptions 3.1、公式 (3.0.1) p.7，Assumptions 4.1 p.16，Theorem 4.2、Proposition 4.3 p.17，Corollary 4.5 p.18，Theorem 5.10 pp.28–29。其曲线商公式中的 $\deg\varphi$ 在本文由完整证明替换为实际 $\kappa_f/a_f^2$。
- M. Bertolini, H. Darmon and K. Prasanna, **Generalized Heegner cycles and $p$-adic Rankin L-series**, *Duke Mathematical Journal* **162** (2013), 1033–1148；[作者全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/51.BDP1/paper.pdf)。所核 68 页作者版 §5.3、Assumption 5.12 与 Theorem 5.13 在 pp.62–63；允许一般系数嵌入，权二、类数一情形给本文 (3.2)。
- B. Perrin-Riou, **Points de Heegner et dérivées de fonctions $L$ $p$-adiques**, *Inventiones Mathematicae* **89** (1987), 455–510，DOI [10.1007/BF01388982](https://doi.org/10.1007/BF01388982)。本文使用的准确圆分规范化是 Hashimoto Theorem 4.2 对其 Theorem 1.3 的已发表重述；未从只能读到摘要的网页补写额外适用范围。
- [R47](R47-heegner-logarithms-global-height.md) §§1–3：每个实际因子的所有特征对数非零、对数同构、Hecke 平衡高度的迹系数；§5：$u_D$ 和规范平移坐标。
- [R43](R43-neron-height-from-integral-correction.md) §§1、4：[实际 Poincaré 范数、Coleman–Gross 配对以及 Nekovář 对应除子负号]；[R49](R49-independent-qc-functions-and-saturated-degree.md) 命题 2A：完整真实函数的 splitting 变化相消；[R54](R54-hecke-spectral-defect-and-finite-target.md) (2.3)：本文 (6.2) 所微分的真实函数。
- LMFDB：[newspace $1681.2.a$](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/1681/2/a/)，访问 2026-11-12；其 Fricke 分解和轨道维数仅用作 §7 的计算定位。
