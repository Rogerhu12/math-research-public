# 原端点辅助条件与全部有限上同调测试的相容性

日期：2026-11-16。**状态：本文证明一个逐值、逐有限层的 Chebotarev 加条件引理，并将它应用于 R886 的原三个最高 CM 分量。** 它保持任意有限批上同调测试的全部原值，强于仅证明辅助素数具有正密度。本文不把尚未取得完整证明的 JNS 辅助集合扩张版本当作既有定理。

## 1. 原对象和要比较的两种辅助集合

保持 [R886](../results/R886-original-highest-cm-auxiliary-units-and-base-preserving-normalization.md) 的全部规范：
$K=\mathbf Q(\omega)$，固定原普通 ray 中的 $p>211$，原有限角色 $\eta=\eta_{10}$ 阶为十八，
$E_0:y^2=x^3+1$，$\mathbf N=\psi_0\bar\psi_0=\varepsilon_{\rm cyc}$。
三个原最高角色分别是
$$
\rho_\ell=\eta^{e_\ell}\psi_0^3\mathbf N^{-1},
\qquad(e_4,e_{10},e_{16})=(5,17,11).
\tag{1}
$$
令 $T_\ell$ 为原最高角色的一次固定整格；允许先作原来源所需的一次固定扩大，不随辅助导子改变。系数环为 $\mathcal O$，极大理想由 $\varpi$ 生成。

R886 已实际构造 $\tau\in G_K$，满足
$$
\eta(\tau)=-1,\quad\psi_0(\tau)=-\omega,\quad
\bar\psi_0(\tau)=-\omega^2,\quad
\rho_\ell(\tau)=\varepsilon_{\rm cyc}(\tau)=1.
\tag{2}
$$
因此 $\tau$ 在三个最高角色上都恒等，但在原后三个 Euler 分量上有值
$(\omega^2,\omega,\omega)$。

固定有限扩张
$$
F=H_\eta K(E_0[p]).
\tag{3}
$$
这里 $H_\eta/K$ 就是原十八阶 Artin 扩张。$p$ 分裂且 $E_0$ 的全部 CM 自同态在 $K$ 上定义，所以
$$
\operatorname{Gal}(K(E_0[p])/K)
\subset(\mathcal O_K/p\mathcal O_K)^\times
\simeq\mathbf F_p^\times\times\mathbf F_p^\times.
$$
特别
$$
[F:K]\mid18(p-1)^2,\qquad p\nmid[F:K].
\tag{4}
$$
不需要为 (4) 假设这两个原扩张线性不交。两者均在复共轭下稳定，所以 $F/\mathbf Q$ 为 Galois。

对一个固定 $\ell$ 和整数 $n\ge1$，置
$$
\Omega_n=K(\mu_{p^n})K(T_\ell/\varpi^nT_\ell),\qquad
\delta=\tau|_F.
\tag{5}
$$
本题的 p-Hilbert 类域为 $K$。若系数环的绝对分歧指数大于一，后面需要同时读取 $p^n$ 精度时可统一将表示的下标换成 $en$；这不改变论证。本文所有模 $\varpi^n$ 的读数都按 (5) 的实际下标理解。

由 (2)，$\tau|_{\Omega_n}=1$。记 $\mathcal P_n$ 为避开 $6\cdot17p$、在 $K$ 中分裂、并带一个选定素点 $\mathfrak q\mid q$ 的素数，满足
$$
\operatorname{Fr}_{\mathfrak q}|_{\Omega_n}=1,\qquad
\operatorname{Fr}_{\mathfrak q}|_F=\delta.
\tag{6}
$$
Frobenius 方向仍与 R886 一致。另一共轭方向同时共轭全部数据，不混用角色。

条件 (6) 的第二部分准确给 R886 的模 p 数据，故
$$
\mathcal P_n\subset\mathcal L_1.
\tag{7}
$$
这里不声称 $\mathcal P_n$ 等于 R886 中要求两条 CM 根都满足模 $p^n$ 同余的更小集合 $\mathcal L_n$。对原秩一系统，(7) 和第一部分的深度已经是本引理需要的条件。

## 2. 有限测试域的基本引理

