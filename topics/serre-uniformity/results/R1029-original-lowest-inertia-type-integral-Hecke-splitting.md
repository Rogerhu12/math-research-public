# R1029：原最低惯性型的整 Hecke 分裂与首对数保留

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
global_route / root，finite-group 部分另经 o2_high_coefficient 核对。

**已证明：原 \(p\equiv11\bmod12\) 行有一个真正整的 \(p\)-进
Hecke 幂等元 \(e_1\)，在原良好 Jacobian 的 \(p\)-可除群上分裂出
最低惯性型，保留 R1023 的全部第 \(m\) 层对数。**
它的特殊 Hodge 空间纯为权 \(m\)；该块内部的同角色整提升模
\(p\) 唯一。R1026 的原负 deck 对数在此块中仍准确为第 \(m\)
层本原。

这里的对象是实际 \(p\)-可除群的整类型块。
本文不把它称作一个已经选好的 \(\mathbf Q\)-简单阿贝尔商，
也不把其整格自动认作 R1011 任意商模型的 Néron 格。
指定 CM jet 的非齐次系数仍须计算。

## 1. 同一个原曲线、底环和整 Hecke 代数

全篇设
\[
p=12g-1>37,\qquad m=(p-1)/2,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad
\varepsilon=\pi_0^m.
\tag{1029.1}
\]
使用 R1014/R1018 的原 \(X_1\)、\(J=J_1\)、
良好模型 \(\mathcal J/R\) 和
\[
P=(p-1)D_0,\qquad D_0=(3-N)[c_1-c_0],\qquad
N=1+\delta+\delta^2.
\]
\(R\) 在必要的非分歧扩张后含全部标记，
\(\sigma(\pi_0)=\xi\pi_0\)，\(\xi\) 阶为 \(e_0\)。

只取满足 \(\ell\nmid6p,\ \ell\equiv1\bmod3\) 的原 Hecke 对应：
\[
\mathbb T^s=\mathbf Z[\,1,T_\ell:
                  \ell\nmid6p,\ \ell\equiv1\bmod3\,]
       \subset\operatorname{End}_{\mathbf Q}(J),\qquad
\mathbb T_p^s=\mathbb T^s\otimes\mathbf Z_p .
\tag{1029.2}
\]
原关系 \(T_\ell\delta=\delta^\ell T_\ell\) 使这些对应与
\(\delta\) 交换，因而沿原 \(\kappa_4\) 三次扭曲下降到
\(\mathbf Q\)。不在此处把惯性素数的单个 \(T_\ell\) 也当成
已下降的对应。
\(\mathbb T^s\) 是有限无挠 \(\mathbf Z\)-代数：
它是有限秩 \(\operatorname{End}_{\mathbf Q}(J)\) 的子模，
且其特征零作用由真实 Hecke 本征分解对角化。

canonical \(X_4\) 与 \(X_1\) 在 \(\mathbf Q_p\) 上同构：
\(p\equiv2\bmod3\) 使模 \(p\) 立方为双射，单位根由 Hensel
唯一提升，所以原 \(\sqrt[3]4\) 已在 \(\mathbf Q_p\)。
因此下面从 canonical spectrum 读取的 \(p\)-处惯性型，
就是原 \(J\) 的类型；没有另换一个局部 twist。

约定 \(\widetilde\omega\)、\(\widetilde\omega_2\) 为一阶、二阶
fundamental characters 的 Teichmüller 提升；
其模 \(p\) 约化写为 \(\omega,\psi\)，满足
\(\omega=\psi^{p+1}\)。目标型为
\[
\boxed{\quad
\tau_1=\widetilde\omega_2^{p-1}
             \oplus\widetilde\omega_2^{-(p-1)}.
\quad}
\tag{1029.3}
\]
在原 \(\pi_0\) 惯性记号中，它的两个角色是 \(\xi^m,\xi^{-m}\)。

## 2. 原正规化子保留的完整局部类型

原 canonical 水平含中心，故中央角色平凡；它含
\(K_p(1)=1+pM_2(\mathbf Z_p)\)。
Miyauchi–Yamauchi 的 Theorems 1.1–1.2（取 \(n=2\)、主同余
层一）给完整限制：主系列两字符各至多导子一，特殊表示的
扭字符至多导子一，超尖点的导子至多二。
超尖点 Weil 表示不可约、惯性不变量为零，故导子
\(2+\operatorname{Swan}\le2\)，确实是 tame depth zero。
因此没有漏掉 wild 或更深类型。

