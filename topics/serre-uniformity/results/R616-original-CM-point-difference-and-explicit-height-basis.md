# R616：原六层的实际 CM 点差、两重 Gross–Zagier 与固定高度基

日期：2026-11-14。状态：**本文的点差判据及充分非消失区域已证明；一般素数的非消失和二次高度首项仍 OPEN。**

本文只研究原曲线 \(X_1=Z_p\) 的同一个实际商。另一扭向的中心值仅作为该 CM 点 Gross–Zagier 公式的第二因子出现，不被当作 \(J_{X_1}\) 的商。所得生成元不依赖某个候选的额外坏支撑 \(D\)。

## 1. 对象、结论与两个真正不同的 Hecke 因子

令 \(p\ge41\)、\(p\equiv5\pmod6\)，
\[
K=\mathbb Q(s),\quad s=\sqrt{-3},\quad
\zeta=(-1+s)/2,\quad \operatorname{Im}s>0.
\]
取 R575 的角色
\[
\theta(\zeta)=\zeta^{-1},\qquad \theta(s)=-1,\qquad
\Psi_\theta((a))=a\epsilon_3(a)\theta(a).
\tag{616.1}
\]
令 \(\alpha=\sqrt[3]4>0\)，并按算术 Frobenius 互反规范定义
\(\kappa(\sigma)=\sigma(\alpha)/\alpha\)。记
\[
f_\theta=\operatorname{AI}(\Psi_\theta),\qquad
g_{\theta,+}=\operatorname{AI}(\Psi_\theta\kappa),\qquad
g_{\theta,-}=\operatorname{AI}(\Psi_\theta\kappa^{-1}).
\tag{616.2}
\]
两种 \(g\) 的准确水平都是 \(108p^2\)，根号分别为 \(-1,+1\)。其中 \(g_{\theta,+}\) 是 R575 已证明出现于原 \(X_1\) 的实际家族；\(g_{\theta,-}\) 是独立的相反扭向家族。

沿用 R593/R597 的同一几何：
\[
Y=W_p,\qquad j=6912v(1-v),\qquad
X_1:\ v=a^3,\qquad X_4:\ v=4u^3.
\tag{616.3}
\]
这里均表示与实际非分裂 Cartan 项链曲线取纤维积后的光滑射影规范化，不把它们当成有理参数直线。指定 \(\mu_6\)-稳定的 CM 项链在 \(X_{\rm ns}^+(p)\) 上给有理点；其 \(j\) 映射在特征零的该粗点处为一次。\(Y\) 的 \(v=0,1\) 两个指定点均有理。

在 \(X_1\) 上取
\[
c_0:\ a=0,\qquad c_1:\ a=1
\tag{616.4}
\]
及上述同一 CM 项链。二者都是 \(\mathbb Q\)-点。取与 R575 三次下降相容的实际商
\[
q_1:J_{X_1}\longrightarrow A_{\theta,1},\qquad
j_1(x)=q_1[x-c_0],\qquad
\beta_\theta=j_1(c_1)\in A_{\theta,1}(\mathbb Q)\otimes\mathbb Q.
\tag{616.5}
\]
商同态的有理同源分母可统一清除；本文非挠性、秩及高度恒等式不依赖这个非零整数尺度。