**引理。** 设 $\Omega/K$ 为有限 Galois 扩张，$F/K$ 为有限 Galois 扩张且 $p\nmid[F:K]$。给定 $\delta\in\operatorname{Gal}(F/K)$，假定 $\delta$ 在 $F\cap\Omega$ 上恒等。若 $M/K$ 有限 Galois，$\Omega\subset M$，且 $\operatorname{Gal}(M/\Omega)$ 为 p 群，那么对每个
$g\in\operatorname{Gal}(M/\Omega)$，存在
$$
\widetilde g\in\operatorname{Gal}(MF/K),\qquad
\widetilde g|_M=g,\quad\widetilde g|_F=\delta.
\tag{8}
$$
这样的 $\widetilde g$ 的 Frobenius 共轭类由避开任意给定有限集的无穷多个素点实现。若 $K$ 为二次虚域且所有字段在复共轭下稳定，可令其下方有理素数在 $K$ 中分裂，并选择实现上述方向的素点。

**证明。** $F\Omega/\Omega$ 的次数素于 p，而 $M/\Omega$ 的次数为 p 幂，故
$$
M\cap F\Omega=\Omega.
\tag{9}
$$
$\delta$ 与 $\operatorname{id}_\Omega$ 在交域上相容，定义 $F\Omega/\Omega$ 的一个元。由 (9)，
$$
\operatorname{Gal}(MF/\Omega)
\simeq
\operatorname{Gal}(M/\Omega)\times
\operatorname{Gal}(F\Omega/\Omega).
\tag{10}
$$
取这两个指定分量即得 (8)。最后使用有限 Galois 扩张的 Chebotarev 定理。在对 $\mathbf Q$ 的 Galois 闭包中取限制到 $K$ 为恒等的该元，它的素数在 $K$ 中分裂；选定其上素点保持指定 Frobenius。若只先有对 $K$ 的 Galois 性，加入复共轭字段后作同样论证。证毕。

(9) 是逐值保持的关键；仅知道两个素数集合分别有正密度不能替代它。

## 3. 为什么原有限上同调数据恰好切出 p 扩张

先设 $A=T_\ell/\varpi^nT_\ell$，并取有限批
$$
z_1,\ldots,z_s\in H^1(K,A).
$$
选连续 cocycle 代表。在 $G_{\Omega_n}$ 上，$A$ 的作用平凡，每个限制都是到有限加法 p 群 $A$ 的连续同态。令 $M$ 为这些限制同态共同核的固定域。则
$$
\operatorname{Gal}(M/\Omega_n)
\hookrightarrow A^s
\tag{11}
$$
是有限 p 群。

共同核在 $G_K$ 下正规。事实上，对 $h\in G_{\Omega_n}$ 与 $g\in G_K$，
cocycle 恒等式给
$$
z_i(ghg^{-1})=\rho_\ell(g)z_i(h).
\tag{12}
$$
因此 $M/K$ 为 Galois，每个原 cocycle 也因其在该共同核上为零而通过
$\operatorname{Gal}(M/K)$ 分解。

将 §2 用于 (3)、(5)、(11)。它给出如下**全读数结论**：
对每个原来可实现的 $g\in\operatorname{Gal}(M/\Omega_n)$，
可以另选同一 $M$-Frobenius 元而额外要求其在 $F$ 上等于 $\delta$。
于是全部
$$
\bigl(z_1(g),\ldots,z_s(g)\bigr)
\tag{13}
$$
逐项不变。这里保留的是既有的可实现向量，不声称任意指定的 $A^s$ 向量都可实现。

对 $g|_{\Omega_n}=1$，改变 cocycle 代表不改变 (13)，因为 coboundary 为
$(\rho_\ell(g)-1)a=0$。在相应未分歧素点，(13) 就是用同一个 Frobenius 标识读取的有限局部类。共轭素点、对偶类、若干不同有限精度可同时加入有限批，并先统一增大 $n$；结论仍是同一个 (8)，不需逐类选互不相容的素数。

## 4. 任意已经使用的 p 环类层也完整保持

设 $B/K$ 为有限 Galois p 扩张；特别可取有限多个原 $K[m]$ 及有限 wild 层的合成。给定有限批
$$
z_i\in H^1(B,A_i),
$$
其中各 $A_i$ 是所需的原最高有限模、其共轭或对偶，选 $\Omega$ 同时平凡化所有这些有限模并含相应根单位。先在 $B\Omega$ 上限制这些 cocycle，再加入它们的全部 $K$-共轭，令 $M$ 为共同测试域。于是
$$
B\Omega\subset M,\qquad M/K\ \text{Galois},\qquad
\operatorname{Gal}(M/\Omega)\ \text{为 p 群}.
\tag{14}
$$
最后一句同时用了 $B\Omega/\Omega$ 为 p 扩张。