令 \(G=\operatorname{GL}_2(\mathbf F_p)\)，
\(C=\mathbf F_{p^2}^{\times}\)，\(N_{\rm ns}=C\rtimes\langle w\rangle\)，
其中 \(w\) 是 Frobenius。
以下有限型及其真实 \(N_{\rm ns}\)-固定向量给出全部情形。

### 2.1 主系列与尖点型的原奇偶性

主系列为
\(\operatorname{Ind}_B^G(\chi,\chi^{-1})\)，
\(\chi=\widetilde\omega^a\)、\(\chi^2\ne1\)。
其 \(C\)-固定空间是一维。
对 \(zw\in Cw\)，特征多项式是
\(T^2-\operatorname N(z)\)。
范数为平方时的 split 特征值为 \(t,-t\)，主系列 character 为
\(2\chi(-1)\)；范数为非平方时 character 为零。
两类各占一半，所以 \(w\) 在固定线上作用为 \(\chi(-1)\)。
因此
\[
\dim\pi_a^{N_{\rm ns}}=1
             \quad\Longleftrightarrow\quad a\ {\rm even}.
\tag{1029.4}
\]

尖点型由
\[
\theta_r=\widetilde\omega_2^{r(p-1)},\qquad
\theta_r|_{\mathbf F_p^\times}=1,\qquad \theta_r^2\ne1
\]
参数化，且 \(\theta_r,\theta_r^{-1}\) 给同一表示。
其 \(C\)-固定空间也为一维。
在 \(Cw\) 的 split 半部 character 为零；
nonsplit 半部的两个特征值为 \(t,-t\)、\(t^p=-t\)。
\(t\) 在 \(C/\mathbf F_p^\times\) 中是二阶元素，故 character 为
\(-2\theta_r(t)=-2(-1)^r\)。
平均后 \(w\) 在固定线上作用为 \(-(-1)^r\)。
所以
\[
\dim\pi_r^{N_{\rm ns}}=1
             \quad\Longleftrightarrow\quad r\ {\rm odd}.
\tag{1029.5}
\]
这里没有用一个只知道 Cartan 固定向量的结论代替正规化子条件。

两种 \(C\)-固定维数亦可直接核：
主系列在非中心 \(C\) 上 character 为零，中心上为 \(p+1\)；
尖点型在中心为 \(p-1\)，其它 \(t\in C\) 为
\(-\theta_r(t)-\theta_r(t)^p\)。
利用非平凡 \(\theta_r\) 的完整 character sum 为零，分别得到一。

### 2.2 所有退化与旧类型

Steinberg 表示是 \(\mathbf P^1(\mathbf F_p)\) 置换表示减去常数；
\(C\) 传递作用，故它没有 \(C\)-固定向量。
二次 twist \(\operatorname{St}\otimes\epsilon\det\) 的
\(C\)-固定空间一维，在 \(Cw\) 上的平均为
\(\epsilon(-1)=-1\)，因为 \(p\equiv3\bmod4\)，
所以它也没有 \(N_{\rm ns}\)-固定向量。