**定理 616.1。** 对每个 (616.1) 的 \(\theta\)，
\[
\boxed{\ \beta_\theta\ne0
\ \text{于 }A_{\theta,1}(\mathbb Q)\otimes\mathbb Q
\quad\Longleftrightarrow\quad
L'(g_{\theta,+},1)L(g_{\theta,-},1)\ne0.\ }
\tag{616.6}
\]
这里可在任一对应的实系数嵌入下检验右侧；若一侧成立，全部相应嵌入均成立。令 \(F=\operatorname{End}_{\mathbb Q}^0(A_{\theta,1})\) 为该形式的全实系数域。条件成立时
\[
A_{\theta,1}(\mathbb Q)\otimes\mathbb Q=F\beta_\theta,
\qquad
\operatorname{rank}A_{\theta,1}(\mathbb Q)=\dim A_{\theta,1},
\tag{616.7}
\]
且实际 \(p\)-进对数为同构。特别地，这是一条由**原曲线两个指定有理 CM 点**给出的 \(F\)-生成直线，不需要另选辅助 Heegner 域或未知的 Mordell–Weil 生成元来表示有理点。

§6 给不含候选 \(D\) 的可检验充分区域。§7 保持 R593/R596 的同一高度、同一截面与同一有限目标集合，将其二次项写成这些指定 CM 点像的高度矩阵。本文不计算该矩阵的 \(p\)-进单位性。

## 2. 真实 CM 轨道就是这个点差的三次特征分量

由 R575，规范模曲线 \(X_4\) 的甲板作用
\(\delta_\zeta:u\mapsto\zeta u\) 在 \(f_\theta\) 因子上是正 CM 算子 \([\zeta]\)。这一步采用 R575 的完整 Galois/Hodge 归一化，不能把被更正的相反方向放回本式。

同构
\[
\iota:X_1\longrightarrow X_4,\qquad u=a/\alpha
\tag{616.8}
\]
将 \(c_0\) 送到规范有理点 \(c_{0,4}\)，将 \(c_1\) 送到
\[
c:\quad v=1,\quad u=1/\alpha .
\tag{616.9}
\]
由于 \(Y\) 在该 CM 项链上 \(v-1\) 是一次参数，而 \(u\ne0\)，该三次覆盖在 \(c\) 处不分歧。三点恰由 \(4u^3=1\) 给出；故在 \(K\) 上的定义域准确为 \(K(\alpha)\)，轨道大小为三。对 \(\sigma\in G_K\)，
\[
\sigma c=\delta_{\kappa(\sigma)^{-1}}c .
\tag{616.10}
\]

令 \(q_4:J_{X_4}\to A_{\theta,4}\) 是与 \(q_1\) 相容的未扭曲商。三次下降在同源范畴给
\[
P=q_4[c-c_{0,4}]
   =\iota_A(\beta_\theta),\qquad
\sigma P=[\kappa(\sigma)^{-1}]P .
\tag{616.11}
\]
此处 \(\iota_A\) 是相应阿贝尔簇的扭曲同构；也可先选该实际扭曲模型再作任意非零有理同源。由于 \(\alpha\) 为实数，\(P\) 定义在 \(\mathbb Q(\alpha)\)，故复共轭固定 \(P\)。

在 \(E=FK\) 上把 \([\zeta]\) 分成两个 CM 特征。由 (616.11)，\(\kappa\)-加权的算术 Galois 平均选出 \(P\) 的正 CM 分量，\(\kappa^{-1}\)-平均选出其共轭分量。两个分量由复共轭交换，所以其中一个为零当且仅当 \(P\) 为零。

为精确比较 Gross–Zagier 中的基点，令 \(o\) 为有理次数一 Hodge 除子，\(f_o(x)=q_4[x-o]\)。\(c_{0,4}\) 为有理点，而非平凡三次角色的和为零，故
\[
\sum_{\sigma\in\operatorname{Gal}(K(\alpha)/K)}
 \kappa(\sigma) f_o(c^\sigma)
=
\sum_\sigma\kappa(\sigma)\sigma P .
\tag{616.12}
\]
因此这里**没有**删掉一个未知的非有理基点常数。Shimura 互反律将真实 CM toric 轨道识别为 (616.10)；toric 积分只是 (616.12) 乘以一个非零 Haar 体积。若所引用文献以相反 Artin 规范记 reciprocity，同时将 toric 角色取逆；两特征分量和下节两因子交换，(616.6) 不变。

规范水平含全部有限整中心，有理中心已取商，因此 \(\pi_\theta\) 的中央角色平凡。又 \(\kappa^c=\kappa^{-1}\)，且 \(\kappa^3=1\)，从而 \(\kappa\) 在 \(\mathbb A_{\mathbb Q}^{\times}\) 上平凡：不分裂处由共轭固定性得 \(\kappa^2=1\)，分裂处两分量互逆。这核准了 Gross–Zagier 的中央相容条件。

## 3. 基变换因子及勘误后的 epsilon 规范

规范未扭曲表示满足
\[
(\pi_\theta)_K=\Psi_\theta\boxplus\Psi_\theta^c.
\]
由于 \(\kappa^c=\kappa^{-1}\)，对算术中心 \(s=1\) 有准确的有限 Euler 乘积恒等式
\[
\begin{aligned}
L((\pi_\theta)_K\otimes\kappa,s)
&=L(\Psi_\theta\kappa,s)L(\Psi_\theta^c\kappa,s)\\
&=L(g_{\theta,+},s)L(g_{\theta,-},s).
\end{aligned}
\tag{616.13}
\]
第二等号对第二理想和作复共轭；它不改变 \(\theta\) 的指定轨道。因为第一因子根号负，
\[
L'((\pi_\theta)_K\otimes\kappa,1)
=L'(g_{\theta,+},1)L(g_{\theta,-},1).
\tag{616.14}
\]
式中没有 type \(3,5,7\) 的辅助高权角色。

必须区分两个局部 epsilon 规范。记 \(\epsilon_{\rm BC,v}\) 为 \(K_v\) 上二维 base-change 表示的根号，\(\epsilon_{\rm RS,v}\) 为在 \(\mathbb Q_v\) 上诱导后的四维 Rankin–Selberg 根号，则
\[
\epsilon_{\rm RS,v}=\eta_v(-1)\epsilon_{\rm BC,v},
\qquad \eta=\chi_{K/\mathbb Q}.
\tag{616.15}
\]
这是二维诱导的 Langlands 常数的平方。Yuan–Zhang–Zhang 2026 勘误 PDF pp.1–2，第 2、5 条及跨页脚注，明确指出两规范相差 \(\eta_v(-1)\)，并将其 base-change 规范下的正确判据写为
\[
\epsilon_{\rm BC,v}
=\chi_v(-1)\epsilon(B_v).
\tag{616.16}
\]
不能把 CST §2.3 旧印式中的额外 \(\eta_v(-1)\) 与 base-change 根号混用。

R575 与 R348 保留的独立局部计算给：

| 位置 | \(\epsilon_v(g_+)\) | \(\epsilon_v(g_-)\) | \(\eta_v(-1)\) | \(\epsilon_{\rm BC,v}\) |
|---|---:|---:|---:|---:|
| \(2\) | \(-1\) | \(-1\) | \(+1\) | \(+1\) |
| \(3\) | \(-1\) | \(+1\) | \(-1\) | \(+1\) |
| \(p\) | \(+1\) | \(+1\) | \(+1\) | \(+1\) |
| 其他有限处 | \(+1\) | \(+1\) | \(+1\) | \(+1\) |
| \(\infty\) | \(-1\) | \(-1\) | \(-1\) | \(-1\) |

表中两条 \(\mathbb Q\)-形式根号的乘积是 \(\epsilon_{\rm RS}\)，最后一列才是除以 \(\eta(-1)\) 后的 \(\epsilon_{\rm BC}\)。又 \(\kappa_v(-1)=1\)。故相关 incoherent 四元数代数在全部有限处为 \(M_2(\mathbb Q_v)\)，在无穷处为 Hamilton 代数，正是规范模曲线的 Gross–Zagier 情形。权二在无穷的 Jacquet–Langlands 向量及平凡有限阶无穷角色给非零的标准无穷局部因子；不把 holomorphic 离散系列中的一个平凡环面函数积分冒作这一因子。

## 4. 同一 CM 标记的实际局部向量非零

本节检验实际商 \(q_4\) 的向量，而不是只验证存在某个可选择的 test vector。

### 4.1 六水平的两个二维型

由 R348/R575 的保留有限型及 R588 §5，\(\pi_{\theta,2}^{K(2)}\) 是
\[
\mathbf1\oplus\operatorname{Std}_2
\]
的三维置换型；\(\pi_{\theta,3}^{K(3)}\) 是二维 cuspidal 型
\[
\operatorname{Std}_3=\operatorname{Std}_2\circ\vartheta,
\qquad
\vartheta:\operatorname{GL}_2(\mathbb F_3)\twoheadrightarrow S_3
\tag{616.17}
\]
的膨胀，核为 \(Q_8\)。这里 \(\pi_{\theta,3}\) 是导子二的 depth-zero supercuspidal。其原 CM 局部角色在 \(-1\) 取 \(-1\)、在 \(s\) 取 \(-i\)，与共轭角色不同；有限型中央角色平凡，故确为 (616.17) 的唯一二维 cuspidal 型。

实际 \(H_6\) 是 \(\vartheta\) 的图式。因此
\[
\bigl((\mathbf1\oplus\operatorname{Std}_2)
       \otimes\operatorname{Std}_3\bigr)^{H_6}
=
(\operatorname{Std}_2\otimes\operatorname{Std}_3)^{H_6}
\tag{616.18}
\]
为一维，其非零向量是一项非退化不变配对。实际 \(q_4\) 所对应的 tame 向量就在这条线，故相差的只是非零标量。

在 (616.9) 的点，\(X_4\to j\) 在特征零粗模上不分歧；所以椭圆曲线的 \(\mu_3\) 稳定子保留在实际 \(H_6\) 中。在由同一 CM 格 \(\mathcal O_K\) 及完整六水平标记给出的嵌入下，两个 CM 单位 \(C_3\) 因而由 \(\vartheta\) 对齐。用其特征基表示 (616.18) 的非零向量，必为
\[
w=a\,e_\zeta\otimes f_{\zeta^{-1}}
  +b\,e_{\zeta^{-1}}\otimes f_\zeta,\qquad ab\ne0.
\tag{616.19}
\]
若任一系数为零，该不变配对会退化；图式内的反射也直接交换两个分量。

这项对齐针对 \(c\) 的实际标记。它不是在原曲线上交换 \(c_0,c_1\) 的假想自同构；两点在 \(j\) 上的分歧行为不同。

### 4.2 角色与 3 处另一赋值陪集

\(\kappa\) 的 \(K\)-导子是 \((2)(s)^2=(6)\)。3 处的**角色导子指数为二**；相应二维诱导表示的 \(\mathbb Q_3\)-Artin 导子指数三不是本处指数。

R575 的局部互反计算给
\[
\kappa_3(1+s)=\zeta,\qquad
\kappa_3(s)=1,\qquad
\kappa_3(\zeta)=\zeta^{-1}.
\tag{616.20}
\]
最后一式由 \(\zeta\equiv1-s\pmod{s^2}\) 得到。全局单位 \(\zeta\) 的互反像为一，且其他有限处在单位上平凡，故
\[
\kappa_2(\zeta)=\zeta .
\tag{616.21}
\]
在 2 处，单位环面商是 \(\mathbb F_4^\times=C_3\)；在 3 处，相关单位商也是 \(C_3\)。因此 \(\kappa\) 及 \(\kappa^{-1}\) 的联合投影恰选出 (616.19) 的两个非零分量之一。

3 处使用实际 depth-zero compact-induction 模型
\(\mathrm{c}\text{-}\mathrm{Ind}_{ZK}^{\mathrm{GL}_2(\mathbb Q_3)}\widetilde{\operatorname{Std}}_3\)。
完整 \(K(3)\)-固定型由支持在 \(ZK\) 的向量实现；R588 §5.1 的有限右平移是 \(d(3)\)，它把 newvector 送到此型中。矩阵 \(\iota(s)\) 及其整个单位陪集的 determinant 赋值为奇数，\(ZK\) 的 determinant 赋值均为偶数。故该陪集上的矩阵系数严格为零。

余下单位陪集的联合积分是一个正体积乘以 (616.19) 所选分量的平方范数，因而严格正。这里必须同时处理 2、3 两处：实际 \(H_6\)-不变向量一般不是二者的纯张量。没有把它先当作纯张量再凭局部存在性相乘。

附带的有限型证书只验证一个等价模型：取
\[
C=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\quad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
G=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
不变张量矩阵 \(W=3G^{-1}=\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\)
有范数平方 18，两种相反 \(C_3\) 特征联合投影各有范数平方 9。它仅验证 (616.19) 的有限维恒等式，不进行任何 \(p\)-网格或 \(L\) 值扫描。

### 4.3 其余有限处

在 \(p\)，\(4\) 在 \(\mathbb Q_p\) 中为立方，所以 \(\kappa_p=1\)。CM 项链的实际环面是非分裂 Cartan，\(q_4\) 的 \(N_{\rm ns}\)-固定线特别为此环面固定。R434/R588 给该线非零；因此环面积分为正体积乘向量范数。条件 \(\theta(s)=-1\) 是该实际正规化子线的条件，未另换 \(\theta\)。

在 \(q\nmid6p\)，表示、角色及 CM 格嵌入均未分歧，采用实际球向量；标准未分歧 toric 积分等于非零局部 \(L\) 因子乘非零归一化因子。在非分裂处也可直接用紧环面固定性。所有相关中心局部 Euler 因子无零、无极点。

## 5. 对实际向量应用两重 Gross–Zagier

主来源为 Cai–Shu–Tian，*Explicit Gross–Zagier and Waldspurger formulae*，§2.3 的一般公式 **(2.4)** 及其前全部中央、局部与测度条件：

<https://arxiv.org/pdf/1408.1733>

并同时采用 Yuan–Zhang–Zhang 勘误：

<https://faculty.bicmr.pku.edu.cn/~yxy/preprints/erratum-GZSC.pdf>

这里不套用额外要求互素或 split-Heegner 的简介特例；\(3\) 的分歧及 \(p\) 的惰性均在 §§3–4 的实际局部检验中处理。也不使用三重积／Chow–Heegner 因子化或省略它的分歧修正项。

将 (2.4) 乘回全局配对后，其两边都是向量与对偶向量的双线性式。在包含于 \(H_6\) 的乘积小水平上，将 (616.18) 的向量写成有限个纯张量之和，再按双线性逐项应用。因此公式适用于真正的非纯张量 tame 向量；2、3 两处的合并局部式正是 §4.2 已证明非零的联合积分。

对正极化及相应对偶参数化，选择共轭配对，toric 点的自配对是正定 Néron–Tate 高度的相应 CM 分量。§4 的全部有限因子和标准无穷因子非零，故 (616.12)–(616.14) 给
\[
\text{该 CM 特征分量的高度}
=C_\theta L'(g_{\theta,+},1)L(g_{\theta,-},1),
\qquad C_\theta\ne0 .
\tag{616.22}
\]
本篇只使用非零性，不给未经计算的 \(C_\theta\) 数值、\(p\)-进赋值或单位断言。

正定性及 §2 的两个共轭分量说明左侧为零当且仅当 \(\beta_\theta\) 为挠，证明 (616.6)。若乘积非零，则 \(L'(g_{\theta,+},1)\ne0\)。已发布的任意水平 Heegner 秩接口对实际 \(A_{\theta,1}\) 给 rank = dimension 及对数同构。因为其 \(F\)-秩为一，任一非挠 \(\beta_\theta\) 都生成整个 \(F\)-直线，证明 (616.7)。

同一 \(F\)-直线的每个实分量都有严格正的极化高度。对这些分量应用同一公式即得 (616.6) 的逐嵌入陈述；没有对超越的 \(L'\) 值臆造直接 Galois 作用。

## 6. 不含候选 D 的本原有效区域

本节再假设 \(p\equiv2,5\pmod9\)，并取指定本原角色 \(\theta_{-1}\)。令
\[
N=p+1=3M,\quad (M,3)=1,\quad
R=\operatorname{rad}(M),\quad J=2^{\omega(M)}-2,\quad
H=(p/2)^{2/R},\quad t=\frac{c}{p},\quad c=\frac{\pi}{3\sqrt3}.
\tag{616.23}
\]
这些条件覆盖当前主问题剩余的素数类；这里的 \(d=1\) 指原曲线，不是令第二覆盖的候选参数为一。

### 6.1 原两家族中的共同可见射线估计

R608/R614 的 ring-class 变换最初是针对实际第二覆盖的 \(\kappa_d^{-1}\) 推导的。这里须保留一个额外相位，不能直接抹掉 \(\kappa_p\)。

设 \(m=1\) 若 \(p\equiv5\pmod9\)，\(m=2\) 若 \(p\equiv2\pmod9\)。令
\(\eta_p=\kappa_p\)，\(\nu=\theta\eta_p^{-m}\)。由 \(mM\equiv2\pmod3\)，\(\theta\) 的全部集合对应 ring-class 群 \(C/\mu_3\) 的全部奇角色；本原 \(\theta\) 对应全部本原 \(\nu\)。

对唯一 primary 生成元 \(a\equiv1\pmod3\)，定义
\[
\lambda_{p,\pm}((a))=a\,\kappa((a))^{\pm1}\kappa_p((a))^m.
\tag{616.24}
\]
于是原两家族的 Hecke 角色**准确等于**
\[
\Psi_\theta\kappa^{\pm1}=\lambda_{p,\pm}\nu .
\tag{616.25}
\]
该附加相位依赖 \(p\)，但在平均中固定，取值在 \(K\)，绝对值为一；它在有理标量上平凡。因此可见射线的唯一拆分
\(a=\chi_{-3}(n)n\beta\) 仍给
\(\lambda_{p,\pm}(a)=\chi_{-3}(n)n\lambda_{p,\pm}(\beta)\)。
R614 的带符号倍数和、可见格点计数和 Ramanujan 权重遂逐项适用，且不改任何常数。

具体地，令 \(\mathcal O=\{o\mid R:o>2\}\)，
\[
H_o=\begin{cases}(\sqrt3p/2)^{1/o},&o\ \text{奇},\\
(p/2)^{2/o},&o\ \text{偶},\end{cases}
\qquad S=(1+1/2)(1+1/p)<2.
\]
记原 \(g_+\) 的全族／本原导数均值为 \(A_+^{\rm full},A_+^{\rm prim}\)，原 \(g_-\) 的对应中心值均值为 \(A_-^{\rm full},A_-^{\rm prim}\)。则
\[
|A_+^{\rm prim}-A_+^{\rm full}|
\le24S\sum_{o\in\mathcal O}
\left[\frac{E_1(tH_o^2)}{H_o}+3\sqrt{3\sqrt3/p}\right]=E_+,
\tag{616.26}
\]
\[
|A_-^{\rm prim}-A_-^{\rm full}|
\le24S\sum_{o\in\mathcal O}
\left[\frac{e^{-tH_o^2}}{H_o}+3\sqrt{3\sqrt3/p}\right]=E_-.
\tag{616.27}
\]
两核分别来自精确的负号导数 AFE 和正号中心值 AFE；未交换它们。

R600 对原实际 \(g_+\) 给 \(A_+^{\rm full}>28/5\)，并保留更强的逐 \(p\) 主项界
\[
A_+^{\rm full}>
3c\left[\log(p/c)-29/50-\frac23\log2\right]-1/250.
\tag{616.28}
\]
R348 §7 经 R575 明确保留的独立相反族结论是
\[
A_-^{\rm full}>\frac{5393}{6150}.
\tag{616.29}
\]
故 (616.26)–(616.29) 本身就是一个不含候选 \(D\) 的可计算充分判据：两次本原均值的下界均为正，则 (616.6) 对指定 \(\theta_{-1}\) 成立。

这一步需要同一轨道的非消失，而非只有两个不相交的非零角色。全部本原 \(\theta\) 在两个固定扭向内各成一个有理 Galois 轨道；固定 \(K\) 的圆分自同构同时保留 \(\kappa^{\pm1}\)。共同任意水平秩接口把一个嵌入的非零导数／中心值传到各嵌入的非零 Heegner 高度乘积，所以两次正均值分别给所有本原嵌入非零。因而二者确实在指定 \(\theta_{-1}\) 相交。

### 6.2 一个简明 radical 区域

若 \(J=0\)，即 \(p+1=3\cdot2^\nu\)，则所有角色已经本原，(616.29) 与 R600 的 \(28/5\) 立即给 (616.6)–(616.7)。这里只陈述参数形状，不声称此类素数无穷。

若 \(J>0\)，以下两个显式条件充分：
\[
\boxed{\quad H\ge480J,\qquad \sqrt p\ge1440J.\quad}
\tag{616.30}
\]
等价地，\(p\ge2(480J)^{R/2}\) 且 \(p\ge(1440J)^2\)。

证明仍保留两个核的不同常数。记 \(B=\log p-1\)。条件给 \(B>2\)，
\(H_o\ge H\ge1\)，且
\[
E_1(tH_o^2)<\log p+2<\frac52B,\qquad
\sqrt{3\sqrt3}<5/2 .
\]
故
\[
E_+<\frac{120JB}{H}+\frac{360J}{\sqrt p}
\le B/4+1/4<B/2,
\qquad
E_-<\frac{48J}{H}+\frac{360J}{\sqrt p}
\le\frac7{20}.
\tag{616.31}
\]
因为 \(3/5<c<61/100\)、\(\log2<7/10\) 以及
\(\log(1/c)>1/10\)，(616.28) 大于
\((9/5)B-1/250\)。其中最后一个对数界可由
\(e^{1/10}<10/9<100/61\) 直接核准。因此
\[
A_+^{\rm prim}>\frac{13}{10}B-\frac1{250}>\frac{649}{250}>0,
\qquad
A_-^{\rm prim}>\frac{5393}{6150}-\frac7{20}
=\frac{6481}{12300}>0.
\tag{616.32}
\]
这证明指定实际 \(\beta_{-1}\) 的非挠性及生成元结论。

例如 R614 已有完整 Lucas \(N+1\) 素性证书的
\[
p=15\cdot2^{73}-1=141670994486089356410879
\]
满足 (616.30)：\(R=10,J=2\)，而 R614 已核的更强界含额外 \(\mathcal L>1\)。本篇不为此重跑任何 \(L\) 值或长系数计算。

### 6.3 另一个不要求小 radical 的形状

若 \(p+1=6\ell\)，\(\ell>3\) 为素数，则非本原比例为 \(1/\ell\)。R600 已给原 \(g_+\) 在 \(p\ge101\) 的本原非消失。对原 \(g_-\)，中心值 AFE 与 R598 的理想计数证明给
\[
|L(g_{\theta,-},1)|
\le2\sqrt{3\sqrt3\,p}<5\sqrt p.
\tag{616.33}
\]
因而 \(p\ge1225\) 时
\[
\frac{5\sqrt p}{\ell}
=\frac{30\sqrt p}{p+1}
<\frac{30}{\sqrt p}\le\frac67
<\frac{5393}{6150}.
\tag{616.34}
\]
删去至多一个非本原角色仍留下正的本原中心值总和。故该形状且 \(p\ge1225\) 也满足 (616.6)–(616.7)。这不是对该参数形状素数无限性的断言。

## 7. 同一高度的固定 CM 矩阵，不更换 splitting

现在固定一个满足定理的实际因子，记 \(A=A_{\theta,1}\)、\(\beta=\beta_\theta\)、\(g=[F:\mathbb Q]\)。保持 R593/R596 已选的实际极化、全局 idèle 角色、\(p\) 处 splitting、刚性化、清分母截面及所有 \(p\) 外项。

选 \(F\) 的一组有理基 \(e_1,\dots,e_g\)，可由该模因子的有理 Hecke 对应给出，并令
\[
\beta_i=e_i\beta,\qquad \ell_i=\log_p\beta_i .
\tag{616.35}
\]
在同源范畴清分母以后，\(\beta_i\) 是**明确两个 CM 点差的 Hecke 像**，不是未知的 Mordell–Weil 生成元。由 (616.7)，\(\ell_i\) 是实际 Lie 空间的一组 \(\mathbb Q_p\)-基。对同一 Abel 映射 \(j_1\)，定义坐标函数 \(u_i(x)\)：
\[
\log_pj_1(x)=\sum_i u_i(x)\ell_i.
\tag{616.36}
\]
若 \(x\in X_1(\mathbb Q)\)，则 \(j_1(x)\in F\beta\)，故这些坐标准确属于 \(\mathbb Q\)，且
\[
j_1(x)=\sum_i u_i(x)\beta_i
\quad\text{于 }A(\mathbb Q)\otimes\mathbb Q.
\tag{616.37}
\]

令 \(b_h\) 是 R593 中实际对称线丛 \(\mathcal L_h\) 的同一全局高度二次型极化后的双线性配对，令 \(H_h\) 为固定矩阵
\[
(H_h)_{ij}=b_h(\beta_i,\beta_j).
\tag{616.38}
\]
于是有理点的实际二次高度项准确为
\[
Q_h(\log_pj_1(x))=u(x)^{\mathsf t}H_hu(x).
\tag{616.39}
\]
这一矩阵式对原 splitting 直接成立，不假定它与 \(F\) 相容，不以更换高度来偷换原有限目标集合。

因而 R596 的同一原曲线高度关系变为
\[
\rho_h(x)=u(x)^{\mathsf t}H_hu(x)
 +2\ell_h\!\left(\log_p\phi_{1,*}[x-c_0]\right)
 -\lambda_{p,h,1}(x)
\in\Omega_h
\quad(x\in X_1(\mathbb Q)).
\tag{616.40}
\]
所有 \(H_h\) 的输入点、对数基、基点和局部截面现在均固定在原曲线上，不随候选 \(d,D\) 改变。\(\eta_h\) 的线性项仍按 R596 处理；本文没有把它删去。

若另选一个 \(F\)-相容的高度，(616.38) 可进一步用一个迹型参数表示，但那需要同时运输所有局部项。为保持原规范，本文不作该改变。

## 8. 边界、来源与执行范围

本文的新结论是 (616.6) 的**同一点差**公式、其 D-independent 本原充分区域，以及 (616.35)–(616.40) 的固定 CM 高度基。它没有：

- 证明所有惰性 \(p\) 的两个因子同时非零；
- 证明 \(\log\beta\)、\(H_h\)、实际局部高度首项或调节子为 \(p\)-单位；
- 将一个原始 Abel 积分的首项当成整个二次高度函数的首项；
- 把 \(X_1/c_1\) 的结果直接搬到不同的 \(X_d/c_0\) 商，或排除尚未验证的全部候选。

主来源与既有输入：

- R575：实际正 CM 甲板、三次下降、两个扭向及实际负根号。
- R593/R596/R597：同一有理 CM 基点、真实 Abel 映射、固定高度与运输边界。
- R434/R588 §5：实际有限 \(p\) 型及 2、3 处表示。深度零 compact induction 的主来源是 File–Martin–Pitale，*Test vectors and central L-values for GL(2)*，§5B4：<https://msp.org/ant/2017/11-2/ant-v11-n2-p01-p.pdf>。
- Cai–Shu–Tian §2.3 (2.4) 与 YZZ 2026 勘误 pp.1–2，准确使用范围见 §§3、5。
- R348 §7 仅保留相反族的独立解析均值；R600/R608/R614 及共同任意水平 rank 接口提供各自已经说明的解析、轨道与秩前置。

执行只包含一个二维有限群张量的精确恒等式证书与常数有理比较；没有新本地长计算、未执行 CI 任务或数值猜测。程序为 `scripts/R616_tame_pairing_certificate.py`，本次实际产物为 `notes/R616-tame-pairing-certificate.json`；来源与发布字节分别见 `notes/R616-agent-CM-point-manifest.json` 和 `notes/R616-handoff-manifest.json`。