仍有 $M\cap F\Omega=\Omega$，故 §2 允许保留 $g$ 在整个 $M$ 上的值，同时添加
$g|_F=\delta$。这包括：

- 对已用环类层 $B$ 的 Frobenius 值，特别是要求新素数在 $B$ 中完全分裂；
- 所有原有限 cocycle 的值、线性组合及配对中用到的值；
- 若素点在 $B/K$ 的剩余次数为 $f$，用于该素点局部化的 $g^f$ 的全部值；
- 两个共轭素点的同时数据，因为对应的共轭 cocycle 已列入 (14)。

没有先把共轭素点认作同一个点，也没有删掉剩余次数。
对每一步有限 Kolyvagin 选择，可以先将此前全部已用字段和全部测试加入 (14)，然后作一次新的 Chebotarev 选择。所需字段虽可随步骤增大，素于 p 的原字段 $F$ 始终是 (3)，没有改变原 $\eta$ 或原最低层。

## 5. 原秩一表示没有遗漏的 inflation 类

上面的结论保持全部**已能检测**的读数。对本题最高表示还可证明，限制到这些测试域前不存在看不见的 inflation 类。

$K$ 上的 $\rho_\ell$ 与 cyclotomic 都是角色，所以
$\Gamma_n=\operatorname{Gal}(\Omega_n/K)$ 为阿贝尔群。R886 的十七惯性元 $\gamma=\tau_{17}$ 满足
$$
\eta(\gamma)=-1,\quad
\psi_0(\gamma)=\bar\psi_0(\gamma)=1,\quad
\rho_\ell(\gamma)=-1.
\tag{15}
$$
因 (1) 的三个指数均奇，(15) 对三个原分量同时成立。
$\gamma-1=-2$ 在 $A$ 上可逆，且 $\gamma$ 在 $\Gamma_n$ 中为中心元。
Sah 引理在这里可直接证明：对任一 cocycle $c$，比较
$c(\gamma g)=c(g\gamma)$ 得
$$
(\gamma-1)c(g)=(g-1)c(\gamma).
$$
除以 $\gamma-1$ 后 $c$ 是 coboundary。故
$$
H^1(\Gamma_n,A)=0,\qquad
H^1(K,A)\hookrightarrow H^1(\Omega_n,A).
\tag{16}
$$

对 §4 的原环类 p 扩张 $B$，$B/K$ 在十七处不分歧；十七惯性仍可给 (15)，并且 $B\Omega_n/B$ 的 Galois 群仍阿贝尔。因此同样有
$$
H^1(B,A)\hookrightarrow H^1(B\Omega_n,A).
\tag{17}
$$
也可以只用一般 restriction–corestriction：对任何素于 p 的有限扩张，
$\operatorname{cor}\circ\operatorname{res}$ 是一个在 $A$ 上可逆的整数，
所以添加 (3) 不会杀掉非零有限上同调类。对联合同态的像甚至有逐值版本：
其像是 p 群，而限制子群的指数素于 p，故限制前后联合像相同。
这些是完整有限模上的等式，不只是张量 $\mathbf Q_p$ 后的维数比较。

(15) 同时固定 $K(\mu_{p^\infty},(\mathcal O_K^\times)^{1/p^\infty})$：
前者在十七处不分歧，$\mathcal O_K^\times=\mu_6$。
因此原 ACR Remark 8.4 的 $\gamma$ 条件在此仍原样保留。

## 6. 接回真正原范数系统