有限一维二次 determinant character 亦无
\(N_{\rm ns}\)-固定向量，因为
\(\det N_{\rm ns}=\mathbf F_p^\times\)。
具有相同 tame 字符的二次主系列在 \(K_p(1)\)-固定部中分解为
这两个二次类型，故亦被排除。
tame 字符都平凡的 unramified 主系列只有其球面线保留；
它若出现在这里，会产生去掉 \(p\) 水平后的
\[
S_2(H_6)=H^0(X'(6),\Omega^1)
        =H^0(\mathbf P^1,\Omega^1)=0,
\tag{1029.6}
\]
矛盾。这里保留原 tame \(H_6\)，不是替换成 level one。
真正一维的 \(\operatorname{GL}_2(\mathbf Q_p)\) 表示不出现在
尖点自守谱中；有限一维类型已按上述主系列退化情形处理。

综上，原谱只可能有
\[
\begin{array}{c|c|c}
 &\text{Weil 惯性型}&\text{参数范围}\\ \hline
{\rm cusp}&
\tau_r=\widetilde\omega_2^{r(p-1)}
              \oplus\widetilde\omega_2^{-r(p-1)}
 &1\le r\le(p-1)/2,\quad r\ {\rm odd}\\
{\rm PS}&
\tau_a=\widetilde\omega^a\oplus\widetilde\omega^{-a}
 &1\le a<(p-1)/2,\quad a\ {\rm even}.
\end{array}
\tag{1029.7}
\]
有限型与 tame Weil 参数的对应保留实际字符；depth-zero
超尖点的 unramified rectifier 不改变这里的惯性。
Mercuri–Schoof Proposition 2.1 也给出 (1029.4)–(1029.5)
及二次 Steinberg 的同一完整判据。

## 3. 模 \(p\) 惯性半单化：逐项排除全部相邻类型

权二 Galois 成分具有 Hodge–Tate 权 \(\{0,1\}\)。
原 \(J\) 在 \(R\) 上良好，故它们 potentially crystalline。
在 \(p\) 处，Saito 的 local–global compatibility 将
(1029.7) 识别为这些实际 \(p\)-进表示的 Weil 惯性型。
本段使用这个 \(p=\ell\) 比较，不能仅引用
\(p\ne\ell\) 的 Carayol 比较。

置 \(q=p-1\)。将 (1029.7) 代入 Savitt 的 corrected
Theorems 6.11–6.12／Corollary 6.15，剩余惯性半单化只能为
\[
\begin{array}{c|l}
\tau_r&
 O_r=\{\omega^r,\omega^{1-r}\},\
 A_r=\{\psi^{p+rq},\psi^{1-rq}\},\
 B_r=\{\psi^{1+rq},\psi^{p-rq}\}\\
\tau_a&
 \{\omega^{a+1},\omega^{-a}\},\
 \{\omega^{1-a},\omega^a\},\
 A_a .
\end{array}
\tag{1029.8}
\]
公式只记 unordered semisimplification，不删除可能的
non-split extensions。
Savitt Remark 6.17 明确说明这个半单化列表不要求剩余
endomorphism ring 为标量；其额外限制涉及完整整格扩张的分类。

为核准尖点代入的 indices，写
\[
r(p-1)=i+(p+1)j,\qquad
i=p+1-2r,\quad j=r-1.
\]
原范围中 \(2\le i\le p-1\)，尤其没有被 corrected 文本另行处理的
\(i=1,p\) 遗漏。
主系列取 \(i=a,j=-a\)，其
\(\{j-i\}=p-1-2a\)，即得 (1029.8)。

目标 \(\tau_1\) 的列表是
\[
O_1=\{1,\omega\},\quad
A_1=\{\psi^{2p-1},\psi^{2-p}\},\quad
B_1=\{\psi^p,\psi\}.
\tag{1029.9}
\]
全部 \(A_r,B_r,A_a\) 的指数模 \(p+1\) 是奇数，
而 \(p+1\) 为偶数，所以它们都是 genuine niveau two，
不会与 niveau-one 的 \(O_1\) 混同。

在 \(1\le r\le(p-1)/2\) 内，比较 unordered 指数给
\[
\begin{array}{c|c}
\text{等式}&\text{唯一可能参数}\\ \hline
O_r=O_1&r=1\\
A_r=A_1&r=1\\
B_r=A_1&r=2\\
B_r=B_1&r=1\\
A_r=B_1&\text{无}.
\end{array}
\tag{1029.10}
\]
这只是模 \(q\) 或模 \(q(p+1)\) 的整数等式。
例如 \(B_r\) 的第一指数等于 \(A_1\) 的第一指数要求
\(q(r-2)\equiv0\bmod q(p+1)\)，故 \(r=2\)；
交换配对给 \(r\equiv-1\bmod p+1\)，不在范围内。
其它各行同样约掉 \(q\) 即得。
唯一额外参数 \(r=2\) 已被 (1029.5) 排除。

对主系列的原代表范围，任一 ordinary pair 等于 \(O_1\)
只可能 \(a=1\)，或退化参数 \(a=0\)；
\(A_a=A_1\) 只可能 \(a=1\)，而 \(A_a=B_1\) 无解。
\(a=1\) 被 (1029.4) 排除，\(a=0\) 已由 (1029.6)
及 Steinberg 检查处理。
由此准确得到：
\[
\boxed{\quad
\text{原谱的 }\tau_1\text{ 成分与任一非 }\tau_1\text{ 成分，}
\ \overline\rho|_{I_p}^{\,ss}\text{ 不同。}
\quad}
\tag{1029.11}
\]

## 4. 从实际 split Hecke 谱得到整幂等元

先说明 \(\tau_1\) 子集确实对 \(\mathbb T_p^s[1/p]\) 的谱定义良好。
若两个 canonical 成分在所有 \(\ell\equiv1\bmod3\) 的
\(T_\ell\) 特征值相同，这些素数在
\(K=\mathbf Q(\sqrt{-3})\) 分裂。
Chebotarev 与 Brauer–Nesbitt 在 \(G_K\) 上比较其二维表示，
给出同构的半单化限制。
分裂的 degree-one 素点足以作该比较；degree-two 素点不需要补
额外的 Hecke 值。
\(p\) 在 \(K\) 未分歧，故 \(I_p\subset G_K\)，两者的惯性型相同。
允许 \(\pi,\pi\otimes\chi_{-3}\) 被合并：这个二次 twist
在 \(p\) 未分歧，仍不改变 \(\tau_1\)。

此外，\(\tau_1\) 的 traces 属于 \(\mathbf Q_p\)：
对 Teichmüller \((p+1)\)-次根 \(z\)，
unramified Frobenius 送 \(z\) 到 \(z^p=z^{-1}\)，
故 \(z+z^{-1}\in\mathbf Q_p\)。
所以 \(\tau_1\) 的特征零谱子集对
\(\operatorname{Gal}(\overline{\mathbf Q}_p/\mathbf Q_p)\) 稳定，
给一个有理幂等元
\(e_1^0\in\mathbb T_p^s[1/p]\)。

现在付清其整性。若 \(\mathbb T_p^s\) 的某一 maximal ideal
同时位于一个 \(\tau_1\) generic prime 和一个其它类型 generic
prime 之上，取共同有限系数扩张及剩余嵌入后，
全部实际 split \(T_\ell\) 特征值模该位相同。
再次以 Chebotarev／Brauer–Nesbitt，在 \(G_K\) 上得到两个
剩余表示半单化同构，故它们在 \(I_p\) 上的半单化相同。
这与 (1029.11) 矛盾。
比较时两表示的 determinant 都是同一模 \(p\) cyclotomic
character；没有缺一个 determinant 条件。

有限 \(\mathbf Z_p\)-代数 \(\mathbb T_p^s\) 已完备，
按 maximal ideals 分解为有限乘积。
每个乘积因子的所有 generic primes 由上段同属
\(\tau_1\) 或同属其补。
在前者取一、后者取零，得到
\[
\boxed{\quad
e_1\in\mathbb T_p^s,\quad e_1^2=e_1,\quad
e_1[1/p]=e_1^0.
\quad}
\tag{1029.12}
\]
这一步没有将某个含 \(p\) 分母的特征零投影直接用在整格上。

## 5. 实际 \(p\)-可除群分裂与底 Hodge 空间

原 \(T_\ell\) 都是实际整对应，延伸为良好
\(\mathcal J/R\) 的自同态。
(1029.12) 在每个 \(\mathcal J[p^n]\) 上由
\(\mathbb T^s\) 的模 \(p^n\) 元素给出，且随 \(n\) 相容。
故它是真正的 \(p\)-可除群幂等元：
\[
\boxed{\quad
\mathcal J[p^\infty]
 =\mathcal G_1\times\mathcal G_{\rm rest}.
\quad}
\tag{1029.13}
\]
其 Hodge 格和 Lie 格都是原格的整 direct summands。
它与原 \(\delta\) 交换。
这是 \(p\)-进端环中的类型块，不要求它来自
\(\operatorname{End}_{\mathbf Q}^0(J)\) 的一个有理幂等元；
\(r=1\) 的其它 \(\mathbf Q\)-Galois 共轭类型没有被冒称不存在。

现在才将惯性型与特殊 Hodge 空间比较。
\(\mathcal G_1\) 的特殊 Dieudonné crystal 在反转 \(p\) 后，
通过原良好模型的 crystalline comparison 和 descent data，
只有惯性特征值 \(\xi^m,\xi^{-m}\)；
\(\mathcal G_{\rm rest}\) 没有这两个值。
惯性阶 \(e_0\) 与 \(p\) 互素，整 character projectors
保持 crystal 格并与模 \(p\) 约化交换。
因此同样的角色排除对其特殊 de Rham 及 Hodge 子商成立。

R1018/R1023 已完整计算原特殊 Hodge 权：
\[
m\le w_i<pm=e_0-m;
\]
权 \(m\) 恰来自全部 \(e_s=1\) 尾的底层，而权
\(-m=e_0-m\) 根本不存在。
所以
\[
\boxed{\quad
(e_1\omega_{\mathcal J})\otimes k
  =(\omega_{\mathcal J}\otimes k)_{w=m}.
\quad}
\tag{1029.14}
\]
特别地 \(e_1\) 在全部原底 Hodge 空间及其对偶方向上为恒等。
论证先取得 (1029.13) 的整分裂，再对特殊 crystal 取角色；
未由一个 Weil–Deligne 型直接猜 generic Hodge filtration。

由单位 character 平均及 Nakayama，
\(e_1\omega_{\mathcal J}\) 有一组整基 \(\Omega_i\)，每个满足
\[
\sigma^*\Omega_i=\xi^m\Omega_i.
\tag{1029.15}
\]
若该块内两个权 \(m\) 的提升具有相同特殊纤维，写其差为
\(\sum a_i\Omega_i\)，则
\(\sigma(a_i)=a_i\)。
于是 \(a_i\in R^\sigma=W(k)\)；其模 \(\pi_0\) 为零，
准确意味着 \(a_i\in pW(k)\)。
故
\[
\boxed{\quad
\text{该类型块内，同一底 Hodge 向量的权 }m
\text{ 整提升模 }p\text{ 唯一。}
\quad}
\tag{1029.16}
\]
若先只取有限非分歧底域，则 \(W(k)\) 在此式读作那个实际
非分歧整数环；结论不变。

## 6. 保留原首对数和真实非 CM 来源

由 (1029.14)，\(e_1\) 在 R1023 的原首层上作用为一：
\[
\boxed{\quad
e_1\log P\equiv\log P
 \equiv\varepsilon\sum_s
       \theta_s\bigl(\lambda(s)+R_p(s)\bigr)f_s
       \pmod{\pi_0^{m+1}}.
\quad}
\tag{1029.17}
\]
\(\lambda,R_p,\theta_s,f_s\) 全保留 R1023 的实际定义。
式中没有删除 degree-\(p\) log 返回项或其跨尾分量。

在扩张底环后的 Lie 格中取 R1026 的原线性 projector
\[
e_-=(1+\zeta\delta_*+\zeta^2\delta_*^2)/3.
\tag{1029.18}
\]
它与 \(e_1\) 交换。
这里 \(e_-\) 是含外部 \(R\) 系数的 Lie／Hodge projector；
不据此另称它为一个 \(p\)-可除群自同态。
真正可直接作用于群的 new projector 是
\(e_{\rm new}=1-N/3\)，它属于原端环的 \(\mathbf Z_p\)-完备化，
而且 \(e_{\rm new}P=P\)。

R1026 的同一个明确定义绝对常数 \(C_*\) 给
\[
\boxed{\quad
e_-e_1\log P\in
 \pi_0^m e_-\operatorname{Lie}(\mathcal G_1\cap
                                      \mathcal G_{\rm new})
 \setminus
 \pi_0^{m+1} e_-\operatorname{Lie}(\mathcal G_1\cap
                                      \mathcal G_{\rm new}),
 \qquad p>C_* .
\quad}
\tag{1029.19}
\]
这里交记号指两个交换整幂等元定义的共同 direct factor。
这是实际整类型块里的本原性。
R575/R1010/R1026 已付清全部 CM 新成分的原
\(\delta=\zeta\) Hodge 方向，故 (1029.18) 杀其 Lie 分量。
因此 (1029.19) 有真正非 CM generic 来源。

特别地，从实际 Hecke 分解可选择一个非 CM canonical 成分，
它在某个 \(p\)-进系数嵌入具有 \(\tau_1\)，原点差在该成分
投影非挠。
对该成分沿 R1011 §§2–5 的同一三次限制标量及简单商构造，
得到真实有理半秩商 \(C\)。
若仅使用 R1011 已登记的数值范围，可取
\(p>\max(C_*,431)\)。
这不是任意指定简单商的首对数单位结论：该商的实际 Néron
投影、同源尺度和 CM jet 的相对整格仍须核算。

## 7. R1028 的提升差在类型块内如何消失

R1028 的原中心提升 \(\Omega_I\) 有权
\(w_I=e_0-(p+1)\)。
在 (1029.15) 的基中写 \(e_1\Omega_I\)，其系数的
完整惯性权必须为
\[
w_I-m=e_0-3m-2 .
\]
因此
\[
e_1\Omega_I\in\pi_0^{e_0-3m-2}
                    e_1\omega_{\mathcal J},\qquad
\boxed{\quad
e_1\bigl(\pi_0^{3m+2}\Omega_I\bigr)
       \in p\,e_1\omega_{\mathcal J}.
\quad}
\tag{1029.20}
\]
因为 \(e_0>4m\)，R1028 所列任意同特殊纤维提升差，
在施加真正 \(e_1\) 后不再改变 \(\varepsilon^4\) 阶的 jet。
这与该块内的模 \(p\) 唯一性 (1029.16) 一致。

准确剩余问题是求实际 \(e_1\Omega\) 的非齐次首 jet；
(1029.20) 不说它等于一个未经 \(e_1\) 处理的参考
\(\Omega\) 的 jet，也不说 R1028 的参考修正系数自动为零。
原对数列与实际 CM Abel 列的相对行列式／统一尾项，
仍是接续任务。O0 的完整全局覆盖亦没有被本篇取消。

## 来源与审核范围

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)、
  [R1008](R1008-wild-inertia-and-all-rational-correspondence-centralization.md)：
  原 canonical tame 水平、准确三次扭曲和全自守谱范围。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)、
  [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)、
  [R1026](R1026-original-single-remainder-and-integral-CM-annihilating-log-direction.md)：
  全部原 Hodge 权、完整首 log 和负 deck 首向量的实际本原性。