[原端点全 split tame 系统](2026-11-16-original-endpoint-tame-norm-system.md)
已构造同一原 $C_{02,\ell}$、同一旧副本和 Artin 归一的有限类。
R886 §9 在 $\mathcal L_1$ 上除去三个真群环单位，给
$$
c^{\rm end}_{m,\ell}\in
\operatorname{Sel}_{\rm bal}(K[m],T'_\ell),\qquad
c^{\rm end}_{1,\ell}=z^{\rm end}_{\ell,p},
$$
以及最高角色自己的线性 Euler 范数关系。
本文没有改变这些类，尤其没有再作一项依赖辅助层的缩放。

§§2–5 证明：即使要求辅助素数满足所有原后三 Euler 单位条件，
任何原表示及其有限环类层上需要的有限上同调 Frobenius 测试，
仍可按原值同时实现。它不只保证存在某个辅助素数，也不靠新的正密度假设。

局部 balanced 条件仍是原 $\mathfrak p$ 全、$\bar{\mathfrak p}$ 零，
所有 $v\nmid p$ 的原有理局部群为零。本文的 Chebotarev 字段只是检测用字段；
没有把原全局底域改成 $F$，没有将原端点替成 R814 的 canonical 类，
也没有使用后者的 p=7993 检测。

## 7. 与已核文献陈述的精确区别

Do 的 [2022 Princeton 博士论文作者原稿](https://www.math.ucla.edu/~kdo/Tuan_PhD_Thesis.pdf)
§4.3（printed pp.83–92），尤其 §4.3.2（pp.90–92），把
$\Omega_n$ 定义成表示有限商、p 幂根单位及 p-Hilbert 类域的合成，
并要求 Euler-system 的辅助集合几乎包含一个指定的 split-$\sigma$ 集合。
其 Theorem 4.3.5 引用 JNS；本文已读取这些实际定义和定理正文，
没有取得其中所引 JNS 预稿的完整证明。
[ACR 刊本](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)
Definition 8.1、Theorem 8.3 和 Remark 8.4 的相应范围仍完整保持。

本题的区别不能靠把 $n$ 加大抹掉。秩一情形 Hyp($\sigma$) 迫使
$\rho_\ell(\sigma)=1$，又要求其固定全部 p 幂根单位，
所以 $\sigma|_{\Omega_n}=1$。
而对任意 $n$，在 $F\Omega_n$ 中完全分裂的素数具有正密度，
属于该未加条件的 split-$\sigma$ 集合。
它们的原四条角色模 p 全为一，故原后三个 Euler 因子的 augmentation 均不是单位。
因此 R886 的单位辅助集合并不直接满足上述“几乎包含”条件；
这不是漏删有限坏素数。

本文付清的是：这个真子集仍保留全部有限上同调测试，且已给逐域、逐值的证明。
若后续使用 JNS 或 split Kolyvagin 的证明，仍应明确核对其需要的素数选择
是否正由这些有限测试和有限排除组成。**本文不单凭这个可验证接口宣布
Selmer 秩一、原局部化单射或原底类非零。**

## 8. 输出和范围

本证明只使用原固定角色、原有限 tame 系统、有限 Galois 理论、
cocycle 恒等式和 Chebotarev。未执行数学程序，未扫描目标素数。

最强已经证明的输出是：对每个原 $p$、每个有限精度、
每个已用原 p 环类层及每个有限批 cohomology 测试，
R886 的三个额外 Euler 单位条件均可与全部原读数同步实现；
原 n=1 端点类和全十七角色完全不变。


## 附录 A. 原十七惯性给出的两个素点全读数

本附录加强 §§2–5：对原最高角色，不仅可以保持一组已经能出现的读数，还能明确描述有限批独立类在两个共轭素点上的联合像。全程固定原 $\ell,p,\eta,\rho_\ell$，不更换原端点。

### A.1 最小系数环与两个整投影

记
$$
\mathcal O_0=\mathbf Z_p[\mu_{18}],\qquad k_0=\mathcal O_0/p,\qquad
T_0=\mathcal O_0(\rho_\ell),\quad A_n=T_0/p^n.
\tag{A1}
$$
根单位和表示都取原指定 p-adic 嵌入。$p\equiv1\pmod6$，故 $\omega\in\mathbf Z_p$，$\mathcal O_0/\mathbf Z_p$ 不分歧，次数为一或三。两条 CM Tate 角色取值于 $\mathbf Z_p^\times$，所以 (A1) 是原表示的实际定义环。上同调类若已另扩系数，须按 A.5 处理；不能凭扩大系数使有限 Galois 像凭空成为更大的向量空间。

令 $T_0^c$ 为同一底模上角色 $\rho_\ell^c$ 的作用，系数保持固定。原共轭自对偶身份给
$$
\rho_\ell^c=\mathbf N\rho_\ell^{-1}.
\tag{A2}
$$
因此正文 $\Omega_n$ 同时平凡化 $A_n,A_n^c$。

原十七惯性的 $\eta$ 像是全部 $\mu_{18}$，两条 CM Tate 角色在那里都为一。可取一个惯性元 $a$，使 $\eta(a)=\omega$。因为三个 $e_\ell=5,17,11$ 都模三等于二，
$$
\rho_\ell(a)=\omega^2,\qquad \rho_\ell^c(a)=\omega.
\tag{A3}
$$
故在 $A_n^d\oplus(A_n^c)^e$ 上，
$$
e_+=\frac{a-\omega}{\omega^2-\omega},\qquad
e_-=\frac{a-\omega^2}{\omega-\omega^2}
\tag{A4}
$$
是两个整投影。这里分母在 $\mathbf Z_p$ 中为单位。再取十七惯性元 $b$ 使 $\eta(b)$ 为本原十八次根。三个 $e_\ell$ 都与十八互素，因而
$$
\mathbf Z_p[\rho_\ell(b)]=
\mathbf Z_p[\rho_\ell^c(b)]=\mathcal O_0.
\tag{A5}
$$
(A4) 分开两个符号，(A5) 给各自的完整系数环作用；这两步不能以“单个矩阵可逆”替代。

### A.2 联合像定理

**定理。** 取
$$
c_1,\ldots,c_d\in H^1(K,A_n),\qquad
d_1,\ldots,d_e\in H^1(K,A_n^c).
$$
假设两组各自的模 p 像分别在 $H^1(K,A_1)$ 与 $H^1(K,A_1^c)$ 中 $k_0$-线性无关。则限制到 $G_{\Omega_n}$ 后的联合同态
$$
g\longmapsto(c_1(g),\ldots,c_d(g),d_1(g),\ldots,d_e(g))
\tag{A6}
$$
的像准确为
$$
(\mathcal O_0/p^n)^d\oplus(\mathcal O_0/p^n)^e.
\tag{A7}
$$
读数使用固定的两条秩一基。若只考虑一组及其复共轭，可取 $d_i=c_i^c$，其中
$c_i^c(g)=c_i(cgc^{-1})$，外部复共轭 $c^2=1$ 不作用于系数。

**证明。** 记像为 $I$。它是有限加法 p 群，故为 $\mathbf Z_p$ 子模。正文 (12) 证明它在 $G_K$ 的表示作用下稳定。于是 (A4) 给
$$
I=I_+\oplus I_-,
$$
(A5) 再证明两个因子各为 $\mathcal O_0/p^n$ 子模。

先看 $I_+$ 的模 p 像。若它是 $k_0^d$ 的真子空间，存在一个非零 $k_0$ 线性行杀掉它。相应的原 $c_i\bmod p$ 的线性组合在 $G_{\Omega_n}$ 上为零。由于 $\operatorname{Gal}(\Omega_n/K)$ 阿贝尔，并仍含正文 (15) 的十七惯性标量 $-1$，Sah 的同一证明给
$$
H^1(\operatorname{Gal}(\Omega_n/K),A_1)=0.
$$
因此该线性组合在 $H^1(K,A_1)$ 中为零，矛盾。故 $I_+$ 模 p 满射；Nakayama 引理给 $I_+=(\mathcal O_0/p^n)^d$。负号因子同理，得 (A7)。这里用的是整个 $\Omega_n$ 上的 Sah 注入，不曾把限制到 $\Omega_1$ 的像误当成限制到 $\Omega_n$ 的像。证毕。

### A.3 在原单位辅助集合内实现矩阵

将 (A6) 的全部核及其复共轭加入正文 §3 的测试域 $M$。定理说明，在 $\operatorname{Gal}(M/\Omega_n)$ 中可以选择任意指定的 (A7) 读数。正文 §2 的纤维积则允许**保持同一个 $M$-元**，同时要求其在 $F=H_\eta K(E_0[p])$ 上为 $\delta$。

因此，在避开任意给定有限素数集后，可选无穷多个带方向的分裂 $q$，满足正文 $\mathcal P_n\subset\mathcal L_1$ 的全部条件，并实现这些指定读数。选择 $M$ 中的一个素点使其 Frobenius 为已选元，再以固定复共轭选择另一个素点，给准确的两点标识。若只记录未加这种标识的素点，读数只在共同可逆换基下确定；秩和行列式非零不受影响。

特别，对模 p 线性无关的两类 $c_1,c_2$，可令
$$
\begin{pmatrix}
\operatorname{loc}_{\mathfrak q}c_1&
\operatorname{loc}_{\mathfrak q}c_2\\
\operatorname{loc}_{\bar{\mathfrak q}}c_1&
\operatorname{loc}_{\bar{\mathfrak q}}c_2
\end{pmatrix}
=
\begin{pmatrix}1&0\\0&1\end{pmatrix}
\pmod{p^n},
\tag{A8}
$$
其中第二行按上述共轭标识读取。所有类在这些素点都未分歧，且 $\rho_\ell(\operatorname{Fr})=1\bmod p^n$，故有限局部群的标准 Frobenius 读数确为 $\mathcal O_0/p^n$。同时保有
$q\equiv1\bmod p^n$、原三个额外 Euler 群环单位、两个原 CM 符号以及原十七角色。

### A.4 已用环类层与逐步选择

上述定理也适用于原有限 Galois p 扩张 $B/K$ 上的类，条件是 $B$ 在十七处不分歧；原 tame 环类层和已用有限反循环层均满足。将 $\Omega_n$ 换成 $B\Omega_n$。十七惯性仍完整包含在 $G_B$，(A3)–(A5) 及 Sah 注入都不变。

先为 $G_B$ 上的两组类构造联合测试域，再加入全部 $K$-共轭和复共轭。得到的 $M/K$ 为 Galois，且 $M/\Omega_n$ 为 p 扩张。原联合测试域是其中的商，故任意 (A7) 读数可先在该商实现，再提升到固定 $B\Omega_n$ 的 $M$-元。正文的纤维积仍可附加 $\delta$。如此选得的 $q$ 还在整个已用 $B$ 中分裂；本段没有把一般非一剩余次数的任意读数也声称为自由变量。

每次选择只需加入此前实际用到的有限类、有限层和有限排除集，再重复上述过程。因此，所有要求在两个共轭素点检测若干独立有限类、指定一个类为零而另一个为单位、或使某个有限局部化矩阵满秩的调用，均可在原 $\mathcal L_1$ 内完成。存在依赖关系的测试必须保持其依赖关系；不能指定与它矛盾的读数。

### A.5 扩大系数时的准确版本

(A7) 是在实际最小环 $\mathcal O_0$ 上的陈述。若把系数扩大为有限扩张 $\mathcal O'$，一个有限 Galois 加法像不自动是 $\mathcal O'$ 子模，所以不无条件声称任意 $\mathcal O'/p^n$ 矩阵都能由 Frobenius 实现。

所需的秩与非零行列式结论仍有无损版本。在残余系数域 $k'$ 上取两类 $c_1,c_2$ 线性无关。Sah 注入表明它们的正号联合像的 $k'$-线性包为 $(k')^2$；同一组的负号像由复共轭给出。两个符号仍由 (A4) 独立分开。因此可分别选正号、负号像中的两条 $k'$-线性无关向量，再在同一个群元上同时实现它们。所得两点矩阵的行列式在 $k'$ 中非零，并仍能附加原 $\delta$ 条件。这足够支付两类的同时独立检测，却没有把其具体矩阵强行归为 (A8) 的单位阵。

对于有限多个更一般的测试，先按其实际定义环及真实联合像工作，再使用正文的逐值引理；不作无根据的系数饱和。

### A.6 接下来仍需证明的关系

本附录支付的是原 split 下降的**选素数接口**，没有制造 Euler 类的有限—奇异关系。原 balanced 条件在 $\mathfrak p$ 全、$\bar{\mathfrak p}$ 零，且共轭自对偶；通常 Mazur–Rubin 的 core-rank-one 定理不能因此直接调用。

这一点也可从已发表 Lei–Loeffler–Zerbes 的
[Euler systems for modular forms over imaginary quadratic fields](https://antoniolei.com/wp-content/uploads/2014/11/cmeuler.pdf)
Appendix B.2.4（印 pp.39–40）的 core-rank 公式核对：
本题秩一 $V$ 的复处贡献为一，两 p 位的局部群总维数为二，原 full/zero 条件维数为一，两处 $H^0(V^\vee(1))$ 均零，故通常 core rank 为零。
必须使用或证明真正的 split、共轭自对偶下降；上述全矩阵检测恰为这种证明提供一个现已完整付清的调用接口。
它本身不宣布原 Selmer 秩、原底类非零或普通局部化单射。