- [R1028](R1028-original-Igusa-Kummer-model-and-same-order-CM-jet-correction.md)：
  同一个中心提升及其 \(\pi_0^{3m+2}\) 修正。
- Miyauchi–Yamauchi，
  *A remark on conductor, depth and principal congruence subgroups*，
  J. Algebra 592 (2022), 424–434，
  [作者公开版](https://arxiv.org/pdf/2107.08130)，
  Theorems 1.1–1.2；本文已重新核对其一般局部域版本。
- Mercuri–Schoof，
  *Modular forms invariant under non-split Cartan subgroups*，
  Math. Comp. 89 (2020), 1969–1991，
  [作者正式 offprint](https://reneschoof.github.io/mcom3503.pdf)，
  §2、Proposition 2.1、§3.2：完整四类与原正规化子奇偶条件。
  本文另按原 \(C,Cw\) character 均值直接证明所用符号。
- David Savitt，
  *On a conjecture of Conrad, Diamond, and Taylor*，
  [作者 corrected 全文](https://math.jhu.edu/~savitt/papers/pdfs/cdt_corrected.pdf)，
  Theorems 6.11–6.12、Corollary 6.15、Remark 6.17。
  使用后者明确覆盖的任意整格半单化，不挪用更强的扩张分类。
- Takeshi Saito，*Modular forms and p-adic Hodge theory*，
  Invent. Math. 129 (1997), 607–620，
  [正式 DOI](https://doi.org/10.1007/s002220050175)。
  本次未取得该原刊全文；实际读到作者自己的
  [Galois representations in arithmetic geometry II](https://www.ms.u-tokyo.ac.jp/~t-saito/pp/GR2.pdf)，
  §2.3 末尾、PDF 第10页，明确陈述 elliptic modular forms
  的 \(p=\ell\) local–global compatibility 并引用本人上述定理。
  亦与 Savitt §6.4 对此输入的使用相符；未将 Hilbert 版
  \([F:\mathbf Q]>1\) 的独立范围硬套到 \(\mathbf Q\)。

global_route 与 root 纸面逐项核完整局部类型、character 奇偶、
全部剩余惯性等式、split Hecke 的域与剩余位、有限整代数分解、
真实 \(p\)-可除群延伸、特殊 crystal 与 Hodge 的顺序、
底 log 保留和 (1029.20) 的完整次数。
本篇没有数学程序或有限素数扫描。
Serre 主目标仍 OPEN。
